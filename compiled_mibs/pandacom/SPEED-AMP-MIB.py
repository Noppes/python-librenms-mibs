# SNMP MIB module (SPEED-AMP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\pandacom\SPEED-AMP-MIB

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

(amplifier,) = mibBuilder.importSymbols(
    "SPEEDCARRIER-MIB",
    "amplifier")


# MODULE-IDENTITY

speedAmp = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 3652, 3, 5, 1)
)
if mibBuilder.loadTexts:
    speedAmp.setRevisions(
        ("2020-10-07 00:00",
         "2019-04-25 00:00",
         "2017-12-07 00:00",
         "2017-08-16 00:00",
         "2013-12-12 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_SpeedAmpModuleOverviewTable_Object = MibTable
speedAmpModuleOverviewTable = _SpeedAmpModuleOverviewTable_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 5, 1, 1)
)
if mibBuilder.loadTexts:
    speedAmpModuleOverviewTable.setStatus("current")
_SpeedAmpModuleOverviewEntry_Object = MibTableRow
speedAmpModuleOverviewEntry = _SpeedAmpModuleOverviewEntry_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 5, 1, 1, 1)
)
speedAmpModuleOverviewEntry.setIndexNames(
    (0, "SPEED-AMP-MIB", "speedAmpMSlot"),
)
if mibBuilder.loadTexts:
    speedAmpModuleOverviewEntry.setStatus("current")


class _SpeedAmpMSlot_Type(Integer32):
    """Custom type speedAmpMSlot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 19),
    )


_SpeedAmpMSlot_Type.__name__ = "Integer32"
_SpeedAmpMSlot_Object = MibTableColumn
speedAmpMSlot = _SpeedAmpMSlot_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 5, 1, 1, 1, 2),
    _SpeedAmpMSlot_Type()
)
speedAmpMSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    speedAmpMSlot.setStatus("current")


class _SpeedAmpMDevice_Type(Integer32):
    """Custom type speedAmpMDevice based on Integer32"""
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
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19,
              20,
              21,
              22,
              23,
              24,
              25,
              255)
        )
    )
    namedValues = NamedValues(
        *(("notAvailable", 0),
          ("other", 1),
          ("preamp14", 2),
          ("booster17", 3),
          ("booster17OSC", 4),
          ("booster23OSC", 5),
          ("inline17", 6),
          ("inline23", 7),
          ("ramanMaster10", 8),
          ("ramanMaster15", 9),
          ("ramanSlave10", 10),
          ("ramanSlave15", 11),
          ("ramanStandalone10", 12),
          ("ramanStandalone15", 13),
          ("preamp14ext", 14),
          ("booster17ext", 15),
          ("booster17OSCext", 16),
          ("booster23OSCext", 17),
          ("inline17ext", 18),
          ("inline23ext", 19),
          ("preamp14H", 20),
          ("preamp14extH", 21),
          ("booster17H", 22),
          ("booster17extH", 23),
          ("booster20H", 24),
          ("booster20extH", 25),
          ("unknown", 255))
    )


_SpeedAmpMDevice_Type.__name__ = "Integer32"
_SpeedAmpMDevice_Object = MibTableColumn
speedAmpMDevice = _SpeedAmpMDevice_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 5, 1, 1, 1, 3),
    _SpeedAmpMDevice_Type()
)
speedAmpMDevice.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    speedAmpMDevice.setStatus("current")


class _SpeedAmpMStatus_Type(Integer32):
    """Custom type speedAmpMStatus based on Integer32"""
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
        *(("notAvailable", 0),
          ("running", 1),
          ("resetSoftware", 2),
          ("resetConfig", 3),
          ("resetCAN", 4),
          ("resetHardware", 5),
          ("resetStatistic", 6),
          ("unknown", 255))
    )


_SpeedAmpMStatus_Type.__name__ = "Integer32"
_SpeedAmpMStatus_Object = MibTableColumn
speedAmpMStatus = _SpeedAmpMStatus_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 5, 1, 1, 1, 4),
    _SpeedAmpMStatus_Type()
)
speedAmpMStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    speedAmpMStatus.setStatus("current")
_SpeedAmpMSysUpTime_Type = TimeTicks
_SpeedAmpMSysUpTime_Object = MibTableColumn
speedAmpMSysUpTime = _SpeedAmpMSysUpTime_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 5, 1, 1, 1, 5),
    _SpeedAmpMSysUpTime_Type()
)
speedAmpMSysUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    speedAmpMSysUpTime.setStatus("current")
_SpeedAmpMTemp_Type = Integer32
_SpeedAmpMTemp_Object = MibTableColumn
speedAmpMTemp = _SpeedAmpMTemp_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 5, 1, 1, 1, 6),
    _SpeedAmpMTemp_Type()
)
speedAmpMTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    speedAmpMTemp.setStatus("current")


class _SpeedAmpMAlarmState_Type(Integer32):
    """Custom type speedAmpMAlarmState based on Integer32"""
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
        *(("notAvailable", 0),
          ("noAlarm", 1),
          ("activeAlarms", 2),
          ("unknown", 255))
    )


_SpeedAmpMAlarmState_Type.__name__ = "Integer32"
_SpeedAmpMAlarmState_Object = MibTableColumn
speedAmpMAlarmState = _SpeedAmpMAlarmState_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 5, 1, 1, 1, 7),
    _SpeedAmpMAlarmState_Type()
)
speedAmpMAlarmState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    speedAmpMAlarmState.setStatus("current")


class _SpeedAmpMSerialNumber_Type(DisplayString):
    """Custom type speedAmpMSerialNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 17),
    )


_SpeedAmpMSerialNumber_Type.__name__ = "DisplayString"
_SpeedAmpMSerialNumber_Object = MibTableColumn
speedAmpMSerialNumber = _SpeedAmpMSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 5, 1, 1, 1, 8),
    _SpeedAmpMSerialNumber_Type()
)
speedAmpMSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    speedAmpMSerialNumber.setStatus("current")
_SpeedAmpModuleImagesOverviewTable_Object = MibTable
speedAmpModuleImagesOverviewTable = _SpeedAmpModuleImagesOverviewTable_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 5, 1, 2)
)
if mibBuilder.loadTexts:
    speedAmpModuleImagesOverviewTable.setStatus("current")
_SpeedAmpModuleImagesOverviewEntry_Object = MibTableRow
speedAmpModuleImagesOverviewEntry = _SpeedAmpModuleImagesOverviewEntry_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 5, 1, 2, 1)
)
speedAmpModuleImagesOverviewEntry.setIndexNames(
    (0, "SPEED-AMP-MIB", "speedAmpSWSlot"),
)
if mibBuilder.loadTexts:
    speedAmpModuleImagesOverviewEntry.setStatus("current")


class _SpeedAmpSWSlot_Type(Integer32):
    """Custom type speedAmpSWSlot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 19),
    )


_SpeedAmpSWSlot_Type.__name__ = "Integer32"
_SpeedAmpSWSlot_Object = MibTableColumn
speedAmpSWSlot = _SpeedAmpSWSlot_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 5, 1, 2, 1, 2),
    _SpeedAmpSWSlot_Type()
)
speedAmpSWSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    speedAmpSWSlot.setStatus("current")


class _SpeedAmpSwKernelImage_Type(DisplayString):
    """Custom type speedAmpSwKernelImage based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_SpeedAmpSwKernelImage_Type.__name__ = "DisplayString"
_SpeedAmpSwKernelImage_Object = MibTableColumn
speedAmpSwKernelImage = _SpeedAmpSwKernelImage_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 5, 1, 2, 1, 3),
    _SpeedAmpSwKernelImage_Type()
)
speedAmpSwKernelImage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    speedAmpSwKernelImage.setStatus("current")


class _SpeedAmpSwAppImage_Type(DisplayString):
    """Custom type speedAmpSwAppImage based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_SpeedAmpSwAppImage_Type.__name__ = "DisplayString"
_SpeedAmpSwAppImage_Object = MibTableColumn
speedAmpSwAppImage = _SpeedAmpSwAppImage_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 5, 1, 2, 1, 4),
    _SpeedAmpSwAppImage_Type()
)
speedAmpSwAppImage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    speedAmpSwAppImage.setStatus("current")


class _SpeedAmpSwUploadStatus_Type(Integer32):
    """Custom type speedAmpSwUploadStatus based on Integer32"""
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
        *(("notAvailable", 0),
          ("ready", 1),
          ("startUpload", 2),
          ("uploadActive", 3),
          ("uploadFailure", 4),
          ("unknown", 255))
    )


_SpeedAmpSwUploadStatus_Type.__name__ = "Integer32"
_SpeedAmpSwUploadStatus_Object = MibTableColumn
speedAmpSwUploadStatus = _SpeedAmpSwUploadStatus_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 5, 1, 2, 1, 5),
    _SpeedAmpSwUploadStatus_Type()
)
speedAmpSwUploadStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    speedAmpSwUploadStatus.setStatus("current")


class _SpeedAmpSwUpdateStatus_Type(Integer32):
    """Custom type speedAmpSwUpdateStatus based on Integer32"""
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
          ("idle", 1),
          ("activateKernel", 2),
          ("activateApplication", 3),
          ("unknown", 255))
    )


_SpeedAmpSwUpdateStatus_Type.__name__ = "Integer32"
_SpeedAmpSwUpdateStatus_Object = MibTableColumn
speedAmpSwUpdateStatus = _SpeedAmpSwUpdateStatus_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 5, 1, 2, 1, 6),
    _SpeedAmpSwUpdateStatus_Type()
)
speedAmpSwUpdateStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    speedAmpSwUpdateStatus.setStatus("current")


class _SpeedAmpHwVersion_Type(DisplayString):
    """Custom type speedAmpHwVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 17),
    )


_SpeedAmpHwVersion_Type.__name__ = "DisplayString"
_SpeedAmpHwVersion_Object = MibTableColumn
speedAmpHwVersion = _SpeedAmpHwVersion_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 5, 1, 2, 1, 7),
    _SpeedAmpHwVersion_Type()
)
speedAmpHwVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    speedAmpHwVersion.setStatus("current")
_SpeedAmpModuleBoardConfigTable_Object = MibTable
speedAmpModuleBoardConfigTable = _SpeedAmpModuleBoardConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 5, 1, 3)
)
if mibBuilder.loadTexts:
    speedAmpModuleBoardConfigTable.setStatus("current")
_SpeedAmpModuleBoardConfigEntry_Object = MibTableRow
speedAmpModuleBoardConfigEntry = _SpeedAmpModuleBoardConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 5, 1, 3, 1)
)
speedAmpModuleBoardConfigEntry.setIndexNames(
    (0, "SPEED-AMP-MIB", "speedAmpTemperatureSlot"),
)
if mibBuilder.loadTexts:
    speedAmpModuleBoardConfigEntry.setStatus("current")


class _SpeedAmpTemperatureSlot_Type(Integer32):
    """Custom type speedAmpTemperatureSlot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 19),
    )


_SpeedAmpTemperatureSlot_Type.__name__ = "Integer32"
_SpeedAmpTemperatureSlot_Object = MibTableColumn
speedAmpTemperatureSlot = _SpeedAmpTemperatureSlot_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 5, 1, 3, 1, 2),
    _SpeedAmpTemperatureSlot_Type()
)
speedAmpTemperatureSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    speedAmpTemperatureSlot.setStatus("current")


class _SpeedAmpTemperatureHighWarning_Type(Integer32):
    """Custom type speedAmpTemperatureHighWarning based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 60),
    )


_SpeedAmpTemperatureHighWarning_Type.__name__ = "Integer32"
_SpeedAmpTemperatureHighWarning_Object = MibTableColumn
speedAmpTemperatureHighWarning = _SpeedAmpTemperatureHighWarning_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 5, 1, 3, 1, 3),
    _SpeedAmpTemperatureHighWarning_Type()
)
speedAmpTemperatureHighWarning.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    speedAmpTemperatureHighWarning.setStatus("current")
_SpeedAmpTemperatureHighAlarm_Type = Integer32
_SpeedAmpTemperatureHighAlarm_Object = MibTableColumn
speedAmpTemperatureHighAlarm = _SpeedAmpTemperatureHighAlarm_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 5, 1, 3, 1, 4),
    _SpeedAmpTemperatureHighAlarm_Type()
)
speedAmpTemperatureHighAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    speedAmpTemperatureHighAlarm.setStatus("current")
_SpeedAmpModuleNetworkParameterTable_Object = MibTable
speedAmpModuleNetworkParameterTable = _SpeedAmpModuleNetworkParameterTable_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 5, 1, 4)
)
if mibBuilder.loadTexts:
    speedAmpModuleNetworkParameterTable.setStatus("current")
_SpeedAmpModuleNetworkParameterEntry_Object = MibTableRow
speedAmpModuleNetworkParameterEntry = _SpeedAmpModuleNetworkParameterEntry_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 5, 1, 4, 1)
)
speedAmpModuleNetworkParameterEntry.setIndexNames(
    (0, "SPEED-AMP-MIB", "speedAmpMNetworkSlot"),
)
if mibBuilder.loadTexts:
    speedAmpModuleNetworkParameterEntry.setStatus("current")


class _SpeedAmpMNetworkSlot_Type(Integer32):
    """Custom type speedAmpMNetworkSlot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 19),
    )


_SpeedAmpMNetworkSlot_Type.__name__ = "Integer32"
_SpeedAmpMNetworkSlot_Object = MibTableColumn
speedAmpMNetworkSlot = _SpeedAmpMNetworkSlot_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 5, 1, 4, 1, 2),
    _SpeedAmpMNetworkSlot_Type()
)
speedAmpMNetworkSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    speedAmpMNetworkSlot.setStatus("current")


class _SpeedAmpMNetworkAdress_Type(IpAddress):
    """Custom type speedAmpMNetworkAdress based on IpAddress"""
    defaultHexValue = "c0a80065"


_SpeedAmpMNetworkAdress_Type.__name__ = "IpAddress"
_SpeedAmpMNetworkAdress_Object = MibTableColumn
speedAmpMNetworkAdress = _SpeedAmpMNetworkAdress_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 5, 1, 4, 1, 3),
    _SpeedAmpMNetworkAdress_Type()
)
speedAmpMNetworkAdress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    speedAmpMNetworkAdress.setStatus("current")


class _SpeedAmpMNetworkMask_Type(IpAddress):
    """Custom type speedAmpMNetworkMask based on IpAddress"""
    defaultHexValue = "ffffff00"


_SpeedAmpMNetworkMask_Type.__name__ = "IpAddress"
_SpeedAmpMNetworkMask_Object = MibTableColumn
speedAmpMNetworkMask = _SpeedAmpMNetworkMask_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 5, 1, 4, 1, 4),
    _SpeedAmpMNetworkMask_Type()
)
speedAmpMNetworkMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    speedAmpMNetworkMask.setStatus("current")


class _SpeedAmpMNetworkGateway_Type(IpAddress):
    """Custom type speedAmpMNetworkGateway based on IpAddress"""
    defaultHexValue = "00000000"


_SpeedAmpMNetworkGateway_Type.__name__ = "IpAddress"
_SpeedAmpMNetworkGateway_Object = MibTableColumn
speedAmpMNetworkGateway = _SpeedAmpMNetworkGateway_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 5, 1, 4, 1, 5),
    _SpeedAmpMNetworkGateway_Type()
)
speedAmpMNetworkGateway.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    speedAmpMNetworkGateway.setStatus("current")


class _SpeedAmpMNetworkSnmpTrapSink1_Type(IpAddress):
    """Custom type speedAmpMNetworkSnmpTrapSink1 based on IpAddress"""
    defaultHexValue = "00000000"


_SpeedAmpMNetworkSnmpTrapSink1_Type.__name__ = "IpAddress"
_SpeedAmpMNetworkSnmpTrapSink1_Object = MibTableColumn
speedAmpMNetworkSnmpTrapSink1 = _SpeedAmpMNetworkSnmpTrapSink1_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 5, 1, 4, 1, 6),
    _SpeedAmpMNetworkSnmpTrapSink1_Type()
)
speedAmpMNetworkSnmpTrapSink1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    speedAmpMNetworkSnmpTrapSink1.setStatus("current")


class _SpeedAmpMNetworkSnmpTrapSink2_Type(IpAddress):
    """Custom type speedAmpMNetworkSnmpTrapSink2 based on IpAddress"""
    defaultHexValue = "00000000"


_SpeedAmpMNetworkSnmpTrapSink2_Type.__name__ = "IpAddress"
_SpeedAmpMNetworkSnmpTrapSink2_Object = MibTableColumn
speedAmpMNetworkSnmpTrapSink2 = _SpeedAmpMNetworkSnmpTrapSink2_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 5, 1, 4, 1, 7),
    _SpeedAmpMNetworkSnmpTrapSink2_Type()
)
speedAmpMNetworkSnmpTrapSink2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    speedAmpMNetworkSnmpTrapSink2.setStatus("current")


class _SpeedAmpMNetworkSnmpTrapSink3_Type(IpAddress):
    """Custom type speedAmpMNetworkSnmpTrapSink3 based on IpAddress"""
    defaultHexValue = "00000000"


_SpeedAmpMNetworkSnmpTrapSink3_Type.__name__ = "IpAddress"
_SpeedAmpMNetworkSnmpTrapSink3_Object = MibTableColumn
speedAmpMNetworkSnmpTrapSink3 = _SpeedAmpMNetworkSnmpTrapSink3_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 5, 1, 4, 1, 8),
    _SpeedAmpMNetworkSnmpTrapSink3_Type()
)
speedAmpMNetworkSnmpTrapSink3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    speedAmpMNetworkSnmpTrapSink3.setStatus("current")


class _SpeedAmpMNetworkSnmpTrapSink4_Type(IpAddress):
    """Custom type speedAmpMNetworkSnmpTrapSink4 based on IpAddress"""
    defaultHexValue = "00000000"


_SpeedAmpMNetworkSnmpTrapSink4_Type.__name__ = "IpAddress"
_SpeedAmpMNetworkSnmpTrapSink4_Object = MibTableColumn
speedAmpMNetworkSnmpTrapSink4 = _SpeedAmpMNetworkSnmpTrapSink4_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 5, 1, 4, 1, 9),
    _SpeedAmpMNetworkSnmpTrapSink4_Type()
)
speedAmpMNetworkSnmpTrapSink4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    speedAmpMNetworkSnmpTrapSink4.setStatus("current")


class _SpeedAmpMNetworkSnmpTrapSink5_Type(IpAddress):
    """Custom type speedAmpMNetworkSnmpTrapSink5 based on IpAddress"""
    defaultHexValue = "00000000"


_SpeedAmpMNetworkSnmpTrapSink5_Type.__name__ = "IpAddress"
_SpeedAmpMNetworkSnmpTrapSink5_Object = MibTableColumn
speedAmpMNetworkSnmpTrapSink5 = _SpeedAmpMNetworkSnmpTrapSink5_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 5, 1, 4, 1, 10),
    _SpeedAmpMNetworkSnmpTrapSink5_Type()
)
speedAmpMNetworkSnmpTrapSink5.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    speedAmpMNetworkSnmpTrapSink5.setStatus("current")


class _SpeedAmpMNetworkSnmpReadCommunity_Type(DisplayString):
    """Custom type speedAmpMNetworkSnmpReadCommunity based on DisplayString"""
    defaultValue = OctetString("public")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_SpeedAmpMNetworkSnmpReadCommunity_Type.__name__ = "DisplayString"
_SpeedAmpMNetworkSnmpReadCommunity_Object = MibTableColumn
speedAmpMNetworkSnmpReadCommunity = _SpeedAmpMNetworkSnmpReadCommunity_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 5, 1, 4, 1, 11),
    _SpeedAmpMNetworkSnmpReadCommunity_Type()
)
speedAmpMNetworkSnmpReadCommunity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    speedAmpMNetworkSnmpReadCommunity.setStatus("current")


class _SpeedAmpMNetworkSnmpWriteCommunity_Type(DisplayString):
    """Custom type speedAmpMNetworkSnmpWriteCommunity based on DisplayString"""
    defaultValue = OctetString("private")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_SpeedAmpMNetworkSnmpWriteCommunity_Type.__name__ = "DisplayString"
_SpeedAmpMNetworkSnmpWriteCommunity_Object = MibTableColumn
speedAmpMNetworkSnmpWriteCommunity = _SpeedAmpMNetworkSnmpWriteCommunity_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 5, 1, 4, 1, 12),
    _SpeedAmpMNetworkSnmpWriteCommunity_Type()
)
speedAmpMNetworkSnmpWriteCommunity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    speedAmpMNetworkSnmpWriteCommunity.setStatus("current")


class _SpeedAmpMNetworkSysLocation_Type(DisplayString):
    """Custom type speedAmpMNetworkSysLocation based on DisplayString"""
    defaultValue = OctetString("serverroom")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_SpeedAmpMNetworkSysLocation_Type.__name__ = "DisplayString"
_SpeedAmpMNetworkSysLocation_Object = MibTableColumn
speedAmpMNetworkSysLocation = _SpeedAmpMNetworkSysLocation_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 5, 1, 4, 1, 13),
    _SpeedAmpMNetworkSysLocation_Type()
)
speedAmpMNetworkSysLocation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    speedAmpMNetworkSysLocation.setStatus("current")


class _SpeedAmpMNetworkSnmpAgentStatus_Type(Integer32):
    """Custom type speedAmpMNetworkSnmpAgentStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              254,
              255)
        )
    )
    namedValues = NamedValues(
        *(("notAvailable", 0),
          ("down", 1),
          ("up", 2),
          ("notImplemented", 254),
          ("unknown", 255))
    )


_SpeedAmpMNetworkSnmpAgentStatus_Type.__name__ = "Integer32"
_SpeedAmpMNetworkSnmpAgentStatus_Object = MibTableColumn
speedAmpMNetworkSnmpAgentStatus = _SpeedAmpMNetworkSnmpAgentStatus_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 5, 1, 4, 1, 14),
    _SpeedAmpMNetworkSnmpAgentStatus_Type()
)
speedAmpMNetworkSnmpAgentStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    speedAmpMNetworkSnmpAgentStatus.setStatus("current")


class _SpeedAmpMNetworkHttpServerStatus_Type(Integer32):
    """Custom type speedAmpMNetworkHttpServerStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              254,
              255)
        )
    )
    namedValues = NamedValues(
        *(("notAvailable", 0),
          ("down", 1),
          ("up", 2),
          ("notImplemented", 254),
          ("unknown", 255))
    )


_SpeedAmpMNetworkHttpServerStatus_Type.__name__ = "Integer32"
_SpeedAmpMNetworkHttpServerStatus_Object = MibTableColumn
speedAmpMNetworkHttpServerStatus = _SpeedAmpMNetworkHttpServerStatus_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 5, 1, 4, 1, 15),
    _SpeedAmpMNetworkHttpServerStatus_Type()
)
speedAmpMNetworkHttpServerStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    speedAmpMNetworkHttpServerStatus.setStatus("current")


class _SpeedAmpMNetworkSysname_Type(DisplayString):
    """Custom type speedAmpMNetworkSysname based on DisplayString"""
    defaultValue = OctetString("serverroom")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_SpeedAmpMNetworkSysname_Type.__name__ = "DisplayString"
_SpeedAmpMNetworkSysname_Object = MibTableColumn
speedAmpMNetworkSysname = _SpeedAmpMNetworkSysname_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 5, 1, 4, 1, 16),
    _SpeedAmpMNetworkSysname_Type()
)
speedAmpMNetworkSysname.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    speedAmpMNetworkSysname.setStatus("current")


class _SpeedAmpNNetworkSyscontact_Type(DisplayString):
    """Custom type speedAmpNNetworkSyscontact based on DisplayString"""
    defaultValue = OctetString("serverroom")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_SpeedAmpNNetworkSyscontact_Type.__name__ = "DisplayString"
_SpeedAmpNNetworkSyscontact_Object = MibTableColumn
speedAmpNNetworkSyscontact = _SpeedAmpNNetworkSyscontact_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 5, 1, 4, 1, 17),
    _SpeedAmpNNetworkSyscontact_Type()
)
speedAmpNNetworkSyscontact.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    speedAmpNNetworkSyscontact.setStatus("current")


class _SpeedAmpMNetworkUserTimeout_Type(Integer32):
    """Custom type speedAmpMNetworkUserTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(120, 3600),
    )


_SpeedAmpMNetworkUserTimeout_Type.__name__ = "Integer32"
_SpeedAmpMNetworkUserTimeout_Object = MibTableColumn
speedAmpMNetworkUserTimeout = _SpeedAmpMNetworkUserTimeout_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 5, 1, 4, 1, 18),
    _SpeedAmpMNetworkUserTimeout_Type()
)
speedAmpMNetworkUserTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    speedAmpMNetworkUserTimeout.setStatus("current")


class _SpeedAmpMNetworkAccess_Type(Integer32):
    """Custom type speedAmpMNetworkAccess based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              254,
              255)
        )
    )
    namedValues = NamedValues(
        *(("notavailable", 0),
          ("off", 1),
          ("telnet", 2),
          ("ssh2", 3),
          ("notImplemented", 254),
          ("unknown", 255))
    )


_SpeedAmpMNetworkAccess_Type.__name__ = "Integer32"
_SpeedAmpMNetworkAccess_Object = MibTableColumn
speedAmpMNetworkAccess = _SpeedAmpMNetworkAccess_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 5, 1, 4, 1, 19),
    _SpeedAmpMNetworkAccess_Type()
)
speedAmpMNetworkAccess.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    speedAmpMNetworkAccess.setStatus("current")
_SpeedAmpModuleEthPortOverviewTable_Object = MibTable
speedAmpModuleEthPortOverviewTable = _SpeedAmpModuleEthPortOverviewTable_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 5, 1, 5)
)
if mibBuilder.loadTexts:
    speedAmpModuleEthPortOverviewTable.setStatus("current")
_SpeedAmpModuleEthPortOverviewEntry_Object = MibTableRow
speedAmpModuleEthPortOverviewEntry = _SpeedAmpModuleEthPortOverviewEntry_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 5, 1, 5, 1)
)
speedAmpModuleEthPortOverviewEntry.setIndexNames(
    (0, "SPEED-AMP-MIB", "speedAmpMEthIndex"),
)
if mibBuilder.loadTexts:
    speedAmpModuleEthPortOverviewEntry.setStatus("current")


class _SpeedAmpMEthIndex_Type(Integer32):
    """Custom type speedAmpMEthIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1900),
    )


_SpeedAmpMEthIndex_Type.__name__ = "Integer32"
_SpeedAmpMEthIndex_Object = MibTableColumn
speedAmpMEthIndex = _SpeedAmpMEthIndex_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 5, 1, 5, 1, 1),
    _SpeedAmpMEthIndex_Type()
)
speedAmpMEthIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    speedAmpMEthIndex.setStatus("current")


class _SpeedAmpMEthSlot_Type(Integer32):
    """Custom type speedAmpMEthSlot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 19),
    )


_SpeedAmpMEthSlot_Type.__name__ = "Integer32"
_SpeedAmpMEthSlot_Object = MibTableColumn
speedAmpMEthSlot = _SpeedAmpMEthSlot_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 5, 1, 5, 1, 2),
    _SpeedAmpMEthSlot_Type()
)
speedAmpMEthSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    speedAmpMEthSlot.setStatus("current")


class _SpeedAmpMEthPort_Type(Integer32):
    """Custom type speedAmpMEthPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5),
    )


_SpeedAmpMEthPort_Type.__name__ = "Integer32"
_SpeedAmpMEthPort_Object = MibTableColumn
speedAmpMEthPort = _SpeedAmpMEthPort_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 5, 1, 5, 1, 3),
    _SpeedAmpMEthPort_Type()
)
speedAmpMEthPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    speedAmpMEthPort.setStatus("current")


class _SpeedAmpMEthPortname_Type(DisplayString):
    """Custom type speedAmpMEthPortname based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_SpeedAmpMEthPortname_Type.__name__ = "DisplayString"
_SpeedAmpMEthPortname_Object = MibTableColumn
speedAmpMEthPortname = _SpeedAmpMEthPortname_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 5, 1, 5, 1, 4),
    _SpeedAmpMEthPortname_Type()
)
speedAmpMEthPortname.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    speedAmpMEthPortname.setStatus("current")


class _SpeedAmpMEthPortAdminState_Type(Integer32):
    """Custom type speedAmpMEthPortAdminState based on Integer32"""
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
        *(("notAvailable", 0),
          ("adminDown", 1),
          ("adminUp", 2),
          ("unknown", 255))
    )


_SpeedAmpMEthPortAdminState_Type.__name__ = "Integer32"
_SpeedAmpMEthPortAdminState_Object = MibTableColumn
speedAmpMEthPortAdminState = _SpeedAmpMEthPortAdminState_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 5, 1, 5, 1, 5),
    _SpeedAmpMEthPortAdminState_Type()
)
speedAmpMEthPortAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    speedAmpMEthPortAdminState.setStatus("current")


class _SpeedAmpMEthPortOperState_Type(Integer32):
    """Custom type speedAmpMEthPortOperState based on Integer32"""
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
        *(("notAvailable", 0),
          ("down", 1),
          ("up", 2),
          ("unknown", 255))
    )


_SpeedAmpMEthPortOperState_Type.__name__ = "Integer32"
_SpeedAmpMEthPortOperState_Object = MibTableColumn
speedAmpMEthPortOperState = _SpeedAmpMEthPortOperState_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 5, 1, 5, 1, 6),
    _SpeedAmpMEthPortOperState_Type()
)
speedAmpMEthPortOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    speedAmpMEthPortOperState.setStatus("current")


class _SpeedAmpMEthPortMode_Type(Integer32):
    """Custom type speedAmpMEthPortMode based on Integer32"""
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
              255)
        )
    )
    namedValues = NamedValues(
        *(("notAvailable", 0),
          ("autoneg", 1),
          ("hdx10", 2),
          ("fdx10", 3),
          ("hdx100", 4),
          ("fdx100", 5),
          ("hdlc", 6),
          ("rmii", 7),
          ("unknown", 255))
    )


_SpeedAmpMEthPortMode_Type.__name__ = "Integer32"
_SpeedAmpMEthPortMode_Object = MibTableColumn
speedAmpMEthPortMode = _SpeedAmpMEthPortMode_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 5, 1, 5, 1, 7),
    _SpeedAmpMEthPortMode_Type()
)
speedAmpMEthPortMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    speedAmpMEthPortMode.setStatus("current")


class _SpeedAmpMEthSFPState_Type(Integer32):
    """Custom type speedAmpMEthSFPState based on Integer32"""
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
        *(("notAvailable", 0),
          ("sfpOperDown", 1),
          ("sfpOperUp", 2),
          ("sfpTxFault", 3),
          ("sfpInstalled", 4),
          ("sfpRemoved", 5),
          ("sfpNotPossible", 6),
          ("unknown", 255))
    )


_SpeedAmpMEthSFPState_Type.__name__ = "Integer32"
_SpeedAmpMEthSFPState_Object = MibTableColumn
speedAmpMEthSFPState = _SpeedAmpMEthSFPState_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 5, 1, 5, 1, 8),
    _SpeedAmpMEthSFPState_Type()
)
speedAmpMEthSFPState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    speedAmpMEthSFPState.setStatus("current")
_SpeedAmpMEthPortRxPackets_Type = Integer32
_SpeedAmpMEthPortRxPackets_Object = MibTableColumn
speedAmpMEthPortRxPackets = _SpeedAmpMEthPortRxPackets_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 5, 1, 5, 1, 9),
    _SpeedAmpMEthPortRxPackets_Type()
)
speedAmpMEthPortRxPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    speedAmpMEthPortRxPackets.setStatus("current")
_SpeedAmpMEthPortTxPackets_Type = Integer32
_SpeedAmpMEthPortTxPackets_Object = MibTableColumn
speedAmpMEthPortTxPackets = _SpeedAmpMEthPortTxPackets_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 5, 1, 5, 1, 10),
    _SpeedAmpMEthPortTxPackets_Type()
)
speedAmpMEthPortTxPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    speedAmpMEthPortTxPackets.setStatus("current")
_SpeedAmpMEthErrors_Type = Integer32
_SpeedAmpMEthErrors_Object = MibTableColumn
speedAmpMEthErrors = _SpeedAmpMEthErrors_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 5, 1, 5, 1, 11),
    _SpeedAmpMEthErrors_Type()
)
speedAmpMEthErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    speedAmpMEthErrors.setStatus("current")
_SpeedAmpMEthPortConfigTable_Object = MibTable
speedAmpMEthPortConfigTable = _SpeedAmpMEthPortConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 5, 1, 6)
)
if mibBuilder.loadTexts:
    speedAmpMEthPortConfigTable.setStatus("current")
_SpeedAmpMEthPortConfigEntry_Object = MibTableRow
speedAmpMEthPortConfigEntry = _SpeedAmpMEthPortConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 5, 1, 6, 1)
)
speedAmpMEthPortConfigEntry.setIndexNames(
    (0, "SPEED-AMP-MIB", "speedAmpMEthPCfgIndex"),
)
if mibBuilder.loadTexts:
    speedAmpMEthPortConfigEntry.setStatus("current")


class _SpeedAmpMEthPCfgIndex_Type(Integer32):
    """Custom type speedAmpMEthPCfgIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1900),
    )


_SpeedAmpMEthPCfgIndex_Type.__name__ = "Integer32"
_SpeedAmpMEthPCfgIndex_Object = MibTableColumn
speedAmpMEthPCfgIndex = _SpeedAmpMEthPCfgIndex_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 5, 1, 6, 1, 1),
    _SpeedAmpMEthPCfgIndex_Type()
)
speedAmpMEthPCfgIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    speedAmpMEthPCfgIndex.setStatus("current")


class _SpeedAmpMEthPCfgSlot_Type(Integer32):
    """Custom type speedAmpMEthPCfgSlot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 19),
    )


_SpeedAmpMEthPCfgSlot_Type.__name__ = "Integer32"
_SpeedAmpMEthPCfgSlot_Object = MibTableColumn
speedAmpMEthPCfgSlot = _SpeedAmpMEthPCfgSlot_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 5, 1, 6, 1, 2),
    _SpeedAmpMEthPCfgSlot_Type()
)
speedAmpMEthPCfgSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    speedAmpMEthPCfgSlot.setStatus("current")


class _SpeedAmpMEthPCfgPort_Type(Integer32):
    """Custom type speedAmpMEthPCfgPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5),
    )


_SpeedAmpMEthPCfgPort_Type.__name__ = "Integer32"
_SpeedAmpMEthPCfgPort_Object = MibTableColumn
speedAmpMEthPCfgPort = _SpeedAmpMEthPCfgPort_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 5, 1, 6, 1, 3),
    _SpeedAmpMEthPCfgPort_Type()
)
speedAmpMEthPCfgPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    speedAmpMEthPCfgPort.setStatus("current")


class _SpeedAmpMEthPCfgAdminConfig_Type(Integer32):
    """Custom type speedAmpMEthPCfgAdminConfig based on Integer32"""
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
        *(("notAvailable", 0),
          ("adminDown", 1),
          ("adminUp", 2),
          ("unknown", 255))
    )


_SpeedAmpMEthPCfgAdminConfig_Type.__name__ = "Integer32"
_SpeedAmpMEthPCfgAdminConfig_Object = MibTableColumn
speedAmpMEthPCfgAdminConfig = _SpeedAmpMEthPCfgAdminConfig_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 5, 1, 6, 1, 4),
    _SpeedAmpMEthPCfgAdminConfig_Type()
)
speedAmpMEthPCfgAdminConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    speedAmpMEthPCfgAdminConfig.setStatus("current")


class _SpeedAmpMEthPCfgDescription_Type(DisplayString):
    """Custom type speedAmpMEthPCfgDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_SpeedAmpMEthPCfgDescription_Type.__name__ = "DisplayString"
_SpeedAmpMEthPCfgDescription_Object = MibTableColumn
speedAmpMEthPCfgDescription = _SpeedAmpMEthPCfgDescription_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 5, 1, 6, 1, 5),
    _SpeedAmpMEthPCfgDescription_Type()
)
speedAmpMEthPCfgDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    speedAmpMEthPCfgDescription.setStatus("current")


class _SpeedAmpMEthPCfgMode_Type(Integer32):
    """Custom type speedAmpMEthPCfgMode based on Integer32"""
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
              255)
        )
    )
    namedValues = NamedValues(
        *(("notAvailable", 0),
          ("autoneg", 1),
          ("fix10HDX", 2),
          ("fix10FDX", 3),
          ("fix100HDX", 4),
          ("fix100FDX", 5),
          ("fixhdlc", 6),
          ("fixrmii", 7),
          ("unknown", 255))
    )


_SpeedAmpMEthPCfgMode_Type.__name__ = "Integer32"
_SpeedAmpMEthPCfgMode_Object = MibTableColumn
speedAmpMEthPCfgMode = _SpeedAmpMEthPCfgMode_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 5, 1, 6, 1, 6),
    _SpeedAmpMEthPCfgMode_Type()
)
speedAmpMEthPCfgMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    speedAmpMEthPCfgMode.setStatus("current")


class _SpeedAmpMEthPCfgAlarmReporting_Type(Integer32):
    """Custom type speedAmpMEthPCfgAlarmReporting based on Integer32"""
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


_SpeedAmpMEthPCfgAlarmReporting_Type.__name__ = "Integer32"
_SpeedAmpMEthPCfgAlarmReporting_Object = MibTableColumn
speedAmpMEthPCfgAlarmReporting = _SpeedAmpMEthPCfgAlarmReporting_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 5, 1, 6, 1, 7),
    _SpeedAmpMEthPCfgAlarmReporting_Type()
)
speedAmpMEthPCfgAlarmReporting.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    speedAmpMEthPCfgAlarmReporting.setStatus("current")


class _SpeedAmpMEthPCfgAlarmSchedule_Type(Integer32):
    """Custom type speedAmpMEthPCfgAlarmSchedule based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1200),
    )


_SpeedAmpMEthPCfgAlarmSchedule_Type.__name__ = "Integer32"
_SpeedAmpMEthPCfgAlarmSchedule_Object = MibTableColumn
speedAmpMEthPCfgAlarmSchedule = _SpeedAmpMEthPCfgAlarmSchedule_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 5, 1, 6, 1, 8),
    _SpeedAmpMEthPCfgAlarmSchedule_Type()
)
speedAmpMEthPCfgAlarmSchedule.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    speedAmpMEthPCfgAlarmSchedule.setStatus("current")
_SpeedAmpModuleGeneralSFPInfosTable_Object = MibTable
speedAmpModuleGeneralSFPInfosTable = _SpeedAmpModuleGeneralSFPInfosTable_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 5, 1, 7)
)
if mibBuilder.loadTexts:
    speedAmpModuleGeneralSFPInfosTable.setStatus("current")
_SpeedAmpModuleGeneralSFPInfosEntry_Object = MibTableRow
speedAmpModuleGeneralSFPInfosEntry = _SpeedAmpModuleGeneralSFPInfosEntry_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 5, 1, 7, 1)
)
speedAmpModuleGeneralSFPInfosEntry.setIndexNames(
    (0, "SPEED-AMP-MIB", "speedAmpSFPIndex"),
)
if mibBuilder.loadTexts:
    speedAmpModuleGeneralSFPInfosEntry.setStatus("current")


class _SpeedAmpSFPIndex_Type(Integer32):
    """Custom type speedAmpSFPIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1900),
    )


_SpeedAmpSFPIndex_Type.__name__ = "Integer32"
_SpeedAmpSFPIndex_Object = MibTableColumn
speedAmpSFPIndex = _SpeedAmpSFPIndex_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 5, 1, 7, 1, 1),
    _SpeedAmpSFPIndex_Type()
)
speedAmpSFPIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    speedAmpSFPIndex.setStatus("current")
_SpeedAmpSFPSlot_Type = Integer32
_SpeedAmpSFPSlot_Object = MibTableColumn
speedAmpSFPSlot = _SpeedAmpSFPSlot_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 5, 1, 7, 1, 2),
    _SpeedAmpSFPSlot_Type()
)
speedAmpSFPSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    speedAmpSFPSlot.setStatus("current")
_SpeedAmpSFPPort_Type = Integer32
_SpeedAmpSFPPort_Object = MibTableColumn
speedAmpSFPPort = _SpeedAmpSFPPort_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 5, 1, 7, 1, 3),
    _SpeedAmpSFPPort_Type()
)
speedAmpSFPPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    speedAmpSFPPort.setStatus("current")


class _SpeedAmpSFPVendorName_Type(DisplayString):
    """Custom type speedAmpSFPVendorName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 17),
    )


_SpeedAmpSFPVendorName_Type.__name__ = "DisplayString"
_SpeedAmpSFPVendorName_Object = MibTableColumn
speedAmpSFPVendorName = _SpeedAmpSFPVendorName_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 5, 1, 7, 1, 4),
    _SpeedAmpSFPVendorName_Type()
)
speedAmpSFPVendorName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    speedAmpSFPVendorName.setStatus("current")


class _SpeedAmpSFPPartNumber_Type(DisplayString):
    """Custom type speedAmpSFPPartNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 17),
    )


_SpeedAmpSFPPartNumber_Type.__name__ = "DisplayString"
_SpeedAmpSFPPartNumber_Object = MibTableColumn
speedAmpSFPPartNumber = _SpeedAmpSFPPartNumber_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 5, 1, 7, 1, 5),
    _SpeedAmpSFPPartNumber_Type()
)
speedAmpSFPPartNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    speedAmpSFPPartNumber.setStatus("current")


class _SpeedAmpSFPSerialNumber_Type(DisplayString):
    """Custom type speedAmpSFPSerialNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 17),
    )


_SpeedAmpSFPSerialNumber_Type.__name__ = "DisplayString"
_SpeedAmpSFPSerialNumber_Object = MibTableColumn
speedAmpSFPSerialNumber = _SpeedAmpSFPSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 5, 1, 7, 1, 6),
    _SpeedAmpSFPSerialNumber_Type()
)
speedAmpSFPSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    speedAmpSFPSerialNumber.setStatus("current")
_SpeedAmpSFPWavelength_Type = Integer32
_SpeedAmpSFPWavelength_Object = MibTableColumn
speedAmpSFPWavelength = _SpeedAmpSFPWavelength_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 5, 1, 7, 1, 7),
    _SpeedAmpSFPWavelength_Type()
)
speedAmpSFPWavelength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    speedAmpSFPWavelength.setStatus("current")


class _SpeedAmpSFPDMIMode_Type(Integer32):
    """Custom type speedAmpSFPDMIMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              254,
              255)
        )
    )
    namedValues = NamedValues(
        *(("notAvailable", 0),
          ("sff8472V93", 1),
          ("sff8472V95", 2),
          ("sff8472V102", 3),
          ("sffVother", 4),
          ("notImplemented", 254),
          ("unknown", 255))
    )


_SpeedAmpSFPDMIMode_Type.__name__ = "Integer32"
_SpeedAmpSFPDMIMode_Object = MibTableColumn
speedAmpSFPDMIMode = _SpeedAmpSFPDMIMode_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 5, 1, 7, 1, 8),
    _SpeedAmpSFPDMIMode_Type()
)
speedAmpSFPDMIMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    speedAmpSFPDMIMode.setStatus("current")


class _SpeedAmpSFPPortType_Type(Integer32):
    """Custom type speedAmpSFPPortType based on Integer32"""
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
        *(("notAvailable", 0),
          ("osc", 1),
          ("user", 2),
          ("unknown", 255))
    )


_SpeedAmpSFPPortType_Type.__name__ = "Integer32"
_SpeedAmpSFPPortType_Object = MibTableColumn
speedAmpSFPPortType = _SpeedAmpSFPPortType_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 5, 1, 7, 1, 9),
    _SpeedAmpSFPPortType_Type()
)
speedAmpSFPPortType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    speedAmpSFPPortType.setStatus("current")
_SpeedAmpModuleSFPMessurementTable_Object = MibTable
speedAmpModuleSFPMessurementTable = _SpeedAmpModuleSFPMessurementTable_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 5, 1, 8)
)
if mibBuilder.loadTexts:
    speedAmpModuleSFPMessurementTable.setStatus("current")
_SpeedAmpModuleSFPMessurementEntry_Object = MibTableRow
speedAmpModuleSFPMessurementEntry = _SpeedAmpModuleSFPMessurementEntry_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 5, 1, 8, 1)
)
speedAmpModuleSFPMessurementEntry.setIndexNames(
    (0, "SPEED-AMP-MIB", "speedAmpMSFPIndex"),
)
if mibBuilder.loadTexts:
    speedAmpModuleSFPMessurementEntry.setStatus("current")


class _SpeedAmpMSFPIndex_Type(Integer32):
    """Custom type speedAmpMSFPIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1900),
    )


_SpeedAmpMSFPIndex_Type.__name__ = "Integer32"
_SpeedAmpMSFPIndex_Object = MibTableColumn
speedAmpMSFPIndex = _SpeedAmpMSFPIndex_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 5, 1, 8, 1, 1),
    _SpeedAmpMSFPIndex_Type()
)
speedAmpMSFPIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    speedAmpMSFPIndex.setStatus("current")
_SpeedAmpMSFPSlot_Type = Integer32
_SpeedAmpMSFPSlot_Object = MibTableColumn
speedAmpMSFPSlot = _SpeedAmpMSFPSlot_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 5, 1, 8, 1, 2),
    _SpeedAmpMSFPSlot_Type()
)
speedAmpMSFPSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    speedAmpMSFPSlot.setStatus("current")
_SpeedAmpMSFPPort_Type = Integer32
_SpeedAmpMSFPPort_Object = MibTableColumn
speedAmpMSFPPort = _SpeedAmpMSFPPort_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 5, 1, 8, 1, 3),
    _SpeedAmpMSFPPort_Type()
)
speedAmpMSFPPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    speedAmpMSFPPort.setStatus("current")
_SpeedAmpMSFPRXPower_Type = Integer32
_SpeedAmpMSFPRXPower_Object = MibTableColumn
speedAmpMSFPRXPower = _SpeedAmpMSFPRXPower_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 5, 1, 8, 1, 4),
    _SpeedAmpMSFPRXPower_Type()
)
speedAmpMSFPRXPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    speedAmpMSFPRXPower.setStatus("current")
_SpeedAmpMSFPTXPower_Type = Integer32
_SpeedAmpMSFPTXPower_Object = MibTableColumn
speedAmpMSFPTXPower = _SpeedAmpMSFPTXPower_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 5, 1, 8, 1, 5),
    _SpeedAmpMSFPTXPower_Type()
)
speedAmpMSFPTXPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    speedAmpMSFPTXPower.setStatus("current")
_SpeedAmpMSFPTXBias_Type = Integer32
_SpeedAmpMSFPTXBias_Object = MibTableColumn
speedAmpMSFPTXBias = _SpeedAmpMSFPTXBias_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 5, 1, 8, 1, 6),
    _SpeedAmpMSFPTXBias_Type()
)
speedAmpMSFPTXBias.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    speedAmpMSFPTXBias.setStatus("current")
_SpeedAmpMSFPTemp_Type = Integer32
_SpeedAmpMSFPTemp_Object = MibTableColumn
speedAmpMSFPTemp = _SpeedAmpMSFPTemp_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 5, 1, 8, 1, 7),
    _SpeedAmpMSFPTemp_Type()
)
speedAmpMSFPTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    speedAmpMSFPTemp.setStatus("current")


class _SpeedAmpMSFPPortType_Type(Integer32):
    """Custom type speedAmpMSFPPortType based on Integer32"""
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
        *(("notAvailable", 0),
          ("osc", 1),
          ("user", 2),
          ("unknown", 255))
    )


_SpeedAmpMSFPPortType_Type.__name__ = "Integer32"
_SpeedAmpMSFPPortType_Object = MibTableColumn
speedAmpMSFPPortType = _SpeedAmpMSFPPortType_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 5, 1, 8, 1, 8),
    _SpeedAmpMSFPPortType_Type()
)
speedAmpMSFPPortType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    speedAmpMSFPPortType.setStatus("current")
_SpeedAmpDevGeneralInfosTable_Object = MibTable
speedAmpDevGeneralInfosTable = _SpeedAmpDevGeneralInfosTable_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 5, 1, 9)
)
if mibBuilder.loadTexts:
    speedAmpDevGeneralInfosTable.setStatus("current")
_SpeedAmpDevGeneralInfosEntry_Object = MibTableRow
speedAmpDevGeneralInfosEntry = _SpeedAmpDevGeneralInfosEntry_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 5, 1, 9, 1)
)
speedAmpDevGeneralInfosEntry.setIndexNames(
    (0, "SPEED-AMP-MIB", "speedAmpDevSlot"),
)
if mibBuilder.loadTexts:
    speedAmpDevGeneralInfosEntry.setStatus("current")


class _SpeedAmpDevSlot_Type(Integer32):
    """Custom type speedAmpDevSlot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 19),
    )


_SpeedAmpDevSlot_Type.__name__ = "Integer32"
_SpeedAmpDevSlot_Object = MibTableColumn
speedAmpDevSlot = _SpeedAmpDevSlot_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 5, 1, 9, 1, 2),
    _SpeedAmpDevSlot_Type()
)
speedAmpDevSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    speedAmpDevSlot.setStatus("current")


class _SpeedAmpDevSerialNumber_Type(DisplayString):
    """Custom type speedAmpDevSerialNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 17),
    )


_SpeedAmpDevSerialNumber_Type.__name__ = "DisplayString"
_SpeedAmpDevSerialNumber_Object = MibTableColumn
speedAmpDevSerialNumber = _SpeedAmpDevSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 5, 1, 9, 1, 3),
    _SpeedAmpDevSerialNumber_Type()
)
speedAmpDevSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    speedAmpDevSerialNumber.setStatus("current")


class _SpeedAmpDevConfiguration_Type(Integer32):
    """Custom type speedAmpDevConfiguration based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              3,
              4,
              5,
              6,
              255)
        )
    )
    namedValues = NamedValues(
        *(("notAvailable", 0),
          ("confConstantPower", 3),
          ("confConstantGain", 4),
          ("confOFF", 5),
          ("confOther", 6),
          ("unknown", 255))
    )


_SpeedAmpDevConfiguration_Type.__name__ = "Integer32"
_SpeedAmpDevConfiguration_Object = MibTableColumn
speedAmpDevConfiguration = _SpeedAmpDevConfiguration_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 5, 1, 9, 1, 4),
    _SpeedAmpDevConfiguration_Type()
)
speedAmpDevConfiguration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    speedAmpDevConfiguration.setStatus("current")


class _SpeedAmpDevModuletype_Type(Integer32):
    """Custom type speedAmpDevModuletype based on Integer32"""
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
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19,
              255)
        )
    )
    namedValues = NamedValues(
        *(("notAvailable", 0),
          ("other", 1),
          ("preamp14", 2),
          ("booster17", 3),
          ("booster17OSC", 4),
          ("booster23OSC", 5),
          ("inline17", 6),
          ("inline23", 7),
          ("ramanMaster10", 8),
          ("ramanMaster15", 9),
          ("ramanSlave10", 10),
          ("ramanSlave15", 11),
          ("ramanStandalone10", 12),
          ("ramanStandalone15", 13),
          ("preamp14ext", 14),
          ("booster17ext", 15),
          ("booster17OSCext", 16),
          ("booster23OSCext", 17),
          ("inline17ext", 18),
          ("inline23ext", 19),
          ("unknown", 255))
    )


_SpeedAmpDevModuletype_Type.__name__ = "Integer32"
_SpeedAmpDevModuletype_Object = MibTableColumn
speedAmpDevModuletype = _SpeedAmpDevModuletype_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 5, 1, 9, 1, 5),
    _SpeedAmpDevModuletype_Type()
)
speedAmpDevModuletype.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    speedAmpDevModuletype.setStatus("current")


class _SpeedAmpDevVersion_Type(DisplayString):
    """Custom type speedAmpDevVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 17),
    )


_SpeedAmpDevVersion_Type.__name__ = "DisplayString"
_SpeedAmpDevVersion_Object = MibTableColumn
speedAmpDevVersion = _SpeedAmpDevVersion_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 5, 1, 9, 1, 6),
    _SpeedAmpDevVersion_Type()
)
speedAmpDevVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    speedAmpDevVersion.setStatus("current")
_SpeedAmpDevVendor_Type = Integer32
_SpeedAmpDevVendor_Object = MibTableColumn
speedAmpDevVendor = _SpeedAmpDevVendor_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 5, 1, 9, 1, 7),
    _SpeedAmpDevVendor_Type()
)
speedAmpDevVendor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    speedAmpDevVendor.setStatus("current")


class _SpeedAmpDevLinePortDescription_Type(DisplayString):
    """Custom type speedAmpDevLinePortDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_SpeedAmpDevLinePortDescription_Type.__name__ = "DisplayString"
_SpeedAmpDevLinePortDescription_Object = MibTableColumn
speedAmpDevLinePortDescription = _SpeedAmpDevLinePortDescription_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 5, 1, 9, 1, 8),
    _SpeedAmpDevLinePortDescription_Type()
)
speedAmpDevLinePortDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    speedAmpDevLinePortDescription.setStatus("current")


class _SpeedAmpDevClientPortDescription_Type(DisplayString):
    """Custom type speedAmpDevClientPortDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_SpeedAmpDevClientPortDescription_Type.__name__ = "DisplayString"
_SpeedAmpDevClientPortDescription_Object = MibTableColumn
speedAmpDevClientPortDescription = _SpeedAmpDevClientPortDescription_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 5, 1, 9, 1, 9),
    _SpeedAmpDevClientPortDescription_Type()
)
speedAmpDevClientPortDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    speedAmpDevClientPortDescription.setStatus("current")
_SpeedAmpDevOverviewTable_Object = MibTable
speedAmpDevOverviewTable = _SpeedAmpDevOverviewTable_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 5, 1, 10)
)
if mibBuilder.loadTexts:
    speedAmpDevOverviewTable.setStatus("current")
_SpeedAmpDevOverviewEntry_Object = MibTableRow
speedAmpDevOverviewEntry = _SpeedAmpDevOverviewEntry_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 5, 1, 10, 1)
)
speedAmpDevOverviewEntry.setIndexNames(
    (0, "SPEED-AMP-MIB", "speedAmpDevMSlot"),
)
if mibBuilder.loadTexts:
    speedAmpDevOverviewEntry.setStatus("current")


class _SpeedAmpDevMSlot_Type(Integer32):
    """Custom type speedAmpDevMSlot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 19),
    )


_SpeedAmpDevMSlot_Type.__name__ = "Integer32"
_SpeedAmpDevMSlot_Object = MibTableColumn
speedAmpDevMSlot = _SpeedAmpDevMSlot_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 5, 1, 10, 1, 2),
    _SpeedAmpDevMSlot_Type()
)
speedAmpDevMSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    speedAmpDevMSlot.setStatus("current")
_SpeedAmpDevGain_Type = Integer32
_SpeedAmpDevGain_Object = MibTableColumn
speedAmpDevGain = _SpeedAmpDevGain_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 5, 1, 10, 1, 3),
    _SpeedAmpDevGain_Type()
)
speedAmpDevGain.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    speedAmpDevGain.setStatus("current")
_SpeedAmpDevPumpCurrent_Type = Integer32
_SpeedAmpDevPumpCurrent_Object = MibTableColumn
speedAmpDevPumpCurrent = _SpeedAmpDevPumpCurrent_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 5, 1, 10, 1, 4),
    _SpeedAmpDevPumpCurrent_Type()
)
speedAmpDevPumpCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    speedAmpDevPumpCurrent.setStatus("current")
_SpeedAmpDevPumpPower_Type = Integer32
_SpeedAmpDevPumpPower_Object = MibTableColumn
speedAmpDevPumpPower = _SpeedAmpDevPumpPower_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 5, 1, 10, 1, 5),
    _SpeedAmpDevPumpPower_Type()
)
speedAmpDevPumpPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    speedAmpDevPumpPower.setStatus("current")


class _SpeedAmpDevMode_Type(Integer32):
    """Custom type speedAmpDevMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              3,
              4,
              5,
              6,
              255)
        )
    )
    namedValues = NamedValues(
        *(("notAvailable", 0),
          ("confConstantPower", 3),
          ("confConstantGain", 4),
          ("confOFF", 5),
          ("confOther", 6),
          ("unknown", 255))
    )


_SpeedAmpDevMode_Type.__name__ = "Integer32"
_SpeedAmpDevMode_Object = MibTableColumn
speedAmpDevMode = _SpeedAmpDevMode_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 5, 1, 10, 1, 6),
    _SpeedAmpDevMode_Type()
)
speedAmpDevMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    speedAmpDevMode.setStatus("current")


class _SpeedAmpDevModeShutdown_Type(Integer32):
    """Custom type speedAmpDevModeShutdown based on Integer32"""
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
        *(("notAvailable", 0),
          ("cfgAutoLaserShutdownOff", 1),
          ("cfgAutoLaserShutdownOn", 2),
          ("unknown", 255))
    )


_SpeedAmpDevModeShutdown_Type.__name__ = "Integer32"
_SpeedAmpDevModeShutdown_Object = MibTableColumn
speedAmpDevModeShutdown = _SpeedAmpDevModeShutdown_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 5, 1, 10, 1, 7),
    _SpeedAmpDevModeShutdown_Type()
)
speedAmpDevModeShutdown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    speedAmpDevModeShutdown.setStatus("current")
_SpeedAmpDevLosInputThreshold_Type = Integer32
_SpeedAmpDevLosInputThreshold_Object = MibTableColumn
speedAmpDevLosInputThreshold = _SpeedAmpDevLosInputThreshold_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 5, 1, 10, 1, 8),
    _SpeedAmpDevLosInputThreshold_Type()
)
speedAmpDevLosInputThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    speedAmpDevLosInputThreshold.setStatus("current")
_SpeedAmpDevHighOutputThreshold_Type = Integer32
_SpeedAmpDevHighOutputThreshold_Object = MibTableColumn
speedAmpDevHighOutputThreshold = _SpeedAmpDevHighOutputThreshold_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 5, 1, 10, 1, 9),
    _SpeedAmpDevHighOutputThreshold_Type()
)
speedAmpDevHighOutputThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    speedAmpDevHighOutputThreshold.setStatus("current")


class _SpeedAmpDevAlarm_Type(Integer32):
    """Custom type speedAmpDevAlarm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              254)
        )
    )
    namedValues = NamedValues(
        *(("noAlarm", 0),
          ("unknown", 254))
    )


_SpeedAmpDevAlarm_Type.__name__ = "Integer32"
_SpeedAmpDevAlarm_Object = MibTableColumn
speedAmpDevAlarm = _SpeedAmpDevAlarm_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 5, 1, 10, 1, 10),
    _SpeedAmpDevAlarm_Type()
)
speedAmpDevAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    speedAmpDevAlarm.setStatus("current")
_SpeedAmpDevCaseTemperature_Type = Integer32
_SpeedAmpDevCaseTemperature_Object = MibTableColumn
speedAmpDevCaseTemperature = _SpeedAmpDevCaseTemperature_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 5, 1, 10, 1, 11),
    _SpeedAmpDevCaseTemperature_Type()
)
speedAmpDevCaseTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    speedAmpDevCaseTemperature.setStatus("current")
_SpeedAmpDevClientInputPower_Type = Integer32
_SpeedAmpDevClientInputPower_Object = MibTableColumn
speedAmpDevClientInputPower = _SpeedAmpDevClientInputPower_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 5, 1, 10, 1, 12),
    _SpeedAmpDevClientInputPower_Type()
)
speedAmpDevClientInputPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    speedAmpDevClientInputPower.setStatus("current")
_SpeedAmpDevLineOutputPower_Type = Integer32
_SpeedAmpDevLineOutputPower_Object = MibTableColumn
speedAmpDevLineOutputPower = _SpeedAmpDevLineOutputPower_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 5, 1, 10, 1, 13),
    _SpeedAmpDevLineOutputPower_Type()
)
speedAmpDevLineOutputPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    speedAmpDevLineOutputPower.setStatus("current")
_SpeedAmpDevBackreflectionThreshold_Type = Integer32
_SpeedAmpDevBackreflectionThreshold_Object = MibTableColumn
speedAmpDevBackreflectionThreshold = _SpeedAmpDevBackreflectionThreshold_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 5, 1, 10, 1, 14),
    _SpeedAmpDevBackreflectionThreshold_Type()
)
speedAmpDevBackreflectionThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    speedAmpDevBackreflectionThreshold.setStatus("current")
_SpeedAmpDevShutdownThreshold_Type = Integer32
_SpeedAmpDevShutdownThreshold_Object = MibTableColumn
speedAmpDevShutdownThreshold = _SpeedAmpDevShutdownThreshold_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 5, 1, 10, 1, 15),
    _SpeedAmpDevShutdownThreshold_Type()
)
speedAmpDevShutdownThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    speedAmpDevShutdownThreshold.setStatus("current")
_SpeedAmpDevBackreflectionRatio_Type = Integer32
_SpeedAmpDevBackreflectionRatio_Object = MibTableColumn
speedAmpDevBackreflectionRatio = _SpeedAmpDevBackreflectionRatio_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 5, 1, 10, 1, 16),
    _SpeedAmpDevBackreflectionRatio_Type()
)
speedAmpDevBackreflectionRatio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    speedAmpDevBackreflectionRatio.setStatus("current")
_SpeedAmpDevConfigTable_Object = MibTable
speedAmpDevConfigTable = _SpeedAmpDevConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 5, 1, 11)
)
if mibBuilder.loadTexts:
    speedAmpDevConfigTable.setStatus("current")
_SpeedAmpDevConfigEntry_Object = MibTableRow
speedAmpDevConfigEntry = _SpeedAmpDevConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 5, 1, 11, 1)
)
speedAmpDevConfigEntry.setIndexNames(
    (0, "SPEED-AMP-MIB", "speedAmpDevCfgSlot"),
)
if mibBuilder.loadTexts:
    speedAmpDevConfigEntry.setStatus("current")


class _SpeedAmpDevCfgSlot_Type(Integer32):
    """Custom type speedAmpDevCfgSlot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 19),
    )


_SpeedAmpDevCfgSlot_Type.__name__ = "Integer32"
_SpeedAmpDevCfgSlot_Object = MibTableColumn
speedAmpDevCfgSlot = _SpeedAmpDevCfgSlot_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 5, 1, 11, 1, 2),
    _SpeedAmpDevCfgSlot_Type()
)
speedAmpDevCfgSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    speedAmpDevCfgSlot.setStatus("current")
_SpeedAmpDevCfgGainValue_Type = Integer32
_SpeedAmpDevCfgGainValue_Object = MibTableColumn
speedAmpDevCfgGainValue = _SpeedAmpDevCfgGainValue_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 5, 1, 11, 1, 3),
    _SpeedAmpDevCfgGainValue_Type()
)
speedAmpDevCfgGainValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    speedAmpDevCfgGainValue.setStatus("current")
_SpeedAmpDevCfgPoutValue_Type = Integer32
_SpeedAmpDevCfgPoutValue_Object = MibTableColumn
speedAmpDevCfgPoutValue = _SpeedAmpDevCfgPoutValue_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 5, 1, 11, 1, 4),
    _SpeedAmpDevCfgPoutValue_Type()
)
speedAmpDevCfgPoutValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    speedAmpDevCfgPoutValue.setStatus("current")


class _SpeedAmpDevCfgPumpPwr_Type(Integer32):
    """Custom type speedAmpDevCfgPumpPwr based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 660),
    )


_SpeedAmpDevCfgPumpPwr_Type.__name__ = "Integer32"
_SpeedAmpDevCfgPumpPwr_Object = MibTableColumn
speedAmpDevCfgPumpPwr = _SpeedAmpDevCfgPumpPwr_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 5, 1, 11, 1, 5),
    _SpeedAmpDevCfgPumpPwr_Type()
)
speedAmpDevCfgPumpPwr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    speedAmpDevCfgPumpPwr.setStatus("current")


class _SpeedAmpDevCfgModeValue_Type(Integer32):
    """Custom type speedAmpDevCfgModeValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              3,
              4,
              5,
              6,
              255)
        )
    )
    namedValues = NamedValues(
        *(("notAvailable", 0),
          ("confConstantPower", 3),
          ("confConstantGain", 4),
          ("confOFF", 5),
          ("confOther", 6),
          ("unknown", 255))
    )


_SpeedAmpDevCfgModeValue_Type.__name__ = "Integer32"
_SpeedAmpDevCfgModeValue_Object = MibTableColumn
speedAmpDevCfgModeValue = _SpeedAmpDevCfgModeValue_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 5, 1, 11, 1, 6),
    _SpeedAmpDevCfgModeValue_Type()
)
speedAmpDevCfgModeValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    speedAmpDevCfgModeValue.setStatus("current")


class _SpeedAmpDevCfgPowerSafetyModeValue_Type(Integer32):
    """Custom type speedAmpDevCfgPowerSafetyModeValue based on Integer32"""
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
        *(("notAvailable", 0),
          ("cfgAutoLaserShutdownOff", 1),
          ("cfgAutoLaserShutdownOn", 2),
          ("unknown", 255))
    )


_SpeedAmpDevCfgPowerSafetyModeValue_Type.__name__ = "Integer32"
_SpeedAmpDevCfgPowerSafetyModeValue_Object = MibTableColumn
speedAmpDevCfgPowerSafetyModeValue = _SpeedAmpDevCfgPowerSafetyModeValue_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 5, 1, 11, 1, 7),
    _SpeedAmpDevCfgPowerSafetyModeValue_Type()
)
speedAmpDevCfgPowerSafetyModeValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    speedAmpDevCfgPowerSafetyModeValue.setStatus("current")
_SpeedAmpDevCfgLosInputThresholdValue_Type = Integer32
_SpeedAmpDevCfgLosInputThresholdValue_Object = MibTableColumn
speedAmpDevCfgLosInputThresholdValue = _SpeedAmpDevCfgLosInputThresholdValue_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 5, 1, 11, 1, 8),
    _SpeedAmpDevCfgLosInputThresholdValue_Type()
)
speedAmpDevCfgLosInputThresholdValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    speedAmpDevCfgLosInputThresholdValue.setStatus("current")


class _SpeedAmpDevCfgLinePortDescription_Type(DisplayString):
    """Custom type speedAmpDevCfgLinePortDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_SpeedAmpDevCfgLinePortDescription_Type.__name__ = "DisplayString"
_SpeedAmpDevCfgLinePortDescription_Object = MibTableColumn
speedAmpDevCfgLinePortDescription = _SpeedAmpDevCfgLinePortDescription_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 5, 1, 11, 1, 9),
    _SpeedAmpDevCfgLinePortDescription_Type()
)
speedAmpDevCfgLinePortDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    speedAmpDevCfgLinePortDescription.setStatus("current")


class _SpeedAmpDevCfgClientPortDescription_Type(DisplayString):
    """Custom type speedAmpDevCfgClientPortDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_SpeedAmpDevCfgClientPortDescription_Type.__name__ = "DisplayString"
_SpeedAmpDevCfgClientPortDescription_Object = MibTableColumn
speedAmpDevCfgClientPortDescription = _SpeedAmpDevCfgClientPortDescription_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 5, 1, 11, 1, 10),
    _SpeedAmpDevCfgClientPortDescription_Type()
)
speedAmpDevCfgClientPortDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    speedAmpDevCfgClientPortDescription.setStatus("current")


class _SpeedAmpDevCfgAlarmReporting_Type(Integer32):
    """Custom type speedAmpDevCfgAlarmReporting based on Integer32"""
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


_SpeedAmpDevCfgAlarmReporting_Type.__name__ = "Integer32"
_SpeedAmpDevCfgAlarmReporting_Object = MibTableColumn
speedAmpDevCfgAlarmReporting = _SpeedAmpDevCfgAlarmReporting_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 5, 1, 11, 1, 11),
    _SpeedAmpDevCfgAlarmReporting_Type()
)
speedAmpDevCfgAlarmReporting.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    speedAmpDevCfgAlarmReporting.setStatus("current")


class _SpeedAmpDevCfgAlarmSchedule_Type(Integer32):
    """Custom type speedAmpDevCfgAlarmSchedule based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1200),
    )


_SpeedAmpDevCfgAlarmSchedule_Type.__name__ = "Integer32"
_SpeedAmpDevCfgAlarmSchedule_Object = MibTableColumn
speedAmpDevCfgAlarmSchedule = _SpeedAmpDevCfgAlarmSchedule_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 5, 1, 11, 1, 12),
    _SpeedAmpDevCfgAlarmSchedule_Type()
)
speedAmpDevCfgAlarmSchedule.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    speedAmpDevCfgAlarmSchedule.setStatus("current")
_SpeedAmpDevCfgBackreflectionThresholdValue_Type = Integer32
_SpeedAmpDevCfgBackreflectionThresholdValue_Object = MibTableColumn
speedAmpDevCfgBackreflectionThresholdValue = _SpeedAmpDevCfgBackreflectionThresholdValue_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 5, 1, 11, 1, 13),
    _SpeedAmpDevCfgBackreflectionThresholdValue_Type()
)
speedAmpDevCfgBackreflectionThresholdValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    speedAmpDevCfgBackreflectionThresholdValue.setStatus("current")
_SpeedAmpDevAlarmTable_Object = MibTable
speedAmpDevAlarmTable = _SpeedAmpDevAlarmTable_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 5, 1, 12)
)
if mibBuilder.loadTexts:
    speedAmpDevAlarmTable.setStatus("current")
_SpeedAmpDevAlarmEntry_Object = MibTableRow
speedAmpDevAlarmEntry = _SpeedAmpDevAlarmEntry_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 5, 1, 12, 1)
)
speedAmpDevAlarmEntry.setIndexNames(
    (0, "SPEED-AMP-MIB", "speedAmpDevAlarmSlot"),
)
if mibBuilder.loadTexts:
    speedAmpDevAlarmEntry.setStatus("current")


class _SpeedAmpDevAlarmSlot_Type(Integer32):
    """Custom type speedAmpDevAlarmSlot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 19),
    )


_SpeedAmpDevAlarmSlot_Type.__name__ = "Integer32"
_SpeedAmpDevAlarmSlot_Object = MibTableColumn
speedAmpDevAlarmSlot = _SpeedAmpDevAlarmSlot_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 5, 1, 12, 1, 2),
    _SpeedAmpDevAlarmSlot_Type()
)
speedAmpDevAlarmSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    speedAmpDevAlarmSlot.setStatus("current")


class _SpeedAmpDevAlarmOpticalInput_Type(Integer32):
    """Custom type speedAmpDevAlarmOpticalInput based on Integer32"""
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
          ("noAlarm", 1),
          ("activeAlarm", 2),
          ("unknown", 255))
    )


_SpeedAmpDevAlarmOpticalInput_Type.__name__ = "Integer32"
_SpeedAmpDevAlarmOpticalInput_Object = MibTableColumn
speedAmpDevAlarmOpticalInput = _SpeedAmpDevAlarmOpticalInput_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 5, 1, 12, 1, 3),
    _SpeedAmpDevAlarmOpticalInput_Type()
)
speedAmpDevAlarmOpticalInput.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    speedAmpDevAlarmOpticalInput.setStatus("current")


class _SpeedAmpDevAlarmOpticalOutput_Type(Integer32):
    """Custom type speedAmpDevAlarmOpticalOutput based on Integer32"""
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
          ("noAlarm", 1),
          ("activeAlarm", 2),
          ("unknown", 255))
    )


_SpeedAmpDevAlarmOpticalOutput_Type.__name__ = "Integer32"
_SpeedAmpDevAlarmOpticalOutput_Object = MibTableColumn
speedAmpDevAlarmOpticalOutput = _SpeedAmpDevAlarmOpticalOutput_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 5, 1, 12, 1, 4),
    _SpeedAmpDevAlarmOpticalOutput_Type()
)
speedAmpDevAlarmOpticalOutput.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    speedAmpDevAlarmOpticalOutput.setStatus("current")


class _SpeedAmpDevAlarmModuleTemperature_Type(Integer32):
    """Custom type speedAmpDevAlarmModuleTemperature based on Integer32"""
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
          ("noAlarm", 1),
          ("activeAlarm", 2),
          ("unknown", 255))
    )


_SpeedAmpDevAlarmModuleTemperature_Type.__name__ = "Integer32"
_SpeedAmpDevAlarmModuleTemperature_Object = MibTableColumn
speedAmpDevAlarmModuleTemperature = _SpeedAmpDevAlarmModuleTemperature_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 5, 1, 12, 1, 5),
    _SpeedAmpDevAlarmModuleTemperature_Type()
)
speedAmpDevAlarmModuleTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    speedAmpDevAlarmModuleTemperature.setStatus("current")


class _SpeedAmpDevAlarmPumpTemperature_Type(Integer32):
    """Custom type speedAmpDevAlarmPumpTemperature based on Integer32"""
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
          ("noAlarm", 1),
          ("activeAlarm", 2),
          ("unknown", 255))
    )


_SpeedAmpDevAlarmPumpTemperature_Type.__name__ = "Integer32"
_SpeedAmpDevAlarmPumpTemperature_Object = MibTableColumn
speedAmpDevAlarmPumpTemperature = _SpeedAmpDevAlarmPumpTemperature_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 5, 1, 12, 1, 6),
    _SpeedAmpDevAlarmPumpTemperature_Type()
)
speedAmpDevAlarmPumpTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    speedAmpDevAlarmPumpTemperature.setStatus("current")


class _SpeedAmpDevAlarmPumpDriveCurrent_Type(Integer32):
    """Custom type speedAmpDevAlarmPumpDriveCurrent based on Integer32"""
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
          ("noAlarm", 1),
          ("activeAlarm", 2),
          ("unknown", 255))
    )


_SpeedAmpDevAlarmPumpDriveCurrent_Type.__name__ = "Integer32"
_SpeedAmpDevAlarmPumpDriveCurrent_Object = MibTableColumn
speedAmpDevAlarmPumpDriveCurrent = _SpeedAmpDevAlarmPumpDriveCurrent_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 5, 1, 12, 1, 7),
    _SpeedAmpDevAlarmPumpDriveCurrent_Type()
)
speedAmpDevAlarmPumpDriveCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    speedAmpDevAlarmPumpDriveCurrent.setStatus("current")


class _SpeedAmpDevAlarmSupplyVoltage_Type(Integer32):
    """Custom type speedAmpDevAlarmSupplyVoltage based on Integer32"""
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
          ("noAlarm", 1),
          ("activeAlarm", 2),
          ("unknown", 255))
    )


_SpeedAmpDevAlarmSupplyVoltage_Type.__name__ = "Integer32"
_SpeedAmpDevAlarmSupplyVoltage_Object = MibTableColumn
speedAmpDevAlarmSupplyVoltage = _SpeedAmpDevAlarmSupplyVoltage_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 5, 1, 12, 1, 8),
    _SpeedAmpDevAlarmSupplyVoltage_Type()
)
speedAmpDevAlarmSupplyVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    speedAmpDevAlarmSupplyVoltage.setStatus("current")


class _SpeedAmpDevAlarmAutoshutdown_Type(Integer32):
    """Custom type speedAmpDevAlarmAutoshutdown based on Integer32"""
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
          ("noAlarm", 1),
          ("activeAlarm", 2),
          ("unknown", 255))
    )


_SpeedAmpDevAlarmAutoshutdown_Type.__name__ = "Integer32"
_SpeedAmpDevAlarmAutoshutdown_Object = MibTableColumn
speedAmpDevAlarmAutoshutdown = _SpeedAmpDevAlarmAutoshutdown_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 5, 1, 12, 1, 9),
    _SpeedAmpDevAlarmAutoshutdown_Type()
)
speedAmpDevAlarmAutoshutdown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    speedAmpDevAlarmAutoshutdown.setStatus("current")


class _SpeedAmpDevAlarmSecurityMonitor_Type(Integer32):
    """Custom type speedAmpDevAlarmSecurityMonitor based on Integer32"""
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
        *(("notAvailiable", 0),
          ("secmonready", 1),
          ("secmonhalted", 2),
          ("secmonfailure", 3),
          ("unknown", 255))
    )


_SpeedAmpDevAlarmSecurityMonitor_Type.__name__ = "Integer32"
_SpeedAmpDevAlarmSecurityMonitor_Object = MibTableColumn
speedAmpDevAlarmSecurityMonitor = _SpeedAmpDevAlarmSecurityMonitor_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 5, 1, 12, 1, 10),
    _SpeedAmpDevAlarmSecurityMonitor_Type()
)
speedAmpDevAlarmSecurityMonitor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    speedAmpDevAlarmSecurityMonitor.setStatus("current")


class _SpeedAmpDevAlarmBackref_Type(Integer32):
    """Custom type speedAmpDevAlarmBackref based on Integer32"""
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
          ("noAlarm", 1),
          ("activeAlarm", 2),
          ("unknown", 255))
    )


_SpeedAmpDevAlarmBackref_Type.__name__ = "Integer32"
_SpeedAmpDevAlarmBackref_Object = MibTableColumn
speedAmpDevAlarmBackref = _SpeedAmpDevAlarmBackref_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 5, 1, 12, 1, 11),
    _SpeedAmpDevAlarmBackref_Type()
)
speedAmpDevAlarmBackref.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    speedAmpDevAlarmBackref.setStatus("current")
_SpeedAmpModuleSFPAlarmTable_Object = MibTable
speedAmpModuleSFPAlarmTable = _SpeedAmpModuleSFPAlarmTable_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 5, 1, 13)
)
if mibBuilder.loadTexts:
    speedAmpModuleSFPAlarmTable.setStatus("current")
_SpeedAmpModuleSFPAlarmEntry_Object = MibTableRow
speedAmpModuleSFPAlarmEntry = _SpeedAmpModuleSFPAlarmEntry_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 5, 1, 13, 1)
)
speedAmpModuleSFPAlarmEntry.setIndexNames(
    (0, "SPEED-AMP-MIB", "speedAmpMSFPAIndex"),
)
if mibBuilder.loadTexts:
    speedAmpModuleSFPAlarmEntry.setStatus("current")


class _SpeedAmpMSFPAIndex_Type(Integer32):
    """Custom type speedAmpMSFPAIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1900),
    )


_SpeedAmpMSFPAIndex_Type.__name__ = "Integer32"
_SpeedAmpMSFPAIndex_Object = MibTableColumn
speedAmpMSFPAIndex = _SpeedAmpMSFPAIndex_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 5, 1, 13, 1, 1),
    _SpeedAmpMSFPAIndex_Type()
)
speedAmpMSFPAIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    speedAmpMSFPAIndex.setStatus("current")
_SpeedAmpMSFPASlot_Type = Integer32
_SpeedAmpMSFPASlot_Object = MibTableColumn
speedAmpMSFPASlot = _SpeedAmpMSFPASlot_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 5, 1, 13, 1, 2),
    _SpeedAmpMSFPASlot_Type()
)
speedAmpMSFPASlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    speedAmpMSFPASlot.setStatus("current")
_SpeedAmpMSFPAPort_Type = Integer32
_SpeedAmpMSFPAPort_Object = MibTableColumn
speedAmpMSFPAPort = _SpeedAmpMSFPAPort_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 5, 1, 13, 1, 3),
    _SpeedAmpMSFPAPort_Type()
)
speedAmpMSFPAPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    speedAmpMSFPAPort.setStatus("current")


class _SpeedAmpMSFPARxPowerAlarm_Type(Integer32):
    """Custom type speedAmpMSFPARxPowerAlarm based on Integer32"""
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
        *(("notAvailiable", 0),
          ("noAlarm", 1),
          ("rxLowAlarm", 2),
          ("rxHighAlarm", 3),
          ("unknown", 255))
    )


_SpeedAmpMSFPARxPowerAlarm_Type.__name__ = "Integer32"
_SpeedAmpMSFPARxPowerAlarm_Object = MibTableColumn
speedAmpMSFPARxPowerAlarm = _SpeedAmpMSFPARxPowerAlarm_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 5, 1, 13, 1, 4),
    _SpeedAmpMSFPARxPowerAlarm_Type()
)
speedAmpMSFPARxPowerAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    speedAmpMSFPARxPowerAlarm.setStatus("current")


class _SpeedAmpMSFPATxPowerAlarm_Type(Integer32):
    """Custom type speedAmpMSFPATxPowerAlarm based on Integer32"""
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
          ("noAlarm", 1),
          ("activeAlarm", 2),
          ("unknown", 255))
    )


_SpeedAmpMSFPATxPowerAlarm_Type.__name__ = "Integer32"
_SpeedAmpMSFPATxPowerAlarm_Object = MibTableColumn
speedAmpMSFPATxPowerAlarm = _SpeedAmpMSFPATxPowerAlarm_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 5, 1, 13, 1, 5),
    _SpeedAmpMSFPATxPowerAlarm_Type()
)
speedAmpMSFPATxPowerAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    speedAmpMSFPATxPowerAlarm.setStatus("current")


class _SpeedAmpMSFPATxBiasAlarm_Type(Integer32):
    """Custom type speedAmpMSFPATxBiasAlarm based on Integer32"""
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
          ("noAlarm", 1),
          ("activeAlarm", 2),
          ("unknown", 255))
    )


_SpeedAmpMSFPATxBiasAlarm_Type.__name__ = "Integer32"
_SpeedAmpMSFPATxBiasAlarm_Object = MibTableColumn
speedAmpMSFPATxBiasAlarm = _SpeedAmpMSFPATxBiasAlarm_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 5, 1, 13, 1, 6),
    _SpeedAmpMSFPATxBiasAlarm_Type()
)
speedAmpMSFPATxBiasAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    speedAmpMSFPATxBiasAlarm.setStatus("current")


class _SpeedAmpMSFPATemperatureAlarm_Type(Integer32):
    """Custom type speedAmpMSFPATemperatureAlarm based on Integer32"""
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
        *(("notAvailiable", 0),
          ("noAlarm", 1),
          ("highWarning", 2),
          ("highAlarm", 3),
          ("unknown", 255))
    )


_SpeedAmpMSFPATemperatureAlarm_Type.__name__ = "Integer32"
_SpeedAmpMSFPATemperatureAlarm_Object = MibTableColumn
speedAmpMSFPATemperatureAlarm = _SpeedAmpMSFPATemperatureAlarm_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 5, 1, 13, 1, 7),
    _SpeedAmpMSFPATemperatureAlarm_Type()
)
speedAmpMSFPATemperatureAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    speedAmpMSFPATemperatureAlarm.setStatus("current")


class _SpeedAmpMSFPADWDMAlarm_Type(Integer32):
    """Custom type speedAmpMSFPADWDMAlarm based on Integer32"""
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
          ("noAlarm", 1),
          ("activeAlarm", 2),
          ("unknown", 255))
    )


_SpeedAmpMSFPADWDMAlarm_Type.__name__ = "Integer32"
_SpeedAmpMSFPADWDMAlarm_Object = MibTableColumn
speedAmpMSFPADWDMAlarm = _SpeedAmpMSFPADWDMAlarm_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 5, 1, 13, 1, 8),
    _SpeedAmpMSFPADWDMAlarm_Type()
)
speedAmpMSFPADWDMAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    speedAmpMSFPADWDMAlarm.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SPEED-AMP-MIB",
    **{"speedAmp": speedAmp,
       "speedAmpModuleOverviewTable": speedAmpModuleOverviewTable,
       "speedAmpModuleOverviewEntry": speedAmpModuleOverviewEntry,
       "speedAmpMSlot": speedAmpMSlot,
       "speedAmpMDevice": speedAmpMDevice,
       "speedAmpMStatus": speedAmpMStatus,
       "speedAmpMSysUpTime": speedAmpMSysUpTime,
       "speedAmpMTemp": speedAmpMTemp,
       "speedAmpMAlarmState": speedAmpMAlarmState,
       "speedAmpMSerialNumber": speedAmpMSerialNumber,
       "speedAmpModuleImagesOverviewTable": speedAmpModuleImagesOverviewTable,
       "speedAmpModuleImagesOverviewEntry": speedAmpModuleImagesOverviewEntry,
       "speedAmpSWSlot": speedAmpSWSlot,
       "speedAmpSwKernelImage": speedAmpSwKernelImage,
       "speedAmpSwAppImage": speedAmpSwAppImage,
       "speedAmpSwUploadStatus": speedAmpSwUploadStatus,
       "speedAmpSwUpdateStatus": speedAmpSwUpdateStatus,
       "speedAmpHwVersion": speedAmpHwVersion,
       "speedAmpModuleBoardConfigTable": speedAmpModuleBoardConfigTable,
       "speedAmpModuleBoardConfigEntry": speedAmpModuleBoardConfigEntry,
       "speedAmpTemperatureSlot": speedAmpTemperatureSlot,
       "speedAmpTemperatureHighWarning": speedAmpTemperatureHighWarning,
       "speedAmpTemperatureHighAlarm": speedAmpTemperatureHighAlarm,
       "speedAmpModuleNetworkParameterTable": speedAmpModuleNetworkParameterTable,
       "speedAmpModuleNetworkParameterEntry": speedAmpModuleNetworkParameterEntry,
       "speedAmpMNetworkSlot": speedAmpMNetworkSlot,
       "speedAmpMNetworkAdress": speedAmpMNetworkAdress,
       "speedAmpMNetworkMask": speedAmpMNetworkMask,
       "speedAmpMNetworkGateway": speedAmpMNetworkGateway,
       "speedAmpMNetworkSnmpTrapSink1": speedAmpMNetworkSnmpTrapSink1,
       "speedAmpMNetworkSnmpTrapSink2": speedAmpMNetworkSnmpTrapSink2,
       "speedAmpMNetworkSnmpTrapSink3": speedAmpMNetworkSnmpTrapSink3,
       "speedAmpMNetworkSnmpTrapSink4": speedAmpMNetworkSnmpTrapSink4,
       "speedAmpMNetworkSnmpTrapSink5": speedAmpMNetworkSnmpTrapSink5,
       "speedAmpMNetworkSnmpReadCommunity": speedAmpMNetworkSnmpReadCommunity,
       "speedAmpMNetworkSnmpWriteCommunity": speedAmpMNetworkSnmpWriteCommunity,
       "speedAmpMNetworkSysLocation": speedAmpMNetworkSysLocation,
       "speedAmpMNetworkSnmpAgentStatus": speedAmpMNetworkSnmpAgentStatus,
       "speedAmpMNetworkHttpServerStatus": speedAmpMNetworkHttpServerStatus,
       "speedAmpMNetworkSysname": speedAmpMNetworkSysname,
       "speedAmpNNetworkSyscontact": speedAmpNNetworkSyscontact,
       "speedAmpMNetworkUserTimeout": speedAmpMNetworkUserTimeout,
       "speedAmpMNetworkAccess": speedAmpMNetworkAccess,
       "speedAmpModuleEthPortOverviewTable": speedAmpModuleEthPortOverviewTable,
       "speedAmpModuleEthPortOverviewEntry": speedAmpModuleEthPortOverviewEntry,
       "speedAmpMEthIndex": speedAmpMEthIndex,
       "speedAmpMEthSlot": speedAmpMEthSlot,
       "speedAmpMEthPort": speedAmpMEthPort,
       "speedAmpMEthPortname": speedAmpMEthPortname,
       "speedAmpMEthPortAdminState": speedAmpMEthPortAdminState,
       "speedAmpMEthPortOperState": speedAmpMEthPortOperState,
       "speedAmpMEthPortMode": speedAmpMEthPortMode,
       "speedAmpMEthSFPState": speedAmpMEthSFPState,
       "speedAmpMEthPortRxPackets": speedAmpMEthPortRxPackets,
       "speedAmpMEthPortTxPackets": speedAmpMEthPortTxPackets,
       "speedAmpMEthErrors": speedAmpMEthErrors,
       "speedAmpMEthPortConfigTable": speedAmpMEthPortConfigTable,
       "speedAmpMEthPortConfigEntry": speedAmpMEthPortConfigEntry,
       "speedAmpMEthPCfgIndex": speedAmpMEthPCfgIndex,
       "speedAmpMEthPCfgSlot": speedAmpMEthPCfgSlot,
       "speedAmpMEthPCfgPort": speedAmpMEthPCfgPort,
       "speedAmpMEthPCfgAdminConfig": speedAmpMEthPCfgAdminConfig,
       "speedAmpMEthPCfgDescription": speedAmpMEthPCfgDescription,
       "speedAmpMEthPCfgMode": speedAmpMEthPCfgMode,
       "speedAmpMEthPCfgAlarmReporting": speedAmpMEthPCfgAlarmReporting,
       "speedAmpMEthPCfgAlarmSchedule": speedAmpMEthPCfgAlarmSchedule,
       "speedAmpModuleGeneralSFPInfosTable": speedAmpModuleGeneralSFPInfosTable,
       "speedAmpModuleGeneralSFPInfosEntry": speedAmpModuleGeneralSFPInfosEntry,
       "speedAmpSFPIndex": speedAmpSFPIndex,
       "speedAmpSFPSlot": speedAmpSFPSlot,
       "speedAmpSFPPort": speedAmpSFPPort,
       "speedAmpSFPVendorName": speedAmpSFPVendorName,
       "speedAmpSFPPartNumber": speedAmpSFPPartNumber,
       "speedAmpSFPSerialNumber": speedAmpSFPSerialNumber,
       "speedAmpSFPWavelength": speedAmpSFPWavelength,
       "speedAmpSFPDMIMode": speedAmpSFPDMIMode,
       "speedAmpSFPPortType": speedAmpSFPPortType,
       "speedAmpModuleSFPMessurementTable": speedAmpModuleSFPMessurementTable,
       "speedAmpModuleSFPMessurementEntry": speedAmpModuleSFPMessurementEntry,
       "speedAmpMSFPIndex": speedAmpMSFPIndex,
       "speedAmpMSFPSlot": speedAmpMSFPSlot,
       "speedAmpMSFPPort": speedAmpMSFPPort,
       "speedAmpMSFPRXPower": speedAmpMSFPRXPower,
       "speedAmpMSFPTXPower": speedAmpMSFPTXPower,
       "speedAmpMSFPTXBias": speedAmpMSFPTXBias,
       "speedAmpMSFPTemp": speedAmpMSFPTemp,
       "speedAmpMSFPPortType": speedAmpMSFPPortType,
       "speedAmpDevGeneralInfosTable": speedAmpDevGeneralInfosTable,
       "speedAmpDevGeneralInfosEntry": speedAmpDevGeneralInfosEntry,
       "speedAmpDevSlot": speedAmpDevSlot,
       "speedAmpDevSerialNumber": speedAmpDevSerialNumber,
       "speedAmpDevConfiguration": speedAmpDevConfiguration,
       "speedAmpDevModuletype": speedAmpDevModuletype,
       "speedAmpDevVersion": speedAmpDevVersion,
       "speedAmpDevVendor": speedAmpDevVendor,
       "speedAmpDevLinePortDescription": speedAmpDevLinePortDescription,
       "speedAmpDevClientPortDescription": speedAmpDevClientPortDescription,
       "speedAmpDevOverviewTable": speedAmpDevOverviewTable,
       "speedAmpDevOverviewEntry": speedAmpDevOverviewEntry,
       "speedAmpDevMSlot": speedAmpDevMSlot,
       "speedAmpDevGain": speedAmpDevGain,
       "speedAmpDevPumpCurrent": speedAmpDevPumpCurrent,
       "speedAmpDevPumpPower": speedAmpDevPumpPower,
       "speedAmpDevMode": speedAmpDevMode,
       "speedAmpDevModeShutdown": speedAmpDevModeShutdown,
       "speedAmpDevLosInputThreshold": speedAmpDevLosInputThreshold,
       "speedAmpDevHighOutputThreshold": speedAmpDevHighOutputThreshold,
       "speedAmpDevAlarm": speedAmpDevAlarm,
       "speedAmpDevCaseTemperature": speedAmpDevCaseTemperature,
       "speedAmpDevClientInputPower": speedAmpDevClientInputPower,
       "speedAmpDevLineOutputPower": speedAmpDevLineOutputPower,
       "speedAmpDevBackreflectionThreshold": speedAmpDevBackreflectionThreshold,
       "speedAmpDevShutdownThreshold": speedAmpDevShutdownThreshold,
       "speedAmpDevBackreflectionRatio": speedAmpDevBackreflectionRatio,
       "speedAmpDevConfigTable": speedAmpDevConfigTable,
       "speedAmpDevConfigEntry": speedAmpDevConfigEntry,
       "speedAmpDevCfgSlot": speedAmpDevCfgSlot,
       "speedAmpDevCfgGainValue": speedAmpDevCfgGainValue,
       "speedAmpDevCfgPoutValue": speedAmpDevCfgPoutValue,
       "speedAmpDevCfgPumpPwr": speedAmpDevCfgPumpPwr,
       "speedAmpDevCfgModeValue": speedAmpDevCfgModeValue,
       "speedAmpDevCfgPowerSafetyModeValue": speedAmpDevCfgPowerSafetyModeValue,
       "speedAmpDevCfgLosInputThresholdValue": speedAmpDevCfgLosInputThresholdValue,
       "speedAmpDevCfgLinePortDescription": speedAmpDevCfgLinePortDescription,
       "speedAmpDevCfgClientPortDescription": speedAmpDevCfgClientPortDescription,
       "speedAmpDevCfgAlarmReporting": speedAmpDevCfgAlarmReporting,
       "speedAmpDevCfgAlarmSchedule": speedAmpDevCfgAlarmSchedule,
       "speedAmpDevCfgBackreflectionThresholdValue": speedAmpDevCfgBackreflectionThresholdValue,
       "speedAmpDevAlarmTable": speedAmpDevAlarmTable,
       "speedAmpDevAlarmEntry": speedAmpDevAlarmEntry,
       "speedAmpDevAlarmSlot": speedAmpDevAlarmSlot,
       "speedAmpDevAlarmOpticalInput": speedAmpDevAlarmOpticalInput,
       "speedAmpDevAlarmOpticalOutput": speedAmpDevAlarmOpticalOutput,
       "speedAmpDevAlarmModuleTemperature": speedAmpDevAlarmModuleTemperature,
       "speedAmpDevAlarmPumpTemperature": speedAmpDevAlarmPumpTemperature,
       "speedAmpDevAlarmPumpDriveCurrent": speedAmpDevAlarmPumpDriveCurrent,
       "speedAmpDevAlarmSupplyVoltage": speedAmpDevAlarmSupplyVoltage,
       "speedAmpDevAlarmAutoshutdown": speedAmpDevAlarmAutoshutdown,
       "speedAmpDevAlarmSecurityMonitor": speedAmpDevAlarmSecurityMonitor,
       "speedAmpDevAlarmBackref": speedAmpDevAlarmBackref,
       "speedAmpModuleSFPAlarmTable": speedAmpModuleSFPAlarmTable,
       "speedAmpModuleSFPAlarmEntry": speedAmpModuleSFPAlarmEntry,
       "speedAmpMSFPAIndex": speedAmpMSFPAIndex,
       "speedAmpMSFPASlot": speedAmpMSFPASlot,
       "speedAmpMSFPAPort": speedAmpMSFPAPort,
       "speedAmpMSFPARxPowerAlarm": speedAmpMSFPARxPowerAlarm,
       "speedAmpMSFPATxPowerAlarm": speedAmpMSFPATxPowerAlarm,
       "speedAmpMSFPATxBiasAlarm": speedAmpMSFPATxBiasAlarm,
       "speedAmpMSFPATemperatureAlarm": speedAmpMSFPATemperatureAlarm,
       "speedAmpMSFPADWDMAlarm": speedAmpMSFPADWDMAlarm}
)
