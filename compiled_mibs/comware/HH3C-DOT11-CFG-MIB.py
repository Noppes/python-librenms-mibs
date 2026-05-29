# SNMP MIB module (HH3C-DOT11-CFG-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\comware\HH3C-DOT11-CFG-MIB

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

(Hh3cDot11AuthenType,
 Hh3cDot11ChannelScopeType,
 Hh3cDot11CirMode,
 Hh3cDot11ObjectIDType,
 Hh3cDot11PreambleType,
 Hh3cDot11RadioElementIndex,
 Hh3cDot11RadioScopeType,
 Hh3cDot11RadioType,
 Hh3cDot11RadioType2,
 Hh3cDot11SSIDEncryptModeType,
 Hh3cDot11SSIDStringType,
 Hh3cDot11SecIEStatusType,
 Hh3cDot11ServicePolicyIDType,
 Hh3cDot11TruthValueCM,
 Hh3cDot11TunnelSecSchemType,
 Hh3cDot11TxPwrLevelScopeType,
 Hh3cDot11WorkMode,
 hh3cDot11,
 hh3cDot11APElementIndex) = mibBuilder.importSymbols(
    "HH3C-DOT11-REF-MIB",
    "Hh3cDot11AuthenType",
    "Hh3cDot11ChannelScopeType",
    "Hh3cDot11CirMode",
    "Hh3cDot11ObjectIDType",
    "Hh3cDot11PreambleType",
    "Hh3cDot11RadioElementIndex",
    "Hh3cDot11RadioScopeType",
    "Hh3cDot11RadioType",
    "Hh3cDot11RadioType2",
    "Hh3cDot11SSIDEncryptModeType",
    "Hh3cDot11SSIDStringType",
    "Hh3cDot11SecIEStatusType",
    "Hh3cDot11ServicePolicyIDType",
    "Hh3cDot11TruthValueCM",
    "Hh3cDot11TunnelSecSchemType",
    "Hh3cDot11TxPwrLevelScopeType",
    "Hh3cDot11WorkMode",
    "hh3cDot11",
    "hh3cDot11APElementIndex")

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

(InetAddress,) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress")

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
 MacAddress,
 PhysAddress,
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

hh3cDot11CFG = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4)
)
if mibBuilder.loadTexts:
    hh3cDot11CFG.setRevisions(
        ("2020-12-11 18:00",
         "2017-10-09 18:00",
         "2016-03-11 18:00",
         "2014-09-19 18:00",
         "2010-09-25 18:00",
         "2010-09-02 18:00",
         "2009-07-29 18:00",
         "2009-05-07 20:00",
         "2009-03-20 15:30",
         "2008-11-07 15:30",
         "2008-07-09 18:00",
         "2008-02-25 18:00",
         "2007-12-21 18:00",
         "2007-10-09 16:55",
         "2007-06-19 18:00",
         "2007-04-27 20:00",
         "2007-02-01 20:00",
         "2006-05-10 19:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Hh3cDot11GlobeConfigGroup_ObjectIdentity = ObjectIdentity
hh3cDot11GlobeConfigGroup = _Hh3cDot11GlobeConfigGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 1)
)


class _Hh3cDot11GlobalCountryCode_Type(OctetString):
    """Custom type hh3cDot11GlobalCountryCode based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 3),
    )
    fixed_length = 3


_Hh3cDot11GlobalCountryCode_Type.__name__ = "OctetString"
_Hh3cDot11GlobalCountryCode_Object = MibScalar
hh3cDot11GlobalCountryCode = _Hh3cDot11GlobalCountryCode_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 1, 1),
    _Hh3cDot11GlobalCountryCode_Type()
)
hh3cDot11GlobalCountryCode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDot11GlobalCountryCode.setStatus("current")


class _Hh3cDot11StaKeepALiveTimerIntvl_Type(Unsigned32):
    """Custom type hh3cDot11StaKeepALiveTimerIntvl based on Unsigned32"""
    defaultValue = 0


_Hh3cDot11StaKeepALiveTimerIntvl_Type.__name__ = "Unsigned32"
_Hh3cDot11StaKeepALiveTimerIntvl_Object = MibScalar
hh3cDot11StaKeepALiveTimerIntvl = _Hh3cDot11StaKeepALiveTimerIntvl_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 1, 2),
    _Hh3cDot11StaKeepALiveTimerIntvl_Type()
)
hh3cDot11StaKeepALiveTimerIntvl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDot11StaKeepALiveTimerIntvl.setStatus("current")
if mibBuilder.loadTexts:
    hh3cDot11StaKeepALiveTimerIntvl.setUnits("second")
_Hh3cDot11StaIdleTimerIntvl_Type = Integer32
_Hh3cDot11StaIdleTimerIntvl_Object = MibScalar
hh3cDot11StaIdleTimerIntvl = _Hh3cDot11StaIdleTimerIntvl_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 1, 3),
    _Hh3cDot11StaIdleTimerIntvl_Type()
)
hh3cDot11StaIdleTimerIntvl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDot11StaIdleTimerIntvl.setStatus("current")
if mibBuilder.loadTexts:
    hh3cDot11StaIdleTimerIntvl.setUnits("second")


class _Hh3cDot11BroadcastProbeReply_Type(TruthValue):
    """Custom type hh3cDot11BroadcastProbeReply based on TruthValue"""
    defaultValue = 1


_Hh3cDot11BroadcastProbeReply_Type.__name__ = "TruthValue"
_Hh3cDot11BroadcastProbeReply_Object = MibScalar
hh3cDot11BroadcastProbeReply = _Hh3cDot11BroadcastProbeReply_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 1, 4),
    _Hh3cDot11BroadcastProbeReply_Type()
)
hh3cDot11BroadcastProbeReply.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDot11BroadcastProbeReply.setStatus("current")


class _Hh3cDot11APScanMode_Type(Integer32):
    """Custom type hh3cDot11APScanMode based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("passive", 2))
    )


_Hh3cDot11APScanMode_Type.__name__ = "Integer32"
_Hh3cDot11APScanMode_Object = MibScalar
hh3cDot11APScanMode = _Hh3cDot11APScanMode_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 1, 5),
    _Hh3cDot11APScanMode_Type()
)
hh3cDot11APScanMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDot11APScanMode.setStatus("current")
_Hh3cDot11ACCtrlTunnelSecSupport_Type = Hh3cDot11TunnelSecSchemType
_Hh3cDot11ACCtrlTunnelSecSupport_Object = MibScalar
hh3cDot11ACCtrlTunnelSecSupport = _Hh3cDot11ACCtrlTunnelSecSupport_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 1, 6),
    _Hh3cDot11ACCtrlTunnelSecSupport_Type()
)
hh3cDot11ACCtrlTunnelSecSupport.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDot11ACCtrlTunnelSecSupport.setStatus("current")


class _Hh3cDot11ACDataTunnelSecSupport_Type(Hh3cDot11TunnelSecSchemType):
    """Custom type hh3cDot11ACDataTunnelSecSupport based on Hh3cDot11TunnelSecSchemType"""
    defaultValue = 1


_Hh3cDot11ACDataTunnelSecSupport_Type.__name__ = "Hh3cDot11TunnelSecSchemType"
_Hh3cDot11ACDataTunnelSecSupport_Object = MibScalar
hh3cDot11ACDataTunnelSecSupport = _Hh3cDot11ACDataTunnelSecSupport_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 1, 7),
    _Hh3cDot11ACDataTunnelSecSupport_Type()
)
hh3cDot11ACDataTunnelSecSupport.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDot11ACDataTunnelSecSupport.setStatus("current")


class _Hh3cDot11ACAutoAPSupport_Type(TruthValue):
    """Custom type hh3cDot11ACAutoAPSupport based on TruthValue"""
    defaultValue = 2


_Hh3cDot11ACAutoAPSupport_Type.__name__ = "TruthValue"
_Hh3cDot11ACAutoAPSupport_Object = MibScalar
hh3cDot11ACAutoAPSupport = _Hh3cDot11ACAutoAPSupport_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 1, 8),
    _Hh3cDot11ACAutoAPSupport_Type()
)
hh3cDot11ACAutoAPSupport.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDot11ACAutoAPSupport.setStatus("current")


class _Hh3cDot11AutoAPName_Type(OctetString):
    """Custom type hh3cDot11AutoAPName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_Hh3cDot11AutoAPName_Type.__name__ = "OctetString"
_Hh3cDot11AutoAPName_Object = MibScalar
hh3cDot11AutoAPName = _Hh3cDot11AutoAPName_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 1, 9),
    _Hh3cDot11AutoAPName_Type()
)
hh3cDot11AutoAPName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDot11AutoAPName.setStatus("current")


class _Hh3cDot11PersistentName_Type(OctetString):
    """Custom type hh3cDot11PersistentName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_Hh3cDot11PersistentName_Type.__name__ = "OctetString"
_Hh3cDot11PersistentName_Object = MibScalar
hh3cDot11PersistentName = _Hh3cDot11PersistentName_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 1, 10),
    _Hh3cDot11PersistentName_Type()
)
hh3cDot11PersistentName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDot11PersistentName.setStatus("current")
_Hh3cDot11IntfTrapThreshold_Type = Integer32
_Hh3cDot11IntfTrapThreshold_Object = MibScalar
hh3cDot11IntfTrapThreshold = _Hh3cDot11IntfTrapThreshold_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 1, 11),
    _Hh3cDot11IntfTrapThreshold_Type()
)
hh3cDot11IntfTrapThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDot11IntfTrapThreshold.setStatus("current")
if mibBuilder.loadTexts:
    hh3cDot11IntfTrapThreshold.setUnits("dbm")


class _Hh3cDot11MonitorInterval_Type(Unsigned32):
    """Custom type hh3cDot11MonitorInterval based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(5, 15),
    )


_Hh3cDot11MonitorInterval_Type.__name__ = "Unsigned32"
_Hh3cDot11MonitorInterval_Object = MibScalar
hh3cDot11MonitorInterval = _Hh3cDot11MonitorInterval_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 1, 12),
    _Hh3cDot11MonitorInterval_Type()
)
hh3cDot11MonitorInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDot11MonitorInterval.setStatus("current")
if mibBuilder.loadTexts:
    hh3cDot11MonitorInterval.setUnits("minute")


class _Hh3cDot11SampleInterval_Type(Unsigned32):
    """Custom type hh3cDot11SampleInterval based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(10, 300),
    )


_Hh3cDot11SampleInterval_Type.__name__ = "Unsigned32"
_Hh3cDot11SampleInterval_Object = MibScalar
hh3cDot11SampleInterval = _Hh3cDot11SampleInterval_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 1, 13),
    _Hh3cDot11SampleInterval_Type()
)
hh3cDot11SampleInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDot11SampleInterval.setStatus("current")
if mibBuilder.loadTexts:
    hh3cDot11SampleInterval.setUnits("second")


class _Hh3cDot11ChnlSwitChkInterval_Type(Unsigned32):
    """Custom type hh3cDot11ChnlSwitChkInterval based on Unsigned32"""
    defaultValue = 8

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(8, 180),
    )


_Hh3cDot11ChnlSwitChkInterval_Type.__name__ = "Unsigned32"
_Hh3cDot11ChnlSwitChkInterval_Object = MibScalar
hh3cDot11ChnlSwitChkInterval = _Hh3cDot11ChnlSwitChkInterval_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 1, 14),
    _Hh3cDot11ChnlSwitChkInterval_Type()
)
hh3cDot11ChnlSwitChkInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDot11ChnlSwitChkInterval.setStatus("current")
if mibBuilder.loadTexts:
    hh3cDot11ChnlSwitChkInterval.setUnits("minute")


class _Hh3cDot11APUserUplimit_Type(Unsigned32):
    """Custom type hh3cDot11APUserUplimit based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Hh3cDot11APUserUplimit_Type.__name__ = "Unsigned32"
_Hh3cDot11APUserUplimit_Object = MibScalar
hh3cDot11APUserUplimit = _Hh3cDot11APUserUplimit_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 1, 15),
    _Hh3cDot11APUserUplimit_Type()
)
hh3cDot11APUserUplimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDot11APUserUplimit.setStatus("current")


class _Hh3cDot11APL2IsolateEnable_Type(TruthValue):
    """Custom type hh3cDot11APL2IsolateEnable based on TruthValue"""
    defaultValue = 2


_Hh3cDot11APL2IsolateEnable_Type.__name__ = "TruthValue"
_Hh3cDot11APL2IsolateEnable_Object = MibScalar
hh3cDot11APL2IsolateEnable = _Hh3cDot11APL2IsolateEnable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 1, 16),
    _Hh3cDot11APL2IsolateEnable_Type()
)
hh3cDot11APL2IsolateEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDot11APL2IsolateEnable.setStatus("current")
_Hh3cDot11APBSSIDSupportNum_Type = Integer32
_Hh3cDot11APBSSIDSupportNum_Object = MibScalar
hh3cDot11APBSSIDSupportNum = _Hh3cDot11APBSSIDSupportNum_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 1, 17),
    _Hh3cDot11APBSSIDSupportNum_Type()
)
hh3cDot11APBSSIDSupportNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11APBSSIDSupportNum.setStatus("current")
_Hh3cDot11APLastUpdateStatTime_Type = DateAndTime
_Hh3cDot11APLastUpdateStatTime_Object = MibScalar
hh3cDot11APLastUpdateStatTime = _Hh3cDot11APLastUpdateStatTime_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 1, 18),
    _Hh3cDot11APLastUpdateStatTime_Type()
)
hh3cDot11APLastUpdateStatTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11APLastUpdateStatTime.setStatus("current")


class _Hh3cDot11APDoSProtectEnable_Type(TruthValue):
    """Custom type hh3cDot11APDoSProtectEnable based on TruthValue"""
    defaultValue = 2


_Hh3cDot11APDoSProtectEnable_Type.__name__ = "TruthValue"
_Hh3cDot11APDoSProtectEnable_Object = MibScalar
hh3cDot11APDoSProtectEnable = _Hh3cDot11APDoSProtectEnable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 1, 19),
    _Hh3cDot11APDoSProtectEnable_Type()
)
hh3cDot11APDoSProtectEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDot11APDoSProtectEnable.setStatus("current")


class _Hh3cDot11MaxAPPerIf_Type(Unsigned32):
    """Custom type hh3cDot11MaxAPPerIf based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Hh3cDot11MaxAPPerIf_Type.__name__ = "Unsigned32"
_Hh3cDot11MaxAPPerIf_Object = MibScalar
hh3cDot11MaxAPPerIf = _Hh3cDot11MaxAPPerIf_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 1, 20),
    _Hh3cDot11MaxAPPerIf_Type()
)
hh3cDot11MaxAPPerIf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDot11MaxAPPerIf.setStatus("current")
_Hh3cDot11SampleTimeStamp_Type = DateAndTime
_Hh3cDot11SampleTimeStamp_Object = MibScalar
hh3cDot11SampleTimeStamp = _Hh3cDot11SampleTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 1, 21),
    _Hh3cDot11SampleTimeStamp_Type()
)
hh3cDot11SampleTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11SampleTimeStamp.setStatus("current")


class _Hh3cDot11UplinkTrackId_Type(Unsigned32):
    """Custom type hh3cDot11UplinkTrackId based on Unsigned32"""
    defaultValue = 0


_Hh3cDot11UplinkTrackId_Type.__name__ = "Unsigned32"
_Hh3cDot11UplinkTrackId_Object = MibScalar
hh3cDot11UplinkTrackId = _Hh3cDot11UplinkTrackId_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 1, 22),
    _Hh3cDot11UplinkTrackId_Type()
)
hh3cDot11UplinkTrackId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDot11UplinkTrackId.setStatus("current")


class _Hh3cDot11RtCollectSwitch_Type(TruthValue):
    """Custom type hh3cDot11RtCollectSwitch based on TruthValue"""
    defaultValue = 2


_Hh3cDot11RtCollectSwitch_Type.__name__ = "TruthValue"
_Hh3cDot11RtCollectSwitch_Object = MibScalar
hh3cDot11RtCollectSwitch = _Hh3cDot11RtCollectSwitch_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 1, 23),
    _Hh3cDot11RtCollectSwitch_Type()
)
hh3cDot11RtCollectSwitch.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDot11RtCollectSwitch.setStatus("current")
_Hh3cDot11RglCollectIntvl_Type = Integer32
_Hh3cDot11RglCollectIntvl_Object = MibScalar
hh3cDot11RglCollectIntvl = _Hh3cDot11RglCollectIntvl_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 1, 24),
    _Hh3cDot11RglCollectIntvl_Type()
)
hh3cDot11RglCollectIntvl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDot11RglCollectIntvl.setStatus("current")
if mibBuilder.loadTexts:
    hh3cDot11RglCollectIntvl.setUnits("second")
_Hh3cDot11RtCollectIntvl_Type = Integer32
_Hh3cDot11RtCollectIntvl_Object = MibScalar
hh3cDot11RtCollectIntvl = _Hh3cDot11RtCollectIntvl_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 1, 25),
    _Hh3cDot11RtCollectIntvl_Type()
)
hh3cDot11RtCollectIntvl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDot11RtCollectIntvl.setStatus("current")
if mibBuilder.loadTexts:
    hh3cDot11RtCollectIntvl.setUnits("second")


class _Hh3cDot11AllAPCpuUsageThreshold_Type(Integer32):
    """Custom type hh3cDot11AllAPCpuUsageThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Hh3cDot11AllAPCpuUsageThreshold_Type.__name__ = "Integer32"
_Hh3cDot11AllAPCpuUsageThreshold_Object = MibScalar
hh3cDot11AllAPCpuUsageThreshold = _Hh3cDot11AllAPCpuUsageThreshold_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 1, 26),
    _Hh3cDot11AllAPCpuUsageThreshold_Type()
)
hh3cDot11AllAPCpuUsageThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDot11AllAPCpuUsageThreshold.setStatus("current")
if mibBuilder.loadTexts:
    hh3cDot11AllAPCpuUsageThreshold.setUnits("onepercent")


class _Hh3cDot11AllAPMemUsageThreshold_Type(Integer32):
    """Custom type hh3cDot11AllAPMemUsageThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Hh3cDot11AllAPMemUsageThreshold_Type.__name__ = "Integer32"
_Hh3cDot11AllAPMemUsageThreshold_Object = MibScalar
hh3cDot11AllAPMemUsageThreshold = _Hh3cDot11AllAPMemUsageThreshold_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 1, 27),
    _Hh3cDot11AllAPMemUsageThreshold_Type()
)
hh3cDot11AllAPMemUsageThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDot11AllAPMemUsageThreshold.setStatus("current")
if mibBuilder.loadTexts:
    hh3cDot11AllAPMemUsageThreshold.setUnits("onepercent")
_Hh3cDot11AdjIntfTrapThreshold_Type = Integer32
_Hh3cDot11AdjIntfTrapThreshold_Object = MibScalar
hh3cDot11AdjIntfTrapThreshold = _Hh3cDot11AdjIntfTrapThreshold_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 1, 28),
    _Hh3cDot11AdjIntfTrapThreshold_Type()
)
hh3cDot11AdjIntfTrapThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDot11AdjIntfTrapThreshold.setStatus("current")
if mibBuilder.loadTexts:
    hh3cDot11AdjIntfTrapThreshold.setUnits("dbm")


class _Hh3cDot11AllAPMonitorMode_Type(Integer32):
    """Custom type hh3cDot11AllAPMonitorMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("normal", 1),
          ("monitor", 2),
          ("hybrid", 3))
    )


_Hh3cDot11AllAPMonitorMode_Type.__name__ = "Integer32"
_Hh3cDot11AllAPMonitorMode_Object = MibScalar
hh3cDot11AllAPMonitorMode = _Hh3cDot11AllAPMonitorMode_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 1, 29),
    _Hh3cDot11AllAPMonitorMode_Type()
)
hh3cDot11AllAPMonitorMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDot11AllAPMonitorMode.setStatus("current")


class _Hh3cDot11GlobalApFmwUpdState_Type(Integer32):
    """Custom type hh3cDot11GlobalApFmwUpdState based on Integer32"""
    defaultValue = 1

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


_Hh3cDot11GlobalApFmwUpdState_Type.__name__ = "Integer32"
_Hh3cDot11GlobalApFmwUpdState_Object = MibScalar
hh3cDot11GlobalApFmwUpdState = _Hh3cDot11GlobalApFmwUpdState_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 1, 30),
    _Hh3cDot11GlobalApFmwUpdState_Type()
)
hh3cDot11GlobalApFmwUpdState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDot11GlobalApFmwUpdState.setStatus("current")
_Hh3cDot11ACNasIDCM_Type = OctetString
_Hh3cDot11ACNasIDCM_Object = MibScalar
hh3cDot11ACNasIDCM = _Hh3cDot11ACNasIDCM_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 1, 31),
    _Hh3cDot11ACNasIDCM_Type()
)
hh3cDot11ACNasIDCM.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDot11ACNasIDCM.setStatus("current")


class _Hh3cDot11ACRole_Type(Integer32):
    """Custom type hh3cDot11ACRole based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("normal", 1),
          ("central", 2),
          ("local", 3))
    )


_Hh3cDot11ACRole_Type.__name__ = "Integer32"
_Hh3cDot11ACRole_Object = MibScalar
hh3cDot11ACRole = _Hh3cDot11ACRole_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 1, 32),
    _Hh3cDot11ACRole_Type()
)
hh3cDot11ACRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11ACRole.setStatus("current")


class _Hh3cDot11GlobalLocalACState_Type(Integer32):
    """Custom type hh3cDot11GlobalLocalACState based on Integer32"""
    defaultValue = 2

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


_Hh3cDot11GlobalLocalACState_Type.__name__ = "Integer32"
_Hh3cDot11GlobalLocalACState_Object = MibScalar
hh3cDot11GlobalLocalACState = _Hh3cDot11GlobalLocalACState_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 1, 33),
    _Hh3cDot11GlobalLocalACState_Type()
)
hh3cDot11GlobalLocalACState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDot11GlobalLocalACState.setStatus("current")
_Hh3cDot11CentralACIPAddress_Type = IpAddress
_Hh3cDot11CentralACIPAddress_Object = MibScalar
hh3cDot11CentralACIPAddress = _Hh3cDot11CentralACIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 1, 34),
    _Hh3cDot11CentralACIPAddress_Type()
)
hh3cDot11CentralACIPAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDot11CentralACIPAddress.setStatus("current")
_Hh3cDot11CentralACIPv6Address_Type = OctetString
_Hh3cDot11CentralACIPv6Address_Object = MibScalar
hh3cDot11CentralACIPv6Address = _Hh3cDot11CentralACIPv6Address_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 1, 35),
    _Hh3cDot11CentralACIPv6Address_Type()
)
hh3cDot11CentralACIPv6Address.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDot11CentralACIPv6Address.setStatus("current")
_Hh3cDot11iMcIP_Type = IpAddress
_Hh3cDot11iMcIP_Object = MibScalar
hh3cDot11iMcIP = _Hh3cDot11iMcIP_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 1, 36),
    _Hh3cDot11iMcIP_Type()
)
hh3cDot11iMcIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDot11iMcIP.setStatus("current")
_Hh3cDot11iMcPort_Type = Integer32
_Hh3cDot11iMcPort_Object = MibScalar
hh3cDot11iMcPort = _Hh3cDot11iMcPort_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 1, 37),
    _Hh3cDot11iMcPort_Type()
)
hh3cDot11iMcPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDot11iMcPort.setStatus("current")


class _Hh3cDot11APProvisionSave_Type(OctetString):
    """Custom type hh3cDot11APProvisionSave based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_Hh3cDot11APProvisionSave_Type.__name__ = "OctetString"
_Hh3cDot11APProvisionSave_Object = MibScalar
hh3cDot11APProvisionSave = _Hh3cDot11APProvisionSave_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 1, 38),
    _Hh3cDot11APProvisionSave_Type()
)
hh3cDot11APProvisionSave.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDot11APProvisionSave.setStatus("current")


class _Hh3cDot11ApRenameCurrentName_Type(OctetString):
    """Custom type hh3cDot11ApRenameCurrentName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_Hh3cDot11ApRenameCurrentName_Type.__name__ = "OctetString"
_Hh3cDot11ApRenameCurrentName_Object = MibScalar
hh3cDot11ApRenameCurrentName = _Hh3cDot11ApRenameCurrentName_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 1, 39),
    _Hh3cDot11ApRenameCurrentName_Type()
)
hh3cDot11ApRenameCurrentName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDot11ApRenameCurrentName.setStatus("current")


class _Hh3cDot11ApRenameNewName_Type(OctetString):
    """Custom type hh3cDot11ApRenameNewName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_Hh3cDot11ApRenameNewName_Type.__name__ = "OctetString"
_Hh3cDot11ApRenameNewName_Object = MibScalar
hh3cDot11ApRenameNewName = _Hh3cDot11ApRenameNewName_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 1, 40),
    _Hh3cDot11ApRenameNewName_Type()
)
hh3cDot11ApRenameNewName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDot11ApRenameNewName.setStatus("current")
_Hh3cDot11ACDescription_Type = OctetString
_Hh3cDot11ACDescription_Object = MibScalar
hh3cDot11ACDescription = _Hh3cDot11ACDescription_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 1, 41),
    _Hh3cDot11ACDescription_Type()
)
hh3cDot11ACDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDot11ACDescription.setStatus("current")
_Hh3cDot11PolicyConfigGroup_ObjectIdentity = ObjectIdentity
hh3cDot11PolicyConfigGroup = _Hh3cDot11PolicyConfigGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 2)
)
_Hh3cDot11RadioPolicyTable_Object = MibTable
hh3cDot11RadioPolicyTable = _Hh3cDot11RadioPolicyTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 2, 1)
)
if mibBuilder.loadTexts:
    hh3cDot11RadioPolicyTable.setStatus("current")
_Hh3cDot11RadioPolicyEntry_Object = MibTableRow
hh3cDot11RadioPolicyEntry = _Hh3cDot11RadioPolicyEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 2, 1, 1)
)
hh3cDot11RadioPolicyEntry.setIndexNames(
    (1, "HH3C-DOT11-CFG-MIB", "hh3cDot11RadioPolicyName"),
)
if mibBuilder.loadTexts:
    hh3cDot11RadioPolicyEntry.setStatus("current")


class _Hh3cDot11RadioPolicyName_Type(OctetString):
    """Custom type hh3cDot11RadioPolicyName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_Hh3cDot11RadioPolicyName_Type.__name__ = "OctetString"
_Hh3cDot11RadioPolicyName_Object = MibTableColumn
hh3cDot11RadioPolicyName = _Hh3cDot11RadioPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 2, 1, 1, 1),
    _Hh3cDot11RadioPolicyName_Type()
)
hh3cDot11RadioPolicyName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cDot11RadioPolicyName.setStatus("current")


class _Hh3cDot11BeaconInterval_Type(Integer32):
    """Custom type hh3cDot11BeaconInterval based on Integer32"""
    defaultValue = 100


_Hh3cDot11BeaconInterval_Type.__name__ = "Integer32"
_Hh3cDot11BeaconInterval_Object = MibTableColumn
hh3cDot11BeaconInterval = _Hh3cDot11BeaconInterval_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 2, 1, 1, 2),
    _Hh3cDot11BeaconInterval_Type()
)
hh3cDot11BeaconInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cDot11BeaconInterval.setStatus("current")
if mibBuilder.loadTexts:
    hh3cDot11BeaconInterval.setUnits("TU")


class _Hh3cDot11DtimInterval_Type(Integer32):
    """Custom type hh3cDot11DtimInterval based on Integer32"""
    defaultValue = 1


_Hh3cDot11DtimInterval_Type.__name__ = "Integer32"
_Hh3cDot11DtimInterval_Object = MibTableColumn
hh3cDot11DtimInterval = _Hh3cDot11DtimInterval_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 2, 1, 1, 3),
    _Hh3cDot11DtimInterval_Type()
)
hh3cDot11DtimInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cDot11DtimInterval.setStatus("current")


class _Hh3cDot11RtsThreshold_Type(Integer32):
    """Custom type hh3cDot11RtsThreshold based on Integer32"""
    defaultValue = 2346


_Hh3cDot11RtsThreshold_Type.__name__ = "Integer32"
_Hh3cDot11RtsThreshold_Object = MibTableColumn
hh3cDot11RtsThreshold = _Hh3cDot11RtsThreshold_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 2, 1, 1, 4),
    _Hh3cDot11RtsThreshold_Type()
)
hh3cDot11RtsThreshold.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cDot11RtsThreshold.setStatus("current")
if mibBuilder.loadTexts:
    hh3cDot11RtsThreshold.setUnits("byte")


class _Hh3cDot11FragThreshold_Type(Integer32):
    """Custom type hh3cDot11FragThreshold based on Integer32"""
    defaultValue = 2346


_Hh3cDot11FragThreshold_Type.__name__ = "Integer32"
_Hh3cDot11FragThreshold_Object = MibTableColumn
hh3cDot11FragThreshold = _Hh3cDot11FragThreshold_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 2, 1, 1, 5),
    _Hh3cDot11FragThreshold_Type()
)
hh3cDot11FragThreshold.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cDot11FragThreshold.setStatus("current")
if mibBuilder.loadTexts:
    hh3cDot11FragThreshold.setUnits("byte")


class _Hh3cDot11ShortRetryThreshold_Type(Integer32):
    """Custom type hh3cDot11ShortRetryThreshold based on Integer32"""
    defaultValue = 7


_Hh3cDot11ShortRetryThreshold_Type.__name__ = "Integer32"
_Hh3cDot11ShortRetryThreshold_Object = MibTableColumn
hh3cDot11ShortRetryThreshold = _Hh3cDot11ShortRetryThreshold_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 2, 1, 1, 6),
    _Hh3cDot11ShortRetryThreshold_Type()
)
hh3cDot11ShortRetryThreshold.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cDot11ShortRetryThreshold.setStatus("current")


class _Hh3cDot11LongRetryThreshold_Type(Integer32):
    """Custom type hh3cDot11LongRetryThreshold based on Integer32"""
    defaultValue = 4


_Hh3cDot11LongRetryThreshold_Type.__name__ = "Integer32"
_Hh3cDot11LongRetryThreshold_Object = MibTableColumn
hh3cDot11LongRetryThreshold = _Hh3cDot11LongRetryThreshold_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 2, 1, 1, 7),
    _Hh3cDot11LongRetryThreshold_Type()
)
hh3cDot11LongRetryThreshold.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cDot11LongRetryThreshold.setStatus("current")


class _Hh3cDot11MaxRxLifetime_Type(Unsigned32):
    """Custom type hh3cDot11MaxRxLifetime based on Unsigned32"""
    defaultValue = 2000


_Hh3cDot11MaxRxLifetime_Type.__name__ = "Unsigned32"
_Hh3cDot11MaxRxLifetime_Object = MibTableColumn
hh3cDot11MaxRxLifetime = _Hh3cDot11MaxRxLifetime_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 2, 1, 1, 8),
    _Hh3cDot11MaxRxLifetime_Type()
)
hh3cDot11MaxRxLifetime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cDot11MaxRxLifetime.setStatus("current")
if mibBuilder.loadTexts:
    hh3cDot11MaxRxLifetime.setUnits("millisecond")
_Hh3cDot11RdoPolicyRowStatus_Type = RowStatus
_Hh3cDot11RdoPolicyRowStatus_Object = MibTableColumn
hh3cDot11RdoPolicyRowStatus = _Hh3cDot11RdoPolicyRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 2, 1, 1, 9),
    _Hh3cDot11RdoPolicyRowStatus_Type()
)
hh3cDot11RdoPolicyRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cDot11RdoPolicyRowStatus.setStatus("current")


class _Hh3cDot11RdoClientMaxCount_Type(Integer32):
    """Custom type hh3cDot11RdoClientMaxCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_Hh3cDot11RdoClientMaxCount_Type.__name__ = "Integer32"
_Hh3cDot11RdoClientMaxCount_Object = MibTableColumn
hh3cDot11RdoClientMaxCount = _Hh3cDot11RdoClientMaxCount_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 2, 1, 1, 10),
    _Hh3cDot11RdoClientMaxCount_Type()
)
hh3cDot11RdoClientMaxCount.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cDot11RdoClientMaxCount.setStatus("current")
_Hh3cDot11BeaconIntervalMs_Type = Integer32
_Hh3cDot11BeaconIntervalMs_Object = MibTableColumn
hh3cDot11BeaconIntervalMs = _Hh3cDot11BeaconIntervalMs_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 2, 1, 1, 11),
    _Hh3cDot11BeaconIntervalMs_Type()
)
hh3cDot11BeaconIntervalMs.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cDot11BeaconIntervalMs.setStatus("current")
if mibBuilder.loadTexts:
    hh3cDot11BeaconIntervalMs.setUnits("ms")
_Hh3cDot11ServicePolicyTable_Object = MibTable
hh3cDot11ServicePolicyTable = _Hh3cDot11ServicePolicyTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 2, 2)
)
if mibBuilder.loadTexts:
    hh3cDot11ServicePolicyTable.setStatus("current")
_Hh3cDot11ServicePolicyEntry_Object = MibTableRow
hh3cDot11ServicePolicyEntry = _Hh3cDot11ServicePolicyEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 2, 2, 1)
)
hh3cDot11ServicePolicyEntry.setIndexNames(
    (0, "HH3C-DOT11-CFG-MIB", "hh3cDot11ServicePolicyID"),
)
if mibBuilder.loadTexts:
    hh3cDot11ServicePolicyEntry.setStatus("current")
_Hh3cDot11ServicePolicyID_Type = Hh3cDot11ServicePolicyIDType
_Hh3cDot11ServicePolicyID_Object = MibTableColumn
hh3cDot11ServicePolicyID = _Hh3cDot11ServicePolicyID_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 2, 2, 1, 1),
    _Hh3cDot11ServicePolicyID_Type()
)
hh3cDot11ServicePolicyID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cDot11ServicePolicyID.setStatus("current")
_Hh3cDot11SSIDName_Type = Hh3cDot11SSIDStringType
_Hh3cDot11SSIDName_Object = MibTableColumn
hh3cDot11SSIDName = _Hh3cDot11SSIDName_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 2, 2, 1, 2),
    _Hh3cDot11SSIDName_Type()
)
hh3cDot11SSIDName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cDot11SSIDName.setStatus("current")


class _Hh3cDot11SSIDHidden_Type(TruthValue):
    """Custom type hh3cDot11SSIDHidden based on TruthValue"""
    defaultValue = 2


_Hh3cDot11SSIDHidden_Type.__name__ = "TruthValue"
_Hh3cDot11SSIDHidden_Object = MibTableColumn
hh3cDot11SSIDHidden = _Hh3cDot11SSIDHidden_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 2, 2, 1, 3),
    _Hh3cDot11SSIDHidden_Type()
)
hh3cDot11SSIDHidden.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cDot11SSIDHidden.setStatus("current")
_Hh3cDot11AuthenMode_Type = Hh3cDot11AuthenType
_Hh3cDot11AuthenMode_Object = MibTableColumn
hh3cDot11AuthenMode = _Hh3cDot11AuthenMode_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 2, 2, 1, 4),
    _Hh3cDot11AuthenMode_Type()
)
hh3cDot11AuthenMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cDot11AuthenMode.setStatus("current")
_Hh3cDot11SSIDEncryptionMode_Type = Hh3cDot11SSIDEncryptModeType
_Hh3cDot11SSIDEncryptionMode_Object = MibTableColumn
hh3cDot11SSIDEncryptionMode = _Hh3cDot11SSIDEncryptionMode_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 2, 2, 1, 5),
    _Hh3cDot11SSIDEncryptionMode_Type()
)
hh3cDot11SSIDEncryptionMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cDot11SSIDEncryptionMode.setStatus("current")


class _Hh3cDot11WlanInfBindingType_Type(OctetString):
    """Custom type hh3cDot11WlanInfBindingType based on OctetString"""
    defaultValue = OctetString("WLAN-ESS")


_Hh3cDot11WlanInfBindingType_Type.__name__ = "OctetString"
_Hh3cDot11WlanInfBindingType_Object = MibTableColumn
hh3cDot11WlanInfBindingType = _Hh3cDot11WlanInfBindingType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 2, 2, 1, 6),
    _Hh3cDot11WlanInfBindingType_Type()
)
hh3cDot11WlanInfBindingType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cDot11WlanInfBindingType.setStatus("current")
_Hh3cDot11WlanInfBindingID_Type = Integer32
_Hh3cDot11WlanInfBindingID_Object = MibTableColumn
hh3cDot11WlanInfBindingID = _Hh3cDot11WlanInfBindingID_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 2, 2, 1, 7),
    _Hh3cDot11WlanInfBindingID_Type()
)
hh3cDot11WlanInfBindingID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cDot11WlanInfBindingID.setStatus("current")
_Hh3cDot11SrvPolicyRowStatus_Type = RowStatus
_Hh3cDot11SrvPolicyRowStatus_Object = MibTableColumn
hh3cDot11SrvPolicyRowStatus = _Hh3cDot11SrvPolicyRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 2, 2, 1, 8),
    _Hh3cDot11SrvPolicyRowStatus_Type()
)
hh3cDot11SrvPolicyRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cDot11SrvPolicyRowStatus.setStatus("current")


class _Hh3cDot11ClientMaxCount_Type(Integer32):
    """Custom type hh3cDot11ClientMaxCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_Hh3cDot11ClientMaxCount_Type.__name__ = "Integer32"
_Hh3cDot11ClientMaxCount_Object = MibTableColumn
hh3cDot11ClientMaxCount = _Hh3cDot11ClientMaxCount_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 2, 2, 1, 9),
    _Hh3cDot11ClientMaxCount_Type()
)
hh3cDot11ClientMaxCount.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cDot11ClientMaxCount.setStatus("current")


class _Hh3cDot11SPInCirMode_Type(Hh3cDot11CirMode):
    """Custom type hh3cDot11SPInCirMode based on Hh3cDot11CirMode"""
    defaultValue = 1


_Hh3cDot11SPInCirMode_Type.__name__ = "Hh3cDot11CirMode"
_Hh3cDot11SPInCirMode_Object = MibTableColumn
hh3cDot11SPInCirMode = _Hh3cDot11SPInCirMode_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 2, 2, 1, 10),
    _Hh3cDot11SPInCirMode_Type()
)
hh3cDot11SPInCirMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cDot11SPInCirMode.setStatus("current")


class _Hh3cDot11SPInCirValue_Type(Integer32):
    """Custom type hh3cDot11SPInCirValue based on Integer32"""
    defaultValue = 0


_Hh3cDot11SPInCirValue_Type.__name__ = "Integer32"
_Hh3cDot11SPInCirValue_Object = MibTableColumn
hh3cDot11SPInCirValue = _Hh3cDot11SPInCirValue_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 2, 2, 1, 11),
    _Hh3cDot11SPInCirValue_Type()
)
hh3cDot11SPInCirValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cDot11SPInCirValue.setStatus("current")
if mibBuilder.loadTexts:
    hh3cDot11SPInCirValue.setUnits("Kbps")


class _Hh3cDot11SPOutCirMode_Type(Hh3cDot11CirMode):
    """Custom type hh3cDot11SPOutCirMode based on Hh3cDot11CirMode"""
    defaultValue = 1


_Hh3cDot11SPOutCirMode_Type.__name__ = "Hh3cDot11CirMode"
_Hh3cDot11SPOutCirMode_Object = MibTableColumn
hh3cDot11SPOutCirMode = _Hh3cDot11SPOutCirMode_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 2, 2, 1, 12),
    _Hh3cDot11SPOutCirMode_Type()
)
hh3cDot11SPOutCirMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cDot11SPOutCirMode.setStatus("current")


class _Hh3cDot11SPOutCirValue_Type(Integer32):
    """Custom type hh3cDot11SPOutCirValue based on Integer32"""
    defaultValue = 0


_Hh3cDot11SPOutCirValue_Type.__name__ = "Integer32"
_Hh3cDot11SPOutCirValue_Object = MibTableColumn
hh3cDot11SPOutCirValue = _Hh3cDot11SPOutCirValue_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 2, 2, 1, 13),
    _Hh3cDot11SPOutCirValue_Type()
)
hh3cDot11SPOutCirValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cDot11SPOutCirValue.setStatus("current")
if mibBuilder.loadTexts:
    hh3cDot11SPOutCirValue.setUnits("Kbps")


class _Hh3cDot11WlanInfPVID_Type(Integer32):
    """Custom type hh3cDot11WlanInfPVID based on Integer32"""
    defaultValue = 1


_Hh3cDot11WlanInfPVID_Type.__name__ = "Integer32"
_Hh3cDot11WlanInfPVID_Object = MibTableColumn
hh3cDot11WlanInfPVID = _Hh3cDot11WlanInfPVID_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 2, 2, 1, 14),
    _Hh3cDot11WlanInfPVID_Type()
)
hh3cDot11WlanInfPVID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cDot11WlanInfPVID.setStatus("current")


class _Hh3cDot11SPInCirStaticValue_Type(Integer32):
    """Custom type hh3cDot11SPInCirStaticValue based on Integer32"""
    defaultValue = 0


_Hh3cDot11SPInCirStaticValue_Type.__name__ = "Integer32"
_Hh3cDot11SPInCirStaticValue_Object = MibTableColumn
hh3cDot11SPInCirStaticValue = _Hh3cDot11SPInCirStaticValue_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 2, 2, 1, 15),
    _Hh3cDot11SPInCirStaticValue_Type()
)
hh3cDot11SPInCirStaticValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cDot11SPInCirStaticValue.setStatus("current")
if mibBuilder.loadTexts:
    hh3cDot11SPInCirStaticValue.setUnits("Kbps")


class _Hh3cDot11SPOutCirStaticValue_Type(Integer32):
    """Custom type hh3cDot11SPOutCirStaticValue based on Integer32"""
    defaultValue = 0


_Hh3cDot11SPOutCirStaticValue_Type.__name__ = "Integer32"
_Hh3cDot11SPOutCirStaticValue_Object = MibTableColumn
hh3cDot11SPOutCirStaticValue = _Hh3cDot11SPOutCirStaticValue_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 2, 2, 1, 16),
    _Hh3cDot11SPOutCirStaticValue_Type()
)
hh3cDot11SPOutCirStaticValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cDot11SPOutCirStaticValue.setStatus("current")
if mibBuilder.loadTexts:
    hh3cDot11SPOutCirStaticValue.setUnits("Kbps")


class _Hh3cDot11SPIsolate_Type(TruthValue):
    """Custom type hh3cDot11SPIsolate based on TruthValue"""
    defaultValue = 2


_Hh3cDot11SPIsolate_Type.__name__ = "TruthValue"
_Hh3cDot11SPIsolate_Object = MibTableColumn
hh3cDot11SPIsolate = _Hh3cDot11SPIsolate_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 2, 2, 1, 17),
    _Hh3cDot11SPIsolate_Type()
)
hh3cDot11SPIsolate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cDot11SPIsolate.setStatus("current")
_Hh3cDot11WlanexAuthServerIP_Type = IpAddress
_Hh3cDot11WlanexAuthServerIP_Object = MibTableColumn
hh3cDot11WlanexAuthServerIP = _Hh3cDot11WlanexAuthServerIP_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 2, 2, 1, 18),
    _Hh3cDot11WlanexAuthServerIP_Type()
)
hh3cDot11WlanexAuthServerIP.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cDot11WlanexAuthServerIP.setStatus("current")


class _Hh3cDot11SPBeaconMeasEnable_Type(TruthValue):
    """Custom type hh3cDot11SPBeaconMeasEnable based on TruthValue"""
    defaultValue = 2


_Hh3cDot11SPBeaconMeasEnable_Type.__name__ = "TruthValue"
_Hh3cDot11SPBeaconMeasEnable_Object = MibTableColumn
hh3cDot11SPBeaconMeasEnable = _Hh3cDot11SPBeaconMeasEnable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 2, 2, 1, 19),
    _Hh3cDot11SPBeaconMeasEnable_Type()
)
hh3cDot11SPBeaconMeasEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cDot11SPBeaconMeasEnable.setStatus("current")


class _Hh3cDot11SPBeaconMeasType_Type(Integer32):
    """Custom type hh3cDot11SPBeaconMeasType based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("passive", 1),
          ("active", 2),
          ("beaconTable", 3))
    )


_Hh3cDot11SPBeaconMeasType_Type.__name__ = "Integer32"
_Hh3cDot11SPBeaconMeasType_Object = MibTableColumn
hh3cDot11SPBeaconMeasType = _Hh3cDot11SPBeaconMeasType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 2, 2, 1, 20),
    _Hh3cDot11SPBeaconMeasType_Type()
)
hh3cDot11SPBeaconMeasType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cDot11SPBeaconMeasType.setStatus("current")


class _Hh3cDot11SPBeaconMeasInterval_Type(Integer32):
    """Custom type hh3cDot11SPBeaconMeasInterval based on Integer32"""
    defaultValue = 60

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 200),
    )


_Hh3cDot11SPBeaconMeasInterval_Type.__name__ = "Integer32"
_Hh3cDot11SPBeaconMeasInterval_Object = MibTableColumn
hh3cDot11SPBeaconMeasInterval = _Hh3cDot11SPBeaconMeasInterval_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 2, 2, 1, 21),
    _Hh3cDot11SPBeaconMeasInterval_Type()
)
hh3cDot11SPBeaconMeasInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cDot11SPBeaconMeasInterval.setStatus("current")
if mibBuilder.loadTexts:
    hh3cDot11SPBeaconMeasInterval.setUnits("second")


class _Hh3cDot11AuthenModeCM_Type(Integer32):
    """Custom type hh3cDot11AuthenModeCM based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("opensystem", 0),
          ("sharedkey", 1))
    )


_Hh3cDot11AuthenModeCM_Type.__name__ = "Integer32"
_Hh3cDot11AuthenModeCM_Object = MibTableColumn
hh3cDot11AuthenModeCM = _Hh3cDot11AuthenModeCM_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 2, 2, 1, 22),
    _Hh3cDot11AuthenModeCM_Type()
)
hh3cDot11AuthenModeCM.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cDot11AuthenModeCM.setStatus("current")


class _Hh3cDot11SecIEStatusCM_Type(Integer32):
    """Custom type hh3cDot11SecIEStatusCM based on Integer32"""
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
        *(("none", 0),
          ("wpa", 1),
          ("wpa2", 2),
          ("wlanex", 3))
    )


_Hh3cDot11SecIEStatusCM_Type.__name__ = "Integer32"
_Hh3cDot11SecIEStatusCM_Object = MibTableColumn
hh3cDot11SecIEStatusCM = _Hh3cDot11SecIEStatusCM_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 2, 2, 1, 23),
    _Hh3cDot11SecIEStatusCM_Type()
)
hh3cDot11SecIEStatusCM.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cDot11SecIEStatusCM.setStatus("current")


class _Hh3cDot11SecurityCiphersCM_Type(Integer32):
    """Custom type hh3cDot11SecurityCiphersCM based on Integer32"""
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
        *(("none", 0),
          ("wep40", 1),
          ("wep104", 2),
          ("tkip", 3),
          ("aesccmp", 4),
          ("wpisms4", 5))
    )


_Hh3cDot11SecurityCiphersCM_Type.__name__ = "Integer32"
_Hh3cDot11SecurityCiphersCM_Object = MibTableColumn
hh3cDot11SecurityCiphersCM = _Hh3cDot11SecurityCiphersCM_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 2, 2, 1, 24),
    _Hh3cDot11SecurityCiphersCM_Type()
)
hh3cDot11SecurityCiphersCM.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cDot11SecurityCiphersCM.setStatus("current")


class _Hh3cDot11SrvPolicyStatusCM_Type(Integer32):
    """Custom type hh3cDot11SrvPolicyStatusCM based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_Hh3cDot11SrvPolicyStatusCM_Type.__name__ = "Integer32"
_Hh3cDot11SrvPolicyStatusCM_Object = MibTableColumn
hh3cDot11SrvPolicyStatusCM = _Hh3cDot11SrvPolicyStatusCM_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 2, 2, 1, 25),
    _Hh3cDot11SrvPolicyStatusCM_Type()
)
hh3cDot11SrvPolicyStatusCM.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cDot11SrvPolicyStatusCM.setStatus("current")


class _Hh3cDot11SSIDHiddenCM_Type(Hh3cDot11TruthValueCM):
    """Custom type hh3cDot11SSIDHiddenCM based on Hh3cDot11TruthValueCM"""
    defaultValue = 0


_Hh3cDot11SSIDHiddenCM_Type.__name__ = "Hh3cDot11TruthValueCM"
_Hh3cDot11SSIDHiddenCM_Object = MibTableColumn
hh3cDot11SSIDHiddenCM = _Hh3cDot11SSIDHiddenCM_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 2, 2, 1, 26),
    _Hh3cDot11SSIDHiddenCM_Type()
)
hh3cDot11SSIDHiddenCM.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cDot11SSIDHiddenCM.setStatus("current")


class _Hh3cDot11SPIsolateCM_Type(Hh3cDot11TruthValueCM):
    """Custom type hh3cDot11SPIsolateCM based on Hh3cDot11TruthValueCM"""
    defaultValue = 0


_Hh3cDot11SPIsolateCM_Type.__name__ = "Hh3cDot11TruthValueCM"
_Hh3cDot11SPIsolateCM_Object = MibTableColumn
hh3cDot11SPIsolateCM = _Hh3cDot11SPIsolateCM_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 2, 2, 1, 27),
    _Hh3cDot11SPIsolateCM_Type()
)
hh3cDot11SPIsolateCM.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cDot11SPIsolateCM.setStatus("current")


class _Hh3cDot11FwdVlanBitMapLow_Type(OctetString):
    """Custom type hh3cDot11FwdVlanBitMapLow based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_Hh3cDot11FwdVlanBitMapLow_Type.__name__ = "OctetString"
_Hh3cDot11FwdVlanBitMapLow_Object = MibTableColumn
hh3cDot11FwdVlanBitMapLow = _Hh3cDot11FwdVlanBitMapLow_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 2, 2, 1, 28),
    _Hh3cDot11FwdVlanBitMapLow_Type()
)
hh3cDot11FwdVlanBitMapLow.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cDot11FwdVlanBitMapLow.setStatus("current")


class _Hh3cDot11FwdVlanBitMapHigh_Type(OctetString):
    """Custom type hh3cDot11FwdVlanBitMapHigh based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_Hh3cDot11FwdVlanBitMapHigh_Type.__name__ = "OctetString"
_Hh3cDot11FwdVlanBitMapHigh_Object = MibTableColumn
hh3cDot11FwdVlanBitMapHigh = _Hh3cDot11FwdVlanBitMapHigh_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 2, 2, 1, 29),
    _Hh3cDot11FwdVlanBitMapHigh_Type()
)
hh3cDot11FwdVlanBitMapHigh.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cDot11FwdVlanBitMapHigh.setStatus("current")
_Hh3cDot11ServicePolicyName_Type = OctetString
_Hh3cDot11ServicePolicyName_Object = MibTableColumn
hh3cDot11ServicePolicyName = _Hh3cDot11ServicePolicyName_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 2, 2, 1, 30),
    _Hh3cDot11ServicePolicyName_Type()
)
hh3cDot11ServicePolicyName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cDot11ServicePolicyName.setStatus("current")


class _Hh3cDot11SecurityModeCM_Type(Integer32):
    """Custom type hh3cDot11SecurityModeCM based on Integer32"""
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
        *(("none", 0),
          ("psk", 1),
          ("radius", 2),
          ("wlanex", 3))
    )


_Hh3cDot11SecurityModeCM_Type.__name__ = "Integer32"
_Hh3cDot11SecurityModeCM_Object = MibTableColumn
hh3cDot11SecurityModeCM = _Hh3cDot11SecurityModeCM_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 2, 2, 1, 31),
    _Hh3cDot11SecurityModeCM_Type()
)
hh3cDot11SecurityModeCM.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDot11SecurityModeCM.setStatus("current")


class _Hh3cDot11SPInCbsValue_Type(Integer32):
    """Custom type hh3cDot11SPInCbsValue based on Integer32"""
    defaultValue = 0


_Hh3cDot11SPInCbsValue_Type.__name__ = "Integer32"
_Hh3cDot11SPInCbsValue_Object = MibTableColumn
hh3cDot11SPInCbsValue = _Hh3cDot11SPInCbsValue_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 2, 2, 1, 32),
    _Hh3cDot11SPInCbsValue_Type()
)
hh3cDot11SPInCbsValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cDot11SPInCbsValue.setStatus("current")
if mibBuilder.loadTexts:
    hh3cDot11SPInCbsValue.setUnits("byte")


class _Hh3cDot11SPOutCbsValue_Type(Integer32):
    """Custom type hh3cDot11SPOutCbsValue based on Integer32"""
    defaultValue = 0


_Hh3cDot11SPOutCbsValue_Type.__name__ = "Integer32"
_Hh3cDot11SPOutCbsValue_Object = MibTableColumn
hh3cDot11SPOutCbsValue = _Hh3cDot11SPOutCbsValue_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 2, 2, 1, 33),
    _Hh3cDot11SPOutCbsValue_Type()
)
hh3cDot11SPOutCbsValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cDot11SPOutCbsValue.setStatus("current")
if mibBuilder.loadTexts:
    hh3cDot11SPOutCbsValue.setUnits("byte")
_Hh3cDot11WlanInfCustomerPVID_Type = Integer32
_Hh3cDot11WlanInfCustomerPVID_Object = MibTableColumn
hh3cDot11WlanInfCustomerPVID = _Hh3cDot11WlanInfCustomerPVID_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 2, 2, 1, 34),
    _Hh3cDot11WlanInfCustomerPVID_Type()
)
hh3cDot11WlanInfCustomerPVID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cDot11WlanInfCustomerPVID.setStatus("current")
_Hh3cDot11ServicePolicyExtTable_Object = MibTable
hh3cDot11ServicePolicyExtTable = _Hh3cDot11ServicePolicyExtTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 2, 3)
)
if mibBuilder.loadTexts:
    hh3cDot11ServicePolicyExtTable.setStatus("current")
_Hh3cDot11ServicePolicyExtEntry_Object = MibTableRow
hh3cDot11ServicePolicyExtEntry = _Hh3cDot11ServicePolicyExtEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 2, 3, 1)
)
hh3cDot11ServicePolicyExtEntry.setIndexNames(
    (0, "HH3C-DOT11-CFG-MIB", "hh3cDot11ServicePolicyExtID"),
)
if mibBuilder.loadTexts:
    hh3cDot11ServicePolicyExtEntry.setStatus("current")
_Hh3cDot11ServicePolicyExtID_Type = Hh3cDot11ServicePolicyIDType
_Hh3cDot11ServicePolicyExtID_Object = MibTableColumn
hh3cDot11ServicePolicyExtID = _Hh3cDot11ServicePolicyExtID_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 2, 3, 1, 1),
    _Hh3cDot11ServicePolicyExtID_Type()
)
hh3cDot11ServicePolicyExtID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cDot11ServicePolicyExtID.setStatus("current")
_Hh3cDot11SecIEStatus_Type = Hh3cDot11SecIEStatusType
_Hh3cDot11SecIEStatus_Object = MibTableColumn
hh3cDot11SecIEStatus = _Hh3cDot11SecIEStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 2, 3, 1, 2),
    _Hh3cDot11SecIEStatus_Type()
)
hh3cDot11SecIEStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cDot11SecIEStatus.setStatus("current")
_Hh3cDot11SecurityCiphers_Type = Integer32
_Hh3cDot11SecurityCiphers_Object = MibTableColumn
hh3cDot11SecurityCiphers = _Hh3cDot11SecurityCiphers_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 2, 3, 1, 3),
    _Hh3cDot11SecurityCiphers_Type()
)
hh3cDot11SecurityCiphers.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cDot11SecurityCiphers.setStatus("current")


class _Hh3cDot11CipherKeyIndex_Type(Integer32):
    """Custom type hh3cDot11CipherKeyIndex based on Integer32"""
    defaultValue = 1


_Hh3cDot11CipherKeyIndex_Type.__name__ = "Integer32"
_Hh3cDot11CipherKeyIndex_Object = MibTableColumn
hh3cDot11CipherKeyIndex = _Hh3cDot11CipherKeyIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 2, 3, 1, 4),
    _Hh3cDot11CipherKeyIndex_Type()
)
hh3cDot11CipherKeyIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cDot11CipherKeyIndex.setStatus("current")
_Hh3cDot11CipherKey_Type = OctetString
_Hh3cDot11CipherKey_Object = MibTableColumn
hh3cDot11CipherKey = _Hh3cDot11CipherKey_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 2, 3, 1, 5),
    _Hh3cDot11CipherKey_Type()
)
hh3cDot11CipherKey.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cDot11CipherKey.setStatus("current")
_Hh3cDot11SrvPolicyExtRowStatus_Type = RowStatus
_Hh3cDot11SrvPolicyExtRowStatus_Object = MibTableColumn
hh3cDot11SrvPolicyExtRowStatus = _Hh3cDot11SrvPolicyExtRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 2, 3, 1, 6),
    _Hh3cDot11SrvPolicyExtRowStatus_Type()
)
hh3cDot11SrvPolicyExtRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cDot11SrvPolicyExtRowStatus.setStatus("current")


class _Hh3cDot11CipherKeyType_Type(Integer32):
    """Custom type hh3cDot11CipherKeyType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("char", 1),
          ("hex", 2))
    )


_Hh3cDot11CipherKeyType_Type.__name__ = "Integer32"
_Hh3cDot11CipherKeyType_Object = MibTableColumn
hh3cDot11CipherKeyType = _Hh3cDot11CipherKeyType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 2, 3, 1, 7),
    _Hh3cDot11CipherKeyType_Type()
)
hh3cDot11CipherKeyType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cDot11CipherKeyType.setStatus("current")


class _Hh3cDot11AkmMode_Type(Integer32):
    """Custom type hh3cDot11AkmMode based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("dot1x", 1),
          ("psk", 2))
    )


_Hh3cDot11AkmMode_Type.__name__ = "Integer32"
_Hh3cDot11AkmMode_Object = MibTableColumn
hh3cDot11AkmMode = _Hh3cDot11AkmMode_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 2, 3, 1, 8),
    _Hh3cDot11AkmMode_Type()
)
hh3cDot11AkmMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cDot11AkmMode.setStatus("current")
_Hh3cDot11PskKey_Type = OctetString
_Hh3cDot11PskKey_Object = MibTableColumn
hh3cDot11PskKey = _Hh3cDot11PskKey_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 2, 3, 1, 9),
    _Hh3cDot11PskKey_Type()
)
hh3cDot11PskKey.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cDot11PskKey.setStatus("current")
_Hh3cDot11RadioPolicyExtTable_Object = MibTable
hh3cDot11RadioPolicyExtTable = _Hh3cDot11RadioPolicyExtTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 2, 4)
)
if mibBuilder.loadTexts:
    hh3cDot11RadioPolicyExtTable.setStatus("current")
_Hh3cDot11RadioPolicyExtEntry_Object = MibTableRow
hh3cDot11RadioPolicyExtEntry = _Hh3cDot11RadioPolicyExtEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 2, 4, 1)
)
hh3cDot11RadioPolicyExtEntry.setIndexNames(
    (0, "HH3C-DOT11-CFG-MIB", "hh3cDot11RPAPSerialID"),
    (0, "HH3C-DOT11-CFG-MIB", "hh3cDot11RPRadioID"),
)
if mibBuilder.loadTexts:
    hh3cDot11RadioPolicyExtEntry.setStatus("current")


class _Hh3cDot11RPAPSerialID_Type(OctetString):
    """Custom type hh3cDot11RPAPSerialID based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_Hh3cDot11RPAPSerialID_Type.__name__ = "OctetString"
_Hh3cDot11RPAPSerialID_Object = MibTableColumn
hh3cDot11RPAPSerialID = _Hh3cDot11RPAPSerialID_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 2, 4, 1, 1),
    _Hh3cDot11RPAPSerialID_Type()
)
hh3cDot11RPAPSerialID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cDot11RPAPSerialID.setStatus("current")
_Hh3cDot11RPRadioID_Type = Hh3cDot11RadioScopeType
_Hh3cDot11RPRadioID_Object = MibTableColumn
hh3cDot11RPRadioID = _Hh3cDot11RPRadioID_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 2, 4, 1, 2),
    _Hh3cDot11RPRadioID_Type()
)
hh3cDot11RPRadioID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cDot11RPRadioID.setStatus("current")


class _Hh3cDot11RPBeaconInterval_Type(Integer32):
    """Custom type hh3cDot11RPBeaconInterval based on Integer32"""
    defaultValue = 100


_Hh3cDot11RPBeaconInterval_Type.__name__ = "Integer32"
_Hh3cDot11RPBeaconInterval_Object = MibTableColumn
hh3cDot11RPBeaconInterval = _Hh3cDot11RPBeaconInterval_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 2, 4, 1, 3),
    _Hh3cDot11RPBeaconInterval_Type()
)
hh3cDot11RPBeaconInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDot11RPBeaconInterval.setStatus("current")
if mibBuilder.loadTexts:
    hh3cDot11RPBeaconInterval.setUnits("milliseconds")


class _Hh3cDot11RPDtimInterval_Type(Integer32):
    """Custom type hh3cDot11RPDtimInterval based on Integer32"""
    defaultValue = 1


_Hh3cDot11RPDtimInterval_Type.__name__ = "Integer32"
_Hh3cDot11RPDtimInterval_Object = MibTableColumn
hh3cDot11RPDtimInterval = _Hh3cDot11RPDtimInterval_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 2, 4, 1, 4),
    _Hh3cDot11RPDtimInterval_Type()
)
hh3cDot11RPDtimInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDot11RPDtimInterval.setStatus("current")


class _Hh3cDot11RPRtsThreshold_Type(Integer32):
    """Custom type hh3cDot11RPRtsThreshold based on Integer32"""
    defaultValue = 2346


_Hh3cDot11RPRtsThreshold_Type.__name__ = "Integer32"
_Hh3cDot11RPRtsThreshold_Object = MibTableColumn
hh3cDot11RPRtsThreshold = _Hh3cDot11RPRtsThreshold_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 2, 4, 1, 5),
    _Hh3cDot11RPRtsThreshold_Type()
)
hh3cDot11RPRtsThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDot11RPRtsThreshold.setStatus("current")
if mibBuilder.loadTexts:
    hh3cDot11RPRtsThreshold.setUnits("byte")


class _Hh3cDot11RPFragThreshold_Type(Integer32):
    """Custom type hh3cDot11RPFragThreshold based on Integer32"""
    defaultValue = 2346


_Hh3cDot11RPFragThreshold_Type.__name__ = "Integer32"
_Hh3cDot11RPFragThreshold_Object = MibTableColumn
hh3cDot11RPFragThreshold = _Hh3cDot11RPFragThreshold_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 2, 4, 1, 6),
    _Hh3cDot11RPFragThreshold_Type()
)
hh3cDot11RPFragThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDot11RPFragThreshold.setStatus("current")
if mibBuilder.loadTexts:
    hh3cDot11RPFragThreshold.setUnits("byte")


class _Hh3cDot11RPShortRetryThreshold_Type(Integer32):
    """Custom type hh3cDot11RPShortRetryThreshold based on Integer32"""
    defaultValue = 7


_Hh3cDot11RPShortRetryThreshold_Type.__name__ = "Integer32"
_Hh3cDot11RPShortRetryThreshold_Object = MibTableColumn
hh3cDot11RPShortRetryThreshold = _Hh3cDot11RPShortRetryThreshold_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 2, 4, 1, 7),
    _Hh3cDot11RPShortRetryThreshold_Type()
)
hh3cDot11RPShortRetryThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDot11RPShortRetryThreshold.setStatus("current")


class _Hh3cDot11RPLongRetryThreshold_Type(Integer32):
    """Custom type hh3cDot11RPLongRetryThreshold based on Integer32"""
    defaultValue = 4


_Hh3cDot11RPLongRetryThreshold_Type.__name__ = "Integer32"
_Hh3cDot11RPLongRetryThreshold_Object = MibTableColumn
hh3cDot11RPLongRetryThreshold = _Hh3cDot11RPLongRetryThreshold_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 2, 4, 1, 8),
    _Hh3cDot11RPLongRetryThreshold_Type()
)
hh3cDot11RPLongRetryThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDot11RPLongRetryThreshold.setStatus("current")


class _Hh3cDot11RPClientMaxCount_Type(Integer32):
    """Custom type hh3cDot11RPClientMaxCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_Hh3cDot11RPClientMaxCount_Type.__name__ = "Integer32"
_Hh3cDot11RPClientMaxCount_Object = MibTableColumn
hh3cDot11RPClientMaxCount = _Hh3cDot11RPClientMaxCount_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 2, 4, 1, 9),
    _Hh3cDot11RPClientMaxCount_Type()
)
hh3cDot11RPClientMaxCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDot11RPClientMaxCount.setStatus("current")


class _Hh3cDot11RPBeaconIntervalCM_Type(Integer32):
    """Custom type hh3cDot11RPBeaconIntervalCM based on Integer32"""
    defaultValue = 100


_Hh3cDot11RPBeaconIntervalCM_Type.__name__ = "Integer32"
_Hh3cDot11RPBeaconIntervalCM_Object = MibTableColumn
hh3cDot11RPBeaconIntervalCM = _Hh3cDot11RPBeaconIntervalCM_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 2, 4, 1, 10),
    _Hh3cDot11RPBeaconIntervalCM_Type()
)
hh3cDot11RPBeaconIntervalCM.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDot11RPBeaconIntervalCM.setStatus("current")
if mibBuilder.loadTexts:
    hh3cDot11RPBeaconIntervalCM.setUnits("timeunit")
_Hh3cDot11SrvPortSecurityTable_Object = MibTable
hh3cDot11SrvPortSecurityTable = _Hh3cDot11SrvPortSecurityTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 2, 5)
)
if mibBuilder.loadTexts:
    hh3cDot11SrvPortSecurityTable.setStatus("current")
_Hh3cDot11SrvPortSecurityEntry_Object = MibTableRow
hh3cDot11SrvPortSecurityEntry = _Hh3cDot11SrvPortSecurityEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 2, 5, 1)
)
hh3cDot11SrvPortSecurityEntry.setIndexNames(
    (0, "HH3C-DOT11-CFG-MIB", "hh3cDot11SecurityServicePolicyID"),
)
if mibBuilder.loadTexts:
    hh3cDot11SrvPortSecurityEntry.setStatus("current")
_Hh3cDot11SecurityServicePolicyID_Type = Hh3cDot11ServicePolicyIDType
_Hh3cDot11SecurityServicePolicyID_Object = MibTableColumn
hh3cDot11SecurityServicePolicyID = _Hh3cDot11SecurityServicePolicyID_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 2, 5, 1, 1),
    _Hh3cDot11SecurityServicePolicyID_Type()
)
hh3cDot11SecurityServicePolicyID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cDot11SecurityServicePolicyID.setStatus("current")


class _Hh3cDot11SrvPortSecurityMode_Type(Integer32):
    """Custom type hh3cDot11SrvPortSecurityMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("noRestrictions", 1),
          ("userLoginSecureExt", 2),
          ("psk", 3),
          ("macAddressAndPsk", 4),
          ("userLoginSecureExtOrPsk", 5),
          ("ext", 6))
    )


_Hh3cDot11SrvPortSecurityMode_Type.__name__ = "Integer32"
_Hh3cDot11SrvPortSecurityMode_Object = MibTableColumn
hh3cDot11SrvPortSecurityMode = _Hh3cDot11SrvPortSecurityMode_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 2, 5, 1, 2),
    _Hh3cDot11SrvPortSecurityMode_Type()
)
hh3cDot11SrvPortSecurityMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDot11SrvPortSecurityMode.setStatus("current")


class _Hh3cDot11SrvSecurityKeyType_Type(Integer32):
    """Custom type hh3cDot11SrvSecurityKeyType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("userLoginTxKeyTypeNone", 1),
          ("userLoginTxKeyTypeDot11Key", 2),
          ("userLoginTxKeyTypeRsaRC4Key", 3))
    )


_Hh3cDot11SrvSecurityKeyType_Type.__name__ = "Integer32"
_Hh3cDot11SrvSecurityKeyType_Object = MibTableColumn
hh3cDot11SrvSecurityKeyType = _Hh3cDot11SrvSecurityKeyType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 2, 5, 1, 3),
    _Hh3cDot11SrvSecurityKeyType_Type()
)
hh3cDot11SrvSecurityKeyType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDot11SrvSecurityKeyType.setStatus("current")


class _Hh3cDot11SrvSecurityPskKeyMode_Type(Integer32):
    """Custom type hh3cDot11SrvSecurityPskKeyMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("pskKeyModeNone", 1),
          ("pskKeyModePassPhrase", 2),
          ("pskKeyModeRawKey", 3))
    )


_Hh3cDot11SrvSecurityPskKeyMode_Type.__name__ = "Integer32"
_Hh3cDot11SrvSecurityPskKeyMode_Object = MibTableColumn
hh3cDot11SrvSecurityPskKeyMode = _Hh3cDot11SrvSecurityPskKeyMode_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 2, 5, 1, 4),
    _Hh3cDot11SrvSecurityPskKeyMode_Type()
)
hh3cDot11SrvSecurityPskKeyMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDot11SrvSecurityPskKeyMode.setStatus("current")


class _Hh3cDot11SrvSecurityPskKeyString_Type(DisplayString):
    """Custom type hh3cDot11SrvSecurityPskKeyString based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_Hh3cDot11SrvSecurityPskKeyString_Type.__name__ = "DisplayString"
_Hh3cDot11SrvSecurityPskKeyString_Object = MibTableColumn
hh3cDot11SrvSecurityPskKeyString = _Hh3cDot11SrvSecurityPskKeyString_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 2, 5, 1, 5),
    _Hh3cDot11SrvSecurityPskKeyString_Type()
)
hh3cDot11SrvSecurityPskKeyString.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDot11SrvSecurityPskKeyString.setStatus("current")


class _Hh3cDot11SrvPortSecurityModeCM_Type(Integer32):
    """Custom type hh3cDot11SrvPortSecurityModeCM based on Integer32"""
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
        *(("none", 0),
          ("psk", 1),
          ("radius", 2),
          ("wlanex", 3))
    )


_Hh3cDot11SrvPortSecurityModeCM_Type.__name__ = "Integer32"
_Hh3cDot11SrvPortSecurityModeCM_Object = MibTableColumn
hh3cDot11SrvPortSecurityModeCM = _Hh3cDot11SrvPortSecurityModeCM_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 2, 5, 1, 6),
    _Hh3cDot11SrvPortSecurityModeCM_Type()
)
hh3cDot11SrvPortSecurityModeCM.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDot11SrvPortSecurityModeCM.setStatus("current")
_Hh3cDot11SrvPolicyExtendTable_Object = MibTable
hh3cDot11SrvPolicyExtendTable = _Hh3cDot11SrvPolicyExtendTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 2, 6)
)
if mibBuilder.loadTexts:
    hh3cDot11SrvPolicyExtendTable.setStatus("current")
_Hh3cDot11SrvPolicyExtendEntry_Object = MibTableRow
hh3cDot11SrvPolicyExtendEntry = _Hh3cDot11SrvPolicyExtendEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 2, 6, 1)
)
hh3cDot11SrvPolicyExtendEntry.setIndexNames(
    (0, "HH3C-DOT11-CFG-MIB", "hh3cDot11ServicePolicyID"),
)
if mibBuilder.loadTexts:
    hh3cDot11SrvPolicyExtendEntry.setStatus("current")


class _Hh3cDot11SPEnable_Type(Integer32):
    """Custom type hh3cDot11SPEnable based on Integer32"""
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


_Hh3cDot11SPEnable_Type.__name__ = "Integer32"
_Hh3cDot11SPEnable_Object = MibTableColumn
hh3cDot11SPEnable = _Hh3cDot11SPEnable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 2, 6, 1, 1),
    _Hh3cDot11SPEnable_Type()
)
hh3cDot11SPEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDot11SPEnable.setStatus("current")
_Hh3cDot11SrvL2AuthenTable_Object = MibTable
hh3cDot11SrvL2AuthenTable = _Hh3cDot11SrvL2AuthenTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 2, 7)
)
if mibBuilder.loadTexts:
    hh3cDot11SrvL2AuthenTable.setStatus("current")
_Hh3cDot11SrvL2AuthenEntry_Object = MibTableRow
hh3cDot11SrvL2AuthenEntry = _Hh3cDot11SrvL2AuthenEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 2, 7, 1)
)
hh3cDot11SrvL2AuthenEntry.setIndexNames(
    (0, "HH3C-DOT11-CFG-MIB", "hh3cDot11SrvL2AuthenID"),
)
if mibBuilder.loadTexts:
    hh3cDot11SrvL2AuthenEntry.setStatus("current")
_Hh3cDot11SrvL2AuthenID_Type = Hh3cDot11ServicePolicyIDType
_Hh3cDot11SrvL2AuthenID_Object = MibTableColumn
hh3cDot11SrvL2AuthenID = _Hh3cDot11SrvL2AuthenID_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 2, 7, 1, 1),
    _Hh3cDot11SrvL2AuthenID_Type()
)
hh3cDot11SrvL2AuthenID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cDot11SrvL2AuthenID.setStatus("current")


class _Hh3cDot11L2AuthenMode_Type(Integer32):
    """Custom type hh3cDot11L2AuthenMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("bypass", 1),
          ("macAuthentication", 2),
          ("macThenDot1xAuthentication", 3),
          ("dot1xAuthentication", 4),
          ("dot1xThenMacAuthentication", 5),
          ("ouiThenDot1x", 6),
          ("macAndDot1x", 7))
    )


_Hh3cDot11L2AuthenMode_Type.__name__ = "Integer32"
_Hh3cDot11L2AuthenMode_Object = MibTableColumn
hh3cDot11L2AuthenMode = _Hh3cDot11L2AuthenMode_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 2, 7, 1, 2),
    _Hh3cDot11L2AuthenMode_Type()
)
hh3cDot11L2AuthenMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDot11L2AuthenMode.setStatus("current")
_Hh3cDot11L2IntrusProtectEnable_Type = TruthValue
_Hh3cDot11L2IntrusProtectEnable_Object = MibTableColumn
hh3cDot11L2IntrusProtectEnable = _Hh3cDot11L2IntrusProtectEnable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 2, 7, 1, 3),
    _Hh3cDot11L2IntrusProtectEnable_Type()
)
hh3cDot11L2IntrusProtectEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDot11L2IntrusProtectEnable.setStatus("current")


class _Hh3cDot11L2IntrusProtectOpt_Type(Integer32):
    """Custom type hh3cDot11L2IntrusProtectOpt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("blockMACTemporarily", 1),
          ("stopServiceTemporarily", 2),
          ("stopService", 3))
    )


_Hh3cDot11L2IntrusProtectOpt_Type.__name__ = "Integer32"
_Hh3cDot11L2IntrusProtectOpt_Object = MibTableColumn
hh3cDot11L2IntrusProtectOpt = _Hh3cDot11L2IntrusProtectOpt_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 2, 7, 1, 4),
    _Hh3cDot11L2IntrusProtectOpt_Type()
)
hh3cDot11L2IntrusProtectOpt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDot11L2IntrusProtectOpt.setStatus("current")


class _Hh3cDot11TempServiceStopTimer_Type(Integer32):
    """Custom type hh3cDot11TempServiceStopTimer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 300),
    )


_Hh3cDot11TempServiceStopTimer_Type.__name__ = "Integer32"
_Hh3cDot11TempServiceStopTimer_Object = MibTableColumn
hh3cDot11TempServiceStopTimer = _Hh3cDot11TempServiceStopTimer_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 2, 7, 1, 5),
    _Hh3cDot11TempServiceStopTimer_Type()
)
hh3cDot11TempServiceStopTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDot11TempServiceStopTimer.setStatus("current")


class _Hh3cDot11TempBlockMACTimer_Type(Integer32):
    """Custom type hh3cDot11TempBlockMACTimer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(60, 300),
    )


_Hh3cDot11TempBlockMACTimer_Type.__name__ = "Integer32"
_Hh3cDot11TempBlockMACTimer_Object = MibTableColumn
hh3cDot11TempBlockMACTimer = _Hh3cDot11TempBlockMACTimer_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 2, 7, 1, 6),
    _Hh3cDot11TempBlockMACTimer_Type()
)
hh3cDot11TempBlockMACTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDot11TempBlockMACTimer.setStatus("current")
_Hh3cDot11L2IgnoreAuthorization_Type = TruthValue
_Hh3cDot11L2IgnoreAuthorization_Object = MibTableColumn
hh3cDot11L2IgnoreAuthorization = _Hh3cDot11L2IgnoreAuthorization_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 2, 7, 1, 7),
    _Hh3cDot11L2IgnoreAuthorization_Type()
)
hh3cDot11L2IgnoreAuthorization.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDot11L2IgnoreAuthorization.setStatus("current")


class _Hh3cDot11L2FailVLAN_Type(Integer32):
    """Custom type hh3cDot11L2FailVLAN based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_Hh3cDot11L2FailVLAN_Type.__name__ = "Integer32"
_Hh3cDot11L2FailVLAN_Object = MibTableColumn
hh3cDot11L2FailVLAN = _Hh3cDot11L2FailVLAN_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 2, 7, 1, 8),
    _Hh3cDot11L2FailVLAN_Type()
)
hh3cDot11L2FailVLAN.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDot11L2FailVLAN.setStatus("current")


class _Hh3cDot11L2CriticalVLAN_Type(Integer32):
    """Custom type hh3cDot11L2CriticalVLAN based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_Hh3cDot11L2CriticalVLAN_Type.__name__ = "Integer32"
_Hh3cDot11L2CriticalVLAN_Object = MibTableColumn
hh3cDot11L2CriticalVLAN = _Hh3cDot11L2CriticalVLAN_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 2, 7, 1, 9),
    _Hh3cDot11L2CriticalVLAN_Type()
)
hh3cDot11L2CriticalVLAN.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDot11L2CriticalVLAN.setStatus("current")
_Hh3cDot11L2AuthorFailOffline_Type = TruthValue
_Hh3cDot11L2AuthorFailOffline_Object = MibTableColumn
hh3cDot11L2AuthorFailOffline = _Hh3cDot11L2AuthorFailOffline_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 2, 7, 1, 10),
    _Hh3cDot11L2AuthorFailOffline_Type()
)
hh3cDot11L2AuthorFailOffline.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDot11L2AuthorFailOffline.setStatus("current")
_Hh3cDot11L2AccountFailOffline_Type = TruthValue
_Hh3cDot11L2AccountFailOffline_Object = MibTableColumn
hh3cDot11L2AccountFailOffline = _Hh3cDot11L2AccountFailOffline_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 2, 7, 1, 11),
    _Hh3cDot11L2AccountFailOffline_Type()
)
hh3cDot11L2AccountFailOffline.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDot11L2AccountFailOffline.setStatus("current")
_Hh3cDot11Dot1xHSEnable_Type = TruthValue
_Hh3cDot11Dot1xHSEnable_Object = MibTableColumn
hh3cDot11Dot1xHSEnable = _Hh3cDot11Dot1xHSEnable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 2, 7, 1, 12),
    _Hh3cDot11Dot1xHSEnable_Type()
)
hh3cDot11Dot1xHSEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDot11Dot1xHSEnable.setStatus("current")
_Hh3cDot11Dot1xSecureHSEnable_Type = TruthValue
_Hh3cDot11Dot1xSecureHSEnable_Object = MibTableColumn
hh3cDot11Dot1xSecureHSEnable = _Hh3cDot11Dot1xSecureHSEnable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 2, 7, 1, 13),
    _Hh3cDot11Dot1xSecureHSEnable_Type()
)
hh3cDot11Dot1xSecureHSEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDot11Dot1xSecureHSEnable.setStatus("current")
_Hh3cDot11Dot1xReauthenEnable_Type = TruthValue
_Hh3cDot11Dot1xReauthenEnable_Object = MibTableColumn
hh3cDot11Dot1xReauthenEnable = _Hh3cDot11Dot1xReauthenEnable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 2, 7, 1, 14),
    _Hh3cDot11Dot1xReauthenEnable_Type()
)
hh3cDot11Dot1xReauthenEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDot11Dot1xReauthenEnable.setStatus("current")
_Hh3cDot11Dot1xMandatoryDomain_Type = OctetString
_Hh3cDot11Dot1xMandatoryDomain_Object = MibTableColumn
hh3cDot11Dot1xMandatoryDomain = _Hh3cDot11Dot1xMandatoryDomain_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 2, 7, 1, 15),
    _Hh3cDot11Dot1xMandatoryDomain_Type()
)
hh3cDot11Dot1xMandatoryDomain.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDot11Dot1xMandatoryDomain.setStatus("current")
_Hh3cDot11Dot1xMaxUserCount_Type = Integer32
_Hh3cDot11Dot1xMaxUserCount_Object = MibTableColumn
hh3cDot11Dot1xMaxUserCount = _Hh3cDot11Dot1xMaxUserCount_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 2, 7, 1, 16),
    _Hh3cDot11Dot1xMaxUserCount_Type()
)
hh3cDot11Dot1xMaxUserCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDot11Dot1xMaxUserCount.setStatus("current")
_Hh3cDot11MACAuthenDomain_Type = OctetString
_Hh3cDot11MACAuthenDomain_Object = MibTableColumn
hh3cDot11MACAuthenDomain = _Hh3cDot11MACAuthenDomain_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 2, 7, 1, 17),
    _Hh3cDot11MACAuthenDomain_Type()
)
hh3cDot11MACAuthenDomain.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDot11MACAuthenDomain.setStatus("current")
_Hh3cDot11MACAuthenMaxUserCount_Type = Integer32
_Hh3cDot11MACAuthenMaxUserCount_Object = MibTableColumn
hh3cDot11MACAuthenMaxUserCount = _Hh3cDot11MACAuthenMaxUserCount_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 2, 7, 1, 18),
    _Hh3cDot11MACAuthenMaxUserCount_Type()
)
hh3cDot11MACAuthenMaxUserCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDot11MACAuthenMaxUserCount.setStatus("current")
_Hh3cDot11IPLearningTable_Object = MibTable
hh3cDot11IPLearningTable = _Hh3cDot11IPLearningTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 2, 8)
)
if mibBuilder.loadTexts:
    hh3cDot11IPLearningTable.setStatus("current")
_Hh3cDot11IPLearningEntry_Object = MibTableRow
hh3cDot11IPLearningEntry = _Hh3cDot11IPLearningEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 2, 8, 1)
)
hh3cDot11IPLearningEntry.setIndexNames(
    (0, "HH3C-DOT11-CFG-MIB", "hh3cDot11IPLearningServiceName"),
    (0, "HH3C-DOT11-CFG-MIB", "hh3cDot11IPLearningType"),
)
if mibBuilder.loadTexts:
    hh3cDot11IPLearningEntry.setStatus("current")


class _Hh3cDot11IPLearningServiceName_Type(OctetString):
    """Custom type hh3cDot11IPLearningServiceName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_Hh3cDot11IPLearningServiceName_Type.__name__ = "OctetString"
_Hh3cDot11IPLearningServiceName_Object = MibTableColumn
hh3cDot11IPLearningServiceName = _Hh3cDot11IPLearningServiceName_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 2, 8, 1, 1),
    _Hh3cDot11IPLearningServiceName_Type()
)
hh3cDot11IPLearningServiceName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cDot11IPLearningServiceName.setStatus("current")


class _Hh3cDot11IPLearningType_Type(Integer32):
    """Custom type hh3cDot11IPLearningType based on Integer32"""
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
        *(("invalid", 1),
          ("arp", 2),
          ("dhcp", 3),
          ("dhcp6", 4),
          ("nd", 5))
    )


_Hh3cDot11IPLearningType_Type.__name__ = "Integer32"
_Hh3cDot11IPLearningType_Object = MibTableColumn
hh3cDot11IPLearningType = _Hh3cDot11IPLearningType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 2, 8, 1, 2),
    _Hh3cDot11IPLearningType_Type()
)
hh3cDot11IPLearningType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cDot11IPLearningType.setStatus("current")
_Hh3cDot11IPLearningStatus_Type = TruthValue
_Hh3cDot11IPLearningStatus_Object = MibTableColumn
hh3cDot11IPLearningStatus = _Hh3cDot11IPLearningStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 2, 8, 1, 3),
    _Hh3cDot11IPLearningStatus_Type()
)
hh3cDot11IPLearningStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDot11IPLearningStatus.setStatus("current")


class _Hh3cDot11IPLearningVlanBitMapL_Type(OctetString):
    """Custom type hh3cDot11IPLearningVlanBitMapL based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 256),
    )


_Hh3cDot11IPLearningVlanBitMapL_Type.__name__ = "OctetString"
_Hh3cDot11IPLearningVlanBitMapL_Object = MibTableColumn
hh3cDot11IPLearningVlanBitMapL = _Hh3cDot11IPLearningVlanBitMapL_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 2, 8, 1, 4),
    _Hh3cDot11IPLearningVlanBitMapL_Type()
)
hh3cDot11IPLearningVlanBitMapL.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDot11IPLearningVlanBitMapL.setStatus("current")


class _Hh3cDot11IPLearningVlanBitMapH_Type(OctetString):
    """Custom type hh3cDot11IPLearningVlanBitMapH based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 256),
    )


_Hh3cDot11IPLearningVlanBitMapH_Type.__name__ = "OctetString"
_Hh3cDot11IPLearningVlanBitMapH_Object = MibTableColumn
hh3cDot11IPLearningVlanBitMapH = _Hh3cDot11IPLearningVlanBitMapH_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 2, 8, 1, 5),
    _Hh3cDot11IPLearningVlanBitMapH_Type()
)
hh3cDot11IPLearningVlanBitMapH.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDot11IPLearningVlanBitMapH.setStatus("current")
_Hh3cDot11APConfigGroup_ObjectIdentity = ObjectIdentity
hh3cDot11APConfigGroup = _Hh3cDot11APConfigGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 3)
)
_Hh3cDot11APTemplateTable_Object = MibTable
hh3cDot11APTemplateTable = _Hh3cDot11APTemplateTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 3, 1)
)
if mibBuilder.loadTexts:
    hh3cDot11APTemplateTable.setStatus("current")
_Hh3cDot11APTemplateEntry_Object = MibTableRow
hh3cDot11APTemplateEntry = _Hh3cDot11APTemplateEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 3, 1, 1)
)
hh3cDot11APTemplateEntry.setIndexNames(
    (0, "HH3C-DOT11-CFG-MIB", "hh3cDot11APTemplateName"),
)
if mibBuilder.loadTexts:
    hh3cDot11APTemplateEntry.setStatus("current")


class _Hh3cDot11APTemplateName_Type(OctetString):
    """Custom type hh3cDot11APTemplateName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_Hh3cDot11APTemplateName_Type.__name__ = "OctetString"
_Hh3cDot11APTemplateName_Object = MibTableColumn
hh3cDot11APTemplateName = _Hh3cDot11APTemplateName_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 3, 1, 1, 1),
    _Hh3cDot11APTemplateName_Type()
)
hh3cDot11APTemplateName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cDot11APTemplateName.setStatus("current")
_Hh3cDot11APSerialID_Type = OctetString
_Hh3cDot11APSerialID_Object = MibTableColumn
hh3cDot11APSerialID = _Hh3cDot11APSerialID_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 3, 1, 1, 2),
    _Hh3cDot11APSerialID_Type()
)
hh3cDot11APSerialID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cDot11APSerialID.setStatus("current")
_Hh3cDot11TemplateAPModelAlias_Type = OctetString
_Hh3cDot11TemplateAPModelAlias_Object = MibTableColumn
hh3cDot11TemplateAPModelAlias = _Hh3cDot11TemplateAPModelAlias_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 3, 1, 1, 3),
    _Hh3cDot11TemplateAPModelAlias_Type()
)
hh3cDot11TemplateAPModelAlias.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cDot11TemplateAPModelAlias.setStatus("current")
_Hh3cDot11Description_Type = OctetString
_Hh3cDot11Description_Object = MibTableColumn
hh3cDot11Description = _Hh3cDot11Description_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 3, 1, 1, 4),
    _Hh3cDot11Description_Type()
)
hh3cDot11Description.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cDot11Description.setStatus("current")


class _Hh3cDot11APWorkMode_Type(Integer32):
    """Custom type hh3cDot11APWorkMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("normal", 1),
          ("monitor", 2),
          ("hybrid", 3))
    )


_Hh3cDot11APWorkMode_Type.__name__ = "Integer32"
_Hh3cDot11APWorkMode_Object = MibTableColumn
hh3cDot11APWorkMode = _Hh3cDot11APWorkMode_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 3, 1, 1, 5),
    _Hh3cDot11APWorkMode_Type()
)
hh3cDot11APWorkMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cDot11APWorkMode.setStatus("current")
_Hh3cDot11APTemplateRowStatus_Type = RowStatus
_Hh3cDot11APTemplateRowStatus_Object = MibTableColumn
hh3cDot11APTemplateRowStatus = _Hh3cDot11APTemplateRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 3, 1, 1, 6),
    _Hh3cDot11APTemplateRowStatus_Type()
)
hh3cDot11APTemplateRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cDot11APTemplateRowStatus.setStatus("current")
_Hh3cDot11APName_Type = OctetString
_Hh3cDot11APName_Object = MibTableColumn
hh3cDot11APName = _Hh3cDot11APName_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 3, 1, 1, 7),
    _Hh3cDot11APName_Type()
)
hh3cDot11APName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cDot11APName.setStatus("current")
_Hh3cDot11StatisInterv_Type = Integer32
_Hh3cDot11StatisInterv_Object = MibTableColumn
hh3cDot11StatisInterv = _Hh3cDot11StatisInterv_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 3, 1, 1, 8),
    _Hh3cDot11StatisInterv_Type()
)
hh3cDot11StatisInterv.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cDot11StatisInterv.setStatus("current")
if mibBuilder.loadTexts:
    hh3cDot11StatisInterv.setUnits("second")


class _Hh3cDot11APBroadcastProbeReply_Type(TruthValue):
    """Custom type hh3cDot11APBroadcastProbeReply based on TruthValue"""
    defaultValue = 1


_Hh3cDot11APBroadcastProbeReply_Type.__name__ = "TruthValue"
_Hh3cDot11APBroadcastProbeReply_Object = MibTableColumn
hh3cDot11APBroadcastProbeReply = _Hh3cDot11APBroadcastProbeReply_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 3, 1, 1, 9),
    _Hh3cDot11APBroadcastProbeReply_Type()
)
hh3cDot11APBroadcastProbeReply.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cDot11APBroadcastProbeReply.setStatus("current")
_Hh3cDot11StaIdleTimerInterv_Type = Integer32
_Hh3cDot11StaIdleTimerInterv_Object = MibTableColumn
hh3cDot11StaIdleTimerInterv = _Hh3cDot11StaIdleTimerInterv_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 3, 1, 1, 10),
    _Hh3cDot11StaIdleTimerInterv_Type()
)
hh3cDot11StaIdleTimerInterv.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cDot11StaIdleTimerInterv.setStatus("current")
if mibBuilder.loadTexts:
    hh3cDot11StaIdleTimerInterv.setUnits("second")
_Hh3cDot11StaKeepAliveTimerInterv_Type = Integer32
_Hh3cDot11StaKeepAliveTimerInterv_Object = MibTableColumn
hh3cDot11StaKeepAliveTimerInterv = _Hh3cDot11StaKeepAliveTimerInterv_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 3, 1, 1, 11),
    _Hh3cDot11StaKeepAliveTimerInterv_Type()
)
hh3cDot11StaKeepAliveTimerInterv.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cDot11StaKeepAliveTimerInterv.setStatus("current")
if mibBuilder.loadTexts:
    hh3cDot11StaKeepAliveTimerInterv.setUnits("second")
_Hh3cDot11APCir_Type = Integer32
_Hh3cDot11APCir_Object = MibTableColumn
hh3cDot11APCir = _Hh3cDot11APCir_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 3, 1, 1, 12),
    _Hh3cDot11APCir_Type()
)
hh3cDot11APCir.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cDot11APCir.setStatus("current")
if mibBuilder.loadTexts:
    hh3cDot11APCir.setUnits("Kbps")
_Hh3cDot11APCbs_Type = Integer32
_Hh3cDot11APCbs_Object = MibTableColumn
hh3cDot11APCbs = _Hh3cDot11APCbs_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 3, 1, 1, 13),
    _Hh3cDot11APCbs_Type()
)
hh3cDot11APCbs.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cDot11APCbs.setStatus("current")
if mibBuilder.loadTexts:
    hh3cDot11APCbs.setUnits("Bytes")


class _Hh3cDot11APPriorityLevel_Type(Integer32):
    """Custom type hh3cDot11APPriorityLevel based on Integer32"""
    defaultValue = 4

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_Hh3cDot11APPriorityLevel_Type.__name__ = "Integer32"
_Hh3cDot11APPriorityLevel_Object = MibTableColumn
hh3cDot11APPriorityLevel = _Hh3cDot11APPriorityLevel_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 3, 1, 1, 14),
    _Hh3cDot11APPriorityLevel_Type()
)
hh3cDot11APPriorityLevel.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cDot11APPriorityLevel.setStatus("current")
_Hh3cDot11APElementID_Type = Integer32
_Hh3cDot11APElementID_Object = MibTableColumn
hh3cDot11APElementID = _Hh3cDot11APElementID_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 3, 1, 1, 15),
    _Hh3cDot11APElementID_Type()
)
hh3cDot11APElementID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11APElementID.setStatus("current")


class _Hh3cDot11APDevDetectEnable_Type(TruthValue):
    """Custom type hh3cDot11APDevDetectEnable based on TruthValue"""
    defaultValue = 2


_Hh3cDot11APDevDetectEnable_Type.__name__ = "TruthValue"
_Hh3cDot11APDevDetectEnable_Object = MibTableColumn
hh3cDot11APDevDetectEnable = _Hh3cDot11APDevDetectEnable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 3, 1, 1, 16),
    _Hh3cDot11APDevDetectEnable_Type()
)
hh3cDot11APDevDetectEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cDot11APDevDetectEnable.setStatus("current")


class _Hh3cDot11APGetIPMethod_Type(Integer32):
    """Custom type hh3cDot11APGetIPMethod based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dhcpAlloc", 1),
          ("static", 2))
    )


_Hh3cDot11APGetIPMethod_Type.__name__ = "Integer32"
_Hh3cDot11APGetIPMethod_Object = MibTableColumn
hh3cDot11APGetIPMethod = _Hh3cDot11APGetIPMethod_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 3, 1, 1, 17),
    _Hh3cDot11APGetIPMethod_Type()
)
hh3cDot11APGetIPMethod.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cDot11APGetIPMethod.setStatus("current")


class _Hh3cDot11StatisIntervMode_Type(Integer32):
    """Custom type hh3cDot11StatisIntervMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("normal", 1),
          ("realtime", 2))
    )


_Hh3cDot11StatisIntervMode_Type.__name__ = "Integer32"
_Hh3cDot11StatisIntervMode_Object = MibTableColumn
hh3cDot11StatisIntervMode = _Hh3cDot11StatisIntervMode_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 3, 1, 1, 18),
    _Hh3cDot11StatisIntervMode_Type()
)
hh3cDot11StatisIntervMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cDot11StatisIntervMode.setStatus("current")


class _Hh3cDot11ApTrapEnabled_Type(TruthValue):
    """Custom type hh3cDot11ApTrapEnabled based on TruthValue"""
    defaultValue = 1


_Hh3cDot11ApTrapEnabled_Type.__name__ = "TruthValue"
_Hh3cDot11ApTrapEnabled_Object = MibTableColumn
hh3cDot11ApTrapEnabled = _Hh3cDot11ApTrapEnabled_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 3, 1, 1, 19),
    _Hh3cDot11ApTrapEnabled_Type()
)
hh3cDot11ApTrapEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDot11ApTrapEnabled.setStatus("current")


class _Hh3cDot11ApFmwUpdState_Type(Integer32):
    """Custom type hh3cDot11ApFmwUpdState based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2),
          ("inherit", 3))
    )


_Hh3cDot11ApFmwUpdState_Type.__name__ = "Integer32"
_Hh3cDot11ApFmwUpdState_Object = MibTableColumn
hh3cDot11ApFmwUpdState = _Hh3cDot11ApFmwUpdState_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 3, 1, 1, 20),
    _Hh3cDot11ApFmwUpdState_Type()
)
hh3cDot11ApFmwUpdState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cDot11ApFmwUpdState.setStatus("current")


class _Hh3cDot11StatisIntervModeCM_Type(Integer32):
    """Custom type hh3cDot11StatisIntervModeCM based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_Hh3cDot11StatisIntervModeCM_Type.__name__ = "Integer32"
_Hh3cDot11StatisIntervModeCM_Object = MibTableColumn
hh3cDot11StatisIntervModeCM = _Hh3cDot11StatisIntervModeCM_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 3, 1, 1, 21),
    _Hh3cDot11StatisIntervModeCM_Type()
)
hh3cDot11StatisIntervModeCM.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cDot11StatisIntervModeCM.setStatus("current")
_Hh3cDot11ApNasIDCM_Type = OctetString
_Hh3cDot11ApNasIDCM_Object = MibTableColumn
hh3cDot11ApNasIDCM = _Hh3cDot11ApNasIDCM_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 3, 1, 1, 22),
    _Hh3cDot11ApNasIDCM_Type()
)
hh3cDot11ApNasIDCM.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cDot11ApNasIDCM.setStatus("current")


class _Hh3cDot11ApCoveragetype_Type(Integer32):
    """Custom type hh3cDot11ApCoveragetype based on Integer32"""
    defaultValue = 1

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
        *(("school", 1),
          ("traffic", 2),
          ("shopping", 3),
          ("company", 4))
    )


_Hh3cDot11ApCoveragetype_Type.__name__ = "Integer32"
_Hh3cDot11ApCoveragetype_Object = MibTableColumn
hh3cDot11ApCoveragetype = _Hh3cDot11ApCoveragetype_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 3, 1, 1, 23),
    _Hh3cDot11ApCoveragetype_Type()
)
hh3cDot11ApCoveragetype.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cDot11ApCoveragetype.setStatus("current")


class _Hh3cDot11APControlAddressState_Type(Integer32):
    """Custom type hh3cDot11APControlAddressState based on Integer32"""
    defaultValue = 2

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


_Hh3cDot11APControlAddressState_Type.__name__ = "Integer32"
_Hh3cDot11APControlAddressState_Object = MibTableColumn
hh3cDot11APControlAddressState = _Hh3cDot11APControlAddressState_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 3, 1, 1, 24),
    _Hh3cDot11APControlAddressState_Type()
)
hh3cDot11APControlAddressState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cDot11APControlAddressState.setStatus("current")
_Hh3cDot11APControlAddressIPv4_Type = IpAddress
_Hh3cDot11APControlAddressIPv4_Object = MibTableColumn
hh3cDot11APControlAddressIPv4 = _Hh3cDot11APControlAddressIPv4_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 3, 1, 1, 25),
    _Hh3cDot11APControlAddressIPv4_Type()
)
hh3cDot11APControlAddressIPv4.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cDot11APControlAddressIPv4.setStatus("current")
_Hh3cDot11APControlAddressIPv6_Type = OctetString
_Hh3cDot11APControlAddressIPv6_Object = MibTableColumn
hh3cDot11APControlAddressIPv6 = _Hh3cDot11APControlAddressIPv6_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 3, 1, 1, 26),
    _Hh3cDot11APControlAddressIPv6_Type()
)
hh3cDot11APControlAddressIPv6.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cDot11APControlAddressIPv6.setStatus("current")
_Hh3cDot11APLocalACName_Type = OctetString
_Hh3cDot11APLocalACName_Object = MibTableColumn
hh3cDot11APLocalACName = _Hh3cDot11APLocalACName_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 3, 1, 1, 27),
    _Hh3cDot11APLocalACName_Type()
)
hh3cDot11APLocalACName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11APLocalACName.setStatus("current")
_Hh3cDot11APEchoInterval_Type = Integer32
_Hh3cDot11APEchoInterval_Object = MibTableColumn
hh3cDot11APEchoInterval = _Hh3cDot11APEchoInterval_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 3, 1, 1, 28),
    _Hh3cDot11APEchoInterval_Type()
)
hh3cDot11APEchoInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDot11APEchoInterval.setStatus("current")
_Hh3cDot11APProvisionAPIPv4_Type = IpAddress
_Hh3cDot11APProvisionAPIPv4_Object = MibTableColumn
hh3cDot11APProvisionAPIPv4 = _Hh3cDot11APProvisionAPIPv4_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 3, 1, 1, 29),
    _Hh3cDot11APProvisionAPIPv4_Type()
)
hh3cDot11APProvisionAPIPv4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDot11APProvisionAPIPv4.setStatus("current")


class _Hh3cDot11APProvisionIPv4Mask_Type(Integer32):
    """Custom type hh3cDot11APProvisionIPv4Mask based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 31),
    )


_Hh3cDot11APProvisionIPv4Mask_Type.__name__ = "Integer32"
_Hh3cDot11APProvisionIPv4Mask_Object = MibTableColumn
hh3cDot11APProvisionIPv4Mask = _Hh3cDot11APProvisionIPv4Mask_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 3, 1, 1, 30),
    _Hh3cDot11APProvisionIPv4Mask_Type()
)
hh3cDot11APProvisionIPv4Mask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDot11APProvisionIPv4Mask.setStatus("current")
_Hh3cDot11APProvisionAPIPv6_Type = OctetString
_Hh3cDot11APProvisionAPIPv6_Object = MibTableColumn
hh3cDot11APProvisionAPIPv6 = _Hh3cDot11APProvisionAPIPv6_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 3, 1, 1, 31),
    _Hh3cDot11APProvisionAPIPv6_Type()
)
hh3cDot11APProvisionAPIPv6.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDot11APProvisionAPIPv6.setStatus("current")


class _Hh3cDot11APProvisionIPv6PrefixLen_Type(Integer32):
    """Custom type hh3cDot11APProvisionIPv6PrefixLen based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 128),
    )


_Hh3cDot11APProvisionIPv6PrefixLen_Type.__name__ = "Integer32"
_Hh3cDot11APProvisionIPv6PrefixLen_Object = MibTableColumn
hh3cDot11APProvisionIPv6PrefixLen = _Hh3cDot11APProvisionIPv6PrefixLen_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 3, 1, 1, 32),
    _Hh3cDot11APProvisionIPv6PrefixLen_Type()
)
hh3cDot11APProvisionIPv6PrefixLen.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDot11APProvisionIPv6PrefixLen.setStatus("current")
_Hh3cDot11APProvisionACIPv4_Type = IpAddress
_Hh3cDot11APProvisionACIPv4_Object = MibTableColumn
hh3cDot11APProvisionACIPv4 = _Hh3cDot11APProvisionACIPv4_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 3, 1, 1, 33),
    _Hh3cDot11APProvisionACIPv4_Type()
)
hh3cDot11APProvisionACIPv4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDot11APProvisionACIPv4.setStatus("current")
_Hh3cDot11APProvisionACIpv6_Type = OctetString
_Hh3cDot11APProvisionACIpv6_Object = MibTableColumn
hh3cDot11APProvisionACIpv6 = _Hh3cDot11APProvisionACIpv6_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 3, 1, 1, 34),
    _Hh3cDot11APProvisionACIpv6_Type()
)
hh3cDot11APProvisionACIpv6.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cDot11APProvisionACIpv6.setStatus("current")
_Hh3cDot11APProvisionGateWayIPV4_Type = IpAddress
_Hh3cDot11APProvisionGateWayIPV4_Object = MibTableColumn
hh3cDot11APProvisionGateWayIPV4 = _Hh3cDot11APProvisionGateWayIPV4_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 3, 1, 1, 35),
    _Hh3cDot11APProvisionGateWayIPV4_Type()
)
hh3cDot11APProvisionGateWayIPV4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDot11APProvisionGateWayIPV4.setStatus("current")
_Hh3cDot11APProvisionGateWayIPV6_Type = OctetString
_Hh3cDot11APProvisionGateWayIPV6_Object = MibTableColumn
hh3cDot11APProvisionGateWayIPV6 = _Hh3cDot11APProvisionGateWayIPV6_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 3, 1, 1, 36),
    _Hh3cDot11APProvisionGateWayIPV6_Type()
)
hh3cDot11APProvisionGateWayIPV6.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cDot11APProvisionGateWayIPV6.setStatus("current")
_Hh3cDot11APMapConfigFileName_Type = OctetString
_Hh3cDot11APMapConfigFileName_Object = MibTableColumn
hh3cDot11APMapConfigFileName = _Hh3cDot11APMapConfigFileName_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 3, 1, 1, 37),
    _Hh3cDot11APMapConfigFileName_Type()
)
hh3cDot11APMapConfigFileName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cDot11APMapConfigFileName.setStatus("current")
_Hh3cDot11RadioToConfigTable_Object = MibTable
hh3cDot11RadioToConfigTable = _Hh3cDot11RadioToConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 3, 2)
)
if mibBuilder.loadTexts:
    hh3cDot11RadioToConfigTable.setStatus("current")
_Hh3cDot11RadioToConfigEntry_Object = MibTableRow
hh3cDot11RadioToConfigEntry = _Hh3cDot11RadioToConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 3, 2, 1)
)
hh3cDot11RadioToConfigEntry.setIndexNames(
    (0, "HH3C-DOT11-CFG-MIB", "hh3cDot11APTemplateNameCfg"),
    (0, "HH3C-DOT11-CFG-MIB", "hh3cDot11CfgRadioID"),
)
if mibBuilder.loadTexts:
    hh3cDot11RadioToConfigEntry.setStatus("current")


class _Hh3cDot11APTemplateNameCfg_Type(OctetString):
    """Custom type hh3cDot11APTemplateNameCfg based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_Hh3cDot11APTemplateNameCfg_Type.__name__ = "OctetString"
_Hh3cDot11APTemplateNameCfg_Object = MibTableColumn
hh3cDot11APTemplateNameCfg = _Hh3cDot11APTemplateNameCfg_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 3, 2, 1, 1),
    _Hh3cDot11APTemplateNameCfg_Type()
)
hh3cDot11APTemplateNameCfg.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cDot11APTemplateNameCfg.setStatus("current")
_Hh3cDot11CfgRadioID_Type = Hh3cDot11RadioScopeType
_Hh3cDot11CfgRadioID_Object = MibTableColumn
hh3cDot11CfgRadioID = _Hh3cDot11CfgRadioID_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 3, 2, 1, 2),
    _Hh3cDot11CfgRadioID_Type()
)
hh3cDot11CfgRadioID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cDot11CfgRadioID.setStatus("current")
_Hh3cDot11CfgRadioPolicyName_Type = OctetString
_Hh3cDot11CfgRadioPolicyName_Object = MibTableColumn
hh3cDot11CfgRadioPolicyName = _Hh3cDot11CfgRadioPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 3, 2, 1, 3),
    _Hh3cDot11CfgRadioPolicyName_Type()
)
hh3cDot11CfgRadioPolicyName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDot11CfgRadioPolicyName.setStatus("current")
_Hh3cDot11CfgRadioType_Type = Hh3cDot11RadioType
_Hh3cDot11CfgRadioType_Object = MibTableColumn
hh3cDot11CfgRadioType = _Hh3cDot11CfgRadioType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 3, 2, 1, 4),
    _Hh3cDot11CfgRadioType_Type()
)
hh3cDot11CfgRadioType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDot11CfgRadioType.setStatus("current")
_Hh3cDot11CfgChannel_Type = Hh3cDot11ChannelScopeType
_Hh3cDot11CfgChannel_Object = MibTableColumn
hh3cDot11CfgChannel = _Hh3cDot11CfgChannel_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 3, 2, 1, 5),
    _Hh3cDot11CfgChannel_Type()
)
hh3cDot11CfgChannel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDot11CfgChannel.setStatus("current")
_Hh3cDot11CfgMaxTxPowerLevel_Type = Hh3cDot11TxPwrLevelScopeType
_Hh3cDot11CfgMaxTxPowerLevel_Object = MibTableColumn
hh3cDot11CfgMaxTxPowerLevel = _Hh3cDot11CfgMaxTxPowerLevel_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 3, 2, 1, 6),
    _Hh3cDot11CfgMaxTxPowerLevel_Type()
)
hh3cDot11CfgMaxTxPowerLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDot11CfgMaxTxPowerLevel.setStatus("current")
if mibBuilder.loadTexts:
    hh3cDot11CfgMaxTxPowerLevel.setUnits("dbm")


class _Hh3cDot11PreambleLen_Type(Hh3cDot11PreambleType):
    """Custom type hh3cDot11PreambleLen based on Hh3cDot11PreambleType"""
    defaultValue = 2


_Hh3cDot11PreambleLen_Type.__name__ = "Hh3cDot11PreambleType"
_Hh3cDot11PreambleLen_Object = MibTableColumn
hh3cDot11PreambleLen = _Hh3cDot11PreambleLen_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 3, 2, 1, 7),
    _Hh3cDot11PreambleLen_Type()
)
hh3cDot11PreambleLen.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDot11PreambleLen.setStatus("current")
_Hh3cDot11CfgRadioStatus_Type = TruthValue
_Hh3cDot11CfgRadioStatus_Object = MibTableColumn
hh3cDot11CfgRadioStatus = _Hh3cDot11CfgRadioStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 3, 2, 1, 8),
    _Hh3cDot11CfgRadioStatus_Type()
)
hh3cDot11CfgRadioStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDot11CfgRadioStatus.setStatus("current")
_Hh3cDot11CfgRdElementID_Type = Unsigned32
_Hh3cDot11CfgRdElementID_Object = MibTableColumn
hh3cDot11CfgRdElementID = _Hh3cDot11CfgRdElementID_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 3, 2, 1, 9),
    _Hh3cDot11CfgRdElementID_Type()
)
hh3cDot11CfgRdElementID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11CfgRdElementID.setStatus("current")
_Hh3cDot11CfgWorkMode_Type = Hh3cDot11WorkMode
_Hh3cDot11CfgWorkMode_Object = MibTableColumn
hh3cDot11CfgWorkMode = _Hh3cDot11CfgWorkMode_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 3, 2, 1, 10),
    _Hh3cDot11CfgWorkMode_Type()
)
hh3cDot11CfgWorkMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDot11CfgWorkMode.setStatus("current")
_Hh3cDot11CfgPwrAttValue_Type = Integer32
_Hh3cDot11CfgPwrAttValue_Object = MibTableColumn
hh3cDot11CfgPwrAttValue = _Hh3cDot11CfgPwrAttValue_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 3, 2, 1, 11),
    _Hh3cDot11CfgPwrAttValue_Type()
)
hh3cDot11CfgPwrAttValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDot11CfgPwrAttValue.setStatus("current")


class _Hh3cDot11RadioTxArithmetic_Type(Integer32):
    """Custom type hh3cDot11RadioTxArithmetic based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("quality", 1),
          ("bandwidth", 2))
    )


_Hh3cDot11RadioTxArithmetic_Type.__name__ = "Integer32"
_Hh3cDot11RadioTxArithmetic_Object = MibTableColumn
hh3cDot11RadioTxArithmetic = _Hh3cDot11RadioTxArithmetic_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 3, 2, 1, 12),
    _Hh3cDot11RadioTxArithmetic_Type()
)
hh3cDot11RadioTxArithmetic.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDot11RadioTxArithmetic.setStatus("current")


class _Hh3cDot11CfgChannelLockStat_Type(Integer32):
    """Custom type hh3cDot11CfgChannelLockStat based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("unlocked", 1),
          ("locked", 2))
    )


_Hh3cDot11CfgChannelLockStat_Type.__name__ = "Integer32"
_Hh3cDot11CfgChannelLockStat_Object = MibTableColumn
hh3cDot11CfgChannelLockStat = _Hh3cDot11CfgChannelLockStat_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 3, 2, 1, 13),
    _Hh3cDot11CfgChannelLockStat_Type()
)
hh3cDot11CfgChannelLockStat.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDot11CfgChannelLockStat.setStatus("current")


class _Hh3cDot11CfgPowerLockStat_Type(Integer32):
    """Custom type hh3cDot11CfgPowerLockStat based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("unlocked", 1),
          ("locked", 2))
    )


_Hh3cDot11CfgPowerLockStat_Type.__name__ = "Integer32"
_Hh3cDot11CfgPowerLockStat_Object = MibTableColumn
hh3cDot11CfgPowerLockStat = _Hh3cDot11CfgPowerLockStat_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 3, 2, 1, 14),
    _Hh3cDot11CfgPowerLockStat_Type()
)
hh3cDot11CfgPowerLockStat.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDot11CfgPowerLockStat.setStatus("current")
_Hh3cDot11CfgLBRdGroupId_Type = Unsigned32
_Hh3cDot11CfgLBRdGroupId_Object = MibTableColumn
hh3cDot11CfgLBRdGroupId = _Hh3cDot11CfgLBRdGroupId_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 3, 2, 1, 15),
    _Hh3cDot11CfgLBRdGroupId_Type()
)
hh3cDot11CfgLBRdGroupId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDot11CfgLBRdGroupId.setStatus("current")
_Hh3cDot11CfgRRMSDRdGroupId_Type = Unsigned32
_Hh3cDot11CfgRRMSDRdGroupId_Object = MibTableColumn
hh3cDot11CfgRRMSDRdGroupId = _Hh3cDot11CfgRRMSDRdGroupId_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 3, 2, 1, 16),
    _Hh3cDot11CfgRRMSDRdGroupId_Type()
)
hh3cDot11CfgRRMSDRdGroupId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDot11CfgRRMSDRdGroupId.setStatus("current")
_Hh3cDot11CfgRadioType2_Type = Hh3cDot11RadioType2
_Hh3cDot11CfgRadioType2_Object = MibTableColumn
hh3cDot11CfgRadioType2 = _Hh3cDot11CfgRadioType2_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 3, 2, 1, 17),
    _Hh3cDot11CfgRadioType2_Type()
)
hh3cDot11CfgRadioType2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDot11CfgRadioType2.setStatus("current")
_Hh3cDot11CfgIDSEnable_Type = TruthValue
_Hh3cDot11CfgIDSEnable_Object = MibTableColumn
hh3cDot11CfgIDSEnable = _Hh3cDot11CfgIDSEnable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 3, 2, 1, 18),
    _Hh3cDot11CfgIDSEnable_Type()
)
hh3cDot11CfgIDSEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDot11CfgIDSEnable.setStatus("current")
_Hh3cDot11CfgSaEnable_Type = TruthValue
_Hh3cDot11CfgSaEnable_Object = MibTableColumn
hh3cDot11CfgSaEnable = _Hh3cDot11CfgSaEnable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 3, 2, 1, 19),
    _Hh3cDot11CfgSaEnable_Type()
)
hh3cDot11CfgSaEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDot11CfgSaEnable.setStatus("current")
_Hh3cDot11CfgSaCltRtFFTData_Type = TruthValue
_Hh3cDot11CfgSaCltRtFFTData_Object = MibTableColumn
hh3cDot11CfgSaCltRtFFTData = _Hh3cDot11CfgSaCltRtFFTData_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 3, 2, 1, 20),
    _Hh3cDot11CfgSaCltRtFFTData_Type()
)
hh3cDot11CfgSaCltRtFFTData.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDot11CfgSaCltRtFFTData.setStatus("current")


class _Hh3cDot11CfgSaBand_Type(Integer32):
    """Custom type hh3cDot11CfgSaBand based on Integer32"""
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
        *(("dot11g", 1),
          ("dot11aLower", 2),
          ("dot11aMiddle", 3),
          ("dot11aUpper", 4))
    )


_Hh3cDot11CfgSaBand_Type.__name__ = "Integer32"
_Hh3cDot11CfgSaBand_Object = MibTableColumn
hh3cDot11CfgSaBand = _Hh3cDot11CfgSaBand_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 3, 2, 1, 21),
    _Hh3cDot11CfgSaBand_Type()
)
hh3cDot11CfgSaBand.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDot11CfgSaBand.setStatus("current")


class _Hh3cDot11CfgSaRptDevType_Type(Bits):
    """Custom type hh3cDot11CfgSaRptDevType based on Bits"""
    namedValues = NamedValues(
        *(("microwave", 0),
          ("microwaveInverter", 1),
          ("bluetooth", 2),
          ("fixedFreqOthers", 3),
          ("fixedFreqCordlessPhone", 4),
          ("fixedFreqVideo", 5),
          ("fixedFreqAudio", 6),
          ("freqHopperOthers", 7),
          ("freqHopperCordlessBase", 8),
          ("freqHopperCordlessNetwork", 9),
          ("freqHopperXbox", 10),
          ("genericInterferer", 11))
    )

_Hh3cDot11CfgSaRptDevType_Type.__name__ = "Bits"
_Hh3cDot11CfgSaRptDevType_Object = MibTableColumn
hh3cDot11CfgSaRptDevType = _Hh3cDot11CfgSaRptDevType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 3, 2, 1, 22),
    _Hh3cDot11CfgSaRptDevType_Type()
)
hh3cDot11CfgSaRptDevType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDot11CfgSaRptDevType.setStatus("current")
_Hh3cDot11CfgSaTrapDevEnable_Type = TruthValue
_Hh3cDot11CfgSaTrapDevEnable_Object = MibTableColumn
hh3cDot11CfgSaTrapDevEnable = _Hh3cDot11CfgSaTrapDevEnable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 3, 2, 1, 23),
    _Hh3cDot11CfgSaTrapDevEnable_Type()
)
hh3cDot11CfgSaTrapDevEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDot11CfgSaTrapDevEnable.setStatus("current")


class _Hh3cDot11CfgSaTrapDevType_Type(Bits):
    """Custom type hh3cDot11CfgSaTrapDevType based on Bits"""
    namedValues = NamedValues(
        *(("microwave", 0),
          ("microwaveInverter", 1),
          ("bluetooth", 2),
          ("fixedFreqOthers", 3),
          ("fixedFreqCordlessPhone", 4),
          ("fixedFreqVideo", 5),
          ("fixedFreqAudio", 6),
          ("freqHopperOthers", 7),
          ("freqHopperCordlessBase", 8),
          ("freqHopperCordlessNetwork", 9),
          ("freqHopperXbox", 10),
          ("genericInterferer", 11))
    )

_Hh3cDot11CfgSaTrapDevType_Type.__name__ = "Bits"
_Hh3cDot11CfgSaTrapDevType_Object = MibTableColumn
hh3cDot11CfgSaTrapDevType = _Hh3cDot11CfgSaTrapDevType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 3, 2, 1, 24),
    _Hh3cDot11CfgSaTrapDevType_Type()
)
hh3cDot11CfgSaTrapDevType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDot11CfgSaTrapDevType.setStatus("current")
_Hh3cDot11CfgSaTrapAQEnable_Type = TruthValue
_Hh3cDot11CfgSaTrapAQEnable_Object = MibTableColumn
hh3cDot11CfgSaTrapAQEnable = _Hh3cDot11CfgSaTrapAQEnable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 3, 2, 1, 25),
    _Hh3cDot11CfgSaTrapAQEnable_Type()
)
hh3cDot11CfgSaTrapAQEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDot11CfgSaTrapAQEnable.setStatus("current")


class _Hh3cDot11CfgSaTrapAQThreshold_Type(Integer32):
    """Custom type hh3cDot11CfgSaTrapAQThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_Hh3cDot11CfgSaTrapAQThreshold_Type.__name__ = "Integer32"
_Hh3cDot11CfgSaTrapAQThreshold_Object = MibTableColumn
hh3cDot11CfgSaTrapAQThreshold = _Hh3cDot11CfgSaTrapAQThreshold_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 3, 2, 1, 26),
    _Hh3cDot11CfgSaTrapAQThreshold_Type()
)
hh3cDot11CfgSaTrapAQThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDot11CfgSaTrapAQThreshold.setStatus("current")
_Hh3cDot11CfgSaDrivenRRMEnable_Type = TruthValue
_Hh3cDot11CfgSaDrivenRRMEnable_Object = MibTableColumn
hh3cDot11CfgSaDrivenRRMEnable = _Hh3cDot11CfgSaDrivenRRMEnable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 3, 2, 1, 27),
    _Hh3cDot11CfgSaDrivenRRMEnable_Type()
)
hh3cDot11CfgSaDrivenRRMEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDot11CfgSaDrivenRRMEnable.setStatus("current")


class _Hh3cDot11CfgSaDrivenRRMSnt_Type(Integer32):
    """Custom type hh3cDot11CfgSaDrivenRRMSnt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("low", 1),
          ("medium", 2),
          ("high", 3))
    )


_Hh3cDot11CfgSaDrivenRRMSnt_Type.__name__ = "Integer32"
_Hh3cDot11CfgSaDrivenRRMSnt_Object = MibTableColumn
hh3cDot11CfgSaDrivenRRMSnt = _Hh3cDot11CfgSaDrivenRRMSnt_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 3, 2, 1, 28),
    _Hh3cDot11CfgSaDrivenRRMSnt_Type()
)
hh3cDot11CfgSaDrivenRRMSnt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDot11CfgSaDrivenRRMSnt.setStatus("current")


class _Hh3cDot11CfgSPInCirMode_Type(Hh3cDot11CirMode):
    """Custom type hh3cDot11CfgSPInCirMode based on Hh3cDot11CirMode"""
    defaultValue = 1


_Hh3cDot11CfgSPInCirMode_Type.__name__ = "Hh3cDot11CirMode"
_Hh3cDot11CfgSPInCirMode_Object = MibTableColumn
hh3cDot11CfgSPInCirMode = _Hh3cDot11CfgSPInCirMode_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 3, 2, 1, 29),
    _Hh3cDot11CfgSPInCirMode_Type()
)
hh3cDot11CfgSPInCirMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cDot11CfgSPInCirMode.setStatus("current")


class _Hh3cDot11CfgSPInCirValue_Type(Integer32):
    """Custom type hh3cDot11CfgSPInCirValue based on Integer32"""
    defaultValue = 0


_Hh3cDot11CfgSPInCirValue_Type.__name__ = "Integer32"
_Hh3cDot11CfgSPInCirValue_Object = MibTableColumn
hh3cDot11CfgSPInCirValue = _Hh3cDot11CfgSPInCirValue_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 3, 2, 1, 30),
    _Hh3cDot11CfgSPInCirValue_Type()
)
hh3cDot11CfgSPInCirValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cDot11CfgSPInCirValue.setStatus("current")
if mibBuilder.loadTexts:
    hh3cDot11CfgSPInCirValue.setUnits("Kbps")


class _Hh3cDot11CfgSPOutCirMode_Type(Hh3cDot11CirMode):
    """Custom type hh3cDot11CfgSPOutCirMode based on Hh3cDot11CirMode"""
    defaultValue = 1


_Hh3cDot11CfgSPOutCirMode_Type.__name__ = "Hh3cDot11CirMode"
_Hh3cDot11CfgSPOutCirMode_Object = MibTableColumn
hh3cDot11CfgSPOutCirMode = _Hh3cDot11CfgSPOutCirMode_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 3, 2, 1, 31),
    _Hh3cDot11CfgSPOutCirMode_Type()
)
hh3cDot11CfgSPOutCirMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cDot11CfgSPOutCirMode.setStatus("current")


class _Hh3cDot11CfgSPOutCirValue_Type(Integer32):
    """Custom type hh3cDot11CfgSPOutCirValue based on Integer32"""
    defaultValue = 0


_Hh3cDot11CfgSPOutCirValue_Type.__name__ = "Integer32"
_Hh3cDot11CfgSPOutCirValue_Object = MibTableColumn
hh3cDot11CfgSPOutCirValue = _Hh3cDot11CfgSPOutCirValue_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 3, 2, 1, 32),
    _Hh3cDot11CfgSPOutCirValue_Type()
)
hh3cDot11CfgSPOutCirValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cDot11CfgSPOutCirValue.setStatus("current")
if mibBuilder.loadTexts:
    hh3cDot11CfgSPOutCirValue.setUnits("Kbps")
_Hh3cDot11APServiceSetTable_Object = MibTable
hh3cDot11APServiceSetTable = _Hh3cDot11APServiceSetTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 3, 3)
)
if mibBuilder.loadTexts:
    hh3cDot11APServiceSetTable.setStatus("current")
_Hh3cDot11APServiceSetEntry_Object = MibTableRow
hh3cDot11APServiceSetEntry = _Hh3cDot11APServiceSetEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 3, 3, 1)
)
hh3cDot11APServiceSetEntry.setIndexNames(
    (0, "HH3C-DOT11-CFG-MIB", "hh3cDot11APTemplateNameCfg"),
    (0, "HH3C-DOT11-CFG-MIB", "hh3cDot11CfgRadioID"),
    (0, "HH3C-DOT11-CFG-MIB", "hh3cDot11CfgServicePolicyID"),
)
if mibBuilder.loadTexts:
    hh3cDot11APServiceSetEntry.setStatus("current")
_Hh3cDot11CfgServicePolicyID_Type = Hh3cDot11ServicePolicyIDType
_Hh3cDot11CfgServicePolicyID_Object = MibTableColumn
hh3cDot11CfgServicePolicyID = _Hh3cDot11CfgServicePolicyID_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 3, 3, 1, 1),
    _Hh3cDot11CfgServicePolicyID_Type()
)
hh3cDot11CfgServicePolicyID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cDot11CfgServicePolicyID.setStatus("current")
_Hh3cDot11SrvSetRowStatus_Type = RowStatus
_Hh3cDot11SrvSetRowStatus_Object = MibTableColumn
hh3cDot11SrvSetRowStatus = _Hh3cDot11SrvSetRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 3, 3, 1, 2),
    _Hh3cDot11SrvSetRowStatus_Type()
)
hh3cDot11SrvSetRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cDot11SrvSetRowStatus.setStatus("current")


class _Hh3cDot11ServiceSetVlanId_Type(Integer32):
    """Custom type hh3cDot11ServiceSetVlanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_Hh3cDot11ServiceSetVlanId_Type.__name__ = "Integer32"
_Hh3cDot11ServiceSetVlanId_Object = MibTableColumn
hh3cDot11ServiceSetVlanId = _Hh3cDot11ServiceSetVlanId_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 3, 3, 1, 3),
    _Hh3cDot11ServiceSetVlanId_Type()
)
hh3cDot11ServiceSetVlanId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cDot11ServiceSetVlanId.setStatus("current")


class _Hh3cDot11ServiceSetVlanGroup_Type(OctetString):
    """Custom type hh3cDot11ServiceSetVlanGroup based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_Hh3cDot11ServiceSetVlanGroup_Type.__name__ = "OctetString"
_Hh3cDot11ServiceSetVlanGroup_Object = MibTableColumn
hh3cDot11ServiceSetVlanGroup = _Hh3cDot11ServiceSetVlanGroup_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 3, 3, 1, 4),
    _Hh3cDot11ServiceSetVlanGroup_Type()
)
hh3cDot11ServiceSetVlanGroup.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cDot11ServiceSetVlanGroup.setStatus("current")
_Hh3cDot11APSysInfoSetTable_Object = MibTable
hh3cDot11APSysInfoSetTable = _Hh3cDot11APSysInfoSetTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 3, 4)
)
if mibBuilder.loadTexts:
    hh3cDot11APSysInfoSetTable.setStatus("current")
_Hh3cDot11APSysInfoSetEntry_Object = MibTableRow
hh3cDot11APSysInfoSetEntry = _Hh3cDot11APSysInfoSetEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 3, 4, 1)
)
hh3cDot11APSysInfoSetEntry.setIndexNames(
    (0, "HH3C-DOT11-CFG-MIB", "hh3cDot11SIDAPSerialID"),
)
if mibBuilder.loadTexts:
    hh3cDot11APSysInfoSetEntry.setStatus("current")


class _Hh3cDot11APSysNetID_Type(OctetString):
    """Custom type hh3cDot11APSysNetID based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_Hh3cDot11APSysNetID_Type.__name__ = "OctetString"
_Hh3cDot11APSysNetID_Object = MibTableColumn
hh3cDot11APSysNetID = _Hh3cDot11APSysNetID_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 3, 4, 1, 1),
    _Hh3cDot11APSysNetID_Type()
)
hh3cDot11APSysNetID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDot11APSysNetID.setStatus("current")


class _Hh3cDot11APCpuUsageThreshold_Type(Integer32):
    """Custom type hh3cDot11APCpuUsageThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Hh3cDot11APCpuUsageThreshold_Type.__name__ = "Integer32"
_Hh3cDot11APCpuUsageThreshold_Object = MibTableColumn
hh3cDot11APCpuUsageThreshold = _Hh3cDot11APCpuUsageThreshold_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 3, 4, 1, 2),
    _Hh3cDot11APCpuUsageThreshold_Type()
)
hh3cDot11APCpuUsageThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDot11APCpuUsageThreshold.setStatus("current")
if mibBuilder.loadTexts:
    hh3cDot11APCpuUsageThreshold.setUnits("onepercent")


class _Hh3cDot11APMemUsageThreshold_Type(Integer32):
    """Custom type hh3cDot11APMemUsageThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Hh3cDot11APMemUsageThreshold_Type.__name__ = "Integer32"
_Hh3cDot11APMemUsageThreshold_Object = MibTableColumn
hh3cDot11APMemUsageThreshold = _Hh3cDot11APMemUsageThreshold_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 3, 4, 1, 3),
    _Hh3cDot11APMemUsageThreshold_Type()
)
hh3cDot11APMemUsageThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDot11APMemUsageThreshold.setStatus("current")
if mibBuilder.loadTexts:
    hh3cDot11APMemUsageThreshold.setUnits("onepercent")
_Hh3cDot11APLimitTable_Object = MibTable
hh3cDot11APLimitTable = _Hh3cDot11APLimitTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 3, 5)
)
if mibBuilder.loadTexts:
    hh3cDot11APLimitTable.setStatus("current")
_Hh3cDot11APLimitEntry_Object = MibTableRow
hh3cDot11APLimitEntry = _Hh3cDot11APLimitEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 3, 5, 1)
)
hh3cDot11APLimitEntry.setIndexNames(
    (0, "HH3C-DOT11-REF-MIB", "hh3cDot11APElementIndex"),
)
if mibBuilder.loadTexts:
    hh3cDot11APLimitEntry.setStatus("current")


class _Hh3cDot11APSsidNumLimit_Type(Integer32):
    """Custom type hh3cDot11APSsidNumLimit based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Hh3cDot11APSsidNumLimit_Type.__name__ = "Integer32"
_Hh3cDot11APSsidNumLimit_Object = MibTableColumn
hh3cDot11APSsidNumLimit = _Hh3cDot11APSsidNumLimit_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 3, 5, 1, 1),
    _Hh3cDot11APSsidNumLimit_Type()
)
hh3cDot11APSsidNumLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDot11APSsidNumLimit.setStatus("current")


class _Hh3cDot11APUserCntLimit_Type(Integer32):
    """Custom type hh3cDot11APUserCntLimit based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Hh3cDot11APUserCntLimit_Type.__name__ = "Integer32"
_Hh3cDot11APUserCntLimit_Object = MibTableColumn
hh3cDot11APUserCntLimit = _Hh3cDot11APUserCntLimit_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 3, 5, 1, 2),
    _Hh3cDot11APUserCntLimit_Type()
)
hh3cDot11APUserCntLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDot11APUserCntLimit.setStatus("current")


class _Hh3cDot11APUserThreshold_Type(Integer32):
    """Custom type hh3cDot11APUserThreshold based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Hh3cDot11APUserThreshold_Type.__name__ = "Integer32"
_Hh3cDot11APUserThreshold_Object = MibTableColumn
hh3cDot11APUserThreshold = _Hh3cDot11APUserThreshold_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 3, 5, 1, 3),
    _Hh3cDot11APUserThreshold_Type()
)
hh3cDot11APUserThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDot11APUserThreshold.setStatus("current")
_Hh3cDot11APIfSetTable_Object = MibTable
hh3cDot11APIfSetTable = _Hh3cDot11APIfSetTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 3, 6)
)
if mibBuilder.loadTexts:
    hh3cDot11APIfSetTable.setStatus("current")
_Hh3cDot11APIfSetEntry_Object = MibTableRow
hh3cDot11APIfSetEntry = _Hh3cDot11APIfSetEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 3, 6, 1)
)
hh3cDot11APIfSetEntry.setIndexNames(
    (0, "HH3C-DOT11-REF-MIB", "hh3cDot11APElementIndex"),
    (0, "HH3C-DOT11-CFG-MIB", "hh3cDot11APSetIfIndex"),
)
if mibBuilder.loadTexts:
    hh3cDot11APIfSetEntry.setStatus("current")
_Hh3cDot11APSetIfIndex_Type = Integer32
_Hh3cDot11APSetIfIndex_Object = MibTableColumn
hh3cDot11APSetIfIndex = _Hh3cDot11APSetIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 3, 6, 1, 1),
    _Hh3cDot11APSetIfIndex_Type()
)
hh3cDot11APSetIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cDot11APSetIfIndex.setStatus("current")
_Hh3cDot11APIfAlias_Type = DisplayString
_Hh3cDot11APIfAlias_Object = MibTableColumn
hh3cDot11APIfAlias = _Hh3cDot11APIfAlias_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 3, 6, 1, 2),
    _Hh3cDot11APIfAlias_Type()
)
hh3cDot11APIfAlias.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDot11APIfAlias.setStatus("current")
_Hh3cDot11APServiceVlanTable_Object = MibTable
hh3cDot11APServiceVlanTable = _Hh3cDot11APServiceVlanTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 3, 7)
)
if mibBuilder.loadTexts:
    hh3cDot11APServiceVlanTable.setStatus("current")
_Hh3cDot11APServiceVlanEntry_Object = MibTableRow
hh3cDot11APServiceVlanEntry = _Hh3cDot11APServiceVlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 3, 7, 1)
)
hh3cDot11APServiceVlanEntry.setIndexNames(
    (0, "HH3C-DOT11-CFG-MIB", "hh3cDot11APServiceVlanSerialID"),
    (0, "HH3C-DOT11-CFG-MIB", "hh3cDot11APServiceVlanSPID"),
)
if mibBuilder.loadTexts:
    hh3cDot11APServiceVlanEntry.setStatus("current")
_Hh3cDot11APServiceVlanSerialID_Type = OctetString
_Hh3cDot11APServiceVlanSerialID_Object = MibTableColumn
hh3cDot11APServiceVlanSerialID = _Hh3cDot11APServiceVlanSerialID_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 3, 7, 1, 1),
    _Hh3cDot11APServiceVlanSerialID_Type()
)
hh3cDot11APServiceVlanSerialID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cDot11APServiceVlanSerialID.setStatus("current")
_Hh3cDot11APServiceVlanSPID_Type = Hh3cDot11ServicePolicyIDType
_Hh3cDot11APServiceVlanSPID_Object = MibTableColumn
hh3cDot11APServiceVlanSPID = _Hh3cDot11APServiceVlanSPID_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 3, 7, 1, 2),
    _Hh3cDot11APServiceVlanSPID_Type()
)
hh3cDot11APServiceVlanSPID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cDot11APServiceVlanSPID.setStatus("current")


class _Hh3cDot11APServiceVlanId_Type(Integer32):
    """Custom type hh3cDot11APServiceVlanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_Hh3cDot11APServiceVlanId_Type.__name__ = "Integer32"
_Hh3cDot11APServiceVlanId_Object = MibTableColumn
hh3cDot11APServiceVlanId = _Hh3cDot11APServiceVlanId_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 3, 7, 1, 3),
    _Hh3cDot11APServiceVlanId_Type()
)
hh3cDot11APServiceVlanId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cDot11APServiceVlanId.setStatus("current")
_Hh3cDot11APServiceVlanRowStatus_Type = RowStatus
_Hh3cDot11APServiceVlanRowStatus_Object = MibTableColumn
hh3cDot11APServiceVlanRowStatus = _Hh3cDot11APServiceVlanRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 3, 7, 1, 4),
    _Hh3cDot11APServiceVlanRowStatus_Type()
)
hh3cDot11APServiceVlanRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cDot11APServiceVlanRowStatus.setStatus("current")
_Hh3cDot11RadioConfigTable_Object = MibTable
hh3cDot11RadioConfigTable = _Hh3cDot11RadioConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 3, 8)
)
if mibBuilder.loadTexts:
    hh3cDot11RadioConfigTable.setStatus("current")
_Hh3cDot11RadioConfigEntry_Object = MibTableRow
hh3cDot11RadioConfigEntry = _Hh3cDot11RadioConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 3, 8, 1)
)
hh3cDot11RadioConfigEntry.setIndexNames(
    (0, "HH3C-DOT11-CFG-MIB", "hh3cDot11RCAPSerialID"),
    (0, "HH3C-DOT11-CFG-MIB", "hh3cDot11RCRadioID"),
)
if mibBuilder.loadTexts:
    hh3cDot11RadioConfigEntry.setStatus("current")


class _Hh3cDot11RCAPSerialID_Type(OctetString):
    """Custom type hh3cDot11RCAPSerialID based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_Hh3cDot11RCAPSerialID_Type.__name__ = "OctetString"
_Hh3cDot11RCAPSerialID_Object = MibTableColumn
hh3cDot11RCAPSerialID = _Hh3cDot11RCAPSerialID_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 3, 8, 1, 1),
    _Hh3cDot11RCAPSerialID_Type()
)
hh3cDot11RCAPSerialID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cDot11RCAPSerialID.setStatus("current")
_Hh3cDot11RCRadioID_Type = Hh3cDot11RadioScopeType
_Hh3cDot11RCRadioID_Object = MibTableColumn
hh3cDot11RCRadioID = _Hh3cDot11RCRadioID_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 3, 8, 1, 2),
    _Hh3cDot11RCRadioID_Type()
)
hh3cDot11RCRadioID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cDot11RCRadioID.setStatus("current")
_Hh3cDot11RCRadioType_Type = Hh3cDot11RadioType
_Hh3cDot11RCRadioType_Object = MibTableColumn
hh3cDot11RCRadioType = _Hh3cDot11RCRadioType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 3, 8, 1, 3),
    _Hh3cDot11RCRadioType_Type()
)
hh3cDot11RCRadioType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDot11RCRadioType.setStatus("current")
_Hh3cDot11RCChannel_Type = Hh3cDot11ChannelScopeType
_Hh3cDot11RCChannel_Object = MibTableColumn
hh3cDot11RCChannel = _Hh3cDot11RCChannel_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 3, 8, 1, 4),
    _Hh3cDot11RCChannel_Type()
)
hh3cDot11RCChannel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDot11RCChannel.setStatus("current")


class _Hh3cDot11RCPreambleLen_Type(Hh3cDot11PreambleType):
    """Custom type hh3cDot11RCPreambleLen based on Hh3cDot11PreambleType"""
    defaultValue = 2


_Hh3cDot11RCPreambleLen_Type.__name__ = "Hh3cDot11PreambleType"
_Hh3cDot11RCPreambleLen_Object = MibTableColumn
hh3cDot11RCPreambleLen = _Hh3cDot11RCPreambleLen_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 3, 8, 1, 5),
    _Hh3cDot11RCPreambleLen_Type()
)
hh3cDot11RCPreambleLen.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDot11RCPreambleLen.setStatus("current")
_Hh3cDot11RCPwrAttValue_Type = Integer32
_Hh3cDot11RCPwrAttValue_Object = MibTableColumn
hh3cDot11RCPwrAttValue = _Hh3cDot11RCPwrAttValue_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 3, 8, 1, 6),
    _Hh3cDot11RCPwrAttValue_Type()
)
hh3cDot11RCPwrAttValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDot11RCPwrAttValue.setStatus("current")
_Hh3cDot11RCApPowerLevel_Type = Hh3cDot11TxPwrLevelScopeType
_Hh3cDot11RCApPowerLevel_Object = MibTableColumn
hh3cDot11RCApPowerLevel = _Hh3cDot11RCApPowerLevel_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 3, 8, 1, 7),
    _Hh3cDot11RCApPowerLevel_Type()
)
hh3cDot11RCApPowerLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDot11RCApPowerLevel.setStatus("current")
if mibBuilder.loadTexts:
    hh3cDot11RCApPowerLevel.setUnits("dbm")
_Hh3cDot11RCDynamicChlState_Type = TruthValue
_Hh3cDot11RCDynamicChlState_Object = MibTableColumn
hh3cDot11RCDynamicChlState = _Hh3cDot11RCDynamicChlState_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 3, 8, 1, 8),
    _Hh3cDot11RCDynamicChlState_Type()
)
hh3cDot11RCDynamicChlState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDot11RCDynamicChlState.setStatus("current")
_Hh3cDot11RCDynamicPowerState_Type = TruthValue
_Hh3cDot11RCDynamicPowerState_Object = MibTableColumn
hh3cDot11RCDynamicPowerState = _Hh3cDot11RCDynamicPowerState_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 3, 8, 1, 9),
    _Hh3cDot11RCDynamicPowerState_Type()
)
hh3cDot11RCDynamicPowerState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDot11RCDynamicPowerState.setStatus("current")
_Hh3cDot11RCRadioStatus_Type = TruthValue
_Hh3cDot11RCRadioStatus_Object = MibTableColumn
hh3cDot11RCRadioStatus = _Hh3cDot11RCRadioStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 3, 8, 1, 10),
    _Hh3cDot11RCRadioStatus_Type()
)
hh3cDot11RCRadioStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDot11RCRadioStatus.setStatus("current")


class _Hh3cDot11RCRadioRate_Type(OctetString):
    """Custom type hh3cDot11RCRadioRate based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_Hh3cDot11RCRadioRate_Type.__name__ = "OctetString"
_Hh3cDot11RCRadioRate_Object = MibTableColumn
hh3cDot11RCRadioRate = _Hh3cDot11RCRadioRate_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 3, 8, 1, 11),
    _Hh3cDot11RCRadioRate_Type()
)
hh3cDot11RCRadioRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDot11RCRadioRate.setStatus("current")
_Hh3cDot11RCPwrAdjustStepLength_Type = Integer32
_Hh3cDot11RCPwrAdjustStepLength_Object = MibTableColumn
hh3cDot11RCPwrAdjustStepLength = _Hh3cDot11RCPwrAdjustStepLength_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 3, 8, 1, 12),
    _Hh3cDot11RCPwrAdjustStepLength_Type()
)
hh3cDot11RCPwrAdjustStepLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11RCPwrAdjustStepLength.setStatus("current")
_Hh3cDot11RCRadioType2_Type = Hh3cDot11RadioType2
_Hh3cDot11RCRadioType2_Object = MibTableColumn
hh3cDot11RCRadioType2 = _Hh3cDot11RCRadioType2_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 3, 8, 1, 13),
    _Hh3cDot11RCRadioType2_Type()
)
hh3cDot11RCRadioType2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDot11RCRadioType2.setStatus("current")


class _Hh3cDot11RCPreambleLenCM_Type(Integer32):
    """Custom type hh3cDot11RCPreambleLenCM based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("long", 0),
          ("short", 1))
    )


_Hh3cDot11RCPreambleLenCM_Type.__name__ = "Integer32"
_Hh3cDot11RCPreambleLenCM_Object = MibTableColumn
hh3cDot11RCPreambleLenCM = _Hh3cDot11RCPreambleLenCM_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 3, 8, 1, 14),
    _Hh3cDot11RCPreambleLenCM_Type()
)
hh3cDot11RCPreambleLenCM.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDot11RCPreambleLenCM.setStatus("current")


class _Hh3cDot11RCDynamicChlStateCM_Type(Integer32):
    """Custom type hh3cDot11RCDynamicChlStateCM based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_Hh3cDot11RCDynamicChlStateCM_Type.__name__ = "Integer32"
_Hh3cDot11RCDynamicChlStateCM_Object = MibTableColumn
hh3cDot11RCDynamicChlStateCM = _Hh3cDot11RCDynamicChlStateCM_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 3, 8, 1, 15),
    _Hh3cDot11RCDynamicChlStateCM_Type()
)
hh3cDot11RCDynamicChlStateCM.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDot11RCDynamicChlStateCM.setStatus("current")


class _Hh3cDot11RCRadioStatusCM_Type(Integer32):
    """Custom type hh3cDot11RCRadioStatusCM based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("up", 1),
          ("down", 2),
          ("testing", 3))
    )


_Hh3cDot11RCRadioStatusCM_Type.__name__ = "Integer32"
_Hh3cDot11RCRadioStatusCM_Object = MibTableColumn
hh3cDot11RCRadioStatusCM = _Hh3cDot11RCRadioStatusCM_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 3, 8, 1, 16),
    _Hh3cDot11RCRadioStatusCM_Type()
)
hh3cDot11RCRadioStatusCM.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDot11RCRadioStatusCM.setStatus("current")


class _Hh3cDot11RCRadioRateCM_Type(OctetString):
    """Custom type hh3cDot11RCRadioRateCM based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_Hh3cDot11RCRadioRateCM_Type.__name__ = "OctetString"
_Hh3cDot11RCRadioRateCM_Object = MibTableColumn
hh3cDot11RCRadioRateCM = _Hh3cDot11RCRadioRateCM_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 3, 8, 1, 17),
    _Hh3cDot11RCRadioRateCM_Type()
)
hh3cDot11RCRadioRateCM.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDot11RCRadioRateCM.setStatus("current")
_Hh3cDot11RCDynamicPowerStateCM_Type = Hh3cDot11TruthValueCM
_Hh3cDot11RCDynamicPowerStateCM_Object = MibTableColumn
hh3cDot11RCDynamicPowerStateCM = _Hh3cDot11RCDynamicPowerStateCM_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 3, 8, 1, 18),
    _Hh3cDot11RCDynamicPowerStateCM_Type()
)
hh3cDot11RCDynamicPowerStateCM.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDot11RCDynamicPowerStateCM.setStatus("current")


class _Hh3cDot11RCRssiThresholdCM_Type(Integer32):
    """Custom type hh3cDot11RCRssiThresholdCM based on Integer32"""
    defaultValue = 1


_Hh3cDot11RCRssiThresholdCM_Type.__name__ = "Integer32"
_Hh3cDot11RCRssiThresholdCM_Object = MibTableColumn
hh3cDot11RCRssiThresholdCM = _Hh3cDot11RCRssiThresholdCM_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 3, 8, 1, 19),
    _Hh3cDot11RCRssiThresholdCM_Type()
)
hh3cDot11RCRssiThresholdCM.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDot11RCRssiThresholdCM.setStatus("current")
if mibBuilder.loadTexts:
    hh3cDot11RCRssiThresholdCM.setUnits("dBm")
_Hh3cDot11RCDynamicChlStateSelfDecisiveCM_Type = Hh3cDot11TruthValueCM
_Hh3cDot11RCDynamicChlStateSelfDecisiveCM_Object = MibTableColumn
hh3cDot11RCDynamicChlStateSelfDecisiveCM = _Hh3cDot11RCDynamicChlStateSelfDecisiveCM_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 3, 8, 1, 20),
    _Hh3cDot11RCDynamicChlStateSelfDecisiveCM_Type()
)
hh3cDot11RCDynamicChlStateSelfDecisiveCM.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDot11RCDynamicChlStateSelfDecisiveCM.setStatus("current")
_Hh3cDot11RCDynamicPowerStateSelfDecisiveCM_Type = Hh3cDot11TruthValueCM
_Hh3cDot11RCDynamicPowerStateSelfDecisiveCM_Object = MibTableColumn
hh3cDot11RCDynamicPowerStateSelfDecisiveCM = _Hh3cDot11RCDynamicPowerStateSelfDecisiveCM_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 3, 8, 1, 21),
    _Hh3cDot11RCDynamicPowerStateSelfDecisiveCM_Type()
)
hh3cDot11RCDynamicPowerStateSelfDecisiveCM.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDot11RCDynamicPowerStateSelfDecisiveCM.setStatus("current")
_Hh3cDot11RadioSSIDCfgTable_Object = MibTable
hh3cDot11RadioSSIDCfgTable = _Hh3cDot11RadioSSIDCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 3, 9)
)
if mibBuilder.loadTexts:
    hh3cDot11RadioSSIDCfgTable.setStatus("current")
_Hh3cDot11RadioSSIDCfgEntry_Object = MibTableRow
hh3cDot11RadioSSIDCfgEntry = _Hh3cDot11RadioSSIDCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 3, 9, 1)
)
hh3cDot11RadioSSIDCfgEntry.setIndexNames(
    (0, "HH3C-DOT11-CFG-MIB", "hh3cDot11RadioSSIDSerialID"),
    (0, "HH3C-DOT11-CFG-MIB", "hh3cDot11RadioSSIDRadioID"),
    (0, "HH3C-DOT11-CFG-MIB", "hh3cDot11RadioSSIDWLANID"),
)
if mibBuilder.loadTexts:
    hh3cDot11RadioSSIDCfgEntry.setStatus("current")
_Hh3cDot11RadioSSIDSerialID_Type = Hh3cDot11ObjectIDType
_Hh3cDot11RadioSSIDSerialID_Object = MibTableColumn
hh3cDot11RadioSSIDSerialID = _Hh3cDot11RadioSSIDSerialID_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 3, 9, 1, 1),
    _Hh3cDot11RadioSSIDSerialID_Type()
)
hh3cDot11RadioSSIDSerialID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cDot11RadioSSIDSerialID.setStatus("current")
_Hh3cDot11RadioSSIDRadioID_Type = Hh3cDot11RadioScopeType
_Hh3cDot11RadioSSIDRadioID_Object = MibTableColumn
hh3cDot11RadioSSIDRadioID = _Hh3cDot11RadioSSIDRadioID_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 3, 9, 1, 2),
    _Hh3cDot11RadioSSIDRadioID_Type()
)
hh3cDot11RadioSSIDRadioID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cDot11RadioSSIDRadioID.setStatus("current")
_Hh3cDot11RadioSSIDWLANID_Type = Integer32
_Hh3cDot11RadioSSIDWLANID_Object = MibTableColumn
hh3cDot11RadioSSIDWLANID = _Hh3cDot11RadioSSIDWLANID_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 3, 9, 1, 3),
    _Hh3cDot11RadioSSIDWLANID_Type()
)
hh3cDot11RadioSSIDWLANID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cDot11RadioSSIDWLANID.setStatus("current")
_Hh3cDot11RadioSSIDIndex_Type = Hh3cDot11ServicePolicyIDType
_Hh3cDot11RadioSSIDIndex_Object = MibTableColumn
hh3cDot11RadioSSIDIndex = _Hh3cDot11RadioSSIDIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 3, 9, 1, 4),
    _Hh3cDot11RadioSSIDIndex_Type()
)
hh3cDot11RadioSSIDIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cDot11RadioSSIDIndex.setStatus("current")
_Hh3cDot11RadioBSSID_Type = MacAddress
_Hh3cDot11RadioBSSID_Object = MibTableColumn
hh3cDot11RadioBSSID = _Hh3cDot11RadioBSSID_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 3, 9, 1, 5),
    _Hh3cDot11RadioBSSID_Type()
)
hh3cDot11RadioBSSID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11RadioBSSID.setStatus("current")
_Hh3cDot11RadioSSIDRowStatus_Type = RowStatus
_Hh3cDot11RadioSSIDRowStatus_Object = MibTableColumn
hh3cDot11RadioSSIDRowStatus = _Hh3cDot11RadioSSIDRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 3, 9, 1, 6),
    _Hh3cDot11RadioSSIDRowStatus_Type()
)
hh3cDot11RadioSSIDRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cDot11RadioSSIDRowStatus.setStatus("current")
_Hh3cDot11APSerialIDTable_Object = MibTable
hh3cDot11APSerialIDTable = _Hh3cDot11APSerialIDTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 3, 10)
)
if mibBuilder.loadTexts:
    hh3cDot11APSerialIDTable.setStatus("current")
_Hh3cDot11APSerialIDEntry_Object = MibTableRow
hh3cDot11APSerialIDEntry = _Hh3cDot11APSerialIDEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 3, 10, 1)
)
hh3cDot11APSerialIDEntry.setIndexNames(
    (0, "HH3C-DOT11-CFG-MIB", "hh3cDot11SIDAPSerialID"),
)
if mibBuilder.loadTexts:
    hh3cDot11APSerialIDEntry.setStatus("current")
_Hh3cDot11SIDAPSerialID_Type = OctetString
_Hh3cDot11SIDAPSerialID_Object = MibTableColumn
hh3cDot11SIDAPSerialID = _Hh3cDot11SIDAPSerialID_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 3, 10, 1, 1),
    _Hh3cDot11SIDAPSerialID_Type()
)
hh3cDot11SIDAPSerialID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cDot11SIDAPSerialID.setStatus("current")


class _Hh3cDot11SIDAPWorkMode_Type(Integer32):
    """Custom type hh3cDot11SIDAPWorkMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("normal", 1),
          ("monitor", 2),
          ("hybrid", 3))
    )


_Hh3cDot11SIDAPWorkMode_Type.__name__ = "Integer32"
_Hh3cDot11SIDAPWorkMode_Object = MibTableColumn
hh3cDot11SIDAPWorkMode = _Hh3cDot11SIDAPWorkMode_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 3, 10, 1, 2),
    _Hh3cDot11SIDAPWorkMode_Type()
)
hh3cDot11SIDAPWorkMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cDot11SIDAPWorkMode.setStatus("current")


class _Hh3cDot11SIDAPGetIPMethod_Type(Integer32):
    """Custom type hh3cDot11SIDAPGetIPMethod based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dhcpAlloc", 1),
          ("static", 2))
    )


_Hh3cDot11SIDAPGetIPMethod_Type.__name__ = "Integer32"
_Hh3cDot11SIDAPGetIPMethod_Object = MibTableColumn
hh3cDot11SIDAPGetIPMethod = _Hh3cDot11SIDAPGetIPMethod_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 3, 10, 1, 3),
    _Hh3cDot11SIDAPGetIPMethod_Type()
)
hh3cDot11SIDAPGetIPMethod.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cDot11SIDAPGetIPMethod.setStatus("current")
_Hh3cDot11SIDAPTemplateName_Type = OctetString
_Hh3cDot11SIDAPTemplateName_Object = MibTableColumn
hh3cDot11SIDAPTemplateName = _Hh3cDot11SIDAPTemplateName_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 3, 10, 1, 4),
    _Hh3cDot11SIDAPTemplateName_Type()
)
hh3cDot11SIDAPTemplateName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cDot11SIDAPTemplateName.setStatus("current")
_Hh3cDot11SIDModelAlias_Type = OctetString
_Hh3cDot11SIDModelAlias_Object = MibTableColumn
hh3cDot11SIDModelAlias = _Hh3cDot11SIDModelAlias_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 3, 10, 1, 5),
    _Hh3cDot11SIDModelAlias_Type()
)
hh3cDot11SIDModelAlias.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cDot11SIDModelAlias.setStatus("current")
_Hh3cDot11SIDAPDescription_Type = OctetString
_Hh3cDot11SIDAPDescription_Object = MibTableColumn
hh3cDot11SIDAPDescription = _Hh3cDot11SIDAPDescription_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 3, 10, 1, 6),
    _Hh3cDot11SIDAPDescription_Type()
)
hh3cDot11SIDAPDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cDot11SIDAPDescription.setStatus("current")
_Hh3cDot11SIDRowStatus_Type = RowStatus
_Hh3cDot11SIDRowStatus_Object = MibTableColumn
hh3cDot11SIDRowStatus = _Hh3cDot11SIDRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 3, 10, 1, 7),
    _Hh3cDot11SIDRowStatus_Type()
)
hh3cDot11SIDRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cDot11SIDRowStatus.setStatus("current")
_Hh3cDot11SIDAPName_Type = OctetString
_Hh3cDot11SIDAPName_Object = MibTableColumn
hh3cDot11SIDAPName = _Hh3cDot11SIDAPName_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 3, 10, 1, 8),
    _Hh3cDot11SIDAPName_Type()
)
hh3cDot11SIDAPName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cDot11SIDAPName.setStatus("current")
_Hh3cDot11SIDStatisInterv_Type = Integer32
_Hh3cDot11SIDStatisInterv_Object = MibTableColumn
hh3cDot11SIDStatisInterv = _Hh3cDot11SIDStatisInterv_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 3, 10, 1, 9),
    _Hh3cDot11SIDStatisInterv_Type()
)
hh3cDot11SIDStatisInterv.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cDot11SIDStatisInterv.setStatus("current")
if mibBuilder.loadTexts:
    hh3cDot11SIDStatisInterv.setUnits("second")


class _Hh3cDot11SIDAPBroadcastProbeReply_Type(TruthValue):
    """Custom type hh3cDot11SIDAPBroadcastProbeReply based on TruthValue"""
    defaultValue = 1


_Hh3cDot11SIDAPBroadcastProbeReply_Type.__name__ = "TruthValue"
_Hh3cDot11SIDAPBroadcastProbeReply_Object = MibTableColumn
hh3cDot11SIDAPBroadcastProbeReply = _Hh3cDot11SIDAPBroadcastProbeReply_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 3, 10, 1, 10),
    _Hh3cDot11SIDAPBroadcastProbeReply_Type()
)
hh3cDot11SIDAPBroadcastProbeReply.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cDot11SIDAPBroadcastProbeReply.setStatus("current")
_Hh3cDot11SIDAPStaIdleTimerInterv_Type = Integer32
_Hh3cDot11SIDAPStaIdleTimerInterv_Object = MibTableColumn
hh3cDot11SIDAPStaIdleTimerInterv = _Hh3cDot11SIDAPStaIdleTimerInterv_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 3, 10, 1, 11),
    _Hh3cDot11SIDAPStaIdleTimerInterv_Type()
)
hh3cDot11SIDAPStaIdleTimerInterv.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cDot11SIDAPStaIdleTimerInterv.setStatus("current")
if mibBuilder.loadTexts:
    hh3cDot11SIDAPStaIdleTimerInterv.setUnits("second")
_Hh3cDot11SIDStaKeepAliveTimerInterv_Type = Integer32
_Hh3cDot11SIDStaKeepAliveTimerInterv_Object = MibTableColumn
hh3cDot11SIDStaKeepAliveTimerInterv = _Hh3cDot11SIDStaKeepAliveTimerInterv_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 3, 10, 1, 12),
    _Hh3cDot11SIDStaKeepAliveTimerInterv_Type()
)
hh3cDot11SIDStaKeepAliveTimerInterv.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cDot11SIDStaKeepAliveTimerInterv.setStatus("current")
if mibBuilder.loadTexts:
    hh3cDot11SIDStaKeepAliveTimerInterv.setUnits("second")
_Hh3cDot11SIDAPCir_Type = Integer32
_Hh3cDot11SIDAPCir_Object = MibTableColumn
hh3cDot11SIDAPCir = _Hh3cDot11SIDAPCir_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 3, 10, 1, 13),
    _Hh3cDot11SIDAPCir_Type()
)
hh3cDot11SIDAPCir.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cDot11SIDAPCir.setStatus("current")
if mibBuilder.loadTexts:
    hh3cDot11SIDAPCir.setUnits("Kbps")
_Hh3cDot11SIDAPCbs_Type = Integer32
_Hh3cDot11SIDAPCbs_Object = MibTableColumn
hh3cDot11SIDAPCbs = _Hh3cDot11SIDAPCbs_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 3, 10, 1, 14),
    _Hh3cDot11SIDAPCbs_Type()
)
hh3cDot11SIDAPCbs.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cDot11SIDAPCbs.setStatus("current")
if mibBuilder.loadTexts:
    hh3cDot11SIDAPCbs.setUnits("Bytes")


class _Hh3cDot11SIDAPPriorityLevel_Type(Integer32):
    """Custom type hh3cDot11SIDAPPriorityLevel based on Integer32"""
    defaultValue = 4

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_Hh3cDot11SIDAPPriorityLevel_Type.__name__ = "Integer32"
_Hh3cDot11SIDAPPriorityLevel_Object = MibTableColumn
hh3cDot11SIDAPPriorityLevel = _Hh3cDot11SIDAPPriorityLevel_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 3, 10, 1, 15),
    _Hh3cDot11SIDAPPriorityLevel_Type()
)
hh3cDot11SIDAPPriorityLevel.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cDot11SIDAPPriorityLevel.setStatus("current")
_Hh3cDot11SIDAPElementID_Type = Integer32
_Hh3cDot11SIDAPElementID_Object = MibTableColumn
hh3cDot11SIDAPElementID = _Hh3cDot11SIDAPElementID_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 3, 10, 1, 16),
    _Hh3cDot11SIDAPElementID_Type()
)
hh3cDot11SIDAPElementID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11SIDAPElementID.setStatus("current")


class _Hh3cDot11SIDAPDevDetectEnable_Type(TruthValue):
    """Custom type hh3cDot11SIDAPDevDetectEnable based on TruthValue"""
    defaultValue = 2


_Hh3cDot11SIDAPDevDetectEnable_Type.__name__ = "TruthValue"
_Hh3cDot11SIDAPDevDetectEnable_Object = MibTableColumn
hh3cDot11SIDAPDevDetectEnable = _Hh3cDot11SIDAPDevDetectEnable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 3, 10, 1, 17),
    _Hh3cDot11SIDAPDevDetectEnable_Type()
)
hh3cDot11SIDAPDevDetectEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cDot11SIDAPDevDetectEnable.setStatus("current")


class _Hh3cDot11SIDAPStatisIntervMode_Type(Integer32):
    """Custom type hh3cDot11SIDAPStatisIntervMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("normal", 1),
          ("realtime", 2))
    )


_Hh3cDot11SIDAPStatisIntervMode_Type.__name__ = "Integer32"
_Hh3cDot11SIDAPStatisIntervMode_Object = MibTableColumn
hh3cDot11SIDAPStatisIntervMode = _Hh3cDot11SIDAPStatisIntervMode_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 3, 10, 1, 18),
    _Hh3cDot11SIDAPStatisIntervMode_Type()
)
hh3cDot11SIDAPStatisIntervMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cDot11SIDAPStatisIntervMode.setStatus("current")


class _Hh3cDot11SIDAPWorkModeCM_Type(Integer32):
    """Custom type hh3cDot11SIDAPWorkModeCM based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("normal", 0),
          ("monitor", 1),
          ("semimonitor", 2))
    )


_Hh3cDot11SIDAPWorkModeCM_Type.__name__ = "Integer32"
_Hh3cDot11SIDAPWorkModeCM_Object = MibTableColumn
hh3cDot11SIDAPWorkModeCM = _Hh3cDot11SIDAPWorkModeCM_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 3, 10, 1, 19),
    _Hh3cDot11SIDAPWorkModeCM_Type()
)
hh3cDot11SIDAPWorkModeCM.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cDot11SIDAPWorkModeCM.setStatus("current")
_Hh3cDot11SIDEchoInterval_Type = Integer32
_Hh3cDot11SIDEchoInterval_Object = MibTableColumn
hh3cDot11SIDEchoInterval = _Hh3cDot11SIDEchoInterval_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 3, 10, 1, 20),
    _Hh3cDot11SIDEchoInterval_Type()
)
hh3cDot11SIDEchoInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDot11SIDEchoInterval.setStatus("current")
if mibBuilder.loadTexts:
    hh3cDot11SIDEchoInterval.setUnits("second")
_Hh3cDot11APSTVlanTable_Object = MibTable
hh3cDot11APSTVlanTable = _Hh3cDot11APSTVlanTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 3, 11)
)
if mibBuilder.loadTexts:
    hh3cDot11APSTVlanTable.setStatus("current")
_Hh3cDot11APSTVlanEntry_Object = MibTableRow
hh3cDot11APSTVlanEntry = _Hh3cDot11APSTVlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 3, 11, 1)
)
hh3cDot11APSTVlanEntry.setIndexNames(
    (0, "HH3C-DOT11-CFG-MIB", "hh3cDot11SIDAPSerialID"),
    (0, "HH3C-DOT11-CFG-MIB", "hh3cDot11CfgRadioID"),
    (0, "HH3C-DOT11-CFG-MIB", "hh3cDot11CfgServicePolicyID"),
)
if mibBuilder.loadTexts:
    hh3cDot11APSTVlanEntry.setStatus("current")


class _Hh3cDot11CfgSTVLANID_Type(Integer32):
    """Custom type hh3cDot11CfgSTVLANID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_Hh3cDot11CfgSTVLANID_Type.__name__ = "Integer32"
_Hh3cDot11CfgSTVLANID_Object = MibTableColumn
hh3cDot11CfgSTVLANID = _Hh3cDot11CfgSTVLANID_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 3, 11, 1, 1),
    _Hh3cDot11CfgSTVLANID_Type()
)
hh3cDot11CfgSTVLANID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cDot11CfgSTVLANID.setStatus("current")


class _Hh3cDot11CfgSTNASPortID_Type(OctetString):
    """Custom type hh3cDot11CfgSTNASPortID based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_Hh3cDot11CfgSTNASPortID_Type.__name__ = "OctetString"
_Hh3cDot11CfgSTNASPortID_Object = MibTableColumn
hh3cDot11CfgSTNASPortID = _Hh3cDot11CfgSTNASPortID_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 3, 11, 1, 2),
    _Hh3cDot11CfgSTNASPortID_Type()
)
hh3cDot11CfgSTNASPortID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11CfgSTNASPortID.setStatus("current")
_Hh3cDot11CfgServiceSetRowStatus_Type = RowStatus
_Hh3cDot11CfgServiceSetRowStatus_Object = MibTableColumn
hh3cDot11CfgServiceSetRowStatus = _Hh3cDot11CfgServiceSetRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 3, 11, 1, 3),
    _Hh3cDot11CfgServiceSetRowStatus_Type()
)
hh3cDot11CfgServiceSetRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cDot11CfgServiceSetRowStatus.setStatus("current")


class _Hh3cDot11CfgSTNASID_Type(OctetString):
    """Custom type hh3cDot11CfgSTNASID based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_Hh3cDot11CfgSTNASID_Type.__name__ = "OctetString"
_Hh3cDot11CfgSTNASID_Object = MibTableColumn
hh3cDot11CfgSTNASID = _Hh3cDot11CfgSTNASID_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 3, 11, 1, 4),
    _Hh3cDot11CfgSTNASID_Type()
)
hh3cDot11CfgSTNASID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11CfgSTNASID.setStatus("current")
_Hh3cDot11RadioIntfConfigGroup_ObjectIdentity = ObjectIdentity
hh3cDot11RadioIntfConfigGroup = _Hh3cDot11RadioIntfConfigGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 4)
)
_Hh3cDot11RadioIntfConfigTable_Object = MibTable
hh3cDot11RadioIntfConfigTable = _Hh3cDot11RadioIntfConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 4, 1)
)
if mibBuilder.loadTexts:
    hh3cDot11RadioIntfConfigTable.setStatus("current")
_Hh3cDot11RadioIntfConfigEntry_Object = MibTableRow
hh3cDot11RadioIntfConfigEntry = _Hh3cDot11RadioIntfConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 4, 1, 1)
)
hh3cDot11RadioIntfConfigEntry.setIndexNames(
    (0, "HH3C-DOT11-CFG-MIB", "hh3cDot11RadioIfIdx"),
)
if mibBuilder.loadTexts:
    hh3cDot11RadioIntfConfigEntry.setStatus("current")
_Hh3cDot11RadioIfIdx_Type = Integer32
_Hh3cDot11RadioIfIdx_Object = MibTableColumn
hh3cDot11RadioIfIdx = _Hh3cDot11RadioIfIdx_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 4, 1, 1, 1),
    _Hh3cDot11RadioIfIdx_Type()
)
hh3cDot11RadioIfIdx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cDot11RadioIfIdx.setStatus("current")


class _Hh3cDot11RadioCfgBeaconIntvl_Type(Integer32):
    """Custom type hh3cDot11RadioCfgBeaconIntvl based on Integer32"""
    defaultValue = 100


_Hh3cDot11RadioCfgBeaconIntvl_Type.__name__ = "Integer32"
_Hh3cDot11RadioCfgBeaconIntvl_Object = MibTableColumn
hh3cDot11RadioCfgBeaconIntvl = _Hh3cDot11RadioCfgBeaconIntvl_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 4, 1, 1, 2),
    _Hh3cDot11RadioCfgBeaconIntvl_Type()
)
hh3cDot11RadioCfgBeaconIntvl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDot11RadioCfgBeaconIntvl.setStatus("current")
if mibBuilder.loadTexts:
    hh3cDot11RadioCfgBeaconIntvl.setUnits("TU")


class _Hh3cDot11RadioCfgDtimIntvl_Type(Integer32):
    """Custom type hh3cDot11RadioCfgDtimIntvl based on Integer32"""
    defaultValue = 1


_Hh3cDot11RadioCfgDtimIntvl_Type.__name__ = "Integer32"
_Hh3cDot11RadioCfgDtimIntvl_Object = MibTableColumn
hh3cDot11RadioCfgDtimIntvl = _Hh3cDot11RadioCfgDtimIntvl_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 4, 1, 1, 3),
    _Hh3cDot11RadioCfgDtimIntvl_Type()
)
hh3cDot11RadioCfgDtimIntvl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDot11RadioCfgDtimIntvl.setStatus("current")


class _Hh3cDot11RadioCfgRtsThreshold_Type(Integer32):
    """Custom type hh3cDot11RadioCfgRtsThreshold based on Integer32"""
    defaultValue = 2346


_Hh3cDot11RadioCfgRtsThreshold_Type.__name__ = "Integer32"
_Hh3cDot11RadioCfgRtsThreshold_Object = MibTableColumn
hh3cDot11RadioCfgRtsThreshold = _Hh3cDot11RadioCfgRtsThreshold_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 4, 1, 1, 4),
    _Hh3cDot11RadioCfgRtsThreshold_Type()
)
hh3cDot11RadioCfgRtsThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDot11RadioCfgRtsThreshold.setStatus("current")
if mibBuilder.loadTexts:
    hh3cDot11RadioCfgRtsThreshold.setUnits("Byte")


class _Hh3cDot11RadioCfgFragThreshold_Type(Integer32):
    """Custom type hh3cDot11RadioCfgFragThreshold based on Integer32"""
    defaultValue = 2346


_Hh3cDot11RadioCfgFragThreshold_Type.__name__ = "Integer32"
_Hh3cDot11RadioCfgFragThreshold_Object = MibTableColumn
hh3cDot11RadioCfgFragThreshold = _Hh3cDot11RadioCfgFragThreshold_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 4, 1, 1, 5),
    _Hh3cDot11RadioCfgFragThreshold_Type()
)
hh3cDot11RadioCfgFragThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDot11RadioCfgFragThreshold.setStatus("current")
if mibBuilder.loadTexts:
    hh3cDot11RadioCfgFragThreshold.setUnits("Byte")


class _Hh3cDot11RadioCfgShtRetryThld_Type(Integer32):
    """Custom type hh3cDot11RadioCfgShtRetryThld based on Integer32"""
    defaultValue = 5


_Hh3cDot11RadioCfgShtRetryThld_Type.__name__ = "Integer32"
_Hh3cDot11RadioCfgShtRetryThld_Object = MibTableColumn
hh3cDot11RadioCfgShtRetryThld = _Hh3cDot11RadioCfgShtRetryThld_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 4, 1, 1, 6),
    _Hh3cDot11RadioCfgShtRetryThld_Type()
)
hh3cDot11RadioCfgShtRetryThld.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDot11RadioCfgShtRetryThld.setStatus("current")


class _Hh3cDot11RadioCfglongRtrThld_Type(Integer32):
    """Custom type hh3cDot11RadioCfglongRtrThld based on Integer32"""
    defaultValue = 5


_Hh3cDot11RadioCfglongRtrThld_Type.__name__ = "Integer32"
_Hh3cDot11RadioCfglongRtrThld_Object = MibTableColumn
hh3cDot11RadioCfglongRtrThld = _Hh3cDot11RadioCfglongRtrThld_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 4, 1, 1, 7),
    _Hh3cDot11RadioCfglongRtrThld_Type()
)
hh3cDot11RadioCfglongRtrThld.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDot11RadioCfglongRtrThld.setStatus("current")


class _Hh3cDot11RadioCfgMaxRxLifetime_Type(Unsigned32):
    """Custom type hh3cDot11RadioCfgMaxRxLifetime based on Unsigned32"""
    defaultValue = 2000


_Hh3cDot11RadioCfgMaxRxLifetime_Type.__name__ = "Unsigned32"
_Hh3cDot11RadioCfgMaxRxLifetime_Object = MibTableColumn
hh3cDot11RadioCfgMaxRxLifetime = _Hh3cDot11RadioCfgMaxRxLifetime_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 4, 1, 1, 8),
    _Hh3cDot11RadioCfgMaxRxLifetime_Type()
)
hh3cDot11RadioCfgMaxRxLifetime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDot11RadioCfgMaxRxLifetime.setStatus("current")
if mibBuilder.loadTexts:
    hh3cDot11RadioCfgMaxRxLifetime.setUnits("millisecond")
_Hh3cDot11RadioCfgType_Type = Hh3cDot11RadioType
_Hh3cDot11RadioCfgType_Object = MibTableColumn
hh3cDot11RadioCfgType = _Hh3cDot11RadioCfgType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 4, 1, 1, 9),
    _Hh3cDot11RadioCfgType_Type()
)
hh3cDot11RadioCfgType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDot11RadioCfgType.setStatus("current")


class _Hh3cDot11RadioCfgChannel_Type(Hh3cDot11ChannelScopeType):
    """Custom type hh3cDot11RadioCfgChannel based on Hh3cDot11ChannelScopeType"""
    defaultValue = 1


_Hh3cDot11RadioCfgChannel_Type.__name__ = "Hh3cDot11ChannelScopeType"
_Hh3cDot11RadioCfgChannel_Object = MibTableColumn
hh3cDot11RadioCfgChannel = _Hh3cDot11RadioCfgChannel_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 4, 1, 1, 10),
    _Hh3cDot11RadioCfgChannel_Type()
)
hh3cDot11RadioCfgChannel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDot11RadioCfgChannel.setStatus("current")
_Hh3cDot11RadioCfgMaxTxPwrLvl_Type = Hh3cDot11TxPwrLevelScopeType
_Hh3cDot11RadioCfgMaxTxPwrLvl_Object = MibTableColumn
hh3cDot11RadioCfgMaxTxPwrLvl = _Hh3cDot11RadioCfgMaxTxPwrLvl_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 4, 1, 1, 11),
    _Hh3cDot11RadioCfgMaxTxPwrLvl_Type()
)
hh3cDot11RadioCfgMaxTxPwrLvl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDot11RadioCfgMaxTxPwrLvl.setStatus("current")
if mibBuilder.loadTexts:
    hh3cDot11RadioCfgMaxTxPwrLvl.setUnits("dbm")


class _Hh3cDot11RadioCfgPreambleLen_Type(Hh3cDot11PreambleType):
    """Custom type hh3cDot11RadioCfgPreambleLen based on Hh3cDot11PreambleType"""
    defaultValue = 2


_Hh3cDot11RadioCfgPreambleLen_Type.__name__ = "Hh3cDot11PreambleType"
_Hh3cDot11RadioCfgPreambleLen_Object = MibTableColumn
hh3cDot11RadioCfgPreambleLen = _Hh3cDot11RadioCfgPreambleLen_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 4, 1, 1, 12),
    _Hh3cDot11RadioCfgPreambleLen_Type()
)
hh3cDot11RadioCfgPreambleLen.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDot11RadioCfgPreambleLen.setStatus("current")
_Hh3cDot11RadioCfgWorkMode_Type = Hh3cDot11WorkMode
_Hh3cDot11RadioCfgWorkMode_Object = MibTableColumn
hh3cDot11RadioCfgWorkMode = _Hh3cDot11RadioCfgWorkMode_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 4, 1, 1, 13),
    _Hh3cDot11RadioCfgWorkMode_Type()
)
hh3cDot11RadioCfgWorkMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDot11RadioCfgWorkMode.setStatus("current")


class _Hh3cDot11RadioCfgOnly11gEnable_Type(TruthValue):
    """Custom type hh3cDot11RadioCfgOnly11gEnable based on TruthValue"""
    defaultValue = 2


_Hh3cDot11RadioCfgOnly11gEnable_Type.__name__ = "TruthValue"
_Hh3cDot11RadioCfgOnly11gEnable_Object = MibTableColumn
hh3cDot11RadioCfgOnly11gEnable = _Hh3cDot11RadioCfgOnly11gEnable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 4, 1, 1, 14),
    _Hh3cDot11RadioCfgOnly11gEnable_Type()
)
hh3cDot11RadioCfgOnly11gEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDot11RadioCfgOnly11gEnable.setStatus("current")
_Hh3cDot11RadioCfgType2_Type = Hh3cDot11RadioType2
_Hh3cDot11RadioCfgType2_Object = MibTableColumn
hh3cDot11RadioCfgType2 = _Hh3cDot11RadioCfgType2_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 4, 1, 1, 15),
    _Hh3cDot11RadioCfgType2_Type()
)
hh3cDot11RadioCfgType2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDot11RadioCfgType2.setStatus("current")


class _Hh3cDot11RadioCfgRssithresholdCM_Type(Integer32):
    """Custom type hh3cDot11RadioCfgRssithresholdCM based on Integer32"""
    defaultValue = 1


_Hh3cDot11RadioCfgRssithresholdCM_Type.__name__ = "Integer32"
_Hh3cDot11RadioCfgRssithresholdCM_Object = MibTableColumn
hh3cDot11RadioCfgRssithresholdCM = _Hh3cDot11RadioCfgRssithresholdCM_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 4, 1, 1, 16),
    _Hh3cDot11RadioCfgRssithresholdCM_Type()
)
hh3cDot11RadioCfgRssithresholdCM.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDot11RadioCfgRssithresholdCM.setStatus("current")
if mibBuilder.loadTexts:
    hh3cDot11RadioCfgRssithresholdCM.setUnits("dBm")
_Hh3cDot11RadioIntfBindTable_Object = MibTable
hh3cDot11RadioIntfBindTable = _Hh3cDot11RadioIntfBindTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 4, 2)
)
if mibBuilder.loadTexts:
    hh3cDot11RadioIntfBindTable.setStatus("current")
_Hh3cDot11RadioIntfBindEntry_Object = MibTableRow
hh3cDot11RadioIntfBindEntry = _Hh3cDot11RadioIntfBindEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 4, 2, 1)
)
hh3cDot11RadioIntfBindEntry.setIndexNames(
    (0, "HH3C-DOT11-CFG-MIB", "hh3cDot11RadioIfIdx"),
    (0, "HH3C-DOT11-CFG-MIB", "hh3cDot11RadioIntfBindSvcPlcyID"),
)
if mibBuilder.loadTexts:
    hh3cDot11RadioIntfBindEntry.setStatus("current")
_Hh3cDot11RadioIntfBindSvcPlcyID_Type = Hh3cDot11ServicePolicyIDType
_Hh3cDot11RadioIntfBindSvcPlcyID_Object = MibTableColumn
hh3cDot11RadioIntfBindSvcPlcyID = _Hh3cDot11RadioIntfBindSvcPlcyID_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 4, 2, 1, 1),
    _Hh3cDot11RadioIntfBindSvcPlcyID_Type()
)
hh3cDot11RadioIntfBindSvcPlcyID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cDot11RadioIntfBindSvcPlcyID.setStatus("current")
_Hh3cDot11RadioIntfBindIfIdx_Type = Unsigned32
_Hh3cDot11RadioIntfBindIfIdx_Object = MibTableColumn
hh3cDot11RadioIntfBindIfIdx = _Hh3cDot11RadioIntfBindIfIdx_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 4, 2, 1, 2),
    _Hh3cDot11RadioIntfBindIfIdx_Type()
)
hh3cDot11RadioIntfBindIfIdx.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cDot11RadioIntfBindIfIdx.setStatus("current")
_Hh3cDot11RadioIntfBindRowStatus_Type = RowStatus
_Hh3cDot11RadioIntfBindRowStatus_Object = MibTableColumn
hh3cDot11RadioIntfBindRowStatus = _Hh3cDot11RadioIntfBindRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 4, 2, 1, 3),
    _Hh3cDot11RadioIntfBindRowStatus_Type()
)
hh3cDot11RadioIntfBindRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cDot11RadioIntfBindRowStatus.setStatus("current")
_Hh3cDot11DataRateConfigGroup_ObjectIdentity = ObjectIdentity
hh3cDot11DataRateConfigGroup = _Hh3cDot11DataRateConfigGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 5)
)
_Hh3cDot11DataRateConfigTable_Object = MibTable
hh3cDot11DataRateConfigTable = _Hh3cDot11DataRateConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 5, 1)
)
if mibBuilder.loadTexts:
    hh3cDot11DataRateConfigTable.setStatus("current")
_Hh3cDot11DataRateConfigEntry_Object = MibTableRow
hh3cDot11DataRateConfigEntry = _Hh3cDot11DataRateConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 5, 1, 1)
)
hh3cDot11DataRateConfigEntry.setIndexNames(
    (0, "HH3C-DOT11-CFG-MIB", "hh3cDot11RadioTypeID"),
)
if mibBuilder.loadTexts:
    hh3cDot11DataRateConfigEntry.setStatus("current")
_Hh3cDot11RadioTypeID_Type = Hh3cDot11RadioType
_Hh3cDot11RadioTypeID_Object = MibTableColumn
hh3cDot11RadioTypeID = _Hh3cDot11RadioTypeID_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 5, 1, 1, 1),
    _Hh3cDot11RadioTypeID_Type()
)
hh3cDot11RadioTypeID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cDot11RadioTypeID.setStatus("current")


class _Hh3cDot11SupportedRateSet_Type(OctetString):
    """Custom type hh3cDot11SupportedRateSet based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_Hh3cDot11SupportedRateSet_Type.__name__ = "OctetString"
_Hh3cDot11SupportedRateSet_Object = MibTableColumn
hh3cDot11SupportedRateSet = _Hh3cDot11SupportedRateSet_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 5, 1, 1, 2),
    _Hh3cDot11SupportedRateSet_Type()
)
hh3cDot11SupportedRateSet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDot11SupportedRateSet.setStatus("current")


class _Hh3cDot11MandatoryRateSet_Type(OctetString):
    """Custom type hh3cDot11MandatoryRateSet based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_Hh3cDot11MandatoryRateSet_Type.__name__ = "OctetString"
_Hh3cDot11MandatoryRateSet_Object = MibTableColumn
hh3cDot11MandatoryRateSet = _Hh3cDot11MandatoryRateSet_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 5, 1, 1, 3),
    _Hh3cDot11MandatoryRateSet_Type()
)
hh3cDot11MandatoryRateSet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDot11MandatoryRateSet.setStatus("current")


class _Hh3cDot11DisabledRateSet_Type(OctetString):
    """Custom type hh3cDot11DisabledRateSet based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_Hh3cDot11DisabledRateSet_Type.__name__ = "OctetString"
_Hh3cDot11DisabledRateSet_Object = MibTableColumn
hh3cDot11DisabledRateSet = _Hh3cDot11DisabledRateSet_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 5, 1, 1, 4),
    _Hh3cDot11DisabledRateSet_Type()
)
hh3cDot11DisabledRateSet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDot11DisabledRateSet.setStatus("current")


class _Hh3cDot11SmartRateSet_Type(OctetString):
    """Custom type hh3cDot11SmartRateSet based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_Hh3cDot11SmartRateSet_Type.__name__ = "OctetString"
_Hh3cDot11SmartRateSet_Object = MibTableColumn
hh3cDot11SmartRateSet = _Hh3cDot11SmartRateSet_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 5, 1, 1, 5),
    _Hh3cDot11SmartRateSet_Type()
)
hh3cDot11SmartRateSet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDot11SmartRateSet.setStatus("current")
_Hh3cDot11InterfaceConfigGroup_ObjectIdentity = ObjectIdentity
hh3cDot11InterfaceConfigGroup = _Hh3cDot11InterfaceConfigGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 6)
)
_Hh3cDot11WlanEssIfTable_Object = MibTable
hh3cDot11WlanEssIfTable = _Hh3cDot11WlanEssIfTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 6, 1)
)
if mibBuilder.loadTexts:
    hh3cDot11WlanEssIfTable.setStatus("current")
_Hh3cDot11WlanEssIfEntry_Object = MibTableRow
hh3cDot11WlanEssIfEntry = _Hh3cDot11WlanEssIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 6, 1, 1)
)
hh3cDot11WlanEssIfEntry.setIndexNames(
    (0, "HH3C-DOT11-CFG-MIB", "hh3cDot11WlanEssIfNumber"),
)
if mibBuilder.loadTexts:
    hh3cDot11WlanEssIfEntry.setStatus("current")
_Hh3cDot11WlanEssIfNumber_Type = Integer32
_Hh3cDot11WlanEssIfNumber_Object = MibTableColumn
hh3cDot11WlanEssIfNumber = _Hh3cDot11WlanEssIfNumber_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 6, 1, 1, 1),
    _Hh3cDot11WlanEssIfNumber_Type()
)
hh3cDot11WlanEssIfNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cDot11WlanEssIfNumber.setStatus("current")
_Hh3cDot11WlanEssIfIndex_Type = Integer32
_Hh3cDot11WlanEssIfIndex_Object = MibTableColumn
hh3cDot11WlanEssIfIndex = _Hh3cDot11WlanEssIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 6, 1, 1, 2),
    _Hh3cDot11WlanEssIfIndex_Type()
)
hh3cDot11WlanEssIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11WlanEssIfIndex.setStatus("current")
_Hh3cDot11WlanEssRowStatus_Type = RowStatus
_Hh3cDot11WlanEssRowStatus_Object = MibTableColumn
hh3cDot11WlanEssRowStatus = _Hh3cDot11WlanEssRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 6, 1, 1, 3),
    _Hh3cDot11WlanEssRowStatus_Type()
)
hh3cDot11WlanEssRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cDot11WlanEssRowStatus.setStatus("current")
_Hh3cDot11WlanBssIfTable_Object = MibTable
hh3cDot11WlanBssIfTable = _Hh3cDot11WlanBssIfTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 6, 2)
)
if mibBuilder.loadTexts:
    hh3cDot11WlanBssIfTable.setStatus("current")
_Hh3cDot11WlanBssIfEntry_Object = MibTableRow
hh3cDot11WlanBssIfEntry = _Hh3cDot11WlanBssIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 6, 2, 1)
)
hh3cDot11WlanBssIfEntry.setIndexNames(
    (0, "HH3C-DOT11-CFG-MIB", "hh3cDot11WlanBssIfNumber"),
)
if mibBuilder.loadTexts:
    hh3cDot11WlanBssIfEntry.setStatus("current")
_Hh3cDot11WlanBssIfNumber_Type = Integer32
_Hh3cDot11WlanBssIfNumber_Object = MibTableColumn
hh3cDot11WlanBssIfNumber = _Hh3cDot11WlanBssIfNumber_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 6, 2, 1, 1),
    _Hh3cDot11WlanBssIfNumber_Type()
)
hh3cDot11WlanBssIfNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cDot11WlanBssIfNumber.setStatus("current")
_Hh3cDot11WlanBssIfIndex_Type = Integer32
_Hh3cDot11WlanBssIfIndex_Object = MibTableColumn
hh3cDot11WlanBssIfIndex = _Hh3cDot11WlanBssIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 6, 2, 1, 2),
    _Hh3cDot11WlanBssIfIndex_Type()
)
hh3cDot11WlanBssIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11WlanBssIfIndex.setStatus("current")
_Hh3cDot11WlanBssRowStatus_Type = RowStatus
_Hh3cDot11WlanBssRowStatus_Object = MibTableColumn
hh3cDot11WlanBssRowStatus = _Hh3cDot11WlanBssRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 6, 2, 1, 3),
    _Hh3cDot11WlanBssRowStatus_Type()
)
hh3cDot11WlanBssRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cDot11WlanBssRowStatus.setStatus("current")
_Hh3cDot11WLANEthernetIfTable_Object = MibTable
hh3cDot11WLANEthernetIfTable = _Hh3cDot11WLANEthernetIfTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 6, 3)
)
if mibBuilder.loadTexts:
    hh3cDot11WLANEthernetIfTable.setStatus("current")
_Hh3cDot11WLANEthernetIfEntry_Object = MibTableRow
hh3cDot11WLANEthernetIfEntry = _Hh3cDot11WLANEthernetIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 6, 3, 1)
)
hh3cDot11WLANEthernetIfEntry.setIndexNames(
    (0, "HH3C-DOT11-CFG-MIB", "hh3cDot11WlanEthernetIfNumber"),
)
if mibBuilder.loadTexts:
    hh3cDot11WLANEthernetIfEntry.setStatus("current")
_Hh3cDot11WlanEthernetIfNumber_Type = Integer32
_Hh3cDot11WlanEthernetIfNumber_Object = MibTableColumn
hh3cDot11WlanEthernetIfNumber = _Hh3cDot11WlanEthernetIfNumber_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 6, 3, 1, 1),
    _Hh3cDot11WlanEthernetIfNumber_Type()
)
hh3cDot11WlanEthernetIfNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cDot11WlanEthernetIfNumber.setStatus("current")
_Hh3cDot11WLANEthernetIfIndex_Type = Integer32
_Hh3cDot11WLANEthernetIfIndex_Object = MibTableColumn
hh3cDot11WLANEthernetIfIndex = _Hh3cDot11WLANEthernetIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 6, 3, 1, 2),
    _Hh3cDot11WLANEthernetIfIndex_Type()
)
hh3cDot11WLANEthernetIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11WLANEthernetIfIndex.setStatus("current")
_Hh3cDot11WlanEthernetRowStatus_Type = RowStatus
_Hh3cDot11WlanEthernetRowStatus_Object = MibTableColumn
hh3cDot11WlanEthernetRowStatus = _Hh3cDot11WlanEthernetRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 6, 3, 1, 3),
    _Hh3cDot11WlanEthernetRowStatus_Type()
)
hh3cDot11WlanEthernetRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cDot11WlanEthernetRowStatus.setStatus("current")
_Hh3cDot11PortSecurityTable_Object = MibTable
hh3cDot11PortSecurityTable = _Hh3cDot11PortSecurityTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 6, 4)
)
if mibBuilder.loadTexts:
    hh3cDot11PortSecurityTable.setStatus("current")
_Hh3cDot11PortSecurityEntry_Object = MibTableRow
hh3cDot11PortSecurityEntry = _Hh3cDot11PortSecurityEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 6, 4, 1)
)
hh3cDot11PortSecurityEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    hh3cDot11PortSecurityEntry.setStatus("current")


class _Hh3cDot11PortSecurityMode_Type(Integer32):
    """Custom type hh3cDot11PortSecurityMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("noRestrictions", 1),
          ("userLoginSecureExt", 2),
          ("psk", 3),
          ("macAddressAndPsk", 4),
          ("userLoginSecureExtOrPsk", 5),
          ("ext", 6))
    )


_Hh3cDot11PortSecurityMode_Type.__name__ = "Integer32"
_Hh3cDot11PortSecurityMode_Object = MibTableColumn
hh3cDot11PortSecurityMode = _Hh3cDot11PortSecurityMode_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 6, 4, 1, 1),
    _Hh3cDot11PortSecurityMode_Type()
)
hh3cDot11PortSecurityMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDot11PortSecurityMode.setStatus("current")


class _Hh3cDot11SecurityUserLoginTxKeyType_Type(Integer32):
    """Custom type hh3cDot11SecurityUserLoginTxKeyType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("userLoginTxKeyTypeNone", 1),
          ("userLoginTxKeyTypeDot11Key", 2),
          ("userLoginTxKeyTypeRsaRC4Key", 3))
    )


_Hh3cDot11SecurityUserLoginTxKeyType_Type.__name__ = "Integer32"
_Hh3cDot11SecurityUserLoginTxKeyType_Object = MibTableColumn
hh3cDot11SecurityUserLoginTxKeyType = _Hh3cDot11SecurityUserLoginTxKeyType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 6, 4, 1, 2),
    _Hh3cDot11SecurityUserLoginTxKeyType_Type()
)
hh3cDot11SecurityUserLoginTxKeyType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDot11SecurityUserLoginTxKeyType.setStatus("current")


class _Hh3cDot11SecurityPskKeyMode_Type(Integer32):
    """Custom type hh3cDot11SecurityPskKeyMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("pskKeyModeNone", 1),
          ("pskKeyModePassPhrase", 2),
          ("pskKeyModeRawKey", 3))
    )


_Hh3cDot11SecurityPskKeyMode_Type.__name__ = "Integer32"
_Hh3cDot11SecurityPskKeyMode_Object = MibTableColumn
hh3cDot11SecurityPskKeyMode = _Hh3cDot11SecurityPskKeyMode_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 6, 4, 1, 3),
    _Hh3cDot11SecurityPskKeyMode_Type()
)
hh3cDot11SecurityPskKeyMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDot11SecurityPskKeyMode.setStatus("current")
_Hh3cDot11SecurityPskKeyString_Type = DisplayString
_Hh3cDot11SecurityPskKeyString_Object = MibTableColumn
hh3cDot11SecurityPskKeyString = _Hh3cDot11SecurityPskKeyString_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 6, 4, 1, 4),
    _Hh3cDot11SecurityPskKeyString_Type()
)
hh3cDot11SecurityPskKeyString.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDot11SecurityPskKeyString.setStatus("current")
_Hh3cDot11WlanMeshIfTable_Object = MibTable
hh3cDot11WlanMeshIfTable = _Hh3cDot11WlanMeshIfTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 6, 5)
)
if mibBuilder.loadTexts:
    hh3cDot11WlanMeshIfTable.setStatus("current")
_Hh3cDot11WlanMeshIfEntry_Object = MibTableRow
hh3cDot11WlanMeshIfEntry = _Hh3cDot11WlanMeshIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 6, 5, 1)
)
hh3cDot11WlanMeshIfEntry.setIndexNames(
    (0, "HH3C-DOT11-CFG-MIB", "hh3cDot11WlanMeshIfNumber"),
)
if mibBuilder.loadTexts:
    hh3cDot11WlanMeshIfEntry.setStatus("current")
_Hh3cDot11WlanMeshIfNumber_Type = Integer32
_Hh3cDot11WlanMeshIfNumber_Object = MibTableColumn
hh3cDot11WlanMeshIfNumber = _Hh3cDot11WlanMeshIfNumber_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 6, 5, 1, 1),
    _Hh3cDot11WlanMeshIfNumber_Type()
)
hh3cDot11WlanMeshIfNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cDot11WlanMeshIfNumber.setStatus("current")
_Hh3cDot11WlanMeshIfIndex_Type = Integer32
_Hh3cDot11WlanMeshIfIndex_Object = MibTableColumn
hh3cDot11WlanMeshIfIndex = _Hh3cDot11WlanMeshIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 6, 5, 1, 2),
    _Hh3cDot11WlanMeshIfIndex_Type()
)
hh3cDot11WlanMeshIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11WlanMeshIfIndex.setStatus("current")
_Hh3cDot11WlanMeshRowStatus_Type = RowStatus
_Hh3cDot11WlanMeshRowStatus_Object = MibTableColumn
hh3cDot11WlanMeshRowStatus = _Hh3cDot11WlanMeshRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 6, 5, 1, 3),
    _Hh3cDot11WlanMeshRowStatus_Type()
)
hh3cDot11WlanMeshRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cDot11WlanMeshRowStatus.setStatus("current")
_Hh3cDot11ACBackupGroup_ObjectIdentity = ObjectIdentity
hh3cDot11ACBackupGroup = _Hh3cDot11ACBackupGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 7)
)
_Hh3cDot11BackupACAdrssIP_Type = InetAddress
_Hh3cDot11BackupACAdrssIP_Object = MibScalar
hh3cDot11BackupACAdrssIP = _Hh3cDot11BackupACAdrssIP_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 7, 1),
    _Hh3cDot11BackupACAdrssIP_Type()
)
hh3cDot11BackupACAdrssIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDot11BackupACAdrssIP.setStatus("current")
_Hh3cDot11BackupACAdrssIPv6_Type = InetAddress
_Hh3cDot11BackupACAdrssIPv6_Object = MibScalar
hh3cDot11BackupACAdrssIPv6 = _Hh3cDot11BackupACAdrssIPv6_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 7, 2),
    _Hh3cDot11BackupACAdrssIPv6_Type()
)
hh3cDot11BackupACAdrssIPv6.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDot11BackupACAdrssIPv6.setStatus("current")
_Hh3cDot11RadioElementConfigGroup_ObjectIdentity = ObjectIdentity
hh3cDot11RadioElementConfigGroup = _Hh3cDot11RadioElementConfigGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 8)
)
_Hh3cDot11nRadioCfgTable_Object = MibTable
hh3cDot11nRadioCfgTable = _Hh3cDot11nRadioCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 8, 1)
)
if mibBuilder.loadTexts:
    hh3cDot11nRadioCfgTable.setStatus("current")
_Hh3cDot11nRadioCfgEntry_Object = MibTableRow
hh3cDot11nRadioCfgEntry = _Hh3cDot11nRadioCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 8, 1, 1)
)
hh3cDot11nRadioCfgEntry.setIndexNames(
    (0, "HH3C-DOT11-CFG-MIB", "hh3cDot11nRadioCfgIndex"),
)
if mibBuilder.loadTexts:
    hh3cDot11nRadioCfgEntry.setStatus("current")
_Hh3cDot11nRadioCfgIndex_Type = Hh3cDot11RadioElementIndex
_Hh3cDot11nRadioCfgIndex_Object = MibTableColumn
hh3cDot11nRadioCfgIndex = _Hh3cDot11nRadioCfgIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 8, 1, 1, 1),
    _Hh3cDot11nRadioCfgIndex_Type()
)
hh3cDot11nRadioCfgIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cDot11nRadioCfgIndex.setStatus("current")


class _Hh3cDot11nAMpduEnable_Type(TruthValue):
    """Custom type hh3cDot11nAMpduEnable based on TruthValue"""
    defaultValue = 1


_Hh3cDot11nAMpduEnable_Type.__name__ = "TruthValue"
_Hh3cDot11nAMpduEnable_Object = MibTableColumn
hh3cDot11nAMpduEnable = _Hh3cDot11nAMpduEnable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 8, 1, 1, 2),
    _Hh3cDot11nAMpduEnable_Type()
)
hh3cDot11nAMpduEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDot11nAMpduEnable.setStatus("current")


class _Hh3cDot11nAMsduEnable_Type(TruthValue):
    """Custom type hh3cDot11nAMsduEnable based on TruthValue"""
    defaultValue = 1


_Hh3cDot11nAMsduEnable_Type.__name__ = "TruthValue"
_Hh3cDot11nAMsduEnable_Object = MibTableColumn
hh3cDot11nAMsduEnable = _Hh3cDot11nAMsduEnable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 8, 1, 1, 3),
    _Hh3cDot11nAMsduEnable_Type()
)
hh3cDot11nAMsduEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDot11nAMsduEnable.setStatus("current")


class _Hh3cDot11nClientDot11nOnly_Type(TruthValue):
    """Custom type hh3cDot11nClientDot11nOnly based on TruthValue"""
    defaultValue = 2


_Hh3cDot11nClientDot11nOnly_Type.__name__ = "TruthValue"
_Hh3cDot11nClientDot11nOnly_Object = MibTableColumn
hh3cDot11nClientDot11nOnly = _Hh3cDot11nClientDot11nOnly_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 8, 1, 1, 4),
    _Hh3cDot11nClientDot11nOnly_Type()
)
hh3cDot11nClientDot11nOnly.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDot11nClientDot11nOnly.setStatus("current")


class _Hh3cDot11nChanelBand_Type(Integer32):
    """Custom type hh3cDot11nChanelBand based on Integer32"""
    defaultValue = 2

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
        *(("mode20", 1),
          ("mode40", 2),
          ("mode80", 3),
          ("mode160", 4),
          ("mode80and80", 5))
    )


_Hh3cDot11nChanelBand_Type.__name__ = "Integer32"
_Hh3cDot11nChanelBand_Object = MibTableColumn
hh3cDot11nChanelBand = _Hh3cDot11nChanelBand_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 8, 1, 1, 5),
    _Hh3cDot11nChanelBand_Type()
)
hh3cDot11nChanelBand.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDot11nChanelBand.setStatus("current")


class _Hh3cDot11nShortGiEnable_Type(TruthValue):
    """Custom type hh3cDot11nShortGiEnable based on TruthValue"""
    defaultValue = 1


_Hh3cDot11nShortGiEnable_Type.__name__ = "TruthValue"
_Hh3cDot11nShortGiEnable_Object = MibTableColumn
hh3cDot11nShortGiEnable = _Hh3cDot11nShortGiEnable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 8, 1, 1, 6),
    _Hh3cDot11nShortGiEnable_Type()
)
hh3cDot11nShortGiEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDot11nShortGiEnable.setStatus("current")


class _Hh3cDot11nClientDot11acOnly_Type(TruthValue):
    """Custom type hh3cDot11nClientDot11acOnly based on TruthValue"""
    defaultValue = 2


_Hh3cDot11nClientDot11acOnly_Type.__name__ = "TruthValue"
_Hh3cDot11nClientDot11acOnly_Object = MibTableColumn
hh3cDot11nClientDot11acOnly = _Hh3cDot11nClientDot11acOnly_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 8, 1, 1, 7),
    _Hh3cDot11nClientDot11acOnly_Type()
)
hh3cDot11nClientDot11acOnly.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDot11nClientDot11acOnly.setStatus("current")


class _Hh3cDot11nSupportMaxMcs_Type(Integer32):
    """Custom type hh3cDot11nSupportMaxMcs based on Integer32"""
    defaultValue = 76

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 76),
    )


_Hh3cDot11nSupportMaxMcs_Type.__name__ = "Integer32"
_Hh3cDot11nSupportMaxMcs_Object = MibTableColumn
hh3cDot11nSupportMaxMcs = _Hh3cDot11nSupportMaxMcs_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 8, 1, 1, 8),
    _Hh3cDot11nSupportMaxMcs_Type()
)
hh3cDot11nSupportMaxMcs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDot11nSupportMaxMcs.setStatus("current")


class _Hh3cDot11nMandatoryMaxMcs_Type(Integer32):
    """Custom type hh3cDot11nMandatoryMaxMcs based on Integer32"""
    defaultValue = 255

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 76),
        ValueRangeConstraint(255, 255),
    )


_Hh3cDot11nMandatoryMaxMcs_Type.__name__ = "Integer32"
_Hh3cDot11nMandatoryMaxMcs_Object = MibTableColumn
hh3cDot11nMandatoryMaxMcs = _Hh3cDot11nMandatoryMaxMcs_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 8, 1, 1, 9),
    _Hh3cDot11nMandatoryMaxMcs_Type()
)
hh3cDot11nMandatoryMaxMcs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDot11nMandatoryMaxMcs.setStatus("current")
_Hh3cDot11RadioWDSTable_Object = MibTable
hh3cDot11RadioWDSTable = _Hh3cDot11RadioWDSTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 8, 2)
)
if mibBuilder.loadTexts:
    hh3cDot11RadioWDSTable.setStatus("current")
_Hh3cDot11RadioWDSEntry_Object = MibTableRow
hh3cDot11RadioWDSEntry = _Hh3cDot11RadioWDSEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 8, 2, 1)
)
hh3cDot11RadioWDSEntry.setIndexNames(
    (0, "HH3C-DOT11-CFG-MIB", "hh3cDot11RadioWDSIndex"),
)
if mibBuilder.loadTexts:
    hh3cDot11RadioWDSEntry.setStatus("current")
_Hh3cDot11RadioWDSIndex_Type = Hh3cDot11RadioElementIndex
_Hh3cDot11RadioWDSIndex_Object = MibTableColumn
hh3cDot11RadioWDSIndex = _Hh3cDot11RadioWDSIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 8, 2, 1, 1),
    _Hh3cDot11RadioWDSIndex_Type()
)
hh3cDot11RadioWDSIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cDot11RadioWDSIndex.setStatus("current")


class _Hh3cDot11RadioWDSMode_Type(Integer32):
    """Custom type hh3cDot11RadioWDSMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("nowds", 1),
          ("wds", 2))
    )


_Hh3cDot11RadioWDSMode_Type.__name__ = "Integer32"
_Hh3cDot11RadioWDSMode_Object = MibTableColumn
hh3cDot11RadioWDSMode = _Hh3cDot11RadioWDSMode_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 8, 2, 1, 2),
    _Hh3cDot11RadioWDSMode_Type()
)
hh3cDot11RadioWDSMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDot11RadioWDSMode.setStatus("current")


class _Hh3cDot11RadioWDSNetWorkID_Type(OctetString):
    """Custom type hh3cDot11RadioWDSNetWorkID based on OctetString"""
    defaultValue = OctetString("")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Hh3cDot11RadioWDSNetWorkID_Type.__name__ = "OctetString"
_Hh3cDot11RadioWDSNetWorkID_Object = MibTableColumn
hh3cDot11RadioWDSNetWorkID = _Hh3cDot11RadioWDSNetWorkID_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 8, 2, 1, 3),
    _Hh3cDot11RadioWDSNetWorkID_Type()
)
hh3cDot11RadioWDSNetWorkID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDot11RadioWDSNetWorkID.setStatus("current")


class _Hh3cDot11WDSSecPskKeyMode_Type(Integer32):
    """Custom type hh3cDot11WDSSecPskKeyMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("pskKeyModeNone", 1),
          ("pskKeyModePassPhrase", 2),
          ("pskKeyModeRawKey", 3))
    )


_Hh3cDot11WDSSecPskKeyMode_Type.__name__ = "Integer32"
_Hh3cDot11WDSSecPskKeyMode_Object = MibTableColumn
hh3cDot11WDSSecPskKeyMode = _Hh3cDot11WDSSecPskKeyMode_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 8, 2, 1, 4),
    _Hh3cDot11WDSSecPskKeyMode_Type()
)
hh3cDot11WDSSecPskKeyMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDot11WDSSecPskKeyMode.setStatus("current")


class _Hh3cDot11WDSSecPskKeyString_Type(DisplayString):
    """Custom type hh3cDot11WDSSecPskKeyString based on DisplayString"""
    defaultValue = OctetString("")


_Hh3cDot11WDSSecPskKeyString_Type.__name__ = "DisplayString"
_Hh3cDot11WDSSecPskKeyString_Object = MibTableColumn
hh3cDot11WDSSecPskKeyString = _Hh3cDot11WDSSecPskKeyString_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 8, 2, 1, 5),
    _Hh3cDot11WDSSecPskKeyString_Type()
)
hh3cDot11WDSSecPskKeyString.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDot11WDSSecPskKeyString.setStatus("current")
_Hh3cDot11nRadioCfg2Table_Object = MibTable
hh3cDot11nRadioCfg2Table = _Hh3cDot11nRadioCfg2Table_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 8, 3)
)
if mibBuilder.loadTexts:
    hh3cDot11nRadioCfg2Table.setStatus("current")
_Hh3cDot11nRadioCfg2Entry_Object = MibTableRow
hh3cDot11nRadioCfg2Entry = _Hh3cDot11nRadioCfg2Entry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 8, 3, 1)
)
hh3cDot11nRadioCfg2Entry.setIndexNames(
    (0, "HH3C-DOT11-CFG-MIB", "hh3cDot11nRadioCfg2APIDIndex"),
    (0, "HH3C-DOT11-CFG-MIB", "hh3cDot11nRadioCfg2RadioIDIndex"),
)
if mibBuilder.loadTexts:
    hh3cDot11nRadioCfg2Entry.setStatus("current")
_Hh3cDot11nRadioCfg2APIDIndex_Type = Hh3cDot11ObjectIDType
_Hh3cDot11nRadioCfg2APIDIndex_Object = MibTableColumn
hh3cDot11nRadioCfg2APIDIndex = _Hh3cDot11nRadioCfg2APIDIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 8, 3, 1, 1),
    _Hh3cDot11nRadioCfg2APIDIndex_Type()
)
hh3cDot11nRadioCfg2APIDIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cDot11nRadioCfg2APIDIndex.setStatus("current")
_Hh3cDot11nRadioCfg2RadioIDIndex_Type = Hh3cDot11RadioScopeType
_Hh3cDot11nRadioCfg2RadioIDIndex_Object = MibTableColumn
hh3cDot11nRadioCfg2RadioIDIndex = _Hh3cDot11nRadioCfg2RadioIDIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 8, 3, 1, 2),
    _Hh3cDot11nRadioCfg2RadioIDIndex_Type()
)
hh3cDot11nRadioCfg2RadioIDIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cDot11nRadioCfg2RadioIDIndex.setStatus("current")


class _Hh3cDot11nRadioCfg2AMpduEnable_Type(TruthValue):
    """Custom type hh3cDot11nRadioCfg2AMpduEnable based on TruthValue"""
    defaultValue = 1


_Hh3cDot11nRadioCfg2AMpduEnable_Type.__name__ = "TruthValue"
_Hh3cDot11nRadioCfg2AMpduEnable_Object = MibTableColumn
hh3cDot11nRadioCfg2AMpduEnable = _Hh3cDot11nRadioCfg2AMpduEnable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 8, 3, 1, 3),
    _Hh3cDot11nRadioCfg2AMpduEnable_Type()
)
hh3cDot11nRadioCfg2AMpduEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDot11nRadioCfg2AMpduEnable.setStatus("current")


class _Hh3cDot11nRadioCfg2AMsduEnable_Type(TruthValue):
    """Custom type hh3cDot11nRadioCfg2AMsduEnable based on TruthValue"""
    defaultValue = 1


_Hh3cDot11nRadioCfg2AMsduEnable_Type.__name__ = "TruthValue"
_Hh3cDot11nRadioCfg2AMsduEnable_Object = MibTableColumn
hh3cDot11nRadioCfg2AMsduEnable = _Hh3cDot11nRadioCfg2AMsduEnable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 8, 3, 1, 4),
    _Hh3cDot11nRadioCfg2AMsduEnable_Type()
)
hh3cDot11nRadioCfg2AMsduEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDot11nRadioCfg2AMsduEnable.setStatus("current")


class _Hh3cDot11nRadioCfg2ClientDot11nOnly_Type(TruthValue):
    """Custom type hh3cDot11nRadioCfg2ClientDot11nOnly based on TruthValue"""
    defaultValue = 2


_Hh3cDot11nRadioCfg2ClientDot11nOnly_Type.__name__ = "TruthValue"
_Hh3cDot11nRadioCfg2ClientDot11nOnly_Object = MibTableColumn
hh3cDot11nRadioCfg2ClientDot11nOnly = _Hh3cDot11nRadioCfg2ClientDot11nOnly_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 8, 3, 1, 5),
    _Hh3cDot11nRadioCfg2ClientDot11nOnly_Type()
)
hh3cDot11nRadioCfg2ClientDot11nOnly.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDot11nRadioCfg2ClientDot11nOnly.setStatus("current")


class _Hh3cDot11nRadioCfg2ChannelBand_Type(Integer32):
    """Custom type hh3cDot11nRadioCfg2ChannelBand based on Integer32"""
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
        *(("mode20", 1),
          ("mode40", 2),
          ("mode80", 3),
          ("mode160", 4),
          ("mode80and80", 5))
    )


_Hh3cDot11nRadioCfg2ChannelBand_Type.__name__ = "Integer32"
_Hh3cDot11nRadioCfg2ChannelBand_Object = MibTableColumn
hh3cDot11nRadioCfg2ChannelBand = _Hh3cDot11nRadioCfg2ChannelBand_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 8, 3, 1, 6),
    _Hh3cDot11nRadioCfg2ChannelBand_Type()
)
hh3cDot11nRadioCfg2ChannelBand.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDot11nRadioCfg2ChannelBand.setStatus("current")


class _Hh3cDot11nRadioCfg2ShortGiEnable_Type(TruthValue):
    """Custom type hh3cDot11nRadioCfg2ShortGiEnable based on TruthValue"""
    defaultValue = 1


_Hh3cDot11nRadioCfg2ShortGiEnable_Type.__name__ = "TruthValue"
_Hh3cDot11nRadioCfg2ShortGiEnable_Object = MibTableColumn
hh3cDot11nRadioCfg2ShortGiEnable = _Hh3cDot11nRadioCfg2ShortGiEnable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 8, 3, 1, 7),
    _Hh3cDot11nRadioCfg2ShortGiEnable_Type()
)
hh3cDot11nRadioCfg2ShortGiEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDot11nRadioCfg2ShortGiEnable.setStatus("current")


class _Hh3cDot11nRadioCfg2AMpduEnableCM_Type(Integer32):
    """Custom type hh3cDot11nRadioCfg2AMpduEnableCM based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_Hh3cDot11nRadioCfg2AMpduEnableCM_Type.__name__ = "Integer32"
_Hh3cDot11nRadioCfg2AMpduEnableCM_Object = MibTableColumn
hh3cDot11nRadioCfg2AMpduEnableCM = _Hh3cDot11nRadioCfg2AMpduEnableCM_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 8, 3, 1, 8),
    _Hh3cDot11nRadioCfg2AMpduEnableCM_Type()
)
hh3cDot11nRadioCfg2AMpduEnableCM.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDot11nRadioCfg2AMpduEnableCM.setStatus("current")


class _Hh3cDot11nRadioCfg2ChannelBandCM_Type(Integer32):
    """Custom type hh3cDot11nRadioCfg2ChannelBandCM based on Integer32"""
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
        *(("mode40", 1),
          ("mode20", 2),
          ("mode80", 3),
          ("mode160", 4),
          ("mode80and80", 5))
    )


_Hh3cDot11nRadioCfg2ChannelBandCM_Type.__name__ = "Integer32"
_Hh3cDot11nRadioCfg2ChannelBandCM_Object = MibTableColumn
hh3cDot11nRadioCfg2ChannelBandCM = _Hh3cDot11nRadioCfg2ChannelBandCM_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 8, 3, 1, 9),
    _Hh3cDot11nRadioCfg2ChannelBandCM_Type()
)
hh3cDot11nRadioCfg2ChannelBandCM.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDot11nRadioCfg2ChannelBandCM.setStatus("current")


class _Hh3cDot11nRadioCfg2ShortGiEnableCM_Type(Integer32):
    """Custom type hh3cDot11nRadioCfg2ShortGiEnableCM based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_Hh3cDot11nRadioCfg2ShortGiEnableCM_Type.__name__ = "Integer32"
_Hh3cDot11nRadioCfg2ShortGiEnableCM_Object = MibTableColumn
hh3cDot11nRadioCfg2ShortGiEnableCM = _Hh3cDot11nRadioCfg2ShortGiEnableCM_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 8, 3, 1, 10),
    _Hh3cDot11nRadioCfg2ShortGiEnableCM_Type()
)
hh3cDot11nRadioCfg2ShortGiEnableCM.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDot11nRadioCfg2ShortGiEnableCM.setStatus("current")


class _Hh3cDot11nRadioCfg2ClientDot11acOnly_Type(TruthValue):
    """Custom type hh3cDot11nRadioCfg2ClientDot11acOnly based on TruthValue"""
    defaultValue = 2


_Hh3cDot11nRadioCfg2ClientDot11acOnly_Type.__name__ = "TruthValue"
_Hh3cDot11nRadioCfg2ClientDot11acOnly_Object = MibTableColumn
hh3cDot11nRadioCfg2ClientDot11acOnly = _Hh3cDot11nRadioCfg2ClientDot11acOnly_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 8, 3, 1, 11),
    _Hh3cDot11nRadioCfg2ClientDot11acOnly_Type()
)
hh3cDot11nRadioCfg2ClientDot11acOnly.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDot11nRadioCfg2ClientDot11acOnly.setStatus("current")


class _Hh3cDot11nRadioCfg2ClientDot11nOnlyCM_Type(Hh3cDot11TruthValueCM):
    """Custom type hh3cDot11nRadioCfg2ClientDot11nOnlyCM based on Hh3cDot11TruthValueCM"""
    defaultValue = 0


_Hh3cDot11nRadioCfg2ClientDot11nOnlyCM_Type.__name__ = "Hh3cDot11TruthValueCM"
_Hh3cDot11nRadioCfg2ClientDot11nOnlyCM_Object = MibTableColumn
hh3cDot11nRadioCfg2ClientDot11nOnlyCM = _Hh3cDot11nRadioCfg2ClientDot11nOnlyCM_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 8, 3, 1, 12),
    _Hh3cDot11nRadioCfg2ClientDot11nOnlyCM_Type()
)
hh3cDot11nRadioCfg2ClientDot11nOnlyCM.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDot11nRadioCfg2ClientDot11nOnlyCM.setStatus("current")


class _Hh3cDot11nRadioCfg2SupportMaxMcs_Type(Integer32):
    """Custom type hh3cDot11nRadioCfg2SupportMaxMcs based on Integer32"""
    defaultValue = 76

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 76),
    )


_Hh3cDot11nRadioCfg2SupportMaxMcs_Type.__name__ = "Integer32"
_Hh3cDot11nRadioCfg2SupportMaxMcs_Object = MibTableColumn
hh3cDot11nRadioCfg2SupportMaxMcs = _Hh3cDot11nRadioCfg2SupportMaxMcs_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 8, 3, 1, 13),
    _Hh3cDot11nRadioCfg2SupportMaxMcs_Type()
)
hh3cDot11nRadioCfg2SupportMaxMcs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDot11nRadioCfg2SupportMaxMcs.setStatus("current")


class _Hh3cDot11nRadioCfg2MandatoryMaxMcs_Type(Integer32):
    """Custom type hh3cDot11nRadioCfg2MandatoryMaxMcs based on Integer32"""
    defaultValue = 255

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 76),
        ValueRangeConstraint(255, 255),
    )


_Hh3cDot11nRadioCfg2MandatoryMaxMcs_Type.__name__ = "Integer32"
_Hh3cDot11nRadioCfg2MandatoryMaxMcs_Object = MibTableColumn
hh3cDot11nRadioCfg2MandatoryMaxMcs = _Hh3cDot11nRadioCfg2MandatoryMaxMcs_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 8, 3, 1, 14),
    _Hh3cDot11nRadioCfg2MandatoryMaxMcs_Type()
)
hh3cDot11nRadioCfg2MandatoryMaxMcs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDot11nRadioCfg2MandatoryMaxMcs.setStatus("current")
_Hh3cDot11CfgNotifyGroup_ObjectIdentity = ObjectIdentity
hh3cDot11CfgNotifyGroup = _Hh3cDot11CfgNotifyGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 9)
)
_Hh3cDot11CfgNotifications_ObjectIdentity = ObjectIdentity
hh3cDot11CfgNotifications = _Hh3cDot11CfgNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 9, 0)
)
_Hh3cDot11CfgTrapVarObjects_ObjectIdentity = ObjectIdentity
hh3cDot11CfgTrapVarObjects = _Hh3cDot11CfgTrapVarObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 9, 1)
)


class _Hh3cDot11PreConflictTemplateNum_Type(Integer32):
    """Custom type hh3cDot11PreConflictTemplateNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_Hh3cDot11PreConflictTemplateNum_Type.__name__ = "Integer32"
_Hh3cDot11PreConflictTemplateNum_Object = MibScalar
hh3cDot11PreConflictTemplateNum = _Hh3cDot11PreConflictTemplateNum_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 9, 1, 1),
    _Hh3cDot11PreConflictTemplateNum_Type()
)
hh3cDot11PreConflictTemplateNum.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cDot11PreConflictTemplateNum.setStatus("current")


class _Hh3cDot11CurrConflictTemplateNum_Type(Integer32):
    """Custom type hh3cDot11CurrConflictTemplateNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_Hh3cDot11CurrConflictTemplateNum_Type.__name__ = "Integer32"
_Hh3cDot11CurrConflictTemplateNum_Object = MibScalar
hh3cDot11CurrConflictTemplateNum = _Hh3cDot11CurrConflictTemplateNum_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 9, 1, 2),
    _Hh3cDot11CurrConflictTemplateNum_Type()
)
hh3cDot11CurrConflictTemplateNum.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cDot11CurrConflictTemplateNum.setStatus("current")


class _Hh3cDot11ConflictCipherIdx_Type(Integer32):
    """Custom type hh3cDot11ConflictCipherIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_Hh3cDot11ConflictCipherIdx_Type.__name__ = "Integer32"
_Hh3cDot11ConflictCipherIdx_Object = MibScalar
hh3cDot11ConflictCipherIdx = _Hh3cDot11ConflictCipherIdx_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 9, 1, 3),
    _Hh3cDot11ConflictCipherIdx_Type()
)
hh3cDot11ConflictCipherIdx.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cDot11ConflictCipherIdx.setStatus("current")
_Hh3cDot11ConfigureAPID_Type = Hh3cDot11ObjectIDType
_Hh3cDot11ConfigureAPID_Object = MibScalar
hh3cDot11ConfigureAPID = _Hh3cDot11ConfigureAPID_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 9, 1, 4),
    _Hh3cDot11ConfigureAPID_Type()
)
hh3cDot11ConfigureAPID.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cDot11ConfigureAPID.setStatus("current")
_Hh3cDot11ConfigureRadioID_Type = Hh3cDot11RadioScopeType
_Hh3cDot11ConfigureRadioID_Object = MibScalar
hh3cDot11ConfigureRadioID = _Hh3cDot11ConfigureRadioID_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 9, 1, 5),
    _Hh3cDot11ConfigureRadioID_Type()
)
hh3cDot11ConfigureRadioID.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cDot11ConfigureRadioID.setStatus("current")
_Hh3cDot11ConfigureAPMacAddress_Type = MacAddress
_Hh3cDot11ConfigureAPMacAddress_Object = MibScalar
hh3cDot11ConfigureAPMacAddress = _Hh3cDot11ConfigureAPMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 9, 1, 6),
    _Hh3cDot11ConfigureAPMacAddress_Type()
)
hh3cDot11ConfigureAPMacAddress.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cDot11ConfigureAPMacAddress.setStatus("current")
_Hh3cDot11PreConflictTemplateSSID_Type = Hh3cDot11SSIDStringType
_Hh3cDot11PreConflictTemplateSSID_Object = MibScalar
hh3cDot11PreConflictTemplateSSID = _Hh3cDot11PreConflictTemplateSSID_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 9, 1, 7),
    _Hh3cDot11PreConflictTemplateSSID_Type()
)
hh3cDot11PreConflictTemplateSSID.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cDot11PreConflictTemplateSSID.setStatus("current")
_Hh3cDot11CurrConflictTemplateSSID_Type = Hh3cDot11SSIDStringType
_Hh3cDot11CurrConflictTemplateSSID_Object = MibScalar
hh3cDot11CurrConflictTemplateSSID = _Hh3cDot11CurrConflictTemplateSSID_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 9, 1, 8),
    _Hh3cDot11CurrConflictTemplateSSID_Type()
)
hh3cDot11CurrConflictTemplateSSID.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cDot11CurrConflictTemplateSSID.setStatus("current")
_Hh3cDot11LocalACConfigGroup_ObjectIdentity = ObjectIdentity
hh3cDot11LocalACConfigGroup = _Hh3cDot11LocalACConfigGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 10)
)
_Hh3cDot11LocalACTemplateTable_Object = MibTable
hh3cDot11LocalACTemplateTable = _Hh3cDot11LocalACTemplateTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 10, 1)
)
if mibBuilder.loadTexts:
    hh3cDot11LocalACTemplateTable.setStatus("current")
_Hh3cDot11LocalACTemplateEntry_Object = MibTableRow
hh3cDot11LocalACTemplateEntry = _Hh3cDot11LocalACTemplateEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 10, 1, 1)
)
hh3cDot11LocalACTemplateEntry.setIndexNames(
    (0, "HH3C-DOT11-CFG-MIB", "hh3cDot11LocalACTemplateName"),
)
if mibBuilder.loadTexts:
    hh3cDot11LocalACTemplateEntry.setStatus("current")


class _Hh3cDot11LocalACTemplateName_Type(OctetString):
    """Custom type hh3cDot11LocalACTemplateName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_Hh3cDot11LocalACTemplateName_Type.__name__ = "OctetString"
_Hh3cDot11LocalACTemplateName_Object = MibTableColumn
hh3cDot11LocalACTemplateName = _Hh3cDot11LocalACTemplateName_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 10, 1, 1, 1),
    _Hh3cDot11LocalACTemplateName_Type()
)
hh3cDot11LocalACTemplateName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cDot11LocalACTemplateName.setStatus("current")
_Hh3cDot11LocalACName_Type = OctetString
_Hh3cDot11LocalACName_Object = MibTableColumn
hh3cDot11LocalACName = _Hh3cDot11LocalACName_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 10, 1, 1, 2),
    _Hh3cDot11LocalACName_Type()
)
hh3cDot11LocalACName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cDot11LocalACName.setStatus("current")
_Hh3cDot11LocalACSerialID_Type = OctetString
_Hh3cDot11LocalACSerialID_Object = MibTableColumn
hh3cDot11LocalACSerialID = _Hh3cDot11LocalACSerialID_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 10, 1, 1, 3),
    _Hh3cDot11LocalACSerialID_Type()
)
hh3cDot11LocalACSerialID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cDot11LocalACSerialID.setStatus("current")
_Hh3cDot11TemLocalACModelAlias_Type = OctetString
_Hh3cDot11TemLocalACModelAlias_Object = MibTableColumn
hh3cDot11TemLocalACModelAlias = _Hh3cDot11TemLocalACModelAlias_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 10, 1, 1, 4),
    _Hh3cDot11TemLocalACModelAlias_Type()
)
hh3cDot11TemLocalACModelAlias.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cDot11TemLocalACModelAlias.setStatus("current")
_Hh3cDot11LocalACTempRowStatus_Type = RowStatus
_Hh3cDot11LocalACTempRowStatus_Object = MibTableColumn
hh3cDot11LocalACTempRowStatus = _Hh3cDot11LocalACTempRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 10, 1, 1, 5),
    _Hh3cDot11LocalACTempRowStatus_Type()
)
hh3cDot11LocalACTempRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cDot11LocalACTempRowStatus.setStatus("current")


class _Hh3cDot11LocalACStatus_Type(Integer32):
    """Custom type hh3cDot11LocalACStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("join", 1),
          ("joinConfirm", 2),
          ("download", 3),
          ("config", 4),
          ("run", 5),
          ("idle", 6))
    )


_Hh3cDot11LocalACStatus_Type.__name__ = "Integer32"
_Hh3cDot11LocalACStatus_Object = MibTableColumn
hh3cDot11LocalACStatus = _Hh3cDot11LocalACStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 10, 1, 1, 6),
    _Hh3cDot11LocalACStatus_Type()
)
hh3cDot11LocalACStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11LocalACStatus.setStatus("current")
_Hh3cDot11LocalACIPAddress_Type = IpAddress
_Hh3cDot11LocalACIPAddress_Object = MibTableColumn
hh3cDot11LocalACIPAddress = _Hh3cDot11LocalACIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 10, 1, 1, 7),
    _Hh3cDot11LocalACIPAddress_Type()
)
hh3cDot11LocalACIPAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11LocalACIPAddress.setStatus("current")
_Hh3cDot11LocalACIPv6Address_Type = OctetString
_Hh3cDot11LocalACIPv6Address_Object = MibTableColumn
hh3cDot11LocalACIPv6Address = _Hh3cDot11LocalACIPv6Address_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 10, 1, 1, 8),
    _Hh3cDot11LocalACIPv6Address_Type()
)
hh3cDot11LocalACIPv6Address.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11LocalACIPv6Address.setStatus("current")


class _Hh3cDot11EchoInterval_Type(Integer32):
    """Custom type hh3cDot11EchoInterval based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(5, 255),
    )


_Hh3cDot11EchoInterval_Type.__name__ = "Integer32"
_Hh3cDot11EchoInterval_Object = MibTableColumn
hh3cDot11EchoInterval = _Hh3cDot11EchoInterval_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 10, 1, 1, 9),
    _Hh3cDot11EchoInterval_Type()
)
hh3cDot11EchoInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cDot11EchoInterval.setStatus("current")
if mibBuilder.loadTexts:
    hh3cDot11EchoInterval.setUnits("second")


class _Hh3cDot11RetransInterval_Type(Integer32):
    """Custom type hh3cDot11RetransInterval based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(3, 8),
    )


_Hh3cDot11RetransInterval_Type.__name__ = "Integer32"
_Hh3cDot11RetransInterval_Object = MibTableColumn
hh3cDot11RetransInterval = _Hh3cDot11RetransInterval_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 10, 1, 1, 10),
    _Hh3cDot11RetransInterval_Type()
)
hh3cDot11RetransInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cDot11RetransInterval.setStatus("current")
if mibBuilder.loadTexts:
    hh3cDot11RetransInterval.setUnits("second")


class _Hh3cDot11RetransCount_Type(Integer32):
    """Custom type hh3cDot11RetransCount based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 5),
    )


_Hh3cDot11RetransCount_Type.__name__ = "Integer32"
_Hh3cDot11RetransCount_Object = MibTableColumn
hh3cDot11RetransCount = _Hh3cDot11RetransCount_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 10, 1, 1, 11),
    _Hh3cDot11RetransCount_Type()
)
hh3cDot11RetransCount.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cDot11RetransCount.setStatus("current")
if mibBuilder.loadTexts:
    hh3cDot11RetransCount.setUnits("second")


class _Hh3cDot11FirmwareUpgrade_Type(Integer32):
    """Custom type hh3cDot11FirmwareUpgrade based on Integer32"""
    defaultValue = 1

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


_Hh3cDot11FirmwareUpgrade_Type.__name__ = "Integer32"
_Hh3cDot11FirmwareUpgrade_Object = MibTableColumn
hh3cDot11FirmwareUpgrade = _Hh3cDot11FirmwareUpgrade_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 10, 1, 1, 12),
    _Hh3cDot11FirmwareUpgrade_Type()
)
hh3cDot11FirmwareUpgrade.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cDot11FirmwareUpgrade.setStatus("current")
_Hh3cDot11RemoteConfigGroup_ObjectIdentity = ObjectIdentity
hh3cDot11RemoteConfigGroup = _Hh3cDot11RemoteConfigGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 11)
)
_Hh3cDot11RemoteCfgApTable_Object = MibTable
hh3cDot11RemoteCfgApTable = _Hh3cDot11RemoteCfgApTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 11, 1)
)
if mibBuilder.loadTexts:
    hh3cDot11RemoteCfgApTable.setStatus("current")
_Hh3cDot11RemoteCfgApEntry_Object = MibTableRow
hh3cDot11RemoteCfgApEntry = _Hh3cDot11RemoteCfgApEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 11, 1, 1)
)
hh3cDot11RemoteCfgApEntry.setIndexNames(
    (0, "HH3C-DOT11-CFG-MIB", "hh3cDot11RmtApName"),
)
if mibBuilder.loadTexts:
    hh3cDot11RemoteCfgApEntry.setStatus("current")


class _Hh3cDot11RmtApName_Type(OctetString):
    """Custom type hh3cDot11RmtApName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 127),
    )


_Hh3cDot11RmtApName_Type.__name__ = "OctetString"
_Hh3cDot11RmtApName_Object = MibTableColumn
hh3cDot11RmtApName = _Hh3cDot11RmtApName_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 11, 1, 1, 1),
    _Hh3cDot11RmtApName_Type()
)
hh3cDot11RmtApName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cDot11RmtApName.setStatus("current")
_Hh3cDot11RmtVlanList_Type = OctetString
_Hh3cDot11RmtVlanList_Object = MibTableColumn
hh3cDot11RmtVlanList = _Hh3cDot11RmtVlanList_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 11, 1, 1, 2),
    _Hh3cDot11RmtVlanList_Type()
)
hh3cDot11RmtVlanList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDot11RmtVlanList.setStatus("current")


class _Hh3cDot11RmtCfgEnable_Type(TruthValue):
    """Custom type hh3cDot11RmtCfgEnable based on TruthValue"""
    defaultValue = 2


_Hh3cDot11RmtCfgEnable_Type.__name__ = "TruthValue"
_Hh3cDot11RmtCfgEnable_Object = MibTableColumn
hh3cDot11RmtCfgEnable = _Hh3cDot11RmtCfgEnable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 11, 1, 1, 3),
    _Hh3cDot11RmtCfgEnable_Type()
)
hh3cDot11RmtCfgEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDot11RmtCfgEnable.setStatus("current")
_Hh3cDot11RemoteCfgIFTable_Object = MibTable
hh3cDot11RemoteCfgIFTable = _Hh3cDot11RemoteCfgIFTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 11, 2)
)
if mibBuilder.loadTexts:
    hh3cDot11RemoteCfgIFTable.setStatus("current")
_Hh3cDot11RemoteCfgIFEntry_Object = MibTableRow
hh3cDot11RemoteCfgIFEntry = _Hh3cDot11RemoteCfgIFEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 11, 2, 1)
)
hh3cDot11RemoteCfgIFEntry.setIndexNames(
    (0, "HH3C-DOT11-CFG-MIB", "hh3cDot11RmtIfApName"),
    (0, "HH3C-DOT11-CFG-MIB", "hh3cDot11RmtIfType"),
    (0, "HH3C-DOT11-CFG-MIB", "hh3cDot11RmtIfNum"),
)
if mibBuilder.loadTexts:
    hh3cDot11RemoteCfgIFEntry.setStatus("current")


class _Hh3cDot11RmtIfApName_Type(OctetString):
    """Custom type hh3cDot11RmtIfApName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 127),
    )


_Hh3cDot11RmtIfApName_Type.__name__ = "OctetString"
_Hh3cDot11RmtIfApName_Object = MibTableColumn
hh3cDot11RmtIfApName = _Hh3cDot11RmtIfApName_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 11, 2, 1, 1),
    _Hh3cDot11RmtIfApName_Type()
)
hh3cDot11RmtIfApName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cDot11RmtIfApName.setStatus("current")
_Hh3cDot11RmtIfType_Type = Integer32
_Hh3cDot11RmtIfType_Object = MibTableColumn
hh3cDot11RmtIfType = _Hh3cDot11RmtIfType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 11, 2, 1, 2),
    _Hh3cDot11RmtIfType_Type()
)
hh3cDot11RmtIfType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cDot11RmtIfType.setStatus("current")
_Hh3cDot11RmtIfNum_Type = Integer32
_Hh3cDot11RmtIfNum_Object = MibTableColumn
hh3cDot11RmtIfNum = _Hh3cDot11RmtIfNum_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 11, 2, 1, 3),
    _Hh3cDot11RmtIfNum_Type()
)
hh3cDot11RmtIfNum.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cDot11RmtIfNum.setStatus("current")
_Hh3cDot11RmtIfName_Type = OctetString
_Hh3cDot11RmtIfName_Object = MibTableColumn
hh3cDot11RmtIfName = _Hh3cDot11RmtIfName_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 11, 2, 1, 4),
    _Hh3cDot11RmtIfName_Type()
)
hh3cDot11RmtIfName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11RmtIfName.setStatus("current")


class _Hh3cDot11RmtIfLinkType_Type(Integer32):
    """Custom type hh3cDot11RmtIfLinkType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("access", 1),
          ("trunk", 2),
          ("hybrid", 3))
    )


_Hh3cDot11RmtIfLinkType_Type.__name__ = "Integer32"
_Hh3cDot11RmtIfLinkType_Object = MibTableColumn
hh3cDot11RmtIfLinkType = _Hh3cDot11RmtIfLinkType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 11, 2, 1, 5),
    _Hh3cDot11RmtIfLinkType_Type()
)
hh3cDot11RmtIfLinkType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDot11RmtIfLinkType.setStatus("current")
_Hh3cDot11RmtIfAccessVlan_Type = Integer32
_Hh3cDot11RmtIfAccessVlan_Object = MibTableColumn
hh3cDot11RmtIfAccessVlan = _Hh3cDot11RmtIfAccessVlan_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 11, 2, 1, 6),
    _Hh3cDot11RmtIfAccessVlan_Type()
)
hh3cDot11RmtIfAccessVlan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDot11RmtIfAccessVlan.setStatus("current")
_Hh3cDot11RmtIfTrunkPvidVlan_Type = Integer32
_Hh3cDot11RmtIfTrunkPvidVlan_Object = MibTableColumn
hh3cDot11RmtIfTrunkPvidVlan = _Hh3cDot11RmtIfTrunkPvidVlan_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 11, 2, 1, 7),
    _Hh3cDot11RmtIfTrunkPvidVlan_Type()
)
hh3cDot11RmtIfTrunkPvidVlan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDot11RmtIfTrunkPvidVlan.setStatus("current")
_Hh3cDot11RmtIfTrunkVlanlist_Type = OctetString
_Hh3cDot11RmtIfTrunkVlanlist_Object = MibTableColumn
hh3cDot11RmtIfTrunkVlanlist = _Hh3cDot11RmtIfTrunkVlanlist_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 11, 2, 1, 8),
    _Hh3cDot11RmtIfTrunkVlanlist_Type()
)
hh3cDot11RmtIfTrunkVlanlist.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDot11RmtIfTrunkVlanlist.setStatus("current")
_Hh3cDot11RmtIfHybridPvidVlan_Type = Integer32
_Hh3cDot11RmtIfHybridPvidVlan_Object = MibTableColumn
hh3cDot11RmtIfHybridPvidVlan = _Hh3cDot11RmtIfHybridPvidVlan_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 11, 2, 1, 9),
    _Hh3cDot11RmtIfHybridPvidVlan_Type()
)
hh3cDot11RmtIfHybridPvidVlan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDot11RmtIfHybridPvidVlan.setStatus("current")
_Hh3cDot11RmtIfHybVlanListTag_Type = OctetString
_Hh3cDot11RmtIfHybVlanListTag_Object = MibTableColumn
hh3cDot11RmtIfHybVlanListTag = _Hh3cDot11RmtIfHybVlanListTag_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 11, 2, 1, 10),
    _Hh3cDot11RmtIfHybVlanListTag_Type()
)
hh3cDot11RmtIfHybVlanListTag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDot11RmtIfHybVlanListTag.setStatus("current")
_Hh3cDot11RmtIfHybVlanListUnTag_Type = OctetString
_Hh3cDot11RmtIfHybVlanListUnTag_Object = MibTableColumn
hh3cDot11RmtIfHybVlanListUnTag = _Hh3cDot11RmtIfHybVlanListUnTag_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 11, 2, 1, 11),
    _Hh3cDot11RmtIfHybVlanListUnTag_Type()
)
hh3cDot11RmtIfHybVlanListUnTag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDot11RmtIfHybVlanListUnTag.setStatus("current")


class _Hh3cDot11RmtIfIsolate_Type(TruthValue):
    """Custom type hh3cDot11RmtIfIsolate based on TruthValue"""
    defaultValue = 1


_Hh3cDot11RmtIfIsolate_Type.__name__ = "TruthValue"
_Hh3cDot11RmtIfIsolate_Object = MibTableColumn
hh3cDot11RmtIfIsolate = _Hh3cDot11RmtIfIsolate_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 11, 2, 1, 12),
    _Hh3cDot11RmtIfIsolate_Type()
)
hh3cDot11RmtIfIsolate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDot11RmtIfIsolate.setStatus("current")
_Hh3cDot11RmtIfLinkAggGroupId_Type = Integer32
_Hh3cDot11RmtIfLinkAggGroupId_Object = MibTableColumn
hh3cDot11RmtIfLinkAggGroupId = _Hh3cDot11RmtIfLinkAggGroupId_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 11, 2, 1, 13),
    _Hh3cDot11RmtIfLinkAggGroupId_Type()
)
hh3cDot11RmtIfLinkAggGroupId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDot11RmtIfLinkAggGroupId.setStatus("current")


class _Hh3cDot11RmtIfManagement_Type(TruthValue):
    """Custom type hh3cDot11RmtIfManagement based on TruthValue"""
    defaultValue = 1


_Hh3cDot11RmtIfManagement_Type.__name__ = "TruthValue"
_Hh3cDot11RmtIfManagement_Object = MibTableColumn
hh3cDot11RmtIfManagement = _Hh3cDot11RmtIfManagement_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 11, 2, 1, 14),
    _Hh3cDot11RmtIfManagement_Type()
)
hh3cDot11RmtIfManagement.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDot11RmtIfManagement.setStatus("current")

# Managed Objects groups


# Notification objects

hh3cDot11CfgCipherChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 9, 0, 1)
)
hh3cDot11CfgCipherChange.setObjects(
      *(("HH3C-DOT11-CFG-MIB", "hh3cDot11SSIDName"),
        ("HH3C-DOT11-CFG-MIB", "hh3cDot11SecurityCiphers"))
)
if mibBuilder.loadTexts:
    hh3cDot11CfgCipherChange.setStatus(
        "current"
    )

hh3cDot11CfgPSKChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 9, 0, 2)
)
hh3cDot11CfgPSKChange.setObjects(
    ("HH3C-DOT11-CFG-MIB", "hh3cDot11SSIDName")
)
if mibBuilder.loadTexts:
    hh3cDot11CfgPSKChange.setStatus(
        "current"
    )

hh3cDot11SSIDWepIDConflictTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 4, 9, 0, 3)
)
hh3cDot11SSIDWepIDConflictTrap.setObjects(
      *(("HH3C-DOT11-CFG-MIB", "hh3cDot11PreConflictTemplateNum"),
        ("HH3C-DOT11-CFG-MIB", "hh3cDot11CurrConflictTemplateNum"),
        ("HH3C-DOT11-CFG-MIB", "hh3cDot11ConflictCipherIdx"),
        ("HH3C-DOT11-CFG-MIB", "hh3cDot11ConfigureAPID"),
        ("HH3C-DOT11-CFG-MIB", "hh3cDot11ConfigureRadioID"),
        ("HH3C-DOT11-CFG-MIB", "hh3cDot11ConfigureAPMacAddress"),
        ("HH3C-DOT11-CFG-MIB", "hh3cDot11PreConflictTemplateSSID"),
        ("HH3C-DOT11-CFG-MIB", "hh3cDot11CurrConflictTemplateSSID"))
)
if mibBuilder.loadTexts:
    hh3cDot11SSIDWepIDConflictTrap.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HH3C-DOT11-CFG-MIB",
    **{"hh3cDot11CFG": hh3cDot11CFG,
       "hh3cDot11GlobeConfigGroup": hh3cDot11GlobeConfigGroup,
       "hh3cDot11GlobalCountryCode": hh3cDot11GlobalCountryCode,
       "hh3cDot11StaKeepALiveTimerIntvl": hh3cDot11StaKeepALiveTimerIntvl,
       "hh3cDot11StaIdleTimerIntvl": hh3cDot11StaIdleTimerIntvl,
       "hh3cDot11BroadcastProbeReply": hh3cDot11BroadcastProbeReply,
       "hh3cDot11APScanMode": hh3cDot11APScanMode,
       "hh3cDot11ACCtrlTunnelSecSupport": hh3cDot11ACCtrlTunnelSecSupport,
       "hh3cDot11ACDataTunnelSecSupport": hh3cDot11ACDataTunnelSecSupport,
       "hh3cDot11ACAutoAPSupport": hh3cDot11ACAutoAPSupport,
       "hh3cDot11AutoAPName": hh3cDot11AutoAPName,
       "hh3cDot11PersistentName": hh3cDot11PersistentName,
       "hh3cDot11IntfTrapThreshold": hh3cDot11IntfTrapThreshold,
       "hh3cDot11MonitorInterval": hh3cDot11MonitorInterval,
       "hh3cDot11SampleInterval": hh3cDot11SampleInterval,
       "hh3cDot11ChnlSwitChkInterval": hh3cDot11ChnlSwitChkInterval,
       "hh3cDot11APUserUplimit": hh3cDot11APUserUplimit,
       "hh3cDot11APL2IsolateEnable": hh3cDot11APL2IsolateEnable,
       "hh3cDot11APBSSIDSupportNum": hh3cDot11APBSSIDSupportNum,
       "hh3cDot11APLastUpdateStatTime": hh3cDot11APLastUpdateStatTime,
       "hh3cDot11APDoSProtectEnable": hh3cDot11APDoSProtectEnable,
       "hh3cDot11MaxAPPerIf": hh3cDot11MaxAPPerIf,
       "hh3cDot11SampleTimeStamp": hh3cDot11SampleTimeStamp,
       "hh3cDot11UplinkTrackId": hh3cDot11UplinkTrackId,
       "hh3cDot11RtCollectSwitch": hh3cDot11RtCollectSwitch,
       "hh3cDot11RglCollectIntvl": hh3cDot11RglCollectIntvl,
       "hh3cDot11RtCollectIntvl": hh3cDot11RtCollectIntvl,
       "hh3cDot11AllAPCpuUsageThreshold": hh3cDot11AllAPCpuUsageThreshold,
       "hh3cDot11AllAPMemUsageThreshold": hh3cDot11AllAPMemUsageThreshold,
       "hh3cDot11AdjIntfTrapThreshold": hh3cDot11AdjIntfTrapThreshold,
       "hh3cDot11AllAPMonitorMode": hh3cDot11AllAPMonitorMode,
       "hh3cDot11GlobalApFmwUpdState": hh3cDot11GlobalApFmwUpdState,
       "hh3cDot11ACNasIDCM": hh3cDot11ACNasIDCM,
       "hh3cDot11ACRole": hh3cDot11ACRole,
       "hh3cDot11GlobalLocalACState": hh3cDot11GlobalLocalACState,
       "hh3cDot11CentralACIPAddress": hh3cDot11CentralACIPAddress,
       "hh3cDot11CentralACIPv6Address": hh3cDot11CentralACIPv6Address,
       "hh3cDot11iMcIP": hh3cDot11iMcIP,
       "hh3cDot11iMcPort": hh3cDot11iMcPort,
       "hh3cDot11APProvisionSave": hh3cDot11APProvisionSave,
       "hh3cDot11ApRenameCurrentName": hh3cDot11ApRenameCurrentName,
       "hh3cDot11ApRenameNewName": hh3cDot11ApRenameNewName,
       "hh3cDot11ACDescription": hh3cDot11ACDescription,
       "hh3cDot11PolicyConfigGroup": hh3cDot11PolicyConfigGroup,
       "hh3cDot11RadioPolicyTable": hh3cDot11RadioPolicyTable,
       "hh3cDot11RadioPolicyEntry": hh3cDot11RadioPolicyEntry,
       "hh3cDot11RadioPolicyName": hh3cDot11RadioPolicyName,
       "hh3cDot11BeaconInterval": hh3cDot11BeaconInterval,
       "hh3cDot11DtimInterval": hh3cDot11DtimInterval,
       "hh3cDot11RtsThreshold": hh3cDot11RtsThreshold,
       "hh3cDot11FragThreshold": hh3cDot11FragThreshold,
       "hh3cDot11ShortRetryThreshold": hh3cDot11ShortRetryThreshold,
       "hh3cDot11LongRetryThreshold": hh3cDot11LongRetryThreshold,
       "hh3cDot11MaxRxLifetime": hh3cDot11MaxRxLifetime,
       "hh3cDot11RdoPolicyRowStatus": hh3cDot11RdoPolicyRowStatus,
       "hh3cDot11RdoClientMaxCount": hh3cDot11RdoClientMaxCount,
       "hh3cDot11BeaconIntervalMs": hh3cDot11BeaconIntervalMs,
       "hh3cDot11ServicePolicyTable": hh3cDot11ServicePolicyTable,
       "hh3cDot11ServicePolicyEntry": hh3cDot11ServicePolicyEntry,
       "hh3cDot11ServicePolicyID": hh3cDot11ServicePolicyID,
       "hh3cDot11SSIDName": hh3cDot11SSIDName,
       "hh3cDot11SSIDHidden": hh3cDot11SSIDHidden,
       "hh3cDot11AuthenMode": hh3cDot11AuthenMode,
       "hh3cDot11SSIDEncryptionMode": hh3cDot11SSIDEncryptionMode,
       "hh3cDot11WlanInfBindingType": hh3cDot11WlanInfBindingType,
       "hh3cDot11WlanInfBindingID": hh3cDot11WlanInfBindingID,
       "hh3cDot11SrvPolicyRowStatus": hh3cDot11SrvPolicyRowStatus,
       "hh3cDot11ClientMaxCount": hh3cDot11ClientMaxCount,
       "hh3cDot11SPInCirMode": hh3cDot11SPInCirMode,
       "hh3cDot11SPInCirValue": hh3cDot11SPInCirValue,
       "hh3cDot11SPOutCirMode": hh3cDot11SPOutCirMode,
       "hh3cDot11SPOutCirValue": hh3cDot11SPOutCirValue,
       "hh3cDot11WlanInfPVID": hh3cDot11WlanInfPVID,
       "hh3cDot11SPInCirStaticValue": hh3cDot11SPInCirStaticValue,
       "hh3cDot11SPOutCirStaticValue": hh3cDot11SPOutCirStaticValue,
       "hh3cDot11SPIsolate": hh3cDot11SPIsolate,
       "hh3cDot11WlanexAuthServerIP": hh3cDot11WlanexAuthServerIP,
       "hh3cDot11SPBeaconMeasEnable": hh3cDot11SPBeaconMeasEnable,
       "hh3cDot11SPBeaconMeasType": hh3cDot11SPBeaconMeasType,
       "hh3cDot11SPBeaconMeasInterval": hh3cDot11SPBeaconMeasInterval,
       "hh3cDot11AuthenModeCM": hh3cDot11AuthenModeCM,
       "hh3cDot11SecIEStatusCM": hh3cDot11SecIEStatusCM,
       "hh3cDot11SecurityCiphersCM": hh3cDot11SecurityCiphersCM,
       "hh3cDot11SrvPolicyStatusCM": hh3cDot11SrvPolicyStatusCM,
       "hh3cDot11SSIDHiddenCM": hh3cDot11SSIDHiddenCM,
       "hh3cDot11SPIsolateCM": hh3cDot11SPIsolateCM,
       "hh3cDot11FwdVlanBitMapLow": hh3cDot11FwdVlanBitMapLow,
       "hh3cDot11FwdVlanBitMapHigh": hh3cDot11FwdVlanBitMapHigh,
       "hh3cDot11ServicePolicyName": hh3cDot11ServicePolicyName,
       "hh3cDot11SecurityModeCM": hh3cDot11SecurityModeCM,
       "hh3cDot11SPInCbsValue": hh3cDot11SPInCbsValue,
       "hh3cDot11SPOutCbsValue": hh3cDot11SPOutCbsValue,
       "hh3cDot11WlanInfCustomerPVID": hh3cDot11WlanInfCustomerPVID,
       "hh3cDot11ServicePolicyExtTable": hh3cDot11ServicePolicyExtTable,
       "hh3cDot11ServicePolicyExtEntry": hh3cDot11ServicePolicyExtEntry,
       "hh3cDot11ServicePolicyExtID": hh3cDot11ServicePolicyExtID,
       "hh3cDot11SecIEStatus": hh3cDot11SecIEStatus,
       "hh3cDot11SecurityCiphers": hh3cDot11SecurityCiphers,
       "hh3cDot11CipherKeyIndex": hh3cDot11CipherKeyIndex,
       "hh3cDot11CipherKey": hh3cDot11CipherKey,
       "hh3cDot11SrvPolicyExtRowStatus": hh3cDot11SrvPolicyExtRowStatus,
       "hh3cDot11CipherKeyType": hh3cDot11CipherKeyType,
       "hh3cDot11AkmMode": hh3cDot11AkmMode,
       "hh3cDot11PskKey": hh3cDot11PskKey,
       "hh3cDot11RadioPolicyExtTable": hh3cDot11RadioPolicyExtTable,
       "hh3cDot11RadioPolicyExtEntry": hh3cDot11RadioPolicyExtEntry,
       "hh3cDot11RPAPSerialID": hh3cDot11RPAPSerialID,
       "hh3cDot11RPRadioID": hh3cDot11RPRadioID,
       "hh3cDot11RPBeaconInterval": hh3cDot11RPBeaconInterval,
       "hh3cDot11RPDtimInterval": hh3cDot11RPDtimInterval,
       "hh3cDot11RPRtsThreshold": hh3cDot11RPRtsThreshold,
       "hh3cDot11RPFragThreshold": hh3cDot11RPFragThreshold,
       "hh3cDot11RPShortRetryThreshold": hh3cDot11RPShortRetryThreshold,
       "hh3cDot11RPLongRetryThreshold": hh3cDot11RPLongRetryThreshold,
       "hh3cDot11RPClientMaxCount": hh3cDot11RPClientMaxCount,
       "hh3cDot11RPBeaconIntervalCM": hh3cDot11RPBeaconIntervalCM,
       "hh3cDot11SrvPortSecurityTable": hh3cDot11SrvPortSecurityTable,
       "hh3cDot11SrvPortSecurityEntry": hh3cDot11SrvPortSecurityEntry,
       "hh3cDot11SecurityServicePolicyID": hh3cDot11SecurityServicePolicyID,
       "hh3cDot11SrvPortSecurityMode": hh3cDot11SrvPortSecurityMode,
       "hh3cDot11SrvSecurityKeyType": hh3cDot11SrvSecurityKeyType,
       "hh3cDot11SrvSecurityPskKeyMode": hh3cDot11SrvSecurityPskKeyMode,
       "hh3cDot11SrvSecurityPskKeyString": hh3cDot11SrvSecurityPskKeyString,
       "hh3cDot11SrvPortSecurityModeCM": hh3cDot11SrvPortSecurityModeCM,
       "hh3cDot11SrvPolicyExtendTable": hh3cDot11SrvPolicyExtendTable,
       "hh3cDot11SrvPolicyExtendEntry": hh3cDot11SrvPolicyExtendEntry,
       "hh3cDot11SPEnable": hh3cDot11SPEnable,
       "hh3cDot11SrvL2AuthenTable": hh3cDot11SrvL2AuthenTable,
       "hh3cDot11SrvL2AuthenEntry": hh3cDot11SrvL2AuthenEntry,
       "hh3cDot11SrvL2AuthenID": hh3cDot11SrvL2AuthenID,
       "hh3cDot11L2AuthenMode": hh3cDot11L2AuthenMode,
       "hh3cDot11L2IntrusProtectEnable": hh3cDot11L2IntrusProtectEnable,
       "hh3cDot11L2IntrusProtectOpt": hh3cDot11L2IntrusProtectOpt,
       "hh3cDot11TempServiceStopTimer": hh3cDot11TempServiceStopTimer,
       "hh3cDot11TempBlockMACTimer": hh3cDot11TempBlockMACTimer,
       "hh3cDot11L2IgnoreAuthorization": hh3cDot11L2IgnoreAuthorization,
       "hh3cDot11L2FailVLAN": hh3cDot11L2FailVLAN,
       "hh3cDot11L2CriticalVLAN": hh3cDot11L2CriticalVLAN,
       "hh3cDot11L2AuthorFailOffline": hh3cDot11L2AuthorFailOffline,
       "hh3cDot11L2AccountFailOffline": hh3cDot11L2AccountFailOffline,
       "hh3cDot11Dot1xHSEnable": hh3cDot11Dot1xHSEnable,
       "hh3cDot11Dot1xSecureHSEnable": hh3cDot11Dot1xSecureHSEnable,
       "hh3cDot11Dot1xReauthenEnable": hh3cDot11Dot1xReauthenEnable,
       "hh3cDot11Dot1xMandatoryDomain": hh3cDot11Dot1xMandatoryDomain,
       "hh3cDot11Dot1xMaxUserCount": hh3cDot11Dot1xMaxUserCount,
       "hh3cDot11MACAuthenDomain": hh3cDot11MACAuthenDomain,
       "hh3cDot11MACAuthenMaxUserCount": hh3cDot11MACAuthenMaxUserCount,
       "hh3cDot11IPLearningTable": hh3cDot11IPLearningTable,
       "hh3cDot11IPLearningEntry": hh3cDot11IPLearningEntry,
       "hh3cDot11IPLearningServiceName": hh3cDot11IPLearningServiceName,
       "hh3cDot11IPLearningType": hh3cDot11IPLearningType,
       "hh3cDot11IPLearningStatus": hh3cDot11IPLearningStatus,
       "hh3cDot11IPLearningVlanBitMapL": hh3cDot11IPLearningVlanBitMapL,
       "hh3cDot11IPLearningVlanBitMapH": hh3cDot11IPLearningVlanBitMapH,
       "hh3cDot11APConfigGroup": hh3cDot11APConfigGroup,
       "hh3cDot11APTemplateTable": hh3cDot11APTemplateTable,
       "hh3cDot11APTemplateEntry": hh3cDot11APTemplateEntry,
       "hh3cDot11APTemplateName": hh3cDot11APTemplateName,
       "hh3cDot11APSerialID": hh3cDot11APSerialID,
       "hh3cDot11TemplateAPModelAlias": hh3cDot11TemplateAPModelAlias,
       "hh3cDot11Description": hh3cDot11Description,
       "hh3cDot11APWorkMode": hh3cDot11APWorkMode,
       "hh3cDot11APTemplateRowStatus": hh3cDot11APTemplateRowStatus,
       "hh3cDot11APName": hh3cDot11APName,
       "hh3cDot11StatisInterv": hh3cDot11StatisInterv,
       "hh3cDot11APBroadcastProbeReply": hh3cDot11APBroadcastProbeReply,
       "hh3cDot11StaIdleTimerInterv": hh3cDot11StaIdleTimerInterv,
       "hh3cDot11StaKeepAliveTimerInterv": hh3cDot11StaKeepAliveTimerInterv,
       "hh3cDot11APCir": hh3cDot11APCir,
       "hh3cDot11APCbs": hh3cDot11APCbs,
       "hh3cDot11APPriorityLevel": hh3cDot11APPriorityLevel,
       "hh3cDot11APElementID": hh3cDot11APElementID,
       "hh3cDot11APDevDetectEnable": hh3cDot11APDevDetectEnable,
       "hh3cDot11APGetIPMethod": hh3cDot11APGetIPMethod,
       "hh3cDot11StatisIntervMode": hh3cDot11StatisIntervMode,
       "hh3cDot11ApTrapEnabled": hh3cDot11ApTrapEnabled,
       "hh3cDot11ApFmwUpdState": hh3cDot11ApFmwUpdState,
       "hh3cDot11StatisIntervModeCM": hh3cDot11StatisIntervModeCM,
       "hh3cDot11ApNasIDCM": hh3cDot11ApNasIDCM,
       "hh3cDot11ApCoveragetype": hh3cDot11ApCoveragetype,
       "hh3cDot11APControlAddressState": hh3cDot11APControlAddressState,
       "hh3cDot11APControlAddressIPv4": hh3cDot11APControlAddressIPv4,
       "hh3cDot11APControlAddressIPv6": hh3cDot11APControlAddressIPv6,
       "hh3cDot11APLocalACName": hh3cDot11APLocalACName,
       "hh3cDot11APEchoInterval": hh3cDot11APEchoInterval,
       "hh3cDot11APProvisionAPIPv4": hh3cDot11APProvisionAPIPv4,
       "hh3cDot11APProvisionIPv4Mask": hh3cDot11APProvisionIPv4Mask,
       "hh3cDot11APProvisionAPIPv6": hh3cDot11APProvisionAPIPv6,
       "hh3cDot11APProvisionIPv6PrefixLen": hh3cDot11APProvisionIPv6PrefixLen,
       "hh3cDot11APProvisionACIPv4": hh3cDot11APProvisionACIPv4,
       "hh3cDot11APProvisionACIpv6": hh3cDot11APProvisionACIpv6,
       "hh3cDot11APProvisionGateWayIPV4": hh3cDot11APProvisionGateWayIPV4,
       "hh3cDot11APProvisionGateWayIPV6": hh3cDot11APProvisionGateWayIPV6,
       "hh3cDot11APMapConfigFileName": hh3cDot11APMapConfigFileName,
       "hh3cDot11RadioToConfigTable": hh3cDot11RadioToConfigTable,
       "hh3cDot11RadioToConfigEntry": hh3cDot11RadioToConfigEntry,
       "hh3cDot11APTemplateNameCfg": hh3cDot11APTemplateNameCfg,
       "hh3cDot11CfgRadioID": hh3cDot11CfgRadioID,
       "hh3cDot11CfgRadioPolicyName": hh3cDot11CfgRadioPolicyName,
       "hh3cDot11CfgRadioType": hh3cDot11CfgRadioType,
       "hh3cDot11CfgChannel": hh3cDot11CfgChannel,
       "hh3cDot11CfgMaxTxPowerLevel": hh3cDot11CfgMaxTxPowerLevel,
       "hh3cDot11PreambleLen": hh3cDot11PreambleLen,
       "hh3cDot11CfgRadioStatus": hh3cDot11CfgRadioStatus,
       "hh3cDot11CfgRdElementID": hh3cDot11CfgRdElementID,
       "hh3cDot11CfgWorkMode": hh3cDot11CfgWorkMode,
       "hh3cDot11CfgPwrAttValue": hh3cDot11CfgPwrAttValue,
       "hh3cDot11RadioTxArithmetic": hh3cDot11RadioTxArithmetic,
       "hh3cDot11CfgChannelLockStat": hh3cDot11CfgChannelLockStat,
       "hh3cDot11CfgPowerLockStat": hh3cDot11CfgPowerLockStat,
       "hh3cDot11CfgLBRdGroupId": hh3cDot11CfgLBRdGroupId,
       "hh3cDot11CfgRRMSDRdGroupId": hh3cDot11CfgRRMSDRdGroupId,
       "hh3cDot11CfgRadioType2": hh3cDot11CfgRadioType2,
       "hh3cDot11CfgIDSEnable": hh3cDot11CfgIDSEnable,
       "hh3cDot11CfgSaEnable": hh3cDot11CfgSaEnable,
       "hh3cDot11CfgSaCltRtFFTData": hh3cDot11CfgSaCltRtFFTData,
       "hh3cDot11CfgSaBand": hh3cDot11CfgSaBand,
       "hh3cDot11CfgSaRptDevType": hh3cDot11CfgSaRptDevType,
       "hh3cDot11CfgSaTrapDevEnable": hh3cDot11CfgSaTrapDevEnable,
       "hh3cDot11CfgSaTrapDevType": hh3cDot11CfgSaTrapDevType,
       "hh3cDot11CfgSaTrapAQEnable": hh3cDot11CfgSaTrapAQEnable,
       "hh3cDot11CfgSaTrapAQThreshold": hh3cDot11CfgSaTrapAQThreshold,
       "hh3cDot11CfgSaDrivenRRMEnable": hh3cDot11CfgSaDrivenRRMEnable,
       "hh3cDot11CfgSaDrivenRRMSnt": hh3cDot11CfgSaDrivenRRMSnt,
       "hh3cDot11CfgSPInCirMode": hh3cDot11CfgSPInCirMode,
       "hh3cDot11CfgSPInCirValue": hh3cDot11CfgSPInCirValue,
       "hh3cDot11CfgSPOutCirMode": hh3cDot11CfgSPOutCirMode,
       "hh3cDot11CfgSPOutCirValue": hh3cDot11CfgSPOutCirValue,
       "hh3cDot11APServiceSetTable": hh3cDot11APServiceSetTable,
       "hh3cDot11APServiceSetEntry": hh3cDot11APServiceSetEntry,
       "hh3cDot11CfgServicePolicyID": hh3cDot11CfgServicePolicyID,
       "hh3cDot11SrvSetRowStatus": hh3cDot11SrvSetRowStatus,
       "hh3cDot11ServiceSetVlanId": hh3cDot11ServiceSetVlanId,
       "hh3cDot11ServiceSetVlanGroup": hh3cDot11ServiceSetVlanGroup,
       "hh3cDot11APSysInfoSetTable": hh3cDot11APSysInfoSetTable,
       "hh3cDot11APSysInfoSetEntry": hh3cDot11APSysInfoSetEntry,
       "hh3cDot11APSysNetID": hh3cDot11APSysNetID,
       "hh3cDot11APCpuUsageThreshold": hh3cDot11APCpuUsageThreshold,
       "hh3cDot11APMemUsageThreshold": hh3cDot11APMemUsageThreshold,
       "hh3cDot11APLimitTable": hh3cDot11APLimitTable,
       "hh3cDot11APLimitEntry": hh3cDot11APLimitEntry,
       "hh3cDot11APSsidNumLimit": hh3cDot11APSsidNumLimit,
       "hh3cDot11APUserCntLimit": hh3cDot11APUserCntLimit,
       "hh3cDot11APUserThreshold": hh3cDot11APUserThreshold,
       "hh3cDot11APIfSetTable": hh3cDot11APIfSetTable,
       "hh3cDot11APIfSetEntry": hh3cDot11APIfSetEntry,
       "hh3cDot11APSetIfIndex": hh3cDot11APSetIfIndex,
       "hh3cDot11APIfAlias": hh3cDot11APIfAlias,
       "hh3cDot11APServiceVlanTable": hh3cDot11APServiceVlanTable,
       "hh3cDot11APServiceVlanEntry": hh3cDot11APServiceVlanEntry,
       "hh3cDot11APServiceVlanSerialID": hh3cDot11APServiceVlanSerialID,
       "hh3cDot11APServiceVlanSPID": hh3cDot11APServiceVlanSPID,
       "hh3cDot11APServiceVlanId": hh3cDot11APServiceVlanId,
       "hh3cDot11APServiceVlanRowStatus": hh3cDot11APServiceVlanRowStatus,
       "hh3cDot11RadioConfigTable": hh3cDot11RadioConfigTable,
       "hh3cDot11RadioConfigEntry": hh3cDot11RadioConfigEntry,
       "hh3cDot11RCAPSerialID": hh3cDot11RCAPSerialID,
       "hh3cDot11RCRadioID": hh3cDot11RCRadioID,
       "hh3cDot11RCRadioType": hh3cDot11RCRadioType,
       "hh3cDot11RCChannel": hh3cDot11RCChannel,
       "hh3cDot11RCPreambleLen": hh3cDot11RCPreambleLen,
       "hh3cDot11RCPwrAttValue": hh3cDot11RCPwrAttValue,
       "hh3cDot11RCApPowerLevel": hh3cDot11RCApPowerLevel,
       "hh3cDot11RCDynamicChlState": hh3cDot11RCDynamicChlState,
       "hh3cDot11RCDynamicPowerState": hh3cDot11RCDynamicPowerState,
       "hh3cDot11RCRadioStatus": hh3cDot11RCRadioStatus,
       "hh3cDot11RCRadioRate": hh3cDot11RCRadioRate,
       "hh3cDot11RCPwrAdjustStepLength": hh3cDot11RCPwrAdjustStepLength,
       "hh3cDot11RCRadioType2": hh3cDot11RCRadioType2,
       "hh3cDot11RCPreambleLenCM": hh3cDot11RCPreambleLenCM,
       "hh3cDot11RCDynamicChlStateCM": hh3cDot11RCDynamicChlStateCM,
       "hh3cDot11RCRadioStatusCM": hh3cDot11RCRadioStatusCM,
       "hh3cDot11RCRadioRateCM": hh3cDot11RCRadioRateCM,
       "hh3cDot11RCDynamicPowerStateCM": hh3cDot11RCDynamicPowerStateCM,
       "hh3cDot11RCRssiThresholdCM": hh3cDot11RCRssiThresholdCM,
       "hh3cDot11RCDynamicChlStateSelfDecisiveCM": hh3cDot11RCDynamicChlStateSelfDecisiveCM,
       "hh3cDot11RCDynamicPowerStateSelfDecisiveCM": hh3cDot11RCDynamicPowerStateSelfDecisiveCM,
       "hh3cDot11RadioSSIDCfgTable": hh3cDot11RadioSSIDCfgTable,
       "hh3cDot11RadioSSIDCfgEntry": hh3cDot11RadioSSIDCfgEntry,
       "hh3cDot11RadioSSIDSerialID": hh3cDot11RadioSSIDSerialID,
       "hh3cDot11RadioSSIDRadioID": hh3cDot11RadioSSIDRadioID,
       "hh3cDot11RadioSSIDWLANID": hh3cDot11RadioSSIDWLANID,
       "hh3cDot11RadioSSIDIndex": hh3cDot11RadioSSIDIndex,
       "hh3cDot11RadioBSSID": hh3cDot11RadioBSSID,
       "hh3cDot11RadioSSIDRowStatus": hh3cDot11RadioSSIDRowStatus,
       "hh3cDot11APSerialIDTable": hh3cDot11APSerialIDTable,
       "hh3cDot11APSerialIDEntry": hh3cDot11APSerialIDEntry,
       "hh3cDot11SIDAPSerialID": hh3cDot11SIDAPSerialID,
       "hh3cDot11SIDAPWorkMode": hh3cDot11SIDAPWorkMode,
       "hh3cDot11SIDAPGetIPMethod": hh3cDot11SIDAPGetIPMethod,
       "hh3cDot11SIDAPTemplateName": hh3cDot11SIDAPTemplateName,
       "hh3cDot11SIDModelAlias": hh3cDot11SIDModelAlias,
       "hh3cDot11SIDAPDescription": hh3cDot11SIDAPDescription,
       "hh3cDot11SIDRowStatus": hh3cDot11SIDRowStatus,
       "hh3cDot11SIDAPName": hh3cDot11SIDAPName,
       "hh3cDot11SIDStatisInterv": hh3cDot11SIDStatisInterv,
       "hh3cDot11SIDAPBroadcastProbeReply": hh3cDot11SIDAPBroadcastProbeReply,
       "hh3cDot11SIDAPStaIdleTimerInterv": hh3cDot11SIDAPStaIdleTimerInterv,
       "hh3cDot11SIDStaKeepAliveTimerInterv": hh3cDot11SIDStaKeepAliveTimerInterv,
       "hh3cDot11SIDAPCir": hh3cDot11SIDAPCir,
       "hh3cDot11SIDAPCbs": hh3cDot11SIDAPCbs,
       "hh3cDot11SIDAPPriorityLevel": hh3cDot11SIDAPPriorityLevel,
       "hh3cDot11SIDAPElementID": hh3cDot11SIDAPElementID,
       "hh3cDot11SIDAPDevDetectEnable": hh3cDot11SIDAPDevDetectEnable,
       "hh3cDot11SIDAPStatisIntervMode": hh3cDot11SIDAPStatisIntervMode,
       "hh3cDot11SIDAPWorkModeCM": hh3cDot11SIDAPWorkModeCM,
       "hh3cDot11SIDEchoInterval": hh3cDot11SIDEchoInterval,
       "hh3cDot11APSTVlanTable": hh3cDot11APSTVlanTable,
       "hh3cDot11APSTVlanEntry": hh3cDot11APSTVlanEntry,
       "hh3cDot11CfgSTVLANID": hh3cDot11CfgSTVLANID,
       "hh3cDot11CfgSTNASPortID": hh3cDot11CfgSTNASPortID,
       "hh3cDot11CfgServiceSetRowStatus": hh3cDot11CfgServiceSetRowStatus,
       "hh3cDot11CfgSTNASID": hh3cDot11CfgSTNASID,
       "hh3cDot11RadioIntfConfigGroup": hh3cDot11RadioIntfConfigGroup,
       "hh3cDot11RadioIntfConfigTable": hh3cDot11RadioIntfConfigTable,
       "hh3cDot11RadioIntfConfigEntry": hh3cDot11RadioIntfConfigEntry,
       "hh3cDot11RadioIfIdx": hh3cDot11RadioIfIdx,
       "hh3cDot11RadioCfgBeaconIntvl": hh3cDot11RadioCfgBeaconIntvl,
       "hh3cDot11RadioCfgDtimIntvl": hh3cDot11RadioCfgDtimIntvl,
       "hh3cDot11RadioCfgRtsThreshold": hh3cDot11RadioCfgRtsThreshold,
       "hh3cDot11RadioCfgFragThreshold": hh3cDot11RadioCfgFragThreshold,
       "hh3cDot11RadioCfgShtRetryThld": hh3cDot11RadioCfgShtRetryThld,
       "hh3cDot11RadioCfglongRtrThld": hh3cDot11RadioCfglongRtrThld,
       "hh3cDot11RadioCfgMaxRxLifetime": hh3cDot11RadioCfgMaxRxLifetime,
       "hh3cDot11RadioCfgType": hh3cDot11RadioCfgType,
       "hh3cDot11RadioCfgChannel": hh3cDot11RadioCfgChannel,
       "hh3cDot11RadioCfgMaxTxPwrLvl": hh3cDot11RadioCfgMaxTxPwrLvl,
       "hh3cDot11RadioCfgPreambleLen": hh3cDot11RadioCfgPreambleLen,
       "hh3cDot11RadioCfgWorkMode": hh3cDot11RadioCfgWorkMode,
       "hh3cDot11RadioCfgOnly11gEnable": hh3cDot11RadioCfgOnly11gEnable,
       "hh3cDot11RadioCfgType2": hh3cDot11RadioCfgType2,
       "hh3cDot11RadioCfgRssithresholdCM": hh3cDot11RadioCfgRssithresholdCM,
       "hh3cDot11RadioIntfBindTable": hh3cDot11RadioIntfBindTable,
       "hh3cDot11RadioIntfBindEntry": hh3cDot11RadioIntfBindEntry,
       "hh3cDot11RadioIntfBindSvcPlcyID": hh3cDot11RadioIntfBindSvcPlcyID,
       "hh3cDot11RadioIntfBindIfIdx": hh3cDot11RadioIntfBindIfIdx,
       "hh3cDot11RadioIntfBindRowStatus": hh3cDot11RadioIntfBindRowStatus,
       "hh3cDot11DataRateConfigGroup": hh3cDot11DataRateConfigGroup,
       "hh3cDot11DataRateConfigTable": hh3cDot11DataRateConfigTable,
       "hh3cDot11DataRateConfigEntry": hh3cDot11DataRateConfigEntry,
       "hh3cDot11RadioTypeID": hh3cDot11RadioTypeID,
       "hh3cDot11SupportedRateSet": hh3cDot11SupportedRateSet,
       "hh3cDot11MandatoryRateSet": hh3cDot11MandatoryRateSet,
       "hh3cDot11DisabledRateSet": hh3cDot11DisabledRateSet,
       "hh3cDot11SmartRateSet": hh3cDot11SmartRateSet,
       "hh3cDot11InterfaceConfigGroup": hh3cDot11InterfaceConfigGroup,
       "hh3cDot11WlanEssIfTable": hh3cDot11WlanEssIfTable,
       "hh3cDot11WlanEssIfEntry": hh3cDot11WlanEssIfEntry,
       "hh3cDot11WlanEssIfNumber": hh3cDot11WlanEssIfNumber,
       "hh3cDot11WlanEssIfIndex": hh3cDot11WlanEssIfIndex,
       "hh3cDot11WlanEssRowStatus": hh3cDot11WlanEssRowStatus,
       "hh3cDot11WlanBssIfTable": hh3cDot11WlanBssIfTable,
       "hh3cDot11WlanBssIfEntry": hh3cDot11WlanBssIfEntry,
       "hh3cDot11WlanBssIfNumber": hh3cDot11WlanBssIfNumber,
       "hh3cDot11WlanBssIfIndex": hh3cDot11WlanBssIfIndex,
       "hh3cDot11WlanBssRowStatus": hh3cDot11WlanBssRowStatus,
       "hh3cDot11WLANEthernetIfTable": hh3cDot11WLANEthernetIfTable,
       "hh3cDot11WLANEthernetIfEntry": hh3cDot11WLANEthernetIfEntry,
       "hh3cDot11WlanEthernetIfNumber": hh3cDot11WlanEthernetIfNumber,
       "hh3cDot11WLANEthernetIfIndex": hh3cDot11WLANEthernetIfIndex,
       "hh3cDot11WlanEthernetRowStatus": hh3cDot11WlanEthernetRowStatus,
       "hh3cDot11PortSecurityTable": hh3cDot11PortSecurityTable,
       "hh3cDot11PortSecurityEntry": hh3cDot11PortSecurityEntry,
       "hh3cDot11PortSecurityMode": hh3cDot11PortSecurityMode,
       "hh3cDot11SecurityUserLoginTxKeyType": hh3cDot11SecurityUserLoginTxKeyType,
       "hh3cDot11SecurityPskKeyMode": hh3cDot11SecurityPskKeyMode,
       "hh3cDot11SecurityPskKeyString": hh3cDot11SecurityPskKeyString,
       "hh3cDot11WlanMeshIfTable": hh3cDot11WlanMeshIfTable,
       "hh3cDot11WlanMeshIfEntry": hh3cDot11WlanMeshIfEntry,
       "hh3cDot11WlanMeshIfNumber": hh3cDot11WlanMeshIfNumber,
       "hh3cDot11WlanMeshIfIndex": hh3cDot11WlanMeshIfIndex,
       "hh3cDot11WlanMeshRowStatus": hh3cDot11WlanMeshRowStatus,
       "hh3cDot11ACBackupGroup": hh3cDot11ACBackupGroup,
       "hh3cDot11BackupACAdrssIP": hh3cDot11BackupACAdrssIP,
       "hh3cDot11BackupACAdrssIPv6": hh3cDot11BackupACAdrssIPv6,
       "hh3cDot11RadioElementConfigGroup": hh3cDot11RadioElementConfigGroup,
       "hh3cDot11nRadioCfgTable": hh3cDot11nRadioCfgTable,
       "hh3cDot11nRadioCfgEntry": hh3cDot11nRadioCfgEntry,
       "hh3cDot11nRadioCfgIndex": hh3cDot11nRadioCfgIndex,
       "hh3cDot11nAMpduEnable": hh3cDot11nAMpduEnable,
       "hh3cDot11nAMsduEnable": hh3cDot11nAMsduEnable,
       "hh3cDot11nClientDot11nOnly": hh3cDot11nClientDot11nOnly,
       "hh3cDot11nChanelBand": hh3cDot11nChanelBand,
       "hh3cDot11nShortGiEnable": hh3cDot11nShortGiEnable,
       "hh3cDot11nClientDot11acOnly": hh3cDot11nClientDot11acOnly,
       "hh3cDot11nSupportMaxMcs": hh3cDot11nSupportMaxMcs,
       "hh3cDot11nMandatoryMaxMcs": hh3cDot11nMandatoryMaxMcs,
       "hh3cDot11RadioWDSTable": hh3cDot11RadioWDSTable,
       "hh3cDot11RadioWDSEntry": hh3cDot11RadioWDSEntry,
       "hh3cDot11RadioWDSIndex": hh3cDot11RadioWDSIndex,
       "hh3cDot11RadioWDSMode": hh3cDot11RadioWDSMode,
       "hh3cDot11RadioWDSNetWorkID": hh3cDot11RadioWDSNetWorkID,
       "hh3cDot11WDSSecPskKeyMode": hh3cDot11WDSSecPskKeyMode,
       "hh3cDot11WDSSecPskKeyString": hh3cDot11WDSSecPskKeyString,
       "hh3cDot11nRadioCfg2Table": hh3cDot11nRadioCfg2Table,
       "hh3cDot11nRadioCfg2Entry": hh3cDot11nRadioCfg2Entry,
       "hh3cDot11nRadioCfg2APIDIndex": hh3cDot11nRadioCfg2APIDIndex,
       "hh3cDot11nRadioCfg2RadioIDIndex": hh3cDot11nRadioCfg2RadioIDIndex,
       "hh3cDot11nRadioCfg2AMpduEnable": hh3cDot11nRadioCfg2AMpduEnable,
       "hh3cDot11nRadioCfg2AMsduEnable": hh3cDot11nRadioCfg2AMsduEnable,
       "hh3cDot11nRadioCfg2ClientDot11nOnly": hh3cDot11nRadioCfg2ClientDot11nOnly,
       "hh3cDot11nRadioCfg2ChannelBand": hh3cDot11nRadioCfg2ChannelBand,
       "hh3cDot11nRadioCfg2ShortGiEnable": hh3cDot11nRadioCfg2ShortGiEnable,
       "hh3cDot11nRadioCfg2AMpduEnableCM": hh3cDot11nRadioCfg2AMpduEnableCM,
       "hh3cDot11nRadioCfg2ChannelBandCM": hh3cDot11nRadioCfg2ChannelBandCM,
       "hh3cDot11nRadioCfg2ShortGiEnableCM": hh3cDot11nRadioCfg2ShortGiEnableCM,
       "hh3cDot11nRadioCfg2ClientDot11acOnly": hh3cDot11nRadioCfg2ClientDot11acOnly,
       "hh3cDot11nRadioCfg2ClientDot11nOnlyCM": hh3cDot11nRadioCfg2ClientDot11nOnlyCM,
       "hh3cDot11nRadioCfg2SupportMaxMcs": hh3cDot11nRadioCfg2SupportMaxMcs,
       "hh3cDot11nRadioCfg2MandatoryMaxMcs": hh3cDot11nRadioCfg2MandatoryMaxMcs,
       "hh3cDot11CfgNotifyGroup": hh3cDot11CfgNotifyGroup,
       "hh3cDot11CfgNotifications": hh3cDot11CfgNotifications,
       "hh3cDot11CfgCipherChange": hh3cDot11CfgCipherChange,
       "hh3cDot11CfgPSKChange": hh3cDot11CfgPSKChange,
       "hh3cDot11SSIDWepIDConflictTrap": hh3cDot11SSIDWepIDConflictTrap,
       "hh3cDot11CfgTrapVarObjects": hh3cDot11CfgTrapVarObjects,
       "hh3cDot11PreConflictTemplateNum": hh3cDot11PreConflictTemplateNum,
       "hh3cDot11CurrConflictTemplateNum": hh3cDot11CurrConflictTemplateNum,
       "hh3cDot11ConflictCipherIdx": hh3cDot11ConflictCipherIdx,
       "hh3cDot11ConfigureAPID": hh3cDot11ConfigureAPID,
       "hh3cDot11ConfigureRadioID": hh3cDot11ConfigureRadioID,
       "hh3cDot11ConfigureAPMacAddress": hh3cDot11ConfigureAPMacAddress,
       "hh3cDot11PreConflictTemplateSSID": hh3cDot11PreConflictTemplateSSID,
       "hh3cDot11CurrConflictTemplateSSID": hh3cDot11CurrConflictTemplateSSID,
       "hh3cDot11LocalACConfigGroup": hh3cDot11LocalACConfigGroup,
       "hh3cDot11LocalACTemplateTable": hh3cDot11LocalACTemplateTable,
       "hh3cDot11LocalACTemplateEntry": hh3cDot11LocalACTemplateEntry,
       "hh3cDot11LocalACTemplateName": hh3cDot11LocalACTemplateName,
       "hh3cDot11LocalACName": hh3cDot11LocalACName,
       "hh3cDot11LocalACSerialID": hh3cDot11LocalACSerialID,
       "hh3cDot11TemLocalACModelAlias": hh3cDot11TemLocalACModelAlias,
       "hh3cDot11LocalACTempRowStatus": hh3cDot11LocalACTempRowStatus,
       "hh3cDot11LocalACStatus": hh3cDot11LocalACStatus,
       "hh3cDot11LocalACIPAddress": hh3cDot11LocalACIPAddress,
       "hh3cDot11LocalACIPv6Address": hh3cDot11LocalACIPv6Address,
       "hh3cDot11EchoInterval": hh3cDot11EchoInterval,
       "hh3cDot11RetransInterval": hh3cDot11RetransInterval,
       "hh3cDot11RetransCount": hh3cDot11RetransCount,
       "hh3cDot11FirmwareUpgrade": hh3cDot11FirmwareUpgrade,
       "hh3cDot11RemoteConfigGroup": hh3cDot11RemoteConfigGroup,
       "hh3cDot11RemoteCfgApTable": hh3cDot11RemoteCfgApTable,
       "hh3cDot11RemoteCfgApEntry": hh3cDot11RemoteCfgApEntry,
       "hh3cDot11RmtApName": hh3cDot11RmtApName,
       "hh3cDot11RmtVlanList": hh3cDot11RmtVlanList,
       "hh3cDot11RmtCfgEnable": hh3cDot11RmtCfgEnable,
       "hh3cDot11RemoteCfgIFTable": hh3cDot11RemoteCfgIFTable,
       "hh3cDot11RemoteCfgIFEntry": hh3cDot11RemoteCfgIFEntry,
       "hh3cDot11RmtIfApName": hh3cDot11RmtIfApName,
       "hh3cDot11RmtIfType": hh3cDot11RmtIfType,
       "hh3cDot11RmtIfNum": hh3cDot11RmtIfNum,
       "hh3cDot11RmtIfName": hh3cDot11RmtIfName,
       "hh3cDot11RmtIfLinkType": hh3cDot11RmtIfLinkType,
       "hh3cDot11RmtIfAccessVlan": hh3cDot11RmtIfAccessVlan,
       "hh3cDot11RmtIfTrunkPvidVlan": hh3cDot11RmtIfTrunkPvidVlan,
       "hh3cDot11RmtIfTrunkVlanlist": hh3cDot11RmtIfTrunkVlanlist,
       "hh3cDot11RmtIfHybridPvidVlan": hh3cDot11RmtIfHybridPvidVlan,
       "hh3cDot11RmtIfHybVlanListTag": hh3cDot11RmtIfHybVlanListTag,
       "hh3cDot11RmtIfHybVlanListUnTag": hh3cDot11RmtIfHybVlanListUnTag,
       "hh3cDot11RmtIfIsolate": hh3cDot11RmtIfIsolate,
       "hh3cDot11RmtIfLinkAggGroupId": hh3cDot11RmtIfLinkAggGroupId,
       "hh3cDot11RmtIfManagement": hh3cDot11RmtIfManagement}
)
