# SNMP MIB module (TIMETRA-NAT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\nokia\TIMETRA-NAT-MIB

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

(InetAddress,
 InetAddressIPv4,
 InetAddressIPv6,
 InetAddressPrefixLength,
 InetAddressType,
 InetPortNumber) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressIPv4",
    "InetAddressIPv6",
    "InetAddressPrefixLength",
    "InetAddressType",
    "InetPortNumber")

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

(DateAndTime,
 DisplayString,
 MacAddress,
 PhysAddress,
 RowStatus,
 TextualConvention,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TimeStamp",
    "TruthValue")

(TmnxChassisIndexOrZero,
 TmnxSlotNum,
 TmnxSlotNumOrZero,
 tmnxCardSlotNum,
 tmnxChassisIndex,
 tmnxMDASlotNum) = mibBuilder.importSymbols(
    "TIMETRA-CHASSIS-MIB",
    "TmnxChassisIndexOrZero",
    "TmnxSlotNum",
    "TmnxSlotNumOrZero",
    "tmnxCardSlotNum",
    "tmnxChassisIndex",
    "tmnxMDASlotNum")

(TFilterID,) = mibBuilder.importSymbols(
    "TIMETRA-FILTER-MIB",
    "TFilterID")

(timetraSRMIBModules,
 tmnxSRConfs,
 tmnxSRNotifyPrefix,
 tmnxSRObjs) = mibBuilder.importSymbols(
    "TIMETRA-GLOBAL-MIB",
    "timetraSRMIBModules",
    "tmnxSRConfs",
    "tmnxSRNotifyPrefix",
    "tmnxSRObjs")

(svcOperGrpName,) = mibBuilder.importSymbols(
    "TIMETRA-SERV-MIB",
    "svcOperGrpName")

(tmnxSubInfoSubIdent,) = mibBuilder.importSymbols(
    "TIMETRA-SUBSCRIBER-MGMT-MIB",
    "tmnxSubInfoSubIdent")

(ServiceOperStatus,
 TFCSet,
 TIpProtocol,
 TItemDescription,
 TLNamedItem,
 TLNamedItemOrEmpty,
 TNamedItem,
 TNamedItemOrEmpty,
 TmnxActionType,
 TmnxAddressAndPrefixAddress,
 TmnxAddressAndPrefixPrefix,
 TmnxAddressAndPrefixType,
 TmnxAdminState,
 TmnxCreateOrigin,
 TmnxDisplayStringURL,
 TmnxEnabledDisabled,
 TmnxEsaNum,
 TmnxEsaVappNum,
 TmnxFpeIdOrZero,
 TmnxIsaScalingProfile,
 TmnxNatIsaGrpId,
 TmnxNatIsaGrpIdOrZero,
 TmnxNatLegacySubscriberType,
 TmnxNatWaterMark,
 TmnxOperState,
 TmnxPortID,
 TmnxServId,
 TmnxSubIdentString,
 TmnxSubIdentStringOrEmpty,
 TmnxSubRadServAlgorithm,
 TmnxSubRadiusAttrType,
 TmnxSubRadiusVendorId,
 TmnxSyslogFacility,
 TmnxSyslogSeverity,
 TmnxVRtrID,
 TmnxVRtrIDOrZero) = mibBuilder.importSymbols(
    "TIMETRA-TC-MIB",
    "ServiceOperStatus",
    "TFCSet",
    "TIpProtocol",
    "TItemDescription",
    "TLNamedItem",
    "TLNamedItemOrEmpty",
    "TNamedItem",
    "TNamedItemOrEmpty",
    "TmnxActionType",
    "TmnxAddressAndPrefixAddress",
    "TmnxAddressAndPrefixPrefix",
    "TmnxAddressAndPrefixType",
    "TmnxAdminState",
    "TmnxCreateOrigin",
    "TmnxDisplayStringURL",
    "TmnxEnabledDisabled",
    "TmnxEsaNum",
    "TmnxEsaVappNum",
    "TmnxFpeIdOrZero",
    "TmnxIsaScalingProfile",
    "TmnxNatIsaGrpId",
    "TmnxNatIsaGrpIdOrZero",
    "TmnxNatLegacySubscriberType",
    "TmnxNatWaterMark",
    "TmnxOperState",
    "TmnxPortID",
    "TmnxServId",
    "TmnxSubIdentString",
    "TmnxSubIdentStringOrEmpty",
    "TmnxSubRadServAlgorithm",
    "TmnxSubRadiusAttrType",
    "TmnxSubRadiusVendorId",
    "TmnxSyslogFacility",
    "TmnxSyslogSeverity",
    "TmnxVRtrID",
    "TmnxVRtrIDOrZero")

(vRtrID,
 vRtrIfIndex) = mibBuilder.importSymbols(
    "TIMETRA-VRTR-MIB",
    "vRtrID",
    "vRtrIfIndex")


# MODULE-IDENTITY

timetraNatMIBModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 1, 1, 3, 65)
)
if mibBuilder.loadTexts:
    timetraNatMIBModule.setRevisions(
        ("2025-03-15 00:00",
         "2024-03-15 00:00",
         "2023-03-15 00:00",
         "2021-03-15 00:00",
         "2010-03-15 00:00",
         "2018-03-15 00:00",
         "2017-03-15 00:00",
         "2016-01-01 00:00",
         "2015-01-01 00:00",
         "2014-02-01 00:00",
         "2012-08-01 00:00",
         "2011-02-01 00:00",
         "2009-07-31 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class TmnxNatAlgProtocols(TextualConvention, Bits):
    status = "current"
    namedValues = NamedValues(
        *(("ftp", 0),
          ("rtsp", 1),
          ("sip", 2),
          ("pptp", 3))
    )


class TmnxPerTenThousand(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000),
    )



class TmnxNatClassifierAction(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dnat", 1),
          ("forward", 2))
    )



class TmnxNatClassifierActionOrNone(TextualConvention, Integer32):
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
        *(("none", 0),
          ("dnat", 1),
          ("forward", 2))
    )



class TmnxNatFiltering(TextualConvention, Integer32):
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
        *(("endpointIndependent", 0),
          ("addressDependent", 1),
          ("addressAndPortDependent", 2))
    )



class TmnxNatFragmentIpMode(TextualConvention, Integer32):
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
        *(("disabled", 0),
          ("fragmentIpv6", 1),
          ("fragmentIpv6UnlessIpv4DfSet", 2))
    )



class TmnxNatFwdActionType(TextualConvention, Integer32):
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
        *(("create", 1),
          ("modify", 2),
          ("destroy", 3))
    )



class TmnxNatIsaMdaOperState(TextualConvention, Integer32):
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
        *(("unavail", 0),
          ("primary", 1),
          ("backup", 2),
          ("busy", 3))
    )



class TmnxNatMode(TextualConvention, Integer32):
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
        *(("auto", 0),
          ("napt", 1),
          ("oneToOne", 2))
    )



class TmnxNatFwdEntryDescription(DisplayString):
    status = "current"
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )



class TmnxNatPlType(TextualConvention, Integer32):
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
        *(("unknown", 0),
          ("largeScale", 1),
          ("l2Aware", 2),
          ("wlanGwAnchor", 3))
    )



class TmnxNatPolicyPurpose(TextualConvention, Integer32):
    status = "current"
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
        *(("nat", 1),
          ("firewall", 2),
          ("cups", 3),
          ("cpm", 4))
    )



class TmnxNatSubscriberIdString(DisplayString):
    status = "current"
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )



class TmnxNatUsageLevel(TextualConvention, Gauge32):
    status = "current"
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )



class TmnxNatUsageStatsType(TextualConvention, Integer32):
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
              10)
        )
    )
    namedValues = NamedValues(
        *(("hostsActive", 1),
          ("hostsPeak", 2),
          ("sessionsTcpCreated", 3),
          ("sessionsTcpDestroyed", 4),
          ("sessionsUdpCreated", 5),
          ("sessionsUdpDestroyed", 6),
          ("sessionsIcmpQueryCreated", 7),
          ("sessionsIcmpQueryDestroyed", 8),
          ("sessionsGreQueryCreated", 9),
          ("sessionsGreQueryDestroyed", 10))
    )



class TmnxNatMemberSubOrHostType(TextualConvention, Integer32):
    status = "current"
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
        *(("lsn", 1),
          ("dsm", 2),
          ("l2awareSub", 3),
          ("l2awareHost", 4))
    )



class TmnxNatInsideRoutesType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dynamic", 1),
          ("static", 2))
    )



# MIB Managed Objects in the order of their OIDs

_TmnxNatConformance_ObjectIdentity = ObjectIdentity
tmnxNatConformance = _TmnxNatConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 65)
)
_TmnxNatCompliances_ObjectIdentity = ObjectIdentity
tmnxNatCompliances = _TmnxNatCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 65, 1)
)
_TmnxNatGroups_ObjectIdentity = ObjectIdentity
tmnxNatGroups = _TmnxNatGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 65, 2)
)
_TmnxNatMGCompliances_ObjectIdentity = ObjectIdentity
tmnxNatMGCompliances = _TmnxNatMGCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 65, 3)
)
_TmnxNatMGGroups_ObjectIdentity = ObjectIdentity
tmnxNatMGGroups = _TmnxNatMGGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 65, 4)
)
_TmnxNat_ObjectIdentity = ObjectIdentity
tmnxNat = _TmnxNat_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65)
)
_TmnxNatObjs_ObjectIdentity = ObjectIdentity
tmnxNatObjs = _TmnxNatObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1)
)
_TmnxNatIsaObjs_ObjectIdentity = ObjectIdentity
tmnxNatIsaObjs = _TmnxNatIsaObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 1)
)
_TmnxNatIsaGrpObjs_ObjectIdentity = ObjectIdentity
tmnxNatIsaGrpObjs = _TmnxNatIsaGrpObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 1, 1)
)
_TmnxNatIsaGrpTable_Object = MibTable
tmnxNatIsaGrpTable = _TmnxNatIsaGrpTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 1, 1, 1)
)
if mibBuilder.loadTexts:
    tmnxNatIsaGrpTable.setStatus("current")
_TmnxNatIsaGrpEntry_Object = MibTableRow
tmnxNatIsaGrpEntry = _TmnxNatIsaGrpEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 1, 1, 1, 1)
)
tmnxNatIsaGrpEntry.setIndexNames(
    (0, "TIMETRA-NAT-MIB", "tmnxNatIsaGrpId"),
)
if mibBuilder.loadTexts:
    tmnxNatIsaGrpEntry.setStatus("current")
_TmnxNatIsaGrpId_Type = TmnxNatIsaGrpId
_TmnxNatIsaGrpId_Object = MibTableColumn
tmnxNatIsaGrpId = _TmnxNatIsaGrpId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 1, 1, 1, 1, 1),
    _TmnxNatIsaGrpId_Type()
)
tmnxNatIsaGrpId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxNatIsaGrpId.setStatus("current")
_TmnxNatIsaGrpRowStatus_Type = RowStatus
_TmnxNatIsaGrpRowStatus_Object = MibTableColumn
tmnxNatIsaGrpRowStatus = _TmnxNatIsaGrpRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 1, 1, 1, 1, 2),
    _TmnxNatIsaGrpRowStatus_Type()
)
tmnxNatIsaGrpRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxNatIsaGrpRowStatus.setStatus("current")
_TmnxNatIsaGrpLastMgmtChange_Type = TimeStamp
_TmnxNatIsaGrpLastMgmtChange_Object = MibTableColumn
tmnxNatIsaGrpLastMgmtChange = _TmnxNatIsaGrpLastMgmtChange_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 1, 1, 1, 1, 3),
    _TmnxNatIsaGrpLastMgmtChange_Type()
)
tmnxNatIsaGrpLastMgmtChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatIsaGrpLastMgmtChange.setStatus("current")


class _TmnxNatIsaGrpDescription_Type(TItemDescription):
    """Custom type tmnxNatIsaGrpDescription based on TItemDescription"""
    defaultValue = OctetString("")


_TmnxNatIsaGrpDescription_Type.__name__ = "TItemDescription"
_TmnxNatIsaGrpDescription_Object = MibTableColumn
tmnxNatIsaGrpDescription = _TmnxNatIsaGrpDescription_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 1, 1, 1, 1, 4),
    _TmnxNatIsaGrpDescription_Type()
)
tmnxNatIsaGrpDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxNatIsaGrpDescription.setStatus("current")


class _TmnxNatIsaGrpAdminState_Type(TmnxAdminState):
    """Custom type tmnxNatIsaGrpAdminState based on TmnxAdminState"""
    defaultValue = 3


_TmnxNatIsaGrpAdminState_Type.__name__ = "TmnxAdminState"
_TmnxNatIsaGrpAdminState_Object = MibTableColumn
tmnxNatIsaGrpAdminState = _TmnxNatIsaGrpAdminState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 1, 1, 1, 1, 5),
    _TmnxNatIsaGrpAdminState_Type()
)
tmnxNatIsaGrpAdminState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxNatIsaGrpAdminState.setStatus("current")


class _TmnxNatIsaGrpActiveMdaLimit_Type(Unsigned32):
    """Custom type tmnxNatIsaGrpActiveMdaLimit based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 28),
    )


_TmnxNatIsaGrpActiveMdaLimit_Type.__name__ = "Unsigned32"
_TmnxNatIsaGrpActiveMdaLimit_Object = MibTableColumn
tmnxNatIsaGrpActiveMdaLimit = _TmnxNatIsaGrpActiveMdaLimit_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 1, 1, 1, 1, 6),
    _TmnxNatIsaGrpActiveMdaLimit_Type()
)
tmnxNatIsaGrpActiveMdaLimit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxNatIsaGrpActiveMdaLimit.setStatus("current")


class _TmnxNatIsaGrpSessionResvCount_Type(Unsigned32):
    """Custom type tmnxNatIsaGrpSessionResvCount based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 6291456),
    )


_TmnxNatIsaGrpSessionResvCount_Type.__name__ = "Unsigned32"
_TmnxNatIsaGrpSessionResvCount_Object = MibTableColumn
tmnxNatIsaGrpSessionResvCount = _TmnxNatIsaGrpSessionResvCount_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 1, 1, 1, 1, 7),
    _TmnxNatIsaGrpSessionResvCount_Type()
)
tmnxNatIsaGrpSessionResvCount.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxNatIsaGrpSessionResvCount.setStatus("obsolete")


class _TmnxNatIsaGrpSessionWatermarkHi_Type(TmnxNatWaterMark):
    """Custom type tmnxNatIsaGrpSessionWatermarkHi based on TmnxNatWaterMark"""
    defaultValue = 0

    subtypeSpec = TmnxNatWaterMark.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 100),
    )


_TmnxNatIsaGrpSessionWatermarkHi_Type.__name__ = "TmnxNatWaterMark"
_TmnxNatIsaGrpSessionWatermarkHi_Object = MibTableColumn
tmnxNatIsaGrpSessionWatermarkHi = _TmnxNatIsaGrpSessionWatermarkHi_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 1, 1, 1, 1, 8),
    _TmnxNatIsaGrpSessionWatermarkHi_Type()
)
tmnxNatIsaGrpSessionWatermarkHi.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxNatIsaGrpSessionWatermarkHi.setStatus("obsolete")


class _TmnxNatIsaGrpSessionWatermarkLo_Type(TmnxNatWaterMark):
    """Custom type tmnxNatIsaGrpSessionWatermarkLo based on TmnxNatWaterMark"""
    defaultValue = 0

    subtypeSpec = TmnxNatWaterMark.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 99),
    )


_TmnxNatIsaGrpSessionWatermarkLo_Type.__name__ = "TmnxNatWaterMark"
_TmnxNatIsaGrpSessionWatermarkLo_Object = MibTableColumn
tmnxNatIsaGrpSessionWatermarkLo = _TmnxNatIsaGrpSessionWatermarkLo_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 1, 1, 1, 1, 9),
    _TmnxNatIsaGrpSessionWatermarkLo_Type()
)
tmnxNatIsaGrpSessionWatermarkLo.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxNatIsaGrpSessionWatermarkLo.setStatus("obsolete")


class _TmnxNatIsaGrpRedundancy_Type(Integer32):
    """Custom type tmnxNatIsaGrpRedundancy based on Integer32"""
    defaultValue = 0

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
        *(("activeStandby", 0),
          ("activeActive", 1),
          ("l2awareBypass", 2),
          ("interChassis", 3))
    )


_TmnxNatIsaGrpRedundancy_Type.__name__ = "Integer32"
_TmnxNatIsaGrpRedundancy_Object = MibTableColumn
tmnxNatIsaGrpRedundancy = _TmnxNatIsaGrpRedundancy_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 1, 1, 1, 1, 10),
    _TmnxNatIsaGrpRedundancy_Type()
)
tmnxNatIsaGrpRedundancy.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxNatIsaGrpRedundancy.setStatus("current")


class _TmnxNatIsaGrpFailedMdaLimit_Type(Unsigned32):
    """Custom type tmnxNatIsaGrpFailedMdaLimit based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_TmnxNatIsaGrpFailedMdaLimit_Type.__name__ = "Unsigned32"
_TmnxNatIsaGrpFailedMdaLimit_Object = MibTableColumn
tmnxNatIsaGrpFailedMdaLimit = _TmnxNatIsaGrpFailedMdaLimit_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 1, 1, 1, 1, 11),
    _TmnxNatIsaGrpFailedMdaLimit_Type()
)
tmnxNatIsaGrpFailedMdaLimit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxNatIsaGrpFailedMdaLimit.setStatus("current")
_TmnxNatIsaGrpOperState_Type = TmnxOperState
_TmnxNatIsaGrpOperState_Object = MibTableColumn
tmnxNatIsaGrpOperState = _TmnxNatIsaGrpOperState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 1, 1, 1, 1, 50),
    _TmnxNatIsaGrpOperState_Type()
)
tmnxNatIsaGrpOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatIsaGrpOperState.setStatus("current")
_TmnxNatIsaGrpDegraded_Type = TruthValue
_TmnxNatIsaGrpDegraded_Object = MibTableColumn
tmnxNatIsaGrpDegraded = _TmnxNatIsaGrpDegraded_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 1, 1, 1, 1, 51),
    _TmnxNatIsaGrpDegraded_Type()
)
tmnxNatIsaGrpDegraded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatIsaGrpDegraded.setStatus("current")


class _TmnxNatIsaGrpScalingProfile_Type(TmnxIsaScalingProfile):
    """Custom type tmnxNatIsaGrpScalingProfile based on TmnxIsaScalingProfile"""
    defaultValue = 1


_TmnxNatIsaGrpScalingProfile_Type.__name__ = "TmnxIsaScalingProfile"
_TmnxNatIsaGrpScalingProfile_Object = MibTableColumn
tmnxNatIsaGrpScalingProfile = _TmnxNatIsaGrpScalingProfile_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 1, 1, 1, 1, 53),
    _TmnxNatIsaGrpScalingProfile_Type()
)
tmnxNatIsaGrpScalingProfile.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxNatIsaGrpScalingProfile.setStatus("current")


class _TmnxNatIsaGrpSicrReplThreshold_Type(Unsigned32):
    """Custom type tmnxNatIsaGrpSicrReplThreshold based on Unsigned32"""
    defaultValue = 20

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 300),
    )


_TmnxNatIsaGrpSicrReplThreshold_Type.__name__ = "Unsigned32"
_TmnxNatIsaGrpSicrReplThreshold_Object = MibTableColumn
tmnxNatIsaGrpSicrReplThreshold = _TmnxNatIsaGrpSicrReplThreshold_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 1, 1, 1, 1, 54),
    _TmnxNatIsaGrpSicrReplThreshold_Type()
)
tmnxNatIsaGrpSicrReplThreshold.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxNatIsaGrpSicrReplThreshold.setStatus("current")
if mibBuilder.loadTexts:
    tmnxNatIsaGrpSicrReplThreshold.setUnits("seconds")


class _TmnxNatIsaGrpSicrToAfterSwitch_Type(Unsigned32):
    """Custom type tmnxNatIsaGrpSicrToAfterSwitch based on Unsigned32"""
    defaultValue = 50

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 50),
    )


_TmnxNatIsaGrpSicrToAfterSwitch_Type.__name__ = "Unsigned32"
_TmnxNatIsaGrpSicrToAfterSwitch_Object = MibTableColumn
tmnxNatIsaGrpSicrToAfterSwitch = _TmnxNatIsaGrpSicrToAfterSwitch_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 1, 1, 1, 1, 55),
    _TmnxNatIsaGrpSicrToAfterSwitch_Type()
)
tmnxNatIsaGrpSicrToAfterSwitch.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxNatIsaGrpSicrToAfterSwitch.setStatus("current")
if mibBuilder.loadTexts:
    tmnxNatIsaGrpSicrToAfterSwitch.setUnits("percent")


class _TmnxNatIsaGrpSicrRouter_Type(TmnxVRtrIDOrZero):
    """Custom type tmnxNatIsaGrpSicrRouter based on TmnxVRtrIDOrZero"""
    defaultValue = 0


_TmnxNatIsaGrpSicrRouter_Type.__name__ = "TmnxVRtrIDOrZero"
_TmnxNatIsaGrpSicrRouter_Object = MibTableColumn
tmnxNatIsaGrpSicrRouter = _TmnxNatIsaGrpSicrRouter_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 1, 1, 1, 1, 56),
    _TmnxNatIsaGrpSicrRouter_Type()
)
tmnxNatIsaGrpSicrRouter.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxNatIsaGrpSicrRouter.setStatus("current")


class _TmnxNatIsaGrpSicrLocAddrType_Type(InetAddressType):
    """Custom type tmnxNatIsaGrpSicrLocAddrType based on InetAddressType"""
    defaultValue = 0


_TmnxNatIsaGrpSicrLocAddrType_Type.__name__ = "InetAddressType"
_TmnxNatIsaGrpSicrLocAddrType_Object = MibTableColumn
tmnxNatIsaGrpSicrLocAddrType = _TmnxNatIsaGrpSicrLocAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 1, 1, 1, 1, 57),
    _TmnxNatIsaGrpSicrLocAddrType_Type()
)
tmnxNatIsaGrpSicrLocAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxNatIsaGrpSicrLocAddrType.setStatus("current")


class _TmnxNatIsaGrpSicrLocAddrStart_Type(InetAddress):
    """Custom type tmnxNatIsaGrpSicrLocAddrStart based on InetAddress"""
    defaultHexValue = ""

    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxNatIsaGrpSicrLocAddrStart_Type.__name__ = "InetAddress"
_TmnxNatIsaGrpSicrLocAddrStart_Object = MibTableColumn
tmnxNatIsaGrpSicrLocAddrStart = _TmnxNatIsaGrpSicrLocAddrStart_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 1, 1, 1, 1, 58),
    _TmnxNatIsaGrpSicrLocAddrStart_Type()
)
tmnxNatIsaGrpSicrLocAddrStart.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxNatIsaGrpSicrLocAddrStart.setStatus("current")


class _TmnxNatIsaGrpSicrRemAddrType_Type(InetAddressType):
    """Custom type tmnxNatIsaGrpSicrRemAddrType based on InetAddressType"""
    defaultValue = 0


_TmnxNatIsaGrpSicrRemAddrType_Type.__name__ = "InetAddressType"
_TmnxNatIsaGrpSicrRemAddrType_Object = MibTableColumn
tmnxNatIsaGrpSicrRemAddrType = _TmnxNatIsaGrpSicrRemAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 1, 1, 1, 1, 59),
    _TmnxNatIsaGrpSicrRemAddrType_Type()
)
tmnxNatIsaGrpSicrRemAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxNatIsaGrpSicrRemAddrType.setStatus("current")


class _TmnxNatIsaGrpSicrRemAddrStart_Type(InetAddress):
    """Custom type tmnxNatIsaGrpSicrRemAddrStart based on InetAddress"""
    defaultHexValue = ""

    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxNatIsaGrpSicrRemAddrStart_Type.__name__ = "InetAddress"
_TmnxNatIsaGrpSicrRemAddrStart_Object = MibTableColumn
tmnxNatIsaGrpSicrRemAddrStart = _TmnxNatIsaGrpSicrRemAddrStart_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 1, 1, 1, 1, 60),
    _TmnxNatIsaGrpSicrRemAddrStart_Type()
)
tmnxNatIsaGrpSicrRemAddrStart.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxNatIsaGrpSicrRemAddrStart.setStatus("current")


class _TmnxNatIsaGrpSicrIpMtu_Type(Unsigned32):
    """Custom type tmnxNatIsaGrpSicrIpMtu based on Unsigned32"""
    defaultValue = 1500

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(512, 9000),
    )


_TmnxNatIsaGrpSicrIpMtu_Type.__name__ = "Unsigned32"
_TmnxNatIsaGrpSicrIpMtu_Object = MibTableColumn
tmnxNatIsaGrpSicrIpMtu = _TmnxNatIsaGrpSicrIpMtu_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 1, 1, 1, 1, 61),
    _TmnxNatIsaGrpSicrIpMtu_Type()
)
tmnxNatIsaGrpSicrIpMtu.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxNatIsaGrpSicrIpMtu.setStatus("current")


class _TmnxNatIsaGrpSicrPreferred_Type(TruthValue):
    """Custom type tmnxNatIsaGrpSicrPreferred based on TruthValue"""
    defaultValue = 2


_TmnxNatIsaGrpSicrPreferred_Type.__name__ = "TruthValue"
_TmnxNatIsaGrpSicrPreferred_Object = MibTableColumn
tmnxNatIsaGrpSicrPreferred = _TmnxNatIsaGrpSicrPreferred_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 1, 1, 1, 1, 62),
    _TmnxNatIsaGrpSicrPreferred_Type()
)
tmnxNatIsaGrpSicrPreferred.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxNatIsaGrpSicrPreferred.setStatus("current")


class _TmnxNatIsaGrpSicrKaInterval_Type(Unsigned32):
    """Custom type tmnxNatIsaGrpSicrKaInterval based on Unsigned32"""
    defaultValue = 30

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 250),
    )


_TmnxNatIsaGrpSicrKaInterval_Type.__name__ = "Unsigned32"
_TmnxNatIsaGrpSicrKaInterval_Object = MibTableColumn
tmnxNatIsaGrpSicrKaInterval = _TmnxNatIsaGrpSicrKaInterval_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 1, 1, 1, 1, 63),
    _TmnxNatIsaGrpSicrKaInterval_Type()
)
tmnxNatIsaGrpSicrKaInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxNatIsaGrpSicrKaInterval.setStatus("current")
if mibBuilder.loadTexts:
    tmnxNatIsaGrpSicrKaInterval.setUnits("deciseconds")


class _TmnxNatIsaGrpSicrKaDropcount_Type(Unsigned32):
    """Custom type tmnxNatIsaGrpSicrKaDropcount based on Unsigned32"""
    defaultValue = 2

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 20),
    )


_TmnxNatIsaGrpSicrKaDropcount_Type.__name__ = "Unsigned32"
_TmnxNatIsaGrpSicrKaDropcount_Object = MibTableColumn
tmnxNatIsaGrpSicrKaDropcount = _TmnxNatIsaGrpSicrKaDropcount_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 1, 1, 1, 1, 64),
    _TmnxNatIsaGrpSicrKaDropcount_Type()
)
tmnxNatIsaGrpSicrKaDropcount.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxNatIsaGrpSicrKaDropcount.setStatus("current")


class _TmnxNatIsaGrpOperGroup_Type(TNamedItemOrEmpty):
    """Custom type tmnxNatIsaGrpOperGroup based on TNamedItemOrEmpty"""
    defaultValue = OctetString("")


_TmnxNatIsaGrpOperGroup_Type.__name__ = "TNamedItemOrEmpty"
_TmnxNatIsaGrpOperGroup_Object = MibTableColumn
tmnxNatIsaGrpOperGroup = _TmnxNatIsaGrpOperGroup_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 1, 1, 1, 1, 65),
    _TmnxNatIsaGrpOperGroup_Type()
)
tmnxNatIsaGrpOperGroup.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxNatIsaGrpOperGroup.setStatus("current")


class _TmnxNatIsaGrpSicrSync_Type(TruthValue):
    """Custom type tmnxNatIsaGrpSicrSync based on TruthValue"""
    defaultValue = 1


_TmnxNatIsaGrpSicrSync_Type.__name__ = "TruthValue"
_TmnxNatIsaGrpSicrSync_Object = MibTableColumn
tmnxNatIsaGrpSicrSync = _TmnxNatIsaGrpSicrSync_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 1, 1, 1, 1, 66),
    _TmnxNatIsaGrpSicrSync_Type()
)
tmnxNatIsaGrpSicrSync.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxNatIsaGrpSicrSync.setStatus("current")


class _TmnxNatIsaGrpMonitorOperGroup_Type(TNamedItemOrEmpty):
    """Custom type tmnxNatIsaGrpMonitorOperGroup based on TNamedItemOrEmpty"""
    defaultValue = OctetString("")


_TmnxNatIsaGrpMonitorOperGroup_Type.__name__ = "TNamedItemOrEmpty"
_TmnxNatIsaGrpMonitorOperGroup_Object = MibTableColumn
tmnxNatIsaGrpMonitorOperGroup = _TmnxNatIsaGrpMonitorOperGroup_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 1, 1, 1, 1, 67),
    _TmnxNatIsaGrpMonitorOperGroup_Type()
)
tmnxNatIsaGrpMonitorOperGroup.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxNatIsaGrpMonitorOperGroup.setStatus("current")
_TmnxNatGrpCfgTable_Object = MibTable
tmnxNatGrpCfgTable = _TmnxNatGrpCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 1, 1, 3)
)
if mibBuilder.loadTexts:
    tmnxNatGrpCfgTable.setStatus("current")
_TmnxNatGrpCfgEntry_Object = MibTableRow
tmnxNatGrpCfgEntry = _TmnxNatGrpCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 1, 1, 3, 1)
)
tmnxNatGrpCfgEntry.setIndexNames(
    (0, "TIMETRA-NAT-MIB", "tmnxNatGrpCfgId"),
)
if mibBuilder.loadTexts:
    tmnxNatGrpCfgEntry.setStatus("current")
_TmnxNatGrpCfgId_Type = TmnxNatIsaGrpId
_TmnxNatGrpCfgId_Object = MibTableColumn
tmnxNatGrpCfgId = _TmnxNatGrpCfgId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 1, 1, 3, 1, 1),
    _TmnxNatGrpCfgId_Type()
)
tmnxNatGrpCfgId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxNatGrpCfgId.setStatus("current")
_TmnxNatGrpCfgLastMgmtChange_Type = TimeStamp
_TmnxNatGrpCfgLastMgmtChange_Object = MibTableColumn
tmnxNatGrpCfgLastMgmtChange = _TmnxNatGrpCfgLastMgmtChange_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 1, 1, 3, 1, 2),
    _TmnxNatGrpCfgLastMgmtChange_Type()
)
tmnxNatGrpCfgLastMgmtChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatGrpCfgLastMgmtChange.setStatus("current")


class _TmnxNatGrpCfgSessionResvCount_Type(Unsigned32):
    """Custom type tmnxNatGrpCfgSessionResvCount based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 6291456),
    )


_TmnxNatGrpCfgSessionResvCount_Type.__name__ = "Unsigned32"
_TmnxNatGrpCfgSessionResvCount_Object = MibTableColumn
tmnxNatGrpCfgSessionResvCount = _TmnxNatGrpCfgSessionResvCount_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 1, 1, 3, 1, 3),
    _TmnxNatGrpCfgSessionResvCount_Type()
)
tmnxNatGrpCfgSessionResvCount.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxNatGrpCfgSessionResvCount.setStatus("current")


class _TmnxNatGrpCfgSessionWatermarkHi_Type(TmnxNatWaterMark):
    """Custom type tmnxNatGrpCfgSessionWatermarkHi based on TmnxNatWaterMark"""
    defaultValue = 0

    subtypeSpec = TmnxNatWaterMark.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 100),
    )


_TmnxNatGrpCfgSessionWatermarkHi_Type.__name__ = "TmnxNatWaterMark"
_TmnxNatGrpCfgSessionWatermarkHi_Object = MibTableColumn
tmnxNatGrpCfgSessionWatermarkHi = _TmnxNatGrpCfgSessionWatermarkHi_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 1, 1, 3, 1, 4),
    _TmnxNatGrpCfgSessionWatermarkHi_Type()
)
tmnxNatGrpCfgSessionWatermarkHi.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxNatGrpCfgSessionWatermarkHi.setStatus("current")


class _TmnxNatGrpCfgSessionWatermarkLo_Type(TmnxNatWaterMark):
    """Custom type tmnxNatGrpCfgSessionWatermarkLo based on TmnxNatWaterMark"""
    defaultValue = 0

    subtypeSpec = TmnxNatWaterMark.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 99),
    )


_TmnxNatGrpCfgSessionWatermarkLo_Type.__name__ = "TmnxNatWaterMark"
_TmnxNatGrpCfgSessionWatermarkLo_Object = MibTableColumn
tmnxNatGrpCfgSessionWatermarkLo = _TmnxNatGrpCfgSessionWatermarkLo_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 1, 1, 3, 1, 5),
    _TmnxNatGrpCfgSessionWatermarkLo_Type()
)
tmnxNatGrpCfgSessionWatermarkLo.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxNatGrpCfgSessionWatermarkLo.setStatus("current")


class _TmnxNatGrpCfgAccountingPlcy_Type(TNamedItemOrEmpty):
    """Custom type tmnxNatGrpCfgAccountingPlcy based on TNamedItemOrEmpty"""
    defaultHexValue = ""


_TmnxNatGrpCfgAccountingPlcy_Type.__name__ = "TNamedItemOrEmpty"
_TmnxNatGrpCfgAccountingPlcy_Object = MibTableColumn
tmnxNatGrpCfgAccountingPlcy = _TmnxNatGrpCfgAccountingPlcy_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 1, 1, 3, 1, 6),
    _TmnxNatGrpCfgAccountingPlcy_Type()
)
tmnxNatGrpCfgAccountingPlcy.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxNatGrpCfgAccountingPlcy.setStatus("current")


class _TmnxNatGrpCfgSessionUpnpMapLimit_Type(Unsigned32):
    """Custom type tmnxNatGrpCfgSessionUpnpMapLimit based on Unsigned32"""
    defaultValue = 524288

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 524288),
    )


_TmnxNatGrpCfgSessionUpnpMapLimit_Type.__name__ = "Unsigned32"
_TmnxNatGrpCfgSessionUpnpMapLimit_Object = MibTableColumn
tmnxNatGrpCfgSessionUpnpMapLimit = _TmnxNatGrpCfgSessionUpnpMapLimit_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 1, 1, 3, 1, 7),
    _TmnxNatGrpCfgSessionUpnpMapLimit_Type()
)
tmnxNatGrpCfgSessionUpnpMapLimit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxNatGrpCfgSessionUpnpMapLimit.setStatus("current")


class _TmnxNatGrpCfgNoLsnSubBlksFree_Type(TruthValue):
    """Custom type tmnxNatGrpCfgNoLsnSubBlksFree based on TruthValue"""
    defaultValue = 2


_TmnxNatGrpCfgNoLsnSubBlksFree_Type.__name__ = "TruthValue"
_TmnxNatGrpCfgNoLsnSubBlksFree_Object = MibTableColumn
tmnxNatGrpCfgNoLsnSubBlksFree = _TmnxNatGrpCfgNoLsnSubBlksFree_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 1, 1, 3, 1, 8),
    _TmnxNatGrpCfgNoLsnSubBlksFree_Type()
)
tmnxNatGrpCfgNoLsnSubBlksFree.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxNatGrpCfgNoLsnSubBlksFree.setStatus("current")


class _TmnxNatGrpCfgLsn_Type(TmnxEnabledDisabled):
    """Custom type tmnxNatGrpCfgLsn based on TmnxEnabledDisabled"""
    defaultValue = 1


_TmnxNatGrpCfgLsn_Type.__name__ = "TmnxEnabledDisabled"
_TmnxNatGrpCfgLsn_Object = MibTableColumn
tmnxNatGrpCfgLsn = _TmnxNatGrpCfgLsn_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 1, 1, 3, 1, 9),
    _TmnxNatGrpCfgLsn_Type()
)
tmnxNatGrpCfgLsn.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxNatGrpCfgLsn.setStatus("current")


class _TmnxNatGrpCfgNoLsnEvents_Type(TruthValue):
    """Custom type tmnxNatGrpCfgNoLsnEvents based on TruthValue"""
    defaultValue = 1


_TmnxNatGrpCfgNoLsnEvents_Type.__name__ = "TruthValue"
_TmnxNatGrpCfgNoLsnEvents_Object = MibTableColumn
tmnxNatGrpCfgNoLsnEvents = _TmnxNatGrpCfgNoLsnEvents_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 1, 1, 3, 1, 10),
    _TmnxNatGrpCfgNoLsnEvents_Type()
)
tmnxNatGrpCfgNoLsnEvents.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxNatGrpCfgNoLsnEvents.setStatus("current")


class _TmnxNatGrpCfgLoadBalancing_Type(Integer32):
    """Custom type tmnxNatGrpCfgLoadBalancing based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("profile1", 1),
          ("profile2", 2))
    )


_TmnxNatGrpCfgLoadBalancing_Type.__name__ = "Integer32"
_TmnxNatGrpCfgLoadBalancing_Object = MibTableColumn
tmnxNatGrpCfgLoadBalancing = _TmnxNatGrpCfgLoadBalancing_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 1, 1, 3, 1, 11),
    _TmnxNatGrpCfgLoadBalancing_Type()
)
tmnxNatGrpCfgLoadBalancing.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxNatGrpCfgLoadBalancing.setStatus("obsolete")


class _TmnxNatGrpCfgLogPerUpdInterval_Type(Unsigned32):
    """Custom type tmnxNatGrpCfgLogPerUpdInterval based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(10, 1440),
    )


_TmnxNatGrpCfgLogPerUpdInterval_Type.__name__ = "Unsigned32"
_TmnxNatGrpCfgLogPerUpdInterval_Object = MibTableColumn
tmnxNatGrpCfgLogPerUpdInterval = _TmnxNatGrpCfgLogPerUpdInterval_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 1, 1, 3, 1, 13),
    _TmnxNatGrpCfgLogPerUpdInterval_Type()
)
tmnxNatGrpCfgLogPerUpdInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxNatGrpCfgLogPerUpdInterval.setStatus("current")
if mibBuilder.loadTexts:
    tmnxNatGrpCfgLogPerUpdInterval.setUnits("minutes")


class _TmnxNatGrpCfgLogPerUpdRateLimit_Type(Unsigned32):
    """Custom type tmnxNatGrpCfgLogPerUpdRateLimit based on Unsigned32"""
    defaultValue = 10000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100000),
    )


_TmnxNatGrpCfgLogPerUpdRateLimit_Type.__name__ = "Unsigned32"
_TmnxNatGrpCfgLogPerUpdRateLimit_Object = MibTableColumn
tmnxNatGrpCfgLogPerUpdRateLimit = _TmnxNatGrpCfgLogPerUpdRateLimit_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 1, 1, 3, 1, 14),
    _TmnxNatGrpCfgLogPerUpdRateLimit_Type()
)
tmnxNatGrpCfgLogPerUpdRateLimit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxNatGrpCfgLogPerUpdRateLimit.setStatus("current")
if mibBuilder.loadTexts:
    tmnxNatGrpCfgLogPerUpdRateLimit.setUnits("messages per second")
_TmnxNatIsaRecoveryAction_ObjectIdentity = ObjectIdentity
tmnxNatIsaRecoveryAction = _TmnxNatIsaRecoveryAction_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 1, 1, 4)
)
_TmnxNatIsaRecovActCardSlotNum_Type = TmnxSlotNum
_TmnxNatIsaRecovActCardSlotNum_Object = MibScalar
tmnxNatIsaRecovActCardSlotNum = _TmnxNatIsaRecovActCardSlotNum_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 1, 1, 4, 1),
    _TmnxNatIsaRecovActCardSlotNum_Type()
)
tmnxNatIsaRecovActCardSlotNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxNatIsaRecovActCardSlotNum.setStatus("current")


class _TmnxNatIsaRecovActCardMDANum_Type(Unsigned32):
    """Custom type tmnxNatIsaRecovActCardMDANum based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_TmnxNatIsaRecovActCardMDANum_Type.__name__ = "Unsigned32"
_TmnxNatIsaRecovActCardMDANum_Object = MibScalar
tmnxNatIsaRecovActCardMDANum = _TmnxNatIsaRecovActCardMDANum_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 1, 1, 4, 2),
    _TmnxNatIsaRecovActCardMDANum_Type()
)
tmnxNatIsaRecovActCardMDANum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxNatIsaRecovActCardMDANum.setStatus("current")
_TmnxNatIsaRecovActActionGo_Type = TmnxActionType
_TmnxNatIsaRecovActActionGo_Object = MibScalar
tmnxNatIsaRecovActActionGo = _TmnxNatIsaRecovActActionGo_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 1, 1, 4, 3),
    _TmnxNatIsaRecovActActionGo_Type()
)
tmnxNatIsaRecovActActionGo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxNatIsaRecovActActionGo.setStatus("current")


class _TmnxNatIsaRecovActActionResult_Type(Integer32):
    """Custom type tmnxNatIsaRecovActActionResult based on Integer32"""
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
        *(("ack", 0),
          ("nak", 1),
          ("notUsed", 2),
          ("notActive", 3),
          ("notInBypass", 4))
    )


_TmnxNatIsaRecovActActionResult_Type.__name__ = "Integer32"
_TmnxNatIsaRecovActActionResult_Object = MibScalar
tmnxNatIsaRecovActActionResult = _TmnxNatIsaRecovActActionResult_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 1, 1, 4, 4),
    _TmnxNatIsaRecovActActionResult_Type()
)
tmnxNatIsaRecovActActionResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatIsaRecovActActionResult.setStatus("current")
_TmnxNatGrpMonOperGrpTable_Object = MibTable
tmnxNatGrpMonOperGrpTable = _TmnxNatGrpMonOperGrpTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 1, 1, 5)
)
if mibBuilder.loadTexts:
    tmnxNatGrpMonOperGrpTable.setStatus("current")
_TmnxNatGrpMonOperGrpEntry_Object = MibTableRow
tmnxNatGrpMonOperGrpEntry = _TmnxNatGrpMonOperGrpEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 1, 1, 5, 1)
)
tmnxNatGrpMonOperGrpEntry.setIndexNames(
    (0, "TIMETRA-NAT-MIB", "tmnxNatIsaGrpId"),
    (0, "TIMETRA-SERV-MIB", "svcOperGrpName"),
)
if mibBuilder.loadTexts:
    tmnxNatGrpMonOperGrpEntry.setStatus("current")
_TmnxNatGrpMonOperGrpRowStatus_Type = RowStatus
_TmnxNatGrpMonOperGrpRowStatus_Object = MibTableColumn
tmnxNatGrpMonOperGrpRowStatus = _TmnxNatGrpMonOperGrpRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 1, 1, 5, 1, 1),
    _TmnxNatGrpMonOperGrpRowStatus_Type()
)
tmnxNatGrpMonOperGrpRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxNatGrpMonOperGrpRowStatus.setStatus("current")
_TmnxNatGrpMonOperGrpLastCh_Type = TimeStamp
_TmnxNatGrpMonOperGrpLastCh_Object = MibTableColumn
tmnxNatGrpMonOperGrpLastCh = _TmnxNatGrpMonOperGrpLastCh_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 1, 1, 5, 1, 2),
    _TmnxNatGrpMonOperGrpLastCh_Type()
)
tmnxNatGrpMonOperGrpLastCh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatGrpMonOperGrpLastCh.setStatus("current")


class _TmnxNatGrpMonOperGrpHlthDrop_Type(Unsigned32):
    """Custom type tmnxNatGrpMonOperGrpHlthDrop based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_TmnxNatGrpMonOperGrpHlthDrop_Type.__name__ = "Unsigned32"
_TmnxNatGrpMonOperGrpHlthDrop_Object = MibTableColumn
tmnxNatGrpMonOperGrpHlthDrop = _TmnxNatGrpMonOperGrpHlthDrop_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 1, 1, 5, 1, 3),
    _TmnxNatGrpMonOperGrpHlthDrop_Type()
)
tmnxNatGrpMonOperGrpHlthDrop.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxNatGrpMonOperGrpHlthDrop.setStatus("current")
_TmnxNatGrpMonOperGrpActHlthDrop_Type = Unsigned32
_TmnxNatGrpMonOperGrpActHlthDrop_Object = MibTableColumn
tmnxNatGrpMonOperGrpActHlthDrop = _TmnxNatGrpMonOperGrpActHlthDrop_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 1, 1, 5, 1, 4),
    _TmnxNatGrpMonOperGrpActHlthDrop_Type()
)
tmnxNatGrpMonOperGrpActHlthDrop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatGrpMonOperGrpActHlthDrop.setStatus("current")
_TmnxNatGrpMonPortTable_Object = MibTable
tmnxNatGrpMonPortTable = _TmnxNatGrpMonPortTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 1, 1, 6)
)
if mibBuilder.loadTexts:
    tmnxNatGrpMonPortTable.setStatus("current")
_TmnxNatGrpMonPortEntry_Object = MibTableRow
tmnxNatGrpMonPortEntry = _TmnxNatGrpMonPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 1, 1, 6, 1)
)
tmnxNatGrpMonPortEntry.setIndexNames(
    (0, "TIMETRA-NAT-MIB", "tmnxNatIsaGrpId"),
    (0, "TIMETRA-NAT-MIB", "tmnxNatGrpMonPortId"),
)
if mibBuilder.loadTexts:
    tmnxNatGrpMonPortEntry.setStatus("current")
_TmnxNatGrpMonPortId_Type = TmnxPortID
_TmnxNatGrpMonPortId_Object = MibTableColumn
tmnxNatGrpMonPortId = _TmnxNatGrpMonPortId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 1, 1, 6, 1, 1),
    _TmnxNatGrpMonPortId_Type()
)
tmnxNatGrpMonPortId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxNatGrpMonPortId.setStatus("current")
_TmnxNatGrpMonPortRowStatus_Type = RowStatus
_TmnxNatGrpMonPortRowStatus_Object = MibTableColumn
tmnxNatGrpMonPortRowStatus = _TmnxNatGrpMonPortRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 1, 1, 6, 1, 2),
    _TmnxNatGrpMonPortRowStatus_Type()
)
tmnxNatGrpMonPortRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxNatGrpMonPortRowStatus.setStatus("current")
_TmnxNatGrpMonPortLastCh_Type = TimeStamp
_TmnxNatGrpMonPortLastCh_Object = MibTableColumn
tmnxNatGrpMonPortLastCh = _TmnxNatGrpMonPortLastCh_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 1, 1, 6, 1, 3),
    _TmnxNatGrpMonPortLastCh_Type()
)
tmnxNatGrpMonPortLastCh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatGrpMonPortLastCh.setStatus("current")


class _TmnxNatGrpMonPortHealthDrop_Type(Unsigned32):
    """Custom type tmnxNatGrpMonPortHealthDrop based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_TmnxNatGrpMonPortHealthDrop_Type.__name__ = "Unsigned32"
_TmnxNatGrpMonPortHealthDrop_Object = MibTableColumn
tmnxNatGrpMonPortHealthDrop = _TmnxNatGrpMonPortHealthDrop_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 1, 1, 6, 1, 4),
    _TmnxNatGrpMonPortHealthDrop_Type()
)
tmnxNatGrpMonPortHealthDrop.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxNatGrpMonPortHealthDrop.setStatus("current")
_TmnxNatGrpMonPortActHealthDrop_Type = Unsigned32
_TmnxNatGrpMonPortActHealthDrop_Object = MibTableColumn
tmnxNatGrpMonPortActHealthDrop = _TmnxNatGrpMonPortActHealthDrop_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 1, 1, 6, 1, 5),
    _TmnxNatGrpMonPortActHealthDrop_Type()
)
tmnxNatGrpMonPortActHealthDrop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatGrpMonPortActHealthDrop.setStatus("current")
_TmnxNatMapTGrpTable_Object = MibTable
tmnxNatMapTGrpTable = _TmnxNatMapTGrpTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 1, 1, 7)
)
if mibBuilder.loadTexts:
    tmnxNatMapTGrpTable.setStatus("current")
_TmnxNatMapTGrpEntry_Object = MibTableRow
tmnxNatMapTGrpEntry = _TmnxNatMapTGrpEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 1, 1, 7, 1)
)
tmnxNatMapTGrpEntry.setIndexNames(
    (0, "TIMETRA-NAT-MIB", "tmnxNatMapTGrpIsaGrpId"),
)
if mibBuilder.loadTexts:
    tmnxNatMapTGrpEntry.setStatus("current")
_TmnxNatMapTGrpIsaGrpId_Type = TmnxNatIsaGrpId
_TmnxNatMapTGrpIsaGrpId_Object = MibTableColumn
tmnxNatMapTGrpIsaGrpId = _TmnxNatMapTGrpIsaGrpId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 1, 1, 7, 1, 1),
    _TmnxNatMapTGrpIsaGrpId_Type()
)
tmnxNatMapTGrpIsaGrpId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxNatMapTGrpIsaGrpId.setStatus("current")
_TmnxNatMapTGrpRowStatus_Type = RowStatus
_TmnxNatMapTGrpRowStatus_Object = MibTableColumn
tmnxNatMapTGrpRowStatus = _TmnxNatMapTGrpRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 1, 1, 7, 1, 2),
    _TmnxNatMapTGrpRowStatus_Type()
)
tmnxNatMapTGrpRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxNatMapTGrpRowStatus.setStatus("current")
_TmnxNatMapTGrpLastCh_Type = TimeStamp
_TmnxNatMapTGrpLastCh_Object = MibTableColumn
tmnxNatMapTGrpLastCh = _TmnxNatMapTGrpLastCh_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 1, 1, 7, 1, 3),
    _TmnxNatMapTGrpLastCh_Type()
)
tmnxNatMapTGrpLastCh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatMapTGrpLastCh.setStatus("current")


class _TmnxNatMapTGrpDescription_Type(TItemDescription):
    """Custom type tmnxNatMapTGrpDescription based on TItemDescription"""
    defaultValue = OctetString("")


_TmnxNatMapTGrpDescription_Type.__name__ = "TItemDescription"
_TmnxNatMapTGrpDescription_Object = MibTableColumn
tmnxNatMapTGrpDescription = _TmnxNatMapTGrpDescription_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 1, 1, 7, 1, 4),
    _TmnxNatMapTGrpDescription_Type()
)
tmnxNatMapTGrpDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxNatMapTGrpDescription.setStatus("current")


class _TmnxNatMapTGrpAdminState_Type(TmnxAdminState):
    """Custom type tmnxNatMapTGrpAdminState based on TmnxAdminState"""
    defaultValue = 3


_TmnxNatMapTGrpAdminState_Type.__name__ = "TmnxAdminState"
_TmnxNatMapTGrpAdminState_Object = MibTableColumn
tmnxNatMapTGrpAdminState = _TmnxNatMapTGrpAdminState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 1, 1, 7, 1, 5),
    _TmnxNatMapTGrpAdminState_Type()
)
tmnxNatMapTGrpAdminState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxNatMapTGrpAdminState.setStatus("current")
_TmnxNatMapTGrpOperState_Type = TmnxOperState
_TmnxNatMapTGrpOperState_Object = MibTableColumn
tmnxNatMapTGrpOperState = _TmnxNatMapTGrpOperState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 1, 1, 7, 1, 6),
    _TmnxNatMapTGrpOperState_Type()
)
tmnxNatMapTGrpOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatMapTGrpOperState.setStatus("current")


class _TmnxNatMapTGrpFragPerPckt_Type(Unsigned32):
    """Custom type tmnxNatMapTGrpFragPerPckt based on Unsigned32"""
    defaultValue = 5

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 20),
    )


_TmnxNatMapTGrpFragPerPckt_Type.__name__ = "Unsigned32"
_TmnxNatMapTGrpFragPerPckt_Object = MibTableColumn
tmnxNatMapTGrpFragPerPckt = _TmnxNatMapTGrpFragPerPckt_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 1, 1, 7, 1, 7),
    _TmnxNatMapTGrpFragPerPckt_Type()
)
tmnxNatMapTGrpFragPerPckt.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxNatMapTGrpFragPerPckt.setStatus("current")
_TmnxNatIsaMdaObjs_ObjectIdentity = ObjectIdentity
tmnxNatIsaMdaObjs = _TmnxNatIsaMdaObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 1, 2)
)
_TmnxNatIsaMdaTable_Object = MibTable
tmnxNatIsaMdaTable = _TmnxNatIsaMdaTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 1, 2, 1)
)
if mibBuilder.loadTexts:
    tmnxNatIsaMdaTable.setStatus("current")
_TmnxNatIsaMdaEntry_Object = MibTableRow
tmnxNatIsaMdaEntry = _TmnxNatIsaMdaEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 1, 2, 1, 1)
)
tmnxNatIsaMdaEntry.setIndexNames(
    (0, "TIMETRA-NAT-MIB", "tmnxNatIsaGrpId"),
    (0, "TIMETRA-CHASSIS-MIB", "tmnxChassisIndex"),
    (0, "TIMETRA-CHASSIS-MIB", "tmnxCardSlotNum"),
    (0, "TIMETRA-CHASSIS-MIB", "tmnxMDASlotNum"),
)
if mibBuilder.loadTexts:
    tmnxNatIsaMdaEntry.setStatus("current")
_TmnxNatIsaMdaRowStatus_Type = RowStatus
_TmnxNatIsaMdaRowStatus_Object = MibTableColumn
tmnxNatIsaMdaRowStatus = _TmnxNatIsaMdaRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 1, 2, 1, 1, 1),
    _TmnxNatIsaMdaRowStatus_Type()
)
tmnxNatIsaMdaRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxNatIsaMdaRowStatus.setStatus("current")
_TmnxNatIsaMdaLastMgmtChange_Type = TimeStamp
_TmnxNatIsaMdaLastMgmtChange_Object = MibTableColumn
tmnxNatIsaMdaLastMgmtChange = _TmnxNatIsaMdaLastMgmtChange_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 1, 2, 1, 1, 2),
    _TmnxNatIsaMdaLastMgmtChange_Type()
)
tmnxNatIsaMdaLastMgmtChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatIsaMdaLastMgmtChange.setStatus("current")
_TmnxNatIsaMdaStatObjs_ObjectIdentity = ObjectIdentity
tmnxNatIsaMdaStatObjs = _TmnxNatIsaMdaStatObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 1, 3)
)
_TmnxNatIsaMdaStatTable_Object = MibTable
tmnxNatIsaMdaStatTable = _TmnxNatIsaMdaStatTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 1, 3, 1)
)
if mibBuilder.loadTexts:
    tmnxNatIsaMdaStatTable.setStatus("current")
_TmnxNatIsaMdaStatEntry_Object = MibTableRow
tmnxNatIsaMdaStatEntry = _TmnxNatIsaMdaStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 1, 3, 1, 1)
)
if mibBuilder.loadTexts:
    tmnxNatIsaMdaStatEntry.setStatus("current")
_TmnxNatIsaMdaStatOperState_Type = TmnxNatIsaMdaOperState
_TmnxNatIsaMdaStatOperState_Object = MibTableColumn
tmnxNatIsaMdaStatOperState = _TmnxNatIsaMdaStatOperState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 1, 3, 1, 1, 1),
    _TmnxNatIsaMdaStatOperState_Type()
)
tmnxNatIsaMdaStatOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatIsaMdaStatOperState.setStatus("current")


class _TmnxNatIsaMdaStatResrcAllocated_Type(Unsigned32):
    """Custom type tmnxNatIsaMdaStatResrcAllocated based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_TmnxNatIsaMdaStatResrcAllocated_Type.__name__ = "Unsigned32"
_TmnxNatIsaMdaStatResrcAllocated_Object = MibTableColumn
tmnxNatIsaMdaStatResrcAllocated = _TmnxNatIsaMdaStatResrcAllocated_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 1, 3, 1, 1, 2),
    _TmnxNatIsaMdaStatResrcAllocated_Type()
)
tmnxNatIsaMdaStatResrcAllocated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatIsaMdaStatResrcAllocated.setStatus("current")
if mibBuilder.loadTexts:
    tmnxNatIsaMdaStatResrcAllocated.setUnits("percent")
_TmnxNatIsaMdaStatBypassL2AwHost_Type = Unsigned32
_TmnxNatIsaMdaStatBypassL2AwHost_Object = MibTableColumn
tmnxNatIsaMdaStatBypassL2AwHost = _TmnxNatIsaMdaStatBypassL2AwHost_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 1, 3, 1, 1, 3),
    _TmnxNatIsaMdaStatBypassL2AwHost_Type()
)
tmnxNatIsaMdaStatBypassL2AwHost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatIsaMdaStatBypassL2AwHost.setStatus("current")
_TmnxNatIsaMemberTable_Object = MibTable
tmnxNatIsaMemberTable = _TmnxNatIsaMemberTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 1, 3, 2)
)
if mibBuilder.loadTexts:
    tmnxNatIsaMemberTable.setStatus("current")
_TmnxNatIsaMemberEntry_Object = MibTableRow
tmnxNatIsaMemberEntry = _TmnxNatIsaMemberEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 1, 3, 2, 1)
)
tmnxNatIsaMemberEntry.setIndexNames(
    (0, "TIMETRA-NAT-MIB", "tmnxNatIsaGrpId"),
    (0, "TIMETRA-NAT-MIB", "tmnxNatIsaMemberId"),
)
if mibBuilder.loadTexts:
    tmnxNatIsaMemberEntry.setStatus("current")
_TmnxNatIsaMemberId_Type = Unsigned32
_TmnxNatIsaMemberId_Object = MibTableColumn
tmnxNatIsaMemberId = _TmnxNatIsaMemberId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 1, 3, 2, 1, 1),
    _TmnxNatIsaMemberId_Type()
)
tmnxNatIsaMemberId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxNatIsaMemberId.setStatus("current")


class _TmnxNatIsaMemberMdaState_Type(Integer32):
    """Custom type tmnxNatIsaMemberMdaState based on Integer32"""
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
              10)
        )
    )
    namedValues = NamedValues(
        *(("inactive", 1),
          ("active", 2),
          ("needsReset", 3),
          ("resetting", 4),
          ("needsReconcile", 5),
          ("reconciling", 6),
          ("needsAudit", 7),
          ("auditing", 8),
          ("failedBypass", 9),
          ("activeBypass", 10))
    )


_TmnxNatIsaMemberMdaState_Type.__name__ = "Integer32"
_TmnxNatIsaMemberMdaState_Object = MibTableColumn
tmnxNatIsaMemberMdaState = _TmnxNatIsaMemberMdaState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 1, 3, 2, 1, 2),
    _TmnxNatIsaMemberMdaState_Type()
)
tmnxNatIsaMemberMdaState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatIsaMemberMdaState.setStatus("current")
_TmnxNatIsaMemberMdaChassisIndex_Type = TmnxChassisIndexOrZero
_TmnxNatIsaMemberMdaChassisIndex_Object = MibTableColumn
tmnxNatIsaMemberMdaChassisIndex = _TmnxNatIsaMemberMdaChassisIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 1, 3, 2, 1, 3),
    _TmnxNatIsaMemberMdaChassisIndex_Type()
)
tmnxNatIsaMemberMdaChassisIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatIsaMemberMdaChassisIndex.setStatus("current")
_TmnxNatIsaMemberMdaCardSlotNum_Type = TmnxSlotNumOrZero
_TmnxNatIsaMemberMdaCardSlotNum_Object = MibTableColumn
tmnxNatIsaMemberMdaCardSlotNum = _TmnxNatIsaMemberMdaCardSlotNum_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 1, 3, 2, 1, 4),
    _TmnxNatIsaMemberMdaCardSlotNum_Type()
)
tmnxNatIsaMemberMdaCardSlotNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatIsaMemberMdaCardSlotNum.setStatus("current")
_TmnxNatIsaMemberMdaSlotNum_Type = Unsigned32
_TmnxNatIsaMemberMdaSlotNum_Object = MibTableColumn
tmnxNatIsaMemberMdaSlotNum = _TmnxNatIsaMemberMdaSlotNum_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 1, 3, 2, 1, 5),
    _TmnxNatIsaMemberMdaSlotNum_Type()
)
tmnxNatIsaMemberMdaSlotNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatIsaMemberMdaSlotNum.setStatus("current")
_TmnxNatIsaMemberIpAddrReserved_Type = Gauge32
_TmnxNatIsaMemberIpAddrReserved_Object = MibTableColumn
tmnxNatIsaMemberIpAddrReserved = _TmnxNatIsaMemberIpAddrReserved_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 1, 3, 2, 1, 6),
    _TmnxNatIsaMemberIpAddrReserved_Type()
)
tmnxNatIsaMemberIpAddrReserved.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatIsaMemberIpAddrReserved.setStatus("current")
_TmnxNatIsaMemberBlocksReserved_Type = Gauge32
_TmnxNatIsaMemberBlocksReserved_Object = MibTableColumn
tmnxNatIsaMemberBlocksReserved = _TmnxNatIsaMemberBlocksReserved_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 1, 3, 2, 1, 7),
    _TmnxNatIsaMemberBlocksReserved_Type()
)
tmnxNatIsaMemberBlocksReserved.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatIsaMemberBlocksReserved.setStatus("current")
_TmnxNatIsaMemberSessionUsage_Type = TmnxNatUsageLevel
_TmnxNatIsaMemberSessionUsage_Object = MibTableColumn
tmnxNatIsaMemberSessionUsage = _TmnxNatIsaMemberSessionUsage_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 1, 3, 2, 1, 8),
    _TmnxNatIsaMemberSessionUsage_Type()
)
tmnxNatIsaMemberSessionUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatIsaMemberSessionUsage.setStatus("current")
_TmnxNatIsaMemberSessionUsageHi_Type = TruthValue
_TmnxNatIsaMemberSessionUsageHi_Object = MibTableColumn
tmnxNatIsaMemberSessionUsageHi = _TmnxNatIsaMemberSessionUsageHi_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 1, 3, 2, 1, 9),
    _TmnxNatIsaMemberSessionUsageHi_Type()
)
tmnxNatIsaMemberSessionUsageHi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatIsaMemberSessionUsageHi.setStatus("current")
_TmnxNatIsaMemberSessionsPrio_Type = Gauge32
_TmnxNatIsaMemberSessionsPrio_Object = MibTableColumn
tmnxNatIsaMemberSessionsPrio = _TmnxNatIsaMemberSessionsPrio_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 1, 3, 2, 1, 10),
    _TmnxNatIsaMemberSessionsPrio_Type()
)
tmnxNatIsaMemberSessionsPrio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatIsaMemberSessionsPrio.setStatus("current")
_TmnxNatIsaMemberEsaNum_Type = TmnxEsaNum
_TmnxNatIsaMemberEsaNum_Object = MibTableColumn
tmnxNatIsaMemberEsaNum = _TmnxNatIsaMemberEsaNum_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 1, 3, 2, 1, 11),
    _TmnxNatIsaMemberEsaNum_Type()
)
tmnxNatIsaMemberEsaNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatIsaMemberEsaNum.setStatus("current")
_TmnxNatIsaMemberEsaVappNum_Type = TmnxEsaVappNum
_TmnxNatIsaMemberEsaVappNum_Object = MibTableColumn
tmnxNatIsaMemberEsaVappNum = _TmnxNatIsaMemberEsaVappNum_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 1, 3, 2, 1, 12),
    _TmnxNatIsaMemberEsaVappNum_Type()
)
tmnxNatIsaMemberEsaVappNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatIsaMemberEsaVappNum.setStatus("current")
_TmnxNatIsaMemberStatsTable_Object = MibTable
tmnxNatIsaMemberStatsTable = _TmnxNatIsaMemberStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 1, 3, 3)
)
if mibBuilder.loadTexts:
    tmnxNatIsaMemberStatsTable.setStatus("current")
_TmnxNatIsaMemberStatsEntry_Object = MibTableRow
tmnxNatIsaMemberStatsEntry = _TmnxNatIsaMemberStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 1, 3, 3, 1)
)
tmnxNatIsaMemberStatsEntry.setIndexNames(
    (0, "TIMETRA-NAT-MIB", "tmnxNatIsaGrpId"),
    (0, "TIMETRA-NAT-MIB", "tmnxNatIsaMemberId"),
    (0, "TIMETRA-NAT-MIB", "tmnxNatIsaMemberStatsType"),
)
if mibBuilder.loadTexts:
    tmnxNatIsaMemberStatsEntry.setStatus("current")


class _TmnxNatIsaMemberStatsType_Type(Unsigned32):
    """Custom type tmnxNatIsaMemberStatsType based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 149),
    )


_TmnxNatIsaMemberStatsType_Type.__name__ = "Unsigned32"
_TmnxNatIsaMemberStatsType_Object = MibTableColumn
tmnxNatIsaMemberStatsType = _TmnxNatIsaMemberStatsType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 1, 3, 3, 1, 1),
    _TmnxNatIsaMemberStatsType_Type()
)
tmnxNatIsaMemberStatsType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxNatIsaMemberStatsType.setStatus("current")


class _TmnxNatIsaMemberStatsName_Type(DisplayString):
    """Custom type tmnxNatIsaMemberStatsName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_TmnxNatIsaMemberStatsName_Type.__name__ = "DisplayString"
_TmnxNatIsaMemberStatsName_Object = MibTableColumn
tmnxNatIsaMemberStatsName = _TmnxNatIsaMemberStatsName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 1, 3, 3, 1, 2),
    _TmnxNatIsaMemberStatsName_Type()
)
tmnxNatIsaMemberStatsName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatIsaMemberStatsName.setStatus("current")
_TmnxNatIsaMemberStatsVal_Type = Counter32
_TmnxNatIsaMemberStatsVal_Object = MibTableColumn
tmnxNatIsaMemberStatsVal = _TmnxNatIsaMemberStatsVal_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 1, 3, 3, 1, 3),
    _TmnxNatIsaMemberStatsVal_Type()
)
tmnxNatIsaMemberStatsVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatIsaMemberStatsVal.setStatus("current")
_TmnxNatIsaMemberStatsValHw_Type = Counter32
_TmnxNatIsaMemberStatsValHw_Object = MibTableColumn
tmnxNatIsaMemberStatsValHw = _TmnxNatIsaMemberStatsValHw_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 1, 3, 3, 1, 4),
    _TmnxNatIsaMemberStatsValHw_Type()
)
tmnxNatIsaMemberStatsValHw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatIsaMemberStatsValHw.setStatus("current")
_TmnxNatIsaMemberStatsValue_Type = Counter64
_TmnxNatIsaMemberStatsValue_Object = MibTableColumn
tmnxNatIsaMemberStatsValue = _TmnxNatIsaMemberStatsValue_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 1, 3, 3, 1, 5),
    _TmnxNatIsaMemberStatsValue_Type()
)
tmnxNatIsaMemberStatsValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatIsaMemberStatsValue.setStatus("current")
_TmnxNatIsaResrcStatsTable_Object = MibTable
tmnxNatIsaResrcStatsTable = _TmnxNatIsaResrcStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 1, 3, 4)
)
if mibBuilder.loadTexts:
    tmnxNatIsaResrcStatsTable.setStatus("current")
_TmnxNatIsaResrcStatsEntry_Object = MibTableRow
tmnxNatIsaResrcStatsEntry = _TmnxNatIsaResrcStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 1, 3, 4, 1)
)
tmnxNatIsaResrcStatsEntry.setIndexNames(
    (0, "TIMETRA-CHASSIS-MIB", "tmnxChassisIndex"),
    (0, "TIMETRA-CHASSIS-MIB", "tmnxCardSlotNum"),
    (0, "TIMETRA-CHASSIS-MIB", "tmnxMDASlotNum"),
    (0, "TIMETRA-NAT-MIB", "tmnxNatIsaResrcStatsId"),
)
if mibBuilder.loadTexts:
    tmnxNatIsaResrcStatsEntry.setStatus("current")


class _TmnxNatIsaResrcStatsId_Type(Unsigned32):
    """Custom type tmnxNatIsaResrcStatsId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 49),
    )


_TmnxNatIsaResrcStatsId_Type.__name__ = "Unsigned32"
_TmnxNatIsaResrcStatsId_Object = MibTableColumn
tmnxNatIsaResrcStatsId = _TmnxNatIsaResrcStatsId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 1, 3, 4, 1, 1),
    _TmnxNatIsaResrcStatsId_Type()
)
tmnxNatIsaResrcStatsId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxNatIsaResrcStatsId.setStatus("current")


class _TmnxNatIsaResrcStatsName_Type(DisplayString):
    """Custom type tmnxNatIsaResrcStatsName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_TmnxNatIsaResrcStatsName_Type.__name__ = "DisplayString"
_TmnxNatIsaResrcStatsName_Object = MibTableColumn
tmnxNatIsaResrcStatsName = _TmnxNatIsaResrcStatsName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 1, 3, 4, 1, 2),
    _TmnxNatIsaResrcStatsName_Type()
)
tmnxNatIsaResrcStatsName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatIsaResrcStatsName.setStatus("current")
_TmnxNatIsaResrcStatsValMax_Type = CounterBasedGauge64
_TmnxNatIsaResrcStatsValMax_Object = MibTableColumn
tmnxNatIsaResrcStatsValMax = _TmnxNatIsaResrcStatsValMax_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 1, 3, 4, 1, 3),
    _TmnxNatIsaResrcStatsValMax_Type()
)
tmnxNatIsaResrcStatsValMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatIsaResrcStatsValMax.setStatus("current")
_TmnxNatIsaResrcStatsValMaxLw_Type = Gauge32
_TmnxNatIsaResrcStatsValMaxLw_Object = MibTableColumn
tmnxNatIsaResrcStatsValMaxLw = _TmnxNatIsaResrcStatsValMaxLw_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 1, 3, 4, 1, 4),
    _TmnxNatIsaResrcStatsValMaxLw_Type()
)
tmnxNatIsaResrcStatsValMaxLw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatIsaResrcStatsValMaxLw.setStatus("current")
_TmnxNatIsaResrcStatsValMaxHw_Type = Gauge32
_TmnxNatIsaResrcStatsValMaxHw_Object = MibTableColumn
tmnxNatIsaResrcStatsValMaxHw = _TmnxNatIsaResrcStatsValMaxHw_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 1, 3, 4, 1, 5),
    _TmnxNatIsaResrcStatsValMaxHw_Type()
)
tmnxNatIsaResrcStatsValMaxHw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatIsaResrcStatsValMaxHw.setStatus("current")
_TmnxNatIsaResrcStatsVal_Type = CounterBasedGauge64
_TmnxNatIsaResrcStatsVal_Object = MibTableColumn
tmnxNatIsaResrcStatsVal = _TmnxNatIsaResrcStatsVal_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 1, 3, 4, 1, 6),
    _TmnxNatIsaResrcStatsVal_Type()
)
tmnxNatIsaResrcStatsVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatIsaResrcStatsVal.setStatus("current")
_TmnxNatIsaResrcStatsValLw_Type = Gauge32
_TmnxNatIsaResrcStatsValLw_Object = MibTableColumn
tmnxNatIsaResrcStatsValLw = _TmnxNatIsaResrcStatsValLw_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 1, 3, 4, 1, 7),
    _TmnxNatIsaResrcStatsValLw_Type()
)
tmnxNatIsaResrcStatsValLw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatIsaResrcStatsValLw.setStatus("current")
_TmnxNatIsaResrcStatsValHw_Type = Gauge32
_TmnxNatIsaResrcStatsValHw_Object = MibTableColumn
tmnxNatIsaResrcStatsValHw = _TmnxNatIsaResrcStatsValHw_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 1, 3, 4, 1, 8),
    _TmnxNatIsaResrcStatsValHw_Type()
)
tmnxNatIsaResrcStatsValHw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatIsaResrcStatsValHw.setStatus("current")
_TmnxNatIsaResrcStatsLimited_Type = TruthValue
_TmnxNatIsaResrcStatsLimited_Object = MibTableColumn
tmnxNatIsaResrcStatsLimited = _TmnxNatIsaResrcStatsLimited_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 1, 3, 4, 1, 9),
    _TmnxNatIsaResrcStatsLimited_Type()
)
tmnxNatIsaResrcStatsLimited.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatIsaResrcStatsLimited.setStatus("current")
_TmnxNatIsaResrcStatsValPeak_Type = CounterBasedGauge64
_TmnxNatIsaResrcStatsValPeak_Object = MibTableColumn
tmnxNatIsaResrcStatsValPeak = _TmnxNatIsaResrcStatsValPeak_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 1, 3, 4, 1, 10),
    _TmnxNatIsaResrcStatsValPeak_Type()
)
tmnxNatIsaResrcStatsValPeak.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatIsaResrcStatsValPeak.setStatus("current")
_TmnxNatIsaResrcStatsValPeakLw_Type = Gauge32
_TmnxNatIsaResrcStatsValPeakLw_Object = MibTableColumn
tmnxNatIsaResrcStatsValPeakLw = _TmnxNatIsaResrcStatsValPeakLw_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 1, 3, 4, 1, 11),
    _TmnxNatIsaResrcStatsValPeakLw_Type()
)
tmnxNatIsaResrcStatsValPeakLw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatIsaResrcStatsValPeakLw.setStatus("current")
_TmnxNatIsaResrcStatsValPeakHw_Type = Gauge32
_TmnxNatIsaResrcStatsValPeakHw_Object = MibTableColumn
tmnxNatIsaResrcStatsValPeakHw = _TmnxNatIsaResrcStatsValPeakHw_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 1, 3, 4, 1, 12),
    _TmnxNatIsaResrcStatsValPeakHw_Type()
)
tmnxNatIsaResrcStatsValPeakHw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatIsaResrcStatsValPeakHw.setStatus("current")


class _TmnxNatIsaResrcStatsPeakTime_Type(DateAndTime):
    """Custom type tmnxNatIsaResrcStatsPeakTime based on DateAndTime"""
    subtypeSpec = DateAndTime.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(11, 11),
    )
    fixed_length = 11


_TmnxNatIsaResrcStatsPeakTime_Type.__name__ = "DateAndTime"
_TmnxNatIsaResrcStatsPeakTime_Object = MibTableColumn
tmnxNatIsaResrcStatsPeakTime = _TmnxNatIsaResrcStatsPeakTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 1, 3, 4, 1, 13),
    _TmnxNatIsaResrcStatsPeakTime_Type()
)
tmnxNatIsaResrcStatsPeakTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatIsaResrcStatsPeakTime.setStatus("current")
_TmnxNatReassemblyStatsTable_Object = MibTable
tmnxNatReassemblyStatsTable = _TmnxNatReassemblyStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 1, 3, 5)
)
if mibBuilder.loadTexts:
    tmnxNatReassemblyStatsTable.setStatus("current")
_TmnxNatReassemblyStatsEntry_Object = MibTableRow
tmnxNatReassemblyStatsEntry = _TmnxNatReassemblyStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 1, 3, 5, 1)
)
tmnxNatReassemblyStatsEntry.setIndexNames(
    (0, "TIMETRA-NAT-MIB", "tmnxNatIsaGrpId"),
    (0, "TIMETRA-NAT-MIB", "tmnxNatIsaMemberId"),
    (0, "TIMETRA-NAT-MIB", "tmnxNatReassemblyStatsType"),
)
if mibBuilder.loadTexts:
    tmnxNatReassemblyStatsEntry.setStatus("current")


class _TmnxNatReassemblyStatsType_Type(Unsigned32):
    """Custom type tmnxNatReassemblyStatsType based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 35),
    )


_TmnxNatReassemblyStatsType_Type.__name__ = "Unsigned32"
_TmnxNatReassemblyStatsType_Object = MibTableColumn
tmnxNatReassemblyStatsType = _TmnxNatReassemblyStatsType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 1, 3, 5, 1, 1),
    _TmnxNatReassemblyStatsType_Type()
)
tmnxNatReassemblyStatsType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxNatReassemblyStatsType.setStatus("current")


class _TmnxNatReassemblyStatsName_Type(DisplayString):
    """Custom type tmnxNatReassemblyStatsName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_TmnxNatReassemblyStatsName_Type.__name__ = "DisplayString"
_TmnxNatReassemblyStatsName_Object = MibTableColumn
tmnxNatReassemblyStatsName = _TmnxNatReassemblyStatsName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 1, 3, 5, 1, 2),
    _TmnxNatReassemblyStatsName_Type()
)
tmnxNatReassemblyStatsName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatReassemblyStatsName.setStatus("current")
_TmnxNatReassemblyStatsVal_Type = Counter64
_TmnxNatReassemblyStatsVal_Object = MibTableColumn
tmnxNatReassemblyStatsVal = _TmnxNatReassemblyStatsVal_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 1, 3, 5, 1, 3),
    _TmnxNatReassemblyStatsVal_Type()
)
tmnxNatReassemblyStatsVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatReassemblyStatsVal.setStatus("current")
_TmnxNatReassemblyStatsValLw_Type = Counter32
_TmnxNatReassemblyStatsValLw_Object = MibTableColumn
tmnxNatReassemblyStatsValLw = _TmnxNatReassemblyStatsValLw_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 1, 3, 5, 1, 4),
    _TmnxNatReassemblyStatsValLw_Type()
)
tmnxNatReassemblyStatsValLw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatReassemblyStatsValLw.setStatus("current")
_TmnxNatReassemblyStatsValHw_Type = Counter32
_TmnxNatReassemblyStatsValHw_Object = MibTableColumn
tmnxNatReassemblyStatsValHw = _TmnxNatReassemblyStatsValHw_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 1, 3, 5, 1, 5),
    _TmnxNatReassemblyStatsValHw_Type()
)
tmnxNatReassemblyStatsValHw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatReassemblyStatsValHw.setStatus("current")
_TmnxNatIsaMemberResrcTable_Object = MibTable
tmnxNatIsaMemberResrcTable = _TmnxNatIsaMemberResrcTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 1, 3, 6)
)
if mibBuilder.loadTexts:
    tmnxNatIsaMemberResrcTable.setStatus("current")
_TmnxNatIsaMemberResrcEntry_Object = MibTableRow
tmnxNatIsaMemberResrcEntry = _TmnxNatIsaMemberResrcEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 1, 3, 6, 1)
)
tmnxNatIsaMemberResrcEntry.setIndexNames(
    (0, "TIMETRA-NAT-MIB", "tmnxNatIsaGrpId"),
    (0, "TIMETRA-NAT-MIB", "tmnxNatIsaMemberId"),
    (0, "TIMETRA-NAT-MIB", "tmnxNatIsaMemberResrcId"),
)
if mibBuilder.loadTexts:
    tmnxNatIsaMemberResrcEntry.setStatus("current")


class _TmnxNatIsaMemberResrcId_Type(Unsigned32):
    """Custom type tmnxNatIsaMemberResrcId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 49),
    )


_TmnxNatIsaMemberResrcId_Type.__name__ = "Unsigned32"
_TmnxNatIsaMemberResrcId_Object = MibTableColumn
tmnxNatIsaMemberResrcId = _TmnxNatIsaMemberResrcId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 1, 3, 6, 1, 1),
    _TmnxNatIsaMemberResrcId_Type()
)
tmnxNatIsaMemberResrcId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxNatIsaMemberResrcId.setStatus("current")


class _TmnxNatIsaMemberResrcName_Type(DisplayString):
    """Custom type tmnxNatIsaMemberResrcName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_TmnxNatIsaMemberResrcName_Type.__name__ = "DisplayString"
_TmnxNatIsaMemberResrcName_Object = MibTableColumn
tmnxNatIsaMemberResrcName = _TmnxNatIsaMemberResrcName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 1, 3, 6, 1, 2),
    _TmnxNatIsaMemberResrcName_Type()
)
tmnxNatIsaMemberResrcName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatIsaMemberResrcName.setStatus("current")
_TmnxNatIsaMemberResrcValMax_Type = CounterBasedGauge64
_TmnxNatIsaMemberResrcValMax_Object = MibTableColumn
tmnxNatIsaMemberResrcValMax = _TmnxNatIsaMemberResrcValMax_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 1, 3, 6, 1, 3),
    _TmnxNatIsaMemberResrcValMax_Type()
)
tmnxNatIsaMemberResrcValMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatIsaMemberResrcValMax.setStatus("current")
_TmnxNatIsaMemberResrcVal_Type = CounterBasedGauge64
_TmnxNatIsaMemberResrcVal_Object = MibTableColumn
tmnxNatIsaMemberResrcVal = _TmnxNatIsaMemberResrcVal_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 1, 3, 6, 1, 4),
    _TmnxNatIsaMemberResrcVal_Type()
)
tmnxNatIsaMemberResrcVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatIsaMemberResrcVal.setStatus("current")
_TmnxNatIsaMemberResrcApplicable_Type = TruthValue
_TmnxNatIsaMemberResrcApplicable_Object = MibTableColumn
tmnxNatIsaMemberResrcApplicable = _TmnxNatIsaMemberResrcApplicable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 1, 3, 6, 1, 5),
    _TmnxNatIsaMemberResrcApplicable_Type()
)
tmnxNatIsaMemberResrcApplicable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatIsaMemberResrcApplicable.setStatus("current")
_TmnxNatIsaMemberResrcValPeak_Type = CounterBasedGauge64
_TmnxNatIsaMemberResrcValPeak_Object = MibTableColumn
tmnxNatIsaMemberResrcValPeak = _TmnxNatIsaMemberResrcValPeak_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 1, 3, 6, 1, 6),
    _TmnxNatIsaMemberResrcValPeak_Type()
)
tmnxNatIsaMemberResrcValPeak.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatIsaMemberResrcValPeak.setStatus("current")


class _TmnxNatIsaMemberResrcPeakTime_Type(DateAndTime):
    """Custom type tmnxNatIsaMemberResrcPeakTime based on DateAndTime"""
    subtypeSpec = DateAndTime.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(11, 11),
    )
    fixed_length = 11


_TmnxNatIsaMemberResrcPeakTime_Type.__name__ = "DateAndTime"
_TmnxNatIsaMemberResrcPeakTime_Object = MibTableColumn
tmnxNatIsaMemberResrcPeakTime = _TmnxNatIsaMemberResrcPeakTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 1, 3, 6, 1, 7),
    _TmnxNatIsaMemberResrcPeakTime_Type()
)
tmnxNatIsaMemberResrcPeakTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatIsaMemberResrcPeakTime.setStatus("current")
_TmnxNatIsaMdaStatsTable_Object = MibTable
tmnxNatIsaMdaStatsTable = _TmnxNatIsaMdaStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 1, 3, 7)
)
if mibBuilder.loadTexts:
    tmnxNatIsaMdaStatsTable.setStatus("current")
_TmnxNatIsaMdaStatsEntry_Object = MibTableRow
tmnxNatIsaMdaStatsEntry = _TmnxNatIsaMdaStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 1, 3, 7, 1)
)
tmnxNatIsaMdaStatsEntry.setIndexNames(
    (0, "TIMETRA-NAT-MIB", "tmnxNatIsaGrpId"),
    (0, "TIMETRA-CHASSIS-MIB", "tmnxChassisIndex"),
    (0, "TIMETRA-CHASSIS-MIB", "tmnxCardSlotNum"),
    (0, "TIMETRA-CHASSIS-MIB", "tmnxMDASlotNum"),
    (0, "TIMETRA-NAT-MIB", "tmnxNatIsaMdaStatsType"),
)
if mibBuilder.loadTexts:
    tmnxNatIsaMdaStatsEntry.setStatus("current")


class _TmnxNatIsaMdaStatsType_Type(Unsigned32):
    """Custom type tmnxNatIsaMdaStatsType based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 149),
    )


_TmnxNatIsaMdaStatsType_Type.__name__ = "Unsigned32"
_TmnxNatIsaMdaStatsType_Object = MibTableColumn
tmnxNatIsaMdaStatsType = _TmnxNatIsaMdaStatsType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 1, 3, 7, 1, 1),
    _TmnxNatIsaMdaStatsType_Type()
)
tmnxNatIsaMdaStatsType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxNatIsaMdaStatsType.setStatus("current")


class _TmnxNatIsaMdaStatsName_Type(DisplayString):
    """Custom type tmnxNatIsaMdaStatsName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_TmnxNatIsaMdaStatsName_Type.__name__ = "DisplayString"
_TmnxNatIsaMdaStatsName_Object = MibTableColumn
tmnxNatIsaMdaStatsName = _TmnxNatIsaMdaStatsName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 1, 3, 7, 1, 2),
    _TmnxNatIsaMdaStatsName_Type()
)
tmnxNatIsaMdaStatsName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatIsaMdaStatsName.setStatus("current")
_TmnxNatIsaMdaStatsValue_Type = Counter64
_TmnxNatIsaMdaStatsValue_Object = MibTableColumn
tmnxNatIsaMdaStatsValue = _TmnxNatIsaMdaStatsValue_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 1, 3, 7, 1, 3),
    _TmnxNatIsaMdaStatsValue_Type()
)
tmnxNatIsaMdaStatsValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatIsaMdaStatsValue.setStatus("current")
_TmnxNatIsaMdaStatsHrTable_Object = MibTable
tmnxNatIsaMdaStatsHrTable = _TmnxNatIsaMdaStatsHrTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 1, 3, 8)
)
if mibBuilder.loadTexts:
    tmnxNatIsaMdaStatsHrTable.setStatus("current")
_TmnxNatIsaMdaStatsHrEntry_Object = MibTableRow
tmnxNatIsaMdaStatsHrEntry = _TmnxNatIsaMdaStatsHrEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 1, 3, 8, 1)
)
tmnxNatIsaMdaStatsHrEntry.setIndexNames(
    (0, "TIMETRA-NAT-MIB", "tmnxNatIsaGrpId"),
    (0, "TIMETRA-CHASSIS-MIB", "tmnxChassisIndex"),
    (0, "TIMETRA-CHASSIS-MIB", "tmnxCardSlotNum"),
    (0, "TIMETRA-CHASSIS-MIB", "tmnxMDASlotNum"),
    (0, "TIMETRA-NAT-MIB", "tmnxNatIsaMdaStatsHrIndex"),
)
if mibBuilder.loadTexts:
    tmnxNatIsaMdaStatsHrEntry.setStatus("current")
_TmnxNatIsaMdaStatsHrIndex_Type = Unsigned32
_TmnxNatIsaMdaStatsHrIndex_Object = MibTableColumn
tmnxNatIsaMdaStatsHrIndex = _TmnxNatIsaMdaStatsHrIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 1, 3, 8, 1, 1),
    _TmnxNatIsaMdaStatsHrIndex_Type()
)
tmnxNatIsaMdaStatsHrIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxNatIsaMdaStatsHrIndex.setStatus("current")


class _TmnxNatIsaMdaStatsHrTime_Type(DateAndTime):
    """Custom type tmnxNatIsaMdaStatsHrTime based on DateAndTime"""
    subtypeSpec = DateAndTime.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(11, 11),
    )
    fixed_length = 11


_TmnxNatIsaMdaStatsHrTime_Type.__name__ = "DateAndTime"
_TmnxNatIsaMdaStatsHrTime_Object = MibTableColumn
tmnxNatIsaMdaStatsHrTime = _TmnxNatIsaMdaStatsHrTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 1, 3, 8, 1, 2),
    _TmnxNatIsaMdaStatsHrTime_Type()
)
tmnxNatIsaMdaStatsHrTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatIsaMdaStatsHrTime.setStatus("current")
_TmnxNatIsaMdaStatsHrWaiting_Type = TmnxPerTenThousand
_TmnxNatIsaMdaStatsHrWaiting_Object = MibTableColumn
tmnxNatIsaMdaStatsHrWaiting = _TmnxNatIsaMdaStatsHrWaiting_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 1, 3, 8, 1, 3),
    _TmnxNatIsaMdaStatsHrWaiting_Type()
)
tmnxNatIsaMdaStatsHrWaiting.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatIsaMdaStatsHrWaiting.setStatus("current")
_TmnxNatIsaMdaStatsHrIdle_Type = TmnxPerTenThousand
_TmnxNatIsaMdaStatsHrIdle_Object = MibTableColumn
tmnxNatIsaMdaStatsHrIdle = _TmnxNatIsaMdaStatsHrIdle_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 1, 3, 8, 1, 4),
    _TmnxNatIsaMdaStatsHrIdle_Type()
)
tmnxNatIsaMdaStatsHrIdle.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatIsaMdaStatsHrIdle.setStatus("current")
_TmnxNatIsaMdaStatsHrWorking_Type = TmnxPerTenThousand
_TmnxNatIsaMdaStatsHrWorking_Object = MibTableColumn
tmnxNatIsaMdaStatsHrWorking = _TmnxNatIsaMdaStatsHrWorking_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 1, 3, 8, 1, 5),
    _TmnxNatIsaMdaStatsHrWorking_Type()
)
tmnxNatIsaMdaStatsHrWorking.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatIsaMdaStatsHrWorking.setStatus("current")
_TmnxNatIsaMdaStatsHrJobs_Type = Unsigned32
_TmnxNatIsaMdaStatsHrJobs_Object = MibTableColumn
tmnxNatIsaMdaStatsHrJobs = _TmnxNatIsaMdaStatsHrJobs_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 1, 3, 8, 1, 6),
    _TmnxNatIsaMdaStatsHrJobs_Type()
)
tmnxNatIsaMdaStatsHrJobs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatIsaMdaStatsHrJobs.setStatus("current")
_TmnxNatIsaMdaStatsHrThroughput_Type = Counter64
_TmnxNatIsaMdaStatsHrThroughput_Object = MibTableColumn
tmnxNatIsaMdaStatsHrThroughput = _TmnxNatIsaMdaStatsHrThroughput_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 1, 3, 8, 1, 7),
    _TmnxNatIsaMdaStatsHrThroughput_Type()
)
tmnxNatIsaMdaStatsHrThroughput.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatIsaMdaStatsHrThroughput.setStatus("current")
_TmnxNatIsaMdaStatsDayTable_Object = MibTable
tmnxNatIsaMdaStatsDayTable = _TmnxNatIsaMdaStatsDayTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 1, 3, 9)
)
if mibBuilder.loadTexts:
    tmnxNatIsaMdaStatsDayTable.setStatus("current")
_TmnxNatIsaMdaStatsDayEntry_Object = MibTableRow
tmnxNatIsaMdaStatsDayEntry = _TmnxNatIsaMdaStatsDayEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 1, 3, 9, 1)
)
tmnxNatIsaMdaStatsDayEntry.setIndexNames(
    (0, "TIMETRA-NAT-MIB", "tmnxNatIsaGrpId"),
    (0, "TIMETRA-CHASSIS-MIB", "tmnxChassisIndex"),
    (0, "TIMETRA-CHASSIS-MIB", "tmnxCardSlotNum"),
    (0, "TIMETRA-CHASSIS-MIB", "tmnxMDASlotNum"),
    (0, "TIMETRA-NAT-MIB", "tmnxNatIsaMdaStatsDayIndex"),
)
if mibBuilder.loadTexts:
    tmnxNatIsaMdaStatsDayEntry.setStatus("current")
_TmnxNatIsaMdaStatsDayIndex_Type = Unsigned32
_TmnxNatIsaMdaStatsDayIndex_Object = MibTableColumn
tmnxNatIsaMdaStatsDayIndex = _TmnxNatIsaMdaStatsDayIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 1, 3, 9, 1, 1),
    _TmnxNatIsaMdaStatsDayIndex_Type()
)
tmnxNatIsaMdaStatsDayIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxNatIsaMdaStatsDayIndex.setStatus("current")


class _TmnxNatIsaMdaStatsDayTime_Type(DateAndTime):
    """Custom type tmnxNatIsaMdaStatsDayTime based on DateAndTime"""
    subtypeSpec = DateAndTime.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(11, 11),
    )
    fixed_length = 11


_TmnxNatIsaMdaStatsDayTime_Type.__name__ = "DateAndTime"
_TmnxNatIsaMdaStatsDayTime_Object = MibTableColumn
tmnxNatIsaMdaStatsDayTime = _TmnxNatIsaMdaStatsDayTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 1, 3, 9, 1, 2),
    _TmnxNatIsaMdaStatsDayTime_Type()
)
tmnxNatIsaMdaStatsDayTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatIsaMdaStatsDayTime.setStatus("current")
_TmnxNatIsaMdaStatsDayWaiting_Type = TmnxPerTenThousand
_TmnxNatIsaMdaStatsDayWaiting_Object = MibTableColumn
tmnxNatIsaMdaStatsDayWaiting = _TmnxNatIsaMdaStatsDayWaiting_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 1, 3, 9, 1, 3),
    _TmnxNatIsaMdaStatsDayWaiting_Type()
)
tmnxNatIsaMdaStatsDayWaiting.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatIsaMdaStatsDayWaiting.setStatus("current")
_TmnxNatIsaMdaStatsDayIdle_Type = TmnxPerTenThousand
_TmnxNatIsaMdaStatsDayIdle_Object = MibTableColumn
tmnxNatIsaMdaStatsDayIdle = _TmnxNatIsaMdaStatsDayIdle_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 1, 3, 9, 1, 4),
    _TmnxNatIsaMdaStatsDayIdle_Type()
)
tmnxNatIsaMdaStatsDayIdle.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatIsaMdaStatsDayIdle.setStatus("current")
_TmnxNatIsaMdaStatsDayWorking_Type = TmnxPerTenThousand
_TmnxNatIsaMdaStatsDayWorking_Object = MibTableColumn
tmnxNatIsaMdaStatsDayWorking = _TmnxNatIsaMdaStatsDayWorking_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 1, 3, 9, 1, 5),
    _TmnxNatIsaMdaStatsDayWorking_Type()
)
tmnxNatIsaMdaStatsDayWorking.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatIsaMdaStatsDayWorking.setStatus("current")
_TmnxNatIsaMdaStatsDayJobs_Type = Unsigned32
_TmnxNatIsaMdaStatsDayJobs_Object = MibTableColumn
tmnxNatIsaMdaStatsDayJobs = _TmnxNatIsaMdaStatsDayJobs_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 1, 3, 9, 1, 6),
    _TmnxNatIsaMdaStatsDayJobs_Type()
)
tmnxNatIsaMdaStatsDayJobs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatIsaMdaStatsDayJobs.setStatus("current")
_TmnxNatIsaMdaStatsDayThroughput_Type = Counter64
_TmnxNatIsaMdaStatsDayThroughput_Object = MibTableColumn
tmnxNatIsaMdaStatsDayThroughput = _TmnxNatIsaMdaStatsDayThroughput_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 1, 3, 9, 1, 7),
    _TmnxNatIsaMdaStatsDayThroughput_Type()
)
tmnxNatIsaMdaStatsDayThroughput.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatIsaMdaStatsDayThroughput.setStatus("current")
_TmnxNatIsaMdaStatsMonthTable_Object = MibTable
tmnxNatIsaMdaStatsMonthTable = _TmnxNatIsaMdaStatsMonthTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 1, 3, 10)
)
if mibBuilder.loadTexts:
    tmnxNatIsaMdaStatsMonthTable.setStatus("current")
_TmnxNatIsaMdaStatsMonthEntry_Object = MibTableRow
tmnxNatIsaMdaStatsMonthEntry = _TmnxNatIsaMdaStatsMonthEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 1, 3, 10, 1)
)
tmnxNatIsaMdaStatsMonthEntry.setIndexNames(
    (0, "TIMETRA-NAT-MIB", "tmnxNatIsaGrpId"),
    (0, "TIMETRA-CHASSIS-MIB", "tmnxChassisIndex"),
    (0, "TIMETRA-CHASSIS-MIB", "tmnxCardSlotNum"),
    (0, "TIMETRA-CHASSIS-MIB", "tmnxMDASlotNum"),
    (0, "TIMETRA-NAT-MIB", "tmnxNatIsaMdaStatsMonthIndex"),
)
if mibBuilder.loadTexts:
    tmnxNatIsaMdaStatsMonthEntry.setStatus("current")
_TmnxNatIsaMdaStatsMonthIndex_Type = Unsigned32
_TmnxNatIsaMdaStatsMonthIndex_Object = MibTableColumn
tmnxNatIsaMdaStatsMonthIndex = _TmnxNatIsaMdaStatsMonthIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 1, 3, 10, 1, 1),
    _TmnxNatIsaMdaStatsMonthIndex_Type()
)
tmnxNatIsaMdaStatsMonthIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxNatIsaMdaStatsMonthIndex.setStatus("current")


class _TmnxNatIsaMdaStatsMonthTime_Type(DateAndTime):
    """Custom type tmnxNatIsaMdaStatsMonthTime based on DateAndTime"""
    subtypeSpec = DateAndTime.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(11, 11),
    )
    fixed_length = 11


_TmnxNatIsaMdaStatsMonthTime_Type.__name__ = "DateAndTime"
_TmnxNatIsaMdaStatsMonthTime_Object = MibTableColumn
tmnxNatIsaMdaStatsMonthTime = _TmnxNatIsaMdaStatsMonthTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 1, 3, 10, 1, 2),
    _TmnxNatIsaMdaStatsMonthTime_Type()
)
tmnxNatIsaMdaStatsMonthTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatIsaMdaStatsMonthTime.setStatus("current")
_TmnxNatIsaMdaStatsMonthWaiting_Type = TmnxPerTenThousand
_TmnxNatIsaMdaStatsMonthWaiting_Object = MibTableColumn
tmnxNatIsaMdaStatsMonthWaiting = _TmnxNatIsaMdaStatsMonthWaiting_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 1, 3, 10, 1, 3),
    _TmnxNatIsaMdaStatsMonthWaiting_Type()
)
tmnxNatIsaMdaStatsMonthWaiting.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatIsaMdaStatsMonthWaiting.setStatus("current")
_TmnxNatIsaMdaStatsMonthIdle_Type = TmnxPerTenThousand
_TmnxNatIsaMdaStatsMonthIdle_Object = MibTableColumn
tmnxNatIsaMdaStatsMonthIdle = _TmnxNatIsaMdaStatsMonthIdle_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 1, 3, 10, 1, 4),
    _TmnxNatIsaMdaStatsMonthIdle_Type()
)
tmnxNatIsaMdaStatsMonthIdle.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatIsaMdaStatsMonthIdle.setStatus("current")
_TmnxNatIsaMdaStatsMonthWorking_Type = TmnxPerTenThousand
_TmnxNatIsaMdaStatsMonthWorking_Object = MibTableColumn
tmnxNatIsaMdaStatsMonthWorking = _TmnxNatIsaMdaStatsMonthWorking_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 1, 3, 10, 1, 5),
    _TmnxNatIsaMdaStatsMonthWorking_Type()
)
tmnxNatIsaMdaStatsMonthWorking.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatIsaMdaStatsMonthWorking.setStatus("current")
_TmnxNatIsaMdaStatsMonthJobs_Type = Unsigned32
_TmnxNatIsaMdaStatsMonthJobs_Object = MibTableColumn
tmnxNatIsaMdaStatsMonthJobs = _TmnxNatIsaMdaStatsMonthJobs_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 1, 3, 10, 1, 6),
    _TmnxNatIsaMdaStatsMonthJobs_Type()
)
tmnxNatIsaMdaStatsMonthJobs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatIsaMdaStatsMonthJobs.setStatus("current")
_TmnxNatIsaMdaStatsMonthThroughp_Type = Counter64
_TmnxNatIsaMdaStatsMonthThroughp_Object = MibTableColumn
tmnxNatIsaMdaStatsMonthThroughp = _TmnxNatIsaMdaStatsMonthThroughp_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 1, 3, 10, 1, 7),
    _TmnxNatIsaMdaStatsMonthThroughp_Type()
)
tmnxNatIsaMdaStatsMonthThroughp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatIsaMdaStatsMonthThroughp.setStatus("current")
_TmnxNatMemSicrStateTable_Object = MibTable
tmnxNatMemSicrStateTable = _TmnxNatMemSicrStateTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 1, 3, 11)
)
if mibBuilder.loadTexts:
    tmnxNatMemSicrStateTable.setStatus("current")
_TmnxNatMemSicrStateEntry_Object = MibTableRow
tmnxNatMemSicrStateEntry = _TmnxNatMemSicrStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 1, 3, 11, 1)
)
tmnxNatMemSicrStateEntry.setIndexNames(
    (0, "TIMETRA-NAT-MIB", "tmnxNatIsaGrpId"),
    (0, "TIMETRA-NAT-MIB", "tmnxNatIsaMemberId"),
)
if mibBuilder.loadTexts:
    tmnxNatMemSicrStateEntry.setStatus("current")


class _TmnxNatMemSicrState_Type(Integer32):
    """Custom type tmnxNatMemSicrState based on Integer32"""
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
        *(("disabled", 0),
          ("waitingSelection", 1),
          ("cleaningUp", 2),
          ("negotiating", 3),
          ("active", 4),
          ("standby", 5))
    )


_TmnxNatMemSicrState_Type.__name__ = "Integer32"
_TmnxNatMemSicrState_Object = MibTableColumn
tmnxNatMemSicrState = _TmnxNatMemSicrState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 1, 3, 11, 1, 1),
    _TmnxNatMemSicrState_Type()
)
tmnxNatMemSicrState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatMemSicrState.setStatus("current")


class _TmnxNatMemSicrPeerState_Type(Integer32):
    """Custom type tmnxNatMemSicrPeerState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("standby", 2))
    )


_TmnxNatMemSicrPeerState_Type.__name__ = "Integer32"
_TmnxNatMemSicrPeerState_Object = MibTableColumn
tmnxNatMemSicrPeerState = _TmnxNatMemSicrPeerState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 1, 3, 11, 1, 2),
    _TmnxNatMemSicrPeerState_Type()
)
tmnxNatMemSicrPeerState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatMemSicrPeerState.setStatus("current")
_TmnxNatMemSicrLocAddrType_Type = InetAddressType
_TmnxNatMemSicrLocAddrType_Object = MibTableColumn
tmnxNatMemSicrLocAddrType = _TmnxNatMemSicrLocAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 1, 3, 11, 1, 3),
    _TmnxNatMemSicrLocAddrType_Type()
)
tmnxNatMemSicrLocAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatMemSicrLocAddrType.setStatus("current")


class _TmnxNatMemSicrLocAddr_Type(InetAddress):
    """Custom type tmnxNatMemSicrLocAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxNatMemSicrLocAddr_Type.__name__ = "InetAddress"
_TmnxNatMemSicrLocAddr_Object = MibTableColumn
tmnxNatMemSicrLocAddr = _TmnxNatMemSicrLocAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 1, 3, 11, 1, 4),
    _TmnxNatMemSicrLocAddr_Type()
)
tmnxNatMemSicrLocAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatMemSicrLocAddr.setStatus("current")
_TmnxNatMemSicrRemAddrType_Type = InetAddressType
_TmnxNatMemSicrRemAddrType_Object = MibTableColumn
tmnxNatMemSicrRemAddrType = _TmnxNatMemSicrRemAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 1, 3, 11, 1, 5),
    _TmnxNatMemSicrRemAddrType_Type()
)
tmnxNatMemSicrRemAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatMemSicrRemAddrType.setStatus("current")


class _TmnxNatMemSicrRemAddr_Type(InetAddress):
    """Custom type tmnxNatMemSicrRemAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxNatMemSicrRemAddr_Type.__name__ = "InetAddress"
_TmnxNatMemSicrRemAddr_Object = MibTableColumn
tmnxNatMemSicrRemAddr = _TmnxNatMemSicrRemAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 1, 3, 11, 1, 6),
    _TmnxNatMemSicrRemAddr_Type()
)
tmnxNatMemSicrRemAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatMemSicrRemAddr.setStatus("current")
_TmnxNatMemSicrStateLastFailed_Type = TimeStamp
_TmnxNatMemSicrStateLastFailed_Object = MibTableColumn
tmnxNatMemSicrStateLastFailed = _TmnxNatMemSicrStateLastFailed_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 1, 3, 11, 1, 7),
    _TmnxNatMemSicrStateLastFailed_Type()
)
tmnxNatMemSicrStateLastFailed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatMemSicrStateLastFailed.setStatus("current")
_TmnxNatMemSicrStateFailReason_Type = DisplayString
_TmnxNatMemSicrStateFailReason_Object = MibTableColumn
tmnxNatMemSicrStateFailReason = _TmnxNatMemSicrStateFailReason_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 1, 3, 11, 1, 8),
    _TmnxNatMemSicrStateFailReason_Type()
)
tmnxNatMemSicrStateFailReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatMemSicrStateFailReason.setStatus("current")
_TmnxNatMemSicrStateUnsupp_Type = CounterBasedGauge64
_TmnxNatMemSicrStateUnsupp_Object = MibTableColumn
tmnxNatMemSicrStateUnsupp = _TmnxNatMemSicrStateUnsupp_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 1, 3, 11, 1, 21),
    _TmnxNatMemSicrStateUnsupp_Type()
)
tmnxNatMemSicrStateUnsupp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatMemSicrStateUnsupp.setStatus("current")
_TmnxNatMemSicrStateTracked_Type = CounterBasedGauge64
_TmnxNatMemSicrStateTracked_Object = MibTableColumn
tmnxNatMemSicrStateTracked = _TmnxNatMemSicrStateTracked_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 1, 3, 11, 1, 22),
    _TmnxNatMemSicrStateTracked_Type()
)
tmnxNatMemSicrStateTracked.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatMemSicrStateTracked.setStatus("current")
_TmnxNatMemSicrStateNotSync_Type = CounterBasedGauge64
_TmnxNatMemSicrStateNotSync_Object = MibTableColumn
tmnxNatMemSicrStateNotSync = _TmnxNatMemSicrStateNotSync_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 1, 3, 11, 1, 23),
    _TmnxNatMemSicrStateNotSync_Type()
)
tmnxNatMemSicrStateNotSync.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatMemSicrStateNotSync.setStatus("current")
_TmnxNatMemSicrStateCreatePending_Type = CounterBasedGauge64
_TmnxNatMemSicrStateCreatePending_Object = MibTableColumn
tmnxNatMemSicrStateCreatePending = _TmnxNatMemSicrStateCreatePending_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 1, 3, 11, 1, 24),
    _TmnxNatMemSicrStateCreatePending_Type()
)
tmnxNatMemSicrStateCreatePending.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatMemSicrStateCreatePending.setStatus("current")
_TmnxNatMemSicrStateCreateSync_Type = CounterBasedGauge64
_TmnxNatMemSicrStateCreateSync_Object = MibTableColumn
tmnxNatMemSicrStateCreateSync = _TmnxNatMemSicrStateCreateSync_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 1, 3, 11, 1, 25),
    _TmnxNatMemSicrStateCreateSync_Type()
)
tmnxNatMemSicrStateCreateSync.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatMemSicrStateCreateSync.setStatus("current")
_TmnxNatMemSicrStateDeleteMarked_Type = CounterBasedGauge64
_TmnxNatMemSicrStateDeleteMarked_Object = MibTableColumn
tmnxNatMemSicrStateDeleteMarked = _TmnxNatMemSicrStateDeleteMarked_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 1, 3, 11, 1, 26),
    _TmnxNatMemSicrStateDeleteMarked_Type()
)
tmnxNatMemSicrStateDeleteMarked.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatMemSicrStateDeleteMarked.setStatus("current")
_TmnxNatMemSicrStateDeletePending_Type = CounterBasedGauge64
_TmnxNatMemSicrStateDeletePending_Object = MibTableColumn
tmnxNatMemSicrStateDeletePending = _TmnxNatMemSicrStateDeletePending_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 1, 3, 11, 1, 27),
    _TmnxNatMemSicrStateDeletePending_Type()
)
tmnxNatMemSicrStateDeletePending.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatMemSicrStateDeletePending.setStatus("current")
_TmnxNatMemSicrStatsTable_Object = MibTable
tmnxNatMemSicrStatsTable = _TmnxNatMemSicrStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 1, 3, 12)
)
if mibBuilder.loadTexts:
    tmnxNatMemSicrStatsTable.setStatus("current")
_TmnxNatMemSicrStatsEntry_Object = MibTableRow
tmnxNatMemSicrStatsEntry = _TmnxNatMemSicrStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 1, 3, 12, 1)
)
if mibBuilder.loadTexts:
    tmnxNatMemSicrStatsEntry.setStatus("current")
_TmnxNatMemSicrStatsTx_Type = Counter64
_TmnxNatMemSicrStatsTx_Object = MibTableColumn
tmnxNatMemSicrStatsTx = _TmnxNatMemSicrStatsTx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 1, 3, 12, 1, 1),
    _TmnxNatMemSicrStatsTx_Type()
)
tmnxNatMemSicrStatsTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatMemSicrStatsTx.setStatus("current")
_TmnxNatMemSicrStatsTxRetransmit_Type = Counter64
_TmnxNatMemSicrStatsTxRetransmit_Object = MibTableColumn
tmnxNatMemSicrStatsTxRetransmit = _TmnxNatMemSicrStatsTxRetransmit_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 1, 3, 12, 1, 2),
    _TmnxNatMemSicrStatsTxRetransmit_Type()
)
tmnxNatMemSicrStatsTxRetransmit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatMemSicrStatsTxRetransmit.setStatus("current")
_TmnxNatMemSicrStatsTxFlowCreate_Type = Counter64
_TmnxNatMemSicrStatsTxFlowCreate_Object = MibTableColumn
tmnxNatMemSicrStatsTxFlowCreate = _TmnxNatMemSicrStatsTxFlowCreate_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 1, 3, 12, 1, 3),
    _TmnxNatMemSicrStatsTxFlowCreate_Type()
)
tmnxNatMemSicrStatsTxFlowCreate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatMemSicrStatsTxFlowCreate.setStatus("current")
_TmnxNatMemSicrStatsTxFlowDelete_Type = Counter64
_TmnxNatMemSicrStatsTxFlowDelete_Object = MibTableColumn
tmnxNatMemSicrStatsTxFlowDelete = _TmnxNatMemSicrStatsTxFlowDelete_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 1, 3, 12, 1, 4),
    _TmnxNatMemSicrStatsTxFlowDelete_Type()
)
tmnxNatMemSicrStatsTxFlowDelete.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatMemSicrStatsTxFlowDelete.setStatus("current")
_TmnxNatMemSicrStatsRx_Type = Counter64
_TmnxNatMemSicrStatsRx_Object = MibTableColumn
tmnxNatMemSicrStatsRx = _TmnxNatMemSicrStatsRx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 1, 3, 12, 1, 5),
    _TmnxNatMemSicrStatsRx_Type()
)
tmnxNatMemSicrStatsRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatMemSicrStatsRx.setStatus("current")
_TmnxNatMemSicrStatsRxFlowCreate_Type = Counter64
_TmnxNatMemSicrStatsRxFlowCreate_Object = MibTableColumn
tmnxNatMemSicrStatsRxFlowCreate = _TmnxNatMemSicrStatsRxFlowCreate_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 1, 3, 12, 1, 6),
    _TmnxNatMemSicrStatsRxFlowCreate_Type()
)
tmnxNatMemSicrStatsRxFlowCreate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatMemSicrStatsRxFlowCreate.setStatus("current")
_TmnxNatMemSicrStatsRxFlowDelete_Type = Counter64
_TmnxNatMemSicrStatsRxFlowDelete_Object = MibTableColumn
tmnxNatMemSicrStatsRxFlowDelete = _TmnxNatMemSicrStatsRxFlowDelete_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 1, 3, 12, 1, 7),
    _TmnxNatMemSicrStatsRxFlowDelete_Type()
)
tmnxNatMemSicrStatsRxFlowDelete.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatMemSicrStatsRxFlowDelete.setStatus("current")
_TmnxNatMemSicrStatsErrNoPolicy_Type = Counter64
_TmnxNatMemSicrStatsErrNoPolicy_Object = MibTableColumn
tmnxNatMemSicrStatsErrNoPolicy = _TmnxNatMemSicrStatsErrNoPolicy_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 1, 3, 12, 1, 8),
    _TmnxNatMemSicrStatsErrNoPolicy_Type()
)
tmnxNatMemSicrStatsErrNoPolicy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatMemSicrStatsErrNoPolicy.setStatus("current")
_TmnxNatMemSicrStatsErrNoBlk_Type = Counter64
_TmnxNatMemSicrStatsErrNoBlk_Object = MibTableColumn
tmnxNatMemSicrStatsErrNoBlk = _TmnxNatMemSicrStatsErrNoBlk_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 1, 3, 12, 1, 9),
    _TmnxNatMemSicrStatsErrNoBlk_Type()
)
tmnxNatMemSicrStatsErrNoBlk.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatMemSicrStatsErrNoBlk.setStatus("current")
_TmnxNatMemSicrStatsErrFrag_Type = Counter64
_TmnxNatMemSicrStatsErrFrag_Object = MibTableColumn
tmnxNatMemSicrStatsErrFrag = _TmnxNatMemSicrStatsErrFrag_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 1, 3, 12, 1, 10),
    _TmnxNatMemSicrStatsErrFrag_Type()
)
tmnxNatMemSicrStatsErrFrag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatMemSicrStatsErrFrag.setStatus("current")
_TmnxNatMemSicrStatsTxAlg_Type = Counter64
_TmnxNatMemSicrStatsTxAlg_Object = MibTableColumn
tmnxNatMemSicrStatsTxAlg = _TmnxNatMemSicrStatsTxAlg_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 1, 3, 12, 1, 11),
    _TmnxNatMemSicrStatsTxAlg_Type()
)
tmnxNatMemSicrStatsTxAlg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatMemSicrStatsTxAlg.setStatus("current")
_TmnxNatMemSicrStatsRxAlg_Type = Counter64
_TmnxNatMemSicrStatsRxAlg_Object = MibTableColumn
tmnxNatMemSicrStatsRxAlg = _TmnxNatMemSicrStatsRxAlg_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 1, 3, 12, 1, 12),
    _TmnxNatMemSicrStatsRxAlg_Type()
)
tmnxNatMemSicrStatsRxAlg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatMemSicrStatsRxAlg.setStatus("current")
_TmnxNatEsaObjs_ObjectIdentity = ObjectIdentity
tmnxNatEsaObjs = _TmnxNatEsaObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 1, 4)
)
_TmnxNatVappTable_Object = MibTable
tmnxNatVappTable = _TmnxNatVappTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 1, 4, 1)
)
if mibBuilder.loadTexts:
    tmnxNatVappTable.setStatus("current")
_TmnxNatVappEntry_Object = MibTableRow
tmnxNatVappEntry = _TmnxNatVappEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 1, 4, 1, 1)
)
tmnxNatVappEntry.setIndexNames(
    (0, "TIMETRA-NAT-MIB", "tmnxNatIsaGrpId"),
    (0, "TIMETRA-NAT-MIB", "tmnxNatEsaNum"),
    (0, "TIMETRA-NAT-MIB", "tmnxNatEsaVappNum"),
)
if mibBuilder.loadTexts:
    tmnxNatVappEntry.setStatus("current")


class _TmnxNatEsaNum_Type(TmnxEsaNum):
    """Custom type tmnxNatEsaNum based on TmnxEsaNum"""
    subtypeSpec = TmnxEsaNum.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_TmnxNatEsaNum_Type.__name__ = "TmnxEsaNum"
_TmnxNatEsaNum_Object = MibTableColumn
tmnxNatEsaNum = _TmnxNatEsaNum_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 1, 4, 1, 1, 1),
    _TmnxNatEsaNum_Type()
)
tmnxNatEsaNum.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxNatEsaNum.setStatus("current")


class _TmnxNatEsaVappNum_Type(TmnxEsaVappNum):
    """Custom type tmnxNatEsaVappNum based on TmnxEsaVappNum"""
    subtypeSpec = TmnxEsaVappNum.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_TmnxNatEsaVappNum_Type.__name__ = "TmnxEsaVappNum"
_TmnxNatEsaVappNum_Object = MibTableColumn
tmnxNatEsaVappNum = _TmnxNatEsaVappNum_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 1, 4, 1, 1, 2),
    _TmnxNatEsaVappNum_Type()
)
tmnxNatEsaVappNum.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxNatEsaVappNum.setStatus("current")
_TmnxNatVappRowStatus_Type = RowStatus
_TmnxNatVappRowStatus_Object = MibTableColumn
tmnxNatVappRowStatus = _TmnxNatVappRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 1, 4, 1, 1, 3),
    _TmnxNatVappRowStatus_Type()
)
tmnxNatVappRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxNatVappRowStatus.setStatus("current")
_TmnxNatVappLastMgmtChange_Type = TimeStamp
_TmnxNatVappLastMgmtChange_Object = MibTableColumn
tmnxNatVappLastMgmtChange = _TmnxNatVappLastMgmtChange_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 1, 4, 1, 1, 4),
    _TmnxNatVappLastMgmtChange_Type()
)
tmnxNatVappLastMgmtChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatVappLastMgmtChange.setStatus("current")
_TmnxNatVappStatTable_Object = MibTable
tmnxNatVappStatTable = _TmnxNatVappStatTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 1, 4, 2)
)
if mibBuilder.loadTexts:
    tmnxNatVappStatTable.setStatus("current")
_TmnxNatVappStatEntry_Object = MibTableRow
tmnxNatVappStatEntry = _TmnxNatVappStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 1, 4, 2, 1)
)
if mibBuilder.loadTexts:
    tmnxNatVappStatEntry.setStatus("current")
_TmnxNatVappStatOperState_Type = TmnxNatIsaMdaOperState
_TmnxNatVappStatOperState_Object = MibTableColumn
tmnxNatVappStatOperState = _TmnxNatVappStatOperState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 1, 4, 2, 1, 1),
    _TmnxNatVappStatOperState_Type()
)
tmnxNatVappStatOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatVappStatOperState.setStatus("current")


class _TmnxNatVappStatResrcAllocated_Type(Unsigned32):
    """Custom type tmnxNatVappStatResrcAllocated based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_TmnxNatVappStatResrcAllocated_Type.__name__ = "Unsigned32"
_TmnxNatVappStatResrcAllocated_Object = MibTableColumn
tmnxNatVappStatResrcAllocated = _TmnxNatVappStatResrcAllocated_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 1, 4, 2, 1, 2),
    _TmnxNatVappStatResrcAllocated_Type()
)
tmnxNatVappStatResrcAllocated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatVappStatResrcAllocated.setStatus("current")
if mibBuilder.loadTexts:
    tmnxNatVappStatResrcAllocated.setUnits("percent")
_TmnxNatVappStatBypassL2AwHost_Type = Unsigned32
_TmnxNatVappStatBypassL2AwHost_Object = MibTableColumn
tmnxNatVappStatBypassL2AwHost = _TmnxNatVappStatBypassL2AwHost_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 1, 4, 2, 1, 3),
    _TmnxNatVappStatBypassL2AwHost_Type()
)
tmnxNatVappStatBypassL2AwHost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatVappStatBypassL2AwHost.setStatus("current")
_TmnxNatVappResrcStatsTable_Object = MibTable
tmnxNatVappResrcStatsTable = _TmnxNatVappResrcStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 1, 4, 3)
)
if mibBuilder.loadTexts:
    tmnxNatVappResrcStatsTable.setStatus("current")
_TmnxNatVappResrcStatsEntry_Object = MibTableRow
tmnxNatVappResrcStatsEntry = _TmnxNatVappResrcStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 1, 4, 3, 1)
)
tmnxNatVappResrcStatsEntry.setIndexNames(
    (0, "TIMETRA-NAT-MIB", "tmnxNatEsaNum"),
    (0, "TIMETRA-NAT-MIB", "tmnxNatEsaVappNum"),
    (0, "TIMETRA-NAT-MIB", "tmnxNatVappResrcStatsId"),
)
if mibBuilder.loadTexts:
    tmnxNatVappResrcStatsEntry.setStatus("current")


class _TmnxNatVappResrcStatsId_Type(Unsigned32):
    """Custom type tmnxNatVappResrcStatsId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 49),
    )


_TmnxNatVappResrcStatsId_Type.__name__ = "Unsigned32"
_TmnxNatVappResrcStatsId_Object = MibTableColumn
tmnxNatVappResrcStatsId = _TmnxNatVappResrcStatsId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 1, 4, 3, 1, 1),
    _TmnxNatVappResrcStatsId_Type()
)
tmnxNatVappResrcStatsId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxNatVappResrcStatsId.setStatus("current")


class _TmnxNatVappResrcStatsName_Type(DisplayString):
    """Custom type tmnxNatVappResrcStatsName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_TmnxNatVappResrcStatsName_Type.__name__ = "DisplayString"
_TmnxNatVappResrcStatsName_Object = MibTableColumn
tmnxNatVappResrcStatsName = _TmnxNatVappResrcStatsName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 1, 4, 3, 1, 2),
    _TmnxNatVappResrcStatsName_Type()
)
tmnxNatVappResrcStatsName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatVappResrcStatsName.setStatus("current")
_TmnxNatVappResrcStatsValMax_Type = CounterBasedGauge64
_TmnxNatVappResrcStatsValMax_Object = MibTableColumn
tmnxNatVappResrcStatsValMax = _TmnxNatVappResrcStatsValMax_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 1, 4, 3, 1, 3),
    _TmnxNatVappResrcStatsValMax_Type()
)
tmnxNatVappResrcStatsValMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatVappResrcStatsValMax.setStatus("current")
_TmnxNatVappResrcStatsValMaxLw_Type = Gauge32
_TmnxNatVappResrcStatsValMaxLw_Object = MibTableColumn
tmnxNatVappResrcStatsValMaxLw = _TmnxNatVappResrcStatsValMaxLw_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 1, 4, 3, 1, 4),
    _TmnxNatVappResrcStatsValMaxLw_Type()
)
tmnxNatVappResrcStatsValMaxLw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatVappResrcStatsValMaxLw.setStatus("current")
_TmnxNatVappResrcStatsValMaxHw_Type = Gauge32
_TmnxNatVappResrcStatsValMaxHw_Object = MibTableColumn
tmnxNatVappResrcStatsValMaxHw = _TmnxNatVappResrcStatsValMaxHw_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 1, 4, 3, 1, 5),
    _TmnxNatVappResrcStatsValMaxHw_Type()
)
tmnxNatVappResrcStatsValMaxHw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatVappResrcStatsValMaxHw.setStatus("current")
_TmnxNatVappResrcStatsVal_Type = CounterBasedGauge64
_TmnxNatVappResrcStatsVal_Object = MibTableColumn
tmnxNatVappResrcStatsVal = _TmnxNatVappResrcStatsVal_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 1, 4, 3, 1, 6),
    _TmnxNatVappResrcStatsVal_Type()
)
tmnxNatVappResrcStatsVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatVappResrcStatsVal.setStatus("current")
_TmnxNatVappResrcStatsValLw_Type = Gauge32
_TmnxNatVappResrcStatsValLw_Object = MibTableColumn
tmnxNatVappResrcStatsValLw = _TmnxNatVappResrcStatsValLw_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 1, 4, 3, 1, 7),
    _TmnxNatVappResrcStatsValLw_Type()
)
tmnxNatVappResrcStatsValLw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatVappResrcStatsValLw.setStatus("current")
_TmnxNatVappResrcStatsValHw_Type = Gauge32
_TmnxNatVappResrcStatsValHw_Object = MibTableColumn
tmnxNatVappResrcStatsValHw = _TmnxNatVappResrcStatsValHw_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 1, 4, 3, 1, 8),
    _TmnxNatVappResrcStatsValHw_Type()
)
tmnxNatVappResrcStatsValHw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatVappResrcStatsValHw.setStatus("current")
_TmnxNatVappResrcStatsLimited_Type = TruthValue
_TmnxNatVappResrcStatsLimited_Object = MibTableColumn
tmnxNatVappResrcStatsLimited = _TmnxNatVappResrcStatsLimited_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 1, 4, 3, 1, 9),
    _TmnxNatVappResrcStatsLimited_Type()
)
tmnxNatVappResrcStatsLimited.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatVappResrcStatsLimited.setStatus("current")
_TmnxNatVappResrcStatsValPeak_Type = CounterBasedGauge64
_TmnxNatVappResrcStatsValPeak_Object = MibTableColumn
tmnxNatVappResrcStatsValPeak = _TmnxNatVappResrcStatsValPeak_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 1, 4, 3, 1, 10),
    _TmnxNatVappResrcStatsValPeak_Type()
)
tmnxNatVappResrcStatsValPeak.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatVappResrcStatsValPeak.setStatus("current")
_TmnxNatVappResrcStatsValPeakLw_Type = Gauge32
_TmnxNatVappResrcStatsValPeakLw_Object = MibTableColumn
tmnxNatVappResrcStatsValPeakLw = _TmnxNatVappResrcStatsValPeakLw_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 1, 4, 3, 1, 11),
    _TmnxNatVappResrcStatsValPeakLw_Type()
)
tmnxNatVappResrcStatsValPeakLw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatVappResrcStatsValPeakLw.setStatus("current")
_TmnxNatVappResrcStatsValPeakHw_Type = Gauge32
_TmnxNatVappResrcStatsValPeakHw_Object = MibTableColumn
tmnxNatVappResrcStatsValPeakHw = _TmnxNatVappResrcStatsValPeakHw_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 1, 4, 3, 1, 12),
    _TmnxNatVappResrcStatsValPeakHw_Type()
)
tmnxNatVappResrcStatsValPeakHw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatVappResrcStatsValPeakHw.setStatus("current")


class _TmnxNatVappResrcStatsPeakTime_Type(DateAndTime):
    """Custom type tmnxNatVappResrcStatsPeakTime based on DateAndTime"""
    subtypeSpec = DateAndTime.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(11, 11),
    )
    fixed_length = 11


_TmnxNatVappResrcStatsPeakTime_Type.__name__ = "DateAndTime"
_TmnxNatVappResrcStatsPeakTime_Object = MibTableColumn
tmnxNatVappResrcStatsPeakTime = _TmnxNatVappResrcStatsPeakTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 1, 4, 3, 1, 13),
    _TmnxNatVappResrcStatsPeakTime_Type()
)
tmnxNatVappResrcStatsPeakTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatVappResrcStatsPeakTime.setStatus("current")
_TmnxNatVappRecoveryAction_ObjectIdentity = ObjectIdentity
tmnxNatVappRecoveryAction = _TmnxNatVappRecoveryAction_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 1, 4, 4)
)
_TmnxNatVappRecovActEsaNum_Type = TmnxEsaNum
_TmnxNatVappRecovActEsaNum_Object = MibScalar
tmnxNatVappRecovActEsaNum = _TmnxNatVappRecovActEsaNum_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 1, 4, 4, 1),
    _TmnxNatVappRecovActEsaNum_Type()
)
tmnxNatVappRecovActEsaNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxNatVappRecovActEsaNum.setStatus("current")
_TmnxNatVappRecovActEsaVappNum_Type = TmnxEsaVappNum
_TmnxNatVappRecovActEsaVappNum_Object = MibScalar
tmnxNatVappRecovActEsaVappNum = _TmnxNatVappRecovActEsaVappNum_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 1, 4, 4, 2),
    _TmnxNatVappRecovActEsaVappNum_Type()
)
tmnxNatVappRecovActEsaVappNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxNatVappRecovActEsaVappNum.setStatus("current")
_TmnxNatVappRecovActActionGo_Type = TmnxActionType
_TmnxNatVappRecovActActionGo_Object = MibScalar
tmnxNatVappRecovActActionGo = _TmnxNatVappRecovActActionGo_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 1, 4, 4, 3),
    _TmnxNatVappRecovActActionGo_Type()
)
tmnxNatVappRecovActActionGo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxNatVappRecovActActionGo.setStatus("current")


class _TmnxNatVappRecovActActionResult_Type(Integer32):
    """Custom type tmnxNatVappRecovActActionResult based on Integer32"""
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
        *(("ack", 0),
          ("nak", 1),
          ("notUsed", 2),
          ("notActive", 3),
          ("notInBypass", 4))
    )


_TmnxNatVappRecovActActionResult_Type.__name__ = "Integer32"
_TmnxNatVappRecovActActionResult_Object = MibScalar
tmnxNatVappRecovActActionResult = _TmnxNatVappRecovActActionResult_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 1, 4, 4, 4),
    _TmnxNatVappRecovActActionResult_Type()
)
tmnxNatVappRecovActActionResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatVappRecovActActionResult.setStatus("current")
_TmnxNatVappPlcyStatsTable_Object = MibTable
tmnxNatVappPlcyStatsTable = _TmnxNatVappPlcyStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 1, 4, 5)
)
if mibBuilder.loadTexts:
    tmnxNatVappPlcyStatsTable.setStatus("current")
_TmnxNatVappPlcyStatsEntry_Object = MibTableRow
tmnxNatVappPlcyStatsEntry = _TmnxNatVappPlcyStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 1, 4, 5, 1)
)
tmnxNatVappPlcyStatsEntry.setIndexNames(
    (0, "TIMETRA-NAT-MIB", "tmnxNatPlcyName"),
    (0, "TIMETRA-NAT-MIB", "tmnxNatEsaNum"),
    (0, "TIMETRA-NAT-MIB", "tmnxNatEsaVappNum"),
    (0, "TIMETRA-NAT-MIB", "tmnxNatVappPlcyStatsType"),
)
if mibBuilder.loadTexts:
    tmnxNatVappPlcyStatsEntry.setStatus("current")
_TmnxNatVappPlcyStatsType_Type = TmnxNatUsageStatsType
_TmnxNatVappPlcyStatsType_Object = MibTableColumn
tmnxNatVappPlcyStatsType = _TmnxNatVappPlcyStatsType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 1, 4, 5, 1, 1),
    _TmnxNatVappPlcyStatsType_Type()
)
tmnxNatVappPlcyStatsType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxNatVappPlcyStatsType.setStatus("current")


class _TmnxNatVappPlcyStatsName_Type(DisplayString):
    """Custom type tmnxNatVappPlcyStatsName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_TmnxNatVappPlcyStatsName_Type.__name__ = "DisplayString"
_TmnxNatVappPlcyStatsName_Object = MibTableColumn
tmnxNatVappPlcyStatsName = _TmnxNatVappPlcyStatsName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 1, 4, 5, 1, 2),
    _TmnxNatVappPlcyStatsName_Type()
)
tmnxNatVappPlcyStatsName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatVappPlcyStatsName.setStatus("current")
_TmnxNatVappPlcyStatsVal_Type = Gauge32
_TmnxNatVappPlcyStatsVal_Object = MibTableColumn
tmnxNatVappPlcyStatsVal = _TmnxNatVappPlcyStatsVal_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 1, 4, 5, 1, 3),
    _TmnxNatVappPlcyStatsVal_Type()
)
tmnxNatVappPlcyStatsVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatVappPlcyStatsVal.setStatus("current")
_TmnxNatVappStatsHrTable_Object = MibTable
tmnxNatVappStatsHrTable = _TmnxNatVappStatsHrTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 1, 4, 6)
)
if mibBuilder.loadTexts:
    tmnxNatVappStatsHrTable.setStatus("current")
_TmnxNatVappStatsHrEntry_Object = MibTableRow
tmnxNatVappStatsHrEntry = _TmnxNatVappStatsHrEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 1, 4, 6, 1)
)
tmnxNatVappStatsHrEntry.setIndexNames(
    (0, "TIMETRA-NAT-MIB", "tmnxNatIsaGrpId"),
    (0, "TIMETRA-NAT-MIB", "tmnxNatEsaNum"),
    (0, "TIMETRA-NAT-MIB", "tmnxNatEsaVappNum"),
    (0, "TIMETRA-NAT-MIB", "tmnxNatVappStatsHrIndex"),
)
if mibBuilder.loadTexts:
    tmnxNatVappStatsHrEntry.setStatus("current")
_TmnxNatVappStatsHrIndex_Type = Unsigned32
_TmnxNatVappStatsHrIndex_Object = MibTableColumn
tmnxNatVappStatsHrIndex = _TmnxNatVappStatsHrIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 1, 4, 6, 1, 1),
    _TmnxNatVappStatsHrIndex_Type()
)
tmnxNatVappStatsHrIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxNatVappStatsHrIndex.setStatus("current")


class _TmnxNatVappStatsHrTime_Type(DateAndTime):
    """Custom type tmnxNatVappStatsHrTime based on DateAndTime"""
    subtypeSpec = DateAndTime.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(11, 11),
    )
    fixed_length = 11


_TmnxNatVappStatsHrTime_Type.__name__ = "DateAndTime"
_TmnxNatVappStatsHrTime_Object = MibTableColumn
tmnxNatVappStatsHrTime = _TmnxNatVappStatsHrTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 1, 4, 6, 1, 2),
    _TmnxNatVappStatsHrTime_Type()
)
tmnxNatVappStatsHrTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatVappStatsHrTime.setStatus("current")
_TmnxNatVappStatsHrWaiting_Type = TmnxPerTenThousand
_TmnxNatVappStatsHrWaiting_Object = MibTableColumn
tmnxNatVappStatsHrWaiting = _TmnxNatVappStatsHrWaiting_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 1, 4, 6, 1, 3),
    _TmnxNatVappStatsHrWaiting_Type()
)
tmnxNatVappStatsHrWaiting.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatVappStatsHrWaiting.setStatus("current")
_TmnxNatVappStatsHrIdle_Type = TmnxPerTenThousand
_TmnxNatVappStatsHrIdle_Object = MibTableColumn
tmnxNatVappStatsHrIdle = _TmnxNatVappStatsHrIdle_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 1, 4, 6, 1, 4),
    _TmnxNatVappStatsHrIdle_Type()
)
tmnxNatVappStatsHrIdle.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatVappStatsHrIdle.setStatus("current")
_TmnxNatVappStatsHrWorking_Type = TmnxPerTenThousand
_TmnxNatVappStatsHrWorking_Object = MibTableColumn
tmnxNatVappStatsHrWorking = _TmnxNatVappStatsHrWorking_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 1, 4, 6, 1, 5),
    _TmnxNatVappStatsHrWorking_Type()
)
tmnxNatVappStatsHrWorking.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatVappStatsHrWorking.setStatus("current")
_TmnxNatVappStatsHrJobs_Type = Unsigned32
_TmnxNatVappStatsHrJobs_Object = MibTableColumn
tmnxNatVappStatsHrJobs = _TmnxNatVappStatsHrJobs_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 1, 4, 6, 1, 6),
    _TmnxNatVappStatsHrJobs_Type()
)
tmnxNatVappStatsHrJobs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatVappStatsHrJobs.setStatus("current")
_TmnxNatVappStatsHrThroughput_Type = Counter64
_TmnxNatVappStatsHrThroughput_Object = MibTableColumn
tmnxNatVappStatsHrThroughput = _TmnxNatVappStatsHrThroughput_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 1, 4, 6, 1, 7),
    _TmnxNatVappStatsHrThroughput_Type()
)
tmnxNatVappStatsHrThroughput.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatVappStatsHrThroughput.setStatus("current")
_TmnxNatVappStatsDayTable_Object = MibTable
tmnxNatVappStatsDayTable = _TmnxNatVappStatsDayTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 1, 4, 7)
)
if mibBuilder.loadTexts:
    tmnxNatVappStatsDayTable.setStatus("current")
_TmnxNatVappStatsDayEntry_Object = MibTableRow
tmnxNatVappStatsDayEntry = _TmnxNatVappStatsDayEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 1, 4, 7, 1)
)
tmnxNatVappStatsDayEntry.setIndexNames(
    (0, "TIMETRA-NAT-MIB", "tmnxNatIsaGrpId"),
    (0, "TIMETRA-NAT-MIB", "tmnxNatEsaNum"),
    (0, "TIMETRA-NAT-MIB", "tmnxNatEsaVappNum"),
    (0, "TIMETRA-NAT-MIB", "tmnxNatVappStatsDayIndex"),
)
if mibBuilder.loadTexts:
    tmnxNatVappStatsDayEntry.setStatus("current")
_TmnxNatVappStatsDayIndex_Type = Unsigned32
_TmnxNatVappStatsDayIndex_Object = MibTableColumn
tmnxNatVappStatsDayIndex = _TmnxNatVappStatsDayIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 1, 4, 7, 1, 1),
    _TmnxNatVappStatsDayIndex_Type()
)
tmnxNatVappStatsDayIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxNatVappStatsDayIndex.setStatus("current")


class _TmnxNatVappStatsDayTime_Type(DateAndTime):
    """Custom type tmnxNatVappStatsDayTime based on DateAndTime"""
    subtypeSpec = DateAndTime.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(11, 11),
    )
    fixed_length = 11


_TmnxNatVappStatsDayTime_Type.__name__ = "DateAndTime"
_TmnxNatVappStatsDayTime_Object = MibTableColumn
tmnxNatVappStatsDayTime = _TmnxNatVappStatsDayTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 1, 4, 7, 1, 2),
    _TmnxNatVappStatsDayTime_Type()
)
tmnxNatVappStatsDayTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatVappStatsDayTime.setStatus("current")
_TmnxNatVappStatsDayWaiting_Type = TmnxPerTenThousand
_TmnxNatVappStatsDayWaiting_Object = MibTableColumn
tmnxNatVappStatsDayWaiting = _TmnxNatVappStatsDayWaiting_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 1, 4, 7, 1, 3),
    _TmnxNatVappStatsDayWaiting_Type()
)
tmnxNatVappStatsDayWaiting.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatVappStatsDayWaiting.setStatus("current")
_TmnxNatVappStatsDayIdle_Type = TmnxPerTenThousand
_TmnxNatVappStatsDayIdle_Object = MibTableColumn
tmnxNatVappStatsDayIdle = _TmnxNatVappStatsDayIdle_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 1, 4, 7, 1, 4),
    _TmnxNatVappStatsDayIdle_Type()
)
tmnxNatVappStatsDayIdle.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatVappStatsDayIdle.setStatus("current")
_TmnxNatVappStatsDayWorking_Type = TmnxPerTenThousand
_TmnxNatVappStatsDayWorking_Object = MibTableColumn
tmnxNatVappStatsDayWorking = _TmnxNatVappStatsDayWorking_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 1, 4, 7, 1, 5),
    _TmnxNatVappStatsDayWorking_Type()
)
tmnxNatVappStatsDayWorking.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatVappStatsDayWorking.setStatus("current")
_TmnxNatVappStatsDayJobs_Type = Unsigned32
_TmnxNatVappStatsDayJobs_Object = MibTableColumn
tmnxNatVappStatsDayJobs = _TmnxNatVappStatsDayJobs_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 1, 4, 7, 1, 6),
    _TmnxNatVappStatsDayJobs_Type()
)
tmnxNatVappStatsDayJobs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatVappStatsDayJobs.setStatus("current")
_TmnxNatVappStatsDayThroughput_Type = Counter64
_TmnxNatVappStatsDayThroughput_Object = MibTableColumn
tmnxNatVappStatsDayThroughput = _TmnxNatVappStatsDayThroughput_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 1, 4, 7, 1, 7),
    _TmnxNatVappStatsDayThroughput_Type()
)
tmnxNatVappStatsDayThroughput.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatVappStatsDayThroughput.setStatus("current")
_TmnxNatVappStatsMonthTable_Object = MibTable
tmnxNatVappStatsMonthTable = _TmnxNatVappStatsMonthTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 1, 4, 8)
)
if mibBuilder.loadTexts:
    tmnxNatVappStatsMonthTable.setStatus("current")
_TmnxNatVappStatsMonthEntry_Object = MibTableRow
tmnxNatVappStatsMonthEntry = _TmnxNatVappStatsMonthEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 1, 4, 8, 1)
)
tmnxNatVappStatsMonthEntry.setIndexNames(
    (0, "TIMETRA-NAT-MIB", "tmnxNatIsaGrpId"),
    (0, "TIMETRA-NAT-MIB", "tmnxNatEsaNum"),
    (0, "TIMETRA-NAT-MIB", "tmnxNatEsaVappNum"),
    (0, "TIMETRA-NAT-MIB", "tmnxNatVappStatsMonthIndex"),
)
if mibBuilder.loadTexts:
    tmnxNatVappStatsMonthEntry.setStatus("current")
_TmnxNatVappStatsMonthIndex_Type = Unsigned32
_TmnxNatVappStatsMonthIndex_Object = MibTableColumn
tmnxNatVappStatsMonthIndex = _TmnxNatVappStatsMonthIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 1, 4, 8, 1, 1),
    _TmnxNatVappStatsMonthIndex_Type()
)
tmnxNatVappStatsMonthIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxNatVappStatsMonthIndex.setStatus("current")


class _TmnxNatVappStatsMonthTime_Type(DateAndTime):
    """Custom type tmnxNatVappStatsMonthTime based on DateAndTime"""
    subtypeSpec = DateAndTime.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(11, 11),
    )
    fixed_length = 11


_TmnxNatVappStatsMonthTime_Type.__name__ = "DateAndTime"
_TmnxNatVappStatsMonthTime_Object = MibTableColumn
tmnxNatVappStatsMonthTime = _TmnxNatVappStatsMonthTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 1, 4, 8, 1, 2),
    _TmnxNatVappStatsMonthTime_Type()
)
tmnxNatVappStatsMonthTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatVappStatsMonthTime.setStatus("current")
_TmnxNatVappStatsMonthWaiting_Type = TmnxPerTenThousand
_TmnxNatVappStatsMonthWaiting_Object = MibTableColumn
tmnxNatVappStatsMonthWaiting = _TmnxNatVappStatsMonthWaiting_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 1, 4, 8, 1, 3),
    _TmnxNatVappStatsMonthWaiting_Type()
)
tmnxNatVappStatsMonthWaiting.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatVappStatsMonthWaiting.setStatus("current")
_TmnxNatVappStatsMonthIdle_Type = TmnxPerTenThousand
_TmnxNatVappStatsMonthIdle_Object = MibTableColumn
tmnxNatVappStatsMonthIdle = _TmnxNatVappStatsMonthIdle_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 1, 4, 8, 1, 4),
    _TmnxNatVappStatsMonthIdle_Type()
)
tmnxNatVappStatsMonthIdle.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatVappStatsMonthIdle.setStatus("current")
_TmnxNatVappStatsMonthWorking_Type = TmnxPerTenThousand
_TmnxNatVappStatsMonthWorking_Object = MibTableColumn
tmnxNatVappStatsMonthWorking = _TmnxNatVappStatsMonthWorking_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 1, 4, 8, 1, 5),
    _TmnxNatVappStatsMonthWorking_Type()
)
tmnxNatVappStatsMonthWorking.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatVappStatsMonthWorking.setStatus("current")
_TmnxNatVappStatsMonthJobs_Type = Unsigned32
_TmnxNatVappStatsMonthJobs_Object = MibTableColumn
tmnxNatVappStatsMonthJobs = _TmnxNatVappStatsMonthJobs_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 1, 4, 8, 1, 6),
    _TmnxNatVappStatsMonthJobs_Type()
)
tmnxNatVappStatsMonthJobs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatVappStatsMonthJobs.setStatus("current")
_TmnxNatVappStatsMonthThroughp_Type = Counter64
_TmnxNatVappStatsMonthThroughp_Object = MibTableColumn
tmnxNatVappStatsMonthThroughp = _TmnxNatVappStatsMonthThroughp_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 1, 4, 8, 1, 7),
    _TmnxNatVappStatsMonthThroughp_Type()
)
tmnxNatVappStatsMonthThroughp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatVappStatsMonthThroughp.setStatus("current")
_TmnxMapTVappTable_Object = MibTable
tmnxMapTVappTable = _TmnxMapTVappTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 1, 4, 9)
)
if mibBuilder.loadTexts:
    tmnxMapTVappTable.setStatus("current")
_TmnxMapTVappEntry_Object = MibTableRow
tmnxMapTVappEntry = _TmnxMapTVappEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 1, 4, 9, 1)
)
tmnxMapTVappEntry.setIndexNames(
    (0, "TIMETRA-NAT-MIB", "tmnxNatMapTGrpIsaGrpId"),
    (0, "TIMETRA-NAT-MIB", "tmnxMapTVappEsaNum"),
    (0, "TIMETRA-NAT-MIB", "tmnxMapTVappEsaVappNum"),
)
if mibBuilder.loadTexts:
    tmnxMapTVappEntry.setStatus("current")


class _TmnxMapTVappEsaNum_Type(TmnxEsaNum):
    """Custom type tmnxMapTVappEsaNum based on TmnxEsaNum"""
    subtypeSpec = TmnxEsaNum.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_TmnxMapTVappEsaNum_Type.__name__ = "TmnxEsaNum"
_TmnxMapTVappEsaNum_Object = MibTableColumn
tmnxMapTVappEsaNum = _TmnxMapTVappEsaNum_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 1, 4, 9, 1, 1),
    _TmnxMapTVappEsaNum_Type()
)
tmnxMapTVappEsaNum.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxMapTVappEsaNum.setStatus("current")


class _TmnxMapTVappEsaVappNum_Type(TmnxEsaVappNum):
    """Custom type tmnxMapTVappEsaVappNum based on TmnxEsaVappNum"""
    subtypeSpec = TmnxEsaVappNum.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_TmnxMapTVappEsaVappNum_Type.__name__ = "TmnxEsaVappNum"
_TmnxMapTVappEsaVappNum_Object = MibTableColumn
tmnxMapTVappEsaVappNum = _TmnxMapTVappEsaVappNum_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 1, 4, 9, 1, 2),
    _TmnxMapTVappEsaVappNum_Type()
)
tmnxMapTVappEsaVappNum.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxMapTVappEsaVappNum.setStatus("current")
_TmnxMapTVappRowStatus_Type = RowStatus
_TmnxMapTVappRowStatus_Object = MibTableColumn
tmnxMapTVappRowStatus = _TmnxMapTVappRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 1, 4, 9, 1, 3),
    _TmnxMapTVappRowStatus_Type()
)
tmnxMapTVappRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxMapTVappRowStatus.setStatus("current")
_TmnxMapTVappLastCh_Type = TimeStamp
_TmnxMapTVappLastCh_Object = MibTableColumn
tmnxMapTVappLastCh = _TmnxMapTVappLastCh_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 1, 4, 9, 1, 4),
    _TmnxMapTVappLastCh_Type()
)
tmnxMapTVappLastCh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMapTVappLastCh.setStatus("current")
_TmnxMapTVappResrcStatsTable_Object = MibTable
tmnxMapTVappResrcStatsTable = _TmnxMapTVappResrcStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 1, 4, 10)
)
if mibBuilder.loadTexts:
    tmnxMapTVappResrcStatsTable.setStatus("current")
_TmnxMapTVappResrcStatsEntry_Object = MibTableRow
tmnxMapTVappResrcStatsEntry = _TmnxMapTVappResrcStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 1, 4, 10, 1)
)
tmnxMapTVappResrcStatsEntry.setIndexNames(
    (0, "TIMETRA-NAT-MIB", "tmnxMapTVappEsaNum"),
    (0, "TIMETRA-NAT-MIB", "tmnxMapTVappEsaVappNum"),
    (0, "TIMETRA-NAT-MIB", "tmnxMapTVappResrcStatsId"),
)
if mibBuilder.loadTexts:
    tmnxMapTVappResrcStatsEntry.setStatus("current")


class _TmnxMapTVappResrcStatsId_Type(Unsigned32):
    """Custom type tmnxMapTVappResrcStatsId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 49),
    )


_TmnxMapTVappResrcStatsId_Type.__name__ = "Unsigned32"
_TmnxMapTVappResrcStatsId_Object = MibTableColumn
tmnxMapTVappResrcStatsId = _TmnxMapTVappResrcStatsId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 1, 4, 10, 1, 1),
    _TmnxMapTVappResrcStatsId_Type()
)
tmnxMapTVappResrcStatsId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxMapTVappResrcStatsId.setStatus("current")


class _TmnxMapTVappResrcStatsName_Type(DisplayString):
    """Custom type tmnxMapTVappResrcStatsName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_TmnxMapTVappResrcStatsName_Type.__name__ = "DisplayString"
_TmnxMapTVappResrcStatsName_Object = MibTableColumn
tmnxMapTVappResrcStatsName = _TmnxMapTVappResrcStatsName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 1, 4, 10, 1, 2),
    _TmnxMapTVappResrcStatsName_Type()
)
tmnxMapTVappResrcStatsName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMapTVappResrcStatsName.setStatus("current")
_TmnxMapTVappResrcStatsVal_Type = CounterBasedGauge64
_TmnxMapTVappResrcStatsVal_Object = MibTableColumn
tmnxMapTVappResrcStatsVal = _TmnxMapTVappResrcStatsVal_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 1, 4, 10, 1, 3),
    _TmnxMapTVappResrcStatsVal_Type()
)
tmnxMapTVappResrcStatsVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMapTVappResrcStatsVal.setStatus("current")
_TmnxMapTVappResrcStatsMaxVal_Type = CounterBasedGauge64
_TmnxMapTVappResrcStatsMaxVal_Object = MibTableColumn
tmnxMapTVappResrcStatsMaxVal = _TmnxMapTVappResrcStatsMaxVal_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 1, 4, 10, 1, 4),
    _TmnxMapTVappResrcStatsMaxVal_Type()
)
tmnxMapTVappResrcStatsMaxVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMapTVappResrcStatsMaxVal.setStatus("current")
_TmnxMapTVappResrcStatsPeakVal_Type = CounterBasedGauge64
_TmnxMapTVappResrcStatsPeakVal_Object = MibTableColumn
tmnxMapTVappResrcStatsPeakVal = _TmnxMapTVappResrcStatsPeakVal_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 1, 4, 10, 1, 5),
    _TmnxMapTVappResrcStatsPeakVal_Type()
)
tmnxMapTVappResrcStatsPeakVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMapTVappResrcStatsPeakVal.setStatus("current")


class _TmnxMapTVappResrcStatsPeakTime_Type(DateAndTime):
    """Custom type tmnxMapTVappResrcStatsPeakTime based on DateAndTime"""
    subtypeSpec = DateAndTime.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(11, 11),
    )
    fixed_length = 11


_TmnxMapTVappResrcStatsPeakTime_Type.__name__ = "DateAndTime"
_TmnxMapTVappResrcStatsPeakTime_Object = MibTableColumn
tmnxMapTVappResrcStatsPeakTime = _TmnxMapTVappResrcStatsPeakTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 1, 4, 10, 1, 6),
    _TmnxMapTVappResrcStatsPeakTime_Type()
)
tmnxMapTVappResrcStatsPeakTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMapTVappResrcStatsPeakTime.setStatus("current")
_TmnxNatIsaGrpStatObjs_ObjectIdentity = ObjectIdentity
tmnxNatIsaGrpStatObjs = _TmnxNatIsaGrpStatObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 1, 5)
)
_TmnxNatGrpSicrStateTable_Object = MibTable
tmnxNatGrpSicrStateTable = _TmnxNatGrpSicrStateTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 1, 5, 1)
)
if mibBuilder.loadTexts:
    tmnxNatGrpSicrStateTable.setStatus("current")
_TmnxNatGrpSicrStateEntry_Object = MibTableRow
tmnxNatGrpSicrStateEntry = _TmnxNatGrpSicrStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 1, 5, 1, 1)
)
tmnxNatGrpSicrStateEntry.setIndexNames(
    (0, "TIMETRA-NAT-MIB", "tmnxNatIsaGrpId"),
)
if mibBuilder.loadTexts:
    tmnxNatGrpSicrStateEntry.setStatus("current")


class _TmnxNatGrpSicrState_Type(Integer32):
    """Custom type tmnxNatGrpSicrState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("initialWaitForPeer", 2),
          ("waitForPeer", 3),
          ("peerTimedOut", 4),
          ("active", 5),
          ("standby", 6),
          ("cleaningUp", 7))
    )


_TmnxNatGrpSicrState_Type.__name__ = "Integer32"
_TmnxNatGrpSicrState_Object = MibTableColumn
tmnxNatGrpSicrState = _TmnxNatGrpSicrState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 1, 5, 1, 1, 1),
    _TmnxNatGrpSicrState_Type()
)
tmnxNatGrpSicrState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatGrpSicrState.setStatus("current")
_TmnxNatGrpSicrStateChanges_Type = Counter32
_TmnxNatGrpSicrStateChanges_Object = MibTableColumn
tmnxNatGrpSicrStateChanges = _TmnxNatGrpSicrStateChanges_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 1, 5, 1, 1, 2),
    _TmnxNatGrpSicrStateChanges_Type()
)
tmnxNatGrpSicrStateChanges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatGrpSicrStateChanges.setStatus("current")
_TmnxNatGrpSicrStateLastCh_Type = TimeStamp
_TmnxNatGrpSicrStateLastCh_Object = MibTableColumn
tmnxNatGrpSicrStateLastCh = _TmnxNatGrpSicrStateLastCh_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 1, 5, 1, 1, 3),
    _TmnxNatGrpSicrStateLastCh_Type()
)
tmnxNatGrpSicrStateLastCh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatGrpSicrStateLastCh.setStatus("current")
_TmnxNatGrpSicrInControl_Type = TruthValue
_TmnxNatGrpSicrInControl_Object = MibTableColumn
tmnxNatGrpSicrInControl = _TmnxNatGrpSicrInControl_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 1, 5, 1, 1, 4),
    _TmnxNatGrpSicrInControl_Type()
)
tmnxNatGrpSicrInControl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatGrpSicrInControl.setStatus("current")
_TmnxNatGrpSicrHealth_Type = Unsigned32
_TmnxNatGrpSicrHealth_Object = MibTableColumn
tmnxNatGrpSicrHealth = _TmnxNatGrpSicrHealth_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 1, 5, 1, 1, 5),
    _TmnxNatGrpSicrHealth_Type()
)
tmnxNatGrpSicrHealth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatGrpSicrHealth.setStatus("current")
_TmnxNatGrpSicrPeerHealth_Type = Unsigned32
_TmnxNatGrpSicrPeerHealth_Object = MibTableColumn
tmnxNatGrpSicrPeerHealth = _TmnxNatGrpSicrPeerHealth_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 1, 5, 1, 1, 6),
    _TmnxNatGrpSicrPeerHealth_Type()
)
tmnxNatGrpSicrPeerHealth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatGrpSicrPeerHealth.setStatus("current")


class _TmnxNatGrpSicrPeerPreferred_Type(Integer32):
    """Custom type tmnxNatGrpSicrPeerPreferred based on Integer32"""
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
          ("true", 1),
          ("false", 2))
    )


_TmnxNatGrpSicrPeerPreferred_Type.__name__ = "Integer32"
_TmnxNatGrpSicrPeerPreferred_Object = MibTableColumn
tmnxNatGrpSicrPeerPreferred = _TmnxNatGrpSicrPeerPreferred_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 1, 5, 1, 1, 7),
    _TmnxNatGrpSicrPeerPreferred_Type()
)
tmnxNatGrpSicrPeerPreferred.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatGrpSicrPeerPreferred.setStatus("current")
_TmnxNatGrpSicrStatsTable_Object = MibTable
tmnxNatGrpSicrStatsTable = _TmnxNatGrpSicrStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 1, 5, 2)
)
if mibBuilder.loadTexts:
    tmnxNatGrpSicrStatsTable.setStatus("current")
_TmnxNatGrpSicrStatsEntry_Object = MibTableRow
tmnxNatGrpSicrStatsEntry = _TmnxNatGrpSicrStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 1, 5, 2, 1)
)
if mibBuilder.loadTexts:
    tmnxNatGrpSicrStatsEntry.setStatus("current")
_TmnxNatGrpSicrTx_Type = Counter64
_TmnxNatGrpSicrTx_Object = MibTableColumn
tmnxNatGrpSicrTx = _TmnxNatGrpSicrTx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 1, 5, 2, 1, 1),
    _TmnxNatGrpSicrTx_Type()
)
tmnxNatGrpSicrTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatGrpSicrTx.setStatus("current")
_TmnxNatGrpSicrTxFailures_Type = Counter64
_TmnxNatGrpSicrTxFailures_Object = MibTableColumn
tmnxNatGrpSicrTxFailures = _TmnxNatGrpSicrTxFailures_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 1, 5, 2, 1, 2),
    _TmnxNatGrpSicrTxFailures_Type()
)
tmnxNatGrpSicrTxFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatGrpSicrTxFailures.setStatus("current")
_TmnxNatGrpSicrRx_Type = Counter64
_TmnxNatGrpSicrRx_Object = MibTableColumn
tmnxNatGrpSicrRx = _TmnxNatGrpSicrRx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 1, 5, 2, 1, 3),
    _TmnxNatGrpSicrRx_Type()
)
tmnxNatGrpSicrRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatGrpSicrRx.setStatus("current")
_TmnxNatGrpSicrRxDropWrongPeer_Type = Counter64
_TmnxNatGrpSicrRxDropWrongPeer_Object = MibTableColumn
tmnxNatGrpSicrRxDropWrongPeer = _TmnxNatGrpSicrRxDropWrongPeer_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 1, 5, 2, 1, 4),
    _TmnxNatGrpSicrRxDropWrongPeer_Type()
)
tmnxNatGrpSicrRxDropWrongPeer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatGrpSicrRxDropWrongPeer.setStatus("current")
_TmnxNatGrpSicrKaTimeout_Type = Counter64
_TmnxNatGrpSicrKaTimeout_Object = MibTableColumn
tmnxNatGrpSicrKaTimeout = _TmnxNatGrpSicrKaTimeout_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 1, 5, 2, 1, 5),
    _TmnxNatGrpSicrKaTimeout_Type()
)
tmnxNatGrpSicrKaTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatGrpSicrKaTimeout.setStatus("current")
_TmnxNatPlcyObjs_ObjectIdentity = ObjectIdentity
tmnxNatPlcyObjs = _TmnxNatPlcyObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 2)
)
_TmnxNatPlcyTable_Object = MibTable
tmnxNatPlcyTable = _TmnxNatPlcyTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 2, 1)
)
if mibBuilder.loadTexts:
    tmnxNatPlcyTable.setStatus("current")
_TmnxNatPlcyEntry_Object = MibTableRow
tmnxNatPlcyEntry = _TmnxNatPlcyEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 2, 1, 1)
)
tmnxNatPlcyEntry.setIndexNames(
    (1, "TIMETRA-NAT-MIB", "tmnxNatPlcyName"),
)
if mibBuilder.loadTexts:
    tmnxNatPlcyEntry.setStatus("current")
_TmnxNatPlcyName_Type = TNamedItem
_TmnxNatPlcyName_Object = MibTableColumn
tmnxNatPlcyName = _TmnxNatPlcyName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 2, 1, 1, 1),
    _TmnxNatPlcyName_Type()
)
tmnxNatPlcyName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxNatPlcyName.setStatus("current")
_TmnxNatPlcyLastMgmtChange_Type = TimeStamp
_TmnxNatPlcyLastMgmtChange_Object = MibTableColumn
tmnxNatPlcyLastMgmtChange = _TmnxNatPlcyLastMgmtChange_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 2, 1, 1, 2),
    _TmnxNatPlcyLastMgmtChange_Type()
)
tmnxNatPlcyLastMgmtChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatPlcyLastMgmtChange.setStatus("current")
_TmnxNatPlcyRowStatus_Type = RowStatus
_TmnxNatPlcyRowStatus_Object = MibTableColumn
tmnxNatPlcyRowStatus = _TmnxNatPlcyRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 2, 1, 1, 3),
    _TmnxNatPlcyRowStatus_Type()
)
tmnxNatPlcyRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxNatPlcyRowStatus.setStatus("current")


class _TmnxNatPlcyDescription_Type(TItemDescription):
    """Custom type tmnxNatPlcyDescription based on TItemDescription"""
    defaultValue = OctetString("")


_TmnxNatPlcyDescription_Type.__name__ = "TItemDescription"
_TmnxNatPlcyDescription_Object = MibTableColumn
tmnxNatPlcyDescription = _TmnxNatPlcyDescription_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 2, 1, 1, 4),
    _TmnxNatPlcyDescription_Type()
)
tmnxNatPlcyDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxNatPlcyDescription.setStatus("current")


class _TmnxNatPlcyPool_Type(TNamedItemOrEmpty):
    """Custom type tmnxNatPlcyPool based on TNamedItemOrEmpty"""
    defaultValue = OctetString("")


_TmnxNatPlcyPool_Type.__name__ = "TNamedItemOrEmpty"
_TmnxNatPlcyPool_Object = MibTableColumn
tmnxNatPlcyPool = _TmnxNatPlcyPool_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 2, 1, 1, 5),
    _TmnxNatPlcyPool_Type()
)
tmnxNatPlcyPool.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxNatPlcyPool.setStatus("current")


class _TmnxNatPlcyPoolVRtr_Type(TmnxVRtrIDOrZero):
    """Custom type tmnxNatPlcyPoolVRtr based on TmnxVRtrIDOrZero"""
    defaultValue = 0


_TmnxNatPlcyPoolVRtr_Type.__name__ = "TmnxVRtrIDOrZero"
_TmnxNatPlcyPoolVRtr_Object = MibTableColumn
tmnxNatPlcyPoolVRtr = _TmnxNatPlcyPoolVRtr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 2, 1, 1, 6),
    _TmnxNatPlcyPoolVRtr_Type()
)
tmnxNatPlcyPoolVRtr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxNatPlcyPoolVRtr.setStatus("current")


class _TmnxNatPlcyFiltering_Type(TmnxNatFiltering):
    """Custom type tmnxNatPlcyFiltering based on TmnxNatFiltering"""
    defaultValue = 0


_TmnxNatPlcyFiltering_Type.__name__ = "TmnxNatFiltering"
_TmnxNatPlcyFiltering_Object = MibTableColumn
tmnxNatPlcyFiltering = _TmnxNatPlcyFiltering_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 2, 1, 1, 7),
    _TmnxNatPlcyFiltering_Type()
)
tmnxNatPlcyFiltering.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxNatPlcyFiltering.setStatus("current")


class _TmnxNatPlcyPortResvCount_Type(Unsigned32):
    """Custom type tmnxNatPlcyPortResvCount based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65534),
    )


_TmnxNatPlcyPortResvCount_Type.__name__ = "Unsigned32"
_TmnxNatPlcyPortResvCount_Object = MibTableColumn
tmnxNatPlcyPortResvCount = _TmnxNatPlcyPortResvCount_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 2, 1, 1, 8),
    _TmnxNatPlcyPortResvCount_Type()
)
tmnxNatPlcyPortResvCount.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxNatPlcyPortResvCount.setStatus("current")


class _TmnxNatPlcyPortWatermarkHigh_Type(TmnxNatWaterMark):
    """Custom type tmnxNatPlcyPortWatermarkHigh based on TmnxNatWaterMark"""
    defaultValue = 0

    subtypeSpec = TmnxNatWaterMark.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 100),
    )


_TmnxNatPlcyPortWatermarkHigh_Type.__name__ = "TmnxNatWaterMark"
_TmnxNatPlcyPortWatermarkHigh_Object = MibTableColumn
tmnxNatPlcyPortWatermarkHigh = _TmnxNatPlcyPortWatermarkHigh_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 2, 1, 1, 9),
    _TmnxNatPlcyPortWatermarkHigh_Type()
)
tmnxNatPlcyPortWatermarkHigh.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxNatPlcyPortWatermarkHigh.setStatus("current")


class _TmnxNatPlcyPortWatermarkLow_Type(TmnxNatWaterMark):
    """Custom type tmnxNatPlcyPortWatermarkLow based on TmnxNatWaterMark"""
    defaultValue = 0

    subtypeSpec = TmnxNatWaterMark.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 99),
    )


_TmnxNatPlcyPortWatermarkLow_Type.__name__ = "TmnxNatWaterMark"
_TmnxNatPlcyPortWatermarkLow_Object = MibTableColumn
tmnxNatPlcyPortWatermarkLow = _TmnxNatPlcyPortWatermarkLow_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 2, 1, 1, 10),
    _TmnxNatPlcyPortWatermarkLow_Type()
)
tmnxNatPlcyPortWatermarkLow.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxNatPlcyPortWatermarkLow.setStatus("current")


class _TmnxNatPlcySessionLimit_Type(Unsigned32):
    """Custom type tmnxNatPlcySessionLimit based on Unsigned32"""
    defaultValue = 65535

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_TmnxNatPlcySessionLimit_Type.__name__ = "Unsigned32"
_TmnxNatPlcySessionLimit_Object = MibTableColumn
tmnxNatPlcySessionLimit = _TmnxNatPlcySessionLimit_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 2, 1, 1, 11),
    _TmnxNatPlcySessionLimit_Type()
)
tmnxNatPlcySessionLimit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxNatPlcySessionLimit.setStatus("current")


class _TmnxNatPlcySessionResvCount_Type(Unsigned32):
    """Custom type tmnxNatPlcySessionResvCount based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65534),
    )


_TmnxNatPlcySessionResvCount_Type.__name__ = "Unsigned32"
_TmnxNatPlcySessionResvCount_Object = MibTableColumn
tmnxNatPlcySessionResvCount = _TmnxNatPlcySessionResvCount_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 2, 1, 1, 12),
    _TmnxNatPlcySessionResvCount_Type()
)
tmnxNatPlcySessionResvCount.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxNatPlcySessionResvCount.setStatus("current")


class _TmnxNatPlcySessionWatermarkHigh_Type(TmnxNatWaterMark):
    """Custom type tmnxNatPlcySessionWatermarkHigh based on TmnxNatWaterMark"""
    defaultValue = 0

    subtypeSpec = TmnxNatWaterMark.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 100),
    )


_TmnxNatPlcySessionWatermarkHigh_Type.__name__ = "TmnxNatWaterMark"
_TmnxNatPlcySessionWatermarkHigh_Object = MibTableColumn
tmnxNatPlcySessionWatermarkHigh = _TmnxNatPlcySessionWatermarkHigh_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 2, 1, 1, 13),
    _TmnxNatPlcySessionWatermarkHigh_Type()
)
tmnxNatPlcySessionWatermarkHigh.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxNatPlcySessionWatermarkHigh.setStatus("current")


class _TmnxNatPlcySessionWatermarkLow_Type(TmnxNatWaterMark):
    """Custom type tmnxNatPlcySessionWatermarkLow based on TmnxNatWaterMark"""
    defaultValue = 0

    subtypeSpec = TmnxNatWaterMark.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 99),
    )


_TmnxNatPlcySessionWatermarkLow_Type.__name__ = "TmnxNatWaterMark"
_TmnxNatPlcySessionWatermarkLow_Object = MibTableColumn
tmnxNatPlcySessionWatermarkLow = _TmnxNatPlcySessionWatermarkLow_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 2, 1, 1, 14),
    _TmnxNatPlcySessionWatermarkLow_Type()
)
tmnxNatPlcySessionWatermarkLow.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxNatPlcySessionWatermarkLow.setStatus("current")


class _TmnxNatPlcyPrioSessionFcSet_Type(TFCSet):
    """Custom type tmnxNatPlcyPrioSessionFcSet based on TFCSet"""
    defaultBinValue = "0"


_TmnxNatPlcyPrioSessionFcSet_Type.__name__ = "TFCSet"
_TmnxNatPlcyPrioSessionFcSet_Object = MibTableColumn
tmnxNatPlcyPrioSessionFcSet = _TmnxNatPlcyPrioSessionFcSet_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 2, 1, 1, 15),
    _TmnxNatPlcyPrioSessionFcSet_Type()
)
tmnxNatPlcyPrioSessionFcSet.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxNatPlcyPrioSessionFcSet.setStatus("current")


class _TmnxNatPlcyToTcpEstab_Type(Unsigned32):
    """Custom type tmnxNatPlcyToTcpEstab based on Unsigned32"""
    defaultValue = 7440

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(60, 86400),
    )


_TmnxNatPlcyToTcpEstab_Type.__name__ = "Unsigned32"
_TmnxNatPlcyToTcpEstab_Object = MibTableColumn
tmnxNatPlcyToTcpEstab = _TmnxNatPlcyToTcpEstab_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 2, 1, 1, 16),
    _TmnxNatPlcyToTcpEstab_Type()
)
tmnxNatPlcyToTcpEstab.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxNatPlcyToTcpEstab.setStatus("current")
if mibBuilder.loadTexts:
    tmnxNatPlcyToTcpEstab.setUnits("seconds")


class _TmnxNatPlcyToTcpTrans_Type(Unsigned32):
    """Custom type tmnxNatPlcyToTcpTrans based on Unsigned32"""
    defaultValue = 240

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(60, 86400),
    )


_TmnxNatPlcyToTcpTrans_Type.__name__ = "Unsigned32"
_TmnxNatPlcyToTcpTrans_Object = MibTableColumn
tmnxNatPlcyToTcpTrans = _TmnxNatPlcyToTcpTrans_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 2, 1, 1, 17),
    _TmnxNatPlcyToTcpTrans_Type()
)
tmnxNatPlcyToTcpTrans.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxNatPlcyToTcpTrans.setStatus("current")
if mibBuilder.loadTexts:
    tmnxNatPlcyToTcpTrans.setUnits("seconds")


class _TmnxNatPlcyToTcpSyn_Type(Unsigned32):
    """Custom type tmnxNatPlcyToTcpSyn based on Unsigned32"""
    defaultValue = 15

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(6, 86400),
    )


_TmnxNatPlcyToTcpSyn_Type.__name__ = "Unsigned32"
_TmnxNatPlcyToTcpSyn_Object = MibTableColumn
tmnxNatPlcyToTcpSyn = _TmnxNatPlcyToTcpSyn_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 2, 1, 1, 18),
    _TmnxNatPlcyToTcpSyn_Type()
)
tmnxNatPlcyToTcpSyn.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxNatPlcyToTcpSyn.setStatus("current")
if mibBuilder.loadTexts:
    tmnxNatPlcyToTcpSyn.setUnits("seconds")


class _TmnxNatPlcyToTcpTimeWait_Type(Unsigned32):
    """Custom type tmnxNatPlcyToTcpTimeWait based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 240),
    )


_TmnxNatPlcyToTcpTimeWait_Type.__name__ = "Unsigned32"
_TmnxNatPlcyToTcpTimeWait_Object = MibTableColumn
tmnxNatPlcyToTcpTimeWait = _TmnxNatPlcyToTcpTimeWait_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 2, 1, 1, 19),
    _TmnxNatPlcyToTcpTimeWait_Type()
)
tmnxNatPlcyToTcpTimeWait.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxNatPlcyToTcpTimeWait.setStatus("current")
if mibBuilder.loadTexts:
    tmnxNatPlcyToTcpTimeWait.setUnits("seconds")


class _TmnxNatPlcyToUdp_Type(Unsigned32):
    """Custom type tmnxNatPlcyToUdp based on Unsigned32"""
    defaultValue = 300

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(60, 86400),
    )


_TmnxNatPlcyToUdp_Type.__name__ = "Unsigned32"
_TmnxNatPlcyToUdp_Object = MibTableColumn
tmnxNatPlcyToUdp = _TmnxNatPlcyToUdp_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 2, 1, 1, 20),
    _TmnxNatPlcyToUdp_Type()
)
tmnxNatPlcyToUdp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxNatPlcyToUdp.setStatus("current")
if mibBuilder.loadTexts:
    tmnxNatPlcyToUdp.setUnits("seconds")


class _TmnxNatPlcyToUdpInitial_Type(Unsigned32):
    """Custom type tmnxNatPlcyToUdpInitial based on Unsigned32"""
    defaultValue = 15

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 300),
    )


_TmnxNatPlcyToUdpInitial_Type.__name__ = "Unsigned32"
_TmnxNatPlcyToUdpInitial_Object = MibTableColumn
tmnxNatPlcyToUdpInitial = _TmnxNatPlcyToUdpInitial_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 2, 1, 1, 21),
    _TmnxNatPlcyToUdpInitial_Type()
)
tmnxNatPlcyToUdpInitial.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxNatPlcyToUdpInitial.setStatus("current")
if mibBuilder.loadTexts:
    tmnxNatPlcyToUdpInitial.setUnits("seconds")


class _TmnxNatPlcyToUdpDns_Type(Unsigned32):
    """Custom type tmnxNatPlcyToUdpDns based on Unsigned32"""
    defaultValue = 15

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(15, 86400),
    )


_TmnxNatPlcyToUdpDns_Type.__name__ = "Unsigned32"
_TmnxNatPlcyToUdpDns_Object = MibTableColumn
tmnxNatPlcyToUdpDns = _TmnxNatPlcyToUdpDns_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 2, 1, 1, 22),
    _TmnxNatPlcyToUdpDns_Type()
)
tmnxNatPlcyToUdpDns.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxNatPlcyToUdpDns.setStatus("current")
if mibBuilder.loadTexts:
    tmnxNatPlcyToUdpDns.setUnits("seconds")


class _TmnxNatPlcyToIcmpQuery_Type(Unsigned32):
    """Custom type tmnxNatPlcyToIcmpQuery based on Unsigned32"""
    defaultValue = 60

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(60, 240),
    )


_TmnxNatPlcyToIcmpQuery_Type.__name__ = "Unsigned32"
_TmnxNatPlcyToIcmpQuery_Object = MibTableColumn
tmnxNatPlcyToIcmpQuery = _TmnxNatPlcyToIcmpQuery_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 2, 1, 1, 23),
    _TmnxNatPlcyToIcmpQuery_Type()
)
tmnxNatPlcyToIcmpQuery.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxNatPlcyToIcmpQuery.setStatus("current")
if mibBuilder.loadTexts:
    tmnxNatPlcyToIcmpQuery.setUnits("seconds")


class _TmnxNatPlcyBlkLimit_Type(Unsigned32):
    """Custom type tmnxNatPlcyBlkLimit based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 40),
    )


_TmnxNatPlcyBlkLimit_Type.__name__ = "Unsigned32"
_TmnxNatPlcyBlkLimit_Object = MibTableColumn
tmnxNatPlcyBlkLimit = _TmnxNatPlcyBlkLimit_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 2, 1, 1, 25),
    _TmnxNatPlcyBlkLimit_Type()
)
tmnxNatPlcyBlkLimit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxNatPlcyBlkLimit.setStatus("current")


class _TmnxNatPlcyToSip_Type(Unsigned32):
    """Custom type tmnxNatPlcyToSip based on Unsigned32"""
    defaultValue = 120

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 7200),
    )


_TmnxNatPlcyToSip_Type.__name__ = "Unsigned32"
_TmnxNatPlcyToSip_Object = MibTableColumn
tmnxNatPlcyToSip = _TmnxNatPlcyToSip_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 2, 1, 1, 26),
    _TmnxNatPlcyToSip_Type()
)
tmnxNatPlcyToSip.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxNatPlcyToSip.setStatus("current")
if mibBuilder.loadTexts:
    tmnxNatPlcyToSip.setUnits("seconds")


class _TmnxNatPlcyAlgEnable_Type(TmnxNatAlgProtocols):
    """Custom type tmnxNatPlcyAlgEnable based on TmnxNatAlgProtocols"""
    defaultBinValue = "1"


_TmnxNatPlcyAlgEnable_Type.__name__ = "TmnxNatAlgProtocols"
_TmnxNatPlcyAlgEnable_Object = MibTableColumn
tmnxNatPlcyAlgEnable = _TmnxNatPlcyAlgEnable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 2, 1, 1, 27),
    _TmnxNatPlcyAlgEnable_Type()
)
tmnxNatPlcyAlgEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxNatPlcyAlgEnable.setStatus("current")


class _TmnxNatPlcyPortFwdLimit_Type(Unsigned32):
    """Custom type tmnxNatPlcyPortFwdLimit based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_TmnxNatPlcyPortFwdLimit_Type.__name__ = "Unsigned32"
_TmnxNatPlcyPortFwdLimit_Object = MibTableColumn
tmnxNatPlcyPortFwdLimit = _TmnxNatPlcyPortFwdLimit_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 2, 1, 1, 28),
    _TmnxNatPlcyPortFwdLimit_Type()
)
tmnxNatPlcyPortFwdLimit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxNatPlcyPortFwdLimit.setStatus("current")


class _TmnxNatPlcyUdpInboundRefresh_Type(TruthValue):
    """Custom type tmnxNatPlcyUdpInboundRefresh based on TruthValue"""
    defaultValue = 2


_TmnxNatPlcyUdpInboundRefresh_Type.__name__ = "TruthValue"
_TmnxNatPlcyUdpInboundRefresh_Object = MibTableColumn
tmnxNatPlcyUdpInboundRefresh = _TmnxNatPlcyUdpInboundRefresh_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 2, 1, 1, 29),
    _TmnxNatPlcyUdpInboundRefresh_Type()
)
tmnxNatPlcyUdpInboundRefresh.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxNatPlcyUdpInboundRefresh.setStatus("current")


class _TmnxNatPlcyIpfixExpPlcy_Type(TNamedItemOrEmpty):
    """Custom type tmnxNatPlcyIpfixExpPlcy based on TNamedItemOrEmpty"""
    defaultValue = OctetString("")


_TmnxNatPlcyIpfixExpPlcy_Type.__name__ = "TNamedItemOrEmpty"
_TmnxNatPlcyIpfixExpPlcy_Object = MibTableColumn
tmnxNatPlcyIpfixExpPlcy = _TmnxNatPlcyIpfixExpPlcy_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 2, 1, 1, 40),
    _TmnxNatPlcyIpfixExpPlcy_Type()
)
tmnxNatPlcyIpfixExpPlcy.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxNatPlcyIpfixExpPlcy.setStatus("current")


class _TmnxNatPlcyTcpMssAdjust_Type(Unsigned32):
    """Custom type tmnxNatPlcyTcpMssAdjust based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(160, 10240),
    )


_TmnxNatPlcyTcpMssAdjust_Type.__name__ = "Unsigned32"
_TmnxNatPlcyTcpMssAdjust_Object = MibTableColumn
tmnxNatPlcyTcpMssAdjust = _TmnxNatPlcyTcpMssAdjust_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 2, 1, 1, 41),
    _TmnxNatPlcyTcpMssAdjust_Type()
)
tmnxNatPlcyTcpMssAdjust.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxNatPlcyTcpMssAdjust.setStatus("current")
if mibBuilder.loadTexts:
    tmnxNatPlcyTcpMssAdjust.setUnits("bytes")


class _TmnxNatPlcyToSubRetention_Type(Unsigned32):
    """Custom type tmnxNatPlcyToSubRetention based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1440),
    )


_TmnxNatPlcyToSubRetention_Type.__name__ = "Unsigned32"
_TmnxNatPlcyToSubRetention_Object = MibTableColumn
tmnxNatPlcyToSubRetention = _TmnxNatPlcyToSubRetention_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 2, 1, 1, 42),
    _TmnxNatPlcyToSubRetention_Type()
)
tmnxNatPlcyToSubRetention.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxNatPlcyToSubRetention.setStatus("current")
if mibBuilder.loadTexts:
    tmnxNatPlcyToSubRetention.setUnits("minutes")
_TmnxNatPlcyCreationOrigin_Type = TmnxCreateOrigin
_TmnxNatPlcyCreationOrigin_Object = MibTableColumn
tmnxNatPlcyCreationOrigin = _TmnxNatPlcyCreationOrigin_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 2, 1, 1, 43),
    _TmnxNatPlcyCreationOrigin_Type()
)
tmnxNatPlcyCreationOrigin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatPlcyCreationOrigin.setStatus("current")


class _TmnxNatPlcyDnatClassifier_Type(TNamedItemOrEmpty):
    """Custom type tmnxNatPlcyDnatClassifier based on TNamedItemOrEmpty"""
    defaultValue = OctetString("")


_TmnxNatPlcyDnatClassifier_Type.__name__ = "TNamedItemOrEmpty"
_TmnxNatPlcyDnatClassifier_Object = MibTableColumn
tmnxNatPlcyDnatClassifier = _TmnxNatPlcyDnatClassifier_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 2, 1, 1, 44),
    _TmnxNatPlcyDnatClassifier_Type()
)
tmnxNatPlcyDnatClassifier.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxNatPlcyDnatClassifier.setStatus("current")


class _TmnxNatPlcyDnatRouter_Type(TmnxVRtrIDOrZero):
    """Custom type tmnxNatPlcyDnatRouter based on TmnxVRtrIDOrZero"""
    defaultValue = 0


_TmnxNatPlcyDnatRouter_Type.__name__ = "TmnxVRtrIDOrZero"
_TmnxNatPlcyDnatRouter_Object = MibTableColumn
tmnxNatPlcyDnatRouter = _TmnxNatPlcyDnatRouter_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 2, 1, 1, 45),
    _TmnxNatPlcyDnatRouter_Type()
)
tmnxNatPlcyDnatRouter.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxNatPlcyDnatRouter.setStatus("current")


class _TmnxNatPlcyDnatIsaGrp_Type(TmnxNatIsaGrpIdOrZero):
    """Custom type tmnxNatPlcyDnatIsaGrp based on TmnxNatIsaGrpIdOrZero"""
    defaultValue = 0


_TmnxNatPlcyDnatIsaGrp_Type.__name__ = "TmnxNatIsaGrpIdOrZero"
_TmnxNatPlcyDnatIsaGrp_Object = MibTableColumn
tmnxNatPlcyDnatIsaGrp = _TmnxNatPlcyDnatIsaGrp_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 2, 1, 1, 46),
    _TmnxNatPlcyDnatIsaGrp_Type()
)
tmnxNatPlcyDnatIsaGrp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxNatPlcyDnatIsaGrp.setStatus("current")


class _TmnxNatPlcyRstUnknownTcp_Type(TruthValue):
    """Custom type tmnxNatPlcyRstUnknownTcp based on TruthValue"""
    defaultValue = 2


_TmnxNatPlcyRstUnknownTcp_Type.__name__ = "TruthValue"
_TmnxNatPlcyRstUnknownTcp_Object = MibTableColumn
tmnxNatPlcyRstUnknownTcp = _TmnxNatPlcyRstUnknownTcp_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 2, 1, 1, 47),
    _TmnxNatPlcyRstUnknownTcp_Type()
)
tmnxNatPlcyRstUnknownTcp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxNatPlcyRstUnknownTcp.setStatus("current")


class _TmnxNatPlcyToTcpRst_Type(Unsigned32):
    """Custom type tmnxNatPlcyToTcpRst based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 240),
    )


_TmnxNatPlcyToTcpRst_Type.__name__ = "Unsigned32"
_TmnxNatPlcyToTcpRst_Object = MibTableColumn
tmnxNatPlcyToTcpRst = _TmnxNatPlcyToTcpRst_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 2, 1, 1, 48),
    _TmnxNatPlcyToTcpRst_Type()
)
tmnxNatPlcyToTcpRst.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxNatPlcyToTcpRst.setStatus("current")
if mibBuilder.loadTexts:
    tmnxNatPlcyToTcpRst.setUnits("seconds")
_TmnxNatPlcyPurpose_Type = TmnxNatPolicyPurpose
_TmnxNatPlcyPurpose_Object = MibTableColumn
tmnxNatPlcyPurpose = _TmnxNatPlcyPurpose_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 2, 1, 1, 49),
    _TmnxNatPlcyPurpose_Type()
)
tmnxNatPlcyPurpose.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatPlcyPurpose.setStatus("current")


class _TmnxNatPlcyToUnknownProtocol_Type(Unsigned32):
    """Custom type tmnxNatPlcyToUnknownProtocol based on Unsigned32"""
    defaultValue = 300

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(60, 86400),
    )


_TmnxNatPlcyToUnknownProtocol_Type.__name__ = "Unsigned32"
_TmnxNatPlcyToUnknownProtocol_Object = MibTableColumn
tmnxNatPlcyToUnknownProtocol = _TmnxNatPlcyToUnknownProtocol_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 2, 1, 1, 50),
    _TmnxNatPlcyToUnknownProtocol_Type()
)
tmnxNatPlcyToUnknownProtocol.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxNatPlcyToUnknownProtocol.setStatus("current")
if mibBuilder.loadTexts:
    tmnxNatPlcyToUnknownProtocol.setUnits("seconds")


class _TmnxNatPlcyL2Outside_Type(TruthValue):
    """Custom type tmnxNatPlcyL2Outside based on TruthValue"""
    defaultValue = 2


_TmnxNatPlcyL2Outside_Type.__name__ = "TruthValue"
_TmnxNatPlcyL2Outside_Object = MibTableColumn
tmnxNatPlcyL2Outside = _TmnxNatPlcyL2Outside_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 2, 1, 1, 51),
    _TmnxNatPlcyL2Outside_Type()
)
tmnxNatPlcyL2Outside.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxNatPlcyL2Outside.setStatus("current")


class _TmnxNatPlcyPortFwdRangeEnd_Type(Unsigned32):
    """Custom type tmnxNatPlcyPortFwdRangeEnd based on Unsigned32"""
    defaultValue = 1023

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1023, 65535),
    )


_TmnxNatPlcyPortFwdRangeEnd_Type.__name__ = "Unsigned32"
_TmnxNatPlcyPortFwdRangeEnd_Object = MibTableColumn
tmnxNatPlcyPortFwdRangeEnd = _TmnxNatPlcyPortFwdRangeEnd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 2, 1, 1, 52),
    _TmnxNatPlcyPortFwdRangeEnd_Type()
)
tmnxNatPlcyPortFwdRangeEnd.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxNatPlcyPortFwdRangeEnd.setStatus("current")


class _TmnxNatPlcySyslogExpPlcy_Type(TNamedItemOrEmpty):
    """Custom type tmnxNatPlcySyslogExpPlcy based on TNamedItemOrEmpty"""
    defaultValue = OctetString("")


_TmnxNatPlcySyslogExpPlcy_Type.__name__ = "TNamedItemOrEmpty"
_TmnxNatPlcySyslogExpPlcy_Object = MibTableColumn
tmnxNatPlcySyslogExpPlcy = _TmnxNatPlcySyslogExpPlcy_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 2, 1, 1, 53),
    _TmnxNatPlcySyslogExpPlcy_Type()
)
tmnxNatPlcySyslogExpPlcy.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxNatPlcySyslogExpPlcy.setStatus("current")


class _TmnxNatPlcyDynamicPorts_Type(Unsigned32):
    """Custom type tmnxNatPlcyDynamicPorts based on Unsigned32"""
    defaultValue = 65536

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65536),
    )


_TmnxNatPlcyDynamicPorts_Type.__name__ = "Unsigned32"
_TmnxNatPlcyDynamicPorts_Object = MibTableColumn
tmnxNatPlcyDynamicPorts = _TmnxNatPlcyDynamicPorts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 2, 1, 1, 54),
    _TmnxNatPlcyDynamicPorts_Type()
)
tmnxNatPlcyDynamicPorts.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxNatPlcyDynamicPorts.setStatus("current")
_TmnxNatPlcyStatsTable_Object = MibTable
tmnxNatPlcyStatsTable = _TmnxNatPlcyStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 2, 2)
)
if mibBuilder.loadTexts:
    tmnxNatPlcyStatsTable.setStatus("current")
_TmnxNatPlcyStatsEntry_Object = MibTableRow
tmnxNatPlcyStatsEntry = _TmnxNatPlcyStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 2, 2, 1)
)
tmnxNatPlcyStatsEntry.setIndexNames(
    (0, "TIMETRA-NAT-MIB", "tmnxNatPlcyName"),
    (0, "TIMETRA-CHASSIS-MIB", "tmnxChassisIndex"),
    (0, "TIMETRA-CHASSIS-MIB", "tmnxCardSlotNum"),
    (0, "TIMETRA-CHASSIS-MIB", "tmnxMDASlotNum"),
    (0, "TIMETRA-NAT-MIB", "tmnxNatPlcyStatsType"),
)
if mibBuilder.loadTexts:
    tmnxNatPlcyStatsEntry.setStatus("current")
_TmnxNatPlcyStatsType_Type = TmnxNatUsageStatsType
_TmnxNatPlcyStatsType_Object = MibTableColumn
tmnxNatPlcyStatsType = _TmnxNatPlcyStatsType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 2, 2, 1, 1),
    _TmnxNatPlcyStatsType_Type()
)
tmnxNatPlcyStatsType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxNatPlcyStatsType.setStatus("current")


class _TmnxNatPlcyStatsName_Type(DisplayString):
    """Custom type tmnxNatPlcyStatsName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_TmnxNatPlcyStatsName_Type.__name__ = "DisplayString"
_TmnxNatPlcyStatsName_Object = MibTableColumn
tmnxNatPlcyStatsName = _TmnxNatPlcyStatsName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 2, 2, 1, 2),
    _TmnxNatPlcyStatsName_Type()
)
tmnxNatPlcyStatsName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatPlcyStatsName.setStatus("current")
_TmnxNatPlcyStatsVal_Type = Gauge32
_TmnxNatPlcyStatsVal_Object = MibTableColumn
tmnxNatPlcyStatsVal = _TmnxNatPlcyStatsVal_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 2, 2, 1, 3),
    _TmnxNatPlcyStatsVal_Type()
)
tmnxNatPlcyStatsVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatPlcyStatsVal.setStatus("current")
_TmnxNatPlcyUnknProtTable_Object = MibTable
tmnxNatPlcyUnknProtTable = _TmnxNatPlcyUnknProtTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 2, 3)
)
if mibBuilder.loadTexts:
    tmnxNatPlcyUnknProtTable.setStatus("current")
_TmnxNatPlcyUnknProtEntry_Object = MibTableRow
tmnxNatPlcyUnknProtEntry = _TmnxNatPlcyUnknProtEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 2, 3, 1)
)
tmnxNatPlcyUnknProtEntry.setIndexNames(
    (0, "TIMETRA-NAT-MIB", "tmnxNatPlcyName"),
    (0, "TIMETRA-NAT-MIB", "tmnxNatPlcyUnknProtNumber"),
)
if mibBuilder.loadTexts:
    tmnxNatPlcyUnknProtEntry.setStatus("current")


class _TmnxNatPlcyUnknProtNumber_Type(Unsigned32):
    """Custom type tmnxNatPlcyUnknProtNumber based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 256),
    )


_TmnxNatPlcyUnknProtNumber_Type.__name__ = "Unsigned32"
_TmnxNatPlcyUnknProtNumber_Object = MibTableColumn
tmnxNatPlcyUnknProtNumber = _TmnxNatPlcyUnknProtNumber_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 2, 3, 1, 1),
    _TmnxNatPlcyUnknProtNumber_Type()
)
tmnxNatPlcyUnknProtNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxNatPlcyUnknProtNumber.setStatus("current")
_TmnxNatPlcyUnknProtRowStatus_Type = RowStatus
_TmnxNatPlcyUnknProtRowStatus_Object = MibTableColumn
tmnxNatPlcyUnknProtRowStatus = _TmnxNatPlcyUnknProtRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 2, 3, 1, 2),
    _TmnxNatPlcyUnknProtRowStatus_Type()
)
tmnxNatPlcyUnknProtRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxNatPlcyUnknProtRowStatus.setStatus("current")
_TmnxNatPlcyUnknProtTimeStamp_Type = TimeStamp
_TmnxNatPlcyUnknProtTimeStamp_Object = MibTableColumn
tmnxNatPlcyUnknProtTimeStamp = _TmnxNatPlcyUnknProtTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 2, 3, 1, 3),
    _TmnxNatPlcyUnknProtTimeStamp_Type()
)
tmnxNatPlcyUnknProtTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatPlcyUnknProtTimeStamp.setStatus("current")
_TmnxNatVrtrObjs_ObjectIdentity = ObjectIdentity
tmnxNatVrtrObjs = _TmnxNatVrtrObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 3)
)
_TmnxNatVrtrTable_Object = MibTable
tmnxNatVrtrTable = _TmnxNatVrtrTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 3, 1)
)
if mibBuilder.loadTexts:
    tmnxNatVrtrTable.setStatus("current")
_TmnxNatVrtrEntry_Object = MibTableRow
tmnxNatVrtrEntry = _TmnxNatVrtrEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 3, 1, 1)
)
tmnxNatVrtrEntry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
)
if mibBuilder.loadTexts:
    tmnxNatVrtrEntry.setStatus("current")
_TmnxNatVrtrLastMgmtChange_Type = TimeStamp
_TmnxNatVrtrLastMgmtChange_Object = MibTableColumn
tmnxNatVrtrLastMgmtChange = _TmnxNatVrtrLastMgmtChange_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 3, 1, 1, 1),
    _TmnxNatVrtrLastMgmtChange_Type()
)
tmnxNatVrtrLastMgmtChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatVrtrLastMgmtChange.setStatus("current")
_TmnxNatVrtrRowStatus_Type = RowStatus
_TmnxNatVrtrRowStatus_Object = MibTableColumn
tmnxNatVrtrRowStatus = _TmnxNatVrtrRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 3, 1, 1, 2),
    _TmnxNatVrtrRowStatus_Type()
)
tmnxNatVrtrRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxNatVrtrRowStatus.setStatus("current")


class _TmnxNatVrtrInPolicy_Type(TNamedItemOrEmpty):
    """Custom type tmnxNatVrtrInPolicy based on TNamedItemOrEmpty"""
    defaultHexValue = ""


_TmnxNatVrtrInPolicy_Type.__name__ = "TNamedItemOrEmpty"
_TmnxNatVrtrInPolicy_Object = MibTableColumn
tmnxNatVrtrInPolicy = _TmnxNatVrtrInPolicy_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 3, 1, 1, 3),
    _TmnxNatVrtrInPolicy_Type()
)
tmnxNatVrtrInPolicy.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxNatVrtrInPolicy.setStatus("current")


class _TmnxNatVrtrInDsliteAdminState_Type(TmnxAdminState):
    """Custom type tmnxNatVrtrInDsliteAdminState based on TmnxAdminState"""
    defaultValue = 3


_TmnxNatVrtrInDsliteAdminState_Type.__name__ = "TmnxAdminState"
_TmnxNatVrtrInDsliteAdminState_Object = MibTableColumn
tmnxNatVrtrInDsliteAdminState = _TmnxNatVrtrInDsliteAdminState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 3, 1, 1, 4),
    _TmnxNatVrtrInDsliteAdminState_Type()
)
tmnxNatVrtrInDsliteAdminState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxNatVrtrInDsliteAdminState.setStatus("current")


class _TmnxNatVrtrInDsliteSubPrefixLen_Type(InetAddressPrefixLength):
    """Custom type tmnxNatVrtrInDsliteSubPrefixLen based on InetAddressPrefixLength"""
    defaultValue = 128

    subtypeSpec = InetAddressPrefixLength.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(32, 64),
        ValueRangeConstraint(128, 128),
    )


_TmnxNatVrtrInDsliteSubPrefixLen_Type.__name__ = "InetAddressPrefixLength"
_TmnxNatVrtrInDsliteSubPrefixLen_Object = MibTableColumn
tmnxNatVrtrInDsliteSubPrefixLen = _TmnxNatVrtrInDsliteSubPrefixLen_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 3, 1, 1, 5),
    _TmnxNatVrtrInDsliteSubPrefixLen_Type()
)
tmnxNatVrtrInDsliteSubPrefixLen.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxNatVrtrInDsliteSubPrefixLen.setStatus("current")


class _TmnxNatVrtrInRedPeerAddrType_Type(InetAddressType):
    """Custom type tmnxNatVrtrInRedPeerAddrType based on InetAddressType"""
    defaultValue = 0


_TmnxNatVrtrInRedPeerAddrType_Type.__name__ = "InetAddressType"
_TmnxNatVrtrInRedPeerAddrType_Object = MibTableColumn
tmnxNatVrtrInRedPeerAddrType = _TmnxNatVrtrInRedPeerAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 3, 1, 1, 10),
    _TmnxNatVrtrInRedPeerAddrType_Type()
)
tmnxNatVrtrInRedPeerAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxNatVrtrInRedPeerAddrType.setStatus("current")


class _TmnxNatVrtrInRedPeerAddr_Type(InetAddress):
    """Custom type tmnxNatVrtrInRedPeerAddr based on InetAddress"""
    defaultHexValue = ""

    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxNatVrtrInRedPeerAddr_Type.__name__ = "InetAddress"
_TmnxNatVrtrInRedPeerAddr_Object = MibTableColumn
tmnxNatVrtrInRedPeerAddr = _TmnxNatVrtrInRedPeerAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 3, 1, 1, 11),
    _TmnxNatVrtrInRedPeerAddr_Type()
)
tmnxNatVrtrInRedPeerAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxNatVrtrInRedPeerAddr.setStatus("current")


class _TmnxNatVrtrInRedSteerRtType_Type(InetAddressType):
    """Custom type tmnxNatVrtrInRedSteerRtType based on InetAddressType"""
    defaultValue = 0


_TmnxNatVrtrInRedSteerRtType_Type.__name__ = "InetAddressType"
_TmnxNatVrtrInRedSteerRtType_Object = MibTableColumn
tmnxNatVrtrInRedSteerRtType = _TmnxNatVrtrInRedSteerRtType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 3, 1, 1, 12),
    _TmnxNatVrtrInRedSteerRtType_Type()
)
tmnxNatVrtrInRedSteerRtType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxNatVrtrInRedSteerRtType.setStatus("current")


class _TmnxNatVrtrInRedSteerRt_Type(InetAddress):
    """Custom type tmnxNatVrtrInRedSteerRt based on InetAddress"""
    defaultHexValue = ""

    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxNatVrtrInRedSteerRt_Type.__name__ = "InetAddress"
_TmnxNatVrtrInRedSteerRt_Object = MibTableColumn
tmnxNatVrtrInRedSteerRt = _TmnxNatVrtrInRedSteerRt_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 3, 1, 1, 13),
    _TmnxNatVrtrInRedSteerRt_Type()
)
tmnxNatVrtrInRedSteerRt.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxNatVrtrInRedSteerRt.setStatus("current")


class _TmnxNatVrtrInRedSteerRtLen_Type(InetAddressPrefixLength):
    """Custom type tmnxNatVrtrInRedSteerRtLen based on InetAddressPrefixLength"""
    defaultValue = 0

    subtypeSpec = InetAddressPrefixLength.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_TmnxNatVrtrInRedSteerRtLen_Type.__name__ = "InetAddressPrefixLength"
_TmnxNatVrtrInRedSteerRtLen_Object = MibTableColumn
tmnxNatVrtrInRedSteerRtLen = _TmnxNatVrtrInRedSteerRtLen_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 3, 1, 1, 14),
    _TmnxNatVrtrInRedSteerRtLen_Type()
)
tmnxNatVrtrInRedSteerRtLen.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxNatVrtrInRedSteerRtLen.setStatus("current")


class _TmnxNatVrtrOutMtu_Type(Unsigned32):
    """Custom type tmnxNatVrtrOutMtu based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(512, 9000),
    )


_TmnxNatVrtrOutMtu_Type.__name__ = "Unsigned32"
_TmnxNatVrtrOutMtu_Object = MibTableColumn
tmnxNatVrtrOutMtu = _TmnxNatVrtrOutMtu_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 3, 1, 1, 15),
    _TmnxNatVrtrOutMtu_Type()
)
tmnxNatVrtrOutMtu.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxNatVrtrOutMtu.setStatus("current")


class _TmnxNatVrtrOutUpstreamIPFilterId_Type(TFilterID):
    """Custom type tmnxNatVrtrOutUpstreamIPFilterId based on TFilterID"""
    defaultValue = 0


_TmnxNatVrtrOutUpstreamIPFilterId_Type.__name__ = "TFilterID"
_TmnxNatVrtrOutUpstreamIPFilterId_Object = MibTableColumn
tmnxNatVrtrOutUpstreamIPFilterId = _TmnxNatVrtrOutUpstreamIPFilterId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 3, 1, 1, 16),
    _TmnxNatVrtrOutUpstreamIPFilterId_Type()
)
tmnxNatVrtrOutUpstreamIPFilterId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxNatVrtrOutUpstreamIPFilterId.setStatus("current")


class _TmnxNatVrtrInMaxDetSubscrLimit_Type(Unsigned32):
    """Custom type tmnxNatVrtrInMaxDetSubscrLimit based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 32768),
    )


_TmnxNatVrtrInMaxDetSubscrLimit_Type.__name__ = "Unsigned32"
_TmnxNatVrtrInMaxDetSubscrLimit_Object = MibTableColumn
tmnxNatVrtrInMaxDetSubscrLimit = _TmnxNatVrtrInMaxDetSubscrLimit_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 3, 1, 1, 20),
    _TmnxNatVrtrInMaxDetSubscrLimit_Type()
)
tmnxNatVrtrInMaxDetSubscrLimit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxNatVrtrInMaxDetSubscrLimit.setStatus("current")


class _TmnxNatVrtrInMaxDetSubLimitDsl_Type(Unsigned32):
    """Custom type tmnxNatVrtrInMaxDetSubLimitDsl based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 32768),
    )


_TmnxNatVrtrInMaxDetSubLimitDsl_Type.__name__ = "Unsigned32"
_TmnxNatVrtrInMaxDetSubLimitDsl_Object = MibTableColumn
tmnxNatVrtrInMaxDetSubLimitDsl = _TmnxNatVrtrInMaxDetSubLimitDsl_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 3, 1, 1, 21),
    _TmnxNatVrtrInMaxDetSubLimitDsl_Type()
)
tmnxNatVrtrInMaxDetSubLimitDsl.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxNatVrtrInMaxDetSubLimitDsl.setStatus("current")


class _TmnxNatVrtrOutDnstreamIPFilterId_Type(TFilterID):
    """Custom type tmnxNatVrtrOutDnstreamIPFilterId based on TFilterID"""
    defaultValue = 0


_TmnxNatVrtrOutDnstreamIPFilterId_Type.__name__ = "TFilterID"
_TmnxNatVrtrOutDnstreamIPFilterId_Object = MibTableColumn
tmnxNatVrtrOutDnstreamIPFilterId = _TmnxNatVrtrOutDnstreamIPFilterId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 3, 1, 1, 22),
    _TmnxNatVrtrOutDnstreamIPFilterId_Type()
)
tmnxNatVrtrOutDnstreamIPFilterId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxNatVrtrOutDnstreamIPFilterId.setStatus("current")


class _TmnxNatVrtrInRedPeer6AddrType_Type(InetAddressType):
    """Custom type tmnxNatVrtrInRedPeer6AddrType based on InetAddressType"""
    defaultValue = 0


_TmnxNatVrtrInRedPeer6AddrType_Type.__name__ = "InetAddressType"
_TmnxNatVrtrInRedPeer6AddrType_Object = MibTableColumn
tmnxNatVrtrInRedPeer6AddrType = _TmnxNatVrtrInRedPeer6AddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 3, 1, 1, 23),
    _TmnxNatVrtrInRedPeer6AddrType_Type()
)
tmnxNatVrtrInRedPeer6AddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxNatVrtrInRedPeer6AddrType.setStatus("current")


class _TmnxNatVrtrInRedPeer6Addr_Type(InetAddress):
    """Custom type tmnxNatVrtrInRedPeer6Addr based on InetAddress"""
    defaultHexValue = ""

    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxNatVrtrInRedPeer6Addr_Type.__name__ = "InetAddress"
_TmnxNatVrtrInRedPeer6Addr_Object = MibTableColumn
tmnxNatVrtrInRedPeer6Addr = _TmnxNatVrtrInRedPeer6Addr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 3, 1, 1, 24),
    _TmnxNatVrtrInRedPeer6Addr_Type()
)
tmnxNatVrtrInRedPeer6Addr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxNatVrtrInRedPeer6Addr.setStatus("current")


class _TmnxNatVrtrOutUpstrmIPv6FilterId_Type(TFilterID):
    """Custom type tmnxNatVrtrOutUpstrmIPv6FilterId based on TFilterID"""
    defaultValue = 0


_TmnxNatVrtrOutUpstrmIPv6FilterId_Type.__name__ = "TFilterID"
_TmnxNatVrtrOutUpstrmIPv6FilterId_Object = MibTableColumn
tmnxNatVrtrOutUpstrmIPv6FilterId = _TmnxNatVrtrOutUpstrmIPv6FilterId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 3, 1, 1, 25),
    _TmnxNatVrtrOutUpstrmIPv6FilterId_Type()
)
tmnxNatVrtrOutUpstrmIPv6FilterId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxNatVrtrOutUpstrmIPv6FilterId.setStatus("current")


class _TmnxNatVrtrOutDnstrmIPv6FilterId_Type(TFilterID):
    """Custom type tmnxNatVrtrOutDnstrmIPv6FilterId based on TFilterID"""
    defaultValue = 0


_TmnxNatVrtrOutDnstrmIPv6FilterId_Type.__name__ = "TFilterID"
_TmnxNatVrtrOutDnstrmIPv6FilterId_Object = MibTableColumn
tmnxNatVrtrOutDnstrmIPv6FilterId = _TmnxNatVrtrOutDnstrmIPv6FilterId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 3, 1, 1, 26),
    _TmnxNatVrtrOutDnstrmIPv6FilterId_Type()
)
tmnxNatVrtrOutDnstrmIPv6FilterId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxNatVrtrOutDnstrmIPv6FilterId.setStatus("current")


class _TmnxNatVrtrInDnstreamIPFilterId_Type(TFilterID):
    """Custom type tmnxNatVrtrInDnstreamIPFilterId based on TFilterID"""
    defaultValue = 0


_TmnxNatVrtrInDnstreamIPFilterId_Type.__name__ = "TFilterID"
_TmnxNatVrtrInDnstreamIPFilterId_Object = MibTableColumn
tmnxNatVrtrInDnstreamIPFilterId = _TmnxNatVrtrInDnstreamIPFilterId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 3, 1, 1, 27),
    _TmnxNatVrtrInDnstreamIPFilterId_Type()
)
tmnxNatVrtrInDnstreamIPFilterId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxNatVrtrInDnstreamIPFilterId.setStatus("current")


class _TmnxNatVrtrInDnatSrcPrefixList_Type(TNamedItemOrEmpty):
    """Custom type tmnxNatVrtrInDnatSrcPrefixList based on TNamedItemOrEmpty"""
    defaultHexValue = ""


_TmnxNatVrtrInDnatSrcPrefixList_Type.__name__ = "TNamedItemOrEmpty"
_TmnxNatVrtrInDnatSrcPrefixList_Object = MibTableColumn
tmnxNatVrtrInDnatSrcPrefixList = _TmnxNatVrtrInDnatSrcPrefixList_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 3, 1, 1, 28),
    _TmnxNatVrtrInDnatSrcPrefixList_Type()
)
tmnxNatVrtrInDnatSrcPrefixList.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxNatVrtrInDnatSrcPrefixList.setStatus("current")


class _TmnxNatVrtrOutDnatOnlyRouteLimit_Type(Unsigned32):
    """Custom type tmnxNatVrtrOutDnatOnlyRouteLimit based on Unsigned32"""
    defaultValue = 32768

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 131072),
    )


_TmnxNatVrtrOutDnatOnlyRouteLimit_Type.__name__ = "Unsigned32"
_TmnxNatVrtrOutDnatOnlyRouteLimit_Object = MibTableColumn
tmnxNatVrtrOutDnatOnlyRouteLimit = _TmnxNatVrtrOutDnatOnlyRouteLimit_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 3, 1, 1, 29),
    _TmnxNatVrtrOutDnatOnlyRouteLimit_Type()
)
tmnxNatVrtrOutDnatOnlyRouteLimit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxNatVrtrOutDnatOnlyRouteLimit.setStatus("current")
_TmnxNatVrtrOutDnatOnlyRoutes_Type = Gauge32
_TmnxNatVrtrOutDnatOnlyRoutes_Object = MibTableColumn
tmnxNatVrtrOutDnatOnlyRoutes = _TmnxNatVrtrOutDnatOnlyRoutes_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 3, 1, 1, 30),
    _TmnxNatVrtrOutDnatOnlyRoutes_Type()
)
tmnxNatVrtrOutDnatOnlyRoutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatVrtrOutDnatOnlyRoutes.setStatus("current")


class _TmnxNatVrtrInImportPolicy1_Type(TLNamedItemOrEmpty):
    """Custom type tmnxNatVrtrInImportPolicy1 based on TLNamedItemOrEmpty"""
    defaultHexValue = ""


_TmnxNatVrtrInImportPolicy1_Type.__name__ = "TLNamedItemOrEmpty"
_TmnxNatVrtrInImportPolicy1_Object = MibTableColumn
tmnxNatVrtrInImportPolicy1 = _TmnxNatVrtrInImportPolicy1_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 3, 1, 1, 31),
    _TmnxNatVrtrInImportPolicy1_Type()
)
tmnxNatVrtrInImportPolicy1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxNatVrtrInImportPolicy1.setStatus("current")


class _TmnxNatVrtrInImportPolicy2_Type(TLNamedItemOrEmpty):
    """Custom type tmnxNatVrtrInImportPolicy2 based on TLNamedItemOrEmpty"""
    defaultHexValue = ""


_TmnxNatVrtrInImportPolicy2_Type.__name__ = "TLNamedItemOrEmpty"
_TmnxNatVrtrInImportPolicy2_Object = MibTableColumn
tmnxNatVrtrInImportPolicy2 = _TmnxNatVrtrInImportPolicy2_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 3, 1, 1, 32),
    _TmnxNatVrtrInImportPolicy2_Type()
)
tmnxNatVrtrInImportPolicy2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxNatVrtrInImportPolicy2.setStatus("current")


class _TmnxNatVrtrInImportPolicy3_Type(TLNamedItemOrEmpty):
    """Custom type tmnxNatVrtrInImportPolicy3 based on TLNamedItemOrEmpty"""
    defaultHexValue = ""


_TmnxNatVrtrInImportPolicy3_Type.__name__ = "TLNamedItemOrEmpty"
_TmnxNatVrtrInImportPolicy3_Object = MibTableColumn
tmnxNatVrtrInImportPolicy3 = _TmnxNatVrtrInImportPolicy3_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 3, 1, 1, 33),
    _TmnxNatVrtrInImportPolicy3_Type()
)
tmnxNatVrtrInImportPolicy3.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxNatVrtrInImportPolicy3.setStatus("current")


class _TmnxNatVrtrInImportPolicy4_Type(TLNamedItemOrEmpty):
    """Custom type tmnxNatVrtrInImportPolicy4 based on TLNamedItemOrEmpty"""
    defaultHexValue = ""


_TmnxNatVrtrInImportPolicy4_Type.__name__ = "TLNamedItemOrEmpty"
_TmnxNatVrtrInImportPolicy4_Object = MibTableColumn
tmnxNatVrtrInImportPolicy4 = _TmnxNatVrtrInImportPolicy4_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 3, 1, 1, 34),
    _TmnxNatVrtrInImportPolicy4_Type()
)
tmnxNatVrtrInImportPolicy4.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxNatVrtrInImportPolicy4.setStatus("current")


class _TmnxNatVrtrInImportPolicy5_Type(TLNamedItemOrEmpty):
    """Custom type tmnxNatVrtrInImportPolicy5 based on TLNamedItemOrEmpty"""
    defaultHexValue = ""


_TmnxNatVrtrInImportPolicy5_Type.__name__ = "TLNamedItemOrEmpty"
_TmnxNatVrtrInImportPolicy5_Object = MibTableColumn
tmnxNatVrtrInImportPolicy5 = _TmnxNatVrtrInImportPolicy5_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 3, 1, 1, 35),
    _TmnxNatVrtrInImportPolicy5_Type()
)
tmnxNatVrtrInImportPolicy5.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxNatVrtrInImportPolicy5.setStatus("current")


class _TmnxNatVrtrSourcePrefixOnly_Type(TruthValue):
    """Custom type tmnxNatVrtrSourcePrefixOnly based on TruthValue"""
    defaultValue = 2


_TmnxNatVrtrSourcePrefixOnly_Type.__name__ = "TruthValue"
_TmnxNatVrtrSourcePrefixOnly_Object = MibTableColumn
tmnxNatVrtrSourcePrefixOnly = _TmnxNatVrtrSourcePrefixOnly_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 3, 1, 1, 36),
    _TmnxNatVrtrSourcePrefixOnly_Type()
)
tmnxNatVrtrSourcePrefixOnly.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxNatVrtrSourcePrefixOnly.setStatus("current")


class _TmnxNatVrtrInL2AwForceUniqueIp_Type(TruthValue):
    """Custom type tmnxNatVrtrInL2AwForceUniqueIp based on TruthValue"""
    defaultValue = 2


_TmnxNatVrtrInL2AwForceUniqueIp_Type.__name__ = "TruthValue"
_TmnxNatVrtrInL2AwForceUniqueIp_Object = MibTableColumn
tmnxNatVrtrInL2AwForceUniqueIp = _TmnxNatVrtrInL2AwForceUniqueIp_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 3, 1, 1, 37),
    _TmnxNatVrtrInL2AwForceUniqueIp_Type()
)
tmnxNatVrtrInL2AwForceUniqueIp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxNatVrtrInL2AwForceUniqueIp.setStatus("current")
_TmnxNatL2AwAddrTable_Object = MibTable
tmnxNatL2AwAddrTable = _TmnxNatL2AwAddrTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 3, 2)
)
if mibBuilder.loadTexts:
    tmnxNatL2AwAddrTable.setStatus("current")
_TmnxNatL2AwAddrEntry_Object = MibTableRow
tmnxNatL2AwAddrEntry = _TmnxNatL2AwAddrEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 3, 2, 1)
)
tmnxNatL2AwAddrEntry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "TIMETRA-NAT-MIB", "tmnxNatL2AwAddrType"),
    (0, "TIMETRA-NAT-MIB", "tmnxNatL2AwAddr"),
    (0, "TIMETRA-NAT-MIB", "tmnxNatL2AwAddrPrefixLen"),
)
if mibBuilder.loadTexts:
    tmnxNatL2AwAddrEntry.setStatus("current")
_TmnxNatL2AwAddrType_Type = InetAddressType
_TmnxNatL2AwAddrType_Object = MibTableColumn
tmnxNatL2AwAddrType = _TmnxNatL2AwAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 3, 2, 1, 1),
    _TmnxNatL2AwAddrType_Type()
)
tmnxNatL2AwAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxNatL2AwAddrType.setStatus("current")


class _TmnxNatL2AwAddr_Type(InetAddress):
    """Custom type tmnxNatL2AwAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxNatL2AwAddr_Type.__name__ = "InetAddress"
_TmnxNatL2AwAddr_Object = MibTableColumn
tmnxNatL2AwAddr = _TmnxNatL2AwAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 3, 2, 1, 2),
    _TmnxNatL2AwAddr_Type()
)
tmnxNatL2AwAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxNatL2AwAddr.setStatus("current")


class _TmnxNatL2AwAddrPrefixLen_Type(InetAddressPrefixLength):
    """Custom type tmnxNatL2AwAddrPrefixLen based on InetAddressPrefixLength"""
    subtypeSpec = InetAddressPrefixLength.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32),
    )


_TmnxNatL2AwAddrPrefixLen_Type.__name__ = "InetAddressPrefixLength"
_TmnxNatL2AwAddrPrefixLen_Object = MibTableColumn
tmnxNatL2AwAddrPrefixLen = _TmnxNatL2AwAddrPrefixLen_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 3, 2, 1, 3),
    _TmnxNatL2AwAddrPrefixLen_Type()
)
tmnxNatL2AwAddrPrefixLen.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxNatL2AwAddrPrefixLen.setStatus("current")
_TmnxNatL2AwAddrRowStatus_Type = RowStatus
_TmnxNatL2AwAddrRowStatus_Object = MibTableColumn
tmnxNatL2AwAddrRowStatus = _TmnxNatL2AwAddrRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 3, 2, 1, 4),
    _TmnxNatL2AwAddrRowStatus_Type()
)
tmnxNatL2AwAddrRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxNatL2AwAddrRowStatus.setStatus("current")
_TmnxNatL2AwAddrLastMgmtChange_Type = TimeStamp
_TmnxNatL2AwAddrLastMgmtChange_Object = MibTableColumn
tmnxNatL2AwAddrLastMgmtChange = _TmnxNatL2AwAddrLastMgmtChange_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 3, 2, 1, 5),
    _TmnxNatL2AwAddrLastMgmtChange_Type()
)
tmnxNatL2AwAddrLastMgmtChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatL2AwAddrLastMgmtChange.setStatus("current")
_TmnxNat64Table_Object = MibTable
tmnxNat64Table = _TmnxNat64Table_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 3, 3)
)
if mibBuilder.loadTexts:
    tmnxNat64Table.setStatus("current")
_TmnxNat64Entry_Object = MibTableRow
tmnxNat64Entry = _TmnxNat64Entry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 3, 3, 1)
)
tmnxNat64Entry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
)
if mibBuilder.loadTexts:
    tmnxNat64Entry.setStatus("current")
_TmnxNat64LastMgmtChange_Type = TimeStamp
_TmnxNat64LastMgmtChange_Object = MibTableColumn
tmnxNat64LastMgmtChange = _TmnxNat64LastMgmtChange_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 3, 3, 1, 1),
    _TmnxNat64LastMgmtChange_Type()
)
tmnxNat64LastMgmtChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNat64LastMgmtChange.setStatus("current")
_TmnxNat64RowStatus_Type = RowStatus
_TmnxNat64RowStatus_Object = MibTableColumn
tmnxNat64RowStatus = _TmnxNat64RowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 3, 3, 1, 2),
    _TmnxNat64RowStatus_Type()
)
tmnxNat64RowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxNat64RowStatus.setStatus("current")


class _TmnxNat64InAdminState_Type(TmnxAdminState):
    """Custom type tmnxNat64InAdminState based on TmnxAdminState"""
    defaultValue = 3


_TmnxNat64InAdminState_Type.__name__ = "TmnxAdminState"
_TmnxNat64InAdminState_Object = MibTableColumn
tmnxNat64InAdminState = _TmnxNat64InAdminState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 3, 3, 1, 3),
    _TmnxNat64InAdminState_Type()
)
tmnxNat64InAdminState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxNat64InAdminState.setStatus("current")


class _TmnxNat64InSubPrefixLen_Type(InetAddressPrefixLength):
    """Custom type tmnxNat64InSubPrefixLen based on InetAddressPrefixLength"""
    defaultValue = 128

    subtypeSpec = InetAddressPrefixLength.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(32, 64),
        ValueRangeConstraint(128, 128),
    )


_TmnxNat64InSubPrefixLen_Type.__name__ = "InetAddressPrefixLength"
_TmnxNat64InSubPrefixLen_Object = MibTableColumn
tmnxNat64InSubPrefixLen = _TmnxNat64InSubPrefixLen_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 3, 3, 1, 4),
    _TmnxNat64InSubPrefixLen_Type()
)
tmnxNat64InSubPrefixLen.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxNat64InSubPrefixLen.setStatus("current")


class _TmnxNat64InPrefix_Type(InetAddressIPv6):
    """Custom type tmnxNat64InPrefix based on InetAddressIPv6"""
    defaultHexValue = "0064ff9b000000000000000000000000"


_TmnxNat64InPrefix_Type.__name__ = "InetAddressIPv6"
_TmnxNat64InPrefix_Object = MibTableColumn
tmnxNat64InPrefix = _TmnxNat64InPrefix_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 3, 3, 1, 5),
    _TmnxNat64InPrefix_Type()
)
tmnxNat64InPrefix.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxNat64InPrefix.setStatus("current")


class _TmnxNat64InPrefixLen_Type(InetAddressPrefixLength):
    """Custom type tmnxNat64InPrefixLen based on InetAddressPrefixLength"""
    defaultValue = 96

    subtypeSpec = InetAddressPrefixLength.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(32, 32),
        ValueRangeConstraint(40, 40),
        ValueRangeConstraint(48, 48),
        ValueRangeConstraint(56, 56),
        ValueRangeConstraint(64, 64),
        ValueRangeConstraint(96, 96),
    )


_TmnxNat64InPrefixLen_Type.__name__ = "InetAddressPrefixLength"
_TmnxNat64InPrefixLen_Object = MibTableColumn
tmnxNat64InPrefixLen = _TmnxNat64InPrefixLen_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 3, 3, 1, 6),
    _TmnxNat64InPrefixLen_Type()
)
tmnxNat64InPrefixLen.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxNat64InPrefixLen.setStatus("current")


class _TmnxNat64InIpv6Mtu_Type(Unsigned32):
    """Custom type tmnxNat64InIpv6Mtu based on Unsigned32"""
    defaultValue = 1520

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1280, 9212),
    )


_TmnxNat64InIpv6Mtu_Type.__name__ = "Unsigned32"
_TmnxNat64InIpv6Mtu_Object = MibTableColumn
tmnxNat64InIpv6Mtu = _TmnxNat64InIpv6Mtu_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 3, 3, 1, 7),
    _TmnxNat64InIpv6Mtu_Type()
)
tmnxNat64InIpv6Mtu.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxNat64InIpv6Mtu.setStatus("current")


class _TmnxNat64InDropZeroIpv4Checksum_Type(TruthValue):
    """Custom type tmnxNat64InDropZeroIpv4Checksum based on TruthValue"""
    defaultValue = 2


_TmnxNat64InDropZeroIpv4Checksum_Type.__name__ = "TruthValue"
_TmnxNat64InDropZeroIpv4Checksum_Object = MibTableColumn
tmnxNat64InDropZeroIpv4Checksum = _TmnxNat64InDropZeroIpv4Checksum_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 3, 3, 1, 8),
    _TmnxNat64InDropZeroIpv4Checksum_Type()
)
tmnxNat64InDropZeroIpv4Checksum.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxNat64InDropZeroIpv4Checksum.setStatus("current")


class _TmnxNat64InSetTos_Type(TruthValue):
    """Custom type tmnxNat64InSetTos based on TruthValue"""
    defaultValue = 2


_TmnxNat64InSetTos_Type.__name__ = "TruthValue"
_TmnxNat64InSetTos_Object = MibTableColumn
tmnxNat64InSetTos = _TmnxNat64InSetTos_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 3, 3, 1, 9),
    _TmnxNat64InSetTos_Type()
)
tmnxNat64InSetTos.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxNat64InSetTos.setStatus("current")


class _TmnxNat64InTos_Type(Unsigned32):
    """Custom type tmnxNat64InTos based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_TmnxNat64InTos_Type.__name__ = "Unsigned32"
_TmnxNat64InTos_Object = MibTableColumn
tmnxNat64InTos = _TmnxNat64InTos_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 3, 3, 1, 10),
    _TmnxNat64InTos_Type()
)
tmnxNat64InTos.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxNat64InTos.setStatus("current")


class _TmnxNat64InIgnoreTos_Type(TruthValue):
    """Custom type tmnxNat64InIgnoreTos based on TruthValue"""
    defaultValue = 2


_TmnxNat64InIgnoreTos_Type.__name__ = "TruthValue"
_TmnxNat64InIgnoreTos_Object = MibTableColumn
tmnxNat64InIgnoreTos = _TmnxNat64InIgnoreTos_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 3, 3, 1, 11),
    _TmnxNat64InIgnoreTos_Type()
)
tmnxNat64InIgnoreTos.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxNat64InIgnoreTos.setStatus("current")


class _TmnxNat64InInsertIpv6FragHeader_Type(TruthValue):
    """Custom type tmnxNat64InInsertIpv6FragHeader based on TruthValue"""
    defaultValue = 2


_TmnxNat64InInsertIpv6FragHeader_Type.__name__ = "TruthValue"
_TmnxNat64InInsertIpv6FragHeader_Object = MibTableColumn
tmnxNat64InInsertIpv6FragHeader = _TmnxNat64InInsertIpv6FragHeader_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 3, 3, 1, 12),
    _TmnxNat64InInsertIpv6FragHeader_Type()
)
tmnxNat64InInsertIpv6FragHeader.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxNat64InInsertIpv6FragHeader.setStatus("current")


class _TmnxNat64InFragmentIp_Type(TmnxNatFragmentIpMode):
    """Custom type tmnxNat64InFragmentIp based on TmnxNatFragmentIpMode"""
    defaultValue = 0


_TmnxNat64InFragmentIp_Type.__name__ = "TmnxNatFragmentIpMode"
_TmnxNat64InFragmentIp_Object = MibTableColumn
tmnxNat64InFragmentIp = _TmnxNat64InFragmentIp_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 3, 3, 1, 15),
    _TmnxNat64InFragmentIp_Type()
)
tmnxNat64InFragmentIp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxNat64InFragmentIp.setStatus("current")
_TmnxNatSubIdTable_Object = MibTable
tmnxNatSubIdTable = _TmnxNatSubIdTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 3, 4)
)
if mibBuilder.loadTexts:
    tmnxNatSubIdTable.setStatus("current")
_TmnxNatSubIdEntry_Object = MibTableRow
tmnxNatSubIdEntry = _TmnxNatSubIdEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 3, 4, 1)
)
if mibBuilder.loadTexts:
    tmnxNatSubIdEntry.setStatus("current")
_TmnxNatSubIdLastMgmtChange_Type = TimeStamp
_TmnxNatSubIdLastMgmtChange_Object = MibTableColumn
tmnxNatSubIdLastMgmtChange = _TmnxNatSubIdLastMgmtChange_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 3, 4, 1, 1),
    _TmnxNatSubIdLastMgmtChange_Type()
)
tmnxNatSubIdLastMgmtChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatSubIdLastMgmtChange.setStatus("current")


class _TmnxNatSubIdDescription_Type(TItemDescription):
    """Custom type tmnxNatSubIdDescription based on TItemDescription"""
    defaultValue = OctetString("")


_TmnxNatSubIdDescription_Type.__name__ = "TItemDescription"
_TmnxNatSubIdDescription_Object = MibTableColumn
tmnxNatSubIdDescription = _TmnxNatSubIdDescription_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 3, 4, 1, 2),
    _TmnxNatSubIdDescription_Type()
)
tmnxNatSubIdDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxNatSubIdDescription.setStatus("current")


class _TmnxNatSubIdAdminState_Type(TmnxAdminState):
    """Custom type tmnxNatSubIdAdminState based on TmnxAdminState"""
    defaultValue = 3


_TmnxNatSubIdAdminState_Type.__name__ = "TmnxAdminState"
_TmnxNatSubIdAdminState_Object = MibTableColumn
tmnxNatSubIdAdminState = _TmnxNatSubIdAdminState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 3, 4, 1, 3),
    _TmnxNatSubIdAdminState_Type()
)
tmnxNatSubIdAdminState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxNatSubIdAdminState.setStatus("current")


class _TmnxNatSubIdRadProxSrvRouter_Type(TmnxVRtrIDOrZero):
    """Custom type tmnxNatSubIdRadProxSrvRouter based on TmnxVRtrIDOrZero"""
    defaultValue = 0


_TmnxNatSubIdRadProxSrvRouter_Type.__name__ = "TmnxVRtrIDOrZero"
_TmnxNatSubIdRadProxSrvRouter_Object = MibTableColumn
tmnxNatSubIdRadProxSrvRouter = _TmnxNatSubIdRadProxSrvRouter_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 3, 4, 1, 4),
    _TmnxNatSubIdRadProxSrvRouter_Type()
)
tmnxNatSubIdRadProxSrvRouter.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxNatSubIdRadProxSrvRouter.setStatus("current")


class _TmnxNatSubIdRadProxSrvName_Type(TNamedItemOrEmpty):
    """Custom type tmnxNatSubIdRadProxSrvName based on TNamedItemOrEmpty"""
    defaultValue = OctetString("")


_TmnxNatSubIdRadProxSrvName_Type.__name__ = "TNamedItemOrEmpty"
_TmnxNatSubIdRadProxSrvName_Object = MibTableColumn
tmnxNatSubIdRadProxSrvName = _TmnxNatSubIdRadProxSrvName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 3, 4, 1, 5),
    _TmnxNatSubIdRadProxSrvName_Type()
)
tmnxNatSubIdRadProxSrvName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxNatSubIdRadProxSrvName.setStatus("current")


class _TmnxNatSubIdRadiusAttributeType_Type(TmnxSubRadiusAttrType):
    """Custom type tmnxNatSubIdRadiusAttributeType based on TmnxSubRadiusAttrType"""
    defaultValue = 11


_TmnxNatSubIdRadiusAttributeType_Type.__name__ = "TmnxSubRadiusAttrType"
_TmnxNatSubIdRadiusAttributeType_Object = MibTableColumn
tmnxNatSubIdRadiusAttributeType = _TmnxNatSubIdRadiusAttributeType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 3, 4, 1, 6),
    _TmnxNatSubIdRadiusAttributeType_Type()
)
tmnxNatSubIdRadiusAttributeType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxNatSubIdRadiusAttributeType.setStatus("current")


class _TmnxNatSubIdRadiusVendorId_Type(TmnxSubRadiusVendorId):
    """Custom type tmnxNatSubIdRadiusVendorId based on TmnxSubRadiusVendorId"""
    defaultValue = 6527


_TmnxNatSubIdRadiusVendorId_Type.__name__ = "TmnxSubRadiusVendorId"
_TmnxNatSubIdRadiusVendorId_Object = MibTableColumn
tmnxNatSubIdRadiusVendorId = _TmnxNatSubIdRadiusVendorId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 3, 4, 1, 7),
    _TmnxNatSubIdRadiusVendorId_Type()
)
tmnxNatSubIdRadiusVendorId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxNatSubIdRadiusVendorId.setStatus("current")


class _TmnxNatSubIdDropUnidentified_Type(TruthValue):
    """Custom type tmnxNatSubIdDropUnidentified based on TruthValue"""
    defaultValue = 2


_TmnxNatSubIdDropUnidentified_Type.__name__ = "TruthValue"
_TmnxNatSubIdDropUnidentified_Object = MibTableColumn
tmnxNatSubIdDropUnidentified = _TmnxNatSubIdDropUnidentified_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 3, 4, 1, 8),
    _TmnxNatSubIdDropUnidentified_Type()
)
tmnxNatSubIdDropUnidentified.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxNatSubIdDropUnidentified.setStatus("current")
_TmnxNatDetPlcyTable_Object = MibTable
tmnxNatDetPlcyTable = _TmnxNatDetPlcyTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 3, 5)
)
if mibBuilder.loadTexts:
    tmnxNatDetPlcyTable.setStatus("obsolete")
_TmnxNatDetPlcyEntry_Object = MibTableRow
tmnxNatDetPlcyEntry = _TmnxNatDetPlcyEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 3, 5, 1)
)
tmnxNatDetPlcyEntry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "TIMETRA-NAT-MIB", "tmnxNatDetPlcySubType"),
    (0, "TIMETRA-NAT-MIB", "tmnxNatDetPlcyAddrType"),
    (0, "TIMETRA-NAT-MIB", "tmnxNatDetPlcyAddr"),
    (0, "TIMETRA-NAT-MIB", "tmnxNatDetPlcyAddrPrefixLength"),
)
if mibBuilder.loadTexts:
    tmnxNatDetPlcyEntry.setStatus("current")
_TmnxNatDetPlcySubType_Type = TmnxNatLegacySubscriberType
_TmnxNatDetPlcySubType_Object = MibTableColumn
tmnxNatDetPlcySubType = _TmnxNatDetPlcySubType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 3, 5, 1, 1),
    _TmnxNatDetPlcySubType_Type()
)
tmnxNatDetPlcySubType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxNatDetPlcySubType.setStatus("current")
_TmnxNatDetPlcyAddrType_Type = InetAddressType
_TmnxNatDetPlcyAddrType_Object = MibTableColumn
tmnxNatDetPlcyAddrType = _TmnxNatDetPlcyAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 3, 5, 1, 2),
    _TmnxNatDetPlcyAddrType_Type()
)
tmnxNatDetPlcyAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxNatDetPlcyAddrType.setStatus("current")


class _TmnxNatDetPlcyAddr_Type(InetAddress):
    """Custom type tmnxNatDetPlcyAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxNatDetPlcyAddr_Type.__name__ = "InetAddress"
_TmnxNatDetPlcyAddr_Object = MibTableColumn
tmnxNatDetPlcyAddr = _TmnxNatDetPlcyAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 3, 5, 1, 3),
    _TmnxNatDetPlcyAddr_Type()
)
tmnxNatDetPlcyAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxNatDetPlcyAddr.setStatus("current")


class _TmnxNatDetPlcyAddrPrefixLength_Type(InetAddressPrefixLength):
    """Custom type tmnxNatDetPlcyAddrPrefixLength based on InetAddressPrefixLength"""
    subtypeSpec = InetAddressPrefixLength.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 128),
    )


_TmnxNatDetPlcyAddrPrefixLength_Type.__name__ = "InetAddressPrefixLength"
_TmnxNatDetPlcyAddrPrefixLength_Object = MibTableColumn
tmnxNatDetPlcyAddrPrefixLength = _TmnxNatDetPlcyAddrPrefixLength_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 3, 5, 1, 4),
    _TmnxNatDetPlcyAddrPrefixLength_Type()
)
tmnxNatDetPlcyAddrPrefixLength.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxNatDetPlcyAddrPrefixLength.setStatus("current")
_TmnxNatDetPlcyRowStatus_Type = RowStatus
_TmnxNatDetPlcyRowStatus_Object = MibTableColumn
tmnxNatDetPlcyRowStatus = _TmnxNatDetPlcyRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 3, 5, 1, 5),
    _TmnxNatDetPlcyRowStatus_Type()
)
tmnxNatDetPlcyRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxNatDetPlcyRowStatus.setStatus("obsolete")
_TmnxNatDetPlcyLastMgmtChange_Type = TimeStamp
_TmnxNatDetPlcyLastMgmtChange_Object = MibTableColumn
tmnxNatDetPlcyLastMgmtChange = _TmnxNatDetPlcyLastMgmtChange_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 3, 5, 1, 6),
    _TmnxNatDetPlcyLastMgmtChange_Type()
)
tmnxNatDetPlcyLastMgmtChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatDetPlcyLastMgmtChange.setStatus("obsolete")
_TmnxNatDetPlcyName_Type = TNamedItem
_TmnxNatDetPlcyName_Object = MibTableColumn
tmnxNatDetPlcyName = _TmnxNatDetPlcyName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 3, 5, 1, 7),
    _TmnxNatDetPlcyName_Type()
)
tmnxNatDetPlcyName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxNatDetPlcyName.setStatus("obsolete")


class _TmnxNatDetPlcyAdminState_Type(TmnxAdminState):
    """Custom type tmnxNatDetPlcyAdminState based on TmnxAdminState"""
    defaultValue = 3


_TmnxNatDetPlcyAdminState_Type.__name__ = "TmnxAdminState"
_TmnxNatDetPlcyAdminState_Object = MibTableColumn
tmnxNatDetPlcyAdminState = _TmnxNatDetPlcyAdminState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 3, 5, 1, 8),
    _TmnxNatDetPlcyAdminState_Type()
)
tmnxNatDetPlcyAdminState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxNatDetPlcyAdminState.setStatus("obsolete")
_TmnxNatDetPlcyOperState_Type = ServiceOperStatus
_TmnxNatDetPlcyOperState_Object = MibTableColumn
tmnxNatDetPlcyOperState = _TmnxNatDetPlcyOperState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 3, 5, 1, 9),
    _TmnxNatDetPlcyOperState_Type()
)
tmnxNatDetPlcyOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatDetPlcyOperState.setStatus("obsolete")
_TmnxNatDetMapTable_Object = MibTable
tmnxNatDetMapTable = _TmnxNatDetMapTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 3, 6)
)
if mibBuilder.loadTexts:
    tmnxNatDetMapTable.setStatus("obsolete")
_TmnxNatDetMapEntry_Object = MibTableRow
tmnxNatDetMapEntry = _TmnxNatDetMapEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 3, 6, 1)
)
tmnxNatDetMapEntry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "TIMETRA-NAT-MIB", "tmnxNatDetPlcySubType"),
    (0, "TIMETRA-NAT-MIB", "tmnxNatDetPlcyAddrType"),
    (0, "TIMETRA-NAT-MIB", "tmnxNatDetPlcyAddr"),
    (0, "TIMETRA-NAT-MIB", "tmnxNatDetPlcyAddrPrefixLength"),
    (0, "TIMETRA-NAT-MIB", "tmnxNatDetMapInAddrType"),
    (0, "TIMETRA-NAT-MIB", "tmnxNatDetMapInStart"),
    (0, "TIMETRA-NAT-MIB", "tmnxNatDetMapInEnd"),
)
if mibBuilder.loadTexts:
    tmnxNatDetMapEntry.setStatus("current")
_TmnxNatDetMapInAddrType_Type = InetAddressType
_TmnxNatDetMapInAddrType_Object = MibTableColumn
tmnxNatDetMapInAddrType = _TmnxNatDetMapInAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 3, 6, 1, 1),
    _TmnxNatDetMapInAddrType_Type()
)
tmnxNatDetMapInAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxNatDetMapInAddrType.setStatus("current")


class _TmnxNatDetMapInStart_Type(InetAddress):
    """Custom type tmnxNatDetMapInStart based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxNatDetMapInStart_Type.__name__ = "InetAddress"
_TmnxNatDetMapInStart_Object = MibTableColumn
tmnxNatDetMapInStart = _TmnxNatDetMapInStart_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 3, 6, 1, 2),
    _TmnxNatDetMapInStart_Type()
)
tmnxNatDetMapInStart.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxNatDetMapInStart.setStatus("current")


class _TmnxNatDetMapInEnd_Type(InetAddress):
    """Custom type tmnxNatDetMapInEnd based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxNatDetMapInEnd_Type.__name__ = "InetAddress"
_TmnxNatDetMapInEnd_Object = MibTableColumn
tmnxNatDetMapInEnd = _TmnxNatDetMapInEnd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 3, 6, 1, 3),
    _TmnxNatDetMapInEnd_Type()
)
tmnxNatDetMapInEnd.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxNatDetMapInEnd.setStatus("current")
_TmnxNatDetMapRowStatus_Type = RowStatus
_TmnxNatDetMapRowStatus_Object = MibTableColumn
tmnxNatDetMapRowStatus = _TmnxNatDetMapRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 3, 6, 1, 4),
    _TmnxNatDetMapRowStatus_Type()
)
tmnxNatDetMapRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxNatDetMapRowStatus.setStatus("obsolete")
_TmnxNatDetMapLastCh_Type = TimeStamp
_TmnxNatDetMapLastCh_Object = MibTableColumn
tmnxNatDetMapLastCh = _TmnxNatDetMapLastCh_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 3, 6, 1, 5),
    _TmnxNatDetMapLastCh_Type()
)
tmnxNatDetMapLastCh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatDetMapLastCh.setStatus("obsolete")
_TmnxNatDetMapOutAddrType_Type = InetAddressType
_TmnxNatDetMapOutAddrType_Object = MibTableColumn
tmnxNatDetMapOutAddrType = _TmnxNatDetMapOutAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 3, 6, 1, 6),
    _TmnxNatDetMapOutAddrType_Type()
)
tmnxNatDetMapOutAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxNatDetMapOutAddrType.setStatus("obsolete")


class _TmnxNatDetMapOutStart_Type(InetAddress):
    """Custom type tmnxNatDetMapOutStart based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxNatDetMapOutStart_Type.__name__ = "InetAddress"
_TmnxNatDetMapOutStart_Object = MibTableColumn
tmnxNatDetMapOutStart = _TmnxNatDetMapOutStart_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 3, 6, 1, 7),
    _TmnxNatDetMapOutStart_Type()
)
tmnxNatDetMapOutStart.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxNatDetMapOutStart.setStatus("obsolete")
_TmnxNatDetMapOperState_Type = ServiceOperStatus
_TmnxNatDetMapOperState_Object = MibTableColumn
tmnxNatDetMapOperState = _TmnxNatDetMapOperState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 3, 6, 1, 8),
    _TmnxNatDetMapOperState_Type()
)
tmnxNatDetMapOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatDetMapOperState.setStatus("obsolete")
_TmnxNatDetPfxMapTable_Object = MibTable
tmnxNatDetPfxMapTable = _TmnxNatDetPfxMapTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 3, 7)
)
if mibBuilder.loadTexts:
    tmnxNatDetPfxMapTable.setStatus("current")
_TmnxNatDetPfxMapEntry_Object = MibTableRow
tmnxNatDetPfxMapEntry = _TmnxNatDetPfxMapEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 3, 7, 1)
)
tmnxNatDetPfxMapEntry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "TIMETRA-NAT-MIB", "tmnxNatDetPfxMapSubType"),
    (0, "TIMETRA-NAT-MIB", "tmnxNatDetPfxMapAddrType"),
    (0, "TIMETRA-NAT-MIB", "tmnxNatDetPfxMapAddr"),
    (0, "TIMETRA-NAT-MIB", "tmnxNatDetPfxMapAddrPrefixLength"),
    (0, "TIMETRA-NAT-MIB", "tmnxNatDetPfxMapNatPolicy"),
)
if mibBuilder.loadTexts:
    tmnxNatDetPfxMapEntry.setStatus("current")
_TmnxNatDetPfxMapSubType_Type = TmnxNatLegacySubscriberType
_TmnxNatDetPfxMapSubType_Object = MibTableColumn
tmnxNatDetPfxMapSubType = _TmnxNatDetPfxMapSubType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 3, 7, 1, 1),
    _TmnxNatDetPfxMapSubType_Type()
)
tmnxNatDetPfxMapSubType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxNatDetPfxMapSubType.setStatus("current")
_TmnxNatDetPfxMapAddrType_Type = InetAddressType
_TmnxNatDetPfxMapAddrType_Object = MibTableColumn
tmnxNatDetPfxMapAddrType = _TmnxNatDetPfxMapAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 3, 7, 1, 2),
    _TmnxNatDetPfxMapAddrType_Type()
)
tmnxNatDetPfxMapAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxNatDetPfxMapAddrType.setStatus("current")


class _TmnxNatDetPfxMapAddr_Type(InetAddress):
    """Custom type tmnxNatDetPfxMapAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxNatDetPfxMapAddr_Type.__name__ = "InetAddress"
_TmnxNatDetPfxMapAddr_Object = MibTableColumn
tmnxNatDetPfxMapAddr = _TmnxNatDetPfxMapAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 3, 7, 1, 3),
    _TmnxNatDetPfxMapAddr_Type()
)
tmnxNatDetPfxMapAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxNatDetPfxMapAddr.setStatus("current")


class _TmnxNatDetPfxMapAddrPrefixLength_Type(InetAddressPrefixLength):
    """Custom type tmnxNatDetPfxMapAddrPrefixLength based on InetAddressPrefixLength"""
    subtypeSpec = InetAddressPrefixLength.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 128),
    )


_TmnxNatDetPfxMapAddrPrefixLength_Type.__name__ = "InetAddressPrefixLength"
_TmnxNatDetPfxMapAddrPrefixLength_Object = MibTableColumn
tmnxNatDetPfxMapAddrPrefixLength = _TmnxNatDetPfxMapAddrPrefixLength_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 3, 7, 1, 4),
    _TmnxNatDetPfxMapAddrPrefixLength_Type()
)
tmnxNatDetPfxMapAddrPrefixLength.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxNatDetPfxMapAddrPrefixLength.setStatus("current")
_TmnxNatDetPfxMapNatPolicy_Type = TNamedItem
_TmnxNatDetPfxMapNatPolicy_Object = MibTableColumn
tmnxNatDetPfxMapNatPolicy = _TmnxNatDetPfxMapNatPolicy_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 3, 7, 1, 5),
    _TmnxNatDetPfxMapNatPolicy_Type()
)
tmnxNatDetPfxMapNatPolicy.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxNatDetPfxMapNatPolicy.setStatus("current")
_TmnxNatDetPfxMapRowStatus_Type = RowStatus
_TmnxNatDetPfxMapRowStatus_Object = MibTableColumn
tmnxNatDetPfxMapRowStatus = _TmnxNatDetPfxMapRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 3, 7, 1, 6),
    _TmnxNatDetPfxMapRowStatus_Type()
)
tmnxNatDetPfxMapRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxNatDetPfxMapRowStatus.setStatus("current")
_TmnxNatDetPfxMapLastMgmtChange_Type = TimeStamp
_TmnxNatDetPfxMapLastMgmtChange_Object = MibTableColumn
tmnxNatDetPfxMapLastMgmtChange = _TmnxNatDetPfxMapLastMgmtChange_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 3, 7, 1, 7),
    _TmnxNatDetPfxMapLastMgmtChange_Type()
)
tmnxNatDetPfxMapLastMgmtChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatDetPfxMapLastMgmtChange.setStatus("current")


class _TmnxNatDetPfxMapAdminState_Type(TmnxAdminState):
    """Custom type tmnxNatDetPfxMapAdminState based on TmnxAdminState"""
    defaultValue = 3


_TmnxNatDetPfxMapAdminState_Type.__name__ = "TmnxAdminState"
_TmnxNatDetPfxMapAdminState_Object = MibTableColumn
tmnxNatDetPfxMapAdminState = _TmnxNatDetPfxMapAdminState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 3, 7, 1, 8),
    _TmnxNatDetPfxMapAdminState_Type()
)
tmnxNatDetPfxMapAdminState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxNatDetPfxMapAdminState.setStatus("current")
_TmnxNatDetPfxMapOperState_Type = ServiceOperStatus
_TmnxNatDetPfxMapOperState_Object = MibTableColumn
tmnxNatDetPfxMapOperState = _TmnxNatDetPfxMapOperState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 3, 7, 1, 9),
    _TmnxNatDetPfxMapOperState_Type()
)
tmnxNatDetPfxMapOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatDetPfxMapOperState.setStatus("current")
_TmnxNatDetMap2Table_Object = MibTable
tmnxNatDetMap2Table = _TmnxNatDetMap2Table_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 3, 8)
)
if mibBuilder.loadTexts:
    tmnxNatDetMap2Table.setStatus("current")
_TmnxNatDetMap2Entry_Object = MibTableRow
tmnxNatDetMap2Entry = _TmnxNatDetMap2Entry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 3, 8, 1)
)
tmnxNatDetMap2Entry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "TIMETRA-NAT-MIB", "tmnxNatDetPfxMapSubType"),
    (0, "TIMETRA-NAT-MIB", "tmnxNatDetPfxMapAddrType"),
    (0, "TIMETRA-NAT-MIB", "tmnxNatDetPfxMapAddr"),
    (0, "TIMETRA-NAT-MIB", "tmnxNatDetPfxMapAddrPrefixLength"),
    (0, "TIMETRA-NAT-MIB", "tmnxNatDetPfxMapNatPolicy"),
    (0, "TIMETRA-NAT-MIB", "tmnxNatDetMap2InAddrType"),
    (0, "TIMETRA-NAT-MIB", "tmnxNatDetMap2InStart"),
    (0, "TIMETRA-NAT-MIB", "tmnxNatDetMap2InEnd"),
)
if mibBuilder.loadTexts:
    tmnxNatDetMap2Entry.setStatus("current")
_TmnxNatDetMap2InAddrType_Type = InetAddressType
_TmnxNatDetMap2InAddrType_Object = MibTableColumn
tmnxNatDetMap2InAddrType = _TmnxNatDetMap2InAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 3, 8, 1, 1),
    _TmnxNatDetMap2InAddrType_Type()
)
tmnxNatDetMap2InAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxNatDetMap2InAddrType.setStatus("current")


class _TmnxNatDetMap2InStart_Type(InetAddress):
    """Custom type tmnxNatDetMap2InStart based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxNatDetMap2InStart_Type.__name__ = "InetAddress"
_TmnxNatDetMap2InStart_Object = MibTableColumn
tmnxNatDetMap2InStart = _TmnxNatDetMap2InStart_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 3, 8, 1, 2),
    _TmnxNatDetMap2InStart_Type()
)
tmnxNatDetMap2InStart.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxNatDetMap2InStart.setStatus("current")


class _TmnxNatDetMap2InEnd_Type(InetAddress):
    """Custom type tmnxNatDetMap2InEnd based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxNatDetMap2InEnd_Type.__name__ = "InetAddress"
_TmnxNatDetMap2InEnd_Object = MibTableColumn
tmnxNatDetMap2InEnd = _TmnxNatDetMap2InEnd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 3, 8, 1, 3),
    _TmnxNatDetMap2InEnd_Type()
)
tmnxNatDetMap2InEnd.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxNatDetMap2InEnd.setStatus("current")
_TmnxNatDetMap2RowStatus_Type = RowStatus
_TmnxNatDetMap2RowStatus_Object = MibTableColumn
tmnxNatDetMap2RowStatus = _TmnxNatDetMap2RowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 3, 8, 1, 4),
    _TmnxNatDetMap2RowStatus_Type()
)
tmnxNatDetMap2RowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxNatDetMap2RowStatus.setStatus("current")
_TmnxNatDetMap2LastCh_Type = TimeStamp
_TmnxNatDetMap2LastCh_Object = MibTableColumn
tmnxNatDetMap2LastCh = _TmnxNatDetMap2LastCh_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 3, 8, 1, 5),
    _TmnxNatDetMap2LastCh_Type()
)
tmnxNatDetMap2LastCh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatDetMap2LastCh.setStatus("current")
_TmnxNatDetMap2OutAddrType_Type = InetAddressType
_TmnxNatDetMap2OutAddrType_Object = MibTableColumn
tmnxNatDetMap2OutAddrType = _TmnxNatDetMap2OutAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 3, 8, 1, 6),
    _TmnxNatDetMap2OutAddrType_Type()
)
tmnxNatDetMap2OutAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxNatDetMap2OutAddrType.setStatus("current")


class _TmnxNatDetMap2OutStart_Type(InetAddress):
    """Custom type tmnxNatDetMap2OutStart based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxNatDetMap2OutStart_Type.__name__ = "InetAddress"
_TmnxNatDetMap2OutStart_Object = MibTableColumn
tmnxNatDetMap2OutStart = _TmnxNatDetMap2OutStart_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 3, 8, 1, 7),
    _TmnxNatDetMap2OutStart_Type()
)
tmnxNatDetMap2OutStart.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxNatDetMap2OutStart.setStatus("current")
_TmnxNatDetMap2OperState_Type = ServiceOperStatus
_TmnxNatDetMap2OperState_Object = MibTableColumn
tmnxNatDetMap2OperState = _TmnxNatDetMap2OperState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 3, 8, 1, 8),
    _TmnxNatDetMap2OperState_Type()
)
tmnxNatDetMap2OperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatDetMap2OperState.setStatus("current")
_TmnxNatVrtrSpfPlcyTable_Object = MibTable
tmnxNatVrtrSpfPlcyTable = _TmnxNatVrtrSpfPlcyTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 3, 9)
)
if mibBuilder.loadTexts:
    tmnxNatVrtrSpfPlcyTable.setStatus("current")
_TmnxNatVrtrSpfPlcyEntry_Object = MibTableRow
tmnxNatVrtrSpfPlcyEntry = _TmnxNatVrtrSpfPlcyEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 3, 9, 1)
)
tmnxNatVrtrSpfPlcyEntry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "TIMETRA-NAT-MIB", "tmnxNatVrtrSpfPlcyInPolicy"),
)
if mibBuilder.loadTexts:
    tmnxNatVrtrSpfPlcyEntry.setStatus("current")
_TmnxNatVrtrSpfPlcyInPolicy_Type = TNamedItemOrEmpty
_TmnxNatVrtrSpfPlcyInPolicy_Object = MibTableColumn
tmnxNatVrtrSpfPlcyInPolicy = _TmnxNatVrtrSpfPlcyInPolicy_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 3, 9, 1, 1),
    _TmnxNatVrtrSpfPlcyInPolicy_Type()
)
tmnxNatVrtrSpfPlcyInPolicy.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxNatVrtrSpfPlcyInPolicy.setStatus("current")
_TmnxNatVrtrSpfPlcyLastMgmChg_Type = TimeStamp
_TmnxNatVrtrSpfPlcyLastMgmChg_Object = MibTableColumn
tmnxNatVrtrSpfPlcyLastMgmChg = _TmnxNatVrtrSpfPlcyLastMgmChg_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 3, 9, 1, 2),
    _TmnxNatVrtrSpfPlcyLastMgmChg_Type()
)
tmnxNatVrtrSpfPlcyLastMgmChg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatVrtrSpfPlcyLastMgmChg.setStatus("current")
_TmnxNatVrtrSpfPlcyRowStatus_Type = RowStatus
_TmnxNatVrtrSpfPlcyRowStatus_Object = MibTableColumn
tmnxNatVrtrSpfPlcyRowStatus = _TmnxNatVrtrSpfPlcyRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 3, 9, 1, 3),
    _TmnxNatVrtrSpfPlcyRowStatus_Type()
)
tmnxNatVrtrSpfPlcyRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxNatVrtrSpfPlcyRowStatus.setStatus("current")
_TmnxNatDetAddrMapTable_Object = MibTable
tmnxNatDetAddrMapTable = _TmnxNatDetAddrMapTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 3, 10)
)
if mibBuilder.loadTexts:
    tmnxNatDetAddrMapTable.setStatus("current")
_TmnxNatDetAddrMapEntry_Object = MibTableRow
tmnxNatDetAddrMapEntry = _TmnxNatDetAddrMapEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 3, 10, 1)
)
tmnxNatDetAddrMapEntry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "TIMETRA-NAT-MIB", "tmnxNatDetAddrMapSubType"),
    (0, "TIMETRA-NAT-MIB", "tmnxNatDetAddrMapInStartType"),
    (0, "TIMETRA-NAT-MIB", "tmnxNatDetAddrMapInStart"),
    (0, "TIMETRA-NAT-MIB", "tmnxNatDetAddrMapInStartPfxLen"),
    (0, "TIMETRA-NAT-MIB", "tmnxNatDetAddrMapInEndType"),
    (0, "TIMETRA-NAT-MIB", "tmnxNatDetAddrMapInEnd"),
    (0, "TIMETRA-NAT-MIB", "tmnxNatDetAddrMapInEndPfxLen"),
    (0, "TIMETRA-NAT-MIB", "tmnxNatDetAddrMapNatPolicy"),
)
if mibBuilder.loadTexts:
    tmnxNatDetAddrMapEntry.setStatus("current")
_TmnxNatDetAddrMapSubType_Type = TmnxNatLegacySubscriberType
_TmnxNatDetAddrMapSubType_Object = MibTableColumn
tmnxNatDetAddrMapSubType = _TmnxNatDetAddrMapSubType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 3, 10, 1, 1),
    _TmnxNatDetAddrMapSubType_Type()
)
tmnxNatDetAddrMapSubType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxNatDetAddrMapSubType.setStatus("current")
_TmnxNatDetAddrMapInStartType_Type = InetAddressType
_TmnxNatDetAddrMapInStartType_Object = MibTableColumn
tmnxNatDetAddrMapInStartType = _TmnxNatDetAddrMapInStartType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 3, 10, 1, 2),
    _TmnxNatDetAddrMapInStartType_Type()
)
tmnxNatDetAddrMapInStartType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxNatDetAddrMapInStartType.setStatus("current")


class _TmnxNatDetAddrMapInStart_Type(InetAddress):
    """Custom type tmnxNatDetAddrMapInStart based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxNatDetAddrMapInStart_Type.__name__ = "InetAddress"
_TmnxNatDetAddrMapInStart_Object = MibTableColumn
tmnxNatDetAddrMapInStart = _TmnxNatDetAddrMapInStart_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 3, 10, 1, 3),
    _TmnxNatDetAddrMapInStart_Type()
)
tmnxNatDetAddrMapInStart.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxNatDetAddrMapInStart.setStatus("current")


class _TmnxNatDetAddrMapInStartPfxLen_Type(InetAddressPrefixLength):
    """Custom type tmnxNatDetAddrMapInStartPfxLen based on InetAddressPrefixLength"""
    defaultValue = 128

    subtypeSpec = InetAddressPrefixLength.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(32, 64),
        ValueRangeConstraint(128, 128),
    )


_TmnxNatDetAddrMapInStartPfxLen_Type.__name__ = "InetAddressPrefixLength"
_TmnxNatDetAddrMapInStartPfxLen_Object = MibTableColumn
tmnxNatDetAddrMapInStartPfxLen = _TmnxNatDetAddrMapInStartPfxLen_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 3, 10, 1, 4),
    _TmnxNatDetAddrMapInStartPfxLen_Type()
)
tmnxNatDetAddrMapInStartPfxLen.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxNatDetAddrMapInStartPfxLen.setStatus("current")
_TmnxNatDetAddrMapInEndType_Type = InetAddressType
_TmnxNatDetAddrMapInEndType_Object = MibTableColumn
tmnxNatDetAddrMapInEndType = _TmnxNatDetAddrMapInEndType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 3, 10, 1, 5),
    _TmnxNatDetAddrMapInEndType_Type()
)
tmnxNatDetAddrMapInEndType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxNatDetAddrMapInEndType.setStatus("current")


class _TmnxNatDetAddrMapInEnd_Type(InetAddress):
    """Custom type tmnxNatDetAddrMapInEnd based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxNatDetAddrMapInEnd_Type.__name__ = "InetAddress"
_TmnxNatDetAddrMapInEnd_Object = MibTableColumn
tmnxNatDetAddrMapInEnd = _TmnxNatDetAddrMapInEnd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 3, 10, 1, 6),
    _TmnxNatDetAddrMapInEnd_Type()
)
tmnxNatDetAddrMapInEnd.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxNatDetAddrMapInEnd.setStatus("current")


class _TmnxNatDetAddrMapInEndPfxLen_Type(InetAddressPrefixLength):
    """Custom type tmnxNatDetAddrMapInEndPfxLen based on InetAddressPrefixLength"""
    defaultValue = 128

    subtypeSpec = InetAddressPrefixLength.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(32, 64),
        ValueRangeConstraint(128, 128),
    )


_TmnxNatDetAddrMapInEndPfxLen_Type.__name__ = "InetAddressPrefixLength"
_TmnxNatDetAddrMapInEndPfxLen_Object = MibTableColumn
tmnxNatDetAddrMapInEndPfxLen = _TmnxNatDetAddrMapInEndPfxLen_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 3, 10, 1, 7),
    _TmnxNatDetAddrMapInEndPfxLen_Type()
)
tmnxNatDetAddrMapInEndPfxLen.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxNatDetAddrMapInEndPfxLen.setStatus("current")
_TmnxNatDetAddrMapNatPolicy_Type = TNamedItem
_TmnxNatDetAddrMapNatPolicy_Object = MibTableColumn
tmnxNatDetAddrMapNatPolicy = _TmnxNatDetAddrMapNatPolicy_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 3, 10, 1, 8),
    _TmnxNatDetAddrMapNatPolicy_Type()
)
tmnxNatDetAddrMapNatPolicy.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxNatDetAddrMapNatPolicy.setStatus("current")
_TmnxNatDetAddrMapRowStatus_Type = RowStatus
_TmnxNatDetAddrMapRowStatus_Object = MibTableColumn
tmnxNatDetAddrMapRowStatus = _TmnxNatDetAddrMapRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 3, 10, 1, 9),
    _TmnxNatDetAddrMapRowStatus_Type()
)
tmnxNatDetAddrMapRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxNatDetAddrMapRowStatus.setStatus("current")
_TmnxNatDetAddrMapLastCh_Type = TimeStamp
_TmnxNatDetAddrMapLastCh_Object = MibTableColumn
tmnxNatDetAddrMapLastCh = _TmnxNatDetAddrMapLastCh_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 3, 10, 1, 10),
    _TmnxNatDetAddrMapLastCh_Type()
)
tmnxNatDetAddrMapLastCh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatDetAddrMapLastCh.setStatus("current")


class _TmnxNatDetAddrMapAdminState_Type(TmnxAdminState):
    """Custom type tmnxNatDetAddrMapAdminState based on TmnxAdminState"""
    defaultValue = 3


_TmnxNatDetAddrMapAdminState_Type.__name__ = "TmnxAdminState"
_TmnxNatDetAddrMapAdminState_Object = MibTableColumn
tmnxNatDetAddrMapAdminState = _TmnxNatDetAddrMapAdminState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 3, 10, 1, 11),
    _TmnxNatDetAddrMapAdminState_Type()
)
tmnxNatDetAddrMapAdminState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxNatDetAddrMapAdminState.setStatus("current")
_TmnxNatDetAddrMapOperState_Type = ServiceOperStatus
_TmnxNatDetAddrMapOperState_Object = MibTableColumn
tmnxNatDetAddrMapOperState = _TmnxNatDetAddrMapOperState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 3, 10, 1, 12),
    _TmnxNatDetAddrMapOperState_Type()
)
tmnxNatDetAddrMapOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatDetAddrMapOperState.setStatus("current")
_TmnxNatDetAddrMapOutStartType_Type = InetAddressType
_TmnxNatDetAddrMapOutStartType_Object = MibTableColumn
tmnxNatDetAddrMapOutStartType = _TmnxNatDetAddrMapOutStartType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 3, 10, 1, 13),
    _TmnxNatDetAddrMapOutStartType_Type()
)
tmnxNatDetAddrMapOutStartType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxNatDetAddrMapOutStartType.setStatus("current")


class _TmnxNatDetAddrMapOutStart_Type(InetAddress):
    """Custom type tmnxNatDetAddrMapOutStart based on InetAddress"""
    defaultHexValue = ""

    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxNatDetAddrMapOutStart_Type.__name__ = "InetAddress"
_TmnxNatDetAddrMapOutStart_Object = MibTableColumn
tmnxNatDetAddrMapOutStart = _TmnxNatDetAddrMapOutStart_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 3, 10, 1, 14),
    _TmnxNatDetAddrMapOutStart_Type()
)
tmnxNatDetAddrMapOutStart.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxNatDetAddrMapOutStart.setStatus("current")
_TmnxNatPoolObjs_ObjectIdentity = ObjectIdentity
tmnxNatPoolObjs = _TmnxNatPoolObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 4)
)
_TmnxNatPlTable_Object = MibTable
tmnxNatPlTable = _TmnxNatPlTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 4, 1)
)
if mibBuilder.loadTexts:
    tmnxNatPlTable.setStatus("current")
_TmnxNatPlEntry_Object = MibTableRow
tmnxNatPlEntry = _TmnxNatPlEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 4, 1, 1)
)
tmnxNatPlEntry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (1, "TIMETRA-NAT-MIB", "tmnxNatPlName"),
)
if mibBuilder.loadTexts:
    tmnxNatPlEntry.setStatus("current")
_TmnxNatPlName_Type = TNamedItem
_TmnxNatPlName_Object = MibTableColumn
tmnxNatPlName = _TmnxNatPlName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 4, 1, 1, 1),
    _TmnxNatPlName_Type()
)
tmnxNatPlName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxNatPlName.setStatus("current")
_TmnxNatPlRowStatus_Type = RowStatus
_TmnxNatPlRowStatus_Object = MibTableColumn
tmnxNatPlRowStatus = _TmnxNatPlRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 4, 1, 1, 2),
    _TmnxNatPlRowStatus_Type()
)
tmnxNatPlRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxNatPlRowStatus.setStatus("current")
_TmnxNatPlLastMgmtChange_Type = TimeStamp
_TmnxNatPlLastMgmtChange_Object = MibTableColumn
tmnxNatPlLastMgmtChange = _TmnxNatPlLastMgmtChange_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 4, 1, 1, 3),
    _TmnxNatPlLastMgmtChange_Type()
)
tmnxNatPlLastMgmtChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatPlLastMgmtChange.setStatus("current")
_TmnxNatPlIsaGrp_Type = TmnxNatIsaGrpId
_TmnxNatPlIsaGrp_Object = MibTableColumn
tmnxNatPlIsaGrp = _TmnxNatPlIsaGrp_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 4, 1, 1, 4),
    _TmnxNatPlIsaGrp_Type()
)
tmnxNatPlIsaGrp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxNatPlIsaGrp.setStatus("current")
_TmnxNatPlType_Type = TmnxNatPlType
_TmnxNatPlType_Object = MibTableColumn
tmnxNatPlType = _TmnxNatPlType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 4, 1, 1, 5),
    _TmnxNatPlType_Type()
)
tmnxNatPlType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxNatPlType.setStatus("current")


class _TmnxNatPlDescription_Type(TItemDescription):
    """Custom type tmnxNatPlDescription based on TItemDescription"""
    defaultValue = OctetString("")


_TmnxNatPlDescription_Type.__name__ = "TItemDescription"
_TmnxNatPlDescription_Object = MibTableColumn
tmnxNatPlDescription = _TmnxNatPlDescription_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 4, 1, 1, 6),
    _TmnxNatPlDescription_Type()
)
tmnxNatPlDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxNatPlDescription.setStatus("current")


class _TmnxNatPlAdminState_Type(TmnxAdminState):
    """Custom type tmnxNatPlAdminState based on TmnxAdminState"""
    defaultValue = 3


_TmnxNatPlAdminState_Type.__name__ = "TmnxAdminState"
_TmnxNatPlAdminState_Object = MibTableColumn
tmnxNatPlAdminState = _TmnxNatPlAdminState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 4, 1, 1, 7),
    _TmnxNatPlAdminState_Type()
)
tmnxNatPlAdminState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxNatPlAdminState.setStatus("current")


class _TmnxNatPlPortResvType_Type(Integer32):
    """Custom type tmnxNatPlPortResvType based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ports", 1),
          ("blocks", 2))
    )


_TmnxNatPlPortResvType_Type.__name__ = "Integer32"
_TmnxNatPlPortResvType_Object = MibTableColumn
tmnxNatPlPortResvType = _TmnxNatPlPortResvType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 4, 1, 1, 8),
    _TmnxNatPlPortResvType_Type()
)
tmnxNatPlPortResvType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxNatPlPortResvType.setStatus("current")


class _TmnxNatPlPortResvVal_Type(Unsigned32):
    """Custom type tmnxNatPlPortResvVal based on Unsigned32"""
    defaultValue = 128

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_TmnxNatPlPortResvVal_Type.__name__ = "Unsigned32"
_TmnxNatPlPortResvVal_Object = MibTableColumn
tmnxNatPlPortResvVal = _TmnxNatPlPortResvVal_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 4, 1, 1, 9),
    _TmnxNatPlPortResvVal_Type()
)
tmnxNatPlPortResvVal.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxNatPlPortResvVal.setStatus("current")


class _TmnxNatPlPortResvAllowPrivileged_Type(TruthValue):
    """Custom type tmnxNatPlPortResvAllowPrivileged based on TruthValue"""
    defaultValue = 2


_TmnxNatPlPortResvAllowPrivileged_Type.__name__ = "TruthValue"
_TmnxNatPlPortResvAllowPrivileged_Object = MibTableColumn
tmnxNatPlPortResvAllowPrivileged = _TmnxNatPlPortResvAllowPrivileged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 4, 1, 1, 10),
    _TmnxNatPlPortResvAllowPrivileged_Type()
)
tmnxNatPlPortResvAllowPrivileged.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxNatPlPortResvAllowPrivileged.setStatus("current")


class _TmnxNatPlWatermarkHigh_Type(TmnxNatWaterMark):
    """Custom type tmnxNatPlWatermarkHigh based on TmnxNatWaterMark"""
    defaultValue = 0

    subtypeSpec = TmnxNatWaterMark.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 100),
    )


_TmnxNatPlWatermarkHigh_Type.__name__ = "TmnxNatWaterMark"
_TmnxNatPlWatermarkHigh_Object = MibTableColumn
tmnxNatPlWatermarkHigh = _TmnxNatPlWatermarkHigh_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 4, 1, 1, 11),
    _TmnxNatPlWatermarkHigh_Type()
)
tmnxNatPlWatermarkHigh.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxNatPlWatermarkHigh.setStatus("current")


class _TmnxNatPlWatermarkLow_Type(TmnxNatWaterMark):
    """Custom type tmnxNatPlWatermarkLow based on TmnxNatWaterMark"""
    defaultValue = 0

    subtypeSpec = TmnxNatWaterMark.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 99),
    )


_TmnxNatPlWatermarkLow_Type.__name__ = "TmnxNatWaterMark"
_TmnxNatPlWatermarkLow_Object = MibTableColumn
tmnxNatPlWatermarkLow = _TmnxNatPlWatermarkLow_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 4, 1, 1, 12),
    _TmnxNatPlWatermarkLow_Type()
)
tmnxNatPlWatermarkLow.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxNatPlWatermarkLow.setStatus("current")


class _TmnxNatPlMode_Type(TmnxNatMode):
    """Custom type tmnxNatPlMode based on TmnxNatMode"""
    defaultValue = 0


_TmnxNatPlMode_Type.__name__ = "TmnxNatMode"
_TmnxNatPlMode_Object = MibTableColumn
tmnxNatPlMode = _TmnxNatPlMode_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 4, 1, 1, 13),
    _TmnxNatPlMode_Type()
)
tmnxNatPlMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxNatPlMode.setStatus("current")


class _TmnxNatPlPortFwdRangeEnd_Type(Unsigned32):
    """Custom type tmnxNatPlPortFwdRangeEnd based on Unsigned32"""
    defaultValue = 1023

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1023, 65535),
    )


_TmnxNatPlPortFwdRangeEnd_Type.__name__ = "Unsigned32"
_TmnxNatPlPortFwdRangeEnd_Object = MibTableColumn
tmnxNatPlPortFwdRangeEnd = _TmnxNatPlPortFwdRangeEnd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 4, 1, 1, 14),
    _TmnxNatPlPortFwdRangeEnd_Type()
)
tmnxNatPlPortFwdRangeEnd.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxNatPlPortFwdRangeEnd.setStatus("current")


class _TmnxNatPlPortFwdDynBlkResv_Type(Unsigned32):
    """Custom type tmnxNatPlPortFwdDynBlkResv based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_TmnxNatPlPortFwdDynBlkResv_Type.__name__ = "Unsigned32"
_TmnxNatPlPortFwdDynBlkResv_Object = MibTableColumn
tmnxNatPlPortFwdDynBlkResv = _TmnxNatPlPortFwdDynBlkResv_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 4, 1, 1, 16),
    _TmnxNatPlPortFwdDynBlkResv_Type()
)
tmnxNatPlPortFwdDynBlkResv.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxNatPlPortFwdDynBlkResv.setStatus("current")
_TmnxNatPlOperMode_Type = TmnxNatMode
_TmnxNatPlOperMode_Object = MibTableColumn
tmnxNatPlOperMode = _TmnxNatPlOperMode_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 4, 1, 1, 20),
    _TmnxNatPlOperMode_Type()
)
tmnxNatPlOperMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatPlOperMode.setStatus("current")


class _TmnxNatPlApplications_Type(Bits):
    """Custom type tmnxNatPlApplications based on Bits"""
    defaultBinValue = "0"

    namedValues = NamedValues(
        *(("agnostic", 0),
          ("flexiblePortAllocation", 1),
          ("useInterfaceIp", 2))
    )

_TmnxNatPlApplications_Type.__name__ = "Bits"
_TmnxNatPlApplications_Object = MibTableColumn
tmnxNatPlApplications = _TmnxNatPlApplications_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 4, 1, 1, 21),
    _TmnxNatPlApplications_Type()
)
tmnxNatPlApplications.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxNatPlApplications.setStatus("current")


class _TmnxNatPlIcmpEchoReply_Type(TruthValue):
    """Custom type tmnxNatPlIcmpEchoReply based on TruthValue"""
    defaultValue = 2


_TmnxNatPlIcmpEchoReply_Type.__name__ = "TruthValue"
_TmnxNatPlIcmpEchoReply_Object = MibTableColumn
tmnxNatPlIcmpEchoReply = _TmnxNatPlIcmpEchoReply_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 4, 1, 1, 22),
    _TmnxNatPlIcmpEchoReply_Type()
)
tmnxNatPlIcmpEchoReply.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxNatPlIcmpEchoReply.setStatus("current")


class _TmnxNatPlExPrtBlcksWatermarkHigh_Type(TmnxNatWaterMark):
    """Custom type tmnxNatPlExPrtBlcksWatermarkHigh based on TmnxNatWaterMark"""
    defaultValue = 0

    subtypeSpec = TmnxNatWaterMark.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 100),
    )


_TmnxNatPlExPrtBlcksWatermarkHigh_Type.__name__ = "TmnxNatWaterMark"
_TmnxNatPlExPrtBlcksWatermarkHigh_Object = MibTableColumn
tmnxNatPlExPrtBlcksWatermarkHigh = _TmnxNatPlExPrtBlcksWatermarkHigh_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 4, 1, 1, 23),
    _TmnxNatPlExPrtBlcksWatermarkHigh_Type()
)
tmnxNatPlExPrtBlcksWatermarkHigh.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxNatPlExPrtBlcksWatermarkHigh.setStatus("current")


class _TmnxNatPlExPrtBlcksWatermarkLow_Type(TmnxNatWaterMark):
    """Custom type tmnxNatPlExPrtBlcksWatermarkLow based on TmnxNatWaterMark"""
    defaultValue = 0

    subtypeSpec = TmnxNatWaterMark.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 99),
    )


_TmnxNatPlExPrtBlcksWatermarkLow_Type.__name__ = "TmnxNatWaterMark"
_TmnxNatPlExPrtBlcksWatermarkLow_Object = MibTableColumn
tmnxNatPlExPrtBlcksWatermarkLow = _TmnxNatPlExPrtBlcksWatermarkLow_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 4, 1, 1, 24),
    _TmnxNatPlExPrtBlcksWatermarkLow_Type()
)
tmnxNatPlExPrtBlcksWatermarkLow.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxNatPlExPrtBlcksWatermarkLow.setStatus("current")


class _TmnxNatPlPortFwdRangeStart_Type(Unsigned32):
    """Custom type tmnxNatPlPortFwdRangeStart based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
        ValueRangeConstraint(1025, 65535),
    )


_TmnxNatPlPortFwdRangeStart_Type.__name__ = "Unsigned32"
_TmnxNatPlPortFwdRangeStart_Object = MibTableColumn
tmnxNatPlPortFwdRangeStart = _TmnxNatPlPortFwdRangeStart_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 4, 1, 1, 25),
    _TmnxNatPlPortFwdRangeStart_Type()
)
tmnxNatPlPortFwdRangeStart.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxNatPlPortFwdRangeStart.setStatus("current")


class _TmnxNatPlDhInsideIpAddrType_Type(InetAddressType):
    """Custom type tmnxNatPlDhInsideIpAddrType based on InetAddressType"""
    defaultValue = 0


_TmnxNatPlDhInsideIpAddrType_Type.__name__ = "InetAddressType"
_TmnxNatPlDhInsideIpAddrType_Object = MibTableColumn
tmnxNatPlDhInsideIpAddrType = _TmnxNatPlDhInsideIpAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 4, 1, 1, 26),
    _TmnxNatPlDhInsideIpAddrType_Type()
)
tmnxNatPlDhInsideIpAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxNatPlDhInsideIpAddrType.setStatus("current")


class _TmnxNatPlDhInsideIpAddress_Type(InetAddress):
    """Custom type tmnxNatPlDhInsideIpAddress based on InetAddress"""
    defaultHexValue = ""

    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxNatPlDhInsideIpAddress_Type.__name__ = "InetAddress"
_TmnxNatPlDhInsideIpAddress_Object = MibTableColumn
tmnxNatPlDhInsideIpAddress = _TmnxNatPlDhInsideIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 4, 1, 1, 27),
    _TmnxNatPlDhInsideIpAddress_Type()
)
tmnxNatPlDhInsideIpAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxNatPlDhInsideIpAddress.setStatus("current")


class _TmnxNatPlDhInsideRtrId_Type(TmnxVRtrIDOrZero):
    """Custom type tmnxNatPlDhInsideRtrId based on TmnxVRtrIDOrZero"""
    defaultValue = 0


_TmnxNatPlDhInsideRtrId_Type.__name__ = "TmnxVRtrIDOrZero"
_TmnxNatPlDhInsideRtrId_Object = MibTableColumn
tmnxNatPlDhInsideRtrId = _TmnxNatPlDhInsideRtrId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 4, 1, 1, 28),
    _TmnxNatPlDhInsideRtrId_Type()
)
tmnxNatPlDhInsideRtrId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxNatPlDhInsideRtrId.setStatus("current")


class _TmnxNatPlDhRate_Type(Unsigned32):
    """Custom type tmnxNatPlDhRate based on Unsigned32"""
    defaultValue = 10

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10000),
    )


_TmnxNatPlDhRate_Type.__name__ = "Unsigned32"
_TmnxNatPlDhRate_Object = MibTableColumn
tmnxNatPlDhRate = _TmnxNatPlDhRate_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 4, 1, 1, 29),
    _TmnxNatPlDhRate_Type()
)
tmnxNatPlDhRate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxNatPlDhRate.setStatus("current")
if mibBuilder.loadTexts:
    tmnxNatPlDhRate.setUnits("mbps")


class _TmnxNatPlAddrPooling_Type(Integer32):
    """Custom type tmnxNatPlAddrPooling based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("paired", 1),
          ("arbitrary", 2))
    )


_TmnxNatPlAddrPooling_Type.__name__ = "Integer32"
_TmnxNatPlAddrPooling_Object = MibTableColumn
tmnxNatPlAddrPooling = _TmnxNatPlAddrPooling_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 4, 1, 1, 30),
    _TmnxNatPlAddrPooling_Type()
)
tmnxNatPlAddrPooling.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxNatPlAddrPooling.setStatus("current")
_TmnxNatPlDhForwardedPackets_Type = Counter64
_TmnxNatPlDhForwardedPackets_Object = MibTableColumn
tmnxNatPlDhForwardedPackets = _TmnxNatPlDhForwardedPackets_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 4, 1, 1, 31),
    _TmnxNatPlDhForwardedPackets_Type()
)
tmnxNatPlDhForwardedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatPlDhForwardedPackets.setStatus("current")
_TmnxNatPlDhDroppedPackets_Type = Counter64
_TmnxNatPlDhDroppedPackets_Object = MibTableColumn
tmnxNatPlDhDroppedPackets = _TmnxNatPlDhDroppedPackets_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 4, 1, 1, 32),
    _TmnxNatPlDhDroppedPackets_Type()
)
tmnxNatPlDhDroppedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatPlDhDroppedPackets.setStatus("current")


class _TmnxNatPlMonitorOperGroup_Type(TNamedItemOrEmpty):
    """Custom type tmnxNatPlMonitorOperGroup based on TNamedItemOrEmpty"""
    defaultValue = OctetString("")


_TmnxNatPlMonitorOperGroup_Type.__name__ = "TNamedItemOrEmpty"
_TmnxNatPlMonitorOperGroup_Object = MibTableColumn
tmnxNatPlMonitorOperGroup = _TmnxNatPlMonitorOperGroup_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 4, 1, 1, 33),
    _TmnxNatPlMonitorOperGroup_Type()
)
tmnxNatPlMonitorOperGroup.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxNatPlMonitorOperGroup.setStatus("current")
_TmnxNatPlRangeTable_Object = MibTable
tmnxNatPlRangeTable = _TmnxNatPlRangeTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 4, 2)
)
if mibBuilder.loadTexts:
    tmnxNatPlRangeTable.setStatus("current")
_TmnxNatPlRangeEntry_Object = MibTableRow
tmnxNatPlRangeEntry = _TmnxNatPlRangeEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 4, 2, 1)
)
tmnxNatPlRangeEntry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "TIMETRA-NAT-MIB", "tmnxNatPlName"),
    (0, "TIMETRA-NAT-MIB", "tmnxNatPlRangeAddrType"),
    (0, "TIMETRA-NAT-MIB", "tmnxNatPlRangeStart"),
    (0, "TIMETRA-NAT-MIB", "tmnxNatPlRangeEnd"),
)
if mibBuilder.loadTexts:
    tmnxNatPlRangeEntry.setStatus("current")
_TmnxNatPlRangeAddrType_Type = InetAddressType
_TmnxNatPlRangeAddrType_Object = MibTableColumn
tmnxNatPlRangeAddrType = _TmnxNatPlRangeAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 4, 2, 1, 1),
    _TmnxNatPlRangeAddrType_Type()
)
tmnxNatPlRangeAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxNatPlRangeAddrType.setStatus("current")


class _TmnxNatPlRangeStart_Type(InetAddress):
    """Custom type tmnxNatPlRangeStart based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxNatPlRangeStart_Type.__name__ = "InetAddress"
_TmnxNatPlRangeStart_Object = MibTableColumn
tmnxNatPlRangeStart = _TmnxNatPlRangeStart_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 4, 2, 1, 2),
    _TmnxNatPlRangeStart_Type()
)
tmnxNatPlRangeStart.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxNatPlRangeStart.setStatus("current")


class _TmnxNatPlRangeEnd_Type(InetAddress):
    """Custom type tmnxNatPlRangeEnd based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxNatPlRangeEnd_Type.__name__ = "InetAddress"
_TmnxNatPlRangeEnd_Object = MibTableColumn
tmnxNatPlRangeEnd = _TmnxNatPlRangeEnd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 4, 2, 1, 3),
    _TmnxNatPlRangeEnd_Type()
)
tmnxNatPlRangeEnd.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxNatPlRangeEnd.setStatus("current")
_TmnxNatPlRangeRowStatus_Type = RowStatus
_TmnxNatPlRangeRowStatus_Object = MibTableColumn
tmnxNatPlRangeRowStatus = _TmnxNatPlRangeRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 4, 2, 1, 4),
    _TmnxNatPlRangeRowStatus_Type()
)
tmnxNatPlRangeRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxNatPlRangeRowStatus.setStatus("current")
_TmnxNatPlRangeLastMgmtChange_Type = TimeStamp
_TmnxNatPlRangeLastMgmtChange_Object = MibTableColumn
tmnxNatPlRangeLastMgmtChange = _TmnxNatPlRangeLastMgmtChange_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 4, 2, 1, 5),
    _TmnxNatPlRangeLastMgmtChange_Type()
)
tmnxNatPlRangeLastMgmtChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatPlRangeLastMgmtChange.setStatus("current")


class _TmnxNatPlRangeDescription_Type(TItemDescription):
    """Custom type tmnxNatPlRangeDescription based on TItemDescription"""
    defaultValue = OctetString("")


_TmnxNatPlRangeDescription_Type.__name__ = "TItemDescription"
_TmnxNatPlRangeDescription_Object = MibTableColumn
tmnxNatPlRangeDescription = _TmnxNatPlRangeDescription_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 4, 2, 1, 6),
    _TmnxNatPlRangeDescription_Type()
)
tmnxNatPlRangeDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxNatPlRangeDescription.setStatus("current")


class _TmnxNatPlRangeAdminDrain_Type(TruthValue):
    """Custom type tmnxNatPlRangeAdminDrain based on TruthValue"""
    defaultValue = 2


_TmnxNatPlRangeAdminDrain_Type.__name__ = "TruthValue"
_TmnxNatPlRangeAdminDrain_Object = MibTableColumn
tmnxNatPlRangeAdminDrain = _TmnxNatPlRangeAdminDrain_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 4, 2, 1, 7),
    _TmnxNatPlRangeAdminDrain_Type()
)
tmnxNatPlRangeAdminDrain.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxNatPlRangeAdminDrain.setStatus("current")
_TmnxNatPlRangeNumAllocatedBlk_Type = Gauge32
_TmnxNatPlRangeNumAllocatedBlk_Object = MibTableColumn
tmnxNatPlRangeNumAllocatedBlk = _TmnxNatPlRangeNumAllocatedBlk_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 4, 2, 1, 8),
    _TmnxNatPlRangeNumAllocatedBlk_Type()
)
tmnxNatPlRangeNumAllocatedBlk.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatPlRangeNumAllocatedBlk.setStatus("obsolete")
_TmnxNatPlL2AwTable_Object = MibTable
tmnxNatPlL2AwTable = _TmnxNatPlL2AwTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 4, 3)
)
if mibBuilder.loadTexts:
    tmnxNatPlL2AwTable.setStatus("current")
_TmnxNatPlL2AwEntry_Object = MibTableRow
tmnxNatPlL2AwEntry = _TmnxNatPlL2AwEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 4, 3, 1)
)
tmnxNatPlL2AwEntry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (1, "TIMETRA-NAT-MIB", "tmnxNatPlName"),
)
if mibBuilder.loadTexts:
    tmnxNatPlL2AwEntry.setStatus("current")
_TmnxNatPlL2AwBlockUsage_Type = TmnxNatUsageLevel
_TmnxNatPlL2AwBlockUsage_Object = MibTableColumn
tmnxNatPlL2AwBlockUsage = _TmnxNatPlL2AwBlockUsage_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 4, 3, 1, 1),
    _TmnxNatPlL2AwBlockUsage_Type()
)
tmnxNatPlL2AwBlockUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatPlL2AwBlockUsage.setStatus("current")
_TmnxNatPlL2AwBlockUsageHi_Type = TruthValue
_TmnxNatPlL2AwBlockUsageHi_Object = MibTableColumn
tmnxNatPlL2AwBlockUsageHi = _TmnxNatPlL2AwBlockUsageHi_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 4, 3, 1, 2),
    _TmnxNatPlL2AwBlockUsageHi_Type()
)
tmnxNatPlL2AwBlockUsageHi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatPlL2AwBlockUsageHi.setStatus("current")


class _TmnxNatPlL2AwExternalAssignment_Type(TruthValue):
    """Custom type tmnxNatPlL2AwExternalAssignment based on TruthValue"""
    defaultValue = 2


_TmnxNatPlL2AwExternalAssignment_Type.__name__ = "TruthValue"
_TmnxNatPlL2AwExternalAssignment_Object = MibTableColumn
tmnxNatPlL2AwExternalAssignment = _TmnxNatPlL2AwExternalAssignment_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 4, 3, 1, 3),
    _TmnxNatPlL2AwExternalAssignment_Type()
)
tmnxNatPlL2AwExternalAssignment.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxNatPlL2AwExternalAssignment.setStatus("current")


class _TmnxNatPlL2AwDynResv_Type(TruthValue):
    """Custom type tmnxNatPlL2AwDynResv based on TruthValue"""
    defaultValue = 2


_TmnxNatPlL2AwDynResv_Type.__name__ = "TruthValue"
_TmnxNatPlL2AwDynResv_Object = MibTableColumn
tmnxNatPlL2AwDynResv = _TmnxNatPlL2AwDynResv_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 4, 3, 1, 4),
    _TmnxNatPlL2AwDynResv_Type()
)
tmnxNatPlL2AwDynResv.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxNatPlL2AwDynResv.setStatus("current")


class _TmnxNatPlL2AwDynResvSubscrLimit_Type(Unsigned32):
    """Custom type tmnxNatPlL2AwDynResvSubscrLimit based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(2, 2000),
    )


_TmnxNatPlL2AwDynResvSubscrLimit_Type.__name__ = "Unsigned32"
_TmnxNatPlL2AwDynResvSubscrLimit_Object = MibTableColumn
tmnxNatPlL2AwDynResvSubscrLimit = _TmnxNatPlL2AwDynResvSubscrLimit_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 4, 3, 1, 5),
    _TmnxNatPlL2AwDynResvSubscrLimit_Type()
)
tmnxNatPlL2AwDynResvSubscrLimit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxNatPlL2AwDynResvSubscrLimit.setStatus("current")


class _TmnxNatPlL2AwDynResvPorts_Type(Unsigned32):
    """Custom type tmnxNatPlL2AwDynResvPorts based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(10, 5000),
    )


_TmnxNatPlL2AwDynResvPorts_Type.__name__ = "Unsigned32"
_TmnxNatPlL2AwDynResvPorts_Object = MibTableColumn
tmnxNatPlL2AwDynResvPorts = _TmnxNatPlL2AwDynResvPorts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 4, 3, 1, 6),
    _TmnxNatPlL2AwDynResvPorts_Type()
)
tmnxNatPlL2AwDynResvPorts.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxNatPlL2AwDynResvPorts.setStatus("current")


class _TmnxNatPlL2AwSubscrWatermarkHigh_Type(TmnxNatWaterMark):
    """Custom type tmnxNatPlL2AwSubscrWatermarkHigh based on TmnxNatWaterMark"""
    defaultValue = 0

    subtypeSpec = TmnxNatWaterMark.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 100),
    )


_TmnxNatPlL2AwSubscrWatermarkHigh_Type.__name__ = "TmnxNatWaterMark"
_TmnxNatPlL2AwSubscrWatermarkHigh_Object = MibTableColumn
tmnxNatPlL2AwSubscrWatermarkHigh = _TmnxNatPlL2AwSubscrWatermarkHigh_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 4, 3, 1, 7),
    _TmnxNatPlL2AwSubscrWatermarkHigh_Type()
)
tmnxNatPlL2AwSubscrWatermarkHigh.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxNatPlL2AwSubscrWatermarkHigh.setStatus("current")


class _TmnxNatPlL2AwSubscrWatermarkLow_Type(TmnxNatWaterMark):
    """Custom type tmnxNatPlL2AwSubscrWatermarkLow based on TmnxNatWaterMark"""
    defaultValue = 0

    subtypeSpec = TmnxNatWaterMark.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 99),
    )


_TmnxNatPlL2AwSubscrWatermarkLow_Type.__name__ = "TmnxNatWaterMark"
_TmnxNatPlL2AwSubscrWatermarkLow_Object = MibTableColumn
tmnxNatPlL2AwSubscrWatermarkLow = _TmnxNatPlL2AwSubscrWatermarkLow_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 4, 3, 1, 8),
    _TmnxNatPlL2AwSubscrWatermarkLow_Type()
)
tmnxNatPlL2AwSubscrWatermarkLow.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxNatPlL2AwSubscrWatermarkLow.setStatus("current")
_TmnxNatPlL2AwSubscrUsage_Type = TmnxNatUsageLevel
_TmnxNatPlL2AwSubscrUsage_Object = MibTableColumn
tmnxNatPlL2AwSubscrUsage = _TmnxNatPlL2AwSubscrUsage_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 4, 3, 1, 9),
    _TmnxNatPlL2AwSubscrUsage_Type()
)
tmnxNatPlL2AwSubscrUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatPlL2AwSubscrUsage.setStatus("current")
_TmnxNatPlL2AwSubscrUsageHi_Type = TruthValue
_TmnxNatPlL2AwSubscrUsageHi_Object = MibTableColumn
tmnxNatPlL2AwSubscrUsageHi = _TmnxNatPlL2AwSubscrUsageHi_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 4, 3, 1, 10),
    _TmnxNatPlL2AwSubscrUsageHi_Type()
)
tmnxNatPlL2AwSubscrUsageHi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatPlL2AwSubscrUsageHi.setStatus("current")
_TmnxNatPlL2AwDynResvNumShrdBlcks_Type = Unsigned32
_TmnxNatPlL2AwDynResvNumShrdBlcks_Object = MibTableColumn
tmnxNatPlL2AwDynResvNumShrdBlcks = _TmnxNatPlL2AwDynResvNumShrdBlcks_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 4, 3, 1, 11),
    _TmnxNatPlL2AwDynResvNumShrdBlcks_Type()
)
tmnxNatPlL2AwDynResvNumShrdBlcks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatPlL2AwDynResvNumShrdBlcks.setStatus("current")
_TmnxNatPlLsnMemberTable_Object = MibTable
tmnxNatPlLsnMemberTable = _TmnxNatPlLsnMemberTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 4, 4)
)
if mibBuilder.loadTexts:
    tmnxNatPlLsnMemberTable.setStatus("current")
_TmnxNatPlLsnMemberEntry_Object = MibTableRow
tmnxNatPlLsnMemberEntry = _TmnxNatPlLsnMemberEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 4, 4, 1)
)
tmnxNatPlLsnMemberEntry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "TIMETRA-NAT-MIB", "tmnxNatPlName"),
    (0, "TIMETRA-NAT-MIB", "tmnxNatIsaMemberId"),
)
if mibBuilder.loadTexts:
    tmnxNatPlLsnMemberEntry.setStatus("current")
_TmnxNatPlLsnMemberIsaGrpId_Type = TmnxNatIsaGrpId
_TmnxNatPlLsnMemberIsaGrpId_Object = MibTableColumn
tmnxNatPlLsnMemberIsaGrpId = _TmnxNatPlLsnMemberIsaGrpId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 4, 4, 1, 1),
    _TmnxNatPlLsnMemberIsaGrpId_Type()
)
tmnxNatPlLsnMemberIsaGrpId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatPlLsnMemberIsaGrpId.setStatus("current")
_TmnxNatPlLsnMemberBlockUsage_Type = TmnxNatUsageLevel
_TmnxNatPlLsnMemberBlockUsage_Object = MibTableColumn
tmnxNatPlLsnMemberBlockUsage = _TmnxNatPlLsnMemberBlockUsage_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 4, 4, 1, 2),
    _TmnxNatPlLsnMemberBlockUsage_Type()
)
tmnxNatPlLsnMemberBlockUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatPlLsnMemberBlockUsage.setStatus("current")
_TmnxNatPlLsnMemberBlockUsageHi_Type = TruthValue
_TmnxNatPlLsnMemberBlockUsageHi_Object = MibTableColumn
tmnxNatPlLsnMemberBlockUsageHi = _TmnxNatPlLsnMemberBlockUsageHi_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 4, 4, 1, 3),
    _TmnxNatPlLsnMemberBlockUsageHi_Type()
)
tmnxNatPlLsnMemberBlockUsageHi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatPlLsnMemberBlockUsageHi.setStatus("current")
_TmnxNatPlLsnMbrTcpPortUsage_Type = Unsigned32
_TmnxNatPlLsnMbrTcpPortUsage_Object = MibTableColumn
tmnxNatPlLsnMbrTcpPortUsage = _TmnxNatPlLsnMbrTcpPortUsage_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 4, 4, 1, 4),
    _TmnxNatPlLsnMbrTcpPortUsage_Type()
)
tmnxNatPlLsnMbrTcpPortUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatPlLsnMbrTcpPortUsage.setStatus("current")
_TmnxNatPlLsnMbrTcpPortUsageHi_Type = TruthValue
_TmnxNatPlLsnMbrTcpPortUsageHi_Object = MibTableColumn
tmnxNatPlLsnMbrTcpPortUsageHi = _TmnxNatPlLsnMbrTcpPortUsageHi_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 4, 4, 1, 5),
    _TmnxNatPlLsnMbrTcpPortUsageHi_Type()
)
tmnxNatPlLsnMbrTcpPortUsageHi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatPlLsnMbrTcpPortUsageHi.setStatus("current")
_TmnxNatPlLsnMbrUdpPortUsage_Type = Unsigned32
_TmnxNatPlLsnMbrUdpPortUsage_Object = MibTableColumn
tmnxNatPlLsnMbrUdpPortUsage = _TmnxNatPlLsnMbrUdpPortUsage_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 4, 4, 1, 6),
    _TmnxNatPlLsnMbrUdpPortUsage_Type()
)
tmnxNatPlLsnMbrUdpPortUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatPlLsnMbrUdpPortUsage.setStatus("current")
_TmnxNatPlLsnMbrUdpPortUsageHi_Type = TruthValue
_TmnxNatPlLsnMbrUdpPortUsageHi_Object = MibTableColumn
tmnxNatPlLsnMbrUdpPortUsageHi = _TmnxNatPlLsnMbrUdpPortUsageHi_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 4, 4, 1, 7),
    _TmnxNatPlLsnMbrUdpPortUsageHi_Type()
)
tmnxNatPlLsnMbrUdpPortUsageHi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatPlLsnMbrUdpPortUsageHi.setStatus("current")
_TmnxNatPlLsnMbrOtherPortUsage_Type = Unsigned32
_TmnxNatPlLsnMbrOtherPortUsage_Object = MibTableColumn
tmnxNatPlLsnMbrOtherPortUsage = _TmnxNatPlLsnMbrOtherPortUsage_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 4, 4, 1, 8),
    _TmnxNatPlLsnMbrOtherPortUsage_Type()
)
tmnxNatPlLsnMbrOtherPortUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatPlLsnMbrOtherPortUsage.setStatus("current")
_TmnxNatPlLsnMbrOtherPortUsageHi_Type = TruthValue
_TmnxNatPlLsnMbrOtherPortUsageHi_Object = MibTableColumn
tmnxNatPlLsnMbrOtherPortUsageHi = _TmnxNatPlLsnMbrOtherPortUsageHi_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 4, 4, 1, 9),
    _TmnxNatPlLsnMbrOtherPortUsageHi_Type()
)
tmnxNatPlLsnMbrOtherPortUsageHi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatPlLsnMbrOtherPortUsageHi.setStatus("current")
_TmnxNatBlkL2AwTable_Object = MibTable
tmnxNatBlkL2AwTable = _TmnxNatBlkL2AwTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 4, 5)
)
if mibBuilder.loadTexts:
    tmnxNatBlkL2AwTable.setStatus("current")
_TmnxNatBlkL2AwEntry_Object = MibTableRow
tmnxNatBlkL2AwEntry = _TmnxNatBlkL2AwEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 4, 5, 1)
)
tmnxNatBlkL2AwEntry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "TIMETRA-NAT-MIB", "tmnxNatBlkL2AwAddrType"),
    (0, "TIMETRA-NAT-MIB", "tmnxNatBlkL2AwAddr"),
    (0, "TIMETRA-NAT-MIB", "tmnxNatBlkL2AwStart"),
)
if mibBuilder.loadTexts:
    tmnxNatBlkL2AwEntry.setStatus("current")
_TmnxNatBlkL2AwAddrType_Type = InetAddressType
_TmnxNatBlkL2AwAddrType_Object = MibTableColumn
tmnxNatBlkL2AwAddrType = _TmnxNatBlkL2AwAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 4, 5, 1, 1),
    _TmnxNatBlkL2AwAddrType_Type()
)
tmnxNatBlkL2AwAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxNatBlkL2AwAddrType.setStatus("current")


class _TmnxNatBlkL2AwAddr_Type(InetAddress):
    """Custom type tmnxNatBlkL2AwAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxNatBlkL2AwAddr_Type.__name__ = "InetAddress"
_TmnxNatBlkL2AwAddr_Object = MibTableColumn
tmnxNatBlkL2AwAddr = _TmnxNatBlkL2AwAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 4, 5, 1, 2),
    _TmnxNatBlkL2AwAddr_Type()
)
tmnxNatBlkL2AwAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxNatBlkL2AwAddr.setStatus("current")
_TmnxNatBlkL2AwStart_Type = InetPortNumber
_TmnxNatBlkL2AwStart_Object = MibTableColumn
tmnxNatBlkL2AwStart = _TmnxNatBlkL2AwStart_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 4, 5, 1, 3),
    _TmnxNatBlkL2AwStart_Type()
)
tmnxNatBlkL2AwStart.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxNatBlkL2AwStart.setStatus("current")
_TmnxNatBlkL2AwEnd_Type = InetPortNumber
_TmnxNatBlkL2AwEnd_Object = MibTableColumn
tmnxNatBlkL2AwEnd = _TmnxNatBlkL2AwEnd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 4, 5, 1, 4),
    _TmnxNatBlkL2AwEnd_Type()
)
tmnxNatBlkL2AwEnd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatBlkL2AwEnd.setStatus("current")
_TmnxNatBlkL2AwPool_Type = TLNamedItem
_TmnxNatBlkL2AwPool_Object = MibTableColumn
tmnxNatBlkL2AwPool = _TmnxNatBlkL2AwPool_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 4, 5, 1, 5),
    _TmnxNatBlkL2AwPool_Type()
)
tmnxNatBlkL2AwPool.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatBlkL2AwPool.setStatus("current")
_TmnxNatBlkL2AwSubIdent_Type = TmnxSubIdentString
_TmnxNatBlkL2AwSubIdent_Object = MibTableColumn
tmnxNatBlkL2AwSubIdent = _TmnxNatBlkL2AwSubIdent_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 4, 5, 1, 6),
    _TmnxNatBlkL2AwSubIdent_Type()
)
tmnxNatBlkL2AwSubIdent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatBlkL2AwSubIdent.setStatus("current")
_TmnxNatBlkL2AwPolicy_Type = TNamedItemOrEmpty
_TmnxNatBlkL2AwPolicy_Object = MibTableColumn
tmnxNatBlkL2AwPolicy = _TmnxNatBlkL2AwPolicy_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 4, 5, 1, 7),
    _TmnxNatBlkL2AwPolicy_Type()
)
tmnxNatBlkL2AwPolicy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatBlkL2AwPolicy.setStatus("current")


class _TmnxNatBlkL2AwStartDateAndTime_Type(DateAndTime):
    """Custom type tmnxNatBlkL2AwStartDateAndTime based on DateAndTime"""
    subtypeSpec = DateAndTime.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(11, 11),
    )
    fixed_length = 11


_TmnxNatBlkL2AwStartDateAndTime_Type.__name__ = "DateAndTime"
_TmnxNatBlkL2AwStartDateAndTime_Object = MibTableColumn
tmnxNatBlkL2AwStartDateAndTime = _TmnxNatBlkL2AwStartDateAndTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 4, 5, 1, 8),
    _TmnxNatBlkL2AwStartDateAndTime_Type()
)
tmnxNatBlkL2AwStartDateAndTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatBlkL2AwStartDateAndTime.setStatus("current")
_TmnxNatBlkLsnTable_Object = MibTable
tmnxNatBlkLsnTable = _TmnxNatBlkLsnTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 4, 6)
)
if mibBuilder.loadTexts:
    tmnxNatBlkLsnTable.setStatus("obsolete")
_TmnxNatBlkLsnEntry_Object = MibTableRow
tmnxNatBlkLsnEntry = _TmnxNatBlkLsnEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 4, 6, 1)
)
tmnxNatBlkLsnEntry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "TIMETRA-NAT-MIB", "tmnxNatBlkLsnAddrType"),
    (0, "TIMETRA-NAT-MIB", "tmnxNatBlkLsnAddr"),
    (0, "TIMETRA-NAT-MIB", "tmnxNatBlkLsnStart"),
)
if mibBuilder.loadTexts:
    tmnxNatBlkLsnEntry.setStatus("current")
_TmnxNatBlkLsnAddrType_Type = InetAddressType
_TmnxNatBlkLsnAddrType_Object = MibTableColumn
tmnxNatBlkLsnAddrType = _TmnxNatBlkLsnAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 4, 6, 1, 1),
    _TmnxNatBlkLsnAddrType_Type()
)
tmnxNatBlkLsnAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxNatBlkLsnAddrType.setStatus("current")


class _TmnxNatBlkLsnAddr_Type(InetAddress):
    """Custom type tmnxNatBlkLsnAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxNatBlkLsnAddr_Type.__name__ = "InetAddress"
_TmnxNatBlkLsnAddr_Object = MibTableColumn
tmnxNatBlkLsnAddr = _TmnxNatBlkLsnAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 4, 6, 1, 2),
    _TmnxNatBlkLsnAddr_Type()
)
tmnxNatBlkLsnAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxNatBlkLsnAddr.setStatus("current")
_TmnxNatBlkLsnStart_Type = InetPortNumber
_TmnxNatBlkLsnStart_Object = MibTableColumn
tmnxNatBlkLsnStart = _TmnxNatBlkLsnStart_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 4, 6, 1, 3),
    _TmnxNatBlkLsnStart_Type()
)
tmnxNatBlkLsnStart.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxNatBlkLsnStart.setStatus("current")
_TmnxNatBlkLsnEnd_Type = InetPortNumber
_TmnxNatBlkLsnEnd_Object = MibTableColumn
tmnxNatBlkLsnEnd = _TmnxNatBlkLsnEnd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 4, 6, 1, 4),
    _TmnxNatBlkLsnEnd_Type()
)
tmnxNatBlkLsnEnd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatBlkLsnEnd.setStatus("obsolete")
_TmnxNatBlkLsnPool_Type = TLNamedItem
_TmnxNatBlkLsnPool_Object = MibTableColumn
tmnxNatBlkLsnPool = _TmnxNatBlkLsnPool_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 4, 6, 1, 5),
    _TmnxNatBlkLsnPool_Type()
)
tmnxNatBlkLsnPool.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatBlkLsnPool.setStatus("obsolete")
_TmnxNatBlkLsnSubId_Type = Unsigned32
_TmnxNatBlkLsnSubId_Object = MibTableColumn
tmnxNatBlkLsnSubId = _TmnxNatBlkLsnSubId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 4, 6, 1, 6),
    _TmnxNatBlkLsnSubId_Type()
)
tmnxNatBlkLsnSubId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatBlkLsnSubId.setStatus("obsolete")
_TmnxNatBlkLsnInsideVRtrID_Type = TmnxVRtrID
_TmnxNatBlkLsnInsideVRtrID_Object = MibTableColumn
tmnxNatBlkLsnInsideVRtrID = _TmnxNatBlkLsnInsideVRtrID_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 4, 6, 1, 7),
    _TmnxNatBlkLsnInsideVRtrID_Type()
)
tmnxNatBlkLsnInsideVRtrID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatBlkLsnInsideVRtrID.setStatus("obsolete")
_TmnxNatBlkLsnInsideAddrType_Type = InetAddressType
_TmnxNatBlkLsnInsideAddrType_Object = MibTableColumn
tmnxNatBlkLsnInsideAddrType = _TmnxNatBlkLsnInsideAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 4, 6, 1, 8),
    _TmnxNatBlkLsnInsideAddrType_Type()
)
tmnxNatBlkLsnInsideAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatBlkLsnInsideAddrType.setStatus("obsolete")


class _TmnxNatBlkLsnInsideAddr_Type(InetAddress):
    """Custom type tmnxNatBlkLsnInsideAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxNatBlkLsnInsideAddr_Type.__name__ = "InetAddress"
_TmnxNatBlkLsnInsideAddr_Object = MibTableColumn
tmnxNatBlkLsnInsideAddr = _TmnxNatBlkLsnInsideAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 4, 6, 1, 9),
    _TmnxNatBlkLsnInsideAddr_Type()
)
tmnxNatBlkLsnInsideAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatBlkLsnInsideAddr.setStatus("obsolete")
_TmnxNatBlkLsnPolicy_Type = TNamedItemOrEmpty
_TmnxNatBlkLsnPolicy_Object = MibTableColumn
tmnxNatBlkLsnPolicy = _TmnxNatBlkLsnPolicy_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 4, 6, 1, 10),
    _TmnxNatBlkLsnPolicy_Type()
)
tmnxNatBlkLsnPolicy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatBlkLsnPolicy.setStatus("obsolete")


class _TmnxNatBlkLsnStartDateAndTime_Type(DateAndTime):
    """Custom type tmnxNatBlkLsnStartDateAndTime based on DateAndTime"""
    subtypeSpec = DateAndTime.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(11, 11),
    )
    fixed_length = 11


_TmnxNatBlkLsnStartDateAndTime_Type.__name__ = "DateAndTime"
_TmnxNatBlkLsnStartDateAndTime_Object = MibTableColumn
tmnxNatBlkLsnStartDateAndTime = _TmnxNatBlkLsnStartDateAndTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 4, 6, 1, 11),
    _TmnxNatBlkLsnStartDateAndTime_Type()
)
tmnxNatBlkLsnStartDateAndTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatBlkLsnStartDateAndTime.setStatus("obsolete")
_TmnxNatPlLsnTable_Object = MibTable
tmnxNatPlLsnTable = _TmnxNatPlLsnTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 4, 7)
)
if mibBuilder.loadTexts:
    tmnxNatPlLsnTable.setStatus("current")
_TmnxNatPlLsnEntry_Object = MibTableRow
tmnxNatPlLsnEntry = _TmnxNatPlLsnEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 4, 7, 1)
)
tmnxNatPlLsnEntry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (1, "TIMETRA-NAT-MIB", "tmnxNatPlName"),
)
if mibBuilder.loadTexts:
    tmnxNatPlLsnEntry.setStatus("current")


class _TmnxNatPlLsnSubscriberLimit_Type(Unsigned32):
    """Custom type tmnxNatPlLsnSubscriberLimit based on Unsigned32"""
    defaultValue = 4294967295

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
        ValueRangeConstraint(4294967295, 4294967295),
    )


_TmnxNatPlLsnSubscriberLimit_Type.__name__ = "Unsigned32"
_TmnxNatPlLsnSubscriberLimit_Object = MibTableColumn
tmnxNatPlLsnSubscriberLimit = _TmnxNatPlLsnSubscriberLimit_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 4, 7, 1, 1),
    _TmnxNatPlLsnSubscriberLimit_Type()
)
tmnxNatPlLsnSubscriberLimit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxNatPlLsnSubscriberLimit.setStatus("current")


class _TmnxNatPlLsnRedExpPrefixType_Type(InetAddressType):
    """Custom type tmnxNatPlLsnRedExpPrefixType based on InetAddressType"""
    defaultValue = 0


_TmnxNatPlLsnRedExpPrefixType_Type.__name__ = "InetAddressType"
_TmnxNatPlLsnRedExpPrefixType_Object = MibTableColumn
tmnxNatPlLsnRedExpPrefixType = _TmnxNatPlLsnRedExpPrefixType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 4, 7, 1, 10),
    _TmnxNatPlLsnRedExpPrefixType_Type()
)
tmnxNatPlLsnRedExpPrefixType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxNatPlLsnRedExpPrefixType.setStatus("current")


class _TmnxNatPlLsnRedExpPrefix_Type(InetAddress):
    """Custom type tmnxNatPlLsnRedExpPrefix based on InetAddress"""
    defaultHexValue = ""

    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxNatPlLsnRedExpPrefix_Type.__name__ = "InetAddress"
_TmnxNatPlLsnRedExpPrefix_Object = MibTableColumn
tmnxNatPlLsnRedExpPrefix = _TmnxNatPlLsnRedExpPrefix_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 4, 7, 1, 11),
    _TmnxNatPlLsnRedExpPrefix_Type()
)
tmnxNatPlLsnRedExpPrefix.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxNatPlLsnRedExpPrefix.setStatus("current")


class _TmnxNatPlLsnRedExpPrefixLen_Type(InetAddressPrefixLength):
    """Custom type tmnxNatPlLsnRedExpPrefixLen based on InetAddressPrefixLength"""
    defaultValue = 0

    subtypeSpec = InetAddressPrefixLength.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_TmnxNatPlLsnRedExpPrefixLen_Type.__name__ = "InetAddressPrefixLength"
_TmnxNatPlLsnRedExpPrefixLen_Object = MibTableColumn
tmnxNatPlLsnRedExpPrefixLen = _TmnxNatPlLsnRedExpPrefixLen_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 4, 7, 1, 12),
    _TmnxNatPlLsnRedExpPrefixLen_Type()
)
tmnxNatPlLsnRedExpPrefixLen.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxNatPlLsnRedExpPrefixLen.setStatus("current")


class _TmnxNatPlLsnRedMonPrefixType_Type(InetAddressType):
    """Custom type tmnxNatPlLsnRedMonPrefixType based on InetAddressType"""
    defaultValue = 0


_TmnxNatPlLsnRedMonPrefixType_Type.__name__ = "InetAddressType"
_TmnxNatPlLsnRedMonPrefixType_Object = MibTableColumn
tmnxNatPlLsnRedMonPrefixType = _TmnxNatPlLsnRedMonPrefixType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 4, 7, 1, 13),
    _TmnxNatPlLsnRedMonPrefixType_Type()
)
tmnxNatPlLsnRedMonPrefixType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxNatPlLsnRedMonPrefixType.setStatus("current")


class _TmnxNatPlLsnRedMonPrefix_Type(InetAddress):
    """Custom type tmnxNatPlLsnRedMonPrefix based on InetAddress"""
    defaultHexValue = ""

    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxNatPlLsnRedMonPrefix_Type.__name__ = "InetAddress"
_TmnxNatPlLsnRedMonPrefix_Object = MibTableColumn
tmnxNatPlLsnRedMonPrefix = _TmnxNatPlLsnRedMonPrefix_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 4, 7, 1, 14),
    _TmnxNatPlLsnRedMonPrefix_Type()
)
tmnxNatPlLsnRedMonPrefix.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxNatPlLsnRedMonPrefix.setStatus("current")


class _TmnxNatPlLsnRedMonPrefixLen_Type(InetAddressPrefixLength):
    """Custom type tmnxNatPlLsnRedMonPrefixLen based on InetAddressPrefixLength"""
    defaultValue = 0

    subtypeSpec = InetAddressPrefixLength.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_TmnxNatPlLsnRedMonPrefixLen_Type.__name__ = "InetAddressPrefixLength"
_TmnxNatPlLsnRedMonPrefixLen_Object = MibTableColumn
tmnxNatPlLsnRedMonPrefixLen = _TmnxNatPlLsnRedMonPrefixLen_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 4, 7, 1, 15),
    _TmnxNatPlLsnRedMonPrefixLen_Type()
)
tmnxNatPlLsnRedMonPrefixLen.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxNatPlLsnRedMonPrefixLen.setStatus("current")
_TmnxNatPlLsnRedActive_Type = TruthValue
_TmnxNatPlLsnRedActive_Object = MibTableColumn
tmnxNatPlLsnRedActive = _TmnxNatPlLsnRedActive_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 4, 7, 1, 16),
    _TmnxNatPlLsnRedActive_Type()
)
tmnxNatPlLsnRedActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatPlLsnRedActive.setStatus("current")


class _TmnxNatPlLsnDetPortResv_Type(Unsigned32):
    """Custom type tmnxNatPlLsnDetPortResv based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_TmnxNatPlLsnDetPortResv_Type.__name__ = "Unsigned32"
_TmnxNatPlLsnDetPortResv_Object = MibTableColumn
tmnxNatPlLsnDetPortResv = _TmnxNatPlLsnDetPortResv_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 4, 7, 1, 20),
    _TmnxNatPlLsnDetPortResv_Type()
)
tmnxNatPlLsnDetPortResv.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxNatPlLsnDetPortResv.setStatus("current")


class _TmnxNatPlLsnRedAdminState_Type(TmnxAdminState):
    """Custom type tmnxNatPlLsnRedAdminState based on TmnxAdminState"""
    defaultValue = 3


_TmnxNatPlLsnRedAdminState_Type.__name__ = "TmnxAdminState"
_TmnxNatPlLsnRedAdminState_Object = MibTableColumn
tmnxNatPlLsnRedAdminState = _TmnxNatPlLsnRedAdminState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 4, 7, 1, 21),
    _TmnxNatPlLsnRedAdminState_Type()
)
tmnxNatPlLsnRedAdminState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxNatPlLsnRedAdminState.setStatus("current")


class _TmnxNatPlLsnRedFollowPoolRouter_Type(TmnxVRtrIDOrZero):
    """Custom type tmnxNatPlLsnRedFollowPoolRouter based on TmnxVRtrIDOrZero"""
    defaultValue = 0


_TmnxNatPlLsnRedFollowPoolRouter_Type.__name__ = "TmnxVRtrIDOrZero"
_TmnxNatPlLsnRedFollowPoolRouter_Object = MibTableColumn
tmnxNatPlLsnRedFollowPoolRouter = _TmnxNatPlLsnRedFollowPoolRouter_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 4, 7, 1, 22),
    _TmnxNatPlLsnRedFollowPoolRouter_Type()
)
tmnxNatPlLsnRedFollowPoolRouter.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxNatPlLsnRedFollowPoolRouter.setStatus("current")


class _TmnxNatPlLsnRedFollowPool_Type(TNamedItemOrEmpty):
    """Custom type tmnxNatPlLsnRedFollowPool based on TNamedItemOrEmpty"""
    defaultValue = OctetString("")


_TmnxNatPlLsnRedFollowPool_Type.__name__ = "TNamedItemOrEmpty"
_TmnxNatPlLsnRedFollowPool_Object = MibTableColumn
tmnxNatPlLsnRedFollowPool = _TmnxNatPlLsnRedFollowPool_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 4, 7, 1, 23),
    _TmnxNatPlLsnRedFollowPool_Type()
)
tmnxNatPlLsnRedFollowPool.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxNatPlLsnRedFollowPool.setStatus("current")


class _TmnxNatPlLsnFreePortLimitTcp_Type(Unsigned32):
    """Custom type tmnxNatPlLsnFreePortLimitTcp based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 10000),
    )


_TmnxNatPlLsnFreePortLimitTcp_Type.__name__ = "Unsigned32"
_TmnxNatPlLsnFreePortLimitTcp_Object = MibTableColumn
tmnxNatPlLsnFreePortLimitTcp = _TmnxNatPlLsnFreePortLimitTcp_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 4, 7, 1, 24),
    _TmnxNatPlLsnFreePortLimitTcp_Type()
)
tmnxNatPlLsnFreePortLimitTcp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxNatPlLsnFreePortLimitTcp.setStatus("current")


class _TmnxNatPlLsnFreePortLimitUdp_Type(Unsigned32):
    """Custom type tmnxNatPlLsnFreePortLimitUdp based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 10000),
    )


_TmnxNatPlLsnFreePortLimitUdp_Type.__name__ = "Unsigned32"
_TmnxNatPlLsnFreePortLimitUdp_Object = MibTableColumn
tmnxNatPlLsnFreePortLimitUdp = _TmnxNatPlLsnFreePortLimitUdp_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 4, 7, 1, 25),
    _TmnxNatPlLsnFreePortLimitUdp_Type()
)
tmnxNatPlLsnFreePortLimitUdp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxNatPlLsnFreePortLimitUdp.setStatus("current")


class _TmnxNatPlLsnFreePortLimitIcmp_Type(Unsigned32):
    """Custom type tmnxNatPlLsnFreePortLimitIcmp based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 10000),
    )


_TmnxNatPlLsnFreePortLimitIcmp_Type.__name__ = "Unsigned32"
_TmnxNatPlLsnFreePortLimitIcmp_Object = MibTableColumn
tmnxNatPlLsnFreePortLimitIcmp = _TmnxNatPlLsnFreePortLimitIcmp_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 4, 7, 1, 26),
    _TmnxNatPlLsnFreePortLimitIcmp_Type()
)
tmnxNatPlLsnFreePortLimitIcmp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxNatPlLsnFreePortLimitIcmp.setStatus("current")


class _TmnxNatPlLsnRedState_Type(Integer32):
    """Custom type tmnxNatPlLsnRedState based on Integer32"""
    defaultValue = 0

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
              9)
        )
    )
    namedValues = NamedValues(
        *(("down", 0),
          ("downHeld", 1),
          ("standby", 2),
          ("standbyHeld", 3),
          ("active", 4),
          ("activeHeld", 5),
          ("activeSick", 6),
          ("needsAudit", 7),
          ("disabledUp", 8),
          ("disabledDown", 9))
    )


_TmnxNatPlLsnRedState_Type.__name__ = "Integer32"
_TmnxNatPlLsnRedState_Object = MibTableColumn
tmnxNatPlLsnRedState = _TmnxNatPlLsnRedState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 4, 7, 1, 27),
    _TmnxNatPlLsnRedState_Type()
)
tmnxNatPlLsnRedState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatPlLsnRedState.setStatus("current")


class _TmnxNatPlLsnRedStateReason_Type(TItemDescription):
    """Custom type tmnxNatPlLsnRedStateReason based on TItemDescription"""
    defaultValue = OctetString("")


_TmnxNatPlLsnRedStateReason_Type.__name__ = "TItemDescription"
_TmnxNatPlLsnRedStateReason_Object = MibTableColumn
tmnxNatPlLsnRedStateReason = _TmnxNatPlLsnRedStateReason_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 4, 7, 1, 28),
    _TmnxNatPlLsnRedStateReason_Type()
)
tmnxNatPlLsnRedStateReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatPlLsnRedStateReason.setStatus("current")


class _TmnxNatPlLsnCpmReservedPorts_Type(Unsigned32):
    """Custom type tmnxNatPlLsnCpmReservedPorts based on Unsigned32"""
    defaultValue = 10

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_TmnxNatPlLsnCpmReservedPorts_Type.__name__ = "Unsigned32"
_TmnxNatPlLsnCpmReservedPorts_Object = MibTableColumn
tmnxNatPlLsnCpmReservedPorts = _TmnxNatPlLsnCpmReservedPorts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 4, 7, 1, 29),
    _TmnxNatPlLsnCpmReservedPorts_Type()
)
tmnxNatPlLsnCpmReservedPorts.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxNatPlLsnCpmReservedPorts.setStatus("current")
_TmnxNatPlHistAction_ObjectIdentity = ObjectIdentity
tmnxNatPlHistAction = _TmnxNatPlHistAction_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 4, 8)
)
_TmnxNatPlHistActionVRtrId_Type = TmnxVRtrIDOrZero
_TmnxNatPlHistActionVRtrId_Object = MibScalar
tmnxNatPlHistActionVRtrId = _TmnxNatPlHistActionVRtrId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 4, 8, 1),
    _TmnxNatPlHistActionVRtrId_Type()
)
tmnxNatPlHistActionVRtrId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxNatPlHistActionVRtrId.setStatus("current")
_TmnxNatPlHistActionPoolName_Type = TNamedItemOrEmpty
_TmnxNatPlHistActionPoolName_Object = MibScalar
tmnxNatPlHistActionPoolName = _TmnxNatPlHistActionPoolName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 4, 8, 2),
    _TmnxNatPlHistActionPoolName_Type()
)
tmnxNatPlHistActionPoolName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxNatPlHistActionPoolName.setStatus("current")


class _TmnxNatPlHistActionBucketSize_Type(Unsigned32):
    """Custom type tmnxNatPlHistActionBucketSize based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 65536),
    )


_TmnxNatPlHistActionBucketSize_Type.__name__ = "Unsigned32"
_TmnxNatPlHistActionBucketSize_Object = MibScalar
tmnxNatPlHistActionBucketSize = _TmnxNatPlHistActionBucketSize_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 4, 8, 3),
    _TmnxNatPlHistActionBucketSize_Type()
)
tmnxNatPlHistActionBucketSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxNatPlHistActionBucketSize.setStatus("current")


class _TmnxNatPlHistActionNumBuckets_Type(Unsigned32):
    """Custom type tmnxNatPlHistActionNumBuckets based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(2, 50),
    )


_TmnxNatPlHistActionNumBuckets_Type.__name__ = "Unsigned32"
_TmnxNatPlHistActionNumBuckets_Object = MibScalar
tmnxNatPlHistActionNumBuckets = _TmnxNatPlHistActionNumBuckets_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 4, 8, 4),
    _TmnxNatPlHistActionNumBuckets_Type()
)
tmnxNatPlHistActionNumBuckets.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxNatPlHistActionNumBuckets.setStatus("current")
_TmnxNatPlHistActionGo_Type = TmnxActionType
_TmnxNatPlHistActionGo_Object = MibScalar
tmnxNatPlHistActionGo = _TmnxNatPlHistActionGo_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 4, 8, 5),
    _TmnxNatPlHistActionGo_Type()
)
tmnxNatPlHistActionGo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxNatPlHistActionGo.setStatus("current")
_TmnxNatPlHistTable_Object = MibTable
tmnxNatPlHistTable = _TmnxNatPlHistTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 4, 9)
)
if mibBuilder.loadTexts:
    tmnxNatPlHistTable.setStatus("current")
_TmnxNatPlHistEntry_Object = MibTableRow
tmnxNatPlHistEntry = _TmnxNatPlHistEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 4, 9, 1)
)
tmnxNatPlHistEntry.setIndexNames(
    (0, "TIMETRA-NAT-MIB", "tmnxNatPlHistIndex"),
)
if mibBuilder.loadTexts:
    tmnxNatPlHistEntry.setStatus("current")
_TmnxNatPlHistIndex_Type = Unsigned32
_TmnxNatPlHistIndex_Object = MibTableColumn
tmnxNatPlHistIndex = _TmnxNatPlHistIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 4, 9, 1, 1),
    _TmnxNatPlHistIndex_Type()
)
tmnxNatPlHistIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxNatPlHistIndex.setStatus("current")
_TmnxNatPlHistTimestamp_Type = TimeStamp
_TmnxNatPlHistTimestamp_Object = MibTableColumn
tmnxNatPlHistTimestamp = _TmnxNatPlHistTimestamp_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 4, 9, 1, 2),
    _TmnxNatPlHistTimestamp_Type()
)
tmnxNatPlHistTimestamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatPlHistTimestamp.setStatus("current")
_TmnxNatPlHistVRtrID_Type = TmnxVRtrID
_TmnxNatPlHistVRtrID_Object = MibTableColumn
tmnxNatPlHistVRtrID = _TmnxNatPlHistVRtrID_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 4, 9, 1, 3),
    _TmnxNatPlHistVRtrID_Type()
)
tmnxNatPlHistVRtrID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatPlHistVRtrID.setStatus("current")
_TmnxNatPlHistPoolName_Type = TNamedItem
_TmnxNatPlHistPoolName_Object = MibTableColumn
tmnxNatPlHistPoolName = _TmnxNatPlHistPoolName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 4, 9, 1, 4),
    _TmnxNatPlHistPoolName_Type()
)
tmnxNatPlHistPoolName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatPlHistPoolName.setStatus("current")
_TmnxNatPlHistBucketSize_Type = Unsigned32
_TmnxNatPlHistBucketSize_Object = MibTableColumn
tmnxNatPlHistBucketSize = _TmnxNatPlHistBucketSize_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 4, 9, 1, 5),
    _TmnxNatPlHistBucketSize_Type()
)
tmnxNatPlHistBucketSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatPlHistBucketSize.setStatus("current")
_TmnxNatPlHistNumBuckets_Type = Unsigned32
_TmnxNatPlHistNumBuckets_Object = MibTableColumn
tmnxNatPlHistNumBuckets = _TmnxNatPlHistNumBuckets_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 4, 9, 1, 6),
    _TmnxNatPlHistNumBuckets_Type()
)
tmnxNatPlHistNumBuckets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatPlHistNumBuckets.setStatus("current")
_TmnxNatPlHistTcp_Type = Gauge32
_TmnxNatPlHistTcp_Object = MibTableColumn
tmnxNatPlHistTcp = _TmnxNatPlHistTcp_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 4, 9, 1, 7),
    _TmnxNatPlHistTcp_Type()
)
tmnxNatPlHistTcp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatPlHistTcp.setStatus("current")
_TmnxNatPlHistUdp_Type = Gauge32
_TmnxNatPlHistUdp_Object = MibTableColumn
tmnxNatPlHistUdp = _TmnxNatPlHistUdp_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 4, 9, 1, 8),
    _TmnxNatPlHistUdp_Type()
)
tmnxNatPlHistUdp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatPlHistUdp.setStatus("current")
_TmnxNatPlHistIcmp_Type = Gauge32
_TmnxNatPlHistIcmp_Object = MibTableColumn
tmnxNatPlHistIcmp = _TmnxNatPlHistIcmp_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 4, 9, 1, 9),
    _TmnxNatPlHistIcmp_Type()
)
tmnxNatPlHistIcmp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatPlHistIcmp.setStatus("current")
_TmnxNatPlRangeStatTable_Object = MibTable
tmnxNatPlRangeStatTable = _TmnxNatPlRangeStatTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 4, 10)
)
if mibBuilder.loadTexts:
    tmnxNatPlRangeStatTable.setStatus("current")
_TmnxNatPlRangeStatEntry_Object = MibTableRow
tmnxNatPlRangeStatEntry = _TmnxNatPlRangeStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 4, 10, 1)
)
if mibBuilder.loadTexts:
    tmnxNatPlRangeStatEntry.setStatus("current")
_TmnxNatPlRangeStatNumAllocBlk_Type = Gauge32
_TmnxNatPlRangeStatNumAllocBlk_Object = MibTableColumn
tmnxNatPlRangeStatNumAllocBlk = _TmnxNatPlRangeStatNumAllocBlk_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 4, 10, 1, 8),
    _TmnxNatPlRangeStatNumAllocBlk_Type()
)
tmnxNatPlRangeStatNumAllocBlk.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatPlRangeStatNumAllocBlk.setStatus("current")
_TmnxNatPlRangeStatNumAllocSub_Type = Gauge32
_TmnxNatPlRangeStatNumAllocSub_Object = MibTableColumn
tmnxNatPlRangeStatNumAllocSub = _TmnxNatPlRangeStatNumAllocSub_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 4, 10, 1, 9),
    _TmnxNatPlRangeStatNumAllocSub_Type()
)
tmnxNatPlRangeStatNumAllocSub.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatPlRangeStatNumAllocSub.setStatus("current")
_TmnxNatPlL2AwMemberTable_Object = MibTable
tmnxNatPlL2AwMemberTable = _TmnxNatPlL2AwMemberTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 4, 11)
)
if mibBuilder.loadTexts:
    tmnxNatPlL2AwMemberTable.setStatus("current")
_TmnxNatPlL2AwMemberEntry_Object = MibTableRow
tmnxNatPlL2AwMemberEntry = _TmnxNatPlL2AwMemberEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 4, 11, 1)
)
tmnxNatPlL2AwMemberEntry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "TIMETRA-NAT-MIB", "tmnxNatPlName"),
    (0, "TIMETRA-NAT-MIB", "tmnxNatIsaMemberId"),
)
if mibBuilder.loadTexts:
    tmnxNatPlL2AwMemberEntry.setStatus("current")
_TmnxNatPlL2AwMemberIsaGrpId_Type = TmnxNatIsaGrpId
_TmnxNatPlL2AwMemberIsaGrpId_Object = MibTableColumn
tmnxNatPlL2AwMemberIsaGrpId = _TmnxNatPlL2AwMemberIsaGrpId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 4, 11, 1, 1),
    _TmnxNatPlL2AwMemberIsaGrpId_Type()
)
tmnxNatPlL2AwMemberIsaGrpId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatPlL2AwMemberIsaGrpId.setStatus("current")
_TmnxNatPlL2AwMemberBlockUsage_Type = TmnxNatUsageLevel
_TmnxNatPlL2AwMemberBlockUsage_Object = MibTableColumn
tmnxNatPlL2AwMemberBlockUsage = _TmnxNatPlL2AwMemberBlockUsage_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 4, 11, 1, 2),
    _TmnxNatPlL2AwMemberBlockUsage_Type()
)
tmnxNatPlL2AwMemberBlockUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatPlL2AwMemberBlockUsage.setStatus("current")
_TmnxNatPlL2AwMemberBlockUsageHi_Type = TruthValue
_TmnxNatPlL2AwMemberBlockUsageHi_Object = MibTableColumn
tmnxNatPlL2AwMemberBlockUsageHi = _TmnxNatPlL2AwMemberBlockUsageHi_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 4, 11, 1, 3),
    _TmnxNatPlL2AwMemberBlockUsageHi_Type()
)
tmnxNatPlL2AwMemberBlockUsageHi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatPlL2AwMemberBlockUsageHi.setStatus("current")
_TmnxNatPlRangeExclTable_Object = MibTable
tmnxNatPlRangeExclTable = _TmnxNatPlRangeExclTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 4, 12)
)
if mibBuilder.loadTexts:
    tmnxNatPlRangeExclTable.setStatus("current")
_TmnxNatPlRangeExclEntry_Object = MibTableRow
tmnxNatPlRangeExclEntry = _TmnxNatPlRangeExclEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 4, 12, 1)
)
tmnxNatPlRangeExclEntry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "TIMETRA-NAT-MIB", "tmnxNatPlName"),
    (0, "TIMETRA-NAT-MIB", "tmnxNatPlRangeAddrType"),
    (0, "TIMETRA-NAT-MIB", "tmnxNatPlRangeStart"),
    (0, "TIMETRA-NAT-MIB", "tmnxNatPlRangeEnd"),
    (0, "TIMETRA-NAT-MIB", "tmnxNatPlRangeExclStart"),
    (0, "TIMETRA-NAT-MIB", "tmnxNatPlRangeExclEnd"),
)
if mibBuilder.loadTexts:
    tmnxNatPlRangeExclEntry.setStatus("current")


class _TmnxNatPlRangeExclStart_Type(InetAddress):
    """Custom type tmnxNatPlRangeExclStart based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxNatPlRangeExclStart_Type.__name__ = "InetAddress"
_TmnxNatPlRangeExclStart_Object = MibTableColumn
tmnxNatPlRangeExclStart = _TmnxNatPlRangeExclStart_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 4, 12, 1, 1),
    _TmnxNatPlRangeExclStart_Type()
)
tmnxNatPlRangeExclStart.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxNatPlRangeExclStart.setStatus("current")


class _TmnxNatPlRangeExclEnd_Type(InetAddress):
    """Custom type tmnxNatPlRangeExclEnd based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxNatPlRangeExclEnd_Type.__name__ = "InetAddress"
_TmnxNatPlRangeExclEnd_Object = MibTableColumn
tmnxNatPlRangeExclEnd = _TmnxNatPlRangeExclEnd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 4, 12, 1, 2),
    _TmnxNatPlRangeExclEnd_Type()
)
tmnxNatPlRangeExclEnd.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxNatPlRangeExclEnd.setStatus("current")
_TmnxNatPlRangeExclRowStatus_Type = RowStatus
_TmnxNatPlRangeExclRowStatus_Object = MibTableColumn
tmnxNatPlRangeExclRowStatus = _TmnxNatPlRangeExclRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 4, 12, 1, 3),
    _TmnxNatPlRangeExclRowStatus_Type()
)
tmnxNatPlRangeExclRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxNatPlRangeExclRowStatus.setStatus("current")
_TmnxNatPlRangeExclLastMgmtChange_Type = TimeStamp
_TmnxNatPlRangeExclLastMgmtChange_Object = MibTableColumn
tmnxNatPlRangeExclLastMgmtChange = _TmnxNatPlRangeExclLastMgmtChange_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 4, 12, 1, 4),
    _TmnxNatPlRangeExclLastMgmtChange_Type()
)
tmnxNatPlRangeExclLastMgmtChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatPlRangeExclLastMgmtChange.setStatus("current")
_TmnxNatDestObjs_ObjectIdentity = ObjectIdentity
tmnxNatDestObjs = _TmnxNatDestObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 5)
)
_TmnxNatDestTable_Object = MibTable
tmnxNatDestTable = _TmnxNatDestTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 5, 1)
)
if mibBuilder.loadTexts:
    tmnxNatDestTable.setStatus("current")
_TmnxNatDestEntry_Object = MibTableRow
tmnxNatDestEntry = _TmnxNatDestEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 5, 1, 1)
)
tmnxNatDestEntry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "TIMETRA-NAT-MIB", "tmnxNatDestAddrType"),
    (0, "TIMETRA-NAT-MIB", "tmnxNatDestAddr"),
    (0, "TIMETRA-NAT-MIB", "tmnxNatDestPrefixLen"),
)
if mibBuilder.loadTexts:
    tmnxNatDestEntry.setStatus("current")
_TmnxNatDestAddrType_Type = InetAddressType
_TmnxNatDestAddrType_Object = MibTableColumn
tmnxNatDestAddrType = _TmnxNatDestAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 5, 1, 1, 1),
    _TmnxNatDestAddrType_Type()
)
tmnxNatDestAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxNatDestAddrType.setStatus("current")


class _TmnxNatDestAddr_Type(InetAddress):
    """Custom type tmnxNatDestAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxNatDestAddr_Type.__name__ = "InetAddress"
_TmnxNatDestAddr_Object = MibTableColumn
tmnxNatDestAddr = _TmnxNatDestAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 5, 1, 1, 2),
    _TmnxNatDestAddr_Type()
)
tmnxNatDestAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxNatDestAddr.setStatus("current")


class _TmnxNatDestPrefixLen_Type(InetAddressPrefixLength):
    """Custom type tmnxNatDestPrefixLen based on InetAddressPrefixLength"""
    subtypeSpec = InetAddressPrefixLength.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_TmnxNatDestPrefixLen_Type.__name__ = "InetAddressPrefixLength"
_TmnxNatDestPrefixLen_Object = MibTableColumn
tmnxNatDestPrefixLen = _TmnxNatDestPrefixLen_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 5, 1, 1, 3),
    _TmnxNatDestPrefixLen_Type()
)
tmnxNatDestPrefixLen.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxNatDestPrefixLen.setStatus("current")
_TmnxNatDestRowStatus_Type = RowStatus
_TmnxNatDestRowStatus_Object = MibTableColumn
tmnxNatDestRowStatus = _TmnxNatDestRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 5, 1, 1, 4),
    _TmnxNatDestRowStatus_Type()
)
tmnxNatDestRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxNatDestRowStatus.setStatus("current")
_TmnxNatDestLastMgmtChange_Type = TimeStamp
_TmnxNatDestLastMgmtChange_Object = MibTableColumn
tmnxNatDestLastMgmtChange = _TmnxNatDestLastMgmtChange_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 5, 1, 1, 5),
    _TmnxNatDestLastMgmtChange_Type()
)
tmnxNatDestLastMgmtChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatDestLastMgmtChange.setStatus("current")


class _TmnxNatDestNatPolicy_Type(TNamedItemOrEmpty):
    """Custom type tmnxNatDestNatPolicy based on TNamedItemOrEmpty"""
    defaultValue = OctetString("")


_TmnxNatDestNatPolicy_Type.__name__ = "TNamedItemOrEmpty"
_TmnxNatDestNatPolicy_Object = MibTableColumn
tmnxNatDestNatPolicy = _TmnxNatDestNatPolicy_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 5, 1, 1, 10),
    _TmnxNatDestNatPolicy_Type()
)
tmnxNatDestNatPolicy.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxNatDestNatPolicy.setStatus("current")
_TmnxNatDsliteAddrTable_Object = MibTable
tmnxNatDsliteAddrTable = _TmnxNatDsliteAddrTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 5, 2)
)
if mibBuilder.loadTexts:
    tmnxNatDsliteAddrTable.setStatus("current")
_TmnxNatDsliteAddrEntry_Object = MibTableRow
tmnxNatDsliteAddrEntry = _TmnxNatDsliteAddrEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 5, 2, 1)
)
tmnxNatDsliteAddrEntry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "TIMETRA-NAT-MIB", "tmnxNatDsliteAddrType"),
    (0, "TIMETRA-NAT-MIB", "tmnxNatDsliteAddr"),
)
if mibBuilder.loadTexts:
    tmnxNatDsliteAddrEntry.setStatus("current")
_TmnxNatDsliteAddrType_Type = InetAddressType
_TmnxNatDsliteAddrType_Object = MibTableColumn
tmnxNatDsliteAddrType = _TmnxNatDsliteAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 5, 2, 1, 1),
    _TmnxNatDsliteAddrType_Type()
)
tmnxNatDsliteAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxNatDsliteAddrType.setStatus("current")


class _TmnxNatDsliteAddr_Type(InetAddress):
    """Custom type tmnxNatDsliteAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxNatDsliteAddr_Type.__name__ = "InetAddress"
_TmnxNatDsliteAddr_Object = MibTableColumn
tmnxNatDsliteAddr = _TmnxNatDsliteAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 5, 2, 1, 2),
    _TmnxNatDsliteAddr_Type()
)
tmnxNatDsliteAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxNatDsliteAddr.setStatus("current")
_TmnxNatDsliteAddrRowStatus_Type = RowStatus
_TmnxNatDsliteAddrRowStatus_Object = MibTableColumn
tmnxNatDsliteAddrRowStatus = _TmnxNatDsliteAddrRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 5, 2, 1, 4),
    _TmnxNatDsliteAddrRowStatus_Type()
)
tmnxNatDsliteAddrRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxNatDsliteAddrRowStatus.setStatus("current")
_TmnxNatDsliteAddrLastMgmtChange_Type = TimeStamp
_TmnxNatDsliteAddrLastMgmtChange_Object = MibTableColumn
tmnxNatDsliteAddrLastMgmtChange = _TmnxNatDsliteAddrLastMgmtChange_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 5, 2, 1, 5),
    _TmnxNatDsliteAddrLastMgmtChange_Type()
)
tmnxNatDsliteAddrLastMgmtChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatDsliteAddrLastMgmtChange.setStatus("current")


class _TmnxNatDsliteAddrTunnelMtu_Type(Unsigned32):
    """Custom type tmnxNatDsliteAddrTunnelMtu based on Unsigned32"""
    defaultValue = 1500

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(464, 9212),
    )


_TmnxNatDsliteAddrTunnelMtu_Type.__name__ = "Unsigned32"
_TmnxNatDsliteAddrTunnelMtu_Object = MibTableColumn
tmnxNatDsliteAddrTunnelMtu = _TmnxNatDsliteAddrTunnelMtu_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 5, 2, 1, 6),
    _TmnxNatDsliteAddrTunnelMtu_Type()
)
tmnxNatDsliteAddrTunnelMtu.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxNatDsliteAddrTunnelMtu.setStatus("current")


class _TmnxNatDsliteAddrFragmentIp_Type(TmnxNatFragmentIpMode):
    """Custom type tmnxNatDsliteAddrFragmentIp based on TmnxNatFragmentIpMode"""
    defaultValue = 0


_TmnxNatDsliteAddrFragmentIp_Type.__name__ = "TmnxNatFragmentIpMode"
_TmnxNatDsliteAddrFragmentIp_Object = MibTableColumn
tmnxNatDsliteAddrFragmentIp = _TmnxNatDsliteAddrFragmentIp_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 5, 2, 1, 7),
    _TmnxNatDsliteAddrFragmentIp_Type()
)
tmnxNatDsliteAddrFragmentIp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxNatDsliteAddrFragmentIp.setStatus("current")


class _TmnxNatDsliteAddrReassembly_Type(TruthValue):
    """Custom type tmnxNatDsliteAddrReassembly based on TruthValue"""
    defaultValue = 2


_TmnxNatDsliteAddrReassembly_Type.__name__ = "TruthValue"
_TmnxNatDsliteAddrReassembly_Object = MibTableColumn
tmnxNatDsliteAddrReassembly = _TmnxNatDsliteAddrReassembly_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 5, 2, 1, 8),
    _TmnxNatDsliteAddrReassembly_Type()
)
tmnxNatDsliteAddrReassembly.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxNatDsliteAddrReassembly.setStatus("current")


class _TmnxNatDsliteAddrMinFrstFrgSzRx_Type(Unsigned32):
    """Custom type tmnxNatDsliteAddrMinFrstFrgSzRx based on Unsigned32"""
    defaultValue = 1280

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(512, 1280),
    )


_TmnxNatDsliteAddrMinFrstFrgSzRx_Type.__name__ = "Unsigned32"
_TmnxNatDsliteAddrMinFrstFrgSzRx_Object = MibTableColumn
tmnxNatDsliteAddrMinFrstFrgSzRx = _TmnxNatDsliteAddrMinFrstFrgSzRx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 5, 2, 1, 9),
    _TmnxNatDsliteAddrMinFrstFrgSzRx_Type()
)
tmnxNatDsliteAddrMinFrstFrgSzRx.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxNatDsliteAddrMinFrstFrgSzRx.setStatus("current")
_TmnxNatInsideRoutesTable_Object = MibTable
tmnxNatInsideRoutesTable = _TmnxNatInsideRoutesTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 5, 4)
)
if mibBuilder.loadTexts:
    tmnxNatInsideRoutesTable.setStatus("current")
_TmnxNatInsideRoutesEntry_Object = MibTableRow
tmnxNatInsideRoutesEntry = _TmnxNatInsideRoutesEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 5, 4, 1)
)
tmnxNatInsideRoutesEntry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "TIMETRA-NAT-MIB", "tmnxNatInsideRoutesAddrType"),
    (0, "TIMETRA-NAT-MIB", "tmnxNatInsideRoutesAddr"),
    (0, "TIMETRA-NAT-MIB", "tmnxNatInsideRoutesPrefixLen"),
)
if mibBuilder.loadTexts:
    tmnxNatInsideRoutesEntry.setStatus("current")
_TmnxNatInsideRoutesAddrType_Type = InetAddressType
_TmnxNatInsideRoutesAddrType_Object = MibTableColumn
tmnxNatInsideRoutesAddrType = _TmnxNatInsideRoutesAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 5, 4, 1, 1),
    _TmnxNatInsideRoutesAddrType_Type()
)
tmnxNatInsideRoutesAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxNatInsideRoutesAddrType.setStatus("current")


class _TmnxNatInsideRoutesAddr_Type(InetAddress):
    """Custom type tmnxNatInsideRoutesAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxNatInsideRoutesAddr_Type.__name__ = "InetAddress"
_TmnxNatInsideRoutesAddr_Object = MibTableColumn
tmnxNatInsideRoutesAddr = _TmnxNatInsideRoutesAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 5, 4, 1, 2),
    _TmnxNatInsideRoutesAddr_Type()
)
tmnxNatInsideRoutesAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxNatInsideRoutesAddr.setStatus("current")


class _TmnxNatInsideRoutesPrefixLen_Type(InetAddressPrefixLength):
    """Custom type tmnxNatInsideRoutesPrefixLen based on InetAddressPrefixLength"""
    subtypeSpec = InetAddressPrefixLength.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_TmnxNatInsideRoutesPrefixLen_Type.__name__ = "InetAddressPrefixLength"
_TmnxNatInsideRoutesPrefixLen_Object = MibTableColumn
tmnxNatInsideRoutesPrefixLen = _TmnxNatInsideRoutesPrefixLen_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 5, 4, 1, 3),
    _TmnxNatInsideRoutesPrefixLen_Type()
)
tmnxNatInsideRoutesPrefixLen.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxNatInsideRoutesPrefixLen.setStatus("current")
_TmnxNatInsideRoutesNatPolicy_Type = TNamedItemOrEmpty
_TmnxNatInsideRoutesNatPolicy_Object = MibTableColumn
tmnxNatInsideRoutesNatPolicy = _TmnxNatInsideRoutesNatPolicy_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 5, 4, 1, 4),
    _TmnxNatInsideRoutesNatPolicy_Type()
)
tmnxNatInsideRoutesNatPolicy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatInsideRoutesNatPolicy.setStatus("current")
_TmnxNatInsideRoutesType_Type = TmnxNatInsideRoutesType
_TmnxNatInsideRoutesType_Object = MibTableColumn
tmnxNatInsideRoutesType = _TmnxNatInsideRoutesType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 5, 4, 1, 5),
    _TmnxNatInsideRoutesType_Type()
)
tmnxNatInsideRoutesType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatInsideRoutesType.setStatus("current")
_TmnxNatSubObjs_ObjectIdentity = ObjectIdentity
tmnxNatSubObjs = _TmnxNatSubObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 6)
)
_TmnxNatLsnHostTable_Object = MibTable
tmnxNatLsnHostTable = _TmnxNatLsnHostTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 6, 1)
)
if mibBuilder.loadTexts:
    tmnxNatLsnHostTable.setStatus("obsolete")
_TmnxNatLsnHostEntry_Object = MibTableRow
tmnxNatLsnHostEntry = _TmnxNatLsnHostEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 6, 1, 1)
)
tmnxNatLsnHostEntry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "TIMETRA-NAT-MIB", "tmnxNatLsnHostAddrType"),
    (0, "TIMETRA-NAT-MIB", "tmnxNatLsnHostAddr"),
)
if mibBuilder.loadTexts:
    tmnxNatLsnHostEntry.setStatus("obsolete")
_TmnxNatLsnHostAddrType_Type = InetAddressType
_TmnxNatLsnHostAddrType_Object = MibTableColumn
tmnxNatLsnHostAddrType = _TmnxNatLsnHostAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 6, 1, 1, 1),
    _TmnxNatLsnHostAddrType_Type()
)
tmnxNatLsnHostAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxNatLsnHostAddrType.setStatus("obsolete")


class _TmnxNatLsnHostAddr_Type(InetAddress):
    """Custom type tmnxNatLsnHostAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxNatLsnHostAddr_Type.__name__ = "InetAddress"
_TmnxNatLsnHostAddr_Object = MibTableColumn
tmnxNatLsnHostAddr = _TmnxNatLsnHostAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 6, 1, 1, 2),
    _TmnxNatLsnHostAddr_Type()
)
tmnxNatLsnHostAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxNatLsnHostAddr.setStatus("obsolete")
_TmnxNatLsnHostSubId_Type = Unsigned32
_TmnxNatLsnHostSubId_Object = MibTableColumn
tmnxNatLsnHostSubId = _TmnxNatLsnHostSubId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 6, 1, 1, 3),
    _TmnxNatLsnHostSubId_Type()
)
tmnxNatLsnHostSubId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatLsnHostSubId.setStatus("obsolete")
_TmnxNatLsnHostOutVRtrID_Type = TmnxVRtrID
_TmnxNatLsnHostOutVRtrID_Object = MibTableColumn
tmnxNatLsnHostOutVRtrID = _TmnxNatLsnHostOutVRtrID_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 6, 1, 1, 4),
    _TmnxNatLsnHostOutVRtrID_Type()
)
tmnxNatLsnHostOutVRtrID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatLsnHostOutVRtrID.setStatus("obsolete")
_TmnxNatLsnHostOutAddrType_Type = InetAddressType
_TmnxNatLsnHostOutAddrType_Object = MibTableColumn
tmnxNatLsnHostOutAddrType = _TmnxNatLsnHostOutAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 6, 1, 1, 5),
    _TmnxNatLsnHostOutAddrType_Type()
)
tmnxNatLsnHostOutAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatLsnHostOutAddrType.setStatus("obsolete")


class _TmnxNatLsnHostOutAddr_Type(InetAddress):
    """Custom type tmnxNatLsnHostOutAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxNatLsnHostOutAddr_Type.__name__ = "InetAddress"
_TmnxNatLsnHostOutAddr_Object = MibTableColumn
tmnxNatLsnHostOutAddr = _TmnxNatLsnHostOutAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 6, 1, 1, 6),
    _TmnxNatLsnHostOutAddr_Type()
)
tmnxNatLsnHostOutAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatLsnHostOutAddr.setStatus("obsolete")
_TmnxNatLsnSubTable_Object = MibTable
tmnxNatLsnSubTable = _TmnxNatLsnSubTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 6, 2)
)
if mibBuilder.loadTexts:
    tmnxNatLsnSubTable.setStatus("obsolete")
_TmnxNatLsnSubEntry_Object = MibTableRow
tmnxNatLsnSubEntry = _TmnxNatLsnSubEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 6, 2, 1)
)
tmnxNatLsnSubEntry.setIndexNames(
    (0, "TIMETRA-NAT-MIB", "tmnxNatLsnSubId"),
)
if mibBuilder.loadTexts:
    tmnxNatLsnSubEntry.setStatus("obsolete")
_TmnxNatLsnSubId_Type = Unsigned32
_TmnxNatLsnSubId_Object = MibTableColumn
tmnxNatLsnSubId = _TmnxNatLsnSubId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 6, 2, 1, 1),
    _TmnxNatLsnSubId_Type()
)
tmnxNatLsnSubId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxNatLsnSubId.setStatus("obsolete")
_TmnxNatLsnSubPolicy_Type = TNamedItem
_TmnxNatLsnSubPolicy_Object = MibTableColumn
tmnxNatLsnSubPolicy = _TmnxNatLsnSubPolicy_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 6, 2, 1, 2),
    _TmnxNatLsnSubPolicy_Type()
)
tmnxNatLsnSubPolicy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatLsnSubPolicy.setStatus("obsolete")
_TmnxNatLsnSubIsaGrp_Type = TmnxNatIsaGrpIdOrZero
_TmnxNatLsnSubIsaGrp_Object = MibTableColumn
tmnxNatLsnSubIsaGrp = _TmnxNatLsnSubIsaGrp_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 6, 2, 1, 3),
    _TmnxNatLsnSubIsaGrp_Type()
)
tmnxNatLsnSubIsaGrp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatLsnSubIsaGrp.setStatus("obsolete")
_TmnxNatLsnSubIsaMemberId_Type = Unsigned32
_TmnxNatLsnSubIsaMemberId_Object = MibTableColumn
tmnxNatLsnSubIsaMemberId = _TmnxNatLsnSubIsaMemberId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 6, 2, 1, 4),
    _TmnxNatLsnSubIsaMemberId_Type()
)
tmnxNatLsnSubIsaMemberId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatLsnSubIsaMemberId.setStatus("obsolete")
_TmnxNatLsnSubOutVRtrID_Type = TmnxVRtrIDOrZero
_TmnxNatLsnSubOutVRtrID_Object = MibTableColumn
tmnxNatLsnSubOutVRtrID = _TmnxNatLsnSubOutVRtrID_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 6, 2, 1, 5),
    _TmnxNatLsnSubOutVRtrID_Type()
)
tmnxNatLsnSubOutVRtrID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatLsnSubOutVRtrID.setStatus("obsolete")
_TmnxNatLsnSubOutAddrType_Type = InetAddressType
_TmnxNatLsnSubOutAddrType_Object = MibTableColumn
tmnxNatLsnSubOutAddrType = _TmnxNatLsnSubOutAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 6, 2, 1, 6),
    _TmnxNatLsnSubOutAddrType_Type()
)
tmnxNatLsnSubOutAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatLsnSubOutAddrType.setStatus("obsolete")


class _TmnxNatLsnSubOutAddr_Type(InetAddress):
    """Custom type tmnxNatLsnSubOutAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxNatLsnSubOutAddr_Type.__name__ = "InetAddress"
_TmnxNatLsnSubOutAddr_Object = MibTableColumn
tmnxNatLsnSubOutAddr = _TmnxNatLsnSubOutAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 6, 2, 1, 7),
    _TmnxNatLsnSubOutAddr_Type()
)
tmnxNatLsnSubOutAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatLsnSubOutAddr.setStatus("obsolete")
_TmnxNatLsnSubIdStr_Type = TmnxNatSubscriberIdString
_TmnxNatLsnSubIdStr_Object = MibTableColumn
tmnxNatLsnSubIdStr = _TmnxNatLsnSubIdStr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 6, 2, 1, 8),
    _TmnxNatLsnSubIdStr_Type()
)
tmnxNatLsnSubIdStr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatLsnSubIdStr.setStatus("obsolete")
_TmnxNatLsnSubStatTable_Object = MibTable
tmnxNatLsnSubStatTable = _TmnxNatLsnSubStatTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 6, 3)
)
if mibBuilder.loadTexts:
    tmnxNatLsnSubStatTable.setStatus("obsolete")
_TmnxNatLsnSubStatEntry_Object = MibTableRow
tmnxNatLsnSubStatEntry = _TmnxNatLsnSubStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 6, 3, 1)
)
if mibBuilder.loadTexts:
    tmnxNatLsnSubStatEntry.setStatus("obsolete")
_TmnxNatLsnSubStatIcmpPortUsage_Type = TmnxNatUsageLevel
_TmnxNatLsnSubStatIcmpPortUsage_Object = MibTableColumn
tmnxNatLsnSubStatIcmpPortUsage = _TmnxNatLsnSubStatIcmpPortUsage_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 6, 3, 1, 3),
    _TmnxNatLsnSubStatIcmpPortUsage_Type()
)
tmnxNatLsnSubStatIcmpPortUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatLsnSubStatIcmpPortUsage.setStatus("obsolete")
_TmnxNatLsnSubStatIcmpPortUsageHi_Type = TruthValue
_TmnxNatLsnSubStatIcmpPortUsageHi_Object = MibTableColumn
tmnxNatLsnSubStatIcmpPortUsageHi = _TmnxNatLsnSubStatIcmpPortUsageHi_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 6, 3, 1, 4),
    _TmnxNatLsnSubStatIcmpPortUsageHi_Type()
)
tmnxNatLsnSubStatIcmpPortUsageHi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatLsnSubStatIcmpPortUsageHi.setStatus("obsolete")
_TmnxNatLsnSubStatUdpPortUsage_Type = TmnxNatUsageLevel
_TmnxNatLsnSubStatUdpPortUsage_Object = MibTableColumn
tmnxNatLsnSubStatUdpPortUsage = _TmnxNatLsnSubStatUdpPortUsage_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 6, 3, 1, 5),
    _TmnxNatLsnSubStatUdpPortUsage_Type()
)
tmnxNatLsnSubStatUdpPortUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatLsnSubStatUdpPortUsage.setStatus("obsolete")
_TmnxNatLsnSubStatUdpPortUsageHi_Type = TruthValue
_TmnxNatLsnSubStatUdpPortUsageHi_Object = MibTableColumn
tmnxNatLsnSubStatUdpPortUsageHi = _TmnxNatLsnSubStatUdpPortUsageHi_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 6, 3, 1, 6),
    _TmnxNatLsnSubStatUdpPortUsageHi_Type()
)
tmnxNatLsnSubStatUdpPortUsageHi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatLsnSubStatUdpPortUsageHi.setStatus("obsolete")
_TmnxNatLsnSubStatTcpPortUsage_Type = TmnxNatUsageLevel
_TmnxNatLsnSubStatTcpPortUsage_Object = MibTableColumn
tmnxNatLsnSubStatTcpPortUsage = _TmnxNatLsnSubStatTcpPortUsage_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 6, 3, 1, 7),
    _TmnxNatLsnSubStatTcpPortUsage_Type()
)
tmnxNatLsnSubStatTcpPortUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatLsnSubStatTcpPortUsage.setStatus("obsolete")
_TmnxNatLsnSubStatTcpPortUsageHi_Type = TruthValue
_TmnxNatLsnSubStatTcpPortUsageHi_Object = MibTableColumn
tmnxNatLsnSubStatTcpPortUsageHi = _TmnxNatLsnSubStatTcpPortUsageHi_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 6, 3, 1, 8),
    _TmnxNatLsnSubStatTcpPortUsageHi_Type()
)
tmnxNatLsnSubStatTcpPortUsageHi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatLsnSubStatTcpPortUsageHi.setStatus("obsolete")
_TmnxNatLsnSubStatSessionUsage_Type = TmnxNatUsageLevel
_TmnxNatLsnSubStatSessionUsage_Object = MibTableColumn
tmnxNatLsnSubStatSessionUsage = _TmnxNatLsnSubStatSessionUsage_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 6, 3, 1, 9),
    _TmnxNatLsnSubStatSessionUsage_Type()
)
tmnxNatLsnSubStatSessionUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatLsnSubStatSessionUsage.setStatus("obsolete")
_TmnxNatLsnSubStatSessionUsageHi_Type = TruthValue
_TmnxNatLsnSubStatSessionUsageHi_Object = MibTableColumn
tmnxNatLsnSubStatSessionUsageHi = _TmnxNatLsnSubStatSessionUsageHi_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 6, 3, 1, 10),
    _TmnxNatLsnSubStatSessionUsageHi_Type()
)
tmnxNatLsnSubStatSessionUsageHi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatLsnSubStatSessionUsageHi.setStatus("obsolete")
_TmnxNatLsnSubStatSessions_Type = Gauge32
_TmnxNatLsnSubStatSessions_Object = MibTableColumn
tmnxNatLsnSubStatSessions = _TmnxNatLsnSubStatSessions_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 6, 3, 1, 11),
    _TmnxNatLsnSubStatSessions_Type()
)
tmnxNatLsnSubStatSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatLsnSubStatSessions.setStatus("obsolete")
_TmnxNatLsnSubStatSessionsPrio_Type = Gauge32
_TmnxNatLsnSubStatSessionsPrio_Object = MibTableColumn
tmnxNatLsnSubStatSessionsPrio = _TmnxNatLsnSubStatSessionsPrio_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 6, 3, 1, 12),
    _TmnxNatLsnSubStatSessionsPrio_Type()
)
tmnxNatLsnSubStatSessionsPrio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatLsnSubStatSessionsPrio.setStatus("obsolete")
_TmnxNatLsnSubStatSessionsPeak_Type = Gauge32
_TmnxNatLsnSubStatSessionsPeak_Object = MibTableColumn
tmnxNatLsnSubStatSessionsPeak = _TmnxNatLsnSubStatSessionsPeak_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 6, 3, 1, 13),
    _TmnxNatLsnSubStatSessionsPeak_Type()
)
tmnxNatLsnSubStatSessionsPeak.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatLsnSubStatSessionsPeak.setStatus("obsolete")
_TmnxNatLsnSubBlkTable_Object = MibTable
tmnxNatLsnSubBlkTable = _TmnxNatLsnSubBlkTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 6, 4)
)
if mibBuilder.loadTexts:
    tmnxNatLsnSubBlkTable.setStatus("current")
_TmnxNatLsnSubBlkEntry_Object = MibTableRow
tmnxNatLsnSubBlkEntry = _TmnxNatLsnSubBlkEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 6, 4, 1)
)
tmnxNatLsnSubBlkEntry.setIndexNames(
    (0, "TIMETRA-NAT-MIB", "tmnxNatQryLsnSubResId"),
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "TIMETRA-NAT-MIB", "tmnxNatBlkLsnAddrType"),
    (0, "TIMETRA-NAT-MIB", "tmnxNatBlkLsnAddr"),
    (0, "TIMETRA-NAT-MIB", "tmnxNatBlkLsnStart"),
)
if mibBuilder.loadTexts:
    tmnxNatLsnSubBlkEntry.setStatus("current")
_TmnxNatLsnSubBlkEnd_Type = InetPortNumber
_TmnxNatLsnSubBlkEnd_Object = MibTableColumn
tmnxNatLsnSubBlkEnd = _TmnxNatLsnSubBlkEnd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 6, 4, 1, 1),
    _TmnxNatLsnSubBlkEnd_Type()
)
tmnxNatLsnSubBlkEnd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatLsnSubBlkEnd.setStatus("current")
_TmnxNatLsnSubBlkPolicy_Type = TNamedItemOrEmpty
_TmnxNatLsnSubBlkPolicy_Object = MibTableColumn
tmnxNatLsnSubBlkPolicy = _TmnxNatLsnSubBlkPolicy_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 6, 4, 1, 2),
    _TmnxNatLsnSubBlkPolicy_Type()
)
tmnxNatLsnSubBlkPolicy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatLsnSubBlkPolicy.setStatus("current")
_TmnxNatDsliteSubTable_Object = MibTable
tmnxNatDsliteSubTable = _TmnxNatDsliteSubTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 6, 5)
)
if mibBuilder.loadTexts:
    tmnxNatDsliteSubTable.setStatus("obsolete")
_TmnxNatDsliteSubEntry_Object = MibTableRow
tmnxNatDsliteSubEntry = _TmnxNatDsliteSubEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 6, 5, 1)
)
tmnxNatDsliteSubEntry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "TIMETRA-NAT-MIB", "tmnxNatDsliteSubAddrType"),
    (0, "TIMETRA-NAT-MIB", "tmnxNatDsliteSubAddr"),
    (0, "TIMETRA-NAT-MIB", "tmnxNatDsliteSubAddrPrefixLength"),
)
if mibBuilder.loadTexts:
    tmnxNatDsliteSubEntry.setStatus("obsolete")
_TmnxNatDsliteSubAddrType_Type = InetAddressType
_TmnxNatDsliteSubAddrType_Object = MibTableColumn
tmnxNatDsliteSubAddrType = _TmnxNatDsliteSubAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 6, 5, 1, 1),
    _TmnxNatDsliteSubAddrType_Type()
)
tmnxNatDsliteSubAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxNatDsliteSubAddrType.setStatus("obsolete")


class _TmnxNatDsliteSubAddr_Type(InetAddress):
    """Custom type tmnxNatDsliteSubAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )
    fixed_length = 16


_TmnxNatDsliteSubAddr_Type.__name__ = "InetAddress"
_TmnxNatDsliteSubAddr_Object = MibTableColumn
tmnxNatDsliteSubAddr = _TmnxNatDsliteSubAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 6, 5, 1, 2),
    _TmnxNatDsliteSubAddr_Type()
)
tmnxNatDsliteSubAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxNatDsliteSubAddr.setStatus("obsolete")


class _TmnxNatDsliteSubAddrPrefixLength_Type(InetAddressPrefixLength):
    """Custom type tmnxNatDsliteSubAddrPrefixLength based on InetAddressPrefixLength"""
    subtypeSpec = InetAddressPrefixLength.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 128),
    )


_TmnxNatDsliteSubAddrPrefixLength_Type.__name__ = "InetAddressPrefixLength"
_TmnxNatDsliteSubAddrPrefixLength_Object = MibTableColumn
tmnxNatDsliteSubAddrPrefixLength = _TmnxNatDsliteSubAddrPrefixLength_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 6, 5, 1, 3),
    _TmnxNatDsliteSubAddrPrefixLength_Type()
)
tmnxNatDsliteSubAddrPrefixLength.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxNatDsliteSubAddrPrefixLength.setStatus("obsolete")
_TmnxNatDsliteSubId_Type = Unsigned32
_TmnxNatDsliteSubId_Object = MibTableColumn
tmnxNatDsliteSubId = _TmnxNatDsliteSubId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 6, 5, 1, 4),
    _TmnxNatDsliteSubId_Type()
)
tmnxNatDsliteSubId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatDsliteSubId.setStatus("obsolete")
_TmnxNatL2AwHostTable_Object = MibTable
tmnxNatL2AwHostTable = _TmnxNatL2AwHostTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 6, 11)
)
if mibBuilder.loadTexts:
    tmnxNatL2AwHostTable.setStatus("current")
_TmnxNatL2AwHostEntry_Object = MibTableRow
tmnxNatL2AwHostEntry = _TmnxNatL2AwHostEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 6, 11, 1)
)
tmnxNatL2AwHostEntry.setIndexNames(
    (0, "TIMETRA-SUBSCRIBER-MGMT-MIB", "tmnxSubInfoSubIdent"),
    (0, "TIMETRA-NAT-MIB", "tmnxNatL2AwHostAddrType"),
    (0, "TIMETRA-NAT-MIB", "tmnxNatL2AwHostAddr"),
)
if mibBuilder.loadTexts:
    tmnxNatL2AwHostEntry.setStatus("current")
_TmnxNatL2AwHostAddrType_Type = InetAddressType
_TmnxNatL2AwHostAddrType_Object = MibTableColumn
tmnxNatL2AwHostAddrType = _TmnxNatL2AwHostAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 6, 11, 1, 1),
    _TmnxNatL2AwHostAddrType_Type()
)
tmnxNatL2AwHostAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxNatL2AwHostAddrType.setStatus("current")


class _TmnxNatL2AwHostAddr_Type(InetAddress):
    """Custom type tmnxNatL2AwHostAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxNatL2AwHostAddr_Type.__name__ = "InetAddress"
_TmnxNatL2AwHostAddr_Object = MibTableColumn
tmnxNatL2AwHostAddr = _TmnxNatL2AwHostAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 6, 11, 1, 2),
    _TmnxNatL2AwHostAddr_Type()
)
tmnxNatL2AwHostAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxNatL2AwHostAddr.setStatus("current")
_TmnxNatL2AwHostOutVRtrID_Type = TmnxVRtrIDOrZero
_TmnxNatL2AwHostOutVRtrID_Object = MibTableColumn
tmnxNatL2AwHostOutVRtrID = _TmnxNatL2AwHostOutVRtrID_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 6, 11, 1, 3),
    _TmnxNatL2AwHostOutVRtrID_Type()
)
tmnxNatL2AwHostOutVRtrID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatL2AwHostOutVRtrID.setStatus("current")
_TmnxNatL2AwHostOutAddrType_Type = InetAddressType
_TmnxNatL2AwHostOutAddrType_Object = MibTableColumn
tmnxNatL2AwHostOutAddrType = _TmnxNatL2AwHostOutAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 6, 11, 1, 4),
    _TmnxNatL2AwHostOutAddrType_Type()
)
tmnxNatL2AwHostOutAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatL2AwHostOutAddrType.setStatus("current")


class _TmnxNatL2AwHostOutAddr_Type(InetAddress):
    """Custom type tmnxNatL2AwHostOutAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxNatL2AwHostOutAddr_Type.__name__ = "InetAddress"
_TmnxNatL2AwHostOutAddr_Object = MibTableColumn
tmnxNatL2AwHostOutAddr = _TmnxNatL2AwHostOutAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 6, 11, 1, 5),
    _TmnxNatL2AwHostOutAddr_Type()
)
tmnxNatL2AwHostOutAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatL2AwHostOutAddr.setStatus("current")
_TmnxNatL2AwHostOutStart_Type = InetPortNumber
_TmnxNatL2AwHostOutStart_Object = MibTableColumn
tmnxNatL2AwHostOutStart = _TmnxNatL2AwHostOutStart_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 6, 11, 1, 6),
    _TmnxNatL2AwHostOutStart_Type()
)
tmnxNatL2AwHostOutStart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatL2AwHostOutStart.setStatus("current")
_TmnxNatL2AwSubTable_Object = MibTable
tmnxNatL2AwSubTable = _TmnxNatL2AwSubTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 6, 12)
)
if mibBuilder.loadTexts:
    tmnxNatL2AwSubTable.setStatus("current")
_TmnxNatL2AwSubEntry_Object = MibTableRow
tmnxNatL2AwSubEntry = _TmnxNatL2AwSubEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 6, 12, 1)
)
tmnxNatL2AwSubEntry.setIndexNames(
    (1, "TIMETRA-SUBSCRIBER-MGMT-MIB", "tmnxSubInfoSubIdent"),
)
if mibBuilder.loadTexts:
    tmnxNatL2AwSubEntry.setStatus("current")
_TmnxNatL2AwSubPolicy_Type = TNamedItemOrEmpty
_TmnxNatL2AwSubPolicy_Object = MibTableColumn
tmnxNatL2AwSubPolicy = _TmnxNatL2AwSubPolicy_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 6, 12, 1, 1),
    _TmnxNatL2AwSubPolicy_Type()
)
tmnxNatL2AwSubPolicy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatL2AwSubPolicy.setStatus("current")
_TmnxNatL2AwSubIsaGrp_Type = TmnxNatIsaGrpIdOrZero
_TmnxNatL2AwSubIsaGrp_Object = MibTableColumn
tmnxNatL2AwSubIsaGrp = _TmnxNatL2AwSubIsaGrp_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 6, 12, 1, 2),
    _TmnxNatL2AwSubIsaGrp_Type()
)
tmnxNatL2AwSubIsaGrp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatL2AwSubIsaGrp.setStatus("current")
_TmnxNatL2AwSubIsaMemberId_Type = Unsigned32
_TmnxNatL2AwSubIsaMemberId_Object = MibTableColumn
tmnxNatL2AwSubIsaMemberId = _TmnxNatL2AwSubIsaMemberId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 6, 12, 1, 3),
    _TmnxNatL2AwSubIsaMemberId_Type()
)
tmnxNatL2AwSubIsaMemberId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatL2AwSubIsaMemberId.setStatus("current")
_TmnxNatL2AwSubOutVRtrID_Type = TmnxVRtrIDOrZero
_TmnxNatL2AwSubOutVRtrID_Object = MibTableColumn
tmnxNatL2AwSubOutVRtrID = _TmnxNatL2AwSubOutVRtrID_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 6, 12, 1, 4),
    _TmnxNatL2AwSubOutVRtrID_Type()
)
tmnxNatL2AwSubOutVRtrID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatL2AwSubOutVRtrID.setStatus("current")
_TmnxNatL2AwSubOutAddrType_Type = InetAddressType
_TmnxNatL2AwSubOutAddrType_Object = MibTableColumn
tmnxNatL2AwSubOutAddrType = _TmnxNatL2AwSubOutAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 6, 12, 1, 5),
    _TmnxNatL2AwSubOutAddrType_Type()
)
tmnxNatL2AwSubOutAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatL2AwSubOutAddrType.setStatus("current")


class _TmnxNatL2AwSubOutAddr_Type(InetAddress):
    """Custom type tmnxNatL2AwSubOutAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxNatL2AwSubOutAddr_Type.__name__ = "InetAddress"
_TmnxNatL2AwSubOutAddr_Object = MibTableColumn
tmnxNatL2AwSubOutAddr = _TmnxNatL2AwSubOutAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 6, 12, 1, 6),
    _TmnxNatL2AwSubOutAddr_Type()
)
tmnxNatL2AwSubOutAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatL2AwSubOutAddr.setStatus("current")
_TmnxNatL2AwSubCurrUpnpPlcy_Type = TNamedItemOrEmpty
_TmnxNatL2AwSubCurrUpnpPlcy_Object = MibTableColumn
tmnxNatL2AwSubCurrUpnpPlcy = _TmnxNatL2AwSubCurrUpnpPlcy_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 6, 12, 1, 7),
    _TmnxNatL2AwSubCurrUpnpPlcy_Type()
)
tmnxNatL2AwSubCurrUpnpPlcy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatL2AwSubCurrUpnpPlcy.setStatus("current")
_TmnxNatL2AwSubHostPortBlkSize_Type = Unsigned32
_TmnxNatL2AwSubHostPortBlkSize_Object = MibTableColumn
tmnxNatL2AwSubHostPortBlkSize = _TmnxNatL2AwSubHostPortBlkSize_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 6, 12, 1, 8),
    _TmnxNatL2AwSubHostPortBlkSize_Type()
)
tmnxNatL2AwSubHostPortBlkSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatL2AwSubHostPortBlkSize.setStatus("current")
_TmnxNatL2AwSubFirewallPolicy_Type = TNamedItemOrEmpty
_TmnxNatL2AwSubFirewallPolicy_Object = MibTableColumn
tmnxNatL2AwSubFirewallPolicy = _TmnxNatL2AwSubFirewallPolicy_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 6, 12, 1, 9),
    _TmnxNatL2AwSubFirewallPolicy_Type()
)
tmnxNatL2AwSubFirewallPolicy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatL2AwSubFirewallPolicy.setStatus("current")
_TmnxNatL2AwSubStatTable_Object = MibTable
tmnxNatL2AwSubStatTable = _TmnxNatL2AwSubStatTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 6, 13)
)
if mibBuilder.loadTexts:
    tmnxNatL2AwSubStatTable.setStatus("current")
_TmnxNatL2AwSubStatEntry_Object = MibTableRow
tmnxNatL2AwSubStatEntry = _TmnxNatL2AwSubStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 6, 13, 1)
)
tmnxNatL2AwSubStatEntry.setIndexNames(
    (0, "TIMETRA-SUBSCRIBER-MGMT-MIB", "tmnxSubInfoSubIdent"),
    (1, "TIMETRA-NAT-MIB", "tmnxNatL2AwSubStatNatPolicy"),
)
if mibBuilder.loadTexts:
    tmnxNatL2AwSubStatEntry.setStatus("current")
_TmnxNatL2AwSubStatNatPolicy_Type = TNamedItem
_TmnxNatL2AwSubStatNatPolicy_Object = MibTableColumn
tmnxNatL2AwSubStatNatPolicy = _TmnxNatL2AwSubStatNatPolicy_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 6, 13, 1, 2),
    _TmnxNatL2AwSubStatNatPolicy_Type()
)
tmnxNatL2AwSubStatNatPolicy.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxNatL2AwSubStatNatPolicy.setStatus("current")
_TmnxNatL2AwSubStatIcmpPortUsage_Type = TmnxNatUsageLevel
_TmnxNatL2AwSubStatIcmpPortUsage_Object = MibTableColumn
tmnxNatL2AwSubStatIcmpPortUsage = _TmnxNatL2AwSubStatIcmpPortUsage_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 6, 13, 1, 3),
    _TmnxNatL2AwSubStatIcmpPortUsage_Type()
)
tmnxNatL2AwSubStatIcmpPortUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatL2AwSubStatIcmpPortUsage.setStatus("current")
_TmnxNatL2AwSubStatIcmpPortUsageH_Type = TruthValue
_TmnxNatL2AwSubStatIcmpPortUsageH_Object = MibTableColumn
tmnxNatL2AwSubStatIcmpPortUsageH = _TmnxNatL2AwSubStatIcmpPortUsageH_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 6, 13, 1, 4),
    _TmnxNatL2AwSubStatIcmpPortUsageH_Type()
)
tmnxNatL2AwSubStatIcmpPortUsageH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatL2AwSubStatIcmpPortUsageH.setStatus("current")
_TmnxNatL2AwSubStatUdpPortUsage_Type = TmnxNatUsageLevel
_TmnxNatL2AwSubStatUdpPortUsage_Object = MibTableColumn
tmnxNatL2AwSubStatUdpPortUsage = _TmnxNatL2AwSubStatUdpPortUsage_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 6, 13, 1, 5),
    _TmnxNatL2AwSubStatUdpPortUsage_Type()
)
tmnxNatL2AwSubStatUdpPortUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatL2AwSubStatUdpPortUsage.setStatus("current")
_TmnxNatL2AwSubStatUdpPortUsageHi_Type = TruthValue
_TmnxNatL2AwSubStatUdpPortUsageHi_Object = MibTableColumn
tmnxNatL2AwSubStatUdpPortUsageHi = _TmnxNatL2AwSubStatUdpPortUsageHi_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 6, 13, 1, 6),
    _TmnxNatL2AwSubStatUdpPortUsageHi_Type()
)
tmnxNatL2AwSubStatUdpPortUsageHi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatL2AwSubStatUdpPortUsageHi.setStatus("current")
_TmnxNatL2AwSubStatTcpPortUsage_Type = TmnxNatUsageLevel
_TmnxNatL2AwSubStatTcpPortUsage_Object = MibTableColumn
tmnxNatL2AwSubStatTcpPortUsage = _TmnxNatL2AwSubStatTcpPortUsage_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 6, 13, 1, 7),
    _TmnxNatL2AwSubStatTcpPortUsage_Type()
)
tmnxNatL2AwSubStatTcpPortUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatL2AwSubStatTcpPortUsage.setStatus("current")
_TmnxNatL2AwSubStatTcpPortUsageHi_Type = TruthValue
_TmnxNatL2AwSubStatTcpPortUsageHi_Object = MibTableColumn
tmnxNatL2AwSubStatTcpPortUsageHi = _TmnxNatL2AwSubStatTcpPortUsageHi_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 6, 13, 1, 8),
    _TmnxNatL2AwSubStatTcpPortUsageHi_Type()
)
tmnxNatL2AwSubStatTcpPortUsageHi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatL2AwSubStatTcpPortUsageHi.setStatus("current")
_TmnxNatL2AwSubStatSessionUsage_Type = TmnxNatUsageLevel
_TmnxNatL2AwSubStatSessionUsage_Object = MibTableColumn
tmnxNatL2AwSubStatSessionUsage = _TmnxNatL2AwSubStatSessionUsage_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 6, 13, 1, 9),
    _TmnxNatL2AwSubStatSessionUsage_Type()
)
tmnxNatL2AwSubStatSessionUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatL2AwSubStatSessionUsage.setStatus("current")
_TmnxNatL2AwSubStatSessionUsageHi_Type = TruthValue
_TmnxNatL2AwSubStatSessionUsageHi_Object = MibTableColumn
tmnxNatL2AwSubStatSessionUsageHi = _TmnxNatL2AwSubStatSessionUsageHi_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 6, 13, 1, 10),
    _TmnxNatL2AwSubStatSessionUsageHi_Type()
)
tmnxNatL2AwSubStatSessionUsageHi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatL2AwSubStatSessionUsageHi.setStatus("current")
_TmnxNatL2AwSubStatSessions_Type = Gauge32
_TmnxNatL2AwSubStatSessions_Object = MibTableColumn
tmnxNatL2AwSubStatSessions = _TmnxNatL2AwSubStatSessions_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 6, 13, 1, 11),
    _TmnxNatL2AwSubStatSessions_Type()
)
tmnxNatL2AwSubStatSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatL2AwSubStatSessions.setStatus("current")
_TmnxNatL2AwSubStatSessionsPrio_Type = Gauge32
_TmnxNatL2AwSubStatSessionsPrio_Object = MibTableColumn
tmnxNatL2AwSubStatSessionsPrio = _TmnxNatL2AwSubStatSessionsPrio_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 6, 13, 1, 12),
    _TmnxNatL2AwSubStatSessionsPrio_Type()
)
tmnxNatL2AwSubStatSessionsPrio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatL2AwSubStatSessionsPrio.setStatus("current")
_TmnxNatL2AwSubStatSessionsPeak_Type = Gauge32
_TmnxNatL2AwSubStatSessionsPeak_Object = MibTableColumn
tmnxNatL2AwSubStatSessionsPeak = _TmnxNatL2AwSubStatSessionsPeak_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 6, 13, 1, 13),
    _TmnxNatL2AwSubStatSessionsPeak_Type()
)
tmnxNatL2AwSubStatSessionsPeak.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatL2AwSubStatSessionsPeak.setStatus("current")
_TmnxNatL2AwSubStatCurrUpnpPlcy_Type = TNamedItemOrEmpty
_TmnxNatL2AwSubStatCurrUpnpPlcy_Object = MibTableColumn
tmnxNatL2AwSubStatCurrUpnpPlcy = _TmnxNatL2AwSubStatCurrUpnpPlcy_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 6, 13, 1, 14),
    _TmnxNatL2AwSubStatCurrUpnpPlcy_Type()
)
tmnxNatL2AwSubStatCurrUpnpPlcy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatL2AwSubStatCurrUpnpPlcy.setStatus("obsolete")
_TmnxNatL2AwSubStatPlcyPurpose_Type = TmnxNatPolicyPurpose
_TmnxNatL2AwSubStatPlcyPurpose_Object = MibTableColumn
tmnxNatL2AwSubStatPlcyPurpose = _TmnxNatL2AwSubStatPlcyPurpose_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 6, 13, 1, 15),
    _TmnxNatL2AwSubStatPlcyPurpose_Type()
)
tmnxNatL2AwSubStatPlcyPurpose.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatL2AwSubStatPlcyPurpose.setStatus("current")
_TmnxNatL2AwSubStatDownstreamDrop_Type = Counter64
_TmnxNatL2AwSubStatDownstreamDrop_Object = MibTableColumn
tmnxNatL2AwSubStatDownstreamDrop = _TmnxNatL2AwSubStatDownstreamDrop_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 6, 13, 1, 16),
    _TmnxNatL2AwSubStatDownstreamDrop_Type()
)
tmnxNatL2AwSubStatDownstreamDrop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatL2AwSubStatDownstreamDrop.setStatus("current")
_TmnxNatL2AwSubStatUnknHostDrop_Type = Counter64
_TmnxNatL2AwSubStatUnknHostDrop_Object = MibTableColumn
tmnxNatL2AwSubStatUnknHostDrop = _TmnxNatL2AwSubStatUnknHostDrop_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 6, 13, 1, 17),
    _TmnxNatL2AwSubStatUnknHostDrop_Type()
)
tmnxNatL2AwSubStatUnknHostDrop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatL2AwSubStatUnknHostDrop.setStatus("current")
_TmnxNatL2AwSubBlkTable_Object = MibTable
tmnxNatL2AwSubBlkTable = _TmnxNatL2AwSubBlkTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 6, 14)
)
if mibBuilder.loadTexts:
    tmnxNatL2AwSubBlkTable.setStatus("current")
_TmnxNatL2AwSubBlkEntry_Object = MibTableRow
tmnxNatL2AwSubBlkEntry = _TmnxNatL2AwSubBlkEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 6, 14, 1)
)
tmnxNatL2AwSubBlkEntry.setIndexNames(
    (0, "TIMETRA-SUBSCRIBER-MGMT-MIB", "tmnxSubInfoSubIdent"),
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "TIMETRA-NAT-MIB", "tmnxNatBlkL2AwAddrType"),
    (0, "TIMETRA-NAT-MIB", "tmnxNatBlkL2AwAddr"),
    (0, "TIMETRA-NAT-MIB", "tmnxNatBlkL2AwStart"),
)
if mibBuilder.loadTexts:
    tmnxNatL2AwSubBlkEntry.setStatus("current")
_TmnxNatL2AwSubBlkEnd_Type = InetPortNumber
_TmnxNatL2AwSubBlkEnd_Object = MibTableColumn
tmnxNatL2AwSubBlkEnd = _TmnxNatL2AwSubBlkEnd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 6, 14, 1, 1),
    _TmnxNatL2AwSubBlkEnd_Type()
)
tmnxNatL2AwSubBlkEnd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatL2AwSubBlkEnd.setStatus("current")
_TmnxNatL2AwSubBlkPolicy_Type = TNamedItemOrEmpty
_TmnxNatL2AwSubBlkPolicy_Object = MibTableColumn
tmnxNatL2AwSubBlkPolicy = _TmnxNatL2AwSubBlkPolicy_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 6, 14, 1, 2),
    _TmnxNatL2AwSubBlkPolicy_Type()
)
tmnxNatL2AwSubBlkPolicy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatL2AwSubBlkPolicy.setStatus("current")
_TmnxNat64SubTable_Object = MibTable
tmnxNat64SubTable = _TmnxNat64SubTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 6, 15)
)
if mibBuilder.loadTexts:
    tmnxNat64SubTable.setStatus("obsolete")
_TmnxNat64SubEntry_Object = MibTableRow
tmnxNat64SubEntry = _TmnxNat64SubEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 6, 15, 1)
)
tmnxNat64SubEntry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "TIMETRA-NAT-MIB", "tmnxNat64SubAddrType"),
    (0, "TIMETRA-NAT-MIB", "tmnxNat64SubAddr"),
    (0, "TIMETRA-NAT-MIB", "tmnxNat64SubAddrPrefixLength"),
)
if mibBuilder.loadTexts:
    tmnxNat64SubEntry.setStatus("obsolete")
_TmnxNat64SubAddrType_Type = InetAddressType
_TmnxNat64SubAddrType_Object = MibTableColumn
tmnxNat64SubAddrType = _TmnxNat64SubAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 6, 15, 1, 1),
    _TmnxNat64SubAddrType_Type()
)
tmnxNat64SubAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxNat64SubAddrType.setStatus("obsolete")


class _TmnxNat64SubAddr_Type(InetAddress):
    """Custom type tmnxNat64SubAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )
    fixed_length = 16


_TmnxNat64SubAddr_Type.__name__ = "InetAddress"
_TmnxNat64SubAddr_Object = MibTableColumn
tmnxNat64SubAddr = _TmnxNat64SubAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 6, 15, 1, 2),
    _TmnxNat64SubAddr_Type()
)
tmnxNat64SubAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxNat64SubAddr.setStatus("obsolete")


class _TmnxNat64SubAddrPrefixLength_Type(InetAddressPrefixLength):
    """Custom type tmnxNat64SubAddrPrefixLength based on InetAddressPrefixLength"""
    subtypeSpec = InetAddressPrefixLength.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 128),
    )


_TmnxNat64SubAddrPrefixLength_Type.__name__ = "InetAddressPrefixLength"
_TmnxNat64SubAddrPrefixLength_Object = MibTableColumn
tmnxNat64SubAddrPrefixLength = _TmnxNat64SubAddrPrefixLength_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 6, 15, 1, 3),
    _TmnxNat64SubAddrPrefixLength_Type()
)
tmnxNat64SubAddrPrefixLength.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxNat64SubAddrPrefixLength.setStatus("obsolete")
_TmnxNat64SubId_Type = Unsigned32
_TmnxNat64SubId_Object = MibTableColumn
tmnxNat64SubId = _TmnxNat64SubId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 6, 15, 1, 4),
    _TmnxNat64SubId_Type()
)
tmnxNat64SubId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNat64SubId.setStatus("obsolete")
_TmnxNatLsnSubscIdStrTable_Object = MibTable
tmnxNatLsnSubscIdStrTable = _TmnxNatLsnSubscIdStrTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 6, 16)
)
if mibBuilder.loadTexts:
    tmnxNatLsnSubscIdStrTable.setStatus("current")
_TmnxNatLsnSubscIdStrEntry_Object = MibTableRow
tmnxNatLsnSubscIdStrEntry = _TmnxNatLsnSubscIdStrEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 6, 16, 1)
)
tmnxNatLsnSubscIdStrEntry.setIndexNames(
    (0, "TIMETRA-NAT-MIB", "tmnxNatLsnSubscIdStr"),
    (0, "TIMETRA-NAT-MIB", "tmnxNatLsnSubscIdStrType"),
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "TIMETRA-NAT-MIB", "tmnxNatLsnSubscIdStrAddrType"),
    (0, "TIMETRA-NAT-MIB", "tmnxNatLsnSubscIdStrAddr"),
)
if mibBuilder.loadTexts:
    tmnxNatLsnSubscIdStrEntry.setStatus("current")


class _TmnxNatLsnSubscIdStr_Type(TmnxNatSubscriberIdString):
    """Custom type tmnxNatLsnSubscIdStr based on TmnxNatSubscriberIdString"""
    subtypeSpec = TmnxNatSubscriberIdString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_TmnxNatLsnSubscIdStr_Type.__name__ = "TmnxNatSubscriberIdString"
_TmnxNatLsnSubscIdStr_Object = MibTableColumn
tmnxNatLsnSubscIdStr = _TmnxNatLsnSubscIdStr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 6, 16, 1, 1),
    _TmnxNatLsnSubscIdStr_Type()
)
tmnxNatLsnSubscIdStr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxNatLsnSubscIdStr.setStatus("current")


class _TmnxNatLsnSubscIdStrType_Type(TmnxNatLegacySubscriberType):
    """Custom type tmnxNatLsnSubscIdStrType based on TmnxNatLegacySubscriberType"""
    subtypeSpec = TmnxNatLegacySubscriberType.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("classicLsnSub", 2),
          ("dsliteLsnSub", 3),
          ("nat64LsnSub", 4))
    )


_TmnxNatLsnSubscIdStrType_Type.__name__ = "TmnxNatLegacySubscriberType"
_TmnxNatLsnSubscIdStrType_Object = MibTableColumn
tmnxNatLsnSubscIdStrType = _TmnxNatLsnSubscIdStrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 6, 16, 1, 2),
    _TmnxNatLsnSubscIdStrType_Type()
)
tmnxNatLsnSubscIdStrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxNatLsnSubscIdStrType.setStatus("current")
_TmnxNatLsnSubscIdStrAddrType_Type = InetAddressType
_TmnxNatLsnSubscIdStrAddrType_Object = MibTableColumn
tmnxNatLsnSubscIdStrAddrType = _TmnxNatLsnSubscIdStrAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 6, 16, 1, 3),
    _TmnxNatLsnSubscIdStrAddrType_Type()
)
tmnxNatLsnSubscIdStrAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxNatLsnSubscIdStrAddrType.setStatus("current")


class _TmnxNatLsnSubscIdStrAddr_Type(InetAddress):
    """Custom type tmnxNatLsnSubscIdStrAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxNatLsnSubscIdStrAddr_Type.__name__ = "InetAddress"
_TmnxNatLsnSubscIdStrAddr_Object = MibTableColumn
tmnxNatLsnSubscIdStrAddr = _TmnxNatLsnSubscIdStrAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 6, 16, 1, 4),
    _TmnxNatLsnSubscIdStrAddr_Type()
)
tmnxNatLsnSubscIdStrAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxNatLsnSubscIdStrAddr.setStatus("current")
_TmnxNatLsnSubscIdStrTimeStamp_Type = TimeStamp
_TmnxNatLsnSubscIdStrTimeStamp_Object = MibTableColumn
tmnxNatLsnSubscIdStrTimeStamp = _TmnxNatLsnSubscIdStrTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 6, 16, 1, 5),
    _TmnxNatLsnSubscIdStrTimeStamp_Type()
)
tmnxNatLsnSubscIdStrTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatLsnSubscIdStrTimeStamp.setStatus("current")
_TmnxNatPrefixListTable_Object = MibTable
tmnxNatPrefixListTable = _TmnxNatPrefixListTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 6, 17)
)
if mibBuilder.loadTexts:
    tmnxNatPrefixListTable.setStatus("current")
_TmnxNatPrefixListEntry_Object = MibTableRow
tmnxNatPrefixListEntry = _TmnxNatPrefixListEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 6, 17, 1)
)
tmnxNatPrefixListEntry.setIndexNames(
    (1, "TIMETRA-NAT-MIB", "tmnxNatPrefixListName"),
)
if mibBuilder.loadTexts:
    tmnxNatPrefixListEntry.setStatus("current")
_TmnxNatPrefixListName_Type = TNamedItem
_TmnxNatPrefixListName_Object = MibTableColumn
tmnxNatPrefixListName = _TmnxNatPrefixListName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 6, 17, 1, 1),
    _TmnxNatPrefixListName_Type()
)
tmnxNatPrefixListName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxNatPrefixListName.setStatus("current")
_TmnxNatPrefixListRowStatus_Type = RowStatus
_TmnxNatPrefixListRowStatus_Object = MibTableColumn
tmnxNatPrefixListRowStatus = _TmnxNatPrefixListRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 6, 17, 1, 2),
    _TmnxNatPrefixListRowStatus_Type()
)
tmnxNatPrefixListRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxNatPrefixListRowStatus.setStatus("current")
_TmnxNatPrefixListLastMgmtChange_Type = TimeStamp
_TmnxNatPrefixListLastMgmtChange_Object = MibTableColumn
tmnxNatPrefixListLastMgmtChange = _TmnxNatPrefixListLastMgmtChange_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 6, 17, 1, 3),
    _TmnxNatPrefixListLastMgmtChange_Type()
)
tmnxNatPrefixListLastMgmtChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatPrefixListLastMgmtChange.setStatus("current")


class _TmnxNatPrefixListApplication_Type(Integer32):
    """Custom type tmnxNatPrefixListApplication based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("l2AwareDestToPolicy", 1),
          ("dnatOnlySubscribers", 2))
    )


_TmnxNatPrefixListApplication_Type.__name__ = "Integer32"
_TmnxNatPrefixListApplication_Object = MibTableColumn
tmnxNatPrefixListApplication = _TmnxNatPrefixListApplication_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 6, 17, 1, 4),
    _TmnxNatPrefixListApplication_Type()
)
tmnxNatPrefixListApplication.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxNatPrefixListApplication.setStatus("current")
_TmnxNatPrefixTable_Object = MibTable
tmnxNatPrefixTable = _TmnxNatPrefixTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 6, 18)
)
if mibBuilder.loadTexts:
    tmnxNatPrefixTable.setStatus("current")
_TmnxNatPrefixEntry_Object = MibTableRow
tmnxNatPrefixEntry = _TmnxNatPrefixEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 6, 18, 1)
)
tmnxNatPrefixEntry.setIndexNames(
    (0, "TIMETRA-NAT-MIB", "tmnxNatPrefixListName"),
    (0, "TIMETRA-NAT-MIB", "tmnxNatPrefixAddrType"),
    (0, "TIMETRA-NAT-MIB", "tmnxNatPrefixAddr"),
    (0, "TIMETRA-NAT-MIB", "tmnxNatPrefixPrefixLen"),
)
if mibBuilder.loadTexts:
    tmnxNatPrefixEntry.setStatus("current")
_TmnxNatPrefixAddrType_Type = InetAddressType
_TmnxNatPrefixAddrType_Object = MibTableColumn
tmnxNatPrefixAddrType = _TmnxNatPrefixAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 6, 18, 1, 1),
    _TmnxNatPrefixAddrType_Type()
)
tmnxNatPrefixAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxNatPrefixAddrType.setStatus("current")


class _TmnxNatPrefixAddr_Type(InetAddress):
    """Custom type tmnxNatPrefixAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxNatPrefixAddr_Type.__name__ = "InetAddress"
_TmnxNatPrefixAddr_Object = MibTableColumn
tmnxNatPrefixAddr = _TmnxNatPrefixAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 6, 18, 1, 2),
    _TmnxNatPrefixAddr_Type()
)
tmnxNatPrefixAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxNatPrefixAddr.setStatus("current")


class _TmnxNatPrefixPrefixLen_Type(InetAddressPrefixLength):
    """Custom type tmnxNatPrefixPrefixLen based on InetAddressPrefixLength"""
    subtypeSpec = InetAddressPrefixLength.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_TmnxNatPrefixPrefixLen_Type.__name__ = "InetAddressPrefixLength"
_TmnxNatPrefixPrefixLen_Object = MibTableColumn
tmnxNatPrefixPrefixLen = _TmnxNatPrefixPrefixLen_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 6, 18, 1, 3),
    _TmnxNatPrefixPrefixLen_Type()
)
tmnxNatPrefixPrefixLen.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxNatPrefixPrefixLen.setStatus("current")
_TmnxNatPrefixRowStatus_Type = RowStatus
_TmnxNatPrefixRowStatus_Object = MibTableColumn
tmnxNatPrefixRowStatus = _TmnxNatPrefixRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 6, 18, 1, 4),
    _TmnxNatPrefixRowStatus_Type()
)
tmnxNatPrefixRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxNatPrefixRowStatus.setStatus("current")
_TmnxNatPrefixLastMgmtCh_Type = TimeStamp
_TmnxNatPrefixLastMgmtCh_Object = MibTableColumn
tmnxNatPrefixLastMgmtCh = _TmnxNatPrefixLastMgmtCh_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 6, 18, 1, 5),
    _TmnxNatPrefixLastMgmtCh_Type()
)
tmnxNatPrefixLastMgmtCh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatPrefixLastMgmtCh.setStatus("current")


class _TmnxNatPrefixNatPolicy_Type(TNamedItemOrEmpty):
    """Custom type tmnxNatPrefixNatPolicy based on TNamedItemOrEmpty"""
    defaultValue = OctetString("")


_TmnxNatPrefixNatPolicy_Type.__name__ = "TNamedItemOrEmpty"
_TmnxNatPrefixNatPolicy_Object = MibTableColumn
tmnxNatPrefixNatPolicy = _TmnxNatPrefixNatPolicy_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 6, 18, 1, 6),
    _TmnxNatPrefixNatPolicy_Type()
)
tmnxNatPrefixNatPolicy.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxNatPrefixNatPolicy.setStatus("current")
_TmnxNatL2AwSubPlcyTable_Object = MibTable
tmnxNatL2AwSubPlcyTable = _TmnxNatL2AwSubPlcyTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 6, 19)
)
if mibBuilder.loadTexts:
    tmnxNatL2AwSubPlcyTable.setStatus("current")
_TmnxNatL2AwSubPlcyEntry_Object = MibTableRow
tmnxNatL2AwSubPlcyEntry = _TmnxNatL2AwSubPlcyEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 6, 19, 1)
)
tmnxNatL2AwSubPlcyEntry.setIndexNames(
    (0, "TIMETRA-SUBSCRIBER-MGMT-MIB", "tmnxSubInfoSubIdent"),
    (1, "TIMETRA-NAT-MIB", "tmnxNatL2AwSubPlcy"),
)
if mibBuilder.loadTexts:
    tmnxNatL2AwSubPlcyEntry.setStatus("current")
_TmnxNatL2AwSubPlcy_Type = TNamedItem
_TmnxNatL2AwSubPlcy_Object = MibTableColumn
tmnxNatL2AwSubPlcy = _TmnxNatL2AwSubPlcy_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 6, 19, 1, 1),
    _TmnxNatL2AwSubPlcy_Type()
)
tmnxNatL2AwSubPlcy.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxNatL2AwSubPlcy.setStatus("current")
_TmnxNatL2AwSubPlcyOutVRtrID_Type = TmnxVRtrIDOrZero
_TmnxNatL2AwSubPlcyOutVRtrID_Object = MibTableColumn
tmnxNatL2AwSubPlcyOutVRtrID = _TmnxNatL2AwSubPlcyOutVRtrID_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 6, 19, 1, 2),
    _TmnxNatL2AwSubPlcyOutVRtrID_Type()
)
tmnxNatL2AwSubPlcyOutVRtrID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatL2AwSubPlcyOutVRtrID.setStatus("current")
_TmnxNatL2AwSubPlcyOutAddrType_Type = InetAddressType
_TmnxNatL2AwSubPlcyOutAddrType_Object = MibTableColumn
tmnxNatL2AwSubPlcyOutAddrType = _TmnxNatL2AwSubPlcyOutAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 6, 19, 1, 3),
    _TmnxNatL2AwSubPlcyOutAddrType_Type()
)
tmnxNatL2AwSubPlcyOutAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatL2AwSubPlcyOutAddrType.setStatus("current")


class _TmnxNatL2AwSubPlcyOutAddr_Type(InetAddress):
    """Custom type tmnxNatL2AwSubPlcyOutAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxNatL2AwSubPlcyOutAddr_Type.__name__ = "InetAddress"
_TmnxNatL2AwSubPlcyOutAddr_Object = MibTableColumn
tmnxNatL2AwSubPlcyOutAddr = _TmnxNatL2AwSubPlcyOutAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 6, 19, 1, 4),
    _TmnxNatL2AwSubPlcyOutAddr_Type()
)
tmnxNatL2AwSubPlcyOutAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatL2AwSubPlcyOutAddr.setStatus("current")
_TmnxNatL2AwSubPlcyDnatOvrAddrTyp_Type = InetAddressType
_TmnxNatL2AwSubPlcyDnatOvrAddrTyp_Object = MibTableColumn
tmnxNatL2AwSubPlcyDnatOvrAddrTyp = _TmnxNatL2AwSubPlcyDnatOvrAddrTyp_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 6, 19, 1, 5),
    _TmnxNatL2AwSubPlcyDnatOvrAddrTyp_Type()
)
tmnxNatL2AwSubPlcyDnatOvrAddrTyp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatL2AwSubPlcyDnatOvrAddrTyp.setStatus("current")


class _TmnxNatL2AwSubPlcyDnatOvrAddr_Type(InetAddress):
    """Custom type tmnxNatL2AwSubPlcyDnatOvrAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxNatL2AwSubPlcyDnatOvrAddr_Type.__name__ = "InetAddress"
_TmnxNatL2AwSubPlcyDnatOvrAddr_Object = MibTableColumn
tmnxNatL2AwSubPlcyDnatOvrAddr = _TmnxNatL2AwSubPlcyDnatOvrAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 6, 19, 1, 6),
    _TmnxNatL2AwSubPlcyDnatOvrAddr_Type()
)
tmnxNatL2AwSubPlcyDnatOvrAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatL2AwSubPlcyDnatOvrAddr.setStatus("current")
_TmnxNatL2AwSubPlcyDnatDisable_Type = TruthValue
_TmnxNatL2AwSubPlcyDnatDisable_Object = MibTableColumn
tmnxNatL2AwSubPlcyDnatDisable = _TmnxNatL2AwSubPlcyDnatDisable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 6, 19, 1, 7),
    _TmnxNatL2AwSubPlcyDnatDisable_Type()
)
tmnxNatL2AwSubPlcyDnatDisable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatL2AwSubPlcyDnatDisable.setStatus("current")
_TmnxNatL2AwSubPlcyPurpose_Type = TmnxNatPolicyPurpose
_TmnxNatL2AwSubPlcyPurpose_Object = MibTableColumn
tmnxNatL2AwSubPlcyPurpose = _TmnxNatL2AwSubPlcyPurpose_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 6, 19, 1, 8),
    _TmnxNatL2AwSubPlcyPurpose_Type()
)
tmnxNatL2AwSubPlcyPurpose.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatL2AwSubPlcyPurpose.setStatus("current")
_TmnxNatL2AwSubPlcyOutServiceId_Type = TmnxServId
_TmnxNatL2AwSubPlcyOutServiceId_Object = MibTableColumn
tmnxNatL2AwSubPlcyOutServiceId = _TmnxNatL2AwSubPlcyOutServiceId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 6, 19, 1, 9),
    _TmnxNatL2AwSubPlcyOutServiceId_Type()
)
tmnxNatL2AwSubPlcyOutServiceId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatL2AwSubPlcyOutServiceId.setStatus("current")
_TmnxNatL2AwHostPlcyTable_Object = MibTable
tmnxNatL2AwHostPlcyTable = _TmnxNatL2AwHostPlcyTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 6, 20)
)
if mibBuilder.loadTexts:
    tmnxNatL2AwHostPlcyTable.setStatus("current")
_TmnxNatL2AwHostPlcyEntry_Object = MibTableRow
tmnxNatL2AwHostPlcyEntry = _TmnxNatL2AwHostPlcyEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 6, 20, 1)
)
tmnxNatL2AwHostPlcyEntry.setIndexNames(
    (0, "TIMETRA-SUBSCRIBER-MGMT-MIB", "tmnxSubInfoSubIdent"),
    (0, "TIMETRA-NAT-MIB", "tmnxNatL2AwHostPlcyAddrType"),
    (0, "TIMETRA-NAT-MIB", "tmnxNatL2AwHostPlcyAddr"),
    (0, "TIMETRA-NAT-MIB", "tmnxNatL2AwHostPlcy"),
)
if mibBuilder.loadTexts:
    tmnxNatL2AwHostPlcyEntry.setStatus("current")
_TmnxNatL2AwHostPlcyAddrType_Type = InetAddressType
_TmnxNatL2AwHostPlcyAddrType_Object = MibTableColumn
tmnxNatL2AwHostPlcyAddrType = _TmnxNatL2AwHostPlcyAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 6, 20, 1, 1),
    _TmnxNatL2AwHostPlcyAddrType_Type()
)
tmnxNatL2AwHostPlcyAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxNatL2AwHostPlcyAddrType.setStatus("current")


class _TmnxNatL2AwHostPlcyAddr_Type(InetAddress):
    """Custom type tmnxNatL2AwHostPlcyAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxNatL2AwHostPlcyAddr_Type.__name__ = "InetAddress"
_TmnxNatL2AwHostPlcyAddr_Object = MibTableColumn
tmnxNatL2AwHostPlcyAddr = _TmnxNatL2AwHostPlcyAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 6, 20, 1, 2),
    _TmnxNatL2AwHostPlcyAddr_Type()
)
tmnxNatL2AwHostPlcyAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxNatL2AwHostPlcyAddr.setStatus("current")
_TmnxNatL2AwHostPlcy_Type = TNamedItem
_TmnxNatL2AwHostPlcy_Object = MibTableColumn
tmnxNatL2AwHostPlcy = _TmnxNatL2AwHostPlcy_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 6, 20, 1, 3),
    _TmnxNatL2AwHostPlcy_Type()
)
tmnxNatL2AwHostPlcy.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxNatL2AwHostPlcy.setStatus("current")
_TmnxNatL2AwHostPlcyOutVRtrID_Type = TmnxVRtrIDOrZero
_TmnxNatL2AwHostPlcyOutVRtrID_Object = MibTableColumn
tmnxNatL2AwHostPlcyOutVRtrID = _TmnxNatL2AwHostPlcyOutVRtrID_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 6, 20, 1, 4),
    _TmnxNatL2AwHostPlcyOutVRtrID_Type()
)
tmnxNatL2AwHostPlcyOutVRtrID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatL2AwHostPlcyOutVRtrID.setStatus("current")
_TmnxNatL2AwHostPlcyOutAddrType_Type = InetAddressType
_TmnxNatL2AwHostPlcyOutAddrType_Object = MibTableColumn
tmnxNatL2AwHostPlcyOutAddrType = _TmnxNatL2AwHostPlcyOutAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 6, 20, 1, 5),
    _TmnxNatL2AwHostPlcyOutAddrType_Type()
)
tmnxNatL2AwHostPlcyOutAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatL2AwHostPlcyOutAddrType.setStatus("current")


class _TmnxNatL2AwHostPlcyOutAddr_Type(InetAddress):
    """Custom type tmnxNatL2AwHostPlcyOutAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxNatL2AwHostPlcyOutAddr_Type.__name__ = "InetAddress"
_TmnxNatL2AwHostPlcyOutAddr_Object = MibTableColumn
tmnxNatL2AwHostPlcyOutAddr = _TmnxNatL2AwHostPlcyOutAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 6, 20, 1, 6),
    _TmnxNatL2AwHostPlcyOutAddr_Type()
)
tmnxNatL2AwHostPlcyOutAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatL2AwHostPlcyOutAddr.setStatus("current")
_TmnxNatL2AwHostPlcyOutStart_Type = InetPortNumber
_TmnxNatL2AwHostPlcyOutStart_Object = MibTableColumn
tmnxNatL2AwHostPlcyOutStart = _TmnxNatL2AwHostPlcyOutStart_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 6, 20, 1, 7),
    _TmnxNatL2AwHostPlcyOutStart_Type()
)
tmnxNatL2AwHostPlcyOutStart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatL2AwHostPlcyOutStart.setStatus("current")
_TmnxNatL2AwHostPlcyBypassActive_Type = TruthValue
_TmnxNatL2AwHostPlcyBypassActive_Object = MibTableColumn
tmnxNatL2AwHostPlcyBypassActive = _TmnxNatL2AwHostPlcyBypassActive_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 6, 20, 1, 8),
    _TmnxNatL2AwHostPlcyBypassActive_Type()
)
tmnxNatL2AwHostPlcyBypassActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatL2AwHostPlcyBypassActive.setStatus("current")
_TmnxNatL2AwHostPlcyVasFilter_Type = TNamedItemOrEmpty
_TmnxNatL2AwHostPlcyVasFilter_Object = MibTableColumn
tmnxNatL2AwHostPlcyVasFilter = _TmnxNatL2AwHostPlcyVasFilter_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 6, 20, 1, 9),
    _TmnxNatL2AwHostPlcyVasFilter_Type()
)
tmnxNatL2AwHostPlcyVasFilter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatL2AwHostPlcyVasFilter.setStatus("current")


class _TmnxNatL2AwHostPlcyDNatOverride_Type(Integer32):
    """Custom type tmnxNatL2AwHostPlcyDNatOverride based on Integer32"""
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
          ("enable", 1),
          ("disable", 2))
    )


_TmnxNatL2AwHostPlcyDNatOverride_Type.__name__ = "Integer32"
_TmnxNatL2AwHostPlcyDNatOverride_Object = MibTableColumn
tmnxNatL2AwHostPlcyDNatOverride = _TmnxNatL2AwHostPlcyDNatOverride_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 6, 20, 1, 10),
    _TmnxNatL2AwHostPlcyDNatOverride_Type()
)
tmnxNatL2AwHostPlcyDNatOverride.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatL2AwHostPlcyDNatOverride.setStatus("current")
_TmnxNatL2AwHostPlcyDnatOvrAddrTp_Type = InetAddressType
_TmnxNatL2AwHostPlcyDnatOvrAddrTp_Object = MibTableColumn
tmnxNatL2AwHostPlcyDnatOvrAddrTp = _TmnxNatL2AwHostPlcyDnatOvrAddrTp_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 6, 20, 1, 11),
    _TmnxNatL2AwHostPlcyDnatOvrAddrTp_Type()
)
tmnxNatL2AwHostPlcyDnatOvrAddrTp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatL2AwHostPlcyDnatOvrAddrTp.setStatus("current")


class _TmnxNatL2AwHostPlcyDnatOvrAddr_Type(InetAddress):
    """Custom type tmnxNatL2AwHostPlcyDnatOvrAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxNatL2AwHostPlcyDnatOvrAddr_Type.__name__ = "InetAddress"
_TmnxNatL2AwHostPlcyDnatOvrAddr_Object = MibTableColumn
tmnxNatL2AwHostPlcyDnatOvrAddr = _TmnxNatL2AwHostPlcyDnatOvrAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 6, 20, 1, 12),
    _TmnxNatL2AwHostPlcyDnatOvrAddr_Type()
)
tmnxNatL2AwHostPlcyDnatOvrAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatL2AwHostPlcyDnatOvrAddr.setStatus("current")
_TmnxNatSourcePrefixTable_Object = MibTable
tmnxNatSourcePrefixTable = _TmnxNatSourcePrefixTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 6, 21)
)
if mibBuilder.loadTexts:
    tmnxNatSourcePrefixTable.setStatus("current")
_TmnxNatSourcePrefixEntry_Object = MibTableRow
tmnxNatSourcePrefixEntry = _TmnxNatSourcePrefixEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 6, 21, 1)
)
tmnxNatSourcePrefixEntry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "TIMETRA-NAT-MIB", "tmnxNatSourcePrefixAddrType"),
    (0, "TIMETRA-NAT-MIB", "tmnxNatSourcePrefixAddr"),
    (0, "TIMETRA-NAT-MIB", "tmnxNatSourcePrefixPrefixLen"),
)
if mibBuilder.loadTexts:
    tmnxNatSourcePrefixEntry.setStatus("current")
_TmnxNatSourcePrefixAddrType_Type = InetAddressType
_TmnxNatSourcePrefixAddrType_Object = MibTableColumn
tmnxNatSourcePrefixAddrType = _TmnxNatSourcePrefixAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 6, 21, 1, 1),
    _TmnxNatSourcePrefixAddrType_Type()
)
tmnxNatSourcePrefixAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxNatSourcePrefixAddrType.setStatus("current")


class _TmnxNatSourcePrefixAddr_Type(InetAddress):
    """Custom type tmnxNatSourcePrefixAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )
    fixed_length = 4


_TmnxNatSourcePrefixAddr_Type.__name__ = "InetAddress"
_TmnxNatSourcePrefixAddr_Object = MibTableColumn
tmnxNatSourcePrefixAddr = _TmnxNatSourcePrefixAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 6, 21, 1, 2),
    _TmnxNatSourcePrefixAddr_Type()
)
tmnxNatSourcePrefixAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxNatSourcePrefixAddr.setStatus("current")


class _TmnxNatSourcePrefixPrefixLen_Type(InetAddressPrefixLength):
    """Custom type tmnxNatSourcePrefixPrefixLen based on InetAddressPrefixLength"""
    subtypeSpec = InetAddressPrefixLength.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32),
    )


_TmnxNatSourcePrefixPrefixLen_Type.__name__ = "InetAddressPrefixLength"
_TmnxNatSourcePrefixPrefixLen_Object = MibTableColumn
tmnxNatSourcePrefixPrefixLen = _TmnxNatSourcePrefixPrefixLen_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 6, 21, 1, 3),
    _TmnxNatSourcePrefixPrefixLen_Type()
)
tmnxNatSourcePrefixPrefixLen.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxNatSourcePrefixPrefixLen.setStatus("current")
_TmnxNatSourcePrefixRowStatus_Type = RowStatus
_TmnxNatSourcePrefixRowStatus_Object = MibTableColumn
tmnxNatSourcePrefixRowStatus = _TmnxNatSourcePrefixRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 6, 21, 1, 4),
    _TmnxNatSourcePrefixRowStatus_Type()
)
tmnxNatSourcePrefixRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxNatSourcePrefixRowStatus.setStatus("current")
_TmnxNatSourcePrefixLastMgmtCh_Type = TimeStamp
_TmnxNatSourcePrefixLastMgmtCh_Object = MibTableColumn
tmnxNatSourcePrefixLastMgmtCh = _TmnxNatSourcePrefixLastMgmtCh_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 6, 21, 1, 5),
    _TmnxNatSourcePrefixLastMgmtCh_Type()
)
tmnxNatSourcePrefixLastMgmtCh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatSourcePrefixLastMgmtCh.setStatus("current")


class _TmnxNatSourcePrefixNatPolicy_Type(TNamedItemOrEmpty):
    """Custom type tmnxNatSourcePrefixNatPolicy based on TNamedItemOrEmpty"""
    defaultValue = OctetString("")


_TmnxNatSourcePrefixNatPolicy_Type.__name__ = "TNamedItemOrEmpty"
_TmnxNatSourcePrefixNatPolicy_Object = MibTableColumn
tmnxNatSourcePrefixNatPolicy = _TmnxNatSourcePrefixNatPolicy_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 6, 21, 1, 6),
    _TmnxNatSourcePrefixNatPolicy_Type()
)
tmnxNatSourcePrefixNatPolicy.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxNatSourcePrefixNatPolicy.setStatus("current")
_TmnxNatMapObjs_ObjectIdentity = ObjectIdentity
tmnxNatMapObjs = _TmnxNatMapObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 7)
)
_TmnxNatMapLsnHostTable_Object = MibTable
tmnxNatMapLsnHostTable = _TmnxNatMapLsnHostTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 7, 1)
)
if mibBuilder.loadTexts:
    tmnxNatMapLsnHostTable.setStatus("obsolete")
_TmnxNatMapLsnHostEntry_Object = MibTableRow
tmnxNatMapLsnHostEntry = _TmnxNatMapLsnHostEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 7, 1, 1)
)
tmnxNatMapLsnHostEntry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "TIMETRA-NAT-MIB", "tmnxNatMapLsnHostAddrType"),
    (0, "TIMETRA-NAT-MIB", "tmnxNatMapLsnHostAddr"),
)
if mibBuilder.loadTexts:
    tmnxNatMapLsnHostEntry.setStatus("obsolete")
_TmnxNatMapLsnHostAddrType_Type = InetAddressType
_TmnxNatMapLsnHostAddrType_Object = MibTableColumn
tmnxNatMapLsnHostAddrType = _TmnxNatMapLsnHostAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 7, 1, 1, 1),
    _TmnxNatMapLsnHostAddrType_Type()
)
tmnxNatMapLsnHostAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxNatMapLsnHostAddrType.setStatus("obsolete")


class _TmnxNatMapLsnHostAddr_Type(InetAddress):
    """Custom type tmnxNatMapLsnHostAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxNatMapLsnHostAddr_Type.__name__ = "InetAddress"
_TmnxNatMapLsnHostAddr_Object = MibTableColumn
tmnxNatMapLsnHostAddr = _TmnxNatMapLsnHostAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 7, 1, 1, 2),
    _TmnxNatMapLsnHostAddr_Type()
)
tmnxNatMapLsnHostAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxNatMapLsnHostAddr.setStatus("obsolete")
_TmnxNatMapLsnHostRowStatus_Type = RowStatus
_TmnxNatMapLsnHostRowStatus_Object = MibTableColumn
tmnxNatMapLsnHostRowStatus = _TmnxNatMapLsnHostRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 7, 1, 1, 3),
    _TmnxNatMapLsnHostRowStatus_Type()
)
tmnxNatMapLsnHostRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxNatMapLsnHostRowStatus.setStatus("obsolete")
_TmnxNatMapLsnHostLastMgmtChange_Type = TimeStamp
_TmnxNatMapLsnHostLastMgmtChange_Object = MibTableColumn
tmnxNatMapLsnHostLastMgmtChange = _TmnxNatMapLsnHostLastMgmtChange_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 7, 1, 1, 4),
    _TmnxNatMapLsnHostLastMgmtChange_Type()
)
tmnxNatMapLsnHostLastMgmtChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatMapLsnHostLastMgmtChange.setStatus("obsolete")
_TmnxNatMapLsnHostAdminState_Type = TmnxAdminState
_TmnxNatMapLsnHostAdminState_Object = MibTableColumn
tmnxNatMapLsnHostAdminState = _TmnxNatMapLsnHostAdminState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 7, 1, 1, 5),
    _TmnxNatMapLsnHostAdminState_Type()
)
tmnxNatMapLsnHostAdminState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxNatMapLsnHostAdminState.setStatus("obsolete")
_TmnxNatMapLsnHostOutAddrType_Type = InetAddressType
_TmnxNatMapLsnHostOutAddrType_Object = MibTableColumn
tmnxNatMapLsnHostOutAddrType = _TmnxNatMapLsnHostOutAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 7, 1, 1, 6),
    _TmnxNatMapLsnHostOutAddrType_Type()
)
tmnxNatMapLsnHostOutAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatMapLsnHostOutAddrType.setStatus("obsolete")


class _TmnxNatMapLsnHostOutAddr_Type(InetAddress):
    """Custom type tmnxNatMapLsnHostOutAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxNatMapLsnHostOutAddr_Type.__name__ = "InetAddress"
_TmnxNatMapLsnHostOutAddr_Object = MibTableColumn
tmnxNatMapLsnHostOutAddr = _TmnxNatMapLsnHostOutAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 7, 1, 1, 7),
    _TmnxNatMapLsnHostOutAddr_Type()
)
tmnxNatMapLsnHostOutAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatMapLsnHostOutAddr.setStatus("obsolete")
_TmnxNatMapLsnHostOutVRtrID_Type = TmnxVRtrID
_TmnxNatMapLsnHostOutVRtrID_Object = MibTableColumn
tmnxNatMapLsnHostOutVRtrID = _TmnxNatMapLsnHostOutVRtrID_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 7, 1, 1, 8),
    _TmnxNatMapLsnHostOutVRtrID_Type()
)
tmnxNatMapLsnHostOutVRtrID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatMapLsnHostOutVRtrID.setStatus("obsolete")
_TmnxNatMapTable_Object = MibTable
tmnxNatMapTable = _TmnxNatMapTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 7, 2)
)
if mibBuilder.loadTexts:
    tmnxNatMapTable.setStatus("obsolete")
_TmnxNatMapEntry_Object = MibTableRow
tmnxNatMapEntry = _TmnxNatMapEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 7, 2, 1)
)
tmnxNatMapEntry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "TIMETRA-NAT-MIB", "tmnxNatMapAddrType"),
    (0, "TIMETRA-NAT-MIB", "tmnxNatMapAddr"),
    (0, "TIMETRA-NAT-MIB", "tmnxNatMapPort"),
    (0, "TIMETRA-NAT-MIB", "tmnxNatMapProtocol"),
)
if mibBuilder.loadTexts:
    tmnxNatMapEntry.setStatus("obsolete")
_TmnxNatMapAddrType_Type = InetAddressType
_TmnxNatMapAddrType_Object = MibTableColumn
tmnxNatMapAddrType = _TmnxNatMapAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 7, 2, 1, 1),
    _TmnxNatMapAddrType_Type()
)
tmnxNatMapAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxNatMapAddrType.setStatus("obsolete")


class _TmnxNatMapAddr_Type(InetAddress):
    """Custom type tmnxNatMapAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxNatMapAddr_Type.__name__ = "InetAddress"
_TmnxNatMapAddr_Object = MibTableColumn
tmnxNatMapAddr = _TmnxNatMapAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 7, 2, 1, 2),
    _TmnxNatMapAddr_Type()
)
tmnxNatMapAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxNatMapAddr.setStatus("obsolete")


class _TmnxNatMapPort_Type(Unsigned32):
    """Custom type tmnxNatMapPort based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1023),
    )


_TmnxNatMapPort_Type.__name__ = "Unsigned32"
_TmnxNatMapPort_Object = MibTableColumn
tmnxNatMapPort = _TmnxNatMapPort_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 7, 2, 1, 3),
    _TmnxNatMapPort_Type()
)
tmnxNatMapPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxNatMapPort.setStatus("obsolete")


class _TmnxNatMapProtocol_Type(TIpProtocol):
    """Custom type tmnxNatMapProtocol based on TIpProtocol"""
    subtypeSpec = TIpProtocol.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(6, 6),
        ValueRangeConstraint(17, 17),
    )


_TmnxNatMapProtocol_Type.__name__ = "TIpProtocol"
_TmnxNatMapProtocol_Object = MibTableColumn
tmnxNatMapProtocol = _TmnxNatMapProtocol_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 7, 2, 1, 4),
    _TmnxNatMapProtocol_Type()
)
tmnxNatMapProtocol.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxNatMapProtocol.setStatus("obsolete")
_TmnxNatMapRowStatus_Type = RowStatus
_TmnxNatMapRowStatus_Object = MibTableColumn
tmnxNatMapRowStatus = _TmnxNatMapRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 7, 2, 1, 5),
    _TmnxNatMapRowStatus_Type()
)
tmnxNatMapRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxNatMapRowStatus.setStatus("obsolete")
_TmnxNatMapLastMgmtChange_Type = TimeStamp
_TmnxNatMapLastMgmtChange_Object = MibTableColumn
tmnxNatMapLastMgmtChange = _TmnxNatMapLastMgmtChange_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 7, 2, 1, 6),
    _TmnxNatMapLastMgmtChange_Type()
)
tmnxNatMapLastMgmtChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatMapLastMgmtChange.setStatus("obsolete")


class _TmnxNatMapOutPort_Type(Unsigned32):
    """Custom type tmnxNatMapOutPort based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1023),
    )


_TmnxNatMapOutPort_Type.__name__ = "Unsigned32"
_TmnxNatMapOutPort_Object = MibTableColumn
tmnxNatMapOutPort = _TmnxNatMapOutPort_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 7, 2, 1, 7),
    _TmnxNatMapOutPort_Type()
)
tmnxNatMapOutPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxNatMapOutPort.setStatus("obsolete")
_TmnxNatFwdObjs_ObjectIdentity = ObjectIdentity
tmnxNatFwdObjs = _TmnxNatFwdObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 8)
)
_TmnxNatFwdAction_ObjectIdentity = ObjectIdentity
tmnxNatFwdAction = _TmnxNatFwdAction_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 8, 1)
)
_TmnxNatFwdActionSubType_Type = TmnxNatPlType
_TmnxNatFwdActionSubType_Object = MibScalar
tmnxNatFwdActionSubType = _TmnxNatFwdActionSubType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 8, 1, 1),
    _TmnxNatFwdActionSubType_Type()
)
tmnxNatFwdActionSubType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxNatFwdActionSubType.setStatus("current")
_TmnxNatFwdActionVRtrId_Type = TmnxVRtrID
_TmnxNatFwdActionVRtrId_Object = MibScalar
tmnxNatFwdActionVRtrId = _TmnxNatFwdActionVRtrId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 8, 1, 2),
    _TmnxNatFwdActionVRtrId_Type()
)
tmnxNatFwdActionVRtrId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxNatFwdActionVRtrId.setStatus("current")
_TmnxNatFwdActionAddrType_Type = InetAddressType
_TmnxNatFwdActionAddrType_Object = MibScalar
tmnxNatFwdActionAddrType = _TmnxNatFwdActionAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 8, 1, 3),
    _TmnxNatFwdActionAddrType_Type()
)
tmnxNatFwdActionAddrType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxNatFwdActionAddrType.setStatus("current")


class _TmnxNatFwdActionAddr_Type(InetAddress):
    """Custom type tmnxNatFwdActionAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxNatFwdActionAddr_Type.__name__ = "InetAddress"
_TmnxNatFwdActionAddr_Object = MibScalar
tmnxNatFwdActionAddr = _TmnxNatFwdActionAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 8, 1, 4),
    _TmnxNatFwdActionAddr_Type()
)
tmnxNatFwdActionAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxNatFwdActionAddr.setStatus("current")
_TmnxNatFwdActionB4Addr_Type = InetAddressIPv6
_TmnxNatFwdActionB4Addr_Object = MibScalar
tmnxNatFwdActionB4Addr = _TmnxNatFwdActionB4Addr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 8, 1, 6),
    _TmnxNatFwdActionB4Addr_Type()
)
tmnxNatFwdActionB4Addr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxNatFwdActionB4Addr.setStatus("current")
_TmnxNatFwdActionAftrAddr_Type = InetAddressIPv6
_TmnxNatFwdActionAftrAddr_Object = MibScalar
tmnxNatFwdActionAftrAddr = _TmnxNatFwdActionAftrAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 8, 1, 8),
    _TmnxNatFwdActionAftrAddr_Type()
)
tmnxNatFwdActionAftrAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxNatFwdActionAftrAddr.setStatus("current")
_TmnxNatFwdActionL2awSubscriberId_Type = TmnxSubIdentStringOrEmpty
_TmnxNatFwdActionL2awSubscriberId_Object = MibScalar
tmnxNatFwdActionL2awSubscriberId = _TmnxNatFwdActionL2awSubscriberId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 8, 1, 9),
    _TmnxNatFwdActionL2awSubscriberId_Type()
)
tmnxNatFwdActionL2awSubscriberId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxNatFwdActionL2awSubscriberId.setStatus("current")


class _TmnxNatFwdActionProtocol_Type(Unsigned32):
    """Custom type tmnxNatFwdActionProtocol based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_TmnxNatFwdActionProtocol_Type.__name__ = "Unsigned32"
_TmnxNatFwdActionProtocol_Object = MibScalar
tmnxNatFwdActionProtocol = _TmnxNatFwdActionProtocol_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 8, 1, 10),
    _TmnxNatFwdActionProtocol_Type()
)
tmnxNatFwdActionProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxNatFwdActionProtocol.setStatus("current")


class _TmnxNatFwdActionTimeOut_Type(Unsigned32):
    """Custom type tmnxNatFwdActionTimeOut based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(60, 86400),
    )


_TmnxNatFwdActionTimeOut_Type.__name__ = "Unsigned32"
_TmnxNatFwdActionTimeOut_Object = MibScalar
tmnxNatFwdActionTimeOut = _TmnxNatFwdActionTimeOut_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 8, 1, 11),
    _TmnxNatFwdActionTimeOut_Type()
)
tmnxNatFwdActionTimeOut.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxNatFwdActionTimeOut.setStatus("current")
if mibBuilder.loadTexts:
    tmnxNatFwdActionTimeOut.setUnits("seconds")


class _TmnxNatFwdActionPort_Type(Unsigned32):
    """Custom type tmnxNatFwdActionPort based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_TmnxNatFwdActionPort_Type.__name__ = "Unsigned32"
_TmnxNatFwdActionPort_Object = MibScalar
tmnxNatFwdActionPort = _TmnxNatFwdActionPort_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 8, 1, 12),
    _TmnxNatFwdActionPort_Type()
)
tmnxNatFwdActionPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxNatFwdActionPort.setStatus("current")


class _TmnxNatFwdActionOutPort_Type(Unsigned32):
    """Custom type tmnxNatFwdActionOutPort based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_TmnxNatFwdActionOutPort_Type.__name__ = "Unsigned32"
_TmnxNatFwdActionOutPort_Object = MibScalar
tmnxNatFwdActionOutPort = _TmnxNatFwdActionOutPort_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 8, 1, 13),
    _TmnxNatFwdActionOutPort_Type()
)
tmnxNatFwdActionOutPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxNatFwdActionOutPort.setStatus("current")
_TmnxNatFwdActionOutAddr_Type = InetAddressIPv4
_TmnxNatFwdActionOutAddr_Object = MibScalar
tmnxNatFwdActionOutAddr = _TmnxNatFwdActionOutAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 8, 1, 15),
    _TmnxNatFwdActionOutAddr_Type()
)
tmnxNatFwdActionOutAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxNatFwdActionOutAddr.setStatus("current")
_TmnxNatFwdActionType_Type = TmnxNatFwdActionType
_TmnxNatFwdActionType_Object = MibScalar
tmnxNatFwdActionType = _TmnxNatFwdActionType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 8, 1, 16),
    _TmnxNatFwdActionType_Type()
)
tmnxNatFwdActionType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxNatFwdActionType.setStatus("current")
_TmnxNatFwdActionGo_Type = TmnxActionType
_TmnxNatFwdActionGo_Object = MibScalar
tmnxNatFwdActionGo = _TmnxNatFwdActionGo_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 8, 1, 17),
    _TmnxNatFwdActionGo_Type()
)
tmnxNatFwdActionGo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxNatFwdActionGo.setStatus("current")
_TmnxNatFwdActionSuccessful_Type = TruthValue
_TmnxNatFwdActionSuccessful_Object = MibScalar
tmnxNatFwdActionSuccessful = _TmnxNatFwdActionSuccessful_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 8, 1, 18),
    _TmnxNatFwdActionSuccessful_Type()
)
tmnxNatFwdActionSuccessful.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatFwdActionSuccessful.setStatus("current")
_TmnxNatFwdActionTime_Type = TimeStamp
_TmnxNatFwdActionTime_Object = MibScalar
tmnxNatFwdActionTime = _TmnxNatFwdActionTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 8, 1, 19),
    _TmnxNatFwdActionTime_Type()
)
tmnxNatFwdActionTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatFwdActionTime.setStatus("current")
_TmnxNatFwdActionDescription_Type = TmnxNatFwdEntryDescription
_TmnxNatFwdActionDescription_Object = MibScalar
tmnxNatFwdActionDescription = _TmnxNatFwdActionDescription_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 8, 1, 20),
    _TmnxNatFwdActionDescription_Type()
)
tmnxNatFwdActionDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxNatFwdActionDescription.setStatus("current")
_TmnxNatFwdActionNatPolicy_Type = TNamedItemOrEmpty
_TmnxNatFwdActionNatPolicy_Object = MibScalar
tmnxNatFwdActionNatPolicy = _TmnxNatFwdActionNatPolicy_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 8, 1, 21),
    _TmnxNatFwdActionNatPolicy_Type()
)
tmnxNatFwdActionNatPolicy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxNatFwdActionNatPolicy.setStatus("current")
_TmnxNatFwdActionSaveConfig_Type = TruthValue
_TmnxNatFwdActionSaveConfig_Object = MibScalar
tmnxNatFwdActionSaveConfig = _TmnxNatFwdActionSaveConfig_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 8, 1, 22),
    _TmnxNatFwdActionSaveConfig_Type()
)
tmnxNatFwdActionSaveConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxNatFwdActionSaveConfig.setStatus("current")
_TmnxNatFwdActionSpfForce_Type = TruthValue
_TmnxNatFwdActionSpfForce_Object = MibScalar
tmnxNatFwdActionSpfForce = _TmnxNatFwdActionSpfForce_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 8, 1, 24),
    _TmnxNatFwdActionSpfForce_Type()
)
tmnxNatFwdActionSpfForce.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxNatFwdActionSpfForce.setStatus("current")


class _TmnxNatFwdActionAddrCpm_Type(TruthValue):
    """Custom type tmnxNatFwdActionAddrCpm based on TruthValue"""
    defaultValue = 2


_TmnxNatFwdActionAddrCpm_Type.__name__ = "TruthValue"
_TmnxNatFwdActionAddrCpm_Object = MibScalar
tmnxNatFwdActionAddrCpm = _TmnxNatFwdActionAddrCpm_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 8, 1, 25),
    _TmnxNatFwdActionAddrCpm_Type()
)
tmnxNatFwdActionAddrCpm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxNatFwdActionAddrCpm.setStatus("current")


class _TmnxNatFwdActionOutPublicIf_Type(TruthValue):
    """Custom type tmnxNatFwdActionOutPublicIf based on TruthValue"""
    defaultValue = 2


_TmnxNatFwdActionOutPublicIf_Type.__name__ = "TruthValue"
_TmnxNatFwdActionOutPublicIf_Object = MibScalar
tmnxNatFwdActionOutPublicIf = _TmnxNatFwdActionOutPublicIf_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 8, 1, 26),
    _TmnxNatFwdActionOutPublicIf_Type()
)
tmnxNatFwdActionOutPublicIf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxNatFwdActionOutPublicIf.setStatus("current")
_TmnxNatFwdTable_Object = MibTable
tmnxNatFwdTable = _TmnxNatFwdTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 8, 5)
)
if mibBuilder.loadTexts:
    tmnxNatFwdTable.setStatus("obsolete")
_TmnxNatFwdEntry_Object = MibTableRow
tmnxNatFwdEntry = _TmnxNatFwdEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 8, 5, 1)
)
tmnxNatFwdEntry.setIndexNames(
    (0, "TIMETRA-NAT-MIB", "tmnxNatFwdSubType"),
    (0, "TIMETRA-NAT-MIB", "tmnxNatFwdL2awSubIdent"),
    (0, "TIMETRA-NAT-MIB", "tmnxNatFwdLsnVRtrID"),
    (0, "TIMETRA-NAT-MIB", "tmnxNatFwdLsnB4AddrType"),
    (0, "TIMETRA-NAT-MIB", "tmnxNatFwdLsnB4Addr"),
    (0, "TIMETRA-NAT-MIB", "tmnxNatFwdAddrType"),
    (0, "TIMETRA-NAT-MIB", "tmnxNatFwdAddr"),
    (0, "TIMETRA-NAT-MIB", "tmnxNatFwdProtocol"),
    (0, "TIMETRA-NAT-MIB", "tmnxNatFwdPort"),
)
if mibBuilder.loadTexts:
    tmnxNatFwdEntry.setStatus("obsolete")
_TmnxNatFwdSubType_Type = TmnxNatLegacySubscriberType
_TmnxNatFwdSubType_Object = MibTableColumn
tmnxNatFwdSubType = _TmnxNatFwdSubType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 8, 5, 1, 1),
    _TmnxNatFwdSubType_Type()
)
tmnxNatFwdSubType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxNatFwdSubType.setStatus("obsolete")


class _TmnxNatFwdL2awSubIdent_Type(DisplayString):
    """Custom type tmnxNatFwdL2awSubIdent based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_TmnxNatFwdL2awSubIdent_Type.__name__ = "DisplayString"
_TmnxNatFwdL2awSubIdent_Object = MibTableColumn
tmnxNatFwdL2awSubIdent = _TmnxNatFwdL2awSubIdent_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 8, 5, 1, 2),
    _TmnxNatFwdL2awSubIdent_Type()
)
tmnxNatFwdL2awSubIdent.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxNatFwdL2awSubIdent.setStatus("obsolete")
_TmnxNatFwdLsnVRtrID_Type = TmnxVRtrIDOrZero
_TmnxNatFwdLsnVRtrID_Object = MibTableColumn
tmnxNatFwdLsnVRtrID = _TmnxNatFwdLsnVRtrID_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 8, 5, 1, 3),
    _TmnxNatFwdLsnVRtrID_Type()
)
tmnxNatFwdLsnVRtrID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxNatFwdLsnVRtrID.setStatus("obsolete")
_TmnxNatFwdLsnB4AddrType_Type = InetAddressType
_TmnxNatFwdLsnB4AddrType_Object = MibTableColumn
tmnxNatFwdLsnB4AddrType = _TmnxNatFwdLsnB4AddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 8, 5, 1, 4),
    _TmnxNatFwdLsnB4AddrType_Type()
)
tmnxNatFwdLsnB4AddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxNatFwdLsnB4AddrType.setStatus("obsolete")


class _TmnxNatFwdLsnB4Addr_Type(InetAddress):
    """Custom type tmnxNatFwdLsnB4Addr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(16, 16),
    )


_TmnxNatFwdLsnB4Addr_Type.__name__ = "InetAddress"
_TmnxNatFwdLsnB4Addr_Object = MibTableColumn
tmnxNatFwdLsnB4Addr = _TmnxNatFwdLsnB4Addr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 8, 5, 1, 5),
    _TmnxNatFwdLsnB4Addr_Type()
)
tmnxNatFwdLsnB4Addr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxNatFwdLsnB4Addr.setStatus("obsolete")
_TmnxNatFwdAddrType_Type = InetAddressType
_TmnxNatFwdAddrType_Object = MibTableColumn
tmnxNatFwdAddrType = _TmnxNatFwdAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 8, 5, 1, 6),
    _TmnxNatFwdAddrType_Type()
)
tmnxNatFwdAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxNatFwdAddrType.setStatus("obsolete")


class _TmnxNatFwdAddr_Type(InetAddress):
    """Custom type tmnxNatFwdAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxNatFwdAddr_Type.__name__ = "InetAddress"
_TmnxNatFwdAddr_Object = MibTableColumn
tmnxNatFwdAddr = _TmnxNatFwdAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 8, 5, 1, 7),
    _TmnxNatFwdAddr_Type()
)
tmnxNatFwdAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxNatFwdAddr.setStatus("obsolete")


class _TmnxNatFwdProtocol_Type(Unsigned32):
    """Custom type tmnxNatFwdProtocol based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_TmnxNatFwdProtocol_Type.__name__ = "Unsigned32"
_TmnxNatFwdProtocol_Object = MibTableColumn
tmnxNatFwdProtocol = _TmnxNatFwdProtocol_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 8, 5, 1, 8),
    _TmnxNatFwdProtocol_Type()
)
tmnxNatFwdProtocol.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxNatFwdProtocol.setStatus("obsolete")
_TmnxNatFwdPort_Type = InetPortNumber
_TmnxNatFwdPort_Object = MibTableColumn
tmnxNatFwdPort = _TmnxNatFwdPort_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 8, 5, 1, 9),
    _TmnxNatFwdPort_Type()
)
tmnxNatFwdPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxNatFwdPort.setStatus("obsolete")
_TmnxNatFwdOutVRtrID_Type = TmnxVRtrID
_TmnxNatFwdOutVRtrID_Object = MibTableColumn
tmnxNatFwdOutVRtrID = _TmnxNatFwdOutVRtrID_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 8, 5, 1, 10),
    _TmnxNatFwdOutVRtrID_Type()
)
tmnxNatFwdOutVRtrID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatFwdOutVRtrID.setStatus("obsolete")
_TmnxNatFwdOutAddrType_Type = InetAddressType
_TmnxNatFwdOutAddrType_Object = MibTableColumn
tmnxNatFwdOutAddrType = _TmnxNatFwdOutAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 8, 5, 1, 11),
    _TmnxNatFwdOutAddrType_Type()
)
tmnxNatFwdOutAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatFwdOutAddrType.setStatus("obsolete")


class _TmnxNatFwdOutAddr_Type(InetAddress):
    """Custom type tmnxNatFwdOutAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
    )


_TmnxNatFwdOutAddr_Type.__name__ = "InetAddress"
_TmnxNatFwdOutAddr_Object = MibTableColumn
tmnxNatFwdOutAddr = _TmnxNatFwdOutAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 8, 5, 1, 12),
    _TmnxNatFwdOutAddr_Type()
)
tmnxNatFwdOutAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatFwdOutAddr.setStatus("obsolete")
_TmnxNatFwdOutPort_Type = InetPortNumber
_TmnxNatFwdOutPort_Object = MibTableColumn
tmnxNatFwdOutPort = _TmnxNatFwdOutPort_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 8, 5, 1, 13),
    _TmnxNatFwdOutPort_Type()
)
tmnxNatFwdOutPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatFwdOutPort.setStatus("obsolete")


class _TmnxNatFwdExpiryDateAndTime_Type(DateAndTime):
    """Custom type tmnxNatFwdExpiryDateAndTime based on DateAndTime"""
    subtypeSpec = DateAndTime.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(11, 11),
    )
    fixed_length = 11


_TmnxNatFwdExpiryDateAndTime_Type.__name__ = "DateAndTime"
_TmnxNatFwdExpiryDateAndTime_Object = MibTableColumn
tmnxNatFwdExpiryDateAndTime = _TmnxNatFwdExpiryDateAndTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 8, 5, 1, 14),
    _TmnxNatFwdExpiryDateAndTime_Type()
)
tmnxNatFwdExpiryDateAndTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatFwdExpiryDateAndTime.setStatus("obsolete")
_TmnxNatFwdLsnAftrAddrType_Type = InetAddressType
_TmnxNatFwdLsnAftrAddrType_Object = MibTableColumn
tmnxNatFwdLsnAftrAddrType = _TmnxNatFwdLsnAftrAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 8, 5, 1, 15),
    _TmnxNatFwdLsnAftrAddrType_Type()
)
tmnxNatFwdLsnAftrAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatFwdLsnAftrAddrType.setStatus("obsolete")


class _TmnxNatFwdLsnAftrAddr_Type(InetAddress):
    """Custom type tmnxNatFwdLsnAftrAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(16, 16),
    )


_TmnxNatFwdLsnAftrAddr_Type.__name__ = "InetAddress"
_TmnxNatFwdLsnAftrAddr_Object = MibTableColumn
tmnxNatFwdLsnAftrAddr = _TmnxNatFwdLsnAftrAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 8, 5, 1, 16),
    _TmnxNatFwdLsnAftrAddr_Type()
)
tmnxNatFwdLsnAftrAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatFwdLsnAftrAddr.setStatus("obsolete")
_TmnxNatFwdPersistKey_Type = Unsigned32
_TmnxNatFwdPersistKey_Object = MibTableColumn
tmnxNatFwdPersistKey = _TmnxNatFwdPersistKey_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 8, 5, 1, 17),
    _TmnxNatFwdPersistKey_Type()
)
tmnxNatFwdPersistKey.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatFwdPersistKey.setStatus("obsolete")
_TmnxNatFwdDescription_Type = TmnxNatFwdEntryDescription
_TmnxNatFwdDescription_Object = MibTableColumn
tmnxNatFwdDescription = _TmnxNatFwdDescription_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 8, 5, 1, 18),
    _TmnxNatFwdDescription_Type()
)
tmnxNatFwdDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatFwdDescription.setStatus("obsolete")


class _TmnxNatFwdOrigin_Type(Integer32):
    """Custom type tmnxNatFwdOrigin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dynamic", 1),
          ("static", 2))
    )


_TmnxNatFwdOrigin_Type.__name__ = "Integer32"
_TmnxNatFwdOrigin_Object = MibTableColumn
tmnxNatFwdOrigin = _TmnxNatFwdOrigin_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 8, 5, 1, 19),
    _TmnxNatFwdOrigin_Type()
)
tmnxNatFwdOrigin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatFwdOrigin.setStatus("obsolete")
_TmnxNatFwd2Table_Object = MibTable
tmnxNatFwd2Table = _TmnxNatFwd2Table_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 8, 6)
)
if mibBuilder.loadTexts:
    tmnxNatFwd2Table.setStatus("current")
_TmnxNatFwd2Entry_Object = MibTableRow
tmnxNatFwd2Entry = _TmnxNatFwd2Entry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 8, 6, 1)
)
tmnxNatFwd2Entry.setIndexNames(
    (0, "TIMETRA-NAT-MIB", "tmnxNatFwd2SubType"),
    (0, "TIMETRA-NAT-MIB", "tmnxNatFwd2L2awSubIdent"),
    (0, "TIMETRA-NAT-MIB", "tmnxNatFwd2LsnVRtrID"),
    (0, "TIMETRA-NAT-MIB", "tmnxNatFwd2LsnB4AddrType"),
    (0, "TIMETRA-NAT-MIB", "tmnxNatFwd2LsnB4Addr"),
    (0, "TIMETRA-NAT-MIB", "tmnxNatFwd2AddrType"),
    (0, "TIMETRA-NAT-MIB", "tmnxNatFwd2Addr"),
    (0, "TIMETRA-NAT-MIB", "tmnxNatFwd2NatPolicy"),
    (0, "TIMETRA-NAT-MIB", "tmnxNatFwd2Protocol"),
    (0, "TIMETRA-NAT-MIB", "tmnxNatFwd2Port"),
)
if mibBuilder.loadTexts:
    tmnxNatFwd2Entry.setStatus("current")
_TmnxNatFwd2SubType_Type = TmnxNatLegacySubscriberType
_TmnxNatFwd2SubType_Object = MibTableColumn
tmnxNatFwd2SubType = _TmnxNatFwd2SubType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 8, 6, 1, 1),
    _TmnxNatFwd2SubType_Type()
)
tmnxNatFwd2SubType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxNatFwd2SubType.setStatus("current")
_TmnxNatFwd2L2awSubIdent_Type = TmnxSubIdentStringOrEmpty
_TmnxNatFwd2L2awSubIdent_Object = MibTableColumn
tmnxNatFwd2L2awSubIdent = _TmnxNatFwd2L2awSubIdent_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 8, 6, 1, 2),
    _TmnxNatFwd2L2awSubIdent_Type()
)
tmnxNatFwd2L2awSubIdent.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxNatFwd2L2awSubIdent.setStatus("current")
_TmnxNatFwd2LsnVRtrID_Type = TmnxVRtrIDOrZero
_TmnxNatFwd2LsnVRtrID_Object = MibTableColumn
tmnxNatFwd2LsnVRtrID = _TmnxNatFwd2LsnVRtrID_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 8, 6, 1, 3),
    _TmnxNatFwd2LsnVRtrID_Type()
)
tmnxNatFwd2LsnVRtrID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxNatFwd2LsnVRtrID.setStatus("current")
_TmnxNatFwd2LsnB4AddrType_Type = InetAddressType
_TmnxNatFwd2LsnB4AddrType_Object = MibTableColumn
tmnxNatFwd2LsnB4AddrType = _TmnxNatFwd2LsnB4AddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 8, 6, 1, 4),
    _TmnxNatFwd2LsnB4AddrType_Type()
)
tmnxNatFwd2LsnB4AddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxNatFwd2LsnB4AddrType.setStatus("current")


class _TmnxNatFwd2LsnB4Addr_Type(InetAddress):
    """Custom type tmnxNatFwd2LsnB4Addr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(16, 16),
    )


_TmnxNatFwd2LsnB4Addr_Type.__name__ = "InetAddress"
_TmnxNatFwd2LsnB4Addr_Object = MibTableColumn
tmnxNatFwd2LsnB4Addr = _TmnxNatFwd2LsnB4Addr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 8, 6, 1, 5),
    _TmnxNatFwd2LsnB4Addr_Type()
)
tmnxNatFwd2LsnB4Addr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxNatFwd2LsnB4Addr.setStatus("current")
_TmnxNatFwd2AddrType_Type = InetAddressType
_TmnxNatFwd2AddrType_Object = MibTableColumn
tmnxNatFwd2AddrType = _TmnxNatFwd2AddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 8, 6, 1, 6),
    _TmnxNatFwd2AddrType_Type()
)
tmnxNatFwd2AddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxNatFwd2AddrType.setStatus("current")


class _TmnxNatFwd2Addr_Type(InetAddress):
    """Custom type tmnxNatFwd2Addr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxNatFwd2Addr_Type.__name__ = "InetAddress"
_TmnxNatFwd2Addr_Object = MibTableColumn
tmnxNatFwd2Addr = _TmnxNatFwd2Addr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 8, 6, 1, 7),
    _TmnxNatFwd2Addr_Type()
)
tmnxNatFwd2Addr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxNatFwd2Addr.setStatus("current")


class _TmnxNatFwd2Protocol_Type(Unsigned32):
    """Custom type tmnxNatFwd2Protocol based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_TmnxNatFwd2Protocol_Type.__name__ = "Unsigned32"
_TmnxNatFwd2Protocol_Object = MibTableColumn
tmnxNatFwd2Protocol = _TmnxNatFwd2Protocol_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 8, 6, 1, 8),
    _TmnxNatFwd2Protocol_Type()
)
tmnxNatFwd2Protocol.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxNatFwd2Protocol.setStatus("current")
_TmnxNatFwd2Port_Type = InetPortNumber
_TmnxNatFwd2Port_Object = MibTableColumn
tmnxNatFwd2Port = _TmnxNatFwd2Port_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 8, 6, 1, 9),
    _TmnxNatFwd2Port_Type()
)
tmnxNatFwd2Port.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxNatFwd2Port.setStatus("current")
_TmnxNatFwd2NatPolicy_Type = TNamedItemOrEmpty
_TmnxNatFwd2NatPolicy_Object = MibTableColumn
tmnxNatFwd2NatPolicy = _TmnxNatFwd2NatPolicy_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 8, 6, 1, 10),
    _TmnxNatFwd2NatPolicy_Type()
)
tmnxNatFwd2NatPolicy.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxNatFwd2NatPolicy.setStatus("current")
_TmnxNatFwd2OutVRtrID_Type = TmnxVRtrIDOrZero
_TmnxNatFwd2OutVRtrID_Object = MibTableColumn
tmnxNatFwd2OutVRtrID = _TmnxNatFwd2OutVRtrID_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 8, 6, 1, 11),
    _TmnxNatFwd2OutVRtrID_Type()
)
tmnxNatFwd2OutVRtrID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatFwd2OutVRtrID.setStatus("current")
_TmnxNatFwd2OutAddrType_Type = InetAddressType
_TmnxNatFwd2OutAddrType_Object = MibTableColumn
tmnxNatFwd2OutAddrType = _TmnxNatFwd2OutAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 8, 6, 1, 12),
    _TmnxNatFwd2OutAddrType_Type()
)
tmnxNatFwd2OutAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatFwd2OutAddrType.setStatus("current")


class _TmnxNatFwd2OutAddr_Type(InetAddress):
    """Custom type tmnxNatFwd2OutAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
    )


_TmnxNatFwd2OutAddr_Type.__name__ = "InetAddress"
_TmnxNatFwd2OutAddr_Object = MibTableColumn
tmnxNatFwd2OutAddr = _TmnxNatFwd2OutAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 8, 6, 1, 13),
    _TmnxNatFwd2OutAddr_Type()
)
tmnxNatFwd2OutAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatFwd2OutAddr.setStatus("current")
_TmnxNatFwd2OutPort_Type = InetPortNumber
_TmnxNatFwd2OutPort_Object = MibTableColumn
tmnxNatFwd2OutPort = _TmnxNatFwd2OutPort_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 8, 6, 1, 14),
    _TmnxNatFwd2OutPort_Type()
)
tmnxNatFwd2OutPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatFwd2OutPort.setStatus("current")


class _TmnxNatFwd2ExpiryDateAndTime_Type(DateAndTime):
    """Custom type tmnxNatFwd2ExpiryDateAndTime based on DateAndTime"""
    subtypeSpec = DateAndTime.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(11, 11),
    )
    fixed_length = 11


_TmnxNatFwd2ExpiryDateAndTime_Type.__name__ = "DateAndTime"
_TmnxNatFwd2ExpiryDateAndTime_Object = MibTableColumn
tmnxNatFwd2ExpiryDateAndTime = _TmnxNatFwd2ExpiryDateAndTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 8, 6, 1, 15),
    _TmnxNatFwd2ExpiryDateAndTime_Type()
)
tmnxNatFwd2ExpiryDateAndTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatFwd2ExpiryDateAndTime.setStatus("current")
_TmnxNatFwd2LsnAftrAddrType_Type = InetAddressType
_TmnxNatFwd2LsnAftrAddrType_Object = MibTableColumn
tmnxNatFwd2LsnAftrAddrType = _TmnxNatFwd2LsnAftrAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 8, 6, 1, 16),
    _TmnxNatFwd2LsnAftrAddrType_Type()
)
tmnxNatFwd2LsnAftrAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatFwd2LsnAftrAddrType.setStatus("current")


class _TmnxNatFwd2LsnAftrAddr_Type(InetAddress):
    """Custom type tmnxNatFwd2LsnAftrAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(16, 16),
    )


_TmnxNatFwd2LsnAftrAddr_Type.__name__ = "InetAddress"
_TmnxNatFwd2LsnAftrAddr_Object = MibTableColumn
tmnxNatFwd2LsnAftrAddr = _TmnxNatFwd2LsnAftrAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 8, 6, 1, 17),
    _TmnxNatFwd2LsnAftrAddr_Type()
)
tmnxNatFwd2LsnAftrAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatFwd2LsnAftrAddr.setStatus("current")
_TmnxNatFwd2PersistKey_Type = Unsigned32
_TmnxNatFwd2PersistKey_Object = MibTableColumn
tmnxNatFwd2PersistKey = _TmnxNatFwd2PersistKey_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 8, 6, 1, 18),
    _TmnxNatFwd2PersistKey_Type()
)
tmnxNatFwd2PersistKey.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatFwd2PersistKey.setStatus("current")
_TmnxNatFwd2Description_Type = TmnxNatFwdEntryDescription
_TmnxNatFwd2Description_Object = MibTableColumn
tmnxNatFwd2Description = _TmnxNatFwd2Description_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 8, 6, 1, 19),
    _TmnxNatFwd2Description_Type()
)
tmnxNatFwd2Description.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatFwd2Description.setStatus("current")


class _TmnxNatFwd2Origin_Type(Integer32):
    """Custom type tmnxNatFwd2Origin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dynamic", 1),
          ("static", 2))
    )


_TmnxNatFwd2Origin_Type.__name__ = "Integer32"
_TmnxNatFwd2Origin_Object = MibTableColumn
tmnxNatFwd2Origin = _TmnxNatFwd2Origin_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 8, 6, 1, 20),
    _TmnxNatFwd2Origin_Type()
)
tmnxNatFwd2Origin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatFwd2Origin.setStatus("current")
_TmnxNatFwd2ProtocolVersion_Type = Unsigned32
_TmnxNatFwd2ProtocolVersion_Object = MibTableColumn
tmnxNatFwd2ProtocolVersion = _TmnxNatFwd2ProtocolVersion_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 8, 6, 1, 21),
    _TmnxNatFwd2ProtocolVersion_Type()
)
tmnxNatFwd2ProtocolVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatFwd2ProtocolVersion.setStatus("current")


class _TmnxNatFwd2MappingNumber_Type(OctetString):
    """Custom type tmnxNatFwd2MappingNumber based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(12, 12),
    )
    fixed_length = 12


_TmnxNatFwd2MappingNumber_Type.__name__ = "OctetString"
_TmnxNatFwd2MappingNumber_Object = MibTableColumn
tmnxNatFwd2MappingNumber = _TmnxNatFwd2MappingNumber_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 8, 6, 1, 22),
    _TmnxNatFwd2MappingNumber_Type()
)
tmnxNatFwd2MappingNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatFwd2MappingNumber.setStatus("current")
_TmnxNatFwd2OperState_Type = ServiceOperStatus
_TmnxNatFwd2OperState_Object = MibTableColumn
tmnxNatFwd2OperState = _TmnxNatFwd2OperState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 8, 6, 1, 23),
    _TmnxNatFwd2OperState_Type()
)
tmnxNatFwd2OperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatFwd2OperState.setStatus("current")
_TmnxNatFwd2Persistence_Type = TruthValue
_TmnxNatFwd2Persistence_Object = MibTableColumn
tmnxNatFwd2Persistence = _TmnxNatFwd2Persistence_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 8, 6, 1, 24),
    _TmnxNatFwd2Persistence_Type()
)
tmnxNatFwd2Persistence.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatFwd2Persistence.setStatus("current")
_TmnxNatFwd2ForeignPfxType_Type = InetAddressType
_TmnxNatFwd2ForeignPfxType_Object = MibTableColumn
tmnxNatFwd2ForeignPfxType = _TmnxNatFwd2ForeignPfxType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 8, 6, 1, 25),
    _TmnxNatFwd2ForeignPfxType_Type()
)
tmnxNatFwd2ForeignPfxType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatFwd2ForeignPfxType.setStatus("current")


class _TmnxNatFwd2ForeignPfx_Type(InetAddress):
    """Custom type tmnxNatFwd2ForeignPfx based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(16, 16),
    )


_TmnxNatFwd2ForeignPfx_Type.__name__ = "InetAddress"
_TmnxNatFwd2ForeignPfx_Object = MibTableColumn
tmnxNatFwd2ForeignPfx = _TmnxNatFwd2ForeignPfx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 8, 6, 1, 26),
    _TmnxNatFwd2ForeignPfx_Type()
)
tmnxNatFwd2ForeignPfx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatFwd2ForeignPfx.setStatus("current")
_TmnxNatFwd2ForeignPfxLength_Type = InetAddressPrefixLength
_TmnxNatFwd2ForeignPfxLength_Object = MibTableColumn
tmnxNatFwd2ForeignPfxLength = _TmnxNatFwd2ForeignPfxLength_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 8, 6, 1, 27),
    _TmnxNatFwd2ForeignPfxLength_Type()
)
tmnxNatFwd2ForeignPfxLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatFwd2ForeignPfxLength.setStatus("current")
_TmnxNatFwd2ForeignPort_Type = Integer32
_TmnxNatFwd2ForeignPort_Object = MibTableColumn
tmnxNatFwd2ForeignPort = _TmnxNatFwd2ForeignPort_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 8, 6, 1, 28),
    _TmnxNatFwd2ForeignPort_Type()
)
tmnxNatFwd2ForeignPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatFwd2ForeignPort.setStatus("current")
_TmnxNatFwd2OutService_Type = TmnxServId
_TmnxNatFwd2OutService_Object = MibTableColumn
tmnxNatFwd2OutService = _TmnxNatFwd2OutService_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 8, 6, 1, 29),
    _TmnxNatFwd2OutService_Type()
)
tmnxNatFwd2OutService.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatFwd2OutService.setStatus("current")
_TmnxNatFwd2AddrCpm_Type = TruthValue
_TmnxNatFwd2AddrCpm_Object = MibTableColumn
tmnxNatFwd2AddrCpm = _TmnxNatFwd2AddrCpm_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 8, 6, 1, 31),
    _TmnxNatFwd2AddrCpm_Type()
)
tmnxNatFwd2AddrCpm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatFwd2AddrCpm.setStatus("current")
_TmnxNatFwd2OutPublicIf_Type = TruthValue
_TmnxNatFwd2OutPublicIf_Object = MibTableColumn
tmnxNatFwd2OutPublicIf = _TmnxNatFwd2OutPublicIf_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 8, 6, 1, 32),
    _TmnxNatFwd2OutPublicIf_Type()
)
tmnxNatFwd2OutPublicIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatFwd2OutPublicIf.setStatus("current")
_TmnxNatFwdL2AwTable_Object = MibTable
tmnxNatFwdL2AwTable = _TmnxNatFwdL2AwTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 8, 7)
)
if mibBuilder.loadTexts:
    tmnxNatFwdL2AwTable.setStatus("current")
_TmnxNatFwdL2AwEntry_Object = MibTableRow
tmnxNatFwdL2AwEntry = _TmnxNatFwdL2AwEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 8, 7, 1)
)
tmnxNatFwdL2AwEntry.setIndexNames(
    (0, "TIMETRA-NAT-MIB", "tmnxNatFwdL2AwSubIdent"),
    (0, "TIMETRA-NAT-MIB", "tmnxNatFwdL2AwAddrType"),
    (0, "TIMETRA-NAT-MIB", "tmnxNatFwdL2AwAddr"),
    (0, "TIMETRA-NAT-MIB", "tmnxNatFwdL2AwNatPolicy"),
    (0, "TIMETRA-NAT-MIB", "tmnxNatFwdL2AwProtocol"),
    (0, "TIMETRA-NAT-MIB", "tmnxNatFwdL2AwPort"),
)
if mibBuilder.loadTexts:
    tmnxNatFwdL2AwEntry.setStatus("current")
_TmnxNatFwdL2AwSubIdent_Type = TmnxSubIdentStringOrEmpty
_TmnxNatFwdL2AwSubIdent_Object = MibTableColumn
tmnxNatFwdL2AwSubIdent = _TmnxNatFwdL2AwSubIdent_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 8, 7, 1, 1),
    _TmnxNatFwdL2AwSubIdent_Type()
)
tmnxNatFwdL2AwSubIdent.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxNatFwdL2AwSubIdent.setStatus("current")
_TmnxNatFwdL2AwAddrType_Type = InetAddressType
_TmnxNatFwdL2AwAddrType_Object = MibTableColumn
tmnxNatFwdL2AwAddrType = _TmnxNatFwdL2AwAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 8, 7, 1, 2),
    _TmnxNatFwdL2AwAddrType_Type()
)
tmnxNatFwdL2AwAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxNatFwdL2AwAddrType.setStatus("current")


class _TmnxNatFwdL2AwAddr_Type(InetAddress):
    """Custom type tmnxNatFwdL2AwAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
    )


_TmnxNatFwdL2AwAddr_Type.__name__ = "InetAddress"
_TmnxNatFwdL2AwAddr_Object = MibTableColumn
tmnxNatFwdL2AwAddr = _TmnxNatFwdL2AwAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 8, 7, 1, 3),
    _TmnxNatFwdL2AwAddr_Type()
)
tmnxNatFwdL2AwAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxNatFwdL2AwAddr.setStatus("current")
_TmnxNatFwdL2AwNatPolicy_Type = TNamedItemOrEmpty
_TmnxNatFwdL2AwNatPolicy_Object = MibTableColumn
tmnxNatFwdL2AwNatPolicy = _TmnxNatFwdL2AwNatPolicy_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 8, 7, 1, 4),
    _TmnxNatFwdL2AwNatPolicy_Type()
)
tmnxNatFwdL2AwNatPolicy.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxNatFwdL2AwNatPolicy.setStatus("current")


class _TmnxNatFwdL2AwProtocol_Type(Unsigned32):
    """Custom type tmnxNatFwdL2AwProtocol based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_TmnxNatFwdL2AwProtocol_Type.__name__ = "Unsigned32"
_TmnxNatFwdL2AwProtocol_Object = MibTableColumn
tmnxNatFwdL2AwProtocol = _TmnxNatFwdL2AwProtocol_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 8, 7, 1, 5),
    _TmnxNatFwdL2AwProtocol_Type()
)
tmnxNatFwdL2AwProtocol.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxNatFwdL2AwProtocol.setStatus("current")
_TmnxNatFwdL2AwPort_Type = InetPortNumber
_TmnxNatFwdL2AwPort_Object = MibTableColumn
tmnxNatFwdL2AwPort = _TmnxNatFwdL2AwPort_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 8, 7, 1, 6),
    _TmnxNatFwdL2AwPort_Type()
)
tmnxNatFwdL2AwPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxNatFwdL2AwPort.setStatus("current")
_TmnxNatFwdL2AwOutVRtrID_Type = TmnxVRtrIDOrZero
_TmnxNatFwdL2AwOutVRtrID_Object = MibTableColumn
tmnxNatFwdL2AwOutVRtrID = _TmnxNatFwdL2AwOutVRtrID_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 8, 7, 1, 11),
    _TmnxNatFwdL2AwOutVRtrID_Type()
)
tmnxNatFwdL2AwOutVRtrID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatFwdL2AwOutVRtrID.setStatus("current")
_TmnxNatFwdL2AwOutAddrType_Type = InetAddressType
_TmnxNatFwdL2AwOutAddrType_Object = MibTableColumn
tmnxNatFwdL2AwOutAddrType = _TmnxNatFwdL2AwOutAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 8, 7, 1, 12),
    _TmnxNatFwdL2AwOutAddrType_Type()
)
tmnxNatFwdL2AwOutAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatFwdL2AwOutAddrType.setStatus("current")


class _TmnxNatFwdL2AwOutAddr_Type(InetAddress):
    """Custom type tmnxNatFwdL2AwOutAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
    )


_TmnxNatFwdL2AwOutAddr_Type.__name__ = "InetAddress"
_TmnxNatFwdL2AwOutAddr_Object = MibTableColumn
tmnxNatFwdL2AwOutAddr = _TmnxNatFwdL2AwOutAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 8, 7, 1, 13),
    _TmnxNatFwdL2AwOutAddr_Type()
)
tmnxNatFwdL2AwOutAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatFwdL2AwOutAddr.setStatus("current")
_TmnxNatFwdL2AwOutPort_Type = InetPortNumber
_TmnxNatFwdL2AwOutPort_Object = MibTableColumn
tmnxNatFwdL2AwOutPort = _TmnxNatFwdL2AwOutPort_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 8, 7, 1, 14),
    _TmnxNatFwdL2AwOutPort_Type()
)
tmnxNatFwdL2AwOutPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatFwdL2AwOutPort.setStatus("current")


class _TmnxNatFwdL2AwExpiryDateAndTime_Type(DateAndTime):
    """Custom type tmnxNatFwdL2AwExpiryDateAndTime based on DateAndTime"""
    subtypeSpec = DateAndTime.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(11, 11),
    )
    fixed_length = 11


_TmnxNatFwdL2AwExpiryDateAndTime_Type.__name__ = "DateAndTime"
_TmnxNatFwdL2AwExpiryDateAndTime_Object = MibTableColumn
tmnxNatFwdL2AwExpiryDateAndTime = _TmnxNatFwdL2AwExpiryDateAndTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 8, 7, 1, 15),
    _TmnxNatFwdL2AwExpiryDateAndTime_Type()
)
tmnxNatFwdL2AwExpiryDateAndTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatFwdL2AwExpiryDateAndTime.setStatus("current")
_TmnxNatFwdL2AwPersistKey_Type = Unsigned32
_TmnxNatFwdL2AwPersistKey_Object = MibTableColumn
tmnxNatFwdL2AwPersistKey = _TmnxNatFwdL2AwPersistKey_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 8, 7, 1, 18),
    _TmnxNatFwdL2AwPersistKey_Type()
)
tmnxNatFwdL2AwPersistKey.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatFwdL2AwPersistKey.setStatus("current")


class _TmnxNatFwdL2AwOrigin_Type(Integer32):
    """Custom type tmnxNatFwdL2AwOrigin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dynamic", 1),
          ("static", 2))
    )


_TmnxNatFwdL2AwOrigin_Type.__name__ = "Integer32"
_TmnxNatFwdL2AwOrigin_Object = MibTableColumn
tmnxNatFwdL2AwOrigin = _TmnxNatFwdL2AwOrigin_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 8, 7, 1, 20),
    _TmnxNatFwdL2AwOrigin_Type()
)
tmnxNatFwdL2AwOrigin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatFwdL2AwOrigin.setStatus("current")
_TmnxNatFwdL2AwOperState_Type = ServiceOperStatus
_TmnxNatFwdL2AwOperState_Object = MibTableColumn
tmnxNatFwdL2AwOperState = _TmnxNatFwdL2AwOperState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 8, 7, 1, 23),
    _TmnxNatFwdL2AwOperState_Type()
)
tmnxNatFwdL2AwOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatFwdL2AwOperState.setStatus("current")
_TmnxNatFwdL2AwPersistence_Type = TruthValue
_TmnxNatFwdL2AwPersistence_Object = MibTableColumn
tmnxNatFwdL2AwPersistence = _TmnxNatFwdL2AwPersistence_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 8, 7, 1, 24),
    _TmnxNatFwdL2AwPersistence_Type()
)
tmnxNatFwdL2AwPersistence.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatFwdL2AwPersistence.setStatus("current")
_TmnxNatFwdL2AwOutService_Type = TmnxServId
_TmnxNatFwdL2AwOutService_Object = MibTableColumn
tmnxNatFwdL2AwOutService = _TmnxNatFwdL2AwOutService_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 8, 7, 1, 29),
    _TmnxNatFwdL2AwOutService_Type()
)
tmnxNatFwdL2AwOutService.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatFwdL2AwOutService.setStatus("current")
_TmnxNatAccObjs_ObjectIdentity = ObjectIdentity
tmnxNatAccObjs = _TmnxNatAccObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 9)
)
_TmnxNatApTable_Object = MibTable
tmnxNatApTable = _TmnxNatApTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 9, 1)
)
if mibBuilder.loadTexts:
    tmnxNatApTable.setStatus("obsolete")
_TmnxNatApEntry_Object = MibTableRow
tmnxNatApEntry = _TmnxNatApEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 9, 1, 1)
)
tmnxNatApEntry.setIndexNames(
    (1, "TIMETRA-NAT-MIB", "tmnxNatApName"),
)
if mibBuilder.loadTexts:
    tmnxNatApEntry.setStatus("obsolete")
_TmnxNatApName_Type = TNamedItem
_TmnxNatApName_Object = MibTableColumn
tmnxNatApName = _TmnxNatApName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 9, 1, 1, 1),
    _TmnxNatApName_Type()
)
tmnxNatApName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxNatApName.setStatus("obsolete")
_TmnxNatApLastMgmtChange_Type = TimeStamp
_TmnxNatApLastMgmtChange_Object = MibTableColumn
tmnxNatApLastMgmtChange = _TmnxNatApLastMgmtChange_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 9, 1, 1, 2),
    _TmnxNatApLastMgmtChange_Type()
)
tmnxNatApLastMgmtChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatApLastMgmtChange.setStatus("obsolete")
_TmnxNatApRowStatus_Type = RowStatus
_TmnxNatApRowStatus_Object = MibTableColumn
tmnxNatApRowStatus = _TmnxNatApRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 9, 1, 1, 3),
    _TmnxNatApRowStatus_Type()
)
tmnxNatApRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxNatApRowStatus.setStatus("obsolete")


class _TmnxNatApDescription_Type(TItemDescription):
    """Custom type tmnxNatApDescription based on TItemDescription"""
    defaultValue = OctetString("")


_TmnxNatApDescription_Type.__name__ = "TItemDescription"
_TmnxNatApDescription_Object = MibTableColumn
tmnxNatApDescription = _TmnxNatApDescription_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 9, 1, 1, 4),
    _TmnxNatApDescription_Type()
)
tmnxNatApDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxNatApDescription.setStatus("obsolete")


class _TmnxNatApIncludeAttributes_Type(Bits):
    """Custom type tmnxNatApIncludeAttributes based on Bits"""
    defaultBinValue = "0"

    namedValues = NamedValues(
        *(("framedIpAddr", 0),
          ("nasIdentifier", 1),
          ("natSubscriberString", 2),
          ("userName", 3),
          ("insideServiceId", 4),
          ("outsideServiceId", 5),
          ("outsideIp", 6),
          ("portRangeBlock", 7),
          ("hardwareTimestamp", 8),
          ("releaseReason", 9),
          ("multiSessionId", 10),
          ("frameCounters", 11),
          ("octetCounters", 12),
          ("sessionTime", 13),
          ("calledStationId", 14),
          ("subscriberData", 15))
    )

_TmnxNatApIncludeAttributes_Type.__name__ = "Bits"
_TmnxNatApIncludeAttributes_Object = MibTableColumn
tmnxNatApIncludeAttributes = _TmnxNatApIncludeAttributes_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 9, 1, 1, 5),
    _TmnxNatApIncludeAttributes_Type()
)
tmnxNatApIncludeAttributes.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxNatApIncludeAttributes.setStatus("obsolete")


class _TmnxNatApServersTimeout_Type(Unsigned32):
    """Custom type tmnxNatApServersTimeout based on Unsigned32"""
    defaultValue = 5

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 90),
    )


_TmnxNatApServersTimeout_Type.__name__ = "Unsigned32"
_TmnxNatApServersTimeout_Object = MibTableColumn
tmnxNatApServersTimeout = _TmnxNatApServersTimeout_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 9, 1, 1, 100),
    _TmnxNatApServersTimeout_Type()
)
tmnxNatApServersTimeout.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxNatApServersTimeout.setStatus("obsolete")
if mibBuilder.loadTexts:
    tmnxNatApServersTimeout.setUnits("seconds")


class _TmnxNatApServersRetry_Type(Unsigned32):
    """Custom type tmnxNatApServersRetry based on Unsigned32"""
    defaultValue = 3

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_TmnxNatApServersRetry_Type.__name__ = "Unsigned32"
_TmnxNatApServersRetry_Object = MibTableColumn
tmnxNatApServersRetry = _TmnxNatApServersRetry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 9, 1, 1, 101),
    _TmnxNatApServersRetry_Type()
)
tmnxNatApServersRetry.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxNatApServersRetry.setStatus("obsolete")


class _TmnxNatApServersVRtrID_Type(TmnxVRtrIDOrZero):
    """Custom type tmnxNatApServersVRtrID based on TmnxVRtrIDOrZero"""
    defaultValue = 0


_TmnxNatApServersVRtrID_Type.__name__ = "TmnxVRtrIDOrZero"
_TmnxNatApServersVRtrID_Object = MibTableColumn
tmnxNatApServersVRtrID = _TmnxNatApServersVRtrID_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 9, 1, 1, 102),
    _TmnxNatApServersVRtrID_Type()
)
tmnxNatApServersVRtrID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxNatApServersVRtrID.setStatus("obsolete")


class _TmnxNatApServersSrcAddrType_Type(InetAddressType):
    """Custom type tmnxNatApServersSrcAddrType based on InetAddressType"""
    defaultValue = 0


_TmnxNatApServersSrcAddrType_Type.__name__ = "InetAddressType"
_TmnxNatApServersSrcAddrType_Object = MibTableColumn
tmnxNatApServersSrcAddrType = _TmnxNatApServersSrcAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 9, 1, 1, 103),
    _TmnxNatApServersSrcAddrType_Type()
)
tmnxNatApServersSrcAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxNatApServersSrcAddrType.setStatus("obsolete")


class _TmnxNatApServersSrcAddrStart_Type(InetAddress):
    """Custom type tmnxNatApServersSrcAddrStart based on InetAddress"""
    defaultHexValue = ""

    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxNatApServersSrcAddrStart_Type.__name__ = "InetAddress"
_TmnxNatApServersSrcAddrStart_Object = MibTableColumn
tmnxNatApServersSrcAddrStart = _TmnxNatApServersSrcAddrStart_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 9, 1, 1, 104),
    _TmnxNatApServersSrcAddrStart_Type()
)
tmnxNatApServersSrcAddrStart.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxNatApServersSrcAddrStart.setStatus("obsolete")


class _TmnxNatApServersSrcAddrEnd_Type(InetAddress):
    """Custom type tmnxNatApServersSrcAddrEnd based on InetAddress"""
    defaultHexValue = ""

    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxNatApServersSrcAddrEnd_Type.__name__ = "InetAddress"
_TmnxNatApServersSrcAddrEnd_Object = MibTableColumn
tmnxNatApServersSrcAddrEnd = _TmnxNatApServersSrcAddrEnd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 9, 1, 1, 105),
    _TmnxNatApServersSrcAddrEnd_Type()
)
tmnxNatApServersSrcAddrEnd.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxNatApServersSrcAddrEnd.setStatus("obsolete")


class _TmnxNatApServersAlgorithm_Type(TmnxSubRadServAlgorithm):
    """Custom type tmnxNatApServersAlgorithm based on TmnxSubRadServAlgorithm"""
    defaultValue = 1

    subtypeSpec = TmnxSubRadServAlgorithm.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("direct", 1),
          ("roundRobin", 2))
    )


_TmnxNatApServersAlgorithm_Type.__name__ = "TmnxSubRadServAlgorithm"
_TmnxNatApServersAlgorithm_Object = MibTableColumn
tmnxNatApServersAlgorithm = _TmnxNatApServersAlgorithm_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 9, 1, 1, 106),
    _TmnxNatApServersAlgorithm_Type()
)
tmnxNatApServersAlgorithm.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxNatApServersAlgorithm.setStatus("obsolete")
_TmnxNatApServTable_Object = MibTable
tmnxNatApServTable = _TmnxNatApServTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 9, 2)
)
if mibBuilder.loadTexts:
    tmnxNatApServTable.setStatus("obsolete")
_TmnxNatApServEntry_Object = MibTableRow
tmnxNatApServEntry = _TmnxNatApServEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 9, 2, 1)
)
tmnxNatApServEntry.setIndexNames(
    (0, "TIMETRA-NAT-MIB", "tmnxNatApName"),
    (0, "TIMETRA-NAT-MIB", "tmnxNatApServIndex"),
)
if mibBuilder.loadTexts:
    tmnxNatApServEntry.setStatus("obsolete")


class _TmnxNatApServIndex_Type(Unsigned32):
    """Custom type tmnxNatApServIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_TmnxNatApServIndex_Type.__name__ = "Unsigned32"
_TmnxNatApServIndex_Object = MibTableColumn
tmnxNatApServIndex = _TmnxNatApServIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 9, 2, 1, 1),
    _TmnxNatApServIndex_Type()
)
tmnxNatApServIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxNatApServIndex.setStatus("obsolete")
_TmnxNatApServRowStatus_Type = RowStatus
_TmnxNatApServRowStatus_Object = MibTableColumn
tmnxNatApServRowStatus = _TmnxNatApServRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 9, 2, 1, 2),
    _TmnxNatApServRowStatus_Type()
)
tmnxNatApServRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxNatApServRowStatus.setStatus("obsolete")
_TmnxNatApServLastMgmtChange_Type = TimeStamp
_TmnxNatApServLastMgmtChange_Object = MibTableColumn
tmnxNatApServLastMgmtChange = _TmnxNatApServLastMgmtChange_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 9, 2, 1, 3),
    _TmnxNatApServLastMgmtChange_Type()
)
tmnxNatApServLastMgmtChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatApServLastMgmtChange.setStatus("obsolete")
_TmnxNatApServAddrType_Type = InetAddressType
_TmnxNatApServAddrType_Object = MibTableColumn
tmnxNatApServAddrType = _TmnxNatApServAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 9, 2, 1, 5),
    _TmnxNatApServAddrType_Type()
)
tmnxNatApServAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxNatApServAddrType.setStatus("obsolete")


class _TmnxNatApServAddr_Type(InetAddress):
    """Custom type tmnxNatApServAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxNatApServAddr_Type.__name__ = "InetAddress"
_TmnxNatApServAddr_Object = MibTableColumn
tmnxNatApServAddr = _TmnxNatApServAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 9, 2, 1, 6),
    _TmnxNatApServAddr_Type()
)
tmnxNatApServAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxNatApServAddr.setStatus("obsolete")


class _TmnxNatApServSecret_Type(DisplayString):
    """Custom type tmnxNatApServSecret based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(1, 20),
    )


_TmnxNatApServSecret_Type.__name__ = "DisplayString"
_TmnxNatApServSecret_Object = MibTableColumn
tmnxNatApServSecret = _TmnxNatApServSecret_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 9, 2, 1, 7),
    _TmnxNatApServSecret_Type()
)
tmnxNatApServSecret.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxNatApServSecret.setStatus("obsolete")


class _TmnxNatApServAcctPort_Type(Unsigned32):
    """Custom type tmnxNatApServAcctPort based on Unsigned32"""
    defaultValue = 1813

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_TmnxNatApServAcctPort_Type.__name__ = "Unsigned32"
_TmnxNatApServAcctPort_Object = MibTableColumn
tmnxNatApServAcctPort = _TmnxNatApServAcctPort_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 9, 2, 1, 8),
    _TmnxNatApServAcctPort_Type()
)
tmnxNatApServAcctPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxNatApServAcctPort.setStatus("obsolete")
_TmnxNatApServStatTable_Object = MibTable
tmnxNatApServStatTable = _TmnxNatApServStatTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 9, 3)
)
if mibBuilder.loadTexts:
    tmnxNatApServStatTable.setStatus("obsolete")
_TmnxNatApServStatEntry_Object = MibTableRow
tmnxNatApServStatEntry = _TmnxNatApServStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 9, 3, 1)
)
tmnxNatApServStatEntry.setIndexNames(
    (0, "TIMETRA-NAT-MIB", "tmnxNatApName"),
    (0, "TIMETRA-NAT-MIB", "tmnxNatApServIndex"),
    (0, "TIMETRA-NAT-MIB", "tmnxNatIsaGrpId"),
    (0, "TIMETRA-NAT-MIB", "tmnxNatIsaMemberId"),
)
if mibBuilder.loadTexts:
    tmnxNatApServStatEntry.setStatus("obsolete")
_TmnxNatApServStatSrcAddrType_Type = InetAddressType
_TmnxNatApServStatSrcAddrType_Object = MibTableColumn
tmnxNatApServStatSrcAddrType = _TmnxNatApServStatSrcAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 9, 3, 1, 1),
    _TmnxNatApServStatSrcAddrType_Type()
)
tmnxNatApServStatSrcAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatApServStatSrcAddrType.setStatus("obsolete")


class _TmnxNatApServStatSrcAddr_Type(InetAddress):
    """Custom type tmnxNatApServStatSrcAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxNatApServStatSrcAddr_Type.__name__ = "InetAddress"
_TmnxNatApServStatSrcAddr_Object = MibTableColumn
tmnxNatApServStatSrcAddr = _TmnxNatApServStatSrcAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 9, 3, 1, 2),
    _TmnxNatApServStatSrcAddr_Type()
)
tmnxNatApServStatSrcAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatApServStatSrcAddr.setStatus("obsolete")
_TmnxNatApServStatOperState_Type = TmnxOperState
_TmnxNatApServStatOperState_Object = MibTableColumn
tmnxNatApServStatOperState = _TmnxNatApServStatOperState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 9, 3, 1, 3),
    _TmnxNatApServStatOperState_Type()
)
tmnxNatApServStatOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatApServStatOperState.setStatus("obsolete")
_TmnxNatApServStatTxRequests_Type = Counter32
_TmnxNatApServStatTxRequests_Object = MibTableColumn
tmnxNatApServStatTxRequests = _TmnxNatApServStatTxRequests_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 9, 3, 1, 4),
    _TmnxNatApServStatTxRequests_Type()
)
tmnxNatApServStatTxRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatApServStatTxRequests.setStatus("obsolete")
_TmnxNatApServStatReqTimeout_Type = Counter32
_TmnxNatApServStatReqTimeout_Object = MibTableColumn
tmnxNatApServStatReqTimeout = _TmnxNatApServStatReqTimeout_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 9, 3, 1, 6),
    _TmnxNatApServStatReqTimeout_Type()
)
tmnxNatApServStatReqTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatApServStatReqTimeout.setStatus("obsolete")
_TmnxNatApServStatSendRetries_Type = Counter32
_TmnxNatApServStatSendRetries_Object = MibTableColumn
tmnxNatApServStatSendRetries = _TmnxNatApServStatSendRetries_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 9, 3, 1, 7),
    _TmnxNatApServStatSendRetries_Type()
)
tmnxNatApServStatSendRetries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatApServStatSendRetries.setStatus("obsolete")
_TmnxNatPcpObjs_ObjectIdentity = ObjectIdentity
tmnxNatPcpObjs = _TmnxNatPcpObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 10)
)
_TmnxNatPcpPlcyTable_Object = MibTable
tmnxNatPcpPlcyTable = _TmnxNatPcpPlcyTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 10, 1)
)
if mibBuilder.loadTexts:
    tmnxNatPcpPlcyTable.setStatus("current")
_TmnxNatPcpPlcyEntry_Object = MibTableRow
tmnxNatPcpPlcyEntry = _TmnxNatPcpPlcyEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 10, 1, 1)
)
tmnxNatPcpPlcyEntry.setIndexNames(
    (1, "TIMETRA-NAT-MIB", "tmnxNatPcpPlcyName"),
)
if mibBuilder.loadTexts:
    tmnxNatPcpPlcyEntry.setStatus("current")
_TmnxNatPcpPlcyName_Type = TNamedItem
_TmnxNatPcpPlcyName_Object = MibTableColumn
tmnxNatPcpPlcyName = _TmnxNatPcpPlcyName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 10, 1, 1, 1),
    _TmnxNatPcpPlcyName_Type()
)
tmnxNatPcpPlcyName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxNatPcpPlcyName.setStatus("current")
_TmnxNatPcpPlcyLastMgmtChange_Type = TimeStamp
_TmnxNatPcpPlcyLastMgmtChange_Object = MibTableColumn
tmnxNatPcpPlcyLastMgmtChange = _TmnxNatPcpPlcyLastMgmtChange_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 10, 1, 1, 2),
    _TmnxNatPcpPlcyLastMgmtChange_Type()
)
tmnxNatPcpPlcyLastMgmtChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatPcpPlcyLastMgmtChange.setStatus("current")
_TmnxNatPcpPlcyRowStatus_Type = RowStatus
_TmnxNatPcpPlcyRowStatus_Object = MibTableColumn
tmnxNatPcpPlcyRowStatus = _TmnxNatPcpPlcyRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 10, 1, 1, 3),
    _TmnxNatPcpPlcyRowStatus_Type()
)
tmnxNatPcpPlcyRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxNatPcpPlcyRowStatus.setStatus("current")


class _TmnxNatPcpPlcyDescription_Type(TItemDescription):
    """Custom type tmnxNatPcpPlcyDescription based on TItemDescription"""
    defaultValue = OctetString("")


_TmnxNatPcpPlcyDescription_Type.__name__ = "TItemDescription"
_TmnxNatPcpPlcyDescription_Object = MibTableColumn
tmnxNatPcpPlcyDescription = _TmnxNatPcpPlcyDescription_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 10, 1, 1, 4),
    _TmnxNatPcpPlcyDescription_Type()
)
tmnxNatPcpPlcyDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxNatPcpPlcyDescription.setStatus("current")


class _TmnxNatPcpPlcyOpcodes_Type(Bits):
    """Custom type tmnxNatPcpPlcyOpcodes based on Bits"""
    defaultBinValue = "0"

    namedValues = NamedValues(
        *(("get", 0),
          ("map", 1),
          ("announce", 2))
    )

_TmnxNatPcpPlcyOpcodes_Type.__name__ = "Bits"
_TmnxNatPcpPlcyOpcodes_Object = MibTableColumn
tmnxNatPcpPlcyOpcodes = _TmnxNatPcpPlcyOpcodes_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 10, 1, 1, 5),
    _TmnxNatPcpPlcyOpcodes_Type()
)
tmnxNatPcpPlcyOpcodes.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxNatPcpPlcyOpcodes.setStatus("current")


class _TmnxNatPcpPlcyOptions_Type(Bits):
    """Custom type tmnxNatPcpPlcyOptions based on Bits"""
    defaultBinValue = "0"

    namedValues = NamedValues(
        *(("description", 0),
          ("next", 1),
          ("portReservation", 2),
          ("thirdParty", 3),
          ("preferFailure", 4),
          ("portSet", 5))
    )

_TmnxNatPcpPlcyOptions_Type.__name__ = "Bits"
_TmnxNatPcpPlcyOptions_Object = MibTableColumn
tmnxNatPcpPlcyOptions = _TmnxNatPcpPlcyOptions_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 10, 1, 1, 6),
    _TmnxNatPcpPlcyOptions_Type()
)
tmnxNatPcpPlcyOptions.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxNatPcpPlcyOptions.setStatus("current")


class _TmnxNatPcpPlcyMinimumLifetime_Type(Unsigned32):
    """Custom type tmnxNatPcpPlcyMinimumLifetime based on Unsigned32"""
    defaultValue = 120

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(60, 86399),
    )


_TmnxNatPcpPlcyMinimumLifetime_Type.__name__ = "Unsigned32"
_TmnxNatPcpPlcyMinimumLifetime_Object = MibTableColumn
tmnxNatPcpPlcyMinimumLifetime = _TmnxNatPcpPlcyMinimumLifetime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 10, 1, 1, 7),
    _TmnxNatPcpPlcyMinimumLifetime_Type()
)
tmnxNatPcpPlcyMinimumLifetime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxNatPcpPlcyMinimumLifetime.setStatus("current")
if mibBuilder.loadTexts:
    tmnxNatPcpPlcyMinimumLifetime.setUnits("seconds")


class _TmnxNatPcpPlcyMaximumLifetime_Type(Unsigned32):
    """Custom type tmnxNatPcpPlcyMaximumLifetime based on Unsigned32"""
    defaultValue = 86400

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(61, 86400),
    )


_TmnxNatPcpPlcyMaximumLifetime_Type.__name__ = "Unsigned32"
_TmnxNatPcpPlcyMaximumLifetime_Object = MibTableColumn
tmnxNatPcpPlcyMaximumLifetime = _TmnxNatPcpPlcyMaximumLifetime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 10, 1, 1, 8),
    _TmnxNatPcpPlcyMaximumLifetime_Type()
)
tmnxNatPcpPlcyMaximumLifetime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxNatPcpPlcyMaximumLifetime.setStatus("current")
if mibBuilder.loadTexts:
    tmnxNatPcpPlcyMaximumLifetime.setUnits("seconds")


class _TmnxNatPcpPlcyMaxDescriptionLen_Type(Unsigned32):
    """Custom type tmnxNatPcpPlcyMaxDescriptionLen based on Unsigned32"""
    defaultValue = 64

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_TmnxNatPcpPlcyMaxDescriptionLen_Type.__name__ = "Unsigned32"
_TmnxNatPcpPlcyMaxDescriptionLen_Object = MibTableColumn
tmnxNatPcpPlcyMaxDescriptionLen = _TmnxNatPcpPlcyMaxDescriptionLen_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 10, 1, 1, 9),
    _TmnxNatPcpPlcyMaxDescriptionLen_Type()
)
tmnxNatPcpPlcyMaxDescriptionLen.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxNatPcpPlcyMaxDescriptionLen.setStatus("current")


class _TmnxNatPcpPlcyMinimumVersion_Type(Unsigned32):
    """Custom type tmnxNatPcpPlcyMinimumVersion based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_TmnxNatPcpPlcyMinimumVersion_Type.__name__ = "Unsigned32"
_TmnxNatPcpPlcyMinimumVersion_Object = MibTableColumn
tmnxNatPcpPlcyMinimumVersion = _TmnxNatPcpPlcyMinimumVersion_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 10, 1, 1, 10),
    _TmnxNatPcpPlcyMinimumVersion_Type()
)
tmnxNatPcpPlcyMinimumVersion.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxNatPcpPlcyMinimumVersion.setStatus("current")
if mibBuilder.loadTexts:
    tmnxNatPcpPlcyMinimumVersion.setUnits("seconds")


class _TmnxNatPcpPlcyMaximumVersion_Type(Unsigned32):
    """Custom type tmnxNatPcpPlcyMaximumVersion based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_TmnxNatPcpPlcyMaximumVersion_Type.__name__ = "Unsigned32"
_TmnxNatPcpPlcyMaximumVersion_Object = MibTableColumn
tmnxNatPcpPlcyMaximumVersion = _TmnxNatPcpPlcyMaximumVersion_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 10, 1, 1, 11),
    _TmnxNatPcpPlcyMaximumVersion_Type()
)
tmnxNatPcpPlcyMaximumVersion.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxNatPcpPlcyMaximumVersion.setStatus("current")
if mibBuilder.loadTexts:
    tmnxNatPcpPlcyMaximumVersion.setUnits("seconds")


class _TmnxNatPcpPlcyReuseExtIp_Type(TruthValue):
    """Custom type tmnxNatPcpPlcyReuseExtIp based on TruthValue"""
    defaultValue = 2


_TmnxNatPcpPlcyReuseExtIp_Type.__name__ = "TruthValue"
_TmnxNatPcpPlcyReuseExtIp_Object = MibTableColumn
tmnxNatPcpPlcyReuseExtIp = _TmnxNatPcpPlcyReuseExtIp_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 10, 1, 1, 12),
    _TmnxNatPcpPlcyReuseExtIp_Type()
)
tmnxNatPcpPlcyReuseExtIp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxNatPcpPlcyReuseExtIp.setStatus("current")
_TmnxNatPcpSrvTable_Object = MibTable
tmnxNatPcpSrvTable = _TmnxNatPcpSrvTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 10, 2)
)
if mibBuilder.loadTexts:
    tmnxNatPcpSrvTable.setStatus("current")
_TmnxNatPcpSrvEntry_Object = MibTableRow
tmnxNatPcpSrvEntry = _TmnxNatPcpSrvEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 10, 2, 1)
)
tmnxNatPcpSrvEntry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (1, "TIMETRA-NAT-MIB", "tmnxNatPcpSrvName"),
)
if mibBuilder.loadTexts:
    tmnxNatPcpSrvEntry.setStatus("current")
_TmnxNatPcpSrvName_Type = TNamedItem
_TmnxNatPcpSrvName_Object = MibTableColumn
tmnxNatPcpSrvName = _TmnxNatPcpSrvName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 10, 2, 1, 1),
    _TmnxNatPcpSrvName_Type()
)
tmnxNatPcpSrvName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxNatPcpSrvName.setStatus("current")
_TmnxNatPcpSrvLastCh_Type = TimeStamp
_TmnxNatPcpSrvLastCh_Object = MibTableColumn
tmnxNatPcpSrvLastCh = _TmnxNatPcpSrvLastCh_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 10, 2, 1, 2),
    _TmnxNatPcpSrvLastCh_Type()
)
tmnxNatPcpSrvLastCh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatPcpSrvLastCh.setStatus("current")
_TmnxNatPcpSrvRowStatus_Type = RowStatus
_TmnxNatPcpSrvRowStatus_Object = MibTableColumn
tmnxNatPcpSrvRowStatus = _TmnxNatPcpSrvRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 10, 2, 1, 3),
    _TmnxNatPcpSrvRowStatus_Type()
)
tmnxNatPcpSrvRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxNatPcpSrvRowStatus.setStatus("current")


class _TmnxNatPcpSrvAdminState_Type(TmnxAdminState):
    """Custom type tmnxNatPcpSrvAdminState based on TmnxAdminState"""
    defaultValue = 3


_TmnxNatPcpSrvAdminState_Type.__name__ = "TmnxAdminState"
_TmnxNatPcpSrvAdminState_Object = MibTableColumn
tmnxNatPcpSrvAdminState = _TmnxNatPcpSrvAdminState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 10, 2, 1, 4),
    _TmnxNatPcpSrvAdminState_Type()
)
tmnxNatPcpSrvAdminState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxNatPcpSrvAdminState.setStatus("current")


class _TmnxNatPcpSrvDescription_Type(TItemDescription):
    """Custom type tmnxNatPcpSrvDescription based on TItemDescription"""
    defaultValue = OctetString("")


_TmnxNatPcpSrvDescription_Type.__name__ = "TItemDescription"
_TmnxNatPcpSrvDescription_Object = MibTableColumn
tmnxNatPcpSrvDescription = _TmnxNatPcpSrvDescription_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 10, 2, 1, 5),
    _TmnxNatPcpSrvDescription_Type()
)
tmnxNatPcpSrvDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxNatPcpSrvDescription.setStatus("current")


class _TmnxNatPcpSrvPlcy_Type(TNamedItemOrEmpty):
    """Custom type tmnxNatPcpSrvPlcy based on TNamedItemOrEmpty"""
    defaultValue = OctetString("")


_TmnxNatPcpSrvPlcy_Type.__name__ = "TNamedItemOrEmpty"
_TmnxNatPcpSrvPlcy_Object = MibTableColumn
tmnxNatPcpSrvPlcy = _TmnxNatPcpSrvPlcy_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 10, 2, 1, 6),
    _TmnxNatPcpSrvPlcy_Type()
)
tmnxNatPcpSrvPlcy.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxNatPcpSrvPlcy.setStatus("current")


class _TmnxNatPcpSrvFwdInsideRouter_Type(TmnxVRtrIDOrZero):
    """Custom type tmnxNatPcpSrvFwdInsideRouter based on TmnxVRtrIDOrZero"""
    defaultValue = 0


_TmnxNatPcpSrvFwdInsideRouter_Type.__name__ = "TmnxVRtrIDOrZero"
_TmnxNatPcpSrvFwdInsideRouter_Object = MibTableColumn
tmnxNatPcpSrvFwdInsideRouter = _TmnxNatPcpSrvFwdInsideRouter_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 10, 2, 1, 7),
    _TmnxNatPcpSrvFwdInsideRouter_Type()
)
tmnxNatPcpSrvFwdInsideRouter.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxNatPcpSrvFwdInsideRouter.setStatus("current")


class _TmnxNatPcpSrvDsliteAftrAddr_Type(InetAddressIPv6):
    """Custom type tmnxNatPcpSrvDsliteAftrAddr based on InetAddressIPv6"""
    defaultHexValue = "00000000000000000000000000000000"


_TmnxNatPcpSrvDsliteAftrAddr_Type.__name__ = "InetAddressIPv6"
_TmnxNatPcpSrvDsliteAftrAddr_Object = MibTableColumn
tmnxNatPcpSrvDsliteAftrAddr = _TmnxNatPcpSrvDsliteAftrAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 10, 2, 1, 8),
    _TmnxNatPcpSrvDsliteAftrAddr_Type()
)
tmnxNatPcpSrvDsliteAftrAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxNatPcpSrvDsliteAftrAddr.setStatus("current")
_TmnxNatPcpSrvState_Type = TmnxOperState
_TmnxNatPcpSrvState_Object = MibTableColumn
tmnxNatPcpSrvState = _TmnxNatPcpSrvState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 10, 2, 1, 9),
    _TmnxNatPcpSrvState_Type()
)
tmnxNatPcpSrvState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatPcpSrvState.setStatus("current")


class _TmnxNatPcpSrvStateDescription_Type(DisplayString):
    """Custom type tmnxNatPcpSrvStateDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_TmnxNatPcpSrvStateDescription_Type.__name__ = "DisplayString"
_TmnxNatPcpSrvStateDescription_Object = MibTableColumn
tmnxNatPcpSrvStateDescription = _TmnxNatPcpSrvStateDescription_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 10, 2, 1, 10),
    _TmnxNatPcpSrvStateDescription_Type()
)
tmnxNatPcpSrvStateDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatPcpSrvStateDescription.setStatus("current")


class _TmnxNatPcpSrvEpoch_Type(Unsigned32):
    """Custom type tmnxNatPcpSrvEpoch based on Unsigned32"""
    defaultValue = 0


_TmnxNatPcpSrvEpoch_Type.__name__ = "Unsigned32"
_TmnxNatPcpSrvEpoch_Object = MibTableColumn
tmnxNatPcpSrvEpoch = _TmnxNatPcpSrvEpoch_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 10, 2, 1, 11),
    _TmnxNatPcpSrvEpoch_Type()
)
tmnxNatPcpSrvEpoch.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxNatPcpSrvEpoch.setStatus("current")
_TmnxNatPcpSrvIfTable_Object = MibTable
tmnxNatPcpSrvIfTable = _TmnxNatPcpSrvIfTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 10, 3)
)
if mibBuilder.loadTexts:
    tmnxNatPcpSrvIfTable.setStatus("current")
_TmnxNatPcpSrvIfEntry_Object = MibTableRow
tmnxNatPcpSrvIfEntry = _TmnxNatPcpSrvIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 10, 3, 1)
)
tmnxNatPcpSrvIfEntry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "TIMETRA-NAT-MIB", "tmnxNatPcpSrvName"),
    (0, "TIMETRA-VRTR-MIB", "vRtrIfIndex"),
)
if mibBuilder.loadTexts:
    tmnxNatPcpSrvIfEntry.setStatus("current")
_TmnxNatPcpSrvIfRowStatus_Type = RowStatus
_TmnxNatPcpSrvIfRowStatus_Object = MibTableColumn
tmnxNatPcpSrvIfRowStatus = _TmnxNatPcpSrvIfRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 10, 3, 1, 1),
    _TmnxNatPcpSrvIfRowStatus_Type()
)
tmnxNatPcpSrvIfRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxNatPcpSrvIfRowStatus.setStatus("current")
_TmnxNatPcpSrvIfLastCh_Type = TimeStamp
_TmnxNatPcpSrvIfLastCh_Object = MibTableColumn
tmnxNatPcpSrvIfLastCh = _TmnxNatPcpSrvIfLastCh_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 10, 3, 1, 2),
    _TmnxNatPcpSrvIfLastCh_Type()
)
tmnxNatPcpSrvIfLastCh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatPcpSrvIfLastCh.setStatus("current")
_TmnxNatPcpSrvIfStatsTable_Object = MibTable
tmnxNatPcpSrvIfStatsTable = _TmnxNatPcpSrvIfStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 10, 4)
)
if mibBuilder.loadTexts:
    tmnxNatPcpSrvIfStatsTable.setStatus("current")
_TmnxNatPcpSrvIfStatsEntry_Object = MibTableRow
tmnxNatPcpSrvIfStatsEntry = _TmnxNatPcpSrvIfStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 10, 4, 1)
)
tmnxNatPcpSrvIfStatsEntry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "TIMETRA-NAT-MIB", "tmnxNatPcpSrvName"),
    (0, "TIMETRA-VRTR-MIB", "vRtrIfIndex"),
    (0, "TIMETRA-NAT-MIB", "tmnxNatPcpSrvIfStatsType"),
)
if mibBuilder.loadTexts:
    tmnxNatPcpSrvIfStatsEntry.setStatus("current")


class _TmnxNatPcpSrvIfStatsType_Type(Unsigned32):
    """Custom type tmnxNatPcpSrvIfStatsType based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 53),
    )


_TmnxNatPcpSrvIfStatsType_Type.__name__ = "Unsigned32"
_TmnxNatPcpSrvIfStatsType_Object = MibTableColumn
tmnxNatPcpSrvIfStatsType = _TmnxNatPcpSrvIfStatsType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 10, 4, 1, 1),
    _TmnxNatPcpSrvIfStatsType_Type()
)
tmnxNatPcpSrvIfStatsType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxNatPcpSrvIfStatsType.setStatus("current")


class _TmnxNatPcpSrvIfStatsName_Type(DisplayString):
    """Custom type tmnxNatPcpSrvIfStatsName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 58),
    )


_TmnxNatPcpSrvIfStatsName_Type.__name__ = "DisplayString"
_TmnxNatPcpSrvIfStatsName_Object = MibTableColumn
tmnxNatPcpSrvIfStatsName = _TmnxNatPcpSrvIfStatsName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 10, 4, 1, 2),
    _TmnxNatPcpSrvIfStatsName_Type()
)
tmnxNatPcpSrvIfStatsName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatPcpSrvIfStatsName.setStatus("current")
_TmnxNatPcpSrvIfStatsValLw_Type = Counter32
_TmnxNatPcpSrvIfStatsValLw_Object = MibTableColumn
tmnxNatPcpSrvIfStatsValLw = _TmnxNatPcpSrvIfStatsValLw_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 10, 4, 1, 3),
    _TmnxNatPcpSrvIfStatsValLw_Type()
)
tmnxNatPcpSrvIfStatsValLw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatPcpSrvIfStatsValLw.setStatus("current")
_TmnxNatPcpSrvIfStatsValHw_Type = Counter32
_TmnxNatPcpSrvIfStatsValHw_Object = MibTableColumn
tmnxNatPcpSrvIfStatsValHw = _TmnxNatPcpSrvIfStatsValHw_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 10, 4, 1, 4),
    _TmnxNatPcpSrvIfStatsValHw_Type()
)
tmnxNatPcpSrvIfStatsValHw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatPcpSrvIfStatsValHw.setStatus("current")
_TmnxNatPcpSrvIfStatsVal_Type = Counter64
_TmnxNatPcpSrvIfStatsVal_Object = MibTableColumn
tmnxNatPcpSrvIfStatsVal = _TmnxNatPcpSrvIfStatsVal_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 10, 4, 1, 5),
    _TmnxNatPcpSrvIfStatsVal_Type()
)
tmnxNatPcpSrvIfStatsVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatPcpSrvIfStatsVal.setStatus("current")
_TmnxNatSubscIdObjs_ObjectIdentity = ObjectIdentity
tmnxNatSubscIdObjs = _TmnxNatSubscIdObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 11)
)
_TmnxNatSubscIdVendorTable_Object = MibTable
tmnxNatSubscIdVendorTable = _TmnxNatSubscIdVendorTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 11, 1)
)
if mibBuilder.loadTexts:
    tmnxNatSubscIdVendorTable.setStatus("current")
_TmnxNatSubscIdVendorEntry_Object = MibTableRow
tmnxNatSubscIdVendorEntry = _TmnxNatSubscIdVendorEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 11, 1, 1)
)
tmnxNatSubscIdVendorEntry.setIndexNames(
    (0, "TIMETRA-NAT-MIB", "tmnxNatSubscIdVendorId"),
)
if mibBuilder.loadTexts:
    tmnxNatSubscIdVendorEntry.setStatus("current")
_TmnxNatSubscIdVendorId_Type = TmnxSubRadiusVendorId
_TmnxNatSubscIdVendorId_Object = MibTableColumn
tmnxNatSubscIdVendorId = _TmnxNatSubscIdVendorId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 11, 1, 1, 1),
    _TmnxNatSubscIdVendorId_Type()
)
tmnxNatSubscIdVendorId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxNatSubscIdVendorId.setStatus("current")


class _TmnxNatSubscIdVendorStr_Type(DisplayString):
    """Custom type tmnxNatSubscIdVendorStr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_TmnxNatSubscIdVendorStr_Type.__name__ = "DisplayString"
_TmnxNatSubscIdVendorStr_Object = MibTableColumn
tmnxNatSubscIdVendorStr = _TmnxNatSubscIdVendorStr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 11, 1, 1, 2),
    _TmnxNatSubscIdVendorStr_Type()
)
tmnxNatSubscIdVendorStr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatSubscIdVendorStr.setStatus("current")
_TmnxNatSubscIdVendorDescription_Type = TItemDescription
_TmnxNatSubscIdVendorDescription_Object = MibTableColumn
tmnxNatSubscIdVendorDescription = _TmnxNatSubscIdVendorDescription_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 11, 1, 1, 3),
    _TmnxNatSubscIdVendorDescription_Type()
)
tmnxNatSubscIdVendorDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatSubscIdVendorDescription.setStatus("current")
_TmnxNatSubscIdAttrTable_Object = MibTable
tmnxNatSubscIdAttrTable = _TmnxNatSubscIdAttrTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 11, 2)
)
if mibBuilder.loadTexts:
    tmnxNatSubscIdAttrTable.setStatus("current")
_TmnxNatSubscIdAttrEntry_Object = MibTableRow
tmnxNatSubscIdAttrEntry = _TmnxNatSubscIdAttrEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 11, 2, 1)
)
tmnxNatSubscIdAttrEntry.setIndexNames(
    (0, "TIMETRA-NAT-MIB", "tmnxNatSubscIdVendorId"),
    (0, "TIMETRA-NAT-MIB", "tmnxNatSubscIdAttrType"),
)
if mibBuilder.loadTexts:
    tmnxNatSubscIdAttrEntry.setStatus("current")
_TmnxNatSubscIdAttrType_Type = TmnxSubRadiusAttrType
_TmnxNatSubscIdAttrType_Object = MibTableColumn
tmnxNatSubscIdAttrType = _TmnxNatSubscIdAttrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 11, 2, 1, 1),
    _TmnxNatSubscIdAttrType_Type()
)
tmnxNatSubscIdAttrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxNatSubscIdAttrType.setStatus("current")


class _TmnxNatSubscIdAttrStr_Type(DisplayString):
    """Custom type tmnxNatSubscIdAttrStr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_TmnxNatSubscIdAttrStr_Type.__name__ = "DisplayString"
_TmnxNatSubscIdAttrStr_Object = MibTableColumn
tmnxNatSubscIdAttrStr = _TmnxNatSubscIdAttrStr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 11, 2, 1, 2),
    _TmnxNatSubscIdAttrStr_Type()
)
tmnxNatSubscIdAttrStr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatSubscIdAttrStr.setStatus("current")
_TmnxNatSubscIdAttrDescription_Type = TItemDescription
_TmnxNatSubscIdAttrDescription_Object = MibTableColumn
tmnxNatSubscIdAttrDescription = _TmnxNatSubscIdAttrDescription_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 11, 2, 1, 3),
    _TmnxNatSubscIdAttrDescription_Type()
)
tmnxNatSubscIdAttrDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatSubscIdAttrDescription.setStatus("current")
_TmnxNatDetScriptObjs_ObjectIdentity = ObjectIdentity
tmnxNatDetScriptObjs = _TmnxNatDetScriptObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 12)
)


class _TmnxNatDetScriptLocation_Type(TmnxDisplayStringURL):
    """Custom type tmnxNatDetScriptLocation based on TmnxDisplayStringURL"""
    defaultHexValue = ""


_TmnxNatDetScriptLocation_Type.__name__ = "TmnxDisplayStringURL"
_TmnxNatDetScriptLocation_Object = MibScalar
tmnxNatDetScriptLocation = _TmnxNatDetScriptLocation_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 12, 1),
    _TmnxNatDetScriptLocation_Type()
)
tmnxNatDetScriptLocation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxNatDetScriptLocation.setStatus("current")
_TmnxNatDetScriptSaveNeeded_Type = TruthValue
_TmnxNatDetScriptSaveNeeded_Object = MibScalar
tmnxNatDetScriptSaveNeeded = _TmnxNatDetScriptSaveNeeded_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 12, 2),
    _TmnxNatDetScriptSaveNeeded_Type()
)
tmnxNatDetScriptSaveNeeded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatDetScriptSaveNeeded.setStatus("current")


class _TmnxNatDetScriptSave_Type(TmnxActionType):
    """Custom type tmnxNatDetScriptSave based on TmnxActionType"""
    defaultValue = 2


_TmnxNatDetScriptSave_Type.__name__ = "TmnxActionType"
_TmnxNatDetScriptSave_Object = MibScalar
tmnxNatDetScriptSave = _TmnxNatDetScriptSave_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 12, 3),
    _TmnxNatDetScriptSave_Type()
)
tmnxNatDetScriptSave.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxNatDetScriptSave.setStatus("current")


class _TmnxNatDetScriptSaveResult_Type(Integer32):
    """Custom type tmnxNatDetScriptSaveResult based on Integer32"""
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
        *(("none", 1),
          ("inProgress", 2),
          ("success", 3),
          ("failed", 4))
    )


_TmnxNatDetScriptSaveResult_Type.__name__ = "Integer32"
_TmnxNatDetScriptSaveResult_Object = MibScalar
tmnxNatDetScriptSaveResult = _TmnxNatDetScriptSaveResult_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 12, 4),
    _TmnxNatDetScriptSaveResult_Type()
)
tmnxNatDetScriptSaveResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatDetScriptSaveResult.setStatus("current")


class _TmnxNatDetScriptSaveTime_Type(DateAndTime):
    """Custom type tmnxNatDetScriptSaveTime based on DateAndTime"""
    subtypeSpec = DateAndTime.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(11, 11),
    )
    fixed_length = 11


_TmnxNatDetScriptSaveTime_Type.__name__ = "DateAndTime"
_TmnxNatDetScriptSaveTime_Object = MibScalar
tmnxNatDetScriptSaveTime = _TmnxNatDetScriptSaveTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 12, 5),
    _TmnxNatDetScriptSaveTime_Type()
)
tmnxNatDetScriptSaveTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatDetScriptSaveTime.setStatus("current")
_TmnxNatQryObjs_ObjectIdentity = ObjectIdentity
tmnxNatQryObjs = _TmnxNatQryObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 13)
)
_TmnxNatQryLsnSubObjs_ObjectIdentity = ObjectIdentity
tmnxNatQryLsnSubObjs = _TmnxNatQryLsnSubObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 13, 1)
)
_TmnxNatQryLsnSubNextQryId_Type = Unsigned32
_TmnxNatQryLsnSubNextQryId_Object = MibScalar
tmnxNatQryLsnSubNextQryId = _TmnxNatQryLsnSubNextQryId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 13, 1, 1),
    _TmnxNatQryLsnSubNextQryId_Type()
)
tmnxNatQryLsnSubNextQryId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatQryLsnSubNextQryId.setStatus("current")
_TmnxNatQryLsnSubTable_Object = MibTable
tmnxNatQryLsnSubTable = _TmnxNatQryLsnSubTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 13, 1, 2)
)
if mibBuilder.loadTexts:
    tmnxNatQryLsnSubTable.setStatus("current")
_TmnxNatQryLsnSubEntry_Object = MibTableRow
tmnxNatQryLsnSubEntry = _TmnxNatQryLsnSubEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 13, 1, 2, 1)
)
tmnxNatQryLsnSubEntry.setIndexNames(
    (0, "TIMETRA-NAT-MIB", "tmnxNatQryLsnSubQryId"),
)
if mibBuilder.loadTexts:
    tmnxNatQryLsnSubEntry.setStatus("current")
_TmnxNatQryLsnSubQryId_Type = Unsigned32
_TmnxNatQryLsnSubQryId_Object = MibTableColumn
tmnxNatQryLsnSubQryId = _TmnxNatQryLsnSubQryId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 13, 1, 2, 1, 1),
    _TmnxNatQryLsnSubQryId_Type()
)
tmnxNatQryLsnSubQryId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxNatQryLsnSubQryId.setStatus("current")
_TmnxNatQryLsnSubRowStatus_Type = RowStatus
_TmnxNatQryLsnSubRowStatus_Object = MibTableColumn
tmnxNatQryLsnSubRowStatus = _TmnxNatQryLsnSubRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 13, 1, 2, 1, 2),
    _TmnxNatQryLsnSubRowStatus_Type()
)
tmnxNatQryLsnSubRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxNatQryLsnSubRowStatus.setStatus("current")


class _TmnxNatQryLsnSubResultType_Type(Integer32):
    """Custom type tmnxNatQryLsnSubResultType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("detail", 1),
          ("common", 2))
    )


_TmnxNatQryLsnSubResultType_Type.__name__ = "Integer32"
_TmnxNatQryLsnSubResultType_Object = MibTableColumn
tmnxNatQryLsnSubResultType = _TmnxNatQryLsnSubResultType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 13, 1, 2, 1, 3),
    _TmnxNatQryLsnSubResultType_Type()
)
tmnxNatQryLsnSubResultType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxNatQryLsnSubResultType.setStatus("current")


class _TmnxNatQryLsnSubWhereNatPolicy_Type(TNamedItemOrEmpty):
    """Custom type tmnxNatQryLsnSubWhereNatPolicy based on TNamedItemOrEmpty"""
    defaultValue = OctetString("")


_TmnxNatQryLsnSubWhereNatPolicy_Type.__name__ = "TNamedItemOrEmpty"
_TmnxNatQryLsnSubWhereNatPolicy_Object = MibTableColumn
tmnxNatQryLsnSubWhereNatPolicy = _TmnxNatQryLsnSubWhereNatPolicy_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 13, 1, 2, 1, 4),
    _TmnxNatQryLsnSubWhereNatPolicy_Type()
)
tmnxNatQryLsnSubWhereNatPolicy.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxNatQryLsnSubWhereNatPolicy.setStatus("current")


class _TmnxNatQryLsnSubWhereIsaGrp_Type(TmnxNatIsaGrpIdOrZero):
    """Custom type tmnxNatQryLsnSubWhereIsaGrp based on TmnxNatIsaGrpIdOrZero"""
    defaultValue = 0


_TmnxNatQryLsnSubWhereIsaGrp_Type.__name__ = "TmnxNatIsaGrpIdOrZero"
_TmnxNatQryLsnSubWhereIsaGrp_Object = MibTableColumn
tmnxNatQryLsnSubWhereIsaGrp = _TmnxNatQryLsnSubWhereIsaGrp_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 13, 1, 2, 1, 5),
    _TmnxNatQryLsnSubWhereIsaGrp_Type()
)
tmnxNatQryLsnSubWhereIsaGrp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxNatQryLsnSubWhereIsaGrp.setStatus("current")


class _TmnxNatQryLsnSubWhereMemberId_Type(Unsigned32):
    """Custom type tmnxNatQryLsnSubWhereMemberId based on Unsigned32"""
    defaultValue = 0


_TmnxNatQryLsnSubWhereMemberId_Type.__name__ = "Unsigned32"
_TmnxNatQryLsnSubWhereMemberId_Object = MibTableColumn
tmnxNatQryLsnSubWhereMemberId = _TmnxNatQryLsnSubWhereMemberId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 13, 1, 2, 1, 6),
    _TmnxNatQryLsnSubWhereMemberId_Type()
)
tmnxNatQryLsnSubWhereMemberId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxNatQryLsnSubWhereMemberId.setStatus("current")


class _TmnxNatQryLsnSubWhereOutRouter_Type(TmnxVRtrIDOrZero):
    """Custom type tmnxNatQryLsnSubWhereOutRouter based on TmnxVRtrIDOrZero"""
    defaultValue = 0


_TmnxNatQryLsnSubWhereOutRouter_Type.__name__ = "TmnxVRtrIDOrZero"
_TmnxNatQryLsnSubWhereOutRouter_Object = MibTableColumn
tmnxNatQryLsnSubWhereOutRouter = _TmnxNatQryLsnSubWhereOutRouter_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 13, 1, 2, 1, 7),
    _TmnxNatQryLsnSubWhereOutRouter_Type()
)
tmnxNatQryLsnSubWhereOutRouter.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxNatQryLsnSubWhereOutRouter.setStatus("current")


class _TmnxNatQryLsnSubWhereOutAddrType_Type(InetAddressType):
    """Custom type tmnxNatQryLsnSubWhereOutAddrType based on InetAddressType"""
    defaultValue = 0


_TmnxNatQryLsnSubWhereOutAddrType_Type.__name__ = "InetAddressType"
_TmnxNatQryLsnSubWhereOutAddrType_Object = MibTableColumn
tmnxNatQryLsnSubWhereOutAddrType = _TmnxNatQryLsnSubWhereOutAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 13, 1, 2, 1, 8),
    _TmnxNatQryLsnSubWhereOutAddrType_Type()
)
tmnxNatQryLsnSubWhereOutAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxNatQryLsnSubWhereOutAddrType.setStatus("current")


class _TmnxNatQryLsnSubWhereOutAddr_Type(InetAddress):
    """Custom type tmnxNatQryLsnSubWhereOutAddr based on InetAddress"""
    defaultHexValue = ""

    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxNatQryLsnSubWhereOutAddr_Type.__name__ = "InetAddress"
_TmnxNatQryLsnSubWhereOutAddr_Object = MibTableColumn
tmnxNatQryLsnSubWhereOutAddr = _TmnxNatQryLsnSubWhereOutAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 13, 1, 2, 1, 9),
    _TmnxNatQryLsnSubWhereOutAddr_Type()
)
tmnxNatQryLsnSubWhereOutAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxNatQryLsnSubWhereOutAddr.setStatus("current")


class _TmnxNatQryLsnSubWhereInSubType_Type(Integer32):
    """Custom type tmnxNatQryLsnSubWhereInSubType based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("classicLsnSub", 2),
          ("dsliteLsnSub", 3),
          ("nat64LsnSub", 4),
          ("reserved5", 5))
    )


_TmnxNatQryLsnSubWhereInSubType_Type.__name__ = "Integer32"
_TmnxNatQryLsnSubWhereInSubType_Object = MibTableColumn
tmnxNatQryLsnSubWhereInSubType = _TmnxNatQryLsnSubWhereInSubType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 13, 1, 2, 1, 10),
    _TmnxNatQryLsnSubWhereInSubType_Type()
)
tmnxNatQryLsnSubWhereInSubType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxNatQryLsnSubWhereInSubType.setStatus("current")


class _TmnxNatQryLsnSubWhereInRouter_Type(TmnxVRtrIDOrZero):
    """Custom type tmnxNatQryLsnSubWhereInRouter based on TmnxVRtrIDOrZero"""
    defaultValue = 0


_TmnxNatQryLsnSubWhereInRouter_Type.__name__ = "TmnxVRtrIDOrZero"
_TmnxNatQryLsnSubWhereInRouter_Object = MibTableColumn
tmnxNatQryLsnSubWhereInRouter = _TmnxNatQryLsnSubWhereInRouter_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 13, 1, 2, 1, 11),
    _TmnxNatQryLsnSubWhereInRouter_Type()
)
tmnxNatQryLsnSubWhereInRouter.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxNatQryLsnSubWhereInRouter.setStatus("current")


class _TmnxNatQryLsnSubWhereInAddrType_Type(InetAddressType):
    """Custom type tmnxNatQryLsnSubWhereInAddrType based on InetAddressType"""
    defaultValue = 0


_TmnxNatQryLsnSubWhereInAddrType_Type.__name__ = "InetAddressType"
_TmnxNatQryLsnSubWhereInAddrType_Object = MibTableColumn
tmnxNatQryLsnSubWhereInAddrType = _TmnxNatQryLsnSubWhereInAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 13, 1, 2, 1, 12),
    _TmnxNatQryLsnSubWhereInAddrType_Type()
)
tmnxNatQryLsnSubWhereInAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxNatQryLsnSubWhereInAddrType.setStatus("current")


class _TmnxNatQryLsnSubWhereInAddr_Type(InetAddress):
    """Custom type tmnxNatQryLsnSubWhereInAddr based on InetAddress"""
    defaultHexValue = ""

    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxNatQryLsnSubWhereInAddr_Type.__name__ = "InetAddress"
_TmnxNatQryLsnSubWhereInAddr_Object = MibTableColumn
tmnxNatQryLsnSubWhereInAddr = _TmnxNatQryLsnSubWhereInAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 13, 1, 2, 1, 13),
    _TmnxNatQryLsnSubWhereInAddr_Type()
)
tmnxNatQryLsnSubWhereInAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxNatQryLsnSubWhereInAddr.setStatus("current")


class _TmnxNatQryLsnSubWhereInAddrPfxL_Type(InetAddressPrefixLength):
    """Custom type tmnxNatQryLsnSubWhereInAddrPfxL based on InetAddressPrefixLength"""
    defaultValue = 0

    subtypeSpec = InetAddressPrefixLength.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_TmnxNatQryLsnSubWhereInAddrPfxL_Type.__name__ = "InetAddressPrefixLength"
_TmnxNatQryLsnSubWhereInAddrPfxL_Object = MibTableColumn
tmnxNatQryLsnSubWhereInAddrPfxL = _TmnxNatQryLsnSubWhereInAddrPfxL_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 13, 1, 2, 1, 14),
    _TmnxNatQryLsnSubWhereInAddrPfxL_Type()
)
tmnxNatQryLsnSubWhereInAddrPfxL.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxNatQryLsnSubWhereInAddrPfxL.setStatus("current")


class _TmnxNatQryLsnSubWhereSubId_Type(Unsigned32):
    """Custom type tmnxNatQryLsnSubWhereSubId based on Unsigned32"""
    defaultValue = 0


_TmnxNatQryLsnSubWhereSubId_Type.__name__ = "Unsigned32"
_TmnxNatQryLsnSubWhereSubId_Object = MibTableColumn
tmnxNatQryLsnSubWhereSubId = _TmnxNatQryLsnSubWhereSubId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 13, 1, 2, 1, 15),
    _TmnxNatQryLsnSubWhereSubId_Type()
)
tmnxNatQryLsnSubWhereSubId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxNatQryLsnSubWhereSubId.setStatus("current")
_TmnxNatQryLsnSubResTable_Object = MibTable
tmnxNatQryLsnSubResTable = _TmnxNatQryLsnSubResTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 13, 1, 3)
)
if mibBuilder.loadTexts:
    tmnxNatQryLsnSubResTable.setStatus("current")
_TmnxNatQryLsnSubResEntry_Object = MibTableRow
tmnxNatQryLsnSubResEntry = _TmnxNatQryLsnSubResEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 13, 1, 3, 1)
)
tmnxNatQryLsnSubResEntry.setIndexNames(
    (0, "TIMETRA-NAT-MIB", "tmnxNatQryLsnSubQryId"),
    (0, "TIMETRA-NAT-MIB", "tmnxNatQryLsnSubResId"),
    (0, "TIMETRA-NAT-MIB", "tmnxNatQryLsnSubResPolicy"),
)
if mibBuilder.loadTexts:
    tmnxNatQryLsnSubResEntry.setStatus("current")
_TmnxNatQryLsnSubResId_Type = Unsigned32
_TmnxNatQryLsnSubResId_Object = MibTableColumn
tmnxNatQryLsnSubResId = _TmnxNatQryLsnSubResId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 13, 1, 3, 1, 1),
    _TmnxNatQryLsnSubResId_Type()
)
tmnxNatQryLsnSubResId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxNatQryLsnSubResId.setStatus("current")
_TmnxNatQryLsnSubResPolicy_Type = TNamedItem
_TmnxNatQryLsnSubResPolicy_Object = MibTableColumn
tmnxNatQryLsnSubResPolicy = _TmnxNatQryLsnSubResPolicy_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 13, 1, 3, 1, 2),
    _TmnxNatQryLsnSubResPolicy_Type()
)
tmnxNatQryLsnSubResPolicy.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxNatQryLsnSubResPolicy.setStatus("current")
_TmnxNatQryLsnSubResIsaGrp_Type = TmnxNatIsaGrpIdOrZero
_TmnxNatQryLsnSubResIsaGrp_Object = MibTableColumn
tmnxNatQryLsnSubResIsaGrp = _TmnxNatQryLsnSubResIsaGrp_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 13, 1, 3, 1, 3),
    _TmnxNatQryLsnSubResIsaGrp_Type()
)
tmnxNatQryLsnSubResIsaGrp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatQryLsnSubResIsaGrp.setStatus("current")
_TmnxNatQryLsnSubResIsaMemberId_Type = Unsigned32
_TmnxNatQryLsnSubResIsaMemberId_Object = MibTableColumn
tmnxNatQryLsnSubResIsaMemberId = _TmnxNatQryLsnSubResIsaMemberId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 13, 1, 3, 1, 4),
    _TmnxNatQryLsnSubResIsaMemberId_Type()
)
tmnxNatQryLsnSubResIsaMemberId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatQryLsnSubResIsaMemberId.setStatus("current")
_TmnxNatQryLsnSubResOutVRtrID_Type = TmnxVRtrIDOrZero
_TmnxNatQryLsnSubResOutVRtrID_Object = MibTableColumn
tmnxNatQryLsnSubResOutVRtrID = _TmnxNatQryLsnSubResOutVRtrID_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 13, 1, 3, 1, 5),
    _TmnxNatQryLsnSubResOutVRtrID_Type()
)
tmnxNatQryLsnSubResOutVRtrID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatQryLsnSubResOutVRtrID.setStatus("current")
_TmnxNatQryLsnSubResOutAddrType_Type = InetAddressType
_TmnxNatQryLsnSubResOutAddrType_Object = MibTableColumn
tmnxNatQryLsnSubResOutAddrType = _TmnxNatQryLsnSubResOutAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 13, 1, 3, 1, 6),
    _TmnxNatQryLsnSubResOutAddrType_Type()
)
tmnxNatQryLsnSubResOutAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatQryLsnSubResOutAddrType.setStatus("current")


class _TmnxNatQryLsnSubResOutAddr_Type(InetAddress):
    """Custom type tmnxNatQryLsnSubResOutAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxNatQryLsnSubResOutAddr_Type.__name__ = "InetAddress"
_TmnxNatQryLsnSubResOutAddr_Object = MibTableColumn
tmnxNatQryLsnSubResOutAddr = _TmnxNatQryLsnSubResOutAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 13, 1, 3, 1, 7),
    _TmnxNatQryLsnSubResOutAddr_Type()
)
tmnxNatQryLsnSubResOutAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatQryLsnSubResOutAddr.setStatus("current")
_TmnxNatQryLsnSubResIdStr_Type = TmnxNatSubscriberIdString
_TmnxNatQryLsnSubResIdStr_Object = MibTableColumn
tmnxNatQryLsnSubResIdStr = _TmnxNatQryLsnSubResIdStr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 13, 1, 3, 1, 8),
    _TmnxNatQryLsnSubResIdStr_Type()
)
tmnxNatQryLsnSubResIdStr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatQryLsnSubResIdStr.setStatus("current")


class _TmnxNatQryLsnSubResInSubType_Type(Integer32):
    """Custom type tmnxNatQryLsnSubResInSubType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("classicLsnSub", 2),
          ("dsliteLsnSub", 3),
          ("nat64LsnSub", 4),
          ("reserved5", 5))
    )


_TmnxNatQryLsnSubResInSubType_Type.__name__ = "Integer32"
_TmnxNatQryLsnSubResInSubType_Object = MibTableColumn
tmnxNatQryLsnSubResInSubType = _TmnxNatQryLsnSubResInSubType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 13, 1, 3, 1, 9),
    _TmnxNatQryLsnSubResInSubType_Type()
)
tmnxNatQryLsnSubResInSubType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatQryLsnSubResInSubType.setStatus("current")
_TmnxNatQryLsnSubResInRouter_Type = TmnxVRtrIDOrZero
_TmnxNatQryLsnSubResInRouter_Object = MibTableColumn
tmnxNatQryLsnSubResInRouter = _TmnxNatQryLsnSubResInRouter_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 13, 1, 3, 1, 10),
    _TmnxNatQryLsnSubResInRouter_Type()
)
tmnxNatQryLsnSubResInRouter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatQryLsnSubResInRouter.setStatus("current")
_TmnxNatQryLsnSubResInAddrType_Type = InetAddressType
_TmnxNatQryLsnSubResInAddrType_Object = MibTableColumn
tmnxNatQryLsnSubResInAddrType = _TmnxNatQryLsnSubResInAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 13, 1, 3, 1, 11),
    _TmnxNatQryLsnSubResInAddrType_Type()
)
tmnxNatQryLsnSubResInAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatQryLsnSubResInAddrType.setStatus("current")


class _TmnxNatQryLsnSubResInAddr_Type(InetAddress):
    """Custom type tmnxNatQryLsnSubResInAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxNatQryLsnSubResInAddr_Type.__name__ = "InetAddress"
_TmnxNatQryLsnSubResInAddr_Object = MibTableColumn
tmnxNatQryLsnSubResInAddr = _TmnxNatQryLsnSubResInAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 13, 1, 3, 1, 12),
    _TmnxNatQryLsnSubResInAddr_Type()
)
tmnxNatQryLsnSubResInAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatQryLsnSubResInAddr.setStatus("current")
_TmnxNatQryLsnSubResInAddrPfxL_Type = InetAddressPrefixLength
_TmnxNatQryLsnSubResInAddrPfxL_Object = MibTableColumn
tmnxNatQryLsnSubResInAddrPfxL = _TmnxNatQryLsnSubResInAddrPfxL_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 13, 1, 3, 1, 13),
    _TmnxNatQryLsnSubResInAddrPfxL_Type()
)
tmnxNatQryLsnSubResInAddrPfxL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatQryLsnSubResInAddrPfxL.setStatus("current")
_TmnxNatQryLsnSubResIcmpPortUsg_Type = TmnxNatUsageLevel
_TmnxNatQryLsnSubResIcmpPortUsg_Object = MibTableColumn
tmnxNatQryLsnSubResIcmpPortUsg = _TmnxNatQryLsnSubResIcmpPortUsg_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 13, 1, 3, 1, 100),
    _TmnxNatQryLsnSubResIcmpPortUsg_Type()
)
tmnxNatQryLsnSubResIcmpPortUsg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatQryLsnSubResIcmpPortUsg.setStatus("current")
_TmnxNatQryLsnSubResIcmpPortUsgHi_Type = TruthValue
_TmnxNatQryLsnSubResIcmpPortUsgHi_Object = MibTableColumn
tmnxNatQryLsnSubResIcmpPortUsgHi = _TmnxNatQryLsnSubResIcmpPortUsgHi_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 13, 1, 3, 1, 101),
    _TmnxNatQryLsnSubResIcmpPortUsgHi_Type()
)
tmnxNatQryLsnSubResIcmpPortUsgHi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatQryLsnSubResIcmpPortUsgHi.setStatus("current")
_TmnxNatQryLsnSubResUdpPortUsg_Type = TmnxNatUsageLevel
_TmnxNatQryLsnSubResUdpPortUsg_Object = MibTableColumn
tmnxNatQryLsnSubResUdpPortUsg = _TmnxNatQryLsnSubResUdpPortUsg_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 13, 1, 3, 1, 102),
    _TmnxNatQryLsnSubResUdpPortUsg_Type()
)
tmnxNatQryLsnSubResUdpPortUsg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatQryLsnSubResUdpPortUsg.setStatus("current")
_TmnxNatQryLsnSubResUdpPortUsgHi_Type = TruthValue
_TmnxNatQryLsnSubResUdpPortUsgHi_Object = MibTableColumn
tmnxNatQryLsnSubResUdpPortUsgHi = _TmnxNatQryLsnSubResUdpPortUsgHi_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 13, 1, 3, 1, 103),
    _TmnxNatQryLsnSubResUdpPortUsgHi_Type()
)
tmnxNatQryLsnSubResUdpPortUsgHi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatQryLsnSubResUdpPortUsgHi.setStatus("current")
_TmnxNatQryLsnSubResTcpPortUsg_Type = TmnxNatUsageLevel
_TmnxNatQryLsnSubResTcpPortUsg_Object = MibTableColumn
tmnxNatQryLsnSubResTcpPortUsg = _TmnxNatQryLsnSubResTcpPortUsg_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 13, 1, 3, 1, 104),
    _TmnxNatQryLsnSubResTcpPortUsg_Type()
)
tmnxNatQryLsnSubResTcpPortUsg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatQryLsnSubResTcpPortUsg.setStatus("current")
_TmnxNatQryLsnSubResTcpPortUsgHi_Type = TruthValue
_TmnxNatQryLsnSubResTcpPortUsgHi_Object = MibTableColumn
tmnxNatQryLsnSubResTcpPortUsgHi = _TmnxNatQryLsnSubResTcpPortUsgHi_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 13, 1, 3, 1, 105),
    _TmnxNatQryLsnSubResTcpPortUsgHi_Type()
)
tmnxNatQryLsnSubResTcpPortUsgHi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatQryLsnSubResTcpPortUsgHi.setStatus("current")
_TmnxNatQryLsnSubResSessionUsg_Type = TmnxNatUsageLevel
_TmnxNatQryLsnSubResSessionUsg_Object = MibTableColumn
tmnxNatQryLsnSubResSessionUsg = _TmnxNatQryLsnSubResSessionUsg_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 13, 1, 3, 1, 106),
    _TmnxNatQryLsnSubResSessionUsg_Type()
)
tmnxNatQryLsnSubResSessionUsg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatQryLsnSubResSessionUsg.setStatus("current")
_TmnxNatQryLsnSubResSessionUsgHi_Type = TruthValue
_TmnxNatQryLsnSubResSessionUsgHi_Object = MibTableColumn
tmnxNatQryLsnSubResSessionUsgHi = _TmnxNatQryLsnSubResSessionUsgHi_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 13, 1, 3, 1, 107),
    _TmnxNatQryLsnSubResSessionUsgHi_Type()
)
tmnxNatQryLsnSubResSessionUsgHi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatQryLsnSubResSessionUsgHi.setStatus("current")
_TmnxNatQryLsnSubResSessions_Type = Gauge32
_TmnxNatQryLsnSubResSessions_Object = MibTableColumn
tmnxNatQryLsnSubResSessions = _TmnxNatQryLsnSubResSessions_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 13, 1, 3, 1, 108),
    _TmnxNatQryLsnSubResSessions_Type()
)
tmnxNatQryLsnSubResSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatQryLsnSubResSessions.setStatus("current")
_TmnxNatQryLsnSubResSessionsPrio_Type = Gauge32
_TmnxNatQryLsnSubResSessionsPrio_Object = MibTableColumn
tmnxNatQryLsnSubResSessionsPrio = _TmnxNatQryLsnSubResSessionsPrio_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 13, 1, 3, 1, 109),
    _TmnxNatQryLsnSubResSessionsPrio_Type()
)
tmnxNatQryLsnSubResSessionsPrio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatQryLsnSubResSessionsPrio.setStatus("current")
_TmnxNatQryLsnSubResSessionsPeak_Type = Gauge32
_TmnxNatQryLsnSubResSessionsPeak_Object = MibTableColumn
tmnxNatQryLsnSubResSessionsPeak = _TmnxNatQryLsnSubResSessionsPeak_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 13, 1, 3, 1, 110),
    _TmnxNatQryLsnSubResSessionsPeak_Type()
)
tmnxNatQryLsnSubResSessionsPeak.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatQryLsnSubResSessionsPeak.setStatus("current")
_TmnxNatLsnSubPlcyOutIpAddrTable_Object = MibTable
tmnxNatLsnSubPlcyOutIpAddrTable = _TmnxNatLsnSubPlcyOutIpAddrTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 13, 1, 4)
)
if mibBuilder.loadTexts:
    tmnxNatLsnSubPlcyOutIpAddrTable.setStatus("current")
_TmnxNatLsnSubPlcyOutIpAddrEntry_Object = MibTableRow
tmnxNatLsnSubPlcyOutIpAddrEntry = _TmnxNatLsnSubPlcyOutIpAddrEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 13, 1, 4, 1)
)
tmnxNatLsnSubPlcyOutIpAddrEntry.setIndexNames(
    (0, "TIMETRA-NAT-MIB", "tmnxNatLsnSubPlcyOutIpAddrSubId"),
    (0, "TIMETRA-NAT-MIB", "tmnxNatLsnSubPlcyOutIpAddrPolicy"),
    (0, "TIMETRA-NAT-MIB", "tmnxNatLsnSubPlcyOutIpAddrType"),
    (0, "TIMETRA-NAT-MIB", "tmnxNatLsnSubPlcyOutIpAddr"),
)
if mibBuilder.loadTexts:
    tmnxNatLsnSubPlcyOutIpAddrEntry.setStatus("current")
_TmnxNatLsnSubPlcyOutIpAddrSubId_Type = Unsigned32
_TmnxNatLsnSubPlcyOutIpAddrSubId_Object = MibTableColumn
tmnxNatLsnSubPlcyOutIpAddrSubId = _TmnxNatLsnSubPlcyOutIpAddrSubId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 13, 1, 4, 1, 1),
    _TmnxNatLsnSubPlcyOutIpAddrSubId_Type()
)
tmnxNatLsnSubPlcyOutIpAddrSubId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxNatLsnSubPlcyOutIpAddrSubId.setStatus("current")
_TmnxNatLsnSubPlcyOutIpAddrPolicy_Type = TNamedItem
_TmnxNatLsnSubPlcyOutIpAddrPolicy_Object = MibTableColumn
tmnxNatLsnSubPlcyOutIpAddrPolicy = _TmnxNatLsnSubPlcyOutIpAddrPolicy_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 13, 1, 4, 1, 2),
    _TmnxNatLsnSubPlcyOutIpAddrPolicy_Type()
)
tmnxNatLsnSubPlcyOutIpAddrPolicy.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxNatLsnSubPlcyOutIpAddrPolicy.setStatus("current")
_TmnxNatLsnSubPlcyOutIpAddrType_Type = InetAddressType
_TmnxNatLsnSubPlcyOutIpAddrType_Object = MibTableColumn
tmnxNatLsnSubPlcyOutIpAddrType = _TmnxNatLsnSubPlcyOutIpAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 13, 1, 4, 1, 3),
    _TmnxNatLsnSubPlcyOutIpAddrType_Type()
)
tmnxNatLsnSubPlcyOutIpAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxNatLsnSubPlcyOutIpAddrType.setStatus("current")


class _TmnxNatLsnSubPlcyOutIpAddr_Type(InetAddress):
    """Custom type tmnxNatLsnSubPlcyOutIpAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxNatLsnSubPlcyOutIpAddr_Type.__name__ = "InetAddress"
_TmnxNatLsnSubPlcyOutIpAddr_Object = MibTableColumn
tmnxNatLsnSubPlcyOutIpAddr = _TmnxNatLsnSubPlcyOutIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 13, 1, 4, 1, 4),
    _TmnxNatLsnSubPlcyOutIpAddr_Type()
)
tmnxNatLsnSubPlcyOutIpAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxNatLsnSubPlcyOutIpAddr.setStatus("current")
_TmnxNatLsnSubPlcyOutIpAddrOutVR_Type = TmnxVRtrID
_TmnxNatLsnSubPlcyOutIpAddrOutVR_Object = MibTableColumn
tmnxNatLsnSubPlcyOutIpAddrOutVR = _TmnxNatLsnSubPlcyOutIpAddrOutVR_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 13, 1, 4, 1, 5),
    _TmnxNatLsnSubPlcyOutIpAddrOutVR_Type()
)
tmnxNatLsnSubPlcyOutIpAddrOutVR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatLsnSubPlcyOutIpAddrOutVR.setStatus("current")
_TmnxNatLsnSubPlcyOutIpBlkTable_Object = MibTable
tmnxNatLsnSubPlcyOutIpBlkTable = _TmnxNatLsnSubPlcyOutIpBlkTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 13, 1, 5)
)
if mibBuilder.loadTexts:
    tmnxNatLsnSubPlcyOutIpBlkTable.setStatus("current")
_TmnxNatLsnSubPlcyOutIpBlkEntry_Object = MibTableRow
tmnxNatLsnSubPlcyOutIpBlkEntry = _TmnxNatLsnSubPlcyOutIpBlkEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 13, 1, 5, 1)
)
tmnxNatLsnSubPlcyOutIpBlkEntry.setIndexNames(
    (0, "TIMETRA-NAT-MIB", "tmnxNatLsnSubPlcyOutIpBlkSubId"),
    (0, "TIMETRA-NAT-MIB", "tmnxNatLsnSubPlcyOutIpBlkPolicy"),
    (0, "TIMETRA-NAT-MIB", "tmnxNatLsnSubPlcyOutIpBlkIpType"),
    (0, "TIMETRA-NAT-MIB", "tmnxNatLsnSubPlcyOutIpBlkIp"),
    (0, "TIMETRA-NAT-MIB", "tmnxNatLsnSubPlcyOutIpBlkStart"),
)
if mibBuilder.loadTexts:
    tmnxNatLsnSubPlcyOutIpBlkEntry.setStatus("current")
_TmnxNatLsnSubPlcyOutIpBlkSubId_Type = Unsigned32
_TmnxNatLsnSubPlcyOutIpBlkSubId_Object = MibTableColumn
tmnxNatLsnSubPlcyOutIpBlkSubId = _TmnxNatLsnSubPlcyOutIpBlkSubId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 13, 1, 5, 1, 1),
    _TmnxNatLsnSubPlcyOutIpBlkSubId_Type()
)
tmnxNatLsnSubPlcyOutIpBlkSubId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxNatLsnSubPlcyOutIpBlkSubId.setStatus("current")
_TmnxNatLsnSubPlcyOutIpBlkPolicy_Type = TNamedItem
_TmnxNatLsnSubPlcyOutIpBlkPolicy_Object = MibTableColumn
tmnxNatLsnSubPlcyOutIpBlkPolicy = _TmnxNatLsnSubPlcyOutIpBlkPolicy_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 13, 1, 5, 1, 2),
    _TmnxNatLsnSubPlcyOutIpBlkPolicy_Type()
)
tmnxNatLsnSubPlcyOutIpBlkPolicy.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxNatLsnSubPlcyOutIpBlkPolicy.setStatus("current")
_TmnxNatLsnSubPlcyOutIpBlkIpType_Type = InetAddressType
_TmnxNatLsnSubPlcyOutIpBlkIpType_Object = MibTableColumn
tmnxNatLsnSubPlcyOutIpBlkIpType = _TmnxNatLsnSubPlcyOutIpBlkIpType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 13, 1, 5, 1, 3),
    _TmnxNatLsnSubPlcyOutIpBlkIpType_Type()
)
tmnxNatLsnSubPlcyOutIpBlkIpType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxNatLsnSubPlcyOutIpBlkIpType.setStatus("current")


class _TmnxNatLsnSubPlcyOutIpBlkIp_Type(InetAddress):
    """Custom type tmnxNatLsnSubPlcyOutIpBlkIp based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxNatLsnSubPlcyOutIpBlkIp_Type.__name__ = "InetAddress"
_TmnxNatLsnSubPlcyOutIpBlkIp_Object = MibTableColumn
tmnxNatLsnSubPlcyOutIpBlkIp = _TmnxNatLsnSubPlcyOutIpBlkIp_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 13, 1, 5, 1, 4),
    _TmnxNatLsnSubPlcyOutIpBlkIp_Type()
)
tmnxNatLsnSubPlcyOutIpBlkIp.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxNatLsnSubPlcyOutIpBlkIp.setStatus("current")
_TmnxNatLsnSubPlcyOutIpBlkStart_Type = Unsigned32
_TmnxNatLsnSubPlcyOutIpBlkStart_Object = MibTableColumn
tmnxNatLsnSubPlcyOutIpBlkStart = _TmnxNatLsnSubPlcyOutIpBlkStart_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 13, 1, 5, 1, 5),
    _TmnxNatLsnSubPlcyOutIpBlkStart_Type()
)
tmnxNatLsnSubPlcyOutIpBlkStart.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxNatLsnSubPlcyOutIpBlkStart.setStatus("current")
_TmnxNatLsnSubPlcyOutIpBlkEnd_Type = Unsigned32
_TmnxNatLsnSubPlcyOutIpBlkEnd_Object = MibTableColumn
tmnxNatLsnSubPlcyOutIpBlkEnd = _TmnxNatLsnSubPlcyOutIpBlkEnd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 13, 1, 5, 1, 6),
    _TmnxNatLsnSubPlcyOutIpBlkEnd_Type()
)
tmnxNatLsnSubPlcyOutIpBlkEnd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatLsnSubPlcyOutIpBlkEnd.setStatus("current")
_TmnxNatUpnpObjs_ObjectIdentity = ObjectIdentity
tmnxNatUpnpObjs = _TmnxNatUpnpObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 14)
)
_TmnxNatUpnpPlcyTable_Object = MibTable
tmnxNatUpnpPlcyTable = _TmnxNatUpnpPlcyTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 14, 1)
)
if mibBuilder.loadTexts:
    tmnxNatUpnpPlcyTable.setStatus("current")
_TmnxNatUpnpPlcyEntry_Object = MibTableRow
tmnxNatUpnpPlcyEntry = _TmnxNatUpnpPlcyEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 14, 1, 1)
)
tmnxNatUpnpPlcyEntry.setIndexNames(
    (1, "TIMETRA-NAT-MIB", "tmnxNatUpnpPlcyName"),
)
if mibBuilder.loadTexts:
    tmnxNatUpnpPlcyEntry.setStatus("current")
_TmnxNatUpnpPlcyName_Type = TNamedItem
_TmnxNatUpnpPlcyName_Object = MibTableColumn
tmnxNatUpnpPlcyName = _TmnxNatUpnpPlcyName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 14, 1, 1, 1),
    _TmnxNatUpnpPlcyName_Type()
)
tmnxNatUpnpPlcyName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxNatUpnpPlcyName.setStatus("current")
_TmnxNatUpnpPlcyRowStatus_Type = RowStatus
_TmnxNatUpnpPlcyRowStatus_Object = MibTableColumn
tmnxNatUpnpPlcyRowStatus = _TmnxNatUpnpPlcyRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 14, 1, 1, 2),
    _TmnxNatUpnpPlcyRowStatus_Type()
)
tmnxNatUpnpPlcyRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxNatUpnpPlcyRowStatus.setStatus("current")
_TmnxNatUpnpPlcyLastMgmtChange_Type = TimeStamp
_TmnxNatUpnpPlcyLastMgmtChange_Object = MibTableColumn
tmnxNatUpnpPlcyLastMgmtChange = _TmnxNatUpnpPlcyLastMgmtChange_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 14, 1, 1, 3),
    _TmnxNatUpnpPlcyLastMgmtChange_Type()
)
tmnxNatUpnpPlcyLastMgmtChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatUpnpPlcyLastMgmtChange.setStatus("current")


class _TmnxNatUpnpPlcyDescription_Type(TItemDescription):
    """Custom type tmnxNatUpnpPlcyDescription based on TItemDescription"""
    defaultValue = OctetString("")


_TmnxNatUpnpPlcyDescription_Type.__name__ = "TItemDescription"
_TmnxNatUpnpPlcyDescription_Object = MibTableColumn
tmnxNatUpnpPlcyDescription = _TmnxNatUpnpPlcyDescription_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 14, 1, 1, 4),
    _TmnxNatUpnpPlcyDescription_Type()
)
tmnxNatUpnpPlcyDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxNatUpnpPlcyDescription.setStatus("current")


class _TmnxNatUpnpPlcyMappingLimit_Type(Unsigned32):
    """Custom type tmnxNatUpnpPlcyMappingLimit based on Unsigned32"""
    defaultValue = 256

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 256),
    )


_TmnxNatUpnpPlcyMappingLimit_Type.__name__ = "Unsigned32"
_TmnxNatUpnpPlcyMappingLimit_Object = MibTableColumn
tmnxNatUpnpPlcyMappingLimit = _TmnxNatUpnpPlcyMappingLimit_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 14, 1, 1, 5),
    _TmnxNatUpnpPlcyMappingLimit_Type()
)
tmnxNatUpnpPlcyMappingLimit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxNatUpnpPlcyMappingLimit.setStatus("current")


class _TmnxNatUpnpPlcyStrictMode_Type(TruthValue):
    """Custom type tmnxNatUpnpPlcyStrictMode based on TruthValue"""
    defaultValue = 2


_TmnxNatUpnpPlcyStrictMode_Type.__name__ = "TruthValue"
_TmnxNatUpnpPlcyStrictMode_Object = MibTableColumn
tmnxNatUpnpPlcyStrictMode = _TmnxNatUpnpPlcyStrictMode_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 14, 1, 1, 6),
    _TmnxNatUpnpPlcyStrictMode_Type()
)
tmnxNatUpnpPlcyStrictMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxNatUpnpPlcyStrictMode.setStatus("current")


class _TmnxNatUpnpPlcyListeningPort_Type(InetPortNumber):
    """Custom type tmnxNatUpnpPlcyListeningPort based on InetPortNumber"""
    defaultValue = 5000

    subtypeSpec = InetPortNumber.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_TmnxNatUpnpPlcyListeningPort_Type.__name__ = "InetPortNumber"
_TmnxNatUpnpPlcyListeningPort_Object = MibTableColumn
tmnxNatUpnpPlcyListeningPort = _TmnxNatUpnpPlcyListeningPort_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 14, 1, 1, 7),
    _TmnxNatUpnpPlcyListeningPort_Type()
)
tmnxNatUpnpPlcyListeningPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxNatUpnpPlcyListeningPort.setStatus("current")
_TmnxNatUpnpPlcyStatsTable_Object = MibTable
tmnxNatUpnpPlcyStatsTable = _TmnxNatUpnpPlcyStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 14, 2)
)
if mibBuilder.loadTexts:
    tmnxNatUpnpPlcyStatsTable.setStatus("current")
_TmnxNatUpnpPlcyStatsEntry_Object = MibTableRow
tmnxNatUpnpPlcyStatsEntry = _TmnxNatUpnpPlcyStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 14, 2, 1)
)
tmnxNatUpnpPlcyStatsEntry.setIndexNames(
    (0, "TIMETRA-NAT-MIB", "tmnxNatUpnpPlcyName"),
    (0, "TIMETRA-NAT-MIB", "tmnxNatUpnpPlcyStatsId"),
)
if mibBuilder.loadTexts:
    tmnxNatUpnpPlcyStatsEntry.setStatus("current")


class _TmnxNatUpnpPlcyStatsId_Type(Unsigned32):
    """Custom type tmnxNatUpnpPlcyStatsId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 50),
    )


_TmnxNatUpnpPlcyStatsId_Type.__name__ = "Unsigned32"
_TmnxNatUpnpPlcyStatsId_Object = MibTableColumn
tmnxNatUpnpPlcyStatsId = _TmnxNatUpnpPlcyStatsId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 14, 2, 1, 1),
    _TmnxNatUpnpPlcyStatsId_Type()
)
tmnxNatUpnpPlcyStatsId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxNatUpnpPlcyStatsId.setStatus("current")


class _TmnxNatUpnpPlcyStatsName_Type(DisplayString):
    """Custom type tmnxNatUpnpPlcyStatsName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_TmnxNatUpnpPlcyStatsName_Type.__name__ = "DisplayString"
_TmnxNatUpnpPlcyStatsName_Object = MibTableColumn
tmnxNatUpnpPlcyStatsName = _TmnxNatUpnpPlcyStatsName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 14, 2, 1, 2),
    _TmnxNatUpnpPlcyStatsName_Type()
)
tmnxNatUpnpPlcyStatsName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatUpnpPlcyStatsName.setStatus("current")
_TmnxNatUpnpPlcyStatsVal_Type = Counter64
_TmnxNatUpnpPlcyStatsVal_Object = MibTableColumn
tmnxNatUpnpPlcyStatsVal = _TmnxNatUpnpPlcyStatsVal_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 14, 2, 1, 3),
    _TmnxNatUpnpPlcyStatsVal_Type()
)
tmnxNatUpnpPlcyStatsVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatUpnpPlcyStatsVal.setStatus("current")
_TmnxNatUpnpPlcyStatTable_Object = MibTable
tmnxNatUpnpPlcyStatTable = _TmnxNatUpnpPlcyStatTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 14, 3)
)
if mibBuilder.loadTexts:
    tmnxNatUpnpPlcyStatTable.setStatus("current")
_TmnxNatUpnpPlcyStatEntry_Object = MibTableRow
tmnxNatUpnpPlcyStatEntry = _TmnxNatUpnpPlcyStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 14, 3, 1)
)
if mibBuilder.loadTexts:
    tmnxNatUpnpPlcyStatEntry.setStatus("current")
_TmnxNatUpnpPlcyStatActMappings_Type = Gauge32
_TmnxNatUpnpPlcyStatActMappings_Object = MibTableColumn
tmnxNatUpnpPlcyStatActMappings = _TmnxNatUpnpPlcyStatActMappings_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 14, 3, 1, 1),
    _TmnxNatUpnpPlcyStatActMappings_Type()
)
tmnxNatUpnpPlcyStatActMappings.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatUpnpPlcyStatActMappings.setStatus("current")
_TmnxNatUpnpPlcyStatSubscrMapped_Type = Gauge32
_TmnxNatUpnpPlcyStatSubscrMapped_Object = MibTableColumn
tmnxNatUpnpPlcyStatSubscrMapped = _TmnxNatUpnpPlcyStatSubscrMapped_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 14, 3, 1, 2),
    _TmnxNatUpnpPlcyStatSubscrMapped_Type()
)
tmnxNatUpnpPlcyStatSubscrMapped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatUpnpPlcyStatSubscrMapped.setStatus("current")
_TmnxNatUpnpPlcyStatSubscr_Type = Gauge32
_TmnxNatUpnpPlcyStatSubscr_Object = MibTableColumn
tmnxNatUpnpPlcyStatSubscr = _TmnxNatUpnpPlcyStatSubscr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 14, 3, 1, 3),
    _TmnxNatUpnpPlcyStatSubscr_Type()
)
tmnxNatUpnpPlcyStatSubscr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatUpnpPlcyStatSubscr.setStatus("current")
_TmnxNatClassifierObjs_ObjectIdentity = ObjectIdentity
tmnxNatClassifierObjs = _TmnxNatClassifierObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 15)
)
_TmnxNatClsfrTable_Object = MibTable
tmnxNatClsfrTable = _TmnxNatClsfrTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 15, 1)
)
if mibBuilder.loadTexts:
    tmnxNatClsfrTable.setStatus("current")
_TmnxNatClsfrEntry_Object = MibTableRow
tmnxNatClsfrEntry = _TmnxNatClsfrEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 15, 1, 1)
)
tmnxNatClsfrEntry.setIndexNames(
    (1, "TIMETRA-NAT-MIB", "tmnxNatClsfrName"),
)
if mibBuilder.loadTexts:
    tmnxNatClsfrEntry.setStatus("current")
_TmnxNatClsfrName_Type = TNamedItem
_TmnxNatClsfrName_Object = MibTableColumn
tmnxNatClsfrName = _TmnxNatClsfrName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 15, 1, 1, 1),
    _TmnxNatClsfrName_Type()
)
tmnxNatClsfrName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxNatClsfrName.setStatus("current")
_TmnxNatClsfrRowStatus_Type = RowStatus
_TmnxNatClsfrRowStatus_Object = MibTableColumn
tmnxNatClsfrRowStatus = _TmnxNatClsfrRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 15, 1, 1, 2),
    _TmnxNatClsfrRowStatus_Type()
)
tmnxNatClsfrRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxNatClsfrRowStatus.setStatus("current")
_TmnxNatClsfrLastCh_Type = TimeStamp
_TmnxNatClsfrLastCh_Object = MibTableColumn
tmnxNatClsfrLastCh = _TmnxNatClsfrLastCh_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 15, 1, 1, 3),
    _TmnxNatClsfrLastCh_Type()
)
tmnxNatClsfrLastCh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatClsfrLastCh.setStatus("current")


class _TmnxNatClsfrDescription_Type(TItemDescription):
    """Custom type tmnxNatClsfrDescription based on TItemDescription"""
    defaultValue = OctetString("")


_TmnxNatClsfrDescription_Type.__name__ = "TItemDescription"
_TmnxNatClsfrDescription_Object = MibTableColumn
tmnxNatClsfrDescription = _TmnxNatClsfrDescription_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 15, 1, 1, 4),
    _TmnxNatClsfrDescription_Type()
)
tmnxNatClsfrDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxNatClsfrDescription.setStatus("current")


class _TmnxNatClsfrDefaultAction_Type(TmnxNatClassifierAction):
    """Custom type tmnxNatClsfrDefaultAction based on TmnxNatClassifierAction"""
    defaultValue = 2


_TmnxNatClsfrDefaultAction_Type.__name__ = "TmnxNatClassifierAction"
_TmnxNatClsfrDefaultAction_Object = MibTableColumn
tmnxNatClsfrDefaultAction = _TmnxNatClsfrDefaultAction_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 15, 1, 1, 5),
    _TmnxNatClsfrDefaultAction_Type()
)
tmnxNatClsfrDefaultAction.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxNatClsfrDefaultAction.setStatus("current")


class _TmnxNatClsfrDefaultActionAddrTyp_Type(InetAddressType):
    """Custom type tmnxNatClsfrDefaultActionAddrTyp based on InetAddressType"""
    defaultValue = 0


_TmnxNatClsfrDefaultActionAddrTyp_Type.__name__ = "InetAddressType"
_TmnxNatClsfrDefaultActionAddrTyp_Object = MibTableColumn
tmnxNatClsfrDefaultActionAddrTyp = _TmnxNatClsfrDefaultActionAddrTyp_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 15, 1, 1, 6),
    _TmnxNatClsfrDefaultActionAddrTyp_Type()
)
tmnxNatClsfrDefaultActionAddrTyp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxNatClsfrDefaultActionAddrTyp.setStatus("current")


class _TmnxNatClsfrDefaultActionAddr_Type(InetAddress):
    """Custom type tmnxNatClsfrDefaultActionAddr based on InetAddress"""
    defaultHexValue = ""

    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
    )


_TmnxNatClsfrDefaultActionAddr_Type.__name__ = "InetAddress"
_TmnxNatClsfrDefaultActionAddr_Object = MibTableColumn
tmnxNatClsfrDefaultActionAddr = _TmnxNatClsfrDefaultActionAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 15, 1, 1, 7),
    _TmnxNatClsfrDefaultActionAddr_Type()
)
tmnxNatClsfrDefaultActionAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxNatClsfrDefaultActionAddr.setStatus("current")


class _TmnxNatClsfrDefaultDnatAddrType_Type(InetAddressType):
    """Custom type tmnxNatClsfrDefaultDnatAddrType based on InetAddressType"""
    defaultValue = 0


_TmnxNatClsfrDefaultDnatAddrType_Type.__name__ = "InetAddressType"
_TmnxNatClsfrDefaultDnatAddrType_Object = MibTableColumn
tmnxNatClsfrDefaultDnatAddrType = _TmnxNatClsfrDefaultDnatAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 15, 1, 1, 8),
    _TmnxNatClsfrDefaultDnatAddrType_Type()
)
tmnxNatClsfrDefaultDnatAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxNatClsfrDefaultDnatAddrType.setStatus("current")


class _TmnxNatClsfrDefaultDnatAddr_Type(InetAddress):
    """Custom type tmnxNatClsfrDefaultDnatAddr based on InetAddress"""
    defaultHexValue = ""

    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
    )


_TmnxNatClsfrDefaultDnatAddr_Type.__name__ = "InetAddress"
_TmnxNatClsfrDefaultDnatAddr_Object = MibTableColumn
tmnxNatClsfrDefaultDnatAddr = _TmnxNatClsfrDefaultDnatAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 15, 1, 1, 9),
    _TmnxNatClsfrDefaultDnatAddr_Type()
)
tmnxNatClsfrDefaultDnatAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxNatClsfrDefaultDnatAddr.setStatus("current")
_TmnxNatClsfrN3Table_Object = MibTable
tmnxNatClsfrN3Table = _TmnxNatClsfrN3Table_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 15, 2)
)
if mibBuilder.loadTexts:
    tmnxNatClsfrN3Table.setStatus("current")
_TmnxNatClsfrN3Entry_Object = MibTableRow
tmnxNatClsfrN3Entry = _TmnxNatClsfrN3Entry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 15, 2, 1)
)
tmnxNatClsfrN3Entry.setIndexNames(
    (0, "TIMETRA-NAT-MIB", "tmnxNatClsfrName"),
    (0, "TIMETRA-NAT-MIB", "tmnxNatClsfrN3Index"),
)
if mibBuilder.loadTexts:
    tmnxNatClsfrN3Entry.setStatus("current")


class _TmnxNatClsfrN3Index_Type(Unsigned32):
    """Custom type tmnxNatClsfrN3Index based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1000),
    )


_TmnxNatClsfrN3Index_Type.__name__ = "Unsigned32"
_TmnxNatClsfrN3Index_Object = MibTableColumn
tmnxNatClsfrN3Index = _TmnxNatClsfrN3Index_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 15, 2, 1, 1),
    _TmnxNatClsfrN3Index_Type()
)
tmnxNatClsfrN3Index.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxNatClsfrN3Index.setStatus("current")
_TmnxNatClsfrN3RowStatus_Type = RowStatus
_TmnxNatClsfrN3RowStatus_Object = MibTableColumn
tmnxNatClsfrN3RowStatus = _TmnxNatClsfrN3RowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 15, 2, 1, 2),
    _TmnxNatClsfrN3RowStatus_Type()
)
tmnxNatClsfrN3RowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxNatClsfrN3RowStatus.setStatus("current")
_TmnxNatClsfrN3LastCh_Type = TimeStamp
_TmnxNatClsfrN3LastCh_Object = MibTableColumn
tmnxNatClsfrN3LastCh = _TmnxNatClsfrN3LastCh_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 15, 2, 1, 3),
    _TmnxNatClsfrN3LastCh_Type()
)
tmnxNatClsfrN3LastCh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatClsfrN3LastCh.setStatus("current")


class _TmnxNatClsfrN3Description_Type(TItemDescription):
    """Custom type tmnxNatClsfrN3Description based on TItemDescription"""
    defaultValue = OctetString("")


_TmnxNatClsfrN3Description_Type.__name__ = "TItemDescription"
_TmnxNatClsfrN3Description_Object = MibTableColumn
tmnxNatClsfrN3Description = _TmnxNatClsfrN3Description_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 15, 2, 1, 4),
    _TmnxNatClsfrN3Description_Type()
)
tmnxNatClsfrN3Description.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxNatClsfrN3Description.setStatus("current")


class _TmnxNatClsfrN3Action_Type(TmnxNatClassifierActionOrNone):
    """Custom type tmnxNatClsfrN3Action based on TmnxNatClassifierActionOrNone"""
    defaultValue = 0


_TmnxNatClsfrN3Action_Type.__name__ = "TmnxNatClassifierActionOrNone"
_TmnxNatClsfrN3Action_Object = MibTableColumn
tmnxNatClsfrN3Action = _TmnxNatClsfrN3Action_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 15, 2, 1, 5),
    _TmnxNatClsfrN3Action_Type()
)
tmnxNatClsfrN3Action.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxNatClsfrN3Action.setStatus("current")


class _TmnxNatClsfrN3DnatAddrType_Type(InetAddressType):
    """Custom type tmnxNatClsfrN3DnatAddrType based on InetAddressType"""
    defaultValue = 0


_TmnxNatClsfrN3DnatAddrType_Type.__name__ = "InetAddressType"
_TmnxNatClsfrN3DnatAddrType_Object = MibTableColumn
tmnxNatClsfrN3DnatAddrType = _TmnxNatClsfrN3DnatAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 15, 2, 1, 6),
    _TmnxNatClsfrN3DnatAddrType_Type()
)
tmnxNatClsfrN3DnatAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxNatClsfrN3DnatAddrType.setStatus("current")


class _TmnxNatClsfrN3DnatAddr_Type(InetAddress):
    """Custom type tmnxNatClsfrN3DnatAddr based on InetAddress"""
    defaultHexValue = ""

    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
    )


_TmnxNatClsfrN3DnatAddr_Type.__name__ = "InetAddress"
_TmnxNatClsfrN3DnatAddr_Object = MibTableColumn
tmnxNatClsfrN3DnatAddr = _TmnxNatClsfrN3DnatAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 15, 2, 1, 7),
    _TmnxNatClsfrN3DnatAddr_Type()
)
tmnxNatClsfrN3DnatAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxNatClsfrN3DnatAddr.setStatus("current")


class _TmnxNatClsfrN3Protocol_Type(TIpProtocol):
    """Custom type tmnxNatClsfrN3Protocol based on TIpProtocol"""
    defaultValue = 17

    subtypeSpec = TIpProtocol.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(6, 6),
        ValueRangeConstraint(17, 17),
    )


_TmnxNatClsfrN3Protocol_Type.__name__ = "TIpProtocol"
_TmnxNatClsfrN3Protocol_Object = MibTableColumn
tmnxNatClsfrN3Protocol = _TmnxNatClsfrN3Protocol_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 15, 2, 1, 8),
    _TmnxNatClsfrN3Protocol_Type()
)
tmnxNatClsfrN3Protocol.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxNatClsfrN3Protocol.setStatus("current")


class _TmnxNatClsfrN3DestPortStart_Type(InetPortNumber):
    """Custom type tmnxNatClsfrN3DestPortStart based on InetPortNumber"""
    defaultValue = 0


_TmnxNatClsfrN3DestPortStart_Type.__name__ = "InetPortNumber"
_TmnxNatClsfrN3DestPortStart_Object = MibTableColumn
tmnxNatClsfrN3DestPortStart = _TmnxNatClsfrN3DestPortStart_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 15, 2, 1, 11),
    _TmnxNatClsfrN3DestPortStart_Type()
)
tmnxNatClsfrN3DestPortStart.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxNatClsfrN3DestPortStart.setStatus("current")


class _TmnxNatClsfrN3DestPortEnd_Type(InetPortNumber):
    """Custom type tmnxNatClsfrN3DestPortEnd based on InetPortNumber"""
    defaultValue = 65535


_TmnxNatClsfrN3DestPortEnd_Type.__name__ = "InetPortNumber"
_TmnxNatClsfrN3DestPortEnd_Object = MibTableColumn
tmnxNatClsfrN3DestPortEnd = _TmnxNatClsfrN3DestPortEnd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 15, 2, 1, 12),
    _TmnxNatClsfrN3DestPortEnd_Type()
)
tmnxNatClsfrN3DestPortEnd.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxNatClsfrN3DestPortEnd.setStatus("current")


class _TmnxNatClsfrN3ForeignAddrType_Type(InetAddressType):
    """Custom type tmnxNatClsfrN3ForeignAddrType based on InetAddressType"""
    defaultValue = 0


_TmnxNatClsfrN3ForeignAddrType_Type.__name__ = "InetAddressType"
_TmnxNatClsfrN3ForeignAddrType_Object = MibTableColumn
tmnxNatClsfrN3ForeignAddrType = _TmnxNatClsfrN3ForeignAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 15, 2, 1, 13),
    _TmnxNatClsfrN3ForeignAddrType_Type()
)
tmnxNatClsfrN3ForeignAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxNatClsfrN3ForeignAddrType.setStatus("current")


class _TmnxNatClsfrN3ForeignAddr_Type(InetAddress):
    """Custom type tmnxNatClsfrN3ForeignAddr based on InetAddress"""
    defaultHexValue = ""

    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
    )


_TmnxNatClsfrN3ForeignAddr_Type.__name__ = "InetAddress"
_TmnxNatClsfrN3ForeignAddr_Object = MibTableColumn
tmnxNatClsfrN3ForeignAddr = _TmnxNatClsfrN3ForeignAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 15, 2, 1, 14),
    _TmnxNatClsfrN3ForeignAddr_Type()
)
tmnxNatClsfrN3ForeignAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxNatClsfrN3ForeignAddr.setStatus("current")
_TmnxNatMappingObjs_ObjectIdentity = ObjectIdentity
tmnxNatMappingObjs = _TmnxNatMappingObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 16)
)
_TmnxNatMapDomTable_Object = MibTable
tmnxNatMapDomTable = _TmnxNatMapDomTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 16, 1)
)
if mibBuilder.loadTexts:
    tmnxNatMapDomTable.setStatus("current")
_TmnxNatMapDomEntry_Object = MibTableRow
tmnxNatMapDomEntry = _TmnxNatMapDomEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 16, 1, 1)
)
tmnxNatMapDomEntry.setIndexNames(
    (1, "TIMETRA-NAT-MIB", "tmnxNatMapDomName"),
)
if mibBuilder.loadTexts:
    tmnxNatMapDomEntry.setStatus("current")
_TmnxNatMapDomName_Type = TNamedItem
_TmnxNatMapDomName_Object = MibTableColumn
tmnxNatMapDomName = _TmnxNatMapDomName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 16, 1, 1, 1),
    _TmnxNatMapDomName_Type()
)
tmnxNatMapDomName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxNatMapDomName.setStatus("current")
_TmnxNatMapDomRowStatus_Type = RowStatus
_TmnxNatMapDomRowStatus_Object = MibTableColumn
tmnxNatMapDomRowStatus = _TmnxNatMapDomRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 16, 1, 1, 2),
    _TmnxNatMapDomRowStatus_Type()
)
tmnxNatMapDomRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxNatMapDomRowStatus.setStatus("current")
_TmnxNatMapDomLastCh_Type = TimeStamp
_TmnxNatMapDomLastCh_Object = MibTableColumn
tmnxNatMapDomLastCh = _TmnxNatMapDomLastCh_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 16, 1, 1, 3),
    _TmnxNatMapDomLastCh_Type()
)
tmnxNatMapDomLastCh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatMapDomLastCh.setStatus("current")


class _TmnxNatMapDomAdminState_Type(TmnxAdminState):
    """Custom type tmnxNatMapDomAdminState based on TmnxAdminState"""
    defaultValue = 3


_TmnxNatMapDomAdminState_Type.__name__ = "TmnxAdminState"
_TmnxNatMapDomAdminState_Object = MibTableColumn
tmnxNatMapDomAdminState = _TmnxNatMapDomAdminState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 16, 1, 1, 4),
    _TmnxNatMapDomAdminState_Type()
)
tmnxNatMapDomAdminState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxNatMapDomAdminState.setStatus("current")


class _TmnxNatMapDomDescription_Type(TItemDescription):
    """Custom type tmnxNatMapDomDescription based on TItemDescription"""
    defaultValue = OctetString("")


_TmnxNatMapDomDescription_Type.__name__ = "TItemDescription"
_TmnxNatMapDomDescription_Object = MibTableColumn
tmnxNatMapDomDescription = _TmnxNatMapDomDescription_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 16, 1, 1, 5),
    _TmnxNatMapDomDescription_Type()
)
tmnxNatMapDomDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxNatMapDomDescription.setStatus("current")


class _TmnxNatMapDomDmrPrefixType_Type(TmnxAddressAndPrefixType):
    """Custom type tmnxNatMapDomDmrPrefixType based on TmnxAddressAndPrefixType"""
    defaultValue = 0


_TmnxNatMapDomDmrPrefixType_Type.__name__ = "TmnxAddressAndPrefixType"
_TmnxNatMapDomDmrPrefixType_Object = MibTableColumn
tmnxNatMapDomDmrPrefixType = _TmnxNatMapDomDmrPrefixType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 16, 1, 1, 6),
    _TmnxNatMapDomDmrPrefixType_Type()
)
tmnxNatMapDomDmrPrefixType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxNatMapDomDmrPrefixType.setStatus("current")


class _TmnxNatMapDomDmrPrefix_Type(TmnxAddressAndPrefixAddress):
    """Custom type tmnxNatMapDomDmrPrefix based on TmnxAddressAndPrefixAddress"""
    defaultHexValue = ""

    subtypeSpec = TmnxAddressAndPrefixAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(16, 16),
    )


_TmnxNatMapDomDmrPrefix_Type.__name__ = "TmnxAddressAndPrefixAddress"
_TmnxNatMapDomDmrPrefix_Object = MibTableColumn
tmnxNatMapDomDmrPrefix = _TmnxNatMapDomDmrPrefix_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 16, 1, 1, 7),
    _TmnxNatMapDomDmrPrefix_Type()
)
tmnxNatMapDomDmrPrefix.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxNatMapDomDmrPrefix.setStatus("current")


class _TmnxNatMapDomDmrPrefixLength_Type(TmnxAddressAndPrefixPrefix):
    """Custom type tmnxNatMapDomDmrPrefixLength based on TmnxAddressAndPrefixPrefix"""
    defaultValue = 0

    subtypeSpec = TmnxAddressAndPrefixPrefix.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 96),
    )


_TmnxNatMapDomDmrPrefixLength_Type.__name__ = "TmnxAddressAndPrefixPrefix"
_TmnxNatMapDomDmrPrefixLength_Object = MibTableColumn
tmnxNatMapDomDmrPrefixLength = _TmnxNatMapDomDmrPrefixLength_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 16, 1, 1, 8),
    _TmnxNatMapDomDmrPrefixLength_Type()
)
tmnxNatMapDomDmrPrefixLength.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxNatMapDomDmrPrefixLength.setStatus("current")


class _TmnxNatMapDomTcpMssAdjust_Type(Unsigned32):
    """Custom type tmnxNatMapDomTcpMssAdjust based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(160, 8626),
    )


_TmnxNatMapDomTcpMssAdjust_Type.__name__ = "Unsigned32"
_TmnxNatMapDomTcpMssAdjust_Object = MibTableColumn
tmnxNatMapDomTcpMssAdjust = _TmnxNatMapDomTcpMssAdjust_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 16, 1, 1, 9),
    _TmnxNatMapDomTcpMssAdjust_Type()
)
tmnxNatMapDomTcpMssAdjust.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxNatMapDomTcpMssAdjust.setStatus("current")
if mibBuilder.loadTexts:
    tmnxNatMapDomTcpMssAdjust.setUnits("bytes")


class _TmnxNatMapDomMtu_Type(Unsigned32):
    """Custom type tmnxNatMapDomMtu based on Unsigned32"""
    defaultValue = 8686

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(160, 8686),
    )


_TmnxNatMapDomMtu_Type.__name__ = "Unsigned32"
_TmnxNatMapDomMtu_Object = MibTableColumn
tmnxNatMapDomMtu = _TmnxNatMapDomMtu_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 16, 1, 1, 10),
    _TmnxNatMapDomMtu_Type()
)
tmnxNatMapDomMtu.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxNatMapDomMtu.setStatus("current")


class _TmnxNatMapDomIpFragmentation_Type(Bits):
    """Custom type tmnxNatMapDomIpFragmentation based on Bits"""
    defaultBinValue = "0"

    namedValues = NamedValues(
        ("v6FragHeader", 0)
    )

_TmnxNatMapDomIpFragmentation_Type.__name__ = "Bits"
_TmnxNatMapDomIpFragmentation_Object = MibTableColumn
tmnxNatMapDomIpFragmentation = _TmnxNatMapDomIpFragmentation_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 16, 1, 1, 11),
    _TmnxNatMapDomIpFragmentation_Type()
)
tmnxNatMapDomIpFragmentation.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxNatMapDomIpFragmentation.setStatus("current")
_TmnxNatMapDomRouter_Type = TmnxVRtrIDOrZero
_TmnxNatMapDomRouter_Object = MibTableColumn
tmnxNatMapDomRouter = _TmnxNatMapDomRouter_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 16, 1, 1, 12),
    _TmnxNatMapDomRouter_Type()
)
tmnxNatMapDomRouter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatMapDomRouter.setStatus("current")


class _TmnxNatMapDomMapTGrpId_Type(TmnxNatIsaGrpIdOrZero):
    """Custom type tmnxNatMapDomMapTGrpId based on TmnxNatIsaGrpIdOrZero"""
    defaultValue = 0


_TmnxNatMapDomMapTGrpId_Type.__name__ = "TmnxNatIsaGrpIdOrZero"
_TmnxNatMapDomMapTGrpId_Object = MibTableColumn
tmnxNatMapDomMapTGrpId = _TmnxNatMapDomMapTGrpId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 16, 1, 1, 13),
    _TmnxNatMapDomMapTGrpId_Type()
)
tmnxNatMapDomMapTGrpId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxNatMapDomMapTGrpId.setStatus("current")


class _TmnxNatMapDomMapTFpeId_Type(TmnxFpeIdOrZero):
    """Custom type tmnxNatMapDomMapTFpeId based on TmnxFpeIdOrZero"""
    defaultValue = 0


_TmnxNatMapDomMapTFpeId_Type.__name__ = "TmnxFpeIdOrZero"
_TmnxNatMapDomMapTFpeId_Object = MibTableColumn
tmnxNatMapDomMapTFpeId = _TmnxNatMapDomMapTFpeId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 16, 1, 1, 14),
    _TmnxNatMapDomMapTFpeId_Type()
)
tmnxNatMapDomMapTFpeId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxNatMapDomMapTFpeId.setStatus("current")


class _TmnxNatMapDomUdpV6ChksumRecalc_Type(TruthValue):
    """Custom type tmnxNatMapDomUdpV6ChksumRecalc based on TruthValue"""
    defaultValue = 2


_TmnxNatMapDomUdpV6ChksumRecalc_Type.__name__ = "TruthValue"
_TmnxNatMapDomUdpV6ChksumRecalc_Object = MibTableColumn
tmnxNatMapDomUdpV6ChksumRecalc = _TmnxNatMapDomUdpV6ChksumRecalc_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 16, 1, 1, 15),
    _TmnxNatMapDomUdpV6ChksumRecalc_Type()
)
tmnxNatMapDomUdpV6ChksumRecalc.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxNatMapDomUdpV6ChksumRecalc.setStatus("current")
_TmnxNatMapRuleTable_Object = MibTable
tmnxNatMapRuleTable = _TmnxNatMapRuleTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 16, 2)
)
if mibBuilder.loadTexts:
    tmnxNatMapRuleTable.setStatus("current")
_TmnxNatMapRuleEntry_Object = MibTableRow
tmnxNatMapRuleEntry = _TmnxNatMapRuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 16, 2, 1)
)
tmnxNatMapRuleEntry.setIndexNames(
    (0, "TIMETRA-NAT-MIB", "tmnxNatMapDomName"),
    (1, "TIMETRA-NAT-MIB", "tmnxNatMapRuleName"),
)
if mibBuilder.loadTexts:
    tmnxNatMapRuleEntry.setStatus("current")
_TmnxNatMapRuleName_Type = TNamedItem
_TmnxNatMapRuleName_Object = MibTableColumn
tmnxNatMapRuleName = _TmnxNatMapRuleName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 16, 2, 1, 1),
    _TmnxNatMapRuleName_Type()
)
tmnxNatMapRuleName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxNatMapRuleName.setStatus("current")
_TmnxNatMapRuleRowStatus_Type = RowStatus
_TmnxNatMapRuleRowStatus_Object = MibTableColumn
tmnxNatMapRuleRowStatus = _TmnxNatMapRuleRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 16, 2, 1, 2),
    _TmnxNatMapRuleRowStatus_Type()
)
tmnxNatMapRuleRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxNatMapRuleRowStatus.setStatus("current")
_TmnxNatMapRuleLastCh_Type = TimeStamp
_TmnxNatMapRuleLastCh_Object = MibTableColumn
tmnxNatMapRuleLastCh = _TmnxNatMapRuleLastCh_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 16, 2, 1, 3),
    _TmnxNatMapRuleLastCh_Type()
)
tmnxNatMapRuleLastCh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatMapRuleLastCh.setStatus("current")


class _TmnxNatMapRuleAdminState_Type(TmnxAdminState):
    """Custom type tmnxNatMapRuleAdminState based on TmnxAdminState"""
    defaultValue = 3


_TmnxNatMapRuleAdminState_Type.__name__ = "TmnxAdminState"
_TmnxNatMapRuleAdminState_Object = MibTableColumn
tmnxNatMapRuleAdminState = _TmnxNatMapRuleAdminState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 16, 2, 1, 4),
    _TmnxNatMapRuleAdminState_Type()
)
tmnxNatMapRuleAdminState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxNatMapRuleAdminState.setStatus("current")


class _TmnxNatMapRuleDescription_Type(TItemDescription):
    """Custom type tmnxNatMapRuleDescription based on TItemDescription"""
    defaultValue = OctetString("")


_TmnxNatMapRuleDescription_Type.__name__ = "TItemDescription"
_TmnxNatMapRuleDescription_Object = MibTableColumn
tmnxNatMapRuleDescription = _TmnxNatMapRuleDescription_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 16, 2, 1, 5),
    _TmnxNatMapRuleDescription_Type()
)
tmnxNatMapRuleDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxNatMapRuleDescription.setStatus("current")


class _TmnxNatMapRulePrefixType_Type(TmnxAddressAndPrefixType):
    """Custom type tmnxNatMapRulePrefixType based on TmnxAddressAndPrefixType"""
    defaultValue = 0


_TmnxNatMapRulePrefixType_Type.__name__ = "TmnxAddressAndPrefixType"
_TmnxNatMapRulePrefixType_Object = MibTableColumn
tmnxNatMapRulePrefixType = _TmnxNatMapRulePrefixType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 16, 2, 1, 6),
    _TmnxNatMapRulePrefixType_Type()
)
tmnxNatMapRulePrefixType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxNatMapRulePrefixType.setStatus("current")


class _TmnxNatMapRulePrefix_Type(TmnxAddressAndPrefixAddress):
    """Custom type tmnxNatMapRulePrefix based on TmnxAddressAndPrefixAddress"""
    defaultHexValue = ""

    subtypeSpec = TmnxAddressAndPrefixAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(16, 16),
    )


_TmnxNatMapRulePrefix_Type.__name__ = "TmnxAddressAndPrefixAddress"
_TmnxNatMapRulePrefix_Object = MibTableColumn
tmnxNatMapRulePrefix = _TmnxNatMapRulePrefix_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 16, 2, 1, 7),
    _TmnxNatMapRulePrefix_Type()
)
tmnxNatMapRulePrefix.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxNatMapRulePrefix.setStatus("current")


class _TmnxNatMapRulePrefixLength_Type(TmnxAddressAndPrefixPrefix):
    """Custom type tmnxNatMapRulePrefixLength based on TmnxAddressAndPrefixPrefix"""
    defaultValue = 0

    subtypeSpec = TmnxAddressAndPrefixPrefix.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 64),
    )


_TmnxNatMapRulePrefixLength_Type.__name__ = "TmnxAddressAndPrefixPrefix"
_TmnxNatMapRulePrefixLength_Object = MibTableColumn
tmnxNatMapRulePrefixLength = _TmnxNatMapRulePrefixLength_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 16, 2, 1, 8),
    _TmnxNatMapRulePrefixLength_Type()
)
tmnxNatMapRulePrefixLength.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxNatMapRulePrefixLength.setStatus("current")


class _TmnxNatMapRuleIpv4PrefixType_Type(TmnxAddressAndPrefixType):
    """Custom type tmnxNatMapRuleIpv4PrefixType based on TmnxAddressAndPrefixType"""
    defaultValue = 0


_TmnxNatMapRuleIpv4PrefixType_Type.__name__ = "TmnxAddressAndPrefixType"
_TmnxNatMapRuleIpv4PrefixType_Object = MibTableColumn
tmnxNatMapRuleIpv4PrefixType = _TmnxNatMapRuleIpv4PrefixType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 16, 2, 1, 9),
    _TmnxNatMapRuleIpv4PrefixType_Type()
)
tmnxNatMapRuleIpv4PrefixType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxNatMapRuleIpv4PrefixType.setStatus("current")


class _TmnxNatMapRuleIpv4Prefix_Type(TmnxAddressAndPrefixAddress):
    """Custom type tmnxNatMapRuleIpv4Prefix based on TmnxAddressAndPrefixAddress"""
    defaultHexValue = ""

    subtypeSpec = TmnxAddressAndPrefixAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
    )


_TmnxNatMapRuleIpv4Prefix_Type.__name__ = "TmnxAddressAndPrefixAddress"
_TmnxNatMapRuleIpv4Prefix_Object = MibTableColumn
tmnxNatMapRuleIpv4Prefix = _TmnxNatMapRuleIpv4Prefix_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 16, 2, 1, 10),
    _TmnxNatMapRuleIpv4Prefix_Type()
)
tmnxNatMapRuleIpv4Prefix.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxNatMapRuleIpv4Prefix.setStatus("current")


class _TmnxNatMapRuleIpv4PrefixLength_Type(TmnxAddressAndPrefixPrefix):
    """Custom type tmnxNatMapRuleIpv4PrefixLength based on TmnxAddressAndPrefixPrefix"""
    defaultValue = 0

    subtypeSpec = TmnxAddressAndPrefixPrefix.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32),
    )


_TmnxNatMapRuleIpv4PrefixLength_Type.__name__ = "TmnxAddressAndPrefixPrefix"
_TmnxNatMapRuleIpv4PrefixLength_Object = MibTableColumn
tmnxNatMapRuleIpv4PrefixLength = _TmnxNatMapRuleIpv4PrefixLength_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 16, 2, 1, 11),
    _TmnxNatMapRuleIpv4PrefixLength_Type()
)
tmnxNatMapRuleIpv4PrefixLength.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxNatMapRuleIpv4PrefixLength.setStatus("current")


class _TmnxNatMapRuleEaLength_Type(Unsigned32):
    """Custom type tmnxNatMapRuleEaLength based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 48),
    )


_TmnxNatMapRuleEaLength_Type.__name__ = "Unsigned32"
_TmnxNatMapRuleEaLength_Object = MibTableColumn
tmnxNatMapRuleEaLength = _TmnxNatMapRuleEaLength_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 16, 2, 1, 12),
    _TmnxNatMapRuleEaLength_Type()
)
tmnxNatMapRuleEaLength.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxNatMapRuleEaLength.setStatus("current")


class _TmnxNatMapRulePsidOffset_Type(Unsigned32):
    """Custom type tmnxNatMapRulePsidOffset based on Unsigned32"""
    defaultValue = 6

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )


_TmnxNatMapRulePsidOffset_Type.__name__ = "Unsigned32"
_TmnxNatMapRulePsidOffset_Object = MibTableColumn
tmnxNatMapRulePsidOffset = _TmnxNatMapRulePsidOffset_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 16, 2, 1, 13),
    _TmnxNatMapRulePsidOffset_Type()
)
tmnxNatMapRulePsidOffset.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxNatMapRulePsidOffset.setStatus("current")
_TmnxNatMapRuleAddrSharingRatio_Type = Gauge32
_TmnxNatMapRuleAddrSharingRatio_Object = MibTableColumn
tmnxNatMapRuleAddrSharingRatio = _TmnxNatMapRuleAddrSharingRatio_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 16, 2, 1, 14),
    _TmnxNatMapRuleAddrSharingRatio_Type()
)
tmnxNatMapRuleAddrSharingRatio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatMapRuleAddrSharingRatio.setStatus("current")
_TmnxNatMapRuleExcludedPorts_Type = Gauge32
_TmnxNatMapRuleExcludedPorts_Object = MibTableColumn
tmnxNatMapRuleExcludedPorts = _TmnxNatMapRuleExcludedPorts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 16, 2, 1, 15),
    _TmnxNatMapRuleExcludedPorts_Type()
)
tmnxNatMapRuleExcludedPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatMapRuleExcludedPorts.setStatus("current")
_TmnxNatMapRulePortsPerUser_Type = Gauge32
_TmnxNatMapRulePortsPerUser_Object = MibTableColumn
tmnxNatMapRulePortsPerUser = _TmnxNatMapRulePortsPerUser_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 16, 2, 1, 16),
    _TmnxNatMapRulePortsPerUser_Type()
)
tmnxNatMapRulePortsPerUser.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatMapRulePortsPerUser.setStatus("current")


class _TmnxNatMapRuleStatsCollection_Type(TruthValue):
    """Custom type tmnxNatMapRuleStatsCollection based on TruthValue"""
    defaultValue = 2


_TmnxNatMapRuleStatsCollection_Type.__name__ = "TruthValue"
_TmnxNatMapRuleStatsCollection_Object = MibTableColumn
tmnxNatMapRuleStatsCollection = _TmnxNatMapRuleStatsCollection_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 16, 2, 1, 17),
    _TmnxNatMapRuleStatsCollection_Type()
)
tmnxNatMapRuleStatsCollection.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxNatMapRuleStatsCollection.setStatus("current")
_TmnxNatMapVrtrDomTable_Object = MibTable
tmnxNatMapVrtrDomTable = _TmnxNatMapVrtrDomTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 16, 3)
)
if mibBuilder.loadTexts:
    tmnxNatMapVrtrDomTable.setStatus("current")
_TmnxNatMapVrtrDomEntry_Object = MibTableRow
tmnxNatMapVrtrDomEntry = _TmnxNatMapVrtrDomEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 16, 3, 1)
)
tmnxNatMapVrtrDomEntry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (1, "TIMETRA-NAT-MIB", "tmnxNatMapDomName"),
)
if mibBuilder.loadTexts:
    tmnxNatMapVrtrDomEntry.setStatus("current")
_TmnxNatMapVrtrDomRowStatus_Type = RowStatus
_TmnxNatMapVrtrDomRowStatus_Object = MibTableColumn
tmnxNatMapVrtrDomRowStatus = _TmnxNatMapVrtrDomRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 16, 3, 1, 2),
    _TmnxNatMapVrtrDomRowStatus_Type()
)
tmnxNatMapVrtrDomRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxNatMapVrtrDomRowStatus.setStatus("current")
_TmnxNatMapVrtrDomLastCh_Type = TimeStamp
_TmnxNatMapVrtrDomLastCh_Object = MibTableColumn
tmnxNatMapVrtrDomLastCh = _TmnxNatMapVrtrDomLastCh_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 16, 3, 1, 3),
    _TmnxNatMapVrtrDomLastCh_Type()
)
tmnxNatMapVrtrDomLastCh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatMapVrtrDomLastCh.setStatus("current")
_TmnxNatMapDomStatsTable_Object = MibTable
tmnxNatMapDomStatsTable = _TmnxNatMapDomStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 16, 20)
)
if mibBuilder.loadTexts:
    tmnxNatMapDomStatsTable.setStatus("current")
_TmnxNatMapDomStatsEntry_Object = MibTableRow
tmnxNatMapDomStatsEntry = _TmnxNatMapDomStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 16, 20, 1)
)
if mibBuilder.loadTexts:
    tmnxNatMapDomStatsEntry.setStatus("current")
_TmnxNatMapDomUpFwdPackets_Type = Counter64
_TmnxNatMapDomUpFwdPackets_Object = MibTableColumn
tmnxNatMapDomUpFwdPackets = _TmnxNatMapDomUpFwdPackets_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 16, 20, 1, 1),
    _TmnxNatMapDomUpFwdPackets_Type()
)
tmnxNatMapDomUpFwdPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatMapDomUpFwdPackets.setStatus("current")
_TmnxNatMapDomUpFwdOctets_Type = Counter64
_TmnxNatMapDomUpFwdOctets_Object = MibTableColumn
tmnxNatMapDomUpFwdOctets = _TmnxNatMapDomUpFwdOctets_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 16, 20, 1, 2),
    _TmnxNatMapDomUpFwdOctets_Type()
)
tmnxNatMapDomUpFwdOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatMapDomUpFwdOctets.setStatus("current")
_TmnxNatMapDomUpDropPackets_Type = Counter64
_TmnxNatMapDomUpDropPackets_Object = MibTableColumn
tmnxNatMapDomUpDropPackets = _TmnxNatMapDomUpDropPackets_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 16, 20, 1, 3),
    _TmnxNatMapDomUpDropPackets_Type()
)
tmnxNatMapDomUpDropPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatMapDomUpDropPackets.setStatus("current")
_TmnxNatMapDomUpDropOctets_Type = Counter64
_TmnxNatMapDomUpDropOctets_Object = MibTableColumn
tmnxNatMapDomUpDropOctets = _TmnxNatMapDomUpDropOctets_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 16, 20, 1, 4),
    _TmnxNatMapDomUpDropOctets_Type()
)
tmnxNatMapDomUpDropOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatMapDomUpDropOctets.setStatus("current")
_TmnxNatMapDomDownFwdPackets_Type = Counter64
_TmnxNatMapDomDownFwdPackets_Object = MibTableColumn
tmnxNatMapDomDownFwdPackets = _TmnxNatMapDomDownFwdPackets_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 16, 20, 1, 5),
    _TmnxNatMapDomDownFwdPackets_Type()
)
tmnxNatMapDomDownFwdPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatMapDomDownFwdPackets.setStatus("current")
_TmnxNatMapDomDownFwdOctets_Type = Counter64
_TmnxNatMapDomDownFwdOctets_Object = MibTableColumn
tmnxNatMapDomDownFwdOctets = _TmnxNatMapDomDownFwdOctets_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 16, 20, 1, 6),
    _TmnxNatMapDomDownFwdOctets_Type()
)
tmnxNatMapDomDownFwdOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatMapDomDownFwdOctets.setStatus("current")
_TmnxNatMapDomDownDropPackets_Type = Counter64
_TmnxNatMapDomDownDropPackets_Object = MibTableColumn
tmnxNatMapDomDownDropPackets = _TmnxNatMapDomDownDropPackets_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 16, 20, 1, 7),
    _TmnxNatMapDomDownDropPackets_Type()
)
tmnxNatMapDomDownDropPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatMapDomDownDropPackets.setStatus("current")
_TmnxNatMapDomDownDropOctets_Type = Counter64
_TmnxNatMapDomDownDropOctets_Object = MibTableColumn
tmnxNatMapDomDownDropOctets = _TmnxNatMapDomDownDropOctets_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 16, 20, 1, 8),
    _TmnxNatMapDomDownDropOctets_Type()
)
tmnxNatMapDomDownDropOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatMapDomDownDropOctets.setStatus("current")
_TmnxNatMapDomUpDropAntiSpoof_Type = Counter64
_TmnxNatMapDomUpDropAntiSpoof_Object = MibTableColumn
tmnxNatMapDomUpDropAntiSpoof = _TmnxNatMapDomUpDropAntiSpoof_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 16, 20, 1, 9),
    _TmnxNatMapDomUpDropAntiSpoof_Type()
)
tmnxNatMapDomUpDropAntiSpoof.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatMapDomUpDropAntiSpoof.setStatus("current")
_TmnxNatMapDomUpDropIcmp6_Type = Counter64
_TmnxNatMapDomUpDropIcmp6_Object = MibTableColumn
tmnxNatMapDomUpDropIcmp6 = _TmnxNatMapDomUpDropIcmp6_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 16, 20, 1, 10),
    _TmnxNatMapDomUpDropIcmp6_Type()
)
tmnxNatMapDomUpDropIcmp6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatMapDomUpDropIcmp6.setStatus("current")
_TmnxNatMapDomUpDropOther_Type = Counter64
_TmnxNatMapDomUpDropOther_Object = MibTableColumn
tmnxNatMapDomUpDropOther = _TmnxNatMapDomUpDropOther_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 16, 20, 1, 11),
    _TmnxNatMapDomUpDropOther_Type()
)
tmnxNatMapDomUpDropOther.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatMapDomUpDropOther.setStatus("current")
_TmnxNatMapDomUpFragRx_Type = Counter64
_TmnxNatMapDomUpFragRx_Object = MibTableColumn
tmnxNatMapDomUpFragRx = _TmnxNatMapDomUpFragRx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 16, 20, 1, 12),
    _TmnxNatMapDomUpFragRx_Type()
)
tmnxNatMapDomUpFragRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatMapDomUpFragRx.setStatus("current")
_TmnxNatMapDomUpIcmp6NodeInfoRx_Type = Counter64
_TmnxNatMapDomUpIcmp6NodeInfoRx_Object = MibTableColumn
tmnxNatMapDomUpIcmp6NodeInfoRx = _TmnxNatMapDomUpIcmp6NodeInfoRx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 16, 20, 1, 13),
    _TmnxNatMapDomUpIcmp6NodeInfoRx_Type()
)
tmnxNatMapDomUpIcmp6NodeInfoRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatMapDomUpIcmp6NodeInfoRx.setStatus("current")
_TmnxNatMapDomUpCpeIcmp6ErrRepRx_Type = Counter64
_TmnxNatMapDomUpCpeIcmp6ErrRepRx_Object = MibTableColumn
tmnxNatMapDomUpCpeIcmp6ErrRepRx = _TmnxNatMapDomUpCpeIcmp6ErrRepRx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 16, 20, 1, 14),
    _TmnxNatMapDomUpCpeIcmp6ErrRepRx_Type()
)
tmnxNatMapDomUpCpeIcmp6ErrRepRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatMapDomUpCpeIcmp6ErrRepRx.setStatus("current")
_TmnxNatMapDomUpImIcmp6ErrRx_Type = Counter64
_TmnxNatMapDomUpImIcmp6ErrRx_Object = MibTableColumn
tmnxNatMapDomUpImIcmp6ErrRx = _TmnxNatMapDomUpImIcmp6ErrRx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 16, 20, 1, 15),
    _TmnxNatMapDomUpImIcmp6ErrRx_Type()
)
tmnxNatMapDomUpImIcmp6ErrRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatMapDomUpImIcmp6ErrRx.setStatus("current")
_TmnxNatMapDomDownDropUnkPro_Type = Counter64
_TmnxNatMapDomDownDropUnkPro_Object = MibTableColumn
tmnxNatMapDomDownDropUnkPro = _TmnxNatMapDomDownDropUnkPro_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 16, 20, 1, 16),
    _TmnxNatMapDomDownDropUnkPro_Type()
)
tmnxNatMapDomDownDropUnkPro.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatMapDomDownDropUnkPro.setStatus("current")
_TmnxNatMapDomDownDropFragReq_Type = Counter64
_TmnxNatMapDomDownDropFragReq_Object = MibTableColumn
tmnxNatMapDomDownDropFragReq = _TmnxNatMapDomDownDropFragReq_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 16, 20, 1, 17),
    _TmnxNatMapDomDownDropFragReq_Type()
)
tmnxNatMapDomDownDropFragReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatMapDomDownDropFragReq.setStatus("current")
_TmnxNatMapDomDownDropIcmp4_Type = Counter64
_TmnxNatMapDomDownDropIcmp4_Object = MibTableColumn
tmnxNatMapDomDownDropIcmp4 = _TmnxNatMapDomDownDropIcmp4_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 16, 20, 1, 18),
    _TmnxNatMapDomDownDropIcmp4_Type()
)
tmnxNatMapDomDownDropIcmp4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatMapDomDownDropIcmp4.setStatus("current")
_TmnxNatMapDomDownFragRx_Type = Counter64
_TmnxNatMapDomDownFragRx_Object = MibTableColumn
tmnxNatMapDomDownFragRx = _TmnxNatMapDomDownFragRx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 16, 20, 1, 19),
    _TmnxNatMapDomDownFragRx_Type()
)
tmnxNatMapDomDownFragRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatMapDomDownFragRx.setStatus("current")
_TmnxNatMapDomDownFragReq_Type = Counter64
_TmnxNatMapDomDownFragReq_Object = MibTableColumn
tmnxNatMapDomDownFragReq = _TmnxNatMapDomDownFragReq_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 16, 20, 1, 20),
    _TmnxNatMapDomDownFragReq_Type()
)
tmnxNatMapDomDownFragReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatMapDomDownFragReq.setStatus("current")
_TmnxNatMapDomDownIcmp4ErrRepRx_Type = Counter64
_TmnxNatMapDomDownIcmp4ErrRepRx_Object = MibTableColumn
tmnxNatMapDomDownIcmp4ErrRepRx = _TmnxNatMapDomDownIcmp4ErrRepRx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 16, 20, 1, 21),
    _TmnxNatMapDomDownIcmp4ErrRepRx_Type()
)
tmnxNatMapDomDownIcmp4ErrRepRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatMapDomDownIcmp4ErrRepRx.setStatus("current")
_TmnxNatMapDomDownIcmp4EchoRx_Type = Counter64
_TmnxNatMapDomDownIcmp4EchoRx_Object = MibTableColumn
tmnxNatMapDomDownIcmp4EchoRx = _TmnxNatMapDomDownIcmp4EchoRx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 16, 20, 1, 22),
    _TmnxNatMapDomDownIcmp4EchoRx_Type()
)
tmnxNatMapDomDownIcmp4EchoRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatMapDomDownIcmp4EchoRx.setStatus("current")
_TmnxNatMapDomUpDropUnkProto_Type = Counter64
_TmnxNatMapDomUpDropUnkProto_Object = MibTableColumn
tmnxNatMapDomUpDropUnkProto = _TmnxNatMapDomUpDropUnkProto_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 16, 20, 1, 23),
    _TmnxNatMapDomUpDropUnkProto_Type()
)
tmnxNatMapDomUpDropUnkProto.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatMapDomUpDropUnkProto.setStatus("current")
_TmnxNatMapFragStatsTable_Object = MibTable
tmnxNatMapFragStatsTable = _TmnxNatMapFragStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 16, 21)
)
if mibBuilder.loadTexts:
    tmnxNatMapFragStatsTable.setStatus("current")
_TmnxNatMapFragStatsEntry_Object = MibTableRow
tmnxNatMapFragStatsEntry = _TmnxNatMapFragStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 16, 21, 1)
)
tmnxNatMapFragStatsEntry.setIndexNames(
    (0, "TIMETRA-NAT-MIB", "tmnxNatMapFragStatsId"),
)
if mibBuilder.loadTexts:
    tmnxNatMapFragStatsEntry.setStatus("current")


class _TmnxNatMapFragStatsId_Type(Unsigned32):
    """Custom type tmnxNatMapFragStatsId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 19),
    )


_TmnxNatMapFragStatsId_Type.__name__ = "Unsigned32"
_TmnxNatMapFragStatsId_Object = MibTableColumn
tmnxNatMapFragStatsId = _TmnxNatMapFragStatsId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 16, 21, 1, 1),
    _TmnxNatMapFragStatsId_Type()
)
tmnxNatMapFragStatsId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxNatMapFragStatsId.setStatus("current")


class _TmnxNatMapFragStatsName_Type(DisplayString):
    """Custom type tmnxNatMapFragStatsName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_TmnxNatMapFragStatsName_Type.__name__ = "DisplayString"
_TmnxNatMapFragStatsName_Object = MibTableColumn
tmnxNatMapFragStatsName = _TmnxNatMapFragStatsName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 16, 21, 1, 2),
    _TmnxNatMapFragStatsName_Type()
)
tmnxNatMapFragStatsName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatMapFragStatsName.setStatus("current")
_TmnxNatMapFragStatsVal_Type = Counter64
_TmnxNatMapFragStatsVal_Object = MibTableColumn
tmnxNatMapFragStatsVal = _TmnxNatMapFragStatsVal_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 16, 21, 1, 3),
    _TmnxNatMapFragStatsVal_Type()
)
tmnxNatMapFragStatsVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatMapFragStatsVal.setStatus("current")
_TmnxNatMapRuleStatsTable_Object = MibTable
tmnxNatMapRuleStatsTable = _TmnxNatMapRuleStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 16, 22)
)
if mibBuilder.loadTexts:
    tmnxNatMapRuleStatsTable.setStatus("current")
_TmnxNatMapRuleStatsEntry_Object = MibTableRow
tmnxNatMapRuleStatsEntry = _TmnxNatMapRuleStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 16, 22, 1)
)
if mibBuilder.loadTexts:
    tmnxNatMapRuleStatsEntry.setStatus("current")
_TmnxNatMapRuleUpFwdPackets_Type = Counter64
_TmnxNatMapRuleUpFwdPackets_Object = MibTableColumn
tmnxNatMapRuleUpFwdPackets = _TmnxNatMapRuleUpFwdPackets_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 16, 22, 1, 1),
    _TmnxNatMapRuleUpFwdPackets_Type()
)
tmnxNatMapRuleUpFwdPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatMapRuleUpFwdPackets.setStatus("current")
_TmnxNatMapRuleUpFwdOctets_Type = Counter64
_TmnxNatMapRuleUpFwdOctets_Object = MibTableColumn
tmnxNatMapRuleUpFwdOctets = _TmnxNatMapRuleUpFwdOctets_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 16, 22, 1, 2),
    _TmnxNatMapRuleUpFwdOctets_Type()
)
tmnxNatMapRuleUpFwdOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatMapRuleUpFwdOctets.setStatus("current")
_TmnxNatMapRuleUpDropPackets_Type = Counter64
_TmnxNatMapRuleUpDropPackets_Object = MibTableColumn
tmnxNatMapRuleUpDropPackets = _TmnxNatMapRuleUpDropPackets_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 16, 22, 1, 3),
    _TmnxNatMapRuleUpDropPackets_Type()
)
tmnxNatMapRuleUpDropPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatMapRuleUpDropPackets.setStatus("current")
_TmnxNatMapRuleUpDropOctets_Type = Counter64
_TmnxNatMapRuleUpDropOctets_Object = MibTableColumn
tmnxNatMapRuleUpDropOctets = _TmnxNatMapRuleUpDropOctets_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 16, 22, 1, 4),
    _TmnxNatMapRuleUpDropOctets_Type()
)
tmnxNatMapRuleUpDropOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatMapRuleUpDropOctets.setStatus("current")
_TmnxNatMapRuleDownFwdPackets_Type = Counter64
_TmnxNatMapRuleDownFwdPackets_Object = MibTableColumn
tmnxNatMapRuleDownFwdPackets = _TmnxNatMapRuleDownFwdPackets_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 16, 22, 1, 5),
    _TmnxNatMapRuleDownFwdPackets_Type()
)
tmnxNatMapRuleDownFwdPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatMapRuleDownFwdPackets.setStatus("current")
_TmnxNatMapRuleDownFwdOctets_Type = Counter64
_TmnxNatMapRuleDownFwdOctets_Object = MibTableColumn
tmnxNatMapRuleDownFwdOctets = _TmnxNatMapRuleDownFwdOctets_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 16, 22, 1, 6),
    _TmnxNatMapRuleDownFwdOctets_Type()
)
tmnxNatMapRuleDownFwdOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatMapRuleDownFwdOctets.setStatus("current")
_TmnxNatMapRuleDownDropPackets_Type = Counter64
_TmnxNatMapRuleDownDropPackets_Object = MibTableColumn
tmnxNatMapRuleDownDropPackets = _TmnxNatMapRuleDownDropPackets_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 16, 22, 1, 7),
    _TmnxNatMapRuleDownDropPackets_Type()
)
tmnxNatMapRuleDownDropPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatMapRuleDownDropPackets.setStatus("current")
_TmnxNatMapRuleDownDropOctets_Type = Counter64
_TmnxNatMapRuleDownDropOctets_Object = MibTableColumn
tmnxNatMapRuleDownDropOctets = _TmnxNatMapRuleDownDropOctets_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 16, 22, 1, 8),
    _TmnxNatMapRuleDownDropOctets_Type()
)
tmnxNatMapRuleDownDropOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatMapRuleDownDropOctets.setStatus("current")
_TmnxNatMapRuleUpDropAntiSpoof_Type = Counter64
_TmnxNatMapRuleUpDropAntiSpoof_Object = MibTableColumn
tmnxNatMapRuleUpDropAntiSpoof = _TmnxNatMapRuleUpDropAntiSpoof_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 16, 22, 1, 9),
    _TmnxNatMapRuleUpDropAntiSpoof_Type()
)
tmnxNatMapRuleUpDropAntiSpoof.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatMapRuleUpDropAntiSpoof.setStatus("current")
_TmnxNatMapRuleUpDropIcmp6_Type = Counter64
_TmnxNatMapRuleUpDropIcmp6_Object = MibTableColumn
tmnxNatMapRuleUpDropIcmp6 = _TmnxNatMapRuleUpDropIcmp6_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 16, 22, 1, 10),
    _TmnxNatMapRuleUpDropIcmp6_Type()
)
tmnxNatMapRuleUpDropIcmp6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatMapRuleUpDropIcmp6.setStatus("current")
_TmnxNatMapRuleUpDropOther_Type = Counter64
_TmnxNatMapRuleUpDropOther_Object = MibTableColumn
tmnxNatMapRuleUpDropOther = _TmnxNatMapRuleUpDropOther_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 16, 22, 1, 11),
    _TmnxNatMapRuleUpDropOther_Type()
)
tmnxNatMapRuleUpDropOther.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatMapRuleUpDropOther.setStatus("current")
_TmnxNatMapRuleUpFragRx_Type = Counter64
_TmnxNatMapRuleUpFragRx_Object = MibTableColumn
tmnxNatMapRuleUpFragRx = _TmnxNatMapRuleUpFragRx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 16, 22, 1, 12),
    _TmnxNatMapRuleUpFragRx_Type()
)
tmnxNatMapRuleUpFragRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatMapRuleUpFragRx.setStatus("current")
_TmnxNatMapRuleUpIcmp6NodeInfoRx_Type = Counter64
_TmnxNatMapRuleUpIcmp6NodeInfoRx_Object = MibTableColumn
tmnxNatMapRuleUpIcmp6NodeInfoRx = _TmnxNatMapRuleUpIcmp6NodeInfoRx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 16, 22, 1, 13),
    _TmnxNatMapRuleUpIcmp6NodeInfoRx_Type()
)
tmnxNatMapRuleUpIcmp6NodeInfoRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatMapRuleUpIcmp6NodeInfoRx.setStatus("current")
_TmnxNatMapRuleUpCpeIcmp6ErrRepRx_Type = Counter64
_TmnxNatMapRuleUpCpeIcmp6ErrRepRx_Object = MibTableColumn
tmnxNatMapRuleUpCpeIcmp6ErrRepRx = _TmnxNatMapRuleUpCpeIcmp6ErrRepRx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 16, 22, 1, 14),
    _TmnxNatMapRuleUpCpeIcmp6ErrRepRx_Type()
)
tmnxNatMapRuleUpCpeIcmp6ErrRepRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatMapRuleUpCpeIcmp6ErrRepRx.setStatus("current")
_TmnxNatMapRuleUpImIcmp6ErrRx_Type = Counter64
_TmnxNatMapRuleUpImIcmp6ErrRx_Object = MibTableColumn
tmnxNatMapRuleUpImIcmp6ErrRx = _TmnxNatMapRuleUpImIcmp6ErrRx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 16, 22, 1, 15),
    _TmnxNatMapRuleUpImIcmp6ErrRx_Type()
)
tmnxNatMapRuleUpImIcmp6ErrRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatMapRuleUpImIcmp6ErrRx.setStatus("current")
_TmnxNatMapRuleDownDropUnkPro_Type = Counter64
_TmnxNatMapRuleDownDropUnkPro_Object = MibTableColumn
tmnxNatMapRuleDownDropUnkPro = _TmnxNatMapRuleDownDropUnkPro_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 16, 22, 1, 16),
    _TmnxNatMapRuleDownDropUnkPro_Type()
)
tmnxNatMapRuleDownDropUnkPro.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatMapRuleDownDropUnkPro.setStatus("current")
_TmnxNatMapRuleDownDropFragReq_Type = Counter64
_TmnxNatMapRuleDownDropFragReq_Object = MibTableColumn
tmnxNatMapRuleDownDropFragReq = _TmnxNatMapRuleDownDropFragReq_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 16, 22, 1, 17),
    _TmnxNatMapRuleDownDropFragReq_Type()
)
tmnxNatMapRuleDownDropFragReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatMapRuleDownDropFragReq.setStatus("current")
_TmnxNatMapRuleDownDropIcmp4_Type = Counter64
_TmnxNatMapRuleDownDropIcmp4_Object = MibTableColumn
tmnxNatMapRuleDownDropIcmp4 = _TmnxNatMapRuleDownDropIcmp4_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 16, 22, 1, 18),
    _TmnxNatMapRuleDownDropIcmp4_Type()
)
tmnxNatMapRuleDownDropIcmp4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatMapRuleDownDropIcmp4.setStatus("current")
_TmnxNatMapRuleDownFragRx_Type = Counter64
_TmnxNatMapRuleDownFragRx_Object = MibTableColumn
tmnxNatMapRuleDownFragRx = _TmnxNatMapRuleDownFragRx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 16, 22, 1, 19),
    _TmnxNatMapRuleDownFragRx_Type()
)
tmnxNatMapRuleDownFragRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatMapRuleDownFragRx.setStatus("current")
_TmnxNatMapRuleDownFragReq_Type = Counter64
_TmnxNatMapRuleDownFragReq_Object = MibTableColumn
tmnxNatMapRuleDownFragReq = _TmnxNatMapRuleDownFragReq_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 16, 22, 1, 20),
    _TmnxNatMapRuleDownFragReq_Type()
)
tmnxNatMapRuleDownFragReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatMapRuleDownFragReq.setStatus("current")
_TmnxNatMapRuleDownIcmp4ErrRepRx_Type = Counter64
_TmnxNatMapRuleDownIcmp4ErrRepRx_Object = MibTableColumn
tmnxNatMapRuleDownIcmp4ErrRepRx = _TmnxNatMapRuleDownIcmp4ErrRepRx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 16, 22, 1, 21),
    _TmnxNatMapRuleDownIcmp4ErrRepRx_Type()
)
tmnxNatMapRuleDownIcmp4ErrRepRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatMapRuleDownIcmp4ErrRepRx.setStatus("current")
_TmnxNatMapRuleDownIcmp4EchoRx_Type = Counter64
_TmnxNatMapRuleDownIcmp4EchoRx_Object = MibTableColumn
tmnxNatMapRuleDownIcmp4EchoRx = _TmnxNatMapRuleDownIcmp4EchoRx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 16, 22, 1, 22),
    _TmnxNatMapRuleDownIcmp4EchoRx_Type()
)
tmnxNatMapRuleDownIcmp4EchoRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatMapRuleDownIcmp4EchoRx.setStatus("current")
_TmnxNatMapRuleUpDropUnkProto_Type = Counter64
_TmnxNatMapRuleUpDropUnkProto_Object = MibTableColumn
tmnxNatMapRuleUpDropUnkProto = _TmnxNatMapRuleUpDropUnkProto_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 16, 22, 1, 23),
    _TmnxNatMapRuleUpDropUnkProto_Type()
)
tmnxNatMapRuleUpDropUnkProto.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatMapRuleUpDropUnkProto.setStatus("current")
_TmnxMapTDomVappStatsTable_Object = MibTable
tmnxMapTDomVappStatsTable = _TmnxMapTDomVappStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 16, 23)
)
if mibBuilder.loadTexts:
    tmnxMapTDomVappStatsTable.setStatus("current")
_TmnxMapTDomVappStatsEntry_Object = MibTableRow
tmnxMapTDomVappStatsEntry = _TmnxMapTDomVappStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 16, 23, 1)
)
tmnxMapTDomVappStatsEntry.setIndexNames(
    (0, "TIMETRA-NAT-MIB", "tmnxNatMapDomName"),
    (0, "TIMETRA-NAT-MIB", "tmnxMapTVappEsaNum"),
    (0, "TIMETRA-NAT-MIB", "tmnxMapTVappEsaVappNum"),
)
if mibBuilder.loadTexts:
    tmnxMapTDomVappStatsEntry.setStatus("current")
_TmnxMapTDomVappUpFwdPackets_Type = Counter64
_TmnxMapTDomVappUpFwdPackets_Object = MibTableColumn
tmnxMapTDomVappUpFwdPackets = _TmnxMapTDomVappUpFwdPackets_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 16, 23, 1, 1),
    _TmnxMapTDomVappUpFwdPackets_Type()
)
tmnxMapTDomVappUpFwdPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMapTDomVappUpFwdPackets.setStatus("current")
_TmnxMapTDomVappUpFwdOctets_Type = Counter64
_TmnxMapTDomVappUpFwdOctets_Object = MibTableColumn
tmnxMapTDomVappUpFwdOctets = _TmnxMapTDomVappUpFwdOctets_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 16, 23, 1, 2),
    _TmnxMapTDomVappUpFwdOctets_Type()
)
tmnxMapTDomVappUpFwdOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMapTDomVappUpFwdOctets.setStatus("current")
_TmnxMapTDomVappUpDropPackets_Type = Counter64
_TmnxMapTDomVappUpDropPackets_Object = MibTableColumn
tmnxMapTDomVappUpDropPackets = _TmnxMapTDomVappUpDropPackets_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 16, 23, 1, 3),
    _TmnxMapTDomVappUpDropPackets_Type()
)
tmnxMapTDomVappUpDropPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMapTDomVappUpDropPackets.setStatus("current")
_TmnxMapTDomVappUpDropOctets_Type = Counter64
_TmnxMapTDomVappUpDropOctets_Object = MibTableColumn
tmnxMapTDomVappUpDropOctets = _TmnxMapTDomVappUpDropOctets_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 16, 23, 1, 4),
    _TmnxMapTDomVappUpDropOctets_Type()
)
tmnxMapTDomVappUpDropOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMapTDomVappUpDropOctets.setStatus("current")
_TmnxMapTDomVappUpDropAntiSpoof_Type = Counter64
_TmnxMapTDomVappUpDropAntiSpoof_Object = MibTableColumn
tmnxMapTDomVappUpDropAntiSpoof = _TmnxMapTDomVappUpDropAntiSpoof_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 16, 23, 1, 5),
    _TmnxMapTDomVappUpDropAntiSpoof_Type()
)
tmnxMapTDomVappUpDropAntiSpoof.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMapTDomVappUpDropAntiSpoof.setStatus("current")
_TmnxMapTDomVappUpDropIcmp6_Type = Counter64
_TmnxMapTDomVappUpDropIcmp6_Object = MibTableColumn
tmnxMapTDomVappUpDropIcmp6 = _TmnxMapTDomVappUpDropIcmp6_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 16, 23, 1, 6),
    _TmnxMapTDomVappUpDropIcmp6_Type()
)
tmnxMapTDomVappUpDropIcmp6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMapTDomVappUpDropIcmp6.setStatus("current")
_TmnxMapTDomVappUpDropUnkProto_Type = Counter64
_TmnxMapTDomVappUpDropUnkProto_Object = MibTableColumn
tmnxMapTDomVappUpDropUnkProto = _TmnxMapTDomVappUpDropUnkProto_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 16, 23, 1, 7),
    _TmnxMapTDomVappUpDropUnkProto_Type()
)
tmnxMapTDomVappUpDropUnkProto.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMapTDomVappUpDropUnkProto.setStatus("current")
_TmnxMapTDomVappUpFragRx_Type = Counter64
_TmnxMapTDomVappUpFragRx_Object = MibTableColumn
tmnxMapTDomVappUpFragRx = _TmnxMapTDomVappUpFragRx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 16, 23, 1, 9),
    _TmnxMapTDomVappUpFragRx_Type()
)
tmnxMapTDomVappUpFragRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMapTDomVappUpFragRx.setStatus("current")
_TmnxMapTDomVappUpIcmp6EchoRx_Type = Counter64
_TmnxMapTDomVappUpIcmp6EchoRx_Object = MibTableColumn
tmnxMapTDomVappUpIcmp6EchoRx = _TmnxMapTDomVappUpIcmp6EchoRx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 16, 23, 1, 11),
    _TmnxMapTDomVappUpIcmp6EchoRx_Type()
)
tmnxMapTDomVappUpIcmp6EchoRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMapTDomVappUpIcmp6EchoRx.setStatus("current")
_TmnxMapTDomVappUpCpeIcmp6ErrRx_Type = Counter64
_TmnxMapTDomVappUpCpeIcmp6ErrRx_Object = MibTableColumn
tmnxMapTDomVappUpCpeIcmp6ErrRx = _TmnxMapTDomVappUpCpeIcmp6ErrRx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 16, 23, 1, 12),
    _TmnxMapTDomVappUpCpeIcmp6ErrRx_Type()
)
tmnxMapTDomVappUpCpeIcmp6ErrRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMapTDomVappUpCpeIcmp6ErrRx.setStatus("current")
_TmnxMapTDomVappUpImIcmp6ErrRx_Type = Counter64
_TmnxMapTDomVappUpImIcmp6ErrRx_Object = MibTableColumn
tmnxMapTDomVappUpImIcmp6ErrRx = _TmnxMapTDomVappUpImIcmp6ErrRx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 16, 23, 1, 13),
    _TmnxMapTDomVappUpImIcmp6ErrRx_Type()
)
tmnxMapTDomVappUpImIcmp6ErrRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMapTDomVappUpImIcmp6ErrRx.setStatus("current")
_TmnxMapTDomVappDownFwdPackets_Type = Counter64
_TmnxMapTDomVappDownFwdPackets_Object = MibTableColumn
tmnxMapTDomVappDownFwdPackets = _TmnxMapTDomVappDownFwdPackets_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 16, 23, 1, 14),
    _TmnxMapTDomVappDownFwdPackets_Type()
)
tmnxMapTDomVappDownFwdPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMapTDomVappDownFwdPackets.setStatus("current")
_TmnxMapTDomVappDownFwdOctets_Type = Counter64
_TmnxMapTDomVappDownFwdOctets_Object = MibTableColumn
tmnxMapTDomVappDownFwdOctets = _TmnxMapTDomVappDownFwdOctets_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 16, 23, 1, 15),
    _TmnxMapTDomVappDownFwdOctets_Type()
)
tmnxMapTDomVappDownFwdOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMapTDomVappDownFwdOctets.setStatus("current")
_TmnxMapTDomVappDownDropPackets_Type = Counter64
_TmnxMapTDomVappDownDropPackets_Object = MibTableColumn
tmnxMapTDomVappDownDropPackets = _TmnxMapTDomVappDownDropPackets_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 16, 23, 1, 16),
    _TmnxMapTDomVappDownDropPackets_Type()
)
tmnxMapTDomVappDownDropPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMapTDomVappDownDropPackets.setStatus("current")
_TmnxMapTDomVappDownDropOctets_Type = Counter64
_TmnxMapTDomVappDownDropOctets_Object = MibTableColumn
tmnxMapTDomVappDownDropOctets = _TmnxMapTDomVappDownDropOctets_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 16, 23, 1, 17),
    _TmnxMapTDomVappDownDropOctets_Type()
)
tmnxMapTDomVappDownDropOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMapTDomVappDownDropOctets.setStatus("current")
_TmnxMapTDomVappDownDropFragRx_Type = Counter64
_TmnxMapTDomVappDownDropFragRx_Object = MibTableColumn
tmnxMapTDomVappDownDropFragRx = _TmnxMapTDomVappDownDropFragRx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 16, 23, 1, 18),
    _TmnxMapTDomVappDownDropFragRx_Type()
)
tmnxMapTDomVappDownDropFragRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMapTDomVappDownDropFragRx.setStatus("current")
_TmnxMapTDomVappDownDropFragReq_Type = Counter64
_TmnxMapTDomVappDownDropFragReq_Object = MibTableColumn
tmnxMapTDomVappDownDropFragReq = _TmnxMapTDomVappDownDropFragReq_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 16, 23, 1, 19),
    _TmnxMapTDomVappDownDropFragReq_Type()
)
tmnxMapTDomVappDownDropFragReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMapTDomVappDownDropFragReq.setStatus("current")
_TmnxMapTDomVappDownDropIcmp4_Type = Counter64
_TmnxMapTDomVappDownDropIcmp4_Object = MibTableColumn
tmnxMapTDomVappDownDropIcmp4 = _TmnxMapTDomVappDownDropIcmp4_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 16, 23, 1, 20),
    _TmnxMapTDomVappDownDropIcmp4_Type()
)
tmnxMapTDomVappDownDropIcmp4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMapTDomVappDownDropIcmp4.setStatus("current")
_TmnxMapTDomVappDownDropUnkProto_Type = Counter64
_TmnxMapTDomVappDownDropUnkProto_Object = MibTableColumn
tmnxMapTDomVappDownDropUnkProto = _TmnxMapTDomVappDownDropUnkProto_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 16, 23, 1, 21),
    _TmnxMapTDomVappDownDropUnkProto_Type()
)
tmnxMapTDomVappDownDropUnkProto.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMapTDomVappDownDropUnkProto.setStatus("current")
_TmnxMapTDomVappDownFragRx_Type = Counter64
_TmnxMapTDomVappDownFragRx_Object = MibTableColumn
tmnxMapTDomVappDownFragRx = _TmnxMapTDomVappDownFragRx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 16, 23, 1, 22),
    _TmnxMapTDomVappDownFragRx_Type()
)
tmnxMapTDomVappDownFragRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMapTDomVappDownFragRx.setStatus("current")
_TmnxMapTDomVappDownFragReq_Type = Counter64
_TmnxMapTDomVappDownFragReq_Object = MibTableColumn
tmnxMapTDomVappDownFragReq = _TmnxMapTDomVappDownFragReq_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 16, 23, 1, 23),
    _TmnxMapTDomVappDownFragReq_Type()
)
tmnxMapTDomVappDownFragReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMapTDomVappDownFragReq.setStatus("current")
_TmnxMapTDomVappDownIcmp4EchoRx_Type = Counter64
_TmnxMapTDomVappDownIcmp4EchoRx_Object = MibTableColumn
tmnxMapTDomVappDownIcmp4EchoRx = _TmnxMapTDomVappDownIcmp4EchoRx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 16, 23, 1, 24),
    _TmnxMapTDomVappDownIcmp4EchoRx_Type()
)
tmnxMapTDomVappDownIcmp4EchoRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMapTDomVappDownIcmp4EchoRx.setStatus("current")
_TmnxMapTDomVappDownIcmp4ErrRepRx_Type = Counter64
_TmnxMapTDomVappDownIcmp4ErrRepRx_Object = MibTableColumn
tmnxMapTDomVappDownIcmp4ErrRepRx = _TmnxMapTDomVappDownIcmp4ErrRepRx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 16, 23, 1, 25),
    _TmnxMapTDomVappDownIcmp4ErrRepRx_Type()
)
tmnxMapTDomVappDownIcmp4ErrRepRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMapTDomVappDownIcmp4ErrRepRx.setStatus("current")
_TmnxMapTDomVappIcmp4ErrFragDf_Type = Counter64
_TmnxMapTDomVappIcmp4ErrFragDf_Object = MibTableColumn
tmnxMapTDomVappIcmp4ErrFragDf = _TmnxMapTDomVappIcmp4ErrFragDf_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 16, 23, 1, 26),
    _TmnxMapTDomVappIcmp4ErrFragDf_Type()
)
tmnxMapTDomVappIcmp4ErrFragDf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMapTDomVappIcmp4ErrFragDf.setStatus("current")
_TmnxMapTDomVappDownUdpRecalc_Type = Counter64
_TmnxMapTDomVappDownUdpRecalc_Object = MibTableColumn
tmnxMapTDomVappDownUdpRecalc = _TmnxMapTDomVappDownUdpRecalc_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 16, 23, 1, 27),
    _TmnxMapTDomVappDownUdpRecalc_Type()
)
tmnxMapTDomVappDownUdpRecalc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMapTDomVappDownUdpRecalc.setStatus("current")
_TmnxMapTRuleVappStatsTable_Object = MibTable
tmnxMapTRuleVappStatsTable = _TmnxMapTRuleVappStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 16, 24)
)
if mibBuilder.loadTexts:
    tmnxMapTRuleVappStatsTable.setStatus("current")
_TmnxMapTRuleVappStatsEntry_Object = MibTableRow
tmnxMapTRuleVappStatsEntry = _TmnxMapTRuleVappStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 16, 24, 1)
)
tmnxMapTRuleVappStatsEntry.setIndexNames(
    (0, "TIMETRA-NAT-MIB", "tmnxNatMapDomName"),
    (0, "TIMETRA-NAT-MIB", "tmnxNatMapRuleName"),
    (0, "TIMETRA-NAT-MIB", "tmnxMapTVappEsaNum"),
    (0, "TIMETRA-NAT-MIB", "tmnxMapTVappEsaVappNum"),
)
if mibBuilder.loadTexts:
    tmnxMapTRuleVappStatsEntry.setStatus("current")
_TmnxMapTRuleVappUpFwdPackets_Type = Counter64
_TmnxMapTRuleVappUpFwdPackets_Object = MibTableColumn
tmnxMapTRuleVappUpFwdPackets = _TmnxMapTRuleVappUpFwdPackets_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 16, 24, 1, 1),
    _TmnxMapTRuleVappUpFwdPackets_Type()
)
tmnxMapTRuleVappUpFwdPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMapTRuleVappUpFwdPackets.setStatus("current")
_TmnxMapTRuleVappUpFwdOctets_Type = Counter64
_TmnxMapTRuleVappUpFwdOctets_Object = MibTableColumn
tmnxMapTRuleVappUpFwdOctets = _TmnxMapTRuleVappUpFwdOctets_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 16, 24, 1, 2),
    _TmnxMapTRuleVappUpFwdOctets_Type()
)
tmnxMapTRuleVappUpFwdOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMapTRuleVappUpFwdOctets.setStatus("current")
_TmnxMapTRuleVappUpDropPackets_Type = Counter64
_TmnxMapTRuleVappUpDropPackets_Object = MibTableColumn
tmnxMapTRuleVappUpDropPackets = _TmnxMapTRuleVappUpDropPackets_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 16, 24, 1, 3),
    _TmnxMapTRuleVappUpDropPackets_Type()
)
tmnxMapTRuleVappUpDropPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMapTRuleVappUpDropPackets.setStatus("current")
_TmnxMapTRuleVappUpDropOctets_Type = Counter64
_TmnxMapTRuleVappUpDropOctets_Object = MibTableColumn
tmnxMapTRuleVappUpDropOctets = _TmnxMapTRuleVappUpDropOctets_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 16, 24, 1, 4),
    _TmnxMapTRuleVappUpDropOctets_Type()
)
tmnxMapTRuleVappUpDropOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMapTRuleVappUpDropOctets.setStatus("current")
_TmnxMapTRuleVappUpDropAntiSpoof_Type = Counter64
_TmnxMapTRuleVappUpDropAntiSpoof_Object = MibTableColumn
tmnxMapTRuleVappUpDropAntiSpoof = _TmnxMapTRuleVappUpDropAntiSpoof_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 16, 24, 1, 5),
    _TmnxMapTRuleVappUpDropAntiSpoof_Type()
)
tmnxMapTRuleVappUpDropAntiSpoof.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMapTRuleVappUpDropAntiSpoof.setStatus("current")
_TmnxMapTRuleVappUpDropIcmp6_Type = Counter64
_TmnxMapTRuleVappUpDropIcmp6_Object = MibTableColumn
tmnxMapTRuleVappUpDropIcmp6 = _TmnxMapTRuleVappUpDropIcmp6_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 16, 24, 1, 6),
    _TmnxMapTRuleVappUpDropIcmp6_Type()
)
tmnxMapTRuleVappUpDropIcmp6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMapTRuleVappUpDropIcmp6.setStatus("current")
_TmnxMapTRuleVappUpDropUnkProto_Type = Counter64
_TmnxMapTRuleVappUpDropUnkProto_Object = MibTableColumn
tmnxMapTRuleVappUpDropUnkProto = _TmnxMapTRuleVappUpDropUnkProto_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 16, 24, 1, 7),
    _TmnxMapTRuleVappUpDropUnkProto_Type()
)
tmnxMapTRuleVappUpDropUnkProto.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMapTRuleVappUpDropUnkProto.setStatus("current")
_TmnxMapTRuleVappUpFragRx_Type = Counter64
_TmnxMapTRuleVappUpFragRx_Object = MibTableColumn
tmnxMapTRuleVappUpFragRx = _TmnxMapTRuleVappUpFragRx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 16, 24, 1, 9),
    _TmnxMapTRuleVappUpFragRx_Type()
)
tmnxMapTRuleVappUpFragRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMapTRuleVappUpFragRx.setStatus("current")
_TmnxMapTRuleVappUpIcmp6EchoRx_Type = Counter64
_TmnxMapTRuleVappUpIcmp6EchoRx_Object = MibTableColumn
tmnxMapTRuleVappUpIcmp6EchoRx = _TmnxMapTRuleVappUpIcmp6EchoRx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 16, 24, 1, 10),
    _TmnxMapTRuleVappUpIcmp6EchoRx_Type()
)
tmnxMapTRuleVappUpIcmp6EchoRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMapTRuleVappUpIcmp6EchoRx.setStatus("current")
_TmnxMapTRuleVappUpCpeIcmp6ErrRx_Type = Counter64
_TmnxMapTRuleVappUpCpeIcmp6ErrRx_Object = MibTableColumn
tmnxMapTRuleVappUpCpeIcmp6ErrRx = _TmnxMapTRuleVappUpCpeIcmp6ErrRx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 16, 24, 1, 12),
    _TmnxMapTRuleVappUpCpeIcmp6ErrRx_Type()
)
tmnxMapTRuleVappUpCpeIcmp6ErrRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMapTRuleVappUpCpeIcmp6ErrRx.setStatus("current")
_TmnxMapTRuleVappUpImIcmp6ErrRx_Type = Counter64
_TmnxMapTRuleVappUpImIcmp6ErrRx_Object = MibTableColumn
tmnxMapTRuleVappUpImIcmp6ErrRx = _TmnxMapTRuleVappUpImIcmp6ErrRx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 16, 24, 1, 13),
    _TmnxMapTRuleVappUpImIcmp6ErrRx_Type()
)
tmnxMapTRuleVappUpImIcmp6ErrRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMapTRuleVappUpImIcmp6ErrRx.setStatus("current")
_TmnxMapTRuleVappDownFwdPackets_Type = Counter64
_TmnxMapTRuleVappDownFwdPackets_Object = MibTableColumn
tmnxMapTRuleVappDownFwdPackets = _TmnxMapTRuleVappDownFwdPackets_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 16, 24, 1, 14),
    _TmnxMapTRuleVappDownFwdPackets_Type()
)
tmnxMapTRuleVappDownFwdPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMapTRuleVappDownFwdPackets.setStatus("current")
_TmnxMapTRuleVappDownFwdOctets_Type = Counter64
_TmnxMapTRuleVappDownFwdOctets_Object = MibTableColumn
tmnxMapTRuleVappDownFwdOctets = _TmnxMapTRuleVappDownFwdOctets_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 16, 24, 1, 15),
    _TmnxMapTRuleVappDownFwdOctets_Type()
)
tmnxMapTRuleVappDownFwdOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMapTRuleVappDownFwdOctets.setStatus("current")
_TmnxMapTRuleVappDownDropPackets_Type = Counter64
_TmnxMapTRuleVappDownDropPackets_Object = MibTableColumn
tmnxMapTRuleVappDownDropPackets = _TmnxMapTRuleVappDownDropPackets_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 16, 24, 1, 16),
    _TmnxMapTRuleVappDownDropPackets_Type()
)
tmnxMapTRuleVappDownDropPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMapTRuleVappDownDropPackets.setStatus("current")
_TmnxMapTRuleVappDownDropOctets_Type = Counter64
_TmnxMapTRuleVappDownDropOctets_Object = MibTableColumn
tmnxMapTRuleVappDownDropOctets = _TmnxMapTRuleVappDownDropOctets_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 16, 24, 1, 17),
    _TmnxMapTRuleVappDownDropOctets_Type()
)
tmnxMapTRuleVappDownDropOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMapTRuleVappDownDropOctets.setStatus("current")
_TmnxMapTRuleVappDownDropFragRx_Type = Counter64
_TmnxMapTRuleVappDownDropFragRx_Object = MibTableColumn
tmnxMapTRuleVappDownDropFragRx = _TmnxMapTRuleVappDownDropFragRx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 16, 24, 1, 18),
    _TmnxMapTRuleVappDownDropFragRx_Type()
)
tmnxMapTRuleVappDownDropFragRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMapTRuleVappDownDropFragRx.setStatus("current")
_TmnxMapTRuleVappDownDropFragReq_Type = Counter64
_TmnxMapTRuleVappDownDropFragReq_Object = MibTableColumn
tmnxMapTRuleVappDownDropFragReq = _TmnxMapTRuleVappDownDropFragReq_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 16, 24, 1, 19),
    _TmnxMapTRuleVappDownDropFragReq_Type()
)
tmnxMapTRuleVappDownDropFragReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMapTRuleVappDownDropFragReq.setStatus("current")
_TmnxMapTRuleVappDownDropIcmp4_Type = Counter64
_TmnxMapTRuleVappDownDropIcmp4_Object = MibTableColumn
tmnxMapTRuleVappDownDropIcmp4 = _TmnxMapTRuleVappDownDropIcmp4_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 16, 24, 1, 20),
    _TmnxMapTRuleVappDownDropIcmp4_Type()
)
tmnxMapTRuleVappDownDropIcmp4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMapTRuleVappDownDropIcmp4.setStatus("current")
_TmnxMapTRuleVappDownDropUnkProto_Type = Counter64
_TmnxMapTRuleVappDownDropUnkProto_Object = MibTableColumn
tmnxMapTRuleVappDownDropUnkProto = _TmnxMapTRuleVappDownDropUnkProto_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 16, 24, 1, 21),
    _TmnxMapTRuleVappDownDropUnkProto_Type()
)
tmnxMapTRuleVappDownDropUnkProto.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMapTRuleVappDownDropUnkProto.setStatus("current")
_TmnxMapTRuleVappDownFragRx_Type = Counter64
_TmnxMapTRuleVappDownFragRx_Object = MibTableColumn
tmnxMapTRuleVappDownFragRx = _TmnxMapTRuleVappDownFragRx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 16, 24, 1, 22),
    _TmnxMapTRuleVappDownFragRx_Type()
)
tmnxMapTRuleVappDownFragRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMapTRuleVappDownFragRx.setStatus("current")
_TmnxMapTRuleVappDownFragReq_Type = Counter64
_TmnxMapTRuleVappDownFragReq_Object = MibTableColumn
tmnxMapTRuleVappDownFragReq = _TmnxMapTRuleVappDownFragReq_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 16, 24, 1, 23),
    _TmnxMapTRuleVappDownFragReq_Type()
)
tmnxMapTRuleVappDownFragReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMapTRuleVappDownFragReq.setStatus("current")
_TmnxMapTRuleVappDownIcmp4EchoRx_Type = Counter64
_TmnxMapTRuleVappDownIcmp4EchoRx_Object = MibTableColumn
tmnxMapTRuleVappDownIcmp4EchoRx = _TmnxMapTRuleVappDownIcmp4EchoRx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 16, 24, 1, 24),
    _TmnxMapTRuleVappDownIcmp4EchoRx_Type()
)
tmnxMapTRuleVappDownIcmp4EchoRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMapTRuleVappDownIcmp4EchoRx.setStatus("current")
_TmnxMapTRuleVappDnIcmp4ErrRepRx_Type = Counter64
_TmnxMapTRuleVappDnIcmp4ErrRepRx_Object = MibTableColumn
tmnxMapTRuleVappDnIcmp4ErrRepRx = _TmnxMapTRuleVappDnIcmp4ErrRepRx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 16, 24, 1, 25),
    _TmnxMapTRuleVappDnIcmp4ErrRepRx_Type()
)
tmnxMapTRuleVappDnIcmp4ErrRepRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMapTRuleVappDnIcmp4ErrRepRx.setStatus("current")
_TmnxMapTRuleVappIcmp4ErrFragDf_Type = Counter64
_TmnxMapTRuleVappIcmp4ErrFragDf_Object = MibTableColumn
tmnxMapTRuleVappIcmp4ErrFragDf = _TmnxMapTRuleVappIcmp4ErrFragDf_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 16, 24, 1, 26),
    _TmnxMapTRuleVappIcmp4ErrFragDf_Type()
)
tmnxMapTRuleVappIcmp4ErrFragDf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMapTRuleVappIcmp4ErrFragDf.setStatus("current")
_TmnxMapTRuleVappDownUdpRecalc_Type = Counter64
_TmnxMapTRuleVappDownUdpRecalc_Object = MibTableColumn
tmnxMapTRuleVappDownUdpRecalc = _TmnxMapTRuleVappDownUdpRecalc_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 16, 24, 1, 27),
    _TmnxMapTRuleVappDownUdpRecalc_Type()
)
tmnxMapTRuleVappDownUdpRecalc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMapTRuleVappDownUdpRecalc.setStatus("current")
_TmnxMapTDomVappFragStatsTable_Object = MibTable
tmnxMapTDomVappFragStatsTable = _TmnxMapTDomVappFragStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 16, 25)
)
if mibBuilder.loadTexts:
    tmnxMapTDomVappFragStatsTable.setStatus("current")
_TmnxMapTDomVappFragStatsEntry_Object = MibTableRow
tmnxMapTDomVappFragStatsEntry = _TmnxMapTDomVappFragStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 16, 25, 1)
)
tmnxMapTDomVappFragStatsEntry.setIndexNames(
    (0, "TIMETRA-NAT-MIB", "tmnxNatMapDomName"),
    (0, "TIMETRA-NAT-MIB", "tmnxMapTVappEsaNum"),
    (0, "TIMETRA-NAT-MIB", "tmnxMapTVappEsaVappNum"),
)
if mibBuilder.loadTexts:
    tmnxMapTDomVappFragStatsEntry.setStatus("current")
_TmnxMapTDomVFragRxResolvedFrag_Type = Counter64
_TmnxMapTDomVFragRxResolvedFrag_Object = MibTableColumn
tmnxMapTDomVFragRxResolvedFrag = _TmnxMapTDomVFragRxResolvedFrag_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 16, 25, 1, 1),
    _TmnxMapTDomVFragRxResolvedFrag_Type()
)
tmnxMapTDomVFragRxResolvedFrag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMapTDomVFragRxResolvedFrag.setStatus("current")
_TmnxMapTDomVFragRxUnresolvedFrag_Type = Counter64
_TmnxMapTDomVFragRxUnresolvedFrag_Object = MibTableColumn
tmnxMapTDomVFragRxUnresolvedFrag = _TmnxMapTDomVFragRxUnresolvedFrag_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 16, 25, 1, 2),
    _TmnxMapTDomVFragRxUnresolvedFrag_Type()
)
tmnxMapTDomVFragRxUnresolvedFrag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMapTDomVFragRxUnresolvedFrag.setStatus("current")
_TmnxMapTDomVFragTxFrag_Type = Counter64
_TmnxMapTDomVFragTxFrag_Object = MibTableColumn
tmnxMapTDomVFragTxFrag = _TmnxMapTDomVFragTxFrag_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 16, 25, 1, 3),
    _TmnxMapTDomVFragTxFrag_Type()
)
tmnxMapTDomVFragTxFrag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMapTDomVFragTxFrag.setStatus("current")
_TmnxMapTDomVFragDropFTimeout_Type = Counter64
_TmnxMapTDomVFragDropFTimeout_Object = MibTableColumn
tmnxMapTDomVFragDropFTimeout = _TmnxMapTDomVFragDropFTimeout_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 16, 25, 1, 4),
    _TmnxMapTDomVFragDropFTimeout_Type()
)
tmnxMapTDomVFragDropFTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMapTDomVFragDropFTimeout.setStatus("current")
_TmnxMapTDomVFragDropBufExhaust_Type = Counter64
_TmnxMapTDomVFragDropBufExhaust_Object = MibTableColumn
tmnxMapTDomVFragDropBufExhaust = _TmnxMapTDomVFragDropBufExhaust_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 16, 25, 1, 5),
    _TmnxMapTDomVFragDropBufExhaust_Type()
)
tmnxMapTDomVFragDropBufExhaust.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMapTDomVFragDropBufExhaust.setStatus("current")
_TmnxMapTDomVFragDropTooManyFrag_Type = Counter64
_TmnxMapTDomVFragDropTooManyFrag_Object = MibTableColumn
tmnxMapTDomVFragDropTooManyFrag = _TmnxMapTDomVFragDropTooManyFrag_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 16, 25, 1, 6),
    _TmnxMapTDomVFragDropTooManyFrag_Type()
)
tmnxMapTDomVFragDropTooManyFrag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMapTDomVFragDropTooManyFrag.setStatus("current")
_TmnxMapTDomVFragDropTooManyLists_Type = Counter64
_TmnxMapTDomVFragDropTooManyLists_Object = MibTableColumn
tmnxMapTDomVFragDropTooManyLists = _TmnxMapTDomVFragDropTooManyLists_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 16, 25, 1, 7),
    _TmnxMapTDomVFragDropTooManyLists_Type()
)
tmnxMapTDomVFragDropTooManyLists.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMapTDomVFragDropTooManyLists.setStatus("current")
_TmnxMapTDomVFragDropFragLists_Type = Counter64
_TmnxMapTDomVFragDropFragLists_Object = MibTableColumn
tmnxMapTDomVFragDropFragLists = _TmnxMapTDomVFragDropFragLists_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 16, 25, 1, 8),
    _TmnxMapTDomVFragDropFragLists_Type()
)
tmnxMapTDomVFragDropFragLists.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMapTDomVFragDropFragLists.setStatus("current")
_TmnxMapTDomVFragOverlappingFirst_Type = Counter64
_TmnxMapTDomVFragOverlappingFirst_Object = MibTableColumn
tmnxMapTDomVFragOverlappingFirst = _TmnxMapTDomVFragOverlappingFirst_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 16, 25, 1, 9),
    _TmnxMapTDomVFragOverlappingFirst_Type()
)
tmnxMapTDomVFragOverlappingFirst.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMapTDomVFragOverlappingFirst.setStatus("current")
_TmnxMapTDomVappFragListTable_Object = MibTable
tmnxMapTDomVappFragListTable = _TmnxMapTDomVappFragListTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 16, 26)
)
if mibBuilder.loadTexts:
    tmnxMapTDomVappFragListTable.setStatus("current")
_TmnxMapTDomVappFragListEntry_Object = MibTableRow
tmnxMapTDomVappFragListEntry = _TmnxMapTDomVappFragListEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 16, 26, 1)
)
tmnxMapTDomVappFragListEntry.setIndexNames(
    (0, "TIMETRA-NAT-MIB", "tmnxNatMapDomName"),
    (0, "TIMETRA-NAT-MIB", "tmnxMapTVappEsaNum"),
    (0, "TIMETRA-NAT-MIB", "tmnxMapTVappEsaVappNum"),
    (0, "TIMETRA-NAT-MIB", "tmnxMapTVappFragListId"),
)
if mibBuilder.loadTexts:
    tmnxMapTDomVappFragListEntry.setStatus("current")


class _TmnxMapTVappFragListId_Type(Unsigned32):
    """Custom type tmnxMapTVappFragListId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 20),
    )


_TmnxMapTVappFragListId_Type.__name__ = "Unsigned32"
_TmnxMapTVappFragListId_Object = MibTableColumn
tmnxMapTVappFragListId = _TmnxMapTVappFragListId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 16, 26, 1, 1),
    _TmnxMapTVappFragListId_Type()
)
tmnxMapTVappFragListId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxMapTVappFragListId.setStatus("current")
_TmnxMapTDomVFragListResolvedFrag_Type = Counter64
_TmnxMapTDomVFragListResolvedFrag_Object = MibTableColumn
tmnxMapTDomVFragListResolvedFrag = _TmnxMapTDomVFragListResolvedFrag_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 16, 26, 1, 2),
    _TmnxMapTDomVFragListResolvedFrag_Type()
)
tmnxMapTDomVFragListResolvedFrag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMapTDomVFragListResolvedFrag.setStatus("current")
_TmnxMapTDomVFragListDroppedFrag_Type = Counter64
_TmnxMapTDomVFragListDroppedFrag_Object = MibTableColumn
tmnxMapTDomVFragListDroppedFrag = _TmnxMapTDomVFragListDroppedFrag_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 16, 26, 1, 3),
    _TmnxMapTDomVFragListDroppedFrag_Type()
)
tmnxMapTDomVFragListDroppedFrag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMapTDomVFragListDroppedFrag.setStatus("current")
_TmnxNatMapDomFPStatsTable_Object = MibTable
tmnxNatMapDomFPStatsTable = _TmnxNatMapDomFPStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 16, 27)
)
if mibBuilder.loadTexts:
    tmnxNatMapDomFPStatsTable.setStatus("current")
_TmnxNatMapDomFPStatsEntry_Object = MibTableRow
tmnxNatMapDomFPStatsEntry = _TmnxNatMapDomFPStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 16, 27, 1)
)
if mibBuilder.loadTexts:
    tmnxNatMapDomFPStatsEntry.setStatus("current")
_TmnxNatMapDomFPUpFwdPackets_Type = Counter64
_TmnxNatMapDomFPUpFwdPackets_Object = MibTableColumn
tmnxNatMapDomFPUpFwdPackets = _TmnxNatMapDomFPUpFwdPackets_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 16, 27, 1, 1),
    _TmnxNatMapDomFPUpFwdPackets_Type()
)
tmnxNatMapDomFPUpFwdPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatMapDomFPUpFwdPackets.setStatus("current")
_TmnxNatMapDomFPUpFwdOctets_Type = Counter64
_TmnxNatMapDomFPUpFwdOctets_Object = MibTableColumn
tmnxNatMapDomFPUpFwdOctets = _TmnxNatMapDomFPUpFwdOctets_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 16, 27, 1, 2),
    _TmnxNatMapDomFPUpFwdOctets_Type()
)
tmnxNatMapDomFPUpFwdOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatMapDomFPUpFwdOctets.setStatus("current")
_TmnxNatMapDomFPUpDropAnchorIf_Type = Counter64
_TmnxNatMapDomFPUpDropAnchorIf_Object = MibTableColumn
tmnxNatMapDomFPUpDropAnchorIf = _TmnxNatMapDomFPUpDropAnchorIf_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 16, 27, 1, 3),
    _TmnxNatMapDomFPUpDropAnchorIf_Type()
)
tmnxNatMapDomFPUpDropAnchorIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatMapDomFPUpDropAnchorIf.setStatus("current")
_TmnxNatMapDomFPUpDropAntiSpoof_Type = Counter64
_TmnxNatMapDomFPUpDropAntiSpoof_Object = MibTableColumn
tmnxNatMapDomFPUpDropAntiSpoof = _TmnxNatMapDomFPUpDropAntiSpoof_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 16, 27, 1, 4),
    _TmnxNatMapDomFPUpDropAntiSpoof_Type()
)
tmnxNatMapDomFPUpDropAntiSpoof.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatMapDomFPUpDropAntiSpoof.setStatus("current")
_TmnxNatMapDomFPUpDropUnkProto_Type = Counter64
_TmnxNatMapDomFPUpDropUnkProto_Object = MibTableColumn
tmnxNatMapDomFPUpDropUnkProto = _TmnxNatMapDomFPUpDropUnkProto_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 16, 27, 1, 5),
    _TmnxNatMapDomFPUpDropUnkProto_Type()
)
tmnxNatMapDomFPUpDropUnkProto.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatMapDomFPUpDropUnkProto.setStatus("current")
_TmnxNatMapDomFPDownFwdPackets_Type = Counter64
_TmnxNatMapDomFPDownFwdPackets_Object = MibTableColumn
tmnxNatMapDomFPDownFwdPackets = _TmnxNatMapDomFPDownFwdPackets_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 16, 27, 1, 6),
    _TmnxNatMapDomFPDownFwdPackets_Type()
)
tmnxNatMapDomFPDownFwdPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatMapDomFPDownFwdPackets.setStatus("current")
_TmnxNatMapDomFPDownFwdOctets_Type = Counter64
_TmnxNatMapDomFPDownFwdOctets_Object = MibTableColumn
tmnxNatMapDomFPDownFwdOctets = _TmnxNatMapDomFPDownFwdOctets_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 16, 27, 1, 7),
    _TmnxNatMapDomFPDownFwdOctets_Type()
)
tmnxNatMapDomFPDownFwdOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatMapDomFPDownFwdOctets.setStatus("current")
_TmnxNatMapDomFPDownDropAnchorIf_Type = Counter64
_TmnxNatMapDomFPDownDropAnchorIf_Object = MibTableColumn
tmnxNatMapDomFPDownDropAnchorIf = _TmnxNatMapDomFPDownDropAnchorIf_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 16, 27, 1, 8),
    _TmnxNatMapDomFPDownDropAnchorIf_Type()
)
tmnxNatMapDomFPDownDropAnchorIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatMapDomFPDownDropAnchorIf.setStatus("current")
_TmnxNatMapDomFPDownDropUnkPro_Type = Counter64
_TmnxNatMapDomFPDownDropUnkPro_Object = MibTableColumn
tmnxNatMapDomFPDownDropUnkPro = _TmnxNatMapDomFPDownDropUnkPro_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 16, 27, 1, 9),
    _TmnxNatMapDomFPDownDropUnkPro_Type()
)
tmnxNatMapDomFPDownDropUnkPro.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatMapDomFPDownDropUnkPro.setStatus("current")
_TmnxNatMapRuleFPStatsTable_Object = MibTable
tmnxNatMapRuleFPStatsTable = _TmnxNatMapRuleFPStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 16, 28)
)
if mibBuilder.loadTexts:
    tmnxNatMapRuleFPStatsTable.setStatus("current")
_TmnxNatMapRuleFPStatsEntry_Object = MibTableRow
tmnxNatMapRuleFPStatsEntry = _TmnxNatMapRuleFPStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 16, 28, 1)
)
if mibBuilder.loadTexts:
    tmnxNatMapRuleFPStatsEntry.setStatus("current")
_TmnxNatMapRuleFPUpFwdPackets_Type = Counter64
_TmnxNatMapRuleFPUpFwdPackets_Object = MibTableColumn
tmnxNatMapRuleFPUpFwdPackets = _TmnxNatMapRuleFPUpFwdPackets_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 16, 28, 1, 1),
    _TmnxNatMapRuleFPUpFwdPackets_Type()
)
tmnxNatMapRuleFPUpFwdPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatMapRuleFPUpFwdPackets.setStatus("current")
_TmnxNatMapRuleFPUpFwdOctets_Type = Counter64
_TmnxNatMapRuleFPUpFwdOctets_Object = MibTableColumn
tmnxNatMapRuleFPUpFwdOctets = _TmnxNatMapRuleFPUpFwdOctets_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 16, 28, 1, 2),
    _TmnxNatMapRuleFPUpFwdOctets_Type()
)
tmnxNatMapRuleFPUpFwdOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatMapRuleFPUpFwdOctets.setStatus("current")
_TmnxNatMapRuleFPUpDropAntiSpoof_Type = Counter64
_TmnxNatMapRuleFPUpDropAntiSpoof_Object = MibTableColumn
tmnxNatMapRuleFPUpDropAntiSpoof = _TmnxNatMapRuleFPUpDropAntiSpoof_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 16, 28, 1, 3),
    _TmnxNatMapRuleFPUpDropAntiSpoof_Type()
)
tmnxNatMapRuleFPUpDropAntiSpoof.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatMapRuleFPUpDropAntiSpoof.setStatus("current")
_TmnxNatMapRuleFPDownFwdPackets_Type = Counter64
_TmnxNatMapRuleFPDownFwdPackets_Object = MibTableColumn
tmnxNatMapRuleFPDownFwdPackets = _TmnxNatMapRuleFPDownFwdPackets_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 16, 28, 1, 4),
    _TmnxNatMapRuleFPDownFwdPackets_Type()
)
tmnxNatMapRuleFPDownFwdPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatMapRuleFPDownFwdPackets.setStatus("current")
_TmnxNatMapRuleFPDownFwdOctets_Type = Counter64
_TmnxNatMapRuleFPDownFwdOctets_Object = MibTableColumn
tmnxNatMapRuleFPDownFwdOctets = _TmnxNatMapRuleFPDownFwdOctets_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 16, 28, 1, 5),
    _TmnxNatMapRuleFPDownFwdOctets_Type()
)
tmnxNatMapRuleFPDownFwdOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatMapRuleFPDownFwdOctets.setStatus("current")
_TmnxNatFirewallObjs_ObjectIdentity = ObjectIdentity
tmnxNatFirewallObjs = _TmnxNatFirewallObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 17)
)
_TmnxNatFwlPlcyTable_Object = MibTable
tmnxNatFwlPlcyTable = _TmnxNatFwlPlcyTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 17, 1)
)
if mibBuilder.loadTexts:
    tmnxNatFwlPlcyTable.setStatus("current")
_TmnxNatFwlPlcyEntry_Object = MibTableRow
tmnxNatFwlPlcyEntry = _TmnxNatFwlPlcyEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 17, 1, 1)
)
tmnxNatFwlPlcyEntry.setIndexNames(
    (1, "TIMETRA-NAT-MIB", "tmnxNatFwlPlcyName"),
)
if mibBuilder.loadTexts:
    tmnxNatFwlPlcyEntry.setStatus("current")
_TmnxNatFwlPlcyName_Type = TNamedItem
_TmnxNatFwlPlcyName_Object = MibTableColumn
tmnxNatFwlPlcyName = _TmnxNatFwlPlcyName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 17, 1, 1, 1),
    _TmnxNatFwlPlcyName_Type()
)
tmnxNatFwlPlcyName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxNatFwlPlcyName.setStatus("current")
_TmnxNatFwlPlcyRowStatus_Type = RowStatus
_TmnxNatFwlPlcyRowStatus_Object = MibTableColumn
tmnxNatFwlPlcyRowStatus = _TmnxNatFwlPlcyRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 17, 1, 1, 2),
    _TmnxNatFwlPlcyRowStatus_Type()
)
tmnxNatFwlPlcyRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxNatFwlPlcyRowStatus.setStatus("current")


class _TmnxNatFwlPlcyDomainRouter_Type(TmnxVRtrIDOrZero):
    """Custom type tmnxNatFwlPlcyDomainRouter based on TmnxVRtrIDOrZero"""
    defaultValue = 0


_TmnxNatFwlPlcyDomainRouter_Type.__name__ = "TmnxVRtrIDOrZero"
_TmnxNatFwlPlcyDomainRouter_Object = MibTableColumn
tmnxNatFwlPlcyDomainRouter = _TmnxNatFwlPlcyDomainRouter_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 17, 1, 1, 7),
    _TmnxNatFwlPlcyDomainRouter_Type()
)
tmnxNatFwlPlcyDomainRouter.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxNatFwlPlcyDomainRouter.setStatus("current")


class _TmnxNatFwlPlcyDomainName_Type(TNamedItemOrEmpty):
    """Custom type tmnxNatFwlPlcyDomainName based on TNamedItemOrEmpty"""
    defaultValue = OctetString("")


_TmnxNatFwlPlcyDomainName_Type.__name__ = "TNamedItemOrEmpty"
_TmnxNatFwlPlcyDomainName_Object = MibTableColumn
tmnxNatFwlPlcyDomainName = _TmnxNatFwlPlcyDomainName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 17, 1, 1, 8),
    _TmnxNatFwlPlcyDomainName_Type()
)
tmnxNatFwlPlcyDomainName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxNatFwlPlcyDomainName.setStatus("current")
_TmnxNatPolicyTable_Object = MibTable
tmnxNatPolicyTable = _TmnxNatPolicyTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 17, 2)
)
if mibBuilder.loadTexts:
    tmnxNatPolicyTable.setStatus("current")
_TmnxNatPolicyEntry_Object = MibTableRow
tmnxNatPolicyEntry = _TmnxNatPolicyEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 17, 2, 1)
)
tmnxNatPolicyEntry.setIndexNames(
    (1, "TIMETRA-NAT-MIB", "tmnxNatPolicyName"),
)
if mibBuilder.loadTexts:
    tmnxNatPolicyEntry.setStatus("current")
_TmnxNatPolicyName_Type = TNamedItem
_TmnxNatPolicyName_Object = MibTableColumn
tmnxNatPolicyName = _TmnxNatPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 17, 2, 1, 1),
    _TmnxNatPolicyName_Type()
)
tmnxNatPolicyName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxNatPolicyName.setStatus("current")
_TmnxNatPolicyRowStatus_Type = RowStatus
_TmnxNatPolicyRowStatus_Object = MibTableColumn
tmnxNatPolicyRowStatus = _TmnxNatPolicyRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 17, 2, 1, 2),
    _TmnxNatPolicyRowStatus_Type()
)
tmnxNatPolicyRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxNatPolicyRowStatus.setStatus("current")
_TmnxNatFwlDomTable_Object = MibTable
tmnxNatFwlDomTable = _TmnxNatFwlDomTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 17, 3)
)
if mibBuilder.loadTexts:
    tmnxNatFwlDomTable.setStatus("current")
_TmnxNatFwlDomEntry_Object = MibTableRow
tmnxNatFwlDomEntry = _TmnxNatFwlDomEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 17, 3, 1)
)
tmnxNatFwlDomEntry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (1, "TIMETRA-NAT-MIB", "tmnxNatFwlDomName"),
)
if mibBuilder.loadTexts:
    tmnxNatFwlDomEntry.setStatus("current")
_TmnxNatFwlDomName_Type = TNamedItem
_TmnxNatFwlDomName_Object = MibTableColumn
tmnxNatFwlDomName = _TmnxNatFwlDomName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 17, 3, 1, 1),
    _TmnxNatFwlDomName_Type()
)
tmnxNatFwlDomName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxNatFwlDomName.setStatus("current")
_TmnxNatFwlDomRowStatus_Type = RowStatus
_TmnxNatFwlDomRowStatus_Object = MibTableColumn
tmnxNatFwlDomRowStatus = _TmnxNatFwlDomRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 17, 3, 1, 2),
    _TmnxNatFwlDomRowStatus_Type()
)
tmnxNatFwlDomRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxNatFwlDomRowStatus.setStatus("current")
_TmnxNatFwlDomLastMgmtChange_Type = TimeStamp
_TmnxNatFwlDomLastMgmtChange_Object = MibTableColumn
tmnxNatFwlDomLastMgmtChange = _TmnxNatFwlDomLastMgmtChange_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 17, 3, 1, 3),
    _TmnxNatFwlDomLastMgmtChange_Type()
)
tmnxNatFwlDomLastMgmtChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatFwlDomLastMgmtChange.setStatus("current")
_TmnxNatFwlDomIsaGrp_Type = TmnxNatIsaGrpId
_TmnxNatFwlDomIsaGrp_Object = MibTableColumn
tmnxNatFwlDomIsaGrp = _TmnxNatFwlDomIsaGrp_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 17, 3, 1, 4),
    _TmnxNatFwlDomIsaGrp_Type()
)
tmnxNatFwlDomIsaGrp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxNatFwlDomIsaGrp.setStatus("current")


class _TmnxNatFwlDomAdminState_Type(TmnxAdminState):
    """Custom type tmnxNatFwlDomAdminState based on TmnxAdminState"""
    defaultValue = 3


_TmnxNatFwlDomAdminState_Type.__name__ = "TmnxAdminState"
_TmnxNatFwlDomAdminState_Object = MibTableColumn
tmnxNatFwlDomAdminState = _TmnxNatFwlDomAdminState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 17, 3, 1, 5),
    _TmnxNatFwlDomAdminState_Type()
)
tmnxNatFwlDomAdminState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxNatFwlDomAdminState.setStatus("current")


class _TmnxNatFwlDomDhcp6ServerRouter_Type(TmnxVRtrIDOrZero):
    """Custom type tmnxNatFwlDomDhcp6ServerRouter based on TmnxVRtrIDOrZero"""
    defaultValue = 0


_TmnxNatFwlDomDhcp6ServerRouter_Type.__name__ = "TmnxVRtrIDOrZero"
_TmnxNatFwlDomDhcp6ServerRouter_Object = MibTableColumn
tmnxNatFwlDomDhcp6ServerRouter = _TmnxNatFwlDomDhcp6ServerRouter_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 17, 3, 1, 7),
    _TmnxNatFwlDomDhcp6ServerRouter_Type()
)
tmnxNatFwlDomDhcp6ServerRouter.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxNatFwlDomDhcp6ServerRouter.setStatus("current")


class _TmnxNatFwlDomDhcp6ServerName_Type(TNamedItemOrEmpty):
    """Custom type tmnxNatFwlDomDhcp6ServerName based on TNamedItemOrEmpty"""
    defaultValue = OctetString("")


_TmnxNatFwlDomDhcp6ServerName_Type.__name__ = "TNamedItemOrEmpty"
_TmnxNatFwlDomDhcp6ServerName_Object = MibTableColumn
tmnxNatFwlDomDhcp6ServerName = _TmnxNatFwlDomDhcp6ServerName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 17, 3, 1, 8),
    _TmnxNatFwlDomDhcp6ServerName_Type()
)
tmnxNatFwlDomDhcp6ServerName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxNatFwlDomDhcp6ServerName.setStatus("current")
_TmnxNatFwlDomPrefixTable_Object = MibTable
tmnxNatFwlDomPrefixTable = _TmnxNatFwlDomPrefixTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 17, 4)
)
if mibBuilder.loadTexts:
    tmnxNatFwlDomPrefixTable.setStatus("current")
_TmnxNatFwlDomPrefixEntry_Object = MibTableRow
tmnxNatFwlDomPrefixEntry = _TmnxNatFwlDomPrefixEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 17, 4, 1)
)
tmnxNatFwlDomPrefixEntry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "TIMETRA-NAT-MIB", "tmnxNatFwlDomName"),
    (0, "TIMETRA-NAT-MIB", "tmnxNatFwlDomPrefixAddrType"),
    (0, "TIMETRA-NAT-MIB", "tmnxNatFwlDomPrefix"),
    (0, "TIMETRA-NAT-MIB", "tmnxNatFwlDomPrefixLength"),
)
if mibBuilder.loadTexts:
    tmnxNatFwlDomPrefixEntry.setStatus("current")
_TmnxNatFwlDomPrefixAddrType_Type = InetAddressType
_TmnxNatFwlDomPrefixAddrType_Object = MibTableColumn
tmnxNatFwlDomPrefixAddrType = _TmnxNatFwlDomPrefixAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 17, 4, 1, 1),
    _TmnxNatFwlDomPrefixAddrType_Type()
)
tmnxNatFwlDomPrefixAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxNatFwlDomPrefixAddrType.setStatus("current")


class _TmnxNatFwlDomPrefix_Type(InetAddress):
    """Custom type tmnxNatFwlDomPrefix based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(16, 16),
    )


_TmnxNatFwlDomPrefix_Type.__name__ = "InetAddress"
_TmnxNatFwlDomPrefix_Object = MibTableColumn
tmnxNatFwlDomPrefix = _TmnxNatFwlDomPrefix_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 17, 4, 1, 2),
    _TmnxNatFwlDomPrefix_Type()
)
tmnxNatFwlDomPrefix.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxNatFwlDomPrefix.setStatus("current")


class _TmnxNatFwlDomPrefixLength_Type(InetAddressPrefixLength):
    """Custom type tmnxNatFwlDomPrefixLength based on InetAddressPrefixLength"""
    subtypeSpec = InetAddressPrefixLength.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(32, 64),
    )


_TmnxNatFwlDomPrefixLength_Type.__name__ = "InetAddressPrefixLength"
_TmnxNatFwlDomPrefixLength_Object = MibTableColumn
tmnxNatFwlDomPrefixLength = _TmnxNatFwlDomPrefixLength_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 17, 4, 1, 3),
    _TmnxNatFwlDomPrefixLength_Type()
)
tmnxNatFwlDomPrefixLength.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxNatFwlDomPrefixLength.setStatus("current")
_TmnxNatFwlDomPrefixRowStatus_Type = RowStatus
_TmnxNatFwlDomPrefixRowStatus_Object = MibTableColumn
tmnxNatFwlDomPrefixRowStatus = _TmnxNatFwlDomPrefixRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 17, 4, 1, 4),
    _TmnxNatFwlDomPrefixRowStatus_Type()
)
tmnxNatFwlDomPrefixRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxNatFwlDomPrefixRowStatus.setStatus("current")
_TmnxNatFwlDomPrefixLastCh_Type = TimeStamp
_TmnxNatFwlDomPrefixLastCh_Object = MibTableColumn
tmnxNatFwlDomPrefixLastCh = _TmnxNatFwlDomPrefixLastCh_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 17, 4, 1, 5),
    _TmnxNatFwlDomPrefixLastCh_Type()
)
tmnxNatFwlDomPrefixLastCh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatFwlDomPrefixLastCh.setStatus("current")


class _TmnxNatFwlDomPrefixDescription_Type(TItemDescription):
    """Custom type tmnxNatFwlDomPrefixDescription based on TItemDescription"""
    defaultValue = OctetString("")


_TmnxNatFwlDomPrefixDescription_Type.__name__ = "TItemDescription"
_TmnxNatFwlDomPrefixDescription_Object = MibTableColumn
tmnxNatFwlDomPrefixDescription = _TmnxNatFwlDomPrefixDescription_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 17, 4, 1, 6),
    _TmnxNatFwlDomPrefixDescription_Type()
)
tmnxNatFwlDomPrefixDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxNatFwlDomPrefixDescription.setStatus("current")
_TmnxNatFwlHostTable_Object = MibTable
tmnxNatFwlHostTable = _TmnxNatFwlHostTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 17, 5)
)
if mibBuilder.loadTexts:
    tmnxNatFwlHostTable.setStatus("current")
_TmnxNatFwlHostEntry_Object = MibTableRow
tmnxNatFwlHostEntry = _TmnxNatFwlHostEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 17, 5, 1)
)
tmnxNatFwlHostEntry.setIndexNames(
    (0, "TIMETRA-SUBSCRIBER-MGMT-MIB", "tmnxSubInfoSubIdent"),
    (0, "TIMETRA-NAT-MIB", "tmnxNatFwlHostAddrType"),
    (0, "TIMETRA-NAT-MIB", "tmnxNatFwlHostAddr"),
    (0, "TIMETRA-NAT-MIB", "tmnxNatFwlHostAddrPrefixLength"),
    (0, "TIMETRA-NAT-MIB", "tmnxNatFwlHostMacAddress"),
    (0, "TIMETRA-NAT-MIB", "tmnxNatFwlHostPlcy"),
)
if mibBuilder.loadTexts:
    tmnxNatFwlHostEntry.setStatus("current")
_TmnxNatFwlHostAddrType_Type = InetAddressType
_TmnxNatFwlHostAddrType_Object = MibTableColumn
tmnxNatFwlHostAddrType = _TmnxNatFwlHostAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 17, 5, 1, 1),
    _TmnxNatFwlHostAddrType_Type()
)
tmnxNatFwlHostAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxNatFwlHostAddrType.setStatus("current")


class _TmnxNatFwlHostAddr_Type(InetAddress):
    """Custom type tmnxNatFwlHostAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxNatFwlHostAddr_Type.__name__ = "InetAddress"
_TmnxNatFwlHostAddr_Object = MibTableColumn
tmnxNatFwlHostAddr = _TmnxNatFwlHostAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 17, 5, 1, 2),
    _TmnxNatFwlHostAddr_Type()
)
tmnxNatFwlHostAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxNatFwlHostAddr.setStatus("current")
_TmnxNatFwlHostAddrPrefixLength_Type = InetAddressPrefixLength
_TmnxNatFwlHostAddrPrefixLength_Object = MibTableColumn
tmnxNatFwlHostAddrPrefixLength = _TmnxNatFwlHostAddrPrefixLength_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 17, 5, 1, 3),
    _TmnxNatFwlHostAddrPrefixLength_Type()
)
tmnxNatFwlHostAddrPrefixLength.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxNatFwlHostAddrPrefixLength.setStatus("current")
_TmnxNatFwlHostMacAddress_Type = MacAddress
_TmnxNatFwlHostMacAddress_Object = MibTableColumn
tmnxNatFwlHostMacAddress = _TmnxNatFwlHostMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 17, 5, 1, 4),
    _TmnxNatFwlHostMacAddress_Type()
)
tmnxNatFwlHostMacAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxNatFwlHostMacAddress.setStatus("current")
_TmnxNatFwlHostPlcy_Type = TNamedItem
_TmnxNatFwlHostPlcy_Object = MibTableColumn
tmnxNatFwlHostPlcy = _TmnxNatFwlHostPlcy_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 17, 5, 1, 5),
    _TmnxNatFwlHostPlcy_Type()
)
tmnxNatFwlHostPlcy.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxNatFwlHostPlcy.setStatus("current")
_TmnxNatFwlHostVRtrID_Type = TmnxVRtrIDOrZero
_TmnxNatFwlHostVRtrID_Object = MibTableColumn
tmnxNatFwlHostVRtrID = _TmnxNatFwlHostVRtrID_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 17, 5, 1, 6),
    _TmnxNatFwlHostVRtrID_Type()
)
tmnxNatFwlHostVRtrID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatFwlHostVRtrID.setStatus("current")
_TmnxNatFwlHostDmzV6_Type = TruthValue
_TmnxNatFwlHostDmzV6_Object = MibTableColumn
tmnxNatFwlHostDmzV6 = _TmnxNatFwlHostDmzV6_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 17, 5, 1, 7),
    _TmnxNatFwlHostDmzV6_Type()
)
tmnxNatFwlHostDmzV6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatFwlHostDmzV6.setStatus("current")
_TmnxNatFwlNbrTable_Object = MibTable
tmnxNatFwlNbrTable = _TmnxNatFwlNbrTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 17, 6)
)
if mibBuilder.loadTexts:
    tmnxNatFwlNbrTable.setStatus("current")
_TmnxNatFwlNbrEntry_Object = MibTableRow
tmnxNatFwlNbrEntry = _TmnxNatFwlNbrEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 17, 6, 1)
)
tmnxNatFwlNbrEntry.setIndexNames(
    (0, "TIMETRA-SUBSCRIBER-MGMT-MIB", "tmnxSubInfoSubIdent"),
    (0, "TIMETRA-NAT-MIB", "tmnxNatFwlNbrAddrType"),
    (0, "TIMETRA-NAT-MIB", "tmnxNatFwlNbrAddr"),
)
if mibBuilder.loadTexts:
    tmnxNatFwlNbrEntry.setStatus("current")
_TmnxNatFwlNbrAddrType_Type = InetAddressType
_TmnxNatFwlNbrAddrType_Object = MibTableColumn
tmnxNatFwlNbrAddrType = _TmnxNatFwlNbrAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 17, 6, 1, 1),
    _TmnxNatFwlNbrAddrType_Type()
)
tmnxNatFwlNbrAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxNatFwlNbrAddrType.setStatus("current")


class _TmnxNatFwlNbrAddr_Type(InetAddress):
    """Custom type tmnxNatFwlNbrAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )
    fixed_length = 16


_TmnxNatFwlNbrAddr_Type.__name__ = "InetAddress"
_TmnxNatFwlNbrAddr_Object = MibTableColumn
tmnxNatFwlNbrAddr = _TmnxNatFwlNbrAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 17, 6, 1, 2),
    _TmnxNatFwlNbrAddr_Type()
)
tmnxNatFwlNbrAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxNatFwlNbrAddr.setStatus("current")
_TmnxNatFwlNbrMacAddress_Type = MacAddress
_TmnxNatFwlNbrMacAddress_Object = MibTableColumn
tmnxNatFwlNbrMacAddress = _TmnxNatFwlNbrMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 17, 6, 1, 3),
    _TmnxNatFwlNbrMacAddress_Type()
)
tmnxNatFwlNbrMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatFwlNbrMacAddress.setStatus("current")
_TmnxNatSyslogObjs_ObjectIdentity = ObjectIdentity
tmnxNatSyslogObjs = _TmnxNatSyslogObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 18)
)
_TmnxNatSyslogExpPlcyTable_Object = MibTable
tmnxNatSyslogExpPlcyTable = _TmnxNatSyslogExpPlcyTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 18, 1)
)
if mibBuilder.loadTexts:
    tmnxNatSyslogExpPlcyTable.setStatus("current")
_TmnxNatSyslogExpPlcyEntry_Object = MibTableRow
tmnxNatSyslogExpPlcyEntry = _TmnxNatSyslogExpPlcyEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 18, 1, 1)
)
tmnxNatSyslogExpPlcyEntry.setIndexNames(
    (1, "TIMETRA-NAT-MIB", "tmnxNatSyslogExpPlcyName"),
)
if mibBuilder.loadTexts:
    tmnxNatSyslogExpPlcyEntry.setStatus("current")
_TmnxNatSyslogExpPlcyName_Type = TNamedItem
_TmnxNatSyslogExpPlcyName_Object = MibTableColumn
tmnxNatSyslogExpPlcyName = _TmnxNatSyslogExpPlcyName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 18, 1, 1, 1),
    _TmnxNatSyslogExpPlcyName_Type()
)
tmnxNatSyslogExpPlcyName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxNatSyslogExpPlcyName.setStatus("current")
_TmnxNatSyslogExpPlcyLastCh_Type = TimeStamp
_TmnxNatSyslogExpPlcyLastCh_Object = MibTableColumn
tmnxNatSyslogExpPlcyLastCh = _TmnxNatSyslogExpPlcyLastCh_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 18, 1, 1, 2),
    _TmnxNatSyslogExpPlcyLastCh_Type()
)
tmnxNatSyslogExpPlcyLastCh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatSyslogExpPlcyLastCh.setStatus("current")
_TmnxNatSyslogExpPlcyRowStatus_Type = RowStatus
_TmnxNatSyslogExpPlcyRowStatus_Object = MibTableColumn
tmnxNatSyslogExpPlcyRowStatus = _TmnxNatSyslogExpPlcyRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 18, 1, 1, 3),
    _TmnxNatSyslogExpPlcyRowStatus_Type()
)
tmnxNatSyslogExpPlcyRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxNatSyslogExpPlcyRowStatus.setStatus("current")


class _TmnxNatSyslogExpPlcyDescription_Type(TItemDescription):
    """Custom type tmnxNatSyslogExpPlcyDescription based on TItemDescription"""
    defaultValue = OctetString("")


_TmnxNatSyslogExpPlcyDescription_Type.__name__ = "TItemDescription"
_TmnxNatSyslogExpPlcyDescription_Object = MibTableColumn
tmnxNatSyslogExpPlcyDescription = _TmnxNatSyslogExpPlcyDescription_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 18, 1, 1, 4),
    _TmnxNatSyslogExpPlcyDescription_Type()
)
tmnxNatSyslogExpPlcyDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxNatSyslogExpPlcyDescription.setStatus("current")


class _TmnxNatSyslogExpPlcyFacility_Type(TmnxSyslogFacility):
    """Custom type tmnxNatSyslogExpPlcyFacility based on TmnxSyslogFacility"""
    defaultValue = 16


_TmnxNatSyslogExpPlcyFacility_Type.__name__ = "TmnxSyslogFacility"
_TmnxNatSyslogExpPlcyFacility_Object = MibTableColumn
tmnxNatSyslogExpPlcyFacility = _TmnxNatSyslogExpPlcyFacility_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 18, 1, 1, 5),
    _TmnxNatSyslogExpPlcyFacility_Type()
)
tmnxNatSyslogExpPlcyFacility.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxNatSyslogExpPlcyFacility.setStatus("current")


class _TmnxNatSyslogExpPlcySeverity_Type(TmnxSyslogSeverity):
    """Custom type tmnxNatSyslogExpPlcySeverity based on TmnxSyslogSeverity"""
    defaultValue = 6


_TmnxNatSyslogExpPlcySeverity_Type.__name__ = "TmnxSyslogSeverity"
_TmnxNatSyslogExpPlcySeverity_Object = MibTableColumn
tmnxNatSyslogExpPlcySeverity = _TmnxNatSyslogExpPlcySeverity_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 18, 1, 1, 6),
    _TmnxNatSyslogExpPlcySeverity_Type()
)
tmnxNatSyslogExpPlcySeverity.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxNatSyslogExpPlcySeverity.setStatus("current")


class _TmnxNatSyslogExpPlcyPrefix_Type(DisplayString):
    """Custom type tmnxNatSyslogExpPlcyPrefix based on DisplayString"""
    defaultValue = OctetString("TMNX")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_TmnxNatSyslogExpPlcyPrefix_Type.__name__ = "DisplayString"
_TmnxNatSyslogExpPlcyPrefix_Object = MibTableColumn
tmnxNatSyslogExpPlcyPrefix = _TmnxNatSyslogExpPlcyPrefix_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 18, 1, 1, 7),
    _TmnxNatSyslogExpPlcyPrefix_Type()
)
tmnxNatSyslogExpPlcyPrefix.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxNatSyslogExpPlcyPrefix.setStatus("current")


class _TmnxNatSyslogExpPlcyInclude_Type(Bits):
    """Custom type tmnxNatSyslogExpPlcyInclude based on Bits"""
    defaultBinValue = "0"

    namedValues = NamedValues(
        *(("subId", 0),
          ("foreignIp", 1),
          ("foreignPort", 2),
          ("destinationIp", 3),
          ("natPolicyName", 4))
    )

_TmnxNatSyslogExpPlcyInclude_Type.__name__ = "Bits"
_TmnxNatSyslogExpPlcyInclude_Object = MibTableColumn
tmnxNatSyslogExpPlcyInclude = _TmnxNatSyslogExpPlcyInclude_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 18, 1, 1, 8),
    _TmnxNatSyslogExpPlcyInclude_Type()
)
tmnxNatSyslogExpPlcyInclude.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxNatSyslogExpPlcyInclude.setStatus("current")


class _TmnxNatSyslogExpPlcyMtu_Type(Unsigned32):
    """Custom type tmnxNatSyslogExpPlcyMtu based on Unsigned32"""
    defaultValue = 1500

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(512, 9000),
    )


_TmnxNatSyslogExpPlcyMtu_Type.__name__ = "Unsigned32"
_TmnxNatSyslogExpPlcyMtu_Object = MibTableColumn
tmnxNatSyslogExpPlcyMtu = _TmnxNatSyslogExpPlcyMtu_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 18, 1, 1, 9),
    _TmnxNatSyslogExpPlcyMtu_Type()
)
tmnxNatSyslogExpPlcyMtu.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxNatSyslogExpPlcyMtu.setStatus("current")


class _TmnxNatSyslogExpPlcyRateLimit_Type(Integer32):
    """Custom type tmnxNatSyslogExpPlcyRateLimit based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(10, 2147483647),
    )


_TmnxNatSyslogExpPlcyRateLimit_Type.__name__ = "Integer32"
_TmnxNatSyslogExpPlcyRateLimit_Object = MibTableColumn
tmnxNatSyslogExpPlcyRateLimit = _TmnxNatSyslogExpPlcyRateLimit_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 18, 1, 1, 10),
    _TmnxNatSyslogExpPlcyRateLimit_Type()
)
tmnxNatSyslogExpPlcyRateLimit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxNatSyslogExpPlcyRateLimit.setStatus("current")
if mibBuilder.loadTexts:
    tmnxNatSyslogExpPlcyRateLimit.setUnits("packets per second")


class _TmnxNatSyslogExpPlcyMaxTxDelay_Type(Integer32):
    """Custom type tmnxNatSyslogExpPlcyMaxTxDelay based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_TmnxNatSyslogExpPlcyMaxTxDelay_Type.__name__ = "Integer32"
_TmnxNatSyslogExpPlcyMaxTxDelay_Object = MibTableColumn
tmnxNatSyslogExpPlcyMaxTxDelay = _TmnxNatSyslogExpPlcyMaxTxDelay_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 18, 1, 1, 11),
    _TmnxNatSyslogExpPlcyMaxTxDelay_Type()
)
tmnxNatSyslogExpPlcyMaxTxDelay.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxNatSyslogExpPlcyMaxTxDelay.setStatus("current")
if mibBuilder.loadTexts:
    tmnxNatSyslogExpPlcyMaxTxDelay.setUnits("deciseconds")
_TmnxNatSyslogColTable_Object = MibTable
tmnxNatSyslogColTable = _TmnxNatSyslogColTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 18, 2)
)
if mibBuilder.loadTexts:
    tmnxNatSyslogColTable.setStatus("current")
_TmnxNatSyslogColEntry_Object = MibTableRow
tmnxNatSyslogColEntry = _TmnxNatSyslogColEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 18, 2, 1)
)
tmnxNatSyslogColEntry.setIndexNames(
    (0, "TIMETRA-NAT-MIB", "tmnxNatSyslogExpPlcyName"),
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "TIMETRA-NAT-MIB", "tmnxNatSyslogColAddrType"),
    (0, "TIMETRA-NAT-MIB", "tmnxNatSyslogColAddr"),
)
if mibBuilder.loadTexts:
    tmnxNatSyslogColEntry.setStatus("current")
_TmnxNatSyslogColAddrType_Type = InetAddressType
_TmnxNatSyslogColAddrType_Object = MibTableColumn
tmnxNatSyslogColAddrType = _TmnxNatSyslogColAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 18, 2, 1, 1),
    _TmnxNatSyslogColAddrType_Type()
)
tmnxNatSyslogColAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxNatSyslogColAddrType.setStatus("current")


class _TmnxNatSyslogColAddr_Type(InetAddress):
    """Custom type tmnxNatSyslogColAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
    )


_TmnxNatSyslogColAddr_Type.__name__ = "InetAddress"
_TmnxNatSyslogColAddr_Object = MibTableColumn
tmnxNatSyslogColAddr = _TmnxNatSyslogColAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 18, 2, 1, 2),
    _TmnxNatSyslogColAddr_Type()
)
tmnxNatSyslogColAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxNatSyslogColAddr.setStatus("current")
_TmnxNatSyslogColRowStatus_Type = RowStatus
_TmnxNatSyslogColRowStatus_Object = MibTableColumn
tmnxNatSyslogColRowStatus = _TmnxNatSyslogColRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 18, 2, 1, 3),
    _TmnxNatSyslogColRowStatus_Type()
)
tmnxNatSyslogColRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxNatSyslogColRowStatus.setStatus("current")
_TmnxNatSyslogColLastCh_Type = TimeStamp
_TmnxNatSyslogColLastCh_Object = MibTableColumn
tmnxNatSyslogColLastCh = _TmnxNatSyslogColLastCh_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 18, 2, 1, 4),
    _TmnxNatSyslogColLastCh_Type()
)
tmnxNatSyslogColLastCh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatSyslogColLastCh.setStatus("current")


class _TmnxNatSyslogColAdminState_Type(TmnxAdminState):
    """Custom type tmnxNatSyslogColAdminState based on TmnxAdminState"""
    defaultValue = 3


_TmnxNatSyslogColAdminState_Type.__name__ = "TmnxAdminState"
_TmnxNatSyslogColAdminState_Object = MibTableColumn
tmnxNatSyslogColAdminState = _TmnxNatSyslogColAdminState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 18, 2, 1, 5),
    _TmnxNatSyslogColAdminState_Type()
)
tmnxNatSyslogColAdminState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxNatSyslogColAdminState.setStatus("current")


class _TmnxNatSyslogColSrcAddrType_Type(InetAddressType):
    """Custom type tmnxNatSyslogColSrcAddrType based on InetAddressType"""
    defaultValue = 0


_TmnxNatSyslogColSrcAddrType_Type.__name__ = "InetAddressType"
_TmnxNatSyslogColSrcAddrType_Object = MibTableColumn
tmnxNatSyslogColSrcAddrType = _TmnxNatSyslogColSrcAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 18, 2, 1, 6),
    _TmnxNatSyslogColSrcAddrType_Type()
)
tmnxNatSyslogColSrcAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxNatSyslogColSrcAddrType.setStatus("current")


class _TmnxNatSyslogColSrcAddr_Type(InetAddress):
    """Custom type tmnxNatSyslogColSrcAddr based on InetAddress"""
    defaultValue = OctetString("")

    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
    )


_TmnxNatSyslogColSrcAddr_Type.__name__ = "InetAddress"
_TmnxNatSyslogColSrcAddr_Object = MibTableColumn
tmnxNatSyslogColSrcAddr = _TmnxNatSyslogColSrcAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 18, 2, 1, 7),
    _TmnxNatSyslogColSrcAddr_Type()
)
tmnxNatSyslogColSrcAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxNatSyslogColSrcAddr.setStatus("current")


class _TmnxNatSyslogColDestPort_Type(InetPortNumber):
    """Custom type tmnxNatSyslogColDestPort based on InetPortNumber"""
    defaultValue = 514

    subtypeSpec = InetPortNumber.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_TmnxNatSyslogColDestPort_Type.__name__ = "InetPortNumber"
_TmnxNatSyslogColDestPort_Object = MibTableColumn
tmnxNatSyslogColDestPort = _TmnxNatSyslogColDestPort_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 18, 2, 1, 8),
    _TmnxNatSyslogColDestPort_Type()
)
tmnxNatSyslogColDestPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxNatSyslogColDestPort.setStatus("current")
_TmnxNatCupsObjs_ObjectIdentity = ObjectIdentity
tmnxNatCupsObjs = _TmnxNatCupsObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 19)
)
_TmnxNatUpPlcyTable_Object = MibTable
tmnxNatUpPlcyTable = _TmnxNatUpPlcyTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 19, 1)
)
if mibBuilder.loadTexts:
    tmnxNatUpPlcyTable.setStatus("current")
_TmnxNatUpPlcyEntry_Object = MibTableRow
tmnxNatUpPlcyEntry = _TmnxNatUpPlcyEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 19, 1, 1)
)
tmnxNatUpPlcyEntry.setIndexNames(
    (1, "TIMETRA-NAT-MIB", "tmnxNatUpPlcyName"),
)
if mibBuilder.loadTexts:
    tmnxNatUpPlcyEntry.setStatus("current")
_TmnxNatUpPlcyName_Type = TNamedItem
_TmnxNatUpPlcyName_Object = MibTableColumn
tmnxNatUpPlcyName = _TmnxNatUpPlcyName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 19, 1, 1, 1),
    _TmnxNatUpPlcyName_Type()
)
tmnxNatUpPlcyName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxNatUpPlcyName.setStatus("current")
_TmnxNatUpPlcyRowStatus_Type = RowStatus
_TmnxNatUpPlcyRowStatus_Object = MibTableColumn
tmnxNatUpPlcyRowStatus = _TmnxNatUpPlcyRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 19, 1, 1, 2),
    _TmnxNatUpPlcyRowStatus_Type()
)
tmnxNatUpPlcyRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxNatUpPlcyRowStatus.setStatus("current")


class _TmnxNatUpPlcyExtPortBlkSize_Type(Unsigned32):
    """Custom type tmnxNatUpPlcyExtPortBlkSize based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(10, 5000),
    )


_TmnxNatUpPlcyExtPortBlkSize_Type.__name__ = "Unsigned32"
_TmnxNatUpPlcyExtPortBlkSize_Object = MibTableColumn
tmnxNatUpPlcyExtPortBlkSize = _TmnxNatUpPlcyExtPortBlkSize_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 19, 1, 1, 3),
    _TmnxNatUpPlcyExtPortBlkSize_Type()
)
tmnxNatUpPlcyExtPortBlkSize.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxNatUpPlcyExtPortBlkSize.setStatus("current")


class _TmnxNatUpPlcyIcmpEchoReply_Type(TruthValue):
    """Custom type tmnxNatUpPlcyIcmpEchoReply based on TruthValue"""
    defaultValue = 2


_TmnxNatUpPlcyIcmpEchoReply_Type.__name__ = "TruthValue"
_TmnxNatUpPlcyIcmpEchoReply_Object = MibTableColumn
tmnxNatUpPlcyIcmpEchoReply = _TmnxNatUpPlcyIcmpEchoReply_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 19, 1, 1, 4),
    _TmnxNatUpPlcyIcmpEchoReply_Type()
)
tmnxNatUpPlcyIcmpEchoReply.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxNatUpPlcyIcmpEchoReply.setStatus("current")


class _TmnxNatUpPlExPrtBlcksWmarkHigh_Type(TmnxNatWaterMark):
    """Custom type tmnxNatUpPlExPrtBlcksWmarkHigh based on TmnxNatWaterMark"""
    defaultValue = 0

    subtypeSpec = TmnxNatWaterMark.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 100),
    )


_TmnxNatUpPlExPrtBlcksWmarkHigh_Type.__name__ = "TmnxNatWaterMark"
_TmnxNatUpPlExPrtBlcksWmarkHigh_Object = MibTableColumn
tmnxNatUpPlExPrtBlcksWmarkHigh = _TmnxNatUpPlExPrtBlcksWmarkHigh_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 19, 1, 1, 5),
    _TmnxNatUpPlExPrtBlcksWmarkHigh_Type()
)
tmnxNatUpPlExPrtBlcksWmarkHigh.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxNatUpPlExPrtBlcksWmarkHigh.setStatus("current")


class _TmnxNatUpPlExPrtBlcksWmarkLow_Type(TmnxNatWaterMark):
    """Custom type tmnxNatUpPlExPrtBlcksWmarkLow based on TmnxNatWaterMark"""
    defaultValue = 0

    subtypeSpec = TmnxNatWaterMark.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 99),
    )


_TmnxNatUpPlExPrtBlcksWmarkLow_Type.__name__ = "TmnxNatWaterMark"
_TmnxNatUpPlExPrtBlcksWmarkLow_Object = MibTableColumn
tmnxNatUpPlExPrtBlcksWmarkLow = _TmnxNatUpPlExPrtBlcksWmarkLow_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 19, 1, 1, 6),
    _TmnxNatUpPlExPrtBlcksWmarkLow_Type()
)
tmnxNatUpPlExPrtBlcksWmarkLow.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxNatUpPlExPrtBlcksWmarkLow.setStatus("current")


class _TmnxNatUpPlcyDhInsideIpAddrType_Type(InetAddressType):
    """Custom type tmnxNatUpPlcyDhInsideIpAddrType based on InetAddressType"""
    defaultValue = 0


_TmnxNatUpPlcyDhInsideIpAddrType_Type.__name__ = "InetAddressType"
_TmnxNatUpPlcyDhInsideIpAddrType_Object = MibTableColumn
tmnxNatUpPlcyDhInsideIpAddrType = _TmnxNatUpPlcyDhInsideIpAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 19, 1, 1, 7),
    _TmnxNatUpPlcyDhInsideIpAddrType_Type()
)
tmnxNatUpPlcyDhInsideIpAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxNatUpPlcyDhInsideIpAddrType.setStatus("current")


class _TmnxNatUpPlcyDhInsideIpAddress_Type(InetAddress):
    """Custom type tmnxNatUpPlcyDhInsideIpAddress based on InetAddress"""
    defaultHexValue = ""

    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
    )


_TmnxNatUpPlcyDhInsideIpAddress_Type.__name__ = "InetAddress"
_TmnxNatUpPlcyDhInsideIpAddress_Object = MibTableColumn
tmnxNatUpPlcyDhInsideIpAddress = _TmnxNatUpPlcyDhInsideIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 19, 1, 1, 8),
    _TmnxNatUpPlcyDhInsideIpAddress_Type()
)
tmnxNatUpPlcyDhInsideIpAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxNatUpPlcyDhInsideIpAddress.setStatus("current")


class _TmnxNatUpPlcyDhInsideRtrId_Type(TmnxVRtrIDOrZero):
    """Custom type tmnxNatUpPlcyDhInsideRtrId based on TmnxVRtrIDOrZero"""
    defaultValue = 0


_TmnxNatUpPlcyDhInsideRtrId_Type.__name__ = "TmnxVRtrIDOrZero"
_TmnxNatUpPlcyDhInsideRtrId_Object = MibTableColumn
tmnxNatUpPlcyDhInsideRtrId = _TmnxNatUpPlcyDhInsideRtrId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 19, 1, 1, 9),
    _TmnxNatUpPlcyDhInsideRtrId_Type()
)
tmnxNatUpPlcyDhInsideRtrId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxNatUpPlcyDhInsideRtrId.setStatus("current")


class _TmnxNatUpPlcyDhRate_Type(Unsigned32):
    """Custom type tmnxNatUpPlcyDhRate based on Unsigned32"""
    defaultValue = 10

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10000),
    )


_TmnxNatUpPlcyDhRate_Type.__name__ = "Unsigned32"
_TmnxNatUpPlcyDhRate_Object = MibTableColumn
tmnxNatUpPlcyDhRate = _TmnxNatUpPlcyDhRate_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 19, 1, 1, 10),
    _TmnxNatUpPlcyDhRate_Type()
)
tmnxNatUpPlcyDhRate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxNatUpPlcyDhRate.setStatus("current")
if mibBuilder.loadTexts:
    tmnxNatUpPlcyDhRate.setUnits("mbps")
_TmnxNatSysStatsObjs_ObjectIdentity = ObjectIdentity
tmnxNatSysStatsObjs = _TmnxNatSysStatsObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 20)
)
_TmnxNatSysRadiusAcctInterimDrop_Type = Counter64
_TmnxNatSysRadiusAcctInterimDrop_Object = MibScalar
tmnxNatSysRadiusAcctInterimDrop = _TmnxNatSysRadiusAcctInterimDrop_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 20, 1),
    _TmnxNatSysRadiusAcctInterimDrop_Type()
)
tmnxNatSysRadiusAcctInterimDrop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatSysRadiusAcctInterimDrop.setStatus("current")
_TmnxNatCpmObjs_ObjectIdentity = ObjectIdentity
tmnxNatCpmObjs = _TmnxNatCpmObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 21)
)
_TmnxNatCpmPlcyTable_Object = MibTable
tmnxNatCpmPlcyTable = _TmnxNatCpmPlcyTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 21, 1)
)
if mibBuilder.loadTexts:
    tmnxNatCpmPlcyTable.setStatus("current")
_TmnxNatCpmPlcyEntry_Object = MibTableRow
tmnxNatCpmPlcyEntry = _TmnxNatCpmPlcyEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 21, 1, 1)
)
tmnxNatCpmPlcyEntry.setIndexNames(
    (1, "TIMETRA-NAT-MIB", "tmnxNatCpmPlcyName"),
)
if mibBuilder.loadTexts:
    tmnxNatCpmPlcyEntry.setStatus("current")
_TmnxNatCpmPlcyName_Type = TNamedItem
_TmnxNatCpmPlcyName_Object = MibTableColumn
tmnxNatCpmPlcyName = _TmnxNatCpmPlcyName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 21, 1, 1, 1),
    _TmnxNatCpmPlcyName_Type()
)
tmnxNatCpmPlcyName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxNatCpmPlcyName.setStatus("current")
_TmnxNatCpmPlcyRowStatus_Type = RowStatus
_TmnxNatCpmPlcyRowStatus_Object = MibTableColumn
tmnxNatCpmPlcyRowStatus = _TmnxNatCpmPlcyRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 21, 1, 1, 2),
    _TmnxNatCpmPlcyRowStatus_Type()
)
tmnxNatCpmPlcyRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxNatCpmPlcyRowStatus.setStatus("current")
_TmnxNatIsaGrpTableLastCh_Type = TimeStamp
_TmnxNatIsaGrpTableLastCh_Object = MibScalar
tmnxNatIsaGrpTableLastCh = _TmnxNatIsaGrpTableLastCh_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 100),
    _TmnxNatIsaGrpTableLastCh_Type()
)
tmnxNatIsaGrpTableLastCh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatIsaGrpTableLastCh.setStatus("current")
_TmnxNatIsaMdaTableLastCh_Type = TimeStamp
_TmnxNatIsaMdaTableLastCh_Object = MibScalar
tmnxNatIsaMdaTableLastCh = _TmnxNatIsaMdaTableLastCh_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 101),
    _TmnxNatIsaMdaTableLastCh_Type()
)
tmnxNatIsaMdaTableLastCh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatIsaMdaTableLastCh.setStatus("current")
_TmnxNatIsaMdaStatTableLastCh_Type = TimeStamp
_TmnxNatIsaMdaStatTableLastCh_Object = MibScalar
tmnxNatIsaMdaStatTableLastCh = _TmnxNatIsaMdaStatTableLastCh_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 102),
    _TmnxNatIsaMdaStatTableLastCh_Type()
)
tmnxNatIsaMdaStatTableLastCh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatIsaMdaStatTableLastCh.setStatus("current")
_TmnxNatPlcyTableLastCh_Type = TimeStamp
_TmnxNatPlcyTableLastCh_Object = MibScalar
tmnxNatPlcyTableLastCh = _TmnxNatPlcyTableLastCh_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 103),
    _TmnxNatPlcyTableLastCh_Type()
)
tmnxNatPlcyTableLastCh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatPlcyTableLastCh.setStatus("current")
_TmnxNatVrtrTableLastCh_Type = TimeStamp
_TmnxNatVrtrTableLastCh_Object = MibScalar
tmnxNatVrtrTableLastCh = _TmnxNatVrtrTableLastCh_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 104),
    _TmnxNatVrtrTableLastCh_Type()
)
tmnxNatVrtrTableLastCh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatVrtrTableLastCh.setStatus("current")
_TmnxNatL2AwAddrTableLastCh_Type = TimeStamp
_TmnxNatL2AwAddrTableLastCh_Object = MibScalar
tmnxNatL2AwAddrTableLastCh = _TmnxNatL2AwAddrTableLastCh_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 105),
    _TmnxNatL2AwAddrTableLastCh_Type()
)
tmnxNatL2AwAddrTableLastCh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatL2AwAddrTableLastCh.setStatus("current")
_TmnxNatPlTableLastCh_Type = TimeStamp
_TmnxNatPlTableLastCh_Object = MibScalar
tmnxNatPlTableLastCh = _TmnxNatPlTableLastCh_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 106),
    _TmnxNatPlTableLastCh_Type()
)
tmnxNatPlTableLastCh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatPlTableLastCh.setStatus("current")
_TmnxNatPlRangeTableLastCh_Type = TimeStamp
_TmnxNatPlRangeTableLastCh_Object = MibScalar
tmnxNatPlRangeTableLastCh = _TmnxNatPlRangeTableLastCh_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 107),
    _TmnxNatPlRangeTableLastCh_Type()
)
tmnxNatPlRangeTableLastCh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatPlRangeTableLastCh.setStatus("current")
_TmnxNatDestTableLastCh_Type = TimeStamp
_TmnxNatDestTableLastCh_Object = MibScalar
tmnxNatDestTableLastCh = _TmnxNatDestTableLastCh_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 108),
    _TmnxNatDestTableLastCh_Type()
)
tmnxNatDestTableLastCh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatDestTableLastCh.setStatus("current")
_TmnxNatMapLsnHostTableLastCh_Type = TimeStamp
_TmnxNatMapLsnHostTableLastCh_Object = MibScalar
tmnxNatMapLsnHostTableLastCh = _TmnxNatMapLsnHostTableLastCh_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 109),
    _TmnxNatMapLsnHostTableLastCh_Type()
)
tmnxNatMapLsnHostTableLastCh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatMapLsnHostTableLastCh.setStatus("obsolete")
_TmnxNatMapTableLastCh_Type = TimeStamp
_TmnxNatMapTableLastCh_Object = MibScalar
tmnxNatMapTableLastCh = _TmnxNatMapTableLastCh_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 110),
    _TmnxNatMapTableLastCh_Type()
)
tmnxNatMapTableLastCh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatMapTableLastCh.setStatus("obsolete")
_TmnxNatDsliteAddrTableLastCh_Type = TimeStamp
_TmnxNatDsliteAddrTableLastCh_Object = MibScalar
tmnxNatDsliteAddrTableLastCh = _TmnxNatDsliteAddrTableLastCh_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 111),
    _TmnxNatDsliteAddrTableLastCh_Type()
)
tmnxNatDsliteAddrTableLastCh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatDsliteAddrTableLastCh.setStatus("current")
_TmnxNatApTableLastCh_Type = TimeStamp
_TmnxNatApTableLastCh_Object = MibScalar
tmnxNatApTableLastCh = _TmnxNatApTableLastCh_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 112),
    _TmnxNatApTableLastCh_Type()
)
tmnxNatApTableLastCh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatApTableLastCh.setStatus("obsolete")
_TmnxNatApServTableLastCh_Type = TimeStamp
_TmnxNatApServTableLastCh_Object = MibScalar
tmnxNatApServTableLastCh = _TmnxNatApServTableLastCh_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 113),
    _TmnxNatApServTableLastCh_Type()
)
tmnxNatApServTableLastCh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatApServTableLastCh.setStatus("obsolete")
_TmnxNat64TableLastCh_Type = TimeStamp
_TmnxNat64TableLastCh_Object = MibScalar
tmnxNat64TableLastCh = _TmnxNat64TableLastCh_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 115),
    _TmnxNat64TableLastCh_Type()
)
tmnxNat64TableLastCh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNat64TableLastCh.setStatus("current")
_TmnxNatGrpCfgTableLastCh_Type = TimeStamp
_TmnxNatGrpCfgTableLastCh_Object = MibScalar
tmnxNatGrpCfgTableLastCh = _TmnxNatGrpCfgTableLastCh_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 116),
    _TmnxNatGrpCfgTableLastCh_Type()
)
tmnxNatGrpCfgTableLastCh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatGrpCfgTableLastCh.setStatus("current")
_TmnxNatSubIdTableLastCh_Type = TimeStamp
_TmnxNatSubIdTableLastCh_Object = MibScalar
tmnxNatSubIdTableLastCh = _TmnxNatSubIdTableLastCh_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 117),
    _TmnxNatSubIdTableLastCh_Type()
)
tmnxNatSubIdTableLastCh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatSubIdTableLastCh.setStatus("current")
_TmnxNatPcpPlcyTableLastCh_Type = TimeStamp
_TmnxNatPcpPlcyTableLastCh_Object = MibScalar
tmnxNatPcpPlcyTableLastCh = _TmnxNatPcpPlcyTableLastCh_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 118),
    _TmnxNatPcpPlcyTableLastCh_Type()
)
tmnxNatPcpPlcyTableLastCh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatPcpPlcyTableLastCh.setStatus("current")
_TmnxNatPcpSrvTableLastCh_Type = TimeStamp
_TmnxNatPcpSrvTableLastCh_Object = MibScalar
tmnxNatPcpSrvTableLastCh = _TmnxNatPcpSrvTableLastCh_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 119),
    _TmnxNatPcpSrvTableLastCh_Type()
)
tmnxNatPcpSrvTableLastCh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatPcpSrvTableLastCh.setStatus("current")
_TmnxNatPcpSrvIfTableLastCh_Type = TimeStamp
_TmnxNatPcpSrvIfTableLastCh_Object = MibScalar
tmnxNatPcpSrvIfTableLastCh = _TmnxNatPcpSrvIfTableLastCh_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 121),
    _TmnxNatPcpSrvIfTableLastCh_Type()
)
tmnxNatPcpSrvIfTableLastCh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatPcpSrvIfTableLastCh.setStatus("current")
_TmnxNatDetPlcyTableLastCh_Type = TimeStamp
_TmnxNatDetPlcyTableLastCh_Object = MibScalar
tmnxNatDetPlcyTableLastCh = _TmnxNatDetPlcyTableLastCh_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 122),
    _TmnxNatDetPlcyTableLastCh_Type()
)
tmnxNatDetPlcyTableLastCh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatDetPlcyTableLastCh.setStatus("current")
_TmnxNatDetMapTableLastCh_Type = TimeStamp
_TmnxNatDetMapTableLastCh_Object = MibScalar
tmnxNatDetMapTableLastCh = _TmnxNatDetMapTableLastCh_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 123),
    _TmnxNatDetMapTableLastCh_Type()
)
tmnxNatDetMapTableLastCh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatDetMapTableLastCh.setStatus("current")
_TmnxNatUpnpPlcyTableLastCh_Type = TimeStamp
_TmnxNatUpnpPlcyTableLastCh_Object = MibScalar
tmnxNatUpnpPlcyTableLastCh = _TmnxNatUpnpPlcyTableLastCh_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 125),
    _TmnxNatUpnpPlcyTableLastCh_Type()
)
tmnxNatUpnpPlcyTableLastCh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatUpnpPlcyTableLastCh.setStatus("current")
_TmnxNatPrefixListTableLastCh_Type = TimeStamp
_TmnxNatPrefixListTableLastCh_Object = MibScalar
tmnxNatPrefixListTableLastCh = _TmnxNatPrefixListTableLastCh_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 130),
    _TmnxNatPrefixListTableLastCh_Type()
)
tmnxNatPrefixListTableLastCh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatPrefixListTableLastCh.setStatus("current")
_TmnxNatPrefixTableLastCh_Type = TimeStamp
_TmnxNatPrefixTableLastCh_Object = MibScalar
tmnxNatPrefixTableLastCh = _TmnxNatPrefixTableLastCh_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 131),
    _TmnxNatPrefixTableLastCh_Type()
)
tmnxNatPrefixTableLastCh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatPrefixTableLastCh.setStatus("current")
_TmnxNatClsfrTableLastCh_Type = TimeStamp
_TmnxNatClsfrTableLastCh_Object = MibScalar
tmnxNatClsfrTableLastCh = _TmnxNatClsfrTableLastCh_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 132),
    _TmnxNatClsfrTableLastCh_Type()
)
tmnxNatClsfrTableLastCh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatClsfrTableLastCh.setStatus("current")
_TmnxNatClsfrN3TableLastCh_Type = TimeStamp
_TmnxNatClsfrN3TableLastCh_Object = MibScalar
tmnxNatClsfrN3TableLastCh = _TmnxNatClsfrN3TableLastCh_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 133),
    _TmnxNatClsfrN3TableLastCh_Type()
)
tmnxNatClsfrN3TableLastCh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatClsfrN3TableLastCh.setStatus("current")
_TmnxNatMapDomTableLastCh_Type = TimeStamp
_TmnxNatMapDomTableLastCh_Object = MibScalar
tmnxNatMapDomTableLastCh = _TmnxNatMapDomTableLastCh_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 134),
    _TmnxNatMapDomTableLastCh_Type()
)
tmnxNatMapDomTableLastCh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatMapDomTableLastCh.setStatus("current")
_TmnxNatMapRuleTableLastCh_Type = TimeStamp
_TmnxNatMapRuleTableLastCh_Object = MibScalar
tmnxNatMapRuleTableLastCh = _TmnxNatMapRuleTableLastCh_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 135),
    _TmnxNatMapRuleTableLastCh_Type()
)
tmnxNatMapRuleTableLastCh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatMapRuleTableLastCh.setStatus("current")
_TmnxNatMapVrtrDomTableLastCh_Type = TimeStamp
_TmnxNatMapVrtrDomTableLastCh_Object = MibScalar
tmnxNatMapVrtrDomTableLastCh = _TmnxNatMapVrtrDomTableLastCh_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 136),
    _TmnxNatMapVrtrDomTableLastCh_Type()
)
tmnxNatMapVrtrDomTableLastCh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatMapVrtrDomTableLastCh.setStatus("current")
_TmnxNatFwlPlcyTableLastCh_Type = TimeStamp
_TmnxNatFwlPlcyTableLastCh_Object = MibScalar
tmnxNatFwlPlcyTableLastCh = _TmnxNatFwlPlcyTableLastCh_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 137),
    _TmnxNatFwlPlcyTableLastCh_Type()
)
tmnxNatFwlPlcyTableLastCh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatFwlPlcyTableLastCh.setStatus("current")
_TmnxNatFwlDomTableLastCh_Type = TimeStamp
_TmnxNatFwlDomTableLastCh_Object = MibScalar
tmnxNatFwlDomTableLastCh = _TmnxNatFwlDomTableLastCh_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 138),
    _TmnxNatFwlDomTableLastCh_Type()
)
tmnxNatFwlDomTableLastCh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatFwlDomTableLastCh.setStatus("current")
_TmnxNatFwlDomPrefixTableLastCh_Type = TimeStamp
_TmnxNatFwlDomPrefixTableLastCh_Object = MibScalar
tmnxNatFwlDomPrefixTableLastCh = _TmnxNatFwlDomPrefixTableLastCh_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 139),
    _TmnxNatFwlDomPrefixTableLastCh_Type()
)
tmnxNatFwlDomPrefixTableLastCh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatFwlDomPrefixTableLastCh.setStatus("current")
_TmnxNatPlcyUnknProtTableLastCh_Type = TimeStamp
_TmnxNatPlcyUnknProtTableLastCh_Object = MibScalar
tmnxNatPlcyUnknProtTableLastCh = _TmnxNatPlcyUnknProtTableLastCh_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 140),
    _TmnxNatPlcyUnknProtTableLastCh_Type()
)
tmnxNatPlcyUnknProtTableLastCh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatPlcyUnknProtTableLastCh.setStatus("current")
_TmnxNatSyslogExpPlcyTableLastCh_Type = TimeStamp
_TmnxNatSyslogExpPlcyTableLastCh_Object = MibScalar
tmnxNatSyslogExpPlcyTableLastCh = _TmnxNatSyslogExpPlcyTableLastCh_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 141),
    _TmnxNatSyslogExpPlcyTableLastCh_Type()
)
tmnxNatSyslogExpPlcyTableLastCh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatSyslogExpPlcyTableLastCh.setStatus("current")
_TmnxNatSyslogColTableLastCh_Type = TimeStamp
_TmnxNatSyslogColTableLastCh_Object = MibScalar
tmnxNatSyslogColTableLastCh = _TmnxNatSyslogColTableLastCh_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 142),
    _TmnxNatSyslogColTableLastCh_Type()
)
tmnxNatSyslogColTableLastCh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatSyslogColTableLastCh.setStatus("current")
_TmnxNatGrpMonOperGrpTableLastCh_Type = TimeStamp
_TmnxNatGrpMonOperGrpTableLastCh_Object = MibScalar
tmnxNatGrpMonOperGrpTableLastCh = _TmnxNatGrpMonOperGrpTableLastCh_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 143),
    _TmnxNatGrpMonOperGrpTableLastCh_Type()
)
tmnxNatGrpMonOperGrpTableLastCh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatGrpMonOperGrpTableLastCh.setStatus("current")
_TmnxNatGrpMonPortTableLastCh_Type = TimeStamp
_TmnxNatGrpMonPortTableLastCh_Object = MibScalar
tmnxNatGrpMonPortTableLastCh = _TmnxNatGrpMonPortTableLastCh_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 144),
    _TmnxNatGrpMonPortTableLastCh_Type()
)
tmnxNatGrpMonPortTableLastCh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatGrpMonPortTableLastCh.setStatus("current")
_TmnxNatVappTableLastCh_Type = TimeStamp
_TmnxNatVappTableLastCh_Object = MibScalar
tmnxNatVappTableLastCh = _TmnxNatVappTableLastCh_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 145),
    _TmnxNatVappTableLastCh_Type()
)
tmnxNatVappTableLastCh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatVappTableLastCh.setStatus("current")
_TmnxNatDetPfxMapTableLastCh_Type = TimeStamp
_TmnxNatDetPfxMapTableLastCh_Object = MibScalar
tmnxNatDetPfxMapTableLastCh = _TmnxNatDetPfxMapTableLastCh_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 148),
    _TmnxNatDetPfxMapTableLastCh_Type()
)
tmnxNatDetPfxMapTableLastCh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatDetPfxMapTableLastCh.setStatus("current")
_TmnxNatDetMap2TableLastCh_Type = TimeStamp
_TmnxNatDetMap2TableLastCh_Object = MibScalar
tmnxNatDetMap2TableLastCh = _TmnxNatDetMap2TableLastCh_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 149),
    _TmnxNatDetMap2TableLastCh_Type()
)
tmnxNatDetMap2TableLastCh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatDetMap2TableLastCh.setStatus("current")
_TmnxNatSourcePrefixTableLastCh_Type = TimeStamp
_TmnxNatSourcePrefixTableLastCh_Object = MibScalar
tmnxNatSourcePrefixTableLastCh = _TmnxNatSourcePrefixTableLastCh_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 150),
    _TmnxNatSourcePrefixTableLastCh_Type()
)
tmnxNatSourcePrefixTableLastCh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatSourcePrefixTableLastCh.setStatus("current")
_TmnxNatDetAddrMapTableLastCh_Type = TimeStamp
_TmnxNatDetAddrMapTableLastCh_Object = MibScalar
tmnxNatDetAddrMapTableLastCh = _TmnxNatDetAddrMapTableLastCh_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 151),
    _TmnxNatDetAddrMapTableLastCh_Type()
)
tmnxNatDetAddrMapTableLastCh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatDetAddrMapTableLastCh.setStatus("current")
_TmnxNatMapTGrpTableLastCh_Type = TimeStamp
_TmnxNatMapTGrpTableLastCh_Object = MibScalar
tmnxNatMapTGrpTableLastCh = _TmnxNatMapTGrpTableLastCh_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 152),
    _TmnxNatMapTGrpTableLastCh_Type()
)
tmnxNatMapTGrpTableLastCh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatMapTGrpTableLastCh.setStatus("current")
_TmnxMapTVappTableLastCh_Type = TimeStamp
_TmnxMapTVappTableLastCh_Object = MibScalar
tmnxMapTVappTableLastCh = _TmnxMapTVappTableLastCh_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 153),
    _TmnxMapTVappTableLastCh_Type()
)
tmnxMapTVappTableLastCh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxMapTVappTableLastCh.setStatus("current")
_TmnxNatPlRangeExclTableLastCh_Type = TimeStamp
_TmnxNatPlRangeExclTableLastCh_Object = MibScalar
tmnxNatPlRangeExclTableLastCh = _TmnxNatPlRangeExclTableLastCh_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 154),
    _TmnxNatPlRangeExclTableLastCh_Type()
)
tmnxNatPlRangeExclTableLastCh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatPlRangeExclTableLastCh.setStatus("current")
_TmnxNatCpmPlcyTableLastCh_Type = TimeStamp
_TmnxNatCpmPlcyTableLastCh_Object = MibScalar
tmnxNatCpmPlcyTableLastCh = _TmnxNatCpmPlcyTableLastCh_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 155),
    _TmnxNatCpmPlcyTableLastCh_Type()
)
tmnxNatCpmPlcyTableLastCh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatCpmPlcyTableLastCh.setStatus("current")
_TmnxNatVrtrSpfPlcyTblLastCh_Type = TimeStamp
_TmnxNatVrtrSpfPlcyTblLastCh_Object = MibScalar
tmnxNatVrtrSpfPlcyTblLastCh = _TmnxNatVrtrSpfPlcyTblLastCh_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 160),
    _TmnxNatVrtrSpfPlcyTblLastCh_Type()
)
tmnxNatVrtrSpfPlcyTblLastCh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatVrtrSpfPlcyTblLastCh.setStatus("current")
_TmnxNatResourceProblem_Type = TruthValue
_TmnxNatResourceProblem_Object = MibScalar
tmnxNatResourceProblem = _TmnxNatResourceProblem_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 200),
    _TmnxNatResourceProblem_Type()
)
tmnxNatResourceProblem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatResourceProblem.setStatus("current")
_TmnxNatLsnSubscIdCount_Type = Gauge32
_TmnxNatLsnSubscIdCount_Object = MibScalar
tmnxNatLsnSubscIdCount = _TmnxNatLsnSubscIdCount_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 201),
    _TmnxNatLsnSubscIdCount_Type()
)
tmnxNatLsnSubscIdCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatLsnSubscIdCount.setStatus("current")
_TmnxNatQryLsnSubMaxQryId_Type = Unsigned32
_TmnxNatQryLsnSubMaxQryId_Object = MibScalar
tmnxNatQryLsnSubMaxQryId = _TmnxNatQryLsnSubMaxQryId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 202),
    _TmnxNatQryLsnSubMaxQryId_Type()
)
tmnxNatQryLsnSubMaxQryId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatQryLsnSubMaxQryId.setStatus("current")
_TmnxNatL2AwHostCount_Type = Gauge32
_TmnxNatL2AwHostCount_Object = MibScalar
tmnxNatL2AwHostCount = _TmnxNatL2AwHostCount_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 203),
    _TmnxNatL2AwHostCount_Type()
)
tmnxNatL2AwHostCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatL2AwHostCount.setStatus("current")
_TmnxNatFwlNbrCount_Type = Gauge32
_TmnxNatFwlNbrCount_Object = MibScalar
tmnxNatFwlNbrCount = _TmnxNatFwlNbrCount_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 204),
    _TmnxNatFwlNbrCount_Type()
)
tmnxNatFwlNbrCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatFwlNbrCount.setStatus("current")
_TmnxNatFwlHostCount_Type = Gauge32
_TmnxNatFwlHostCount_Object = MibScalar
tmnxNatFwlHostCount = _TmnxNatFwlHostCount_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 1, 205),
    _TmnxNatFwlHostCount_Type()
)
tmnxNatFwlHostCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxNatFwlHostCount.setStatus("current")
_TmnxNatNotificationObjs_ObjectIdentity = ObjectIdentity
tmnxNatNotificationObjs = _TmnxNatNotificationObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 2)
)


class _TmnxNatNotifyDescription_Type(DisplayString):
    """Custom type tmnxNatNotifyDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_TmnxNatNotifyDescription_Type.__name__ = "DisplayString"
_TmnxNatNotifyDescription_Object = MibScalar
tmnxNatNotifyDescription = _TmnxNatNotifyDescription_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 2, 1),
    _TmnxNatNotifyDescription_Type()
)
tmnxNatNotifyDescription.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tmnxNatNotifyDescription.setStatus("current")
_TmnxNatNotifyOutsideVRtrID_Type = TmnxVRtrID
_TmnxNatNotifyOutsideVRtrID_Object = MibScalar
tmnxNatNotifyOutsideVRtrID = _TmnxNatNotifyOutsideVRtrID_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 2, 2),
    _TmnxNatNotifyOutsideVRtrID_Type()
)
tmnxNatNotifyOutsideVRtrID.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tmnxNatNotifyOutsideVRtrID.setStatus("current")
_TmnxNatNotifyInsideVRtrID_Type = TmnxVRtrIDOrZero
_TmnxNatNotifyInsideVRtrID_Object = MibScalar
tmnxNatNotifyInsideVRtrID = _TmnxNatNotifyInsideVRtrID_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 2, 3),
    _TmnxNatNotifyInsideVRtrID_Type()
)
tmnxNatNotifyInsideVRtrID.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tmnxNatNotifyInsideVRtrID.setStatus("current")
_TmnxNatNotifyOutsideAddrType_Type = InetAddressType
_TmnxNatNotifyOutsideAddrType_Object = MibScalar
tmnxNatNotifyOutsideAddrType = _TmnxNatNotifyOutsideAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 2, 4),
    _TmnxNatNotifyOutsideAddrType_Type()
)
tmnxNatNotifyOutsideAddrType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tmnxNatNotifyOutsideAddrType.setStatus("current")


class _TmnxNatNotifyOutsideAddr_Type(InetAddress):
    """Custom type tmnxNatNotifyOutsideAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxNatNotifyOutsideAddr_Type.__name__ = "InetAddress"
_TmnxNatNotifyOutsideAddr_Object = MibScalar
tmnxNatNotifyOutsideAddr = _TmnxNatNotifyOutsideAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 2, 5),
    _TmnxNatNotifyOutsideAddr_Type()
)
tmnxNatNotifyOutsideAddr.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tmnxNatNotifyOutsideAddr.setStatus("current")
_TmnxNatNotifyInsideAddrType_Type = InetAddressType
_TmnxNatNotifyInsideAddrType_Object = MibScalar
tmnxNatNotifyInsideAddrType = _TmnxNatNotifyInsideAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 2, 6),
    _TmnxNatNotifyInsideAddrType_Type()
)
tmnxNatNotifyInsideAddrType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tmnxNatNotifyInsideAddrType.setStatus("current")


class _TmnxNatNotifyInsideAddr_Type(InetAddress):
    """Custom type tmnxNatNotifyInsideAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxNatNotifyInsideAddr_Type.__name__ = "InetAddress"
_TmnxNatNotifyInsideAddr_Object = MibScalar
tmnxNatNotifyInsideAddr = _TmnxNatNotifyInsideAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 2, 7),
    _TmnxNatNotifyInsideAddr_Type()
)
tmnxNatNotifyInsideAddr.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tmnxNatNotifyInsideAddr.setStatus("current")
_TmnxNatNotifyPort_Type = InetPortNumber
_TmnxNatNotifyPort_Object = MibScalar
tmnxNatNotifyPort = _TmnxNatNotifyPort_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 2, 8),
    _TmnxNatNotifyPort_Type()
)
tmnxNatNotifyPort.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tmnxNatNotifyPort.setStatus("current")
_TmnxNatNotifyPort2_Type = InetPortNumber
_TmnxNatNotifyPort2_Object = MibScalar
tmnxNatNotifyPort2 = _TmnxNatNotifyPort2_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 2, 9),
    _TmnxNatNotifyPort2_Type()
)
tmnxNatNotifyPort2.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tmnxNatNotifyPort2.setStatus("current")


class _TmnxNatNotifyDateAndTime_Type(DateAndTime):
    """Custom type tmnxNatNotifyDateAndTime based on DateAndTime"""
    subtypeSpec = DateAndTime.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(11, 11),
    )
    fixed_length = 11


_TmnxNatNotifyDateAndTime_Type.__name__ = "DateAndTime"
_TmnxNatNotifyDateAndTime_Object = MibScalar
tmnxNatNotifyDateAndTime = _TmnxNatNotifyDateAndTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 2, 10),
    _TmnxNatNotifyDateAndTime_Type()
)
tmnxNatNotifyDateAndTime.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tmnxNatNotifyDateAndTime.setStatus("current")
_TmnxNatNotifyTruthValue_Type = TruthValue
_TmnxNatNotifyTruthValue_Object = MibScalar
tmnxNatNotifyTruthValue = _TmnxNatNotifyTruthValue_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 2, 11),
    _TmnxNatNotifyTruthValue_Type()
)
tmnxNatNotifyTruthValue.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tmnxNatNotifyTruthValue.setStatus("current")
_TmnxNatNotifyLsnSubId_Type = Unsigned32
_TmnxNatNotifyLsnSubId_Object = MibScalar
tmnxNatNotifyLsnSubId = _TmnxNatNotifyLsnSubId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 2, 13),
    _TmnxNatNotifyLsnSubId_Type()
)
tmnxNatNotifyLsnSubId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tmnxNatNotifyLsnSubId.setStatus("current")


class _TmnxNatNotifyL2AwSubIdent_Type(DisplayString):
    """Custom type tmnxNatNotifyL2AwSubIdent based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_TmnxNatNotifyL2AwSubIdent_Type.__name__ = "DisplayString"
_TmnxNatNotifyL2AwSubIdent_Object = MibScalar
tmnxNatNotifyL2AwSubIdent = _TmnxNatNotifyL2AwSubIdent_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 2, 14),
    _TmnxNatNotifyL2AwSubIdent_Type()
)
tmnxNatNotifyL2AwSubIdent.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tmnxNatNotifyL2AwSubIdent.setStatus("current")
_TmnxNatNotifyOutsideEndAddrType_Type = InetAddressType
_TmnxNatNotifyOutsideEndAddrType_Object = MibScalar
tmnxNatNotifyOutsideEndAddrType = _TmnxNatNotifyOutsideEndAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 2, 15),
    _TmnxNatNotifyOutsideEndAddrType_Type()
)
tmnxNatNotifyOutsideEndAddrType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tmnxNatNotifyOutsideEndAddrType.setStatus("current")


class _TmnxNatNotifyOutsideEndAddr_Type(InetAddress):
    """Custom type tmnxNatNotifyOutsideEndAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxNatNotifyOutsideEndAddr_Type.__name__ = "InetAddress"
_TmnxNatNotifyOutsideEndAddr_Object = MibScalar
tmnxNatNotifyOutsideEndAddr = _TmnxNatNotifyOutsideEndAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 2, 16),
    _TmnxNatNotifyOutsideEndAddr_Type()
)
tmnxNatNotifyOutsideEndAddr.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tmnxNatNotifyOutsideEndAddr.setStatus("current")
_TmnxNatNotifyPlSeqNum_Type = Counter64
_TmnxNatNotifyPlSeqNum_Object = MibScalar
tmnxNatNotifyPlSeqNum = _TmnxNatNotifyPlSeqNum_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 2, 17),
    _TmnxNatNotifyPlSeqNum_Type()
)
tmnxNatNotifyPlSeqNum.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tmnxNatNotifyPlSeqNum.setStatus("current")
_TmnxNatNotifySubscriberType_Type = TmnxNatLegacySubscriberType
_TmnxNatNotifySubscriberType_Object = MibScalar
tmnxNatNotifySubscriberType = _TmnxNatNotifySubscriberType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 2, 20),
    _TmnxNatNotifySubscriberType_Type()
)
tmnxNatNotifySubscriberType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tmnxNatNotifySubscriberType.setStatus("current")
_TmnxNatNotifyMdaChassisIndex_Type = TmnxChassisIndexOrZero
_TmnxNatNotifyMdaChassisIndex_Object = MibScalar
tmnxNatNotifyMdaChassisIndex = _TmnxNatNotifyMdaChassisIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 2, 21),
    _TmnxNatNotifyMdaChassisIndex_Type()
)
tmnxNatNotifyMdaChassisIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tmnxNatNotifyMdaChassisIndex.setStatus("current")
_TmnxNatNotifyMdaCardSlotNum_Type = TmnxSlotNumOrZero
_TmnxNatNotifyMdaCardSlotNum_Object = MibScalar
tmnxNatNotifyMdaCardSlotNum = _TmnxNatNotifyMdaCardSlotNum_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 2, 22),
    _TmnxNatNotifyMdaCardSlotNum_Type()
)
tmnxNatNotifyMdaCardSlotNum.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tmnxNatNotifyMdaCardSlotNum.setStatus("current")
_TmnxNatNotifyMdaSlotNum_Type = Unsigned32
_TmnxNatNotifyMdaSlotNum_Object = MibScalar
tmnxNatNotifyMdaSlotNum = _TmnxNatNotifyMdaSlotNum_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 2, 23),
    _TmnxNatNotifyMdaSlotNum_Type()
)
tmnxNatNotifyMdaSlotNum.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tmnxNatNotifyMdaSlotNum.setStatus("current")
_TmnxNatNotifyCounter_Type = Counter64
_TmnxNatNotifyCounter_Object = MibScalar
tmnxNatNotifyCounter = _TmnxNatNotifyCounter_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 2, 24),
    _TmnxNatNotifyCounter_Type()
)
tmnxNatNotifyCounter.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tmnxNatNotifyCounter.setStatus("current")
_TmnxNatNotifyNumber_Type = Unsigned32
_TmnxNatNotifyNumber_Object = MibScalar
tmnxNatNotifyNumber = _TmnxNatNotifyNumber_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 2, 25),
    _TmnxNatNotifyNumber_Type()
)
tmnxNatNotifyNumber.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tmnxNatNotifyNumber.setStatus("current")


class _TmnxNatNotifyInsideAddrPrefixLen_Type(InetAddressPrefixLength):
    """Custom type tmnxNatNotifyInsideAddrPrefixLen based on InetAddressPrefixLength"""
    subtypeSpec = InetAddressPrefixLength.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 128),
    )


_TmnxNatNotifyInsideAddrPrefixLen_Type.__name__ = "InetAddressPrefixLength"
_TmnxNatNotifyInsideAddrPrefixLen_Object = MibScalar
tmnxNatNotifyInsideAddrPrefixLen = _TmnxNatNotifyInsideAddrPrefixLen_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 2, 26),
    _TmnxNatNotifyInsideAddrPrefixLen_Type()
)
tmnxNatNotifyInsideAddrPrefixLen.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tmnxNatNotifyInsideAddrPrefixLen.setStatus("current")
_TmnxNatNotifyName_Type = TNamedItemOrEmpty
_TmnxNatNotifyName_Object = MibScalar
tmnxNatNotifyName = _TmnxNatNotifyName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 2, 27),
    _TmnxNatNotifyName_Type()
)
tmnxNatNotifyName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tmnxNatNotifyName.setStatus("current")
_TmnxNatNotifyIsaGrpId_Type = TmnxNatIsaGrpId
_TmnxNatNotifyIsaGrpId_Object = MibScalar
tmnxNatNotifyIsaGrpId = _TmnxNatNotifyIsaGrpId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 2, 28),
    _TmnxNatNotifyIsaGrpId_Type()
)
tmnxNatNotifyIsaGrpId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tmnxNatNotifyIsaGrpId.setStatus("current")
_TmnxNatNotifyIsaMemberId_Type = Unsigned32
_TmnxNatNotifyIsaMemberId_Object = MibScalar
tmnxNatNotifyIsaMemberId = _TmnxNatNotifyIsaMemberId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 2, 29),
    _TmnxNatNotifyIsaMemberId_Type()
)
tmnxNatNotifyIsaMemberId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tmnxNatNotifyIsaMemberId.setStatus("current")
_TmnxNatNotifyMemberSubOrHostType_Type = TmnxNatMemberSubOrHostType
_TmnxNatNotifyMemberSubOrHostType_Object = MibScalar
tmnxNatNotifyMemberSubOrHostType = _TmnxNatNotifyMemberSubOrHostType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 2, 30),
    _TmnxNatNotifyMemberSubOrHostType_Type()
)
tmnxNatNotifyMemberSubOrHostType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tmnxNatNotifyMemberSubOrHostType.setStatus("current")
_TmnxNatNotifyMemberSubOrHostDesc_Type = TItemDescription
_TmnxNatNotifyMemberSubOrHostDesc_Object = MibScalar
tmnxNatNotifyMemberSubOrHostDesc = _TmnxNatNotifyMemberSubOrHostDesc_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 2, 31),
    _TmnxNatNotifyMemberSubOrHostDesc_Type()
)
tmnxNatNotifyMemberSubOrHostDesc.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tmnxNatNotifyMemberSubOrHostDesc.setStatus("current")
_TmnxNatNotifyIsaMemberEsaNum_Type = TmnxEsaNum
_TmnxNatNotifyIsaMemberEsaNum_Object = MibScalar
tmnxNatNotifyIsaMemberEsaNum = _TmnxNatNotifyIsaMemberEsaNum_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 2, 32),
    _TmnxNatNotifyIsaMemberEsaNum_Type()
)
tmnxNatNotifyIsaMemberEsaNum.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tmnxNatNotifyIsaMemberEsaNum.setStatus("current")
_TmnxNatNotifyIsaMemberEsaVappNum_Type = TmnxEsaVappNum
_TmnxNatNotifyIsaMemberEsaVappNum_Object = MibScalar
tmnxNatNotifyIsaMemberEsaVappNum = _TmnxNatNotifyIsaMemberEsaVappNum_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 2, 33),
    _TmnxNatNotifyIsaMemberEsaVappNum_Type()
)
tmnxNatNotifyIsaMemberEsaVappNum.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tmnxNatNotifyIsaMemberEsaVappNum.setStatus("current")
_TmnxNatNotifyPoolName_Type = TNamedItem
_TmnxNatNotifyPoolName_Object = MibScalar
tmnxNatNotifyPoolName = _TmnxNatNotifyPoolName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 2, 34),
    _TmnxNatNotifyPoolName_Type()
)
tmnxNatNotifyPoolName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tmnxNatNotifyPoolName.setStatus("current")
_TmnxNatNotifyOutsideIPv4AddrType_Type = InetAddressType
_TmnxNatNotifyOutsideIPv4AddrType_Object = MibScalar
tmnxNatNotifyOutsideIPv4AddrType = _TmnxNatNotifyOutsideIPv4AddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 2, 35),
    _TmnxNatNotifyOutsideIPv4AddrType_Type()
)
tmnxNatNotifyOutsideIPv4AddrType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tmnxNatNotifyOutsideIPv4AddrType.setStatus("current")


class _TmnxNatNotifyOutsideIPv4Addr_Type(InetAddress):
    """Custom type tmnxNatNotifyOutsideIPv4Addr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )
    fixed_length = 4


_TmnxNatNotifyOutsideIPv4Addr_Type.__name__ = "InetAddress"
_TmnxNatNotifyOutsideIPv4Addr_Object = MibScalar
tmnxNatNotifyOutsideIPv4Addr = _TmnxNatNotifyOutsideIPv4Addr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 2, 36),
    _TmnxNatNotifyOutsideIPv4Addr_Type()
)
tmnxNatNotifyOutsideIPv4Addr.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tmnxNatNotifyOutsideIPv4Addr.setStatus("current")
_TmnxNatNotifyMbrExPrtBlckUsageHi_Type = TruthValue
_TmnxNatNotifyMbrExPrtBlckUsageHi_Object = MibScalar
tmnxNatNotifyMbrExPrtBlckUsageHi = _TmnxNatNotifyMbrExPrtBlckUsageHi_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 2, 37),
    _TmnxNatNotifyMbrExPrtBlckUsageHi_Type()
)
tmnxNatNotifyMbrExPrtBlckUsageHi.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tmnxNatNotifyMbrExPrtBlckUsageHi.setStatus("current")
_TmnxNatNotifyPolicyIndex_Type = Unsigned32
_TmnxNatNotifyPolicyIndex_Object = MibScalar
tmnxNatNotifyPolicyIndex = _TmnxNatNotifyPolicyIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 2, 38),
    _TmnxNatNotifyPolicyIndex_Type()
)
tmnxNatNotifyPolicyIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tmnxNatNotifyPolicyIndex.setStatus("current")
_TmnxNatNotifyPlLsnMbrPortUsageHi_Type = TruthValue
_TmnxNatNotifyPlLsnMbrPortUsageHi_Object = MibScalar
tmnxNatNotifyPlLsnMbrPortUsageHi = _TmnxNatNotifyPlLsnMbrPortUsageHi_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 2, 39),
    _TmnxNatNotifyPlLsnMbrPortUsageHi_Type()
)
tmnxNatNotifyPlLsnMbrPortUsageHi.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tmnxNatNotifyPlLsnMbrPortUsageHi.setStatus("current")


class _TmnxNatNotifyPlLsnMbrProtocol_Type(Integer32):
    """Custom type tmnxNatNotifyPlLsnMbrProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("tcp", 1),
          ("udp", 2),
          ("other", 3))
    )


_TmnxNatNotifyPlLsnMbrProtocol_Type.__name__ = "Integer32"
_TmnxNatNotifyPlLsnMbrProtocol_Object = MibScalar
tmnxNatNotifyPlLsnMbrProtocol = _TmnxNatNotifyPlLsnMbrProtocol_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 2, 40),
    _TmnxNatNotifyPlLsnMbrProtocol_Type()
)
tmnxNatNotifyPlLsnMbrProtocol.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tmnxNatNotifyPlLsnMbrProtocol.setStatus("current")
_TmnxNatNotifyInterimUpdate_Type = TruthValue
_TmnxNatNotifyInterimUpdate_Object = MibScalar
tmnxNatNotifyInterimUpdate = _TmnxNatNotifyInterimUpdate_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 65, 2, 41),
    _TmnxNatNotifyInterimUpdate_Type()
)
tmnxNatNotifyInterimUpdate.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tmnxNatNotifyInterimUpdate.setStatus("current")
_TmnxNatNotifyPrefix_ObjectIdentity = ObjectIdentity
tmnxNatNotifyPrefix = _TmnxNatNotifyPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 65)
)
_TmnxNatNotifications_ObjectIdentity = ObjectIdentity
tmnxNatNotifications = _TmnxNatNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 65, 0)
)
tmnxNatIsaMdaEntry.registerAugmentions(
    ("TIMETRA-NAT-MIB",
     "tmnxNatIsaMdaStatEntry")
)
tmnxNatIsaMdaStatEntry.setIndexNames(*tmnxNatIsaMdaEntry.getIndexNames())
tmnxNatMemSicrStateEntry.registerAugmentions(
    ("TIMETRA-NAT-MIB",
     "tmnxNatMemSicrStatsEntry")
)
tmnxNatMemSicrStatsEntry.setIndexNames(*tmnxNatMemSicrStateEntry.getIndexNames())
tmnxNatVappEntry.registerAugmentions(
    ("TIMETRA-NAT-MIB",
     "tmnxNatVappStatEntry")
)
tmnxNatVappStatEntry.setIndexNames(*tmnxNatVappEntry.getIndexNames())
tmnxNatGrpSicrStateEntry.registerAugmentions(
    ("TIMETRA-NAT-MIB",
     "tmnxNatGrpSicrStatsEntry")
)
tmnxNatGrpSicrStatsEntry.setIndexNames(*tmnxNatGrpSicrStateEntry.getIndexNames())
tmnxNatVrtrEntry.registerAugmentions(
    ("TIMETRA-NAT-MIB",
     "tmnxNatSubIdEntry")
)
tmnxNatSubIdEntry.setIndexNames(*tmnxNatVrtrEntry.getIndexNames())
tmnxNatPlRangeEntry.registerAugmentions(
    ("TIMETRA-NAT-MIB",
     "tmnxNatPlRangeStatEntry")
)
tmnxNatPlRangeStatEntry.setIndexNames(*tmnxNatPlRangeEntry.getIndexNames())
tmnxNatLsnSubEntry.registerAugmentions(
    ("TIMETRA-NAT-MIB",
     "tmnxNatLsnSubStatEntry")
)
tmnxNatLsnSubStatEntry.setIndexNames(*tmnxNatLsnSubEntry.getIndexNames())
tmnxNatUpnpPlcyEntry.registerAugmentions(
    ("TIMETRA-NAT-MIB",
     "tmnxNatUpnpPlcyStatEntry")
)
tmnxNatUpnpPlcyStatEntry.setIndexNames(*tmnxNatUpnpPlcyEntry.getIndexNames())
tmnxNatMapDomEntry.registerAugmentions(
    ("TIMETRA-NAT-MIB",
     "tmnxNatMapDomStatsEntry")
)
tmnxNatMapDomStatsEntry.setIndexNames(*tmnxNatMapDomEntry.getIndexNames())
tmnxNatMapRuleEntry.registerAugmentions(
    ("TIMETRA-NAT-MIB",
     "tmnxNatMapRuleStatsEntry")
)
tmnxNatMapRuleStatsEntry.setIndexNames(*tmnxNatMapRuleEntry.getIndexNames())
tmnxNatMapDomEntry.registerAugmentions(
    ("TIMETRA-NAT-MIB",
     "tmnxNatMapDomFPStatsEntry")
)
tmnxNatMapDomFPStatsEntry.setIndexNames(*tmnxNatMapDomEntry.getIndexNames())
tmnxNatMapRuleEntry.registerAugmentions(
    ("TIMETRA-NAT-MIB",
     "tmnxNatMapRuleFPStatsEntry")
)
tmnxNatMapRuleFPStatsEntry.setIndexNames(*tmnxNatMapRuleEntry.getIndexNames())

# Managed Objects groups

tmnxNatIsaGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 65, 2, 1)
)
tmnxNatIsaGroup.setObjects(
      *(("TIMETRA-NAT-MIB", "tmnxNatIsaGrpTableLastCh"),
        ("TIMETRA-NAT-MIB", "tmnxNatIsaGrpRowStatus"),
        ("TIMETRA-NAT-MIB", "tmnxNatIsaGrpLastMgmtChange"),
        ("TIMETRA-NAT-MIB", "tmnxNatIsaGrpDescription"),
        ("TIMETRA-NAT-MIB", "tmnxNatIsaGrpAdminState"),
        ("TIMETRA-NAT-MIB", "tmnxNatIsaGrpActiveMdaLimit"),
        ("TIMETRA-NAT-MIB", "tmnxNatIsaGrpOperState"),
        ("TIMETRA-NAT-MIB", "tmnxNatIsaMdaTableLastCh"),
        ("TIMETRA-NAT-MIB", "tmnxNatIsaMdaRowStatus"),
        ("TIMETRA-NAT-MIB", "tmnxNatIsaMdaLastMgmtChange"))
)
if mibBuilder.loadTexts:
    tmnxNatIsaGroup.setStatus("obsolete")

tmnxNatIsaStatGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 65, 2, 2)
)
tmnxNatIsaStatGroup.setObjects(
      *(("TIMETRA-NAT-MIB", "tmnxNatIsaMdaStatTableLastCh"),
        ("TIMETRA-NAT-MIB", "tmnxNatIsaMdaStatOperState"),
        ("TIMETRA-NAT-MIB", "tmnxNatIsaMemberMdaState"),
        ("TIMETRA-NAT-MIB", "tmnxNatIsaMemberMdaChassisIndex"),
        ("TIMETRA-NAT-MIB", "tmnxNatIsaMemberMdaCardSlotNum"),
        ("TIMETRA-NAT-MIB", "tmnxNatIsaMemberMdaSlotNum"),
        ("TIMETRA-NAT-MIB", "tmnxNatIsaMemberIpAddrReserved"),
        ("TIMETRA-NAT-MIB", "tmnxNatIsaMemberBlocksReserved"),
        ("TIMETRA-NAT-MIB", "tmnxNatIsaMemberSessionUsage"),
        ("TIMETRA-NAT-MIB", "tmnxNatIsaMemberSessionUsageHi"),
        ("TIMETRA-NAT-MIB", "tmnxNatIsaMemberSessionsPrio"),
        ("TIMETRA-NAT-MIB", "tmnxNatIsaMemberStatsName"),
        ("TIMETRA-NAT-MIB", "tmnxNatIsaMemberStatsVal"),
        ("TIMETRA-NAT-MIB", "tmnxNatResourceProblem"))
)
if mibBuilder.loadTexts:
    tmnxNatIsaStatGroup.setStatus("current")

tmnxNatPlcyGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 65, 2, 3)
)
tmnxNatPlcyGroup.setObjects(
      *(("TIMETRA-NAT-MIB", "tmnxNatPlcyTableLastCh"),
        ("TIMETRA-NAT-MIB", "tmnxNatVrtrTableLastCh"),
        ("TIMETRA-NAT-MIB", "tmnxNatPlcyLastMgmtChange"),
        ("TIMETRA-NAT-MIB", "tmnxNatPlcyRowStatus"),
        ("TIMETRA-NAT-MIB", "tmnxNatPlcyDescription"),
        ("TIMETRA-NAT-MIB", "tmnxNatPlcyPool"),
        ("TIMETRA-NAT-MIB", "tmnxNatPlcyPoolVRtr"),
        ("TIMETRA-NAT-MIB", "tmnxNatPlcyFiltering"),
        ("TIMETRA-NAT-MIB", "tmnxNatPlcyPortResvCount"),
        ("TIMETRA-NAT-MIB", "tmnxNatPlcyPortWatermarkHigh"),
        ("TIMETRA-NAT-MIB", "tmnxNatPlcyPortWatermarkLow"),
        ("TIMETRA-NAT-MIB", "tmnxNatPlcySessionLimit"),
        ("TIMETRA-NAT-MIB", "tmnxNatPlcySessionResvCount"),
        ("TIMETRA-NAT-MIB", "tmnxNatPlcySessionWatermarkHigh"),
        ("TIMETRA-NAT-MIB", "tmnxNatPlcySessionWatermarkLow"),
        ("TIMETRA-NAT-MIB", "tmnxNatPlcyPrioSessionFcSet"),
        ("TIMETRA-NAT-MIB", "tmnxNatPlcyToTcpEstab"),
        ("TIMETRA-NAT-MIB", "tmnxNatPlcyToTcpTrans"),
        ("TIMETRA-NAT-MIB", "tmnxNatPlcyToTcpSyn"),
        ("TIMETRA-NAT-MIB", "tmnxNatPlcyToTcpTimeWait"),
        ("TIMETRA-NAT-MIB", "tmnxNatPlcyToUdp"),
        ("TIMETRA-NAT-MIB", "tmnxNatPlcyToUdpInitial"),
        ("TIMETRA-NAT-MIB", "tmnxNatPlcyToUdpDns"),
        ("TIMETRA-NAT-MIB", "tmnxNatPlcyToIcmpQuery"))
)
if mibBuilder.loadTexts:
    tmnxNatPlcyGroup.setStatus("current")

tmnxNatPlcyStatGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 65, 2, 4)
)
tmnxNatPlcyStatGroup.setObjects(
      *(("TIMETRA-NAT-MIB", "tmnxNatPlcyStatsName"),
        ("TIMETRA-NAT-MIB", "tmnxNatPlcyStatsVal"))
)
if mibBuilder.loadTexts:
    tmnxNatPlcyStatGroup.setStatus("current")

tmnxNatVrtrGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 65, 2, 5)
)
tmnxNatVrtrGroup.setObjects(
      *(("TIMETRA-NAT-MIB", "tmnxNatVrtrTableLastCh"),
        ("TIMETRA-NAT-MIB", "tmnxNatVrtrLastMgmtChange"),
        ("TIMETRA-NAT-MIB", "tmnxNatVrtrRowStatus"),
        ("TIMETRA-NAT-MIB", "tmnxNatVrtrInPolicy"))
)
if mibBuilder.loadTexts:
    tmnxNatVrtrGroup.setStatus("current")

tmnxNatPlGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 65, 2, 6)
)
tmnxNatPlGroup.setObjects(
      *(("TIMETRA-NAT-MIB", "tmnxNatPlTableLastCh"),
        ("TIMETRA-NAT-MIB", "tmnxNatPlRowStatus"),
        ("TIMETRA-NAT-MIB", "tmnxNatPlLastMgmtChange"),
        ("TIMETRA-NAT-MIB", "tmnxNatPlIsaGrp"),
        ("TIMETRA-NAT-MIB", "tmnxNatPlType"),
        ("TIMETRA-NAT-MIB", "tmnxNatPlDescription"),
        ("TIMETRA-NAT-MIB", "tmnxNatPlAdminState"),
        ("TIMETRA-NAT-MIB", "tmnxNatPlPortResvType"),
        ("TIMETRA-NAT-MIB", "tmnxNatPlPortResvVal"),
        ("TIMETRA-NAT-MIB", "tmnxNatPlPortResvAllowPrivileged"),
        ("TIMETRA-NAT-MIB", "tmnxNatPlWatermarkHigh"),
        ("TIMETRA-NAT-MIB", "tmnxNatPlWatermarkLow"),
        ("TIMETRA-NAT-MIB", "tmnxNatPlRangeTableLastCh"),
        ("TIMETRA-NAT-MIB", "tmnxNatPlRangeRowStatus"),
        ("TIMETRA-NAT-MIB", "tmnxNatPlRangeLastMgmtChange"),
        ("TIMETRA-NAT-MIB", "tmnxNatPlRangeDescription"),
        ("TIMETRA-NAT-MIB", "tmnxNatPlRangeAdminDrain"),
        ("TIMETRA-NAT-MIB", "tmnxNatPlRangeNumAllocatedBlk"))
)
if mibBuilder.loadTexts:
    tmnxNatPlGroup.setStatus("obsolete")

tmnxNatDestGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 65, 2, 7)
)
tmnxNatDestGroup.setObjects(
      *(("TIMETRA-NAT-MIB", "tmnxNatDestTableLastCh"),
        ("TIMETRA-NAT-MIB", "tmnxNatDestRowStatus"),
        ("TIMETRA-NAT-MIB", "tmnxNatDestLastMgmtChange"))
)
if mibBuilder.loadTexts:
    tmnxNatDestGroup.setStatus("current")

tmnxNatL2AwGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 65, 2, 8)
)
tmnxNatL2AwGroup.setObjects(
      *(("TIMETRA-NAT-MIB", "tmnxNatL2AwAddrTableLastCh"),
        ("TIMETRA-NAT-MIB", "tmnxNatL2AwAddrRowStatus"),
        ("TIMETRA-NAT-MIB", "tmnxNatL2AwAddrLastMgmtChange"),
        ("TIMETRA-NAT-MIB", "tmnxNatPlL2AwBlockUsage"),
        ("TIMETRA-NAT-MIB", "tmnxNatPlL2AwBlockUsageHi"),
        ("TIMETRA-NAT-MIB", "tmnxNatBlkL2AwEnd"),
        ("TIMETRA-NAT-MIB", "tmnxNatBlkL2AwPool"),
        ("TIMETRA-NAT-MIB", "tmnxNatBlkL2AwSubIdent"),
        ("TIMETRA-NAT-MIB", "tmnxNatBlkL2AwPolicy"),
        ("TIMETRA-NAT-MIB", "tmnxNatBlkL2AwStartDateAndTime"),
        ("TIMETRA-NAT-MIB", "tmnxNatL2AwHostOutVRtrID"),
        ("TIMETRA-NAT-MIB", "tmnxNatL2AwHostOutAddrType"),
        ("TIMETRA-NAT-MIB", "tmnxNatL2AwHostOutAddr"),
        ("TIMETRA-NAT-MIB", "tmnxNatL2AwHostOutStart"),
        ("TIMETRA-NAT-MIB", "tmnxNatL2AwSubPolicy"),
        ("TIMETRA-NAT-MIB", "tmnxNatL2AwSubIsaGrp"),
        ("TIMETRA-NAT-MIB", "tmnxNatL2AwSubIsaMemberId"),
        ("TIMETRA-NAT-MIB", "tmnxNatL2AwSubOutVRtrID"),
        ("TIMETRA-NAT-MIB", "tmnxNatL2AwSubOutAddrType"),
        ("TIMETRA-NAT-MIB", "tmnxNatL2AwSubOutAddr"),
        ("TIMETRA-NAT-MIB", "tmnxNatL2AwSubStatIcmpPortUsage"),
        ("TIMETRA-NAT-MIB", "tmnxNatL2AwSubStatIcmpPortUsageH"),
        ("TIMETRA-NAT-MIB", "tmnxNatL2AwSubStatUdpPortUsage"),
        ("TIMETRA-NAT-MIB", "tmnxNatL2AwSubStatUdpPortUsageHi"),
        ("TIMETRA-NAT-MIB", "tmnxNatL2AwSubStatTcpPortUsage"),
        ("TIMETRA-NAT-MIB", "tmnxNatL2AwSubStatTcpPortUsageHi"),
        ("TIMETRA-NAT-MIB", "tmnxNatL2AwSubStatSessionUsage"),
        ("TIMETRA-NAT-MIB", "tmnxNatL2AwSubStatSessionUsageHi"),
        ("TIMETRA-NAT-MIB", "tmnxNatL2AwSubStatSessions"),
        ("TIMETRA-NAT-MIB", "tmnxNatL2AwSubStatSessionsPrio"),
        ("TIMETRA-NAT-MIB", "tmnxNatL2AwSubStatSessionsPeak"),
        ("TIMETRA-NAT-MIB", "tmnxNatL2AwSubBlkEnd"))
)
if mibBuilder.loadTexts:
    tmnxNatL2AwGroup.setStatus("obsolete")

tmnxNatLsnGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 65, 2, 9)
)
tmnxNatLsnGroup.setObjects(
      *(("TIMETRA-NAT-MIB", "tmnxNatPlLsnMemberIsaGrpId"),
        ("TIMETRA-NAT-MIB", "tmnxNatPlLsnMemberBlockUsage"),
        ("TIMETRA-NAT-MIB", "tmnxNatPlLsnMemberBlockUsageHi"),
        ("TIMETRA-NAT-MIB", "tmnxNatBlkLsnEnd"),
        ("TIMETRA-NAT-MIB", "tmnxNatBlkLsnPool"),
        ("TIMETRA-NAT-MIB", "tmnxNatBlkLsnSubId"),
        ("TIMETRA-NAT-MIB", "tmnxNatBlkLsnInsideVRtrID"),
        ("TIMETRA-NAT-MIB", "tmnxNatBlkLsnInsideAddrType"),
        ("TIMETRA-NAT-MIB", "tmnxNatBlkLsnInsideAddr"),
        ("TIMETRA-NAT-MIB", "tmnxNatBlkLsnPolicy"),
        ("TIMETRA-NAT-MIB", "tmnxNatBlkLsnStartDateAndTime"),
        ("TIMETRA-NAT-MIB", "tmnxNatLsnHostSubId"),
        ("TIMETRA-NAT-MIB", "tmnxNatLsnHostOutVRtrID"),
        ("TIMETRA-NAT-MIB", "tmnxNatLsnHostOutAddrType"),
        ("TIMETRA-NAT-MIB", "tmnxNatLsnHostOutAddr"),
        ("TIMETRA-NAT-MIB", "tmnxNatLsnSubPolicy"),
        ("TIMETRA-NAT-MIB", "tmnxNatLsnSubIsaGrp"),
        ("TIMETRA-NAT-MIB", "tmnxNatLsnSubIsaMemberId"),
        ("TIMETRA-NAT-MIB", "tmnxNatLsnSubOutVRtrID"),
        ("TIMETRA-NAT-MIB", "tmnxNatLsnSubOutAddrType"),
        ("TIMETRA-NAT-MIB", "tmnxNatLsnSubOutAddr"),
        ("TIMETRA-NAT-MIB", "tmnxNatLsnSubStatIcmpPortUsage"),
        ("TIMETRA-NAT-MIB", "tmnxNatLsnSubStatIcmpPortUsageHi"),
        ("TIMETRA-NAT-MIB", "tmnxNatLsnSubStatUdpPortUsage"),
        ("TIMETRA-NAT-MIB", "tmnxNatLsnSubStatUdpPortUsageHi"),
        ("TIMETRA-NAT-MIB", "tmnxNatLsnSubStatTcpPortUsage"),
        ("TIMETRA-NAT-MIB", "tmnxNatLsnSubStatTcpPortUsageHi"),
        ("TIMETRA-NAT-MIB", "tmnxNatLsnSubStatSessionUsage"),
        ("TIMETRA-NAT-MIB", "tmnxNatLsnSubStatSessionUsageHi"),
        ("TIMETRA-NAT-MIB", "tmnxNatLsnSubStatSessions"),
        ("TIMETRA-NAT-MIB", "tmnxNatLsnSubStatSessionsPrio"),
        ("TIMETRA-NAT-MIB", "tmnxNatLsnSubStatSessionsPeak"),
        ("TIMETRA-NAT-MIB", "tmnxNatLsnSubBlkEnd"))
)
if mibBuilder.loadTexts:
    tmnxNatLsnGroup.setStatus("obsolete")

tmnxNatMapGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 65, 2, 10)
)
tmnxNatMapGroup.setObjects(
      *(("TIMETRA-NAT-MIB", "tmnxNatMapLsnHostTableLastCh"),
        ("TIMETRA-NAT-MIB", "tmnxNatMapLsnHostRowStatus"),
        ("TIMETRA-NAT-MIB", "tmnxNatMapLsnHostLastMgmtChange"),
        ("TIMETRA-NAT-MIB", "tmnxNatMapLsnHostAdminState"),
        ("TIMETRA-NAT-MIB", "tmnxNatMapLsnHostOutAddrType"),
        ("TIMETRA-NAT-MIB", "tmnxNatMapLsnHostOutAddr"),
        ("TIMETRA-NAT-MIB", "tmnxNatMapLsnHostOutVRtrID"),
        ("TIMETRA-NAT-MIB", "tmnxNatMapTableLastCh"),
        ("TIMETRA-NAT-MIB", "tmnxNatMapRowStatus"),
        ("TIMETRA-NAT-MIB", "tmnxNatMapLastMgmtChange"),
        ("TIMETRA-NAT-MIB", "tmnxNatMapOutPort"))
)
if mibBuilder.loadTexts:
    tmnxNatMapGroup.setStatus("obsolete")

tmnxNatLsnV9v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 65, 2, 15)
)
tmnxNatLsnV9v0Group.setObjects(
      *(("TIMETRA-NAT-MIB", "tmnxNatPlLsnSubscriberLimit"),
        ("TIMETRA-NAT-MIB", "tmnxNatPlcyBlkLimit"),
        ("TIMETRA-NAT-MIB", "tmnxNatPlMode"),
        ("TIMETRA-NAT-MIB", "tmnxNatDsliteSubId"),
        ("TIMETRA-NAT-MIB", "tmnxNatDsliteAddrTableLastCh"),
        ("TIMETRA-NAT-MIB", "tmnxNatDsliteAddrRowStatus"),
        ("TIMETRA-NAT-MIB", "tmnxNatDsliteAddrLastMgmtChange"),
        ("TIMETRA-NAT-MIB", "tmnxNatDsliteAddrTunnelMtu"))
)
if mibBuilder.loadTexts:
    tmnxNatLsnV9v0Group.setStatus("obsolete")

tmnxNatVrtrV9v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 65, 2, 16)
)
tmnxNatVrtrV9v0Group.setObjects(
      *(("TIMETRA-NAT-MIB", "tmnxNatVrtrInDsliteAdminState"),
        ("TIMETRA-NAT-MIB", "tmnxNatVrtrInDsliteSubPrefixLen"),
        ("TIMETRA-NAT-MIB", "tmnxNatVrtrOutMtu"))
)
if mibBuilder.loadTexts:
    tmnxNatVrtrV9v0Group.setStatus("current")

tmnxNatPlcyV9v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 65, 2, 17)
)
tmnxNatPlcyV9v0Group.setObjects(
      *(("TIMETRA-NAT-MIB", "tmnxNatPlcyToSip"),
        ("TIMETRA-NAT-MIB", "tmnxNatPlcyAlgEnable"),
        ("TIMETRA-NAT-MIB", "tmnxNatPlcyPortFwdLimit"),
        ("TIMETRA-NAT-MIB", "tmnxNatPlcyUdpInboundRefresh"))
)
if mibBuilder.loadTexts:
    tmnxNatPlcyV9v0Group.setStatus("current")

tmnxNatFwdGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 65, 2, 18)
)
tmnxNatFwdGroup.setObjects(
      *(("TIMETRA-NAT-MIB", "tmnxNatFwdOutVRtrID"),
        ("TIMETRA-NAT-MIB", "tmnxNatFwdOutAddrType"),
        ("TIMETRA-NAT-MIB", "tmnxNatFwdOutAddr"),
        ("TIMETRA-NAT-MIB", "tmnxNatFwdOutPort"),
        ("TIMETRA-NAT-MIB", "tmnxNatFwdExpiryDateAndTime"),
        ("TIMETRA-NAT-MIB", "tmnxNatFwdLsnAftrAddrType"),
        ("TIMETRA-NAT-MIB", "tmnxNatFwdLsnAftrAddr"),
        ("TIMETRA-NAT-MIB", "tmnxNatFwdPersistKey"))
)
if mibBuilder.loadTexts:
    tmnxNatFwdGroup.setStatus("obsolete")

tmnxNatPlV9v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 65, 2, 19)
)
tmnxNatPlV9v0Group.setObjects(
      *(("TIMETRA-NAT-MIB", "tmnxNatPlPortFwdRangeEnd"),
        ("TIMETRA-NAT-MIB", "tmnxNatPlOperMode"))
)
if mibBuilder.loadTexts:
    tmnxNatPlV9v0Group.setStatus("obsolete")

tmnxNatRedGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 65, 2, 20)
)
tmnxNatRedGroup.setObjects(
      *(("TIMETRA-NAT-MIB", "tmnxNatVrtrInRedPeerAddrType"),
        ("TIMETRA-NAT-MIB", "tmnxNatVrtrInRedPeerAddr"),
        ("TIMETRA-NAT-MIB", "tmnxNatVrtrInRedPeer6AddrType"),
        ("TIMETRA-NAT-MIB", "tmnxNatVrtrInRedPeer6Addr"),
        ("TIMETRA-NAT-MIB", "tmnxNatVrtrInRedSteerRtType"),
        ("TIMETRA-NAT-MIB", "tmnxNatVrtrInRedSteerRt"),
        ("TIMETRA-NAT-MIB", "tmnxNatVrtrInRedSteerRtLen"),
        ("TIMETRA-NAT-MIB", "tmnxNatPlLsnRedExpPrefixType"),
        ("TIMETRA-NAT-MIB", "tmnxNatPlLsnRedExpPrefix"),
        ("TIMETRA-NAT-MIB", "tmnxNatPlLsnRedExpPrefixLen"),
        ("TIMETRA-NAT-MIB", "tmnxNatPlLsnRedMonPrefixType"),
        ("TIMETRA-NAT-MIB", "tmnxNatPlLsnRedMonPrefix"),
        ("TIMETRA-NAT-MIB", "tmnxNatPlLsnRedMonPrefixLen"),
        ("TIMETRA-NAT-MIB", "tmnxNatPlLsnRedActive"))
)
if mibBuilder.loadTexts:
    tmnxNatRedGroup.setStatus("current")

tmnxNatPlcyV10v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 65, 2, 22)
)
tmnxNatPlcyV10v0Group.setObjects(
      *(("TIMETRA-NAT-MIB", "tmnxNatPlcyIpfixExpPlcy"),
        ("TIMETRA-NAT-MIB", "tmnxNatPlcyTcpMssAdjust"),
        ("TIMETRA-NAT-MIB", "tmnxNatPlcyToSubRetention"))
)
if mibBuilder.loadTexts:
    tmnxNatPlcyV10v0Group.setStatus("current")

tmnxNatIsaV10v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 65, 2, 23)
)
tmnxNatIsaV10v0Group.setObjects(
      *(("TIMETRA-NAT-MIB", "tmnxNatIsaGrpTableLastCh"),
        ("TIMETRA-NAT-MIB", "tmnxNatIsaGrpRowStatus"),
        ("TIMETRA-NAT-MIB", "tmnxNatIsaGrpLastMgmtChange"),
        ("TIMETRA-NAT-MIB", "tmnxNatIsaGrpDescription"),
        ("TIMETRA-NAT-MIB", "tmnxNatIsaGrpAdminState"),
        ("TIMETRA-NAT-MIB", "tmnxNatIsaGrpActiveMdaLimit"),
        ("TIMETRA-NAT-MIB", "tmnxNatIsaGrpOperState"),
        ("TIMETRA-NAT-MIB", "tmnxNatIsaMdaTableLastCh"),
        ("TIMETRA-NAT-MIB", "tmnxNatIsaMdaRowStatus"),
        ("TIMETRA-NAT-MIB", "tmnxNatIsaMdaLastMgmtChange"))
)
if mibBuilder.loadTexts:
    tmnxNatIsaV10v0Group.setStatus("obsolete")

tmnxNatAccGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 65, 2, 24)
)
tmnxNatAccGroup.setObjects(
      *(("TIMETRA-NAT-MIB", "tmnxNatGrpCfgAccountingPlcy"),
        ("TIMETRA-NAT-MIB", "tmnxNatApTableLastCh"),
        ("TIMETRA-NAT-MIB", "tmnxNatApLastMgmtChange"),
        ("TIMETRA-NAT-MIB", "tmnxNatApRowStatus"),
        ("TIMETRA-NAT-MIB", "tmnxNatApDescription"),
        ("TIMETRA-NAT-MIB", "tmnxNatApIncludeAttributes"),
        ("TIMETRA-NAT-MIB", "tmnxNatApServersTimeout"),
        ("TIMETRA-NAT-MIB", "tmnxNatApServersRetry"),
        ("TIMETRA-NAT-MIB", "tmnxNatApServersVRtrID"),
        ("TIMETRA-NAT-MIB", "tmnxNatApServersSrcAddrType"),
        ("TIMETRA-NAT-MIB", "tmnxNatApServersSrcAddrStart"),
        ("TIMETRA-NAT-MIB", "tmnxNatApServersSrcAddrEnd"),
        ("TIMETRA-NAT-MIB", "tmnxNatApServersAlgorithm"),
        ("TIMETRA-NAT-MIB", "tmnxNatApServTableLastCh"),
        ("TIMETRA-NAT-MIB", "tmnxNatApServRowStatus"),
        ("TIMETRA-NAT-MIB", "tmnxNatApServLastMgmtChange"),
        ("TIMETRA-NAT-MIB", "tmnxNatApServAddrType"),
        ("TIMETRA-NAT-MIB", "tmnxNatApServAddr"),
        ("TIMETRA-NAT-MIB", "tmnxNatApServSecret"),
        ("TIMETRA-NAT-MIB", "tmnxNatApServAcctPort"),
        ("TIMETRA-NAT-MIB", "tmnxNatApServStatSrcAddrType"),
        ("TIMETRA-NAT-MIB", "tmnxNatApServStatSrcAddr"),
        ("TIMETRA-NAT-MIB", "tmnxNatApServStatOperState"),
        ("TIMETRA-NAT-MIB", "tmnxNatApServStatTxRequests"),
        ("TIMETRA-NAT-MIB", "tmnxNatApServStatReqTimeout"),
        ("TIMETRA-NAT-MIB", "tmnxNatApServStatSendRetries"))
)
if mibBuilder.loadTexts:
    tmnxNatAccGroup.setStatus("obsolete")

tmnxNatWlanGwGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 65, 2, 25)
)
tmnxNatWlanGwGroup.setObjects(
      *(("TIMETRA-NAT-MIB", "tmnxNatGrpCfgTableLastCh"),
        ("TIMETRA-NAT-MIB", "tmnxNatGrpCfgLastMgmtChange"),
        ("TIMETRA-NAT-MIB", "tmnxNatGrpCfgSessionResvCount"),
        ("TIMETRA-NAT-MIB", "tmnxNatGrpCfgSessionWatermarkHi"),
        ("TIMETRA-NAT-MIB", "tmnxNatGrpCfgSessionWatermarkLo"))
)
if mibBuilder.loadTexts:
    tmnxNatWlanGwGroup.setStatus("current")

tmnxNat64Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 65, 2, 26)
)
tmnxNat64Group.setObjects(
      *(("TIMETRA-NAT-MIB", "tmnxNat64TableLastCh"),
        ("TIMETRA-NAT-MIB", "tmnxNat64LastMgmtChange"),
        ("TIMETRA-NAT-MIB", "tmnxNat64RowStatus"),
        ("TIMETRA-NAT-MIB", "tmnxNat64InAdminState"),
        ("TIMETRA-NAT-MIB", "tmnxNat64InSubPrefixLen"),
        ("TIMETRA-NAT-MIB", "tmnxNat64InPrefix"),
        ("TIMETRA-NAT-MIB", "tmnxNat64InPrefixLen"),
        ("TIMETRA-NAT-MIB", "tmnxNat64InIpv6Mtu"),
        ("TIMETRA-NAT-MIB", "tmnxNat64InDropZeroIpv4Checksum"),
        ("TIMETRA-NAT-MIB", "tmnxNat64InSetTos"),
        ("TIMETRA-NAT-MIB", "tmnxNat64InTos"),
        ("TIMETRA-NAT-MIB", "tmnxNat64InIgnoreTos"),
        ("TIMETRA-NAT-MIB", "tmnxNat64InInsertIpv6FragHeader"),
        ("TIMETRA-NAT-MIB", "tmnxNat64SubId"))
)
if mibBuilder.loadTexts:
    tmnxNat64Group.setStatus("obsolete")

tmnxNatLsnSubIdentGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 65, 2, 27)
)
tmnxNatLsnSubIdentGroup.setObjects(
      *(("TIMETRA-NAT-MIB", "tmnxNatSubIdTableLastCh"),
        ("TIMETRA-NAT-MIB", "tmnxNatSubIdLastMgmtChange"),
        ("TIMETRA-NAT-MIB", "tmnxNatSubIdDescription"),
        ("TIMETRA-NAT-MIB", "tmnxNatSubIdAdminState"),
        ("TIMETRA-NAT-MIB", "tmnxNatSubIdRadProxSrvRouter"),
        ("TIMETRA-NAT-MIB", "tmnxNatSubIdRadProxSrvName"),
        ("TIMETRA-NAT-MIB", "tmnxNatSubIdRadiusAttributeType"),
        ("TIMETRA-NAT-MIB", "tmnxNatSubIdRadiusVendorId"),
        ("TIMETRA-NAT-MIB", "tmnxNatSubIdDropUnidentified"),
        ("TIMETRA-NAT-MIB", "tmnxNatLsnSubIdStr"),
        ("TIMETRA-NAT-MIB", "tmnxNatLsnSubscIdStrTimeStamp"),
        ("TIMETRA-NAT-MIB", "tmnxNatSubscIdVendorStr"),
        ("TIMETRA-NAT-MIB", "tmnxNatSubscIdVendorDescription"),
        ("TIMETRA-NAT-MIB", "tmnxNatSubscIdAttrStr"),
        ("TIMETRA-NAT-MIB", "tmnxNatSubscIdAttrDescription"),
        ("TIMETRA-NAT-MIB", "tmnxNatLsnSubscIdCount"))
)
if mibBuilder.loadTexts:
    tmnxNatLsnSubIdentGroup.setStatus("obsolete")

tmnxNatPcpGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 65, 2, 28)
)
tmnxNatPcpGroup.setObjects(
      *(("TIMETRA-NAT-MIB", "tmnxNatFwdActionDescription"),
        ("TIMETRA-NAT-MIB", "tmnxNatFwdDescription"),
        ("TIMETRA-NAT-MIB", "tmnxNatFwdOrigin"),
        ("TIMETRA-NAT-MIB", "tmnxNatPcpPlcyTableLastCh"),
        ("TIMETRA-NAT-MIB", "tmnxNatPcpPlcyLastMgmtChange"),
        ("TIMETRA-NAT-MIB", "tmnxNatPcpPlcyRowStatus"),
        ("TIMETRA-NAT-MIB", "tmnxNatPcpPlcyDescription"),
        ("TIMETRA-NAT-MIB", "tmnxNatPcpPlcyOpcodes"),
        ("TIMETRA-NAT-MIB", "tmnxNatPcpPlcyOptions"),
        ("TIMETRA-NAT-MIB", "tmnxNatPcpPlcyMinimumLifetime"),
        ("TIMETRA-NAT-MIB", "tmnxNatPcpPlcyMaximumLifetime"),
        ("TIMETRA-NAT-MIB", "tmnxNatPcpPlcyMaxDescriptionLen"),
        ("TIMETRA-NAT-MIB", "tmnxNatPcpSrvTableLastCh"),
        ("TIMETRA-NAT-MIB", "tmnxNatPcpSrvLastCh"),
        ("TIMETRA-NAT-MIB", "tmnxNatPcpSrvRowStatus"),
        ("TIMETRA-NAT-MIB", "tmnxNatPcpSrvAdminState"),
        ("TIMETRA-NAT-MIB", "tmnxNatPcpSrvDescription"),
        ("TIMETRA-NAT-MIB", "tmnxNatPcpSrvPlcy"),
        ("TIMETRA-NAT-MIB", "tmnxNatPcpSrvFwdInsideRouter"),
        ("TIMETRA-NAT-MIB", "tmnxNatPcpSrvDsliteAftrAddr"),
        ("TIMETRA-NAT-MIB", "tmnxNatPcpSrvState"),
        ("TIMETRA-NAT-MIB", "tmnxNatPcpSrvStateDescription"),
        ("TIMETRA-NAT-MIB", "tmnxNatPcpSrvEpoch"),
        ("TIMETRA-NAT-MIB", "tmnxNatPcpSrvIfTableLastCh"),
        ("TIMETRA-NAT-MIB", "tmnxNatPcpSrvIfRowStatus"),
        ("TIMETRA-NAT-MIB", "tmnxNatPcpSrvIfLastCh"),
        ("TIMETRA-NAT-MIB", "tmnxNatPcpSrvIfStatsName"),
        ("TIMETRA-NAT-MIB", "tmnxNatPcpSrvIfStatsValLw"),
        ("TIMETRA-NAT-MIB", "tmnxNatPcpSrvIfStatsValHw"),
        ("TIMETRA-NAT-MIB", "tmnxNatPcpSrvIfStatsVal"))
)
if mibBuilder.loadTexts:
    tmnxNatPcpGroup.setStatus("current")

tmnxNatIsaStatV10v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 65, 2, 29)
)
tmnxNatIsaStatV10v0Group.setObjects(
      *(("TIMETRA-NAT-MIB", "tmnxNatIsaMemberStatsValHw"),
        ("TIMETRA-NAT-MIB", "tmnxNatIsaMemberStatsValue"),
        ("TIMETRA-NAT-MIB", "tmnxNatIsaResrcStatsName"),
        ("TIMETRA-NAT-MIB", "tmnxNatIsaResrcStatsValMax"),
        ("TIMETRA-NAT-MIB", "tmnxNatIsaResrcStatsValMaxLw"),
        ("TIMETRA-NAT-MIB", "tmnxNatIsaResrcStatsValMaxHw"),
        ("TIMETRA-NAT-MIB", "tmnxNatIsaResrcStatsVal"),
        ("TIMETRA-NAT-MIB", "tmnxNatIsaResrcStatsValLw"),
        ("TIMETRA-NAT-MIB", "tmnxNatIsaResrcStatsValHw"))
)
if mibBuilder.loadTexts:
    tmnxNatIsaStatV10v0Group.setStatus("current")

tmnxNatDeterministicGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 65, 2, 30)
)
tmnxNatDeterministicGroup.setObjects(
      *(("TIMETRA-NAT-MIB", "tmnxNatVrtrInMaxDetSubscrLimit"),
        ("TIMETRA-NAT-MIB", "tmnxNatVrtrInMaxDetSubLimitDsl"),
        ("TIMETRA-NAT-MIB", "tmnxNatDetPlcyTableLastCh"),
        ("TIMETRA-NAT-MIB", "tmnxNatDetPlcyRowStatus"),
        ("TIMETRA-NAT-MIB", "tmnxNatDetPlcyLastMgmtChange"),
        ("TIMETRA-NAT-MIB", "tmnxNatDetPlcyName"),
        ("TIMETRA-NAT-MIB", "tmnxNatDetPlcyRowStatus"),
        ("TIMETRA-NAT-MIB", "tmnxNatDetPlcyAdminState"),
        ("TIMETRA-NAT-MIB", "tmnxNatDetMapTableLastCh"),
        ("TIMETRA-NAT-MIB", "tmnxNatDetMapRowStatus"),
        ("TIMETRA-NAT-MIB", "tmnxNatDetMapLastCh"),
        ("TIMETRA-NAT-MIB", "tmnxNatDetMapOutAddrType"),
        ("TIMETRA-NAT-MIB", "tmnxNatDetMapOutStart"),
        ("TIMETRA-NAT-MIB", "tmnxNatPlLsnDetPortResv"),
        ("TIMETRA-NAT-MIB", "tmnxNatDetScriptLocation"),
        ("TIMETRA-NAT-MIB", "tmnxNatDetScriptSaveNeeded"),
        ("TIMETRA-NAT-MIB", "tmnxNatDetScriptSave"),
        ("TIMETRA-NAT-MIB", "tmnxNatDetScriptSaveResult"),
        ("TIMETRA-NAT-MIB", "tmnxNatDetScriptSaveTime"))
)
if mibBuilder.loadTexts:
    tmnxNatDeterministicGroup.setStatus("obsolete")

tmnxNatVrtrIPFilterGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 65, 2, 31)
)
tmnxNatVrtrIPFilterGroup.setObjects(
    ("TIMETRA-NAT-MIB", "tmnxNatVrtrOutUpstreamIPFilterId")
)
if mibBuilder.loadTexts:
    tmnxNatVrtrIPFilterGroup.setStatus("current")

tmnxNatPlV11v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 65, 2, 32)
)
tmnxNatPlV11v0Group.setObjects(
      *(("TIMETRA-NAT-MIB", "tmnxNatPlTableLastCh"),
        ("TIMETRA-NAT-MIB", "tmnxNatPlRowStatus"),
        ("TIMETRA-NAT-MIB", "tmnxNatPlLastMgmtChange"),
        ("TIMETRA-NAT-MIB", "tmnxNatPlIsaGrp"),
        ("TIMETRA-NAT-MIB", "tmnxNatPlType"),
        ("TIMETRA-NAT-MIB", "tmnxNatPlDescription"),
        ("TIMETRA-NAT-MIB", "tmnxNatPlAdminState"),
        ("TIMETRA-NAT-MIB", "tmnxNatPlPortResvType"),
        ("TIMETRA-NAT-MIB", "tmnxNatPlPortResvVal"),
        ("TIMETRA-NAT-MIB", "tmnxNatPlPortResvAllowPrivileged"),
        ("TIMETRA-NAT-MIB", "tmnxNatPlWatermarkHigh"),
        ("TIMETRA-NAT-MIB", "tmnxNatPlWatermarkLow"),
        ("TIMETRA-NAT-MIB", "tmnxNatPlRangeTableLastCh"),
        ("TIMETRA-NAT-MIB", "tmnxNatPlRangeRowStatus"),
        ("TIMETRA-NAT-MIB", "tmnxNatPlRangeLastMgmtChange"),
        ("TIMETRA-NAT-MIB", "tmnxNatPlRangeDescription"),
        ("TIMETRA-NAT-MIB", "tmnxNatPlRangeAdminDrain"),
        ("TIMETRA-NAT-MIB", "tmnxNatPlPortFwdRangeEnd"),
        ("TIMETRA-NAT-MIB", "tmnxNatPlOperMode"),
        ("TIMETRA-NAT-MIB", "tmnxNatPlPortFwdDynBlkResv"),
        ("TIMETRA-NAT-MIB", "tmnxNatPlHistActionVRtrId"),
        ("TIMETRA-NAT-MIB", "tmnxNatPlHistActionPoolName"),
        ("TIMETRA-NAT-MIB", "tmnxNatPlHistActionBucketSize"),
        ("TIMETRA-NAT-MIB", "tmnxNatPlHistActionNumBuckets"),
        ("TIMETRA-NAT-MIB", "tmnxNatPlHistActionGo"),
        ("TIMETRA-NAT-MIB", "tmnxNatPlHistTimestamp"),
        ("TIMETRA-NAT-MIB", "tmnxNatPlHistVRtrID"),
        ("TIMETRA-NAT-MIB", "tmnxNatPlHistPoolName"),
        ("TIMETRA-NAT-MIB", "tmnxNatPlHistBucketSize"),
        ("TIMETRA-NAT-MIB", "tmnxNatPlHistNumBuckets"),
        ("TIMETRA-NAT-MIB", "tmnxNatPlHistTcp"),
        ("TIMETRA-NAT-MIB", "tmnxNatPlHistUdp"),
        ("TIMETRA-NAT-MIB", "tmnxNatPlHistIcmp"),
        ("TIMETRA-NAT-MIB", "tmnxNatPlRangeStatNumAllocBlk"))
)
if mibBuilder.loadTexts:
    tmnxNatPlV11v0Group.setStatus("current")

tmnxNatAccV11v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 65, 2, 33)
)
tmnxNatAccV11v0Group.setObjects(
    ("TIMETRA-NAT-MIB", "tmnxNatGrpCfgAccountingPlcy")
)
if mibBuilder.loadTexts:
    tmnxNatAccV11v0Group.setStatus("current")

tmnxNatIsaStatV11v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 65, 2, 34)
)
tmnxNatIsaStatV11v0Group.setObjects(
      *(("TIMETRA-NAT-MIB", "tmnxNatReassemblyStatsName"),
        ("TIMETRA-NAT-MIB", "tmnxNatReassemblyStatsVal"),
        ("TIMETRA-NAT-MIB", "tmnxNatReassemblyStatsValLw"),
        ("TIMETRA-NAT-MIB", "tmnxNatReassemblyStatsValHw"))
)
if mibBuilder.loadTexts:
    tmnxNatIsaStatV11v0Group.setStatus("current")

tmnxNatFragmentIpGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 65, 2, 35)
)
tmnxNatFragmentIpGroup.setObjects(
      *(("TIMETRA-NAT-MIB", "tmnxNatDsliteAddrFragmentIp"),
        ("TIMETRA-NAT-MIB", "tmnxNat64InFragmentIp"))
)
if mibBuilder.loadTexts:
    tmnxNatFragmentIpGroup.setStatus("current")

tmnxNatMultiPlcyGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 65, 2, 36)
)
tmnxNatMultiPlcyGroup.setObjects(
      *(("TIMETRA-NAT-MIB", "tmnxNatDestNatPolicy"),
        ("TIMETRA-NAT-MIB", "tmnxNatPlLsnRedAdminState"),
        ("TIMETRA-NAT-MIB", "tmnxNatPlLsnRedFollowPoolRouter"),
        ("TIMETRA-NAT-MIB", "tmnxNatPlLsnRedFollowPool"),
        ("TIMETRA-NAT-MIB", "tmnxNatLsnSubBlkPolicy"),
        ("TIMETRA-NAT-MIB", "tmnxNatQryLsnSubNextQryId"),
        ("TIMETRA-NAT-MIB", "tmnxNatQryLsnSubMaxQryId"),
        ("TIMETRA-NAT-MIB", "tmnxNatQryLsnSubRowStatus"),
        ("TIMETRA-NAT-MIB", "tmnxNatQryLsnSubResultType"),
        ("TIMETRA-NAT-MIB", "tmnxNatQryLsnSubWhereNatPolicy"),
        ("TIMETRA-NAT-MIB", "tmnxNatQryLsnSubWhereIsaGrp"),
        ("TIMETRA-NAT-MIB", "tmnxNatQryLsnSubWhereMemberId"),
        ("TIMETRA-NAT-MIB", "tmnxNatQryLsnSubWhereOutRouter"),
        ("TIMETRA-NAT-MIB", "tmnxNatQryLsnSubWhereOutAddrType"),
        ("TIMETRA-NAT-MIB", "tmnxNatQryLsnSubWhereOutAddr"),
        ("TIMETRA-NAT-MIB", "tmnxNatQryLsnSubWhereInSubType"),
        ("TIMETRA-NAT-MIB", "tmnxNatQryLsnSubWhereInRouter"),
        ("TIMETRA-NAT-MIB", "tmnxNatQryLsnSubWhereInAddrType"),
        ("TIMETRA-NAT-MIB", "tmnxNatQryLsnSubWhereInAddr"),
        ("TIMETRA-NAT-MIB", "tmnxNatQryLsnSubWhereInAddrPfxL"),
        ("TIMETRA-NAT-MIB", "tmnxNatQryLsnSubWhereSubId"),
        ("TIMETRA-NAT-MIB", "tmnxNatQryLsnSubResIsaGrp"),
        ("TIMETRA-NAT-MIB", "tmnxNatQryLsnSubResIsaMemberId"),
        ("TIMETRA-NAT-MIB", "tmnxNatQryLsnSubResOutVRtrID"),
        ("TIMETRA-NAT-MIB", "tmnxNatQryLsnSubResOutAddrType"),
        ("TIMETRA-NAT-MIB", "tmnxNatQryLsnSubResOutAddr"),
        ("TIMETRA-NAT-MIB", "tmnxNatQryLsnSubResIdStr"),
        ("TIMETRA-NAT-MIB", "tmnxNatQryLsnSubResInSubType"),
        ("TIMETRA-NAT-MIB", "tmnxNatQryLsnSubResInRouter"),
        ("TIMETRA-NAT-MIB", "tmnxNatQryLsnSubResInAddrType"),
        ("TIMETRA-NAT-MIB", "tmnxNatQryLsnSubResInAddr"),
        ("TIMETRA-NAT-MIB", "tmnxNatQryLsnSubResInAddrPfxL"),
        ("TIMETRA-NAT-MIB", "tmnxNatQryLsnSubResIcmpPortUsg"),
        ("TIMETRA-NAT-MIB", "tmnxNatQryLsnSubResIcmpPortUsgHi"),
        ("TIMETRA-NAT-MIB", "tmnxNatQryLsnSubResUdpPortUsg"),
        ("TIMETRA-NAT-MIB", "tmnxNatQryLsnSubResUdpPortUsgHi"),
        ("TIMETRA-NAT-MIB", "tmnxNatQryLsnSubResTcpPortUsg"),
        ("TIMETRA-NAT-MIB", "tmnxNatQryLsnSubResTcpPortUsgHi"),
        ("TIMETRA-NAT-MIB", "tmnxNatQryLsnSubResSessionUsg"),
        ("TIMETRA-NAT-MIB", "tmnxNatQryLsnSubResSessionUsgHi"),
        ("TIMETRA-NAT-MIB", "tmnxNatQryLsnSubResSessions"),
        ("TIMETRA-NAT-MIB", "tmnxNatQryLsnSubResSessionsPrio"),
        ("TIMETRA-NAT-MIB", "tmnxNatQryLsnSubResSessionsPeak"),
        ("TIMETRA-NAT-MIB", "tmnxNatFwdActionNatPolicy"),
        ("TIMETRA-NAT-MIB", "tmnxNatFwd2OutVRtrID"),
        ("TIMETRA-NAT-MIB", "tmnxNatFwd2OutAddrType"),
        ("TIMETRA-NAT-MIB", "tmnxNatFwd2OutAddr"),
        ("TIMETRA-NAT-MIB", "tmnxNatFwd2OutPort"),
        ("TIMETRA-NAT-MIB", "tmnxNatFwd2ExpiryDateAndTime"),
        ("TIMETRA-NAT-MIB", "tmnxNatFwd2LsnAftrAddrType"),
        ("TIMETRA-NAT-MIB", "tmnxNatFwd2LsnAftrAddr"),
        ("TIMETRA-NAT-MIB", "tmnxNatFwd2PersistKey"),
        ("TIMETRA-NAT-MIB", "tmnxNatFwd2Description"),
        ("TIMETRA-NAT-MIB", "tmnxNatFwd2Origin"))
)
if mibBuilder.loadTexts:
    tmnxNatMultiPlcyGroup.setStatus("current")

tmnxNatIsaV12v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 65, 2, 37)
)
tmnxNatIsaV12v0Group.setObjects(
      *(("TIMETRA-NAT-MIB", "tmnxNatIsaGrpTableLastCh"),
        ("TIMETRA-NAT-MIB", "tmnxNatIsaGrpRowStatus"),
        ("TIMETRA-NAT-MIB", "tmnxNatIsaGrpLastMgmtChange"),
        ("TIMETRA-NAT-MIB", "tmnxNatIsaGrpDescription"),
        ("TIMETRA-NAT-MIB", "tmnxNatIsaGrpAdminState"),
        ("TIMETRA-NAT-MIB", "tmnxNatIsaGrpActiveMdaLimit"),
        ("TIMETRA-NAT-MIB", "tmnxNatIsaGrpOperState"),
        ("TIMETRA-NAT-MIB", "tmnxNatIsaGrpDegraded"),
        ("TIMETRA-NAT-MIB", "tmnxNatIsaMdaTableLastCh"),
        ("TIMETRA-NAT-MIB", "tmnxNatIsaMdaRowStatus"),
        ("TIMETRA-NAT-MIB", "tmnxNatIsaMdaLastMgmtChange"))
)
if mibBuilder.loadTexts:
    tmnxNatIsaV12v0Group.setStatus("current")

tmnxNatQryGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 65, 2, 38)
)
tmnxNatQryGroup.setObjects(
      *(("TIMETRA-NAT-MIB", "tmnxNatQryLsnSubNextQryId"),
        ("TIMETRA-NAT-MIB", "tmnxNatQryLsnSubRowStatus"),
        ("TIMETRA-NAT-MIB", "tmnxNatQryLsnSubWhereNatPolicy"),
        ("TIMETRA-NAT-MIB", "tmnxNatQryLsnSubWhereIsaGrp"),
        ("TIMETRA-NAT-MIB", "tmnxNatQryLsnSubWhereMemberId"),
        ("TIMETRA-NAT-MIB", "tmnxNatQryLsnSubWhereOutRouter"),
        ("TIMETRA-NAT-MIB", "tmnxNatQryLsnSubWhereOutAddrType"),
        ("TIMETRA-NAT-MIB", "tmnxNatQryLsnSubWhereOutAddr"),
        ("TIMETRA-NAT-MIB", "tmnxNatQryLsnSubResIsaGrp"),
        ("TIMETRA-NAT-MIB", "tmnxNatQryLsnSubResIsaMemberId"),
        ("TIMETRA-NAT-MIB", "tmnxNatQryLsnSubResOutVRtrID"),
        ("TIMETRA-NAT-MIB", "tmnxNatQryLsnSubResOutAddrType"),
        ("TIMETRA-NAT-MIB", "tmnxNatQryLsnSubResOutAddr"),
        ("TIMETRA-NAT-MIB", "tmnxNatQryLsnSubResIdStr"),
        ("TIMETRA-NAT-MIB", "tmnxNatQryLsnSubResIcmpPortUsg"),
        ("TIMETRA-NAT-MIB", "tmnxNatQryLsnSubResIcmpPortUsgHi"),
        ("TIMETRA-NAT-MIB", "tmnxNatQryLsnSubResUdpPortUsg"),
        ("TIMETRA-NAT-MIB", "tmnxNatQryLsnSubResUdpPortUsgHi"),
        ("TIMETRA-NAT-MIB", "tmnxNatQryLsnSubResTcpPortUsg"),
        ("TIMETRA-NAT-MIB", "tmnxNatQryLsnSubResTcpPortUsgHi"),
        ("TIMETRA-NAT-MIB", "tmnxNatQryLsnSubResSessionUsg"),
        ("TIMETRA-NAT-MIB", "tmnxNatQryLsnSubResSessionUsgHi"),
        ("TIMETRA-NAT-MIB", "tmnxNatQryLsnSubResSessions"),
        ("TIMETRA-NAT-MIB", "tmnxNatQryLsnSubResSessionsPrio"),
        ("TIMETRA-NAT-MIB", "tmnxNatQryLsnSubResSessionsPeak"))
)
if mibBuilder.loadTexts:
    tmnxNatQryGroup.setStatus("current")

tmnxNatVrtrIPFilterV12v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 65, 2, 39)
)
tmnxNatVrtrIPFilterV12v0Group.setObjects(
    ("TIMETRA-NAT-MIB", "tmnxNatVrtrOutDnstreamIPFilterId")
)
if mibBuilder.loadTexts:
    tmnxNatVrtrIPFilterV12v0Group.setStatus("current")

tmnxNatFwd2Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 65, 2, 40)
)
tmnxNatFwd2Group.setObjects(
      *(("TIMETRA-NAT-MIB", "tmnxNatFwdActionSubType"),
        ("TIMETRA-NAT-MIB", "tmnxNatFwdActionVRtrId"),
        ("TIMETRA-NAT-MIB", "tmnxNatFwdActionAddrType"),
        ("TIMETRA-NAT-MIB", "tmnxNatFwdActionAddr"),
        ("TIMETRA-NAT-MIB", "tmnxNatFwdActionB4Addr"),
        ("TIMETRA-NAT-MIB", "tmnxNatFwdActionAftrAddr"),
        ("TIMETRA-NAT-MIB", "tmnxNatFwdActionL2awSubscriberId"),
        ("TIMETRA-NAT-MIB", "tmnxNatFwdActionProtocol"),
        ("TIMETRA-NAT-MIB", "tmnxNatFwdActionTimeOut"),
        ("TIMETRA-NAT-MIB", "tmnxNatFwdActionPort"),
        ("TIMETRA-NAT-MIB", "tmnxNatFwdActionOutPort"),
        ("TIMETRA-NAT-MIB", "tmnxNatFwdActionOutAddr"),
        ("TIMETRA-NAT-MIB", "tmnxNatFwdActionType"),
        ("TIMETRA-NAT-MIB", "tmnxNatFwdActionGo"),
        ("TIMETRA-NAT-MIB", "tmnxNatFwdActionSuccessful"),
        ("TIMETRA-NAT-MIB", "tmnxNatFwdActionTime"))
)
if mibBuilder.loadTexts:
    tmnxNatFwd2Group.setStatus("current")

tmnxNatLsnV12v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 65, 2, 41)
)
tmnxNatLsnV12v0Group.setObjects(
      *(("TIMETRA-NAT-MIB", "tmnxNatPlLsnMemberIsaGrpId"),
        ("TIMETRA-NAT-MIB", "tmnxNatPlLsnMemberBlockUsage"),
        ("TIMETRA-NAT-MIB", "tmnxNatPlLsnMemberBlockUsageHi"),
        ("TIMETRA-NAT-MIB", "tmnxNatBlkLsnEnd"),
        ("TIMETRA-NAT-MIB", "tmnxNatBlkLsnPool"),
        ("TIMETRA-NAT-MIB", "tmnxNatBlkLsnSubId"),
        ("TIMETRA-NAT-MIB", "tmnxNatBlkLsnInsideVRtrID"),
        ("TIMETRA-NAT-MIB", "tmnxNatBlkLsnInsideAddrType"),
        ("TIMETRA-NAT-MIB", "tmnxNatBlkLsnInsideAddr"),
        ("TIMETRA-NAT-MIB", "tmnxNatBlkLsnPolicy"),
        ("TIMETRA-NAT-MIB", "tmnxNatBlkLsnStartDateAndTime"),
        ("TIMETRA-NAT-MIB", "tmnxNatLsnSubBlkEnd"),
        ("TIMETRA-NAT-MIB", "tmnxNatPlLsnSubscriberLimit"),
        ("TIMETRA-NAT-MIB", "tmnxNatPlcyBlkLimit"),
        ("TIMETRA-NAT-MIB", "tmnxNatPlMode"),
        ("TIMETRA-NAT-MIB", "tmnxNatDsliteAddrTableLastCh"),
        ("TIMETRA-NAT-MIB", "tmnxNatDsliteAddrRowStatus"),
        ("TIMETRA-NAT-MIB", "tmnxNatDsliteAddrLastMgmtChange"),
        ("TIMETRA-NAT-MIB", "tmnxNatDsliteAddrTunnelMtu"),
        ("TIMETRA-NAT-MIB", "tmnxNat64TableLastCh"),
        ("TIMETRA-NAT-MIB", "tmnxNat64LastMgmtChange"),
        ("TIMETRA-NAT-MIB", "tmnxNat64RowStatus"),
        ("TIMETRA-NAT-MIB", "tmnxNat64InAdminState"),
        ("TIMETRA-NAT-MIB", "tmnxNat64InSubPrefixLen"),
        ("TIMETRA-NAT-MIB", "tmnxNat64InPrefix"),
        ("TIMETRA-NAT-MIB", "tmnxNat64InPrefixLen"),
        ("TIMETRA-NAT-MIB", "tmnxNat64InIpv6Mtu"),
        ("TIMETRA-NAT-MIB", "tmnxNat64InDropZeroIpv4Checksum"),
        ("TIMETRA-NAT-MIB", "tmnxNat64InSetTos"),
        ("TIMETRA-NAT-MIB", "tmnxNat64InTos"),
        ("TIMETRA-NAT-MIB", "tmnxNat64InIgnoreTos"),
        ("TIMETRA-NAT-MIB", "tmnxNat64InInsertIpv6FragHeader"))
)
if mibBuilder.loadTexts:
    tmnxNatLsnV12v0Group.setStatus("obsolete")

tmnxNatLsnSubIdentV12v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 65, 2, 42)
)
tmnxNatLsnSubIdentV12v0Group.setObjects(
      *(("TIMETRA-NAT-MIB", "tmnxNatSubIdTableLastCh"),
        ("TIMETRA-NAT-MIB", "tmnxNatSubIdLastMgmtChange"),
        ("TIMETRA-NAT-MIB", "tmnxNatSubIdDescription"),
        ("TIMETRA-NAT-MIB", "tmnxNatSubIdAdminState"),
        ("TIMETRA-NAT-MIB", "tmnxNatSubIdRadProxSrvRouter"),
        ("TIMETRA-NAT-MIB", "tmnxNatSubIdRadProxSrvName"),
        ("TIMETRA-NAT-MIB", "tmnxNatSubIdRadiusAttributeType"),
        ("TIMETRA-NAT-MIB", "tmnxNatSubIdRadiusVendorId"),
        ("TIMETRA-NAT-MIB", "tmnxNatSubIdDropUnidentified"),
        ("TIMETRA-NAT-MIB", "tmnxNatLsnSubscIdStrTimeStamp"),
        ("TIMETRA-NAT-MIB", "tmnxNatSubscIdVendorStr"),
        ("TIMETRA-NAT-MIB", "tmnxNatSubscIdVendorDescription"),
        ("TIMETRA-NAT-MIB", "tmnxNatSubscIdAttrStr"),
        ("TIMETRA-NAT-MIB", "tmnxNatSubscIdAttrDescription"),
        ("TIMETRA-NAT-MIB", "tmnxNatLsnSubscIdCount"))
)
if mibBuilder.loadTexts:
    tmnxNatLsnSubIdentV12v0Group.setStatus("current")

tmnxNatPcp2Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 65, 2, 43)
)
tmnxNatPcp2Group.setObjects(
      *(("TIMETRA-NAT-MIB", "tmnxNatPcpPlcyMinimumVersion"),
        ("TIMETRA-NAT-MIB", "tmnxNatPcpPlcyMaximumVersion"),
        ("TIMETRA-NAT-MIB", "tmnxNatFwd2ProtocolVersion"),
        ("TIMETRA-NAT-MIB", "tmnxNatFwd2MappingNumber"))
)
if mibBuilder.loadTexts:
    tmnxNatPcp2Group.setStatus("current")

tmnxNatIsa2Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 65, 2, 44)
)
tmnxNatIsa2Group.setObjects(
      *(("TIMETRA-NAT-MIB", "tmnxNatDetPlcyOperState"),
        ("TIMETRA-NAT-MIB", "tmnxNatDetMapOperState"),
        ("TIMETRA-NAT-MIB", "tmnxNatFwd2OperState"))
)
if mibBuilder.loadTexts:
    tmnxNatIsa2Group.setStatus("obsolete")

tmnxNatUpnpGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 65, 2, 45)
)
tmnxNatUpnpGroup.setObjects(
      *(("TIMETRA-NAT-MIB", "tmnxNatGrpCfgSessionUpnpMapLimit"),
        ("TIMETRA-NAT-MIB", "tmnxNatUpnpPlcyRowStatus"),
        ("TIMETRA-NAT-MIB", "tmnxNatUpnpPlcyLastMgmtChange"),
        ("TIMETRA-NAT-MIB", "tmnxNatUpnpPlcyDescription"),
        ("TIMETRA-NAT-MIB", "tmnxNatUpnpPlcyMappingLimit"),
        ("TIMETRA-NAT-MIB", "tmnxNatUpnpPlcyStrictMode"),
        ("TIMETRA-NAT-MIB", "tmnxNatUpnpPlcyListeningPort"),
        ("TIMETRA-NAT-MIB", "tmnxNatUpnpPlcyTableLastCh"),
        ("TIMETRA-NAT-MIB", "tmnxNatUpnpPlcyStatsName"),
        ("TIMETRA-NAT-MIB", "tmnxNatUpnpPlcyStatsVal"),
        ("TIMETRA-NAT-MIB", "tmnxNatUpnpPlcyStatActMappings"),
        ("TIMETRA-NAT-MIB", "tmnxNatUpnpPlcyStatSubscrMapped"),
        ("TIMETRA-NAT-MIB", "tmnxNatUpnpPlcyStatSubscr"),
        ("TIMETRA-NAT-MIB", "tmnxNatL2AwSubStatCurrUpnpPlcy"))
)
if mibBuilder.loadTexts:
    tmnxNatUpnpGroup.setStatus("obsolete")

tmnxNatActiveActiveRedGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 65, 2, 46)
)
tmnxNatActiveActiveRedGroup.setObjects(
      *(("TIMETRA-NAT-MIB", "tmnxNatIsaGrpRedundancy"),
        ("TIMETRA-NAT-MIB", "tmnxNatIsaGrpFailedMdaLimit"),
        ("TIMETRA-NAT-MIB", "tmnxNatIsaMdaStatResrcAllocated"),
        ("TIMETRA-NAT-MIB", "tmnxNatIsaResrcStatsLimited"),
        ("TIMETRA-NAT-MIB", "tmnxNatIsaMdaStatsName"),
        ("TIMETRA-NAT-MIB", "tmnxNatIsaMdaStatsValue"),
        ("TIMETRA-NAT-MIB", "tmnxNatIsaMemberResrcName"),
        ("TIMETRA-NAT-MIB", "tmnxNatIsaMemberResrcValMax"),
        ("TIMETRA-NAT-MIB", "tmnxNatIsaMemberResrcVal"),
        ("TIMETRA-NAT-MIB", "tmnxNatIsaMemberResrcApplicable"))
)
if mibBuilder.loadTexts:
    tmnxNatActiveActiveRedGroup.setStatus("current")

tmnxNatPlV13v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 65, 2, 47)
)
tmnxNatPlV13v0Group.setObjects(
    ("TIMETRA-NAT-MIB", "tmnxNatPlApplications")
)
if mibBuilder.loadTexts:
    tmnxNatPlV13v0Group.setStatus("current")

tmnxNatVrtrIPv6FilterV13v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 65, 2, 48)
)
tmnxNatVrtrIPv6FilterV13v0Group.setObjects(
      *(("TIMETRA-NAT-MIB", "tmnxNatVrtrOutUpstrmIPv6FilterId"),
        ("TIMETRA-NAT-MIB", "tmnxNatVrtrOutDnstrmIPv6FilterId"))
)
if mibBuilder.loadTexts:
    tmnxNatVrtrIPv6FilterV13v0Group.setStatus("current")

tmnxNatNoLsnSubBlksFreeGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 65, 2, 49)
)
tmnxNatNoLsnSubBlksFreeGroup.setObjects(
    ("TIMETRA-NAT-MIB", "tmnxNatGrpCfgNoLsnSubBlksFree")
)
if mibBuilder.loadTexts:
    tmnxNatNoLsnSubBlksFreeGroup.setStatus("current")

tmnxNatWlanGwV14v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 65, 2, 50)
)
tmnxNatWlanGwV14v0Group.setObjects(
    ("TIMETRA-NAT-MIB", "tmnxNatGrpCfgLsn")
)
if mibBuilder.loadTexts:
    tmnxNatWlanGwV14v0Group.setStatus("current")

tmnxNatVrtrIPFilterV14v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 65, 2, 51)
)
tmnxNatVrtrIPFilterV14v0Group.setObjects(
    ("TIMETRA-NAT-MIB", "tmnxNatVrtrInDnstreamIPFilterId")
)
if mibBuilder.loadTexts:
    tmnxNatVrtrIPFilterV14v0Group.setStatus("current")

tmnxNatUpnpV14v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 65, 2, 52)
)
tmnxNatUpnpV14v0Group.setObjects(
      *(("TIMETRA-NAT-MIB", "tmnxNatGrpCfgSessionUpnpMapLimit"),
        ("TIMETRA-NAT-MIB", "tmnxNatUpnpPlcyRowStatus"),
        ("TIMETRA-NAT-MIB", "tmnxNatUpnpPlcyLastMgmtChange"),
        ("TIMETRA-NAT-MIB", "tmnxNatUpnpPlcyDescription"),
        ("TIMETRA-NAT-MIB", "tmnxNatUpnpPlcyMappingLimit"),
        ("TIMETRA-NAT-MIB", "tmnxNatUpnpPlcyStrictMode"),
        ("TIMETRA-NAT-MIB", "tmnxNatUpnpPlcyListeningPort"),
        ("TIMETRA-NAT-MIB", "tmnxNatUpnpPlcyTableLastCh"),
        ("TIMETRA-NAT-MIB", "tmnxNatUpnpPlcyStatsName"),
        ("TIMETRA-NAT-MIB", "tmnxNatUpnpPlcyStatsVal"),
        ("TIMETRA-NAT-MIB", "tmnxNatUpnpPlcyStatActMappings"),
        ("TIMETRA-NAT-MIB", "tmnxNatUpnpPlcyStatSubscrMapped"),
        ("TIMETRA-NAT-MIB", "tmnxNatUpnpPlcyStatSubscr"))
)
if mibBuilder.loadTexts:
    tmnxNatUpnpV14v0Group.setStatus("current")

tmnxNatPlcyV14v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 65, 2, 53)
)
tmnxNatPlcyV14v0Group.setObjects(
      *(("TIMETRA-NAT-MIB", "tmnxNatPlcyRstUnknownTcp"),
        ("TIMETRA-NAT-MIB", "tmnxNatPlcyToTcpRst"))
)
if mibBuilder.loadTexts:
    tmnxNatPlcyV14v0Group.setStatus("current")

tmnxNatPlcyV15v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 65, 2, 54)
)
tmnxNatPlcyV15v0Group.setObjects(
      *(("TIMETRA-NAT-MIB", "tmnxNatPlcyL2Outside"),
        ("TIMETRA-NAT-MIB", "tmnxNatPlcyPortFwdRangeEnd"),
        ("TIMETRA-NAT-MIB", "tmnxNatL2AwSubPlcyOutServiceId"),
        ("TIMETRA-NAT-MIB", "tmnxNatFwd2OutService"))
)
if mibBuilder.loadTexts:
    tmnxNatPlcyV15v0Group.setStatus("current")

tmnxNatWlanGwV15v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 65, 2, 55)
)
tmnxNatWlanGwV15v0Group.setObjects(
    ("TIMETRA-NAT-MIB", "tmnxNatGrpCfgNoLsnEvents")
)
if mibBuilder.loadTexts:
    tmnxNatWlanGwV15v0Group.setStatus("current")

tmnxNatFwdV15v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 65, 2, 56)
)
tmnxNatFwdV15v0Group.setObjects(
      *(("TIMETRA-NAT-MIB", "tmnxNatFwd2ForeignPfxType"),
        ("TIMETRA-NAT-MIB", "tmnxNatFwd2ForeignPfx"),
        ("TIMETRA-NAT-MIB", "tmnxNatFwd2ForeignPfxLength"),
        ("TIMETRA-NAT-MIB", "tmnxNatFwd2ForeignPort"))
)
if mibBuilder.loadTexts:
    tmnxNatFwdV15v0Group.setStatus("current")

tmnxNatFwdL2AwGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 65, 2, 57)
)
tmnxNatFwdL2AwGroup.setObjects(
      *(("TIMETRA-NAT-MIB", "tmnxNatFwdL2AwOutVRtrID"),
        ("TIMETRA-NAT-MIB", "tmnxNatFwdL2AwOutAddrType"),
        ("TIMETRA-NAT-MIB", "tmnxNatFwdL2AwOutAddr"),
        ("TIMETRA-NAT-MIB", "tmnxNatFwdL2AwOutPort"),
        ("TIMETRA-NAT-MIB", "tmnxNatFwdL2AwExpiryDateAndTime"),
        ("TIMETRA-NAT-MIB", "tmnxNatFwdL2AwPersistKey"),
        ("TIMETRA-NAT-MIB", "tmnxNatFwdL2AwOrigin"),
        ("TIMETRA-NAT-MIB", "tmnxNatFwdL2AwOperState"),
        ("TIMETRA-NAT-MIB", "tmnxNatFwdL2AwPersistence"),
        ("TIMETRA-NAT-MIB", "tmnxNatFwdL2AwOutService"))
)
if mibBuilder.loadTexts:
    tmnxNatFwdL2AwGroup.setStatus("current")

tmnxNatPcpExt1Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 65, 2, 58)
)
tmnxNatPcpExt1Group.setObjects(
    ("TIMETRA-NAT-MIB", "tmnxNatPcpPlcyReuseExtIp")
)
if mibBuilder.loadTexts:
    tmnxNatPcpExt1Group.setStatus("current")

tmnxNatDeterministic2Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 65, 2, 59)
)
tmnxNatDeterministic2Group.setObjects(
      *(("TIMETRA-NAT-MIB", "tmnxNatDetPfxMapTableLastCh"),
        ("TIMETRA-NAT-MIB", "tmnxNatDetPfxMapRowStatus"),
        ("TIMETRA-NAT-MIB", "tmnxNatDetPfxMapLastMgmtChange"),
        ("TIMETRA-NAT-MIB", "tmnxNatDetPfxMapRowStatus"),
        ("TIMETRA-NAT-MIB", "tmnxNatDetPfxMapAdminState"),
        ("TIMETRA-NAT-MIB", "tmnxNatDetPfxMapOperState"),
        ("TIMETRA-NAT-MIB", "tmnxNatDetMap2TableLastCh"),
        ("TIMETRA-NAT-MIB", "tmnxNatDetMap2RowStatus"),
        ("TIMETRA-NAT-MIB", "tmnxNatDetMap2LastCh"),
        ("TIMETRA-NAT-MIB", "tmnxNatDetMap2OutAddrType"),
        ("TIMETRA-NAT-MIB", "tmnxNatDetMap2OutStart"),
        ("TIMETRA-NAT-MIB", "tmnxNatDetMap2OperState"))
)
if mibBuilder.loadTexts:
    tmnxNatDeterministic2Group.setStatus("current")

tmnxNatDetV23v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 65, 2, 60)
)
tmnxNatDetV23v0Group.setObjects(
      *(("TIMETRA-NAT-MIB", "tmnxNatVrtrInMaxDetSubscrLimit"),
        ("TIMETRA-NAT-MIB", "tmnxNatVrtrInMaxDetSubLimitDsl"),
        ("TIMETRA-NAT-MIB", "tmnxNatDetPlcyTableLastCh"),
        ("TIMETRA-NAT-MIB", "tmnxNatDetMapTableLastCh"),
        ("TIMETRA-NAT-MIB", "tmnxNatPlLsnDetPortResv"),
        ("TIMETRA-NAT-MIB", "tmnxNatDetScriptLocation"),
        ("TIMETRA-NAT-MIB", "tmnxNatDetScriptSaveNeeded"),
        ("TIMETRA-NAT-MIB", "tmnxNatDetScriptSave"),
        ("TIMETRA-NAT-MIB", "tmnxNatDetScriptSaveResult"),
        ("TIMETRA-NAT-MIB", "tmnxNatDetScriptSaveTime"))
)
if mibBuilder.loadTexts:
    tmnxNatDetV23v0Group.setStatus("current")

tmnxNatIsa2V23v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 65, 2, 61)
)
tmnxNatIsa2V23v0Group.setObjects(
    ("TIMETRA-NAT-MIB", "tmnxNatFwd2OperState")
)
if mibBuilder.loadTexts:
    tmnxNatIsa2V23v0Group.setStatus("current")

tmnxNatPlcyV23v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 65, 2, 62)
)
tmnxNatPlcyV23v0Group.setObjects(
    ("TIMETRA-NAT-MIB", "tmnxNatPlcyDynamicPorts")
)
if mibBuilder.loadTexts:
    tmnxNatPlcyV23v0Group.setStatus("current")

tmnxNatDetV24v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 65, 2, 63)
)
tmnxNatDetV24v0Group.setObjects(
      *(("TIMETRA-NAT-MIB", "tmnxNatDetAddrMapTableLastCh"),
        ("TIMETRA-NAT-MIB", "tmnxNatDetAddrMapRowStatus"),
        ("TIMETRA-NAT-MIB", "tmnxNatDetAddrMapLastCh"),
        ("TIMETRA-NAT-MIB", "tmnxNatDetAddrMapAdminState"),
        ("TIMETRA-NAT-MIB", "tmnxNatDetAddrMapOperState"),
        ("TIMETRA-NAT-MIB", "tmnxNatDetAddrMapOutStartType"),
        ("TIMETRA-NAT-MIB", "tmnxNatDetAddrMapOutStart"))
)
if mibBuilder.loadTexts:
    tmnxNatDetV24v0Group.setStatus("current")

tmnxNatGrpCfgV25v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 65, 2, 64)
)
tmnxNatGrpCfgV25v0Group.setObjects(
      *(("TIMETRA-NAT-MIB", "tmnxNatGrpCfgLogPerUpdInterval"),
        ("TIMETRA-NAT-MIB", "tmnxNatGrpCfgLogPerUpdRateLimit"))
)
if mibBuilder.loadTexts:
    tmnxNatGrpCfgV25v0Group.setStatus("current")

tmnxNatPlRangeExclGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 65, 2, 65)
)
tmnxNatPlRangeExclGroup.setObjects(
      *(("TIMETRA-NAT-MIB", "tmnxNatPlRangeExclTableLastCh"),
        ("TIMETRA-NAT-MIB", "tmnxNatPlRangeExclRowStatus"),
        ("TIMETRA-NAT-MIB", "tmnxNatPlRangeExclLastMgmtChange"))
)
if mibBuilder.loadTexts:
    tmnxNatPlRangeExclGroup.setStatus("current")

tmnxNatPublicIpGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 65, 2, 66)
)
tmnxNatPublicIpGroup.setObjects(
      *(("TIMETRA-NAT-MIB", "tmnxNatFwdActionAddrCpm"),
        ("TIMETRA-NAT-MIB", "tmnxNatFwdActionOutPublicIf"),
        ("TIMETRA-NAT-MIB", "tmnxNatFwd2AddrCpm"),
        ("TIMETRA-NAT-MIB", "tmnxNatFwd2OutPublicIf"),
        ("TIMETRA-NAT-MIB", "tmnxNatPlLsnCpmReservedPorts"),
        ("TIMETRA-NAT-MIB", "tmnxNatCpmPlcyRowStatus"),
        ("TIMETRA-NAT-MIB", "tmnxNatCpmPlcyTableLastCh"))
)
if mibBuilder.loadTexts:
    tmnxNatPublicIpGroup.setStatus("current")

tmnxNatObsoleteGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 65, 2, 98)
)
tmnxNatObsoleteGroup.setObjects(
      *(("TIMETRA-NAT-MIB", "tmnxNatMapLsnHostTableLastCh"),
        ("TIMETRA-NAT-MIB", "tmnxNatMapLsnHostRowStatus"),
        ("TIMETRA-NAT-MIB", "tmnxNatMapLsnHostLastMgmtChange"),
        ("TIMETRA-NAT-MIB", "tmnxNatMapLsnHostAdminState"),
        ("TIMETRA-NAT-MIB", "tmnxNatMapLsnHostOutAddrType"),
        ("TIMETRA-NAT-MIB", "tmnxNatMapLsnHostOutAddr"),
        ("TIMETRA-NAT-MIB", "tmnxNatMapLsnHostOutVRtrID"),
        ("TIMETRA-NAT-MIB", "tmnxNatMapTableLastCh"),
        ("TIMETRA-NAT-MIB", "tmnxNatMapRowStatus"),
        ("TIMETRA-NAT-MIB", "tmnxNatMapLastMgmtChange"),
        ("TIMETRA-NAT-MIB", "tmnxNatMapOutPort"),
        ("TIMETRA-NAT-MIB", "tmnxNatIsaGrpSessionResvCount"),
        ("TIMETRA-NAT-MIB", "tmnxNatIsaGrpSessionWatermarkHi"),
        ("TIMETRA-NAT-MIB", "tmnxNatIsaGrpSessionWatermarkLo"),
        ("TIMETRA-NAT-MIB", "tmnxNatApTableLastCh"),
        ("TIMETRA-NAT-MIB", "tmnxNatApLastMgmtChange"),
        ("TIMETRA-NAT-MIB", "tmnxNatApRowStatus"),
        ("TIMETRA-NAT-MIB", "tmnxNatApDescription"),
        ("TIMETRA-NAT-MIB", "tmnxNatApIncludeAttributes"),
        ("TIMETRA-NAT-MIB", "tmnxNatApServersTimeout"),
        ("TIMETRA-NAT-MIB", "tmnxNatApServersRetry"),
        ("TIMETRA-NAT-MIB", "tmnxNatApServersVRtrID"),
        ("TIMETRA-NAT-MIB", "tmnxNatApServersSrcAddrType"),
        ("TIMETRA-NAT-MIB", "tmnxNatApServersSrcAddrStart"),
        ("TIMETRA-NAT-MIB", "tmnxNatApServersSrcAddrEnd"),
        ("TIMETRA-NAT-MIB", "tmnxNatApServersAlgorithm"),
        ("TIMETRA-NAT-MIB", "tmnxNatApServTableLastCh"),
        ("TIMETRA-NAT-MIB", "tmnxNatApServRowStatus"),
        ("TIMETRA-NAT-MIB", "tmnxNatApServLastMgmtChange"),
        ("TIMETRA-NAT-MIB", "tmnxNatApServAddrType"),
        ("TIMETRA-NAT-MIB", "tmnxNatApServAddr"),
        ("TIMETRA-NAT-MIB", "tmnxNatApServSecret"),
        ("TIMETRA-NAT-MIB", "tmnxNatApServAcctPort"),
        ("TIMETRA-NAT-MIB", "tmnxNatApServStatSrcAddrType"),
        ("TIMETRA-NAT-MIB", "tmnxNatApServStatSrcAddr"),
        ("TIMETRA-NAT-MIB", "tmnxNatApServStatOperState"),
        ("TIMETRA-NAT-MIB", "tmnxNatApServStatTxRequests"),
        ("TIMETRA-NAT-MIB", "tmnxNatApServStatReqTimeout"),
        ("TIMETRA-NAT-MIB", "tmnxNatApServStatSendRetries"),
        ("TIMETRA-NAT-MIB", "tmnxNatPlRangeNumAllocatedBlk"),
        ("TIMETRA-NAT-MIB", "tmnxNatFwdOutVRtrID"),
        ("TIMETRA-NAT-MIB", "tmnxNatFwdOutAddrType"),
        ("TIMETRA-NAT-MIB", "tmnxNatFwdOutAddr"),
        ("TIMETRA-NAT-MIB", "tmnxNatFwdOutPort"),
        ("TIMETRA-NAT-MIB", "tmnxNatFwdExpiryDateAndTime"),
        ("TIMETRA-NAT-MIB", "tmnxNatFwdLsnAftrAddrType"),
        ("TIMETRA-NAT-MIB", "tmnxNatFwdLsnAftrAddr"),
        ("TIMETRA-NAT-MIB", "tmnxNatFwdPersistKey"),
        ("TIMETRA-NAT-MIB", "tmnxNatFwdDescription"),
        ("TIMETRA-NAT-MIB", "tmnxNatFwdOrigin"),
        ("TIMETRA-NAT-MIB", "tmnxNatLsnHostSubId"),
        ("TIMETRA-NAT-MIB", "tmnxNatLsnHostOutVRtrID"),
        ("TIMETRA-NAT-MIB", "tmnxNatLsnHostOutAddrType"),
        ("TIMETRA-NAT-MIB", "tmnxNatLsnHostOutAddr"),
        ("TIMETRA-NAT-MIB", "tmnxNatDsliteSubId"),
        ("TIMETRA-NAT-MIB", "tmnxNat64SubId"),
        ("TIMETRA-NAT-MIB", "tmnxNatLsnSubPolicy"),
        ("TIMETRA-NAT-MIB", "tmnxNatLsnSubIsaGrp"),
        ("TIMETRA-NAT-MIB", "tmnxNatLsnSubIsaMemberId"),
        ("TIMETRA-NAT-MIB", "tmnxNatLsnSubOutVRtrID"),
        ("TIMETRA-NAT-MIB", "tmnxNatLsnSubOutAddrType"),
        ("TIMETRA-NAT-MIB", "tmnxNatLsnSubOutAddr"),
        ("TIMETRA-NAT-MIB", "tmnxNatLsnSubStatIcmpPortUsage"),
        ("TIMETRA-NAT-MIB", "tmnxNatLsnSubStatIcmpPortUsageHi"),
        ("TIMETRA-NAT-MIB", "tmnxNatLsnSubStatUdpPortUsage"),
        ("TIMETRA-NAT-MIB", "tmnxNatLsnSubStatUdpPortUsageHi"),
        ("TIMETRA-NAT-MIB", "tmnxNatLsnSubStatTcpPortUsage"),
        ("TIMETRA-NAT-MIB", "tmnxNatLsnSubStatTcpPortUsageHi"),
        ("TIMETRA-NAT-MIB", "tmnxNatLsnSubStatSessionUsage"),
        ("TIMETRA-NAT-MIB", "tmnxNatLsnSubStatSessionUsageHi"),
        ("TIMETRA-NAT-MIB", "tmnxNatLsnSubStatSessions"),
        ("TIMETRA-NAT-MIB", "tmnxNatLsnSubStatSessionsPrio"),
        ("TIMETRA-NAT-MIB", "tmnxNatLsnSubStatSessionsPeak"),
        ("TIMETRA-NAT-MIB", "tmnxNatLsnSubIdStr"),
        ("TIMETRA-NAT-MIB", "tmnxNatL2AwSubStatCurrUpnpPlcy"),
        ("TIMETRA-NAT-MIB", "tmnxNatBlkLsnEnd"),
        ("TIMETRA-NAT-MIB", "tmnxNatBlkLsnPool"),
        ("TIMETRA-NAT-MIB", "tmnxNatBlkLsnSubId"),
        ("TIMETRA-NAT-MIB", "tmnxNatBlkLsnInsideVRtrID"),
        ("TIMETRA-NAT-MIB", "tmnxNatBlkLsnInsideAddrType"),
        ("TIMETRA-NAT-MIB", "tmnxNatBlkLsnInsideAddr"),
        ("TIMETRA-NAT-MIB", "tmnxNatBlkLsnPolicy"),
        ("TIMETRA-NAT-MIB", "tmnxNatBlkLsnStartDateAndTime"),
        ("TIMETRA-NAT-MIB", "tmnxNatGrpCfgLoadBalancing"),
        ("TIMETRA-NAT-MIB", "tmnxNatDetPlcyRowStatus"),
        ("TIMETRA-NAT-MIB", "tmnxNatDetPlcyLastMgmtChange"),
        ("TIMETRA-NAT-MIB", "tmnxNatDetPlcyName"),
        ("TIMETRA-NAT-MIB", "tmnxNatDetPlcyAdminState"),
        ("TIMETRA-NAT-MIB", "tmnxNatDetPlcyOperState"),
        ("TIMETRA-NAT-MIB", "tmnxNatDetMapRowStatus"),
        ("TIMETRA-NAT-MIB", "tmnxNatDetMapLastCh"),
        ("TIMETRA-NAT-MIB", "tmnxNatDetMapOutAddrType"),
        ("TIMETRA-NAT-MIB", "tmnxNatDetMapOutStart"),
        ("TIMETRA-NAT-MIB", "tmnxNatDetMapOperState"))
)
if mibBuilder.loadTexts:
    tmnxNatObsoleteGroup.setStatus("current")

tmnxNatNotifyObjsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 65, 2, 99)
)
tmnxNatNotifyObjsGroup.setObjects(
      *(("TIMETRA-NAT-MIB", "tmnxNatNotifyDescription"),
        ("TIMETRA-NAT-MIB", "tmnxNatNotifyOutsideVRtrID"),
        ("TIMETRA-NAT-MIB", "tmnxNatNotifyInsideVRtrID"),
        ("TIMETRA-NAT-MIB", "tmnxNatNotifyOutsideAddrType"),
        ("TIMETRA-NAT-MIB", "tmnxNatNotifyOutsideAddr"),
        ("TIMETRA-NAT-MIB", "tmnxNatNotifyOutsideEndAddrType"),
        ("TIMETRA-NAT-MIB", "tmnxNatNotifyOutsideEndAddr"),
        ("TIMETRA-NAT-MIB", "tmnxNatNotifyInsideAddrType"),
        ("TIMETRA-NAT-MIB", "tmnxNatNotifyInsideAddr"),
        ("TIMETRA-NAT-MIB", "tmnxNatNotifyPort"),
        ("TIMETRA-NAT-MIB", "tmnxNatNotifyPort2"),
        ("TIMETRA-NAT-MIB", "tmnxNatNotifyDateAndTime"),
        ("TIMETRA-NAT-MIB", "tmnxNatNotifyTruthValue"),
        ("TIMETRA-NAT-MIB", "tmnxNatNotifyLsnSubId"),
        ("TIMETRA-NAT-MIB", "tmnxNatNotifyL2AwSubIdent"),
        ("TIMETRA-NAT-MIB", "tmnxNatNotifyPlSeqNum"),
        ("TIMETRA-NAT-MIB", "tmnxNatNotifySubscriberType"),
        ("TIMETRA-NAT-MIB", "tmnxNatNotifyMdaChassisIndex"),
        ("TIMETRA-NAT-MIB", "tmnxNatNotifyMdaCardSlotNum"),
        ("TIMETRA-NAT-MIB", "tmnxNatNotifyMdaSlotNum"),
        ("TIMETRA-NAT-MIB", "tmnxNatNotifyCounter"),
        ("TIMETRA-NAT-MIB", "tmnxNatNotifyNumber"),
        ("TIMETRA-NAT-MIB", "tmnxNatNotifyInsideAddrPrefixLen"),
        ("TIMETRA-NAT-MIB", "tmnxNatNotifyName"),
        ("TIMETRA-NAT-MIB", "tmnxNatNotifyIsaGrpId"),
        ("TIMETRA-NAT-MIB", "tmnxNatNotifyIsaMemberId"),
        ("TIMETRA-NAT-MIB", "tmnxNatNotifyMemberSubOrHostType"),
        ("TIMETRA-NAT-MIB", "tmnxNatNotifyMemberSubOrHostDesc"),
        ("TIMETRA-NAT-MIB", "tmnxNatNotifyIsaMemberEsaNum"),
        ("TIMETRA-NAT-MIB", "tmnxNatNotifyIsaMemberEsaVappNum"),
        ("TIMETRA-NAT-MIB", "tmnxNatNotifyPoolName"),
        ("TIMETRA-NAT-MIB", "tmnxNatNotifyOutsideIPv4AddrType"),
        ("TIMETRA-NAT-MIB", "tmnxNatNotifyOutsideIPv4Addr"),
        ("TIMETRA-NAT-MIB", "tmnxNatNotifyMbrExPrtBlckUsageHi"),
        ("TIMETRA-NAT-MIB", "tmnxNatNotifyPolicyIndex"),
        ("TIMETRA-NAT-MIB", "tmnxNatNotifyPlLsnMbrPortUsageHi"),
        ("TIMETRA-NAT-MIB", "tmnxNatNotifyPlLsnMbrProtocol"),
        ("TIMETRA-NAT-MIB", "tmnxNatNotifyInterimUpdate"))
)
if mibBuilder.loadTexts:
    tmnxNatNotifyObjsGroup.setStatus("current")

tmnxNatPlcyXmppEnhGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 65, 2, 106)
)
tmnxNatPlcyXmppEnhGroup.setObjects(
    ("TIMETRA-NAT-MIB", "tmnxNatPlcyCreationOrigin")
)
if mibBuilder.loadTexts:
    tmnxNatPlcyXmppEnhGroup.setStatus("current")

tmnxNatFwdCfgGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 65, 2, 107)
)
tmnxNatFwdCfgGroup.setObjects(
      *(("TIMETRA-NAT-MIB", "tmnxNatFwdActionSaveConfig"),
        ("TIMETRA-NAT-MIB", "tmnxNatFwd2Persistence"))
)
if mibBuilder.loadTexts:
    tmnxNatFwdCfgGroup.setStatus("current")

tmnxNatL2AwV14v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 65, 2, 108)
)
tmnxNatL2AwV14v0Group.setObjects(
      *(("TIMETRA-NAT-MIB", "tmnxNatL2AwAddrTableLastCh"),
        ("TIMETRA-NAT-MIB", "tmnxNatL2AwAddrRowStatus"),
        ("TIMETRA-NAT-MIB", "tmnxNatL2AwAddrLastMgmtChange"),
        ("TIMETRA-NAT-MIB", "tmnxNatPlL2AwBlockUsage"),
        ("TIMETRA-NAT-MIB", "tmnxNatPlL2AwBlockUsageHi"),
        ("TIMETRA-NAT-MIB", "tmnxNatBlkL2AwEnd"),
        ("TIMETRA-NAT-MIB", "tmnxNatBlkL2AwPool"),
        ("TIMETRA-NAT-MIB", "tmnxNatBlkL2AwSubIdent"),
        ("TIMETRA-NAT-MIB", "tmnxNatBlkL2AwPolicy"),
        ("TIMETRA-NAT-MIB", "tmnxNatBlkL2AwStartDateAndTime"),
        ("TIMETRA-NAT-MIB", "tmnxNatPrefixTableLastCh"),
        ("TIMETRA-NAT-MIB", "tmnxNatPrefixRowStatus"),
        ("TIMETRA-NAT-MIB", "tmnxNatPrefixLastMgmtCh"),
        ("TIMETRA-NAT-MIB", "tmnxNatPrefixNatPolicy"),
        ("TIMETRA-NAT-MIB", "tmnxNatPrefixListTableLastCh"),
        ("TIMETRA-NAT-MIB", "tmnxNatPrefixListRowStatus"),
        ("TIMETRA-NAT-MIB", "tmnxNatPrefixListLastMgmtChange"),
        ("TIMETRA-NAT-MIB", "tmnxNatPrefixListApplication"),
        ("TIMETRA-NAT-MIB", "tmnxNatL2AwHostOutVRtrID"),
        ("TIMETRA-NAT-MIB", "tmnxNatL2AwHostOutAddrType"),
        ("TIMETRA-NAT-MIB", "tmnxNatL2AwHostOutAddr"),
        ("TIMETRA-NAT-MIB", "tmnxNatL2AwHostOutStart"),
        ("TIMETRA-NAT-MIB", "tmnxNatL2AwSubPolicy"),
        ("TIMETRA-NAT-MIB", "tmnxNatL2AwSubIsaGrp"),
        ("TIMETRA-NAT-MIB", "tmnxNatL2AwSubIsaMemberId"),
        ("TIMETRA-NAT-MIB", "tmnxNatL2AwSubOutVRtrID"),
        ("TIMETRA-NAT-MIB", "tmnxNatL2AwSubOutAddrType"),
        ("TIMETRA-NAT-MIB", "tmnxNatL2AwSubOutAddr"),
        ("TIMETRA-NAT-MIB", "tmnxNatL2AwSubCurrUpnpPlcy"),
        ("TIMETRA-NAT-MIB", "tmnxNatL2AwSubHostPortBlkSize"),
        ("TIMETRA-NAT-MIB", "tmnxNatL2AwSubStatIcmpPortUsage"),
        ("TIMETRA-NAT-MIB", "tmnxNatL2AwSubStatIcmpPortUsageH"),
        ("TIMETRA-NAT-MIB", "tmnxNatL2AwSubStatUdpPortUsage"),
        ("TIMETRA-NAT-MIB", "tmnxNatL2AwSubStatUdpPortUsageHi"),
        ("TIMETRA-NAT-MIB", "tmnxNatL2AwSubStatTcpPortUsage"),
        ("TIMETRA-NAT-MIB", "tmnxNatL2AwSubStatTcpPortUsageHi"),
        ("TIMETRA-NAT-MIB", "tmnxNatL2AwSubStatSessionUsage"),
        ("TIMETRA-NAT-MIB", "tmnxNatL2AwSubStatSessionUsageHi"),
        ("TIMETRA-NAT-MIB", "tmnxNatL2AwSubStatSessions"),
        ("TIMETRA-NAT-MIB", "tmnxNatL2AwSubStatSessionsPrio"),
        ("TIMETRA-NAT-MIB", "tmnxNatL2AwSubStatSessionsPeak"),
        ("TIMETRA-NAT-MIB", "tmnxNatL2AwSubBlkEnd"),
        ("TIMETRA-NAT-MIB", "tmnxNatL2AwSubPlcyOutVRtrID"),
        ("TIMETRA-NAT-MIB", "tmnxNatL2AwSubPlcyOutAddrType"),
        ("TIMETRA-NAT-MIB", "tmnxNatL2AwSubPlcyOutAddr"),
        ("TIMETRA-NAT-MIB", "tmnxNatL2AwSubPlcyDnatOvrAddrTyp"),
        ("TIMETRA-NAT-MIB", "tmnxNatL2AwSubPlcyDnatOvrAddr"),
        ("TIMETRA-NAT-MIB", "tmnxNatL2AwSubPlcyDnatDisable"),
        ("TIMETRA-NAT-MIB", "tmnxNatL2AwHostPlcyOutVRtrID"),
        ("TIMETRA-NAT-MIB", "tmnxNatL2AwHostPlcyOutAddrType"),
        ("TIMETRA-NAT-MIB", "tmnxNatL2AwHostPlcyOutAddr"),
        ("TIMETRA-NAT-MIB", "tmnxNatL2AwHostPlcyOutStart"),
        ("TIMETRA-NAT-MIB", "tmnxNatL2AwSubBlkPolicy"))
)
if mibBuilder.loadTexts:
    tmnxNatL2AwV14v0Group.setStatus("current")

tmnxNatDestinationNatGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 65, 2, 109)
)
tmnxNatDestinationNatGroup.setObjects(
      *(("TIMETRA-NAT-MIB", "tmnxNatPlcyDnatClassifier"),
        ("TIMETRA-NAT-MIB", "tmnxNatPlcyDnatRouter"),
        ("TIMETRA-NAT-MIB", "tmnxNatPlcyDnatIsaGrp"),
        ("TIMETRA-NAT-MIB", "tmnxNatVrtrInDnatSrcPrefixList"),
        ("TIMETRA-NAT-MIB", "tmnxNatVrtrOutDnatOnlyRouteLimit"),
        ("TIMETRA-NAT-MIB", "tmnxNatVrtrOutDnatOnlyRoutes"),
        ("TIMETRA-NAT-MIB", "tmnxNatClsfrTableLastCh"),
        ("TIMETRA-NAT-MIB", "tmnxNatClsfrRowStatus"),
        ("TIMETRA-NAT-MIB", "tmnxNatClsfrLastCh"),
        ("TIMETRA-NAT-MIB", "tmnxNatClsfrDescription"),
        ("TIMETRA-NAT-MIB", "tmnxNatClsfrDefaultAction"),
        ("TIMETRA-NAT-MIB", "tmnxNatClsfrDefaultActionAddrTyp"),
        ("TIMETRA-NAT-MIB", "tmnxNatClsfrDefaultActionAddr"),
        ("TIMETRA-NAT-MIB", "tmnxNatClsfrDefaultDnatAddrType"),
        ("TIMETRA-NAT-MIB", "tmnxNatClsfrDefaultDnatAddr"),
        ("TIMETRA-NAT-MIB", "tmnxNatClsfrN3RowStatus"),
        ("TIMETRA-NAT-MIB", "tmnxNatClsfrN3TableLastCh"),
        ("TIMETRA-NAT-MIB", "tmnxNatClsfrN3LastCh"),
        ("TIMETRA-NAT-MIB", "tmnxNatClsfrN3Description"),
        ("TIMETRA-NAT-MIB", "tmnxNatClsfrN3Action"),
        ("TIMETRA-NAT-MIB", "tmnxNatClsfrN3DnatAddrType"),
        ("TIMETRA-NAT-MIB", "tmnxNatClsfrN3DnatAddr"),
        ("TIMETRA-NAT-MIB", "tmnxNatClsfrN3Protocol"),
        ("TIMETRA-NAT-MIB", "tmnxNatClsfrN3DestPortStart"),
        ("TIMETRA-NAT-MIB", "tmnxNatClsfrN3DestPortEnd"),
        ("TIMETRA-NAT-MIB", "tmnxNatVrtrInImportPolicy1"),
        ("TIMETRA-NAT-MIB", "tmnxNatVrtrInImportPolicy2"),
        ("TIMETRA-NAT-MIB", "tmnxNatVrtrInImportPolicy3"),
        ("TIMETRA-NAT-MIB", "tmnxNatVrtrInImportPolicy4"),
        ("TIMETRA-NAT-MIB", "tmnxNatVrtrInImportPolicy5"),
        ("TIMETRA-NAT-MIB", "tmnxNatVrtrSourcePrefixOnly"))
)
if mibBuilder.loadTexts:
    tmnxNatDestinationNatGroup.setStatus("current")

tmnxNatMappingGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 65, 2, 111)
)
tmnxNatMappingGroup.setObjects(
      *(("TIMETRA-NAT-MIB", "tmnxNatMapDomTableLastCh"),
        ("TIMETRA-NAT-MIB", "tmnxNatMapDomRowStatus"),
        ("TIMETRA-NAT-MIB", "tmnxNatMapDomLastCh"),
        ("TIMETRA-NAT-MIB", "tmnxNatMapDomAdminState"),
        ("TIMETRA-NAT-MIB", "tmnxNatMapDomDescription"),
        ("TIMETRA-NAT-MIB", "tmnxNatMapDomDmrPrefixType"),
        ("TIMETRA-NAT-MIB", "tmnxNatMapDomDmrPrefix"),
        ("TIMETRA-NAT-MIB", "tmnxNatMapDomDmrPrefixLength"),
        ("TIMETRA-NAT-MIB", "tmnxNatMapDomTcpMssAdjust"),
        ("TIMETRA-NAT-MIB", "tmnxNatMapDomMtu"),
        ("TIMETRA-NAT-MIB", "tmnxNatMapDomIpFragmentation"),
        ("TIMETRA-NAT-MIB", "tmnxNatMapDomRouter"),
        ("TIMETRA-NAT-MIB", "tmnxNatMapRuleTableLastCh"),
        ("TIMETRA-NAT-MIB", "tmnxNatMapRuleRowStatus"),
        ("TIMETRA-NAT-MIB", "tmnxNatMapRuleLastCh"),
        ("TIMETRA-NAT-MIB", "tmnxNatMapRuleAdminState"),
        ("TIMETRA-NAT-MIB", "tmnxNatMapRuleDescription"),
        ("TIMETRA-NAT-MIB", "tmnxNatMapRulePrefixType"),
        ("TIMETRA-NAT-MIB", "tmnxNatMapRulePrefix"),
        ("TIMETRA-NAT-MIB", "tmnxNatMapRulePrefixLength"),
        ("TIMETRA-NAT-MIB", "tmnxNatMapRuleIpv4PrefixType"),
        ("TIMETRA-NAT-MIB", "tmnxNatMapRuleIpv4Prefix"),
        ("TIMETRA-NAT-MIB", "tmnxNatMapRuleIpv4PrefixLength"),
        ("TIMETRA-NAT-MIB", "tmnxNatMapRuleEaLength"),
        ("TIMETRA-NAT-MIB", "tmnxNatMapRulePsidOffset"),
        ("TIMETRA-NAT-MIB", "tmnxNatMapRuleAddrSharingRatio"),
        ("TIMETRA-NAT-MIB", "tmnxNatMapRuleExcludedPorts"),
        ("TIMETRA-NAT-MIB", "tmnxNatMapRulePortsPerUser"),
        ("TIMETRA-NAT-MIB", "tmnxNatMapVrtrDomTableLastCh"),
        ("TIMETRA-NAT-MIB", "tmnxNatMapVrtrDomRowStatus"),
        ("TIMETRA-NAT-MIB", "tmnxNatMapVrtrDomLastCh"),
        ("TIMETRA-NAT-MIB", "tmnxNatMapDomUpFwdPackets"),
        ("TIMETRA-NAT-MIB", "tmnxNatMapDomUpFwdOctets"),
        ("TIMETRA-NAT-MIB", "tmnxNatMapDomUpDropPackets"),
        ("TIMETRA-NAT-MIB", "tmnxNatMapDomUpDropOctets"),
        ("TIMETRA-NAT-MIB", "tmnxNatMapDomDownFwdPackets"),
        ("TIMETRA-NAT-MIB", "tmnxNatMapDomDownFwdOctets"),
        ("TIMETRA-NAT-MIB", "tmnxNatMapDomDownDropPackets"),
        ("TIMETRA-NAT-MIB", "tmnxNatMapDomDownDropOctets"),
        ("TIMETRA-NAT-MIB", "tmnxNatMapFragStatsName"),
        ("TIMETRA-NAT-MIB", "tmnxNatMapFragStatsVal"))
)
if mibBuilder.loadTexts:
    tmnxNatMappingGroup.setStatus("current")

tmnxNatL2AwExternalAssignGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 65, 2, 112)
)
tmnxNatL2AwExternalAssignGroup.setObjects(
    ("TIMETRA-NAT-MIB", "tmnxNatPlL2AwExternalAssignment")
)
if mibBuilder.loadTexts:
    tmnxNatL2AwExternalAssignGroup.setStatus("current")

tmnxNatFirewallGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 65, 2, 113)
)
tmnxNatFirewallGroup.setObjects(
      *(("TIMETRA-NAT-MIB", "tmnxNatPlcyPurpose"),
        ("TIMETRA-NAT-MIB", "tmnxNatPlcyToUnknownProtocol"),
        ("TIMETRA-NAT-MIB", "tmnxNatFwlPlcyTableLastCh"),
        ("TIMETRA-NAT-MIB", "tmnxNatFwlPlcyRowStatus"),
        ("TIMETRA-NAT-MIB", "tmnxNatFwlPlcyDomainRouter"),
        ("TIMETRA-NAT-MIB", "tmnxNatFwlPlcyDomainName"),
        ("TIMETRA-NAT-MIB", "tmnxNatPolicyRowStatus"),
        ("TIMETRA-NAT-MIB", "tmnxNatL2AwSubFirewallPolicy"),
        ("TIMETRA-NAT-MIB", "tmnxNatL2AwSubPlcyPurpose"),
        ("TIMETRA-NAT-MIB", "tmnxNatL2AwSubStatPlcyPurpose"),
        ("TIMETRA-NAT-MIB", "tmnxNatL2AwSubStatDownstreamDrop"),
        ("TIMETRA-NAT-MIB", "tmnxNatL2AwSubStatUnknHostDrop"),
        ("TIMETRA-NAT-MIB", "tmnxNatFwlDomRowStatus"),
        ("TIMETRA-NAT-MIB", "tmnxNatFwlDomLastMgmtChange"),
        ("TIMETRA-NAT-MIB", "tmnxNatFwlDomIsaGrp"),
        ("TIMETRA-NAT-MIB", "tmnxNatFwlDomAdminState"),
        ("TIMETRA-NAT-MIB", "tmnxNatFwlDomDhcp6ServerRouter"),
        ("TIMETRA-NAT-MIB", "tmnxNatFwlDomDhcp6ServerName"),
        ("TIMETRA-NAT-MIB", "tmnxNatFwlDomTableLastCh"),
        ("TIMETRA-NAT-MIB", "tmnxNatFwlDomPrefixRowStatus"),
        ("TIMETRA-NAT-MIB", "tmnxNatFwlDomPrefixLastCh"),
        ("TIMETRA-NAT-MIB", "tmnxNatFwlDomPrefixDescription"),
        ("TIMETRA-NAT-MIB", "tmnxNatFwlDomPrefixTableLastCh"),
        ("TIMETRA-NAT-MIB", "tmnxNatFwlHostVRtrID"),
        ("TIMETRA-NAT-MIB", "tmnxNatFwlHostDmzV6"),
        ("TIMETRA-NAT-MIB", "tmnxNatPlcyUnknProtTableLastCh"),
        ("TIMETRA-NAT-MIB", "tmnxNatPlcyUnknProtRowStatus"),
        ("TIMETRA-NAT-MIB", "tmnxNatPlcyUnknProtTimeStamp"),
        ("TIMETRA-NAT-MIB", "tmnxNatFwlNbrMacAddress"),
        ("TIMETRA-NAT-MIB", "tmnxNatFwlNbrCount"),
        ("TIMETRA-NAT-MIB", "tmnxNatFwlHostCount"),
        ("TIMETRA-NAT-MIB", "tmnxNatL2AwHostCount"))
)
if mibBuilder.loadTexts:
    tmnxNatFirewallGroup.setStatus("current")

tmnxNatL2AwV15v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 65, 2, 114)
)
tmnxNatL2AwV15v0Group.setObjects(
      *(("TIMETRA-NAT-MIB", "tmnxNatL2AwHostPlcyBypassActive"),
        ("TIMETRA-NAT-MIB", "tmnxNatL2AwHostPlcyVasFilter"),
        ("TIMETRA-NAT-MIB", "tmnxNatIsaMdaStatBypassL2AwHost"),
        ("TIMETRA-NAT-MIB", "tmnxNatIsaRecovActCardSlotNum"),
        ("TIMETRA-NAT-MIB", "tmnxNatIsaRecovActCardMDANum"),
        ("TIMETRA-NAT-MIB", "tmnxNatIsaRecovActActionGo"),
        ("TIMETRA-NAT-MIB", "tmnxNatIsaRecovActActionResult"))
)
if mibBuilder.loadTexts:
    tmnxNatL2AwV15v0Group.setStatus("current")

tmnxNatSyslogGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 65, 2, 116)
)
tmnxNatSyslogGroup.setObjects(
      *(("TIMETRA-NAT-MIB", "tmnxNatSyslogExpPlcyLastCh"),
        ("TIMETRA-NAT-MIB", "tmnxNatSyslogExpPlcyRowStatus"),
        ("TIMETRA-NAT-MIB", "tmnxNatSyslogExpPlcyDescription"),
        ("TIMETRA-NAT-MIB", "tmnxNatSyslogExpPlcyFacility"),
        ("TIMETRA-NAT-MIB", "tmnxNatSyslogExpPlcySeverity"),
        ("TIMETRA-NAT-MIB", "tmnxNatSyslogExpPlcyPrefix"),
        ("TIMETRA-NAT-MIB", "tmnxNatSyslogExpPlcyInclude"),
        ("TIMETRA-NAT-MIB", "tmnxNatSyslogExpPlcyMtu"),
        ("TIMETRA-NAT-MIB", "tmnxNatSyslogExpPlcyRateLimit"),
        ("TIMETRA-NAT-MIB", "tmnxNatSyslogExpPlcyMaxTxDelay"),
        ("TIMETRA-NAT-MIB", "tmnxNatSyslogExpPlcyTableLastCh"),
        ("TIMETRA-NAT-MIB", "tmnxNatSyslogColRowStatus"),
        ("TIMETRA-NAT-MIB", "tmnxNatSyslogColLastCh"),
        ("TIMETRA-NAT-MIB", "tmnxNatSyslogColAdminState"),
        ("TIMETRA-NAT-MIB", "tmnxNatSyslogColSrcAddrType"),
        ("TIMETRA-NAT-MIB", "tmnxNatSyslogColSrcAddr"),
        ("TIMETRA-NAT-MIB", "tmnxNatSyslogColDestPort"),
        ("TIMETRA-NAT-MIB", "tmnxNatSyslogColTableLastCh"),
        ("TIMETRA-NAT-MIB", "tmnxNatPlcySyslogExpPlcy"))
)
if mibBuilder.loadTexts:
    tmnxNatSyslogGroup.setStatus("current")

tmnxNatCupsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 65, 2, 117)
)
tmnxNatCupsGroup.setObjects(
      *(("TIMETRA-NAT-MIB", "tmnxNatUpPlcyRowStatus"),
        ("TIMETRA-NAT-MIB", "tmnxNatUpPlcyExtPortBlkSize"))
)
if mibBuilder.loadTexts:
    tmnxNatCupsGroup.setStatus("current")

tmnxNatMappingV24v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 65, 2, 120)
)
tmnxNatMappingV24v0Group.setObjects(
      *(("TIMETRA-NAT-MIB", "tmnxNatMapRuleUpFwdPackets"),
        ("TIMETRA-NAT-MIB", "tmnxNatMapRuleUpFwdOctets"),
        ("TIMETRA-NAT-MIB", "tmnxNatMapRuleUpDropPackets"),
        ("TIMETRA-NAT-MIB", "tmnxNatMapRuleUpDropOctets"),
        ("TIMETRA-NAT-MIB", "tmnxNatMapRuleDownFwdPackets"),
        ("TIMETRA-NAT-MIB", "tmnxNatMapRuleDownFwdOctets"),
        ("TIMETRA-NAT-MIB", "tmnxNatMapRuleDownDropPackets"),
        ("TIMETRA-NAT-MIB", "tmnxNatMapRuleDownDropOctets"),
        ("TIMETRA-NAT-MIB", "tmnxNatMapRuleStatsCollection"),
        ("TIMETRA-NAT-MIB", "tmnxNatMapRuleUpDropAntiSpoof"),
        ("TIMETRA-NAT-MIB", "tmnxNatMapRuleUpDropIcmp6"),
        ("TIMETRA-NAT-MIB", "tmnxNatMapRuleUpDropOther"),
        ("TIMETRA-NAT-MIB", "tmnxNatMapRuleUpFragRx"),
        ("TIMETRA-NAT-MIB", "tmnxNatMapRuleUpIcmp6NodeInfoRx"),
        ("TIMETRA-NAT-MIB", "tmnxNatMapRuleUpCpeIcmp6ErrRepRx"),
        ("TIMETRA-NAT-MIB", "tmnxNatMapRuleUpImIcmp6ErrRx"),
        ("TIMETRA-NAT-MIB", "tmnxNatMapRuleDownDropUnkPro"),
        ("TIMETRA-NAT-MIB", "tmnxNatMapRuleDownDropFragReq"),
        ("TIMETRA-NAT-MIB", "tmnxNatMapRuleDownDropIcmp4"),
        ("TIMETRA-NAT-MIB", "tmnxNatMapRuleDownFragRx"),
        ("TIMETRA-NAT-MIB", "tmnxNatMapRuleDownFragReq"),
        ("TIMETRA-NAT-MIB", "tmnxNatMapRuleDownIcmp4ErrRepRx"),
        ("TIMETRA-NAT-MIB", "tmnxNatMapRuleDownIcmp4EchoRx"),
        ("TIMETRA-NAT-MIB", "tmnxNatMapDomMapTGrpId"),
        ("TIMETRA-NAT-MIB", "tmnxNatMapDomMapTFpeId"),
        ("TIMETRA-NAT-MIB", "tmnxNatMapDomUdpV6ChksumRecalc"),
        ("TIMETRA-NAT-MIB", "tmnxNatMapDomUpDropAntiSpoof"),
        ("TIMETRA-NAT-MIB", "tmnxNatMapDomUpDropIcmp6"),
        ("TIMETRA-NAT-MIB", "tmnxNatMapDomUpDropOther"),
        ("TIMETRA-NAT-MIB", "tmnxNatMapDomUpFragRx"),
        ("TIMETRA-NAT-MIB", "tmnxNatMapDomUpIcmp6NodeInfoRx"),
        ("TIMETRA-NAT-MIB", "tmnxNatMapDomUpCpeIcmp6ErrRepRx"),
        ("TIMETRA-NAT-MIB", "tmnxNatMapDomUpImIcmp6ErrRx"),
        ("TIMETRA-NAT-MIB", "tmnxNatMapDomDownDropUnkPro"),
        ("TIMETRA-NAT-MIB", "tmnxNatMapDomDownDropFragReq"),
        ("TIMETRA-NAT-MIB", "tmnxNatMapDomDownDropIcmp4"),
        ("TIMETRA-NAT-MIB", "tmnxNatMapDomDownFragRx"),
        ("TIMETRA-NAT-MIB", "tmnxNatMapDomDownFragReq"),
        ("TIMETRA-NAT-MIB", "tmnxNatMapDomDownIcmp4ErrRepRx"),
        ("TIMETRA-NAT-MIB", "tmnxNatMapDomDownIcmp4EchoRx"),
        ("TIMETRA-NAT-MIB", "tmnxNatMapRuleUpDropUnkProto"),
        ("TIMETRA-NAT-MIB", "tmnxNatMapDomUpDropUnkProto"),
        ("TIMETRA-NAT-MIB", "tmnxMapTDomVappUpFwdPackets"),
        ("TIMETRA-NAT-MIB", "tmnxMapTDomVappUpFwdOctets"),
        ("TIMETRA-NAT-MIB", "tmnxMapTDomVappUpDropPackets"),
        ("TIMETRA-NAT-MIB", "tmnxMapTDomVappUpDropOctets"),
        ("TIMETRA-NAT-MIB", "tmnxMapTDomVappUpDropAntiSpoof"),
        ("TIMETRA-NAT-MIB", "tmnxMapTDomVappUpDropIcmp6"),
        ("TIMETRA-NAT-MIB", "tmnxMapTDomVappUpDropUnkProto"),
        ("TIMETRA-NAT-MIB", "tmnxMapTDomVappUpFragRx"),
        ("TIMETRA-NAT-MIB", "tmnxMapTDomVappUpIcmp6EchoRx"),
        ("TIMETRA-NAT-MIB", "tmnxMapTDomVappUpCpeIcmp6ErrRx"),
        ("TIMETRA-NAT-MIB", "tmnxMapTDomVappUpImIcmp6ErrRx"),
        ("TIMETRA-NAT-MIB", "tmnxMapTDomVappDownFwdPackets"),
        ("TIMETRA-NAT-MIB", "tmnxMapTDomVappDownFwdOctets"),
        ("TIMETRA-NAT-MIB", "tmnxMapTDomVappDownDropPackets"),
        ("TIMETRA-NAT-MIB", "tmnxMapTDomVappDownDropOctets"),
        ("TIMETRA-NAT-MIB", "tmnxMapTDomVappDownDropFragRx"),
        ("TIMETRA-NAT-MIB", "tmnxMapTDomVappDownDropFragReq"),
        ("TIMETRA-NAT-MIB", "tmnxMapTDomVappDownDropIcmp4"),
        ("TIMETRA-NAT-MIB", "tmnxMapTDomVappDownDropUnkProto"),
        ("TIMETRA-NAT-MIB", "tmnxMapTDomVappDownFragRx"),
        ("TIMETRA-NAT-MIB", "tmnxMapTDomVappDownFragReq"),
        ("TIMETRA-NAT-MIB", "tmnxMapTDomVappDownIcmp4EchoRx"),
        ("TIMETRA-NAT-MIB", "tmnxMapTDomVappDownIcmp4ErrRepRx"),
        ("TIMETRA-NAT-MIB", "tmnxMapTDomVappIcmp4ErrFragDf"),
        ("TIMETRA-NAT-MIB", "tmnxMapTDomVappDownUdpRecalc"),
        ("TIMETRA-NAT-MIB", "tmnxMapTRuleVappUpFwdPackets"),
        ("TIMETRA-NAT-MIB", "tmnxMapTRuleVappUpFwdOctets"),
        ("TIMETRA-NAT-MIB", "tmnxMapTRuleVappUpDropPackets"),
        ("TIMETRA-NAT-MIB", "tmnxMapTRuleVappUpDropOctets"),
        ("TIMETRA-NAT-MIB", "tmnxMapTRuleVappUpDropAntiSpoof"),
        ("TIMETRA-NAT-MIB", "tmnxMapTRuleVappUpDropIcmp6"),
        ("TIMETRA-NAT-MIB", "tmnxMapTRuleVappUpDropUnkProto"),
        ("TIMETRA-NAT-MIB", "tmnxMapTRuleVappUpFragRx"),
        ("TIMETRA-NAT-MIB", "tmnxMapTRuleVappUpIcmp6EchoRx"),
        ("TIMETRA-NAT-MIB", "tmnxMapTRuleVappUpCpeIcmp6ErrRx"),
        ("TIMETRA-NAT-MIB", "tmnxMapTRuleVappUpImIcmp6ErrRx"),
        ("TIMETRA-NAT-MIB", "tmnxMapTRuleVappDownFwdPackets"),
        ("TIMETRA-NAT-MIB", "tmnxMapTRuleVappDownFwdOctets"),
        ("TIMETRA-NAT-MIB", "tmnxMapTRuleVappDownDropPackets"),
        ("TIMETRA-NAT-MIB", "tmnxMapTRuleVappDownDropOctets"),
        ("TIMETRA-NAT-MIB", "tmnxMapTRuleVappDownDropFragRx"),
        ("TIMETRA-NAT-MIB", "tmnxMapTRuleVappDownDropFragReq"),
        ("TIMETRA-NAT-MIB", "tmnxMapTRuleVappDownDropIcmp4"),
        ("TIMETRA-NAT-MIB", "tmnxMapTRuleVappDownDropUnkProto"),
        ("TIMETRA-NAT-MIB", "tmnxMapTRuleVappDownFragRx"),
        ("TIMETRA-NAT-MIB", "tmnxMapTRuleVappDownFragReq"),
        ("TIMETRA-NAT-MIB", "tmnxMapTRuleVappDownIcmp4EchoRx"),
        ("TIMETRA-NAT-MIB", "tmnxMapTRuleVappDnIcmp4ErrRepRx"),
        ("TIMETRA-NAT-MIB", "tmnxMapTRuleVappIcmp4ErrFragDf"),
        ("TIMETRA-NAT-MIB", "tmnxMapTRuleVappDownUdpRecalc"),
        ("TIMETRA-NAT-MIB", "tmnxMapTDomVFragRxResolvedFrag"),
        ("TIMETRA-NAT-MIB", "tmnxMapTDomVFragRxUnresolvedFrag"),
        ("TIMETRA-NAT-MIB", "tmnxMapTDomVFragTxFrag"),
        ("TIMETRA-NAT-MIB", "tmnxMapTDomVFragDropFTimeout"),
        ("TIMETRA-NAT-MIB", "tmnxMapTDomVFragDropBufExhaust"),
        ("TIMETRA-NAT-MIB", "tmnxMapTDomVFragDropTooManyFrag"),
        ("TIMETRA-NAT-MIB", "tmnxMapTDomVFragDropTooManyLists"),
        ("TIMETRA-NAT-MIB", "tmnxMapTDomVFragDropFragLists"),
        ("TIMETRA-NAT-MIB", "tmnxMapTDomVFragOverlappingFirst"),
        ("TIMETRA-NAT-MIB", "tmnxMapTDomVFragListResolvedFrag"),
        ("TIMETRA-NAT-MIB", "tmnxMapTDomVFragListDroppedFrag"),
        ("TIMETRA-NAT-MIB", "tmnxNatMapDomFPUpFwdPackets"),
        ("TIMETRA-NAT-MIB", "tmnxNatMapDomFPUpFwdOctets"),
        ("TIMETRA-NAT-MIB", "tmnxNatMapDomFPUpDropAnchorIf"),
        ("TIMETRA-NAT-MIB", "tmnxNatMapDomFPUpDropAntiSpoof"),
        ("TIMETRA-NAT-MIB", "tmnxNatMapDomFPUpDropUnkProto"),
        ("TIMETRA-NAT-MIB", "tmnxNatMapDomFPDownFwdPackets"),
        ("TIMETRA-NAT-MIB", "tmnxNatMapDomFPDownFwdOctets"),
        ("TIMETRA-NAT-MIB", "tmnxNatMapDomFPDownDropAnchorIf"),
        ("TIMETRA-NAT-MIB", "tmnxNatMapDomFPDownDropUnkPro"),
        ("TIMETRA-NAT-MIB", "tmnxNatMapRuleFPUpFwdPackets"),
        ("TIMETRA-NAT-MIB", "tmnxNatMapRuleFPUpFwdOctets"),
        ("TIMETRA-NAT-MIB", "tmnxNatMapRuleFPUpDropAntiSpoof"),
        ("TIMETRA-NAT-MIB", "tmnxNatMapRuleFPDownFwdPackets"),
        ("TIMETRA-NAT-MIB", "tmnxNatMapRuleFPDownFwdOctets"))
)
if mibBuilder.loadTexts:
    tmnxNatMappingV24v0Group.setStatus("current")

tmnxNatIsaStatV16v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 65, 2, 151)
)
tmnxNatIsaStatV16v0Group.setObjects(
      *(("TIMETRA-NAT-MIB", "tmnxNatIsaResrcStatsValPeak"),
        ("TIMETRA-NAT-MIB", "tmnxNatIsaResrcStatsValPeakLw"),
        ("TIMETRA-NAT-MIB", "tmnxNatIsaResrcStatsValPeakHw"),
        ("TIMETRA-NAT-MIB", "tmnxNatIsaResrcStatsPeakTime"),
        ("TIMETRA-NAT-MIB", "tmnxNatIsaMemberResrcValPeak"),
        ("TIMETRA-NAT-MIB", "tmnxNatIsaMemberResrcPeakTime"),
        ("TIMETRA-NAT-MIB", "tmnxNatIsaMdaStatsHrTime"),
        ("TIMETRA-NAT-MIB", "tmnxNatIsaMdaStatsHrWaiting"),
        ("TIMETRA-NAT-MIB", "tmnxNatIsaMdaStatsHrIdle"),
        ("TIMETRA-NAT-MIB", "tmnxNatIsaMdaStatsHrWorking"),
        ("TIMETRA-NAT-MIB", "tmnxNatIsaMdaStatsHrJobs"),
        ("TIMETRA-NAT-MIB", "tmnxNatIsaMdaStatsHrThroughput"),
        ("TIMETRA-NAT-MIB", "tmnxNatIsaMdaStatsDayTime"),
        ("TIMETRA-NAT-MIB", "tmnxNatIsaMdaStatsDayWaiting"),
        ("TIMETRA-NAT-MIB", "tmnxNatIsaMdaStatsDayIdle"),
        ("TIMETRA-NAT-MIB", "tmnxNatIsaMdaStatsDayWorking"),
        ("TIMETRA-NAT-MIB", "tmnxNatIsaMdaStatsDayJobs"),
        ("TIMETRA-NAT-MIB", "tmnxNatIsaMdaStatsDayThroughput"),
        ("TIMETRA-NAT-MIB", "tmnxNatIsaMdaStatsMonthTime"),
        ("TIMETRA-NAT-MIB", "tmnxNatIsaMdaStatsMonthWaiting"),
        ("TIMETRA-NAT-MIB", "tmnxNatIsaMdaStatsMonthIdle"),
        ("TIMETRA-NAT-MIB", "tmnxNatIsaMdaStatsMonthWorking"),
        ("TIMETRA-NAT-MIB", "tmnxNatIsaMdaStatsMonthJobs"),
        ("TIMETRA-NAT-MIB", "tmnxNatIsaMdaStatsMonthThroughp"))
)
if mibBuilder.loadTexts:
    tmnxNatIsaStatV16v0Group.setStatus("current")

tmnxNatIsaScalingGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 65, 2, 152)
)
tmnxNatIsaScalingGroup.setObjects(
    ("TIMETRA-NAT-MIB", "tmnxNatIsaGrpScalingProfile")
)
if mibBuilder.loadTexts:
    tmnxNatIsaScalingGroup.setStatus("current")

tmnxNatDsliteReassemblyGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 65, 2, 153)
)
tmnxNatDsliteReassemblyGroup.setObjects(
    ("TIMETRA-NAT-MIB", "tmnxNatDsliteAddrReassembly")
)
if mibBuilder.loadTexts:
    tmnxNatDsliteReassemblyGroup.setStatus("current")

tmnxNatSicrGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 65, 2, 154)
)
tmnxNatSicrGroup.setObjects(
      *(("TIMETRA-NAT-MIB", "tmnxNatIsaGrpSicrReplThreshold"),
        ("TIMETRA-NAT-MIB", "tmnxNatIsaGrpSicrToAfterSwitch"),
        ("TIMETRA-NAT-MIB", "tmnxNatIsaGrpSicrRouter"),
        ("TIMETRA-NAT-MIB", "tmnxNatIsaGrpSicrLocAddrType"),
        ("TIMETRA-NAT-MIB", "tmnxNatIsaGrpSicrLocAddrStart"),
        ("TIMETRA-NAT-MIB", "tmnxNatIsaGrpSicrRemAddrType"),
        ("TIMETRA-NAT-MIB", "tmnxNatIsaGrpSicrRemAddrStart"),
        ("TIMETRA-NAT-MIB", "tmnxNatIsaGrpSicrIpMtu"),
        ("TIMETRA-NAT-MIB", "tmnxNatIsaGrpSicrPreferred"),
        ("TIMETRA-NAT-MIB", "tmnxNatIsaGrpSicrKaInterval"),
        ("TIMETRA-NAT-MIB", "tmnxNatIsaGrpSicrKaDropcount"),
        ("TIMETRA-NAT-MIB", "tmnxNatGrpMonOperGrpRowStatus"),
        ("TIMETRA-NAT-MIB", "tmnxNatGrpMonOperGrpLastCh"),
        ("TIMETRA-NAT-MIB", "tmnxNatGrpMonOperGrpHlthDrop"),
        ("TIMETRA-NAT-MIB", "tmnxNatGrpMonPortRowStatus"),
        ("TIMETRA-NAT-MIB", "tmnxNatGrpMonPortLastCh"),
        ("TIMETRA-NAT-MIB", "tmnxNatGrpMonPortHealthDrop"),
        ("TIMETRA-NAT-MIB", "tmnxNatGrpMonOperGrpTableLastCh"),
        ("TIMETRA-NAT-MIB", "tmnxNatGrpMonPortTableLastCh"),
        ("TIMETRA-NAT-MIB", "tmnxNatGrpMonOperGrpActHlthDrop"),
        ("TIMETRA-NAT-MIB", "tmnxNatGrpMonPortActHealthDrop"),
        ("TIMETRA-NAT-MIB", "tmnxNatMemSicrPeerState"),
        ("TIMETRA-NAT-MIB", "tmnxNatMemSicrState"),
        ("TIMETRA-NAT-MIB", "tmnxNatMemSicrLocAddrType"),
        ("TIMETRA-NAT-MIB", "tmnxNatMemSicrLocAddr"),
        ("TIMETRA-NAT-MIB", "tmnxNatMemSicrRemAddrType"),
        ("TIMETRA-NAT-MIB", "tmnxNatMemSicrRemAddr"),
        ("TIMETRA-NAT-MIB", "tmnxNatMemSicrStateLastFailed"),
        ("TIMETRA-NAT-MIB", "tmnxNatMemSicrStateFailReason"),
        ("TIMETRA-NAT-MIB", "tmnxNatMemSicrStateUnsupp"),
        ("TIMETRA-NAT-MIB", "tmnxNatMemSicrStateTracked"),
        ("TIMETRA-NAT-MIB", "tmnxNatMemSicrStateNotSync"),
        ("TIMETRA-NAT-MIB", "tmnxNatMemSicrStateCreatePending"),
        ("TIMETRA-NAT-MIB", "tmnxNatMemSicrStateCreateSync"),
        ("TIMETRA-NAT-MIB", "tmnxNatMemSicrStateDeleteMarked"),
        ("TIMETRA-NAT-MIB", "tmnxNatMemSicrStateDeletePending"),
        ("TIMETRA-NAT-MIB", "tmnxNatMemSicrStatsErrFrag"),
        ("TIMETRA-NAT-MIB", "tmnxNatMemSicrStatsErrNoBlk"),
        ("TIMETRA-NAT-MIB", "tmnxNatMemSicrStatsErrNoPolicy"),
        ("TIMETRA-NAT-MIB", "tmnxNatMemSicrStatsRx"),
        ("TIMETRA-NAT-MIB", "tmnxNatMemSicrStatsRxFlowCreate"),
        ("TIMETRA-NAT-MIB", "tmnxNatMemSicrStatsRxFlowDelete"),
        ("TIMETRA-NAT-MIB", "tmnxNatMemSicrStatsTx"),
        ("TIMETRA-NAT-MIB", "tmnxNatMemSicrStatsTxFlowCreate"),
        ("TIMETRA-NAT-MIB", "tmnxNatMemSicrStatsTxFlowDelete"),
        ("TIMETRA-NAT-MIB", "tmnxNatMemSicrStatsTxRetransmit"),
        ("TIMETRA-NAT-MIB", "tmnxNatMemSicrStatsRxAlg"),
        ("TIMETRA-NAT-MIB", "tmnxNatMemSicrStatsTxAlg"),
        ("TIMETRA-NAT-MIB", "tmnxNatGrpSicrHealth"),
        ("TIMETRA-NAT-MIB", "tmnxNatGrpSicrInControl"),
        ("TIMETRA-NAT-MIB", "tmnxNatGrpSicrKaTimeout"),
        ("TIMETRA-NAT-MIB", "tmnxNatGrpSicrPeerHealth"),
        ("TIMETRA-NAT-MIB", "tmnxNatGrpSicrPeerPreferred"),
        ("TIMETRA-NAT-MIB", "tmnxNatGrpSicrRx"),
        ("TIMETRA-NAT-MIB", "tmnxNatGrpSicrRxDropWrongPeer"),
        ("TIMETRA-NAT-MIB", "tmnxNatGrpSicrState"),
        ("TIMETRA-NAT-MIB", "tmnxNatGrpSicrStateChanges"),
        ("TIMETRA-NAT-MIB", "tmnxNatGrpSicrStateLastCh"),
        ("TIMETRA-NAT-MIB", "tmnxNatGrpSicrTx"),
        ("TIMETRA-NAT-MIB", "tmnxNatGrpSicrTxFailures"))
)
if mibBuilder.loadTexts:
    tmnxNatSicrGroup.setStatus("current")

tmnxNatDestinationNatV19v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 65, 2, 155)
)
tmnxNatDestinationNatV19v0Group.setObjects(
      *(("TIMETRA-NAT-MIB", "tmnxNatClsfrN3ForeignAddrType"),
        ("TIMETRA-NAT-MIB", "tmnxNatClsfrN3ForeignAddr"),
        ("TIMETRA-NAT-MIB", "tmnxNatL2AwHostPlcyDNatOverride"),
        ("TIMETRA-NAT-MIB", "tmnxNatL2AwHostPlcyDnatOvrAddrTp"),
        ("TIMETRA-NAT-MIB", "tmnxNatL2AwHostPlcyDnatOvrAddr"))
)
if mibBuilder.loadTexts:
    tmnxNatDestinationNatV19v0Group.setStatus("current")

tmnxNatLsnV19v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 65, 2, 156)
)
tmnxNatLsnV19v0Group.setObjects(
      *(("TIMETRA-NAT-MIB", "tmnxNatLsnSubBlkEnd"),
        ("TIMETRA-NAT-MIB", "tmnxNatPlLsnMemberIsaGrpId"),
        ("TIMETRA-NAT-MIB", "tmnxNatPlLsnMemberBlockUsage"),
        ("TIMETRA-NAT-MIB", "tmnxNatPlLsnMemberBlockUsageHi"),
        ("TIMETRA-NAT-MIB", "tmnxNatPlLsnSubscriberLimit"),
        ("TIMETRA-NAT-MIB", "tmnxNatPlcyBlkLimit"),
        ("TIMETRA-NAT-MIB", "tmnxNatPlMode"),
        ("TIMETRA-NAT-MIB", "tmnxNatDsliteAddrTableLastCh"),
        ("TIMETRA-NAT-MIB", "tmnxNatDsliteAddrRowStatus"),
        ("TIMETRA-NAT-MIB", "tmnxNatDsliteAddrLastMgmtChange"),
        ("TIMETRA-NAT-MIB", "tmnxNatDsliteAddrTunnelMtu"),
        ("TIMETRA-NAT-MIB", "tmnxNat64TableLastCh"),
        ("TIMETRA-NAT-MIB", "tmnxNat64LastMgmtChange"),
        ("TIMETRA-NAT-MIB", "tmnxNat64RowStatus"),
        ("TIMETRA-NAT-MIB", "tmnxNat64InAdminState"),
        ("TIMETRA-NAT-MIB", "tmnxNat64InSubPrefixLen"),
        ("TIMETRA-NAT-MIB", "tmnxNat64InPrefix"),
        ("TIMETRA-NAT-MIB", "tmnxNat64InPrefixLen"),
        ("TIMETRA-NAT-MIB", "tmnxNat64InIpv6Mtu"),
        ("TIMETRA-NAT-MIB", "tmnxNat64InDropZeroIpv4Checksum"),
        ("TIMETRA-NAT-MIB", "tmnxNat64InSetTos"),
        ("TIMETRA-NAT-MIB", "tmnxNat64InTos"),
        ("TIMETRA-NAT-MIB", "tmnxNat64InIgnoreTos"),
        ("TIMETRA-NAT-MIB", "tmnxNat64InInsertIpv6FragHeader"))
)
if mibBuilder.loadTexts:
    tmnxNatLsnV19v0Group.setStatus("current")

tmnxNatEsaV19v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 65, 2, 157)
)
tmnxNatEsaV19v0Group.setObjects(
      *(("TIMETRA-NAT-MIB", "tmnxNatVappTableLastCh"),
        ("TIMETRA-NAT-MIB", "tmnxNatVappRowStatus"),
        ("TIMETRA-NAT-MIB", "tmnxNatVappLastMgmtChange"),
        ("TIMETRA-NAT-MIB", "tmnxNatIsaMemberEsaNum"),
        ("TIMETRA-NAT-MIB", "tmnxNatIsaMemberEsaVappNum"),
        ("TIMETRA-NAT-MIB", "tmnxNatVappStatOperState"),
        ("TIMETRA-NAT-MIB", "tmnxNatVappStatResrcAllocated"),
        ("TIMETRA-NAT-MIB", "tmnxNatVappStatBypassL2AwHost"),
        ("TIMETRA-NAT-MIB", "tmnxNatVappResrcStatsLimited"),
        ("TIMETRA-NAT-MIB", "tmnxNatVappResrcStatsName"),
        ("TIMETRA-NAT-MIB", "tmnxNatVappResrcStatsPeakTime"),
        ("TIMETRA-NAT-MIB", "tmnxNatVappResrcStatsVal"),
        ("TIMETRA-NAT-MIB", "tmnxNatVappResrcStatsValHw"),
        ("TIMETRA-NAT-MIB", "tmnxNatVappResrcStatsValLw"),
        ("TIMETRA-NAT-MIB", "tmnxNatVappResrcStatsValMax"),
        ("TIMETRA-NAT-MIB", "tmnxNatVappResrcStatsValMaxHw"),
        ("TIMETRA-NAT-MIB", "tmnxNatVappResrcStatsValMaxLw"),
        ("TIMETRA-NAT-MIB", "tmnxNatVappResrcStatsValPeak"),
        ("TIMETRA-NAT-MIB", "tmnxNatVappResrcStatsValPeakHw"),
        ("TIMETRA-NAT-MIB", "tmnxNatVappResrcStatsValPeakLw"),
        ("TIMETRA-NAT-MIB", "tmnxNatVappRecovActEsaNum"),
        ("TIMETRA-NAT-MIB", "tmnxNatVappRecovActEsaVappNum"),
        ("TIMETRA-NAT-MIB", "tmnxNatVappRecovActActionGo"),
        ("TIMETRA-NAT-MIB", "tmnxNatVappRecovActActionResult"),
        ("TIMETRA-NAT-MIB", "tmnxNatVappPlcyStatsName"),
        ("TIMETRA-NAT-MIB", "tmnxNatVappPlcyStatsVal"),
        ("TIMETRA-NAT-MIB", "tmnxNatVappStatsHrTime"),
        ("TIMETRA-NAT-MIB", "tmnxNatVappStatsHrWaiting"),
        ("TIMETRA-NAT-MIB", "tmnxNatVappStatsHrIdle"),
        ("TIMETRA-NAT-MIB", "tmnxNatVappStatsHrWorking"),
        ("TIMETRA-NAT-MIB", "tmnxNatVappStatsHrJobs"),
        ("TIMETRA-NAT-MIB", "tmnxNatVappStatsHrThroughput"),
        ("TIMETRA-NAT-MIB", "tmnxNatVappStatsDayTime"),
        ("TIMETRA-NAT-MIB", "tmnxNatVappStatsDayWaiting"),
        ("TIMETRA-NAT-MIB", "tmnxNatVappStatsDayIdle"),
        ("TIMETRA-NAT-MIB", "tmnxNatVappStatsDayWorking"),
        ("TIMETRA-NAT-MIB", "tmnxNatVappStatsDayJobs"),
        ("TIMETRA-NAT-MIB", "tmnxNatVappStatsDayThroughput"),
        ("TIMETRA-NAT-MIB", "tmnxNatVappStatsMonthTime"),
        ("TIMETRA-NAT-MIB", "tmnxNatVappStatsMonthWaiting"),
        ("TIMETRA-NAT-MIB", "tmnxNatVappStatsMonthIdle"),
        ("TIMETRA-NAT-MIB", "tmnxNatVappStatsMonthWorking"),
        ("TIMETRA-NAT-MIB", "tmnxNatVappStatsMonthJobs"),
        ("TIMETRA-NAT-MIB", "tmnxNatVappStatsMonthThroughp"))
)
if mibBuilder.loadTexts:
    tmnxNatEsaV19v0Group.setStatus("current")

tmnxNatL2AwDynamicBlkAllocGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 65, 2, 161)
)
tmnxNatL2AwDynamicBlkAllocGroup.setObjects(
      *(("TIMETRA-NAT-MIB", "tmnxNatPlL2AwDynResv"),
        ("TIMETRA-NAT-MIB", "tmnxNatPlL2AwDynResvSubscrLimit"),
        ("TIMETRA-NAT-MIB", "tmnxNatPlL2AwDynResvPorts"),
        ("TIMETRA-NAT-MIB", "tmnxNatSysRadiusAcctInterimDrop"),
        ("TIMETRA-NAT-MIB", "tmnxNatPlL2AwDynResvNumShrdBlcks"))
)
if mibBuilder.loadTexts:
    tmnxNatL2AwDynamicBlkAllocGroup.setStatus("current")

tmnxNatInsideRoutesGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 65, 2, 162)
)
tmnxNatInsideRoutesGroup.setObjects(
      *(("TIMETRA-NAT-MIB", "tmnxNatInsideRoutesNatPolicy"),
        ("TIMETRA-NAT-MIB", "tmnxNatInsideRoutesType"))
)
if mibBuilder.loadTexts:
    tmnxNatInsideRoutesGroup.setStatus("current")

tmnxNatPlV21v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 65, 2, 163)
)
tmnxNatPlV21v0Group.setObjects(
      *(("TIMETRA-NAT-MIB", "tmnxNatPlIcmpEchoReply"),
        ("TIMETRA-NAT-MIB", "tmnxNatPlRangeStatNumAllocSub"))
)
if mibBuilder.loadTexts:
    tmnxNatPlV21v0Group.setStatus("current")

tmnxNatDsliteV21v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 65, 2, 164)
)
tmnxNatDsliteV21v0Group.setObjects(
    ("TIMETRA-NAT-MIB", "tmnxNatDsliteAddrMinFrstFrgSzRx")
)
if mibBuilder.loadTexts:
    tmnxNatDsliteV21v0Group.setStatus("current")

tmnxNatCupsV21v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 65, 2, 165)
)
tmnxNatCupsV21v0Group.setObjects(
    ("TIMETRA-NAT-MIB", "tmnxNatUpPlcyIcmpEchoReply")
)
if mibBuilder.loadTexts:
    tmnxNatCupsV21v0Group.setStatus("current")

tmnxNatPlWmarkV22v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 65, 2, 166)
)
tmnxNatPlWmarkV22v0Group.setObjects(
      *(("TIMETRA-NAT-MIB", "tmnxNatPlL2AwSubscrWatermarkHigh"),
        ("TIMETRA-NAT-MIB", "tmnxNatPlL2AwSubscrWatermarkLow"),
        ("TIMETRA-NAT-MIB", "tmnxNatPlL2AwSubscrUsage"),
        ("TIMETRA-NAT-MIB", "tmnxNatPlL2AwSubscrUsageHi"),
        ("TIMETRA-NAT-MIB", "tmnxNatPlExPrtBlcksWatermarkHigh"),
        ("TIMETRA-NAT-MIB", "tmnxNatPlExPrtBlcksWatermarkLow"))
)
if mibBuilder.loadTexts:
    tmnxNatPlWmarkV22v0Group.setStatus("current")

tmnxNatCupsV22v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 65, 2, 168)
)
tmnxNatCupsV22v0Group.setObjects(
      *(("TIMETRA-NAT-MIB", "tmnxNatUpPlExPrtBlcksWmarkHigh"),
        ("TIMETRA-NAT-MIB", "tmnxNatUpPlExPrtBlcksWmarkLow"))
)
if mibBuilder.loadTexts:
    tmnxNatCupsV22v0Group.setStatus("current")

tmnxNatIsaV22v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 65, 2, 169)
)
tmnxNatIsaV22v0Group.setObjects(
    ("TIMETRA-NAT-MIB", "tmnxNatIsaGrpOperGroup")
)
if mibBuilder.loadTexts:
    tmnxNatIsaV22v0Group.setStatus("current")

tmnxNatPlV22v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 65, 2, 170)
)
tmnxNatPlV22v0Group.setObjects(
      *(("TIMETRA-NAT-MIB", "tmnxNatPlPortFwdRangeStart"),
        ("TIMETRA-NAT-MIB", "tmnxNatPlDhInsideIpAddrType"),
        ("TIMETRA-NAT-MIB", "tmnxNatPlDhInsideIpAddress"),
        ("TIMETRA-NAT-MIB", "tmnxNatPlDhInsideRtrId"),
        ("TIMETRA-NAT-MIB", "tmnxNatPlDhRate"),
        ("TIMETRA-NAT-MIB", "tmnxNatPlDhForwardedPackets"),
        ("TIMETRA-NAT-MIB", "tmnxNatPlDhDroppedPackets"))
)
if mibBuilder.loadTexts:
    tmnxNatPlV22v0Group.setStatus("current")

tmnxNatPlL2AwV22v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 65, 2, 171)
)
tmnxNatPlL2AwV22v0Group.setObjects(
      *(("TIMETRA-NAT-MIB", "tmnxNatPlL2AwMemberIsaGrpId"),
        ("TIMETRA-NAT-MIB", "tmnxNatPlL2AwMemberBlockUsage"),
        ("TIMETRA-NAT-MIB", "tmnxNatPlL2AwMemberBlockUsageHi"))
)
if mibBuilder.loadTexts:
    tmnxNatPlL2AwV22v0Group.setStatus("current")

tmnxNatSicrV22v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 65, 2, 172)
)
tmnxNatSicrV22v0Group.setObjects(
    ("TIMETRA-NAT-MIB", "tmnxNatIsaGrpSicrSync")
)
if mibBuilder.loadTexts:
    tmnxNatSicrV22v0Group.setStatus("current")

tmnxNatSourcePrefixV23v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 65, 2, 173)
)
tmnxNatSourcePrefixV23v0Group.setObjects(
      *(("TIMETRA-NAT-MIB", "tmnxNatSourcePrefixRowStatus"),
        ("TIMETRA-NAT-MIB", "tmnxNatSourcePrefixLastMgmtCh"),
        ("TIMETRA-NAT-MIB", "tmnxNatSourcePrefixNatPolicy"),
        ("TIMETRA-NAT-MIB", "tmnxNatSourcePrefixTableLastCh"))
)
if mibBuilder.loadTexts:
    tmnxNatSourcePrefixV23v0Group.setStatus("current")

tmnxNatVrtrSpfPlcyV23v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 65, 2, 174)
)
tmnxNatVrtrSpfPlcyV23v0Group.setObjects(
      *(("TIMETRA-NAT-MIB", "tmnxNatVrtrSpfPlcyLastMgmChg"),
        ("TIMETRA-NAT-MIB", "tmnxNatVrtrSpfPlcyRowStatus"),
        ("TIMETRA-NAT-MIB", "tmnxNatVrtrSpfPlcyTblLastCh"))
)
if mibBuilder.loadTexts:
    tmnxNatVrtrSpfPlcyV23v0Group.setStatus("current")

tmnxNatPlV23v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 65, 2, 175)
)
tmnxNatPlV23v0Group.setObjects(
    ("TIMETRA-NAT-MIB", "tmnxNatPlAddrPooling")
)
if mibBuilder.loadTexts:
    tmnxNatPlV23v0Group.setStatus("current")

tmnxNatUpPlcyV22v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 65, 2, 176)
)
tmnxNatUpPlcyV22v0Group.setObjects(
      *(("TIMETRA-NAT-MIB", "tmnxNatUpPlcyDhInsideIpAddrType"),
        ("TIMETRA-NAT-MIB", "tmnxNatUpPlcyDhInsideIpAddress"),
        ("TIMETRA-NAT-MIB", "tmnxNatUpPlcyDhInsideRtrId"),
        ("TIMETRA-NAT-MIB", "tmnxNatUpPlcyDhRate"))
)
if mibBuilder.loadTexts:
    tmnxNatUpPlcyV22v0Group.setStatus("current")

tmnxNatVrtrV23v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 65, 2, 177)
)
tmnxNatVrtrV23v0Group.setObjects(
    ("TIMETRA-NAT-MIB", "tmnxNatVrtrInL2AwForceUniqueIp")
)
if mibBuilder.loadTexts:
    tmnxNatVrtrV23v0Group.setStatus("current")

tmnxNatLsnV23v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 65, 2, 178)
)
tmnxNatLsnV23v0Group.setObjects(
      *(("TIMETRA-NAT-MIB", "tmnxNatLsnSubPlcyOutIpAddrOutVR"),
        ("TIMETRA-NAT-MIB", "tmnxNatLsnSubPlcyOutIpBlkEnd"),
        ("TIMETRA-NAT-MIB", "tmnxNatPlLsnMbrTcpPortUsage"),
        ("TIMETRA-NAT-MIB", "tmnxNatPlLsnMbrTcpPortUsageHi"),
        ("TIMETRA-NAT-MIB", "tmnxNatPlLsnMbrUdpPortUsage"),
        ("TIMETRA-NAT-MIB", "tmnxNatPlLsnMbrUdpPortUsageHi"),
        ("TIMETRA-NAT-MIB", "tmnxNatPlLsnMbrOtherPortUsage"),
        ("TIMETRA-NAT-MIB", "tmnxNatPlLsnMbrOtherPortUsageHi"))
)
if mibBuilder.loadTexts:
    tmnxNatLsnV23v0Group.setStatus("current")

tmnxNatFwdActionV23v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 65, 2, 179)
)
tmnxNatFwdActionV23v0Group.setObjects(
    ("TIMETRA-NAT-MIB", "tmnxNatFwdActionSpfForce")
)
if mibBuilder.loadTexts:
    tmnxNatFwdActionV23v0Group.setStatus("current")

tmnxNatPlLsnV23v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 65, 2, 180)
)
tmnxNatPlLsnV23v0Group.setObjects(
      *(("TIMETRA-NAT-MIB", "tmnxNatPlLsnFreePortLimitTcp"),
        ("TIMETRA-NAT-MIB", "tmnxNatPlLsnFreePortLimitUdp"),
        ("TIMETRA-NAT-MIB", "tmnxNatPlLsnFreePortLimitIcmp"))
)
if mibBuilder.loadTexts:
    tmnxNatPlLsnV23v0Group.setStatus("current")

tmnxNatPlLsnV24v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 65, 2, 181)
)
tmnxNatPlLsnV24v0Group.setObjects(
      *(("TIMETRA-NAT-MIB", "tmnxNatPlLsnRedState"),
        ("TIMETRA-NAT-MIB", "tmnxNatPlLsnRedStateReason"))
)
if mibBuilder.loadTexts:
    tmnxNatPlLsnV24v0Group.setStatus("current")

tmnxNatIsaV24v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 65, 2, 183)
)
tmnxNatIsaV24v0Group.setObjects(
      *(("TIMETRA-NAT-MIB", "tmnxNatMapTGrpTableLastCh"),
        ("TIMETRA-NAT-MIB", "tmnxNatMapTGrpRowStatus"),
        ("TIMETRA-NAT-MIB", "tmnxNatMapTGrpLastCh"),
        ("TIMETRA-NAT-MIB", "tmnxNatMapTGrpDescription"),
        ("TIMETRA-NAT-MIB", "tmnxNatMapTGrpAdminState"),
        ("TIMETRA-NAT-MIB", "tmnxNatMapTGrpOperState"),
        ("TIMETRA-NAT-MIB", "tmnxNatMapTGrpFragPerPckt"))
)
if mibBuilder.loadTexts:
    tmnxNatIsaV24v0Group.setStatus("current")

tmnxNatEsaV24v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 65, 2, 184)
)
tmnxNatEsaV24v0Group.setObjects(
      *(("TIMETRA-NAT-MIB", "tmnxMapTVappTableLastCh"),
        ("TIMETRA-NAT-MIB", "tmnxMapTVappRowStatus"),
        ("TIMETRA-NAT-MIB", "tmnxMapTVappLastCh"),
        ("TIMETRA-NAT-MIB", "tmnxMapTVappResrcStatsName"),
        ("TIMETRA-NAT-MIB", "tmnxMapTVappResrcStatsVal"),
        ("TIMETRA-NAT-MIB", "tmnxMapTVappResrcStatsMaxVal"),
        ("TIMETRA-NAT-MIB", "tmnxMapTVappResrcStatsPeakVal"),
        ("TIMETRA-NAT-MIB", "tmnxMapTVappResrcStatsPeakTime"))
)
if mibBuilder.loadTexts:
    tmnxNatEsaV24v0Group.setStatus("current")

tmnxNatIsaV25v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 65, 2, 186)
)
tmnxNatIsaV25v0Group.setObjects(
    ("TIMETRA-NAT-MIB", "tmnxNatIsaGrpMonitorOperGroup")
)
if mibBuilder.loadTexts:
    tmnxNatIsaV25v0Group.setStatus("current")

tmnxNatPlV25v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 65, 2, 187)
)
tmnxNatPlV25v0Group.setObjects(
    ("TIMETRA-NAT-MIB", "tmnxNatPlMonitorOperGroup")
)
if mibBuilder.loadTexts:
    tmnxNatPlV25v0Group.setStatus("current")


# Notification objects

tmnxNatPlL2AwBlockUsageHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 65, 0, 1)
)
tmnxNatPlL2AwBlockUsageHigh.setObjects(
    ("TIMETRA-NAT-MIB", "tmnxNatPlL2AwBlockUsageHi")
)
if mibBuilder.loadTexts:
    tmnxNatPlL2AwBlockUsageHigh.setStatus(
        "current"
    )

tmnxNatIsaMemberSessionUsageHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 65, 0, 2)
)
tmnxNatIsaMemberSessionUsageHigh.setObjects(
      *(("TIMETRA-NAT-MIB", "tmnxNatIsaMemberSessionUsageHi"),
        ("TIMETRA-NAT-MIB", "tmnxNatIsaMemberMdaChassisIndex"),
        ("TIMETRA-NAT-MIB", "tmnxNatIsaMemberMdaCardSlotNum"),
        ("TIMETRA-NAT-MIB", "tmnxNatIsaMemberMdaSlotNum"),
        ("TIMETRA-NAT-MIB", "tmnxNatIsaMemberEsaNum"),
        ("TIMETRA-NAT-MIB", "tmnxNatIsaMemberEsaVappNum"))
)
if mibBuilder.loadTexts:
    tmnxNatIsaMemberSessionUsageHigh.setStatus(
        "current"
    )

tmnxNatPlLsnMemberBlockUsageHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 65, 0, 3)
)
tmnxNatPlLsnMemberBlockUsageHigh.setObjects(
      *(("TIMETRA-NAT-MIB", "tmnxNatPlLsnMemberBlockUsageHi"),
        ("TIMETRA-NAT-MIB", "tmnxNatIsaMemberMdaChassisIndex"),
        ("TIMETRA-NAT-MIB", "tmnxNatIsaMemberMdaCardSlotNum"),
        ("TIMETRA-NAT-MIB", "tmnxNatIsaMemberMdaSlotNum"),
        ("TIMETRA-NAT-MIB", "tmnxNatIsaMemberEsaNum"),
        ("TIMETRA-NAT-MIB", "tmnxNatIsaMemberEsaVappNum"))
)
if mibBuilder.loadTexts:
    tmnxNatPlLsnMemberBlockUsageHigh.setStatus(
        "current"
    )

tmnxNatLsnSubIcmpPortUsageHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 65, 0, 4)
)
tmnxNatLsnSubIcmpPortUsageHigh.setObjects(
      *(("TIMETRA-NAT-MIB", "tmnxNatLsnSubStatIcmpPortUsageHi"),
        ("TIMETRA-NAT-MIB", "tmnxNatNotifyInsideVRtrID"),
        ("TIMETRA-NAT-MIB", "tmnxNatNotifyInsideAddrType"),
        ("TIMETRA-NAT-MIB", "tmnxNatNotifyInsideAddr"))
)
if mibBuilder.loadTexts:
    tmnxNatLsnSubIcmpPortUsageHigh.setStatus(
        "obsolete"
    )

tmnxNatLsnSubUdpPortUsageHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 65, 0, 5)
)
tmnxNatLsnSubUdpPortUsageHigh.setObjects(
      *(("TIMETRA-NAT-MIB", "tmnxNatLsnSubStatUdpPortUsageHi"),
        ("TIMETRA-NAT-MIB", "tmnxNatNotifyInsideVRtrID"),
        ("TIMETRA-NAT-MIB", "tmnxNatNotifyInsideAddrType"),
        ("TIMETRA-NAT-MIB", "tmnxNatNotifyInsideAddr"))
)
if mibBuilder.loadTexts:
    tmnxNatLsnSubUdpPortUsageHigh.setStatus(
        "obsolete"
    )

tmnxNatLsnSubTcpPortUsageHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 65, 0, 6)
)
tmnxNatLsnSubTcpPortUsageHigh.setObjects(
      *(("TIMETRA-NAT-MIB", "tmnxNatLsnSubStatTcpPortUsageHi"),
        ("TIMETRA-NAT-MIB", "tmnxNatNotifyInsideVRtrID"),
        ("TIMETRA-NAT-MIB", "tmnxNatNotifyInsideAddrType"),
        ("TIMETRA-NAT-MIB", "tmnxNatNotifyInsideAddr"))
)
if mibBuilder.loadTexts:
    tmnxNatLsnSubTcpPortUsageHigh.setStatus(
        "obsolete"
    )

tmnxNatL2AwSubIcmpPortUsageHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 65, 0, 7)
)
tmnxNatL2AwSubIcmpPortUsageHigh.setObjects(
    ("TIMETRA-NAT-MIB", "tmnxNatL2AwSubStatIcmpPortUsageH")
)
if mibBuilder.loadTexts:
    tmnxNatL2AwSubIcmpPortUsageHigh.setStatus(
        "current"
    )

tmnxNatL2AwSubUdpPortUsageHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 65, 0, 8)
)
tmnxNatL2AwSubUdpPortUsageHigh.setObjects(
    ("TIMETRA-NAT-MIB", "tmnxNatL2AwSubStatUdpPortUsageHi")
)
if mibBuilder.loadTexts:
    tmnxNatL2AwSubUdpPortUsageHigh.setStatus(
        "current"
    )

tmnxNatL2AwSubTcpPortUsageHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 65, 0, 9)
)
tmnxNatL2AwSubTcpPortUsageHigh.setObjects(
    ("TIMETRA-NAT-MIB", "tmnxNatL2AwSubStatTcpPortUsageHi")
)
if mibBuilder.loadTexts:
    tmnxNatL2AwSubTcpPortUsageHigh.setStatus(
        "current"
    )

tmnxNatL2AwSubSessionUsageHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 65, 0, 10)
)
tmnxNatL2AwSubSessionUsageHigh.setObjects(
    ("TIMETRA-NAT-MIB", "tmnxNatL2AwSubStatSessionUsageHi")
)
if mibBuilder.loadTexts:
    tmnxNatL2AwSubSessionUsageHigh.setStatus(
        "current"
    )

tmnxNatLsnSubSessionUsageHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 65, 0, 11)
)
tmnxNatLsnSubSessionUsageHigh.setObjects(
      *(("TIMETRA-NAT-MIB", "tmnxNatLsnSubStatSessionUsageHi"),
        ("TIMETRA-NAT-MIB", "tmnxNatNotifyInsideVRtrID"),
        ("TIMETRA-NAT-MIB", "tmnxNatNotifyInsideAddrType"),
        ("TIMETRA-NAT-MIB", "tmnxNatNotifyInsideAddr"))
)
if mibBuilder.loadTexts:
    tmnxNatLsnSubSessionUsageHigh.setStatus(
        "obsolete"
    )

tmnxNatPlBlockAllocationLsn = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 65, 0, 12)
)
tmnxNatPlBlockAllocationLsn.setObjects(
      *(("TIMETRA-NAT-MIB", "tmnxNatNotifyOutsideVRtrID"),
        ("TIMETRA-NAT-MIB", "tmnxNatNotifyOutsideAddrType"),
        ("TIMETRA-NAT-MIB", "tmnxNatNotifyOutsideAddr"),
        ("TIMETRA-NAT-MIB", "tmnxNatNotifyPort"),
        ("TIMETRA-NAT-MIB", "tmnxNatNotifyPort2"),
        ("TIMETRA-NAT-MIB", "tmnxNatNotifyDateAndTime"),
        ("TIMETRA-NAT-MIB", "tmnxNatNotifyLsnSubId"),
        ("TIMETRA-NAT-MIB", "tmnxNatNotifyInsideVRtrID"),
        ("TIMETRA-NAT-MIB", "tmnxNatNotifyInsideAddrType"),
        ("TIMETRA-NAT-MIB", "tmnxNatNotifyInsideAddr"),
        ("TIMETRA-NAT-MIB", "tmnxNatNotifyTruthValue"),
        ("TIMETRA-NAT-MIB", "tmnxNatNotifyPlSeqNum"),
        ("TIMETRA-NAT-MIB", "tmnxNatNotifySubscriberType"),
        ("TIMETRA-NAT-MIB", "tmnxNatNotifyMdaChassisIndex"),
        ("TIMETRA-NAT-MIB", "tmnxNatNotifyMdaCardSlotNum"),
        ("TIMETRA-NAT-MIB", "tmnxNatNotifyMdaSlotNum"),
        ("TIMETRA-NAT-MIB", "tmnxNatNotifyNumber"),
        ("TIMETRA-NAT-MIB", "tmnxNatNotifyIsaMemberEsaNum"),
        ("TIMETRA-NAT-MIB", "tmnxNatNotifyIsaMemberEsaVappNum"),
        ("TIMETRA-NAT-MIB", "tmnxNatNotifyInterimUpdate"))
)
if mibBuilder.loadTexts:
    tmnxNatPlBlockAllocationLsn.setStatus(
        "current"
    )

tmnxNatPlBlockAllocationL2Aw = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 65, 0, 13)
)
tmnxNatPlBlockAllocationL2Aw.setObjects(
      *(("TIMETRA-NAT-MIB", "tmnxNatNotifyOutsideVRtrID"),
        ("TIMETRA-NAT-MIB", "tmnxNatNotifyOutsideAddrType"),
        ("TIMETRA-NAT-MIB", "tmnxNatNotifyOutsideAddr"),
        ("TIMETRA-NAT-MIB", "tmnxNatNotifyPort"),
        ("TIMETRA-NAT-MIB", "tmnxNatNotifyPort2"),
        ("TIMETRA-NAT-MIB", "tmnxNatNotifyDateAndTime"),
        ("TIMETRA-NAT-MIB", "tmnxNatNotifyL2AwSubIdent"),
        ("TIMETRA-NAT-MIB", "tmnxNatNotifyTruthValue"),
        ("TIMETRA-NAT-MIB", "tmnxNatNotifyPlSeqNum"),
        ("TIMETRA-NAT-MIB", "tmnxNatNotifyName"))
)
if mibBuilder.loadTexts:
    tmnxNatPlBlockAllocationL2Aw.setStatus(
        "current"
    )

tmnxNatResourceProblemDetected = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 65, 0, 14)
)
tmnxNatResourceProblemDetected.setObjects(
    ("TIMETRA-NAT-MIB", "tmnxNatResourceProblem")
)
if mibBuilder.loadTexts:
    tmnxNatResourceProblemDetected.setStatus(
        "current"
    )

tmnxNatResourceProblemCause = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 65, 0, 15)
)
tmnxNatResourceProblemCause.setObjects(
    ("TIMETRA-NAT-MIB", "tmnxNatNotifyDescription")
)
if mibBuilder.loadTexts:
    tmnxNatResourceProblemCause.setStatus(
        "current"
    )

tmnxNatPlAddrFree = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 65, 0, 16)
)
tmnxNatPlAddrFree.setObjects(
      *(("TIMETRA-NAT-MIB", "tmnxNatNotifyOutsideVRtrID"),
        ("TIMETRA-NAT-MIB", "tmnxNatNotifyOutsideAddrType"),
        ("TIMETRA-NAT-MIB", "tmnxNatNotifyOutsideAddr"),
        ("TIMETRA-NAT-MIB", "tmnxNatNotifyOutsideEndAddrType"),
        ("TIMETRA-NAT-MIB", "tmnxNatNotifyOutsideEndAddr"),
        ("TIMETRA-NAT-MIB", "tmnxNatNotifyDateAndTime"),
        ("TIMETRA-NAT-MIB", "tmnxNatNotifyInsideVRtrID"),
        ("TIMETRA-NAT-MIB", "tmnxNatNotifyDescription"),
        ("TIMETRA-NAT-MIB", "tmnxNatNotifyPlSeqNum"))
)
if mibBuilder.loadTexts:
    tmnxNatPlAddrFree.setStatus(
        "current"
    )

tmnxNatPlLsnRedActiveChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 65, 0, 17)
)
tmnxNatPlLsnRedActiveChanged.setObjects(
      *(("TIMETRA-NAT-MIB", "tmnxNatPlLsnRedActive"),
        ("TIMETRA-NAT-MIB", "tmnxNatNotifyDescription"))
)
if mibBuilder.loadTexts:
    tmnxNatPlLsnRedActiveChanged.setStatus(
        "current"
    )

tmnxNatPcpSrvStateChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 65, 0, 18)
)
tmnxNatPcpSrvStateChanged.setObjects(
      *(("TIMETRA-NAT-MIB", "tmnxNatPcpSrvState"),
        ("TIMETRA-NAT-MIB", "tmnxNatPcpSrvStateDescription"))
)
if mibBuilder.loadTexts:
    tmnxNatPcpSrvStateChanged.setStatus(
        "current"
    )

tmnxNatFwdEntryAdded = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 65, 0, 19)
)
tmnxNatFwdEntryAdded.setObjects(
      *(("TIMETRA-NAT-MIB", "tmnxNatFwdOutVRtrID"),
        ("TIMETRA-NAT-MIB", "tmnxNatFwdOutAddrType"),
        ("TIMETRA-NAT-MIB", "tmnxNatFwdOutAddr"),
        ("TIMETRA-NAT-MIB", "tmnxNatFwdOutPort"),
        ("TIMETRA-NAT-MIB", "tmnxNatFwdLsnAftrAddrType"),
        ("TIMETRA-NAT-MIB", "tmnxNatFwdLsnAftrAddr"),
        ("TIMETRA-NAT-MIB", "tmnxNatFwdOrigin"),
        ("TIMETRA-NAT-MIB", "tmnxNatNotifyTruthValue"),
        ("TIMETRA-NAT-MIB", "tmnxNatNotifyPlSeqNum"))
)
if mibBuilder.loadTexts:
    tmnxNatFwdEntryAdded.setStatus(
        "obsolete"
    )

tmnxNatMdaActive = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 65, 0, 20)
)
tmnxNatMdaActive.setObjects(
      *(("TIMETRA-NAT-MIB", "tmnxNatIsaMdaRowStatus"),
        ("TIMETRA-NAT-MIB", "tmnxNatNotifyTruthValue"))
)
if mibBuilder.loadTexts:
    tmnxNatMdaActive.setStatus(
        "current"
    )

tmnxNatLsnSubBlksFree = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 65, 0, 21)
)
tmnxNatLsnSubBlksFree.setObjects(
      *(("TIMETRA-NAT-MIB", "tmnxNatNotifyLsnSubId"),
        ("TIMETRA-NAT-MIB", "tmnxNatNotifyInsideVRtrID"),
        ("TIMETRA-NAT-MIB", "tmnxNatNotifyInsideAddrType"),
        ("TIMETRA-NAT-MIB", "tmnxNatNotifyInsideAddr"),
        ("TIMETRA-NAT-MIB", "tmnxNatNotifyPlSeqNum"),
        ("TIMETRA-NAT-MIB", "tmnxNatNotifySubscriberType"),
        ("TIMETRA-NAT-MIB", "tmnxNatNotifyMdaChassisIndex"),
        ("TIMETRA-NAT-MIB", "tmnxNatNotifyMdaCardSlotNum"),
        ("TIMETRA-NAT-MIB", "tmnxNatNotifyMdaSlotNum"),
        ("TIMETRA-NAT-MIB", "tmnxNatNotifyDateAndTime"),
        ("TIMETRA-NAT-MIB", "tmnxNatNotifyNumber"),
        ("TIMETRA-NAT-MIB", "tmnxNatNotifyIsaMemberEsaNum"),
        ("TIMETRA-NAT-MIB", "tmnxNatNotifyIsaMemberEsaVappNum"))
)
if mibBuilder.loadTexts:
    tmnxNatLsnSubBlksFree.setStatus(
        "current"
    )

tmnxNatDetPlcyChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 65, 0, 22)
)
if mibBuilder.loadTexts:
    tmnxNatDetPlcyChanged.setStatus(
        "current"
    )

tmnxNatMdaDetectsLoadSharingErr = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 65, 0, 23)
)
tmnxNatMdaDetectsLoadSharingErr.setObjects(
      *(("TIMETRA-NAT-MIB", "tmnxNatIsaMdaRowStatus"),
        ("TIMETRA-NAT-MIB", "tmnxNatNotifyCounter"))
)
if mibBuilder.loadTexts:
    tmnxNatMdaDetectsLoadSharingErr.setStatus(
        "current"
    )

tmnxNatIsaGrpOperStateChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 65, 0, 24)
)
tmnxNatIsaGrpOperStateChanged.setObjects(
    ("TIMETRA-NAT-MIB", "tmnxNatIsaGrpOperState")
)
if mibBuilder.loadTexts:
    tmnxNatIsaGrpOperStateChanged.setStatus(
        "current"
    )

tmnxNatIsaGrpIsDegraded = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 65, 0, 25)
)
tmnxNatIsaGrpIsDegraded.setObjects(
    ("TIMETRA-NAT-MIB", "tmnxNatIsaGrpDegraded")
)
if mibBuilder.loadTexts:
    tmnxNatIsaGrpIsDegraded.setStatus(
        "current"
    )

tmnxNatLsnSubIcmpPortUsgHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 65, 0, 26)
)
tmnxNatLsnSubIcmpPortUsgHigh.setObjects(
      *(("TIMETRA-NAT-MIB", "tmnxNatQryLsnSubResIcmpPortUsgHi"),
        ("TIMETRA-NAT-MIB", "tmnxNatNotifyInsideVRtrID"),
        ("TIMETRA-NAT-MIB", "tmnxNatNotifyInsideAddrType"),
        ("TIMETRA-NAT-MIB", "tmnxNatNotifyInsideAddr"))
)
if mibBuilder.loadTexts:
    tmnxNatLsnSubIcmpPortUsgHigh.setStatus(
        "current"
    )

tmnxNatLsnSubUdpPortUsgHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 65, 0, 27)
)
tmnxNatLsnSubUdpPortUsgHigh.setObjects(
      *(("TIMETRA-NAT-MIB", "tmnxNatQryLsnSubResUdpPortUsgHi"),
        ("TIMETRA-NAT-MIB", "tmnxNatNotifyInsideVRtrID"),
        ("TIMETRA-NAT-MIB", "tmnxNatNotifyInsideAddrType"),
        ("TIMETRA-NAT-MIB", "tmnxNatNotifyInsideAddr"))
)
if mibBuilder.loadTexts:
    tmnxNatLsnSubUdpPortUsgHigh.setStatus(
        "current"
    )

tmnxNatLsnSubTcpPortUsgHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 65, 0, 28)
)
tmnxNatLsnSubTcpPortUsgHigh.setObjects(
      *(("TIMETRA-NAT-MIB", "tmnxNatQryLsnSubResTcpPortUsgHi"),
        ("TIMETRA-NAT-MIB", "tmnxNatNotifyInsideVRtrID"),
        ("TIMETRA-NAT-MIB", "tmnxNatNotifyInsideAddrType"),
        ("TIMETRA-NAT-MIB", "tmnxNatNotifyInsideAddr"))
)
if mibBuilder.loadTexts:
    tmnxNatLsnSubTcpPortUsgHigh.setStatus(
        "current"
    )

tmnxNatLsnSubSessionUsgHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 65, 0, 29)
)
tmnxNatLsnSubSessionUsgHigh.setObjects(
      *(("TIMETRA-NAT-MIB", "tmnxNatQryLsnSubResSessionUsgHi"),
        ("TIMETRA-NAT-MIB", "tmnxNatNotifyInsideVRtrID"),
        ("TIMETRA-NAT-MIB", "tmnxNatNotifyInsideAddrType"),
        ("TIMETRA-NAT-MIB", "tmnxNatNotifyInsideAddr"))
)
if mibBuilder.loadTexts:
    tmnxNatLsnSubSessionUsgHigh.setStatus(
        "current"
    )

tmnxNatInAddrPrefixBlksFree = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 65, 0, 30)
)
tmnxNatInAddrPrefixBlksFree.setObjects(
      *(("TIMETRA-NAT-MIB", "tmnxNatNotifySubscriberType"),
        ("TIMETRA-NAT-MIB", "tmnxNatNotifyInsideVRtrID"),
        ("TIMETRA-NAT-MIB", "tmnxNatNotifyInsideAddrType"),
        ("TIMETRA-NAT-MIB", "tmnxNatNotifyInsideAddr"),
        ("TIMETRA-NAT-MIB", "tmnxNatNotifyInsideAddrPrefixLen"),
        ("TIMETRA-NAT-MIB", "tmnxNatNotifyPlSeqNum"),
        ("TIMETRA-NAT-MIB", "tmnxNatNotifyMdaChassisIndex"),
        ("TIMETRA-NAT-MIB", "tmnxNatNotifyMdaCardSlotNum"),
        ("TIMETRA-NAT-MIB", "tmnxNatNotifyMdaSlotNum"),
        ("TIMETRA-NAT-MIB", "tmnxNatNotifyDateAndTime"),
        ("TIMETRA-NAT-MIB", "tmnxNatNotifyDescription"),
        ("TIMETRA-NAT-MIB", "tmnxNatNotifyIsaMemberEsaNum"),
        ("TIMETRA-NAT-MIB", "tmnxNatNotifyIsaMemberEsaVappNum"),
        ("TIMETRA-NAT-MIB", "tmnxNatNotifyPolicyIndex"))
)
if mibBuilder.loadTexts:
    tmnxNatInAddrPrefixBlksFree.setStatus(
        "current"
    )

tmnxNatFwd2EntryAdded = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 65, 0, 31)
)
tmnxNatFwd2EntryAdded.setObjects(
      *(("TIMETRA-NAT-MIB", "tmnxNatFwd2OutVRtrID"),
        ("TIMETRA-NAT-MIB", "tmnxNatFwd2OutAddrType"),
        ("TIMETRA-NAT-MIB", "tmnxNatFwd2OutAddr"),
        ("TIMETRA-NAT-MIB", "tmnxNatFwd2OutPort"),
        ("TIMETRA-NAT-MIB", "tmnxNatFwd2LsnAftrAddrType"),
        ("TIMETRA-NAT-MIB", "tmnxNatFwd2LsnAftrAddr"),
        ("TIMETRA-NAT-MIB", "tmnxNatFwd2Origin"),
        ("TIMETRA-NAT-MIB", "tmnxNatNotifyTruthValue"),
        ("TIMETRA-NAT-MIB", "tmnxNatNotifyPlSeqNum"))
)
if mibBuilder.loadTexts:
    tmnxNatFwd2EntryAdded.setStatus(
        "current"
    )

tmnxNatDetPlcyOperStateChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 65, 0, 32)
)
tmnxNatDetPlcyOperStateChanged.setObjects(
      *(("TIMETRA-NAT-MIB", "tmnxNatDetPlcyOperState"),
        ("TIMETRA-NAT-MIB", "tmnxNatNotifyDescription"))
)
if mibBuilder.loadTexts:
    tmnxNatDetPlcyOperStateChanged.setStatus(
        "current"
    )

tmnxNatDetMapOperStateChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 65, 0, 33)
)
tmnxNatDetMapOperStateChanged.setObjects(
      *(("TIMETRA-NAT-MIB", "tmnxNatDetMapOperState"),
        ("TIMETRA-NAT-MIB", "tmnxNatNotifyDescription"))
)
if mibBuilder.loadTexts:
    tmnxNatDetMapOperStateChanged.setStatus(
        "current"
    )

tmnxNatFwd2OperStateChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 65, 0, 34)
)
tmnxNatFwd2OperStateChanged.setObjects(
    ("TIMETRA-NAT-MIB", "tmnxNatFwd2OperState")
)
if mibBuilder.loadTexts:
    tmnxNatFwd2OperStateChanged.setStatus(
        "current"
    )

tmnxNatVrtrOutDnatOnlyRoutesHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 65, 0, 35)
)
tmnxNatVrtrOutDnatOnlyRoutesHigh.setObjects(
      *(("TIMETRA-NAT-MIB", "tmnxNatVrtrOutDnatOnlyRoutes"),
        ("TIMETRA-NAT-MIB", "tmnxNatVrtrOutDnatOnlyRouteLimit"),
        ("TIMETRA-NAT-MIB", "tmnxNatNotifyTruthValue"))
)
if mibBuilder.loadTexts:
    tmnxNatVrtrOutDnatOnlyRoutesHigh.setStatus(
        "current"
    )

tmnxNatMapRuleChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 65, 0, 36)
)
tmnxNatMapRuleChange.setObjects(
      *(("TIMETRA-NAT-MIB", "tmnxNatMapRulePrefixType"),
        ("TIMETRA-NAT-MIB", "tmnxNatMapRulePrefix"),
        ("TIMETRA-NAT-MIB", "tmnxNatMapRulePrefixLength"),
        ("TIMETRA-NAT-MIB", "tmnxNatMapRuleIpv4PrefixType"),
        ("TIMETRA-NAT-MIB", "tmnxNatMapRuleIpv4Prefix"),
        ("TIMETRA-NAT-MIB", "tmnxNatMapRuleIpv4PrefixLength"),
        ("TIMETRA-NAT-MIB", "tmnxNatMapRuleEaLength"),
        ("TIMETRA-NAT-MIB", "tmnxNatMapRulePsidOffset"),
        ("TIMETRA-NAT-MIB", "tmnxNatNotifyTruthValue"),
        ("TIMETRA-VRTR-MIB", "vRtrID"),
        ("TIMETRA-NAT-MIB", "tmnxNatNotifyDateAndTime"))
)
if mibBuilder.loadTexts:
    tmnxNatMapRuleChange.setStatus(
        "current"
    )

tmnxNatMaxNbrSubsOrHostsExceeded = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 65, 0, 37)
)
tmnxNatMaxNbrSubsOrHostsExceeded.setObjects(
      *(("TIMETRA-NAT-MIB", "tmnxNatNotifyIsaGrpId"),
        ("TIMETRA-NAT-MIB", "tmnxNatNotifyIsaMemberId"),
        ("TIMETRA-NAT-MIB", "tmnxNatNotifyMemberSubOrHostType"),
        ("TIMETRA-NAT-MIB", "tmnxNatNotifyMemberSubOrHostDesc"),
        ("TIMETRA-NAT-MIB", "tmnxNatNotifyMdaChassisIndex"),
        ("TIMETRA-NAT-MIB", "tmnxNatNotifyMdaCardSlotNum"),
        ("TIMETRA-NAT-MIB", "tmnxNatNotifyMdaSlotNum"),
        ("TIMETRA-NAT-MIB", "tmnxNatNotifyDateAndTime"),
        ("TIMETRA-NAT-MIB", "tmnxNatNotifyIsaMemberEsaNum"),
        ("TIMETRA-NAT-MIB", "tmnxNatNotifyIsaMemberEsaVappNum"))
)
if mibBuilder.loadTexts:
    tmnxNatMaxNbrSubsOrHostsExceeded.setStatus(
        "current"
    )

tmnxNatNbrSubsOrHostsBelowThrsh = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 65, 0, 38)
)
tmnxNatNbrSubsOrHostsBelowThrsh.setObjects(
      *(("TIMETRA-NAT-MIB", "tmnxNatNotifyIsaGrpId"),
        ("TIMETRA-NAT-MIB", "tmnxNatNotifyIsaMemberId"),
        ("TIMETRA-NAT-MIB", "tmnxNatNotifyMemberSubOrHostType"),
        ("TIMETRA-NAT-MIB", "tmnxNatNotifyMemberSubOrHostDesc"),
        ("TIMETRA-NAT-MIB", "tmnxNatNotifyMdaChassisIndex"),
        ("TIMETRA-NAT-MIB", "tmnxNatNotifyMdaCardSlotNum"),
        ("TIMETRA-NAT-MIB", "tmnxNatNotifyMdaSlotNum"),
        ("TIMETRA-NAT-MIB", "tmnxNatNotifyDateAndTime"),
        ("TIMETRA-NAT-MIB", "tmnxNatNotifyIsaMemberEsaNum"),
        ("TIMETRA-NAT-MIB", "tmnxNatNotifyIsaMemberEsaVappNum"))
)
if mibBuilder.loadTexts:
    tmnxNatNbrSubsOrHostsBelowThrsh.setStatus(
        "current"
    )

tmnxNatVappActive = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 65, 0, 39)
)
tmnxNatVappActive.setObjects(
      *(("TIMETRA-NAT-MIB", "tmnxNatVappRowStatus"),
        ("TIMETRA-NAT-MIB", "tmnxNatNotifyTruthValue"))
)
if mibBuilder.loadTexts:
    tmnxNatVappActive.setStatus(
        "current"
    )

tmnxNatVappDetectsLoadSharingErr = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 65, 0, 40)
)
tmnxNatVappDetectsLoadSharingErr.setObjects(
      *(("TIMETRA-NAT-MIB", "tmnxNatVappRowStatus"),
        ("TIMETRA-NAT-MIB", "tmnxNatNotifyCounter"))
)
if mibBuilder.loadTexts:
    tmnxNatVappDetectsLoadSharingErr.setStatus(
        "current"
    )

tmnxNatDetPfxMapOperStateChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 65, 0, 41)
)
tmnxNatDetPfxMapOperStateChanged.setObjects(
      *(("TIMETRA-NAT-MIB", "tmnxNatDetPfxMapOperState"),
        ("TIMETRA-NAT-MIB", "tmnxNatNotifyDescription"))
)
if mibBuilder.loadTexts:
    tmnxNatDetPfxMapOperStateChanged.setStatus(
        "current"
    )

tmnxNatDetMap2OperStateChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 65, 0, 42)
)
tmnxNatDetMap2OperStateChanged.setObjects(
      *(("TIMETRA-NAT-MIB", "tmnxNatDetMap2OperState"),
        ("TIMETRA-NAT-MIB", "tmnxNatNotifyDescription"))
)
if mibBuilder.loadTexts:
    tmnxNatDetMap2OperStateChanged.setStatus(
        "current"
    )

tmnxNatDynamicConfigMismatch = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 65, 0, 43)
)
tmnxNatDynamicConfigMismatch.setObjects(
      *(("TIMETRA-NAT-MIB", "tmnxNatNotifyInsideAddrType"),
        ("TIMETRA-NAT-MIB", "tmnxNatNotifyInsideAddr"),
        ("TIMETRA-NAT-MIB", "tmnxNatNotifyInsideAddrPrefixLen"),
        ("TIMETRA-NAT-MIB", "tmnxNatNotifyOutsideVRtrID"),
        ("TIMETRA-NAT-MIB", "tmnxNatNotifyName"),
        ("TIMETRA-NAT-MIB", "tmnxNatNotifyInsideVRtrID"),
        ("TIMETRA-NAT-MIB", "tmnxNatNotifyDescription"))
)
if mibBuilder.loadTexts:
    tmnxNatDynamicConfigMismatch.setStatus(
        "current"
    )

tmnxNatPlL2AwMembrBlockUsageHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 65, 0, 44)
)
tmnxNatPlL2AwMembrBlockUsageHigh.setObjects(
      *(("TIMETRA-NAT-MIB", "tmnxNatPlL2AwSubscrUsageHi"),
        ("TIMETRA-NAT-MIB", "tmnxNatIsaMemberMdaChassisIndex"),
        ("TIMETRA-NAT-MIB", "tmnxNatIsaMemberMdaCardSlotNum"),
        ("TIMETRA-NAT-MIB", "tmnxNatIsaMemberMdaSlotNum"),
        ("TIMETRA-NAT-MIB", "tmnxNatIsaMemberEsaNum"),
        ("TIMETRA-NAT-MIB", "tmnxNatIsaMemberEsaVappNum"))
)
if mibBuilder.loadTexts:
    tmnxNatPlL2AwMembrBlockUsageHigh.setStatus(
        "current"
    )

tmnxNatPlMemberExtBlockUsageHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 65, 0, 45)
)
tmnxNatPlMemberExtBlockUsageHigh.setObjects(
      *(("TIMETRA-NAT-MIB", "tmnxNatNotifyMbrExPrtBlckUsageHi"),
        ("TIMETRA-VRTR-MIB", "vRtrID"),
        ("TIMETRA-NAT-MIB", "tmnxNatNotifyPoolName"),
        ("TIMETRA-NAT-MIB", "tmnxNatIsaMemberMdaChassisIndex"),
        ("TIMETRA-NAT-MIB", "tmnxNatIsaMemberMdaCardSlotNum"),
        ("TIMETRA-NAT-MIB", "tmnxNatIsaMemberMdaSlotNum"),
        ("TIMETRA-NAT-MIB", "tmnxNatIsaMemberEsaNum"),
        ("TIMETRA-NAT-MIB", "tmnxNatIsaMemberEsaVappNum"),
        ("TIMETRA-NAT-MIB", "tmnxNatNotifyOutsideIPv4AddrType"),
        ("TIMETRA-NAT-MIB", "tmnxNatNotifyOutsideIPv4Addr"))
)
if mibBuilder.loadTexts:
    tmnxNatPlMemberExtBlockUsageHigh.setStatus(
        "current"
    )

tmnxNatPlLsnMemberPortUsageHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 65, 0, 46)
)
tmnxNatPlLsnMemberPortUsageHigh.setObjects(
      *(("TIMETRA-NAT-MIB", "tmnxNatNotifyPlLsnMbrPortUsageHi"),
        ("TIMETRA-VRTR-MIB", "vRtrID"),
        ("TIMETRA-NAT-MIB", "tmnxNatNotifyPoolName"),
        ("TIMETRA-NAT-MIB", "tmnxNatNotifyPlLsnMbrProtocol"),
        ("TIMETRA-NAT-MIB", "tmnxNatIsaMemberMdaChassisIndex"),
        ("TIMETRA-NAT-MIB", "tmnxNatIsaMemberMdaCardSlotNum"),
        ("TIMETRA-NAT-MIB", "tmnxNatIsaMemberMdaSlotNum"),
        ("TIMETRA-NAT-MIB", "tmnxNatIsaMemberEsaNum"),
        ("TIMETRA-NAT-MIB", "tmnxNatIsaMemberEsaVappNum"),
        ("TIMETRA-NAT-MIB", "tmnxNatNotifyOutsideAddrType"),
        ("TIMETRA-NAT-MIB", "tmnxNatNotifyOutsideAddr"))
)
if mibBuilder.loadTexts:
    tmnxNatPlLsnMemberPortUsageHigh.setStatus(
        "current"
    )

tmnxNatDetAddrMapOperStateChngd = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 65, 0, 47)
)
tmnxNatDetAddrMapOperStateChngd.setObjects(
      *(("TIMETRA-NAT-MIB", "tmnxNatDetAddrMapOperState"),
        ("TIMETRA-NAT-MIB", "tmnxNatNotifyDescription"))
)
if mibBuilder.loadTexts:
    tmnxNatDetAddrMapOperStateChngd.setStatus(
        "current"
    )


# Notifications groups

tmnxNatNotifyGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 65, 2, 100)
)
tmnxNatNotifyGroup.setObjects(
      *(("TIMETRA-NAT-MIB", "tmnxNatPlL2AwBlockUsageHigh"),
        ("TIMETRA-NAT-MIB", "tmnxNatIsaMemberSessionUsageHigh"),
        ("TIMETRA-NAT-MIB", "tmnxNatPlLsnMemberBlockUsageHigh"),
        ("TIMETRA-NAT-MIB", "tmnxNatLsnSubIcmpPortUsageHigh"),
        ("TIMETRA-NAT-MIB", "tmnxNatLsnSubUdpPortUsageHigh"),
        ("TIMETRA-NAT-MIB", "tmnxNatLsnSubTcpPortUsageHigh"),
        ("TIMETRA-NAT-MIB", "tmnxNatL2AwSubIcmpPortUsageHigh"),
        ("TIMETRA-NAT-MIB", "tmnxNatL2AwSubUdpPortUsageHigh"),
        ("TIMETRA-NAT-MIB", "tmnxNatL2AwSubTcpPortUsageHigh"),
        ("TIMETRA-NAT-MIB", "tmnxNatL2AwSubSessionUsageHigh"),
        ("TIMETRA-NAT-MIB", "tmnxNatLsnSubSessionUsageHigh"),
        ("TIMETRA-NAT-MIB", "tmnxNatPlBlockAllocationLsn"),
        ("TIMETRA-NAT-MIB", "tmnxNatPlBlockAllocationL2Aw"),
        ("TIMETRA-NAT-MIB", "tmnxNatResourceProblemDetected"),
        ("TIMETRA-NAT-MIB", "tmnxNatResourceProblemCause"),
        ("TIMETRA-NAT-MIB", "tmnxNatPlAddrFree"))
)
if mibBuilder.loadTexts:
    tmnxNatNotifyGroup.setStatus(
        "obsolete"
    )

tmnxNatNotifyV9v0Group = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 65, 2, 101)
)
tmnxNatNotifyV9v0Group.setObjects(
    ("TIMETRA-NAT-MIB", "tmnxNatPlLsnRedActiveChanged")
)
if mibBuilder.loadTexts:
    tmnxNatNotifyV9v0Group.setStatus(
        "obsolete"
    )

tmnxNatNotifyV10v0Group = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 65, 2, 102)
)
tmnxNatNotifyV10v0Group.setObjects(
      *(("TIMETRA-NAT-MIB", "tmnxNatPcpSrvStateChanged"),
        ("TIMETRA-NAT-MIB", "tmnxNatFwdEntryAdded"))
)
if mibBuilder.loadTexts:
    tmnxNatNotifyV10v0Group.setStatus(
        "obsolete"
    )

tmnxNatNotifyV11v0Group = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 65, 2, 103)
)
tmnxNatNotifyV11v0Group.setObjects(
      *(("TIMETRA-NAT-MIB", "tmnxNatMdaActive"),
        ("TIMETRA-NAT-MIB", "tmnxNatLsnSubBlksFree"),
        ("TIMETRA-NAT-MIB", "tmnxNatDetPlcyChanged"),
        ("TIMETRA-NAT-MIB", "tmnxNatMdaDetectsLoadSharingErr"))
)
if mibBuilder.loadTexts:
    tmnxNatNotifyV11v0Group.setStatus(
        "obsolete"
    )

tmnxNatNotifyV12v0Group = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 65, 2, 104)
)
tmnxNatNotifyV12v0Group.setObjects(
      *(("TIMETRA-NAT-MIB", "tmnxNatPlL2AwBlockUsageHigh"),
        ("TIMETRA-NAT-MIB", "tmnxNatIsaMemberSessionUsageHigh"),
        ("TIMETRA-NAT-MIB", "tmnxNatPlLsnMemberBlockUsageHigh"),
        ("TIMETRA-NAT-MIB", "tmnxNatL2AwSubIcmpPortUsageHigh"),
        ("TIMETRA-NAT-MIB", "tmnxNatL2AwSubUdpPortUsageHigh"),
        ("TIMETRA-NAT-MIB", "tmnxNatL2AwSubTcpPortUsageHigh"),
        ("TIMETRA-NAT-MIB", "tmnxNatL2AwSubSessionUsageHigh"),
        ("TIMETRA-NAT-MIB", "tmnxNatPlBlockAllocationLsn"),
        ("TIMETRA-NAT-MIB", "tmnxNatPlBlockAllocationL2Aw"),
        ("TIMETRA-NAT-MIB", "tmnxNatResourceProblemDetected"),
        ("TIMETRA-NAT-MIB", "tmnxNatResourceProblemCause"),
        ("TIMETRA-NAT-MIB", "tmnxNatPlAddrFree"),
        ("TIMETRA-NAT-MIB", "tmnxNatPlLsnRedActiveChanged"),
        ("TIMETRA-NAT-MIB", "tmnxNatPcpSrvStateChanged"),
        ("TIMETRA-NAT-MIB", "tmnxNatMdaActive"),
        ("TIMETRA-NAT-MIB", "tmnxNatLsnSubBlksFree"),
        ("TIMETRA-NAT-MIB", "tmnxNatDetPlcyChanged"),
        ("TIMETRA-NAT-MIB", "tmnxNatMdaDetectsLoadSharingErr"),
        ("TIMETRA-NAT-MIB", "tmnxNatLsnSubIcmpPortUsgHigh"),
        ("TIMETRA-NAT-MIB", "tmnxNatLsnSubUdpPortUsgHigh"),
        ("TIMETRA-NAT-MIB", "tmnxNatLsnSubTcpPortUsgHigh"),
        ("TIMETRA-NAT-MIB", "tmnxNatLsnSubSessionUsgHigh"),
        ("TIMETRA-NAT-MIB", "tmnxNatFwd2EntryAdded"),
        ("TIMETRA-NAT-MIB", "tmnxNatIsaGrpOperStateChanged"),
        ("TIMETRA-NAT-MIB", "tmnxNatIsaGrpIsDegraded"),
        ("TIMETRA-NAT-MIB", "tmnxNatInAddrPrefixBlksFree"))
)
if mibBuilder.loadTexts:
    tmnxNatNotifyV12v0Group.setStatus(
        "obsolete"
    )

tmnxNatNotifyV13v0Group = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 65, 2, 105)
)
tmnxNatNotifyV13v0Group.setObjects(
      *(("TIMETRA-NAT-MIB", "tmnxNatPlL2AwBlockUsageHigh"),
        ("TIMETRA-NAT-MIB", "tmnxNatIsaMemberSessionUsageHigh"),
        ("TIMETRA-NAT-MIB", "tmnxNatPlLsnMemberBlockUsageHigh"),
        ("TIMETRA-NAT-MIB", "tmnxNatL2AwSubIcmpPortUsageHigh"),
        ("TIMETRA-NAT-MIB", "tmnxNatL2AwSubUdpPortUsageHigh"),
        ("TIMETRA-NAT-MIB", "tmnxNatL2AwSubTcpPortUsageHigh"),
        ("TIMETRA-NAT-MIB", "tmnxNatL2AwSubSessionUsageHigh"),
        ("TIMETRA-NAT-MIB", "tmnxNatPlBlockAllocationLsn"),
        ("TIMETRA-NAT-MIB", "tmnxNatPlBlockAllocationL2Aw"),
        ("TIMETRA-NAT-MIB", "tmnxNatResourceProblemDetected"),
        ("TIMETRA-NAT-MIB", "tmnxNatResourceProblemCause"),
        ("TIMETRA-NAT-MIB", "tmnxNatPlAddrFree"),
        ("TIMETRA-NAT-MIB", "tmnxNatPlLsnRedActiveChanged"),
        ("TIMETRA-NAT-MIB", "tmnxNatPcpSrvStateChanged"),
        ("TIMETRA-NAT-MIB", "tmnxNatMdaActive"),
        ("TIMETRA-NAT-MIB", "tmnxNatLsnSubBlksFree"),
        ("TIMETRA-NAT-MIB", "tmnxNatDetPlcyChanged"),
        ("TIMETRA-NAT-MIB", "tmnxNatMdaDetectsLoadSharingErr"),
        ("TIMETRA-NAT-MIB", "tmnxNatLsnSubIcmpPortUsgHigh"),
        ("TIMETRA-NAT-MIB", "tmnxNatLsnSubUdpPortUsgHigh"),
        ("TIMETRA-NAT-MIB", "tmnxNatLsnSubTcpPortUsgHigh"),
        ("TIMETRA-NAT-MIB", "tmnxNatLsnSubSessionUsgHigh"),
        ("TIMETRA-NAT-MIB", "tmnxNatFwd2EntryAdded"),
        ("TIMETRA-NAT-MIB", "tmnxNatIsaGrpOperStateChanged"),
        ("TIMETRA-NAT-MIB", "tmnxNatIsaGrpIsDegraded"),
        ("TIMETRA-NAT-MIB", "tmnxNatInAddrPrefixBlksFree"),
        ("TIMETRA-NAT-MIB", "tmnxNatDetPlcyOperStateChanged"),
        ("TIMETRA-NAT-MIB", "tmnxNatDetMapOperStateChanged"),
        ("TIMETRA-NAT-MIB", "tmnxNatFwd2OperStateChanged"))
)
if mibBuilder.loadTexts:
    tmnxNatNotifyV13v0Group.setStatus(
        "obsolete"
    )

tmnxNatNotifyV14v0Group = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 65, 2, 110)
)
tmnxNatNotifyV14v0Group.setObjects(
      *(("TIMETRA-NAT-MIB", "tmnxNatPlL2AwBlockUsageHigh"),
        ("TIMETRA-NAT-MIB", "tmnxNatIsaMemberSessionUsageHigh"),
        ("TIMETRA-NAT-MIB", "tmnxNatPlLsnMemberBlockUsageHigh"),
        ("TIMETRA-NAT-MIB", "tmnxNatL2AwSubIcmpPortUsageHigh"),
        ("TIMETRA-NAT-MIB", "tmnxNatL2AwSubUdpPortUsageHigh"),
        ("TIMETRA-NAT-MIB", "tmnxNatL2AwSubTcpPortUsageHigh"),
        ("TIMETRA-NAT-MIB", "tmnxNatL2AwSubSessionUsageHigh"),
        ("TIMETRA-NAT-MIB", "tmnxNatPlBlockAllocationLsn"),
        ("TIMETRA-NAT-MIB", "tmnxNatPlBlockAllocationL2Aw"),
        ("TIMETRA-NAT-MIB", "tmnxNatResourceProblemDetected"),
        ("TIMETRA-NAT-MIB", "tmnxNatResourceProblemCause"),
        ("TIMETRA-NAT-MIB", "tmnxNatPlAddrFree"),
        ("TIMETRA-NAT-MIB", "tmnxNatPlLsnRedActiveChanged"),
        ("TIMETRA-NAT-MIB", "tmnxNatPcpSrvStateChanged"),
        ("TIMETRA-NAT-MIB", "tmnxNatMdaActive"),
        ("TIMETRA-NAT-MIB", "tmnxNatLsnSubBlksFree"),
        ("TIMETRA-NAT-MIB", "tmnxNatDetPlcyChanged"),
        ("TIMETRA-NAT-MIB", "tmnxNatMdaDetectsLoadSharingErr"),
        ("TIMETRA-NAT-MIB", "tmnxNatLsnSubIcmpPortUsgHigh"),
        ("TIMETRA-NAT-MIB", "tmnxNatLsnSubUdpPortUsgHigh"),
        ("TIMETRA-NAT-MIB", "tmnxNatLsnSubTcpPortUsgHigh"),
        ("TIMETRA-NAT-MIB", "tmnxNatLsnSubSessionUsgHigh"),
        ("TIMETRA-NAT-MIB", "tmnxNatFwd2EntryAdded"),
        ("TIMETRA-NAT-MIB", "tmnxNatIsaGrpOperStateChanged"),
        ("TIMETRA-NAT-MIB", "tmnxNatIsaGrpIsDegraded"),
        ("TIMETRA-NAT-MIB", "tmnxNatInAddrPrefixBlksFree"),
        ("TIMETRA-NAT-MIB", "tmnxNatDetPlcyOperStateChanged"),
        ("TIMETRA-NAT-MIB", "tmnxNatDetMapOperStateChanged"),
        ("TIMETRA-NAT-MIB", "tmnxNatFwd2OperStateChanged"),
        ("TIMETRA-NAT-MIB", "tmnxNatVrtrOutDnatOnlyRoutesHigh"),
        ("TIMETRA-NAT-MIB", "tmnxNatMapRuleChange"))
)
if mibBuilder.loadTexts:
    tmnxNatNotifyV14v0Group.setStatus(
        "obsolete"
    )

tmnxNatNotifyV15v0Group = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 65, 2, 115)
)
tmnxNatNotifyV15v0Group.setObjects(
      *(("TIMETRA-NAT-MIB", "tmnxNatMaxNbrSubsOrHostsExceeded"),
        ("TIMETRA-NAT-MIB", "tmnxNatNbrSubsOrHostsBelowThrsh"))
)
if mibBuilder.loadTexts:
    tmnxNatNotifyV15v0Group.setStatus(
        "current"
    )

tmnxNatNotifyV23v0Group = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 65, 2, 119)
)
tmnxNatNotifyV23v0Group.setObjects(
      *(("TIMETRA-NAT-MIB", "tmnxNatPlL2AwBlockUsageHigh"),
        ("TIMETRA-NAT-MIB", "tmnxNatIsaMemberSessionUsageHigh"),
        ("TIMETRA-NAT-MIB", "tmnxNatPlLsnMemberBlockUsageHigh"),
        ("TIMETRA-NAT-MIB", "tmnxNatL2AwSubIcmpPortUsageHigh"),
        ("TIMETRA-NAT-MIB", "tmnxNatL2AwSubUdpPortUsageHigh"),
        ("TIMETRA-NAT-MIB", "tmnxNatL2AwSubTcpPortUsageHigh"),
        ("TIMETRA-NAT-MIB", "tmnxNatL2AwSubSessionUsageHigh"),
        ("TIMETRA-NAT-MIB", "tmnxNatPlBlockAllocationLsn"),
        ("TIMETRA-NAT-MIB", "tmnxNatPlBlockAllocationL2Aw"),
        ("TIMETRA-NAT-MIB", "tmnxNatResourceProblemDetected"),
        ("TIMETRA-NAT-MIB", "tmnxNatResourceProblemCause"),
        ("TIMETRA-NAT-MIB", "tmnxNatPlAddrFree"),
        ("TIMETRA-NAT-MIB", "tmnxNatPlLsnRedActiveChanged"),
        ("TIMETRA-NAT-MIB", "tmnxNatPcpSrvStateChanged"),
        ("TIMETRA-NAT-MIB", "tmnxNatMdaActive"),
        ("TIMETRA-NAT-MIB", "tmnxNatLsnSubBlksFree"),
        ("TIMETRA-NAT-MIB", "tmnxNatDetPlcyChanged"),
        ("TIMETRA-NAT-MIB", "tmnxNatMdaDetectsLoadSharingErr"),
        ("TIMETRA-NAT-MIB", "tmnxNatLsnSubIcmpPortUsgHigh"),
        ("TIMETRA-NAT-MIB", "tmnxNatLsnSubUdpPortUsgHigh"),
        ("TIMETRA-NAT-MIB", "tmnxNatLsnSubTcpPortUsgHigh"),
        ("TIMETRA-NAT-MIB", "tmnxNatLsnSubSessionUsgHigh"),
        ("TIMETRA-NAT-MIB", "tmnxNatFwd2EntryAdded"),
        ("TIMETRA-NAT-MIB", "tmnxNatIsaGrpOperStateChanged"),
        ("TIMETRA-NAT-MIB", "tmnxNatIsaGrpIsDegraded"),
        ("TIMETRA-NAT-MIB", "tmnxNatInAddrPrefixBlksFree"),
        ("TIMETRA-NAT-MIB", "tmnxNatFwd2OperStateChanged"),
        ("TIMETRA-NAT-MIB", "tmnxNatVrtrOutDnatOnlyRoutesHigh"),
        ("TIMETRA-NAT-MIB", "tmnxNatMapRuleChange"),
        ("TIMETRA-NAT-MIB", "tmnxNatPlLsnMemberPortUsageHigh"))
)
if mibBuilder.loadTexts:
    tmnxNatNotifyV23v0Group.setStatus(
        "current"
    )

tmnxNatObsoletedNotifyGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 65, 2, 150)
)
tmnxNatObsoletedNotifyGroup.setObjects(
      *(("TIMETRA-NAT-MIB", "tmnxNatFwdEntryAdded"),
        ("TIMETRA-NAT-MIB", "tmnxNatLsnSubIcmpPortUsageHigh"),
        ("TIMETRA-NAT-MIB", "tmnxNatLsnSubUdpPortUsageHigh"),
        ("TIMETRA-NAT-MIB", "tmnxNatLsnSubTcpPortUsageHigh"),
        ("TIMETRA-NAT-MIB", "tmnxNatLsnSubSessionUsageHigh"),
        ("TIMETRA-NAT-MIB", "tmnxNatDetPlcyOperStateChanged"),
        ("TIMETRA-NAT-MIB", "tmnxNatDetMapOperStateChanged"))
)
if mibBuilder.loadTexts:
    tmnxNatObsoletedNotifyGroup.setStatus(
        "current"
    )

tmnxNatNotifyV19v0Group = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 65, 2, 158)
)
tmnxNatNotifyV19v0Group.setObjects(
      *(("TIMETRA-NAT-MIB", "tmnxNatVappActive"),
        ("TIMETRA-NAT-MIB", "tmnxNatVappDetectsLoadSharingErr"))
)
if mibBuilder.loadTexts:
    tmnxNatNotifyV19v0Group.setStatus(
        "current"
    )

tmnxNatNotifyV21v0Group = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 65, 2, 160)
)
tmnxNatNotifyV21v0Group.setObjects(
      *(("TIMETRA-NAT-MIB", "tmnxNatDetPfxMapOperStateChanged"),
        ("TIMETRA-NAT-MIB", "tmnxNatDetMap2OperStateChanged"),
        ("TIMETRA-NAT-MIB", "tmnxNatDynamicConfigMismatch"))
)
if mibBuilder.loadTexts:
    tmnxNatNotifyV21v0Group.setStatus(
        "current"
    )

tmnxNatPlWmarkNotifyV22v0Group = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 65, 2, 167)
)
tmnxNatPlWmarkNotifyV22v0Group.setObjects(
      *(("TIMETRA-NAT-MIB", "tmnxNatPlL2AwMembrBlockUsageHigh"),
        ("TIMETRA-NAT-MIB", "tmnxNatPlMemberExtBlockUsageHigh"))
)
if mibBuilder.loadTexts:
    tmnxNatPlWmarkNotifyV22v0Group.setStatus(
        "current"
    )

tmnxNatNotifyV24v0Group = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 65, 2, 182)
)
tmnxNatNotifyV24v0Group.setObjects(
    ("TIMETRA-NAT-MIB", "tmnxNatDetAddrMapOperStateChngd")
)
if mibBuilder.loadTexts:
    tmnxNatNotifyV24v0Group.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

tmnxNatCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 65, 1, 1)
)
tmnxNatCompliance.setObjects(
      *(("TIMETRA-NAT-MIB", "tmnxNatIsaGroup"),
        ("TIMETRA-NAT-MIB", "tmnxNatPlcyGroup"),
        ("TIMETRA-NAT-MIB", "tmnxNatVrtrGroup"),
        ("TIMETRA-NAT-MIB", "tmnxNatPlGroup"),
        ("TIMETRA-NAT-MIB", "tmnxNatDestGroup"),
        ("TIMETRA-NAT-MIB", "tmnxNatL2AwGroup"),
        ("TIMETRA-NAT-MIB", "tmnxNatLsnGroup"),
        ("TIMETRA-NAT-MIB", "tmnxNatMapGroup"))
)
if mibBuilder.loadTexts:
    tmnxNatCompliance.setStatus(
        "obsolete"
    )

tmnxNatStatCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 65, 1, 2)
)
tmnxNatStatCompliance.setObjects(
      *(("TIMETRA-NAT-MIB", "tmnxNatIsaStatGroup"),
        ("TIMETRA-NAT-MIB", "tmnxNatPlcyStatGroup"))
)
if mibBuilder.loadTexts:
    tmnxNatStatCompliance.setStatus(
        "current"
    )

tmnxNatNotifyCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 65, 1, 3)
)
tmnxNatNotifyCompliance.setObjects(
    ("TIMETRA-NAT-MIB", "tmnxNatNotifyGroup")
)
if mibBuilder.loadTexts:
    tmnxNatNotifyCompliance.setStatus(
        "obsolete"
    )

tmnxNatV9v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 65, 1, 4)
)
tmnxNatV9v0Compliance.setObjects(
      *(("TIMETRA-NAT-MIB", "tmnxNatIsaGroup"),
        ("TIMETRA-NAT-MIB", "tmnxNatIsaStatGroup"),
        ("TIMETRA-NAT-MIB", "tmnxNatPlcyGroup"),
        ("TIMETRA-NAT-MIB", "tmnxNatPlcyV9v0Group"),
        ("TIMETRA-NAT-MIB", "tmnxNatPlcyStatGroup"),
        ("TIMETRA-NAT-MIB", "tmnxNatVrtrGroup"),
        ("TIMETRA-NAT-MIB", "tmnxNatVrtrV9v0Group"),
        ("TIMETRA-NAT-MIB", "tmnxNatRedGroup"),
        ("TIMETRA-NAT-MIB", "tmnxNatPlGroup"),
        ("TIMETRA-NAT-MIB", "tmnxNatPlV9v0Group"),
        ("TIMETRA-NAT-MIB", "tmnxNatDestGroup"),
        ("TIMETRA-NAT-MIB", "tmnxNatL2AwGroup"),
        ("TIMETRA-NAT-MIB", "tmnxNatLsnGroup"),
        ("TIMETRA-NAT-MIB", "tmnxNatLsnV9v0Group"),
        ("TIMETRA-NAT-MIB", "tmnxNatFwdGroup"))
)
if mibBuilder.loadTexts:
    tmnxNatV9v0Compliance.setStatus(
        "obsolete"
    )

tmnxNatNotifyV9v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 65, 1, 5)
)
tmnxNatNotifyV9v0Compliance.setObjects(
      *(("TIMETRA-NAT-MIB", "tmnxNatNotifyGroup"),
        ("TIMETRA-NAT-MIB", "tmnxNatNotifyV9v0Group"))
)
if mibBuilder.loadTexts:
    tmnxNatNotifyV9v0Compliance.setStatus(
        "obsolete"
    )

tmnxNatV10v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 65, 1, 6)
)
tmnxNatV10v0Compliance.setObjects(
      *(("TIMETRA-NAT-MIB", "tmnxNatIsaV10v0Group"),
        ("TIMETRA-NAT-MIB", "tmnxNatIsaStatGroup"),
        ("TIMETRA-NAT-MIB", "tmnxNatIsaStatV10v0Group"),
        ("TIMETRA-NAT-MIB", "tmnxNatPlcyGroup"),
        ("TIMETRA-NAT-MIB", "tmnxNatPlcyV9v0Group"),
        ("TIMETRA-NAT-MIB", "tmnxNatPlcyV10v0Group"),
        ("TIMETRA-NAT-MIB", "tmnxNatPlcyStatGroup"),
        ("TIMETRA-NAT-MIB", "tmnxNatVrtrGroup"),
        ("TIMETRA-NAT-MIB", "tmnxNatVrtrV9v0Group"),
        ("TIMETRA-NAT-MIB", "tmnxNatRedGroup"),
        ("TIMETRA-NAT-MIB", "tmnxNatPlGroup"),
        ("TIMETRA-NAT-MIB", "tmnxNatPlV9v0Group"),
        ("TIMETRA-NAT-MIB", "tmnxNatDestGroup"),
        ("TIMETRA-NAT-MIB", "tmnxNatL2AwGroup"),
        ("TIMETRA-NAT-MIB", "tmnxNatLsnGroup"),
        ("TIMETRA-NAT-MIB", "tmnxNatLsnV9v0Group"),
        ("TIMETRA-NAT-MIB", "tmnxNatFwdGroup"),
        ("TIMETRA-NAT-MIB", "tmnxNatAccGroup"),
        ("TIMETRA-NAT-MIB", "tmnxNatWlanGwGroup"),
        ("TIMETRA-NAT-MIB", "tmnxNat64Group"),
        ("TIMETRA-NAT-MIB", "tmnxNatLsnSubIdentGroup"),
        ("TIMETRA-NAT-MIB", "tmnxNatPcpGroup"))
)
if mibBuilder.loadTexts:
    tmnxNatV10v0Compliance.setStatus(
        "obsolete"
    )

tmnxNatNotifyV10v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 65, 1, 7)
)
tmnxNatNotifyV10v0Compliance.setObjects(
      *(("TIMETRA-NAT-MIB", "tmnxNatNotifyGroup"),
        ("TIMETRA-NAT-MIB", "tmnxNatNotifyV9v0Group"),
        ("TIMETRA-NAT-MIB", "tmnxNatNotifyV10v0Group"))
)
if mibBuilder.loadTexts:
    tmnxNatNotifyV10v0Compliance.setStatus(
        "obsolete"
    )

tmnxNatV11v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 65, 1, 8)
)
tmnxNatV11v0Compliance.setObjects(
      *(("TIMETRA-NAT-MIB", "tmnxNatIsaV10v0Group"),
        ("TIMETRA-NAT-MIB", "tmnxNatIsaStatGroup"),
        ("TIMETRA-NAT-MIB", "tmnxNatIsaStatV10v0Group"),
        ("TIMETRA-NAT-MIB", "tmnxNatIsaStatV11v0Group"),
        ("TIMETRA-NAT-MIB", "tmnxNatPlcyGroup"),
        ("TIMETRA-NAT-MIB", "tmnxNatPlcyV9v0Group"),
        ("TIMETRA-NAT-MIB", "tmnxNatPlcyV10v0Group"),
        ("TIMETRA-NAT-MIB", "tmnxNatPlcyStatGroup"),
        ("TIMETRA-NAT-MIB", "tmnxNatVrtrGroup"),
        ("TIMETRA-NAT-MIB", "tmnxNatVrtrV9v0Group"),
        ("TIMETRA-NAT-MIB", "tmnxNatVrtrIPFilterGroup"),
        ("TIMETRA-NAT-MIB", "tmnxNatRedGroup"),
        ("TIMETRA-NAT-MIB", "tmnxNatPlV11v0Group"),
        ("TIMETRA-NAT-MIB", "tmnxNatDestGroup"),
        ("TIMETRA-NAT-MIB", "tmnxNatL2AwGroup"),
        ("TIMETRA-NAT-MIB", "tmnxNatLsnGroup"),
        ("TIMETRA-NAT-MIB", "tmnxNatLsnV9v0Group"),
        ("TIMETRA-NAT-MIB", "tmnxNatFwdGroup"),
        ("TIMETRA-NAT-MIB", "tmnxNatAccV11v0Group"),
        ("TIMETRA-NAT-MIB", "tmnxNatWlanGwGroup"),
        ("TIMETRA-NAT-MIB", "tmnxNat64Group"),
        ("TIMETRA-NAT-MIB", "tmnxNatLsnSubIdentGroup"),
        ("TIMETRA-NAT-MIB", "tmnxNatPcpGroup"),
        ("TIMETRA-NAT-MIB", "tmnxNatDeterministicGroup"),
        ("TIMETRA-NAT-MIB", "tmnxNatFragmentIpGroup"))
)
if mibBuilder.loadTexts:
    tmnxNatV11v0Compliance.setStatus(
        "obsolete"
    )

tmnxNatNotifyV11v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 65, 1, 9)
)
tmnxNatNotifyV11v0Compliance.setObjects(
      *(("TIMETRA-NAT-MIB", "tmnxNatNotifyGroup"),
        ("TIMETRA-NAT-MIB", "tmnxNatNotifyV9v0Group"),
        ("TIMETRA-NAT-MIB", "tmnxNatNotifyV10v0Group"),
        ("TIMETRA-NAT-MIB", "tmnxNatNotifyV11v0Group"))
)
if mibBuilder.loadTexts:
    tmnxNatNotifyV11v0Compliance.setStatus(
        "obsolete"
    )

tmnxNatV12v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 65, 1, 10)
)
tmnxNatV12v0Compliance.setObjects(
      *(("TIMETRA-NAT-MIB", "tmnxNatIsaV12v0Group"),
        ("TIMETRA-NAT-MIB", "tmnxNatIsaStatGroup"),
        ("TIMETRA-NAT-MIB", "tmnxNatIsaStatV10v0Group"),
        ("TIMETRA-NAT-MIB", "tmnxNatIsaStatV11v0Group"),
        ("TIMETRA-NAT-MIB", "tmnxNatPlcyGroup"),
        ("TIMETRA-NAT-MIB", "tmnxNatPlcyV9v0Group"),
        ("TIMETRA-NAT-MIB", "tmnxNatPlcyV10v0Group"),
        ("TIMETRA-NAT-MIB", "tmnxNatPlcyStatGroup"),
        ("TIMETRA-NAT-MIB", "tmnxNatVrtrGroup"),
        ("TIMETRA-NAT-MIB", "tmnxNatVrtrV9v0Group"),
        ("TIMETRA-NAT-MIB", "tmnxNatVrtrIPFilterGroup"),
        ("TIMETRA-NAT-MIB", "tmnxNatRedGroup"),
        ("TIMETRA-NAT-MIB", "tmnxNatPlV11v0Group"),
        ("TIMETRA-NAT-MIB", "tmnxNatDestGroup"),
        ("TIMETRA-NAT-MIB", "tmnxNatL2AwGroup"),
        ("TIMETRA-NAT-MIB", "tmnxNatLsnV12v0Group"),
        ("TIMETRA-NAT-MIB", "tmnxNatAccV11v0Group"),
        ("TIMETRA-NAT-MIB", "tmnxNatWlanGwGroup"),
        ("TIMETRA-NAT-MIB", "tmnxNatLsnSubIdentV12v0Group"),
        ("TIMETRA-NAT-MIB", "tmnxNatPcpGroup"),
        ("TIMETRA-NAT-MIB", "tmnxNatDeterministicGroup"),
        ("TIMETRA-NAT-MIB", "tmnxNatFragmentIpGroup"),
        ("TIMETRA-NAT-MIB", "tmnxNatFwd2Group"),
        ("TIMETRA-NAT-MIB", "tmnxNatMultiPlcyGroup"),
        ("TIMETRA-NAT-MIB", "tmnxNatQryGroup"),
        ("TIMETRA-NAT-MIB", "tmnxNatVrtrIPFilterV12v0Group"))
)
if mibBuilder.loadTexts:
    tmnxNatV12v0Compliance.setStatus(
        "obsolete"
    )

tmnxNatNotifyV12v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 65, 1, 11)
)
tmnxNatNotifyV12v0Compliance.setObjects(
    ("TIMETRA-NAT-MIB", "tmnxNatNotifyV12v0Group")
)
if mibBuilder.loadTexts:
    tmnxNatNotifyV12v0Compliance.setStatus(
        "obsolete"
    )

tmnxNatV13v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 65, 1, 12)
)
tmnxNatV13v0Compliance.setObjects(
      *(("TIMETRA-NAT-MIB", "tmnxNatIsaV12v0Group"),
        ("TIMETRA-NAT-MIB", "tmnxNatIsaStatGroup"),
        ("TIMETRA-NAT-MIB", "tmnxNatIsaStatV10v0Group"),
        ("TIMETRA-NAT-MIB", "tmnxNatIsaStatV11v0Group"),
        ("TIMETRA-NAT-MIB", "tmnxNatPlcyGroup"),
        ("TIMETRA-NAT-MIB", "tmnxNatPlcyV9v0Group"),
        ("TIMETRA-NAT-MIB", "tmnxNatPlcyV10v0Group"),
        ("TIMETRA-NAT-MIB", "tmnxNatPlcyStatGroup"),
        ("TIMETRA-NAT-MIB", "tmnxNatVrtrGroup"),
        ("TIMETRA-NAT-MIB", "tmnxNatVrtrV9v0Group"),
        ("TIMETRA-NAT-MIB", "tmnxNatVrtrIPFilterGroup"),
        ("TIMETRA-NAT-MIB", "tmnxNatRedGroup"),
        ("TIMETRA-NAT-MIB", "tmnxNatPlV11v0Group"),
        ("TIMETRA-NAT-MIB", "tmnxNatDestGroup"),
        ("TIMETRA-NAT-MIB", "tmnxNatL2AwGroup"),
        ("TIMETRA-NAT-MIB", "tmnxNatLsnV12v0Group"),
        ("TIMETRA-NAT-MIB", "tmnxNatAccV11v0Group"),
        ("TIMETRA-NAT-MIB", "tmnxNatWlanGwGroup"),
        ("TIMETRA-NAT-MIB", "tmnxNatLsnSubIdentV12v0Group"),
        ("TIMETRA-NAT-MIB", "tmnxNatPcpGroup"),
        ("TIMETRA-NAT-MIB", "tmnxNatPcp2Group"),
        ("TIMETRA-NAT-MIB", "tmnxNatDeterministicGroup"),
        ("TIMETRA-NAT-MIB", "tmnxNatFragmentIpGroup"),
        ("TIMETRA-NAT-MIB", "tmnxNatFwd2Group"),
        ("TIMETRA-NAT-MIB", "tmnxNatMultiPlcyGroup"),
        ("TIMETRA-NAT-MIB", "tmnxNatQryGroup"),
        ("TIMETRA-NAT-MIB", "tmnxNatIsa2Group"),
        ("TIMETRA-NAT-MIB", "tmnxNatVrtrIPFilterV12v0Group"),
        ("TIMETRA-NAT-MIB", "tmnxNatUpnpGroup"),
        ("TIMETRA-NAT-MIB", "tmnxNatActiveActiveRedGroup"),
        ("TIMETRA-NAT-MIB", "tmnxNatPlV13v0Group"),
        ("TIMETRA-NAT-MIB", "tmnxNatVrtrIPv6FilterV13v0Group"),
        ("TIMETRA-NAT-MIB", "tmnxNatNoLsnSubBlksFreeGroup"),
        ("TIMETRA-NAT-MIB", "tmnxNatPlcyXmppEnhGroup"))
)
if mibBuilder.loadTexts:
    tmnxNatV13v0Compliance.setStatus(
        "obsolete"
    )

tmnxNatNotifyV13v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 65, 1, 13)
)
tmnxNatNotifyV13v0Compliance.setObjects(
    ("TIMETRA-NAT-MIB", "tmnxNatNotifyV13v0Group")
)
if mibBuilder.loadTexts:
    tmnxNatNotifyV13v0Compliance.setStatus(
        "obsolete"
    )

tmnxNatV14v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 65, 1, 14)
)
tmnxNatV14v0Compliance.setObjects(
      *(("TIMETRA-NAT-MIB", "tmnxNatIsaV12v0Group"),
        ("TIMETRA-NAT-MIB", "tmnxNatIsaStatGroup"),
        ("TIMETRA-NAT-MIB", "tmnxNatIsaStatV10v0Group"),
        ("TIMETRA-NAT-MIB", "tmnxNatIsaStatV11v0Group"),
        ("TIMETRA-NAT-MIB", "tmnxNatPlcyGroup"),
        ("TIMETRA-NAT-MIB", "tmnxNatPlcyV9v0Group"),
        ("TIMETRA-NAT-MIB", "tmnxNatPlcyV10v0Group"),
        ("TIMETRA-NAT-MIB", "tmnxNatPlcyV14v0Group"),
        ("TIMETRA-NAT-MIB", "tmnxNatPlcyStatGroup"),
        ("TIMETRA-NAT-MIB", "tmnxNatVrtrGroup"),
        ("TIMETRA-NAT-MIB", "tmnxNatVrtrV9v0Group"),
        ("TIMETRA-NAT-MIB", "tmnxNatVrtrIPFilterGroup"),
        ("TIMETRA-NAT-MIB", "tmnxNatRedGroup"),
        ("TIMETRA-NAT-MIB", "tmnxNatPlV11v0Group"),
        ("TIMETRA-NAT-MIB", "tmnxNatDestGroup"),
        ("TIMETRA-NAT-MIB", "tmnxNatL2AwV14v0Group"),
        ("TIMETRA-NAT-MIB", "tmnxNatLsnV12v0Group"),
        ("TIMETRA-NAT-MIB", "tmnxNatAccV11v0Group"),
        ("TIMETRA-NAT-MIB", "tmnxNatWlanGwGroup"),
        ("TIMETRA-NAT-MIB", "tmnxNatLsnSubIdentV12v0Group"),
        ("TIMETRA-NAT-MIB", "tmnxNatPcpGroup"),
        ("TIMETRA-NAT-MIB", "tmnxNatPcp2Group"),
        ("TIMETRA-NAT-MIB", "tmnxNatDeterministicGroup"),
        ("TIMETRA-NAT-MIB", "tmnxNatFragmentIpGroup"),
        ("TIMETRA-NAT-MIB", "tmnxNatFwd2Group"),
        ("TIMETRA-NAT-MIB", "tmnxNatMultiPlcyGroup"),
        ("TIMETRA-NAT-MIB", "tmnxNatQryGroup"),
        ("TIMETRA-NAT-MIB", "tmnxNatIsa2Group"),
        ("TIMETRA-NAT-MIB", "tmnxNatVrtrIPFilterV12v0Group"),
        ("TIMETRA-NAT-MIB", "tmnxNatUpnpV14v0Group"),
        ("TIMETRA-NAT-MIB", "tmnxNatActiveActiveRedGroup"),
        ("TIMETRA-NAT-MIB", "tmnxNatPlV13v0Group"),
        ("TIMETRA-NAT-MIB", "tmnxNatVrtrIPv6FilterV13v0Group"),
        ("TIMETRA-NAT-MIB", "tmnxNatNoLsnSubBlksFreeGroup"),
        ("TIMETRA-NAT-MIB", "tmnxNatPlcyXmppEnhGroup"),
        ("TIMETRA-NAT-MIB", "tmnxNatWlanGwV14v0Group"),
        ("TIMETRA-NAT-MIB", "tmnxNatFwdCfgGroup"),
        ("TIMETRA-NAT-MIB", "tmnxNatDestinationNatGroup"),
        ("TIMETRA-NAT-MIB", "tmnxNatVrtrIPFilterV14v0Group"),
        ("TIMETRA-NAT-MIB", "tmnxNatMappingGroup"))
)
if mibBuilder.loadTexts:
    tmnxNatV14v0Compliance.setStatus(
        "obsolete"
    )

tmnxNatNotifyV14v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 65, 1, 15)
)
tmnxNatNotifyV14v0Compliance.setObjects(
    ("TIMETRA-NAT-MIB", "tmnxNatNotifyV14v0Group")
)
if mibBuilder.loadTexts:
    tmnxNatNotifyV14v0Compliance.setStatus(
        "obsolete"
    )

tmnxNatV15v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 65, 1, 16)
)
tmnxNatV15v0Compliance.setObjects(
      *(("TIMETRA-NAT-MIB", "tmnxNatIsaV12v0Group"),
        ("TIMETRA-NAT-MIB", "tmnxNatIsaStatGroup"),
        ("TIMETRA-NAT-MIB", "tmnxNatIsaStatV10v0Group"),
        ("TIMETRA-NAT-MIB", "tmnxNatIsaStatV11v0Group"),
        ("TIMETRA-NAT-MIB", "tmnxNatIsaStatV16v0Group"),
        ("TIMETRA-NAT-MIB", "tmnxNatIsaScalingGroup"),
        ("TIMETRA-NAT-MIB", "tmnxNatPlcyGroup"),
        ("TIMETRA-NAT-MIB", "tmnxNatPlcyV9v0Group"),
        ("TIMETRA-NAT-MIB", "tmnxNatPlcyV10v0Group"),
        ("TIMETRA-NAT-MIB", "tmnxNatPlcyV14v0Group"),
        ("TIMETRA-NAT-MIB", "tmnxNatPlcyV15v0Group"),
        ("TIMETRA-NAT-MIB", "tmnxNatPlcyStatGroup"),
        ("TIMETRA-NAT-MIB", "tmnxNatVrtrGroup"),
        ("TIMETRA-NAT-MIB", "tmnxNatVrtrV9v0Group"),
        ("TIMETRA-NAT-MIB", "tmnxNatVrtrIPFilterGroup"),
        ("TIMETRA-NAT-MIB", "tmnxNatRedGroup"),
        ("TIMETRA-NAT-MIB", "tmnxNatPlV11v0Group"),
        ("TIMETRA-NAT-MIB", "tmnxNatDestGroup"),
        ("TIMETRA-NAT-MIB", "tmnxNatL2AwV14v0Group"),
        ("TIMETRA-NAT-MIB", "tmnxNatL2AwV15v0Group"),
        ("TIMETRA-NAT-MIB", "tmnxNatLsnV12v0Group"),
        ("TIMETRA-NAT-MIB", "tmnxNatAccV11v0Group"),
        ("TIMETRA-NAT-MIB", "tmnxNatWlanGwGroup"),
        ("TIMETRA-NAT-MIB", "tmnxNatLsnSubIdentV12v0Group"),
        ("TIMETRA-NAT-MIB", "tmnxNatPcpGroup"),
        ("TIMETRA-NAT-MIB", "tmnxNatPcp2Group"),
        ("TIMETRA-NAT-MIB", "tmnxNatDeterministicGroup"),
        ("TIMETRA-NAT-MIB", "tmnxNatFragmentIpGroup"),
        ("TIMETRA-NAT-MIB", "tmnxNatFwd2Group"),
        ("TIMETRA-NAT-MIB", "tmnxNatMultiPlcyGroup"),
        ("TIMETRA-NAT-MIB", "tmnxNatQryGroup"),
        ("TIMETRA-NAT-MIB", "tmnxNatIsa2Group"),
        ("TIMETRA-NAT-MIB", "tmnxNatVrtrIPFilterV12v0Group"),
        ("TIMETRA-NAT-MIB", "tmnxNatUpnpV14v0Group"),
        ("TIMETRA-NAT-MIB", "tmnxNatActiveActiveRedGroup"),
        ("TIMETRA-NAT-MIB", "tmnxNatPlV13v0Group"),
        ("TIMETRA-NAT-MIB", "tmnxNatVrtrIPv6FilterV13v0Group"),
        ("TIMETRA-NAT-MIB", "tmnxNatNoLsnSubBlksFreeGroup"),
        ("TIMETRA-NAT-MIB", "tmnxNatPlcyXmppEnhGroup"),
        ("TIMETRA-NAT-MIB", "tmnxNatWlanGwV14v0Group"),
        ("TIMETRA-NAT-MIB", "tmnxNatWlanGwV15v0Group"),
        ("TIMETRA-NAT-MIB", "tmnxNatFwdCfgGroup"),
        ("TIMETRA-NAT-MIB", "tmnxNatDestinationNatGroup"),
        ("TIMETRA-NAT-MIB", "tmnxNatVrtrIPFilterV14v0Group"),
        ("TIMETRA-NAT-MIB", "tmnxNatMappingGroup"),
        ("TIMETRA-NAT-MIB", "tmnxNatL2AwExternalAssignGroup"),
        ("TIMETRA-NAT-MIB", "tmnxNatFirewallGroup"),
        ("TIMETRA-NAT-MIB", "tmnxNatFwdV15v0Group"))
)
if mibBuilder.loadTexts:
    tmnxNatV15v0Compliance.setStatus(
        "obsolete"
    )

tmnxNatNotifyV15v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 65, 1, 17)
)
tmnxNatNotifyV15v0Compliance.setObjects(
      *(("TIMETRA-NAT-MIB", "tmnxNatNotifyV14v0Group"),
        ("TIMETRA-NAT-MIB", "tmnxNatNotifyV15v0Group"))
)
if mibBuilder.loadTexts:
    tmnxNatNotifyV15v0Compliance.setStatus(
        "obsolete"
    )

tmnxNatV16v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 65, 1, 18)
)
tmnxNatV16v0Compliance.setObjects(
      *(("TIMETRA-NAT-MIB", "tmnxNatIsaV12v0Group"),
        ("TIMETRA-NAT-MIB", "tmnxNatIsaStatGroup"),
        ("TIMETRA-NAT-MIB", "tmnxNatIsaStatV10v0Group"),
        ("TIMETRA-NAT-MIB", "tmnxNatIsaStatV11v0Group"),
        ("TIMETRA-NAT-MIB", "tmnxNatIsaStatV16v0Group"),
        ("TIMETRA-NAT-MIB", "tmnxNatIsaScalingGroup"),
        ("TIMETRA-NAT-MIB", "tmnxNatPlcyGroup"),
        ("TIMETRA-NAT-MIB", "tmnxNatPlcyV9v0Group"),
        ("TIMETRA-NAT-MIB", "tmnxNatPlcyV10v0Group"),
        ("TIMETRA-NAT-MIB", "tmnxNatPlcyV14v0Group"),
        ("TIMETRA-NAT-MIB", "tmnxNatPlcyV15v0Group"),
        ("TIMETRA-NAT-MIB", "tmnxNatPlcyStatGroup"),
        ("TIMETRA-NAT-MIB", "tmnxNatVrtrGroup"),
        ("TIMETRA-NAT-MIB", "tmnxNatVrtrV9v0Group"),
        ("TIMETRA-NAT-MIB", "tmnxNatVrtrIPFilterGroup"),
        ("TIMETRA-NAT-MIB", "tmnxNatRedGroup"),
        ("TIMETRA-NAT-MIB", "tmnxNatPlV11v0Group"),
        ("TIMETRA-NAT-MIB", "tmnxNatDestGroup"),
        ("TIMETRA-NAT-MIB", "tmnxNatL2AwV14v0Group"),
        ("TIMETRA-NAT-MIB", "tmnxNatL2AwV15v0Group"),
        ("TIMETRA-NAT-MIB", "tmnxNatLsnV12v0Group"),
        ("TIMETRA-NAT-MIB", "tmnxNatAccV11v0Group"),
        ("TIMETRA-NAT-MIB", "tmnxNatWlanGwGroup"),
        ("TIMETRA-NAT-MIB", "tmnxNatLsnSubIdentV12v0Group"),
        ("TIMETRA-NAT-MIB", "tmnxNatPcpGroup"),
        ("TIMETRA-NAT-MIB", "tmnxNatPcp2Group"),
        ("TIMETRA-NAT-MIB", "tmnxNatDeterministicGroup"),
        ("TIMETRA-NAT-MIB", "tmnxNatFragmentIpGroup"),
        ("TIMETRA-NAT-MIB", "tmnxNatFwd2Group"),
        ("TIMETRA-NAT-MIB", "tmnxNatMultiPlcyGroup"),
        ("TIMETRA-NAT-MIB", "tmnxNatQryGroup"),
        ("TIMETRA-NAT-MIB", "tmnxNatIsa2Group"),
        ("TIMETRA-NAT-MIB", "tmnxNatVrtrIPFilterV12v0Group"),
        ("TIMETRA-NAT-MIB", "tmnxNatUpnpV14v0Group"),
        ("TIMETRA-NAT-MIB", "tmnxNatActiveActiveRedGroup"),
        ("TIMETRA-NAT-MIB", "tmnxNatPlV13v0Group"),
        ("TIMETRA-NAT-MIB", "tmnxNatVrtrIPv6FilterV13v0Group"),
        ("TIMETRA-NAT-MIB", "tmnxNatNoLsnSubBlksFreeGroup"),
        ("TIMETRA-NAT-MIB", "tmnxNatPlcyXmppEnhGroup"),
        ("TIMETRA-NAT-MIB", "tmnxNatWlanGwV14v0Group"),
        ("TIMETRA-NAT-MIB", "tmnxNatWlanGwV15v0Group"),
        ("TIMETRA-NAT-MIB", "tmnxNatFwdCfgGroup"),
        ("TIMETRA-NAT-MIB", "tmnxNatDestinationNatGroup"),
        ("TIMETRA-NAT-MIB", "tmnxNatVrtrIPFilterV14v0Group"),
        ("TIMETRA-NAT-MIB", "tmnxNatMappingGroup"),
        ("TIMETRA-NAT-MIB", "tmnxNatL2AwExternalAssignGroup"),
        ("TIMETRA-NAT-MIB", "tmnxNatFirewallGroup"),
        ("TIMETRA-NAT-MIB", "tmnxNatFwdV15v0Group"),
        ("TIMETRA-NAT-MIB", "tmnxNatSyslogGroup"),
        ("TIMETRA-NAT-MIB", "tmnxNatDsliteReassemblyGroup"))
)
if mibBuilder.loadTexts:
    tmnxNatV16v0Compliance.setStatus(
        "obsolete"
    )

tmnxNatV19v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 65, 1, 19)
)
tmnxNatV19v0Compliance.setObjects(
      *(("TIMETRA-NAT-MIB", "tmnxNatIsaV12v0Group"),
        ("TIMETRA-NAT-MIB", "tmnxNatIsaStatGroup"),
        ("TIMETRA-NAT-MIB", "tmnxNatIsaStatV10v0Group"),
        ("TIMETRA-NAT-MIB", "tmnxNatIsaStatV11v0Group"),
        ("TIMETRA-NAT-MIB", "tmnxNatIsaStatV16v0Group"),
        ("TIMETRA-NAT-MIB", "tmnxNatIsaScalingGroup"),
        ("TIMETRA-NAT-MIB", "tmnxNatPlcyGroup"),
        ("TIMETRA-NAT-MIB", "tmnxNatPlcyV9v0Group"),
        ("TIMETRA-NAT-MIB", "tmnxNatPlcyV10v0Group"),
        ("TIMETRA-NAT-MIB", "tmnxNatPlcyV14v0Group"),
        ("TIMETRA-NAT-MIB", "tmnxNatPlcyV15v0Group"),
        ("TIMETRA-NAT-MIB", "tmnxNatPlcyStatGroup"),
        ("TIMETRA-NAT-MIB", "tmnxNatVrtrGroup"),
        ("TIMETRA-NAT-MIB", "tmnxNatVrtrV9v0Group"),
        ("TIMETRA-NAT-MIB", "tmnxNatVrtrIPFilterGroup"),
        ("TIMETRA-NAT-MIB", "tmnxNatRedGroup"),
        ("TIMETRA-NAT-MIB", "tmnxNatPlV11v0Group"),
        ("TIMETRA-NAT-MIB", "tmnxNatDestGroup"),
        ("TIMETRA-NAT-MIB", "tmnxNatL2AwV14v0Group"),
        ("TIMETRA-NAT-MIB", "tmnxNatL2AwV15v0Group"),
        ("TIMETRA-NAT-MIB", "tmnxNatAccV11v0Group"),
        ("TIMETRA-NAT-MIB", "tmnxNatWlanGwGroup"),
        ("TIMETRA-NAT-MIB", "tmnxNatLsnSubIdentV12v0Group"),
        ("TIMETRA-NAT-MIB", "tmnxNatPcpGroup"),
        ("TIMETRA-NAT-MIB", "tmnxNatPcp2Group"),
        ("TIMETRA-NAT-MIB", "tmnxNatDeterministicGroup"),
        ("TIMETRA-NAT-MIB", "tmnxNatFragmentIpGroup"),
        ("TIMETRA-NAT-MIB", "tmnxNatFwd2Group"),
        ("TIMETRA-NAT-MIB", "tmnxNatMultiPlcyGroup"),
        ("TIMETRA-NAT-MIB", "tmnxNatQryGroup"),
        ("TIMETRA-NAT-MIB", "tmnxNatIsa2Group"),
        ("TIMETRA-NAT-MIB", "tmnxNatVrtrIPFilterV12v0Group"),
        ("TIMETRA-NAT-MIB", "tmnxNatUpnpV14v0Group"),
        ("TIMETRA-NAT-MIB", "tmnxNatActiveActiveRedGroup"),
        ("TIMETRA-NAT-MIB", "tmnxNatPlV13v0Group"),
        ("TIMETRA-NAT-MIB", "tmnxNatVrtrIPv6FilterV13v0Group"),
        ("TIMETRA-NAT-MIB", "tmnxNatNoLsnSubBlksFreeGroup"),
        ("TIMETRA-NAT-MIB", "tmnxNatPlcyXmppEnhGroup"),
        ("TIMETRA-NAT-MIB", "tmnxNatWlanGwV14v0Group"),
        ("TIMETRA-NAT-MIB", "tmnxNatWlanGwV15v0Group"),
        ("TIMETRA-NAT-MIB", "tmnxNatFwdCfgGroup"),
        ("TIMETRA-NAT-MIB", "tmnxNatDestinationNatGroup"),
        ("TIMETRA-NAT-MIB", "tmnxNatVrtrIPFilterV14v0Group"),
        ("TIMETRA-NAT-MIB", "tmnxNatMappingGroup"),
        ("TIMETRA-NAT-MIB", "tmnxNatL2AwExternalAssignGroup"),
        ("TIMETRA-NAT-MIB", "tmnxNatFirewallGroup"),
        ("TIMETRA-NAT-MIB", "tmnxNatFwdV15v0Group"),
        ("TIMETRA-NAT-MIB", "tmnxNatSyslogGroup"),
        ("TIMETRA-NAT-MIB", "tmnxNatDsliteReassemblyGroup"),
        ("TIMETRA-NAT-MIB", "tmnxNatSicrGroup"),
        ("TIMETRA-NAT-MIB", "tmnxNatDestinationNatV19v0Group"),
        ("TIMETRA-NAT-MIB", "tmnxNatLsnV19v0Group"),
        ("TIMETRA-NAT-MIB", "tmnxNatEsaV19v0Group"),
        ("TIMETRA-NAT-MIB", "tmnxNatNotifyV19v0Group"))
)
if mibBuilder.loadTexts:
    tmnxNatV19v0Compliance.setStatus(
        "obsolete"
    )

tmnxNatV20v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 65, 1, 20)
)
tmnxNatV20v0Compliance.setObjects(
      *(("TIMETRA-NAT-MIB", "tmnxNatIsaV12v0Group"),
        ("TIMETRA-NAT-MIB", "tmnxNatIsaStatGroup"),
        ("TIMETRA-NAT-MIB", "tmnxNatIsaStatV10v0Group"),
        ("TIMETRA-NAT-MIB", "tmnxNatIsaStatV11v0Group"),
        ("TIMETRA-NAT-MIB", "tmnxNatIsaStatV16v0Group"),
        ("TIMETRA-NAT-MIB", "tmnxNatIsaScalingGroup"),
        ("TIMETRA-NAT-MIB", "tmnxNatPlcyGroup"),
        ("TIMETRA-NAT-MIB", "tmnxNatPlcyV9v0Group"),
        ("TIMETRA-NAT-MIB", "tmnxNatPlcyV10v0Group"),
        ("TIMETRA-NAT-MIB", "tmnxNatPlcyV14v0Group"),
        ("TIMETRA-NAT-MIB", "tmnxNatPlcyV15v0Group"),
        ("TIMETRA-NAT-MIB", "tmnxNatPlcyStatGroup"),
        ("TIMETRA-NAT-MIB", "tmnxNatVrtrGroup"),
        ("TIMETRA-NAT-MIB", "tmnxNatVrtrV9v0Group"),
        ("TIMETRA-NAT-MIB", "tmnxNatVrtrIPFilterGroup"),
        ("TIMETRA-NAT-MIB", "tmnxNatRedGroup"),
        ("TIMETRA-NAT-MIB", "tmnxNatPlV11v0Group"),
        ("TIMETRA-NAT-MIB", "tmnxNatDestGroup"),
        ("TIMETRA-NAT-MIB", "tmnxNatL2AwV14v0Group"),
        ("TIMETRA-NAT-MIB", "tmnxNatL2AwV15v0Group"),
        ("TIMETRA-NAT-MIB", "tmnxNatAccV11v0Group"),
        ("TIMETRA-NAT-MIB", "tmnxNatWlanGwGroup"),
        ("TIMETRA-NAT-MIB", "tmnxNatLsnSubIdentV12v0Group"),
        ("TIMETRA-NAT-MIB", "tmnxNatPcpGroup"),
        ("TIMETRA-NAT-MIB", "tmnxNatPcp2Group"),
        ("TIMETRA-NAT-MIB", "tmnxNatDeterministicGroup"),
        ("TIMETRA-NAT-MIB", "tmnxNatFragmentIpGroup"),
        ("TIMETRA-NAT-MIB", "tmnxNatFwd2Group"),
        ("TIMETRA-NAT-MIB", "tmnxNatMultiPlcyGroup"),
        ("TIMETRA-NAT-MIB", "tmnxNatQryGroup"),
        ("TIMETRA-NAT-MIB", "tmnxNatIsa2Group"),
        ("TIMETRA-NAT-MIB", "tmnxNatVrtrIPFilterV12v0Group"),
        ("TIMETRA-NAT-MIB", "tmnxNatUpnpV14v0Group"),
        ("TIMETRA-NAT-MIB", "tmnxNatActiveActiveRedGroup"),
        ("TIMETRA-NAT-MIB", "tmnxNatPlV13v0Group"),
        ("TIMETRA-NAT-MIB", "tmnxNatVrtrIPv6FilterV13v0Group"),
        ("TIMETRA-NAT-MIB", "tmnxNatNoLsnSubBlksFreeGroup"),
        ("TIMETRA-NAT-MIB", "tmnxNatPlcyXmppEnhGroup"),
        ("TIMETRA-NAT-MIB", "tmnxNatWlanGwV14v0Group"),
        ("TIMETRA-NAT-MIB", "tmnxNatWlanGwV15v0Group"),
        ("TIMETRA-NAT-MIB", "tmnxNatFwdCfgGroup"),
        ("TIMETRA-NAT-MIB", "tmnxNatDestinationNatGroup"),
        ("TIMETRA-NAT-MIB", "tmnxNatVrtrIPFilterV14v0Group"),
        ("TIMETRA-NAT-MIB", "tmnxNatMappingGroup"),
        ("TIMETRA-NAT-MIB", "tmnxNatL2AwExternalAssignGroup"),
        ("TIMETRA-NAT-MIB", "tmnxNatFirewallGroup"),
        ("TIMETRA-NAT-MIB", "tmnxNatFwdV15v0Group"),
        ("TIMETRA-NAT-MIB", "tmnxNatSyslogGroup"),
        ("TIMETRA-NAT-MIB", "tmnxNatDsliteReassemblyGroup"),
        ("TIMETRA-NAT-MIB", "tmnxNatSicrGroup"),
        ("TIMETRA-NAT-MIB", "tmnxNatDestinationNatV19v0Group"),
        ("TIMETRA-NAT-MIB", "tmnxNatLsnV19v0Group"),
        ("TIMETRA-NAT-MIB", "tmnxNatEsaV19v0Group"),
        ("TIMETRA-NAT-MIB", "tmnxNatFwdL2AwGroup"),
        ("TIMETRA-NAT-MIB", "tmnxNatNotifyV19v0Group"),
        ("TIMETRA-NAT-MIB", "tmnxNatPcpExt1Group"),
        ("TIMETRA-NAT-MIB", "tmnxNatCupsGroup"))
)
if mibBuilder.loadTexts:
    tmnxNatV20v0Compliance.setStatus(
        "obsolete"
    )

tmnxNatV21v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 65, 1, 21)
)
tmnxNatV21v0Compliance.setObjects(
      *(("TIMETRA-NAT-MIB", "tmnxNatIsaV12v0Group"),
        ("TIMETRA-NAT-MIB", "tmnxNatIsaStatGroup"),
        ("TIMETRA-NAT-MIB", "tmnxNatIsaStatV10v0Group"),
        ("TIMETRA-NAT-MIB", "tmnxNatIsaStatV11v0Group"),
        ("TIMETRA-NAT-MIB", "tmnxNatIsaStatV16v0Group"),
        ("TIMETRA-NAT-MIB", "tmnxNatIsaScalingGroup"),
        ("TIMETRA-NAT-MIB", "tmnxNatPlcyGroup"),
        ("TIMETRA-NAT-MIB", "tmnxNatPlcyV9v0Group"),
        ("TIMETRA-NAT-MIB", "tmnxNatPlcyV10v0Group"),
        ("TIMETRA-NAT-MIB", "tmnxNatPlcyV14v0Group"),
        ("TIMETRA-NAT-MIB", "tmnxNatPlcyV15v0Group"),
        ("TIMETRA-NAT-MIB", "tmnxNatPlcyStatGroup"),
        ("TIMETRA-NAT-MIB", "tmnxNatVrtrGroup"),
        ("TIMETRA-NAT-MIB", "tmnxNatVrtrV9v0Group"),
        ("TIMETRA-NAT-MIB", "tmnxNatVrtrIPFilterGroup"),
        ("TIMETRA-NAT-MIB", "tmnxNatRedGroup"),
        ("TIMETRA-NAT-MIB", "tmnxNatPlV11v0Group"),
        ("TIMETRA-NAT-MIB", "tmnxNatDestGroup"),
        ("TIMETRA-NAT-MIB", "tmnxNatL2AwV14v0Group"),
        ("TIMETRA-NAT-MIB", "tmnxNatL2AwV15v0Group"),
        ("TIMETRA-NAT-MIB", "tmnxNatAccV11v0Group"),
        ("TIMETRA-NAT-MIB", "tmnxNatWlanGwGroup"),
        ("TIMETRA-NAT-MIB", "tmnxNatLsnSubIdentV12v0Group"),
        ("TIMETRA-NAT-MIB", "tmnxNatPcpGroup"),
        ("TIMETRA-NAT-MIB", "tmnxNatPcp2Group"),
        ("TIMETRA-NAT-MIB", "tmnxNatDeterministicGroup"),
        ("TIMETRA-NAT-MIB", "tmnxNatFragmentIpGroup"),
        ("TIMETRA-NAT-MIB", "tmnxNatFwd2Group"),
        ("TIMETRA-NAT-MIB", "tmnxNatMultiPlcyGroup"),
        ("TIMETRA-NAT-MIB", "tmnxNatQryGroup"),
        ("TIMETRA-NAT-MIB", "tmnxNatIsa2Group"),
        ("TIMETRA-NAT-MIB", "tmnxNatVrtrIPFilterV12v0Group"),
        ("TIMETRA-NAT-MIB", "tmnxNatUpnpV14v0Group"),
        ("TIMETRA-NAT-MIB", "tmnxNatActiveActiveRedGroup"),
        ("TIMETRA-NAT-MIB", "tmnxNatPlV13v0Group"),
        ("TIMETRA-NAT-MIB", "tmnxNatVrtrIPv6FilterV13v0Group"),
        ("TIMETRA-NAT-MIB", "tmnxNatNoLsnSubBlksFreeGroup"),
        ("TIMETRA-NAT-MIB", "tmnxNatPlcyXmppEnhGroup"),
        ("TIMETRA-NAT-MIB", "tmnxNatWlanGwV14v0Group"),
        ("TIMETRA-NAT-MIB", "tmnxNatWlanGwV15v0Group"),
        ("TIMETRA-NAT-MIB", "tmnxNatFwdCfgGroup"),
        ("TIMETRA-NAT-MIB", "tmnxNatDestinationNatGroup"),
        ("TIMETRA-NAT-MIB", "tmnxNatVrtrIPFilterV14v0Group"),
        ("TIMETRA-NAT-MIB", "tmnxNatMappingGroup"),
        ("TIMETRA-NAT-MIB", "tmnxNatL2AwExternalAssignGroup"),
        ("TIMETRA-NAT-MIB", "tmnxNatFirewallGroup"),
        ("TIMETRA-NAT-MIB", "tmnxNatFwdV15v0Group"),
        ("TIMETRA-NAT-MIB", "tmnxNatSyslogGroup"),
        ("TIMETRA-NAT-MIB", "tmnxNatDsliteReassemblyGroup"),
        ("TIMETRA-NAT-MIB", "tmnxNatSicrGroup"),
        ("TIMETRA-NAT-MIB", "tmnxNatDestinationNatV19v0Group"),
        ("TIMETRA-NAT-MIB", "tmnxNatLsnV19v0Group"),
        ("TIMETRA-NAT-MIB", "tmnxNatEsaV19v0Group"),
        ("TIMETRA-NAT-MIB", "tmnxNatFwdL2AwGroup"),
        ("TIMETRA-NAT-MIB", "tmnxNatNotifyV19v0Group"),
        ("TIMETRA-NAT-MIB", "tmnxNatPcpExt1Group"),
        ("TIMETRA-NAT-MIB", "tmnxNatCupsGroup"),
        ("TIMETRA-NAT-MIB", "tmnxNatDeterministic2Group"),
        ("TIMETRA-NAT-MIB", "tmnxNatNotifyV21v0Group"),
        ("TIMETRA-NAT-MIB", "tmnxNatL2AwDynamicBlkAllocGroup"),
        ("TIMETRA-NAT-MIB", "tmnxNatInsideRoutesGroup"),
        ("TIMETRA-NAT-MIB", "tmnxNatPlV21v0Group"),
        ("TIMETRA-NAT-MIB", "tmnxNatDsliteV21v0Group"),
        ("TIMETRA-NAT-MIB", "tmnxNatCupsV21v0Group"))
)
if mibBuilder.loadTexts:
    tmnxNatV21v0Compliance.setStatus(
        "obsolete"
    )

tmnxNatV22v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 65, 1, 22)
)
tmnxNatV22v0Compliance.setObjects(
      *(("TIMETRA-NAT-MIB", "tmnxNatPlV22v0Group"),
        ("TIMETRA-NAT-MIB", "tmnxNatPlWmarkV22v0Group"),
        ("TIMETRA-NAT-MIB", "tmnxNatPlWmarkNotifyV22v0Group"),
        ("TIMETRA-NAT-MIB", "tmnxNatCupsV22v0Group"),
        ("TIMETRA-NAT-MIB", "tmnxNatIsaV22v0Group"),
        ("TIMETRA-NAT-MIB", "tmnxNatPlL2AwV22v0Group"),
        ("TIMETRA-NAT-MIB", "tmnxNatSicrV22v0Group"),
        ("TIMETRA-NAT-MIB", "tmnxNatUpPlcyV22v0Group"))
)
if mibBuilder.loadTexts:
    tmnxNatV22v0Compliance.setStatus(
        "obsolete"
    )

tmnxNatV23v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 65, 1, 23)
)
tmnxNatV23v0Compliance.setObjects(
      *(("TIMETRA-NAT-MIB", "tmnxNatIsaV12v0Group"),
        ("TIMETRA-NAT-MIB", "tmnxNatIsaStatGroup"),
        ("TIMETRA-NAT-MIB", "tmnxNatIsaStatV10v0Group"),
        ("TIMETRA-NAT-MIB", "tmnxNatIsaStatV11v0Group"),
        ("TIMETRA-NAT-MIB", "tmnxNatIsaStatV16v0Group"),
        ("TIMETRA-NAT-MIB", "tmnxNatIsaScalingGroup"),
        ("TIMETRA-NAT-MIB", "tmnxNatPlcyGroup"),
        ("TIMETRA-NAT-MIB", "tmnxNatPlcyV9v0Group"),
        ("TIMETRA-NAT-MIB", "tmnxNatPlcyV10v0Group"),
        ("TIMETRA-NAT-MIB", "tmnxNatPlcyV14v0Group"),
        ("TIMETRA-NAT-MIB", "tmnxNatPlcyV15v0Group"),
        ("TIMETRA-NAT-MIB", "tmnxNatPlcyV23v0Group"),
        ("TIMETRA-NAT-MIB", "tmnxNatPlcyStatGroup"),
        ("TIMETRA-NAT-MIB", "tmnxNatVrtrGroup"),
        ("TIMETRA-NAT-MIB", "tmnxNatVrtrV9v0Group"),
        ("TIMETRA-NAT-MIB", "tmnxNatVrtrIPFilterGroup"),
        ("TIMETRA-NAT-MIB", "tmnxNatRedGroup"),
        ("TIMETRA-NAT-MIB", "tmnxNatPlV11v0Group"),
        ("TIMETRA-NAT-MIB", "tmnxNatDestGroup"),
        ("TIMETRA-NAT-MIB", "tmnxNatL2AwV14v0Group"),
        ("TIMETRA-NAT-MIB", "tmnxNatL2AwV15v0Group"),
        ("TIMETRA-NAT-MIB", "tmnxNatAccV11v0Group"),
        ("TIMETRA-NAT-MIB", "tmnxNatWlanGwGroup"),
        ("TIMETRA-NAT-MIB", "tmnxNatLsnSubIdentV12v0Group"),
        ("TIMETRA-NAT-MIB", "tmnxNatPcpGroup"),
        ("TIMETRA-NAT-MIB", "tmnxNatPcp2Group"),
        ("TIMETRA-NAT-MIB", "tmnxNatDetV23v0Group"),
        ("TIMETRA-NAT-MIB", "tmnxNatFragmentIpGroup"),
        ("TIMETRA-NAT-MIB", "tmnxNatFwd2Group"),
        ("TIMETRA-NAT-MIB", "tmnxNatMultiPlcyGroup"),
        ("TIMETRA-NAT-MIB", "tmnxNatQryGroup"),
        ("TIMETRA-NAT-MIB", "tmnxNatIsa2V23v0Group"),
        ("TIMETRA-NAT-MIB", "tmnxNatVrtrIPFilterV12v0Group"),
        ("TIMETRA-NAT-MIB", "tmnxNatUpnpV14v0Group"),
        ("TIMETRA-NAT-MIB", "tmnxNatActiveActiveRedGroup"),
        ("TIMETRA-NAT-MIB", "tmnxNatPlV13v0Group"),
        ("TIMETRA-NAT-MIB", "tmnxNatVrtrIPv6FilterV13v0Group"),
        ("TIMETRA-NAT-MIB", "tmnxNatNoLsnSubBlksFreeGroup"),
        ("TIMETRA-NAT-MIB", "tmnxNatPlcyXmppEnhGroup"),
        ("TIMETRA-NAT-MIB", "tmnxNatWlanGwV14v0Group"),
        ("TIMETRA-NAT-MIB", "tmnxNatWlanGwV15v0Group"),
        ("TIMETRA-NAT-MIB", "tmnxNatFwdCfgGroup"),
        ("TIMETRA-NAT-MIB", "tmnxNatDestinationNatGroup"),
        ("TIMETRA-NAT-MIB", "tmnxNatVrtrIPFilterV14v0Group"),
        ("TIMETRA-NAT-MIB", "tmnxNatMappingGroup"),
        ("TIMETRA-NAT-MIB", "tmnxNatL2AwExternalAssignGroup"),
        ("TIMETRA-NAT-MIB", "tmnxNatFirewallGroup"),
        ("TIMETRA-NAT-MIB", "tmnxNatFwdV15v0Group"),
        ("TIMETRA-NAT-MIB", "tmnxNatSyslogGroup"),
        ("TIMETRA-NAT-MIB", "tmnxNatDsliteReassemblyGroup"),
        ("TIMETRA-NAT-MIB", "tmnxNatSicrGroup"),
        ("TIMETRA-NAT-MIB", "tmnxNatDestinationNatV19v0Group"),
        ("TIMETRA-NAT-MIB", "tmnxNatLsnV19v0Group"),
        ("TIMETRA-NAT-MIB", "tmnxNatEsaV19v0Group"),
        ("TIMETRA-NAT-MIB", "tmnxNatFwdL2AwGroup"),
        ("TIMETRA-NAT-MIB", "tmnxNatNotifyV19v0Group"),
        ("TIMETRA-NAT-MIB", "tmnxNatPcpExt1Group"),
        ("TIMETRA-NAT-MIB", "tmnxNatCupsGroup"),
        ("TIMETRA-NAT-MIB", "tmnxNatDeterministic2Group"),
        ("TIMETRA-NAT-MIB", "tmnxNatNotifyV21v0Group"),
        ("TIMETRA-NAT-MIB", "tmnxNatL2AwDynamicBlkAllocGroup"),
        ("TIMETRA-NAT-MIB", "tmnxNatInsideRoutesGroup"),
        ("TIMETRA-NAT-MIB", "tmnxNatPlV21v0Group"),
        ("TIMETRA-NAT-MIB", "tmnxNatDsliteV21v0Group"),
        ("TIMETRA-NAT-MIB", "tmnxNatCupsV21v0Group"),
        ("TIMETRA-NAT-MIB", "tmnxNatPlV22v0Group"),
        ("TIMETRA-NAT-MIB", "tmnxNatPlWmarkV22v0Group"),
        ("TIMETRA-NAT-MIB", "tmnxNatPlWmarkNotifyV22v0Group"),
        ("TIMETRA-NAT-MIB", "tmnxNatCupsV22v0Group"),
        ("TIMETRA-NAT-MIB", "tmnxNatIsaV22v0Group"),
        ("TIMETRA-NAT-MIB", "tmnxNatPlL2AwV22v0Group"),
        ("TIMETRA-NAT-MIB", "tmnxNatSicrV22v0Group"),
        ("TIMETRA-NAT-MIB", "tmnxNatUpPlcyV22v0Group"),
        ("TIMETRA-NAT-MIB", "tmnxNatSourcePrefixV23v0Group"),
        ("TIMETRA-NAT-MIB", "tmnxNatVrtrSpfPlcyV23v0Group"),
        ("TIMETRA-NAT-MIB", "tmnxNatPlV23v0Group"),
        ("TIMETRA-NAT-MIB", "tmnxNatVrtrV23v0Group"),
        ("TIMETRA-NAT-MIB", "tmnxNatLsnV23v0Group"),
        ("TIMETRA-NAT-MIB", "tmnxNatFwdActionV23v0Group"),
        ("TIMETRA-NAT-MIB", "tmnxNatPlLsnV23v0Group"))
)
if mibBuilder.loadTexts:
    tmnxNatV23v0Compliance.setStatus(
        "obsolete"
    )

tmnxNatNotifyV23v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 65, 1, 24)
)
tmnxNatNotifyV23v0Compliance.setObjects(
      *(("TIMETRA-NAT-MIB", "tmnxNatNotifyV15v0Group"),
        ("TIMETRA-NAT-MIB", "tmnxNatNotifyV23v0Group"))
)
if mibBuilder.loadTexts:
    tmnxNatNotifyV23v0Compliance.setStatus(
        "current"
    )

tmnxNatV24v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 65, 1, 25)
)
tmnxNatV24v0Compliance.setObjects(
      *(("TIMETRA-NAT-MIB", "tmnxNatIsaV12v0Group"),
        ("TIMETRA-NAT-MIB", "tmnxNatIsaStatGroup"),
        ("TIMETRA-NAT-MIB", "tmnxNatIsaStatV10v0Group"),
        ("TIMETRA-NAT-MIB", "tmnxNatIsaStatV11v0Group"),
        ("TIMETRA-NAT-MIB", "tmnxNatIsaStatV16v0Group"),
        ("TIMETRA-NAT-MIB", "tmnxNatIsaScalingGroup"),
        ("TIMETRA-NAT-MIB", "tmnxNatPlcyGroup"),
        ("TIMETRA-NAT-MIB", "tmnxNatPlcyV9v0Group"),
        ("TIMETRA-NAT-MIB", "tmnxNatPlcyV10v0Group"),
        ("TIMETRA-NAT-MIB", "tmnxNatPlcyV14v0Group"),
        ("TIMETRA-NAT-MIB", "tmnxNatPlcyV15v0Group"),
        ("TIMETRA-NAT-MIB", "tmnxNatPlcyV23v0Group"),
        ("TIMETRA-NAT-MIB", "tmnxNatPlcyStatGroup"),
        ("TIMETRA-NAT-MIB", "tmnxNatVrtrGroup"),
        ("TIMETRA-NAT-MIB", "tmnxNatVrtrV9v0Group"),
        ("TIMETRA-NAT-MIB", "tmnxNatVrtrIPFilterGroup"),
        ("TIMETRA-NAT-MIB", "tmnxNatRedGroup"),
        ("TIMETRA-NAT-MIB", "tmnxNatPlV11v0Group"),
        ("TIMETRA-NAT-MIB", "tmnxNatDestGroup"),
        ("TIMETRA-NAT-MIB", "tmnxNatL2AwV14v0Group"),
        ("TIMETRA-NAT-MIB", "tmnxNatL2AwV15v0Group"),
        ("TIMETRA-NAT-MIB", "tmnxNatAccV11v0Group"),
        ("TIMETRA-NAT-MIB", "tmnxNatWlanGwGroup"),
        ("TIMETRA-NAT-MIB", "tmnxNatLsnSubIdentV12v0Group"),
        ("TIMETRA-NAT-MIB", "tmnxNatPcpGroup"),
        ("TIMETRA-NAT-MIB", "tmnxNatPcp2Group"),
        ("TIMETRA-NAT-MIB", "tmnxNatDetV23v0Group"),
        ("TIMETRA-NAT-MIB", "tmnxNatDetV24v0Group"),
        ("TIMETRA-NAT-MIB", "tmnxNatFragmentIpGroup"),
        ("TIMETRA-NAT-MIB", "tmnxNatFwd2Group"),
        ("TIMETRA-NAT-MIB", "tmnxNatMultiPlcyGroup"),
        ("TIMETRA-NAT-MIB", "tmnxNatQryGroup"),
        ("TIMETRA-NAT-MIB", "tmnxNatIsa2V23v0Group"),
        ("TIMETRA-NAT-MIB", "tmnxNatVrtrIPFilterV12v0Group"),
        ("TIMETRA-NAT-MIB", "tmnxNatUpnpV14v0Group"),
        ("TIMETRA-NAT-MIB", "tmnxNatActiveActiveRedGroup"),
        ("TIMETRA-NAT-MIB", "tmnxNatPlV13v0Group"),
        ("TIMETRA-NAT-MIB", "tmnxNatVrtrIPv6FilterV13v0Group"),
        ("TIMETRA-NAT-MIB", "tmnxNatNoLsnSubBlksFreeGroup"),
        ("TIMETRA-NAT-MIB", "tmnxNatPlcyXmppEnhGroup"),
        ("TIMETRA-NAT-MIB", "tmnxNatWlanGwV14v0Group"),
        ("TIMETRA-NAT-MIB", "tmnxNatWlanGwV15v0Group"),
        ("TIMETRA-NAT-MIB", "tmnxNatFwdCfgGroup"),
        ("TIMETRA-NAT-MIB", "tmnxNatDestinationNatGroup"),
        ("TIMETRA-NAT-MIB", "tmnxNatVrtrIPFilterV14v0Group"),
        ("TIMETRA-NAT-MIB", "tmnxNatMappingGroup"),
        ("TIMETRA-NAT-MIB", "tmnxNatL2AwExternalAssignGroup"),
        ("TIMETRA-NAT-MIB", "tmnxNatFirewallGroup"),
        ("TIMETRA-NAT-MIB", "tmnxNatFwdV15v0Group"),
        ("TIMETRA-NAT-MIB", "tmnxNatSyslogGroup"),
        ("TIMETRA-NAT-MIB", "tmnxNatDsliteReassemblyGroup"),
        ("TIMETRA-NAT-MIB", "tmnxNatSicrGroup"),
        ("TIMETRA-NAT-MIB", "tmnxNatDestinationNatV19v0Group"),
        ("TIMETRA-NAT-MIB", "tmnxNatLsnV19v0Group"),
        ("TIMETRA-NAT-MIB", "tmnxNatEsaV19v0Group"),
        ("TIMETRA-NAT-MIB", "tmnxNatFwdL2AwGroup"),
        ("TIMETRA-NAT-MIB", "tmnxNatNotifyV19v0Group"),
        ("TIMETRA-NAT-MIB", "tmnxNatPcpExt1Group"),
        ("TIMETRA-NAT-MIB", "tmnxNatCupsGroup"),
        ("TIMETRA-NAT-MIB", "tmnxNatDeterministic2Group"),
        ("TIMETRA-NAT-MIB", "tmnxNatNotifyV21v0Group"),
        ("TIMETRA-NAT-MIB", "tmnxNatL2AwDynamicBlkAllocGroup"),
        ("TIMETRA-NAT-MIB", "tmnxNatInsideRoutesGroup"),
        ("TIMETRA-NAT-MIB", "tmnxNatPlV21v0Group"),
        ("TIMETRA-NAT-MIB", "tmnxNatDsliteV21v0Group"),
        ("TIMETRA-NAT-MIB", "tmnxNatCupsV21v0Group"),
        ("TIMETRA-NAT-MIB", "tmnxNatPlV22v0Group"),
        ("TIMETRA-NAT-MIB", "tmnxNatPlWmarkV22v0Group"),
        ("TIMETRA-NAT-MIB", "tmnxNatPlWmarkNotifyV22v0Group"),
        ("TIMETRA-NAT-MIB", "tmnxNatCupsV22v0Group"),
        ("TIMETRA-NAT-MIB", "tmnxNatIsaV22v0Group"),
        ("TIMETRA-NAT-MIB", "tmnxNatPlL2AwV22v0Group"),
        ("TIMETRA-NAT-MIB", "tmnxNatSicrV22v0Group"),
        ("TIMETRA-NAT-MIB", "tmnxNatUpPlcyV22v0Group"),
        ("TIMETRA-NAT-MIB", "tmnxNatSourcePrefixV23v0Group"),
        ("TIMETRA-NAT-MIB", "tmnxNatVrtrSpfPlcyV23v0Group"),
        ("TIMETRA-NAT-MIB", "tmnxNatPlV23v0Group"),
        ("TIMETRA-NAT-MIB", "tmnxNatVrtrV23v0Group"),
        ("TIMETRA-NAT-MIB", "tmnxNatLsnV23v0Group"),
        ("TIMETRA-NAT-MIB", "tmnxNatFwdActionV23v0Group"),
        ("TIMETRA-NAT-MIB", "tmnxNatPlLsnV23v0Group"),
        ("TIMETRA-NAT-MIB", "tmnxNatPlLsnV24v0Group"),
        ("TIMETRA-NAT-MIB", "tmnxNatEsaV24v0Group"),
        ("TIMETRA-NAT-MIB", "tmnxNatIsaV24v0Group"),
        ("TIMETRA-NAT-MIB", "tmnxNatMappingV24v0Group"),
        ("TIMETRA-NAT-MIB", "tmnxNatNotifyV24v0Group"))
)
if mibBuilder.loadTexts:
    tmnxNatV24v0Compliance.setStatus(
        "current"
    )

tmnxNatV25v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 65, 1, 26)
)
tmnxNatV25v0Compliance.setObjects(
      *(("TIMETRA-NAT-MIB", "tmnxNatIsaV12v0Group"),
        ("TIMETRA-NAT-MIB", "tmnxNatIsaStatGroup"),
        ("TIMETRA-NAT-MIB", "tmnxNatIsaStatV10v0Group"),
        ("TIMETRA-NAT-MIB", "tmnxNatIsaStatV11v0Group"),
        ("TIMETRA-NAT-MIB", "tmnxNatIsaStatV16v0Group"),
        ("TIMETRA-NAT-MIB", "tmnxNatIsaScalingGroup"),
        ("TIMETRA-NAT-MIB", "tmnxNatPlcyGroup"),
        ("TIMETRA-NAT-MIB", "tmnxNatPlcyV9v0Group"),
        ("TIMETRA-NAT-MIB", "tmnxNatPlcyV10v0Group"),
        ("TIMETRA-NAT-MIB", "tmnxNatPlcyV14v0Group"),
        ("TIMETRA-NAT-MIB", "tmnxNatPlcyV15v0Group"),
        ("TIMETRA-NAT-MIB", "tmnxNatPlcyV23v0Group"),
        ("TIMETRA-NAT-MIB", "tmnxNatPlcyStatGroup"),
        ("TIMETRA-NAT-MIB", "tmnxNatVrtrGroup"),
        ("TIMETRA-NAT-MIB", "tmnxNatVrtrV9v0Group"),
        ("TIMETRA-NAT-MIB", "tmnxNatVrtrIPFilterGroup"),
        ("TIMETRA-NAT-MIB", "tmnxNatRedGroup"),
        ("TIMETRA-NAT-MIB", "tmnxNatPlV11v0Group"),
        ("TIMETRA-NAT-MIB", "tmnxNatDestGroup"),
        ("TIMETRA-NAT-MIB", "tmnxNatL2AwV14v0Group"),
        ("TIMETRA-NAT-MIB", "tmnxNatL2AwV15v0Group"),
        ("TIMETRA-NAT-MIB", "tmnxNatAccV11v0Group"),
        ("TIMETRA-NAT-MIB", "tmnxNatWlanGwGroup"),
        ("TIMETRA-NAT-MIB", "tmnxNatLsnSubIdentV12v0Group"),
        ("TIMETRA-NAT-MIB", "tmnxNatPcpGroup"),
        ("TIMETRA-NAT-MIB", "tmnxNatPcp2Group"),
        ("TIMETRA-NAT-MIB", "tmnxNatDetV23v0Group"),
        ("TIMETRA-NAT-MIB", "tmnxNatDetV24v0Group"),
        ("TIMETRA-NAT-MIB", "tmnxNatFragmentIpGroup"),
        ("TIMETRA-NAT-MIB", "tmnxNatFwd2Group"),
        ("TIMETRA-NAT-MIB", "tmnxNatMultiPlcyGroup"),
        ("TIMETRA-NAT-MIB", "tmnxNatQryGroup"),
        ("TIMETRA-NAT-MIB", "tmnxNatIsa2V23v0Group"),
        ("TIMETRA-NAT-MIB", "tmnxNatVrtrIPFilterV12v0Group"),
        ("TIMETRA-NAT-MIB", "tmnxNatUpnpV14v0Group"),
        ("TIMETRA-NAT-MIB", "tmnxNatActiveActiveRedGroup"),
        ("TIMETRA-NAT-MIB", "tmnxNatPlV13v0Group"),
        ("TIMETRA-NAT-MIB", "tmnxNatVrtrIPv6FilterV13v0Group"),
        ("TIMETRA-NAT-MIB", "tmnxNatNoLsnSubBlksFreeGroup"),
        ("TIMETRA-NAT-MIB", "tmnxNatPlcyXmppEnhGroup"),
        ("TIMETRA-NAT-MIB", "tmnxNatWlanGwV14v0Group"),
        ("TIMETRA-NAT-MIB", "tmnxNatWlanGwV15v0Group"),
        ("TIMETRA-NAT-MIB", "tmnxNatFwdCfgGroup"),
        ("TIMETRA-NAT-MIB", "tmnxNatDestinationNatGroup"),
        ("TIMETRA-NAT-MIB", "tmnxNatVrtrIPFilterV14v0Group"),
        ("TIMETRA-NAT-MIB", "tmnxNatMappingGroup"),
        ("TIMETRA-NAT-MIB", "tmnxNatL2AwExternalAssignGroup"),
        ("TIMETRA-NAT-MIB", "tmnxNatFirewallGroup"),
        ("TIMETRA-NAT-MIB", "tmnxNatFwdV15v0Group"),
        ("TIMETRA-NAT-MIB", "tmnxNatSyslogGroup"),
        ("TIMETRA-NAT-MIB", "tmnxNatDsliteReassemblyGroup"),
        ("TIMETRA-NAT-MIB", "tmnxNatSicrGroup"),
        ("TIMETRA-NAT-MIB", "tmnxNatDestinationNatV19v0Group"),
        ("TIMETRA-NAT-MIB", "tmnxNatLsnV19v0Group"),
        ("TIMETRA-NAT-MIB", "tmnxNatEsaV19v0Group"),
        ("TIMETRA-NAT-MIB", "tmnxNatFwdL2AwGroup"),
        ("TIMETRA-NAT-MIB", "tmnxNatNotifyV19v0Group"),
        ("TIMETRA-NAT-MIB", "tmnxNatPcpExt1Group"),
        ("TIMETRA-NAT-MIB", "tmnxNatCupsGroup"),
        ("TIMETRA-NAT-MIB", "tmnxNatDeterministic2Group"),
        ("TIMETRA-NAT-MIB", "tmnxNatNotifyV21v0Group"),
        ("TIMETRA-NAT-MIB", "tmnxNatL2AwDynamicBlkAllocGroup"),
        ("TIMETRA-NAT-MIB", "tmnxNatInsideRoutesGroup"),
        ("TIMETRA-NAT-MIB", "tmnxNatPlV21v0Group"),
        ("TIMETRA-NAT-MIB", "tmnxNatDsliteV21v0Group"),
        ("TIMETRA-NAT-MIB", "tmnxNatCupsV21v0Group"),
        ("TIMETRA-NAT-MIB", "tmnxNatPlV22v0Group"),
        ("TIMETRA-NAT-MIB", "tmnxNatPlWmarkV22v0Group"),
        ("TIMETRA-NAT-MIB", "tmnxNatPlWmarkNotifyV22v0Group"),
        ("TIMETRA-NAT-MIB", "tmnxNatCupsV22v0Group"),
        ("TIMETRA-NAT-MIB", "tmnxNatIsaV22v0Group"),
        ("TIMETRA-NAT-MIB", "tmnxNatPlL2AwV22v0Group"),
        ("TIMETRA-NAT-MIB", "tmnxNatSicrV22v0Group"),
        ("TIMETRA-NAT-MIB", "tmnxNatUpPlcyV22v0Group"),
        ("TIMETRA-NAT-MIB", "tmnxNatSourcePrefixV23v0Group"),
        ("TIMETRA-NAT-MIB", "tmnxNatVrtrSpfPlcyV23v0Group"),
        ("TIMETRA-NAT-MIB", "tmnxNatPlV23v0Group"),
        ("TIMETRA-NAT-MIB", "tmnxNatVrtrV23v0Group"),
        ("TIMETRA-NAT-MIB", "tmnxNatLsnV23v0Group"),
        ("TIMETRA-NAT-MIB", "tmnxNatFwdActionV23v0Group"),
        ("TIMETRA-NAT-MIB", "tmnxNatPlLsnV23v0Group"),
        ("TIMETRA-NAT-MIB", "tmnxNatPlLsnV24v0Group"),
        ("TIMETRA-NAT-MIB", "tmnxNatEsaV24v0Group"),
        ("TIMETRA-NAT-MIB", "tmnxNatIsaV24v0Group"),
        ("TIMETRA-NAT-MIB", "tmnxNatMappingV24v0Group"),
        ("TIMETRA-NAT-MIB", "tmnxNatNotifyV24v0Group"),
        ("TIMETRA-NAT-MIB", "tmnxNatGrpCfgV25v0Group"),
        ("TIMETRA-NAT-MIB", "tmnxNatPlRangeExclGroup"),
        ("TIMETRA-NAT-MIB", "tmnxNatPublicIpGroup"),
        ("TIMETRA-NAT-MIB", "tmnxNatIsaV25v0Group"),
        ("TIMETRA-NAT-MIB", "tmnxNatPlV25v0Group"))
)
if mibBuilder.loadTexts:
    tmnxNatV25v0Compliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TIMETRA-NAT-MIB",
    **{"TmnxNatAlgProtocols": TmnxNatAlgProtocols,
       "TmnxPerTenThousand": TmnxPerTenThousand,
       "TmnxNatClassifierAction": TmnxNatClassifierAction,
       "TmnxNatClassifierActionOrNone": TmnxNatClassifierActionOrNone,
       "TmnxNatFiltering": TmnxNatFiltering,
       "TmnxNatFragmentIpMode": TmnxNatFragmentIpMode,
       "TmnxNatFwdActionType": TmnxNatFwdActionType,
       "TmnxNatIsaMdaOperState": TmnxNatIsaMdaOperState,
       "TmnxNatMode": TmnxNatMode,
       "TmnxNatFwdEntryDescription": TmnxNatFwdEntryDescription,
       "TmnxNatPlType": TmnxNatPlType,
       "TmnxNatPolicyPurpose": TmnxNatPolicyPurpose,
       "TmnxNatSubscriberIdString": TmnxNatSubscriberIdString,
       "TmnxNatUsageLevel": TmnxNatUsageLevel,
       "TmnxNatUsageStatsType": TmnxNatUsageStatsType,
       "TmnxNatMemberSubOrHostType": TmnxNatMemberSubOrHostType,
       "TmnxNatInsideRoutesType": TmnxNatInsideRoutesType,
       "timetraNatMIBModule": timetraNatMIBModule,
       "tmnxNatConformance": tmnxNatConformance,
       "tmnxNatCompliances": tmnxNatCompliances,
       "tmnxNatCompliance": tmnxNatCompliance,
       "tmnxNatStatCompliance": tmnxNatStatCompliance,
       "tmnxNatNotifyCompliance": tmnxNatNotifyCompliance,
       "tmnxNatV9v0Compliance": tmnxNatV9v0Compliance,
       "tmnxNatNotifyV9v0Compliance": tmnxNatNotifyV9v0Compliance,
       "tmnxNatV10v0Compliance": tmnxNatV10v0Compliance,
       "tmnxNatNotifyV10v0Compliance": tmnxNatNotifyV10v0Compliance,
       "tmnxNatV11v0Compliance": tmnxNatV11v0Compliance,
       "tmnxNatNotifyV11v0Compliance": tmnxNatNotifyV11v0Compliance,
       "tmnxNatV12v0Compliance": tmnxNatV12v0Compliance,
       "tmnxNatNotifyV12v0Compliance": tmnxNatNotifyV12v0Compliance,
       "tmnxNatV13v0Compliance": tmnxNatV13v0Compliance,
       "tmnxNatNotifyV13v0Compliance": tmnxNatNotifyV13v0Compliance,
       "tmnxNatV14v0Compliance": tmnxNatV14v0Compliance,
       "tmnxNatNotifyV14v0Compliance": tmnxNatNotifyV14v0Compliance,
       "tmnxNatV15v0Compliance": tmnxNatV15v0Compliance,
       "tmnxNatNotifyV15v0Compliance": tmnxNatNotifyV15v0Compliance,
       "tmnxNatV16v0Compliance": tmnxNatV16v0Compliance,
       "tmnxNatV19v0Compliance": tmnxNatV19v0Compliance,
       "tmnxNatV20v0Compliance": tmnxNatV20v0Compliance,
       "tmnxNatV21v0Compliance": tmnxNatV21v0Compliance,
       "tmnxNatV22v0Compliance": tmnxNatV22v0Compliance,
       "tmnxNatV23v0Compliance": tmnxNatV23v0Compliance,
       "tmnxNatNotifyV23v0Compliance": tmnxNatNotifyV23v0Compliance,
       "tmnxNatV24v0Compliance": tmnxNatV24v0Compliance,
       "tmnxNatV25v0Compliance": tmnxNatV25v0Compliance,
       "tmnxNatGroups": tmnxNatGroups,
       "tmnxNatIsaGroup": tmnxNatIsaGroup,
       "tmnxNatIsaStatGroup": tmnxNatIsaStatGroup,
       "tmnxNatPlcyGroup": tmnxNatPlcyGroup,
       "tmnxNatPlcyStatGroup": tmnxNatPlcyStatGroup,
       "tmnxNatVrtrGroup": tmnxNatVrtrGroup,
       "tmnxNatPlGroup": tmnxNatPlGroup,
       "tmnxNatDestGroup": tmnxNatDestGroup,
       "tmnxNatL2AwGroup": tmnxNatL2AwGroup,
       "tmnxNatLsnGroup": tmnxNatLsnGroup,
       "tmnxNatMapGroup": tmnxNatMapGroup,
       "tmnxNatLsnV9v0Group": tmnxNatLsnV9v0Group,
       "tmnxNatVrtrV9v0Group": tmnxNatVrtrV9v0Group,
       "tmnxNatPlcyV9v0Group": tmnxNatPlcyV9v0Group,
       "tmnxNatFwdGroup": tmnxNatFwdGroup,
       "tmnxNatPlV9v0Group": tmnxNatPlV9v0Group,
       "tmnxNatRedGroup": tmnxNatRedGroup,
       "tmnxNatPlcyV10v0Group": tmnxNatPlcyV10v0Group,
       "tmnxNatIsaV10v0Group": tmnxNatIsaV10v0Group,
       "tmnxNatAccGroup": tmnxNatAccGroup,
       "tmnxNatWlanGwGroup": tmnxNatWlanGwGroup,
       "tmnxNat64Group": tmnxNat64Group,
       "tmnxNatLsnSubIdentGroup": tmnxNatLsnSubIdentGroup,
       "tmnxNatPcpGroup": tmnxNatPcpGroup,
       "tmnxNatIsaStatV10v0Group": tmnxNatIsaStatV10v0Group,
       "tmnxNatDeterministicGroup": tmnxNatDeterministicGroup,
       "tmnxNatVrtrIPFilterGroup": tmnxNatVrtrIPFilterGroup,
       "tmnxNatPlV11v0Group": tmnxNatPlV11v0Group,
       "tmnxNatAccV11v0Group": tmnxNatAccV11v0Group,
       "tmnxNatIsaStatV11v0Group": tmnxNatIsaStatV11v0Group,
       "tmnxNatFragmentIpGroup": tmnxNatFragmentIpGroup,
       "tmnxNatMultiPlcyGroup": tmnxNatMultiPlcyGroup,
       "tmnxNatIsaV12v0Group": tmnxNatIsaV12v0Group,
       "tmnxNatQryGroup": tmnxNatQryGroup,
       "tmnxNatVrtrIPFilterV12v0Group": tmnxNatVrtrIPFilterV12v0Group,
       "tmnxNatFwd2Group": tmnxNatFwd2Group,
       "tmnxNatLsnV12v0Group": tmnxNatLsnV12v0Group,
       "tmnxNatLsnSubIdentV12v0Group": tmnxNatLsnSubIdentV12v0Group,
       "tmnxNatPcp2Group": tmnxNatPcp2Group,
       "tmnxNatIsa2Group": tmnxNatIsa2Group,
       "tmnxNatUpnpGroup": tmnxNatUpnpGroup,
       "tmnxNatActiveActiveRedGroup": tmnxNatActiveActiveRedGroup,
       "tmnxNatPlV13v0Group": tmnxNatPlV13v0Group,
       "tmnxNatVrtrIPv6FilterV13v0Group": tmnxNatVrtrIPv6FilterV13v0Group,
       "tmnxNatNoLsnSubBlksFreeGroup": tmnxNatNoLsnSubBlksFreeGroup,
       "tmnxNatWlanGwV14v0Group": tmnxNatWlanGwV14v0Group,
       "tmnxNatVrtrIPFilterV14v0Group": tmnxNatVrtrIPFilterV14v0Group,
       "tmnxNatUpnpV14v0Group": tmnxNatUpnpV14v0Group,
       "tmnxNatPlcyV14v0Group": tmnxNatPlcyV14v0Group,
       "tmnxNatPlcyV15v0Group": tmnxNatPlcyV15v0Group,
       "tmnxNatWlanGwV15v0Group": tmnxNatWlanGwV15v0Group,
       "tmnxNatFwdV15v0Group": tmnxNatFwdV15v0Group,
       "tmnxNatFwdL2AwGroup": tmnxNatFwdL2AwGroup,
       "tmnxNatPcpExt1Group": tmnxNatPcpExt1Group,
       "tmnxNatDeterministic2Group": tmnxNatDeterministic2Group,
       "tmnxNatDetV23v0Group": tmnxNatDetV23v0Group,
       "tmnxNatIsa2V23v0Group": tmnxNatIsa2V23v0Group,
       "tmnxNatPlcyV23v0Group": tmnxNatPlcyV23v0Group,
       "tmnxNatDetV24v0Group": tmnxNatDetV24v0Group,
       "tmnxNatGrpCfgV25v0Group": tmnxNatGrpCfgV25v0Group,
       "tmnxNatPlRangeExclGroup": tmnxNatPlRangeExclGroup,
       "tmnxNatPublicIpGroup": tmnxNatPublicIpGroup,
       "tmnxNatObsoleteGroup": tmnxNatObsoleteGroup,
       "tmnxNatNotifyObjsGroup": tmnxNatNotifyObjsGroup,
       "tmnxNatNotifyGroup": tmnxNatNotifyGroup,
       "tmnxNatNotifyV9v0Group": tmnxNatNotifyV9v0Group,
       "tmnxNatNotifyV10v0Group": tmnxNatNotifyV10v0Group,
       "tmnxNatNotifyV11v0Group": tmnxNatNotifyV11v0Group,
       "tmnxNatNotifyV12v0Group": tmnxNatNotifyV12v0Group,
       "tmnxNatNotifyV13v0Group": tmnxNatNotifyV13v0Group,
       "tmnxNatPlcyXmppEnhGroup": tmnxNatPlcyXmppEnhGroup,
       "tmnxNatFwdCfgGroup": tmnxNatFwdCfgGroup,
       "tmnxNatL2AwV14v0Group": tmnxNatL2AwV14v0Group,
       "tmnxNatDestinationNatGroup": tmnxNatDestinationNatGroup,
       "tmnxNatNotifyV14v0Group": tmnxNatNotifyV14v0Group,
       "tmnxNatMappingGroup": tmnxNatMappingGroup,
       "tmnxNatL2AwExternalAssignGroup": tmnxNatL2AwExternalAssignGroup,
       "tmnxNatFirewallGroup": tmnxNatFirewallGroup,
       "tmnxNatL2AwV15v0Group": tmnxNatL2AwV15v0Group,
       "tmnxNatNotifyV15v0Group": tmnxNatNotifyV15v0Group,
       "tmnxNatSyslogGroup": tmnxNatSyslogGroup,
       "tmnxNatCupsGroup": tmnxNatCupsGroup,
       "tmnxNatNotifyV23v0Group": tmnxNatNotifyV23v0Group,
       "tmnxNatMappingV24v0Group": tmnxNatMappingV24v0Group,
       "tmnxNatObsoletedNotifyGroup": tmnxNatObsoletedNotifyGroup,
       "tmnxNatIsaStatV16v0Group": tmnxNatIsaStatV16v0Group,
       "tmnxNatIsaScalingGroup": tmnxNatIsaScalingGroup,
       "tmnxNatDsliteReassemblyGroup": tmnxNatDsliteReassemblyGroup,
       "tmnxNatSicrGroup": tmnxNatSicrGroup,
       "tmnxNatDestinationNatV19v0Group": tmnxNatDestinationNatV19v0Group,
       "tmnxNatLsnV19v0Group": tmnxNatLsnV19v0Group,
       "tmnxNatEsaV19v0Group": tmnxNatEsaV19v0Group,
       "tmnxNatNotifyV19v0Group": tmnxNatNotifyV19v0Group,
       "tmnxNatNotifyV21v0Group": tmnxNatNotifyV21v0Group,
       "tmnxNatL2AwDynamicBlkAllocGroup": tmnxNatL2AwDynamicBlkAllocGroup,
       "tmnxNatInsideRoutesGroup": tmnxNatInsideRoutesGroup,
       "tmnxNatPlV21v0Group": tmnxNatPlV21v0Group,
       "tmnxNatDsliteV21v0Group": tmnxNatDsliteV21v0Group,
       "tmnxNatCupsV21v0Group": tmnxNatCupsV21v0Group,
       "tmnxNatPlWmarkV22v0Group": tmnxNatPlWmarkV22v0Group,
       "tmnxNatPlWmarkNotifyV22v0Group": tmnxNatPlWmarkNotifyV22v0Group,
       "tmnxNatCupsV22v0Group": tmnxNatCupsV22v0Group,
       "tmnxNatIsaV22v0Group": tmnxNatIsaV22v0Group,
       "tmnxNatPlV22v0Group": tmnxNatPlV22v0Group,
       "tmnxNatPlL2AwV22v0Group": tmnxNatPlL2AwV22v0Group,
       "tmnxNatSicrV22v0Group": tmnxNatSicrV22v0Group,
       "tmnxNatSourcePrefixV23v0Group": tmnxNatSourcePrefixV23v0Group,
       "tmnxNatVrtrSpfPlcyV23v0Group": tmnxNatVrtrSpfPlcyV23v0Group,
       "tmnxNatPlV23v0Group": tmnxNatPlV23v0Group,
       "tmnxNatUpPlcyV22v0Group": tmnxNatUpPlcyV22v0Group,
       "tmnxNatVrtrV23v0Group": tmnxNatVrtrV23v0Group,
       "tmnxNatLsnV23v0Group": tmnxNatLsnV23v0Group,
       "tmnxNatFwdActionV23v0Group": tmnxNatFwdActionV23v0Group,
       "tmnxNatPlLsnV23v0Group": tmnxNatPlLsnV23v0Group,
       "tmnxNatPlLsnV24v0Group": tmnxNatPlLsnV24v0Group,
       "tmnxNatNotifyV24v0Group": tmnxNatNotifyV24v0Group,
       "tmnxNatIsaV24v0Group": tmnxNatIsaV24v0Group,
       "tmnxNatEsaV24v0Group": tmnxNatEsaV24v0Group,
       "tmnxNatIsaV25v0Group": tmnxNatIsaV25v0Group,
       "tmnxNatPlV25v0Group": tmnxNatPlV25v0Group,
       "tmnxNatMGCompliances": tmnxNatMGCompliances,
       "tmnxNatMGGroups": tmnxNatMGGroups,
       "tmnxNat": tmnxNat,
       "tmnxNatObjs": tmnxNatObjs,
       "tmnxNatIsaObjs": tmnxNatIsaObjs,
       "tmnxNatIsaGrpObjs": tmnxNatIsaGrpObjs,
       "tmnxNatIsaGrpTable": tmnxNatIsaGrpTable,
       "tmnxNatIsaGrpEntry": tmnxNatIsaGrpEntry,
       "tmnxNatIsaGrpId": tmnxNatIsaGrpId,
       "tmnxNatIsaGrpRowStatus": tmnxNatIsaGrpRowStatus,
       "tmnxNatIsaGrpLastMgmtChange": tmnxNatIsaGrpLastMgmtChange,
       "tmnxNatIsaGrpDescription": tmnxNatIsaGrpDescription,
       "tmnxNatIsaGrpAdminState": tmnxNatIsaGrpAdminState,
       "tmnxNatIsaGrpActiveMdaLimit": tmnxNatIsaGrpActiveMdaLimit,
       "tmnxNatIsaGrpSessionResvCount": tmnxNatIsaGrpSessionResvCount,
       "tmnxNatIsaGrpSessionWatermarkHi": tmnxNatIsaGrpSessionWatermarkHi,
       "tmnxNatIsaGrpSessionWatermarkLo": tmnxNatIsaGrpSessionWatermarkLo,
       "tmnxNatIsaGrpRedundancy": tmnxNatIsaGrpRedundancy,
       "tmnxNatIsaGrpFailedMdaLimit": tmnxNatIsaGrpFailedMdaLimit,
       "tmnxNatIsaGrpOperState": tmnxNatIsaGrpOperState,
       "tmnxNatIsaGrpDegraded": tmnxNatIsaGrpDegraded,
       "tmnxNatIsaGrpScalingProfile": tmnxNatIsaGrpScalingProfile,
       "tmnxNatIsaGrpSicrReplThreshold": tmnxNatIsaGrpSicrReplThreshold,
       "tmnxNatIsaGrpSicrToAfterSwitch": tmnxNatIsaGrpSicrToAfterSwitch,
       "tmnxNatIsaGrpSicrRouter": tmnxNatIsaGrpSicrRouter,
       "tmnxNatIsaGrpSicrLocAddrType": tmnxNatIsaGrpSicrLocAddrType,
       "tmnxNatIsaGrpSicrLocAddrStart": tmnxNatIsaGrpSicrLocAddrStart,
       "tmnxNatIsaGrpSicrRemAddrType": tmnxNatIsaGrpSicrRemAddrType,
       "tmnxNatIsaGrpSicrRemAddrStart": tmnxNatIsaGrpSicrRemAddrStart,
       "tmnxNatIsaGrpSicrIpMtu": tmnxNatIsaGrpSicrIpMtu,
       "tmnxNatIsaGrpSicrPreferred": tmnxNatIsaGrpSicrPreferred,
       "tmnxNatIsaGrpSicrKaInterval": tmnxNatIsaGrpSicrKaInterval,
       "tmnxNatIsaGrpSicrKaDropcount": tmnxNatIsaGrpSicrKaDropcount,
       "tmnxNatIsaGrpOperGroup": tmnxNatIsaGrpOperGroup,
       "tmnxNatIsaGrpSicrSync": tmnxNatIsaGrpSicrSync,
       "tmnxNatIsaGrpMonitorOperGroup": tmnxNatIsaGrpMonitorOperGroup,
       "tmnxNatGrpCfgTable": tmnxNatGrpCfgTable,
       "tmnxNatGrpCfgEntry": tmnxNatGrpCfgEntry,
       "tmnxNatGrpCfgId": tmnxNatGrpCfgId,
       "tmnxNatGrpCfgLastMgmtChange": tmnxNatGrpCfgLastMgmtChange,
       "tmnxNatGrpCfgSessionResvCount": tmnxNatGrpCfgSessionResvCount,
       "tmnxNatGrpCfgSessionWatermarkHi": tmnxNatGrpCfgSessionWatermarkHi,
       "tmnxNatGrpCfgSessionWatermarkLo": tmnxNatGrpCfgSessionWatermarkLo,
       "tmnxNatGrpCfgAccountingPlcy": tmnxNatGrpCfgAccountingPlcy,
       "tmnxNatGrpCfgSessionUpnpMapLimit": tmnxNatGrpCfgSessionUpnpMapLimit,
       "tmnxNatGrpCfgNoLsnSubBlksFree": tmnxNatGrpCfgNoLsnSubBlksFree,
       "tmnxNatGrpCfgLsn": tmnxNatGrpCfgLsn,
       "tmnxNatGrpCfgNoLsnEvents": tmnxNatGrpCfgNoLsnEvents,
       "tmnxNatGrpCfgLoadBalancing": tmnxNatGrpCfgLoadBalancing,
       "tmnxNatGrpCfgLogPerUpdInterval": tmnxNatGrpCfgLogPerUpdInterval,
       "tmnxNatGrpCfgLogPerUpdRateLimit": tmnxNatGrpCfgLogPerUpdRateLimit,
       "tmnxNatIsaRecoveryAction": tmnxNatIsaRecoveryAction,
       "tmnxNatIsaRecovActCardSlotNum": tmnxNatIsaRecovActCardSlotNum,
       "tmnxNatIsaRecovActCardMDANum": tmnxNatIsaRecovActCardMDANum,
       "tmnxNatIsaRecovActActionGo": tmnxNatIsaRecovActActionGo,
       "tmnxNatIsaRecovActActionResult": tmnxNatIsaRecovActActionResult,
       "tmnxNatGrpMonOperGrpTable": tmnxNatGrpMonOperGrpTable,
       "tmnxNatGrpMonOperGrpEntry": tmnxNatGrpMonOperGrpEntry,
       "tmnxNatGrpMonOperGrpRowStatus": tmnxNatGrpMonOperGrpRowStatus,
       "tmnxNatGrpMonOperGrpLastCh": tmnxNatGrpMonOperGrpLastCh,
       "tmnxNatGrpMonOperGrpHlthDrop": tmnxNatGrpMonOperGrpHlthDrop,
       "tmnxNatGrpMonOperGrpActHlthDrop": tmnxNatGrpMonOperGrpActHlthDrop,
       "tmnxNatGrpMonPortTable": tmnxNatGrpMonPortTable,
       "tmnxNatGrpMonPortEntry": tmnxNatGrpMonPortEntry,
       "tmnxNatGrpMonPortId": tmnxNatGrpMonPortId,
       "tmnxNatGrpMonPortRowStatus": tmnxNatGrpMonPortRowStatus,
       "tmnxNatGrpMonPortLastCh": tmnxNatGrpMonPortLastCh,
       "tmnxNatGrpMonPortHealthDrop": tmnxNatGrpMonPortHealthDrop,
       "tmnxNatGrpMonPortActHealthDrop": tmnxNatGrpMonPortActHealthDrop,
       "tmnxNatMapTGrpTable": tmnxNatMapTGrpTable,
       "tmnxNatMapTGrpEntry": tmnxNatMapTGrpEntry,
       "tmnxNatMapTGrpIsaGrpId": tmnxNatMapTGrpIsaGrpId,
       "tmnxNatMapTGrpRowStatus": tmnxNatMapTGrpRowStatus,
       "tmnxNatMapTGrpLastCh": tmnxNatMapTGrpLastCh,
       "tmnxNatMapTGrpDescription": tmnxNatMapTGrpDescription,
       "tmnxNatMapTGrpAdminState": tmnxNatMapTGrpAdminState,
       "tmnxNatMapTGrpOperState": tmnxNatMapTGrpOperState,
       "tmnxNatMapTGrpFragPerPckt": tmnxNatMapTGrpFragPerPckt,
       "tmnxNatIsaMdaObjs": tmnxNatIsaMdaObjs,
       "tmnxNatIsaMdaTable": tmnxNatIsaMdaTable,
       "tmnxNatIsaMdaEntry": tmnxNatIsaMdaEntry,
       "tmnxNatIsaMdaRowStatus": tmnxNatIsaMdaRowStatus,
       "tmnxNatIsaMdaLastMgmtChange": tmnxNatIsaMdaLastMgmtChange,
       "tmnxNatIsaMdaStatObjs": tmnxNatIsaMdaStatObjs,
       "tmnxNatIsaMdaStatTable": tmnxNatIsaMdaStatTable,
       "tmnxNatIsaMdaStatEntry": tmnxNatIsaMdaStatEntry,
       "tmnxNatIsaMdaStatOperState": tmnxNatIsaMdaStatOperState,
       "tmnxNatIsaMdaStatResrcAllocated": tmnxNatIsaMdaStatResrcAllocated,
       "tmnxNatIsaMdaStatBypassL2AwHost": tmnxNatIsaMdaStatBypassL2AwHost,
       "tmnxNatIsaMemberTable": tmnxNatIsaMemberTable,
       "tmnxNatIsaMemberEntry": tmnxNatIsaMemberEntry,
       "tmnxNatIsaMemberId": tmnxNatIsaMemberId,
       "tmnxNatIsaMemberMdaState": tmnxNatIsaMemberMdaState,
       "tmnxNatIsaMemberMdaChassisIndex": tmnxNatIsaMemberMdaChassisIndex,
       "tmnxNatIsaMemberMdaCardSlotNum": tmnxNatIsaMemberMdaCardSlotNum,
       "tmnxNatIsaMemberMdaSlotNum": tmnxNatIsaMemberMdaSlotNum,
       "tmnxNatIsaMemberIpAddrReserved": tmnxNatIsaMemberIpAddrReserved,
       "tmnxNatIsaMemberBlocksReserved": tmnxNatIsaMemberBlocksReserved,
       "tmnxNatIsaMemberSessionUsage": tmnxNatIsaMemberSessionUsage,
       "tmnxNatIsaMemberSessionUsageHi": tmnxNatIsaMemberSessionUsageHi,
       "tmnxNatIsaMemberSessionsPrio": tmnxNatIsaMemberSessionsPrio,
       "tmnxNatIsaMemberEsaNum": tmnxNatIsaMemberEsaNum,
       "tmnxNatIsaMemberEsaVappNum": tmnxNatIsaMemberEsaVappNum,
       "tmnxNatIsaMemberStatsTable": tmnxNatIsaMemberStatsTable,
       "tmnxNatIsaMemberStatsEntry": tmnxNatIsaMemberStatsEntry,
       "tmnxNatIsaMemberStatsType": tmnxNatIsaMemberStatsType,
       "tmnxNatIsaMemberStatsName": tmnxNatIsaMemberStatsName,
       "tmnxNatIsaMemberStatsVal": tmnxNatIsaMemberStatsVal,
       "tmnxNatIsaMemberStatsValHw": tmnxNatIsaMemberStatsValHw,
       "tmnxNatIsaMemberStatsValue": tmnxNatIsaMemberStatsValue,
       "tmnxNatIsaResrcStatsTable": tmnxNatIsaResrcStatsTable,
       "tmnxNatIsaResrcStatsEntry": tmnxNatIsaResrcStatsEntry,
       "tmnxNatIsaResrcStatsId": tmnxNatIsaResrcStatsId,
       "tmnxNatIsaResrcStatsName": tmnxNatIsaResrcStatsName,
       "tmnxNatIsaResrcStatsValMax": tmnxNatIsaResrcStatsValMax,
       "tmnxNatIsaResrcStatsValMaxLw": tmnxNatIsaResrcStatsValMaxLw,
       "tmnxNatIsaResrcStatsValMaxHw": tmnxNatIsaResrcStatsValMaxHw,
       "tmnxNatIsaResrcStatsVal": tmnxNatIsaResrcStatsVal,
       "tmnxNatIsaResrcStatsValLw": tmnxNatIsaResrcStatsValLw,
       "tmnxNatIsaResrcStatsValHw": tmnxNatIsaResrcStatsValHw,
       "tmnxNatIsaResrcStatsLimited": tmnxNatIsaResrcStatsLimited,
       "tmnxNatIsaResrcStatsValPeak": tmnxNatIsaResrcStatsValPeak,
       "tmnxNatIsaResrcStatsValPeakLw": tmnxNatIsaResrcStatsValPeakLw,
       "tmnxNatIsaResrcStatsValPeakHw": tmnxNatIsaResrcStatsValPeakHw,
       "tmnxNatIsaResrcStatsPeakTime": tmnxNatIsaResrcStatsPeakTime,
       "tmnxNatReassemblyStatsTable": tmnxNatReassemblyStatsTable,
       "tmnxNatReassemblyStatsEntry": tmnxNatReassemblyStatsEntry,
       "tmnxNatReassemblyStatsType": tmnxNatReassemblyStatsType,
       "tmnxNatReassemblyStatsName": tmnxNatReassemblyStatsName,
       "tmnxNatReassemblyStatsVal": tmnxNatReassemblyStatsVal,
       "tmnxNatReassemblyStatsValLw": tmnxNatReassemblyStatsValLw,
       "tmnxNatReassemblyStatsValHw": tmnxNatReassemblyStatsValHw,
       "tmnxNatIsaMemberResrcTable": tmnxNatIsaMemberResrcTable,
       "tmnxNatIsaMemberResrcEntry": tmnxNatIsaMemberResrcEntry,
       "tmnxNatIsaMemberResrcId": tmnxNatIsaMemberResrcId,
       "tmnxNatIsaMemberResrcName": tmnxNatIsaMemberResrcName,
       "tmnxNatIsaMemberResrcValMax": tmnxNatIsaMemberResrcValMax,
       "tmnxNatIsaMemberResrcVal": tmnxNatIsaMemberResrcVal,
       "tmnxNatIsaMemberResrcApplicable": tmnxNatIsaMemberResrcApplicable,
       "tmnxNatIsaMemberResrcValPeak": tmnxNatIsaMemberResrcValPeak,
       "tmnxNatIsaMemberResrcPeakTime": tmnxNatIsaMemberResrcPeakTime,
       "tmnxNatIsaMdaStatsTable": tmnxNatIsaMdaStatsTable,
       "tmnxNatIsaMdaStatsEntry": tmnxNatIsaMdaStatsEntry,
       "tmnxNatIsaMdaStatsType": tmnxNatIsaMdaStatsType,
       "tmnxNatIsaMdaStatsName": tmnxNatIsaMdaStatsName,
       "tmnxNatIsaMdaStatsValue": tmnxNatIsaMdaStatsValue,
       "tmnxNatIsaMdaStatsHrTable": tmnxNatIsaMdaStatsHrTable,
       "tmnxNatIsaMdaStatsHrEntry": tmnxNatIsaMdaStatsHrEntry,
       "tmnxNatIsaMdaStatsHrIndex": tmnxNatIsaMdaStatsHrIndex,
       "tmnxNatIsaMdaStatsHrTime": tmnxNatIsaMdaStatsHrTime,
       "tmnxNatIsaMdaStatsHrWaiting": tmnxNatIsaMdaStatsHrWaiting,
       "tmnxNatIsaMdaStatsHrIdle": tmnxNatIsaMdaStatsHrIdle,
       "tmnxNatIsaMdaStatsHrWorking": tmnxNatIsaMdaStatsHrWorking,
       "tmnxNatIsaMdaStatsHrJobs": tmnxNatIsaMdaStatsHrJobs,
       "tmnxNatIsaMdaStatsHrThroughput": tmnxNatIsaMdaStatsHrThroughput,
       "tmnxNatIsaMdaStatsDayTable": tmnxNatIsaMdaStatsDayTable,
       "tmnxNatIsaMdaStatsDayEntry": tmnxNatIsaMdaStatsDayEntry,
       "tmnxNatIsaMdaStatsDayIndex": tmnxNatIsaMdaStatsDayIndex,
       "tmnxNatIsaMdaStatsDayTime": tmnxNatIsaMdaStatsDayTime,
       "tmnxNatIsaMdaStatsDayWaiting": tmnxNatIsaMdaStatsDayWaiting,
       "tmnxNatIsaMdaStatsDayIdle": tmnxNatIsaMdaStatsDayIdle,
       "tmnxNatIsaMdaStatsDayWorking": tmnxNatIsaMdaStatsDayWorking,
       "tmnxNatIsaMdaStatsDayJobs": tmnxNatIsaMdaStatsDayJobs,
       "tmnxNatIsaMdaStatsDayThroughput": tmnxNatIsaMdaStatsDayThroughput,
       "tmnxNatIsaMdaStatsMonthTable": tmnxNatIsaMdaStatsMonthTable,
       "tmnxNatIsaMdaStatsMonthEntry": tmnxNatIsaMdaStatsMonthEntry,
       "tmnxNatIsaMdaStatsMonthIndex": tmnxNatIsaMdaStatsMonthIndex,
       "tmnxNatIsaMdaStatsMonthTime": tmnxNatIsaMdaStatsMonthTime,
       "tmnxNatIsaMdaStatsMonthWaiting": tmnxNatIsaMdaStatsMonthWaiting,
       "tmnxNatIsaMdaStatsMonthIdle": tmnxNatIsaMdaStatsMonthIdle,
       "tmnxNatIsaMdaStatsMonthWorking": tmnxNatIsaMdaStatsMonthWorking,
       "tmnxNatIsaMdaStatsMonthJobs": tmnxNatIsaMdaStatsMonthJobs,
       "tmnxNatIsaMdaStatsMonthThroughp": tmnxNatIsaMdaStatsMonthThroughp,
       "tmnxNatMemSicrStateTable": tmnxNatMemSicrStateTable,
       "tmnxNatMemSicrStateEntry": tmnxNatMemSicrStateEntry,
       "tmnxNatMemSicrState": tmnxNatMemSicrState,
       "tmnxNatMemSicrPeerState": tmnxNatMemSicrPeerState,
       "tmnxNatMemSicrLocAddrType": tmnxNatMemSicrLocAddrType,
       "tmnxNatMemSicrLocAddr": tmnxNatMemSicrLocAddr,
       "tmnxNatMemSicrRemAddrType": tmnxNatMemSicrRemAddrType,
       "tmnxNatMemSicrRemAddr": tmnxNatMemSicrRemAddr,
       "tmnxNatMemSicrStateLastFailed": tmnxNatMemSicrStateLastFailed,
       "tmnxNatMemSicrStateFailReason": tmnxNatMemSicrStateFailReason,
       "tmnxNatMemSicrStateUnsupp": tmnxNatMemSicrStateUnsupp,
       "tmnxNatMemSicrStateTracked": tmnxNatMemSicrStateTracked,
       "tmnxNatMemSicrStateNotSync": tmnxNatMemSicrStateNotSync,
       "tmnxNatMemSicrStateCreatePending": tmnxNatMemSicrStateCreatePending,
       "tmnxNatMemSicrStateCreateSync": tmnxNatMemSicrStateCreateSync,
       "tmnxNatMemSicrStateDeleteMarked": tmnxNatMemSicrStateDeleteMarked,
       "tmnxNatMemSicrStateDeletePending": tmnxNatMemSicrStateDeletePending,
       "tmnxNatMemSicrStatsTable": tmnxNatMemSicrStatsTable,
       "tmnxNatMemSicrStatsEntry": tmnxNatMemSicrStatsEntry,
       "tmnxNatMemSicrStatsTx": tmnxNatMemSicrStatsTx,
       "tmnxNatMemSicrStatsTxRetransmit": tmnxNatMemSicrStatsTxRetransmit,
       "tmnxNatMemSicrStatsTxFlowCreate": tmnxNatMemSicrStatsTxFlowCreate,
       "tmnxNatMemSicrStatsTxFlowDelete": tmnxNatMemSicrStatsTxFlowDelete,
       "tmnxNatMemSicrStatsRx": tmnxNatMemSicrStatsRx,
       "tmnxNatMemSicrStatsRxFlowCreate": tmnxNatMemSicrStatsRxFlowCreate,
       "tmnxNatMemSicrStatsRxFlowDelete": tmnxNatMemSicrStatsRxFlowDelete,
       "tmnxNatMemSicrStatsErrNoPolicy": tmnxNatMemSicrStatsErrNoPolicy,
       "tmnxNatMemSicrStatsErrNoBlk": tmnxNatMemSicrStatsErrNoBlk,
       "tmnxNatMemSicrStatsErrFrag": tmnxNatMemSicrStatsErrFrag,
       "tmnxNatMemSicrStatsTxAlg": tmnxNatMemSicrStatsTxAlg,
       "tmnxNatMemSicrStatsRxAlg": tmnxNatMemSicrStatsRxAlg,
       "tmnxNatEsaObjs": tmnxNatEsaObjs,
       "tmnxNatVappTable": tmnxNatVappTable,
       "tmnxNatVappEntry": tmnxNatVappEntry,
       "tmnxNatEsaNum": tmnxNatEsaNum,
       "tmnxNatEsaVappNum": tmnxNatEsaVappNum,
       "tmnxNatVappRowStatus": tmnxNatVappRowStatus,
       "tmnxNatVappLastMgmtChange": tmnxNatVappLastMgmtChange,
       "tmnxNatVappStatTable": tmnxNatVappStatTable,
       "tmnxNatVappStatEntry": tmnxNatVappStatEntry,
       "tmnxNatVappStatOperState": tmnxNatVappStatOperState,
       "tmnxNatVappStatResrcAllocated": tmnxNatVappStatResrcAllocated,
       "tmnxNatVappStatBypassL2AwHost": tmnxNatVappStatBypassL2AwHost,
       "tmnxNatVappResrcStatsTable": tmnxNatVappResrcStatsTable,
       "tmnxNatVappResrcStatsEntry": tmnxNatVappResrcStatsEntry,
       "tmnxNatVappResrcStatsId": tmnxNatVappResrcStatsId,
       "tmnxNatVappResrcStatsName": tmnxNatVappResrcStatsName,
       "tmnxNatVappResrcStatsValMax": tmnxNatVappResrcStatsValMax,
       "tmnxNatVappResrcStatsValMaxLw": tmnxNatVappResrcStatsValMaxLw,
       "tmnxNatVappResrcStatsValMaxHw": tmnxNatVappResrcStatsValMaxHw,
       "tmnxNatVappResrcStatsVal": tmnxNatVappResrcStatsVal,
       "tmnxNatVappResrcStatsValLw": tmnxNatVappResrcStatsValLw,
       "tmnxNatVappResrcStatsValHw": tmnxNatVappResrcStatsValHw,
       "tmnxNatVappResrcStatsLimited": tmnxNatVappResrcStatsLimited,
       "tmnxNatVappResrcStatsValPeak": tmnxNatVappResrcStatsValPeak,
       "tmnxNatVappResrcStatsValPeakLw": tmnxNatVappResrcStatsValPeakLw,
       "tmnxNatVappResrcStatsValPeakHw": tmnxNatVappResrcStatsValPeakHw,
       "tmnxNatVappResrcStatsPeakTime": tmnxNatVappResrcStatsPeakTime,
       "tmnxNatVappRecoveryAction": tmnxNatVappRecoveryAction,
       "tmnxNatVappRecovActEsaNum": tmnxNatVappRecovActEsaNum,
       "tmnxNatVappRecovActEsaVappNum": tmnxNatVappRecovActEsaVappNum,
       "tmnxNatVappRecovActActionGo": tmnxNatVappRecovActActionGo,
       "tmnxNatVappRecovActActionResult": tmnxNatVappRecovActActionResult,
       "tmnxNatVappPlcyStatsTable": tmnxNatVappPlcyStatsTable,
       "tmnxNatVappPlcyStatsEntry": tmnxNatVappPlcyStatsEntry,
       "tmnxNatVappPlcyStatsType": tmnxNatVappPlcyStatsType,
       "tmnxNatVappPlcyStatsName": tmnxNatVappPlcyStatsName,
       "tmnxNatVappPlcyStatsVal": tmnxNatVappPlcyStatsVal,
       "tmnxNatVappStatsHrTable": tmnxNatVappStatsHrTable,
       "tmnxNatVappStatsHrEntry": tmnxNatVappStatsHrEntry,
       "tmnxNatVappStatsHrIndex": tmnxNatVappStatsHrIndex,
       "tmnxNatVappStatsHrTime": tmnxNatVappStatsHrTime,
       "tmnxNatVappStatsHrWaiting": tmnxNatVappStatsHrWaiting,
       "tmnxNatVappStatsHrIdle": tmnxNatVappStatsHrIdle,
       "tmnxNatVappStatsHrWorking": tmnxNatVappStatsHrWorking,
       "tmnxNatVappStatsHrJobs": tmnxNatVappStatsHrJobs,
       "tmnxNatVappStatsHrThroughput": tmnxNatVappStatsHrThroughput,
       "tmnxNatVappStatsDayTable": tmnxNatVappStatsDayTable,
       "tmnxNatVappStatsDayEntry": tmnxNatVappStatsDayEntry,
       "tmnxNatVappStatsDayIndex": tmnxNatVappStatsDayIndex,
       "tmnxNatVappStatsDayTime": tmnxNatVappStatsDayTime,
       "tmnxNatVappStatsDayWaiting": tmnxNatVappStatsDayWaiting,
       "tmnxNatVappStatsDayIdle": tmnxNatVappStatsDayIdle,
       "tmnxNatVappStatsDayWorking": tmnxNatVappStatsDayWorking,
       "tmnxNatVappStatsDayJobs": tmnxNatVappStatsDayJobs,
       "tmnxNatVappStatsDayThroughput": tmnxNatVappStatsDayThroughput,
       "tmnxNatVappStatsMonthTable": tmnxNatVappStatsMonthTable,
       "tmnxNatVappStatsMonthEntry": tmnxNatVappStatsMonthEntry,
       "tmnxNatVappStatsMonthIndex": tmnxNatVappStatsMonthIndex,
       "tmnxNatVappStatsMonthTime": tmnxNatVappStatsMonthTime,
       "tmnxNatVappStatsMonthWaiting": tmnxNatVappStatsMonthWaiting,
       "tmnxNatVappStatsMonthIdle": tmnxNatVappStatsMonthIdle,
       "tmnxNatVappStatsMonthWorking": tmnxNatVappStatsMonthWorking,
       "tmnxNatVappStatsMonthJobs": tmnxNatVappStatsMonthJobs,
       "tmnxNatVappStatsMonthThroughp": tmnxNatVappStatsMonthThroughp,
       "tmnxMapTVappTable": tmnxMapTVappTable,
       "tmnxMapTVappEntry": tmnxMapTVappEntry,
       "tmnxMapTVappEsaNum": tmnxMapTVappEsaNum,
       "tmnxMapTVappEsaVappNum": tmnxMapTVappEsaVappNum,
       "tmnxMapTVappRowStatus": tmnxMapTVappRowStatus,
       "tmnxMapTVappLastCh": tmnxMapTVappLastCh,
       "tmnxMapTVappResrcStatsTable": tmnxMapTVappResrcStatsTable,
       "tmnxMapTVappResrcStatsEntry": tmnxMapTVappResrcStatsEntry,
       "tmnxMapTVappResrcStatsId": tmnxMapTVappResrcStatsId,
       "tmnxMapTVappResrcStatsName": tmnxMapTVappResrcStatsName,
       "tmnxMapTVappResrcStatsVal": tmnxMapTVappResrcStatsVal,
       "tmnxMapTVappResrcStatsMaxVal": tmnxMapTVappResrcStatsMaxVal,
       "tmnxMapTVappResrcStatsPeakVal": tmnxMapTVappResrcStatsPeakVal,
       "tmnxMapTVappResrcStatsPeakTime": tmnxMapTVappResrcStatsPeakTime,
       "tmnxNatIsaGrpStatObjs": tmnxNatIsaGrpStatObjs,
       "tmnxNatGrpSicrStateTable": tmnxNatGrpSicrStateTable,
       "tmnxNatGrpSicrStateEntry": tmnxNatGrpSicrStateEntry,
       "tmnxNatGrpSicrState": tmnxNatGrpSicrState,
       "tmnxNatGrpSicrStateChanges": tmnxNatGrpSicrStateChanges,
       "tmnxNatGrpSicrStateLastCh": tmnxNatGrpSicrStateLastCh,
       "tmnxNatGrpSicrInControl": tmnxNatGrpSicrInControl,
       "tmnxNatGrpSicrHealth": tmnxNatGrpSicrHealth,
       "tmnxNatGrpSicrPeerHealth": tmnxNatGrpSicrPeerHealth,
       "tmnxNatGrpSicrPeerPreferred": tmnxNatGrpSicrPeerPreferred,
       "tmnxNatGrpSicrStatsTable": tmnxNatGrpSicrStatsTable,
       "tmnxNatGrpSicrStatsEntry": tmnxNatGrpSicrStatsEntry,
       "tmnxNatGrpSicrTx": tmnxNatGrpSicrTx,
       "tmnxNatGrpSicrTxFailures": tmnxNatGrpSicrTxFailures,
       "tmnxNatGrpSicrRx": tmnxNatGrpSicrRx,
       "tmnxNatGrpSicrRxDropWrongPeer": tmnxNatGrpSicrRxDropWrongPeer,
       "tmnxNatGrpSicrKaTimeout": tmnxNatGrpSicrKaTimeout,
       "tmnxNatPlcyObjs": tmnxNatPlcyObjs,
       "tmnxNatPlcyTable": tmnxNatPlcyTable,
       "tmnxNatPlcyEntry": tmnxNatPlcyEntry,
       "tmnxNatPlcyName": tmnxNatPlcyName,
       "tmnxNatPlcyLastMgmtChange": tmnxNatPlcyLastMgmtChange,
       "tmnxNatPlcyRowStatus": tmnxNatPlcyRowStatus,
       "tmnxNatPlcyDescription": tmnxNatPlcyDescription,
       "tmnxNatPlcyPool": tmnxNatPlcyPool,
       "tmnxNatPlcyPoolVRtr": tmnxNatPlcyPoolVRtr,
       "tmnxNatPlcyFiltering": tmnxNatPlcyFiltering,
       "tmnxNatPlcyPortResvCount": tmnxNatPlcyPortResvCount,
       "tmnxNatPlcyPortWatermarkHigh": tmnxNatPlcyPortWatermarkHigh,
       "tmnxNatPlcyPortWatermarkLow": tmnxNatPlcyPortWatermarkLow,
       "tmnxNatPlcySessionLimit": tmnxNatPlcySessionLimit,
       "tmnxNatPlcySessionResvCount": tmnxNatPlcySessionResvCount,
       "tmnxNatPlcySessionWatermarkHigh": tmnxNatPlcySessionWatermarkHigh,
       "tmnxNatPlcySessionWatermarkLow": tmnxNatPlcySessionWatermarkLow,
       "tmnxNatPlcyPrioSessionFcSet": tmnxNatPlcyPrioSessionFcSet,
       "tmnxNatPlcyToTcpEstab": tmnxNatPlcyToTcpEstab,
       "tmnxNatPlcyToTcpTrans": tmnxNatPlcyToTcpTrans,
       "tmnxNatPlcyToTcpSyn": tmnxNatPlcyToTcpSyn,
       "tmnxNatPlcyToTcpTimeWait": tmnxNatPlcyToTcpTimeWait,
       "tmnxNatPlcyToUdp": tmnxNatPlcyToUdp,
       "tmnxNatPlcyToUdpInitial": tmnxNatPlcyToUdpInitial,
       "tmnxNatPlcyToUdpDns": tmnxNatPlcyToUdpDns,
       "tmnxNatPlcyToIcmpQuery": tmnxNatPlcyToIcmpQuery,
       "tmnxNatPlcyBlkLimit": tmnxNatPlcyBlkLimit,
       "tmnxNatPlcyToSip": tmnxNatPlcyToSip,
       "tmnxNatPlcyAlgEnable": tmnxNatPlcyAlgEnable,
       "tmnxNatPlcyPortFwdLimit": tmnxNatPlcyPortFwdLimit,
       "tmnxNatPlcyUdpInboundRefresh": tmnxNatPlcyUdpInboundRefresh,
       "tmnxNatPlcyIpfixExpPlcy": tmnxNatPlcyIpfixExpPlcy,
       "tmnxNatPlcyTcpMssAdjust": tmnxNatPlcyTcpMssAdjust,
       "tmnxNatPlcyToSubRetention": tmnxNatPlcyToSubRetention,
       "tmnxNatPlcyCreationOrigin": tmnxNatPlcyCreationOrigin,
       "tmnxNatPlcyDnatClassifier": tmnxNatPlcyDnatClassifier,
       "tmnxNatPlcyDnatRouter": tmnxNatPlcyDnatRouter,
       "tmnxNatPlcyDnatIsaGrp": tmnxNatPlcyDnatIsaGrp,
       "tmnxNatPlcyRstUnknownTcp": tmnxNatPlcyRstUnknownTcp,
       "tmnxNatPlcyToTcpRst": tmnxNatPlcyToTcpRst,
       "tmnxNatPlcyPurpose": tmnxNatPlcyPurpose,
       "tmnxNatPlcyToUnknownProtocol": tmnxNatPlcyToUnknownProtocol,
       "tmnxNatPlcyL2Outside": tmnxNatPlcyL2Outside,
       "tmnxNatPlcyPortFwdRangeEnd": tmnxNatPlcyPortFwdRangeEnd,
       "tmnxNatPlcySyslogExpPlcy": tmnxNatPlcySyslogExpPlcy,
       "tmnxNatPlcyDynamicPorts": tmnxNatPlcyDynamicPorts,
       "tmnxNatPlcyStatsTable": tmnxNatPlcyStatsTable,
       "tmnxNatPlcyStatsEntry": tmnxNatPlcyStatsEntry,
       "tmnxNatPlcyStatsType": tmnxNatPlcyStatsType,
       "tmnxNatPlcyStatsName": tmnxNatPlcyStatsName,
       "tmnxNatPlcyStatsVal": tmnxNatPlcyStatsVal,
       "tmnxNatPlcyUnknProtTable": tmnxNatPlcyUnknProtTable,
       "tmnxNatPlcyUnknProtEntry": tmnxNatPlcyUnknProtEntry,
       "tmnxNatPlcyUnknProtNumber": tmnxNatPlcyUnknProtNumber,
       "tmnxNatPlcyUnknProtRowStatus": tmnxNatPlcyUnknProtRowStatus,
       "tmnxNatPlcyUnknProtTimeStamp": tmnxNatPlcyUnknProtTimeStamp,
       "tmnxNatVrtrObjs": tmnxNatVrtrObjs,
       "tmnxNatVrtrTable": tmnxNatVrtrTable,
       "tmnxNatVrtrEntry": tmnxNatVrtrEntry,
       "tmnxNatVrtrLastMgmtChange": tmnxNatVrtrLastMgmtChange,
       "tmnxNatVrtrRowStatus": tmnxNatVrtrRowStatus,
       "tmnxNatVrtrInPolicy": tmnxNatVrtrInPolicy,
       "tmnxNatVrtrInDsliteAdminState": tmnxNatVrtrInDsliteAdminState,
       "tmnxNatVrtrInDsliteSubPrefixLen": tmnxNatVrtrInDsliteSubPrefixLen,
       "tmnxNatVrtrInRedPeerAddrType": tmnxNatVrtrInRedPeerAddrType,
       "tmnxNatVrtrInRedPeerAddr": tmnxNatVrtrInRedPeerAddr,
       "tmnxNatVrtrInRedSteerRtType": tmnxNatVrtrInRedSteerRtType,
       "tmnxNatVrtrInRedSteerRt": tmnxNatVrtrInRedSteerRt,
       "tmnxNatVrtrInRedSteerRtLen": tmnxNatVrtrInRedSteerRtLen,
       "tmnxNatVrtrOutMtu": tmnxNatVrtrOutMtu,
       "tmnxNatVrtrOutUpstreamIPFilterId": tmnxNatVrtrOutUpstreamIPFilterId,
       "tmnxNatVrtrInMaxDetSubscrLimit": tmnxNatVrtrInMaxDetSubscrLimit,
       "tmnxNatVrtrInMaxDetSubLimitDsl": tmnxNatVrtrInMaxDetSubLimitDsl,
       "tmnxNatVrtrOutDnstreamIPFilterId": tmnxNatVrtrOutDnstreamIPFilterId,
       "tmnxNatVrtrInRedPeer6AddrType": tmnxNatVrtrInRedPeer6AddrType,
       "tmnxNatVrtrInRedPeer6Addr": tmnxNatVrtrInRedPeer6Addr,
       "tmnxNatVrtrOutUpstrmIPv6FilterId": tmnxNatVrtrOutUpstrmIPv6FilterId,
       "tmnxNatVrtrOutDnstrmIPv6FilterId": tmnxNatVrtrOutDnstrmIPv6FilterId,
       "tmnxNatVrtrInDnstreamIPFilterId": tmnxNatVrtrInDnstreamIPFilterId,
       "tmnxNatVrtrInDnatSrcPrefixList": tmnxNatVrtrInDnatSrcPrefixList,
       "tmnxNatVrtrOutDnatOnlyRouteLimit": tmnxNatVrtrOutDnatOnlyRouteLimit,
       "tmnxNatVrtrOutDnatOnlyRoutes": tmnxNatVrtrOutDnatOnlyRoutes,
       "tmnxNatVrtrInImportPolicy1": tmnxNatVrtrInImportPolicy1,
       "tmnxNatVrtrInImportPolicy2": tmnxNatVrtrInImportPolicy2,
       "tmnxNatVrtrInImportPolicy3": tmnxNatVrtrInImportPolicy3,
       "tmnxNatVrtrInImportPolicy4": tmnxNatVrtrInImportPolicy4,
       "tmnxNatVrtrInImportPolicy5": tmnxNatVrtrInImportPolicy5,
       "tmnxNatVrtrSourcePrefixOnly": tmnxNatVrtrSourcePrefixOnly,
       "tmnxNatVrtrInL2AwForceUniqueIp": tmnxNatVrtrInL2AwForceUniqueIp,
       "tmnxNatL2AwAddrTable": tmnxNatL2AwAddrTable,
       "tmnxNatL2AwAddrEntry": tmnxNatL2AwAddrEntry,
       "tmnxNatL2AwAddrType": tmnxNatL2AwAddrType,
       "tmnxNatL2AwAddr": tmnxNatL2AwAddr,
       "tmnxNatL2AwAddrPrefixLen": tmnxNatL2AwAddrPrefixLen,
       "tmnxNatL2AwAddrRowStatus": tmnxNatL2AwAddrRowStatus,
       "tmnxNatL2AwAddrLastMgmtChange": tmnxNatL2AwAddrLastMgmtChange,
       "tmnxNat64Table": tmnxNat64Table,
       "tmnxNat64Entry": tmnxNat64Entry,
       "tmnxNat64LastMgmtChange": tmnxNat64LastMgmtChange,
       "tmnxNat64RowStatus": tmnxNat64RowStatus,
       "tmnxNat64InAdminState": tmnxNat64InAdminState,
       "tmnxNat64InSubPrefixLen": tmnxNat64InSubPrefixLen,
       "tmnxNat64InPrefix": tmnxNat64InPrefix,
       "tmnxNat64InPrefixLen": tmnxNat64InPrefixLen,
       "tmnxNat64InIpv6Mtu": tmnxNat64InIpv6Mtu,
       "tmnxNat64InDropZeroIpv4Checksum": tmnxNat64InDropZeroIpv4Checksum,
       "tmnxNat64InSetTos": tmnxNat64InSetTos,
       "tmnxNat64InTos": tmnxNat64InTos,
       "tmnxNat64InIgnoreTos": tmnxNat64InIgnoreTos,
       "tmnxNat64InInsertIpv6FragHeader": tmnxNat64InInsertIpv6FragHeader,
       "tmnxNat64InFragmentIp": tmnxNat64InFragmentIp,
       "tmnxNatSubIdTable": tmnxNatSubIdTable,
       "tmnxNatSubIdEntry": tmnxNatSubIdEntry,
       "tmnxNatSubIdLastMgmtChange": tmnxNatSubIdLastMgmtChange,
       "tmnxNatSubIdDescription": tmnxNatSubIdDescription,
       "tmnxNatSubIdAdminState": tmnxNatSubIdAdminState,
       "tmnxNatSubIdRadProxSrvRouter": tmnxNatSubIdRadProxSrvRouter,
       "tmnxNatSubIdRadProxSrvName": tmnxNatSubIdRadProxSrvName,
       "tmnxNatSubIdRadiusAttributeType": tmnxNatSubIdRadiusAttributeType,
       "tmnxNatSubIdRadiusVendorId": tmnxNatSubIdRadiusVendorId,
       "tmnxNatSubIdDropUnidentified": tmnxNatSubIdDropUnidentified,
       "tmnxNatDetPlcyTable": tmnxNatDetPlcyTable,
       "tmnxNatDetPlcyEntry": tmnxNatDetPlcyEntry,
       "tmnxNatDetPlcySubType": tmnxNatDetPlcySubType,
       "tmnxNatDetPlcyAddrType": tmnxNatDetPlcyAddrType,
       "tmnxNatDetPlcyAddr": tmnxNatDetPlcyAddr,
       "tmnxNatDetPlcyAddrPrefixLength": tmnxNatDetPlcyAddrPrefixLength,
       "tmnxNatDetPlcyRowStatus": tmnxNatDetPlcyRowStatus,
       "tmnxNatDetPlcyLastMgmtChange": tmnxNatDetPlcyLastMgmtChange,
       "tmnxNatDetPlcyName": tmnxNatDetPlcyName,
       "tmnxNatDetPlcyAdminState": tmnxNatDetPlcyAdminState,
       "tmnxNatDetPlcyOperState": tmnxNatDetPlcyOperState,
       "tmnxNatDetMapTable": tmnxNatDetMapTable,
       "tmnxNatDetMapEntry": tmnxNatDetMapEntry,
       "tmnxNatDetMapInAddrType": tmnxNatDetMapInAddrType,
       "tmnxNatDetMapInStart": tmnxNatDetMapInStart,
       "tmnxNatDetMapInEnd": tmnxNatDetMapInEnd,
       "tmnxNatDetMapRowStatus": tmnxNatDetMapRowStatus,
       "tmnxNatDetMapLastCh": tmnxNatDetMapLastCh,
       "tmnxNatDetMapOutAddrType": tmnxNatDetMapOutAddrType,
       "tmnxNatDetMapOutStart": tmnxNatDetMapOutStart,
       "tmnxNatDetMapOperState": tmnxNatDetMapOperState,
       "tmnxNatDetPfxMapTable": tmnxNatDetPfxMapTable,
       "tmnxNatDetPfxMapEntry": tmnxNatDetPfxMapEntry,
       "tmnxNatDetPfxMapSubType": tmnxNatDetPfxMapSubType,
       "tmnxNatDetPfxMapAddrType": tmnxNatDetPfxMapAddrType,
       "tmnxNatDetPfxMapAddr": tmnxNatDetPfxMapAddr,
       "tmnxNatDetPfxMapAddrPrefixLength": tmnxNatDetPfxMapAddrPrefixLength,
       "tmnxNatDetPfxMapNatPolicy": tmnxNatDetPfxMapNatPolicy,
       "tmnxNatDetPfxMapRowStatus": tmnxNatDetPfxMapRowStatus,
       "tmnxNatDetPfxMapLastMgmtChange": tmnxNatDetPfxMapLastMgmtChange,
       "tmnxNatDetPfxMapAdminState": tmnxNatDetPfxMapAdminState,
       "tmnxNatDetPfxMapOperState": tmnxNatDetPfxMapOperState,
       "tmnxNatDetMap2Table": tmnxNatDetMap2Table,
       "tmnxNatDetMap2Entry": tmnxNatDetMap2Entry,
       "tmnxNatDetMap2InAddrType": tmnxNatDetMap2InAddrType,
       "tmnxNatDetMap2InStart": tmnxNatDetMap2InStart,
       "tmnxNatDetMap2InEnd": tmnxNatDetMap2InEnd,
       "tmnxNatDetMap2RowStatus": tmnxNatDetMap2RowStatus,
       "tmnxNatDetMap2LastCh": tmnxNatDetMap2LastCh,
       "tmnxNatDetMap2OutAddrType": tmnxNatDetMap2OutAddrType,
       "tmnxNatDetMap2OutStart": tmnxNatDetMap2OutStart,
       "tmnxNatDetMap2OperState": tmnxNatDetMap2OperState,
       "tmnxNatVrtrSpfPlcyTable": tmnxNatVrtrSpfPlcyTable,
       "tmnxNatVrtrSpfPlcyEntry": tmnxNatVrtrSpfPlcyEntry,
       "tmnxNatVrtrSpfPlcyInPolicy": tmnxNatVrtrSpfPlcyInPolicy,
       "tmnxNatVrtrSpfPlcyLastMgmChg": tmnxNatVrtrSpfPlcyLastMgmChg,
       "tmnxNatVrtrSpfPlcyRowStatus": tmnxNatVrtrSpfPlcyRowStatus,
       "tmnxNatDetAddrMapTable": tmnxNatDetAddrMapTable,
       "tmnxNatDetAddrMapEntry": tmnxNatDetAddrMapEntry,
       "tmnxNatDetAddrMapSubType": tmnxNatDetAddrMapSubType,
       "tmnxNatDetAddrMapInStartType": tmnxNatDetAddrMapInStartType,
       "tmnxNatDetAddrMapInStart": tmnxNatDetAddrMapInStart,
       "tmnxNatDetAddrMapInStartPfxLen": tmnxNatDetAddrMapInStartPfxLen,
       "tmnxNatDetAddrMapInEndType": tmnxNatDetAddrMapInEndType,
       "tmnxNatDetAddrMapInEnd": tmnxNatDetAddrMapInEnd,
       "tmnxNatDetAddrMapInEndPfxLen": tmnxNatDetAddrMapInEndPfxLen,
       "tmnxNatDetAddrMapNatPolicy": tmnxNatDetAddrMapNatPolicy,
       "tmnxNatDetAddrMapRowStatus": tmnxNatDetAddrMapRowStatus,
       "tmnxNatDetAddrMapLastCh": tmnxNatDetAddrMapLastCh,
       "tmnxNatDetAddrMapAdminState": tmnxNatDetAddrMapAdminState,
       "tmnxNatDetAddrMapOperState": tmnxNatDetAddrMapOperState,
       "tmnxNatDetAddrMapOutStartType": tmnxNatDetAddrMapOutStartType,
       "tmnxNatDetAddrMapOutStart": tmnxNatDetAddrMapOutStart,
       "tmnxNatPoolObjs": tmnxNatPoolObjs,
       "tmnxNatPlTable": tmnxNatPlTable,
       "tmnxNatPlEntry": tmnxNatPlEntry,
       "tmnxNatPlName": tmnxNatPlName,
       "tmnxNatPlRowStatus": tmnxNatPlRowStatus,
       "tmnxNatPlLastMgmtChange": tmnxNatPlLastMgmtChange,
       "tmnxNatPlIsaGrp": tmnxNatPlIsaGrp,
       "tmnxNatPlType": tmnxNatPlType,
       "tmnxNatPlDescription": tmnxNatPlDescription,
       "tmnxNatPlAdminState": tmnxNatPlAdminState,
       "tmnxNatPlPortResvType": tmnxNatPlPortResvType,
       "tmnxNatPlPortResvVal": tmnxNatPlPortResvVal,
       "tmnxNatPlPortResvAllowPrivileged": tmnxNatPlPortResvAllowPrivileged,
       "tmnxNatPlWatermarkHigh": tmnxNatPlWatermarkHigh,
       "tmnxNatPlWatermarkLow": tmnxNatPlWatermarkLow,
       "tmnxNatPlMode": tmnxNatPlMode,
       "tmnxNatPlPortFwdRangeEnd": tmnxNatPlPortFwdRangeEnd,
       "tmnxNatPlPortFwdDynBlkResv": tmnxNatPlPortFwdDynBlkResv,
       "tmnxNatPlOperMode": tmnxNatPlOperMode,
       "tmnxNatPlApplications": tmnxNatPlApplications,
       "tmnxNatPlIcmpEchoReply": tmnxNatPlIcmpEchoReply,
       "tmnxNatPlExPrtBlcksWatermarkHigh": tmnxNatPlExPrtBlcksWatermarkHigh,
       "tmnxNatPlExPrtBlcksWatermarkLow": tmnxNatPlExPrtBlcksWatermarkLow,
       "tmnxNatPlPortFwdRangeStart": tmnxNatPlPortFwdRangeStart,
       "tmnxNatPlDhInsideIpAddrType": tmnxNatPlDhInsideIpAddrType,
       "tmnxNatPlDhInsideIpAddress": tmnxNatPlDhInsideIpAddress,
       "tmnxNatPlDhInsideRtrId": tmnxNatPlDhInsideRtrId,
       "tmnxNatPlDhRate": tmnxNatPlDhRate,
       "tmnxNatPlAddrPooling": tmnxNatPlAddrPooling,
       "tmnxNatPlDhForwardedPackets": tmnxNatPlDhForwardedPackets,
       "tmnxNatPlDhDroppedPackets": tmnxNatPlDhDroppedPackets,
       "tmnxNatPlMonitorOperGroup": tmnxNatPlMonitorOperGroup,
       "tmnxNatPlRangeTable": tmnxNatPlRangeTable,
       "tmnxNatPlRangeEntry": tmnxNatPlRangeEntry,
       "tmnxNatPlRangeAddrType": tmnxNatPlRangeAddrType,
       "tmnxNatPlRangeStart": tmnxNatPlRangeStart,
       "tmnxNatPlRangeEnd": tmnxNatPlRangeEnd,
       "tmnxNatPlRangeRowStatus": tmnxNatPlRangeRowStatus,
       "tmnxNatPlRangeLastMgmtChange": tmnxNatPlRangeLastMgmtChange,
       "tmnxNatPlRangeDescription": tmnxNatPlRangeDescription,
       "tmnxNatPlRangeAdminDrain": tmnxNatPlRangeAdminDrain,
       "tmnxNatPlRangeNumAllocatedBlk": tmnxNatPlRangeNumAllocatedBlk,
       "tmnxNatPlL2AwTable": tmnxNatPlL2AwTable,
       "tmnxNatPlL2AwEntry": tmnxNatPlL2AwEntry,
       "tmnxNatPlL2AwBlockUsage": tmnxNatPlL2AwBlockUsage,
       "tmnxNatPlL2AwBlockUsageHi": tmnxNatPlL2AwBlockUsageHi,
       "tmnxNatPlL2AwExternalAssignment": tmnxNatPlL2AwExternalAssignment,
       "tmnxNatPlL2AwDynResv": tmnxNatPlL2AwDynResv,
       "tmnxNatPlL2AwDynResvSubscrLimit": tmnxNatPlL2AwDynResvSubscrLimit,
       "tmnxNatPlL2AwDynResvPorts": tmnxNatPlL2AwDynResvPorts,
       "tmnxNatPlL2AwSubscrWatermarkHigh": tmnxNatPlL2AwSubscrWatermarkHigh,
       "tmnxNatPlL2AwSubscrWatermarkLow": tmnxNatPlL2AwSubscrWatermarkLow,
       "tmnxNatPlL2AwSubscrUsage": tmnxNatPlL2AwSubscrUsage,
       "tmnxNatPlL2AwSubscrUsageHi": tmnxNatPlL2AwSubscrUsageHi,
       "tmnxNatPlL2AwDynResvNumShrdBlcks": tmnxNatPlL2AwDynResvNumShrdBlcks,
       "tmnxNatPlLsnMemberTable": tmnxNatPlLsnMemberTable,
       "tmnxNatPlLsnMemberEntry": tmnxNatPlLsnMemberEntry,
       "tmnxNatPlLsnMemberIsaGrpId": tmnxNatPlLsnMemberIsaGrpId,
       "tmnxNatPlLsnMemberBlockUsage": tmnxNatPlLsnMemberBlockUsage,
       "tmnxNatPlLsnMemberBlockUsageHi": tmnxNatPlLsnMemberBlockUsageHi,
       "tmnxNatPlLsnMbrTcpPortUsage": tmnxNatPlLsnMbrTcpPortUsage,
       "tmnxNatPlLsnMbrTcpPortUsageHi": tmnxNatPlLsnMbrTcpPortUsageHi,
       "tmnxNatPlLsnMbrUdpPortUsage": tmnxNatPlLsnMbrUdpPortUsage,
       "tmnxNatPlLsnMbrUdpPortUsageHi": tmnxNatPlLsnMbrUdpPortUsageHi,
       "tmnxNatPlLsnMbrOtherPortUsage": tmnxNatPlLsnMbrOtherPortUsage,
       "tmnxNatPlLsnMbrOtherPortUsageHi": tmnxNatPlLsnMbrOtherPortUsageHi,
       "tmnxNatBlkL2AwTable": tmnxNatBlkL2AwTable,
       "tmnxNatBlkL2AwEntry": tmnxNatBlkL2AwEntry,
       "tmnxNatBlkL2AwAddrType": tmnxNatBlkL2AwAddrType,
       "tmnxNatBlkL2AwAddr": tmnxNatBlkL2AwAddr,
       "tmnxNatBlkL2AwStart": tmnxNatBlkL2AwStart,
       "tmnxNatBlkL2AwEnd": tmnxNatBlkL2AwEnd,
       "tmnxNatBlkL2AwPool": tmnxNatBlkL2AwPool,
       "tmnxNatBlkL2AwSubIdent": tmnxNatBlkL2AwSubIdent,
       "tmnxNatBlkL2AwPolicy": tmnxNatBlkL2AwPolicy,
       "tmnxNatBlkL2AwStartDateAndTime": tmnxNatBlkL2AwStartDateAndTime,
       "tmnxNatBlkLsnTable": tmnxNatBlkLsnTable,
       "tmnxNatBlkLsnEntry": tmnxNatBlkLsnEntry,
       "tmnxNatBlkLsnAddrType": tmnxNatBlkLsnAddrType,
       "tmnxNatBlkLsnAddr": tmnxNatBlkLsnAddr,
       "tmnxNatBlkLsnStart": tmnxNatBlkLsnStart,
       "tmnxNatBlkLsnEnd": tmnxNatBlkLsnEnd,
       "tmnxNatBlkLsnPool": tmnxNatBlkLsnPool,
       "tmnxNatBlkLsnSubId": tmnxNatBlkLsnSubId,
       "tmnxNatBlkLsnInsideVRtrID": tmnxNatBlkLsnInsideVRtrID,
       "tmnxNatBlkLsnInsideAddrType": tmnxNatBlkLsnInsideAddrType,
       "tmnxNatBlkLsnInsideAddr": tmnxNatBlkLsnInsideAddr,
       "tmnxNatBlkLsnPolicy": tmnxNatBlkLsnPolicy,
       "tmnxNatBlkLsnStartDateAndTime": tmnxNatBlkLsnStartDateAndTime,
       "tmnxNatPlLsnTable": tmnxNatPlLsnTable,
       "tmnxNatPlLsnEntry": tmnxNatPlLsnEntry,
       "tmnxNatPlLsnSubscriberLimit": tmnxNatPlLsnSubscriberLimit,
       "tmnxNatPlLsnRedExpPrefixType": tmnxNatPlLsnRedExpPrefixType,
       "tmnxNatPlLsnRedExpPrefix": tmnxNatPlLsnRedExpPrefix,
       "tmnxNatPlLsnRedExpPrefixLen": tmnxNatPlLsnRedExpPrefixLen,
       "tmnxNatPlLsnRedMonPrefixType": tmnxNatPlLsnRedMonPrefixType,
       "tmnxNatPlLsnRedMonPrefix": tmnxNatPlLsnRedMonPrefix,
       "tmnxNatPlLsnRedMonPrefixLen": tmnxNatPlLsnRedMonPrefixLen,
       "tmnxNatPlLsnRedActive": tmnxNatPlLsnRedActive,
       "tmnxNatPlLsnDetPortResv": tmnxNatPlLsnDetPortResv,
       "tmnxNatPlLsnRedAdminState": tmnxNatPlLsnRedAdminState,
       "tmnxNatPlLsnRedFollowPoolRouter": tmnxNatPlLsnRedFollowPoolRouter,
       "tmnxNatPlLsnRedFollowPool": tmnxNatPlLsnRedFollowPool,
       "tmnxNatPlLsnFreePortLimitTcp": tmnxNatPlLsnFreePortLimitTcp,
       "tmnxNatPlLsnFreePortLimitUdp": tmnxNatPlLsnFreePortLimitUdp,
       "tmnxNatPlLsnFreePortLimitIcmp": tmnxNatPlLsnFreePortLimitIcmp,
       "tmnxNatPlLsnRedState": tmnxNatPlLsnRedState,
       "tmnxNatPlLsnRedStateReason": tmnxNatPlLsnRedStateReason,
       "tmnxNatPlLsnCpmReservedPorts": tmnxNatPlLsnCpmReservedPorts,
       "tmnxNatPlHistAction": tmnxNatPlHistAction,
       "tmnxNatPlHistActionVRtrId": tmnxNatPlHistActionVRtrId,
       "tmnxNatPlHistActionPoolName": tmnxNatPlHistActionPoolName,
       "tmnxNatPlHistActionBucketSize": tmnxNatPlHistActionBucketSize,
       "tmnxNatPlHistActionNumBuckets": tmnxNatPlHistActionNumBuckets,
       "tmnxNatPlHistActionGo": tmnxNatPlHistActionGo,
       "tmnxNatPlHistTable": tmnxNatPlHistTable,
       "tmnxNatPlHistEntry": tmnxNatPlHistEntry,
       "tmnxNatPlHistIndex": tmnxNatPlHistIndex,
       "tmnxNatPlHistTimestamp": tmnxNatPlHistTimestamp,
       "tmnxNatPlHistVRtrID": tmnxNatPlHistVRtrID,
       "tmnxNatPlHistPoolName": tmnxNatPlHistPoolName,
       "tmnxNatPlHistBucketSize": tmnxNatPlHistBucketSize,
       "tmnxNatPlHistNumBuckets": tmnxNatPlHistNumBuckets,
       "tmnxNatPlHistTcp": tmnxNatPlHistTcp,
       "tmnxNatPlHistUdp": tmnxNatPlHistUdp,
       "tmnxNatPlHistIcmp": tmnxNatPlHistIcmp,
       "tmnxNatPlRangeStatTable": tmnxNatPlRangeStatTable,
       "tmnxNatPlRangeStatEntry": tmnxNatPlRangeStatEntry,
       "tmnxNatPlRangeStatNumAllocBlk": tmnxNatPlRangeStatNumAllocBlk,
       "tmnxNatPlRangeStatNumAllocSub": tmnxNatPlRangeStatNumAllocSub,
       "tmnxNatPlL2AwMemberTable": tmnxNatPlL2AwMemberTable,
       "tmnxNatPlL2AwMemberEntry": tmnxNatPlL2AwMemberEntry,
       "tmnxNatPlL2AwMemberIsaGrpId": tmnxNatPlL2AwMemberIsaGrpId,
       "tmnxNatPlL2AwMemberBlockUsage": tmnxNatPlL2AwMemberBlockUsage,
       "tmnxNatPlL2AwMemberBlockUsageHi": tmnxNatPlL2AwMemberBlockUsageHi,
       "tmnxNatPlRangeExclTable": tmnxNatPlRangeExclTable,
       "tmnxNatPlRangeExclEntry": tmnxNatPlRangeExclEntry,
       "tmnxNatPlRangeExclStart": tmnxNatPlRangeExclStart,
       "tmnxNatPlRangeExclEnd": tmnxNatPlRangeExclEnd,
       "tmnxNatPlRangeExclRowStatus": tmnxNatPlRangeExclRowStatus,
       "tmnxNatPlRangeExclLastMgmtChange": tmnxNatPlRangeExclLastMgmtChange,
       "tmnxNatDestObjs": tmnxNatDestObjs,
       "tmnxNatDestTable": tmnxNatDestTable,
       "tmnxNatDestEntry": tmnxNatDestEntry,
       "tmnxNatDestAddrType": tmnxNatDestAddrType,
       "tmnxNatDestAddr": tmnxNatDestAddr,
       "tmnxNatDestPrefixLen": tmnxNatDestPrefixLen,
       "tmnxNatDestRowStatus": tmnxNatDestRowStatus,
       "tmnxNatDestLastMgmtChange": tmnxNatDestLastMgmtChange,
       "tmnxNatDestNatPolicy": tmnxNatDestNatPolicy,
       "tmnxNatDsliteAddrTable": tmnxNatDsliteAddrTable,
       "tmnxNatDsliteAddrEntry": tmnxNatDsliteAddrEntry,
       "tmnxNatDsliteAddrType": tmnxNatDsliteAddrType,
       "tmnxNatDsliteAddr": tmnxNatDsliteAddr,
       "tmnxNatDsliteAddrRowStatus": tmnxNatDsliteAddrRowStatus,
       "tmnxNatDsliteAddrLastMgmtChange": tmnxNatDsliteAddrLastMgmtChange,
       "tmnxNatDsliteAddrTunnelMtu": tmnxNatDsliteAddrTunnelMtu,
       "tmnxNatDsliteAddrFragmentIp": tmnxNatDsliteAddrFragmentIp,
       "tmnxNatDsliteAddrReassembly": tmnxNatDsliteAddrReassembly,
       "tmnxNatDsliteAddrMinFrstFrgSzRx": tmnxNatDsliteAddrMinFrstFrgSzRx,
       "tmnxNatInsideRoutesTable": tmnxNatInsideRoutesTable,
       "tmnxNatInsideRoutesEntry": tmnxNatInsideRoutesEntry,
       "tmnxNatInsideRoutesAddrType": tmnxNatInsideRoutesAddrType,
       "tmnxNatInsideRoutesAddr": tmnxNatInsideRoutesAddr,
       "tmnxNatInsideRoutesPrefixLen": tmnxNatInsideRoutesPrefixLen,
       "tmnxNatInsideRoutesNatPolicy": tmnxNatInsideRoutesNatPolicy,
       "tmnxNatInsideRoutesType": tmnxNatInsideRoutesType,
       "tmnxNatSubObjs": tmnxNatSubObjs,
       "tmnxNatLsnHostTable": tmnxNatLsnHostTable,
       "tmnxNatLsnHostEntry": tmnxNatLsnHostEntry,
       "tmnxNatLsnHostAddrType": tmnxNatLsnHostAddrType,
       "tmnxNatLsnHostAddr": tmnxNatLsnHostAddr,
       "tmnxNatLsnHostSubId": tmnxNatLsnHostSubId,
       "tmnxNatLsnHostOutVRtrID": tmnxNatLsnHostOutVRtrID,
       "tmnxNatLsnHostOutAddrType": tmnxNatLsnHostOutAddrType,
       "tmnxNatLsnHostOutAddr": tmnxNatLsnHostOutAddr,
       "tmnxNatLsnSubTable": tmnxNatLsnSubTable,
       "tmnxNatLsnSubEntry": tmnxNatLsnSubEntry,
       "tmnxNatLsnSubId": tmnxNatLsnSubId,
       "tmnxNatLsnSubPolicy": tmnxNatLsnSubPolicy,
       "tmnxNatLsnSubIsaGrp": tmnxNatLsnSubIsaGrp,
       "tmnxNatLsnSubIsaMemberId": tmnxNatLsnSubIsaMemberId,
       "tmnxNatLsnSubOutVRtrID": tmnxNatLsnSubOutVRtrID,
       "tmnxNatLsnSubOutAddrType": tmnxNatLsnSubOutAddrType,
       "tmnxNatLsnSubOutAddr": tmnxNatLsnSubOutAddr,
       "tmnxNatLsnSubIdStr": tmnxNatLsnSubIdStr,
       "tmnxNatLsnSubStatTable": tmnxNatLsnSubStatTable,
       "tmnxNatLsnSubStatEntry": tmnxNatLsnSubStatEntry,
       "tmnxNatLsnSubStatIcmpPortUsage": tmnxNatLsnSubStatIcmpPortUsage,
       "tmnxNatLsnSubStatIcmpPortUsageHi": tmnxNatLsnSubStatIcmpPortUsageHi,
       "tmnxNatLsnSubStatUdpPortUsage": tmnxNatLsnSubStatUdpPortUsage,
       "tmnxNatLsnSubStatUdpPortUsageHi": tmnxNatLsnSubStatUdpPortUsageHi,
       "tmnxNatLsnSubStatTcpPortUsage": tmnxNatLsnSubStatTcpPortUsage,
       "tmnxNatLsnSubStatTcpPortUsageHi": tmnxNatLsnSubStatTcpPortUsageHi,
       "tmnxNatLsnSubStatSessionUsage": tmnxNatLsnSubStatSessionUsage,
       "tmnxNatLsnSubStatSessionUsageHi": tmnxNatLsnSubStatSessionUsageHi,
       "tmnxNatLsnSubStatSessions": tmnxNatLsnSubStatSessions,
       "tmnxNatLsnSubStatSessionsPrio": tmnxNatLsnSubStatSessionsPrio,
       "tmnxNatLsnSubStatSessionsPeak": tmnxNatLsnSubStatSessionsPeak,
       "tmnxNatLsnSubBlkTable": tmnxNatLsnSubBlkTable,
       "tmnxNatLsnSubBlkEntry": tmnxNatLsnSubBlkEntry,
       "tmnxNatLsnSubBlkEnd": tmnxNatLsnSubBlkEnd,
       "tmnxNatLsnSubBlkPolicy": tmnxNatLsnSubBlkPolicy,
       "tmnxNatDsliteSubTable": tmnxNatDsliteSubTable,
       "tmnxNatDsliteSubEntry": tmnxNatDsliteSubEntry,
       "tmnxNatDsliteSubAddrType": tmnxNatDsliteSubAddrType,
       "tmnxNatDsliteSubAddr": tmnxNatDsliteSubAddr,
       "tmnxNatDsliteSubAddrPrefixLength": tmnxNatDsliteSubAddrPrefixLength,
       "tmnxNatDsliteSubId": tmnxNatDsliteSubId,
       "tmnxNatL2AwHostTable": tmnxNatL2AwHostTable,
       "tmnxNatL2AwHostEntry": tmnxNatL2AwHostEntry,
       "tmnxNatL2AwHostAddrType": tmnxNatL2AwHostAddrType,
       "tmnxNatL2AwHostAddr": tmnxNatL2AwHostAddr,
       "tmnxNatL2AwHostOutVRtrID": tmnxNatL2AwHostOutVRtrID,
       "tmnxNatL2AwHostOutAddrType": tmnxNatL2AwHostOutAddrType,
       "tmnxNatL2AwHostOutAddr": tmnxNatL2AwHostOutAddr,
       "tmnxNatL2AwHostOutStart": tmnxNatL2AwHostOutStart,
       "tmnxNatL2AwSubTable": tmnxNatL2AwSubTable,
       "tmnxNatL2AwSubEntry": tmnxNatL2AwSubEntry,
       "tmnxNatL2AwSubPolicy": tmnxNatL2AwSubPolicy,
       "tmnxNatL2AwSubIsaGrp": tmnxNatL2AwSubIsaGrp,
       "tmnxNatL2AwSubIsaMemberId": tmnxNatL2AwSubIsaMemberId,
       "tmnxNatL2AwSubOutVRtrID": tmnxNatL2AwSubOutVRtrID,
       "tmnxNatL2AwSubOutAddrType": tmnxNatL2AwSubOutAddrType,
       "tmnxNatL2AwSubOutAddr": tmnxNatL2AwSubOutAddr,
       "tmnxNatL2AwSubCurrUpnpPlcy": tmnxNatL2AwSubCurrUpnpPlcy,
       "tmnxNatL2AwSubHostPortBlkSize": tmnxNatL2AwSubHostPortBlkSize,
       "tmnxNatL2AwSubFirewallPolicy": tmnxNatL2AwSubFirewallPolicy,
       "tmnxNatL2AwSubStatTable": tmnxNatL2AwSubStatTable,
       "tmnxNatL2AwSubStatEntry": tmnxNatL2AwSubStatEntry,
       "tmnxNatL2AwSubStatNatPolicy": tmnxNatL2AwSubStatNatPolicy,
       "tmnxNatL2AwSubStatIcmpPortUsage": tmnxNatL2AwSubStatIcmpPortUsage,
       "tmnxNatL2AwSubStatIcmpPortUsageH": tmnxNatL2AwSubStatIcmpPortUsageH,
       "tmnxNatL2AwSubStatUdpPortUsage": tmnxNatL2AwSubStatUdpPortUsage,
       "tmnxNatL2AwSubStatUdpPortUsageHi": tmnxNatL2AwSubStatUdpPortUsageHi,
       "tmnxNatL2AwSubStatTcpPortUsage": tmnxNatL2AwSubStatTcpPortUsage,
       "tmnxNatL2AwSubStatTcpPortUsageHi": tmnxNatL2AwSubStatTcpPortUsageHi,
       "tmnxNatL2AwSubStatSessionUsage": tmnxNatL2AwSubStatSessionUsage,
       "tmnxNatL2AwSubStatSessionUsageHi": tmnxNatL2AwSubStatSessionUsageHi,
       "tmnxNatL2AwSubStatSessions": tmnxNatL2AwSubStatSessions,
       "tmnxNatL2AwSubStatSessionsPrio": tmnxNatL2AwSubStatSessionsPrio,
       "tmnxNatL2AwSubStatSessionsPeak": tmnxNatL2AwSubStatSessionsPeak,
       "tmnxNatL2AwSubStatCurrUpnpPlcy": tmnxNatL2AwSubStatCurrUpnpPlcy,
       "tmnxNatL2AwSubStatPlcyPurpose": tmnxNatL2AwSubStatPlcyPurpose,
       "tmnxNatL2AwSubStatDownstreamDrop": tmnxNatL2AwSubStatDownstreamDrop,
       "tmnxNatL2AwSubStatUnknHostDrop": tmnxNatL2AwSubStatUnknHostDrop,
       "tmnxNatL2AwSubBlkTable": tmnxNatL2AwSubBlkTable,
       "tmnxNatL2AwSubBlkEntry": tmnxNatL2AwSubBlkEntry,
       "tmnxNatL2AwSubBlkEnd": tmnxNatL2AwSubBlkEnd,
       "tmnxNatL2AwSubBlkPolicy": tmnxNatL2AwSubBlkPolicy,
       "tmnxNat64SubTable": tmnxNat64SubTable,
       "tmnxNat64SubEntry": tmnxNat64SubEntry,
       "tmnxNat64SubAddrType": tmnxNat64SubAddrType,
       "tmnxNat64SubAddr": tmnxNat64SubAddr,
       "tmnxNat64SubAddrPrefixLength": tmnxNat64SubAddrPrefixLength,
       "tmnxNat64SubId": tmnxNat64SubId,
       "tmnxNatLsnSubscIdStrTable": tmnxNatLsnSubscIdStrTable,
       "tmnxNatLsnSubscIdStrEntry": tmnxNatLsnSubscIdStrEntry,
       "tmnxNatLsnSubscIdStr": tmnxNatLsnSubscIdStr,
       "tmnxNatLsnSubscIdStrType": tmnxNatLsnSubscIdStrType,
       "tmnxNatLsnSubscIdStrAddrType": tmnxNatLsnSubscIdStrAddrType,
       "tmnxNatLsnSubscIdStrAddr": tmnxNatLsnSubscIdStrAddr,
       "tmnxNatLsnSubscIdStrTimeStamp": tmnxNatLsnSubscIdStrTimeStamp,
       "tmnxNatPrefixListTable": tmnxNatPrefixListTable,
       "tmnxNatPrefixListEntry": tmnxNatPrefixListEntry,
       "tmnxNatPrefixListName": tmnxNatPrefixListName,
       "tmnxNatPrefixListRowStatus": tmnxNatPrefixListRowStatus,
       "tmnxNatPrefixListLastMgmtChange": tmnxNatPrefixListLastMgmtChange,
       "tmnxNatPrefixListApplication": tmnxNatPrefixListApplication,
       "tmnxNatPrefixTable": tmnxNatPrefixTable,
       "tmnxNatPrefixEntry": tmnxNatPrefixEntry,
       "tmnxNatPrefixAddrType": tmnxNatPrefixAddrType,
       "tmnxNatPrefixAddr": tmnxNatPrefixAddr,
       "tmnxNatPrefixPrefixLen": tmnxNatPrefixPrefixLen,
       "tmnxNatPrefixRowStatus": tmnxNatPrefixRowStatus,
       "tmnxNatPrefixLastMgmtCh": tmnxNatPrefixLastMgmtCh,
       "tmnxNatPrefixNatPolicy": tmnxNatPrefixNatPolicy,
       "tmnxNatL2AwSubPlcyTable": tmnxNatL2AwSubPlcyTable,
       "tmnxNatL2AwSubPlcyEntry": tmnxNatL2AwSubPlcyEntry,
       "tmnxNatL2AwSubPlcy": tmnxNatL2AwSubPlcy,
       "tmnxNatL2AwSubPlcyOutVRtrID": tmnxNatL2AwSubPlcyOutVRtrID,
       "tmnxNatL2AwSubPlcyOutAddrType": tmnxNatL2AwSubPlcyOutAddrType,
       "tmnxNatL2AwSubPlcyOutAddr": tmnxNatL2AwSubPlcyOutAddr,
       "tmnxNatL2AwSubPlcyDnatOvrAddrTyp": tmnxNatL2AwSubPlcyDnatOvrAddrTyp,
       "tmnxNatL2AwSubPlcyDnatOvrAddr": tmnxNatL2AwSubPlcyDnatOvrAddr,
       "tmnxNatL2AwSubPlcyDnatDisable": tmnxNatL2AwSubPlcyDnatDisable,
       "tmnxNatL2AwSubPlcyPurpose": tmnxNatL2AwSubPlcyPurpose,
       "tmnxNatL2AwSubPlcyOutServiceId": tmnxNatL2AwSubPlcyOutServiceId,
       "tmnxNatL2AwHostPlcyTable": tmnxNatL2AwHostPlcyTable,
       "tmnxNatL2AwHostPlcyEntry": tmnxNatL2AwHostPlcyEntry,
       "tmnxNatL2AwHostPlcyAddrType": tmnxNatL2AwHostPlcyAddrType,
       "tmnxNatL2AwHostPlcyAddr": tmnxNatL2AwHostPlcyAddr,
       "tmnxNatL2AwHostPlcy": tmnxNatL2AwHostPlcy,
       "tmnxNatL2AwHostPlcyOutVRtrID": tmnxNatL2AwHostPlcyOutVRtrID,
       "tmnxNatL2AwHostPlcyOutAddrType": tmnxNatL2AwHostPlcyOutAddrType,
       "tmnxNatL2AwHostPlcyOutAddr": tmnxNatL2AwHostPlcyOutAddr,
       "tmnxNatL2AwHostPlcyOutStart": tmnxNatL2AwHostPlcyOutStart,
       "tmnxNatL2AwHostPlcyBypassActive": tmnxNatL2AwHostPlcyBypassActive,
       "tmnxNatL2AwHostPlcyVasFilter": tmnxNatL2AwHostPlcyVasFilter,
       "tmnxNatL2AwHostPlcyDNatOverride": tmnxNatL2AwHostPlcyDNatOverride,
       "tmnxNatL2AwHostPlcyDnatOvrAddrTp": tmnxNatL2AwHostPlcyDnatOvrAddrTp,
       "tmnxNatL2AwHostPlcyDnatOvrAddr": tmnxNatL2AwHostPlcyDnatOvrAddr,
       "tmnxNatSourcePrefixTable": tmnxNatSourcePrefixTable,
       "tmnxNatSourcePrefixEntry": tmnxNatSourcePrefixEntry,
       "tmnxNatSourcePrefixAddrType": tmnxNatSourcePrefixAddrType,
       "tmnxNatSourcePrefixAddr": tmnxNatSourcePrefixAddr,
       "tmnxNatSourcePrefixPrefixLen": tmnxNatSourcePrefixPrefixLen,
       "tmnxNatSourcePrefixRowStatus": tmnxNatSourcePrefixRowStatus,
       "tmnxNatSourcePrefixLastMgmtCh": tmnxNatSourcePrefixLastMgmtCh,
       "tmnxNatSourcePrefixNatPolicy": tmnxNatSourcePrefixNatPolicy,
       "tmnxNatMapObjs": tmnxNatMapObjs,
       "tmnxNatMapLsnHostTable": tmnxNatMapLsnHostTable,
       "tmnxNatMapLsnHostEntry": tmnxNatMapLsnHostEntry,
       "tmnxNatMapLsnHostAddrType": tmnxNatMapLsnHostAddrType,
       "tmnxNatMapLsnHostAddr": tmnxNatMapLsnHostAddr,
       "tmnxNatMapLsnHostRowStatus": tmnxNatMapLsnHostRowStatus,
       "tmnxNatMapLsnHostLastMgmtChange": tmnxNatMapLsnHostLastMgmtChange,
       "tmnxNatMapLsnHostAdminState": tmnxNatMapLsnHostAdminState,
       "tmnxNatMapLsnHostOutAddrType": tmnxNatMapLsnHostOutAddrType,
       "tmnxNatMapLsnHostOutAddr": tmnxNatMapLsnHostOutAddr,
       "tmnxNatMapLsnHostOutVRtrID": tmnxNatMapLsnHostOutVRtrID,
       "tmnxNatMapTable": tmnxNatMapTable,
       "tmnxNatMapEntry": tmnxNatMapEntry,
       "tmnxNatMapAddrType": tmnxNatMapAddrType,
       "tmnxNatMapAddr": tmnxNatMapAddr,
       "tmnxNatMapPort": tmnxNatMapPort,
       "tmnxNatMapProtocol": tmnxNatMapProtocol,
       "tmnxNatMapRowStatus": tmnxNatMapRowStatus,
       "tmnxNatMapLastMgmtChange": tmnxNatMapLastMgmtChange,
       "tmnxNatMapOutPort": tmnxNatMapOutPort,
       "tmnxNatFwdObjs": tmnxNatFwdObjs,
       "tmnxNatFwdAction": tmnxNatFwdAction,
       "tmnxNatFwdActionSubType": tmnxNatFwdActionSubType,
       "tmnxNatFwdActionVRtrId": tmnxNatFwdActionVRtrId,
       "tmnxNatFwdActionAddrType": tmnxNatFwdActionAddrType,
       "tmnxNatFwdActionAddr": tmnxNatFwdActionAddr,
       "tmnxNatFwdActionB4Addr": tmnxNatFwdActionB4Addr,
       "tmnxNatFwdActionAftrAddr": tmnxNatFwdActionAftrAddr,
       "tmnxNatFwdActionL2awSubscriberId": tmnxNatFwdActionL2awSubscriberId,
       "tmnxNatFwdActionProtocol": tmnxNatFwdActionProtocol,
       "tmnxNatFwdActionTimeOut": tmnxNatFwdActionTimeOut,
       "tmnxNatFwdActionPort": tmnxNatFwdActionPort,
       "tmnxNatFwdActionOutPort": tmnxNatFwdActionOutPort,
       "tmnxNatFwdActionOutAddr": tmnxNatFwdActionOutAddr,
       "tmnxNatFwdActionType": tmnxNatFwdActionType,
       "tmnxNatFwdActionGo": tmnxNatFwdActionGo,
       "tmnxNatFwdActionSuccessful": tmnxNatFwdActionSuccessful,
       "tmnxNatFwdActionTime": tmnxNatFwdActionTime,
       "tmnxNatFwdActionDescription": tmnxNatFwdActionDescription,
       "tmnxNatFwdActionNatPolicy": tmnxNatFwdActionNatPolicy,
       "tmnxNatFwdActionSaveConfig": tmnxNatFwdActionSaveConfig,
       "tmnxNatFwdActionSpfForce": tmnxNatFwdActionSpfForce,
       "tmnxNatFwdActionAddrCpm": tmnxNatFwdActionAddrCpm,
       "tmnxNatFwdActionOutPublicIf": tmnxNatFwdActionOutPublicIf,
       "tmnxNatFwdTable": tmnxNatFwdTable,
       "tmnxNatFwdEntry": tmnxNatFwdEntry,
       "tmnxNatFwdSubType": tmnxNatFwdSubType,
       "tmnxNatFwdL2awSubIdent": tmnxNatFwdL2awSubIdent,
       "tmnxNatFwdLsnVRtrID": tmnxNatFwdLsnVRtrID,
       "tmnxNatFwdLsnB4AddrType": tmnxNatFwdLsnB4AddrType,
       "tmnxNatFwdLsnB4Addr": tmnxNatFwdLsnB4Addr,
       "tmnxNatFwdAddrType": tmnxNatFwdAddrType,
       "tmnxNatFwdAddr": tmnxNatFwdAddr,
       "tmnxNatFwdProtocol": tmnxNatFwdProtocol,
       "tmnxNatFwdPort": tmnxNatFwdPort,
       "tmnxNatFwdOutVRtrID": tmnxNatFwdOutVRtrID,
       "tmnxNatFwdOutAddrType": tmnxNatFwdOutAddrType,
       "tmnxNatFwdOutAddr": tmnxNatFwdOutAddr,
       "tmnxNatFwdOutPort": tmnxNatFwdOutPort,
       "tmnxNatFwdExpiryDateAndTime": tmnxNatFwdExpiryDateAndTime,
       "tmnxNatFwdLsnAftrAddrType": tmnxNatFwdLsnAftrAddrType,
       "tmnxNatFwdLsnAftrAddr": tmnxNatFwdLsnAftrAddr,
       "tmnxNatFwdPersistKey": tmnxNatFwdPersistKey,
       "tmnxNatFwdDescription": tmnxNatFwdDescription,
       "tmnxNatFwdOrigin": tmnxNatFwdOrigin,
       "tmnxNatFwd2Table": tmnxNatFwd2Table,
       "tmnxNatFwd2Entry": tmnxNatFwd2Entry,
       "tmnxNatFwd2SubType": tmnxNatFwd2SubType,
       "tmnxNatFwd2L2awSubIdent": tmnxNatFwd2L2awSubIdent,
       "tmnxNatFwd2LsnVRtrID": tmnxNatFwd2LsnVRtrID,
       "tmnxNatFwd2LsnB4AddrType": tmnxNatFwd2LsnB4AddrType,
       "tmnxNatFwd2LsnB4Addr": tmnxNatFwd2LsnB4Addr,
       "tmnxNatFwd2AddrType": tmnxNatFwd2AddrType,
       "tmnxNatFwd2Addr": tmnxNatFwd2Addr,
       "tmnxNatFwd2Protocol": tmnxNatFwd2Protocol,
       "tmnxNatFwd2Port": tmnxNatFwd2Port,
       "tmnxNatFwd2NatPolicy": tmnxNatFwd2NatPolicy,
       "tmnxNatFwd2OutVRtrID": tmnxNatFwd2OutVRtrID,
       "tmnxNatFwd2OutAddrType": tmnxNatFwd2OutAddrType,
       "tmnxNatFwd2OutAddr": tmnxNatFwd2OutAddr,
       "tmnxNatFwd2OutPort": tmnxNatFwd2OutPort,
       "tmnxNatFwd2ExpiryDateAndTime": tmnxNatFwd2ExpiryDateAndTime,
       "tmnxNatFwd2LsnAftrAddrType": tmnxNatFwd2LsnAftrAddrType,
       "tmnxNatFwd2LsnAftrAddr": tmnxNatFwd2LsnAftrAddr,
       "tmnxNatFwd2PersistKey": tmnxNatFwd2PersistKey,
       "tmnxNatFwd2Description": tmnxNatFwd2Description,
       "tmnxNatFwd2Origin": tmnxNatFwd2Origin,
       "tmnxNatFwd2ProtocolVersion": tmnxNatFwd2ProtocolVersion,
       "tmnxNatFwd2MappingNumber": tmnxNatFwd2MappingNumber,
       "tmnxNatFwd2OperState": tmnxNatFwd2OperState,
       "tmnxNatFwd2Persistence": tmnxNatFwd2Persistence,
       "tmnxNatFwd2ForeignPfxType": tmnxNatFwd2ForeignPfxType,
       "tmnxNatFwd2ForeignPfx": tmnxNatFwd2ForeignPfx,
       "tmnxNatFwd2ForeignPfxLength": tmnxNatFwd2ForeignPfxLength,
       "tmnxNatFwd2ForeignPort": tmnxNatFwd2ForeignPort,
       "tmnxNatFwd2OutService": tmnxNatFwd2OutService,
       "tmnxNatFwd2AddrCpm": tmnxNatFwd2AddrCpm,
       "tmnxNatFwd2OutPublicIf": tmnxNatFwd2OutPublicIf,
       "tmnxNatFwdL2AwTable": tmnxNatFwdL2AwTable,
       "tmnxNatFwdL2AwEntry": tmnxNatFwdL2AwEntry,
       "tmnxNatFwdL2AwSubIdent": tmnxNatFwdL2AwSubIdent,
       "tmnxNatFwdL2AwAddrType": tmnxNatFwdL2AwAddrType,
       "tmnxNatFwdL2AwAddr": tmnxNatFwdL2AwAddr,
       "tmnxNatFwdL2AwNatPolicy": tmnxNatFwdL2AwNatPolicy,
       "tmnxNatFwdL2AwProtocol": tmnxNatFwdL2AwProtocol,
       "tmnxNatFwdL2AwPort": tmnxNatFwdL2AwPort,
       "tmnxNatFwdL2AwOutVRtrID": tmnxNatFwdL2AwOutVRtrID,
       "tmnxNatFwdL2AwOutAddrType": tmnxNatFwdL2AwOutAddrType,
       "tmnxNatFwdL2AwOutAddr": tmnxNatFwdL2AwOutAddr,
       "tmnxNatFwdL2AwOutPort": tmnxNatFwdL2AwOutPort,
       "tmnxNatFwdL2AwExpiryDateAndTime": tmnxNatFwdL2AwExpiryDateAndTime,
       "tmnxNatFwdL2AwPersistKey": tmnxNatFwdL2AwPersistKey,
       "tmnxNatFwdL2AwOrigin": tmnxNatFwdL2AwOrigin,
       "tmnxNatFwdL2AwOperState": tmnxNatFwdL2AwOperState,
       "tmnxNatFwdL2AwPersistence": tmnxNatFwdL2AwPersistence,
       "tmnxNatFwdL2AwOutService": tmnxNatFwdL2AwOutService,
       "tmnxNatAccObjs": tmnxNatAccObjs,
       "tmnxNatApTable": tmnxNatApTable,
       "tmnxNatApEntry": tmnxNatApEntry,
       "tmnxNatApName": tmnxNatApName,
       "tmnxNatApLastMgmtChange": tmnxNatApLastMgmtChange,
       "tmnxNatApRowStatus": tmnxNatApRowStatus,
       "tmnxNatApDescription": tmnxNatApDescription,
       "tmnxNatApIncludeAttributes": tmnxNatApIncludeAttributes,
       "tmnxNatApServersTimeout": tmnxNatApServersTimeout,
       "tmnxNatApServersRetry": tmnxNatApServersRetry,
       "tmnxNatApServersVRtrID": tmnxNatApServersVRtrID,
       "tmnxNatApServersSrcAddrType": tmnxNatApServersSrcAddrType,
       "tmnxNatApServersSrcAddrStart": tmnxNatApServersSrcAddrStart,
       "tmnxNatApServersSrcAddrEnd": tmnxNatApServersSrcAddrEnd,
       "tmnxNatApServersAlgorithm": tmnxNatApServersAlgorithm,
       "tmnxNatApServTable": tmnxNatApServTable,
       "tmnxNatApServEntry": tmnxNatApServEntry,
       "tmnxNatApServIndex": tmnxNatApServIndex,
       "tmnxNatApServRowStatus": tmnxNatApServRowStatus,
       "tmnxNatApServLastMgmtChange": tmnxNatApServLastMgmtChange,
       "tmnxNatApServAddrType": tmnxNatApServAddrType,
       "tmnxNatApServAddr": tmnxNatApServAddr,
       "tmnxNatApServSecret": tmnxNatApServSecret,
       "tmnxNatApServAcctPort": tmnxNatApServAcctPort,
       "tmnxNatApServStatTable": tmnxNatApServStatTable,
       "tmnxNatApServStatEntry": tmnxNatApServStatEntry,
       "tmnxNatApServStatSrcAddrType": tmnxNatApServStatSrcAddrType,
       "tmnxNatApServStatSrcAddr": tmnxNatApServStatSrcAddr,
       "tmnxNatApServStatOperState": tmnxNatApServStatOperState,
       "tmnxNatApServStatTxRequests": tmnxNatApServStatTxRequests,
       "tmnxNatApServStatReqTimeout": tmnxNatApServStatReqTimeout,
       "tmnxNatApServStatSendRetries": tmnxNatApServStatSendRetries,
       "tmnxNatPcpObjs": tmnxNatPcpObjs,
       "tmnxNatPcpPlcyTable": tmnxNatPcpPlcyTable,
       "tmnxNatPcpPlcyEntry": tmnxNatPcpPlcyEntry,
       "tmnxNatPcpPlcyName": tmnxNatPcpPlcyName,
       "tmnxNatPcpPlcyLastMgmtChange": tmnxNatPcpPlcyLastMgmtChange,
       "tmnxNatPcpPlcyRowStatus": tmnxNatPcpPlcyRowStatus,
       "tmnxNatPcpPlcyDescription": tmnxNatPcpPlcyDescription,
       "tmnxNatPcpPlcyOpcodes": tmnxNatPcpPlcyOpcodes,
       "tmnxNatPcpPlcyOptions": tmnxNatPcpPlcyOptions,
       "tmnxNatPcpPlcyMinimumLifetime": tmnxNatPcpPlcyMinimumLifetime,
       "tmnxNatPcpPlcyMaximumLifetime": tmnxNatPcpPlcyMaximumLifetime,
       "tmnxNatPcpPlcyMaxDescriptionLen": tmnxNatPcpPlcyMaxDescriptionLen,
       "tmnxNatPcpPlcyMinimumVersion": tmnxNatPcpPlcyMinimumVersion,
       "tmnxNatPcpPlcyMaximumVersion": tmnxNatPcpPlcyMaximumVersion,
       "tmnxNatPcpPlcyReuseExtIp": tmnxNatPcpPlcyReuseExtIp,
       "tmnxNatPcpSrvTable": tmnxNatPcpSrvTable,
       "tmnxNatPcpSrvEntry": tmnxNatPcpSrvEntry,
       "tmnxNatPcpSrvName": tmnxNatPcpSrvName,
       "tmnxNatPcpSrvLastCh": tmnxNatPcpSrvLastCh,
       "tmnxNatPcpSrvRowStatus": tmnxNatPcpSrvRowStatus,
       "tmnxNatPcpSrvAdminState": tmnxNatPcpSrvAdminState,
       "tmnxNatPcpSrvDescription": tmnxNatPcpSrvDescription,
       "tmnxNatPcpSrvPlcy": tmnxNatPcpSrvPlcy,
       "tmnxNatPcpSrvFwdInsideRouter": tmnxNatPcpSrvFwdInsideRouter,
       "tmnxNatPcpSrvDsliteAftrAddr": tmnxNatPcpSrvDsliteAftrAddr,
       "tmnxNatPcpSrvState": tmnxNatPcpSrvState,
       "tmnxNatPcpSrvStateDescription": tmnxNatPcpSrvStateDescription,
       "tmnxNatPcpSrvEpoch": tmnxNatPcpSrvEpoch,
       "tmnxNatPcpSrvIfTable": tmnxNatPcpSrvIfTable,
       "tmnxNatPcpSrvIfEntry": tmnxNatPcpSrvIfEntry,
       "tmnxNatPcpSrvIfRowStatus": tmnxNatPcpSrvIfRowStatus,
       "tmnxNatPcpSrvIfLastCh": tmnxNatPcpSrvIfLastCh,
       "tmnxNatPcpSrvIfStatsTable": tmnxNatPcpSrvIfStatsTable,
       "tmnxNatPcpSrvIfStatsEntry": tmnxNatPcpSrvIfStatsEntry,
       "tmnxNatPcpSrvIfStatsType": tmnxNatPcpSrvIfStatsType,
       "tmnxNatPcpSrvIfStatsName": tmnxNatPcpSrvIfStatsName,
       "tmnxNatPcpSrvIfStatsValLw": tmnxNatPcpSrvIfStatsValLw,
       "tmnxNatPcpSrvIfStatsValHw": tmnxNatPcpSrvIfStatsValHw,
       "tmnxNatPcpSrvIfStatsVal": tmnxNatPcpSrvIfStatsVal,
       "tmnxNatSubscIdObjs": tmnxNatSubscIdObjs,
       "tmnxNatSubscIdVendorTable": tmnxNatSubscIdVendorTable,
       "tmnxNatSubscIdVendorEntry": tmnxNatSubscIdVendorEntry,
       "tmnxNatSubscIdVendorId": tmnxNatSubscIdVendorId,
       "tmnxNatSubscIdVendorStr": tmnxNatSubscIdVendorStr,
       "tmnxNatSubscIdVendorDescription": tmnxNatSubscIdVendorDescription,
       "tmnxNatSubscIdAttrTable": tmnxNatSubscIdAttrTable,
       "tmnxNatSubscIdAttrEntry": tmnxNatSubscIdAttrEntry,
       "tmnxNatSubscIdAttrType": tmnxNatSubscIdAttrType,
       "tmnxNatSubscIdAttrStr": tmnxNatSubscIdAttrStr,
       "tmnxNatSubscIdAttrDescription": tmnxNatSubscIdAttrDescription,
       "tmnxNatDetScriptObjs": tmnxNatDetScriptObjs,
       "tmnxNatDetScriptLocation": tmnxNatDetScriptLocation,
       "tmnxNatDetScriptSaveNeeded": tmnxNatDetScriptSaveNeeded,
       "tmnxNatDetScriptSave": tmnxNatDetScriptSave,
       "tmnxNatDetScriptSaveResult": tmnxNatDetScriptSaveResult,
       "tmnxNatDetScriptSaveTime": tmnxNatDetScriptSaveTime,
       "tmnxNatQryObjs": tmnxNatQryObjs,
       "tmnxNatQryLsnSubObjs": tmnxNatQryLsnSubObjs,
       "tmnxNatQryLsnSubNextQryId": tmnxNatQryLsnSubNextQryId,
       "tmnxNatQryLsnSubTable": tmnxNatQryLsnSubTable,
       "tmnxNatQryLsnSubEntry": tmnxNatQryLsnSubEntry,
       "tmnxNatQryLsnSubQryId": tmnxNatQryLsnSubQryId,
       "tmnxNatQryLsnSubRowStatus": tmnxNatQryLsnSubRowStatus,
       "tmnxNatQryLsnSubResultType": tmnxNatQryLsnSubResultType,
       "tmnxNatQryLsnSubWhereNatPolicy": tmnxNatQryLsnSubWhereNatPolicy,
       "tmnxNatQryLsnSubWhereIsaGrp": tmnxNatQryLsnSubWhereIsaGrp,
       "tmnxNatQryLsnSubWhereMemberId": tmnxNatQryLsnSubWhereMemberId,
       "tmnxNatQryLsnSubWhereOutRouter": tmnxNatQryLsnSubWhereOutRouter,
       "tmnxNatQryLsnSubWhereOutAddrType": tmnxNatQryLsnSubWhereOutAddrType,
       "tmnxNatQryLsnSubWhereOutAddr": tmnxNatQryLsnSubWhereOutAddr,
       "tmnxNatQryLsnSubWhereInSubType": tmnxNatQryLsnSubWhereInSubType,
       "tmnxNatQryLsnSubWhereInRouter": tmnxNatQryLsnSubWhereInRouter,
       "tmnxNatQryLsnSubWhereInAddrType": tmnxNatQryLsnSubWhereInAddrType,
       "tmnxNatQryLsnSubWhereInAddr": tmnxNatQryLsnSubWhereInAddr,
       "tmnxNatQryLsnSubWhereInAddrPfxL": tmnxNatQryLsnSubWhereInAddrPfxL,
       "tmnxNatQryLsnSubWhereSubId": tmnxNatQryLsnSubWhereSubId,
       "tmnxNatQryLsnSubResTable": tmnxNatQryLsnSubResTable,
       "tmnxNatQryLsnSubResEntry": tmnxNatQryLsnSubResEntry,
       "tmnxNatQryLsnSubResId": tmnxNatQryLsnSubResId,
       "tmnxNatQryLsnSubResPolicy": tmnxNatQryLsnSubResPolicy,
       "tmnxNatQryLsnSubResIsaGrp": tmnxNatQryLsnSubResIsaGrp,
       "tmnxNatQryLsnSubResIsaMemberId": tmnxNatQryLsnSubResIsaMemberId,
       "tmnxNatQryLsnSubResOutVRtrID": tmnxNatQryLsnSubResOutVRtrID,
       "tmnxNatQryLsnSubResOutAddrType": tmnxNatQryLsnSubResOutAddrType,
       "tmnxNatQryLsnSubResOutAddr": tmnxNatQryLsnSubResOutAddr,
       "tmnxNatQryLsnSubResIdStr": tmnxNatQryLsnSubResIdStr,
       "tmnxNatQryLsnSubResInSubType": tmnxNatQryLsnSubResInSubType,
       "tmnxNatQryLsnSubResInRouter": tmnxNatQryLsnSubResInRouter,
       "tmnxNatQryLsnSubResInAddrType": tmnxNatQryLsnSubResInAddrType,
       "tmnxNatQryLsnSubResInAddr": tmnxNatQryLsnSubResInAddr,
       "tmnxNatQryLsnSubResInAddrPfxL": tmnxNatQryLsnSubResInAddrPfxL,
       "tmnxNatQryLsnSubResIcmpPortUsg": tmnxNatQryLsnSubResIcmpPortUsg,
       "tmnxNatQryLsnSubResIcmpPortUsgHi": tmnxNatQryLsnSubResIcmpPortUsgHi,
       "tmnxNatQryLsnSubResUdpPortUsg": tmnxNatQryLsnSubResUdpPortUsg,
       "tmnxNatQryLsnSubResUdpPortUsgHi": tmnxNatQryLsnSubResUdpPortUsgHi,
       "tmnxNatQryLsnSubResTcpPortUsg": tmnxNatQryLsnSubResTcpPortUsg,
       "tmnxNatQryLsnSubResTcpPortUsgHi": tmnxNatQryLsnSubResTcpPortUsgHi,
       "tmnxNatQryLsnSubResSessionUsg": tmnxNatQryLsnSubResSessionUsg,
       "tmnxNatQryLsnSubResSessionUsgHi": tmnxNatQryLsnSubResSessionUsgHi,
       "tmnxNatQryLsnSubResSessions": tmnxNatQryLsnSubResSessions,
       "tmnxNatQryLsnSubResSessionsPrio": tmnxNatQryLsnSubResSessionsPrio,
       "tmnxNatQryLsnSubResSessionsPeak": tmnxNatQryLsnSubResSessionsPeak,
       "tmnxNatLsnSubPlcyOutIpAddrTable": tmnxNatLsnSubPlcyOutIpAddrTable,
       "tmnxNatLsnSubPlcyOutIpAddrEntry": tmnxNatLsnSubPlcyOutIpAddrEntry,
       "tmnxNatLsnSubPlcyOutIpAddrSubId": tmnxNatLsnSubPlcyOutIpAddrSubId,
       "tmnxNatLsnSubPlcyOutIpAddrPolicy": tmnxNatLsnSubPlcyOutIpAddrPolicy,
       "tmnxNatLsnSubPlcyOutIpAddrType": tmnxNatLsnSubPlcyOutIpAddrType,
       "tmnxNatLsnSubPlcyOutIpAddr": tmnxNatLsnSubPlcyOutIpAddr,
       "tmnxNatLsnSubPlcyOutIpAddrOutVR": tmnxNatLsnSubPlcyOutIpAddrOutVR,
       "tmnxNatLsnSubPlcyOutIpBlkTable": tmnxNatLsnSubPlcyOutIpBlkTable,
       "tmnxNatLsnSubPlcyOutIpBlkEntry": tmnxNatLsnSubPlcyOutIpBlkEntry,
       "tmnxNatLsnSubPlcyOutIpBlkSubId": tmnxNatLsnSubPlcyOutIpBlkSubId,
       "tmnxNatLsnSubPlcyOutIpBlkPolicy": tmnxNatLsnSubPlcyOutIpBlkPolicy,
       "tmnxNatLsnSubPlcyOutIpBlkIpType": tmnxNatLsnSubPlcyOutIpBlkIpType,
       "tmnxNatLsnSubPlcyOutIpBlkIp": tmnxNatLsnSubPlcyOutIpBlkIp,
       "tmnxNatLsnSubPlcyOutIpBlkStart": tmnxNatLsnSubPlcyOutIpBlkStart,
       "tmnxNatLsnSubPlcyOutIpBlkEnd": tmnxNatLsnSubPlcyOutIpBlkEnd,
       "tmnxNatUpnpObjs": tmnxNatUpnpObjs,
       "tmnxNatUpnpPlcyTable": tmnxNatUpnpPlcyTable,
       "tmnxNatUpnpPlcyEntry": tmnxNatUpnpPlcyEntry,
       "tmnxNatUpnpPlcyName": tmnxNatUpnpPlcyName,
       "tmnxNatUpnpPlcyRowStatus": tmnxNatUpnpPlcyRowStatus,
       "tmnxNatUpnpPlcyLastMgmtChange": tmnxNatUpnpPlcyLastMgmtChange,
       "tmnxNatUpnpPlcyDescription": tmnxNatUpnpPlcyDescription,
       "tmnxNatUpnpPlcyMappingLimit": tmnxNatUpnpPlcyMappingLimit,
       "tmnxNatUpnpPlcyStrictMode": tmnxNatUpnpPlcyStrictMode,
       "tmnxNatUpnpPlcyListeningPort": tmnxNatUpnpPlcyListeningPort,
       "tmnxNatUpnpPlcyStatsTable": tmnxNatUpnpPlcyStatsTable,
       "tmnxNatUpnpPlcyStatsEntry": tmnxNatUpnpPlcyStatsEntry,
       "tmnxNatUpnpPlcyStatsId": tmnxNatUpnpPlcyStatsId,
       "tmnxNatUpnpPlcyStatsName": tmnxNatUpnpPlcyStatsName,
       "tmnxNatUpnpPlcyStatsVal": tmnxNatUpnpPlcyStatsVal,
       "tmnxNatUpnpPlcyStatTable": tmnxNatUpnpPlcyStatTable,
       "tmnxNatUpnpPlcyStatEntry": tmnxNatUpnpPlcyStatEntry,
       "tmnxNatUpnpPlcyStatActMappings": tmnxNatUpnpPlcyStatActMappings,
       "tmnxNatUpnpPlcyStatSubscrMapped": tmnxNatUpnpPlcyStatSubscrMapped,
       "tmnxNatUpnpPlcyStatSubscr": tmnxNatUpnpPlcyStatSubscr,
       "tmnxNatClassifierObjs": tmnxNatClassifierObjs,
       "tmnxNatClsfrTable": tmnxNatClsfrTable,
       "tmnxNatClsfrEntry": tmnxNatClsfrEntry,
       "tmnxNatClsfrName": tmnxNatClsfrName,
       "tmnxNatClsfrRowStatus": tmnxNatClsfrRowStatus,
       "tmnxNatClsfrLastCh": tmnxNatClsfrLastCh,
       "tmnxNatClsfrDescription": tmnxNatClsfrDescription,
       "tmnxNatClsfrDefaultAction": tmnxNatClsfrDefaultAction,
       "tmnxNatClsfrDefaultActionAddrTyp": tmnxNatClsfrDefaultActionAddrTyp,
       "tmnxNatClsfrDefaultActionAddr": tmnxNatClsfrDefaultActionAddr,
       "tmnxNatClsfrDefaultDnatAddrType": tmnxNatClsfrDefaultDnatAddrType,
       "tmnxNatClsfrDefaultDnatAddr": tmnxNatClsfrDefaultDnatAddr,
       "tmnxNatClsfrN3Table": tmnxNatClsfrN3Table,
       "tmnxNatClsfrN3Entry": tmnxNatClsfrN3Entry,
       "tmnxNatClsfrN3Index": tmnxNatClsfrN3Index,
       "tmnxNatClsfrN3RowStatus": tmnxNatClsfrN3RowStatus,
       "tmnxNatClsfrN3LastCh": tmnxNatClsfrN3LastCh,
       "tmnxNatClsfrN3Description": tmnxNatClsfrN3Description,
       "tmnxNatClsfrN3Action": tmnxNatClsfrN3Action,
       "tmnxNatClsfrN3DnatAddrType": tmnxNatClsfrN3DnatAddrType,
       "tmnxNatClsfrN3DnatAddr": tmnxNatClsfrN3DnatAddr,
       "tmnxNatClsfrN3Protocol": tmnxNatClsfrN3Protocol,
       "tmnxNatClsfrN3DestPortStart": tmnxNatClsfrN3DestPortStart,
       "tmnxNatClsfrN3DestPortEnd": tmnxNatClsfrN3DestPortEnd,
       "tmnxNatClsfrN3ForeignAddrType": tmnxNatClsfrN3ForeignAddrType,
       "tmnxNatClsfrN3ForeignAddr": tmnxNatClsfrN3ForeignAddr,
       "tmnxNatMappingObjs": tmnxNatMappingObjs,
       "tmnxNatMapDomTable": tmnxNatMapDomTable,
       "tmnxNatMapDomEntry": tmnxNatMapDomEntry,
       "tmnxNatMapDomName": tmnxNatMapDomName,
       "tmnxNatMapDomRowStatus": tmnxNatMapDomRowStatus,
       "tmnxNatMapDomLastCh": tmnxNatMapDomLastCh,
       "tmnxNatMapDomAdminState": tmnxNatMapDomAdminState,
       "tmnxNatMapDomDescription": tmnxNatMapDomDescription,
       "tmnxNatMapDomDmrPrefixType": tmnxNatMapDomDmrPrefixType,
       "tmnxNatMapDomDmrPrefix": tmnxNatMapDomDmrPrefix,
       "tmnxNatMapDomDmrPrefixLength": tmnxNatMapDomDmrPrefixLength,
       "tmnxNatMapDomTcpMssAdjust": tmnxNatMapDomTcpMssAdjust,
       "tmnxNatMapDomMtu": tmnxNatMapDomMtu,
       "tmnxNatMapDomIpFragmentation": tmnxNatMapDomIpFragmentation,
       "tmnxNatMapDomRouter": tmnxNatMapDomRouter,
       "tmnxNatMapDomMapTGrpId": tmnxNatMapDomMapTGrpId,
       "tmnxNatMapDomMapTFpeId": tmnxNatMapDomMapTFpeId,
       "tmnxNatMapDomUdpV6ChksumRecalc": tmnxNatMapDomUdpV6ChksumRecalc,
       "tmnxNatMapRuleTable": tmnxNatMapRuleTable,
       "tmnxNatMapRuleEntry": tmnxNatMapRuleEntry,
       "tmnxNatMapRuleName": tmnxNatMapRuleName,
       "tmnxNatMapRuleRowStatus": tmnxNatMapRuleRowStatus,
       "tmnxNatMapRuleLastCh": tmnxNatMapRuleLastCh,
       "tmnxNatMapRuleAdminState": tmnxNatMapRuleAdminState,
       "tmnxNatMapRuleDescription": tmnxNatMapRuleDescription,
       "tmnxNatMapRulePrefixType": tmnxNatMapRulePrefixType,
       "tmnxNatMapRulePrefix": tmnxNatMapRulePrefix,
       "tmnxNatMapRulePrefixLength": tmnxNatMapRulePrefixLength,
       "tmnxNatMapRuleIpv4PrefixType": tmnxNatMapRuleIpv4PrefixType,
       "tmnxNatMapRuleIpv4Prefix": tmnxNatMapRuleIpv4Prefix,
       "tmnxNatMapRuleIpv4PrefixLength": tmnxNatMapRuleIpv4PrefixLength,
       "tmnxNatMapRuleEaLength": tmnxNatMapRuleEaLength,
       "tmnxNatMapRulePsidOffset": tmnxNatMapRulePsidOffset,
       "tmnxNatMapRuleAddrSharingRatio": tmnxNatMapRuleAddrSharingRatio,
       "tmnxNatMapRuleExcludedPorts": tmnxNatMapRuleExcludedPorts,
       "tmnxNatMapRulePortsPerUser": tmnxNatMapRulePortsPerUser,
       "tmnxNatMapRuleStatsCollection": tmnxNatMapRuleStatsCollection,
       "tmnxNatMapVrtrDomTable": tmnxNatMapVrtrDomTable,
       "tmnxNatMapVrtrDomEntry": tmnxNatMapVrtrDomEntry,
       "tmnxNatMapVrtrDomRowStatus": tmnxNatMapVrtrDomRowStatus,
       "tmnxNatMapVrtrDomLastCh": tmnxNatMapVrtrDomLastCh,
       "tmnxNatMapDomStatsTable": tmnxNatMapDomStatsTable,
       "tmnxNatMapDomStatsEntry": tmnxNatMapDomStatsEntry,
       "tmnxNatMapDomUpFwdPackets": tmnxNatMapDomUpFwdPackets,
       "tmnxNatMapDomUpFwdOctets": tmnxNatMapDomUpFwdOctets,
       "tmnxNatMapDomUpDropPackets": tmnxNatMapDomUpDropPackets,
       "tmnxNatMapDomUpDropOctets": tmnxNatMapDomUpDropOctets,
       "tmnxNatMapDomDownFwdPackets": tmnxNatMapDomDownFwdPackets,
       "tmnxNatMapDomDownFwdOctets": tmnxNatMapDomDownFwdOctets,
       "tmnxNatMapDomDownDropPackets": tmnxNatMapDomDownDropPackets,
       "tmnxNatMapDomDownDropOctets": tmnxNatMapDomDownDropOctets,
       "tmnxNatMapDomUpDropAntiSpoof": tmnxNatMapDomUpDropAntiSpoof,
       "tmnxNatMapDomUpDropIcmp6": tmnxNatMapDomUpDropIcmp6,
       "tmnxNatMapDomUpDropOther": tmnxNatMapDomUpDropOther,
       "tmnxNatMapDomUpFragRx": tmnxNatMapDomUpFragRx,
       "tmnxNatMapDomUpIcmp6NodeInfoRx": tmnxNatMapDomUpIcmp6NodeInfoRx,
       "tmnxNatMapDomUpCpeIcmp6ErrRepRx": tmnxNatMapDomUpCpeIcmp6ErrRepRx,
       "tmnxNatMapDomUpImIcmp6ErrRx": tmnxNatMapDomUpImIcmp6ErrRx,
       "tmnxNatMapDomDownDropUnkPro": tmnxNatMapDomDownDropUnkPro,
       "tmnxNatMapDomDownDropFragReq": tmnxNatMapDomDownDropFragReq,
       "tmnxNatMapDomDownDropIcmp4": tmnxNatMapDomDownDropIcmp4,
       "tmnxNatMapDomDownFragRx": tmnxNatMapDomDownFragRx,
       "tmnxNatMapDomDownFragReq": tmnxNatMapDomDownFragReq,
       "tmnxNatMapDomDownIcmp4ErrRepRx": tmnxNatMapDomDownIcmp4ErrRepRx,
       "tmnxNatMapDomDownIcmp4EchoRx": tmnxNatMapDomDownIcmp4EchoRx,
       "tmnxNatMapDomUpDropUnkProto": tmnxNatMapDomUpDropUnkProto,
       "tmnxNatMapFragStatsTable": tmnxNatMapFragStatsTable,
       "tmnxNatMapFragStatsEntry": tmnxNatMapFragStatsEntry,
       "tmnxNatMapFragStatsId": tmnxNatMapFragStatsId,
       "tmnxNatMapFragStatsName": tmnxNatMapFragStatsName,
       "tmnxNatMapFragStatsVal": tmnxNatMapFragStatsVal,
       "tmnxNatMapRuleStatsTable": tmnxNatMapRuleStatsTable,
       "tmnxNatMapRuleStatsEntry": tmnxNatMapRuleStatsEntry,
       "tmnxNatMapRuleUpFwdPackets": tmnxNatMapRuleUpFwdPackets,
       "tmnxNatMapRuleUpFwdOctets": tmnxNatMapRuleUpFwdOctets,
       "tmnxNatMapRuleUpDropPackets": tmnxNatMapRuleUpDropPackets,
       "tmnxNatMapRuleUpDropOctets": tmnxNatMapRuleUpDropOctets,
       "tmnxNatMapRuleDownFwdPackets": tmnxNatMapRuleDownFwdPackets,
       "tmnxNatMapRuleDownFwdOctets": tmnxNatMapRuleDownFwdOctets,
       "tmnxNatMapRuleDownDropPackets": tmnxNatMapRuleDownDropPackets,
       "tmnxNatMapRuleDownDropOctets": tmnxNatMapRuleDownDropOctets,
       "tmnxNatMapRuleUpDropAntiSpoof": tmnxNatMapRuleUpDropAntiSpoof,
       "tmnxNatMapRuleUpDropIcmp6": tmnxNatMapRuleUpDropIcmp6,
       "tmnxNatMapRuleUpDropOther": tmnxNatMapRuleUpDropOther,
       "tmnxNatMapRuleUpFragRx": tmnxNatMapRuleUpFragRx,
       "tmnxNatMapRuleUpIcmp6NodeInfoRx": tmnxNatMapRuleUpIcmp6NodeInfoRx,
       "tmnxNatMapRuleUpCpeIcmp6ErrRepRx": tmnxNatMapRuleUpCpeIcmp6ErrRepRx,
       "tmnxNatMapRuleUpImIcmp6ErrRx": tmnxNatMapRuleUpImIcmp6ErrRx,
       "tmnxNatMapRuleDownDropUnkPro": tmnxNatMapRuleDownDropUnkPro,
       "tmnxNatMapRuleDownDropFragReq": tmnxNatMapRuleDownDropFragReq,
       "tmnxNatMapRuleDownDropIcmp4": tmnxNatMapRuleDownDropIcmp4,
       "tmnxNatMapRuleDownFragRx": tmnxNatMapRuleDownFragRx,
       "tmnxNatMapRuleDownFragReq": tmnxNatMapRuleDownFragReq,
       "tmnxNatMapRuleDownIcmp4ErrRepRx": tmnxNatMapRuleDownIcmp4ErrRepRx,
       "tmnxNatMapRuleDownIcmp4EchoRx": tmnxNatMapRuleDownIcmp4EchoRx,
       "tmnxNatMapRuleUpDropUnkProto": tmnxNatMapRuleUpDropUnkProto,
       "tmnxMapTDomVappStatsTable": tmnxMapTDomVappStatsTable,
       "tmnxMapTDomVappStatsEntry": tmnxMapTDomVappStatsEntry,
       "tmnxMapTDomVappUpFwdPackets": tmnxMapTDomVappUpFwdPackets,
       "tmnxMapTDomVappUpFwdOctets": tmnxMapTDomVappUpFwdOctets,
       "tmnxMapTDomVappUpDropPackets": tmnxMapTDomVappUpDropPackets,
       "tmnxMapTDomVappUpDropOctets": tmnxMapTDomVappUpDropOctets,
       "tmnxMapTDomVappUpDropAntiSpoof": tmnxMapTDomVappUpDropAntiSpoof,
       "tmnxMapTDomVappUpDropIcmp6": tmnxMapTDomVappUpDropIcmp6,
       "tmnxMapTDomVappUpDropUnkProto": tmnxMapTDomVappUpDropUnkProto,
       "tmnxMapTDomVappUpFragRx": tmnxMapTDomVappUpFragRx,
       "tmnxMapTDomVappUpIcmp6EchoRx": tmnxMapTDomVappUpIcmp6EchoRx,
       "tmnxMapTDomVappUpCpeIcmp6ErrRx": tmnxMapTDomVappUpCpeIcmp6ErrRx,
       "tmnxMapTDomVappUpImIcmp6ErrRx": tmnxMapTDomVappUpImIcmp6ErrRx,
       "tmnxMapTDomVappDownFwdPackets": tmnxMapTDomVappDownFwdPackets,
       "tmnxMapTDomVappDownFwdOctets": tmnxMapTDomVappDownFwdOctets,
       "tmnxMapTDomVappDownDropPackets": tmnxMapTDomVappDownDropPackets,
       "tmnxMapTDomVappDownDropOctets": tmnxMapTDomVappDownDropOctets,
       "tmnxMapTDomVappDownDropFragRx": tmnxMapTDomVappDownDropFragRx,
       "tmnxMapTDomVappDownDropFragReq": tmnxMapTDomVappDownDropFragReq,
       "tmnxMapTDomVappDownDropIcmp4": tmnxMapTDomVappDownDropIcmp4,
       "tmnxMapTDomVappDownDropUnkProto": tmnxMapTDomVappDownDropUnkProto,
       "tmnxMapTDomVappDownFragRx": tmnxMapTDomVappDownFragRx,
       "tmnxMapTDomVappDownFragReq": tmnxMapTDomVappDownFragReq,
       "tmnxMapTDomVappDownIcmp4EchoRx": tmnxMapTDomVappDownIcmp4EchoRx,
       "tmnxMapTDomVappDownIcmp4ErrRepRx": tmnxMapTDomVappDownIcmp4ErrRepRx,
       "tmnxMapTDomVappIcmp4ErrFragDf": tmnxMapTDomVappIcmp4ErrFragDf,
       "tmnxMapTDomVappDownUdpRecalc": tmnxMapTDomVappDownUdpRecalc,
       "tmnxMapTRuleVappStatsTable": tmnxMapTRuleVappStatsTable,
       "tmnxMapTRuleVappStatsEntry": tmnxMapTRuleVappStatsEntry,
       "tmnxMapTRuleVappUpFwdPackets": tmnxMapTRuleVappUpFwdPackets,
       "tmnxMapTRuleVappUpFwdOctets": tmnxMapTRuleVappUpFwdOctets,
       "tmnxMapTRuleVappUpDropPackets": tmnxMapTRuleVappUpDropPackets,
       "tmnxMapTRuleVappUpDropOctets": tmnxMapTRuleVappUpDropOctets,
       "tmnxMapTRuleVappUpDropAntiSpoof": tmnxMapTRuleVappUpDropAntiSpoof,
       "tmnxMapTRuleVappUpDropIcmp6": tmnxMapTRuleVappUpDropIcmp6,
       "tmnxMapTRuleVappUpDropUnkProto": tmnxMapTRuleVappUpDropUnkProto,
       "tmnxMapTRuleVappUpFragRx": tmnxMapTRuleVappUpFragRx,
       "tmnxMapTRuleVappUpIcmp6EchoRx": tmnxMapTRuleVappUpIcmp6EchoRx,
       "tmnxMapTRuleVappUpCpeIcmp6ErrRx": tmnxMapTRuleVappUpCpeIcmp6ErrRx,
       "tmnxMapTRuleVappUpImIcmp6ErrRx": tmnxMapTRuleVappUpImIcmp6ErrRx,
       "tmnxMapTRuleVappDownFwdPackets": tmnxMapTRuleVappDownFwdPackets,
       "tmnxMapTRuleVappDownFwdOctets": tmnxMapTRuleVappDownFwdOctets,
       "tmnxMapTRuleVappDownDropPackets": tmnxMapTRuleVappDownDropPackets,
       "tmnxMapTRuleVappDownDropOctets": tmnxMapTRuleVappDownDropOctets,
       "tmnxMapTRuleVappDownDropFragRx": tmnxMapTRuleVappDownDropFragRx,
       "tmnxMapTRuleVappDownDropFragReq": tmnxMapTRuleVappDownDropFragReq,
       "tmnxMapTRuleVappDownDropIcmp4": tmnxMapTRuleVappDownDropIcmp4,
       "tmnxMapTRuleVappDownDropUnkProto": tmnxMapTRuleVappDownDropUnkProto,
       "tmnxMapTRuleVappDownFragRx": tmnxMapTRuleVappDownFragRx,
       "tmnxMapTRuleVappDownFragReq": tmnxMapTRuleVappDownFragReq,
       "tmnxMapTRuleVappDownIcmp4EchoRx": tmnxMapTRuleVappDownIcmp4EchoRx,
       "tmnxMapTRuleVappDnIcmp4ErrRepRx": tmnxMapTRuleVappDnIcmp4ErrRepRx,
       "tmnxMapTRuleVappIcmp4ErrFragDf": tmnxMapTRuleVappIcmp4ErrFragDf,
       "tmnxMapTRuleVappDownUdpRecalc": tmnxMapTRuleVappDownUdpRecalc,
       "tmnxMapTDomVappFragStatsTable": tmnxMapTDomVappFragStatsTable,
       "tmnxMapTDomVappFragStatsEntry": tmnxMapTDomVappFragStatsEntry,
       "tmnxMapTDomVFragRxResolvedFrag": tmnxMapTDomVFragRxResolvedFrag,
       "tmnxMapTDomVFragRxUnresolvedFrag": tmnxMapTDomVFragRxUnresolvedFrag,
       "tmnxMapTDomVFragTxFrag": tmnxMapTDomVFragTxFrag,
       "tmnxMapTDomVFragDropFTimeout": tmnxMapTDomVFragDropFTimeout,
       "tmnxMapTDomVFragDropBufExhaust": tmnxMapTDomVFragDropBufExhaust,
       "tmnxMapTDomVFragDropTooManyFrag": tmnxMapTDomVFragDropTooManyFrag,
       "tmnxMapTDomVFragDropTooManyLists": tmnxMapTDomVFragDropTooManyLists,
       "tmnxMapTDomVFragDropFragLists": tmnxMapTDomVFragDropFragLists,
       "tmnxMapTDomVFragOverlappingFirst": tmnxMapTDomVFragOverlappingFirst,
       "tmnxMapTDomVappFragListTable": tmnxMapTDomVappFragListTable,
       "tmnxMapTDomVappFragListEntry": tmnxMapTDomVappFragListEntry,
       "tmnxMapTVappFragListId": tmnxMapTVappFragListId,
       "tmnxMapTDomVFragListResolvedFrag": tmnxMapTDomVFragListResolvedFrag,
       "tmnxMapTDomVFragListDroppedFrag": tmnxMapTDomVFragListDroppedFrag,
       "tmnxNatMapDomFPStatsTable": tmnxNatMapDomFPStatsTable,
       "tmnxNatMapDomFPStatsEntry": tmnxNatMapDomFPStatsEntry,
       "tmnxNatMapDomFPUpFwdPackets": tmnxNatMapDomFPUpFwdPackets,
       "tmnxNatMapDomFPUpFwdOctets": tmnxNatMapDomFPUpFwdOctets,
       "tmnxNatMapDomFPUpDropAnchorIf": tmnxNatMapDomFPUpDropAnchorIf,
       "tmnxNatMapDomFPUpDropAntiSpoof": tmnxNatMapDomFPUpDropAntiSpoof,
       "tmnxNatMapDomFPUpDropUnkProto": tmnxNatMapDomFPUpDropUnkProto,
       "tmnxNatMapDomFPDownFwdPackets": tmnxNatMapDomFPDownFwdPackets,
       "tmnxNatMapDomFPDownFwdOctets": tmnxNatMapDomFPDownFwdOctets,
       "tmnxNatMapDomFPDownDropAnchorIf": tmnxNatMapDomFPDownDropAnchorIf,
       "tmnxNatMapDomFPDownDropUnkPro": tmnxNatMapDomFPDownDropUnkPro,
       "tmnxNatMapRuleFPStatsTable": tmnxNatMapRuleFPStatsTable,
       "tmnxNatMapRuleFPStatsEntry": tmnxNatMapRuleFPStatsEntry,
       "tmnxNatMapRuleFPUpFwdPackets": tmnxNatMapRuleFPUpFwdPackets,
       "tmnxNatMapRuleFPUpFwdOctets": tmnxNatMapRuleFPUpFwdOctets,
       "tmnxNatMapRuleFPUpDropAntiSpoof": tmnxNatMapRuleFPUpDropAntiSpoof,
       "tmnxNatMapRuleFPDownFwdPackets": tmnxNatMapRuleFPDownFwdPackets,
       "tmnxNatMapRuleFPDownFwdOctets": tmnxNatMapRuleFPDownFwdOctets,
       "tmnxNatFirewallObjs": tmnxNatFirewallObjs,
       "tmnxNatFwlPlcyTable": tmnxNatFwlPlcyTable,
       "tmnxNatFwlPlcyEntry": tmnxNatFwlPlcyEntry,
       "tmnxNatFwlPlcyName": tmnxNatFwlPlcyName,
       "tmnxNatFwlPlcyRowStatus": tmnxNatFwlPlcyRowStatus,
       "tmnxNatFwlPlcyDomainRouter": tmnxNatFwlPlcyDomainRouter,
       "tmnxNatFwlPlcyDomainName": tmnxNatFwlPlcyDomainName,
       "tmnxNatPolicyTable": tmnxNatPolicyTable,
       "tmnxNatPolicyEntry": tmnxNatPolicyEntry,
       "tmnxNatPolicyName": tmnxNatPolicyName,
       "tmnxNatPolicyRowStatus": tmnxNatPolicyRowStatus,
       "tmnxNatFwlDomTable": tmnxNatFwlDomTable,
       "tmnxNatFwlDomEntry": tmnxNatFwlDomEntry,
       "tmnxNatFwlDomName": tmnxNatFwlDomName,
       "tmnxNatFwlDomRowStatus": tmnxNatFwlDomRowStatus,
       "tmnxNatFwlDomLastMgmtChange": tmnxNatFwlDomLastMgmtChange,
       "tmnxNatFwlDomIsaGrp": tmnxNatFwlDomIsaGrp,
       "tmnxNatFwlDomAdminState": tmnxNatFwlDomAdminState,
       "tmnxNatFwlDomDhcp6ServerRouter": tmnxNatFwlDomDhcp6ServerRouter,
       "tmnxNatFwlDomDhcp6ServerName": tmnxNatFwlDomDhcp6ServerName,
       "tmnxNatFwlDomPrefixTable": tmnxNatFwlDomPrefixTable,
       "tmnxNatFwlDomPrefixEntry": tmnxNatFwlDomPrefixEntry,
       "tmnxNatFwlDomPrefixAddrType": tmnxNatFwlDomPrefixAddrType,
       "tmnxNatFwlDomPrefix": tmnxNatFwlDomPrefix,
       "tmnxNatFwlDomPrefixLength": tmnxNatFwlDomPrefixLength,
       "tmnxNatFwlDomPrefixRowStatus": tmnxNatFwlDomPrefixRowStatus,
       "tmnxNatFwlDomPrefixLastCh": tmnxNatFwlDomPrefixLastCh,
       "tmnxNatFwlDomPrefixDescription": tmnxNatFwlDomPrefixDescription,
       "tmnxNatFwlHostTable": tmnxNatFwlHostTable,
       "tmnxNatFwlHostEntry": tmnxNatFwlHostEntry,
       "tmnxNatFwlHostAddrType": tmnxNatFwlHostAddrType,
       "tmnxNatFwlHostAddr": tmnxNatFwlHostAddr,
       "tmnxNatFwlHostAddrPrefixLength": tmnxNatFwlHostAddrPrefixLength,
       "tmnxNatFwlHostMacAddress": tmnxNatFwlHostMacAddress,
       "tmnxNatFwlHostPlcy": tmnxNatFwlHostPlcy,
       "tmnxNatFwlHostVRtrID": tmnxNatFwlHostVRtrID,
       "tmnxNatFwlHostDmzV6": tmnxNatFwlHostDmzV6,
       "tmnxNatFwlNbrTable": tmnxNatFwlNbrTable,
       "tmnxNatFwlNbrEntry": tmnxNatFwlNbrEntry,
       "tmnxNatFwlNbrAddrType": tmnxNatFwlNbrAddrType,
       "tmnxNatFwlNbrAddr": tmnxNatFwlNbrAddr,
       "tmnxNatFwlNbrMacAddress": tmnxNatFwlNbrMacAddress,
       "tmnxNatSyslogObjs": tmnxNatSyslogObjs,
       "tmnxNatSyslogExpPlcyTable": tmnxNatSyslogExpPlcyTable,
       "tmnxNatSyslogExpPlcyEntry": tmnxNatSyslogExpPlcyEntry,
       "tmnxNatSyslogExpPlcyName": tmnxNatSyslogExpPlcyName,
       "tmnxNatSyslogExpPlcyLastCh": tmnxNatSyslogExpPlcyLastCh,
       "tmnxNatSyslogExpPlcyRowStatus": tmnxNatSyslogExpPlcyRowStatus,
       "tmnxNatSyslogExpPlcyDescription": tmnxNatSyslogExpPlcyDescription,
       "tmnxNatSyslogExpPlcyFacility": tmnxNatSyslogExpPlcyFacility,
       "tmnxNatSyslogExpPlcySeverity": tmnxNatSyslogExpPlcySeverity,
       "tmnxNatSyslogExpPlcyPrefix": tmnxNatSyslogExpPlcyPrefix,
       "tmnxNatSyslogExpPlcyInclude": tmnxNatSyslogExpPlcyInclude,
       "tmnxNatSyslogExpPlcyMtu": tmnxNatSyslogExpPlcyMtu,
       "tmnxNatSyslogExpPlcyRateLimit": tmnxNatSyslogExpPlcyRateLimit,
       "tmnxNatSyslogExpPlcyMaxTxDelay": tmnxNatSyslogExpPlcyMaxTxDelay,
       "tmnxNatSyslogColTable": tmnxNatSyslogColTable,
       "tmnxNatSyslogColEntry": tmnxNatSyslogColEntry,
       "tmnxNatSyslogColAddrType": tmnxNatSyslogColAddrType,
       "tmnxNatSyslogColAddr": tmnxNatSyslogColAddr,
       "tmnxNatSyslogColRowStatus": tmnxNatSyslogColRowStatus,
       "tmnxNatSyslogColLastCh": tmnxNatSyslogColLastCh,
       "tmnxNatSyslogColAdminState": tmnxNatSyslogColAdminState,
       "tmnxNatSyslogColSrcAddrType": tmnxNatSyslogColSrcAddrType,
       "tmnxNatSyslogColSrcAddr": tmnxNatSyslogColSrcAddr,
       "tmnxNatSyslogColDestPort": tmnxNatSyslogColDestPort,
       "tmnxNatCupsObjs": tmnxNatCupsObjs,
       "tmnxNatUpPlcyTable": tmnxNatUpPlcyTable,
       "tmnxNatUpPlcyEntry": tmnxNatUpPlcyEntry,
       "tmnxNatUpPlcyName": tmnxNatUpPlcyName,
       "tmnxNatUpPlcyRowStatus": tmnxNatUpPlcyRowStatus,
       "tmnxNatUpPlcyExtPortBlkSize": tmnxNatUpPlcyExtPortBlkSize,
       "tmnxNatUpPlcyIcmpEchoReply": tmnxNatUpPlcyIcmpEchoReply,
       "tmnxNatUpPlExPrtBlcksWmarkHigh": tmnxNatUpPlExPrtBlcksWmarkHigh,
       "tmnxNatUpPlExPrtBlcksWmarkLow": tmnxNatUpPlExPrtBlcksWmarkLow,
       "tmnxNatUpPlcyDhInsideIpAddrType": tmnxNatUpPlcyDhInsideIpAddrType,
       "tmnxNatUpPlcyDhInsideIpAddress": tmnxNatUpPlcyDhInsideIpAddress,
       "tmnxNatUpPlcyDhInsideRtrId": tmnxNatUpPlcyDhInsideRtrId,
       "tmnxNatUpPlcyDhRate": tmnxNatUpPlcyDhRate,
       "tmnxNatSysStatsObjs": tmnxNatSysStatsObjs,
       "tmnxNatSysRadiusAcctInterimDrop": tmnxNatSysRadiusAcctInterimDrop,
       "tmnxNatCpmObjs": tmnxNatCpmObjs,
       "tmnxNatCpmPlcyTable": tmnxNatCpmPlcyTable,
       "tmnxNatCpmPlcyEntry": tmnxNatCpmPlcyEntry,
       "tmnxNatCpmPlcyName": tmnxNatCpmPlcyName,
       "tmnxNatCpmPlcyRowStatus": tmnxNatCpmPlcyRowStatus,
       "tmnxNatIsaGrpTableLastCh": tmnxNatIsaGrpTableLastCh,
       "tmnxNatIsaMdaTableLastCh": tmnxNatIsaMdaTableLastCh,
       "tmnxNatIsaMdaStatTableLastCh": tmnxNatIsaMdaStatTableLastCh,
       "tmnxNatPlcyTableLastCh": tmnxNatPlcyTableLastCh,
       "tmnxNatVrtrTableLastCh": tmnxNatVrtrTableLastCh,
       "tmnxNatL2AwAddrTableLastCh": tmnxNatL2AwAddrTableLastCh,
       "tmnxNatPlTableLastCh": tmnxNatPlTableLastCh,
       "tmnxNatPlRangeTableLastCh": tmnxNatPlRangeTableLastCh,
       "tmnxNatDestTableLastCh": tmnxNatDestTableLastCh,
       "tmnxNatMapLsnHostTableLastCh": tmnxNatMapLsnHostTableLastCh,
       "tmnxNatMapTableLastCh": tmnxNatMapTableLastCh,
       "tmnxNatDsliteAddrTableLastCh": tmnxNatDsliteAddrTableLastCh,
       "tmnxNatApTableLastCh": tmnxNatApTableLastCh,
       "tmnxNatApServTableLastCh": tmnxNatApServTableLastCh,
       "tmnxNat64TableLastCh": tmnxNat64TableLastCh,
       "tmnxNatGrpCfgTableLastCh": tmnxNatGrpCfgTableLastCh,
       "tmnxNatSubIdTableLastCh": tmnxNatSubIdTableLastCh,
       "tmnxNatPcpPlcyTableLastCh": tmnxNatPcpPlcyTableLastCh,
       "tmnxNatPcpSrvTableLastCh": tmnxNatPcpSrvTableLastCh,
       "tmnxNatPcpSrvIfTableLastCh": tmnxNatPcpSrvIfTableLastCh,
       "tmnxNatDetPlcyTableLastCh": tmnxNatDetPlcyTableLastCh,
       "tmnxNatDetMapTableLastCh": tmnxNatDetMapTableLastCh,
       "tmnxNatUpnpPlcyTableLastCh": tmnxNatUpnpPlcyTableLastCh,
       "tmnxNatPrefixListTableLastCh": tmnxNatPrefixListTableLastCh,
       "tmnxNatPrefixTableLastCh": tmnxNatPrefixTableLastCh,
       "tmnxNatClsfrTableLastCh": tmnxNatClsfrTableLastCh,
       "tmnxNatClsfrN3TableLastCh": tmnxNatClsfrN3TableLastCh,
       "tmnxNatMapDomTableLastCh": tmnxNatMapDomTableLastCh,
       "tmnxNatMapRuleTableLastCh": tmnxNatMapRuleTableLastCh,
       "tmnxNatMapVrtrDomTableLastCh": tmnxNatMapVrtrDomTableLastCh,
       "tmnxNatFwlPlcyTableLastCh": tmnxNatFwlPlcyTableLastCh,
       "tmnxNatFwlDomTableLastCh": tmnxNatFwlDomTableLastCh,
       "tmnxNatFwlDomPrefixTableLastCh": tmnxNatFwlDomPrefixTableLastCh,
       "tmnxNatPlcyUnknProtTableLastCh": tmnxNatPlcyUnknProtTableLastCh,
       "tmnxNatSyslogExpPlcyTableLastCh": tmnxNatSyslogExpPlcyTableLastCh,
       "tmnxNatSyslogColTableLastCh": tmnxNatSyslogColTableLastCh,
       "tmnxNatGrpMonOperGrpTableLastCh": tmnxNatGrpMonOperGrpTableLastCh,
       "tmnxNatGrpMonPortTableLastCh": tmnxNatGrpMonPortTableLastCh,
       "tmnxNatVappTableLastCh": tmnxNatVappTableLastCh,
       "tmnxNatDetPfxMapTableLastCh": tmnxNatDetPfxMapTableLastCh,
       "tmnxNatDetMap2TableLastCh": tmnxNatDetMap2TableLastCh,
       "tmnxNatSourcePrefixTableLastCh": tmnxNatSourcePrefixTableLastCh,
       "tmnxNatDetAddrMapTableLastCh": tmnxNatDetAddrMapTableLastCh,
       "tmnxNatMapTGrpTableLastCh": tmnxNatMapTGrpTableLastCh,
       "tmnxMapTVappTableLastCh": tmnxMapTVappTableLastCh,
       "tmnxNatPlRangeExclTableLastCh": tmnxNatPlRangeExclTableLastCh,
       "tmnxNatCpmPlcyTableLastCh": tmnxNatCpmPlcyTableLastCh,
       "tmnxNatVrtrSpfPlcyTblLastCh": tmnxNatVrtrSpfPlcyTblLastCh,
       "tmnxNatResourceProblem": tmnxNatResourceProblem,
       "tmnxNatLsnSubscIdCount": tmnxNatLsnSubscIdCount,
       "tmnxNatQryLsnSubMaxQryId": tmnxNatQryLsnSubMaxQryId,
       "tmnxNatL2AwHostCount": tmnxNatL2AwHostCount,
       "tmnxNatFwlNbrCount": tmnxNatFwlNbrCount,
       "tmnxNatFwlHostCount": tmnxNatFwlHostCount,
       "tmnxNatNotificationObjs": tmnxNatNotificationObjs,
       "tmnxNatNotifyDescription": tmnxNatNotifyDescription,
       "tmnxNatNotifyOutsideVRtrID": tmnxNatNotifyOutsideVRtrID,
       "tmnxNatNotifyInsideVRtrID": tmnxNatNotifyInsideVRtrID,
       "tmnxNatNotifyOutsideAddrType": tmnxNatNotifyOutsideAddrType,
       "tmnxNatNotifyOutsideAddr": tmnxNatNotifyOutsideAddr,
       "tmnxNatNotifyInsideAddrType": tmnxNatNotifyInsideAddrType,
       "tmnxNatNotifyInsideAddr": tmnxNatNotifyInsideAddr,
       "tmnxNatNotifyPort": tmnxNatNotifyPort,
       "tmnxNatNotifyPort2": tmnxNatNotifyPort2,
       "tmnxNatNotifyDateAndTime": tmnxNatNotifyDateAndTime,
       "tmnxNatNotifyTruthValue": tmnxNatNotifyTruthValue,
       "tmnxNatNotifyLsnSubId": tmnxNatNotifyLsnSubId,
       "tmnxNatNotifyL2AwSubIdent": tmnxNatNotifyL2AwSubIdent,
       "tmnxNatNotifyOutsideEndAddrType": tmnxNatNotifyOutsideEndAddrType,
       "tmnxNatNotifyOutsideEndAddr": tmnxNatNotifyOutsideEndAddr,
       "tmnxNatNotifyPlSeqNum": tmnxNatNotifyPlSeqNum,
       "tmnxNatNotifySubscriberType": tmnxNatNotifySubscriberType,
       "tmnxNatNotifyMdaChassisIndex": tmnxNatNotifyMdaChassisIndex,
       "tmnxNatNotifyMdaCardSlotNum": tmnxNatNotifyMdaCardSlotNum,
       "tmnxNatNotifyMdaSlotNum": tmnxNatNotifyMdaSlotNum,
       "tmnxNatNotifyCounter": tmnxNatNotifyCounter,
       "tmnxNatNotifyNumber": tmnxNatNotifyNumber,
       "tmnxNatNotifyInsideAddrPrefixLen": tmnxNatNotifyInsideAddrPrefixLen,
       "tmnxNatNotifyName": tmnxNatNotifyName,
       "tmnxNatNotifyIsaGrpId": tmnxNatNotifyIsaGrpId,
       "tmnxNatNotifyIsaMemberId": tmnxNatNotifyIsaMemberId,
       "tmnxNatNotifyMemberSubOrHostType": tmnxNatNotifyMemberSubOrHostType,
       "tmnxNatNotifyMemberSubOrHostDesc": tmnxNatNotifyMemberSubOrHostDesc,
       "tmnxNatNotifyIsaMemberEsaNum": tmnxNatNotifyIsaMemberEsaNum,
       "tmnxNatNotifyIsaMemberEsaVappNum": tmnxNatNotifyIsaMemberEsaVappNum,
       "tmnxNatNotifyPoolName": tmnxNatNotifyPoolName,
       "tmnxNatNotifyOutsideIPv4AddrType": tmnxNatNotifyOutsideIPv4AddrType,
       "tmnxNatNotifyOutsideIPv4Addr": tmnxNatNotifyOutsideIPv4Addr,
       "tmnxNatNotifyMbrExPrtBlckUsageHi": tmnxNatNotifyMbrExPrtBlckUsageHi,
       "tmnxNatNotifyPolicyIndex": tmnxNatNotifyPolicyIndex,
       "tmnxNatNotifyPlLsnMbrPortUsageHi": tmnxNatNotifyPlLsnMbrPortUsageHi,
       "tmnxNatNotifyPlLsnMbrProtocol": tmnxNatNotifyPlLsnMbrProtocol,
       "tmnxNatNotifyInterimUpdate": tmnxNatNotifyInterimUpdate,
       "tmnxNatNotifyPrefix": tmnxNatNotifyPrefix,
       "tmnxNatNotifications": tmnxNatNotifications,
       "tmnxNatPlL2AwBlockUsageHigh": tmnxNatPlL2AwBlockUsageHigh,
       "tmnxNatIsaMemberSessionUsageHigh": tmnxNatIsaMemberSessionUsageHigh,
       "tmnxNatPlLsnMemberBlockUsageHigh": tmnxNatPlLsnMemberBlockUsageHigh,
       "tmnxNatLsnSubIcmpPortUsageHigh": tmnxNatLsnSubIcmpPortUsageHigh,
       "tmnxNatLsnSubUdpPortUsageHigh": tmnxNatLsnSubUdpPortUsageHigh,
       "tmnxNatLsnSubTcpPortUsageHigh": tmnxNatLsnSubTcpPortUsageHigh,
       "tmnxNatL2AwSubIcmpPortUsageHigh": tmnxNatL2AwSubIcmpPortUsageHigh,
       "tmnxNatL2AwSubUdpPortUsageHigh": tmnxNatL2AwSubUdpPortUsageHigh,
       "tmnxNatL2AwSubTcpPortUsageHigh": tmnxNatL2AwSubTcpPortUsageHigh,
       "tmnxNatL2AwSubSessionUsageHigh": tmnxNatL2AwSubSessionUsageHigh,
       "tmnxNatLsnSubSessionUsageHigh": tmnxNatLsnSubSessionUsageHigh,
       "tmnxNatPlBlockAllocationLsn": tmnxNatPlBlockAllocationLsn,
       "tmnxNatPlBlockAllocationL2Aw": tmnxNatPlBlockAllocationL2Aw,
       "tmnxNatResourceProblemDetected": tmnxNatResourceProblemDetected,
       "tmnxNatResourceProblemCause": tmnxNatResourceProblemCause,
       "tmnxNatPlAddrFree": tmnxNatPlAddrFree,
       "tmnxNatPlLsnRedActiveChanged": tmnxNatPlLsnRedActiveChanged,
       "tmnxNatPcpSrvStateChanged": tmnxNatPcpSrvStateChanged,
       "tmnxNatFwdEntryAdded": tmnxNatFwdEntryAdded,
       "tmnxNatMdaActive": tmnxNatMdaActive,
       "tmnxNatLsnSubBlksFree": tmnxNatLsnSubBlksFree,
       "tmnxNatDetPlcyChanged": tmnxNatDetPlcyChanged,
       "tmnxNatMdaDetectsLoadSharingErr": tmnxNatMdaDetectsLoadSharingErr,
       "tmnxNatIsaGrpOperStateChanged": tmnxNatIsaGrpOperStateChanged,
       "tmnxNatIsaGrpIsDegraded": tmnxNatIsaGrpIsDegraded,
       "tmnxNatLsnSubIcmpPortUsgHigh": tmnxNatLsnSubIcmpPortUsgHigh,
       "tmnxNatLsnSubUdpPortUsgHigh": tmnxNatLsnSubUdpPortUsgHigh,
       "tmnxNatLsnSubTcpPortUsgHigh": tmnxNatLsnSubTcpPortUsgHigh,
       "tmnxNatLsnSubSessionUsgHigh": tmnxNatLsnSubSessionUsgHigh,
       "tmnxNatInAddrPrefixBlksFree": tmnxNatInAddrPrefixBlksFree,
       "tmnxNatFwd2EntryAdded": tmnxNatFwd2EntryAdded,
       "tmnxNatDetPlcyOperStateChanged": tmnxNatDetPlcyOperStateChanged,
       "tmnxNatDetMapOperStateChanged": tmnxNatDetMapOperStateChanged,
       "tmnxNatFwd2OperStateChanged": tmnxNatFwd2OperStateChanged,
       "tmnxNatVrtrOutDnatOnlyRoutesHigh": tmnxNatVrtrOutDnatOnlyRoutesHigh,
       "tmnxNatMapRuleChange": tmnxNatMapRuleChange,
       "tmnxNatMaxNbrSubsOrHostsExceeded": tmnxNatMaxNbrSubsOrHostsExceeded,
       "tmnxNatNbrSubsOrHostsBelowThrsh": tmnxNatNbrSubsOrHostsBelowThrsh,
       "tmnxNatVappActive": tmnxNatVappActive,
       "tmnxNatVappDetectsLoadSharingErr": tmnxNatVappDetectsLoadSharingErr,
       "tmnxNatDetPfxMapOperStateChanged": tmnxNatDetPfxMapOperStateChanged,
       "tmnxNatDetMap2OperStateChanged": tmnxNatDetMap2OperStateChanged,
       "tmnxNatDynamicConfigMismatch": tmnxNatDynamicConfigMismatch,
       "tmnxNatPlL2AwMembrBlockUsageHigh": tmnxNatPlL2AwMembrBlockUsageHigh,
       "tmnxNatPlMemberExtBlockUsageHigh": tmnxNatPlMemberExtBlockUsageHigh,
       "tmnxNatPlLsnMemberPortUsageHigh": tmnxNatPlLsnMemberPortUsageHigh,
       "tmnxNatDetAddrMapOperStateChngd": tmnxNatDetAddrMapOperStateChngd}
)
