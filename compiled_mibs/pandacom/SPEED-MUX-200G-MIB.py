# SNMP MIB module (SPEED-MUX-200G-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\pandacom\SPEED-MUX-200G-MIB

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

(multiplexer,) = mibBuilder.importSymbols(
    "SPEEDCARRIER-MIB",
    "multiplexer")


# MODULE-IDENTITY

speedMux200g = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 3652, 3, 4, 1)
)
if mibBuilder.loadTexts:
    speedMux200g.setRevisions(
        ("2020-10-07 00:00",
         "2020-04-07 00:00",
         "2019-06-24 00:00",
         "2019-04-25 00:00",
         "2019-04-10 00:00",
         "2019-01-17 00:00",
         "2018-06-06 00:00",
         "2018-02-14 00:00",
         "2017-07-28 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_SpeedMux200gMOverviewTable_Object = MibTable
speedMux200gMOverviewTable = _SpeedMux200gMOverviewTable_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 4, 1, 1)
)
if mibBuilder.loadTexts:
    speedMux200gMOverviewTable.setStatus("current")
_SpeedMux200gMOverviewEntry_Object = MibTableRow
speedMux200gMOverviewEntry = _SpeedMux200gMOverviewEntry_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 4, 1, 1, 1)
)
speedMux200gMOverviewEntry.setIndexNames(
    (0, "SPEED-MUX-200G-MIB", "speedMux200gMOverviewIndex"),
)
if mibBuilder.loadTexts:
    speedMux200gMOverviewEntry.setStatus("current")


class _SpeedMux200gMOverviewIndex_Type(Integer32):
    """Custom type speedMux200gMOverviewIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_SpeedMux200gMOverviewIndex_Type.__name__ = "Integer32"
_SpeedMux200gMOverviewIndex_Object = MibTableColumn
speedMux200gMOverviewIndex = _SpeedMux200gMOverviewIndex_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 4, 1, 1, 1, 1),
    _SpeedMux200gMOverviewIndex_Type()
)
speedMux200gMOverviewIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    speedMux200gMOverviewIndex.setStatus("current")


class _SpeedMux200gMSlot_Type(Integer32):
    """Custom type speedMux200gMSlot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 19),
    )


_SpeedMux200gMSlot_Type.__name__ = "Integer32"
_SpeedMux200gMSlot_Object = MibTableColumn
speedMux200gMSlot = _SpeedMux200gMSlot_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 4, 1, 1, 1, 2),
    _SpeedMux200gMSlot_Type()
)
speedMux200gMSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    speedMux200gMSlot.setStatus("current")


class _SpeedMux200gMDevice_Type(Integer32):
    """Custom type speedMux200gMDevice based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              16,
              17,
              19,
              20,
              255)
        )
    )
    namedValues = NamedValues(
        *(("notAvailable", 0),
          ("speedMuxSX200e6QSFP2cfp", 16),
          ("speedMuxSX200s6QSFP2cfp", 17),
          ("speedMuxSX200e5QSFPcfp2", 19),
          ("speedMuxSX200s5QSFPcfp2", 20),
          ("unknown", 255))
    )


_SpeedMux200gMDevice_Type.__name__ = "Integer32"
_SpeedMux200gMDevice_Object = MibTableColumn
speedMux200gMDevice = _SpeedMux200gMDevice_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 4, 1, 1, 1, 3),
    _SpeedMux200gMDevice_Type()
)
speedMux200gMDevice.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    speedMux200gMDevice.setStatus("current")


class _SpeedMux200gMState_Type(Integer32):
    """Custom type speedMux200gMState based on Integer32"""
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


_SpeedMux200gMState_Type.__name__ = "Integer32"
_SpeedMux200gMState_Object = MibTableColumn
speedMux200gMState = _SpeedMux200gMState_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 4, 1, 1, 1, 4),
    _SpeedMux200gMState_Type()
)
speedMux200gMState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    speedMux200gMState.setStatus("current")


class _SpeedMux200gMSysName_Type(DisplayString):
    """Custom type speedMux200gMSysName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_SpeedMux200gMSysName_Type.__name__ = "DisplayString"
_SpeedMux200gMSysName_Object = MibTableColumn
speedMux200gMSysName = _SpeedMux200gMSysName_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 4, 1, 1, 1, 5),
    _SpeedMux200gMSysName_Type()
)
speedMux200gMSysName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    speedMux200gMSysName.setStatus("current")
_SpeedMux200gMSysUpTime_Type = TimeTicks
_SpeedMux200gMSysUpTime_Object = MibTableColumn
speedMux200gMSysUpTime = _SpeedMux200gMSysUpTime_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 4, 1, 1, 1, 6),
    _SpeedMux200gMSysUpTime_Type()
)
speedMux200gMSysUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    speedMux200gMSysUpTime.setStatus("current")
_SpeedMux200gMTemperature_Type = Integer32
_SpeedMux200gMTemperature_Object = MibTableColumn
speedMux200gMTemperature = _SpeedMux200gMTemperature_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 4, 1, 1, 1, 7),
    _SpeedMux200gMTemperature_Type()
)
speedMux200gMTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    speedMux200gMTemperature.setStatus("current")


class _SpeedMux200gMAlarmState_Type(Integer32):
    """Custom type speedMux200gMAlarmState based on Integer32"""
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


_SpeedMux200gMAlarmState_Type.__name__ = "Integer32"
_SpeedMux200gMAlarmState_Object = MibTableColumn
speedMux200gMAlarmState = _SpeedMux200gMAlarmState_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 4, 1, 1, 1, 8),
    _SpeedMux200gMAlarmState_Type()
)
speedMux200gMAlarmState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    speedMux200gMAlarmState.setStatus("current")


class _SpeedMux200gMKernelImage_Type(DisplayString):
    """Custom type speedMux200gMKernelImage based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_SpeedMux200gMKernelImage_Type.__name__ = "DisplayString"
_SpeedMux200gMKernelImage_Object = MibTableColumn
speedMux200gMKernelImage = _SpeedMux200gMKernelImage_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 4, 1, 1, 1, 9),
    _SpeedMux200gMKernelImage_Type()
)
speedMux200gMKernelImage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    speedMux200gMKernelImage.setStatus("current")


class _SpeedMux200gMAppImage_Type(DisplayString):
    """Custom type speedMux200gMAppImage based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_SpeedMux200gMAppImage_Type.__name__ = "DisplayString"
_SpeedMux200gMAppImage_Object = MibTableColumn
speedMux200gMAppImage = _SpeedMux200gMAppImage_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 4, 1, 1, 1, 10),
    _SpeedMux200gMAppImage_Type()
)
speedMux200gMAppImage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    speedMux200gMAppImage.setStatus("current")


class _SpeedMux200gMHwVersion_Type(DisplayString):
    """Custom type speedMux200gMHwVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_SpeedMux200gMHwVersion_Type.__name__ = "DisplayString"
_SpeedMux200gMHwVersion_Object = MibTableColumn
speedMux200gMHwVersion = _SpeedMux200gMHwVersion_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 4, 1, 1, 1, 11),
    _SpeedMux200gMHwVersion_Type()
)
speedMux200gMHwVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    speedMux200gMHwVersion.setStatus("current")


class _SpeedMux200gMDevSerialNumber_Type(DisplayString):
    """Custom type speedMux200gMDevSerialNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 17),
    )


_SpeedMux200gMDevSerialNumber_Type.__name__ = "DisplayString"
_SpeedMux200gMDevSerialNumber_Object = MibTableColumn
speedMux200gMDevSerialNumber = _SpeedMux200gMDevSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 4, 1, 1, 1, 12),
    _SpeedMux200gMDevSerialNumber_Type()
)
speedMux200gMDevSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    speedMux200gMDevSerialNumber.setStatus("current")


class _SpeedMux200gMTemperatureAlarm_Type(Integer32):
    """Custom type speedMux200gMTemperatureAlarm based on Integer32"""
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


_SpeedMux200gMTemperatureAlarm_Type.__name__ = "Integer32"
_SpeedMux200gMTemperatureAlarm_Object = MibTableColumn
speedMux200gMTemperatureAlarm = _SpeedMux200gMTemperatureAlarm_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 4, 1, 1, 1, 13),
    _SpeedMux200gMTemperatureAlarm_Type()
)
speedMux200gMTemperatureAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    speedMux200gMTemperatureAlarm.setStatus("current")


class _SpeedMux200gMOTNAlarm_Type(Integer32):
    """Custom type speedMux200gMOTNAlarm based on Integer32"""
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


_SpeedMux200gMOTNAlarm_Type.__name__ = "Integer32"
_SpeedMux200gMOTNAlarm_Object = MibTableColumn
speedMux200gMOTNAlarm = _SpeedMux200gMOTNAlarm_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 4, 1, 1, 1, 14),
    _SpeedMux200gMOTNAlarm_Type()
)
speedMux200gMOTNAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    speedMux200gMOTNAlarm.setStatus("current")


class _SpeedMux200gMBoardHWAlarm_Type(Integer32):
    """Custom type speedMux200gMBoardHWAlarm based on Integer32"""
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


_SpeedMux200gMBoardHWAlarm_Type.__name__ = "Integer32"
_SpeedMux200gMBoardHWAlarm_Object = MibTableColumn
speedMux200gMBoardHWAlarm = _SpeedMux200gMBoardHWAlarm_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 4, 1, 1, 1, 15),
    _SpeedMux200gMBoardHWAlarm_Type()
)
speedMux200gMBoardHWAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    speedMux200gMBoardHWAlarm.setStatus("current")
_SpeedMux200gMConfigTable_Object = MibTable
speedMux200gMConfigTable = _SpeedMux200gMConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 4, 1, 2)
)
if mibBuilder.loadTexts:
    speedMux200gMConfigTable.setStatus("current")
_SpeedMux200gMConfigEntry_Object = MibTableRow
speedMux200gMConfigEntry = _SpeedMux200gMConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 4, 1, 2, 1)
)
speedMux200gMConfigEntry.setIndexNames(
    (0, "SPEED-MUX-200G-MIB", "speedMux200gMConfigIndex"),
)
if mibBuilder.loadTexts:
    speedMux200gMConfigEntry.setStatus("current")


class _SpeedMux200gMConfigIndex_Type(Integer32):
    """Custom type speedMux200gMConfigIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_SpeedMux200gMConfigIndex_Type.__name__ = "Integer32"
_SpeedMux200gMConfigIndex_Object = MibTableColumn
speedMux200gMConfigIndex = _SpeedMux200gMConfigIndex_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 4, 1, 2, 1, 1),
    _SpeedMux200gMConfigIndex_Type()
)
speedMux200gMConfigIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    speedMux200gMConfigIndex.setStatus("current")


class _SpeedMux200gMNetIpAddress_Type(IpAddress):
    """Custom type speedMux200gMNetIpAddress based on IpAddress"""
    defaultHexValue = "c0a80068"


_SpeedMux200gMNetIpAddress_Type.__name__ = "IpAddress"
_SpeedMux200gMNetIpAddress_Object = MibTableColumn
speedMux200gMNetIpAddress = _SpeedMux200gMNetIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 4, 1, 2, 1, 2),
    _SpeedMux200gMNetIpAddress_Type()
)
speedMux200gMNetIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    speedMux200gMNetIpAddress.setStatus("current")


class _SpeedMux200gMNetNetmask_Type(IpAddress):
    """Custom type speedMux200gMNetNetmask based on IpAddress"""
    defaultHexValue = "ffffff00"


_SpeedMux200gMNetNetmask_Type.__name__ = "IpAddress"
_SpeedMux200gMNetNetmask_Object = MibTableColumn
speedMux200gMNetNetmask = _SpeedMux200gMNetNetmask_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 4, 1, 2, 1, 3),
    _SpeedMux200gMNetNetmask_Type()
)
speedMux200gMNetNetmask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    speedMux200gMNetNetmask.setStatus("current")
_SpeedMux200gMNetGateway_Type = IpAddress
_SpeedMux200gMNetGateway_Object = MibTableColumn
speedMux200gMNetGateway = _SpeedMux200gMNetGateway_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 4, 1, 2, 1, 4),
    _SpeedMux200gMNetGateway_Type()
)
speedMux200gMNetGateway.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    speedMux200gMNetGateway.setStatus("current")
_SpeedMux200gMSNMPTrapsink1_Type = IpAddress
_SpeedMux200gMSNMPTrapsink1_Object = MibTableColumn
speedMux200gMSNMPTrapsink1 = _SpeedMux200gMSNMPTrapsink1_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 4, 1, 2, 1, 5),
    _SpeedMux200gMSNMPTrapsink1_Type()
)
speedMux200gMSNMPTrapsink1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    speedMux200gMSNMPTrapsink1.setStatus("current")
_SpeedMux200gMSNMPTrapsink2_Type = IpAddress
_SpeedMux200gMSNMPTrapsink2_Object = MibTableColumn
speedMux200gMSNMPTrapsink2 = _SpeedMux200gMSNMPTrapsink2_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 4, 1, 2, 1, 6),
    _SpeedMux200gMSNMPTrapsink2_Type()
)
speedMux200gMSNMPTrapsink2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    speedMux200gMSNMPTrapsink2.setStatus("current")
_SpeedMux200gMSNMPTrapsink3_Type = IpAddress
_SpeedMux200gMSNMPTrapsink3_Object = MibTableColumn
speedMux200gMSNMPTrapsink3 = _SpeedMux200gMSNMPTrapsink3_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 4, 1, 2, 1, 7),
    _SpeedMux200gMSNMPTrapsink3_Type()
)
speedMux200gMSNMPTrapsink3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    speedMux200gMSNMPTrapsink3.setStatus("current")
_SpeedMux200gMSNMPTrapsink4_Type = IpAddress
_SpeedMux200gMSNMPTrapsink4_Object = MibTableColumn
speedMux200gMSNMPTrapsink4 = _SpeedMux200gMSNMPTrapsink4_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 4, 1, 2, 1, 8),
    _SpeedMux200gMSNMPTrapsink4_Type()
)
speedMux200gMSNMPTrapsink4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    speedMux200gMSNMPTrapsink4.setStatus("current")
_SpeedMux200gMSNMPTrapsink5_Type = IpAddress
_SpeedMux200gMSNMPTrapsink5_Object = MibTableColumn
speedMux200gMSNMPTrapsink5 = _SpeedMux200gMSNMPTrapsink5_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 4, 1, 2, 1, 9),
    _SpeedMux200gMSNMPTrapsink5_Type()
)
speedMux200gMSNMPTrapsink5.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    speedMux200gMSNMPTrapsink5.setStatus("current")


class _SpeedMux200gMSNMPReadCommunity_Type(DisplayString):
    """Custom type speedMux200gMSNMPReadCommunity based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_SpeedMux200gMSNMPReadCommunity_Type.__name__ = "DisplayString"
_SpeedMux200gMSNMPReadCommunity_Object = MibTableColumn
speedMux200gMSNMPReadCommunity = _SpeedMux200gMSNMPReadCommunity_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 4, 1, 2, 1, 10),
    _SpeedMux200gMSNMPReadCommunity_Type()
)
speedMux200gMSNMPReadCommunity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    speedMux200gMSNMPReadCommunity.setStatus("current")


class _SpeedMux200gMTempWarningLevel_Type(Integer32):
    """Custom type speedMux200gMTempWarningLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 60),
    )


_SpeedMux200gMTempWarningLevel_Type.__name__ = "Integer32"
_SpeedMux200gMTempWarningLevel_Object = MibTableColumn
speedMux200gMTempWarningLevel = _SpeedMux200gMTempWarningLevel_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 4, 1, 2, 1, 11),
    _SpeedMux200gMTempWarningLevel_Type()
)
speedMux200gMTempWarningLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    speedMux200gMTempWarningLevel.setStatus("current")
_SpeedMux200gMTempAlarmLevel_Type = Integer32
_SpeedMux200gMTempAlarmLevel_Object = MibTableColumn
speedMux200gMTempAlarmLevel = _SpeedMux200gMTempAlarmLevel_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 4, 1, 2, 1, 12),
    _SpeedMux200gMTempAlarmLevel_Type()
)
speedMux200gMTempAlarmLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    speedMux200gMTempAlarmLevel.setStatus("current")


class _SpeedMux200gMSNMPSysContact_Type(DisplayString):
    """Custom type speedMux200gMSNMPSysContact based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_SpeedMux200gMSNMPSysContact_Type.__name__ = "DisplayString"
_SpeedMux200gMSNMPSysContact_Object = MibTableColumn
speedMux200gMSNMPSysContact = _SpeedMux200gMSNMPSysContact_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 4, 1, 2, 1, 13),
    _SpeedMux200gMSNMPSysContact_Type()
)
speedMux200gMSNMPSysContact.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    speedMux200gMSNMPSysContact.setStatus("current")


class _SpeedMux200gMSNMPSysLocation_Type(DisplayString):
    """Custom type speedMux200gMSNMPSysLocation based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_SpeedMux200gMSNMPSysLocation_Type.__name__ = "DisplayString"
_SpeedMux200gMSNMPSysLocation_Object = MibTableColumn
speedMux200gMSNMPSysLocation = _SpeedMux200gMSNMPSysLocation_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 4, 1, 2, 1, 14),
    _SpeedMux200gMSNMPSysLocation_Type()
)
speedMux200gMSNMPSysLocation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    speedMux200gMSNMPSysLocation.setStatus("current")


class _SpeedMux200gMCLIUserTimeout_Type(Integer32):
    """Custom type speedMux200gMCLIUserTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(120, 3600),
    )


_SpeedMux200gMCLIUserTimeout_Type.__name__ = "Integer32"
_SpeedMux200gMCLIUserTimeout_Object = MibTableColumn
speedMux200gMCLIUserTimeout = _SpeedMux200gMCLIUserTimeout_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 4, 1, 2, 1, 15),
    _SpeedMux200gMCLIUserTimeout_Type()
)
speedMux200gMCLIUserTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    speedMux200gMCLIUserTimeout.setStatus("current")


class _SpeedMux200gMNetAccess_Type(Integer32):
    """Custom type speedMux200gMNetAccess based on Integer32"""
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
        *(("notavailable", 0),
          ("off", 1),
          ("telnet", 2),
          ("ssh", 3),
          ("notPossible", 255))
    )


_SpeedMux200gMNetAccess_Type.__name__ = "Integer32"
_SpeedMux200gMNetAccess_Object = MibTableColumn
speedMux200gMNetAccess = _SpeedMux200gMNetAccess_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 4, 1, 2, 1, 16),
    _SpeedMux200gMNetAccess_Type()
)
speedMux200gMNetAccess.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    speedMux200gMNetAccess.setStatus("current")


class _SpeedMux200gMApplicationConfig_Type(Integer32):
    """Custom type speedMux200gMApplicationConfig based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 6),
    )


_SpeedMux200gMApplicationConfig_Type.__name__ = "Integer32"
_SpeedMux200gMApplicationConfig_Object = MibTableColumn
speedMux200gMApplicationConfig = _SpeedMux200gMApplicationConfig_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 4, 1, 2, 1, 17),
    _SpeedMux200gMApplicationConfig_Type()
)
speedMux200gMApplicationConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    speedMux200gMApplicationConfig.setStatus("current")
_SpeedMux200gEthPortTable_Object = MibTable
speedMux200gEthPortTable = _SpeedMux200gEthPortTable_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 4, 1, 3)
)
if mibBuilder.loadTexts:
    speedMux200gEthPortTable.setStatus("current")
_SpeedMux200gEthPortEntry_Object = MibTableRow
speedMux200gEthPortEntry = _SpeedMux200gEthPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 4, 1, 3, 1)
)
speedMux200gEthPortEntry.setIndexNames(
    (0, "SPEED-MUX-200G-MIB", "speedMux200gEthPortIndex"),
)
if mibBuilder.loadTexts:
    speedMux200gEthPortEntry.setStatus("current")


class _SpeedMux200gEthPortIndex_Type(Integer32):
    """Custom type speedMux200gEthPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1900),
    )


_SpeedMux200gEthPortIndex_Type.__name__ = "Integer32"
_SpeedMux200gEthPortIndex_Object = MibTableColumn
speedMux200gEthPortIndex = _SpeedMux200gEthPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 4, 1, 3, 1, 1),
    _SpeedMux200gEthPortIndex_Type()
)
speedMux200gEthPortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    speedMux200gEthPortIndex.setStatus("current")
_SpeedMux200gEthSlot_Type = Integer32
_SpeedMux200gEthSlot_Object = MibTableColumn
speedMux200gEthSlot = _SpeedMux200gEthSlot_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 4, 1, 3, 1, 2),
    _SpeedMux200gEthSlot_Type()
)
speedMux200gEthSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    speedMux200gEthSlot.setStatus("current")
_SpeedMux200gEthPort_Type = Integer32
_SpeedMux200gEthPort_Object = MibTableColumn
speedMux200gEthPort = _SpeedMux200gEthPort_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 4, 1, 3, 1, 3),
    _SpeedMux200gEthPort_Type()
)
speedMux200gEthPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    speedMux200gEthPort.setStatus("current")


class _SpeedMux200gEthPortDescription_Type(DisplayString):
    """Custom type speedMux200gEthPortDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_SpeedMux200gEthPortDescription_Type.__name__ = "DisplayString"
_SpeedMux200gEthPortDescription_Object = MibTableColumn
speedMux200gEthPortDescription = _SpeedMux200gEthPortDescription_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 4, 1, 3, 1, 4),
    _SpeedMux200gEthPortDescription_Type()
)
speedMux200gEthPortDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    speedMux200gEthPortDescription.setStatus("current")


class _SpeedMux200gEthPortMode_Type(Integer32):
    """Custom type speedMux200gEthPortMode based on Integer32"""
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
          ("fdx1000", 6),
          ("off", 7),
          ("unknown", 255))
    )


_SpeedMux200gEthPortMode_Type.__name__ = "Integer32"
_SpeedMux200gEthPortMode_Object = MibTableColumn
speedMux200gEthPortMode = _SpeedMux200gEthPortMode_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 4, 1, 3, 1, 5),
    _SpeedMux200gEthPortMode_Type()
)
speedMux200gEthPortMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    speedMux200gEthPortMode.setStatus("current")


class _SpeedMux200gEthPortOperState_Type(Integer32):
    """Custom type speedMux200gEthPortOperState based on Integer32"""
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
        *(("notavailable", 0),
          ("linkDown", 1),
          ("hdx10", 2),
          ("fdx10", 3),
          ("hdx100", 4),
          ("fdx100", 5),
          ("fdx1000", 6),
          ("off", 7),
          ("unknown", 255))
    )


_SpeedMux200gEthPortOperState_Type.__name__ = "Integer32"
_SpeedMux200gEthPortOperState_Object = MibTableColumn
speedMux200gEthPortOperState = _SpeedMux200gEthPortOperState_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 4, 1, 3, 1, 6),
    _SpeedMux200gEthPortOperState_Type()
)
speedMux200gEthPortOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    speedMux200gEthPortOperState.setStatus("current")
_SpeedMux200gClientPortLaneTable_Object = MibTable
speedMux200gClientPortLaneTable = _SpeedMux200gClientPortLaneTable_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 4, 1, 4)
)
if mibBuilder.loadTexts:
    speedMux200gClientPortLaneTable.setStatus("current")
_SpeedMux200gClientPortLaneEntry_Object = MibTableRow
speedMux200gClientPortLaneEntry = _SpeedMux200gClientPortLaneEntry_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 4, 1, 4, 1)
)
speedMux200gClientPortLaneEntry.setIndexNames(
    (0, "SPEED-MUX-200G-MIB", "speedMux200gClientPortLaneIndex"),
)
if mibBuilder.loadTexts:
    speedMux200gClientPortLaneEntry.setStatus("current")


class _SpeedMux200gClientPortLaneIndex_Type(Integer32):
    """Custom type speedMux200gClientPortLaneIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1900),
    )


_SpeedMux200gClientPortLaneIndex_Type.__name__ = "Integer32"
_SpeedMux200gClientPortLaneIndex_Object = MibTableColumn
speedMux200gClientPortLaneIndex = _SpeedMux200gClientPortLaneIndex_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 4, 1, 4, 1, 1),
    _SpeedMux200gClientPortLaneIndex_Type()
)
speedMux200gClientPortLaneIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    speedMux200gClientPortLaneIndex.setStatus("current")
_SpeedMux200gClientSlot_Type = Integer32
_SpeedMux200gClientSlot_Object = MibTableColumn
speedMux200gClientSlot = _SpeedMux200gClientSlot_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 4, 1, 4, 1, 2),
    _SpeedMux200gClientSlot_Type()
)
speedMux200gClientSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    speedMux200gClientSlot.setStatus("current")
_SpeedMux200gClientPortLane_Type = Integer32
_SpeedMux200gClientPortLane_Object = MibTableColumn
speedMux200gClientPortLane = _SpeedMux200gClientPortLane_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 4, 1, 4, 1, 3),
    _SpeedMux200gClientPortLane_Type()
)
speedMux200gClientPortLane.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    speedMux200gClientPortLane.setStatus("current")


class _SpeedMux200gClientPortLaneDescription_Type(DisplayString):
    """Custom type speedMux200gClientPortLaneDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_SpeedMux200gClientPortLaneDescription_Type.__name__ = "DisplayString"
_SpeedMux200gClientPortLaneDescription_Object = MibTableColumn
speedMux200gClientPortLaneDescription = _SpeedMux200gClientPortLaneDescription_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 4, 1, 4, 1, 4),
    _SpeedMux200gClientPortLaneDescription_Type()
)
speedMux200gClientPortLaneDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    speedMux200gClientPortLaneDescription.setStatus("current")


class _SpeedMux200gClientPortLaneAdminConfig_Type(Integer32):
    """Custom type speedMux200gClientPortLaneAdminConfig based on Integer32"""
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


_SpeedMux200gClientPortLaneAdminConfig_Type.__name__ = "Integer32"
_SpeedMux200gClientPortLaneAdminConfig_Object = MibTableColumn
speedMux200gClientPortLaneAdminConfig = _SpeedMux200gClientPortLaneAdminConfig_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 4, 1, 4, 1, 5),
    _SpeedMux200gClientPortLaneAdminConfig_Type()
)
speedMux200gClientPortLaneAdminConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    speedMux200gClientPortLaneAdminConfig.setStatus("current")


class _SpeedMux200gClientPortLaneOperState_Type(Integer32):
    """Custom type speedMux200gClientPortLaneOperState based on Integer32"""
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


_SpeedMux200gClientPortLaneOperState_Type.__name__ = "Integer32"
_SpeedMux200gClientPortLaneOperState_Object = MibTableColumn
speedMux200gClientPortLaneOperState = _SpeedMux200gClientPortLaneOperState_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 4, 1, 4, 1, 6),
    _SpeedMux200gClientPortLaneOperState_Type()
)
speedMux200gClientPortLaneOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    speedMux200gClientPortLaneOperState.setStatus("current")


class _SpeedMux200gClientPortLaneLoopConfig_Type(Integer32):
    """Custom type speedMux200gClientPortLaneLoopConfig based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("notAvailable", 0),
          ("off", 1),
          ("internal", 3),
          ("external", 4))
    )


_SpeedMux200gClientPortLaneLoopConfig_Type.__name__ = "Integer32"
_SpeedMux200gClientPortLaneLoopConfig_Object = MibTableColumn
speedMux200gClientPortLaneLoopConfig = _SpeedMux200gClientPortLaneLoopConfig_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 4, 1, 4, 1, 7),
    _SpeedMux200gClientPortLaneLoopConfig_Type()
)
speedMux200gClientPortLaneLoopConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    speedMux200gClientPortLaneLoopConfig.setStatus("current")


class _SpeedMux200gClientPortLaneAlarmDeactivation_Type(Integer32):
    """Custom type speedMux200gClientPortLaneAlarmDeactivation based on Integer32"""
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


_SpeedMux200gClientPortLaneAlarmDeactivation_Type.__name__ = "Integer32"
_SpeedMux200gClientPortLaneAlarmDeactivation_Object = MibTableColumn
speedMux200gClientPortLaneAlarmDeactivation = _SpeedMux200gClientPortLaneAlarmDeactivation_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 4, 1, 4, 1, 8),
    _SpeedMux200gClientPortLaneAlarmDeactivation_Type()
)
speedMux200gClientPortLaneAlarmDeactivation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    speedMux200gClientPortLaneAlarmDeactivation.setStatus("current")


class _SpeedMux200gClientPortLaneAlarmSchedule_Type(Integer32):
    """Custom type speedMux200gClientPortLaneAlarmSchedule based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1200),
    )


_SpeedMux200gClientPortLaneAlarmSchedule_Type.__name__ = "Integer32"
_SpeedMux200gClientPortLaneAlarmSchedule_Object = MibTableColumn
speedMux200gClientPortLaneAlarmSchedule = _SpeedMux200gClientPortLaneAlarmSchedule_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 4, 1, 4, 1, 9),
    _SpeedMux200gClientPortLaneAlarmSchedule_Type()
)
speedMux200gClientPortLaneAlarmSchedule.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    speedMux200gClientPortLaneAlarmSchedule.setStatus("current")


class _SpeedMux200gClientPortLaneProtocol_Type(Integer32):
    """Custom type speedMux200gClientPortLaneProtocol based on Integer32"""
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
              29)
        )
    )
    namedValues = NamedValues(
        *(("notavailable", 0),
          ("bundled", 1),
          ("eth40G", 2),
          ("fc32G", 3),
          ("fc16G", 4),
          ("fc8G", 5),
          ("fc10G", 6),
          ("eth10G", 7),
          ("cpri7", 8),
          ("cpri6", 9),
          ("cpri5", 10),
          ("ibqdr", 11),
          ("ibddr", 12),
          ("otu2", 13),
          ("otu3", 14),
          ("otu4", 15),
          ("eth100G", 16),
          ("eth100GMAC", 17),
          ("eth1G", 18),
          ("eth25G", 19),
          ("fc4G", 20),
          ("eth40Gsplit", 29))
    )


_SpeedMux200gClientPortLaneProtocol_Type.__name__ = "Integer32"
_SpeedMux200gClientPortLaneProtocol_Object = MibTableColumn
speedMux200gClientPortLaneProtocol = _SpeedMux200gClientPortLaneProtocol_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 4, 1, 4, 1, 10),
    _SpeedMux200gClientPortLaneProtocol_Type()
)
speedMux200gClientPortLaneProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    speedMux200gClientPortLaneProtocol.setStatus("current")


class _SpeedMux200gClientPortLaneConnectionToLinePort_Type(Integer32):
    """Custom type speedMux200gClientPortLaneConnectionToLinePort based on Integer32"""
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
        *(("notavailable", 0),
          ("line1", 1),
          ("line2", 2),
          ("none", 255))
    )


_SpeedMux200gClientPortLaneConnectionToLinePort_Type.__name__ = "Integer32"
_SpeedMux200gClientPortLaneConnectionToLinePort_Object = MibTableColumn
speedMux200gClientPortLaneConnectionToLinePort = _SpeedMux200gClientPortLaneConnectionToLinePort_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 4, 1, 4, 1, 11),
    _SpeedMux200gClientPortLaneConnectionToLinePort_Type()
)
speedMux200gClientPortLaneConnectionToLinePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    speedMux200gClientPortLaneConnectionToLinePort.setStatus("current")


class _SpeedMux200gClientPortLaneLLCFconfig_Type(Integer32):
    """Custom type speedMux200gClientPortLaneLLCFconfig based on Integer32"""
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


_SpeedMux200gClientPortLaneLLCFconfig_Type.__name__ = "Integer32"
_SpeedMux200gClientPortLaneLLCFconfig_Object = MibTableColumn
speedMux200gClientPortLaneLLCFconfig = _SpeedMux200gClientPortLaneLLCFconfig_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 4, 1, 4, 1, 12),
    _SpeedMux200gClientPortLaneLLCFconfig_Type()
)
speedMux200gClientPortLaneLLCFconfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    speedMux200gClientPortLaneLLCFconfig.setStatus("current")
_SpeedMux200gLinePortTable_Object = MibTable
speedMux200gLinePortTable = _SpeedMux200gLinePortTable_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 4, 1, 5)
)
if mibBuilder.loadTexts:
    speedMux200gLinePortTable.setStatus("current")
_SpeedMux200gLinePortEntry_Object = MibTableRow
speedMux200gLinePortEntry = _SpeedMux200gLinePortEntry_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 4, 1, 5, 1)
)
speedMux200gLinePortEntry.setIndexNames(
    (0, "SPEED-MUX-200G-MIB", "speedMux200gLinePortIndex"),
)
if mibBuilder.loadTexts:
    speedMux200gLinePortEntry.setStatus("current")


class _SpeedMux200gLinePortIndex_Type(Integer32):
    """Custom type speedMux200gLinePortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_SpeedMux200gLinePortIndex_Type.__name__ = "Integer32"
_SpeedMux200gLinePortIndex_Object = MibTableColumn
speedMux200gLinePortIndex = _SpeedMux200gLinePortIndex_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 4, 1, 5, 1, 1),
    _SpeedMux200gLinePortIndex_Type()
)
speedMux200gLinePortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    speedMux200gLinePortIndex.setStatus("current")
_SpeedMux200gLineSlot_Type = Integer32
_SpeedMux200gLineSlot_Object = MibTableColumn
speedMux200gLineSlot = _SpeedMux200gLineSlot_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 4, 1, 5, 1, 2),
    _SpeedMux200gLineSlot_Type()
)
speedMux200gLineSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    speedMux200gLineSlot.setStatus("current")
_SpeedMux200gLinePort_Type = Integer32
_SpeedMux200gLinePort_Object = MibTableColumn
speedMux200gLinePort = _SpeedMux200gLinePort_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 4, 1, 5, 1, 3),
    _SpeedMux200gLinePort_Type()
)
speedMux200gLinePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    speedMux200gLinePort.setStatus("current")


class _SpeedMux200gLinePortDescription_Type(DisplayString):
    """Custom type speedMux200gLinePortDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_SpeedMux200gLinePortDescription_Type.__name__ = "DisplayString"
_SpeedMux200gLinePortDescription_Object = MibTableColumn
speedMux200gLinePortDescription = _SpeedMux200gLinePortDescription_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 4, 1, 5, 1, 4),
    _SpeedMux200gLinePortDescription_Type()
)
speedMux200gLinePortDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    speedMux200gLinePortDescription.setStatus("current")


class _SpeedMux200gLinePortAdminConfig_Type(Integer32):
    """Custom type speedMux200gLinePortAdminConfig based on Integer32"""
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


_SpeedMux200gLinePortAdminConfig_Type.__name__ = "Integer32"
_SpeedMux200gLinePortAdminConfig_Object = MibTableColumn
speedMux200gLinePortAdminConfig = _SpeedMux200gLinePortAdminConfig_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 4, 1, 5, 1, 5),
    _SpeedMux200gLinePortAdminConfig_Type()
)
speedMux200gLinePortAdminConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    speedMux200gLinePortAdminConfig.setStatus("current")


class _SpeedMux200gLinePortOperState_Type(Integer32):
    """Custom type speedMux200gLinePortOperState based on Integer32"""
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


_SpeedMux200gLinePortOperState_Type.__name__ = "Integer32"
_SpeedMux200gLinePortOperState_Object = MibTableColumn
speedMux200gLinePortOperState = _SpeedMux200gLinePortOperState_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 4, 1, 5, 1, 6),
    _SpeedMux200gLinePortOperState_Type()
)
speedMux200gLinePortOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    speedMux200gLinePortOperState.setStatus("current")


class _SpeedMux200gLinePortLoopConfig_Type(Integer32):
    """Custom type speedMux200gLinePortLoopConfig based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("notAvailable", 0),
          ("off", 1),
          ("internal", 3),
          ("external", 4))
    )


_SpeedMux200gLinePortLoopConfig_Type.__name__ = "Integer32"
_SpeedMux200gLinePortLoopConfig_Object = MibTableColumn
speedMux200gLinePortLoopConfig = _SpeedMux200gLinePortLoopConfig_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 4, 1, 5, 1, 7),
    _SpeedMux200gLinePortLoopConfig_Type()
)
speedMux200gLinePortLoopConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    speedMux200gLinePortLoopConfig.setStatus("current")


class _SpeedMux200gLinePortAlarmDeactivation_Type(Integer32):
    """Custom type speedMux200gLinePortAlarmDeactivation based on Integer32"""
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


_SpeedMux200gLinePortAlarmDeactivation_Type.__name__ = "Integer32"
_SpeedMux200gLinePortAlarmDeactivation_Object = MibTableColumn
speedMux200gLinePortAlarmDeactivation = _SpeedMux200gLinePortAlarmDeactivation_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 4, 1, 5, 1, 8),
    _SpeedMux200gLinePortAlarmDeactivation_Type()
)
speedMux200gLinePortAlarmDeactivation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    speedMux200gLinePortAlarmDeactivation.setStatus("current")


class _SpeedMux200gLinePortAlarmSchedule_Type(Integer32):
    """Custom type speedMux200gLinePortAlarmSchedule based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1200),
    )


_SpeedMux200gLinePortAlarmSchedule_Type.__name__ = "Integer32"
_SpeedMux200gLinePortAlarmSchedule_Object = MibTableColumn
speedMux200gLinePortAlarmSchedule = _SpeedMux200gLinePortAlarmSchedule_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 4, 1, 5, 1, 9),
    _SpeedMux200gLinePortAlarmSchedule_Type()
)
speedMux200gLinePortAlarmSchedule.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    speedMux200gLinePortAlarmSchedule.setStatus("current")


class _SpeedMux200gLinePortSpeed_Type(Integer32):
    """Custom type speedMux200gLinePortSpeed based on Integer32"""
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
        *(("notavailable", 0),
          ("eth100G", 1),
          ("otu4", 2),
          ("eth2x40G", 3))
    )


_SpeedMux200gLinePortSpeed_Type.__name__ = "Integer32"
_SpeedMux200gLinePortSpeed_Object = MibTableColumn
speedMux200gLinePortSpeed = _SpeedMux200gLinePortSpeed_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 4, 1, 5, 1, 10),
    _SpeedMux200gLinePortSpeed_Type()
)
speedMux200gLinePortSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    speedMux200gLinePortSpeed.setStatus("current")
_SpeedMux200gLineGroup_Type = Integer32
_SpeedMux200gLineGroup_Object = MibTableColumn
speedMux200gLineGroup = _SpeedMux200gLineGroup_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 4, 1, 5, 1, 11),
    _SpeedMux200gLineGroup_Type()
)
speedMux200gLineGroup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    speedMux200gLineGroup.setStatus("current")


class _SpeedMux200gLinePortLLCFconfig_Type(Integer32):
    """Custom type speedMux200gLinePortLLCFconfig based on Integer32"""
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


_SpeedMux200gLinePortLLCFconfig_Type.__name__ = "Integer32"
_SpeedMux200gLinePortLLCFconfig_Object = MibTableColumn
speedMux200gLinePortLLCFconfig = _SpeedMux200gLinePortLLCFconfig_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 4, 1, 5, 1, 12),
    _SpeedMux200gLinePortLLCFconfig_Type()
)
speedMux200gLinePortLLCFconfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    speedMux200gLinePortLLCFconfig.setStatus("current")


class _SpeedMux200gLinePortXCVtunableConfigSelection_Type(Integer32):
    """Custom type speedMux200gLinePortXCVtunableConfigSelection based on Integer32"""
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


_SpeedMux200gLinePortXCVtunableConfigSelection_Type.__name__ = "Integer32"
_SpeedMux200gLinePortXCVtunableConfigSelection_Object = MibTableColumn
speedMux200gLinePortXCVtunableConfigSelection = _SpeedMux200gLinePortXCVtunableConfigSelection_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 4, 1, 5, 1, 13),
    _SpeedMux200gLinePortXCVtunableConfigSelection_Type()
)
speedMux200gLinePortXCVtunableConfigSelection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    speedMux200gLinePortXCVtunableConfigSelection.setStatus("current")


class _SpeedMux200gLinePortXCVtunChannelConfig_Type(DisplayString):
    """Custom type speedMux200gLinePortXCVtunChannelConfig based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 4),
    )


_SpeedMux200gLinePortXCVtunChannelConfig_Type.__name__ = "DisplayString"
_SpeedMux200gLinePortXCVtunChannelConfig_Object = MibTableColumn
speedMux200gLinePortXCVtunChannelConfig = _SpeedMux200gLinePortXCVtunChannelConfig_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 4, 1, 5, 1, 14),
    _SpeedMux200gLinePortXCVtunChannelConfig_Type()
)
speedMux200gLinePortXCVtunChannelConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    speedMux200gLinePortXCVtunChannelConfig.setStatus("current")


class _SpeedMux200gLinePortXCVtunWavelengthConfig_Type(Integer32):
    """Custom type speedMux200gLinePortXCVtunWavelengthConfig based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1528350, 1577100),
    )


_SpeedMux200gLinePortXCVtunWavelengthConfig_Type.__name__ = "Integer32"
_SpeedMux200gLinePortXCVtunWavelengthConfig_Object = MibTableColumn
speedMux200gLinePortXCVtunWavelengthConfig = _SpeedMux200gLinePortXCVtunWavelengthConfig_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 4, 1, 5, 1, 15),
    _SpeedMux200gLinePortXCVtunWavelengthConfig_Type()
)
speedMux200gLinePortXCVtunWavelengthConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    speedMux200gLinePortXCVtunWavelengthConfig.setStatus("current")


class _SpeedMux200gLinePortXCVTxPower_Type(Integer32):
    """Custom type speedMux200gLinePortXCVTxPower based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1500, 100),
    )


_SpeedMux200gLinePortXCVTxPower_Type.__name__ = "Integer32"
_SpeedMux200gLinePortXCVTxPower_Object = MibTableColumn
speedMux200gLinePortXCVTxPower = _SpeedMux200gLinePortXCVTxPower_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 4, 1, 5, 1, 16),
    _SpeedMux200gLinePortXCVTxPower_Type()
)
speedMux200gLinePortXCVTxPower.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    speedMux200gLinePortXCVTxPower.setStatus("current")
_SpeedMux200gLinePortXCVConfigDispersion_Type = Integer32
_SpeedMux200gLinePortXCVConfigDispersion_Object = MibTableColumn
speedMux200gLinePortXCVConfigDispersion = _SpeedMux200gLinePortXCVConfigDispersion_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 4, 1, 5, 1, 17),
    _SpeedMux200gLinePortXCVConfigDispersion_Type()
)
speedMux200gLinePortXCVConfigDispersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    speedMux200gLinePortXCVConfigDispersion.setStatus("current")


class _SpeedMux200gLinePortEncryption_Type(Integer32):
    """Custom type speedMux200gLinePortEncryption based on Integer32"""
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
          ("noLicense", 1),
          ("off", 2),
          ("running", 3),
          ("syncronisation", 4),
          ("failure", 5),
          ("weak", 6),
          ("bypass", 7),
          ("unknown", 255))
    )


_SpeedMux200gLinePortEncryption_Type.__name__ = "Integer32"
_SpeedMux200gLinePortEncryption_Object = MibTableColumn
speedMux200gLinePortEncryption = _SpeedMux200gLinePortEncryption_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 4, 1, 5, 1, 18),
    _SpeedMux200gLinePortEncryption_Type()
)
speedMux200gLinePortEncryption.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    speedMux200gLinePortEncryption.setStatus("current")


class _SpeedMux200gLinePortModulationConfig_Type(Integer32):
    """Custom type speedMux200gLinePortModulationConfig based on Integer32"""
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
          ("mod8QAM", 1),
          ("mod16QAM", 2),
          ("modDPQPSK", 3))
    )


_SpeedMux200gLinePortModulationConfig_Type.__name__ = "Integer32"
_SpeedMux200gLinePortModulationConfig_Object = MibTableColumn
speedMux200gLinePortModulationConfig = _SpeedMux200gLinePortModulationConfig_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 4, 1, 5, 1, 19),
    _SpeedMux200gLinePortModulationConfig_Type()
)
speedMux200gLinePortModulationConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    speedMux200gLinePortModulationConfig.setStatus("current")
_SpeedMux200gClientPortXCVInfoTable_Object = MibTable
speedMux200gClientPortXCVInfoTable = _SpeedMux200gClientPortXCVInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 4, 1, 6)
)
if mibBuilder.loadTexts:
    speedMux200gClientPortXCVInfoTable.setStatus("current")
_SpeedMux200gClientPortXCVInfoEntry_Object = MibTableRow
speedMux200gClientPortXCVInfoEntry = _SpeedMux200gClientPortXCVInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 4, 1, 6, 1)
)
speedMux200gClientPortXCVInfoEntry.setIndexNames(
    (0, "SPEED-MUX-200G-MIB", "speedMux200gClientPortXCVInfoIndex"),
)
if mibBuilder.loadTexts:
    speedMux200gClientPortXCVInfoEntry.setStatus("current")


class _SpeedMux200gClientPortXCVInfoIndex_Type(Integer32):
    """Custom type speedMux200gClientPortXCVInfoIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1900),
    )


_SpeedMux200gClientPortXCVInfoIndex_Type.__name__ = "Integer32"
_SpeedMux200gClientPortXCVInfoIndex_Object = MibTableColumn
speedMux200gClientPortXCVInfoIndex = _SpeedMux200gClientPortXCVInfoIndex_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 4, 1, 6, 1, 1),
    _SpeedMux200gClientPortXCVInfoIndex_Type()
)
speedMux200gClientPortXCVInfoIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    speedMux200gClientPortXCVInfoIndex.setStatus("current")
_SpeedMux200gClientXCVInfoSlot_Type = Integer32
_SpeedMux200gClientXCVInfoSlot_Object = MibTableColumn
speedMux200gClientXCVInfoSlot = _SpeedMux200gClientXCVInfoSlot_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 4, 1, 6, 1, 2),
    _SpeedMux200gClientXCVInfoSlot_Type()
)
speedMux200gClientXCVInfoSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    speedMux200gClientXCVInfoSlot.setStatus("current")
_SpeedMux200gClientXCVInfoPort_Type = Integer32
_SpeedMux200gClientXCVInfoPort_Object = MibTableColumn
speedMux200gClientXCVInfoPort = _SpeedMux200gClientXCVInfoPort_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 4, 1, 6, 1, 3),
    _SpeedMux200gClientXCVInfoPort_Type()
)
speedMux200gClientXCVInfoPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    speedMux200gClientXCVInfoPort.setStatus("current")


class _SpeedMux200gClientPortXCVState_Type(Integer32):
    """Custom type speedMux200gClientPortXCVState based on Integer32"""
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
          ("removed", 1),
          ("installed", 2),
          ("downTxFault", 3))
    )


_SpeedMux200gClientPortXCVState_Type.__name__ = "Integer32"
_SpeedMux200gClientPortXCVState_Object = MibTableColumn
speedMux200gClientPortXCVState = _SpeedMux200gClientPortXCVState_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 4, 1, 6, 1, 4),
    _SpeedMux200gClientPortXCVState_Type()
)
speedMux200gClientPortXCVState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    speedMux200gClientPortXCVState.setStatus("current")


class _SpeedMux200gClientPortXCVVendorName_Type(DisplayString):
    """Custom type speedMux200gClientPortXCVVendorName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_SpeedMux200gClientPortXCVVendorName_Type.__name__ = "DisplayString"
_SpeedMux200gClientPortXCVVendorName_Object = MibTableColumn
speedMux200gClientPortXCVVendorName = _SpeedMux200gClientPortXCVVendorName_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 4, 1, 6, 1, 5),
    _SpeedMux200gClientPortXCVVendorName_Type()
)
speedMux200gClientPortXCVVendorName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    speedMux200gClientPortXCVVendorName.setStatus("current")


class _SpeedMux200gClientPortXCVVendorPartNumber_Type(DisplayString):
    """Custom type speedMux200gClientPortXCVVendorPartNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_SpeedMux200gClientPortXCVVendorPartNumber_Type.__name__ = "DisplayString"
_SpeedMux200gClientPortXCVVendorPartNumber_Object = MibTableColumn
speedMux200gClientPortXCVVendorPartNumber = _SpeedMux200gClientPortXCVVendorPartNumber_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 4, 1, 6, 1, 6),
    _SpeedMux200gClientPortXCVVendorPartNumber_Type()
)
speedMux200gClientPortXCVVendorPartNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    speedMux200gClientPortXCVVendorPartNumber.setStatus("current")


class _SpeedMux200gClientPortXCVVendorSerialNumber_Type(DisplayString):
    """Custom type speedMux200gClientPortXCVVendorSerialNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_SpeedMux200gClientPortXCVVendorSerialNumber_Type.__name__ = "DisplayString"
_SpeedMux200gClientPortXCVVendorSerialNumber_Object = MibTableColumn
speedMux200gClientPortXCVVendorSerialNumber = _SpeedMux200gClientPortXCVVendorSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 4, 1, 6, 1, 7),
    _SpeedMux200gClientPortXCVVendorSerialNumber_Type()
)
speedMux200gClientPortXCVVendorSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    speedMux200gClientPortXCVVendorSerialNumber.setStatus("current")


class _SpeedMux200gClientPortXCVType_Type(Integer32):
    """Custom type speedMux200gClientPortXCVType based on Integer32"""
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
              10)
        )
    )
    namedValues = NamedValues(
        *(("notAvailable", 0),
          ("sfp", 1),
          ("xfp", 2),
          ("dwdmSfp", 3),
          ("qsfp", 4),
          ("qsfpPlus", 5),
          ("cfp", 6),
          ("cxp", 7),
          ("cfp2", 8),
          ("cfp4", 9),
          ("qsfp28", 10))
    )


_SpeedMux200gClientPortXCVType_Type.__name__ = "Integer32"
_SpeedMux200gClientPortXCVType_Object = MibTableColumn
speedMux200gClientPortXCVType = _SpeedMux200gClientPortXCVType_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 4, 1, 6, 1, 8),
    _SpeedMux200gClientPortXCVType_Type()
)
speedMux200gClientPortXCVType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    speedMux200gClientPortXCVType.setStatus("current")


class _SpeedMux200gClientPortXCVConnector_Type(Integer32):
    """Custom type speedMux200gClientPortXCVConnector based on Integer32"""
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
              14)
        )
    )
    namedValues = NamedValues(
        *(("notAvailable", 0),
          ("lc", 1),
          ("sc", 2),
          ("mpo", 3),
          ("rj45", 4),
          ("fc", 5),
          ("bnc", 6),
          ("fj", 7),
          ("mtRj", 8),
          ("mu", 9),
          ("sg", 10),
          ("op", 11),
          ("hssdc", 12),
          ("cp", 13),
          ("mxc", 14))
    )


_SpeedMux200gClientPortXCVConnector_Type.__name__ = "Integer32"
_SpeedMux200gClientPortXCVConnector_Object = MibTableColumn
speedMux200gClientPortXCVConnector = _SpeedMux200gClientPortXCVConnector_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 4, 1, 6, 1, 9),
    _SpeedMux200gClientPortXCVConnector_Type()
)
speedMux200gClientPortXCVConnector.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    speedMux200gClientPortXCVConnector.setStatus("current")
_SpeedMux200gClientPortXCVLaneCount_Type = Integer32
_SpeedMux200gClientPortXCVLaneCount_Object = MibTableColumn
speedMux200gClientPortXCVLaneCount = _SpeedMux200gClientPortXCVLaneCount_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 4, 1, 6, 1, 10),
    _SpeedMux200gClientPortXCVLaneCount_Type()
)
speedMux200gClientPortXCVLaneCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    speedMux200gClientPortXCVLaneCount.setStatus("current")
_SpeedMux200gClientPortXCVWavelengthLane1_Type = Integer32
_SpeedMux200gClientPortXCVWavelengthLane1_Object = MibTableColumn
speedMux200gClientPortXCVWavelengthLane1 = _SpeedMux200gClientPortXCVWavelengthLane1_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 4, 1, 6, 1, 11),
    _SpeedMux200gClientPortXCVWavelengthLane1_Type()
)
speedMux200gClientPortXCVWavelengthLane1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    speedMux200gClientPortXCVWavelengthLane1.setStatus("current")
_SpeedMux200gClientPortXCVWavelengthLane2_Type = Integer32
_SpeedMux200gClientPortXCVWavelengthLane2_Object = MibTableColumn
speedMux200gClientPortXCVWavelengthLane2 = _SpeedMux200gClientPortXCVWavelengthLane2_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 4, 1, 6, 1, 12),
    _SpeedMux200gClientPortXCVWavelengthLane2_Type()
)
speedMux200gClientPortXCVWavelengthLane2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    speedMux200gClientPortXCVWavelengthLane2.setStatus("current")
_SpeedMux200gClientPortXCVWavelengthLane3_Type = Integer32
_SpeedMux200gClientPortXCVWavelengthLane3_Object = MibTableColumn
speedMux200gClientPortXCVWavelengthLane3 = _SpeedMux200gClientPortXCVWavelengthLane3_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 4, 1, 6, 1, 13),
    _SpeedMux200gClientPortXCVWavelengthLane3_Type()
)
speedMux200gClientPortXCVWavelengthLane3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    speedMux200gClientPortXCVWavelengthLane3.setStatus("current")
_SpeedMux200gClientPortXCVWavelengthLane4_Type = Integer32
_SpeedMux200gClientPortXCVWavelengthLane4_Object = MibTableColumn
speedMux200gClientPortXCVWavelengthLane4 = _SpeedMux200gClientPortXCVWavelengthLane4_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 4, 1, 6, 1, 14),
    _SpeedMux200gClientPortXCVWavelengthLane4_Type()
)
speedMux200gClientPortXCVWavelengthLane4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    speedMux200gClientPortXCVWavelengthLane4.setStatus("current")


class _SpeedMux200gClientPortXCVDMIState_Type(Integer32):
    """Custom type speedMux200gClientPortXCVDMIState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("notSupported", 0),
          ("implemented", 1))
    )


_SpeedMux200gClientPortXCVDMIState_Type.__name__ = "Integer32"
_SpeedMux200gClientPortXCVDMIState_Object = MibTableColumn
speedMux200gClientPortXCVDMIState = _SpeedMux200gClientPortXCVDMIState_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 4, 1, 6, 1, 15),
    _SpeedMux200gClientPortXCVDMIState_Type()
)
speedMux200gClientPortXCVDMIState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    speedMux200gClientPortXCVDMIState.setStatus("current")
_SpeedMux200gClientPortXCVDMITemp_Type = Integer32
_SpeedMux200gClientPortXCVDMITemp_Object = MibTableColumn
speedMux200gClientPortXCVDMITemp = _SpeedMux200gClientPortXCVDMITemp_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 4, 1, 6, 1, 16),
    _SpeedMux200gClientPortXCVDMITemp_Type()
)
speedMux200gClientPortXCVDMITemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    speedMux200gClientPortXCVDMITemp.setStatus("current")
_SpeedMux200gLinePortXCVInfoTable_Object = MibTable
speedMux200gLinePortXCVInfoTable = _SpeedMux200gLinePortXCVInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 4, 1, 7)
)
if mibBuilder.loadTexts:
    speedMux200gLinePortXCVInfoTable.setStatus("current")
_SpeedMux200gLinePortXCVInfoEntry_Object = MibTableRow
speedMux200gLinePortXCVInfoEntry = _SpeedMux200gLinePortXCVInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 4, 1, 7, 1)
)
speedMux200gLinePortXCVInfoEntry.setIndexNames(
    (0, "SPEED-MUX-200G-MIB", "speedMux200gLinePortXCVInfoIndex"),
)
if mibBuilder.loadTexts:
    speedMux200gLinePortXCVInfoEntry.setStatus("current")


class _SpeedMux200gLinePortXCVInfoIndex_Type(Integer32):
    """Custom type speedMux200gLinePortXCVInfoIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1900),
    )


_SpeedMux200gLinePortXCVInfoIndex_Type.__name__ = "Integer32"
_SpeedMux200gLinePortXCVInfoIndex_Object = MibTableColumn
speedMux200gLinePortXCVInfoIndex = _SpeedMux200gLinePortXCVInfoIndex_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 4, 1, 7, 1, 1),
    _SpeedMux200gLinePortXCVInfoIndex_Type()
)
speedMux200gLinePortXCVInfoIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    speedMux200gLinePortXCVInfoIndex.setStatus("current")
_SpeedMux200gLineXCVInfoSlot_Type = Integer32
_SpeedMux200gLineXCVInfoSlot_Object = MibTableColumn
speedMux200gLineXCVInfoSlot = _SpeedMux200gLineXCVInfoSlot_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 4, 1, 7, 1, 2),
    _SpeedMux200gLineXCVInfoSlot_Type()
)
speedMux200gLineXCVInfoSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    speedMux200gLineXCVInfoSlot.setStatus("current")
_SpeedMux200gLineXCVInfoPort_Type = Integer32
_SpeedMux200gLineXCVInfoPort_Object = MibTableColumn
speedMux200gLineXCVInfoPort = _SpeedMux200gLineXCVInfoPort_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 4, 1, 7, 1, 3),
    _SpeedMux200gLineXCVInfoPort_Type()
)
speedMux200gLineXCVInfoPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    speedMux200gLineXCVInfoPort.setStatus("current")


class _SpeedMux200gLinePortXCVState_Type(Integer32):
    """Custom type speedMux200gLinePortXCVState based on Integer32"""
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
          ("removed", 1),
          ("installed", 2),
          ("downTxFault", 3))
    )


_SpeedMux200gLinePortXCVState_Type.__name__ = "Integer32"
_SpeedMux200gLinePortXCVState_Object = MibTableColumn
speedMux200gLinePortXCVState = _SpeedMux200gLinePortXCVState_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 4, 1, 7, 1, 4),
    _SpeedMux200gLinePortXCVState_Type()
)
speedMux200gLinePortXCVState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    speedMux200gLinePortXCVState.setStatus("current")


class _SpeedMux200gLinePortXCVVendorName_Type(DisplayString):
    """Custom type speedMux200gLinePortXCVVendorName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_SpeedMux200gLinePortXCVVendorName_Type.__name__ = "DisplayString"
_SpeedMux200gLinePortXCVVendorName_Object = MibTableColumn
speedMux200gLinePortXCVVendorName = _SpeedMux200gLinePortXCVVendorName_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 4, 1, 7, 1, 5),
    _SpeedMux200gLinePortXCVVendorName_Type()
)
speedMux200gLinePortXCVVendorName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    speedMux200gLinePortXCVVendorName.setStatus("current")


class _SpeedMux200gLinePortXCVVendorPartNumber_Type(DisplayString):
    """Custom type speedMux200gLinePortXCVVendorPartNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_SpeedMux200gLinePortXCVVendorPartNumber_Type.__name__ = "DisplayString"
_SpeedMux200gLinePortXCVVendorPartNumber_Object = MibTableColumn
speedMux200gLinePortXCVVendorPartNumber = _SpeedMux200gLinePortXCVVendorPartNumber_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 4, 1, 7, 1, 6),
    _SpeedMux200gLinePortXCVVendorPartNumber_Type()
)
speedMux200gLinePortXCVVendorPartNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    speedMux200gLinePortXCVVendorPartNumber.setStatus("current")


class _SpeedMux200gLinePortXCVVendorSerialNumber_Type(DisplayString):
    """Custom type speedMux200gLinePortXCVVendorSerialNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_SpeedMux200gLinePortXCVVendorSerialNumber_Type.__name__ = "DisplayString"
_SpeedMux200gLinePortXCVVendorSerialNumber_Object = MibTableColumn
speedMux200gLinePortXCVVendorSerialNumber = _SpeedMux200gLinePortXCVVendorSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 4, 1, 7, 1, 7),
    _SpeedMux200gLinePortXCVVendorSerialNumber_Type()
)
speedMux200gLinePortXCVVendorSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    speedMux200gLinePortXCVVendorSerialNumber.setStatus("current")


class _SpeedMux200gLinePortXCVType_Type(Integer32):
    """Custom type speedMux200gLinePortXCVType based on Integer32"""
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
              10)
        )
    )
    namedValues = NamedValues(
        *(("notAvailable", 0),
          ("sfp", 1),
          ("xfp", 2),
          ("dwdmSfp", 3),
          ("qsfp", 4),
          ("qsfpPlus", 5),
          ("cfp", 6),
          ("cxp", 7),
          ("cfp2", 8),
          ("cfp4", 9),
          ("qsfp28", 10))
    )


_SpeedMux200gLinePortXCVType_Type.__name__ = "Integer32"
_SpeedMux200gLinePortXCVType_Object = MibTableColumn
speedMux200gLinePortXCVType = _SpeedMux200gLinePortXCVType_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 4, 1, 7, 1, 8),
    _SpeedMux200gLinePortXCVType_Type()
)
speedMux200gLinePortXCVType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    speedMux200gLinePortXCVType.setStatus("current")
_SpeedMux200gLinePortXCVLaneCount_Type = Integer32
_SpeedMux200gLinePortXCVLaneCount_Object = MibTableColumn
speedMux200gLinePortXCVLaneCount = _SpeedMux200gLinePortXCVLaneCount_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 4, 1, 7, 1, 9),
    _SpeedMux200gLinePortXCVLaneCount_Type()
)
speedMux200gLinePortXCVLaneCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    speedMux200gLinePortXCVLaneCount.setStatus("current")


class _SpeedMux200gLinePortXCVDMIState_Type(Integer32):
    """Custom type speedMux200gLinePortXCVDMIState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("notSupported", 0),
          ("implemented", 1))
    )


_SpeedMux200gLinePortXCVDMIState_Type.__name__ = "Integer32"
_SpeedMux200gLinePortXCVDMIState_Object = MibTableColumn
speedMux200gLinePortXCVDMIState = _SpeedMux200gLinePortXCVDMIState_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 4, 1, 7, 1, 10),
    _SpeedMux200gLinePortXCVDMIState_Type()
)
speedMux200gLinePortXCVDMIState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    speedMux200gLinePortXCVDMIState.setStatus("current")


class _SpeedMux200gLinePortXCVDWDMChannel_Type(DisplayString):
    """Custom type speedMux200gLinePortXCVDWDMChannel based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 4),
    )


_SpeedMux200gLinePortXCVDWDMChannel_Type.__name__ = "DisplayString"
_SpeedMux200gLinePortXCVDWDMChannel_Object = MibTableColumn
speedMux200gLinePortXCVDWDMChannel = _SpeedMux200gLinePortXCVDWDMChannel_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 4, 1, 7, 1, 11),
    _SpeedMux200gLinePortXCVDWDMChannel_Type()
)
speedMux200gLinePortXCVDWDMChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    speedMux200gLinePortXCVDWDMChannel.setStatus("current")


class _SpeedMux200gLinePortXCVtunFunctionality_Type(Integer32):
    """Custom type speedMux200gLinePortXCVtunFunctionality based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("notSupported", 0),
          ("implemented", 1))
    )


_SpeedMux200gLinePortXCVtunFunctionality_Type.__name__ = "Integer32"
_SpeedMux200gLinePortXCVtunFunctionality_Object = MibTableColumn
speedMux200gLinePortXCVtunFunctionality = _SpeedMux200gLinePortXCVtunFunctionality_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 4, 1, 7, 1, 12),
    _SpeedMux200gLinePortXCVtunFunctionality_Type()
)
speedMux200gLinePortXCVtunFunctionality.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    speedMux200gLinePortXCVtunFunctionality.setStatus("current")
_SpeedMux200gLinePortXCVtunChannelSpacing_Type = Integer32
_SpeedMux200gLinePortXCVtunChannelSpacing_Object = MibTableColumn
speedMux200gLinePortXCVtunChannelSpacing = _SpeedMux200gLinePortXCVtunChannelSpacing_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 4, 1, 7, 1, 13),
    _SpeedMux200gLinePortXCVtunChannelSpacing_Type()
)
speedMux200gLinePortXCVtunChannelSpacing.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    speedMux200gLinePortXCVtunChannelSpacing.setStatus("current")
_SpeedMux200gLinePortXCVtunNumberofChannels_Type = Integer32
_SpeedMux200gLinePortXCVtunNumberofChannels_Object = MibTableColumn
speedMux200gLinePortXCVtunNumberofChannels = _SpeedMux200gLinePortXCVtunNumberofChannels_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 4, 1, 7, 1, 14),
    _SpeedMux200gLinePortXCVtunNumberofChannels_Type()
)
speedMux200gLinePortXCVtunNumberofChannels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    speedMux200gLinePortXCVtunNumberofChannels.setStatus("current")


class _SpeedMux200gLinePortXCVtunFirstChannel_Type(DisplayString):
    """Custom type speedMux200gLinePortXCVtunFirstChannel based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 4),
    )


_SpeedMux200gLinePortXCVtunFirstChannel_Type.__name__ = "DisplayString"
_SpeedMux200gLinePortXCVtunFirstChannel_Object = MibTableColumn
speedMux200gLinePortXCVtunFirstChannel = _SpeedMux200gLinePortXCVtunFirstChannel_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 4, 1, 7, 1, 15),
    _SpeedMux200gLinePortXCVtunFirstChannel_Type()
)
speedMux200gLinePortXCVtunFirstChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    speedMux200gLinePortXCVtunFirstChannel.setStatus("current")


class _SpeedMux200gLinePortXCVtunLastChannel_Type(DisplayString):
    """Custom type speedMux200gLinePortXCVtunLastChannel based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 4),
    )


_SpeedMux200gLinePortXCVtunLastChannel_Type.__name__ = "DisplayString"
_SpeedMux200gLinePortXCVtunLastChannel_Object = MibTableColumn
speedMux200gLinePortXCVtunLastChannel = _SpeedMux200gLinePortXCVtunLastChannel_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 4, 1, 7, 1, 16),
    _SpeedMux200gLinePortXCVtunLastChannel_Type()
)
speedMux200gLinePortXCVtunLastChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    speedMux200gLinePortXCVtunLastChannel.setStatus("current")
_SpeedMux200gLinePortXCVtunFirstWavelength_Type = Integer32
_SpeedMux200gLinePortXCVtunFirstWavelength_Object = MibTableColumn
speedMux200gLinePortXCVtunFirstWavelength = _SpeedMux200gLinePortXCVtunFirstWavelength_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 4, 1, 7, 1, 17),
    _SpeedMux200gLinePortXCVtunFirstWavelength_Type()
)
speedMux200gLinePortXCVtunFirstWavelength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    speedMux200gLinePortXCVtunFirstWavelength.setStatus("current")
_SpeedMux200gLinePortXCVtunLastWavelength_Type = Integer32
_SpeedMux200gLinePortXCVtunLastWavelength_Object = MibTableColumn
speedMux200gLinePortXCVtunLastWavelength = _SpeedMux200gLinePortXCVtunLastWavelength_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 4, 1, 7, 1, 18),
    _SpeedMux200gLinePortXCVtunLastWavelength_Type()
)
speedMux200gLinePortXCVtunLastWavelength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    speedMux200gLinePortXCVtunLastWavelength.setStatus("current")
_SpeedMux200gLinePortXCVDMITemp_Type = Integer32
_SpeedMux200gLinePortXCVDMITemp_Object = MibTableColumn
speedMux200gLinePortXCVDMITemp = _SpeedMux200gLinePortXCVDMITemp_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 4, 1, 7, 1, 19),
    _SpeedMux200gLinePortXCVDMITemp_Type()
)
speedMux200gLinePortXCVDMITemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    speedMux200gLinePortXCVDMITemp.setStatus("current")
_SpeedMux200gClientPortXCVThresholdTable_Object = MibTable
speedMux200gClientPortXCVThresholdTable = _SpeedMux200gClientPortXCVThresholdTable_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 4, 1, 8)
)
if mibBuilder.loadTexts:
    speedMux200gClientPortXCVThresholdTable.setStatus("current")
_SpeedMux200gClientPortXCVThresholdEntry_Object = MibTableRow
speedMux200gClientPortXCVThresholdEntry = _SpeedMux200gClientPortXCVThresholdEntry_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 4, 1, 8, 1)
)
speedMux200gClientPortXCVThresholdEntry.setIndexNames(
    (0, "SPEED-MUX-200G-MIB", "speedMux200gClientPortXCVDMIIndex"),
)
if mibBuilder.loadTexts:
    speedMux200gClientPortXCVThresholdEntry.setStatus("current")


class _SpeedMux200gClientPortXCVDMIIndex_Type(Integer32):
    """Custom type speedMux200gClientPortXCVDMIIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1900),
    )


_SpeedMux200gClientPortXCVDMIIndex_Type.__name__ = "Integer32"
_SpeedMux200gClientPortXCVDMIIndex_Object = MibTableColumn
speedMux200gClientPortXCVDMIIndex = _SpeedMux200gClientPortXCVDMIIndex_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 4, 1, 8, 1, 1),
    _SpeedMux200gClientPortXCVDMIIndex_Type()
)
speedMux200gClientPortXCVDMIIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    speedMux200gClientPortXCVDMIIndex.setStatus("current")
_SpeedMux200gClientPortXCVDMISlot_Type = Integer32
_SpeedMux200gClientPortXCVDMISlot_Object = MibTableColumn
speedMux200gClientPortXCVDMISlot = _SpeedMux200gClientPortXCVDMISlot_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 4, 1, 8, 1, 2),
    _SpeedMux200gClientPortXCVDMISlot_Type()
)
speedMux200gClientPortXCVDMISlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    speedMux200gClientPortXCVDMISlot.setStatus("current")
_SpeedMux200gClientPortXCVDMIPort_Type = Integer32
_SpeedMux200gClientPortXCVDMIPort_Object = MibTableColumn
speedMux200gClientPortXCVDMIPort = _SpeedMux200gClientPortXCVDMIPort_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 4, 1, 8, 1, 3),
    _SpeedMux200gClientPortXCVDMIPort_Type()
)
speedMux200gClientPortXCVDMIPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    speedMux200gClientPortXCVDMIPort.setStatus("current")
_SpeedMux200gClientPortXCVDMIRxLowWarningThreshold_Type = Integer32
_SpeedMux200gClientPortXCVDMIRxLowWarningThreshold_Object = MibTableColumn
speedMux200gClientPortXCVDMIRxLowWarningThreshold = _SpeedMux200gClientPortXCVDMIRxLowWarningThreshold_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 4, 1, 8, 1, 4),
    _SpeedMux200gClientPortXCVDMIRxLowWarningThreshold_Type()
)
speedMux200gClientPortXCVDMIRxLowWarningThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    speedMux200gClientPortXCVDMIRxLowWarningThreshold.setStatus("current")
_SpeedMux200gClientPortXCVDMIRxLowAlarmThreshold_Type = Integer32
_SpeedMux200gClientPortXCVDMIRxLowAlarmThreshold_Object = MibTableColumn
speedMux200gClientPortXCVDMIRxLowAlarmThreshold = _SpeedMux200gClientPortXCVDMIRxLowAlarmThreshold_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 4, 1, 8, 1, 5),
    _SpeedMux200gClientPortXCVDMIRxLowAlarmThreshold_Type()
)
speedMux200gClientPortXCVDMIRxLowAlarmThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    speedMux200gClientPortXCVDMIRxLowAlarmThreshold.setStatus("current")
_SpeedMux200gClientPortXCVDMIRxHighWarningThreshold_Type = Integer32
_SpeedMux200gClientPortXCVDMIRxHighWarningThreshold_Object = MibTableColumn
speedMux200gClientPortXCVDMIRxHighWarningThreshold = _SpeedMux200gClientPortXCVDMIRxHighWarningThreshold_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 4, 1, 8, 1, 6),
    _SpeedMux200gClientPortXCVDMIRxHighWarningThreshold_Type()
)
speedMux200gClientPortXCVDMIRxHighWarningThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    speedMux200gClientPortXCVDMIRxHighWarningThreshold.setStatus("current")
_SpeedMux200gClientPortXCVDMIRxHighAlarmThreshold_Type = Integer32
_SpeedMux200gClientPortXCVDMIRxHighAlarmThreshold_Object = MibTableColumn
speedMux200gClientPortXCVDMIRxHighAlarmThreshold = _SpeedMux200gClientPortXCVDMIRxHighAlarmThreshold_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 4, 1, 8, 1, 7),
    _SpeedMux200gClientPortXCVDMIRxHighAlarmThreshold_Type()
)
speedMux200gClientPortXCVDMIRxHighAlarmThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    speedMux200gClientPortXCVDMIRxHighAlarmThreshold.setStatus("current")
_SpeedMux200gClientPortXCVDMITxLowWarningThreshold_Type = Integer32
_SpeedMux200gClientPortXCVDMITxLowWarningThreshold_Object = MibTableColumn
speedMux200gClientPortXCVDMITxLowWarningThreshold = _SpeedMux200gClientPortXCVDMITxLowWarningThreshold_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 4, 1, 8, 1, 8),
    _SpeedMux200gClientPortXCVDMITxLowWarningThreshold_Type()
)
speedMux200gClientPortXCVDMITxLowWarningThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    speedMux200gClientPortXCVDMITxLowWarningThreshold.setStatus("current")
_SpeedMux200gClientPortXCVDMITxLowAlarmThreshold_Type = Integer32
_SpeedMux200gClientPortXCVDMITxLowAlarmThreshold_Object = MibTableColumn
speedMux200gClientPortXCVDMITxLowAlarmThreshold = _SpeedMux200gClientPortXCVDMITxLowAlarmThreshold_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 4, 1, 8, 1, 9),
    _SpeedMux200gClientPortXCVDMITxLowAlarmThreshold_Type()
)
speedMux200gClientPortXCVDMITxLowAlarmThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    speedMux200gClientPortXCVDMITxLowAlarmThreshold.setStatus("current")
_SpeedMux200gClientPortXCVDMIBiasLowAlarmThreshold_Type = Integer32
_SpeedMux200gClientPortXCVDMIBiasLowAlarmThreshold_Object = MibTableColumn
speedMux200gClientPortXCVDMIBiasLowAlarmThreshold = _SpeedMux200gClientPortXCVDMIBiasLowAlarmThreshold_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 4, 1, 8, 1, 10),
    _SpeedMux200gClientPortXCVDMIBiasLowAlarmThreshold_Type()
)
speedMux200gClientPortXCVDMIBiasLowAlarmThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    speedMux200gClientPortXCVDMIBiasLowAlarmThreshold.setStatus("current")
_SpeedMux200gClientPortXCVDMIBiasHighAlarmThreshold_Type = Integer32
_SpeedMux200gClientPortXCVDMIBiasHighAlarmThreshold_Object = MibTableColumn
speedMux200gClientPortXCVDMIBiasHighAlarmThreshold = _SpeedMux200gClientPortXCVDMIBiasHighAlarmThreshold_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 4, 1, 8, 1, 11),
    _SpeedMux200gClientPortXCVDMIBiasHighAlarmThreshold_Type()
)
speedMux200gClientPortXCVDMIBiasHighAlarmThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    speedMux200gClientPortXCVDMIBiasHighAlarmThreshold.setStatus("current")
_SpeedMux200gClientPortXCVDMITempWarningThreshold_Type = Integer32
_SpeedMux200gClientPortXCVDMITempWarningThreshold_Object = MibTableColumn
speedMux200gClientPortXCVDMITempWarningThreshold = _SpeedMux200gClientPortXCVDMITempWarningThreshold_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 4, 1, 8, 1, 12),
    _SpeedMux200gClientPortXCVDMITempWarningThreshold_Type()
)
speedMux200gClientPortXCVDMITempWarningThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    speedMux200gClientPortXCVDMITempWarningThreshold.setStatus("current")
_SpeedMux200gClientPortXCVDMITempAlarmThreshold_Type = Integer32
_SpeedMux200gClientPortXCVDMITempAlarmThreshold_Object = MibTableColumn
speedMux200gClientPortXCVDMITempAlarmThreshold = _SpeedMux200gClientPortXCVDMITempAlarmThreshold_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 4, 1, 8, 1, 13),
    _SpeedMux200gClientPortXCVDMITempAlarmThreshold_Type()
)
speedMux200gClientPortXCVDMITempAlarmThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    speedMux200gClientPortXCVDMITempAlarmThreshold.setStatus("current")
_SpeedMux200gLinePortXCVThresholdTable_Object = MibTable
speedMux200gLinePortXCVThresholdTable = _SpeedMux200gLinePortXCVThresholdTable_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 4, 1, 9)
)
if mibBuilder.loadTexts:
    speedMux200gLinePortXCVThresholdTable.setStatus("current")
_SpeedMux200gLinePortXCVThresholdEntry_Object = MibTableRow
speedMux200gLinePortXCVThresholdEntry = _SpeedMux200gLinePortXCVThresholdEntry_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 4, 1, 9, 1)
)
speedMux200gLinePortXCVThresholdEntry.setIndexNames(
    (0, "SPEED-MUX-200G-MIB", "speedMux200gLinePortXCVDMIIndex"),
)
if mibBuilder.loadTexts:
    speedMux200gLinePortXCVThresholdEntry.setStatus("current")


class _SpeedMux200gLinePortXCVDMIIndex_Type(Integer32):
    """Custom type speedMux200gLinePortXCVDMIIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1900),
    )


_SpeedMux200gLinePortXCVDMIIndex_Type.__name__ = "Integer32"
_SpeedMux200gLinePortXCVDMIIndex_Object = MibTableColumn
speedMux200gLinePortXCVDMIIndex = _SpeedMux200gLinePortXCVDMIIndex_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 4, 1, 9, 1, 1),
    _SpeedMux200gLinePortXCVDMIIndex_Type()
)
speedMux200gLinePortXCVDMIIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    speedMux200gLinePortXCVDMIIndex.setStatus("current")
_SpeedMux200gLinePortXCVDMISlot_Type = Integer32
_SpeedMux200gLinePortXCVDMISlot_Object = MibTableColumn
speedMux200gLinePortXCVDMISlot = _SpeedMux200gLinePortXCVDMISlot_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 4, 1, 9, 1, 2),
    _SpeedMux200gLinePortXCVDMISlot_Type()
)
speedMux200gLinePortXCVDMISlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    speedMux200gLinePortXCVDMISlot.setStatus("current")
_SpeedMux200gLinePortXCVDMIPort_Type = Integer32
_SpeedMux200gLinePortXCVDMIPort_Object = MibTableColumn
speedMux200gLinePortXCVDMIPort = _SpeedMux200gLinePortXCVDMIPort_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 4, 1, 9, 1, 3),
    _SpeedMux200gLinePortXCVDMIPort_Type()
)
speedMux200gLinePortXCVDMIPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    speedMux200gLinePortXCVDMIPort.setStatus("current")
_SpeedMux200gLinePortXCVDMIRxLowWarningThreshold_Type = Integer32
_SpeedMux200gLinePortXCVDMIRxLowWarningThreshold_Object = MibTableColumn
speedMux200gLinePortXCVDMIRxLowWarningThreshold = _SpeedMux200gLinePortXCVDMIRxLowWarningThreshold_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 4, 1, 9, 1, 4),
    _SpeedMux200gLinePortXCVDMIRxLowWarningThreshold_Type()
)
speedMux200gLinePortXCVDMIRxLowWarningThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    speedMux200gLinePortXCVDMIRxLowWarningThreshold.setStatus("current")
_SpeedMux200gLinePortXCVDMIRxLowAlarmThreshold_Type = Integer32
_SpeedMux200gLinePortXCVDMIRxLowAlarmThreshold_Object = MibTableColumn
speedMux200gLinePortXCVDMIRxLowAlarmThreshold = _SpeedMux200gLinePortXCVDMIRxLowAlarmThreshold_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 4, 1, 9, 1, 5),
    _SpeedMux200gLinePortXCVDMIRxLowAlarmThreshold_Type()
)
speedMux200gLinePortXCVDMIRxLowAlarmThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    speedMux200gLinePortXCVDMIRxLowAlarmThreshold.setStatus("current")
_SpeedMux200gLinePortXCVDMIRxHighWarningThreshold_Type = Integer32
_SpeedMux200gLinePortXCVDMIRxHighWarningThreshold_Object = MibTableColumn
speedMux200gLinePortXCVDMIRxHighWarningThreshold = _SpeedMux200gLinePortXCVDMIRxHighWarningThreshold_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 4, 1, 9, 1, 6),
    _SpeedMux200gLinePortXCVDMIRxHighWarningThreshold_Type()
)
speedMux200gLinePortXCVDMIRxHighWarningThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    speedMux200gLinePortXCVDMIRxHighWarningThreshold.setStatus("current")
_SpeedMux200gLinePortXCVDMIRxHighAlarmThreshold_Type = Integer32
_SpeedMux200gLinePortXCVDMIRxHighAlarmThreshold_Object = MibTableColumn
speedMux200gLinePortXCVDMIRxHighAlarmThreshold = _SpeedMux200gLinePortXCVDMIRxHighAlarmThreshold_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 4, 1, 9, 1, 7),
    _SpeedMux200gLinePortXCVDMIRxHighAlarmThreshold_Type()
)
speedMux200gLinePortXCVDMIRxHighAlarmThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    speedMux200gLinePortXCVDMIRxHighAlarmThreshold.setStatus("current")
_SpeedMux200gLinePortXCVDMITxLowWarningThreshold_Type = Integer32
_SpeedMux200gLinePortXCVDMITxLowWarningThreshold_Object = MibTableColumn
speedMux200gLinePortXCVDMITxLowWarningThreshold = _SpeedMux200gLinePortXCVDMITxLowWarningThreshold_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 4, 1, 9, 1, 8),
    _SpeedMux200gLinePortXCVDMITxLowWarningThreshold_Type()
)
speedMux200gLinePortXCVDMITxLowWarningThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    speedMux200gLinePortXCVDMITxLowWarningThreshold.setStatus("current")
_SpeedMux200gLinePortXCVDMITxLowAlarmThreshold_Type = Integer32
_SpeedMux200gLinePortXCVDMITxLowAlarmThreshold_Object = MibTableColumn
speedMux200gLinePortXCVDMITxLowAlarmThreshold = _SpeedMux200gLinePortXCVDMITxLowAlarmThreshold_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 4, 1, 9, 1, 9),
    _SpeedMux200gLinePortXCVDMITxLowAlarmThreshold_Type()
)
speedMux200gLinePortXCVDMITxLowAlarmThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    speedMux200gLinePortXCVDMITxLowAlarmThreshold.setStatus("current")
_SpeedMux200gLinePortXCVDMIBiasLowAlarmThreshold_Type = Integer32
_SpeedMux200gLinePortXCVDMIBiasLowAlarmThreshold_Object = MibTableColumn
speedMux200gLinePortXCVDMIBiasLowAlarmThreshold = _SpeedMux200gLinePortXCVDMIBiasLowAlarmThreshold_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 4, 1, 9, 1, 10),
    _SpeedMux200gLinePortXCVDMIBiasLowAlarmThreshold_Type()
)
speedMux200gLinePortXCVDMIBiasLowAlarmThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    speedMux200gLinePortXCVDMIBiasLowAlarmThreshold.setStatus("current")
_SpeedMux200gLinePortXCVDMIBiasHighAlarmThreshold_Type = Integer32
_SpeedMux200gLinePortXCVDMIBiasHighAlarmThreshold_Object = MibTableColumn
speedMux200gLinePortXCVDMIBiasHighAlarmThreshold = _SpeedMux200gLinePortXCVDMIBiasHighAlarmThreshold_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 4, 1, 9, 1, 11),
    _SpeedMux200gLinePortXCVDMIBiasHighAlarmThreshold_Type()
)
speedMux200gLinePortXCVDMIBiasHighAlarmThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    speedMux200gLinePortXCVDMIBiasHighAlarmThreshold.setStatus("current")
_SpeedMux200gLinePortXCVDMITempWarningThreshold_Type = Integer32
_SpeedMux200gLinePortXCVDMITempWarningThreshold_Object = MibTableColumn
speedMux200gLinePortXCVDMITempWarningThreshold = _SpeedMux200gLinePortXCVDMITempWarningThreshold_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 4, 1, 9, 1, 12),
    _SpeedMux200gLinePortXCVDMITempWarningThreshold_Type()
)
speedMux200gLinePortXCVDMITempWarningThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    speedMux200gLinePortXCVDMITempWarningThreshold.setStatus("current")
_SpeedMux200gLinePortXCVDMITempAlarmThreshold_Type = Integer32
_SpeedMux200gLinePortXCVDMITempAlarmThreshold_Object = MibTableColumn
speedMux200gLinePortXCVDMITempAlarmThreshold = _SpeedMux200gLinePortXCVDMITempAlarmThreshold_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 4, 1, 9, 1, 13),
    _SpeedMux200gLinePortXCVDMITempAlarmThreshold_Type()
)
speedMux200gLinePortXCVDMITempAlarmThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    speedMux200gLinePortXCVDMITempAlarmThreshold.setStatus("current")
_SpeedMux200gClientPortXCVValueTable_Object = MibTable
speedMux200gClientPortXCVValueTable = _SpeedMux200gClientPortXCVValueTable_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 4, 1, 10)
)
if mibBuilder.loadTexts:
    speedMux200gClientPortXCVValueTable.setStatus("current")
_SpeedMux200gClientPortXCVValueEntry_Object = MibTableRow
speedMux200gClientPortXCVValueEntry = _SpeedMux200gClientPortXCVValueEntry_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 4, 1, 10, 1)
)
speedMux200gClientPortXCVValueEntry.setIndexNames(
    (0, "SPEED-MUX-200G-MIB", "speedMux200gClientPortXCVDMIMIndex"),
)
if mibBuilder.loadTexts:
    speedMux200gClientPortXCVValueEntry.setStatus("current")


class _SpeedMux200gClientPortXCVDMIMIndex_Type(Integer32):
    """Custom type speedMux200gClientPortXCVDMIMIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1900),
    )


_SpeedMux200gClientPortXCVDMIMIndex_Type.__name__ = "Integer32"
_SpeedMux200gClientPortXCVDMIMIndex_Object = MibTableColumn
speedMux200gClientPortXCVDMIMIndex = _SpeedMux200gClientPortXCVDMIMIndex_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 4, 1, 10, 1, 1),
    _SpeedMux200gClientPortXCVDMIMIndex_Type()
)
speedMux200gClientPortXCVDMIMIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    speedMux200gClientPortXCVDMIMIndex.setStatus("current")
_SpeedMux200gClientPortXCVDMIMSlot_Type = Integer32
_SpeedMux200gClientPortXCVDMIMSlot_Object = MibTableColumn
speedMux200gClientPortXCVDMIMSlot = _SpeedMux200gClientPortXCVDMIMSlot_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 4, 1, 10, 1, 2),
    _SpeedMux200gClientPortXCVDMIMSlot_Type()
)
speedMux200gClientPortXCVDMIMSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    speedMux200gClientPortXCVDMIMSlot.setStatus("current")
_SpeedMux200gClientPortXCVDMIMPort_Type = Integer32
_SpeedMux200gClientPortXCVDMIMPort_Object = MibTableColumn
speedMux200gClientPortXCVDMIMPort = _SpeedMux200gClientPortXCVDMIMPort_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 4, 1, 10, 1, 3),
    _SpeedMux200gClientPortXCVDMIMPort_Type()
)
speedMux200gClientPortXCVDMIMPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    speedMux200gClientPortXCVDMIMPort.setStatus("current")
_SpeedMux200gClientPortXCVDMIRxLevelLane1_Type = Integer32
_SpeedMux200gClientPortXCVDMIRxLevelLane1_Object = MibTableColumn
speedMux200gClientPortXCVDMIRxLevelLane1 = _SpeedMux200gClientPortXCVDMIRxLevelLane1_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 4, 1, 10, 1, 4),
    _SpeedMux200gClientPortXCVDMIRxLevelLane1_Type()
)
speedMux200gClientPortXCVDMIRxLevelLane1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    speedMux200gClientPortXCVDMIRxLevelLane1.setStatus("current")
_SpeedMux200gClientPortXCVDMIRxLevelLane2_Type = Integer32
_SpeedMux200gClientPortXCVDMIRxLevelLane2_Object = MibTableColumn
speedMux200gClientPortXCVDMIRxLevelLane2 = _SpeedMux200gClientPortXCVDMIRxLevelLane2_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 4, 1, 10, 1, 5),
    _SpeedMux200gClientPortXCVDMIRxLevelLane2_Type()
)
speedMux200gClientPortXCVDMIRxLevelLane2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    speedMux200gClientPortXCVDMIRxLevelLane2.setStatus("current")
_SpeedMux200gClientPortXCVDMIRxLevelLane3_Type = Integer32
_SpeedMux200gClientPortXCVDMIRxLevelLane3_Object = MibTableColumn
speedMux200gClientPortXCVDMIRxLevelLane3 = _SpeedMux200gClientPortXCVDMIRxLevelLane3_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 4, 1, 10, 1, 6),
    _SpeedMux200gClientPortXCVDMIRxLevelLane3_Type()
)
speedMux200gClientPortXCVDMIRxLevelLane3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    speedMux200gClientPortXCVDMIRxLevelLane3.setStatus("current")
_SpeedMux200gClientPortXCVDMIRxLevelLane4_Type = Integer32
_SpeedMux200gClientPortXCVDMIRxLevelLane4_Object = MibTableColumn
speedMux200gClientPortXCVDMIRxLevelLane4 = _SpeedMux200gClientPortXCVDMIRxLevelLane4_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 4, 1, 10, 1, 7),
    _SpeedMux200gClientPortXCVDMIRxLevelLane4_Type()
)
speedMux200gClientPortXCVDMIRxLevelLane4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    speedMux200gClientPortXCVDMIRxLevelLane4.setStatus("current")
_SpeedMux200gClientPortXCVDMITxLevelLane1_Type = Integer32
_SpeedMux200gClientPortXCVDMITxLevelLane1_Object = MibTableColumn
speedMux200gClientPortXCVDMITxLevelLane1 = _SpeedMux200gClientPortXCVDMITxLevelLane1_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 4, 1, 10, 1, 8),
    _SpeedMux200gClientPortXCVDMITxLevelLane1_Type()
)
speedMux200gClientPortXCVDMITxLevelLane1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    speedMux200gClientPortXCVDMITxLevelLane1.setStatus("current")
_SpeedMux200gClientPortXCVDMITxLevelLane2_Type = Integer32
_SpeedMux200gClientPortXCVDMITxLevelLane2_Object = MibTableColumn
speedMux200gClientPortXCVDMITxLevelLane2 = _SpeedMux200gClientPortXCVDMITxLevelLane2_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 4, 1, 10, 1, 9),
    _SpeedMux200gClientPortXCVDMITxLevelLane2_Type()
)
speedMux200gClientPortXCVDMITxLevelLane2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    speedMux200gClientPortXCVDMITxLevelLane2.setStatus("current")
_SpeedMux200gClientPortXCVDMITxLevelLane3_Type = Integer32
_SpeedMux200gClientPortXCVDMITxLevelLane3_Object = MibTableColumn
speedMux200gClientPortXCVDMITxLevelLane3 = _SpeedMux200gClientPortXCVDMITxLevelLane3_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 4, 1, 10, 1, 10),
    _SpeedMux200gClientPortXCVDMITxLevelLane3_Type()
)
speedMux200gClientPortXCVDMITxLevelLane3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    speedMux200gClientPortXCVDMITxLevelLane3.setStatus("current")
_SpeedMux200gClientPortXCVDMITxLevelLane4_Type = Integer32
_SpeedMux200gClientPortXCVDMITxLevelLane4_Object = MibTableColumn
speedMux200gClientPortXCVDMITxLevelLane4 = _SpeedMux200gClientPortXCVDMITxLevelLane4_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 4, 1, 10, 1, 11),
    _SpeedMux200gClientPortXCVDMITxLevelLane4_Type()
)
speedMux200gClientPortXCVDMITxLevelLane4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    speedMux200gClientPortXCVDMITxLevelLane4.setStatus("current")
_SpeedMux200gClientPortXCVDMITxBiasLane1_Type = Integer32
_SpeedMux200gClientPortXCVDMITxBiasLane1_Object = MibTableColumn
speedMux200gClientPortXCVDMITxBiasLane1 = _SpeedMux200gClientPortXCVDMITxBiasLane1_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 4, 1, 10, 1, 12),
    _SpeedMux200gClientPortXCVDMITxBiasLane1_Type()
)
speedMux200gClientPortXCVDMITxBiasLane1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    speedMux200gClientPortXCVDMITxBiasLane1.setStatus("current")
_SpeedMux200gClientPortXCVDMITxBiasLane2_Type = Integer32
_SpeedMux200gClientPortXCVDMITxBiasLane2_Object = MibTableColumn
speedMux200gClientPortXCVDMITxBiasLane2 = _SpeedMux200gClientPortXCVDMITxBiasLane2_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 4, 1, 10, 1, 13),
    _SpeedMux200gClientPortXCVDMITxBiasLane2_Type()
)
speedMux200gClientPortXCVDMITxBiasLane2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    speedMux200gClientPortXCVDMITxBiasLane2.setStatus("current")
_SpeedMux200gClientPortXCVDMITxBiasLane3_Type = Integer32
_SpeedMux200gClientPortXCVDMITxBiasLane3_Object = MibTableColumn
speedMux200gClientPortXCVDMITxBiasLane3 = _SpeedMux200gClientPortXCVDMITxBiasLane3_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 4, 1, 10, 1, 14),
    _SpeedMux200gClientPortXCVDMITxBiasLane3_Type()
)
speedMux200gClientPortXCVDMITxBiasLane3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    speedMux200gClientPortXCVDMITxBiasLane3.setStatus("current")
_SpeedMux200gClientPortXCVDMITxBiasLane4_Type = Integer32
_SpeedMux200gClientPortXCVDMITxBiasLane4_Object = MibTableColumn
speedMux200gClientPortXCVDMITxBiasLane4 = _SpeedMux200gClientPortXCVDMITxBiasLane4_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 4, 1, 10, 1, 15),
    _SpeedMux200gClientPortXCVDMITxBiasLane4_Type()
)
speedMux200gClientPortXCVDMITxBiasLane4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    speedMux200gClientPortXCVDMITxBiasLane4.setStatus("current")
_SpeedMux200gLinePortXCVValueTable_Object = MibTable
speedMux200gLinePortXCVValueTable = _SpeedMux200gLinePortXCVValueTable_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 4, 1, 11)
)
if mibBuilder.loadTexts:
    speedMux200gLinePortXCVValueTable.setStatus("current")
_SpeedMux200gLinePortXCVValueEntry_Object = MibTableRow
speedMux200gLinePortXCVValueEntry = _SpeedMux200gLinePortXCVValueEntry_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 4, 1, 11, 1)
)
speedMux200gLinePortXCVValueEntry.setIndexNames(
    (0, "SPEED-MUX-200G-MIB", "speedMux200gLinePortXCVDMIMIndex"),
)
if mibBuilder.loadTexts:
    speedMux200gLinePortXCVValueEntry.setStatus("current")


class _SpeedMux200gLinePortXCVDMIMIndex_Type(Integer32):
    """Custom type speedMux200gLinePortXCVDMIMIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1900),
    )


_SpeedMux200gLinePortXCVDMIMIndex_Type.__name__ = "Integer32"
_SpeedMux200gLinePortXCVDMIMIndex_Object = MibTableColumn
speedMux200gLinePortXCVDMIMIndex = _SpeedMux200gLinePortXCVDMIMIndex_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 4, 1, 11, 1, 1),
    _SpeedMux200gLinePortXCVDMIMIndex_Type()
)
speedMux200gLinePortXCVDMIMIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    speedMux200gLinePortXCVDMIMIndex.setStatus("current")
_SpeedMux200gLinePortXCVDMIMSlot_Type = Integer32
_SpeedMux200gLinePortXCVDMIMSlot_Object = MibTableColumn
speedMux200gLinePortXCVDMIMSlot = _SpeedMux200gLinePortXCVDMIMSlot_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 4, 1, 11, 1, 2),
    _SpeedMux200gLinePortXCVDMIMSlot_Type()
)
speedMux200gLinePortXCVDMIMSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    speedMux200gLinePortXCVDMIMSlot.setStatus("current")
_SpeedMux200gLinePortXCVDMIMPort_Type = Integer32
_SpeedMux200gLinePortXCVDMIMPort_Object = MibTableColumn
speedMux200gLinePortXCVDMIMPort = _SpeedMux200gLinePortXCVDMIMPort_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 4, 1, 11, 1, 3),
    _SpeedMux200gLinePortXCVDMIMPort_Type()
)
speedMux200gLinePortXCVDMIMPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    speedMux200gLinePortXCVDMIMPort.setStatus("current")
_SpeedMux200gLinePortXCVDMITempLevel_Type = Integer32
_SpeedMux200gLinePortXCVDMITempLevel_Object = MibTableColumn
speedMux200gLinePortXCVDMITempLevel = _SpeedMux200gLinePortXCVDMITempLevel_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 4, 1, 11, 1, 4),
    _SpeedMux200gLinePortXCVDMITempLevel_Type()
)
speedMux200gLinePortXCVDMITempLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    speedMux200gLinePortXCVDMITempLevel.setStatus("current")
_SpeedMux200gLinePortXCVDMIRxLevel_Type = Integer32
_SpeedMux200gLinePortXCVDMIRxLevel_Object = MibTableColumn
speedMux200gLinePortXCVDMIRxLevel = _SpeedMux200gLinePortXCVDMIRxLevel_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 4, 1, 11, 1, 5),
    _SpeedMux200gLinePortXCVDMIRxLevel_Type()
)
speedMux200gLinePortXCVDMIRxLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    speedMux200gLinePortXCVDMIRxLevel.setStatus("current")
if mibBuilder.loadTexts:
    speedMux200gLinePortXCVDMIRxLevel.setUnits("dBm")
_SpeedMux200gLinePortXCVDMITxLevel_Type = Integer32
_SpeedMux200gLinePortXCVDMITxLevel_Object = MibTableColumn
speedMux200gLinePortXCVDMITxLevel = _SpeedMux200gLinePortXCVDMITxLevel_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 4, 1, 11, 1, 6),
    _SpeedMux200gLinePortXCVDMITxLevel_Type()
)
speedMux200gLinePortXCVDMITxLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    speedMux200gLinePortXCVDMITxLevel.setStatus("current")
_SpeedMux200gLinePortXCVDMITxBias_Type = Integer32
_SpeedMux200gLinePortXCVDMITxBias_Object = MibTableColumn
speedMux200gLinePortXCVDMITxBias = _SpeedMux200gLinePortXCVDMITxBias_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 4, 1, 11, 1, 7),
    _SpeedMux200gLinePortXCVDMITxBias_Type()
)
speedMux200gLinePortXCVDMITxBias.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    speedMux200gLinePortXCVDMITxBias.setStatus("current")
_SpeedMux200gLinePortXCVDMIDispersion_Type = Integer32
_SpeedMux200gLinePortXCVDMIDispersion_Object = MibTableColumn
speedMux200gLinePortXCVDMIDispersion = _SpeedMux200gLinePortXCVDMIDispersion_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 4, 1, 11, 1, 8),
    _SpeedMux200gLinePortXCVDMIDispersion_Type()
)
speedMux200gLinePortXCVDMIDispersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    speedMux200gLinePortXCVDMIDispersion.setStatus("current")
_SpeedMux200gLinePortOTNFECcorrectedBits_Type = Counter64
_SpeedMux200gLinePortOTNFECcorrectedBits_Object = MibTableColumn
speedMux200gLinePortOTNFECcorrectedBits = _SpeedMux200gLinePortOTNFECcorrectedBits_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 4, 1, 11, 1, 9),
    _SpeedMux200gLinePortOTNFECcorrectedBits_Type()
)
speedMux200gLinePortOTNFECcorrectedBits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    speedMux200gLinePortOTNFECcorrectedBits.setStatus("current")
_SpeedMux200gLinePortOTNFECuncorrectedBlocks_Type = Counter64
_SpeedMux200gLinePortOTNFECuncorrectedBlocks_Object = MibTableColumn
speedMux200gLinePortOTNFECuncorrectedBlocks = _SpeedMux200gLinePortOTNFECuncorrectedBlocks_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 4, 1, 11, 1, 10),
    _SpeedMux200gLinePortOTNFECuncorrectedBlocks_Type()
)
speedMux200gLinePortOTNFECuncorrectedBlocks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    speedMux200gLinePortOTNFECuncorrectedBlocks.setStatus("current")
_SpeedMux200gClientPortXCVAlarmTable_Object = MibTable
speedMux200gClientPortXCVAlarmTable = _SpeedMux200gClientPortXCVAlarmTable_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 4, 1, 12)
)
if mibBuilder.loadTexts:
    speedMux200gClientPortXCVAlarmTable.setStatus("current")
_SpeedMux200gClientPortXCVAlarmEntry_Object = MibTableRow
speedMux200gClientPortXCVAlarmEntry = _SpeedMux200gClientPortXCVAlarmEntry_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 4, 1, 12, 1)
)
speedMux200gClientPortXCVAlarmEntry.setIndexNames(
    (0, "SPEED-MUX-200G-MIB", "speedMux200gClientPortXCVDAlarmIndex"),
)
if mibBuilder.loadTexts:
    speedMux200gClientPortXCVAlarmEntry.setStatus("current")


class _SpeedMux200gClientPortXCVDAlarmIndex_Type(Integer32):
    """Custom type speedMux200gClientPortXCVDAlarmIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1900),
    )


_SpeedMux200gClientPortXCVDAlarmIndex_Type.__name__ = "Integer32"
_SpeedMux200gClientPortXCVDAlarmIndex_Object = MibTableColumn
speedMux200gClientPortXCVDAlarmIndex = _SpeedMux200gClientPortXCVDAlarmIndex_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 4, 1, 12, 1, 1),
    _SpeedMux200gClientPortXCVDAlarmIndex_Type()
)
speedMux200gClientPortXCVDAlarmIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    speedMux200gClientPortXCVDAlarmIndex.setStatus("current")
_SpeedMux200gClientPortXCVAlarmSlot_Type = Integer32
_SpeedMux200gClientPortXCVAlarmSlot_Object = MibTableColumn
speedMux200gClientPortXCVAlarmSlot = _SpeedMux200gClientPortXCVAlarmSlot_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 4, 1, 12, 1, 2),
    _SpeedMux200gClientPortXCVAlarmSlot_Type()
)
speedMux200gClientPortXCVAlarmSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    speedMux200gClientPortXCVAlarmSlot.setStatus("current")
_SpeedMux200gClientPortXCVAlarmPort_Type = Integer32
_SpeedMux200gClientPortXCVAlarmPort_Object = MibTableColumn
speedMux200gClientPortXCVAlarmPort = _SpeedMux200gClientPortXCVAlarmPort_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 4, 1, 12, 1, 3),
    _SpeedMux200gClientPortXCVAlarmPort_Type()
)
speedMux200gClientPortXCVAlarmPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    speedMux200gClientPortXCVAlarmPort.setStatus("current")


class _SpeedMux200gClientPortXCVRxAlarmLane1_Type(Integer32):
    """Custom type speedMux200gClientPortXCVRxAlarmLane1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              4,
              5,
              6,
              7,
              255)
        )
    )
    namedValues = NamedValues(
        *(("notAvailable", 0),
          ("noAlarm", 1),
          ("lowWarning", 4),
          ("lowAlarm", 5),
          ("highWarning", 6),
          ("highAlarm", 7),
          ("unknownAlarm", 255))
    )


_SpeedMux200gClientPortXCVRxAlarmLane1_Type.__name__ = "Integer32"
_SpeedMux200gClientPortXCVRxAlarmLane1_Object = MibTableColumn
speedMux200gClientPortXCVRxAlarmLane1 = _SpeedMux200gClientPortXCVRxAlarmLane1_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 4, 1, 12, 1, 4),
    _SpeedMux200gClientPortXCVRxAlarmLane1_Type()
)
speedMux200gClientPortXCVRxAlarmLane1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    speedMux200gClientPortXCVRxAlarmLane1.setStatus("current")


class _SpeedMux200gClientPortXCVRxAlarmLane2_Type(Integer32):
    """Custom type speedMux200gClientPortXCVRxAlarmLane2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              4,
              5,
              6,
              7,
              255)
        )
    )
    namedValues = NamedValues(
        *(("notAvailable", 0),
          ("noAlarm", 1),
          ("lowWarning", 4),
          ("lowAlarm", 5),
          ("highWarning", 6),
          ("highAlarm", 7),
          ("unknownAlarm", 255))
    )


_SpeedMux200gClientPortXCVRxAlarmLane2_Type.__name__ = "Integer32"
_SpeedMux200gClientPortXCVRxAlarmLane2_Object = MibTableColumn
speedMux200gClientPortXCVRxAlarmLane2 = _SpeedMux200gClientPortXCVRxAlarmLane2_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 4, 1, 12, 1, 5),
    _SpeedMux200gClientPortXCVRxAlarmLane2_Type()
)
speedMux200gClientPortXCVRxAlarmLane2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    speedMux200gClientPortXCVRxAlarmLane2.setStatus("current")


class _SpeedMux200gClientPortXCVRxAlarmLane3_Type(Integer32):
    """Custom type speedMux200gClientPortXCVRxAlarmLane3 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              4,
              5,
              6,
              7,
              255)
        )
    )
    namedValues = NamedValues(
        *(("notAvailable", 0),
          ("noAlarm", 1),
          ("lowWarning", 4),
          ("lowAlarm", 5),
          ("highWarning", 6),
          ("highAlarm", 7),
          ("unknownAlarm", 255))
    )


_SpeedMux200gClientPortXCVRxAlarmLane3_Type.__name__ = "Integer32"
_SpeedMux200gClientPortXCVRxAlarmLane3_Object = MibTableColumn
speedMux200gClientPortXCVRxAlarmLane3 = _SpeedMux200gClientPortXCVRxAlarmLane3_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 4, 1, 12, 1, 6),
    _SpeedMux200gClientPortXCVRxAlarmLane3_Type()
)
speedMux200gClientPortXCVRxAlarmLane3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    speedMux200gClientPortXCVRxAlarmLane3.setStatus("current")


class _SpeedMux200gClientPortXCVRxAlarmLane4_Type(Integer32):
    """Custom type speedMux200gClientPortXCVRxAlarmLane4 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              4,
              5,
              6,
              7,
              255)
        )
    )
    namedValues = NamedValues(
        *(("notAvailable", 0),
          ("noAlarm", 1),
          ("lowWarning", 4),
          ("lowAlarm", 5),
          ("highWarning", 6),
          ("highAlarm", 7),
          ("unknownAlarm", 255))
    )


_SpeedMux200gClientPortXCVRxAlarmLane4_Type.__name__ = "Integer32"
_SpeedMux200gClientPortXCVRxAlarmLane4_Object = MibTableColumn
speedMux200gClientPortXCVRxAlarmLane4 = _SpeedMux200gClientPortXCVRxAlarmLane4_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 4, 1, 12, 1, 7),
    _SpeedMux200gClientPortXCVRxAlarmLane4_Type()
)
speedMux200gClientPortXCVRxAlarmLane4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    speedMux200gClientPortXCVRxAlarmLane4.setStatus("current")


class _SpeedMux200gClientPortXCVTxAlarmLane1_Type(Integer32):
    """Custom type speedMux200gClientPortXCVTxAlarmLane1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              3)
        )
    )
    namedValues = NamedValues(
        *(("notAvailable", 0),
          ("noAlarm", 1),
          ("activeAlarm", 3))
    )


_SpeedMux200gClientPortXCVTxAlarmLane1_Type.__name__ = "Integer32"
_SpeedMux200gClientPortXCVTxAlarmLane1_Object = MibTableColumn
speedMux200gClientPortXCVTxAlarmLane1 = _SpeedMux200gClientPortXCVTxAlarmLane1_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 4, 1, 12, 1, 8),
    _SpeedMux200gClientPortXCVTxAlarmLane1_Type()
)
speedMux200gClientPortXCVTxAlarmLane1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    speedMux200gClientPortXCVTxAlarmLane1.setStatus("current")


class _SpeedMux200gClientPortXCVTxAlarmLane2_Type(Integer32):
    """Custom type speedMux200gClientPortXCVTxAlarmLane2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              3)
        )
    )
    namedValues = NamedValues(
        *(("notAvailable", 0),
          ("noAlarm", 1),
          ("activeAlarm", 3))
    )


_SpeedMux200gClientPortXCVTxAlarmLane2_Type.__name__ = "Integer32"
_SpeedMux200gClientPortXCVTxAlarmLane2_Object = MibTableColumn
speedMux200gClientPortXCVTxAlarmLane2 = _SpeedMux200gClientPortXCVTxAlarmLane2_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 4, 1, 12, 1, 9),
    _SpeedMux200gClientPortXCVTxAlarmLane2_Type()
)
speedMux200gClientPortXCVTxAlarmLane2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    speedMux200gClientPortXCVTxAlarmLane2.setStatus("current")


class _SpeedMux200gClientPortXCVTxAlarmLane3_Type(Integer32):
    """Custom type speedMux200gClientPortXCVTxAlarmLane3 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              3)
        )
    )
    namedValues = NamedValues(
        *(("notAvailable", 0),
          ("noAlarm", 1),
          ("activeAlarm", 3))
    )


_SpeedMux200gClientPortXCVTxAlarmLane3_Type.__name__ = "Integer32"
_SpeedMux200gClientPortXCVTxAlarmLane3_Object = MibTableColumn
speedMux200gClientPortXCVTxAlarmLane3 = _SpeedMux200gClientPortXCVTxAlarmLane3_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 4, 1, 12, 1, 10),
    _SpeedMux200gClientPortXCVTxAlarmLane3_Type()
)
speedMux200gClientPortXCVTxAlarmLane3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    speedMux200gClientPortXCVTxAlarmLane3.setStatus("current")


class _SpeedMux200gClientPortXCVTxAlarmLane4_Type(Integer32):
    """Custom type speedMux200gClientPortXCVTxAlarmLane4 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              3)
        )
    )
    namedValues = NamedValues(
        *(("notAvailable", 0),
          ("noAlarm", 1),
          ("activeAlarm", 3))
    )


_SpeedMux200gClientPortXCVTxAlarmLane4_Type.__name__ = "Integer32"
_SpeedMux200gClientPortXCVTxAlarmLane4_Object = MibTableColumn
speedMux200gClientPortXCVTxAlarmLane4 = _SpeedMux200gClientPortXCVTxAlarmLane4_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 4, 1, 12, 1, 11),
    _SpeedMux200gClientPortXCVTxAlarmLane4_Type()
)
speedMux200gClientPortXCVTxAlarmLane4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    speedMux200gClientPortXCVTxAlarmLane4.setStatus("current")


class _SpeedMux200gClientPortXCVTxBiasAlarmLane1_Type(Integer32):
    """Custom type speedMux200gClientPortXCVTxBiasAlarmLane1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              3)
        )
    )
    namedValues = NamedValues(
        *(("notAvailable", 0),
          ("noAlarm", 1),
          ("activeAlarm", 3))
    )


_SpeedMux200gClientPortXCVTxBiasAlarmLane1_Type.__name__ = "Integer32"
_SpeedMux200gClientPortXCVTxBiasAlarmLane1_Object = MibTableColumn
speedMux200gClientPortXCVTxBiasAlarmLane1 = _SpeedMux200gClientPortXCVTxBiasAlarmLane1_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 4, 1, 12, 1, 12),
    _SpeedMux200gClientPortXCVTxBiasAlarmLane1_Type()
)
speedMux200gClientPortXCVTxBiasAlarmLane1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    speedMux200gClientPortXCVTxBiasAlarmLane1.setStatus("current")


class _SpeedMux200gClientPortXCVTxBiasAlarmLane2_Type(Integer32):
    """Custom type speedMux200gClientPortXCVTxBiasAlarmLane2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              3)
        )
    )
    namedValues = NamedValues(
        *(("notAvailable", 0),
          ("noAlarm", 1),
          ("activeAlarm", 3))
    )


_SpeedMux200gClientPortXCVTxBiasAlarmLane2_Type.__name__ = "Integer32"
_SpeedMux200gClientPortXCVTxBiasAlarmLane2_Object = MibTableColumn
speedMux200gClientPortXCVTxBiasAlarmLane2 = _SpeedMux200gClientPortXCVTxBiasAlarmLane2_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 4, 1, 12, 1, 13),
    _SpeedMux200gClientPortXCVTxBiasAlarmLane2_Type()
)
speedMux200gClientPortXCVTxBiasAlarmLane2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    speedMux200gClientPortXCVTxBiasAlarmLane2.setStatus("current")


class _SpeedMux200gClientPortXCVTxBiasAlarmLane3_Type(Integer32):
    """Custom type speedMux200gClientPortXCVTxBiasAlarmLane3 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              3)
        )
    )
    namedValues = NamedValues(
        *(("notAvailable", 0),
          ("noAlarm", 1),
          ("activeAlarm", 3))
    )


_SpeedMux200gClientPortXCVTxBiasAlarmLane3_Type.__name__ = "Integer32"
_SpeedMux200gClientPortXCVTxBiasAlarmLane3_Object = MibTableColumn
speedMux200gClientPortXCVTxBiasAlarmLane3 = _SpeedMux200gClientPortXCVTxBiasAlarmLane3_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 4, 1, 12, 1, 14),
    _SpeedMux200gClientPortXCVTxBiasAlarmLane3_Type()
)
speedMux200gClientPortXCVTxBiasAlarmLane3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    speedMux200gClientPortXCVTxBiasAlarmLane3.setStatus("current")


class _SpeedMux200gClientPortXCVTxBiasAlarmLane4_Type(Integer32):
    """Custom type speedMux200gClientPortXCVTxBiasAlarmLane4 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              3)
        )
    )
    namedValues = NamedValues(
        *(("notAvailable", 0),
          ("noAlarm", 1),
          ("activeAlarm", 3))
    )


_SpeedMux200gClientPortXCVTxBiasAlarmLane4_Type.__name__ = "Integer32"
_SpeedMux200gClientPortXCVTxBiasAlarmLane4_Object = MibTableColumn
speedMux200gClientPortXCVTxBiasAlarmLane4 = _SpeedMux200gClientPortXCVTxBiasAlarmLane4_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 4, 1, 12, 1, 15),
    _SpeedMux200gClientPortXCVTxBiasAlarmLane4_Type()
)
speedMux200gClientPortXCVTxBiasAlarmLane4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    speedMux200gClientPortXCVTxBiasAlarmLane4.setStatus("current")


class _SpeedMux200gClientPortXCVCDRAlarmLane1_Type(Integer32):
    """Custom type speedMux200gClientPortXCVCDRAlarmLane1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              3)
        )
    )
    namedValues = NamedValues(
        *(("notAvailable", 0),
          ("noAlarm", 1),
          ("activeAlarm", 3))
    )


_SpeedMux200gClientPortXCVCDRAlarmLane1_Type.__name__ = "Integer32"
_SpeedMux200gClientPortXCVCDRAlarmLane1_Object = MibTableColumn
speedMux200gClientPortXCVCDRAlarmLane1 = _SpeedMux200gClientPortXCVCDRAlarmLane1_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 4, 1, 12, 1, 16),
    _SpeedMux200gClientPortXCVCDRAlarmLane1_Type()
)
speedMux200gClientPortXCVCDRAlarmLane1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    speedMux200gClientPortXCVCDRAlarmLane1.setStatus("current")


class _SpeedMux200gClientPortXCVCDRAlarmLane2_Type(Integer32):
    """Custom type speedMux200gClientPortXCVCDRAlarmLane2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              3)
        )
    )
    namedValues = NamedValues(
        *(("notAvailable", 0),
          ("noAlarm", 1),
          ("activeAlarm", 3))
    )


_SpeedMux200gClientPortXCVCDRAlarmLane2_Type.__name__ = "Integer32"
_SpeedMux200gClientPortXCVCDRAlarmLane2_Object = MibTableColumn
speedMux200gClientPortXCVCDRAlarmLane2 = _SpeedMux200gClientPortXCVCDRAlarmLane2_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 4, 1, 12, 1, 17),
    _SpeedMux200gClientPortXCVCDRAlarmLane2_Type()
)
speedMux200gClientPortXCVCDRAlarmLane2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    speedMux200gClientPortXCVCDRAlarmLane2.setStatus("current")


class _SpeedMux200gClientPortXCVCDRAlarmLane3_Type(Integer32):
    """Custom type speedMux200gClientPortXCVCDRAlarmLane3 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              3)
        )
    )
    namedValues = NamedValues(
        *(("notAvailable", 0),
          ("noAlarm", 1),
          ("activeAlarm", 3))
    )


_SpeedMux200gClientPortXCVCDRAlarmLane3_Type.__name__ = "Integer32"
_SpeedMux200gClientPortXCVCDRAlarmLane3_Object = MibTableColumn
speedMux200gClientPortXCVCDRAlarmLane3 = _SpeedMux200gClientPortXCVCDRAlarmLane3_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 4, 1, 12, 1, 18),
    _SpeedMux200gClientPortXCVCDRAlarmLane3_Type()
)
speedMux200gClientPortXCVCDRAlarmLane3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    speedMux200gClientPortXCVCDRAlarmLane3.setStatus("current")


class _SpeedMux200gClientPortXCVCDRAlarmLane4_Type(Integer32):
    """Custom type speedMux200gClientPortXCVCDRAlarmLane4 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              3)
        )
    )
    namedValues = NamedValues(
        *(("notAvailable", 0),
          ("noAlarm", 1),
          ("activeAlarm", 3))
    )


_SpeedMux200gClientPortXCVCDRAlarmLane4_Type.__name__ = "Integer32"
_SpeedMux200gClientPortXCVCDRAlarmLane4_Object = MibTableColumn
speedMux200gClientPortXCVCDRAlarmLane4 = _SpeedMux200gClientPortXCVCDRAlarmLane4_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 4, 1, 12, 1, 19),
    _SpeedMux200gClientPortXCVCDRAlarmLane4_Type()
)
speedMux200gClientPortXCVCDRAlarmLane4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    speedMux200gClientPortXCVCDRAlarmLane4.setStatus("current")


class _SpeedMux200gClientPortXCVVCCAlarm_Type(Integer32):
    """Custom type speedMux200gClientPortXCVVCCAlarm based on Integer32"""
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
          ("noAlarm", 1),
          ("activeWarning", 2),
          ("activeAlarm", 3),
          ("unknownAlarm", 255))
    )


_SpeedMux200gClientPortXCVVCCAlarm_Type.__name__ = "Integer32"
_SpeedMux200gClientPortXCVVCCAlarm_Object = MibTableColumn
speedMux200gClientPortXCVVCCAlarm = _SpeedMux200gClientPortXCVVCCAlarm_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 4, 1, 12, 1, 20),
    _SpeedMux200gClientPortXCVVCCAlarm_Type()
)
speedMux200gClientPortXCVVCCAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    speedMux200gClientPortXCVVCCAlarm.setStatus("current")


class _SpeedMux200gClientPortXCVTempAlarm_Type(Integer32):
    """Custom type speedMux200gClientPortXCVTempAlarm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              6,
              7,
              255)
        )
    )
    namedValues = NamedValues(
        *(("notAvailable", 0),
          ("noAlarm", 1),
          ("highWarning", 6),
          ("highAlarm", 7),
          ("unknownAlarm", 255))
    )


_SpeedMux200gClientPortXCVTempAlarm_Type.__name__ = "Integer32"
_SpeedMux200gClientPortXCVTempAlarm_Object = MibTableColumn
speedMux200gClientPortXCVTempAlarm = _SpeedMux200gClientPortXCVTempAlarm_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 4, 1, 12, 1, 21),
    _SpeedMux200gClientPortXCVTempAlarm_Type()
)
speedMux200gClientPortXCVTempAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    speedMux200gClientPortXCVTempAlarm.setStatus("current")
_SpeedMux200gLinePortAlarmTable_Object = MibTable
speedMux200gLinePortAlarmTable = _SpeedMux200gLinePortAlarmTable_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 4, 1, 13)
)
if mibBuilder.loadTexts:
    speedMux200gLinePortAlarmTable.setStatus("current")
_SpeedMux200gLinePortAlarmEntry_Object = MibTableRow
speedMux200gLinePortAlarmEntry = _SpeedMux200gLinePortAlarmEntry_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 4, 1, 13, 1)
)
speedMux200gLinePortAlarmEntry.setIndexNames(
    (0, "SPEED-MUX-200G-MIB", "speedMux200gLinePortAlarmIndex"),
)
if mibBuilder.loadTexts:
    speedMux200gLinePortAlarmEntry.setStatus("current")


class _SpeedMux200gLinePortAlarmIndex_Type(Integer32):
    """Custom type speedMux200gLinePortAlarmIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1900),
    )


_SpeedMux200gLinePortAlarmIndex_Type.__name__ = "Integer32"
_SpeedMux200gLinePortAlarmIndex_Object = MibTableColumn
speedMux200gLinePortAlarmIndex = _SpeedMux200gLinePortAlarmIndex_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 4, 1, 13, 1, 1),
    _SpeedMux200gLinePortAlarmIndex_Type()
)
speedMux200gLinePortAlarmIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    speedMux200gLinePortAlarmIndex.setStatus("current")
_SpeedMux200gLinePortAlarmSlot_Type = Integer32
_SpeedMux200gLinePortAlarmSlot_Object = MibTableColumn
speedMux200gLinePortAlarmSlot = _SpeedMux200gLinePortAlarmSlot_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 4, 1, 13, 1, 2),
    _SpeedMux200gLinePortAlarmSlot_Type()
)
speedMux200gLinePortAlarmSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    speedMux200gLinePortAlarmSlot.setStatus("current")
_SpeedMux200gLinePortAlarmPort_Type = Integer32
_SpeedMux200gLinePortAlarmPort_Object = MibTableColumn
speedMux200gLinePortAlarmPort = _SpeedMux200gLinePortAlarmPort_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 4, 1, 13, 1, 3),
    _SpeedMux200gLinePortAlarmPort_Type()
)
speedMux200gLinePortAlarmPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    speedMux200gLinePortAlarmPort.setStatus("current")


class _SpeedMux200gLinePortXCVRxAlarm_Type(Integer32):
    """Custom type speedMux200gLinePortXCVRxAlarm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              4,
              5,
              6,
              7,
              255)
        )
    )
    namedValues = NamedValues(
        *(("notAvailable", 0),
          ("noAlarm", 1),
          ("lowWarning", 4),
          ("lowAlarm", 5),
          ("highWarning", 6),
          ("highAlarm", 7),
          ("unknownAlarm", 255))
    )


_SpeedMux200gLinePortXCVRxAlarm_Type.__name__ = "Integer32"
_SpeedMux200gLinePortXCVRxAlarm_Object = MibTableColumn
speedMux200gLinePortXCVRxAlarm = _SpeedMux200gLinePortXCVRxAlarm_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 4, 1, 13, 1, 4),
    _SpeedMux200gLinePortXCVRxAlarm_Type()
)
speedMux200gLinePortXCVRxAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    speedMux200gLinePortXCVRxAlarm.setStatus("current")


class _SpeedMux200gLinePortXCVTxAlarm_Type(Integer32):
    """Custom type speedMux200gLinePortXCVTxAlarm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              3)
        )
    )
    namedValues = NamedValues(
        *(("notAvailable", 0),
          ("noAlarm", 1),
          ("activeAlarm", 3))
    )


_SpeedMux200gLinePortXCVTxAlarm_Type.__name__ = "Integer32"
_SpeedMux200gLinePortXCVTxAlarm_Object = MibTableColumn
speedMux200gLinePortXCVTxAlarm = _SpeedMux200gLinePortXCVTxAlarm_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 4, 1, 13, 1, 5),
    _SpeedMux200gLinePortXCVTxAlarm_Type()
)
speedMux200gLinePortXCVTxAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    speedMux200gLinePortXCVTxAlarm.setStatus("current")


class _SpeedMux200gLinePortXCVTxBiasAlarm_Type(Integer32):
    """Custom type speedMux200gLinePortXCVTxBiasAlarm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              3)
        )
    )
    namedValues = NamedValues(
        *(("notAvailable", 0),
          ("noAlarm", 1),
          ("activeAlarm", 3))
    )


_SpeedMux200gLinePortXCVTxBiasAlarm_Type.__name__ = "Integer32"
_SpeedMux200gLinePortXCVTxBiasAlarm_Object = MibTableColumn
speedMux200gLinePortXCVTxBiasAlarm = _SpeedMux200gLinePortXCVTxBiasAlarm_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 4, 1, 13, 1, 6),
    _SpeedMux200gLinePortXCVTxBiasAlarm_Type()
)
speedMux200gLinePortXCVTxBiasAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    speedMux200gLinePortXCVTxBiasAlarm.setStatus("current")


class _SpeedMux200gLinePortXCVTempAlarm_Type(Integer32):
    """Custom type speedMux200gLinePortXCVTempAlarm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              6,
              7,
              255)
        )
    )
    namedValues = NamedValues(
        *(("notAvailable", 0),
          ("noAlarm", 1),
          ("highWarning", 6),
          ("highAlarm", 7),
          ("unknownAlarm", 255))
    )


_SpeedMux200gLinePortXCVTempAlarm_Type.__name__ = "Integer32"
_SpeedMux200gLinePortXCVTempAlarm_Object = MibTableColumn
speedMux200gLinePortXCVTempAlarm = _SpeedMux200gLinePortXCVTempAlarm_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 4, 1, 13, 1, 7),
    _SpeedMux200gLinePortXCVTempAlarm_Type()
)
speedMux200gLinePortXCVTempAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    speedMux200gLinePortXCVTempAlarm.setStatus("current")


class _SpeedMux200gLinePortEncryptionAlarm_Type(Integer32):
    """Custom type speedMux200gLinePortEncryptionAlarm based on Integer32"""
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
          ("noAlarm", 1),
          ("activeWarning", 2),
          ("activeAlarm", 3),
          ("unknownAlarm", 255))
    )


_SpeedMux200gLinePortEncryptionAlarm_Type.__name__ = "Integer32"
_SpeedMux200gLinePortEncryptionAlarm_Object = MibTableColumn
speedMux200gLinePortEncryptionAlarm = _SpeedMux200gLinePortEncryptionAlarm_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 4, 1, 13, 1, 8),
    _SpeedMux200gLinePortEncryptionAlarm_Type()
)
speedMux200gLinePortEncryptionAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    speedMux200gLinePortEncryptionAlarm.setStatus("current")
_SpeedMux200gProfileTable_Object = MibTable
speedMux200gProfileTable = _SpeedMux200gProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 4, 1, 14)
)
if mibBuilder.loadTexts:
    speedMux200gProfileTable.setStatus("current")
_SpeedMux200gProfileEntry_Object = MibTableRow
speedMux200gProfileEntry = _SpeedMux200gProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 4, 1, 14, 1)
)
speedMux200gProfileEntry.setIndexNames(
    (0, "SPEED-MUX-200G-MIB", "speedMux200gProfileIndex"),
)
if mibBuilder.loadTexts:
    speedMux200gProfileEntry.setStatus("current")


class _SpeedMux200gProfileIndex_Type(Integer32):
    """Custom type speedMux200gProfileIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1962024),
    )


_SpeedMux200gProfileIndex_Type.__name__ = "Integer32"
_SpeedMux200gProfileIndex_Object = MibTableColumn
speedMux200gProfileIndex = _SpeedMux200gProfileIndex_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 4, 1, 14, 1, 1),
    _SpeedMux200gProfileIndex_Type()
)
speedMux200gProfileIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    speedMux200gProfileIndex.setStatus("current")
_SpeedMux200gProfileSlot_Type = Integer32
_SpeedMux200gProfileSlot_Object = MibTableColumn
speedMux200gProfileSlot = _SpeedMux200gProfileSlot_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 4, 1, 14, 1, 2),
    _SpeedMux200gProfileSlot_Type()
)
speedMux200gProfileSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    speedMux200gProfileSlot.setStatus("current")
_SpeedMux200gProfileNumber_Type = Integer32
_SpeedMux200gProfileNumber_Object = MibTableColumn
speedMux200gProfileNumber = _SpeedMux200gProfileNumber_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 4, 1, 14, 1, 3),
    _SpeedMux200gProfileNumber_Type()
)
speedMux200gProfileNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    speedMux200gProfileNumber.setStatus("current")


class _SpeedMux200gProfileIsEditable_Type(Integer32):
    """Custom type speedMux200gProfileIsEditable based on Integer32"""
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
          ("true", 1),
          ("false", 2),
          ("unknown", 255))
    )


_SpeedMux200gProfileIsEditable_Type.__name__ = "Integer32"
_SpeedMux200gProfileIsEditable_Object = MibTableColumn
speedMux200gProfileIsEditable = _SpeedMux200gProfileIsEditable_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 4, 1, 14, 1, 4),
    _SpeedMux200gProfileIsEditable_Type()
)
speedMux200gProfileIsEditable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    speedMux200gProfileIsEditable.setStatus("current")


class _SpeedMux200gProfileDescription_Type(DisplayString):
    """Custom type speedMux200gProfileDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_SpeedMux200gProfileDescription_Type.__name__ = "DisplayString"
_SpeedMux200gProfileDescription_Object = MibTableColumn
speedMux200gProfileDescription = _SpeedMux200gProfileDescription_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 4, 1, 14, 1, 5),
    _SpeedMux200gProfileDescription_Type()
)
speedMux200gProfileDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    speedMux200gProfileDescription.setStatus("current")


class _SpeedMux200gProfilePort_Type(Integer32):
    """Custom type speedMux200gProfilePort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              21,
              22,
              23,
              24,
              25,
              26,
              27,
              28,
              29,
              30,
              31,
              32,
              33,
              34,
              35,
              36,
              37,
              38,
              39,
              40,
              41,
              42,
              43,
              44)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("line1", 1),
          ("line2", 2),
          ("qsfp11", 21),
          ("qsfp12", 22),
          ("qsfp13", 23),
          ("qsfp14", 24),
          ("qsfp21", 25),
          ("qsfp22", 26),
          ("qsfp23", 27),
          ("qsfp24", 28),
          ("qsfp31", 29),
          ("qsfp32", 30),
          ("qsfp33", 31),
          ("qsfp34", 32),
          ("qsfp41", 33),
          ("qsfp42", 34),
          ("qsfp43", 35),
          ("qsfp44", 36),
          ("qsfp51", 37),
          ("qsfp52", 38),
          ("qsfp53", 39),
          ("qsfp54", 40),
          ("qsfp61", 41),
          ("qsfp62", 42),
          ("qsfp63", 43),
          ("qsfp64", 44))
    )


_SpeedMux200gProfilePort_Type.__name__ = "Integer32"
_SpeedMux200gProfilePort_Object = MibTableColumn
speedMux200gProfilePort = _SpeedMux200gProfilePort_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 4, 1, 14, 1, 7),
    _SpeedMux200gProfilePort_Type()
)
speedMux200gProfilePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    speedMux200gProfilePort.setStatus("current")


class _SpeedMux200gProfilePortMapToLine_Type(Integer32):
    """Custom type speedMux200gProfilePortMapToLine based on Integer32"""
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
        *(("nonapplicable", 0),
          ("toLine1", 1),
          ("toLine2", 2),
          ("none", 254),
          ("unknown", 255))
    )


_SpeedMux200gProfilePortMapToLine_Type.__name__ = "Integer32"
_SpeedMux200gProfilePortMapToLine_Object = MibTableColumn
speedMux200gProfilePortMapToLine = _SpeedMux200gProfilePortMapToLine_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 4, 1, 14, 1, 8),
    _SpeedMux200gProfilePortMapToLine_Type()
)
speedMux200gProfilePortMapToLine.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    speedMux200gProfilePortMapToLine.setStatus("current")


class _SpeedMux200gProfilePortProtocol_Type(Integer32):
    """Custom type speedMux200gProfilePortProtocol based on Integer32"""
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
              18)
        )
    )
    namedValues = NamedValues(
        *(("nonapplicable", 0),
          ("bundled", 1),
          ("eth40G", 2),
          ("fc32G", 3),
          ("fc16G", 4),
          ("fc8G", 5),
          ("fc10G", 6),
          ("eth10G", 7),
          ("cpri7", 8),
          ("cpri6", 9),
          ("cpri5", 10),
          ("ibqdr", 11),
          ("ibddr", 12),
          ("otu2", 13),
          ("otu3", 14),
          ("otu4", 15),
          ("eth100GCBR", 16),
          ("eth100GMAC", 17),
          ("eth1G", 18))
    )


_SpeedMux200gProfilePortProtocol_Type.__name__ = "Integer32"
_SpeedMux200gProfilePortProtocol_Object = MibTableColumn
speedMux200gProfilePortProtocol = _SpeedMux200gProfilePortProtocol_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 4, 1, 14, 1, 9),
    _SpeedMux200gProfilePortProtocol_Type()
)
speedMux200gProfilePortProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    speedMux200gProfilePortProtocol.setStatus("current")


class _SpeedMux200gProfileProtecionConfig_Type(Integer32):
    """Custom type speedMux200gProfileProtecionConfig based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("nonapplicable", 0),
          ("disabled", 1),
          ("enabled", 2))
    )


_SpeedMux200gProfileProtecionConfig_Type.__name__ = "Integer32"
_SpeedMux200gProfileProtecionConfig_Object = MibTableColumn
speedMux200gProfileProtecionConfig = _SpeedMux200gProfileProtecionConfig_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 4, 1, 14, 1, 10),
    _SpeedMux200gProfileProtecionConfig_Type()
)
speedMux200gProfileProtecionConfig.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    speedMux200gProfileProtecionConfig.setStatus("current")
_SpeedMux200gMLineProtectionTable_Object = MibTable
speedMux200gMLineProtectionTable = _SpeedMux200gMLineProtectionTable_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 4, 1, 15)
)
if mibBuilder.loadTexts:
    speedMux200gMLineProtectionTable.setStatus("current")
_SpeedMux200gMLineProtectionEntry_Object = MibTableRow
speedMux200gMLineProtectionEntry = _SpeedMux200gMLineProtectionEntry_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 4, 1, 15, 1)
)
speedMux200gMLineProtectionEntry.setIndexNames(
    (0, "SPEED-MUX-200G-MIB", "speedMux200gMProtectionIndex"),
)
if mibBuilder.loadTexts:
    speedMux200gMLineProtectionEntry.setStatus("current")


class _SpeedMux200gMProtectionIndex_Type(Integer32):
    """Custom type speedMux200gMProtectionIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_SpeedMux200gMProtectionIndex_Type.__name__ = "Integer32"
_SpeedMux200gMProtectionIndex_Object = MibTableColumn
speedMux200gMProtectionIndex = _SpeedMux200gMProtectionIndex_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 4, 1, 15, 1, 1),
    _SpeedMux200gMProtectionIndex_Type()
)
speedMux200gMProtectionIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    speedMux200gMProtectionIndex.setStatus("current")
_SpeedMux200gMProtectionSlot_Type = Integer32
_SpeedMux200gMProtectionSlot_Object = MibTableColumn
speedMux200gMProtectionSlot = _SpeedMux200gMProtectionSlot_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 4, 1, 15, 1, 2),
    _SpeedMux200gMProtectionSlot_Type()
)
speedMux200gMProtectionSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    speedMux200gMProtectionSlot.setStatus("current")


class _SpeedMux200gMProtectionMode_Type(Integer32):
    """Custom type speedMux200gMProtectionMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("notavailable", 0),
          ("fallbackLine1", 1),
          ("fallbackLine2", 2),
          ("staticLine1", 3),
          ("staticLine2", 4))
    )


_SpeedMux200gMProtectionMode_Type.__name__ = "Integer32"
_SpeedMux200gMProtectionMode_Object = MibTableColumn
speedMux200gMProtectionMode = _SpeedMux200gMProtectionMode_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 4, 1, 15, 1, 3),
    _SpeedMux200gMProtectionMode_Type()
)
speedMux200gMProtectionMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    speedMux200gMProtectionMode.setStatus("current")


class _SpeedMux200gMProtectionFallbackConfig_Type(Integer32):
    """Custom type speedMux200gMProtectionFallbackConfig based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 3600),
    )


_SpeedMux200gMProtectionFallbackConfig_Type.__name__ = "Integer32"
_SpeedMux200gMProtectionFallbackConfig_Object = MibTableColumn
speedMux200gMProtectionFallbackConfig = _SpeedMux200gMProtectionFallbackConfig_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 4, 1, 15, 1, 4),
    _SpeedMux200gMProtectionFallbackConfig_Type()
)
speedMux200gMProtectionFallbackConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    speedMux200gMProtectionFallbackConfig.setStatus("current")


class _SpeedMux200gMProtectionStatus_Type(Integer32):
    """Custom type speedMux200gMProtectionStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("notavailable", 0),
          ("init", 1),
          ("synchronizing", 2),
          ("line1Active", 3),
          ("line2Active", 4),
          ("off", 5))
    )


_SpeedMux200gMProtectionStatus_Type.__name__ = "Integer32"
_SpeedMux200gMProtectionStatus_Object = MibTableColumn
speedMux200gMProtectionStatus = _SpeedMux200gMProtectionStatus_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 4, 1, 15, 1, 5),
    _SpeedMux200gMProtectionStatus_Type()
)
speedMux200gMProtectionStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    speedMux200gMProtectionStatus.setStatus("current")


class _SpeedMux200gMProtectionMainPath_Type(Integer32):
    """Custom type speedMux200gMProtectionMainPath based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("notavailable", 0),
          ("line1", 1),
          ("line2", 2),
          ("init", 3),
          ("fallback", 4))
    )


_SpeedMux200gMProtectionMainPath_Type.__name__ = "Integer32"
_SpeedMux200gMProtectionMainPath_Object = MibTableColumn
speedMux200gMProtectionMainPath = _SpeedMux200gMProtectionMainPath_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 4, 1, 15, 1, 6),
    _SpeedMux200gMProtectionMainPath_Type()
)
speedMux200gMProtectionMainPath.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    speedMux200gMProtectionMainPath.setStatus("current")


class _SpeedMux200gMProtectionBackupPath_Type(Integer32):
    """Custom type speedMux200gMProtectionBackupPath based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("notavailable", 0),
          ("line1", 1),
          ("line2", 2),
          ("init", 3),
          ("fallback", 4))
    )


_SpeedMux200gMProtectionBackupPath_Type.__name__ = "Integer32"
_SpeedMux200gMProtectionBackupPath_Object = MibTableColumn
speedMux200gMProtectionBackupPath = _SpeedMux200gMProtectionBackupPath_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 4, 1, 15, 1, 7),
    _SpeedMux200gMProtectionBackupPath_Type()
)
speedMux200gMProtectionBackupPath.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    speedMux200gMProtectionBackupPath.setStatus("current")


class _SpeedMux200gMProtectionFallbackTime_Type(Integer32):
    """Custom type speedMux200gMProtectionFallbackTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3600),
    )


_SpeedMux200gMProtectionFallbackTime_Type.__name__ = "Integer32"
_SpeedMux200gMProtectionFallbackTime_Object = MibTableColumn
speedMux200gMProtectionFallbackTime = _SpeedMux200gMProtectionFallbackTime_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 4, 1, 15, 1, 8),
    _SpeedMux200gMProtectionFallbackTime_Type()
)
speedMux200gMProtectionFallbackTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    speedMux200gMProtectionFallbackTime.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SPEED-MUX-200G-MIB",
    **{"speedMux200g": speedMux200g,
       "speedMux200gMOverviewTable": speedMux200gMOverviewTable,
       "speedMux200gMOverviewEntry": speedMux200gMOverviewEntry,
       "speedMux200gMOverviewIndex": speedMux200gMOverviewIndex,
       "speedMux200gMSlot": speedMux200gMSlot,
       "speedMux200gMDevice": speedMux200gMDevice,
       "speedMux200gMState": speedMux200gMState,
       "speedMux200gMSysName": speedMux200gMSysName,
       "speedMux200gMSysUpTime": speedMux200gMSysUpTime,
       "speedMux200gMTemperature": speedMux200gMTemperature,
       "speedMux200gMAlarmState": speedMux200gMAlarmState,
       "speedMux200gMKernelImage": speedMux200gMKernelImage,
       "speedMux200gMAppImage": speedMux200gMAppImage,
       "speedMux200gMHwVersion": speedMux200gMHwVersion,
       "speedMux200gMDevSerialNumber": speedMux200gMDevSerialNumber,
       "speedMux200gMTemperatureAlarm": speedMux200gMTemperatureAlarm,
       "speedMux200gMOTNAlarm": speedMux200gMOTNAlarm,
       "speedMux200gMBoardHWAlarm": speedMux200gMBoardHWAlarm,
       "speedMux200gMConfigTable": speedMux200gMConfigTable,
       "speedMux200gMConfigEntry": speedMux200gMConfigEntry,
       "speedMux200gMConfigIndex": speedMux200gMConfigIndex,
       "speedMux200gMNetIpAddress": speedMux200gMNetIpAddress,
       "speedMux200gMNetNetmask": speedMux200gMNetNetmask,
       "speedMux200gMNetGateway": speedMux200gMNetGateway,
       "speedMux200gMSNMPTrapsink1": speedMux200gMSNMPTrapsink1,
       "speedMux200gMSNMPTrapsink2": speedMux200gMSNMPTrapsink2,
       "speedMux200gMSNMPTrapsink3": speedMux200gMSNMPTrapsink3,
       "speedMux200gMSNMPTrapsink4": speedMux200gMSNMPTrapsink4,
       "speedMux200gMSNMPTrapsink5": speedMux200gMSNMPTrapsink5,
       "speedMux200gMSNMPReadCommunity": speedMux200gMSNMPReadCommunity,
       "speedMux200gMTempWarningLevel": speedMux200gMTempWarningLevel,
       "speedMux200gMTempAlarmLevel": speedMux200gMTempAlarmLevel,
       "speedMux200gMSNMPSysContact": speedMux200gMSNMPSysContact,
       "speedMux200gMSNMPSysLocation": speedMux200gMSNMPSysLocation,
       "speedMux200gMCLIUserTimeout": speedMux200gMCLIUserTimeout,
       "speedMux200gMNetAccess": speedMux200gMNetAccess,
       "speedMux200gMApplicationConfig": speedMux200gMApplicationConfig,
       "speedMux200gEthPortTable": speedMux200gEthPortTable,
       "speedMux200gEthPortEntry": speedMux200gEthPortEntry,
       "speedMux200gEthPortIndex": speedMux200gEthPortIndex,
       "speedMux200gEthSlot": speedMux200gEthSlot,
       "speedMux200gEthPort": speedMux200gEthPort,
       "speedMux200gEthPortDescription": speedMux200gEthPortDescription,
       "speedMux200gEthPortMode": speedMux200gEthPortMode,
       "speedMux200gEthPortOperState": speedMux200gEthPortOperState,
       "speedMux200gClientPortLaneTable": speedMux200gClientPortLaneTable,
       "speedMux200gClientPortLaneEntry": speedMux200gClientPortLaneEntry,
       "speedMux200gClientPortLaneIndex": speedMux200gClientPortLaneIndex,
       "speedMux200gClientSlot": speedMux200gClientSlot,
       "speedMux200gClientPortLane": speedMux200gClientPortLane,
       "speedMux200gClientPortLaneDescription": speedMux200gClientPortLaneDescription,
       "speedMux200gClientPortLaneAdminConfig": speedMux200gClientPortLaneAdminConfig,
       "speedMux200gClientPortLaneOperState": speedMux200gClientPortLaneOperState,
       "speedMux200gClientPortLaneLoopConfig": speedMux200gClientPortLaneLoopConfig,
       "speedMux200gClientPortLaneAlarmDeactivation": speedMux200gClientPortLaneAlarmDeactivation,
       "speedMux200gClientPortLaneAlarmSchedule": speedMux200gClientPortLaneAlarmSchedule,
       "speedMux200gClientPortLaneProtocol": speedMux200gClientPortLaneProtocol,
       "speedMux200gClientPortLaneConnectionToLinePort": speedMux200gClientPortLaneConnectionToLinePort,
       "speedMux200gClientPortLaneLLCFconfig": speedMux200gClientPortLaneLLCFconfig,
       "speedMux200gLinePortTable": speedMux200gLinePortTable,
       "speedMux200gLinePortEntry": speedMux200gLinePortEntry,
       "speedMux200gLinePortIndex": speedMux200gLinePortIndex,
       "speedMux200gLineSlot": speedMux200gLineSlot,
       "speedMux200gLinePort": speedMux200gLinePort,
       "speedMux200gLinePortDescription": speedMux200gLinePortDescription,
       "speedMux200gLinePortAdminConfig": speedMux200gLinePortAdminConfig,
       "speedMux200gLinePortOperState": speedMux200gLinePortOperState,
       "speedMux200gLinePortLoopConfig": speedMux200gLinePortLoopConfig,
       "speedMux200gLinePortAlarmDeactivation": speedMux200gLinePortAlarmDeactivation,
       "speedMux200gLinePortAlarmSchedule": speedMux200gLinePortAlarmSchedule,
       "speedMux200gLinePortSpeed": speedMux200gLinePortSpeed,
       "speedMux200gLineGroup": speedMux200gLineGroup,
       "speedMux200gLinePortLLCFconfig": speedMux200gLinePortLLCFconfig,
       "speedMux200gLinePortXCVtunableConfigSelection": speedMux200gLinePortXCVtunableConfigSelection,
       "speedMux200gLinePortXCVtunChannelConfig": speedMux200gLinePortXCVtunChannelConfig,
       "speedMux200gLinePortXCVtunWavelengthConfig": speedMux200gLinePortXCVtunWavelengthConfig,
       "speedMux200gLinePortXCVTxPower": speedMux200gLinePortXCVTxPower,
       "speedMux200gLinePortXCVConfigDispersion": speedMux200gLinePortXCVConfigDispersion,
       "speedMux200gLinePortEncryption": speedMux200gLinePortEncryption,
       "speedMux200gLinePortModulationConfig": speedMux200gLinePortModulationConfig,
       "speedMux200gClientPortXCVInfoTable": speedMux200gClientPortXCVInfoTable,
       "speedMux200gClientPortXCVInfoEntry": speedMux200gClientPortXCVInfoEntry,
       "speedMux200gClientPortXCVInfoIndex": speedMux200gClientPortXCVInfoIndex,
       "speedMux200gClientXCVInfoSlot": speedMux200gClientXCVInfoSlot,
       "speedMux200gClientXCVInfoPort": speedMux200gClientXCVInfoPort,
       "speedMux200gClientPortXCVState": speedMux200gClientPortXCVState,
       "speedMux200gClientPortXCVVendorName": speedMux200gClientPortXCVVendorName,
       "speedMux200gClientPortXCVVendorPartNumber": speedMux200gClientPortXCVVendorPartNumber,
       "speedMux200gClientPortXCVVendorSerialNumber": speedMux200gClientPortXCVVendorSerialNumber,
       "speedMux200gClientPortXCVType": speedMux200gClientPortXCVType,
       "speedMux200gClientPortXCVConnector": speedMux200gClientPortXCVConnector,
       "speedMux200gClientPortXCVLaneCount": speedMux200gClientPortXCVLaneCount,
       "speedMux200gClientPortXCVWavelengthLane1": speedMux200gClientPortXCVWavelengthLane1,
       "speedMux200gClientPortXCVWavelengthLane2": speedMux200gClientPortXCVWavelengthLane2,
       "speedMux200gClientPortXCVWavelengthLane3": speedMux200gClientPortXCVWavelengthLane3,
       "speedMux200gClientPortXCVWavelengthLane4": speedMux200gClientPortXCVWavelengthLane4,
       "speedMux200gClientPortXCVDMIState": speedMux200gClientPortXCVDMIState,
       "speedMux200gClientPortXCVDMITemp": speedMux200gClientPortXCVDMITemp,
       "speedMux200gLinePortXCVInfoTable": speedMux200gLinePortXCVInfoTable,
       "speedMux200gLinePortXCVInfoEntry": speedMux200gLinePortXCVInfoEntry,
       "speedMux200gLinePortXCVInfoIndex": speedMux200gLinePortXCVInfoIndex,
       "speedMux200gLineXCVInfoSlot": speedMux200gLineXCVInfoSlot,
       "speedMux200gLineXCVInfoPort": speedMux200gLineXCVInfoPort,
       "speedMux200gLinePortXCVState": speedMux200gLinePortXCVState,
       "speedMux200gLinePortXCVVendorName": speedMux200gLinePortXCVVendorName,
       "speedMux200gLinePortXCVVendorPartNumber": speedMux200gLinePortXCVVendorPartNumber,
       "speedMux200gLinePortXCVVendorSerialNumber": speedMux200gLinePortXCVVendorSerialNumber,
       "speedMux200gLinePortXCVType": speedMux200gLinePortXCVType,
       "speedMux200gLinePortXCVLaneCount": speedMux200gLinePortXCVLaneCount,
       "speedMux200gLinePortXCVDMIState": speedMux200gLinePortXCVDMIState,
       "speedMux200gLinePortXCVDWDMChannel": speedMux200gLinePortXCVDWDMChannel,
       "speedMux200gLinePortXCVtunFunctionality": speedMux200gLinePortXCVtunFunctionality,
       "speedMux200gLinePortXCVtunChannelSpacing": speedMux200gLinePortXCVtunChannelSpacing,
       "speedMux200gLinePortXCVtunNumberofChannels": speedMux200gLinePortXCVtunNumberofChannels,
       "speedMux200gLinePortXCVtunFirstChannel": speedMux200gLinePortXCVtunFirstChannel,
       "speedMux200gLinePortXCVtunLastChannel": speedMux200gLinePortXCVtunLastChannel,
       "speedMux200gLinePortXCVtunFirstWavelength": speedMux200gLinePortXCVtunFirstWavelength,
       "speedMux200gLinePortXCVtunLastWavelength": speedMux200gLinePortXCVtunLastWavelength,
       "speedMux200gLinePortXCVDMITemp": speedMux200gLinePortXCVDMITemp,
       "speedMux200gClientPortXCVThresholdTable": speedMux200gClientPortXCVThresholdTable,
       "speedMux200gClientPortXCVThresholdEntry": speedMux200gClientPortXCVThresholdEntry,
       "speedMux200gClientPortXCVDMIIndex": speedMux200gClientPortXCVDMIIndex,
       "speedMux200gClientPortXCVDMISlot": speedMux200gClientPortXCVDMISlot,
       "speedMux200gClientPortXCVDMIPort": speedMux200gClientPortXCVDMIPort,
       "speedMux200gClientPortXCVDMIRxLowWarningThreshold": speedMux200gClientPortXCVDMIRxLowWarningThreshold,
       "speedMux200gClientPortXCVDMIRxLowAlarmThreshold": speedMux200gClientPortXCVDMIRxLowAlarmThreshold,
       "speedMux200gClientPortXCVDMIRxHighWarningThreshold": speedMux200gClientPortXCVDMIRxHighWarningThreshold,
       "speedMux200gClientPortXCVDMIRxHighAlarmThreshold": speedMux200gClientPortXCVDMIRxHighAlarmThreshold,
       "speedMux200gClientPortXCVDMITxLowWarningThreshold": speedMux200gClientPortXCVDMITxLowWarningThreshold,
       "speedMux200gClientPortXCVDMITxLowAlarmThreshold": speedMux200gClientPortXCVDMITxLowAlarmThreshold,
       "speedMux200gClientPortXCVDMIBiasLowAlarmThreshold": speedMux200gClientPortXCVDMIBiasLowAlarmThreshold,
       "speedMux200gClientPortXCVDMIBiasHighAlarmThreshold": speedMux200gClientPortXCVDMIBiasHighAlarmThreshold,
       "speedMux200gClientPortXCVDMITempWarningThreshold": speedMux200gClientPortXCVDMITempWarningThreshold,
       "speedMux200gClientPortXCVDMITempAlarmThreshold": speedMux200gClientPortXCVDMITempAlarmThreshold,
       "speedMux200gLinePortXCVThresholdTable": speedMux200gLinePortXCVThresholdTable,
       "speedMux200gLinePortXCVThresholdEntry": speedMux200gLinePortXCVThresholdEntry,
       "speedMux200gLinePortXCVDMIIndex": speedMux200gLinePortXCVDMIIndex,
       "speedMux200gLinePortXCVDMISlot": speedMux200gLinePortXCVDMISlot,
       "speedMux200gLinePortXCVDMIPort": speedMux200gLinePortXCVDMIPort,
       "speedMux200gLinePortXCVDMIRxLowWarningThreshold": speedMux200gLinePortXCVDMIRxLowWarningThreshold,
       "speedMux200gLinePortXCVDMIRxLowAlarmThreshold": speedMux200gLinePortXCVDMIRxLowAlarmThreshold,
       "speedMux200gLinePortXCVDMIRxHighWarningThreshold": speedMux200gLinePortXCVDMIRxHighWarningThreshold,
       "speedMux200gLinePortXCVDMIRxHighAlarmThreshold": speedMux200gLinePortXCVDMIRxHighAlarmThreshold,
       "speedMux200gLinePortXCVDMITxLowWarningThreshold": speedMux200gLinePortXCVDMITxLowWarningThreshold,
       "speedMux200gLinePortXCVDMITxLowAlarmThreshold": speedMux200gLinePortXCVDMITxLowAlarmThreshold,
       "speedMux200gLinePortXCVDMIBiasLowAlarmThreshold": speedMux200gLinePortXCVDMIBiasLowAlarmThreshold,
       "speedMux200gLinePortXCVDMIBiasHighAlarmThreshold": speedMux200gLinePortXCVDMIBiasHighAlarmThreshold,
       "speedMux200gLinePortXCVDMITempWarningThreshold": speedMux200gLinePortXCVDMITempWarningThreshold,
       "speedMux200gLinePortXCVDMITempAlarmThreshold": speedMux200gLinePortXCVDMITempAlarmThreshold,
       "speedMux200gClientPortXCVValueTable": speedMux200gClientPortXCVValueTable,
       "speedMux200gClientPortXCVValueEntry": speedMux200gClientPortXCVValueEntry,
       "speedMux200gClientPortXCVDMIMIndex": speedMux200gClientPortXCVDMIMIndex,
       "speedMux200gClientPortXCVDMIMSlot": speedMux200gClientPortXCVDMIMSlot,
       "speedMux200gClientPortXCVDMIMPort": speedMux200gClientPortXCVDMIMPort,
       "speedMux200gClientPortXCVDMIRxLevelLane1": speedMux200gClientPortXCVDMIRxLevelLane1,
       "speedMux200gClientPortXCVDMIRxLevelLane2": speedMux200gClientPortXCVDMIRxLevelLane2,
       "speedMux200gClientPortXCVDMIRxLevelLane3": speedMux200gClientPortXCVDMIRxLevelLane3,
       "speedMux200gClientPortXCVDMIRxLevelLane4": speedMux200gClientPortXCVDMIRxLevelLane4,
       "speedMux200gClientPortXCVDMITxLevelLane1": speedMux200gClientPortXCVDMITxLevelLane1,
       "speedMux200gClientPortXCVDMITxLevelLane2": speedMux200gClientPortXCVDMITxLevelLane2,
       "speedMux200gClientPortXCVDMITxLevelLane3": speedMux200gClientPortXCVDMITxLevelLane3,
       "speedMux200gClientPortXCVDMITxLevelLane4": speedMux200gClientPortXCVDMITxLevelLane4,
       "speedMux200gClientPortXCVDMITxBiasLane1": speedMux200gClientPortXCVDMITxBiasLane1,
       "speedMux200gClientPortXCVDMITxBiasLane2": speedMux200gClientPortXCVDMITxBiasLane2,
       "speedMux200gClientPortXCVDMITxBiasLane3": speedMux200gClientPortXCVDMITxBiasLane3,
       "speedMux200gClientPortXCVDMITxBiasLane4": speedMux200gClientPortXCVDMITxBiasLane4,
       "speedMux200gLinePortXCVValueTable": speedMux200gLinePortXCVValueTable,
       "speedMux200gLinePortXCVValueEntry": speedMux200gLinePortXCVValueEntry,
       "speedMux200gLinePortXCVDMIMIndex": speedMux200gLinePortXCVDMIMIndex,
       "speedMux200gLinePortXCVDMIMSlot": speedMux200gLinePortXCVDMIMSlot,
       "speedMux200gLinePortXCVDMIMPort": speedMux200gLinePortXCVDMIMPort,
       "speedMux200gLinePortXCVDMITempLevel": speedMux200gLinePortXCVDMITempLevel,
       "speedMux200gLinePortXCVDMIRxLevel": speedMux200gLinePortXCVDMIRxLevel,
       "speedMux200gLinePortXCVDMITxLevel": speedMux200gLinePortXCVDMITxLevel,
       "speedMux200gLinePortXCVDMITxBias": speedMux200gLinePortXCVDMITxBias,
       "speedMux200gLinePortXCVDMIDispersion": speedMux200gLinePortXCVDMIDispersion,
       "speedMux200gLinePortOTNFECcorrectedBits": speedMux200gLinePortOTNFECcorrectedBits,
       "speedMux200gLinePortOTNFECuncorrectedBlocks": speedMux200gLinePortOTNFECuncorrectedBlocks,
       "speedMux200gClientPortXCVAlarmTable": speedMux200gClientPortXCVAlarmTable,
       "speedMux200gClientPortXCVAlarmEntry": speedMux200gClientPortXCVAlarmEntry,
       "speedMux200gClientPortXCVDAlarmIndex": speedMux200gClientPortXCVDAlarmIndex,
       "speedMux200gClientPortXCVAlarmSlot": speedMux200gClientPortXCVAlarmSlot,
       "speedMux200gClientPortXCVAlarmPort": speedMux200gClientPortXCVAlarmPort,
       "speedMux200gClientPortXCVRxAlarmLane1": speedMux200gClientPortXCVRxAlarmLane1,
       "speedMux200gClientPortXCVRxAlarmLane2": speedMux200gClientPortXCVRxAlarmLane2,
       "speedMux200gClientPortXCVRxAlarmLane3": speedMux200gClientPortXCVRxAlarmLane3,
       "speedMux200gClientPortXCVRxAlarmLane4": speedMux200gClientPortXCVRxAlarmLane4,
       "speedMux200gClientPortXCVTxAlarmLane1": speedMux200gClientPortXCVTxAlarmLane1,
       "speedMux200gClientPortXCVTxAlarmLane2": speedMux200gClientPortXCVTxAlarmLane2,
       "speedMux200gClientPortXCVTxAlarmLane3": speedMux200gClientPortXCVTxAlarmLane3,
       "speedMux200gClientPortXCVTxAlarmLane4": speedMux200gClientPortXCVTxAlarmLane4,
       "speedMux200gClientPortXCVTxBiasAlarmLane1": speedMux200gClientPortXCVTxBiasAlarmLane1,
       "speedMux200gClientPortXCVTxBiasAlarmLane2": speedMux200gClientPortXCVTxBiasAlarmLane2,
       "speedMux200gClientPortXCVTxBiasAlarmLane3": speedMux200gClientPortXCVTxBiasAlarmLane3,
       "speedMux200gClientPortXCVTxBiasAlarmLane4": speedMux200gClientPortXCVTxBiasAlarmLane4,
       "speedMux200gClientPortXCVCDRAlarmLane1": speedMux200gClientPortXCVCDRAlarmLane1,
       "speedMux200gClientPortXCVCDRAlarmLane2": speedMux200gClientPortXCVCDRAlarmLane2,
       "speedMux200gClientPortXCVCDRAlarmLane3": speedMux200gClientPortXCVCDRAlarmLane3,
       "speedMux200gClientPortXCVCDRAlarmLane4": speedMux200gClientPortXCVCDRAlarmLane4,
       "speedMux200gClientPortXCVVCCAlarm": speedMux200gClientPortXCVVCCAlarm,
       "speedMux200gClientPortXCVTempAlarm": speedMux200gClientPortXCVTempAlarm,
       "speedMux200gLinePortAlarmTable": speedMux200gLinePortAlarmTable,
       "speedMux200gLinePortAlarmEntry": speedMux200gLinePortAlarmEntry,
       "speedMux200gLinePortAlarmIndex": speedMux200gLinePortAlarmIndex,
       "speedMux200gLinePortAlarmSlot": speedMux200gLinePortAlarmSlot,
       "speedMux200gLinePortAlarmPort": speedMux200gLinePortAlarmPort,
       "speedMux200gLinePortXCVRxAlarm": speedMux200gLinePortXCVRxAlarm,
       "speedMux200gLinePortXCVTxAlarm": speedMux200gLinePortXCVTxAlarm,
       "speedMux200gLinePortXCVTxBiasAlarm": speedMux200gLinePortXCVTxBiasAlarm,
       "speedMux200gLinePortXCVTempAlarm": speedMux200gLinePortXCVTempAlarm,
       "speedMux200gLinePortEncryptionAlarm": speedMux200gLinePortEncryptionAlarm,
       "speedMux200gProfileTable": speedMux200gProfileTable,
       "speedMux200gProfileEntry": speedMux200gProfileEntry,
       "speedMux200gProfileIndex": speedMux200gProfileIndex,
       "speedMux200gProfileSlot": speedMux200gProfileSlot,
       "speedMux200gProfileNumber": speedMux200gProfileNumber,
       "speedMux200gProfileIsEditable": speedMux200gProfileIsEditable,
       "speedMux200gProfileDescription": speedMux200gProfileDescription,
       "speedMux200gProfilePort": speedMux200gProfilePort,
       "speedMux200gProfilePortMapToLine": speedMux200gProfilePortMapToLine,
       "speedMux200gProfilePortProtocol": speedMux200gProfilePortProtocol,
       "speedMux200gProfileProtecionConfig": speedMux200gProfileProtecionConfig,
       "speedMux200gMLineProtectionTable": speedMux200gMLineProtectionTable,
       "speedMux200gMLineProtectionEntry": speedMux200gMLineProtectionEntry,
       "speedMux200gMProtectionIndex": speedMux200gMProtectionIndex,
       "speedMux200gMProtectionSlot": speedMux200gMProtectionSlot,
       "speedMux200gMProtectionMode": speedMux200gMProtectionMode,
       "speedMux200gMProtectionFallbackConfig": speedMux200gMProtectionFallbackConfig,
       "speedMux200gMProtectionStatus": speedMux200gMProtectionStatus,
       "speedMux200gMProtectionMainPath": speedMux200gMProtectionMainPath,
       "speedMux200gMProtectionBackupPath": speedMux200gMProtectionBackupPath,
       "speedMux200gMProtectionFallbackTime": speedMux200gMProtectionFallbackTime}
)
