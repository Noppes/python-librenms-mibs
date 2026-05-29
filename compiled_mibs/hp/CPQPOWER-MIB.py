# SNMP MIB module (CPQPOWER-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\hp\CPQPOWER-MIB

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

(compaq,) = mibBuilder.importSymbols(
    "CPQHOST-MIB",
    "compaq")

(ifDescr,
 ifIndex) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifDescr",
    "ifIndex")

(ModuleCompliance,
 NotificationGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup")

(sysContact,
 sysDescr,
 sysLocation,
 sysName) = mibBuilder.importSymbols(
    "SNMPv2-MIB",
    "sysContact",
    "sysDescr",
    "sysLocation",
    "sysName")

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
 NotificationType,
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
    "NotificationType",
    "TimeTicks",
    "Unsigned32",
    "iso")

(DisplayString,
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CpqPower_ObjectIdentity = ObjectIdentity
cpqPower = _CpqPower_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 165)
)
_PowerDevice_ObjectIdentity = ObjectIdentity
powerDevice = _PowerDevice_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 165, 1)
)
_TrapInfo_ObjectIdentity = ObjectIdentity
trapInfo = _TrapInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 165, 1, 1)
)
_TrapCode_Type = Integer32
_TrapCode_Object = MibScalar
trapCode = _TrapCode_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 1, 1, 1),
    _TrapCode_Type()
)
trapCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trapCode.setStatus("mandatory")


class _TrapDescription_Type(DisplayString):
    """Custom type trapDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_TrapDescription_Type.__name__ = "DisplayString"
_TrapDescription_Object = MibScalar
trapDescription = _TrapDescription_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 1, 1, 2),
    _TrapDescription_Type()
)
trapDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trapDescription.setStatus("mandatory")


class _TrapDeviceMgmtUrl_Type(DisplayString):
    """Custom type trapDeviceMgmtUrl based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_TrapDeviceMgmtUrl_Type.__name__ = "DisplayString"
_TrapDeviceMgmtUrl_Object = MibScalar
trapDeviceMgmtUrl = _TrapDeviceMgmtUrl_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 1, 1, 3),
    _TrapDeviceMgmtUrl_Type()
)
trapDeviceMgmtUrl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trapDeviceMgmtUrl.setStatus("mandatory")


class _TrapDeviceDetails_Type(DisplayString):
    """Custom type trapDeviceDetails based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_TrapDeviceDetails_Type.__name__ = "DisplayString"
_TrapDeviceDetails_Object = MibScalar
trapDeviceDetails = _TrapDeviceDetails_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 1, 1, 4),
    _TrapDeviceDetails_Type()
)
trapDeviceDetails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trapDeviceDetails.setStatus("mandatory")


class _TrapDeviceName_Type(DisplayString):
    """Custom type trapDeviceName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_TrapDeviceName_Type.__name__ = "DisplayString"
_TrapDeviceName_Object = MibScalar
trapDeviceName = _TrapDeviceName_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 1, 1, 5),
    _TrapDeviceName_Type()
)
trapDeviceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trapDeviceName.setStatus("mandatory")
_ManagementModuleIdent_ObjectIdentity = ObjectIdentity
managementModuleIdent = _ManagementModuleIdent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 165, 1, 2)
)
_DeviceManufacturer_Type = DisplayString
_DeviceManufacturer_Object = MibScalar
deviceManufacturer = _DeviceManufacturer_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 1, 2, 1),
    _DeviceManufacturer_Type()
)
deviceManufacturer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deviceManufacturer.setStatus("mandatory")
_DeviceModel_Type = DisplayString
_DeviceModel_Object = MibScalar
deviceModel = _DeviceModel_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 1, 2, 2),
    _DeviceModel_Type()
)
deviceModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deviceModel.setStatus("mandatory")
_DeviceFirmwareVersion_Type = DisplayString
_DeviceFirmwareVersion_Object = MibScalar
deviceFirmwareVersion = _DeviceFirmwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 1, 2, 3),
    _DeviceFirmwareVersion_Type()
)
deviceFirmwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deviceFirmwareVersion.setStatus("mandatory")
_DeviceHardwareVersion_Type = DisplayString
_DeviceHardwareVersion_Object = MibScalar
deviceHardwareVersion = _DeviceHardwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 1, 2, 4),
    _DeviceHardwareVersion_Type()
)
deviceHardwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deviceHardwareVersion.setStatus("mandatory")
_DeviceIdentName_Type = DisplayString
_DeviceIdentName_Object = MibScalar
deviceIdentName = _DeviceIdentName_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 1, 2, 5),
    _DeviceIdentName_Type()
)
deviceIdentName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    deviceIdentName.setStatus("mandatory")
_DevicePartNumber_Type = DisplayString
_DevicePartNumber_Object = MibScalar
devicePartNumber = _DevicePartNumber_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 1, 2, 6),
    _DevicePartNumber_Type()
)
devicePartNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    devicePartNumber.setStatus("mandatory")
_DeviceSerialNumber_Type = DisplayString
_DeviceSerialNumber_Object = MibScalar
deviceSerialNumber = _DeviceSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 1, 2, 7),
    _DeviceSerialNumber_Type()
)
deviceSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deviceSerialNumber.setStatus("mandatory")
_DeviceMACAddress_Type = DisplayString
_DeviceMACAddress_Object = MibScalar
deviceMACAddress = _DeviceMACAddress_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 1, 2, 8),
    _DeviceMACAddress_Type()
)
deviceMACAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deviceMACAddress.setStatus("mandatory")
_Pdu_ObjectIdentity = ObjectIdentity
pdu = _Pdu_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 165, 2)
)
_PduIdent_ObjectIdentity = ObjectIdentity
pduIdent = _PduIdent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 165, 2, 1)
)


class _NumOfPdu_Type(Integer32):
    """Custom type numOfPdu based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_NumOfPdu_Type.__name__ = "Integer32"
_NumOfPdu_Object = MibScalar
numOfPdu = _NumOfPdu_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 2, 1, 1),
    _NumOfPdu_Type()
)
numOfPdu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    numOfPdu.setStatus("mandatory")
_PduIdentTable_Object = MibTable
pduIdentTable = _PduIdentTable_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 2, 1, 2)
)
if mibBuilder.loadTexts:
    pduIdentTable.setStatus("mandatory")
_PduIdentEntry_Object = MibTableRow
pduIdentEntry = _PduIdentEntry_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 2, 1, 2, 1)
)
pduIdentEntry.setIndexNames(
    (0, "CPQPOWER-MIB", "pduIdentIndex"),
)
if mibBuilder.loadTexts:
    pduIdentEntry.setStatus("mandatory")


class _PduIdentIndex_Type(Integer32):
    """Custom type pduIdentIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_PduIdentIndex_Type.__name__ = "Integer32"
_PduIdentIndex_Object = MibTableColumn
pduIdentIndex = _PduIdentIndex_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 2, 1, 2, 1, 1),
    _PduIdentIndex_Type()
)
pduIdentIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduIdentIndex.setStatus("mandatory")


class _PduName_Type(DisplayString):
    """Custom type pduName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_PduName_Type.__name__ = "DisplayString"
_PduName_Object = MibTableColumn
pduName = _PduName_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 2, 1, 2, 1, 2),
    _PduName_Type()
)
pduName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduName.setStatus("mandatory")


class _PduModel_Type(DisplayString):
    """Custom type pduModel based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_PduModel_Type.__name__ = "DisplayString"
_PduModel_Object = MibTableColumn
pduModel = _PduModel_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 2, 1, 2, 1, 3),
    _PduModel_Type()
)
pduModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduModel.setStatus("mandatory")


class _PduManufacturer_Type(DisplayString):
    """Custom type pduManufacturer based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_PduManufacturer_Type.__name__ = "DisplayString"
_PduManufacturer_Object = MibTableColumn
pduManufacturer = _PduManufacturer_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 2, 1, 2, 1, 4),
    _PduManufacturer_Type()
)
pduManufacturer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduManufacturer.setStatus("mandatory")


class _PduFirmwareVersion_Type(DisplayString):
    """Custom type pduFirmwareVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_PduFirmwareVersion_Type.__name__ = "DisplayString"
_PduFirmwareVersion_Object = MibTableColumn
pduFirmwareVersion = _PduFirmwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 2, 1, 2, 1, 5),
    _PduFirmwareVersion_Type()
)
pduFirmwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduFirmwareVersion.setStatus("mandatory")


class _PduPartNumber_Type(DisplayString):
    """Custom type pduPartNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_PduPartNumber_Type.__name__ = "DisplayString"
_PduPartNumber_Object = MibTableColumn
pduPartNumber = _PduPartNumber_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 2, 1, 2, 1, 6),
    _PduPartNumber_Type()
)
pduPartNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduPartNumber.setStatus("mandatory")


class _PduSerialNumber_Type(DisplayString):
    """Custom type pduSerialNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_PduSerialNumber_Type.__name__ = "DisplayString"
_PduSerialNumber_Object = MibTableColumn
pduSerialNumber = _PduSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 2, 1, 2, 1, 7),
    _PduSerialNumber_Type()
)
pduSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduSerialNumber.setStatus("mandatory")


class _PduStatus_Type(Integer32):
    """Custom type pduStatus based on Integer32"""
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
        *(("other", 1),
          ("ok", 2),
          ("degraded", 3),
          ("failed", 4))
    )


_PduStatus_Type.__name__ = "Integer32"
_PduStatus_Object = MibTableColumn
pduStatus = _PduStatus_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 2, 1, 2, 1, 8),
    _PduStatus_Type()
)
pduStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduStatus.setStatus("mandatory")


class _PduControllable_Type(Integer32):
    """Custom type pduControllable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("yes", 1),
          ("no", 2))
    )


_PduControllable_Type.__name__ = "Integer32"
_PduControllable_Object = MibTableColumn
pduControllable = _PduControllable_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 2, 1, 2, 1, 9),
    _PduControllable_Type()
)
pduControllable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduControllable.setStatus("mandatory")
_PduInput_ObjectIdentity = ObjectIdentity
pduInput = _PduInput_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 165, 2, 2)
)
_PduInputTable_Object = MibTable
pduInputTable = _PduInputTable_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 2, 2, 1)
)
if mibBuilder.loadTexts:
    pduInputTable.setStatus("mandatory")
_PduInputEntry_Object = MibTableRow
pduInputEntry = _PduInputEntry_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 2, 2, 1, 1)
)
pduInputEntry.setIndexNames(
    (0, "CPQPOWER-MIB", "pduInputIndex"),
)
if mibBuilder.loadTexts:
    pduInputEntry.setStatus("mandatory")


class _PduInputIndex_Type(Integer32):
    """Custom type pduInputIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_PduInputIndex_Type.__name__ = "Integer32"
_PduInputIndex_Object = MibTableColumn
pduInputIndex = _PduInputIndex_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 2, 2, 1, 1, 1),
    _PduInputIndex_Type()
)
pduInputIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduInputIndex.setStatus("mandatory")


class _InputVoltage_Type(Integer32):
    """Custom type inputVoltage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_InputVoltage_Type.__name__ = "Integer32"
_InputVoltage_Object = MibTableColumn
inputVoltage = _InputVoltage_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 2, 2, 1, 1, 2),
    _InputVoltage_Type()
)
inputVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inputVoltage.setStatus("mandatory")


class _InputCurrent_Type(Integer32):
    """Custom type inputCurrent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_InputCurrent_Type.__name__ = "Integer32"
_InputCurrent_Object = MibTableColumn
inputCurrent = _InputCurrent_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 2, 2, 1, 1, 3),
    _InputCurrent_Type()
)
inputCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inputCurrent.setStatus("mandatory")
_PduOutput_ObjectIdentity = ObjectIdentity
pduOutput = _PduOutput_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 165, 2, 3)
)
_PduOutputTable_Object = MibTable
pduOutputTable = _PduOutputTable_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 2, 3, 1)
)
if mibBuilder.loadTexts:
    pduOutputTable.setStatus("mandatory")
_PduOutputEntry_Object = MibTableRow
pduOutputEntry = _PduOutputEntry_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 2, 3, 1, 1)
)
pduOutputEntry.setIndexNames(
    (0, "CPQPOWER-MIB", "pduOutputIndex"),
)
if mibBuilder.loadTexts:
    pduOutputEntry.setStatus("mandatory")


class _PduOutputIndex_Type(Integer32):
    """Custom type pduOutputIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_PduOutputIndex_Type.__name__ = "Integer32"
_PduOutputIndex_Object = MibTableColumn
pduOutputIndex = _PduOutputIndex_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 2, 3, 1, 1, 1),
    _PduOutputIndex_Type()
)
pduOutputIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduOutputIndex.setStatus("mandatory")


class _PduOutputLoad_Type(Integer32):
    """Custom type pduOutputLoad based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 200),
    )


_PduOutputLoad_Type.__name__ = "Integer32"
_PduOutputLoad_Object = MibTableColumn
pduOutputLoad = _PduOutputLoad_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 2, 3, 1, 1, 2),
    _PduOutputLoad_Type()
)
pduOutputLoad.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduOutputLoad.setStatus("mandatory")
_PduOutputHeat_Type = Integer32
_PduOutputHeat_Object = MibTableColumn
pduOutputHeat = _PduOutputHeat_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 2, 3, 1, 1, 3),
    _PduOutputHeat_Type()
)
pduOutputHeat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduOutputHeat.setStatus("mandatory")
_PduOutputPower_Type = Integer32
_PduOutputPower_Object = MibTableColumn
pduOutputPower = _PduOutputPower_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 2, 3, 1, 1, 4),
    _PduOutputPower_Type()
)
pduOutputPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduOutputPower.setStatus("mandatory")
_PduOutputNumBreakers_Type = Integer32
_PduOutputNumBreakers_Object = MibTableColumn
pduOutputNumBreakers = _PduOutputNumBreakers_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 2, 3, 1, 1, 5),
    _PduOutputNumBreakers_Type()
)
pduOutputNumBreakers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduOutputNumBreakers.setStatus("mandatory")
_PduOutputBreakerTable_Object = MibTable
pduOutputBreakerTable = _PduOutputBreakerTable_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 2, 3, 2)
)
if mibBuilder.loadTexts:
    pduOutputBreakerTable.setStatus("mandatory")
_PduOutputBreakerEntry_Object = MibTableRow
pduOutputBreakerEntry = _PduOutputBreakerEntry_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 2, 3, 2, 1)
)
pduOutputBreakerEntry.setIndexNames(
    (0, "CPQPOWER-MIB", "pduOutputIndex"),
    (0, "CPQPOWER-MIB", "breakerIndex"),
)
if mibBuilder.loadTexts:
    pduOutputBreakerEntry.setStatus("mandatory")


class _BreakerIndex_Type(Integer32):
    """Custom type breakerIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_BreakerIndex_Type.__name__ = "Integer32"
_BreakerIndex_Object = MibTableColumn
breakerIndex = _BreakerIndex_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 2, 3, 2, 1, 1),
    _BreakerIndex_Type()
)
breakerIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    breakerIndex.setStatus("mandatory")
_BreakerVoltage_Type = Integer32
_BreakerVoltage_Object = MibTableColumn
breakerVoltage = _BreakerVoltage_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 2, 3, 2, 1, 2),
    _BreakerVoltage_Type()
)
breakerVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    breakerVoltage.setStatus("mandatory")
_BreakerCurrent_Type = Integer32
_BreakerCurrent_Object = MibTableColumn
breakerCurrent = _BreakerCurrent_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 2, 3, 2, 1, 3),
    _BreakerCurrent_Type()
)
breakerCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    breakerCurrent.setStatus("mandatory")
_BreakerPercentLoad_Type = Integer32
_BreakerPercentLoad_Object = MibTableColumn
breakerPercentLoad = _BreakerPercentLoad_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 2, 3, 2, 1, 4),
    _BreakerPercentLoad_Type()
)
breakerPercentLoad.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    breakerPercentLoad.setStatus("mandatory")


class _BreakerStatus_Type(Integer32):
    """Custom type breakerStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("normal", 1),
          ("overloadWarning", 2),
          ("overloadCritical", 3),
          ("voltageRangeWarning", 4),
          ("voltageRangeCritical", 5))
    )


_BreakerStatus_Type.__name__ = "Integer32"
_BreakerStatus_Object = MibTableColumn
breakerStatus = _BreakerStatus_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 2, 3, 2, 1, 5),
    _BreakerStatus_Type()
)
breakerStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    breakerStatus.setStatus("mandatory")
_Ups_ObjectIdentity = ObjectIdentity
ups = _Ups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 165, 3)
)
_UpsIdent_ObjectIdentity = ObjectIdentity
upsIdent = _UpsIdent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 165, 3, 1)
)


class _UpsIdentManufacturer_Type(DisplayString):
    """Custom type upsIdentManufacturer based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_UpsIdentManufacturer_Type.__name__ = "DisplayString"
_UpsIdentManufacturer_Object = MibScalar
upsIdentManufacturer = _UpsIdentManufacturer_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 3, 1, 1),
    _UpsIdentManufacturer_Type()
)
upsIdentManufacturer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsIdentManufacturer.setStatus("mandatory")


class _UpsIdentModel_Type(DisplayString):
    """Custom type upsIdentModel based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_UpsIdentModel_Type.__name__ = "DisplayString"
_UpsIdentModel_Object = MibScalar
upsIdentModel = _UpsIdentModel_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 3, 1, 2),
    _UpsIdentModel_Type()
)
upsIdentModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsIdentModel.setStatus("mandatory")


class _UpsIdentSoftwareVersions_Type(DisplayString):
    """Custom type upsIdentSoftwareVersions based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_UpsIdentSoftwareVersions_Type.__name__ = "DisplayString"
_UpsIdentSoftwareVersions_Object = MibScalar
upsIdentSoftwareVersions = _UpsIdentSoftwareVersions_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 3, 1, 3),
    _UpsIdentSoftwareVersions_Type()
)
upsIdentSoftwareVersions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsIdentSoftwareVersions.setStatus("mandatory")


class _UpsIdentOemCode_Type(Integer32):
    """Custom type upsIdentOemCode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_UpsIdentOemCode_Type.__name__ = "Integer32"
_UpsIdentOemCode_Object = MibScalar
upsIdentOemCode = _UpsIdentOemCode_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 3, 1, 4),
    _UpsIdentOemCode_Type()
)
upsIdentOemCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsIdentOemCode.setStatus("mandatory")
_UpsBattery_ObjectIdentity = ObjectIdentity
upsBattery = _UpsBattery_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 165, 3, 2)
)


class _UpsBatTimeRemaining_Type(Integer32):
    """Custom type upsBatTimeRemaining based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_UpsBatTimeRemaining_Type.__name__ = "Integer32"
_UpsBatTimeRemaining_Object = MibScalar
upsBatTimeRemaining = _UpsBatTimeRemaining_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 3, 2, 1),
    _UpsBatTimeRemaining_Type()
)
upsBatTimeRemaining.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsBatTimeRemaining.setStatus("mandatory")


class _UpsBatVoltage_Type(Integer32):
    """Custom type upsBatVoltage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_UpsBatVoltage_Type.__name__ = "Integer32"
_UpsBatVoltage_Object = MibScalar
upsBatVoltage = _UpsBatVoltage_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 3, 2, 2),
    _UpsBatVoltage_Type()
)
upsBatVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsBatVoltage.setStatus("mandatory")


class _UpsBatCurrent_Type(Integer32):
    """Custom type upsBatCurrent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_UpsBatCurrent_Type.__name__ = "Integer32"
_UpsBatCurrent_Object = MibScalar
upsBatCurrent = _UpsBatCurrent_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 3, 2, 3),
    _UpsBatCurrent_Type()
)
upsBatCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsBatCurrent.setStatus("mandatory")


class _UpsBatCapacity_Type(Integer32):
    """Custom type upsBatCapacity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_UpsBatCapacity_Type.__name__ = "Integer32"
_UpsBatCapacity_Object = MibScalar
upsBatCapacity = _UpsBatCapacity_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 3, 2, 4),
    _UpsBatCapacity_Type()
)
upsBatCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsBatCapacity.setStatus("mandatory")


class _UpsBatteryAbmStatus_Type(Integer32):
    """Custom type upsBatteryAbmStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("batteryCharging", 1),
          ("batteryDischarging", 2),
          ("batteryFloating", 3),
          ("batteryResting", 4),
          ("unknown", 5))
    )


_UpsBatteryAbmStatus_Type.__name__ = "Integer32"
_UpsBatteryAbmStatus_Object = MibScalar
upsBatteryAbmStatus = _UpsBatteryAbmStatus_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 3, 2, 5),
    _UpsBatteryAbmStatus_Type()
)
upsBatteryAbmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsBatteryAbmStatus.setStatus("mandatory")
_UpsInput_ObjectIdentity = ObjectIdentity
upsInput = _UpsInput_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 165, 3, 3)
)


class _UpsInputFrequency_Type(Integer32):
    """Custom type upsInputFrequency based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_UpsInputFrequency_Type.__name__ = "Integer32"
_UpsInputFrequency_Object = MibScalar
upsInputFrequency = _UpsInputFrequency_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 3, 3, 1),
    _UpsInputFrequency_Type()
)
upsInputFrequency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsInputFrequency.setStatus("mandatory")
_UpsInputLineBads_Type = Counter32
_UpsInputLineBads_Object = MibScalar
upsInputLineBads = _UpsInputLineBads_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 3, 3, 2),
    _UpsInputLineBads_Type()
)
upsInputLineBads.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsInputLineBads.setStatus("mandatory")


class _UpsInputNumPhases_Type(Integer32):
    """Custom type upsInputNumPhases based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 6),
    )


_UpsInputNumPhases_Type.__name__ = "Integer32"
_UpsInputNumPhases_Object = MibScalar
upsInputNumPhases = _UpsInputNumPhases_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 3, 3, 3),
    _UpsInputNumPhases_Type()
)
upsInputNumPhases.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsInputNumPhases.setStatus("mandatory")
_UpsInputTable_Object = MibTable
upsInputTable = _UpsInputTable_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 3, 3, 4)
)
if mibBuilder.loadTexts:
    upsInputTable.setStatus("mandatory")
_UpsInputEntry_Object = MibTableRow
upsInputEntry = _UpsInputEntry_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 3, 3, 4, 1)
)
upsInputEntry.setIndexNames(
    (0, "CPQPOWER-MIB", "upsInputPhase"),
)
if mibBuilder.loadTexts:
    upsInputEntry.setStatus("mandatory")


class _UpsInputPhase_Type(Integer32):
    """Custom type upsInputPhase based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 6),
    )


_UpsInputPhase_Type.__name__ = "Integer32"
_UpsInputPhase_Object = MibTableColumn
upsInputPhase = _UpsInputPhase_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 3, 3, 4, 1, 1),
    _UpsInputPhase_Type()
)
upsInputPhase.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsInputPhase.setStatus("mandatory")


class _UpsInputVoltage_Type(Integer32):
    """Custom type upsInputVoltage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_UpsInputVoltage_Type.__name__ = "Integer32"
_UpsInputVoltage_Object = MibTableColumn
upsInputVoltage = _UpsInputVoltage_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 3, 3, 4, 1, 2),
    _UpsInputVoltage_Type()
)
upsInputVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsInputVoltage.setStatus("mandatory")


class _UpsInputCurrent_Type(Integer32):
    """Custom type upsInputCurrent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_UpsInputCurrent_Type.__name__ = "Integer32"
_UpsInputCurrent_Object = MibTableColumn
upsInputCurrent = _UpsInputCurrent_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 3, 3, 4, 1, 3),
    _UpsInputCurrent_Type()
)
upsInputCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsInputCurrent.setStatus("mandatory")


class _UpsInputWatts_Type(Integer32):
    """Custom type upsInputWatts based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_UpsInputWatts_Type.__name__ = "Integer32"
_UpsInputWatts_Object = MibTableColumn
upsInputWatts = _UpsInputWatts_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 3, 3, 4, 1, 4),
    _UpsInputWatts_Type()
)
upsInputWatts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsInputWatts.setStatus("mandatory")


class _UpsInputSource_Type(Integer32):
    """Custom type upsInputSource based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("none", 2),
          ("primaryUtility", 3),
          ("bypassFeed", 4),
          ("secondaryUtility", 5),
          ("generator", 6),
          ("flywheel", 7),
          ("fuelcell", 8))
    )


_UpsInputSource_Type.__name__ = "Integer32"
_UpsInputSource_Object = MibScalar
upsInputSource = _UpsInputSource_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 3, 3, 5),
    _UpsInputSource_Type()
)
upsInputSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsInputSource.setStatus("mandatory")
_UpsOutput_ObjectIdentity = ObjectIdentity
upsOutput = _UpsOutput_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 165, 3, 4)
)


class _UpsOutputLoad_Type(Integer32):
    """Custom type upsOutputLoad based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 200),
    )


_UpsOutputLoad_Type.__name__ = "Integer32"
_UpsOutputLoad_Object = MibScalar
upsOutputLoad = _UpsOutputLoad_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 3, 4, 1),
    _UpsOutputLoad_Type()
)
upsOutputLoad.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsOutputLoad.setStatus("mandatory")


class _UpsOutputFrequency_Type(Integer32):
    """Custom type upsOutputFrequency based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_UpsOutputFrequency_Type.__name__ = "Integer32"
_UpsOutputFrequency_Object = MibScalar
upsOutputFrequency = _UpsOutputFrequency_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 3, 4, 2),
    _UpsOutputFrequency_Type()
)
upsOutputFrequency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsOutputFrequency.setStatus("mandatory")


class _UpsOutputNumPhases_Type(Integer32):
    """Custom type upsOutputNumPhases based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 6),
    )


_UpsOutputNumPhases_Type.__name__ = "Integer32"
_UpsOutputNumPhases_Object = MibScalar
upsOutputNumPhases = _UpsOutputNumPhases_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 3, 4, 3),
    _UpsOutputNumPhases_Type()
)
upsOutputNumPhases.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsOutputNumPhases.setStatus("mandatory")
_UpsOutputTable_Object = MibTable
upsOutputTable = _UpsOutputTable_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 3, 4, 4)
)
if mibBuilder.loadTexts:
    upsOutputTable.setStatus("mandatory")
_UpsOutputEntry_Object = MibTableRow
upsOutputEntry = _UpsOutputEntry_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 3, 4, 4, 1)
)
upsOutputEntry.setIndexNames(
    (0, "CPQPOWER-MIB", "upsOutputPhase"),
)
if mibBuilder.loadTexts:
    upsOutputEntry.setStatus("mandatory")


class _UpsOutputPhase_Type(Integer32):
    """Custom type upsOutputPhase based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 6),
    )


_UpsOutputPhase_Type.__name__ = "Integer32"
_UpsOutputPhase_Object = MibTableColumn
upsOutputPhase = _UpsOutputPhase_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 3, 4, 4, 1, 1),
    _UpsOutputPhase_Type()
)
upsOutputPhase.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsOutputPhase.setStatus("mandatory")


class _UpsOutputVoltage_Type(Integer32):
    """Custom type upsOutputVoltage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_UpsOutputVoltage_Type.__name__ = "Integer32"
_UpsOutputVoltage_Object = MibTableColumn
upsOutputVoltage = _UpsOutputVoltage_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 3, 4, 4, 1, 2),
    _UpsOutputVoltage_Type()
)
upsOutputVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsOutputVoltage.setStatus("mandatory")


class _UpsOutputCurrent_Type(Integer32):
    """Custom type upsOutputCurrent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_UpsOutputCurrent_Type.__name__ = "Integer32"
_UpsOutputCurrent_Object = MibTableColumn
upsOutputCurrent = _UpsOutputCurrent_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 3, 4, 4, 1, 3),
    _UpsOutputCurrent_Type()
)
upsOutputCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsOutputCurrent.setStatus("mandatory")


class _UpsOutputWatts_Type(Integer32):
    """Custom type upsOutputWatts based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_UpsOutputWatts_Type.__name__ = "Integer32"
_UpsOutputWatts_Object = MibTableColumn
upsOutputWatts = _UpsOutputWatts_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 3, 4, 4, 1, 4),
    _UpsOutputWatts_Type()
)
upsOutputWatts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsOutputWatts.setStatus("mandatory")


class _UpsOutputSource_Type(Integer32):
    """Custom type upsOutputSource based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("none", 2),
          ("normal", 3),
          ("bypass", 4),
          ("battery", 5),
          ("booster", 6),
          ("reducer", 7),
          ("parallelCapacity", 8),
          ("parallelRedundant", 9),
          ("highEfficiencyMode", 10))
    )


_UpsOutputSource_Type.__name__ = "Integer32"
_UpsOutputSource_Object = MibScalar
upsOutputSource = _UpsOutputSource_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 3, 4, 5),
    _UpsOutputSource_Type()
)
upsOutputSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsOutputSource.setStatus("mandatory")
_UpsBypass_ObjectIdentity = ObjectIdentity
upsBypass = _UpsBypass_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 165, 3, 5)
)


class _UpsBypassFrequency_Type(Integer32):
    """Custom type upsBypassFrequency based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_UpsBypassFrequency_Type.__name__ = "Integer32"
_UpsBypassFrequency_Object = MibScalar
upsBypassFrequency = _UpsBypassFrequency_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 3, 5, 1),
    _UpsBypassFrequency_Type()
)
upsBypassFrequency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsBypassFrequency.setStatus("mandatory")


class _UpsBypassNumPhases_Type(Integer32):
    """Custom type upsBypassNumPhases based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 6),
    )


_UpsBypassNumPhases_Type.__name__ = "Integer32"
_UpsBypassNumPhases_Object = MibScalar
upsBypassNumPhases = _UpsBypassNumPhases_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 3, 5, 2),
    _UpsBypassNumPhases_Type()
)
upsBypassNumPhases.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsBypassNumPhases.setStatus("mandatory")
_UpsBypassTable_Object = MibTable
upsBypassTable = _UpsBypassTable_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 3, 5, 3)
)
if mibBuilder.loadTexts:
    upsBypassTable.setStatus("mandatory")
_UpsBypassEntry_Object = MibTableRow
upsBypassEntry = _UpsBypassEntry_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 3, 5, 3, 1)
)
upsBypassEntry.setIndexNames(
    (0, "CPQPOWER-MIB", "upsBypassPhase"),
)
if mibBuilder.loadTexts:
    upsBypassEntry.setStatus("mandatory")


class _UpsBypassPhase_Type(Integer32):
    """Custom type upsBypassPhase based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 6),
    )


_UpsBypassPhase_Type.__name__ = "Integer32"
_UpsBypassPhase_Object = MibTableColumn
upsBypassPhase = _UpsBypassPhase_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 3, 5, 3, 1, 1),
    _UpsBypassPhase_Type()
)
upsBypassPhase.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsBypassPhase.setStatus("mandatory")


class _UpsBypassVoltage_Type(Integer32):
    """Custom type upsBypassVoltage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_UpsBypassVoltage_Type.__name__ = "Integer32"
_UpsBypassVoltage_Object = MibTableColumn
upsBypassVoltage = _UpsBypassVoltage_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 3, 5, 3, 1, 2),
    _UpsBypassVoltage_Type()
)
upsBypassVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsBypassVoltage.setStatus("mandatory")
_UpsEnvironment_ObjectIdentity = ObjectIdentity
upsEnvironment = _UpsEnvironment_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 165, 3, 6)
)


class _UpsEnvAmbientTemp_Type(Integer32):
    """Custom type upsEnvAmbientTemp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-100, 200),
    )


_UpsEnvAmbientTemp_Type.__name__ = "Integer32"
_UpsEnvAmbientTemp_Object = MibScalar
upsEnvAmbientTemp = _UpsEnvAmbientTemp_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 3, 6, 1),
    _UpsEnvAmbientTemp_Type()
)
upsEnvAmbientTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsEnvAmbientTemp.setStatus("mandatory")


class _UpsEnvAmbientLowerLimit_Type(Integer32):
    """Custom type upsEnvAmbientLowerLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-100, 200),
    )


_UpsEnvAmbientLowerLimit_Type.__name__ = "Integer32"
_UpsEnvAmbientLowerLimit_Object = MibScalar
upsEnvAmbientLowerLimit = _UpsEnvAmbientLowerLimit_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 3, 6, 2),
    _UpsEnvAmbientLowerLimit_Type()
)
upsEnvAmbientLowerLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsEnvAmbientLowerLimit.setStatus("mandatory")


class _UpsEnvAmbientUpperLimit_Type(Integer32):
    """Custom type upsEnvAmbientUpperLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-100, 200),
    )


_UpsEnvAmbientUpperLimit_Type.__name__ = "Integer32"
_UpsEnvAmbientUpperLimit_Object = MibScalar
upsEnvAmbientUpperLimit = _UpsEnvAmbientUpperLimit_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 3, 6, 3),
    _UpsEnvAmbientUpperLimit_Type()
)
upsEnvAmbientUpperLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsEnvAmbientUpperLimit.setStatus("mandatory")


class _UpsEnvAmbientHumidity_Type(Integer32):
    """Custom type upsEnvAmbientHumidity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_UpsEnvAmbientHumidity_Type.__name__ = "Integer32"
_UpsEnvAmbientHumidity_Object = MibScalar
upsEnvAmbientHumidity = _UpsEnvAmbientHumidity_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 3, 6, 4),
    _UpsEnvAmbientHumidity_Type()
)
upsEnvAmbientHumidity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsEnvAmbientHumidity.setStatus("mandatory")


class _UpsEnvRemoteTemp_Type(Integer32):
    """Custom type upsEnvRemoteTemp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-100, 200),
    )


_UpsEnvRemoteTemp_Type.__name__ = "Integer32"
_UpsEnvRemoteTemp_Object = MibScalar
upsEnvRemoteTemp = _UpsEnvRemoteTemp_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 3, 6, 5),
    _UpsEnvRemoteTemp_Type()
)
upsEnvRemoteTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsEnvRemoteTemp.setStatus("mandatory")


class _UpsEnvRemoteHumidity_Type(Integer32):
    """Custom type upsEnvRemoteHumidity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_UpsEnvRemoteHumidity_Type.__name__ = "Integer32"
_UpsEnvRemoteHumidity_Object = MibScalar
upsEnvRemoteHumidity = _UpsEnvRemoteHumidity_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 3, 6, 6),
    _UpsEnvRemoteHumidity_Type()
)
upsEnvRemoteHumidity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsEnvRemoteHumidity.setStatus("mandatory")


class _UpsEnvNumContacts_Type(Integer32):
    """Custom type upsEnvNumContacts based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_UpsEnvNumContacts_Type.__name__ = "Integer32"
_UpsEnvNumContacts_Object = MibScalar
upsEnvNumContacts = _UpsEnvNumContacts_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 3, 6, 7),
    _UpsEnvNumContacts_Type()
)
upsEnvNumContacts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsEnvNumContacts.setStatus("mandatory")
_UpsContactsTable_Object = MibTable
upsContactsTable = _UpsContactsTable_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 3, 6, 8)
)
if mibBuilder.loadTexts:
    upsContactsTable.setStatus("mandatory")
_UpsContactsTableEntry_Object = MibTableRow
upsContactsTableEntry = _UpsContactsTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 3, 6, 8, 1)
)
upsContactsTableEntry.setIndexNames(
    (0, "CPQPOWER-MIB", "upsContactIndex"),
)
if mibBuilder.loadTexts:
    upsContactsTableEntry.setStatus("mandatory")


class _UpsContactIndex_Type(Integer32):
    """Custom type upsContactIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_UpsContactIndex_Type.__name__ = "Integer32"
_UpsContactIndex_Object = MibTableColumn
upsContactIndex = _UpsContactIndex_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 3, 6, 8, 1, 1),
    _UpsContactIndex_Type()
)
upsContactIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsContactIndex.setStatus("mandatory")


class _UpsContactType_Type(Integer32):
    """Custom type upsContactType based on Integer32"""
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
        *(("normallyOpen", 1),
          ("normallyClosed", 2),
          ("anyChange", 3),
          ("notUsed", 4))
    )


_UpsContactType_Type.__name__ = "Integer32"
_UpsContactType_Object = MibTableColumn
upsContactType = _UpsContactType_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 3, 6, 8, 1, 2),
    _UpsContactType_Type()
)
upsContactType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsContactType.setStatus("mandatory")


class _UpsContactState_Type(Integer32):
    """Custom type upsContactState based on Integer32"""
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
        *(("open", 1),
          ("closed", 2),
          ("openWithNotice", 3),
          ("closedWithNotice", 4))
    )


_UpsContactState_Type.__name__ = "Integer32"
_UpsContactState_Object = MibTableColumn
upsContactState = _UpsContactState_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 3, 6, 8, 1, 3),
    _UpsContactState_Type()
)
upsContactState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsContactState.setStatus("mandatory")


class _UpsContactDescr_Type(DisplayString):
    """Custom type upsContactDescr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_UpsContactDescr_Type.__name__ = "DisplayString"
_UpsContactDescr_Object = MibTableColumn
upsContactDescr = _UpsContactDescr_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 3, 6, 8, 1, 4),
    _UpsContactDescr_Type()
)
upsContactDescr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsContactDescr.setStatus("mandatory")


class _UpsEnvRemoteTempLowerLimit_Type(Integer32):
    """Custom type upsEnvRemoteTempLowerLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-100, 200),
    )


_UpsEnvRemoteTempLowerLimit_Type.__name__ = "Integer32"
_UpsEnvRemoteTempLowerLimit_Object = MibScalar
upsEnvRemoteTempLowerLimit = _UpsEnvRemoteTempLowerLimit_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 3, 6, 9),
    _UpsEnvRemoteTempLowerLimit_Type()
)
upsEnvRemoteTempLowerLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsEnvRemoteTempLowerLimit.setStatus("mandatory")


class _UpsEnvRemoteTempUpperLimit_Type(Integer32):
    """Custom type upsEnvRemoteTempUpperLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-100, 200),
    )


_UpsEnvRemoteTempUpperLimit_Type.__name__ = "Integer32"
_UpsEnvRemoteTempUpperLimit_Object = MibScalar
upsEnvRemoteTempUpperLimit = _UpsEnvRemoteTempUpperLimit_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 3, 6, 10),
    _UpsEnvRemoteTempUpperLimit_Type()
)
upsEnvRemoteTempUpperLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsEnvRemoteTempUpperLimit.setStatus("mandatory")


class _UpsEnvRemoteHumidityLowerLimit_Type(Integer32):
    """Custom type upsEnvRemoteHumidityLowerLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_UpsEnvRemoteHumidityLowerLimit_Type.__name__ = "Integer32"
_UpsEnvRemoteHumidityLowerLimit_Object = MibScalar
upsEnvRemoteHumidityLowerLimit = _UpsEnvRemoteHumidityLowerLimit_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 3, 6, 11),
    _UpsEnvRemoteHumidityLowerLimit_Type()
)
upsEnvRemoteHumidityLowerLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsEnvRemoteHumidityLowerLimit.setStatus("mandatory")


class _UpsEnvRemoteHumidityUpperLimit_Type(Integer32):
    """Custom type upsEnvRemoteHumidityUpperLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_UpsEnvRemoteHumidityUpperLimit_Type.__name__ = "Integer32"
_UpsEnvRemoteHumidityUpperLimit_Object = MibScalar
upsEnvRemoteHumidityUpperLimit = _UpsEnvRemoteHumidityUpperLimit_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 3, 6, 12),
    _UpsEnvRemoteHumidityUpperLimit_Type()
)
upsEnvRemoteHumidityUpperLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsEnvRemoteHumidityUpperLimit.setStatus("mandatory")
_UpsTest_ObjectIdentity = ObjectIdentity
upsTest = _UpsTest_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 165, 3, 7)
)


class _UpsTestBattery_Type(Integer32):
    """Custom type upsTestBattery based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("startTest", 1)
    )


_UpsTestBattery_Type.__name__ = "Integer32"
_UpsTestBattery_Object = MibScalar
upsTestBattery = _UpsTestBattery_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 3, 7, 1),
    _UpsTestBattery_Type()
)
upsTestBattery.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsTestBattery.setStatus("mandatory")


class _UpsTestBatteryStatus_Type(Integer32):
    """Custom type upsTestBatteryStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 1),
          ("passed", 2),
          ("failed", 3),
          ("inProgress", 4),
          ("notSupported", 5),
          ("inhibited", 6),
          ("scheduled", 7))
    )


_UpsTestBatteryStatus_Type.__name__ = "Integer32"
_UpsTestBatteryStatus_Object = MibScalar
upsTestBatteryStatus = _UpsTestBatteryStatus_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 3, 7, 2),
    _UpsTestBatteryStatus_Type()
)
upsTestBatteryStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsTestBatteryStatus.setStatus("mandatory")


class _UpsTestTrap_Type(Integer32):
    """Custom type upsTestTrap based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("startTestTrap", 1)
    )


_UpsTestTrap_Type.__name__ = "Integer32"
_UpsTestTrap_Object = MibScalar
upsTestTrap = _UpsTestTrap_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 3, 7, 3),
    _UpsTestTrap_Type()
)
upsTestTrap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsTestTrap.setStatus("mandatory")
_UpsControl_ObjectIdentity = ObjectIdentity
upsControl = _UpsControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 165, 3, 8)
)


class _UpsControlOutputOffDelay_Type(Integer32):
    """Custom type upsControlOutputOffDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_UpsControlOutputOffDelay_Type.__name__ = "Integer32"
_UpsControlOutputOffDelay_Object = MibScalar
upsControlOutputOffDelay = _UpsControlOutputOffDelay_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 3, 8, 1),
    _UpsControlOutputOffDelay_Type()
)
upsControlOutputOffDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsControlOutputOffDelay.setStatus("mandatory")


class _UpsControlOutputOnDelay_Type(Integer32):
    """Custom type upsControlOutputOnDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_UpsControlOutputOnDelay_Type.__name__ = "Integer32"
_UpsControlOutputOnDelay_Object = MibScalar
upsControlOutputOnDelay = _UpsControlOutputOnDelay_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 3, 8, 2),
    _UpsControlOutputOnDelay_Type()
)
upsControlOutputOnDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsControlOutputOnDelay.setStatus("mandatory")


class _UpsControlOutputOffTrapDelay_Type(Integer32):
    """Custom type upsControlOutputOffTrapDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_UpsControlOutputOffTrapDelay_Type.__name__ = "Integer32"
_UpsControlOutputOffTrapDelay_Object = MibScalar
upsControlOutputOffTrapDelay = _UpsControlOutputOffTrapDelay_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 3, 8, 3),
    _UpsControlOutputOffTrapDelay_Type()
)
upsControlOutputOffTrapDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsControlOutputOffTrapDelay.setStatus("mandatory")


class _UpsControlOutputOnTrapDelay_Type(Integer32):
    """Custom type upsControlOutputOnTrapDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_UpsControlOutputOnTrapDelay_Type.__name__ = "Integer32"
_UpsControlOutputOnTrapDelay_Object = MibScalar
upsControlOutputOnTrapDelay = _UpsControlOutputOnTrapDelay_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 3, 8, 4),
    _UpsControlOutputOnTrapDelay_Type()
)
upsControlOutputOnTrapDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsControlOutputOnTrapDelay.setStatus("deprecated")


class _UpsControlToBypassDelay_Type(Integer32):
    """Custom type upsControlToBypassDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_UpsControlToBypassDelay_Type.__name__ = "Integer32"
_UpsControlToBypassDelay_Object = MibScalar
upsControlToBypassDelay = _UpsControlToBypassDelay_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 3, 8, 5),
    _UpsControlToBypassDelay_Type()
)
upsControlToBypassDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsControlToBypassDelay.setStatus("mandatory")


class _UpsLoadShedSecsWithRestart_Type(Integer32):
    """Custom type upsLoadShedSecsWithRestart based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_UpsLoadShedSecsWithRestart_Type.__name__ = "Integer32"
_UpsLoadShedSecsWithRestart_Object = MibScalar
upsLoadShedSecsWithRestart = _UpsLoadShedSecsWithRestart_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 3, 8, 6),
    _UpsLoadShedSecsWithRestart_Type()
)
upsLoadShedSecsWithRestart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsLoadShedSecsWithRestart.setStatus("mandatory")
_UpsConfig_ObjectIdentity = ObjectIdentity
upsConfig = _UpsConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 165, 3, 9)
)


class _UpsConfigOutputVoltage_Type(Integer32):
    """Custom type upsConfigOutputVoltage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_UpsConfigOutputVoltage_Type.__name__ = "Integer32"
_UpsConfigOutputVoltage_Object = MibScalar
upsConfigOutputVoltage = _UpsConfigOutputVoltage_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 3, 9, 1),
    _UpsConfigOutputVoltage_Type()
)
upsConfigOutputVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsConfigOutputVoltage.setStatus("mandatory")


class _UpsConfigInputVoltage_Type(Integer32):
    """Custom type upsConfigInputVoltage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_UpsConfigInputVoltage_Type.__name__ = "Integer32"
_UpsConfigInputVoltage_Object = MibScalar
upsConfigInputVoltage = _UpsConfigInputVoltage_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 3, 9, 2),
    _UpsConfigInputVoltage_Type()
)
upsConfigInputVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsConfigInputVoltage.setStatus("mandatory")


class _UpsConfigOutputWatts_Type(Integer32):
    """Custom type upsConfigOutputWatts based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_UpsConfigOutputWatts_Type.__name__ = "Integer32"
_UpsConfigOutputWatts_Object = MibScalar
upsConfigOutputWatts = _UpsConfigOutputWatts_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 3, 9, 3),
    _UpsConfigOutputWatts_Type()
)
upsConfigOutputWatts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsConfigOutputWatts.setStatus("mandatory")


class _UpsConfigOutputFreq_Type(Integer32):
    """Custom type upsConfigOutputFreq based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_UpsConfigOutputFreq_Type.__name__ = "Integer32"
_UpsConfigOutputFreq_Object = MibScalar
upsConfigOutputFreq = _UpsConfigOutputFreq_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 3, 9, 4),
    _UpsConfigOutputFreq_Type()
)
upsConfigOutputFreq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsConfigOutputFreq.setStatus("mandatory")


class _UpsConfigDateAndTime_Type(DisplayString):
    """Custom type upsConfigDateAndTime based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 22),
    )


_UpsConfigDateAndTime_Type.__name__ = "DisplayString"
_UpsConfigDateAndTime_Object = MibScalar
upsConfigDateAndTime = _UpsConfigDateAndTime_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 3, 9, 5),
    _UpsConfigDateAndTime_Type()
)
upsConfigDateAndTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsConfigDateAndTime.setStatus("mandatory")


class _UpsConfigLowOutputVoltageLimit_Type(Integer32):
    """Custom type upsConfigLowOutputVoltageLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_UpsConfigLowOutputVoltageLimit_Type.__name__ = "Integer32"
_UpsConfigLowOutputVoltageLimit_Object = MibScalar
upsConfigLowOutputVoltageLimit = _UpsConfigLowOutputVoltageLimit_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 3, 9, 6),
    _UpsConfigLowOutputVoltageLimit_Type()
)
upsConfigLowOutputVoltageLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsConfigLowOutputVoltageLimit.setStatus("mandatory")


class _UpsConfigHighOutputVoltageLimit_Type(Integer32):
    """Custom type upsConfigHighOutputVoltageLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_UpsConfigHighOutputVoltageLimit_Type.__name__ = "Integer32"
_UpsConfigHighOutputVoltageLimit_Object = MibScalar
upsConfigHighOutputVoltageLimit = _UpsConfigHighOutputVoltageLimit_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 3, 9, 7),
    _UpsConfigHighOutputVoltageLimit_Type()
)
upsConfigHighOutputVoltageLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsConfigHighOutputVoltageLimit.setStatus("mandatory")
_UpsRecep_ObjectIdentity = ObjectIdentity
upsRecep = _UpsRecep_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 165, 3, 10)
)


class _UpsNumReceptacles_Type(Integer32):
    """Custom type upsNumReceptacles based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 64),
    )


_UpsNumReceptacles_Type.__name__ = "Integer32"
_UpsNumReceptacles_Object = MibScalar
upsNumReceptacles = _UpsNumReceptacles_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 3, 10, 1),
    _UpsNumReceptacles_Type()
)
upsNumReceptacles.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsNumReceptacles.setStatus("mandatory")
_UpsRecepTable_Object = MibTable
upsRecepTable = _UpsRecepTable_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 3, 10, 2)
)
if mibBuilder.loadTexts:
    upsRecepTable.setStatus("mandatory")
_UpsRecepEntry_Object = MibTableRow
upsRecepEntry = _UpsRecepEntry_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 3, 10, 2, 1)
)
upsRecepEntry.setIndexNames(
    (0, "CPQPOWER-MIB", "upsRecepIndex"),
)
if mibBuilder.loadTexts:
    upsRecepEntry.setStatus("mandatory")


class _UpsRecepIndex_Type(Integer32):
    """Custom type upsRecepIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_UpsRecepIndex_Type.__name__ = "Integer32"
_UpsRecepIndex_Object = MibTableColumn
upsRecepIndex = _UpsRecepIndex_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 3, 10, 2, 1, 1),
    _UpsRecepIndex_Type()
)
upsRecepIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsRecepIndex.setStatus("mandatory")


class _UpsRecepStatus_Type(Integer32):
    """Custom type upsRecepStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("on", 1),
          ("off", 2),
          ("pendingOff", 3),
          ("pendingOn", 4),
          ("unknown", 5))
    )


_UpsRecepStatus_Type.__name__ = "Integer32"
_UpsRecepStatus_Object = MibTableColumn
upsRecepStatus = _UpsRecepStatus_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 3, 10, 2, 1, 2),
    _UpsRecepStatus_Type()
)
upsRecepStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsRecepStatus.setStatus("mandatory")


class _UpsRecepOffDelaySecs_Type(Integer32):
    """Custom type upsRecepOffDelaySecs based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_UpsRecepOffDelaySecs_Type.__name__ = "Integer32"
_UpsRecepOffDelaySecs_Object = MibTableColumn
upsRecepOffDelaySecs = _UpsRecepOffDelaySecs_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 3, 10, 2, 1, 3),
    _UpsRecepOffDelaySecs_Type()
)
upsRecepOffDelaySecs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsRecepOffDelaySecs.setStatus("mandatory")


class _UpsRecepOnDelaySecs_Type(Integer32):
    """Custom type upsRecepOnDelaySecs based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_UpsRecepOnDelaySecs_Type.__name__ = "Integer32"
_UpsRecepOnDelaySecs_Object = MibTableColumn
upsRecepOnDelaySecs = _UpsRecepOnDelaySecs_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 3, 10, 2, 1, 4),
    _UpsRecepOnDelaySecs_Type()
)
upsRecepOnDelaySecs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsRecepOnDelaySecs.setStatus("mandatory")


class _UpsRecepAutoOffDelay_Type(Integer32):
    """Custom type upsRecepAutoOffDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 32767),
    )


_UpsRecepAutoOffDelay_Type.__name__ = "Integer32"
_UpsRecepAutoOffDelay_Object = MibTableColumn
upsRecepAutoOffDelay = _UpsRecepAutoOffDelay_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 3, 10, 2, 1, 5),
    _UpsRecepAutoOffDelay_Type()
)
upsRecepAutoOffDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsRecepAutoOffDelay.setStatus("mandatory")


class _UpsRecepAutoOnDelay_Type(Integer32):
    """Custom type upsRecepAutoOnDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 32767),
    )


_UpsRecepAutoOnDelay_Type.__name__ = "Integer32"
_UpsRecepAutoOnDelay_Object = MibTableColumn
upsRecepAutoOnDelay = _UpsRecepAutoOnDelay_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 3, 10, 2, 1, 6),
    _UpsRecepAutoOnDelay_Type()
)
upsRecepAutoOnDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsRecepAutoOnDelay.setStatus("mandatory")


class _UpsRecepShedSecsWithRestart_Type(Integer32):
    """Custom type upsRecepShedSecsWithRestart based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_UpsRecepShedSecsWithRestart_Type.__name__ = "Integer32"
_UpsRecepShedSecsWithRestart_Object = MibTableColumn
upsRecepShedSecsWithRestart = _UpsRecepShedSecsWithRestart_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 3, 10, 2, 1, 7),
    _UpsRecepShedSecsWithRestart_Type()
)
upsRecepShedSecsWithRestart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsRecepShedSecsWithRestart.setStatus("mandatory")
_UpsTopology_ObjectIdentity = ObjectIdentity
upsTopology = _UpsTopology_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 165, 3, 11)
)


class _UpsTopologyType_Type(Integer32):
    """Custom type upsTopologyType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32767),
    )


_UpsTopologyType_Type.__name__ = "Integer32"
_UpsTopologyType_Object = MibScalar
upsTopologyType = _UpsTopologyType_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 3, 11, 1),
    _UpsTopologyType_Type()
)
upsTopologyType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsTopologyType.setStatus("mandatory")


class _UpsTopoMachineCode_Type(Integer32):
    """Custom type upsTopoMachineCode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32767),
    )


_UpsTopoMachineCode_Type.__name__ = "Integer32"
_UpsTopoMachineCode_Object = MibScalar
upsTopoMachineCode = _UpsTopoMachineCode_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 3, 11, 2),
    _UpsTopoMachineCode_Type()
)
upsTopoMachineCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsTopoMachineCode.setStatus("mandatory")


class _UpsTopoUnitNumber_Type(Integer32):
    """Custom type upsTopoUnitNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 64),
    )


_UpsTopoUnitNumber_Type.__name__ = "Integer32"
_UpsTopoUnitNumber_Object = MibScalar
upsTopoUnitNumber = _UpsTopoUnitNumber_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 3, 11, 3),
    _UpsTopoUnitNumber_Type()
)
upsTopoUnitNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsTopoUnitNumber.setStatus("mandatory")


class _UpsTopoPowerStrategy_Type(Integer32):
    """Custom type upsTopoPowerStrategy based on Integer32"""
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
        *(("highAlert", 1),
          ("standard", 2),
          ("enableHighEfficiency", 3),
          ("immediateHighEfficiency", 4))
    )


_UpsTopoPowerStrategy_Type.__name__ = "Integer32"
_UpsTopoPowerStrategy_Object = MibScalar
upsTopoPowerStrategy = _UpsTopoPowerStrategy_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 3, 11, 4),
    _UpsTopoPowerStrategy_Type()
)
upsTopoPowerStrategy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsTopoPowerStrategy.setStatus("mandatory")
_Pdr_ObjectIdentity = ObjectIdentity
pdr = _Pdr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 165, 4)
)
_PdrIdent_ObjectIdentity = ObjectIdentity
pdrIdent = _PdrIdent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 165, 4, 1)
)


class _PdrName_Type(DisplayString):
    """Custom type pdrName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_PdrName_Type.__name__ = "DisplayString"
_PdrName_Object = MibScalar
pdrName = _PdrName_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 4, 1, 1),
    _PdrName_Type()
)
pdrName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pdrName.setStatus("mandatory")


class _PdrModel_Type(DisplayString):
    """Custom type pdrModel based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_PdrModel_Type.__name__ = "DisplayString"
_PdrModel_Object = MibScalar
pdrModel = _PdrModel_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 4, 1, 2),
    _PdrModel_Type()
)
pdrModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdrModel.setStatus("mandatory")


class _PdrManufacturer_Type(DisplayString):
    """Custom type pdrManufacturer based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_PdrManufacturer_Type.__name__ = "DisplayString"
_PdrManufacturer_Object = MibScalar
pdrManufacturer = _PdrManufacturer_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 4, 1, 3),
    _PdrManufacturer_Type()
)
pdrManufacturer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdrManufacturer.setStatus("mandatory")


class _PdrFirmwareVersion_Type(DisplayString):
    """Custom type pdrFirmwareVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_PdrFirmwareVersion_Type.__name__ = "DisplayString"
_PdrFirmwareVersion_Object = MibScalar
pdrFirmwareVersion = _PdrFirmwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 4, 1, 4),
    _PdrFirmwareVersion_Type()
)
pdrFirmwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdrFirmwareVersion.setStatus("mandatory")


class _PdrPartNumber_Type(DisplayString):
    """Custom type pdrPartNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_PdrPartNumber_Type.__name__ = "DisplayString"
_PdrPartNumber_Object = MibScalar
pdrPartNumber = _PdrPartNumber_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 4, 1, 5),
    _PdrPartNumber_Type()
)
pdrPartNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdrPartNumber.setStatus("mandatory")


class _PdrSerialNumber_Type(DisplayString):
    """Custom type pdrSerialNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_PdrSerialNumber_Type.__name__ = "DisplayString"
_PdrSerialNumber_Object = MibScalar
pdrSerialNumber = _PdrSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 4, 1, 6),
    _PdrSerialNumber_Type()
)
pdrSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdrSerialNumber.setStatus("mandatory")


class _PdrVARating_Type(Integer32):
    """Custom type pdrVARating based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_PdrVARating_Type.__name__ = "Integer32"
_PdrVARating_Object = MibScalar
pdrVARating = _PdrVARating_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 4, 1, 7),
    _PdrVARating_Type()
)
pdrVARating.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdrVARating.setStatus("mandatory")


class _PdrNominalOutputVoltage_Type(Integer32):
    """Custom type pdrNominalOutputVoltage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_PdrNominalOutputVoltage_Type.__name__ = "Integer32"
_PdrNominalOutputVoltage_Object = MibScalar
pdrNominalOutputVoltage = _PdrNominalOutputVoltage_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 4, 1, 8),
    _PdrNominalOutputVoltage_Type()
)
pdrNominalOutputVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdrNominalOutputVoltage.setStatus("mandatory")


class _PdrNumPhases_Type(Integer32):
    """Custom type pdrNumPhases based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_PdrNumPhases_Type.__name__ = "Integer32"
_PdrNumPhases_Object = MibScalar
pdrNumPhases = _PdrNumPhases_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 4, 1, 9),
    _PdrNumPhases_Type()
)
pdrNumPhases.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdrNumPhases.setStatus("mandatory")


class _PdrNumPanels_Type(Integer32):
    """Custom type pdrNumPanels based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_PdrNumPanels_Type.__name__ = "Integer32"
_PdrNumPanels_Object = MibScalar
pdrNumPanels = _PdrNumPanels_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 4, 1, 10),
    _PdrNumPanels_Type()
)
pdrNumPanels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdrNumPanels.setStatus("mandatory")


class _PdrNumBreakers_Type(Integer32):
    """Custom type pdrNumBreakers based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_PdrNumBreakers_Type.__name__ = "Integer32"
_PdrNumBreakers_Object = MibScalar
pdrNumBreakers = _PdrNumBreakers_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 4, 1, 11),
    _PdrNumBreakers_Type()
)
pdrNumBreakers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdrNumBreakers.setStatus("mandatory")
_PdrPanel_ObjectIdentity = ObjectIdentity
pdrPanel = _PdrPanel_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 165, 4, 2)
)
_PdrPanelTable_Object = MibTable
pdrPanelTable = _PdrPanelTable_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 4, 2, 1)
)
if mibBuilder.loadTexts:
    pdrPanelTable.setStatus("mandatory")
_PdrPanelEntry_Object = MibTableRow
pdrPanelEntry = _PdrPanelEntry_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 4, 2, 1, 1)
)
pdrPanelEntry.setIndexNames(
    (0, "CPQPOWER-MIB", "pdrPanelIndex"),
)
if mibBuilder.loadTexts:
    pdrPanelEntry.setStatus("mandatory")


class _PdrPanelIndex_Type(Integer32):
    """Custom type pdrPanelIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10),
    )


_PdrPanelIndex_Type.__name__ = "Integer32"
_PdrPanelIndex_Object = MibTableColumn
pdrPanelIndex = _PdrPanelIndex_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 4, 2, 1, 1, 1),
    _PdrPanelIndex_Type()
)
pdrPanelIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdrPanelIndex.setStatus("mandatory")


class _PdrPanelFrequency_Type(Integer32):
    """Custom type pdrPanelFrequency based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_PdrPanelFrequency_Type.__name__ = "Integer32"
_PdrPanelFrequency_Object = MibTableColumn
pdrPanelFrequency = _PdrPanelFrequency_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 4, 2, 1, 1, 2),
    _PdrPanelFrequency_Type()
)
pdrPanelFrequency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdrPanelFrequency.setStatus("mandatory")


class _PdrPanelPower_Type(Integer32):
    """Custom type pdrPanelPower based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_PdrPanelPower_Type.__name__ = "Integer32"
_PdrPanelPower_Object = MibTableColumn
pdrPanelPower = _PdrPanelPower_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 4, 2, 1, 1, 3),
    _PdrPanelPower_Type()
)
pdrPanelPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdrPanelPower.setStatus("mandatory")


class _PdrPanelRatedCurrent_Type(Integer32):
    """Custom type pdrPanelRatedCurrent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_PdrPanelRatedCurrent_Type.__name__ = "Integer32"
_PdrPanelRatedCurrent_Object = MibTableColumn
pdrPanelRatedCurrent = _PdrPanelRatedCurrent_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 4, 2, 1, 1, 4),
    _PdrPanelRatedCurrent_Type()
)
pdrPanelRatedCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdrPanelRatedCurrent.setStatus("mandatory")


class _PdrPanelMonthlyKWH_Type(Integer32):
    """Custom type pdrPanelMonthlyKWH based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_PdrPanelMonthlyKWH_Type.__name__ = "Integer32"
_PdrPanelMonthlyKWH_Object = MibTableColumn
pdrPanelMonthlyKWH = _PdrPanelMonthlyKWH_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 4, 2, 1, 1, 5),
    _PdrPanelMonthlyKWH_Type()
)
pdrPanelMonthlyKWH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdrPanelMonthlyKWH.setStatus("mandatory")


class _PdrPanelYearlyKWH_Type(Integer32):
    """Custom type pdrPanelYearlyKWH based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_PdrPanelYearlyKWH_Type.__name__ = "Integer32"
_PdrPanelYearlyKWH_Object = MibTableColumn
pdrPanelYearlyKWH = _PdrPanelYearlyKWH_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 4, 2, 1, 1, 6),
    _PdrPanelYearlyKWH_Type()
)
pdrPanelYearlyKWH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdrPanelYearlyKWH.setStatus("mandatory")


class _PdrPanelTotalKWH_Type(Integer32):
    """Custom type pdrPanelTotalKWH based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_PdrPanelTotalKWH_Type.__name__ = "Integer32"
_PdrPanelTotalKWH_Object = MibTableColumn
pdrPanelTotalKWH = _PdrPanelTotalKWH_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 4, 2, 1, 1, 7),
    _PdrPanelTotalKWH_Type()
)
pdrPanelTotalKWH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdrPanelTotalKWH.setStatus("mandatory")


class _PdrPanelVoltageA_Type(Integer32):
    """Custom type pdrPanelVoltageA based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_PdrPanelVoltageA_Type.__name__ = "Integer32"
_PdrPanelVoltageA_Object = MibTableColumn
pdrPanelVoltageA = _PdrPanelVoltageA_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 4, 2, 1, 1, 8),
    _PdrPanelVoltageA_Type()
)
pdrPanelVoltageA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdrPanelVoltageA.setStatus("mandatory")


class _PdrPanelVoltageB_Type(Integer32):
    """Custom type pdrPanelVoltageB based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_PdrPanelVoltageB_Type.__name__ = "Integer32"
_PdrPanelVoltageB_Object = MibTableColumn
pdrPanelVoltageB = _PdrPanelVoltageB_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 4, 2, 1, 1, 9),
    _PdrPanelVoltageB_Type()
)
pdrPanelVoltageB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdrPanelVoltageB.setStatus("mandatory")


class _PdrPanelVoltageC_Type(Integer32):
    """Custom type pdrPanelVoltageC based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_PdrPanelVoltageC_Type.__name__ = "Integer32"
_PdrPanelVoltageC_Object = MibTableColumn
pdrPanelVoltageC = _PdrPanelVoltageC_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 4, 2, 1, 1, 10),
    _PdrPanelVoltageC_Type()
)
pdrPanelVoltageC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdrPanelVoltageC.setStatus("mandatory")


class _PdrPanelCurrentA_Type(Integer32):
    """Custom type pdrPanelCurrentA based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_PdrPanelCurrentA_Type.__name__ = "Integer32"
_PdrPanelCurrentA_Object = MibTableColumn
pdrPanelCurrentA = _PdrPanelCurrentA_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 4, 2, 1, 1, 11),
    _PdrPanelCurrentA_Type()
)
pdrPanelCurrentA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdrPanelCurrentA.setStatus("mandatory")


class _PdrPanelCurrentB_Type(Integer32):
    """Custom type pdrPanelCurrentB based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_PdrPanelCurrentB_Type.__name__ = "Integer32"
_PdrPanelCurrentB_Object = MibTableColumn
pdrPanelCurrentB = _PdrPanelCurrentB_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 4, 2, 1, 1, 12),
    _PdrPanelCurrentB_Type()
)
pdrPanelCurrentB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdrPanelCurrentB.setStatus("mandatory")


class _PdrPanelCurrentC_Type(Integer32):
    """Custom type pdrPanelCurrentC based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_PdrPanelCurrentC_Type.__name__ = "Integer32"
_PdrPanelCurrentC_Object = MibTableColumn
pdrPanelCurrentC = _PdrPanelCurrentC_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 4, 2, 1, 1, 13),
    _PdrPanelCurrentC_Type()
)
pdrPanelCurrentC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdrPanelCurrentC.setStatus("mandatory")


class _PdrPanelLoadA_Type(Integer32):
    """Custom type pdrPanelLoadA based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 200),
    )


_PdrPanelLoadA_Type.__name__ = "Integer32"
_PdrPanelLoadA_Object = MibTableColumn
pdrPanelLoadA = _PdrPanelLoadA_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 4, 2, 1, 1, 14),
    _PdrPanelLoadA_Type()
)
pdrPanelLoadA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdrPanelLoadA.setStatus("mandatory")


class _PdrPanelLoadB_Type(Integer32):
    """Custom type pdrPanelLoadB based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 200),
    )


_PdrPanelLoadB_Type.__name__ = "Integer32"
_PdrPanelLoadB_Object = MibTableColumn
pdrPanelLoadB = _PdrPanelLoadB_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 4, 2, 1, 1, 15),
    _PdrPanelLoadB_Type()
)
pdrPanelLoadB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdrPanelLoadB.setStatus("mandatory")


class _PdrPanelLoadC_Type(Integer32):
    """Custom type pdrPanelLoadC based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 200),
    )


_PdrPanelLoadC_Type.__name__ = "Integer32"
_PdrPanelLoadC_Object = MibTableColumn
pdrPanelLoadC = _PdrPanelLoadC_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 4, 2, 1, 1, 16),
    _PdrPanelLoadC_Type()
)
pdrPanelLoadC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdrPanelLoadC.setStatus("mandatory")
_PdrBreaker_ObjectIdentity = ObjectIdentity
pdrBreaker = _PdrBreaker_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 165, 4, 3)
)
_PdrBreakerTable_Object = MibTable
pdrBreakerTable = _PdrBreakerTable_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 4, 3, 1)
)
if mibBuilder.loadTexts:
    pdrBreakerTable.setStatus("mandatory")
_PdrBreakerEntry_Object = MibTableRow
pdrBreakerEntry = _PdrBreakerEntry_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 4, 3, 1, 1)
)
pdrBreakerEntry.setIndexNames(
    (0, "CPQPOWER-MIB", "pdrPanelIndex"),
    (0, "CPQPOWER-MIB", "pdrBreakerIndex"),
)
if mibBuilder.loadTexts:
    pdrBreakerEntry.setStatus("mandatory")


class _PdrBreakerIndex_Type(Integer32):
    """Custom type pdrBreakerIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 200),
    )


_PdrBreakerIndex_Type.__name__ = "Integer32"
_PdrBreakerIndex_Object = MibTableColumn
pdrBreakerIndex = _PdrBreakerIndex_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 4, 3, 1, 1, 1),
    _PdrBreakerIndex_Type()
)
pdrBreakerIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdrBreakerIndex.setStatus("mandatory")
_PdrBreakerPanel_Type = Integer32
_PdrBreakerPanel_Object = MibTableColumn
pdrBreakerPanel = _PdrBreakerPanel_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 4, 3, 1, 1, 2),
    _PdrBreakerPanel_Type()
)
pdrBreakerPanel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdrBreakerPanel.setStatus("mandatory")
_PdrBreakerNumPosition_Type = Integer32
_PdrBreakerNumPosition_Object = MibTableColumn
pdrBreakerNumPosition = _PdrBreakerNumPosition_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 4, 3, 1, 1, 3),
    _PdrBreakerNumPosition_Type()
)
pdrBreakerNumPosition.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdrBreakerNumPosition.setStatus("mandatory")
_PdrBreakerNumPhases_Type = Integer32
_PdrBreakerNumPhases_Object = MibTableColumn
pdrBreakerNumPhases = _PdrBreakerNumPhases_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 4, 3, 1, 1, 4),
    _PdrBreakerNumPhases_Type()
)
pdrBreakerNumPhases.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdrBreakerNumPhases.setStatus("mandatory")
_PdrBreakerNumSequence_Type = Integer32
_PdrBreakerNumSequence_Object = MibTableColumn
pdrBreakerNumSequence = _PdrBreakerNumSequence_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 4, 3, 1, 1, 5),
    _PdrBreakerNumSequence_Type()
)
pdrBreakerNumSequence.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdrBreakerNumSequence.setStatus("mandatory")
_PdrBreakerRatedCurrent_Type = Integer32
_PdrBreakerRatedCurrent_Object = MibTableColumn
pdrBreakerRatedCurrent = _PdrBreakerRatedCurrent_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 4, 3, 1, 1, 6),
    _PdrBreakerRatedCurrent_Type()
)
pdrBreakerRatedCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdrBreakerRatedCurrent.setStatus("mandatory")


class _PdrBreakerMonthlyKWH_Type(Integer32):
    """Custom type pdrBreakerMonthlyKWH based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_PdrBreakerMonthlyKWH_Type.__name__ = "Integer32"
_PdrBreakerMonthlyKWH_Object = MibTableColumn
pdrBreakerMonthlyKWH = _PdrBreakerMonthlyKWH_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 4, 3, 1, 1, 7),
    _PdrBreakerMonthlyKWH_Type()
)
pdrBreakerMonthlyKWH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdrBreakerMonthlyKWH.setStatus("mandatory")


class _PdrBreakerYearlyKWH_Type(Integer32):
    """Custom type pdrBreakerYearlyKWH based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_PdrBreakerYearlyKWH_Type.__name__ = "Integer32"
_PdrBreakerYearlyKWH_Object = MibTableColumn
pdrBreakerYearlyKWH = _PdrBreakerYearlyKWH_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 4, 3, 1, 1, 8),
    _PdrBreakerYearlyKWH_Type()
)
pdrBreakerYearlyKWH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdrBreakerYearlyKWH.setStatus("mandatory")


class _PdrBreakerTotalKWH_Type(Integer32):
    """Custom type pdrBreakerTotalKWH based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_PdrBreakerTotalKWH_Type.__name__ = "Integer32"
_PdrBreakerTotalKWH_Object = MibTableColumn
pdrBreakerTotalKWH = _PdrBreakerTotalKWH_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 4, 3, 1, 1, 9),
    _PdrBreakerTotalKWH_Type()
)
pdrBreakerTotalKWH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdrBreakerTotalKWH.setStatus("mandatory")


class _PdrBreakerCurrent_Type(Integer32):
    """Custom type pdrBreakerCurrent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_PdrBreakerCurrent_Type.__name__ = "Integer32"
_PdrBreakerCurrent_Object = MibTableColumn
pdrBreakerCurrent = _PdrBreakerCurrent_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 4, 3, 1, 1, 10),
    _PdrBreakerCurrent_Type()
)
pdrBreakerCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdrBreakerCurrent.setStatus("mandatory")


class _PdrBreakerCurrentPercent_Type(Integer32):
    """Custom type pdrBreakerCurrentPercent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 200),
    )


_PdrBreakerCurrentPercent_Type.__name__ = "Integer32"
_PdrBreakerCurrentPercent_Object = MibTableColumn
pdrBreakerCurrentPercent = _PdrBreakerCurrentPercent_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 4, 3, 1, 1, 11),
    _PdrBreakerCurrentPercent_Type()
)
pdrBreakerCurrentPercent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdrBreakerCurrentPercent.setStatus("mandatory")
_PdrBreakerPower_Type = Integer32
_PdrBreakerPower_Object = MibTableColumn
pdrBreakerPower = _PdrBreakerPower_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 4, 3, 1, 1, 12),
    _PdrBreakerPower_Type()
)
pdrBreakerPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdrBreakerPower.setStatus("mandatory")


class _PdrBreakerPercentWarning_Type(Integer32):
    """Custom type pdrBreakerPercentWarning based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 200),
    )


_PdrBreakerPercentWarning_Type.__name__ = "Integer32"
_PdrBreakerPercentWarning_Object = MibTableColumn
pdrBreakerPercentWarning = _PdrBreakerPercentWarning_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 4, 3, 1, 1, 13),
    _PdrBreakerPercentWarning_Type()
)
pdrBreakerPercentWarning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdrBreakerPercentWarning.setStatus("mandatory")
_PdrBreakerPercentOverload_Type = Integer32
_PdrBreakerPercentOverload_Object = MibTableColumn
pdrBreakerPercentOverload = _PdrBreakerPercentOverload_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 4, 3, 1, 1, 14),
    _PdrBreakerPercentOverload_Type()
)
pdrBreakerPercentOverload.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdrBreakerPercentOverload.setStatus("mandatory")
_Mpdu_ObjectIdentity = ObjectIdentity
mpdu = _Mpdu_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 165, 5)
)
_MpduIdent_ObjectIdentity = ObjectIdentity
mpduIdent = _MpduIdent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 165, 5, 1)
)
_MpduNumMPDU_Type = Integer32
_MpduNumMPDU_Object = MibScalar
mpduNumMPDU = _MpduNumMPDU_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 5, 1, 1),
    _MpduNumMPDU_Type()
)
mpduNumMPDU.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpduNumMPDU.setStatus("mandatory")
_MpduIdentTable_Object = MibTable
mpduIdentTable = _MpduIdentTable_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 5, 1, 2)
)
if mibBuilder.loadTexts:
    mpduIdentTable.setStatus("mandatory")
_MpduIdentEntry_Object = MibTableRow
mpduIdentEntry = _MpduIdentEntry_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 5, 1, 2, 1)
)
mpduIdentEntry.setIndexNames(
    (0, "CPQPOWER-MIB", "mpduIdentIndex"),
)
if mibBuilder.loadTexts:
    mpduIdentEntry.setStatus("mandatory")


class _MpduIdentIndex_Type(Integer32):
    """Custom type mpduIdentIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_MpduIdentIndex_Type.__name__ = "Integer32"
_MpduIdentIndex_Object = MibTableColumn
mpduIdentIndex = _MpduIdentIndex_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 5, 1, 2, 1, 1),
    _MpduIdentIndex_Type()
)
mpduIdentIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpduIdentIndex.setStatus("mandatory")
_MpduManufacturer_Type = DisplayString
_MpduManufacturer_Object = MibTableColumn
mpduManufacturer = _MpduManufacturer_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 5, 1, 2, 1, 2),
    _MpduManufacturer_Type()
)
mpduManufacturer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpduManufacturer.setStatus("mandatory")
_MpduModel_Type = DisplayString
_MpduModel_Object = MibTableColumn
mpduModel = _MpduModel_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 5, 1, 2, 1, 3),
    _MpduModel_Type()
)
mpduModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpduModel.setStatus("mandatory")
_MpduName_Type = DisplayString
_MpduName_Object = MibTableColumn
mpduName = _MpduName_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 5, 1, 2, 1, 4),
    _MpduName_Type()
)
mpduName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpduName.setStatus("mandatory")
_MpduFirmwareVersion_Type = DisplayString
_MpduFirmwareVersion_Object = MibTableColumn
mpduFirmwareVersion = _MpduFirmwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 5, 1, 2, 1, 5),
    _MpduFirmwareVersion_Type()
)
mpduFirmwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpduFirmwareVersion.setStatus("mandatory")
_MpduHardwareVersion_Type = DisplayString
_MpduHardwareVersion_Object = MibTableColumn
mpduHardwareVersion = _MpduHardwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 5, 1, 2, 1, 6),
    _MpduHardwareVersion_Type()
)
mpduHardwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpduHardwareVersion.setStatus("mandatory")
_MpduPartNumber_Type = DisplayString
_MpduPartNumber_Object = MibTableColumn
mpduPartNumber = _MpduPartNumber_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 5, 1, 2, 1, 7),
    _MpduPartNumber_Type()
)
mpduPartNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpduPartNumber.setStatus("mandatory")
_MpduSerialNumber_Type = DisplayString
_MpduSerialNumber_Object = MibTableColumn
mpduSerialNumber = _MpduSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 5, 1, 2, 1, 8),
    _MpduSerialNumber_Type()
)
mpduSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpduSerialNumber.setStatus("mandatory")
_MpduUUID_Type = DisplayString
_MpduUUID_Object = MibTableColumn
mpduUUID = _MpduUUID_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 5, 1, 2, 1, 9),
    _MpduUUID_Type()
)
mpduUUID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpduUUID.setStatus("mandatory")
_MpduIP_Type = DisplayString
_MpduIP_Object = MibTableColumn
mpduIP = _MpduIP_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 5, 1, 2, 1, 10),
    _MpduIP_Type()
)
mpduIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpduIP.setStatus("mandatory")
_MpduMACAddress_Type = DisplayString
_MpduMACAddress_Object = MibTableColumn
mpduMACAddress = _MpduMACAddress_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 5, 1, 2, 1, 11),
    _MpduMACAddress_Type()
)
mpduMACAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpduMACAddress.setStatus("mandatory")
_MpduControlStatus_Type = DisplayString
_MpduControlStatus_Object = MibTableColumn
mpduControlStatus = _MpduControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 5, 1, 2, 1, 12),
    _MpduControlStatus_Type()
)
mpduControlStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpduControlStatus.setStatus("mandatory")
_MpduRegion_Type = DisplayString
_MpduRegion_Object = MibTableColumn
mpduRegion = _MpduRegion_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 5, 1, 2, 1, 13),
    _MpduRegion_Type()
)
mpduRegion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpduRegion.setStatus("mandatory")
_MpduType_Type = DisplayString
_MpduType_Object = MibTableColumn
mpduType = _MpduType_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 5, 1, 2, 1, 14),
    _MpduType_Type()
)
mpduType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpduType.setStatus("mandatory")
_MpduPowerRating_Type = DisplayString
_MpduPowerRating_Object = MibTableColumn
mpduPowerRating = _MpduPowerRating_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 5, 1, 2, 1, 15),
    _MpduPowerRating_Type()
)
mpduPowerRating.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpduPowerRating.setStatus("mandatory")
_MpduInputRating_Type = DisplayString
_MpduInputRating_Object = MibTableColumn
mpduInputRating = _MpduInputRating_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 5, 1, 2, 1, 16),
    _MpduInputRating_Type()
)
mpduInputRating.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpduInputRating.setStatus("mandatory")
_MpduInputPlug_Type = DisplayString
_MpduInputPlug_Object = MibTableColumn
mpduInputPlug = _MpduInputPlug_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 5, 1, 2, 1, 17),
    _MpduInputPlug_Type()
)
mpduInputPlug.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpduInputPlug.setStatus("mandatory")
_MpduNumBreakers_Type = Integer32
_MpduNumBreakers_Object = MibTableColumn
mpduNumBreakers = _MpduNumBreakers_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 5, 1, 2, 1, 18),
    _MpduNumBreakers_Type()
)
mpduNumBreakers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpduNumBreakers.setStatus("mandatory")
_MpduNumOutlet_Type = Integer32
_MpduNumOutlet_Object = MibTableColumn
mpduNumOutlet = _MpduNumOutlet_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 5, 1, 2, 1, 19),
    _MpduNumOutlet_Type()
)
mpduNumOutlet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpduNumOutlet.setStatus("mandatory")
_MpduUHeight_Type = Integer32
_MpduUHeight_Object = MibTableColumn
mpduUHeight = _MpduUHeight_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 5, 1, 2, 1, 20),
    _MpduUHeight_Type()
)
mpduUHeight.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpduUHeight.setStatus("mandatory")
_MpduRedundantStatus_Type = DisplayString
_MpduRedundantStatus_Object = MibTableColumn
mpduRedundantStatus = _MpduRedundantStatus_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 5, 1, 2, 1, 21),
    _MpduRedundantStatus_Type()
)
mpduRedundantStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpduRedundantStatus.setStatus("mandatory")
_MpduNumSmartExtBar_Type = Integer32
_MpduNumSmartExtBar_Object = MibTableColumn
mpduNumSmartExtBar = _MpduNumSmartExtBar_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 5, 1, 2, 1, 22),
    _MpduNumSmartExtBar_Type()
)
mpduNumSmartExtBar.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpduNumSmartExtBar.setStatus("mandatory")
_MpduPanelName_Type = DisplayString
_MpduPanelName_Object = MibTableColumn
mpduPanelName = _MpduPanelName_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 5, 1, 2, 1, 23),
    _MpduPanelName_Type()
)
mpduPanelName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpduPanelName.setStatus("mandatory")
_MpduPanelBreakerName_Type = DisplayString
_MpduPanelBreakerName_Object = MibTableColumn
mpduPanelBreakerName = _MpduPanelBreakerName_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 5, 1, 2, 1, 24),
    _MpduPanelBreakerName_Type()
)
mpduPanelBreakerName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpduPanelBreakerName.setStatus("mandatory")
_MpduPanelBreakerRating_Type = DisplayString
_MpduPanelBreakerRating_Object = MibTableColumn
mpduPanelBreakerRating = _MpduPanelBreakerRating_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 5, 1, 2, 1, 25),
    _MpduPanelBreakerRating_Type()
)
mpduPanelBreakerRating.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpduPanelBreakerRating.setStatus("mandatory")
_MpduACFeedName_Type = DisplayString
_MpduACFeedName_Object = MibTableColumn
mpduACFeedName = _MpduACFeedName_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 5, 1, 2, 1, 26),
    _MpduACFeedName_Type()
)
mpduACFeedName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpduACFeedName.setStatus("mandatory")
_MpduFloorName_Type = DisplayString
_MpduFloorName_Object = MibTableColumn
mpduFloorName = _MpduFloorName_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 5, 1, 2, 1, 27),
    _MpduFloorName_Type()
)
mpduFloorName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpduFloorName.setStatus("mandatory")
_MpduRoomName_Type = DisplayString
_MpduRoomName_Object = MibTableColumn
mpduRoomName = _MpduRoomName_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 5, 1, 2, 1, 28),
    _MpduRoomName_Type()
)
mpduRoomName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpduRoomName.setStatus("mandatory")
_MpduRow_Type = DisplayString
_MpduRow_Object = MibTableColumn
mpduRow = _MpduRow_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 5, 1, 2, 1, 29),
    _MpduRow_Type()
)
mpduRow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpduRow.setStatus("mandatory")
_MpduRowPosition_Type = DisplayString
_MpduRowPosition_Object = MibTableColumn
mpduRowPosition = _MpduRowPosition_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 5, 1, 2, 1, 30),
    _MpduRowPosition_Type()
)
mpduRowPosition.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpduRowPosition.setStatus("mandatory")
_MpduRackName_Type = DisplayString
_MpduRackName_Object = MibTableColumn
mpduRackName = _MpduRackName_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 5, 1, 2, 1, 31),
    _MpduRackName_Type()
)
mpduRackName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpduRackName.setStatus("mandatory")
_MpduRackHeight_Type = DisplayString
_MpduRackHeight_Object = MibTableColumn
mpduRackHeight = _MpduRackHeight_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 5, 1, 2, 1, 32),
    _MpduRackHeight_Type()
)
mpduRackHeight.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpduRackHeight.setStatus("mandatory")
_MpduRackID_Type = DisplayString
_MpduRackID_Object = MibTableColumn
mpduRackID = _MpduRackID_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 5, 1, 2, 1, 33),
    _MpduRackID_Type()
)
mpduRackID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpduRackID.setStatus("mandatory")
_MpduUPosition_Type = Integer32
_MpduUPosition_Object = MibTableColumn
mpduUPosition = _MpduUPosition_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 5, 1, 2, 1, 34),
    _MpduUPosition_Type()
)
mpduUPosition.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpduUPosition.setStatus("mandatory")
_MpduPairedPDUUUID_Type = DisplayString
_MpduPairedPDUUUID_Object = MibTableColumn
mpduPairedPDUUUID = _MpduPairedPDUUUID_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 5, 1, 2, 1, 35),
    _MpduPairedPDUUUID_Type()
)
mpduPairedPDUUUID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpduPairedPDUUUID.setStatus("mandatory")
_MpduPairedPDUIP_Type = DisplayString
_MpduPairedPDUIP_Object = MibTableColumn
mpduPairedPDUIP = _MpduPairedPDUIP_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 5, 1, 2, 1, 36),
    _MpduPairedPDUIP_Type()
)
mpduPairedPDUIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpduPairedPDUIP.setStatus("mandatory")
_MpduInstalledLocation_Type = Integer32
_MpduInstalledLocation_Object = MibTableColumn
mpduInstalledLocation = _MpduInstalledLocation_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 5, 1, 2, 1, 37),
    _MpduInstalledLocation_Type()
)
mpduInstalledLocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpduInstalledLocation.setStatus("mandatory")
_MpduTotalPowerWatt_Type = Integer32
_MpduTotalPowerWatt_Object = MibTableColumn
mpduTotalPowerWatt = _MpduTotalPowerWatt_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 5, 1, 2, 1, 38),
    _MpduTotalPowerWatt_Type()
)
mpduTotalPowerWatt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpduTotalPowerWatt.setStatus("mandatory")
_MpduTotalPowerVA_Type = Integer32
_MpduTotalPowerVA_Object = MibTableColumn
mpduTotalPowerVA = _MpduTotalPowerVA_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 5, 1, 2, 1, 39),
    _MpduTotalPowerVA_Type()
)
mpduTotalPowerVA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpduTotalPowerVA.setStatus("mandatory")
_MpduTotalPercentLoad_Type = Integer32
_MpduTotalPercentLoad_Object = MibTableColumn
mpduTotalPercentLoad = _MpduTotalPercentLoad_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 5, 1, 2, 1, 40),
    _MpduTotalPercentLoad_Type()
)
mpduTotalPercentLoad.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpduTotalPercentLoad.setStatus("mandatory")
_MpduRegionalNominalVoltage_Type = DisplayString
_MpduRegionalNominalVoltage_Object = MibTableColumn
mpduRegionalNominalVoltage = _MpduRegionalNominalVoltage_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 5, 1, 2, 1, 41),
    _MpduRegionalNominalVoltage_Type()
)
mpduRegionalNominalVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpduRegionalNominalVoltage.setStatus("mandatory")
_MpduOutput_ObjectIdentity = ObjectIdentity
mpduOutput = _MpduOutput_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 165, 5, 2)
)
_MpduOutputTable_Object = MibTable
mpduOutputTable = _MpduOutputTable_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 5, 2, 1)
)
if mibBuilder.loadTexts:
    mpduOutputTable.setStatus("mandatory")
_MpduOutputEntry_Object = MibTableRow
mpduOutputEntry = _MpduOutputEntry_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 5, 2, 1, 1)
)
mpduOutputEntry.setIndexNames(
    (0, "CPQPOWER-MIB", "mpduIdentIndex"),
    (0, "CPQPOWER-MIB", "mpduOutputIndex"),
)
if mibBuilder.loadTexts:
    mpduOutputEntry.setStatus("mandatory")


class _MpduOutputIndex_Type(Integer32):
    """Custom type mpduOutputIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_MpduOutputIndex_Type.__name__ = "Integer32"
_MpduOutputIndex_Object = MibTableColumn
mpduOutputIndex = _MpduOutputIndex_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 5, 2, 1, 1, 1),
    _MpduOutputIndex_Type()
)
mpduOutputIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpduOutputIndex.setStatus("mandatory")
_MpduOutputStatus_Type = DisplayString
_MpduOutputStatus_Object = MibTableColumn
mpduOutputStatus = _MpduOutputStatus_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 5, 2, 1, 1, 2),
    _MpduOutputStatus_Type()
)
mpduOutputStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpduOutputStatus.setStatus("mandatory")
_MpduOutputBreakerRating_Type = Integer32
_MpduOutputBreakerRating_Object = MibTableColumn
mpduOutputBreakerRating = _MpduOutputBreakerRating_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 5, 2, 1, 1, 3),
    _MpduOutputBreakerRating_Type()
)
mpduOutputBreakerRating.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpduOutputBreakerRating.setStatus("mandatory")
_MpduOutputSmartDevice_Type = DisplayString
_MpduOutputSmartDevice_Object = MibTableColumn
mpduOutputSmartDevice = _MpduOutputSmartDevice_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 5, 2, 1, 1, 4),
    _MpduOutputSmartDevice_Type()
)
mpduOutputSmartDevice.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpduOutputSmartDevice.setStatus("mandatory")
_MpduOutputPercentLoad_Type = Integer32
_MpduOutputPercentLoad_Object = MibTableColumn
mpduOutputPercentLoad = _MpduOutputPercentLoad_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 5, 2, 1, 1, 5),
    _MpduOutputPercentLoad_Type()
)
mpduOutputPercentLoad.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpduOutputPercentLoad.setStatus("mandatory")
_MpduOutputVoltage_Type = Integer32
_MpduOutputVoltage_Object = MibTableColumn
mpduOutputVoltage = _MpduOutputVoltage_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 5, 2, 1, 1, 6),
    _MpduOutputVoltage_Type()
)
mpduOutputVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpduOutputVoltage.setStatus("mandatory")
_MpduOutputCurrent_Type = Integer32
_MpduOutputCurrent_Object = MibTableColumn
mpduOutputCurrent = _MpduOutputCurrent_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 5, 2, 1, 1, 7),
    _MpduOutputCurrent_Type()
)
mpduOutputCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpduOutputCurrent.setStatus("mandatory")
_MpduOutputPowerVA_Type = Integer32
_MpduOutputPowerVA_Object = MibTableColumn
mpduOutputPowerVA = _MpduOutputPowerVA_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 5, 2, 1, 1, 8),
    _MpduOutputPowerVA_Type()
)
mpduOutputPowerVA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpduOutputPowerVA.setStatus("mandatory")
_MpduOutputPowerWatt_Type = Integer32
_MpduOutputPowerWatt_Object = MibTableColumn
mpduOutputPowerWatt = _MpduOutputPowerWatt_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 5, 2, 1, 1, 9),
    _MpduOutputPowerWatt_Type()
)
mpduOutputPowerWatt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpduOutputPowerWatt.setStatus("mandatory")
_MpduOutputPowerFactor_Type = Integer32
_MpduOutputPowerFactor_Object = MibTableColumn
mpduOutputPowerFactor = _MpduOutputPowerFactor_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 5, 2, 1, 1, 10),
    _MpduOutputPowerFactor_Type()
)
mpduOutputPowerFactor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpduOutputPowerFactor.setStatus("mandatory")
_MpduOutputWarningThreshold_Type = Integer32
_MpduOutputWarningThreshold_Object = MibTableColumn
mpduOutputWarningThreshold = _MpduOutputWarningThreshold_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 5, 2, 1, 1, 11),
    _MpduOutputWarningThreshold_Type()
)
mpduOutputWarningThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpduOutputWarningThreshold.setStatus("mandatory")
_MpduOutputCriticalThreshold_Type = Integer32
_MpduOutputCriticalThreshold_Object = MibTableColumn
mpduOutputCriticalThreshold = _MpduOutputCriticalThreshold_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 5, 2, 1, 1, 12),
    _MpduOutputCriticalThreshold_Type()
)
mpduOutputCriticalThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpduOutputCriticalThreshold.setStatus("mandatory")
_MpduOutputPowerWattHour_Type = Integer32
_MpduOutputPowerWattHour_Object = MibTableColumn
mpduOutputPowerWattHour = _MpduOutputPowerWattHour_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 5, 2, 1, 1, 13),
    _MpduOutputPowerWattHour_Type()
)
mpduOutputPowerWattHour.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpduOutputPowerWattHour.setStatus("mandatory")
_MpduDeviceIdent_ObjectIdentity = ObjectIdentity
mpduDeviceIdent = _MpduDeviceIdent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 165, 5, 3)
)
_MpduDeviceIdentTable_Object = MibTable
mpduDeviceIdentTable = _MpduDeviceIdentTable_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 5, 3, 1)
)
if mibBuilder.loadTexts:
    mpduDeviceIdentTable.setStatus("mandatory")
_MpduDeviceIdentEntry_Object = MibTableRow
mpduDeviceIdentEntry = _MpduDeviceIdentEntry_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 5, 3, 1, 1)
)
mpduDeviceIdentEntry.setIndexNames(
    (0, "CPQPOWER-MIB", "mpduIdentIndex"),
    (0, "CPQPOWER-MIB", "mpduDeviceIdentIndex"),
)
if mibBuilder.loadTexts:
    mpduDeviceIdentEntry.setStatus("mandatory")


class _MpduDeviceIdentIndex_Type(Integer32):
    """Custom type mpduDeviceIdentIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_MpduDeviceIdentIndex_Type.__name__ = "Integer32"
_MpduDeviceIdentIndex_Object = MibTableColumn
mpduDeviceIdentIndex = _MpduDeviceIdentIndex_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 5, 3, 1, 1, 1),
    _MpduDeviceIdentIndex_Type()
)
mpduDeviceIdentIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpduDeviceIdentIndex.setStatus("mandatory")
_MpduDeviceStatus_Type = DisplayString
_MpduDeviceStatus_Object = MibTableColumn
mpduDeviceStatus = _MpduDeviceStatus_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 5, 3, 1, 1, 2),
    _MpduDeviceStatus_Type()
)
mpduDeviceStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpduDeviceStatus.setStatus("mandatory")
_MpduDeviceUIDStatus_Type = DisplayString
_MpduDeviceUIDStatus_Object = MibTableColumn
mpduDeviceUIDStatus = _MpduDeviceUIDStatus_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 5, 3, 1, 1, 3),
    _MpduDeviceUIDStatus_Type()
)
mpduDeviceUIDStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpduDeviceUIDStatus.setStatus("mandatory")
_MpduDeviceNumOutlet_Type = Integer32
_MpduDeviceNumOutlet_Object = MibTableColumn
mpduDeviceNumOutlet = _MpduDeviceNumOutlet_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 5, 3, 1, 1, 4),
    _MpduDeviceNumOutlet_Type()
)
mpduDeviceNumOutlet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpduDeviceNumOutlet.setStatus("mandatory")
_MpduDeviceUHeight_Type = Integer32
_MpduDeviceUHeight_Object = MibTableColumn
mpduDeviceUHeight = _MpduDeviceUHeight_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 5, 3, 1, 1, 5),
    _MpduDeviceUHeight_Type()
)
mpduDeviceUHeight.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpduDeviceUHeight.setStatus("mandatory")
_MpduDevicePowerRating_Type = DisplayString
_MpduDevicePowerRating_Object = MibTableColumn
mpduDevicePowerRating = _MpduDevicePowerRating_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 5, 3, 1, 1, 6),
    _MpduDevicePowerRating_Type()
)
mpduDevicePowerRating.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpduDevicePowerRating.setStatus("mandatory")
_MpduDeviceManufacturer_Type = DisplayString
_MpduDeviceManufacturer_Object = MibTableColumn
mpduDeviceManufacturer = _MpduDeviceManufacturer_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 5, 3, 1, 1, 7),
    _MpduDeviceManufacturer_Type()
)
mpduDeviceManufacturer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpduDeviceManufacturer.setStatus("mandatory")
_MpduDeviceType_Type = DisplayString
_MpduDeviceType_Object = MibTableColumn
mpduDeviceType = _MpduDeviceType_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 5, 3, 1, 1, 8),
    _MpduDeviceType_Type()
)
mpduDeviceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpduDeviceType.setStatus("mandatory")
_MpduDeviceModel_Type = DisplayString
_MpduDeviceModel_Object = MibTableColumn
mpduDeviceModel = _MpduDeviceModel_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 5, 3, 1, 1, 9),
    _MpduDeviceModel_Type()
)
mpduDeviceModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpduDeviceModel.setStatus("mandatory")
_MpduDeviceName_Type = DisplayString
_MpduDeviceName_Object = MibTableColumn
mpduDeviceName = _MpduDeviceName_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 5, 3, 1, 1, 10),
    _MpduDeviceName_Type()
)
mpduDeviceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpduDeviceName.setStatus("mandatory")
_MpduDeviceFirmwareVersion_Type = DisplayString
_MpduDeviceFirmwareVersion_Object = MibTableColumn
mpduDeviceFirmwareVersion = _MpduDeviceFirmwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 5, 3, 1, 1, 11),
    _MpduDeviceFirmwareVersion_Type()
)
mpduDeviceFirmwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpduDeviceFirmwareVersion.setStatus("mandatory")
_MpduDeviceHardwareVersion_Type = DisplayString
_MpduDeviceHardwareVersion_Object = MibTableColumn
mpduDeviceHardwareVersion = _MpduDeviceHardwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 5, 3, 1, 1, 12),
    _MpduDeviceHardwareVersion_Type()
)
mpduDeviceHardwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpduDeviceHardwareVersion.setStatus("mandatory")
_MpduDevicePartNumber_Type = DisplayString
_MpduDevicePartNumber_Object = MibTableColumn
mpduDevicePartNumber = _MpduDevicePartNumber_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 5, 3, 1, 1, 13),
    _MpduDevicePartNumber_Type()
)
mpduDevicePartNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpduDevicePartNumber.setStatus("mandatory")
_MpduDeviceSerialNumber_Type = DisplayString
_MpduDeviceSerialNumber_Object = MibTableColumn
mpduDeviceSerialNumber = _MpduDeviceSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 5, 3, 1, 1, 14),
    _MpduDeviceSerialNumber_Type()
)
mpduDeviceSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpduDeviceSerialNumber.setStatus("mandatory")
_MpduDeviceUUID_Type = DisplayString
_MpduDeviceUUID_Object = MibTableColumn
mpduDeviceUUID = _MpduDeviceUUID_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 5, 3, 1, 1, 15),
    _MpduDeviceUUID_Type()
)
mpduDeviceUUID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpduDeviceUUID.setStatus("mandatory")
_MpduDeviceIP_Type = DisplayString
_MpduDeviceIP_Object = MibTableColumn
mpduDeviceIP = _MpduDeviceIP_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 5, 3, 1, 1, 16),
    _MpduDeviceIP_Type()
)
mpduDeviceIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpduDeviceIP.setStatus("mandatory")
_MpduDeviceMAC_Type = DisplayString
_MpduDeviceMAC_Object = MibTableColumn
mpduDeviceMAC = _MpduDeviceMAC_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 5, 3, 1, 1, 17),
    _MpduDeviceMAC_Type()
)
mpduDeviceMAC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpduDeviceMAC.setStatus("mandatory")
_MpduDevicePSUSlotNo_Type = Integer32
_MpduDevicePSUSlotNo_Object = MibTableColumn
mpduDevicePSUSlotNo = _MpduDevicePSUSlotNo_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 5, 3, 1, 1, 18),
    _MpduDevicePSUSlotNo_Type()
)
mpduDevicePSUSlotNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpduDevicePSUSlotNo.setStatus("mandatory")
_MpduDeviceUPosition_Type = Integer32
_MpduDeviceUPosition_Object = MibTableColumn
mpduDeviceUPosition = _MpduDeviceUPosition_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 5, 3, 1, 1, 19),
    _MpduDeviceUPosition_Type()
)
mpduDeviceUPosition.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpduDeviceUPosition.setStatus("mandatory")
_MpduDeviceDetectionThreshold_Type = Integer32
_MpduDeviceDetectionThreshold_Object = MibTableColumn
mpduDeviceDetectionThreshold = _MpduDeviceDetectionThreshold_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 5, 3, 1, 1, 20),
    _MpduDeviceDetectionThreshold_Type()
)
mpduDeviceDetectionThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpduDeviceDetectionThreshold.setStatus("mandatory")
_MpduSmExtBarOutlet_ObjectIdentity = ObjectIdentity
mpduSmExtBarOutlet = _MpduSmExtBarOutlet_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 165, 5, 4)
)
_MpduSmExtBarOutletTable_Object = MibTable
mpduSmExtBarOutletTable = _MpduSmExtBarOutletTable_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 5, 4, 1)
)
if mibBuilder.loadTexts:
    mpduSmExtBarOutletTable.setStatus("mandatory")
_MpduSmExtBarOutletEntry_Object = MibTableRow
mpduSmExtBarOutletEntry = _MpduSmExtBarOutletEntry_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 5, 4, 1, 1)
)
mpduSmExtBarOutletEntry.setIndexNames(
    (0, "CPQPOWER-MIB", "mpduIdentIndex"),
    (0, "CPQPOWER-MIB", "mpduOutputIndex"),
    (0, "CPQPOWER-MIB", "mpduSmExtBarOutletIndex"),
)
if mibBuilder.loadTexts:
    mpduSmExtBarOutletEntry.setStatus("mandatory")


class _MpduSmExtBarOutletIndex_Type(Integer32):
    """Custom type mpduSmExtBarOutletIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_MpduSmExtBarOutletIndex_Type.__name__ = "Integer32"
_MpduSmExtBarOutletIndex_Object = MibTableColumn
mpduSmExtBarOutletIndex = _MpduSmExtBarOutletIndex_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 5, 4, 1, 1, 1),
    _MpduSmExtBarOutletIndex_Type()
)
mpduSmExtBarOutletIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpduSmExtBarOutletIndex.setStatus("mandatory")
_MpduSmExtBarOutletStatus_Type = DisplayString
_MpduSmExtBarOutletStatus_Object = MibTableColumn
mpduSmExtBarOutletStatus = _MpduSmExtBarOutletStatus_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 5, 4, 1, 1, 2),
    _MpduSmExtBarOutletStatus_Type()
)
mpduSmExtBarOutletStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpduSmExtBarOutletStatus.setStatus("mandatory")
_MpduSmExtBarOutletUIDStatus_Type = DisplayString
_MpduSmExtBarOutletUIDStatus_Object = MibTableColumn
mpduSmExtBarOutletUIDStatus = _MpduSmExtBarOutletUIDStatus_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 5, 4, 1, 1, 3),
    _MpduSmExtBarOutletUIDStatus_Type()
)
mpduSmExtBarOutletUIDStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpduSmExtBarOutletUIDStatus.setStatus("mandatory")
_MpduSmExtBarOutletRating_Type = Integer32
_MpduSmExtBarOutletRating_Object = MibTableColumn
mpduSmExtBarOutletRating = _MpduSmExtBarOutletRating_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 5, 4, 1, 1, 4),
    _MpduSmExtBarOutletRating_Type()
)
mpduSmExtBarOutletRating.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpduSmExtBarOutletRating.setStatus("mandatory")
_MpduSmExtBarOutletVoltage_Type = Integer32
_MpduSmExtBarOutletVoltage_Object = MibTableColumn
mpduSmExtBarOutletVoltage = _MpduSmExtBarOutletVoltage_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 5, 4, 1, 1, 5),
    _MpduSmExtBarOutletVoltage_Type()
)
mpduSmExtBarOutletVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpduSmExtBarOutletVoltage.setStatus("mandatory")
_MpduSmExtBarOutletCurrent_Type = Integer32
_MpduSmExtBarOutletCurrent_Object = MibTableColumn
mpduSmExtBarOutletCurrent = _MpduSmExtBarOutletCurrent_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 5, 4, 1, 1, 6),
    _MpduSmExtBarOutletCurrent_Type()
)
mpduSmExtBarOutletCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpduSmExtBarOutletCurrent.setStatus("mandatory")
_MpduSmExtBarOutletPowerWatt_Type = Integer32
_MpduSmExtBarOutletPowerWatt_Object = MibTableColumn
mpduSmExtBarOutletPowerWatt = _MpduSmExtBarOutletPowerWatt_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 5, 4, 1, 1, 7),
    _MpduSmExtBarOutletPowerWatt_Type()
)
mpduSmExtBarOutletPowerWatt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpduSmExtBarOutletPowerWatt.setStatus("mandatory")
_MpduSmExtBarOutletPowerFactor_Type = Integer32
_MpduSmExtBarOutletPowerFactor_Object = MibTableColumn
mpduSmExtBarOutletPowerFactor = _MpduSmExtBarOutletPowerFactor_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 5, 4, 1, 1, 8),
    _MpduSmExtBarOutletPowerFactor_Type()
)
mpduSmExtBarOutletPowerFactor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpduSmExtBarOutletPowerFactor.setStatus("mandatory")
_MpduSmExtBarOutletDeviceName_Type = DisplayString
_MpduSmExtBarOutletDeviceName_Object = MibTableColumn
mpduSmExtBarOutletDeviceName = _MpduSmExtBarOutletDeviceName_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 5, 4, 1, 1, 9),
    _MpduSmExtBarOutletDeviceName_Type()
)
mpduSmExtBarOutletDeviceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpduSmExtBarOutletDeviceName.setStatus("mandatory")
_MpduSmExtBarOutletDeviceUUID_Type = DisplayString
_MpduSmExtBarOutletDeviceUUID_Object = MibTableColumn
mpduSmExtBarOutletDeviceUUID = _MpduSmExtBarOutletDeviceUUID_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 5, 4, 1, 1, 10),
    _MpduSmExtBarOutletDeviceUUID_Type()
)
mpduSmExtBarOutletDeviceUUID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpduSmExtBarOutletDeviceUUID.setStatus("mandatory")
_MpduSmExtBarOutletDeviceProduct_Type = DisplayString
_MpduSmExtBarOutletDeviceProduct_Object = MibTableColumn
mpduSmExtBarOutletDeviceProduct = _MpduSmExtBarOutletDeviceProduct_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 5, 4, 1, 1, 11),
    _MpduSmExtBarOutletDeviceProduct_Type()
)
mpduSmExtBarOutletDeviceProduct.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpduSmExtBarOutletDeviceProduct.setStatus("mandatory")
_MpduSmExtBarOutletDeviceIP_Type = DisplayString
_MpduSmExtBarOutletDeviceIP_Object = MibTableColumn
mpduSmExtBarOutletDeviceIP = _MpduSmExtBarOutletDeviceIP_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 5, 4, 1, 1, 12),
    _MpduSmExtBarOutletDeviceIP_Type()
)
mpduSmExtBarOutletDeviceIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpduSmExtBarOutletDeviceIP.setStatus("mandatory")
_MpduSmExtBarOutletAutoDiscovered_Type = Integer32
_MpduSmExtBarOutletAutoDiscovered_Object = MibTableColumn
mpduSmExtBarOutletAutoDiscovered = _MpduSmExtBarOutletAutoDiscovered_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 5, 4, 1, 1, 13),
    _MpduSmExtBarOutletAutoDiscovered_Type()
)
mpduSmExtBarOutletAutoDiscovered.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpduSmExtBarOutletAutoDiscovered.setStatus("mandatory")
_MpduSmExtBarOutletDeviceMAC_Type = DisplayString
_MpduSmExtBarOutletDeviceMAC_Object = MibTableColumn
mpduSmExtBarOutletDeviceMAC = _MpduSmExtBarOutletDeviceMAC_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 5, 4, 1, 1, 14),
    _MpduSmExtBarOutletDeviceMAC_Type()
)
mpduSmExtBarOutletDeviceMAC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpduSmExtBarOutletDeviceMAC.setStatus("mandatory")
_MpduSmExtBarOutletDeviceSN_Type = DisplayString
_MpduSmExtBarOutletDeviceSN_Object = MibTableColumn
mpduSmExtBarOutletDeviceSN = _MpduSmExtBarOutletDeviceSN_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 5, 4, 1, 1, 15),
    _MpduSmExtBarOutletDeviceSN_Type()
)
mpduSmExtBarOutletDeviceSN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpduSmExtBarOutletDeviceSN.setStatus("mandatory")
_MpduSmExtBarOutletDevicePSSlotNo_Type = Integer32
_MpduSmExtBarOutletDevicePSSlotNo_Object = MibTableColumn
mpduSmExtBarOutletDevicePSSlotNo = _MpduSmExtBarOutletDevicePSSlotNo_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 5, 4, 1, 1, 16),
    _MpduSmExtBarOutletDevicePSSlotNo_Type()
)
mpduSmExtBarOutletDevicePSSlotNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpduSmExtBarOutletDevicePSSlotNo.setStatus("mandatory")
_MpduSmExtBarOutletDeviceUPosition_Type = Integer32
_MpduSmExtBarOutletDeviceUPosition_Object = MibTableColumn
mpduSmExtBarOutletDeviceUPosition = _MpduSmExtBarOutletDeviceUPosition_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 5, 4, 1, 1, 17),
    _MpduSmExtBarOutletDeviceUPosition_Type()
)
mpduSmExtBarOutletDeviceUPosition.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpduSmExtBarOutletDeviceUPosition.setStatus("mandatory")
_MpduSmExtBarOutletDeviceUHeight_Type = Integer32
_MpduSmExtBarOutletDeviceUHeight_Object = MibTableColumn
mpduSmExtBarOutletDeviceUHeight = _MpduSmExtBarOutletDeviceUHeight_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 5, 4, 1, 1, 18),
    _MpduSmExtBarOutletDeviceUHeight_Type()
)
mpduSmExtBarOutletDeviceUHeight.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpduSmExtBarOutletDeviceUHeight.setStatus("mandatory")
_MpduSmExtBarOutletDeviceInstalledLocation_Type = Integer32
_MpduSmExtBarOutletDeviceInstalledLocation_Object = MibTableColumn
mpduSmExtBarOutletDeviceInstalledLocation = _MpduSmExtBarOutletDeviceInstalledLocation_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 5, 4, 1, 1, 19),
    _MpduSmExtBarOutletDeviceInstalledLocation_Type()
)
mpduSmExtBarOutletDeviceInstalledLocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpduSmExtBarOutletDeviceInstalledLocation.setStatus("mandatory")
_MpduSmExtBarOutletPowerWattHour_Type = Integer32
_MpduSmExtBarOutletPowerWattHour_Object = MibTableColumn
mpduSmExtBarOutletPowerWattHour = _MpduSmExtBarOutletPowerWattHour_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 5, 4, 1, 1, 20),
    _MpduSmExtBarOutletPowerWattHour_Type()
)
mpduSmExtBarOutletPowerWattHour.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpduSmExtBarOutletPowerWattHour.setStatus("mandatory")
_Oups_ObjectIdentity = ObjectIdentity
oups = _Oups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 165, 6)
)
_OupsIdent_ObjectIdentity = ObjectIdentity
oupsIdent = _OupsIdent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 165, 6, 1)
)


class _OupsIdentManufacturer_Type(DisplayString):
    """Custom type oupsIdentManufacturer based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_OupsIdentManufacturer_Type.__name__ = "DisplayString"
_OupsIdentManufacturer_Object = MibScalar
oupsIdentManufacturer = _OupsIdentManufacturer_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 6, 1, 1),
    _OupsIdentManufacturer_Type()
)
oupsIdentManufacturer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oupsIdentManufacturer.setStatus("mandatory")


class _OupsIdentModel_Type(DisplayString):
    """Custom type oupsIdentModel based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_OupsIdentModel_Type.__name__ = "DisplayString"
_OupsIdentModel_Object = MibScalar
oupsIdentModel = _OupsIdentModel_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 6, 1, 2),
    _OupsIdentModel_Type()
)
oupsIdentModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oupsIdentModel.setStatus("mandatory")


class _OupsIdentSystemFWVersion_Type(DisplayString):
    """Custom type oupsIdentSystemFWVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_OupsIdentSystemFWVersion_Type.__name__ = "DisplayString"
_OupsIdentSystemFWVersion_Object = MibScalar
oupsIdentSystemFWVersion = _OupsIdentSystemFWVersion_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 6, 1, 3),
    _OupsIdentSystemFWVersion_Type()
)
oupsIdentSystemFWVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oupsIdentSystemFWVersion.setStatus("mandatory")


class _OupsIdentPowerModuleFWVersion_Type(DisplayString):
    """Custom type oupsIdentPowerModuleFWVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_OupsIdentPowerModuleFWVersion_Type.__name__ = "DisplayString"
_OupsIdentPowerModuleFWVersion_Object = MibScalar
oupsIdentPowerModuleFWVersion = _OupsIdentPowerModuleFWVersion_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 6, 1, 4),
    _OupsIdentPowerModuleFWVersion_Type()
)
oupsIdentPowerModuleFWVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oupsIdentPowerModuleFWVersion.setStatus("mandatory")


class _OupsIdentOemCode_Type(DisplayString):
    """Custom type oupsIdentOemCode based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_OupsIdentOemCode_Type.__name__ = "DisplayString"
_OupsIdentOemCode_Object = MibScalar
oupsIdentOemCode = _OupsIdentOemCode_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 6, 1, 5),
    _OupsIdentOemCode_Type()
)
oupsIdentOemCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oupsIdentOemCode.setStatus("mandatory")


class _OupsIdentSerialNumber_Type(DisplayString):
    """Custom type oupsIdentSerialNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_OupsIdentSerialNumber_Type.__name__ = "DisplayString"
_OupsIdentSerialNumber_Object = MibScalar
oupsIdentSerialNumber = _OupsIdentSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 6, 1, 6),
    _OupsIdentSerialNumber_Type()
)
oupsIdentSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oupsIdentSerialNumber.setStatus("mandatory")


class _OupsIdentPartNumber_Type(DisplayString):
    """Custom type oupsIdentPartNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_OupsIdentPartNumber_Type.__name__ = "DisplayString"
_OupsIdentPartNumber_Object = MibScalar
oupsIdentPartNumber = _OupsIdentPartNumber_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 6, 1, 7),
    _OupsIdentPartNumber_Type()
)
oupsIdentPartNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oupsIdentPartNumber.setStatus("mandatory")
_OupsBattery_ObjectIdentity = ObjectIdentity
oupsBattery = _OupsBattery_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 165, 6, 2)
)


class _OupsBatTimeRemaining_Type(Integer32):
    """Custom type oupsBatTimeRemaining based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_OupsBatTimeRemaining_Type.__name__ = "Integer32"
_OupsBatTimeRemaining_Object = MibScalar
oupsBatTimeRemaining = _OupsBatTimeRemaining_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 6, 2, 1),
    _OupsBatTimeRemaining_Type()
)
oupsBatTimeRemaining.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oupsBatTimeRemaining.setStatus("mandatory")


class _OupsBatVoltage_Type(Integer32):
    """Custom type oupsBatVoltage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_OupsBatVoltage_Type.__name__ = "Integer32"
_OupsBatVoltage_Object = MibScalar
oupsBatVoltage = _OupsBatVoltage_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 6, 2, 2),
    _OupsBatVoltage_Type()
)
oupsBatVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oupsBatVoltage.setStatus("mandatory")


class _OupsBatCapacity_Type(Integer32):
    """Custom type oupsBatCapacity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_OupsBatCapacity_Type.__name__ = "Integer32"
_OupsBatCapacity_Object = MibScalar
oupsBatCapacity = _OupsBatCapacity_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 6, 2, 3),
    _OupsBatCapacity_Type()
)
oupsBatCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oupsBatCapacity.setStatus("mandatory")


class _OupsBatAbmStatus_Type(Integer32):
    """Custom type oupsBatAbmStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("batteryCharging", 1),
          ("batteryDischarging", 2),
          ("batteryResting", 3),
          ("batteryTesting", 4),
          ("notAvailable", 5))
    )


_OupsBatAbmStatus_Type.__name__ = "Integer32"
_OupsBatAbmStatus_Object = MibScalar
oupsBatAbmStatus = _OupsBatAbmStatus_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 6, 2, 4),
    _OupsBatAbmStatus_Type()
)
oupsBatAbmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oupsBatAbmStatus.setStatus("mandatory")


class _OupsBatTestStatus_Type(Integer32):
    """Custom type oupsBatTestStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 1),
          ("passed", 2),
          ("failed", 3),
          ("inProgress", 4),
          ("notSupported", 5),
          ("inhibited", 6))
    )


_OupsBatTestStatus_Type.__name__ = "Integer32"
_OupsBatTestStatus_Object = MibScalar
oupsBatTestStatus = _OupsBatTestStatus_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 6, 2, 5),
    _OupsBatTestStatus_Type()
)
oupsBatTestStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oupsBatTestStatus.setStatus("mandatory")


class _OupsBatLatestTestDate_Type(DisplayString):
    """Custom type oupsBatLatestTestDate based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_OupsBatLatestTestDate_Type.__name__ = "DisplayString"
_OupsBatLatestTestDate_Object = MibScalar
oupsBatLatestTestDate = _OupsBatLatestTestDate_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 6, 2, 6),
    _OupsBatLatestTestDate_Type()
)
oupsBatLatestTestDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oupsBatLatestTestDate.setStatus("mandatory")


class _OupsBatReplacementDateBP1_Type(DisplayString):
    """Custom type oupsBatReplacementDateBP1 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_OupsBatReplacementDateBP1_Type.__name__ = "DisplayString"
_OupsBatReplacementDateBP1_Object = MibScalar
oupsBatReplacementDateBP1 = _OupsBatReplacementDateBP1_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 6, 2, 7),
    _OupsBatReplacementDateBP1_Type()
)
oupsBatReplacementDateBP1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oupsBatReplacementDateBP1.setStatus("mandatory")


class _OupsBatReplacementDateBP2_Type(DisplayString):
    """Custom type oupsBatReplacementDateBP2 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_OupsBatReplacementDateBP2_Type.__name__ = "DisplayString"
_OupsBatReplacementDateBP2_Object = MibScalar
oupsBatReplacementDateBP2 = _OupsBatReplacementDateBP2_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 6, 2, 8),
    _OupsBatReplacementDateBP2_Type()
)
oupsBatReplacementDateBP2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oupsBatReplacementDateBP2.setStatus("mandatory")


class _OupsBatToACDelay_Type(Integer32):
    """Custom type oupsBatToACDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 150),
    )


_OupsBatToACDelay_Type.__name__ = "Integer32"
_OupsBatToACDelay_Object = MibScalar
oupsBatToACDelay = _OupsBatToACDelay_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 6, 2, 9),
    _OupsBatToACDelay_Type()
)
oupsBatToACDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oupsBatToACDelay.setStatus("mandatory")


class _OupsBatChargeDelay_Type(Integer32):
    """Custom type oupsBatChargeDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 9999),
    )


_OupsBatChargeDelay_Type.__name__ = "Integer32"
_OupsBatChargeDelay_Object = MibScalar
oupsBatChargeDelay = _OupsBatChargeDelay_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 6, 2, 10),
    _OupsBatChargeDelay_Type()
)
oupsBatChargeDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oupsBatChargeDelay.setStatus("mandatory")


class _OupsBatNumModules_Type(Integer32):
    """Custom type oupsBatNumModules based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_OupsBatNumModules_Type.__name__ = "Integer32"
_OupsBatNumModules_Object = MibScalar
oupsBatNumModules = _OupsBatNumModules_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 6, 2, 11),
    _OupsBatNumModules_Type()
)
oupsBatNumModules.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oupsBatNumModules.setStatus("mandatory")


class _OupsBatModel_Type(DisplayString):
    """Custom type oupsBatModel based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_OupsBatModel_Type.__name__ = "DisplayString"
_OupsBatModel_Object = MibScalar
oupsBatModel = _OupsBatModel_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 6, 2, 12),
    _OupsBatModel_Type()
)
oupsBatModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oupsBatModel.setStatus("mandatory")


class _OupsBatChargingPowerLevelUtility_Type(DisplayString):
    """Custom type oupsBatChargingPowerLevelUtility based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_OupsBatChargingPowerLevelUtility_Type.__name__ = "DisplayString"
_OupsBatChargingPowerLevelUtility_Object = MibScalar
oupsBatChargingPowerLevelUtility = _OupsBatChargingPowerLevelUtility_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 6, 2, 13),
    _OupsBatChargingPowerLevelUtility_Type()
)
oupsBatChargingPowerLevelUtility.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oupsBatChargingPowerLevelUtility.setStatus("mandatory")


class _OupsBatChargingPowerLevelGenerator_Type(DisplayString):
    """Custom type oupsBatChargingPowerLevelGenerator based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_OupsBatChargingPowerLevelGenerator_Type.__name__ = "DisplayString"
_OupsBatChargingPowerLevelGenerator_Object = MibScalar
oupsBatChargingPowerLevelGenerator = _OupsBatChargingPowerLevelGenerator_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 6, 2, 14),
    _OupsBatChargingPowerLevelGenerator_Type()
)
oupsBatChargingPowerLevelGenerator.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oupsBatChargingPowerLevelGenerator.setStatus("mandatory")


class _OupsBatSharedConfig_Type(DisplayString):
    """Custom type oupsBatSharedConfig based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_OupsBatSharedConfig_Type.__name__ = "DisplayString"
_OupsBatSharedConfig_Object = MibScalar
oupsBatSharedConfig = _OupsBatSharedConfig_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 6, 2, 15),
    _OupsBatSharedConfig_Type()
)
oupsBatSharedConfig.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oupsBatSharedConfig.setStatus("mandatory")


class _OupsBatPackFWVerBP1_Type(DisplayString):
    """Custom type oupsBatPackFWVerBP1 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_OupsBatPackFWVerBP1_Type.__name__ = "DisplayString"
_OupsBatPackFWVerBP1_Object = MibScalar
oupsBatPackFWVerBP1 = _OupsBatPackFWVerBP1_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 6, 2, 16),
    _OupsBatPackFWVerBP1_Type()
)
oupsBatPackFWVerBP1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oupsBatPackFWVerBP1.setStatus("mandatory")


class _OupsBatPackFWVerBP2_Type(DisplayString):
    """Custom type oupsBatPackFWVerBP2 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_OupsBatPackFWVerBP2_Type.__name__ = "DisplayString"
_OupsBatPackFWVerBP2_Object = MibScalar
oupsBatPackFWVerBP2 = _OupsBatPackFWVerBP2_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 6, 2, 17),
    _OupsBatPackFWVerBP2_Type()
)
oupsBatPackFWVerBP2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oupsBatPackFWVerBP2.setStatus("mandatory")
_OupsInput_ObjectIdentity = ObjectIdentity
oupsInput = _OupsInput_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 165, 6, 3)
)


class _OupsInputFrequency_Type(Integer32):
    """Custom type oupsInputFrequency based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_OupsInputFrequency_Type.__name__ = "Integer32"
_OupsInputFrequency_Object = MibScalar
oupsInputFrequency = _OupsInputFrequency_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 6, 3, 1),
    _OupsInputFrequency_Type()
)
oupsInputFrequency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oupsInputFrequency.setStatus("mandatory")


class _OupsInputLineBads_Type(Integer32):
    """Custom type oupsInputLineBads based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 6),
    )


_OupsInputLineBads_Type.__name__ = "Integer32"
_OupsInputLineBads_Object = MibScalar
oupsInputLineBads = _OupsInputLineBads_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 6, 3, 2),
    _OupsInputLineBads_Type()
)
oupsInputLineBads.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oupsInputLineBads.setStatus("mandatory")


class _OupsInputNumPhases_Type(Integer32):
    """Custom type oupsInputNumPhases based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 6),
    )


_OupsInputNumPhases_Type.__name__ = "Integer32"
_OupsInputNumPhases_Object = MibScalar
oupsInputNumPhases = _OupsInputNumPhases_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 6, 3, 3),
    _OupsInputNumPhases_Type()
)
oupsInputNumPhases.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oupsInputNumPhases.setStatus("mandatory")
_OupsInputTable_Object = MibTable
oupsInputTable = _OupsInputTable_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 6, 3, 4)
)
if mibBuilder.loadTexts:
    oupsInputTable.setStatus("mandatory")
_OupsInputEntry_Object = MibTableRow
oupsInputEntry = _OupsInputEntry_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 6, 3, 4, 1)
)
oupsInputEntry.setIndexNames(
    (0, "CPQPOWER-MIB", "oupsInputPhase"),
)
if mibBuilder.loadTexts:
    oupsInputEntry.setStatus("mandatory")


class _OupsInputPhase_Type(Integer32):
    """Custom type oupsInputPhase based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 6),
    )


_OupsInputPhase_Type.__name__ = "Integer32"
_OupsInputPhase_Object = MibTableColumn
oupsInputPhase = _OupsInputPhase_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 6, 3, 4, 1, 1),
    _OupsInputPhase_Type()
)
oupsInputPhase.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oupsInputPhase.setStatus("mandatory")


class _OupsInputVoltage_Type(Integer32):
    """Custom type oupsInputVoltage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_OupsInputVoltage_Type.__name__ = "Integer32"
_OupsInputVoltage_Object = MibTableColumn
oupsInputVoltage = _OupsInputVoltage_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 6, 3, 4, 1, 2),
    _OupsInputVoltage_Type()
)
oupsInputVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oupsInputVoltage.setStatus("mandatory")


class _OupsInputCurrent_Type(Integer32):
    """Custom type oupsInputCurrent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_OupsInputCurrent_Type.__name__ = "Integer32"
_OupsInputCurrent_Object = MibTableColumn
oupsInputCurrent = _OupsInputCurrent_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 6, 3, 4, 1, 3),
    _OupsInputCurrent_Type()
)
oupsInputCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oupsInputCurrent.setStatus("mandatory")


class _OupsInputWatts_Type(Integer32):
    """Custom type oupsInputWatts based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_OupsInputWatts_Type.__name__ = "Integer32"
_OupsInputWatts_Object = MibTableColumn
oupsInputWatts = _OupsInputWatts_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 6, 3, 4, 1, 4),
    _OupsInputWatts_Type()
)
oupsInputWatts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oupsInputWatts.setStatus("mandatory")


class _OupsInputPowerFactor_Type(Integer32):
    """Custom type oupsInputPowerFactor based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_OupsInputPowerFactor_Type.__name__ = "Integer32"
_OupsInputPowerFactor_Object = MibScalar
oupsInputPowerFactor = _OupsInputPowerFactor_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 6, 3, 5),
    _OupsInputPowerFactor_Type()
)
oupsInputPowerFactor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oupsInputPowerFactor.setStatus("mandatory")


class _OupsInputDBType_Type(DisplayString):
    """Custom type oupsInputDBType based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_OupsInputDBType_Type.__name__ = "DisplayString"
_OupsInputDBType_Object = MibScalar
oupsInputDBType = _OupsInputDBType_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 6, 3, 6),
    _OupsInputDBType_Type()
)
oupsInputDBType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oupsInputDBType.setStatus("mandatory")


class _OupsInputUpperVoltage_Type(Integer32):
    """Custom type oupsInputUpperVoltage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 999),
    )


_OupsInputUpperVoltage_Type.__name__ = "Integer32"
_OupsInputUpperVoltage_Object = MibScalar
oupsInputUpperVoltage = _OupsInputUpperVoltage_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 6, 3, 7),
    _OupsInputUpperVoltage_Type()
)
oupsInputUpperVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oupsInputUpperVoltage.setStatus("mandatory")


class _OupsInputLowerVoltage_Type(Integer32):
    """Custom type oupsInputLowerVoltage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 999),
    )


_OupsInputLowerVoltage_Type.__name__ = "Integer32"
_OupsInputLowerVoltage_Object = MibScalar
oupsInputLowerVoltage = _OupsInputLowerVoltage_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 6, 3, 8),
    _OupsInputLowerVoltage_Type()
)
oupsInputLowerVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oupsInputLowerVoltage.setStatus("mandatory")


class _OupsGeneratorDetection_Type(Integer32):
    """Custom type oupsGeneratorDetection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("onGenerator", 1),
          ("offGenerator", 2),
          ("noAction", 3))
    )


_OupsGeneratorDetection_Type.__name__ = "Integer32"
_OupsGeneratorDetection_Object = MibScalar
oupsGeneratorDetection = _OupsGeneratorDetection_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 6, 3, 9),
    _OupsGeneratorDetection_Type()
)
oupsGeneratorDetection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oupsGeneratorDetection.setStatus("mandatory")


class _OupsInputWithGenerator_Type(Integer32):
    """Custom type oupsInputWithGenerator based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("woGenerator", 1),
          ("withGenerator", 2))
    )


_OupsInputWithGenerator_Type.__name__ = "Integer32"
_OupsInputWithGenerator_Object = MibScalar
oupsInputWithGenerator = _OupsInputWithGenerator_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 6, 3, 10),
    _OupsInputWithGenerator_Type()
)
oupsInputWithGenerator.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oupsInputWithGenerator.setStatus("mandatory")
_OupsOutput_ObjectIdentity = ObjectIdentity
oupsOutput = _OupsOutput_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 165, 6, 4)
)


class _OupsOutputLoad_Type(Integer32):
    """Custom type oupsOutputLoad based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 200),
    )


_OupsOutputLoad_Type.__name__ = "Integer32"
_OupsOutputLoad_Object = MibScalar
oupsOutputLoad = _OupsOutputLoad_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 6, 4, 1),
    _OupsOutputLoad_Type()
)
oupsOutputLoad.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oupsOutputLoad.setStatus("mandatory")


class _OupsOutputFrequency_Type(Integer32):
    """Custom type oupsOutputFrequency based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_OupsOutputFrequency_Type.__name__ = "Integer32"
_OupsOutputFrequency_Object = MibScalar
oupsOutputFrequency = _OupsOutputFrequency_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 6, 4, 2),
    _OupsOutputFrequency_Type()
)
oupsOutputFrequency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oupsOutputFrequency.setStatus("mandatory")


class _OupsOutputNumPhases_Type(Integer32):
    """Custom type oupsOutputNumPhases based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 6),
    )


_OupsOutputNumPhases_Type.__name__ = "Integer32"
_OupsOutputNumPhases_Object = MibScalar
oupsOutputNumPhases = _OupsOutputNumPhases_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 6, 4, 3),
    _OupsOutputNumPhases_Type()
)
oupsOutputNumPhases.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oupsOutputNumPhases.setStatus("mandatory")
_OupsOutputTable_Object = MibTable
oupsOutputTable = _OupsOutputTable_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 6, 4, 4)
)
if mibBuilder.loadTexts:
    oupsOutputTable.setStatus("mandatory")
_OupsOutputEntry_Object = MibTableRow
oupsOutputEntry = _OupsOutputEntry_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 6, 4, 4, 1)
)
oupsOutputEntry.setIndexNames(
    (0, "CPQPOWER-MIB", "oupsOutputPhase"),
)
if mibBuilder.loadTexts:
    oupsOutputEntry.setStatus("mandatory")


class _OupsOutputPhase_Type(Integer32):
    """Custom type oupsOutputPhase based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 6),
    )


_OupsOutputPhase_Type.__name__ = "Integer32"
_OupsOutputPhase_Object = MibTableColumn
oupsOutputPhase = _OupsOutputPhase_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 6, 4, 4, 1, 1),
    _OupsOutputPhase_Type()
)
oupsOutputPhase.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oupsOutputPhase.setStatus("mandatory")


class _OupsOutputVoltage_Type(Integer32):
    """Custom type oupsOutputVoltage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_OupsOutputVoltage_Type.__name__ = "Integer32"
_OupsOutputVoltage_Object = MibTableColumn
oupsOutputVoltage = _OupsOutputVoltage_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 6, 4, 4, 1, 2),
    _OupsOutputVoltage_Type()
)
oupsOutputVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oupsOutputVoltage.setStatus("mandatory")


class _OupsOutputCurrent_Type(Integer32):
    """Custom type oupsOutputCurrent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_OupsOutputCurrent_Type.__name__ = "Integer32"
_OupsOutputCurrent_Object = MibTableColumn
oupsOutputCurrent = _OupsOutputCurrent_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 6, 4, 4, 1, 3),
    _OupsOutputCurrent_Type()
)
oupsOutputCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oupsOutputCurrent.setStatus("mandatory")


class _OupsOutputWatts_Type(Integer32):
    """Custom type oupsOutputWatts based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_OupsOutputWatts_Type.__name__ = "Integer32"
_OupsOutputWatts_Object = MibTableColumn
oupsOutputWatts = _OupsOutputWatts_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 6, 4, 4, 1, 4),
    _OupsOutputWatts_Type()
)
oupsOutputWatts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oupsOutputWatts.setStatus("mandatory")


class _OupsOutputLoadPerPhase_Type(Integer32):
    """Custom type oupsOutputLoadPerPhase based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 200),
    )


_OupsOutputLoadPerPhase_Type.__name__ = "Integer32"
_OupsOutputLoadPerPhase_Object = MibTableColumn
oupsOutputLoadPerPhase = _OupsOutputLoadPerPhase_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 6, 4, 4, 1, 5),
    _OupsOutputLoadPerPhase_Type()
)
oupsOutputLoadPerPhase.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oupsOutputLoadPerPhase.setStatus("mandatory")


class _OupsOutputPowerFactor_Type(Integer32):
    """Custom type oupsOutputPowerFactor based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_OupsOutputPowerFactor_Type.__name__ = "Integer32"
_OupsOutputPowerFactor_Object = MibScalar
oupsOutputPowerFactor = _OupsOutputPowerFactor_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 6, 4, 5),
    _OupsOutputPowerFactor_Type()
)
oupsOutputPowerFactor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oupsOutputPowerFactor.setStatus("mandatory")


class _OupsOutputSource_Type(Integer32):
    """Custom type oupsOutputSource based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("acSource", 1),
          ("battery", 2))
    )


_OupsOutputSource_Type.__name__ = "Integer32"
_OupsOutputSource_Object = MibScalar
oupsOutputSource = _OupsOutputSource_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 6, 4, 6),
    _OupsOutputSource_Type()
)
oupsOutputSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oupsOutputSource.setStatus("mandatory")
_OupsMonitor_ObjectIdentity = ObjectIdentity
oupsMonitor = _OupsMonitor_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 165, 6, 5)
)


class _OupsMonitorAmbientTemp_Type(Integer32):
    """Custom type oupsMonitorAmbientTemp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-100, 200),
    )


_OupsMonitorAmbientTemp_Type.__name__ = "Integer32"
_OupsMonitorAmbientTemp_Object = MibScalar
oupsMonitorAmbientTemp = _OupsMonitorAmbientTemp_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 6, 5, 1),
    _OupsMonitorAmbientTemp_Type()
)
oupsMonitorAmbientTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oupsMonitorAmbientTemp.setStatus("mandatory")


class _OupsMonitorBypassSCRTemp_Type(Integer32):
    """Custom type oupsMonitorBypassSCRTemp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-100, 200),
    )


_OupsMonitorBypassSCRTemp_Type.__name__ = "Integer32"
_OupsMonitorBypassSCRTemp_Object = MibScalar
oupsMonitorBypassSCRTemp = _OupsMonitorBypassSCRTemp_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 6, 5, 2),
    _OupsMonitorBypassSCRTemp_Type()
)
oupsMonitorBypassSCRTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oupsMonitorBypassSCRTemp.setStatus("mandatory")


class _OupsMonitorDDTemp_Type(Integer32):
    """Custom type oupsMonitorDDTemp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-100, 200),
    )


_OupsMonitorDDTemp_Type.__name__ = "Integer32"
_OupsMonitorDDTemp_Object = MibScalar
oupsMonitorDDTemp = _OupsMonitorDDTemp_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 6, 5, 3),
    _OupsMonitorDDTemp_Type()
)
oupsMonitorDDTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oupsMonitorDDTemp.setStatus("mandatory")


class _OupsMonitorInverterTemp_Type(Integer32):
    """Custom type oupsMonitorInverterTemp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-100, 200),
    )


_OupsMonitorInverterTemp_Type.__name__ = "Integer32"
_OupsMonitorInverterTemp_Object = MibScalar
oupsMonitorInverterTemp = _OupsMonitorInverterTemp_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 6, 5, 4),
    _OupsMonitorInverterTemp_Type()
)
oupsMonitorInverterTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oupsMonitorInverterTemp.setStatus("mandatory")


class _OupsMonitorChargerTemp_Type(Integer32):
    """Custom type oupsMonitorChargerTemp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-100, 200),
    )


_OupsMonitorChargerTemp_Type.__name__ = "Integer32"
_OupsMonitorChargerTemp_Object = MibScalar
oupsMonitorChargerTemp = _OupsMonitorChargerTemp_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 6, 5, 5),
    _OupsMonitorChargerTemp_Type()
)
oupsMonitorChargerTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oupsMonitorChargerTemp.setStatus("mandatory")


class _OupsMonitorBP1Temp_Type(DisplayString):
    """Custom type oupsMonitorBP1Temp based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_OupsMonitorBP1Temp_Type.__name__ = "DisplayString"
_OupsMonitorBP1Temp_Object = MibScalar
oupsMonitorBP1Temp = _OupsMonitorBP1Temp_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 6, 5, 6),
    _OupsMonitorBP1Temp_Type()
)
oupsMonitorBP1Temp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oupsMonitorBP1Temp.setStatus("mandatory")


class _OupsMonitorBP2Temp_Type(DisplayString):
    """Custom type oupsMonitorBP2Temp based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_OupsMonitorBP2Temp_Type.__name__ = "DisplayString"
_OupsMonitorBP2Temp_Object = MibScalar
oupsMonitorBP2Temp = _OupsMonitorBP2Temp_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 6, 5, 7),
    _OupsMonitorBP2Temp_Type()
)
oupsMonitorBP2Temp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oupsMonitorBP2Temp.setStatus("mandatory")


class _OupsMonitorRestartDelay_Type(Integer32):
    """Custom type oupsMonitorRestartDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 150),
    )


_OupsMonitorRestartDelay_Type.__name__ = "Integer32"
_OupsMonitorRestartDelay_Object = MibScalar
oupsMonitorRestartDelay = _OupsMonitorRestartDelay_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 6, 5, 8),
    _OupsMonitorRestartDelay_Type()
)
oupsMonitorRestartDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oupsMonitorRestartDelay.setStatus("mandatory")


class _OupsMonitorACCLoadLevel_Type(DisplayString):
    """Custom type oupsMonitorACCLoadLevel based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_OupsMonitorACCLoadLevel_Type.__name__ = "DisplayString"
_OupsMonitorACCLoadLevel_Object = MibScalar
oupsMonitorACCLoadLevel = _OupsMonitorACCLoadLevel_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 6, 5, 9),
    _OupsMonitorACCLoadLevel_Type()
)
oupsMonitorACCLoadLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oupsMonitorACCLoadLevel.setStatus("mandatory")


class _OupsMonitorOperatingMode_Type(DisplayString):
    """Custom type oupsMonitorOperatingMode based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_OupsMonitorOperatingMode_Type.__name__ = "DisplayString"
_OupsMonitorOperatingMode_Object = MibScalar
oupsMonitorOperatingMode = _OupsMonitorOperatingMode_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 6, 5, 10),
    _OupsMonitorOperatingMode_Type()
)
oupsMonitorOperatingMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oupsMonitorOperatingMode.setStatus("mandatory")


class _OupsMonitorOperationType_Type(DisplayString):
    """Custom type oupsMonitorOperationType based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_OupsMonitorOperationType_Type.__name__ = "DisplayString"
_OupsMonitorOperationType_Object = MibScalar
oupsMonitorOperationType = _OupsMonitorOperationType_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 6, 5, 11),
    _OupsMonitorOperationType_Type()
)
oupsMonitorOperationType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oupsMonitorOperationType.setStatus("mandatory")


class _OupsTestTrap_Type(Integer32):
    """Custom type oupsTestTrap based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("startTestTrap", 1)
    )


_OupsTestTrap_Type.__name__ = "Integer32"
_OupsTestTrap_Object = MibScalar
oupsTestTrap = _OupsTestTrap_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 6, 5, 12),
    _OupsTestTrap_Type()
)
oupsTestTrap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oupsTestTrap.setStatus("mandatory")


class _OupsOnGenDuration_Type(Integer32):
    """Custom type oupsOnGenDuration based on Integer32"""
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
        *(("for30Min", 1),
          ("for1Hr", 2),
          ("for2Hr", 3),
          ("for4Hr", 4))
    )


_OupsOnGenDuration_Type.__name__ = "Integer32"
_OupsOnGenDuration_Object = MibScalar
oupsOnGenDuration = _OupsOnGenDuration_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 6, 5, 13),
    _OupsOnGenDuration_Type()
)
oupsOnGenDuration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oupsOnGenDuration.setStatus("mandatory")


class _OupsRuntimeLimitation_Type(Integer32):
    """Custom type oupsRuntimeLimitation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_OupsRuntimeLimitation_Type.__name__ = "Integer32"
_OupsRuntimeLimitation_Object = MibScalar
oupsRuntimeLimitation = _OupsRuntimeLimitation_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 6, 5, 14),
    _OupsRuntimeLimitation_Type()
)
oupsRuntimeLimitation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oupsRuntimeLimitation.setStatus("mandatory")
_OupsRackDiscovery_ObjectIdentity = ObjectIdentity
oupsRackDiscovery = _OupsRackDiscovery_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 165, 6, 6)
)


class _OupsRackTagVersion_Type(Integer32):
    """Custom type oupsRackTagVersion based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10),
    )


_OupsRackTagVersion_Type.__name__ = "Integer32"
_OupsRackTagVersion_Object = MibScalar
oupsRackTagVersion = _OupsRackTagVersion_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 6, 6, 1),
    _OupsRackTagVersion_Type()
)
oupsRackTagVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oupsRackTagVersion.setStatus("mandatory")


class _OupsRackID_Type(DisplayString):
    """Custom type oupsRackID based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_OupsRackID_Type.__name__ = "DisplayString"
_OupsRackID_Object = MibScalar
oupsRackID = _OupsRackID_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 6, 6, 2),
    _OupsRackID_Type()
)
oupsRackID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oupsRackID.setStatus("mandatory")


class _OupsRackPartNumber_Type(DisplayString):
    """Custom type oupsRackPartNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_OupsRackPartNumber_Type.__name__ = "DisplayString"
_OupsRackPartNumber_Object = MibScalar
oupsRackPartNumber = _OupsRackPartNumber_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 6, 6, 3),
    _OupsRackPartNumber_Type()
)
oupsRackPartNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oupsRackPartNumber.setStatus("mandatory")


class _OupsRackProductDescription_Type(DisplayString):
    """Custom type oupsRackProductDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_OupsRackProductDescription_Type.__name__ = "DisplayString"
_OupsRackProductDescription_Object = MibScalar
oupsRackProductDescription = _OupsRackProductDescription_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 6, 6, 4),
    _OupsRackProductDescription_Type()
)
oupsRackProductDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oupsRackProductDescription.setStatus("mandatory")


class _OupsRackEncULocation_Type(DisplayString):
    """Custom type oupsRackEncULocation based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_OupsRackEncULocation_Type.__name__ = "DisplayString"
_OupsRackEncULocation_Object = MibScalar
oupsRackEncULocation = _OupsRackEncULocation_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 6, 6, 5),
    _OupsRackEncULocation_Type()
)
oupsRackEncULocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oupsRackEncULocation.setStatus("mandatory")


class _OupsRackUHeight_Type(Integer32):
    """Custom type oupsRackUHeight based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 50),
    )


_OupsRackUHeight_Type.__name__ = "Integer32"
_OupsRackUHeight_Object = MibScalar
oupsRackUHeight = _OupsRackUHeight_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 6, 6, 6),
    _OupsRackUHeight_Type()
)
oupsRackUHeight.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oupsRackUHeight.setStatus("mandatory")


class _OupsRackPUUPosition_Type(Integer32):
    """Custom type oupsRackPUUPosition based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 50),
    )


_OupsRackPUUPosition_Type.__name__ = "Integer32"
_OupsRackPUUPosition_Object = MibScalar
oupsRackPUUPosition = _OupsRackPUUPosition_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 6, 6, 7),
    _OupsRackPUUPosition_Type()
)
oupsRackPUUPosition.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oupsRackPUUPosition.setStatus("mandatory")


class _OupsRackPUUHeight_Type(Integer32):
    """Custom type oupsRackPUUHeight based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10),
    )


_OupsRackPUUHeight_Type.__name__ = "Integer32"
_OupsRackPUUHeight_Object = MibScalar
oupsRackPUUHeight = _OupsRackPUUHeight_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 6, 6, 8),
    _OupsRackPUUHeight_Type()
)
oupsRackPUUHeight.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oupsRackPUUHeight.setStatus("mandatory")


class _OupsRackBP1UPosition_Type(Integer32):
    """Custom type oupsRackBP1UPosition based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 50),
    )


_OupsRackBP1UPosition_Type.__name__ = "Integer32"
_OupsRackBP1UPosition_Object = MibScalar
oupsRackBP1UPosition = _OupsRackBP1UPosition_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 6, 6, 9),
    _OupsRackBP1UPosition_Type()
)
oupsRackBP1UPosition.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oupsRackBP1UPosition.setStatus("mandatory")


class _OupsRackBP1UHeight_Type(Integer32):
    """Custom type oupsRackBP1UHeight based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10),
    )


_OupsRackBP1UHeight_Type.__name__ = "Integer32"
_OupsRackBP1UHeight_Object = MibScalar
oupsRackBP1UHeight = _OupsRackBP1UHeight_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 6, 6, 10),
    _OupsRackBP1UHeight_Type()
)
oupsRackBP1UHeight.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oupsRackBP1UHeight.setStatus("mandatory")


class _OupsRackBP2UPosition_Type(Integer32):
    """Custom type oupsRackBP2UPosition based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 50),
    )


_OupsRackBP2UPosition_Type.__name__ = "Integer32"
_OupsRackBP2UPosition_Object = MibScalar
oupsRackBP2UPosition = _OupsRackBP2UPosition_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 6, 6, 11),
    _OupsRackBP2UPosition_Type()
)
oupsRackBP2UPosition.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oupsRackBP2UPosition.setStatus("mandatory")


class _OupsRackBP2UHeight_Type(Integer32):
    """Custom type oupsRackBP2UHeight based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10),
    )


_OupsRackBP2UHeight_Type.__name__ = "Integer32"
_OupsRackBP2UHeight_Object = MibScalar
oupsRackBP2UHeight = _OupsRackBP2UHeight_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 6, 6, 12),
    _OupsRackBP2UHeight_Type()
)
oupsRackBP2UHeight.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oupsRackBP2UHeight.setStatus("mandatory")
_Pdu2_ObjectIdentity = ObjectIdentity
pdu2 = _Pdu2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 165, 7)
)
_Pdu2Ident_ObjectIdentity = ObjectIdentity
pdu2Ident = _Pdu2Ident_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 165, 7, 1)
)


class _Pdu2NumberPDU_Type(Integer32):
    """Custom type pdu2NumberPDU based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_Pdu2NumberPDU_Type.__name__ = "Integer32"
_Pdu2NumberPDU_Object = MibScalar
pdu2NumberPDU = _Pdu2NumberPDU_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 7, 1, 1),
    _Pdu2NumberPDU_Type()
)
pdu2NumberPDU.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu2NumberPDU.setStatus("mandatory")
_Pdu2IdentTable_Object = MibTable
pdu2IdentTable = _Pdu2IdentTable_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 7, 1, 2)
)
if mibBuilder.loadTexts:
    pdu2IdentTable.setStatus("mandatory")
_Pdu2IdentEntry_Object = MibTableRow
pdu2IdentEntry = _Pdu2IdentEntry_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 7, 1, 2, 1)
)
pdu2IdentEntry.setIndexNames(
    (0, "CPQPOWER-MIB", "pdu2IdentIndex"),
)
if mibBuilder.loadTexts:
    pdu2IdentEntry.setStatus("mandatory")


class _Pdu2IdentIndex_Type(Integer32):
    """Custom type pdu2IdentIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Pdu2IdentIndex_Type.__name__ = "Integer32"
_Pdu2IdentIndex_Object = MibTableColumn
pdu2IdentIndex = _Pdu2IdentIndex_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 7, 1, 2, 1, 1),
    _Pdu2IdentIndex_Type()
)
pdu2IdentIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu2IdentIndex.setStatus("mandatory")


class _Pdu2Name_Type(DisplayString):
    """Custom type pdu2Name based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_Pdu2Name_Type.__name__ = "DisplayString"
_Pdu2Name_Object = MibTableColumn
pdu2Name = _Pdu2Name_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 7, 1, 2, 1, 2),
    _Pdu2Name_Type()
)
pdu2Name.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu2Name.setStatus("mandatory")


class _Pdu2Model_Type(DisplayString):
    """Custom type pdu2Model based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_Pdu2Model_Type.__name__ = "DisplayString"
_Pdu2Model_Object = MibTableColumn
pdu2Model = _Pdu2Model_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 7, 1, 2, 1, 3),
    _Pdu2Model_Type()
)
pdu2Model.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu2Model.setStatus("mandatory")


class _Pdu2Manufacturer_Type(DisplayString):
    """Custom type pdu2Manufacturer based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_Pdu2Manufacturer_Type.__name__ = "DisplayString"
_Pdu2Manufacturer_Object = MibTableColumn
pdu2Manufacturer = _Pdu2Manufacturer_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 7, 1, 2, 1, 4),
    _Pdu2Manufacturer_Type()
)
pdu2Manufacturer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu2Manufacturer.setStatus("mandatory")


class _Pdu2FirmwareVersion_Type(DisplayString):
    """Custom type pdu2FirmwareVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_Pdu2FirmwareVersion_Type.__name__ = "DisplayString"
_Pdu2FirmwareVersion_Object = MibTableColumn
pdu2FirmwareVersion = _Pdu2FirmwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 7, 1, 2, 1, 5),
    _Pdu2FirmwareVersion_Type()
)
pdu2FirmwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu2FirmwareVersion.setStatus("mandatory")


class _Pdu2PartNumber_Type(DisplayString):
    """Custom type pdu2PartNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_Pdu2PartNumber_Type.__name__ = "DisplayString"
_Pdu2PartNumber_Object = MibTableColumn
pdu2PartNumber = _Pdu2PartNumber_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 7, 1, 2, 1, 6),
    _Pdu2PartNumber_Type()
)
pdu2PartNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu2PartNumber.setStatus("mandatory")


class _Pdu2SerialNumber_Type(DisplayString):
    """Custom type pdu2SerialNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_Pdu2SerialNumber_Type.__name__ = "DisplayString"
_Pdu2SerialNumber_Object = MibTableColumn
pdu2SerialNumber = _Pdu2SerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 7, 1, 2, 1, 7),
    _Pdu2SerialNumber_Type()
)
pdu2SerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu2SerialNumber.setStatus("mandatory")


class _Pdu2Status_Type(Integer32):
    """Custom type pdu2Status based on Integer32"""
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
        *(("other", 1),
          ("ok", 2),
          ("degraded", 3),
          ("failed", 4))
    )


_Pdu2Status_Type.__name__ = "Integer32"
_Pdu2Status_Object = MibTableColumn
pdu2Status = _Pdu2Status_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 7, 1, 2, 1, 8),
    _Pdu2Status_Type()
)
pdu2Status.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu2Status.setStatus("mandatory")


class _Pdu2Controllable_Type(Integer32):
    """Custom type pdu2Controllable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("yes", 1),
          ("no", 2))
    )


_Pdu2Controllable_Type.__name__ = "Integer32"
_Pdu2Controllable_Object = MibTableColumn
pdu2Controllable = _Pdu2Controllable_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 7, 1, 2, 1, 9),
    _Pdu2Controllable_Type()
)
pdu2Controllable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu2Controllable.setStatus("mandatory")


class _Pdu2InputPhaseCount_Type(Integer32):
    """Custom type pdu2InputPhaseCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_Pdu2InputPhaseCount_Type.__name__ = "Integer32"
_Pdu2InputPhaseCount_Object = MibTableColumn
pdu2InputPhaseCount = _Pdu2InputPhaseCount_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 7, 1, 2, 1, 10),
    _Pdu2InputPhaseCount_Type()
)
pdu2InputPhaseCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu2InputPhaseCount.setStatus("mandatory")


class _Pdu2GroupCount_Type(Integer32):
    """Custom type pdu2GroupCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_Pdu2GroupCount_Type.__name__ = "Integer32"
_Pdu2GroupCount_Object = MibTableColumn
pdu2GroupCount = _Pdu2GroupCount_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 7, 1, 2, 1, 11),
    _Pdu2GroupCount_Type()
)
pdu2GroupCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu2GroupCount.setStatus("mandatory")


class _Pdu2OutletCount_Type(Integer32):
    """Custom type pdu2OutletCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_Pdu2OutletCount_Type.__name__ = "Integer32"
_Pdu2OutletCount_Object = MibTableColumn
pdu2OutletCount = _Pdu2OutletCount_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 7, 1, 2, 1, 12),
    _Pdu2OutletCount_Type()
)
pdu2OutletCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu2OutletCount.setStatus("mandatory")
_Pdu2Input_ObjectIdentity = ObjectIdentity
pdu2Input = _Pdu2Input_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 165, 7, 2)
)
_Pdu2InputTable_Object = MibTable
pdu2InputTable = _Pdu2InputTable_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 7, 2, 1)
)
if mibBuilder.loadTexts:
    pdu2InputTable.setStatus("mandatory")
_Pdu2InputEntry_Object = MibTableRow
pdu2InputEntry = _Pdu2InputEntry_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 7, 2, 1, 1)
)
pdu2InputEntry.setIndexNames(
    (0, "CPQPOWER-MIB", "pdu2IdentIndex"),
)
if mibBuilder.loadTexts:
    pdu2InputEntry.setStatus("mandatory")


class _Pdu2InputType_Type(Integer32):
    """Custom type pdu2InputType based on Integer32"""
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
        *(("singlePhase", 1),
          ("splitPhase", 2),
          ("threePhaseDelta", 3),
          ("threePhaseWye", 4))
    )


_Pdu2InputType_Type.__name__ = "Integer32"
_Pdu2InputType_Object = MibTableColumn
pdu2InputType = _Pdu2InputType_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 7, 2, 1, 1, 1),
    _Pdu2InputType_Type()
)
pdu2InputType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu2InputType.setStatus("mandatory")


class _Pdu2InputFrequency_Type(Integer32):
    """Custom type pdu2InputFrequency based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_Pdu2InputFrequency_Type.__name__ = "Integer32"
_Pdu2InputFrequency_Object = MibTableColumn
pdu2InputFrequency = _Pdu2InputFrequency_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 7, 2, 1, 1, 2),
    _Pdu2InputFrequency_Type()
)
pdu2InputFrequency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu2InputFrequency.setStatus("mandatory")


class _Pdu2InputFrequencyStatus_Type(Integer32):
    """Custom type pdu2InputFrequencyStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("good", 1),
          ("outOfRange", 2))
    )


_Pdu2InputFrequencyStatus_Type.__name__ = "Integer32"
_Pdu2InputFrequencyStatus_Object = MibTableColumn
pdu2InputFrequencyStatus = _Pdu2InputFrequencyStatus_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 7, 2, 1, 1, 3),
    _Pdu2InputFrequencyStatus_Type()
)
pdu2InputFrequencyStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu2InputFrequencyStatus.setStatus("mandatory")
_Pdu2InputPowerVA_Type = Integer32
_Pdu2InputPowerVA_Object = MibTableColumn
pdu2InputPowerVA = _Pdu2InputPowerVA_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 7, 2, 1, 1, 4),
    _Pdu2InputPowerVA_Type()
)
pdu2InputPowerVA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu2InputPowerVA.setStatus("mandatory")
_Pdu2InputPowerWatts_Type = Integer32
_Pdu2InputPowerWatts_Object = MibTableColumn
pdu2InputPowerWatts = _Pdu2InputPowerWatts_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 7, 2, 1, 1, 5),
    _Pdu2InputPowerWatts_Type()
)
pdu2InputPowerWatts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu2InputPowerWatts.setStatus("mandatory")
_Pdu2InputPowerWattHour_Type = Integer32
_Pdu2InputPowerWattHour_Object = MibTableColumn
pdu2InputPowerWattHour = _Pdu2InputPowerWattHour_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 7, 2, 1, 1, 6),
    _Pdu2InputPowerWattHour_Type()
)
pdu2InputPowerWattHour.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu2InputPowerWattHour.setStatus("mandatory")


class _Pdu2InputPowerWattHourTimer_Type(DisplayString):
    """Custom type pdu2InputPowerWattHourTimer based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 22),
    )


_Pdu2InputPowerWattHourTimer_Type.__name__ = "DisplayString"
_Pdu2InputPowerWattHourTimer_Object = MibTableColumn
pdu2InputPowerWattHourTimer = _Pdu2InputPowerWattHourTimer_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 7, 2, 1, 1, 7),
    _Pdu2InputPowerWattHourTimer_Type()
)
pdu2InputPowerWattHourTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu2InputPowerWattHourTimer.setStatus("mandatory")
_Pdu2InputPowerFactor_Type = Integer32
_Pdu2InputPowerFactor_Object = MibTableColumn
pdu2InputPowerFactor = _Pdu2InputPowerFactor_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 7, 2, 1, 1, 8),
    _Pdu2InputPowerFactor_Type()
)
pdu2InputPowerFactor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu2InputPowerFactor.setStatus("mandatory")
_Pdu2InputPowerVAR_Type = Integer32
_Pdu2InputPowerVAR_Object = MibTableColumn
pdu2InputPowerVAR = _Pdu2InputPowerVAR_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 7, 2, 1, 1, 9),
    _Pdu2InputPowerVAR_Type()
)
pdu2InputPowerVAR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu2InputPowerVAR.setStatus("mandatory")
_Pdu2InputPhaseTable_Object = MibTable
pdu2InputPhaseTable = _Pdu2InputPhaseTable_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 7, 2, 2)
)
if mibBuilder.loadTexts:
    pdu2InputPhaseTable.setStatus("mandatory")
_Pdu2InputPhaseEntry_Object = MibTableRow
pdu2InputPhaseEntry = _Pdu2InputPhaseEntry_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 7, 2, 2, 1)
)
pdu2InputPhaseEntry.setIndexNames(
    (0, "CPQPOWER-MIB", "pdu2IdentIndex"),
    (0, "CPQPOWER-MIB", "pdu2InputPhaseIndex"),
)
if mibBuilder.loadTexts:
    pdu2InputPhaseEntry.setStatus("mandatory")


class _Pdu2InputPhaseIndex_Type(Integer32):
    """Custom type pdu2InputPhaseIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Pdu2InputPhaseIndex_Type.__name__ = "Integer32"
_Pdu2InputPhaseIndex_Object = MibTableColumn
pdu2InputPhaseIndex = _Pdu2InputPhaseIndex_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 7, 2, 2, 1, 1),
    _Pdu2InputPhaseIndex_Type()
)
pdu2InputPhaseIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu2InputPhaseIndex.setStatus("mandatory")


class _Pdu2InputPhaseVoltageMeasType_Type(Integer32):
    """Custom type pdu2InputPhaseVoltageMeasType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("singlePhase", 1),
          ("phase1toN", 2),
          ("phase2toN", 3),
          ("phase3toN", 4),
          ("phase1to2", 5),
          ("phase2to3", 6),
          ("phase3to1", 7))
    )


_Pdu2InputPhaseVoltageMeasType_Type.__name__ = "Integer32"
_Pdu2InputPhaseVoltageMeasType_Object = MibTableColumn
pdu2InputPhaseVoltageMeasType = _Pdu2InputPhaseVoltageMeasType_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 7, 2, 2, 1, 2),
    _Pdu2InputPhaseVoltageMeasType_Type()
)
pdu2InputPhaseVoltageMeasType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu2InputPhaseVoltageMeasType.setStatus("mandatory")
_Pdu2InputPhaseVoltage_Type = Integer32
_Pdu2InputPhaseVoltage_Object = MibTableColumn
pdu2InputPhaseVoltage = _Pdu2InputPhaseVoltage_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 7, 2, 2, 1, 3),
    _Pdu2InputPhaseVoltage_Type()
)
pdu2InputPhaseVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu2InputPhaseVoltage.setStatus("mandatory")


class _Pdu2InputPhaseVoltageThStatus_Type(Integer32):
    """Custom type pdu2InputPhaseVoltageThStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("good", 1),
          ("lowWarning", 2),
          ("lowCritical", 3),
          ("highWarning", 4),
          ("highCritical", 5))
    )


_Pdu2InputPhaseVoltageThStatus_Type.__name__ = "Integer32"
_Pdu2InputPhaseVoltageThStatus_Object = MibTableColumn
pdu2InputPhaseVoltageThStatus = _Pdu2InputPhaseVoltageThStatus_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 7, 2, 2, 1, 4),
    _Pdu2InputPhaseVoltageThStatus_Type()
)
pdu2InputPhaseVoltageThStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu2InputPhaseVoltageThStatus.setStatus("mandatory")


class _Pdu2InputPhaseVoltageThLowerWarning_Type(Integer32):
    """Custom type pdu2InputPhaseVoltageThLowerWarning based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 500000),
    )


_Pdu2InputPhaseVoltageThLowerWarning_Type.__name__ = "Integer32"
_Pdu2InputPhaseVoltageThLowerWarning_Object = MibTableColumn
pdu2InputPhaseVoltageThLowerWarning = _Pdu2InputPhaseVoltageThLowerWarning_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 7, 2, 2, 1, 5),
    _Pdu2InputPhaseVoltageThLowerWarning_Type()
)
pdu2InputPhaseVoltageThLowerWarning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu2InputPhaseVoltageThLowerWarning.setStatus("mandatory")


class _Pdu2InputPhaseVoltageThLowerCritical_Type(Integer32):
    """Custom type pdu2InputPhaseVoltageThLowerCritical based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 500000),
    )


_Pdu2InputPhaseVoltageThLowerCritical_Type.__name__ = "Integer32"
_Pdu2InputPhaseVoltageThLowerCritical_Object = MibTableColumn
pdu2InputPhaseVoltageThLowerCritical = _Pdu2InputPhaseVoltageThLowerCritical_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 7, 2, 2, 1, 6),
    _Pdu2InputPhaseVoltageThLowerCritical_Type()
)
pdu2InputPhaseVoltageThLowerCritical.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu2InputPhaseVoltageThLowerCritical.setStatus("mandatory")


class _Pdu2InputPhaseVoltageThUpperWarning_Type(Integer32):
    """Custom type pdu2InputPhaseVoltageThUpperWarning based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 500000),
    )


_Pdu2InputPhaseVoltageThUpperWarning_Type.__name__ = "Integer32"
_Pdu2InputPhaseVoltageThUpperWarning_Object = MibTableColumn
pdu2InputPhaseVoltageThUpperWarning = _Pdu2InputPhaseVoltageThUpperWarning_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 7, 2, 2, 1, 7),
    _Pdu2InputPhaseVoltageThUpperWarning_Type()
)
pdu2InputPhaseVoltageThUpperWarning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu2InputPhaseVoltageThUpperWarning.setStatus("mandatory")


class _Pdu2InputPhaseVoltageThUpperCritical_Type(Integer32):
    """Custom type pdu2InputPhaseVoltageThUpperCritical based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 500000),
    )


_Pdu2InputPhaseVoltageThUpperCritical_Type.__name__ = "Integer32"
_Pdu2InputPhaseVoltageThUpperCritical_Object = MibTableColumn
pdu2InputPhaseVoltageThUpperCritical = _Pdu2InputPhaseVoltageThUpperCritical_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 7, 2, 2, 1, 8),
    _Pdu2InputPhaseVoltageThUpperCritical_Type()
)
pdu2InputPhaseVoltageThUpperCritical.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu2InputPhaseVoltageThUpperCritical.setStatus("mandatory")


class _Pdu2InputPhaseCurrentMeasType_Type(Integer32):
    """Custom type pdu2InputPhaseCurrentMeasType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("singlePhase", 1),
          ("neutral", 2),
          ("phase1", 3),
          ("phase2", 4),
          ("phase3", 5))
    )


_Pdu2InputPhaseCurrentMeasType_Type.__name__ = "Integer32"
_Pdu2InputPhaseCurrentMeasType_Object = MibTableColumn
pdu2InputPhaseCurrentMeasType = _Pdu2InputPhaseCurrentMeasType_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 7, 2, 2, 1, 9),
    _Pdu2InputPhaseCurrentMeasType_Type()
)
pdu2InputPhaseCurrentMeasType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu2InputPhaseCurrentMeasType.setStatus("mandatory")
_Pdu2InputPhaseCurrentRating_Type = Integer32
_Pdu2InputPhaseCurrentRating_Object = MibTableColumn
pdu2InputPhaseCurrentRating = _Pdu2InputPhaseCurrentRating_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 7, 2, 2, 1, 10),
    _Pdu2InputPhaseCurrentRating_Type()
)
pdu2InputPhaseCurrentRating.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu2InputPhaseCurrentRating.setStatus("mandatory")
_Pdu2InputPhaseCurrent_Type = Integer32
_Pdu2InputPhaseCurrent_Object = MibTableColumn
pdu2InputPhaseCurrent = _Pdu2InputPhaseCurrent_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 7, 2, 2, 1, 11),
    _Pdu2InputPhaseCurrent_Type()
)
pdu2InputPhaseCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu2InputPhaseCurrent.setStatus("mandatory")


class _Pdu2InputPhaseCurrentThStatus_Type(Integer32):
    """Custom type pdu2InputPhaseCurrentThStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("good", 1),
          ("lowWarning", 2),
          ("lowCritical", 3),
          ("highWarning", 4),
          ("highCritical", 5))
    )


_Pdu2InputPhaseCurrentThStatus_Type.__name__ = "Integer32"
_Pdu2InputPhaseCurrentThStatus_Object = MibTableColumn
pdu2InputPhaseCurrentThStatus = _Pdu2InputPhaseCurrentThStatus_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 7, 2, 2, 1, 12),
    _Pdu2InputPhaseCurrentThStatus_Type()
)
pdu2InputPhaseCurrentThStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu2InputPhaseCurrentThStatus.setStatus("mandatory")


class _Pdu2InputPhaseCurrentThLowerWarning_Type(Integer32):
    """Custom type pdu2InputPhaseCurrentThLowerWarning based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 100000),
    )


_Pdu2InputPhaseCurrentThLowerWarning_Type.__name__ = "Integer32"
_Pdu2InputPhaseCurrentThLowerWarning_Object = MibTableColumn
pdu2InputPhaseCurrentThLowerWarning = _Pdu2InputPhaseCurrentThLowerWarning_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 7, 2, 2, 1, 13),
    _Pdu2InputPhaseCurrentThLowerWarning_Type()
)
pdu2InputPhaseCurrentThLowerWarning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu2InputPhaseCurrentThLowerWarning.setStatus("mandatory")


class _Pdu2InputPhaseCurrentThLowerCritical_Type(Integer32):
    """Custom type pdu2InputPhaseCurrentThLowerCritical based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 100000),
    )


_Pdu2InputPhaseCurrentThLowerCritical_Type.__name__ = "Integer32"
_Pdu2InputPhaseCurrentThLowerCritical_Object = MibTableColumn
pdu2InputPhaseCurrentThLowerCritical = _Pdu2InputPhaseCurrentThLowerCritical_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 7, 2, 2, 1, 14),
    _Pdu2InputPhaseCurrentThLowerCritical_Type()
)
pdu2InputPhaseCurrentThLowerCritical.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu2InputPhaseCurrentThLowerCritical.setStatus("mandatory")


class _Pdu2InputPhaseCurrentThUpperWarning_Type(Integer32):
    """Custom type pdu2InputPhaseCurrentThUpperWarning based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 100000),
    )


_Pdu2InputPhaseCurrentThUpperWarning_Type.__name__ = "Integer32"
_Pdu2InputPhaseCurrentThUpperWarning_Object = MibTableColumn
pdu2InputPhaseCurrentThUpperWarning = _Pdu2InputPhaseCurrentThUpperWarning_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 7, 2, 2, 1, 15),
    _Pdu2InputPhaseCurrentThUpperWarning_Type()
)
pdu2InputPhaseCurrentThUpperWarning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu2InputPhaseCurrentThUpperWarning.setStatus("mandatory")


class _Pdu2InputPhaseCurrentThUpperCritical_Type(Integer32):
    """Custom type pdu2InputPhaseCurrentThUpperCritical based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 100000),
    )


_Pdu2InputPhaseCurrentThUpperCritical_Type.__name__ = "Integer32"
_Pdu2InputPhaseCurrentThUpperCritical_Object = MibTableColumn
pdu2InputPhaseCurrentThUpperCritical = _Pdu2InputPhaseCurrentThUpperCritical_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 7, 2, 2, 1, 16),
    _Pdu2InputPhaseCurrentThUpperCritical_Type()
)
pdu2InputPhaseCurrentThUpperCritical.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu2InputPhaseCurrentThUpperCritical.setStatus("mandatory")
_Pdu2InputPhaseCurrentCrestFactor_Type = Integer32
_Pdu2InputPhaseCurrentCrestFactor_Object = MibTableColumn
pdu2InputPhaseCurrentCrestFactor = _Pdu2InputPhaseCurrentCrestFactor_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 7, 2, 2, 1, 17),
    _Pdu2InputPhaseCurrentCrestFactor_Type()
)
pdu2InputPhaseCurrentCrestFactor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu2InputPhaseCurrentCrestFactor.setStatus("mandatory")
_Pdu2InputPhaseCurrentPercentLoad_Type = Integer32
_Pdu2InputPhaseCurrentPercentLoad_Object = MibTableColumn
pdu2InputPhaseCurrentPercentLoad = _Pdu2InputPhaseCurrentPercentLoad_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 7, 2, 2, 1, 18),
    _Pdu2InputPhaseCurrentPercentLoad_Type()
)
pdu2InputPhaseCurrentPercentLoad.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu2InputPhaseCurrentPercentLoad.setStatus("mandatory")


class _Pdu2InputPhasePowerMeasType_Type(Integer32):
    """Custom type pdu2InputPhasePowerMeasType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("singlePhase", 1),
          ("neutral", 2),
          ("phase1", 3),
          ("phase2", 4),
          ("phase3", 5))
    )


_Pdu2InputPhasePowerMeasType_Type.__name__ = "Integer32"
_Pdu2InputPhasePowerMeasType_Object = MibTableColumn
pdu2InputPhasePowerMeasType = _Pdu2InputPhasePowerMeasType_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 7, 2, 2, 1, 19),
    _Pdu2InputPhasePowerMeasType_Type()
)
pdu2InputPhasePowerMeasType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu2InputPhasePowerMeasType.setStatus("mandatory")
_Pdu2InputPhasePowerVA_Type = Integer32
_Pdu2InputPhasePowerVA_Object = MibTableColumn
pdu2InputPhasePowerVA = _Pdu2InputPhasePowerVA_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 7, 2, 2, 1, 20),
    _Pdu2InputPhasePowerVA_Type()
)
pdu2InputPhasePowerVA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu2InputPhasePowerVA.setStatus("mandatory")
_Pdu2InputPhasePowerWatts_Type = Integer32
_Pdu2InputPhasePowerWatts_Object = MibTableColumn
pdu2InputPhasePowerWatts = _Pdu2InputPhasePowerWatts_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 7, 2, 2, 1, 21),
    _Pdu2InputPhasePowerWatts_Type()
)
pdu2InputPhasePowerWatts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu2InputPhasePowerWatts.setStatus("mandatory")
_Pdu2InputPhasePowerWattHour_Type = Integer32
_Pdu2InputPhasePowerWattHour_Object = MibTableColumn
pdu2InputPhasePowerWattHour = _Pdu2InputPhasePowerWattHour_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 7, 2, 2, 1, 22),
    _Pdu2InputPhasePowerWattHour_Type()
)
pdu2InputPhasePowerWattHour.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu2InputPhasePowerWattHour.setStatus("mandatory")


class _Pdu2InputPhasePowerWattHourTimer_Type(DisplayString):
    """Custom type pdu2InputPhasePowerWattHourTimer based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 22),
    )


_Pdu2InputPhasePowerWattHourTimer_Type.__name__ = "DisplayString"
_Pdu2InputPhasePowerWattHourTimer_Object = MibTableColumn
pdu2InputPhasePowerWattHourTimer = _Pdu2InputPhasePowerWattHourTimer_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 7, 2, 2, 1, 23),
    _Pdu2InputPhasePowerWattHourTimer_Type()
)
pdu2InputPhasePowerWattHourTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu2InputPhasePowerWattHourTimer.setStatus("mandatory")
_Pdu2InputPhasePowerFactor_Type = Integer32
_Pdu2InputPhasePowerFactor_Object = MibTableColumn
pdu2InputPhasePowerFactor = _Pdu2InputPhasePowerFactor_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 7, 2, 2, 1, 24),
    _Pdu2InputPhasePowerFactor_Type()
)
pdu2InputPhasePowerFactor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu2InputPhasePowerFactor.setStatus("mandatory")
_Pdu2InputPhasePowerVAR_Type = Integer32
_Pdu2InputPhasePowerVAR_Object = MibTableColumn
pdu2InputPhasePowerVAR = _Pdu2InputPhasePowerVAR_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 7, 2, 2, 1, 25),
    _Pdu2InputPhasePowerVAR_Type()
)
pdu2InputPhasePowerVAR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu2InputPhasePowerVAR.setStatus("mandatory")
_Pdu2Group_ObjectIdentity = ObjectIdentity
pdu2Group = _Pdu2Group_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 165, 7, 3)
)
_Pdu2GroupTable_Object = MibTable
pdu2GroupTable = _Pdu2GroupTable_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 7, 3, 1)
)
if mibBuilder.loadTexts:
    pdu2GroupTable.setStatus("mandatory")
_Pdu2GroupEntry_Object = MibTableRow
pdu2GroupEntry = _Pdu2GroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 7, 3, 1, 1)
)
pdu2GroupEntry.setIndexNames(
    (0, "CPQPOWER-MIB", "pdu2IdentIndex"),
    (0, "CPQPOWER-MIB", "pdu2GroupIndex"),
)
if mibBuilder.loadTexts:
    pdu2GroupEntry.setStatus("mandatory")


class _Pdu2GroupIndex_Type(Integer32):
    """Custom type pdu2GroupIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Pdu2GroupIndex_Type.__name__ = "Integer32"
_Pdu2GroupIndex_Object = MibTableColumn
pdu2GroupIndex = _Pdu2GroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 7, 3, 1, 1, 1),
    _Pdu2GroupIndex_Type()
)
pdu2GroupIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu2GroupIndex.setStatus("mandatory")


class _Pdu2GroupName_Type(DisplayString):
    """Custom type pdu2GroupName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_Pdu2GroupName_Type.__name__ = "DisplayString"
_Pdu2GroupName_Object = MibTableColumn
pdu2GroupName = _Pdu2GroupName_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 7, 3, 1, 1, 2),
    _Pdu2GroupName_Type()
)
pdu2GroupName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu2GroupName.setStatus("mandatory")


class _Pdu2GroupType_Type(Integer32):
    """Custom type pdu2GroupType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("breaker1pole", 2),
          ("breaker2pole", 3),
          ("breaker3pole", 4),
          ("outletSection", 5))
    )


_Pdu2GroupType_Type.__name__ = "Integer32"
_Pdu2GroupType_Object = MibTableColumn
pdu2GroupType = _Pdu2GroupType_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 7, 3, 1, 1, 3),
    _Pdu2GroupType_Type()
)
pdu2GroupType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu2GroupType.setStatus("mandatory")


class _Pdu2GroupVoltageMeasType_Type(Integer32):
    """Custom type pdu2GroupVoltageMeasType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("singlePhase", 1),
          ("phase1toN", 2),
          ("phase2toN", 3),
          ("phase3toN", 4),
          ("phase1to2", 5),
          ("phase2to3", 6),
          ("phase3to1", 7))
    )


_Pdu2GroupVoltageMeasType_Type.__name__ = "Integer32"
_Pdu2GroupVoltageMeasType_Object = MibTableColumn
pdu2GroupVoltageMeasType = _Pdu2GroupVoltageMeasType_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 7, 3, 1, 1, 4),
    _Pdu2GroupVoltageMeasType_Type()
)
pdu2GroupVoltageMeasType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu2GroupVoltageMeasType.setStatus("mandatory")
_Pdu2GroupVoltage_Type = Integer32
_Pdu2GroupVoltage_Object = MibTableColumn
pdu2GroupVoltage = _Pdu2GroupVoltage_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 7, 3, 1, 1, 5),
    _Pdu2GroupVoltage_Type()
)
pdu2GroupVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu2GroupVoltage.setStatus("mandatory")


class _Pdu2GroupVoltageThStatus_Type(Integer32):
    """Custom type pdu2GroupVoltageThStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("good", 1),
          ("lowWarning", 2),
          ("lowCritical", 3),
          ("highWarning", 4),
          ("highCritical", 5))
    )


_Pdu2GroupVoltageThStatus_Type.__name__ = "Integer32"
_Pdu2GroupVoltageThStatus_Object = MibTableColumn
pdu2GroupVoltageThStatus = _Pdu2GroupVoltageThStatus_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 7, 3, 1, 1, 6),
    _Pdu2GroupVoltageThStatus_Type()
)
pdu2GroupVoltageThStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu2GroupVoltageThStatus.setStatus("mandatory")


class _Pdu2GroupVoltageThLowerWarning_Type(Integer32):
    """Custom type pdu2GroupVoltageThLowerWarning based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 500000),
    )


_Pdu2GroupVoltageThLowerWarning_Type.__name__ = "Integer32"
_Pdu2GroupVoltageThLowerWarning_Object = MibTableColumn
pdu2GroupVoltageThLowerWarning = _Pdu2GroupVoltageThLowerWarning_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 7, 3, 1, 1, 7),
    _Pdu2GroupVoltageThLowerWarning_Type()
)
pdu2GroupVoltageThLowerWarning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu2GroupVoltageThLowerWarning.setStatus("mandatory")


class _Pdu2GroupVoltageThLowerCritical_Type(Integer32):
    """Custom type pdu2GroupVoltageThLowerCritical based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 500000),
    )


_Pdu2GroupVoltageThLowerCritical_Type.__name__ = "Integer32"
_Pdu2GroupVoltageThLowerCritical_Object = MibTableColumn
pdu2GroupVoltageThLowerCritical = _Pdu2GroupVoltageThLowerCritical_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 7, 3, 1, 1, 8),
    _Pdu2GroupVoltageThLowerCritical_Type()
)
pdu2GroupVoltageThLowerCritical.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu2GroupVoltageThLowerCritical.setStatus("mandatory")


class _Pdu2GroupVoltageThUpperWarning_Type(Integer32):
    """Custom type pdu2GroupVoltageThUpperWarning based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 500000),
    )


_Pdu2GroupVoltageThUpperWarning_Type.__name__ = "Integer32"
_Pdu2GroupVoltageThUpperWarning_Object = MibTableColumn
pdu2GroupVoltageThUpperWarning = _Pdu2GroupVoltageThUpperWarning_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 7, 3, 1, 1, 9),
    _Pdu2GroupVoltageThUpperWarning_Type()
)
pdu2GroupVoltageThUpperWarning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu2GroupVoltageThUpperWarning.setStatus("mandatory")


class _Pdu2GroupVoltageThUpperCritical_Type(Integer32):
    """Custom type pdu2GroupVoltageThUpperCritical based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 500000),
    )


_Pdu2GroupVoltageThUpperCritical_Type.__name__ = "Integer32"
_Pdu2GroupVoltageThUpperCritical_Object = MibTableColumn
pdu2GroupVoltageThUpperCritical = _Pdu2GroupVoltageThUpperCritical_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 7, 3, 1, 1, 10),
    _Pdu2GroupVoltageThUpperCritical_Type()
)
pdu2GroupVoltageThUpperCritical.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu2GroupVoltageThUpperCritical.setStatus("mandatory")
_Pdu2groupCurrentRating_Type = Integer32
_Pdu2groupCurrentRating_Object = MibTableColumn
pdu2groupCurrentRating = _Pdu2groupCurrentRating_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 7, 3, 1, 1, 11),
    _Pdu2groupCurrentRating_Type()
)
pdu2groupCurrentRating.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu2groupCurrentRating.setStatus("mandatory")
_Pdu2GroupCurrent_Type = Integer32
_Pdu2GroupCurrent_Object = MibTableColumn
pdu2GroupCurrent = _Pdu2GroupCurrent_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 7, 3, 1, 1, 12),
    _Pdu2GroupCurrent_Type()
)
pdu2GroupCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu2GroupCurrent.setStatus("mandatory")


class _Pdu2GroupCurrentThStatus_Type(Integer32):
    """Custom type pdu2GroupCurrentThStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("good", 1),
          ("lowWarning", 2),
          ("lowCritical", 3),
          ("highWarning", 4),
          ("highCritical", 5))
    )


_Pdu2GroupCurrentThStatus_Type.__name__ = "Integer32"
_Pdu2GroupCurrentThStatus_Object = MibTableColumn
pdu2GroupCurrentThStatus = _Pdu2GroupCurrentThStatus_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 7, 3, 1, 1, 13),
    _Pdu2GroupCurrentThStatus_Type()
)
pdu2GroupCurrentThStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu2GroupCurrentThStatus.setStatus("mandatory")


class _Pdu2GroupCurrentThLowerWarning_Type(Integer32):
    """Custom type pdu2GroupCurrentThLowerWarning based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 100000),
    )


_Pdu2GroupCurrentThLowerWarning_Type.__name__ = "Integer32"
_Pdu2GroupCurrentThLowerWarning_Object = MibTableColumn
pdu2GroupCurrentThLowerWarning = _Pdu2GroupCurrentThLowerWarning_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 7, 3, 1, 1, 14),
    _Pdu2GroupCurrentThLowerWarning_Type()
)
pdu2GroupCurrentThLowerWarning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu2GroupCurrentThLowerWarning.setStatus("mandatory")


class _Pdu2GroupCurrentThLowerCritical_Type(Integer32):
    """Custom type pdu2GroupCurrentThLowerCritical based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 100000),
    )


_Pdu2GroupCurrentThLowerCritical_Type.__name__ = "Integer32"
_Pdu2GroupCurrentThLowerCritical_Object = MibTableColumn
pdu2GroupCurrentThLowerCritical = _Pdu2GroupCurrentThLowerCritical_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 7, 3, 1, 1, 15),
    _Pdu2GroupCurrentThLowerCritical_Type()
)
pdu2GroupCurrentThLowerCritical.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu2GroupCurrentThLowerCritical.setStatus("mandatory")


class _Pdu2GroupCurrentThUpperWarning_Type(Integer32):
    """Custom type pdu2GroupCurrentThUpperWarning based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 100000),
    )


_Pdu2GroupCurrentThUpperWarning_Type.__name__ = "Integer32"
_Pdu2GroupCurrentThUpperWarning_Object = MibTableColumn
pdu2GroupCurrentThUpperWarning = _Pdu2GroupCurrentThUpperWarning_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 7, 3, 1, 1, 16),
    _Pdu2GroupCurrentThUpperWarning_Type()
)
pdu2GroupCurrentThUpperWarning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu2GroupCurrentThUpperWarning.setStatus("mandatory")


class _Pdu2GroupCurrentThUpperCritical_Type(Integer32):
    """Custom type pdu2GroupCurrentThUpperCritical based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 100000),
    )


_Pdu2GroupCurrentThUpperCritical_Type.__name__ = "Integer32"
_Pdu2GroupCurrentThUpperCritical_Object = MibTableColumn
pdu2GroupCurrentThUpperCritical = _Pdu2GroupCurrentThUpperCritical_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 7, 3, 1, 1, 17),
    _Pdu2GroupCurrentThUpperCritical_Type()
)
pdu2GroupCurrentThUpperCritical.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu2GroupCurrentThUpperCritical.setStatus("mandatory")
_Pdu2GroupCurrentCrestFactor_Type = Integer32
_Pdu2GroupCurrentCrestFactor_Object = MibTableColumn
pdu2GroupCurrentCrestFactor = _Pdu2GroupCurrentCrestFactor_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 7, 3, 1, 1, 18),
    _Pdu2GroupCurrentCrestFactor_Type()
)
pdu2GroupCurrentCrestFactor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu2GroupCurrentCrestFactor.setStatus("mandatory")
_Pdu2GroupCurrentPercentLoad_Type = Integer32
_Pdu2GroupCurrentPercentLoad_Object = MibTableColumn
pdu2GroupCurrentPercentLoad = _Pdu2GroupCurrentPercentLoad_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 7, 3, 1, 1, 19),
    _Pdu2GroupCurrentPercentLoad_Type()
)
pdu2GroupCurrentPercentLoad.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu2GroupCurrentPercentLoad.setStatus("mandatory")
_Pdu2GroupPowerVA_Type = Integer32
_Pdu2GroupPowerVA_Object = MibTableColumn
pdu2GroupPowerVA = _Pdu2GroupPowerVA_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 7, 3, 1, 1, 20),
    _Pdu2GroupPowerVA_Type()
)
pdu2GroupPowerVA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu2GroupPowerVA.setStatus("mandatory")
_Pdu2GroupPowerWatts_Type = Integer32
_Pdu2GroupPowerWatts_Object = MibTableColumn
pdu2GroupPowerWatts = _Pdu2GroupPowerWatts_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 7, 3, 1, 1, 21),
    _Pdu2GroupPowerWatts_Type()
)
pdu2GroupPowerWatts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu2GroupPowerWatts.setStatus("mandatory")
_Pdu2GroupPowerWattHour_Type = Integer32
_Pdu2GroupPowerWattHour_Object = MibTableColumn
pdu2GroupPowerWattHour = _Pdu2GroupPowerWattHour_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 7, 3, 1, 1, 22),
    _Pdu2GroupPowerWattHour_Type()
)
pdu2GroupPowerWattHour.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu2GroupPowerWattHour.setStatus("mandatory")


class _Pdu2GroupPowerWattHourTimer_Type(DisplayString):
    """Custom type pdu2GroupPowerWattHourTimer based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 22),
    )


_Pdu2GroupPowerWattHourTimer_Type.__name__ = "DisplayString"
_Pdu2GroupPowerWattHourTimer_Object = MibTableColumn
pdu2GroupPowerWattHourTimer = _Pdu2GroupPowerWattHourTimer_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 7, 3, 1, 1, 23),
    _Pdu2GroupPowerWattHourTimer_Type()
)
pdu2GroupPowerWattHourTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu2GroupPowerWattHourTimer.setStatus("mandatory")
_Pdu2GroupPowerFactor_Type = Integer32
_Pdu2GroupPowerFactor_Object = MibTableColumn
pdu2GroupPowerFactor = _Pdu2GroupPowerFactor_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 7, 3, 1, 1, 24),
    _Pdu2GroupPowerFactor_Type()
)
pdu2GroupPowerFactor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu2GroupPowerFactor.setStatus("mandatory")
_Pdu2GroupPowerVAR_Type = Integer32
_Pdu2GroupPowerVAR_Object = MibTableColumn
pdu2GroupPowerVAR = _Pdu2GroupPowerVAR_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 7, 3, 1, 1, 25),
    _Pdu2GroupPowerVAR_Type()
)
pdu2GroupPowerVAR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu2GroupPowerVAR.setStatus("mandatory")


class _Pdu2GroupOutletCount_Type(Integer32):
    """Custom type pdu2GroupOutletCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_Pdu2GroupOutletCount_Type.__name__ = "Integer32"
_Pdu2GroupOutletCount_Object = MibTableColumn
pdu2GroupOutletCount = _Pdu2GroupOutletCount_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 7, 3, 1, 1, 26),
    _Pdu2GroupOutletCount_Type()
)
pdu2GroupOutletCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu2GroupOutletCount.setStatus("mandatory")


class _Pdu2GroupBreakerStatus_Type(Integer32):
    """Custom type pdu2GroupBreakerStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("notApplicable", 1),
          ("breakerOn", 2),
          ("breakerOff", 3))
    )


_Pdu2GroupBreakerStatus_Type.__name__ = "Integer32"
_Pdu2GroupBreakerStatus_Object = MibTableColumn
pdu2GroupBreakerStatus = _Pdu2GroupBreakerStatus_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 7, 3, 1, 1, 27),
    _Pdu2GroupBreakerStatus_Type()
)
pdu2GroupBreakerStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu2GroupBreakerStatus.setStatus("mandatory")
_Pdu2Environment_ObjectIdentity = ObjectIdentity
pdu2Environment = _Pdu2Environment_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 165, 7, 4)
)
_Pdu2EnvProbeTable_Object = MibTable
pdu2EnvProbeTable = _Pdu2EnvProbeTable_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 7, 4, 1)
)
if mibBuilder.loadTexts:
    pdu2EnvProbeTable.setStatus("mandatory")
_Pdu2EnvProbeEntry_Object = MibTableRow
pdu2EnvProbeEntry = _Pdu2EnvProbeEntry_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 7, 4, 1, 1)
)
pdu2EnvProbeEntry.setIndexNames(
    (0, "CPQPOWER-MIB", "pdu2IdentIndex"),
)
if mibBuilder.loadTexts:
    pdu2EnvProbeEntry.setStatus("mandatory")


class _Pdu2TemperatureScale_Type(Integer32):
    """Custom type pdu2TemperatureScale based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("celsius", 1),
          ("fahrenheit", 2))
    )


_Pdu2TemperatureScale_Type.__name__ = "Integer32"
_Pdu2TemperatureScale_Object = MibTableColumn
pdu2TemperatureScale = _Pdu2TemperatureScale_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 7, 4, 1, 1, 1),
    _Pdu2TemperatureScale_Type()
)
pdu2TemperatureScale.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu2TemperatureScale.setStatus("mandatory")
_Pdu2TemperatureCount_Type = Integer32
_Pdu2TemperatureCount_Object = MibTableColumn
pdu2TemperatureCount = _Pdu2TemperatureCount_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 7, 4, 1, 1, 2),
    _Pdu2TemperatureCount_Type()
)
pdu2TemperatureCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu2TemperatureCount.setStatus("mandatory")
_Pdu2HumidityCount_Type = Integer32
_Pdu2HumidityCount_Object = MibTableColumn
pdu2HumidityCount = _Pdu2HumidityCount_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 7, 4, 1, 1, 3),
    _Pdu2HumidityCount_Type()
)
pdu2HumidityCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu2HumidityCount.setStatus("mandatory")
_Pdu2ContactCount_Type = Integer32
_Pdu2ContactCount_Object = MibTableColumn
pdu2ContactCount = _Pdu2ContactCount_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 7, 4, 1, 1, 4),
    _Pdu2ContactCount_Type()
)
pdu2ContactCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu2ContactCount.setStatus("mandatory")
_Pdu2TemperatureTable_Object = MibTable
pdu2TemperatureTable = _Pdu2TemperatureTable_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 7, 4, 2)
)
if mibBuilder.loadTexts:
    pdu2TemperatureTable.setStatus("mandatory")
_Pdu2TemperatureEntry_Object = MibTableRow
pdu2TemperatureEntry = _Pdu2TemperatureEntry_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 7, 4, 2, 1)
)
pdu2TemperatureEntry.setIndexNames(
    (0, "CPQPOWER-MIB", "pdu2IdentIndex"),
    (0, "CPQPOWER-MIB", "pdu2TemperatureIndex"),
)
if mibBuilder.loadTexts:
    pdu2TemperatureEntry.setStatus("mandatory")


class _Pdu2TemperatureIndex_Type(Integer32):
    """Custom type pdu2TemperatureIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_Pdu2TemperatureIndex_Type.__name__ = "Integer32"
_Pdu2TemperatureIndex_Object = MibTableColumn
pdu2TemperatureIndex = _Pdu2TemperatureIndex_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 7, 4, 2, 1, 1),
    _Pdu2TemperatureIndex_Type()
)
pdu2TemperatureIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu2TemperatureIndex.setStatus("mandatory")


class _Pdu2TemperatureName_Type(DisplayString):
    """Custom type pdu2TemperatureName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_Pdu2TemperatureName_Type.__name__ = "DisplayString"
_Pdu2TemperatureName_Object = MibTableColumn
pdu2TemperatureName = _Pdu2TemperatureName_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 7, 4, 2, 1, 2),
    _Pdu2TemperatureName_Type()
)
pdu2TemperatureName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu2TemperatureName.setStatus("mandatory")


class _Pdu2TemperatureProbeStatus_Type(Integer32):
    """Custom type pdu2TemperatureProbeStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disconnected", 1),
          ("connected", 2),
          ("bad", 3))
    )


_Pdu2TemperatureProbeStatus_Type.__name__ = "Integer32"
_Pdu2TemperatureProbeStatus_Object = MibTableColumn
pdu2TemperatureProbeStatus = _Pdu2TemperatureProbeStatus_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 7, 4, 2, 1, 3),
    _Pdu2TemperatureProbeStatus_Type()
)
pdu2TemperatureProbeStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu2TemperatureProbeStatus.setStatus("mandatory")
_Pdu2TemperatureValue_Type = Integer32
_Pdu2TemperatureValue_Object = MibTableColumn
pdu2TemperatureValue = _Pdu2TemperatureValue_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 7, 4, 2, 1, 4),
    _Pdu2TemperatureValue_Type()
)
pdu2TemperatureValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu2TemperatureValue.setStatus("mandatory")


class _Pdu2TemperatureThStatus_Type(Integer32):
    """Custom type pdu2TemperatureThStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("good", 1),
          ("lowWarning", 2),
          ("lowCritical", 3),
          ("highWarning", 4),
          ("highCritical", 5))
    )


_Pdu2TemperatureThStatus_Type.__name__ = "Integer32"
_Pdu2TemperatureThStatus_Object = MibTableColumn
pdu2TemperatureThStatus = _Pdu2TemperatureThStatus_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 7, 4, 2, 1, 5),
    _Pdu2TemperatureThStatus_Type()
)
pdu2TemperatureThStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu2TemperatureThStatus.setStatus("mandatory")


class _Pdu2TemperatureThLowerWarning_Type(Integer32):
    """Custom type pdu2TemperatureThLowerWarning based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 150000),
    )


_Pdu2TemperatureThLowerWarning_Type.__name__ = "Integer32"
_Pdu2TemperatureThLowerWarning_Object = MibTableColumn
pdu2TemperatureThLowerWarning = _Pdu2TemperatureThLowerWarning_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 7, 4, 2, 1, 6),
    _Pdu2TemperatureThLowerWarning_Type()
)
pdu2TemperatureThLowerWarning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu2TemperatureThLowerWarning.setStatus("mandatory")


class _Pdu2TemperatureThLowerCritical_Type(Integer32):
    """Custom type pdu2TemperatureThLowerCritical based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 150000),
    )


_Pdu2TemperatureThLowerCritical_Type.__name__ = "Integer32"
_Pdu2TemperatureThLowerCritical_Object = MibTableColumn
pdu2TemperatureThLowerCritical = _Pdu2TemperatureThLowerCritical_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 7, 4, 2, 1, 7),
    _Pdu2TemperatureThLowerCritical_Type()
)
pdu2TemperatureThLowerCritical.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu2TemperatureThLowerCritical.setStatus("mandatory")


class _Pdu2TemperatureThUpperWarning_Type(Integer32):
    """Custom type pdu2TemperatureThUpperWarning based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 150000),
    )


_Pdu2TemperatureThUpperWarning_Type.__name__ = "Integer32"
_Pdu2TemperatureThUpperWarning_Object = MibTableColumn
pdu2TemperatureThUpperWarning = _Pdu2TemperatureThUpperWarning_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 7, 4, 2, 1, 8),
    _Pdu2TemperatureThUpperWarning_Type()
)
pdu2TemperatureThUpperWarning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu2TemperatureThUpperWarning.setStatus("mandatory")


class _Pdu2TemperatureThUpperCritical_Type(Integer32):
    """Custom type pdu2TemperatureThUpperCritical based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 150000),
    )


_Pdu2TemperatureThUpperCritical_Type.__name__ = "Integer32"
_Pdu2TemperatureThUpperCritical_Object = MibTableColumn
pdu2TemperatureThUpperCritical = _Pdu2TemperatureThUpperCritical_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 7, 4, 2, 1, 9),
    _Pdu2TemperatureThUpperCritical_Type()
)
pdu2TemperatureThUpperCritical.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu2TemperatureThUpperCritical.setStatus("mandatory")
_Pdu2HumidityTable_Object = MibTable
pdu2HumidityTable = _Pdu2HumidityTable_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 7, 4, 3)
)
if mibBuilder.loadTexts:
    pdu2HumidityTable.setStatus("mandatory")
_Pdu2HumidityEntry_Object = MibTableRow
pdu2HumidityEntry = _Pdu2HumidityEntry_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 7, 4, 3, 1)
)
pdu2HumidityEntry.setIndexNames(
    (0, "CPQPOWER-MIB", "pdu2IdentIndex"),
    (0, "CPQPOWER-MIB", "pdu2HumidityIndex"),
)
if mibBuilder.loadTexts:
    pdu2HumidityEntry.setStatus("mandatory")


class _Pdu2HumidityIndex_Type(Integer32):
    """Custom type pdu2HumidityIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_Pdu2HumidityIndex_Type.__name__ = "Integer32"
_Pdu2HumidityIndex_Object = MibTableColumn
pdu2HumidityIndex = _Pdu2HumidityIndex_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 7, 4, 3, 1, 1),
    _Pdu2HumidityIndex_Type()
)
pdu2HumidityIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu2HumidityIndex.setStatus("mandatory")


class _Pdu2HumidityName_Type(DisplayString):
    """Custom type pdu2HumidityName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_Pdu2HumidityName_Type.__name__ = "DisplayString"
_Pdu2HumidityName_Object = MibTableColumn
pdu2HumidityName = _Pdu2HumidityName_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 7, 4, 3, 1, 2),
    _Pdu2HumidityName_Type()
)
pdu2HumidityName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu2HumidityName.setStatus("mandatory")


class _Pdu2HumidityProbeStatus_Type(Integer32):
    """Custom type pdu2HumidityProbeStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disconnected", 1),
          ("connected", 2),
          ("bad", 3))
    )


_Pdu2HumidityProbeStatus_Type.__name__ = "Integer32"
_Pdu2HumidityProbeStatus_Object = MibTableColumn
pdu2HumidityProbeStatus = _Pdu2HumidityProbeStatus_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 7, 4, 3, 1, 3),
    _Pdu2HumidityProbeStatus_Type()
)
pdu2HumidityProbeStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu2HumidityProbeStatus.setStatus("mandatory")
_Pdu2HumidityValue_Type = Integer32
_Pdu2HumidityValue_Object = MibTableColumn
pdu2HumidityValue = _Pdu2HumidityValue_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 7, 4, 3, 1, 4),
    _Pdu2HumidityValue_Type()
)
pdu2HumidityValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu2HumidityValue.setStatus("mandatory")


class _Pdu2HumidityThStatus_Type(Integer32):
    """Custom type pdu2HumidityThStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("good", 1),
          ("lowWarning", 2),
          ("lowCritical", 3),
          ("highWarning", 4),
          ("highCritical", 5))
    )


_Pdu2HumidityThStatus_Type.__name__ = "Integer32"
_Pdu2HumidityThStatus_Object = MibTableColumn
pdu2HumidityThStatus = _Pdu2HumidityThStatus_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 7, 4, 3, 1, 5),
    _Pdu2HumidityThStatus_Type()
)
pdu2HumidityThStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu2HumidityThStatus.setStatus("mandatory")


class _Pdu2HumidityThLowerWarning_Type(Integer32):
    """Custom type pdu2HumidityThLowerWarning based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 1000),
    )


_Pdu2HumidityThLowerWarning_Type.__name__ = "Integer32"
_Pdu2HumidityThLowerWarning_Object = MibTableColumn
pdu2HumidityThLowerWarning = _Pdu2HumidityThLowerWarning_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 7, 4, 3, 1, 6),
    _Pdu2HumidityThLowerWarning_Type()
)
pdu2HumidityThLowerWarning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu2HumidityThLowerWarning.setStatus("mandatory")


class _Pdu2HumidityThLowerCritical_Type(Integer32):
    """Custom type pdu2HumidityThLowerCritical based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 1000),
    )


_Pdu2HumidityThLowerCritical_Type.__name__ = "Integer32"
_Pdu2HumidityThLowerCritical_Object = MibTableColumn
pdu2HumidityThLowerCritical = _Pdu2HumidityThLowerCritical_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 7, 4, 3, 1, 7),
    _Pdu2HumidityThLowerCritical_Type()
)
pdu2HumidityThLowerCritical.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu2HumidityThLowerCritical.setStatus("mandatory")


class _Pdu2HumidityThUpperWarning_Type(Integer32):
    """Custom type pdu2HumidityThUpperWarning based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 1000),
    )


_Pdu2HumidityThUpperWarning_Type.__name__ = "Integer32"
_Pdu2HumidityThUpperWarning_Object = MibTableColumn
pdu2HumidityThUpperWarning = _Pdu2HumidityThUpperWarning_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 7, 4, 3, 1, 8),
    _Pdu2HumidityThUpperWarning_Type()
)
pdu2HumidityThUpperWarning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu2HumidityThUpperWarning.setStatus("mandatory")


class _Pdu2HumidityThUpperCritical_Type(Integer32):
    """Custom type pdu2HumidityThUpperCritical based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 1000),
    )


_Pdu2HumidityThUpperCritical_Type.__name__ = "Integer32"
_Pdu2HumidityThUpperCritical_Object = MibTableColumn
pdu2HumidityThUpperCritical = _Pdu2HumidityThUpperCritical_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 7, 4, 3, 1, 9),
    _Pdu2HumidityThUpperCritical_Type()
)
pdu2HumidityThUpperCritical.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu2HumidityThUpperCritical.setStatus("mandatory")
_Pdu2ContactTable_Object = MibTable
pdu2ContactTable = _Pdu2ContactTable_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 7, 4, 4)
)
if mibBuilder.loadTexts:
    pdu2ContactTable.setStatus("mandatory")
_Pdu2ContactEntry_Object = MibTableRow
pdu2ContactEntry = _Pdu2ContactEntry_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 7, 4, 4, 1)
)
pdu2ContactEntry.setIndexNames(
    (0, "CPQPOWER-MIB", "pdu2IdentIndex"),
    (0, "CPQPOWER-MIB", "pdu2ContactIndex"),
)
if mibBuilder.loadTexts:
    pdu2ContactEntry.setStatus("mandatory")


class _Pdu2ContactIndex_Type(Integer32):
    """Custom type pdu2ContactIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_Pdu2ContactIndex_Type.__name__ = "Integer32"
_Pdu2ContactIndex_Object = MibTableColumn
pdu2ContactIndex = _Pdu2ContactIndex_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 7, 4, 4, 1, 1),
    _Pdu2ContactIndex_Type()
)
pdu2ContactIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu2ContactIndex.setStatus("mandatory")


class _Pdu2ContactName_Type(DisplayString):
    """Custom type pdu2ContactName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_Pdu2ContactName_Type.__name__ = "DisplayString"
_Pdu2ContactName_Object = MibTableColumn
pdu2ContactName = _Pdu2ContactName_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 7, 4, 4, 1, 2),
    _Pdu2ContactName_Type()
)
pdu2ContactName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu2ContactName.setStatus("mandatory")


class _Pdu2ContactProbeStatus_Type(Integer32):
    """Custom type pdu2ContactProbeStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disconnected", 1),
          ("connected", 2),
          ("bad", 3))
    )


_Pdu2ContactProbeStatus_Type.__name__ = "Integer32"
_Pdu2ContactProbeStatus_Object = MibTableColumn
pdu2ContactProbeStatus = _Pdu2ContactProbeStatus_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 7, 4, 4, 1, 3),
    _Pdu2ContactProbeStatus_Type()
)
pdu2ContactProbeStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu2ContactProbeStatus.setStatus("mandatory")


class _Pdu2ContactState_Type(Integer32):
    """Custom type pdu2ContactState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("contactOpen", 1),
          ("contactClosed", 2),
          ("contactBad", 3))
    )


_Pdu2ContactState_Type.__name__ = "Integer32"
_Pdu2ContactState_Object = MibTableColumn
pdu2ContactState = _Pdu2ContactState_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 7, 4, 4, 1, 4),
    _Pdu2ContactState_Type()
)
pdu2ContactState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu2ContactState.setStatus("mandatory")
_Pdu2Outlet_ObjectIdentity = ObjectIdentity
pdu2Outlet = _Pdu2Outlet_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 165, 7, 5)
)
_Pdu2OutletTable_Object = MibTable
pdu2OutletTable = _Pdu2OutletTable_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 7, 5, 1)
)
if mibBuilder.loadTexts:
    pdu2OutletTable.setStatus("mandatory")
_Pdu2OutletEntry_Object = MibTableRow
pdu2OutletEntry = _Pdu2OutletEntry_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 7, 5, 1, 1)
)
pdu2OutletEntry.setIndexNames(
    (0, "CPQPOWER-MIB", "pdu2IdentIndex"),
    (0, "CPQPOWER-MIB", "pdu2OutletIndex"),
)
if mibBuilder.loadTexts:
    pdu2OutletEntry.setStatus("mandatory")


class _Pdu2OutletIndex_Type(Integer32):
    """Custom type pdu2OutletIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Pdu2OutletIndex_Type.__name__ = "Integer32"
_Pdu2OutletIndex_Object = MibTableColumn
pdu2OutletIndex = _Pdu2OutletIndex_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 7, 5, 1, 1, 1),
    _Pdu2OutletIndex_Type()
)
pdu2OutletIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu2OutletIndex.setStatus("mandatory")


class _Pdu2OutletName_Type(DisplayString):
    """Custom type pdu2OutletName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_Pdu2OutletName_Type.__name__ = "DisplayString"
_Pdu2OutletName_Object = MibTableColumn
pdu2OutletName = _Pdu2OutletName_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 7, 5, 1, 1, 2),
    _Pdu2OutletName_Type()
)
pdu2OutletName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu2OutletName.setStatus("mandatory")


class _Pdu2OutletType_Type(Integer32):
    """Custom type pdu2OutletType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              10,
              11,
              12,
              20,
              21,
              22,
              23,
              24,
              25,
              26,
              27,
              28,
              29,
              30)
        )
    )
    namedValues = NamedValues(
        *(("iecC13", 1),
          ("iecC19", 2),
          ("uk", 10),
          ("french", 11),
          ("schuko", 12),
          ("nema515", 20),
          ("nema51520", 21),
          ("nema520", 22),
          ("nemaL520", 23),
          ("nemaL530", 24),
          ("nema615", 25),
          ("nema620", 26),
          ("nemaL620", 27),
          ("nemaL630", 28),
          ("nemaL715", 29),
          ("rf203p277", 30))
    )


_Pdu2OutletType_Type.__name__ = "Integer32"
_Pdu2OutletType_Object = MibTableColumn
pdu2OutletType = _Pdu2OutletType_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 7, 5, 1, 1, 3),
    _Pdu2OutletType_Type()
)
pdu2OutletType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu2OutletType.setStatus("mandatory")
_Pdu2OutletCurrentRating_Type = Integer32
_Pdu2OutletCurrentRating_Object = MibTableColumn
pdu2OutletCurrentRating = _Pdu2OutletCurrentRating_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 7, 5, 1, 1, 4),
    _Pdu2OutletCurrentRating_Type()
)
pdu2OutletCurrentRating.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu2OutletCurrentRating.setStatus("mandatory")
_Pdu2OutletCurrent_Type = Integer32
_Pdu2OutletCurrent_Object = MibTableColumn
pdu2OutletCurrent = _Pdu2OutletCurrent_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 7, 5, 1, 1, 5),
    _Pdu2OutletCurrent_Type()
)
pdu2OutletCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu2OutletCurrent.setStatus("mandatory")


class _Pdu2OutletCurrentThStatus_Type(Integer32):
    """Custom type pdu2OutletCurrentThStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("good", 1),
          ("lowWarning", 2),
          ("lowCritical", 3),
          ("highWarning", 4),
          ("highCritical", 5))
    )


_Pdu2OutletCurrentThStatus_Type.__name__ = "Integer32"
_Pdu2OutletCurrentThStatus_Object = MibTableColumn
pdu2OutletCurrentThStatus = _Pdu2OutletCurrentThStatus_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 7, 5, 1, 1, 6),
    _Pdu2OutletCurrentThStatus_Type()
)
pdu2OutletCurrentThStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu2OutletCurrentThStatus.setStatus("mandatory")


class _Pdu2OutletCurrentThLowerWarning_Type(Integer32):
    """Custom type pdu2OutletCurrentThLowerWarning based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 100000),
    )


_Pdu2OutletCurrentThLowerWarning_Type.__name__ = "Integer32"
_Pdu2OutletCurrentThLowerWarning_Object = MibTableColumn
pdu2OutletCurrentThLowerWarning = _Pdu2OutletCurrentThLowerWarning_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 7, 5, 1, 1, 7),
    _Pdu2OutletCurrentThLowerWarning_Type()
)
pdu2OutletCurrentThLowerWarning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu2OutletCurrentThLowerWarning.setStatus("mandatory")


class _Pdu2OutletCurrentThLowerCritical_Type(Integer32):
    """Custom type pdu2OutletCurrentThLowerCritical based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 100000),
    )


_Pdu2OutletCurrentThLowerCritical_Type.__name__ = "Integer32"
_Pdu2OutletCurrentThLowerCritical_Object = MibTableColumn
pdu2OutletCurrentThLowerCritical = _Pdu2OutletCurrentThLowerCritical_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 7, 5, 1, 1, 8),
    _Pdu2OutletCurrentThLowerCritical_Type()
)
pdu2OutletCurrentThLowerCritical.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu2OutletCurrentThLowerCritical.setStatus("mandatory")


class _Pdu2OutletCurrentThUpperWarning_Type(Integer32):
    """Custom type pdu2OutletCurrentThUpperWarning based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 100000),
    )


_Pdu2OutletCurrentThUpperWarning_Type.__name__ = "Integer32"
_Pdu2OutletCurrentThUpperWarning_Object = MibTableColumn
pdu2OutletCurrentThUpperWarning = _Pdu2OutletCurrentThUpperWarning_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 7, 5, 1, 1, 9),
    _Pdu2OutletCurrentThUpperWarning_Type()
)
pdu2OutletCurrentThUpperWarning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu2OutletCurrentThUpperWarning.setStatus("mandatory")


class _Pdu2OutletCurrentThUpperCritical_Type(Integer32):
    """Custom type pdu2OutletCurrentThUpperCritical based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 100000),
    )


_Pdu2OutletCurrentThUpperCritical_Type.__name__ = "Integer32"
_Pdu2OutletCurrentThUpperCritical_Object = MibTableColumn
pdu2OutletCurrentThUpperCritical = _Pdu2OutletCurrentThUpperCritical_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 7, 5, 1, 1, 10),
    _Pdu2OutletCurrentThUpperCritical_Type()
)
pdu2OutletCurrentThUpperCritical.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu2OutletCurrentThUpperCritical.setStatus("mandatory")
_Pdu2OutletCurrentCrestFactor_Type = Integer32
_Pdu2OutletCurrentCrestFactor_Object = MibTableColumn
pdu2OutletCurrentCrestFactor = _Pdu2OutletCurrentCrestFactor_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 7, 5, 1, 1, 11),
    _Pdu2OutletCurrentCrestFactor_Type()
)
pdu2OutletCurrentCrestFactor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu2OutletCurrentCrestFactor.setStatus("mandatory")
_Pdu2OutletCurrentPercentLoad_Type = Integer32
_Pdu2OutletCurrentPercentLoad_Object = MibTableColumn
pdu2OutletCurrentPercentLoad = _Pdu2OutletCurrentPercentLoad_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 7, 5, 1, 1, 12),
    _Pdu2OutletCurrentPercentLoad_Type()
)
pdu2OutletCurrentPercentLoad.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu2OutletCurrentPercentLoad.setStatus("mandatory")
_Pdu2OutletVA_Type = Integer32
_Pdu2OutletVA_Object = MibTableColumn
pdu2OutletVA = _Pdu2OutletVA_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 7, 5, 1, 1, 13),
    _Pdu2OutletVA_Type()
)
pdu2OutletVA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu2OutletVA.setStatus("mandatory")
_Pdu2OutletWatts_Type = Integer32
_Pdu2OutletWatts_Object = MibTableColumn
pdu2OutletWatts = _Pdu2OutletWatts_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 7, 5, 1, 1, 14),
    _Pdu2OutletWatts_Type()
)
pdu2OutletWatts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu2OutletWatts.setStatus("mandatory")
_Pdu2OutletWh_Type = Integer32
_Pdu2OutletWh_Object = MibTableColumn
pdu2OutletWh = _Pdu2OutletWh_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 7, 5, 1, 1, 15),
    _Pdu2OutletWh_Type()
)
pdu2OutletWh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu2OutletWh.setStatus("mandatory")


class _Pdu2OutletWhTimer_Type(DisplayString):
    """Custom type pdu2OutletWhTimer based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 22),
    )


_Pdu2OutletWhTimer_Type.__name__ = "DisplayString"
_Pdu2OutletWhTimer_Object = MibTableColumn
pdu2OutletWhTimer = _Pdu2OutletWhTimer_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 7, 5, 1, 1, 16),
    _Pdu2OutletWhTimer_Type()
)
pdu2OutletWhTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu2OutletWhTimer.setStatus("mandatory")
_Pdu2OutletPowerFactor_Type = Integer32
_Pdu2OutletPowerFactor_Object = MibTableColumn
pdu2OutletPowerFactor = _Pdu2OutletPowerFactor_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 7, 5, 1, 1, 17),
    _Pdu2OutletPowerFactor_Type()
)
pdu2OutletPowerFactor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu2OutletPowerFactor.setStatus("mandatory")
_Pdu2OutletVAR_Type = Integer32
_Pdu2OutletVAR_Object = MibTableColumn
pdu2OutletVAR = _Pdu2OutletVAR_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 7, 5, 1, 1, 18),
    _Pdu2OutletVAR_Type()
)
pdu2OutletVAR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu2OutletVAR.setStatus("mandatory")
_Pdu2OutletControlTable_Object = MibTable
pdu2OutletControlTable = _Pdu2OutletControlTable_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 7, 5, 2)
)
if mibBuilder.loadTexts:
    pdu2OutletControlTable.setStatus("mandatory")
_Pdu2OutletControlEntry_Object = MibTableRow
pdu2OutletControlEntry = _Pdu2OutletControlEntry_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 7, 5, 2, 1)
)
pdu2OutletControlEntry.setIndexNames(
    (0, "CPQPOWER-MIB", "pdu2IdentIndex"),
    (0, "CPQPOWER-MIB", "pdu2OutletIndex"),
)
if mibBuilder.loadTexts:
    pdu2OutletControlEntry.setStatus("mandatory")


class _Pdu2OutletControlStatus_Type(Integer32):
    """Custom type pdu2OutletControlStatus based on Integer32"""
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
        *(("off", 1),
          ("on", 2),
          ("pendingOff", 3),
          ("pendingOn", 4))
    )


_Pdu2OutletControlStatus_Type.__name__ = "Integer32"
_Pdu2OutletControlStatus_Object = MibTableColumn
pdu2OutletControlStatus = _Pdu2OutletControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 7, 5, 2, 1, 1),
    _Pdu2OutletControlStatus_Type()
)
pdu2OutletControlStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu2OutletControlStatus.setStatus("mandatory")


class _Pdu2OutletControlOffCmd_Type(Integer32):
    """Custom type pdu2OutletControlOffCmd based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 99999),
    )


_Pdu2OutletControlOffCmd_Type.__name__ = "Integer32"
_Pdu2OutletControlOffCmd_Object = MibTableColumn
pdu2OutletControlOffCmd = _Pdu2OutletControlOffCmd_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 7, 5, 2, 1, 2),
    _Pdu2OutletControlOffCmd_Type()
)
pdu2OutletControlOffCmd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pdu2OutletControlOffCmd.setStatus("mandatory")


class _Pdu2OutletControlOnCmd_Type(Integer32):
    """Custom type pdu2OutletControlOnCmd based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 99999),
    )


_Pdu2OutletControlOnCmd_Type.__name__ = "Integer32"
_Pdu2OutletControlOnCmd_Object = MibTableColumn
pdu2OutletControlOnCmd = _Pdu2OutletControlOnCmd_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 7, 5, 2, 1, 3),
    _Pdu2OutletControlOnCmd_Type()
)
pdu2OutletControlOnCmd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pdu2OutletControlOnCmd.setStatus("mandatory")


class _Pdu2OutletControlRebootCmd_Type(Integer32):
    """Custom type pdu2OutletControlRebootCmd based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 99999),
    )


_Pdu2OutletControlRebootCmd_Type.__name__ = "Integer32"
_Pdu2OutletControlRebootCmd_Object = MibTableColumn
pdu2OutletControlRebootCmd = _Pdu2OutletControlRebootCmd_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 7, 5, 2, 1, 4),
    _Pdu2OutletControlRebootCmd_Type()
)
pdu2OutletControlRebootCmd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pdu2OutletControlRebootCmd.setStatus("mandatory")


class _Pdu2OutletControlPowerOnState_Type(Integer32):
    """Custom type pdu2OutletControlPowerOnState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2),
          ("lastState", 3))
    )


_Pdu2OutletControlPowerOnState_Type.__name__ = "Integer32"
_Pdu2OutletControlPowerOnState_Object = MibTableColumn
pdu2OutletControlPowerOnState = _Pdu2OutletControlPowerOnState_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 7, 5, 2, 1, 5),
    _Pdu2OutletControlPowerOnState_Type()
)
pdu2OutletControlPowerOnState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pdu2OutletControlPowerOnState.setStatus("mandatory")


class _Pdu2OutletControlSequenceDelay_Type(Integer32):
    """Custom type pdu2OutletControlSequenceDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 99999),
    )


_Pdu2OutletControlSequenceDelay_Type.__name__ = "Integer32"
_Pdu2OutletControlSequenceDelay_Object = MibTableColumn
pdu2OutletControlSequenceDelay = _Pdu2OutletControlSequenceDelay_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 7, 5, 2, 1, 6),
    _Pdu2OutletControlSequenceDelay_Type()
)
pdu2OutletControlSequenceDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pdu2OutletControlSequenceDelay.setStatus("mandatory")


class _Pdu2OutletControlRebootOffTime_Type(Integer32):
    """Custom type pdu2OutletControlRebootOffTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 99999),
    )


_Pdu2OutletControlRebootOffTime_Type.__name__ = "Integer32"
_Pdu2OutletControlRebootOffTime_Object = MibTableColumn
pdu2OutletControlRebootOffTime = _Pdu2OutletControlRebootOffTime_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 7, 5, 2, 1, 7),
    _Pdu2OutletControlRebootOffTime_Type()
)
pdu2OutletControlRebootOffTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pdu2OutletControlRebootOffTime.setStatus("mandatory")


class _Pdu2OutletControlSwitchable_Type(Integer32):
    """Custom type pdu2OutletControlSwitchable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("switchable", 1),
          ("notSwitchable", 2))
    )


_Pdu2OutletControlSwitchable_Type.__name__ = "Integer32"
_Pdu2OutletControlSwitchable_Object = MibTableColumn
pdu2OutletControlSwitchable = _Pdu2OutletControlSwitchable_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 7, 5, 2, 1, 8),
    _Pdu2OutletControlSwitchable_Type()
)
pdu2OutletControlSwitchable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pdu2OutletControlSwitchable.setStatus("mandatory")


class _Pdu2OutletControlShutoffDelay_Type(Integer32):
    """Custom type pdu2OutletControlShutoffDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 99999),
    )


_Pdu2OutletControlShutoffDelay_Type.__name__ = "Integer32"
_Pdu2OutletControlShutoffDelay_Object = MibTableColumn
pdu2OutletControlShutoffDelay = _Pdu2OutletControlShutoffDelay_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 7, 5, 2, 1, 9),
    _Pdu2OutletControlShutoffDelay_Type()
)
pdu2OutletControlShutoffDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pdu2OutletControlShutoffDelay.setStatus("mandatory")
_Hpdu_ObjectIdentity = ObjectIdentity
hpdu = _Hpdu_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 165, 9)
)
_HpduIdent_ObjectIdentity = ObjectIdentity
hpduIdent = _HpduIdent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 165, 9, 1)
)


class _HpduNumPhase_Type(Integer32):
    """Custom type hpduNumPhase based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_HpduNumPhase_Type.__name__ = "Integer32"
_HpduNumPhase_Object = MibScalar
hpduNumPhase = _HpduNumPhase_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 9, 1, 1),
    _HpduNumPhase_Type()
)
hpduNumPhase.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpduNumPhase.setStatus("mandatory")
_HpduIdentTable_Object = MibTable
hpduIdentTable = _HpduIdentTable_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 9, 1, 2)
)
if mibBuilder.loadTexts:
    hpduIdentTable.setStatus("mandatory")
_HpduIdentEntry_Object = MibTableRow
hpduIdentEntry = _HpduIdentEntry_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 9, 1, 2, 1)
)
hpduIdentEntry.setIndexNames(
    (0, "CPQPOWER-MIB", "hpduIdentIndex"),
)
if mibBuilder.loadTexts:
    hpduIdentEntry.setStatus("mandatory")


class _HpduIdentIndex_Type(Integer32):
    """Custom type hpduIdentIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_HpduIdentIndex_Type.__name__ = "Integer32"
_HpduIdentIndex_Object = MibTableColumn
hpduIdentIndex = _HpduIdentIndex_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 9, 1, 2, 1, 1),
    _HpduIdentIndex_Type()
)
hpduIdentIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpduIdentIndex.setStatus("mandatory")
_HpduManufacturer_Type = DisplayString
_HpduManufacturer_Object = MibTableColumn
hpduManufacturer = _HpduManufacturer_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 9, 1, 2, 1, 2),
    _HpduManufacturer_Type()
)
hpduManufacturer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpduManufacturer.setStatus("mandatory")
_HpduModel_Type = DisplayString
_HpduModel_Object = MibTableColumn
hpduModel = _HpduModel_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 9, 1, 2, 1, 3),
    _HpduModel_Type()
)
hpduModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpduModel.setStatus("mandatory")
_HpduName_Type = DisplayString
_HpduName_Object = MibTableColumn
hpduName = _HpduName_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 9, 1, 2, 1, 4),
    _HpduName_Type()
)
hpduName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpduName.setStatus("mandatory")
_HpduFirmwareVersion_Type = DisplayString
_HpduFirmwareVersion_Object = MibTableColumn
hpduFirmwareVersion = _HpduFirmwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 9, 1, 2, 1, 5),
    _HpduFirmwareVersion_Type()
)
hpduFirmwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpduFirmwareVersion.setStatus("mandatory")
_HpduHardwareVersion_Type = DisplayString
_HpduHardwareVersion_Object = MibTableColumn
hpduHardwareVersion = _HpduHardwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 9, 1, 2, 1, 6),
    _HpduHardwareVersion_Type()
)
hpduHardwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpduHardwareVersion.setStatus("mandatory")
_HpduPartNumber_Type = DisplayString
_HpduPartNumber_Object = MibTableColumn
hpduPartNumber = _HpduPartNumber_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 9, 1, 2, 1, 7),
    _HpduPartNumber_Type()
)
hpduPartNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpduPartNumber.setStatus("mandatory")
_HpduSerialNumber_Type = DisplayString
_HpduSerialNumber_Object = MibTableColumn
hpduSerialNumber = _HpduSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 9, 1, 2, 1, 8),
    _HpduSerialNumber_Type()
)
hpduSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpduSerialNumber.setStatus("mandatory")
_HpduUUID_Type = DisplayString
_HpduUUID_Object = MibTableColumn
hpduUUID = _HpduUUID_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 9, 1, 2, 1, 9),
    _HpduUUID_Type()
)
hpduUUID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpduUUID.setStatus("mandatory")
_HpduType_Type = DisplayString
_HpduType_Object = MibTableColumn
hpduType = _HpduType_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 9, 1, 2, 1, 10),
    _HpduType_Type()
)
hpduType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpduType.setStatus("mandatory")
_HpduPowerRating_Type = DisplayString
_HpduPowerRating_Object = MibTableColumn
hpduPowerRating = _HpduPowerRating_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 9, 1, 2, 1, 11),
    _HpduPowerRating_Type()
)
hpduPowerRating.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpduPowerRating.setStatus("mandatory")
_HpduInputRating_Type = DisplayString
_HpduInputRating_Object = MibTableColumn
hpduInputRating = _HpduInputRating_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 9, 1, 2, 1, 12),
    _HpduInputRating_Type()
)
hpduInputRating.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpduInputRating.setStatus("mandatory")
_HpduRegionalNominalVoltage_Type = DisplayString
_HpduRegionalNominalVoltage_Object = MibTableColumn
hpduRegionalNominalVoltage = _HpduRegionalNominalVoltage_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 9, 1, 2, 1, 13),
    _HpduRegionalNominalVoltage_Type()
)
hpduRegionalNominalVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpduRegionalNominalVoltage.setStatus("mandatory")


class _HpduNumOutputBreakers_Type(Integer32):
    """Custom type hpduNumOutputBreakers based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10),
    )


_HpduNumOutputBreakers_Type.__name__ = "Integer32"
_HpduNumOutputBreakers_Object = MibTableColumn
hpduNumOutputBreakers = _HpduNumOutputBreakers_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 9, 1, 2, 1, 14),
    _HpduNumOutputBreakers_Type()
)
hpduNumOutputBreakers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpduNumOutputBreakers.setStatus("mandatory")


class _HpduNumMonitoredOutlet_Type(Integer32):
    """Custom type hpduNumMonitoredOutlet based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10),
    )


_HpduNumMonitoredOutlet_Type.__name__ = "Integer32"
_HpduNumMonitoredOutlet_Object = MibTableColumn
hpduNumMonitoredOutlet = _HpduNumMonitoredOutlet_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 9, 1, 2, 1, 15),
    _HpduNumMonitoredOutlet_Type()
)
hpduNumMonitoredOutlet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpduNumMonitoredOutlet.setStatus("mandatory")
_HpduFanStatus_Type = DisplayString
_HpduFanStatus_Object = MibTableColumn
hpduFanStatus = _HpduFanStatus_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 9, 1, 2, 1, 16),
    _HpduFanStatus_Type()
)
hpduFanStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpduFanStatus.setStatus("mandatory")
_HpduTemperature_Type = Integer32
_HpduTemperature_Object = MibTableColumn
hpduTemperature = _HpduTemperature_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 9, 1, 2, 1, 17),
    _HpduTemperature_Type()
)
hpduTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpduTemperature.setStatus("mandatory")
_HpduInput_ObjectIdentity = ObjectIdentity
hpduInput = _HpduInput_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 165, 9, 2)
)
_HpduInputTable_Object = MibTable
hpduInputTable = _HpduInputTable_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 9, 2, 1)
)
if mibBuilder.loadTexts:
    hpduInputTable.setStatus("mandatory")
_HpduInputEntry_Object = MibTableRow
hpduInputEntry = _HpduInputEntry_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 9, 2, 1, 1)
)
hpduInputEntry.setIndexNames(
    (0, "CPQPOWER-MIB", "hpduInputIndex"),
)
if mibBuilder.loadTexts:
    hpduInputEntry.setStatus("mandatory")


class _HpduInputIndex_Type(Integer32):
    """Custom type hpduInputIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_HpduInputIndex_Type.__name__ = "Integer32"
_HpduInputIndex_Object = MibTableColumn
hpduInputIndex = _HpduInputIndex_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 9, 2, 1, 1, 1),
    _HpduInputIndex_Type()
)
hpduInputIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpduInputIndex.setStatus("mandatory")
_HpduInputStatus_Type = DisplayString
_HpduInputStatus_Object = MibTableColumn
hpduInputStatus = _HpduInputStatus_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 9, 2, 1, 1, 2),
    _HpduInputStatus_Type()
)
hpduInputStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpduInputStatus.setStatus("mandatory")
_HpduInputBreakerRating_Type = Integer32
_HpduInputBreakerRating_Object = MibTableColumn
hpduInputBreakerRating = _HpduInputBreakerRating_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 9, 2, 1, 1, 3),
    _HpduInputBreakerRating_Type()
)
hpduInputBreakerRating.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpduInputBreakerRating.setStatus("mandatory")
_HpduInputVoltage_Type = Integer32
_HpduInputVoltage_Object = MibTableColumn
hpduInputVoltage = _HpduInputVoltage_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 9, 2, 1, 1, 4),
    _HpduInputVoltage_Type()
)
hpduInputVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpduInputVoltage.setStatus("mandatory")
_HpduInputCurrent_Type = Integer32
_HpduInputCurrent_Object = MibTableColumn
hpduInputCurrent = _HpduInputCurrent_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 9, 2, 1, 1, 5),
    _HpduInputCurrent_Type()
)
hpduInputCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpduInputCurrent.setStatus("mandatory")
_HpduInputPowerVA_Type = Integer32
_HpduInputPowerVA_Object = MibTableColumn
hpduInputPowerVA = _HpduInputPowerVA_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 9, 2, 1, 1, 6),
    _HpduInputPowerVA_Type()
)
hpduInputPowerVA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpduInputPowerVA.setStatus("mandatory")
_HpduInputPowerWatt_Type = Integer32
_HpduInputPowerWatt_Object = MibTableColumn
hpduInputPowerWatt = _HpduInputPowerWatt_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 9, 2, 1, 1, 7),
    _HpduInputPowerWatt_Type()
)
hpduInputPowerWatt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpduInputPowerWatt.setStatus("mandatory")
_HpduInputPowerFactor_Type = Integer32
_HpduInputPowerFactor_Object = MibTableColumn
hpduInputPowerFactor = _HpduInputPowerFactor_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 9, 2, 1, 1, 8),
    _HpduInputPowerFactor_Type()
)
hpduInputPowerFactor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpduInputPowerFactor.setStatus("mandatory")
_HpduInputWarningThreshold_Type = Integer32
_HpduInputWarningThreshold_Object = MibTableColumn
hpduInputWarningThreshold = _HpduInputWarningThreshold_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 9, 2, 1, 1, 9),
    _HpduInputWarningThreshold_Type()
)
hpduInputWarningThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpduInputWarningThreshold.setStatus("mandatory")
_HpduInputCriticalThreshold_Type = Integer32
_HpduInputCriticalThreshold_Object = MibTableColumn
hpduInputCriticalThreshold = _HpduInputCriticalThreshold_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 9, 2, 1, 1, 10),
    _HpduInputCriticalThreshold_Type()
)
hpduInputCriticalThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpduInputCriticalThreshold.setStatus("mandatory")
_HpduInputPowerWattHour_Type = Integer32
_HpduInputPowerWattHour_Object = MibTableColumn
hpduInputPowerWattHour = _HpduInputPowerWattHour_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 9, 2, 1, 1, 11),
    _HpduInputPowerWattHour_Type()
)
hpduInputPowerWattHour.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpduInputPowerWattHour.setStatus("mandatory")
_HpduInputTotalEnergySince_Type = DisplayString
_HpduInputTotalEnergySince_Object = MibTableColumn
hpduInputTotalEnergySince = _HpduInputTotalEnergySince_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 9, 2, 1, 1, 12),
    _HpduInputTotalEnergySince_Type()
)
hpduInputTotalEnergySince.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpduInputTotalEnergySince.setStatus("mandatory")
_HpduInputEnergyMeteringTotalHours_Type = Integer32
_HpduInputEnergyMeteringTotalHours_Object = MibTableColumn
hpduInputEnergyMeteringTotalHours = _HpduInputEnergyMeteringTotalHours_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 9, 2, 1, 1, 13),
    _HpduInputEnergyMeteringTotalHours_Type()
)
hpduInputEnergyMeteringTotalHours.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpduInputEnergyMeteringTotalHours.setStatus("mandatory")
_HpduOutlet_ObjectIdentity = ObjectIdentity
hpduOutlet = _HpduOutlet_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 165, 9, 3)
)
_HpduOutletTable_Object = MibTable
hpduOutletTable = _HpduOutletTable_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 9, 3, 1)
)
if mibBuilder.loadTexts:
    hpduOutletTable.setStatus("mandatory")
_HpduOutletEntry_Object = MibTableRow
hpduOutletEntry = _HpduOutletEntry_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 9, 3, 1, 1)
)
hpduOutletEntry.setIndexNames(
    (0, "CPQPOWER-MIB", "hpduNumMonitoredOutlet"),
    (0, "CPQPOWER-MIB", "hpduNumPhase"),
    (0, "CPQPOWER-MIB", "hpduOutletIndex"),
)
if mibBuilder.loadTexts:
    hpduOutletEntry.setStatus("mandatory")


class _HpduOutletIndex_Type(Integer32):
    """Custom type hpduOutletIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_HpduOutletIndex_Type.__name__ = "Integer32"
_HpduOutletIndex_Object = MibTableColumn
hpduOutletIndex = _HpduOutletIndex_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 9, 3, 1, 1, 1),
    _HpduOutletIndex_Type()
)
hpduOutletIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpduOutletIndex.setStatus("mandatory")
_HpduOutletStatus_Type = DisplayString
_HpduOutletStatus_Object = MibTableColumn
hpduOutletStatus = _HpduOutletStatus_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 9, 3, 1, 1, 2),
    _HpduOutletStatus_Type()
)
hpduOutletStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpduOutletStatus.setStatus("mandatory")
_HpduOutletBreakerRating_Type = Integer32
_HpduOutletBreakerRating_Object = MibTableColumn
hpduOutletBreakerRating = _HpduOutletBreakerRating_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 9, 3, 1, 1, 3),
    _HpduOutletBreakerRating_Type()
)
hpduOutletBreakerRating.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpduOutletBreakerRating.setStatus("mandatory")
_HpduOutletPercentLoad_Type = Integer32
_HpduOutletPercentLoad_Object = MibTableColumn
hpduOutletPercentLoad = _HpduOutletPercentLoad_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 9, 3, 1, 1, 4),
    _HpduOutletPercentLoad_Type()
)
hpduOutletPercentLoad.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpduOutletPercentLoad.setStatus("mandatory")
_HpduOutletVoltage_Type = Integer32
_HpduOutletVoltage_Object = MibTableColumn
hpduOutletVoltage = _HpduOutletVoltage_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 9, 3, 1, 1, 5),
    _HpduOutletVoltage_Type()
)
hpduOutletVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpduOutletVoltage.setStatus("mandatory")
_HpduOutletCurrent_Type = Integer32
_HpduOutletCurrent_Object = MibTableColumn
hpduOutletCurrent = _HpduOutletCurrent_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 9, 3, 1, 1, 6),
    _HpduOutletCurrent_Type()
)
hpduOutletCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpduOutletCurrent.setStatus("mandatory")
_HpduOutletPowerVA_Type = Integer32
_HpduOutletPowerVA_Object = MibTableColumn
hpduOutletPowerVA = _HpduOutletPowerVA_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 9, 3, 1, 1, 7),
    _HpduOutletPowerVA_Type()
)
hpduOutletPowerVA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpduOutletPowerVA.setStatus("mandatory")
_HpduOutletPowerWatt_Type = Integer32
_HpduOutletPowerWatt_Object = MibTableColumn
hpduOutletPowerWatt = _HpduOutletPowerWatt_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 9, 3, 1, 1, 8),
    _HpduOutletPowerWatt_Type()
)
hpduOutletPowerWatt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpduOutletPowerWatt.setStatus("mandatory")
_HpduOutletPowerFactor_Type = Integer32
_HpduOutletPowerFactor_Object = MibTableColumn
hpduOutletPowerFactor = _HpduOutletPowerFactor_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 9, 3, 1, 1, 9),
    _HpduOutletPowerFactor_Type()
)
hpduOutletPowerFactor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpduOutletPowerFactor.setStatus("mandatory")
_HpduOutletWarningThreshold_Type = Integer32
_HpduOutletWarningThreshold_Object = MibTableColumn
hpduOutletWarningThreshold = _HpduOutletWarningThreshold_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 9, 3, 1, 1, 10),
    _HpduOutletWarningThreshold_Type()
)
hpduOutletWarningThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpduOutletWarningThreshold.setStatus("mandatory")
_HpduOutletCriticalThreshold_Type = Integer32
_HpduOutletCriticalThreshold_Object = MibTableColumn
hpduOutletCriticalThreshold = _HpduOutletCriticalThreshold_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 9, 3, 1, 1, 11),
    _HpduOutletCriticalThreshold_Type()
)
hpduOutletCriticalThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpduOutletCriticalThreshold.setStatus("mandatory")
_HpduOutletPowerWattHour_Type = Integer32
_HpduOutletPowerWattHour_Object = MibTableColumn
hpduOutletPowerWattHour = _HpduOutletPowerWattHour_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 9, 3, 1, 1, 12),
    _HpduOutletPowerWattHour_Type()
)
hpduOutletPowerWattHour.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpduOutletPowerWattHour.setStatus("mandatory")
_HpduOutletTotalEnergySince_Type = DisplayString
_HpduOutletTotalEnergySince_Object = MibTableColumn
hpduOutletTotalEnergySince = _HpduOutletTotalEnergySince_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 9, 3, 1, 1, 13),
    _HpduOutletTotalEnergySince_Type()
)
hpduOutletTotalEnergySince.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpduOutletTotalEnergySince.setStatus("mandatory")
_HpduOutletEnergyMeteringTotalHours_Type = Integer32
_HpduOutletEnergyMeteringTotalHours_Object = MibTableColumn
hpduOutletEnergyMeteringTotalHours = _HpduOutletEnergyMeteringTotalHours_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 9, 3, 1, 1, 14),
    _HpduOutletEnergyMeteringTotalHours_Type()
)
hpduOutletEnergyMeteringTotalHours.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpduOutletEnergyMeteringTotalHours.setStatus("mandatory")
_Pdu3_ObjectIdentity = ObjectIdentity
pdu3 = _Pdu3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 165, 11)
)
_Pdu3Ident_ObjectIdentity = ObjectIdentity
pdu3Ident = _Pdu3Ident_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 165, 11, 1)
)


class _Pdu3NumberPDU_Type(Integer32):
    """Custom type pdu3NumberPDU based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_Pdu3NumberPDU_Type.__name__ = "Integer32"
_Pdu3NumberPDU_Object = MibScalar
pdu3NumberPDU = _Pdu3NumberPDU_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 11, 1, 1),
    _Pdu3NumberPDU_Type()
)
pdu3NumberPDU.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu3NumberPDU.setStatus("mandatory")
_Pdu3IdentTable_Object = MibTable
pdu3IdentTable = _Pdu3IdentTable_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 11, 1, 2)
)
if mibBuilder.loadTexts:
    pdu3IdentTable.setStatus("mandatory")
_Pdu3IdentEntry_Object = MibTableRow
pdu3IdentEntry = _Pdu3IdentEntry_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 11, 1, 2, 1)
)
pdu3IdentEntry.setIndexNames(
    (0, "CPQPOWER-MIB", "pdu3IdentIndex"),
)
if mibBuilder.loadTexts:
    pdu3IdentEntry.setStatus("mandatory")


class _Pdu3IdentIndex_Type(Integer32):
    """Custom type pdu3IdentIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Pdu3IdentIndex_Type.__name__ = "Integer32"
_Pdu3IdentIndex_Object = MibTableColumn
pdu3IdentIndex = _Pdu3IdentIndex_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 11, 1, 2, 1, 1),
    _Pdu3IdentIndex_Type()
)
pdu3IdentIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu3IdentIndex.setStatus("mandatory")


class _Pdu3Name_Type(DisplayString):
    """Custom type pdu3Name based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_Pdu3Name_Type.__name__ = "DisplayString"
_Pdu3Name_Object = MibTableColumn
pdu3Name = _Pdu3Name_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 11, 1, 2, 1, 2),
    _Pdu3Name_Type()
)
pdu3Name.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu3Name.setStatus("mandatory")


class _Pdu3Model_Type(DisplayString):
    """Custom type pdu3Model based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_Pdu3Model_Type.__name__ = "DisplayString"
_Pdu3Model_Object = MibTableColumn
pdu3Model = _Pdu3Model_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 11, 1, 2, 1, 3),
    _Pdu3Model_Type()
)
pdu3Model.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu3Model.setStatus("mandatory")


class _Pdu3Manufacturer_Type(DisplayString):
    """Custom type pdu3Manufacturer based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_Pdu3Manufacturer_Type.__name__ = "DisplayString"
_Pdu3Manufacturer_Object = MibTableColumn
pdu3Manufacturer = _Pdu3Manufacturer_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 11, 1, 2, 1, 4),
    _Pdu3Manufacturer_Type()
)
pdu3Manufacturer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu3Manufacturer.setStatus("mandatory")


class _Pdu3FirmwareVersion_Type(DisplayString):
    """Custom type pdu3FirmwareVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_Pdu3FirmwareVersion_Type.__name__ = "DisplayString"
_Pdu3FirmwareVersion_Object = MibTableColumn
pdu3FirmwareVersion = _Pdu3FirmwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 11, 1, 2, 1, 5),
    _Pdu3FirmwareVersion_Type()
)
pdu3FirmwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu3FirmwareVersion.setStatus("mandatory")
_Pdu3FirmwareVersionTimeStamp_Type = DisplayString
_Pdu3FirmwareVersionTimeStamp_Object = MibTableColumn
pdu3FirmwareVersionTimeStamp = _Pdu3FirmwareVersionTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 11, 1, 2, 1, 6),
    _Pdu3FirmwareVersionTimeStamp_Type()
)
pdu3FirmwareVersionTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu3FirmwareVersionTimeStamp.setStatus("mandatory")


class _Pdu3PartNumber_Type(DisplayString):
    """Custom type pdu3PartNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_Pdu3PartNumber_Type.__name__ = "DisplayString"
_Pdu3PartNumber_Object = MibTableColumn
pdu3PartNumber = _Pdu3PartNumber_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 11, 1, 2, 1, 7),
    _Pdu3PartNumber_Type()
)
pdu3PartNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu3PartNumber.setStatus("mandatory")


class _Pdu3SerialNumber_Type(DisplayString):
    """Custom type pdu3SerialNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_Pdu3SerialNumber_Type.__name__ = "DisplayString"
_Pdu3SerialNumber_Object = MibTableColumn
pdu3SerialNumber = _Pdu3SerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 11, 1, 2, 1, 8),
    _Pdu3SerialNumber_Type()
)
pdu3SerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu3SerialNumber.setStatus("mandatory")


class _Pdu3Status_Type(Integer32):
    """Custom type pdu3Status based on Integer32"""
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
        *(("other", 1),
          ("ok", 2),
          ("degraded", 3),
          ("failed", 4))
    )


_Pdu3Status_Type.__name__ = "Integer32"
_Pdu3Status_Object = MibTableColumn
pdu3Status = _Pdu3Status_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 11, 1, 2, 1, 9),
    _Pdu3Status_Type()
)
pdu3Status.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu3Status.setStatus("mandatory")


class _Pdu3Controllable_Type(Integer32):
    """Custom type pdu3Controllable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("yes", 1),
          ("no", 2))
    )


_Pdu3Controllable_Type.__name__ = "Integer32"
_Pdu3Controllable_Object = MibTableColumn
pdu3Controllable = _Pdu3Controllable_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 11, 1, 2, 1, 10),
    _Pdu3Controllable_Type()
)
pdu3Controllable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu3Controllable.setStatus("mandatory")


class _Pdu3InputPhaseCount_Type(Integer32):
    """Custom type pdu3InputPhaseCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_Pdu3InputPhaseCount_Type.__name__ = "Integer32"
_Pdu3InputPhaseCount_Object = MibTableColumn
pdu3InputPhaseCount = _Pdu3InputPhaseCount_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 11, 1, 2, 1, 11),
    _Pdu3InputPhaseCount_Type()
)
pdu3InputPhaseCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu3InputPhaseCount.setStatus("mandatory")


class _Pdu3GroupCount_Type(Integer32):
    """Custom type pdu3GroupCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_Pdu3GroupCount_Type.__name__ = "Integer32"
_Pdu3GroupCount_Object = MibTableColumn
pdu3GroupCount = _Pdu3GroupCount_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 11, 1, 2, 1, 12),
    _Pdu3GroupCount_Type()
)
pdu3GroupCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu3GroupCount.setStatus("mandatory")


class _Pdu3OutletCount_Type(Integer32):
    """Custom type pdu3OutletCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_Pdu3OutletCount_Type.__name__ = "Integer32"
_Pdu3OutletCount_Object = MibTableColumn
pdu3OutletCount = _Pdu3OutletCount_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 11, 1, 2, 1, 13),
    _Pdu3OutletCount_Type()
)
pdu3OutletCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu3OutletCount.setStatus("mandatory")
_Pdu3MACAddress_Type = DisplayString
_Pdu3MACAddress_Object = MibTableColumn
pdu3MACAddress = _Pdu3MACAddress_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 11, 1, 2, 1, 14),
    _Pdu3MACAddress_Type()
)
pdu3MACAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu3MACAddress.setStatus("mandatory")
_Pdu3IPv4Address_Type = DisplayString
_Pdu3IPv4Address_Object = MibTableColumn
pdu3IPv4Address = _Pdu3IPv4Address_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 11, 1, 2, 1, 15),
    _Pdu3IPv4Address_Type()
)
pdu3IPv4Address.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu3IPv4Address.setStatus("mandatory")
_Pdu3IPv6Address_Type = DisplayString
_Pdu3IPv6Address_Object = MibTableColumn
pdu3IPv6Address = _Pdu3IPv6Address_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 11, 1, 2, 1, 16),
    _Pdu3IPv6Address_Type()
)
pdu3IPv6Address.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu3IPv6Address.setStatus("mandatory")
_Pdu3ConfigTable_Object = MibTable
pdu3ConfigTable = _Pdu3ConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 11, 1, 3)
)
if mibBuilder.loadTexts:
    pdu3ConfigTable.setStatus("mandatory")
_Pdu3ConfigEntry_Object = MibTableRow
pdu3ConfigEntry = _Pdu3ConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 11, 1, 3, 1)
)
pdu3ConfigEntry.setIndexNames(
    (0, "CPQPOWER-MIB", "pdu3ConfigIndex"),
)
if mibBuilder.loadTexts:
    pdu3ConfigEntry.setStatus("mandatory")


class _Pdu3ConfigIndex_Type(Integer32):
    """Custom type pdu3ConfigIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 20),
    )


_Pdu3ConfigIndex_Type.__name__ = "Integer32"
_Pdu3ConfigIndex_Object = MibTableColumn
pdu3ConfigIndex = _Pdu3ConfigIndex_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 11, 1, 3, 1, 1),
    _Pdu3ConfigIndex_Type()
)
pdu3ConfigIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu3ConfigIndex.setStatus("mandatory")


class _Pdu3ConfigSsh_Type(Integer32):
    """Custom type pdu3ConfigSsh based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_Pdu3ConfigSsh_Type.__name__ = "Integer32"
_Pdu3ConfigSsh_Object = MibTableColumn
pdu3ConfigSsh = _Pdu3ConfigSsh_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 11, 1, 3, 1, 2),
    _Pdu3ConfigSsh_Type()
)
pdu3ConfigSsh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu3ConfigSsh.setStatus("mandatory")


class _Pdu3ConfigFtps_Type(Integer32):
    """Custom type pdu3ConfigFtps based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_Pdu3ConfigFtps_Type.__name__ = "Integer32"
_Pdu3ConfigFtps_Object = MibTableColumn
pdu3ConfigFtps = _Pdu3ConfigFtps_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 11, 1, 3, 1, 3),
    _Pdu3ConfigFtps_Type()
)
pdu3ConfigFtps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu3ConfigFtps.setStatus("mandatory")


class _Pdu3ConfigHttp_Type(Integer32):
    """Custom type pdu3ConfigHttp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_Pdu3ConfigHttp_Type.__name__ = "Integer32"
_Pdu3ConfigHttp_Object = MibTableColumn
pdu3ConfigHttp = _Pdu3ConfigHttp_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 11, 1, 3, 1, 4),
    _Pdu3ConfigHttp_Type()
)
pdu3ConfigHttp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu3ConfigHttp.setStatus("mandatory")


class _Pdu3ConfigHttps_Type(Integer32):
    """Custom type pdu3ConfigHttps based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_Pdu3ConfigHttps_Type.__name__ = "Integer32"
_Pdu3ConfigHttps_Object = MibTableColumn
pdu3ConfigHttps = _Pdu3ConfigHttps_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 11, 1, 3, 1, 5),
    _Pdu3ConfigHttps_Type()
)
pdu3ConfigHttps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu3ConfigHttps.setStatus("mandatory")


class _Pdu3ConfigIPv4IPv6Switch_Type(Integer32):
    """Custom type pdu3ConfigIPv4IPv6Switch based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("iPv4", 1),
          ("iPv6", 2),
          ("iPv4IPv6", 3))
    )


_Pdu3ConfigIPv4IPv6Switch_Type.__name__ = "Integer32"
_Pdu3ConfigIPv4IPv6Switch_Object = MibTableColumn
pdu3ConfigIPv4IPv6Switch = _Pdu3ConfigIPv4IPv6Switch_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 11, 1, 3, 1, 6),
    _Pdu3ConfigIPv4IPv6Switch_Type()
)
pdu3ConfigIPv4IPv6Switch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu3ConfigIPv4IPv6Switch.setStatus("mandatory")


class _Pdu3ConfigRedfishAPI_Type(Integer32):
    """Custom type pdu3ConfigRedfishAPI based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_Pdu3ConfigRedfishAPI_Type.__name__ = "Integer32"
_Pdu3ConfigRedfishAPI_Object = MibTableColumn
pdu3ConfigRedfishAPI = _Pdu3ConfigRedfishAPI_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 11, 1, 3, 1, 7),
    _Pdu3ConfigRedfishAPI_Type()
)
pdu3ConfigRedfishAPI.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pdu3ConfigRedfishAPI.setStatus("mandatory")


class _Pdu3ConfigOledDispalyOrientation_Type(Integer32):
    """Custom type pdu3ConfigOledDispalyOrientation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("displayNormal", 1),
          ("displayReverse", 2))
    )


_Pdu3ConfigOledDispalyOrientation_Type.__name__ = "Integer32"
_Pdu3ConfigOledDispalyOrientation_Object = MibTableColumn
pdu3ConfigOledDispalyOrientation = _Pdu3ConfigOledDispalyOrientation_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 11, 1, 3, 1, 8),
    _Pdu3ConfigOledDispalyOrientation_Type()
)
pdu3ConfigOledDispalyOrientation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pdu3ConfigOledDispalyOrientation.setStatus("mandatory")


class _Pdu3ConfigEnergyReset_Type(Integer32):
    """Custom type pdu3ConfigEnergyReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("noOperation", 1),
          ("reset", 2),
          ("notSupported", 3))
    )


_Pdu3ConfigEnergyReset_Type.__name__ = "Integer32"
_Pdu3ConfigEnergyReset_Object = MibTableColumn
pdu3ConfigEnergyReset = _Pdu3ConfigEnergyReset_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 11, 1, 3, 1, 9),
    _Pdu3ConfigEnergyReset_Type()
)
pdu3ConfigEnergyReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pdu3ConfigEnergyReset.setStatus("mandatory")


class _Pdu3ConfigNetworkManagementCardReset_Type(Integer32):
    """Custom type pdu3ConfigNetworkManagementCardReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("noOperation", 0),
          ("reset", 1))
    )


_Pdu3ConfigNetworkManagementCardReset_Type.__name__ = "Integer32"
_Pdu3ConfigNetworkManagementCardReset_Object = MibTableColumn
pdu3ConfigNetworkManagementCardReset = _Pdu3ConfigNetworkManagementCardReset_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 11, 1, 3, 1, 10),
    _Pdu3ConfigNetworkManagementCardReset_Type()
)
pdu3ConfigNetworkManagementCardReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pdu3ConfigNetworkManagementCardReset.setStatus("mandatory")


class _Pdu3ConfigDaisyChainStatus_Type(Integer32):
    """Custom type pdu3ConfigDaisyChainStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            0
        )
    )
    namedValues = NamedValues(
        ("daisychain", 0)
    )


_Pdu3ConfigDaisyChainStatus_Type.__name__ = "Integer32"
_Pdu3ConfigDaisyChainStatus_Object = MibTableColumn
pdu3ConfigDaisyChainStatus = _Pdu3ConfigDaisyChainStatus_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 11, 1, 3, 1, 11),
    _Pdu3ConfigDaisyChainStatus_Type()
)
pdu3ConfigDaisyChainStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pdu3ConfigDaisyChainStatus.setStatus("mandatory")
_Pdu3Input_ObjectIdentity = ObjectIdentity
pdu3Input = _Pdu3Input_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 165, 11, 2)
)
_Pdu3InputTable_Object = MibTable
pdu3InputTable = _Pdu3InputTable_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 11, 2, 1)
)
if mibBuilder.loadTexts:
    pdu3InputTable.setStatus("mandatory")
_Pdu3InputEntry_Object = MibTableRow
pdu3InputEntry = _Pdu3InputEntry_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 11, 2, 1, 1)
)
pdu3InputEntry.setIndexNames(
    (0, "CPQPOWER-MIB", "pdu3IdentIndex"),
)
if mibBuilder.loadTexts:
    pdu3InputEntry.setStatus("mandatory")


class _Pdu3InputType_Type(Integer32):
    """Custom type pdu3InputType based on Integer32"""
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
        *(("singlePhase", 1),
          ("splitPhase", 2),
          ("threePhaseDelta", 3),
          ("threePhaseWye", 4))
    )


_Pdu3InputType_Type.__name__ = "Integer32"
_Pdu3InputType_Object = MibTableColumn
pdu3InputType = _Pdu3InputType_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 11, 2, 1, 1, 1),
    _Pdu3InputType_Type()
)
pdu3InputType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu3InputType.setStatus("mandatory")


class _Pdu3InputFrequency_Type(Integer32):
    """Custom type pdu3InputFrequency based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_Pdu3InputFrequency_Type.__name__ = "Integer32"
_Pdu3InputFrequency_Object = MibTableColumn
pdu3InputFrequency = _Pdu3InputFrequency_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 11, 2, 1, 1, 2),
    _Pdu3InputFrequency_Type()
)
pdu3InputFrequency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu3InputFrequency.setStatus("mandatory")


class _Pdu3InputFrequencyStatus_Type(Integer32):
    """Custom type pdu3InputFrequencyStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("good", 1),
          ("outOfRange", 2))
    )


_Pdu3InputFrequencyStatus_Type.__name__ = "Integer32"
_Pdu3InputFrequencyStatus_Object = MibTableColumn
pdu3InputFrequencyStatus = _Pdu3InputFrequencyStatus_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 11, 2, 1, 1, 3),
    _Pdu3InputFrequencyStatus_Type()
)
pdu3InputFrequencyStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu3InputFrequencyStatus.setStatus("mandatory")
_Pdu3InputPowerVA_Type = Integer32
_Pdu3InputPowerVA_Object = MibTableColumn
pdu3InputPowerVA = _Pdu3InputPowerVA_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 11, 2, 1, 1, 4),
    _Pdu3InputPowerVA_Type()
)
pdu3InputPowerVA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu3InputPowerVA.setStatus("mandatory")
_Pdu3InputPowerWatts_Type = Integer32
_Pdu3InputPowerWatts_Object = MibTableColumn
pdu3InputPowerWatts = _Pdu3InputPowerWatts_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 11, 2, 1, 1, 5),
    _Pdu3InputPowerWatts_Type()
)
pdu3InputPowerWatts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu3InputPowerWatts.setStatus("mandatory")
_Pdu3InputTotalEnergy_Type = Integer32
_Pdu3InputTotalEnergy_Object = MibTableColumn
pdu3InputTotalEnergy = _Pdu3InputTotalEnergy_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 11, 2, 1, 1, 6),
    _Pdu3InputTotalEnergy_Type()
)
pdu3InputTotalEnergy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu3InputTotalEnergy.setStatus("mandatory")


class _Pdu3InputPowerWattHourTimer_Type(DisplayString):
    """Custom type pdu3InputPowerWattHourTimer based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 22),
    )


_Pdu3InputPowerWattHourTimer_Type.__name__ = "DisplayString"
_Pdu3InputPowerWattHourTimer_Object = MibTableColumn
pdu3InputPowerWattHourTimer = _Pdu3InputPowerWattHourTimer_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 11, 2, 1, 1, 7),
    _Pdu3InputPowerWattHourTimer_Type()
)
pdu3InputPowerWattHourTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu3InputPowerWattHourTimer.setStatus("mandatory")
_Pdu3InputResettableEnergy_Type = Integer32
_Pdu3InputResettableEnergy_Object = MibTableColumn
pdu3InputResettableEnergy = _Pdu3InputResettableEnergy_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 11, 2, 1, 1, 8),
    _Pdu3InputResettableEnergy_Type()
)
pdu3InputResettableEnergy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu3InputResettableEnergy.setStatus("mandatory")
_Pdu3InputPowerFactor_Type = Integer32
_Pdu3InputPowerFactor_Object = MibTableColumn
pdu3InputPowerFactor = _Pdu3InputPowerFactor_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 11, 2, 1, 1, 9),
    _Pdu3InputPowerFactor_Type()
)
pdu3InputPowerFactor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu3InputPowerFactor.setStatus("mandatory")
_Pdu3InputPowerVAR_Type = Integer32
_Pdu3InputPowerVAR_Object = MibTableColumn
pdu3InputPowerVAR = _Pdu3InputPowerVAR_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 11, 2, 1, 1, 10),
    _Pdu3InputPowerVAR_Type()
)
pdu3InputPowerVAR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu3InputPowerVAR.setStatus("mandatory")
_Pdu3InputPhaseTable_Object = MibTable
pdu3InputPhaseTable = _Pdu3InputPhaseTable_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 11, 2, 2)
)
if mibBuilder.loadTexts:
    pdu3InputPhaseTable.setStatus("mandatory")
_Pdu3InputPhaseEntry_Object = MibTableRow
pdu3InputPhaseEntry = _Pdu3InputPhaseEntry_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 11, 2, 2, 1)
)
pdu3InputPhaseEntry.setIndexNames(
    (0, "CPQPOWER-MIB", "pdu3IdentIndex"),
    (0, "CPQPOWER-MIB", "pdu3InputPhaseIndex"),
)
if mibBuilder.loadTexts:
    pdu3InputPhaseEntry.setStatus("mandatory")


class _Pdu3InputPhaseIndex_Type(Integer32):
    """Custom type pdu3InputPhaseIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Pdu3InputPhaseIndex_Type.__name__ = "Integer32"
_Pdu3InputPhaseIndex_Object = MibTableColumn
pdu3InputPhaseIndex = _Pdu3InputPhaseIndex_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 11, 2, 2, 1, 1),
    _Pdu3InputPhaseIndex_Type()
)
pdu3InputPhaseIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu3InputPhaseIndex.setStatus("mandatory")


class _Pdu3InputPhaseVoltageMeasType_Type(Integer32):
    """Custom type pdu3InputPhaseVoltageMeasType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("singlePhase", 1),
          ("phase1toN", 2),
          ("phase2toN", 3),
          ("phase3toN", 4),
          ("phase1to2", 5),
          ("phase2to3", 6),
          ("phase3to1", 7))
    )


_Pdu3InputPhaseVoltageMeasType_Type.__name__ = "Integer32"
_Pdu3InputPhaseVoltageMeasType_Object = MibTableColumn
pdu3InputPhaseVoltageMeasType = _Pdu3InputPhaseVoltageMeasType_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 11, 2, 2, 1, 2),
    _Pdu3InputPhaseVoltageMeasType_Type()
)
pdu3InputPhaseVoltageMeasType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu3InputPhaseVoltageMeasType.setStatus("mandatory")
_Pdu3InputPhaseVoltage_Type = Integer32
_Pdu3InputPhaseVoltage_Object = MibTableColumn
pdu3InputPhaseVoltage = _Pdu3InputPhaseVoltage_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 11, 2, 2, 1, 3),
    _Pdu3InputPhaseVoltage_Type()
)
pdu3InputPhaseVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu3InputPhaseVoltage.setStatus("mandatory")


class _Pdu3InputPhaseVoltageThStatus_Type(Integer32):
    """Custom type pdu3InputPhaseVoltageThStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("good", 1),
          ("lowWarning", 2),
          ("lowCritical", 3),
          ("highWarning", 4),
          ("highCritical", 5))
    )


_Pdu3InputPhaseVoltageThStatus_Type.__name__ = "Integer32"
_Pdu3InputPhaseVoltageThStatus_Object = MibTableColumn
pdu3InputPhaseVoltageThStatus = _Pdu3InputPhaseVoltageThStatus_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 11, 2, 2, 1, 4),
    _Pdu3InputPhaseVoltageThStatus_Type()
)
pdu3InputPhaseVoltageThStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu3InputPhaseVoltageThStatus.setStatus("mandatory")


class _Pdu3InputPhaseVoltageThLowerWarning_Type(Integer32):
    """Custom type pdu3InputPhaseVoltageThLowerWarning based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 500000),
    )


_Pdu3InputPhaseVoltageThLowerWarning_Type.__name__ = "Integer32"
_Pdu3InputPhaseVoltageThLowerWarning_Object = MibTableColumn
pdu3InputPhaseVoltageThLowerWarning = _Pdu3InputPhaseVoltageThLowerWarning_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 11, 2, 2, 1, 5),
    _Pdu3InputPhaseVoltageThLowerWarning_Type()
)
pdu3InputPhaseVoltageThLowerWarning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu3InputPhaseVoltageThLowerWarning.setStatus("mandatory")


class _Pdu3InputPhaseVoltageThLowerCritical_Type(Integer32):
    """Custom type pdu3InputPhaseVoltageThLowerCritical based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 500000),
    )


_Pdu3InputPhaseVoltageThLowerCritical_Type.__name__ = "Integer32"
_Pdu3InputPhaseVoltageThLowerCritical_Object = MibTableColumn
pdu3InputPhaseVoltageThLowerCritical = _Pdu3InputPhaseVoltageThLowerCritical_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 11, 2, 2, 1, 6),
    _Pdu3InputPhaseVoltageThLowerCritical_Type()
)
pdu3InputPhaseVoltageThLowerCritical.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu3InputPhaseVoltageThLowerCritical.setStatus("mandatory")


class _Pdu3InputPhaseVoltageThUpperWarning_Type(Integer32):
    """Custom type pdu3InputPhaseVoltageThUpperWarning based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 500000),
    )


_Pdu3InputPhaseVoltageThUpperWarning_Type.__name__ = "Integer32"
_Pdu3InputPhaseVoltageThUpperWarning_Object = MibTableColumn
pdu3InputPhaseVoltageThUpperWarning = _Pdu3InputPhaseVoltageThUpperWarning_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 11, 2, 2, 1, 7),
    _Pdu3InputPhaseVoltageThUpperWarning_Type()
)
pdu3InputPhaseVoltageThUpperWarning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu3InputPhaseVoltageThUpperWarning.setStatus("mandatory")


class _Pdu3InputPhaseVoltageThUpperCritical_Type(Integer32):
    """Custom type pdu3InputPhaseVoltageThUpperCritical based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 500000),
    )


_Pdu3InputPhaseVoltageThUpperCritical_Type.__name__ = "Integer32"
_Pdu3InputPhaseVoltageThUpperCritical_Object = MibTableColumn
pdu3InputPhaseVoltageThUpperCritical = _Pdu3InputPhaseVoltageThUpperCritical_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 11, 2, 2, 1, 8),
    _Pdu3InputPhaseVoltageThUpperCritical_Type()
)
pdu3InputPhaseVoltageThUpperCritical.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu3InputPhaseVoltageThUpperCritical.setStatus("mandatory")


class _Pdu3InputPhaseCurrentMeasType_Type(Integer32):
    """Custom type pdu3InputPhaseCurrentMeasType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("singlePhase", 1),
          ("neutral", 2),
          ("phase1", 3),
          ("phase2", 4),
          ("phase3", 5))
    )


_Pdu3InputPhaseCurrentMeasType_Type.__name__ = "Integer32"
_Pdu3InputPhaseCurrentMeasType_Object = MibTableColumn
pdu3InputPhaseCurrentMeasType = _Pdu3InputPhaseCurrentMeasType_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 11, 2, 2, 1, 9),
    _Pdu3InputPhaseCurrentMeasType_Type()
)
pdu3InputPhaseCurrentMeasType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu3InputPhaseCurrentMeasType.setStatus("mandatory")
_Pdu3InputPhaseCurrentRating_Type = Integer32
_Pdu3InputPhaseCurrentRating_Object = MibTableColumn
pdu3InputPhaseCurrentRating = _Pdu3InputPhaseCurrentRating_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 11, 2, 2, 1, 10),
    _Pdu3InputPhaseCurrentRating_Type()
)
pdu3InputPhaseCurrentRating.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu3InputPhaseCurrentRating.setStatus("mandatory")
_Pdu3InputPhaseCurrent_Type = Integer32
_Pdu3InputPhaseCurrent_Object = MibTableColumn
pdu3InputPhaseCurrent = _Pdu3InputPhaseCurrent_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 11, 2, 2, 1, 11),
    _Pdu3InputPhaseCurrent_Type()
)
pdu3InputPhaseCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu3InputPhaseCurrent.setStatus("mandatory")


class _Pdu3InputPhaseCurrentThStatus_Type(Integer32):
    """Custom type pdu3InputPhaseCurrentThStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("good", 1),
          ("lowWarning", 2),
          ("lowCritical", 3),
          ("highWarning", 4),
          ("highCritical", 5))
    )


_Pdu3InputPhaseCurrentThStatus_Type.__name__ = "Integer32"
_Pdu3InputPhaseCurrentThStatus_Object = MibTableColumn
pdu3InputPhaseCurrentThStatus = _Pdu3InputPhaseCurrentThStatus_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 11, 2, 2, 1, 12),
    _Pdu3InputPhaseCurrentThStatus_Type()
)
pdu3InputPhaseCurrentThStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu3InputPhaseCurrentThStatus.setStatus("mandatory")


class _Pdu3InputPhaseCurrentThLowerWarning_Type(Integer32):
    """Custom type pdu3InputPhaseCurrentThLowerWarning based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 100000),
    )


_Pdu3InputPhaseCurrentThLowerWarning_Type.__name__ = "Integer32"
_Pdu3InputPhaseCurrentThLowerWarning_Object = MibTableColumn
pdu3InputPhaseCurrentThLowerWarning = _Pdu3InputPhaseCurrentThLowerWarning_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 11, 2, 2, 1, 13),
    _Pdu3InputPhaseCurrentThLowerWarning_Type()
)
pdu3InputPhaseCurrentThLowerWarning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu3InputPhaseCurrentThLowerWarning.setStatus("mandatory")


class _Pdu3InputPhaseCurrentThLowerCritical_Type(Integer32):
    """Custom type pdu3InputPhaseCurrentThLowerCritical based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 100000),
    )


_Pdu3InputPhaseCurrentThLowerCritical_Type.__name__ = "Integer32"
_Pdu3InputPhaseCurrentThLowerCritical_Object = MibTableColumn
pdu3InputPhaseCurrentThLowerCritical = _Pdu3InputPhaseCurrentThLowerCritical_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 11, 2, 2, 1, 14),
    _Pdu3InputPhaseCurrentThLowerCritical_Type()
)
pdu3InputPhaseCurrentThLowerCritical.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu3InputPhaseCurrentThLowerCritical.setStatus("mandatory")


class _Pdu3InputPhaseCurrentThUpperWarning_Type(Integer32):
    """Custom type pdu3InputPhaseCurrentThUpperWarning based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 100000),
    )


_Pdu3InputPhaseCurrentThUpperWarning_Type.__name__ = "Integer32"
_Pdu3InputPhaseCurrentThUpperWarning_Object = MibTableColumn
pdu3InputPhaseCurrentThUpperWarning = _Pdu3InputPhaseCurrentThUpperWarning_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 11, 2, 2, 1, 15),
    _Pdu3InputPhaseCurrentThUpperWarning_Type()
)
pdu3InputPhaseCurrentThUpperWarning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu3InputPhaseCurrentThUpperWarning.setStatus("mandatory")


class _Pdu3InputPhaseCurrentThUpperCritical_Type(Integer32):
    """Custom type pdu3InputPhaseCurrentThUpperCritical based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 100000),
    )


_Pdu3InputPhaseCurrentThUpperCritical_Type.__name__ = "Integer32"
_Pdu3InputPhaseCurrentThUpperCritical_Object = MibTableColumn
pdu3InputPhaseCurrentThUpperCritical = _Pdu3InputPhaseCurrentThUpperCritical_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 11, 2, 2, 1, 16),
    _Pdu3InputPhaseCurrentThUpperCritical_Type()
)
pdu3InputPhaseCurrentThUpperCritical.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu3InputPhaseCurrentThUpperCritical.setStatus("mandatory")
_Pdu3InputPhaseCurrentPercentLoad_Type = Integer32
_Pdu3InputPhaseCurrentPercentLoad_Object = MibTableColumn
pdu3InputPhaseCurrentPercentLoad = _Pdu3InputPhaseCurrentPercentLoad_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 11, 2, 2, 1, 17),
    _Pdu3InputPhaseCurrentPercentLoad_Type()
)
pdu3InputPhaseCurrentPercentLoad.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu3InputPhaseCurrentPercentLoad.setStatus("mandatory")


class _Pdu3InputPhasePowerMeasType_Type(Integer32):
    """Custom type pdu3InputPhasePowerMeasType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("singlePhase", 1),
          ("neutral", 2),
          ("phase1", 3),
          ("phase2", 4),
          ("phase3", 5))
    )


_Pdu3InputPhasePowerMeasType_Type.__name__ = "Integer32"
_Pdu3InputPhasePowerMeasType_Object = MibTableColumn
pdu3InputPhasePowerMeasType = _Pdu3InputPhasePowerMeasType_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 11, 2, 2, 1, 18),
    _Pdu3InputPhasePowerMeasType_Type()
)
pdu3InputPhasePowerMeasType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu3InputPhasePowerMeasType.setStatus("mandatory")
_Pdu3InputPhasePowerVA_Type = Integer32
_Pdu3InputPhasePowerVA_Object = MibTableColumn
pdu3InputPhasePowerVA = _Pdu3InputPhasePowerVA_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 11, 2, 2, 1, 19),
    _Pdu3InputPhasePowerVA_Type()
)
pdu3InputPhasePowerVA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu3InputPhasePowerVA.setStatus("mandatory")
_Pdu3InputPhasePowerWatts_Type = Integer32
_Pdu3InputPhasePowerWatts_Object = MibTableColumn
pdu3InputPhasePowerWatts = _Pdu3InputPhasePowerWatts_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 11, 2, 2, 1, 20),
    _Pdu3InputPhasePowerWatts_Type()
)
pdu3InputPhasePowerWatts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu3InputPhasePowerWatts.setStatus("mandatory")
_Pdu3InputPhasePowerWattHour_Type = Integer32
_Pdu3InputPhasePowerWattHour_Object = MibTableColumn
pdu3InputPhasePowerWattHour = _Pdu3InputPhasePowerWattHour_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 11, 2, 2, 1, 21),
    _Pdu3InputPhasePowerWattHour_Type()
)
pdu3InputPhasePowerWattHour.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu3InputPhasePowerWattHour.setStatus("mandatory")


class _Pdu3InputPhasePowerWattHourTimer_Type(DisplayString):
    """Custom type pdu3InputPhasePowerWattHourTimer based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 22),
    )


_Pdu3InputPhasePowerWattHourTimer_Type.__name__ = "DisplayString"
_Pdu3InputPhasePowerWattHourTimer_Object = MibTableColumn
pdu3InputPhasePowerWattHourTimer = _Pdu3InputPhasePowerWattHourTimer_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 11, 2, 2, 1, 22),
    _Pdu3InputPhasePowerWattHourTimer_Type()
)
pdu3InputPhasePowerWattHourTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu3InputPhasePowerWattHourTimer.setStatus("mandatory")
_Pdu3InputPhasePowerFactor_Type = Integer32
_Pdu3InputPhasePowerFactor_Object = MibTableColumn
pdu3InputPhasePowerFactor = _Pdu3InputPhasePowerFactor_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 11, 2, 2, 1, 23),
    _Pdu3InputPhasePowerFactor_Type()
)
pdu3InputPhasePowerFactor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu3InputPhasePowerFactor.setStatus("mandatory")
_Pdu3InputPhasePowerVAR_Type = Integer32
_Pdu3InputPhasePowerVAR_Object = MibTableColumn
pdu3InputPhasePowerVAR = _Pdu3InputPhasePowerVAR_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 11, 2, 2, 1, 24),
    _Pdu3InputPhasePowerVAR_Type()
)
pdu3InputPhasePowerVAR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu3InputPhasePowerVAR.setStatus("mandatory")
_Pdu3Group_ObjectIdentity = ObjectIdentity
pdu3Group = _Pdu3Group_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 165, 11, 3)
)
_Pdu3GroupTable_Object = MibTable
pdu3GroupTable = _Pdu3GroupTable_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 11, 3, 1)
)
if mibBuilder.loadTexts:
    pdu3GroupTable.setStatus("mandatory")
_Pdu3GroupEntry_Object = MibTableRow
pdu3GroupEntry = _Pdu3GroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 11, 3, 1, 1)
)
pdu3GroupEntry.setIndexNames(
    (0, "CPQPOWER-MIB", "pdu3IdentIndex"),
    (0, "CPQPOWER-MIB", "pdu3GroupIndex"),
)
if mibBuilder.loadTexts:
    pdu3GroupEntry.setStatus("mandatory")


class _Pdu3GroupIndex_Type(Integer32):
    """Custom type pdu3GroupIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Pdu3GroupIndex_Type.__name__ = "Integer32"
_Pdu3GroupIndex_Object = MibTableColumn
pdu3GroupIndex = _Pdu3GroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 11, 3, 1, 1, 1),
    _Pdu3GroupIndex_Type()
)
pdu3GroupIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu3GroupIndex.setStatus("mandatory")


class _Pdu3GroupName_Type(DisplayString):
    """Custom type pdu3GroupName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_Pdu3GroupName_Type.__name__ = "DisplayString"
_Pdu3GroupName_Object = MibTableColumn
pdu3GroupName = _Pdu3GroupName_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 11, 3, 1, 1, 2),
    _Pdu3GroupName_Type()
)
pdu3GroupName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu3GroupName.setStatus("mandatory")


class _Pdu3GroupType_Type(Integer32):
    """Custom type pdu3GroupType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("breaker1pole", 2),
          ("breaker2pole", 3),
          ("breaker3pole", 4),
          ("outletSection", 5))
    )


_Pdu3GroupType_Type.__name__ = "Integer32"
_Pdu3GroupType_Object = MibTableColumn
pdu3GroupType = _Pdu3GroupType_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 11, 3, 1, 1, 3),
    _Pdu3GroupType_Type()
)
pdu3GroupType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu3GroupType.setStatus("mandatory")


class _Pdu3GroupVoltageMeasType_Type(Integer32):
    """Custom type pdu3GroupVoltageMeasType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("singlePhase", 1),
          ("phase1toN", 2),
          ("phase2toN", 3),
          ("phase3toN", 4),
          ("phase1to2", 5),
          ("phase2to3", 6),
          ("phase3to1", 7))
    )


_Pdu3GroupVoltageMeasType_Type.__name__ = "Integer32"
_Pdu3GroupVoltageMeasType_Object = MibTableColumn
pdu3GroupVoltageMeasType = _Pdu3GroupVoltageMeasType_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 11, 3, 1, 1, 4),
    _Pdu3GroupVoltageMeasType_Type()
)
pdu3GroupVoltageMeasType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu3GroupVoltageMeasType.setStatus("mandatory")
_Pdu3GroupVoltage_Type = Integer32
_Pdu3GroupVoltage_Object = MibTableColumn
pdu3GroupVoltage = _Pdu3GroupVoltage_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 11, 3, 1, 1, 5),
    _Pdu3GroupVoltage_Type()
)
pdu3GroupVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu3GroupVoltage.setStatus("mandatory")


class _Pdu3GroupVoltageThStatus_Type(Integer32):
    """Custom type pdu3GroupVoltageThStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("good", 1),
          ("lowWarning", 2),
          ("lowCritical", 3),
          ("highWarning", 4),
          ("highCritical", 5))
    )


_Pdu3GroupVoltageThStatus_Type.__name__ = "Integer32"
_Pdu3GroupVoltageThStatus_Object = MibTableColumn
pdu3GroupVoltageThStatus = _Pdu3GroupVoltageThStatus_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 11, 3, 1, 1, 6),
    _Pdu3GroupVoltageThStatus_Type()
)
pdu3GroupVoltageThStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu3GroupVoltageThStatus.setStatus("mandatory")


class _Pdu3GroupVoltageThLowerWarning_Type(Integer32):
    """Custom type pdu3GroupVoltageThLowerWarning based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 500000),
    )


_Pdu3GroupVoltageThLowerWarning_Type.__name__ = "Integer32"
_Pdu3GroupVoltageThLowerWarning_Object = MibTableColumn
pdu3GroupVoltageThLowerWarning = _Pdu3GroupVoltageThLowerWarning_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 11, 3, 1, 1, 7),
    _Pdu3GroupVoltageThLowerWarning_Type()
)
pdu3GroupVoltageThLowerWarning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu3GroupVoltageThLowerWarning.setStatus("mandatory")


class _Pdu3GroupVoltageThLowerCritical_Type(Integer32):
    """Custom type pdu3GroupVoltageThLowerCritical based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 500000),
    )


_Pdu3GroupVoltageThLowerCritical_Type.__name__ = "Integer32"
_Pdu3GroupVoltageThLowerCritical_Object = MibTableColumn
pdu3GroupVoltageThLowerCritical = _Pdu3GroupVoltageThLowerCritical_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 11, 3, 1, 1, 8),
    _Pdu3GroupVoltageThLowerCritical_Type()
)
pdu3GroupVoltageThLowerCritical.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu3GroupVoltageThLowerCritical.setStatus("mandatory")


class _Pdu3GroupVoltageThUpperWarning_Type(Integer32):
    """Custom type pdu3GroupVoltageThUpperWarning based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 500000),
    )


_Pdu3GroupVoltageThUpperWarning_Type.__name__ = "Integer32"
_Pdu3GroupVoltageThUpperWarning_Object = MibTableColumn
pdu3GroupVoltageThUpperWarning = _Pdu3GroupVoltageThUpperWarning_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 11, 3, 1, 1, 9),
    _Pdu3GroupVoltageThUpperWarning_Type()
)
pdu3GroupVoltageThUpperWarning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu3GroupVoltageThUpperWarning.setStatus("mandatory")


class _Pdu3GroupVoltageThUpperCritical_Type(Integer32):
    """Custom type pdu3GroupVoltageThUpperCritical based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 500000),
    )


_Pdu3GroupVoltageThUpperCritical_Type.__name__ = "Integer32"
_Pdu3GroupVoltageThUpperCritical_Object = MibTableColumn
pdu3GroupVoltageThUpperCritical = _Pdu3GroupVoltageThUpperCritical_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 11, 3, 1, 1, 10),
    _Pdu3GroupVoltageThUpperCritical_Type()
)
pdu3GroupVoltageThUpperCritical.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu3GroupVoltageThUpperCritical.setStatus("mandatory")
_Pdu3groupCurrentRating_Type = Integer32
_Pdu3groupCurrentRating_Object = MibTableColumn
pdu3groupCurrentRating = _Pdu3groupCurrentRating_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 11, 3, 1, 1, 11),
    _Pdu3groupCurrentRating_Type()
)
pdu3groupCurrentRating.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu3groupCurrentRating.setStatus("mandatory")
_Pdu3GroupCurrent_Type = Integer32
_Pdu3GroupCurrent_Object = MibTableColumn
pdu3GroupCurrent = _Pdu3GroupCurrent_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 11, 3, 1, 1, 12),
    _Pdu3GroupCurrent_Type()
)
pdu3GroupCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu3GroupCurrent.setStatus("mandatory")


class _Pdu3GroupCurrentThStatus_Type(Integer32):
    """Custom type pdu3GroupCurrentThStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("good", 1),
          ("lowWarning", 2),
          ("lowCritical", 3),
          ("highWarning", 4),
          ("highCritical", 5))
    )


_Pdu3GroupCurrentThStatus_Type.__name__ = "Integer32"
_Pdu3GroupCurrentThStatus_Object = MibTableColumn
pdu3GroupCurrentThStatus = _Pdu3GroupCurrentThStatus_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 11, 3, 1, 1, 13),
    _Pdu3GroupCurrentThStatus_Type()
)
pdu3GroupCurrentThStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu3GroupCurrentThStatus.setStatus("mandatory")


class _Pdu3GroupCurrentThLowerWarning_Type(Integer32):
    """Custom type pdu3GroupCurrentThLowerWarning based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 100000),
    )


_Pdu3GroupCurrentThLowerWarning_Type.__name__ = "Integer32"
_Pdu3GroupCurrentThLowerWarning_Object = MibTableColumn
pdu3GroupCurrentThLowerWarning = _Pdu3GroupCurrentThLowerWarning_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 11, 3, 1, 1, 14),
    _Pdu3GroupCurrentThLowerWarning_Type()
)
pdu3GroupCurrentThLowerWarning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu3GroupCurrentThLowerWarning.setStatus("mandatory")


class _Pdu3GroupCurrentThLowerCritical_Type(Integer32):
    """Custom type pdu3GroupCurrentThLowerCritical based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 100000),
    )


_Pdu3GroupCurrentThLowerCritical_Type.__name__ = "Integer32"
_Pdu3GroupCurrentThLowerCritical_Object = MibTableColumn
pdu3GroupCurrentThLowerCritical = _Pdu3GroupCurrentThLowerCritical_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 11, 3, 1, 1, 15),
    _Pdu3GroupCurrentThLowerCritical_Type()
)
pdu3GroupCurrentThLowerCritical.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu3GroupCurrentThLowerCritical.setStatus("mandatory")


class _Pdu3GroupCurrentThUpperWarning_Type(Integer32):
    """Custom type pdu3GroupCurrentThUpperWarning based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 100000),
    )


_Pdu3GroupCurrentThUpperWarning_Type.__name__ = "Integer32"
_Pdu3GroupCurrentThUpperWarning_Object = MibTableColumn
pdu3GroupCurrentThUpperWarning = _Pdu3GroupCurrentThUpperWarning_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 11, 3, 1, 1, 16),
    _Pdu3GroupCurrentThUpperWarning_Type()
)
pdu3GroupCurrentThUpperWarning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu3GroupCurrentThUpperWarning.setStatus("mandatory")


class _Pdu3GroupCurrentThUpperCritical_Type(Integer32):
    """Custom type pdu3GroupCurrentThUpperCritical based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 100000),
    )


_Pdu3GroupCurrentThUpperCritical_Type.__name__ = "Integer32"
_Pdu3GroupCurrentThUpperCritical_Object = MibTableColumn
pdu3GroupCurrentThUpperCritical = _Pdu3GroupCurrentThUpperCritical_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 11, 3, 1, 1, 17),
    _Pdu3GroupCurrentThUpperCritical_Type()
)
pdu3GroupCurrentThUpperCritical.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu3GroupCurrentThUpperCritical.setStatus("mandatory")
_Pdu3GroupCurrentPercentLoad_Type = Integer32
_Pdu3GroupCurrentPercentLoad_Object = MibTableColumn
pdu3GroupCurrentPercentLoad = _Pdu3GroupCurrentPercentLoad_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 11, 3, 1, 1, 18),
    _Pdu3GroupCurrentPercentLoad_Type()
)
pdu3GroupCurrentPercentLoad.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu3GroupCurrentPercentLoad.setStatus("mandatory")
_Pdu3GroupPowerVA_Type = Integer32
_Pdu3GroupPowerVA_Object = MibTableColumn
pdu3GroupPowerVA = _Pdu3GroupPowerVA_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 11, 3, 1, 1, 19),
    _Pdu3GroupPowerVA_Type()
)
pdu3GroupPowerVA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu3GroupPowerVA.setStatus("mandatory")
_Pdu3GroupPowerWatts_Type = Integer32
_Pdu3GroupPowerWatts_Object = MibTableColumn
pdu3GroupPowerWatts = _Pdu3GroupPowerWatts_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 11, 3, 1, 1, 20),
    _Pdu3GroupPowerWatts_Type()
)
pdu3GroupPowerWatts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu3GroupPowerWatts.setStatus("mandatory")
_Pdu3GroupPowerWattHour_Type = Integer32
_Pdu3GroupPowerWattHour_Object = MibTableColumn
pdu3GroupPowerWattHour = _Pdu3GroupPowerWattHour_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 11, 3, 1, 1, 21),
    _Pdu3GroupPowerWattHour_Type()
)
pdu3GroupPowerWattHour.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu3GroupPowerWattHour.setStatus("mandatory")


class _Pdu3GroupPowerWattHourTimer_Type(DisplayString):
    """Custom type pdu3GroupPowerWattHourTimer based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 22),
    )


_Pdu3GroupPowerWattHourTimer_Type.__name__ = "DisplayString"
_Pdu3GroupPowerWattHourTimer_Object = MibTableColumn
pdu3GroupPowerWattHourTimer = _Pdu3GroupPowerWattHourTimer_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 11, 3, 1, 1, 22),
    _Pdu3GroupPowerWattHourTimer_Type()
)
pdu3GroupPowerWattHourTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu3GroupPowerWattHourTimer.setStatus("mandatory")
_Pdu3GroupPowerFactor_Type = Integer32
_Pdu3GroupPowerFactor_Object = MibTableColumn
pdu3GroupPowerFactor = _Pdu3GroupPowerFactor_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 11, 3, 1, 1, 23),
    _Pdu3GroupPowerFactor_Type()
)
pdu3GroupPowerFactor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu3GroupPowerFactor.setStatus("mandatory")
_Pdu3GroupPowerVAR_Type = Integer32
_Pdu3GroupPowerVAR_Object = MibTableColumn
pdu3GroupPowerVAR = _Pdu3GroupPowerVAR_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 11, 3, 1, 1, 24),
    _Pdu3GroupPowerVAR_Type()
)
pdu3GroupPowerVAR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu3GroupPowerVAR.setStatus("mandatory")


class _Pdu3GroupOutletCount_Type(Integer32):
    """Custom type pdu3GroupOutletCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_Pdu3GroupOutletCount_Type.__name__ = "Integer32"
_Pdu3GroupOutletCount_Object = MibTableColumn
pdu3GroupOutletCount = _Pdu3GroupOutletCount_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 11, 3, 1, 1, 25),
    _Pdu3GroupOutletCount_Type()
)
pdu3GroupOutletCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu3GroupOutletCount.setStatus("mandatory")


class _Pdu3GroupBreakerStatus_Type(Integer32):
    """Custom type pdu3GroupBreakerStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("notApplicable", 1),
          ("breakerOn", 2),
          ("breakerOff", 3))
    )


_Pdu3GroupBreakerStatus_Type.__name__ = "Integer32"
_Pdu3GroupBreakerStatus_Object = MibTableColumn
pdu3GroupBreakerStatus = _Pdu3GroupBreakerStatus_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 11, 3, 1, 1, 26),
    _Pdu3GroupBreakerStatus_Type()
)
pdu3GroupBreakerStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu3GroupBreakerStatus.setStatus("mandatory")
_Pdu3Environment_ObjectIdentity = ObjectIdentity
pdu3Environment = _Pdu3Environment_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 165, 11, 4)
)
_Pdu3EnvProbeTable_Object = MibTable
pdu3EnvProbeTable = _Pdu3EnvProbeTable_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 11, 4, 1)
)
if mibBuilder.loadTexts:
    pdu3EnvProbeTable.setStatus("mandatory")
_Pdu3EnvProbeEntry_Object = MibTableRow
pdu3EnvProbeEntry = _Pdu3EnvProbeEntry_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 11, 4, 1, 1)
)
pdu3EnvProbeEntry.setIndexNames(
    (0, "CPQPOWER-MIB", "pdu3IdentIndex"),
)
if mibBuilder.loadTexts:
    pdu3EnvProbeEntry.setStatus("mandatory")


class _Pdu3TemperatureScale_Type(Integer32):
    """Custom type pdu3TemperatureScale based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("celsius", 1),
          ("fahrenheit", 2))
    )


_Pdu3TemperatureScale_Type.__name__ = "Integer32"
_Pdu3TemperatureScale_Object = MibTableColumn
pdu3TemperatureScale = _Pdu3TemperatureScale_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 11, 4, 1, 1, 1),
    _Pdu3TemperatureScale_Type()
)
pdu3TemperatureScale.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu3TemperatureScale.setStatus("mandatory")
_Pdu3TemperatureCount_Type = Integer32
_Pdu3TemperatureCount_Object = MibTableColumn
pdu3TemperatureCount = _Pdu3TemperatureCount_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 11, 4, 1, 1, 2),
    _Pdu3TemperatureCount_Type()
)
pdu3TemperatureCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu3TemperatureCount.setStatus("mandatory")
_Pdu3HumidityCount_Type = Integer32
_Pdu3HumidityCount_Object = MibTableColumn
pdu3HumidityCount = _Pdu3HumidityCount_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 11, 4, 1, 1, 3),
    _Pdu3HumidityCount_Type()
)
pdu3HumidityCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu3HumidityCount.setStatus("mandatory")
_Pdu3ContactCount_Type = Integer32
_Pdu3ContactCount_Object = MibTableColumn
pdu3ContactCount = _Pdu3ContactCount_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 11, 4, 1, 1, 4),
    _Pdu3ContactCount_Type()
)
pdu3ContactCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu3ContactCount.setStatus("mandatory")
_Pdu3TemperatureTable_Object = MibTable
pdu3TemperatureTable = _Pdu3TemperatureTable_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 11, 4, 2)
)
if mibBuilder.loadTexts:
    pdu3TemperatureTable.setStatus("mandatory")
_Pdu3TemperatureEntry_Object = MibTableRow
pdu3TemperatureEntry = _Pdu3TemperatureEntry_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 11, 4, 2, 1)
)
pdu3TemperatureEntry.setIndexNames(
    (0, "CPQPOWER-MIB", "pdu3IdentIndex"),
    (0, "CPQPOWER-MIB", "pdu3TemperatureIndex"),
)
if mibBuilder.loadTexts:
    pdu3TemperatureEntry.setStatus("mandatory")


class _Pdu3TemperatureIndex_Type(Integer32):
    """Custom type pdu3TemperatureIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_Pdu3TemperatureIndex_Type.__name__ = "Integer32"
_Pdu3TemperatureIndex_Object = MibTableColumn
pdu3TemperatureIndex = _Pdu3TemperatureIndex_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 11, 4, 2, 1, 1),
    _Pdu3TemperatureIndex_Type()
)
pdu3TemperatureIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu3TemperatureIndex.setStatus("mandatory")


class _Pdu3TemperatureName_Type(DisplayString):
    """Custom type pdu3TemperatureName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_Pdu3TemperatureName_Type.__name__ = "DisplayString"
_Pdu3TemperatureName_Object = MibTableColumn
pdu3TemperatureName = _Pdu3TemperatureName_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 11, 4, 2, 1, 2),
    _Pdu3TemperatureName_Type()
)
pdu3TemperatureName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu3TemperatureName.setStatus("mandatory")


class _Pdu3TemperatureProbeStatus_Type(Integer32):
    """Custom type pdu3TemperatureProbeStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disconnected", 1),
          ("connected", 2),
          ("bad", 3))
    )


_Pdu3TemperatureProbeStatus_Type.__name__ = "Integer32"
_Pdu3TemperatureProbeStatus_Object = MibTableColumn
pdu3TemperatureProbeStatus = _Pdu3TemperatureProbeStatus_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 11, 4, 2, 1, 3),
    _Pdu3TemperatureProbeStatus_Type()
)
pdu3TemperatureProbeStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu3TemperatureProbeStatus.setStatus("mandatory")
_Pdu3TemperatureValue_Type = Integer32
_Pdu3TemperatureValue_Object = MibTableColumn
pdu3TemperatureValue = _Pdu3TemperatureValue_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 11, 4, 2, 1, 4),
    _Pdu3TemperatureValue_Type()
)
pdu3TemperatureValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu3TemperatureValue.setStatus("mandatory")


class _Pdu3TemperatureThStatus_Type(Integer32):
    """Custom type pdu3TemperatureThStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("good", 1),
          ("lowWarning", 2),
          ("lowCritical", 3),
          ("highWarning", 4),
          ("highCritical", 5))
    )


_Pdu3TemperatureThStatus_Type.__name__ = "Integer32"
_Pdu3TemperatureThStatus_Object = MibTableColumn
pdu3TemperatureThStatus = _Pdu3TemperatureThStatus_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 11, 4, 2, 1, 5),
    _Pdu3TemperatureThStatus_Type()
)
pdu3TemperatureThStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu3TemperatureThStatus.setStatus("mandatory")


class _Pdu3TemperatureThLowerWarning_Type(Integer32):
    """Custom type pdu3TemperatureThLowerWarning based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 150000),
    )


_Pdu3TemperatureThLowerWarning_Type.__name__ = "Integer32"
_Pdu3TemperatureThLowerWarning_Object = MibTableColumn
pdu3TemperatureThLowerWarning = _Pdu3TemperatureThLowerWarning_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 11, 4, 2, 1, 6),
    _Pdu3TemperatureThLowerWarning_Type()
)
pdu3TemperatureThLowerWarning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu3TemperatureThLowerWarning.setStatus("mandatory")


class _Pdu3TemperatureThLowerCritical_Type(Integer32):
    """Custom type pdu3TemperatureThLowerCritical based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 150000),
    )


_Pdu3TemperatureThLowerCritical_Type.__name__ = "Integer32"
_Pdu3TemperatureThLowerCritical_Object = MibTableColumn
pdu3TemperatureThLowerCritical = _Pdu3TemperatureThLowerCritical_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 11, 4, 2, 1, 7),
    _Pdu3TemperatureThLowerCritical_Type()
)
pdu3TemperatureThLowerCritical.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu3TemperatureThLowerCritical.setStatus("mandatory")


class _Pdu3TemperatureThUpperWarning_Type(Integer32):
    """Custom type pdu3TemperatureThUpperWarning based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 150000),
    )


_Pdu3TemperatureThUpperWarning_Type.__name__ = "Integer32"
_Pdu3TemperatureThUpperWarning_Object = MibTableColumn
pdu3TemperatureThUpperWarning = _Pdu3TemperatureThUpperWarning_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 11, 4, 2, 1, 8),
    _Pdu3TemperatureThUpperWarning_Type()
)
pdu3TemperatureThUpperWarning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu3TemperatureThUpperWarning.setStatus("mandatory")


class _Pdu3TemperatureThUpperCritical_Type(Integer32):
    """Custom type pdu3TemperatureThUpperCritical based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 150000),
    )


_Pdu3TemperatureThUpperCritical_Type.__name__ = "Integer32"
_Pdu3TemperatureThUpperCritical_Object = MibTableColumn
pdu3TemperatureThUpperCritical = _Pdu3TemperatureThUpperCritical_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 11, 4, 2, 1, 9),
    _Pdu3TemperatureThUpperCritical_Type()
)
pdu3TemperatureThUpperCritical.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu3TemperatureThUpperCritical.setStatus("mandatory")
_Pdu3HumidityTable_Object = MibTable
pdu3HumidityTable = _Pdu3HumidityTable_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 11, 4, 3)
)
if mibBuilder.loadTexts:
    pdu3HumidityTable.setStatus("mandatory")
_Pdu3HumidityEntry_Object = MibTableRow
pdu3HumidityEntry = _Pdu3HumidityEntry_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 11, 4, 3, 1)
)
pdu3HumidityEntry.setIndexNames(
    (0, "CPQPOWER-MIB", "pdu3IdentIndex"),
    (0, "CPQPOWER-MIB", "pdu3HumidityIndex"),
)
if mibBuilder.loadTexts:
    pdu3HumidityEntry.setStatus("mandatory")


class _Pdu3HumidityIndex_Type(Integer32):
    """Custom type pdu3HumidityIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_Pdu3HumidityIndex_Type.__name__ = "Integer32"
_Pdu3HumidityIndex_Object = MibTableColumn
pdu3HumidityIndex = _Pdu3HumidityIndex_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 11, 4, 3, 1, 1),
    _Pdu3HumidityIndex_Type()
)
pdu3HumidityIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu3HumidityIndex.setStatus("mandatory")


class _Pdu3HumidityName_Type(DisplayString):
    """Custom type pdu3HumidityName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_Pdu3HumidityName_Type.__name__ = "DisplayString"
_Pdu3HumidityName_Object = MibTableColumn
pdu3HumidityName = _Pdu3HumidityName_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 11, 4, 3, 1, 2),
    _Pdu3HumidityName_Type()
)
pdu3HumidityName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu3HumidityName.setStatus("mandatory")


class _Pdu3HumidityProbeStatus_Type(Integer32):
    """Custom type pdu3HumidityProbeStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disconnected", 1),
          ("connected", 2),
          ("bad", 3))
    )


_Pdu3HumidityProbeStatus_Type.__name__ = "Integer32"
_Pdu3HumidityProbeStatus_Object = MibTableColumn
pdu3HumidityProbeStatus = _Pdu3HumidityProbeStatus_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 11, 4, 3, 1, 3),
    _Pdu3HumidityProbeStatus_Type()
)
pdu3HumidityProbeStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu3HumidityProbeStatus.setStatus("mandatory")
_Pdu3HumidityValue_Type = Integer32
_Pdu3HumidityValue_Object = MibTableColumn
pdu3HumidityValue = _Pdu3HumidityValue_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 11, 4, 3, 1, 4),
    _Pdu3HumidityValue_Type()
)
pdu3HumidityValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu3HumidityValue.setStatus("mandatory")


class _Pdu3HumidityThStatus_Type(Integer32):
    """Custom type pdu3HumidityThStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("good", 1),
          ("lowWarning", 2),
          ("lowCritical", 3),
          ("highWarning", 4),
          ("highCritical", 5))
    )


_Pdu3HumidityThStatus_Type.__name__ = "Integer32"
_Pdu3HumidityThStatus_Object = MibTableColumn
pdu3HumidityThStatus = _Pdu3HumidityThStatus_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 11, 4, 3, 1, 5),
    _Pdu3HumidityThStatus_Type()
)
pdu3HumidityThStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu3HumidityThStatus.setStatus("mandatory")


class _Pdu3HumidityThLowerWarning_Type(Integer32):
    """Custom type pdu3HumidityThLowerWarning based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 1000),
    )


_Pdu3HumidityThLowerWarning_Type.__name__ = "Integer32"
_Pdu3HumidityThLowerWarning_Object = MibTableColumn
pdu3HumidityThLowerWarning = _Pdu3HumidityThLowerWarning_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 11, 4, 3, 1, 6),
    _Pdu3HumidityThLowerWarning_Type()
)
pdu3HumidityThLowerWarning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu3HumidityThLowerWarning.setStatus("mandatory")


class _Pdu3HumidityThLowerCritical_Type(Integer32):
    """Custom type pdu3HumidityThLowerCritical based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 1000),
    )


_Pdu3HumidityThLowerCritical_Type.__name__ = "Integer32"
_Pdu3HumidityThLowerCritical_Object = MibTableColumn
pdu3HumidityThLowerCritical = _Pdu3HumidityThLowerCritical_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 11, 4, 3, 1, 7),
    _Pdu3HumidityThLowerCritical_Type()
)
pdu3HumidityThLowerCritical.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu3HumidityThLowerCritical.setStatus("mandatory")


class _Pdu3HumidityThUpperWarning_Type(Integer32):
    """Custom type pdu3HumidityThUpperWarning based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 1000),
    )


_Pdu3HumidityThUpperWarning_Type.__name__ = "Integer32"
_Pdu3HumidityThUpperWarning_Object = MibTableColumn
pdu3HumidityThUpperWarning = _Pdu3HumidityThUpperWarning_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 11, 4, 3, 1, 8),
    _Pdu3HumidityThUpperWarning_Type()
)
pdu3HumidityThUpperWarning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu3HumidityThUpperWarning.setStatus("mandatory")


class _Pdu3HumidityThUpperCritical_Type(Integer32):
    """Custom type pdu3HumidityThUpperCritical based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 1000),
    )


_Pdu3HumidityThUpperCritical_Type.__name__ = "Integer32"
_Pdu3HumidityThUpperCritical_Object = MibTableColumn
pdu3HumidityThUpperCritical = _Pdu3HumidityThUpperCritical_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 11, 4, 3, 1, 9),
    _Pdu3HumidityThUpperCritical_Type()
)
pdu3HumidityThUpperCritical.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu3HumidityThUpperCritical.setStatus("mandatory")
_Pdu3ContactTable_Object = MibTable
pdu3ContactTable = _Pdu3ContactTable_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 11, 4, 4)
)
if mibBuilder.loadTexts:
    pdu3ContactTable.setStatus("mandatory")
_Pdu3ContactEntry_Object = MibTableRow
pdu3ContactEntry = _Pdu3ContactEntry_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 11, 4, 4, 1)
)
pdu3ContactEntry.setIndexNames(
    (0, "CPQPOWER-MIB", "pdu3IdentIndex"),
    (0, "CPQPOWER-MIB", "pdu3ContactIndex"),
)
if mibBuilder.loadTexts:
    pdu3ContactEntry.setStatus("mandatory")


class _Pdu3ContactIndex_Type(Integer32):
    """Custom type pdu3ContactIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_Pdu3ContactIndex_Type.__name__ = "Integer32"
_Pdu3ContactIndex_Object = MibTableColumn
pdu3ContactIndex = _Pdu3ContactIndex_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 11, 4, 4, 1, 1),
    _Pdu3ContactIndex_Type()
)
pdu3ContactIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu3ContactIndex.setStatus("mandatory")


class _Pdu3ContactName_Type(DisplayString):
    """Custom type pdu3ContactName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_Pdu3ContactName_Type.__name__ = "DisplayString"
_Pdu3ContactName_Object = MibTableColumn
pdu3ContactName = _Pdu3ContactName_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 11, 4, 4, 1, 2),
    _Pdu3ContactName_Type()
)
pdu3ContactName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu3ContactName.setStatus("mandatory")


class _Pdu3ContactProbeStatus_Type(Integer32):
    """Custom type pdu3ContactProbeStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disconnected", 1),
          ("connected", 2),
          ("bad", 3))
    )


_Pdu3ContactProbeStatus_Type.__name__ = "Integer32"
_Pdu3ContactProbeStatus_Object = MibTableColumn
pdu3ContactProbeStatus = _Pdu3ContactProbeStatus_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 11, 4, 4, 1, 3),
    _Pdu3ContactProbeStatus_Type()
)
pdu3ContactProbeStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu3ContactProbeStatus.setStatus("mandatory")


class _Pdu3ContactState_Type(Integer32):
    """Custom type pdu3ContactState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("contactOpen", 1),
          ("contactClosed", 2),
          ("contactBad", 3))
    )


_Pdu3ContactState_Type.__name__ = "Integer32"
_Pdu3ContactState_Object = MibTableColumn
pdu3ContactState = _Pdu3ContactState_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 11, 4, 4, 1, 4),
    _Pdu3ContactState_Type()
)
pdu3ContactState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu3ContactState.setStatus("mandatory")
_Pdu3Outlet_ObjectIdentity = ObjectIdentity
pdu3Outlet = _Pdu3Outlet_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 165, 11, 5)
)
_Pdu3OutletTable_Object = MibTable
pdu3OutletTable = _Pdu3OutletTable_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 11, 5, 1)
)
if mibBuilder.loadTexts:
    pdu3OutletTable.setStatus("mandatory")
_Pdu3OutletEntry_Object = MibTableRow
pdu3OutletEntry = _Pdu3OutletEntry_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 11, 5, 1, 1)
)
pdu3OutletEntry.setIndexNames(
    (0, "CPQPOWER-MIB", "pdu3IdentIndex"),
    (0, "CPQPOWER-MIB", "pdu3OutletIndex"),
)
if mibBuilder.loadTexts:
    pdu3OutletEntry.setStatus("mandatory")


class _Pdu3OutletIndex_Type(Integer32):
    """Custom type pdu3OutletIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Pdu3OutletIndex_Type.__name__ = "Integer32"
_Pdu3OutletIndex_Object = MibTableColumn
pdu3OutletIndex = _Pdu3OutletIndex_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 11, 5, 1, 1, 1),
    _Pdu3OutletIndex_Type()
)
pdu3OutletIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu3OutletIndex.setStatus("mandatory")


class _Pdu3OutletName_Type(DisplayString):
    """Custom type pdu3OutletName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_Pdu3OutletName_Type.__name__ = "DisplayString"
_Pdu3OutletName_Object = MibTableColumn
pdu3OutletName = _Pdu3OutletName_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 11, 5, 1, 1, 2),
    _Pdu3OutletName_Type()
)
pdu3OutletName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu3OutletName.setStatus("mandatory")


class _Pdu3OutletType_Type(Integer32):
    """Custom type pdu3OutletType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              10,
              11,
              12,
              20,
              21,
              22,
              23,
              24,
              25,
              26,
              27,
              28,
              29,
              30)
        )
    )
    namedValues = NamedValues(
        *(("iecC13", 1),
          ("iecC19", 2),
          ("uk", 10),
          ("french", 11),
          ("schuko", 12),
          ("nema515", 20),
          ("nema51520", 21),
          ("nema520", 22),
          ("nemaL520", 23),
          ("nemaL530", 24),
          ("nema615", 25),
          ("nema620", 26),
          ("nemaL620", 27),
          ("nemaL630", 28),
          ("nemaL715", 29),
          ("rf203p277", 30))
    )


_Pdu3OutletType_Type.__name__ = "Integer32"
_Pdu3OutletType_Object = MibTableColumn
pdu3OutletType = _Pdu3OutletType_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 11, 5, 1, 1, 3),
    _Pdu3OutletType_Type()
)
pdu3OutletType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu3OutletType.setStatus("mandatory")
_Pdu3OutletCurrentRating_Type = Integer32
_Pdu3OutletCurrentRating_Object = MibTableColumn
pdu3OutletCurrentRating = _Pdu3OutletCurrentRating_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 11, 5, 1, 1, 4),
    _Pdu3OutletCurrentRating_Type()
)
pdu3OutletCurrentRating.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu3OutletCurrentRating.setStatus("mandatory")
_Pdu3OutletCurrent_Type = Integer32
_Pdu3OutletCurrent_Object = MibTableColumn
pdu3OutletCurrent = _Pdu3OutletCurrent_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 11, 5, 1, 1, 5),
    _Pdu3OutletCurrent_Type()
)
pdu3OutletCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu3OutletCurrent.setStatus("mandatory")


class _Pdu3OutletActivePowerThStatus_Type(Integer32):
    """Custom type pdu3OutletActivePowerThStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("good", 1),
          ("lowWarning", 2),
          ("lowCritical", 3),
          ("highWarning", 4),
          ("highCritical", 5))
    )


_Pdu3OutletActivePowerThStatus_Type.__name__ = "Integer32"
_Pdu3OutletActivePowerThStatus_Object = MibTableColumn
pdu3OutletActivePowerThStatus = _Pdu3OutletActivePowerThStatus_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 11, 5, 1, 1, 6),
    _Pdu3OutletActivePowerThStatus_Type()
)
pdu3OutletActivePowerThStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu3OutletActivePowerThStatus.setStatus("mandatory")


class _Pdu3OutletActivePowerThLowerWarning_Type(Integer32):
    """Custom type pdu3OutletActivePowerThLowerWarning based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 10000),
    )


_Pdu3OutletActivePowerThLowerWarning_Type.__name__ = "Integer32"
_Pdu3OutletActivePowerThLowerWarning_Object = MibTableColumn
pdu3OutletActivePowerThLowerWarning = _Pdu3OutletActivePowerThLowerWarning_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 11, 5, 1, 1, 7),
    _Pdu3OutletActivePowerThLowerWarning_Type()
)
pdu3OutletActivePowerThLowerWarning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu3OutletActivePowerThLowerWarning.setStatus("mandatory")


class _Pdu3OutletActivePowerThLowerCritical_Type(Integer32):
    """Custom type pdu3OutletActivePowerThLowerCritical based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 10000),
    )


_Pdu3OutletActivePowerThLowerCritical_Type.__name__ = "Integer32"
_Pdu3OutletActivePowerThLowerCritical_Object = MibTableColumn
pdu3OutletActivePowerThLowerCritical = _Pdu3OutletActivePowerThLowerCritical_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 11, 5, 1, 1, 8),
    _Pdu3OutletActivePowerThLowerCritical_Type()
)
pdu3OutletActivePowerThLowerCritical.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu3OutletActivePowerThLowerCritical.setStatus("mandatory")


class _Pdu3OutletActivePowerThUpperWarning_Type(Integer32):
    """Custom type pdu3OutletActivePowerThUpperWarning based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 10000),
    )


_Pdu3OutletActivePowerThUpperWarning_Type.__name__ = "Integer32"
_Pdu3OutletActivePowerThUpperWarning_Object = MibTableColumn
pdu3OutletActivePowerThUpperWarning = _Pdu3OutletActivePowerThUpperWarning_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 11, 5, 1, 1, 9),
    _Pdu3OutletActivePowerThUpperWarning_Type()
)
pdu3OutletActivePowerThUpperWarning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu3OutletActivePowerThUpperWarning.setStatus("mandatory")


class _Pdu3OutletActivePowerThUpperCritical_Type(Integer32):
    """Custom type pdu3OutletActivePowerThUpperCritical based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 10000),
    )


_Pdu3OutletActivePowerThUpperCritical_Type.__name__ = "Integer32"
_Pdu3OutletActivePowerThUpperCritical_Object = MibTableColumn
pdu3OutletActivePowerThUpperCritical = _Pdu3OutletActivePowerThUpperCritical_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 11, 5, 1, 1, 10),
    _Pdu3OutletActivePowerThUpperCritical_Type()
)
pdu3OutletActivePowerThUpperCritical.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu3OutletActivePowerThUpperCritical.setStatus("mandatory")
_Pdu3OutletCurrentPercentLoad_Type = Integer32
_Pdu3OutletCurrentPercentLoad_Object = MibTableColumn
pdu3OutletCurrentPercentLoad = _Pdu3OutletCurrentPercentLoad_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 11, 5, 1, 1, 11),
    _Pdu3OutletCurrentPercentLoad_Type()
)
pdu3OutletCurrentPercentLoad.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu3OutletCurrentPercentLoad.setStatus("mandatory")
_Pdu3OutletVA_Type = Integer32
_Pdu3OutletVA_Object = MibTableColumn
pdu3OutletVA = _Pdu3OutletVA_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 11, 5, 1, 1, 12),
    _Pdu3OutletVA_Type()
)
pdu3OutletVA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu3OutletVA.setStatus("mandatory")
_Pdu3OutletWatts_Type = Integer32
_Pdu3OutletWatts_Object = MibTableColumn
pdu3OutletWatts = _Pdu3OutletWatts_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 11, 5, 1, 1, 13),
    _Pdu3OutletWatts_Type()
)
pdu3OutletWatts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu3OutletWatts.setStatus("mandatory")
_Pdu3OutletWh_Type = Integer32
_Pdu3OutletWh_Object = MibTableColumn
pdu3OutletWh = _Pdu3OutletWh_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 11, 5, 1, 1, 14),
    _Pdu3OutletWh_Type()
)
pdu3OutletWh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu3OutletWh.setStatus("mandatory")


class _Pdu3OutletWhTimer_Type(DisplayString):
    """Custom type pdu3OutletWhTimer based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 22),
    )


_Pdu3OutletWhTimer_Type.__name__ = "DisplayString"
_Pdu3OutletWhTimer_Object = MibTableColumn
pdu3OutletWhTimer = _Pdu3OutletWhTimer_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 11, 5, 1, 1, 15),
    _Pdu3OutletWhTimer_Type()
)
pdu3OutletWhTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu3OutletWhTimer.setStatus("mandatory")
_Pdu3OutletPowerFactor_Type = Integer32
_Pdu3OutletPowerFactor_Object = MibTableColumn
pdu3OutletPowerFactor = _Pdu3OutletPowerFactor_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 11, 5, 1, 1, 16),
    _Pdu3OutletPowerFactor_Type()
)
pdu3OutletPowerFactor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu3OutletPowerFactor.setStatus("mandatory")
_Pdu3OutletVAR_Type = Integer32
_Pdu3OutletVAR_Object = MibTableColumn
pdu3OutletVAR = _Pdu3OutletVAR_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 11, 5, 1, 1, 17),
    _Pdu3OutletVAR_Type()
)
pdu3OutletVAR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu3OutletVAR.setStatus("mandatory")
_Pdu3OutletControlTable_Object = MibTable
pdu3OutletControlTable = _Pdu3OutletControlTable_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 11, 5, 2)
)
if mibBuilder.loadTexts:
    pdu3OutletControlTable.setStatus("mandatory")
_Pdu3OutletControlEntry_Object = MibTableRow
pdu3OutletControlEntry = _Pdu3OutletControlEntry_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 11, 5, 2, 1)
)
pdu3OutletControlEntry.setIndexNames(
    (0, "CPQPOWER-MIB", "pdu3IdentIndex"),
    (0, "CPQPOWER-MIB", "pdu3OutletIndex"),
)
if mibBuilder.loadTexts:
    pdu3OutletControlEntry.setStatus("mandatory")


class _Pdu3OutletControlStatus_Type(Integer32):
    """Custom type pdu3OutletControlStatus based on Integer32"""
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
        *(("off", 1),
          ("on", 2),
          ("pendingOff", 3),
          ("pendingOn", 4))
    )


_Pdu3OutletControlStatus_Type.__name__ = "Integer32"
_Pdu3OutletControlStatus_Object = MibTableColumn
pdu3OutletControlStatus = _Pdu3OutletControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 11, 5, 2, 1, 1),
    _Pdu3OutletControlStatus_Type()
)
pdu3OutletControlStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu3OutletControlStatus.setStatus("mandatory")


class _Pdu3OutletControlOffCmd_Type(Integer32):
    """Custom type pdu3OutletControlOffCmd based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 99999),
    )


_Pdu3OutletControlOffCmd_Type.__name__ = "Integer32"
_Pdu3OutletControlOffCmd_Object = MibTableColumn
pdu3OutletControlOffCmd = _Pdu3OutletControlOffCmd_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 11, 5, 2, 1, 2),
    _Pdu3OutletControlOffCmd_Type()
)
pdu3OutletControlOffCmd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pdu3OutletControlOffCmd.setStatus("mandatory")


class _Pdu3OutletControlOnCmd_Type(Integer32):
    """Custom type pdu3OutletControlOnCmd based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 99999),
    )


_Pdu3OutletControlOnCmd_Type.__name__ = "Integer32"
_Pdu3OutletControlOnCmd_Object = MibTableColumn
pdu3OutletControlOnCmd = _Pdu3OutletControlOnCmd_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 11, 5, 2, 1, 3),
    _Pdu3OutletControlOnCmd_Type()
)
pdu3OutletControlOnCmd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pdu3OutletControlOnCmd.setStatus("mandatory")


class _Pdu3OutletControlRebootCmd_Type(Integer32):
    """Custom type pdu3OutletControlRebootCmd based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 99999),
    )


_Pdu3OutletControlRebootCmd_Type.__name__ = "Integer32"
_Pdu3OutletControlRebootCmd_Object = MibTableColumn
pdu3OutletControlRebootCmd = _Pdu3OutletControlRebootCmd_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 11, 5, 2, 1, 4),
    _Pdu3OutletControlRebootCmd_Type()
)
pdu3OutletControlRebootCmd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pdu3OutletControlRebootCmd.setStatus("mandatory")


class _Pdu3OutletControlPowerOnState_Type(Integer32):
    """Custom type pdu3OutletControlPowerOnState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2),
          ("lastState", 3))
    )


_Pdu3OutletControlPowerOnState_Type.__name__ = "Integer32"
_Pdu3OutletControlPowerOnState_Object = MibTableColumn
pdu3OutletControlPowerOnState = _Pdu3OutletControlPowerOnState_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 11, 5, 2, 1, 5),
    _Pdu3OutletControlPowerOnState_Type()
)
pdu3OutletControlPowerOnState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pdu3OutletControlPowerOnState.setStatus("mandatory")


class _Pdu3OutletControlSequenceDelay_Type(Integer32):
    """Custom type pdu3OutletControlSequenceDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 99999),
    )


_Pdu3OutletControlSequenceDelay_Type.__name__ = "Integer32"
_Pdu3OutletControlSequenceDelay_Object = MibTableColumn
pdu3OutletControlSequenceDelay = _Pdu3OutletControlSequenceDelay_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 11, 5, 2, 1, 6),
    _Pdu3OutletControlSequenceDelay_Type()
)
pdu3OutletControlSequenceDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pdu3OutletControlSequenceDelay.setStatus("mandatory")


class _Pdu3OutletControlRebootOffTime_Type(Integer32):
    """Custom type pdu3OutletControlRebootOffTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 99999),
    )


_Pdu3OutletControlRebootOffTime_Type.__name__ = "Integer32"
_Pdu3OutletControlRebootOffTime_Object = MibTableColumn
pdu3OutletControlRebootOffTime = _Pdu3OutletControlRebootOffTime_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 11, 5, 2, 1, 7),
    _Pdu3OutletControlRebootOffTime_Type()
)
pdu3OutletControlRebootOffTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pdu3OutletControlRebootOffTime.setStatus("mandatory")


class _Pdu3OutletControlSwitchable_Type(Integer32):
    """Custom type pdu3OutletControlSwitchable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("switchable", 1),
          ("notSwitchable", 2))
    )


_Pdu3OutletControlSwitchable_Type.__name__ = "Integer32"
_Pdu3OutletControlSwitchable_Object = MibTableColumn
pdu3OutletControlSwitchable = _Pdu3OutletControlSwitchable_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 11, 5, 2, 1, 8),
    _Pdu3OutletControlSwitchable_Type()
)
pdu3OutletControlSwitchable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pdu3OutletControlSwitchable.setStatus("mandatory")


class _Pdu3OutletControlShutoffDelay_Type(Integer32):
    """Custom type pdu3OutletControlShutoffDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 99999),
    )


_Pdu3OutletControlShutoffDelay_Type.__name__ = "Integer32"
_Pdu3OutletControlShutoffDelay_Object = MibTableColumn
pdu3OutletControlShutoffDelay = _Pdu3OutletControlShutoffDelay_Object(
    (1, 3, 6, 1, 4, 1, 232, 165, 11, 5, 2, 1, 9),
    _Pdu3OutletControlShutoffDelay_Type()
)
pdu3OutletControlShutoffDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pdu3OutletControlShutoffDelay.setStatus("mandatory")

# Managed Objects groups


# Notification objects

trapCritical = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 165, 0, 1)
)
trapCritical.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("CPQPOWER-MIB", "trapCode"),
        ("CPQPOWER-MIB", "trapDescription"),
        ("CPQPOWER-MIB", "trapDeviceName"),
        ("CPQPOWER-MIB", "trapDeviceDetails"),
        ("CPQPOWER-MIB", "trapDeviceMgmtUrl"))
)
if mibBuilder.loadTexts:
    trapCritical.setStatus(
        ""
    )

trapWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 165, 0, 2)
)
trapWarning.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("CPQPOWER-MIB", "trapCode"),
        ("CPQPOWER-MIB", "trapDescription"),
        ("CPQPOWER-MIB", "trapDeviceName"),
        ("CPQPOWER-MIB", "trapDeviceDetails"),
        ("CPQPOWER-MIB", "trapDeviceMgmtUrl"))
)
if mibBuilder.loadTexts:
    trapWarning.setStatus(
        ""
    )

trapInformation = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 165, 0, 3)
)
trapInformation.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("CPQPOWER-MIB", "trapCode"),
        ("CPQPOWER-MIB", "trapDescription"),
        ("CPQPOWER-MIB", "trapDeviceName"),
        ("CPQPOWER-MIB", "trapDeviceDetails"),
        ("CPQPOWER-MIB", "trapDeviceMgmtUrl"))
)
if mibBuilder.loadTexts:
    trapInformation.setStatus(
        ""
    )

trapCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 165, 0, 4)
)
trapCleared.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("CPQPOWER-MIB", "trapCode"),
        ("CPQPOWER-MIB", "trapDescription"),
        ("CPQPOWER-MIB", "trapDeviceName"),
        ("CPQPOWER-MIB", "trapDeviceDetails"),
        ("CPQPOWER-MIB", "trapDeviceMgmtUrl"))
)
if mibBuilder.loadTexts:
    trapCleared.setStatus(
        ""
    )

trapTest = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 165, 0, 5)
)
trapTest.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("CPQPOWER-MIB", "trapCode"),
        ("CPQPOWER-MIB", "trapDescription"),
        ("CPQPOWER-MIB", "trapDeviceName"),
        ("CPQPOWER-MIB", "trapDeviceDetails"),
        ("CPQPOWER-MIB", "trapDeviceMgmtUrl"))
)
if mibBuilder.loadTexts:
    trapTest.setStatus(
        ""
    )

deviceTrapInitialization = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 165, 0, 6)
)
deviceTrapInitialization.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("CPQPOWER-MIB", "deviceIdentName"))
)
if mibBuilder.loadTexts:
    deviceTrapInitialization.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CPQPOWER-MIB",
    **{"cpqPower": cpqPower,
       "trapCritical": trapCritical,
       "trapWarning": trapWarning,
       "trapInformation": trapInformation,
       "trapCleared": trapCleared,
       "trapTest": trapTest,
       "deviceTrapInitialization": deviceTrapInitialization,
       "powerDevice": powerDevice,
       "trapInfo": trapInfo,
       "trapCode": trapCode,
       "trapDescription": trapDescription,
       "trapDeviceMgmtUrl": trapDeviceMgmtUrl,
       "trapDeviceDetails": trapDeviceDetails,
       "trapDeviceName": trapDeviceName,
       "managementModuleIdent": managementModuleIdent,
       "deviceManufacturer": deviceManufacturer,
       "deviceModel": deviceModel,
       "deviceFirmwareVersion": deviceFirmwareVersion,
       "deviceHardwareVersion": deviceHardwareVersion,
       "deviceIdentName": deviceIdentName,
       "devicePartNumber": devicePartNumber,
       "deviceSerialNumber": deviceSerialNumber,
       "deviceMACAddress": deviceMACAddress,
       "pdu": pdu,
       "pduIdent": pduIdent,
       "numOfPdu": numOfPdu,
       "pduIdentTable": pduIdentTable,
       "pduIdentEntry": pduIdentEntry,
       "pduIdentIndex": pduIdentIndex,
       "pduName": pduName,
       "pduModel": pduModel,
       "pduManufacturer": pduManufacturer,
       "pduFirmwareVersion": pduFirmwareVersion,
       "pduPartNumber": pduPartNumber,
       "pduSerialNumber": pduSerialNumber,
       "pduStatus": pduStatus,
       "pduControllable": pduControllable,
       "pduInput": pduInput,
       "pduInputTable": pduInputTable,
       "pduInputEntry": pduInputEntry,
       "pduInputIndex": pduInputIndex,
       "inputVoltage": inputVoltage,
       "inputCurrent": inputCurrent,
       "pduOutput": pduOutput,
       "pduOutputTable": pduOutputTable,
       "pduOutputEntry": pduOutputEntry,
       "pduOutputIndex": pduOutputIndex,
       "pduOutputLoad": pduOutputLoad,
       "pduOutputHeat": pduOutputHeat,
       "pduOutputPower": pduOutputPower,
       "pduOutputNumBreakers": pduOutputNumBreakers,
       "pduOutputBreakerTable": pduOutputBreakerTable,
       "pduOutputBreakerEntry": pduOutputBreakerEntry,
       "breakerIndex": breakerIndex,
       "breakerVoltage": breakerVoltage,
       "breakerCurrent": breakerCurrent,
       "breakerPercentLoad": breakerPercentLoad,
       "breakerStatus": breakerStatus,
       "ups": ups,
       "upsIdent": upsIdent,
       "upsIdentManufacturer": upsIdentManufacturer,
       "upsIdentModel": upsIdentModel,
       "upsIdentSoftwareVersions": upsIdentSoftwareVersions,
       "upsIdentOemCode": upsIdentOemCode,
       "upsBattery": upsBattery,
       "upsBatTimeRemaining": upsBatTimeRemaining,
       "upsBatVoltage": upsBatVoltage,
       "upsBatCurrent": upsBatCurrent,
       "upsBatCapacity": upsBatCapacity,
       "upsBatteryAbmStatus": upsBatteryAbmStatus,
       "upsInput": upsInput,
       "upsInputFrequency": upsInputFrequency,
       "upsInputLineBads": upsInputLineBads,
       "upsInputNumPhases": upsInputNumPhases,
       "upsInputTable": upsInputTable,
       "upsInputEntry": upsInputEntry,
       "upsInputPhase": upsInputPhase,
       "upsInputVoltage": upsInputVoltage,
       "upsInputCurrent": upsInputCurrent,
       "upsInputWatts": upsInputWatts,
       "upsInputSource": upsInputSource,
       "upsOutput": upsOutput,
       "upsOutputLoad": upsOutputLoad,
       "upsOutputFrequency": upsOutputFrequency,
       "upsOutputNumPhases": upsOutputNumPhases,
       "upsOutputTable": upsOutputTable,
       "upsOutputEntry": upsOutputEntry,
       "upsOutputPhase": upsOutputPhase,
       "upsOutputVoltage": upsOutputVoltage,
       "upsOutputCurrent": upsOutputCurrent,
       "upsOutputWatts": upsOutputWatts,
       "upsOutputSource": upsOutputSource,
       "upsBypass": upsBypass,
       "upsBypassFrequency": upsBypassFrequency,
       "upsBypassNumPhases": upsBypassNumPhases,
       "upsBypassTable": upsBypassTable,
       "upsBypassEntry": upsBypassEntry,
       "upsBypassPhase": upsBypassPhase,
       "upsBypassVoltage": upsBypassVoltage,
       "upsEnvironment": upsEnvironment,
       "upsEnvAmbientTemp": upsEnvAmbientTemp,
       "upsEnvAmbientLowerLimit": upsEnvAmbientLowerLimit,
       "upsEnvAmbientUpperLimit": upsEnvAmbientUpperLimit,
       "upsEnvAmbientHumidity": upsEnvAmbientHumidity,
       "upsEnvRemoteTemp": upsEnvRemoteTemp,
       "upsEnvRemoteHumidity": upsEnvRemoteHumidity,
       "upsEnvNumContacts": upsEnvNumContacts,
       "upsContactsTable": upsContactsTable,
       "upsContactsTableEntry": upsContactsTableEntry,
       "upsContactIndex": upsContactIndex,
       "upsContactType": upsContactType,
       "upsContactState": upsContactState,
       "upsContactDescr": upsContactDescr,
       "upsEnvRemoteTempLowerLimit": upsEnvRemoteTempLowerLimit,
       "upsEnvRemoteTempUpperLimit": upsEnvRemoteTempUpperLimit,
       "upsEnvRemoteHumidityLowerLimit": upsEnvRemoteHumidityLowerLimit,
       "upsEnvRemoteHumidityUpperLimit": upsEnvRemoteHumidityUpperLimit,
       "upsTest": upsTest,
       "upsTestBattery": upsTestBattery,
       "upsTestBatteryStatus": upsTestBatteryStatus,
       "upsTestTrap": upsTestTrap,
       "upsControl": upsControl,
       "upsControlOutputOffDelay": upsControlOutputOffDelay,
       "upsControlOutputOnDelay": upsControlOutputOnDelay,
       "upsControlOutputOffTrapDelay": upsControlOutputOffTrapDelay,
       "upsControlOutputOnTrapDelay": upsControlOutputOnTrapDelay,
       "upsControlToBypassDelay": upsControlToBypassDelay,
       "upsLoadShedSecsWithRestart": upsLoadShedSecsWithRestart,
       "upsConfig": upsConfig,
       "upsConfigOutputVoltage": upsConfigOutputVoltage,
       "upsConfigInputVoltage": upsConfigInputVoltage,
       "upsConfigOutputWatts": upsConfigOutputWatts,
       "upsConfigOutputFreq": upsConfigOutputFreq,
       "upsConfigDateAndTime": upsConfigDateAndTime,
       "upsConfigLowOutputVoltageLimit": upsConfigLowOutputVoltageLimit,
       "upsConfigHighOutputVoltageLimit": upsConfigHighOutputVoltageLimit,
       "upsRecep": upsRecep,
       "upsNumReceptacles": upsNumReceptacles,
       "upsRecepTable": upsRecepTable,
       "upsRecepEntry": upsRecepEntry,
       "upsRecepIndex": upsRecepIndex,
       "upsRecepStatus": upsRecepStatus,
       "upsRecepOffDelaySecs": upsRecepOffDelaySecs,
       "upsRecepOnDelaySecs": upsRecepOnDelaySecs,
       "upsRecepAutoOffDelay": upsRecepAutoOffDelay,
       "upsRecepAutoOnDelay": upsRecepAutoOnDelay,
       "upsRecepShedSecsWithRestart": upsRecepShedSecsWithRestart,
       "upsTopology": upsTopology,
       "upsTopologyType": upsTopologyType,
       "upsTopoMachineCode": upsTopoMachineCode,
       "upsTopoUnitNumber": upsTopoUnitNumber,
       "upsTopoPowerStrategy": upsTopoPowerStrategy,
       "pdr": pdr,
       "pdrIdent": pdrIdent,
       "pdrName": pdrName,
       "pdrModel": pdrModel,
       "pdrManufacturer": pdrManufacturer,
       "pdrFirmwareVersion": pdrFirmwareVersion,
       "pdrPartNumber": pdrPartNumber,
       "pdrSerialNumber": pdrSerialNumber,
       "pdrVARating": pdrVARating,
       "pdrNominalOutputVoltage": pdrNominalOutputVoltage,
       "pdrNumPhases": pdrNumPhases,
       "pdrNumPanels": pdrNumPanels,
       "pdrNumBreakers": pdrNumBreakers,
       "pdrPanel": pdrPanel,
       "pdrPanelTable": pdrPanelTable,
       "pdrPanelEntry": pdrPanelEntry,
       "pdrPanelIndex": pdrPanelIndex,
       "pdrPanelFrequency": pdrPanelFrequency,
       "pdrPanelPower": pdrPanelPower,
       "pdrPanelRatedCurrent": pdrPanelRatedCurrent,
       "pdrPanelMonthlyKWH": pdrPanelMonthlyKWH,
       "pdrPanelYearlyKWH": pdrPanelYearlyKWH,
       "pdrPanelTotalKWH": pdrPanelTotalKWH,
       "pdrPanelVoltageA": pdrPanelVoltageA,
       "pdrPanelVoltageB": pdrPanelVoltageB,
       "pdrPanelVoltageC": pdrPanelVoltageC,
       "pdrPanelCurrentA": pdrPanelCurrentA,
       "pdrPanelCurrentB": pdrPanelCurrentB,
       "pdrPanelCurrentC": pdrPanelCurrentC,
       "pdrPanelLoadA": pdrPanelLoadA,
       "pdrPanelLoadB": pdrPanelLoadB,
       "pdrPanelLoadC": pdrPanelLoadC,
       "pdrBreaker": pdrBreaker,
       "pdrBreakerTable": pdrBreakerTable,
       "pdrBreakerEntry": pdrBreakerEntry,
       "pdrBreakerIndex": pdrBreakerIndex,
       "pdrBreakerPanel": pdrBreakerPanel,
       "pdrBreakerNumPosition": pdrBreakerNumPosition,
       "pdrBreakerNumPhases": pdrBreakerNumPhases,
       "pdrBreakerNumSequence": pdrBreakerNumSequence,
       "pdrBreakerRatedCurrent": pdrBreakerRatedCurrent,
       "pdrBreakerMonthlyKWH": pdrBreakerMonthlyKWH,
       "pdrBreakerYearlyKWH": pdrBreakerYearlyKWH,
       "pdrBreakerTotalKWH": pdrBreakerTotalKWH,
       "pdrBreakerCurrent": pdrBreakerCurrent,
       "pdrBreakerCurrentPercent": pdrBreakerCurrentPercent,
       "pdrBreakerPower": pdrBreakerPower,
       "pdrBreakerPercentWarning": pdrBreakerPercentWarning,
       "pdrBreakerPercentOverload": pdrBreakerPercentOverload,
       "mpdu": mpdu,
       "mpduIdent": mpduIdent,
       "mpduNumMPDU": mpduNumMPDU,
       "mpduIdentTable": mpduIdentTable,
       "mpduIdentEntry": mpduIdentEntry,
       "mpduIdentIndex": mpduIdentIndex,
       "mpduManufacturer": mpduManufacturer,
       "mpduModel": mpduModel,
       "mpduName": mpduName,
       "mpduFirmwareVersion": mpduFirmwareVersion,
       "mpduHardwareVersion": mpduHardwareVersion,
       "mpduPartNumber": mpduPartNumber,
       "mpduSerialNumber": mpduSerialNumber,
       "mpduUUID": mpduUUID,
       "mpduIP": mpduIP,
       "mpduMACAddress": mpduMACAddress,
       "mpduControlStatus": mpduControlStatus,
       "mpduRegion": mpduRegion,
       "mpduType": mpduType,
       "mpduPowerRating": mpduPowerRating,
       "mpduInputRating": mpduInputRating,
       "mpduInputPlug": mpduInputPlug,
       "mpduNumBreakers": mpduNumBreakers,
       "mpduNumOutlet": mpduNumOutlet,
       "mpduUHeight": mpduUHeight,
       "mpduRedundantStatus": mpduRedundantStatus,
       "mpduNumSmartExtBar": mpduNumSmartExtBar,
       "mpduPanelName": mpduPanelName,
       "mpduPanelBreakerName": mpduPanelBreakerName,
       "mpduPanelBreakerRating": mpduPanelBreakerRating,
       "mpduACFeedName": mpduACFeedName,
       "mpduFloorName": mpduFloorName,
       "mpduRoomName": mpduRoomName,
       "mpduRow": mpduRow,
       "mpduRowPosition": mpduRowPosition,
       "mpduRackName": mpduRackName,
       "mpduRackHeight": mpduRackHeight,
       "mpduRackID": mpduRackID,
       "mpduUPosition": mpduUPosition,
       "mpduPairedPDUUUID": mpduPairedPDUUUID,
       "mpduPairedPDUIP": mpduPairedPDUIP,
       "mpduInstalledLocation": mpduInstalledLocation,
       "mpduTotalPowerWatt": mpduTotalPowerWatt,
       "mpduTotalPowerVA": mpduTotalPowerVA,
       "mpduTotalPercentLoad": mpduTotalPercentLoad,
       "mpduRegionalNominalVoltage": mpduRegionalNominalVoltage,
       "mpduOutput": mpduOutput,
       "mpduOutputTable": mpduOutputTable,
       "mpduOutputEntry": mpduOutputEntry,
       "mpduOutputIndex": mpduOutputIndex,
       "mpduOutputStatus": mpduOutputStatus,
       "mpduOutputBreakerRating": mpduOutputBreakerRating,
       "mpduOutputSmartDevice": mpduOutputSmartDevice,
       "mpduOutputPercentLoad": mpduOutputPercentLoad,
       "mpduOutputVoltage": mpduOutputVoltage,
       "mpduOutputCurrent": mpduOutputCurrent,
       "mpduOutputPowerVA": mpduOutputPowerVA,
       "mpduOutputPowerWatt": mpduOutputPowerWatt,
       "mpduOutputPowerFactor": mpduOutputPowerFactor,
       "mpduOutputWarningThreshold": mpduOutputWarningThreshold,
       "mpduOutputCriticalThreshold": mpduOutputCriticalThreshold,
       "mpduOutputPowerWattHour": mpduOutputPowerWattHour,
       "mpduDeviceIdent": mpduDeviceIdent,
       "mpduDeviceIdentTable": mpduDeviceIdentTable,
       "mpduDeviceIdentEntry": mpduDeviceIdentEntry,
       "mpduDeviceIdentIndex": mpduDeviceIdentIndex,
       "mpduDeviceStatus": mpduDeviceStatus,
       "mpduDeviceUIDStatus": mpduDeviceUIDStatus,
       "mpduDeviceNumOutlet": mpduDeviceNumOutlet,
       "mpduDeviceUHeight": mpduDeviceUHeight,
       "mpduDevicePowerRating": mpduDevicePowerRating,
       "mpduDeviceManufacturer": mpduDeviceManufacturer,
       "mpduDeviceType": mpduDeviceType,
       "mpduDeviceModel": mpduDeviceModel,
       "mpduDeviceName": mpduDeviceName,
       "mpduDeviceFirmwareVersion": mpduDeviceFirmwareVersion,
       "mpduDeviceHardwareVersion": mpduDeviceHardwareVersion,
       "mpduDevicePartNumber": mpduDevicePartNumber,
       "mpduDeviceSerialNumber": mpduDeviceSerialNumber,
       "mpduDeviceUUID": mpduDeviceUUID,
       "mpduDeviceIP": mpduDeviceIP,
       "mpduDeviceMAC": mpduDeviceMAC,
       "mpduDevicePSUSlotNo": mpduDevicePSUSlotNo,
       "mpduDeviceUPosition": mpduDeviceUPosition,
       "mpduDeviceDetectionThreshold": mpduDeviceDetectionThreshold,
       "mpduSmExtBarOutlet": mpduSmExtBarOutlet,
       "mpduSmExtBarOutletTable": mpduSmExtBarOutletTable,
       "mpduSmExtBarOutletEntry": mpduSmExtBarOutletEntry,
       "mpduSmExtBarOutletIndex": mpduSmExtBarOutletIndex,
       "mpduSmExtBarOutletStatus": mpduSmExtBarOutletStatus,
       "mpduSmExtBarOutletUIDStatus": mpduSmExtBarOutletUIDStatus,
       "mpduSmExtBarOutletRating": mpduSmExtBarOutletRating,
       "mpduSmExtBarOutletVoltage": mpduSmExtBarOutletVoltage,
       "mpduSmExtBarOutletCurrent": mpduSmExtBarOutletCurrent,
       "mpduSmExtBarOutletPowerWatt": mpduSmExtBarOutletPowerWatt,
       "mpduSmExtBarOutletPowerFactor": mpduSmExtBarOutletPowerFactor,
       "mpduSmExtBarOutletDeviceName": mpduSmExtBarOutletDeviceName,
       "mpduSmExtBarOutletDeviceUUID": mpduSmExtBarOutletDeviceUUID,
       "mpduSmExtBarOutletDeviceProduct": mpduSmExtBarOutletDeviceProduct,
       "mpduSmExtBarOutletDeviceIP": mpduSmExtBarOutletDeviceIP,
       "mpduSmExtBarOutletAutoDiscovered": mpduSmExtBarOutletAutoDiscovered,
       "mpduSmExtBarOutletDeviceMAC": mpduSmExtBarOutletDeviceMAC,
       "mpduSmExtBarOutletDeviceSN": mpduSmExtBarOutletDeviceSN,
       "mpduSmExtBarOutletDevicePSSlotNo": mpduSmExtBarOutletDevicePSSlotNo,
       "mpduSmExtBarOutletDeviceUPosition": mpduSmExtBarOutletDeviceUPosition,
       "mpduSmExtBarOutletDeviceUHeight": mpduSmExtBarOutletDeviceUHeight,
       "mpduSmExtBarOutletDeviceInstalledLocation": mpduSmExtBarOutletDeviceInstalledLocation,
       "mpduSmExtBarOutletPowerWattHour": mpduSmExtBarOutletPowerWattHour,
       "oups": oups,
       "oupsIdent": oupsIdent,
       "oupsIdentManufacturer": oupsIdentManufacturer,
       "oupsIdentModel": oupsIdentModel,
       "oupsIdentSystemFWVersion": oupsIdentSystemFWVersion,
       "oupsIdentPowerModuleFWVersion": oupsIdentPowerModuleFWVersion,
       "oupsIdentOemCode": oupsIdentOemCode,
       "oupsIdentSerialNumber": oupsIdentSerialNumber,
       "oupsIdentPartNumber": oupsIdentPartNumber,
       "oupsBattery": oupsBattery,
       "oupsBatTimeRemaining": oupsBatTimeRemaining,
       "oupsBatVoltage": oupsBatVoltage,
       "oupsBatCapacity": oupsBatCapacity,
       "oupsBatAbmStatus": oupsBatAbmStatus,
       "oupsBatTestStatus": oupsBatTestStatus,
       "oupsBatLatestTestDate": oupsBatLatestTestDate,
       "oupsBatReplacementDateBP1": oupsBatReplacementDateBP1,
       "oupsBatReplacementDateBP2": oupsBatReplacementDateBP2,
       "oupsBatToACDelay": oupsBatToACDelay,
       "oupsBatChargeDelay": oupsBatChargeDelay,
       "oupsBatNumModules": oupsBatNumModules,
       "oupsBatModel": oupsBatModel,
       "oupsBatChargingPowerLevelUtility": oupsBatChargingPowerLevelUtility,
       "oupsBatChargingPowerLevelGenerator": oupsBatChargingPowerLevelGenerator,
       "oupsBatSharedConfig": oupsBatSharedConfig,
       "oupsBatPackFWVerBP1": oupsBatPackFWVerBP1,
       "oupsBatPackFWVerBP2": oupsBatPackFWVerBP2,
       "oupsInput": oupsInput,
       "oupsInputFrequency": oupsInputFrequency,
       "oupsInputLineBads": oupsInputLineBads,
       "oupsInputNumPhases": oupsInputNumPhases,
       "oupsInputTable": oupsInputTable,
       "oupsInputEntry": oupsInputEntry,
       "oupsInputPhase": oupsInputPhase,
       "oupsInputVoltage": oupsInputVoltage,
       "oupsInputCurrent": oupsInputCurrent,
       "oupsInputWatts": oupsInputWatts,
       "oupsInputPowerFactor": oupsInputPowerFactor,
       "oupsInputDBType": oupsInputDBType,
       "oupsInputUpperVoltage": oupsInputUpperVoltage,
       "oupsInputLowerVoltage": oupsInputLowerVoltage,
       "oupsGeneratorDetection": oupsGeneratorDetection,
       "oupsInputWithGenerator": oupsInputWithGenerator,
       "oupsOutput": oupsOutput,
       "oupsOutputLoad": oupsOutputLoad,
       "oupsOutputFrequency": oupsOutputFrequency,
       "oupsOutputNumPhases": oupsOutputNumPhases,
       "oupsOutputTable": oupsOutputTable,
       "oupsOutputEntry": oupsOutputEntry,
       "oupsOutputPhase": oupsOutputPhase,
       "oupsOutputVoltage": oupsOutputVoltage,
       "oupsOutputCurrent": oupsOutputCurrent,
       "oupsOutputWatts": oupsOutputWatts,
       "oupsOutputLoadPerPhase": oupsOutputLoadPerPhase,
       "oupsOutputPowerFactor": oupsOutputPowerFactor,
       "oupsOutputSource": oupsOutputSource,
       "oupsMonitor": oupsMonitor,
       "oupsMonitorAmbientTemp": oupsMonitorAmbientTemp,
       "oupsMonitorBypassSCRTemp": oupsMonitorBypassSCRTemp,
       "oupsMonitorDDTemp": oupsMonitorDDTemp,
       "oupsMonitorInverterTemp": oupsMonitorInverterTemp,
       "oupsMonitorChargerTemp": oupsMonitorChargerTemp,
       "oupsMonitorBP1Temp": oupsMonitorBP1Temp,
       "oupsMonitorBP2Temp": oupsMonitorBP2Temp,
       "oupsMonitorRestartDelay": oupsMonitorRestartDelay,
       "oupsMonitorACCLoadLevel": oupsMonitorACCLoadLevel,
       "oupsMonitorOperatingMode": oupsMonitorOperatingMode,
       "oupsMonitorOperationType": oupsMonitorOperationType,
       "oupsTestTrap": oupsTestTrap,
       "oupsOnGenDuration": oupsOnGenDuration,
       "oupsRuntimeLimitation": oupsRuntimeLimitation,
       "oupsRackDiscovery": oupsRackDiscovery,
       "oupsRackTagVersion": oupsRackTagVersion,
       "oupsRackID": oupsRackID,
       "oupsRackPartNumber": oupsRackPartNumber,
       "oupsRackProductDescription": oupsRackProductDescription,
       "oupsRackEncULocation": oupsRackEncULocation,
       "oupsRackUHeight": oupsRackUHeight,
       "oupsRackPUUPosition": oupsRackPUUPosition,
       "oupsRackPUUHeight": oupsRackPUUHeight,
       "oupsRackBP1UPosition": oupsRackBP1UPosition,
       "oupsRackBP1UHeight": oupsRackBP1UHeight,
       "oupsRackBP2UPosition": oupsRackBP2UPosition,
       "oupsRackBP2UHeight": oupsRackBP2UHeight,
       "pdu2": pdu2,
       "pdu2Ident": pdu2Ident,
       "pdu2NumberPDU": pdu2NumberPDU,
       "pdu2IdentTable": pdu2IdentTable,
       "pdu2IdentEntry": pdu2IdentEntry,
       "pdu2IdentIndex": pdu2IdentIndex,
       "pdu2Name": pdu2Name,
       "pdu2Model": pdu2Model,
       "pdu2Manufacturer": pdu2Manufacturer,
       "pdu2FirmwareVersion": pdu2FirmwareVersion,
       "pdu2PartNumber": pdu2PartNumber,
       "pdu2SerialNumber": pdu2SerialNumber,
       "pdu2Status": pdu2Status,
       "pdu2Controllable": pdu2Controllable,
       "pdu2InputPhaseCount": pdu2InputPhaseCount,
       "pdu2GroupCount": pdu2GroupCount,
       "pdu2OutletCount": pdu2OutletCount,
       "pdu2Input": pdu2Input,
       "pdu2InputTable": pdu2InputTable,
       "pdu2InputEntry": pdu2InputEntry,
       "pdu2InputType": pdu2InputType,
       "pdu2InputFrequency": pdu2InputFrequency,
       "pdu2InputFrequencyStatus": pdu2InputFrequencyStatus,
       "pdu2InputPowerVA": pdu2InputPowerVA,
       "pdu2InputPowerWatts": pdu2InputPowerWatts,
       "pdu2InputPowerWattHour": pdu2InputPowerWattHour,
       "pdu2InputPowerWattHourTimer": pdu2InputPowerWattHourTimer,
       "pdu2InputPowerFactor": pdu2InputPowerFactor,
       "pdu2InputPowerVAR": pdu2InputPowerVAR,
       "pdu2InputPhaseTable": pdu2InputPhaseTable,
       "pdu2InputPhaseEntry": pdu2InputPhaseEntry,
       "pdu2InputPhaseIndex": pdu2InputPhaseIndex,
       "pdu2InputPhaseVoltageMeasType": pdu2InputPhaseVoltageMeasType,
       "pdu2InputPhaseVoltage": pdu2InputPhaseVoltage,
       "pdu2InputPhaseVoltageThStatus": pdu2InputPhaseVoltageThStatus,
       "pdu2InputPhaseVoltageThLowerWarning": pdu2InputPhaseVoltageThLowerWarning,
       "pdu2InputPhaseVoltageThLowerCritical": pdu2InputPhaseVoltageThLowerCritical,
       "pdu2InputPhaseVoltageThUpperWarning": pdu2InputPhaseVoltageThUpperWarning,
       "pdu2InputPhaseVoltageThUpperCritical": pdu2InputPhaseVoltageThUpperCritical,
       "pdu2InputPhaseCurrentMeasType": pdu2InputPhaseCurrentMeasType,
       "pdu2InputPhaseCurrentRating": pdu2InputPhaseCurrentRating,
       "pdu2InputPhaseCurrent": pdu2InputPhaseCurrent,
       "pdu2InputPhaseCurrentThStatus": pdu2InputPhaseCurrentThStatus,
       "pdu2InputPhaseCurrentThLowerWarning": pdu2InputPhaseCurrentThLowerWarning,
       "pdu2InputPhaseCurrentThLowerCritical": pdu2InputPhaseCurrentThLowerCritical,
       "pdu2InputPhaseCurrentThUpperWarning": pdu2InputPhaseCurrentThUpperWarning,
       "pdu2InputPhaseCurrentThUpperCritical": pdu2InputPhaseCurrentThUpperCritical,
       "pdu2InputPhaseCurrentCrestFactor": pdu2InputPhaseCurrentCrestFactor,
       "pdu2InputPhaseCurrentPercentLoad": pdu2InputPhaseCurrentPercentLoad,
       "pdu2InputPhasePowerMeasType": pdu2InputPhasePowerMeasType,
       "pdu2InputPhasePowerVA": pdu2InputPhasePowerVA,
       "pdu2InputPhasePowerWatts": pdu2InputPhasePowerWatts,
       "pdu2InputPhasePowerWattHour": pdu2InputPhasePowerWattHour,
       "pdu2InputPhasePowerWattHourTimer": pdu2InputPhasePowerWattHourTimer,
       "pdu2InputPhasePowerFactor": pdu2InputPhasePowerFactor,
       "pdu2InputPhasePowerVAR": pdu2InputPhasePowerVAR,
       "pdu2Group": pdu2Group,
       "pdu2GroupTable": pdu2GroupTable,
       "pdu2GroupEntry": pdu2GroupEntry,
       "pdu2GroupIndex": pdu2GroupIndex,
       "pdu2GroupName": pdu2GroupName,
       "pdu2GroupType": pdu2GroupType,
       "pdu2GroupVoltageMeasType": pdu2GroupVoltageMeasType,
       "pdu2GroupVoltage": pdu2GroupVoltage,
       "pdu2GroupVoltageThStatus": pdu2GroupVoltageThStatus,
       "pdu2GroupVoltageThLowerWarning": pdu2GroupVoltageThLowerWarning,
       "pdu2GroupVoltageThLowerCritical": pdu2GroupVoltageThLowerCritical,
       "pdu2GroupVoltageThUpperWarning": pdu2GroupVoltageThUpperWarning,
       "pdu2GroupVoltageThUpperCritical": pdu2GroupVoltageThUpperCritical,
       "pdu2groupCurrentRating": pdu2groupCurrentRating,
       "pdu2GroupCurrent": pdu2GroupCurrent,
       "pdu2GroupCurrentThStatus": pdu2GroupCurrentThStatus,
       "pdu2GroupCurrentThLowerWarning": pdu2GroupCurrentThLowerWarning,
       "pdu2GroupCurrentThLowerCritical": pdu2GroupCurrentThLowerCritical,
       "pdu2GroupCurrentThUpperWarning": pdu2GroupCurrentThUpperWarning,
       "pdu2GroupCurrentThUpperCritical": pdu2GroupCurrentThUpperCritical,
       "pdu2GroupCurrentCrestFactor": pdu2GroupCurrentCrestFactor,
       "pdu2GroupCurrentPercentLoad": pdu2GroupCurrentPercentLoad,
       "pdu2GroupPowerVA": pdu2GroupPowerVA,
       "pdu2GroupPowerWatts": pdu2GroupPowerWatts,
       "pdu2GroupPowerWattHour": pdu2GroupPowerWattHour,
       "pdu2GroupPowerWattHourTimer": pdu2GroupPowerWattHourTimer,
       "pdu2GroupPowerFactor": pdu2GroupPowerFactor,
       "pdu2GroupPowerVAR": pdu2GroupPowerVAR,
       "pdu2GroupOutletCount": pdu2GroupOutletCount,
       "pdu2GroupBreakerStatus": pdu2GroupBreakerStatus,
       "pdu2Environment": pdu2Environment,
       "pdu2EnvProbeTable": pdu2EnvProbeTable,
       "pdu2EnvProbeEntry": pdu2EnvProbeEntry,
       "pdu2TemperatureScale": pdu2TemperatureScale,
       "pdu2TemperatureCount": pdu2TemperatureCount,
       "pdu2HumidityCount": pdu2HumidityCount,
       "pdu2ContactCount": pdu2ContactCount,
       "pdu2TemperatureTable": pdu2TemperatureTable,
       "pdu2TemperatureEntry": pdu2TemperatureEntry,
       "pdu2TemperatureIndex": pdu2TemperatureIndex,
       "pdu2TemperatureName": pdu2TemperatureName,
       "pdu2TemperatureProbeStatus": pdu2TemperatureProbeStatus,
       "pdu2TemperatureValue": pdu2TemperatureValue,
       "pdu2TemperatureThStatus": pdu2TemperatureThStatus,
       "pdu2TemperatureThLowerWarning": pdu2TemperatureThLowerWarning,
       "pdu2TemperatureThLowerCritical": pdu2TemperatureThLowerCritical,
       "pdu2TemperatureThUpperWarning": pdu2TemperatureThUpperWarning,
       "pdu2TemperatureThUpperCritical": pdu2TemperatureThUpperCritical,
       "pdu2HumidityTable": pdu2HumidityTable,
       "pdu2HumidityEntry": pdu2HumidityEntry,
       "pdu2HumidityIndex": pdu2HumidityIndex,
       "pdu2HumidityName": pdu2HumidityName,
       "pdu2HumidityProbeStatus": pdu2HumidityProbeStatus,
       "pdu2HumidityValue": pdu2HumidityValue,
       "pdu2HumidityThStatus": pdu2HumidityThStatus,
       "pdu2HumidityThLowerWarning": pdu2HumidityThLowerWarning,
       "pdu2HumidityThLowerCritical": pdu2HumidityThLowerCritical,
       "pdu2HumidityThUpperWarning": pdu2HumidityThUpperWarning,
       "pdu2HumidityThUpperCritical": pdu2HumidityThUpperCritical,
       "pdu2ContactTable": pdu2ContactTable,
       "pdu2ContactEntry": pdu2ContactEntry,
       "pdu2ContactIndex": pdu2ContactIndex,
       "pdu2ContactName": pdu2ContactName,
       "pdu2ContactProbeStatus": pdu2ContactProbeStatus,
       "pdu2ContactState": pdu2ContactState,
       "pdu2Outlet": pdu2Outlet,
       "pdu2OutletTable": pdu2OutletTable,
       "pdu2OutletEntry": pdu2OutletEntry,
       "pdu2OutletIndex": pdu2OutletIndex,
       "pdu2OutletName": pdu2OutletName,
       "pdu2OutletType": pdu2OutletType,
       "pdu2OutletCurrentRating": pdu2OutletCurrentRating,
       "pdu2OutletCurrent": pdu2OutletCurrent,
       "pdu2OutletCurrentThStatus": pdu2OutletCurrentThStatus,
       "pdu2OutletCurrentThLowerWarning": pdu2OutletCurrentThLowerWarning,
       "pdu2OutletCurrentThLowerCritical": pdu2OutletCurrentThLowerCritical,
       "pdu2OutletCurrentThUpperWarning": pdu2OutletCurrentThUpperWarning,
       "pdu2OutletCurrentThUpperCritical": pdu2OutletCurrentThUpperCritical,
       "pdu2OutletCurrentCrestFactor": pdu2OutletCurrentCrestFactor,
       "pdu2OutletCurrentPercentLoad": pdu2OutletCurrentPercentLoad,
       "pdu2OutletVA": pdu2OutletVA,
       "pdu2OutletWatts": pdu2OutletWatts,
       "pdu2OutletWh": pdu2OutletWh,
       "pdu2OutletWhTimer": pdu2OutletWhTimer,
       "pdu2OutletPowerFactor": pdu2OutletPowerFactor,
       "pdu2OutletVAR": pdu2OutletVAR,
       "pdu2OutletControlTable": pdu2OutletControlTable,
       "pdu2OutletControlEntry": pdu2OutletControlEntry,
       "pdu2OutletControlStatus": pdu2OutletControlStatus,
       "pdu2OutletControlOffCmd": pdu2OutletControlOffCmd,
       "pdu2OutletControlOnCmd": pdu2OutletControlOnCmd,
       "pdu2OutletControlRebootCmd": pdu2OutletControlRebootCmd,
       "pdu2OutletControlPowerOnState": pdu2OutletControlPowerOnState,
       "pdu2OutletControlSequenceDelay": pdu2OutletControlSequenceDelay,
       "pdu2OutletControlRebootOffTime": pdu2OutletControlRebootOffTime,
       "pdu2OutletControlSwitchable": pdu2OutletControlSwitchable,
       "pdu2OutletControlShutoffDelay": pdu2OutletControlShutoffDelay,
       "hpdu": hpdu,
       "hpduIdent": hpduIdent,
       "hpduNumPhase": hpduNumPhase,
       "hpduIdentTable": hpduIdentTable,
       "hpduIdentEntry": hpduIdentEntry,
       "hpduIdentIndex": hpduIdentIndex,
       "hpduManufacturer": hpduManufacturer,
       "hpduModel": hpduModel,
       "hpduName": hpduName,
       "hpduFirmwareVersion": hpduFirmwareVersion,
       "hpduHardwareVersion": hpduHardwareVersion,
       "hpduPartNumber": hpduPartNumber,
       "hpduSerialNumber": hpduSerialNumber,
       "hpduUUID": hpduUUID,
       "hpduType": hpduType,
       "hpduPowerRating": hpduPowerRating,
       "hpduInputRating": hpduInputRating,
       "hpduRegionalNominalVoltage": hpduRegionalNominalVoltage,
       "hpduNumOutputBreakers": hpduNumOutputBreakers,
       "hpduNumMonitoredOutlet": hpduNumMonitoredOutlet,
       "hpduFanStatus": hpduFanStatus,
       "hpduTemperature": hpduTemperature,
       "hpduInput": hpduInput,
       "hpduInputTable": hpduInputTable,
       "hpduInputEntry": hpduInputEntry,
       "hpduInputIndex": hpduInputIndex,
       "hpduInputStatus": hpduInputStatus,
       "hpduInputBreakerRating": hpduInputBreakerRating,
       "hpduInputVoltage": hpduInputVoltage,
       "hpduInputCurrent": hpduInputCurrent,
       "hpduInputPowerVA": hpduInputPowerVA,
       "hpduInputPowerWatt": hpduInputPowerWatt,
       "hpduInputPowerFactor": hpduInputPowerFactor,
       "hpduInputWarningThreshold": hpduInputWarningThreshold,
       "hpduInputCriticalThreshold": hpduInputCriticalThreshold,
       "hpduInputPowerWattHour": hpduInputPowerWattHour,
       "hpduInputTotalEnergySince": hpduInputTotalEnergySince,
       "hpduInputEnergyMeteringTotalHours": hpduInputEnergyMeteringTotalHours,
       "hpduOutlet": hpduOutlet,
       "hpduOutletTable": hpduOutletTable,
       "hpduOutletEntry": hpduOutletEntry,
       "hpduOutletIndex": hpduOutletIndex,
       "hpduOutletStatus": hpduOutletStatus,
       "hpduOutletBreakerRating": hpduOutletBreakerRating,
       "hpduOutletPercentLoad": hpduOutletPercentLoad,
       "hpduOutletVoltage": hpduOutletVoltage,
       "hpduOutletCurrent": hpduOutletCurrent,
       "hpduOutletPowerVA": hpduOutletPowerVA,
       "hpduOutletPowerWatt": hpduOutletPowerWatt,
       "hpduOutletPowerFactor": hpduOutletPowerFactor,
       "hpduOutletWarningThreshold": hpduOutletWarningThreshold,
       "hpduOutletCriticalThreshold": hpduOutletCriticalThreshold,
       "hpduOutletPowerWattHour": hpduOutletPowerWattHour,
       "hpduOutletTotalEnergySince": hpduOutletTotalEnergySince,
       "hpduOutletEnergyMeteringTotalHours": hpduOutletEnergyMeteringTotalHours,
       "pdu3": pdu3,
       "pdu3Ident": pdu3Ident,
       "pdu3NumberPDU": pdu3NumberPDU,
       "pdu3IdentTable": pdu3IdentTable,
       "pdu3IdentEntry": pdu3IdentEntry,
       "pdu3IdentIndex": pdu3IdentIndex,
       "pdu3Name": pdu3Name,
       "pdu3Model": pdu3Model,
       "pdu3Manufacturer": pdu3Manufacturer,
       "pdu3FirmwareVersion": pdu3FirmwareVersion,
       "pdu3FirmwareVersionTimeStamp": pdu3FirmwareVersionTimeStamp,
       "pdu3PartNumber": pdu3PartNumber,
       "pdu3SerialNumber": pdu3SerialNumber,
       "pdu3Status": pdu3Status,
       "pdu3Controllable": pdu3Controllable,
       "pdu3InputPhaseCount": pdu3InputPhaseCount,
       "pdu3GroupCount": pdu3GroupCount,
       "pdu3OutletCount": pdu3OutletCount,
       "pdu3MACAddress": pdu3MACAddress,
       "pdu3IPv4Address": pdu3IPv4Address,
       "pdu3IPv6Address": pdu3IPv6Address,
       "pdu3ConfigTable": pdu3ConfigTable,
       "pdu3ConfigEntry": pdu3ConfigEntry,
       "pdu3ConfigIndex": pdu3ConfigIndex,
       "pdu3ConfigSsh": pdu3ConfigSsh,
       "pdu3ConfigFtps": pdu3ConfigFtps,
       "pdu3ConfigHttp": pdu3ConfigHttp,
       "pdu3ConfigHttps": pdu3ConfigHttps,
       "pdu3ConfigIPv4IPv6Switch": pdu3ConfigIPv4IPv6Switch,
       "pdu3ConfigRedfishAPI": pdu3ConfigRedfishAPI,
       "pdu3ConfigOledDispalyOrientation": pdu3ConfigOledDispalyOrientation,
       "pdu3ConfigEnergyReset": pdu3ConfigEnergyReset,
       "pdu3ConfigNetworkManagementCardReset": pdu3ConfigNetworkManagementCardReset,
       "pdu3ConfigDaisyChainStatus": pdu3ConfigDaisyChainStatus,
       "pdu3Input": pdu3Input,
       "pdu3InputTable": pdu3InputTable,
       "pdu3InputEntry": pdu3InputEntry,
       "pdu3InputType": pdu3InputType,
       "pdu3InputFrequency": pdu3InputFrequency,
       "pdu3InputFrequencyStatus": pdu3InputFrequencyStatus,
       "pdu3InputPowerVA": pdu3InputPowerVA,
       "pdu3InputPowerWatts": pdu3InputPowerWatts,
       "pdu3InputTotalEnergy": pdu3InputTotalEnergy,
       "pdu3InputPowerWattHourTimer": pdu3InputPowerWattHourTimer,
       "pdu3InputResettableEnergy": pdu3InputResettableEnergy,
       "pdu3InputPowerFactor": pdu3InputPowerFactor,
       "pdu3InputPowerVAR": pdu3InputPowerVAR,
       "pdu3InputPhaseTable": pdu3InputPhaseTable,
       "pdu3InputPhaseEntry": pdu3InputPhaseEntry,
       "pdu3InputPhaseIndex": pdu3InputPhaseIndex,
       "pdu3InputPhaseVoltageMeasType": pdu3InputPhaseVoltageMeasType,
       "pdu3InputPhaseVoltage": pdu3InputPhaseVoltage,
       "pdu3InputPhaseVoltageThStatus": pdu3InputPhaseVoltageThStatus,
       "pdu3InputPhaseVoltageThLowerWarning": pdu3InputPhaseVoltageThLowerWarning,
       "pdu3InputPhaseVoltageThLowerCritical": pdu3InputPhaseVoltageThLowerCritical,
       "pdu3InputPhaseVoltageThUpperWarning": pdu3InputPhaseVoltageThUpperWarning,
       "pdu3InputPhaseVoltageThUpperCritical": pdu3InputPhaseVoltageThUpperCritical,
       "pdu3InputPhaseCurrentMeasType": pdu3InputPhaseCurrentMeasType,
       "pdu3InputPhaseCurrentRating": pdu3InputPhaseCurrentRating,
       "pdu3InputPhaseCurrent": pdu3InputPhaseCurrent,
       "pdu3InputPhaseCurrentThStatus": pdu3InputPhaseCurrentThStatus,
       "pdu3InputPhaseCurrentThLowerWarning": pdu3InputPhaseCurrentThLowerWarning,
       "pdu3InputPhaseCurrentThLowerCritical": pdu3InputPhaseCurrentThLowerCritical,
       "pdu3InputPhaseCurrentThUpperWarning": pdu3InputPhaseCurrentThUpperWarning,
       "pdu3InputPhaseCurrentThUpperCritical": pdu3InputPhaseCurrentThUpperCritical,
       "pdu3InputPhaseCurrentPercentLoad": pdu3InputPhaseCurrentPercentLoad,
       "pdu3InputPhasePowerMeasType": pdu3InputPhasePowerMeasType,
       "pdu3InputPhasePowerVA": pdu3InputPhasePowerVA,
       "pdu3InputPhasePowerWatts": pdu3InputPhasePowerWatts,
       "pdu3InputPhasePowerWattHour": pdu3InputPhasePowerWattHour,
       "pdu3InputPhasePowerWattHourTimer": pdu3InputPhasePowerWattHourTimer,
       "pdu3InputPhasePowerFactor": pdu3InputPhasePowerFactor,
       "pdu3InputPhasePowerVAR": pdu3InputPhasePowerVAR,
       "pdu3Group": pdu3Group,
       "pdu3GroupTable": pdu3GroupTable,
       "pdu3GroupEntry": pdu3GroupEntry,
       "pdu3GroupIndex": pdu3GroupIndex,
       "pdu3GroupName": pdu3GroupName,
       "pdu3GroupType": pdu3GroupType,
       "pdu3GroupVoltageMeasType": pdu3GroupVoltageMeasType,
       "pdu3GroupVoltage": pdu3GroupVoltage,
       "pdu3GroupVoltageThStatus": pdu3GroupVoltageThStatus,
       "pdu3GroupVoltageThLowerWarning": pdu3GroupVoltageThLowerWarning,
       "pdu3GroupVoltageThLowerCritical": pdu3GroupVoltageThLowerCritical,
       "pdu3GroupVoltageThUpperWarning": pdu3GroupVoltageThUpperWarning,
       "pdu3GroupVoltageThUpperCritical": pdu3GroupVoltageThUpperCritical,
       "pdu3groupCurrentRating": pdu3groupCurrentRating,
       "pdu3GroupCurrent": pdu3GroupCurrent,
       "pdu3GroupCurrentThStatus": pdu3GroupCurrentThStatus,
       "pdu3GroupCurrentThLowerWarning": pdu3GroupCurrentThLowerWarning,
       "pdu3GroupCurrentThLowerCritical": pdu3GroupCurrentThLowerCritical,
       "pdu3GroupCurrentThUpperWarning": pdu3GroupCurrentThUpperWarning,
       "pdu3GroupCurrentThUpperCritical": pdu3GroupCurrentThUpperCritical,
       "pdu3GroupCurrentPercentLoad": pdu3GroupCurrentPercentLoad,
       "pdu3GroupPowerVA": pdu3GroupPowerVA,
       "pdu3GroupPowerWatts": pdu3GroupPowerWatts,
       "pdu3GroupPowerWattHour": pdu3GroupPowerWattHour,
       "pdu3GroupPowerWattHourTimer": pdu3GroupPowerWattHourTimer,
       "pdu3GroupPowerFactor": pdu3GroupPowerFactor,
       "pdu3GroupPowerVAR": pdu3GroupPowerVAR,
       "pdu3GroupOutletCount": pdu3GroupOutletCount,
       "pdu3GroupBreakerStatus": pdu3GroupBreakerStatus,
       "pdu3Environment": pdu3Environment,
       "pdu3EnvProbeTable": pdu3EnvProbeTable,
       "pdu3EnvProbeEntry": pdu3EnvProbeEntry,
       "pdu3TemperatureScale": pdu3TemperatureScale,
       "pdu3TemperatureCount": pdu3TemperatureCount,
       "pdu3HumidityCount": pdu3HumidityCount,
       "pdu3ContactCount": pdu3ContactCount,
       "pdu3TemperatureTable": pdu3TemperatureTable,
       "pdu3TemperatureEntry": pdu3TemperatureEntry,
       "pdu3TemperatureIndex": pdu3TemperatureIndex,
       "pdu3TemperatureName": pdu3TemperatureName,
       "pdu3TemperatureProbeStatus": pdu3TemperatureProbeStatus,
       "pdu3TemperatureValue": pdu3TemperatureValue,
       "pdu3TemperatureThStatus": pdu3TemperatureThStatus,
       "pdu3TemperatureThLowerWarning": pdu3TemperatureThLowerWarning,
       "pdu3TemperatureThLowerCritical": pdu3TemperatureThLowerCritical,
       "pdu3TemperatureThUpperWarning": pdu3TemperatureThUpperWarning,
       "pdu3TemperatureThUpperCritical": pdu3TemperatureThUpperCritical,
       "pdu3HumidityTable": pdu3HumidityTable,
       "pdu3HumidityEntry": pdu3HumidityEntry,
       "pdu3HumidityIndex": pdu3HumidityIndex,
       "pdu3HumidityName": pdu3HumidityName,
       "pdu3HumidityProbeStatus": pdu3HumidityProbeStatus,
       "pdu3HumidityValue": pdu3HumidityValue,
       "pdu3HumidityThStatus": pdu3HumidityThStatus,
       "pdu3HumidityThLowerWarning": pdu3HumidityThLowerWarning,
       "pdu3HumidityThLowerCritical": pdu3HumidityThLowerCritical,
       "pdu3HumidityThUpperWarning": pdu3HumidityThUpperWarning,
       "pdu3HumidityThUpperCritical": pdu3HumidityThUpperCritical,
       "pdu3ContactTable": pdu3ContactTable,
       "pdu3ContactEntry": pdu3ContactEntry,
       "pdu3ContactIndex": pdu3ContactIndex,
       "pdu3ContactName": pdu3ContactName,
       "pdu3ContactProbeStatus": pdu3ContactProbeStatus,
       "pdu3ContactState": pdu3ContactState,
       "pdu3Outlet": pdu3Outlet,
       "pdu3OutletTable": pdu3OutletTable,
       "pdu3OutletEntry": pdu3OutletEntry,
       "pdu3OutletIndex": pdu3OutletIndex,
       "pdu3OutletName": pdu3OutletName,
       "pdu3OutletType": pdu3OutletType,
       "pdu3OutletCurrentRating": pdu3OutletCurrentRating,
       "pdu3OutletCurrent": pdu3OutletCurrent,
       "pdu3OutletActivePowerThStatus": pdu3OutletActivePowerThStatus,
       "pdu3OutletActivePowerThLowerWarning": pdu3OutletActivePowerThLowerWarning,
       "pdu3OutletActivePowerThLowerCritical": pdu3OutletActivePowerThLowerCritical,
       "pdu3OutletActivePowerThUpperWarning": pdu3OutletActivePowerThUpperWarning,
       "pdu3OutletActivePowerThUpperCritical": pdu3OutletActivePowerThUpperCritical,
       "pdu3OutletCurrentPercentLoad": pdu3OutletCurrentPercentLoad,
       "pdu3OutletVA": pdu3OutletVA,
       "pdu3OutletWatts": pdu3OutletWatts,
       "pdu3OutletWh": pdu3OutletWh,
       "pdu3OutletWhTimer": pdu3OutletWhTimer,
       "pdu3OutletPowerFactor": pdu3OutletPowerFactor,
       "pdu3OutletVAR": pdu3OutletVAR,
       "pdu3OutletControlTable": pdu3OutletControlTable,
       "pdu3OutletControlEntry": pdu3OutletControlEntry,
       "pdu3OutletControlStatus": pdu3OutletControlStatus,
       "pdu3OutletControlOffCmd": pdu3OutletControlOffCmd,
       "pdu3OutletControlOnCmd": pdu3OutletControlOnCmd,
       "pdu3OutletControlRebootCmd": pdu3OutletControlRebootCmd,
       "pdu3OutletControlPowerOnState": pdu3OutletControlPowerOnState,
       "pdu3OutletControlSequenceDelay": pdu3OutletControlSequenceDelay,
       "pdu3OutletControlRebootOffTime": pdu3OutletControlRebootOffTime,
       "pdu3OutletControlSwitchable": pdu3OutletControlSwitchable,
       "pdu3OutletControlShutoffDelay": pdu3OutletControlShutoffDelay}
)
