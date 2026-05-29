# SNMP MIB module (SPEEDSINGLELINE-XFP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\pandacom\SPEEDSINGLELINE-XFP-MIB

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

(converter,) = mibBuilder.importSymbols(
    "SPEEDCARRIER-MIB",
    "converter")


# MODULE-IDENTITY

convSpeedSingleLineXFP = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 3652, 3, 3, 2)
)
if mibBuilder.loadTexts:
    convSpeedSingleLineXFP.setRevisions(
        ("2019-04-25 00:00",
         "2017-12-11 00:00",
         "2013-12-12 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_ConvSSLXFPModuleOverviewTable_Object = MibTable
convSSLXFPModuleOverviewTable = _ConvSSLXFPModuleOverviewTable_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 3, 2, 1)
)
if mibBuilder.loadTexts:
    convSSLXFPModuleOverviewTable.setStatus("current")
_ConvSSLXFPModuleOverviewEntry_Object = MibTableRow
convSSLXFPModuleOverviewEntry = _ConvSSLXFPModuleOverviewEntry_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 3, 2, 1, 1)
)
convSSLXFPModuleOverviewEntry.setIndexNames(
    (0, "SPEEDSINGLELINE-XFP-MIB", "convSSLXFPMSlot"),
)
if mibBuilder.loadTexts:
    convSSLXFPModuleOverviewEntry.setStatus("current")


class _ConvSSLXFPMSlot_Type(Integer32):
    """Custom type convSSLXFPMSlot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 19),
    )


_ConvSSLXFPMSlot_Type.__name__ = "Integer32"
_ConvSSLXFPMSlot_Object = MibTableColumn
convSSLXFPMSlot = _ConvSSLXFPMSlot_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 3, 2, 1, 1, 2),
    _ConvSSLXFPMSlot_Type()
)
convSSLXFPMSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    convSSLXFPMSlot.setStatus("current")


class _ConvSSLXFPMDevice_Type(Integer32):
    """Custom type convSSLXFPMDevice based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(4,
              5,
              255)
        )
    )
    namedValues = NamedValues(
        *(("devSpeedSingleLineXFP3R", 4),
          ("devSpeedSingleLineXFP", 5),
          ("devunknown", 255))
    )


_ConvSSLXFPMDevice_Type.__name__ = "Integer32"
_ConvSSLXFPMDevice_Object = MibTableColumn
convSSLXFPMDevice = _ConvSSLXFPMDevice_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 3, 2, 1, 1, 3),
    _ConvSSLXFPMDevice_Type()
)
convSSLXFPMDevice.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    convSSLXFPMDevice.setStatus("current")


class _ConvSSLXFPMStatus_Type(Integer32):
    """Custom type convSSLXFPMStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              255)
        )
    )
    namedValues = NamedValues(
        *(("running", 0),
          ("resetSoftware", 1),
          ("resetConfig", 2),
          ("resetCAN", 3),
          ("resetHardware", 4),
          ("unknown", 255))
    )


_ConvSSLXFPMStatus_Type.__name__ = "Integer32"
_ConvSSLXFPMStatus_Object = MibTableColumn
convSSLXFPMStatus = _ConvSSLXFPMStatus_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 3, 2, 1, 1, 4),
    _ConvSSLXFPMStatus_Type()
)
convSSLXFPMStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    convSSLXFPMStatus.setStatus("current")
_ConvSSLXFPMSysUpTime_Type = TimeTicks
_ConvSSLXFPMSysUpTime_Object = MibTableColumn
convSSLXFPMSysUpTime = _ConvSSLXFPMSysUpTime_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 3, 2, 1, 1, 5),
    _ConvSSLXFPMSysUpTime_Type()
)
convSSLXFPMSysUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    convSSLXFPMSysUpTime.setStatus("current")
_ConvSSLXFPMTemp_Type = Integer32
_ConvSSLXFPMTemp_Object = MibTableColumn
convSSLXFPMTemp = _ConvSSLXFPMTemp_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 3, 2, 1, 1, 6),
    _ConvSSLXFPMTemp_Type()
)
convSSLXFPMTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    convSSLXFPMTemp.setStatus("current")


class _ConvSSLXFPMAlarmState_Type(Integer32):
    """Custom type convSSLXFPMAlarmState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              32,
              33,
              34,
              35,
              36,
              37,
              38,
              39,
              64,
              65,
              66,
              67,
              68,
              69,
              70,
              71,
              96,
              97,
              98,
              99,
              100,
              101,
              102,
              103,
              255)
        )
    )
    namedValues = NamedValues(
        *(("noAlarm", 0),
          ("activeAlarmsH1", 1),
          ("cdrAlarmRxP1", 2),
          ("activeAlarmsH3", 3),
          ("cdrAlarmTxP1", 4),
          ("activeAlarmsH5", 5),
          ("cdrAlarmRxP1TxP1", 6),
          ("activeAlarmsH7", 7),
          ("cdrAlarmRxP2", 32),
          ("activeAlarmsH33", 33),
          ("cdrAlarmRxP2RxP1", 34),
          ("activeAlarmsH35", 35),
          ("cdrAlarmRxP2TxP1", 36),
          ("activeAlarmsH37", 37),
          ("cdrAlarmRxP2RxP1TxP1", 38),
          ("activeAlarmsH39", 39),
          ("cdrAlarmTxP2", 64),
          ("activeAlarmsH65", 65),
          ("cdrAlarmTxP2RxP1", 66),
          ("activeAlarmsH67", 67),
          ("cdrAlarmTxP2TxP1", 68),
          ("activeAlarmsH69", 69),
          ("cdrAlarmTxP2RxP1TxP1", 70),
          ("activeAlarmsH71", 71),
          ("cdrAlarmRxP2TxP2", 96),
          ("activeAlarmsH97", 97),
          ("cdrAlarmRxP2TxP2RxP1", 98),
          ("activeAlarmsH99", 99),
          ("cdrAlarmRxP2TxP2TxP1", 100),
          ("activeAlarmsH101", 101),
          ("cdrAlarmRxP2TxP2RxP1TxP1", 102),
          ("activeAlarmsH103", 103),
          ("unknown", 255))
    )


_ConvSSLXFPMAlarmState_Type.__name__ = "Integer32"
_ConvSSLXFPMAlarmState_Object = MibTableColumn
convSSLXFPMAlarmState = _ConvSSLXFPMAlarmState_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 3, 2, 1, 1, 7),
    _ConvSSLXFPMAlarmState_Type()
)
convSSLXFPMAlarmState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    convSSLXFPMAlarmState.setStatus("current")


class _ConvSSLXFPMSerialNumber_Type(DisplayString):
    """Custom type convSSLXFPMSerialNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 19),
    )


_ConvSSLXFPMSerialNumber_Type.__name__ = "DisplayString"
_ConvSSLXFPMSerialNumber_Object = MibTableColumn
convSSLXFPMSerialNumber = _ConvSSLXFPMSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 3, 2, 1, 1, 8),
    _ConvSSLXFPMSerialNumber_Type()
)
convSSLXFPMSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    convSSLXFPMSerialNumber.setStatus("current")
_ConvSSLXFPModuleImagesOverviewTable_Object = MibTable
convSSLXFPModuleImagesOverviewTable = _ConvSSLXFPModuleImagesOverviewTable_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 3, 2, 2)
)
if mibBuilder.loadTexts:
    convSSLXFPModuleImagesOverviewTable.setStatus("current")
_ConvSSLXFPModuleImagesOverviewEntry_Object = MibTableRow
convSSLXFPModuleImagesOverviewEntry = _ConvSSLXFPModuleImagesOverviewEntry_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 3, 2, 2, 1)
)
convSSLXFPModuleImagesOverviewEntry.setIndexNames(
    (0, "SPEEDSINGLELINE-XFP-MIB", "convSSLXFPSWSlot"),
)
if mibBuilder.loadTexts:
    convSSLXFPModuleImagesOverviewEntry.setStatus("current")


class _ConvSSLXFPSWSlot_Type(Integer32):
    """Custom type convSSLXFPSWSlot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 19),
    )


_ConvSSLXFPSWSlot_Type.__name__ = "Integer32"
_ConvSSLXFPSWSlot_Object = MibTableColumn
convSSLXFPSWSlot = _ConvSSLXFPSWSlot_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 3, 2, 2, 1, 2),
    _ConvSSLXFPSWSlot_Type()
)
convSSLXFPSWSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    convSSLXFPSWSlot.setStatus("current")


class _ConvSSLXFPSWBootImage_Type(DisplayString):
    """Custom type convSSLXFPSWBootImage based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 36),
    )


_ConvSSLXFPSWBootImage_Type.__name__ = "DisplayString"
_ConvSSLXFPSWBootImage_Object = MibTableColumn
convSSLXFPSWBootImage = _ConvSSLXFPSWBootImage_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 3, 2, 2, 1, 3),
    _ConvSSLXFPSWBootImage_Type()
)
convSSLXFPSWBootImage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    convSSLXFPSWBootImage.setStatus("current")


class _ConvSSLXFPSWAppImage1_Type(DisplayString):
    """Custom type convSSLXFPSWAppImage1 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 36),
    )


_ConvSSLXFPSWAppImage1_Type.__name__ = "DisplayString"
_ConvSSLXFPSWAppImage1_Object = MibTableColumn
convSSLXFPSWAppImage1 = _ConvSSLXFPSWAppImage1_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 3, 2, 2, 1, 4),
    _ConvSSLXFPSWAppImage1_Type()
)
convSSLXFPSWAppImage1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    convSSLXFPSWAppImage1.setStatus("current")


class _ConvSSLXFPSWAppImage2_Type(DisplayString):
    """Custom type convSSLXFPSWAppImage2 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 36),
    )


_ConvSSLXFPSWAppImage2_Type.__name__ = "DisplayString"
_ConvSSLXFPSWAppImage2_Object = MibTableColumn
convSSLXFPSWAppImage2 = _ConvSSLXFPSWAppImage2_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 3, 2, 2, 1, 5),
    _ConvSSLXFPSWAppImage2_Type()
)
convSSLXFPSWAppImage2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    convSSLXFPSWAppImage2.setStatus("current")


class _ConvSSLXFPSWUploadStatus_Type(Integer32):
    """Custom type convSSLXFPSWUploadStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              255)
        )
    )
    namedValues = NamedValues(
        *(("ready", 0),
          ("startUpload", 1),
          ("uploadActive", 2),
          ("uploadFailure", 3),
          ("notAvailable", 255))
    )


_ConvSSLXFPSWUploadStatus_Type.__name__ = "Integer32"
_ConvSSLXFPSWUploadStatus_Object = MibTableColumn
convSSLXFPSWUploadStatus = _ConvSSLXFPSWUploadStatus_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 3, 2, 2, 1, 6),
    _ConvSSLXFPSWUploadStatus_Type()
)
convSSLXFPSWUploadStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    convSSLXFPSWUploadStatus.setStatus("current")


class _ConvSSLXFPSWUpdateStatus_Type(Integer32):
    """Custom type convSSLXFPSWUpdateStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("idle", 0),
          ("activateImage1", 1),
          ("activateImage2", 2),
          ("notAvailable", 255))
    )


_ConvSSLXFPSWUpdateStatus_Type.__name__ = "Integer32"
_ConvSSLXFPSWUpdateStatus_Object = MibTableColumn
convSSLXFPSWUpdateStatus = _ConvSSLXFPSWUpdateStatus_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 3, 2, 2, 1, 7),
    _ConvSSLXFPSWUpdateStatus_Type()
)
convSSLXFPSWUpdateStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    convSSLXFPSWUpdateStatus.setStatus("current")


class _ConvSSLXFPMHWVersion_Type(DisplayString):
    """Custom type convSSLXFPMHWVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 36),
    )


_ConvSSLXFPMHWVersion_Type.__name__ = "DisplayString"
_ConvSSLXFPMHWVersion_Object = MibTableColumn
convSSLXFPMHWVersion = _ConvSSLXFPMHWVersion_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 3, 2, 2, 1, 8),
    _ConvSSLXFPMHWVersion_Type()
)
convSSLXFPMHWVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    convSSLXFPMHWVersion.setStatus("current")
_ConvSSLXFPModuleBoardConfigTable_Object = MibTable
convSSLXFPModuleBoardConfigTable = _ConvSSLXFPModuleBoardConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 3, 2, 3)
)
if mibBuilder.loadTexts:
    convSSLXFPModuleBoardConfigTable.setStatus("current")
_ConvSSLXFPModuleBoardConfigEntry_Object = MibTableRow
convSSLXFPModuleBoardConfigEntry = _ConvSSLXFPModuleBoardConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 3, 2, 3, 1)
)
convSSLXFPModuleBoardConfigEntry.setIndexNames(
    (0, "SPEEDSINGLELINE-XFP-MIB", "convSSLXFPModuleSlot"),
)
if mibBuilder.loadTexts:
    convSSLXFPModuleBoardConfigEntry.setStatus("current")


class _ConvSSLXFPModuleSlot_Type(Integer32):
    """Custom type convSSLXFPModuleSlot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 19),
    )


_ConvSSLXFPModuleSlot_Type.__name__ = "Integer32"
_ConvSSLXFPModuleSlot_Object = MibTableColumn
convSSLXFPModuleSlot = _ConvSSLXFPModuleSlot_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 3, 2, 3, 1, 2),
    _ConvSSLXFPModuleSlot_Type()
)
convSSLXFPModuleSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    convSSLXFPModuleSlot.setStatus("current")


class _ConvSSLXFPModulePortSpeedConfig_Type(Integer32):
    """Custom type convSSLXFPModulePortSpeedConfig based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              255)
        )
    )
    namedValues = NamedValues(
        *(("stm64", 0),
          ("stm64rs238", 1),
          ("stm64rs237", 2),
          ("ethernet10g64b66b", 3),
          ("ethernet10g237RS", 4),
          ("ethernet10g238RS", 5),
          ("fibreChannel10G64B66B", 6),
          ("fibreChannel10G237RS", 7),
          ("fibreChannel10G238RS", 8),
          ("notAvalilable", 255))
    )


_ConvSSLXFPModulePortSpeedConfig_Type.__name__ = "Integer32"
_ConvSSLXFPModulePortSpeedConfig_Object = MibTableColumn
convSSLXFPModulePortSpeedConfig = _ConvSSLXFPModulePortSpeedConfig_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 3, 2, 3, 1, 3),
    _ConvSSLXFPModulePortSpeedConfig_Type()
)
convSSLXFPModulePortSpeedConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    convSSLXFPModulePortSpeedConfig.setStatus("current")


class _ConvSSLXFPModuleTempHighWarning_Type(Integer32):
    """Custom type convSSLXFPModuleTempHighWarning based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            0
        )
    )
    namedValues = NamedValues(
        ("notImplemented", 0)
    )


_ConvSSLXFPModuleTempHighWarning_Type.__name__ = "Integer32"
_ConvSSLXFPModuleTempHighWarning_Object = MibTableColumn
convSSLXFPModuleTempHighWarning = _ConvSSLXFPModuleTempHighWarning_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 3, 2, 3, 1, 4),
    _ConvSSLXFPModuleTempHighWarning_Type()
)
convSSLXFPModuleTempHighWarning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    convSSLXFPModuleTempHighWarning.setStatus("current")


class _ConvSSLXFPModuleTempHighAlarm_Type(Integer32):
    """Custom type convSSLXFPModuleTempHighAlarm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            0
        )
    )
    namedValues = NamedValues(
        ("notAvalilable", 0)
    )


_ConvSSLXFPModuleTempHighAlarm_Type.__name__ = "Integer32"
_ConvSSLXFPModuleTempHighAlarm_Object = MibTableColumn
convSSLXFPModuleTempHighAlarm = _ConvSSLXFPModuleTempHighAlarm_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 3, 2, 3, 1, 5),
    _ConvSSLXFPModuleTempHighAlarm_Type()
)
convSSLXFPModuleTempHighAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    convSSLXFPModuleTempHighAlarm.setStatus("current")


class _ConvSSLXFPModuleCliTimeout_Type(Integer32):
    """Custom type convSSLXFPModuleCliTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(120, 3600),
    )


_ConvSSLXFPModuleCliTimeout_Type.__name__ = "Integer32"
_ConvSSLXFPModuleCliTimeout_Object = MibTableColumn
convSSLXFPModuleCliTimeout = _ConvSSLXFPModuleCliTimeout_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 3, 2, 3, 1, 6),
    _ConvSSLXFPModuleCliTimeout_Type()
)
convSSLXFPModuleCliTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    convSSLXFPModuleCliTimeout.setStatus("current")


class _ConvSSLXFPModuleEthPortConfig_Type(Integer32):
    """Custom type convSSLXFPModuleEthPortConfig based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notAvalilable", 0),
          ("portDown", 1),
          ("portUp", 2))
    )


_ConvSSLXFPModuleEthPortConfig_Type.__name__ = "Integer32"
_ConvSSLXFPModuleEthPortConfig_Object = MibTableColumn
convSSLXFPModuleEthPortConfig = _ConvSSLXFPModuleEthPortConfig_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 3, 2, 3, 1, 7),
    _ConvSSLXFPModuleEthPortConfig_Type()
)
convSSLXFPModuleEthPortConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    convSSLXFPModuleEthPortConfig.setStatus("current")


class _ConvSSLXFPModuleEthPortState_Type(Integer32):
    """Custom type convSSLXFPModuleEthPortState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notAvalilable", 0),
          ("portDown", 1),
          ("portUp", 2))
    )


_ConvSSLXFPModuleEthPortState_Type.__name__ = "Integer32"
_ConvSSLXFPModuleEthPortState_Object = MibTableColumn
convSSLXFPModuleEthPortState = _ConvSSLXFPModuleEthPortState_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 3, 2, 3, 1, 8),
    _ConvSSLXFPModuleEthPortState_Type()
)
convSSLXFPModuleEthPortState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    convSSLXFPModuleEthPortState.setStatus("current")
_ConvSSLXFPPortOverviewTable_Object = MibTable
convSSLXFPPortOverviewTable = _ConvSSLXFPPortOverviewTable_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 3, 2, 4)
)
if mibBuilder.loadTexts:
    convSSLXFPPortOverviewTable.setStatus("current")
_ConvSSLXFPPortOverviewEntry_Object = MibTableRow
convSSLXFPPortOverviewEntry = _ConvSSLXFPPortOverviewEntry_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 3, 2, 4, 1)
)
convSSLXFPPortOverviewEntry.setIndexNames(
    (0, "SPEEDSINGLELINE-XFP-MIB", "convSSLXFPMPortIndex"),
)
if mibBuilder.loadTexts:
    convSSLXFPPortOverviewEntry.setStatus("current")


class _ConvSSLXFPMPortIndex_Type(Integer32):
    """Custom type convSSLXFPMPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1999),
    )


_ConvSSLXFPMPortIndex_Type.__name__ = "Integer32"
_ConvSSLXFPMPortIndex_Object = MibTableColumn
convSSLXFPMPortIndex = _ConvSSLXFPMPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 3, 2, 4, 1, 1),
    _ConvSSLXFPMPortIndex_Type()
)
convSSLXFPMPortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    convSSLXFPMPortIndex.setStatus("current")


class _ConvSSLXFPMPortSlot_Type(Integer32):
    """Custom type convSSLXFPMPortSlot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 19),
    )


_ConvSSLXFPMPortSlot_Type.__name__ = "Integer32"
_ConvSSLXFPMPortSlot_Object = MibTableColumn
convSSLXFPMPortSlot = _ConvSSLXFPMPortSlot_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 3, 2, 4, 1, 2),
    _ConvSSLXFPMPortSlot_Type()
)
convSSLXFPMPortSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    convSSLXFPMPortSlot.setStatus("current")


class _ConvSSLXFPMPortPort_Type(Integer32):
    """Custom type convSSLXFPMPortPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 34),
    )


_ConvSSLXFPMPortPort_Type.__name__ = "Integer32"
_ConvSSLXFPMPortPort_Object = MibTableColumn
convSSLXFPMPortPort = _ConvSSLXFPMPortPort_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 3, 2, 4, 1, 3),
    _ConvSSLXFPMPortPort_Type()
)
convSSLXFPMPortPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    convSSLXFPMPortPort.setStatus("current")


class _ConvSSLXFPMPortDes_Type(DisplayString):
    """Custom type convSSLXFPMPortDes based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_ConvSSLXFPMPortDes_Type.__name__ = "DisplayString"
_ConvSSLXFPMPortDes_Object = MibTableColumn
convSSLXFPMPortDes = _ConvSSLXFPMPortDes_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 3, 2, 4, 1, 4),
    _ConvSSLXFPMPortDes_Type()
)
convSSLXFPMPortDes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    convSSLXFPMPortDes.setStatus("current")


class _ConvSSLXFPMPortAdminState_Type(Integer32):
    """Custom type convSSLXFPMPortAdminState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              255)
        )
    )
    namedValues = NamedValues(
        *(("adminDown", 0),
          ("adminUp", 1),
          ("notAvalilable", 255))
    )


_ConvSSLXFPMPortAdminState_Type.__name__ = "Integer32"
_ConvSSLXFPMPortAdminState_Object = MibTableColumn
convSSLXFPMPortAdminState = _ConvSSLXFPMPortAdminState_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 3, 2, 4, 1, 5),
    _ConvSSLXFPMPortAdminState_Type()
)
convSSLXFPMPortAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    convSSLXFPMPortAdminState.setStatus("current")


class _ConvSSLXFPMPortXFPState_Type(Integer32):
    """Custom type convSSLXFPMPortXFPState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("xfpRemoved", 0),
          ("xfpInstalled", 1),
          ("xfpTxFault", 2),
          ("notAvalilable", 255))
    )


_ConvSSLXFPMPortXFPState_Type.__name__ = "Integer32"
_ConvSSLXFPMPortXFPState_Object = MibTableColumn
convSSLXFPMPortXFPState = _ConvSSLXFPMPortXFPState_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 3, 2, 4, 1, 6),
    _ConvSSLXFPMPortXFPState_Type()
)
convSSLXFPMPortXFPState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    convSSLXFPMPortXFPState.setStatus("current")


class _ConvSSLXFPMPortTXOperState_Type(Integer32):
    """Custom type convSSLXFPMPortTXOperState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              255)
        )
    )
    namedValues = NamedValues(
        *(("down", 0),
          ("up", 1),
          ("loop", 2),
          ("downLLCF", 3),
          ("downTxFault", 4),
          ("downTxLevel", 5),
          ("bertRunning", 6),
          ("notAvalilable", 255))
    )


_ConvSSLXFPMPortTXOperState_Type.__name__ = "Integer32"
_ConvSSLXFPMPortTXOperState_Object = MibTableColumn
convSSLXFPMPortTXOperState = _ConvSSLXFPMPortTXOperState_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 3, 2, 4, 1, 7),
    _ConvSSLXFPMPortTXOperState_Type()
)
convSSLXFPMPortTXOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    convSSLXFPMPortTXOperState.setStatus("current")


class _ConvSSLXFPMPortRXOperState_Type(Integer32):
    """Custom type convSSLXFPMPortRXOperState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              255)
        )
    )
    namedValues = NamedValues(
        *(("down", 0),
          ("up", 1),
          ("loop", 2),
          ("downLLCF", 3),
          ("downRxFault", 4),
          ("downRxLevel", 5),
          ("bertRunning", 6),
          ("notAvalilable", 255))
    )


_ConvSSLXFPMPortRXOperState_Type.__name__ = "Integer32"
_ConvSSLXFPMPortRXOperState_Object = MibTableColumn
convSSLXFPMPortRXOperState = _ConvSSLXFPMPortRXOperState_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 3, 2, 4, 1, 8),
    _ConvSSLXFPMPortRXOperState_Type()
)
convSSLXFPMPortRXOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    convSSLXFPMPortRXOperState.setStatus("current")


class _ConvSSLXFPMPortAlarmState_Type(Integer32):
    """Custom type convSSLXFPMPortAlarmState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              255)
        )
    )
    namedValues = NamedValues(
        *(("noAlarm", 0),
          ("activeAlarms", 1),
          ("notAvailable", 255))
    )


_ConvSSLXFPMPortAlarmState_Type.__name__ = "Integer32"
_ConvSSLXFPMPortAlarmState_Object = MibTableColumn
convSSLXFPMPortAlarmState = _ConvSSLXFPMPortAlarmState_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 3, 2, 4, 1, 9),
    _ConvSSLXFPMPortAlarmState_Type()
)
convSSLXFPMPortAlarmState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    convSSLXFPMPortAlarmState.setStatus("current")
_ConvSSLXFPModulePortConfigTable_Object = MibTable
convSSLXFPModulePortConfigTable = _ConvSSLXFPModulePortConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 3, 2, 5)
)
if mibBuilder.loadTexts:
    convSSLXFPModulePortConfigTable.setStatus("current")
_ConvSSLXFPModulePortConfigEntry_Object = MibTableRow
convSSLXFPModulePortConfigEntry = _ConvSSLXFPModulePortConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 3, 2, 5, 1)
)
convSSLXFPModulePortConfigEntry.setIndexNames(
    (0, "SPEEDSINGLELINE-XFP-MIB", "convSSLXFPMPortConfIndex"),
)
if mibBuilder.loadTexts:
    convSSLXFPModulePortConfigEntry.setStatus("current")


class _ConvSSLXFPMPortConfIndex_Type(Integer32):
    """Custom type convSSLXFPMPortConfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1999),
    )


_ConvSSLXFPMPortConfIndex_Type.__name__ = "Integer32"
_ConvSSLXFPMPortConfIndex_Object = MibTableColumn
convSSLXFPMPortConfIndex = _ConvSSLXFPMPortConfIndex_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 3, 2, 5, 1, 1),
    _ConvSSLXFPMPortConfIndex_Type()
)
convSSLXFPMPortConfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    convSSLXFPMPortConfIndex.setStatus("current")


class _ConvSSLXFPMPortConfSlot_Type(Integer32):
    """Custom type convSSLXFPMPortConfSlot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 19),
    )


_ConvSSLXFPMPortConfSlot_Type.__name__ = "Integer32"
_ConvSSLXFPMPortConfSlot_Object = MibTableColumn
convSSLXFPMPortConfSlot = _ConvSSLXFPMPortConfSlot_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 3, 2, 5, 1, 2),
    _ConvSSLXFPMPortConfSlot_Type()
)
convSSLXFPMPortConfSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    convSSLXFPMPortConfSlot.setStatus("current")


class _ConvSSLXFPMPortConfPort_Type(Integer32):
    """Custom type convSSLXFPMPortConfPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 34),
    )


_ConvSSLXFPMPortConfPort_Type.__name__ = "Integer32"
_ConvSSLXFPMPortConfPort_Object = MibTableColumn
convSSLXFPMPortConfPort = _ConvSSLXFPMPortConfPort_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 3, 2, 5, 1, 3),
    _ConvSSLXFPMPortConfPort_Type()
)
convSSLXFPMPortConfPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    convSSLXFPMPortConfPort.setStatus("current")


class _ConvSSLXFPMPortAdminConfig_Type(Integer32):
    """Custom type convSSLXFPMPortAdminConfig based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              255)
        )
    )
    namedValues = NamedValues(
        *(("adminDown", 0),
          ("adminUp", 1),
          ("notAvalilable", 255))
    )


_ConvSSLXFPMPortAdminConfig_Type.__name__ = "Integer32"
_ConvSSLXFPMPortAdminConfig_Object = MibTableColumn
convSSLXFPMPortAdminConfig = _ConvSSLXFPMPortAdminConfig_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 3, 2, 5, 1, 4),
    _ConvSSLXFPMPortAdminConfig_Type()
)
convSSLXFPMPortAdminConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    convSSLXFPMPortAdminConfig.setStatus("current")


class _ConvSSLXFPMPortDescription_Type(DisplayString):
    """Custom type convSSLXFPMPortDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_ConvSSLXFPMPortDescription_Type.__name__ = "DisplayString"
_ConvSSLXFPMPortDescription_Object = MibTableColumn
convSSLXFPMPortDescription = _ConvSSLXFPMPortDescription_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 3, 2, 5, 1, 5),
    _ConvSSLXFPMPortDescription_Type()
)
convSSLXFPMPortDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    convSSLXFPMPortDescription.setStatus("current")


class _ConvSSLXFPMPortLLCFConfig_Type(Integer32):
    """Custom type convSSLXFPMPortLLCFConfig based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              255)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1),
          ("notAvalilable", 255))
    )


_ConvSSLXFPMPortLLCFConfig_Type.__name__ = "Integer32"
_ConvSSLXFPMPortLLCFConfig_Object = MibTableColumn
convSSLXFPMPortLLCFConfig = _ConvSSLXFPMPortLLCFConfig_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 3, 2, 5, 1, 6),
    _ConvSSLXFPMPortLLCFConfig_Type()
)
convSSLXFPMPortLLCFConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    convSSLXFPMPortLLCFConfig.setStatus("current")


class _ConvSSLXFPMPortLoopConfig_Type(Integer32):
    """Custom type convSSLXFPMPortLoopConfig based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("externalLoop", 1),
          ("internalLoop", 2),
          ("notAvalilable", 255))
    )


_ConvSSLXFPMPortLoopConfig_Type.__name__ = "Integer32"
_ConvSSLXFPMPortLoopConfig_Object = MibTableColumn
convSSLXFPMPortLoopConfig = _ConvSSLXFPMPortLoopConfig_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 3, 2, 5, 1, 7),
    _ConvSSLXFPMPortLoopConfig_Type()
)
convSSLXFPMPortLoopConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    convSSLXFPMPortLoopConfig.setStatus("current")


class _ConvSSLXFPMPortAlarmDeactivation_Type(Integer32):
    """Custom type convSSLXFPMPortAlarmDeactivation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              255)
        )
    )
    namedValues = NamedValues(
        *(("notAvailable", 0),
          ("alarmReportingEnabled", 1),
          ("alarmReportingDisabledbySchedule", 2),
          ("alarmReportingDisabledPermanent", 3),
          ("unknown", 255))
    )


_ConvSSLXFPMPortAlarmDeactivation_Type.__name__ = "Integer32"
_ConvSSLXFPMPortAlarmDeactivation_Object = MibTableColumn
convSSLXFPMPortAlarmDeactivation = _ConvSSLXFPMPortAlarmDeactivation_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 3, 2, 5, 1, 8),
    _ConvSSLXFPMPortAlarmDeactivation_Type()
)
convSSLXFPMPortAlarmDeactivation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    convSSLXFPMPortAlarmDeactivation.setStatus("current")


class _ConvSSLXFPMPortAlarmSchedule_Type(Integer32):
    """Custom type convSSLXFPMPortAlarmSchedule based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1200),
    )


_ConvSSLXFPMPortAlarmSchedule_Type.__name__ = "Integer32"
_ConvSSLXFPMPortAlarmSchedule_Object = MibTableColumn
convSSLXFPMPortAlarmSchedule = _ConvSSLXFPMPortAlarmSchedule_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 3, 2, 5, 1, 9),
    _ConvSSLXFPMPortAlarmSchedule_Type()
)
convSSLXFPMPortAlarmSchedule.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    convSSLXFPMPortAlarmSchedule.setStatus("current")


class _ConvSSLXFPMPortOTNConfig_Type(Integer32):
    """Custom type convSSLXFPMPortOTNConfig based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("notAvailable", 0),
          ("otnBypass", 1),
          ("otnWithFEC", 2),
          ("otnWithoutFEC", 3))
    )


_ConvSSLXFPMPortOTNConfig_Type.__name__ = "Integer32"
_ConvSSLXFPMPortOTNConfig_Object = MibTableColumn
convSSLXFPMPortOTNConfig = _ConvSSLXFPMPortOTNConfig_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 3, 2, 5, 1, 10),
    _ConvSSLXFPMPortOTNConfig_Type()
)
convSSLXFPMPortOTNConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    convSSLXFPMPortOTNConfig.setStatus("current")


class _ConvSSLXFPMPortOTNMapping_Type(Integer32):
    """Custom type convSSLXFPMPortOTNMapping based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notAvailable", 0),
          ("otnFixedByteStuffing", 1),
          ("otnWithoutFixedByteStuffing", 2))
    )


_ConvSSLXFPMPortOTNMapping_Type.__name__ = "Integer32"
_ConvSSLXFPMPortOTNMapping_Object = MibTableColumn
convSSLXFPMPortOTNMapping = _ConvSSLXFPMPortOTNMapping_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 3, 2, 5, 1, 11),
    _ConvSSLXFPMPortOTNMapping_Type()
)
convSSLXFPMPortOTNMapping.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    convSSLXFPMPortOTNMapping.setStatus("current")
_ConvSSLXFPModulePortGeneralXFPInfosTable_Object = MibTable
convSSLXFPModulePortGeneralXFPInfosTable = _ConvSSLXFPModulePortGeneralXFPInfosTable_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 3, 2, 6)
)
if mibBuilder.loadTexts:
    convSSLXFPModulePortGeneralXFPInfosTable.setStatus("current")
_ConvSSLXFPModulePortGeneralXFPInfosEntry_Object = MibTableRow
convSSLXFPModulePortGeneralXFPInfosEntry = _ConvSSLXFPModulePortGeneralXFPInfosEntry_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 3, 2, 6, 1)
)
convSSLXFPModulePortGeneralXFPInfosEntry.setIndexNames(
    (0, "SPEEDSINGLELINE-XFP-MIB", "convSSLXFPMPortGenIndex"),
)
if mibBuilder.loadTexts:
    convSSLXFPModulePortGeneralXFPInfosEntry.setStatus("current")


class _ConvSSLXFPMPortGenIndex_Type(Integer32):
    """Custom type convSSLXFPMPortGenIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1999),
    )


_ConvSSLXFPMPortGenIndex_Type.__name__ = "Integer32"
_ConvSSLXFPMPortGenIndex_Object = MibTableColumn
convSSLXFPMPortGenIndex = _ConvSSLXFPMPortGenIndex_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 3, 2, 6, 1, 1),
    _ConvSSLXFPMPortGenIndex_Type()
)
convSSLXFPMPortGenIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    convSSLXFPMPortGenIndex.setStatus("current")


class _ConvSSLXFPMPortGenSlot_Type(Integer32):
    """Custom type convSSLXFPMPortGenSlot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 19),
    )


_ConvSSLXFPMPortGenSlot_Type.__name__ = "Integer32"
_ConvSSLXFPMPortGenSlot_Object = MibTableColumn
convSSLXFPMPortGenSlot = _ConvSSLXFPMPortGenSlot_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 3, 2, 6, 1, 2),
    _ConvSSLXFPMPortGenSlot_Type()
)
convSSLXFPMPortGenSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    convSSLXFPMPortGenSlot.setStatus("current")


class _ConvSSLXFPMPortGenPort_Type(Integer32):
    """Custom type convSSLXFPMPortGenPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 34),
    )


_ConvSSLXFPMPortGenPort_Type.__name__ = "Integer32"
_ConvSSLXFPMPortGenPort_Object = MibTableColumn
convSSLXFPMPortGenPort = _ConvSSLXFPMPortGenPort_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 3, 2, 6, 1, 3),
    _ConvSSLXFPMPortGenPort_Type()
)
convSSLXFPMPortGenPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    convSSLXFPMPortGenPort.setStatus("current")


class _ConvSSLXFPMPortXFPPowerclass_Type(Integer32):
    """Custom type convSSLXFPMPortXFPPowerclass based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              255)
        )
    )
    namedValues = NamedValues(
        *(("upTo1-5W", 1),
          ("upTo2-5W", 2),
          ("upTo3-5W", 3),
          ("greater3-5W", 4),
          ("notAvalilable", 255))
    )


_ConvSSLXFPMPortXFPPowerclass_Type.__name__ = "Integer32"
_ConvSSLXFPMPortXFPPowerclass_Object = MibTableColumn
convSSLXFPMPortXFPPowerclass = _ConvSSLXFPMPortXFPPowerclass_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 3, 2, 6, 1, 4),
    _ConvSSLXFPMPortXFPPowerclass_Type()
)
convSSLXFPMPortXFPPowerclass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    convSSLXFPMPortXFPPowerclass.setStatus("current")


class _ConvSSLXFPMPortXFPSmFiberLength_Type(Integer32):
    """Custom type convSSLXFPMPortXFPSmFiberLength based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_ConvSSLXFPMPortXFPSmFiberLength_Type.__name__ = "Integer32"
_ConvSSLXFPMPortXFPSmFiberLength_Object = MibTableColumn
convSSLXFPMPortXFPSmFiberLength = _ConvSSLXFPMPortXFPSmFiberLength_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 3, 2, 6, 1, 5),
    _ConvSSLXFPMPortXFPSmFiberLength_Type()
)
convSSLXFPMPortXFPSmFiberLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    convSSLXFPMPortXFPSmFiberLength.setStatus("current")


class _ConvSSLXFPMPortVendorName_Type(DisplayString):
    """Custom type convSSLXFPMPortVendorName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_ConvSSLXFPMPortVendorName_Type.__name__ = "DisplayString"
_ConvSSLXFPMPortVendorName_Object = MibTableColumn
convSSLXFPMPortVendorName = _ConvSSLXFPMPortVendorName_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 3, 2, 6, 1, 6),
    _ConvSSLXFPMPortVendorName_Type()
)
convSSLXFPMPortVendorName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    convSSLXFPMPortVendorName.setStatus("current")


class _ConvSSLXFPMPortSerialNumber_Type(DisplayString):
    """Custom type convSSLXFPMPortSerialNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_ConvSSLXFPMPortSerialNumber_Type.__name__ = "DisplayString"
_ConvSSLXFPMPortSerialNumber_Object = MibTableColumn
convSSLXFPMPortSerialNumber = _ConvSSLXFPMPortSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 3, 2, 6, 1, 7),
    _ConvSSLXFPMPortSerialNumber_Type()
)
convSSLXFPMPortSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    convSSLXFPMPortSerialNumber.setStatus("current")


class _ConvSSLXFPMPortWavelength_Type(DisplayString):
    """Custom type convSSLXFPMPortWavelength based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_ConvSSLXFPMPortWavelength_Type.__name__ = "DisplayString"
_ConvSSLXFPMPortWavelength_Object = MibTableColumn
convSSLXFPMPortWavelength = _ConvSSLXFPMPortWavelength_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 3, 2, 6, 1, 8),
    _ConvSSLXFPMPortWavelength_Type()
)
convSSLXFPMPortWavelength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    convSSLXFPMPortWavelength.setStatus("current")


class _ConvSSLXFPMPortPartNumber_Type(DisplayString):
    """Custom type convSSLXFPMPortPartNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_ConvSSLXFPMPortPartNumber_Type.__name__ = "DisplayString"
_ConvSSLXFPMPortPartNumber_Object = MibTableColumn
convSSLXFPMPortPartNumber = _ConvSSLXFPMPortPartNumber_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 3, 2, 6, 1, 9),
    _ConvSSLXFPMPortPartNumber_Type()
)
convSSLXFPMPortPartNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    convSSLXFPMPortPartNumber.setStatus("current")
_ConvSSLXFPModulePortXFPMessurementTable_Object = MibTable
convSSLXFPModulePortXFPMessurementTable = _ConvSSLXFPModulePortXFPMessurementTable_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 3, 2, 7)
)
if mibBuilder.loadTexts:
    convSSLXFPModulePortXFPMessurementTable.setStatus("current")
_ConvSSLXFPModulePortXFPMessurementEntry_Object = MibTableRow
convSSLXFPModulePortXFPMessurementEntry = _ConvSSLXFPModulePortXFPMessurementEntry_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 3, 2, 7, 1)
)
convSSLXFPModulePortXFPMessurementEntry.setIndexNames(
    (0, "SPEEDSINGLELINE-XFP-MIB", "convSSLXFPMPortMesIndex"),
)
if mibBuilder.loadTexts:
    convSSLXFPModulePortXFPMessurementEntry.setStatus("current")


class _ConvSSLXFPMPortMesIndex_Type(Integer32):
    """Custom type convSSLXFPMPortMesIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1999),
    )


_ConvSSLXFPMPortMesIndex_Type.__name__ = "Integer32"
_ConvSSLXFPMPortMesIndex_Object = MibTableColumn
convSSLXFPMPortMesIndex = _ConvSSLXFPMPortMesIndex_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 3, 2, 7, 1, 1),
    _ConvSSLXFPMPortMesIndex_Type()
)
convSSLXFPMPortMesIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    convSSLXFPMPortMesIndex.setStatus("current")


class _ConvSSLXFPMPortMesSlot_Type(Integer32):
    """Custom type convSSLXFPMPortMesSlot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 19),
    )


_ConvSSLXFPMPortMesSlot_Type.__name__ = "Integer32"
_ConvSSLXFPMPortMesSlot_Object = MibTableColumn
convSSLXFPMPortMesSlot = _ConvSSLXFPMPortMesSlot_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 3, 2, 7, 1, 2),
    _ConvSSLXFPMPortMesSlot_Type()
)
convSSLXFPMPortMesSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    convSSLXFPMPortMesSlot.setStatus("current")


class _ConvSSLXFPMPortMesPort_Type(Integer32):
    """Custom type convSSLXFPMPortMesPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 34),
    )


_ConvSSLXFPMPortMesPort_Type.__name__ = "Integer32"
_ConvSSLXFPMPortMesPort_Object = MibTableColumn
convSSLXFPMPortMesPort = _ConvSSLXFPMPortMesPort_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 3, 2, 7, 1, 3),
    _ConvSSLXFPMPortMesPort_Type()
)
convSSLXFPMPortMesPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    convSSLXFPMPortMesPort.setStatus("current")
_ConvSSLXFPMPortRxPower_Type = Integer32
_ConvSSLXFPMPortRxPower_Object = MibTableColumn
convSSLXFPMPortRxPower = _ConvSSLXFPMPortRxPower_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 3, 2, 7, 1, 4),
    _ConvSSLXFPMPortRxPower_Type()
)
convSSLXFPMPortRxPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    convSSLXFPMPortRxPower.setStatus("current")
_ConvSSLXFPMPortTxPower_Type = Integer32
_ConvSSLXFPMPortTxPower_Object = MibTableColumn
convSSLXFPMPortTxPower = _ConvSSLXFPMPortTxPower_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 3, 2, 7, 1, 5),
    _ConvSSLXFPMPortTxPower_Type()
)
convSSLXFPMPortTxPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    convSSLXFPMPortTxPower.setStatus("current")
_ConvSSLXFPMPortXFPTemp_Type = Integer32
_ConvSSLXFPMPortXFPTemp_Object = MibTableColumn
convSSLXFPMPortXFPTemp = _ConvSSLXFPMPortXFPTemp_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 3, 2, 7, 1, 6),
    _ConvSSLXFPMPortXFPTemp_Type()
)
convSSLXFPMPortXFPTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    convSSLXFPMPortXFPTemp.setStatus("current")
_ConvSSLXFPMPortTxBias_Type = Integer32
_ConvSSLXFPMPortTxBias_Object = MibTableColumn
convSSLXFPMPortTxBias = _ConvSSLXFPMPortTxBias_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 3, 2, 7, 1, 7),
    _ConvSSLXFPMPortTxBias_Type()
)
convSSLXFPMPortTxBias.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    convSSLXFPMPortTxBias.setStatus("current")
_ConvSSLXFPMPortFECRate_Type = Integer32
_ConvSSLXFPMPortFECRate_Object = MibTableColumn
convSSLXFPMPortFECRate = _ConvSSLXFPMPortFECRate_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 3, 2, 7, 1, 8),
    _ConvSSLXFPMPortFECRate_Type()
)
convSSLXFPMPortFECRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    convSSLXFPMPortFECRate.setStatus("current")
_ConvSSLXFPModuleThresholdsConfigTable_Object = MibTable
convSSLXFPModuleThresholdsConfigTable = _ConvSSLXFPModuleThresholdsConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 3, 2, 8)
)
if mibBuilder.loadTexts:
    convSSLXFPModuleThresholdsConfigTable.setStatus("current")
_ConvSSLXFPModuleThresholdsConfigEntry_Object = MibTableRow
convSSLXFPModuleThresholdsConfigEntry = _ConvSSLXFPModuleThresholdsConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 3, 2, 8, 1)
)
convSSLXFPModuleThresholdsConfigEntry.setIndexNames(
    (0, "SPEEDSINGLELINE-XFP-MIB", "convSSLXFPMPortThresIndex"),
)
if mibBuilder.loadTexts:
    convSSLXFPModuleThresholdsConfigEntry.setStatus("current")


class _ConvSSLXFPMPortThresIndex_Type(Integer32):
    """Custom type convSSLXFPMPortThresIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1999),
    )


_ConvSSLXFPMPortThresIndex_Type.__name__ = "Integer32"
_ConvSSLXFPMPortThresIndex_Object = MibTableColumn
convSSLXFPMPortThresIndex = _ConvSSLXFPMPortThresIndex_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 3, 2, 8, 1, 1),
    _ConvSSLXFPMPortThresIndex_Type()
)
convSSLXFPMPortThresIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    convSSLXFPMPortThresIndex.setStatus("current")


class _ConvSSLXFPMPortThresSlot_Type(Integer32):
    """Custom type convSSLXFPMPortThresSlot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 19),
    )


_ConvSSLXFPMPortThresSlot_Type.__name__ = "Integer32"
_ConvSSLXFPMPortThresSlot_Object = MibTableColumn
convSSLXFPMPortThresSlot = _ConvSSLXFPMPortThresSlot_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 3, 2, 8, 1, 2),
    _ConvSSLXFPMPortThresSlot_Type()
)
convSSLXFPMPortThresSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    convSSLXFPMPortThresSlot.setStatus("current")


class _ConvSSLXFPMPortThresPort_Type(Integer32):
    """Custom type convSSLXFPMPortThresPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 34),
    )


_ConvSSLXFPMPortThresPort_Type.__name__ = "Integer32"
_ConvSSLXFPMPortThresPort_Object = MibTableColumn
convSSLXFPMPortThresPort = _ConvSSLXFPMPortThresPort_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 3, 2, 8, 1, 3),
    _ConvSSLXFPMPortThresPort_Type()
)
convSSLXFPMPortThresPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    convSSLXFPMPortThresPort.setStatus("current")
_ConvSSLXFPMPortRxLowAlarmLevel_Type = Integer32
_ConvSSLXFPMPortRxLowAlarmLevel_Object = MibTableColumn
convSSLXFPMPortRxLowAlarmLevel = _ConvSSLXFPMPortRxLowAlarmLevel_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 3, 2, 8, 1, 4),
    _ConvSSLXFPMPortRxLowAlarmLevel_Type()
)
convSSLXFPMPortRxLowAlarmLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    convSSLXFPMPortRxLowAlarmLevel.setStatus("current")
_ConvSSLXFPMPortRxHighAlarmLevel_Type = Integer32
_ConvSSLXFPMPortRxHighAlarmLevel_Object = MibTableColumn
convSSLXFPMPortRxHighAlarmLevel = _ConvSSLXFPMPortRxHighAlarmLevel_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 3, 2, 8, 1, 5),
    _ConvSSLXFPMPortRxHighAlarmLevel_Type()
)
convSSLXFPMPortRxHighAlarmLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    convSSLXFPMPortRxHighAlarmLevel.setStatus("current")
_ConvSSLXFPMPortRxLowWarningLevel_Type = Integer32
_ConvSSLXFPMPortRxLowWarningLevel_Object = MibTableColumn
convSSLXFPMPortRxLowWarningLevel = _ConvSSLXFPMPortRxLowWarningLevel_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 3, 2, 8, 1, 6),
    _ConvSSLXFPMPortRxLowWarningLevel_Type()
)
convSSLXFPMPortRxLowWarningLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    convSSLXFPMPortRxLowWarningLevel.setStatus("current")
_ConvSSLXFPMPortRxHighWarningLevel_Type = Integer32
_ConvSSLXFPMPortRxHighWarningLevel_Object = MibTableColumn
convSSLXFPMPortRxHighWarningLevel = _ConvSSLXFPMPortRxHighWarningLevel_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 3, 2, 8, 1, 7),
    _ConvSSLXFPMPortRxHighWarningLevel_Type()
)
convSSLXFPMPortRxHighWarningLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    convSSLXFPMPortRxHighWarningLevel.setStatus("current")
_ConvSSLXFPMPortTxLowAlarmLevel_Type = Integer32
_ConvSSLXFPMPortTxLowAlarmLevel_Object = MibTableColumn
convSSLXFPMPortTxLowAlarmLevel = _ConvSSLXFPMPortTxLowAlarmLevel_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 3, 2, 8, 1, 8),
    _ConvSSLXFPMPortTxLowAlarmLevel_Type()
)
convSSLXFPMPortTxLowAlarmLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    convSSLXFPMPortTxLowAlarmLevel.setStatus("current")
_ConvSSLXFPMPortTxHighAlarmLevel_Type = Integer32
_ConvSSLXFPMPortTxHighAlarmLevel_Object = MibTableColumn
convSSLXFPMPortTxHighAlarmLevel = _ConvSSLXFPMPortTxHighAlarmLevel_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 3, 2, 8, 1, 9),
    _ConvSSLXFPMPortTxHighAlarmLevel_Type()
)
convSSLXFPMPortTxHighAlarmLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    convSSLXFPMPortTxHighAlarmLevel.setStatus("current")
_ConvSSLXFPMPortTxLowWarningLevel_Type = Integer32
_ConvSSLXFPMPortTxLowWarningLevel_Object = MibTableColumn
convSSLXFPMPortTxLowWarningLevel = _ConvSSLXFPMPortTxLowWarningLevel_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 3, 2, 8, 1, 10),
    _ConvSSLXFPMPortTxLowWarningLevel_Type()
)
convSSLXFPMPortTxLowWarningLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    convSSLXFPMPortTxLowWarningLevel.setStatus("current")
_ConvSSLXFPMPortTxHighWarningLevel_Type = Integer32
_ConvSSLXFPMPortTxHighWarningLevel_Object = MibTableColumn
convSSLXFPMPortTxHighWarningLevel = _ConvSSLXFPMPortTxHighWarningLevel_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 3, 2, 8, 1, 11),
    _ConvSSLXFPMPortTxHighWarningLevel_Type()
)
convSSLXFPMPortTxHighWarningLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    convSSLXFPMPortTxHighWarningLevel.setStatus("current")
_ConvSSLXFPMPortTxBiasLowAlarmLevel_Type = Integer32
_ConvSSLXFPMPortTxBiasLowAlarmLevel_Object = MibTableColumn
convSSLXFPMPortTxBiasLowAlarmLevel = _ConvSSLXFPMPortTxBiasLowAlarmLevel_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 3, 2, 8, 1, 12),
    _ConvSSLXFPMPortTxBiasLowAlarmLevel_Type()
)
convSSLXFPMPortTxBiasLowAlarmLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    convSSLXFPMPortTxBiasLowAlarmLevel.setStatus("current")
_ConvSSLXFPMPortTxBiasHighAlarmLevel_Type = Integer32
_ConvSSLXFPMPortTxBiasHighAlarmLevel_Object = MibTableColumn
convSSLXFPMPortTxBiasHighAlarmLevel = _ConvSSLXFPMPortTxBiasHighAlarmLevel_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 3, 2, 8, 1, 13),
    _ConvSSLXFPMPortTxBiasHighAlarmLevel_Type()
)
convSSLXFPMPortTxBiasHighAlarmLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    convSSLXFPMPortTxBiasHighAlarmLevel.setStatus("current")
_ConvSSLXFPMPortTxBiasLowWarningLevel_Type = Integer32
_ConvSSLXFPMPortTxBiasLowWarningLevel_Object = MibTableColumn
convSSLXFPMPortTxBiasLowWarningLevel = _ConvSSLXFPMPortTxBiasLowWarningLevel_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 3, 2, 8, 1, 14),
    _ConvSSLXFPMPortTxBiasLowWarningLevel_Type()
)
convSSLXFPMPortTxBiasLowWarningLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    convSSLXFPMPortTxBiasLowWarningLevel.setStatus("current")
_ConvSSLXFPMPortTxBiasHighWarningLevel_Type = Integer32
_ConvSSLXFPMPortTxBiasHighWarningLevel_Object = MibTableColumn
convSSLXFPMPortTxBiasHighWarningLevel = _ConvSSLXFPMPortTxBiasHighWarningLevel_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 3, 2, 8, 1, 15),
    _ConvSSLXFPMPortTxBiasHighWarningLevel_Type()
)
convSSLXFPMPortTxBiasHighWarningLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    convSSLXFPMPortTxBiasHighWarningLevel.setStatus("current")
_ConvSSLXFPMPortTempLowAlarmLevel_Type = Integer32
_ConvSSLXFPMPortTempLowAlarmLevel_Object = MibTableColumn
convSSLXFPMPortTempLowAlarmLevel = _ConvSSLXFPMPortTempLowAlarmLevel_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 3, 2, 8, 1, 16),
    _ConvSSLXFPMPortTempLowAlarmLevel_Type()
)
convSSLXFPMPortTempLowAlarmLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    convSSLXFPMPortTempLowAlarmLevel.setStatus("current")
_ConvSSLXFPMPortTempHighAlarmLevel_Type = Integer32
_ConvSSLXFPMPortTempHighAlarmLevel_Object = MibTableColumn
convSSLXFPMPortTempHighAlarmLevel = _ConvSSLXFPMPortTempHighAlarmLevel_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 3, 2, 8, 1, 17),
    _ConvSSLXFPMPortTempHighAlarmLevel_Type()
)
convSSLXFPMPortTempHighAlarmLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    convSSLXFPMPortTempHighAlarmLevel.setStatus("current")
_ConvSSLXFPMPortTempLowWarningLevel_Type = Integer32
_ConvSSLXFPMPortTempLowWarningLevel_Object = MibTableColumn
convSSLXFPMPortTempLowWarningLevel = _ConvSSLXFPMPortTempLowWarningLevel_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 3, 2, 8, 1, 18),
    _ConvSSLXFPMPortTempLowWarningLevel_Type()
)
convSSLXFPMPortTempLowWarningLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    convSSLXFPMPortTempLowWarningLevel.setStatus("current")
_ConvSSLXFPMPortTempHighWarningLevel_Type = Integer32
_ConvSSLXFPMPortTempHighWarningLevel_Object = MibTableColumn
convSSLXFPMPortTempHighWarningLevel = _ConvSSLXFPMPortTempHighWarningLevel_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 3, 2, 8, 1, 19),
    _ConvSSLXFPMPortTempHighWarningLevel_Type()
)
convSSLXFPMPortTempHighWarningLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    convSSLXFPMPortTempHighWarningLevel.setStatus("current")
_ConvSSLXFPModuleEventTable_Object = MibTable
convSSLXFPModuleEventTable = _ConvSSLXFPModuleEventTable_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 3, 2, 9)
)
if mibBuilder.loadTexts:
    convSSLXFPModuleEventTable.setStatus("current")
_ConvSSLXFPModuleEventEntry_Object = MibTableRow
convSSLXFPModuleEventEntry = _ConvSSLXFPModuleEventEntry_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 3, 2, 9, 1)
)
convSSLXFPModuleEventEntry.setIndexNames(
    (0, "SPEEDSINGLELINE-XFP-MIB", "convSSLXFPPIndex"),
)
if mibBuilder.loadTexts:
    convSSLXFPModuleEventEntry.setStatus("current")


class _ConvSSLXFPPIndex_Type(Integer32):
    """Custom type convSSLXFPPIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1999),
    )


_ConvSSLXFPPIndex_Type.__name__ = "Integer32"
_ConvSSLXFPPIndex_Object = MibTableColumn
convSSLXFPPIndex = _ConvSSLXFPPIndex_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 3, 2, 9, 1, 1),
    _ConvSSLXFPPIndex_Type()
)
convSSLXFPPIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    convSSLXFPPIndex.setStatus("current")


class _ConvSSLXFPPSlot_Type(Integer32):
    """Custom type convSSLXFPPSlot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 19),
    )


_ConvSSLXFPPSlot_Type.__name__ = "Integer32"
_ConvSSLXFPPSlot_Object = MibTableColumn
convSSLXFPPSlot = _ConvSSLXFPPSlot_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 3, 2, 9, 1, 2),
    _ConvSSLXFPPSlot_Type()
)
convSSLXFPPSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    convSSLXFPPSlot.setStatus("current")


class _ConvSSLXFPPPort_Type(Integer32):
    """Custom type convSSLXFPPPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 34),
    )


_ConvSSLXFPPPort_Type.__name__ = "Integer32"
_ConvSSLXFPPPort_Object = MibTableColumn
convSSLXFPPPort = _ConvSSLXFPPPort_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 3, 2, 9, 1, 3),
    _ConvSSLXFPPPort_Type()
)
convSSLXFPPPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    convSSLXFPPPort.setStatus("current")


class _ConvSSLXFPPPortRxLowAlarmEvent_Type(Integer32):
    """Custom type convSSLXFPPPortRxLowAlarmEvent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              255)
        )
    )
    namedValues = NamedValues(
        *(("normal", 0),
          ("active", 1),
          ("notAvailable", 255))
    )


_ConvSSLXFPPPortRxLowAlarmEvent_Type.__name__ = "Integer32"
_ConvSSLXFPPPortRxLowAlarmEvent_Object = MibTableColumn
convSSLXFPPPortRxLowAlarmEvent = _ConvSSLXFPPPortRxLowAlarmEvent_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 3, 2, 9, 1, 4),
    _ConvSSLXFPPPortRxLowAlarmEvent_Type()
)
convSSLXFPPPortRxLowAlarmEvent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    convSSLXFPPPortRxLowAlarmEvent.setStatus("current")


class _ConvSSLXFPPPortRxHighAlarmEvent_Type(Integer32):
    """Custom type convSSLXFPPPortRxHighAlarmEvent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              255)
        )
    )
    namedValues = NamedValues(
        *(("normal", 0),
          ("active", 1),
          ("notAvailable", 255))
    )


_ConvSSLXFPPPortRxHighAlarmEvent_Type.__name__ = "Integer32"
_ConvSSLXFPPPortRxHighAlarmEvent_Object = MibTableColumn
convSSLXFPPPortRxHighAlarmEvent = _ConvSSLXFPPPortRxHighAlarmEvent_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 3, 2, 9, 1, 5),
    _ConvSSLXFPPPortRxHighAlarmEvent_Type()
)
convSSLXFPPPortRxHighAlarmEvent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    convSSLXFPPPortRxHighAlarmEvent.setStatus("current")


class _ConvSSLXFPPPortRxLowWarningEvent_Type(Integer32):
    """Custom type convSSLXFPPPortRxLowWarningEvent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              255)
        )
    )
    namedValues = NamedValues(
        *(("normal", 0),
          ("active", 1),
          ("notAvailable", 255))
    )


_ConvSSLXFPPPortRxLowWarningEvent_Type.__name__ = "Integer32"
_ConvSSLXFPPPortRxLowWarningEvent_Object = MibTableColumn
convSSLXFPPPortRxLowWarningEvent = _ConvSSLXFPPPortRxLowWarningEvent_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 3, 2, 9, 1, 6),
    _ConvSSLXFPPPortRxLowWarningEvent_Type()
)
convSSLXFPPPortRxLowWarningEvent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    convSSLXFPPPortRxLowWarningEvent.setStatus("current")


class _ConvSSLXFPPPortRxHighWarningEvent_Type(Integer32):
    """Custom type convSSLXFPPPortRxHighWarningEvent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              255)
        )
    )
    namedValues = NamedValues(
        *(("normal", 0),
          ("active", 1),
          ("notAvailable", 255))
    )


_ConvSSLXFPPPortRxHighWarningEvent_Type.__name__ = "Integer32"
_ConvSSLXFPPPortRxHighWarningEvent_Object = MibTableColumn
convSSLXFPPPortRxHighWarningEvent = _ConvSSLXFPPPortRxHighWarningEvent_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 3, 2, 9, 1, 7),
    _ConvSSLXFPPPortRxHighWarningEvent_Type()
)
convSSLXFPPPortRxHighWarningEvent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    convSSLXFPPPortRxHighWarningEvent.setStatus("current")


class _ConvSSLXFPPPortTxLowAlarmEvent_Type(Integer32):
    """Custom type convSSLXFPPPortTxLowAlarmEvent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              255)
        )
    )
    namedValues = NamedValues(
        *(("normal", 0),
          ("active", 1),
          ("notAvailable", 255))
    )


_ConvSSLXFPPPortTxLowAlarmEvent_Type.__name__ = "Integer32"
_ConvSSLXFPPPortTxLowAlarmEvent_Object = MibTableColumn
convSSLXFPPPortTxLowAlarmEvent = _ConvSSLXFPPPortTxLowAlarmEvent_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 3, 2, 9, 1, 8),
    _ConvSSLXFPPPortTxLowAlarmEvent_Type()
)
convSSLXFPPPortTxLowAlarmEvent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    convSSLXFPPPortTxLowAlarmEvent.setStatus("current")


class _ConvSSLXFPPPortTxHighAlarmEvent_Type(Integer32):
    """Custom type convSSLXFPPPortTxHighAlarmEvent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              255)
        )
    )
    namedValues = NamedValues(
        *(("normal", 0),
          ("active", 1),
          ("notAvailable", 255))
    )


_ConvSSLXFPPPortTxHighAlarmEvent_Type.__name__ = "Integer32"
_ConvSSLXFPPPortTxHighAlarmEvent_Object = MibTableColumn
convSSLXFPPPortTxHighAlarmEvent = _ConvSSLXFPPPortTxHighAlarmEvent_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 3, 2, 9, 1, 9),
    _ConvSSLXFPPPortTxHighAlarmEvent_Type()
)
convSSLXFPPPortTxHighAlarmEvent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    convSSLXFPPPortTxHighAlarmEvent.setStatus("current")


class _ConvSSLXFPPPortTxLowWarningEvent_Type(Integer32):
    """Custom type convSSLXFPPPortTxLowWarningEvent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              255)
        )
    )
    namedValues = NamedValues(
        *(("normal", 0),
          ("active", 1),
          ("notAvailable", 255))
    )


_ConvSSLXFPPPortTxLowWarningEvent_Type.__name__ = "Integer32"
_ConvSSLXFPPPortTxLowWarningEvent_Object = MibTableColumn
convSSLXFPPPortTxLowWarningEvent = _ConvSSLXFPPPortTxLowWarningEvent_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 3, 2, 9, 1, 10),
    _ConvSSLXFPPPortTxLowWarningEvent_Type()
)
convSSLXFPPPortTxLowWarningEvent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    convSSLXFPPPortTxLowWarningEvent.setStatus("current")


class _ConvSSLXFPPPortTxHighWarningEvent_Type(Integer32):
    """Custom type convSSLXFPPPortTxHighWarningEvent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              255)
        )
    )
    namedValues = NamedValues(
        *(("normal", 0),
          ("active", 1),
          ("notAvailable", 255))
    )


_ConvSSLXFPPPortTxHighWarningEvent_Type.__name__ = "Integer32"
_ConvSSLXFPPPortTxHighWarningEvent_Object = MibTableColumn
convSSLXFPPPortTxHighWarningEvent = _ConvSSLXFPPPortTxHighWarningEvent_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 3, 2, 9, 1, 11),
    _ConvSSLXFPPPortTxHighWarningEvent_Type()
)
convSSLXFPPPortTxHighWarningEvent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    convSSLXFPPPortTxHighWarningEvent.setStatus("current")


class _ConvSSLXFPPPortTxBiasLowAlarmEvent_Type(Integer32):
    """Custom type convSSLXFPPPortTxBiasLowAlarmEvent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              255)
        )
    )
    namedValues = NamedValues(
        *(("normal", 0),
          ("active", 1),
          ("notAvailable", 255))
    )


_ConvSSLXFPPPortTxBiasLowAlarmEvent_Type.__name__ = "Integer32"
_ConvSSLXFPPPortTxBiasLowAlarmEvent_Object = MibTableColumn
convSSLXFPPPortTxBiasLowAlarmEvent = _ConvSSLXFPPPortTxBiasLowAlarmEvent_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 3, 2, 9, 1, 12),
    _ConvSSLXFPPPortTxBiasLowAlarmEvent_Type()
)
convSSLXFPPPortTxBiasLowAlarmEvent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    convSSLXFPPPortTxBiasLowAlarmEvent.setStatus("current")


class _ConvSSLXFPPPortTxBiasHighAlarmEvent_Type(Integer32):
    """Custom type convSSLXFPPPortTxBiasHighAlarmEvent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              255)
        )
    )
    namedValues = NamedValues(
        *(("normal", 0),
          ("active", 1),
          ("notAvailable", 255))
    )


_ConvSSLXFPPPortTxBiasHighAlarmEvent_Type.__name__ = "Integer32"
_ConvSSLXFPPPortTxBiasHighAlarmEvent_Object = MibTableColumn
convSSLXFPPPortTxBiasHighAlarmEvent = _ConvSSLXFPPPortTxBiasHighAlarmEvent_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 3, 2, 9, 1, 13),
    _ConvSSLXFPPPortTxBiasHighAlarmEvent_Type()
)
convSSLXFPPPortTxBiasHighAlarmEvent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    convSSLXFPPPortTxBiasHighAlarmEvent.setStatus("current")


class _ConvSSLXFPPPortTxBiasLowWarningEvent_Type(Integer32):
    """Custom type convSSLXFPPPortTxBiasLowWarningEvent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              255)
        )
    )
    namedValues = NamedValues(
        *(("normal", 0),
          ("active", 1),
          ("notAvailable", 255))
    )


_ConvSSLXFPPPortTxBiasLowWarningEvent_Type.__name__ = "Integer32"
_ConvSSLXFPPPortTxBiasLowWarningEvent_Object = MibTableColumn
convSSLXFPPPortTxBiasLowWarningEvent = _ConvSSLXFPPPortTxBiasLowWarningEvent_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 3, 2, 9, 1, 14),
    _ConvSSLXFPPPortTxBiasLowWarningEvent_Type()
)
convSSLXFPPPortTxBiasLowWarningEvent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    convSSLXFPPPortTxBiasLowWarningEvent.setStatus("current")


class _ConvSSLXFPPPortTxBiasHighWarningEvent_Type(Integer32):
    """Custom type convSSLXFPPPortTxBiasHighWarningEvent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              255)
        )
    )
    namedValues = NamedValues(
        *(("normal", 0),
          ("active", 1),
          ("notAvailable", 255))
    )


_ConvSSLXFPPPortTxBiasHighWarningEvent_Type.__name__ = "Integer32"
_ConvSSLXFPPPortTxBiasHighWarningEvent_Object = MibTableColumn
convSSLXFPPPortTxBiasHighWarningEvent = _ConvSSLXFPPPortTxBiasHighWarningEvent_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 3, 2, 9, 1, 15),
    _ConvSSLXFPPPortTxBiasHighWarningEvent_Type()
)
convSSLXFPPPortTxBiasHighWarningEvent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    convSSLXFPPPortTxBiasHighWarningEvent.setStatus("current")


class _ConvSSLXFPPPortTempLowAlarmEvent_Type(Integer32):
    """Custom type convSSLXFPPPortTempLowAlarmEvent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              255)
        )
    )
    namedValues = NamedValues(
        *(("normal", 0),
          ("active", 1),
          ("notAvailable", 255))
    )


_ConvSSLXFPPPortTempLowAlarmEvent_Type.__name__ = "Integer32"
_ConvSSLXFPPPortTempLowAlarmEvent_Object = MibTableColumn
convSSLXFPPPortTempLowAlarmEvent = _ConvSSLXFPPPortTempLowAlarmEvent_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 3, 2, 9, 1, 16),
    _ConvSSLXFPPPortTempLowAlarmEvent_Type()
)
convSSLXFPPPortTempLowAlarmEvent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    convSSLXFPPPortTempLowAlarmEvent.setStatus("current")


class _ConvSSLXFPPPortTempHighAlarmEvent_Type(Integer32):
    """Custom type convSSLXFPPPortTempHighAlarmEvent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              255)
        )
    )
    namedValues = NamedValues(
        *(("normal", 0),
          ("active", 1),
          ("notAvailable", 255))
    )


_ConvSSLXFPPPortTempHighAlarmEvent_Type.__name__ = "Integer32"
_ConvSSLXFPPPortTempHighAlarmEvent_Object = MibTableColumn
convSSLXFPPPortTempHighAlarmEvent = _ConvSSLXFPPPortTempHighAlarmEvent_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 3, 2, 9, 1, 17),
    _ConvSSLXFPPPortTempHighAlarmEvent_Type()
)
convSSLXFPPPortTempHighAlarmEvent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    convSSLXFPPPortTempHighAlarmEvent.setStatus("current")


class _ConvSSLXFPPPortTempLowWarningEvent_Type(Integer32):
    """Custom type convSSLXFPPPortTempLowWarningEvent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              255)
        )
    )
    namedValues = NamedValues(
        *(("normal", 0),
          ("active", 1),
          ("notAvailable", 255))
    )


_ConvSSLXFPPPortTempLowWarningEvent_Type.__name__ = "Integer32"
_ConvSSLXFPPPortTempLowWarningEvent_Object = MibTableColumn
convSSLXFPPPortTempLowWarningEvent = _ConvSSLXFPPPortTempLowWarningEvent_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 3, 2, 9, 1, 18),
    _ConvSSLXFPPPortTempLowWarningEvent_Type()
)
convSSLXFPPPortTempLowWarningEvent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    convSSLXFPPPortTempLowWarningEvent.setStatus("current")


class _ConvSSLXFPPPortTempHighWarningEvent_Type(Integer32):
    """Custom type convSSLXFPPPortTempHighWarningEvent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              255)
        )
    )
    namedValues = NamedValues(
        *(("normal", 0),
          ("active", 1),
          ("notAvailable", 255))
    )


_ConvSSLXFPPPortTempHighWarningEvent_Type.__name__ = "Integer32"
_ConvSSLXFPPPortTempHighWarningEvent_Object = MibTableColumn
convSSLXFPPPortTempHighWarningEvent = _ConvSSLXFPPPortTempHighWarningEvent_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 3, 2, 9, 1, 19),
    _ConvSSLXFPPPortTempHighWarningEvent_Type()
)
convSSLXFPPPortTempHighWarningEvent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    convSSLXFPPPortTempHighWarningEvent.setStatus("current")


class _ConvSSLXFPPPortOtnAlarmEvent_Type(Integer32):
    """Custom type convSSLXFPPPortOtnAlarmEvent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("normal", 0),
          ("active", 1))
    )


_ConvSSLXFPPPortOtnAlarmEvent_Type.__name__ = "Integer32"
_ConvSSLXFPPPortOtnAlarmEvent_Object = MibTableColumn
convSSLXFPPPortOtnAlarmEvent = _ConvSSLXFPPPortOtnAlarmEvent_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 3, 2, 9, 1, 20),
    _ConvSSLXFPPPortOtnAlarmEvent_Type()
)
convSSLXFPPPortOtnAlarmEvent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    convSSLXFPPPortOtnAlarmEvent.setStatus("current")
_ConvSSLXFPPortTunableTable_Object = MibTable
convSSLXFPPortTunableTable = _ConvSSLXFPPortTunableTable_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 3, 2, 10)
)
if mibBuilder.loadTexts:
    convSSLXFPPortTunableTable.setStatus("current")
_ConvSSLXFPPortTunableEntry_Object = MibTableRow
convSSLXFPPortTunableEntry = _ConvSSLXFPPortTunableEntry_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 3, 2, 10, 1)
)
convSSLXFPPortTunableEntry.setIndexNames(
    (0, "SPEEDSINGLELINE-XFP-MIB", "convSSLXFPPortXCVIndex"),
)
if mibBuilder.loadTexts:
    convSSLXFPPortTunableEntry.setStatus("current")


class _ConvSSLXFPPortXCVIndex_Type(Integer32):
    """Custom type convSSLXFPPortXCVIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1999),
    )


_ConvSSLXFPPortXCVIndex_Type.__name__ = "Integer32"
_ConvSSLXFPPortXCVIndex_Object = MibTableColumn
convSSLXFPPortXCVIndex = _ConvSSLXFPPortXCVIndex_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 3, 2, 10, 1, 1),
    _ConvSSLXFPPortXCVIndex_Type()
)
convSSLXFPPortXCVIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    convSSLXFPPortXCVIndex.setStatus("current")


class _ConvSSLXFPPortXCVSlot_Type(Integer32):
    """Custom type convSSLXFPPortXCVSlot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 19),
    )


_ConvSSLXFPPortXCVSlot_Type.__name__ = "Integer32"
_ConvSSLXFPPortXCVSlot_Object = MibTableColumn
convSSLXFPPortXCVSlot = _ConvSSLXFPPortXCVSlot_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 3, 2, 10, 1, 2),
    _ConvSSLXFPPortXCVSlot_Type()
)
convSSLXFPPortXCVSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    convSSLXFPPortXCVSlot.setStatus("current")


class _ConvSSLXFPPortXCVPort_Type(Integer32):
    """Custom type convSSLXFPPortXCVPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 34),
    )


_ConvSSLXFPPortXCVPort_Type.__name__ = "Integer32"
_ConvSSLXFPPortXCVPort_Object = MibTableColumn
convSSLXFPPortXCVPort = _ConvSSLXFPPortXCVPort_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 3, 2, 10, 1, 3),
    _ConvSSLXFPPortXCVPort_Type()
)
convSSLXFPPortXCVPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    convSSLXFPPortXCVPort.setStatus("current")
_ConvSSLXFPPortXCVChannelSpacing_Type = Integer32
_ConvSSLXFPPortXCVChannelSpacing_Object = MibTableColumn
convSSLXFPPortXCVChannelSpacing = _ConvSSLXFPPortXCVChannelSpacing_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 3, 2, 10, 1, 4),
    _ConvSSLXFPPortXCVChannelSpacing_Type()
)
convSSLXFPPortXCVChannelSpacing.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    convSSLXFPPortXCVChannelSpacing.setStatus("current")
_ConvSSLXFPPortXCVNumberOfChannels_Type = Integer32
_ConvSSLXFPPortXCVNumberOfChannels_Object = MibTableColumn
convSSLXFPPortXCVNumberOfChannels = _ConvSSLXFPPortXCVNumberOfChannels_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 3, 2, 10, 1, 5),
    _ConvSSLXFPPortXCVNumberOfChannels_Type()
)
convSSLXFPPortXCVNumberOfChannels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    convSSLXFPPortXCVNumberOfChannels.setStatus("current")
_ConvSSLXFPPortXCVCenterWavlength_Type = Integer32
_ConvSSLXFPPortXCVCenterWavlength_Object = MibTableColumn
convSSLXFPPortXCVCenterWavlength = _ConvSSLXFPPortXCVCenterWavlength_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 3, 2, 10, 1, 6),
    _ConvSSLXFPPortXCVCenterWavlength_Type()
)
convSSLXFPPortXCVCenterWavlength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    convSSLXFPPortXCVCenterWavlength.setStatus("current")


class _ConvSSLXFPPortXCVTunableFeature_Type(Integer32):
    """Custom type convSSLXFPPortXCVTunableFeature based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              4,
              6)
        )
    )
    namedValues = NamedValues(
        *(("notAvailable", 0),
          ("notTunable", 1),
          ("byWavelength", 2),
          ("byChannel", 4),
          ("byChannelAndWavelength", 6))
    )


_ConvSSLXFPPortXCVTunableFeature_Type.__name__ = "Integer32"
_ConvSSLXFPPortXCVTunableFeature_Object = MibTableColumn
convSSLXFPPortXCVTunableFeature = _ConvSSLXFPPortXCVTunableFeature_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 3, 2, 10, 1, 7),
    _ConvSSLXFPPortXCVTunableFeature_Type()
)
convSSLXFPPortXCVTunableFeature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    convSSLXFPPortXCVTunableFeature.setStatus("current")


class _ConvSSLXFPPortXCVTunableMinMaxChannel_Type(DisplayString):
    """Custom type convSSLXFPPortXCVTunableMinMaxChannel based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 9),
    )


_ConvSSLXFPPortXCVTunableMinMaxChannel_Type.__name__ = "DisplayString"
_ConvSSLXFPPortXCVTunableMinMaxChannel_Object = MibTableColumn
convSSLXFPPortXCVTunableMinMaxChannel = _ConvSSLXFPPortXCVTunableMinMaxChannel_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 3, 2, 10, 1, 8),
    _ConvSSLXFPPortXCVTunableMinMaxChannel_Type()
)
convSSLXFPPortXCVTunableMinMaxChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    convSSLXFPPortXCVTunableMinMaxChannel.setStatus("current")
_ConvSSLXFPPortXCVTunableWavelengthConfig_Type = Integer32
_ConvSSLXFPPortXCVTunableWavelengthConfig_Object = MibTableColumn
convSSLXFPPortXCVTunableWavelengthConfig = _ConvSSLXFPPortXCVTunableWavelengthConfig_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 3, 2, 10, 1, 9),
    _ConvSSLXFPPortXCVTunableWavelengthConfig_Type()
)
convSSLXFPPortXCVTunableWavelengthConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    convSSLXFPPortXCVTunableWavelengthConfig.setStatus("current")


class _ConvSSLXFPPortXCVTunableChannelConfig_Type(DisplayString):
    """Custom type convSSLXFPPortXCVTunableChannelConfig based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 4),
    )


_ConvSSLXFPPortXCVTunableChannelConfig_Type.__name__ = "DisplayString"
_ConvSSLXFPPortXCVTunableChannelConfig_Object = MibTableColumn
convSSLXFPPortXCVTunableChannelConfig = _ConvSSLXFPPortXCVTunableChannelConfig_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 3, 2, 10, 1, 10),
    _ConvSSLXFPPortXCVTunableChannelConfig_Type()
)
convSSLXFPPortXCVTunableChannelConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    convSSLXFPPortXCVTunableChannelConfig.setStatus("current")


class _ConvSSLXFPPortXCVTunableConfigSelection_Type(Integer32):
    """Custom type convSSLXFPPortXCVTunableConfigSelection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("notAvailiable", 0),
          ("xcvInternal", 1),
          ("configFile", 2),
          ("unknown", 255))
    )


_ConvSSLXFPPortXCVTunableConfigSelection_Type.__name__ = "Integer32"
_ConvSSLXFPPortXCVTunableConfigSelection_Object = MibTableColumn
convSSLXFPPortXCVTunableConfigSelection = _ConvSSLXFPPortXCVTunableConfigSelection_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 3, 2, 10, 1, 11),
    _ConvSSLXFPPortXCVTunableConfigSelection_Type()
)
convSSLXFPPortXCVTunableConfigSelection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    convSSLXFPPortXCVTunableConfigSelection.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SPEEDSINGLELINE-XFP-MIB",
    **{"convSpeedSingleLineXFP": convSpeedSingleLineXFP,
       "convSSLXFPModuleOverviewTable": convSSLXFPModuleOverviewTable,
       "convSSLXFPModuleOverviewEntry": convSSLXFPModuleOverviewEntry,
       "convSSLXFPMSlot": convSSLXFPMSlot,
       "convSSLXFPMDevice": convSSLXFPMDevice,
       "convSSLXFPMStatus": convSSLXFPMStatus,
       "convSSLXFPMSysUpTime": convSSLXFPMSysUpTime,
       "convSSLXFPMTemp": convSSLXFPMTemp,
       "convSSLXFPMAlarmState": convSSLXFPMAlarmState,
       "convSSLXFPMSerialNumber": convSSLXFPMSerialNumber,
       "convSSLXFPModuleImagesOverviewTable": convSSLXFPModuleImagesOverviewTable,
       "convSSLXFPModuleImagesOverviewEntry": convSSLXFPModuleImagesOverviewEntry,
       "convSSLXFPSWSlot": convSSLXFPSWSlot,
       "convSSLXFPSWBootImage": convSSLXFPSWBootImage,
       "convSSLXFPSWAppImage1": convSSLXFPSWAppImage1,
       "convSSLXFPSWAppImage2": convSSLXFPSWAppImage2,
       "convSSLXFPSWUploadStatus": convSSLXFPSWUploadStatus,
       "convSSLXFPSWUpdateStatus": convSSLXFPSWUpdateStatus,
       "convSSLXFPMHWVersion": convSSLXFPMHWVersion,
       "convSSLXFPModuleBoardConfigTable": convSSLXFPModuleBoardConfigTable,
       "convSSLXFPModuleBoardConfigEntry": convSSLXFPModuleBoardConfigEntry,
       "convSSLXFPModuleSlot": convSSLXFPModuleSlot,
       "convSSLXFPModulePortSpeedConfig": convSSLXFPModulePortSpeedConfig,
       "convSSLXFPModuleTempHighWarning": convSSLXFPModuleTempHighWarning,
       "convSSLXFPModuleTempHighAlarm": convSSLXFPModuleTempHighAlarm,
       "convSSLXFPModuleCliTimeout": convSSLXFPModuleCliTimeout,
       "convSSLXFPModuleEthPortConfig": convSSLXFPModuleEthPortConfig,
       "convSSLXFPModuleEthPortState": convSSLXFPModuleEthPortState,
       "convSSLXFPPortOverviewTable": convSSLXFPPortOverviewTable,
       "convSSLXFPPortOverviewEntry": convSSLXFPPortOverviewEntry,
       "convSSLXFPMPortIndex": convSSLXFPMPortIndex,
       "convSSLXFPMPortSlot": convSSLXFPMPortSlot,
       "convSSLXFPMPortPort": convSSLXFPMPortPort,
       "convSSLXFPMPortDes": convSSLXFPMPortDes,
       "convSSLXFPMPortAdminState": convSSLXFPMPortAdminState,
       "convSSLXFPMPortXFPState": convSSLXFPMPortXFPState,
       "convSSLXFPMPortTXOperState": convSSLXFPMPortTXOperState,
       "convSSLXFPMPortRXOperState": convSSLXFPMPortRXOperState,
       "convSSLXFPMPortAlarmState": convSSLXFPMPortAlarmState,
       "convSSLXFPModulePortConfigTable": convSSLXFPModulePortConfigTable,
       "convSSLXFPModulePortConfigEntry": convSSLXFPModulePortConfigEntry,
       "convSSLXFPMPortConfIndex": convSSLXFPMPortConfIndex,
       "convSSLXFPMPortConfSlot": convSSLXFPMPortConfSlot,
       "convSSLXFPMPortConfPort": convSSLXFPMPortConfPort,
       "convSSLXFPMPortAdminConfig": convSSLXFPMPortAdminConfig,
       "convSSLXFPMPortDescription": convSSLXFPMPortDescription,
       "convSSLXFPMPortLLCFConfig": convSSLXFPMPortLLCFConfig,
       "convSSLXFPMPortLoopConfig": convSSLXFPMPortLoopConfig,
       "convSSLXFPMPortAlarmDeactivation": convSSLXFPMPortAlarmDeactivation,
       "convSSLXFPMPortAlarmSchedule": convSSLXFPMPortAlarmSchedule,
       "convSSLXFPMPortOTNConfig": convSSLXFPMPortOTNConfig,
       "convSSLXFPMPortOTNMapping": convSSLXFPMPortOTNMapping,
       "convSSLXFPModulePortGeneralXFPInfosTable": convSSLXFPModulePortGeneralXFPInfosTable,
       "convSSLXFPModulePortGeneralXFPInfosEntry": convSSLXFPModulePortGeneralXFPInfosEntry,
       "convSSLXFPMPortGenIndex": convSSLXFPMPortGenIndex,
       "convSSLXFPMPortGenSlot": convSSLXFPMPortGenSlot,
       "convSSLXFPMPortGenPort": convSSLXFPMPortGenPort,
       "convSSLXFPMPortXFPPowerclass": convSSLXFPMPortXFPPowerclass,
       "convSSLXFPMPortXFPSmFiberLength": convSSLXFPMPortXFPSmFiberLength,
       "convSSLXFPMPortVendorName": convSSLXFPMPortVendorName,
       "convSSLXFPMPortSerialNumber": convSSLXFPMPortSerialNumber,
       "convSSLXFPMPortWavelength": convSSLXFPMPortWavelength,
       "convSSLXFPMPortPartNumber": convSSLXFPMPortPartNumber,
       "convSSLXFPModulePortXFPMessurementTable": convSSLXFPModulePortXFPMessurementTable,
       "convSSLXFPModulePortXFPMessurementEntry": convSSLXFPModulePortXFPMessurementEntry,
       "convSSLXFPMPortMesIndex": convSSLXFPMPortMesIndex,
       "convSSLXFPMPortMesSlot": convSSLXFPMPortMesSlot,
       "convSSLXFPMPortMesPort": convSSLXFPMPortMesPort,
       "convSSLXFPMPortRxPower": convSSLXFPMPortRxPower,
       "convSSLXFPMPortTxPower": convSSLXFPMPortTxPower,
       "convSSLXFPMPortXFPTemp": convSSLXFPMPortXFPTemp,
       "convSSLXFPMPortTxBias": convSSLXFPMPortTxBias,
       "convSSLXFPMPortFECRate": convSSLXFPMPortFECRate,
       "convSSLXFPModuleThresholdsConfigTable": convSSLXFPModuleThresholdsConfigTable,
       "convSSLXFPModuleThresholdsConfigEntry": convSSLXFPModuleThresholdsConfigEntry,
       "convSSLXFPMPortThresIndex": convSSLXFPMPortThresIndex,
       "convSSLXFPMPortThresSlot": convSSLXFPMPortThresSlot,
       "convSSLXFPMPortThresPort": convSSLXFPMPortThresPort,
       "convSSLXFPMPortRxLowAlarmLevel": convSSLXFPMPortRxLowAlarmLevel,
       "convSSLXFPMPortRxHighAlarmLevel": convSSLXFPMPortRxHighAlarmLevel,
       "convSSLXFPMPortRxLowWarningLevel": convSSLXFPMPortRxLowWarningLevel,
       "convSSLXFPMPortRxHighWarningLevel": convSSLXFPMPortRxHighWarningLevel,
       "convSSLXFPMPortTxLowAlarmLevel": convSSLXFPMPortTxLowAlarmLevel,
       "convSSLXFPMPortTxHighAlarmLevel": convSSLXFPMPortTxHighAlarmLevel,
       "convSSLXFPMPortTxLowWarningLevel": convSSLXFPMPortTxLowWarningLevel,
       "convSSLXFPMPortTxHighWarningLevel": convSSLXFPMPortTxHighWarningLevel,
       "convSSLXFPMPortTxBiasLowAlarmLevel": convSSLXFPMPortTxBiasLowAlarmLevel,
       "convSSLXFPMPortTxBiasHighAlarmLevel": convSSLXFPMPortTxBiasHighAlarmLevel,
       "convSSLXFPMPortTxBiasLowWarningLevel": convSSLXFPMPortTxBiasLowWarningLevel,
       "convSSLXFPMPortTxBiasHighWarningLevel": convSSLXFPMPortTxBiasHighWarningLevel,
       "convSSLXFPMPortTempLowAlarmLevel": convSSLXFPMPortTempLowAlarmLevel,
       "convSSLXFPMPortTempHighAlarmLevel": convSSLXFPMPortTempHighAlarmLevel,
       "convSSLXFPMPortTempLowWarningLevel": convSSLXFPMPortTempLowWarningLevel,
       "convSSLXFPMPortTempHighWarningLevel": convSSLXFPMPortTempHighWarningLevel,
       "convSSLXFPModuleEventTable": convSSLXFPModuleEventTable,
       "convSSLXFPModuleEventEntry": convSSLXFPModuleEventEntry,
       "convSSLXFPPIndex": convSSLXFPPIndex,
       "convSSLXFPPSlot": convSSLXFPPSlot,
       "convSSLXFPPPort": convSSLXFPPPort,
       "convSSLXFPPPortRxLowAlarmEvent": convSSLXFPPPortRxLowAlarmEvent,
       "convSSLXFPPPortRxHighAlarmEvent": convSSLXFPPPortRxHighAlarmEvent,
       "convSSLXFPPPortRxLowWarningEvent": convSSLXFPPPortRxLowWarningEvent,
       "convSSLXFPPPortRxHighWarningEvent": convSSLXFPPPortRxHighWarningEvent,
       "convSSLXFPPPortTxLowAlarmEvent": convSSLXFPPPortTxLowAlarmEvent,
       "convSSLXFPPPortTxHighAlarmEvent": convSSLXFPPPortTxHighAlarmEvent,
       "convSSLXFPPPortTxLowWarningEvent": convSSLXFPPPortTxLowWarningEvent,
       "convSSLXFPPPortTxHighWarningEvent": convSSLXFPPPortTxHighWarningEvent,
       "convSSLXFPPPortTxBiasLowAlarmEvent": convSSLXFPPPortTxBiasLowAlarmEvent,
       "convSSLXFPPPortTxBiasHighAlarmEvent": convSSLXFPPPortTxBiasHighAlarmEvent,
       "convSSLXFPPPortTxBiasLowWarningEvent": convSSLXFPPPortTxBiasLowWarningEvent,
       "convSSLXFPPPortTxBiasHighWarningEvent": convSSLXFPPPortTxBiasHighWarningEvent,
       "convSSLXFPPPortTempLowAlarmEvent": convSSLXFPPPortTempLowAlarmEvent,
       "convSSLXFPPPortTempHighAlarmEvent": convSSLXFPPPortTempHighAlarmEvent,
       "convSSLXFPPPortTempLowWarningEvent": convSSLXFPPPortTempLowWarningEvent,
       "convSSLXFPPPortTempHighWarningEvent": convSSLXFPPPortTempHighWarningEvent,
       "convSSLXFPPPortOtnAlarmEvent": convSSLXFPPPortOtnAlarmEvent,
       "convSSLXFPPortTunableTable": convSSLXFPPortTunableTable,
       "convSSLXFPPortTunableEntry": convSSLXFPPortTunableEntry,
       "convSSLXFPPortXCVIndex": convSSLXFPPortXCVIndex,
       "convSSLXFPPortXCVSlot": convSSLXFPPortXCVSlot,
       "convSSLXFPPortXCVPort": convSSLXFPPortXCVPort,
       "convSSLXFPPortXCVChannelSpacing": convSSLXFPPortXCVChannelSpacing,
       "convSSLXFPPortXCVNumberOfChannels": convSSLXFPPortXCVNumberOfChannels,
       "convSSLXFPPortXCVCenterWavlength": convSSLXFPPortXCVCenterWavlength,
       "convSSLXFPPortXCVTunableFeature": convSSLXFPPortXCVTunableFeature,
       "convSSLXFPPortXCVTunableMinMaxChannel": convSSLXFPPortXCVTunableMinMaxChannel,
       "convSSLXFPPortXCVTunableWavelengthConfig": convSSLXFPPortXCVTunableWavelengthConfig,
       "convSSLXFPPortXCVTunableChannelConfig": convSSLXFPPortXCVTunableChannelConfig,
       "convSSLXFPPortXCVTunableConfigSelection": convSSLXFPPortXCVTunableConfigSelection}
)
