# SNMP MIB module (AX-DEVICE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\alaxala\AX-DEVICE-MIB

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

(axMib,) = mibBuilder.importSymbols(
    "AX-SMI-MIB",
    "axMib")

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

axDevice = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 1002)
)
if mibBuilder.loadTexts:
    axDevice.setRevisions(
        ("2020-09-24 00:00",
         "2019-03-11 00:00",
         "2018-02-13 00:00",
         "2016-07-19 00:00",
         "2016-06-13 00:00",
         "2016-02-03 00:00",
         "2015-12-25 00:00",
         "2014-10-02 00:00",
         "2014-02-28 00:00",
         "2013-08-02 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AxChassis_ObjectIdentity = ObjectIdentity
axChassis = _AxChassis_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 1002, 1)
)
_AxChassisMaxNumber_Type = Integer32
_AxChassisMaxNumber_Object = MibScalar
axChassisMaxNumber = _AxChassisMaxNumber_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 1002, 1, 1),
    _AxChassisMaxNumber_Type()
)
axChassisMaxNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axChassisMaxNumber.setStatus("current")
_AxChassisTable_Object = MibTable
axChassisTable = _AxChassisTable_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 1002, 1, 2)
)
if mibBuilder.loadTexts:
    axChassisTable.setStatus("current")
_AxChassisEntry_Object = MibTableRow
axChassisEntry = _AxChassisEntry_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 1002, 1, 2, 1)
)
axChassisEntry.setIndexNames(
    (0, "AX-DEVICE-MIB", "axChassisIndex"),
)
if mibBuilder.loadTexts:
    axChassisEntry.setStatus("current")
_AxChassisIndex_Type = Integer32
_AxChassisIndex_Object = MibTableColumn
axChassisIndex = _AxChassisIndex_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 1002, 1, 2, 1, 1),
    _AxChassisIndex_Type()
)
axChassisIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    axChassisIndex.setStatus("current")
_AxChassisName_Type = DisplayString
_AxChassisName_Object = MibTableColumn
axChassisName = _AxChassisName_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 1002, 1, 2, 1, 2),
    _AxChassisName_Type()
)
axChassisName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axChassisName.setStatus("current")
_AxChassisAbbreviation_Type = DisplayString
_AxChassisAbbreviation_Object = MibTableColumn
axChassisAbbreviation = _AxChassisAbbreviation_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 1002, 1, 2, 1, 3),
    _AxChassisAbbreviation_Type()
)
axChassisAbbreviation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axChassisAbbreviation.setStatus("current")


class _AxChassisType_Type(Integer32):
    """Custom type axChassisType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              3000,
              3001,
              3002,
              4000,
              4001,
              4002,
              4100,
              4103)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("ax8608R", 3000),
          ("ax8616R", 3001),
          ("ax8632R", 3002),
          ("ax8608S", 4000),
          ("ax8616S", 4001),
          ("ax8632S", 4002),
          ("ax8308S", 4100),
          ("ax8304S", 4103))
    )


_AxChassisType_Type.__name__ = "Integer32"
_AxChassisType_Object = MibTableColumn
axChassisType = _AxChassisType_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 1002, 1, 2, 1, 4),
    _AxChassisType_Type()
)
axChassisType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axChassisType.setStatus("current")
_AxPowerUnitNumber_Type = Integer32
_AxPowerUnitNumber_Object = MibTableColumn
axPowerUnitNumber = _AxPowerUnitNumber_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 1002, 1, 2, 1, 5),
    _AxPowerUnitNumber_Type()
)
axPowerUnitNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axPowerUnitNumber.setStatus("current")
_AxFanNumber_Type = Integer32
_AxFanNumber_Object = MibTableColumn
axFanNumber = _AxFanNumber_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 1002, 1, 2, 1, 6),
    _AxFanNumber_Type()
)
axFanNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axFanNumber.setStatus("current")
_AxBcuBoardNumber_Type = Integer32
_AxBcuBoardNumber_Object = MibTableColumn
axBcuBoardNumber = _AxBcuBoardNumber_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 1002, 1, 2, 1, 7),
    _AxBcuBoardNumber_Type()
)
axBcuBoardNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axBcuBoardNumber.setStatus("current")
_AxSfuBoardNumber_Type = Integer32
_AxSfuBoardNumber_Object = MibTableColumn
axSfuBoardNumber = _AxSfuBoardNumber_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 1002, 1, 2, 1, 8),
    _AxSfuBoardNumber_Type()
)
axSfuBoardNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axSfuBoardNumber.setStatus("current")
_AxPruBoardNumber_Type = Integer32
_AxPruBoardNumber_Object = MibTableColumn
axPruBoardNumber = _AxPruBoardNumber_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 1002, 1, 2, 1, 9),
    _AxPruBoardNumber_Type()
)
axPruBoardNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axPruBoardNumber.setStatus("current")
_AxPsuBoardNumber_Type = Integer32
_AxPsuBoardNumber_Object = MibTableColumn
axPsuBoardNumber = _AxPsuBoardNumber_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 1002, 1, 2, 1, 10),
    _AxPsuBoardNumber_Type()
)
axPsuBoardNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axPsuBoardNumber.setStatus("current")
_AxNifBoardNumber_Type = Integer32
_AxNifBoardNumber_Object = MibTableColumn
axNifBoardNumber = _AxNifBoardNumber_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 1002, 1, 2, 1, 11),
    _AxNifBoardNumber_Type()
)
axNifBoardNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axNifBoardNumber.setStatus("current")
_AxChassisSerialInformation_Type = DisplayString
_AxChassisSerialInformation_Object = MibTableColumn
axChassisSerialInformation = _AxChassisSerialInformation_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 1002, 1, 2, 1, 13),
    _AxChassisSerialInformation_Type()
)
axChassisSerialInformation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axChassisSerialInformation.setStatus("current")
_AxChassisSystemTable_Object = MibTable
axChassisSystemTable = _AxChassisSystemTable_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 1002, 1, 3)
)
if mibBuilder.loadTexts:
    axChassisSystemTable.setStatus("current")
_AxChassisSystemEntry_Object = MibTableRow
axChassisSystemEntry = _AxChassisSystemEntry_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 1002, 1, 3, 1)
)
axChassisSystemEntry.setIndexNames(
    (0, "AX-DEVICE-MIB", "axChassisIndex"),
)
if mibBuilder.loadTexts:
    axChassisSystemEntry.setStatus("current")


class _AxChassisStatus_Type(Integer32):
    """Custom type axChassisStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            2
        )
    )
    namedValues = NamedValues(
        ("up", 2)
    )


_AxChassisStatus_Type.__name__ = "Integer32"
_AxChassisStatus_Object = MibTableColumn
axChassisStatus = _AxChassisStatus_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 1002, 1, 3, 1, 1),
    _AxChassisStatus_Type()
)
axChassisStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axChassisStatus.setStatus("current")


class _AxPowerSupplyUnitRedundancyMode_Type(Integer32):
    """Custom type axPowerSupplyUnitRedundancyMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              99)
        )
    )
    namedValues = NamedValues(
        *(("powerSupply", 1),
          ("powerSupplyAndInputSource", 2),
          ("notConfigured", 99))
    )


_AxPowerSupplyUnitRedundancyMode_Type.__name__ = "Integer32"
_AxPowerSupplyUnitRedundancyMode_Object = MibTableColumn
axPowerSupplyUnitRedundancyMode = _AxPowerSupplyUnitRedundancyMode_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 1002, 1, 3, 1, 2),
    _AxPowerSupplyUnitRedundancyMode_Type()
)
axPowerSupplyUnitRedundancyMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axPowerSupplyUnitRedundancyMode.setStatus("current")


class _AxFanMode_Type(Integer32):
    """Custom type axFanMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("normal", 1),
          ("cool", 2))
    )


_AxFanMode_Type.__name__ = "Integer32"
_AxFanMode_Object = MibTableColumn
axFanMode = _AxFanMode_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 1002, 1, 3, 1, 3),
    _AxFanMode_Type()
)
axFanMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axFanMode.setStatus("current")


class _AxBcuBoardRedundancyStatus_Type(Integer32):
    """Custom type axBcuBoardRedundancyStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("simplex", 1),
          ("duplex", 2))
    )


_AxBcuBoardRedundancyStatus_Type.__name__ = "Integer32"
_AxBcuBoardRedundancyStatus_Object = MibTableColumn
axBcuBoardRedundancyStatus = _AxBcuBoardRedundancyStatus_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 1002, 1, 3, 1, 4),
    _AxBcuBoardRedundancyStatus_Type()
)
axBcuBoardRedundancyStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axBcuBoardRedundancyStatus.setStatus("current")
_AxTotalPowerSupplyCapacity_Type = Integer32
_AxTotalPowerSupplyCapacity_Object = MibTableColumn
axTotalPowerSupplyCapacity = _AxTotalPowerSupplyCapacity_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 1002, 1, 3, 1, 10),
    _AxTotalPowerSupplyCapacity_Type()
)
axTotalPowerSupplyCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axTotalPowerSupplyCapacity.setStatus("current")
_AxPowerSupplyCapacitySourceA_Type = Integer32
_AxPowerSupplyCapacitySourceA_Object = MibTableColumn
axPowerSupplyCapacitySourceA = _AxPowerSupplyCapacitySourceA_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 1002, 1, 3, 1, 11),
    _AxPowerSupplyCapacitySourceA_Type()
)
axPowerSupplyCapacitySourceA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axPowerSupplyCapacitySourceA.setStatus("current")
_AxPowerSupplyCapacitySourceB_Type = Integer32
_AxPowerSupplyCapacitySourceB_Object = MibTableColumn
axPowerSupplyCapacitySourceB = _AxPowerSupplyCapacitySourceB_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 1002, 1, 3, 1, 12),
    _AxPowerSupplyCapacitySourceB_Type()
)
axPowerSupplyCapacitySourceB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axPowerSupplyCapacitySourceB.setStatus("current")
_AxTotalPowerAllocated_Type = Integer32
_AxTotalPowerAllocated_Object = MibTableColumn
axTotalPowerAllocated = _AxTotalPowerAllocated_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 1002, 1, 3, 1, 13),
    _AxTotalPowerAllocated_Type()
)
axTotalPowerAllocated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axTotalPowerAllocated.setStatus("current")
_AxTotalPowerAvailable_Type = Integer32
_AxTotalPowerAvailable_Object = MibTableColumn
axTotalPowerAvailable = _AxTotalPowerAvailable_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 1002, 1, 3, 1, 14),
    _AxTotalPowerAvailable_Type()
)
axTotalPowerAvailable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axTotalPowerAvailable.setStatus("current")
_AxRedundantPowerAvailable_Type = Integer32
_AxRedundantPowerAvailable_Object = MibTableColumn
axRedundantPowerAvailable = _AxRedundantPowerAvailable_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 1002, 1, 3, 1, 15),
    _AxRedundantPowerAvailable_Type()
)
axRedundantPowerAvailable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axRedundantPowerAvailable.setStatus("current")
_AxPowerAvailableSourceA_Type = Integer32
_AxPowerAvailableSourceA_Object = MibTableColumn
axPowerAvailableSourceA = _AxPowerAvailableSourceA_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 1002, 1, 3, 1, 16),
    _AxPowerAvailableSourceA_Type()
)
axPowerAvailableSourceA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axPowerAvailableSourceA.setStatus("current")
_AxPowerAvailableSourceB_Type = Integer32
_AxPowerAvailableSourceB_Object = MibTableColumn
axPowerAvailableSourceB = _AxPowerAvailableSourceB_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 1002, 1, 3, 1, 17),
    _AxPowerAvailableSourceB_Type()
)
axPowerAvailableSourceB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axPowerAvailableSourceB.setStatus("current")
_AxChassisSystemTraps_ObjectIdentity = ObjectIdentity
axChassisSystemTraps = _AxChassisSystemTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 1002, 1, 3, 2)
)
_AxChassisSystemTrapsPrefix_ObjectIdentity = ObjectIdentity
axChassisSystemTrapsPrefix = _AxChassisSystemTrapsPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 1002, 1, 3, 2, 0)
)
_AxPowerSupplyUnitTable_Object = MibTable
axPowerSupplyUnitTable = _AxPowerSupplyUnitTable_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 1002, 1, 4)
)
if mibBuilder.loadTexts:
    axPowerSupplyUnitTable.setStatus("current")
_AxPowerSupplyUnitEntry_Object = MibTableRow
axPowerSupplyUnitEntry = _AxPowerSupplyUnitEntry_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 1002, 1, 4, 1)
)
axPowerSupplyUnitEntry.setIndexNames(
    (0, "AX-DEVICE-MIB", "axChassisIndex"),
    (0, "AX-DEVICE-MIB", "axPowerSupplyUnitIndex"),
)
if mibBuilder.loadTexts:
    axPowerSupplyUnitEntry.setStatus("current")
_AxPowerSupplyUnitIndex_Type = Integer32
_AxPowerSupplyUnitIndex_Object = MibTableColumn
axPowerSupplyUnitIndex = _AxPowerSupplyUnitIndex_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 1002, 1, 4, 1, 1),
    _AxPowerSupplyUnitIndex_Type()
)
axPowerSupplyUnitIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    axPowerSupplyUnitIndex.setStatus("current")
_AxPowerSupplyName_Type = DisplayString
_AxPowerSupplyName_Object = MibTableColumn
axPowerSupplyName = _AxPowerSupplyName_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 1002, 1, 4, 1, 2),
    _AxPowerSupplyName_Type()
)
axPowerSupplyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axPowerSupplyName.setStatus("current")
_AxPowerSupplyAbbreviation_Type = DisplayString
_AxPowerSupplyAbbreviation_Object = MibTableColumn
axPowerSupplyAbbreviation = _AxPowerSupplyAbbreviation_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 1002, 1, 4, 1, 3),
    _AxPowerSupplyAbbreviation_Type()
)
axPowerSupplyAbbreviation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axPowerSupplyAbbreviation.setStatus("current")
_AxPowerSupplySerialInformation_Type = DisplayString
_AxPowerSupplySerialInformation_Object = MibTableColumn
axPowerSupplySerialInformation = _AxPowerSupplySerialInformation_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 1002, 1, 4, 1, 4),
    _AxPowerSupplySerialInformation_Type()
)
axPowerSupplySerialInformation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axPowerSupplySerialInformation.setStatus("current")


class _AxPowerSupplyInputVoltage_Type(Integer32):
    """Custom type axPowerSupplyInputVoltage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              99)
        )
    )
    namedValues = NamedValues(
        *(("ac100V120V", 1),
          ("ac200V240V", 2),
          ("dc48V", 3),
          ("dc380V", 4),
          ("unknown", 99))
    )


_AxPowerSupplyInputVoltage_Type.__name__ = "Integer32"
_AxPowerSupplyInputVoltage_Object = MibTableColumn
axPowerSupplyInputVoltage = _AxPowerSupplyInputVoltage_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 1002, 1, 4, 1, 5),
    _AxPowerSupplyInputVoltage_Type()
)
axPowerSupplyInputVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axPowerSupplyInputVoltage.setStatus("current")


class _AxPowerSupplyConnectStatus_Type(Integer32):
    """Custom type axPowerSupplyConnectStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("connect", 1),
          ("notconnect", 2))
    )


_AxPowerSupplyConnectStatus_Type.__name__ = "Integer32"
_AxPowerSupplyConnectStatus_Object = MibTableColumn
axPowerSupplyConnectStatus = _AxPowerSupplyConnectStatus_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 1002, 1, 4, 1, 6),
    _AxPowerSupplyConnectStatus_Type()
)
axPowerSupplyConnectStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axPowerSupplyConnectStatus.setStatus("current")


class _AxPowerSupplyStatus_Type(Integer32):
    """Custom type axPowerSupplyStatus based on Integer32"""
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
        *(("active", 1),
          ("fault", 2),
          ("connect", 3),
          ("notconnect", 4),
          ("notsupport", 5))
    )


_AxPowerSupplyStatus_Type.__name__ = "Integer32"
_AxPowerSupplyStatus_Object = MibTableColumn
axPowerSupplyStatus = _AxPowerSupplyStatus_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 1002, 1, 4, 1, 7),
    _AxPowerSupplyStatus_Type()
)
axPowerSupplyStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axPowerSupplyStatus.setStatus("current")
_AxPowerSupplyTotalAccumRunTime_Type = Integer32
_AxPowerSupplyTotalAccumRunTime_Object = MibTableColumn
axPowerSupplyTotalAccumRunTime = _AxPowerSupplyTotalAccumRunTime_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 1002, 1, 4, 1, 8),
    _AxPowerSupplyTotalAccumRunTime_Type()
)
axPowerSupplyTotalAccumRunTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axPowerSupplyTotalAccumRunTime.setStatus("current")
_AxPowerSupplyCautionAccumRunTime_Type = Integer32
_AxPowerSupplyCautionAccumRunTime_Object = MibTableColumn
axPowerSupplyCautionAccumRunTime = _AxPowerSupplyCautionAccumRunTime_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 1002, 1, 4, 1, 9),
    _AxPowerSupplyCautionAccumRunTime_Type()
)
axPowerSupplyCautionAccumRunTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axPowerSupplyCautionAccumRunTime.setStatus("current")
_AxPowerSupplyCriticalAccumRunTime_Type = Integer32
_AxPowerSupplyCriticalAccumRunTime_Object = MibTableColumn
axPowerSupplyCriticalAccumRunTime = _AxPowerSupplyCriticalAccumRunTime_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 1002, 1, 4, 1, 10),
    _AxPowerSupplyCriticalAccumRunTime_Type()
)
axPowerSupplyCriticalAccumRunTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axPowerSupplyCriticalAccumRunTime.setStatus("current")
_AxPowerSupplyElapsedTime_Type = Integer32
_AxPowerSupplyElapsedTime_Object = MibTableColumn
axPowerSupplyElapsedTime = _AxPowerSupplyElapsedTime_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 1002, 1, 4, 1, 11),
    _AxPowerSupplyElapsedTime_Type()
)
axPowerSupplyElapsedTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axPowerSupplyElapsedTime.setStatus("current")
_AxPowerSupplyUnitTraps_ObjectIdentity = ObjectIdentity
axPowerSupplyUnitTraps = _AxPowerSupplyUnitTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 1002, 1, 4, 2)
)
_AxPowerSupplyUnitTrapsPrefix_ObjectIdentity = ObjectIdentity
axPowerSupplyUnitTrapsPrefix = _AxPowerSupplyUnitTrapsPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 1002, 1, 4, 2, 0)
)
_AxFanUnitTable_Object = MibTable
axFanUnitTable = _AxFanUnitTable_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 1002, 1, 5)
)
if mibBuilder.loadTexts:
    axFanUnitTable.setStatus("current")
_AxFanUnitEntry_Object = MibTableRow
axFanUnitEntry = _AxFanUnitEntry_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 1002, 1, 5, 1)
)
axFanUnitEntry.setIndexNames(
    (0, "AX-DEVICE-MIB", "axChassisIndex"),
    (0, "AX-DEVICE-MIB", "axFanUnitIndex"),
)
if mibBuilder.loadTexts:
    axFanUnitEntry.setStatus("current")
_AxFanUnitIndex_Type = Integer32
_AxFanUnitIndex_Object = MibTableColumn
axFanUnitIndex = _AxFanUnitIndex_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 1002, 1, 5, 1, 1),
    _AxFanUnitIndex_Type()
)
axFanUnitIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    axFanUnitIndex.setStatus("current")
_AxFanUnitName_Type = DisplayString
_AxFanUnitName_Object = MibTableColumn
axFanUnitName = _AxFanUnitName_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 1002, 1, 5, 1, 2),
    _AxFanUnitName_Type()
)
axFanUnitName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axFanUnitName.setStatus("current")
_AxFanUnitAbbreviation_Type = DisplayString
_AxFanUnitAbbreviation_Object = MibTableColumn
axFanUnitAbbreviation = _AxFanUnitAbbreviation_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 1002, 1, 5, 1, 3),
    _AxFanUnitAbbreviation_Type()
)
axFanUnitAbbreviation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axFanUnitAbbreviation.setStatus("current")
_AxFanUnitSerialInformation_Type = DisplayString
_AxFanUnitSerialInformation_Object = MibTableColumn
axFanUnitSerialInformation = _AxFanUnitSerialInformation_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 1002, 1, 5, 1, 4),
    _AxFanUnitSerialInformation_Type()
)
axFanUnitSerialInformation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axFanUnitSerialInformation.setStatus("current")


class _AxFanUnitStatus_Type(Integer32):
    """Custom type axFanUnitStatus based on Integer32"""
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
        *(("active", 1),
          ("fault", 2),
          ("notconnect", 3),
          ("notsupport", 4))
    )


_AxFanUnitStatus_Type.__name__ = "Integer32"
_AxFanUnitStatus_Object = MibTableColumn
axFanUnitStatus = _AxFanUnitStatus_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 1002, 1, 5, 1, 5),
    _AxFanUnitStatus_Type()
)
axFanUnitStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axFanUnitStatus.setStatus("current")
_AxFanUnitSpeed_Type = Integer32
_AxFanUnitSpeed_Object = MibTableColumn
axFanUnitSpeed = _AxFanUnitSpeed_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 1002, 1, 5, 1, 6),
    _AxFanUnitSpeed_Type()
)
axFanUnitSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axFanUnitSpeed.setStatus("current")
_AxFanUnitTotalAccumRunTime_Type = Integer32
_AxFanUnitTotalAccumRunTime_Object = MibTableColumn
axFanUnitTotalAccumRunTime = _AxFanUnitTotalAccumRunTime_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 1002, 1, 5, 1, 8),
    _AxFanUnitTotalAccumRunTime_Type()
)
axFanUnitTotalAccumRunTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axFanUnitTotalAccumRunTime.setStatus("current")
_AxFanUnitCautionAccumRunTime_Type = Integer32
_AxFanUnitCautionAccumRunTime_Object = MibTableColumn
axFanUnitCautionAccumRunTime = _AxFanUnitCautionAccumRunTime_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 1002, 1, 5, 1, 9),
    _AxFanUnitCautionAccumRunTime_Type()
)
axFanUnitCautionAccumRunTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axFanUnitCautionAccumRunTime.setStatus("current")
_AxFanUnitCriticalAccumRunTime_Type = Integer32
_AxFanUnitCriticalAccumRunTime_Object = MibTableColumn
axFanUnitCriticalAccumRunTime = _AxFanUnitCriticalAccumRunTime_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 1002, 1, 5, 1, 10),
    _AxFanUnitCriticalAccumRunTime_Type()
)
axFanUnitCriticalAccumRunTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axFanUnitCriticalAccumRunTime.setStatus("current")
_AxFanUnitElapsedTime_Type = Integer32
_AxFanUnitElapsedTime_Object = MibTableColumn
axFanUnitElapsedTime = _AxFanUnitElapsedTime_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 1002, 1, 5, 1, 11),
    _AxFanUnitElapsedTime_Type()
)
axFanUnitElapsedTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axFanUnitElapsedTime.setStatus("current")
_AxFanUnitLedStatus_Type = Integer32
_AxFanUnitLedStatus_Object = MibTableColumn
axFanUnitLedStatus = _AxFanUnitLedStatus_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 1002, 1, 5, 1, 12),
    _AxFanUnitLedStatus_Type()
)
axFanUnitLedStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axFanUnitLedStatus.setStatus("current")
_AxAirFanUnitTraps_ObjectIdentity = ObjectIdentity
axAirFanUnitTraps = _AxAirFanUnitTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 1002, 1, 5, 2)
)
_AxAirFanUnitTrapsPrefix_ObjectIdentity = ObjectIdentity
axAirFanUnitTrapsPrefix = _AxAirFanUnitTrapsPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 1002, 1, 5, 2, 0)
)
_AxBcuBoard_ObjectIdentity = ObjectIdentity
axBcuBoard = _AxBcuBoard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 1002, 2)
)
_AxBcuBoardTable_Object = MibTable
axBcuBoardTable = _AxBcuBoardTable_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 1002, 2, 1)
)
if mibBuilder.loadTexts:
    axBcuBoardTable.setStatus("current")
_AxBcuBoardEntry_Object = MibTableRow
axBcuBoardEntry = _AxBcuBoardEntry_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 1002, 2, 1, 1)
)
axBcuBoardEntry.setIndexNames(
    (0, "AX-DEVICE-MIB", "axChassisIndex"),
    (0, "AX-DEVICE-MIB", "axBcuBoardIndex"),
)
if mibBuilder.loadTexts:
    axBcuBoardEntry.setStatus("current")
_AxBcuBoardIndex_Type = Integer32
_AxBcuBoardIndex_Object = MibTableColumn
axBcuBoardIndex = _AxBcuBoardIndex_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 1002, 2, 1, 1, 1),
    _AxBcuBoardIndex_Type()
)
axBcuBoardIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    axBcuBoardIndex.setStatus("current")


class _AxBcuOperLedStatus_Type(Bits):
    """Custom type axBcuOperLedStatus based on Bits"""
    namedValues = NamedValues(
        *(("unknown", 0),
          ("notconnect", 1),
          ("lightOff", 2),
          ("green", 3),
          ("greenBlink", 4),
          ("red", 5))
    )

_AxBcuOperLedStatus_Type.__name__ = "Bits"
_AxBcuOperLedStatus_Object = MibTableColumn
axBcuOperLedStatus = _AxBcuOperLedStatus_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 1002, 2, 1, 1, 2),
    _AxBcuOperLedStatus_Type()
)
axBcuOperLedStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axBcuOperLedStatus.setStatus("current")


class _AxBcuOperModeStatus_Type(Bits):
    """Custom type axBcuOperModeStatus based on Bits"""
    namedValues = NamedValues(
        *(("unknown", 0),
          ("initialize", 1),
          ("active", 2),
          ("standby", 3),
          ("standbyConfigrationDiscord", 4),
          ("standbySoftwareVersionDiscord", 5),
          ("fault", 7),
          ("inactive", 8),
          ("notconnect", 9),
          ("notsupport", 10),
          ("faultRestrained", 11))
    )

_AxBcuOperModeStatus_Type.__name__ = "Bits"
_AxBcuOperModeStatus_Object = MibTableColumn
axBcuOperModeStatus = _AxBcuOperModeStatus_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 1002, 2, 1, 1, 3),
    _AxBcuOperModeStatus_Type()
)
axBcuOperModeStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axBcuOperModeStatus.setStatus("current")


class _AxBcuActiveLedStatus_Type(Bits):
    """Custom type axBcuActiveLedStatus based on Bits"""
    namedValues = NamedValues(
        *(("unknown", 0),
          ("notconnect", 1),
          ("lightOff", 2),
          ("green", 3))
    )

_AxBcuActiveLedStatus_Type.__name__ = "Bits"
_AxBcuActiveLedStatus_Object = MibTableColumn
axBcuActiveLedStatus = _AxBcuActiveLedStatus_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 1002, 2, 1, 1, 4),
    _AxBcuActiveLedStatus_Type()
)
axBcuActiveLedStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axBcuActiveLedStatus.setStatus("current")


class _AxBcuSystem1LedStatus_Type(Bits):
    """Custom type axBcuSystem1LedStatus based on Bits"""
    namedValues = NamedValues(
        *(("unknown", 0),
          ("notconnect", 1),
          ("lightOff", 2),
          ("green", 3),
          ("greenBlink", 4),
          ("red", 5))
    )

_AxBcuSystem1LedStatus_Type.__name__ = "Bits"
_AxBcuSystem1LedStatus_Object = MibTableColumn
axBcuSystem1LedStatus = _AxBcuSystem1LedStatus_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 1002, 2, 1, 1, 5),
    _AxBcuSystem1LedStatus_Type()
)
axBcuSystem1LedStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axBcuSystem1LedStatus.setStatus("current")


class _AxBcuSystem2LedStatus_Type(Bits):
    """Custom type axBcuSystem2LedStatus based on Bits"""
    namedValues = NamedValues(
        *(("unknown", 0),
          ("notconnect", 1),
          ("lightOff", 2),
          ("green", 3),
          ("greenBlink", 4),
          ("red", 5))
    )

_AxBcuSystem2LedStatus_Type.__name__ = "Bits"
_AxBcuSystem2LedStatus_Object = MibTableColumn
axBcuSystem2LedStatus = _AxBcuSystem2LedStatus_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 1002, 2, 1, 1, 6),
    _AxBcuSystem2LedStatus_Type()
)
axBcuSystem2LedStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axBcuSystem2LedStatus.setStatus("current")
_AxBcuBoardName_Type = DisplayString
_AxBcuBoardName_Object = MibTableColumn
axBcuBoardName = _AxBcuBoardName_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 1002, 2, 1, 1, 7),
    _AxBcuBoardName_Type()
)
axBcuBoardName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axBcuBoardName.setStatus("current")
_AxBcuBoardAbbreviation_Type = DisplayString
_AxBcuBoardAbbreviation_Object = MibTableColumn
axBcuBoardAbbreviation = _AxBcuBoardAbbreviation_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 1002, 2, 1, 1, 8),
    _AxBcuBoardAbbreviation_Type()
)
axBcuBoardAbbreviation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axBcuBoardAbbreviation.setStatus("current")
_AxBcuSoftwareVersion_Type = DisplayString
_AxBcuSoftwareVersion_Object = MibTableColumn
axBcuSoftwareVersion = _AxBcuSoftwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 1002, 2, 1, 1, 9),
    _AxBcuSoftwareVersion_Type()
)
axBcuSoftwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axBcuSoftwareVersion.setStatus("current")
_AxBcuFlashTotalSize_Type = Integer32
_AxBcuFlashTotalSize_Object = MibTableColumn
axBcuFlashTotalSize = _AxBcuFlashTotalSize_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 1002, 2, 1, 1, 20),
    _AxBcuFlashTotalSize_Type()
)
axBcuFlashTotalSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axBcuFlashTotalSize.setStatus("current")
_AxBcuFlashUsedSize_Type = Integer32
_AxBcuFlashUsedSize_Object = MibTableColumn
axBcuFlashUsedSize = _AxBcuFlashUsedSize_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 1002, 2, 1, 1, 21),
    _AxBcuFlashUsedSize_Type()
)
axBcuFlashUsedSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axBcuFlashUsedSize.setStatus("current")
_AxBcuFlashFreeSize_Type = Integer32
_AxBcuFlashFreeSize_Object = MibTableColumn
axBcuFlashFreeSize = _AxBcuFlashFreeSize_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 1002, 2, 1, 1, 22),
    _AxBcuFlashFreeSize_Type()
)
axBcuFlashFreeSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axBcuFlashFreeSize.setStatus("current")
_AxBcuTemperatureStatusNumber_Type = Integer32
_AxBcuTemperatureStatusNumber_Object = MibTableColumn
axBcuTemperatureStatusNumber = _AxBcuTemperatureStatusNumber_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 1002, 2, 1, 1, 23),
    _AxBcuTemperatureStatusNumber_Type()
)
axBcuTemperatureStatusNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axBcuTemperatureStatusNumber.setStatus("current")
_AxBcuSerialInformation_Type = DisplayString
_AxBcuSerialInformation_Object = MibTableColumn
axBcuSerialInformation = _AxBcuSerialInformation_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 1002, 2, 1, 1, 24),
    _AxBcuSerialInformation_Type()
)
axBcuSerialInformation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axBcuSerialInformation.setStatus("current")
_AxBcuTotalAccumRunTime_Type = Integer32
_AxBcuTotalAccumRunTime_Object = MibTableColumn
axBcuTotalAccumRunTime = _AxBcuTotalAccumRunTime_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 1002, 2, 1, 1, 25),
    _AxBcuTotalAccumRunTime_Type()
)
axBcuTotalAccumRunTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axBcuTotalAccumRunTime.setStatus("current")
_AxBcuCautionAccumRunTime_Type = Integer32
_AxBcuCautionAccumRunTime_Object = MibTableColumn
axBcuCautionAccumRunTime = _AxBcuCautionAccumRunTime_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 1002, 2, 1, 1, 26),
    _AxBcuCautionAccumRunTime_Type()
)
axBcuCautionAccumRunTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axBcuCautionAccumRunTime.setStatus("current")
_AxBcuCriticalAccumRunTime_Type = Integer32
_AxBcuCriticalAccumRunTime_Object = MibTableColumn
axBcuCriticalAccumRunTime = _AxBcuCriticalAccumRunTime_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 1002, 2, 1, 1, 27),
    _AxBcuCriticalAccumRunTime_Type()
)
axBcuCriticalAccumRunTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axBcuCriticalAccumRunTime.setStatus("current")
_AxBcuElapsedTime_Type = Integer32
_AxBcuElapsedTime_Object = MibTableColumn
axBcuElapsedTime = _AxBcuElapsedTime_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 1002, 2, 1, 1, 28),
    _AxBcuElapsedTime_Type()
)
axBcuElapsedTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axBcuElapsedTime.setStatus("current")
_AxBcuBoardTraps_ObjectIdentity = ObjectIdentity
axBcuBoardTraps = _AxBcuBoardTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 1002, 2, 1, 2)
)
_AxBcuBoardTrapsPrefix_ObjectIdentity = ObjectIdentity
axBcuBoardTrapsPrefix = _AxBcuBoardTrapsPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 1002, 2, 1, 2, 0)
)
_AxBcuTemperatureStatusTable_Object = MibTable
axBcuTemperatureStatusTable = _AxBcuTemperatureStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 1002, 2, 2)
)
if mibBuilder.loadTexts:
    axBcuTemperatureStatusTable.setStatus("current")
_AxBcuTemperatureStatusEntry_Object = MibTableRow
axBcuTemperatureStatusEntry = _AxBcuTemperatureStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 1002, 2, 2, 1)
)
axBcuTemperatureStatusEntry.setIndexNames(
    (0, "AX-DEVICE-MIB", "axChassisIndex"),
    (0, "AX-DEVICE-MIB", "axBcuBoardIndex"),
    (0, "AX-DEVICE-MIB", "axBcuTemperatureStatusIndex"),
)
if mibBuilder.loadTexts:
    axBcuTemperatureStatusEntry.setStatus("current")
_AxBcuTemperatureStatusIndex_Type = Integer32
_AxBcuTemperatureStatusIndex_Object = MibTableColumn
axBcuTemperatureStatusIndex = _AxBcuTemperatureStatusIndex_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 1002, 2, 2, 1, 1),
    _AxBcuTemperatureStatusIndex_Type()
)
axBcuTemperatureStatusIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    axBcuTemperatureStatusIndex.setStatus("current")
_AxBcuTemperatureStatusDescr_Type = DisplayString
_AxBcuTemperatureStatusDescr_Object = MibTableColumn
axBcuTemperatureStatusDescr = _AxBcuTemperatureStatusDescr_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 1002, 2, 2, 1, 2),
    _AxBcuTemperatureStatusDescr_Type()
)
axBcuTemperatureStatusDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axBcuTemperatureStatusDescr.setStatus("current")
_AxBcuTemperatureStatusValue_Type = Integer32
_AxBcuTemperatureStatusValue_Object = MibTableColumn
axBcuTemperatureStatusValue = _AxBcuTemperatureStatusValue_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 1002, 2, 2, 1, 3),
    _AxBcuTemperatureStatusValue_Type()
)
axBcuTemperatureStatusValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axBcuTemperatureStatusValue.setStatus("current")
_AxBcuTemperatureThreshold_Type = Integer32
_AxBcuTemperatureThreshold_Object = MibTableColumn
axBcuTemperatureThreshold = _AxBcuTemperatureThreshold_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 1002, 2, 2, 1, 4),
    _AxBcuTemperatureThreshold_Type()
)
axBcuTemperatureThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axBcuTemperatureThreshold.setStatus("current")
_AxBcuTemperatureState_Type = Integer32
_AxBcuTemperatureState_Object = MibTableColumn
axBcuTemperatureState = _AxBcuTemperatureState_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 1002, 2, 2, 1, 5),
    _AxBcuTemperatureState_Type()
)
axBcuTemperatureState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axBcuTemperatureState.setStatus("current")
_AxBcuTemperatureWarning_Type = Integer32
_AxBcuTemperatureWarning_Object = MibTableColumn
axBcuTemperatureWarning = _AxBcuTemperatureWarning_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 1002, 2, 2, 1, 6),
    _AxBcuTemperatureWarning_Type()
)
axBcuTemperatureWarning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axBcuTemperatureWarning.setStatus("current")
_AxBcuTemperatureWarningAverage_Type = Integer32
_AxBcuTemperatureWarningAverage_Object = MibTableColumn
axBcuTemperatureWarningAverage = _AxBcuTemperatureWarningAverage_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 1002, 2, 2, 1, 7),
    _AxBcuTemperatureWarningAverage_Type()
)
axBcuTemperatureWarningAverage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axBcuTemperatureWarningAverage.setStatus("current")
_AxBcuTemperatureWarningAveragePeriod_Type = Integer32
_AxBcuTemperatureWarningAveragePeriod_Object = MibTableColumn
axBcuTemperatureWarningAveragePeriod = _AxBcuTemperatureWarningAveragePeriod_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 1002, 2, 2, 1, 8),
    _AxBcuTemperatureWarningAveragePeriod_Type()
)
axBcuTemperatureWarningAveragePeriod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axBcuTemperatureWarningAveragePeriod.setStatus("current")
_AxBcuTemperatureTraps_ObjectIdentity = ObjectIdentity
axBcuTemperatureTraps = _AxBcuTemperatureTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 1002, 2, 2, 2)
)
_AxBcuTemperatureTrapsPrefix_ObjectIdentity = ObjectIdentity
axBcuTemperatureTrapsPrefix = _AxBcuTemperatureTrapsPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 1002, 2, 2, 2, 0)
)
_AxMemoryCardTable_Object = MibTable
axMemoryCardTable = _AxMemoryCardTable_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 1002, 2, 3)
)
if mibBuilder.loadTexts:
    axMemoryCardTable.setStatus("current")
_AxMemoryCardEntry_Object = MibTableRow
axMemoryCardEntry = _AxMemoryCardEntry_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 1002, 2, 3, 1)
)
axMemoryCardEntry.setIndexNames(
    (0, "AX-DEVICE-MIB", "axChassisIndex"),
    (0, "AX-DEVICE-MIB", "axBcuBoardIndex"),
    (0, "AX-DEVICE-MIB", "axMemoryCardIndex"),
)
if mibBuilder.loadTexts:
    axMemoryCardEntry.setStatus("current")
_AxMemoryCardIndex_Type = Integer32
_AxMemoryCardIndex_Object = MibTableColumn
axMemoryCardIndex = _AxMemoryCardIndex_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 1002, 2, 3, 1, 1),
    _AxMemoryCardIndex_Type()
)
axMemoryCardIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    axMemoryCardIndex.setStatus("current")


class _AxMemoryCardConnection_Type(Integer32):
    """Custom type axMemoryCardConnection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("connect", 1),
          ("notconnect", 2),
          ("unknown", 3))
    )


_AxMemoryCardConnection_Type.__name__ = "Integer32"
_AxMemoryCardConnection_Object = MibTableColumn
axMemoryCardConnection = _AxMemoryCardConnection_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 1002, 2, 3, 1, 2),
    _AxMemoryCardConnection_Type()
)
axMemoryCardConnection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axMemoryCardConnection.setStatus("current")
_AxMemoryCardID_Type = OctetString
_AxMemoryCardID_Object = MibTableColumn
axMemoryCardID = _AxMemoryCardID_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 1002, 2, 3, 1, 3),
    _AxMemoryCardID_Type()
)
axMemoryCardID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axMemoryCardID.setStatus("current")
_AxMemoryCardTotalSize_Type = Integer32
_AxMemoryCardTotalSize_Object = MibTableColumn
axMemoryCardTotalSize = _AxMemoryCardTotalSize_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 1002, 2, 3, 1, 4),
    _AxMemoryCardTotalSize_Type()
)
axMemoryCardTotalSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axMemoryCardTotalSize.setStatus("current")
_AxMemoryCardUsedSize_Type = Integer32
_AxMemoryCardUsedSize_Object = MibTableColumn
axMemoryCardUsedSize = _AxMemoryCardUsedSize_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 1002, 2, 3, 1, 5),
    _AxMemoryCardUsedSize_Type()
)
axMemoryCardUsedSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axMemoryCardUsedSize.setStatus("current")
_AxMemoryCardFreeSize_Type = Integer32
_AxMemoryCardFreeSize_Object = MibTableColumn
axMemoryCardFreeSize = _AxMemoryCardFreeSize_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 1002, 2, 3, 1, 6),
    _AxMemoryCardFreeSize_Type()
)
axMemoryCardFreeSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axMemoryCardFreeSize.setStatus("current")
_AxBcuCpuTable_Object = MibTable
axBcuCpuTable = _AxBcuCpuTable_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 1002, 2, 4)
)
if mibBuilder.loadTexts:
    axBcuCpuTable.setStatus("current")
_AxBcuCpuEntry_Object = MibTableRow
axBcuCpuEntry = _AxBcuCpuEntry_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 1002, 2, 4, 1)
)
axBcuCpuEntry.setIndexNames(
    (0, "AX-DEVICE-MIB", "axChassisIndex"),
    (0, "AX-DEVICE-MIB", "axBcuBoardIndex"),
    (0, "AX-DEVICE-MIB", "axBcuCpuIndex"),
)
if mibBuilder.loadTexts:
    axBcuCpuEntry.setStatus("current")


class _AxBcuCpuIndex_Type(Integer32):
    """Custom type axBcuCpuIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("bcucpu", 1),
          ("pa", 2))
    )


_AxBcuCpuIndex_Type.__name__ = "Integer32"
_AxBcuCpuIndex_Object = MibTableColumn
axBcuCpuIndex = _AxBcuCpuIndex_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 1002, 2, 4, 1, 1),
    _AxBcuCpuIndex_Type()
)
axBcuCpuIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    axBcuCpuIndex.setStatus("current")


class _AxBcuCpuStatus_Type(Bits):
    """Custom type axBcuCpuStatus based on Bits"""
    namedValues = NamedValues(
        *(("unknown", 0),
          ("initialize", 1),
          ("active", 2),
          ("fault", 3),
          ("notconnect", 4))
    )

_AxBcuCpuStatus_Type.__name__ = "Bits"
_AxBcuCpuStatus_Object = MibTableColumn
axBcuCpuStatus = _AxBcuCpuStatus_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 1002, 2, 4, 1, 2),
    _AxBcuCpuStatus_Type()
)
axBcuCpuStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axBcuCpuStatus.setStatus("current")
_AxBcuCpuUpTime_Type = DisplayString
_AxBcuCpuUpTime_Object = MibTableColumn
axBcuCpuUpTime = _AxBcuCpuUpTime_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 1002, 2, 4, 1, 3),
    _AxBcuCpuUpTime_Type()
)
axBcuCpuUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axBcuCpuUpTime.setStatus("current")
_AxBcuCpuClock_Type = Integer32
_AxBcuCpuClock_Object = MibTableColumn
axBcuCpuClock = _AxBcuCpuClock_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 1002, 2, 4, 1, 4),
    _AxBcuCpuClock_Type()
)
axBcuCpuClock.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axBcuCpuClock.setStatus("current")
_AxBcuCpuLoad1m_Type = Integer32
_AxBcuCpuLoad1m_Object = MibTableColumn
axBcuCpuLoad1m = _AxBcuCpuLoad1m_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 1002, 2, 4, 1, 5),
    _AxBcuCpuLoad1m_Type()
)
axBcuCpuLoad1m.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axBcuCpuLoad1m.setStatus("current")
_AxBcuMemoryTotalSize_Type = Integer32
_AxBcuMemoryTotalSize_Object = MibTableColumn
axBcuMemoryTotalSize = _AxBcuMemoryTotalSize_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 1002, 2, 4, 1, 6),
    _AxBcuMemoryTotalSize_Type()
)
axBcuMemoryTotalSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axBcuMemoryTotalSize.setStatus("current")
_AxBcuMemoryUsedSize_Type = Integer32
_AxBcuMemoryUsedSize_Object = MibTableColumn
axBcuMemoryUsedSize = _AxBcuMemoryUsedSize_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 1002, 2, 4, 1, 7),
    _AxBcuMemoryUsedSize_Type()
)
axBcuMemoryUsedSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axBcuMemoryUsedSize.setStatus("current")
_AxBcuMemoryFreeSize_Type = Integer32
_AxBcuMemoryFreeSize_Object = MibTableColumn
axBcuMemoryFreeSize = _AxBcuMemoryFreeSize_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 1002, 2, 4, 1, 8),
    _AxBcuMemoryFreeSize_Type()
)
axBcuMemoryFreeSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axBcuMemoryFreeSize.setStatus("current")
_AxBcuFatalErrorRestartNum_Type = Integer32
_AxBcuFatalErrorRestartNum_Object = MibTableColumn
axBcuFatalErrorRestartNum = _AxBcuFatalErrorRestartNum_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 1002, 2, 4, 1, 9),
    _AxBcuFatalErrorRestartNum_Type()
)
axBcuFatalErrorRestartNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axBcuFatalErrorRestartNum.setStatus("current")
_AxSfuBoard_ObjectIdentity = ObjectIdentity
axSfuBoard = _AxSfuBoard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 1002, 3)
)
_AxSfuBoardTable_Object = MibTable
axSfuBoardTable = _AxSfuBoardTable_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 1002, 3, 1)
)
if mibBuilder.loadTexts:
    axSfuBoardTable.setStatus("current")
_AxSfuBoardEntry_Object = MibTableRow
axSfuBoardEntry = _AxSfuBoardEntry_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 1002, 3, 1, 1)
)
axSfuBoardEntry.setIndexNames(
    (0, "AX-DEVICE-MIB", "axChassisIndex"),
    (0, "AX-DEVICE-MIB", "axSfuBoardIndex"),
)
if mibBuilder.loadTexts:
    axSfuBoardEntry.setStatus("current")
_AxSfuBoardIndex_Type = Integer32
_AxSfuBoardIndex_Object = MibTableColumn
axSfuBoardIndex = _AxSfuBoardIndex_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 1002, 3, 1, 1, 1),
    _AxSfuBoardIndex_Type()
)
axSfuBoardIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    axSfuBoardIndex.setStatus("current")
_AxSfuBoardType_Type = Integer32
_AxSfuBoardType_Object = MibTableColumn
axSfuBoardType = _AxSfuBoardType_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 1002, 3, 1, 1, 2),
    _AxSfuBoardType_Type()
)
axSfuBoardType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axSfuBoardType.setStatus("current")


class _AxSfuOperLedStatus_Type(Integer32):
    """Custom type axSfuOperLedStatus based on Integer32"""
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
        *(("unknown", 1),
          ("green", 2),
          ("greenblink", 3),
          ("red", 4),
          ("extinction", 5))
    )


_AxSfuOperLedStatus_Type.__name__ = "Integer32"
_AxSfuOperLedStatus_Object = MibTableColumn
axSfuOperLedStatus = _AxSfuOperLedStatus_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 1002, 3, 1, 1, 3),
    _AxSfuOperLedStatus_Type()
)
axSfuOperLedStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axSfuOperLedStatus.setStatus("current")


class _AxSfuActiveLedStatus_Type(Integer32):
    """Custom type axSfuActiveLedStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 1),
          ("green", 2),
          ("extinction", 3))
    )


_AxSfuActiveLedStatus_Type.__name__ = "Integer32"
_AxSfuActiveLedStatus_Object = MibTableColumn
axSfuActiveLedStatus = _AxSfuActiveLedStatus_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 1002, 3, 1, 1, 4),
    _AxSfuActiveLedStatus_Type()
)
axSfuActiveLedStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axSfuActiveLedStatus.setStatus("current")


class _AxSfuOperModeStatus_Type(Integer32):
    """Custom type axSfuOperModeStatus based on Integer32"""
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
              99)
        )
    )
    namedValues = NamedValues(
        *(("notconnect", 1),
          ("notsupport", 2),
          ("active", 3),
          ("initialize", 4),
          ("fault", 5),
          ("inactive", 6),
          ("disable", 7),
          ("unknown", 99))
    )


_AxSfuOperModeStatus_Type.__name__ = "Integer32"
_AxSfuOperModeStatus_Object = MibTableColumn
axSfuOperModeStatus = _AxSfuOperModeStatus_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 1002, 3, 1, 1, 5),
    _AxSfuOperModeStatus_Type()
)
axSfuOperModeStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axSfuOperModeStatus.setStatus("current")


class _AxSfuUpdateStatus_Type(Integer32):
    """Custom type axSfuUpdateStatus based on Integer32"""
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
        *(("none", 1),
          ("executing", 2),
          ("restartrequired", 3),
          ("failed", 4))
    )


_AxSfuUpdateStatus_Type.__name__ = "Integer32"
_AxSfuUpdateStatus_Object = MibTableColumn
axSfuUpdateStatus = _AxSfuUpdateStatus_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 1002, 3, 1, 1, 6),
    _AxSfuUpdateStatus_Type()
)
axSfuUpdateStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axSfuUpdateStatus.setStatus("current")
_AxSfuErrorRestartNum_Type = Integer32
_AxSfuErrorRestartNum_Object = MibTableColumn
axSfuErrorRestartNum = _AxSfuErrorRestartNum_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 1002, 3, 1, 1, 7),
    _AxSfuErrorRestartNum_Type()
)
axSfuErrorRestartNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axSfuErrorRestartNum.setStatus("current")
_AxSfuBoardName_Type = DisplayString
_AxSfuBoardName_Object = MibTableColumn
axSfuBoardName = _AxSfuBoardName_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 1002, 3, 1, 1, 8),
    _AxSfuBoardName_Type()
)
axSfuBoardName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axSfuBoardName.setStatus("current")
_AxSfuBoardAbbreviation_Type = DisplayString
_AxSfuBoardAbbreviation_Object = MibTableColumn
axSfuBoardAbbreviation = _AxSfuBoardAbbreviation_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 1002, 3, 1, 1, 9),
    _AxSfuBoardAbbreviation_Type()
)
axSfuBoardAbbreviation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axSfuBoardAbbreviation.setStatus("current")
_AxSfuSerialInformation_Type = DisplayString
_AxSfuSerialInformation_Object = MibTableColumn
axSfuSerialInformation = _AxSfuSerialInformation_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 1002, 3, 1, 1, 10),
    _AxSfuSerialInformation_Type()
)
axSfuSerialInformation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axSfuSerialInformation.setStatus("current")


class _AxSfuTemperatureState_Type(Integer32):
    """Custom type axSfuTemperatureState based on Integer32"""
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
        *(("unknown", 1),
          ("normal", 2),
          ("critical", 3),
          ("fault", 4))
    )


_AxSfuTemperatureState_Type.__name__ = "Integer32"
_AxSfuTemperatureState_Object = MibTableColumn
axSfuTemperatureState = _AxSfuTemperatureState_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 1002, 3, 1, 1, 11),
    _AxSfuTemperatureState_Type()
)
axSfuTemperatureState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axSfuTemperatureState.setStatus("current")
_AxSfuTotalAccumRunTime_Type = Integer32
_AxSfuTotalAccumRunTime_Object = MibTableColumn
axSfuTotalAccumRunTime = _AxSfuTotalAccumRunTime_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 1002, 3, 1, 1, 12),
    _AxSfuTotalAccumRunTime_Type()
)
axSfuTotalAccumRunTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axSfuTotalAccumRunTime.setStatus("current")
_AxSfuCautionAccumRunTime_Type = Integer32
_AxSfuCautionAccumRunTime_Object = MibTableColumn
axSfuCautionAccumRunTime = _AxSfuCautionAccumRunTime_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 1002, 3, 1, 1, 13),
    _AxSfuCautionAccumRunTime_Type()
)
axSfuCautionAccumRunTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axSfuCautionAccumRunTime.setStatus("current")
_AxSfuCriticalAccumRunTime_Type = Integer32
_AxSfuCriticalAccumRunTime_Object = MibTableColumn
axSfuCriticalAccumRunTime = _AxSfuCriticalAccumRunTime_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 1002, 3, 1, 1, 14),
    _AxSfuCriticalAccumRunTime_Type()
)
axSfuCriticalAccumRunTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axSfuCriticalAccumRunTime.setStatus("current")
_AxSfuElapsedTime_Type = Integer32
_AxSfuElapsedTime_Object = MibTableColumn
axSfuElapsedTime = _AxSfuElapsedTime_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 1002, 3, 1, 1, 15),
    _AxSfuElapsedTime_Type()
)
axSfuElapsedTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axSfuElapsedTime.setStatus("current")
_AxSfuBoardTraps_ObjectIdentity = ObjectIdentity
axSfuBoardTraps = _AxSfuBoardTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 1002, 3, 2)
)
_AxSfuStateChangeTrapPrefix_ObjectIdentity = ObjectIdentity
axSfuStateChangeTrapPrefix = _AxSfuStateChangeTrapPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 1002, 3, 2, 0)
)
_AxPruBoard_ObjectIdentity = ObjectIdentity
axPruBoard = _AxPruBoard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 1002, 4)
)
_AxPruBoardTable_Object = MibTable
axPruBoardTable = _AxPruBoardTable_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 1002, 4, 1)
)
if mibBuilder.loadTexts:
    axPruBoardTable.setStatus("current")
_AxPruBoardEntry_Object = MibTableRow
axPruBoardEntry = _AxPruBoardEntry_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 1002, 4, 1, 1)
)
axPruBoardEntry.setIndexNames(
    (0, "AX-DEVICE-MIB", "axChassisIndex"),
    (0, "AX-DEVICE-MIB", "axPruBoardIndex"),
)
if mibBuilder.loadTexts:
    axPruBoardEntry.setStatus("current")
_AxPruBoardIndex_Type = Integer32
_AxPruBoardIndex_Object = MibTableColumn
axPruBoardIndex = _AxPruBoardIndex_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 1002, 4, 1, 1, 1),
    _AxPruBoardIndex_Type()
)
axPruBoardIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    axPruBoardIndex.setStatus("current")
_AxPruBoardType_Type = Integer32
_AxPruBoardType_Object = MibTableColumn
axPruBoardType = _AxPruBoardType_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 1002, 4, 1, 1, 2),
    _AxPruBoardType_Type()
)
axPruBoardType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axPruBoardType.setStatus("current")


class _AxPruOperLedStatus_Type(Integer32):
    """Custom type axPruOperLedStatus based on Integer32"""
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
        *(("unknown", 1),
          ("green", 2),
          ("greenblink", 3),
          ("red", 4),
          ("extinction", 5))
    )


_AxPruOperLedStatus_Type.__name__ = "Integer32"
_AxPruOperLedStatus_Object = MibTableColumn
axPruOperLedStatus = _AxPruOperLedStatus_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 1002, 4, 1, 1, 3),
    _AxPruOperLedStatus_Type()
)
axPruOperLedStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axPruOperLedStatus.setStatus("current")


class _AxPruOperModeStatus_Type(Integer32):
    """Custom type axPruOperModeStatus based on Integer32"""
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
              99)
        )
    )
    namedValues = NamedValues(
        *(("notconnect", 1),
          ("notsupport", 2),
          ("active", 3),
          ("initialize", 4),
          ("fault", 5),
          ("inactive", 6),
          ("disable", 7),
          ("powershortage", 8),
          ("unknown", 99))
    )


_AxPruOperModeStatus_Type.__name__ = "Integer32"
_AxPruOperModeStatus_Object = MibTableColumn
axPruOperModeStatus = _AxPruOperModeStatus_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 1002, 4, 1, 1, 4),
    _AxPruOperModeStatus_Type()
)
axPruOperModeStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axPruOperModeStatus.setStatus("current")


class _AxPruUpdateStatus_Type(Integer32):
    """Custom type axPruUpdateStatus based on Integer32"""
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
        *(("none", 1),
          ("executing", 2),
          ("restartrequired", 3),
          ("failed", 4))
    )


_AxPruUpdateStatus_Type.__name__ = "Integer32"
_AxPruUpdateStatus_Object = MibTableColumn
axPruUpdateStatus = _AxPruUpdateStatus_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 1002, 4, 1, 1, 5),
    _AxPruUpdateStatus_Type()
)
axPruUpdateStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axPruUpdateStatus.setStatus("current")
_AxPruErrorRestartNum_Type = Integer32
_AxPruErrorRestartNum_Object = MibTableColumn
axPruErrorRestartNum = _AxPruErrorRestartNum_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 1002, 4, 1, 1, 6),
    _AxPruErrorRestartNum_Type()
)
axPruErrorRestartNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axPruErrorRestartNum.setStatus("current")
_AxPruBoardName_Type = DisplayString
_AxPruBoardName_Object = MibTableColumn
axPruBoardName = _AxPruBoardName_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 1002, 4, 1, 1, 7),
    _AxPruBoardName_Type()
)
axPruBoardName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axPruBoardName.setStatus("current")
_AxPruBoardAbbreviation_Type = DisplayString
_AxPruBoardAbbreviation_Object = MibTableColumn
axPruBoardAbbreviation = _AxPruBoardAbbreviation_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 1002, 4, 1, 1, 8),
    _AxPruBoardAbbreviation_Type()
)
axPruBoardAbbreviation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axPruBoardAbbreviation.setStatus("current")
_AxPruSerialInformation_Type = DisplayString
_AxPruSerialInformation_Object = MibTableColumn
axPruSerialInformation = _AxPruSerialInformation_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 1002, 4, 1, 1, 9),
    _AxPruSerialInformation_Type()
)
axPruSerialInformation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axPruSerialInformation.setStatus("current")
_AxPruCpuUpTime_Type = DisplayString
_AxPruCpuUpTime_Object = MibTableColumn
axPruCpuUpTime = _AxPruCpuUpTime_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 1002, 4, 1, 1, 10),
    _AxPruCpuUpTime_Type()
)
axPruCpuUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axPruCpuUpTime.setStatus("current")
_AxPruCpuClock_Type = Integer32
_AxPruCpuClock_Object = MibTableColumn
axPruCpuClock = _AxPruCpuClock_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 1002, 4, 1, 1, 11),
    _AxPruCpuClock_Type()
)
axPruCpuClock.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axPruCpuClock.setStatus("current")
_AxPruCpuLoad1m_Type = Integer32
_AxPruCpuLoad1m_Object = MibTableColumn
axPruCpuLoad1m = _AxPruCpuLoad1m_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 1002, 4, 1, 1, 12),
    _AxPruCpuLoad1m_Type()
)
axPruCpuLoad1m.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axPruCpuLoad1m.setStatus("current")
_AxPruMemoryTotalSize_Type = Integer32
_AxPruMemoryTotalSize_Object = MibTableColumn
axPruMemoryTotalSize = _AxPruMemoryTotalSize_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 1002, 4, 1, 1, 13),
    _AxPruMemoryTotalSize_Type()
)
axPruMemoryTotalSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axPruMemoryTotalSize.setStatus("current")
_AxPruMemoryUsedSize_Type = Integer32
_AxPruMemoryUsedSize_Object = MibTableColumn
axPruMemoryUsedSize = _AxPruMemoryUsedSize_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 1002, 4, 1, 1, 14),
    _AxPruMemoryUsedSize_Type()
)
axPruMemoryUsedSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axPruMemoryUsedSize.setStatus("current")
_AxPruMemoryFreeSize_Type = Integer32
_AxPruMemoryFreeSize_Object = MibTableColumn
axPruMemoryFreeSize = _AxPruMemoryFreeSize_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 1002, 4, 1, 1, 15),
    _AxPruMemoryFreeSize_Type()
)
axPruMemoryFreeSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axPruMemoryFreeSize.setStatus("current")


class _AxPruTemperatureState_Type(Integer32):
    """Custom type axPruTemperatureState based on Integer32"""
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
        *(("unknown", 1),
          ("normal", 2),
          ("critical", 3),
          ("fault", 4))
    )


_AxPruTemperatureState_Type.__name__ = "Integer32"
_AxPruTemperatureState_Object = MibTableColumn
axPruTemperatureState = _AxPruTemperatureState_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 1002, 4, 1, 1, 16),
    _AxPruTemperatureState_Type()
)
axPruTemperatureState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axPruTemperatureState.setStatus("current")
_AxPruTotalAccumRunTime_Type = Integer32
_AxPruTotalAccumRunTime_Object = MibTableColumn
axPruTotalAccumRunTime = _AxPruTotalAccumRunTime_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 1002, 4, 1, 1, 17),
    _AxPruTotalAccumRunTime_Type()
)
axPruTotalAccumRunTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axPruTotalAccumRunTime.setStatus("current")
_AxPruCautionAccumRunTime_Type = Integer32
_AxPruCautionAccumRunTime_Object = MibTableColumn
axPruCautionAccumRunTime = _AxPruCautionAccumRunTime_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 1002, 4, 1, 1, 18),
    _AxPruCautionAccumRunTime_Type()
)
axPruCautionAccumRunTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axPruCautionAccumRunTime.setStatus("current")
_AxPruCriticalAccumRunTime_Type = Integer32
_AxPruCriticalAccumRunTime_Object = MibTableColumn
axPruCriticalAccumRunTime = _AxPruCriticalAccumRunTime_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 1002, 4, 1, 1, 19),
    _AxPruCriticalAccumRunTime_Type()
)
axPruCriticalAccumRunTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axPruCriticalAccumRunTime.setStatus("current")
_AxPruElapsedTime_Type = Integer32
_AxPruElapsedTime_Object = MibTableColumn
axPruElapsedTime = _AxPruElapsedTime_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 1002, 4, 1, 1, 20),
    _AxPruElapsedTime_Type()
)
axPruElapsedTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axPruElapsedTime.setStatus("current")
_AxPruBoardTraps_ObjectIdentity = ObjectIdentity
axPruBoardTraps = _AxPruBoardTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 1002, 4, 2)
)
_AxPruStateChangeTrapPrefix_ObjectIdentity = ObjectIdentity
axPruStateChangeTrapPrefix = _AxPruStateChangeTrapPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 1002, 4, 2, 0)
)
_AxPsuBoard_ObjectIdentity = ObjectIdentity
axPsuBoard = _AxPsuBoard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 1002, 5)
)
_AxPsuBoardTable_Object = MibTable
axPsuBoardTable = _AxPsuBoardTable_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 1002, 5, 1)
)
if mibBuilder.loadTexts:
    axPsuBoardTable.setStatus("current")
_AxPsuBoardEntry_Object = MibTableRow
axPsuBoardEntry = _AxPsuBoardEntry_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 1002, 5, 1, 1)
)
axPsuBoardEntry.setIndexNames(
    (0, "AX-DEVICE-MIB", "axChassisIndex"),
    (0, "AX-DEVICE-MIB", "axPsuBoardIndex"),
)
if mibBuilder.loadTexts:
    axPsuBoardEntry.setStatus("current")
_AxPsuBoardIndex_Type = Integer32
_AxPsuBoardIndex_Object = MibTableColumn
axPsuBoardIndex = _AxPsuBoardIndex_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 1002, 5, 1, 1, 1),
    _AxPsuBoardIndex_Type()
)
axPsuBoardIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    axPsuBoardIndex.setStatus("current")
_AxPsuBoardType_Type = Integer32
_AxPsuBoardType_Object = MibTableColumn
axPsuBoardType = _AxPsuBoardType_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 1002, 5, 1, 1, 2),
    _AxPsuBoardType_Type()
)
axPsuBoardType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axPsuBoardType.setStatus("current")


class _AxPsuOperLedStatus_Type(Integer32):
    """Custom type axPsuOperLedStatus based on Integer32"""
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
        *(("unknown", 1),
          ("green", 2),
          ("greenblink", 3),
          ("red", 4),
          ("extinction", 5))
    )


_AxPsuOperLedStatus_Type.__name__ = "Integer32"
_AxPsuOperLedStatus_Object = MibTableColumn
axPsuOperLedStatus = _AxPsuOperLedStatus_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 1002, 5, 1, 1, 3),
    _AxPsuOperLedStatus_Type()
)
axPsuOperLedStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axPsuOperLedStatus.setStatus("current")


class _AxPsuOperModeStatus_Type(Integer32):
    """Custom type axPsuOperModeStatus based on Integer32"""
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
              99)
        )
    )
    namedValues = NamedValues(
        *(("notconnect", 1),
          ("notsupport", 2),
          ("active", 3),
          ("initialize", 4),
          ("fault", 5),
          ("inactive", 6),
          ("disable", 7),
          ("powershortage", 8),
          ("unknown", 99))
    )


_AxPsuOperModeStatus_Type.__name__ = "Integer32"
_AxPsuOperModeStatus_Object = MibTableColumn
axPsuOperModeStatus = _AxPsuOperModeStatus_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 1002, 5, 1, 1, 4),
    _AxPsuOperModeStatus_Type()
)
axPsuOperModeStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axPsuOperModeStatus.setStatus("current")


class _AxPsuUpdateStatus_Type(Integer32):
    """Custom type axPsuUpdateStatus based on Integer32"""
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
        *(("none", 1),
          ("executing", 2),
          ("restartrequired", 3),
          ("failed", 4))
    )


_AxPsuUpdateStatus_Type.__name__ = "Integer32"
_AxPsuUpdateStatus_Object = MibTableColumn
axPsuUpdateStatus = _AxPsuUpdateStatus_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 1002, 5, 1, 1, 5),
    _AxPsuUpdateStatus_Type()
)
axPsuUpdateStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axPsuUpdateStatus.setStatus("current")
_AxPsuErrorRestartNum_Type = Integer32
_AxPsuErrorRestartNum_Object = MibTableColumn
axPsuErrorRestartNum = _AxPsuErrorRestartNum_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 1002, 5, 1, 1, 6),
    _AxPsuErrorRestartNum_Type()
)
axPsuErrorRestartNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axPsuErrorRestartNum.setStatus("current")
_AxPsuBoardName_Type = DisplayString
_AxPsuBoardName_Object = MibTableColumn
axPsuBoardName = _AxPsuBoardName_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 1002, 5, 1, 1, 7),
    _AxPsuBoardName_Type()
)
axPsuBoardName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axPsuBoardName.setStatus("current")
_AxPsuBoardAbbreviation_Type = DisplayString
_AxPsuBoardAbbreviation_Object = MibTableColumn
axPsuBoardAbbreviation = _AxPsuBoardAbbreviation_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 1002, 5, 1, 1, 8),
    _AxPsuBoardAbbreviation_Type()
)
axPsuBoardAbbreviation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axPsuBoardAbbreviation.setStatus("current")
_AxPsuSerialInformation_Type = DisplayString
_AxPsuSerialInformation_Object = MibTableColumn
axPsuSerialInformation = _AxPsuSerialInformation_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 1002, 5, 1, 1, 9),
    _AxPsuSerialInformation_Type()
)
axPsuSerialInformation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axPsuSerialInformation.setStatus("current")
_AxPsuCpuUpTime_Type = DisplayString
_AxPsuCpuUpTime_Object = MibTableColumn
axPsuCpuUpTime = _AxPsuCpuUpTime_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 1002, 5, 1, 1, 10),
    _AxPsuCpuUpTime_Type()
)
axPsuCpuUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axPsuCpuUpTime.setStatus("current")
_AxPsuCpuClock_Type = Integer32
_AxPsuCpuClock_Object = MibTableColumn
axPsuCpuClock = _AxPsuCpuClock_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 1002, 5, 1, 1, 11),
    _AxPsuCpuClock_Type()
)
axPsuCpuClock.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axPsuCpuClock.setStatus("current")
_AxPsuCpuLoad1m_Type = Integer32
_AxPsuCpuLoad1m_Object = MibTableColumn
axPsuCpuLoad1m = _AxPsuCpuLoad1m_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 1002, 5, 1, 1, 12),
    _AxPsuCpuLoad1m_Type()
)
axPsuCpuLoad1m.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axPsuCpuLoad1m.setStatus("current")
_AxPsuMemoryTotalSize_Type = Integer32
_AxPsuMemoryTotalSize_Object = MibTableColumn
axPsuMemoryTotalSize = _AxPsuMemoryTotalSize_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 1002, 5, 1, 1, 13),
    _AxPsuMemoryTotalSize_Type()
)
axPsuMemoryTotalSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axPsuMemoryTotalSize.setStatus("current")
_AxPsuMemoryUsedSize_Type = Integer32
_AxPsuMemoryUsedSize_Object = MibTableColumn
axPsuMemoryUsedSize = _AxPsuMemoryUsedSize_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 1002, 5, 1, 1, 14),
    _AxPsuMemoryUsedSize_Type()
)
axPsuMemoryUsedSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axPsuMemoryUsedSize.setStatus("current")
_AxPsuMemoryFreeSize_Type = Integer32
_AxPsuMemoryFreeSize_Object = MibTableColumn
axPsuMemoryFreeSize = _AxPsuMemoryFreeSize_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 1002, 5, 1, 1, 15),
    _AxPsuMemoryFreeSize_Type()
)
axPsuMemoryFreeSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axPsuMemoryFreeSize.setStatus("current")


class _AxPsuTemperatureState_Type(Integer32):
    """Custom type axPsuTemperatureState based on Integer32"""
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
        *(("unknown", 1),
          ("normal", 2),
          ("critical", 3),
          ("fault", 4))
    )


_AxPsuTemperatureState_Type.__name__ = "Integer32"
_AxPsuTemperatureState_Object = MibTableColumn
axPsuTemperatureState = _AxPsuTemperatureState_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 1002, 5, 1, 1, 16),
    _AxPsuTemperatureState_Type()
)
axPsuTemperatureState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axPsuTemperatureState.setStatus("current")
_AxPsuTotalAccumRunTime_Type = Integer32
_AxPsuTotalAccumRunTime_Object = MibTableColumn
axPsuTotalAccumRunTime = _AxPsuTotalAccumRunTime_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 1002, 5, 1, 1, 17),
    _AxPsuTotalAccumRunTime_Type()
)
axPsuTotalAccumRunTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axPsuTotalAccumRunTime.setStatus("current")
_AxPsuCautionAccumRunTime_Type = Integer32
_AxPsuCautionAccumRunTime_Object = MibTableColumn
axPsuCautionAccumRunTime = _AxPsuCautionAccumRunTime_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 1002, 5, 1, 1, 18),
    _AxPsuCautionAccumRunTime_Type()
)
axPsuCautionAccumRunTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axPsuCautionAccumRunTime.setStatus("current")
_AxPsuCriticalAccumRunTime_Type = Integer32
_AxPsuCriticalAccumRunTime_Object = MibTableColumn
axPsuCriticalAccumRunTime = _AxPsuCriticalAccumRunTime_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 1002, 5, 1, 1, 19),
    _AxPsuCriticalAccumRunTime_Type()
)
axPsuCriticalAccumRunTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axPsuCriticalAccumRunTime.setStatus("current")
_AxPsuElapsedTime_Type = Integer32
_AxPsuElapsedTime_Object = MibTableColumn
axPsuElapsedTime = _AxPsuElapsedTime_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 1002, 5, 1, 1, 20),
    _AxPsuElapsedTime_Type()
)
axPsuElapsedTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axPsuElapsedTime.setStatus("current")
_AxPsuBoardTraps_ObjectIdentity = ObjectIdentity
axPsuBoardTraps = _AxPsuBoardTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 1002, 5, 2)
)
_AxPsuStateChangeTrapPrefix_ObjectIdentity = ObjectIdentity
axPsuStateChangeTrapPrefix = _AxPsuStateChangeTrapPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 1002, 5, 2, 0)
)
_AxNifBoard_ObjectIdentity = ObjectIdentity
axNifBoard = _AxNifBoard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 1002, 6)
)
_AxNifBoardTable_Object = MibTable
axNifBoardTable = _AxNifBoardTable_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 1002, 6, 1)
)
if mibBuilder.loadTexts:
    axNifBoardTable.setStatus("current")
_AxNifBoardEntry_Object = MibTableRow
axNifBoardEntry = _AxNifBoardEntry_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 1002, 6, 1, 1)
)
axNifBoardEntry.setIndexNames(
    (0, "AX-DEVICE-MIB", "axChassisIndex"),
    (0, "AX-DEVICE-MIB", "axNifBoardIndex"),
)
if mibBuilder.loadTexts:
    axNifBoardEntry.setStatus("current")
_AxNifBoardIndex_Type = Integer32
_AxNifBoardIndex_Object = MibTableColumn
axNifBoardIndex = _AxNifBoardIndex_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 1002, 6, 1, 1, 1),
    _AxNifBoardIndex_Type()
)
axNifBoardIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    axNifBoardIndex.setStatus("current")
_AxNifBoardType_Type = Integer32
_AxNifBoardType_Object = MibTableColumn
axNifBoardType = _AxNifBoardType_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 1002, 6, 1, 1, 2),
    _AxNifBoardType_Type()
)
axNifBoardType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axNifBoardType.setStatus("current")


class _AxNifOperLedStatus_Type(Integer32):
    """Custom type axNifOperLedStatus based on Integer32"""
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
        *(("unknown", 1),
          ("green", 2),
          ("greenblink", 3),
          ("red", 4),
          ("extinction", 5))
    )


_AxNifOperLedStatus_Type.__name__ = "Integer32"
_AxNifOperLedStatus_Object = MibTableColumn
axNifOperLedStatus = _AxNifOperLedStatus_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 1002, 6, 1, 1, 3),
    _AxNifOperLedStatus_Type()
)
axNifOperLedStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axNifOperLedStatus.setStatus("current")


class _AxNifOperModeStatus_Type(Integer32):
    """Custom type axNifOperModeStatus based on Integer32"""
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
              99)
        )
    )
    namedValues = NamedValues(
        *(("notconnect", 1),
          ("notsupport", 2),
          ("active", 3),
          ("initialize", 4),
          ("fault", 5),
          ("inactive", 6),
          ("disable", 7),
          ("powershortage", 8),
          ("unknown", 99))
    )


_AxNifOperModeStatus_Type.__name__ = "Integer32"
_AxNifOperModeStatus_Object = MibTableColumn
axNifOperModeStatus = _AxNifOperModeStatus_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 1002, 6, 1, 1, 4),
    _AxNifOperModeStatus_Type()
)
axNifOperModeStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axNifOperModeStatus.setStatus("current")


class _AxNifUpdateStatus_Type(Integer32):
    """Custom type axNifUpdateStatus based on Integer32"""
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
        *(("none", 1),
          ("executing", 2),
          ("restartrequired", 3),
          ("failed", 4))
    )


_AxNifUpdateStatus_Type.__name__ = "Integer32"
_AxNifUpdateStatus_Object = MibTableColumn
axNifUpdateStatus = _AxNifUpdateStatus_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 1002, 6, 1, 1, 5),
    _AxNifUpdateStatus_Type()
)
axNifUpdateStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axNifUpdateStatus.setStatus("current")
_AxNifErrorRestartNum_Type = Integer32
_AxNifErrorRestartNum_Object = MibTableColumn
axNifErrorRestartNum = _AxNifErrorRestartNum_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 1002, 6, 1, 1, 6),
    _AxNifErrorRestartNum_Type()
)
axNifErrorRestartNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axNifErrorRestartNum.setStatus("current")
_AxNifBoardName_Type = DisplayString
_AxNifBoardName_Object = MibTableColumn
axNifBoardName = _AxNifBoardName_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 1002, 6, 1, 1, 7),
    _AxNifBoardName_Type()
)
axNifBoardName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axNifBoardName.setStatus("current")
_AxNifBoardAbbreviation_Type = DisplayString
_AxNifBoardAbbreviation_Object = MibTableColumn
axNifBoardAbbreviation = _AxNifBoardAbbreviation_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 1002, 6, 1, 1, 8),
    _AxNifBoardAbbreviation_Type()
)
axNifBoardAbbreviation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axNifBoardAbbreviation.setStatus("current")
_AxNifPhysLineNumber_Type = Integer32
_AxNifPhysLineNumber_Object = MibTableColumn
axNifPhysLineNumber = _AxNifPhysLineNumber_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 1002, 6, 1, 1, 9),
    _AxNifPhysLineNumber_Type()
)
axNifPhysLineNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axNifPhysLineNumber.setStatus("current")
_AxNifSerialInformation_Type = DisplayString
_AxNifSerialInformation_Object = MibTableColumn
axNifSerialInformation = _AxNifSerialInformation_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 1002, 6, 1, 1, 10),
    _AxNifSerialInformation_Type()
)
axNifSerialInformation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axNifSerialInformation.setStatus("current")


class _AxNifTemperatureState_Type(Integer32):
    """Custom type axNifTemperatureState based on Integer32"""
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
        *(("unknown", 1),
          ("normal", 2),
          ("critical", 3),
          ("fault", 4))
    )


_AxNifTemperatureState_Type.__name__ = "Integer32"
_AxNifTemperatureState_Object = MibTableColumn
axNifTemperatureState = _AxNifTemperatureState_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 1002, 6, 1, 1, 11),
    _AxNifTemperatureState_Type()
)
axNifTemperatureState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axNifTemperatureState.setStatus("current")
_AxNifTotalAccumRunTime_Type = Integer32
_AxNifTotalAccumRunTime_Object = MibTableColumn
axNifTotalAccumRunTime = _AxNifTotalAccumRunTime_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 1002, 6, 1, 1, 12),
    _AxNifTotalAccumRunTime_Type()
)
axNifTotalAccumRunTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axNifTotalAccumRunTime.setStatus("current")
_AxNifCautionAccumRunTime_Type = Integer32
_AxNifCautionAccumRunTime_Object = MibTableColumn
axNifCautionAccumRunTime = _AxNifCautionAccumRunTime_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 1002, 6, 1, 1, 13),
    _AxNifCautionAccumRunTime_Type()
)
axNifCautionAccumRunTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axNifCautionAccumRunTime.setStatus("current")
_AxNifCriticalAccumRunTime_Type = Integer32
_AxNifCriticalAccumRunTime_Object = MibTableColumn
axNifCriticalAccumRunTime = _AxNifCriticalAccumRunTime_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 1002, 6, 1, 1, 14),
    _AxNifCriticalAccumRunTime_Type()
)
axNifCriticalAccumRunTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axNifCriticalAccumRunTime.setStatus("current")
_AxNifElapsedTime_Type = Integer32
_AxNifElapsedTime_Object = MibTableColumn
axNifElapsedTime = _AxNifElapsedTime_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 1002, 6, 1, 1, 15),
    _AxNifElapsedTime_Type()
)
axNifElapsedTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axNifElapsedTime.setStatus("current")


class _AxNifReadyLedStatus_Type(Integer32):
    """Custom type axNifReadyLedStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              5)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 1),
          ("green", 2),
          ("greenblink", 3),
          ("extinction", 5))
    )


_AxNifReadyLedStatus_Type.__name__ = "Integer32"
_AxNifReadyLedStatus_Object = MibTableColumn
axNifReadyLedStatus = _AxNifReadyLedStatus_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 1002, 6, 1, 1, 16),
    _AxNifReadyLedStatus_Type()
)
axNifReadyLedStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axNifReadyLedStatus.setStatus("current")
_AxNifBoardTraps_ObjectIdentity = ObjectIdentity
axNifBoardTraps = _AxNifBoardTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 1002, 6, 2)
)
_AxNifStateChangeTrapPrefix_ObjectIdentity = ObjectIdentity
axNifStateChangeTrapPrefix = _AxNifStateChangeTrapPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 1002, 6, 2, 0)
)
_AxSmcTable_Object = MibTable
axSmcTable = _AxSmcTable_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 1002, 6, 3)
)
if mibBuilder.loadTexts:
    axSmcTable.setStatus("current")
_AxSmcEntry_Object = MibTableRow
axSmcEntry = _AxSmcEntry_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 1002, 6, 3, 1)
)
axSmcEntry.setIndexNames(
    (0, "AX-DEVICE-MIB", "axChassisIndex"),
    (0, "AX-DEVICE-MIB", "axNifBoardIndex"),
)
if mibBuilder.loadTexts:
    axSmcEntry.setStatus("current")
_AxSmcCpuClock_Type = Integer32
_AxSmcCpuClock_Object = MibTableColumn
axSmcCpuClock = _AxSmcCpuClock_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 1002, 6, 3, 1, 1),
    _AxSmcCpuClock_Type()
)
axSmcCpuClock.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axSmcCpuClock.setStatus("current")
_AxSmcCpuLoad1m_Type = Integer32
_AxSmcCpuLoad1m_Object = MibTableColumn
axSmcCpuLoad1m = _AxSmcCpuLoad1m_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 1002, 6, 3, 1, 2),
    _AxSmcCpuLoad1m_Type()
)
axSmcCpuLoad1m.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axSmcCpuLoad1m.setStatus("current")
_AxSmcMemoryTotalSize_Type = Integer32
_AxSmcMemoryTotalSize_Object = MibTableColumn
axSmcMemoryTotalSize = _AxSmcMemoryTotalSize_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 1002, 6, 3, 1, 3),
    _AxSmcMemoryTotalSize_Type()
)
axSmcMemoryTotalSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axSmcMemoryTotalSize.setStatus("current")
_AxSmcMemoryUsedSize_Type = Integer32
_AxSmcMemoryUsedSize_Object = MibTableColumn
axSmcMemoryUsedSize = _AxSmcMemoryUsedSize_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 1002, 6, 3, 1, 4),
    _AxSmcMemoryUsedSize_Type()
)
axSmcMemoryUsedSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axSmcMemoryUsedSize.setStatus("current")
_AxSmcMemoryFreeSize_Type = Integer32
_AxSmcMemoryFreeSize_Object = MibTableColumn
axSmcMemoryFreeSize = _AxSmcMemoryFreeSize_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 1002, 6, 3, 1, 5),
    _AxSmcMemoryFreeSize_Type()
)
axSmcMemoryFreeSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axSmcMemoryFreeSize.setStatus("current")
_AxSmcBoardTraps_ObjectIdentity = ObjectIdentity
axSmcBoardTraps = _AxSmcBoardTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 1002, 6, 4)
)
_AxSmcBoardTrapsPrefix_ObjectIdentity = ObjectIdentity
axSmcBoardTrapsPrefix = _AxSmcBoardTrapsPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 1002, 6, 4, 0)
)
_AxPhysLine_ObjectIdentity = ObjectIdentity
axPhysLine = _AxPhysLine_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 1002, 7)
)
_AxPhysLineTable_Object = MibTable
axPhysLineTable = _AxPhysLineTable_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 1002, 7, 1)
)
if mibBuilder.loadTexts:
    axPhysLineTable.setStatus("current")
_AxPhysLineEntry_Object = MibTableRow
axPhysLineEntry = _AxPhysLineEntry_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 1002, 7, 1, 1)
)
axPhysLineEntry.setIndexNames(
    (0, "AX-DEVICE-MIB", "axChassisIndex"),
    (0, "AX-DEVICE-MIB", "axNifBoardIndex"),
    (0, "AX-DEVICE-MIB", "axPhysLineIndex"),
)
if mibBuilder.loadTexts:
    axPhysLineEntry.setStatus("current")
_AxPhysLineIndex_Type = Integer32
_AxPhysLineIndex_Object = MibTableColumn
axPhysLineIndex = _AxPhysLineIndex_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 1002, 7, 1, 1, 1),
    _AxPhysLineIndex_Type()
)
axPhysLineIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    axPhysLineIndex.setStatus("current")


class _AxPhysLineConnectorType_Type(Integer32):
    """Custom type axPhysLineConnectorType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              301,
              302,
              303,
              304,
              305,
              306,
              307,
              308,
              309,
              401,
              402,
              403,
              404,
              501,
              502,
              601,
              602,
              603,
              604)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("type1000BASE-LX", 301),
          ("type1000BASE-SX", 302),
          ("type1000BASE-LH", 303),
          ("type1000BASE-BX10-D", 304),
          ("type1000BASE-BX10-U", 305),
          ("type1000BASE-BX40-D", 306),
          ("type1000BASE-BX40-U", 307),
          ("type1000BASE-SX2", 308),
          ("type1000BASE-UTP", 309),
          ("type10GBASE-SR", 401),
          ("type10GBASE-LR", 402),
          ("type10GBASE-ER", 403),
          ("type10GBASE-ZR", 404),
          ("type40GBASE-SR4", 501),
          ("type40GBASE-LR4", 502),
          ("type100GBASE-LR4", 601),
          ("type100GBASE-SR4", 602),
          ("type100GBASE-CWDM4", 603),
          ("type100GBASE-4WDM-40", 604))
    )


_AxPhysLineConnectorType_Type.__name__ = "Integer32"
_AxPhysLineConnectorType_Object = MibTableColumn
axPhysLineConnectorType = _AxPhysLineConnectorType_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 1002, 7, 1, 1, 2),
    _AxPhysLineConnectorType_Type()
)
axPhysLineConnectorType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axPhysLineConnectorType.setStatus("current")


class _AxPhysLineOperStatus_Type(Integer32):
    """Custom type axPhysLineOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("active", 2),
          ("initialization", 3),
          ("down", 4),
          ("lock", 6),
          ("close", 7),
          ("line-fault", 8),
          ("test", 9),
          ("standby", 10),
          ("suspend", 11),
          ("unused", 12),
          ("mismatch", 13))
    )


_AxPhysLineOperStatus_Type.__name__ = "Integer32"
_AxPhysLineOperStatus_Object = MibTableColumn
axPhysLineOperStatus = _AxPhysLineOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 1002, 7, 1, 1, 3),
    _AxPhysLineOperStatus_Type()
)
axPhysLineOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axPhysLineOperStatus.setStatus("current")
_AxPhysLineIfIndexNumber_Type = Integer32
_AxPhysLineIfIndexNumber_Object = MibTableColumn
axPhysLineIfIndexNumber = _AxPhysLineIfIndexNumber_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 1002, 7, 1, 1, 4),
    _AxPhysLineIfIndexNumber_Type()
)
axPhysLineIfIndexNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axPhysLineIfIndexNumber.setStatus("current")


class _AxPhysLineTransceiverStatus_Type(Integer32):
    """Custom type axPhysLineTransceiverStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              20,
              21,
              22,
              24,
              40,
              41,
              42,
              44,
              50,
              51,
              52,
              54,
              60,
              61,
              62,
              64,
              70,
              71,
              72,
              74)
        )
    )
    namedValues = NamedValues(
        *(("unchangeable-transceiver", 1),
          ("sfp-mounted", 20),
          ("sfp-unmounted", 21),
          ("unsupported-sfp-mounted", 22),
          ("sfp-fault", 24),
          ("sfpp-mounted", 40),
          ("sfpp-unmounted", 41),
          ("unsupported-sfpp-mounted", 42),
          ("sfpp-fault", 44),
          ("qsfpp-mounted", 50),
          ("qsfpp-unmounted", 51),
          ("unsupported-qsfpp-mounted", 52),
          ("qsfpp-fault", 54),
          ("cfp-mounted", 60),
          ("cfp-unmounted", 61),
          ("unsupported-cfp-mounted", 62),
          ("cfp-fault", 64),
          ("qsfp28-mounted", 70),
          ("qsfp28-unmounted", 71),
          ("unsupported-qsfp28-mounted", 72),
          ("qsfp28-fault", 74))
    )


_AxPhysLineTransceiverStatus_Type.__name__ = "Integer32"
_AxPhysLineTransceiverStatus_Object = MibTableColumn
axPhysLineTransceiverStatus = _AxPhysLineTransceiverStatus_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 1002, 7, 1, 1, 5),
    _AxPhysLineTransceiverStatus_Type()
)
axPhysLineTransceiverStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axPhysLineTransceiverStatus.setStatus("current")
_AxPhysLineLaneTable_Object = MibTable
axPhysLineLaneTable = _AxPhysLineLaneTable_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 1002, 7, 2)
)
if mibBuilder.loadTexts:
    axPhysLineLaneTable.setStatus("current")
_AxPhysLineLaneEntry_Object = MibTableRow
axPhysLineLaneEntry = _AxPhysLineLaneEntry_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 1002, 7, 2, 1)
)
axPhysLineLaneEntry.setIndexNames(
    (0, "AX-DEVICE-MIB", "axChassisIndex"),
    (0, "AX-DEVICE-MIB", "axNifBoardIndex"),
    (0, "AX-DEVICE-MIB", "axPhysLineIndex"),
    (0, "AX-DEVICE-MIB", "axPhysLineLaneIndex"),
)
if mibBuilder.loadTexts:
    axPhysLineLaneEntry.setStatus("current")
_AxPhysLineLaneIndex_Type = Integer32
_AxPhysLineLaneIndex_Object = MibTableColumn
axPhysLineLaneIndex = _AxPhysLineLaneIndex_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 1002, 7, 2, 1, 1),
    _AxPhysLineLaneIndex_Type()
)
axPhysLineLaneIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    axPhysLineLaneIndex.setStatus("current")
_AxPhysLineLaneTransceiverTxPower_Type = Integer32
_AxPhysLineLaneTransceiverTxPower_Object = MibTableColumn
axPhysLineLaneTransceiverTxPower = _AxPhysLineLaneTransceiverTxPower_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 1002, 7, 2, 1, 2),
    _AxPhysLineLaneTransceiverTxPower_Type()
)
axPhysLineLaneTransceiverTxPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axPhysLineLaneTransceiverTxPower.setStatus("current")
_AxPhysLineLaneTransceiverRxPower_Type = Integer32
_AxPhysLineLaneTransceiverRxPower_Object = MibTableColumn
axPhysLineLaneTransceiverRxPower = _AxPhysLineLaneTransceiverRxPower_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 1002, 7, 2, 1, 3),
    _AxPhysLineLaneTransceiverRxPower_Type()
)
axPhysLineLaneTransceiverRxPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axPhysLineLaneTransceiverRxPower.setStatus("current")
_AxInterface_ObjectIdentity = ObjectIdentity
axInterface = _AxInterface_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 1002, 8)
)
_AxLineIfTable_Object = MibTable
axLineIfTable = _AxLineIfTable_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 1002, 8, 1)
)
if mibBuilder.loadTexts:
    axLineIfTable.setStatus("current")
_AxLineIfEntry_Object = MibTableRow
axLineIfEntry = _AxLineIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 1002, 8, 1, 1)
)
axLineIfEntry.setIndexNames(
    (0, "AX-DEVICE-MIB", "axChassisIndex"),
    (0, "AX-DEVICE-MIB", "axNifBoardIndex"),
    (0, "AX-DEVICE-MIB", "axPhysLineIndex"),
    (0, "AX-DEVICE-MIB", "axLineIfIndex"),
)
if mibBuilder.loadTexts:
    axLineIfEntry.setStatus("current")
_AxLineIfIndex_Type = Integer32
_AxLineIfIndex_Object = MibTableColumn
axLineIfIndex = _AxLineIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 1002, 8, 1, 1, 1),
    _AxLineIfIndex_Type()
)
axLineIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    axLineIfIndex.setStatus("current")
_AxIfIndex_Type = Integer32
_AxIfIndex_Object = MibTableColumn
axIfIndex = _AxIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 1002, 8, 1, 1, 2),
    _AxIfIndex_Type()
)
axIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axIfIndex.setStatus("current")
_AxIfIpAddress_Type = IpAddress
_AxIfIpAddress_Object = MibTableColumn
axIfIpAddress = _AxIfIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 1002, 8, 1, 1, 3),
    _AxIfIpAddress_Type()
)
axIfIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axIfIpAddress.setStatus("current")
_AxIfIpv6Address_Type = OctetString
_AxIfIpv6Address_Object = MibTableColumn
axIfIpv6Address = _AxIfIpv6Address_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 1002, 8, 1, 1, 4),
    _AxIfIpv6Address_Type()
)
axIfIpv6Address.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axIfIpv6Address.setStatus("current")
_AxDeviceConformance_ObjectIdentity = ObjectIdentity
axDeviceConformance = _AxDeviceConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 1002, 1000)
)
_AxDeviceCompliances_ObjectIdentity = ObjectIdentity
axDeviceCompliances = _AxDeviceCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 1002, 1000, 1)
)
_AxDeviceGroups_ObjectIdentity = ObjectIdentity
axDeviceGroups = _AxDeviceGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 1002, 1000, 2)
)

# Managed Objects groups

axDeviceGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 1002, 1000, 2, 1)
)
axDeviceGroup.setObjects(
      *(("AX-DEVICE-MIB", "axChassisMaxNumber"),
        ("AX-DEVICE-MIB", "axChassisName"),
        ("AX-DEVICE-MIB", "axChassisAbbreviation"),
        ("AX-DEVICE-MIB", "axChassisType"),
        ("AX-DEVICE-MIB", "axPowerUnitNumber"),
        ("AX-DEVICE-MIB", "axFanNumber"),
        ("AX-DEVICE-MIB", "axBcuBoardNumber"),
        ("AX-DEVICE-MIB", "axSfuBoardNumber"),
        ("AX-DEVICE-MIB", "axPruBoardNumber"),
        ("AX-DEVICE-MIB", "axPsuBoardNumber"),
        ("AX-DEVICE-MIB", "axNifBoardNumber"),
        ("AX-DEVICE-MIB", "axChassisSerialInformation"),
        ("AX-DEVICE-MIB", "axChassisStatus"),
        ("AX-DEVICE-MIB", "axPowerSupplyUnitRedundancyMode"),
        ("AX-DEVICE-MIB", "axFanMode"),
        ("AX-DEVICE-MIB", "axBcuBoardRedundancyStatus"),
        ("AX-DEVICE-MIB", "axTotalPowerSupplyCapacity"),
        ("AX-DEVICE-MIB", "axPowerSupplyCapacitySourceA"),
        ("AX-DEVICE-MIB", "axPowerSupplyCapacitySourceB"),
        ("AX-DEVICE-MIB", "axTotalPowerAllocated"),
        ("AX-DEVICE-MIB", "axTotalPowerAvailable"),
        ("AX-DEVICE-MIB", "axRedundantPowerAvailable"),
        ("AX-DEVICE-MIB", "axPowerAvailableSourceA"),
        ("AX-DEVICE-MIB", "axPowerAvailableSourceB"),
        ("AX-DEVICE-MIB", "axPowerSupplyName"),
        ("AX-DEVICE-MIB", "axPowerSupplyAbbreviation"),
        ("AX-DEVICE-MIB", "axPowerSupplySerialInformation"),
        ("AX-DEVICE-MIB", "axPowerSupplyInputVoltage"),
        ("AX-DEVICE-MIB", "axPowerSupplyConnectStatus"),
        ("AX-DEVICE-MIB", "axPowerSupplyStatus"),
        ("AX-DEVICE-MIB", "axPowerSupplyTotalAccumRunTime"),
        ("AX-DEVICE-MIB", "axPowerSupplyCautionAccumRunTime"),
        ("AX-DEVICE-MIB", "axPowerSupplyCriticalAccumRunTime"),
        ("AX-DEVICE-MIB", "axPowerSupplyElapsedTime"),
        ("AX-DEVICE-MIB", "axFanUnitName"),
        ("AX-DEVICE-MIB", "axFanUnitAbbreviation"),
        ("AX-DEVICE-MIB", "axFanUnitSerialInformation"),
        ("AX-DEVICE-MIB", "axFanUnitStatus"),
        ("AX-DEVICE-MIB", "axFanUnitSpeed"),
        ("AX-DEVICE-MIB", "axFanUnitTotalAccumRunTime"),
        ("AX-DEVICE-MIB", "axFanUnitCautionAccumRunTime"),
        ("AX-DEVICE-MIB", "axFanUnitCriticalAccumRunTime"),
        ("AX-DEVICE-MIB", "axFanUnitElapsedTime"),
        ("AX-DEVICE-MIB", "axFanUnitLedStatus"),
        ("AX-DEVICE-MIB", "axBcuOperLedStatus"),
        ("AX-DEVICE-MIB", "axBcuOperModeStatus"),
        ("AX-DEVICE-MIB", "axBcuActiveLedStatus"),
        ("AX-DEVICE-MIB", "axBcuSystem1LedStatus"),
        ("AX-DEVICE-MIB", "axBcuSystem2LedStatus"),
        ("AX-DEVICE-MIB", "axBcuBoardName"),
        ("AX-DEVICE-MIB", "axBcuBoardAbbreviation"),
        ("AX-DEVICE-MIB", "axBcuSoftwareVersion"),
        ("AX-DEVICE-MIB", "axBcuFlashTotalSize"),
        ("AX-DEVICE-MIB", "axBcuFlashUsedSize"),
        ("AX-DEVICE-MIB", "axBcuFlashFreeSize"),
        ("AX-DEVICE-MIB", "axBcuTemperatureStatusNumber"),
        ("AX-DEVICE-MIB", "axBcuSerialInformation"),
        ("AX-DEVICE-MIB", "axBcuTotalAccumRunTime"),
        ("AX-DEVICE-MIB", "axBcuCautionAccumRunTime"),
        ("AX-DEVICE-MIB", "axBcuCriticalAccumRunTime"),
        ("AX-DEVICE-MIB", "axBcuElapsedTime"),
        ("AX-DEVICE-MIB", "axBcuTemperatureStatusDescr"),
        ("AX-DEVICE-MIB", "axBcuTemperatureStatusValue"),
        ("AX-DEVICE-MIB", "axBcuTemperatureThreshold"),
        ("AX-DEVICE-MIB", "axBcuTemperatureState"),
        ("AX-DEVICE-MIB", "axBcuTemperatureWarning"),
        ("AX-DEVICE-MIB", "axBcuTemperatureWarningAverage"),
        ("AX-DEVICE-MIB", "axBcuTemperatureWarningAveragePeriod"),
        ("AX-DEVICE-MIB", "axMemoryCardConnection"),
        ("AX-DEVICE-MIB", "axMemoryCardID"),
        ("AX-DEVICE-MIB", "axMemoryCardTotalSize"),
        ("AX-DEVICE-MIB", "axMemoryCardUsedSize"),
        ("AX-DEVICE-MIB", "axMemoryCardFreeSize"),
        ("AX-DEVICE-MIB", "axBcuCpuStatus"),
        ("AX-DEVICE-MIB", "axBcuCpuUpTime"),
        ("AX-DEVICE-MIB", "axBcuCpuClock"),
        ("AX-DEVICE-MIB", "axBcuCpuLoad1m"),
        ("AX-DEVICE-MIB", "axBcuMemoryTotalSize"),
        ("AX-DEVICE-MIB", "axBcuMemoryUsedSize"),
        ("AX-DEVICE-MIB", "axBcuMemoryFreeSize"),
        ("AX-DEVICE-MIB", "axBcuFatalErrorRestartNum"),
        ("AX-DEVICE-MIB", "axIfIndex"),
        ("AX-DEVICE-MIB", "axIfIpAddress"),
        ("AX-DEVICE-MIB", "axIfIpv6Address"),
        ("AX-DEVICE-MIB", "axSfuBoardType"),
        ("AX-DEVICE-MIB", "axSfuOperLedStatus"),
        ("AX-DEVICE-MIB", "axSfuActiveLedStatus"),
        ("AX-DEVICE-MIB", "axSfuOperModeStatus"),
        ("AX-DEVICE-MIB", "axSfuUpdateStatus"),
        ("AX-DEVICE-MIB", "axSfuErrorRestartNum"),
        ("AX-DEVICE-MIB", "axSfuBoardName"),
        ("AX-DEVICE-MIB", "axSfuBoardAbbreviation"),
        ("AX-DEVICE-MIB", "axSfuSerialInformation"),
        ("AX-DEVICE-MIB", "axSfuTemperatureState"),
        ("AX-DEVICE-MIB", "axSfuTotalAccumRunTime"),
        ("AX-DEVICE-MIB", "axSfuCautionAccumRunTime"),
        ("AX-DEVICE-MIB", "axSfuCriticalAccumRunTime"),
        ("AX-DEVICE-MIB", "axSfuElapsedTime"),
        ("AX-DEVICE-MIB", "axPruBoardType"),
        ("AX-DEVICE-MIB", "axPruOperLedStatus"),
        ("AX-DEVICE-MIB", "axPruOperModeStatus"),
        ("AX-DEVICE-MIB", "axPruUpdateStatus"),
        ("AX-DEVICE-MIB", "axPruErrorRestartNum"),
        ("AX-DEVICE-MIB", "axPruBoardName"),
        ("AX-DEVICE-MIB", "axPruBoardAbbreviation"),
        ("AX-DEVICE-MIB", "axPruSerialInformation"),
        ("AX-DEVICE-MIB", "axPruCpuUpTime"),
        ("AX-DEVICE-MIB", "axPruCpuClock"),
        ("AX-DEVICE-MIB", "axPruCpuLoad1m"),
        ("AX-DEVICE-MIB", "axPruMemoryTotalSize"),
        ("AX-DEVICE-MIB", "axPruMemoryUsedSize"),
        ("AX-DEVICE-MIB", "axPruMemoryFreeSize"),
        ("AX-DEVICE-MIB", "axPruTemperatureState"),
        ("AX-DEVICE-MIB", "axPruTotalAccumRunTime"),
        ("AX-DEVICE-MIB", "axPruCautionAccumRunTime"),
        ("AX-DEVICE-MIB", "axPruCriticalAccumRunTime"),
        ("AX-DEVICE-MIB", "axPruElapsedTime"),
        ("AX-DEVICE-MIB", "axPsuBoardType"),
        ("AX-DEVICE-MIB", "axPsuOperLedStatus"),
        ("AX-DEVICE-MIB", "axPsuOperModeStatus"),
        ("AX-DEVICE-MIB", "axPsuUpdateStatus"),
        ("AX-DEVICE-MIB", "axPsuErrorRestartNum"),
        ("AX-DEVICE-MIB", "axPsuBoardName"),
        ("AX-DEVICE-MIB", "axPsuBoardAbbreviation"),
        ("AX-DEVICE-MIB", "axPsuSerialInformation"),
        ("AX-DEVICE-MIB", "axPsuCpuUpTime"),
        ("AX-DEVICE-MIB", "axPsuCpuClock"),
        ("AX-DEVICE-MIB", "axPsuCpuLoad1m"),
        ("AX-DEVICE-MIB", "axPsuMemoryTotalSize"),
        ("AX-DEVICE-MIB", "axPsuMemoryUsedSize"),
        ("AX-DEVICE-MIB", "axPsuMemoryFreeSize"),
        ("AX-DEVICE-MIB", "axPsuTemperatureState"),
        ("AX-DEVICE-MIB", "axPsuTotalAccumRunTime"),
        ("AX-DEVICE-MIB", "axPsuCautionAccumRunTime"),
        ("AX-DEVICE-MIB", "axPsuCriticalAccumRunTime"),
        ("AX-DEVICE-MIB", "axPsuElapsedTime"),
        ("AX-DEVICE-MIB", "axNifBoardType"),
        ("AX-DEVICE-MIB", "axNifOperLedStatus"),
        ("AX-DEVICE-MIB", "axNifOperModeStatus"),
        ("AX-DEVICE-MIB", "axNifUpdateStatus"),
        ("AX-DEVICE-MIB", "axNifErrorRestartNum"),
        ("AX-DEVICE-MIB", "axNifBoardName"),
        ("AX-DEVICE-MIB", "axNifBoardAbbreviation"),
        ("AX-DEVICE-MIB", "axNifPhysLineNumber"),
        ("AX-DEVICE-MIB", "axNifSerialInformation"),
        ("AX-DEVICE-MIB", "axNifTemperatureState"),
        ("AX-DEVICE-MIB", "axNifTotalAccumRunTime"),
        ("AX-DEVICE-MIB", "axNifCautionAccumRunTime"),
        ("AX-DEVICE-MIB", "axNifCriticalAccumRunTime"),
        ("AX-DEVICE-MIB", "axNifElapsedTime"),
        ("AX-DEVICE-MIB", "axNifReadyLedStatus"),
        ("AX-DEVICE-MIB", "axSmcCpuClock"),
        ("AX-DEVICE-MIB", "axSmcCpuLoad1m"),
        ("AX-DEVICE-MIB", "axSmcMemoryTotalSize"),
        ("AX-DEVICE-MIB", "axSmcMemoryUsedSize"),
        ("AX-DEVICE-MIB", "axSmcMemoryFreeSize"),
        ("AX-DEVICE-MIB", "axPhysLineConnectorType"),
        ("AX-DEVICE-MIB", "axPhysLineOperStatus"),
        ("AX-DEVICE-MIB", "axPhysLineIfIndexNumber"),
        ("AX-DEVICE-MIB", "axPhysLineTransceiverStatus"),
        ("AX-DEVICE-MIB", "axPhysLineLaneTransceiverTxPower"),
        ("AX-DEVICE-MIB", "axPhysLineLaneTransceiverRxPower"))
)
if mibBuilder.loadTexts:
    axDeviceGroup.setStatus("current")


# Notification objects

axPowerRedundancyFailureTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 1002, 1, 3, 2, 0, 1)
)
axPowerRedundancyFailureTrap.setObjects(
    ("AX-DEVICE-MIB", "axChassisIndex")
)
if mibBuilder.loadTexts:
    axPowerRedundancyFailureTrap.setStatus(
        "current"
    )

axPowerRedundancyRecoveryTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 1002, 1, 3, 2, 0, 2)
)
axPowerRedundancyRecoveryTrap.setObjects(
    ("AX-DEVICE-MIB", "axChassisIndex")
)
if mibBuilder.loadTexts:
    axPowerRedundancyRecoveryTrap.setStatus(
        "current"
    )

axPowerSupplyInsufficientTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 1002, 1, 3, 2, 0, 3)
)
axPowerSupplyInsufficientTrap.setObjects(
    ("AX-DEVICE-MIB", "axChassisIndex")
)
if mibBuilder.loadTexts:
    axPowerSupplyInsufficientTrap.setStatus(
        "current"
    )

axPowerSupplyInsufficientRecoveryTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 1002, 1, 3, 2, 0, 4)
)
axPowerSupplyInsufficientRecoveryTrap.setObjects(
    ("AX-DEVICE-MIB", "axChassisIndex")
)
if mibBuilder.loadTexts:
    axPowerSupplyInsufficientRecoveryTrap.setStatus(
        "current"
    )

axPowerSupplyFailureTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 1002, 1, 4, 2, 0, 1)
)
axPowerSupplyFailureTrap.setObjects(
      *(("AX-DEVICE-MIB", "axChassisIndex"),
        ("AX-DEVICE-MIB", "axPowerSupplyUnitIndex"))
)
if mibBuilder.loadTexts:
    axPowerSupplyFailureTrap.setStatus(
        "current"
    )

axPowerSupplyRecoveryTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 1002, 1, 4, 2, 0, 2)
)
axPowerSupplyRecoveryTrap.setObjects(
      *(("AX-DEVICE-MIB", "axChassisIndex"),
        ("AX-DEVICE-MIB", "axPowerSupplyUnitIndex"))
)
if mibBuilder.loadTexts:
    axPowerSupplyRecoveryTrap.setStatus(
        "current"
    )

axPowerSupplyStatusChangeTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 1002, 1, 4, 2, 0, 3)
)
axPowerSupplyStatusChangeTrap.setObjects(
      *(("AX-DEVICE-MIB", "axChassisIndex"),
        ("AX-DEVICE-MIB", "axPowerSupplyUnitIndex"))
)
if mibBuilder.loadTexts:
    axPowerSupplyStatusChangeTrap.setStatus(
        "current"
    )

axAirFanUnitStopTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 1002, 1, 5, 2, 0, 1)
)
axAirFanUnitStopTrap.setObjects(
      *(("AX-DEVICE-MIB", "axChassisIndex"),
        ("AX-DEVICE-MIB", "axFanUnitIndex"))
)
if mibBuilder.loadTexts:
    axAirFanUnitStopTrap.setStatus(
        "current"
    )

axAirFanUnitRecoveryTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 1002, 1, 5, 2, 0, 2)
)
axAirFanUnitRecoveryTrap.setObjects(
      *(("AX-DEVICE-MIB", "axChassisIndex"),
        ("AX-DEVICE-MIB", "axFanUnitIndex"))
)
if mibBuilder.loadTexts:
    axAirFanUnitRecoveryTrap.setStatus(
        "current"
    )

axStandbyUpSimplexToDuplexTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 1002, 2, 1, 2, 0, 1)
)
axStandbyUpSimplexToDuplexTrap.setObjects(
      *(("AX-DEVICE-MIB", "axChassisIndex"),
        ("AX-DEVICE-MIB", "axBcuBoardIndex"))
)
if mibBuilder.loadTexts:
    axStandbyUpSimplexToDuplexTrap.setStatus(
        "current"
    )

axStandbyDownDuplexToSimplexTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 1002, 2, 1, 2, 0, 2)
)
axStandbyDownDuplexToSimplexTrap.setObjects(
      *(("AX-DEVICE-MIB", "axChassisIndex"),
        ("AX-DEVICE-MIB", "axBcuBoardIndex"))
)
if mibBuilder.loadTexts:
    axStandbyDownDuplexToSimplexTrap.setStatus(
        "current"
    )

axBcuMemoryUsageAlarmTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 1002, 2, 1, 2, 0, 3)
)
axBcuMemoryUsageAlarmTrap.setObjects(
      *(("AX-DEVICE-MIB", "axChassisIndex"),
        ("AX-DEVICE-MIB", "axBcuBoardIndex"))
)
if mibBuilder.loadTexts:
    axBcuMemoryUsageAlarmTrap.setStatus(
        "current"
    )

axBcuMemoryUsageRecoveryTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 1002, 2, 1, 2, 0, 4)
)
axBcuMemoryUsageRecoveryTrap.setObjects(
      *(("AX-DEVICE-MIB", "axChassisIndex"),
        ("AX-DEVICE-MIB", "axBcuBoardIndex"))
)
if mibBuilder.loadTexts:
    axBcuMemoryUsageRecoveryTrap.setStatus(
        "current"
    )

axBcuTemperatureTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 1002, 2, 2, 2, 0, 1)
)
axBcuTemperatureTrap.setObjects(
      *(("AX-DEVICE-MIB", "axChassisIndex"),
        ("AX-DEVICE-MIB", "axBcuBoardIndex"),
        ("AX-DEVICE-MIB", "axBcuTemperatureStatusIndex"),
        ("AX-DEVICE-MIB", "axBcuTemperatureState"))
)
if mibBuilder.loadTexts:
    axBcuTemperatureTrap.setStatus(
        "current"
    )

axSfuStateChangeTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 1002, 3, 2, 0, 1)
)
axSfuStateChangeTrap.setObjects(
      *(("AX-DEVICE-MIB", "axChassisIndex"),
        ("AX-DEVICE-MIB", "axSfuBoardIndex"),
        ("AX-DEVICE-MIB", "axSfuOperModeStatus"))
)
if mibBuilder.loadTexts:
    axSfuStateChangeTrap.setStatus(
        "current"
    )

axPruStateChangeTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 1002, 4, 2, 0, 1)
)
axPruStateChangeTrap.setObjects(
      *(("AX-DEVICE-MIB", "axChassisIndex"),
        ("AX-DEVICE-MIB", "axPruBoardIndex"),
        ("AX-DEVICE-MIB", "axPruOperModeStatus"))
)
if mibBuilder.loadTexts:
    axPruStateChangeTrap.setStatus(
        "current"
    )

axPsuStateChangeTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 1002, 5, 2, 0, 1)
)
axPsuStateChangeTrap.setObjects(
      *(("AX-DEVICE-MIB", "axChassisIndex"),
        ("AX-DEVICE-MIB", "axPsuBoardIndex"),
        ("AX-DEVICE-MIB", "axPsuOperModeStatus"))
)
if mibBuilder.loadTexts:
    axPsuStateChangeTrap.setStatus(
        "current"
    )

axNifStateChangeTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 1002, 6, 2, 0, 1)
)
axNifStateChangeTrap.setObjects(
      *(("AX-DEVICE-MIB", "axChassisIndex"),
        ("AX-DEVICE-MIB", "axNifBoardIndex"),
        ("AX-DEVICE-MIB", "axNifOperModeStatus"))
)
if mibBuilder.loadTexts:
    axNifStateChangeTrap.setStatus(
        "current"
    )

axSmcMemoryUsageAlarmTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 1002, 6, 4, 0, 1)
)
axSmcMemoryUsageAlarmTrap.setObjects(
      *(("AX-DEVICE-MIB", "axChassisIndex"),
        ("AX-DEVICE-MIB", "axNifBoardIndex"))
)
if mibBuilder.loadTexts:
    axSmcMemoryUsageAlarmTrap.setStatus(
        "current"
    )

axSmcMemoryUsageRecoveryTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 1002, 6, 4, 0, 2)
)
axSmcMemoryUsageRecoveryTrap.setObjects(
      *(("AX-DEVICE-MIB", "axChassisIndex"),
        ("AX-DEVICE-MIB", "axNifBoardIndex"))
)
if mibBuilder.loadTexts:
    axSmcMemoryUsageRecoveryTrap.setStatus(
        "current"
    )


# Notifications groups

axDeviceTrapGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 1002, 1000, 2, 10)
)
axDeviceTrapGroup.setObjects(
      *(("AX-DEVICE-MIB", "axPowerRedundancyFailureTrap"),
        ("AX-DEVICE-MIB", "axPowerRedundancyRecoveryTrap"),
        ("AX-DEVICE-MIB", "axPowerSupplyInsufficientTrap"),
        ("AX-DEVICE-MIB", "axPowerSupplyInsufficientRecoveryTrap"),
        ("AX-DEVICE-MIB", "axPowerSupplyFailureTrap"),
        ("AX-DEVICE-MIB", "axPowerSupplyRecoveryTrap"),
        ("AX-DEVICE-MIB", "axPowerSupplyStatusChangeTrap"),
        ("AX-DEVICE-MIB", "axAirFanUnitStopTrap"),
        ("AX-DEVICE-MIB", "axAirFanUnitRecoveryTrap"),
        ("AX-DEVICE-MIB", "axStandbyUpSimplexToDuplexTrap"),
        ("AX-DEVICE-MIB", "axStandbyDownDuplexToSimplexTrap"),
        ("AX-DEVICE-MIB", "axBcuMemoryUsageAlarmTrap"),
        ("AX-DEVICE-MIB", "axBcuMemoryUsageRecoveryTrap"),
        ("AX-DEVICE-MIB", "axBcuTemperatureTrap"),
        ("AX-DEVICE-MIB", "axSfuStateChangeTrap"),
        ("AX-DEVICE-MIB", "axPruStateChangeTrap"),
        ("AX-DEVICE-MIB", "axPsuStateChangeTrap"),
        ("AX-DEVICE-MIB", "axNifStateChangeTrap"),
        ("AX-DEVICE-MIB", "axSmcMemoryUsageAlarmTrap"),
        ("AX-DEVICE-MIB", "axSmcMemoryUsageRecoveryTrap"))
)
if mibBuilder.loadTexts:
    axDeviceTrapGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

axDeviceCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 1002, 1000, 1, 1)
)
axDeviceCompliance.setObjects(
      *(("AX-DEVICE-MIB", "axDeviceGroup"),
        ("AX-DEVICE-MIB", "axDeviceTrapGroup"))
)
if mibBuilder.loadTexts:
    axDeviceCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "AX-DEVICE-MIB",
    **{"axDevice": axDevice,
       "axChassis": axChassis,
       "axChassisMaxNumber": axChassisMaxNumber,
       "axChassisTable": axChassisTable,
       "axChassisEntry": axChassisEntry,
       "axChassisIndex": axChassisIndex,
       "axChassisName": axChassisName,
       "axChassisAbbreviation": axChassisAbbreviation,
       "axChassisType": axChassisType,
       "axPowerUnitNumber": axPowerUnitNumber,
       "axFanNumber": axFanNumber,
       "axBcuBoardNumber": axBcuBoardNumber,
       "axSfuBoardNumber": axSfuBoardNumber,
       "axPruBoardNumber": axPruBoardNumber,
       "axPsuBoardNumber": axPsuBoardNumber,
       "axNifBoardNumber": axNifBoardNumber,
       "axChassisSerialInformation": axChassisSerialInformation,
       "axChassisSystemTable": axChassisSystemTable,
       "axChassisSystemEntry": axChassisSystemEntry,
       "axChassisStatus": axChassisStatus,
       "axPowerSupplyUnitRedundancyMode": axPowerSupplyUnitRedundancyMode,
       "axFanMode": axFanMode,
       "axBcuBoardRedundancyStatus": axBcuBoardRedundancyStatus,
       "axTotalPowerSupplyCapacity": axTotalPowerSupplyCapacity,
       "axPowerSupplyCapacitySourceA": axPowerSupplyCapacitySourceA,
       "axPowerSupplyCapacitySourceB": axPowerSupplyCapacitySourceB,
       "axTotalPowerAllocated": axTotalPowerAllocated,
       "axTotalPowerAvailable": axTotalPowerAvailable,
       "axRedundantPowerAvailable": axRedundantPowerAvailable,
       "axPowerAvailableSourceA": axPowerAvailableSourceA,
       "axPowerAvailableSourceB": axPowerAvailableSourceB,
       "axChassisSystemTraps": axChassisSystemTraps,
       "axChassisSystemTrapsPrefix": axChassisSystemTrapsPrefix,
       "axPowerRedundancyFailureTrap": axPowerRedundancyFailureTrap,
       "axPowerRedundancyRecoveryTrap": axPowerRedundancyRecoveryTrap,
       "axPowerSupplyInsufficientTrap": axPowerSupplyInsufficientTrap,
       "axPowerSupplyInsufficientRecoveryTrap": axPowerSupplyInsufficientRecoveryTrap,
       "axPowerSupplyUnitTable": axPowerSupplyUnitTable,
       "axPowerSupplyUnitEntry": axPowerSupplyUnitEntry,
       "axPowerSupplyUnitIndex": axPowerSupplyUnitIndex,
       "axPowerSupplyName": axPowerSupplyName,
       "axPowerSupplyAbbreviation": axPowerSupplyAbbreviation,
       "axPowerSupplySerialInformation": axPowerSupplySerialInformation,
       "axPowerSupplyInputVoltage": axPowerSupplyInputVoltage,
       "axPowerSupplyConnectStatus": axPowerSupplyConnectStatus,
       "axPowerSupplyStatus": axPowerSupplyStatus,
       "axPowerSupplyTotalAccumRunTime": axPowerSupplyTotalAccumRunTime,
       "axPowerSupplyCautionAccumRunTime": axPowerSupplyCautionAccumRunTime,
       "axPowerSupplyCriticalAccumRunTime": axPowerSupplyCriticalAccumRunTime,
       "axPowerSupplyElapsedTime": axPowerSupplyElapsedTime,
       "axPowerSupplyUnitTraps": axPowerSupplyUnitTraps,
       "axPowerSupplyUnitTrapsPrefix": axPowerSupplyUnitTrapsPrefix,
       "axPowerSupplyFailureTrap": axPowerSupplyFailureTrap,
       "axPowerSupplyRecoveryTrap": axPowerSupplyRecoveryTrap,
       "axPowerSupplyStatusChangeTrap": axPowerSupplyStatusChangeTrap,
       "axFanUnitTable": axFanUnitTable,
       "axFanUnitEntry": axFanUnitEntry,
       "axFanUnitIndex": axFanUnitIndex,
       "axFanUnitName": axFanUnitName,
       "axFanUnitAbbreviation": axFanUnitAbbreviation,
       "axFanUnitSerialInformation": axFanUnitSerialInformation,
       "axFanUnitStatus": axFanUnitStatus,
       "axFanUnitSpeed": axFanUnitSpeed,
       "axFanUnitTotalAccumRunTime": axFanUnitTotalAccumRunTime,
       "axFanUnitCautionAccumRunTime": axFanUnitCautionAccumRunTime,
       "axFanUnitCriticalAccumRunTime": axFanUnitCriticalAccumRunTime,
       "axFanUnitElapsedTime": axFanUnitElapsedTime,
       "axFanUnitLedStatus": axFanUnitLedStatus,
       "axAirFanUnitTraps": axAirFanUnitTraps,
       "axAirFanUnitTrapsPrefix": axAirFanUnitTrapsPrefix,
       "axAirFanUnitStopTrap": axAirFanUnitStopTrap,
       "axAirFanUnitRecoveryTrap": axAirFanUnitRecoveryTrap,
       "axBcuBoard": axBcuBoard,
       "axBcuBoardTable": axBcuBoardTable,
       "axBcuBoardEntry": axBcuBoardEntry,
       "axBcuBoardIndex": axBcuBoardIndex,
       "axBcuOperLedStatus": axBcuOperLedStatus,
       "axBcuOperModeStatus": axBcuOperModeStatus,
       "axBcuActiveLedStatus": axBcuActiveLedStatus,
       "axBcuSystem1LedStatus": axBcuSystem1LedStatus,
       "axBcuSystem2LedStatus": axBcuSystem2LedStatus,
       "axBcuBoardName": axBcuBoardName,
       "axBcuBoardAbbreviation": axBcuBoardAbbreviation,
       "axBcuSoftwareVersion": axBcuSoftwareVersion,
       "axBcuFlashTotalSize": axBcuFlashTotalSize,
       "axBcuFlashUsedSize": axBcuFlashUsedSize,
       "axBcuFlashFreeSize": axBcuFlashFreeSize,
       "axBcuTemperatureStatusNumber": axBcuTemperatureStatusNumber,
       "axBcuSerialInformation": axBcuSerialInformation,
       "axBcuTotalAccumRunTime": axBcuTotalAccumRunTime,
       "axBcuCautionAccumRunTime": axBcuCautionAccumRunTime,
       "axBcuCriticalAccumRunTime": axBcuCriticalAccumRunTime,
       "axBcuElapsedTime": axBcuElapsedTime,
       "axBcuBoardTraps": axBcuBoardTraps,
       "axBcuBoardTrapsPrefix": axBcuBoardTrapsPrefix,
       "axStandbyUpSimplexToDuplexTrap": axStandbyUpSimplexToDuplexTrap,
       "axStandbyDownDuplexToSimplexTrap": axStandbyDownDuplexToSimplexTrap,
       "axBcuMemoryUsageAlarmTrap": axBcuMemoryUsageAlarmTrap,
       "axBcuMemoryUsageRecoveryTrap": axBcuMemoryUsageRecoveryTrap,
       "axBcuTemperatureStatusTable": axBcuTemperatureStatusTable,
       "axBcuTemperatureStatusEntry": axBcuTemperatureStatusEntry,
       "axBcuTemperatureStatusIndex": axBcuTemperatureStatusIndex,
       "axBcuTemperatureStatusDescr": axBcuTemperatureStatusDescr,
       "axBcuTemperatureStatusValue": axBcuTemperatureStatusValue,
       "axBcuTemperatureThreshold": axBcuTemperatureThreshold,
       "axBcuTemperatureState": axBcuTemperatureState,
       "axBcuTemperatureWarning": axBcuTemperatureWarning,
       "axBcuTemperatureWarningAverage": axBcuTemperatureWarningAverage,
       "axBcuTemperatureWarningAveragePeriod": axBcuTemperatureWarningAveragePeriod,
       "axBcuTemperatureTraps": axBcuTemperatureTraps,
       "axBcuTemperatureTrapsPrefix": axBcuTemperatureTrapsPrefix,
       "axBcuTemperatureTrap": axBcuTemperatureTrap,
       "axMemoryCardTable": axMemoryCardTable,
       "axMemoryCardEntry": axMemoryCardEntry,
       "axMemoryCardIndex": axMemoryCardIndex,
       "axMemoryCardConnection": axMemoryCardConnection,
       "axMemoryCardID": axMemoryCardID,
       "axMemoryCardTotalSize": axMemoryCardTotalSize,
       "axMemoryCardUsedSize": axMemoryCardUsedSize,
       "axMemoryCardFreeSize": axMemoryCardFreeSize,
       "axBcuCpuTable": axBcuCpuTable,
       "axBcuCpuEntry": axBcuCpuEntry,
       "axBcuCpuIndex": axBcuCpuIndex,
       "axBcuCpuStatus": axBcuCpuStatus,
       "axBcuCpuUpTime": axBcuCpuUpTime,
       "axBcuCpuClock": axBcuCpuClock,
       "axBcuCpuLoad1m": axBcuCpuLoad1m,
       "axBcuMemoryTotalSize": axBcuMemoryTotalSize,
       "axBcuMemoryUsedSize": axBcuMemoryUsedSize,
       "axBcuMemoryFreeSize": axBcuMemoryFreeSize,
       "axBcuFatalErrorRestartNum": axBcuFatalErrorRestartNum,
       "axSfuBoard": axSfuBoard,
       "axSfuBoardTable": axSfuBoardTable,
       "axSfuBoardEntry": axSfuBoardEntry,
       "axSfuBoardIndex": axSfuBoardIndex,
       "axSfuBoardType": axSfuBoardType,
       "axSfuOperLedStatus": axSfuOperLedStatus,
       "axSfuActiveLedStatus": axSfuActiveLedStatus,
       "axSfuOperModeStatus": axSfuOperModeStatus,
       "axSfuUpdateStatus": axSfuUpdateStatus,
       "axSfuErrorRestartNum": axSfuErrorRestartNum,
       "axSfuBoardName": axSfuBoardName,
       "axSfuBoardAbbreviation": axSfuBoardAbbreviation,
       "axSfuSerialInformation": axSfuSerialInformation,
       "axSfuTemperatureState": axSfuTemperatureState,
       "axSfuTotalAccumRunTime": axSfuTotalAccumRunTime,
       "axSfuCautionAccumRunTime": axSfuCautionAccumRunTime,
       "axSfuCriticalAccumRunTime": axSfuCriticalAccumRunTime,
       "axSfuElapsedTime": axSfuElapsedTime,
       "axSfuBoardTraps": axSfuBoardTraps,
       "axSfuStateChangeTrapPrefix": axSfuStateChangeTrapPrefix,
       "axSfuStateChangeTrap": axSfuStateChangeTrap,
       "axPruBoard": axPruBoard,
       "axPruBoardTable": axPruBoardTable,
       "axPruBoardEntry": axPruBoardEntry,
       "axPruBoardIndex": axPruBoardIndex,
       "axPruBoardType": axPruBoardType,
       "axPruOperLedStatus": axPruOperLedStatus,
       "axPruOperModeStatus": axPruOperModeStatus,
       "axPruUpdateStatus": axPruUpdateStatus,
       "axPruErrorRestartNum": axPruErrorRestartNum,
       "axPruBoardName": axPruBoardName,
       "axPruBoardAbbreviation": axPruBoardAbbreviation,
       "axPruSerialInformation": axPruSerialInformation,
       "axPruCpuUpTime": axPruCpuUpTime,
       "axPruCpuClock": axPruCpuClock,
       "axPruCpuLoad1m": axPruCpuLoad1m,
       "axPruMemoryTotalSize": axPruMemoryTotalSize,
       "axPruMemoryUsedSize": axPruMemoryUsedSize,
       "axPruMemoryFreeSize": axPruMemoryFreeSize,
       "axPruTemperatureState": axPruTemperatureState,
       "axPruTotalAccumRunTime": axPruTotalAccumRunTime,
       "axPruCautionAccumRunTime": axPruCautionAccumRunTime,
       "axPruCriticalAccumRunTime": axPruCriticalAccumRunTime,
       "axPruElapsedTime": axPruElapsedTime,
       "axPruBoardTraps": axPruBoardTraps,
       "axPruStateChangeTrapPrefix": axPruStateChangeTrapPrefix,
       "axPruStateChangeTrap": axPruStateChangeTrap,
       "axPsuBoard": axPsuBoard,
       "axPsuBoardTable": axPsuBoardTable,
       "axPsuBoardEntry": axPsuBoardEntry,
       "axPsuBoardIndex": axPsuBoardIndex,
       "axPsuBoardType": axPsuBoardType,
       "axPsuOperLedStatus": axPsuOperLedStatus,
       "axPsuOperModeStatus": axPsuOperModeStatus,
       "axPsuUpdateStatus": axPsuUpdateStatus,
       "axPsuErrorRestartNum": axPsuErrorRestartNum,
       "axPsuBoardName": axPsuBoardName,
       "axPsuBoardAbbreviation": axPsuBoardAbbreviation,
       "axPsuSerialInformation": axPsuSerialInformation,
       "axPsuCpuUpTime": axPsuCpuUpTime,
       "axPsuCpuClock": axPsuCpuClock,
       "axPsuCpuLoad1m": axPsuCpuLoad1m,
       "axPsuMemoryTotalSize": axPsuMemoryTotalSize,
       "axPsuMemoryUsedSize": axPsuMemoryUsedSize,
       "axPsuMemoryFreeSize": axPsuMemoryFreeSize,
       "axPsuTemperatureState": axPsuTemperatureState,
       "axPsuTotalAccumRunTime": axPsuTotalAccumRunTime,
       "axPsuCautionAccumRunTime": axPsuCautionAccumRunTime,
       "axPsuCriticalAccumRunTime": axPsuCriticalAccumRunTime,
       "axPsuElapsedTime": axPsuElapsedTime,
       "axPsuBoardTraps": axPsuBoardTraps,
       "axPsuStateChangeTrapPrefix": axPsuStateChangeTrapPrefix,
       "axPsuStateChangeTrap": axPsuStateChangeTrap,
       "axNifBoard": axNifBoard,
       "axNifBoardTable": axNifBoardTable,
       "axNifBoardEntry": axNifBoardEntry,
       "axNifBoardIndex": axNifBoardIndex,
       "axNifBoardType": axNifBoardType,
       "axNifOperLedStatus": axNifOperLedStatus,
       "axNifOperModeStatus": axNifOperModeStatus,
       "axNifUpdateStatus": axNifUpdateStatus,
       "axNifErrorRestartNum": axNifErrorRestartNum,
       "axNifBoardName": axNifBoardName,
       "axNifBoardAbbreviation": axNifBoardAbbreviation,
       "axNifPhysLineNumber": axNifPhysLineNumber,
       "axNifSerialInformation": axNifSerialInformation,
       "axNifTemperatureState": axNifTemperatureState,
       "axNifTotalAccumRunTime": axNifTotalAccumRunTime,
       "axNifCautionAccumRunTime": axNifCautionAccumRunTime,
       "axNifCriticalAccumRunTime": axNifCriticalAccumRunTime,
       "axNifElapsedTime": axNifElapsedTime,
       "axNifReadyLedStatus": axNifReadyLedStatus,
       "axNifBoardTraps": axNifBoardTraps,
       "axNifStateChangeTrapPrefix": axNifStateChangeTrapPrefix,
       "axNifStateChangeTrap": axNifStateChangeTrap,
       "axSmcTable": axSmcTable,
       "axSmcEntry": axSmcEntry,
       "axSmcCpuClock": axSmcCpuClock,
       "axSmcCpuLoad1m": axSmcCpuLoad1m,
       "axSmcMemoryTotalSize": axSmcMemoryTotalSize,
       "axSmcMemoryUsedSize": axSmcMemoryUsedSize,
       "axSmcMemoryFreeSize": axSmcMemoryFreeSize,
       "axSmcBoardTraps": axSmcBoardTraps,
       "axSmcBoardTrapsPrefix": axSmcBoardTrapsPrefix,
       "axSmcMemoryUsageAlarmTrap": axSmcMemoryUsageAlarmTrap,
       "axSmcMemoryUsageRecoveryTrap": axSmcMemoryUsageRecoveryTrap,
       "axPhysLine": axPhysLine,
       "axPhysLineTable": axPhysLineTable,
       "axPhysLineEntry": axPhysLineEntry,
       "axPhysLineIndex": axPhysLineIndex,
       "axPhysLineConnectorType": axPhysLineConnectorType,
       "axPhysLineOperStatus": axPhysLineOperStatus,
       "axPhysLineIfIndexNumber": axPhysLineIfIndexNumber,
       "axPhysLineTransceiverStatus": axPhysLineTransceiverStatus,
       "axPhysLineLaneTable": axPhysLineLaneTable,
       "axPhysLineLaneEntry": axPhysLineLaneEntry,
       "axPhysLineLaneIndex": axPhysLineLaneIndex,
       "axPhysLineLaneTransceiverTxPower": axPhysLineLaneTransceiverTxPower,
       "axPhysLineLaneTransceiverRxPower": axPhysLineLaneTransceiverRxPower,
       "axInterface": axInterface,
       "axLineIfTable": axLineIfTable,
       "axLineIfEntry": axLineIfEntry,
       "axLineIfIndex": axLineIfIndex,
       "axIfIndex": axIfIndex,
       "axIfIpAddress": axIfIpAddress,
       "axIfIpv6Address": axIfIpv6Address,
       "axDeviceConformance": axDeviceConformance,
       "axDeviceCompliances": axDeviceCompliances,
       "axDeviceCompliance": axDeviceCompliance,
       "axDeviceGroups": axDeviceGroups,
       "axDeviceGroup": axDeviceGroup,
       "axDeviceTrapGroup": axDeviceTrapGroup}
)
