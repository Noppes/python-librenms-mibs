# SNMP MIB module (SPEED-MULTILINE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\pandacom\SPEED-MULTILINE-MIB

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

(FixedDiv100,) = mibBuilder.importSymbols(
    "PanDacom-MIB",
    "FixedDiv100")

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

speedMultiline = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 3652, 3, 3, 6)
)
if mibBuilder.loadTexts:
    speedMultiline.setRevisions(
        ("2019-11-04 00:00",
         "2019-10-31 00:00",
         "2019-07-31 00:00",
         "2019-05-22 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_SpeedMultilineMOverviewTable_Object = MibTable
speedMultilineMOverviewTable = _SpeedMultilineMOverviewTable_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 3, 6, 1)
)
if mibBuilder.loadTexts:
    speedMultilineMOverviewTable.setStatus("current")
_SpeedMultilineMOverviewEntry_Object = MibTableRow
speedMultilineMOverviewEntry = _SpeedMultilineMOverviewEntry_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 3, 6, 1, 1)
)
speedMultilineMOverviewEntry.setIndexNames(
    (0, "SPEED-MULTILINE-MIB", "speedMultilineMOverviewIndex"),
)
if mibBuilder.loadTexts:
    speedMultilineMOverviewEntry.setStatus("current")


class _SpeedMultilineMOverviewIndex_Type(Integer32):
    """Custom type speedMultilineMOverviewIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_SpeedMultilineMOverviewIndex_Type.__name__ = "Integer32"
_SpeedMultilineMOverviewIndex_Object = MibTableColumn
speedMultilineMOverviewIndex = _SpeedMultilineMOverviewIndex_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 3, 6, 1, 1, 1),
    _SpeedMultilineMOverviewIndex_Type()
)
speedMultilineMOverviewIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    speedMultilineMOverviewIndex.setStatus("current")


class _SpeedMultilineMSlot_Type(Integer32):
    """Custom type speedMultilineMSlot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 19),
    )


_SpeedMultilineMSlot_Type.__name__ = "Integer32"
_SpeedMultilineMSlot_Object = MibTableColumn
speedMultilineMSlot = _SpeedMultilineMSlot_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 3, 6, 1, 1, 2),
    _SpeedMultilineMSlot_Type()
)
speedMultilineMSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    speedMultilineMSlot.setStatus("current")


class _SpeedMultilineMDevice_Type(Integer32):
    """Custom type speedMultilineMDevice based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              21,
              22,
              23,
              24,
              255)
        )
    )
    namedValues = NamedValues(
        *(("notAvailable", 0),
          ("speedDuallineSFP2R", 21),
          ("speedDualline10G3R", 22),
          ("speedQuadline10G3R", 23),
          ("speedSixline10G3R", 24),
          ("unknown", 255))
    )


_SpeedMultilineMDevice_Type.__name__ = "Integer32"
_SpeedMultilineMDevice_Object = MibTableColumn
speedMultilineMDevice = _SpeedMultilineMDevice_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 3, 6, 1, 1, 3),
    _SpeedMultilineMDevice_Type()
)
speedMultilineMDevice.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    speedMultilineMDevice.setStatus("current")


class _SpeedMultilineMState_Type(Integer32):
    """Custom type speedMultilineMState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              255)
        )
    )
    namedValues = NamedValues(
        *(("notAvailable", 0),
          ("running", 1),
          ("resetSoftware", 2),
          ("resetConfig", 3),
          ("resetRegistration", 4),
          ("resetHardware", 5),
          ("unknown", 255))
    )


_SpeedMultilineMState_Type.__name__ = "Integer32"
_SpeedMultilineMState_Object = MibTableColumn
speedMultilineMState = _SpeedMultilineMState_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 3, 6, 1, 1, 4),
    _SpeedMultilineMState_Type()
)
speedMultilineMState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    speedMultilineMState.setStatus("current")


class _SpeedMultilineMSysName_Type(DisplayString):
    """Custom type speedMultilineMSysName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_SpeedMultilineMSysName_Type.__name__ = "DisplayString"
_SpeedMultilineMSysName_Object = MibTableColumn
speedMultilineMSysName = _SpeedMultilineMSysName_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 3, 6, 1, 1, 5),
    _SpeedMultilineMSysName_Type()
)
speedMultilineMSysName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    speedMultilineMSysName.setStatus("current")
_SpeedMultilineMSysUpTime_Type = TimeTicks
_SpeedMultilineMSysUpTime_Object = MibTableColumn
speedMultilineMSysUpTime = _SpeedMultilineMSysUpTime_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 3, 6, 1, 1, 6),
    _SpeedMultilineMSysUpTime_Type()
)
speedMultilineMSysUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    speedMultilineMSysUpTime.setStatus("current")
_SpeedMultilineMTemperature_Type = Integer32
_SpeedMultilineMTemperature_Object = MibTableColumn
speedMultilineMTemperature = _SpeedMultilineMTemperature_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 3, 6, 1, 1, 7),
    _SpeedMultilineMTemperature_Type()
)
speedMultilineMTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    speedMultilineMTemperature.setStatus("current")


class _SpeedMultilineMAlarmState_Type(Integer32):
    """Custom type speedMultilineMAlarmState based on Integer32"""
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
              128,
              129,
              130,
              131,
              132,
              133,
              134)
        )
    )
    namedValues = NamedValues(
        *(("notAvailable", 0),
          ("noAlarm", 1),
          ("activeWarning", 2),
          ("activeAlarm", 3),
          ("lowWarning", 4),
          ("lowAlarm", 5),
          ("highWarning", 6),
          ("highAlarm", 7),
          ("noAlarms", 128),
          ("activeWarnings", 129),
          ("activeAlarms", 130),
          ("lowWarnings", 131),
          ("lowAlarms", 132),
          ("highWarnings", 133),
          ("highAlarms", 134))
    )


_SpeedMultilineMAlarmState_Type.__name__ = "Integer32"
_SpeedMultilineMAlarmState_Object = MibTableColumn
speedMultilineMAlarmState = _SpeedMultilineMAlarmState_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 3, 6, 1, 1, 8),
    _SpeedMultilineMAlarmState_Type()
)
speedMultilineMAlarmState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    speedMultilineMAlarmState.setStatus("current")


class _SpeedMultilineMAppImage_Type(DisplayString):
    """Custom type speedMultilineMAppImage based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_SpeedMultilineMAppImage_Type.__name__ = "DisplayString"
_SpeedMultilineMAppImage_Object = MibTableColumn
speedMultilineMAppImage = _SpeedMultilineMAppImage_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 3, 6, 1, 1, 9),
    _SpeedMultilineMAppImage_Type()
)
speedMultilineMAppImage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    speedMultilineMAppImage.setStatus("current")


class _SpeedMultilineMHwVersion_Type(DisplayString):
    """Custom type speedMultilineMHwVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_SpeedMultilineMHwVersion_Type.__name__ = "DisplayString"
_SpeedMultilineMHwVersion_Object = MibTableColumn
speedMultilineMHwVersion = _SpeedMultilineMHwVersion_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 3, 6, 1, 1, 10),
    _SpeedMultilineMHwVersion_Type()
)
speedMultilineMHwVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    speedMultilineMHwVersion.setStatus("current")


class _SpeedMultilineMDevSerialNumber_Type(DisplayString):
    """Custom type speedMultilineMDevSerialNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 17),
    )


_SpeedMultilineMDevSerialNumber_Type.__name__ = "DisplayString"
_SpeedMultilineMDevSerialNumber_Object = MibTableColumn
speedMultilineMDevSerialNumber = _SpeedMultilineMDevSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 3, 6, 1, 1, 11),
    _SpeedMultilineMDevSerialNumber_Type()
)
speedMultilineMDevSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    speedMultilineMDevSerialNumber.setStatus("current")


class _SpeedMultilineMTemperatureAlarm_Type(Integer32):
    """Custom type speedMultilineMTemperatureAlarm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              3)
        )
    )
    namedValues = NamedValues(
        *(("noAlarm", 0),
          ("activeWarning", 1),
          ("activeAlarm", 3))
    )


_SpeedMultilineMTemperatureAlarm_Type.__name__ = "Integer32"
_SpeedMultilineMTemperatureAlarm_Object = MibTableColumn
speedMultilineMTemperatureAlarm = _SpeedMultilineMTemperatureAlarm_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 3, 6, 1, 1, 12),
    _SpeedMultilineMTemperatureAlarm_Type()
)
speedMultilineMTemperatureAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    speedMultilineMTemperatureAlarm.setStatus("current")


class _SpeedMultilineMBoardHWAlarm_Type(Integer32):
    """Custom type speedMultilineMBoardHWAlarm based on Integer32"""
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
              128,
              129,
              130,
              131,
              132,
              133,
              134,
              255)
        )
    )
    namedValues = NamedValues(
        *(("notAvailable", 0),
          ("noAlarm", 1),
          ("activeWarning", 2),
          ("activeAlarm", 3),
          ("lowWarning", 4),
          ("lowAlarm", 5),
          ("highWarning", 6),
          ("highAlarm", 7),
          ("noAlarms", 128),
          ("activeWarnings", 129),
          ("activeAlarms", 130),
          ("lowWarnings", 131),
          ("lowAlarms", 132),
          ("highWarnings", 133),
          ("highAlarms", 134),
          ("unknown", 255))
    )


_SpeedMultilineMBoardHWAlarm_Type.__name__ = "Integer32"
_SpeedMultilineMBoardHWAlarm_Object = MibTableColumn
speedMultilineMBoardHWAlarm = _SpeedMultilineMBoardHWAlarm_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 3, 6, 1, 1, 13),
    _SpeedMultilineMBoardHWAlarm_Type()
)
speedMultilineMBoardHWAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    speedMultilineMBoardHWAlarm.setStatus("current")


class _SpeedMultilineMPortTxConnection_Type(Integer32):
    """Custom type speedMultilineMPortTxConnection based on Integer32"""
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
          ("connect1to3and2to4", 1),
          ("connect1to4and2to3", 2),
          ("unknown", 255))
    )


_SpeedMultilineMPortTxConnection_Type.__name__ = "Integer32"
_SpeedMultilineMPortTxConnection_Object = MibTableColumn
speedMultilineMPortTxConnection = _SpeedMultilineMPortTxConnection_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 3, 6, 1, 1, 14),
    _SpeedMultilineMPortTxConnection_Type()
)
speedMultilineMPortTxConnection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    speedMultilineMPortTxConnection.setStatus("current")


class _SpeedMultilineMTempWarningLevel_Type(Integer32):
    """Custom type speedMultilineMTempWarningLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 60),
    )


_SpeedMultilineMTempWarningLevel_Type.__name__ = "Integer32"
_SpeedMultilineMTempWarningLevel_Object = MibTableColumn
speedMultilineMTempWarningLevel = _SpeedMultilineMTempWarningLevel_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 3, 6, 1, 1, 15),
    _SpeedMultilineMTempWarningLevel_Type()
)
speedMultilineMTempWarningLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    speedMultilineMTempWarningLevel.setStatus("current")
_SpeedMultilineMTempAlarmLevel_Type = Integer32
_SpeedMultilineMTempAlarmLevel_Object = MibTableColumn
speedMultilineMTempAlarmLevel = _SpeedMultilineMTempAlarmLevel_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 3, 6, 1, 1, 16),
    _SpeedMultilineMTempAlarmLevel_Type()
)
speedMultilineMTempAlarmLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    speedMultilineMTempAlarmLevel.setStatus("current")


class _SpeedMultilineMCLIUserTimeout_Type(Integer32):
    """Custom type speedMultilineMCLIUserTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(120, 3600),
    )


_SpeedMultilineMCLIUserTimeout_Type.__name__ = "Integer32"
_SpeedMultilineMCLIUserTimeout_Object = MibTableColumn
speedMultilineMCLIUserTimeout = _SpeedMultilineMCLIUserTimeout_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 3, 6, 1, 1, 17),
    _SpeedMultilineMCLIUserTimeout_Type()
)
speedMultilineMCLIUserTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    speedMultilineMCLIUserTimeout.setStatus("current")
_SpeedMultilinePortConfigTable_Object = MibTable
speedMultilinePortConfigTable = _SpeedMultilinePortConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 3, 6, 2)
)
if mibBuilder.loadTexts:
    speedMultilinePortConfigTable.setStatus("current")
_SpeedMultilinePortConfigEntry_Object = MibTableRow
speedMultilinePortConfigEntry = _SpeedMultilinePortConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 3, 6, 2, 1)
)
speedMultilinePortConfigEntry.setIndexNames(
    (0, "SPEED-MULTILINE-MIB", "speedMultilinePortIndex"),
)
if mibBuilder.loadTexts:
    speedMultilinePortConfigEntry.setStatus("current")


class _SpeedMultilinePortIndex_Type(Integer32):
    """Custom type speedMultilinePortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1900),
    )


_SpeedMultilinePortIndex_Type.__name__ = "Integer32"
_SpeedMultilinePortIndex_Object = MibTableColumn
speedMultilinePortIndex = _SpeedMultilinePortIndex_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 3, 6, 2, 1, 1),
    _SpeedMultilinePortIndex_Type()
)
speedMultilinePortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    speedMultilinePortIndex.setStatus("current")


class _SpeedMultilinePortSlot_Type(Integer32):
    """Custom type speedMultilinePortSlot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 19),
    )


_SpeedMultilinePortSlot_Type.__name__ = "Integer32"
_SpeedMultilinePortSlot_Object = MibTableColumn
speedMultilinePortSlot = _SpeedMultilinePortSlot_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 3, 6, 2, 1, 2),
    _SpeedMultilinePortSlot_Type()
)
speedMultilinePortSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    speedMultilinePortSlot.setStatus("current")
_SpeedMultilinePort_Type = Integer32
_SpeedMultilinePort_Object = MibTableColumn
speedMultilinePort = _SpeedMultilinePort_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 3, 6, 2, 1, 3),
    _SpeedMultilinePort_Type()
)
speedMultilinePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    speedMultilinePort.setStatus("current")


class _SpeedMultilinePortDescription_Type(DisplayString):
    """Custom type speedMultilinePortDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_SpeedMultilinePortDescription_Type.__name__ = "DisplayString"
_SpeedMultilinePortDescription_Object = MibTableColumn
speedMultilinePortDescription = _SpeedMultilinePortDescription_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 3, 6, 2, 1, 4),
    _SpeedMultilinePortDescription_Type()
)
speedMultilinePortDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    speedMultilinePortDescription.setStatus("current")


class _SpeedMultilinePortOperState_Type(Integer32):
    """Custom type speedMultilinePortOperState based on Integer32"""
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
        *(("notAvailable", 0),
          ("down", 1),
          ("up", 2),
          ("loop", 3),
          ("downLLCF", 4),
          ("downTxFault", 5),
          ("downRxLevel", 6),
          ("downTxLevel", 7),
          ("bertRunning", 8),
          ("unknown", 255))
    )


_SpeedMultilinePortOperState_Type.__name__ = "Integer32"
_SpeedMultilinePortOperState_Object = MibTableColumn
speedMultilinePortOperState = _SpeedMultilinePortOperState_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 3, 6, 2, 1, 5),
    _SpeedMultilinePortOperState_Type()
)
speedMultilinePortOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    speedMultilinePortOperState.setStatus("current")


class _SpeedMultilinePortAdminConfig_Type(Integer32):
    """Custom type speedMultilinePortAdminConfig based on Integer32"""
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
          ("adminDown", 1),
          ("adminUp", 2))
    )


_SpeedMultilinePortAdminConfig_Type.__name__ = "Integer32"
_SpeedMultilinePortAdminConfig_Object = MibTableColumn
speedMultilinePortAdminConfig = _SpeedMultilinePortAdminConfig_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 3, 6, 2, 1, 6),
    _SpeedMultilinePortAdminConfig_Type()
)
speedMultilinePortAdminConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    speedMultilinePortAdminConfig.setStatus("current")


class _SpeedMultilinePortLoopConfig_Type(Integer32):
    """Custom type speedMultilinePortLoopConfig based on Integer32"""
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
          ("off", 1),
          ("on", 2))
    )


_SpeedMultilinePortLoopConfig_Type.__name__ = "Integer32"
_SpeedMultilinePortLoopConfig_Object = MibTableColumn
speedMultilinePortLoopConfig = _SpeedMultilinePortLoopConfig_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 3, 6, 2, 1, 7),
    _SpeedMultilinePortLoopConfig_Type()
)
speedMultilinePortLoopConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    speedMultilinePortLoopConfig.setStatus("current")


class _SpeedMultilinePortAlarmDeactivation_Type(Integer32):
    """Custom type speedMultilinePortAlarmDeactivation based on Integer32"""
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
          ("activateAlarms", 1),
          ("deactivateBySchedule", 2),
          ("deactivatePermanently", 3))
    )


_SpeedMultilinePortAlarmDeactivation_Type.__name__ = "Integer32"
_SpeedMultilinePortAlarmDeactivation_Object = MibTableColumn
speedMultilinePortAlarmDeactivation = _SpeedMultilinePortAlarmDeactivation_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 3, 6, 2, 1, 8),
    _SpeedMultilinePortAlarmDeactivation_Type()
)
speedMultilinePortAlarmDeactivation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    speedMultilinePortAlarmDeactivation.setStatus("current")


class _SpeedMultilinePortAlarmSchedule_Type(Integer32):
    """Custom type speedMultilinePortAlarmSchedule based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1200),
    )


_SpeedMultilinePortAlarmSchedule_Type.__name__ = "Integer32"
_SpeedMultilinePortAlarmSchedule_Object = MibTableColumn
speedMultilinePortAlarmSchedule = _SpeedMultilinePortAlarmSchedule_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 3, 6, 2, 1, 9),
    _SpeedMultilinePortAlarmSchedule_Type()
)
speedMultilinePortAlarmSchedule.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    speedMultilinePortAlarmSchedule.setStatus("current")


class _SpeedMultilinePortProtocol_Type(Integer32):
    """Custom type speedMultilinePortProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              5,
              7,
              18,
              20,
              21,
              22,
              24,
              25,
              26,
              27)
        )
    )
    namedValues = NamedValues(
        *(("notavailable", 0),
          ("fc8G", 5),
          ("eth10G", 7),
          ("eth1G", 18),
          ("fc4G", 20),
          ("fc2G", 21),
          ("eth2G", 22),
          ("ib5G", 24),
          ("ib10G", 25),
          ("stm64", 26),
          ("stm16", 27))
    )


_SpeedMultilinePortProtocol_Type.__name__ = "Integer32"
_SpeedMultilinePortProtocol_Object = MibTableColumn
speedMultilinePortProtocol = _SpeedMultilinePortProtocol_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 3, 6, 2, 1, 10),
    _SpeedMultilinePortProtocol_Type()
)
speedMultilinePortProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    speedMultilinePortProtocol.setStatus("current")


class _SpeedMultilinePortLLCFconfig_Type(Integer32):
    """Custom type speedMultilinePortLLCFconfig based on Integer32"""
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
          ("off", 1),
          ("on", 2))
    )


_SpeedMultilinePortLLCFconfig_Type.__name__ = "Integer32"
_SpeedMultilinePortLLCFconfig_Object = MibTableColumn
speedMultilinePortLLCFconfig = _SpeedMultilinePortLLCFconfig_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 3, 6, 2, 1, 11),
    _SpeedMultilinePortLLCFconfig_Type()
)
speedMultilinePortLLCFconfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    speedMultilinePortLLCFconfig.setStatus("current")


class _SpeedMultilinePortXCVtunableConfigSelection_Type(Integer32):
    """Custom type speedMultilinePortXCVtunableConfigSelection based on Integer32"""
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
          ("xcvInternal", 1),
          ("configFile", 2),
          ("unknown", 255))
    )


_SpeedMultilinePortXCVtunableConfigSelection_Type.__name__ = "Integer32"
_SpeedMultilinePortXCVtunableConfigSelection_Object = MibTableColumn
speedMultilinePortXCVtunableConfigSelection = _SpeedMultilinePortXCVtunableConfigSelection_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 3, 6, 2, 1, 12),
    _SpeedMultilinePortXCVtunableConfigSelection_Type()
)
speedMultilinePortXCVtunableConfigSelection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    speedMultilinePortXCVtunableConfigSelection.setStatus("current")


class _SpeedMultilinePortXCVtunChannelConfig_Type(DisplayString):
    """Custom type speedMultilinePortXCVtunChannelConfig based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 4),
    )


_SpeedMultilinePortXCVtunChannelConfig_Type.__name__ = "DisplayString"
_SpeedMultilinePortXCVtunChannelConfig_Object = MibTableColumn
speedMultilinePortXCVtunChannelConfig = _SpeedMultilinePortXCVtunChannelConfig_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 3, 6, 2, 1, 13),
    _SpeedMultilinePortXCVtunChannelConfig_Type()
)
speedMultilinePortXCVtunChannelConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    speedMultilinePortXCVtunChannelConfig.setStatus("current")


class _SpeedMultilinePortXCVTunWavelengthConfig_Type(Integer32):
    """Custom type speedMultilinePortXCVTunWavelengthConfig based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1528350, 1577100),
    )


_SpeedMultilinePortXCVTunWavelengthConfig_Type.__name__ = "Integer32"
_SpeedMultilinePortXCVTunWavelengthConfig_Object = MibTableColumn
speedMultilinePortXCVTunWavelengthConfig = _SpeedMultilinePortXCVTunWavelengthConfig_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 3, 6, 2, 1, 14),
    _SpeedMultilinePortXCVTunWavelengthConfig_Type()
)
speedMultilinePortXCVTunWavelengthConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    speedMultilinePortXCVTunWavelengthConfig.setStatus("current")


class _SpeedMultilinePortCopperSpeed_Type(Integer32):
    """Custom type speedMultilinePortCopperSpeed based on Integer32"""
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
              12)
        )
    )
    namedValues = NamedValues(
        *(("notAvailable", 0),
          ("eth10MBhdxFORCED", 1),
          ("eth10MBhdxAUTO", 2),
          ("eth10MBfdxFORCED", 3),
          ("eth10MB", 4),
          ("eth100MBhdxFORCED", 5),
          ("eth100MBhdx", 6),
          ("eth100MBfdxFORCED", 7),
          ("eth100MB", 8),
          ("eth1000MB", 12))
    )


_SpeedMultilinePortCopperSpeed_Type.__name__ = "Integer32"
_SpeedMultilinePortCopperSpeed_Object = MibTableColumn
speedMultilinePortCopperSpeed = _SpeedMultilinePortCopperSpeed_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 3, 6, 2, 1, 15),
    _SpeedMultilinePortCopperSpeed_Type()
)
speedMultilinePortCopperSpeed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    speedMultilinePortCopperSpeed.setStatus("current")


class _SpeedMultilinePortCopperMDI_Type(Integer32):
    """Custom type speedMultilinePortCopperMDI based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("notAvailable", 0),
          ("mdi", 2),
          ("auto", 3))
    )


_SpeedMultilinePortCopperMDI_Type.__name__ = "Integer32"
_SpeedMultilinePortCopperMDI_Object = MibTableColumn
speedMultilinePortCopperMDI = _SpeedMultilinePortCopperMDI_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 3, 6, 2, 1, 16),
    _SpeedMultilinePortCopperMDI_Type()
)
speedMultilinePortCopperMDI.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    speedMultilinePortCopperMDI.setStatus("current")
_SpeedMultilinePortXCVInfoTable_Object = MibTable
speedMultilinePortXCVInfoTable = _SpeedMultilinePortXCVInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 3, 6, 3)
)
if mibBuilder.loadTexts:
    speedMultilinePortXCVInfoTable.setStatus("current")
_SpeedMultilinePortXCVInfoEntry_Object = MibTableRow
speedMultilinePortXCVInfoEntry = _SpeedMultilinePortXCVInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 3, 6, 3, 1)
)
speedMultilinePortXCVInfoEntry.setIndexNames(
    (0, "SPEED-MULTILINE-MIB", "speedMultilinePortXCVIndex"),
)
if mibBuilder.loadTexts:
    speedMultilinePortXCVInfoEntry.setStatus("current")


class _SpeedMultilinePortXCVIndex_Type(Integer32):
    """Custom type speedMultilinePortXCVIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1900),
    )


_SpeedMultilinePortXCVIndex_Type.__name__ = "Integer32"
_SpeedMultilinePortXCVIndex_Object = MibTableColumn
speedMultilinePortXCVIndex = _SpeedMultilinePortXCVIndex_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 3, 6, 3, 1, 1),
    _SpeedMultilinePortXCVIndex_Type()
)
speedMultilinePortXCVIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    speedMultilinePortXCVIndex.setStatus("current")
_SpeedMultilinePortXCVSlot_Type = Integer32
_SpeedMultilinePortXCVSlot_Object = MibTableColumn
speedMultilinePortXCVSlot = _SpeedMultilinePortXCVSlot_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 3, 6, 3, 1, 2),
    _SpeedMultilinePortXCVSlot_Type()
)
speedMultilinePortXCVSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    speedMultilinePortXCVSlot.setStatus("current")
_SpeedMultilinePortXCVPort_Type = Integer32
_SpeedMultilinePortXCVPort_Object = MibTableColumn
speedMultilinePortXCVPort = _SpeedMultilinePortXCVPort_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 3, 6, 3, 1, 3),
    _SpeedMultilinePortXCVPort_Type()
)
speedMultilinePortXCVPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    speedMultilinePortXCVPort.setStatus("current")


class _SpeedMultilinePortXCVState_Type(Integer32):
    """Custom type speedMultilinePortXCVState based on Integer32"""
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
          ("xcvRemoved", 1),
          ("xcvInstalled", 2),
          ("xcvTxFault", 3),
          ("unknown", 255))
    )


_SpeedMultilinePortXCVState_Type.__name__ = "Integer32"
_SpeedMultilinePortXCVState_Object = MibTableColumn
speedMultilinePortXCVState = _SpeedMultilinePortXCVState_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 3, 6, 3, 1, 4),
    _SpeedMultilinePortXCVState_Type()
)
speedMultilinePortXCVState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    speedMultilinePortXCVState.setStatus("current")


class _SpeedMultilinePortXCVVendorName_Type(DisplayString):
    """Custom type speedMultilinePortXCVVendorName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_SpeedMultilinePortXCVVendorName_Type.__name__ = "DisplayString"
_SpeedMultilinePortXCVVendorName_Object = MibTableColumn
speedMultilinePortXCVVendorName = _SpeedMultilinePortXCVVendorName_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 3, 6, 3, 1, 5),
    _SpeedMultilinePortXCVVendorName_Type()
)
speedMultilinePortXCVVendorName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    speedMultilinePortXCVVendorName.setStatus("current")


class _SpeedMultilinePortXCVVendorPartNumber_Type(DisplayString):
    """Custom type speedMultilinePortXCVVendorPartNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_SpeedMultilinePortXCVVendorPartNumber_Type.__name__ = "DisplayString"
_SpeedMultilinePortXCVVendorPartNumber_Object = MibTableColumn
speedMultilinePortXCVVendorPartNumber = _SpeedMultilinePortXCVVendorPartNumber_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 3, 6, 3, 1, 6),
    _SpeedMultilinePortXCVVendorPartNumber_Type()
)
speedMultilinePortXCVVendorPartNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    speedMultilinePortXCVVendorPartNumber.setStatus("current")


class _SpeedMultilinePortXCVVendorSerialNumber_Type(DisplayString):
    """Custom type speedMultilinePortXCVVendorSerialNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_SpeedMultilinePortXCVVendorSerialNumber_Type.__name__ = "DisplayString"
_SpeedMultilinePortXCVVendorSerialNumber_Object = MibTableColumn
speedMultilinePortXCVVendorSerialNumber = _SpeedMultilinePortXCVVendorSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 3, 6, 3, 1, 7),
    _SpeedMultilinePortXCVVendorSerialNumber_Type()
)
speedMultilinePortXCVVendorSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    speedMultilinePortXCVVendorSerialNumber.setStatus("current")


class _SpeedMultilinePortXCVType_Type(Integer32):
    """Custom type speedMultilinePortXCVType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              10,
              254,
              255)
        )
    )
    namedValues = NamedValues(
        *(("unspecified", 0),
          ("tSFP", 1),
          ("tXFP", 2),
          ("tDWDMSFP", 3),
          ("tQSFP", 4),
          ("tQSFPP", 5),
          ("tQSFP28", 10),
          ("tCopperSFP", 254),
          ("vendorSpecific", 255))
    )


_SpeedMultilinePortXCVType_Type.__name__ = "Integer32"
_SpeedMultilinePortXCVType_Object = MibTableColumn
speedMultilinePortXCVType = _SpeedMultilinePortXCVType_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 3, 6, 3, 1, 8),
    _SpeedMultilinePortXCVType_Type()
)
speedMultilinePortXCVType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    speedMultilinePortXCVType.setStatus("current")


class _SpeedMultilinePortXCVConnector_Type(Integer32):
    """Custom type speedMultilinePortXCVConnector based on Integer32"""
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
              255)
        )
    )
    namedValues = NamedValues(
        *(("unspecified", 0),
          ("cLC", 1),
          ("cSC", 2),
          ("cMPO", 3),
          ("cRJ45", 4),
          ("cFC", 5),
          ("cBNC", 6),
          ("cFJ", 7),
          ("cMTRJ", 8),
          ("cMU", 9),
          ("cSG", 10),
          ("cOpticalPigtail", 11),
          ("cHSSDC", 12),
          ("cCP", 13),
          ("cMXC", 14),
          ("unknown", 255))
    )


_SpeedMultilinePortXCVConnector_Type.__name__ = "Integer32"
_SpeedMultilinePortXCVConnector_Object = MibTableColumn
speedMultilinePortXCVConnector = _SpeedMultilinePortXCVConnector_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 3, 6, 3, 1, 9),
    _SpeedMultilinePortXCVConnector_Type()
)
speedMultilinePortXCVConnector.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    speedMultilinePortXCVConnector.setStatus("current")
_SpeedMultilinePortXCVWavelength_Type = Integer32
_SpeedMultilinePortXCVWavelength_Object = MibTableColumn
speedMultilinePortXCVWavelength = _SpeedMultilinePortXCVWavelength_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 3, 6, 3, 1, 10),
    _SpeedMultilinePortXCVWavelength_Type()
)
speedMultilinePortXCVWavelength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    speedMultilinePortXCVWavelength.setStatus("current")


class _SpeedMultilinePortXCVDMIState_Type(Integer32):
    """Custom type speedMultilinePortXCVDMIState based on Integer32"""
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
          ("dmiAvailable", 1),
          ("notImplemented", 2),
          ("unknown", 255))
    )


_SpeedMultilinePortXCVDMIState_Type.__name__ = "Integer32"
_SpeedMultilinePortXCVDMIState_Object = MibTableColumn
speedMultilinePortXCVDMIState = _SpeedMultilinePortXCVDMIState_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 3, 6, 3, 1, 11),
    _SpeedMultilinePortXCVDMIState_Type()
)
speedMultilinePortXCVDMIState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    speedMultilinePortXCVDMIState.setStatus("current")
_SpeedMultilinePortXCVValueTable_Object = MibTable
speedMultilinePortXCVValueTable = _SpeedMultilinePortXCVValueTable_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 3, 6, 4)
)
if mibBuilder.loadTexts:
    speedMultilinePortXCVValueTable.setStatus("current")
_SpeedMultilinePortXCVValueEntry_Object = MibTableRow
speedMultilinePortXCVValueEntry = _SpeedMultilinePortXCVValueEntry_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 3, 6, 4, 1)
)
speedMultilinePortXCVValueEntry.setIndexNames(
    (0, "SPEED-MULTILINE-MIB", "speedMultilinePortXCVDMIIndex"),
)
if mibBuilder.loadTexts:
    speedMultilinePortXCVValueEntry.setStatus("current")


class _SpeedMultilinePortXCVDMIIndex_Type(Integer32):
    """Custom type speedMultilinePortXCVDMIIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1900),
    )


_SpeedMultilinePortXCVDMIIndex_Type.__name__ = "Integer32"
_SpeedMultilinePortXCVDMIIndex_Object = MibTableColumn
speedMultilinePortXCVDMIIndex = _SpeedMultilinePortXCVDMIIndex_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 3, 6, 4, 1, 1),
    _SpeedMultilinePortXCVDMIIndex_Type()
)
speedMultilinePortXCVDMIIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    speedMultilinePortXCVDMIIndex.setStatus("current")
_SpeedMultilinePortXCVDMISlot_Type = Integer32
_SpeedMultilinePortXCVDMISlot_Object = MibTableColumn
speedMultilinePortXCVDMISlot = _SpeedMultilinePortXCVDMISlot_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 3, 6, 4, 1, 2),
    _SpeedMultilinePortXCVDMISlot_Type()
)
speedMultilinePortXCVDMISlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    speedMultilinePortXCVDMISlot.setStatus("current")
_SpeedMultilinePortXCVDMIPort_Type = Integer32
_SpeedMultilinePortXCVDMIPort_Object = MibTableColumn
speedMultilinePortXCVDMIPort = _SpeedMultilinePortXCVDMIPort_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 3, 6, 4, 1, 3),
    _SpeedMultilinePortXCVDMIPort_Type()
)
speedMultilinePortXCVDMIPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    speedMultilinePortXCVDMIPort.setStatus("current")
_SpeedMultilinePortXCVDMIRxLevel_Type = FixedDiv100
_SpeedMultilinePortXCVDMIRxLevel_Object = MibTableColumn
speedMultilinePortXCVDMIRxLevel = _SpeedMultilinePortXCVDMIRxLevel_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 3, 6, 4, 1, 4),
    _SpeedMultilinePortXCVDMIRxLevel_Type()
)
speedMultilinePortXCVDMIRxLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    speedMultilinePortXCVDMIRxLevel.setStatus("current")
_SpeedMultilinePortXCVDMITxLevel_Type = FixedDiv100
_SpeedMultilinePortXCVDMITxLevel_Object = MibTableColumn
speedMultilinePortXCVDMITxLevel = _SpeedMultilinePortXCVDMITxLevel_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 3, 6, 4, 1, 5),
    _SpeedMultilinePortXCVDMITxLevel_Type()
)
speedMultilinePortXCVDMITxLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    speedMultilinePortXCVDMITxLevel.setStatus("current")
_SpeedMultilinePortXCVDMITxBias_Type = FixedDiv100
_SpeedMultilinePortXCVDMITxBias_Object = MibTableColumn
speedMultilinePortXCVDMITxBias = _SpeedMultilinePortXCVDMITxBias_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 3, 6, 4, 1, 6),
    _SpeedMultilinePortXCVDMITxBias_Type()
)
speedMultilinePortXCVDMITxBias.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    speedMultilinePortXCVDMITxBias.setStatus("current")
_SpeedMultilinePortXCVDMITemp_Type = Integer32
_SpeedMultilinePortXCVDMITemp_Object = MibTableColumn
speedMultilinePortXCVDMITemp = _SpeedMultilinePortXCVDMITemp_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 3, 6, 4, 1, 7),
    _SpeedMultilinePortXCVDMITemp_Type()
)
speedMultilinePortXCVDMITemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    speedMultilinePortXCVDMITemp.setStatus("current")
_SpeedMultilinePortXCVAlarmTable_Object = MibTable
speedMultilinePortXCVAlarmTable = _SpeedMultilinePortXCVAlarmTable_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 3, 6, 5)
)
if mibBuilder.loadTexts:
    speedMultilinePortXCVAlarmTable.setStatus("current")
_SpeedMultilinePortXCVAlarmEntry_Object = MibTableRow
speedMultilinePortXCVAlarmEntry = _SpeedMultilinePortXCVAlarmEntry_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 3, 6, 5, 1)
)
speedMultilinePortXCVAlarmEntry.setIndexNames(
    (0, "SPEED-MULTILINE-MIB", "speedMultilinePortAIndex"),
)
if mibBuilder.loadTexts:
    speedMultilinePortXCVAlarmEntry.setStatus("current")


class _SpeedMultilinePortAIndex_Type(Integer32):
    """Custom type speedMultilinePortAIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1900),
    )


_SpeedMultilinePortAIndex_Type.__name__ = "Integer32"
_SpeedMultilinePortAIndex_Object = MibTableColumn
speedMultilinePortAIndex = _SpeedMultilinePortAIndex_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 3, 6, 5, 1, 1),
    _SpeedMultilinePortAIndex_Type()
)
speedMultilinePortAIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    speedMultilinePortAIndex.setStatus("current")
_SpeedMultilinePortASlot_Type = Integer32
_SpeedMultilinePortASlot_Object = MibTableColumn
speedMultilinePortASlot = _SpeedMultilinePortASlot_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 3, 6, 5, 1, 2),
    _SpeedMultilinePortASlot_Type()
)
speedMultilinePortASlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    speedMultilinePortASlot.setStatus("current")
_SpeedMultilinePortAPort_Type = Integer32
_SpeedMultilinePortAPort_Object = MibTableColumn
speedMultilinePortAPort = _SpeedMultilinePortAPort_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 3, 6, 5, 1, 3),
    _SpeedMultilinePortAPort_Type()
)
speedMultilinePortAPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    speedMultilinePortAPort.setStatus("current")


class _SpeedMultilinePortXCVDMIRxLowAlarm_Type(Integer32):
    """Custom type speedMultilinePortXCVDMIRxLowAlarm based on Integer32"""
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
        *(("noAlarm", 0),
          ("activeWarning", 1),
          ("activeAlarm", 2),
          ("unknown", 255))
    )


_SpeedMultilinePortXCVDMIRxLowAlarm_Type.__name__ = "Integer32"
_SpeedMultilinePortXCVDMIRxLowAlarm_Object = MibTableColumn
speedMultilinePortXCVDMIRxLowAlarm = _SpeedMultilinePortXCVDMIRxLowAlarm_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 3, 6, 5, 1, 4),
    _SpeedMultilinePortXCVDMIRxLowAlarm_Type()
)
speedMultilinePortXCVDMIRxLowAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    speedMultilinePortXCVDMIRxLowAlarm.setStatus("current")


class _SpeedMultilinePortXCVDMIRxHighAlarm_Type(Integer32):
    """Custom type speedMultilinePortXCVDMIRxHighAlarm based on Integer32"""
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
        *(("noAlarm", 0),
          ("activeWarning", 1),
          ("activeAlarm", 2),
          ("unknown", 255))
    )


_SpeedMultilinePortXCVDMIRxHighAlarm_Type.__name__ = "Integer32"
_SpeedMultilinePortXCVDMIRxHighAlarm_Object = MibTableColumn
speedMultilinePortXCVDMIRxHighAlarm = _SpeedMultilinePortXCVDMIRxHighAlarm_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 3, 6, 5, 1, 5),
    _SpeedMultilinePortXCVDMIRxHighAlarm_Type()
)
speedMultilinePortXCVDMIRxHighAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    speedMultilinePortXCVDMIRxHighAlarm.setStatus("current")


class _SpeedMultilinePortXCVDMITxLowAlarm_Type(Integer32):
    """Custom type speedMultilinePortXCVDMITxLowAlarm based on Integer32"""
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
        *(("noAlarm", 0),
          ("activeWarning", 1),
          ("activeAlarm", 2),
          ("unknown", 255))
    )


_SpeedMultilinePortXCVDMITxLowAlarm_Type.__name__ = "Integer32"
_SpeedMultilinePortXCVDMITxLowAlarm_Object = MibTableColumn
speedMultilinePortXCVDMITxLowAlarm = _SpeedMultilinePortXCVDMITxLowAlarm_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 3, 6, 5, 1, 6),
    _SpeedMultilinePortXCVDMITxLowAlarm_Type()
)
speedMultilinePortXCVDMITxLowAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    speedMultilinePortXCVDMITxLowAlarm.setStatus("current")


class _SpeedMultilinePortXCVDMIBiasLowAlarm_Type(Integer32):
    """Custom type speedMultilinePortXCVDMIBiasLowAlarm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("noAlarm", 0),
          ("activeAlarm", 2),
          ("unknown", 255))
    )


_SpeedMultilinePortXCVDMIBiasLowAlarm_Type.__name__ = "Integer32"
_SpeedMultilinePortXCVDMIBiasLowAlarm_Object = MibTableColumn
speedMultilinePortXCVDMIBiasLowAlarm = _SpeedMultilinePortXCVDMIBiasLowAlarm_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 3, 6, 5, 1, 7),
    _SpeedMultilinePortXCVDMIBiasLowAlarm_Type()
)
speedMultilinePortXCVDMIBiasLowAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    speedMultilinePortXCVDMIBiasLowAlarm.setStatus("current")


class _SpeedMultilinePortXCVDMIBiasHighAlarm_Type(Integer32):
    """Custom type speedMultilinePortXCVDMIBiasHighAlarm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("noAlarm", 0),
          ("activeAlarm", 2),
          ("unknown", 255))
    )


_SpeedMultilinePortXCVDMIBiasHighAlarm_Type.__name__ = "Integer32"
_SpeedMultilinePortXCVDMIBiasHighAlarm_Object = MibTableColumn
speedMultilinePortXCVDMIBiasHighAlarm = _SpeedMultilinePortXCVDMIBiasHighAlarm_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 3, 6, 5, 1, 8),
    _SpeedMultilinePortXCVDMIBiasHighAlarm_Type()
)
speedMultilinePortXCVDMIBiasHighAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    speedMultilinePortXCVDMIBiasHighAlarm.setStatus("current")


class _SpeedMultilinePortXCVTempHighAlarm_Type(Integer32):
    """Custom type speedMultilinePortXCVTempHighAlarm based on Integer32"""
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
        *(("noAlarm", 0),
          ("activeWarning", 1),
          ("activeAlarm", 2),
          ("unknown", 255))
    )


_SpeedMultilinePortXCVTempHighAlarm_Type.__name__ = "Integer32"
_SpeedMultilinePortXCVTempHighAlarm_Object = MibTableColumn
speedMultilinePortXCVTempHighAlarm = _SpeedMultilinePortXCVTempHighAlarm_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 3, 6, 5, 1, 9),
    _SpeedMultilinePortXCVTempHighAlarm_Type()
)
speedMultilinePortXCVTempHighAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    speedMultilinePortXCVTempHighAlarm.setStatus("current")


class _SpeedMultilinePortXCVVCCAlarm_Type(Integer32):
    """Custom type speedMultilinePortXCVVCCAlarm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("noAlarm", 0),
          ("activeAlarm", 2),
          ("unknown", 255))
    )


_SpeedMultilinePortXCVVCCAlarm_Type.__name__ = "Integer32"
_SpeedMultilinePortXCVVCCAlarm_Object = MibTableColumn
speedMultilinePortXCVVCCAlarm = _SpeedMultilinePortXCVVCCAlarm_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 3, 6, 5, 1, 10),
    _SpeedMultilinePortXCVVCCAlarm_Type()
)
speedMultilinePortXCVVCCAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    speedMultilinePortXCVVCCAlarm.setStatus("current")


class _SpeedMultilinePortXCVDWDMAlarm_Type(Integer32):
    """Custom type speedMultilinePortXCVDWDMAlarm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("noAlarm", 0),
          ("activeAlarm", 2),
          ("unknown", 255))
    )


_SpeedMultilinePortXCVDWDMAlarm_Type.__name__ = "Integer32"
_SpeedMultilinePortXCVDWDMAlarm_Object = MibTableColumn
speedMultilinePortXCVDWDMAlarm = _SpeedMultilinePortXCVDWDMAlarm_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 3, 6, 5, 1, 11),
    _SpeedMultilinePortXCVDWDMAlarm_Type()
)
speedMultilinePortXCVDWDMAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    speedMultilinePortXCVDWDMAlarm.setStatus("current")


class _SpeedMultilinePortXCVLCalAlarm_Type(Integer32):
    """Custom type speedMultilinePortXCVLCalAlarm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("noAlarm", 0),
          ("activeAlarm", 2),
          ("unknown", 255))
    )


_SpeedMultilinePortXCVLCalAlarm_Type.__name__ = "Integer32"
_SpeedMultilinePortXCVLCalAlarm_Object = MibTableColumn
speedMultilinePortXCVLCalAlarm = _SpeedMultilinePortXCVLCalAlarm_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 3, 6, 5, 1, 12),
    _SpeedMultilinePortXCVLCalAlarm_Type()
)
speedMultilinePortXCVLCalAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    speedMultilinePortXCVLCalAlarm.setStatus("current")


class _SpeedMultilinePortXCVCDRLOLAlarm_Type(Integer32):
    """Custom type speedMultilinePortXCVCDRLOLAlarm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("noAlarm", 0),
          ("activeAlarm", 2),
          ("unknown", 255))
    )


_SpeedMultilinePortXCVCDRLOLAlarm_Type.__name__ = "Integer32"
_SpeedMultilinePortXCVCDRLOLAlarm_Object = MibTableColumn
speedMultilinePortXCVCDRLOLAlarm = _SpeedMultilinePortXCVCDRLOLAlarm_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 3, 6, 5, 1, 13),
    _SpeedMultilinePortXCVCDRLOLAlarm_Type()
)
speedMultilinePortXCVCDRLOLAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    speedMultilinePortXCVCDRLOLAlarm.setStatus("current")
_SpeedMultilinePortXCVThresholdTable_Object = MibTable
speedMultilinePortXCVThresholdTable = _SpeedMultilinePortXCVThresholdTable_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 3, 6, 6)
)
if mibBuilder.loadTexts:
    speedMultilinePortXCVThresholdTable.setStatus("current")
_SpeedMultilinePortXCVThresholdEntry_Object = MibTableRow
speedMultilinePortXCVThresholdEntry = _SpeedMultilinePortXCVThresholdEntry_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 3, 6, 6, 1)
)
speedMultilinePortXCVThresholdEntry.setIndexNames(
    (0, "SPEED-MULTILINE-MIB", "speedMultilinePortXCVThresIndex"),
)
if mibBuilder.loadTexts:
    speedMultilinePortXCVThresholdEntry.setStatus("current")


class _SpeedMultilinePortXCVThresIndex_Type(Integer32):
    """Custom type speedMultilinePortXCVThresIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1999),
    )


_SpeedMultilinePortXCVThresIndex_Type.__name__ = "Integer32"
_SpeedMultilinePortXCVThresIndex_Object = MibTableColumn
speedMultilinePortXCVThresIndex = _SpeedMultilinePortXCVThresIndex_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 3, 6, 6, 1, 1),
    _SpeedMultilinePortXCVThresIndex_Type()
)
speedMultilinePortXCVThresIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    speedMultilinePortXCVThresIndex.setStatus("current")


class _SpeedMultilinePortXCVThresSlot_Type(Integer32):
    """Custom type speedMultilinePortXCVThresSlot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 19),
    )


_SpeedMultilinePortXCVThresSlot_Type.__name__ = "Integer32"
_SpeedMultilinePortXCVThresSlot_Object = MibTableColumn
speedMultilinePortXCVThresSlot = _SpeedMultilinePortXCVThresSlot_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 3, 6, 6, 1, 2),
    _SpeedMultilinePortXCVThresSlot_Type()
)
speedMultilinePortXCVThresSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    speedMultilinePortXCVThresSlot.setStatus("current")


class _SpeedMultilinePortXCVThresPort_Type(Integer32):
    """Custom type speedMultilinePortXCVThresPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 34),
    )


_SpeedMultilinePortXCVThresPort_Type.__name__ = "Integer32"
_SpeedMultilinePortXCVThresPort_Object = MibTableColumn
speedMultilinePortXCVThresPort = _SpeedMultilinePortXCVThresPort_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 3, 6, 6, 1, 3),
    _SpeedMultilinePortXCVThresPort_Type()
)
speedMultilinePortXCVThresPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    speedMultilinePortXCVThresPort.setStatus("current")
_SpeedMultilinePortXCVRxLowAlarmLevel_Type = FixedDiv100
_SpeedMultilinePortXCVRxLowAlarmLevel_Object = MibTableColumn
speedMultilinePortXCVRxLowAlarmLevel = _SpeedMultilinePortXCVRxLowAlarmLevel_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 3, 6, 6, 1, 4),
    _SpeedMultilinePortXCVRxLowAlarmLevel_Type()
)
speedMultilinePortXCVRxLowAlarmLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    speedMultilinePortXCVRxLowAlarmLevel.setStatus("current")
_SpeedMultilinePortXCVRxHighAlarmLevel_Type = FixedDiv100
_SpeedMultilinePortXCVRxHighAlarmLevel_Object = MibTableColumn
speedMultilinePortXCVRxHighAlarmLevel = _SpeedMultilinePortXCVRxHighAlarmLevel_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 3, 6, 6, 1, 5),
    _SpeedMultilinePortXCVRxHighAlarmLevel_Type()
)
speedMultilinePortXCVRxHighAlarmLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    speedMultilinePortXCVRxHighAlarmLevel.setStatus("current")
_SpeedMultilinePortXCVRxLowWarningLevel_Type = FixedDiv100
_SpeedMultilinePortXCVRxLowWarningLevel_Object = MibTableColumn
speedMultilinePortXCVRxLowWarningLevel = _SpeedMultilinePortXCVRxLowWarningLevel_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 3, 6, 6, 1, 6),
    _SpeedMultilinePortXCVRxLowWarningLevel_Type()
)
speedMultilinePortXCVRxLowWarningLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    speedMultilinePortXCVRxLowWarningLevel.setStatus("current")
_SpeedMultilinePortXCVRxHighWarningLevel_Type = FixedDiv100
_SpeedMultilinePortXCVRxHighWarningLevel_Object = MibTableColumn
speedMultilinePortXCVRxHighWarningLevel = _SpeedMultilinePortXCVRxHighWarningLevel_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 3, 6, 6, 1, 7),
    _SpeedMultilinePortXCVRxHighWarningLevel_Type()
)
speedMultilinePortXCVRxHighWarningLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    speedMultilinePortXCVRxHighWarningLevel.setStatus("current")
_SpeedMultilinePortXCVTxLowAlarmLevel_Type = FixedDiv100
_SpeedMultilinePortXCVTxLowAlarmLevel_Object = MibTableColumn
speedMultilinePortXCVTxLowAlarmLevel = _SpeedMultilinePortXCVTxLowAlarmLevel_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 3, 6, 6, 1, 8),
    _SpeedMultilinePortXCVTxLowAlarmLevel_Type()
)
speedMultilinePortXCVTxLowAlarmLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    speedMultilinePortXCVTxLowAlarmLevel.setStatus("current")
_SpeedMultilinePortXCVTxLowWarningLevel_Type = FixedDiv100
_SpeedMultilinePortXCVTxLowWarningLevel_Object = MibTableColumn
speedMultilinePortXCVTxLowWarningLevel = _SpeedMultilinePortXCVTxLowWarningLevel_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 3, 6, 6, 1, 9),
    _SpeedMultilinePortXCVTxLowWarningLevel_Type()
)
speedMultilinePortXCVTxLowWarningLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    speedMultilinePortXCVTxLowWarningLevel.setStatus("current")
_SpeedMultilinePortXCVTxBiasLowAlarmLevel_Type = FixedDiv100
_SpeedMultilinePortXCVTxBiasLowAlarmLevel_Object = MibTableColumn
speedMultilinePortXCVTxBiasLowAlarmLevel = _SpeedMultilinePortXCVTxBiasLowAlarmLevel_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 3, 6, 6, 1, 10),
    _SpeedMultilinePortXCVTxBiasLowAlarmLevel_Type()
)
speedMultilinePortXCVTxBiasLowAlarmLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    speedMultilinePortXCVTxBiasLowAlarmLevel.setStatus("current")
_SpeedMultilinePortXCVTxBiasHighAlarmLevel_Type = FixedDiv100
_SpeedMultilinePortXCVTxBiasHighAlarmLevel_Object = MibTableColumn
speedMultilinePortXCVTxBiasHighAlarmLevel = _SpeedMultilinePortXCVTxBiasHighAlarmLevel_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 3, 6, 6, 1, 11),
    _SpeedMultilinePortXCVTxBiasHighAlarmLevel_Type()
)
speedMultilinePortXCVTxBiasHighAlarmLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    speedMultilinePortXCVTxBiasHighAlarmLevel.setStatus("current")
_SpeedMultilinePortXCVTempHighAlarmLevel_Type = Integer32
_SpeedMultilinePortXCVTempHighAlarmLevel_Object = MibTableColumn
speedMultilinePortXCVTempHighAlarmLevel = _SpeedMultilinePortXCVTempHighAlarmLevel_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 3, 6, 6, 1, 12),
    _SpeedMultilinePortXCVTempHighAlarmLevel_Type()
)
speedMultilinePortXCVTempHighAlarmLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    speedMultilinePortXCVTempHighAlarmLevel.setStatus("current")
_SpeedMultilinePortXCVTempHighWarningLevel_Type = Integer32
_SpeedMultilinePortXCVTempHighWarningLevel_Object = MibTableColumn
speedMultilinePortXCVTempHighWarningLevel = _SpeedMultilinePortXCVTempHighWarningLevel_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 3, 6, 6, 1, 13),
    _SpeedMultilinePortXCVTempHighWarningLevel_Type()
)
speedMultilinePortXCVTempHighWarningLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    speedMultilinePortXCVTempHighWarningLevel.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SPEED-MULTILINE-MIB",
    **{"speedMultiline": speedMultiline,
       "speedMultilineMOverviewTable": speedMultilineMOverviewTable,
       "speedMultilineMOverviewEntry": speedMultilineMOverviewEntry,
       "speedMultilineMOverviewIndex": speedMultilineMOverviewIndex,
       "speedMultilineMSlot": speedMultilineMSlot,
       "speedMultilineMDevice": speedMultilineMDevice,
       "speedMultilineMState": speedMultilineMState,
       "speedMultilineMSysName": speedMultilineMSysName,
       "speedMultilineMSysUpTime": speedMultilineMSysUpTime,
       "speedMultilineMTemperature": speedMultilineMTemperature,
       "speedMultilineMAlarmState": speedMultilineMAlarmState,
       "speedMultilineMAppImage": speedMultilineMAppImage,
       "speedMultilineMHwVersion": speedMultilineMHwVersion,
       "speedMultilineMDevSerialNumber": speedMultilineMDevSerialNumber,
       "speedMultilineMTemperatureAlarm": speedMultilineMTemperatureAlarm,
       "speedMultilineMBoardHWAlarm": speedMultilineMBoardHWAlarm,
       "speedMultilineMPortTxConnection": speedMultilineMPortTxConnection,
       "speedMultilineMTempWarningLevel": speedMultilineMTempWarningLevel,
       "speedMultilineMTempAlarmLevel": speedMultilineMTempAlarmLevel,
       "speedMultilineMCLIUserTimeout": speedMultilineMCLIUserTimeout,
       "speedMultilinePortConfigTable": speedMultilinePortConfigTable,
       "speedMultilinePortConfigEntry": speedMultilinePortConfigEntry,
       "speedMultilinePortIndex": speedMultilinePortIndex,
       "speedMultilinePortSlot": speedMultilinePortSlot,
       "speedMultilinePort": speedMultilinePort,
       "speedMultilinePortDescription": speedMultilinePortDescription,
       "speedMultilinePortOperState": speedMultilinePortOperState,
       "speedMultilinePortAdminConfig": speedMultilinePortAdminConfig,
       "speedMultilinePortLoopConfig": speedMultilinePortLoopConfig,
       "speedMultilinePortAlarmDeactivation": speedMultilinePortAlarmDeactivation,
       "speedMultilinePortAlarmSchedule": speedMultilinePortAlarmSchedule,
       "speedMultilinePortProtocol": speedMultilinePortProtocol,
       "speedMultilinePortLLCFconfig": speedMultilinePortLLCFconfig,
       "speedMultilinePortXCVtunableConfigSelection": speedMultilinePortXCVtunableConfigSelection,
       "speedMultilinePortXCVtunChannelConfig": speedMultilinePortXCVtunChannelConfig,
       "speedMultilinePortXCVTunWavelengthConfig": speedMultilinePortXCVTunWavelengthConfig,
       "speedMultilinePortCopperSpeed": speedMultilinePortCopperSpeed,
       "speedMultilinePortCopperMDI": speedMultilinePortCopperMDI,
       "speedMultilinePortXCVInfoTable": speedMultilinePortXCVInfoTable,
       "speedMultilinePortXCVInfoEntry": speedMultilinePortXCVInfoEntry,
       "speedMultilinePortXCVIndex": speedMultilinePortXCVIndex,
       "speedMultilinePortXCVSlot": speedMultilinePortXCVSlot,
       "speedMultilinePortXCVPort": speedMultilinePortXCVPort,
       "speedMultilinePortXCVState": speedMultilinePortXCVState,
       "speedMultilinePortXCVVendorName": speedMultilinePortXCVVendorName,
       "speedMultilinePortXCVVendorPartNumber": speedMultilinePortXCVVendorPartNumber,
       "speedMultilinePortXCVVendorSerialNumber": speedMultilinePortXCVVendorSerialNumber,
       "speedMultilinePortXCVType": speedMultilinePortXCVType,
       "speedMultilinePortXCVConnector": speedMultilinePortXCVConnector,
       "speedMultilinePortXCVWavelength": speedMultilinePortXCVWavelength,
       "speedMultilinePortXCVDMIState": speedMultilinePortXCVDMIState,
       "speedMultilinePortXCVValueTable": speedMultilinePortXCVValueTable,
       "speedMultilinePortXCVValueEntry": speedMultilinePortXCVValueEntry,
       "speedMultilinePortXCVDMIIndex": speedMultilinePortXCVDMIIndex,
       "speedMultilinePortXCVDMISlot": speedMultilinePortXCVDMISlot,
       "speedMultilinePortXCVDMIPort": speedMultilinePortXCVDMIPort,
       "speedMultilinePortXCVDMIRxLevel": speedMultilinePortXCVDMIRxLevel,
       "speedMultilinePortXCVDMITxLevel": speedMultilinePortXCVDMITxLevel,
       "speedMultilinePortXCVDMITxBias": speedMultilinePortXCVDMITxBias,
       "speedMultilinePortXCVDMITemp": speedMultilinePortXCVDMITemp,
       "speedMultilinePortXCVAlarmTable": speedMultilinePortXCVAlarmTable,
       "speedMultilinePortXCVAlarmEntry": speedMultilinePortXCVAlarmEntry,
       "speedMultilinePortAIndex": speedMultilinePortAIndex,
       "speedMultilinePortASlot": speedMultilinePortASlot,
       "speedMultilinePortAPort": speedMultilinePortAPort,
       "speedMultilinePortXCVDMIRxLowAlarm": speedMultilinePortXCVDMIRxLowAlarm,
       "speedMultilinePortXCVDMIRxHighAlarm": speedMultilinePortXCVDMIRxHighAlarm,
       "speedMultilinePortXCVDMITxLowAlarm": speedMultilinePortXCVDMITxLowAlarm,
       "speedMultilinePortXCVDMIBiasLowAlarm": speedMultilinePortXCVDMIBiasLowAlarm,
       "speedMultilinePortXCVDMIBiasHighAlarm": speedMultilinePortXCVDMIBiasHighAlarm,
       "speedMultilinePortXCVTempHighAlarm": speedMultilinePortXCVTempHighAlarm,
       "speedMultilinePortXCVVCCAlarm": speedMultilinePortXCVVCCAlarm,
       "speedMultilinePortXCVDWDMAlarm": speedMultilinePortXCVDWDMAlarm,
       "speedMultilinePortXCVLCalAlarm": speedMultilinePortXCVLCalAlarm,
       "speedMultilinePortXCVCDRLOLAlarm": speedMultilinePortXCVCDRLOLAlarm,
       "speedMultilinePortXCVThresholdTable": speedMultilinePortXCVThresholdTable,
       "speedMultilinePortXCVThresholdEntry": speedMultilinePortXCVThresholdEntry,
       "speedMultilinePortXCVThresIndex": speedMultilinePortXCVThresIndex,
       "speedMultilinePortXCVThresSlot": speedMultilinePortXCVThresSlot,
       "speedMultilinePortXCVThresPort": speedMultilinePortXCVThresPort,
       "speedMultilinePortXCVRxLowAlarmLevel": speedMultilinePortXCVRxLowAlarmLevel,
       "speedMultilinePortXCVRxHighAlarmLevel": speedMultilinePortXCVRxHighAlarmLevel,
       "speedMultilinePortXCVRxLowWarningLevel": speedMultilinePortXCVRxLowWarningLevel,
       "speedMultilinePortXCVRxHighWarningLevel": speedMultilinePortXCVRxHighWarningLevel,
       "speedMultilinePortXCVTxLowAlarmLevel": speedMultilinePortXCVTxLowAlarmLevel,
       "speedMultilinePortXCVTxLowWarningLevel": speedMultilinePortXCVTxLowWarningLevel,
       "speedMultilinePortXCVTxBiasLowAlarmLevel": speedMultilinePortXCVTxBiasLowAlarmLevel,
       "speedMultilinePortXCVTxBiasHighAlarmLevel": speedMultilinePortXCVTxBiasHighAlarmLevel,
       "speedMultilinePortXCVTempHighAlarmLevel": speedMultilinePortXCVTempHighAlarmLevel,
       "speedMultilinePortXCVTempHighWarningLevel": speedMultilinePortXCVTempHighWarningLevel}
)
