# SNMP MIB module (SPEED-DUALLINE-FC) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\pandacom\SPEED-DUALLINE-FC

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

speedDuallineFC = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 3652, 3, 3, 3)
)
if mibBuilder.loadTexts:
    speedDuallineFC.setRevisions(
        ("2019-11-07 00:00",
         "2019-04-25 00:00",
         "2017-12-07 00:00",
         "2013-12-12 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_SpeedDuallineFCMOverviewTable_Object = MibTable
speedDuallineFCMOverviewTable = _SpeedDuallineFCMOverviewTable_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 3, 3, 1)
)
if mibBuilder.loadTexts:
    speedDuallineFCMOverviewTable.setStatus("current")
_SpeedDuallineFCMOverviewEntry_Object = MibTableRow
speedDuallineFCMOverviewEntry = _SpeedDuallineFCMOverviewEntry_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 3, 3, 1, 1)
)
speedDuallineFCMOverviewEntry.setIndexNames(
    (0, "SPEED-DUALLINE-FC", "speedDuallineFCSlot"),
)
if mibBuilder.loadTexts:
    speedDuallineFCMOverviewEntry.setStatus("current")


class _SpeedDuallineFCSlot_Type(Integer32):
    """Custom type speedDuallineFCSlot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 19),
    )


_SpeedDuallineFCSlot_Type.__name__ = "Integer32"
_SpeedDuallineFCSlot_Object = MibTableColumn
speedDuallineFCSlot = _SpeedDuallineFCSlot_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 3, 3, 1, 1, 2),
    _SpeedDuallineFCSlot_Type()
)
speedDuallineFCSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    speedDuallineFCSlot.setStatus("current")


class _SpeedDuallineFCMDevice_Type(Integer32):
    """Custom type speedDuallineFCMDevice based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              32,
              255)
        )
    )
    namedValues = NamedValues(
        *(("notAvailable", 0),
          ("speedDuallineFCXFP", 6),
          ("speedDuallineFCSFP", 7),
          ("speedDualline10GXFP", 8),
          ("speedDualline10GSFP", 9),
          ("speedDualline16GXFP", 10),
          ("speedDualline16GSFP", 11),
          ("speedDualline10GXFP2R", 12),
          ("speedDualline16GSFPH", 32),
          ("unknown", 255))
    )


_SpeedDuallineFCMDevice_Type.__name__ = "Integer32"
_SpeedDuallineFCMDevice_Object = MibTableColumn
speedDuallineFCMDevice = _SpeedDuallineFCMDevice_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 3, 3, 1, 1, 3),
    _SpeedDuallineFCMDevice_Type()
)
speedDuallineFCMDevice.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    speedDuallineFCMDevice.setStatus("current")


class _SpeedDuallineFCMState_Type(Integer32):
    """Custom type speedDuallineFCMState based on Integer32"""
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
          ("resetCAN", 4),
          ("resetHardware", 5),
          ("unknown", 255))
    )


_SpeedDuallineFCMState_Type.__name__ = "Integer32"
_SpeedDuallineFCMState_Object = MibTableColumn
speedDuallineFCMState = _SpeedDuallineFCMState_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 3, 3, 1, 1, 4),
    _SpeedDuallineFCMState_Type()
)
speedDuallineFCMState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    speedDuallineFCMState.setStatus("current")


class _SpeedDuallineFCMSysName_Type(DisplayString):
    """Custom type speedDuallineFCMSysName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_SpeedDuallineFCMSysName_Type.__name__ = "DisplayString"
_SpeedDuallineFCMSysName_Object = MibTableColumn
speedDuallineFCMSysName = _SpeedDuallineFCMSysName_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 3, 3, 1, 1, 5),
    _SpeedDuallineFCMSysName_Type()
)
speedDuallineFCMSysName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    speedDuallineFCMSysName.setStatus("current")
_SpeedDuallineFCMSysUpTime_Type = TimeTicks
_SpeedDuallineFCMSysUpTime_Object = MibTableColumn
speedDuallineFCMSysUpTime = _SpeedDuallineFCMSysUpTime_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 3, 3, 1, 1, 6),
    _SpeedDuallineFCMSysUpTime_Type()
)
speedDuallineFCMSysUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    speedDuallineFCMSysUpTime.setStatus("current")
_SpeedDuallineFCMTemperature_Type = Integer32
_SpeedDuallineFCMTemperature_Object = MibTableColumn
speedDuallineFCMTemperature = _SpeedDuallineFCMTemperature_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 3, 3, 1, 1, 7),
    _SpeedDuallineFCMTemperature_Type()
)
speedDuallineFCMTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    speedDuallineFCMTemperature.setStatus("current")


class _SpeedDuallineFCMAlarmState_Type(Integer32):
    """Custom type speedDuallineFCMAlarmState based on Integer32"""
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


_SpeedDuallineFCMAlarmState_Type.__name__ = "Integer32"
_SpeedDuallineFCMAlarmState_Object = MibTableColumn
speedDuallineFCMAlarmState = _SpeedDuallineFCMAlarmState_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 3, 3, 1, 1, 8),
    _SpeedDuallineFCMAlarmState_Type()
)
speedDuallineFCMAlarmState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    speedDuallineFCMAlarmState.setStatus("current")


class _SpeedDuallineFCMKernelImage_Type(DisplayString):
    """Custom type speedDuallineFCMKernelImage based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_SpeedDuallineFCMKernelImage_Type.__name__ = "DisplayString"
_SpeedDuallineFCMKernelImage_Object = MibTableColumn
speedDuallineFCMKernelImage = _SpeedDuallineFCMKernelImage_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 3, 3, 1, 1, 9),
    _SpeedDuallineFCMKernelImage_Type()
)
speedDuallineFCMKernelImage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    speedDuallineFCMKernelImage.setStatus("current")


class _SpeedDuallineFCMAppImage_Type(DisplayString):
    """Custom type speedDuallineFCMAppImage based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_SpeedDuallineFCMAppImage_Type.__name__ = "DisplayString"
_SpeedDuallineFCMAppImage_Object = MibTableColumn
speedDuallineFCMAppImage = _SpeedDuallineFCMAppImage_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 3, 3, 1, 1, 10),
    _SpeedDuallineFCMAppImage_Type()
)
speedDuallineFCMAppImage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    speedDuallineFCMAppImage.setStatus("current")


class _SpeedDuallineFCMHwVersion_Type(DisplayString):
    """Custom type speedDuallineFCMHwVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 17),
    )


_SpeedDuallineFCMHwVersion_Type.__name__ = "DisplayString"
_SpeedDuallineFCMHwVersion_Object = MibTableColumn
speedDuallineFCMHwVersion = _SpeedDuallineFCMHwVersion_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 3, 3, 1, 1, 11),
    _SpeedDuallineFCMHwVersion_Type()
)
speedDuallineFCMHwVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    speedDuallineFCMHwVersion.setStatus("current")


class _SpeedDuallineFCMSerialNumber_Type(DisplayString):
    """Custom type speedDuallineFCMSerialNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 17),
    )


_SpeedDuallineFCMSerialNumber_Type.__name__ = "DisplayString"
_SpeedDuallineFCMSerialNumber_Object = MibTableColumn
speedDuallineFCMSerialNumber = _SpeedDuallineFCMSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 3, 3, 1, 1, 12),
    _SpeedDuallineFCMSerialNumber_Type()
)
speedDuallineFCMSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    speedDuallineFCMSerialNumber.setStatus("current")


class _SpeedDuallineFCMEthPortState_Type(Integer32):
    """Custom type speedDuallineFCMEthPortState based on Integer32"""
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
        *(("notavailable", 0),
          ("linkDown", 1),
          ("hdx10", 2),
          ("fdx10", 3),
          ("hdx100", 4),
          ("fdx100", 5),
          ("off", 6),
          ("unknown", 255))
    )


_SpeedDuallineFCMEthPortState_Type.__name__ = "Integer32"
_SpeedDuallineFCMEthPortState_Object = MibTableColumn
speedDuallineFCMEthPortState = _SpeedDuallineFCMEthPortState_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 3, 3, 1, 1, 13),
    _SpeedDuallineFCMEthPortState_Type()
)
speedDuallineFCMEthPortState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    speedDuallineFCMEthPortState.setStatus("current")


class _SpeedDuallineFCMUploadState_Type(Integer32):
    """Custom type speedDuallineFCMUploadState based on Integer32"""
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


_SpeedDuallineFCMUploadState_Type.__name__ = "Integer32"
_SpeedDuallineFCMUploadState_Object = MibTableColumn
speedDuallineFCMUploadState = _SpeedDuallineFCMUploadState_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 3, 3, 1, 1, 14),
    _SpeedDuallineFCMUploadState_Type()
)
speedDuallineFCMUploadState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    speedDuallineFCMUploadState.setStatus("current")


class _SpeedDuallineFCMUpdateState_Type(Integer32):
    """Custom type speedDuallineFCMUpdateState based on Integer32"""
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


_SpeedDuallineFCMUpdateState_Type.__name__ = "Integer32"
_SpeedDuallineFCMUpdateState_Object = MibTableColumn
speedDuallineFCMUpdateState = _SpeedDuallineFCMUpdateState_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 3, 3, 1, 1, 15),
    _SpeedDuallineFCMUpdateState_Type()
)
speedDuallineFCMUpdateState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    speedDuallineFCMUpdateState.setStatus("current")
_SpeedDuallineFCMConfigTable_Object = MibTable
speedDuallineFCMConfigTable = _SpeedDuallineFCMConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 3, 3, 2)
)
if mibBuilder.loadTexts:
    speedDuallineFCMConfigTable.setStatus("current")
_SpeedDuallineFCMConfigEntry_Object = MibTableRow
speedDuallineFCMConfigEntry = _SpeedDuallineFCMConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 3, 3, 2, 1)
)
speedDuallineFCMConfigEntry.setIndexNames(
    (0, "SPEED-DUALLINE-FC", "speedDuallineFCMSlot"),
)
if mibBuilder.loadTexts:
    speedDuallineFCMConfigEntry.setStatus("current")


class _SpeedDuallineFCMSlot_Type(Integer32):
    """Custom type speedDuallineFCMSlot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 19),
    )


_SpeedDuallineFCMSlot_Type.__name__ = "Integer32"
_SpeedDuallineFCMSlot_Object = MibTableColumn
speedDuallineFCMSlot = _SpeedDuallineFCMSlot_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 3, 3, 2, 1, 2),
    _SpeedDuallineFCMSlot_Type()
)
speedDuallineFCMSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    speedDuallineFCMSlot.setStatus("current")


class _SpeedDuallineFCMIpAddress_Type(IpAddress):
    """Custom type speedDuallineFCMIpAddress based on IpAddress"""
    defaultHexValue = "c0a80066"


_SpeedDuallineFCMIpAddress_Type.__name__ = "IpAddress"
_SpeedDuallineFCMIpAddress_Object = MibTableColumn
speedDuallineFCMIpAddress = _SpeedDuallineFCMIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 3, 3, 2, 1, 3),
    _SpeedDuallineFCMIpAddress_Type()
)
speedDuallineFCMIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    speedDuallineFCMIpAddress.setStatus("current")


class _SpeedDuallineFCMIpNetmask_Type(IpAddress):
    """Custom type speedDuallineFCMIpNetmask based on IpAddress"""
    defaultHexValue = "ffffff00"


_SpeedDuallineFCMIpNetmask_Type.__name__ = "IpAddress"
_SpeedDuallineFCMIpNetmask_Object = MibTableColumn
speedDuallineFCMIpNetmask = _SpeedDuallineFCMIpNetmask_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 3, 3, 2, 1, 4),
    _SpeedDuallineFCMIpNetmask_Type()
)
speedDuallineFCMIpNetmask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    speedDuallineFCMIpNetmask.setStatus("current")
_SpeedDuallineFCMIpGateway_Type = IpAddress
_SpeedDuallineFCMIpGateway_Object = MibTableColumn
speedDuallineFCMIpGateway = _SpeedDuallineFCMIpGateway_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 3, 3, 2, 1, 5),
    _SpeedDuallineFCMIpGateway_Type()
)
speedDuallineFCMIpGateway.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    speedDuallineFCMIpGateway.setStatus("current")
_SpeedDuallineFCMTrapSink1_Type = IpAddress
_SpeedDuallineFCMTrapSink1_Object = MibTableColumn
speedDuallineFCMTrapSink1 = _SpeedDuallineFCMTrapSink1_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 3, 3, 2, 1, 6),
    _SpeedDuallineFCMTrapSink1_Type()
)
speedDuallineFCMTrapSink1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    speedDuallineFCMTrapSink1.setStatus("current")
_SpeedDuallineFCMTrapSink2_Type = IpAddress
_SpeedDuallineFCMTrapSink2_Object = MibTableColumn
speedDuallineFCMTrapSink2 = _SpeedDuallineFCMTrapSink2_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 3, 3, 2, 1, 7),
    _SpeedDuallineFCMTrapSink2_Type()
)
speedDuallineFCMTrapSink2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    speedDuallineFCMTrapSink2.setStatus("current")
_SpeedDuallineFCMTrapSink3_Type = IpAddress
_SpeedDuallineFCMTrapSink3_Object = MibTableColumn
speedDuallineFCMTrapSink3 = _SpeedDuallineFCMTrapSink3_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 3, 3, 2, 1, 8),
    _SpeedDuallineFCMTrapSink3_Type()
)
speedDuallineFCMTrapSink3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    speedDuallineFCMTrapSink3.setStatus("current")
_SpeedDuallineFCMTrapSink4_Type = IpAddress
_SpeedDuallineFCMTrapSink4_Object = MibTableColumn
speedDuallineFCMTrapSink4 = _SpeedDuallineFCMTrapSink4_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 3, 3, 2, 1, 9),
    _SpeedDuallineFCMTrapSink4_Type()
)
speedDuallineFCMTrapSink4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    speedDuallineFCMTrapSink4.setStatus("current")
_SpeedDuallineFCMTrapSink5_Type = IpAddress
_SpeedDuallineFCMTrapSink5_Object = MibTableColumn
speedDuallineFCMTrapSink5 = _SpeedDuallineFCMTrapSink5_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 3, 3, 2, 1, 10),
    _SpeedDuallineFCMTrapSink5_Type()
)
speedDuallineFCMTrapSink5.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    speedDuallineFCMTrapSink5.setStatus("current")


class _SpeedDuallineFCMSNMPReadCommunity_Type(DisplayString):
    """Custom type speedDuallineFCMSNMPReadCommunity based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_SpeedDuallineFCMSNMPReadCommunity_Type.__name__ = "DisplayString"
_SpeedDuallineFCMSNMPReadCommunity_Object = MibTableColumn
speedDuallineFCMSNMPReadCommunity = _SpeedDuallineFCMSNMPReadCommunity_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 3, 3, 2, 1, 11),
    _SpeedDuallineFCMSNMPReadCommunity_Type()
)
speedDuallineFCMSNMPReadCommunity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    speedDuallineFCMSNMPReadCommunity.setStatus("current")


class _SpeedDuallineFCMSNMPWriteCommunity_Type(DisplayString):
    """Custom type speedDuallineFCMSNMPWriteCommunity based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_SpeedDuallineFCMSNMPWriteCommunity_Type.__name__ = "DisplayString"
_SpeedDuallineFCMSNMPWriteCommunity_Object = MibTableColumn
speedDuallineFCMSNMPWriteCommunity = _SpeedDuallineFCMSNMPWriteCommunity_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 3, 3, 2, 1, 12),
    _SpeedDuallineFCMSNMPWriteCommunity_Type()
)
speedDuallineFCMSNMPWriteCommunity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    speedDuallineFCMSNMPWriteCommunity.setStatus("current")


class _SpeedDuallineFCMTempWarningLevel_Type(Integer32):
    """Custom type speedDuallineFCMTempWarningLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 60),
    )


_SpeedDuallineFCMTempWarningLevel_Type.__name__ = "Integer32"
_SpeedDuallineFCMTempWarningLevel_Object = MibTableColumn
speedDuallineFCMTempWarningLevel = _SpeedDuallineFCMTempWarningLevel_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 3, 3, 2, 1, 13),
    _SpeedDuallineFCMTempWarningLevel_Type()
)
speedDuallineFCMTempWarningLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    speedDuallineFCMTempWarningLevel.setStatus("current")
_SpeedDuallineFCMTempAlarmLevel_Type = Integer32
_SpeedDuallineFCMTempAlarmLevel_Object = MibTableColumn
speedDuallineFCMTempAlarmLevel = _SpeedDuallineFCMTempAlarmLevel_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 3, 3, 2, 1, 14),
    _SpeedDuallineFCMTempAlarmLevel_Type()
)
speedDuallineFCMTempAlarmLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    speedDuallineFCMTempAlarmLevel.setStatus("current")


class _SpeedDuallineFCMSNMPSyscontact_Type(DisplayString):
    """Custom type speedDuallineFCMSNMPSyscontact based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_SpeedDuallineFCMSNMPSyscontact_Type.__name__ = "DisplayString"
_SpeedDuallineFCMSNMPSyscontact_Object = MibTableColumn
speedDuallineFCMSNMPSyscontact = _SpeedDuallineFCMSNMPSyscontact_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 3, 3, 2, 1, 15),
    _SpeedDuallineFCMSNMPSyscontact_Type()
)
speedDuallineFCMSNMPSyscontact.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    speedDuallineFCMSNMPSyscontact.setStatus("current")


class _SpeedDuallineFCMSNMPSyslocation_Type(DisplayString):
    """Custom type speedDuallineFCMSNMPSyslocation based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_SpeedDuallineFCMSNMPSyslocation_Type.__name__ = "DisplayString"
_SpeedDuallineFCMSNMPSyslocation_Object = MibTableColumn
speedDuallineFCMSNMPSyslocation = _SpeedDuallineFCMSNMPSyslocation_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 3, 3, 2, 1, 16),
    _SpeedDuallineFCMSNMPSyslocation_Type()
)
speedDuallineFCMSNMPSyslocation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    speedDuallineFCMSNMPSyslocation.setStatus("current")


class _SpeedDuallineFCMPortTxConnection_Type(Integer32):
    """Custom type speedDuallineFCMPortTxConnection based on Integer32"""
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
          ("connect1to3and2to4", 1),
          ("connect1to4and2to3", 2),
          ("connect1to2and3to4fixed", 3),
          ("unknown", 255))
    )


_SpeedDuallineFCMPortTxConnection_Type.__name__ = "Integer32"
_SpeedDuallineFCMPortTxConnection_Object = MibTableColumn
speedDuallineFCMPortTxConnection = _SpeedDuallineFCMPortTxConnection_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 3, 3, 2, 1, 17),
    _SpeedDuallineFCMPortTxConnection_Type()
)
speedDuallineFCMPortTxConnection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    speedDuallineFCMPortTxConnection.setStatus("current")


class _SpeedDuallineFCMUserTimeout_Type(Integer32):
    """Custom type speedDuallineFCMUserTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(120, 3600),
    )


_SpeedDuallineFCMUserTimeout_Type.__name__ = "Integer32"
_SpeedDuallineFCMUserTimeout_Object = MibTableColumn
speedDuallineFCMUserTimeout = _SpeedDuallineFCMUserTimeout_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 3, 3, 2, 1, 18),
    _SpeedDuallineFCMUserTimeout_Type()
)
speedDuallineFCMUserTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    speedDuallineFCMUserTimeout.setStatus("current")


class _SpeedDuallineFCMEthPortMode_Type(Integer32):
    """Custom type speedDuallineFCMEthPortMode based on Integer32"""
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
        *(("notavailable", 0),
          ("autoneg", 1),
          ("hdx10", 2),
          ("fdx10", 3),
          ("hdx100", 4),
          ("fdx100", 5),
          ("off", 6),
          ("unknown", 255))
    )


_SpeedDuallineFCMEthPortMode_Type.__name__ = "Integer32"
_SpeedDuallineFCMEthPortMode_Object = MibTableColumn
speedDuallineFCMEthPortMode = _SpeedDuallineFCMEthPortMode_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 3, 3, 2, 1, 19),
    _SpeedDuallineFCMEthPortMode_Type()
)
speedDuallineFCMEthPortMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    speedDuallineFCMEthPortMode.setStatus("current")


class _SpeedDuallineFCMAccess_Type(Integer32):
    """Custom type speedDuallineFCMAccess based on Integer32"""
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


_SpeedDuallineFCMAccess_Type.__name__ = "Integer32"
_SpeedDuallineFCMAccess_Object = MibTableColumn
speedDuallineFCMAccess = _SpeedDuallineFCMAccess_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 3, 3, 2, 1, 20),
    _SpeedDuallineFCMAccess_Type()
)
speedDuallineFCMAccess.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    speedDuallineFCMAccess.setStatus("current")
_SpeedDuallineFCMProtectionTable_Object = MibTable
speedDuallineFCMProtectionTable = _SpeedDuallineFCMProtectionTable_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 3, 3, 3)
)
if mibBuilder.loadTexts:
    speedDuallineFCMProtectionTable.setStatus("current")
_SpeedDuallineFCMProtectionEntry_Object = MibTableRow
speedDuallineFCMProtectionEntry = _SpeedDuallineFCMProtectionEntry_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 3, 3, 3, 1)
)
speedDuallineFCMProtectionEntry.setIndexNames(
    (0, "SPEED-DUALLINE-FC", "speedDuallineFCMLinkProtectionSlot"),
)
if mibBuilder.loadTexts:
    speedDuallineFCMProtectionEntry.setStatus("current")


class _SpeedDuallineFCMLinkProtectionSlot_Type(Integer32):
    """Custom type speedDuallineFCMLinkProtectionSlot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 19),
    )


_SpeedDuallineFCMLinkProtectionSlot_Type.__name__ = "Integer32"
_SpeedDuallineFCMLinkProtectionSlot_Object = MibTableColumn
speedDuallineFCMLinkProtectionSlot = _SpeedDuallineFCMLinkProtectionSlot_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 3, 3, 3, 1, 2),
    _SpeedDuallineFCMLinkProtectionSlot_Type()
)
speedDuallineFCMLinkProtectionSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    speedDuallineFCMLinkProtectionSlot.setStatus("current")


class _SpeedDuallineFCMLinkProtectionConfig_Type(Integer32):
    """Custom type speedDuallineFCMLinkProtectionConfig based on Integer32"""
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
        *(("unknown", 0),
          ("protectionOFF", 1),
          ("protectionOn", 2),
          ("notAvailable", 255))
    )


_SpeedDuallineFCMLinkProtectionConfig_Type.__name__ = "Integer32"
_SpeedDuallineFCMLinkProtectionConfig_Object = MibTableColumn
speedDuallineFCMLinkProtectionConfig = _SpeedDuallineFCMLinkProtectionConfig_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 3, 3, 3, 1, 3),
    _SpeedDuallineFCMLinkProtectionConfig_Type()
)
speedDuallineFCMLinkProtectionConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    speedDuallineFCMLinkProtectionConfig.setStatus("current")


class _SpeedDuallineFCMLinkProtectionState_Type(Integer32):
    """Custom type speedDuallineFCMLinkProtectionState based on Integer32"""
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
        *(("unknown", 0),
          ("port1active", 1),
          ("port2active", 2),
          ("testingPort1", 3),
          ("testingPort2", 4),
          ("noneActive", 5),
          ("notAvailable", 255))
    )


_SpeedDuallineFCMLinkProtectionState_Type.__name__ = "Integer32"
_SpeedDuallineFCMLinkProtectionState_Object = MibTableColumn
speedDuallineFCMLinkProtectionState = _SpeedDuallineFCMLinkProtectionState_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 3, 3, 3, 1, 4),
    _SpeedDuallineFCMLinkProtectionState_Type()
)
speedDuallineFCMLinkProtectionState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    speedDuallineFCMLinkProtectionState.setStatus("current")


class _SpeedDuallineFCMLinkProtectionFallbackTime_Type(Integer32):
    """Custom type speedDuallineFCMLinkProtectionFallbackTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 3600),
    )


_SpeedDuallineFCMLinkProtectionFallbackTime_Type.__name__ = "Integer32"
_SpeedDuallineFCMLinkProtectionFallbackTime_Object = MibTableColumn
speedDuallineFCMLinkProtectionFallbackTime = _SpeedDuallineFCMLinkProtectionFallbackTime_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 3, 3, 3, 1, 5),
    _SpeedDuallineFCMLinkProtectionFallbackTime_Type()
)
speedDuallineFCMLinkProtectionFallbackTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    speedDuallineFCMLinkProtectionFallbackTime.setStatus("current")


class _SpeedDuallineFCMLinkProtectionRXLevelPort1_Type(Integer32):
    """Custom type speedDuallineFCMLinkProtectionRXLevelPort1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-4000, 500),
    )


_SpeedDuallineFCMLinkProtectionRXLevelPort1_Type.__name__ = "Integer32"
_SpeedDuallineFCMLinkProtectionRXLevelPort1_Object = MibTableColumn
speedDuallineFCMLinkProtectionRXLevelPort1 = _SpeedDuallineFCMLinkProtectionRXLevelPort1_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 3, 3, 3, 1, 6),
    _SpeedDuallineFCMLinkProtectionRXLevelPort1_Type()
)
speedDuallineFCMLinkProtectionRXLevelPort1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    speedDuallineFCMLinkProtectionRXLevelPort1.setStatus("current")


class _SpeedDuallineFCMLinkProtectionRXLevelPort2_Type(Integer32):
    """Custom type speedDuallineFCMLinkProtectionRXLevelPort2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-4000, 500),
    )


_SpeedDuallineFCMLinkProtectionRXLevelPort2_Type.__name__ = "Integer32"
_SpeedDuallineFCMLinkProtectionRXLevelPort2_Object = MibTableColumn
speedDuallineFCMLinkProtectionRXLevelPort2 = _SpeedDuallineFCMLinkProtectionRXLevelPort2_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 3, 3, 3, 1, 7),
    _SpeedDuallineFCMLinkProtectionRXLevelPort2_Type()
)
speedDuallineFCMLinkProtectionRXLevelPort2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    speedDuallineFCMLinkProtectionRXLevelPort2.setStatus("current")


class _SpeedDuallineFCMLinkProtectionClientPort_Type(Integer32):
    """Custom type speedDuallineFCMLinkProtectionClientPort based on Integer32"""
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
          ("port3", 1),
          ("port4", 2),
          ("unknown", 255))
    )


_SpeedDuallineFCMLinkProtectionClientPort_Type.__name__ = "Integer32"
_SpeedDuallineFCMLinkProtectionClientPort_Object = MibTableColumn
speedDuallineFCMLinkProtectionClientPort = _SpeedDuallineFCMLinkProtectionClientPort_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 3, 3, 3, 1, 8),
    _SpeedDuallineFCMLinkProtectionClientPort_Type()
)
speedDuallineFCMLinkProtectionClientPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    speedDuallineFCMLinkProtectionClientPort.setStatus("current")


class _SpeedDuallineFCMLinkProtectionMode_Type(Integer32):
    """Custom type speedDuallineFCMLinkProtectionMode based on Integer32"""
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
        *(("notavailable", 0),
          ("fallbackPort1", 1),
          ("fallbackPort2", 2),
          ("staticPort1", 3),
          ("staticPort2", 4),
          ("unknown", 255))
    )


_SpeedDuallineFCMLinkProtectionMode_Type.__name__ = "Integer32"
_SpeedDuallineFCMLinkProtectionMode_Object = MibTableColumn
speedDuallineFCMLinkProtectionMode = _SpeedDuallineFCMLinkProtectionMode_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 3, 3, 3, 1, 9),
    _SpeedDuallineFCMLinkProtectionMode_Type()
)
speedDuallineFCMLinkProtectionMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    speedDuallineFCMLinkProtectionMode.setStatus("current")
_SpeedDuallineFCPortOverviewTable_Object = MibTable
speedDuallineFCPortOverviewTable = _SpeedDuallineFCPortOverviewTable_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 3, 3, 4)
)
if mibBuilder.loadTexts:
    speedDuallineFCPortOverviewTable.setStatus("current")
_SpeedDuallineFCPortOverviewEntry_Object = MibTableRow
speedDuallineFCPortOverviewEntry = _SpeedDuallineFCPortOverviewEntry_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 3, 3, 4, 1)
)
speedDuallineFCPortOverviewEntry.setIndexNames(
    (0, "SPEED-DUALLINE-FC", "speedDuallineFCPortIndex"),
)
if mibBuilder.loadTexts:
    speedDuallineFCPortOverviewEntry.setStatus("current")


class _SpeedDuallineFCPortIndex_Type(Integer32):
    """Custom type speedDuallineFCPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1900),
    )


_SpeedDuallineFCPortIndex_Type.__name__ = "Integer32"
_SpeedDuallineFCPortIndex_Object = MibTableColumn
speedDuallineFCPortIndex = _SpeedDuallineFCPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 3, 3, 4, 1, 1),
    _SpeedDuallineFCPortIndex_Type()
)
speedDuallineFCPortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    speedDuallineFCPortIndex.setStatus("current")
_SpeedDuallineFCPortSlot_Type = Integer32
_SpeedDuallineFCPortSlot_Object = MibTableColumn
speedDuallineFCPortSlot = _SpeedDuallineFCPortSlot_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 3, 3, 4, 1, 2),
    _SpeedDuallineFCPortSlot_Type()
)
speedDuallineFCPortSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    speedDuallineFCPortSlot.setStatus("current")
_SpeedDuallineFCPortPort_Type = Integer32
_SpeedDuallineFCPortPort_Object = MibTableColumn
speedDuallineFCPortPort = _SpeedDuallineFCPortPort_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 3, 3, 4, 1, 3),
    _SpeedDuallineFCPortPort_Type()
)
speedDuallineFCPortPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    speedDuallineFCPortPort.setStatus("current")


class _SpeedDuallineFCPortDescription_Type(DisplayString):
    """Custom type speedDuallineFCPortDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_SpeedDuallineFCPortDescription_Type.__name__ = "DisplayString"
_SpeedDuallineFCPortDescription_Object = MibTableColumn
speedDuallineFCPortDescription = _SpeedDuallineFCPortDescription_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 3, 3, 4, 1, 4),
    _SpeedDuallineFCPortDescription_Type()
)
speedDuallineFCPortDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    speedDuallineFCPortDescription.setStatus("current")


class _SpeedDuallineFCPortAdminConfig_Type(Integer32):
    """Custom type speedDuallineFCPortAdminConfig based on Integer32"""
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


_SpeedDuallineFCPortAdminConfig_Type.__name__ = "Integer32"
_SpeedDuallineFCPortAdminConfig_Object = MibTableColumn
speedDuallineFCPortAdminConfig = _SpeedDuallineFCPortAdminConfig_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 3, 3, 4, 1, 5),
    _SpeedDuallineFCPortAdminConfig_Type()
)
speedDuallineFCPortAdminConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    speedDuallineFCPortAdminConfig.setStatus("current")


class _SpeedDuallineFCPortOperState_Type(Integer32):
    """Custom type speedDuallineFCPortOperState based on Integer32"""
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
          ("bertRunnung", 8),
          ("unknown", 255))
    )


_SpeedDuallineFCPortOperState_Type.__name__ = "Integer32"
_SpeedDuallineFCPortOperState_Object = MibTableColumn
speedDuallineFCPortOperState = _SpeedDuallineFCPortOperState_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 3, 3, 4, 1, 6),
    _SpeedDuallineFCPortOperState_Type()
)
speedDuallineFCPortOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    speedDuallineFCPortOperState.setStatus("current")


class _SpeedDuallineFCPortXCVState_Type(Integer32):
    """Custom type speedDuallineFCPortXCVState based on Integer32"""
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


_SpeedDuallineFCPortXCVState_Type.__name__ = "Integer32"
_SpeedDuallineFCPortXCVState_Object = MibTableColumn
speedDuallineFCPortXCVState = _SpeedDuallineFCPortXCVState_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 3, 3, 4, 1, 7),
    _SpeedDuallineFCPortXCVState_Type()
)
speedDuallineFCPortXCVState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    speedDuallineFCPortXCVState.setStatus("current")


class _SpeedDuallineFCPortLLCFconfig_Type(Integer32):
    """Custom type speedDuallineFCPortLLCFconfig based on Integer32"""
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
          ("off", 1),
          ("on", 2),
          ("unknown", 255))
    )


_SpeedDuallineFCPortLLCFconfig_Type.__name__ = "Integer32"
_SpeedDuallineFCPortLLCFconfig_Object = MibTableColumn
speedDuallineFCPortLLCFconfig = _SpeedDuallineFCPortLLCFconfig_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 3, 3, 4, 1, 8),
    _SpeedDuallineFCPortLLCFconfig_Type()
)
speedDuallineFCPortLLCFconfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    speedDuallineFCPortLLCFconfig.setStatus("current")


class _SpeedDuallineFCPortLoopConfig_Type(Integer32):
    """Custom type speedDuallineFCPortLoopConfig based on Integer32"""
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
          ("off", 1),
          ("on", 2),
          ("unknown", 255))
    )


_SpeedDuallineFCPortLoopConfig_Type.__name__ = "Integer32"
_SpeedDuallineFCPortLoopConfig_Object = MibTableColumn
speedDuallineFCPortLoopConfig = _SpeedDuallineFCPortLoopConfig_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 3, 3, 4, 1, 9),
    _SpeedDuallineFCPortLoopConfig_Type()
)
speedDuallineFCPortLoopConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    speedDuallineFCPortLoopConfig.setStatus("current")


class _SpeedDuallineFCPortSpeedConfig_Type(Integer32):
    """Custom type speedDuallineFCPortSpeedConfig based on Integer32"""
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
              16)
        )
    )
    namedValues = NamedValues(
        *(("notAvailable", 0),
          ("fibrechannel1G", 1),
          ("fibrechannel2G", 2),
          ("fibrechannel4G", 3),
          ("fibrechannel8G", 4),
          ("fibrechannel16G", 5),
          ("sfp9930-11300", 6),
          ("bypass", 16))
    )


_SpeedDuallineFCPortSpeedConfig_Type.__name__ = "Integer32"
_SpeedDuallineFCPortSpeedConfig_Object = MibTableColumn
speedDuallineFCPortSpeedConfig = _SpeedDuallineFCPortSpeedConfig_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 3, 3, 4, 1, 10),
    _SpeedDuallineFCPortSpeedConfig_Type()
)
speedDuallineFCPortSpeedConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    speedDuallineFCPortSpeedConfig.setStatus("current")


class _SpeedDuallineFCPortAlarmState_Type(Integer32):
    """Custom type speedDuallineFCPortAlarmState based on Integer32"""
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
          ("noAlarms", 1),
          ("activeAlarms", 2),
          ("unknown", 255))
    )


_SpeedDuallineFCPortAlarmState_Type.__name__ = "Integer32"
_SpeedDuallineFCPortAlarmState_Object = MibTableColumn
speedDuallineFCPortAlarmState = _SpeedDuallineFCPortAlarmState_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 3, 3, 4, 1, 11),
    _SpeedDuallineFCPortAlarmState_Type()
)
speedDuallineFCPortAlarmState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    speedDuallineFCPortAlarmState.setStatus("current")


class _SpeedDuallineFCPortAlarmDeactivation_Type(Integer32):
    """Custom type speedDuallineFCPortAlarmDeactivation based on Integer32"""
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


_SpeedDuallineFCPortAlarmDeactivation_Type.__name__ = "Integer32"
_SpeedDuallineFCPortAlarmDeactivation_Object = MibTableColumn
speedDuallineFCPortAlarmDeactivation = _SpeedDuallineFCPortAlarmDeactivation_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 3, 3, 4, 1, 12),
    _SpeedDuallineFCPortAlarmDeactivation_Type()
)
speedDuallineFCPortAlarmDeactivation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    speedDuallineFCPortAlarmDeactivation.setStatus("current")


class _SpeedDuallineFCPortAlarmSchedule_Type(Integer32):
    """Custom type speedDuallineFCPortAlarmSchedule based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1200),
    )


_SpeedDuallineFCPortAlarmSchedule_Type.__name__ = "Integer32"
_SpeedDuallineFCPortAlarmSchedule_Object = MibTableColumn
speedDuallineFCPortAlarmSchedule = _SpeedDuallineFCPortAlarmSchedule_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 3, 3, 4, 1, 13),
    _SpeedDuallineFCPortAlarmSchedule_Type()
)
speedDuallineFCPortAlarmSchedule.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    speedDuallineFCPortAlarmSchedule.setStatus("current")
_SpeedDuallineFCXCVOverviewTable_Object = MibTable
speedDuallineFCXCVOverviewTable = _SpeedDuallineFCXCVOverviewTable_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 3, 3, 5)
)
if mibBuilder.loadTexts:
    speedDuallineFCXCVOverviewTable.setStatus("current")
_SpeedDuallineFCXCVOverviewEntry_Object = MibTableRow
speedDuallineFCXCVOverviewEntry = _SpeedDuallineFCXCVOverviewEntry_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 3, 3, 5, 1)
)
speedDuallineFCXCVOverviewEntry.setIndexNames(
    (0, "SPEED-DUALLINE-FC", "speedDuallineFCPortXCVIndex"),
)
if mibBuilder.loadTexts:
    speedDuallineFCXCVOverviewEntry.setStatus("current")


class _SpeedDuallineFCPortXCVIndex_Type(Integer32):
    """Custom type speedDuallineFCPortXCVIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1900),
    )


_SpeedDuallineFCPortXCVIndex_Type.__name__ = "Integer32"
_SpeedDuallineFCPortXCVIndex_Object = MibTableColumn
speedDuallineFCPortXCVIndex = _SpeedDuallineFCPortXCVIndex_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 3, 3, 5, 1, 1),
    _SpeedDuallineFCPortXCVIndex_Type()
)
speedDuallineFCPortXCVIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    speedDuallineFCPortXCVIndex.setStatus("current")
_SpeedDuallineFCPortXCVSlot_Type = Integer32
_SpeedDuallineFCPortXCVSlot_Object = MibTableColumn
speedDuallineFCPortXCVSlot = _SpeedDuallineFCPortXCVSlot_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 3, 3, 5, 1, 2),
    _SpeedDuallineFCPortXCVSlot_Type()
)
speedDuallineFCPortXCVSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    speedDuallineFCPortXCVSlot.setStatus("current")
_SpeedDuallineFCPortXCVPort_Type = Integer32
_SpeedDuallineFCPortXCVPort_Object = MibTableColumn
speedDuallineFCPortXCVPort = _SpeedDuallineFCPortXCVPort_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 3, 3, 5, 1, 3),
    _SpeedDuallineFCPortXCVPort_Type()
)
speedDuallineFCPortXCVPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    speedDuallineFCPortXCVPort.setStatus("current")


class _SpeedDuallineFCPortXCVVendorName_Type(DisplayString):
    """Custom type speedDuallineFCPortXCVVendorName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_SpeedDuallineFCPortXCVVendorName_Type.__name__ = "DisplayString"
_SpeedDuallineFCPortXCVVendorName_Object = MibTableColumn
speedDuallineFCPortXCVVendorName = _SpeedDuallineFCPortXCVVendorName_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 3, 3, 5, 1, 4),
    _SpeedDuallineFCPortXCVVendorName_Type()
)
speedDuallineFCPortXCVVendorName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    speedDuallineFCPortXCVVendorName.setStatus("current")


class _SpeedDuallineFCPortXCVVendorPartNumber_Type(DisplayString):
    """Custom type speedDuallineFCPortXCVVendorPartNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_SpeedDuallineFCPortXCVVendorPartNumber_Type.__name__ = "DisplayString"
_SpeedDuallineFCPortXCVVendorPartNumber_Object = MibTableColumn
speedDuallineFCPortXCVVendorPartNumber = _SpeedDuallineFCPortXCVVendorPartNumber_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 3, 3, 5, 1, 5),
    _SpeedDuallineFCPortXCVVendorPartNumber_Type()
)
speedDuallineFCPortXCVVendorPartNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    speedDuallineFCPortXCVVendorPartNumber.setStatus("current")


class _SpeedDuallineFCPortXCVVendorSerialNumber_Type(DisplayString):
    """Custom type speedDuallineFCPortXCVVendorSerialNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_SpeedDuallineFCPortXCVVendorSerialNumber_Type.__name__ = "DisplayString"
_SpeedDuallineFCPortXCVVendorSerialNumber_Object = MibTableColumn
speedDuallineFCPortXCVVendorSerialNumber = _SpeedDuallineFCPortXCVVendorSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 3, 3, 5, 1, 6),
    _SpeedDuallineFCPortXCVVendorSerialNumber_Type()
)
speedDuallineFCPortXCVVendorSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    speedDuallineFCPortXCVVendorSerialNumber.setStatus("current")


class _SpeedDuallineFCPortXCVType_Type(Integer32):
    """Custom type speedDuallineFCPortXCVType based on Integer32"""
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
              254,
              255)
        )
    )
    namedValues = NamedValues(
        *(("unspecified", 0),
          ("tGBIC", 1),
          ("tModuleSolderedToMotherboard", 2),
          ("tSFPTransceiver", 3),
          ("t300PinXBI", 4),
          ("tXENPAK", 5),
          ("tXFP", 6),
          ("tXFF", 7),
          ("tXFP-E", 8),
          ("tXPAK", 9),
          ("tX2", 10),
          ("tDWDMSFPTransceiver", 11),
          ("tCopperSFPTransceiver", 254),
          ("vendorSpecific", 255))
    )


_SpeedDuallineFCPortXCVType_Type.__name__ = "Integer32"
_SpeedDuallineFCPortXCVType_Object = MibTableColumn
speedDuallineFCPortXCVType = _SpeedDuallineFCPortXCVType_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 3, 3, 5, 1, 7),
    _SpeedDuallineFCPortXCVType_Type()
)
speedDuallineFCPortXCVType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    speedDuallineFCPortXCVType.setStatus("current")


class _SpeedDuallineFCPortXCVConnector_Type(Integer32):
    """Custom type speedDuallineFCPortXCVConnector based on Integer32"""
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
              32,
              33,
              34,
              255)
        )
    )
    namedValues = NamedValues(
        *(("unspecified", 0),
          ("cSC", 1),
          ("cFibreChannelStyle1CopperConnector", 2),
          ("cFibreChannelStyle2CopperConnector", 3),
          ("cBncTnc", 4),
          ("cFibreChannerCoaxialHeader", 5),
          ("cFibreJack", 6),
          ("cLC", 7),
          ("cMTRJ", 8),
          ("cMU", 9),
          ("cSG", 10),
          ("cOpticalPigtail", 11),
          ("cHSSDCII", 32),
          ("cCopperPigtail", 33),
          ("cRJ45", 34),
          ("unknown", 255))
    )


_SpeedDuallineFCPortXCVConnector_Type.__name__ = "Integer32"
_SpeedDuallineFCPortXCVConnector_Object = MibTableColumn
speedDuallineFCPortXCVConnector = _SpeedDuallineFCPortXCVConnector_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 3, 3, 5, 1, 8),
    _SpeedDuallineFCPortXCVConnector_Type()
)
speedDuallineFCPortXCVConnector.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    speedDuallineFCPortXCVConnector.setStatus("current")
_SpeedDuallineFCPortXCVWavelength_Type = Integer32
_SpeedDuallineFCPortXCVWavelength_Object = MibTableColumn
speedDuallineFCPortXCVWavelength = _SpeedDuallineFCPortXCVWavelength_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 3, 3, 5, 1, 9),
    _SpeedDuallineFCPortXCVWavelength_Type()
)
speedDuallineFCPortXCVWavelength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    speedDuallineFCPortXCVWavelength.setStatus("current")


class _SpeedDuallineFCPortXCVDMIState_Type(Integer32):
    """Custom type speedDuallineFCPortXCVDMIState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              253,
              254,
              255)
        )
    )
    namedValues = NamedValues(
        *(("notAvailable", 0),
          ("sff8472V93", 1),
          ("sff8472V95", 2),
          ("sff8472V102", 3),
          ("sff8472V104", 4),
          ("sff8472V11", 5),
          ("dmiAvailable", 253),
          ("notImplemented", 254),
          ("unknown", 255))
    )


_SpeedDuallineFCPortXCVDMIState_Type.__name__ = "Integer32"
_SpeedDuallineFCPortXCVDMIState_Object = MibTableColumn
speedDuallineFCPortXCVDMIState = _SpeedDuallineFCPortXCVDMIState_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 3, 3, 5, 1, 10),
    _SpeedDuallineFCPortXCVDMIState_Type()
)
speedDuallineFCPortXCVDMIState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    speedDuallineFCPortXCVDMIState.setStatus("current")
_SpeedDuallineFCXCVFeatureTable_Object = MibTable
speedDuallineFCXCVFeatureTable = _SpeedDuallineFCXCVFeatureTable_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 3, 3, 6)
)
if mibBuilder.loadTexts:
    speedDuallineFCXCVFeatureTable.setStatus("current")
_SpeedDuallineFCXCVFeatureEntry_Object = MibTableRow
speedDuallineFCXCVFeatureEntry = _SpeedDuallineFCXCVFeatureEntry_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 3, 3, 6, 1)
)
speedDuallineFCXCVFeatureEntry.setIndexNames(
    (0, "SPEED-DUALLINE-FC", "speedDuallineFCPortXCVFIndex"),
)
if mibBuilder.loadTexts:
    speedDuallineFCXCVFeatureEntry.setStatus("current")


class _SpeedDuallineFCPortXCVFIndex_Type(Integer32):
    """Custom type speedDuallineFCPortXCVFIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1900),
    )


_SpeedDuallineFCPortXCVFIndex_Type.__name__ = "Integer32"
_SpeedDuallineFCPortXCVFIndex_Object = MibTableColumn
speedDuallineFCPortXCVFIndex = _SpeedDuallineFCPortXCVFIndex_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 3, 3, 6, 1, 1),
    _SpeedDuallineFCPortXCVFIndex_Type()
)
speedDuallineFCPortXCVFIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    speedDuallineFCPortXCVFIndex.setStatus("current")
_SpeedDuallineFCPortXCVFSlot_Type = Integer32
_SpeedDuallineFCPortXCVFSlot_Object = MibTableColumn
speedDuallineFCPortXCVFSlot = _SpeedDuallineFCPortXCVFSlot_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 3, 3, 6, 1, 2),
    _SpeedDuallineFCPortXCVFSlot_Type()
)
speedDuallineFCPortXCVFSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    speedDuallineFCPortXCVFSlot.setStatus("current")
_SpeedDuallineFCPortXCVFPort_Type = Integer32
_SpeedDuallineFCPortXCVFPort_Object = MibTableColumn
speedDuallineFCPortXCVFPort = _SpeedDuallineFCPortXCVFPort_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 3, 3, 6, 1, 3),
    _SpeedDuallineFCPortXCVFPort_Type()
)
speedDuallineFCPortXCVFPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    speedDuallineFCPortXCVFPort.setStatus("current")


class _SpeedDuallineFCPortXCVBitrateMax_Type(Integer32):
    """Custom type speedDuallineFCPortXCVBitrateMax based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            0
        )
    )
    namedValues = NamedValues(
        ("unspecified", 0)
    )


_SpeedDuallineFCPortXCVBitrateMax_Type.__name__ = "Integer32"
_SpeedDuallineFCPortXCVBitrateMax_Object = MibTableColumn
speedDuallineFCPortXCVBitrateMax = _SpeedDuallineFCPortXCVBitrateMax_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 3, 3, 6, 1, 4),
    _SpeedDuallineFCPortXCVBitrateMax_Type()
)
speedDuallineFCPortXCVBitrateMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    speedDuallineFCPortXCVBitrateMax.setStatus("current")


class _SpeedDuallineFCPortXCVBitrateMin_Type(Integer32):
    """Custom type speedDuallineFCPortXCVBitrateMin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            0
        )
    )
    namedValues = NamedValues(
        ("unspecified", 0)
    )


_SpeedDuallineFCPortXCVBitrateMin_Type.__name__ = "Integer32"
_SpeedDuallineFCPortXCVBitrateMin_Object = MibTableColumn
speedDuallineFCPortXCVBitrateMin = _SpeedDuallineFCPortXCVBitrateMin_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 3, 3, 6, 1, 5),
    _SpeedDuallineFCPortXCVBitrateMin_Type()
)
speedDuallineFCPortXCVBitrateMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    speedDuallineFCPortXCVBitrateMin.setStatus("current")
_SpeedDuallineFCPortXCVLengthSMkm_Type = Integer32
_SpeedDuallineFCPortXCVLengthSMkm_Object = MibTableColumn
speedDuallineFCPortXCVLengthSMkm = _SpeedDuallineFCPortXCVLengthSMkm_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 3, 3, 6, 1, 6),
    _SpeedDuallineFCPortXCVLengthSMkm_Type()
)
speedDuallineFCPortXCVLengthSMkm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    speedDuallineFCPortXCVLengthSMkm.setStatus("current")
_SpeedDuallineFCPortXCVLength50_Type = Integer32
_SpeedDuallineFCPortXCVLength50_Object = MibTableColumn
speedDuallineFCPortXCVLength50 = _SpeedDuallineFCPortXCVLength50_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 3, 3, 6, 1, 7),
    _SpeedDuallineFCPortXCVLength50_Type()
)
speedDuallineFCPortXCVLength50.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    speedDuallineFCPortXCVLength50.setStatus("current")
_SpeedDuallineFCPortXCVLength62_Type = Integer32
_SpeedDuallineFCPortXCVLength62_Object = MibTableColumn
speedDuallineFCPortXCVLength62 = _SpeedDuallineFCPortXCVLength62_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 3, 3, 6, 1, 8),
    _SpeedDuallineFCPortXCVLength62_Type()
)
speedDuallineFCPortXCVLength62.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    speedDuallineFCPortXCVLength62.setStatus("current")
_SpeedDuallineFCPortXCVLengthCopper_Type = Integer32
_SpeedDuallineFCPortXCVLengthCopper_Object = MibTableColumn
speedDuallineFCPortXCVLengthCopper = _SpeedDuallineFCPortXCVLengthCopper_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 3, 3, 6, 1, 9),
    _SpeedDuallineFCPortXCVLengthCopper_Type()
)
speedDuallineFCPortXCVLengthCopper.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    speedDuallineFCPortXCVLengthCopper.setStatus("current")
_SpeedDuallineFCXCVMeassurementTable_Object = MibTable
speedDuallineFCXCVMeassurementTable = _SpeedDuallineFCXCVMeassurementTable_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 3, 3, 7)
)
if mibBuilder.loadTexts:
    speedDuallineFCXCVMeassurementTable.setStatus("current")
_SpeedDuallineFCXCVMeassurementEntry_Object = MibTableRow
speedDuallineFCXCVMeassurementEntry = _SpeedDuallineFCXCVMeassurementEntry_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 3, 3, 7, 1)
)
speedDuallineFCXCVMeassurementEntry.setIndexNames(
    (0, "SPEED-DUALLINE-FC", "speedDuallineFCPortXCVDMIIndex"),
)
if mibBuilder.loadTexts:
    speedDuallineFCXCVMeassurementEntry.setStatus("current")


class _SpeedDuallineFCPortXCVDMIIndex_Type(Integer32):
    """Custom type speedDuallineFCPortXCVDMIIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1900),
    )


_SpeedDuallineFCPortXCVDMIIndex_Type.__name__ = "Integer32"
_SpeedDuallineFCPortXCVDMIIndex_Object = MibTableColumn
speedDuallineFCPortXCVDMIIndex = _SpeedDuallineFCPortXCVDMIIndex_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 3, 3, 7, 1, 1),
    _SpeedDuallineFCPortXCVDMIIndex_Type()
)
speedDuallineFCPortXCVDMIIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    speedDuallineFCPortXCVDMIIndex.setStatus("current")
_SpeedDuallineFCPortXCVDMISlot_Type = Integer32
_SpeedDuallineFCPortXCVDMISlot_Object = MibTableColumn
speedDuallineFCPortXCVDMISlot = _SpeedDuallineFCPortXCVDMISlot_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 3, 3, 7, 1, 2),
    _SpeedDuallineFCPortXCVDMISlot_Type()
)
speedDuallineFCPortXCVDMISlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    speedDuallineFCPortXCVDMISlot.setStatus("current")
_SpeedDuallineFCPortXCVDMIPort_Type = Integer32
_SpeedDuallineFCPortXCVDMIPort_Object = MibTableColumn
speedDuallineFCPortXCVDMIPort = _SpeedDuallineFCPortXCVDMIPort_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 3, 3, 7, 1, 3),
    _SpeedDuallineFCPortXCVDMIPort_Type()
)
speedDuallineFCPortXCVDMIPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    speedDuallineFCPortXCVDMIPort.setStatus("current")
_SpeedDuallineFCPortXCVDMIRxLevel_Type = Integer32
_SpeedDuallineFCPortXCVDMIRxLevel_Object = MibTableColumn
speedDuallineFCPortXCVDMIRxLevel = _SpeedDuallineFCPortXCVDMIRxLevel_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 3, 3, 7, 1, 4),
    _SpeedDuallineFCPortXCVDMIRxLevel_Type()
)
speedDuallineFCPortXCVDMIRxLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    speedDuallineFCPortXCVDMIRxLevel.setStatus("current")
_SpeedDuallineFCPortXCVDMITxLevel_Type = Integer32
_SpeedDuallineFCPortXCVDMITxLevel_Object = MibTableColumn
speedDuallineFCPortXCVDMITxLevel = _SpeedDuallineFCPortXCVDMITxLevel_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 3, 3, 7, 1, 5),
    _SpeedDuallineFCPortXCVDMITxLevel_Type()
)
speedDuallineFCPortXCVDMITxLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    speedDuallineFCPortXCVDMITxLevel.setStatus("current")
_SpeedDuallineFCPortXCVDMITxBias_Type = Integer32
_SpeedDuallineFCPortXCVDMITxBias_Object = MibTableColumn
speedDuallineFCPortXCVDMITxBias = _SpeedDuallineFCPortXCVDMITxBias_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 3, 3, 7, 1, 6),
    _SpeedDuallineFCPortXCVDMITxBias_Type()
)
speedDuallineFCPortXCVDMITxBias.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    speedDuallineFCPortXCVDMITxBias.setStatus("current")
_SpeedDuallineFCPortXCVDMITemp_Type = Integer32
_SpeedDuallineFCPortXCVDMITemp_Object = MibTableColumn
speedDuallineFCPortXCVDMITemp = _SpeedDuallineFCPortXCVDMITemp_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 3, 3, 7, 1, 7),
    _SpeedDuallineFCPortXCVDMITemp_Type()
)
speedDuallineFCPortXCVDMITemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    speedDuallineFCPortXCVDMITemp.setStatus("current")
_SpeedDuallineFCXCVAlarmTable_Object = MibTable
speedDuallineFCXCVAlarmTable = _SpeedDuallineFCXCVAlarmTable_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 3, 3, 8)
)
if mibBuilder.loadTexts:
    speedDuallineFCXCVAlarmTable.setStatus("current")
_SpeedDuallineFCXCVAlarmEntry_Object = MibTableRow
speedDuallineFCXCVAlarmEntry = _SpeedDuallineFCXCVAlarmEntry_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 3, 3, 8, 1)
)
speedDuallineFCXCVAlarmEntry.setIndexNames(
    (0, "SPEED-DUALLINE-FC", "speedDuallineFCPortAIndex"),
)
if mibBuilder.loadTexts:
    speedDuallineFCXCVAlarmEntry.setStatus("current")


class _SpeedDuallineFCPortAIndex_Type(Integer32):
    """Custom type speedDuallineFCPortAIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1900),
    )


_SpeedDuallineFCPortAIndex_Type.__name__ = "Integer32"
_SpeedDuallineFCPortAIndex_Object = MibTableColumn
speedDuallineFCPortAIndex = _SpeedDuallineFCPortAIndex_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 3, 3, 8, 1, 1),
    _SpeedDuallineFCPortAIndex_Type()
)
speedDuallineFCPortAIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    speedDuallineFCPortAIndex.setStatus("current")
_SpeedDuallineFCPortASlot_Type = Integer32
_SpeedDuallineFCPortASlot_Object = MibTableColumn
speedDuallineFCPortASlot = _SpeedDuallineFCPortASlot_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 3, 3, 8, 1, 2),
    _SpeedDuallineFCPortASlot_Type()
)
speedDuallineFCPortASlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    speedDuallineFCPortASlot.setStatus("current")
_SpeedDuallineFCPortAPort_Type = Integer32
_SpeedDuallineFCPortAPort_Object = MibTableColumn
speedDuallineFCPortAPort = _SpeedDuallineFCPortAPort_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 3, 3, 8, 1, 3),
    _SpeedDuallineFCPortAPort_Type()
)
speedDuallineFCPortAPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    speedDuallineFCPortAPort.setStatus("current")


class _SpeedDuallineFCPortXCVDMIRxPowerAlarm_Type(Integer32):
    """Custom type speedDuallineFCPortXCVDMIRxPowerAlarm based on Integer32"""
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
        *(("notAvailiable", 0),
          ("noAlarm", 1),
          ("rxLowWarning", 2),
          ("rxLowAlarm", 3),
          ("rxHighAlarm", 4),
          ("unknown", 255))
    )


_SpeedDuallineFCPortXCVDMIRxPowerAlarm_Type.__name__ = "Integer32"
_SpeedDuallineFCPortXCVDMIRxPowerAlarm_Object = MibTableColumn
speedDuallineFCPortXCVDMIRxPowerAlarm = _SpeedDuallineFCPortXCVDMIRxPowerAlarm_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 3, 3, 8, 1, 4),
    _SpeedDuallineFCPortXCVDMIRxPowerAlarm_Type()
)
speedDuallineFCPortXCVDMIRxPowerAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    speedDuallineFCPortXCVDMIRxPowerAlarm.setStatus("current")


class _SpeedDuallineFCPortXCVDMITxLowAlarm_Type(Integer32):
    """Custom type speedDuallineFCPortXCVDMITxLowAlarm based on Integer32"""
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


_SpeedDuallineFCPortXCVDMITxLowAlarm_Type.__name__ = "Integer32"
_SpeedDuallineFCPortXCVDMITxLowAlarm_Object = MibTableColumn
speedDuallineFCPortXCVDMITxLowAlarm = _SpeedDuallineFCPortXCVDMITxLowAlarm_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 3, 3, 8, 1, 5),
    _SpeedDuallineFCPortXCVDMITxLowAlarm_Type()
)
speedDuallineFCPortXCVDMITxLowAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    speedDuallineFCPortXCVDMITxLowAlarm.setStatus("current")


class _SpeedDuallineFCPortXCVDMIBiasAlarmEvent_Type(Integer32):
    """Custom type speedDuallineFCPortXCVDMIBiasAlarmEvent based on Integer32"""
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


_SpeedDuallineFCPortXCVDMIBiasAlarmEvent_Type.__name__ = "Integer32"
_SpeedDuallineFCPortXCVDMIBiasAlarmEvent_Object = MibTableColumn
speedDuallineFCPortXCVDMIBiasAlarmEvent = _SpeedDuallineFCPortXCVDMIBiasAlarmEvent_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 3, 3, 8, 1, 6),
    _SpeedDuallineFCPortXCVDMIBiasAlarmEvent_Type()
)
speedDuallineFCPortXCVDMIBiasAlarmEvent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    speedDuallineFCPortXCVDMIBiasAlarmEvent.setStatus("current")


class _SpeedDuallineFCPortXCVDWDMLaserTempAlarmEvent_Type(Integer32):
    """Custom type speedDuallineFCPortXCVDWDMLaserTempAlarmEvent based on Integer32"""
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
          ("lowAlarm", 2),
          ("highAlarm", 3),
          ("unknown", 255))
    )


_SpeedDuallineFCPortXCVDWDMLaserTempAlarmEvent_Type.__name__ = "Integer32"
_SpeedDuallineFCPortXCVDWDMLaserTempAlarmEvent_Object = MibTableColumn
speedDuallineFCPortXCVDWDMLaserTempAlarmEvent = _SpeedDuallineFCPortXCVDWDMLaserTempAlarmEvent_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 3, 3, 8, 1, 7),
    _SpeedDuallineFCPortXCVDWDMLaserTempAlarmEvent_Type()
)
speedDuallineFCPortXCVDWDMLaserTempAlarmEvent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    speedDuallineFCPortXCVDWDMLaserTempAlarmEvent.setStatus("current")


class _SpeedDuallineFCPortXCVDWDMTECAlarmEvent_Type(Integer32):
    """Custom type speedDuallineFCPortXCVDWDMTECAlarmEvent based on Integer32"""
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


_SpeedDuallineFCPortXCVDWDMTECAlarmEvent_Type.__name__ = "Integer32"
_SpeedDuallineFCPortXCVDWDMTECAlarmEvent_Object = MibTableColumn
speedDuallineFCPortXCVDWDMTECAlarmEvent = _SpeedDuallineFCPortXCVDWDMTECAlarmEvent_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 3, 3, 8, 1, 8),
    _SpeedDuallineFCPortXCVDWDMTECAlarmEvent_Type()
)
speedDuallineFCPortXCVDWDMTECAlarmEvent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    speedDuallineFCPortXCVDWDMTECAlarmEvent.setStatus("current")


class _SpeedDuallineFCPortXCVTempHighAlarm_Type(Integer32):
    """Custom type speedDuallineFCPortXCVTempHighAlarm based on Integer32"""
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


_SpeedDuallineFCPortXCVTempHighAlarm_Type.__name__ = "Integer32"
_SpeedDuallineFCPortXCVTempHighAlarm_Object = MibTableColumn
speedDuallineFCPortXCVTempHighAlarm = _SpeedDuallineFCPortXCVTempHighAlarm_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 3, 3, 8, 1, 9),
    _SpeedDuallineFCPortXCVTempHighAlarm_Type()
)
speedDuallineFCPortXCVTempHighAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    speedDuallineFCPortXCVTempHighAlarm.setStatus("current")


class _SpeedDuallineFCPortXCVCDRALARM_Type(Integer32):
    """Custom type speedDuallineFCPortXCVCDRALARM based on Integer32"""
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


_SpeedDuallineFCPortXCVCDRALARM_Type.__name__ = "Integer32"
_SpeedDuallineFCPortXCVCDRALARM_Object = MibTableColumn
speedDuallineFCPortXCVCDRALARM = _SpeedDuallineFCPortXCVCDRALARM_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 3, 3, 8, 1, 10),
    _SpeedDuallineFCPortXCVCDRALARM_Type()
)
speedDuallineFCPortXCVCDRALARM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    speedDuallineFCPortXCVCDRALARM.setStatus("current")


class _SpeedDuallineFCPortXCVTuningAlarm_Type(Integer32):
    """Custom type speedDuallineFCPortXCVTuningAlarm based on Integer32"""
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
        *(("notAvailiable", 0),
          ("noAlarm", 1),
          ("activeAlarm", 2),
          ("notImplemented", 254),
          ("unknown", 255))
    )


_SpeedDuallineFCPortXCVTuningAlarm_Type.__name__ = "Integer32"
_SpeedDuallineFCPortXCVTuningAlarm_Object = MibTableColumn
speedDuallineFCPortXCVTuningAlarm = _SpeedDuallineFCPortXCVTuningAlarm_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 3, 3, 8, 1, 11),
    _SpeedDuallineFCPortXCVTuningAlarm_Type()
)
speedDuallineFCPortXCVTuningAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    speedDuallineFCPortXCVTuningAlarm.setStatus("current")
_SpeedDuallineFCMBoardAlarmTable_Object = MibTable
speedDuallineFCMBoardAlarmTable = _SpeedDuallineFCMBoardAlarmTable_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 3, 3, 9)
)
if mibBuilder.loadTexts:
    speedDuallineFCMBoardAlarmTable.setStatus("current")
_SpeedDuallineFCMBoardAlarmEntry_Object = MibTableRow
speedDuallineFCMBoardAlarmEntry = _SpeedDuallineFCMBoardAlarmEntry_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 3, 3, 9, 1)
)
speedDuallineFCMBoardAlarmEntry.setIndexNames(
    (0, "SPEED-DUALLINE-FC", "speedDuallineFCMBoardSlot"),
)
if mibBuilder.loadTexts:
    speedDuallineFCMBoardAlarmEntry.setStatus("current")


class _SpeedDuallineFCMBoardSlot_Type(Integer32):
    """Custom type speedDuallineFCMBoardSlot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 19),
    )


_SpeedDuallineFCMBoardSlot_Type.__name__ = "Integer32"
_SpeedDuallineFCMBoardSlot_Object = MibTableColumn
speedDuallineFCMBoardSlot = _SpeedDuallineFCMBoardSlot_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 3, 3, 9, 1, 2),
    _SpeedDuallineFCMBoardSlot_Type()
)
speedDuallineFCMBoardSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    speedDuallineFCMBoardSlot.setStatus("current")


class _SpeedDuallineFCMBoardTempAlarm_Type(Integer32):
    """Custom type speedDuallineFCMBoardTempAlarm based on Integer32"""
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


_SpeedDuallineFCMBoardTempAlarm_Type.__name__ = "Integer32"
_SpeedDuallineFCMBoardTempAlarm_Object = MibTableColumn
speedDuallineFCMBoardTempAlarm = _SpeedDuallineFCMBoardTempAlarm_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 3, 3, 9, 1, 3),
    _SpeedDuallineFCMBoardTempAlarm_Type()
)
speedDuallineFCMBoardTempAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    speedDuallineFCMBoardTempAlarm.setStatus("current")
_SpeedDuallineFCXCVTunableTable_Object = MibTable
speedDuallineFCXCVTunableTable = _SpeedDuallineFCXCVTunableTable_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 3, 3, 10)
)
if mibBuilder.loadTexts:
    speedDuallineFCXCVTunableTable.setStatus("current")
_SpeedDuallineFCXCVTunableEntry_Object = MibTableRow
speedDuallineFCXCVTunableEntry = _SpeedDuallineFCXCVTunableEntry_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 3, 3, 10, 1)
)
speedDuallineFCXCVTunableEntry.setIndexNames(
    (0, "SPEED-DUALLINE-FC", "speedDuallineFCPortXCVTunIndex"),
)
if mibBuilder.loadTexts:
    speedDuallineFCXCVTunableEntry.setStatus("current")


class _SpeedDuallineFCPortXCVTunIndex_Type(Integer32):
    """Custom type speedDuallineFCPortXCVTunIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1900),
    )


_SpeedDuallineFCPortXCVTunIndex_Type.__name__ = "Integer32"
_SpeedDuallineFCPortXCVTunIndex_Object = MibTableColumn
speedDuallineFCPortXCVTunIndex = _SpeedDuallineFCPortXCVTunIndex_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 3, 3, 10, 1, 1),
    _SpeedDuallineFCPortXCVTunIndex_Type()
)
speedDuallineFCPortXCVTunIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    speedDuallineFCPortXCVTunIndex.setStatus("current")
_SpeedDuallineFCPortXCVTunSlot_Type = Integer32
_SpeedDuallineFCPortXCVTunSlot_Object = MibTableColumn
speedDuallineFCPortXCVTunSlot = _SpeedDuallineFCPortXCVTunSlot_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 3, 3, 10, 1, 2),
    _SpeedDuallineFCPortXCVTunSlot_Type()
)
speedDuallineFCPortXCVTunSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    speedDuallineFCPortXCVTunSlot.setStatus("current")
_SpeedDuallineFCPortXCVTunPort_Type = Integer32
_SpeedDuallineFCPortXCVTunPort_Object = MibTableColumn
speedDuallineFCPortXCVTunPort = _SpeedDuallineFCPortXCVTunPort_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 3, 3, 10, 1, 3),
    _SpeedDuallineFCPortXCVTunPort_Type()
)
speedDuallineFCPortXCVTunPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    speedDuallineFCPortXCVTunPort.setStatus("current")
_SpeedDuallineFCPortXCVChannelSpacing_Type = Integer32
_SpeedDuallineFCPortXCVChannelSpacing_Object = MibTableColumn
speedDuallineFCPortXCVChannelSpacing = _SpeedDuallineFCPortXCVChannelSpacing_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 3, 3, 10, 1, 4),
    _SpeedDuallineFCPortXCVChannelSpacing_Type()
)
speedDuallineFCPortXCVChannelSpacing.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    speedDuallineFCPortXCVChannelSpacing.setStatus("current")
_SpeedDuallineFCPortXCVNumberOfChannels_Type = Integer32
_SpeedDuallineFCPortXCVNumberOfChannels_Object = MibTableColumn
speedDuallineFCPortXCVNumberOfChannels = _SpeedDuallineFCPortXCVNumberOfChannels_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 3, 3, 10, 1, 5),
    _SpeedDuallineFCPortXCVNumberOfChannels_Type()
)
speedDuallineFCPortXCVNumberOfChannels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    speedDuallineFCPortXCVNumberOfChannels.setStatus("current")
_SpeedDuallineFCPortXCVCenterWavlength_Type = Integer32
_SpeedDuallineFCPortXCVCenterWavlength_Object = MibTableColumn
speedDuallineFCPortXCVCenterWavlength = _SpeedDuallineFCPortXCVCenterWavlength_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 3, 3, 10, 1, 6),
    _SpeedDuallineFCPortXCVCenterWavlength_Type()
)
speedDuallineFCPortXCVCenterWavlength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    speedDuallineFCPortXCVCenterWavlength.setStatus("current")


class _SpeedDuallineFCPortXCVTunableFeature_Type(Integer32):
    """Custom type speedDuallineFCPortXCVTunableFeature based on Integer32"""
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


_SpeedDuallineFCPortXCVTunableFeature_Type.__name__ = "Integer32"
_SpeedDuallineFCPortXCVTunableFeature_Object = MibTableColumn
speedDuallineFCPortXCVTunableFeature = _SpeedDuallineFCPortXCVTunableFeature_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 3, 3, 10, 1, 7),
    _SpeedDuallineFCPortXCVTunableFeature_Type()
)
speedDuallineFCPortXCVTunableFeature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    speedDuallineFCPortXCVTunableFeature.setStatus("current")


class _SpeedDuallineFCPortXCVTunableMinMaxChannel_Type(DisplayString):
    """Custom type speedDuallineFCPortXCVTunableMinMaxChannel based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 9),
    )


_SpeedDuallineFCPortXCVTunableMinMaxChannel_Type.__name__ = "DisplayString"
_SpeedDuallineFCPortXCVTunableMinMaxChannel_Object = MibTableColumn
speedDuallineFCPortXCVTunableMinMaxChannel = _SpeedDuallineFCPortXCVTunableMinMaxChannel_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 3, 3, 10, 1, 8),
    _SpeedDuallineFCPortXCVTunableMinMaxChannel_Type()
)
speedDuallineFCPortXCVTunableMinMaxChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    speedDuallineFCPortXCVTunableMinMaxChannel.setStatus("current")
_SpeedDuallineFCPortXCVTunableWavelengthConfig_Type = Integer32
_SpeedDuallineFCPortXCVTunableWavelengthConfig_Object = MibTableColumn
speedDuallineFCPortXCVTunableWavelengthConfig = _SpeedDuallineFCPortXCVTunableWavelengthConfig_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 3, 3, 10, 1, 9),
    _SpeedDuallineFCPortXCVTunableWavelengthConfig_Type()
)
speedDuallineFCPortXCVTunableWavelengthConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    speedDuallineFCPortXCVTunableWavelengthConfig.setStatus("current")


class _SpeedDuallineFCPortXCVTunableChannelConfig_Type(DisplayString):
    """Custom type speedDuallineFCPortXCVTunableChannelConfig based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 4),
    )


_SpeedDuallineFCPortXCVTunableChannelConfig_Type.__name__ = "DisplayString"
_SpeedDuallineFCPortXCVTunableChannelConfig_Object = MibTableColumn
speedDuallineFCPortXCVTunableChannelConfig = _SpeedDuallineFCPortXCVTunableChannelConfig_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 3, 3, 10, 1, 10),
    _SpeedDuallineFCPortXCVTunableChannelConfig_Type()
)
speedDuallineFCPortXCVTunableChannelConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    speedDuallineFCPortXCVTunableChannelConfig.setStatus("current")


class _SpeedDuallineFCPortXCVTunableConfigSelection_Type(Integer32):
    """Custom type speedDuallineFCPortXCVTunableConfigSelection based on Integer32"""
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


_SpeedDuallineFCPortXCVTunableConfigSelection_Type.__name__ = "Integer32"
_SpeedDuallineFCPortXCVTunableConfigSelection_Object = MibTableColumn
speedDuallineFCPortXCVTunableConfigSelection = _SpeedDuallineFCPortXCVTunableConfigSelection_Object(
    (1, 3, 6, 1, 4, 1, 3652, 3, 3, 3, 10, 1, 11),
    _SpeedDuallineFCPortXCVTunableConfigSelection_Type()
)
speedDuallineFCPortXCVTunableConfigSelection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    speedDuallineFCPortXCVTunableConfigSelection.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SPEED-DUALLINE-FC",
    **{"speedDuallineFC": speedDuallineFC,
       "speedDuallineFCMOverviewTable": speedDuallineFCMOverviewTable,
       "speedDuallineFCMOverviewEntry": speedDuallineFCMOverviewEntry,
       "speedDuallineFCSlot": speedDuallineFCSlot,
       "speedDuallineFCMDevice": speedDuallineFCMDevice,
       "speedDuallineFCMState": speedDuallineFCMState,
       "speedDuallineFCMSysName": speedDuallineFCMSysName,
       "speedDuallineFCMSysUpTime": speedDuallineFCMSysUpTime,
       "speedDuallineFCMTemperature": speedDuallineFCMTemperature,
       "speedDuallineFCMAlarmState": speedDuallineFCMAlarmState,
       "speedDuallineFCMKernelImage": speedDuallineFCMKernelImage,
       "speedDuallineFCMAppImage": speedDuallineFCMAppImage,
       "speedDuallineFCMHwVersion": speedDuallineFCMHwVersion,
       "speedDuallineFCMSerialNumber": speedDuallineFCMSerialNumber,
       "speedDuallineFCMEthPortState": speedDuallineFCMEthPortState,
       "speedDuallineFCMUploadState": speedDuallineFCMUploadState,
       "speedDuallineFCMUpdateState": speedDuallineFCMUpdateState,
       "speedDuallineFCMConfigTable": speedDuallineFCMConfigTable,
       "speedDuallineFCMConfigEntry": speedDuallineFCMConfigEntry,
       "speedDuallineFCMSlot": speedDuallineFCMSlot,
       "speedDuallineFCMIpAddress": speedDuallineFCMIpAddress,
       "speedDuallineFCMIpNetmask": speedDuallineFCMIpNetmask,
       "speedDuallineFCMIpGateway": speedDuallineFCMIpGateway,
       "speedDuallineFCMTrapSink1": speedDuallineFCMTrapSink1,
       "speedDuallineFCMTrapSink2": speedDuallineFCMTrapSink2,
       "speedDuallineFCMTrapSink3": speedDuallineFCMTrapSink3,
       "speedDuallineFCMTrapSink4": speedDuallineFCMTrapSink4,
       "speedDuallineFCMTrapSink5": speedDuallineFCMTrapSink5,
       "speedDuallineFCMSNMPReadCommunity": speedDuallineFCMSNMPReadCommunity,
       "speedDuallineFCMSNMPWriteCommunity": speedDuallineFCMSNMPWriteCommunity,
       "speedDuallineFCMTempWarningLevel": speedDuallineFCMTempWarningLevel,
       "speedDuallineFCMTempAlarmLevel": speedDuallineFCMTempAlarmLevel,
       "speedDuallineFCMSNMPSyscontact": speedDuallineFCMSNMPSyscontact,
       "speedDuallineFCMSNMPSyslocation": speedDuallineFCMSNMPSyslocation,
       "speedDuallineFCMPortTxConnection": speedDuallineFCMPortTxConnection,
       "speedDuallineFCMUserTimeout": speedDuallineFCMUserTimeout,
       "speedDuallineFCMEthPortMode": speedDuallineFCMEthPortMode,
       "speedDuallineFCMAccess": speedDuallineFCMAccess,
       "speedDuallineFCMProtectionTable": speedDuallineFCMProtectionTable,
       "speedDuallineFCMProtectionEntry": speedDuallineFCMProtectionEntry,
       "speedDuallineFCMLinkProtectionSlot": speedDuallineFCMLinkProtectionSlot,
       "speedDuallineFCMLinkProtectionConfig": speedDuallineFCMLinkProtectionConfig,
       "speedDuallineFCMLinkProtectionState": speedDuallineFCMLinkProtectionState,
       "speedDuallineFCMLinkProtectionFallbackTime": speedDuallineFCMLinkProtectionFallbackTime,
       "speedDuallineFCMLinkProtectionRXLevelPort1": speedDuallineFCMLinkProtectionRXLevelPort1,
       "speedDuallineFCMLinkProtectionRXLevelPort2": speedDuallineFCMLinkProtectionRXLevelPort2,
       "speedDuallineFCMLinkProtectionClientPort": speedDuallineFCMLinkProtectionClientPort,
       "speedDuallineFCMLinkProtectionMode": speedDuallineFCMLinkProtectionMode,
       "speedDuallineFCPortOverviewTable": speedDuallineFCPortOverviewTable,
       "speedDuallineFCPortOverviewEntry": speedDuallineFCPortOverviewEntry,
       "speedDuallineFCPortIndex": speedDuallineFCPortIndex,
       "speedDuallineFCPortSlot": speedDuallineFCPortSlot,
       "speedDuallineFCPortPort": speedDuallineFCPortPort,
       "speedDuallineFCPortDescription": speedDuallineFCPortDescription,
       "speedDuallineFCPortAdminConfig": speedDuallineFCPortAdminConfig,
       "speedDuallineFCPortOperState": speedDuallineFCPortOperState,
       "speedDuallineFCPortXCVState": speedDuallineFCPortXCVState,
       "speedDuallineFCPortLLCFconfig": speedDuallineFCPortLLCFconfig,
       "speedDuallineFCPortLoopConfig": speedDuallineFCPortLoopConfig,
       "speedDuallineFCPortSpeedConfig": speedDuallineFCPortSpeedConfig,
       "speedDuallineFCPortAlarmState": speedDuallineFCPortAlarmState,
       "speedDuallineFCPortAlarmDeactivation": speedDuallineFCPortAlarmDeactivation,
       "speedDuallineFCPortAlarmSchedule": speedDuallineFCPortAlarmSchedule,
       "speedDuallineFCXCVOverviewTable": speedDuallineFCXCVOverviewTable,
       "speedDuallineFCXCVOverviewEntry": speedDuallineFCXCVOverviewEntry,
       "speedDuallineFCPortXCVIndex": speedDuallineFCPortXCVIndex,
       "speedDuallineFCPortXCVSlot": speedDuallineFCPortXCVSlot,
       "speedDuallineFCPortXCVPort": speedDuallineFCPortXCVPort,
       "speedDuallineFCPortXCVVendorName": speedDuallineFCPortXCVVendorName,
       "speedDuallineFCPortXCVVendorPartNumber": speedDuallineFCPortXCVVendorPartNumber,
       "speedDuallineFCPortXCVVendorSerialNumber": speedDuallineFCPortXCVVendorSerialNumber,
       "speedDuallineFCPortXCVType": speedDuallineFCPortXCVType,
       "speedDuallineFCPortXCVConnector": speedDuallineFCPortXCVConnector,
       "speedDuallineFCPortXCVWavelength": speedDuallineFCPortXCVWavelength,
       "speedDuallineFCPortXCVDMIState": speedDuallineFCPortXCVDMIState,
       "speedDuallineFCXCVFeatureTable": speedDuallineFCXCVFeatureTable,
       "speedDuallineFCXCVFeatureEntry": speedDuallineFCXCVFeatureEntry,
       "speedDuallineFCPortXCVFIndex": speedDuallineFCPortXCVFIndex,
       "speedDuallineFCPortXCVFSlot": speedDuallineFCPortXCVFSlot,
       "speedDuallineFCPortXCVFPort": speedDuallineFCPortXCVFPort,
       "speedDuallineFCPortXCVBitrateMax": speedDuallineFCPortXCVBitrateMax,
       "speedDuallineFCPortXCVBitrateMin": speedDuallineFCPortXCVBitrateMin,
       "speedDuallineFCPortXCVLengthSMkm": speedDuallineFCPortXCVLengthSMkm,
       "speedDuallineFCPortXCVLength50": speedDuallineFCPortXCVLength50,
       "speedDuallineFCPortXCVLength62": speedDuallineFCPortXCVLength62,
       "speedDuallineFCPortXCVLengthCopper": speedDuallineFCPortXCVLengthCopper,
       "speedDuallineFCXCVMeassurementTable": speedDuallineFCXCVMeassurementTable,
       "speedDuallineFCXCVMeassurementEntry": speedDuallineFCXCVMeassurementEntry,
       "speedDuallineFCPortXCVDMIIndex": speedDuallineFCPortXCVDMIIndex,
       "speedDuallineFCPortXCVDMISlot": speedDuallineFCPortXCVDMISlot,
       "speedDuallineFCPortXCVDMIPort": speedDuallineFCPortXCVDMIPort,
       "speedDuallineFCPortXCVDMIRxLevel": speedDuallineFCPortXCVDMIRxLevel,
       "speedDuallineFCPortXCVDMITxLevel": speedDuallineFCPortXCVDMITxLevel,
       "speedDuallineFCPortXCVDMITxBias": speedDuallineFCPortXCVDMITxBias,
       "speedDuallineFCPortXCVDMITemp": speedDuallineFCPortXCVDMITemp,
       "speedDuallineFCXCVAlarmTable": speedDuallineFCXCVAlarmTable,
       "speedDuallineFCXCVAlarmEntry": speedDuallineFCXCVAlarmEntry,
       "speedDuallineFCPortAIndex": speedDuallineFCPortAIndex,
       "speedDuallineFCPortASlot": speedDuallineFCPortASlot,
       "speedDuallineFCPortAPort": speedDuallineFCPortAPort,
       "speedDuallineFCPortXCVDMIRxPowerAlarm": speedDuallineFCPortXCVDMIRxPowerAlarm,
       "speedDuallineFCPortXCVDMITxLowAlarm": speedDuallineFCPortXCVDMITxLowAlarm,
       "speedDuallineFCPortXCVDMIBiasAlarmEvent": speedDuallineFCPortXCVDMIBiasAlarmEvent,
       "speedDuallineFCPortXCVDWDMLaserTempAlarmEvent": speedDuallineFCPortXCVDWDMLaserTempAlarmEvent,
       "speedDuallineFCPortXCVDWDMTECAlarmEvent": speedDuallineFCPortXCVDWDMTECAlarmEvent,
       "speedDuallineFCPortXCVTempHighAlarm": speedDuallineFCPortXCVTempHighAlarm,
       "speedDuallineFCPortXCVCDRALARM": speedDuallineFCPortXCVCDRALARM,
       "speedDuallineFCPortXCVTuningAlarm": speedDuallineFCPortXCVTuningAlarm,
       "speedDuallineFCMBoardAlarmTable": speedDuallineFCMBoardAlarmTable,
       "speedDuallineFCMBoardAlarmEntry": speedDuallineFCMBoardAlarmEntry,
       "speedDuallineFCMBoardSlot": speedDuallineFCMBoardSlot,
       "speedDuallineFCMBoardTempAlarm": speedDuallineFCMBoardTempAlarm,
       "speedDuallineFCXCVTunableTable": speedDuallineFCXCVTunableTable,
       "speedDuallineFCXCVTunableEntry": speedDuallineFCXCVTunableEntry,
       "speedDuallineFCPortXCVTunIndex": speedDuallineFCPortXCVTunIndex,
       "speedDuallineFCPortXCVTunSlot": speedDuallineFCPortXCVTunSlot,
       "speedDuallineFCPortXCVTunPort": speedDuallineFCPortXCVTunPort,
       "speedDuallineFCPortXCVChannelSpacing": speedDuallineFCPortXCVChannelSpacing,
       "speedDuallineFCPortXCVNumberOfChannels": speedDuallineFCPortXCVNumberOfChannels,
       "speedDuallineFCPortXCVCenterWavlength": speedDuallineFCPortXCVCenterWavlength,
       "speedDuallineFCPortXCVTunableFeature": speedDuallineFCPortXCVTunableFeature,
       "speedDuallineFCPortXCVTunableMinMaxChannel": speedDuallineFCPortXCVTunableMinMaxChannel,
       "speedDuallineFCPortXCVTunableWavelengthConfig": speedDuallineFCPortXCVTunableWavelengthConfig,
       "speedDuallineFCPortXCVTunableChannelConfig": speedDuallineFCPortXCVTunableChannelConfig,
       "speedDuallineFCPortXCVTunableConfigSelection": speedDuallineFCPortXCVTunableConfigSelection}
)
