# SNMP MIB module (DCP-INTERFACE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\smartoptics\DCP-INTERFACE-MIB

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

(dcpGeneric,) = mibBuilder.importSymbols(
    "DCP-MIB",
    "dcpGeneric")

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

(InterfacePortMode,
 InterfaceStatus,
 ItuPerceivedSeverity,
 OpticalPower1Decimal) = mibBuilder.importSymbols(
    "SO-TC-MIB",
    "InterfacePortMode",
    "InterfaceStatus",
    "ItuPerceivedSeverity",
    "OpticalPower1Decimal")


# MODULE-IDENTITY

dcpInterface = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 30826, 2, 2, 1)
)
if mibBuilder.loadTexts:
    dcpInterface.setRevisions(
        ("2023-07-03 04:00",
         "2023-07-01 10:00",
         "2022-12-16 12:00",
         "2022-03-18 13:00",
         "2021-02-25 12:00",
         "2019-10-29 15:00",
         "2018-10-08 14:44")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_DcpInterfaceObjects_ObjectIdentity = ObjectIdentity
dcpInterfaceObjects = _DcpInterfaceObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30826, 2, 2, 1, 1)
)
_DcpInterfaceTable_Object = MibTable
dcpInterfaceTable = _DcpInterfaceTable_Object(
    (1, 3, 6, 1, 4, 1, 30826, 2, 2, 1, 1, 1)
)
if mibBuilder.loadTexts:
    dcpInterfaceTable.setStatus("current")
_DcpInterfaceEntry_Object = MibTableRow
dcpInterfaceEntry = _DcpInterfaceEntry_Object(
    (1, 3, 6, 1, 4, 1, 30826, 2, 2, 1, 1, 1, 1)
)
dcpInterfaceEntry.setIndexNames(
    (0, "DCP-INTERFACE-MIB", "dcpInterfaceIndex"),
)
if mibBuilder.loadTexts:
    dcpInterfaceEntry.setStatus("current")


class _DcpInterfaceIndex_Type(Unsigned32):
    """Custom type dcpInterfaceIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1000000),
    )


_DcpInterfaceIndex_Type.__name__ = "Unsigned32"
_DcpInterfaceIndex_Object = MibTableColumn
dcpInterfaceIndex = _DcpInterfaceIndex_Object(
    (1, 3, 6, 1, 4, 1, 30826, 2, 2, 1, 1, 1, 1, 1),
    _DcpInterfaceIndex_Type()
)
dcpInterfaceIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dcpInterfaceIndex.setStatus("current")
_DcpInterfaceName_Type = DisplayString
_DcpInterfaceName_Object = MibTableColumn
dcpInterfaceName = _DcpInterfaceName_Object(
    (1, 3, 6, 1, 4, 1, 30826, 2, 2, 1, 1, 1, 1, 2),
    _DcpInterfaceName_Type()
)
dcpInterfaceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcpInterfaceName.setStatus("current")
_DcpInterfaceRxPower_Type = OpticalPower1Decimal
_DcpInterfaceRxPower_Object = MibTableColumn
dcpInterfaceRxPower = _DcpInterfaceRxPower_Object(
    (1, 3, 6, 1, 4, 1, 30826, 2, 2, 1, 1, 1, 1, 3),
    _DcpInterfaceRxPower_Type()
)
dcpInterfaceRxPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcpInterfaceRxPower.setStatus("current")
_DcpInterfaceTxPower_Type = OpticalPower1Decimal
_DcpInterfaceTxPower_Object = MibTableColumn
dcpInterfaceTxPower = _DcpInterfaceTxPower_Object(
    (1, 3, 6, 1, 4, 1, 30826, 2, 2, 1, 1, 1, 1, 4),
    _DcpInterfaceTxPower_Type()
)
dcpInterfaceTxPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcpInterfaceTxPower.setStatus("current")
_DcpInterfaceStatus_Type = InterfaceStatus
_DcpInterfaceStatus_Object = MibTableColumn
dcpInterfaceStatus = _DcpInterfaceStatus_Object(
    (1, 3, 6, 1, 4, 1, 30826, 2, 2, 1, 1, 1, 1, 5),
    _DcpInterfaceStatus_Type()
)
dcpInterfaceStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcpInterfaceStatus.setStatus("current")
_DcpInterfaceAlarm_Type = ItuPerceivedSeverity
_DcpInterfaceAlarm_Object = MibTableColumn
dcpInterfaceAlarm = _DcpInterfaceAlarm_Object(
    (1, 3, 6, 1, 4, 1, 30826, 2, 2, 1, 1, 1, 1, 6),
    _DcpInterfaceAlarm_Type()
)
dcpInterfaceAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcpInterfaceAlarm.setStatus("current")
_DcpInterfaceFormat_Type = DisplayString
_DcpInterfaceFormat_Object = MibTableColumn
dcpInterfaceFormat = _DcpInterfaceFormat_Object(
    (1, 3, 6, 1, 4, 1, 30826, 2, 2, 1, 1, 1, 1, 7),
    _DcpInterfaceFormat_Type()
)
dcpInterfaceFormat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcpInterfaceFormat.setStatus("current")
_DcpInterfaceWavelength_Type = DisplayString
_DcpInterfaceWavelength_Object = MibTableColumn
dcpInterfaceWavelength = _DcpInterfaceWavelength_Object(
    (1, 3, 6, 1, 4, 1, 30826, 2, 2, 1, 1, 1, 1, 8),
    _DcpInterfaceWavelength_Type()
)
dcpInterfaceWavelength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcpInterfaceWavelength.setStatus("current")
_DcpInterfaceChannelId_Type = DisplayString
_DcpInterfaceChannelId_Object = MibTableColumn
dcpInterfaceChannelId = _DcpInterfaceChannelId_Object(
    (1, 3, 6, 1, 4, 1, 30826, 2, 2, 1, 1, 1, 1, 9),
    _DcpInterfaceChannelId_Type()
)
dcpInterfaceChannelId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcpInterfaceChannelId.setStatus("current")


class _DcpInterfaceDescription_Type(DisplayString):
    """Custom type dcpInterfaceDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_DcpInterfaceDescription_Type.__name__ = "DisplayString"
_DcpInterfaceDescription_Object = MibTableColumn
dcpInterfaceDescription = _DcpInterfaceDescription_Object(
    (1, 3, 6, 1, 4, 1, 30826, 2, 2, 1, 1, 1, 1, 10),
    _DcpInterfaceDescription_Type()
)
dcpInterfaceDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcpInterfaceDescription.setStatus("current")


class _DcpInterfacePortType_Type(DisplayString):
    """Custom type dcpInterfacePortType based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_DcpInterfacePortType_Type.__name__ = "DisplayString"
_DcpInterfacePortType_Object = MibTableColumn
dcpInterfacePortType = _DcpInterfacePortType_Object(
    (1, 3, 6, 1, 4, 1, 30826, 2, 2, 1, 1, 1, 1, 11),
    _DcpInterfacePortType_Type()
)
dcpInterfacePortType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcpInterfacePortType.setStatus("current")
_DcpInterfacePortMode_Type = InterfacePortMode
_DcpInterfacePortMode_Object = MibTableColumn
dcpInterfacePortMode = _DcpInterfacePortMode_Object(
    (1, 3, 6, 1, 4, 1, 30826, 2, 2, 1, 1, 1, 1, 12),
    _DcpInterfacePortMode_Type()
)
dcpInterfacePortMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcpInterfacePortMode.setStatus("current")
_DcpInterfaceMIBCompliance_ObjectIdentity = ObjectIdentity
dcpInterfaceMIBCompliance = _DcpInterfaceMIBCompliance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30826, 2, 2, 1, 2)
)
_DcpInterfaceMIBGroups_ObjectIdentity = ObjectIdentity
dcpInterfaceMIBGroups = _DcpInterfaceMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30826, 2, 2, 1, 2, 1)
)
_DcpInterfaceMIBCompliances_ObjectIdentity = ObjectIdentity
dcpInterfaceMIBCompliances = _DcpInterfaceMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30826, 2, 2, 1, 2, 2)
)
_DcpInterfaceTrxMIBGroups_ObjectIdentity = ObjectIdentity
dcpInterfaceTrxMIBGroups = _DcpInterfaceTrxMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30826, 2, 2, 1, 2, 3)
)
_DcpInterfaceTrxLanesMIBGroups_ObjectIdentity = ObjectIdentity
dcpInterfaceTrxLanesMIBGroups = _DcpInterfaceTrxLanesMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30826, 2, 2, 1, 2, 4)
)
_DcpInterfaceTrxObjects_ObjectIdentity = ObjectIdentity
dcpInterfaceTrxObjects = _DcpInterfaceTrxObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30826, 2, 2, 1, 3)
)
_DcpInterfaceTrxTable_Object = MibTable
dcpInterfaceTrxTable = _DcpInterfaceTrxTable_Object(
    (1, 3, 6, 1, 4, 1, 30826, 2, 2, 1, 3, 1)
)
if mibBuilder.loadTexts:
    dcpInterfaceTrxTable.setStatus("current")
_DcpInterfaceTrxEntry_Object = MibTableRow
dcpInterfaceTrxEntry = _DcpInterfaceTrxEntry_Object(
    (1, 3, 6, 1, 4, 1, 30826, 2, 2, 1, 3, 1, 1)
)
dcpInterfaceTrxEntry.setIndexNames(
    (0, "DCP-INTERFACE-MIB", "dcpInterfaceTrxIndex"),
)
if mibBuilder.loadTexts:
    dcpInterfaceTrxEntry.setStatus("current")


class _DcpInterfaceTrxIndex_Type(Unsigned32):
    """Custom type dcpInterfaceTrxIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1000000),
    )


_DcpInterfaceTrxIndex_Type.__name__ = "Unsigned32"
_DcpInterfaceTrxIndex_Object = MibTableColumn
dcpInterfaceTrxIndex = _DcpInterfaceTrxIndex_Object(
    (1, 3, 6, 1, 4, 1, 30826, 2, 2, 1, 3, 1, 1, 1),
    _DcpInterfaceTrxIndex_Type()
)
dcpInterfaceTrxIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dcpInterfaceTrxIndex.setStatus("current")
_DcpInterfaceTrxName_Type = DisplayString
_DcpInterfaceTrxName_Object = MibTableColumn
dcpInterfaceTrxName = _DcpInterfaceTrxName_Object(
    (1, 3, 6, 1, 4, 1, 30826, 2, 2, 1, 3, 1, 1, 2),
    _DcpInterfaceTrxName_Type()
)
dcpInterfaceTrxName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcpInterfaceTrxName.setStatus("current")
_DcpInterfaceTrxLanes_Type = Unsigned32
_DcpInterfaceTrxLanes_Object = MibTableColumn
dcpInterfaceTrxLanes = _DcpInterfaceTrxLanes_Object(
    (1, 3, 6, 1, 4, 1, 30826, 2, 2, 1, 3, 1, 1, 3),
    _DcpInterfaceTrxLanes_Type()
)
dcpInterfaceTrxLanes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcpInterfaceTrxLanes.setStatus("current")
_DcpInterfaceTrxTemperature_Type = OpticalPower1Decimal
_DcpInterfaceTrxTemperature_Object = MibTableColumn
dcpInterfaceTrxTemperature = _DcpInterfaceTrxTemperature_Object(
    (1, 3, 6, 1, 4, 1, 30826, 2, 2, 1, 3, 1, 1, 4),
    _DcpInterfaceTrxTemperature_Type()
)
dcpInterfaceTrxTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcpInterfaceTrxTemperature.setStatus("current")
_DcpInterfaceTrxTemperatureHighWarningThreshold_Type = OpticalPower1Decimal
_DcpInterfaceTrxTemperatureHighWarningThreshold_Object = MibTableColumn
dcpInterfaceTrxTemperatureHighWarningThreshold = _DcpInterfaceTrxTemperatureHighWarningThreshold_Object(
    (1, 3, 6, 1, 4, 1, 30826, 2, 2, 1, 3, 1, 1, 5),
    _DcpInterfaceTrxTemperatureHighWarningThreshold_Type()
)
dcpInterfaceTrxTemperatureHighWarningThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcpInterfaceTrxTemperatureHighWarningThreshold.setStatus("current")
_DcpInterfaceTrxTemperatureHighAlarmThreshold_Type = OpticalPower1Decimal
_DcpInterfaceTrxTemperatureHighAlarmThreshold_Object = MibTableColumn
dcpInterfaceTrxTemperatureHighAlarmThreshold = _DcpInterfaceTrxTemperatureHighAlarmThreshold_Object(
    (1, 3, 6, 1, 4, 1, 30826, 2, 2, 1, 3, 1, 1, 6),
    _DcpInterfaceTrxTemperatureHighAlarmThreshold_Type()
)
dcpInterfaceTrxTemperatureHighAlarmThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcpInterfaceTrxTemperatureHighAlarmThreshold.setStatus("current")
_DcpInterfaceTrxWavelength_Type = DisplayString
_DcpInterfaceTrxWavelength_Object = MibTableColumn
dcpInterfaceTrxWavelength = _DcpInterfaceTrxWavelength_Object(
    (1, 3, 6, 1, 4, 1, 30826, 2, 2, 1, 3, 1, 1, 7),
    _DcpInterfaceTrxWavelength_Type()
)
dcpInterfaceTrxWavelength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcpInterfaceTrxWavelength.setStatus("current")
_DcpInterfaceTrxChannelId_Type = DisplayString
_DcpInterfaceTrxChannelId_Object = MibTableColumn
dcpInterfaceTrxChannelId = _DcpInterfaceTrxChannelId_Object(
    (1, 3, 6, 1, 4, 1, 30826, 2, 2, 1, 3, 1, 1, 8),
    _DcpInterfaceTrxChannelId_Type()
)
dcpInterfaceTrxChannelId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcpInterfaceTrxChannelId.setStatus("current")
_DcpInterfaceTrxActualFrequency_Type = OpticalPower1Decimal
_DcpInterfaceTrxActualFrequency_Object = MibTableColumn
dcpInterfaceTrxActualFrequency = _DcpInterfaceTrxActualFrequency_Object(
    (1, 3, 6, 1, 4, 1, 30826, 2, 2, 1, 3, 1, 1, 9),
    _DcpInterfaceTrxActualFrequency_Type()
)
dcpInterfaceTrxActualFrequency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcpInterfaceTrxActualFrequency.setStatus("current")
_DcpInterfaceTrxWantedFrequency_Type = OpticalPower1Decimal
_DcpInterfaceTrxWantedFrequency_Object = MibTableColumn
dcpInterfaceTrxWantedFrequency = _DcpInterfaceTrxWantedFrequency_Object(
    (1, 3, 6, 1, 4, 1, 30826, 2, 2, 1, 3, 1, 1, 10),
    _DcpInterfaceTrxWantedFrequency_Type()
)
dcpInterfaceTrxWantedFrequency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcpInterfaceTrxWantedFrequency.setStatus("current")
_DcpInterfaceTrxGridSpacing_Type = OpticalPower1Decimal
_DcpInterfaceTrxGridSpacing_Object = MibTableColumn
dcpInterfaceTrxGridSpacing = _DcpInterfaceTrxGridSpacing_Object(
    (1, 3, 6, 1, 4, 1, 30826, 2, 2, 1, 3, 1, 1, 11),
    _DcpInterfaceTrxGridSpacing_Type()
)
dcpInterfaceTrxGridSpacing.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcpInterfaceTrxGridSpacing.setStatus("current")
_DcpInterfaceTrxTotalRxPower_Type = OpticalPower1Decimal
_DcpInterfaceTrxTotalRxPower_Object = MibTableColumn
dcpInterfaceTrxTotalRxPower = _DcpInterfaceTrxTotalRxPower_Object(
    (1, 3, 6, 1, 4, 1, 30826, 2, 2, 1, 3, 1, 1, 12),
    _DcpInterfaceTrxTotalRxPower_Type()
)
dcpInterfaceTrxTotalRxPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcpInterfaceTrxTotalRxPower.setStatus("current")
_DcpInterfaceTrxSignalRxPower_Type = OpticalPower1Decimal
_DcpInterfaceTrxSignalRxPower_Object = MibTableColumn
dcpInterfaceTrxSignalRxPower = _DcpInterfaceTrxSignalRxPower_Object(
    (1, 3, 6, 1, 4, 1, 30826, 2, 2, 1, 3, 1, 1, 13),
    _DcpInterfaceTrxSignalRxPower_Type()
)
dcpInterfaceTrxSignalRxPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcpInterfaceTrxSignalRxPower.setStatus("current")
_DcpInterfaceTrxTxPower_Type = OpticalPower1Decimal
_DcpInterfaceTrxTxPower_Object = MibTableColumn
dcpInterfaceTrxTxPower = _DcpInterfaceTrxTxPower_Object(
    (1, 3, 6, 1, 4, 1, 30826, 2, 2, 1, 3, 1, 1, 14),
    _DcpInterfaceTrxTxPower_Type()
)
dcpInterfaceTrxTxPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcpInterfaceTrxTxPower.setStatus("current")
_DcpInterfaceTrxTxBias_Type = OpticalPower1Decimal
_DcpInterfaceTrxTxBias_Object = MibTableColumn
dcpInterfaceTrxTxBias = _DcpInterfaceTrxTxBias_Object(
    (1, 3, 6, 1, 4, 1, 30826, 2, 2, 1, 3, 1, 1, 15),
    _DcpInterfaceTrxTxBias_Type()
)
dcpInterfaceTrxTxBias.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcpInterfaceTrxTxBias.setStatus("current")
_DcpInterfaceTrxRxSensitivity_Type = OpticalPower1Decimal
_DcpInterfaceTrxRxSensitivity_Object = MibTableColumn
dcpInterfaceTrxRxSensitivity = _DcpInterfaceTrxRxSensitivity_Object(
    (1, 3, 6, 1, 4, 1, 30826, 2, 2, 1, 3, 1, 1, 16),
    _DcpInterfaceTrxRxSensitivity_Type()
)
dcpInterfaceTrxRxSensitivity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcpInterfaceTrxRxSensitivity.setStatus("current")
_DcpInterfaceTrxRxLosThreshold_Type = OpticalPower1Decimal
_DcpInterfaceTrxRxLosThreshold_Object = MibTableColumn
dcpInterfaceTrxRxLosThreshold = _DcpInterfaceTrxRxLosThreshold_Object(
    (1, 3, 6, 1, 4, 1, 30826, 2, 2, 1, 3, 1, 1, 17),
    _DcpInterfaceTrxRxLosThreshold_Type()
)
dcpInterfaceTrxRxLosThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcpInterfaceTrxRxLosThreshold.setStatus("current")
_DcpInterfaceTrxModulationType_Type = DisplayString
_DcpInterfaceTrxModulationType_Object = MibTableColumn
dcpInterfaceTrxModulationType = _DcpInterfaceTrxModulationType_Object(
    (1, 3, 6, 1, 4, 1, 30826, 2, 2, 1, 3, 1, 1, 18),
    _DcpInterfaceTrxModulationType_Type()
)
dcpInterfaceTrxModulationType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcpInterfaceTrxModulationType.setStatus("current")
_DcpInterfaceTrxBandwidth_Type = Unsigned32
_DcpInterfaceTrxBandwidth_Object = MibTableColumn
dcpInterfaceTrxBandwidth = _DcpInterfaceTrxBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 30826, 2, 2, 1, 3, 1, 1, 19),
    _DcpInterfaceTrxBandwidth_Type()
)
dcpInterfaceTrxBandwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcpInterfaceTrxBandwidth.setStatus("current")
_DcpInterfaceTrxFec_Type = DisplayString
_DcpInterfaceTrxFec_Object = MibTableColumn
dcpInterfaceTrxFec = _DcpInterfaceTrxFec_Object(
    (1, 3, 6, 1, 4, 1, 30826, 2, 2, 1, 3, 1, 1, 20),
    _DcpInterfaceTrxFec_Type()
)
dcpInterfaceTrxFec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcpInterfaceTrxFec.setStatus("current")
_DcpInterfaceTrxPulseShaping_Type = DisplayString
_DcpInterfaceTrxPulseShaping_Object = MibTableColumn
dcpInterfaceTrxPulseShaping = _DcpInterfaceTrxPulseShaping_Object(
    (1, 3, 6, 1, 4, 1, 30826, 2, 2, 1, 3, 1, 1, 21),
    _DcpInterfaceTrxPulseShaping_Type()
)
dcpInterfaceTrxPulseShaping.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcpInterfaceTrxPulseShaping.setStatus("current")
_DcpInterfaceTrxCertified_Type = DisplayString
_DcpInterfaceTrxCertified_Object = MibTableColumn
dcpInterfaceTrxCertified = _DcpInterfaceTrxCertified_Object(
    (1, 3, 6, 1, 4, 1, 30826, 2, 2, 1, 3, 1, 1, 22),
    _DcpInterfaceTrxCertified_Type()
)
dcpInterfaceTrxCertified.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcpInterfaceTrxCertified.setStatus("current")
_DcpInterfaceTrxOsnr_Type = OpticalPower1Decimal
_DcpInterfaceTrxOsnr_Object = MibTableColumn
dcpInterfaceTrxOsnr = _DcpInterfaceTrxOsnr_Object(
    (1, 3, 6, 1, 4, 1, 30826, 2, 2, 1, 3, 1, 1, 23),
    _DcpInterfaceTrxOsnr_Type()
)
dcpInterfaceTrxOsnr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcpInterfaceTrxOsnr.setStatus("current")
_DcpInterfaceTrxChromaticDispersion_Type = Integer32
_DcpInterfaceTrxChromaticDispersion_Object = MibTableColumn
dcpInterfaceTrxChromaticDispersion = _DcpInterfaceTrxChromaticDispersion_Object(
    (1, 3, 6, 1, 4, 1, 30826, 2, 2, 1, 3, 1, 1, 24),
    _DcpInterfaceTrxChromaticDispersion_Type()
)
dcpInterfaceTrxChromaticDispersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcpInterfaceTrxChromaticDispersion.setStatus("current")
_DcpInterfaceTrxDiffGroupDelay_Type = OpticalPower1Decimal
_DcpInterfaceTrxDiffGroupDelay_Object = MibTableColumn
dcpInterfaceTrxDiffGroupDelay = _DcpInterfaceTrxDiffGroupDelay_Object(
    (1, 3, 6, 1, 4, 1, 30826, 2, 2, 1, 3, 1, 1, 25),
    _DcpInterfaceTrxDiffGroupDelay_Type()
)
dcpInterfaceTrxDiffGroupDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcpInterfaceTrxDiffGroupDelay.setStatus("current")
_DcpInterfaceTrxPolarizationDependentLoss_Type = OpticalPower1Decimal
_DcpInterfaceTrxPolarizationDependentLoss_Object = MibTableColumn
dcpInterfaceTrxPolarizationDependentLoss = _DcpInterfaceTrxPolarizationDependentLoss_Object(
    (1, 3, 6, 1, 4, 1, 30826, 2, 2, 1, 3, 1, 1, 26),
    _DcpInterfaceTrxPolarizationDependentLoss_Type()
)
dcpInterfaceTrxPolarizationDependentLoss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcpInterfaceTrxPolarizationDependentLoss.setStatus("current")
_DcpInterfaceTrxPreFecBerMantissa_Type = OpticalPower1Decimal
_DcpInterfaceTrxPreFecBerMantissa_Object = MibTableColumn
dcpInterfaceTrxPreFecBerMantissa = _DcpInterfaceTrxPreFecBerMantissa_Object(
    (1, 3, 6, 1, 4, 1, 30826, 2, 2, 1, 3, 1, 1, 27),
    _DcpInterfaceTrxPreFecBerMantissa_Type()
)
dcpInterfaceTrxPreFecBerMantissa.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcpInterfaceTrxPreFecBerMantissa.setStatus("current")


class _DcpInterfaceTrxPreFecBerExponent_Type(Integer32):
    """Custom type dcpInterfaceTrxPreFecBerExponent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-30, 0),
    )


_DcpInterfaceTrxPreFecBerExponent_Type.__name__ = "Integer32"
_DcpInterfaceTrxPreFecBerExponent_Object = MibTableColumn
dcpInterfaceTrxPreFecBerExponent = _DcpInterfaceTrxPreFecBerExponent_Object(
    (1, 3, 6, 1, 4, 1, 30826, 2, 2, 1, 3, 1, 1, 28),
    _DcpInterfaceTrxPreFecBerExponent_Type()
)
dcpInterfaceTrxPreFecBerExponent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcpInterfaceTrxPreFecBerExponent.setStatus("current")
_DcpInterfaceTrxPreFecBerAvgMantissa_Type = OpticalPower1Decimal
_DcpInterfaceTrxPreFecBerAvgMantissa_Object = MibTableColumn
dcpInterfaceTrxPreFecBerAvgMantissa = _DcpInterfaceTrxPreFecBerAvgMantissa_Object(
    (1, 3, 6, 1, 4, 1, 30826, 2, 2, 1, 3, 1, 1, 29),
    _DcpInterfaceTrxPreFecBerAvgMantissa_Type()
)
dcpInterfaceTrxPreFecBerAvgMantissa.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcpInterfaceTrxPreFecBerAvgMantissa.setStatus("current")


class _DcpInterfaceTrxPreFecBerAvgExponent_Type(Integer32):
    """Custom type dcpInterfaceTrxPreFecBerAvgExponent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-30, 0),
    )


_DcpInterfaceTrxPreFecBerAvgExponent_Type.__name__ = "Integer32"
_DcpInterfaceTrxPreFecBerAvgExponent_Object = MibTableColumn
dcpInterfaceTrxPreFecBerAvgExponent = _DcpInterfaceTrxPreFecBerAvgExponent_Object(
    (1, 3, 6, 1, 4, 1, 30826, 2, 2, 1, 3, 1, 1, 30),
    _DcpInterfaceTrxPreFecBerAvgExponent_Type()
)
dcpInterfaceTrxPreFecBerAvgExponent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcpInterfaceTrxPreFecBerAvgExponent.setStatus("current")
_DcpInterfaceTrxUncorrectedBerMantissa_Type = OpticalPower1Decimal
_DcpInterfaceTrxUncorrectedBerMantissa_Object = MibTableColumn
dcpInterfaceTrxUncorrectedBerMantissa = _DcpInterfaceTrxUncorrectedBerMantissa_Object(
    (1, 3, 6, 1, 4, 1, 30826, 2, 2, 1, 3, 1, 1, 31),
    _DcpInterfaceTrxUncorrectedBerMantissa_Type()
)
dcpInterfaceTrxUncorrectedBerMantissa.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcpInterfaceTrxUncorrectedBerMantissa.setStatus("current")


class _DcpInterfaceTrxUncorrectedBerExponent_Type(Integer32):
    """Custom type dcpInterfaceTrxUncorrectedBerExponent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-30, 0),
    )


_DcpInterfaceTrxUncorrectedBerExponent_Type.__name__ = "Integer32"
_DcpInterfaceTrxUncorrectedBerExponent_Object = MibTableColumn
dcpInterfaceTrxUncorrectedBerExponent = _DcpInterfaceTrxUncorrectedBerExponent_Object(
    (1, 3, 6, 1, 4, 1, 30826, 2, 2, 1, 3, 1, 1, 32),
    _DcpInterfaceTrxUncorrectedBerExponent_Type()
)
dcpInterfaceTrxUncorrectedBerExponent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcpInterfaceTrxUncorrectedBerExponent.setStatus("current")
_DcpInterfaceTrxPostFecBerMantissa_Type = OpticalPower1Decimal
_DcpInterfaceTrxPostFecBerMantissa_Object = MibTableColumn
dcpInterfaceTrxPostFecBerMantissa = _DcpInterfaceTrxPostFecBerMantissa_Object(
    (1, 3, 6, 1, 4, 1, 30826, 2, 2, 1, 3, 1, 1, 33),
    _DcpInterfaceTrxPostFecBerMantissa_Type()
)
dcpInterfaceTrxPostFecBerMantissa.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcpInterfaceTrxPostFecBerMantissa.setStatus("current")


class _DcpInterfaceTrxPostFecBerExponent_Type(Integer32):
    """Custom type dcpInterfaceTrxPostFecBerExponent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-30, 0),
    )


_DcpInterfaceTrxPostFecBerExponent_Type.__name__ = "Integer32"
_DcpInterfaceTrxPostFecBerExponent_Object = MibTableColumn
dcpInterfaceTrxPostFecBerExponent = _DcpInterfaceTrxPostFecBerExponent_Object(
    (1, 3, 6, 1, 4, 1, 30826, 2, 2, 1, 3, 1, 1, 34),
    _DcpInterfaceTrxPostFecBerExponent_Type()
)
dcpInterfaceTrxPostFecBerExponent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcpInterfaceTrxPostFecBerExponent.setStatus("current")
_DcpInterfaceTrxQvalue_Type = OpticalPower1Decimal
_DcpInterfaceTrxQvalue_Object = MibTableColumn
dcpInterfaceTrxQvalue = _DcpInterfaceTrxQvalue_Object(
    (1, 3, 6, 1, 4, 1, 30826, 2, 2, 1, 3, 1, 1, 35),
    _DcpInterfaceTrxQvalue_Type()
)
dcpInterfaceTrxQvalue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcpInterfaceTrxQvalue.setStatus("current")
_DcpInterfaceTrxQmargin_Type = OpticalPower1Decimal
_DcpInterfaceTrxQmargin_Object = MibTableColumn
dcpInterfaceTrxQmargin = _DcpInterfaceTrxQmargin_Object(
    (1, 3, 6, 1, 4, 1, 30826, 2, 2, 1, 3, 1, 1, 36),
    _DcpInterfaceTrxQmargin_Type()
)
dcpInterfaceTrxQmargin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcpInterfaceTrxQmargin.setStatus("current")
_DcpInterfaceTrxStateOfPolarizationROC_Type = Unsigned32
_DcpInterfaceTrxStateOfPolarizationROC_Object = MibTableColumn
dcpInterfaceTrxStateOfPolarizationROC = _DcpInterfaceTrxStateOfPolarizationROC_Object(
    (1, 3, 6, 1, 4, 1, 30826, 2, 2, 1, 3, 1, 1, 37),
    _DcpInterfaceTrxStateOfPolarizationROC_Type()
)
dcpInterfaceTrxStateOfPolarizationROC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcpInterfaceTrxStateOfPolarizationROC.setStatus("current")
_DcpInterfaceTrxLanesObjects_ObjectIdentity = ObjectIdentity
dcpInterfaceTrxLanesObjects = _DcpInterfaceTrxLanesObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30826, 2, 2, 1, 4)
)
_DcpInterfaceTrxLanesTable_Object = MibTable
dcpInterfaceTrxLanesTable = _DcpInterfaceTrxLanesTable_Object(
    (1, 3, 6, 1, 4, 1, 30826, 2, 2, 1, 4, 1)
)
if mibBuilder.loadTexts:
    dcpInterfaceTrxLanesTable.setStatus("current")
_DcpInterfaceTrxLanesEntry_Object = MibTableRow
dcpInterfaceTrxLanesEntry = _DcpInterfaceTrxLanesEntry_Object(
    (1, 3, 6, 1, 4, 1, 30826, 2, 2, 1, 4, 1, 1)
)
dcpInterfaceTrxLanesEntry.setIndexNames(
    (0, "DCP-INTERFACE-MIB", "dcpInterfaceTrxLanesIndex"),
)
if mibBuilder.loadTexts:
    dcpInterfaceTrxLanesEntry.setStatus("current")


class _DcpInterfaceTrxLanesIndex_Type(Unsigned32):
    """Custom type dcpInterfaceTrxLanesIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1000000),
    )


_DcpInterfaceTrxLanesIndex_Type.__name__ = "Unsigned32"
_DcpInterfaceTrxLanesIndex_Object = MibTableColumn
dcpInterfaceTrxLanesIndex = _DcpInterfaceTrxLanesIndex_Object(
    (1, 3, 6, 1, 4, 1, 30826, 2, 2, 1, 4, 1, 1, 1),
    _DcpInterfaceTrxLanesIndex_Type()
)
dcpInterfaceTrxLanesIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dcpInterfaceTrxLanesIndex.setStatus("current")
_DcpInterfaceTrxLanesName_Type = DisplayString
_DcpInterfaceTrxLanesName_Object = MibTableColumn
dcpInterfaceTrxLanesName = _DcpInterfaceTrxLanesName_Object(
    (1, 3, 6, 1, 4, 1, 30826, 2, 2, 1, 4, 1, 1, 2),
    _DcpInterfaceTrxLanesName_Type()
)
dcpInterfaceTrxLanesName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcpInterfaceTrxLanesName.setStatus("current")
_DcpInterfaceTrxLanesRxPower_Type = OpticalPower1Decimal
_DcpInterfaceTrxLanesRxPower_Object = MibTableColumn
dcpInterfaceTrxLanesRxPower = _DcpInterfaceTrxLanesRxPower_Object(
    (1, 3, 6, 1, 4, 1, 30826, 2, 2, 1, 4, 1, 1, 3),
    _DcpInterfaceTrxLanesRxPower_Type()
)
dcpInterfaceTrxLanesRxPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcpInterfaceTrxLanesRxPower.setStatus("current")
_DcpInterfaceTrxLanesTxPower_Type = OpticalPower1Decimal
_DcpInterfaceTrxLanesTxPower_Object = MibTableColumn
dcpInterfaceTrxLanesTxPower = _DcpInterfaceTrxLanesTxPower_Object(
    (1, 3, 6, 1, 4, 1, 30826, 2, 2, 1, 4, 1, 1, 4),
    _DcpInterfaceTrxLanesTxPower_Type()
)
dcpInterfaceTrxLanesTxPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcpInterfaceTrxLanesTxPower.setStatus("current")
_DcpInterfaceTrxLanesRxSensitivity_Type = OpticalPower1Decimal
_DcpInterfaceTrxLanesRxSensitivity_Object = MibTableColumn
dcpInterfaceTrxLanesRxSensitivity = _DcpInterfaceTrxLanesRxSensitivity_Object(
    (1, 3, 6, 1, 4, 1, 30826, 2, 2, 1, 4, 1, 1, 5),
    _DcpInterfaceTrxLanesRxSensitivity_Type()
)
dcpInterfaceTrxLanesRxSensitivity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcpInterfaceTrxLanesRxSensitivity.setStatus("current")
_DcpInterfaceTrxLanesTxBias_Type = OpticalPower1Decimal
_DcpInterfaceTrxLanesTxBias_Object = MibTableColumn
dcpInterfaceTrxLanesTxBias = _DcpInterfaceTrxLanesTxBias_Object(
    (1, 3, 6, 1, 4, 1, 30826, 2, 2, 1, 4, 1, 1, 6),
    _DcpInterfaceTrxLanesTxBias_Type()
)
dcpInterfaceTrxLanesTxBias.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcpInterfaceTrxLanesTxBias.setStatus("current")

# Managed Objects groups

dcpInterfaceTableGroupV1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 30826, 2, 2, 1, 2, 1, 1)
)
dcpInterfaceTableGroupV1.setObjects(
      *(("DCP-INTERFACE-MIB", "dcpInterfaceName"),
        ("DCP-INTERFACE-MIB", "dcpInterfaceRxPower"),
        ("DCP-INTERFACE-MIB", "dcpInterfaceTxPower"),
        ("DCP-INTERFACE-MIB", "dcpInterfaceStatus"),
        ("DCP-INTERFACE-MIB", "dcpInterfaceAlarm"),
        ("DCP-INTERFACE-MIB", "dcpInterfaceFormat"),
        ("DCP-INTERFACE-MIB", "dcpInterfaceChannelId"),
        ("DCP-INTERFACE-MIB", "dcpInterfaceWavelength"))
)
if mibBuilder.loadTexts:
    dcpInterfaceTableGroupV1.setStatus("deprecated")

dcpInterfaceTableGroupV2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 30826, 2, 2, 1, 2, 1, 2)
)
dcpInterfaceTableGroupV2.setObjects(
      *(("DCP-INTERFACE-MIB", "dcpInterfaceName"),
        ("DCP-INTERFACE-MIB", "dcpInterfaceRxPower"),
        ("DCP-INTERFACE-MIB", "dcpInterfaceTxPower"),
        ("DCP-INTERFACE-MIB", "dcpInterfaceStatus"),
        ("DCP-INTERFACE-MIB", "dcpInterfaceAlarm"),
        ("DCP-INTERFACE-MIB", "dcpInterfaceFormat"),
        ("DCP-INTERFACE-MIB", "dcpInterfaceChannelId"),
        ("DCP-INTERFACE-MIB", "dcpInterfaceWavelength"),
        ("DCP-INTERFACE-MIB", "dcpInterfaceDescription"))
)
if mibBuilder.loadTexts:
    dcpInterfaceTableGroupV2.setStatus("current")

dcpInterfaceTableGroupV3 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 30826, 2, 2, 1, 2, 1, 3)
)
dcpInterfaceTableGroupV3.setObjects(
      *(("DCP-INTERFACE-MIB", "dcpInterfaceName"),
        ("DCP-INTERFACE-MIB", "dcpInterfaceRxPower"),
        ("DCP-INTERFACE-MIB", "dcpInterfaceTxPower"),
        ("DCP-INTERFACE-MIB", "dcpInterfaceStatus"),
        ("DCP-INTERFACE-MIB", "dcpInterfaceAlarm"),
        ("DCP-INTERFACE-MIB", "dcpInterfaceFormat"),
        ("DCP-INTERFACE-MIB", "dcpInterfaceChannelId"),
        ("DCP-INTERFACE-MIB", "dcpInterfaceWavelength"),
        ("DCP-INTERFACE-MIB", "dcpInterfaceDescription"),
        ("DCP-INTERFACE-MIB", "dcpInterfacePortType"),
        ("DCP-INTERFACE-MIB", "dcpInterfacePortMode"))
)
if mibBuilder.loadTexts:
    dcpInterfaceTableGroupV3.setStatus("current")

dcpInterfaceTrxTableGroupV1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 30826, 2, 2, 1, 2, 3, 1)
)
dcpInterfaceTrxTableGroupV1.setObjects(
      *(("DCP-INTERFACE-MIB", "dcpInterfaceTrxName"),
        ("DCP-INTERFACE-MIB", "dcpInterfaceTrxName"),
        ("DCP-INTERFACE-MIB", "dcpInterfaceTrxLanes"),
        ("DCP-INTERFACE-MIB", "dcpInterfaceTrxTemperature"),
        ("DCP-INTERFACE-MIB", "dcpInterfaceTrxTemperatureHighWarningThreshold"),
        ("DCP-INTERFACE-MIB", "dcpInterfaceTrxTemperatureHighAlarmThreshold"),
        ("DCP-INTERFACE-MIB", "dcpInterfaceTrxWavelength"),
        ("DCP-INTERFACE-MIB", "dcpInterfaceTrxChannelId"),
        ("DCP-INTERFACE-MIB", "dcpInterfaceTrxActualFrequency"),
        ("DCP-INTERFACE-MIB", "dcpInterfaceTrxWantedFrequency"),
        ("DCP-INTERFACE-MIB", "dcpInterfaceTrxGridSpacing"),
        ("DCP-INTERFACE-MIB", "dcpInterfaceTrxTotalRxPower"),
        ("DCP-INTERFACE-MIB", "dcpInterfaceTrxSignalRxPower"),
        ("DCP-INTERFACE-MIB", "dcpInterfaceTrxTxPower"),
        ("DCP-INTERFACE-MIB", "dcpInterfaceTrxTxBias"),
        ("DCP-INTERFACE-MIB", "dcpInterfaceTrxRxSensitivity"),
        ("DCP-INTERFACE-MIB", "dcpInterfaceTrxRxLosThreshold"),
        ("DCP-INTERFACE-MIB", "dcpInterfaceTrxModulationType"),
        ("DCP-INTERFACE-MIB", "dcpInterfaceTrxBandwidth"),
        ("DCP-INTERFACE-MIB", "dcpInterfaceTrxFec"),
        ("DCP-INTERFACE-MIB", "dcpInterfaceTrxPulseShaping"),
        ("DCP-INTERFACE-MIB", "dcpInterfaceTrxCertified"),
        ("DCP-INTERFACE-MIB", "dcpInterfaceTrxOsnr"),
        ("DCP-INTERFACE-MIB", "dcpInterfaceTrxChromaticDispersion"),
        ("DCP-INTERFACE-MIB", "dcpInterfaceTrxDiffGroupDelay"),
        ("DCP-INTERFACE-MIB", "dcpInterfaceTrxPolarizationDependentLoss"),
        ("DCP-INTERFACE-MIB", "dcpInterfaceTrxPreFecBerMantissa"),
        ("DCP-INTERFACE-MIB", "dcpInterfaceTrxPreFecBerExponent"),
        ("DCP-INTERFACE-MIB", "dcpInterfaceTrxPreFecBerAvgMantissa"),
        ("DCP-INTERFACE-MIB", "dcpInterfaceTrxPreFecBerAvgExponent"),
        ("DCP-INTERFACE-MIB", "dcpInterfaceTrxUncorrectedBerMantissa"),
        ("DCP-INTERFACE-MIB", "dcpInterfaceTrxUncorrectedBerExponent"),
        ("DCP-INTERFACE-MIB", "dcpInterfaceTrxPostFecBerMantissa"),
        ("DCP-INTERFACE-MIB", "dcpInterfaceTrxPostFecBerExponent"),
        ("DCP-INTERFACE-MIB", "dcpInterfaceTrxQvalue"),
        ("DCP-INTERFACE-MIB", "dcpInterfaceTrxQmargin"))
)
if mibBuilder.loadTexts:
    dcpInterfaceTrxTableGroupV1.setStatus("current")

dcpInterfaceTrxTableGroupV2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 30826, 2, 2, 1, 2, 3, 2)
)
dcpInterfaceTrxTableGroupV2.setObjects(
      *(("DCP-INTERFACE-MIB", "dcpInterfaceTrxName"),
        ("DCP-INTERFACE-MIB", "dcpInterfaceTrxName"),
        ("DCP-INTERFACE-MIB", "dcpInterfaceTrxLanes"),
        ("DCP-INTERFACE-MIB", "dcpInterfaceTrxTemperature"),
        ("DCP-INTERFACE-MIB", "dcpInterfaceTrxTemperatureHighWarningThreshold"),
        ("DCP-INTERFACE-MIB", "dcpInterfaceTrxTemperatureHighAlarmThreshold"),
        ("DCP-INTERFACE-MIB", "dcpInterfaceTrxWavelength"),
        ("DCP-INTERFACE-MIB", "dcpInterfaceTrxChannelId"),
        ("DCP-INTERFACE-MIB", "dcpInterfaceTrxActualFrequency"),
        ("DCP-INTERFACE-MIB", "dcpInterfaceTrxWantedFrequency"),
        ("DCP-INTERFACE-MIB", "dcpInterfaceTrxGridSpacing"),
        ("DCP-INTERFACE-MIB", "dcpInterfaceTrxTotalRxPower"),
        ("DCP-INTERFACE-MIB", "dcpInterfaceTrxSignalRxPower"),
        ("DCP-INTERFACE-MIB", "dcpInterfaceTrxTxPower"),
        ("DCP-INTERFACE-MIB", "dcpInterfaceTrxTxBias"),
        ("DCP-INTERFACE-MIB", "dcpInterfaceTrxRxSensitivity"),
        ("DCP-INTERFACE-MIB", "dcpInterfaceTrxRxLosThreshold"),
        ("DCP-INTERFACE-MIB", "dcpInterfaceTrxModulationType"),
        ("DCP-INTERFACE-MIB", "dcpInterfaceTrxBandwidth"),
        ("DCP-INTERFACE-MIB", "dcpInterfaceTrxFec"),
        ("DCP-INTERFACE-MIB", "dcpInterfaceTrxPulseShaping"),
        ("DCP-INTERFACE-MIB", "dcpInterfaceTrxCertified"),
        ("DCP-INTERFACE-MIB", "dcpInterfaceTrxOsnr"),
        ("DCP-INTERFACE-MIB", "dcpInterfaceTrxChromaticDispersion"),
        ("DCP-INTERFACE-MIB", "dcpInterfaceTrxDiffGroupDelay"),
        ("DCP-INTERFACE-MIB", "dcpInterfaceTrxPolarizationDependentLoss"),
        ("DCP-INTERFACE-MIB", "dcpInterfaceTrxPreFecBerMantissa"),
        ("DCP-INTERFACE-MIB", "dcpInterfaceTrxPreFecBerExponent"),
        ("DCP-INTERFACE-MIB", "dcpInterfaceTrxPreFecBerAvgMantissa"),
        ("DCP-INTERFACE-MIB", "dcpInterfaceTrxPreFecBerAvgExponent"),
        ("DCP-INTERFACE-MIB", "dcpInterfaceTrxUncorrectedBerMantissa"),
        ("DCP-INTERFACE-MIB", "dcpInterfaceTrxUncorrectedBerExponent"),
        ("DCP-INTERFACE-MIB", "dcpInterfaceTrxPostFecBerMantissa"),
        ("DCP-INTERFACE-MIB", "dcpInterfaceTrxPostFecBerExponent"),
        ("DCP-INTERFACE-MIB", "dcpInterfaceTrxQvalue"),
        ("DCP-INTERFACE-MIB", "dcpInterfaceTrxQmargin"),
        ("DCP-INTERFACE-MIB", "dcpInterfaceTrxStateOfPolarizationROC"))
)
if mibBuilder.loadTexts:
    dcpInterfaceTrxTableGroupV2.setStatus("current")

dcpInterfaceTrxLanesTableGroupV1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 30826, 2, 2, 1, 2, 4, 1)
)
dcpInterfaceTrxLanesTableGroupV1.setObjects(
      *(("DCP-INTERFACE-MIB", "dcpInterfaceTrxLanesName"),
        ("DCP-INTERFACE-MIB", "dcpInterfaceTrxLanesRxPower"),
        ("DCP-INTERFACE-MIB", "dcpInterfaceTrxLanesTxPower"),
        ("DCP-INTERFACE-MIB", "dcpInterfaceTrxLanesRxSensitivity"),
        ("DCP-INTERFACE-MIB", "dcpInterfaceTrxLanesTxBias"))
)
if mibBuilder.loadTexts:
    dcpInterfaceTrxLanesTableGroupV1.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

dcpInterfaceBasicComplV1 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 30826, 2, 2, 1, 2, 2, 1)
)
dcpInterfaceBasicComplV1.setObjects(
    ("DCP-INTERFACE-MIB", "dcpInterfaceTableGroupV1")
)
if mibBuilder.loadTexts:
    dcpInterfaceBasicComplV1.setStatus(
        "deprecated"
    )

dcpInterfaceBasicComplV2 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 30826, 2, 2, 1, 2, 2, 2)
)
dcpInterfaceBasicComplV2.setObjects(
    ("DCP-INTERFACE-MIB", "dcpInterfaceTableGroupV2")
)
if mibBuilder.loadTexts:
    dcpInterfaceBasicComplV2.setStatus(
        "deprecated"
    )

dcpInterfaceBasicComplV3 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 30826, 2, 2, 1, 2, 2, 3)
)
dcpInterfaceBasicComplV3.setObjects(
    ("DCP-INTERFACE-MIB", "dcpInterfaceTableGroupV3")
)
if mibBuilder.loadTexts:
    dcpInterfaceBasicComplV3.setStatus(
        "current"
    )

dcpInterfaceBasicComplV4 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 30826, 2, 2, 1, 2, 2, 4)
)
dcpInterfaceBasicComplV4.setObjects(
      *(("DCP-INTERFACE-MIB", "dcpInterfaceTableGroupV3"),
        ("DCP-INTERFACE-MIB", "dcpInterfaceTrxTableGroupV1"),
        ("DCP-INTERFACE-MIB", "dcpInterfaceTrxLanesTableGroupV1"))
)
if mibBuilder.loadTexts:
    dcpInterfaceBasicComplV4.setStatus(
        "current"
    )

dcpInterfaceBasicComplV5 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 30826, 2, 2, 1, 2, 2, 5)
)
dcpInterfaceBasicComplV5.setObjects(
      *(("DCP-INTERFACE-MIB", "dcpInterfaceTableGroupV3"),
        ("DCP-INTERFACE-MIB", "dcpInterfaceTrxTableGroupV2"),
        ("DCP-INTERFACE-MIB", "dcpInterfaceTrxLanesTableGroupV1"))
)
if mibBuilder.loadTexts:
    dcpInterfaceBasicComplV5.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "DCP-INTERFACE-MIB",
    **{"dcpInterface": dcpInterface,
       "dcpInterfaceObjects": dcpInterfaceObjects,
       "dcpInterfaceTable": dcpInterfaceTable,
       "dcpInterfaceEntry": dcpInterfaceEntry,
       "dcpInterfaceIndex": dcpInterfaceIndex,
       "dcpInterfaceName": dcpInterfaceName,
       "dcpInterfaceRxPower": dcpInterfaceRxPower,
       "dcpInterfaceTxPower": dcpInterfaceTxPower,
       "dcpInterfaceStatus": dcpInterfaceStatus,
       "dcpInterfaceAlarm": dcpInterfaceAlarm,
       "dcpInterfaceFormat": dcpInterfaceFormat,
       "dcpInterfaceWavelength": dcpInterfaceWavelength,
       "dcpInterfaceChannelId": dcpInterfaceChannelId,
       "dcpInterfaceDescription": dcpInterfaceDescription,
       "dcpInterfacePortType": dcpInterfacePortType,
       "dcpInterfacePortMode": dcpInterfacePortMode,
       "dcpInterfaceMIBCompliance": dcpInterfaceMIBCompliance,
       "dcpInterfaceMIBGroups": dcpInterfaceMIBGroups,
       "dcpInterfaceTableGroupV1": dcpInterfaceTableGroupV1,
       "dcpInterfaceTableGroupV2": dcpInterfaceTableGroupV2,
       "dcpInterfaceTableGroupV3": dcpInterfaceTableGroupV3,
       "dcpInterfaceMIBCompliances": dcpInterfaceMIBCompliances,
       "dcpInterfaceBasicComplV1": dcpInterfaceBasicComplV1,
       "dcpInterfaceBasicComplV2": dcpInterfaceBasicComplV2,
       "dcpInterfaceBasicComplV3": dcpInterfaceBasicComplV3,
       "dcpInterfaceBasicComplV4": dcpInterfaceBasicComplV4,
       "dcpInterfaceBasicComplV5": dcpInterfaceBasicComplV5,
       "dcpInterfaceTrxMIBGroups": dcpInterfaceTrxMIBGroups,
       "dcpInterfaceTrxTableGroupV1": dcpInterfaceTrxTableGroupV1,
       "dcpInterfaceTrxTableGroupV2": dcpInterfaceTrxTableGroupV2,
       "dcpInterfaceTrxLanesMIBGroups": dcpInterfaceTrxLanesMIBGroups,
       "dcpInterfaceTrxLanesTableGroupV1": dcpInterfaceTrxLanesTableGroupV1,
       "dcpInterfaceTrxObjects": dcpInterfaceTrxObjects,
       "dcpInterfaceTrxTable": dcpInterfaceTrxTable,
       "dcpInterfaceTrxEntry": dcpInterfaceTrxEntry,
       "dcpInterfaceTrxIndex": dcpInterfaceTrxIndex,
       "dcpInterfaceTrxName": dcpInterfaceTrxName,
       "dcpInterfaceTrxLanes": dcpInterfaceTrxLanes,
       "dcpInterfaceTrxTemperature": dcpInterfaceTrxTemperature,
       "dcpInterfaceTrxTemperatureHighWarningThreshold": dcpInterfaceTrxTemperatureHighWarningThreshold,
       "dcpInterfaceTrxTemperatureHighAlarmThreshold": dcpInterfaceTrxTemperatureHighAlarmThreshold,
       "dcpInterfaceTrxWavelength": dcpInterfaceTrxWavelength,
       "dcpInterfaceTrxChannelId": dcpInterfaceTrxChannelId,
       "dcpInterfaceTrxActualFrequency": dcpInterfaceTrxActualFrequency,
       "dcpInterfaceTrxWantedFrequency": dcpInterfaceTrxWantedFrequency,
       "dcpInterfaceTrxGridSpacing": dcpInterfaceTrxGridSpacing,
       "dcpInterfaceTrxTotalRxPower": dcpInterfaceTrxTotalRxPower,
       "dcpInterfaceTrxSignalRxPower": dcpInterfaceTrxSignalRxPower,
       "dcpInterfaceTrxTxPower": dcpInterfaceTrxTxPower,
       "dcpInterfaceTrxTxBias": dcpInterfaceTrxTxBias,
       "dcpInterfaceTrxRxSensitivity": dcpInterfaceTrxRxSensitivity,
       "dcpInterfaceTrxRxLosThreshold": dcpInterfaceTrxRxLosThreshold,
       "dcpInterfaceTrxModulationType": dcpInterfaceTrxModulationType,
       "dcpInterfaceTrxBandwidth": dcpInterfaceTrxBandwidth,
       "dcpInterfaceTrxFec": dcpInterfaceTrxFec,
       "dcpInterfaceTrxPulseShaping": dcpInterfaceTrxPulseShaping,
       "dcpInterfaceTrxCertified": dcpInterfaceTrxCertified,
       "dcpInterfaceTrxOsnr": dcpInterfaceTrxOsnr,
       "dcpInterfaceTrxChromaticDispersion": dcpInterfaceTrxChromaticDispersion,
       "dcpInterfaceTrxDiffGroupDelay": dcpInterfaceTrxDiffGroupDelay,
       "dcpInterfaceTrxPolarizationDependentLoss": dcpInterfaceTrxPolarizationDependentLoss,
       "dcpInterfaceTrxPreFecBerMantissa": dcpInterfaceTrxPreFecBerMantissa,
       "dcpInterfaceTrxPreFecBerExponent": dcpInterfaceTrxPreFecBerExponent,
       "dcpInterfaceTrxPreFecBerAvgMantissa": dcpInterfaceTrxPreFecBerAvgMantissa,
       "dcpInterfaceTrxPreFecBerAvgExponent": dcpInterfaceTrxPreFecBerAvgExponent,
       "dcpInterfaceTrxUncorrectedBerMantissa": dcpInterfaceTrxUncorrectedBerMantissa,
       "dcpInterfaceTrxUncorrectedBerExponent": dcpInterfaceTrxUncorrectedBerExponent,
       "dcpInterfaceTrxPostFecBerMantissa": dcpInterfaceTrxPostFecBerMantissa,
       "dcpInterfaceTrxPostFecBerExponent": dcpInterfaceTrxPostFecBerExponent,
       "dcpInterfaceTrxQvalue": dcpInterfaceTrxQvalue,
       "dcpInterfaceTrxQmargin": dcpInterfaceTrxQmargin,
       "dcpInterfaceTrxStateOfPolarizationROC": dcpInterfaceTrxStateOfPolarizationROC,
       "dcpInterfaceTrxLanesObjects": dcpInterfaceTrxLanesObjects,
       "dcpInterfaceTrxLanesTable": dcpInterfaceTrxLanesTable,
       "dcpInterfaceTrxLanesEntry": dcpInterfaceTrxLanesEntry,
       "dcpInterfaceTrxLanesIndex": dcpInterfaceTrxLanesIndex,
       "dcpInterfaceTrxLanesName": dcpInterfaceTrxLanesName,
       "dcpInterfaceTrxLanesRxPower": dcpInterfaceTrxLanesRxPower,
       "dcpInterfaceTrxLanesTxPower": dcpInterfaceTrxLanesTxPower,
       "dcpInterfaceTrxLanesRxSensitivity": dcpInterfaceTrxLanesRxSensitivity,
       "dcpInterfaceTrxLanesTxBias": dcpInterfaceTrxLanesTxBias}
)
