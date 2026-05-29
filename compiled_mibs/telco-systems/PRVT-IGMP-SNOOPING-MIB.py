# SNMP MIB module (PRVT-IGMP-SNOOPING-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\telco-systems\binox\PRVT-IGMP-SNOOPING-MIB

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

(switch,) = mibBuilder.importSymbols(
    "PRVT-SWITCH-MIB",
    "switch")

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
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

prvtIgmpSnoopingMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 135)
)
if mibBuilder.loadTexts:
    prvtIgmpSnoopingMIB.setRevisions(
        ("2010-02-03 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_PrvtIgmpSnoopMIBObjects_ObjectIdentity = ObjectIdentity
prvtIgmpSnoopMIBObjects = _PrvtIgmpSnoopMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 135, 1)
)
_PrvtIgmpSnoopObjects_ObjectIdentity = ObjectIdentity
prvtIgmpSnoopObjects = _PrvtIgmpSnoopObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 135, 1, 1)
)
_PrvtIgmpSnoopCfgTable_Object = MibTable
prvtIgmpSnoopCfgTable = _PrvtIgmpSnoopCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 135, 1, 1, 1)
)
if mibBuilder.loadTexts:
    prvtIgmpSnoopCfgTable.setStatus("current")
_PrvtIgmpSnoopCfgEntry_Object = MibTableRow
prvtIgmpSnoopCfgEntry = _PrvtIgmpSnoopCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 135, 1, 1, 1, 1)
)
prvtIgmpSnoopCfgEntry.setIndexNames(
    (0, "PRVT-IGMP-SNOOPING-MIB", "prvtIgmpSnoopCfgSvcType"),
    (0, "PRVT-IGMP-SNOOPING-MIB", "prvtIgmpSnoopCfgSvcId"),
)
if mibBuilder.loadTexts:
    prvtIgmpSnoopCfgEntry.setStatus("current")


class _PrvtIgmpSnoopCfgSvcType_Type(Integer32):
    """Custom type prvtIgmpSnoopCfgSvcType based on Integer32"""
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
        *(("vlan", 1),
          ("vpls", 2),
          ("dot1q", 3),
          ("tls", 4))
    )


_PrvtIgmpSnoopCfgSvcType_Type.__name__ = "Integer32"
_PrvtIgmpSnoopCfgSvcType_Object = MibTableColumn
prvtIgmpSnoopCfgSvcType = _PrvtIgmpSnoopCfgSvcType_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 135, 1, 1, 1, 1, 1),
    _PrvtIgmpSnoopCfgSvcType_Type()
)
prvtIgmpSnoopCfgSvcType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    prvtIgmpSnoopCfgSvcType.setStatus("current")


class _PrvtIgmpSnoopCfgSvcId_Type(Unsigned32):
    """Custom type prvtIgmpSnoopCfgSvcId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967294),
    )


_PrvtIgmpSnoopCfgSvcId_Type.__name__ = "Unsigned32"
_PrvtIgmpSnoopCfgSvcId_Object = MibTableColumn
prvtIgmpSnoopCfgSvcId = _PrvtIgmpSnoopCfgSvcId_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 135, 1, 1, 1, 1, 2),
    _PrvtIgmpSnoopCfgSvcId_Type()
)
prvtIgmpSnoopCfgSvcId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    prvtIgmpSnoopCfgSvcId.setStatus("current")
_PrvtIgmpSnoopCfgRowStatus_Type = RowStatus
_PrvtIgmpSnoopCfgRowStatus_Object = MibTableColumn
prvtIgmpSnoopCfgRowStatus = _PrvtIgmpSnoopCfgRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 135, 1, 1, 1, 1, 3),
    _PrvtIgmpSnoopCfgRowStatus_Type()
)
prvtIgmpSnoopCfgRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    prvtIgmpSnoopCfgRowStatus.setStatus("current")
_PrvtIgmpSnoopCfgEnable_Type = TruthValue
_PrvtIgmpSnoopCfgEnable_Object = MibTableColumn
prvtIgmpSnoopCfgEnable = _PrvtIgmpSnoopCfgEnable_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 135, 1, 1, 1, 1, 4),
    _PrvtIgmpSnoopCfgEnable_Type()
)
prvtIgmpSnoopCfgEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    prvtIgmpSnoopCfgEnable.setStatus("current")
_PrvtIgmpSnoopCfgRouterAlertCheck_Type = TruthValue
_PrvtIgmpSnoopCfgRouterAlertCheck_Object = MibTableColumn
prvtIgmpSnoopCfgRouterAlertCheck = _PrvtIgmpSnoopCfgRouterAlertCheck_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 135, 1, 1, 1, 1, 5),
    _PrvtIgmpSnoopCfgRouterAlertCheck_Type()
)
prvtIgmpSnoopCfgRouterAlertCheck.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    prvtIgmpSnoopCfgRouterAlertCheck.setStatus("current")
_PrvtIgmpSnoopCfgIpTosCheck_Type = TruthValue
_PrvtIgmpSnoopCfgIpTosCheck_Object = MibTableColumn
prvtIgmpSnoopCfgIpTosCheck = _PrvtIgmpSnoopCfgIpTosCheck_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 135, 1, 1, 1, 1, 6),
    _PrvtIgmpSnoopCfgIpTosCheck_Type()
)
prvtIgmpSnoopCfgIpTosCheck.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    prvtIgmpSnoopCfgIpTosCheck.setStatus("current")
_PrvtIgmpSnoopCfgFloodOnFlush_Type = TruthValue
_PrvtIgmpSnoopCfgFloodOnFlush_Object = MibTableColumn
prvtIgmpSnoopCfgFloodOnFlush = _PrvtIgmpSnoopCfgFloodOnFlush_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 135, 1, 1, 1, 1, 7),
    _PrvtIgmpSnoopCfgFloodOnFlush_Type()
)
prvtIgmpSnoopCfgFloodOnFlush.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    prvtIgmpSnoopCfgFloodOnFlush.setStatus("current")


class _PrvtIgmpSnoopCfgTmrRobustness_Type(Unsigned32):
    """Custom type prvtIgmpSnoopCfgTmrRobustness based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_PrvtIgmpSnoopCfgTmrRobustness_Type.__name__ = "Unsigned32"
_PrvtIgmpSnoopCfgTmrRobustness_Object = MibTableColumn
prvtIgmpSnoopCfgTmrRobustness = _PrvtIgmpSnoopCfgTmrRobustness_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 135, 1, 1, 1, 1, 8),
    _PrvtIgmpSnoopCfgTmrRobustness_Type()
)
prvtIgmpSnoopCfgTmrRobustness.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    prvtIgmpSnoopCfgTmrRobustness.setStatus("current")


class _PrvtIgmpSnoopCfgTmrQIntvl_Type(Unsigned32):
    """Custom type prvtIgmpSnoopCfgTmrQIntvl based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_PrvtIgmpSnoopCfgTmrQIntvl_Type.__name__ = "Unsigned32"
_PrvtIgmpSnoopCfgTmrQIntvl_Object = MibTableColumn
prvtIgmpSnoopCfgTmrQIntvl = _PrvtIgmpSnoopCfgTmrQIntvl_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 135, 1, 1, 1, 1, 9),
    _PrvtIgmpSnoopCfgTmrQIntvl_Type()
)
prvtIgmpSnoopCfgTmrQIntvl.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    prvtIgmpSnoopCfgTmrQIntvl.setStatus("current")


class _PrvtIgmpSnoopCfgTmrQRespIntvl_Type(Unsigned32):
    """Custom type prvtIgmpSnoopCfgTmrQRespIntvl based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_PrvtIgmpSnoopCfgTmrQRespIntvl_Type.__name__ = "Unsigned32"
_PrvtIgmpSnoopCfgTmrQRespIntvl_Object = MibTableColumn
prvtIgmpSnoopCfgTmrQRespIntvl = _PrvtIgmpSnoopCfgTmrQRespIntvl_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 135, 1, 1, 1, 1, 10),
    _PrvtIgmpSnoopCfgTmrQRespIntvl_Type()
)
prvtIgmpSnoopCfgTmrQRespIntvl.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    prvtIgmpSnoopCfgTmrQRespIntvl.setStatus("current")


class _PrvtIgmpSnoopCfgTmrLastMbrQIntvl_Type(Unsigned32):
    """Custom type prvtIgmpSnoopCfgTmrLastMbrQIntvl based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_PrvtIgmpSnoopCfgTmrLastMbrQIntvl_Type.__name__ = "Unsigned32"
_PrvtIgmpSnoopCfgTmrLastMbrQIntvl_Object = MibTableColumn
prvtIgmpSnoopCfgTmrLastMbrQIntvl = _PrvtIgmpSnoopCfgTmrLastMbrQIntvl_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 135, 1, 1, 1, 1, 11),
    _PrvtIgmpSnoopCfgTmrLastMbrQIntvl_Type()
)
prvtIgmpSnoopCfgTmrLastMbrQIntvl.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    prvtIgmpSnoopCfgTmrLastMbrQIntvl.setStatus("current")


class _PrvtIgmpSnoopCfgMode_Type(Integer32):
    """Custom type prvtIgmpSnoopCfgMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("transparent", 0),
          ("report-suppression", 1),
          ("proxy", 2))
    )


_PrvtIgmpSnoopCfgMode_Type.__name__ = "Integer32"
_PrvtIgmpSnoopCfgMode_Object = MibTableColumn
prvtIgmpSnoopCfgMode = _PrvtIgmpSnoopCfgMode_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 135, 1, 1, 1, 1, 12),
    _PrvtIgmpSnoopCfgMode_Type()
)
prvtIgmpSnoopCfgMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    prvtIgmpSnoopCfgMode.setStatus("current")
_PrvtIgmpSnoopCfgSourceAddr_Type = IpAddress
_PrvtIgmpSnoopCfgSourceAddr_Object = MibTableColumn
prvtIgmpSnoopCfgSourceAddr = _PrvtIgmpSnoopCfgSourceAddr_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 135, 1, 1, 1, 1, 13),
    _PrvtIgmpSnoopCfgSourceAddr_Type()
)
prvtIgmpSnoopCfgSourceAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    prvtIgmpSnoopCfgSourceAddr.setStatus("current")
_PrvtIgmpSnoopCfgIfTable_Object = MibTable
prvtIgmpSnoopCfgIfTable = _PrvtIgmpSnoopCfgIfTable_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 135, 1, 1, 2)
)
if mibBuilder.loadTexts:
    prvtIgmpSnoopCfgIfTable.setStatus("current")
_PrvtIgmpSnoopCfgIfEntry_Object = MibTableRow
prvtIgmpSnoopCfgIfEntry = _PrvtIgmpSnoopCfgIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 135, 1, 1, 2, 1)
)
prvtIgmpSnoopCfgIfEntry.setIndexNames(
    (0, "PRVT-IGMP-SNOOPING-MIB", "prvtIgmpSnoopCfgSvcType"),
    (0, "PRVT-IGMP-SNOOPING-MIB", "prvtIgmpSnoopCfgSvcId"),
    (0, "PRVT-IGMP-SNOOPING-MIB", "prvtIgmpSnoopCfgIfType"),
    (0, "PRVT-IGMP-SNOOPING-MIB", "prvtIgmpSnoopCfgIfName"),
)
if mibBuilder.loadTexts:
    prvtIgmpSnoopCfgIfEntry.setStatus("current")


class _PrvtIgmpSnoopCfgIfType_Type(Integer32):
    """Custom type prvtIgmpSnoopCfgIfType based on Integer32"""
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
        *(("port", 1),
          ("sap", 2),
          ("spoke-sdp", 3),
          ("mesh-sdp", 4))
    )


_PrvtIgmpSnoopCfgIfType_Type.__name__ = "Integer32"
_PrvtIgmpSnoopCfgIfType_Object = MibTableColumn
prvtIgmpSnoopCfgIfType = _PrvtIgmpSnoopCfgIfType_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 135, 1, 1, 2, 1, 1),
    _PrvtIgmpSnoopCfgIfType_Type()
)
prvtIgmpSnoopCfgIfType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    prvtIgmpSnoopCfgIfType.setStatus("current")
_PrvtIgmpSnoopCfgIfName_Type = OctetString
_PrvtIgmpSnoopCfgIfName_Object = MibTableColumn
prvtIgmpSnoopCfgIfName = _PrvtIgmpSnoopCfgIfName_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 135, 1, 1, 2, 1, 2),
    _PrvtIgmpSnoopCfgIfName_Type()
)
prvtIgmpSnoopCfgIfName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    prvtIgmpSnoopCfgIfName.setStatus("current")
_PrvtIgmpSnoopCfgIfRowStatus_Type = RowStatus
_PrvtIgmpSnoopCfgIfRowStatus_Object = MibTableColumn
prvtIgmpSnoopCfgIfRowStatus = _PrvtIgmpSnoopCfgIfRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 135, 1, 1, 2, 1, 3),
    _PrvtIgmpSnoopCfgIfRowStatus_Type()
)
prvtIgmpSnoopCfgIfRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    prvtIgmpSnoopCfgIfRowStatus.setStatus("current")


class _PrvtIgmpSnoopCfgIfMaxGroups_Type(Unsigned32):
    """Custom type prvtIgmpSnoopCfgIfMaxGroups based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1024),
    )


_PrvtIgmpSnoopCfgIfMaxGroups_Type.__name__ = "Unsigned32"
_PrvtIgmpSnoopCfgIfMaxGroups_Object = MibTableColumn
prvtIgmpSnoopCfgIfMaxGroups = _PrvtIgmpSnoopCfgIfMaxGroups_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 135, 1, 1, 2, 1, 4),
    _PrvtIgmpSnoopCfgIfMaxGroups_Type()
)
prvtIgmpSnoopCfgIfMaxGroups.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    prvtIgmpSnoopCfgIfMaxGroups.setStatus("current")
_PrvtIgmpSnoopCfgIfMRouter_Type = TruthValue
_PrvtIgmpSnoopCfgIfMRouter_Object = MibTableColumn
prvtIgmpSnoopCfgIfMRouter = _PrvtIgmpSnoopCfgIfMRouter_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 135, 1, 1, 2, 1, 5),
    _PrvtIgmpSnoopCfgIfMRouter_Type()
)
prvtIgmpSnoopCfgIfMRouter.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    prvtIgmpSnoopCfgIfMRouter.setStatus("current")
_PrvtIgmpSnoopCfgIfMRouterBlock_Type = TruthValue
_PrvtIgmpSnoopCfgIfMRouterBlock_Object = MibTableColumn
prvtIgmpSnoopCfgIfMRouterBlock = _PrvtIgmpSnoopCfgIfMRouterBlock_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 135, 1, 1, 2, 1, 6),
    _PrvtIgmpSnoopCfgIfMRouterBlock_Type()
)
prvtIgmpSnoopCfgIfMRouterBlock.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    prvtIgmpSnoopCfgIfMRouterBlock.setStatus("current")
_PrvtIgmpSnoopCfgIfExplctTracking_Type = TruthValue
_PrvtIgmpSnoopCfgIfExplctTracking_Object = MibTableColumn
prvtIgmpSnoopCfgIfExplctTracking = _PrvtIgmpSnoopCfgIfExplctTracking_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 135, 1, 1, 2, 1, 7),
    _PrvtIgmpSnoopCfgIfExplctTracking_Type()
)
prvtIgmpSnoopCfgIfExplctTracking.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    prvtIgmpSnoopCfgIfExplctTracking.setStatus("current")
_PrvtIgmpSnoopCfgIfFastLeave_Type = TruthValue
_PrvtIgmpSnoopCfgIfFastLeave_Object = MibTableColumn
prvtIgmpSnoopCfgIfFastLeave = _PrvtIgmpSnoopCfgIfFastLeave_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 135, 1, 1, 2, 1, 8),
    _PrvtIgmpSnoopCfgIfFastLeave_Type()
)
prvtIgmpSnoopCfgIfFastLeave.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    prvtIgmpSnoopCfgIfFastLeave.setStatus("current")
_PrvtIgmpSnoopCfgIfReportBlock_Type = TruthValue
_PrvtIgmpSnoopCfgIfReportBlock_Object = MibTableColumn
prvtIgmpSnoopCfgIfReportBlock = _PrvtIgmpSnoopCfgIfReportBlock_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 135, 1, 1, 2, 1, 9),
    _PrvtIgmpSnoopCfgIfReportBlock_Type()
)
prvtIgmpSnoopCfgIfReportBlock.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    prvtIgmpSnoopCfgIfReportBlock.setStatus("current")
_PrvtIgmpSnoopCfgIfForceFwd_Type = TruthValue
_PrvtIgmpSnoopCfgIfForceFwd_Object = MibTableColumn
prvtIgmpSnoopCfgIfForceFwd = _PrvtIgmpSnoopCfgIfForceFwd_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 135, 1, 1, 2, 1, 10),
    _PrvtIgmpSnoopCfgIfForceFwd_Type()
)
prvtIgmpSnoopCfgIfForceFwd.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    prvtIgmpSnoopCfgIfForceFwd.setStatus("current")
_PrvtIgmpSnoopCfgIfMrtAllowRprts_Type = TruthValue
_PrvtIgmpSnoopCfgIfMrtAllowRprts_Object = MibTableColumn
prvtIgmpSnoopCfgIfMrtAllowRprts = _PrvtIgmpSnoopCfgIfMrtAllowRprts_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 135, 1, 1, 2, 1, 11),
    _PrvtIgmpSnoopCfgIfMrtAllowRprts_Type()
)
prvtIgmpSnoopCfgIfMrtAllowRprts.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    prvtIgmpSnoopCfgIfMrtAllowRprts.setStatus("current")
_PrvtIgmpSnoopCfgIfQuerier_Type = TruthValue
_PrvtIgmpSnoopCfgIfQuerier_Object = MibTableColumn
prvtIgmpSnoopCfgIfQuerier = _PrvtIgmpSnoopCfgIfQuerier_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 135, 1, 1, 2, 1, 12),
    _PrvtIgmpSnoopCfgIfQuerier_Type()
)
prvtIgmpSnoopCfgIfQuerier.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    prvtIgmpSnoopCfgIfQuerier.setStatus("current")
_PrvtIgmpSnoopDbGrpTable_Object = MibTable
prvtIgmpSnoopDbGrpTable = _PrvtIgmpSnoopDbGrpTable_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 135, 1, 1, 3)
)
if mibBuilder.loadTexts:
    prvtIgmpSnoopDbGrpTable.setStatus("current")
_PrvtIgmpSnoopDbGrpEntry_Object = MibTableRow
prvtIgmpSnoopDbGrpEntry = _PrvtIgmpSnoopDbGrpEntry_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 135, 1, 1, 3, 1)
)
prvtIgmpSnoopDbGrpEntry.setIndexNames(
    (0, "PRVT-IGMP-SNOOPING-MIB", "prvtIgmpSnoopDbGrpStatsVlanId"),
    (0, "PRVT-IGMP-SNOOPING-MIB", "prvtIgmpSnoopCfgIfName"),
    (0, "PRVT-IGMP-SNOOPING-MIB", "prvtIgmpSnoopDbGrpIpAddr"),
)
if mibBuilder.loadTexts:
    prvtIgmpSnoopDbGrpEntry.setStatus("current")
_PrvtIgmpSnoopDbGrpIpAddr_Type = IpAddress
_PrvtIgmpSnoopDbGrpIpAddr_Object = MibTableColumn
prvtIgmpSnoopDbGrpIpAddr = _PrvtIgmpSnoopDbGrpIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 135, 1, 1, 3, 1, 1),
    _PrvtIgmpSnoopDbGrpIpAddr_Type()
)
prvtIgmpSnoopDbGrpIpAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    prvtIgmpSnoopDbGrpIpAddr.setStatus("current")


class _PrvtIgmpSnoopDbGrpBitFlags_Type(Unsigned32):
    """Custom type prvtIgmpSnoopDbGrpBitFlags based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_PrvtIgmpSnoopDbGrpBitFlags_Type.__name__ = "Unsigned32"
_PrvtIgmpSnoopDbGrpBitFlags_Object = MibTableColumn
prvtIgmpSnoopDbGrpBitFlags = _PrvtIgmpSnoopDbGrpBitFlags_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 135, 1, 1, 3, 1, 2),
    _PrvtIgmpSnoopDbGrpBitFlags_Type()
)
prvtIgmpSnoopDbGrpBitFlags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtIgmpSnoopDbGrpBitFlags.setStatus("current")


class _PrvtIgmpSnoopDbGrpFilterMode_Type(Integer32):
    """Custom type prvtIgmpSnoopDbGrpFilterMode based on Integer32"""
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
        *(("include", 1),
          ("exclude", 2),
          ("toInclude", 3),
          ("toExclude", 4),
          ("allow", 5),
          ("block", 6))
    )


_PrvtIgmpSnoopDbGrpFilterMode_Type.__name__ = "Integer32"
_PrvtIgmpSnoopDbGrpFilterMode_Object = MibTableColumn
prvtIgmpSnoopDbGrpFilterMode = _PrvtIgmpSnoopDbGrpFilterMode_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 135, 1, 1, 3, 1, 3),
    _PrvtIgmpSnoopDbGrpFilterMode_Type()
)
prvtIgmpSnoopDbGrpFilterMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtIgmpSnoopDbGrpFilterMode.setStatus("current")


class _PrvtIgmpSnoopDbGrpExpireTime_Type(Unsigned32):
    """Custom type prvtIgmpSnoopDbGrpExpireTime based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_PrvtIgmpSnoopDbGrpExpireTime_Type.__name__ = "Unsigned32"
_PrvtIgmpSnoopDbGrpExpireTime_Object = MibTableColumn
prvtIgmpSnoopDbGrpExpireTime = _PrvtIgmpSnoopDbGrpExpireTime_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 135, 1, 1, 3, 1, 4),
    _PrvtIgmpSnoopDbGrpExpireTime_Type()
)
prvtIgmpSnoopDbGrpExpireTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtIgmpSnoopDbGrpExpireTime.setStatus("current")
_PrvtIgmpSnoopDbGrpHostTable_Object = MibTable
prvtIgmpSnoopDbGrpHostTable = _PrvtIgmpSnoopDbGrpHostTable_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 135, 1, 1, 4)
)
if mibBuilder.loadTexts:
    prvtIgmpSnoopDbGrpHostTable.setStatus("current")
_PrvtIgmpSnoopDbGrpHostEntry_Object = MibTableRow
prvtIgmpSnoopDbGrpHostEntry = _PrvtIgmpSnoopDbGrpHostEntry_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 135, 1, 1, 4, 1)
)
prvtIgmpSnoopDbGrpHostEntry.setIndexNames(
    (0, "PRVT-IGMP-SNOOPING-MIB", "prvtIgmpSnoopDbGrpStatsVlanId"),
    (0, "PRVT-IGMP-SNOOPING-MIB", "prvtIgmpSnoopCfgIfName"),
    (0, "PRVT-IGMP-SNOOPING-MIB", "prvtIgmpSnoopDbGrpIpAddr"),
    (0, "PRVT-IGMP-SNOOPING-MIB", "prvtIgmpSnoopDbGrpHostSourceIp"),
)
if mibBuilder.loadTexts:
    prvtIgmpSnoopDbGrpHostEntry.setStatus("current")
_PrvtIgmpSnoopDbGrpHostSourceIp_Type = IpAddress
_PrvtIgmpSnoopDbGrpHostSourceIp_Object = MibTableColumn
prvtIgmpSnoopDbGrpHostSourceIp = _PrvtIgmpSnoopDbGrpHostSourceIp_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 135, 1, 1, 4, 1, 1),
    _PrvtIgmpSnoopDbGrpHostSourceIp_Type()
)
prvtIgmpSnoopDbGrpHostSourceIp.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    prvtIgmpSnoopDbGrpHostSourceIp.setStatus("current")


class _PrvtIgmpSnoopDbGrpHostExpireTime_Type(Unsigned32):
    """Custom type prvtIgmpSnoopDbGrpHostExpireTime based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_PrvtIgmpSnoopDbGrpHostExpireTime_Type.__name__ = "Unsigned32"
_PrvtIgmpSnoopDbGrpHostExpireTime_Object = MibTableColumn
prvtIgmpSnoopDbGrpHostExpireTime = _PrvtIgmpSnoopDbGrpHostExpireTime_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 135, 1, 1, 4, 1, 2),
    _PrvtIgmpSnoopDbGrpHostExpireTime_Type()
)
prvtIgmpSnoopDbGrpHostExpireTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtIgmpSnoopDbGrpHostExpireTime.setStatus("current")
_PrvtIgmpSnoopDbGrpSrcTable_Object = MibTable
prvtIgmpSnoopDbGrpSrcTable = _PrvtIgmpSnoopDbGrpSrcTable_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 135, 1, 1, 5)
)
if mibBuilder.loadTexts:
    prvtIgmpSnoopDbGrpSrcTable.setStatus("current")
_PrvtIgmpSnoopDbGrpSrcEntry_Object = MibTableRow
prvtIgmpSnoopDbGrpSrcEntry = _PrvtIgmpSnoopDbGrpSrcEntry_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 135, 1, 1, 5, 1)
)
prvtIgmpSnoopDbGrpSrcEntry.setIndexNames(
    (0, "PRVT-IGMP-SNOOPING-MIB", "prvtIgmpSnoopDbGrpStatsVlanId"),
    (0, "PRVT-IGMP-SNOOPING-MIB", "prvtIgmpSnoopCfgIfName"),
    (0, "PRVT-IGMP-SNOOPING-MIB", "prvtIgmpSnoopDbGrpIpAddr"),
    (0, "PRVT-IGMP-SNOOPING-MIB", "prvtIgmpSnoopDbGrpSrcIpAddr"),
)
if mibBuilder.loadTexts:
    prvtIgmpSnoopDbGrpSrcEntry.setStatus("current")
_PrvtIgmpSnoopDbGrpSrcIpAddr_Type = IpAddress
_PrvtIgmpSnoopDbGrpSrcIpAddr_Object = MibTableColumn
prvtIgmpSnoopDbGrpSrcIpAddr = _PrvtIgmpSnoopDbGrpSrcIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 135, 1, 1, 5, 1, 1),
    _PrvtIgmpSnoopDbGrpSrcIpAddr_Type()
)
prvtIgmpSnoopDbGrpSrcIpAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    prvtIgmpSnoopDbGrpSrcIpAddr.setStatus("current")


class _PrvtIgmpSnoopDbGrpSrcExpTime_Type(Unsigned32):
    """Custom type prvtIgmpSnoopDbGrpSrcExpTime based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_PrvtIgmpSnoopDbGrpSrcExpTime_Type.__name__ = "Unsigned32"
_PrvtIgmpSnoopDbGrpSrcExpTime_Object = MibTableColumn
prvtIgmpSnoopDbGrpSrcExpTime = _PrvtIgmpSnoopDbGrpSrcExpTime_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 135, 1, 1, 5, 1, 2),
    _PrvtIgmpSnoopDbGrpSrcExpTime_Type()
)
prvtIgmpSnoopDbGrpSrcExpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtIgmpSnoopDbGrpSrcExpTime.setStatus("current")
_PrvtIgmpSnoopDbGrpSrcHostTable_Object = MibTable
prvtIgmpSnoopDbGrpSrcHostTable = _PrvtIgmpSnoopDbGrpSrcHostTable_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 135, 1, 1, 6)
)
if mibBuilder.loadTexts:
    prvtIgmpSnoopDbGrpSrcHostTable.setStatus("current")
_PrvtIgmpSnoopDbGrpSrcHostEntry_Object = MibTableRow
prvtIgmpSnoopDbGrpSrcHostEntry = _PrvtIgmpSnoopDbGrpSrcHostEntry_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 135, 1, 1, 6, 1)
)
prvtIgmpSnoopDbGrpSrcHostEntry.setIndexNames(
    (0, "PRVT-IGMP-SNOOPING-MIB", "prvtIgmpSnoopDbGrpStatsVlanId"),
    (0, "PRVT-IGMP-SNOOPING-MIB", "prvtIgmpSnoopCfgIfName"),
    (0, "PRVT-IGMP-SNOOPING-MIB", "prvtIgmpSnoopDbGrpIpAddr"),
    (0, "PRVT-IGMP-SNOOPING-MIB", "prvtIgmpSnoopDbGrpSrcIpAddr"),
    (0, "PRVT-IGMP-SNOOPING-MIB", "prvtIgmpSnoopDbGrpSrcHostIp"),
)
if mibBuilder.loadTexts:
    prvtIgmpSnoopDbGrpSrcHostEntry.setStatus("current")
_PrvtIgmpSnoopDbGrpSrcHostIp_Type = IpAddress
_PrvtIgmpSnoopDbGrpSrcHostIp_Object = MibTableColumn
prvtIgmpSnoopDbGrpSrcHostIp = _PrvtIgmpSnoopDbGrpSrcHostIp_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 135, 1, 1, 6, 1, 1),
    _PrvtIgmpSnoopDbGrpSrcHostIp_Type()
)
prvtIgmpSnoopDbGrpSrcHostIp.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    prvtIgmpSnoopDbGrpSrcHostIp.setStatus("current")


class _PrvtIgmpSnoopDbGrpSrcHostExpTime_Type(Unsigned32):
    """Custom type prvtIgmpSnoopDbGrpSrcHostExpTime based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_PrvtIgmpSnoopDbGrpSrcHostExpTime_Type.__name__ = "Unsigned32"
_PrvtIgmpSnoopDbGrpSrcHostExpTime_Object = MibTableColumn
prvtIgmpSnoopDbGrpSrcHostExpTime = _PrvtIgmpSnoopDbGrpSrcHostExpTime_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 135, 1, 1, 6, 1, 2),
    _PrvtIgmpSnoopDbGrpSrcHostExpTime_Type()
)
prvtIgmpSnoopDbGrpSrcHostExpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtIgmpSnoopDbGrpSrcHostExpTime.setStatus("current")
_PrvtIgmpSnoopDbMrtrTable_Object = MibTable
prvtIgmpSnoopDbMrtrTable = _PrvtIgmpSnoopDbMrtrTable_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 135, 1, 1, 7)
)
if mibBuilder.loadTexts:
    prvtIgmpSnoopDbMrtrTable.setStatus("current")
_PrvtIgmpSnoopDbMrtrEntry_Object = MibTableRow
prvtIgmpSnoopDbMrtrEntry = _PrvtIgmpSnoopDbMrtrEntry_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 135, 1, 1, 7, 1)
)
prvtIgmpSnoopDbMrtrEntry.setIndexNames(
    (0, "PRVT-IGMP-SNOOPING-MIB", "prvtIgmpSnoopDbGrpStatsVlanId"),
    (0, "PRVT-IGMP-SNOOPING-MIB", "prvtIgmpSnoopCfgIfName"),
    (0, "PRVT-IGMP-SNOOPING-MIB", "prvtIgmpSnoopDbMrtrSrcIp"),
)
if mibBuilder.loadTexts:
    prvtIgmpSnoopDbMrtrEntry.setStatus("current")
_PrvtIgmpSnoopDbMrtrSrcIp_Type = IpAddress
_PrvtIgmpSnoopDbMrtrSrcIp_Object = MibTableColumn
prvtIgmpSnoopDbMrtrSrcIp = _PrvtIgmpSnoopDbMrtrSrcIp_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 135, 1, 1, 7, 1, 1),
    _PrvtIgmpSnoopDbMrtrSrcIp_Type()
)
prvtIgmpSnoopDbMrtrSrcIp.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    prvtIgmpSnoopDbMrtrSrcIp.setStatus("current")


class _PrvtIgmpSnoopDbMrtrFlags_Type(Unsigned32):
    """Custom type prvtIgmpSnoopDbMrtrFlags based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_PrvtIgmpSnoopDbMrtrFlags_Type.__name__ = "Unsigned32"
_PrvtIgmpSnoopDbMrtrFlags_Object = MibTableColumn
prvtIgmpSnoopDbMrtrFlags = _PrvtIgmpSnoopDbMrtrFlags_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 135, 1, 1, 7, 1, 2),
    _PrvtIgmpSnoopDbMrtrFlags_Type()
)
prvtIgmpSnoopDbMrtrFlags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtIgmpSnoopDbMrtrFlags.setStatus("current")


class _PrvtIgmpSnoopDbMrtrExpTime_Type(Unsigned32):
    """Custom type prvtIgmpSnoopDbMrtrExpTime based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_PrvtIgmpSnoopDbMrtrExpTime_Type.__name__ = "Unsigned32"
_PrvtIgmpSnoopDbMrtrExpTime_Object = MibTableColumn
prvtIgmpSnoopDbMrtrExpTime = _PrvtIgmpSnoopDbMrtrExpTime_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 135, 1, 1, 7, 1, 3),
    _PrvtIgmpSnoopDbMrtrExpTime_Type()
)
prvtIgmpSnoopDbMrtrExpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtIgmpSnoopDbMrtrExpTime.setStatus("current")
_PrvtIgmpSnoopDbGrpStatsTable_Object = MibTable
prvtIgmpSnoopDbGrpStatsTable = _PrvtIgmpSnoopDbGrpStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 135, 1, 1, 8)
)
if mibBuilder.loadTexts:
    prvtIgmpSnoopDbGrpStatsTable.setStatus("current")
_PrvtIgmpSnoopDbGrpStatsEntry_Object = MibTableRow
prvtIgmpSnoopDbGrpStatsEntry = _PrvtIgmpSnoopDbGrpStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 135, 1, 1, 8, 1)
)
prvtIgmpSnoopDbGrpStatsEntry.setIndexNames(
    (0, "PRVT-IGMP-SNOOPING-MIB", "prvtIgmpSnoopDbGrpStatsVlanId"),
)
if mibBuilder.loadTexts:
    prvtIgmpSnoopDbGrpStatsEntry.setStatus("current")
_PrvtIgmpSnoopDbGrpStatsVlanId_Type = Integer32
_PrvtIgmpSnoopDbGrpStatsVlanId_Object = MibTableColumn
prvtIgmpSnoopDbGrpStatsVlanId = _PrvtIgmpSnoopDbGrpStatsVlanId_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 135, 1, 1, 8, 1, 1),
    _PrvtIgmpSnoopDbGrpStatsVlanId_Type()
)
prvtIgmpSnoopDbGrpStatsVlanId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    prvtIgmpSnoopDbGrpStatsVlanId.setStatus("current")
_PrvtIgmpSnoopDbGrpStatsDscPkt_Type = Unsigned32
_PrvtIgmpSnoopDbGrpStatsDscPkt_Object = MibTableColumn
prvtIgmpSnoopDbGrpStatsDscPkt = _PrvtIgmpSnoopDbGrpStatsDscPkt_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 135, 1, 1, 8, 1, 2),
    _PrvtIgmpSnoopDbGrpStatsDscPkt_Type()
)
prvtIgmpSnoopDbGrpStatsDscPkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtIgmpSnoopDbGrpStatsDscPkt.setStatus("current")
_PrvtIgmpSnoopDbGrpStatsDscPktTtl_Type = Unsigned32
_PrvtIgmpSnoopDbGrpStatsDscPktTtl_Object = MibTableColumn
prvtIgmpSnoopDbGrpStatsDscPktTtl = _PrvtIgmpSnoopDbGrpStatsDscPktTtl_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 135, 1, 1, 8, 1, 3),
    _PrvtIgmpSnoopDbGrpStatsDscPktTtl_Type()
)
prvtIgmpSnoopDbGrpStatsDscPktTtl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtIgmpSnoopDbGrpStatsDscPktTtl.setStatus("current")
_PrvtIgmpSnoopDbGrpStatsDscPktChk_Type = Unsigned32
_PrvtIgmpSnoopDbGrpStatsDscPktChk_Object = MibTableColumn
prvtIgmpSnoopDbGrpStatsDscPktChk = _PrvtIgmpSnoopDbGrpStatsDscPktChk_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 135, 1, 1, 8, 1, 4),
    _PrvtIgmpSnoopDbGrpStatsDscPktChk_Type()
)
prvtIgmpSnoopDbGrpStatsDscPktChk.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtIgmpSnoopDbGrpStatsDscPktChk.setStatus("current")
_PrvtIgmpSnoopDbGrpStatsDscPktRA_Type = Unsigned32
_PrvtIgmpSnoopDbGrpStatsDscPktRA_Object = MibTableColumn
prvtIgmpSnoopDbGrpStatsDscPktRA = _PrvtIgmpSnoopDbGrpStatsDscPktRA_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 135, 1, 1, 8, 1, 5),
    _PrvtIgmpSnoopDbGrpStatsDscPktRA_Type()
)
prvtIgmpSnoopDbGrpStatsDscPktRA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtIgmpSnoopDbGrpStatsDscPktRA.setStatus("current")
_PrvtIgmpSnoopDbIfStatsTable_Object = MibTable
prvtIgmpSnoopDbIfStatsTable = _PrvtIgmpSnoopDbIfStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 135, 1, 1, 9)
)
if mibBuilder.loadTexts:
    prvtIgmpSnoopDbIfStatsTable.setStatus("current")
_PrvtIgmpSnoopDbIfStatsEntry_Object = MibTableRow
prvtIgmpSnoopDbIfStatsEntry = _PrvtIgmpSnoopDbIfStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 135, 1, 1, 9, 1)
)
prvtIgmpSnoopDbIfStatsEntry.setIndexNames(
    (0, "PRVT-IGMP-SNOOPING-MIB", "prvtIgmpSnoopDbGrpStatsVlanId"),
    (0, "PRVT-IGMP-SNOOPING-MIB", "prvtIgmpSnoopDbIfStatsIfName"),
)
if mibBuilder.loadTexts:
    prvtIgmpSnoopDbIfStatsEntry.setStatus("current")
_PrvtIgmpSnoopDbIfStatsIfName_Type = OctetString
_PrvtIgmpSnoopDbIfStatsIfName_Object = MibTableColumn
prvtIgmpSnoopDbIfStatsIfName = _PrvtIgmpSnoopDbIfStatsIfName_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 135, 1, 1, 9, 1, 1),
    _PrvtIgmpSnoopDbIfStatsIfName_Type()
)
prvtIgmpSnoopDbIfStatsIfName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    prvtIgmpSnoopDbIfStatsIfName.setStatus("current")
_PrvtIgmpSnoopDbIfStatsV2Reports_Type = Unsigned32
_PrvtIgmpSnoopDbIfStatsV2Reports_Object = MibTableColumn
prvtIgmpSnoopDbIfStatsV2Reports = _PrvtIgmpSnoopDbIfStatsV2Reports_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 135, 1, 1, 9, 1, 2),
    _PrvtIgmpSnoopDbIfStatsV2Reports_Type()
)
prvtIgmpSnoopDbIfStatsV2Reports.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtIgmpSnoopDbIfStatsV2Reports.setStatus("current")
_PrvtIgmpSnoopDbIfStatsV2Leaves_Type = Unsigned32
_PrvtIgmpSnoopDbIfStatsV2Leaves_Object = MibTableColumn
prvtIgmpSnoopDbIfStatsV2Leaves = _PrvtIgmpSnoopDbIfStatsV2Leaves_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 135, 1, 1, 9, 1, 3),
    _PrvtIgmpSnoopDbIfStatsV2Leaves_Type()
)
prvtIgmpSnoopDbIfStatsV2Leaves.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtIgmpSnoopDbIfStatsV2Leaves.setStatus("current")
_PrvtIgmpSnoopDbIfStatsV3Reports_Type = Unsigned32
_PrvtIgmpSnoopDbIfStatsV3Reports_Object = MibTableColumn
prvtIgmpSnoopDbIfStatsV3Reports = _PrvtIgmpSnoopDbIfStatsV3Reports_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 135, 1, 1, 9, 1, 4),
    _PrvtIgmpSnoopDbIfStatsV3Reports_Type()
)
prvtIgmpSnoopDbIfStatsV3Reports.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtIgmpSnoopDbIfStatsV3Reports.setStatus("current")
_PrvtIgmpSnoopDbIfStatsGenQueries_Type = Unsigned32
_PrvtIgmpSnoopDbIfStatsGenQueries_Object = MibTableColumn
prvtIgmpSnoopDbIfStatsGenQueries = _PrvtIgmpSnoopDbIfStatsGenQueries_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 135, 1, 1, 9, 1, 5),
    _PrvtIgmpSnoopDbIfStatsGenQueries_Type()
)
prvtIgmpSnoopDbIfStatsGenQueries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtIgmpSnoopDbIfStatsGenQueries.setStatus("current")
_PrvtIgmpSnoopDbIfStatsGrpQueries_Type = Unsigned32
_PrvtIgmpSnoopDbIfStatsGrpQueries_Object = MibTableColumn
prvtIgmpSnoopDbIfStatsGrpQueries = _PrvtIgmpSnoopDbIfStatsGrpQueries_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 135, 1, 1, 9, 1, 6),
    _PrvtIgmpSnoopDbIfStatsGrpQueries_Type()
)
prvtIgmpSnoopDbIfStatsGrpQueries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtIgmpSnoopDbIfStatsGrpQueries.setStatus("current")
_PrvtIgmpSnoopDbIfStatsSrcQueries_Type = Unsigned32
_PrvtIgmpSnoopDbIfStatsSrcQueries_Object = MibTableColumn
prvtIgmpSnoopDbIfStatsSrcQueries = _PrvtIgmpSnoopDbIfStatsSrcQueries_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 135, 1, 1, 9, 1, 7),
    _PrvtIgmpSnoopDbIfStatsSrcQueries_Type()
)
prvtIgmpSnoopDbIfStatsSrcQueries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtIgmpSnoopDbIfStatsSrcQueries.setStatus("current")
_PrvtIgmpSnoopMemoryTable_Object = MibTable
prvtIgmpSnoopMemoryTable = _PrvtIgmpSnoopMemoryTable_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 135, 1, 1, 10)
)
if mibBuilder.loadTexts:
    prvtIgmpSnoopMemoryTable.setStatus("current")
_PrvtIgmpSnoopMemoryEntry_Object = MibTableRow
prvtIgmpSnoopMemoryEntry = _PrvtIgmpSnoopMemoryEntry_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 135, 1, 1, 10, 1)
)
prvtIgmpSnoopMemoryEntry.setIndexNames(
    (0, "PRVT-IGMP-SNOOPING-MIB", "prvtIgmpSnoopMemoryPoolId"),
)
if mibBuilder.loadTexts:
    prvtIgmpSnoopMemoryEntry.setStatus("current")
_PrvtIgmpSnoopMemoryPoolId_Type = Unsigned32
_PrvtIgmpSnoopMemoryPoolId_Object = MibTableColumn
prvtIgmpSnoopMemoryPoolId = _PrvtIgmpSnoopMemoryPoolId_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 135, 1, 1, 10, 1, 1),
    _PrvtIgmpSnoopMemoryPoolId_Type()
)
prvtIgmpSnoopMemoryPoolId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    prvtIgmpSnoopMemoryPoolId.setStatus("current")
_PrvtIgmpSnoopMemoryPoolName_Type = OctetString
_PrvtIgmpSnoopMemoryPoolName_Object = MibTableColumn
prvtIgmpSnoopMemoryPoolName = _PrvtIgmpSnoopMemoryPoolName_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 135, 1, 1, 10, 1, 2),
    _PrvtIgmpSnoopMemoryPoolName_Type()
)
prvtIgmpSnoopMemoryPoolName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtIgmpSnoopMemoryPoolName.setStatus("current")
_PrvtIgmpSnoopMemoryTaken_Type = Unsigned32
_PrvtIgmpSnoopMemoryTaken_Object = MibTableColumn
prvtIgmpSnoopMemoryTaken = _PrvtIgmpSnoopMemoryTaken_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 135, 1, 1, 10, 1, 3),
    _PrvtIgmpSnoopMemoryTaken_Type()
)
prvtIgmpSnoopMemoryTaken.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtIgmpSnoopMemoryTaken.setStatus("current")
_PrvtIgmpSnoopMemoryFree_Type = Unsigned32
_PrvtIgmpSnoopMemoryFree_Object = MibTableColumn
prvtIgmpSnoopMemoryFree = _PrvtIgmpSnoopMemoryFree_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 135, 1, 1, 10, 1, 4),
    _PrvtIgmpSnoopMemoryFree_Type()
)
prvtIgmpSnoopMemoryFree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtIgmpSnoopMemoryFree.setStatus("current")
_PrvtIgmpSnoopMemoryToAllocate_Type = Unsigned32
_PrvtIgmpSnoopMemoryToAllocate_Object = MibTableColumn
prvtIgmpSnoopMemoryToAllocate = _PrvtIgmpSnoopMemoryToAllocate_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 135, 1, 1, 10, 1, 5),
    _PrvtIgmpSnoopMemoryToAllocate_Type()
)
prvtIgmpSnoopMemoryToAllocate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtIgmpSnoopMemoryToAllocate.setStatus("current")
_PrvtIgmpSnoopMemoryInitCount_Type = Unsigned32
_PrvtIgmpSnoopMemoryInitCount_Object = MibTableColumn
prvtIgmpSnoopMemoryInitCount = _PrvtIgmpSnoopMemoryInitCount_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 135, 1, 1, 10, 1, 6),
    _PrvtIgmpSnoopMemoryInitCount_Type()
)
prvtIgmpSnoopMemoryInitCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtIgmpSnoopMemoryInitCount.setStatus("current")
_PrvtIgmpSnoopMemorySize_Type = Unsigned32
_PrvtIgmpSnoopMemorySize_Object = MibTableColumn
prvtIgmpSnoopMemorySize = _PrvtIgmpSnoopMemorySize_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 135, 1, 1, 10, 1, 7),
    _PrvtIgmpSnoopMemorySize_Type()
)
prvtIgmpSnoopMemorySize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtIgmpSnoopMemorySize.setStatus("current")
_PrvtIgmpSnoopMemoryAllAllocated_Type = Unsigned32
_PrvtIgmpSnoopMemoryAllAllocated_Object = MibTableColumn
prvtIgmpSnoopMemoryAllAllocated = _PrvtIgmpSnoopMemoryAllAllocated_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 135, 1, 1, 10, 1, 8),
    _PrvtIgmpSnoopMemoryAllAllocated_Type()
)
prvtIgmpSnoopMemoryAllAllocated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtIgmpSnoopMemoryAllAllocated.setStatus("current")
_PrvtIgmpSnoopApplStatsObjects_ObjectIdentity = ObjectIdentity
prvtIgmpSnoopApplStatsObjects = _PrvtIgmpSnoopApplStatsObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 135, 1, 1, 11)
)
_PrvtIgmpSnoopCapturedPckts_Type = Unsigned32
_PrvtIgmpSnoopCapturedPckts_Object = MibScalar
prvtIgmpSnoopCapturedPckts = _PrvtIgmpSnoopCapturedPckts_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 135, 1, 1, 11, 1),
    _PrvtIgmpSnoopCapturedPckts_Type()
)
prvtIgmpSnoopCapturedPckts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtIgmpSnoopCapturedPckts.setStatus("current")
_PrvtIgmpSnoopCapturedReports_Type = Unsigned32
_PrvtIgmpSnoopCapturedReports_Object = MibScalar
prvtIgmpSnoopCapturedReports = _PrvtIgmpSnoopCapturedReports_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 135, 1, 1, 11, 2),
    _PrvtIgmpSnoopCapturedReports_Type()
)
prvtIgmpSnoopCapturedReports.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtIgmpSnoopCapturedReports.setStatus("current")
_PrvtIgmpSnoopUniqueSources_Type = Unsigned32
_PrvtIgmpSnoopUniqueSources_Object = MibScalar
prvtIgmpSnoopUniqueSources = _PrvtIgmpSnoopUniqueSources_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 135, 1, 1, 11, 3),
    _PrvtIgmpSnoopUniqueSources_Type()
)
prvtIgmpSnoopUniqueSources.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtIgmpSnoopUniqueSources.setStatus("current")
_PrvtIgmpSnoopUniqueGroupRecords_Type = Unsigned32
_PrvtIgmpSnoopUniqueGroupRecords_Object = MibScalar
prvtIgmpSnoopUniqueGroupRecords = _PrvtIgmpSnoopUniqueGroupRecords_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 135, 1, 1, 11, 4),
    _PrvtIgmpSnoopUniqueGroupRecords_Type()
)
prvtIgmpSnoopUniqueGroupRecords.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtIgmpSnoopUniqueGroupRecords.setStatus("current")
_PrvtIgmpSnoopDuplicateSources_Type = Unsigned32
_PrvtIgmpSnoopDuplicateSources_Object = MibScalar
prvtIgmpSnoopDuplicateSources = _PrvtIgmpSnoopDuplicateSources_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 135, 1, 1, 11, 5),
    _PrvtIgmpSnoopDuplicateSources_Type()
)
prvtIgmpSnoopDuplicateSources.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtIgmpSnoopDuplicateSources.setStatus("current")
_PrvtIgmpSnoopDuplicateGrpRecs_Type = Unsigned32
_PrvtIgmpSnoopDuplicateGrpRecs_Object = MibScalar
prvtIgmpSnoopDuplicateGrpRecs = _PrvtIgmpSnoopDuplicateGrpRecs_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 135, 1, 1, 11, 6),
    _PrvtIgmpSnoopDuplicateGrpRecs_Type()
)
prvtIgmpSnoopDuplicateGrpRecs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtIgmpSnoopDuplicateGrpRecs.setStatus("current")
_PrvtIgmpSnoopUniqueMacs_Type = Unsigned32
_PrvtIgmpSnoopUniqueMacs_Object = MibScalar
prvtIgmpSnoopUniqueMacs = _PrvtIgmpSnoopUniqueMacs_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 135, 1, 1, 11, 7),
    _PrvtIgmpSnoopUniqueMacs_Type()
)
prvtIgmpSnoopUniqueMacs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtIgmpSnoopUniqueMacs.setStatus("current")
_PrvtIgmpSnoopDuplicateMacs_Type = Unsigned32
_PrvtIgmpSnoopDuplicateMacs_Object = MibScalar
prvtIgmpSnoopDuplicateMacs = _PrvtIgmpSnoopDuplicateMacs_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 135, 1, 1, 11, 8),
    _PrvtIgmpSnoopDuplicateMacs_Type()
)
prvtIgmpSnoopDuplicateMacs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtIgmpSnoopDuplicateMacs.setStatus("current")
_PrvtIgmpSnoopUniqueHsis_Type = Unsigned32
_PrvtIgmpSnoopUniqueHsis_Object = MibScalar
prvtIgmpSnoopUniqueHsis = _PrvtIgmpSnoopUniqueHsis_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 135, 1, 1, 11, 9),
    _PrvtIgmpSnoopUniqueHsis_Type()
)
prvtIgmpSnoopUniqueHsis.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtIgmpSnoopUniqueHsis.setStatus("current")
_PrvtIgmpSnoopDuplicateHsis_Type = Unsigned32
_PrvtIgmpSnoopDuplicateHsis_Object = MibScalar
prvtIgmpSnoopDuplicateHsis = _PrvtIgmpSnoopDuplicateHsis_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 135, 1, 1, 11, 10),
    _PrvtIgmpSnoopDuplicateHsis_Type()
)
prvtIgmpSnoopDuplicateHsis.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtIgmpSnoopDuplicateHsis.setStatus("current")
_PrvtIgmpSnoopMvrObjects_ObjectIdentity = ObjectIdentity
prvtIgmpSnoopMvrObjects = _PrvtIgmpSnoopMvrObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 135, 1, 3)
)
_PrvtIgmpSnoopMvrShutdown_Type = TruthValue
_PrvtIgmpSnoopMvrShutdown_Object = MibScalar
prvtIgmpSnoopMvrShutdown = _PrvtIgmpSnoopMvrShutdown_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 135, 1, 3, 1),
    _PrvtIgmpSnoopMvrShutdown_Type()
)
prvtIgmpSnoopMvrShutdown.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prvtIgmpSnoopMvrShutdown.setStatus("current")


class _PrvtIgmpSnoopMvrMode_Type(Integer32):
    """Custom type prvtIgmpSnoopMvrMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("static", 1),
          ("dynamic", 2))
    )


_PrvtIgmpSnoopMvrMode_Type.__name__ = "Integer32"
_PrvtIgmpSnoopMvrMode_Object = MibScalar
prvtIgmpSnoopMvrMode = _PrvtIgmpSnoopMvrMode_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 135, 1, 3, 2),
    _PrvtIgmpSnoopMvrMode_Type()
)
prvtIgmpSnoopMvrMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prvtIgmpSnoopMvrMode.setStatus("current")


class _PrvtIgmpSnoopMvrVlan_Type(Integer32):
    """Custom type prvtIgmpSnoopMvrVlan based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4092),
    )


_PrvtIgmpSnoopMvrVlan_Type.__name__ = "Integer32"
_PrvtIgmpSnoopMvrVlan_Object = MibScalar
prvtIgmpSnoopMvrVlan = _PrvtIgmpSnoopMvrVlan_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 135, 1, 3, 3),
    _PrvtIgmpSnoopMvrVlan_Type()
)
prvtIgmpSnoopMvrVlan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prvtIgmpSnoopMvrVlan.setStatus("current")
_PrvtIgmpSnoopMvrSrcIp_Type = IpAddress
_PrvtIgmpSnoopMvrSrcIp_Object = MibScalar
prvtIgmpSnoopMvrSrcIp = _PrvtIgmpSnoopMvrSrcIp_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 135, 1, 3, 4),
    _PrvtIgmpSnoopMvrSrcIp_Type()
)
prvtIgmpSnoopMvrSrcIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prvtIgmpSnoopMvrSrcIp.setStatus("current")
_PrvtIgmpSnoopMvrGrpTable_Object = MibTable
prvtIgmpSnoopMvrGrpTable = _PrvtIgmpSnoopMvrGrpTable_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 135, 1, 3, 10)
)
if mibBuilder.loadTexts:
    prvtIgmpSnoopMvrGrpTable.setStatus("current")
_PrvtIgmpSnoopMvrGrpEntry_Object = MibTableRow
prvtIgmpSnoopMvrGrpEntry = _PrvtIgmpSnoopMvrGrpEntry_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 135, 1, 3, 10, 1)
)
prvtIgmpSnoopMvrGrpEntry.setIndexNames(
    (0, "PRVT-IGMP-SNOOPING-MIB", "prvtIgmpSnoopMvrGrpName"),
)
if mibBuilder.loadTexts:
    prvtIgmpSnoopMvrGrpEntry.setStatus("current")


class _PrvtIgmpSnoopMvrGrpName_Type(OctetString):
    """Custom type prvtIgmpSnoopMvrGrpName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_PrvtIgmpSnoopMvrGrpName_Type.__name__ = "OctetString"
_PrvtIgmpSnoopMvrGrpName_Object = MibTableColumn
prvtIgmpSnoopMvrGrpName = _PrvtIgmpSnoopMvrGrpName_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 135, 1, 3, 10, 1, 1),
    _PrvtIgmpSnoopMvrGrpName_Type()
)
prvtIgmpSnoopMvrGrpName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    prvtIgmpSnoopMvrGrpName.setStatus("current")
_PrvtIgmpSnoopMvrGrpRowStatus_Type = RowStatus
_PrvtIgmpSnoopMvrGrpRowStatus_Object = MibTableColumn
prvtIgmpSnoopMvrGrpRowStatus = _PrvtIgmpSnoopMvrGrpRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 135, 1, 3, 10, 1, 2),
    _PrvtIgmpSnoopMvrGrpRowStatus_Type()
)
prvtIgmpSnoopMvrGrpRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    prvtIgmpSnoopMvrGrpRowStatus.setStatus("current")
_PrvtIgmpSnoopMvrGrpAsmTable_Object = MibTable
prvtIgmpSnoopMvrGrpAsmTable = _PrvtIgmpSnoopMvrGrpAsmTable_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 135, 1, 3, 11)
)
if mibBuilder.loadTexts:
    prvtIgmpSnoopMvrGrpAsmTable.setStatus("current")
_PrvtIgmpSnoopMvrGrpAsmEntry_Object = MibTableRow
prvtIgmpSnoopMvrGrpAsmEntry = _PrvtIgmpSnoopMvrGrpAsmEntry_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 135, 1, 3, 11, 1)
)
prvtIgmpSnoopMvrGrpAsmEntry.setIndexNames(
    (0, "PRVT-IGMP-SNOOPING-MIB", "prvtIgmpSnoopMvrGrpName"),
    (0, "PRVT-IGMP-SNOOPING-MIB", "prvtIgmpSnoopMvrGrpAsmIndex"),
)
if mibBuilder.loadTexts:
    prvtIgmpSnoopMvrGrpAsmEntry.setStatus("current")


class _PrvtIgmpSnoopMvrGrpAsmIndex_Type(Unsigned32):
    """Custom type prvtIgmpSnoopMvrGrpAsmIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_PrvtIgmpSnoopMvrGrpAsmIndex_Type.__name__ = "Unsigned32"
_PrvtIgmpSnoopMvrGrpAsmIndex_Object = MibTableColumn
prvtIgmpSnoopMvrGrpAsmIndex = _PrvtIgmpSnoopMvrGrpAsmIndex_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 135, 1, 3, 11, 1, 1),
    _PrvtIgmpSnoopMvrGrpAsmIndex_Type()
)
prvtIgmpSnoopMvrGrpAsmIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    prvtIgmpSnoopMvrGrpAsmIndex.setStatus("current")
_PrvtIgmpSnoopMvrGrpAsmRowStatus_Type = RowStatus
_PrvtIgmpSnoopMvrGrpAsmRowStatus_Object = MibTableColumn
prvtIgmpSnoopMvrGrpAsmRowStatus = _PrvtIgmpSnoopMvrGrpAsmRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 135, 1, 3, 11, 1, 2),
    _PrvtIgmpSnoopMvrGrpAsmRowStatus_Type()
)
prvtIgmpSnoopMvrGrpAsmRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    prvtIgmpSnoopMvrGrpAsmRowStatus.setStatus("current")
_PrvtIgmpSnoopMvrGrpAsmAddr_Type = IpAddress
_PrvtIgmpSnoopMvrGrpAsmAddr_Object = MibTableColumn
prvtIgmpSnoopMvrGrpAsmAddr = _PrvtIgmpSnoopMvrGrpAsmAddr_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 135, 1, 3, 11, 1, 3),
    _PrvtIgmpSnoopMvrGrpAsmAddr_Type()
)
prvtIgmpSnoopMvrGrpAsmAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    prvtIgmpSnoopMvrGrpAsmAddr.setStatus("current")


class _PrvtIgmpSnoopMvrGrpAsmCount_Type(Unsigned32):
    """Custom type prvtIgmpSnoopMvrGrpAsmCount based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 256),
    )


_PrvtIgmpSnoopMvrGrpAsmCount_Type.__name__ = "Unsigned32"
_PrvtIgmpSnoopMvrGrpAsmCount_Object = MibTableColumn
prvtIgmpSnoopMvrGrpAsmCount = _PrvtIgmpSnoopMvrGrpAsmCount_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 135, 1, 3, 11, 1, 4),
    _PrvtIgmpSnoopMvrGrpAsmCount_Type()
)
prvtIgmpSnoopMvrGrpAsmCount.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    prvtIgmpSnoopMvrGrpAsmCount.setStatus("current")
_PrvtIgmpSnoopMvrGrpSsmTable_Object = MibTable
prvtIgmpSnoopMvrGrpSsmTable = _PrvtIgmpSnoopMvrGrpSsmTable_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 135, 1, 3, 12)
)
if mibBuilder.loadTexts:
    prvtIgmpSnoopMvrGrpSsmTable.setStatus("current")
_PrvtIgmpSnoopMvrGrpSsmEntry_Object = MibTableRow
prvtIgmpSnoopMvrGrpSsmEntry = _PrvtIgmpSnoopMvrGrpSsmEntry_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 135, 1, 3, 12, 1)
)
prvtIgmpSnoopMvrGrpSsmEntry.setIndexNames(
    (0, "PRVT-IGMP-SNOOPING-MIB", "prvtIgmpSnoopMvrGrpName"),
    (0, "PRVT-IGMP-SNOOPING-MIB", "prvtIgmpSnoopMvrGrpSsmIndex"),
)
if mibBuilder.loadTexts:
    prvtIgmpSnoopMvrGrpSsmEntry.setStatus("current")


class _PrvtIgmpSnoopMvrGrpSsmIndex_Type(Unsigned32):
    """Custom type prvtIgmpSnoopMvrGrpSsmIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_PrvtIgmpSnoopMvrGrpSsmIndex_Type.__name__ = "Unsigned32"
_PrvtIgmpSnoopMvrGrpSsmIndex_Object = MibTableColumn
prvtIgmpSnoopMvrGrpSsmIndex = _PrvtIgmpSnoopMvrGrpSsmIndex_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 135, 1, 3, 12, 1, 1),
    _PrvtIgmpSnoopMvrGrpSsmIndex_Type()
)
prvtIgmpSnoopMvrGrpSsmIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    prvtIgmpSnoopMvrGrpSsmIndex.setStatus("current")
_PrvtIgmpSnoopMvrGrpSsmRowStatus_Type = RowStatus
_PrvtIgmpSnoopMvrGrpSsmRowStatus_Object = MibTableColumn
prvtIgmpSnoopMvrGrpSsmRowStatus = _PrvtIgmpSnoopMvrGrpSsmRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 135, 1, 3, 12, 1, 2),
    _PrvtIgmpSnoopMvrGrpSsmRowStatus_Type()
)
prvtIgmpSnoopMvrGrpSsmRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    prvtIgmpSnoopMvrGrpSsmRowStatus.setStatus("current")
_PrvtIgmpSnoopMvrGrpSsmAddr_Type = IpAddress
_PrvtIgmpSnoopMvrGrpSsmAddr_Object = MibTableColumn
prvtIgmpSnoopMvrGrpSsmAddr = _PrvtIgmpSnoopMvrGrpSsmAddr_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 135, 1, 3, 12, 1, 3),
    _PrvtIgmpSnoopMvrGrpSsmAddr_Type()
)
prvtIgmpSnoopMvrGrpSsmAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    prvtIgmpSnoopMvrGrpSsmAddr.setStatus("current")
_PrvtIgmpSnoopMvrGrpSsmSrcList_Type = OctetString
_PrvtIgmpSnoopMvrGrpSsmSrcList_Object = MibTableColumn
prvtIgmpSnoopMvrGrpSsmSrcList = _PrvtIgmpSnoopMvrGrpSsmSrcList_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 135, 1, 3, 12, 1, 4),
    _PrvtIgmpSnoopMvrGrpSsmSrcList_Type()
)
prvtIgmpSnoopMvrGrpSsmSrcList.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    prvtIgmpSnoopMvrGrpSsmSrcList.setStatus("current")


class _PrvtIgmpSnoopMvrGrpSsmMode_Type(Integer32):
    """Custom type prvtIgmpSnoopMvrGrpSsmMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("include", 1),
          ("exclude", 2))
    )


_PrvtIgmpSnoopMvrGrpSsmMode_Type.__name__ = "Integer32"
_PrvtIgmpSnoopMvrGrpSsmMode_Object = MibTableColumn
prvtIgmpSnoopMvrGrpSsmMode = _PrvtIgmpSnoopMvrGrpSsmMode_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 135, 1, 3, 12, 1, 5),
    _PrvtIgmpSnoopMvrGrpSsmMode_Type()
)
prvtIgmpSnoopMvrGrpSsmMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    prvtIgmpSnoopMvrGrpSsmMode.setStatus("current")
_PrvtIgmpSnoopMvrPortTable_Object = MibTable
prvtIgmpSnoopMvrPortTable = _PrvtIgmpSnoopMvrPortTable_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 135, 1, 3, 13)
)
if mibBuilder.loadTexts:
    prvtIgmpSnoopMvrPortTable.setStatus("current")
_PrvtIgmpSnoopMvrPortEntry_Object = MibTableRow
prvtIgmpSnoopMvrPortEntry = _PrvtIgmpSnoopMvrPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 135, 1, 3, 13, 1)
)
prvtIgmpSnoopMvrPortEntry.setIndexNames(
    (0, "PRVT-IGMP-SNOOPING-MIB", "prvtIgmpSnoopCfgIfName"),
)
if mibBuilder.loadTexts:
    prvtIgmpSnoopMvrPortEntry.setStatus("current")
_PrvtIgmpSnoopMvrPortRowStatus_Type = RowStatus
_PrvtIgmpSnoopMvrPortRowStatus_Object = MibTableColumn
prvtIgmpSnoopMvrPortRowStatus = _PrvtIgmpSnoopMvrPortRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 135, 1, 3, 13, 1, 1),
    _PrvtIgmpSnoopMvrPortRowStatus_Type()
)
prvtIgmpSnoopMvrPortRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    prvtIgmpSnoopMvrPortRowStatus.setStatus("current")


class _PrvtIgmpSnoopMvrPortType_Type(Integer32):
    """Custom type prvtIgmpSnoopMvrPortType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("source", 1),
          ("receiver", 2))
    )


_PrvtIgmpSnoopMvrPortType_Type.__name__ = "Integer32"
_PrvtIgmpSnoopMvrPortType_Object = MibTableColumn
prvtIgmpSnoopMvrPortType = _PrvtIgmpSnoopMvrPortType_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 135, 1, 3, 13, 1, 2),
    _PrvtIgmpSnoopMvrPortType_Type()
)
prvtIgmpSnoopMvrPortType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    prvtIgmpSnoopMvrPortType.setStatus("current")
_PrvtIgmpSnoopMvrPortExpTrack_Type = TruthValue
_PrvtIgmpSnoopMvrPortExpTrack_Object = MibTableColumn
prvtIgmpSnoopMvrPortExpTrack = _PrvtIgmpSnoopMvrPortExpTrack_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 135, 1, 3, 13, 1, 3),
    _PrvtIgmpSnoopMvrPortExpTrack_Type()
)
prvtIgmpSnoopMvrPortExpTrack.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    prvtIgmpSnoopMvrPortExpTrack.setStatus("current")
_PrvtIgmpSnoopMvrPortFastLeave_Type = TruthValue
_PrvtIgmpSnoopMvrPortFastLeave_Object = MibTableColumn
prvtIgmpSnoopMvrPortFastLeave = _PrvtIgmpSnoopMvrPortFastLeave_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 135, 1, 3, 13, 1, 4),
    _PrvtIgmpSnoopMvrPortFastLeave_Type()
)
prvtIgmpSnoopMvrPortFastLeave.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    prvtIgmpSnoopMvrPortFastLeave.setStatus("current")
_PrvtIgmpSnoopMvrPortMcGrpTable_Object = MibTable
prvtIgmpSnoopMvrPortMcGrpTable = _PrvtIgmpSnoopMvrPortMcGrpTable_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 135, 1, 3, 14)
)
if mibBuilder.loadTexts:
    prvtIgmpSnoopMvrPortMcGrpTable.setStatus("current")
_PrvtIgmpSnoopMvrPortMcGrpEntry_Object = MibTableRow
prvtIgmpSnoopMvrPortMcGrpEntry = _PrvtIgmpSnoopMvrPortMcGrpEntry_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 135, 1, 3, 14, 1)
)
prvtIgmpSnoopMvrPortMcGrpEntry.setIndexNames(
    (0, "PRVT-IGMP-SNOOPING-MIB", "prvtIgmpSnoopCfgIfName"),
    (0, "PRVT-IGMP-SNOOPING-MIB", "prvtIgmpSnoopMvrGrpName"),
)
if mibBuilder.loadTexts:
    prvtIgmpSnoopMvrPortMcGrpEntry.setStatus("current")
_PrvtIgmpSnoopMvrPortMcGrpRStatus_Type = RowStatus
_PrvtIgmpSnoopMvrPortMcGrpRStatus_Object = MibTableColumn
prvtIgmpSnoopMvrPortMcGrpRStatus = _PrvtIgmpSnoopMvrPortMcGrpRStatus_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 135, 1, 3, 14, 1, 1),
    _PrvtIgmpSnoopMvrPortMcGrpRStatus_Type()
)
prvtIgmpSnoopMvrPortMcGrpRStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    prvtIgmpSnoopMvrPortMcGrpRStatus.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "PRVT-IGMP-SNOOPING-MIB",
    **{"prvtIgmpSnoopingMIB": prvtIgmpSnoopingMIB,
       "prvtIgmpSnoopMIBObjects": prvtIgmpSnoopMIBObjects,
       "prvtIgmpSnoopObjects": prvtIgmpSnoopObjects,
       "prvtIgmpSnoopCfgTable": prvtIgmpSnoopCfgTable,
       "prvtIgmpSnoopCfgEntry": prvtIgmpSnoopCfgEntry,
       "prvtIgmpSnoopCfgSvcType": prvtIgmpSnoopCfgSvcType,
       "prvtIgmpSnoopCfgSvcId": prvtIgmpSnoopCfgSvcId,
       "prvtIgmpSnoopCfgRowStatus": prvtIgmpSnoopCfgRowStatus,
       "prvtIgmpSnoopCfgEnable": prvtIgmpSnoopCfgEnable,
       "prvtIgmpSnoopCfgRouterAlertCheck": prvtIgmpSnoopCfgRouterAlertCheck,
       "prvtIgmpSnoopCfgIpTosCheck": prvtIgmpSnoopCfgIpTosCheck,
       "prvtIgmpSnoopCfgFloodOnFlush": prvtIgmpSnoopCfgFloodOnFlush,
       "prvtIgmpSnoopCfgTmrRobustness": prvtIgmpSnoopCfgTmrRobustness,
       "prvtIgmpSnoopCfgTmrQIntvl": prvtIgmpSnoopCfgTmrQIntvl,
       "prvtIgmpSnoopCfgTmrQRespIntvl": prvtIgmpSnoopCfgTmrQRespIntvl,
       "prvtIgmpSnoopCfgTmrLastMbrQIntvl": prvtIgmpSnoopCfgTmrLastMbrQIntvl,
       "prvtIgmpSnoopCfgMode": prvtIgmpSnoopCfgMode,
       "prvtIgmpSnoopCfgSourceAddr": prvtIgmpSnoopCfgSourceAddr,
       "prvtIgmpSnoopCfgIfTable": prvtIgmpSnoopCfgIfTable,
       "prvtIgmpSnoopCfgIfEntry": prvtIgmpSnoopCfgIfEntry,
       "prvtIgmpSnoopCfgIfType": prvtIgmpSnoopCfgIfType,
       "prvtIgmpSnoopCfgIfName": prvtIgmpSnoopCfgIfName,
       "prvtIgmpSnoopCfgIfRowStatus": prvtIgmpSnoopCfgIfRowStatus,
       "prvtIgmpSnoopCfgIfMaxGroups": prvtIgmpSnoopCfgIfMaxGroups,
       "prvtIgmpSnoopCfgIfMRouter": prvtIgmpSnoopCfgIfMRouter,
       "prvtIgmpSnoopCfgIfMRouterBlock": prvtIgmpSnoopCfgIfMRouterBlock,
       "prvtIgmpSnoopCfgIfExplctTracking": prvtIgmpSnoopCfgIfExplctTracking,
       "prvtIgmpSnoopCfgIfFastLeave": prvtIgmpSnoopCfgIfFastLeave,
       "prvtIgmpSnoopCfgIfReportBlock": prvtIgmpSnoopCfgIfReportBlock,
       "prvtIgmpSnoopCfgIfForceFwd": prvtIgmpSnoopCfgIfForceFwd,
       "prvtIgmpSnoopCfgIfMrtAllowRprts": prvtIgmpSnoopCfgIfMrtAllowRprts,
       "prvtIgmpSnoopCfgIfQuerier": prvtIgmpSnoopCfgIfQuerier,
       "prvtIgmpSnoopDbGrpTable": prvtIgmpSnoopDbGrpTable,
       "prvtIgmpSnoopDbGrpEntry": prvtIgmpSnoopDbGrpEntry,
       "prvtIgmpSnoopDbGrpIpAddr": prvtIgmpSnoopDbGrpIpAddr,
       "prvtIgmpSnoopDbGrpBitFlags": prvtIgmpSnoopDbGrpBitFlags,
       "prvtIgmpSnoopDbGrpFilterMode": prvtIgmpSnoopDbGrpFilterMode,
       "prvtIgmpSnoopDbGrpExpireTime": prvtIgmpSnoopDbGrpExpireTime,
       "prvtIgmpSnoopDbGrpHostTable": prvtIgmpSnoopDbGrpHostTable,
       "prvtIgmpSnoopDbGrpHostEntry": prvtIgmpSnoopDbGrpHostEntry,
       "prvtIgmpSnoopDbGrpHostSourceIp": prvtIgmpSnoopDbGrpHostSourceIp,
       "prvtIgmpSnoopDbGrpHostExpireTime": prvtIgmpSnoopDbGrpHostExpireTime,
       "prvtIgmpSnoopDbGrpSrcTable": prvtIgmpSnoopDbGrpSrcTable,
       "prvtIgmpSnoopDbGrpSrcEntry": prvtIgmpSnoopDbGrpSrcEntry,
       "prvtIgmpSnoopDbGrpSrcIpAddr": prvtIgmpSnoopDbGrpSrcIpAddr,
       "prvtIgmpSnoopDbGrpSrcExpTime": prvtIgmpSnoopDbGrpSrcExpTime,
       "prvtIgmpSnoopDbGrpSrcHostTable": prvtIgmpSnoopDbGrpSrcHostTable,
       "prvtIgmpSnoopDbGrpSrcHostEntry": prvtIgmpSnoopDbGrpSrcHostEntry,
       "prvtIgmpSnoopDbGrpSrcHostIp": prvtIgmpSnoopDbGrpSrcHostIp,
       "prvtIgmpSnoopDbGrpSrcHostExpTime": prvtIgmpSnoopDbGrpSrcHostExpTime,
       "prvtIgmpSnoopDbMrtrTable": prvtIgmpSnoopDbMrtrTable,
       "prvtIgmpSnoopDbMrtrEntry": prvtIgmpSnoopDbMrtrEntry,
       "prvtIgmpSnoopDbMrtrSrcIp": prvtIgmpSnoopDbMrtrSrcIp,
       "prvtIgmpSnoopDbMrtrFlags": prvtIgmpSnoopDbMrtrFlags,
       "prvtIgmpSnoopDbMrtrExpTime": prvtIgmpSnoopDbMrtrExpTime,
       "prvtIgmpSnoopDbGrpStatsTable": prvtIgmpSnoopDbGrpStatsTable,
       "prvtIgmpSnoopDbGrpStatsEntry": prvtIgmpSnoopDbGrpStatsEntry,
       "prvtIgmpSnoopDbGrpStatsVlanId": prvtIgmpSnoopDbGrpStatsVlanId,
       "prvtIgmpSnoopDbGrpStatsDscPkt": prvtIgmpSnoopDbGrpStatsDscPkt,
       "prvtIgmpSnoopDbGrpStatsDscPktTtl": prvtIgmpSnoopDbGrpStatsDscPktTtl,
       "prvtIgmpSnoopDbGrpStatsDscPktChk": prvtIgmpSnoopDbGrpStatsDscPktChk,
       "prvtIgmpSnoopDbGrpStatsDscPktRA": prvtIgmpSnoopDbGrpStatsDscPktRA,
       "prvtIgmpSnoopDbIfStatsTable": prvtIgmpSnoopDbIfStatsTable,
       "prvtIgmpSnoopDbIfStatsEntry": prvtIgmpSnoopDbIfStatsEntry,
       "prvtIgmpSnoopDbIfStatsIfName": prvtIgmpSnoopDbIfStatsIfName,
       "prvtIgmpSnoopDbIfStatsV2Reports": prvtIgmpSnoopDbIfStatsV2Reports,
       "prvtIgmpSnoopDbIfStatsV2Leaves": prvtIgmpSnoopDbIfStatsV2Leaves,
       "prvtIgmpSnoopDbIfStatsV3Reports": prvtIgmpSnoopDbIfStatsV3Reports,
       "prvtIgmpSnoopDbIfStatsGenQueries": prvtIgmpSnoopDbIfStatsGenQueries,
       "prvtIgmpSnoopDbIfStatsGrpQueries": prvtIgmpSnoopDbIfStatsGrpQueries,
       "prvtIgmpSnoopDbIfStatsSrcQueries": prvtIgmpSnoopDbIfStatsSrcQueries,
       "prvtIgmpSnoopMemoryTable": prvtIgmpSnoopMemoryTable,
       "prvtIgmpSnoopMemoryEntry": prvtIgmpSnoopMemoryEntry,
       "prvtIgmpSnoopMemoryPoolId": prvtIgmpSnoopMemoryPoolId,
       "prvtIgmpSnoopMemoryPoolName": prvtIgmpSnoopMemoryPoolName,
       "prvtIgmpSnoopMemoryTaken": prvtIgmpSnoopMemoryTaken,
       "prvtIgmpSnoopMemoryFree": prvtIgmpSnoopMemoryFree,
       "prvtIgmpSnoopMemoryToAllocate": prvtIgmpSnoopMemoryToAllocate,
       "prvtIgmpSnoopMemoryInitCount": prvtIgmpSnoopMemoryInitCount,
       "prvtIgmpSnoopMemorySize": prvtIgmpSnoopMemorySize,
       "prvtIgmpSnoopMemoryAllAllocated": prvtIgmpSnoopMemoryAllAllocated,
       "prvtIgmpSnoopApplStatsObjects": prvtIgmpSnoopApplStatsObjects,
       "prvtIgmpSnoopCapturedPckts": prvtIgmpSnoopCapturedPckts,
       "prvtIgmpSnoopCapturedReports": prvtIgmpSnoopCapturedReports,
       "prvtIgmpSnoopUniqueSources": prvtIgmpSnoopUniqueSources,
       "prvtIgmpSnoopUniqueGroupRecords": prvtIgmpSnoopUniqueGroupRecords,
       "prvtIgmpSnoopDuplicateSources": prvtIgmpSnoopDuplicateSources,
       "prvtIgmpSnoopDuplicateGrpRecs": prvtIgmpSnoopDuplicateGrpRecs,
       "prvtIgmpSnoopUniqueMacs": prvtIgmpSnoopUniqueMacs,
       "prvtIgmpSnoopDuplicateMacs": prvtIgmpSnoopDuplicateMacs,
       "prvtIgmpSnoopUniqueHsis": prvtIgmpSnoopUniqueHsis,
       "prvtIgmpSnoopDuplicateHsis": prvtIgmpSnoopDuplicateHsis,
       "prvtIgmpSnoopMvrObjects": prvtIgmpSnoopMvrObjects,
       "prvtIgmpSnoopMvrShutdown": prvtIgmpSnoopMvrShutdown,
       "prvtIgmpSnoopMvrMode": prvtIgmpSnoopMvrMode,
       "prvtIgmpSnoopMvrVlan": prvtIgmpSnoopMvrVlan,
       "prvtIgmpSnoopMvrSrcIp": prvtIgmpSnoopMvrSrcIp,
       "prvtIgmpSnoopMvrGrpTable": prvtIgmpSnoopMvrGrpTable,
       "prvtIgmpSnoopMvrGrpEntry": prvtIgmpSnoopMvrGrpEntry,
       "prvtIgmpSnoopMvrGrpName": prvtIgmpSnoopMvrGrpName,
       "prvtIgmpSnoopMvrGrpRowStatus": prvtIgmpSnoopMvrGrpRowStatus,
       "prvtIgmpSnoopMvrGrpAsmTable": prvtIgmpSnoopMvrGrpAsmTable,
       "prvtIgmpSnoopMvrGrpAsmEntry": prvtIgmpSnoopMvrGrpAsmEntry,
       "prvtIgmpSnoopMvrGrpAsmIndex": prvtIgmpSnoopMvrGrpAsmIndex,
       "prvtIgmpSnoopMvrGrpAsmRowStatus": prvtIgmpSnoopMvrGrpAsmRowStatus,
       "prvtIgmpSnoopMvrGrpAsmAddr": prvtIgmpSnoopMvrGrpAsmAddr,
       "prvtIgmpSnoopMvrGrpAsmCount": prvtIgmpSnoopMvrGrpAsmCount,
       "prvtIgmpSnoopMvrGrpSsmTable": prvtIgmpSnoopMvrGrpSsmTable,
       "prvtIgmpSnoopMvrGrpSsmEntry": prvtIgmpSnoopMvrGrpSsmEntry,
       "prvtIgmpSnoopMvrGrpSsmIndex": prvtIgmpSnoopMvrGrpSsmIndex,
       "prvtIgmpSnoopMvrGrpSsmRowStatus": prvtIgmpSnoopMvrGrpSsmRowStatus,
       "prvtIgmpSnoopMvrGrpSsmAddr": prvtIgmpSnoopMvrGrpSsmAddr,
       "prvtIgmpSnoopMvrGrpSsmSrcList": prvtIgmpSnoopMvrGrpSsmSrcList,
       "prvtIgmpSnoopMvrGrpSsmMode": prvtIgmpSnoopMvrGrpSsmMode,
       "prvtIgmpSnoopMvrPortTable": prvtIgmpSnoopMvrPortTable,
       "prvtIgmpSnoopMvrPortEntry": prvtIgmpSnoopMvrPortEntry,
       "prvtIgmpSnoopMvrPortRowStatus": prvtIgmpSnoopMvrPortRowStatus,
       "prvtIgmpSnoopMvrPortType": prvtIgmpSnoopMvrPortType,
       "prvtIgmpSnoopMvrPortExpTrack": prvtIgmpSnoopMvrPortExpTrack,
       "prvtIgmpSnoopMvrPortFastLeave": prvtIgmpSnoopMvrPortFastLeave,
       "prvtIgmpSnoopMvrPortMcGrpTable": prvtIgmpSnoopMvrPortMcGrpTable,
       "prvtIgmpSnoopMvrPortMcGrpEntry": prvtIgmpSnoopMvrPortMcGrpEntry,
       "prvtIgmpSnoopMvrPortMcGrpRStatus": prvtIgmpSnoopMvrPortMcGrpRStatus}
)
