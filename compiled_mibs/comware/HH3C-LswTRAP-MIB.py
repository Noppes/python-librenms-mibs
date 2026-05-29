# SNMP MIB module (HH3C-LswTRAP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\comware\HH3C-LswTRAP-MIB

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

(CounterBasedGauge64,) = mibBuilder.importSymbols(
    "HCNUM-TC",
    "CounterBasedGauge64")

(hh3cLswCoreIndex,
 hh3cLswCoreMinorThreshold,
 hh3cLswCoreRecoveryThreshold,
 hh3cLswCoreThreshold,
 hh3cLswCpuIndex,
 hh3cLswCpuMemory,
 hh3cLswCpuMemoryCriticalThreshold,
 hh3cLswCpuMemoryCurrentState,
 hh3cLswCpuMemoryEarlyWarningThreshold,
 hh3cLswCpuMemoryFree,
 hh3cLswCpuMemoryFreeRatio,
 hh3cLswCpuMemoryHighFree,
 hh3cLswCpuMemoryHighTotal,
 hh3cLswCpuMemoryLowFree,
 hh3cLswCpuMemoryLowTotal,
 hh3cLswCpuMemoryMinorThreshold,
 hh3cLswCpuMemoryNormalThreshold,
 hh3cLswCpuMemorySecureThreshold,
 hh3cLswCpuMemorySevereThreshold,
 hh3cLswCpuRatio,
 hh3cLswCpuUsageMinorThreshold,
 hh3cLswCpuUsageRecoverThreshold,
 hh3cLswCpuUsageSevereThreshold,
 hh3cLswFrameIndex,
 hh3cLswSlotIndex,
 hh3cLswSubslotIndex) = mibBuilder.importSymbols(
    "HH3C-LSW-DEV-ADM-MIB",
    "hh3cLswCoreIndex",
    "hh3cLswCoreMinorThreshold",
    "hh3cLswCoreRecoveryThreshold",
    "hh3cLswCoreThreshold",
    "hh3cLswCpuIndex",
    "hh3cLswCpuMemory",
    "hh3cLswCpuMemoryCriticalThreshold",
    "hh3cLswCpuMemoryCurrentState",
    "hh3cLswCpuMemoryEarlyWarningThreshold",
    "hh3cLswCpuMemoryFree",
    "hh3cLswCpuMemoryFreeRatio",
    "hh3cLswCpuMemoryHighFree",
    "hh3cLswCpuMemoryHighTotal",
    "hh3cLswCpuMemoryLowFree",
    "hh3cLswCpuMemoryLowTotal",
    "hh3cLswCpuMemoryMinorThreshold",
    "hh3cLswCpuMemoryNormalThreshold",
    "hh3cLswCpuMemorySecureThreshold",
    "hh3cLswCpuMemorySevereThreshold",
    "hh3cLswCpuRatio",
    "hh3cLswCpuUsageMinorThreshold",
    "hh3cLswCpuUsageRecoverThreshold",
    "hh3cLswCpuUsageSevereThreshold",
    "hh3cLswFrameIndex",
    "hh3cLswSlotIndex",
    "hh3cLswSubslotIndex")

(hh3cDevMFanNum,
 hh3cDevMFirstTrapTime,
 hh3cDevMPowerNum) = mibBuilder.importSymbols(
    "HH3C-LswDEVM-MIB",
    "hh3cDevMFanNum",
    "hh3cDevMFirstTrapTime",
    "hh3cDevMPowerNum")

(hh3clswCommon,) = mibBuilder.importSymbols(
    "HH3C-OID-MIB",
    "hh3clswCommon")

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

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

hh3cLswTrapMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 12)
)
if mibBuilder.loadTexts:
    hh3cLswTrapMib.setRevisions(
        ("2020-10-15 00:00",
         "2019-11-22 00:00",
         "2019-01-11 00:00",
         "2018-04-13 00:00",
         "2017-12-05 00:00",
         "2017-07-17 00:00",
         "2017-06-24 00:00",
         "2017-01-12 00:00",
         "2011-11-26 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Hh3csLswTRAPMibObject_ObjectIdentity = ObjectIdentity
hh3csLswTRAPMibObject = _Hh3csLswTRAPMibObject_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 12, 1)
)
_Hh3cNetworkHealthMonitorFailure_ObjectIdentity = ObjectIdentity
hh3cNetworkHealthMonitorFailure = _Hh3cNetworkHealthMonitorFailure_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 12, 1, 98)
)
_Hh3cNetworkHealthMonitorNormal_ObjectIdentity = ObjectIdentity
hh3cNetworkHealthMonitorNormal = _Hh3cNetworkHealthMonitorNormal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 12, 1, 99)
)
_Hh3csLswTRAPMibInfor_ObjectIdentity = ObjectIdentity
hh3csLswTRAPMibInfor = _Hh3csLswTRAPMibInfor_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 12, 2)
)


class _Hh3csLswTrapCpuCoreInfo_Type(SnmpAdminString):
    """Custom type hh3csLswTrapCpuCoreInfo based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_Hh3csLswTrapCpuCoreInfo_Type.__name__ = "SnmpAdminString"
_Hh3csLswTrapCpuCoreInfo_Object = MibScalar
hh3csLswTrapCpuCoreInfo = _Hh3csLswTrapCpuCoreInfo_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 12, 2, 1),
    _Hh3csLswTrapCpuCoreInfo_Type()
)
hh3csLswTrapCpuCoreInfo.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3csLswTrapCpuCoreInfo.setStatus("current")


class _Hh3csLswTrapProcessCpuInfo_Type(SnmpAdminString):
    """Custom type hh3csLswTrapProcessCpuInfo based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_Hh3csLswTrapProcessCpuInfo_Type.__name__ = "SnmpAdminString"
_Hh3csLswTrapProcessCpuInfo_Object = MibScalar
hh3csLswTrapProcessCpuInfo = _Hh3csLswTrapProcessCpuInfo_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 12, 2, 2),
    _Hh3csLswTrapProcessCpuInfo_Type()
)
hh3csLswTrapProcessCpuInfo.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3csLswTrapProcessCpuInfo.setStatus("current")


class _Hh3csLswTrapProcessMemoryInfo_Type(SnmpAdminString):
    """Custom type hh3csLswTrapProcessMemoryInfo based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_Hh3csLswTrapProcessMemoryInfo_Type.__name__ = "SnmpAdminString"
_Hh3csLswTrapProcessMemoryInfo_Object = MibScalar
hh3csLswTrapProcessMemoryInfo = _Hh3csLswTrapProcessMemoryInfo_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 12, 2, 3),
    _Hh3csLswTrapProcessMemoryInfo_Type()
)
hh3csLswTrapProcessMemoryInfo.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3csLswTrapProcessMemoryInfo.setStatus("current")


class _Hh3csLswTrapSlubInfo_Type(SnmpAdminString):
    """Custom type hh3csLswTrapSlubInfo based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_Hh3csLswTrapSlubInfo_Type.__name__ = "SnmpAdminString"
_Hh3csLswTrapSlubInfo_Object = MibScalar
hh3csLswTrapSlubInfo = _Hh3csLswTrapSlubInfo_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 12, 2, 4),
    _Hh3csLswTrapSlubInfo_Type()
)
hh3csLswTrapSlubInfo.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3csLswTrapSlubInfo.setStatus("current")


class _Hh3cLswTrapCpuUsage_Type(SnmpAdminString):
    """Custom type hh3cLswTrapCpuUsage based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_Hh3cLswTrapCpuUsage_Type.__name__ = "SnmpAdminString"
_Hh3cLswTrapCpuUsage_Object = MibScalar
hh3cLswTrapCpuUsage = _Hh3cLswTrapCpuUsage_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 12, 2, 5),
    _Hh3cLswTrapCpuUsage_Type()
)
hh3cLswTrapCpuUsage.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cLswTrapCpuUsage.setStatus("current")


class _Hh3cLswTrapCoreProcessInfo_Type(SnmpAdminString):
    """Custom type hh3cLswTrapCoreProcessInfo based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_Hh3cLswTrapCoreProcessInfo_Type.__name__ = "SnmpAdminString"
_Hh3cLswTrapCoreProcessInfo_Object = MibScalar
hh3cLswTrapCoreProcessInfo = _Hh3cLswTrapCoreProcessInfo_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 12, 2, 6),
    _Hh3cLswTrapCoreProcessInfo_Type()
)
hh3cLswTrapCoreProcessInfo.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cLswTrapCoreProcessInfo.setStatus("current")
_Hh3cLswCoreTrapUsage_Type = Unsigned32
_Hh3cLswCoreTrapUsage_Object = MibScalar
hh3cLswCoreTrapUsage = _Hh3cLswCoreTrapUsage_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 12, 2, 7),
    _Hh3cLswCoreTrapUsage_Type()
)
hh3cLswCoreTrapUsage.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cLswCoreTrapUsage.setStatus("current")
_Hh3cBoardAvailablePower_Type = Integer32
_Hh3cBoardAvailablePower_Object = MibScalar
hh3cBoardAvailablePower = _Hh3cBoardAvailablePower_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 12, 2, 8),
    _Hh3cBoardAvailablePower_Type()
)
hh3cBoardAvailablePower.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cBoardAvailablePower.setStatus("current")
_Hh3cBoardRequiredPower_Type = Integer32
_Hh3cBoardRequiredPower_Object = MibScalar
hh3cBoardRequiredPower = _Hh3cBoardRequiredPower_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 12, 2, 9),
    _Hh3cBoardRequiredPower_Type()
)
hh3cBoardRequiredPower.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cBoardRequiredPower.setStatus("current")
_Hh3cLswAlarmInPortInNum_Type = Unsigned32
_Hh3cLswAlarmInPortInNum_Object = MibScalar
hh3cLswAlarmInPortInNum = _Hh3cLswAlarmInPortInNum_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 12, 2, 10),
    _Hh3cLswAlarmInPortInNum_Type()
)
hh3cLswAlarmInPortInNum.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cLswAlarmInPortInNum.setStatus("current")
_Hh3cDMAMemoryTotal_Type = CounterBasedGauge64
_Hh3cDMAMemoryTotal_Object = MibScalar
hh3cDMAMemoryTotal = _Hh3cDMAMemoryTotal_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 12, 2, 11),
    _Hh3cDMAMemoryTotal_Type()
)
hh3cDMAMemoryTotal.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cDMAMemoryTotal.setStatus("current")
if mibBuilder.loadTexts:
    hh3cDMAMemoryTotal.setUnits("byte")
_Hh3cDMAMemoryUsed_Type = CounterBasedGauge64
_Hh3cDMAMemoryUsed_Object = MibScalar
hh3cDMAMemoryUsed = _Hh3cDMAMemoryUsed_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 12, 2, 12),
    _Hh3cDMAMemoryUsed_Type()
)
hh3cDMAMemoryUsed.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cDMAMemoryUsed.setStatus("current")
if mibBuilder.loadTexts:
    hh3cDMAMemoryUsed.setUnits("byte")
_Hh3cDMAMemoryFree_Type = CounterBasedGauge64
_Hh3cDMAMemoryFree_Object = MibScalar
hh3cDMAMemoryFree = _Hh3cDMAMemoryFree_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 12, 2, 13),
    _Hh3cDMAMemoryFree_Type()
)
hh3cDMAMemoryFree.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cDMAMemoryFree.setStatus("current")
if mibBuilder.loadTexts:
    hh3cDMAMemoryFree.setUnits("byte")


class _Hh3cDMAMemoryFreeRatio_Type(Unsigned32):
    """Custom type hh3cDMAMemoryFreeRatio based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Hh3cDMAMemoryFreeRatio_Type.__name__ = "Unsigned32"
_Hh3cDMAMemoryFreeRatio_Object = MibScalar
hh3cDMAMemoryFreeRatio = _Hh3cDMAMemoryFreeRatio_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 12, 2, 14),
    _Hh3cDMAMemoryFreeRatio_Type()
)
hh3cDMAMemoryFreeRatio.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cDMAMemoryFreeRatio.setStatus("current")
_Hh3cDMAMemoryCriticalThreshold_Type = Unsigned32
_Hh3cDMAMemoryCriticalThreshold_Object = MibScalar
hh3cDMAMemoryCriticalThreshold = _Hh3cDMAMemoryCriticalThreshold_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 12, 2, 15),
    _Hh3cDMAMemoryCriticalThreshold_Type()
)
hh3cDMAMemoryCriticalThreshold.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cDMAMemoryCriticalThreshold.setStatus("current")
_Hh3cDMAMemoryRecoverThreshold_Type = Unsigned32
_Hh3cDMAMemoryRecoverThreshold_Object = MibScalar
hh3cDMAMemoryRecoverThreshold = _Hh3cDMAMemoryRecoverThreshold_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 12, 2, 16),
    _Hh3cDMAMemoryRecoverThreshold_Type()
)
hh3cDMAMemoryRecoverThreshold.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cDMAMemoryRecoverThreshold.setStatus("current")


class _Hh3cDMAMemoryCurrentState_Type(Integer32):
    """Custom type hh3cDMAMemoryCurrentState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("normal", 1),
          ("critical", 2))
    )


_Hh3cDMAMemoryCurrentState_Type.__name__ = "Integer32"
_Hh3cDMAMemoryCurrentState_Object = MibScalar
hh3cDMAMemoryCurrentState = _Hh3cDMAMemoryCurrentState_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 12, 2, 17),
    _Hh3cDMAMemoryCurrentState_Type()
)
hh3cDMAMemoryCurrentState.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cDMAMemoryCurrentState.setStatus("current")
_Hh3cFrameRemainingPower_Type = Unsigned32
_Hh3cFrameRemainingPower_Object = MibScalar
hh3cFrameRemainingPower = _Hh3cFrameRemainingPower_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 12, 2, 18),
    _Hh3cFrameRemainingPower_Type()
)
hh3cFrameRemainingPower.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cFrameRemainingPower.setStatus("current")
if mibBuilder.loadTexts:
    hh3cFrameRemainingPower.setUnits("W")
_Hh3csLswTRAPMibObjectV2_ObjectIdentity = ObjectIdentity
hh3csLswTRAPMibObjectV2 = _Hh3csLswTRAPMibObjectV2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 12, 3)
)
_Hh3csLswTRAPMibObjectV2Prefix_ObjectIdentity = ObjectIdentity
hh3csLswTRAPMibObjectV2Prefix = _Hh3csLswTRAPMibObjectV2Prefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 12, 3, 0)
)

# Managed Objects groups


# Notification objects

hh3cpowerfailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 12, 1, 1)
)
hh3cpowerfailure.setObjects(
      *(("HH3C-LswDEVM-MIB", "hh3cDevMPowerNum"),
        ("HH3C-LswDEVM-MIB", "hh3cDevMFirstTrapTime"))
)
if mibBuilder.loadTexts:
    hh3cpowerfailure.setStatus(
        "current"
    )

hh3cPowerNormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 12, 1, 2)
)
hh3cPowerNormal.setObjects(
      *(("HH3C-LswDEVM-MIB", "hh3cDevMPowerNum"),
        ("HH3C-LswDEVM-MIB", "hh3cDevMFirstTrapTime"))
)
if mibBuilder.loadTexts:
    hh3cPowerNormal.setStatus(
        "current"
    )

hh3cMasterPowerNormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 12, 1, 3)
)
hh3cMasterPowerNormal.setObjects(
    ("HH3C-LswDEVM-MIB", "hh3cDevMPowerNum")
)
if mibBuilder.loadTexts:
    hh3cMasterPowerNormal.setStatus(
        "current"
    )

hh3cSlavePowerNormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 12, 1, 4)
)
hh3cSlavePowerNormal.setObjects(
    ("HH3C-LswDEVM-MIB", "hh3cDevMPowerNum")
)
if mibBuilder.loadTexts:
    hh3cSlavePowerNormal.setStatus(
        "current"
    )

hh3cPowerRemoved = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 12, 1, 5)
)
hh3cPowerRemoved.setObjects(
    ("HH3C-LswDEVM-MIB", "hh3cDevMPowerNum")
)
if mibBuilder.loadTexts:
    hh3cPowerRemoved.setStatus(
        "current"
    )

hh3cfanfailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 12, 1, 6)
)
hh3cfanfailure.setObjects(
    ("HH3C-LswDEVM-MIB", "hh3cDevMFanNum")
)
if mibBuilder.loadTexts:
    hh3cfanfailure.setStatus(
        "current"
    )

hh3cFanNormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 12, 1, 7)
)
hh3cFanNormal.setObjects(
    ("HH3C-LswDEVM-MIB", "hh3cDevMFanNum")
)
if mibBuilder.loadTexts:
    hh3cFanNormal.setStatus(
        "current"
    )

hh3cBoardRemoved = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 12, 1, 8)
)
hh3cBoardRemoved.setObjects(
      *(("HH3C-LSW-DEV-ADM-MIB", "hh3cLswFrameIndex"),
        ("HH3C-LSW-DEV-ADM-MIB", "hh3cLswSlotIndex"))
)
if mibBuilder.loadTexts:
    hh3cBoardRemoved.setStatus(
        "current"
    )

hh3cBoardInserted = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 12, 1, 9)
)
hh3cBoardInserted.setObjects(
      *(("HH3C-LSW-DEV-ADM-MIB", "hh3cLswFrameIndex"),
        ("HH3C-LSW-DEV-ADM-MIB", "hh3cLswSlotIndex"))
)
if mibBuilder.loadTexts:
    hh3cBoardInserted.setStatus(
        "current"
    )

hh3cBoardFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 12, 1, 10)
)
hh3cBoardFailure.setObjects(
      *(("HH3C-LSW-DEV-ADM-MIB", "hh3cLswFrameIndex"),
        ("HH3C-LSW-DEV-ADM-MIB", "hh3cLswSlotIndex"))
)
if mibBuilder.loadTexts:
    hh3cBoardFailure.setStatus(
        "current"
    )

hh3cBoardNormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 12, 1, 11)
)
hh3cBoardNormal.setObjects(
      *(("HH3C-LSW-DEV-ADM-MIB", "hh3cLswFrameIndex"),
        ("HH3C-LSW-DEV-ADM-MIB", "hh3cLswSlotIndex"))
)
if mibBuilder.loadTexts:
    hh3cBoardNormal.setStatus(
        "current"
    )

hh3cSubcardRemove = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 12, 1, 12)
)
hh3cSubcardRemove.setObjects(
      *(("HH3C-LSW-DEV-ADM-MIB", "hh3cLswFrameIndex"),
        ("HH3C-LSW-DEV-ADM-MIB", "hh3cLswSlotIndex"),
        ("HH3C-LSW-DEV-ADM-MIB", "hh3cLswSubslotIndex"))
)
if mibBuilder.loadTexts:
    hh3cSubcardRemove.setStatus(
        "current"
    )

hh3cSubcardInsert = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 12, 1, 13)
)
hh3cSubcardInsert.setObjects(
      *(("HH3C-LSW-DEV-ADM-MIB", "hh3cLswFrameIndex"),
        ("HH3C-LSW-DEV-ADM-MIB", "hh3cLswSlotIndex"),
        ("HH3C-LSW-DEV-ADM-MIB", "hh3cLswSubslotIndex"))
)
if mibBuilder.loadTexts:
    hh3cSubcardInsert.setStatus(
        "current"
    )

hh3cBoardTemperatureLower = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 12, 1, 14)
)
hh3cBoardTemperatureLower.setObjects(
      *(("HH3C-LSW-DEV-ADM-MIB", "hh3cLswFrameIndex"),
        ("HH3C-LSW-DEV-ADM-MIB", "hh3cLswSlotIndex"))
)
if mibBuilder.loadTexts:
    hh3cBoardTemperatureLower.setStatus(
        "current"
    )

hh3cBoardTemperatureFromLowerToNormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 12, 1, 15)
)
hh3cBoardTemperatureFromLowerToNormal.setObjects(
      *(("HH3C-LSW-DEV-ADM-MIB", "hh3cLswFrameIndex"),
        ("HH3C-LSW-DEV-ADM-MIB", "hh3cLswSlotIndex"))
)
if mibBuilder.loadTexts:
    hh3cBoardTemperatureFromLowerToNormal.setStatus(
        "current"
    )

hh3cBoardTemperatureHigher = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 12, 1, 16)
)
hh3cBoardTemperatureHigher.setObjects(
      *(("HH3C-LSW-DEV-ADM-MIB", "hh3cLswFrameIndex"),
        ("HH3C-LSW-DEV-ADM-MIB", "hh3cLswSlotIndex"))
)
if mibBuilder.loadTexts:
    hh3cBoardTemperatureHigher.setStatus(
        "current"
    )

hh3cBoardTemperatureFormHigherToNormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 12, 1, 17)
)
hh3cBoardTemperatureFormHigherToNormal.setObjects(
      *(("HH3C-LSW-DEV-ADM-MIB", "hh3cLswFrameIndex"),
        ("HH3C-LSW-DEV-ADM-MIB", "hh3cLswSlotIndex"))
)
if mibBuilder.loadTexts:
    hh3cBoardTemperatureFormHigherToNormal.setStatus(
        "current"
    )

hh3cRequestLoading = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 12, 1, 18)
)
hh3cRequestLoading.setObjects(
      *(("HH3C-LSW-DEV-ADM-MIB", "hh3cLswFrameIndex"),
        ("HH3C-LSW-DEV-ADM-MIB", "hh3cLswSlotIndex"))
)
if mibBuilder.loadTexts:
    hh3cRequestLoading.setStatus(
        "current"
    )

hh3cLoadFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 12, 1, 19)
)
hh3cLoadFailure.setObjects(
      *(("HH3C-LSW-DEV-ADM-MIB", "hh3cLswFrameIndex"),
        ("HH3C-LSW-DEV-ADM-MIB", "hh3cLswSlotIndex"))
)
if mibBuilder.loadTexts:
    hh3cLoadFailure.setStatus(
        "current"
    )

hh3cLoadFinished = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 12, 1, 20)
)
hh3cLoadFinished.setObjects(
      *(("HH3C-LSW-DEV-ADM-MIB", "hh3cLswFrameIndex"),
        ("HH3C-LSW-DEV-ADM-MIB", "hh3cLswSlotIndex"))
)
if mibBuilder.loadTexts:
    hh3cLoadFinished.setStatus(
        "current"
    )

hh3cBackBoardModeSetFuilure = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 12, 1, 21)
)
hh3cBackBoardModeSetFuilure.setObjects(
    ("HH3C-LSW-DEV-ADM-MIB", "hh3cLswFrameIndex")
)
if mibBuilder.loadTexts:
    hh3cBackBoardModeSetFuilure.setStatus(
        "current"
    )

hh3cBackBoardModeSetOK = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 12, 1, 22)
)
hh3cBackBoardModeSetOK.setObjects(
    ("HH3C-LSW-DEV-ADM-MIB", "hh3cLswFrameIndex")
)
if mibBuilder.loadTexts:
    hh3cBackBoardModeSetOK.setStatus(
        "current"
    )

hh3cPowerInserted = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 12, 1, 23)
)
hh3cPowerInserted.setObjects(
    ("HH3C-LswDEVM-MIB", "hh3cDevMPowerNum")
)
if mibBuilder.loadTexts:
    hh3cPowerInserted.setStatus(
        "current"
    )

hh3cBootImageUpdated = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 12, 1, 24)
)
hh3cBootImageUpdated.setObjects(
      *(("HH3C-LSW-DEV-ADM-MIB", "hh3cLswFrameIndex"),
        ("HH3C-LSW-DEV-ADM-MIB", "hh3cLswSlotIndex"))
)
if mibBuilder.loadTexts:
    hh3cBootImageUpdated.setStatus(
        "current"
    )

hh3cCpuRemoved = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 12, 1, 25)
)
hh3cCpuRemoved.setObjects(
      *(("HH3C-LSW-DEV-ADM-MIB", "hh3cLswFrameIndex"),
        ("HH3C-LSW-DEV-ADM-MIB", "hh3cLswSlotIndex"),
        ("HH3C-LSW-DEV-ADM-MIB", "hh3cLswCpuIndex"))
)
if mibBuilder.loadTexts:
    hh3cCpuRemoved.setStatus(
        "current"
    )

hh3cCpuFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 12, 1, 26)
)
hh3cCpuFailure.setObjects(
      *(("HH3C-LSW-DEV-ADM-MIB", "hh3cLswFrameIndex"),
        ("HH3C-LSW-DEV-ADM-MIB", "hh3cLswSlotIndex"),
        ("HH3C-LSW-DEV-ADM-MIB", "hh3cLswCpuIndex"))
)
if mibBuilder.loadTexts:
    hh3cCpuFailure.setStatus(
        "current"
    )

hh3cCpuNormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 12, 1, 27)
)
hh3cCpuNormal.setObjects(
      *(("HH3C-LSW-DEV-ADM-MIB", "hh3cLswFrameIndex"),
        ("HH3C-LSW-DEV-ADM-MIB", "hh3cLswSlotIndex"),
        ("HH3C-LSW-DEV-ADM-MIB", "hh3cLswCpuIndex"))
)
if mibBuilder.loadTexts:
    hh3cCpuNormal.setStatus(
        "current"
    )

hh3cPowerIncompatible = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 12, 1, 28)
)
hh3cPowerIncompatible.setObjects(
    ("HH3C-LswDEVM-MIB", "hh3cDevMPowerNum")
)
if mibBuilder.loadTexts:
    hh3cPowerIncompatible.setStatus(
        "current"
    )

hh3cCpuUsageSevereNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 12, 1, 29)
)
hh3cCpuUsageSevereNotification.setObjects(
      *(("HH3C-LSW-DEV-ADM-MIB", "hh3cLswFrameIndex"),
        ("HH3C-LSW-DEV-ADM-MIB", "hh3cLswSlotIndex"),
        ("HH3C-LSW-DEV-ADM-MIB", "hh3cLswCpuIndex"),
        ("HH3C-LSW-DEV-ADM-MIB", "hh3cLswCpuRatio"),
        ("HH3C-LSW-DEV-ADM-MIB", "hh3cLswCpuUsageMinorThreshold"),
        ("HH3C-LSW-DEV-ADM-MIB", "hh3cLswCpuUsageSevereThreshold"),
        ("HH3C-LSW-DEV-ADM-MIB", "hh3cLswCpuUsageRecoverThreshold"),
        ("HH3C-LswTRAP-MIB", "hh3csLswTrapCpuCoreInfo"),
        ("HH3C-LswTRAP-MIB", "hh3csLswTrapProcessCpuInfo"))
)
if mibBuilder.loadTexts:
    hh3cCpuUsageSevereNotification.setStatus(
        "current"
    )

hh3cCpuUsageSevereRecoverNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 12, 1, 30)
)
hh3cCpuUsageSevereRecoverNotification.setObjects(
      *(("HH3C-LSW-DEV-ADM-MIB", "hh3cLswFrameIndex"),
        ("HH3C-LSW-DEV-ADM-MIB", "hh3cLswSlotIndex"),
        ("HH3C-LSW-DEV-ADM-MIB", "hh3cLswCpuIndex"),
        ("HH3C-LSW-DEV-ADM-MIB", "hh3cLswCpuRatio"),
        ("HH3C-LSW-DEV-ADM-MIB", "hh3cLswCpuUsageMinorThreshold"),
        ("HH3C-LSW-DEV-ADM-MIB", "hh3cLswCpuUsageSevereThreshold"),
        ("HH3C-LSW-DEV-ADM-MIB", "hh3cLswCpuUsageRecoverThreshold"),
        ("HH3C-LswTRAP-MIB", "hh3csLswTrapCpuCoreInfo"),
        ("HH3C-LswTRAP-MIB", "hh3csLswTrapProcessCpuInfo"))
)
if mibBuilder.loadTexts:
    hh3cCpuUsageSevereRecoverNotification.setStatus(
        "current"
    )

hh3cCpuUsageMinorNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 12, 1, 31)
)
hh3cCpuUsageMinorNotification.setObjects(
      *(("HH3C-LSW-DEV-ADM-MIB", "hh3cLswFrameIndex"),
        ("HH3C-LSW-DEV-ADM-MIB", "hh3cLswSlotIndex"),
        ("HH3C-LSW-DEV-ADM-MIB", "hh3cLswCpuIndex"),
        ("HH3C-LSW-DEV-ADM-MIB", "hh3cLswCpuRatio"),
        ("HH3C-LSW-DEV-ADM-MIB", "hh3cLswCpuUsageMinorThreshold"),
        ("HH3C-LSW-DEV-ADM-MIB", "hh3cLswCpuUsageSevereThreshold"),
        ("HH3C-LSW-DEV-ADM-MIB", "hh3cLswCpuUsageRecoverThreshold"),
        ("HH3C-LswTRAP-MIB", "hh3csLswTrapCpuCoreInfo"),
        ("HH3C-LswTRAP-MIB", "hh3csLswTrapProcessCpuInfo"))
)
if mibBuilder.loadTexts:
    hh3cCpuUsageMinorNotification.setStatus(
        "current"
    )

hh3cCpuUsageMinorRecoverNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 12, 1, 32)
)
hh3cCpuUsageMinorRecoverNotification.setObjects(
      *(("HH3C-LSW-DEV-ADM-MIB", "hh3cLswFrameIndex"),
        ("HH3C-LSW-DEV-ADM-MIB", "hh3cLswSlotIndex"),
        ("HH3C-LSW-DEV-ADM-MIB", "hh3cLswCpuIndex"),
        ("HH3C-LSW-DEV-ADM-MIB", "hh3cLswCpuRatio"),
        ("HH3C-LSW-DEV-ADM-MIB", "hh3cLswCpuUsageMinorThreshold"),
        ("HH3C-LSW-DEV-ADM-MIB", "hh3cLswCpuUsageSevereThreshold"),
        ("HH3C-LSW-DEV-ADM-MIB", "hh3cLswCpuUsageRecoverThreshold"),
        ("HH3C-LswTRAP-MIB", "hh3csLswTrapCpuCoreInfo"),
        ("HH3C-LswTRAP-MIB", "hh3csLswTrapProcessCpuInfo"))
)
if mibBuilder.loadTexts:
    hh3cCpuUsageMinorRecoverNotification.setStatus(
        "current"
    )

hh3cMemoryUsageEarlyWarningNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 12, 1, 33)
)
hh3cMemoryUsageEarlyWarningNotification.setObjects(
      *(("HH3C-LSW-DEV-ADM-MIB", "hh3cLswFrameIndex"),
        ("HH3C-LSW-DEV-ADM-MIB", "hh3cLswSlotIndex"),
        ("HH3C-LSW-DEV-ADM-MIB", "hh3cLswCpuIndex"),
        ("HH3C-LSW-DEV-ADM-MIB", "hh3cLswCpuMemory"),
        ("HH3C-LSW-DEV-ADM-MIB", "hh3cLswCpuMemoryFree"),
        ("HH3C-LSW-DEV-ADM-MIB", "hh3cLswCpuMemoryFreeRatio"),
        ("HH3C-LSW-DEV-ADM-MIB", "hh3cLswCpuMemoryHighTotal"),
        ("HH3C-LSW-DEV-ADM-MIB", "hh3cLswCpuMemoryHighFree"),
        ("HH3C-LSW-DEV-ADM-MIB", "hh3cLswCpuMemoryLowTotal"),
        ("HH3C-LSW-DEV-ADM-MIB", "hh3cLswCpuMemoryLowFree"),
        ("HH3C-LSW-DEV-ADM-MIB", "hh3cLswCpuMemorySecureThreshold"),
        ("HH3C-LSW-DEV-ADM-MIB", "hh3cLswCpuMemoryEarlyWarningThreshold"),
        ("HH3C-LSW-DEV-ADM-MIB", "hh3cLswCpuMemoryNormalThreshold"),
        ("HH3C-LSW-DEV-ADM-MIB", "hh3cLswCpuMemoryMinorThreshold"),
        ("HH3C-LSW-DEV-ADM-MIB", "hh3cLswCpuMemorySevereThreshold"),
        ("HH3C-LSW-DEV-ADM-MIB", "hh3cLswCpuMemoryCriticalThreshold"),
        ("HH3C-LSW-DEV-ADM-MIB", "hh3cLswCpuMemoryCurrentState"),
        ("HH3C-LswTRAP-MIB", "hh3csLswTrapProcessMemoryInfo"),
        ("HH3C-LswTRAP-MIB", "hh3csLswTrapSlubInfo"))
)
if mibBuilder.loadTexts:
    hh3cMemoryUsageEarlyWarningNotification.setStatus(
        "current"
    )

hh3cMemoryUsageEarlyWarningRecoverNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 12, 1, 34)
)
hh3cMemoryUsageEarlyWarningRecoverNotification.setObjects(
      *(("HH3C-LSW-DEV-ADM-MIB", "hh3cLswFrameIndex"),
        ("HH3C-LSW-DEV-ADM-MIB", "hh3cLswSlotIndex"),
        ("HH3C-LSW-DEV-ADM-MIB", "hh3cLswCpuIndex"),
        ("HH3C-LSW-DEV-ADM-MIB", "hh3cLswCpuMemory"),
        ("HH3C-LSW-DEV-ADM-MIB", "hh3cLswCpuMemoryFree"),
        ("HH3C-LSW-DEV-ADM-MIB", "hh3cLswCpuMemoryFreeRatio"),
        ("HH3C-LSW-DEV-ADM-MIB", "hh3cLswCpuMemoryHighTotal"),
        ("HH3C-LSW-DEV-ADM-MIB", "hh3cLswCpuMemoryHighFree"),
        ("HH3C-LSW-DEV-ADM-MIB", "hh3cLswCpuMemoryLowTotal"),
        ("HH3C-LSW-DEV-ADM-MIB", "hh3cLswCpuMemoryLowFree"),
        ("HH3C-LSW-DEV-ADM-MIB", "hh3cLswCpuMemorySecureThreshold"),
        ("HH3C-LSW-DEV-ADM-MIB", "hh3cLswCpuMemoryEarlyWarningThreshold"),
        ("HH3C-LSW-DEV-ADM-MIB", "hh3cLswCpuMemoryNormalThreshold"),
        ("HH3C-LSW-DEV-ADM-MIB", "hh3cLswCpuMemoryMinorThreshold"),
        ("HH3C-LSW-DEV-ADM-MIB", "hh3cLswCpuMemorySevereThreshold"),
        ("HH3C-LSW-DEV-ADM-MIB", "hh3cLswCpuMemoryCriticalThreshold"),
        ("HH3C-LSW-DEV-ADM-MIB", "hh3cLswCpuMemoryCurrentState"),
        ("HH3C-LswTRAP-MIB", "hh3csLswTrapProcessMemoryInfo"),
        ("HH3C-LswTRAP-MIB", "hh3csLswTrapSlubInfo"))
)
if mibBuilder.loadTexts:
    hh3cMemoryUsageEarlyWarningRecoverNotification.setStatus(
        "current"
    )

hh3cMemoryUsageMinorNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 12, 1, 35)
)
hh3cMemoryUsageMinorNotification.setObjects(
      *(("HH3C-LSW-DEV-ADM-MIB", "hh3cLswFrameIndex"),
        ("HH3C-LSW-DEV-ADM-MIB", "hh3cLswSlotIndex"),
        ("HH3C-LSW-DEV-ADM-MIB", "hh3cLswCpuIndex"),
        ("HH3C-LSW-DEV-ADM-MIB", "hh3cLswCpuMemory"),
        ("HH3C-LSW-DEV-ADM-MIB", "hh3cLswCpuMemoryFree"),
        ("HH3C-LSW-DEV-ADM-MIB", "hh3cLswCpuMemoryFreeRatio"),
        ("HH3C-LSW-DEV-ADM-MIB", "hh3cLswCpuMemoryHighTotal"),
        ("HH3C-LSW-DEV-ADM-MIB", "hh3cLswCpuMemoryHighFree"),
        ("HH3C-LSW-DEV-ADM-MIB", "hh3cLswCpuMemoryLowTotal"),
        ("HH3C-LSW-DEV-ADM-MIB", "hh3cLswCpuMemoryLowFree"),
        ("HH3C-LSW-DEV-ADM-MIB", "hh3cLswCpuMemorySecureThreshold"),
        ("HH3C-LSW-DEV-ADM-MIB", "hh3cLswCpuMemoryEarlyWarningThreshold"),
        ("HH3C-LSW-DEV-ADM-MIB", "hh3cLswCpuMemoryNormalThreshold"),
        ("HH3C-LSW-DEV-ADM-MIB", "hh3cLswCpuMemoryMinorThreshold"),
        ("HH3C-LSW-DEV-ADM-MIB", "hh3cLswCpuMemorySevereThreshold"),
        ("HH3C-LSW-DEV-ADM-MIB", "hh3cLswCpuMemoryCriticalThreshold"),
        ("HH3C-LSW-DEV-ADM-MIB", "hh3cLswCpuMemoryCurrentState"),
        ("HH3C-LswTRAP-MIB", "hh3csLswTrapProcessMemoryInfo"),
        ("HH3C-LswTRAP-MIB", "hh3csLswTrapSlubInfo"))
)
if mibBuilder.loadTexts:
    hh3cMemoryUsageMinorNotification.setStatus(
        "current"
    )

hh3cMemoryUsageMinorRecoverNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 12, 1, 36)
)
hh3cMemoryUsageMinorRecoverNotification.setObjects(
      *(("HH3C-LSW-DEV-ADM-MIB", "hh3cLswFrameIndex"),
        ("HH3C-LSW-DEV-ADM-MIB", "hh3cLswSlotIndex"),
        ("HH3C-LSW-DEV-ADM-MIB", "hh3cLswCpuIndex"),
        ("HH3C-LSW-DEV-ADM-MIB", "hh3cLswCpuMemory"),
        ("HH3C-LSW-DEV-ADM-MIB", "hh3cLswCpuMemoryFree"),
        ("HH3C-LSW-DEV-ADM-MIB", "hh3cLswCpuMemoryFreeRatio"),
        ("HH3C-LSW-DEV-ADM-MIB", "hh3cLswCpuMemoryHighTotal"),
        ("HH3C-LSW-DEV-ADM-MIB", "hh3cLswCpuMemoryHighFree"),
        ("HH3C-LSW-DEV-ADM-MIB", "hh3cLswCpuMemoryLowTotal"),
        ("HH3C-LSW-DEV-ADM-MIB", "hh3cLswCpuMemoryLowFree"),
        ("HH3C-LSW-DEV-ADM-MIB", "hh3cLswCpuMemorySecureThreshold"),
        ("HH3C-LSW-DEV-ADM-MIB", "hh3cLswCpuMemoryEarlyWarningThreshold"),
        ("HH3C-LSW-DEV-ADM-MIB", "hh3cLswCpuMemoryNormalThreshold"),
        ("HH3C-LSW-DEV-ADM-MIB", "hh3cLswCpuMemoryMinorThreshold"),
        ("HH3C-LSW-DEV-ADM-MIB", "hh3cLswCpuMemorySevereThreshold"),
        ("HH3C-LSW-DEV-ADM-MIB", "hh3cLswCpuMemoryCriticalThreshold"),
        ("HH3C-LSW-DEV-ADM-MIB", "hh3cLswCpuMemoryCurrentState"),
        ("HH3C-LswTRAP-MIB", "hh3csLswTrapProcessMemoryInfo"),
        ("HH3C-LswTRAP-MIB", "hh3csLswTrapSlubInfo"))
)
if mibBuilder.loadTexts:
    hh3cMemoryUsageMinorRecoverNotification.setStatus(
        "current"
    )

hh3cMemoryUsageSevereNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 12, 1, 37)
)
hh3cMemoryUsageSevereNotification.setObjects(
      *(("HH3C-LSW-DEV-ADM-MIB", "hh3cLswFrameIndex"),
        ("HH3C-LSW-DEV-ADM-MIB", "hh3cLswSlotIndex"),
        ("HH3C-LSW-DEV-ADM-MIB", "hh3cLswCpuIndex"),
        ("HH3C-LSW-DEV-ADM-MIB", "hh3cLswCpuMemory"),
        ("HH3C-LSW-DEV-ADM-MIB", "hh3cLswCpuMemoryFree"),
        ("HH3C-LSW-DEV-ADM-MIB", "hh3cLswCpuMemoryFreeRatio"),
        ("HH3C-LSW-DEV-ADM-MIB", "hh3cLswCpuMemoryHighTotal"),
        ("HH3C-LSW-DEV-ADM-MIB", "hh3cLswCpuMemoryHighFree"),
        ("HH3C-LSW-DEV-ADM-MIB", "hh3cLswCpuMemoryLowTotal"),
        ("HH3C-LSW-DEV-ADM-MIB", "hh3cLswCpuMemoryLowFree"),
        ("HH3C-LSW-DEV-ADM-MIB", "hh3cLswCpuMemorySecureThreshold"),
        ("HH3C-LSW-DEV-ADM-MIB", "hh3cLswCpuMemoryEarlyWarningThreshold"),
        ("HH3C-LSW-DEV-ADM-MIB", "hh3cLswCpuMemoryNormalThreshold"),
        ("HH3C-LSW-DEV-ADM-MIB", "hh3cLswCpuMemoryMinorThreshold"),
        ("HH3C-LSW-DEV-ADM-MIB", "hh3cLswCpuMemorySevereThreshold"),
        ("HH3C-LSW-DEV-ADM-MIB", "hh3cLswCpuMemoryCriticalThreshold"),
        ("HH3C-LSW-DEV-ADM-MIB", "hh3cLswCpuMemoryCurrentState"),
        ("HH3C-LswTRAP-MIB", "hh3csLswTrapProcessMemoryInfo"),
        ("HH3C-LswTRAP-MIB", "hh3csLswTrapSlubInfo"))
)
if mibBuilder.loadTexts:
    hh3cMemoryUsageSevereNotification.setStatus(
        "current"
    )

hh3cMemoryUsageSevereRecoverNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 12, 1, 38)
)
hh3cMemoryUsageSevereRecoverNotification.setObjects(
      *(("HH3C-LSW-DEV-ADM-MIB", "hh3cLswFrameIndex"),
        ("HH3C-LSW-DEV-ADM-MIB", "hh3cLswSlotIndex"),
        ("HH3C-LSW-DEV-ADM-MIB", "hh3cLswCpuIndex"),
        ("HH3C-LSW-DEV-ADM-MIB", "hh3cLswCpuMemory"),
        ("HH3C-LSW-DEV-ADM-MIB", "hh3cLswCpuMemoryFree"),
        ("HH3C-LSW-DEV-ADM-MIB", "hh3cLswCpuMemoryFreeRatio"),
        ("HH3C-LSW-DEV-ADM-MIB", "hh3cLswCpuMemoryHighTotal"),
        ("HH3C-LSW-DEV-ADM-MIB", "hh3cLswCpuMemoryHighFree"),
        ("HH3C-LSW-DEV-ADM-MIB", "hh3cLswCpuMemoryLowTotal"),
        ("HH3C-LSW-DEV-ADM-MIB", "hh3cLswCpuMemoryLowFree"),
        ("HH3C-LSW-DEV-ADM-MIB", "hh3cLswCpuMemorySecureThreshold"),
        ("HH3C-LSW-DEV-ADM-MIB", "hh3cLswCpuMemoryEarlyWarningThreshold"),
        ("HH3C-LSW-DEV-ADM-MIB", "hh3cLswCpuMemoryNormalThreshold"),
        ("HH3C-LSW-DEV-ADM-MIB", "hh3cLswCpuMemoryMinorThreshold"),
        ("HH3C-LSW-DEV-ADM-MIB", "hh3cLswCpuMemorySevereThreshold"),
        ("HH3C-LSW-DEV-ADM-MIB", "hh3cLswCpuMemoryCriticalThreshold"),
        ("HH3C-LSW-DEV-ADM-MIB", "hh3cLswCpuMemoryCurrentState"),
        ("HH3C-LswTRAP-MIB", "hh3csLswTrapProcessMemoryInfo"),
        ("HH3C-LswTRAP-MIB", "hh3csLswTrapSlubInfo"))
)
if mibBuilder.loadTexts:
    hh3cMemoryUsageSevereRecoverNotification.setStatus(
        "current"
    )

hh3cMemoryUsageCriticalNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 12, 1, 39)
)
hh3cMemoryUsageCriticalNotification.setObjects(
      *(("HH3C-LSW-DEV-ADM-MIB", "hh3cLswFrameIndex"),
        ("HH3C-LSW-DEV-ADM-MIB", "hh3cLswSlotIndex"),
        ("HH3C-LSW-DEV-ADM-MIB", "hh3cLswCpuIndex"),
        ("HH3C-LSW-DEV-ADM-MIB", "hh3cLswCpuMemory"),
        ("HH3C-LSW-DEV-ADM-MIB", "hh3cLswCpuMemoryFree"),
        ("HH3C-LSW-DEV-ADM-MIB", "hh3cLswCpuMemoryFreeRatio"),
        ("HH3C-LSW-DEV-ADM-MIB", "hh3cLswCpuMemoryHighTotal"),
        ("HH3C-LSW-DEV-ADM-MIB", "hh3cLswCpuMemoryHighFree"),
        ("HH3C-LSW-DEV-ADM-MIB", "hh3cLswCpuMemoryLowTotal"),
        ("HH3C-LSW-DEV-ADM-MIB", "hh3cLswCpuMemoryLowFree"),
        ("HH3C-LSW-DEV-ADM-MIB", "hh3cLswCpuMemorySecureThreshold"),
        ("HH3C-LSW-DEV-ADM-MIB", "hh3cLswCpuMemoryEarlyWarningThreshold"),
        ("HH3C-LSW-DEV-ADM-MIB", "hh3cLswCpuMemoryNormalThreshold"),
        ("HH3C-LSW-DEV-ADM-MIB", "hh3cLswCpuMemoryMinorThreshold"),
        ("HH3C-LSW-DEV-ADM-MIB", "hh3cLswCpuMemorySevereThreshold"),
        ("HH3C-LSW-DEV-ADM-MIB", "hh3cLswCpuMemoryCriticalThreshold"),
        ("HH3C-LSW-DEV-ADM-MIB", "hh3cLswCpuMemoryCurrentState"),
        ("HH3C-LswTRAP-MIB", "hh3csLswTrapProcessMemoryInfo"),
        ("HH3C-LswTRAP-MIB", "hh3csLswTrapSlubInfo"))
)
if mibBuilder.loadTexts:
    hh3cMemoryUsageCriticalNotification.setStatus(
        "current"
    )

hh3cMemoryUsageCriticalRecoverNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 12, 1, 40)
)
hh3cMemoryUsageCriticalRecoverNotification.setObjects(
      *(("HH3C-LSW-DEV-ADM-MIB", "hh3cLswFrameIndex"),
        ("HH3C-LSW-DEV-ADM-MIB", "hh3cLswSlotIndex"),
        ("HH3C-LSW-DEV-ADM-MIB", "hh3cLswCpuIndex"),
        ("HH3C-LSW-DEV-ADM-MIB", "hh3cLswCpuMemory"),
        ("HH3C-LSW-DEV-ADM-MIB", "hh3cLswCpuMemoryFree"),
        ("HH3C-LSW-DEV-ADM-MIB", "hh3cLswCpuMemoryFreeRatio"),
        ("HH3C-LSW-DEV-ADM-MIB", "hh3cLswCpuMemoryHighTotal"),
        ("HH3C-LSW-DEV-ADM-MIB", "hh3cLswCpuMemoryHighFree"),
        ("HH3C-LSW-DEV-ADM-MIB", "hh3cLswCpuMemoryLowTotal"),
        ("HH3C-LSW-DEV-ADM-MIB", "hh3cLswCpuMemoryLowFree"),
        ("HH3C-LSW-DEV-ADM-MIB", "hh3cLswCpuMemorySecureThreshold"),
        ("HH3C-LSW-DEV-ADM-MIB", "hh3cLswCpuMemoryEarlyWarningThreshold"),
        ("HH3C-LSW-DEV-ADM-MIB", "hh3cLswCpuMemoryNormalThreshold"),
        ("HH3C-LSW-DEV-ADM-MIB", "hh3cLswCpuMemoryMinorThreshold"),
        ("HH3C-LSW-DEV-ADM-MIB", "hh3cLswCpuMemorySevereThreshold"),
        ("HH3C-LSW-DEV-ADM-MIB", "hh3cLswCpuMemoryCriticalThreshold"),
        ("HH3C-LSW-DEV-ADM-MIB", "hh3cLswCpuMemoryCurrentState"),
        ("HH3C-LswTRAP-MIB", "hh3csLswTrapProcessMemoryInfo"),
        ("HH3C-LswTRAP-MIB", "hh3csLswTrapSlubInfo"))
)
if mibBuilder.loadTexts:
    hh3cMemoryUsageCriticalRecoverNotification.setStatus(
        "current"
    )

hh3cCoreUsageNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 12, 3, 0, 1)
)
hh3cCoreUsageNotification.setObjects(
      *(("HH3C-LSW-DEV-ADM-MIB", "hh3cLswFrameIndex"),
        ("HH3C-LSW-DEV-ADM-MIB", "hh3cLswSlotIndex"),
        ("HH3C-LSW-DEV-ADM-MIB", "hh3cLswCpuIndex"),
        ("HH3C-LSW-DEV-ADM-MIB", "hh3cLswCoreIndex"),
        ("HH3C-LswTRAP-MIB", "hh3cLswCoreTrapUsage"),
        ("HH3C-LSW-DEV-ADM-MIB", "hh3cLswCoreThreshold"),
        ("HH3C-LswTRAP-MIB", "hh3cLswTrapCpuUsage"),
        ("HH3C-LswTRAP-MIB", "hh3cLswTrapCoreProcessInfo"),
        ("HH3C-LSW-DEV-ADM-MIB", "hh3cLswCoreMinorThreshold"),
        ("HH3C-LSW-DEV-ADM-MIB", "hh3cLswCoreRecoveryThreshold"))
)
if mibBuilder.loadTexts:
    hh3cCoreUsageNotification.setStatus(
        "current"
    )

hh3cBoardPowerNotEnough = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 12, 3, 0, 2)
)
hh3cBoardPowerNotEnough.setObjects(
      *(("HH3C-LSW-DEV-ADM-MIB", "hh3cLswFrameIndex"),
        ("HH3C-LSW-DEV-ADM-MIB", "hh3cLswSlotIndex"),
        ("HH3C-LswTRAP-MIB", "hh3cBoardAvailablePower"),
        ("HH3C-LswTRAP-MIB", "hh3cBoardRequiredPower"))
)
if mibBuilder.loadTexts:
    hh3cBoardPowerNotEnough.setStatus(
        "current"
    )

hh3cAlarmInPortIn = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 12, 3, 0, 3)
)
hh3cAlarmInPortIn.setObjects(
      *(("HH3C-LSW-DEV-ADM-MIB", "hh3cLswFrameIndex"),
        ("HH3C-LSW-DEV-ADM-MIB", "hh3cLswSlotIndex"),
        ("HH3C-LswTRAP-MIB", "hh3cLswAlarmInPortInNum"))
)
if mibBuilder.loadTexts:
    hh3cAlarmInPortIn.setStatus(
        "current"
    )

hh3cAlarmInPortRecover = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 12, 3, 0, 4)
)
hh3cAlarmInPortRecover.setObjects(
      *(("HH3C-LSW-DEV-ADM-MIB", "hh3cLswFrameIndex"),
        ("HH3C-LSW-DEV-ADM-MIB", "hh3cLswSlotIndex"),
        ("HH3C-LswTRAP-MIB", "hh3cLswAlarmInPortInNum"))
)
if mibBuilder.loadTexts:
    hh3cAlarmInPortRecover.setStatus(
        "current"
    )

hh3cCoreUsageSevereRecoveryNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 12, 3, 0, 10)
)
hh3cCoreUsageSevereRecoveryNotification.setObjects(
      *(("HH3C-LSW-DEV-ADM-MIB", "hh3cLswFrameIndex"),
        ("HH3C-LSW-DEV-ADM-MIB", "hh3cLswSlotIndex"),
        ("HH3C-LSW-DEV-ADM-MIB", "hh3cLswCpuIndex"),
        ("HH3C-LSW-DEV-ADM-MIB", "hh3cLswCoreIndex"),
        ("HH3C-LswTRAP-MIB", "hh3cLswCoreTrapUsage"),
        ("HH3C-LSW-DEV-ADM-MIB", "hh3cLswCoreThreshold"),
        ("HH3C-LswTRAP-MIB", "hh3cLswTrapCpuUsage"),
        ("HH3C-LswTRAP-MIB", "hh3cLswTrapCoreProcessInfo"),
        ("HH3C-LSW-DEV-ADM-MIB", "hh3cLswCoreMinorThreshold"),
        ("HH3C-LSW-DEV-ADM-MIB", "hh3cLswCoreRecoveryThreshold"))
)
if mibBuilder.loadTexts:
    hh3cCoreUsageSevereRecoveryNotification.setStatus(
        "current"
    )

hh3cCoreUsageMinorNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 12, 3, 0, 11)
)
hh3cCoreUsageMinorNotification.setObjects(
      *(("HH3C-LSW-DEV-ADM-MIB", "hh3cLswFrameIndex"),
        ("HH3C-LSW-DEV-ADM-MIB", "hh3cLswSlotIndex"),
        ("HH3C-LSW-DEV-ADM-MIB", "hh3cLswCpuIndex"),
        ("HH3C-LSW-DEV-ADM-MIB", "hh3cLswCoreIndex"),
        ("HH3C-LswTRAP-MIB", "hh3cLswCoreTrapUsage"),
        ("HH3C-LSW-DEV-ADM-MIB", "hh3cLswCoreThreshold"),
        ("HH3C-LswTRAP-MIB", "hh3cLswTrapCpuUsage"),
        ("HH3C-LswTRAP-MIB", "hh3cLswTrapCoreProcessInfo"),
        ("HH3C-LSW-DEV-ADM-MIB", "hh3cLswCoreMinorThreshold"),
        ("HH3C-LSW-DEV-ADM-MIB", "hh3cLswCoreRecoveryThreshold"))
)
if mibBuilder.loadTexts:
    hh3cCoreUsageMinorNotification.setStatus(
        "current"
    )

hh3cCoreUsageMinorRecoveryNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 12, 3, 0, 12)
)
hh3cCoreUsageMinorRecoveryNotification.setObjects(
      *(("HH3C-LSW-DEV-ADM-MIB", "hh3cLswFrameIndex"),
        ("HH3C-LSW-DEV-ADM-MIB", "hh3cLswSlotIndex"),
        ("HH3C-LSW-DEV-ADM-MIB", "hh3cLswCpuIndex"),
        ("HH3C-LSW-DEV-ADM-MIB", "hh3cLswCoreIndex"),
        ("HH3C-LswTRAP-MIB", "hh3cLswCoreTrapUsage"),
        ("HH3C-LSW-DEV-ADM-MIB", "hh3cLswCoreThreshold"),
        ("HH3C-LswTRAP-MIB", "hh3cLswTrapCpuUsage"),
        ("HH3C-LswTRAP-MIB", "hh3cLswTrapCoreProcessInfo"),
        ("HH3C-LSW-DEV-ADM-MIB", "hh3cLswCoreMinorThreshold"),
        ("HH3C-LSW-DEV-ADM-MIB", "hh3cLswCoreRecoveryThreshold"))
)
if mibBuilder.loadTexts:
    hh3cCoreUsageMinorRecoveryNotification.setStatus(
        "current"
    )

hh3cDMAMemoryUsageCriticalNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 12, 3, 0, 41)
)
hh3cDMAMemoryUsageCriticalNotification.setObjects(
      *(("HH3C-LSW-DEV-ADM-MIB", "hh3cLswFrameIndex"),
        ("HH3C-LSW-DEV-ADM-MIB", "hh3cLswSlotIndex"),
        ("HH3C-LSW-DEV-ADM-MIB", "hh3cLswCpuIndex"),
        ("HH3C-LswTRAP-MIB", "hh3cDMAMemoryTotal"),
        ("HH3C-LswTRAP-MIB", "hh3cDMAMemoryUsed"),
        ("HH3C-LswTRAP-MIB", "hh3cDMAMemoryFree"),
        ("HH3C-LswTRAP-MIB", "hh3cDMAMemoryCurrentState"),
        ("HH3C-LswTRAP-MIB", "hh3cDMAMemoryFreeRatio"),
        ("HH3C-LswTRAP-MIB", "hh3cDMAMemoryCriticalThreshold"))
)
if mibBuilder.loadTexts:
    hh3cDMAMemoryUsageCriticalNotification.setStatus(
        "current"
    )

hh3cDMAMemoryUsageRecoverNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 12, 3, 0, 42)
)
hh3cDMAMemoryUsageRecoverNotification.setObjects(
      *(("HH3C-LSW-DEV-ADM-MIB", "hh3cLswFrameIndex"),
        ("HH3C-LSW-DEV-ADM-MIB", "hh3cLswSlotIndex"),
        ("HH3C-LSW-DEV-ADM-MIB", "hh3cLswCpuIndex"),
        ("HH3C-LswTRAP-MIB", "hh3cDMAMemoryTotal"),
        ("HH3C-LswTRAP-MIB", "hh3cDMAMemoryUsed"),
        ("HH3C-LswTRAP-MIB", "hh3cDMAMemoryFree"),
        ("HH3C-LswTRAP-MIB", "hh3cDMAMemoryCurrentState"),
        ("HH3C-LswTRAP-MIB", "hh3cDMAMemoryFreeRatio"),
        ("HH3C-LswTRAP-MIB", "hh3cDMAMemoryRecoverThreshold"))
)
if mibBuilder.loadTexts:
    hh3cDMAMemoryUsageRecoverNotification.setStatus(
        "current"
    )

hh3cRemainingPowerNotEnough = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 12, 3, 0, 43)
)
hh3cRemainingPowerNotEnough.setObjects(
      *(("HH3C-LSW-DEV-ADM-MIB", "hh3cLswFrameIndex"),
        ("HH3C-LswTRAP-MIB", "hh3cFrameRemainingPower"))
)
if mibBuilder.loadTexts:
    hh3cRemainingPowerNotEnough.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HH3C-LswTRAP-MIB",
    **{"hh3cLswTrapMib": hh3cLswTrapMib,
       "hh3csLswTRAPMibObject": hh3csLswTRAPMibObject,
       "hh3cpowerfailure": hh3cpowerfailure,
       "hh3cPowerNormal": hh3cPowerNormal,
       "hh3cMasterPowerNormal": hh3cMasterPowerNormal,
       "hh3cSlavePowerNormal": hh3cSlavePowerNormal,
       "hh3cPowerRemoved": hh3cPowerRemoved,
       "hh3cfanfailure": hh3cfanfailure,
       "hh3cFanNormal": hh3cFanNormal,
       "hh3cBoardRemoved": hh3cBoardRemoved,
       "hh3cBoardInserted": hh3cBoardInserted,
       "hh3cBoardFailure": hh3cBoardFailure,
       "hh3cBoardNormal": hh3cBoardNormal,
       "hh3cSubcardRemove": hh3cSubcardRemove,
       "hh3cSubcardInsert": hh3cSubcardInsert,
       "hh3cBoardTemperatureLower": hh3cBoardTemperatureLower,
       "hh3cBoardTemperatureFromLowerToNormal": hh3cBoardTemperatureFromLowerToNormal,
       "hh3cBoardTemperatureHigher": hh3cBoardTemperatureHigher,
       "hh3cBoardTemperatureFormHigherToNormal": hh3cBoardTemperatureFormHigherToNormal,
       "hh3cRequestLoading": hh3cRequestLoading,
       "hh3cLoadFailure": hh3cLoadFailure,
       "hh3cLoadFinished": hh3cLoadFinished,
       "hh3cBackBoardModeSetFuilure": hh3cBackBoardModeSetFuilure,
       "hh3cBackBoardModeSetOK": hh3cBackBoardModeSetOK,
       "hh3cPowerInserted": hh3cPowerInserted,
       "hh3cBootImageUpdated": hh3cBootImageUpdated,
       "hh3cCpuRemoved": hh3cCpuRemoved,
       "hh3cCpuFailure": hh3cCpuFailure,
       "hh3cCpuNormal": hh3cCpuNormal,
       "hh3cPowerIncompatible": hh3cPowerIncompatible,
       "hh3cCpuUsageSevereNotification": hh3cCpuUsageSevereNotification,
       "hh3cCpuUsageSevereRecoverNotification": hh3cCpuUsageSevereRecoverNotification,
       "hh3cCpuUsageMinorNotification": hh3cCpuUsageMinorNotification,
       "hh3cCpuUsageMinorRecoverNotification": hh3cCpuUsageMinorRecoverNotification,
       "hh3cMemoryUsageEarlyWarningNotification": hh3cMemoryUsageEarlyWarningNotification,
       "hh3cMemoryUsageEarlyWarningRecoverNotification": hh3cMemoryUsageEarlyWarningRecoverNotification,
       "hh3cMemoryUsageMinorNotification": hh3cMemoryUsageMinorNotification,
       "hh3cMemoryUsageMinorRecoverNotification": hh3cMemoryUsageMinorRecoverNotification,
       "hh3cMemoryUsageSevereNotification": hh3cMemoryUsageSevereNotification,
       "hh3cMemoryUsageSevereRecoverNotification": hh3cMemoryUsageSevereRecoverNotification,
       "hh3cMemoryUsageCriticalNotification": hh3cMemoryUsageCriticalNotification,
       "hh3cMemoryUsageCriticalRecoverNotification": hh3cMemoryUsageCriticalRecoverNotification,
       "hh3cNetworkHealthMonitorFailure": hh3cNetworkHealthMonitorFailure,
       "hh3cNetworkHealthMonitorNormal": hh3cNetworkHealthMonitorNormal,
       "hh3csLswTRAPMibInfor": hh3csLswTRAPMibInfor,
       "hh3csLswTrapCpuCoreInfo": hh3csLswTrapCpuCoreInfo,
       "hh3csLswTrapProcessCpuInfo": hh3csLswTrapProcessCpuInfo,
       "hh3csLswTrapProcessMemoryInfo": hh3csLswTrapProcessMemoryInfo,
       "hh3csLswTrapSlubInfo": hh3csLswTrapSlubInfo,
       "hh3cLswTrapCpuUsage": hh3cLswTrapCpuUsage,
       "hh3cLswTrapCoreProcessInfo": hh3cLswTrapCoreProcessInfo,
       "hh3cLswCoreTrapUsage": hh3cLswCoreTrapUsage,
       "hh3cBoardAvailablePower": hh3cBoardAvailablePower,
       "hh3cBoardRequiredPower": hh3cBoardRequiredPower,
       "hh3cLswAlarmInPortInNum": hh3cLswAlarmInPortInNum,
       "hh3cDMAMemoryTotal": hh3cDMAMemoryTotal,
       "hh3cDMAMemoryUsed": hh3cDMAMemoryUsed,
       "hh3cDMAMemoryFree": hh3cDMAMemoryFree,
       "hh3cDMAMemoryFreeRatio": hh3cDMAMemoryFreeRatio,
       "hh3cDMAMemoryCriticalThreshold": hh3cDMAMemoryCriticalThreshold,
       "hh3cDMAMemoryRecoverThreshold": hh3cDMAMemoryRecoverThreshold,
       "hh3cDMAMemoryCurrentState": hh3cDMAMemoryCurrentState,
       "hh3cFrameRemainingPower": hh3cFrameRemainingPower,
       "hh3csLswTRAPMibObjectV2": hh3csLswTRAPMibObjectV2,
       "hh3csLswTRAPMibObjectV2Prefix": hh3csLswTRAPMibObjectV2Prefix,
       "hh3cCoreUsageNotification": hh3cCoreUsageNotification,
       "hh3cBoardPowerNotEnough": hh3cBoardPowerNotEnough,
       "hh3cAlarmInPortIn": hh3cAlarmInPortIn,
       "hh3cAlarmInPortRecover": hh3cAlarmInPortRecover,
       "hh3cCoreUsageSevereRecoveryNotification": hh3cCoreUsageSevereRecoveryNotification,
       "hh3cCoreUsageMinorNotification": hh3cCoreUsageMinorNotification,
       "hh3cCoreUsageMinorRecoveryNotification": hh3cCoreUsageMinorRecoveryNotification,
       "hh3cDMAMemoryUsageCriticalNotification": hh3cDMAMemoryUsageCriticalNotification,
       "hh3cDMAMemoryUsageRecoverNotification": hh3cDMAMemoryUsageRecoverNotification,
       "hh3cRemainingPowerNotEnough": hh3cRemainingPowerNotEnough}
)
