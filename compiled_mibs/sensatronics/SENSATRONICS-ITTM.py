# SNMP MIB module (SENSATRONICS-ITTM) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\sensatronics\SENSATRONICS-ITTM

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

(envMonitors,) = mibBuilder.importSymbols(
    "SENSATRONICS-SMI",
    "envMonitors")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

productITTM = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 16174, 1, 1, 1)
)
if mibBuilder.loadTexts:
    productITTM.setRevisions(
        ("2005-02-23 09:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_UnitInfo_ObjectIdentity = ObjectIdentity
unitInfo = _UnitInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 16174, 1, 1, 1, 1)
)


class _UnitName_Type(DisplayString):
    """Custom type unitName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(32, 32),
    )
    fixed_length = 32


_UnitName_Type.__name__ = "DisplayString"
_UnitName_Object = MibScalar
unitName = _UnitName_Object(
    (1, 3, 6, 1, 4, 1, 16174, 1, 1, 1, 1, 1),
    _UnitName_Type()
)
unitName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    unitName.setStatus("current")


class _UnitModel_Type(DisplayString):
    """Custom type unitModel based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(5, 5),
    )
    fixed_length = 5


_UnitModel_Type.__name__ = "DisplayString"
_UnitModel_Object = MibScalar
unitModel = _UnitModel_Object(
    (1, 3, 6, 1, 4, 1, 16174, 1, 1, 1, 1, 2),
    _UnitModel_Type()
)
unitModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    unitModel.setStatus("current")


class _UnitManufacturer_Type(DisplayString):
    """Custom type unitManufacturer based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(12, 12),
    )
    fixed_length = 12


_UnitManufacturer_Type.__name__ = "DisplayString"
_UnitManufacturer_Object = MibScalar
unitManufacturer = _UnitManufacturer_Object(
    (1, 3, 6, 1, 4, 1, 16174, 1, 1, 1, 1, 3),
    _UnitManufacturer_Type()
)
unitManufacturer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    unitManufacturer.setStatus("current")


class _UnitWeb_Type(DisplayString):
    """Custom type unitWeb based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(28, 28),
    )
    fixed_length = 28


_UnitWeb_Type.__name__ = "DisplayString"
_UnitWeb_Object = MibScalar
unitWeb = _UnitWeb_Object(
    (1, 3, 6, 1, 4, 1, 16174, 1, 1, 1, 1, 4),
    _UnitWeb_Type()
)
unitWeb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    unitWeb.setStatus("current")


class _UnitFirmware_Type(DisplayString):
    """Custom type unitFirmware based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(5, 5),
    )
    fixed_length = 5


_UnitFirmware_Type.__name__ = "DisplayString"
_UnitFirmware_Object = MibScalar
unitFirmware = _UnitFirmware_Object(
    (1, 3, 6, 1, 4, 1, 16174, 1, 1, 1, 1, 5),
    _UnitFirmware_Type()
)
unitFirmware.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    unitFirmware.setStatus("current")


class _UnitFWReleaseDate_Type(DisplayString):
    """Custom type unitFWReleaseDate based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(18, 18),
    )
    fixed_length = 18


_UnitFWReleaseDate_Type.__name__ = "DisplayString"
_UnitFWReleaseDate_Object = MibScalar
unitFWReleaseDate = _UnitFWReleaseDate_Object(
    (1, 3, 6, 1, 4, 1, 16174, 1, 1, 1, 1, 6),
    _UnitFWReleaseDate_Type()
)
unitFWReleaseDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    unitFWReleaseDate.setStatus("current")


class _UnitSerial_Type(DisplayString):
    """Custom type unitSerial based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(32, 32),
    )
    fixed_length = 32


_UnitSerial_Type.__name__ = "DisplayString"
_UnitSerial_Object = MibScalar
unitSerial = _UnitSerial_Object(
    (1, 3, 6, 1, 4, 1, 16174, 1, 1, 1, 1, 7),
    _UnitSerial_Type()
)
unitSerial.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    unitSerial.setStatus("current")


class _UnitConfig_Type(Integer32):
    """Custom type unitConfig based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_UnitConfig_Type.__name__ = "Integer32"
_UnitConfig_Object = MibScalar
unitConfig = _UnitConfig_Object(
    (1, 3, 6, 1, 4, 1, 16174, 1, 1, 1, 1, 8),
    _UnitConfig_Type()
)
unitConfig.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    unitConfig.setStatus("current")
_ConfigData_ObjectIdentity = ObjectIdentity
configData = _ConfigData_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 16174, 1, 1, 1, 2)
)
_NetInfo_ObjectIdentity = ObjectIdentity
netInfo = _NetInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 16174, 1, 1, 1, 2, 1)
)


class _NetMode_Type(Integer32):
    """Custom type netMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_NetMode_Type.__name__ = "Integer32"
_NetMode_Object = MibScalar
netMode = _NetMode_Object(
    (1, 3, 6, 1, 4, 1, 16174, 1, 1, 1, 2, 1, 1),
    _NetMode_Type()
)
netMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netMode.setStatus("current")


class _NetIP_Type(DisplayString):
    """Custom type netIP based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )
    fixed_length = 16


_NetIP_Type.__name__ = "DisplayString"
_NetIP_Object = MibScalar
netIP = _NetIP_Object(
    (1, 3, 6, 1, 4, 1, 16174, 1, 1, 1, 2, 1, 2),
    _NetIP_Type()
)
netIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netIP.setStatus("current")


class _NetNM_Type(DisplayString):
    """Custom type netNM based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )
    fixed_length = 16


_NetNM_Type.__name__ = "DisplayString"
_NetNM_Object = MibScalar
netNM = _NetNM_Object(
    (1, 3, 6, 1, 4, 1, 16174, 1, 1, 1, 2, 1, 3),
    _NetNM_Type()
)
netNM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netNM.setStatus("current")


class _NetGW_Type(DisplayString):
    """Custom type netGW based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )
    fixed_length = 16


_NetGW_Type.__name__ = "DisplayString"
_NetGW_Object = MibScalar
netGW = _NetGW_Object(
    (1, 3, 6, 1, 4, 1, 16174, 1, 1, 1, 2, 1, 4),
    _NetGW_Type()
)
netGW.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netGW.setStatus("current")


class _NetHTTPPort_Type(Integer32):
    """Custom type netHTTPPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_NetHTTPPort_Type.__name__ = "Integer32"
_NetHTTPPort_Object = MibScalar
netHTTPPort = _NetHTTPPort_Object(
    (1, 3, 6, 1, 4, 1, 16174, 1, 1, 1, 2, 1, 5),
    _NetHTTPPort_Type()
)
netHTTPPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    netHTTPPort.setStatus("current")
_TrapConfig_ObjectIdentity = ObjectIdentity
trapConfig = _TrapConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 16174, 1, 1, 1, 2, 2)
)
_ManagerConfig_ObjectIdentity = ObjectIdentity
managerConfig = _ManagerConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 16174, 1, 1, 1, 2, 2, 1)
)


class _ManagerIP_Type(DisplayString):
    """Custom type managerIP based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )
    fixed_length = 16


_ManagerIP_Type.__name__ = "DisplayString"
_ManagerIP_Object = MibScalar
managerIP = _ManagerIP_Object(
    (1, 3, 6, 1, 4, 1, 16174, 1, 1, 1, 2, 2, 1, 1),
    _ManagerIP_Type()
)
managerIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    managerIP.setStatus("current")
_MeasurementSystem_ObjectIdentity = ObjectIdentity
measurementSystem = _MeasurementSystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 16174, 1, 1, 1, 2, 3)
)


class _UnitMode_Type(Integer32):
    """Custom type unitMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_UnitMode_Type.__name__ = "Integer32"
_UnitMode_Object = MibScalar
unitMode = _UnitMode_Object(
    (1, 3, 6, 1, 4, 1, 16174, 1, 1, 1, 2, 3, 1),
    _UnitMode_Type()
)
unitMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    unitMode.setStatus("current")
_SensorInfo_ObjectIdentity = ObjectIdentity
sensorInfo = _SensorInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 16174, 1, 1, 1, 3)
)
_Sensor1_ObjectIdentity = ObjectIdentity
sensor1 = _Sensor1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 16174, 1, 1, 1, 3, 1)
)


class _Sensor1Name_Type(DisplayString):
    """Custom type sensor1Name based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )
    fixed_length = 16


_Sensor1Name_Type.__name__ = "DisplayString"
_Sensor1Name_Object = MibScalar
sensor1Name = _Sensor1Name_Object(
    (1, 3, 6, 1, 4, 1, 16174, 1, 1, 1, 3, 1, 1),
    _Sensor1Name_Type()
)
sensor1Name.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sensor1Name.setStatus("current")


class _Sensor1DataStr_Type(DisplayString):
    """Custom type sensor1DataStr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(5, 5),
    )
    fixed_length = 5


_Sensor1DataStr_Type.__name__ = "DisplayString"
_Sensor1DataStr_Object = MibScalar
sensor1DataStr = _Sensor1DataStr_Object(
    (1, 3, 6, 1, 4, 1, 16174, 1, 1, 1, 3, 1, 2),
    _Sensor1DataStr_Type()
)
sensor1DataStr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sensor1DataStr.setStatus("current")


class _Sensor1DataInt_Type(Integer32):
    """Custom type sensor1DataInt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-100, 255),
    )


_Sensor1DataInt_Type.__name__ = "Integer32"
_Sensor1DataInt_Object = MibScalar
sensor1DataInt = _Sensor1DataInt_Object(
    (1, 3, 6, 1, 4, 1, 16174, 1, 1, 1, 3, 1, 3),
    _Sensor1DataInt_Type()
)
sensor1DataInt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sensor1DataInt.setStatus("current")


class _Sensor1SwitchInt_Type(Integer32):
    """Custom type sensor1SwitchInt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Sensor1SwitchInt_Type.__name__ = "Integer32"
_Sensor1SwitchInt_Object = MibScalar
sensor1SwitchInt = _Sensor1SwitchInt_Object(
    (1, 3, 6, 1, 4, 1, 16174, 1, 1, 1, 3, 1, 4),
    _Sensor1SwitchInt_Type()
)
sensor1SwitchInt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sensor1SwitchInt.setStatus("current")


class _Sensor1SwitchStr_Type(DisplayString):
    """Custom type sensor1SwitchStr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )
    fixed_length = 6


_Sensor1SwitchStr_Type.__name__ = "DisplayString"
_Sensor1SwitchStr_Object = MibScalar
sensor1SwitchStr = _Sensor1SwitchStr_Object(
    (1, 3, 6, 1, 4, 1, 16174, 1, 1, 1, 3, 1, 5),
    _Sensor1SwitchStr_Type()
)
sensor1SwitchStr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sensor1SwitchStr.setStatus("current")
_Sensor2_ObjectIdentity = ObjectIdentity
sensor2 = _Sensor2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 16174, 1, 1, 1, 3, 2)
)


class _Sensor2Name_Type(DisplayString):
    """Custom type sensor2Name based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )
    fixed_length = 16


_Sensor2Name_Type.__name__ = "DisplayString"
_Sensor2Name_Object = MibScalar
sensor2Name = _Sensor2Name_Object(
    (1, 3, 6, 1, 4, 1, 16174, 1, 1, 1, 3, 2, 1),
    _Sensor2Name_Type()
)
sensor2Name.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sensor2Name.setStatus("current")


class _Sensor2DataStr_Type(DisplayString):
    """Custom type sensor2DataStr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(5, 5),
    )
    fixed_length = 5


_Sensor2DataStr_Type.__name__ = "DisplayString"
_Sensor2DataStr_Object = MibScalar
sensor2DataStr = _Sensor2DataStr_Object(
    (1, 3, 6, 1, 4, 1, 16174, 1, 1, 1, 3, 2, 2),
    _Sensor2DataStr_Type()
)
sensor2DataStr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sensor2DataStr.setStatus("current")


class _Sensor2DataInt_Type(Integer32):
    """Custom type sensor2DataInt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-100, 255),
    )


_Sensor2DataInt_Type.__name__ = "Integer32"
_Sensor2DataInt_Object = MibScalar
sensor2DataInt = _Sensor2DataInt_Object(
    (1, 3, 6, 1, 4, 1, 16174, 1, 1, 1, 3, 2, 3),
    _Sensor2DataInt_Type()
)
sensor2DataInt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sensor2DataInt.setStatus("current")


class _Sensor2SwitchInt_Type(Integer32):
    """Custom type sensor2SwitchInt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Sensor2SwitchInt_Type.__name__ = "Integer32"
_Sensor2SwitchInt_Object = MibScalar
sensor2SwitchInt = _Sensor2SwitchInt_Object(
    (1, 3, 6, 1, 4, 1, 16174, 1, 1, 1, 3, 2, 4),
    _Sensor2SwitchInt_Type()
)
sensor2SwitchInt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sensor2SwitchInt.setStatus("current")


class _Sensor2SwitchStr_Type(DisplayString):
    """Custom type sensor2SwitchStr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )
    fixed_length = 6


_Sensor2SwitchStr_Type.__name__ = "DisplayString"
_Sensor2SwitchStr_Object = MibScalar
sensor2SwitchStr = _Sensor2SwitchStr_Object(
    (1, 3, 6, 1, 4, 1, 16174, 1, 1, 1, 3, 2, 5),
    _Sensor2SwitchStr_Type()
)
sensor2SwitchStr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sensor2SwitchStr.setStatus("current")
_Sensor3_ObjectIdentity = ObjectIdentity
sensor3 = _Sensor3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 16174, 1, 1, 1, 3, 3)
)


class _Sensor3Name_Type(DisplayString):
    """Custom type sensor3Name based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )
    fixed_length = 16


_Sensor3Name_Type.__name__ = "DisplayString"
_Sensor3Name_Object = MibScalar
sensor3Name = _Sensor3Name_Object(
    (1, 3, 6, 1, 4, 1, 16174, 1, 1, 1, 3, 3, 1),
    _Sensor3Name_Type()
)
sensor3Name.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sensor3Name.setStatus("current")


class _Sensor3DataStr_Type(DisplayString):
    """Custom type sensor3DataStr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(5, 5),
    )
    fixed_length = 5


_Sensor3DataStr_Type.__name__ = "DisplayString"
_Sensor3DataStr_Object = MibScalar
sensor3DataStr = _Sensor3DataStr_Object(
    (1, 3, 6, 1, 4, 1, 16174, 1, 1, 1, 3, 3, 2),
    _Sensor3DataStr_Type()
)
sensor3DataStr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sensor3DataStr.setStatus("current")


class _Sensor3DataInt_Type(Integer32):
    """Custom type sensor3DataInt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-100, 255),
    )


_Sensor3DataInt_Type.__name__ = "Integer32"
_Sensor3DataInt_Object = MibScalar
sensor3DataInt = _Sensor3DataInt_Object(
    (1, 3, 6, 1, 4, 1, 16174, 1, 1, 1, 3, 3, 3),
    _Sensor3DataInt_Type()
)
sensor3DataInt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sensor3DataInt.setStatus("current")


class _Sensor3SwitchInt_Type(Integer32):
    """Custom type sensor3SwitchInt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Sensor3SwitchInt_Type.__name__ = "Integer32"
_Sensor3SwitchInt_Object = MibScalar
sensor3SwitchInt = _Sensor3SwitchInt_Object(
    (1, 3, 6, 1, 4, 1, 16174, 1, 1, 1, 3, 3, 4),
    _Sensor3SwitchInt_Type()
)
sensor3SwitchInt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sensor3SwitchInt.setStatus("current")


class _Sensor3SwitchStr_Type(DisplayString):
    """Custom type sensor3SwitchStr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )
    fixed_length = 6


_Sensor3SwitchStr_Type.__name__ = "DisplayString"
_Sensor3SwitchStr_Object = MibScalar
sensor3SwitchStr = _Sensor3SwitchStr_Object(
    (1, 3, 6, 1, 4, 1, 16174, 1, 1, 1, 3, 3, 5),
    _Sensor3SwitchStr_Type()
)
sensor3SwitchStr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sensor3SwitchStr.setStatus("current")
_Sensor4_ObjectIdentity = ObjectIdentity
sensor4 = _Sensor4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 16174, 1, 1, 1, 3, 4)
)


class _Sensor4Name_Type(DisplayString):
    """Custom type sensor4Name based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )
    fixed_length = 16


_Sensor4Name_Type.__name__ = "DisplayString"
_Sensor4Name_Object = MibScalar
sensor4Name = _Sensor4Name_Object(
    (1, 3, 6, 1, 4, 1, 16174, 1, 1, 1, 3, 4, 1),
    _Sensor4Name_Type()
)
sensor4Name.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sensor4Name.setStatus("current")


class _Sensor4DataStr_Type(DisplayString):
    """Custom type sensor4DataStr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(5, 5),
    )
    fixed_length = 5


_Sensor4DataStr_Type.__name__ = "DisplayString"
_Sensor4DataStr_Object = MibScalar
sensor4DataStr = _Sensor4DataStr_Object(
    (1, 3, 6, 1, 4, 1, 16174, 1, 1, 1, 3, 4, 2),
    _Sensor4DataStr_Type()
)
sensor4DataStr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sensor4DataStr.setStatus("current")


class _Sensor4DataInt_Type(Integer32):
    """Custom type sensor4DataInt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-100, 255),
    )


_Sensor4DataInt_Type.__name__ = "Integer32"
_Sensor4DataInt_Object = MibScalar
sensor4DataInt = _Sensor4DataInt_Object(
    (1, 3, 6, 1, 4, 1, 16174, 1, 1, 1, 3, 4, 3),
    _Sensor4DataInt_Type()
)
sensor4DataInt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sensor4DataInt.setStatus("current")


class _Sensor4SwitchInt_Type(Integer32):
    """Custom type sensor4SwitchInt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Sensor4SwitchInt_Type.__name__ = "Integer32"
_Sensor4SwitchInt_Object = MibScalar
sensor4SwitchInt = _Sensor4SwitchInt_Object(
    (1, 3, 6, 1, 4, 1, 16174, 1, 1, 1, 3, 4, 4),
    _Sensor4SwitchInt_Type()
)
sensor4SwitchInt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sensor4SwitchInt.setStatus("current")


class _Sensor4SwitchStr_Type(DisplayString):
    """Custom type sensor4SwitchStr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )
    fixed_length = 6


_Sensor4SwitchStr_Type.__name__ = "DisplayString"
_Sensor4SwitchStr_Object = MibScalar
sensor4SwitchStr = _Sensor4SwitchStr_Object(
    (1, 3, 6, 1, 4, 1, 16174, 1, 1, 1, 3, 4, 5),
    _Sensor4SwitchStr_Type()
)
sensor4SwitchStr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sensor4SwitchStr.setStatus("current")
_Sensor5_ObjectIdentity = ObjectIdentity
sensor5 = _Sensor5_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 16174, 1, 1, 1, 3, 5)
)


class _Sensor5Name_Type(DisplayString):
    """Custom type sensor5Name based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )
    fixed_length = 16


_Sensor5Name_Type.__name__ = "DisplayString"
_Sensor5Name_Object = MibScalar
sensor5Name = _Sensor5Name_Object(
    (1, 3, 6, 1, 4, 1, 16174, 1, 1, 1, 3, 5, 1),
    _Sensor5Name_Type()
)
sensor5Name.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sensor5Name.setStatus("current")


class _Sensor5DataStr_Type(DisplayString):
    """Custom type sensor5DataStr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(5, 5),
    )
    fixed_length = 5


_Sensor5DataStr_Type.__name__ = "DisplayString"
_Sensor5DataStr_Object = MibScalar
sensor5DataStr = _Sensor5DataStr_Object(
    (1, 3, 6, 1, 4, 1, 16174, 1, 1, 1, 3, 5, 2),
    _Sensor5DataStr_Type()
)
sensor5DataStr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sensor5DataStr.setStatus("current")


class _Sensor5DataInt_Type(Integer32):
    """Custom type sensor5DataInt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-100, 255),
    )


_Sensor5DataInt_Type.__name__ = "Integer32"
_Sensor5DataInt_Object = MibScalar
sensor5DataInt = _Sensor5DataInt_Object(
    (1, 3, 6, 1, 4, 1, 16174, 1, 1, 1, 3, 5, 3),
    _Sensor5DataInt_Type()
)
sensor5DataInt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sensor5DataInt.setStatus("current")


class _Sensor5SwitchInt_Type(Integer32):
    """Custom type sensor5SwitchInt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Sensor5SwitchInt_Type.__name__ = "Integer32"
_Sensor5SwitchInt_Object = MibScalar
sensor5SwitchInt = _Sensor5SwitchInt_Object(
    (1, 3, 6, 1, 4, 1, 16174, 1, 1, 1, 3, 5, 4),
    _Sensor5SwitchInt_Type()
)
sensor5SwitchInt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sensor5SwitchInt.setStatus("current")


class _Sensor5SwitchStr_Type(DisplayString):
    """Custom type sensor5SwitchStr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )
    fixed_length = 6


_Sensor5SwitchStr_Type.__name__ = "DisplayString"
_Sensor5SwitchStr_Object = MibScalar
sensor5SwitchStr = _Sensor5SwitchStr_Object(
    (1, 3, 6, 1, 4, 1, 16174, 1, 1, 1, 3, 5, 5),
    _Sensor5SwitchStr_Type()
)
sensor5SwitchStr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sensor5SwitchStr.setStatus("current")
_Sensor6_ObjectIdentity = ObjectIdentity
sensor6 = _Sensor6_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 16174, 1, 1, 1, 3, 6)
)


class _Sensor6Name_Type(DisplayString):
    """Custom type sensor6Name based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )
    fixed_length = 16


_Sensor6Name_Type.__name__ = "DisplayString"
_Sensor6Name_Object = MibScalar
sensor6Name = _Sensor6Name_Object(
    (1, 3, 6, 1, 4, 1, 16174, 1, 1, 1, 3, 6, 1),
    _Sensor6Name_Type()
)
sensor6Name.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sensor6Name.setStatus("current")


class _Sensor6DataStr_Type(DisplayString):
    """Custom type sensor6DataStr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(5, 5),
    )
    fixed_length = 5


_Sensor6DataStr_Type.__name__ = "DisplayString"
_Sensor6DataStr_Object = MibScalar
sensor6DataStr = _Sensor6DataStr_Object(
    (1, 3, 6, 1, 4, 1, 16174, 1, 1, 1, 3, 6, 2),
    _Sensor6DataStr_Type()
)
sensor6DataStr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sensor6DataStr.setStatus("current")


class _Sensor6DataInt_Type(Integer32):
    """Custom type sensor6DataInt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-100, 255),
    )


_Sensor6DataInt_Type.__name__ = "Integer32"
_Sensor6DataInt_Object = MibScalar
sensor6DataInt = _Sensor6DataInt_Object(
    (1, 3, 6, 1, 4, 1, 16174, 1, 1, 1, 3, 6, 3),
    _Sensor6DataInt_Type()
)
sensor6DataInt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sensor6DataInt.setStatus("current")


class _Sensor6SwitchInt_Type(Integer32):
    """Custom type sensor6SwitchInt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Sensor6SwitchInt_Type.__name__ = "Integer32"
_Sensor6SwitchInt_Object = MibScalar
sensor6SwitchInt = _Sensor6SwitchInt_Object(
    (1, 3, 6, 1, 4, 1, 16174, 1, 1, 1, 3, 6, 4),
    _Sensor6SwitchInt_Type()
)
sensor6SwitchInt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sensor6SwitchInt.setStatus("current")


class _Sensor6SwitchStr_Type(DisplayString):
    """Custom type sensor6SwitchStr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )
    fixed_length = 6


_Sensor6SwitchStr_Type.__name__ = "DisplayString"
_Sensor6SwitchStr_Object = MibScalar
sensor6SwitchStr = _Sensor6SwitchStr_Object(
    (1, 3, 6, 1, 4, 1, 16174, 1, 1, 1, 3, 6, 5),
    _Sensor6SwitchStr_Type()
)
sensor6SwitchStr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sensor6SwitchStr.setStatus("current")
_Sensor7_ObjectIdentity = ObjectIdentity
sensor7 = _Sensor7_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 16174, 1, 1, 1, 3, 7)
)


class _Sensor7Name_Type(DisplayString):
    """Custom type sensor7Name based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )
    fixed_length = 16


_Sensor7Name_Type.__name__ = "DisplayString"
_Sensor7Name_Object = MibScalar
sensor7Name = _Sensor7Name_Object(
    (1, 3, 6, 1, 4, 1, 16174, 1, 1, 1, 3, 7, 1),
    _Sensor7Name_Type()
)
sensor7Name.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sensor7Name.setStatus("current")


class _Sensor7DataStr_Type(DisplayString):
    """Custom type sensor7DataStr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(5, 5),
    )
    fixed_length = 5


_Sensor7DataStr_Type.__name__ = "DisplayString"
_Sensor7DataStr_Object = MibScalar
sensor7DataStr = _Sensor7DataStr_Object(
    (1, 3, 6, 1, 4, 1, 16174, 1, 1, 1, 3, 7, 2),
    _Sensor7DataStr_Type()
)
sensor7DataStr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sensor7DataStr.setStatus("current")


class _Sensor7DataInt_Type(Integer32):
    """Custom type sensor7DataInt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-100, 255),
    )


_Sensor7DataInt_Type.__name__ = "Integer32"
_Sensor7DataInt_Object = MibScalar
sensor7DataInt = _Sensor7DataInt_Object(
    (1, 3, 6, 1, 4, 1, 16174, 1, 1, 1, 3, 7, 3),
    _Sensor7DataInt_Type()
)
sensor7DataInt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sensor7DataInt.setStatus("current")


class _Sensor7SwitchInt_Type(Integer32):
    """Custom type sensor7SwitchInt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Sensor7SwitchInt_Type.__name__ = "Integer32"
_Sensor7SwitchInt_Object = MibScalar
sensor7SwitchInt = _Sensor7SwitchInt_Object(
    (1, 3, 6, 1, 4, 1, 16174, 1, 1, 1, 3, 7, 4),
    _Sensor7SwitchInt_Type()
)
sensor7SwitchInt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sensor7SwitchInt.setStatus("current")


class _Sensor7SwitchStr_Type(DisplayString):
    """Custom type sensor7SwitchStr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )
    fixed_length = 6


_Sensor7SwitchStr_Type.__name__ = "DisplayString"
_Sensor7SwitchStr_Object = MibScalar
sensor7SwitchStr = _Sensor7SwitchStr_Object(
    (1, 3, 6, 1, 4, 1, 16174, 1, 1, 1, 3, 7, 5),
    _Sensor7SwitchStr_Type()
)
sensor7SwitchStr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sensor7SwitchStr.setStatus("current")
_Sensor8_ObjectIdentity = ObjectIdentity
sensor8 = _Sensor8_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 16174, 1, 1, 1, 3, 8)
)


class _Sensor8Name_Type(DisplayString):
    """Custom type sensor8Name based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )
    fixed_length = 16


_Sensor8Name_Type.__name__ = "DisplayString"
_Sensor8Name_Object = MibScalar
sensor8Name = _Sensor8Name_Object(
    (1, 3, 6, 1, 4, 1, 16174, 1, 1, 1, 3, 8, 1),
    _Sensor8Name_Type()
)
sensor8Name.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sensor8Name.setStatus("current")


class _Sensor8DataStr_Type(DisplayString):
    """Custom type sensor8DataStr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(5, 5),
    )
    fixed_length = 5


_Sensor8DataStr_Type.__name__ = "DisplayString"
_Sensor8DataStr_Object = MibScalar
sensor8DataStr = _Sensor8DataStr_Object(
    (1, 3, 6, 1, 4, 1, 16174, 1, 1, 1, 3, 8, 2),
    _Sensor8DataStr_Type()
)
sensor8DataStr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sensor8DataStr.setStatus("current")


class _Sensor8DataInt_Type(Integer32):
    """Custom type sensor8DataInt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-100, 255),
    )


_Sensor8DataInt_Type.__name__ = "Integer32"
_Sensor8DataInt_Object = MibScalar
sensor8DataInt = _Sensor8DataInt_Object(
    (1, 3, 6, 1, 4, 1, 16174, 1, 1, 1, 3, 8, 3),
    _Sensor8DataInt_Type()
)
sensor8DataInt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sensor8DataInt.setStatus("current")


class _Sensor8SwitchInt_Type(Integer32):
    """Custom type sensor8SwitchInt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Sensor8SwitchInt_Type.__name__ = "Integer32"
_Sensor8SwitchInt_Object = MibScalar
sensor8SwitchInt = _Sensor8SwitchInt_Object(
    (1, 3, 6, 1, 4, 1, 16174, 1, 1, 1, 3, 8, 4),
    _Sensor8SwitchInt_Type()
)
sensor8SwitchInt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sensor8SwitchInt.setStatus("current")


class _Sensor8SwitchStr_Type(DisplayString):
    """Custom type sensor8SwitchStr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )
    fixed_length = 6


_Sensor8SwitchStr_Type.__name__ = "DisplayString"
_Sensor8SwitchStr_Object = MibScalar
sensor8SwitchStr = _Sensor8SwitchStr_Object(
    (1, 3, 6, 1, 4, 1, 16174, 1, 1, 1, 3, 8, 5),
    _Sensor8SwitchStr_Type()
)
sensor8SwitchStr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sensor8SwitchStr.setStatus("current")
_Sensor9_ObjectIdentity = ObjectIdentity
sensor9 = _Sensor9_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 16174, 1, 1, 1, 3, 9)
)


class _Sensor9Name_Type(DisplayString):
    """Custom type sensor9Name based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )
    fixed_length = 16


_Sensor9Name_Type.__name__ = "DisplayString"
_Sensor9Name_Object = MibScalar
sensor9Name = _Sensor9Name_Object(
    (1, 3, 6, 1, 4, 1, 16174, 1, 1, 1, 3, 9, 1),
    _Sensor9Name_Type()
)
sensor9Name.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sensor9Name.setStatus("current")


class _Sensor9DataStr_Type(DisplayString):
    """Custom type sensor9DataStr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(5, 5),
    )
    fixed_length = 5


_Sensor9DataStr_Type.__name__ = "DisplayString"
_Sensor9DataStr_Object = MibScalar
sensor9DataStr = _Sensor9DataStr_Object(
    (1, 3, 6, 1, 4, 1, 16174, 1, 1, 1, 3, 9, 2),
    _Sensor9DataStr_Type()
)
sensor9DataStr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sensor9DataStr.setStatus("current")


class _Sensor9DataInt_Type(Integer32):
    """Custom type sensor9DataInt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-100, 255),
    )


_Sensor9DataInt_Type.__name__ = "Integer32"
_Sensor9DataInt_Object = MibScalar
sensor9DataInt = _Sensor9DataInt_Object(
    (1, 3, 6, 1, 4, 1, 16174, 1, 1, 1, 3, 9, 3),
    _Sensor9DataInt_Type()
)
sensor9DataInt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sensor9DataInt.setStatus("current")


class _Sensor9SwitchInt_Type(Integer32):
    """Custom type sensor9SwitchInt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Sensor9SwitchInt_Type.__name__ = "Integer32"
_Sensor9SwitchInt_Object = MibScalar
sensor9SwitchInt = _Sensor9SwitchInt_Object(
    (1, 3, 6, 1, 4, 1, 16174, 1, 1, 1, 3, 9, 4),
    _Sensor9SwitchInt_Type()
)
sensor9SwitchInt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sensor9SwitchInt.setStatus("current")


class _Sensor9SwitchStr_Type(DisplayString):
    """Custom type sensor9SwitchStr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )
    fixed_length = 6


_Sensor9SwitchStr_Type.__name__ = "DisplayString"
_Sensor9SwitchStr_Object = MibScalar
sensor9SwitchStr = _Sensor9SwitchStr_Object(
    (1, 3, 6, 1, 4, 1, 16174, 1, 1, 1, 3, 9, 5),
    _Sensor9SwitchStr_Type()
)
sensor9SwitchStr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sensor9SwitchStr.setStatus("current")
_Sensor10_ObjectIdentity = ObjectIdentity
sensor10 = _Sensor10_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 16174, 1, 1, 1, 3, 10)
)


class _Sensor10Name_Type(DisplayString):
    """Custom type sensor10Name based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )
    fixed_length = 16


_Sensor10Name_Type.__name__ = "DisplayString"
_Sensor10Name_Object = MibScalar
sensor10Name = _Sensor10Name_Object(
    (1, 3, 6, 1, 4, 1, 16174, 1, 1, 1, 3, 10, 1),
    _Sensor10Name_Type()
)
sensor10Name.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sensor10Name.setStatus("current")


class _Sensor10DataStr_Type(DisplayString):
    """Custom type sensor10DataStr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(5, 5),
    )
    fixed_length = 5


_Sensor10DataStr_Type.__name__ = "DisplayString"
_Sensor10DataStr_Object = MibScalar
sensor10DataStr = _Sensor10DataStr_Object(
    (1, 3, 6, 1, 4, 1, 16174, 1, 1, 1, 3, 10, 2),
    _Sensor10DataStr_Type()
)
sensor10DataStr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sensor10DataStr.setStatus("current")


class _Sensor10DataInt_Type(Integer32):
    """Custom type sensor10DataInt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-100, 255),
    )


_Sensor10DataInt_Type.__name__ = "Integer32"
_Sensor10DataInt_Object = MibScalar
sensor10DataInt = _Sensor10DataInt_Object(
    (1, 3, 6, 1, 4, 1, 16174, 1, 1, 1, 3, 10, 3),
    _Sensor10DataInt_Type()
)
sensor10DataInt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sensor10DataInt.setStatus("current")


class _Sensor10SwitchInt_Type(Integer32):
    """Custom type sensor10SwitchInt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Sensor10SwitchInt_Type.__name__ = "Integer32"
_Sensor10SwitchInt_Object = MibScalar
sensor10SwitchInt = _Sensor10SwitchInt_Object(
    (1, 3, 6, 1, 4, 1, 16174, 1, 1, 1, 3, 10, 4),
    _Sensor10SwitchInt_Type()
)
sensor10SwitchInt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sensor10SwitchInt.setStatus("current")


class _Sensor10SwitchStr_Type(DisplayString):
    """Custom type sensor10SwitchStr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )
    fixed_length = 6


_Sensor10SwitchStr_Type.__name__ = "DisplayString"
_Sensor10SwitchStr_Object = MibScalar
sensor10SwitchStr = _Sensor10SwitchStr_Object(
    (1, 3, 6, 1, 4, 1, 16174, 1, 1, 1, 3, 10, 5),
    _Sensor10SwitchStr_Type()
)
sensor10SwitchStr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sensor10SwitchStr.setStatus("current")
_Sensor11_ObjectIdentity = ObjectIdentity
sensor11 = _Sensor11_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 16174, 1, 1, 1, 3, 11)
)


class _Sensor11Name_Type(DisplayString):
    """Custom type sensor11Name based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )
    fixed_length = 16


_Sensor11Name_Type.__name__ = "DisplayString"
_Sensor11Name_Object = MibScalar
sensor11Name = _Sensor11Name_Object(
    (1, 3, 6, 1, 4, 1, 16174, 1, 1, 1, 3, 11, 1),
    _Sensor11Name_Type()
)
sensor11Name.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sensor11Name.setStatus("current")


class _Sensor11DataStr_Type(DisplayString):
    """Custom type sensor11DataStr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(5, 5),
    )
    fixed_length = 5


_Sensor11DataStr_Type.__name__ = "DisplayString"
_Sensor11DataStr_Object = MibScalar
sensor11DataStr = _Sensor11DataStr_Object(
    (1, 3, 6, 1, 4, 1, 16174, 1, 1, 1, 3, 11, 2),
    _Sensor11DataStr_Type()
)
sensor11DataStr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sensor11DataStr.setStatus("current")


class _Sensor11DataInt_Type(Integer32):
    """Custom type sensor11DataInt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-100, 255),
    )


_Sensor11DataInt_Type.__name__ = "Integer32"
_Sensor11DataInt_Object = MibScalar
sensor11DataInt = _Sensor11DataInt_Object(
    (1, 3, 6, 1, 4, 1, 16174, 1, 1, 1, 3, 11, 3),
    _Sensor11DataInt_Type()
)
sensor11DataInt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sensor11DataInt.setStatus("current")


class _Sensor11SwitchInt_Type(Integer32):
    """Custom type sensor11SwitchInt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Sensor11SwitchInt_Type.__name__ = "Integer32"
_Sensor11SwitchInt_Object = MibScalar
sensor11SwitchInt = _Sensor11SwitchInt_Object(
    (1, 3, 6, 1, 4, 1, 16174, 1, 1, 1, 3, 11, 4),
    _Sensor11SwitchInt_Type()
)
sensor11SwitchInt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sensor11SwitchInt.setStatus("current")


class _Sensor11SwitchStr_Type(DisplayString):
    """Custom type sensor11SwitchStr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )
    fixed_length = 6


_Sensor11SwitchStr_Type.__name__ = "DisplayString"
_Sensor11SwitchStr_Object = MibScalar
sensor11SwitchStr = _Sensor11SwitchStr_Object(
    (1, 3, 6, 1, 4, 1, 16174, 1, 1, 1, 3, 11, 5),
    _Sensor11SwitchStr_Type()
)
sensor11SwitchStr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sensor11SwitchStr.setStatus("current")
_Sensor12_ObjectIdentity = ObjectIdentity
sensor12 = _Sensor12_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 16174, 1, 1, 1, 3, 12)
)


class _Sensor12Name_Type(DisplayString):
    """Custom type sensor12Name based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )
    fixed_length = 16


_Sensor12Name_Type.__name__ = "DisplayString"
_Sensor12Name_Object = MibScalar
sensor12Name = _Sensor12Name_Object(
    (1, 3, 6, 1, 4, 1, 16174, 1, 1, 1, 3, 12, 1),
    _Sensor12Name_Type()
)
sensor12Name.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sensor12Name.setStatus("current")


class _Sensor12DataStr_Type(DisplayString):
    """Custom type sensor12DataStr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(5, 5),
    )
    fixed_length = 5


_Sensor12DataStr_Type.__name__ = "DisplayString"
_Sensor12DataStr_Object = MibScalar
sensor12DataStr = _Sensor12DataStr_Object(
    (1, 3, 6, 1, 4, 1, 16174, 1, 1, 1, 3, 12, 2),
    _Sensor12DataStr_Type()
)
sensor12DataStr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sensor12DataStr.setStatus("current")


class _Sensor12DataInt_Type(Integer32):
    """Custom type sensor12DataInt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-100, 255),
    )


_Sensor12DataInt_Type.__name__ = "Integer32"
_Sensor12DataInt_Object = MibScalar
sensor12DataInt = _Sensor12DataInt_Object(
    (1, 3, 6, 1, 4, 1, 16174, 1, 1, 1, 3, 12, 3),
    _Sensor12DataInt_Type()
)
sensor12DataInt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sensor12DataInt.setStatus("current")


class _Sensor12SwitchInt_Type(Integer32):
    """Custom type sensor12SwitchInt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Sensor12SwitchInt_Type.__name__ = "Integer32"
_Sensor12SwitchInt_Object = MibScalar
sensor12SwitchInt = _Sensor12SwitchInt_Object(
    (1, 3, 6, 1, 4, 1, 16174, 1, 1, 1, 3, 12, 4),
    _Sensor12SwitchInt_Type()
)
sensor12SwitchInt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sensor12SwitchInt.setStatus("current")


class _Sensor12SwitchStr_Type(DisplayString):
    """Custom type sensor12SwitchStr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )
    fixed_length = 6


_Sensor12SwitchStr_Type.__name__ = "DisplayString"
_Sensor12SwitchStr_Object = MibScalar
sensor12SwitchStr = _Sensor12SwitchStr_Object(
    (1, 3, 6, 1, 4, 1, 16174, 1, 1, 1, 3, 12, 5),
    _Sensor12SwitchStr_Type()
)
sensor12SwitchStr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sensor12SwitchStr.setStatus("current")
_Sensor13_ObjectIdentity = ObjectIdentity
sensor13 = _Sensor13_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 16174, 1, 1, 1, 3, 13)
)


class _Sensor13Name_Type(DisplayString):
    """Custom type sensor13Name based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )
    fixed_length = 16


_Sensor13Name_Type.__name__ = "DisplayString"
_Sensor13Name_Object = MibScalar
sensor13Name = _Sensor13Name_Object(
    (1, 3, 6, 1, 4, 1, 16174, 1, 1, 1, 3, 13, 1),
    _Sensor13Name_Type()
)
sensor13Name.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sensor13Name.setStatus("current")


class _Sensor13DataStr_Type(DisplayString):
    """Custom type sensor13DataStr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(5, 5),
    )
    fixed_length = 5


_Sensor13DataStr_Type.__name__ = "DisplayString"
_Sensor13DataStr_Object = MibScalar
sensor13DataStr = _Sensor13DataStr_Object(
    (1, 3, 6, 1, 4, 1, 16174, 1, 1, 1, 3, 13, 2),
    _Sensor13DataStr_Type()
)
sensor13DataStr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sensor13DataStr.setStatus("current")


class _Sensor13DataInt_Type(Integer32):
    """Custom type sensor13DataInt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-100, 255),
    )


_Sensor13DataInt_Type.__name__ = "Integer32"
_Sensor13DataInt_Object = MibScalar
sensor13DataInt = _Sensor13DataInt_Object(
    (1, 3, 6, 1, 4, 1, 16174, 1, 1, 1, 3, 13, 3),
    _Sensor13DataInt_Type()
)
sensor13DataInt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sensor13DataInt.setStatus("current")


class _Sensor13SwitchInt_Type(Integer32):
    """Custom type sensor13SwitchInt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Sensor13SwitchInt_Type.__name__ = "Integer32"
_Sensor13SwitchInt_Object = MibScalar
sensor13SwitchInt = _Sensor13SwitchInt_Object(
    (1, 3, 6, 1, 4, 1, 16174, 1, 1, 1, 3, 13, 4),
    _Sensor13SwitchInt_Type()
)
sensor13SwitchInt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sensor13SwitchInt.setStatus("current")


class _Sensor13SwitchStr_Type(DisplayString):
    """Custom type sensor13SwitchStr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )
    fixed_length = 6


_Sensor13SwitchStr_Type.__name__ = "DisplayString"
_Sensor13SwitchStr_Object = MibScalar
sensor13SwitchStr = _Sensor13SwitchStr_Object(
    (1, 3, 6, 1, 4, 1, 16174, 1, 1, 1, 3, 13, 5),
    _Sensor13SwitchStr_Type()
)
sensor13SwitchStr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sensor13SwitchStr.setStatus("current")
_Sensor14_ObjectIdentity = ObjectIdentity
sensor14 = _Sensor14_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 16174, 1, 1, 1, 3, 14)
)


class _Sensor14Name_Type(DisplayString):
    """Custom type sensor14Name based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )
    fixed_length = 16


_Sensor14Name_Type.__name__ = "DisplayString"
_Sensor14Name_Object = MibScalar
sensor14Name = _Sensor14Name_Object(
    (1, 3, 6, 1, 4, 1, 16174, 1, 1, 1, 3, 14, 1),
    _Sensor14Name_Type()
)
sensor14Name.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sensor14Name.setStatus("current")


class _Sensor14DataStr_Type(DisplayString):
    """Custom type sensor14DataStr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(5, 5),
    )
    fixed_length = 5


_Sensor14DataStr_Type.__name__ = "DisplayString"
_Sensor14DataStr_Object = MibScalar
sensor14DataStr = _Sensor14DataStr_Object(
    (1, 3, 6, 1, 4, 1, 16174, 1, 1, 1, 3, 14, 2),
    _Sensor14DataStr_Type()
)
sensor14DataStr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sensor14DataStr.setStatus("current")


class _Sensor14DataInt_Type(Integer32):
    """Custom type sensor14DataInt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-100, 255),
    )


_Sensor14DataInt_Type.__name__ = "Integer32"
_Sensor14DataInt_Object = MibScalar
sensor14DataInt = _Sensor14DataInt_Object(
    (1, 3, 6, 1, 4, 1, 16174, 1, 1, 1, 3, 14, 3),
    _Sensor14DataInt_Type()
)
sensor14DataInt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sensor14DataInt.setStatus("current")


class _Sensor14SwitchInt_Type(Integer32):
    """Custom type sensor14SwitchInt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Sensor14SwitchInt_Type.__name__ = "Integer32"
_Sensor14SwitchInt_Object = MibScalar
sensor14SwitchInt = _Sensor14SwitchInt_Object(
    (1, 3, 6, 1, 4, 1, 16174, 1, 1, 1, 3, 14, 4),
    _Sensor14SwitchInt_Type()
)
sensor14SwitchInt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sensor14SwitchInt.setStatus("current")


class _Sensor14SwitchStr_Type(DisplayString):
    """Custom type sensor14SwitchStr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )
    fixed_length = 6


_Sensor14SwitchStr_Type.__name__ = "DisplayString"
_Sensor14SwitchStr_Object = MibScalar
sensor14SwitchStr = _Sensor14SwitchStr_Object(
    (1, 3, 6, 1, 4, 1, 16174, 1, 1, 1, 3, 14, 5),
    _Sensor14SwitchStr_Type()
)
sensor14SwitchStr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sensor14SwitchStr.setStatus("current")
_Sensor15_ObjectIdentity = ObjectIdentity
sensor15 = _Sensor15_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 16174, 1, 1, 1, 3, 15)
)


class _Sensor15Name_Type(DisplayString):
    """Custom type sensor15Name based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )
    fixed_length = 16


_Sensor15Name_Type.__name__ = "DisplayString"
_Sensor15Name_Object = MibScalar
sensor15Name = _Sensor15Name_Object(
    (1, 3, 6, 1, 4, 1, 16174, 1, 1, 1, 3, 15, 1),
    _Sensor15Name_Type()
)
sensor15Name.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sensor15Name.setStatus("current")


class _Sensor15DataStr_Type(DisplayString):
    """Custom type sensor15DataStr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(5, 5),
    )
    fixed_length = 5


_Sensor15DataStr_Type.__name__ = "DisplayString"
_Sensor15DataStr_Object = MibScalar
sensor15DataStr = _Sensor15DataStr_Object(
    (1, 3, 6, 1, 4, 1, 16174, 1, 1, 1, 3, 15, 2),
    _Sensor15DataStr_Type()
)
sensor15DataStr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sensor15DataStr.setStatus("current")


class _Sensor15DataInt_Type(Integer32):
    """Custom type sensor15DataInt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-100, 255),
    )


_Sensor15DataInt_Type.__name__ = "Integer32"
_Sensor15DataInt_Object = MibScalar
sensor15DataInt = _Sensor15DataInt_Object(
    (1, 3, 6, 1, 4, 1, 16174, 1, 1, 1, 3, 15, 3),
    _Sensor15DataInt_Type()
)
sensor15DataInt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sensor15DataInt.setStatus("current")


class _Sensor15SwitchInt_Type(Integer32):
    """Custom type sensor15SwitchInt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Sensor15SwitchInt_Type.__name__ = "Integer32"
_Sensor15SwitchInt_Object = MibScalar
sensor15SwitchInt = _Sensor15SwitchInt_Object(
    (1, 3, 6, 1, 4, 1, 16174, 1, 1, 1, 3, 15, 4),
    _Sensor15SwitchInt_Type()
)
sensor15SwitchInt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sensor15SwitchInt.setStatus("current")


class _Sensor15SwitchStr_Type(DisplayString):
    """Custom type sensor15SwitchStr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )
    fixed_length = 6


_Sensor15SwitchStr_Type.__name__ = "DisplayString"
_Sensor15SwitchStr_Object = MibScalar
sensor15SwitchStr = _Sensor15SwitchStr_Object(
    (1, 3, 6, 1, 4, 1, 16174, 1, 1, 1, 3, 15, 5),
    _Sensor15SwitchStr_Type()
)
sensor15SwitchStr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sensor15SwitchStr.setStatus("current")
_Sensor16_ObjectIdentity = ObjectIdentity
sensor16 = _Sensor16_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 16174, 1, 1, 1, 3, 16)
)


class _Sensor16Name_Type(DisplayString):
    """Custom type sensor16Name based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )
    fixed_length = 16


_Sensor16Name_Type.__name__ = "DisplayString"
_Sensor16Name_Object = MibScalar
sensor16Name = _Sensor16Name_Object(
    (1, 3, 6, 1, 4, 1, 16174, 1, 1, 1, 3, 16, 1),
    _Sensor16Name_Type()
)
sensor16Name.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sensor16Name.setStatus("current")


class _Sensor16DataStr_Type(DisplayString):
    """Custom type sensor16DataStr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(5, 5),
    )
    fixed_length = 5


_Sensor16DataStr_Type.__name__ = "DisplayString"
_Sensor16DataStr_Object = MibScalar
sensor16DataStr = _Sensor16DataStr_Object(
    (1, 3, 6, 1, 4, 1, 16174, 1, 1, 1, 3, 16, 2),
    _Sensor16DataStr_Type()
)
sensor16DataStr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sensor16DataStr.setStatus("current")


class _Sensor16DataInt_Type(Integer32):
    """Custom type sensor16DataInt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-100, 255),
    )


_Sensor16DataInt_Type.__name__ = "Integer32"
_Sensor16DataInt_Object = MibScalar
sensor16DataInt = _Sensor16DataInt_Object(
    (1, 3, 6, 1, 4, 1, 16174, 1, 1, 1, 3, 16, 3),
    _Sensor16DataInt_Type()
)
sensor16DataInt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sensor16DataInt.setStatus("current")


class _Sensor16SwitchInt_Type(Integer32):
    """Custom type sensor16SwitchInt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Sensor16SwitchInt_Type.__name__ = "Integer32"
_Sensor16SwitchInt_Object = MibScalar
sensor16SwitchInt = _Sensor16SwitchInt_Object(
    (1, 3, 6, 1, 4, 1, 16174, 1, 1, 1, 3, 16, 4),
    _Sensor16SwitchInt_Type()
)
sensor16SwitchInt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sensor16SwitchInt.setStatus("current")


class _Sensor16SwitchStr_Type(DisplayString):
    """Custom type sensor16SwitchStr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )
    fixed_length = 6


_Sensor16SwitchStr_Type.__name__ = "DisplayString"
_Sensor16SwitchStr_Object = MibScalar
sensor16SwitchStr = _Sensor16SwitchStr_Object(
    (1, 3, 6, 1, 4, 1, 16174, 1, 1, 1, 3, 16, 5),
    _Sensor16SwitchStr_Type()
)
sensor16SwitchStr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sensor16SwitchStr.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SENSATRONICS-ITTM",
    **{"productITTM": productITTM,
       "unitInfo": unitInfo,
       "unitName": unitName,
       "unitModel": unitModel,
       "unitManufacturer": unitManufacturer,
       "unitWeb": unitWeb,
       "unitFirmware": unitFirmware,
       "unitFWReleaseDate": unitFWReleaseDate,
       "unitSerial": unitSerial,
       "unitConfig": unitConfig,
       "configData": configData,
       "netInfo": netInfo,
       "netMode": netMode,
       "netIP": netIP,
       "netNM": netNM,
       "netGW": netGW,
       "netHTTPPort": netHTTPPort,
       "trapConfig": trapConfig,
       "managerConfig": managerConfig,
       "managerIP": managerIP,
       "measurementSystem": measurementSystem,
       "unitMode": unitMode,
       "sensorInfo": sensorInfo,
       "sensor1": sensor1,
       "sensor1Name": sensor1Name,
       "sensor1DataStr": sensor1DataStr,
       "sensor1DataInt": sensor1DataInt,
       "sensor1SwitchInt": sensor1SwitchInt,
       "sensor1SwitchStr": sensor1SwitchStr,
       "sensor2": sensor2,
       "sensor2Name": sensor2Name,
       "sensor2DataStr": sensor2DataStr,
       "sensor2DataInt": sensor2DataInt,
       "sensor2SwitchInt": sensor2SwitchInt,
       "sensor2SwitchStr": sensor2SwitchStr,
       "sensor3": sensor3,
       "sensor3Name": sensor3Name,
       "sensor3DataStr": sensor3DataStr,
       "sensor3DataInt": sensor3DataInt,
       "sensor3SwitchInt": sensor3SwitchInt,
       "sensor3SwitchStr": sensor3SwitchStr,
       "sensor4": sensor4,
       "sensor4Name": sensor4Name,
       "sensor4DataStr": sensor4DataStr,
       "sensor4DataInt": sensor4DataInt,
       "sensor4SwitchInt": sensor4SwitchInt,
       "sensor4SwitchStr": sensor4SwitchStr,
       "sensor5": sensor5,
       "sensor5Name": sensor5Name,
       "sensor5DataStr": sensor5DataStr,
       "sensor5DataInt": sensor5DataInt,
       "sensor5SwitchInt": sensor5SwitchInt,
       "sensor5SwitchStr": sensor5SwitchStr,
       "sensor6": sensor6,
       "sensor6Name": sensor6Name,
       "sensor6DataStr": sensor6DataStr,
       "sensor6DataInt": sensor6DataInt,
       "sensor6SwitchInt": sensor6SwitchInt,
       "sensor6SwitchStr": sensor6SwitchStr,
       "sensor7": sensor7,
       "sensor7Name": sensor7Name,
       "sensor7DataStr": sensor7DataStr,
       "sensor7DataInt": sensor7DataInt,
       "sensor7SwitchInt": sensor7SwitchInt,
       "sensor7SwitchStr": sensor7SwitchStr,
       "sensor8": sensor8,
       "sensor8Name": sensor8Name,
       "sensor8DataStr": sensor8DataStr,
       "sensor8DataInt": sensor8DataInt,
       "sensor8SwitchInt": sensor8SwitchInt,
       "sensor8SwitchStr": sensor8SwitchStr,
       "sensor9": sensor9,
       "sensor9Name": sensor9Name,
       "sensor9DataStr": sensor9DataStr,
       "sensor9DataInt": sensor9DataInt,
       "sensor9SwitchInt": sensor9SwitchInt,
       "sensor9SwitchStr": sensor9SwitchStr,
       "sensor10": sensor10,
       "sensor10Name": sensor10Name,
       "sensor10DataStr": sensor10DataStr,
       "sensor10DataInt": sensor10DataInt,
       "sensor10SwitchInt": sensor10SwitchInt,
       "sensor10SwitchStr": sensor10SwitchStr,
       "sensor11": sensor11,
       "sensor11Name": sensor11Name,
       "sensor11DataStr": sensor11DataStr,
       "sensor11DataInt": sensor11DataInt,
       "sensor11SwitchInt": sensor11SwitchInt,
       "sensor11SwitchStr": sensor11SwitchStr,
       "sensor12": sensor12,
       "sensor12Name": sensor12Name,
       "sensor12DataStr": sensor12DataStr,
       "sensor12DataInt": sensor12DataInt,
       "sensor12SwitchInt": sensor12SwitchInt,
       "sensor12SwitchStr": sensor12SwitchStr,
       "sensor13": sensor13,
       "sensor13Name": sensor13Name,
       "sensor13DataStr": sensor13DataStr,
       "sensor13DataInt": sensor13DataInt,
       "sensor13SwitchInt": sensor13SwitchInt,
       "sensor13SwitchStr": sensor13SwitchStr,
       "sensor14": sensor14,
       "sensor14Name": sensor14Name,
       "sensor14DataStr": sensor14DataStr,
       "sensor14DataInt": sensor14DataInt,
       "sensor14SwitchInt": sensor14SwitchInt,
       "sensor14SwitchStr": sensor14SwitchStr,
       "sensor15": sensor15,
       "sensor15Name": sensor15Name,
       "sensor15DataStr": sensor15DataStr,
       "sensor15DataInt": sensor15DataInt,
       "sensor15SwitchInt": sensor15SwitchInt,
       "sensor15SwitchStr": sensor15SwitchStr,
       "sensor16": sensor16,
       "sensor16Name": sensor16Name,
       "sensor16DataStr": sensor16DataStr,
       "sensor16DataInt": sensor16DataInt,
       "sensor16SwitchInt": sensor16SwitchInt,
       "sensor16SwitchStr": sensor16SwitchStr}
)
