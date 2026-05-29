# SNMP MIB module (FORTINET-FORTIMANAGER-FORTIANALYZER-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\fortinet\FORTINET-FORTIMANAGER-FORTIANALYZER-MIB

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

(FnBoolState,
 FnIndex,
 fnGenTrapMsg,
 fnSysSerial,
 fortinet) = mibBuilder.importSymbols(
    "FORTINET-CORE-MIB",
    "FnBoolState",
    "FnIndex",
    "fnGenTrapMsg",
    "fnSysSerial",
    "fortinet")

(InetAddress,
 InetPortNumber) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetPortNumber")

(ModuleCompliance,
 NotificationGroup,
 ObjectGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup",
    "ObjectGroup")

(sysName,) = mibBuilder.importSymbols(
    "SNMPv2-MIB",
    "sysName")

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

fnFortiManagerMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 103)
)
if mibBuilder.loadTexts:
    fnFortiManagerMib.setRevisions(
        ("2022-04-23 00:00",
         "2022-02-04 00:00",
         "2021-05-13 00:00",
         "2020-02-12 00:00",
         "2019-08-21 00:00",
         "2018-08-07 00:00",
         "2017-10-13 00:00",
         "2017-07-27 00:00",
         "2017-06-28 00:00",
         "2015-08-15 00:00",
         "2015-06-12 00:00",
         "2014-04-22 00:00",
         "2013-06-10 00:00",
         "2013-03-27 00:00",
         "2012-11-26 00:00",
         "2012-04-20 00:00",
         "2011-03-25 00:00",
         "2011-01-19 00:00",
         "2008-07-18 00:00",
         "2008-06-26 00:00",
         "2008-06-16 00:00",
         "2008-06-10 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class FmTenths(TextualConvention, Gauge32):
    status = "current"
    displayHint = "d-1"


class FmHundredths(TextualConvention, Gauge32):
    status = "current"
    displayHint = "d-2"


class FmRAIDStatusCode(TextualConvention, Integer32):
    status = "current"
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
              9,
              10,
              11,
              12,
              100,
              101,
              102,
              103,
              104,
              105,
              200,
              201,
              202,
              203,
              204,
              205,
              206)
        )
    )
    namedValues = NamedValues(
        *(("arrayOK", 1),
          ("arrayDegraded", 2),
          ("arrayFailed", 3),
          ("arrayRebuilding", 4),
          ("arrayRebuildingStarted", 5),
          ("arrayRebuildingFinished", 6),
          ("arrayInitializing", 7),
          ("arrayInitializingStarted", 8),
          ("arrayInitializingFinished", 9),
          ("diskOk", 10),
          ("diskDegraded", 11),
          ("diskFailEvent", 12),
          ("diskUnavailable", 100),
          ("diskUnused", 101),
          ("diskOK", 102),
          ("diskRebuilding", 103),
          ("diskFailed", 104),
          ("diskSpare", 105),
          ("raidUnavailable", 200),
          ("raidOK", 201),
          ("raidDegraded", 202),
          ("raidFailed", 203),
          ("raidBackground-Initializing", 204),
          ("raidBackground-Verifying", 205),
          ("raidBackground-Rebuilding", 206))
    )



class FmSessProto(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              4,
              6,
              8,
              12,
              17,
              22,
              41,
              46,
              47,
              50,
              51,
              89,
              103,
              108,
              255)
        )
    )
    namedValues = NamedValues(
        *(("ip", 0),
          ("icmp", 1),
          ("igmp", 2),
          ("ipip", 4),
          ("tcp", 6),
          ("egp", 8),
          ("pup", 12),
          ("udp", 17),
          ("idp", 22),
          ("ipv6", 41),
          ("rsvp", 46),
          ("gre", 47),
          ("esp", 50),
          ("ah", 51),
          ("ospf", 89),
          ("pim", 103),
          ("comp", 108),
          ("raw", 255))
    )



class FmAdomEntMode(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("normal", 1),
          ("backup", 2))
    )



class FmAdomEntVpnMode(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("central-console", 1),
          ("policy-and-device", 2),
          ("not-applicable", 3))
    )



class FmDeviceEntMode(TextualConvention, Integer32):
    status = "current"
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
        *(("unregistered", 0),
          ("fmg", 1),
          ("faz", 2),
          ("fmg-faz", 3))
    )



class FmDeviceEntHaMode(TextualConvention, Integer32):
    status = "current"
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
        *(("standalone", 0),
          ("a-p", 1),
          ("a-a", 2),
          ("elbc", 3),
          ("dual", 4),
          ("fmg", 5))
    )



class FmDeviceEntConnectState(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 0),
          ("up", 1),
          ("down", 2))
    )



class FmDeviceEntDbState(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 0),
          ("not-modified", 1),
          ("modified", 2))
    )



class FmDeviceEntConfigState(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 0),
          ("in-sync", 1),
          ("out-of-sync", 2))
    )



class FmDeviceEntState(TextualConvention, Integer32):
    status = "current"
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
              15)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("unknown", 1),
          ("checked-in", 2),
          ("in-progress", 3),
          ("installed", 4),
          ("aborted", 5),
          ("sched", 6),
          ("retry", 7),
          ("canceled", 8),
          ("pending", 9),
          ("retrieved", 10),
          ("changed-conf", 11),
          ("sync-fail", 12),
          ("timeout", 13),
          ("rev-reverted", 14),
          ("auto-updated", 15))
    )



class FmDeviceEntSupportState(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("expired", 0),
          ("valid", 1))
    )



class FmRaidLevel(TextualConvention, Integer32):
    status = "current"
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
        *(("unavailable", 0),
          ("linear", 1),
          ("raid-0", 2),
          ("raid-1", 3),
          ("raid-1s", 4),
          ("raid-5", 5),
          ("raid-5s", 6),
          ("raid-6", 7),
          ("raid-6s", 8),
          ("raid-10", 9),
          ("raid-10s", 10),
          ("raid-50", 11),
          ("raid-50s", 12),
          ("raid-60", 13),
          ("raid-60s", 14))
    )



class FmRaidState(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("unavailable", 0),
          ("ok", 1),
          ("degraded", 2),
          ("failed", 3),
          ("background-initializing", 4),
          ("background-verifying", 5),
          ("background-rebuilding", 6))
    )



class FmRaidDiskEntState(TextualConvention, Integer32):
    status = "current"
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
        *(("unavailable", 0),
          ("failed", 1),
          ("unused", 2),
          ("ok", 3),
          ("rebuilding", 4),
          ("spare", 5))
    )



class FmSensorEntType(TextualConvention, Integer32):
    status = "current"
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
        *(("power", 0),
          ("fan", 1),
          ("temperature", 2),
          ("voltage", 3))
    )



class FmSensorEntState(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("ok", 0),
          ("failed", 1),
          ("out-of-range-not-critical", 2),
          ("out-of-range-critical", 3),
          ("out-of-range-not-recoverable", 4),
          ("input-lost", 5),
          ("not-present", 6))
    )



class FmHaMode(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("standalone", 0),
          ("master", 1),
          ("slave", 2))
    )



class FmHaPeerEntState(TextualConvention, Integer32):
    status = "current"
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
        *(("down", 0),
          ("negotiating", 1),
          ("synchronizing", 2),
          ("up", 3))
    )



class FmUmServiceStatus(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 0),
          ("up", 1),
          ("down", 2))
    )



class FmUmBoolState(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 0),
          ("yes", 1),
          ("no", 2))
    )



# MIB Managed Objects in the order of their OIDs

_FmTraps_ObjectIdentity = ObjectIdentity
fmTraps = _FmTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 103, 0)
)
_FmTrapPrefix_ObjectIdentity = ObjectIdentity
fmTrapPrefix = _FmTrapPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 103, 0, 0)
)
_FmTrapObject_ObjectIdentity = ObjectIdentity
fmTrapObject = _FmTrapObject_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 103, 0, 1)
)
_FmRAIDStatus_Type = FmRAIDStatusCode
_FmRAIDStatus_Object = MibScalar
fmRAIDStatus = _FmRAIDStatus_Object(
    (1, 3, 6, 1, 4, 1, 12356, 103, 0, 1, 1),
    _FmRAIDStatus_Type()
)
fmRAIDStatus.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    fmRAIDStatus.setStatus("current")


class _FmRAIDDevIndex_Type(DisplayString):
    """Custom type fmRAIDDevIndex based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_FmRAIDDevIndex_Type.__name__ = "DisplayString"
_FmRAIDDevIndex_Object = MibScalar
fmRAIDDevIndex = _FmRAIDDevIndex_Object(
    (1, 3, 6, 1, 4, 1, 12356, 103, 0, 1, 2),
    _FmRAIDDevIndex_Type()
)
fmRAIDDevIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    fmRAIDDevIndex.setStatus("current")
_FmLogRate_Type = Gauge32
_FmLogRate_Object = MibScalar
fmLogRate = _FmLogRate_Object(
    (1, 3, 6, 1, 4, 1, 12356, 103, 0, 1, 3),
    _FmLogRate_Type()
)
fmLogRate.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    fmLogRate.setStatus("current")
_FmLogRateThreshold_Type = Gauge32
_FmLogRateThreshold_Object = MibScalar
fmLogRateThreshold = _FmLogRateThreshold_Object(
    (1, 3, 6, 1, 4, 1, 12356, 103, 0, 1, 4),
    _FmLogRateThreshold_Type()
)
fmLogRateThreshold.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    fmLogRateThreshold.setStatus("current")
_FmLogDataRate_Type = Gauge32
_FmLogDataRate_Object = MibScalar
fmLogDataRate = _FmLogDataRate_Object(
    (1, 3, 6, 1, 4, 1, 12356, 103, 0, 1, 5),
    _FmLogDataRate_Type()
)
fmLogDataRate.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    fmLogDataRate.setStatus("current")
_FmLogDataRateThreshold_Type = Gauge32
_FmLogDataRateThreshold_Object = MibScalar
fmLogDataRateThreshold = _FmLogDataRateThreshold_Object(
    (1, 3, 6, 1, 4, 1, 12356, 103, 0, 1, 6),
    _FmLogDataRateThreshold_Type()
)
fmLogDataRateThreshold.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    fmLogDataRateThreshold.setStatus("current")
_FmLicGbDay_Type = Gauge32
_FmLicGbDay_Object = MibScalar
fmLicGbDay = _FmLicGbDay_Object(
    (1, 3, 6, 1, 4, 1, 12356, 103, 0, 1, 7),
    _FmLicGbDay_Type()
)
fmLicGbDay.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    fmLicGbDay.setStatus("current")
_FmLicGbDayThreshold_Type = Gauge32
_FmLicGbDayThreshold_Object = MibScalar
fmLicGbDayThreshold = _FmLicGbDayThreshold_Object(
    (1, 3, 6, 1, 4, 1, 12356, 103, 0, 1, 8),
    _FmLicGbDayThreshold_Type()
)
fmLicGbDayThreshold.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    fmLicGbDayThreshold.setStatus("current")
_FmLicDevQuota_Type = Gauge32
_FmLicDevQuota_Object = MibScalar
fmLicDevQuota = _FmLicDevQuota_Object(
    (1, 3, 6, 1, 4, 1, 12356, 103, 0, 1, 9),
    _FmLicDevQuota_Type()
)
fmLicDevQuota.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    fmLicDevQuota.setStatus("current")
_FmLicDevQuotaThreshold_Type = Gauge32
_FmLicDevQuotaThreshold_Object = MibScalar
fmLicDevQuotaThreshold = _FmLicDevQuotaThreshold_Object(
    (1, 3, 6, 1, 4, 1, 12356, 103, 0, 1, 10),
    _FmLicDevQuotaThreshold_Type()
)
fmLicDevQuotaThreshold.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    fmLicDevQuotaThreshold.setStatus("current")
_FmSensorState_Type = FmSensorEntState
_FmSensorState_Object = MibScalar
fmSensorState = _FmSensorState_Object(
    (1, 3, 6, 1, 4, 1, 12356, 103, 0, 1, 11),
    _FmSensorState_Type()
)
fmSensorState.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    fmSensorState.setStatus("current")
_FmSensorName_Type = DisplayString
_FmSensorName_Object = MibScalar
fmSensorName = _FmSensorName_Object(
    (1, 3, 6, 1, 4, 1, 12356, 103, 0, 1, 12),
    _FmSensorName_Type()
)
fmSensorName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    fmSensorName.setStatus("current")
_FmModel_ObjectIdentity = ObjectIdentity
fmModel = _FmModel_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 103, 1)
)
_Fmgvm_ObjectIdentity = ObjectIdentity
fmgvm = _Fmgvm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 103, 1, 64)
)
_Fmg100_ObjectIdentity = ObjectIdentity
fmg100 = _Fmg100_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 103, 1, 1000)
)
_Fmg100C_ObjectIdentity = ObjectIdentity
fmg100C = _Fmg100C_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 103, 1, 1003)
)
_Fmg200D_ObjectIdentity = ObjectIdentity
fmg200D = _Fmg200D_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 103, 1, 2004)
)
_Fmg200E_ObjectIdentity = ObjectIdentity
fmg200E = _Fmg200E_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 103, 1, 2005)
)
_Fmg200F_ObjectIdentity = ObjectIdentity
fmg200F = _Fmg200F_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 103, 1, 2006)
)
_Fmg200G_ObjectIdentity = ObjectIdentity
fmg200G = _Fmg200G_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 103, 1, 2007)
)
_Fmg300D_ObjectIdentity = ObjectIdentity
fmg300D = _Fmg300D_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 103, 1, 3004)
)
_Fmg300E_ObjectIdentity = ObjectIdentity
fmg300E = _Fmg300E_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 103, 1, 3005)
)
_Fmg300F_ObjectIdentity = ObjectIdentity
fmg300F = _Fmg300F_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 103, 1, 3006)
)
_Fmg400_ObjectIdentity = ObjectIdentity
fmg400 = _Fmg400_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 103, 1, 4000)
)
_Fmg400A_ObjectIdentity = ObjectIdentity
fmg400A = _Fmg400A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 103, 1, 4001)
)
_Fmg400B_ObjectIdentity = ObjectIdentity
fmg400B = _Fmg400B_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 103, 1, 4002)
)
_Fmg400C_ObjectIdentity = ObjectIdentity
fmg400C = _Fmg400C_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 103, 1, 4003)
)
_Fmg400E_ObjectIdentity = ObjectIdentity
fmg400E = _Fmg400E_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 103, 1, 4005)
)
_Fmg400G_ObjectIdentity = ObjectIdentity
fmg400G = _Fmg400G_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 103, 1, 4007)
)
_Fmg410G_ObjectIdentity = ObjectIdentity
fmg410G = _Fmg410G_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 103, 1, 4107)
)
_Fmg1000C_ObjectIdentity = ObjectIdentity
fmg1000C = _Fmg1000C_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 103, 1, 10003)
)
_Fmg1000D_ObjectIdentity = ObjectIdentity
fmg1000D = _Fmg1000D_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 103, 1, 10004)
)
_Fmg1000F_ObjectIdentity = ObjectIdentity
fmg1000F = _Fmg1000F_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 103, 1, 10006)
)
_Fmg1000G_ObjectIdentity = ObjectIdentity
fmg1000G = _Fmg1000G_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 103, 1, 10007)
)
_Fmg2000XL_ObjectIdentity = ObjectIdentity
fmg2000XL = _Fmg2000XL_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 103, 1, 20000)
)
_Fmg2000E_ObjectIdentity = ObjectIdentity
fmg2000E = _Fmg2000E_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 103, 1, 20005)
)
_Fmg3000_ObjectIdentity = ObjectIdentity
fmg3000 = _Fmg3000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 103, 1, 30000)
)
_Fmg3000B_ObjectIdentity = ObjectIdentity
fmg3000B = _Fmg3000B_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 103, 1, 30002)
)
_Fmg3000C_ObjectIdentity = ObjectIdentity
fmg3000C = _Fmg3000C_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 103, 1, 30003)
)
_Fmg3000F_ObjectIdentity = ObjectIdentity
fmg3000F = _Fmg3000F_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 103, 1, 30006)
)
_Fmg3000G_ObjectIdentity = ObjectIdentity
fmg3000G = _Fmg3000G_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 103, 1, 30007)
)
_Fmg3100G_ObjectIdentity = ObjectIdentity
fmg3100G = _Fmg3100G_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 103, 1, 31007)
)
_Fmg3700F_ObjectIdentity = ObjectIdentity
fmg3700F = _Fmg3700F_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 103, 1, 37006)
)
_Fmg3700G_ObjectIdentity = ObjectIdentity
fmg3700G = _Fmg3700G_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 103, 1, 37007)
)
_Fmg3900E_ObjectIdentity = ObjectIdentity
fmg3900E = _Fmg3900E_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 103, 1, 39005)
)
_Fmg4000D_ObjectIdentity = ObjectIdentity
fmg4000D = _Fmg4000D_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 103, 1, 40004)
)
_Fmg4000E_ObjectIdentity = ObjectIdentity
fmg4000E = _Fmg4000E_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 103, 1, 40005)
)
_Fmg5001A_ObjectIdentity = ObjectIdentity
fmg5001A = _Fmg5001A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 103, 1, 50011)
)
_FmSystem_ObjectIdentity = ObjectIdentity
fmSystem = _FmSystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 103, 2)
)
_FmSystemInfo_ObjectIdentity = ObjectIdentity
fmSystemInfo = _FmSystemInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 103, 2, 1)
)


class _FmSysCpuUsage_Type(Integer32):
    """Custom type fmSysCpuUsage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_FmSysCpuUsage_Type.__name__ = "Integer32"
_FmSysCpuUsage_Object = MibScalar
fmSysCpuUsage = _FmSysCpuUsage_Object(
    (1, 3, 6, 1, 4, 1, 12356, 103, 2, 1, 1),
    _FmSysCpuUsage_Type()
)
fmSysCpuUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fmSysCpuUsage.setStatus("current")
_FmSysMemUsed_Type = Gauge32
_FmSysMemUsed_Object = MibScalar
fmSysMemUsed = _FmSysMemUsed_Object(
    (1, 3, 6, 1, 4, 1, 12356, 103, 2, 1, 2),
    _FmSysMemUsed_Type()
)
fmSysMemUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fmSysMemUsed.setStatus("current")
_FmSysMemCapacity_Type = Gauge32
_FmSysMemCapacity_Object = MibScalar
fmSysMemCapacity = _FmSysMemCapacity_Object(
    (1, 3, 6, 1, 4, 1, 12356, 103, 2, 1, 3),
    _FmSysMemCapacity_Type()
)
fmSysMemCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fmSysMemCapacity.setStatus("current")
_FmSysDiskUsage_Type = Gauge32
_FmSysDiskUsage_Object = MibScalar
fmSysDiskUsage = _FmSysDiskUsage_Object(
    (1, 3, 6, 1, 4, 1, 12356, 103, 2, 1, 4),
    _FmSysDiskUsage_Type()
)
fmSysDiskUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fmSysDiskUsage.setStatus("current")
_FmSysDiskCapacity_Type = Gauge32
_FmSysDiskCapacity_Object = MibScalar
fmSysDiskCapacity = _FmSysDiskCapacity_Object(
    (1, 3, 6, 1, 4, 1, 12356, 103, 2, 1, 5),
    _FmSysDiskCapacity_Type()
)
fmSysDiskCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fmSysDiskCapacity.setStatus("current")


class _FmSysCpuUsageExcludedNice_Type(Gauge32):
    """Custom type fmSysCpuUsageExcludedNice based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_FmSysCpuUsageExcludedNice_Type.__name__ = "Gauge32"
_FmSysCpuUsageExcludedNice_Object = MibScalar
fmSysCpuUsageExcludedNice = _FmSysCpuUsageExcludedNice_Object(
    (1, 3, 6, 1, 4, 1, 12356, 103, 2, 1, 6),
    _FmSysCpuUsageExcludedNice_Type()
)
fmSysCpuUsageExcludedNice.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fmSysCpuUsageExcludedNice.setStatus("current")
_FmSysVersion_Type = DisplayString
_FmSysVersion_Object = MibScalar
fmSysVersion = _FmSysVersion_Object(
    (1, 3, 6, 1, 4, 1, 12356, 103, 2, 1, 7),
    _FmSysVersion_Type()
)
fmSysVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fmSysVersion.setStatus("current")
_FmSysUpTime_Type = Counter64
_FmSysUpTime_Object = MibScalar
fmSysUpTime = _FmSysUpTime_Object(
    (1, 3, 6, 1, 4, 1, 12356, 103, 2, 1, 8),
    _FmSysUpTime_Type()
)
fmSysUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fmSysUpTime.setStatus("current")
if mibBuilder.loadTexts:
    fmSysUpTime.setUnits("hundredths of a second")
_FmSysLogRate_Type = Gauge32
_FmSysLogRate_Object = MibScalar
fmSysLogRate = _FmSysLogRate_Object(
    (1, 3, 6, 1, 4, 1, 12356, 103, 2, 1, 9),
    _FmSysLogRate_Type()
)
fmSysLogRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fmSysLogRate.setStatus("current")
if mibBuilder.loadTexts:
    fmSysLogRate.setUnits("logs per second")
_FmSysLogRateHr_Type = FmHundredths
_FmSysLogRateHr_Object = MibScalar
fmSysLogRateHr = _FmSysLogRateHr_Object(
    (1, 3, 6, 1, 4, 1, 12356, 103, 2, 1, 10),
    _FmSysLogRateHr_Type()
)
fmSysLogRateHr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fmSysLogRateHr.setStatus("current")
if mibBuilder.loadTexts:
    fmSysLogRateHr.setUnits("logs per second")
_FmSysLogIndexingRate_Type = FmHundredths
_FmSysLogIndexingRate_Object = MibScalar
fmSysLogIndexingRate = _FmSysLogIndexingRate_Object(
    (1, 3, 6, 1, 4, 1, 12356, 103, 2, 1, 11),
    _FmSysLogIndexingRate_Type()
)
fmSysLogIndexingRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fmSysLogIndexingRate.setStatus("current")
if mibBuilder.loadTexts:
    fmSysLogIndexingRate.setUnits("logs per second")
_FmSysLogLagTime_Type = Gauge32
_FmSysLogLagTime_Object = MibScalar
fmSysLogLagTime = _FmSysLogLagTime_Object(
    (1, 3, 6, 1, 4, 1, 12356, 103, 2, 1, 12),
    _FmSysLogLagTime_Type()
)
fmSysLogLagTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fmSysLogLagTime.setStatus("current")
if mibBuilder.loadTexts:
    fmSysLogLagTime.setUnits("second")
_FmSysLicGbDayToday_Type = FmHundredths
_FmSysLicGbDayToday_Object = MibScalar
fmSysLicGbDayToday = _FmSysLicGbDayToday_Object(
    (1, 3, 6, 1, 4, 1, 12356, 103, 2, 1, 13),
    _FmSysLicGbDayToday_Type()
)
fmSysLicGbDayToday.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fmSysLicGbDayToday.setStatus("current")
_FmSysLicGbDayYesterday_Type = FmHundredths
_FmSysLicGbDayYesterday_Object = MibScalar
fmSysLicGbDayYesterday = _FmSysLicGbDayYesterday_Object(
    (1, 3, 6, 1, 4, 1, 12356, 103, 2, 1, 14),
    _FmSysLicGbDayYesterday_Type()
)
fmSysLicGbDayYesterday.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fmSysLicGbDayYesterday.setStatus("current")
_FmSysLicGbDayWeekAvg_Type = FmHundredths
_FmSysLicGbDayWeekAvg_Object = MibScalar
fmSysLicGbDayWeekAvg = _FmSysLicGbDayWeekAvg_Object(
    (1, 3, 6, 1, 4, 1, 12356, 103, 2, 1, 15),
    _FmSysLicGbDayWeekAvg_Type()
)
fmSysLicGbDayWeekAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fmSysLicGbDayWeekAvg.setStatus("current")
_FmSysDiskInfo_ObjectIdentity = ObjectIdentity
fmSysDiskInfo = _FmSysDiskInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 103, 2, 1, 16)
)
_FmSysDiskNumber_Type = Gauge32
_FmSysDiskNumber_Object = MibScalar
fmSysDiskNumber = _FmSysDiskNumber_Object(
    (1, 3, 6, 1, 4, 1, 12356, 103, 2, 1, 16, 1),
    _FmSysDiskNumber_Type()
)
fmSysDiskNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fmSysDiskNumber.setStatus("current")
_FmSysDiskTable_Object = MibTable
fmSysDiskTable = _FmSysDiskTable_Object(
    (1, 3, 6, 1, 4, 1, 12356, 103, 2, 1, 17)
)
if mibBuilder.loadTexts:
    fmSysDiskTable.setStatus("current")
_FmSysDiskEntry_Object = MibTableRow
fmSysDiskEntry = _FmSysDiskEntry_Object(
    (1, 3, 6, 1, 4, 1, 12356, 103, 2, 1, 17, 1)
)
fmSysDiskEntry.setIndexNames(
    (0, "FORTINET-FORTIMANAGER-FORTIANALYZER-MIB", "fmSysDiskEntIndex"),
)
if mibBuilder.loadTexts:
    fmSysDiskEntry.setStatus("current")
_FmSysDiskEntIndex_Type = FnIndex
_FmSysDiskEntIndex_Object = MibTableColumn
fmSysDiskEntIndex = _FmSysDiskEntIndex_Object(
    (1, 3, 6, 1, 4, 1, 12356, 103, 2, 1, 17, 1, 1),
    _FmSysDiskEntIndex_Type()
)
fmSysDiskEntIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fmSysDiskEntIndex.setStatus("current")
_FmSysDiskEntName_Type = DisplayString
_FmSysDiskEntName_Object = MibTableColumn
fmSysDiskEntName = _FmSysDiskEntName_Object(
    (1, 3, 6, 1, 4, 1, 12356, 103, 2, 1, 17, 1, 2),
    _FmSysDiskEntName_Type()
)
fmSysDiskEntName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fmSysDiskEntName.setStatus("current")
_FmSysDiskEntUsage_Type = Gauge32
_FmSysDiskEntUsage_Object = MibTableColumn
fmSysDiskEntUsage = _FmSysDiskEntUsage_Object(
    (1, 3, 6, 1, 4, 1, 12356, 103, 2, 1, 17, 1, 3),
    _FmSysDiskEntUsage_Type()
)
fmSysDiskEntUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fmSysDiskEntUsage.setStatus("current")
_FmSysDiskEntCapacity_Type = Gauge32
_FmSysDiskEntCapacity_Object = MibTableColumn
fmSysDiskEntCapacity = _FmSysDiskEntCapacity_Object(
    (1, 3, 6, 1, 4, 1, 12356, 103, 2, 1, 17, 1, 4),
    _FmSysDiskEntCapacity_Type()
)
fmSysDiskEntCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fmSysDiskEntCapacity.setStatus("current")
_FmSysDiskEntIOUtil_Type = FmTenths
_FmSysDiskEntIOUtil_Object = MibTableColumn
fmSysDiskEntIOUtil = _FmSysDiskEntIOUtil_Object(
    (1, 3, 6, 1, 4, 1, 12356, 103, 2, 1, 17, 1, 5),
    _FmSysDiskEntIOUtil_Type()
)
fmSysDiskEntIOUtil.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fmSysDiskEntIOUtil.setStatus("current")
_FmSysLogForwardInfo_ObjectIdentity = ObjectIdentity
fmSysLogForwardInfo = _FmSysLogForwardInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 103, 2, 1, 18)
)
_FmSysLogForwardNumber_Type = Gauge32
_FmSysLogForwardNumber_Object = MibScalar
fmSysLogForwardNumber = _FmSysLogForwardNumber_Object(
    (1, 3, 6, 1, 4, 1, 12356, 103, 2, 1, 18, 1),
    _FmSysLogForwardNumber_Type()
)
fmSysLogForwardNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fmSysLogForwardNumber.setStatus("current")
_FmSysLogForwardTable_Object = MibTable
fmSysLogForwardTable = _FmSysLogForwardTable_Object(
    (1, 3, 6, 1, 4, 1, 12356, 103, 2, 1, 19)
)
if mibBuilder.loadTexts:
    fmSysLogForwardTable.setStatus("current")
_FmSysLogForwardEntry_Object = MibTableRow
fmSysLogForwardEntry = _FmSysLogForwardEntry_Object(
    (1, 3, 6, 1, 4, 1, 12356, 103, 2, 1, 19, 1)
)
fmSysLogForwardEntry.setIndexNames(
    (0, "FORTINET-FORTIMANAGER-FORTIANALYZER-MIB", "fmSysLogForwardIndex"),
)
if mibBuilder.loadTexts:
    fmSysLogForwardEntry.setStatus("current")
_FmSysLogForwardIndex_Type = FnIndex
_FmSysLogForwardIndex_Object = MibTableColumn
fmSysLogForwardIndex = _FmSysLogForwardIndex_Object(
    (1, 3, 6, 1, 4, 1, 12356, 103, 2, 1, 19, 1, 1),
    _FmSysLogForwardIndex_Type()
)
fmSysLogForwardIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fmSysLogForwardIndex.setStatus("current")
_FmSysLogForwardName_Type = DisplayString
_FmSysLogForwardName_Object = MibTableColumn
fmSysLogForwardName = _FmSysLogForwardName_Object(
    (1, 3, 6, 1, 4, 1, 12356, 103, 2, 1, 19, 1, 2),
    _FmSysLogForwardName_Type()
)
fmSysLogForwardName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fmSysLogForwardName.setStatus("current")
_FmSysLogForwardRate_Type = FmHundredths
_FmSysLogForwardRate_Object = MibTableColumn
fmSysLogForwardRate = _FmSysLogForwardRate_Object(
    (1, 3, 6, 1, 4, 1, 12356, 103, 2, 1, 19, 1, 3),
    _FmSysLogForwardRate_Type()
)
fmSysLogForwardRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fmSysLogForwardRate.setStatus("current")
if mibBuilder.loadTexts:
    fmSysLogForwardRate.setUnits("logs per second")
_FaModel_ObjectIdentity = ObjectIdentity
faModel = _FaModel_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 103, 3)
)
_Fazvm_ObjectIdentity = ObjectIdentity
fazvm = _Fazvm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 103, 3, 64)
)
_Faz100_ObjectIdentity = ObjectIdentity
faz100 = _Faz100_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 103, 3, 1000)
)
_Faz100A_ObjectIdentity = ObjectIdentity
faz100A = _Faz100A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 103, 3, 1001)
)
_Faz100B_ObjectIdentity = ObjectIdentity
faz100B = _Faz100B_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 103, 3, 1002)
)
_Faz100C_ObjectIdentity = ObjectIdentity
faz100C = _Faz100C_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 103, 3, 1003)
)
_Faz150G_ObjectIdentity = ObjectIdentity
faz150G = _Faz150G_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 103, 3, 1507)
)
_Faz200D_ObjectIdentity = ObjectIdentity
faz200D = _Faz200D_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 103, 3, 2004)
)
_Faz200E_ObjectIdentity = ObjectIdentity
faz200E = _Faz200E_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 103, 3, 2005)
)
_Faz200F_ObjectIdentity = ObjectIdentity
faz200F = _Faz200F_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 103, 3, 2006)
)
_Faz300D_ObjectIdentity = ObjectIdentity
faz300D = _Faz300D_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 103, 3, 3004)
)
_Faz300F_ObjectIdentity = ObjectIdentity
faz300F = _Faz300F_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 103, 3, 3006)
)
_Faz300G_ObjectIdentity = ObjectIdentity
faz300G = _Faz300G_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 103, 3, 3007)
)
_Faz400_ObjectIdentity = ObjectIdentity
faz400 = _Faz400_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 103, 3, 4000)
)
_Faz400B_ObjectIdentity = ObjectIdentity
faz400B = _Faz400B_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 103, 3, 4002)
)
_Faz400C_ObjectIdentity = ObjectIdentity
faz400C = _Faz400C_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 103, 3, 4003)
)
_Faz400E_ObjectIdentity = ObjectIdentity
faz400E = _Faz400E_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 103, 3, 4005)
)
_Faz800_ObjectIdentity = ObjectIdentity
faz800 = _Faz800_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 103, 3, 8000)
)
_Faz800B_ObjectIdentity = ObjectIdentity
faz800B = _Faz800B_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 103, 3, 8002)
)
_Faz800F_ObjectIdentity = ObjectIdentity
faz800F = _Faz800F_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 103, 3, 8006)
)
_Faz800G_ObjectIdentity = ObjectIdentity
faz800G = _Faz800G_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 103, 3, 8007)
)
_Faz810G_ObjectIdentity = ObjectIdentity
faz810G = _Faz810G_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 103, 3, 8107)
)
_Faz1000B_ObjectIdentity = ObjectIdentity
faz1000B = _Faz1000B_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 103, 3, 10002)
)
_Faz1000C_ObjectIdentity = ObjectIdentity
faz1000C = _Faz1000C_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 103, 3, 10003)
)
_Faz1000D_ObjectIdentity = ObjectIdentity
faz1000D = _Faz1000D_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 103, 3, 10004)
)
_Faz1000E_ObjectIdentity = ObjectIdentity
faz1000E = _Faz1000E_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 103, 3, 10005)
)
_Faz1000F_ObjectIdentity = ObjectIdentity
faz1000F = _Faz1000F_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 103, 3, 10006)
)
_Faz1000G_ObjectIdentity = ObjectIdentity
faz1000G = _Faz1000G_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 103, 3, 10007)
)
_Faz2000_ObjectIdentity = ObjectIdentity
faz2000 = _Faz2000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 103, 3, 20000)
)
_Faz2000A_ObjectIdentity = ObjectIdentity
faz2000A = _Faz2000A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 103, 3, 20001)
)
_Faz2000B_ObjectIdentity = ObjectIdentity
faz2000B = _Faz2000B_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 103, 3, 20002)
)
_Faz2000E_ObjectIdentity = ObjectIdentity
faz2000E = _Faz2000E_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 103, 3, 20005)
)
_Faz3000D_ObjectIdentity = ObjectIdentity
faz3000D = _Faz3000D_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 103, 3, 30004)
)
_Faz3000E_ObjectIdentity = ObjectIdentity
faz3000E = _Faz3000E_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 103, 3, 30005)
)
_Faz3000F_ObjectIdentity = ObjectIdentity
faz3000F = _Faz3000F_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 103, 3, 30006)
)
_Faz3000G_ObjectIdentity = ObjectIdentity
faz3000G = _Faz3000G_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 103, 3, 30007)
)
_Faz3100G_ObjectIdentity = ObjectIdentity
faz3100G = _Faz3100G_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 103, 3, 31007)
)
_Faz3500E_ObjectIdentity = ObjectIdentity
faz3500E = _Faz3500E_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 103, 3, 35005)
)
_Faz3500F_ObjectIdentity = ObjectIdentity
faz3500F = _Faz3500F_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 103, 3, 35006)
)
_Faz3500G_ObjectIdentity = ObjectIdentity
faz3500G = _Faz3500G_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 103, 3, 35007)
)
_Faz3510G_ObjectIdentity = ObjectIdentity
faz3510G = _Faz3510G_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 103, 3, 35107)
)
_Faz3700F_ObjectIdentity = ObjectIdentity
faz3700F = _Faz3700F_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 103, 3, 37006)
)
_Faz3700G_ObjectIdentity = ObjectIdentity
faz3700G = _Faz3700G_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 103, 3, 37007)
)
_Faz3900E_ObjectIdentity = ObjectIdentity
faz3900E = _Faz3900E_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 103, 3, 39005)
)
_Faz4000_ObjectIdentity = ObjectIdentity
faz4000 = _Faz4000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 103, 3, 40000)
)
_Faz4000A_ObjectIdentity = ObjectIdentity
faz4000A = _Faz4000A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 103, 3, 40001)
)
_Faz4000B_ObjectIdentity = ObjectIdentity
faz4000B = _Faz4000B_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 103, 3, 40002)
)
_FmInetProto_ObjectIdentity = ObjectIdentity
fmInetProto = _FmInetProto_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 103, 4)
)
_FmInetProtoInfo_ObjectIdentity = ObjectIdentity
fmInetProtoInfo = _FmInetProtoInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 103, 4, 1)
)
_FmInetProtoTables_ObjectIdentity = ObjectIdentity
fmInetProtoTables = _FmInetProtoTables_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 103, 4, 2)
)
_FmIpSessTable_Object = MibTable
fmIpSessTable = _FmIpSessTable_Object(
    (1, 3, 6, 1, 4, 1, 12356, 103, 4, 2, 1)
)
if mibBuilder.loadTexts:
    fmIpSessTable.setStatus("current")
_FmIpSessEntry_Object = MibTableRow
fmIpSessEntry = _FmIpSessEntry_Object(
    (1, 3, 6, 1, 4, 1, 12356, 103, 4, 2, 1, 1)
)
fmIpSessEntry.setIndexNames(
    (0, "FORTINET-FORTIMANAGER-FORTIANALYZER-MIB", "fmIpSessIndex"),
)
if mibBuilder.loadTexts:
    fmIpSessEntry.setStatus("current")
_FmIpSessIndex_Type = FnIndex
_FmIpSessIndex_Object = MibTableColumn
fmIpSessIndex = _FmIpSessIndex_Object(
    (1, 3, 6, 1, 4, 1, 12356, 103, 4, 2, 1, 1, 1),
    _FmIpSessIndex_Type()
)
fmIpSessIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fmIpSessIndex.setStatus("current")
_FmIpSessProto_Type = FmSessProto
_FmIpSessProto_Object = MibTableColumn
fmIpSessProto = _FmIpSessProto_Object(
    (1, 3, 6, 1, 4, 1, 12356, 103, 4, 2, 1, 1, 2),
    _FmIpSessProto_Type()
)
fmIpSessProto.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fmIpSessProto.setStatus("current")
_FmIpSessFromAddr_Type = IpAddress
_FmIpSessFromAddr_Object = MibTableColumn
fmIpSessFromAddr = _FmIpSessFromAddr_Object(
    (1, 3, 6, 1, 4, 1, 12356, 103, 4, 2, 1, 1, 3),
    _FmIpSessFromAddr_Type()
)
fmIpSessFromAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fmIpSessFromAddr.setStatus("current")
_FmIpSessFromPort_Type = InetPortNumber
_FmIpSessFromPort_Object = MibTableColumn
fmIpSessFromPort = _FmIpSessFromPort_Object(
    (1, 3, 6, 1, 4, 1, 12356, 103, 4, 2, 1, 1, 4),
    _FmIpSessFromPort_Type()
)
fmIpSessFromPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fmIpSessFromPort.setStatus("current")
_FmIpSessToAddr_Type = IpAddress
_FmIpSessToAddr_Object = MibTableColumn
fmIpSessToAddr = _FmIpSessToAddr_Object(
    (1, 3, 6, 1, 4, 1, 12356, 103, 4, 2, 1, 1, 5),
    _FmIpSessToAddr_Type()
)
fmIpSessToAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fmIpSessToAddr.setStatus("current")
_FmIpSessToPort_Type = InetPortNumber
_FmIpSessToPort_Object = MibTableColumn
fmIpSessToPort = _FmIpSessToPort_Object(
    (1, 3, 6, 1, 4, 1, 12356, 103, 4, 2, 1, 1, 6),
    _FmIpSessToPort_Type()
)
fmIpSessToPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fmIpSessToPort.setStatus("current")
_FmIpSessExp_Type = Counter32
_FmIpSessExp_Object = MibTableColumn
fmIpSessExp = _FmIpSessExp_Object(
    (1, 3, 6, 1, 4, 1, 12356, 103, 4, 2, 1, 1, 7),
    _FmIpSessExp_Type()
)
fmIpSessExp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fmIpSessExp.setStatus("current")
_FmAdom_ObjectIdentity = ObjectIdentity
fmAdom = _FmAdom_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 103, 5)
)
_FmAdomInfo_ObjectIdentity = ObjectIdentity
fmAdomInfo = _FmAdomInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 103, 5, 1)
)
_FmAdomEnabled_Type = FnBoolState
_FmAdomEnabled_Object = MibScalar
fmAdomEnabled = _FmAdomEnabled_Object(
    (1, 3, 6, 1, 4, 1, 12356, 103, 5, 1, 1),
    _FmAdomEnabled_Type()
)
fmAdomEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fmAdomEnabled.setStatus("current")
_FmAdomNumber_Type = Integer32
_FmAdomNumber_Object = MibScalar
fmAdomNumber = _FmAdomNumber_Object(
    (1, 3, 6, 1, 4, 1, 12356, 103, 5, 1, 2),
    _FmAdomNumber_Type()
)
fmAdomNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fmAdomNumber.setStatus("current")
_FmAdomMax_Type = Integer32
_FmAdomMax_Object = MibScalar
fmAdomMax = _FmAdomMax_Object(
    (1, 3, 6, 1, 4, 1, 12356, 103, 5, 1, 3),
    _FmAdomMax_Type()
)
fmAdomMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fmAdomMax.setStatus("current")
_FmAdomTable_Object = MibTable
fmAdomTable = _FmAdomTable_Object(
    (1, 3, 6, 1, 4, 1, 12356, 103, 5, 2)
)
if mibBuilder.loadTexts:
    fmAdomTable.setStatus("current")
_FmAdomEntry_Object = MibTableRow
fmAdomEntry = _FmAdomEntry_Object(
    (1, 3, 6, 1, 4, 1, 12356, 103, 5, 2, 1)
)
fmAdomEntry.setIndexNames(
    (0, "FORTINET-FORTIMANAGER-FORTIANALYZER-MIB", "fmAdomEntIndex"),
)
if mibBuilder.loadTexts:
    fmAdomEntry.setStatus("current")
_FmAdomEntIndex_Type = FnIndex
_FmAdomEntIndex_Object = MibTableColumn
fmAdomEntIndex = _FmAdomEntIndex_Object(
    (1, 3, 6, 1, 4, 1, 12356, 103, 5, 2, 1, 1),
    _FmAdomEntIndex_Type()
)
fmAdomEntIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fmAdomEntIndex.setStatus("current")
_FmAdomEntName_Type = DisplayString
_FmAdomEntName_Object = MibTableColumn
fmAdomEntName = _FmAdomEntName_Object(
    (1, 3, 6, 1, 4, 1, 12356, 103, 5, 2, 1, 2),
    _FmAdomEntName_Type()
)
fmAdomEntName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fmAdomEntName.setStatus("current")
_FmAdomEntState_Type = FnBoolState
_FmAdomEntState_Object = MibTableColumn
fmAdomEntState = _FmAdomEntState_Object(
    (1, 3, 6, 1, 4, 1, 12356, 103, 5, 2, 1, 3),
    _FmAdomEntState_Type()
)
fmAdomEntState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fmAdomEntState.setStatus("current")
_FmAdomEntMode_Type = FmAdomEntMode
_FmAdomEntMode_Object = MibTableColumn
fmAdomEntMode = _FmAdomEntMode_Object(
    (1, 3, 6, 1, 4, 1, 12356, 103, 5, 2, 1, 4),
    _FmAdomEntMode_Type()
)
fmAdomEntMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fmAdomEntMode.setStatus("current")
_FmAdomEntFgtNumber_Type = Integer32
_FmAdomEntFgtNumber_Object = MibTableColumn
fmAdomEntFgtNumber = _FmAdomEntFgtNumber_Object(
    (1, 3, 6, 1, 4, 1, 12356, 103, 5, 2, 1, 5),
    _FmAdomEntFgtNumber_Type()
)
fmAdomEntFgtNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fmAdomEntFgtNumber.setStatus("current")
_FmAdomEntPolicyPackageNumber_Type = Integer32
_FmAdomEntPolicyPackageNumber_Object = MibTableColumn
fmAdomEntPolicyPackageNumber = _FmAdomEntPolicyPackageNumber_Object(
    (1, 3, 6, 1, 4, 1, 12356, 103, 5, 2, 1, 6),
    _FmAdomEntPolicyPackageNumber_Type()
)
fmAdomEntPolicyPackageNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fmAdomEntPolicyPackageNumber.setStatus("current")
_FmAdomEntOsVersion_Type = Integer32
_FmAdomEntOsVersion_Object = MibTableColumn
fmAdomEntOsVersion = _FmAdomEntOsVersion_Object(
    (1, 3, 6, 1, 4, 1, 12356, 103, 5, 2, 1, 7),
    _FmAdomEntOsVersion_Type()
)
fmAdomEntOsVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fmAdomEntOsVersion.setStatus("current")
_FmAdomEntMr_Type = Integer32
_FmAdomEntMr_Object = MibTableColumn
fmAdomEntMr = _FmAdomEntMr_Object(
    (1, 3, 6, 1, 4, 1, 12356, 103, 5, 2, 1, 8),
    _FmAdomEntMr_Type()
)
fmAdomEntMr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fmAdomEntMr.setStatus("current")
_FmAdomEntVpnMode_Type = FmAdomEntVpnMode
_FmAdomEntVpnMode_Object = MibTableColumn
fmAdomEntVpnMode = _FmAdomEntVpnMode_Object(
    (1, 3, 6, 1, 4, 1, 12356, 103, 5, 2, 1, 9),
    _FmAdomEntVpnMode_Type()
)
fmAdomEntVpnMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fmAdomEntVpnMode.setStatus("current")
_FmAdomEntLogRateMinute_Type = FmHundredths
_FmAdomEntLogRateMinute_Object = MibTableColumn
fmAdomEntLogRateMinute = _FmAdomEntLogRateMinute_Object(
    (1, 3, 6, 1, 4, 1, 12356, 103, 5, 2, 1, 10),
    _FmAdomEntLogRateMinute_Type()
)
fmAdomEntLogRateMinute.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fmAdomEntLogRateMinute.setStatus("current")
if mibBuilder.loadTexts:
    fmAdomEntLogRateMinute.setUnits("logs per second")
_FmAdomEntArchiveLogRetention_Type = Gauge32
_FmAdomEntArchiveLogRetention_Object = MibTableColumn
fmAdomEntArchiveLogRetention = _FmAdomEntArchiveLogRetention_Object(
    (1, 3, 6, 1, 4, 1, 12356, 103, 5, 2, 1, 11),
    _FmAdomEntArchiveLogRetention_Type()
)
fmAdomEntArchiveLogRetention.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fmAdomEntArchiveLogRetention.setStatus("current")
if mibBuilder.loadTexts:
    fmAdomEntArchiveLogRetention.setUnits("days")
_FmAdomEntArchiveLogQuota_Type = Gauge32
_FmAdomEntArchiveLogQuota_Object = MibTableColumn
fmAdomEntArchiveLogQuota = _FmAdomEntArchiveLogQuota_Object(
    (1, 3, 6, 1, 4, 1, 12356, 103, 5, 2, 1, 12),
    _FmAdomEntArchiveLogQuota_Type()
)
fmAdomEntArchiveLogQuota.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fmAdomEntArchiveLogQuota.setStatus("current")
_FmAdomEntArchiveLogUsedSpace_Type = Gauge32
_FmAdomEntArchiveLogUsedSpace_Object = MibTableColumn
fmAdomEntArchiveLogUsedSpace = _FmAdomEntArchiveLogUsedSpace_Object(
    (1, 3, 6, 1, 4, 1, 12356, 103, 5, 2, 1, 13),
    _FmAdomEntArchiveLogUsedSpace_Type()
)
fmAdomEntArchiveLogUsedSpace.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fmAdomEntArchiveLogUsedSpace.setStatus("current")
_FmAdomEntArchiveLogUsedSpacePercent_Type = FmTenths
_FmAdomEntArchiveLogUsedSpacePercent_Object = MibTableColumn
fmAdomEntArchiveLogUsedSpacePercent = _FmAdomEntArchiveLogUsedSpacePercent_Object(
    (1, 3, 6, 1, 4, 1, 12356, 103, 5, 2, 1, 14),
    _FmAdomEntArchiveLogUsedSpacePercent_Type()
)
fmAdomEntArchiveLogUsedSpacePercent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fmAdomEntArchiveLogUsedSpacePercent.setStatus("current")
_FmAdomEntAnalyticsLogRetention_Type = Gauge32
_FmAdomEntAnalyticsLogRetention_Object = MibTableColumn
fmAdomEntAnalyticsLogRetention = _FmAdomEntAnalyticsLogRetention_Object(
    (1, 3, 6, 1, 4, 1, 12356, 103, 5, 2, 1, 15),
    _FmAdomEntAnalyticsLogRetention_Type()
)
fmAdomEntAnalyticsLogRetention.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fmAdomEntAnalyticsLogRetention.setStatus("current")
if mibBuilder.loadTexts:
    fmAdomEntAnalyticsLogRetention.setUnits("days")
_FmAdomEntAnalyticsLogQuota_Type = Gauge32
_FmAdomEntAnalyticsLogQuota_Object = MibTableColumn
fmAdomEntAnalyticsLogQuota = _FmAdomEntAnalyticsLogQuota_Object(
    (1, 3, 6, 1, 4, 1, 12356, 103, 5, 2, 1, 16),
    _FmAdomEntAnalyticsLogQuota_Type()
)
fmAdomEntAnalyticsLogQuota.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fmAdomEntAnalyticsLogQuota.setStatus("current")
_FmAdomEntAnalyticsLogUsedSpace_Type = Gauge32
_FmAdomEntAnalyticsLogUsedSpace_Object = MibTableColumn
fmAdomEntAnalyticsLogUsedSpace = _FmAdomEntAnalyticsLogUsedSpace_Object(
    (1, 3, 6, 1, 4, 1, 12356, 103, 5, 2, 1, 17),
    _FmAdomEntAnalyticsLogUsedSpace_Type()
)
fmAdomEntAnalyticsLogUsedSpace.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fmAdomEntAnalyticsLogUsedSpace.setStatus("current")
_FmAdomEntAnalyticsLogUsedSpacePercent_Type = FmTenths
_FmAdomEntAnalyticsLogUsedSpacePercent_Object = MibTableColumn
fmAdomEntAnalyticsLogUsedSpacePercent = _FmAdomEntAnalyticsLogUsedSpacePercent_Object(
    (1, 3, 6, 1, 4, 1, 12356, 103, 5, 2, 1, 18),
    _FmAdomEntAnalyticsLogUsedSpacePercent_Type()
)
fmAdomEntAnalyticsLogUsedSpacePercent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fmAdomEntAnalyticsLogUsedSpacePercent.setStatus("current")
_FmAdomEntLicGbDayToday_Type = FmHundredths
_FmAdomEntLicGbDayToday_Object = MibTableColumn
fmAdomEntLicGbDayToday = _FmAdomEntLicGbDayToday_Object(
    (1, 3, 6, 1, 4, 1, 12356, 103, 5, 2, 1, 19),
    _FmAdomEntLicGbDayToday_Type()
)
fmAdomEntLicGbDayToday.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fmAdomEntLicGbDayToday.setStatus("current")
_FmAdomEntLicGbDayYesterday_Type = FmHundredths
_FmAdomEntLicGbDayYesterday_Object = MibTableColumn
fmAdomEntLicGbDayYesterday = _FmAdomEntLicGbDayYesterday_Object(
    (1, 3, 6, 1, 4, 1, 12356, 103, 5, 2, 1, 20),
    _FmAdomEntLicGbDayYesterday_Type()
)
fmAdomEntLicGbDayYesterday.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fmAdomEntLicGbDayYesterday.setStatus("current")
_FmAdomEntLicGbDayWeekAvg_Type = FmHundredths
_FmAdomEntLicGbDayWeekAvg_Object = MibTableColumn
fmAdomEntLicGbDayWeekAvg = _FmAdomEntLicGbDayWeekAvg_Object(
    (1, 3, 6, 1, 4, 1, 12356, 103, 5, 2, 1, 21),
    _FmAdomEntLicGbDayWeekAvg_Type()
)
fmAdomEntLicGbDayWeekAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fmAdomEntLicGbDayWeekAvg.setStatus("current")
_FmDevice_ObjectIdentity = ObjectIdentity
fmDevice = _FmDevice_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 103, 6)
)
_FmDeviceInfo_ObjectIdentity = ObjectIdentity
fmDeviceInfo = _FmDeviceInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 103, 6, 1)
)
_FmDeviceNumber_Type = Integer32
_FmDeviceNumber_Object = MibScalar
fmDeviceNumber = _FmDeviceNumber_Object(
    (1, 3, 6, 1, 4, 1, 12356, 103, 6, 1, 1),
    _FmDeviceNumber_Type()
)
fmDeviceNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fmDeviceNumber.setStatus("current")
_FmVdomNumber_Type = Integer32
_FmVdomNumber_Object = MibScalar
fmVdomNumber = _FmVdomNumber_Object(
    (1, 3, 6, 1, 4, 1, 12356, 103, 6, 1, 2),
    _FmVdomNumber_Type()
)
fmVdomNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fmVdomNumber.setStatus("current")
_FmDeviceTable_Object = MibTable
fmDeviceTable = _FmDeviceTable_Object(
    (1, 3, 6, 1, 4, 1, 12356, 103, 6, 2)
)
if mibBuilder.loadTexts:
    fmDeviceTable.setStatus("current")
_FmDeviceEntry_Object = MibTableRow
fmDeviceEntry = _FmDeviceEntry_Object(
    (1, 3, 6, 1, 4, 1, 12356, 103, 6, 2, 1)
)
fmDeviceEntry.setIndexNames(
    (0, "FORTINET-FORTIMANAGER-FORTIANALYZER-MIB", "fmDeviceEntIndex"),
)
if mibBuilder.loadTexts:
    fmDeviceEntry.setStatus("current")
_FmDeviceEntIndex_Type = FnIndex
_FmDeviceEntIndex_Object = MibTableColumn
fmDeviceEntIndex = _FmDeviceEntIndex_Object(
    (1, 3, 6, 1, 4, 1, 12356, 103, 6, 2, 1, 1),
    _FmDeviceEntIndex_Type()
)
fmDeviceEntIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fmDeviceEntIndex.setStatus("current")
_FmDeviceEntName_Type = DisplayString
_FmDeviceEntName_Object = MibTableColumn
fmDeviceEntName = _FmDeviceEntName_Object(
    (1, 3, 6, 1, 4, 1, 12356, 103, 6, 2, 1, 2),
    _FmDeviceEntName_Type()
)
fmDeviceEntName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fmDeviceEntName.setStatus("current")
_FmDeviceEntSn_Type = DisplayString
_FmDeviceEntSn_Object = MibTableColumn
fmDeviceEntSn = _FmDeviceEntSn_Object(
    (1, 3, 6, 1, 4, 1, 12356, 103, 6, 2, 1, 3),
    _FmDeviceEntSn_Type()
)
fmDeviceEntSn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fmDeviceEntSn.setStatus("current")
_FmDeviceEntMode_Type = FmDeviceEntMode
_FmDeviceEntMode_Object = MibTableColumn
fmDeviceEntMode = _FmDeviceEntMode_Object(
    (1, 3, 6, 1, 4, 1, 12356, 103, 6, 2, 1, 4),
    _FmDeviceEntMode_Type()
)
fmDeviceEntMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fmDeviceEntMode.setStatus("current")
_FmDeviceEntAdom_Type = DisplayString
_FmDeviceEntAdom_Object = MibTableColumn
fmDeviceEntAdom = _FmDeviceEntAdom_Object(
    (1, 3, 6, 1, 4, 1, 12356, 103, 6, 2, 1, 5),
    _FmDeviceEntAdom_Type()
)
fmDeviceEntAdom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fmDeviceEntAdom.setStatus("current")
_FmDeviceEntIp_Type = DisplayString
_FmDeviceEntIp_Object = MibTableColumn
fmDeviceEntIp = _FmDeviceEntIp_Object(
    (1, 3, 6, 1, 4, 1, 12356, 103, 6, 2, 1, 6),
    _FmDeviceEntIp_Type()
)
fmDeviceEntIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fmDeviceEntIp.setStatus("current")
_FmDeviceEntOsVersion_Type = Integer32
_FmDeviceEntOsVersion_Object = MibTableColumn
fmDeviceEntOsVersion = _FmDeviceEntOsVersion_Object(
    (1, 3, 6, 1, 4, 1, 12356, 103, 6, 2, 1, 7),
    _FmDeviceEntOsVersion_Type()
)
fmDeviceEntOsVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fmDeviceEntOsVersion.setStatus("current")
_FmDeviceEntMr_Type = Integer32
_FmDeviceEntMr_Object = MibTableColumn
fmDeviceEntMr = _FmDeviceEntMr_Object(
    (1, 3, 6, 1, 4, 1, 12356, 103, 6, 2, 1, 8),
    _FmDeviceEntMr_Type()
)
fmDeviceEntMr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fmDeviceEntMr.setStatus("current")
_FmDeviceEntBuild_Type = Integer32
_FmDeviceEntBuild_Object = MibTableColumn
fmDeviceEntBuild = _FmDeviceEntBuild_Object(
    (1, 3, 6, 1, 4, 1, 12356, 103, 6, 2, 1, 9),
    _FmDeviceEntBuild_Type()
)
fmDeviceEntBuild.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fmDeviceEntBuild.setStatus("current")
_FmDeviceEntHaMode_Type = FmDeviceEntHaMode
_FmDeviceEntHaMode_Object = MibTableColumn
fmDeviceEntHaMode = _FmDeviceEntHaMode_Object(
    (1, 3, 6, 1, 4, 1, 12356, 103, 6, 2, 1, 10),
    _FmDeviceEntHaMode_Type()
)
fmDeviceEntHaMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fmDeviceEntHaMode.setStatus("current")
_FmDeviceEntHaGroup_Type = DisplayString
_FmDeviceEntHaGroup_Object = MibTableColumn
fmDeviceEntHaGroup = _FmDeviceEntHaGroup_Object(
    (1, 3, 6, 1, 4, 1, 12356, 103, 6, 2, 1, 11),
    _FmDeviceEntHaGroup_Type()
)
fmDeviceEntHaGroup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fmDeviceEntHaGroup.setStatus("current")
_FmDeviceEntConnectState_Type = FmDeviceEntConnectState
_FmDeviceEntConnectState_Object = MibTableColumn
fmDeviceEntConnectState = _FmDeviceEntConnectState_Object(
    (1, 3, 6, 1, 4, 1, 12356, 103, 6, 2, 1, 12),
    _FmDeviceEntConnectState_Type()
)
fmDeviceEntConnectState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fmDeviceEntConnectState.setStatus("current")
_FmDeviceEntDbState_Type = FmDeviceEntDbState
_FmDeviceEntDbState_Object = MibTableColumn
fmDeviceEntDbState = _FmDeviceEntDbState_Object(
    (1, 3, 6, 1, 4, 1, 12356, 103, 6, 2, 1, 13),
    _FmDeviceEntDbState_Type()
)
fmDeviceEntDbState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fmDeviceEntDbState.setStatus("current")
_FmDeviceEntConfigState_Type = FmDeviceEntConfigState
_FmDeviceEntConfigState_Object = MibTableColumn
fmDeviceEntConfigState = _FmDeviceEntConfigState_Object(
    (1, 3, 6, 1, 4, 1, 12356, 103, 6, 2, 1, 14),
    _FmDeviceEntConfigState_Type()
)
fmDeviceEntConfigState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fmDeviceEntConfigState.setStatus("current")
_FmDeviceEntState_Type = FmDeviceEntState
_FmDeviceEntState_Object = MibTableColumn
fmDeviceEntState = _FmDeviceEntState_Object(
    (1, 3, 6, 1, 4, 1, 12356, 103, 6, 2, 1, 15),
    _FmDeviceEntState_Type()
)
fmDeviceEntState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fmDeviceEntState.setStatus("current")
_FmDeviceEntPlatform_Type = DisplayString
_FmDeviceEntPlatform_Object = MibTableColumn
fmDeviceEntPlatform = _FmDeviceEntPlatform_Object(
    (1, 3, 6, 1, 4, 1, 12356, 103, 6, 2, 1, 16),
    _FmDeviceEntPlatform_Type()
)
fmDeviceEntPlatform.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fmDeviceEntPlatform.setStatus("current")
_FmDeviceEntVdomEnabled_Type = FnBoolState
_FmDeviceEntVdomEnabled_Object = MibTableColumn
fmDeviceEntVdomEnabled = _FmDeviceEntVdomEnabled_Object(
    (1, 3, 6, 1, 4, 1, 12356, 103, 6, 2, 1, 17),
    _FmDeviceEntVdomEnabled_Type()
)
fmDeviceEntVdomEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fmDeviceEntVdomEnabled.setStatus("current")
_FmDeviceEntSupportState_Type = FmDeviceEntSupportState
_FmDeviceEntSupportState_Object = MibTableColumn
fmDeviceEntSupportState = _FmDeviceEntSupportState_Object(
    (1, 3, 6, 1, 4, 1, 12356, 103, 6, 2, 1, 18),
    _FmDeviceEntSupportState_Type()
)
fmDeviceEntSupportState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fmDeviceEntSupportState.setStatus("current")
_FmDeviceEntAvExpireDate_Type = DisplayString
_FmDeviceEntAvExpireDate_Object = MibTableColumn
fmDeviceEntAvExpireDate = _FmDeviceEntAvExpireDate_Object(
    (1, 3, 6, 1, 4, 1, 12356, 103, 6, 2, 1, 19),
    _FmDeviceEntAvExpireDate_Type()
)
fmDeviceEntAvExpireDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fmDeviceEntAvExpireDate.setStatus("current")
_FmDeviceEntIpsExpireDate_Type = DisplayString
_FmDeviceEntIpsExpireDate_Object = MibTableColumn
fmDeviceEntIpsExpireDate = _FmDeviceEntIpsExpireDate_Object(
    (1, 3, 6, 1, 4, 1, 12356, 103, 6, 2, 1, 20),
    _FmDeviceEntIpsExpireDate_Type()
)
fmDeviceEntIpsExpireDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fmDeviceEntIpsExpireDate.setStatus("current")
_FmDeviceEntWfExpireDate_Type = DisplayString
_FmDeviceEntWfExpireDate_Object = MibTableColumn
fmDeviceEntWfExpireDate = _FmDeviceEntWfExpireDate_Object(
    (1, 3, 6, 1, 4, 1, 12356, 103, 6, 2, 1, 21),
    _FmDeviceEntWfExpireDate_Type()
)
fmDeviceEntWfExpireDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fmDeviceEntWfExpireDate.setStatus("current")
_FmDeviceEntAsExpireDate_Type = DisplayString
_FmDeviceEntAsExpireDate_Object = MibTableColumn
fmDeviceEntAsExpireDate = _FmDeviceEntAsExpireDate_Object(
    (1, 3, 6, 1, 4, 1, 12356, 103, 6, 2, 1, 22),
    _FmDeviceEntAsExpireDate_Type()
)
fmDeviceEntAsExpireDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fmDeviceEntAsExpireDate.setStatus("current")
_FmDeviceEntPolicyPackageState_Type = DisplayString
_FmDeviceEntPolicyPackageState_Object = MibTableColumn
fmDeviceEntPolicyPackageState = _FmDeviceEntPolicyPackageState_Object(
    (1, 3, 6, 1, 4, 1, 12356, 103, 6, 2, 1, 23),
    _FmDeviceEntPolicyPackageState_Type()
)
fmDeviceEntPolicyPackageState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fmDeviceEntPolicyPackageState.setStatus("current")
_FmDeviceEntDesc_Type = DisplayString
_FmDeviceEntDesc_Object = MibTableColumn
fmDeviceEntDesc = _FmDeviceEntDesc_Object(
    (1, 3, 6, 1, 4, 1, 12356, 103, 6, 2, 1, 24),
    _FmDeviceEntDesc_Type()
)
fmDeviceEntDesc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fmDeviceEntDesc.setStatus("current")
_FmDeviceEntLogRateHour_Type = FmHundredths
_FmDeviceEntLogRateHour_Object = MibTableColumn
fmDeviceEntLogRateHour = _FmDeviceEntLogRateHour_Object(
    (1, 3, 6, 1, 4, 1, 12356, 103, 6, 2, 1, 25),
    _FmDeviceEntLogRateHour_Type()
)
fmDeviceEntLogRateHour.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fmDeviceEntLogRateHour.setStatus("current")
if mibBuilder.loadTexts:
    fmDeviceEntLogRateHour.setUnits("logs per second")
_FmDeviceEntLogRateDay_Type = FmHundredths
_FmDeviceEntLogRateDay_Object = MibTableColumn
fmDeviceEntLogRateDay = _FmDeviceEntLogRateDay_Object(
    (1, 3, 6, 1, 4, 1, 12356, 103, 6, 2, 1, 26),
    _FmDeviceEntLogRateDay_Type()
)
fmDeviceEntLogRateDay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fmDeviceEntLogRateDay.setStatus("current")
if mibBuilder.loadTexts:
    fmDeviceEntLogRateDay.setUnits("logs per second")
_FmDeviceEntLogRateWeek_Type = FmHundredths
_FmDeviceEntLogRateWeek_Object = MibTableColumn
fmDeviceEntLogRateWeek = _FmDeviceEntLogRateWeek_Object(
    (1, 3, 6, 1, 4, 1, 12356, 103, 6, 2, 1, 27),
    _FmDeviceEntLogRateWeek_Type()
)
fmDeviceEntLogRateWeek.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fmDeviceEntLogRateWeek.setStatus("current")
if mibBuilder.loadTexts:
    fmDeviceEntLogRateWeek.setUnits("logs per second")
_FmDeviceEntArchiveLogUsedSpace_Type = Gauge32
_FmDeviceEntArchiveLogUsedSpace_Object = MibTableColumn
fmDeviceEntArchiveLogUsedSpace = _FmDeviceEntArchiveLogUsedSpace_Object(
    (1, 3, 6, 1, 4, 1, 12356, 103, 6, 2, 1, 28),
    _FmDeviceEntArchiveLogUsedSpace_Type()
)
fmDeviceEntArchiveLogUsedSpace.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fmDeviceEntArchiveLogUsedSpace.setStatus("current")
_FmRaid_ObjectIdentity = ObjectIdentity
fmRaid = _FmRaid_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 103, 7)
)
_FmRaidInfo_ObjectIdentity = ObjectIdentity
fmRaidInfo = _FmRaidInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 103, 7, 1)
)
_FmRaidLevel_Type = FmRaidLevel
_FmRaidLevel_Object = MibScalar
fmRaidLevel = _FmRaidLevel_Object(
    (1, 3, 6, 1, 4, 1, 12356, 103, 7, 1, 1),
    _FmRaidLevel_Type()
)
fmRaidLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fmRaidLevel.setStatus("current")
_FmRaidState_Type = FmRaidState
_FmRaidState_Object = MibScalar
fmRaidState = _FmRaidState_Object(
    (1, 3, 6, 1, 4, 1, 12356, 103, 7, 1, 2),
    _FmRaidState_Type()
)
fmRaidState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fmRaidState.setStatus("current")
_FmRaidSize_Type = Integer32
_FmRaidSize_Object = MibScalar
fmRaidSize = _FmRaidSize_Object(
    (1, 3, 6, 1, 4, 1, 12356, 103, 7, 1, 3),
    _FmRaidSize_Type()
)
fmRaidSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fmRaidSize.setStatus("current")
if mibBuilder.loadTexts:
    fmRaidSize.setUnits("GB")
_FmRaidDiskNumber_Type = Integer32
_FmRaidDiskNumber_Object = MibScalar
fmRaidDiskNumber = _FmRaidDiskNumber_Object(
    (1, 3, 6, 1, 4, 1, 12356, 103, 7, 1, 4),
    _FmRaidDiskNumber_Type()
)
fmRaidDiskNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fmRaidDiskNumber.setStatus("current")
_FmRaidDiskTable_Object = MibTable
fmRaidDiskTable = _FmRaidDiskTable_Object(
    (1, 3, 6, 1, 4, 1, 12356, 103, 7, 2)
)
if mibBuilder.loadTexts:
    fmRaidDiskTable.setStatus("current")
_FmRaidDiskEntry_Object = MibTableRow
fmRaidDiskEntry = _FmRaidDiskEntry_Object(
    (1, 3, 6, 1, 4, 1, 12356, 103, 7, 2, 1)
)
fmRaidDiskEntry.setIndexNames(
    (0, "FORTINET-FORTIMANAGER-FORTIANALYZER-MIB", "fmRaidDiskEntIndex"),
)
if mibBuilder.loadTexts:
    fmRaidDiskEntry.setStatus("current")
_FmRaidDiskEntIndex_Type = FnIndex
_FmRaidDiskEntIndex_Object = MibTableColumn
fmRaidDiskEntIndex = _FmRaidDiskEntIndex_Object(
    (1, 3, 6, 1, 4, 1, 12356, 103, 7, 2, 1, 1),
    _FmRaidDiskEntIndex_Type()
)
fmRaidDiskEntIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fmRaidDiskEntIndex.setStatus("current")
_FmRaidDiskEntState_Type = FmRaidDiskEntState
_FmRaidDiskEntState_Object = MibTableColumn
fmRaidDiskEntState = _FmRaidDiskEntState_Object(
    (1, 3, 6, 1, 4, 1, 12356, 103, 7, 2, 1, 2),
    _FmRaidDiskEntState_Type()
)
fmRaidDiskEntState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fmRaidDiskEntState.setStatus("current")
_FmRaidDiskEntSize_Type = Integer32
_FmRaidDiskEntSize_Object = MibTableColumn
fmRaidDiskEntSize = _FmRaidDiskEntSize_Object(
    (1, 3, 6, 1, 4, 1, 12356, 103, 7, 2, 1, 3),
    _FmRaidDiskEntSize_Type()
)
fmRaidDiskEntSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fmRaidDiskEntSize.setStatus("current")
if mibBuilder.loadTexts:
    fmRaidDiskEntSize.setUnits("GB")
_FmSensor_ObjectIdentity = ObjectIdentity
fmSensor = _FmSensor_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 103, 8)
)
_FmSensorTable_Object = MibTable
fmSensorTable = _FmSensorTable_Object(
    (1, 3, 6, 1, 4, 1, 12356, 103, 8, 2)
)
if mibBuilder.loadTexts:
    fmSensorTable.setStatus("current")
_FmSensorEntry_Object = MibTableRow
fmSensorEntry = _FmSensorEntry_Object(
    (1, 3, 6, 1, 4, 1, 12356, 103, 8, 2, 1)
)
fmSensorEntry.setIndexNames(
    (0, "FORTINET-FORTIMANAGER-FORTIANALYZER-MIB", "fmSensorEntIndex"),
)
if mibBuilder.loadTexts:
    fmSensorEntry.setStatus("current")
_FmSensorEntIndex_Type = FnIndex
_FmSensorEntIndex_Object = MibTableColumn
fmSensorEntIndex = _FmSensorEntIndex_Object(
    (1, 3, 6, 1, 4, 1, 12356, 103, 8, 2, 1, 1),
    _FmSensorEntIndex_Type()
)
fmSensorEntIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fmSensorEntIndex.setStatus("current")
_FmSensorEntName_Type = DisplayString
_FmSensorEntName_Object = MibTableColumn
fmSensorEntName = _FmSensorEntName_Object(
    (1, 3, 6, 1, 4, 1, 12356, 103, 8, 2, 1, 2),
    _FmSensorEntName_Type()
)
fmSensorEntName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fmSensorEntName.setStatus("current")
_FmSensorEntVal_Type = DisplayString
_FmSensorEntVal_Object = MibTableColumn
fmSensorEntVal = _FmSensorEntVal_Object(
    (1, 3, 6, 1, 4, 1, 12356, 103, 8, 2, 1, 3),
    _FmSensorEntVal_Type()
)
fmSensorEntVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fmSensorEntVal.setStatus("current")
_FmSensorEntType_Type = FmSensorEntType
_FmSensorEntType_Object = MibTableColumn
fmSensorEntType = _FmSensorEntType_Object(
    (1, 3, 6, 1, 4, 1, 12356, 103, 8, 2, 1, 4),
    _FmSensorEntType_Type()
)
fmSensorEntType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fmSensorEntType.setStatus("current")
_FmSensorEntState_Type = FmSensorEntState
_FmSensorEntState_Object = MibTableColumn
fmSensorEntState = _FmSensorEntState_Object(
    (1, 3, 6, 1, 4, 1, 12356, 103, 8, 2, 1, 5),
    _FmSensorEntState_Type()
)
fmSensorEntState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fmSensorEntState.setStatus("current")
_FmHa_ObjectIdentity = ObjectIdentity
fmHa = _FmHa_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 103, 9)
)
_FmHaInfo_ObjectIdentity = ObjectIdentity
fmHaInfo = _FmHaInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 103, 9, 1)
)
_FmHaMode_Type = FmHaMode
_FmHaMode_Object = MibScalar
fmHaMode = _FmHaMode_Object(
    (1, 3, 6, 1, 4, 1, 12356, 103, 9, 1, 1),
    _FmHaMode_Type()
)
fmHaMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fmHaMode.setStatus("current")
_FmHaClusterId_Type = Integer32
_FmHaClusterId_Object = MibScalar
fmHaClusterId = _FmHaClusterId_Object(
    (1, 3, 6, 1, 4, 1, 12356, 103, 9, 1, 2),
    _FmHaClusterId_Type()
)
fmHaClusterId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fmHaClusterId.setStatus("current")
_FmHaPeerNumber_Type = Integer32
_FmHaPeerNumber_Object = MibScalar
fmHaPeerNumber = _FmHaPeerNumber_Object(
    (1, 3, 6, 1, 4, 1, 12356, 103, 9, 1, 3),
    _FmHaPeerNumber_Type()
)
fmHaPeerNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fmHaPeerNumber.setStatus("current")
_FmHaPeerTable_Object = MibTable
fmHaPeerTable = _FmHaPeerTable_Object(
    (1, 3, 6, 1, 4, 1, 12356, 103, 9, 2)
)
if mibBuilder.loadTexts:
    fmHaPeerTable.setStatus("current")
_FmHaPeerEntry_Object = MibTableRow
fmHaPeerEntry = _FmHaPeerEntry_Object(
    (1, 3, 6, 1, 4, 1, 12356, 103, 9, 2, 1)
)
fmHaPeerEntry.setIndexNames(
    (0, "FORTINET-FORTIMANAGER-FORTIANALYZER-MIB", "fmHaPeerEntIndex"),
)
if mibBuilder.loadTexts:
    fmHaPeerEntry.setStatus("current")
_FmHaPeerEntIndex_Type = FnIndex
_FmHaPeerEntIndex_Object = MibTableColumn
fmHaPeerEntIndex = _FmHaPeerEntIndex_Object(
    (1, 3, 6, 1, 4, 1, 12356, 103, 9, 2, 1, 1),
    _FmHaPeerEntIndex_Type()
)
fmHaPeerEntIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fmHaPeerEntIndex.setStatus("current")
_FmHaPeerEntIp_Type = DisplayString
_FmHaPeerEntIp_Object = MibTableColumn
fmHaPeerEntIp = _FmHaPeerEntIp_Object(
    (1, 3, 6, 1, 4, 1, 12356, 103, 9, 2, 1, 2),
    _FmHaPeerEntIp_Type()
)
fmHaPeerEntIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fmHaPeerEntIp.setStatus("current")
_FmHaPeerEntSn_Type = DisplayString
_FmHaPeerEntSn_Object = MibTableColumn
fmHaPeerEntSn = _FmHaPeerEntSn_Object(
    (1, 3, 6, 1, 4, 1, 12356, 103, 9, 2, 1, 3),
    _FmHaPeerEntSn_Type()
)
fmHaPeerEntSn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fmHaPeerEntSn.setStatus("current")
_FmHaPeerEntEnabled_Type = FnBoolState
_FmHaPeerEntEnabled_Object = MibTableColumn
fmHaPeerEntEnabled = _FmHaPeerEntEnabled_Object(
    (1, 3, 6, 1, 4, 1, 12356, 103, 9, 2, 1, 4),
    _FmHaPeerEntEnabled_Type()
)
fmHaPeerEntEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fmHaPeerEntEnabled.setStatus("current")
_FmHaPeerEntHostName_Type = DisplayString
_FmHaPeerEntHostName_Object = MibTableColumn
fmHaPeerEntHostName = _FmHaPeerEntHostName_Object(
    (1, 3, 6, 1, 4, 1, 12356, 103, 9, 2, 1, 5),
    _FmHaPeerEntHostName_Type()
)
fmHaPeerEntHostName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fmHaPeerEntHostName.setStatus("current")
_FmHaPeerEntState_Type = FmHaPeerEntState
_FmHaPeerEntState_Object = MibTableColumn
fmHaPeerEntState = _FmHaPeerEntState_Object(
    (1, 3, 6, 1, 4, 1, 12356, 103, 9, 2, 1, 6),
    _FmHaPeerEntState_Type()
)
fmHaPeerEntState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fmHaPeerEntState.setStatus("current")
_FmMIBConformance_ObjectIdentity = ObjectIdentity
fmMIBConformance = _FmMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 103, 10)
)
_FmUm_ObjectIdentity = ObjectIdentity
fmUm = _FmUm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 103, 11)
)
_FmUmContract_ObjectIdentity = ObjectIdentity
fmUmContract = _FmUmContract_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 103, 11, 1)
)
_FmUmContractTable_Object = MibTable
fmUmContractTable = _FmUmContractTable_Object(
    (1, 3, 6, 1, 4, 1, 12356, 103, 11, 1, 1)
)
if mibBuilder.loadTexts:
    fmUmContractTable.setStatus("current")
_FmUmContractEntry_Object = MibTableRow
fmUmContractEntry = _FmUmContractEntry_Object(
    (1, 3, 6, 1, 4, 1, 12356, 103, 11, 1, 1, 1)
)
fmUmContractEntry.setIndexNames(
    (0, "FORTINET-FORTIMANAGER-FORTIANALYZER-MIB", "fmUmContractEntryIndex"),
)
if mibBuilder.loadTexts:
    fmUmContractEntry.setStatus("current")
_FmUmContractEntryIndex_Type = FnIndex
_FmUmContractEntryIndex_Object = MibTableColumn
fmUmContractEntryIndex = _FmUmContractEntryIndex_Object(
    (1, 3, 6, 1, 4, 1, 12356, 103, 11, 1, 1, 1, 1),
    _FmUmContractEntryIndex_Type()
)
fmUmContractEntryIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fmUmContractEntryIndex.setStatus("current")


class _FmUmContractEntrySerial_Type(DisplayString):
    """Custom type fmUmContractEntrySerial based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )
    fixed_length = 16


_FmUmContractEntrySerial_Type.__name__ = "DisplayString"
_FmUmContractEntrySerial_Object = MibTableColumn
fmUmContractEntrySerial = _FmUmContractEntrySerial_Object(
    (1, 3, 6, 1, 4, 1, 12356, 103, 11, 1, 1, 1, 2),
    _FmUmContractEntrySerial_Type()
)
fmUmContractEntrySerial.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fmUmContractEntrySerial.setStatus("current")


class _FmUmContractEntryData_Type(DisplayString):
    """Custom type fmUmContractEntryData based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 512),
    )


_FmUmContractEntryData_Type.__name__ = "DisplayString"
_FmUmContractEntryData_Object = MibTableColumn
fmUmContractEntryData = _FmUmContractEntryData_Object(
    (1, 3, 6, 1, 4, 1, 12356, 103, 11, 1, 1, 1, 3),
    _FmUmContractEntryData_Type()
)
fmUmContractEntryData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fmUmContractEntryData.setStatus("current")
_FmUmFds_ObjectIdentity = ObjectIdentity
fmUmFds = _FmUmFds_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 103, 11, 2)
)
_FmUmFdsServiceFds_ObjectIdentity = ObjectIdentity
fmUmFdsServiceFds = _FmUmFdsServiceFds_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 103, 11, 2, 1)
)
_FmUmFdsServiceFdsStatus_Type = FmUmServiceStatus
_FmUmFdsServiceFdsStatus_Object = MibScalar
fmUmFdsServiceFdsStatus = _FmUmFdsServiceFdsStatus_Object(
    (1, 3, 6, 1, 4, 1, 12356, 103, 11, 2, 1, 1),
    _FmUmFdsServiceFdsStatus_Type()
)
fmUmFdsServiceFdsStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fmUmFdsServiceFdsStatus.setStatus("current")
_FmUmFdsServiceFdsServerTable_Object = MibTable
fmUmFdsServiceFdsServerTable = _FmUmFdsServiceFdsServerTable_Object(
    (1, 3, 6, 1, 4, 1, 12356, 103, 11, 2, 1, 2)
)
if mibBuilder.loadTexts:
    fmUmFdsServiceFdsServerTable.setStatus("current")
_FmUmFdsServiceFdsServerEntry_Object = MibTableRow
fmUmFdsServiceFdsServerEntry = _FmUmFdsServiceFdsServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 12356, 103, 11, 2, 1, 2, 1)
)
fmUmFdsServiceFdsServerEntry.setIndexNames(
    (0, "FORTINET-FORTIMANAGER-FORTIANALYZER-MIB", "fmUmFdsServiceFdsServerEntryIndex"),
)
if mibBuilder.loadTexts:
    fmUmFdsServiceFdsServerEntry.setStatus("current")
_FmUmFdsServiceFdsServerEntryIndex_Type = FnIndex
_FmUmFdsServiceFdsServerEntryIndex_Object = MibTableColumn
fmUmFdsServiceFdsServerEntryIndex = _FmUmFdsServiceFdsServerEntryIndex_Object(
    (1, 3, 6, 1, 4, 1, 12356, 103, 11, 2, 1, 2, 1, 1),
    _FmUmFdsServiceFdsServerEntryIndex_Type()
)
fmUmFdsServiceFdsServerEntryIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fmUmFdsServiceFdsServerEntryIndex.setStatus("current")
_FmUmFdsServiceFdsServerAddr_Type = InetAddress
_FmUmFdsServiceFdsServerAddr_Object = MibTableColumn
fmUmFdsServiceFdsServerAddr = _FmUmFdsServiceFdsServerAddr_Object(
    (1, 3, 6, 1, 4, 1, 12356, 103, 11, 2, 1, 2, 1, 2),
    _FmUmFdsServiceFdsServerAddr_Type()
)
fmUmFdsServiceFdsServerAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fmUmFdsServiceFdsServerAddr.setStatus("current")
_FmUmFdsServiceFdsServerPort_Type = InetPortNumber
_FmUmFdsServiceFdsServerPort_Object = MibTableColumn
fmUmFdsServiceFdsServerPort = _FmUmFdsServiceFdsServerPort_Object(
    (1, 3, 6, 1, 4, 1, 12356, 103, 11, 2, 1, 2, 1, 3),
    _FmUmFdsServiceFdsServerPort_Type()
)
fmUmFdsServiceFdsServerPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fmUmFdsServiceFdsServerPort.setStatus("current")
_FmUmFdsServiceFdsServerTimeZone_Type = Integer32
_FmUmFdsServiceFdsServerTimeZone_Object = MibTableColumn
fmUmFdsServiceFdsServerTimeZone = _FmUmFdsServiceFdsServerTimeZone_Object(
    (1, 3, 6, 1, 4, 1, 12356, 103, 11, 2, 1, 2, 1, 4),
    _FmUmFdsServiceFdsServerTimeZone_Type()
)
fmUmFdsServiceFdsServerTimeZone.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fmUmFdsServiceFdsServerTimeZone.setStatus("current")
_FmUmFdsServiceFdsServerCurrent_Type = FmUmBoolState
_FmUmFdsServiceFdsServerCurrent_Object = MibTableColumn
fmUmFdsServiceFdsServerCurrent = _FmUmFdsServiceFdsServerCurrent_Object(
    (1, 3, 6, 1, 4, 1, 12356, 103, 11, 2, 1, 2, 1, 5),
    _FmUmFdsServiceFdsServerCurrent_Type()
)
fmUmFdsServiceFdsServerCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fmUmFdsServiceFdsServerCurrent.setStatus("current")
_FmUmFdsServiceFct_ObjectIdentity = ObjectIdentity
fmUmFdsServiceFct = _FmUmFdsServiceFct_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 103, 11, 2, 2)
)
_FmUmFdsServiceFctStatus_Type = FmUmServiceStatus
_FmUmFdsServiceFctStatus_Object = MibScalar
fmUmFdsServiceFctStatus = _FmUmFdsServiceFctStatus_Object(
    (1, 3, 6, 1, 4, 1, 12356, 103, 11, 2, 2, 1),
    _FmUmFdsServiceFctStatus_Type()
)
fmUmFdsServiceFctStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fmUmFdsServiceFctStatus.setStatus("current")
_FmUmFdsServiceFctServerTable_Object = MibTable
fmUmFdsServiceFctServerTable = _FmUmFdsServiceFctServerTable_Object(
    (1, 3, 6, 1, 4, 1, 12356, 103, 11, 2, 2, 2)
)
if mibBuilder.loadTexts:
    fmUmFdsServiceFctServerTable.setStatus("current")
_FmUmFdsServiceFctServerEntry_Object = MibTableRow
fmUmFdsServiceFctServerEntry = _FmUmFdsServiceFctServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 12356, 103, 11, 2, 2, 2, 1)
)
fmUmFdsServiceFctServerEntry.setIndexNames(
    (0, "FORTINET-FORTIMANAGER-FORTIANALYZER-MIB", "fmUmFdsServiceFctServerEntryIndex"),
)
if mibBuilder.loadTexts:
    fmUmFdsServiceFctServerEntry.setStatus("current")
_FmUmFdsServiceFctServerEntryIndex_Type = FnIndex
_FmUmFdsServiceFctServerEntryIndex_Object = MibTableColumn
fmUmFdsServiceFctServerEntryIndex = _FmUmFdsServiceFctServerEntryIndex_Object(
    (1, 3, 6, 1, 4, 1, 12356, 103, 11, 2, 2, 2, 1, 1),
    _FmUmFdsServiceFctServerEntryIndex_Type()
)
fmUmFdsServiceFctServerEntryIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fmUmFdsServiceFctServerEntryIndex.setStatus("current")
_FmUmFdsServiceFctServerAddr_Type = InetAddress
_FmUmFdsServiceFctServerAddr_Object = MibTableColumn
fmUmFdsServiceFctServerAddr = _FmUmFdsServiceFctServerAddr_Object(
    (1, 3, 6, 1, 4, 1, 12356, 103, 11, 2, 2, 2, 1, 2),
    _FmUmFdsServiceFctServerAddr_Type()
)
fmUmFdsServiceFctServerAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fmUmFdsServiceFctServerAddr.setStatus("current")
_FmUmFdsServiceFctServerPort_Type = InetPortNumber
_FmUmFdsServiceFctServerPort_Object = MibTableColumn
fmUmFdsServiceFctServerPort = _FmUmFdsServiceFctServerPort_Object(
    (1, 3, 6, 1, 4, 1, 12356, 103, 11, 2, 2, 2, 1, 3),
    _FmUmFdsServiceFctServerPort_Type()
)
fmUmFdsServiceFctServerPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fmUmFdsServiceFctServerPort.setStatus("current")
_FmUmFdsServiceFctServerTimeZone_Type = Integer32
_FmUmFdsServiceFctServerTimeZone_Object = MibTableColumn
fmUmFdsServiceFctServerTimeZone = _FmUmFdsServiceFctServerTimeZone_Object(
    (1, 3, 6, 1, 4, 1, 12356, 103, 11, 2, 2, 2, 1, 4),
    _FmUmFdsServiceFctServerTimeZone_Type()
)
fmUmFdsServiceFctServerTimeZone.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fmUmFdsServiceFctServerTimeZone.setStatus("current")
_FmUmFdsServiceFctServerCurrent_Type = FmUmBoolState
_FmUmFdsServiceFctServerCurrent_Object = MibTableColumn
fmUmFdsServiceFctServerCurrent = _FmUmFdsServiceFctServerCurrent_Object(
    (1, 3, 6, 1, 4, 1, 12356, 103, 11, 2, 2, 2, 1, 5),
    _FmUmFdsServiceFctServerCurrent_Type()
)
fmUmFdsServiceFctServerCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fmUmFdsServiceFctServerCurrent.setStatus("current")
_FmUmFdsPackage_ObjectIdentity = ObjectIdentity
fmUmFdsPackage = _FmUmFdsPackage_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 103, 11, 2, 3)
)
_FmUmFdsObjectTable_Object = MibTable
fmUmFdsObjectTable = _FmUmFdsObjectTable_Object(
    (1, 3, 6, 1, 4, 1, 12356, 103, 11, 2, 3, 1)
)
if mibBuilder.loadTexts:
    fmUmFdsObjectTable.setStatus("current")
_FmUmFdsObjectEntry_Object = MibTableRow
fmUmFdsObjectEntry = _FmUmFdsObjectEntry_Object(
    (1, 3, 6, 1, 4, 1, 12356, 103, 11, 2, 3, 1, 1)
)
fmUmFdsObjectEntry.setIndexNames(
    (0, "FORTINET-FORTIMANAGER-FORTIANALYZER-MIB", "fmUmFdsObjectEntryIndex"),
)
if mibBuilder.loadTexts:
    fmUmFdsObjectEntry.setStatus("current")
_FmUmFdsObjectEntryIndex_Type = FnIndex
_FmUmFdsObjectEntryIndex_Object = MibTableColumn
fmUmFdsObjectEntryIndex = _FmUmFdsObjectEntryIndex_Object(
    (1, 3, 6, 1, 4, 1, 12356, 103, 11, 2, 3, 1, 1, 1),
    _FmUmFdsObjectEntryIndex_Type()
)
fmUmFdsObjectEntryIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fmUmFdsObjectEntryIndex.setStatus("current")


class _FmUmFdsObjectEntryObjid_Type(DisplayString):
    """Custom type fmUmFdsObjectEntryObjid based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(17, 17),
    )
    fixed_length = 17


_FmUmFdsObjectEntryObjid_Type.__name__ = "DisplayString"
_FmUmFdsObjectEntryObjid_Object = MibTableColumn
fmUmFdsObjectEntryObjid = _FmUmFdsObjectEntryObjid_Object(
    (1, 3, 6, 1, 4, 1, 12356, 103, 11, 2, 3, 1, 1, 2),
    _FmUmFdsObjectEntryObjid_Type()
)
fmUmFdsObjectEntryObjid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fmUmFdsObjectEntryObjid.setStatus("current")


class _FmUmFdsObjectEntryVersion_Type(DisplayString):
    """Custom type fmUmFdsObjectEntryVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_FmUmFdsObjectEntryVersion_Type.__name__ = "DisplayString"
_FmUmFdsObjectEntryVersion_Object = MibTableColumn
fmUmFdsObjectEntryVersion = _FmUmFdsObjectEntryVersion_Object(
    (1, 3, 6, 1, 4, 1, 12356, 103, 11, 2, 3, 1, 1, 3),
    _FmUmFdsObjectEntryVersion_Type()
)
fmUmFdsObjectEntryVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fmUmFdsObjectEntryVersion.setStatus("current")


class _FmUmFdsObjectEntryDate_Type(DisplayString):
    """Custom type fmUmFdsObjectEntryDate based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_FmUmFdsObjectEntryDate_Type.__name__ = "DisplayString"
_FmUmFdsObjectEntryDate_Object = MibTableColumn
fmUmFdsObjectEntryDate = _FmUmFdsObjectEntryDate_Object(
    (1, 3, 6, 1, 4, 1, 12356, 103, 11, 2, 3, 1, 1, 4),
    _FmUmFdsObjectEntryDate_Type()
)
fmUmFdsObjectEntryDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fmUmFdsObjectEntryDate.setStatus("current")
_FmUmFdsObjectEntrySize_Type = Counter64
_FmUmFdsObjectEntrySize_Object = MibTableColumn
fmUmFdsObjectEntrySize = _FmUmFdsObjectEntrySize_Object(
    (1, 3, 6, 1, 4, 1, 12356, 103, 11, 2, 3, 1, 1, 5),
    _FmUmFdsObjectEntrySize_Type()
)
fmUmFdsObjectEntrySize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fmUmFdsObjectEntrySize.setStatus("current")


class _FmUmFdsObjectEntryDesc_Type(DisplayString):
    """Custom type fmUmFdsObjectEntryDesc based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_FmUmFdsObjectEntryDesc_Type.__name__ = "DisplayString"
_FmUmFdsObjectEntryDesc_Object = MibTableColumn
fmUmFdsObjectEntryDesc = _FmUmFdsObjectEntryDesc_Object(
    (1, 3, 6, 1, 4, 1, 12356, 103, 11, 2, 3, 1, 1, 6),
    _FmUmFdsObjectEntryDesc_Type()
)
fmUmFdsObjectEntryDesc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fmUmFdsObjectEntryDesc.setStatus("current")


class _FmUmFdsObjectEntryProduct_Type(DisplayString):
    """Custom type fmUmFdsObjectEntryProduct based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_FmUmFdsObjectEntryProduct_Type.__name__ = "DisplayString"
_FmUmFdsObjectEntryProduct_Object = MibTableColumn
fmUmFdsObjectEntryProduct = _FmUmFdsObjectEntryProduct_Object(
    (1, 3, 6, 1, 4, 1, 12356, 103, 11, 2, 3, 1, 1, 7),
    _FmUmFdsObjectEntryProduct_Type()
)
fmUmFdsObjectEntryProduct.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fmUmFdsObjectEntryProduct.setStatus("current")
_FmUmDevice_ObjectIdentity = ObjectIdentity
fmUmDevice = _FmUmDevice_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 103, 11, 2, 4)
)
_FmUmDeviceStatusTable_Object = MibTable
fmUmDeviceStatusTable = _FmUmDeviceStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 12356, 103, 11, 2, 4, 1)
)
if mibBuilder.loadTexts:
    fmUmDeviceStatusTable.setStatus("current")
_FmUmDeviceStatusEntry_Object = MibTableRow
fmUmDeviceStatusEntry = _FmUmDeviceStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 12356, 103, 11, 2, 4, 1, 1)
)
fmUmDeviceStatusEntry.setIndexNames(
    (0, "FORTINET-FORTIMANAGER-FORTIANALYZER-MIB", "fmUmDeviceStatusEntryIndex"),
)
if mibBuilder.loadTexts:
    fmUmDeviceStatusEntry.setStatus("current")
_FmUmDeviceStatusEntryIndex_Type = FnIndex
_FmUmDeviceStatusEntryIndex_Object = MibTableColumn
fmUmDeviceStatusEntryIndex = _FmUmDeviceStatusEntryIndex_Object(
    (1, 3, 6, 1, 4, 1, 12356, 103, 11, 2, 4, 1, 1, 1),
    _FmUmDeviceStatusEntryIndex_Type()
)
fmUmDeviceStatusEntryIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fmUmDeviceStatusEntryIndex.setStatus("current")


class _FmUmDeviceStatusEntrySerial_Type(DisplayString):
    """Custom type fmUmDeviceStatusEntrySerial based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )
    fixed_length = 16


_FmUmDeviceStatusEntrySerial_Type.__name__ = "DisplayString"
_FmUmDeviceStatusEntrySerial_Object = MibTableColumn
fmUmDeviceStatusEntrySerial = _FmUmDeviceStatusEntrySerial_Object(
    (1, 3, 6, 1, 4, 1, 12356, 103, 11, 2, 4, 1, 1, 2),
    _FmUmDeviceStatusEntrySerial_Type()
)
fmUmDeviceStatusEntrySerial.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fmUmDeviceStatusEntrySerial.setStatus("current")


class _FmUmDeviceStatusEntryStatus_Type(DisplayString):
    """Custom type fmUmDeviceStatusEntryStatus based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_FmUmDeviceStatusEntryStatus_Type.__name__ = "DisplayString"
_FmUmDeviceStatusEntryStatus_Object = MibTableColumn
fmUmDeviceStatusEntryStatus = _FmUmDeviceStatusEntryStatus_Object(
    (1, 3, 6, 1, 4, 1, 12356, 103, 11, 2, 4, 1, 1, 3),
    _FmUmDeviceStatusEntryStatus_Type()
)
fmUmDeviceStatusEntryStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fmUmDeviceStatusEntryStatus.setStatus("current")
_FmUmDeviceStatusEntryUpdateTime_Type = Counter64
_FmUmDeviceStatusEntryUpdateTime_Object = MibTableColumn
fmUmDeviceStatusEntryUpdateTime = _FmUmDeviceStatusEntryUpdateTime_Object(
    (1, 3, 6, 1, 4, 1, 12356, 103, 11, 2, 4, 1, 1, 4),
    _FmUmDeviceStatusEntryUpdateTime_Type()
)
fmUmDeviceStatusEntryUpdateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fmUmDeviceStatusEntryUpdateTime.setStatus("current")
_FmUmDeviceObjectTable_Object = MibTable
fmUmDeviceObjectTable = _FmUmDeviceObjectTable_Object(
    (1, 3, 6, 1, 4, 1, 12356, 103, 11, 2, 4, 2)
)
if mibBuilder.loadTexts:
    fmUmDeviceObjectTable.setStatus("current")
_FmUmDeviceObjectEntry_Object = MibTableRow
fmUmDeviceObjectEntry = _FmUmDeviceObjectEntry_Object(
    (1, 3, 6, 1, 4, 1, 12356, 103, 11, 2, 4, 2, 1)
)
fmUmDeviceObjectEntry.setIndexNames(
    (0, "FORTINET-FORTIMANAGER-FORTIANALYZER-MIB", "fmUmDeviceObjectEntryIndex"),
)
if mibBuilder.loadTexts:
    fmUmDeviceObjectEntry.setStatus("current")
_FmUmDeviceObjectEntryIndex_Type = FnIndex
_FmUmDeviceObjectEntryIndex_Object = MibTableColumn
fmUmDeviceObjectEntryIndex = _FmUmDeviceObjectEntryIndex_Object(
    (1, 3, 6, 1, 4, 1, 12356, 103, 11, 2, 4, 2, 1, 1),
    _FmUmDeviceObjectEntryIndex_Type()
)
fmUmDeviceObjectEntryIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fmUmDeviceObjectEntryIndex.setStatus("current")


class _FmUmDeviceObjectEntrySerial_Type(DisplayString):
    """Custom type fmUmDeviceObjectEntrySerial based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )
    fixed_length = 16


_FmUmDeviceObjectEntrySerial_Type.__name__ = "DisplayString"
_FmUmDeviceObjectEntrySerial_Object = MibTableColumn
fmUmDeviceObjectEntrySerial = _FmUmDeviceObjectEntrySerial_Object(
    (1, 3, 6, 1, 4, 1, 12356, 103, 11, 2, 4, 2, 1, 2),
    _FmUmDeviceObjectEntrySerial_Type()
)
fmUmDeviceObjectEntrySerial.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fmUmDeviceObjectEntrySerial.setStatus("current")


class _FmUmDeviceObjectEntryObjid_Type(DisplayString):
    """Custom type fmUmDeviceObjectEntryObjid based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(17, 17),
    )
    fixed_length = 17


_FmUmDeviceObjectEntryObjid_Type.__name__ = "DisplayString"
_FmUmDeviceObjectEntryObjid_Object = MibTableColumn
fmUmDeviceObjectEntryObjid = _FmUmDeviceObjectEntryObjid_Object(
    (1, 3, 6, 1, 4, 1, 12356, 103, 11, 2, 4, 2, 1, 3),
    _FmUmDeviceObjectEntryObjid_Type()
)
fmUmDeviceObjectEntryObjid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fmUmDeviceObjectEntryObjid.setStatus("current")


class _FmUmDeviceObjectEntryDeviceVersion_Type(DisplayString):
    """Custom type fmUmDeviceObjectEntryDeviceVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_FmUmDeviceObjectEntryDeviceVersion_Type.__name__ = "DisplayString"
_FmUmDeviceObjectEntryDeviceVersion_Object = MibTableColumn
fmUmDeviceObjectEntryDeviceVersion = _FmUmDeviceObjectEntryDeviceVersion_Object(
    (1, 3, 6, 1, 4, 1, 12356, 103, 11, 2, 4, 2, 1, 4),
    _FmUmDeviceObjectEntryDeviceVersion_Type()
)
fmUmDeviceObjectEntryDeviceVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fmUmDeviceObjectEntryDeviceVersion.setStatus("current")


class _FmUmDeviceObjectEntryServerVersion_Type(DisplayString):
    """Custom type fmUmDeviceObjectEntryServerVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_FmUmDeviceObjectEntryServerVersion_Type.__name__ = "DisplayString"
_FmUmDeviceObjectEntryServerVersion_Object = MibTableColumn
fmUmDeviceObjectEntryServerVersion = _FmUmDeviceObjectEntryServerVersion_Object(
    (1, 3, 6, 1, 4, 1, 12356, 103, 11, 2, 4, 2, 1, 5),
    _FmUmDeviceObjectEntryServerVersion_Type()
)
fmUmDeviceObjectEntryServerVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fmUmDeviceObjectEntryServerVersion.setStatus("current")


class _FmUmDeviceObjectEntryPreferVersion_Type(DisplayString):
    """Custom type fmUmDeviceObjectEntryPreferVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_FmUmDeviceObjectEntryPreferVersion_Type.__name__ = "DisplayString"
_FmUmDeviceObjectEntryPreferVersion_Object = MibTableColumn
fmUmDeviceObjectEntryPreferVersion = _FmUmDeviceObjectEntryPreferVersion_Object(
    (1, 3, 6, 1, 4, 1, 12356, 103, 11, 2, 4, 2, 1, 6),
    _FmUmDeviceObjectEntryPreferVersion_Type()
)
fmUmDeviceObjectEntryPreferVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fmUmDeviceObjectEntryPreferVersion.setStatus("current")
_FmUmFgd_ObjectIdentity = ObjectIdentity
fmUmFgd = _FmUmFgd_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 103, 11, 3)
)
_FmUmFgdServiceFgd_ObjectIdentity = ObjectIdentity
fmUmFgdServiceFgd = _FmUmFgdServiceFgd_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 103, 11, 3, 1)
)
_FmUmFgdServiceFgdStatus_Type = FmUmServiceStatus
_FmUmFgdServiceFgdStatus_Object = MibScalar
fmUmFgdServiceFgdStatus = _FmUmFgdServiceFgdStatus_Object(
    (1, 3, 6, 1, 4, 1, 12356, 103, 11, 3, 1, 1),
    _FmUmFgdServiceFgdStatus_Type()
)
fmUmFgdServiceFgdStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fmUmFgdServiceFgdStatus.setStatus("current")
_FmUmFgdServiceFgdServerTable_Object = MibTable
fmUmFgdServiceFgdServerTable = _FmUmFgdServiceFgdServerTable_Object(
    (1, 3, 6, 1, 4, 1, 12356, 103, 11, 3, 1, 2)
)
if mibBuilder.loadTexts:
    fmUmFgdServiceFgdServerTable.setStatus("current")
_FmUmFgdServiceFgdServerEntry_Object = MibTableRow
fmUmFgdServiceFgdServerEntry = _FmUmFgdServiceFgdServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 12356, 103, 11, 3, 1, 2, 1)
)
fmUmFgdServiceFgdServerEntry.setIndexNames(
    (0, "FORTINET-FORTIMANAGER-FORTIANALYZER-MIB", "fmUmFgdServiceFgdServerEntryIndex"),
)
if mibBuilder.loadTexts:
    fmUmFgdServiceFgdServerEntry.setStatus("current")
_FmUmFgdServiceFgdServerEntryIndex_Type = FnIndex
_FmUmFgdServiceFgdServerEntryIndex_Object = MibTableColumn
fmUmFgdServiceFgdServerEntryIndex = _FmUmFgdServiceFgdServerEntryIndex_Object(
    (1, 3, 6, 1, 4, 1, 12356, 103, 11, 3, 1, 2, 1, 1),
    _FmUmFgdServiceFgdServerEntryIndex_Type()
)
fmUmFgdServiceFgdServerEntryIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fmUmFgdServiceFgdServerEntryIndex.setStatus("current")
_FmUmFgdServiceFgdServerAddr_Type = InetAddress
_FmUmFgdServiceFgdServerAddr_Object = MibTableColumn
fmUmFgdServiceFgdServerAddr = _FmUmFgdServiceFgdServerAddr_Object(
    (1, 3, 6, 1, 4, 1, 12356, 103, 11, 3, 1, 2, 1, 2),
    _FmUmFgdServiceFgdServerAddr_Type()
)
fmUmFgdServiceFgdServerAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fmUmFgdServiceFgdServerAddr.setStatus("current")
_FmUmFgdServiceFgdServerPort_Type = InetPortNumber
_FmUmFgdServiceFgdServerPort_Object = MibTableColumn
fmUmFgdServiceFgdServerPort = _FmUmFgdServiceFgdServerPort_Object(
    (1, 3, 6, 1, 4, 1, 12356, 103, 11, 3, 1, 2, 1, 3),
    _FmUmFgdServiceFgdServerPort_Type()
)
fmUmFgdServiceFgdServerPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fmUmFgdServiceFgdServerPort.setStatus("current")
_FmUmFgdServiceFgdServerTimeZone_Type = Integer32
_FmUmFgdServiceFgdServerTimeZone_Object = MibTableColumn
fmUmFgdServiceFgdServerTimeZone = _FmUmFgdServiceFgdServerTimeZone_Object(
    (1, 3, 6, 1, 4, 1, 12356, 103, 11, 3, 1, 2, 1, 4),
    _FmUmFgdServiceFgdServerTimeZone_Type()
)
fmUmFgdServiceFgdServerTimeZone.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fmUmFgdServiceFgdServerTimeZone.setStatus("current")
_FmUmFgdServiceFgdServerCurrent_Type = FmUmBoolState
_FmUmFgdServiceFgdServerCurrent_Object = MibTableColumn
fmUmFgdServiceFgdServerCurrent = _FmUmFgdServiceFgdServerCurrent_Object(
    (1, 3, 6, 1, 4, 1, 12356, 103, 11, 3, 1, 2, 1, 5),
    _FmUmFgdServiceFgdServerCurrent_Type()
)
fmUmFgdServiceFgdServerCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fmUmFgdServiceFgdServerCurrent.setStatus("current")
_FmUmFgdServiceFgfq_ObjectIdentity = ObjectIdentity
fmUmFgdServiceFgfq = _FmUmFgdServiceFgfq_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 103, 11, 3, 2)
)
_FmUmFgdServiceFgfqStatus_Type = FmUmServiceStatus
_FmUmFgdServiceFgfqStatus_Object = MibScalar
fmUmFgdServiceFgfqStatus = _FmUmFgdServiceFgfqStatus_Object(
    (1, 3, 6, 1, 4, 1, 12356, 103, 11, 3, 2, 1),
    _FmUmFgdServiceFgfqStatus_Type()
)
fmUmFgdServiceFgfqStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fmUmFgdServiceFgfqStatus.setStatus("current")
_FmUmFgdServiceFgfqServerTable_Object = MibTable
fmUmFgdServiceFgfqServerTable = _FmUmFgdServiceFgfqServerTable_Object(
    (1, 3, 6, 1, 4, 1, 12356, 103, 11, 3, 2, 2)
)
if mibBuilder.loadTexts:
    fmUmFgdServiceFgfqServerTable.setStatus("current")
_FmUmFgdServiceFgfqServerEntry_Object = MibTableRow
fmUmFgdServiceFgfqServerEntry = _FmUmFgdServiceFgfqServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 12356, 103, 11, 3, 2, 2, 1)
)
fmUmFgdServiceFgfqServerEntry.setIndexNames(
    (0, "FORTINET-FORTIMANAGER-FORTIANALYZER-MIB", "fmUmFgdServiceFgfqServerEntryIndex"),
)
if mibBuilder.loadTexts:
    fmUmFgdServiceFgfqServerEntry.setStatus("current")
_FmUmFgdServiceFgfqServerEntryIndex_Type = FnIndex
_FmUmFgdServiceFgfqServerEntryIndex_Object = MibTableColumn
fmUmFgdServiceFgfqServerEntryIndex = _FmUmFgdServiceFgfqServerEntryIndex_Object(
    (1, 3, 6, 1, 4, 1, 12356, 103, 11, 3, 2, 2, 1, 1),
    _FmUmFgdServiceFgfqServerEntryIndex_Type()
)
fmUmFgdServiceFgfqServerEntryIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fmUmFgdServiceFgfqServerEntryIndex.setStatus("current")
_FmUmFgdServiceFgfqServerAddr_Type = InetAddress
_FmUmFgdServiceFgfqServerAddr_Object = MibTableColumn
fmUmFgdServiceFgfqServerAddr = _FmUmFgdServiceFgfqServerAddr_Object(
    (1, 3, 6, 1, 4, 1, 12356, 103, 11, 3, 2, 2, 1, 2),
    _FmUmFgdServiceFgfqServerAddr_Type()
)
fmUmFgdServiceFgfqServerAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fmUmFgdServiceFgfqServerAddr.setStatus("current")
_FmUmFgdServiceFgfqServerPort_Type = InetPortNumber
_FmUmFgdServiceFgfqServerPort_Object = MibTableColumn
fmUmFgdServiceFgfqServerPort = _FmUmFgdServiceFgfqServerPort_Object(
    (1, 3, 6, 1, 4, 1, 12356, 103, 11, 3, 2, 2, 1, 3),
    _FmUmFgdServiceFgfqServerPort_Type()
)
fmUmFgdServiceFgfqServerPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fmUmFgdServiceFgfqServerPort.setStatus("current")
_FmUmFgdServiceFgfqServerTimeZone_Type = Integer32
_FmUmFgdServiceFgfqServerTimeZone_Object = MibTableColumn
fmUmFgdServiceFgfqServerTimeZone = _FmUmFgdServiceFgfqServerTimeZone_Object(
    (1, 3, 6, 1, 4, 1, 12356, 103, 11, 3, 2, 2, 1, 4),
    _FmUmFgdServiceFgfqServerTimeZone_Type()
)
fmUmFgdServiceFgfqServerTimeZone.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fmUmFgdServiceFgfqServerTimeZone.setStatus("current")
_FmUmFgdServiceFgfqServerCurrent_Type = FmUmBoolState
_FmUmFgdServiceFgfqServerCurrent_Object = MibTableColumn
fmUmFgdServiceFgfqServerCurrent = _FmUmFgdServiceFgfqServerCurrent_Object(
    (1, 3, 6, 1, 4, 1, 12356, 103, 11, 3, 2, 2, 1, 5),
    _FmUmFgdServiceFgfqServerCurrent_Type()
)
fmUmFgdServiceFgfqServerCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fmUmFgdServiceFgfqServerCurrent.setStatus("current")
_FmUmFgdPackage_ObjectIdentity = ObjectIdentity
fmUmFgdPackage = _FmUmFgdPackage_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 103, 11, 3, 3)
)
_FmUmFgdDBVersionTable_Object = MibTable
fmUmFgdDBVersionTable = _FmUmFgdDBVersionTable_Object(
    (1, 3, 6, 1, 4, 1, 12356, 103, 11, 3, 3, 1)
)
if mibBuilder.loadTexts:
    fmUmFgdDBVersionTable.setStatus("current")
_FmUmFgdDBVersionEntry_Object = MibTableRow
fmUmFgdDBVersionEntry = _FmUmFgdDBVersionEntry_Object(
    (1, 3, 6, 1, 4, 1, 12356, 103, 11, 3, 3, 1, 1)
)
fmUmFgdDBVersionEntry.setIndexNames(
    (0, "FORTINET-FORTIMANAGER-FORTIANALYZER-MIB", "fmUmFgdDBVersionEntryIndex"),
)
if mibBuilder.loadTexts:
    fmUmFgdDBVersionEntry.setStatus("current")
_FmUmFgdDBVersionEntryIndex_Type = FnIndex
_FmUmFgdDBVersionEntryIndex_Object = MibTableColumn
fmUmFgdDBVersionEntryIndex = _FmUmFgdDBVersionEntryIndex_Object(
    (1, 3, 6, 1, 4, 1, 12356, 103, 11, 3, 3, 1, 1, 1),
    _FmUmFgdDBVersionEntryIndex_Type()
)
fmUmFgdDBVersionEntryIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fmUmFgdDBVersionEntryIndex.setStatus("current")


class _FmUmFgdDBVersionEntryCategory_Type(DisplayString):
    """Custom type fmUmFgdDBVersionEntryCategory based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_FmUmFgdDBVersionEntryCategory_Type.__name__ = "DisplayString"
_FmUmFgdDBVersionEntryCategory_Object = MibTableColumn
fmUmFgdDBVersionEntryCategory = _FmUmFgdDBVersionEntryCategory_Object(
    (1, 3, 6, 1, 4, 1, 12356, 103, 11, 3, 3, 1, 1, 2),
    _FmUmFgdDBVersionEntryCategory_Type()
)
fmUmFgdDBVersionEntryCategory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fmUmFgdDBVersionEntryCategory.setStatus("current")


class _FmUmFgdDBVersionEntryVersion_Type(DisplayString):
    """Custom type fmUmFgdDBVersionEntryVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_FmUmFgdDBVersionEntryVersion_Type.__name__ = "DisplayString"
_FmUmFgdDBVersionEntryVersion_Object = MibTableColumn
fmUmFgdDBVersionEntryVersion = _FmUmFgdDBVersionEntryVersion_Object(
    (1, 3, 6, 1, 4, 1, 12356, 103, 11, 3, 3, 1, 1, 3),
    _FmUmFgdDBVersionEntryVersion_Type()
)
fmUmFgdDBVersionEntryVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fmUmFgdDBVersionEntryVersion.setStatus("current")
_FmUmFgdDBVersionEntrySize_Type = Counter64
_FmUmFgdDBVersionEntrySize_Object = MibTableColumn
fmUmFgdDBVersionEntrySize = _FmUmFgdDBVersionEntrySize_Object(
    (1, 3, 6, 1, 4, 1, 12356, 103, 11, 3, 3, 1, 1, 4),
    _FmUmFgdDBVersionEntrySize_Type()
)
fmUmFgdDBVersionEntrySize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fmUmFgdDBVersionEntrySize.setStatus("current")
_FmUmFgdDBVersionEntryDate_Type = Counter64
_FmUmFgdDBVersionEntryDate_Object = MibTableColumn
fmUmFgdDBVersionEntryDate = _FmUmFgdDBVersionEntryDate_Object(
    (1, 3, 6, 1, 4, 1, 12356, 103, 11, 3, 3, 1, 1, 5),
    _FmUmFgdDBVersionEntryDate_Type()
)
fmUmFgdDBVersionEntryDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fmUmFgdDBVersionEntryDate.setStatus("current")


class _FmUmFgdDBVersionEntryDesc_Type(DisplayString):
    """Custom type fmUmFgdDBVersionEntryDesc based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_FmUmFgdDBVersionEntryDesc_Type.__name__ = "DisplayString"
_FmUmFgdDBVersionEntryDesc_Object = MibTableColumn
fmUmFgdDBVersionEntryDesc = _FmUmFgdDBVersionEntryDesc_Object(
    (1, 3, 6, 1, 4, 1, 12356, 103, 11, 3, 3, 1, 1, 6),
    _FmUmFgdDBVersionEntryDesc_Type()
)
fmUmFgdDBVersionEntryDesc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fmUmFgdDBVersionEntryDesc.setStatus("current")
_FmUmFgdQueryStatistic_ObjectIdentity = ObjectIdentity
fmUmFgdQueryStatistic = _FmUmFgdQueryStatistic_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12356, 103, 11, 3, 4)
)
_FmUmFgdQueryStatisticTop10SitesTable_Object = MibTable
fmUmFgdQueryStatisticTop10SitesTable = _FmUmFgdQueryStatisticTop10SitesTable_Object(
    (1, 3, 6, 1, 4, 1, 12356, 103, 11, 3, 4, 1)
)
if mibBuilder.loadTexts:
    fmUmFgdQueryStatisticTop10SitesTable.setStatus("current")
_FmUmFgdQueryStatisticTop10SitesEntry_Object = MibTableRow
fmUmFgdQueryStatisticTop10SitesEntry = _FmUmFgdQueryStatisticTop10SitesEntry_Object(
    (1, 3, 6, 1, 4, 1, 12356, 103, 11, 3, 4, 1, 1)
)
fmUmFgdQueryStatisticTop10SitesEntry.setIndexNames(
    (0, "FORTINET-FORTIMANAGER-FORTIANALYZER-MIB", "fmUmFgdQueryStatisticTop10SitesEntryIndex"),
)
if mibBuilder.loadTexts:
    fmUmFgdQueryStatisticTop10SitesEntry.setStatus("current")
_FmUmFgdQueryStatisticTop10SitesEntryIndex_Type = FnIndex
_FmUmFgdQueryStatisticTop10SitesEntryIndex_Object = MibTableColumn
fmUmFgdQueryStatisticTop10SitesEntryIndex = _FmUmFgdQueryStatisticTop10SitesEntryIndex_Object(
    (1, 3, 6, 1, 4, 1, 12356, 103, 11, 3, 4, 1, 1, 1),
    _FmUmFgdQueryStatisticTop10SitesEntryIndex_Type()
)
fmUmFgdQueryStatisticTop10SitesEntryIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fmUmFgdQueryStatisticTop10SitesEntryIndex.setStatus("current")
_FmUmFgdQueryStatisticTop10SitesEntryAddress_Type = InetAddress
_FmUmFgdQueryStatisticTop10SitesEntryAddress_Object = MibTableColumn
fmUmFgdQueryStatisticTop10SitesEntryAddress = _FmUmFgdQueryStatisticTop10SitesEntryAddress_Object(
    (1, 3, 6, 1, 4, 1, 12356, 103, 11, 3, 4, 1, 1, 2),
    _FmUmFgdQueryStatisticTop10SitesEntryAddress_Type()
)
fmUmFgdQueryStatisticTop10SitesEntryAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fmUmFgdQueryStatisticTop10SitesEntryAddress.setStatus("current")
_FmUmFgdQueryStatisticTop10SitesEntryVisits_Type = Counter64
_FmUmFgdQueryStatisticTop10SitesEntryVisits_Object = MibTableColumn
fmUmFgdQueryStatisticTop10SitesEntryVisits = _FmUmFgdQueryStatisticTop10SitesEntryVisits_Object(
    (1, 3, 6, 1, 4, 1, 12356, 103, 11, 3, 4, 1, 1, 3),
    _FmUmFgdQueryStatisticTop10SitesEntryVisits_Type()
)
fmUmFgdQueryStatisticTop10SitesEntryVisits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fmUmFgdQueryStatisticTop10SitesEntryVisits.setStatus("current")
_FmUmFgdQueryStatisticTop10DevicesTable_Object = MibTable
fmUmFgdQueryStatisticTop10DevicesTable = _FmUmFgdQueryStatisticTop10DevicesTable_Object(
    (1, 3, 6, 1, 4, 1, 12356, 103, 11, 3, 4, 2)
)
if mibBuilder.loadTexts:
    fmUmFgdQueryStatisticTop10DevicesTable.setStatus("current")
_FmUmFgdQueryStatisticTop10DevicesEntry_Object = MibTableRow
fmUmFgdQueryStatisticTop10DevicesEntry = _FmUmFgdQueryStatisticTop10DevicesEntry_Object(
    (1, 3, 6, 1, 4, 1, 12356, 103, 11, 3, 4, 2, 1)
)
fmUmFgdQueryStatisticTop10DevicesEntry.setIndexNames(
    (0, "FORTINET-FORTIMANAGER-FORTIANALYZER-MIB", "fmUmFgdQueryStatisticTop10DevicesEntryIndex"),
)
if mibBuilder.loadTexts:
    fmUmFgdQueryStatisticTop10DevicesEntry.setStatus("current")
_FmUmFgdQueryStatisticTop10DevicesEntryIndex_Type = FnIndex
_FmUmFgdQueryStatisticTop10DevicesEntryIndex_Object = MibTableColumn
fmUmFgdQueryStatisticTop10DevicesEntryIndex = _FmUmFgdQueryStatisticTop10DevicesEntryIndex_Object(
    (1, 3, 6, 1, 4, 1, 12356, 103, 11, 3, 4, 2, 1, 1),
    _FmUmFgdQueryStatisticTop10DevicesEntryIndex_Type()
)
fmUmFgdQueryStatisticTop10DevicesEntryIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fmUmFgdQueryStatisticTop10DevicesEntryIndex.setStatus("current")


class _FmUmFgdQueryStatisticTop10DevicesEntryName_Type(DisplayString):
    """Custom type fmUmFgdQueryStatisticTop10DevicesEntryName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 512),
    )


_FmUmFgdQueryStatisticTop10DevicesEntryName_Type.__name__ = "DisplayString"
_FmUmFgdQueryStatisticTop10DevicesEntryName_Object = MibTableColumn
fmUmFgdQueryStatisticTop10DevicesEntryName = _FmUmFgdQueryStatisticTop10DevicesEntryName_Object(
    (1, 3, 6, 1, 4, 1, 12356, 103, 11, 3, 4, 2, 1, 2),
    _FmUmFgdQueryStatisticTop10DevicesEntryName_Type()
)
fmUmFgdQueryStatisticTop10DevicesEntryName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fmUmFgdQueryStatisticTop10DevicesEntryName.setStatus("current")
_FmUmFgdQueryStatisticTop10DevicesEntryQueries_Type = Counter64
_FmUmFgdQueryStatisticTop10DevicesEntryQueries_Object = MibTableColumn
fmUmFgdQueryStatisticTop10DevicesEntryQueries = _FmUmFgdQueryStatisticTop10DevicesEntryQueries_Object(
    (1, 3, 6, 1, 4, 1, 12356, 103, 11, 3, 4, 2, 1, 3),
    _FmUmFgdQueryStatisticTop10DevicesEntryQueries_Type()
)
fmUmFgdQueryStatisticTop10DevicesEntryQueries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fmUmFgdQueryStatisticTop10DevicesEntryQueries.setStatus("current")
_FmUmFgdQueryStatisticQueryHistoryTable_Object = MibTable
fmUmFgdQueryStatisticQueryHistoryTable = _FmUmFgdQueryStatisticQueryHistoryTable_Object(
    (1, 3, 6, 1, 4, 1, 12356, 103, 11, 3, 4, 3)
)
if mibBuilder.loadTexts:
    fmUmFgdQueryStatisticQueryHistoryTable.setStatus("current")
_FmUmFgdQueryStatisticQueryHistoryEntry_Object = MibTableRow
fmUmFgdQueryStatisticQueryHistoryEntry = _FmUmFgdQueryStatisticQueryHistoryEntry_Object(
    (1, 3, 6, 1, 4, 1, 12356, 103, 11, 3, 4, 3, 1)
)
fmUmFgdQueryStatisticQueryHistoryEntry.setIndexNames(
    (0, "FORTINET-FORTIMANAGER-FORTIANALYZER-MIB", "fmUmFgdQueryStatisticQueryHistoryEntryIndex"),
)
if mibBuilder.loadTexts:
    fmUmFgdQueryStatisticQueryHistoryEntry.setStatus("current")
_FmUmFgdQueryStatisticQueryHistoryEntryIndex_Type = FnIndex
_FmUmFgdQueryStatisticQueryHistoryEntryIndex_Object = MibTableColumn
fmUmFgdQueryStatisticQueryHistoryEntryIndex = _FmUmFgdQueryStatisticQueryHistoryEntryIndex_Object(
    (1, 3, 6, 1, 4, 1, 12356, 103, 11, 3, 4, 3, 1, 1),
    _FmUmFgdQueryStatisticQueryHistoryEntryIndex_Type()
)
fmUmFgdQueryStatisticQueryHistoryEntryIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fmUmFgdQueryStatisticQueryHistoryEntryIndex.setStatus("current")
_FmUmFgdQueryStatisticQueryHistoryEntryBeginTime_Type = Counter64
_FmUmFgdQueryStatisticQueryHistoryEntryBeginTime_Object = MibTableColumn
fmUmFgdQueryStatisticQueryHistoryEntryBeginTime = _FmUmFgdQueryStatisticQueryHistoryEntryBeginTime_Object(
    (1, 3, 6, 1, 4, 1, 12356, 103, 11, 3, 4, 3, 1, 2),
    _FmUmFgdQueryStatisticQueryHistoryEntryBeginTime_Type()
)
fmUmFgdQueryStatisticQueryHistoryEntryBeginTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fmUmFgdQueryStatisticQueryHistoryEntryBeginTime.setStatus("current")
_FmUmFgdQueryStatisticQueryHistoryEntryEndTime_Type = Counter64
_FmUmFgdQueryStatisticQueryHistoryEntryEndTime_Object = MibTableColumn
fmUmFgdQueryStatisticQueryHistoryEntryEndTime = _FmUmFgdQueryStatisticQueryHistoryEntryEndTime_Object(
    (1, 3, 6, 1, 4, 1, 12356, 103, 11, 3, 4, 3, 1, 3),
    _FmUmFgdQueryStatisticQueryHistoryEntryEndTime_Type()
)
fmUmFgdQueryStatisticQueryHistoryEntryEndTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fmUmFgdQueryStatisticQueryHistoryEntryEndTime.setStatus("current")


class _FmUmFgdQueryStatisticQueryHistoryEntryDeviceName_Type(DisplayString):
    """Custom type fmUmFgdQueryStatisticQueryHistoryEntryDeviceName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 512),
    )


_FmUmFgdQueryStatisticQueryHistoryEntryDeviceName_Type.__name__ = "DisplayString"
_FmUmFgdQueryStatisticQueryHistoryEntryDeviceName_Object = MibTableColumn
fmUmFgdQueryStatisticQueryHistoryEntryDeviceName = _FmUmFgdQueryStatisticQueryHistoryEntryDeviceName_Object(
    (1, 3, 6, 1, 4, 1, 12356, 103, 11, 3, 4, 3, 1, 4),
    _FmUmFgdQueryStatisticQueryHistoryEntryDeviceName_Type()
)
fmUmFgdQueryStatisticQueryHistoryEntryDeviceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fmUmFgdQueryStatisticQueryHistoryEntryDeviceName.setStatus("current")
_FmUmFgdQueryStatisticQueryHistoryEntryDeviceAddress_Type = InetAddress
_FmUmFgdQueryStatisticQueryHistoryEntryDeviceAddress_Object = MibTableColumn
fmUmFgdQueryStatisticQueryHistoryEntryDeviceAddress = _FmUmFgdQueryStatisticQueryHistoryEntryDeviceAddress_Object(
    (1, 3, 6, 1, 4, 1, 12356, 103, 11, 3, 4, 3, 1, 5),
    _FmUmFgdQueryStatisticQueryHistoryEntryDeviceAddress_Type()
)
fmUmFgdQueryStatisticQueryHistoryEntryDeviceAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fmUmFgdQueryStatisticQueryHistoryEntryDeviceAddress.setStatus("current")
_FmUmFgdQueryStatisticQueryHistoryEntryQueries_Type = Counter64
_FmUmFgdQueryStatisticQueryHistoryEntryQueries_Object = MibTableColumn
fmUmFgdQueryStatisticQueryHistoryEntryQueries = _FmUmFgdQueryStatisticQueryHistoryEntryQueries_Object(
    (1, 3, 6, 1, 4, 1, 12356, 103, 11, 3, 4, 3, 1, 6),
    _FmUmFgdQueryStatisticQueryHistoryEntryQueries_Type()
)
fmUmFgdQueryStatisticQueryHistoryEntryQueries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fmUmFgdQueryStatisticQueryHistoryEntryQueries.setStatus("current")
_FmUmFgdQueryStatisticQueryHistoryEntryHits_Type = Counter64
_FmUmFgdQueryStatisticQueryHistoryEntryHits_Object = MibTableColumn
fmUmFgdQueryStatisticQueryHistoryEntryHits = _FmUmFgdQueryStatisticQueryHistoryEntryHits_Object(
    (1, 3, 6, 1, 4, 1, 12356, 103, 11, 3, 4, 3, 1, 7),
    _FmUmFgdQueryStatisticQueryHistoryEntryHits_Type()
)
fmUmFgdQueryStatisticQueryHistoryEntryHits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fmUmFgdQueryStatisticQueryHistoryEntryHits.setStatus("current")
_FmUmFgdQueryStatisticQueryHistoryEntryMisses_Type = Counter64
_FmUmFgdQueryStatisticQueryHistoryEntryMisses_Object = MibTableColumn
fmUmFgdQueryStatisticQueryHistoryEntryMisses = _FmUmFgdQueryStatisticQueryHistoryEntryMisses_Object(
    (1, 3, 6, 1, 4, 1, 12356, 103, 11, 3, 4, 3, 1, 8),
    _FmUmFgdQueryStatisticQueryHistoryEntryMisses_Type()
)
fmUmFgdQueryStatisticQueryHistoryEntryMisses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fmUmFgdQueryStatisticQueryHistoryEntryMisses.setStatus("current")


class _FmUmFgdQueryStatisticQueryHistoryEntryBandWidth_Type(DisplayString):
    """Custom type fmUmFgdQueryStatisticQueryHistoryEntryBandWidth based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_FmUmFgdQueryStatisticQueryHistoryEntryBandWidth_Type.__name__ = "DisplayString"
_FmUmFgdQueryStatisticQueryHistoryEntryBandWidth_Object = MibTableColumn
fmUmFgdQueryStatisticQueryHistoryEntryBandWidth = _FmUmFgdQueryStatisticQueryHistoryEntryBandWidth_Object(
    (1, 3, 6, 1, 4, 1, 12356, 103, 11, 3, 4, 3, 1, 9),
    _FmUmFgdQueryStatisticQueryHistoryEntryBandWidth_Type()
)
fmUmFgdQueryStatisticQueryHistoryEntryBandWidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fmUmFgdQueryStatisticQueryHistoryEntryBandWidth.setStatus("current")

# Managed Objects groups

fmSystemObjectGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 12356, 103, 10, 2)
)
fmSystemObjectGroup.setObjects(
      *(("FORTINET-FORTIMANAGER-FORTIANALYZER-MIB", "fmSysMemUsed"),
        ("FORTINET-FORTIMANAGER-FORTIANALYZER-MIB", "fmSysMemCapacity"),
        ("FORTINET-FORTIMANAGER-FORTIANALYZER-MIB", "fmSysCpuUsage"),
        ("FORTINET-FORTIMANAGER-FORTIANALYZER-MIB", "fmSysDiskCapacity"),
        ("FORTINET-FORTIMANAGER-FORTIANALYZER-MIB", "fmSysDiskUsage"),
        ("FORTINET-FORTIMANAGER-FORTIANALYZER-MIB", "fmSysCpuUsageExcludedNice"),
        ("FORTINET-FORTIMANAGER-FORTIANALYZER-MIB", "fmSysVersion"),
        ("FORTINET-FORTIMANAGER-FORTIANALYZER-MIB", "fmSysUpTime"),
        ("FORTINET-FORTIMANAGER-FORTIANALYZER-MIB", "fmSysLogRate"),
        ("FORTINET-FORTIMANAGER-FORTIANALYZER-MIB", "fmSysLogRateHr"),
        ("FORTINET-FORTIMANAGER-FORTIANALYZER-MIB", "fmSysLogLagTime"),
        ("FORTINET-FORTIMANAGER-FORTIANALYZER-MIB", "fmSysLogIndexingRate"),
        ("FORTINET-FORTIMANAGER-FORTIANALYZER-MIB", "fmSysLicGbDayToday"),
        ("FORTINET-FORTIMANAGER-FORTIANALYZER-MIB", "fmSysLicGbDayYesterday"),
        ("FORTINET-FORTIMANAGER-FORTIANALYZER-MIB", "fmSysLicGbDayWeekAvg"),
        ("FORTINET-FORTIMANAGER-FORTIANALYZER-MIB", "fmSysDiskNumber"),
        ("FORTINET-FORTIMANAGER-FORTIANALYZER-MIB", "fmSysDiskEntName"),
        ("FORTINET-FORTIMANAGER-FORTIANALYZER-MIB", "fmSysDiskEntUsage"),
        ("FORTINET-FORTIMANAGER-FORTIANALYZER-MIB", "fmSysDiskEntCapacity"),
        ("FORTINET-FORTIMANAGER-FORTIANALYZER-MIB", "fmSysDiskEntIOUtil"),
        ("FORTINET-FORTIMANAGER-FORTIANALYZER-MIB", "fmSysLogForwardName"),
        ("FORTINET-FORTIMANAGER-FORTIANALYZER-MIB", "fmSysLogForwardNumber"),
        ("FORTINET-FORTIMANAGER-FORTIANALYZER-MIB", "fmSysLogForwardRate"))
)
if mibBuilder.loadTexts:
    fmSystemObjectGroup.setStatus("current")

fmNotificationObjComplianceGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 12356, 103, 10, 3)
)
fmNotificationObjComplianceGroup.setObjects(
      *(("FORTINET-FORTIMANAGER-FORTIANALYZER-MIB", "fmRAIDStatus"),
        ("FORTINET-FORTIMANAGER-FORTIANALYZER-MIB", "fmRAIDDevIndex"),
        ("FORTINET-FORTIMANAGER-FORTIANALYZER-MIB", "fmLogRate"),
        ("FORTINET-FORTIMANAGER-FORTIANALYZER-MIB", "fmLogRateThreshold"),
        ("FORTINET-FORTIMANAGER-FORTIANALYZER-MIB", "fmLogDataRate"),
        ("FORTINET-FORTIMANAGER-FORTIANALYZER-MIB", "fmLogDataRateThreshold"),
        ("FORTINET-FORTIMANAGER-FORTIANALYZER-MIB", "fmLicGbDay"),
        ("FORTINET-FORTIMANAGER-FORTIANALYZER-MIB", "fmLicGbDayThreshold"),
        ("FORTINET-FORTIMANAGER-FORTIANALYZER-MIB", "fmLicDevQuota"),
        ("FORTINET-FORTIMANAGER-FORTIANALYZER-MIB", "fmLicDevQuotaThreshold"),
        ("FORTINET-FORTIMANAGER-FORTIANALYZER-MIB", "fmSensorState"),
        ("FORTINET-FORTIMANAGER-FORTIANALYZER-MIB", "fmSensorName"))
)
if mibBuilder.loadTexts:
    fmNotificationObjComplianceGroup.setStatus("current")

fmSessionComplianceGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 12356, 103, 10, 4)
)
fmSessionComplianceGroup.setObjects(
      *(("FORTINET-FORTIMANAGER-FORTIANALYZER-MIB", "fmIpSessProto"),
        ("FORTINET-FORTIMANAGER-FORTIANALYZER-MIB", "fmIpSessFromAddr"),
        ("FORTINET-FORTIMANAGER-FORTIANALYZER-MIB", "fmIpSessFromPort"),
        ("FORTINET-FORTIMANAGER-FORTIANALYZER-MIB", "fmIpSessToAddr"),
        ("FORTINET-FORTIMANAGER-FORTIANALYZER-MIB", "fmIpSessToPort"),
        ("FORTINET-FORTIMANAGER-FORTIANALYZER-MIB", "fmIpSessExp"))
)
if mibBuilder.loadTexts:
    fmSessionComplianceGroup.setStatus("current")

fmAdomComplianceGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 12356, 103, 10, 5)
)
fmAdomComplianceGroup.setObjects(
      *(("FORTINET-FORTIMANAGER-FORTIANALYZER-MIB", "fmAdomEnabled"),
        ("FORTINET-FORTIMANAGER-FORTIANALYZER-MIB", "fmAdomNumber"),
        ("FORTINET-FORTIMANAGER-FORTIANALYZER-MIB", "fmAdomMax"),
        ("FORTINET-FORTIMANAGER-FORTIANALYZER-MIB", "fmAdomEntName"),
        ("FORTINET-FORTIMANAGER-FORTIANALYZER-MIB", "fmAdomEntState"),
        ("FORTINET-FORTIMANAGER-FORTIANALYZER-MIB", "fmAdomEntMode"),
        ("FORTINET-FORTIMANAGER-FORTIANALYZER-MIB", "fmAdomEntFgtNumber"),
        ("FORTINET-FORTIMANAGER-FORTIANALYZER-MIB", "fmAdomEntPolicyPackageNumber"),
        ("FORTINET-FORTIMANAGER-FORTIANALYZER-MIB", "fmAdomEntOsVersion"),
        ("FORTINET-FORTIMANAGER-FORTIANALYZER-MIB", "fmAdomEntMr"),
        ("FORTINET-FORTIMANAGER-FORTIANALYZER-MIB", "fmAdomEntVpnMode"),
        ("FORTINET-FORTIMANAGER-FORTIANALYZER-MIB", "fmAdomEntLogRateMinute"),
        ("FORTINET-FORTIMANAGER-FORTIANALYZER-MIB", "fmAdomEntArchiveLogRetention"),
        ("FORTINET-FORTIMANAGER-FORTIANALYZER-MIB", "fmAdomEntArchiveLogQuota"),
        ("FORTINET-FORTIMANAGER-FORTIANALYZER-MIB", "fmAdomEntArchiveLogUsedSpace"),
        ("FORTINET-FORTIMANAGER-FORTIANALYZER-MIB", "fmAdomEntArchiveLogUsedSpacePercent"),
        ("FORTINET-FORTIMANAGER-FORTIANALYZER-MIB", "fmAdomEntAnalyticsLogRetention"),
        ("FORTINET-FORTIMANAGER-FORTIANALYZER-MIB", "fmAdomEntAnalyticsLogQuota"),
        ("FORTINET-FORTIMANAGER-FORTIANALYZER-MIB", "fmAdomEntAnalyticsLogUsedSpace"),
        ("FORTINET-FORTIMANAGER-FORTIANALYZER-MIB", "fmAdomEntAnalyticsLogUsedSpacePercent"),
        ("FORTINET-FORTIMANAGER-FORTIANALYZER-MIB", "fmAdomEntLicGbDayToday"),
        ("FORTINET-FORTIMANAGER-FORTIANALYZER-MIB", "fmAdomEntLicGbDayYesterday"),
        ("FORTINET-FORTIMANAGER-FORTIANALYZER-MIB", "fmAdomEntLicGbDayWeekAvg"))
)
if mibBuilder.loadTexts:
    fmAdomComplianceGroup.setStatus("current")

fmDeviceComplianceGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 12356, 103, 10, 6)
)
fmDeviceComplianceGroup.setObjects(
      *(("FORTINET-FORTIMANAGER-FORTIANALYZER-MIB", "fmDeviceNumber"),
        ("FORTINET-FORTIMANAGER-FORTIANALYZER-MIB", "fmVdomNumber"),
        ("FORTINET-FORTIMANAGER-FORTIANALYZER-MIB", "fmDeviceEntName"),
        ("FORTINET-FORTIMANAGER-FORTIANALYZER-MIB", "fmDeviceEntSn"),
        ("FORTINET-FORTIMANAGER-FORTIANALYZER-MIB", "fmDeviceEntMode"),
        ("FORTINET-FORTIMANAGER-FORTIANALYZER-MIB", "fmDeviceEntAdom"),
        ("FORTINET-FORTIMANAGER-FORTIANALYZER-MIB", "fmDeviceEntIp"),
        ("FORTINET-FORTIMANAGER-FORTIANALYZER-MIB", "fmDeviceEntOsVersion"),
        ("FORTINET-FORTIMANAGER-FORTIANALYZER-MIB", "fmDeviceEntMr"),
        ("FORTINET-FORTIMANAGER-FORTIANALYZER-MIB", "fmDeviceEntBuild"),
        ("FORTINET-FORTIMANAGER-FORTIANALYZER-MIB", "fmDeviceEntHaMode"),
        ("FORTINET-FORTIMANAGER-FORTIANALYZER-MIB", "fmDeviceEntHaGroup"),
        ("FORTINET-FORTIMANAGER-FORTIANALYZER-MIB", "fmDeviceEntConnectState"),
        ("FORTINET-FORTIMANAGER-FORTIANALYZER-MIB", "fmDeviceEntDbState"),
        ("FORTINET-FORTIMANAGER-FORTIANALYZER-MIB", "fmDeviceEntConfigState"),
        ("FORTINET-FORTIMANAGER-FORTIANALYZER-MIB", "fmDeviceEntState"),
        ("FORTINET-FORTIMANAGER-FORTIANALYZER-MIB", "fmDeviceEntPlatform"),
        ("FORTINET-FORTIMANAGER-FORTIANALYZER-MIB", "fmDeviceEntVdomEnabled"),
        ("FORTINET-FORTIMANAGER-FORTIANALYZER-MIB", "fmDeviceEntSupportState"),
        ("FORTINET-FORTIMANAGER-FORTIANALYZER-MIB", "fmDeviceEntAvExpireDate"),
        ("FORTINET-FORTIMANAGER-FORTIANALYZER-MIB", "fmDeviceEntIpsExpireDate"),
        ("FORTINET-FORTIMANAGER-FORTIANALYZER-MIB", "fmDeviceEntWfExpireDate"),
        ("FORTINET-FORTIMANAGER-FORTIANALYZER-MIB", "fmDeviceEntAsExpireDate"),
        ("FORTINET-FORTIMANAGER-FORTIANALYZER-MIB", "fmDeviceEntPolicyPackageState"),
        ("FORTINET-FORTIMANAGER-FORTIANALYZER-MIB", "fmDeviceEntDesc"),
        ("FORTINET-FORTIMANAGER-FORTIANALYZER-MIB", "fmDeviceEntLogRateHour"),
        ("FORTINET-FORTIMANAGER-FORTIANALYZER-MIB", "fmDeviceEntLogRateDay"),
        ("FORTINET-FORTIMANAGER-FORTIANALYZER-MIB", "fmDeviceEntLogRateWeek"),
        ("FORTINET-FORTIMANAGER-FORTIANALYZER-MIB", "fmDeviceEntArchiveLogUsedSpace"))
)
if mibBuilder.loadTexts:
    fmDeviceComplianceGroup.setStatus("current")


# Notification objects

fmTrapHASwitch = NotificationType(
    (1, 3, 6, 1, 4, 1, 12356, 103, 0, 0, 401)
)
fmTrapHASwitch.setObjects(
      *(("FORTINET-CORE-MIB", "fnSysSerial"),
        ("SNMPv2-MIB", "sysName"))
)
if mibBuilder.loadTexts:
    fmTrapHASwitch.setStatus(
        "current"
    )

fmTrapRAIDStatusChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 12356, 103, 0, 0, 402)
)
fmTrapRAIDStatusChange.setObjects(
      *(("FORTINET-CORE-MIB", "fnSysSerial"),
        ("SNMPv2-MIB", "sysName"),
        ("FORTINET-FORTIMANAGER-FORTIANALYZER-MIB", "fmRAIDStatus"),
        ("FORTINET-FORTIMANAGER-FORTIANALYZER-MIB", "fmRAIDDevIndex"))
)
if mibBuilder.loadTexts:
    fmTrapRAIDStatusChange.setStatus(
        "current"
    )

fmTrapLogAlert = NotificationType(
    (1, 3, 6, 1, 4, 1, 12356, 103, 0, 0, 403)
)
fmTrapLogAlert.setObjects(
      *(("FORTINET-CORE-MIB", "fnSysSerial"),
        ("SNMPv2-MIB", "sysName"),
        ("FORTINET-CORE-MIB", "fnGenTrapMsg"))
)
if mibBuilder.loadTexts:
    fmTrapLogAlert.setStatus(
        "current"
    )

fmTrapLogRateThreshold = NotificationType(
    (1, 3, 6, 1, 4, 1, 12356, 103, 0, 0, 404)
)
fmTrapLogRateThreshold.setObjects(
      *(("FORTINET-CORE-MIB", "fnSysSerial"),
        ("SNMPv2-MIB", "sysName"),
        ("FORTINET-FORTIMANAGER-FORTIANALYZER-MIB", "fmLogRate"),
        ("FORTINET-FORTIMANAGER-FORTIANALYZER-MIB", "fmLogRateThreshold"))
)
if mibBuilder.loadTexts:
    fmTrapLogRateThreshold.setStatus(
        "current"
    )

fmTrapLogDataRateThreshold = NotificationType(
    (1, 3, 6, 1, 4, 1, 12356, 103, 0, 0, 405)
)
fmTrapLogDataRateThreshold.setObjects(
      *(("FORTINET-CORE-MIB", "fnSysSerial"),
        ("SNMPv2-MIB", "sysName"),
        ("FORTINET-FORTIMANAGER-FORTIANALYZER-MIB", "fmLogDataRate"),
        ("FORTINET-FORTIMANAGER-FORTIANALYZER-MIB", "fmLogDataRateThreshold"))
)
if mibBuilder.loadTexts:
    fmTrapLogDataRateThreshold.setStatus(
        "current"
    )

fmTrapLicGbDayThreshold = NotificationType(
    (1, 3, 6, 1, 4, 1, 12356, 103, 0, 0, 407)
)
fmTrapLicGbDayThreshold.setObjects(
      *(("FORTINET-CORE-MIB", "fnSysSerial"),
        ("SNMPv2-MIB", "sysName"),
        ("FORTINET-FORTIMANAGER-FORTIANALYZER-MIB", "fmLicGbDay"),
        ("FORTINET-FORTIMANAGER-FORTIANALYZER-MIB", "fmLicGbDayThreshold"))
)
if mibBuilder.loadTexts:
    fmTrapLicGbDayThreshold.setStatus(
        "current"
    )

fmTrapLicDevQuotaThreshold = NotificationType(
    (1, 3, 6, 1, 4, 1, 12356, 103, 0, 0, 408)
)
fmTrapLicDevQuotaThreshold.setObjects(
      *(("FORTINET-CORE-MIB", "fnSysSerial"),
        ("SNMPv2-MIB", "sysName"),
        ("FORTINET-FORTIMANAGER-FORTIANALYZER-MIB", "fmLicDevQuota"),
        ("FORTINET-FORTIMANAGER-FORTIANALYZER-MIB", "fmLicDevQuotaThreshold"))
)
if mibBuilder.loadTexts:
    fmTrapLicDevQuotaThreshold.setStatus(
        "current"
    )

fmTrapCpuThresholdExcludeNice = NotificationType(
    (1, 3, 6, 1, 4, 1, 12356, 103, 0, 0, 409)
)
fmTrapCpuThresholdExcludeNice.setObjects(
      *(("FORTINET-CORE-MIB", "fnSysSerial"),
        ("SNMPv2-MIB", "sysName"))
)
if mibBuilder.loadTexts:
    fmTrapCpuThresholdExcludeNice.setStatus(
        "current"
    )

fmTrapPowerStateChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 12356, 103, 0, 0, 410)
)
fmTrapPowerStateChange.setObjects(
      *(("FORTINET-CORE-MIB", "fnSysSerial"),
        ("SNMPv2-MIB", "sysName"),
        ("FORTINET-FORTIMANAGER-FORTIANALYZER-MIB", "fmSensorState"),
        ("FORTINET-FORTIMANAGER-FORTIANALYZER-MIB", "fmSensorName"))
)
if mibBuilder.loadTexts:
    fmTrapPowerStateChange.setStatus(
        "current"
    )

fmTrapFanStateChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 12356, 103, 0, 0, 411)
)
fmTrapFanStateChange.setObjects(
      *(("FORTINET-CORE-MIB", "fnSysSerial"),
        ("SNMPv2-MIB", "sysName"),
        ("FORTINET-FORTIMANAGER-FORTIANALYZER-MIB", "fmSensorState"),
        ("FORTINET-FORTIMANAGER-FORTIANALYZER-MIB", "fmSensorName"))
)
if mibBuilder.loadTexts:
    fmTrapFanStateChange.setStatus(
        "current"
    )

fmTrapTemperatureStateChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 12356, 103, 0, 0, 412)
)
fmTrapTemperatureStateChange.setObjects(
      *(("FORTINET-CORE-MIB", "fnSysSerial"),
        ("SNMPv2-MIB", "sysName"),
        ("FORTINET-FORTIMANAGER-FORTIANALYZER-MIB", "fmSensorState"),
        ("FORTINET-FORTIMANAGER-FORTIANALYZER-MIB", "fmSensorName"))
)
if mibBuilder.loadTexts:
    fmTrapTemperatureStateChange.setStatus(
        "current"
    )

fmTrapVoltageStateChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 12356, 103, 0, 0, 413)
)
fmTrapVoltageStateChange.setObjects(
      *(("FORTINET-CORE-MIB", "fnSysSerial"),
        ("SNMPv2-MIB", "sysName"),
        ("FORTINET-FORTIMANAGER-FORTIANALYZER-MIB", "fmSensorState"),
        ("FORTINET-FORTIMANAGER-FORTIANALYZER-MIB", "fmSensorName"))
)
if mibBuilder.loadTexts:
    fmTrapVoltageStateChange.setStatus(
        "current"
    )


# Notifications groups

fmTrapsComplianceGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 12356, 103, 10, 1)
)
fmTrapsComplianceGroup.setObjects(
      *(("FORTINET-FORTIMANAGER-FORTIANALYZER-MIB", "fmTrapHASwitch"),
        ("FORTINET-FORTIMANAGER-FORTIANALYZER-MIB", "fmTrapRAIDStatusChange"),
        ("FORTINET-FORTIMANAGER-FORTIANALYZER-MIB", "fmTrapLogAlert"),
        ("FORTINET-FORTIMANAGER-FORTIANALYZER-MIB", "fmTrapLogRateThreshold"),
        ("FORTINET-FORTIMANAGER-FORTIANALYZER-MIB", "fmTrapLogDataRateThreshold"),
        ("FORTINET-FORTIMANAGER-FORTIANALYZER-MIB", "fmTrapLicGbDayThreshold"),
        ("FORTINET-FORTIMANAGER-FORTIANALYZER-MIB", "fmTrapLicDevQuotaThreshold"),
        ("FORTINET-FORTIMANAGER-FORTIANALYZER-MIB", "fmTrapCpuThresholdExcludeNice"),
        ("FORTINET-FORTIMANAGER-FORTIANALYZER-MIB", "fmTrapPowerStateChange"),
        ("FORTINET-FORTIMANAGER-FORTIANALYZER-MIB", "fmTrapFanStateChange"),
        ("FORTINET-FORTIMANAGER-FORTIANALYZER-MIB", "fmTrapTemperatureStateChange"),
        ("FORTINET-FORTIMANAGER-FORTIANALYZER-MIB", "fmTrapVoltageStateChange"))
)
if mibBuilder.loadTexts:
    fmTrapsComplianceGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

fmMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 12356, 103, 10, 100)
)
fmMIBCompliance.setObjects(
      *(("FORTINET-FORTIMANAGER-FORTIANALYZER-MIB", "fmTrapsComplianceGroup"),
        ("FORTINET-FORTIMANAGER-FORTIANALYZER-MIB", "fmSystemObjectGroup"),
        ("FORTINET-FORTIMANAGER-FORTIANALYZER-MIB", "fmNotificationObjComplianceGroup"),
        ("FORTINET-FORTIMANAGER-FORTIANALYZER-MIB", "fmSessionComplianceGroup"),
        ("FORTINET-FORTIMANAGER-FORTIANALYZER-MIB", "fmAdomComplianceGroup"),
        ("FORTINET-FORTIMANAGER-FORTIANALYZER-MIB", "fmDeviceComplianceGroup"))
)
if mibBuilder.loadTexts:
    fmMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "FORTINET-FORTIMANAGER-FORTIANALYZER-MIB",
    **{"FmTenths": FmTenths,
       "FmHundredths": FmHundredths,
       "FmRAIDStatusCode": FmRAIDStatusCode,
       "FmSessProto": FmSessProto,
       "FmAdomEntMode": FmAdomEntMode,
       "FmAdomEntVpnMode": FmAdomEntVpnMode,
       "FmDeviceEntMode": FmDeviceEntMode,
       "FmDeviceEntHaMode": FmDeviceEntHaMode,
       "FmDeviceEntConnectState": FmDeviceEntConnectState,
       "FmDeviceEntDbState": FmDeviceEntDbState,
       "FmDeviceEntConfigState": FmDeviceEntConfigState,
       "FmDeviceEntState": FmDeviceEntState,
       "FmDeviceEntSupportState": FmDeviceEntSupportState,
       "FmRaidLevel": FmRaidLevel,
       "FmRaidState": FmRaidState,
       "FmRaidDiskEntState": FmRaidDiskEntState,
       "FmSensorEntType": FmSensorEntType,
       "FmSensorEntState": FmSensorEntState,
       "FmHaMode": FmHaMode,
       "FmHaPeerEntState": FmHaPeerEntState,
       "FmUmServiceStatus": FmUmServiceStatus,
       "FmUmBoolState": FmUmBoolState,
       "fnFortiManagerMib": fnFortiManagerMib,
       "fmTraps": fmTraps,
       "fmTrapPrefix": fmTrapPrefix,
       "fmTrapHASwitch": fmTrapHASwitch,
       "fmTrapRAIDStatusChange": fmTrapRAIDStatusChange,
       "fmTrapLogAlert": fmTrapLogAlert,
       "fmTrapLogRateThreshold": fmTrapLogRateThreshold,
       "fmTrapLogDataRateThreshold": fmTrapLogDataRateThreshold,
       "fmTrapLicGbDayThreshold": fmTrapLicGbDayThreshold,
       "fmTrapLicDevQuotaThreshold": fmTrapLicDevQuotaThreshold,
       "fmTrapCpuThresholdExcludeNice": fmTrapCpuThresholdExcludeNice,
       "fmTrapPowerStateChange": fmTrapPowerStateChange,
       "fmTrapFanStateChange": fmTrapFanStateChange,
       "fmTrapTemperatureStateChange": fmTrapTemperatureStateChange,
       "fmTrapVoltageStateChange": fmTrapVoltageStateChange,
       "fmTrapObject": fmTrapObject,
       "fmRAIDStatus": fmRAIDStatus,
       "fmRAIDDevIndex": fmRAIDDevIndex,
       "fmLogRate": fmLogRate,
       "fmLogRateThreshold": fmLogRateThreshold,
       "fmLogDataRate": fmLogDataRate,
       "fmLogDataRateThreshold": fmLogDataRateThreshold,
       "fmLicGbDay": fmLicGbDay,
       "fmLicGbDayThreshold": fmLicGbDayThreshold,
       "fmLicDevQuota": fmLicDevQuota,
       "fmLicDevQuotaThreshold": fmLicDevQuotaThreshold,
       "fmSensorState": fmSensorState,
       "fmSensorName": fmSensorName,
       "fmModel": fmModel,
       "fmgvm": fmgvm,
       "fmg100": fmg100,
       "fmg100C": fmg100C,
       "fmg200D": fmg200D,
       "fmg200E": fmg200E,
       "fmg200F": fmg200F,
       "fmg200G": fmg200G,
       "fmg300D": fmg300D,
       "fmg300E": fmg300E,
       "fmg300F": fmg300F,
       "fmg400": fmg400,
       "fmg400A": fmg400A,
       "fmg400B": fmg400B,
       "fmg400C": fmg400C,
       "fmg400E": fmg400E,
       "fmg400G": fmg400G,
       "fmg410G": fmg410G,
       "fmg1000C": fmg1000C,
       "fmg1000D": fmg1000D,
       "fmg1000F": fmg1000F,
       "fmg1000G": fmg1000G,
       "fmg2000XL": fmg2000XL,
       "fmg2000E": fmg2000E,
       "fmg3000": fmg3000,
       "fmg3000B": fmg3000B,
       "fmg3000C": fmg3000C,
       "fmg3000F": fmg3000F,
       "fmg3000G": fmg3000G,
       "fmg3100G": fmg3100G,
       "fmg3700F": fmg3700F,
       "fmg3700G": fmg3700G,
       "fmg3900E": fmg3900E,
       "fmg4000D": fmg4000D,
       "fmg4000E": fmg4000E,
       "fmg5001A": fmg5001A,
       "fmSystem": fmSystem,
       "fmSystemInfo": fmSystemInfo,
       "fmSysCpuUsage": fmSysCpuUsage,
       "fmSysMemUsed": fmSysMemUsed,
       "fmSysMemCapacity": fmSysMemCapacity,
       "fmSysDiskUsage": fmSysDiskUsage,
       "fmSysDiskCapacity": fmSysDiskCapacity,
       "fmSysCpuUsageExcludedNice": fmSysCpuUsageExcludedNice,
       "fmSysVersion": fmSysVersion,
       "fmSysUpTime": fmSysUpTime,
       "fmSysLogRate": fmSysLogRate,
       "fmSysLogRateHr": fmSysLogRateHr,
       "fmSysLogIndexingRate": fmSysLogIndexingRate,
       "fmSysLogLagTime": fmSysLogLagTime,
       "fmSysLicGbDayToday": fmSysLicGbDayToday,
       "fmSysLicGbDayYesterday": fmSysLicGbDayYesterday,
       "fmSysLicGbDayWeekAvg": fmSysLicGbDayWeekAvg,
       "fmSysDiskInfo": fmSysDiskInfo,
       "fmSysDiskNumber": fmSysDiskNumber,
       "fmSysDiskTable": fmSysDiskTable,
       "fmSysDiskEntry": fmSysDiskEntry,
       "fmSysDiskEntIndex": fmSysDiskEntIndex,
       "fmSysDiskEntName": fmSysDiskEntName,
       "fmSysDiskEntUsage": fmSysDiskEntUsage,
       "fmSysDiskEntCapacity": fmSysDiskEntCapacity,
       "fmSysDiskEntIOUtil": fmSysDiskEntIOUtil,
       "fmSysLogForwardInfo": fmSysLogForwardInfo,
       "fmSysLogForwardNumber": fmSysLogForwardNumber,
       "fmSysLogForwardTable": fmSysLogForwardTable,
       "fmSysLogForwardEntry": fmSysLogForwardEntry,
       "fmSysLogForwardIndex": fmSysLogForwardIndex,
       "fmSysLogForwardName": fmSysLogForwardName,
       "fmSysLogForwardRate": fmSysLogForwardRate,
       "faModel": faModel,
       "fazvm": fazvm,
       "faz100": faz100,
       "faz100A": faz100A,
       "faz100B": faz100B,
       "faz100C": faz100C,
       "faz150G": faz150G,
       "faz200D": faz200D,
       "faz200E": faz200E,
       "faz200F": faz200F,
       "faz300D": faz300D,
       "faz300F": faz300F,
       "faz300G": faz300G,
       "faz400": faz400,
       "faz400B": faz400B,
       "faz400C": faz400C,
       "faz400E": faz400E,
       "faz800": faz800,
       "faz800B": faz800B,
       "faz800F": faz800F,
       "faz800G": faz800G,
       "faz810G": faz810G,
       "faz1000B": faz1000B,
       "faz1000C": faz1000C,
       "faz1000D": faz1000D,
       "faz1000E": faz1000E,
       "faz1000F": faz1000F,
       "faz1000G": faz1000G,
       "faz2000": faz2000,
       "faz2000A": faz2000A,
       "faz2000B": faz2000B,
       "faz2000E": faz2000E,
       "faz3000D": faz3000D,
       "faz3000E": faz3000E,
       "faz3000F": faz3000F,
       "faz3000G": faz3000G,
       "faz3100G": faz3100G,
       "faz3500E": faz3500E,
       "faz3500F": faz3500F,
       "faz3500G": faz3500G,
       "faz3510G": faz3510G,
       "faz3700F": faz3700F,
       "faz3700G": faz3700G,
       "faz3900E": faz3900E,
       "faz4000": faz4000,
       "faz4000A": faz4000A,
       "faz4000B": faz4000B,
       "fmInetProto": fmInetProto,
       "fmInetProtoInfo": fmInetProtoInfo,
       "fmInetProtoTables": fmInetProtoTables,
       "fmIpSessTable": fmIpSessTable,
       "fmIpSessEntry": fmIpSessEntry,
       "fmIpSessIndex": fmIpSessIndex,
       "fmIpSessProto": fmIpSessProto,
       "fmIpSessFromAddr": fmIpSessFromAddr,
       "fmIpSessFromPort": fmIpSessFromPort,
       "fmIpSessToAddr": fmIpSessToAddr,
       "fmIpSessToPort": fmIpSessToPort,
       "fmIpSessExp": fmIpSessExp,
       "fmAdom": fmAdom,
       "fmAdomInfo": fmAdomInfo,
       "fmAdomEnabled": fmAdomEnabled,
       "fmAdomNumber": fmAdomNumber,
       "fmAdomMax": fmAdomMax,
       "fmAdomTable": fmAdomTable,
       "fmAdomEntry": fmAdomEntry,
       "fmAdomEntIndex": fmAdomEntIndex,
       "fmAdomEntName": fmAdomEntName,
       "fmAdomEntState": fmAdomEntState,
       "fmAdomEntMode": fmAdomEntMode,
       "fmAdomEntFgtNumber": fmAdomEntFgtNumber,
       "fmAdomEntPolicyPackageNumber": fmAdomEntPolicyPackageNumber,
       "fmAdomEntOsVersion": fmAdomEntOsVersion,
       "fmAdomEntMr": fmAdomEntMr,
       "fmAdomEntVpnMode": fmAdomEntVpnMode,
       "fmAdomEntLogRateMinute": fmAdomEntLogRateMinute,
       "fmAdomEntArchiveLogRetention": fmAdomEntArchiveLogRetention,
       "fmAdomEntArchiveLogQuota": fmAdomEntArchiveLogQuota,
       "fmAdomEntArchiveLogUsedSpace": fmAdomEntArchiveLogUsedSpace,
       "fmAdomEntArchiveLogUsedSpacePercent": fmAdomEntArchiveLogUsedSpacePercent,
       "fmAdomEntAnalyticsLogRetention": fmAdomEntAnalyticsLogRetention,
       "fmAdomEntAnalyticsLogQuota": fmAdomEntAnalyticsLogQuota,
       "fmAdomEntAnalyticsLogUsedSpace": fmAdomEntAnalyticsLogUsedSpace,
       "fmAdomEntAnalyticsLogUsedSpacePercent": fmAdomEntAnalyticsLogUsedSpacePercent,
       "fmAdomEntLicGbDayToday": fmAdomEntLicGbDayToday,
       "fmAdomEntLicGbDayYesterday": fmAdomEntLicGbDayYesterday,
       "fmAdomEntLicGbDayWeekAvg": fmAdomEntLicGbDayWeekAvg,
       "fmDevice": fmDevice,
       "fmDeviceInfo": fmDeviceInfo,
       "fmDeviceNumber": fmDeviceNumber,
       "fmVdomNumber": fmVdomNumber,
       "fmDeviceTable": fmDeviceTable,
       "fmDeviceEntry": fmDeviceEntry,
       "fmDeviceEntIndex": fmDeviceEntIndex,
       "fmDeviceEntName": fmDeviceEntName,
       "fmDeviceEntSn": fmDeviceEntSn,
       "fmDeviceEntMode": fmDeviceEntMode,
       "fmDeviceEntAdom": fmDeviceEntAdom,
       "fmDeviceEntIp": fmDeviceEntIp,
       "fmDeviceEntOsVersion": fmDeviceEntOsVersion,
       "fmDeviceEntMr": fmDeviceEntMr,
       "fmDeviceEntBuild": fmDeviceEntBuild,
       "fmDeviceEntHaMode": fmDeviceEntHaMode,
       "fmDeviceEntHaGroup": fmDeviceEntHaGroup,
       "fmDeviceEntConnectState": fmDeviceEntConnectState,
       "fmDeviceEntDbState": fmDeviceEntDbState,
       "fmDeviceEntConfigState": fmDeviceEntConfigState,
       "fmDeviceEntState": fmDeviceEntState,
       "fmDeviceEntPlatform": fmDeviceEntPlatform,
       "fmDeviceEntVdomEnabled": fmDeviceEntVdomEnabled,
       "fmDeviceEntSupportState": fmDeviceEntSupportState,
       "fmDeviceEntAvExpireDate": fmDeviceEntAvExpireDate,
       "fmDeviceEntIpsExpireDate": fmDeviceEntIpsExpireDate,
       "fmDeviceEntWfExpireDate": fmDeviceEntWfExpireDate,
       "fmDeviceEntAsExpireDate": fmDeviceEntAsExpireDate,
       "fmDeviceEntPolicyPackageState": fmDeviceEntPolicyPackageState,
       "fmDeviceEntDesc": fmDeviceEntDesc,
       "fmDeviceEntLogRateHour": fmDeviceEntLogRateHour,
       "fmDeviceEntLogRateDay": fmDeviceEntLogRateDay,
       "fmDeviceEntLogRateWeek": fmDeviceEntLogRateWeek,
       "fmDeviceEntArchiveLogUsedSpace": fmDeviceEntArchiveLogUsedSpace,
       "fmRaid": fmRaid,
       "fmRaidInfo": fmRaidInfo,
       "fmRaidLevel": fmRaidLevel,
       "fmRaidState": fmRaidState,
       "fmRaidSize": fmRaidSize,
       "fmRaidDiskNumber": fmRaidDiskNumber,
       "fmRaidDiskTable": fmRaidDiskTable,
       "fmRaidDiskEntry": fmRaidDiskEntry,
       "fmRaidDiskEntIndex": fmRaidDiskEntIndex,
       "fmRaidDiskEntState": fmRaidDiskEntState,
       "fmRaidDiskEntSize": fmRaidDiskEntSize,
       "fmSensor": fmSensor,
       "fmSensorTable": fmSensorTable,
       "fmSensorEntry": fmSensorEntry,
       "fmSensorEntIndex": fmSensorEntIndex,
       "fmSensorEntName": fmSensorEntName,
       "fmSensorEntVal": fmSensorEntVal,
       "fmSensorEntType": fmSensorEntType,
       "fmSensorEntState": fmSensorEntState,
       "fmHa": fmHa,
       "fmHaInfo": fmHaInfo,
       "fmHaMode": fmHaMode,
       "fmHaClusterId": fmHaClusterId,
       "fmHaPeerNumber": fmHaPeerNumber,
       "fmHaPeerTable": fmHaPeerTable,
       "fmHaPeerEntry": fmHaPeerEntry,
       "fmHaPeerEntIndex": fmHaPeerEntIndex,
       "fmHaPeerEntIp": fmHaPeerEntIp,
       "fmHaPeerEntSn": fmHaPeerEntSn,
       "fmHaPeerEntEnabled": fmHaPeerEntEnabled,
       "fmHaPeerEntHostName": fmHaPeerEntHostName,
       "fmHaPeerEntState": fmHaPeerEntState,
       "fmMIBConformance": fmMIBConformance,
       "fmTrapsComplianceGroup": fmTrapsComplianceGroup,
       "fmSystemObjectGroup": fmSystemObjectGroup,
       "fmNotificationObjComplianceGroup": fmNotificationObjComplianceGroup,
       "fmSessionComplianceGroup": fmSessionComplianceGroup,
       "fmAdomComplianceGroup": fmAdomComplianceGroup,
       "fmDeviceComplianceGroup": fmDeviceComplianceGroup,
       "fmMIBCompliance": fmMIBCompliance,
       "fmUm": fmUm,
       "fmUmContract": fmUmContract,
       "fmUmContractTable": fmUmContractTable,
       "fmUmContractEntry": fmUmContractEntry,
       "fmUmContractEntryIndex": fmUmContractEntryIndex,
       "fmUmContractEntrySerial": fmUmContractEntrySerial,
       "fmUmContractEntryData": fmUmContractEntryData,
       "fmUmFds": fmUmFds,
       "fmUmFdsServiceFds": fmUmFdsServiceFds,
       "fmUmFdsServiceFdsStatus": fmUmFdsServiceFdsStatus,
       "fmUmFdsServiceFdsServerTable": fmUmFdsServiceFdsServerTable,
       "fmUmFdsServiceFdsServerEntry": fmUmFdsServiceFdsServerEntry,
       "fmUmFdsServiceFdsServerEntryIndex": fmUmFdsServiceFdsServerEntryIndex,
       "fmUmFdsServiceFdsServerAddr": fmUmFdsServiceFdsServerAddr,
       "fmUmFdsServiceFdsServerPort": fmUmFdsServiceFdsServerPort,
       "fmUmFdsServiceFdsServerTimeZone": fmUmFdsServiceFdsServerTimeZone,
       "fmUmFdsServiceFdsServerCurrent": fmUmFdsServiceFdsServerCurrent,
       "fmUmFdsServiceFct": fmUmFdsServiceFct,
       "fmUmFdsServiceFctStatus": fmUmFdsServiceFctStatus,
       "fmUmFdsServiceFctServerTable": fmUmFdsServiceFctServerTable,
       "fmUmFdsServiceFctServerEntry": fmUmFdsServiceFctServerEntry,
       "fmUmFdsServiceFctServerEntryIndex": fmUmFdsServiceFctServerEntryIndex,
       "fmUmFdsServiceFctServerAddr": fmUmFdsServiceFctServerAddr,
       "fmUmFdsServiceFctServerPort": fmUmFdsServiceFctServerPort,
       "fmUmFdsServiceFctServerTimeZone": fmUmFdsServiceFctServerTimeZone,
       "fmUmFdsServiceFctServerCurrent": fmUmFdsServiceFctServerCurrent,
       "fmUmFdsPackage": fmUmFdsPackage,
       "fmUmFdsObjectTable": fmUmFdsObjectTable,
       "fmUmFdsObjectEntry": fmUmFdsObjectEntry,
       "fmUmFdsObjectEntryIndex": fmUmFdsObjectEntryIndex,
       "fmUmFdsObjectEntryObjid": fmUmFdsObjectEntryObjid,
       "fmUmFdsObjectEntryVersion": fmUmFdsObjectEntryVersion,
       "fmUmFdsObjectEntryDate": fmUmFdsObjectEntryDate,
       "fmUmFdsObjectEntrySize": fmUmFdsObjectEntrySize,
       "fmUmFdsObjectEntryDesc": fmUmFdsObjectEntryDesc,
       "fmUmFdsObjectEntryProduct": fmUmFdsObjectEntryProduct,
       "fmUmDevice": fmUmDevice,
       "fmUmDeviceStatusTable": fmUmDeviceStatusTable,
       "fmUmDeviceStatusEntry": fmUmDeviceStatusEntry,
       "fmUmDeviceStatusEntryIndex": fmUmDeviceStatusEntryIndex,
       "fmUmDeviceStatusEntrySerial": fmUmDeviceStatusEntrySerial,
       "fmUmDeviceStatusEntryStatus": fmUmDeviceStatusEntryStatus,
       "fmUmDeviceStatusEntryUpdateTime": fmUmDeviceStatusEntryUpdateTime,
       "fmUmDeviceObjectTable": fmUmDeviceObjectTable,
       "fmUmDeviceObjectEntry": fmUmDeviceObjectEntry,
       "fmUmDeviceObjectEntryIndex": fmUmDeviceObjectEntryIndex,
       "fmUmDeviceObjectEntrySerial": fmUmDeviceObjectEntrySerial,
       "fmUmDeviceObjectEntryObjid": fmUmDeviceObjectEntryObjid,
       "fmUmDeviceObjectEntryDeviceVersion": fmUmDeviceObjectEntryDeviceVersion,
       "fmUmDeviceObjectEntryServerVersion": fmUmDeviceObjectEntryServerVersion,
       "fmUmDeviceObjectEntryPreferVersion": fmUmDeviceObjectEntryPreferVersion,
       "fmUmFgd": fmUmFgd,
       "fmUmFgdServiceFgd": fmUmFgdServiceFgd,
       "fmUmFgdServiceFgdStatus": fmUmFgdServiceFgdStatus,
       "fmUmFgdServiceFgdServerTable": fmUmFgdServiceFgdServerTable,
       "fmUmFgdServiceFgdServerEntry": fmUmFgdServiceFgdServerEntry,
       "fmUmFgdServiceFgdServerEntryIndex": fmUmFgdServiceFgdServerEntryIndex,
       "fmUmFgdServiceFgdServerAddr": fmUmFgdServiceFgdServerAddr,
       "fmUmFgdServiceFgdServerPort": fmUmFgdServiceFgdServerPort,
       "fmUmFgdServiceFgdServerTimeZone": fmUmFgdServiceFgdServerTimeZone,
       "fmUmFgdServiceFgdServerCurrent": fmUmFgdServiceFgdServerCurrent,
       "fmUmFgdServiceFgfq": fmUmFgdServiceFgfq,
       "fmUmFgdServiceFgfqStatus": fmUmFgdServiceFgfqStatus,
       "fmUmFgdServiceFgfqServerTable": fmUmFgdServiceFgfqServerTable,
       "fmUmFgdServiceFgfqServerEntry": fmUmFgdServiceFgfqServerEntry,
       "fmUmFgdServiceFgfqServerEntryIndex": fmUmFgdServiceFgfqServerEntryIndex,
       "fmUmFgdServiceFgfqServerAddr": fmUmFgdServiceFgfqServerAddr,
       "fmUmFgdServiceFgfqServerPort": fmUmFgdServiceFgfqServerPort,
       "fmUmFgdServiceFgfqServerTimeZone": fmUmFgdServiceFgfqServerTimeZone,
       "fmUmFgdServiceFgfqServerCurrent": fmUmFgdServiceFgfqServerCurrent,
       "fmUmFgdPackage": fmUmFgdPackage,
       "fmUmFgdDBVersionTable": fmUmFgdDBVersionTable,
       "fmUmFgdDBVersionEntry": fmUmFgdDBVersionEntry,
       "fmUmFgdDBVersionEntryIndex": fmUmFgdDBVersionEntryIndex,
       "fmUmFgdDBVersionEntryCategory": fmUmFgdDBVersionEntryCategory,
       "fmUmFgdDBVersionEntryVersion": fmUmFgdDBVersionEntryVersion,
       "fmUmFgdDBVersionEntrySize": fmUmFgdDBVersionEntrySize,
       "fmUmFgdDBVersionEntryDate": fmUmFgdDBVersionEntryDate,
       "fmUmFgdDBVersionEntryDesc": fmUmFgdDBVersionEntryDesc,
       "fmUmFgdQueryStatistic": fmUmFgdQueryStatistic,
       "fmUmFgdQueryStatisticTop10SitesTable": fmUmFgdQueryStatisticTop10SitesTable,
       "fmUmFgdQueryStatisticTop10SitesEntry": fmUmFgdQueryStatisticTop10SitesEntry,
       "fmUmFgdQueryStatisticTop10SitesEntryIndex": fmUmFgdQueryStatisticTop10SitesEntryIndex,
       "fmUmFgdQueryStatisticTop10SitesEntryAddress": fmUmFgdQueryStatisticTop10SitesEntryAddress,
       "fmUmFgdQueryStatisticTop10SitesEntryVisits": fmUmFgdQueryStatisticTop10SitesEntryVisits,
       "fmUmFgdQueryStatisticTop10DevicesTable": fmUmFgdQueryStatisticTop10DevicesTable,
       "fmUmFgdQueryStatisticTop10DevicesEntry": fmUmFgdQueryStatisticTop10DevicesEntry,
       "fmUmFgdQueryStatisticTop10DevicesEntryIndex": fmUmFgdQueryStatisticTop10DevicesEntryIndex,
       "fmUmFgdQueryStatisticTop10DevicesEntryName": fmUmFgdQueryStatisticTop10DevicesEntryName,
       "fmUmFgdQueryStatisticTop10DevicesEntryQueries": fmUmFgdQueryStatisticTop10DevicesEntryQueries,
       "fmUmFgdQueryStatisticQueryHistoryTable": fmUmFgdQueryStatisticQueryHistoryTable,
       "fmUmFgdQueryStatisticQueryHistoryEntry": fmUmFgdQueryStatisticQueryHistoryEntry,
       "fmUmFgdQueryStatisticQueryHistoryEntryIndex": fmUmFgdQueryStatisticQueryHistoryEntryIndex,
       "fmUmFgdQueryStatisticQueryHistoryEntryBeginTime": fmUmFgdQueryStatisticQueryHistoryEntryBeginTime,
       "fmUmFgdQueryStatisticQueryHistoryEntryEndTime": fmUmFgdQueryStatisticQueryHistoryEntryEndTime,
       "fmUmFgdQueryStatisticQueryHistoryEntryDeviceName": fmUmFgdQueryStatisticQueryHistoryEntryDeviceName,
       "fmUmFgdQueryStatisticQueryHistoryEntryDeviceAddress": fmUmFgdQueryStatisticQueryHistoryEntryDeviceAddress,
       "fmUmFgdQueryStatisticQueryHistoryEntryQueries": fmUmFgdQueryStatisticQueryHistoryEntryQueries,
       "fmUmFgdQueryStatisticQueryHistoryEntryHits": fmUmFgdQueryStatisticQueryHistoryEntryHits,
       "fmUmFgdQueryStatisticQueryHistoryEntryMisses": fmUmFgdQueryStatisticQueryHistoryEntryMisses,
       "fmUmFgdQueryStatisticQueryHistoryEntryBandWidth": fmUmFgdQueryStatisticQueryHistoryEntryBandWidth}
)
