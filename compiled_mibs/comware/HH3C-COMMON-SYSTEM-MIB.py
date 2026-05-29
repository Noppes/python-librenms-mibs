# SNMP MIB module (HH3C-COMMON-SYSTEM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\comware\HH3C-COMMON-SYSTEM-MIB

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

(hh3c,) = mibBuilder.importSymbols(
    "HH3C-OID-MIB",
    "hh3c")

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

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

(DateAndTime,
 DisplayString,
 PhysAddress,
 RowStatus,
 TextualConvention,
 TimeStamp) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TimeStamp")


# MODULE-IDENTITY

hh3cSystem = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 6)
)
if mibBuilder.loadTexts:
    hh3cSystem.setRevisions(
        ("2015-05-05 00:00",
         "2015-03-25 00:00",
         "2014-08-07 17:10",
         "2013-09-13 00:00",
         "2013-05-28 00:00",
         "2012-06-06 00:00",
         "2012-01-07 00:00",
         "2009-05-05 00:00",
         "2008-11-11 00:00",
         "2004-10-12 00:00",
         "2004-08-16 00:00",
         "2004-06-30 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs



class _Hh3cWriteConfig_Type(Integer32):
    """Custom type hh3cWriteConfig based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("save", 1)
    )


_Hh3cWriteConfig_Type.__name__ = "Integer32"
_Hh3cWriteConfig_Object = MibScalar
hh3cWriteConfig = _Hh3cWriteConfig_Object(
    (1, 3, 6, 1, 4, 1, 25506, 6, 5),
    _Hh3cWriteConfig_Type()
)
hh3cWriteConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cWriteConfig.setStatus("current")


class _Hh3cStartFtpServer_Type(Integer32):
    """Custom type hh3cStartFtpServer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_Hh3cStartFtpServer_Type.__name__ = "Integer32"
_Hh3cStartFtpServer_Object = MibScalar
hh3cStartFtpServer = _Hh3cStartFtpServer_Object(
    (1, 3, 6, 1, 4, 1, 25506, 6, 6),
    _Hh3cStartFtpServer_Type()
)
hh3cStartFtpServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cStartFtpServer.setStatus("current")


class _Hh3cReboot_Type(Integer32):
    """Custom type hh3cReboot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("normal", 0),
          ("reboot", 1))
    )


_Hh3cReboot_Type.__name__ = "Integer32"
_Hh3cReboot_Object = MibScalar
hh3cReboot = _Hh3cReboot_Object(
    (1, 3, 6, 1, 4, 1, 25506, 6, 7),
    _Hh3cReboot_Type()
)
hh3cReboot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cReboot.setStatus("current")
_Hh3cSystemNotification_ObjectIdentity = ObjectIdentity
hh3cSystemNotification = _Hh3cSystemNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 6, 8)
)
_Hh3cSoftwareVersion_Type = DisplayString
_Hh3cSoftwareVersion_Object = MibScalar
hh3cSoftwareVersion = _Hh3cSoftwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 25506, 6, 9),
    _Hh3cSoftwareVersion_Type()
)
hh3cSoftwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cSoftwareVersion.setStatus("current")


class _Hh3cSysBootType_Type(Integer32):
    """Custom type hh3cSysBootType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("coldStart", 1),
          ("warmStart", 2))
    )


_Hh3cSysBootType_Type.__name__ = "Integer32"
_Hh3cSysBootType_Object = MibScalar
hh3cSysBootType = _Hh3cSysBootType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 6, 10),
    _Hh3cSysBootType_Type()
)
hh3cSysBootType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cSysBootType.setStatus("current")
_Hh3cSystemInfo_ObjectIdentity = ObjectIdentity
hh3cSystemInfo = _Hh3cSystemInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 6, 11)
)


class _Hh3cSysStatisticPeriod_Type(Integer32):
    """Custom type hh3cSysStatisticPeriod based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 900),
    )


_Hh3cSysStatisticPeriod_Type.__name__ = "Integer32"
_Hh3cSysStatisticPeriod_Object = MibScalar
hh3cSysStatisticPeriod = _Hh3cSysStatisticPeriod_Object(
    (1, 3, 6, 1, 4, 1, 25506, 6, 11, 1),
    _Hh3cSysStatisticPeriod_Type()
)
hh3cSysStatisticPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cSysStatisticPeriod.setStatus("current")
if mibBuilder.loadTexts:
    hh3cSysStatisticPeriod.setUnits("seconds")


class _Hh3cSysSamplePeriod_Type(Integer32):
    """Custom type hh3cSysSamplePeriod based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 300),
    )


_Hh3cSysSamplePeriod_Type.__name__ = "Integer32"
_Hh3cSysSamplePeriod_Object = MibScalar
hh3cSysSamplePeriod = _Hh3cSysSamplePeriod_Object(
    (1, 3, 6, 1, 4, 1, 25506, 6, 11, 2),
    _Hh3cSysSamplePeriod_Type()
)
hh3cSysSamplePeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cSysSamplePeriod.setStatus("current")
if mibBuilder.loadTexts:
    hh3cSysSamplePeriod.setUnits("seconds")


class _Hh3cSysTrapResendPeriod_Type(Integer32):
    """Custom type hh3cSysTrapResendPeriod based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3600),
    )


_Hh3cSysTrapResendPeriod_Type.__name__ = "Integer32"
_Hh3cSysTrapResendPeriod_Object = MibScalar
hh3cSysTrapResendPeriod = _Hh3cSysTrapResendPeriod_Object(
    (1, 3, 6, 1, 4, 1, 25506, 6, 11, 3),
    _Hh3cSysTrapResendPeriod_Type()
)
hh3cSysTrapResendPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cSysTrapResendPeriod.setStatus("current")
if mibBuilder.loadTexts:
    hh3cSysTrapResendPeriod.setUnits("seconds")


class _Hh3cSysTrapCollectionPeriod_Type(Integer32):
    """Custom type hh3cSysTrapCollectionPeriod based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 60),
    )


_Hh3cSysTrapCollectionPeriod_Type.__name__ = "Integer32"
_Hh3cSysTrapCollectionPeriod_Object = MibScalar
hh3cSysTrapCollectionPeriod = _Hh3cSysTrapCollectionPeriod_Object(
    (1, 3, 6, 1, 4, 1, 25506, 6, 11, 4),
    _Hh3cSysTrapCollectionPeriod_Type()
)
hh3cSysTrapCollectionPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cSysTrapCollectionPeriod.setStatus("current")
if mibBuilder.loadTexts:
    hh3cSysTrapCollectionPeriod.setUnits("seconds")
_Hh3cSysSnmpPort_Type = Integer32
_Hh3cSysSnmpPort_Object = MibScalar
hh3cSysSnmpPort = _Hh3cSysSnmpPort_Object(
    (1, 3, 6, 1, 4, 1, 25506, 6, 11, 5),
    _Hh3cSysSnmpPort_Type()
)
hh3cSysSnmpPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cSysSnmpPort.setStatus("current")
_Hh3cSysSnmpTrapPort_Type = Integer32
_Hh3cSysSnmpTrapPort_Object = MibScalar
hh3cSysSnmpTrapPort = _Hh3cSysSnmpTrapPort_Object(
    (1, 3, 6, 1, 4, 1, 25506, 6, 11, 6),
    _Hh3cSysSnmpTrapPort_Type()
)
hh3cSysSnmpTrapPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cSysSnmpTrapPort.setStatus("current")


class _Hh3cSysNetID_Type(OctetString):
    """Custom type hh3cSysNetID based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_Hh3cSysNetID_Type.__name__ = "OctetString"
_Hh3cSysNetID_Object = MibScalar
hh3cSysNetID = _Hh3cSysNetID_Object(
    (1, 3, 6, 1, 4, 1, 25506, 6, 11, 7),
    _Hh3cSysNetID_Type()
)
hh3cSysNetID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cSysNetID.setStatus("current")
_Hh3cSysLastSampleTime_Type = DateAndTime
_Hh3cSysLastSampleTime_Object = MibScalar
hh3cSysLastSampleTime = _Hh3cSysLastSampleTime_Object(
    (1, 3, 6, 1, 4, 1, 25506, 6, 11, 8),
    _Hh3cSysLastSampleTime_Type()
)
hh3cSysLastSampleTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cSysLastSampleTime.setStatus("current")


class _Hh3cSysTrapSendNum_Type(Integer32):
    """Custom type hh3cSysTrapSendNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 24),
    )


_Hh3cSysTrapSendNum_Type.__name__ = "Integer32"
_Hh3cSysTrapSendNum_Object = MibScalar
hh3cSysTrapSendNum = _Hh3cSysTrapSendNum_Object(
    (1, 3, 6, 1, 4, 1, 25506, 6, 11, 9),
    _Hh3cSysTrapSendNum_Type()
)
hh3cSysTrapSendNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cSysTrapSendNum.setStatus("current")
_Hh3cSysFirstTrapTime_Type = TimeTicks
_Hh3cSysFirstTrapTime_Object = MibScalar
hh3cSysFirstTrapTime = _Hh3cSysFirstTrapTime_Object(
    (1, 3, 6, 1, 4, 1, 25506, 6, 11, 10),
    _Hh3cSysFirstTrapTime_Type()
)
hh3cSysFirstTrapTime.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cSysFirstTrapTime.setStatus("current")


class _Hh3cSysBannerMOTD_Type(OctetString):
    """Custom type hh3cSysBannerMOTD based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 2000),
    )


_Hh3cSysBannerMOTD_Type.__name__ = "OctetString"
_Hh3cSysBannerMOTD_Object = MibScalar
hh3cSysBannerMOTD = _Hh3cSysBannerMOTD_Object(
    (1, 3, 6, 1, 4, 1, 25506, 6, 11, 11),
    _Hh3cSysBannerMOTD_Type()
)
hh3cSysBannerMOTD.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cSysBannerMOTD.setStatus("current")
_Hh3cSystemNotificationInfo_ObjectIdentity = ObjectIdentity
hh3cSystemNotificationInfo = _Hh3cSystemNotificationInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 6, 12)
)
_Hh3cSysLoghostIndex_Type = Integer32
_Hh3cSysLoghostIndex_Object = MibScalar
hh3cSysLoghostIndex = _Hh3cSysLoghostIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 6, 12, 1),
    _Hh3cSysLoghostIndex_Type()
)
hh3cSysLoghostIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cSysLoghostIndex.setStatus("current")
_Hh3cSysLoghostIpaddressType_Type = InetAddressType
_Hh3cSysLoghostIpaddressType_Object = MibScalar
hh3cSysLoghostIpaddressType = _Hh3cSysLoghostIpaddressType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 6, 12, 2),
    _Hh3cSysLoghostIpaddressType_Type()
)
hh3cSysLoghostIpaddressType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cSysLoghostIpaddressType.setStatus("current")
_Hh3cSysLoghostIpaddress_Type = InetAddress
_Hh3cSysLoghostIpaddress_Object = MibScalar
hh3cSysLoghostIpaddress = _Hh3cSysLoghostIpaddress_Object(
    (1, 3, 6, 1, 4, 1, 25506, 6, 12, 3),
    _Hh3cSysLoghostIpaddress_Type()
)
hh3cSysLoghostIpaddress.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cSysLoghostIpaddress.setStatus("current")


class _Hh3cSysLoghostTrapVpnName_Type(DisplayString):
    """Custom type hh3cSysLoghostTrapVpnName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_Hh3cSysLoghostTrapVpnName_Type.__name__ = "DisplayString"
_Hh3cSysLoghostTrapVpnName_Object = MibScalar
hh3cSysLoghostTrapVpnName = _Hh3cSysLoghostTrapVpnName_Object(
    (1, 3, 6, 1, 4, 1, 25506, 6, 12, 4),
    _Hh3cSysLoghostTrapVpnName_Type()
)
hh3cSysLoghostTrapVpnName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cSysLoghostTrapVpnName.setStatus("current")
_Hh3cSystemDiagInfoTable_Object = MibTable
hh3cSystemDiagInfoTable = _Hh3cSystemDiagInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 6, 13)
)
if mibBuilder.loadTexts:
    hh3cSystemDiagInfoTable.setStatus("current")
_Hh3cSystemDiagInfoEntry_Object = MibTableRow
hh3cSystemDiagInfoEntry = _Hh3cSystemDiagInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 6, 13, 1)
)
hh3cSystemDiagInfoEntry.setIndexNames(
    (0, "HH3C-COMMON-SYSTEM-MIB", "hh3cSystemDiagInfoIndex"),
)
if mibBuilder.loadTexts:
    hh3cSystemDiagInfoEntry.setStatus("current")


class _Hh3cSystemDiagInfoIndex_Type(Integer32):
    """Custom type hh3cSystemDiagInfoIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Hh3cSystemDiagInfoIndex_Type.__name__ = "Integer32"
_Hh3cSystemDiagInfoIndex_Object = MibTableColumn
hh3cSystemDiagInfoIndex = _Hh3cSystemDiagInfoIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 6, 13, 1, 1),
    _Hh3cSystemDiagInfoIndex_Type()
)
hh3cSystemDiagInfoIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cSystemDiagInfoIndex.setStatus("current")


class _Hh3cSystemDiagInfoFilename_Type(DisplayString):
    """Custom type hh3cSystemDiagInfoFilename based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_Hh3cSystemDiagInfoFilename_Type.__name__ = "DisplayString"
_Hh3cSystemDiagInfoFilename_Object = MibTableColumn
hh3cSystemDiagInfoFilename = _Hh3cSystemDiagInfoFilename_Object(
    (1, 3, 6, 1, 4, 1, 25506, 6, 13, 1, 2),
    _Hh3cSystemDiagInfoFilename_Type()
)
hh3cSystemDiagInfoFilename.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cSystemDiagInfoFilename.setStatus("current")
_Hh3cSystemDiagInfoRowStatus_Type = RowStatus
_Hh3cSystemDiagInfoRowStatus_Object = MibTableColumn
hh3cSystemDiagInfoRowStatus = _Hh3cSystemDiagInfoRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 6, 13, 1, 3),
    _Hh3cSystemDiagInfoRowStatus_Type()
)
hh3cSystemDiagInfoRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cSystemDiagInfoRowStatus.setStatus("current")
_Hh3cSystemDiagInfoOperEndTime_Type = TimeStamp
_Hh3cSystemDiagInfoOperEndTime_Object = MibTableColumn
hh3cSystemDiagInfoOperEndTime = _Hh3cSystemDiagInfoOperEndTime_Object(
    (1, 3, 6, 1, 4, 1, 25506, 6, 13, 1, 4),
    _Hh3cSystemDiagInfoOperEndTime_Type()
)
hh3cSystemDiagInfoOperEndTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cSystemDiagInfoOperEndTime.setStatus("current")


class _Hh3cSystemDiagInfoOperState_Type(Integer32):
    """Custom type hh3cSystemDiagInfoOperState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("opInProgress", 1),
          ("opSuccess", 2),
          ("opFailure", 3))
    )


_Hh3cSystemDiagInfoOperState_Type.__name__ = "Integer32"
_Hh3cSystemDiagInfoOperState_Object = MibTableColumn
hh3cSystemDiagInfoOperState = _Hh3cSystemDiagInfoOperState_Object(
    (1, 3, 6, 1, 4, 1, 25506, 6, 13, 1, 5),
    _Hh3cSystemDiagInfoOperState_Type()
)
hh3cSystemDiagInfoOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cSystemDiagInfoOperState.setStatus("current")


class _Hh3cSystemDiagInfoOperFailReason_Type(DisplayString):
    """Custom type hh3cSystemDiagInfoOperFailReason based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_Hh3cSystemDiagInfoOperFailReason_Type.__name__ = "DisplayString"
_Hh3cSystemDiagInfoOperFailReason_Object = MibTableColumn
hh3cSystemDiagInfoOperFailReason = _Hh3cSystemDiagInfoOperFailReason_Object(
    (1, 3, 6, 1, 4, 1, 25506, 6, 13, 1, 6),
    _Hh3cSystemDiagInfoOperFailReason_Type()
)
hh3cSystemDiagInfoOperFailReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cSystemDiagInfoOperFailReason.setStatus("current")
_Hh3cSystemWorkingMode_ObjectIdentity = ObjectIdentity
hh3cSystemWorkingMode = _Hh3cSystemWorkingMode_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 6, 14)
)
_Hh3cSystemWorkingModeTable_Object = MibTable
hh3cSystemWorkingModeTable = _Hh3cSystemWorkingModeTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 6, 14, 1)
)
if mibBuilder.loadTexts:
    hh3cSystemWorkingModeTable.setStatus("current")
_Hh3cSystemWorkingModeEntry_Object = MibTableRow
hh3cSystemWorkingModeEntry = _Hh3cSystemWorkingModeEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 6, 14, 1, 1)
)
hh3cSystemWorkingModeEntry.setIndexNames(
    (0, "HH3C-COMMON-SYSTEM-MIB", "hh3cSystemWorkingModeIndex"),
)
if mibBuilder.loadTexts:
    hh3cSystemWorkingModeEntry.setStatus("current")


class _Hh3cSystemWorkingModeIndex_Type(Integer32):
    """Custom type hh3cSystemWorkingModeIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Hh3cSystemWorkingModeIndex_Type.__name__ = "Integer32"
_Hh3cSystemWorkingModeIndex_Object = MibTableColumn
hh3cSystemWorkingModeIndex = _Hh3cSystemWorkingModeIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 6, 14, 1, 1, 1),
    _Hh3cSystemWorkingModeIndex_Type()
)
hh3cSystemWorkingModeIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cSystemWorkingModeIndex.setStatus("current")


class _Hh3cSystemWorkingModeName_Type(DisplayString):
    """Custom type hh3cSystemWorkingModeName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_Hh3cSystemWorkingModeName_Type.__name__ = "DisplayString"
_Hh3cSystemWorkingModeName_Object = MibTableColumn
hh3cSystemWorkingModeName = _Hh3cSystemWorkingModeName_Object(
    (1, 3, 6, 1, 4, 1, 25506, 6, 14, 1, 1, 2),
    _Hh3cSystemWorkingModeName_Type()
)
hh3cSystemWorkingModeName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cSystemWorkingModeName.setStatus("current")


class _Hh3cSystemWorkingModeDescr_Type(DisplayString):
    """Custom type hh3cSystemWorkingModeDescr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_Hh3cSystemWorkingModeDescr_Type.__name__ = "DisplayString"
_Hh3cSystemWorkingModeDescr_Object = MibTableColumn
hh3cSystemWorkingModeDescr = _Hh3cSystemWorkingModeDescr_Object(
    (1, 3, 6, 1, 4, 1, 25506, 6, 14, 1, 1, 3),
    _Hh3cSystemWorkingModeDescr_Type()
)
hh3cSystemWorkingModeDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cSystemWorkingModeDescr.setStatus("current")


class _Hh3cSystemWorkingModeDefault_Type(Integer32):
    """Custom type hh3cSystemWorkingModeDefault based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Hh3cSystemWorkingModeDefault_Type.__name__ = "Integer32"
_Hh3cSystemWorkingModeDefault_Object = MibScalar
hh3cSystemWorkingModeDefault = _Hh3cSystemWorkingModeDefault_Object(
    (1, 3, 6, 1, 4, 1, 25506, 6, 14, 2),
    _Hh3cSystemWorkingModeDefault_Type()
)
hh3cSystemWorkingModeDefault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cSystemWorkingModeDefault.setStatus("current")


class _Hh3cSystemWorkingModeCurrent_Type(Integer32):
    """Custom type hh3cSystemWorkingModeCurrent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Hh3cSystemWorkingModeCurrent_Type.__name__ = "Integer32"
_Hh3cSystemWorkingModeCurrent_Object = MibScalar
hh3cSystemWorkingModeCurrent = _Hh3cSystemWorkingModeCurrent_Object(
    (1, 3, 6, 1, 4, 1, 25506, 6, 14, 3),
    _Hh3cSystemWorkingModeCurrent_Type()
)
hh3cSystemWorkingModeCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cSystemWorkingModeCurrent.setStatus("current")


class _Hh3cSystemWorkingModeNext_Type(Integer32):
    """Custom type hh3cSystemWorkingModeNext based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Hh3cSystemWorkingModeNext_Type.__name__ = "Integer32"
_Hh3cSystemWorkingModeNext_Object = MibScalar
hh3cSystemWorkingModeNext = _Hh3cSystemWorkingModeNext_Object(
    (1, 3, 6, 1, 4, 1, 25506, 6, 14, 4),
    _Hh3cSystemWorkingModeNext_Type()
)
hh3cSystemWorkingModeNext.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cSystemWorkingModeNext.setStatus("current")

# Managed Objects groups


# Notification objects

hh3cWriteSuccessTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 6, 8, 1)
)
if mibBuilder.loadTexts:
    hh3cWriteSuccessTrap.setStatus(
        "current"
    )

hh3cWriteFailureTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 6, 8, 2)
)
if mibBuilder.loadTexts:
    hh3cWriteFailureTrap.setStatus(
        "current"
    )

hh3cRebootSendTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 6, 8, 3)
)
if mibBuilder.loadTexts:
    hh3cRebootSendTrap.setStatus(
        "current"
    )

hh3cSysColdStartTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 6, 8, 4)
)
hh3cSysColdStartTrap.setObjects(
    ("HH3C-COMMON-SYSTEM-MIB", "hh3cSysFirstTrapTime")
)
if mibBuilder.loadTexts:
    hh3cSysColdStartTrap.setStatus(
        "current"
    )

hh3cSysWarmStartTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 6, 8, 5)
)
hh3cSysWarmStartTrap.setObjects(
    ("HH3C-COMMON-SYSTEM-MIB", "hh3cSysFirstTrapTime")
)
if mibBuilder.loadTexts:
    hh3cSysWarmStartTrap.setStatus(
        "current"
    )

hh3cSysLoghostUnreachableTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 6, 8, 6)
)
hh3cSysLoghostUnreachableTrap.setObjects(
      *(("HH3C-COMMON-SYSTEM-MIB", "hh3cSysLoghostIndex"),
        ("HH3C-COMMON-SYSTEM-MIB", "hh3cSysLoghostIpaddressType"),
        ("HH3C-COMMON-SYSTEM-MIB", "hh3cSysLoghostIpaddress"),
        ("HH3C-COMMON-SYSTEM-MIB", "hh3cSysLoghostTrapVpnName"))
)
if mibBuilder.loadTexts:
    hh3cSysLoghostUnreachableTrap.setStatus(
        "current"
    )

hh3cSysDyingGaspTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 6, 8, 7)
)
if mibBuilder.loadTexts:
    hh3cSysDyingGaspTrap.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HH3C-COMMON-SYSTEM-MIB",
    **{"hh3cSystem": hh3cSystem,
       "hh3cWriteConfig": hh3cWriteConfig,
       "hh3cStartFtpServer": hh3cStartFtpServer,
       "hh3cReboot": hh3cReboot,
       "hh3cSystemNotification": hh3cSystemNotification,
       "hh3cWriteSuccessTrap": hh3cWriteSuccessTrap,
       "hh3cWriteFailureTrap": hh3cWriteFailureTrap,
       "hh3cRebootSendTrap": hh3cRebootSendTrap,
       "hh3cSysColdStartTrap": hh3cSysColdStartTrap,
       "hh3cSysWarmStartTrap": hh3cSysWarmStartTrap,
       "hh3cSysLoghostUnreachableTrap": hh3cSysLoghostUnreachableTrap,
       "hh3cSysDyingGaspTrap": hh3cSysDyingGaspTrap,
       "hh3cSoftwareVersion": hh3cSoftwareVersion,
       "hh3cSysBootType": hh3cSysBootType,
       "hh3cSystemInfo": hh3cSystemInfo,
       "hh3cSysStatisticPeriod": hh3cSysStatisticPeriod,
       "hh3cSysSamplePeriod": hh3cSysSamplePeriod,
       "hh3cSysTrapResendPeriod": hh3cSysTrapResendPeriod,
       "hh3cSysTrapCollectionPeriod": hh3cSysTrapCollectionPeriod,
       "hh3cSysSnmpPort": hh3cSysSnmpPort,
       "hh3cSysSnmpTrapPort": hh3cSysSnmpTrapPort,
       "hh3cSysNetID": hh3cSysNetID,
       "hh3cSysLastSampleTime": hh3cSysLastSampleTime,
       "hh3cSysTrapSendNum": hh3cSysTrapSendNum,
       "hh3cSysFirstTrapTime": hh3cSysFirstTrapTime,
       "hh3cSysBannerMOTD": hh3cSysBannerMOTD,
       "hh3cSystemNotificationInfo": hh3cSystemNotificationInfo,
       "hh3cSysLoghostIndex": hh3cSysLoghostIndex,
       "hh3cSysLoghostIpaddressType": hh3cSysLoghostIpaddressType,
       "hh3cSysLoghostIpaddress": hh3cSysLoghostIpaddress,
       "hh3cSysLoghostTrapVpnName": hh3cSysLoghostTrapVpnName,
       "hh3cSystemDiagInfoTable": hh3cSystemDiagInfoTable,
       "hh3cSystemDiagInfoEntry": hh3cSystemDiagInfoEntry,
       "hh3cSystemDiagInfoIndex": hh3cSystemDiagInfoIndex,
       "hh3cSystemDiagInfoFilename": hh3cSystemDiagInfoFilename,
       "hh3cSystemDiagInfoRowStatus": hh3cSystemDiagInfoRowStatus,
       "hh3cSystemDiagInfoOperEndTime": hh3cSystemDiagInfoOperEndTime,
       "hh3cSystemDiagInfoOperState": hh3cSystemDiagInfoOperState,
       "hh3cSystemDiagInfoOperFailReason": hh3cSystemDiagInfoOperFailReason,
       "hh3cSystemWorkingMode": hh3cSystemWorkingMode,
       "hh3cSystemWorkingModeTable": hh3cSystemWorkingModeTable,
       "hh3cSystemWorkingModeEntry": hh3cSystemWorkingModeEntry,
       "hh3cSystemWorkingModeIndex": hh3cSystemWorkingModeIndex,
       "hh3cSystemWorkingModeName": hh3cSystemWorkingModeName,
       "hh3cSystemWorkingModeDescr": hh3cSystemWorkingModeDescr,
       "hh3cSystemWorkingModeDefault": hh3cSystemWorkingModeDefault,
       "hh3cSystemWorkingModeCurrent": hh3cSystemWorkingModeCurrent,
       "hh3cSystemWorkingModeNext": hh3cSystemWorkingModeNext}
)
