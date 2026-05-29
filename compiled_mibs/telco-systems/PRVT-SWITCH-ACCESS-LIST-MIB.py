# SNMP MIB module (PRVT-SWITCH-ACCESS-LIST-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\telco-systems\binos\PRVT-SWITCH-ACCESS-LIST-MIB

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

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

(sapEncapValue,
 sapPortId,
 sdpId,
 svcId) = mibBuilder.importSymbols(
    "PRVT-SERV-MIB",
    "sapEncapValue",
    "sapPortId",
    "sdpId",
    "svcId")

(ipSwitch,) = mibBuilder.importSymbols(
    "PRVT-SWITCH-MIB",
    "ipSwitch")

(dot1qVlanIndex,
 dot1qVlanStatus) = mibBuilder.importSymbols(
    "Q-BRIDGE-MIB",
    "dot1qVlanIndex",
    "dot1qVlanStatus")

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

(DisplayString,
 MacAddress,
 PhysAddress,
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

prvtSwitchAccessListMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 1)
)
if mibBuilder.loadTexts:
    prvtSwitchAccessListMib.setRevisions(
        ("2011-02-07 00:00",
         "2010-11-16 00:00",
         "2010-11-03 00:00",
         "2009-04-17 00:00",
         "2008-11-20 00:00",
         "2008-02-14 00:00",
         "2008-01-01 00:00",
         "2007-12-05 00:00",
         "2006-03-22 00:00",
         "2005-10-03 00:00",
         "2005-09-30 00:00",
         "2005-02-28 00:00",
         "2005-02-24 00:00",
         "2005-02-16 00:00",
         "2004-12-15 00:00",
         "2003-10-15 00:00",
         "2003-05-08 00:00",
         "2002-11-12 00:00",
         "2001-11-05 00:00",
         "2001-09-30 00:00",
         "2001-08-27 00:00",
         "2001-07-31 00:00",
         "2001-05-14 00:00",
         "2001-02-20 00:00",
         "2001-02-15 00:00",
         "2001-01-28 00:00",
         "2000-11-13 09:59")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class AccessListAction(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              100)
        )
    )
    namedValues = NamedValues(
        *(("permit", 0),
          ("deny", 1),
          ("shaper", 2),
          ("remark", 3),
          ("undefined", 100))
    )



class IpProtocol(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )



class PortDef(TextualConvention, Integer32):
    status = "current"
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
        *(("undefined", 0),
          ("equal", 1),
          ("range", 2),
          ("greater-than", 3),
          ("less-than", 4))
    )



class Rate(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(13, 1000000),
    )



class ExceedAction(TextualConvention, Integer32):
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
        *(("drop", 0),
          ("markDiscardable", 1),
          ("undefined", 2),
          ("green", 3),
          ("yellow", 4),
          ("red", 5))
    )



class VlanTag(TextualConvention, Integer32):
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
        *(("untagged", 0),
          ("tagged", 1),
          ("undefined", 2))
    )



class ISPType(TextualConvention, Integer32):
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
        *(("connectivity", 0),
          ("normal", 1),
          ("routed", 2))
    )



class Shaper(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )



class ConformAction(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            0
        )
    )
    namedValues = NamedValues(
        ("transmit", 0)
    )



class AssigenValue(TextualConvention, Integer32):
    status = "current"
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



class AccessListModifyTos(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )



class AccessListEstablished(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )



class AccessListDiscard(TextualConvention, Integer32):
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
        *(("normal", 0),
          ("discardable", 1),
          ("green", 2),
          ("yellow", 3),
          ("red", 4),
          ("undefined", 5))
    )



class AccessListRemarkString(TextualConvention, OctetString):
    status = "current"
    displayHint = "40a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )



class TxqDropLevel(TextualConvention, Integer32):
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
        *(("undefined", 0),
          ("green", 1),
          ("yellow", 2))
    )



class MatchTraffic(TextualConvention, Integer32):
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
        *(("undefined", 0),
          ("untagged", 1),
          ("unknown-unicast", 2),
          ("multicast", 3),
          ("broadcast", 4),
          ("known-unicast", 5))
    )



class AccessListStatistics(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )



class AccessListDirection(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("ingress", 0),
          ("egress", 1))
    )



# MIB Managed Objects in the order of their OIDs

_PrvtSwitchAccessListNotifications_ObjectIdentity = ObjectIdentity
prvtSwitchAccessListNotifications = _PrvtSwitchAccessListNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 1, 0)
)
_AccessLists_ObjectIdentity = ObjectIdentity
accessLists = _AccessLists_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 1, 1)
)


class _AccessListTemplate_Type(Integer32):
    """Custom type accessListTemplate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("standard", 1),
          ("vlan-priority", 2))
    )


_AccessListTemplate_Type.__name__ = "Integer32"
_AccessListTemplate_Object = MibScalar
accessListTemplate = _AccessListTemplate_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 1, 1, 1),
    _AccessListTemplate_Type()
)
accessListTemplate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accessListTemplate.setStatus("current")
_AccessGroupsDefinitions_ObjectIdentity = ObjectIdentity
accessGroupsDefinitions = _AccessGroupsDefinitions_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 1, 1, 2)
)
_AccessListControlTable_Object = MibTable
accessListControlTable = _AccessListControlTable_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 1, 1, 2, 1)
)
if mibBuilder.loadTexts:
    accessListControlTable.setStatus("current")
_AccessListControlEntry_Object = MibTableRow
accessListControlEntry = _AccessListControlEntry_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 1, 1, 2, 1, 1)
)
accessListControlEntry.setIndexNames(
    (0, "PRVT-SWITCH-ACCESS-LIST-MIB", "accessListControlListGroup"),
)
if mibBuilder.loadTexts:
    accessListControlEntry.setStatus("current")


class _AccessListControlListGroup_Type(Integer32):
    """Custom type accessListControlListGroup based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_AccessListControlListGroup_Type.__name__ = "Integer32"
_AccessListControlListGroup_Object = MibTableColumn
accessListControlListGroup = _AccessListControlListGroup_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 1, 1, 2, 1, 1, 1),
    _AccessListControlListGroup_Type()
)
accessListControlListGroup.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    accessListControlListGroup.setStatus("current")
_AccessListControlRowStatus_Type = RowStatus
_AccessListControlRowStatus_Object = MibTableColumn
accessListControlRowStatus = _AccessListControlRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 1, 1, 2, 1, 1, 2),
    _AccessListControlRowStatus_Type()
)
accessListControlRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    accessListControlRowStatus.setStatus("current")
_StandardAccessListTable_Object = MibTable
standardAccessListTable = _StandardAccessListTable_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 1, 1, 2, 2)
)
if mibBuilder.loadTexts:
    standardAccessListTable.setStatus("current")
_StandardAccessListEntry_Object = MibTableRow
standardAccessListEntry = _StandardAccessListEntry_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 1, 1, 2, 2, 1)
)
standardAccessListEntry.setIndexNames(
    (0, "PRVT-SWITCH-ACCESS-LIST-MIB", "accessListControlListGroup"),
    (0, "PRVT-SWITCH-ACCESS-LIST-MIB", "standardAccessListIndex"),
)
if mibBuilder.loadTexts:
    standardAccessListEntry.setStatus("current")


class _StandardAccessListIndex_Type(Integer32):
    """Custom type standardAccessListIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_StandardAccessListIndex_Type.__name__ = "Integer32"
_StandardAccessListIndex_Object = MibTableColumn
standardAccessListIndex = _StandardAccessListIndex_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 1, 1, 2, 2, 1, 1),
    _StandardAccessListIndex_Type()
)
standardAccessListIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    standardAccessListIndex.setStatus("current")
_StandardAccessListAction_Type = AccessListAction
_StandardAccessListAction_Object = MibTableColumn
standardAccessListAction = _StandardAccessListAction_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 1, 1, 2, 2, 1, 2),
    _StandardAccessListAction_Type()
)
standardAccessListAction.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    standardAccessListAction.setStatus("current")
_StandardAccessListIpSrc_Type = IpAddress
_StandardAccessListIpSrc_Object = MibTableColumn
standardAccessListIpSrc = _StandardAccessListIpSrc_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 1, 1, 2, 2, 1, 3),
    _StandardAccessListIpSrc_Type()
)
standardAccessListIpSrc.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    standardAccessListIpSrc.setStatus("current")
_StandardAccessListIpMASKsrc_Type = IpAddress
_StandardAccessListIpMASKsrc_Object = MibTableColumn
standardAccessListIpMASKsrc = _StandardAccessListIpMASKsrc_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 1, 1, 2, 2, 1, 4),
    _StandardAccessListIpMASKsrc_Type()
)
standardAccessListIpMASKsrc.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    standardAccessListIpMASKsrc.setStatus("current")
_StandardAccessListRemark_Type = AccessListRemarkString
_StandardAccessListRemark_Object = MibTableColumn
standardAccessListRemark = _StandardAccessListRemark_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 1, 1, 2, 2, 1, 5),
    _StandardAccessListRemark_Type()
)
standardAccessListRemark.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    standardAccessListRemark.setStatus("current")


class _StandardAccessListLog_Type(Integer32):
    """Custom type standardAccessListLog based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("undefined", 0),
          ("log", 1),
          ("log-input", 2))
    )


_StandardAccessListLog_Type.__name__ = "Integer32"
_StandardAccessListLog_Object = MibTableColumn
standardAccessListLog = _StandardAccessListLog_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 1, 1, 2, 2, 1, 6),
    _StandardAccessListLog_Type()
)
standardAccessListLog.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    standardAccessListLog.setStatus("current")


class _StandardAccessListVpt_Type(Integer32):
    """Custom type standardAccessListVpt based on Integer32"""
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
              241,
              242,
              243,
              244,
              245,
              246,
              247,
              248)
        )
    )
    namedValues = NamedValues(
        *(("vpt-value0", 0),
          ("vpt-value1", 1),
          ("vpt-value2", 2),
          ("vpt-value3", 3),
          ("vpt-value4", 4),
          ("vpt-value5", 5),
          ("vpt-value6", 6),
          ("vpt-value7", 7),
          ("undefined", 8),
          ("fc-be", 241),
          ("fc-l2", 242),
          ("fc-af", 243),
          ("fc-l1", 244),
          ("fc-h2", 245),
          ("fc-ef", 246),
          ("fc-h1", 247),
          ("fc-nc", 248))
    )


_StandardAccessListVpt_Type.__name__ = "Integer32"
_StandardAccessListVpt_Object = MibTableColumn
standardAccessListVpt = _StandardAccessListVpt_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 1, 1, 2, 2, 1, 7),
    _StandardAccessListVpt_Type()
)
standardAccessListVpt.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    standardAccessListVpt.setStatus("current")
_StandardAccessListRowStatus_Type = RowStatus
_StandardAccessListRowStatus_Object = MibTableColumn
standardAccessListRowStatus = _StandardAccessListRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 1, 1, 2, 2, 1, 8),
    _StandardAccessListRowStatus_Type()
)
standardAccessListRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    standardAccessListRowStatus.setStatus("current")


class _StandardAccessListVlanId_Type(Integer32):
    """Custom type standardAccessListVlanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4092),
    )


_StandardAccessListVlanId_Type.__name__ = "Integer32"
_StandardAccessListVlanId_Object = MibTableColumn
standardAccessListVlanId = _StandardAccessListVlanId_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 1, 1, 2, 2, 1, 9),
    _StandardAccessListVlanId_Type()
)
standardAccessListVlanId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    standardAccessListVlanId.setStatus("current")
_StandardAccessListVlanMask_Type = DisplayString
_StandardAccessListVlanMask_Object = MibTableColumn
standardAccessListVlanMask = _StandardAccessListVlanMask_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 1, 1, 2, 2, 1, 10),
    _StandardAccessListVlanMask_Type()
)
standardAccessListVlanMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    standardAccessListVlanMask.setStatus("current")


class _StandardAccessListProviderVlanId_Type(Integer32):
    """Custom type standardAccessListProviderVlanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4092),
    )


_StandardAccessListProviderVlanId_Type.__name__ = "Integer32"
_StandardAccessListProviderVlanId_Object = MibTableColumn
standardAccessListProviderVlanId = _StandardAccessListProviderVlanId_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 1, 1, 2, 2, 1, 11),
    _StandardAccessListProviderVlanId_Type()
)
standardAccessListProviderVlanId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    standardAccessListProviderVlanId.setStatus("current")
_StandardAccessListProviderVlanMask_Type = DisplayString
_StandardAccessListProviderVlanMask_Object = MibTableColumn
standardAccessListProviderVlanMask = _StandardAccessListProviderVlanMask_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 1, 1, 2, 2, 1, 12),
    _StandardAccessListProviderVlanMask_Type()
)
standardAccessListProviderVlanMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    standardAccessListProviderVlanMask.setStatus("current")


class _StandardAccessListProviderVpt_Type(Integer32):
    """Custom type standardAccessListProviderVpt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8),
    )


_StandardAccessListProviderVpt_Type.__name__ = "Integer32"
_StandardAccessListProviderVpt_Object = MibTableColumn
standardAccessListProviderVpt = _StandardAccessListProviderVpt_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 1, 1, 2, 2, 1, 13),
    _StandardAccessListProviderVpt_Type()
)
standardAccessListProviderVpt.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    standardAccessListProviderVpt.setStatus("current")
_StandardAccessListUntaggedMode_Type = TruthValue
_StandardAccessListUntaggedMode_Object = MibTableColumn
standardAccessListUntaggedMode = _StandardAccessListUntaggedMode_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 1, 1, 2, 2, 1, 14),
    _StandardAccessListUntaggedMode_Type()
)
standardAccessListUntaggedMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    standardAccessListUntaggedMode.setStatus("current")


class _StandardAccessListDropLevel_Type(Integer32):
    """Custom type standardAccessListDropLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("green", 0),
          ("yellow", 1))
    )


_StandardAccessListDropLevel_Type.__name__ = "Integer32"
_StandardAccessListDropLevel_Object = MibTableColumn
standardAccessListDropLevel = _StandardAccessListDropLevel_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 1, 1, 2, 2, 1, 15),
    _StandardAccessListDropLevel_Type()
)
standardAccessListDropLevel.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    standardAccessListDropLevel.setStatus("current")


class _StandardAccessListDscp_Type(Integer32):
    """Custom type standardAccessListDscp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_StandardAccessListDscp_Type.__name__ = "Integer32"
_StandardAccessListDscp_Object = MibTableColumn
standardAccessListDscp = _StandardAccessListDscp_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 1, 1, 2, 2, 1, 16),
    _StandardAccessListDscp_Type()
)
standardAccessListDscp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    standardAccessListDscp.setStatus("current")
_ExtendedAccessListTable_Object = MibTable
extendedAccessListTable = _ExtendedAccessListTable_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 1, 1, 2, 3)
)
if mibBuilder.loadTexts:
    extendedAccessListTable.setStatus("current")
_ExtendedAccessListEntry_Object = MibTableRow
extendedAccessListEntry = _ExtendedAccessListEntry_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 1, 1, 2, 3, 1)
)
extendedAccessListEntry.setIndexNames(
    (0, "PRVT-SWITCH-ACCESS-LIST-MIB", "accessListControlListGroup"),
    (0, "PRVT-SWITCH-ACCESS-LIST-MIB", "extendedAccessListIndex"),
)
if mibBuilder.loadTexts:
    extendedAccessListEntry.setStatus("current")


class _ExtendedAccessListIndex_Type(Integer32):
    """Custom type extendedAccessListIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_ExtendedAccessListIndex_Type.__name__ = "Integer32"
_ExtendedAccessListIndex_Object = MibTableColumn
extendedAccessListIndex = _ExtendedAccessListIndex_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 1, 1, 2, 3, 1, 1),
    _ExtendedAccessListIndex_Type()
)
extendedAccessListIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    extendedAccessListIndex.setStatus("current")
_ExtendedAccessListAction_Type = AccessListAction
_ExtendedAccessListAction_Object = MibTableColumn
extendedAccessListAction = _ExtendedAccessListAction_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 1, 1, 2, 3, 1, 2),
    _ExtendedAccessListAction_Type()
)
extendedAccessListAction.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    extendedAccessListAction.setStatus("current")
_ExtendedAccessListIpProtocol_Type = IpProtocol
_ExtendedAccessListIpProtocol_Object = MibTableColumn
extendedAccessListIpProtocol = _ExtendedAccessListIpProtocol_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 1, 1, 2, 3, 1, 3),
    _ExtendedAccessListIpProtocol_Type()
)
extendedAccessListIpProtocol.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    extendedAccessListIpProtocol.setStatus("current")
_ExtendedAccessListIpSrc_Type = IpAddress
_ExtendedAccessListIpSrc_Object = MibTableColumn
extendedAccessListIpSrc = _ExtendedAccessListIpSrc_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 1, 1, 2, 3, 1, 4),
    _ExtendedAccessListIpSrc_Type()
)
extendedAccessListIpSrc.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    extendedAccessListIpSrc.setStatus("current")
_ExtendedAccessListIpMASKsrc_Type = IpAddress
_ExtendedAccessListIpMASKsrc_Object = MibTableColumn
extendedAccessListIpMASKsrc = _ExtendedAccessListIpMASKsrc_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 1, 1, 2, 3, 1, 5),
    _ExtendedAccessListIpMASKsrc_Type()
)
extendedAccessListIpMASKsrc.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    extendedAccessListIpMASKsrc.setStatus("current")
_ExtendedAccessListPortDefSrc_Type = PortDef
_ExtendedAccessListPortDefSrc_Object = MibTableColumn
extendedAccessListPortDefSrc = _ExtendedAccessListPortDefSrc_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 1, 1, 2, 3, 1, 6),
    _ExtendedAccessListPortDefSrc_Type()
)
extendedAccessListPortDefSrc.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    extendedAccessListPortDefSrc.setStatus("current")


class _ExtendedAccessListPortNumSrc_Type(Integer32):
    """Custom type extendedAccessListPortNumSrc based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_ExtendedAccessListPortNumSrc_Type.__name__ = "Integer32"
_ExtendedAccessListPortNumSrc_Object = MibTableColumn
extendedAccessListPortNumSrc = _ExtendedAccessListPortNumSrc_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 1, 1, 2, 3, 1, 7),
    _ExtendedAccessListPortNumSrc_Type()
)
extendedAccessListPortNumSrc.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    extendedAccessListPortNumSrc.setStatus("current")


class _ExtendedAccessListPortRangeSrc_Type(Integer32):
    """Custom type extendedAccessListPortRangeSrc based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_ExtendedAccessListPortRangeSrc_Type.__name__ = "Integer32"
_ExtendedAccessListPortRangeSrc_Object = MibTableColumn
extendedAccessListPortRangeSrc = _ExtendedAccessListPortRangeSrc_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 1, 1, 2, 3, 1, 8),
    _ExtendedAccessListPortRangeSrc_Type()
)
extendedAccessListPortRangeSrc.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    extendedAccessListPortRangeSrc.setStatus("current")
_ExtendedAccessListIpDest_Type = IpAddress
_ExtendedAccessListIpDest_Object = MibTableColumn
extendedAccessListIpDest = _ExtendedAccessListIpDest_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 1, 1, 2, 3, 1, 9),
    _ExtendedAccessListIpDest_Type()
)
extendedAccessListIpDest.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    extendedAccessListIpDest.setStatus("current")
_ExtendedAccessListIpMASKdst_Type = IpAddress
_ExtendedAccessListIpMASKdst_Object = MibTableColumn
extendedAccessListIpMASKdst = _ExtendedAccessListIpMASKdst_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 1, 1, 2, 3, 1, 10),
    _ExtendedAccessListIpMASKdst_Type()
)
extendedAccessListIpMASKdst.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    extendedAccessListIpMASKdst.setStatus("current")
_ExtendedAccessListPortDefDst_Type = PortDef
_ExtendedAccessListPortDefDst_Object = MibTableColumn
extendedAccessListPortDefDst = _ExtendedAccessListPortDefDst_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 1, 1, 2, 3, 1, 11),
    _ExtendedAccessListPortDefDst_Type()
)
extendedAccessListPortDefDst.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    extendedAccessListPortDefDst.setStatus("current")


class _ExtendedAccessListPortNumDst_Type(Integer32):
    """Custom type extendedAccessListPortNumDst based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_ExtendedAccessListPortNumDst_Type.__name__ = "Integer32"
_ExtendedAccessListPortNumDst_Object = MibTableColumn
extendedAccessListPortNumDst = _ExtendedAccessListPortNumDst_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 1, 1, 2, 3, 1, 12),
    _ExtendedAccessListPortNumDst_Type()
)
extendedAccessListPortNumDst.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    extendedAccessListPortNumDst.setStatus("current")


class _ExtendedAccessListPortRangeDst_Type(Integer32):
    """Custom type extendedAccessListPortRangeDst based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_ExtendedAccessListPortRangeDst_Type.__name__ = "Integer32"
_ExtendedAccessListPortRangeDst_Object = MibTableColumn
extendedAccessListPortRangeDst = _ExtendedAccessListPortRangeDst_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 1, 1, 2, 3, 1, 13),
    _ExtendedAccessListPortRangeDst_Type()
)
extendedAccessListPortRangeDst.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    extendedAccessListPortRangeDst.setStatus("current")


class _ExtendedAccessListTos_Type(Integer32):
    """Custom type extendedAccessListTos based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_ExtendedAccessListTos_Type.__name__ = "Integer32"
_ExtendedAccessListTos_Object = MibTableColumn
extendedAccessListTos = _ExtendedAccessListTos_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 1, 1, 2, 3, 1, 14),
    _ExtendedAccessListTos_Type()
)
extendedAccessListTos.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    extendedAccessListTos.setStatus("current")


class _ExtendedAccessListPrec_Type(Integer32):
    """Custom type extendedAccessListPrec based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_ExtendedAccessListPrec_Type.__name__ = "Integer32"
_ExtendedAccessListPrec_Object = MibTableColumn
extendedAccessListPrec = _ExtendedAccessListPrec_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 1, 1, 2, 3, 1, 15),
    _ExtendedAccessListPrec_Type()
)
extendedAccessListPrec.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    extendedAccessListPrec.setStatus("current")
_ExtendedAccessListModifyTos_Type = AccessListModifyTos
_ExtendedAccessListModifyTos_Object = MibTableColumn
extendedAccessListModifyTos = _ExtendedAccessListModifyTos_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 1, 1, 2, 3, 1, 16),
    _ExtendedAccessListModifyTos_Type()
)
extendedAccessListModifyTos.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    extendedAccessListModifyTos.setStatus("current")
_ExtendedAccessListRemark_Type = AccessListRemarkString
_ExtendedAccessListRemark_Object = MibTableColumn
extendedAccessListRemark = _ExtendedAccessListRemark_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 1, 1, 2, 3, 1, 17),
    _ExtendedAccessListRemark_Type()
)
extendedAccessListRemark.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    extendedAccessListRemark.setStatus("current")


class _ExtendedAccessListIcmpType_Type(Integer32):
    """Custom type extendedAccessListIcmpType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_ExtendedAccessListIcmpType_Type.__name__ = "Integer32"
_ExtendedAccessListIcmpType_Object = MibTableColumn
extendedAccessListIcmpType = _ExtendedAccessListIcmpType_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 1, 1, 2, 3, 1, 18),
    _ExtendedAccessListIcmpType_Type()
)
extendedAccessListIcmpType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    extendedAccessListIcmpType.setStatus("current")


class _ExtendedAccessListIcmpCode_Type(Integer32):
    """Custom type extendedAccessListIcmpCode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_ExtendedAccessListIcmpCode_Type.__name__ = "Integer32"
_ExtendedAccessListIcmpCode_Object = MibTableColumn
extendedAccessListIcmpCode = _ExtendedAccessListIcmpCode_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 1, 1, 2, 3, 1, 19),
    _ExtendedAccessListIcmpCode_Type()
)
extendedAccessListIcmpCode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    extendedAccessListIcmpCode.setStatus("current")


class _ExtendedAccessListIgmpType_Type(Integer32):
    """Custom type extendedAccessListIgmpType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_ExtendedAccessListIgmpType_Type.__name__ = "Integer32"
_ExtendedAccessListIgmpType_Object = MibTableColumn
extendedAccessListIgmpType = _ExtendedAccessListIgmpType_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 1, 1, 2, 3, 1, 20),
    _ExtendedAccessListIgmpType_Type()
)
extendedAccessListIgmpType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    extendedAccessListIgmpType.setStatus("current")
_ExtendedAccessListEstablished_Type = AccessListEstablished
_ExtendedAccessListEstablished_Object = MibTableColumn
extendedAccessListEstablished = _ExtendedAccessListEstablished_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 1, 1, 2, 3, 1, 21),
    _ExtendedAccessListEstablished_Type()
)
extendedAccessListEstablished.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    extendedAccessListEstablished.setStatus("current")


class _ExtendedAccessListLog_Type(Integer32):
    """Custom type extendedAccessListLog based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("undefined", 0),
          ("log", 1),
          ("log-input", 2))
    )


_ExtendedAccessListLog_Type.__name__ = "Integer32"
_ExtendedAccessListLog_Object = MibTableColumn
extendedAccessListLog = _ExtendedAccessListLog_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 1, 1, 2, 3, 1, 22),
    _ExtendedAccessListLog_Type()
)
extendedAccessListLog.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    extendedAccessListLog.setStatus("current")


class _ExtendedAccessListVpt_Type(Integer32):
    """Custom type extendedAccessListVpt based on Integer32"""
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
              241,
              242,
              243,
              244,
              245,
              246,
              247,
              248)
        )
    )
    namedValues = NamedValues(
        *(("vpt-value0", 0),
          ("vpt-value1", 1),
          ("vpt-value2", 2),
          ("vpt-value3", 3),
          ("vpt-value4", 4),
          ("vpt-value5", 5),
          ("vpt-value6", 6),
          ("vpt-value7", 7),
          ("undefined", 8),
          ("fc-be", 241),
          ("fc-l2", 242),
          ("fc-af", 243),
          ("fc-l1", 244),
          ("fc-h2", 245),
          ("fc-ef", 246),
          ("fc-h1", 247),
          ("fc-nc", 248))
    )


_ExtendedAccessListVpt_Type.__name__ = "Integer32"
_ExtendedAccessListVpt_Object = MibTableColumn
extendedAccessListVpt = _ExtendedAccessListVpt_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 1, 1, 2, 3, 1, 23),
    _ExtendedAccessListVpt_Type()
)
extendedAccessListVpt.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    extendedAccessListVpt.setStatus("current")
_ExtendedAccessListRowStatus_Type = RowStatus
_ExtendedAccessListRowStatus_Object = MibTableColumn
extendedAccessListRowStatus = _ExtendedAccessListRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 1, 1, 2, 3, 1, 24),
    _ExtendedAccessListRowStatus_Type()
)
extendedAccessListRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    extendedAccessListRowStatus.setStatus("current")


class _ExtendedAccessListVlanId_Type(Integer32):
    """Custom type extendedAccessListVlanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4092),
    )


_ExtendedAccessListVlanId_Type.__name__ = "Integer32"
_ExtendedAccessListVlanId_Object = MibTableColumn
extendedAccessListVlanId = _ExtendedAccessListVlanId_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 1, 1, 2, 3, 1, 25),
    _ExtendedAccessListVlanId_Type()
)
extendedAccessListVlanId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    extendedAccessListVlanId.setStatus("current")
_ExtendedAccessListVlanMask_Type = DisplayString
_ExtendedAccessListVlanMask_Object = MibTableColumn
extendedAccessListVlanMask = _ExtendedAccessListVlanMask_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 1, 1, 2, 3, 1, 26),
    _ExtendedAccessListVlanMask_Type()
)
extendedAccessListVlanMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    extendedAccessListVlanMask.setStatus("current")


class _ExtendedAccessListProviderVlanId_Type(Integer32):
    """Custom type extendedAccessListProviderVlanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4092),
    )


_ExtendedAccessListProviderVlanId_Type.__name__ = "Integer32"
_ExtendedAccessListProviderVlanId_Object = MibTableColumn
extendedAccessListProviderVlanId = _ExtendedAccessListProviderVlanId_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 1, 1, 2, 3, 1, 27),
    _ExtendedAccessListProviderVlanId_Type()
)
extendedAccessListProviderVlanId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    extendedAccessListProviderVlanId.setStatus("current")
_ExtendedAccessListProviderVlanMask_Type = DisplayString
_ExtendedAccessListProviderVlanMask_Object = MibTableColumn
extendedAccessListProviderVlanMask = _ExtendedAccessListProviderVlanMask_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 1, 1, 2, 3, 1, 28),
    _ExtendedAccessListProviderVlanMask_Type()
)
extendedAccessListProviderVlanMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    extendedAccessListProviderVlanMask.setStatus("current")


class _ExtendedAccessListProviderVpt_Type(Integer32):
    """Custom type extendedAccessListProviderVpt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8),
    )


_ExtendedAccessListProviderVpt_Type.__name__ = "Integer32"
_ExtendedAccessListProviderVpt_Object = MibTableColumn
extendedAccessListProviderVpt = _ExtendedAccessListProviderVpt_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 1, 1, 2, 3, 1, 29),
    _ExtendedAccessListProviderVpt_Type()
)
extendedAccessListProviderVpt.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    extendedAccessListProviderVpt.setStatus("current")
_ExtendedAccessListUntaggedMode_Type = TruthValue
_ExtendedAccessListUntaggedMode_Object = MibTableColumn
extendedAccessListUntaggedMode = _ExtendedAccessListUntaggedMode_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 1, 1, 2, 3, 1, 30),
    _ExtendedAccessListUntaggedMode_Type()
)
extendedAccessListUntaggedMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    extendedAccessListUntaggedMode.setStatus("current")


class _ExtendedAccessListDropLevel_Type(Integer32):
    """Custom type extendedAccessListDropLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("green", 0),
          ("yellow", 1))
    )


_ExtendedAccessListDropLevel_Type.__name__ = "Integer32"
_ExtendedAccessListDropLevel_Object = MibTableColumn
extendedAccessListDropLevel = _ExtendedAccessListDropLevel_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 1, 1, 2, 3, 1, 31),
    _ExtendedAccessListDropLevel_Type()
)
extendedAccessListDropLevel.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    extendedAccessListDropLevel.setStatus("current")


class _ExtendedAccessListDscp_Type(Integer32):
    """Custom type extendedAccessListDscp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_ExtendedAccessListDscp_Type.__name__ = "Integer32"
_ExtendedAccessListDscp_Object = MibTableColumn
extendedAccessListDscp = _ExtendedAccessListDscp_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 1, 1, 2, 3, 1, 32),
    _ExtendedAccessListDscp_Type()
)
extendedAccessListDscp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    extendedAccessListDscp.setStatus("current")
_MacAccessListTable_Object = MibTable
macAccessListTable = _MacAccessListTable_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 1, 1, 2, 4)
)
if mibBuilder.loadTexts:
    macAccessListTable.setStatus("current")
_MacAccessListEntry_Object = MibTableRow
macAccessListEntry = _MacAccessListEntry_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 1, 1, 2, 4, 1)
)
macAccessListEntry.setIndexNames(
    (0, "PRVT-SWITCH-ACCESS-LIST-MIB", "accessListControlListGroup"),
    (0, "PRVT-SWITCH-ACCESS-LIST-MIB", "macAccessListIndex"),
)
if mibBuilder.loadTexts:
    macAccessListEntry.setStatus("current")


class _MacAccessListIndex_Type(Integer32):
    """Custom type macAccessListIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MacAccessListIndex_Type.__name__ = "Integer32"
_MacAccessListIndex_Object = MibTableColumn
macAccessListIndex = _MacAccessListIndex_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 1, 1, 2, 4, 1, 1),
    _MacAccessListIndex_Type()
)
macAccessListIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    macAccessListIndex.setStatus("current")
_MacAccessListAction_Type = AccessListAction
_MacAccessListAction_Object = MibTableColumn
macAccessListAction = _MacAccessListAction_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 1, 1, 2, 4, 1, 2),
    _MacAccessListAction_Type()
)
macAccessListAction.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    macAccessListAction.setStatus("current")
_MacAccessListMacSrc_Type = MacAddress
_MacAccessListMacSrc_Object = MibTableColumn
macAccessListMacSrc = _MacAccessListMacSrc_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 1, 1, 2, 4, 1, 3),
    _MacAccessListMacSrc_Type()
)
macAccessListMacSrc.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    macAccessListMacSrc.setStatus("current")
_MacAccessListMacSrcMask_Type = MacAddress
_MacAccessListMacSrcMask_Object = MibTableColumn
macAccessListMacSrcMask = _MacAccessListMacSrcMask_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 1, 1, 2, 4, 1, 4),
    _MacAccessListMacSrcMask_Type()
)
macAccessListMacSrcMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    macAccessListMacSrcMask.setStatus("current")
_MacAccessListMacDst_Type = MacAddress
_MacAccessListMacDst_Object = MibTableColumn
macAccessListMacDst = _MacAccessListMacDst_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 1, 1, 2, 4, 1, 5),
    _MacAccessListMacDst_Type()
)
macAccessListMacDst.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    macAccessListMacDst.setStatus("current")
_MacAccessListMacDstMask_Type = MacAddress
_MacAccessListMacDstMask_Object = MibTableColumn
macAccessListMacDstMask = _MacAccessListMacDstMask_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 1, 1, 2, 4, 1, 6),
    _MacAccessListMacDstMask_Type()
)
macAccessListMacDstMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    macAccessListMacDstMask.setStatus("current")
_MacAccessListRemark_Type = AccessListRemarkString
_MacAccessListRemark_Object = MibTableColumn
macAccessListRemark = _MacAccessListRemark_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 1, 1, 2, 4, 1, 7),
    _MacAccessListRemark_Type()
)
macAccessListRemark.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    macAccessListRemark.setStatus("current")


class _MacAccessListLog_Type(Integer32):
    """Custom type macAccessListLog based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("undefined", 0),
          ("log", 1),
          ("log-input", 2))
    )


_MacAccessListLog_Type.__name__ = "Integer32"
_MacAccessListLog_Object = MibTableColumn
macAccessListLog = _MacAccessListLog_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 1, 1, 2, 4, 1, 8),
    _MacAccessListLog_Type()
)
macAccessListLog.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    macAccessListLog.setStatus("current")
_MacAccessListRowStatus_Type = RowStatus
_MacAccessListRowStatus_Object = MibTableColumn
macAccessListRowStatus = _MacAccessListRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 1, 1, 2, 4, 1, 9),
    _MacAccessListRowStatus_Type()
)
macAccessListRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    macAccessListRowStatus.setStatus("current")
_MacAccessListTos_Type = Integer32
_MacAccessListTos_Object = MibTableColumn
macAccessListTos = _MacAccessListTos_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 1, 1, 2, 4, 1, 10),
    _MacAccessListTos_Type()
)
macAccessListTos.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    macAccessListTos.setStatus("current")
_MacAccessListPrecedence_Type = Integer32
_MacAccessListPrecedence_Object = MibTableColumn
macAccessListPrecedence = _MacAccessListPrecedence_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 1, 1, 2, 4, 1, 11),
    _MacAccessListPrecedence_Type()
)
macAccessListPrecedence.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    macAccessListPrecedence.setStatus("current")


class _MacAccessListVpt_Type(Integer32):
    """Custom type macAccessListVpt based on Integer32"""
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
              241,
              242,
              243,
              244,
              245,
              246,
              247,
              248)
        )
    )
    namedValues = NamedValues(
        *(("vpt-value0", 0),
          ("vpt-value1", 1),
          ("vpt-value2", 2),
          ("vpt-value3", 3),
          ("vpt-value4", 4),
          ("vpt-value5", 5),
          ("vpt-value6", 6),
          ("vpt-value7", 7),
          ("undefined", 8),
          ("fc-be", 241),
          ("fc-l2", 242),
          ("fc-af", 243),
          ("fc-l1", 244),
          ("fc-h2", 245),
          ("fc-ef", 246),
          ("fc-h1", 247),
          ("fc-nc", 248))
    )


_MacAccessListVpt_Type.__name__ = "Integer32"
_MacAccessListVpt_Object = MibTableColumn
macAccessListVpt = _MacAccessListVpt_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 1, 1, 2, 4, 1, 12),
    _MacAccessListVpt_Type()
)
macAccessListVpt.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    macAccessListVpt.setStatus("current")


class _MacAccessListVlanId_Type(Integer32):
    """Custom type macAccessListVlanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4092),
    )


_MacAccessListVlanId_Type.__name__ = "Integer32"
_MacAccessListVlanId_Object = MibTableColumn
macAccessListVlanId = _MacAccessListVlanId_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 1, 1, 2, 4, 1, 13),
    _MacAccessListVlanId_Type()
)
macAccessListVlanId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    macAccessListVlanId.setStatus("current")
_MacAccessListVlanMask_Type = DisplayString
_MacAccessListVlanMask_Object = MibTableColumn
macAccessListVlanMask = _MacAccessListVlanMask_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 1, 1, 2, 4, 1, 14),
    _MacAccessListVlanMask_Type()
)
macAccessListVlanMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    macAccessListVlanMask.setStatus("current")


class _MacAccessListInnerVlanId_Type(Integer32):
    """Custom type macAccessListInnerVlanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4092),
    )


_MacAccessListInnerVlanId_Type.__name__ = "Integer32"
_MacAccessListInnerVlanId_Object = MibTableColumn
macAccessListInnerVlanId = _MacAccessListInnerVlanId_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 1, 1, 2, 4, 1, 15),
    _MacAccessListInnerVlanId_Type()
)
macAccessListInnerVlanId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    macAccessListInnerVlanId.setStatus("current")
_MacAccessListInnerVlanMask_Type = DisplayString
_MacAccessListInnerVlanMask_Object = MibTableColumn
macAccessListInnerVlanMask = _MacAccessListInnerVlanMask_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 1, 1, 2, 4, 1, 16),
    _MacAccessListInnerVlanMask_Type()
)
macAccessListInnerVlanMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    macAccessListInnerVlanMask.setStatus("current")


class _MacAccessListInnerVpt_Type(Integer32):
    """Custom type macAccessListInnerVpt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8),
    )


_MacAccessListInnerVpt_Type.__name__ = "Integer32"
_MacAccessListInnerVpt_Object = MibTableColumn
macAccessListInnerVpt = _MacAccessListInnerVpt_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 1, 1, 2, 4, 1, 17),
    _MacAccessListInnerVpt_Type()
)
macAccessListInnerVpt.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    macAccessListInnerVpt.setStatus("current")
_MacAccessListEtherType_Type = DisplayString
_MacAccessListEtherType_Object = MibTableColumn
macAccessListEtherType = _MacAccessListEtherType_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 1, 1, 2, 4, 1, 18),
    _MacAccessListEtherType_Type()
)
macAccessListEtherType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    macAccessListEtherType.setStatus("current")
_MacAccessListDscp_Type = Integer32
_MacAccessListDscp_Object = MibTableColumn
macAccessListDscp = _MacAccessListDscp_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 1, 1, 2, 4, 1, 19),
    _MacAccessListDscp_Type()
)
macAccessListDscp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    macAccessListDscp.setStatus("current")
_MacAccessListMatchTraffic_Type = MatchTraffic
_MacAccessListMatchTraffic_Object = MibTableColumn
macAccessListMatchTraffic = _MacAccessListMatchTraffic_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 1, 1, 2, 4, 1, 20),
    _MacAccessListMatchTraffic_Type()
)
macAccessListMatchTraffic.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    macAccessListMatchTraffic.setStatus("current")
_MacAccessListMatchTrafficPort_Type = DisplayString
_MacAccessListMatchTrafficPort_Object = MibTableColumn
macAccessListMatchTrafficPort = _MacAccessListMatchTrafficPort_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 1, 1, 2, 4, 1, 21),
    _MacAccessListMatchTrafficPort_Type()
)
macAccessListMatchTrafficPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    macAccessListMatchTrafficPort.setStatus("current")
_MacAccessListUntaggedMode_Type = TruthValue
_MacAccessListUntaggedMode_Object = MibTableColumn
macAccessListUntaggedMode = _MacAccessListUntaggedMode_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 1, 1, 2, 4, 1, 22),
    _MacAccessListUntaggedMode_Type()
)
macAccessListUntaggedMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    macAccessListUntaggedMode.setStatus("current")


class _MacAccessListDropLevel_Type(Integer32):
    """Custom type macAccessListDropLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("green", 0),
          ("yellow", 1))
    )


_MacAccessListDropLevel_Type.__name__ = "Integer32"
_MacAccessListDropLevel_Object = MibTableColumn
macAccessListDropLevel = _MacAccessListDropLevel_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 1, 1, 2, 4, 1, 23),
    _MacAccessListDropLevel_Type()
)
macAccessListDropLevel.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    macAccessListDropLevel.setStatus("current")
_EtherTypeAccessListTable_Object = MibTable
etherTypeAccessListTable = _EtherTypeAccessListTable_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 1, 1, 2, 5)
)
if mibBuilder.loadTexts:
    etherTypeAccessListTable.setStatus("current")
_EtherTypeAccessListEntry_Object = MibTableRow
etherTypeAccessListEntry = _EtherTypeAccessListEntry_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 1, 1, 2, 5, 1)
)
etherTypeAccessListEntry.setIndexNames(
    (0, "PRVT-SWITCH-ACCESS-LIST-MIB", "accessListControlListGroup"),
    (0, "PRVT-SWITCH-ACCESS-LIST-MIB", "etherTypeAccessListIndex"),
)
if mibBuilder.loadTexts:
    etherTypeAccessListEntry.setStatus("current")


class _EtherTypeAccessListIndex_Type(Integer32):
    """Custom type etherTypeAccessListIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_EtherTypeAccessListIndex_Type.__name__ = "Integer32"
_EtherTypeAccessListIndex_Object = MibTableColumn
etherTypeAccessListIndex = _EtherTypeAccessListIndex_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 1, 1, 2, 5, 1, 1),
    _EtherTypeAccessListIndex_Type()
)
etherTypeAccessListIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    etherTypeAccessListIndex.setStatus("current")
_EtherTypeAccessListAction_Type = AccessListAction
_EtherTypeAccessListAction_Object = MibTableColumn
etherTypeAccessListAction = _EtherTypeAccessListAction_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 1, 1, 2, 5, 1, 2),
    _EtherTypeAccessListAction_Type()
)
etherTypeAccessListAction.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    etherTypeAccessListAction.setStatus("current")
_EtherTypeAccessListEtherType_Type = DisplayString
_EtherTypeAccessListEtherType_Object = MibTableColumn
etherTypeAccessListEtherType = _EtherTypeAccessListEtherType_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 1, 1, 2, 5, 1, 3),
    _EtherTypeAccessListEtherType_Type()
)
etherTypeAccessListEtherType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    etherTypeAccessListEtherType.setStatus("current")
_EtherTypeAccessListEtherTypeCodeMask_Type = DisplayString
_EtherTypeAccessListEtherTypeCodeMask_Object = MibTableColumn
etherTypeAccessListEtherTypeCodeMask = _EtherTypeAccessListEtherTypeCodeMask_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 1, 1, 2, 5, 1, 4),
    _EtherTypeAccessListEtherTypeCodeMask_Type()
)
etherTypeAccessListEtherTypeCodeMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    etherTypeAccessListEtherTypeCodeMask.setStatus("current")
_EtherTypeAccessListRemark_Type = AccessListRemarkString
_EtherTypeAccessListRemark_Object = MibTableColumn
etherTypeAccessListRemark = _EtherTypeAccessListRemark_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 1, 1, 2, 5, 1, 5),
    _EtherTypeAccessListRemark_Type()
)
etherTypeAccessListRemark.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    etherTypeAccessListRemark.setStatus("current")


class _EtherTypeAccessListLog_Type(Integer32):
    """Custom type etherTypeAccessListLog based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("undefined", 0),
          ("log", 1),
          ("log-input", 2))
    )


_EtherTypeAccessListLog_Type.__name__ = "Integer32"
_EtherTypeAccessListLog_Object = MibTableColumn
etherTypeAccessListLog = _EtherTypeAccessListLog_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 1, 1, 2, 5, 1, 6),
    _EtherTypeAccessListLog_Type()
)
etherTypeAccessListLog.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    etherTypeAccessListLog.setStatus("current")
_EtherTypeAccessListRowStatus_Type = RowStatus
_EtherTypeAccessListRowStatus_Object = MibTableColumn
etherTypeAccessListRowStatus = _EtherTypeAccessListRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 1, 1, 2, 5, 1, 7),
    _EtherTypeAccessListRowStatus_Type()
)
etherTypeAccessListRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etherTypeAccessListRowStatus.setStatus("current")


class _EtherTypeAccessListVlanId_Type(Integer32):
    """Custom type etherTypeAccessListVlanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4092),
    )


_EtherTypeAccessListVlanId_Type.__name__ = "Integer32"
_EtherTypeAccessListVlanId_Object = MibTableColumn
etherTypeAccessListVlanId = _EtherTypeAccessListVlanId_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 1, 1, 2, 5, 1, 8),
    _EtherTypeAccessListVlanId_Type()
)
etherTypeAccessListVlanId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    etherTypeAccessListVlanId.setStatus("current")
_EtherTypeAccessListVlanMask_Type = DisplayString
_EtherTypeAccessListVlanMask_Object = MibTableColumn
etherTypeAccessListVlanMask = _EtherTypeAccessListVlanMask_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 1, 1, 2, 5, 1, 9),
    _EtherTypeAccessListVlanMask_Type()
)
etherTypeAccessListVlanMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    etherTypeAccessListVlanMask.setStatus("current")


class _EtherTypeAccessListProviderVlanId_Type(Integer32):
    """Custom type etherTypeAccessListProviderVlanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4092),
    )


_EtherTypeAccessListProviderVlanId_Type.__name__ = "Integer32"
_EtherTypeAccessListProviderVlanId_Object = MibTableColumn
etherTypeAccessListProviderVlanId = _EtherTypeAccessListProviderVlanId_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 1, 1, 2, 5, 1, 10),
    _EtherTypeAccessListProviderVlanId_Type()
)
etherTypeAccessListProviderVlanId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    etherTypeAccessListProviderVlanId.setStatus("current")
_EtherTypeAccessListProviderVlanMask_Type = DisplayString
_EtherTypeAccessListProviderVlanMask_Object = MibTableColumn
etherTypeAccessListProviderVlanMask = _EtherTypeAccessListProviderVlanMask_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 1, 1, 2, 5, 1, 11),
    _EtherTypeAccessListProviderVlanMask_Type()
)
etherTypeAccessListProviderVlanMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    etherTypeAccessListProviderVlanMask.setStatus("current")


class _EtherTypeAccessListProviderVpt_Type(Integer32):
    """Custom type etherTypeAccessListProviderVpt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8),
    )


_EtherTypeAccessListProviderVpt_Type.__name__ = "Integer32"
_EtherTypeAccessListProviderVpt_Object = MibTableColumn
etherTypeAccessListProviderVpt = _EtherTypeAccessListProviderVpt_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 1, 1, 2, 5, 1, 12),
    _EtherTypeAccessListProviderVpt_Type()
)
etherTypeAccessListProviderVpt.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    etherTypeAccessListProviderVpt.setStatus("current")
_AccessListsInterfaces_ObjectIdentity = ObjectIdentity
accessListsInterfaces = _AccessListsInterfaces_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 1, 1, 3)
)
_AccessListInterfaceTable_Object = MibTable
accessListInterfaceTable = _AccessListInterfaceTable_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 1, 1, 3, 1)
)
if mibBuilder.loadTexts:
    accessListInterfaceTable.setStatus("current")
_AccessListInterfaceEntry_Object = MibTableRow
accessListInterfaceEntry = _AccessListInterfaceEntry_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 1, 1, 3, 1, 1)
)
accessListInterfaceEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "PRVT-SWITCH-ACCESS-LIST-MIB", "accessListInterfaceTableIndex"),
    (0, "PRVT-SWITCH-ACCESS-LIST-MIB", "accessListInterfaceGroupIndex"),
)
if mibBuilder.loadTexts:
    accessListInterfaceEntry.setStatus("current")


class _AccessListInterfaceTableIndex_Type(Integer32):
    """Custom type accessListInterfaceTableIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_AccessListInterfaceTableIndex_Type.__name__ = "Integer32"
_AccessListInterfaceTableIndex_Object = MibTableColumn
accessListInterfaceTableIndex = _AccessListInterfaceTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 1, 1, 3, 1, 1, 1),
    _AccessListInterfaceTableIndex_Type()
)
accessListInterfaceTableIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    accessListInterfaceTableIndex.setStatus("current")


class _AccessListInterfaceGroupIndex_Type(Integer32):
    """Custom type accessListInterfaceGroupIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_AccessListInterfaceGroupIndex_Type.__name__ = "Integer32"
_AccessListInterfaceGroupIndex_Object = MibTableColumn
accessListInterfaceGroupIndex = _AccessListInterfaceGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 1, 1, 3, 1, 1, 2),
    _AccessListInterfaceGroupIndex_Type()
)
accessListInterfaceGroupIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    accessListInterfaceGroupIndex.setStatus("current")


class _AccessListInterfaceDscp_Type(Integer32):
    """Custom type accessListInterfaceDscp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_AccessListInterfaceDscp_Type.__name__ = "Integer32"
_AccessListInterfaceDscp_Object = MibTableColumn
accessListInterfaceDscp = _AccessListInterfaceDscp_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 1, 1, 3, 1, 1, 3),
    _AccessListInterfaceDscp_Type()
)
accessListInterfaceDscp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    accessListInterfaceDscp.setStatus("current")
_AccessListInterfaceRowStatus_Type = RowStatus
_AccessListInterfaceRowStatus_Object = MibTableColumn
accessListInterfaceRowStatus = _AccessListInterfaceRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 1, 1, 3, 1, 1, 4),
    _AccessListInterfaceRowStatus_Type()
)
accessListInterfaceRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accessListInterfaceRowStatus.setStatus("current")


class _AccessListInterfacePriority_Type(Integer32):
    """Custom type accessListInterfacePriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8),
    )


_AccessListInterfacePriority_Type.__name__ = "Integer32"
_AccessListInterfacePriority_Object = MibTableColumn
accessListInterfacePriority = _AccessListInterfacePriority_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 1, 1, 3, 1, 1, 5),
    _AccessListInterfacePriority_Type()
)
accessListInterfacePriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accessListInterfacePriority.setStatus("current")
_AccessListInterfaceDiscard_Type = AccessListDiscard
_AccessListInterfaceDiscard_Object = MibTableColumn
accessListInterfaceDiscard = _AccessListInterfaceDiscard_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 1, 1, 3, 1, 1, 6),
    _AccessListInterfaceDiscard_Type()
)
accessListInterfaceDiscard.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accessListInterfaceDiscard.setStatus("current")
_AccessListInterfaceRateLimit_Type = Rate
_AccessListInterfaceRateLimit_Object = MibTableColumn
accessListInterfaceRateLimit = _AccessListInterfaceRateLimit_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 1, 1, 3, 1, 1, 7),
    _AccessListInterfaceRateLimit_Type()
)
accessListInterfaceRateLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accessListInterfaceRateLimit.setStatus("current")
_AccessListInterfaceExceedAction_Type = ExceedAction
_AccessListInterfaceExceedAction_Object = MibTableColumn
accessListInterfaceExceedAction = _AccessListInterfaceExceedAction_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 1, 1, 3, 1, 1, 8),
    _AccessListInterfaceExceedAction_Type()
)
accessListInterfaceExceedAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accessListInterfaceExceedAction.setStatus("current")
_AccessListInterfaceShaper_Type = Shaper
_AccessListInterfaceShaper_Object = MibTableColumn
accessListInterfaceShaper = _AccessListInterfaceShaper_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 1, 1, 3, 1, 1, 9),
    _AccessListInterfaceShaper_Type()
)
accessListInterfaceShaper.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accessListInterfaceShaper.setStatus("current")
_AccessListInterfaceBurst_Type = Rate
_AccessListInterfaceBurst_Object = MibTableColumn
accessListInterfaceBurst = _AccessListInterfaceBurst_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 1, 1, 3, 1, 1, 10),
    _AccessListInterfaceBurst_Type()
)
accessListInterfaceBurst.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accessListInterfaceBurst.setStatus("current")
_AccessListInterfaceRedirectIfIndex_Type = Integer32
_AccessListInterfaceRedirectIfIndex_Object = MibTableColumn
accessListInterfaceRedirectIfIndex = _AccessListInterfaceRedirectIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 1, 1, 3, 1, 1, 11),
    _AccessListInterfaceRedirectIfIndex_Type()
)
accessListInterfaceRedirectIfIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accessListInterfaceRedirectIfIndex.setStatus("current")
_AccessListInterfaceRedirectVlanID_Type = Integer32
_AccessListInterfaceRedirectVlanID_Object = MibTableColumn
accessListInterfaceRedirectVlanID = _AccessListInterfaceRedirectVlanID_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 1, 1, 3, 1, 1, 12),
    _AccessListInterfaceRedirectVlanID_Type()
)
accessListInterfaceRedirectVlanID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accessListInterfaceRedirectVlanID.setStatus("current")
_AccessListInterfaceRedirectNexthop_Type = IpAddress
_AccessListInterfaceRedirectNexthop_Object = MibTableColumn
accessListInterfaceRedirectNexthop = _AccessListInterfaceRedirectNexthop_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 1, 1, 3, 1, 1, 13),
    _AccessListInterfaceRedirectNexthop_Type()
)
accessListInterfaceRedirectNexthop.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accessListInterfaceRedirectNexthop.setStatus("current")
_AccessListInterfacePeakRate_Type = Rate
_AccessListInterfacePeakRate_Object = MibTableColumn
accessListInterfacePeakRate = _AccessListInterfacePeakRate_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 1, 1, 3, 1, 1, 14),
    _AccessListInterfacePeakRate_Type()
)
accessListInterfacePeakRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accessListInterfacePeakRate.setStatus("current")
_AccessListInterfacePeakBurst_Type = Rate
_AccessListInterfacePeakBurst_Object = MibTableColumn
accessListInterfacePeakBurst = _AccessListInterfacePeakBurst_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 1, 1, 3, 1, 1, 15),
    _AccessListInterfacePeakBurst_Type()
)
accessListInterfacePeakBurst.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accessListInterfacePeakBurst.setStatus("current")


class _AccessListInterfaceColorAware_Type(Integer32):
    """Custom type accessListInterfaceColorAware based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_AccessListInterfaceColorAware_Type.__name__ = "Integer32"
_AccessListInterfaceColorAware_Object = MibTableColumn
accessListInterfaceColorAware = _AccessListInterfaceColorAware_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 1, 1, 3, 1, 1, 16),
    _AccessListInterfaceColorAware_Type()
)
accessListInterfaceColorAware.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accessListInterfaceColorAware.setStatus("current")


class _AccessListInterfacePolicy_Type(Integer32):
    """Custom type accessListInterfacePolicy based on Integer32"""
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
        *(("undefined", 0),
          ("dcsp", 1),
          ("priority", 2),
          ("priority-dp", 3))
    )


_AccessListInterfacePolicy_Type.__name__ = "Integer32"
_AccessListInterfacePolicy_Object = MibTableColumn
accessListInterfacePolicy = _AccessListInterfacePolicy_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 1, 1, 3, 1, 1, 17),
    _AccessListInterfacePolicy_Type()
)
accessListInterfacePolicy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accessListInterfacePolicy.setStatus("current")


class _AccessListInterfaceTrafficClass_Type(Integer32):
    """Custom type accessListInterfaceTrafficClass based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 256),
    )


_AccessListInterfaceTrafficClass_Type.__name__ = "Integer32"
_AccessListInterfaceTrafficClass_Object = MibTableColumn
accessListInterfaceTrafficClass = _AccessListInterfaceTrafficClass_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 1, 1, 3, 1, 1, 18),
    _AccessListInterfaceTrafficClass_Type()
)
accessListInterfaceTrafficClass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accessListInterfaceTrafficClass.setStatus("current")


class _AccessListInterfaceSpanRootTrack_Type(Integer32):
    """Custom type accessListInterfaceSpanRootTrack based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_AccessListInterfaceSpanRootTrack_Type.__name__ = "Integer32"
_AccessListInterfaceSpanRootTrack_Object = MibTableColumn
accessListInterfaceSpanRootTrack = _AccessListInterfaceSpanRootTrack_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 1, 1, 3, 1, 1, 19),
    _AccessListInterfaceSpanRootTrack_Type()
)
accessListInterfaceSpanRootTrack.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    accessListInterfaceSpanRootTrack.setStatus("current")


class _AccessListInterfaceUntagFilter_Type(Integer32):
    """Custom type accessListInterfaceUntagFilter based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_AccessListInterfaceUntagFilter_Type.__name__ = "Integer32"
_AccessListInterfaceUntagFilter_Object = MibTableColumn
accessListInterfaceUntagFilter = _AccessListInterfaceUntagFilter_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 1, 1, 3, 1, 1, 20),
    _AccessListInterfaceUntagFilter_Type()
)
accessListInterfaceUntagFilter.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    accessListInterfaceUntagFilter.setStatus("current")
_AccessListInterfaceTxq_Type = Integer32
_AccessListInterfaceTxq_Object = MibTableColumn
accessListInterfaceTxq = _AccessListInterfaceTxq_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 1, 1, 3, 1, 1, 21),
    _AccessListInterfaceTxq_Type()
)
accessListInterfaceTxq.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    accessListInterfaceTxq.setStatus("current")
_AccessListInterfaceTxqDropLevel_Type = TxqDropLevel
_AccessListInterfaceTxqDropLevel_Object = MibTableColumn
accessListInterfaceTxqDropLevel = _AccessListInterfaceTxqDropLevel_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 1, 1, 3, 1, 1, 22),
    _AccessListInterfaceTxqDropLevel_Type()
)
accessListInterfaceTxqDropLevel.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    accessListInterfaceTxqDropLevel.setStatus("current")
_AccessListInterfaceApplyMirror_Type = TruthValue
_AccessListInterfaceApplyMirror_Object = MibTableColumn
accessListInterfaceApplyMirror = _AccessListInterfaceApplyMirror_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 1, 1, 3, 1, 1, 23),
    _AccessListInterfaceApplyMirror_Type()
)
accessListInterfaceApplyMirror.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    accessListInterfaceApplyMirror.setStatus("current")
_AccessListInterfaceStatistics_Type = AccessListStatistics
_AccessListInterfaceStatistics_Object = MibTableColumn
accessListInterfaceStatistics = _AccessListInterfaceStatistics_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 1, 1, 3, 1, 1, 24),
    _AccessListInterfaceStatistics_Type()
)
accessListInterfaceStatistics.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    accessListInterfaceStatistics.setStatus("current")
_AccessListInterfaceDirection_Type = AccessListDirection
_AccessListInterfaceDirection_Object = MibTableColumn
accessListInterfaceDirection = _AccessListInterfaceDirection_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 1, 1, 3, 1, 1, 25),
    _AccessListInterfaceDirection_Type()
)
accessListInterfaceDirection.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    accessListInterfaceDirection.setStatus("current")
_AccessListInterfaceRateStatistics_Type = AccessListStatistics
_AccessListInterfaceRateStatistics_Object = MibTableColumn
accessListInterfaceRateStatistics = _AccessListInterfaceRateStatistics_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 1, 1, 3, 1, 1, 26),
    _AccessListInterfaceRateStatistics_Type()
)
accessListInterfaceRateStatistics.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    accessListInterfaceRateStatistics.setStatus("current")
_AccessListsVLAN_ObjectIdentity = ObjectIdentity
accessListsVLAN = _AccessListsVLAN_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 1, 1, 4)
)
_AccessListVLANTable_Object = MibTable
accessListVLANTable = _AccessListVLANTable_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 1, 1, 4, 1)
)
if mibBuilder.loadTexts:
    accessListVLANTable.setStatus("current")
_AccessListVLANEntry_Object = MibTableRow
accessListVLANEntry = _AccessListVLANEntry_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 1, 1, 4, 1, 1)
)
accessListVLANEntry.setIndexNames(
    (0, "Q-BRIDGE-MIB", "dot1qVlanIndex"),
    (0, "PRVT-SWITCH-ACCESS-LIST-MIB", "accessListVLANTableIndex"),
    (0, "PRVT-SWITCH-ACCESS-LIST-MIB", "accessListVLANGroupIndex"),
)
if mibBuilder.loadTexts:
    accessListVLANEntry.setStatus("current")


class _AccessListVLANTableIndex_Type(Integer32):
    """Custom type accessListVLANTableIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_AccessListVLANTableIndex_Type.__name__ = "Integer32"
_AccessListVLANTableIndex_Object = MibTableColumn
accessListVLANTableIndex = _AccessListVLANTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 1, 1, 4, 1, 1, 1),
    _AccessListVLANTableIndex_Type()
)
accessListVLANTableIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    accessListVLANTableIndex.setStatus("current")


class _AccessListVLANGroupIndex_Type(Integer32):
    """Custom type accessListVLANGroupIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_AccessListVLANGroupIndex_Type.__name__ = "Integer32"
_AccessListVLANGroupIndex_Object = MibTableColumn
accessListVLANGroupIndex = _AccessListVLANGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 1, 1, 4, 1, 1, 2),
    _AccessListVLANGroupIndex_Type()
)
accessListVLANGroupIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    accessListVLANGroupIndex.setStatus("current")


class _AccessListVLANDscp_Type(Integer32):
    """Custom type accessListVLANDscp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_AccessListVLANDscp_Type.__name__ = "Integer32"
_AccessListVLANDscp_Object = MibTableColumn
accessListVLANDscp = _AccessListVLANDscp_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 1, 1, 4, 1, 1, 3),
    _AccessListVLANDscp_Type()
)
accessListVLANDscp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    accessListVLANDscp.setStatus("current")
_AccessListVLANRowStatus_Type = RowStatus
_AccessListVLANRowStatus_Object = MibTableColumn
accessListVLANRowStatus = _AccessListVLANRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 1, 1, 4, 1, 1, 4),
    _AccessListVLANRowStatus_Type()
)
accessListVLANRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accessListVLANRowStatus.setStatus("current")


class _AccessListVLANPriority_Type(Integer32):
    """Custom type accessListVLANPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8),
    )


_AccessListVLANPriority_Type.__name__ = "Integer32"
_AccessListVLANPriority_Object = MibTableColumn
accessListVLANPriority = _AccessListVLANPriority_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 1, 1, 4, 1, 1, 5),
    _AccessListVLANPriority_Type()
)
accessListVLANPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accessListVLANPriority.setStatus("current")
_AccessListVLANDiscard_Type = AccessListDiscard
_AccessListVLANDiscard_Object = MibTableColumn
accessListVLANDiscard = _AccessListVLANDiscard_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 1, 1, 4, 1, 1, 6),
    _AccessListVLANDiscard_Type()
)
accessListVLANDiscard.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accessListVLANDiscard.setStatus("current")
_AccessListVLANRateLimit_Type = Rate
_AccessListVLANRateLimit_Object = MibTableColumn
accessListVLANRateLimit = _AccessListVLANRateLimit_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 1, 1, 4, 1, 1, 7),
    _AccessListVLANRateLimit_Type()
)
accessListVLANRateLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accessListVLANRateLimit.setStatus("current")
_AccessListVLANExceedAction_Type = ExceedAction
_AccessListVLANExceedAction_Object = MibTableColumn
accessListVLANExceedAction = _AccessListVLANExceedAction_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 1, 1, 4, 1, 1, 8),
    _AccessListVLANExceedAction_Type()
)
accessListVLANExceedAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accessListVLANExceedAction.setStatus("current")
_AccessListVLANBurst_Type = Rate
_AccessListVLANBurst_Object = MibTableColumn
accessListVLANBurst = _AccessListVLANBurst_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 1, 1, 4, 1, 1, 9),
    _AccessListVLANBurst_Type()
)
accessListVLANBurst.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accessListVLANBurst.setStatus("current")
_AccessListVLANRedirectIfIndex_Type = Integer32
_AccessListVLANRedirectIfIndex_Object = MibTableColumn
accessListVLANRedirectIfIndex = _AccessListVLANRedirectIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 1, 1, 4, 1, 1, 10),
    _AccessListVLANRedirectIfIndex_Type()
)
accessListVLANRedirectIfIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accessListVLANRedirectIfIndex.setStatus("current")
_AccessListVLANRedirectVlanID_Type = Integer32
_AccessListVLANRedirectVlanID_Object = MibTableColumn
accessListVLANRedirectVlanID = _AccessListVLANRedirectVlanID_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 1, 1, 4, 1, 1, 11),
    _AccessListVLANRedirectVlanID_Type()
)
accessListVLANRedirectVlanID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accessListVLANRedirectVlanID.setStatus("current")
_AccessListVLANRedirectNexthop_Type = IpAddress
_AccessListVLANRedirectNexthop_Object = MibTableColumn
accessListVLANRedirectNexthop = _AccessListVLANRedirectNexthop_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 1, 1, 4, 1, 1, 12),
    _AccessListVLANRedirectNexthop_Type()
)
accessListVLANRedirectNexthop.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accessListVLANRedirectNexthop.setStatus("current")
_AccessListVLANPeakRate_Type = Rate
_AccessListVLANPeakRate_Object = MibTableColumn
accessListVLANPeakRate = _AccessListVLANPeakRate_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 1, 1, 4, 1, 1, 13),
    _AccessListVLANPeakRate_Type()
)
accessListVLANPeakRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accessListVLANPeakRate.setStatus("current")
_AccessListVLANPeakBurst_Type = Rate
_AccessListVLANPeakBurst_Object = MibTableColumn
accessListVLANPeakBurst = _AccessListVLANPeakBurst_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 1, 1, 4, 1, 1, 14),
    _AccessListVLANPeakBurst_Type()
)
accessListVLANPeakBurst.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accessListVLANPeakBurst.setStatus("current")


class _AccessListVLANColorAware_Type(Integer32):
    """Custom type accessListVLANColorAware based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_AccessListVLANColorAware_Type.__name__ = "Integer32"
_AccessListVLANColorAware_Object = MibTableColumn
accessListVLANColorAware = _AccessListVLANColorAware_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 1, 1, 4, 1, 1, 15),
    _AccessListVLANColorAware_Type()
)
accessListVLANColorAware.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accessListVLANColorAware.setStatus("current")


class _AccessListVLANPolicy_Type(Integer32):
    """Custom type accessListVLANPolicy based on Integer32"""
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
        *(("undefined", 0),
          ("dcsp", 1),
          ("priority", 2),
          ("priority-dp", 3))
    )


_AccessListVLANPolicy_Type.__name__ = "Integer32"
_AccessListVLANPolicy_Object = MibTableColumn
accessListVLANPolicy = _AccessListVLANPolicy_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 1, 1, 4, 1, 1, 16),
    _AccessListVLANPolicy_Type()
)
accessListVLANPolicy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accessListVLANPolicy.setStatus("current")


class _AccessListVLANTrafficClass_Type(Integer32):
    """Custom type accessListVLANTrafficClass based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 256),
    )


_AccessListVLANTrafficClass_Type.__name__ = "Integer32"
_AccessListVLANTrafficClass_Object = MibTableColumn
accessListVLANTrafficClass = _AccessListVLANTrafficClass_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 1, 1, 4, 1, 1, 17),
    _AccessListVLANTrafficClass_Type()
)
accessListVLANTrafficClass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accessListVLANTrafficClass.setStatus("current")


class _AccessListVLANSpanRootTrack_Type(Integer32):
    """Custom type accessListVLANSpanRootTrack based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_AccessListVLANSpanRootTrack_Type.__name__ = "Integer32"
_AccessListVLANSpanRootTrack_Object = MibTableColumn
accessListVLANSpanRootTrack = _AccessListVLANSpanRootTrack_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 1, 1, 4, 1, 1, 18),
    _AccessListVLANSpanRootTrack_Type()
)
accessListVLANSpanRootTrack.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    accessListVLANSpanRootTrack.setStatus("current")


class _AccessListVLANUntagFilter_Type(Integer32):
    """Custom type accessListVLANUntagFilter based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_AccessListVLANUntagFilter_Type.__name__ = "Integer32"
_AccessListVLANUntagFilter_Object = MibTableColumn
accessListVLANUntagFilter = _AccessListVLANUntagFilter_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 1, 1, 4, 1, 1, 19),
    _AccessListVLANUntagFilter_Type()
)
accessListVLANUntagFilter.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    accessListVLANUntagFilter.setStatus("current")
_AccessListVLANApplyMirror_Type = TruthValue
_AccessListVLANApplyMirror_Object = MibTableColumn
accessListVLANApplyMirror = _AccessListVLANApplyMirror_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 1, 1, 4, 1, 1, 20),
    _AccessListVLANApplyMirror_Type()
)
accessListVLANApplyMirror.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    accessListVLANApplyMirror.setStatus("current")
_AccessListVLANStatistics_Type = AccessListStatistics
_AccessListVLANStatistics_Object = MibTableColumn
accessListVLANStatistics = _AccessListVLANStatistics_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 1, 1, 4, 1, 1, 21),
    _AccessListVLANStatistics_Type()
)
accessListVLANStatistics.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    accessListVLANStatistics.setStatus("current")
_AccessListVLANDirection_Type = AccessListDirection
_AccessListVLANDirection_Object = MibTableColumn
accessListVLANDirection = _AccessListVLANDirection_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 1, 1, 4, 1, 1, 22),
    _AccessListVLANDirection_Type()
)
accessListVLANDirection.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    accessListVLANDirection.setStatus("current")
_AccessListsServices_ObjectIdentity = ObjectIdentity
accessListsServices = _AccessListsServices_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 1, 1, 5)
)
_AccessListSapTable_Object = MibTable
accessListSapTable = _AccessListSapTable_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 1, 1, 5, 1)
)
if mibBuilder.loadTexts:
    accessListSapTable.setStatus("current")
_AccessListSapEntry_Object = MibTableRow
accessListSapEntry = _AccessListSapEntry_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 1, 1, 5, 1, 1)
)
accessListSapEntry.setIndexNames(
    (0, "PRVT-SERV-MIB", "svcId"),
    (0, "PRVT-SERV-MIB", "sapPortId"),
    (0, "PRVT-SERV-MIB", "sapEncapValue"),
    (0, "PRVT-SWITCH-ACCESS-LIST-MIB", "accessListSapTableIndex"),
    (0, "PRVT-SWITCH-ACCESS-LIST-MIB", "accessListSapGroupIndex"),
)
if mibBuilder.loadTexts:
    accessListSapEntry.setStatus("current")


class _AccessListSapTableIndex_Type(Integer32):
    """Custom type accessListSapTableIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_AccessListSapTableIndex_Type.__name__ = "Integer32"
_AccessListSapTableIndex_Object = MibTableColumn
accessListSapTableIndex = _AccessListSapTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 1, 1, 5, 1, 1, 1),
    _AccessListSapTableIndex_Type()
)
accessListSapTableIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    accessListSapTableIndex.setStatus("current")


class _AccessListSapGroupIndex_Type(Integer32):
    """Custom type accessListSapGroupIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_AccessListSapGroupIndex_Type.__name__ = "Integer32"
_AccessListSapGroupIndex_Object = MibTableColumn
accessListSapGroupIndex = _AccessListSapGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 1, 1, 5, 1, 1, 2),
    _AccessListSapGroupIndex_Type()
)
accessListSapGroupIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    accessListSapGroupIndex.setStatus("current")
_AccessListSapRowStatus_Type = RowStatus
_AccessListSapRowStatus_Object = MibTableColumn
accessListSapRowStatus = _AccessListSapRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 1, 1, 5, 1, 1, 3),
    _AccessListSapRowStatus_Type()
)
accessListSapRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accessListSapRowStatus.setStatus("current")
_AccessListSapRateLimit_Type = Rate
_AccessListSapRateLimit_Object = MibTableColumn
accessListSapRateLimit = _AccessListSapRateLimit_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 1, 1, 5, 1, 1, 4),
    _AccessListSapRateLimit_Type()
)
accessListSapRateLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accessListSapRateLimit.setStatus("current")
_AccessListSapExceedAction_Type = ExceedAction
_AccessListSapExceedAction_Object = MibTableColumn
accessListSapExceedAction = _AccessListSapExceedAction_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 1, 1, 5, 1, 1, 5),
    _AccessListSapExceedAction_Type()
)
accessListSapExceedAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accessListSapExceedAction.setStatus("current")
_AccessListSapBurst_Type = Rate
_AccessListSapBurst_Object = MibTableColumn
accessListSapBurst = _AccessListSapBurst_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 1, 1, 5, 1, 1, 6),
    _AccessListSapBurst_Type()
)
accessListSapBurst.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accessListSapBurst.setStatus("current")
_AccessListSapPeakRate_Type = Rate
_AccessListSapPeakRate_Object = MibTableColumn
accessListSapPeakRate = _AccessListSapPeakRate_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 1, 1, 5, 1, 1, 7),
    _AccessListSapPeakRate_Type()
)
accessListSapPeakRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accessListSapPeakRate.setStatus("current")
_AccessListSapPeakBurst_Type = Rate
_AccessListSapPeakBurst_Object = MibTableColumn
accessListSapPeakBurst = _AccessListSapPeakBurst_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 1, 1, 5, 1, 1, 8),
    _AccessListSapPeakBurst_Type()
)
accessListSapPeakBurst.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accessListSapPeakBurst.setStatus("current")


class _AccessListSapColorAware_Type(Integer32):
    """Custom type accessListSapColorAware based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_AccessListSapColorAware_Type.__name__ = "Integer32"
_AccessListSapColorAware_Object = MibTableColumn
accessListSapColorAware = _AccessListSapColorAware_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 1, 1, 5, 1, 1, 9),
    _AccessListSapColorAware_Type()
)
accessListSapColorAware.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accessListSapColorAware.setStatus("current")
_AccessListSapTxq_Type = Integer32
_AccessListSapTxq_Object = MibTableColumn
accessListSapTxq = _AccessListSapTxq_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 1, 1, 5, 1, 1, 10),
    _AccessListSapTxq_Type()
)
accessListSapTxq.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    accessListSapTxq.setStatus("current")
_AccessListSapTxqDropLevel_Type = TxqDropLevel
_AccessListSapTxqDropLevel_Object = MibTableColumn
accessListSapTxqDropLevel = _AccessListSapTxqDropLevel_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 1, 1, 5, 1, 1, 11),
    _AccessListSapTxqDropLevel_Type()
)
accessListSapTxqDropLevel.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    accessListSapTxqDropLevel.setStatus("current")
_AccessListSapStatistics_Type = AccessListStatistics
_AccessListSapStatistics_Object = MibTableColumn
accessListSapStatistics = _AccessListSapStatistics_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 1, 1, 5, 1, 1, 12),
    _AccessListSapStatistics_Type()
)
accessListSapStatistics.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    accessListSapStatistics.setStatus("current")
_AccessListSapRateStatistics_Type = AccessListStatistics
_AccessListSapRateStatistics_Object = MibTableColumn
accessListSapRateStatistics = _AccessListSapRateStatistics_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 1, 1, 5, 1, 1, 13),
    _AccessListSapRateStatistics_Type()
)
accessListSapRateStatistics.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    accessListSapRateStatistics.setStatus("current")
_AccessListSapDirection_Type = AccessListDirection
_AccessListSapDirection_Object = MibTableColumn
accessListSapDirection = _AccessListSapDirection_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 1, 1, 5, 1, 1, 14),
    _AccessListSapDirection_Type()
)
accessListSapDirection.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    accessListSapDirection.setStatus("current")
_AccessListsInterfaceStatistics_ObjectIdentity = ObjectIdentity
accessListsInterfaceStatistics = _AccessListsInterfaceStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 1, 1, 6)
)
_AccessListInterfaceStatisticsTable_Object = MibTable
accessListInterfaceStatisticsTable = _AccessListInterfaceStatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 1, 1, 6, 1)
)
if mibBuilder.loadTexts:
    accessListInterfaceStatisticsTable.setStatus("current")
_AccessListInterfaceStatisticsEntry_Object = MibTableRow
accessListInterfaceStatisticsEntry = _AccessListInterfaceStatisticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 1, 1, 6, 1, 1)
)
accessListInterfaceStatisticsEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "PRVT-SWITCH-ACCESS-LIST-MIB", "accessListInterfaceStatisticsGroupIndex"),
)
if mibBuilder.loadTexts:
    accessListInterfaceStatisticsEntry.setStatus("current")


class _AccessListInterfaceStatisticsGroupIndex_Type(Integer32):
    """Custom type accessListInterfaceStatisticsGroupIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_AccessListInterfaceStatisticsGroupIndex_Type.__name__ = "Integer32"
_AccessListInterfaceStatisticsGroupIndex_Object = MibTableColumn
accessListInterfaceStatisticsGroupIndex = _AccessListInterfaceStatisticsGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 1, 1, 6, 1, 1, 1),
    _AccessListInterfaceStatisticsGroupIndex_Type()
)
accessListInterfaceStatisticsGroupIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    accessListInterfaceStatisticsGroupIndex.setStatus("current")
_AccessListInterfaceGreenBytes_Type = Integer32
_AccessListInterfaceGreenBytes_Object = MibTableColumn
accessListInterfaceGreenBytes = _AccessListInterfaceGreenBytes_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 1, 1, 6, 1, 1, 2),
    _AccessListInterfaceGreenBytes_Type()
)
accessListInterfaceGreenBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accessListInterfaceGreenBytes.setStatus("current")
_AccessListInterfaceYellowBytes_Type = Integer32
_AccessListInterfaceYellowBytes_Object = MibTableColumn
accessListInterfaceYellowBytes = _AccessListInterfaceYellowBytes_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 1, 1, 6, 1, 1, 3),
    _AccessListInterfaceYellowBytes_Type()
)
accessListInterfaceYellowBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accessListInterfaceYellowBytes.setStatus("current")
_AccessListInterfaceRedBytes_Type = Integer32
_AccessListInterfaceRedBytes_Object = MibTableColumn
accessListInterfaceRedBytes = _AccessListInterfaceRedBytes_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 1, 1, 6, 1, 1, 4),
    _AccessListInterfaceRedBytes_Type()
)
accessListInterfaceRedBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accessListInterfaceRedBytes.setStatus("current")
_AccessListInterfaceClassifiedPackets_Type = Integer32
_AccessListInterfaceClassifiedPackets_Object = MibTableColumn
accessListInterfaceClassifiedPackets = _AccessListInterfaceClassifiedPackets_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 1, 1, 6, 1, 1, 5),
    _AccessListInterfaceClassifiedPackets_Type()
)
accessListInterfaceClassifiedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accessListInterfaceClassifiedPackets.setStatus("current")
_AccessListsServicesStatistics_ObjectIdentity = ObjectIdentity
accessListsServicesStatistics = _AccessListsServicesStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 1, 1, 7)
)
_AccessListSapStatisticsTable_Object = MibTable
accessListSapStatisticsTable = _AccessListSapStatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 1, 1, 7, 1)
)
if mibBuilder.loadTexts:
    accessListSapStatisticsTable.setStatus("current")
_AccessListSapStatisticsEntry_Object = MibTableRow
accessListSapStatisticsEntry = _AccessListSapStatisticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 1, 1, 7, 1, 1)
)
accessListSapStatisticsEntry.setIndexNames(
    (0, "PRVT-SERV-MIB", "svcId"),
    (0, "PRVT-SERV-MIB", "sapPortId"),
    (0, "PRVT-SERV-MIB", "sapEncapValue"),
    (0, "PRVT-SWITCH-ACCESS-LIST-MIB", "accessListSapStatisticsGroupIndex"),
)
if mibBuilder.loadTexts:
    accessListSapStatisticsEntry.setStatus("current")


class _AccessListSapStatisticsGroupIndex_Type(Integer32):
    """Custom type accessListSapStatisticsGroupIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_AccessListSapStatisticsGroupIndex_Type.__name__ = "Integer32"
_AccessListSapStatisticsGroupIndex_Object = MibTableColumn
accessListSapStatisticsGroupIndex = _AccessListSapStatisticsGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 1, 1, 7, 1, 1, 1),
    _AccessListSapStatisticsGroupIndex_Type()
)
accessListSapStatisticsGroupIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    accessListSapStatisticsGroupIndex.setStatus("current")
_AccessListSapGreenBytes_Type = Integer32
_AccessListSapGreenBytes_Object = MibTableColumn
accessListSapGreenBytes = _AccessListSapGreenBytes_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 1, 1, 7, 1, 1, 2),
    _AccessListSapGreenBytes_Type()
)
accessListSapGreenBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accessListSapGreenBytes.setStatus("current")
_AccessListSapYellowBytes_Type = Integer32
_AccessListSapYellowBytes_Object = MibTableColumn
accessListSapYellowBytes = _AccessListSapYellowBytes_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 1, 1, 7, 1, 1, 3),
    _AccessListSapYellowBytes_Type()
)
accessListSapYellowBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accessListSapYellowBytes.setStatus("current")
_AccessListSapRedBytes_Type = Integer32
_AccessListSapRedBytes_Object = MibTableColumn
accessListSapRedBytes = _AccessListSapRedBytes_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 1, 1, 7, 1, 1, 4),
    _AccessListSapRedBytes_Type()
)
accessListSapRedBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accessListSapRedBytes.setStatus("current")
_AccessListSapClassifiedPackets_Type = Integer32
_AccessListSapClassifiedPackets_Object = MibTableColumn
accessListSapClassifiedPackets = _AccessListSapClassifiedPackets_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 1, 1, 7, 1, 1, 5),
    _AccessListSapClassifiedPackets_Type()
)
accessListSapClassifiedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accessListSapClassifiedPackets.setStatus("current")
_Isp_ObjectIdentity = ObjectIdentity
isp = _Isp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 1, 2)
)
_IspUpLinkTable_Object = MibTable
ispUpLinkTable = _IspUpLinkTable_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 1, 2, 1)
)
if mibBuilder.loadTexts:
    ispUpLinkTable.setStatus("current")
_IspUpLinkEntry_Object = MibTableRow
ispUpLinkEntry = _IspUpLinkEntry_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 1, 2, 1, 1)
)
ispUpLinkEntry.setIndexNames(
    (0, "PRVT-SWITCH-ACCESS-LIST-MIB", "ispUpLinkIndex"),
)
if mibBuilder.loadTexts:
    ispUpLinkEntry.setStatus("current")


class _IspUpLinkIndex_Type(Integer32):
    """Custom type ispUpLinkIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_IspUpLinkIndex_Type.__name__ = "Integer32"
_IspUpLinkIndex_Object = MibTableColumn
ispUpLinkIndex = _IspUpLinkIndex_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 1, 2, 1, 1, 1),
    _IspUpLinkIndex_Type()
)
ispUpLinkIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ispUpLinkIndex.setStatus("current")
_IspUpLinkIfIndex_Type = Integer32
_IspUpLinkIfIndex_Object = MibTableColumn
ispUpLinkIfIndex = _IspUpLinkIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 1, 2, 1, 1, 2),
    _IspUpLinkIfIndex_Type()
)
ispUpLinkIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ispUpLinkIfIndex.setStatus("current")
_IspUpLinkType_Type = ISPType
_IspUpLinkType_Object = MibTableColumn
ispUpLinkType = _IspUpLinkType_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 1, 2, 1, 1, 3),
    _IspUpLinkType_Type()
)
ispUpLinkType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ispUpLinkType.setStatus("current")


class _IspUpLinkAccessGroup_Type(Integer32):
    """Custom type ispUpLinkAccessGroup based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 199),
    )


_IspUpLinkAccessGroup_Type.__name__ = "Integer32"
_IspUpLinkAccessGroup_Object = MibTableColumn
ispUpLinkAccessGroup = _IspUpLinkAccessGroup_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 1, 2, 1, 1, 4),
    _IspUpLinkAccessGroup_Type()
)
ispUpLinkAccessGroup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ispUpLinkAccessGroup.setStatus("current")


class _IspUpLinkVLANid_Type(Integer32):
    """Custom type ispUpLinkVLANid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4000),
    )


_IspUpLinkVLANid_Type.__name__ = "Integer32"
_IspUpLinkVLANid_Object = MibTableColumn
ispUpLinkVLANid = _IspUpLinkVLANid_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 1, 2, 1, 1, 5),
    _IspUpLinkVLANid_Type()
)
ispUpLinkVLANid.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ispUpLinkVLANid.setStatus("current")
_IspUpLinkVLANtag_Type = VlanTag
_IspUpLinkVLANtag_Object = MibTableColumn
ispUpLinkVLANtag = _IspUpLinkVLANtag_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 1, 2, 1, 1, 6),
    _IspUpLinkVLANtag_Type()
)
ispUpLinkVLANtag.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ispUpLinkVLANtag.setStatus("current")
_IspUpLinkRowStatus_Type = RowStatus
_IspUpLinkRowStatus_Object = MibTableColumn
ispUpLinkRowStatus = _IspUpLinkRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 1, 2, 1, 1, 7),
    _IspUpLinkRowStatus_Type()
)
ispUpLinkRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ispUpLinkRowStatus.setStatus("current")
_IspUserInterfaceTable_Object = MibTable
ispUserInterfaceTable = _IspUserInterfaceTable_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 1, 2, 2)
)
if mibBuilder.loadTexts:
    ispUserInterfaceTable.setStatus("current")
_IspUserInterfaceEntry_Object = MibTableRow
ispUserInterfaceEntry = _IspUserInterfaceEntry_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 1, 2, 2, 1)
)
ispUserInterfaceEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    ispUserInterfaceEntry.setStatus("current")
_IspUserInterfaceAssigen_Type = AssigenValue
_IspUserInterfaceAssigen_Object = MibTableColumn
ispUserInterfaceAssigen = _IspUserInterfaceAssigen_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 1, 2, 2, 1, 1),
    _IspUserInterfaceAssigen_Type()
)
ispUserInterfaceAssigen.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ispUserInterfaceAssigen.setStatus("current")


class _IspUserInterfaceIspUplinkIndex_Type(Integer32):
    """Custom type ispUserInterfaceIspUplinkIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_IspUserInterfaceIspUplinkIndex_Type.__name__ = "Integer32"
_IspUserInterfaceIspUplinkIndex_Object = MibTableColumn
ispUserInterfaceIspUplinkIndex = _IspUserInterfaceIspUplinkIndex_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 1, 2, 2, 1, 2),
    _IspUserInterfaceIspUplinkIndex_Type()
)
ispUserInterfaceIspUplinkIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ispUserInterfaceIspUplinkIndex.setStatus("current")
_IspUserInterfaceRateLimit_Type = Rate
_IspUserInterfaceRateLimit_Object = MibTableColumn
ispUserInterfaceRateLimit = _IspUserInterfaceRateLimit_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 1, 2, 2, 1, 3),
    _IspUserInterfaceRateLimit_Type()
)
ispUserInterfaceRateLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ispUserInterfaceRateLimit.setStatus("current")
_IspUserInterfaceConformAction_Type = ConformAction
_IspUserInterfaceConformAction_Object = MibTableColumn
ispUserInterfaceConformAction = _IspUserInterfaceConformAction_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 1, 2, 2, 1, 4),
    _IspUserInterfaceConformAction_Type()
)
ispUserInterfaceConformAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ispUserInterfaceConformAction.setStatus("current")
_IspUserInterfaceExceedAction_Type = ExceedAction
_IspUserInterfaceExceedAction_Object = MibTableColumn
ispUserInterfaceExceedAction = _IspUserInterfaceExceedAction_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 1, 2, 2, 1, 5),
    _IspUserInterfaceExceedAction_Type()
)
ispUserInterfaceExceedAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ispUserInterfaceExceedAction.setStatus("current")
_IspUserInterfaceShaper_Type = Shaper
_IspUserInterfaceShaper_Object = MibTableColumn
ispUserInterfaceShaper = _IspUserInterfaceShaper_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 1, 2, 2, 1, 6),
    _IspUserInterfaceShaper_Type()
)
ispUserInterfaceShaper.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ispUserInterfaceShaper.setStatus("current")
_PrvtSwitchAccessListConformance_ObjectIdentity = ObjectIdentity
prvtSwitchAccessListConformance = _PrvtSwitchAccessListConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 1, 3)
)
_PrvtSwitchAccessListMibGroups_ObjectIdentity = ObjectIdentity
prvtSwitchAccessListMibGroups = _PrvtSwitchAccessListMibGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 1, 3, 1)
)

# Managed Objects groups


# Notification objects

standardAccessListRuleMatched = NotificationType(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 1, 0, 1)
)
standardAccessListRuleMatched.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("Q-BRIDGE-MIB", "dot1qVlanStatus"),
        ("PRVT-SWITCH-ACCESS-LIST-MIB", "standardAccessListAction"))
)
if mibBuilder.loadTexts:
    standardAccessListRuleMatched.setStatus(
        "current"
    )

extendedAccessListRuleMatched = NotificationType(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 1, 0, 2)
)
extendedAccessListRuleMatched.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("Q-BRIDGE-MIB", "dot1qVlanStatus"),
        ("PRVT-SWITCH-ACCESS-LIST-MIB", "extendedAccessListAction"))
)
if mibBuilder.loadTexts:
    extendedAccessListRuleMatched.setStatus(
        "current"
    )

macAccessListRuleMatched = NotificationType(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 1, 0, 3)
)
macAccessListRuleMatched.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("Q-BRIDGE-MIB", "dot1qVlanStatus"),
        ("PRVT-SWITCH-ACCESS-LIST-MIB", "macAccessListAction"))
)
if mibBuilder.loadTexts:
    macAccessListRuleMatched.setStatus(
        "current"
    )

etherTypeAccessListRuleMatched = NotificationType(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 1, 0, 4)
)
etherTypeAccessListRuleMatched.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("Q-BRIDGE-MIB", "dot1qVlanStatus"),
        ("PRVT-SWITCH-ACCESS-LIST-MIB", "etherTypeAccessListAction"))
)
if mibBuilder.loadTexts:
    etherTypeAccessListRuleMatched.setStatus(
        "current"
    )


# Notifications groups

prvtSwitchAccessListNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 1, 3, 1, 1)
)
prvtSwitchAccessListNotificationGroup.setObjects(
      *(("PRVT-SWITCH-ACCESS-LIST-MIB", "standardAccessListRuleMatched"),
        ("PRVT-SWITCH-ACCESS-LIST-MIB", "extendedAccessListRuleMatched"),
        ("PRVT-SWITCH-ACCESS-LIST-MIB", "macAccessListRuleMatched"),
        ("PRVT-SWITCH-ACCESS-LIST-MIB", "etherTypeAccessListRuleMatched"))
)
if mibBuilder.loadTexts:
    prvtSwitchAccessListNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "PRVT-SWITCH-ACCESS-LIST-MIB",
    **{"AccessListAction": AccessListAction,
       "IpProtocol": IpProtocol,
       "PortDef": PortDef,
       "Rate": Rate,
       "ExceedAction": ExceedAction,
       "VlanTag": VlanTag,
       "ISPType": ISPType,
       "Shaper": Shaper,
       "ConformAction": ConformAction,
       "AssigenValue": AssigenValue,
       "AccessListModifyTos": AccessListModifyTos,
       "AccessListEstablished": AccessListEstablished,
       "AccessListDiscard": AccessListDiscard,
       "AccessListRemarkString": AccessListRemarkString,
       "TxqDropLevel": TxqDropLevel,
       "MatchTraffic": MatchTraffic,
       "AccessListStatistics": AccessListStatistics,
       "AccessListDirection": AccessListDirection,
       "prvtSwitchAccessListMib": prvtSwitchAccessListMib,
       "prvtSwitchAccessListNotifications": prvtSwitchAccessListNotifications,
       "standardAccessListRuleMatched": standardAccessListRuleMatched,
       "extendedAccessListRuleMatched": extendedAccessListRuleMatched,
       "macAccessListRuleMatched": macAccessListRuleMatched,
       "etherTypeAccessListRuleMatched": etherTypeAccessListRuleMatched,
       "accessLists": accessLists,
       "accessListTemplate": accessListTemplate,
       "accessGroupsDefinitions": accessGroupsDefinitions,
       "accessListControlTable": accessListControlTable,
       "accessListControlEntry": accessListControlEntry,
       "accessListControlListGroup": accessListControlListGroup,
       "accessListControlRowStatus": accessListControlRowStatus,
       "standardAccessListTable": standardAccessListTable,
       "standardAccessListEntry": standardAccessListEntry,
       "standardAccessListIndex": standardAccessListIndex,
       "standardAccessListAction": standardAccessListAction,
       "standardAccessListIpSrc": standardAccessListIpSrc,
       "standardAccessListIpMASKsrc": standardAccessListIpMASKsrc,
       "standardAccessListRemark": standardAccessListRemark,
       "standardAccessListLog": standardAccessListLog,
       "standardAccessListVpt": standardAccessListVpt,
       "standardAccessListRowStatus": standardAccessListRowStatus,
       "standardAccessListVlanId": standardAccessListVlanId,
       "standardAccessListVlanMask": standardAccessListVlanMask,
       "standardAccessListProviderVlanId": standardAccessListProviderVlanId,
       "standardAccessListProviderVlanMask": standardAccessListProviderVlanMask,
       "standardAccessListProviderVpt": standardAccessListProviderVpt,
       "standardAccessListUntaggedMode": standardAccessListUntaggedMode,
       "standardAccessListDropLevel": standardAccessListDropLevel,
       "standardAccessListDscp": standardAccessListDscp,
       "extendedAccessListTable": extendedAccessListTable,
       "extendedAccessListEntry": extendedAccessListEntry,
       "extendedAccessListIndex": extendedAccessListIndex,
       "extendedAccessListAction": extendedAccessListAction,
       "extendedAccessListIpProtocol": extendedAccessListIpProtocol,
       "extendedAccessListIpSrc": extendedAccessListIpSrc,
       "extendedAccessListIpMASKsrc": extendedAccessListIpMASKsrc,
       "extendedAccessListPortDefSrc": extendedAccessListPortDefSrc,
       "extendedAccessListPortNumSrc": extendedAccessListPortNumSrc,
       "extendedAccessListPortRangeSrc": extendedAccessListPortRangeSrc,
       "extendedAccessListIpDest": extendedAccessListIpDest,
       "extendedAccessListIpMASKdst": extendedAccessListIpMASKdst,
       "extendedAccessListPortDefDst": extendedAccessListPortDefDst,
       "extendedAccessListPortNumDst": extendedAccessListPortNumDst,
       "extendedAccessListPortRangeDst": extendedAccessListPortRangeDst,
       "extendedAccessListTos": extendedAccessListTos,
       "extendedAccessListPrec": extendedAccessListPrec,
       "extendedAccessListModifyTos": extendedAccessListModifyTos,
       "extendedAccessListRemark": extendedAccessListRemark,
       "extendedAccessListIcmpType": extendedAccessListIcmpType,
       "extendedAccessListIcmpCode": extendedAccessListIcmpCode,
       "extendedAccessListIgmpType": extendedAccessListIgmpType,
       "extendedAccessListEstablished": extendedAccessListEstablished,
       "extendedAccessListLog": extendedAccessListLog,
       "extendedAccessListVpt": extendedAccessListVpt,
       "extendedAccessListRowStatus": extendedAccessListRowStatus,
       "extendedAccessListVlanId": extendedAccessListVlanId,
       "extendedAccessListVlanMask": extendedAccessListVlanMask,
       "extendedAccessListProviderVlanId": extendedAccessListProviderVlanId,
       "extendedAccessListProviderVlanMask": extendedAccessListProviderVlanMask,
       "extendedAccessListProviderVpt": extendedAccessListProviderVpt,
       "extendedAccessListUntaggedMode": extendedAccessListUntaggedMode,
       "extendedAccessListDropLevel": extendedAccessListDropLevel,
       "extendedAccessListDscp": extendedAccessListDscp,
       "macAccessListTable": macAccessListTable,
       "macAccessListEntry": macAccessListEntry,
       "macAccessListIndex": macAccessListIndex,
       "macAccessListAction": macAccessListAction,
       "macAccessListMacSrc": macAccessListMacSrc,
       "macAccessListMacSrcMask": macAccessListMacSrcMask,
       "macAccessListMacDst": macAccessListMacDst,
       "macAccessListMacDstMask": macAccessListMacDstMask,
       "macAccessListRemark": macAccessListRemark,
       "macAccessListLog": macAccessListLog,
       "macAccessListRowStatus": macAccessListRowStatus,
       "macAccessListTos": macAccessListTos,
       "macAccessListPrecedence": macAccessListPrecedence,
       "macAccessListVpt": macAccessListVpt,
       "macAccessListVlanId": macAccessListVlanId,
       "macAccessListVlanMask": macAccessListVlanMask,
       "macAccessListInnerVlanId": macAccessListInnerVlanId,
       "macAccessListInnerVlanMask": macAccessListInnerVlanMask,
       "macAccessListInnerVpt": macAccessListInnerVpt,
       "macAccessListEtherType": macAccessListEtherType,
       "macAccessListDscp": macAccessListDscp,
       "macAccessListMatchTraffic": macAccessListMatchTraffic,
       "macAccessListMatchTrafficPort": macAccessListMatchTrafficPort,
       "macAccessListUntaggedMode": macAccessListUntaggedMode,
       "macAccessListDropLevel": macAccessListDropLevel,
       "etherTypeAccessListTable": etherTypeAccessListTable,
       "etherTypeAccessListEntry": etherTypeAccessListEntry,
       "etherTypeAccessListIndex": etherTypeAccessListIndex,
       "etherTypeAccessListAction": etherTypeAccessListAction,
       "etherTypeAccessListEtherType": etherTypeAccessListEtherType,
       "etherTypeAccessListEtherTypeCodeMask": etherTypeAccessListEtherTypeCodeMask,
       "etherTypeAccessListRemark": etherTypeAccessListRemark,
       "etherTypeAccessListLog": etherTypeAccessListLog,
       "etherTypeAccessListRowStatus": etherTypeAccessListRowStatus,
       "etherTypeAccessListVlanId": etherTypeAccessListVlanId,
       "etherTypeAccessListVlanMask": etherTypeAccessListVlanMask,
       "etherTypeAccessListProviderVlanId": etherTypeAccessListProviderVlanId,
       "etherTypeAccessListProviderVlanMask": etherTypeAccessListProviderVlanMask,
       "etherTypeAccessListProviderVpt": etherTypeAccessListProviderVpt,
       "accessListsInterfaces": accessListsInterfaces,
       "accessListInterfaceTable": accessListInterfaceTable,
       "accessListInterfaceEntry": accessListInterfaceEntry,
       "accessListInterfaceTableIndex": accessListInterfaceTableIndex,
       "accessListInterfaceGroupIndex": accessListInterfaceGroupIndex,
       "accessListInterfaceDscp": accessListInterfaceDscp,
       "accessListInterfaceRowStatus": accessListInterfaceRowStatus,
       "accessListInterfacePriority": accessListInterfacePriority,
       "accessListInterfaceDiscard": accessListInterfaceDiscard,
       "accessListInterfaceRateLimit": accessListInterfaceRateLimit,
       "accessListInterfaceExceedAction": accessListInterfaceExceedAction,
       "accessListInterfaceShaper": accessListInterfaceShaper,
       "accessListInterfaceBurst": accessListInterfaceBurst,
       "accessListInterfaceRedirectIfIndex": accessListInterfaceRedirectIfIndex,
       "accessListInterfaceRedirectVlanID": accessListInterfaceRedirectVlanID,
       "accessListInterfaceRedirectNexthop": accessListInterfaceRedirectNexthop,
       "accessListInterfacePeakRate": accessListInterfacePeakRate,
       "accessListInterfacePeakBurst": accessListInterfacePeakBurst,
       "accessListInterfaceColorAware": accessListInterfaceColorAware,
       "accessListInterfacePolicy": accessListInterfacePolicy,
       "accessListInterfaceTrafficClass": accessListInterfaceTrafficClass,
       "accessListInterfaceSpanRootTrack": accessListInterfaceSpanRootTrack,
       "accessListInterfaceUntagFilter": accessListInterfaceUntagFilter,
       "accessListInterfaceTxq": accessListInterfaceTxq,
       "accessListInterfaceTxqDropLevel": accessListInterfaceTxqDropLevel,
       "accessListInterfaceApplyMirror": accessListInterfaceApplyMirror,
       "accessListInterfaceStatistics": accessListInterfaceStatistics,
       "accessListInterfaceDirection": accessListInterfaceDirection,
       "accessListInterfaceRateStatistics": accessListInterfaceRateStatistics,
       "accessListsVLAN": accessListsVLAN,
       "accessListVLANTable": accessListVLANTable,
       "accessListVLANEntry": accessListVLANEntry,
       "accessListVLANTableIndex": accessListVLANTableIndex,
       "accessListVLANGroupIndex": accessListVLANGroupIndex,
       "accessListVLANDscp": accessListVLANDscp,
       "accessListVLANRowStatus": accessListVLANRowStatus,
       "accessListVLANPriority": accessListVLANPriority,
       "accessListVLANDiscard": accessListVLANDiscard,
       "accessListVLANRateLimit": accessListVLANRateLimit,
       "accessListVLANExceedAction": accessListVLANExceedAction,
       "accessListVLANBurst": accessListVLANBurst,
       "accessListVLANRedirectIfIndex": accessListVLANRedirectIfIndex,
       "accessListVLANRedirectVlanID": accessListVLANRedirectVlanID,
       "accessListVLANRedirectNexthop": accessListVLANRedirectNexthop,
       "accessListVLANPeakRate": accessListVLANPeakRate,
       "accessListVLANPeakBurst": accessListVLANPeakBurst,
       "accessListVLANColorAware": accessListVLANColorAware,
       "accessListVLANPolicy": accessListVLANPolicy,
       "accessListVLANTrafficClass": accessListVLANTrafficClass,
       "accessListVLANSpanRootTrack": accessListVLANSpanRootTrack,
       "accessListVLANUntagFilter": accessListVLANUntagFilter,
       "accessListVLANApplyMirror": accessListVLANApplyMirror,
       "accessListVLANStatistics": accessListVLANStatistics,
       "accessListVLANDirection": accessListVLANDirection,
       "accessListsServices": accessListsServices,
       "accessListSapTable": accessListSapTable,
       "accessListSapEntry": accessListSapEntry,
       "accessListSapTableIndex": accessListSapTableIndex,
       "accessListSapGroupIndex": accessListSapGroupIndex,
       "accessListSapRowStatus": accessListSapRowStatus,
       "accessListSapRateLimit": accessListSapRateLimit,
       "accessListSapExceedAction": accessListSapExceedAction,
       "accessListSapBurst": accessListSapBurst,
       "accessListSapPeakRate": accessListSapPeakRate,
       "accessListSapPeakBurst": accessListSapPeakBurst,
       "accessListSapColorAware": accessListSapColorAware,
       "accessListSapTxq": accessListSapTxq,
       "accessListSapTxqDropLevel": accessListSapTxqDropLevel,
       "accessListSapStatistics": accessListSapStatistics,
       "accessListSapRateStatistics": accessListSapRateStatistics,
       "accessListSapDirection": accessListSapDirection,
       "accessListsInterfaceStatistics": accessListsInterfaceStatistics,
       "accessListInterfaceStatisticsTable": accessListInterfaceStatisticsTable,
       "accessListInterfaceStatisticsEntry": accessListInterfaceStatisticsEntry,
       "accessListInterfaceStatisticsGroupIndex": accessListInterfaceStatisticsGroupIndex,
       "accessListInterfaceGreenBytes": accessListInterfaceGreenBytes,
       "accessListInterfaceYellowBytes": accessListInterfaceYellowBytes,
       "accessListInterfaceRedBytes": accessListInterfaceRedBytes,
       "accessListInterfaceClassifiedPackets": accessListInterfaceClassifiedPackets,
       "accessListsServicesStatistics": accessListsServicesStatistics,
       "accessListSapStatisticsTable": accessListSapStatisticsTable,
       "accessListSapStatisticsEntry": accessListSapStatisticsEntry,
       "accessListSapStatisticsGroupIndex": accessListSapStatisticsGroupIndex,
       "accessListSapGreenBytes": accessListSapGreenBytes,
       "accessListSapYellowBytes": accessListSapYellowBytes,
       "accessListSapRedBytes": accessListSapRedBytes,
       "accessListSapClassifiedPackets": accessListSapClassifiedPackets,
       "isp": isp,
       "ispUpLinkTable": ispUpLinkTable,
       "ispUpLinkEntry": ispUpLinkEntry,
       "ispUpLinkIndex": ispUpLinkIndex,
       "ispUpLinkIfIndex": ispUpLinkIfIndex,
       "ispUpLinkType": ispUpLinkType,
       "ispUpLinkAccessGroup": ispUpLinkAccessGroup,
       "ispUpLinkVLANid": ispUpLinkVLANid,
       "ispUpLinkVLANtag": ispUpLinkVLANtag,
       "ispUpLinkRowStatus": ispUpLinkRowStatus,
       "ispUserInterfaceTable": ispUserInterfaceTable,
       "ispUserInterfaceEntry": ispUserInterfaceEntry,
       "ispUserInterfaceAssigen": ispUserInterfaceAssigen,
       "ispUserInterfaceIspUplinkIndex": ispUserInterfaceIspUplinkIndex,
       "ispUserInterfaceRateLimit": ispUserInterfaceRateLimit,
       "ispUserInterfaceConformAction": ispUserInterfaceConformAction,
       "ispUserInterfaceExceedAction": ispUserInterfaceExceedAction,
       "ispUserInterfaceShaper": ispUserInterfaceShaper,
       "prvtSwitchAccessListConformance": prvtSwitchAccessListConformance,
       "prvtSwitchAccessListMibGroups": prvtSwitchAccessListMibGroups,
       "prvtSwitchAccessListNotificationGroup": prvtSwitchAccessListNotificationGroup}
)
