# SNMP MIB module (SENSATRONICS-EM1) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\sensatronics\SENSATRONICS-EM1

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

productEM1 = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 16174, 1, 1, 3)
)
if mibBuilder.loadTexts:
    productEM1.setRevisions(
        ("2004-09-21 09:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_UnitInfo_ObjectIdentity = ObjectIdentity
unitInfo = _UnitInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 16174, 1, 1, 3, 1)
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
    (1, 3, 6, 1, 4, 1, 16174, 1, 1, 3, 1, 1),
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
    (1, 3, 6, 1, 4, 1, 16174, 1, 1, 3, 1, 2),
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
    (1, 3, 6, 1, 4, 1, 16174, 1, 1, 3, 1, 3),
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
    (1, 3, 6, 1, 4, 1, 16174, 1, 1, 3, 1, 4),
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
    (1, 3, 6, 1, 4, 1, 16174, 1, 1, 3, 1, 5),
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
    (1, 3, 6, 1, 4, 1, 16174, 1, 1, 3, 1, 6),
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
    (1, 3, 6, 1, 4, 1, 16174, 1, 1, 3, 1, 7),
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
    (1, 3, 6, 1, 4, 1, 16174, 1, 1, 3, 1, 8),
    _UnitConfig_Type()
)
unitConfig.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    unitConfig.setStatus("current")
_ConfigData_ObjectIdentity = ObjectIdentity
configData = _ConfigData_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 16174, 1, 1, 3, 2)
)
_NetInfo_ObjectIdentity = ObjectIdentity
netInfo = _NetInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 16174, 1, 1, 3, 2, 1)
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
    (1, 3, 6, 1, 4, 1, 16174, 1, 1, 3, 2, 1, 1),
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
    (1, 3, 6, 1, 4, 1, 16174, 1, 1, 3, 2, 1, 2),
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
    (1, 3, 6, 1, 4, 1, 16174, 1, 1, 3, 2, 1, 3),
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
    (1, 3, 6, 1, 4, 1, 16174, 1, 1, 3, 2, 1, 4),
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
    (1, 3, 6, 1, 4, 1, 16174, 1, 1, 3, 2, 1, 5),
    _NetHTTPPort_Type()
)
netHTTPPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    netHTTPPort.setStatus("current")
_TrapConfig_ObjectIdentity = ObjectIdentity
trapConfig = _TrapConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 16174, 1, 1, 3, 2, 2)
)
_ManagerConfig_ObjectIdentity = ObjectIdentity
managerConfig = _ManagerConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 16174, 1, 1, 3, 2, 2, 1)
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
    (1, 3, 6, 1, 4, 1, 16174, 1, 1, 3, 2, 2, 1, 1),
    _ManagerIP_Type()
)
managerIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    managerIP.setStatus("current")
_MeasurementSystem_ObjectIdentity = ObjectIdentity
measurementSystem = _MeasurementSystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 16174, 1, 1, 3, 2, 3)
)


class _UnitMode_Type(DisplayString):
    """Custom type unitMode based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )
    fixed_length = 2


_UnitMode_Type.__name__ = "DisplayString"
_UnitMode_Object = MibScalar
unitMode = _UnitMode_Object(
    (1, 3, 6, 1, 4, 1, 16174, 1, 1, 3, 2, 3, 1),
    _UnitMode_Type()
)
unitMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    unitMode.setStatus("current")
_SensorInfo_ObjectIdentity = ObjectIdentity
sensorInfo = _SensorInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 16174, 1, 1, 3, 3)
)
_Group1_ObjectIdentity = ObjectIdentity
group1 = _Group1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 16174, 1, 1, 3, 3, 1)
)


class _Group1Name_Type(DisplayString):
    """Custom type group1Name based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )
    fixed_length = 16


_Group1Name_Type.__name__ = "DisplayString"
_Group1Name_Object = MibScalar
group1Name = _Group1Name_Object(
    (1, 3, 6, 1, 4, 1, 16174, 1, 1, 3, 3, 1, 1),
    _Group1Name_Type()
)
group1Name.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    group1Name.setStatus("current")


class _Group1TempName_Type(DisplayString):
    """Custom type group1TempName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )
    fixed_length = 16


_Group1TempName_Type.__name__ = "DisplayString"
_Group1TempName_Object = MibScalar
group1TempName = _Group1TempName_Object(
    (1, 3, 6, 1, 4, 1, 16174, 1, 1, 3, 3, 1, 2),
    _Group1TempName_Type()
)
group1TempName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    group1TempName.setStatus("current")


class _Group1TempDataStr_Type(DisplayString):
    """Custom type group1TempDataStr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(5, 5),
    )
    fixed_length = 5


_Group1TempDataStr_Type.__name__ = "DisplayString"
_Group1TempDataStr_Object = MibScalar
group1TempDataStr = _Group1TempDataStr_Object(
    (1, 3, 6, 1, 4, 1, 16174, 1, 1, 3, 3, 1, 3),
    _Group1TempDataStr_Type()
)
group1TempDataStr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    group1TempDataStr.setStatus("current")


class _Group1TempDataInt_Type(Integer32):
    """Custom type group1TempDataInt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1000, 10000),
    )


_Group1TempDataInt_Type.__name__ = "Integer32"
_Group1TempDataInt_Object = MibScalar
group1TempDataInt = _Group1TempDataInt_Object(
    (1, 3, 6, 1, 4, 1, 16174, 1, 1, 3, 3, 1, 4),
    _Group1TempDataInt_Type()
)
group1TempDataInt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    group1TempDataInt.setStatus("current")


class _Group1HumidName_Type(DisplayString):
    """Custom type group1HumidName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )
    fixed_length = 16


_Group1HumidName_Type.__name__ = "DisplayString"
_Group1HumidName_Object = MibScalar
group1HumidName = _Group1HumidName_Object(
    (1, 3, 6, 1, 4, 1, 16174, 1, 1, 3, 3, 1, 5),
    _Group1HumidName_Type()
)
group1HumidName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    group1HumidName.setStatus("current")


class _Group1HumidDataStr_Type(DisplayString):
    """Custom type group1HumidDataStr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(5, 5),
    )
    fixed_length = 5


_Group1HumidDataStr_Type.__name__ = "DisplayString"
_Group1HumidDataStr_Object = MibScalar
group1HumidDataStr = _Group1HumidDataStr_Object(
    (1, 3, 6, 1, 4, 1, 16174, 1, 1, 3, 3, 1, 6),
    _Group1HumidDataStr_Type()
)
group1HumidDataStr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    group1HumidDataStr.setStatus("current")


class _Group1HumidDataInt_Type(Integer32):
    """Custom type group1HumidDataInt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_Group1HumidDataInt_Type.__name__ = "Integer32"
_Group1HumidDataInt_Object = MibScalar
group1HumidDataInt = _Group1HumidDataInt_Object(
    (1, 3, 6, 1, 4, 1, 16174, 1, 1, 3, 3, 1, 7),
    _Group1HumidDataInt_Type()
)
group1HumidDataInt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    group1HumidDataInt.setStatus("current")


class _Group1WetName_Type(DisplayString):
    """Custom type group1WetName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )
    fixed_length = 16


_Group1WetName_Type.__name__ = "DisplayString"
_Group1WetName_Object = MibScalar
group1WetName = _Group1WetName_Object(
    (1, 3, 6, 1, 4, 1, 16174, 1, 1, 3, 3, 1, 8),
    _Group1WetName_Type()
)
group1WetName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    group1WetName.setStatus("current")


class _Group1WetDataStr_Type(DisplayString):
    """Custom type group1WetDataStr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(5, 5),
    )
    fixed_length = 5


_Group1WetDataStr_Type.__name__ = "DisplayString"
_Group1WetDataStr_Object = MibScalar
group1WetDataStr = _Group1WetDataStr_Object(
    (1, 3, 6, 1, 4, 1, 16174, 1, 1, 3, 3, 1, 9),
    _Group1WetDataStr_Type()
)
group1WetDataStr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    group1WetDataStr.setStatus("current")


class _Group1WetDataInt_Type(Integer32):
    """Custom type group1WetDataInt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 110),
    )


_Group1WetDataInt_Type.__name__ = "Integer32"
_Group1WetDataInt_Object = MibScalar
group1WetDataInt = _Group1WetDataInt_Object(
    (1, 3, 6, 1, 4, 1, 16174, 1, 1, 3, 3, 1, 10),
    _Group1WetDataInt_Type()
)
group1WetDataInt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    group1WetDataInt.setStatus("current")
_Group2_ObjectIdentity = ObjectIdentity
group2 = _Group2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 16174, 1, 1, 3, 3, 2)
)


class _Group2Name_Type(DisplayString):
    """Custom type group2Name based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )
    fixed_length = 16


_Group2Name_Type.__name__ = "DisplayString"
_Group2Name_Object = MibScalar
group2Name = _Group2Name_Object(
    (1, 3, 6, 1, 4, 1, 16174, 1, 1, 3, 3, 2, 1),
    _Group2Name_Type()
)
group2Name.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    group2Name.setStatus("current")


class _Group2TempName_Type(DisplayString):
    """Custom type group2TempName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )
    fixed_length = 16


_Group2TempName_Type.__name__ = "DisplayString"
_Group2TempName_Object = MibScalar
group2TempName = _Group2TempName_Object(
    (1, 3, 6, 1, 4, 1, 16174, 1, 1, 3, 3, 2, 2),
    _Group2TempName_Type()
)
group2TempName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    group2TempName.setStatus("current")


class _Group2TempDataStr_Type(DisplayString):
    """Custom type group2TempDataStr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(5, 5),
    )
    fixed_length = 5


_Group2TempDataStr_Type.__name__ = "DisplayString"
_Group2TempDataStr_Object = MibScalar
group2TempDataStr = _Group2TempDataStr_Object(
    (1, 3, 6, 1, 4, 1, 16174, 1, 1, 3, 3, 2, 3),
    _Group2TempDataStr_Type()
)
group2TempDataStr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    group2TempDataStr.setStatus("current")


class _Group2TempDataInt_Type(Integer32):
    """Custom type group2TempDataInt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1000, 10000),
    )


_Group2TempDataInt_Type.__name__ = "Integer32"
_Group2TempDataInt_Object = MibScalar
group2TempDataInt = _Group2TempDataInt_Object(
    (1, 3, 6, 1, 4, 1, 16174, 1, 1, 3, 3, 2, 4),
    _Group2TempDataInt_Type()
)
group2TempDataInt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    group2TempDataInt.setStatus("current")


class _Group2HumidName_Type(DisplayString):
    """Custom type group2HumidName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )
    fixed_length = 16


_Group2HumidName_Type.__name__ = "DisplayString"
_Group2HumidName_Object = MibScalar
group2HumidName = _Group2HumidName_Object(
    (1, 3, 6, 1, 4, 1, 16174, 1, 1, 3, 3, 2, 5),
    _Group2HumidName_Type()
)
group2HumidName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    group2HumidName.setStatus("current")


class _Group2HumidDataStr_Type(DisplayString):
    """Custom type group2HumidDataStr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(5, 5),
    )
    fixed_length = 5


_Group2HumidDataStr_Type.__name__ = "DisplayString"
_Group2HumidDataStr_Object = MibScalar
group2HumidDataStr = _Group2HumidDataStr_Object(
    (1, 3, 6, 1, 4, 1, 16174, 1, 1, 3, 3, 2, 6),
    _Group2HumidDataStr_Type()
)
group2HumidDataStr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    group2HumidDataStr.setStatus("current")


class _Group2HumidDataInt_Type(Integer32):
    """Custom type group2HumidDataInt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_Group2HumidDataInt_Type.__name__ = "Integer32"
_Group2HumidDataInt_Object = MibScalar
group2HumidDataInt = _Group2HumidDataInt_Object(
    (1, 3, 6, 1, 4, 1, 16174, 1, 1, 3, 3, 2, 7),
    _Group2HumidDataInt_Type()
)
group2HumidDataInt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    group2HumidDataInt.setStatus("current")


class _Group2WetName_Type(DisplayString):
    """Custom type group2WetName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )
    fixed_length = 16


_Group2WetName_Type.__name__ = "DisplayString"
_Group2WetName_Object = MibScalar
group2WetName = _Group2WetName_Object(
    (1, 3, 6, 1, 4, 1, 16174, 1, 1, 3, 3, 2, 8),
    _Group2WetName_Type()
)
group2WetName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    group2WetName.setStatus("current")


class _Group2WetDataStr_Type(DisplayString):
    """Custom type group2WetDataStr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(5, 5),
    )
    fixed_length = 5


_Group2WetDataStr_Type.__name__ = "DisplayString"
_Group2WetDataStr_Object = MibScalar
group2WetDataStr = _Group2WetDataStr_Object(
    (1, 3, 6, 1, 4, 1, 16174, 1, 1, 3, 3, 2, 9),
    _Group2WetDataStr_Type()
)
group2WetDataStr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    group2WetDataStr.setStatus("current")


class _Group2WetDataInt_Type(Integer32):
    """Custom type group2WetDataInt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 110),
    )


_Group2WetDataInt_Type.__name__ = "Integer32"
_Group2WetDataInt_Object = MibScalar
group2WetDataInt = _Group2WetDataInt_Object(
    (1, 3, 6, 1, 4, 1, 16174, 1, 1, 3, 3, 2, 10),
    _Group2WetDataInt_Type()
)
group2WetDataInt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    group2WetDataInt.setStatus("current")
_Group3_ObjectIdentity = ObjectIdentity
group3 = _Group3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 16174, 1, 1, 3, 3, 3)
)


class _Group3Name_Type(DisplayString):
    """Custom type group3Name based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )
    fixed_length = 16


_Group3Name_Type.__name__ = "DisplayString"
_Group3Name_Object = MibScalar
group3Name = _Group3Name_Object(
    (1, 3, 6, 1, 4, 1, 16174, 1, 1, 3, 3, 3, 1),
    _Group3Name_Type()
)
group3Name.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    group3Name.setStatus("current")


class _Group3TempName_Type(DisplayString):
    """Custom type group3TempName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )
    fixed_length = 16


_Group3TempName_Type.__name__ = "DisplayString"
_Group3TempName_Object = MibScalar
group3TempName = _Group3TempName_Object(
    (1, 3, 6, 1, 4, 1, 16174, 1, 1, 3, 3, 3, 2),
    _Group3TempName_Type()
)
group3TempName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    group3TempName.setStatus("current")


class _Group3TempDataStr_Type(DisplayString):
    """Custom type group3TempDataStr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(5, 5),
    )
    fixed_length = 5


_Group3TempDataStr_Type.__name__ = "DisplayString"
_Group3TempDataStr_Object = MibScalar
group3TempDataStr = _Group3TempDataStr_Object(
    (1, 3, 6, 1, 4, 1, 16174, 1, 1, 3, 3, 3, 3),
    _Group3TempDataStr_Type()
)
group3TempDataStr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    group3TempDataStr.setStatus("current")


class _Group3TempDataInt_Type(Integer32):
    """Custom type group3TempDataInt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1000, 10000),
    )


_Group3TempDataInt_Type.__name__ = "Integer32"
_Group3TempDataInt_Object = MibScalar
group3TempDataInt = _Group3TempDataInt_Object(
    (1, 3, 6, 1, 4, 1, 16174, 1, 1, 3, 3, 3, 4),
    _Group3TempDataInt_Type()
)
group3TempDataInt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    group3TempDataInt.setStatus("current")


class _Group3HumidName_Type(DisplayString):
    """Custom type group3HumidName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )
    fixed_length = 16


_Group3HumidName_Type.__name__ = "DisplayString"
_Group3HumidName_Object = MibScalar
group3HumidName = _Group3HumidName_Object(
    (1, 3, 6, 1, 4, 1, 16174, 1, 1, 3, 3, 3, 5),
    _Group3HumidName_Type()
)
group3HumidName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    group3HumidName.setStatus("current")


class _Group3HumidDataStr_Type(DisplayString):
    """Custom type group3HumidDataStr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(5, 5),
    )
    fixed_length = 5


_Group3HumidDataStr_Type.__name__ = "DisplayString"
_Group3HumidDataStr_Object = MibScalar
group3HumidDataStr = _Group3HumidDataStr_Object(
    (1, 3, 6, 1, 4, 1, 16174, 1, 1, 3, 3, 3, 6),
    _Group3HumidDataStr_Type()
)
group3HumidDataStr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    group3HumidDataStr.setStatus("current")


class _Group3HumidDataInt_Type(Integer32):
    """Custom type group3HumidDataInt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_Group3HumidDataInt_Type.__name__ = "Integer32"
_Group3HumidDataInt_Object = MibScalar
group3HumidDataInt = _Group3HumidDataInt_Object(
    (1, 3, 6, 1, 4, 1, 16174, 1, 1, 3, 3, 3, 7),
    _Group3HumidDataInt_Type()
)
group3HumidDataInt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    group3HumidDataInt.setStatus("current")


class _Group3WetName_Type(DisplayString):
    """Custom type group3WetName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )
    fixed_length = 16


_Group3WetName_Type.__name__ = "DisplayString"
_Group3WetName_Object = MibScalar
group3WetName = _Group3WetName_Object(
    (1, 3, 6, 1, 4, 1, 16174, 1, 1, 3, 3, 3, 8),
    _Group3WetName_Type()
)
group3WetName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    group3WetName.setStatus("current")


class _Group3WetDataStr_Type(DisplayString):
    """Custom type group3WetDataStr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(5, 5),
    )
    fixed_length = 5


_Group3WetDataStr_Type.__name__ = "DisplayString"
_Group3WetDataStr_Object = MibScalar
group3WetDataStr = _Group3WetDataStr_Object(
    (1, 3, 6, 1, 4, 1, 16174, 1, 1, 3, 3, 3, 9),
    _Group3WetDataStr_Type()
)
group3WetDataStr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    group3WetDataStr.setStatus("current")


class _Group3WetDataInt_Type(Integer32):
    """Custom type group3WetDataInt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 110),
    )


_Group3WetDataInt_Type.__name__ = "Integer32"
_Group3WetDataInt_Object = MibScalar
group3WetDataInt = _Group3WetDataInt_Object(
    (1, 3, 6, 1, 4, 1, 16174, 1, 1, 3, 3, 3, 10),
    _Group3WetDataInt_Type()
)
group3WetDataInt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    group3WetDataInt.setStatus("current")
_Group4_ObjectIdentity = ObjectIdentity
group4 = _Group4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 16174, 1, 1, 3, 3, 4)
)


class _Group4Name_Type(DisplayString):
    """Custom type group4Name based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )
    fixed_length = 16


_Group4Name_Type.__name__ = "DisplayString"
_Group4Name_Object = MibScalar
group4Name = _Group4Name_Object(
    (1, 3, 6, 1, 4, 1, 16174, 1, 1, 3, 3, 4, 1),
    _Group4Name_Type()
)
group4Name.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    group4Name.setStatus("current")


class _Group4TempName_Type(DisplayString):
    """Custom type group4TempName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )
    fixed_length = 16


_Group4TempName_Type.__name__ = "DisplayString"
_Group4TempName_Object = MibScalar
group4TempName = _Group4TempName_Object(
    (1, 3, 6, 1, 4, 1, 16174, 1, 1, 3, 3, 4, 2),
    _Group4TempName_Type()
)
group4TempName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    group4TempName.setStatus("current")


class _Group4TempDataStr_Type(DisplayString):
    """Custom type group4TempDataStr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(5, 5),
    )
    fixed_length = 5


_Group4TempDataStr_Type.__name__ = "DisplayString"
_Group4TempDataStr_Object = MibScalar
group4TempDataStr = _Group4TempDataStr_Object(
    (1, 3, 6, 1, 4, 1, 16174, 1, 1, 3, 3, 4, 3),
    _Group4TempDataStr_Type()
)
group4TempDataStr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    group4TempDataStr.setStatus("current")


class _Group4TempDataInt_Type(Integer32):
    """Custom type group4TempDataInt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1000, 10000),
    )


_Group4TempDataInt_Type.__name__ = "Integer32"
_Group4TempDataInt_Object = MibScalar
group4TempDataInt = _Group4TempDataInt_Object(
    (1, 3, 6, 1, 4, 1, 16174, 1, 1, 3, 3, 4, 4),
    _Group4TempDataInt_Type()
)
group4TempDataInt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    group4TempDataInt.setStatus("current")


class _Group4HumidName_Type(DisplayString):
    """Custom type group4HumidName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )
    fixed_length = 16


_Group4HumidName_Type.__name__ = "DisplayString"
_Group4HumidName_Object = MibScalar
group4HumidName = _Group4HumidName_Object(
    (1, 3, 6, 1, 4, 1, 16174, 1, 1, 3, 3, 4, 5),
    _Group4HumidName_Type()
)
group4HumidName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    group4HumidName.setStatus("current")


class _Group4HumidDataStr_Type(DisplayString):
    """Custom type group4HumidDataStr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(5, 5),
    )
    fixed_length = 5


_Group4HumidDataStr_Type.__name__ = "DisplayString"
_Group4HumidDataStr_Object = MibScalar
group4HumidDataStr = _Group4HumidDataStr_Object(
    (1, 3, 6, 1, 4, 1, 16174, 1, 1, 3, 3, 4, 6),
    _Group4HumidDataStr_Type()
)
group4HumidDataStr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    group4HumidDataStr.setStatus("current")


class _Group4HumidDataInt_Type(Integer32):
    """Custom type group4HumidDataInt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_Group4HumidDataInt_Type.__name__ = "Integer32"
_Group4HumidDataInt_Object = MibScalar
group4HumidDataInt = _Group4HumidDataInt_Object(
    (1, 3, 6, 1, 4, 1, 16174, 1, 1, 3, 3, 4, 7),
    _Group4HumidDataInt_Type()
)
group4HumidDataInt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    group4HumidDataInt.setStatus("current")


class _Group4WetName_Type(DisplayString):
    """Custom type group4WetName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )
    fixed_length = 16


_Group4WetName_Type.__name__ = "DisplayString"
_Group4WetName_Object = MibScalar
group4WetName = _Group4WetName_Object(
    (1, 3, 6, 1, 4, 1, 16174, 1, 1, 3, 3, 4, 8),
    _Group4WetName_Type()
)
group4WetName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    group4WetName.setStatus("current")


class _Group4WetDataStr_Type(DisplayString):
    """Custom type group4WetDataStr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(5, 5),
    )
    fixed_length = 5


_Group4WetDataStr_Type.__name__ = "DisplayString"
_Group4WetDataStr_Object = MibScalar
group4WetDataStr = _Group4WetDataStr_Object(
    (1, 3, 6, 1, 4, 1, 16174, 1, 1, 3, 3, 4, 9),
    _Group4WetDataStr_Type()
)
group4WetDataStr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    group4WetDataStr.setStatus("current")


class _Group4WetDataInt_Type(Integer32):
    """Custom type group4WetDataInt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 110),
    )


_Group4WetDataInt_Type.__name__ = "Integer32"
_Group4WetDataInt_Object = MibScalar
group4WetDataInt = _Group4WetDataInt_Object(
    (1, 3, 6, 1, 4, 1, 16174, 1, 1, 3, 3, 4, 10),
    _Group4WetDataInt_Type()
)
group4WetDataInt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    group4WetDataInt.setStatus("current")
_Group5_ObjectIdentity = ObjectIdentity
group5 = _Group5_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 16174, 1, 1, 3, 3, 5)
)
_PCMprobe1_ObjectIdentity = ObjectIdentity
PCMprobe1 = _PCMprobe1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 16174, 1, 1, 3, 3, 5, 1)
)


class _Probe1Name_Type(DisplayString):
    """Custom type probe1Name based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )
    fixed_length = 16


_Probe1Name_Type.__name__ = "DisplayString"
_Probe1Name_Object = MibScalar
probe1Name = _Probe1Name_Object(
    (1, 3, 6, 1, 4, 1, 16174, 1, 1, 3, 3, 5, 1, 1),
    _Probe1Name_Type()
)
probe1Name.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    probe1Name.setStatus("current")


class _Probe1State_Type(Integer32):
    """Custom type probe1State based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Probe1State_Type.__name__ = "Integer32"
_Probe1State_Object = MibScalar
probe1State = _Probe1State_Object(
    (1, 3, 6, 1, 4, 1, 16174, 1, 1, 3, 3, 5, 1, 2),
    _Probe1State_Type()
)
probe1State.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    probe1State.setStatus("current")


class _Probe1Flags_Type(Integer32):
    """Custom type probe1Flags based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_Probe1Flags_Type.__name__ = "Integer32"
_Probe1Flags_Object = MibScalar
probe1Flags = _Probe1Flags_Object(
    (1, 3, 6, 1, 4, 1, 16174, 1, 1, 3, 3, 5, 1, 3),
    _Probe1Flags_Type()
)
probe1Flags.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    probe1Flags.setStatus("current")
_PCMprobe2_ObjectIdentity = ObjectIdentity
PCMprobe2 = _PCMprobe2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 16174, 1, 1, 3, 3, 5, 2)
)


class _Probe2Name_Type(DisplayString):
    """Custom type probe2Name based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )
    fixed_length = 16


_Probe2Name_Type.__name__ = "DisplayString"
_Probe2Name_Object = MibScalar
probe2Name = _Probe2Name_Object(
    (1, 3, 6, 1, 4, 1, 16174, 1, 1, 3, 3, 5, 2, 1),
    _Probe2Name_Type()
)
probe2Name.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    probe2Name.setStatus("current")


class _Probe2State_Type(Integer32):
    """Custom type probe2State based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Probe2State_Type.__name__ = "Integer32"
_Probe2State_Object = MibScalar
probe2State = _Probe2State_Object(
    (1, 3, 6, 1, 4, 1, 16174, 1, 1, 3, 3, 5, 2, 2),
    _Probe2State_Type()
)
probe2State.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    probe2State.setStatus("current")


class _Probe2Flags_Type(Integer32):
    """Custom type probe2Flags based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_Probe2Flags_Type.__name__ = "Integer32"
_Probe2Flags_Object = MibScalar
probe2Flags = _Probe2Flags_Object(
    (1, 3, 6, 1, 4, 1, 16174, 1, 1, 3, 3, 5, 2, 3),
    _Probe2Flags_Type()
)
probe2Flags.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    probe2Flags.setStatus("current")
_PCMprobe3_ObjectIdentity = ObjectIdentity
PCMprobe3 = _PCMprobe3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 16174, 1, 1, 3, 3, 5, 3)
)


class _Probe3Name_Type(DisplayString):
    """Custom type probe3Name based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )
    fixed_length = 16


_Probe3Name_Type.__name__ = "DisplayString"
_Probe3Name_Object = MibScalar
probe3Name = _Probe3Name_Object(
    (1, 3, 6, 1, 4, 1, 16174, 1, 1, 3, 3, 5, 3, 1),
    _Probe3Name_Type()
)
probe3Name.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    probe3Name.setStatus("current")


class _Probe3State_Type(Integer32):
    """Custom type probe3State based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Probe3State_Type.__name__ = "Integer32"
_Probe3State_Object = MibScalar
probe3State = _Probe3State_Object(
    (1, 3, 6, 1, 4, 1, 16174, 1, 1, 3, 3, 5, 3, 2),
    _Probe3State_Type()
)
probe3State.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    probe3State.setStatus("current")


class _Probe3Flags_Type(Integer32):
    """Custom type probe3Flags based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_Probe3Flags_Type.__name__ = "Integer32"
_Probe3Flags_Object = MibScalar
probe3Flags = _Probe3Flags_Object(
    (1, 3, 6, 1, 4, 1, 16174, 1, 1, 3, 3, 5, 3, 3),
    _Probe3Flags_Type()
)
probe3Flags.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    probe3Flags.setStatus("current")
_PCMprobe4_ObjectIdentity = ObjectIdentity
PCMprobe4 = _PCMprobe4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 16174, 1, 1, 3, 3, 5, 4)
)


class _Probe4Name_Type(DisplayString):
    """Custom type probe4Name based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )
    fixed_length = 16


_Probe4Name_Type.__name__ = "DisplayString"
_Probe4Name_Object = MibScalar
probe4Name = _Probe4Name_Object(
    (1, 3, 6, 1, 4, 1, 16174, 1, 1, 3, 3, 5, 4, 1),
    _Probe4Name_Type()
)
probe4Name.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    probe4Name.setStatus("current")


class _Probe4State_Type(Integer32):
    """Custom type probe4State based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Probe4State_Type.__name__ = "Integer32"
_Probe4State_Object = MibScalar
probe4State = _Probe4State_Object(
    (1, 3, 6, 1, 4, 1, 16174, 1, 1, 3, 3, 5, 4, 2),
    _Probe4State_Type()
)
probe4State.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    probe4State.setStatus("current")


class _Probe4Flags_Type(Integer32):
    """Custom type probe4Flags based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_Probe4Flags_Type.__name__ = "Integer32"
_Probe4Flags_Object = MibScalar
probe4Flags = _Probe4Flags_Object(
    (1, 3, 6, 1, 4, 1, 16174, 1, 1, 3, 3, 5, 4, 3),
    _Probe4Flags_Type()
)
probe4Flags.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    probe4Flags.setStatus("current")
_PCMprobe5_ObjectIdentity = ObjectIdentity
PCMprobe5 = _PCMprobe5_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 16174, 1, 1, 3, 3, 5, 5)
)


class _Probe5Name_Type(DisplayString):
    """Custom type probe5Name based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )
    fixed_length = 16


_Probe5Name_Type.__name__ = "DisplayString"
_Probe5Name_Object = MibScalar
probe5Name = _Probe5Name_Object(
    (1, 3, 6, 1, 4, 1, 16174, 1, 1, 3, 3, 5, 5, 1),
    _Probe5Name_Type()
)
probe5Name.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    probe5Name.setStatus("current")


class _Probe5State_Type(Integer32):
    """Custom type probe5State based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Probe5State_Type.__name__ = "Integer32"
_Probe5State_Object = MibScalar
probe5State = _Probe5State_Object(
    (1, 3, 6, 1, 4, 1, 16174, 1, 1, 3, 3, 5, 5, 2),
    _Probe5State_Type()
)
probe5State.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    probe5State.setStatus("current")


class _Probe5Flags_Type(Integer32):
    """Custom type probe5Flags based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_Probe5Flags_Type.__name__ = "Integer32"
_Probe5Flags_Object = MibScalar
probe5Flags = _Probe5Flags_Object(
    (1, 3, 6, 1, 4, 1, 16174, 1, 1, 3, 3, 5, 5, 3),
    _Probe5Flags_Type()
)
probe5Flags.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    probe5Flags.setStatus("current")
_PCMprobe6_ObjectIdentity = ObjectIdentity
PCMprobe6 = _PCMprobe6_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 16174, 1, 1, 3, 3, 5, 6)
)


class _Probe6Name_Type(DisplayString):
    """Custom type probe6Name based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )
    fixed_length = 16


_Probe6Name_Type.__name__ = "DisplayString"
_Probe6Name_Object = MibScalar
probe6Name = _Probe6Name_Object(
    (1, 3, 6, 1, 4, 1, 16174, 1, 1, 3, 3, 5, 6, 1),
    _Probe6Name_Type()
)
probe6Name.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    probe6Name.setStatus("current")


class _Probe6State_Type(Integer32):
    """Custom type probe6State based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Probe6State_Type.__name__ = "Integer32"
_Probe6State_Object = MibScalar
probe6State = _Probe6State_Object(
    (1, 3, 6, 1, 4, 1, 16174, 1, 1, 3, 3, 5, 6, 2),
    _Probe6State_Type()
)
probe6State.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    probe6State.setStatus("current")


class _Probe6Flags_Type(Integer32):
    """Custom type probe6Flags based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_Probe6Flags_Type.__name__ = "Integer32"
_Probe6Flags_Object = MibScalar
probe6Flags = _Probe6Flags_Object(
    (1, 3, 6, 1, 4, 1, 16174, 1, 1, 3, 3, 5, 6, 3),
    _Probe6Flags_Type()
)
probe6Flags.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    probe6Flags.setStatus("current")
_PCMprobe7_ObjectIdentity = ObjectIdentity
PCMprobe7 = _PCMprobe7_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 16174, 1, 1, 3, 3, 5, 7)
)


class _Probe7Name_Type(DisplayString):
    """Custom type probe7Name based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )
    fixed_length = 16


_Probe7Name_Type.__name__ = "DisplayString"
_Probe7Name_Object = MibScalar
probe7Name = _Probe7Name_Object(
    (1, 3, 6, 1, 4, 1, 16174, 1, 1, 3, 3, 5, 7, 1),
    _Probe7Name_Type()
)
probe7Name.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    probe7Name.setStatus("current")


class _Probe7State_Type(Integer32):
    """Custom type probe7State based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Probe7State_Type.__name__ = "Integer32"
_Probe7State_Object = MibScalar
probe7State = _Probe7State_Object(
    (1, 3, 6, 1, 4, 1, 16174, 1, 1, 3, 3, 5, 7, 2),
    _Probe7State_Type()
)
probe7State.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    probe7State.setStatus("current")


class _Probe7Flags_Type(Integer32):
    """Custom type probe7Flags based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_Probe7Flags_Type.__name__ = "Integer32"
_Probe7Flags_Object = MibScalar
probe7Flags = _Probe7Flags_Object(
    (1, 3, 6, 1, 4, 1, 16174, 1, 1, 3, 3, 5, 7, 3),
    _Probe7Flags_Type()
)
probe7Flags.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    probe7Flags.setStatus("current")
_PCMprobe8_ObjectIdentity = ObjectIdentity
PCMprobe8 = _PCMprobe8_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 16174, 1, 1, 3, 3, 5, 8)
)


class _Probe8Name_Type(DisplayString):
    """Custom type probe8Name based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )
    fixed_length = 16


_Probe8Name_Type.__name__ = "DisplayString"
_Probe8Name_Object = MibScalar
probe8Name = _Probe8Name_Object(
    (1, 3, 6, 1, 4, 1, 16174, 1, 1, 3, 3, 5, 8, 1),
    _Probe8Name_Type()
)
probe8Name.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    probe8Name.setStatus("current")


class _Probe8State_Type(Integer32):
    """Custom type probe8State based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Probe8State_Type.__name__ = "Integer32"
_Probe8State_Object = MibScalar
probe8State = _Probe8State_Object(
    (1, 3, 6, 1, 4, 1, 16174, 1, 1, 3, 3, 5, 8, 2),
    _Probe8State_Type()
)
probe8State.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    probe8State.setStatus("current")


class _Probe8Flags_Type(Integer32):
    """Custom type probe8Flags based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_Probe8Flags_Type.__name__ = "Integer32"
_Probe8Flags_Object = MibScalar
probe8Flags = _Probe8Flags_Object(
    (1, 3, 6, 1, 4, 1, 16174, 1, 1, 3, 3, 5, 8, 3),
    _Probe8Flags_Type()
)
probe8Flags.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    probe8Flags.setStatus("current")
_PCMprobe9_ObjectIdentity = ObjectIdentity
PCMprobe9 = _PCMprobe9_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 16174, 1, 1, 3, 3, 5, 9)
)


class _Probe9Name_Type(DisplayString):
    """Custom type probe9Name based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )
    fixed_length = 16


_Probe9Name_Type.__name__ = "DisplayString"
_Probe9Name_Object = MibScalar
probe9Name = _Probe9Name_Object(
    (1, 3, 6, 1, 4, 1, 16174, 1, 1, 3, 3, 5, 9, 1),
    _Probe9Name_Type()
)
probe9Name.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    probe9Name.setStatus("current")


class _Probe9State_Type(Integer32):
    """Custom type probe9State based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Probe9State_Type.__name__ = "Integer32"
_Probe9State_Object = MibScalar
probe9State = _Probe9State_Object(
    (1, 3, 6, 1, 4, 1, 16174, 1, 1, 3, 3, 5, 9, 2),
    _Probe9State_Type()
)
probe9State.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    probe9State.setStatus("current")


class _Probe9Flags_Type(Integer32):
    """Custom type probe9Flags based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_Probe9Flags_Type.__name__ = "Integer32"
_Probe9Flags_Object = MibScalar
probe9Flags = _Probe9Flags_Object(
    (1, 3, 6, 1, 4, 1, 16174, 1, 1, 3, 3, 5, 9, 3),
    _Probe9Flags_Type()
)
probe9Flags.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    probe9Flags.setStatus("current")
_PCMprobe10_ObjectIdentity = ObjectIdentity
PCMprobe10 = _PCMprobe10_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 16174, 1, 1, 3, 3, 5, 10)
)


class _Probe10Name_Type(DisplayString):
    """Custom type probe10Name based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )
    fixed_length = 16


_Probe10Name_Type.__name__ = "DisplayString"
_Probe10Name_Object = MibScalar
probe10Name = _Probe10Name_Object(
    (1, 3, 6, 1, 4, 1, 16174, 1, 1, 3, 3, 5, 10, 1),
    _Probe10Name_Type()
)
probe10Name.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    probe10Name.setStatus("current")


class _Probe10State_Type(Integer32):
    """Custom type probe10State based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Probe10State_Type.__name__ = "Integer32"
_Probe10State_Object = MibScalar
probe10State = _Probe10State_Object(
    (1, 3, 6, 1, 4, 1, 16174, 1, 1, 3, 3, 5, 10, 2),
    _Probe10State_Type()
)
probe10State.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    probe10State.setStatus("current")


class _Probe10Flags_Type(Integer32):
    """Custom type probe10Flags based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_Probe10Flags_Type.__name__ = "Integer32"
_Probe10Flags_Object = MibScalar
probe10Flags = _Probe10Flags_Object(
    (1, 3, 6, 1, 4, 1, 16174, 1, 1, 3, 3, 5, 10, 3),
    _Probe10Flags_Type()
)
probe10Flags.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    probe10Flags.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SENSATRONICS-EM1",
    **{"productEM1": productEM1,
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
       "group1": group1,
       "group1Name": group1Name,
       "group1TempName": group1TempName,
       "group1TempDataStr": group1TempDataStr,
       "group1TempDataInt": group1TempDataInt,
       "group1HumidName": group1HumidName,
       "group1HumidDataStr": group1HumidDataStr,
       "group1HumidDataInt": group1HumidDataInt,
       "group1WetName": group1WetName,
       "group1WetDataStr": group1WetDataStr,
       "group1WetDataInt": group1WetDataInt,
       "group2": group2,
       "group2Name": group2Name,
       "group2TempName": group2TempName,
       "group2TempDataStr": group2TempDataStr,
       "group2TempDataInt": group2TempDataInt,
       "group2HumidName": group2HumidName,
       "group2HumidDataStr": group2HumidDataStr,
       "group2HumidDataInt": group2HumidDataInt,
       "group2WetName": group2WetName,
       "group2WetDataStr": group2WetDataStr,
       "group2WetDataInt": group2WetDataInt,
       "group3": group3,
       "group3Name": group3Name,
       "group3TempName": group3TempName,
       "group3TempDataStr": group3TempDataStr,
       "group3TempDataInt": group3TempDataInt,
       "group3HumidName": group3HumidName,
       "group3HumidDataStr": group3HumidDataStr,
       "group3HumidDataInt": group3HumidDataInt,
       "group3WetName": group3WetName,
       "group3WetDataStr": group3WetDataStr,
       "group3WetDataInt": group3WetDataInt,
       "group4": group4,
       "group4Name": group4Name,
       "group4TempName": group4TempName,
       "group4TempDataStr": group4TempDataStr,
       "group4TempDataInt": group4TempDataInt,
       "group4HumidName": group4HumidName,
       "group4HumidDataStr": group4HumidDataStr,
       "group4HumidDataInt": group4HumidDataInt,
       "group4WetName": group4WetName,
       "group4WetDataStr": group4WetDataStr,
       "group4WetDataInt": group4WetDataInt,
       "group5": group5,
       "PCMprobe1": PCMprobe1,
       "probe1Name": probe1Name,
       "probe1State": probe1State,
       "probe1Flags": probe1Flags,
       "PCMprobe2": PCMprobe2,
       "probe2Name": probe2Name,
       "probe2State": probe2State,
       "probe2Flags": probe2Flags,
       "PCMprobe3": PCMprobe3,
       "probe3Name": probe3Name,
       "probe3State": probe3State,
       "probe3Flags": probe3Flags,
       "PCMprobe4": PCMprobe4,
       "probe4Name": probe4Name,
       "probe4State": probe4State,
       "probe4Flags": probe4Flags,
       "PCMprobe5": PCMprobe5,
       "probe5Name": probe5Name,
       "probe5State": probe5State,
       "probe5Flags": probe5Flags,
       "PCMprobe6": PCMprobe6,
       "probe6Name": probe6Name,
       "probe6State": probe6State,
       "probe6Flags": probe6Flags,
       "PCMprobe7": PCMprobe7,
       "probe7Name": probe7Name,
       "probe7State": probe7State,
       "probe7Flags": probe7Flags,
       "PCMprobe8": PCMprobe8,
       "probe8Name": probe8Name,
       "probe8State": probe8State,
       "probe8Flags": probe8Flags,
       "PCMprobe9": PCMprobe9,
       "probe9Name": probe9Name,
       "probe9State": probe9State,
       "probe9Flags": probe9Flags,
       "PCMprobe10": PCMprobe10,
       "probe10Name": probe10Name,
       "probe10State": probe10State,
       "probe10Flags": probe10Flags}
)
