# SNMP MIB module (CUBO-MINI-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\hubersuhner\CUBO-MINI

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

(cmini_cube,) = mibBuilder.importSymbols(
    "CUBO-MIB",
    "cmini-cube")

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

(DisplayString,
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

cubo_mini = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 27894, 11, 241)
)
if mibBuilder.loadTexts:
    cubo_mini.setRevisions(
        ("2025-02-24 16:08",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CubominiObjects_ObjectIdentity = ObjectIdentity
cubominiObjects = _CubominiObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27894, 11, 241, 1)
)
_CubominiGeneralGroup_ObjectIdentity = ObjectIdentity
cubominiGeneralGroup = _CubominiGeneralGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27894, 11, 241, 1, 1)
)
_CubominiSystemDataTable_Object = MibTable
cubominiSystemDataTable = _CubominiSystemDataTable_Object(
    (1, 3, 6, 1, 4, 1, 27894, 11, 241, 1, 1, 1)
)
if mibBuilder.loadTexts:
    cubominiSystemDataTable.setStatus("current")
_CubominiSystemDataEntry_Object = MibTableRow
cubominiSystemDataEntry = _CubominiSystemDataEntry_Object(
    (1, 3, 6, 1, 4, 1, 27894, 11, 241, 1, 1, 1, 1)
)
cubominiSystemDataEntry.setIndexNames(
    (0, "CUBO-MINI-MIB", "cubominiSystemDataChassisId"),
)
if mibBuilder.loadTexts:
    cubominiSystemDataEntry.setStatus("current")


class _CubominiSystemDataChassisId_Type(Integer32):
    """Custom type cubominiSystemDataChassisId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CubominiSystemDataChassisId_Type.__name__ = "Integer32"
_CubominiSystemDataChassisId_Object = MibTableColumn
cubominiSystemDataChassisId = _CubominiSystemDataChassisId_Object(
    (1, 3, 6, 1, 4, 1, 27894, 11, 241, 1, 1, 1, 1, 1),
    _CubominiSystemDataChassisId_Type()
)
cubominiSystemDataChassisId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cubominiSystemDataChassisId.setStatus("current")


class _CubominiSystemDataSerialNumber_Type(OctetString):
    """Custom type cubominiSystemDataSerialNumber based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(255, 255),
    )
    fixed_length = 255


_CubominiSystemDataSerialNumber_Type.__name__ = "OctetString"
_CubominiSystemDataSerialNumber_Object = MibTableColumn
cubominiSystemDataSerialNumber = _CubominiSystemDataSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 27894, 11, 241, 1, 1, 1, 1, 2),
    _CubominiSystemDataSerialNumber_Type()
)
cubominiSystemDataSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cubominiSystemDataSerialNumber.setStatus("current")


class _CubominiSystemDataDeviceName_Type(OctetString):
    """Custom type cubominiSystemDataDeviceName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(255, 255),
    )
    fixed_length = 255


_CubominiSystemDataDeviceName_Type.__name__ = "OctetString"
_CubominiSystemDataDeviceName_Object = MibTableColumn
cubominiSystemDataDeviceName = _CubominiSystemDataDeviceName_Object(
    (1, 3, 6, 1, 4, 1, 27894, 11, 241, 1, 1, 1, 1, 3),
    _CubominiSystemDataDeviceName_Type()
)
cubominiSystemDataDeviceName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cubominiSystemDataDeviceName.setStatus("current")


class _CubominiSystemDataSwVersion_Type(OctetString):
    """Custom type cubominiSystemDataSwVersion based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(64, 64),
    )
    fixed_length = 64


_CubominiSystemDataSwVersion_Type.__name__ = "OctetString"
_CubominiSystemDataSwVersion_Object = MibTableColumn
cubominiSystemDataSwVersion = _CubominiSystemDataSwVersion_Object(
    (1, 3, 6, 1, 4, 1, 27894, 11, 241, 1, 1, 1, 1, 4),
    _CubominiSystemDataSwVersion_Type()
)
cubominiSystemDataSwVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cubominiSystemDataSwVersion.setStatus("current")


class _CubominiSystemDataFwVersion_Type(OctetString):
    """Custom type cubominiSystemDataFwVersion based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(64, 64),
    )
    fixed_length = 64


_CubominiSystemDataFwVersion_Type.__name__ = "OctetString"
_CubominiSystemDataFwVersion_Object = MibTableColumn
cubominiSystemDataFwVersion = _CubominiSystemDataFwVersion_Object(
    (1, 3, 6, 1, 4, 1, 27894, 11, 241, 1, 1, 1, 1, 5),
    _CubominiSystemDataFwVersion_Type()
)
cubominiSystemDataFwVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cubominiSystemDataFwVersion.setStatus("current")


class _CubominiSystemDataHwVersion_Type(OctetString):
    """Custom type cubominiSystemDataHwVersion based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(64, 64),
    )
    fixed_length = 64


_CubominiSystemDataHwVersion_Type.__name__ = "OctetString"
_CubominiSystemDataHwVersion_Object = MibTableColumn
cubominiSystemDataHwVersion = _CubominiSystemDataHwVersion_Object(
    (1, 3, 6, 1, 4, 1, 27894, 11, 241, 1, 1, 1, 1, 6),
    _CubominiSystemDataHwVersion_Type()
)
cubominiSystemDataHwVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cubominiSystemDataHwVersion.setStatus("current")
_CubominiFanGroup_ObjectIdentity = ObjectIdentity
cubominiFanGroup = _CubominiFanGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27894, 11, 241, 1, 3)
)
_CubominiFanTable_Object = MibTable
cubominiFanTable = _CubominiFanTable_Object(
    (1, 3, 6, 1, 4, 1, 27894, 11, 241, 1, 3, 1)
)
if mibBuilder.loadTexts:
    cubominiFanTable.setStatus("current")
_CubominiFanEntry_Object = MibTableRow
cubominiFanEntry = _CubominiFanEntry_Object(
    (1, 3, 6, 1, 4, 1, 27894, 11, 241, 1, 3, 1, 1)
)
cubominiFanEntry.setIndexNames(
    (0, "CUBO-MINI-MIB", "cubominiFanChassisId"),
    (0, "CUBO-MINI-MIB", "cubominiFanSlotId"),
    (0, "CUBO-MINI-MIB", "cubominiFanFanslotminiId"),
)
if mibBuilder.loadTexts:
    cubominiFanEntry.setStatus("current")


class _CubominiFanChassisId_Type(Integer32):
    """Custom type cubominiFanChassisId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CubominiFanChassisId_Type.__name__ = "Integer32"
_CubominiFanChassisId_Object = MibTableColumn
cubominiFanChassisId = _CubominiFanChassisId_Object(
    (1, 3, 6, 1, 4, 1, 27894, 11, 241, 1, 3, 1, 1, 1),
    _CubominiFanChassisId_Type()
)
cubominiFanChassisId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cubominiFanChassisId.setStatus("current")


class _CubominiFanSlotId_Type(Integer32):
    """Custom type cubominiFanSlotId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CubominiFanSlotId_Type.__name__ = "Integer32"
_CubominiFanSlotId_Object = MibTableColumn
cubominiFanSlotId = _CubominiFanSlotId_Object(
    (1, 3, 6, 1, 4, 1, 27894, 11, 241, 1, 3, 1, 1, 2),
    _CubominiFanSlotId_Type()
)
cubominiFanSlotId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cubominiFanSlotId.setStatus("current")


class _CubominiFanFanslotminiId_Type(Integer32):
    """Custom type cubominiFanFanslotminiId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CubominiFanFanslotminiId_Type.__name__ = "Integer32"
_CubominiFanFanslotminiId_Object = MibTableColumn
cubominiFanFanslotminiId = _CubominiFanFanslotminiId_Object(
    (1, 3, 6, 1, 4, 1, 27894, 11, 241, 1, 3, 1, 1, 3),
    _CubominiFanFanslotminiId_Type()
)
cubominiFanFanslotminiId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cubominiFanFanslotminiId.setStatus("current")


class _CubominiFanStatus_Type(Integer32):
    """Custom type cubominiFanStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("fail", 2),
          ("ok", 3))
    )


_CubominiFanStatus_Type.__name__ = "Integer32"
_CubominiFanStatus_Object = MibTableColumn
cubominiFanStatus = _CubominiFanStatus_Object(
    (1, 3, 6, 1, 4, 1, 27894, 11, 241, 1, 3, 1, 1, 4),
    _CubominiFanStatus_Type()
)
cubominiFanStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cubominiFanStatus.setStatus("current")
_CubominiFanSpeed_Type = Integer32
_CubominiFanSpeed_Object = MibTableColumn
cubominiFanSpeed = _CubominiFanSpeed_Object(
    (1, 3, 6, 1, 4, 1, 27894, 11, 241, 1, 3, 1, 1, 5),
    _CubominiFanSpeed_Type()
)
cubominiFanSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cubominiFanSpeed.setStatus("current")
if mibBuilder.loadTexts:
    cubominiFanSpeed.setUnits("r.p.m.")
_CubominiManagementGroup_ObjectIdentity = ObjectIdentity
cubominiManagementGroup = _CubominiManagementGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27894, 11, 241, 1, 4)
)
_CubominiSnmpManagersTable_Object = MibTable
cubominiSnmpManagersTable = _CubominiSnmpManagersTable_Object(
    (1, 3, 6, 1, 4, 1, 27894, 11, 241, 1, 4, 1)
)
if mibBuilder.loadTexts:
    cubominiSnmpManagersTable.setStatus("current")
_CubominiSnmpManagersEntry_Object = MibTableRow
cubominiSnmpManagersEntry = _CubominiSnmpManagersEntry_Object(
    (1, 3, 6, 1, 4, 1, 27894, 11, 241, 1, 4, 1, 1)
)
cubominiSnmpManagersEntry.setIndexNames(
    (0, "CUBO-MINI-MIB", "cubominiSnmpManagersChassisId"),
    (0, "CUBO-MINI-MIB", "cubominiSnmpManagersSnmpindexId"),
)
if mibBuilder.loadTexts:
    cubominiSnmpManagersEntry.setStatus("current")


class _CubominiSnmpManagersChassisId_Type(Integer32):
    """Custom type cubominiSnmpManagersChassisId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CubominiSnmpManagersChassisId_Type.__name__ = "Integer32"
_CubominiSnmpManagersChassisId_Object = MibTableColumn
cubominiSnmpManagersChassisId = _CubominiSnmpManagersChassisId_Object(
    (1, 3, 6, 1, 4, 1, 27894, 11, 241, 1, 4, 1, 1, 1),
    _CubominiSnmpManagersChassisId_Type()
)
cubominiSnmpManagersChassisId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cubominiSnmpManagersChassisId.setStatus("current")


class _CubominiSnmpManagersSnmpindexId_Type(Integer32):
    """Custom type cubominiSnmpManagersSnmpindexId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CubominiSnmpManagersSnmpindexId_Type.__name__ = "Integer32"
_CubominiSnmpManagersSnmpindexId_Object = MibTableColumn
cubominiSnmpManagersSnmpindexId = _CubominiSnmpManagersSnmpindexId_Object(
    (1, 3, 6, 1, 4, 1, 27894, 11, 241, 1, 4, 1, 1, 2),
    _CubominiSnmpManagersSnmpindexId_Type()
)
cubominiSnmpManagersSnmpindexId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cubominiSnmpManagersSnmpindexId.setStatus("current")


class _CubominiSnmpManagersIp_Type(OctetString):
    """Custom type cubominiSnmpManagersIp based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(15, 15),
    )
    fixed_length = 15


_CubominiSnmpManagersIp_Type.__name__ = "OctetString"
_CubominiSnmpManagersIp_Object = MibTableColumn
cubominiSnmpManagersIp = _CubominiSnmpManagersIp_Object(
    (1, 3, 6, 1, 4, 1, 27894, 11, 241, 1, 4, 1, 1, 3),
    _CubominiSnmpManagersIp_Type()
)
cubominiSnmpManagersIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cubominiSnmpManagersIp.setStatus("current")
_CubominiEmsManagersTable_Object = MibTable
cubominiEmsManagersTable = _CubominiEmsManagersTable_Object(
    (1, 3, 6, 1, 4, 1, 27894, 11, 241, 1, 4, 2)
)
if mibBuilder.loadTexts:
    cubominiEmsManagersTable.setStatus("current")
_CubominiEmsManagersEntry_Object = MibTableRow
cubominiEmsManagersEntry = _CubominiEmsManagersEntry_Object(
    (1, 3, 6, 1, 4, 1, 27894, 11, 241, 1, 4, 2, 1)
)
cubominiEmsManagersEntry.setIndexNames(
    (0, "CUBO-MINI-MIB", "cubominiEmsManagersChassisId"),
    (0, "CUBO-MINI-MIB", "cubominiEmsManagersEmsindexId"),
)
if mibBuilder.loadTexts:
    cubominiEmsManagersEntry.setStatus("current")


class _CubominiEmsManagersChassisId_Type(Integer32):
    """Custom type cubominiEmsManagersChassisId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CubominiEmsManagersChassisId_Type.__name__ = "Integer32"
_CubominiEmsManagersChassisId_Object = MibTableColumn
cubominiEmsManagersChassisId = _CubominiEmsManagersChassisId_Object(
    (1, 3, 6, 1, 4, 1, 27894, 11, 241, 1, 4, 2, 1, 1),
    _CubominiEmsManagersChassisId_Type()
)
cubominiEmsManagersChassisId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cubominiEmsManagersChassisId.setStatus("current")


class _CubominiEmsManagersEmsindexId_Type(Integer32):
    """Custom type cubominiEmsManagersEmsindexId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CubominiEmsManagersEmsindexId_Type.__name__ = "Integer32"
_CubominiEmsManagersEmsindexId_Object = MibTableColumn
cubominiEmsManagersEmsindexId = _CubominiEmsManagersEmsindexId_Object(
    (1, 3, 6, 1, 4, 1, 27894, 11, 241, 1, 4, 2, 1, 2),
    _CubominiEmsManagersEmsindexId_Type()
)
cubominiEmsManagersEmsindexId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cubominiEmsManagersEmsindexId.setStatus("current")


class _CubominiEmsManagersIp_Type(OctetString):
    """Custom type cubominiEmsManagersIp based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(15, 15),
    )
    fixed_length = 15


_CubominiEmsManagersIp_Type.__name__ = "OctetString"
_CubominiEmsManagersIp_Object = MibTableColumn
cubominiEmsManagersIp = _CubominiEmsManagersIp_Object(
    (1, 3, 6, 1, 4, 1, 27894, 11, 241, 1, 4, 2, 1, 3),
    _CubominiEmsManagersIp_Type()
)
cubominiEmsManagersIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cubominiEmsManagersIp.setStatus("current")
_CubominiNetworkIfGroup_ObjectIdentity = ObjectIdentity
cubominiNetworkIfGroup = _CubominiNetworkIfGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27894, 11, 241, 1, 5)
)
_CubominiNetworkIfTable_Object = MibTable
cubominiNetworkIfTable = _CubominiNetworkIfTable_Object(
    (1, 3, 6, 1, 4, 1, 27894, 11, 241, 1, 5, 1)
)
if mibBuilder.loadTexts:
    cubominiNetworkIfTable.setStatus("current")
_CubominiNetworkIfEntry_Object = MibTableRow
cubominiNetworkIfEntry = _CubominiNetworkIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 27894, 11, 241, 1, 5, 1, 1)
)
cubominiNetworkIfEntry.setIndexNames(
    (0, "CUBO-MINI-MIB", "cubominiNetworkIfChassisId"),
    (0, "CUBO-MINI-MIB", "cubominiNetworkIfNetindexId"),
)
if mibBuilder.loadTexts:
    cubominiNetworkIfEntry.setStatus("current")


class _CubominiNetworkIfChassisId_Type(Integer32):
    """Custom type cubominiNetworkIfChassisId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CubominiNetworkIfChassisId_Type.__name__ = "Integer32"
_CubominiNetworkIfChassisId_Object = MibTableColumn
cubominiNetworkIfChassisId = _CubominiNetworkIfChassisId_Object(
    (1, 3, 6, 1, 4, 1, 27894, 11, 241, 1, 5, 1, 1, 1),
    _CubominiNetworkIfChassisId_Type()
)
cubominiNetworkIfChassisId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cubominiNetworkIfChassisId.setStatus("current")


class _CubominiNetworkIfNetindexId_Type(Integer32):
    """Custom type cubominiNetworkIfNetindexId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CubominiNetworkIfNetindexId_Type.__name__ = "Integer32"
_CubominiNetworkIfNetindexId_Object = MibTableColumn
cubominiNetworkIfNetindexId = _CubominiNetworkIfNetindexId_Object(
    (1, 3, 6, 1, 4, 1, 27894, 11, 241, 1, 5, 1, 1, 2),
    _CubominiNetworkIfNetindexId_Type()
)
cubominiNetworkIfNetindexId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cubominiNetworkIfNetindexId.setStatus("current")


class _CubominiNetworkIfIPAddress_Type(OctetString):
    """Custom type cubominiNetworkIfIPAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(15, 15),
    )
    fixed_length = 15


_CubominiNetworkIfIPAddress_Type.__name__ = "OctetString"
_CubominiNetworkIfIPAddress_Object = MibTableColumn
cubominiNetworkIfIPAddress = _CubominiNetworkIfIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 27894, 11, 241, 1, 5, 1, 1, 3),
    _CubominiNetworkIfIPAddress_Type()
)
cubominiNetworkIfIPAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cubominiNetworkIfIPAddress.setStatus("current")


class _CubominiNetworkIfNetMask_Type(OctetString):
    """Custom type cubominiNetworkIfNetMask based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(15, 15),
    )
    fixed_length = 15


_CubominiNetworkIfNetMask_Type.__name__ = "OctetString"
_CubominiNetworkIfNetMask_Object = MibTableColumn
cubominiNetworkIfNetMask = _CubominiNetworkIfNetMask_Object(
    (1, 3, 6, 1, 4, 1, 27894, 11, 241, 1, 5, 1, 1, 4),
    _CubominiNetworkIfNetMask_Type()
)
cubominiNetworkIfNetMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cubominiNetworkIfNetMask.setStatus("current")


class _CubominiNetworkIfGateway_Type(OctetString):
    """Custom type cubominiNetworkIfGateway based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(15, 15),
    )
    fixed_length = 15


_CubominiNetworkIfGateway_Type.__name__ = "OctetString"
_CubominiNetworkIfGateway_Object = MibTableColumn
cubominiNetworkIfGateway = _CubominiNetworkIfGateway_Object(
    (1, 3, 6, 1, 4, 1, 27894, 11, 241, 1, 5, 1, 1, 5),
    _CubominiNetworkIfGateway_Type()
)
cubominiNetworkIfGateway.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cubominiNetworkIfGateway.setStatus("current")
_CubominiOptGeneralTable_Object = MibTable
cubominiOptGeneralTable = _CubominiOptGeneralTable_Object(
    (1, 3, 6, 1, 4, 1, 27894, 11, 241, 1, 5, 2)
)
if mibBuilder.loadTexts:
    cubominiOptGeneralTable.setStatus("current")
_CubominiOptGeneralEntry_Object = MibTableRow
cubominiOptGeneralEntry = _CubominiOptGeneralEntry_Object(
    (1, 3, 6, 1, 4, 1, 27894, 11, 241, 1, 5, 2, 1)
)
cubominiOptGeneralEntry.setIndexNames(
    (0, "CUBO-MINI-MIB", "cubominiOptGeneralChassisId"),
    (0, "CUBO-MINI-MIB", "cubominiOptGeneralMonindexId"),
    (0, "CUBO-MINI-MIB", "cubominiOptGeneralPortId"),
)
if mibBuilder.loadTexts:
    cubominiOptGeneralEntry.setStatus("current")


class _CubominiOptGeneralChassisId_Type(Integer32):
    """Custom type cubominiOptGeneralChassisId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CubominiOptGeneralChassisId_Type.__name__ = "Integer32"
_CubominiOptGeneralChassisId_Object = MibTableColumn
cubominiOptGeneralChassisId = _CubominiOptGeneralChassisId_Object(
    (1, 3, 6, 1, 4, 1, 27894, 11, 241, 1, 5, 2, 1, 1),
    _CubominiOptGeneralChassisId_Type()
)
cubominiOptGeneralChassisId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cubominiOptGeneralChassisId.setStatus("current")


class _CubominiOptGeneralMonindexId_Type(Integer32):
    """Custom type cubominiOptGeneralMonindexId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CubominiOptGeneralMonindexId_Type.__name__ = "Integer32"
_CubominiOptGeneralMonindexId_Object = MibTableColumn
cubominiOptGeneralMonindexId = _CubominiOptGeneralMonindexId_Object(
    (1, 3, 6, 1, 4, 1, 27894, 11, 241, 1, 5, 2, 1, 2),
    _CubominiOptGeneralMonindexId_Type()
)
cubominiOptGeneralMonindexId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cubominiOptGeneralMonindexId.setStatus("current")


class _CubominiOptGeneralPortId_Type(Integer32):
    """Custom type cubominiOptGeneralPortId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CubominiOptGeneralPortId_Type.__name__ = "Integer32"
_CubominiOptGeneralPortId_Object = MibTableColumn
cubominiOptGeneralPortId = _CubominiOptGeneralPortId_Object(
    (1, 3, 6, 1, 4, 1, 27894, 11, 241, 1, 5, 2, 1, 3),
    _CubominiOptGeneralPortId_Type()
)
cubominiOptGeneralPortId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cubominiOptGeneralPortId.setStatus("current")


class _CubominiOptGeneralIsInserted_Type(Integer32):
    """Custom type cubominiOptGeneralIsInserted based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("notInserted", 2),
          ("inserted", 3))
    )


_CubominiOptGeneralIsInserted_Type.__name__ = "Integer32"
_CubominiOptGeneralIsInserted_Object = MibTableColumn
cubominiOptGeneralIsInserted = _CubominiOptGeneralIsInserted_Object(
    (1, 3, 6, 1, 4, 1, 27894, 11, 241, 1, 5, 2, 1, 4),
    _CubominiOptGeneralIsInserted_Type()
)
cubominiOptGeneralIsInserted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cubominiOptGeneralIsInserted.setStatus("current")


class _CubominiOptGeneralEventsStatus_Type(OctetString):
    """Custom type cubominiOptGeneralEventsStatus based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(10, 10),
    )
    fixed_length = 10


_CubominiOptGeneralEventsStatus_Type.__name__ = "OctetString"
_CubominiOptGeneralEventsStatus_Object = MibTableColumn
cubominiOptGeneralEventsStatus = _CubominiOptGeneralEventsStatus_Object(
    (1, 3, 6, 1, 4, 1, 27894, 11, 241, 1, 5, 2, 1, 5),
    _CubominiOptGeneralEventsStatus_Type()
)
cubominiOptGeneralEventsStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cubominiOptGeneralEventsStatus.setStatus("current")


class _CubominiOptGeneralTxForce_Type(Integer32):
    """Custom type cubominiOptGeneralTxForce based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 3))
    )


_CubominiOptGeneralTxForce_Type.__name__ = "Integer32"
_CubominiOptGeneralTxForce_Object = MibTableColumn
cubominiOptGeneralTxForce = _CubominiOptGeneralTxForce_Object(
    (1, 3, 6, 1, 4, 1, 27894, 11, 241, 1, 5, 2, 1, 6),
    _CubominiOptGeneralTxForce_Type()
)
cubominiOptGeneralTxForce.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cubominiOptGeneralTxForce.setStatus("current")
_CubominiOptIdentTable_Object = MibTable
cubominiOptIdentTable = _CubominiOptIdentTable_Object(
    (1, 3, 6, 1, 4, 1, 27894, 11, 241, 1, 5, 3)
)
if mibBuilder.loadTexts:
    cubominiOptIdentTable.setStatus("current")
_CubominiOptIdentEntry_Object = MibTableRow
cubominiOptIdentEntry = _CubominiOptIdentEntry_Object(
    (1, 3, 6, 1, 4, 1, 27894, 11, 241, 1, 5, 3, 1)
)
cubominiOptIdentEntry.setIndexNames(
    (0, "CUBO-MINI-MIB", "cubominiOptIdentChassisId"),
    (0, "CUBO-MINI-MIB", "cubominiOptIdentMonindexId"),
    (0, "CUBO-MINI-MIB", "cubominiOptIdentPortId"),
)
if mibBuilder.loadTexts:
    cubominiOptIdentEntry.setStatus("current")


class _CubominiOptIdentChassisId_Type(Integer32):
    """Custom type cubominiOptIdentChassisId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CubominiOptIdentChassisId_Type.__name__ = "Integer32"
_CubominiOptIdentChassisId_Object = MibTableColumn
cubominiOptIdentChassisId = _CubominiOptIdentChassisId_Object(
    (1, 3, 6, 1, 4, 1, 27894, 11, 241, 1, 5, 3, 1, 1),
    _CubominiOptIdentChassisId_Type()
)
cubominiOptIdentChassisId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cubominiOptIdentChassisId.setStatus("current")


class _CubominiOptIdentMonindexId_Type(Integer32):
    """Custom type cubominiOptIdentMonindexId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CubominiOptIdentMonindexId_Type.__name__ = "Integer32"
_CubominiOptIdentMonindexId_Object = MibTableColumn
cubominiOptIdentMonindexId = _CubominiOptIdentMonindexId_Object(
    (1, 3, 6, 1, 4, 1, 27894, 11, 241, 1, 5, 3, 1, 2),
    _CubominiOptIdentMonindexId_Type()
)
cubominiOptIdentMonindexId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cubominiOptIdentMonindexId.setStatus("current")


class _CubominiOptIdentPortId_Type(Integer32):
    """Custom type cubominiOptIdentPortId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CubominiOptIdentPortId_Type.__name__ = "Integer32"
_CubominiOptIdentPortId_Object = MibTableColumn
cubominiOptIdentPortId = _CubominiOptIdentPortId_Object(
    (1, 3, 6, 1, 4, 1, 27894, 11, 241, 1, 5, 3, 1, 3),
    _CubominiOptIdentPortId_Type()
)
cubominiOptIdentPortId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cubominiOptIdentPortId.setStatus("current")


class _CubominiOptIdentVendorName_Type(OctetString):
    """Custom type cubominiOptIdentVendorName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )
    fixed_length = 16


_CubominiOptIdentVendorName_Type.__name__ = "OctetString"
_CubominiOptIdentVendorName_Object = MibTableColumn
cubominiOptIdentVendorName = _CubominiOptIdentVendorName_Object(
    (1, 3, 6, 1, 4, 1, 27894, 11, 241, 1, 5, 3, 1, 4),
    _CubominiOptIdentVendorName_Type()
)
cubominiOptIdentVendorName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cubominiOptIdentVendorName.setStatus("current")


class _CubominiOptIdentVendorPartNumber_Type(OctetString):
    """Custom type cubominiOptIdentVendorPartNumber based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )
    fixed_length = 16


_CubominiOptIdentVendorPartNumber_Type.__name__ = "OctetString"
_CubominiOptIdentVendorPartNumber_Object = MibTableColumn
cubominiOptIdentVendorPartNumber = _CubominiOptIdentVendorPartNumber_Object(
    (1, 3, 6, 1, 4, 1, 27894, 11, 241, 1, 5, 3, 1, 5),
    _CubominiOptIdentVendorPartNumber_Type()
)
cubominiOptIdentVendorPartNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cubominiOptIdentVendorPartNumber.setStatus("current")


class _CubominiOptIdentVendorSerialNumber_Type(OctetString):
    """Custom type cubominiOptIdentVendorSerialNumber based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )
    fixed_length = 16


_CubominiOptIdentVendorSerialNumber_Type.__name__ = "OctetString"
_CubominiOptIdentVendorSerialNumber_Object = MibTableColumn
cubominiOptIdentVendorSerialNumber = _CubominiOptIdentVendorSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 27894, 11, 241, 1, 5, 3, 1, 6),
    _CubominiOptIdentVendorSerialNumber_Type()
)
cubominiOptIdentVendorSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cubominiOptIdentVendorSerialNumber.setStatus("current")
_CubominiOptIdentNominalWavelength_Type = Integer32
_CubominiOptIdentNominalWavelength_Object = MibTableColumn
cubominiOptIdentNominalWavelength = _CubominiOptIdentNominalWavelength_Object(
    (1, 3, 6, 1, 4, 1, 27894, 11, 241, 1, 5, 3, 1, 7),
    _CubominiOptIdentNominalWavelength_Type()
)
cubominiOptIdentNominalWavelength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cubominiOptIdentNominalWavelength.setStatus("current")
if mibBuilder.loadTexts:
    cubominiOptIdentNominalWavelength.setUnits("Hundredths (1/100) of a nanometer")
_CubominiDnsServerTable_Object = MibTable
cubominiDnsServerTable = _CubominiDnsServerTable_Object(
    (1, 3, 6, 1, 4, 1, 27894, 11, 241, 1, 5, 4)
)
if mibBuilder.loadTexts:
    cubominiDnsServerTable.setStatus("current")
_CubominiDnsServerEntry_Object = MibTableRow
cubominiDnsServerEntry = _CubominiDnsServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 27894, 11, 241, 1, 5, 4, 1)
)
cubominiDnsServerEntry.setIndexNames(
    (0, "CUBO-MINI-MIB", "cubominiDnsServerChassisId"),
    (0, "CUBO-MINI-MIB", "cubominiDnsServerDnsindexId"),
)
if mibBuilder.loadTexts:
    cubominiDnsServerEntry.setStatus("current")


class _CubominiDnsServerChassisId_Type(Integer32):
    """Custom type cubominiDnsServerChassisId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CubominiDnsServerChassisId_Type.__name__ = "Integer32"
_CubominiDnsServerChassisId_Object = MibTableColumn
cubominiDnsServerChassisId = _CubominiDnsServerChassisId_Object(
    (1, 3, 6, 1, 4, 1, 27894, 11, 241, 1, 5, 4, 1, 1),
    _CubominiDnsServerChassisId_Type()
)
cubominiDnsServerChassisId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cubominiDnsServerChassisId.setStatus("current")


class _CubominiDnsServerDnsindexId_Type(Integer32):
    """Custom type cubominiDnsServerDnsindexId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CubominiDnsServerDnsindexId_Type.__name__ = "Integer32"
_CubominiDnsServerDnsindexId_Object = MibTableColumn
cubominiDnsServerDnsindexId = _CubominiDnsServerDnsindexId_Object(
    (1, 3, 6, 1, 4, 1, 27894, 11, 241, 1, 5, 4, 1, 2),
    _CubominiDnsServerDnsindexId_Type()
)
cubominiDnsServerDnsindexId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cubominiDnsServerDnsindexId.setStatus("current")


class _CubominiDnsServerIpAddress_Type(OctetString):
    """Custom type cubominiDnsServerIpAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(15, 15),
    )
    fixed_length = 15


_CubominiDnsServerIpAddress_Type.__name__ = "OctetString"
_CubominiDnsServerIpAddress_Object = MibTableColumn
cubominiDnsServerIpAddress = _CubominiDnsServerIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 27894, 11, 241, 1, 5, 4, 1, 3),
    _CubominiDnsServerIpAddress_Type()
)
cubominiDnsServerIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cubominiDnsServerIpAddress.setStatus("current")
_CubominiNtpServerGroup_ObjectIdentity = ObjectIdentity
cubominiNtpServerGroup = _CubominiNtpServerGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27894, 11, 241, 1, 5, 5)
)
_CubominiNtpServerParamsTable_Object = MibTable
cubominiNtpServerParamsTable = _CubominiNtpServerParamsTable_Object(
    (1, 3, 6, 1, 4, 1, 27894, 11, 241, 1, 5, 5, 1)
)
if mibBuilder.loadTexts:
    cubominiNtpServerParamsTable.setStatus("current")
_CubominiNtpServerParamsEntry_Object = MibTableRow
cubominiNtpServerParamsEntry = _CubominiNtpServerParamsEntry_Object(
    (1, 3, 6, 1, 4, 1, 27894, 11, 241, 1, 5, 5, 1, 1)
)
cubominiNtpServerParamsEntry.setIndexNames(
    (0, "CUBO-MINI-MIB", "cubominiNtpServerParamsChassisId"),
)
if mibBuilder.loadTexts:
    cubominiNtpServerParamsEntry.setStatus("current")


class _CubominiNtpServerParamsChassisId_Type(Integer32):
    """Custom type cubominiNtpServerParamsChassisId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CubominiNtpServerParamsChassisId_Type.__name__ = "Integer32"
_CubominiNtpServerParamsChassisId_Object = MibTableColumn
cubominiNtpServerParamsChassisId = _CubominiNtpServerParamsChassisId_Object(
    (1, 3, 6, 1, 4, 1, 27894, 11, 241, 1, 5, 5, 1, 1, 1),
    _CubominiNtpServerParamsChassisId_Type()
)
cubominiNtpServerParamsChassisId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cubominiNtpServerParamsChassisId.setStatus("current")


class _CubominiNtpServerParamsActive_Type(Integer32):
    """Custom type cubominiNtpServerParamsActive based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("inactive", 2),
          ("active", 3))
    )


_CubominiNtpServerParamsActive_Type.__name__ = "Integer32"
_CubominiNtpServerParamsActive_Object = MibTableColumn
cubominiNtpServerParamsActive = _CubominiNtpServerParamsActive_Object(
    (1, 3, 6, 1, 4, 1, 27894, 11, 241, 1, 5, 5, 1, 1, 2),
    _CubominiNtpServerParamsActive_Type()
)
cubominiNtpServerParamsActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cubominiNtpServerParamsActive.setStatus("current")
_CubominiNtpServerTable_Object = MibTable
cubominiNtpServerTable = _CubominiNtpServerTable_Object(
    (1, 3, 6, 1, 4, 1, 27894, 11, 241, 1, 5, 5, 2)
)
if mibBuilder.loadTexts:
    cubominiNtpServerTable.setStatus("current")
_CubominiNtpServerEntry_Object = MibTableRow
cubominiNtpServerEntry = _CubominiNtpServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 27894, 11, 241, 1, 5, 5, 2, 1)
)
cubominiNtpServerEntry.setIndexNames(
    (0, "CUBO-MINI-MIB", "cubominiNtpServerChassisId"),
    (0, "CUBO-MINI-MIB", "cubominiNtpServerNtpindexId"),
)
if mibBuilder.loadTexts:
    cubominiNtpServerEntry.setStatus("current")


class _CubominiNtpServerChassisId_Type(Integer32):
    """Custom type cubominiNtpServerChassisId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CubominiNtpServerChassisId_Type.__name__ = "Integer32"
_CubominiNtpServerChassisId_Object = MibTableColumn
cubominiNtpServerChassisId = _CubominiNtpServerChassisId_Object(
    (1, 3, 6, 1, 4, 1, 27894, 11, 241, 1, 5, 5, 2, 1, 1),
    _CubominiNtpServerChassisId_Type()
)
cubominiNtpServerChassisId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cubominiNtpServerChassisId.setStatus("current")


class _CubominiNtpServerNtpindexId_Type(Integer32):
    """Custom type cubominiNtpServerNtpindexId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CubominiNtpServerNtpindexId_Type.__name__ = "Integer32"
_CubominiNtpServerNtpindexId_Object = MibTableColumn
cubominiNtpServerNtpindexId = _CubominiNtpServerNtpindexId_Object(
    (1, 3, 6, 1, 4, 1, 27894, 11, 241, 1, 5, 5, 2, 1, 2),
    _CubominiNtpServerNtpindexId_Type()
)
cubominiNtpServerNtpindexId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cubominiNtpServerNtpindexId.setStatus("current")


class _CubominiNtpServerIPAddress_Type(OctetString):
    """Custom type cubominiNtpServerIPAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(15, 15),
    )
    fixed_length = 15


_CubominiNtpServerIPAddress_Type.__name__ = "OctetString"
_CubominiNtpServerIPAddress_Object = MibTableColumn
cubominiNtpServerIPAddress = _CubominiNtpServerIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 27894, 11, 241, 1, 5, 5, 2, 1, 3),
    _CubominiNtpServerIPAddress_Type()
)
cubominiNtpServerIPAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cubominiNtpServerIPAddress.setStatus("current")
_CubominiXcvrGroup_ObjectIdentity = ObjectIdentity
cubominiXcvrGroup = _CubominiXcvrGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27894, 11, 241, 1, 9)
)
_CubominiXcvrCommonConfigTable_Object = MibTable
cubominiXcvrCommonConfigTable = _CubominiXcvrCommonConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 27894, 11, 241, 1, 9, 1)
)
if mibBuilder.loadTexts:
    cubominiXcvrCommonConfigTable.setStatus("current")
_CubominiXcvrCommonConfigEntry_Object = MibTableRow
cubominiXcvrCommonConfigEntry = _CubominiXcvrCommonConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 27894, 11, 241, 1, 9, 1, 1)
)
cubominiXcvrCommonConfigEntry.setIndexNames(
    (0, "CUBO-MINI-MIB", "cubominiXcvrCommonConfigChassisId"),
    (0, "CUBO-MINI-MIB", "cubominiXcvrCommonConfigSlotId"),
)
if mibBuilder.loadTexts:
    cubominiXcvrCommonConfigEntry.setStatus("current")


class _CubominiXcvrCommonConfigChassisId_Type(Integer32):
    """Custom type cubominiXcvrCommonConfigChassisId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CubominiXcvrCommonConfigChassisId_Type.__name__ = "Integer32"
_CubominiXcvrCommonConfigChassisId_Object = MibTableColumn
cubominiXcvrCommonConfigChassisId = _CubominiXcvrCommonConfigChassisId_Object(
    (1, 3, 6, 1, 4, 1, 27894, 11, 241, 1, 9, 1, 1, 1),
    _CubominiXcvrCommonConfigChassisId_Type()
)
cubominiXcvrCommonConfigChassisId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cubominiXcvrCommonConfigChassisId.setStatus("current")


class _CubominiXcvrCommonConfigSlotId_Type(Integer32):
    """Custom type cubominiXcvrCommonConfigSlotId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CubominiXcvrCommonConfigSlotId_Type.__name__ = "Integer32"
_CubominiXcvrCommonConfigSlotId_Object = MibTableColumn
cubominiXcvrCommonConfigSlotId = _CubominiXcvrCommonConfigSlotId_Object(
    (1, 3, 6, 1, 4, 1, 27894, 11, 241, 1, 9, 1, 1, 2),
    _CubominiXcvrCommonConfigSlotId_Type()
)
cubominiXcvrCommonConfigSlotId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cubominiXcvrCommonConfigSlotId.setStatus("current")


class _CubominiXcvrCommonConfigLoopbackOperation_Type(Integer32):
    """Custom type cubominiXcvrCommonConfigLoopbackOperation based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 3))
    )


_CubominiXcvrCommonConfigLoopbackOperation_Type.__name__ = "Integer32"
_CubominiXcvrCommonConfigLoopbackOperation_Object = MibTableColumn
cubominiXcvrCommonConfigLoopbackOperation = _CubominiXcvrCommonConfigLoopbackOperation_Object(
    (1, 3, 6, 1, 4, 1, 27894, 11, 241, 1, 9, 1, 1, 3),
    _CubominiXcvrCommonConfigLoopbackOperation_Type()
)
cubominiXcvrCommonConfigLoopbackOperation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cubominiXcvrCommonConfigLoopbackOperation.setStatus("current")


class _CubominiXcvrCommonConfigLoopbackTimeout_Type(Integer32):
    """Custom type cubominiXcvrCommonConfigLoopbackTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483),
    )


_CubominiXcvrCommonConfigLoopbackTimeout_Type.__name__ = "Integer32"
_CubominiXcvrCommonConfigLoopbackTimeout_Object = MibTableColumn
cubominiXcvrCommonConfigLoopbackTimeout = _CubominiXcvrCommonConfigLoopbackTimeout_Object(
    (1, 3, 6, 1, 4, 1, 27894, 11, 241, 1, 9, 1, 1, 4),
    _CubominiXcvrCommonConfigLoopbackTimeout_Type()
)
cubominiXcvrCommonConfigLoopbackTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cubominiXcvrCommonConfigLoopbackTimeout.setStatus("current")
if mibBuilder.loadTexts:
    cubominiXcvrCommonConfigLoopbackTimeout.setUnits("Seconds")


class _CubominiXcvrCommonConfigDataRateSet_Type(Integer32):
    """Custom type cubominiXcvrCommonConfigDataRateSet based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("dr40gbps", 2),
          ("dr100gbps", 3),
          ("drotu4", 4))
    )


_CubominiXcvrCommonConfigDataRateSet_Type.__name__ = "Integer32"
_CubominiXcvrCommonConfigDataRateSet_Object = MibTableColumn
cubominiXcvrCommonConfigDataRateSet = _CubominiXcvrCommonConfigDataRateSet_Object(
    (1, 3, 6, 1, 4, 1, 27894, 11, 241, 1, 9, 1, 1, 5),
    _CubominiXcvrCommonConfigDataRateSet_Type()
)
cubominiXcvrCommonConfigDataRateSet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cubominiXcvrCommonConfigDataRateSet.setStatus("current")


class _CubominiXcvrCommonConfigLinkLossFwd_Type(Integer32):
    """Custom type cubominiXcvrCommonConfigLinkLossFwd based on Integer32"""
    defaultValue = 1

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
        *(("llfOff", 1),
          ("llfLn2Cl", 2),
          ("llfCl2Ln", 3),
          ("llfBidir", 4))
    )


_CubominiXcvrCommonConfigLinkLossFwd_Type.__name__ = "Integer32"
_CubominiXcvrCommonConfigLinkLossFwd_Object = MibTableColumn
cubominiXcvrCommonConfigLinkLossFwd = _CubominiXcvrCommonConfigLinkLossFwd_Object(
    (1, 3, 6, 1, 4, 1, 27894, 11, 241, 1, 9, 1, 1, 6),
    _CubominiXcvrCommonConfigLinkLossFwd_Type()
)
cubominiXcvrCommonConfigLinkLossFwd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cubominiXcvrCommonConfigLinkLossFwd.setStatus("current")
_CubominiXcvrGeneralTable_Object = MibTable
cubominiXcvrGeneralTable = _CubominiXcvrGeneralTable_Object(
    (1, 3, 6, 1, 4, 1, 27894, 11, 241, 1, 9, 2)
)
if mibBuilder.loadTexts:
    cubominiXcvrGeneralTable.setStatus("current")
_CubominiXcvrGeneralEntry_Object = MibTableRow
cubominiXcvrGeneralEntry = _CubominiXcvrGeneralEntry_Object(
    (1, 3, 6, 1, 4, 1, 27894, 11, 241, 1, 9, 2, 1)
)
cubominiXcvrGeneralEntry.setIndexNames(
    (0, "CUBO-MINI-MIB", "cubominiXcvrGeneralChassisId"),
    (0, "CUBO-MINI-MIB", "cubominiXcvrGeneralSlotId"),
    (0, "CUBO-MINI-MIB", "cubominiXcvrGeneralPortId"),
)
if mibBuilder.loadTexts:
    cubominiXcvrGeneralEntry.setStatus("current")


class _CubominiXcvrGeneralChassisId_Type(Integer32):
    """Custom type cubominiXcvrGeneralChassisId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CubominiXcvrGeneralChassisId_Type.__name__ = "Integer32"
_CubominiXcvrGeneralChassisId_Object = MibTableColumn
cubominiXcvrGeneralChassisId = _CubominiXcvrGeneralChassisId_Object(
    (1, 3, 6, 1, 4, 1, 27894, 11, 241, 1, 9, 2, 1, 1),
    _CubominiXcvrGeneralChassisId_Type()
)
cubominiXcvrGeneralChassisId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cubominiXcvrGeneralChassisId.setStatus("current")


class _CubominiXcvrGeneralSlotId_Type(Integer32):
    """Custom type cubominiXcvrGeneralSlotId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CubominiXcvrGeneralSlotId_Type.__name__ = "Integer32"
_CubominiXcvrGeneralSlotId_Object = MibTableColumn
cubominiXcvrGeneralSlotId = _CubominiXcvrGeneralSlotId_Object(
    (1, 3, 6, 1, 4, 1, 27894, 11, 241, 1, 9, 2, 1, 2),
    _CubominiXcvrGeneralSlotId_Type()
)
cubominiXcvrGeneralSlotId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cubominiXcvrGeneralSlotId.setStatus("current")


class _CubominiXcvrGeneralPortId_Type(Integer32):
    """Custom type cubominiXcvrGeneralPortId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CubominiXcvrGeneralPortId_Type.__name__ = "Integer32"
_CubominiXcvrGeneralPortId_Object = MibTableColumn
cubominiXcvrGeneralPortId = _CubominiXcvrGeneralPortId_Object(
    (1, 3, 6, 1, 4, 1, 27894, 11, 241, 1, 9, 2, 1, 3),
    _CubominiXcvrGeneralPortId_Type()
)
cubominiXcvrGeneralPortId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cubominiXcvrGeneralPortId.setStatus("current")


class _CubominiXcvrGeneralIsInserted_Type(Integer32):
    """Custom type cubominiXcvrGeneralIsInserted based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("notInserted", 2),
          ("inserted", 3))
    )


_CubominiXcvrGeneralIsInserted_Type.__name__ = "Integer32"
_CubominiXcvrGeneralIsInserted_Object = MibTableColumn
cubominiXcvrGeneralIsInserted = _CubominiXcvrGeneralIsInserted_Object(
    (1, 3, 6, 1, 4, 1, 27894, 11, 241, 1, 9, 2, 1, 4),
    _CubominiXcvrGeneralIsInserted_Type()
)
cubominiXcvrGeneralIsInserted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cubominiXcvrGeneralIsInserted.setStatus("current")


class _CubominiXcvrGeneralEventsStatusAll_Type(OctetString):
    """Custom type cubominiXcvrGeneralEventsStatusAll based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(10, 10),
    )
    fixed_length = 10


_CubominiXcvrGeneralEventsStatusAll_Type.__name__ = "OctetString"
_CubominiXcvrGeneralEventsStatusAll_Object = MibTableColumn
cubominiXcvrGeneralEventsStatusAll = _CubominiXcvrGeneralEventsStatusAll_Object(
    (1, 3, 6, 1, 4, 1, 27894, 11, 241, 1, 9, 2, 1, 5),
    _CubominiXcvrGeneralEventsStatusAll_Type()
)
cubominiXcvrGeneralEventsStatusAll.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cubominiXcvrGeneralEventsStatusAll.setStatus("current")


class _CubominiXcvrGeneralCDRPortEventsStatusAll_Type(OctetString):
    """Custom type cubominiXcvrGeneralCDRPortEventsStatusAll based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )
    fixed_length = 2


_CubominiXcvrGeneralCDRPortEventsStatusAll_Type.__name__ = "OctetString"
_CubominiXcvrGeneralCDRPortEventsStatusAll_Object = MibTableColumn
cubominiXcvrGeneralCDRPortEventsStatusAll = _CubominiXcvrGeneralCDRPortEventsStatusAll_Object(
    (1, 3, 6, 1, 4, 1, 27894, 11, 241, 1, 9, 2, 1, 6),
    _CubominiXcvrGeneralCDRPortEventsStatusAll_Type()
)
cubominiXcvrGeneralCDRPortEventsStatusAll.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cubominiXcvrGeneralCDRPortEventsStatusAll.setStatus("current")


class _CubominiXcvrGeneralTxForceMode_Type(Integer32):
    """Custom type cubominiXcvrGeneralTxForceMode based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 3))
    )


_CubominiXcvrGeneralTxForceMode_Type.__name__ = "Integer32"
_CubominiXcvrGeneralTxForceMode_Object = MibTableColumn
cubominiXcvrGeneralTxForceMode = _CubominiXcvrGeneralTxForceMode_Object(
    (1, 3, 6, 1, 4, 1, 27894, 11, 241, 1, 9, 2, 1, 7),
    _CubominiXcvrGeneralTxForceMode_Type()
)
cubominiXcvrGeneralTxForceMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cubominiXcvrGeneralTxForceMode.setStatus("current")
_CubominiXcvrIdentTable_Object = MibTable
cubominiXcvrIdentTable = _CubominiXcvrIdentTable_Object(
    (1, 3, 6, 1, 4, 1, 27894, 11, 241, 1, 9, 3)
)
if mibBuilder.loadTexts:
    cubominiXcvrIdentTable.setStatus("current")
_CubominiXcvrIdentEntry_Object = MibTableRow
cubominiXcvrIdentEntry = _CubominiXcvrIdentEntry_Object(
    (1, 3, 6, 1, 4, 1, 27894, 11, 241, 1, 9, 3, 1)
)
cubominiXcvrIdentEntry.setIndexNames(
    (0, "CUBO-MINI-MIB", "cubominiXcvrIdentChassisId"),
    (0, "CUBO-MINI-MIB", "cubominiXcvrIdentSlotId"),
    (0, "CUBO-MINI-MIB", "cubominiXcvrIdentPortId"),
)
if mibBuilder.loadTexts:
    cubominiXcvrIdentEntry.setStatus("current")


class _CubominiXcvrIdentChassisId_Type(Integer32):
    """Custom type cubominiXcvrIdentChassisId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CubominiXcvrIdentChassisId_Type.__name__ = "Integer32"
_CubominiXcvrIdentChassisId_Object = MibTableColumn
cubominiXcvrIdentChassisId = _CubominiXcvrIdentChassisId_Object(
    (1, 3, 6, 1, 4, 1, 27894, 11, 241, 1, 9, 3, 1, 1),
    _CubominiXcvrIdentChassisId_Type()
)
cubominiXcvrIdentChassisId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cubominiXcvrIdentChassisId.setStatus("current")


class _CubominiXcvrIdentSlotId_Type(Integer32):
    """Custom type cubominiXcvrIdentSlotId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CubominiXcvrIdentSlotId_Type.__name__ = "Integer32"
_CubominiXcvrIdentSlotId_Object = MibTableColumn
cubominiXcvrIdentSlotId = _CubominiXcvrIdentSlotId_Object(
    (1, 3, 6, 1, 4, 1, 27894, 11, 241, 1, 9, 3, 1, 2),
    _CubominiXcvrIdentSlotId_Type()
)
cubominiXcvrIdentSlotId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cubominiXcvrIdentSlotId.setStatus("current")


class _CubominiXcvrIdentPortId_Type(Integer32):
    """Custom type cubominiXcvrIdentPortId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CubominiXcvrIdentPortId_Type.__name__ = "Integer32"
_CubominiXcvrIdentPortId_Object = MibTableColumn
cubominiXcvrIdentPortId = _CubominiXcvrIdentPortId_Object(
    (1, 3, 6, 1, 4, 1, 27894, 11, 241, 1, 9, 3, 1, 3),
    _CubominiXcvrIdentPortId_Type()
)
cubominiXcvrIdentPortId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cubominiXcvrIdentPortId.setStatus("current")


class _CubominiXcvrIdentVendorName_Type(OctetString):
    """Custom type cubominiXcvrIdentVendorName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )
    fixed_length = 16


_CubominiXcvrIdentVendorName_Type.__name__ = "OctetString"
_CubominiXcvrIdentVendorName_Object = MibTableColumn
cubominiXcvrIdentVendorName = _CubominiXcvrIdentVendorName_Object(
    (1, 3, 6, 1, 4, 1, 27894, 11, 241, 1, 9, 3, 1, 4),
    _CubominiXcvrIdentVendorName_Type()
)
cubominiXcvrIdentVendorName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cubominiXcvrIdentVendorName.setStatus("current")


class _CubominiXcvrIdentVendorPartNumber_Type(OctetString):
    """Custom type cubominiXcvrIdentVendorPartNumber based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )
    fixed_length = 16


_CubominiXcvrIdentVendorPartNumber_Type.__name__ = "OctetString"
_CubominiXcvrIdentVendorPartNumber_Object = MibTableColumn
cubominiXcvrIdentVendorPartNumber = _CubominiXcvrIdentVendorPartNumber_Object(
    (1, 3, 6, 1, 4, 1, 27894, 11, 241, 1, 9, 3, 1, 5),
    _CubominiXcvrIdentVendorPartNumber_Type()
)
cubominiXcvrIdentVendorPartNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cubominiXcvrIdentVendorPartNumber.setStatus("current")


class _CubominiXcvrIdentVendorSerialNumber_Type(OctetString):
    """Custom type cubominiXcvrIdentVendorSerialNumber based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )
    fixed_length = 16


_CubominiXcvrIdentVendorSerialNumber_Type.__name__ = "OctetString"
_CubominiXcvrIdentVendorSerialNumber_Object = MibTableColumn
cubominiXcvrIdentVendorSerialNumber = _CubominiXcvrIdentVendorSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 27894, 11, 241, 1, 9, 3, 1, 6),
    _CubominiXcvrIdentVendorSerialNumber_Type()
)
cubominiXcvrIdentVendorSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cubominiXcvrIdentVendorSerialNumber.setStatus("current")
_CubominiXcvrIdentNominalWavelength_Type = Integer32
_CubominiXcvrIdentNominalWavelength_Object = MibTableColumn
cubominiXcvrIdentNominalWavelength = _CubominiXcvrIdentNominalWavelength_Object(
    (1, 3, 6, 1, 4, 1, 27894, 11, 241, 1, 9, 3, 1, 7),
    _CubominiXcvrIdentNominalWavelength_Type()
)
cubominiXcvrIdentNominalWavelength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cubominiXcvrIdentNominalWavelength.setStatus("current")
if mibBuilder.loadTexts:
    cubominiXcvrIdentNominalWavelength.setUnits("Hundredths (1/100) of a nanometer")
_CubominiXcvrEvThresholdTable_Object = MibTable
cubominiXcvrEvThresholdTable = _CubominiXcvrEvThresholdTable_Object(
    (1, 3, 6, 1, 4, 1, 27894, 11, 241, 1, 9, 4)
)
if mibBuilder.loadTexts:
    cubominiXcvrEvThresholdTable.setStatus("current")
_CubominiXcvrEvThresholdEntry_Object = MibTableRow
cubominiXcvrEvThresholdEntry = _CubominiXcvrEvThresholdEntry_Object(
    (1, 3, 6, 1, 4, 1, 27894, 11, 241, 1, 9, 4, 1)
)
cubominiXcvrEvThresholdEntry.setIndexNames(
    (0, "CUBO-MINI-MIB", "cubominiXcvrEvThresholdChassisId"),
    (0, "CUBO-MINI-MIB", "cubominiXcvrEvThresholdSlotId"),
    (0, "CUBO-MINI-MIB", "cubominiXcvrEvThresholdPortId"),
)
if mibBuilder.loadTexts:
    cubominiXcvrEvThresholdEntry.setStatus("current")


class _CubominiXcvrEvThresholdChassisId_Type(Integer32):
    """Custom type cubominiXcvrEvThresholdChassisId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CubominiXcvrEvThresholdChassisId_Type.__name__ = "Integer32"
_CubominiXcvrEvThresholdChassisId_Object = MibTableColumn
cubominiXcvrEvThresholdChassisId = _CubominiXcvrEvThresholdChassisId_Object(
    (1, 3, 6, 1, 4, 1, 27894, 11, 241, 1, 9, 4, 1, 1),
    _CubominiXcvrEvThresholdChassisId_Type()
)
cubominiXcvrEvThresholdChassisId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cubominiXcvrEvThresholdChassisId.setStatus("current")


class _CubominiXcvrEvThresholdSlotId_Type(Integer32):
    """Custom type cubominiXcvrEvThresholdSlotId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CubominiXcvrEvThresholdSlotId_Type.__name__ = "Integer32"
_CubominiXcvrEvThresholdSlotId_Object = MibTableColumn
cubominiXcvrEvThresholdSlotId = _CubominiXcvrEvThresholdSlotId_Object(
    (1, 3, 6, 1, 4, 1, 27894, 11, 241, 1, 9, 4, 1, 2),
    _CubominiXcvrEvThresholdSlotId_Type()
)
cubominiXcvrEvThresholdSlotId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cubominiXcvrEvThresholdSlotId.setStatus("current")


class _CubominiXcvrEvThresholdPortId_Type(Integer32):
    """Custom type cubominiXcvrEvThresholdPortId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CubominiXcvrEvThresholdPortId_Type.__name__ = "Integer32"
_CubominiXcvrEvThresholdPortId_Object = MibTableColumn
cubominiXcvrEvThresholdPortId = _CubominiXcvrEvThresholdPortId_Object(
    (1, 3, 6, 1, 4, 1, 27894, 11, 241, 1, 9, 4, 1, 3),
    _CubominiXcvrEvThresholdPortId_Type()
)
cubominiXcvrEvThresholdPortId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cubominiXcvrEvThresholdPortId.setStatus("current")


class _CubominiXcvrEvThresholdMinInputPower_Type(Integer32):
    """Custom type cubominiXcvrEvThresholdMinInputPower based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-400, 82),
    )


_CubominiXcvrEvThresholdMinInputPower_Type.__name__ = "Integer32"
_CubominiXcvrEvThresholdMinInputPower_Object = MibTableColumn
cubominiXcvrEvThresholdMinInputPower = _CubominiXcvrEvThresholdMinInputPower_Object(
    (1, 3, 6, 1, 4, 1, 27894, 11, 241, 1, 9, 4, 1, 4),
    _CubominiXcvrEvThresholdMinInputPower_Type()
)
cubominiXcvrEvThresholdMinInputPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cubominiXcvrEvThresholdMinInputPower.setStatus("current")
if mibBuilder.loadTexts:
    cubominiXcvrEvThresholdMinInputPower.setUnits("Tenths (1/10) of dBm")


class _CubominiXcvrEvThresholdMaxInputPower_Type(Integer32):
    """Custom type cubominiXcvrEvThresholdMaxInputPower based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-400, 82),
    )


_CubominiXcvrEvThresholdMaxInputPower_Type.__name__ = "Integer32"
_CubominiXcvrEvThresholdMaxInputPower_Object = MibTableColumn
cubominiXcvrEvThresholdMaxInputPower = _CubominiXcvrEvThresholdMaxInputPower_Object(
    (1, 3, 6, 1, 4, 1, 27894, 11, 241, 1, 9, 4, 1, 5),
    _CubominiXcvrEvThresholdMaxInputPower_Type()
)
cubominiXcvrEvThresholdMaxInputPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cubominiXcvrEvThresholdMaxInputPower.setStatus("current")
if mibBuilder.loadTexts:
    cubominiXcvrEvThresholdMaxInputPower.setUnits("Tenths (1/10) of dBm")


class _CubominiXcvrEvThresholdMinOutputPower_Type(Integer32):
    """Custom type cubominiXcvrEvThresholdMinOutputPower based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-400, 82),
    )


_CubominiXcvrEvThresholdMinOutputPower_Type.__name__ = "Integer32"
_CubominiXcvrEvThresholdMinOutputPower_Object = MibTableColumn
cubominiXcvrEvThresholdMinOutputPower = _CubominiXcvrEvThresholdMinOutputPower_Object(
    (1, 3, 6, 1, 4, 1, 27894, 11, 241, 1, 9, 4, 1, 6),
    _CubominiXcvrEvThresholdMinOutputPower_Type()
)
cubominiXcvrEvThresholdMinOutputPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cubominiXcvrEvThresholdMinOutputPower.setStatus("current")
if mibBuilder.loadTexts:
    cubominiXcvrEvThresholdMinOutputPower.setUnits("Tenths (1/10) of dBm")


class _CubominiXcvrEvThresholdMaxOutputPower_Type(Integer32):
    """Custom type cubominiXcvrEvThresholdMaxOutputPower based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-400, 82),
    )


_CubominiXcvrEvThresholdMaxOutputPower_Type.__name__ = "Integer32"
_CubominiXcvrEvThresholdMaxOutputPower_Object = MibTableColumn
cubominiXcvrEvThresholdMaxOutputPower = _CubominiXcvrEvThresholdMaxOutputPower_Object(
    (1, 3, 6, 1, 4, 1, 27894, 11, 241, 1, 9, 4, 1, 7),
    _CubominiXcvrEvThresholdMaxOutputPower_Type()
)
cubominiXcvrEvThresholdMaxOutputPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cubominiXcvrEvThresholdMaxOutputPower.setStatus("current")
if mibBuilder.loadTexts:
    cubominiXcvrEvThresholdMaxOutputPower.setUnits("Tenths (1/10) of dBm")
_CubominiXcvrDiagnosticsTable_Object = MibTable
cubominiXcvrDiagnosticsTable = _CubominiXcvrDiagnosticsTable_Object(
    (1, 3, 6, 1, 4, 1, 27894, 11, 241, 1, 9, 5)
)
if mibBuilder.loadTexts:
    cubominiXcvrDiagnosticsTable.setStatus("current")
_CubominiXcvrDiagnosticsEntry_Object = MibTableRow
cubominiXcvrDiagnosticsEntry = _CubominiXcvrDiagnosticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 27894, 11, 241, 1, 9, 5, 1)
)
cubominiXcvrDiagnosticsEntry.setIndexNames(
    (0, "CUBO-MINI-MIB", "cubominiXcvrDiagnosticsChassisId"),
    (0, "CUBO-MINI-MIB", "cubominiXcvrDiagnosticsSlotId"),
    (0, "CUBO-MINI-MIB", "cubominiXcvrDiagnosticsPortId"),
)
if mibBuilder.loadTexts:
    cubominiXcvrDiagnosticsEntry.setStatus("current")


class _CubominiXcvrDiagnosticsChassisId_Type(Integer32):
    """Custom type cubominiXcvrDiagnosticsChassisId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CubominiXcvrDiagnosticsChassisId_Type.__name__ = "Integer32"
_CubominiXcvrDiagnosticsChassisId_Object = MibTableColumn
cubominiXcvrDiagnosticsChassisId = _CubominiXcvrDiagnosticsChassisId_Object(
    (1, 3, 6, 1, 4, 1, 27894, 11, 241, 1, 9, 5, 1, 1),
    _CubominiXcvrDiagnosticsChassisId_Type()
)
cubominiXcvrDiagnosticsChassisId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cubominiXcvrDiagnosticsChassisId.setStatus("current")


class _CubominiXcvrDiagnosticsSlotId_Type(Integer32):
    """Custom type cubominiXcvrDiagnosticsSlotId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CubominiXcvrDiagnosticsSlotId_Type.__name__ = "Integer32"
_CubominiXcvrDiagnosticsSlotId_Object = MibTableColumn
cubominiXcvrDiagnosticsSlotId = _CubominiXcvrDiagnosticsSlotId_Object(
    (1, 3, 6, 1, 4, 1, 27894, 11, 241, 1, 9, 5, 1, 2),
    _CubominiXcvrDiagnosticsSlotId_Type()
)
cubominiXcvrDiagnosticsSlotId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cubominiXcvrDiagnosticsSlotId.setStatus("current")


class _CubominiXcvrDiagnosticsPortId_Type(Integer32):
    """Custom type cubominiXcvrDiagnosticsPortId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CubominiXcvrDiagnosticsPortId_Type.__name__ = "Integer32"
_CubominiXcvrDiagnosticsPortId_Object = MibTableColumn
cubominiXcvrDiagnosticsPortId = _CubominiXcvrDiagnosticsPortId_Object(
    (1, 3, 6, 1, 4, 1, 27894, 11, 241, 1, 9, 5, 1, 3),
    _CubominiXcvrDiagnosticsPortId_Type()
)
cubominiXcvrDiagnosticsPortId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cubominiXcvrDiagnosticsPortId.setStatus("current")


class _CubominiXcvrDiagnosticsTemperature_Type(Integer32):
    """Custom type cubominiXcvrDiagnosticsTemperature based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1280, 1279),
    )


_CubominiXcvrDiagnosticsTemperature_Type.__name__ = "Integer32"
_CubominiXcvrDiagnosticsTemperature_Object = MibTableColumn
cubominiXcvrDiagnosticsTemperature = _CubominiXcvrDiagnosticsTemperature_Object(
    (1, 3, 6, 1, 4, 1, 27894, 11, 241, 1, 9, 5, 1, 4),
    _CubominiXcvrDiagnosticsTemperature_Type()
)
cubominiXcvrDiagnosticsTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cubominiXcvrDiagnosticsTemperature.setStatus("current")
if mibBuilder.loadTexts:
    cubominiXcvrDiagnosticsTemperature.setUnits("Tenths (1/10) of Celsius degrees")


class _CubominiXcvrDiagnosticsTxPowerAll_Type(Integer32):
    """Custom type cubominiXcvrDiagnosticsTxPowerAll based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-400, 82),
    )


_CubominiXcvrDiagnosticsTxPowerAll_Type.__name__ = "Integer32"
_CubominiXcvrDiagnosticsTxPowerAll_Object = MibTableColumn
cubominiXcvrDiagnosticsTxPowerAll = _CubominiXcvrDiagnosticsTxPowerAll_Object(
    (1, 3, 6, 1, 4, 1, 27894, 11, 241, 1, 9, 5, 1, 5),
    _CubominiXcvrDiagnosticsTxPowerAll_Type()
)
cubominiXcvrDiagnosticsTxPowerAll.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cubominiXcvrDiagnosticsTxPowerAll.setStatus("current")
if mibBuilder.loadTexts:
    cubominiXcvrDiagnosticsTxPowerAll.setUnits("Tenths (1/10) of dBm")


class _CubominiXcvrDiagnosticsRxPowerAll_Type(Integer32):
    """Custom type cubominiXcvrDiagnosticsRxPowerAll based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-400, 82),
    )


_CubominiXcvrDiagnosticsRxPowerAll_Type.__name__ = "Integer32"
_CubominiXcvrDiagnosticsRxPowerAll_Object = MibTableColumn
cubominiXcvrDiagnosticsRxPowerAll = _CubominiXcvrDiagnosticsRxPowerAll_Object(
    (1, 3, 6, 1, 4, 1, 27894, 11, 241, 1, 9, 5, 1, 6),
    _CubominiXcvrDiagnosticsRxPowerAll_Type()
)
cubominiXcvrDiagnosticsRxPowerAll.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cubominiXcvrDiagnosticsRxPowerAll.setStatus("current")
if mibBuilder.loadTexts:
    cubominiXcvrDiagnosticsRxPowerAll.setUnits("Tenths (1/10) of dBm")
_CubominiXcvrOptChannelsTable_Object = MibTable
cubominiXcvrOptChannelsTable = _CubominiXcvrOptChannelsTable_Object(
    (1, 3, 6, 1, 4, 1, 27894, 11, 241, 1, 9, 6)
)
if mibBuilder.loadTexts:
    cubominiXcvrOptChannelsTable.setStatus("current")
_CubominiXcvrOptChannelsEntry_Object = MibTableRow
cubominiXcvrOptChannelsEntry = _CubominiXcvrOptChannelsEntry_Object(
    (1, 3, 6, 1, 4, 1, 27894, 11, 241, 1, 9, 6, 1)
)
cubominiXcvrOptChannelsEntry.setIndexNames(
    (0, "CUBO-MINI-MIB", "cubominiXcvrOptChannelsChassisId"),
    (0, "CUBO-MINI-MIB", "cubominiXcvrOptChannelsSlotId"),
    (0, "CUBO-MINI-MIB", "cubominiXcvrOptChannelsPortId"),
    (0, "CUBO-MINI-MIB", "cubominiXcvrOptChannelsChannelId"),
)
if mibBuilder.loadTexts:
    cubominiXcvrOptChannelsEntry.setStatus("current")


class _CubominiXcvrOptChannelsChassisId_Type(Integer32):
    """Custom type cubominiXcvrOptChannelsChassisId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CubominiXcvrOptChannelsChassisId_Type.__name__ = "Integer32"
_CubominiXcvrOptChannelsChassisId_Object = MibTableColumn
cubominiXcvrOptChannelsChassisId = _CubominiXcvrOptChannelsChassisId_Object(
    (1, 3, 6, 1, 4, 1, 27894, 11, 241, 1, 9, 6, 1, 1),
    _CubominiXcvrOptChannelsChassisId_Type()
)
cubominiXcvrOptChannelsChassisId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cubominiXcvrOptChannelsChassisId.setStatus("current")


class _CubominiXcvrOptChannelsSlotId_Type(Integer32):
    """Custom type cubominiXcvrOptChannelsSlotId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CubominiXcvrOptChannelsSlotId_Type.__name__ = "Integer32"
_CubominiXcvrOptChannelsSlotId_Object = MibTableColumn
cubominiXcvrOptChannelsSlotId = _CubominiXcvrOptChannelsSlotId_Object(
    (1, 3, 6, 1, 4, 1, 27894, 11, 241, 1, 9, 6, 1, 2),
    _CubominiXcvrOptChannelsSlotId_Type()
)
cubominiXcvrOptChannelsSlotId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cubominiXcvrOptChannelsSlotId.setStatus("current")


class _CubominiXcvrOptChannelsPortId_Type(Integer32):
    """Custom type cubominiXcvrOptChannelsPortId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CubominiXcvrOptChannelsPortId_Type.__name__ = "Integer32"
_CubominiXcvrOptChannelsPortId_Object = MibTableColumn
cubominiXcvrOptChannelsPortId = _CubominiXcvrOptChannelsPortId_Object(
    (1, 3, 6, 1, 4, 1, 27894, 11, 241, 1, 9, 6, 1, 3),
    _CubominiXcvrOptChannelsPortId_Type()
)
cubominiXcvrOptChannelsPortId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cubominiXcvrOptChannelsPortId.setStatus("current")


class _CubominiXcvrOptChannelsChannelId_Type(Integer32):
    """Custom type cubominiXcvrOptChannelsChannelId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CubominiXcvrOptChannelsChannelId_Type.__name__ = "Integer32"
_CubominiXcvrOptChannelsChannelId_Object = MibTableColumn
cubominiXcvrOptChannelsChannelId = _CubominiXcvrOptChannelsChannelId_Object(
    (1, 3, 6, 1, 4, 1, 27894, 11, 241, 1, 9, 6, 1, 4),
    _CubominiXcvrOptChannelsChannelId_Type()
)
cubominiXcvrOptChannelsChannelId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cubominiXcvrOptChannelsChannelId.setStatus("current")


class _CubominiXcvrOptChannelsTxPower_Type(Integer32):
    """Custom type cubominiXcvrOptChannelsTxPower based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-400, 82),
    )


_CubominiXcvrOptChannelsTxPower_Type.__name__ = "Integer32"
_CubominiXcvrOptChannelsTxPower_Object = MibTableColumn
cubominiXcvrOptChannelsTxPower = _CubominiXcvrOptChannelsTxPower_Object(
    (1, 3, 6, 1, 4, 1, 27894, 11, 241, 1, 9, 6, 1, 5),
    _CubominiXcvrOptChannelsTxPower_Type()
)
cubominiXcvrOptChannelsTxPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cubominiXcvrOptChannelsTxPower.setStatus("current")
if mibBuilder.loadTexts:
    cubominiXcvrOptChannelsTxPower.setUnits("Tenths (1/10) of dBm")


class _CubominiXcvrOptChannelsRxPower_Type(Integer32):
    """Custom type cubominiXcvrOptChannelsRxPower based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-400, 82),
    )


_CubominiXcvrOptChannelsRxPower_Type.__name__ = "Integer32"
_CubominiXcvrOptChannelsRxPower_Object = MibTableColumn
cubominiXcvrOptChannelsRxPower = _CubominiXcvrOptChannelsRxPower_Object(
    (1, 3, 6, 1, 4, 1, 27894, 11, 241, 1, 9, 6, 1, 6),
    _CubominiXcvrOptChannelsRxPower_Type()
)
cubominiXcvrOptChannelsRxPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cubominiXcvrOptChannelsRxPower.setStatus("current")
if mibBuilder.loadTexts:
    cubominiXcvrOptChannelsRxPower.setUnits("Tenths (1/10) of dBm")
_CubominiTraps_ObjectIdentity = ObjectIdentity
cubominiTraps = _CubominiTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27894, 11, 241, 2)
)


class _CubominiCardId_Type(Integer32):
    """Custom type cubominiCardId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            241
        )
    )
    namedValues = NamedValues(
        ("cuboMini", 241)
    )


_CubominiCardId_Type.__name__ = "Integer32"
_CubominiCardId_Object = MibScalar
cubominiCardId = _CubominiCardId_Object(
    (1, 3, 6, 1, 4, 1, 27894, 11, 241, 2, 3),
    _CubominiCardId_Type()
)
cubominiCardId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cubominiCardId.setStatus("current")


class _CubominiChassis_Type(Integer32):
    """Custom type cubominiChassis based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CubominiChassis_Type.__name__ = "Integer32"
_CubominiChassis_Object = MibScalar
cubominiChassis = _CubominiChassis_Object(
    (1, 3, 6, 1, 4, 1, 27894, 11, 241, 2, 4),
    _CubominiChassis_Type()
)
cubominiChassis.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cubominiChassis.setStatus("current")


class _CubominiSlot_Type(Integer32):
    """Custom type cubominiSlot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CubominiSlot_Type.__name__ = "Integer32"
_CubominiSlot_Object = MibScalar
cubominiSlot = _CubominiSlot_Object(
    (1, 3, 6, 1, 4, 1, 27894, 11, 241, 2, 5),
    _CubominiSlot_Type()
)
cubominiSlot.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cubominiSlot.setStatus("current")


class _CubominiPort_Type(Integer32):
    """Custom type cubominiPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CubominiPort_Type.__name__ = "Integer32"
_CubominiPort_Object = MibScalar
cubominiPort = _CubominiPort_Object(
    (1, 3, 6, 1, 4, 1, 27894, 11, 241, 2, 6),
    _CubominiPort_Type()
)
cubominiPort.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cubominiPort.setStatus("current")


class _CubominiNotificationId_Type(Integer32):
    """Custom type cubominiNotificationId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(3,
              5,
              259,
              288,
              289,
              290,
              291,
              292,
              296,
              297,
              298,
              299,
              301,
              302,
              336)
        )
    )
    namedValues = NamedValues(
        *(("alarmChassisFanFailure", 3),
          ("eventMonitorReset", 5),
          ("alarmPortRegulatorFailure", 259),
          ("eventTransceiverExtracted", 288),
          ("alarmTransceiverLossOfSignal", 289),
          ("alarmTransceiverTxFailure", 290),
          ("eventTransceiverLaserOff", 291),
          ("alarmCdrRxLossOfLock", 292),
          ("alarmTransceiverLowRxPowerAlarm", 296),
          ("alarmTransceiverHighRxPowerAlarm", 297),
          ("alarmTransceiverLowTxPowerAlarm", 298),
          ("alarmTransceiverHighTxPowerAlarm", 299),
          ("alarmTransceiverLowTemperatureAlarm", 301),
          ("alarmTransceiverHighTemperatureAlarm", 302),
          ("eventTransceiverLoopbackOn", 336))
    )


_CubominiNotificationId_Type.__name__ = "Integer32"
_CubominiNotificationId_Object = MibScalar
cubominiNotificationId = _CubominiNotificationId_Object(
    (1, 3, 6, 1, 4, 1, 27894, 11, 241, 2, 7),
    _CubominiNotificationId_Type()
)
cubominiNotificationId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cubominiNotificationId.setStatus("current")


class _CubominiShortDescription_Type(OctetString):
    """Custom type cubominiShortDescription based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(20, 20),
    )
    fixed_length = 20


_CubominiShortDescription_Type.__name__ = "OctetString"
_CubominiShortDescription_Object = MibScalar
cubominiShortDescription = _CubominiShortDescription_Object(
    (1, 3, 6, 1, 4, 1, 27894, 11, 241, 2, 8),
    _CubominiShortDescription_Type()
)
cubominiShortDescription.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cubominiShortDescription.setStatus("current")


class _CubominiLongDescription_Type(OctetString):
    """Custom type cubominiLongDescription based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(128, 128),
    )
    fixed_length = 128


_CubominiLongDescription_Type.__name__ = "OctetString"
_CubominiLongDescription_Object = MibScalar
cubominiLongDescription = _CubominiLongDescription_Object(
    (1, 3, 6, 1, 4, 1, 27894, 11, 241, 2, 9),
    _CubominiLongDescription_Type()
)
cubominiLongDescription.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cubominiLongDescription.setStatus("current")


class _CubominiSeverity_Type(Integer32):
    """Custom type cubominiSeverity based on Integer32"""
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
          ("notification", 2),
          ("minor", 3),
          ("major", 4),
          ("critical", 5))
    )


_CubominiSeverity_Type.__name__ = "Integer32"
_CubominiSeverity_Object = MibScalar
cubominiSeverity = _CubominiSeverity_Object(
    (1, 3, 6, 1, 4, 1, 27894, 11, 241, 2, 10),
    _CubominiSeverity_Type()
)
cubominiSeverity.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cubominiSeverity.setStatus("current")


class _CubominiData_Type(OctetString):
    """Custom type cubominiData based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(32, 32),
    )
    fixed_length = 32


_CubominiData_Type.__name__ = "OctetString"
_CubominiData_Object = MibScalar
cubominiData = _CubominiData_Object(
    (1, 3, 6, 1, 4, 1, 27894, 11, 241, 2, 11),
    _CubominiData_Type()
)
cubominiData.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cubominiData.setStatus("current")


class _CubominiLabel_Type(OctetString):
    """Custom type cubominiLabel based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(200, 200),
    )
    fixed_length = 200


_CubominiLabel_Type.__name__ = "OctetString"
_CubominiLabel_Object = MibScalar
cubominiLabel = _CubominiLabel_Object(
    (1, 3, 6, 1, 4, 1, 27894, 11, 241, 2, 12),
    _CubominiLabel_Type()
)
cubominiLabel.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cubominiLabel.setStatus("current")


class _CubominiEventTime_Type(OctetString):
    """Custom type cubominiEventTime based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(32, 32),
    )
    fixed_length = 32


_CubominiEventTime_Type.__name__ = "OctetString"
_CubominiEventTime_Object = MibScalar
cubominiEventTime = _CubominiEventTime_Object(
    (1, 3, 6, 1, 4, 1, 27894, 11, 241, 2, 13),
    _CubominiEventTime_Type()
)
cubominiEventTime.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cubominiEventTime.setStatus("current")
_CubominiConformance_ObjectIdentity = ObjectIdentity
cubominiConformance = _CubominiConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27894, 11, 241, 3)
)
_CubominiCompliances_ObjectIdentity = ObjectIdentity
cubominiCompliances = _CubominiCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27894, 11, 241, 3, 1)
)
_CubominiGroups_ObjectIdentity = ObjectIdentity
cubominiGroups = _CubominiGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27894, 11, 241, 3, 2)
)

# Managed Objects groups

cubo_miniGeneralGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 27894, 11, 241, 3, 2, 1)
)
cubo_miniGeneralGroup.setObjects(
      *(("CUBO-MINI-MIB", "cubominiSystemDataSerialNumber"),
        ("CUBO-MINI-MIB", "cubominiSystemDataDeviceName"),
        ("CUBO-MINI-MIB", "cubominiSystemDataSwVersion"),
        ("CUBO-MINI-MIB", "cubominiSystemDataFwVersion"),
        ("CUBO-MINI-MIB", "cubominiSystemDataHwVersion"))
)
if mibBuilder.loadTexts:
    cubo_miniGeneralGroup.setStatus("current")

cubo_miniFanGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 27894, 11, 241, 3, 2, 2)
)
cubo_miniFanGroup.setObjects(
      *(("CUBO-MINI-MIB", "cubominiFanStatus"),
        ("CUBO-MINI-MIB", "cubominiFanSpeed"))
)
if mibBuilder.loadTexts:
    cubo_miniFanGroup.setStatus("current")

cubo_miniManagementGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 27894, 11, 241, 3, 2, 3)
)
cubo_miniManagementGroup.setObjects(
      *(("CUBO-MINI-MIB", "cubominiSnmpManagersIp"),
        ("CUBO-MINI-MIB", "cubominiEmsManagersIp"))
)
if mibBuilder.loadTexts:
    cubo_miniManagementGroup.setStatus("current")

cubo_miniNetworkIfGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 27894, 11, 241, 3, 2, 4)
)
cubo_miniNetworkIfGroup.setObjects(
      *(("CUBO-MINI-MIB", "cubominiNetworkIfIPAddress"),
        ("CUBO-MINI-MIB", "cubominiNetworkIfNetMask"),
        ("CUBO-MINI-MIB", "cubominiNetworkIfGateway"),
        ("CUBO-MINI-MIB", "cubominiOptGeneralIsInserted"),
        ("CUBO-MINI-MIB", "cubominiOptGeneralEventsStatus"),
        ("CUBO-MINI-MIB", "cubominiOptGeneralTxForce"),
        ("CUBO-MINI-MIB", "cubominiOptIdentVendorName"),
        ("CUBO-MINI-MIB", "cubominiOptIdentVendorPartNumber"),
        ("CUBO-MINI-MIB", "cubominiOptIdentVendorSerialNumber"),
        ("CUBO-MINI-MIB", "cubominiOptIdentNominalWavelength"),
        ("CUBO-MINI-MIB", "cubominiDnsServerIpAddress"))
)
if mibBuilder.loadTexts:
    cubo_miniNetworkIfGroup.setStatus("current")

cubo_miniNtpServerGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 27894, 11, 241, 3, 2, 5)
)
cubo_miniNtpServerGroup.setObjects(
      *(("CUBO-MINI-MIB", "cubominiNtpServerParamsActive"),
        ("CUBO-MINI-MIB", "cubominiNtpServerIPAddress"))
)
if mibBuilder.loadTexts:
    cubo_miniNtpServerGroup.setStatus("current")

cubo_miniXcvrGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 27894, 11, 241, 3, 2, 6)
)
cubo_miniXcvrGroup.setObjects(
      *(("CUBO-MINI-MIB", "cubominiXcvrCommonConfigLoopbackOperation"),
        ("CUBO-MINI-MIB", "cubominiXcvrCommonConfigLoopbackTimeout"),
        ("CUBO-MINI-MIB", "cubominiXcvrCommonConfigDataRateSet"),
        ("CUBO-MINI-MIB", "cubominiXcvrCommonConfigLinkLossFwd"),
        ("CUBO-MINI-MIB", "cubominiXcvrGeneralIsInserted"),
        ("CUBO-MINI-MIB", "cubominiXcvrGeneralEventsStatusAll"),
        ("CUBO-MINI-MIB", "cubominiXcvrGeneralCDRPortEventsStatusAll"),
        ("CUBO-MINI-MIB", "cubominiXcvrGeneralTxForceMode"),
        ("CUBO-MINI-MIB", "cubominiXcvrIdentVendorName"),
        ("CUBO-MINI-MIB", "cubominiXcvrIdentVendorPartNumber"),
        ("CUBO-MINI-MIB", "cubominiXcvrIdentVendorSerialNumber"),
        ("CUBO-MINI-MIB", "cubominiXcvrIdentNominalWavelength"),
        ("CUBO-MINI-MIB", "cubominiXcvrEvThresholdMinInputPower"),
        ("CUBO-MINI-MIB", "cubominiXcvrEvThresholdMaxInputPower"),
        ("CUBO-MINI-MIB", "cubominiXcvrEvThresholdMinOutputPower"),
        ("CUBO-MINI-MIB", "cubominiXcvrEvThresholdMaxOutputPower"),
        ("CUBO-MINI-MIB", "cubominiXcvrDiagnosticsTemperature"),
        ("CUBO-MINI-MIB", "cubominiXcvrDiagnosticsTxPowerAll"),
        ("CUBO-MINI-MIB", "cubominiXcvrDiagnosticsRxPowerAll"),
        ("CUBO-MINI-MIB", "cubominiXcvrOptChannelsTxPower"),
        ("CUBO-MINI-MIB", "cubominiXcvrOptChannelsRxPower"))
)
if mibBuilder.loadTexts:
    cubo_miniXcvrGroup.setStatus("current")

cubo_miniNotificationObjectsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 27894, 11, 241, 3, 2, 7)
)
cubo_miniNotificationObjectsGroup.setObjects(
      *(("CUBO-MINI-MIB", "cubominiCardId"),
        ("CUBO-MINI-MIB", "cubominiChassis"),
        ("CUBO-MINI-MIB", "cubominiSlot"),
        ("CUBO-MINI-MIB", "cubominiPort"),
        ("CUBO-MINI-MIB", "cubominiNotificationId"),
        ("CUBO-MINI-MIB", "cubominiShortDescription"),
        ("CUBO-MINI-MIB", "cubominiLongDescription"),
        ("CUBO-MINI-MIB", "cubominiSeverity"),
        ("CUBO-MINI-MIB", "cubominiData"),
        ("CUBO-MINI-MIB", "cubominiLabel"),
        ("CUBO-MINI-MIB", "cubominiEventTime"))
)
if mibBuilder.loadTexts:
    cubo_miniNotificationObjectsGroup.setStatus("current")


# Notification objects

cubominiNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 27894, 11, 241, 2, 2)
)
cubominiNotification.setObjects(
      *(("CUBO-MINI-MIB", "cubominiCardId"),
        ("CUBO-MINI-MIB", "cubominiChassis"),
        ("CUBO-MINI-MIB", "cubominiSlot"),
        ("CUBO-MINI-MIB", "cubominiPort"),
        ("CUBO-MINI-MIB", "cubominiNotificationId"),
        ("CUBO-MINI-MIB", "cubominiShortDescription"),
        ("CUBO-MINI-MIB", "cubominiLongDescription"),
        ("CUBO-MINI-MIB", "cubominiSeverity"),
        ("CUBO-MINI-MIB", "cubominiData"),
        ("CUBO-MINI-MIB", "cubominiLabel"),
        ("CUBO-MINI-MIB", "cubominiEventTime"))
)
if mibBuilder.loadTexts:
    cubominiNotification.setStatus(
        "current"
    )


# Notifications groups

cubo_miniNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 27894, 11, 241, 3, 2, 8)
)
cubo_miniNotificationGroup.setObjects(
    ("CUBO-MINI-MIB", "cubominiNotification")
)
if mibBuilder.loadTexts:
    cubo_miniNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

cubominiCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 27894, 11, 241, 3, 1, 1)
)
cubominiCompliance.setObjects(
      *(("CUBO-MINI-MIB", "cubo-miniGeneralGroup"),
        ("CUBO-MINI-MIB", "cubo-miniFanGroup"),
        ("CUBO-MINI-MIB", "cubo-miniManagementGroup"),
        ("CUBO-MINI-MIB", "cubo-miniNetworkIfGroup"),
        ("CUBO-MINI-MIB", "cubo-miniNtpServerGroup"),
        ("CUBO-MINI-MIB", "cubo-miniXcvrGroup"),
        ("CUBO-MINI-MIB", "cubo-miniNotificationObjectsGroup"),
        ("CUBO-MINI-MIB", "cubo-miniNotificationGroup"))
)
if mibBuilder.loadTexts:
    cubominiCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CUBO-MINI-MIB",
    **{"cubo-mini": cubo_mini,
       "cubominiObjects": cubominiObjects,
       "cubominiGeneralGroup": cubominiGeneralGroup,
       "cubominiSystemDataTable": cubominiSystemDataTable,
       "cubominiSystemDataEntry": cubominiSystemDataEntry,
       "cubominiSystemDataChassisId": cubominiSystemDataChassisId,
       "cubominiSystemDataSerialNumber": cubominiSystemDataSerialNumber,
       "cubominiSystemDataDeviceName": cubominiSystemDataDeviceName,
       "cubominiSystemDataSwVersion": cubominiSystemDataSwVersion,
       "cubominiSystemDataFwVersion": cubominiSystemDataFwVersion,
       "cubominiSystemDataHwVersion": cubominiSystemDataHwVersion,
       "cubominiFanGroup": cubominiFanGroup,
       "cubominiFanTable": cubominiFanTable,
       "cubominiFanEntry": cubominiFanEntry,
       "cubominiFanChassisId": cubominiFanChassisId,
       "cubominiFanSlotId": cubominiFanSlotId,
       "cubominiFanFanslotminiId": cubominiFanFanslotminiId,
       "cubominiFanStatus": cubominiFanStatus,
       "cubominiFanSpeed": cubominiFanSpeed,
       "cubominiManagementGroup": cubominiManagementGroup,
       "cubominiSnmpManagersTable": cubominiSnmpManagersTable,
       "cubominiSnmpManagersEntry": cubominiSnmpManagersEntry,
       "cubominiSnmpManagersChassisId": cubominiSnmpManagersChassisId,
       "cubominiSnmpManagersSnmpindexId": cubominiSnmpManagersSnmpindexId,
       "cubominiSnmpManagersIp": cubominiSnmpManagersIp,
       "cubominiEmsManagersTable": cubominiEmsManagersTable,
       "cubominiEmsManagersEntry": cubominiEmsManagersEntry,
       "cubominiEmsManagersChassisId": cubominiEmsManagersChassisId,
       "cubominiEmsManagersEmsindexId": cubominiEmsManagersEmsindexId,
       "cubominiEmsManagersIp": cubominiEmsManagersIp,
       "cubominiNetworkIfGroup": cubominiNetworkIfGroup,
       "cubominiNetworkIfTable": cubominiNetworkIfTable,
       "cubominiNetworkIfEntry": cubominiNetworkIfEntry,
       "cubominiNetworkIfChassisId": cubominiNetworkIfChassisId,
       "cubominiNetworkIfNetindexId": cubominiNetworkIfNetindexId,
       "cubominiNetworkIfIPAddress": cubominiNetworkIfIPAddress,
       "cubominiNetworkIfNetMask": cubominiNetworkIfNetMask,
       "cubominiNetworkIfGateway": cubominiNetworkIfGateway,
       "cubominiOptGeneralTable": cubominiOptGeneralTable,
       "cubominiOptGeneralEntry": cubominiOptGeneralEntry,
       "cubominiOptGeneralChassisId": cubominiOptGeneralChassisId,
       "cubominiOptGeneralMonindexId": cubominiOptGeneralMonindexId,
       "cubominiOptGeneralPortId": cubominiOptGeneralPortId,
       "cubominiOptGeneralIsInserted": cubominiOptGeneralIsInserted,
       "cubominiOptGeneralEventsStatus": cubominiOptGeneralEventsStatus,
       "cubominiOptGeneralTxForce": cubominiOptGeneralTxForce,
       "cubominiOptIdentTable": cubominiOptIdentTable,
       "cubominiOptIdentEntry": cubominiOptIdentEntry,
       "cubominiOptIdentChassisId": cubominiOptIdentChassisId,
       "cubominiOptIdentMonindexId": cubominiOptIdentMonindexId,
       "cubominiOptIdentPortId": cubominiOptIdentPortId,
       "cubominiOptIdentVendorName": cubominiOptIdentVendorName,
       "cubominiOptIdentVendorPartNumber": cubominiOptIdentVendorPartNumber,
       "cubominiOptIdentVendorSerialNumber": cubominiOptIdentVendorSerialNumber,
       "cubominiOptIdentNominalWavelength": cubominiOptIdentNominalWavelength,
       "cubominiDnsServerTable": cubominiDnsServerTable,
       "cubominiDnsServerEntry": cubominiDnsServerEntry,
       "cubominiDnsServerChassisId": cubominiDnsServerChassisId,
       "cubominiDnsServerDnsindexId": cubominiDnsServerDnsindexId,
       "cubominiDnsServerIpAddress": cubominiDnsServerIpAddress,
       "cubominiNtpServerGroup": cubominiNtpServerGroup,
       "cubominiNtpServerParamsTable": cubominiNtpServerParamsTable,
       "cubominiNtpServerParamsEntry": cubominiNtpServerParamsEntry,
       "cubominiNtpServerParamsChassisId": cubominiNtpServerParamsChassisId,
       "cubominiNtpServerParamsActive": cubominiNtpServerParamsActive,
       "cubominiNtpServerTable": cubominiNtpServerTable,
       "cubominiNtpServerEntry": cubominiNtpServerEntry,
       "cubominiNtpServerChassisId": cubominiNtpServerChassisId,
       "cubominiNtpServerNtpindexId": cubominiNtpServerNtpindexId,
       "cubominiNtpServerIPAddress": cubominiNtpServerIPAddress,
       "cubominiXcvrGroup": cubominiXcvrGroup,
       "cubominiXcvrCommonConfigTable": cubominiXcvrCommonConfigTable,
       "cubominiXcvrCommonConfigEntry": cubominiXcvrCommonConfigEntry,
       "cubominiXcvrCommonConfigChassisId": cubominiXcvrCommonConfigChassisId,
       "cubominiXcvrCommonConfigSlotId": cubominiXcvrCommonConfigSlotId,
       "cubominiXcvrCommonConfigLoopbackOperation": cubominiXcvrCommonConfigLoopbackOperation,
       "cubominiXcvrCommonConfigLoopbackTimeout": cubominiXcvrCommonConfigLoopbackTimeout,
       "cubominiXcvrCommonConfigDataRateSet": cubominiXcvrCommonConfigDataRateSet,
       "cubominiXcvrCommonConfigLinkLossFwd": cubominiXcvrCommonConfigLinkLossFwd,
       "cubominiXcvrGeneralTable": cubominiXcvrGeneralTable,
       "cubominiXcvrGeneralEntry": cubominiXcvrGeneralEntry,
       "cubominiXcvrGeneralChassisId": cubominiXcvrGeneralChassisId,
       "cubominiXcvrGeneralSlotId": cubominiXcvrGeneralSlotId,
       "cubominiXcvrGeneralPortId": cubominiXcvrGeneralPortId,
       "cubominiXcvrGeneralIsInserted": cubominiXcvrGeneralIsInserted,
       "cubominiXcvrGeneralEventsStatusAll": cubominiXcvrGeneralEventsStatusAll,
       "cubominiXcvrGeneralCDRPortEventsStatusAll": cubominiXcvrGeneralCDRPortEventsStatusAll,
       "cubominiXcvrGeneralTxForceMode": cubominiXcvrGeneralTxForceMode,
       "cubominiXcvrIdentTable": cubominiXcvrIdentTable,
       "cubominiXcvrIdentEntry": cubominiXcvrIdentEntry,
       "cubominiXcvrIdentChassisId": cubominiXcvrIdentChassisId,
       "cubominiXcvrIdentSlotId": cubominiXcvrIdentSlotId,
       "cubominiXcvrIdentPortId": cubominiXcvrIdentPortId,
       "cubominiXcvrIdentVendorName": cubominiXcvrIdentVendorName,
       "cubominiXcvrIdentVendorPartNumber": cubominiXcvrIdentVendorPartNumber,
       "cubominiXcvrIdentVendorSerialNumber": cubominiXcvrIdentVendorSerialNumber,
       "cubominiXcvrIdentNominalWavelength": cubominiXcvrIdentNominalWavelength,
       "cubominiXcvrEvThresholdTable": cubominiXcvrEvThresholdTable,
       "cubominiXcvrEvThresholdEntry": cubominiXcvrEvThresholdEntry,
       "cubominiXcvrEvThresholdChassisId": cubominiXcvrEvThresholdChassisId,
       "cubominiXcvrEvThresholdSlotId": cubominiXcvrEvThresholdSlotId,
       "cubominiXcvrEvThresholdPortId": cubominiXcvrEvThresholdPortId,
       "cubominiXcvrEvThresholdMinInputPower": cubominiXcvrEvThresholdMinInputPower,
       "cubominiXcvrEvThresholdMaxInputPower": cubominiXcvrEvThresholdMaxInputPower,
       "cubominiXcvrEvThresholdMinOutputPower": cubominiXcvrEvThresholdMinOutputPower,
       "cubominiXcvrEvThresholdMaxOutputPower": cubominiXcvrEvThresholdMaxOutputPower,
       "cubominiXcvrDiagnosticsTable": cubominiXcvrDiagnosticsTable,
       "cubominiXcvrDiagnosticsEntry": cubominiXcvrDiagnosticsEntry,
       "cubominiXcvrDiagnosticsChassisId": cubominiXcvrDiagnosticsChassisId,
       "cubominiXcvrDiagnosticsSlotId": cubominiXcvrDiagnosticsSlotId,
       "cubominiXcvrDiagnosticsPortId": cubominiXcvrDiagnosticsPortId,
       "cubominiXcvrDiagnosticsTemperature": cubominiXcvrDiagnosticsTemperature,
       "cubominiXcvrDiagnosticsTxPowerAll": cubominiXcvrDiagnosticsTxPowerAll,
       "cubominiXcvrDiagnosticsRxPowerAll": cubominiXcvrDiagnosticsRxPowerAll,
       "cubominiXcvrOptChannelsTable": cubominiXcvrOptChannelsTable,
       "cubominiXcvrOptChannelsEntry": cubominiXcvrOptChannelsEntry,
       "cubominiXcvrOptChannelsChassisId": cubominiXcvrOptChannelsChassisId,
       "cubominiXcvrOptChannelsSlotId": cubominiXcvrOptChannelsSlotId,
       "cubominiXcvrOptChannelsPortId": cubominiXcvrOptChannelsPortId,
       "cubominiXcvrOptChannelsChannelId": cubominiXcvrOptChannelsChannelId,
       "cubominiXcvrOptChannelsTxPower": cubominiXcvrOptChannelsTxPower,
       "cubominiXcvrOptChannelsRxPower": cubominiXcvrOptChannelsRxPower,
       "cubominiTraps": cubominiTraps,
       "cubominiNotification": cubominiNotification,
       "cubominiCardId": cubominiCardId,
       "cubominiChassis": cubominiChassis,
       "cubominiSlot": cubominiSlot,
       "cubominiPort": cubominiPort,
       "cubominiNotificationId": cubominiNotificationId,
       "cubominiShortDescription": cubominiShortDescription,
       "cubominiLongDescription": cubominiLongDescription,
       "cubominiSeverity": cubominiSeverity,
       "cubominiData": cubominiData,
       "cubominiLabel": cubominiLabel,
       "cubominiEventTime": cubominiEventTime,
       "cubominiConformance": cubominiConformance,
       "cubominiCompliances": cubominiCompliances,
       "cubominiCompliance": cubominiCompliance,
       "cubominiGroups": cubominiGroups,
       "cubo-miniGeneralGroup": cubo_miniGeneralGroup,
       "cubo-miniFanGroup": cubo_miniFanGroup,
       "cubo-miniManagementGroup": cubo_miniManagementGroup,
       "cubo-miniNetworkIfGroup": cubo_miniNetworkIfGroup,
       "cubo-miniNtpServerGroup": cubo_miniNtpServerGroup,
       "cubo-miniXcvrGroup": cubo_miniXcvrGroup,
       "cubo-miniNotificationObjectsGroup": cubo_miniNotificationObjectsGroup,
       "cubo-miniNotificationGroup": cubo_miniNotificationGroup}
)
