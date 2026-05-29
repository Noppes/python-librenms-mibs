# SNMP MIB module (HH3C-ACL-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\comware\HH3C-ACL-MIB

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

(hh3cCommon,) = mibBuilder.importSymbols(
    "HH3C-OID-MIB",
    "hh3cCommon")

(InetAddress,
 InetAddressPrefixLength,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressPrefixLength",
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

hh3cAcl = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8)
)
if mibBuilder.loadTexts:
    hh3cAcl.setRevisions(
        ("2014-10-20 10:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class RuleAction(TextualConvention, Integer32):
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
        *(("invalid", 1),
          ("permit", 2),
          ("deny", 3))
    )



class CounterClear(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("cleared", 1),
          ("nouse", 2))
    )



class PortOp(TextualConvention, Integer32):
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
        *(("invalid", 0),
          ("lt", 1),
          ("eq", 2),
          ("gt", 3),
          ("neq", 4),
          ("range", 5))
    )



class DSCPValue(TextualConvention, Integer32):
    status = "current"
    displayHint = "d"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
        ValueRangeConstraint(255, 255),
    )



class TCPFlag(TextualConvention, Integer32):
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
        *(("invalid", 0),
          ("tcpack", 1),
          ("tcpfin", 2),
          ("tcppsh", 3),
          ("tcprst", 4),
          ("tcpsyn", 5),
          ("tcpurg", 6))
    )



class FragmentFlag(TextualConvention, Integer32):
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
        *(("invalid", 0),
          ("fragment", 1),
          ("fragmentSubseq", 2),
          ("nonFragment", 3),
          ("nonSubseq", 4))
    )



class AddressFlag(TextualConvention, Integer32):
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
        *(("invalid", 0),
          ("t64SrcAddrPre64DestAddrPre", 1),
          ("t64SrcAddrPre64DestAddrSuf", 2),
          ("t64SrcAddrSuf64DestAddrPre", 3),
          ("t64SrcAddrSuf64DestAddrSuf", 4),
          ("t128SourceAddress", 5),
          ("t128DestinationAddress", 6))
    )



class DirectionType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("inbound", 1),
          ("outbound", 2))
    )



# MIB Managed Objects in the order of their OIDs

_Hh3cAclMibObjects_ObjectIdentity = ObjectIdentity
hh3cAclMibObjects = _Hh3cAclMibObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 1)
)


class _Hh3cAclMode_Type(Integer32):
    """Custom type hh3cAclMode based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("linkBased", 1),
          ("ipBased", 2))
    )


_Hh3cAclMode_Type.__name__ = "Integer32"
_Hh3cAclMode_Object = MibScalar
hh3cAclMode = _Hh3cAclMode_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 1, 1),
    _Hh3cAclMode_Type()
)
hh3cAclMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cAclMode.setStatus("current")
_Hh3cAclNumGroupTable_Object = MibTable
hh3cAclNumGroupTable = _Hh3cAclNumGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 1, 2)
)
if mibBuilder.loadTexts:
    hh3cAclNumGroupTable.setStatus("current")
_Hh3cAclNumGroupEntry_Object = MibTableRow
hh3cAclNumGroupEntry = _Hh3cAclNumGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 1, 2, 1)
)
hh3cAclNumGroupEntry.setIndexNames(
    (0, "HH3C-ACL-MIB", "hh3cAclNumGroupAclNum"),
)
if mibBuilder.loadTexts:
    hh3cAclNumGroupEntry.setStatus("current")


class _Hh3cAclNumGroupAclNum_Type(Integer32):
    """Custom type hh3cAclNumGroupAclNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1000, 5999),
    )


_Hh3cAclNumGroupAclNum_Type.__name__ = "Integer32"
_Hh3cAclNumGroupAclNum_Object = MibTableColumn
hh3cAclNumGroupAclNum = _Hh3cAclNumGroupAclNum_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 1, 2, 1, 1),
    _Hh3cAclNumGroupAclNum_Type()
)
hh3cAclNumGroupAclNum.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cAclNumGroupAclNum.setStatus("current")


class _Hh3cAclNumGroupMatchOrder_Type(Integer32):
    """Custom type hh3cAclNumGroupMatchOrder based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("config", 1),
          ("auto", 2))
    )


_Hh3cAclNumGroupMatchOrder_Type.__name__ = "Integer32"
_Hh3cAclNumGroupMatchOrder_Object = MibTableColumn
hh3cAclNumGroupMatchOrder = _Hh3cAclNumGroupMatchOrder_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 1, 2, 1, 2),
    _Hh3cAclNumGroupMatchOrder_Type()
)
hh3cAclNumGroupMatchOrder.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cAclNumGroupMatchOrder.setStatus("current")
_Hh3cAclNumGroupSubitemNum_Type = Integer32
_Hh3cAclNumGroupSubitemNum_Object = MibTableColumn
hh3cAclNumGroupSubitemNum = _Hh3cAclNumGroupSubitemNum_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 1, 2, 1, 3),
    _Hh3cAclNumGroupSubitemNum_Type()
)
hh3cAclNumGroupSubitemNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cAclNumGroupSubitemNum.setStatus("current")


class _Hh3cAclNumGroupDescription_Type(OctetString):
    """Custom type hh3cAclNumGroupDescription based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_Hh3cAclNumGroupDescription_Type.__name__ = "OctetString"
_Hh3cAclNumGroupDescription_Object = MibTableColumn
hh3cAclNumGroupDescription = _Hh3cAclNumGroupDescription_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 1, 2, 1, 4),
    _Hh3cAclNumGroupDescription_Type()
)
hh3cAclNumGroupDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cAclNumGroupDescription.setStatus("current")


class _Hh3cAclNumGroupCountClear_Type(Integer32):
    """Custom type hh3cAclNumGroupCountClear based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("cleared", 1),
          ("nouse", 2))
    )


_Hh3cAclNumGroupCountClear_Type.__name__ = "Integer32"
_Hh3cAclNumGroupCountClear_Object = MibTableColumn
hh3cAclNumGroupCountClear = _Hh3cAclNumGroupCountClear_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 1, 2, 1, 5),
    _Hh3cAclNumGroupCountClear_Type()
)
hh3cAclNumGroupCountClear.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cAclNumGroupCountClear.setStatus("current")
_Hh3cAclNumGroupRowStatus_Type = RowStatus
_Hh3cAclNumGroupRowStatus_Object = MibTableColumn
hh3cAclNumGroupRowStatus = _Hh3cAclNumGroupRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 1, 2, 1, 6),
    _Hh3cAclNumGroupRowStatus_Type()
)
hh3cAclNumGroupRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cAclNumGroupRowStatus.setStatus("current")
_Hh3cAclNameGroupTable_Object = MibTable
hh3cAclNameGroupTable = _Hh3cAclNameGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 1, 3)
)
if mibBuilder.loadTexts:
    hh3cAclNameGroupTable.setStatus("current")
_Hh3cAclNameGroupEntry_Object = MibTableRow
hh3cAclNameGroupEntry = _Hh3cAclNameGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 1, 3, 1)
)
hh3cAclNameGroupEntry.setIndexNames(
    (0, "HH3C-ACL-MIB", "hh3cAclNameGroupIndex"),
)
if mibBuilder.loadTexts:
    hh3cAclNameGroupEntry.setStatus("current")


class _Hh3cAclNameGroupIndex_Type(Integer32):
    """Custom type hh3cAclNameGroupIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10000, 12999),
    )


_Hh3cAclNameGroupIndex_Type.__name__ = "Integer32"
_Hh3cAclNameGroupIndex_Object = MibTableColumn
hh3cAclNameGroupIndex = _Hh3cAclNameGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 1, 3, 1, 1),
    _Hh3cAclNameGroupIndex_Type()
)
hh3cAclNameGroupIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cAclNameGroupIndex.setStatus("current")


class _Hh3cAclNameGroupCreateName_Type(OctetString):
    """Custom type hh3cAclNameGroupCreateName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Hh3cAclNameGroupCreateName_Type.__name__ = "OctetString"
_Hh3cAclNameGroupCreateName_Object = MibTableColumn
hh3cAclNameGroupCreateName = _Hh3cAclNameGroupCreateName_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 1, 3, 1, 2),
    _Hh3cAclNameGroupCreateName_Type()
)
hh3cAclNameGroupCreateName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cAclNameGroupCreateName.setStatus("current")


class _Hh3cAclNameGroupTypes_Type(Integer32):
    """Custom type hh3cAclNameGroupTypes based on Integer32"""
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
        *(("basic", 1),
          ("advanced", 2),
          ("ifBased", 3),
          ("link", 4),
          ("user", 5))
    )


_Hh3cAclNameGroupTypes_Type.__name__ = "Integer32"
_Hh3cAclNameGroupTypes_Object = MibTableColumn
hh3cAclNameGroupTypes = _Hh3cAclNameGroupTypes_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 1, 3, 1, 3),
    _Hh3cAclNameGroupTypes_Type()
)
hh3cAclNameGroupTypes.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cAclNameGroupTypes.setStatus("current")


class _Hh3cAclNameGroupMatchOrder_Type(Integer32):
    """Custom type hh3cAclNameGroupMatchOrder based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("config", 1),
          ("auto", 2))
    )


_Hh3cAclNameGroupMatchOrder_Type.__name__ = "Integer32"
_Hh3cAclNameGroupMatchOrder_Object = MibTableColumn
hh3cAclNameGroupMatchOrder = _Hh3cAclNameGroupMatchOrder_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 1, 3, 1, 4),
    _Hh3cAclNameGroupMatchOrder_Type()
)
hh3cAclNameGroupMatchOrder.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cAclNameGroupMatchOrder.setStatus("current")


class _Hh3cAclNameGroupSubitemNum_Type(Integer32):
    """Custom type hh3cAclNameGroupSubitemNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Hh3cAclNameGroupSubitemNum_Type.__name__ = "Integer32"
_Hh3cAclNameGroupSubitemNum_Object = MibTableColumn
hh3cAclNameGroupSubitemNum = _Hh3cAclNameGroupSubitemNum_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 1, 3, 1, 5),
    _Hh3cAclNameGroupSubitemNum_Type()
)
hh3cAclNameGroupSubitemNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cAclNameGroupSubitemNum.setStatus("current")
_Hh3cAclNameGroupRowStatus_Type = RowStatus
_Hh3cAclNameGroupRowStatus_Object = MibTableColumn
hh3cAclNameGroupRowStatus = _Hh3cAclNameGroupRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 1, 3, 1, 6),
    _Hh3cAclNameGroupRowStatus_Type()
)
hh3cAclNameGroupRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cAclNameGroupRowStatus.setStatus("current")
_Hh3cAclBasicRuleTable_Object = MibTable
hh3cAclBasicRuleTable = _Hh3cAclBasicRuleTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 1, 4)
)
if mibBuilder.loadTexts:
    hh3cAclBasicRuleTable.setStatus("current")
_Hh3cAclBasicRuleEntry_Object = MibTableRow
hh3cAclBasicRuleEntry = _Hh3cAclBasicRuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 1, 4, 1)
)
hh3cAclBasicRuleEntry.setIndexNames(
    (0, "HH3C-ACL-MIB", "hh3cAclBasicAclNum"),
    (0, "HH3C-ACL-MIB", "hh3cAclBasicSubitem"),
)
if mibBuilder.loadTexts:
    hh3cAclBasicRuleEntry.setStatus("current")


class _Hh3cAclBasicAclNum_Type(Integer32):
    """Custom type hh3cAclBasicAclNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(2000, 2999),
        ValueRangeConstraint(10000, 12999),
    )


_Hh3cAclBasicAclNum_Type.__name__ = "Integer32"
_Hh3cAclBasicAclNum_Object = MibTableColumn
hh3cAclBasicAclNum = _Hh3cAclBasicAclNum_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 1, 4, 1, 1),
    _Hh3cAclBasicAclNum_Type()
)
hh3cAclBasicAclNum.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cAclBasicAclNum.setStatus("current")


class _Hh3cAclBasicSubitem_Type(Integer32):
    """Custom type hh3cAclBasicSubitem based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Hh3cAclBasicSubitem_Type.__name__ = "Integer32"
_Hh3cAclBasicSubitem_Object = MibTableColumn
hh3cAclBasicSubitem = _Hh3cAclBasicSubitem_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 1, 4, 1, 2),
    _Hh3cAclBasicSubitem_Type()
)
hh3cAclBasicSubitem.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cAclBasicSubitem.setStatus("current")


class _Hh3cAclBasicAct_Type(Integer32):
    """Custom type hh3cAclBasicAct based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("permit", 1),
          ("deny", 2))
    )


_Hh3cAclBasicAct_Type.__name__ = "Integer32"
_Hh3cAclBasicAct_Object = MibTableColumn
hh3cAclBasicAct = _Hh3cAclBasicAct_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 1, 4, 1, 3),
    _Hh3cAclBasicAct_Type()
)
hh3cAclBasicAct.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cAclBasicAct.setStatus("current")
_Hh3cAclBasicSrcIp_Type = IpAddress
_Hh3cAclBasicSrcIp_Object = MibTableColumn
hh3cAclBasicSrcIp = _Hh3cAclBasicSrcIp_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 1, 4, 1, 4),
    _Hh3cAclBasicSrcIp_Type()
)
hh3cAclBasicSrcIp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cAclBasicSrcIp.setStatus("current")
_Hh3cAclBasicSrcWild_Type = IpAddress
_Hh3cAclBasicSrcWild_Object = MibTableColumn
hh3cAclBasicSrcWild = _Hh3cAclBasicSrcWild_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 1, 4, 1, 5),
    _Hh3cAclBasicSrcWild_Type()
)
hh3cAclBasicSrcWild.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cAclBasicSrcWild.setStatus("current")


class _Hh3cAclBasicTimeRangeName_Type(OctetString):
    """Custom type hh3cAclBasicTimeRangeName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Hh3cAclBasicTimeRangeName_Type.__name__ = "OctetString"
_Hh3cAclBasicTimeRangeName_Object = MibTableColumn
hh3cAclBasicTimeRangeName = _Hh3cAclBasicTimeRangeName_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 1, 4, 1, 6),
    _Hh3cAclBasicTimeRangeName_Type()
)
hh3cAclBasicTimeRangeName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cAclBasicTimeRangeName.setStatus("current")
_Hh3cAclBasicFragments_Type = TruthValue
_Hh3cAclBasicFragments_Object = MibTableColumn
hh3cAclBasicFragments = _Hh3cAclBasicFragments_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 1, 4, 1, 7),
    _Hh3cAclBasicFragments_Type()
)
hh3cAclBasicFragments.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cAclBasicFragments.setStatus("current")
_Hh3cAclBasicLog_Type = TruthValue
_Hh3cAclBasicLog_Object = MibTableColumn
hh3cAclBasicLog = _Hh3cAclBasicLog_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 1, 4, 1, 8),
    _Hh3cAclBasicLog_Type()
)
hh3cAclBasicLog.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cAclBasicLog.setStatus("current")
_Hh3cAclBasicEnable_Type = TruthValue
_Hh3cAclBasicEnable_Object = MibTableColumn
hh3cAclBasicEnable = _Hh3cAclBasicEnable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 1, 4, 1, 9),
    _Hh3cAclBasicEnable_Type()
)
hh3cAclBasicEnable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cAclBasicEnable.setStatus("current")
_Hh3cAclBasicCount_Type = Counter32
_Hh3cAclBasicCount_Object = MibTableColumn
hh3cAclBasicCount = _Hh3cAclBasicCount_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 1, 4, 1, 10),
    _Hh3cAclBasicCount_Type()
)
hh3cAclBasicCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cAclBasicCount.setStatus("current")


class _Hh3cAclBasicCountClear_Type(Integer32):
    """Custom type hh3cAclBasicCountClear based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("cleared", 1),
          ("nouse", 2))
    )


_Hh3cAclBasicCountClear_Type.__name__ = "Integer32"
_Hh3cAclBasicCountClear_Object = MibTableColumn
hh3cAclBasicCountClear = _Hh3cAclBasicCountClear_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 1, 4, 1, 11),
    _Hh3cAclBasicCountClear_Type()
)
hh3cAclBasicCountClear.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cAclBasicCountClear.setStatus("current")
_Hh3cAclBasicRowStatus_Type = RowStatus
_Hh3cAclBasicRowStatus_Object = MibTableColumn
hh3cAclBasicRowStatus = _Hh3cAclBasicRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 1, 4, 1, 12),
    _Hh3cAclBasicRowStatus_Type()
)
hh3cAclBasicRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cAclBasicRowStatus.setStatus("current")
_Hh3cAclAdvancedRuleTable_Object = MibTable
hh3cAclAdvancedRuleTable = _Hh3cAclAdvancedRuleTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 1, 5)
)
if mibBuilder.loadTexts:
    hh3cAclAdvancedRuleTable.setStatus("current")
_Hh3cAclAdvancedRuleEntry_Object = MibTableRow
hh3cAclAdvancedRuleEntry = _Hh3cAclAdvancedRuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 1, 5, 1)
)
hh3cAclAdvancedRuleEntry.setIndexNames(
    (0, "HH3C-ACL-MIB", "hh3cAclAdvancedAclNum"),
    (0, "HH3C-ACL-MIB", "hh3cAclAdvancedSubitem"),
)
if mibBuilder.loadTexts:
    hh3cAclAdvancedRuleEntry.setStatus("current")


class _Hh3cAclAdvancedAclNum_Type(Integer32):
    """Custom type hh3cAclAdvancedAclNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(3000, 3999),
        ValueRangeConstraint(10000, 12999),
    )


_Hh3cAclAdvancedAclNum_Type.__name__ = "Integer32"
_Hh3cAclAdvancedAclNum_Object = MibTableColumn
hh3cAclAdvancedAclNum = _Hh3cAclAdvancedAclNum_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 1, 5, 1, 1),
    _Hh3cAclAdvancedAclNum_Type()
)
hh3cAclAdvancedAclNum.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cAclAdvancedAclNum.setStatus("current")


class _Hh3cAclAdvancedSubitem_Type(Integer32):
    """Custom type hh3cAclAdvancedSubitem based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Hh3cAclAdvancedSubitem_Type.__name__ = "Integer32"
_Hh3cAclAdvancedSubitem_Object = MibTableColumn
hh3cAclAdvancedSubitem = _Hh3cAclAdvancedSubitem_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 1, 5, 1, 2),
    _Hh3cAclAdvancedSubitem_Type()
)
hh3cAclAdvancedSubitem.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cAclAdvancedSubitem.setStatus("current")


class _Hh3cAclAdvancedAct_Type(Integer32):
    """Custom type hh3cAclAdvancedAct based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("permit", 1),
          ("deny", 2))
    )


_Hh3cAclAdvancedAct_Type.__name__ = "Integer32"
_Hh3cAclAdvancedAct_Object = MibTableColumn
hh3cAclAdvancedAct = _Hh3cAclAdvancedAct_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 1, 5, 1, 3),
    _Hh3cAclAdvancedAct_Type()
)
hh3cAclAdvancedAct.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cAclAdvancedAct.setStatus("current")


class _Hh3cAclAdvancedProtocol_Type(Integer32):
    """Custom type hh3cAclAdvancedProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_Hh3cAclAdvancedProtocol_Type.__name__ = "Integer32"
_Hh3cAclAdvancedProtocol_Object = MibTableColumn
hh3cAclAdvancedProtocol = _Hh3cAclAdvancedProtocol_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 1, 5, 1, 4),
    _Hh3cAclAdvancedProtocol_Type()
)
hh3cAclAdvancedProtocol.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cAclAdvancedProtocol.setStatus("current")
_Hh3cAclAdvancedSrcIp_Type = IpAddress
_Hh3cAclAdvancedSrcIp_Object = MibTableColumn
hh3cAclAdvancedSrcIp = _Hh3cAclAdvancedSrcIp_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 1, 5, 1, 5),
    _Hh3cAclAdvancedSrcIp_Type()
)
hh3cAclAdvancedSrcIp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cAclAdvancedSrcIp.setStatus("current")
_Hh3cAclAdvancedSrcWild_Type = IpAddress
_Hh3cAclAdvancedSrcWild_Object = MibTableColumn
hh3cAclAdvancedSrcWild = _Hh3cAclAdvancedSrcWild_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 1, 5, 1, 6),
    _Hh3cAclAdvancedSrcWild_Type()
)
hh3cAclAdvancedSrcWild.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cAclAdvancedSrcWild.setStatus("current")


class _Hh3cAclAdvancedSrcOp_Type(Integer32):
    """Custom type hh3cAclAdvancedSrcOp based on Integer32"""
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
        *(("invalid", 0),
          ("lt", 1),
          ("eq", 2),
          ("gt", 3),
          ("neq", 4),
          ("range", 5))
    )


_Hh3cAclAdvancedSrcOp_Type.__name__ = "Integer32"
_Hh3cAclAdvancedSrcOp_Object = MibTableColumn
hh3cAclAdvancedSrcOp = _Hh3cAclAdvancedSrcOp_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 1, 5, 1, 7),
    _Hh3cAclAdvancedSrcOp_Type()
)
hh3cAclAdvancedSrcOp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cAclAdvancedSrcOp.setStatus("current")


class _Hh3cAclAdvancedSrcPort1_Type(Integer32):
    """Custom type hh3cAclAdvancedSrcPort1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Hh3cAclAdvancedSrcPort1_Type.__name__ = "Integer32"
_Hh3cAclAdvancedSrcPort1_Object = MibTableColumn
hh3cAclAdvancedSrcPort1 = _Hh3cAclAdvancedSrcPort1_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 1, 5, 1, 8),
    _Hh3cAclAdvancedSrcPort1_Type()
)
hh3cAclAdvancedSrcPort1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cAclAdvancedSrcPort1.setStatus("current")


class _Hh3cAclAdvancedSrcPort2_Type(Integer32):
    """Custom type hh3cAclAdvancedSrcPort2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Hh3cAclAdvancedSrcPort2_Type.__name__ = "Integer32"
_Hh3cAclAdvancedSrcPort2_Object = MibTableColumn
hh3cAclAdvancedSrcPort2 = _Hh3cAclAdvancedSrcPort2_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 1, 5, 1, 9),
    _Hh3cAclAdvancedSrcPort2_Type()
)
hh3cAclAdvancedSrcPort2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cAclAdvancedSrcPort2.setStatus("current")
_Hh3cAclAdvancedDestIp_Type = IpAddress
_Hh3cAclAdvancedDestIp_Object = MibTableColumn
hh3cAclAdvancedDestIp = _Hh3cAclAdvancedDestIp_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 1, 5, 1, 10),
    _Hh3cAclAdvancedDestIp_Type()
)
hh3cAclAdvancedDestIp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cAclAdvancedDestIp.setStatus("current")
_Hh3cAclAdvancedDestWild_Type = IpAddress
_Hh3cAclAdvancedDestWild_Object = MibTableColumn
hh3cAclAdvancedDestWild = _Hh3cAclAdvancedDestWild_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 1, 5, 1, 11),
    _Hh3cAclAdvancedDestWild_Type()
)
hh3cAclAdvancedDestWild.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cAclAdvancedDestWild.setStatus("current")


class _Hh3cAclAdvancedDestOp_Type(Integer32):
    """Custom type hh3cAclAdvancedDestOp based on Integer32"""
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
        *(("invalid", 0),
          ("lt", 1),
          ("eq", 2),
          ("gt", 3),
          ("neq", 4),
          ("range", 5))
    )


_Hh3cAclAdvancedDestOp_Type.__name__ = "Integer32"
_Hh3cAclAdvancedDestOp_Object = MibTableColumn
hh3cAclAdvancedDestOp = _Hh3cAclAdvancedDestOp_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 1, 5, 1, 12),
    _Hh3cAclAdvancedDestOp_Type()
)
hh3cAclAdvancedDestOp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cAclAdvancedDestOp.setStatus("current")


class _Hh3cAclAdvancedDestPort1_Type(Integer32):
    """Custom type hh3cAclAdvancedDestPort1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Hh3cAclAdvancedDestPort1_Type.__name__ = "Integer32"
_Hh3cAclAdvancedDestPort1_Object = MibTableColumn
hh3cAclAdvancedDestPort1 = _Hh3cAclAdvancedDestPort1_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 1, 5, 1, 13),
    _Hh3cAclAdvancedDestPort1_Type()
)
hh3cAclAdvancedDestPort1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cAclAdvancedDestPort1.setStatus("current")


class _Hh3cAclAdvancedDestPort2_Type(Integer32):
    """Custom type hh3cAclAdvancedDestPort2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Hh3cAclAdvancedDestPort2_Type.__name__ = "Integer32"
_Hh3cAclAdvancedDestPort2_Object = MibTableColumn
hh3cAclAdvancedDestPort2 = _Hh3cAclAdvancedDestPort2_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 1, 5, 1, 14),
    _Hh3cAclAdvancedDestPort2_Type()
)
hh3cAclAdvancedDestPort2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cAclAdvancedDestPort2.setStatus("current")


class _Hh3cAclAdvancedPrecedence_Type(Integer32):
    """Custom type hh3cAclAdvancedPrecedence based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
        ValueRangeConstraint(255, 255),
    )


_Hh3cAclAdvancedPrecedence_Type.__name__ = "Integer32"
_Hh3cAclAdvancedPrecedence_Object = MibTableColumn
hh3cAclAdvancedPrecedence = _Hh3cAclAdvancedPrecedence_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 1, 5, 1, 15),
    _Hh3cAclAdvancedPrecedence_Type()
)
hh3cAclAdvancedPrecedence.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cAclAdvancedPrecedence.setStatus("current")


class _Hh3cAclAdvancedTos_Type(Integer32):
    """Custom type hh3cAclAdvancedTos based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
        ValueRangeConstraint(255, 255),
    )


_Hh3cAclAdvancedTos_Type.__name__ = "Integer32"
_Hh3cAclAdvancedTos_Object = MibTableColumn
hh3cAclAdvancedTos = _Hh3cAclAdvancedTos_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 1, 5, 1, 16),
    _Hh3cAclAdvancedTos_Type()
)
hh3cAclAdvancedTos.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cAclAdvancedTos.setStatus("current")


class _Hh3cAclAdvancedDscp_Type(Integer32):
    """Custom type hh3cAclAdvancedDscp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
        ValueRangeConstraint(255, 255),
    )


_Hh3cAclAdvancedDscp_Type.__name__ = "Integer32"
_Hh3cAclAdvancedDscp_Object = MibTableColumn
hh3cAclAdvancedDscp = _Hh3cAclAdvancedDscp_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 1, 5, 1, 17),
    _Hh3cAclAdvancedDscp_Type()
)
hh3cAclAdvancedDscp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cAclAdvancedDscp.setStatus("current")


class _Hh3cAclAdvancedEstablish_Type(TruthValue):
    """Custom type hh3cAclAdvancedEstablish based on TruthValue"""
    defaultValue = 2


_Hh3cAclAdvancedEstablish_Type.__name__ = "TruthValue"
_Hh3cAclAdvancedEstablish_Object = MibTableColumn
hh3cAclAdvancedEstablish = _Hh3cAclAdvancedEstablish_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 1, 5, 1, 18),
    _Hh3cAclAdvancedEstablish_Type()
)
hh3cAclAdvancedEstablish.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cAclAdvancedEstablish.setStatus("current")


class _Hh3cAclAdvancedTimeRangeName_Type(OctetString):
    """Custom type hh3cAclAdvancedTimeRangeName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Hh3cAclAdvancedTimeRangeName_Type.__name__ = "OctetString"
_Hh3cAclAdvancedTimeRangeName_Object = MibTableColumn
hh3cAclAdvancedTimeRangeName = _Hh3cAclAdvancedTimeRangeName_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 1, 5, 1, 19),
    _Hh3cAclAdvancedTimeRangeName_Type()
)
hh3cAclAdvancedTimeRangeName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cAclAdvancedTimeRangeName.setStatus("current")


class _Hh3cAclAdvancedIcmpType_Type(Integer32):
    """Custom type hh3cAclAdvancedIcmpType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
        ValueRangeConstraint(65535, 65535),
    )


_Hh3cAclAdvancedIcmpType_Type.__name__ = "Integer32"
_Hh3cAclAdvancedIcmpType_Object = MibTableColumn
hh3cAclAdvancedIcmpType = _Hh3cAclAdvancedIcmpType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 1, 5, 1, 20),
    _Hh3cAclAdvancedIcmpType_Type()
)
hh3cAclAdvancedIcmpType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cAclAdvancedIcmpType.setStatus("current")


class _Hh3cAclAdvancedIcmpCode_Type(Integer32):
    """Custom type hh3cAclAdvancedIcmpCode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
        ValueRangeConstraint(65535, 65535),
    )


_Hh3cAclAdvancedIcmpCode_Type.__name__ = "Integer32"
_Hh3cAclAdvancedIcmpCode_Object = MibTableColumn
hh3cAclAdvancedIcmpCode = _Hh3cAclAdvancedIcmpCode_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 1, 5, 1, 21),
    _Hh3cAclAdvancedIcmpCode_Type()
)
hh3cAclAdvancedIcmpCode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cAclAdvancedIcmpCode.setStatus("current")
_Hh3cAclAdvancedFragments_Type = TruthValue
_Hh3cAclAdvancedFragments_Object = MibTableColumn
hh3cAclAdvancedFragments = _Hh3cAclAdvancedFragments_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 1, 5, 1, 22),
    _Hh3cAclAdvancedFragments_Type()
)
hh3cAclAdvancedFragments.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cAclAdvancedFragments.setStatus("current")
_Hh3cAclAdvancedLog_Type = TruthValue
_Hh3cAclAdvancedLog_Object = MibTableColumn
hh3cAclAdvancedLog = _Hh3cAclAdvancedLog_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 1, 5, 1, 23),
    _Hh3cAclAdvancedLog_Type()
)
hh3cAclAdvancedLog.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cAclAdvancedLog.setStatus("current")
_Hh3cAclAdvancedEnable_Type = TruthValue
_Hh3cAclAdvancedEnable_Object = MibTableColumn
hh3cAclAdvancedEnable = _Hh3cAclAdvancedEnable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 1, 5, 1, 24),
    _Hh3cAclAdvancedEnable_Type()
)
hh3cAclAdvancedEnable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cAclAdvancedEnable.setStatus("current")
_Hh3cAclAdvancedCount_Type = Counter32
_Hh3cAclAdvancedCount_Object = MibTableColumn
hh3cAclAdvancedCount = _Hh3cAclAdvancedCount_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 1, 5, 1, 25),
    _Hh3cAclAdvancedCount_Type()
)
hh3cAclAdvancedCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cAclAdvancedCount.setStatus("current")


class _Hh3cAclAdvancedCountClear_Type(Integer32):
    """Custom type hh3cAclAdvancedCountClear based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("cleared", 1),
          ("nouse", 2))
    )


_Hh3cAclAdvancedCountClear_Type.__name__ = "Integer32"
_Hh3cAclAdvancedCountClear_Object = MibTableColumn
hh3cAclAdvancedCountClear = _Hh3cAclAdvancedCountClear_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 1, 5, 1, 26),
    _Hh3cAclAdvancedCountClear_Type()
)
hh3cAclAdvancedCountClear.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cAclAdvancedCountClear.setStatus("current")
_Hh3cAclAdvancedRowStatus_Type = RowStatus
_Hh3cAclAdvancedRowStatus_Object = MibTableColumn
hh3cAclAdvancedRowStatus = _Hh3cAclAdvancedRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 1, 5, 1, 27),
    _Hh3cAclAdvancedRowStatus_Type()
)
hh3cAclAdvancedRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cAclAdvancedRowStatus.setStatus("current")
_Hh3cAclIfRuleTable_Object = MibTable
hh3cAclIfRuleTable = _Hh3cAclIfRuleTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 1, 6)
)
if mibBuilder.loadTexts:
    hh3cAclIfRuleTable.setStatus("current")
_Hh3cAclIfRuleEntry_Object = MibTableRow
hh3cAclIfRuleEntry = _Hh3cAclIfRuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 1, 6, 1)
)
hh3cAclIfRuleEntry.setIndexNames(
    (0, "HH3C-ACL-MIB", "hh3cAclIfAclNum"),
    (0, "HH3C-ACL-MIB", "hh3cAclIfSubitem"),
)
if mibBuilder.loadTexts:
    hh3cAclIfRuleEntry.setStatus("current")


class _Hh3cAclIfAclNum_Type(Integer32):
    """Custom type hh3cAclIfAclNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1000, 1999),
        ValueRangeConstraint(10000, 12999),
    )


_Hh3cAclIfAclNum_Type.__name__ = "Integer32"
_Hh3cAclIfAclNum_Object = MibTableColumn
hh3cAclIfAclNum = _Hh3cAclIfAclNum_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 1, 6, 1, 1),
    _Hh3cAclIfAclNum_Type()
)
hh3cAclIfAclNum.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cAclIfAclNum.setStatus("current")


class _Hh3cAclIfSubitem_Type(Integer32):
    """Custom type hh3cAclIfSubitem based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Hh3cAclIfSubitem_Type.__name__ = "Integer32"
_Hh3cAclIfSubitem_Object = MibTableColumn
hh3cAclIfSubitem = _Hh3cAclIfSubitem_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 1, 6, 1, 2),
    _Hh3cAclIfSubitem_Type()
)
hh3cAclIfSubitem.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cAclIfSubitem.setStatus("current")


class _Hh3cAclIfAct_Type(Integer32):
    """Custom type hh3cAclIfAct based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("permit", 1),
          ("deny", 2))
    )


_Hh3cAclIfAct_Type.__name__ = "Integer32"
_Hh3cAclIfAct_Object = MibTableColumn
hh3cAclIfAct = _Hh3cAclIfAct_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 1, 6, 1, 3),
    _Hh3cAclIfAct_Type()
)
hh3cAclIfAct.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cAclIfAct.setStatus("current")


class _Hh3cAclIfIndex_Type(Integer32):
    """Custom type hh3cAclIfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_Hh3cAclIfIndex_Type.__name__ = "Integer32"
_Hh3cAclIfIndex_Object = MibTableColumn
hh3cAclIfIndex = _Hh3cAclIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 1, 6, 1, 4),
    _Hh3cAclIfIndex_Type()
)
hh3cAclIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cAclIfIndex.setStatus("current")
_Hh3cAclIfAny_Type = TruthValue
_Hh3cAclIfAny_Object = MibTableColumn
hh3cAclIfAny = _Hh3cAclIfAny_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 1, 6, 1, 5),
    _Hh3cAclIfAny_Type()
)
hh3cAclIfAny.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cAclIfAny.setStatus("current")


class _Hh3cAclIfTimeRangeName_Type(OctetString):
    """Custom type hh3cAclIfTimeRangeName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Hh3cAclIfTimeRangeName_Type.__name__ = "OctetString"
_Hh3cAclIfTimeRangeName_Object = MibTableColumn
hh3cAclIfTimeRangeName = _Hh3cAclIfTimeRangeName_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 1, 6, 1, 6),
    _Hh3cAclIfTimeRangeName_Type()
)
hh3cAclIfTimeRangeName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cAclIfTimeRangeName.setStatus("current")
_Hh3cAclIfLog_Type = TruthValue
_Hh3cAclIfLog_Object = MibTableColumn
hh3cAclIfLog = _Hh3cAclIfLog_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 1, 6, 1, 7),
    _Hh3cAclIfLog_Type()
)
hh3cAclIfLog.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cAclIfLog.setStatus("current")
_Hh3cAclIfEnable_Type = TruthValue
_Hh3cAclIfEnable_Object = MibTableColumn
hh3cAclIfEnable = _Hh3cAclIfEnable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 1, 6, 1, 8),
    _Hh3cAclIfEnable_Type()
)
hh3cAclIfEnable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cAclIfEnable.setStatus("current")
_Hh3cAclIfCount_Type = Counter32
_Hh3cAclIfCount_Object = MibTableColumn
hh3cAclIfCount = _Hh3cAclIfCount_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 1, 6, 1, 9),
    _Hh3cAclIfCount_Type()
)
hh3cAclIfCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cAclIfCount.setStatus("current")


class _Hh3cAclIfCountClear_Type(Integer32):
    """Custom type hh3cAclIfCountClear based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("cleared", 1),
          ("nouse", 2))
    )


_Hh3cAclIfCountClear_Type.__name__ = "Integer32"
_Hh3cAclIfCountClear_Object = MibTableColumn
hh3cAclIfCountClear = _Hh3cAclIfCountClear_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 1, 6, 1, 10),
    _Hh3cAclIfCountClear_Type()
)
hh3cAclIfCountClear.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cAclIfCountClear.setStatus("current")
_Hh3cAclIfRowStatus_Type = RowStatus
_Hh3cAclIfRowStatus_Object = MibTableColumn
hh3cAclIfRowStatus = _Hh3cAclIfRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 1, 6, 1, 11),
    _Hh3cAclIfRowStatus_Type()
)
hh3cAclIfRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cAclIfRowStatus.setStatus("current")
_Hh3cAclLinkTable_Object = MibTable
hh3cAclLinkTable = _Hh3cAclLinkTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 1, 7)
)
if mibBuilder.loadTexts:
    hh3cAclLinkTable.setStatus("current")
_Hh3cAclLinkEntry_Object = MibTableRow
hh3cAclLinkEntry = _Hh3cAclLinkEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 1, 7, 1)
)
hh3cAclLinkEntry.setIndexNames(
    (0, "HH3C-ACL-MIB", "hh3cAclLinkAclNum"),
    (0, "HH3C-ACL-MIB", "hh3cAclLinkSubitem"),
)
if mibBuilder.loadTexts:
    hh3cAclLinkEntry.setStatus("current")


class _Hh3cAclLinkAclNum_Type(Integer32):
    """Custom type hh3cAclLinkAclNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(4000, 4999),
        ValueRangeConstraint(10000, 12999),
    )


_Hh3cAclLinkAclNum_Type.__name__ = "Integer32"
_Hh3cAclLinkAclNum_Object = MibTableColumn
hh3cAclLinkAclNum = _Hh3cAclLinkAclNum_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 1, 7, 1, 1),
    _Hh3cAclLinkAclNum_Type()
)
hh3cAclLinkAclNum.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cAclLinkAclNum.setStatus("current")


class _Hh3cAclLinkSubitem_Type(Integer32):
    """Custom type hh3cAclLinkSubitem based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Hh3cAclLinkSubitem_Type.__name__ = "Integer32"
_Hh3cAclLinkSubitem_Object = MibTableColumn
hh3cAclLinkSubitem = _Hh3cAclLinkSubitem_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 1, 7, 1, 2),
    _Hh3cAclLinkSubitem_Type()
)
hh3cAclLinkSubitem.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cAclLinkSubitem.setStatus("current")


class _Hh3cAclLinkAct_Type(Integer32):
    """Custom type hh3cAclLinkAct based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("permit", 1),
          ("deny", 2))
    )


_Hh3cAclLinkAct_Type.__name__ = "Integer32"
_Hh3cAclLinkAct_Object = MibTableColumn
hh3cAclLinkAct = _Hh3cAclLinkAct_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 1, 7, 1, 3),
    _Hh3cAclLinkAct_Type()
)
hh3cAclLinkAct.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cAclLinkAct.setStatus("current")


class _Hh3cAclLinkProtocol_Type(Integer32):
    """Custom type hh3cAclLinkProtocol based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              2048,
              2054,
              32821,
              34887,
              34915,
              34916)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 0),
          ("ip", 2048),
          ("arp", 2054),
          ("rarp", 32821),
          ("mpls", 34887),
          ("pppoeControl", 34915),
          ("pppoeData", 34916))
    )


_Hh3cAclLinkProtocol_Type.__name__ = "Integer32"
_Hh3cAclLinkProtocol_Object = MibTableColumn
hh3cAclLinkProtocol = _Hh3cAclLinkProtocol_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 1, 7, 1, 4),
    _Hh3cAclLinkProtocol_Type()
)
hh3cAclLinkProtocol.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cAclLinkProtocol.setStatus("current")


class _Hh3cAclLinkFormatType_Type(Integer32):
    """Custom type hh3cAclLinkFormatType based on Integer32"""
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
        *(("invalid", 0),
          ("ethernetII", 1),
          ("snap", 2),
          ("ieee802Dot3And2", 3),
          ("ieee802Dot3", 4))
    )


_Hh3cAclLinkFormatType_Type.__name__ = "Integer32"
_Hh3cAclLinkFormatType_Object = MibTableColumn
hh3cAclLinkFormatType = _Hh3cAclLinkFormatType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 1, 7, 1, 5),
    _Hh3cAclLinkFormatType_Type()
)
hh3cAclLinkFormatType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cAclLinkFormatType.setStatus("current")


class _Hh3cAclLinkVlanTag_Type(Integer32):
    """Custom type hh3cAclLinkVlanTag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 0),
          ("tagged", 1),
          ("untagged", 2))
    )


_Hh3cAclLinkVlanTag_Type.__name__ = "Integer32"
_Hh3cAclLinkVlanTag_Object = MibTableColumn
hh3cAclLinkVlanTag = _Hh3cAclLinkVlanTag_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 1, 7, 1, 6),
    _Hh3cAclLinkVlanTag_Type()
)
hh3cAclLinkVlanTag.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cAclLinkVlanTag.setStatus("current")


class _Hh3cAclLinkVlanPri_Type(Integer32):
    """Custom type hh3cAclLinkVlanPri based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
        ValueRangeConstraint(255, 255),
    )


_Hh3cAclLinkVlanPri_Type.__name__ = "Integer32"
_Hh3cAclLinkVlanPri_Object = MibTableColumn
hh3cAclLinkVlanPri = _Hh3cAclLinkVlanPri_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 1, 7, 1, 7),
    _Hh3cAclLinkVlanPri_Type()
)
hh3cAclLinkVlanPri.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cAclLinkVlanPri.setStatus("current")


class _Hh3cAclLinkSrcVlanId_Type(Integer32):
    """Custom type hh3cAclLinkSrcVlanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_Hh3cAclLinkSrcVlanId_Type.__name__ = "Integer32"
_Hh3cAclLinkSrcVlanId_Object = MibTableColumn
hh3cAclLinkSrcVlanId = _Hh3cAclLinkSrcVlanId_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 1, 7, 1, 8),
    _Hh3cAclLinkSrcVlanId_Type()
)
hh3cAclLinkSrcVlanId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cAclLinkSrcVlanId.setStatus("current")
_Hh3cAclLinkSrcMac_Type = MacAddress
_Hh3cAclLinkSrcMac_Object = MibTableColumn
hh3cAclLinkSrcMac = _Hh3cAclLinkSrcMac_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 1, 7, 1, 9),
    _Hh3cAclLinkSrcMac_Type()
)
hh3cAclLinkSrcMac.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cAclLinkSrcMac.setStatus("current")
_Hh3cAclLinkSrcMacWild_Type = MacAddress
_Hh3cAclLinkSrcMacWild_Object = MibTableColumn
hh3cAclLinkSrcMacWild = _Hh3cAclLinkSrcMacWild_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 1, 7, 1, 10),
    _Hh3cAclLinkSrcMacWild_Type()
)
hh3cAclLinkSrcMacWild.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cAclLinkSrcMacWild.setStatus("current")


class _Hh3cAclLinkSrcIfIndex_Type(Integer32):
    """Custom type hh3cAclLinkSrcIfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_Hh3cAclLinkSrcIfIndex_Type.__name__ = "Integer32"
_Hh3cAclLinkSrcIfIndex_Object = MibTableColumn
hh3cAclLinkSrcIfIndex = _Hh3cAclLinkSrcIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 1, 7, 1, 11),
    _Hh3cAclLinkSrcIfIndex_Type()
)
hh3cAclLinkSrcIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cAclLinkSrcIfIndex.setStatus("current")
_Hh3cAclLinkSrcAny_Type = TruthValue
_Hh3cAclLinkSrcAny_Object = MibTableColumn
hh3cAclLinkSrcAny = _Hh3cAclLinkSrcAny_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 1, 7, 1, 12),
    _Hh3cAclLinkSrcAny_Type()
)
hh3cAclLinkSrcAny.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cAclLinkSrcAny.setStatus("current")


class _Hh3cAclLinkDestVlanId_Type(Integer32):
    """Custom type hh3cAclLinkDestVlanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_Hh3cAclLinkDestVlanId_Type.__name__ = "Integer32"
_Hh3cAclLinkDestVlanId_Object = MibTableColumn
hh3cAclLinkDestVlanId = _Hh3cAclLinkDestVlanId_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 1, 7, 1, 13),
    _Hh3cAclLinkDestVlanId_Type()
)
hh3cAclLinkDestVlanId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cAclLinkDestVlanId.setStatus("current")
_Hh3cAclLinkDestMac_Type = MacAddress
_Hh3cAclLinkDestMac_Object = MibTableColumn
hh3cAclLinkDestMac = _Hh3cAclLinkDestMac_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 1, 7, 1, 14),
    _Hh3cAclLinkDestMac_Type()
)
hh3cAclLinkDestMac.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cAclLinkDestMac.setStatus("current")
_Hh3cAclLinkDestMacWild_Type = MacAddress
_Hh3cAclLinkDestMacWild_Object = MibTableColumn
hh3cAclLinkDestMacWild = _Hh3cAclLinkDestMacWild_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 1, 7, 1, 15),
    _Hh3cAclLinkDestMacWild_Type()
)
hh3cAclLinkDestMacWild.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cAclLinkDestMacWild.setStatus("current")


class _Hh3cAclLinkDestIfIndex_Type(Integer32):
    """Custom type hh3cAclLinkDestIfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_Hh3cAclLinkDestIfIndex_Type.__name__ = "Integer32"
_Hh3cAclLinkDestIfIndex_Object = MibTableColumn
hh3cAclLinkDestIfIndex = _Hh3cAclLinkDestIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 1, 7, 1, 16),
    _Hh3cAclLinkDestIfIndex_Type()
)
hh3cAclLinkDestIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cAclLinkDestIfIndex.setStatus("current")
_Hh3cAclLinkDestAny_Type = TruthValue
_Hh3cAclLinkDestAny_Object = MibTableColumn
hh3cAclLinkDestAny = _Hh3cAclLinkDestAny_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 1, 7, 1, 17),
    _Hh3cAclLinkDestAny_Type()
)
hh3cAclLinkDestAny.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cAclLinkDestAny.setStatus("current")


class _Hh3cAclLinkTimeRangeName_Type(OctetString):
    """Custom type hh3cAclLinkTimeRangeName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Hh3cAclLinkTimeRangeName_Type.__name__ = "OctetString"
_Hh3cAclLinkTimeRangeName_Object = MibTableColumn
hh3cAclLinkTimeRangeName = _Hh3cAclLinkTimeRangeName_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 1, 7, 1, 18),
    _Hh3cAclLinkTimeRangeName_Type()
)
hh3cAclLinkTimeRangeName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cAclLinkTimeRangeName.setStatus("current")
_Hh3cAclLinkEnable_Type = TruthValue
_Hh3cAclLinkEnable_Object = MibTableColumn
hh3cAclLinkEnable = _Hh3cAclLinkEnable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 1, 7, 1, 19),
    _Hh3cAclLinkEnable_Type()
)
hh3cAclLinkEnable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cAclLinkEnable.setStatus("current")
_Hh3cAclLinkRowStatus_Type = RowStatus
_Hh3cAclLinkRowStatus_Object = MibTableColumn
hh3cAclLinkRowStatus = _Hh3cAclLinkRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 1, 7, 1, 20),
    _Hh3cAclLinkRowStatus_Type()
)
hh3cAclLinkRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cAclLinkRowStatus.setStatus("current")


class _Hh3cAclLinkTypeCode_Type(OctetString):
    """Custom type hh3cAclLinkTypeCode based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Hh3cAclLinkTypeCode_Type.__name__ = "OctetString"
_Hh3cAclLinkTypeCode_Object = MibTableColumn
hh3cAclLinkTypeCode = _Hh3cAclLinkTypeCode_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 1, 7, 1, 21),
    _Hh3cAclLinkTypeCode_Type()
)
hh3cAclLinkTypeCode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cAclLinkTypeCode.setStatus("current")


class _Hh3cAclLinkTypeMask_Type(OctetString):
    """Custom type hh3cAclLinkTypeMask based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Hh3cAclLinkTypeMask_Type.__name__ = "OctetString"
_Hh3cAclLinkTypeMask_Object = MibTableColumn
hh3cAclLinkTypeMask = _Hh3cAclLinkTypeMask_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 1, 7, 1, 22),
    _Hh3cAclLinkTypeMask_Type()
)
hh3cAclLinkTypeMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cAclLinkTypeMask.setStatus("current")


class _Hh3cAclLinkLsapCode_Type(OctetString):
    """Custom type hh3cAclLinkLsapCode based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Hh3cAclLinkLsapCode_Type.__name__ = "OctetString"
_Hh3cAclLinkLsapCode_Object = MibTableColumn
hh3cAclLinkLsapCode = _Hh3cAclLinkLsapCode_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 1, 7, 1, 23),
    _Hh3cAclLinkLsapCode_Type()
)
hh3cAclLinkLsapCode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cAclLinkLsapCode.setStatus("current")


class _Hh3cAclLinkLsapMask_Type(OctetString):
    """Custom type hh3cAclLinkLsapMask based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Hh3cAclLinkLsapMask_Type.__name__ = "OctetString"
_Hh3cAclLinkLsapMask_Object = MibTableColumn
hh3cAclLinkLsapMask = _Hh3cAclLinkLsapMask_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 1, 7, 1, 24),
    _Hh3cAclLinkLsapMask_Type()
)
hh3cAclLinkLsapMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cAclLinkLsapMask.setStatus("current")


class _Hh3cAclLinkL2LabelRangeOp_Type(Integer32):
    """Custom type hh3cAclLinkL2LabelRangeOp based on Integer32"""
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
        *(("invalid", 0),
          ("lt", 1),
          ("eq", 2),
          ("gt", 3),
          ("neq", 4),
          ("range", 5))
    )


_Hh3cAclLinkL2LabelRangeOp_Type.__name__ = "Integer32"
_Hh3cAclLinkL2LabelRangeOp_Object = MibTableColumn
hh3cAclLinkL2LabelRangeOp = _Hh3cAclLinkL2LabelRangeOp_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 1, 7, 1, 25),
    _Hh3cAclLinkL2LabelRangeOp_Type()
)
hh3cAclLinkL2LabelRangeOp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cAclLinkL2LabelRangeOp.setStatus("current")
_Hh3cAclLinkL2LabelRangeBegin_Type = Integer32
_Hh3cAclLinkL2LabelRangeBegin_Object = MibTableColumn
hh3cAclLinkL2LabelRangeBegin = _Hh3cAclLinkL2LabelRangeBegin_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 1, 7, 1, 26),
    _Hh3cAclLinkL2LabelRangeBegin_Type()
)
hh3cAclLinkL2LabelRangeBegin.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cAclLinkL2LabelRangeBegin.setStatus("current")
_Hh3cAclLinkL2LabelRangeEnd_Type = Integer32
_Hh3cAclLinkL2LabelRangeEnd_Object = MibTableColumn
hh3cAclLinkL2LabelRangeEnd = _Hh3cAclLinkL2LabelRangeEnd_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 1, 7, 1, 27),
    _Hh3cAclLinkL2LabelRangeEnd_Type()
)
hh3cAclLinkL2LabelRangeEnd.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cAclLinkL2LabelRangeEnd.setStatus("current")
_Hh3cAclLinkMplsExp_Type = Integer32
_Hh3cAclLinkMplsExp_Object = MibTableColumn
hh3cAclLinkMplsExp = _Hh3cAclLinkMplsExp_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 1, 7, 1, 28),
    _Hh3cAclLinkMplsExp_Type()
)
hh3cAclLinkMplsExp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cAclLinkMplsExp.setStatus("current")
_Hh3cAclUserTable_Object = MibTable
hh3cAclUserTable = _Hh3cAclUserTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 1, 8)
)
if mibBuilder.loadTexts:
    hh3cAclUserTable.setStatus("current")
_Hh3cAclUserEntry_Object = MibTableRow
hh3cAclUserEntry = _Hh3cAclUserEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 1, 8, 1)
)
hh3cAclUserEntry.setIndexNames(
    (0, "HH3C-ACL-MIB", "hh3cAclUserAclNum"),
    (0, "HH3C-ACL-MIB", "hh3cAclUserSubitem"),
)
if mibBuilder.loadTexts:
    hh3cAclUserEntry.setStatus("current")


class _Hh3cAclUserAclNum_Type(Integer32):
    """Custom type hh3cAclUserAclNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(5000, 5999),
        ValueRangeConstraint(10000, 12999),
    )


_Hh3cAclUserAclNum_Type.__name__ = "Integer32"
_Hh3cAclUserAclNum_Object = MibTableColumn
hh3cAclUserAclNum = _Hh3cAclUserAclNum_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 1, 8, 1, 1),
    _Hh3cAclUserAclNum_Type()
)
hh3cAclUserAclNum.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cAclUserAclNum.setStatus("current")


class _Hh3cAclUserSubitem_Type(Integer32):
    """Custom type hh3cAclUserSubitem based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Hh3cAclUserSubitem_Type.__name__ = "Integer32"
_Hh3cAclUserSubitem_Object = MibTableColumn
hh3cAclUserSubitem = _Hh3cAclUserSubitem_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 1, 8, 1, 2),
    _Hh3cAclUserSubitem_Type()
)
hh3cAclUserSubitem.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cAclUserSubitem.setStatus("current")


class _Hh3cAclUserAct_Type(Integer32):
    """Custom type hh3cAclUserAct based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("permit", 1),
          ("deny", 2))
    )


_Hh3cAclUserAct_Type.__name__ = "Integer32"
_Hh3cAclUserAct_Object = MibTableColumn
hh3cAclUserAct = _Hh3cAclUserAct_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 1, 8, 1, 3),
    _Hh3cAclUserAct_Type()
)
hh3cAclUserAct.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cAclUserAct.setStatus("current")


class _Hh3cAclUserFormatType_Type(Integer32):
    """Custom type hh3cAclUserFormatType based on Integer32"""
    defaultValue = 0

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
        *(("invalid", 0),
          ("ethernetII", 1),
          ("snap", 2),
          ("ieee802Dot2And3", 3),
          ("ieee802Dot4", 4))
    )


_Hh3cAclUserFormatType_Type.__name__ = "Integer32"
_Hh3cAclUserFormatType_Object = MibTableColumn
hh3cAclUserFormatType = _Hh3cAclUserFormatType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 1, 8, 1, 4),
    _Hh3cAclUserFormatType_Type()
)
hh3cAclUserFormatType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cAclUserFormatType.setStatus("current")


class _Hh3cAclUserVlanTag_Type(Integer32):
    """Custom type hh3cAclUserVlanTag based on Integer32"""
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
        *(("invalid", 0),
          ("tagged", 1),
          ("untagged", 2))
    )


_Hh3cAclUserVlanTag_Type.__name__ = "Integer32"
_Hh3cAclUserVlanTag_Object = MibTableColumn
hh3cAclUserVlanTag = _Hh3cAclUserVlanTag_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 1, 8, 1, 5),
    _Hh3cAclUserVlanTag_Type()
)
hh3cAclUserVlanTag.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cAclUserVlanTag.setStatus("current")


class _Hh3cAclUserRuleStr_Type(OctetString):
    """Custom type hh3cAclUserRuleStr based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 80),
    )


_Hh3cAclUserRuleStr_Type.__name__ = "OctetString"
_Hh3cAclUserRuleStr_Object = MibTableColumn
hh3cAclUserRuleStr = _Hh3cAclUserRuleStr_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 1, 8, 1, 6),
    _Hh3cAclUserRuleStr_Type()
)
hh3cAclUserRuleStr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cAclUserRuleStr.setStatus("current")


class _Hh3cAclUserRuleMask_Type(OctetString):
    """Custom type hh3cAclUserRuleMask based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 80),
    )


_Hh3cAclUserRuleMask_Type.__name__ = "OctetString"
_Hh3cAclUserRuleMask_Object = MibTableColumn
hh3cAclUserRuleMask = _Hh3cAclUserRuleMask_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 1, 8, 1, 7),
    _Hh3cAclUserRuleMask_Type()
)
hh3cAclUserRuleMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cAclUserRuleMask.setStatus("current")


class _Hh3cAclUserTimeRangeName_Type(OctetString):
    """Custom type hh3cAclUserTimeRangeName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Hh3cAclUserTimeRangeName_Type.__name__ = "OctetString"
_Hh3cAclUserTimeRangeName_Object = MibTableColumn
hh3cAclUserTimeRangeName = _Hh3cAclUserTimeRangeName_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 1, 8, 1, 8),
    _Hh3cAclUserTimeRangeName_Type()
)
hh3cAclUserTimeRangeName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cAclUserTimeRangeName.setStatus("current")
_Hh3cAclUserEnable_Type = TruthValue
_Hh3cAclUserEnable_Object = MibTableColumn
hh3cAclUserEnable = _Hh3cAclUserEnable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 1, 8, 1, 9),
    _Hh3cAclUserEnable_Type()
)
hh3cAclUserEnable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cAclUserEnable.setStatus("current")
_Hh3cAclUserRowStatus_Type = RowStatus
_Hh3cAclUserRowStatus_Object = MibTableColumn
hh3cAclUserRowStatus = _Hh3cAclUserRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 1, 8, 1, 10),
    _Hh3cAclUserRowStatus_Type()
)
hh3cAclUserRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cAclUserRowStatus.setStatus("current")
_Hh3cAclActiveTable_Object = MibTable
hh3cAclActiveTable = _Hh3cAclActiveTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 1, 9)
)
if mibBuilder.loadTexts:
    hh3cAclActiveTable.setStatus("current")
_Hh3cAclActiveEntry_Object = MibTableRow
hh3cAclActiveEntry = _Hh3cAclActiveEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 1, 9, 1)
)
hh3cAclActiveEntry.setIndexNames(
    (0, "HH3C-ACL-MIB", "hh3cAclActiveAclIndex"),
    (0, "HH3C-ACL-MIB", "hh3cAclActiveIfIndex"),
    (0, "HH3C-ACL-MIB", "hh3cAclActiveVlanID"),
    (0, "HH3C-ACL-MIB", "hh3cAclActiveDirection"),
)
if mibBuilder.loadTexts:
    hh3cAclActiveEntry.setStatus("current")


class _Hh3cAclActiveAclIndex_Type(Integer32):
    """Custom type hh3cAclActiveAclIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 5999),
        ValueRangeConstraint(10000, 12999),
    )


_Hh3cAclActiveAclIndex_Type.__name__ = "Integer32"
_Hh3cAclActiveAclIndex_Object = MibTableColumn
hh3cAclActiveAclIndex = _Hh3cAclActiveAclIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 1, 9, 1, 1),
    _Hh3cAclActiveAclIndex_Type()
)
hh3cAclActiveAclIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cAclActiveAclIndex.setStatus("current")


class _Hh3cAclActiveIfIndex_Type(Integer32):
    """Custom type hh3cAclActiveIfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_Hh3cAclActiveIfIndex_Type.__name__ = "Integer32"
_Hh3cAclActiveIfIndex_Object = MibTableColumn
hh3cAclActiveIfIndex = _Hh3cAclActiveIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 1, 9, 1, 2),
    _Hh3cAclActiveIfIndex_Type()
)
hh3cAclActiveIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cAclActiveIfIndex.setStatus("current")
_Hh3cAclActiveVlanID_Type = Integer32
_Hh3cAclActiveVlanID_Object = MibTableColumn
hh3cAclActiveVlanID = _Hh3cAclActiveVlanID_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 1, 9, 1, 3),
    _Hh3cAclActiveVlanID_Type()
)
hh3cAclActiveVlanID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cAclActiveVlanID.setStatus("current")


class _Hh3cAclActiveDirection_Type(Integer32):
    """Custom type hh3cAclActiveDirection based on Integer32"""
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
        *(("invalid", 0),
          ("input", 1),
          ("output", 2),
          ("both", 3))
    )


_Hh3cAclActiveDirection_Type.__name__ = "Integer32"
_Hh3cAclActiveDirection_Object = MibTableColumn
hh3cAclActiveDirection = _Hh3cAclActiveDirection_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 1, 9, 1, 4),
    _Hh3cAclActiveDirection_Type()
)
hh3cAclActiveDirection.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cAclActiveDirection.setStatus("current")


class _Hh3cAclActiveUserAclNum_Type(Integer32):
    """Custom type hh3cAclActiveUserAclNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(5000, 5999),
        ValueRangeConstraint(10000, 12999),
    )


_Hh3cAclActiveUserAclNum_Type.__name__ = "Integer32"
_Hh3cAclActiveUserAclNum_Object = MibTableColumn
hh3cAclActiveUserAclNum = _Hh3cAclActiveUserAclNum_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 1, 9, 1, 5),
    _Hh3cAclActiveUserAclNum_Type()
)
hh3cAclActiveUserAclNum.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cAclActiveUserAclNum.setStatus("current")


class _Hh3cAclActiveUserAclSubitem_Type(Integer32):
    """Custom type hh3cAclActiveUserAclSubitem based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Hh3cAclActiveUserAclSubitem_Type.__name__ = "Integer32"
_Hh3cAclActiveUserAclSubitem_Object = MibTableColumn
hh3cAclActiveUserAclSubitem = _Hh3cAclActiveUserAclSubitem_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 1, 9, 1, 6),
    _Hh3cAclActiveUserAclSubitem_Type()
)
hh3cAclActiveUserAclSubitem.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cAclActiveUserAclSubitem.setStatus("current")


class _Hh3cAclActiveIpAclNum_Type(Integer32):
    """Custom type hh3cAclActiveIpAclNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(2000, 3999),
        ValueRangeConstraint(10000, 12999),
    )


_Hh3cAclActiveIpAclNum_Type.__name__ = "Integer32"
_Hh3cAclActiveIpAclNum_Object = MibTableColumn
hh3cAclActiveIpAclNum = _Hh3cAclActiveIpAclNum_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 1, 9, 1, 7),
    _Hh3cAclActiveIpAclNum_Type()
)
hh3cAclActiveIpAclNum.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cAclActiveIpAclNum.setStatus("current")


class _Hh3cAclActiveIpAclSubitem_Type(Integer32):
    """Custom type hh3cAclActiveIpAclSubitem based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Hh3cAclActiveIpAclSubitem_Type.__name__ = "Integer32"
_Hh3cAclActiveIpAclSubitem_Object = MibTableColumn
hh3cAclActiveIpAclSubitem = _Hh3cAclActiveIpAclSubitem_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 1, 9, 1, 8),
    _Hh3cAclActiveIpAclSubitem_Type()
)
hh3cAclActiveIpAclSubitem.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cAclActiveIpAclSubitem.setStatus("current")


class _Hh3cAclActiveLinkAclNum_Type(Integer32):
    """Custom type hh3cAclActiveLinkAclNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(4000, 4999),
        ValueRangeConstraint(10000, 12999),
    )


_Hh3cAclActiveLinkAclNum_Type.__name__ = "Integer32"
_Hh3cAclActiveLinkAclNum_Object = MibTableColumn
hh3cAclActiveLinkAclNum = _Hh3cAclActiveLinkAclNum_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 1, 9, 1, 9),
    _Hh3cAclActiveLinkAclNum_Type()
)
hh3cAclActiveLinkAclNum.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cAclActiveLinkAclNum.setStatus("current")


class _Hh3cAclActiveLinkAclSubitem_Type(Integer32):
    """Custom type hh3cAclActiveLinkAclSubitem based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Hh3cAclActiveLinkAclSubitem_Type.__name__ = "Integer32"
_Hh3cAclActiveLinkAclSubitem_Object = MibTableColumn
hh3cAclActiveLinkAclSubitem = _Hh3cAclActiveLinkAclSubitem_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 1, 9, 1, 10),
    _Hh3cAclActiveLinkAclSubitem_Type()
)
hh3cAclActiveLinkAclSubitem.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cAclActiveLinkAclSubitem.setStatus("current")
_Hh3cAclActiveRuntime_Type = TruthValue
_Hh3cAclActiveRuntime_Object = MibTableColumn
hh3cAclActiveRuntime = _Hh3cAclActiveRuntime_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 1, 9, 1, 11),
    _Hh3cAclActiveRuntime_Type()
)
hh3cAclActiveRuntime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cAclActiveRuntime.setStatus("current")
_Hh3cAclActiveRowStatus_Type = RowStatus
_Hh3cAclActiveRowStatus_Object = MibTableColumn
hh3cAclActiveRowStatus = _Hh3cAclActiveRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 1, 9, 1, 12),
    _Hh3cAclActiveRowStatus_Type()
)
hh3cAclActiveRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cAclActiveRowStatus.setStatus("current")
_Hh3cAclIDSTable_Object = MibTable
hh3cAclIDSTable = _Hh3cAclIDSTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 1, 10)
)
if mibBuilder.loadTexts:
    hh3cAclIDSTable.setStatus("current")
_Hh3cAclIDSEntry_Object = MibTableRow
hh3cAclIDSEntry = _Hh3cAclIDSEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 1, 10, 1)
)
hh3cAclIDSEntry.setIndexNames(
    (1, "HH3C-ACL-MIB", "hh3cAclIDSName"),
)
if mibBuilder.loadTexts:
    hh3cAclIDSEntry.setStatus("current")


class _Hh3cAclIDSName_Type(OctetString):
    """Custom type hh3cAclIDSName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_Hh3cAclIDSName_Type.__name__ = "OctetString"
_Hh3cAclIDSName_Object = MibTableColumn
hh3cAclIDSName = _Hh3cAclIDSName_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 1, 10, 1, 1),
    _Hh3cAclIDSName_Type()
)
hh3cAclIDSName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cAclIDSName.setStatus("current")
_Hh3cAclIDSSrcMac_Type = MacAddress
_Hh3cAclIDSSrcMac_Object = MibTableColumn
hh3cAclIDSSrcMac = _Hh3cAclIDSSrcMac_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 1, 10, 1, 2),
    _Hh3cAclIDSSrcMac_Type()
)
hh3cAclIDSSrcMac.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cAclIDSSrcMac.setStatus("current")
_Hh3cAclIDSDestMac_Type = MacAddress
_Hh3cAclIDSDestMac_Object = MibTableColumn
hh3cAclIDSDestMac = _Hh3cAclIDSDestMac_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 1, 10, 1, 3),
    _Hh3cAclIDSDestMac_Type()
)
hh3cAclIDSDestMac.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cAclIDSDestMac.setStatus("current")
_Hh3cAclIDSSrcIp_Type = IpAddress
_Hh3cAclIDSSrcIp_Object = MibTableColumn
hh3cAclIDSSrcIp = _Hh3cAclIDSSrcIp_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 1, 10, 1, 4),
    _Hh3cAclIDSSrcIp_Type()
)
hh3cAclIDSSrcIp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cAclIDSSrcIp.setStatus("current")
_Hh3cAclIDSSrcWild_Type = IpAddress
_Hh3cAclIDSSrcWild_Object = MibTableColumn
hh3cAclIDSSrcWild = _Hh3cAclIDSSrcWild_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 1, 10, 1, 5),
    _Hh3cAclIDSSrcWild_Type()
)
hh3cAclIDSSrcWild.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cAclIDSSrcWild.setStatus("current")
_Hh3cAclIDSDestIp_Type = IpAddress
_Hh3cAclIDSDestIp_Object = MibTableColumn
hh3cAclIDSDestIp = _Hh3cAclIDSDestIp_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 1, 10, 1, 6),
    _Hh3cAclIDSDestIp_Type()
)
hh3cAclIDSDestIp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cAclIDSDestIp.setStatus("current")
_Hh3cAclIDSDestWild_Type = IpAddress
_Hh3cAclIDSDestWild_Object = MibTableColumn
hh3cAclIDSDestWild = _Hh3cAclIDSDestWild_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 1, 10, 1, 7),
    _Hh3cAclIDSDestWild_Type()
)
hh3cAclIDSDestWild.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cAclIDSDestWild.setStatus("current")


class _Hh3cAclIDSSrcPort_Type(Integer32):
    """Custom type hh3cAclIDSSrcPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Hh3cAclIDSSrcPort_Type.__name__ = "Integer32"
_Hh3cAclIDSSrcPort_Object = MibTableColumn
hh3cAclIDSSrcPort = _Hh3cAclIDSSrcPort_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 1, 10, 1, 8),
    _Hh3cAclIDSSrcPort_Type()
)
hh3cAclIDSSrcPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cAclIDSSrcPort.setStatus("current")


class _Hh3cAclIDSDestPort_Type(Integer32):
    """Custom type hh3cAclIDSDestPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Hh3cAclIDSDestPort_Type.__name__ = "Integer32"
_Hh3cAclIDSDestPort_Object = MibTableColumn
hh3cAclIDSDestPort = _Hh3cAclIDSDestPort_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 1, 10, 1, 9),
    _Hh3cAclIDSDestPort_Type()
)
hh3cAclIDSDestPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cAclIDSDestPort.setStatus("current")


class _Hh3cAclIDSProtocol_Type(Integer32):
    """Custom type hh3cAclIDSProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_Hh3cAclIDSProtocol_Type.__name__ = "Integer32"
_Hh3cAclIDSProtocol_Object = MibTableColumn
hh3cAclIDSProtocol = _Hh3cAclIDSProtocol_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 1, 10, 1, 10),
    _Hh3cAclIDSProtocol_Type()
)
hh3cAclIDSProtocol.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cAclIDSProtocol.setStatus("current")


class _Hh3cAclIDSDenyTime_Type(Unsigned32):
    """Custom type hh3cAclIDSDenyTime based on Unsigned32"""
    defaultValue = 0


_Hh3cAclIDSDenyTime_Type.__name__ = "Unsigned32"
_Hh3cAclIDSDenyTime_Object = MibTableColumn
hh3cAclIDSDenyTime = _Hh3cAclIDSDenyTime_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 1, 10, 1, 11),
    _Hh3cAclIDSDenyTime_Type()
)
hh3cAclIDSDenyTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cAclIDSDenyTime.setStatus("current")


class _Hh3cAclIDSAct_Type(Integer32):
    """Custom type hh3cAclIDSAct based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("permit", 1),
          ("deny", 2))
    )


_Hh3cAclIDSAct_Type.__name__ = "Integer32"
_Hh3cAclIDSAct_Object = MibTableColumn
hh3cAclIDSAct = _Hh3cAclIDSAct_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 1, 10, 1, 12),
    _Hh3cAclIDSAct_Type()
)
hh3cAclIDSAct.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cAclIDSAct.setStatus("current")
_Hh3cAclIDSRowStatus_Type = RowStatus
_Hh3cAclIDSRowStatus_Object = MibTableColumn
hh3cAclIDSRowStatus = _Hh3cAclIDSRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 1, 10, 1, 13),
    _Hh3cAclIDSRowStatus_Type()
)
hh3cAclIDSRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cAclIDSRowStatus.setStatus("current")
_Hh3cAclMib2Objects_ObjectIdentity = ObjectIdentity
hh3cAclMib2Objects = _Hh3cAclMib2Objects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 2)
)
_Hh3cAclMib2GlobalGroup_ObjectIdentity = ObjectIdentity
hh3cAclMib2GlobalGroup = _Hh3cAclMib2GlobalGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 2, 1)
)
_Hh3cAclMib2NodesGroup_ObjectIdentity = ObjectIdentity
hh3cAclMib2NodesGroup = _Hh3cAclMib2NodesGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 2, 1, 1)
)


class _Hh3cAclMib2Mode_Type(Integer32):
    """Custom type hh3cAclMib2Mode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("linkBased", 1),
          ("ipBased", 2))
    )


_Hh3cAclMib2Mode_Type.__name__ = "Integer32"
_Hh3cAclMib2Mode_Object = MibScalar
hh3cAclMib2Mode = _Hh3cAclMib2Mode_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 2, 1, 1, 1),
    _Hh3cAclMib2Mode_Type()
)
hh3cAclMib2Mode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cAclMib2Mode.setStatus("current")
_Hh3cAclMib2Version_Type = Integer32
_Hh3cAclMib2Version_Object = MibScalar
hh3cAclMib2Version = _Hh3cAclMib2Version_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 2, 1, 1, 2),
    _Hh3cAclMib2Version_Type()
)
hh3cAclMib2Version.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cAclMib2Version.setStatus("current")


class _Hh3cAclMib2ObjectsCapabilities_Type(Bits):
    """Custom type hh3cAclMib2ObjectsCapabilities based on Bits"""
    namedValues = NamedValues(
        *(("hh3cAclMib2Mode", 0),
          ("hh3cAclVersion", 1),
          ("hh3cAclMib2ObjectsCapabilities", 2),
          ("hh3cAclMib2CapabilityTable", 3),
          ("hh3cAclNumberGroupTable", 4),
          ("hh3cAclIPAclBasicTable", 5),
          ("hh3cAclIPAclAdvancedTable", 6),
          ("hh3cAclMACTable", 7),
          ("hh3cAclEnUserTable", 8),
          ("hh3cAclMib2ProcessingStatus", 9))
    )

_Hh3cAclMib2ObjectsCapabilities_Type.__name__ = "Bits"
_Hh3cAclMib2ObjectsCapabilities_Object = MibScalar
hh3cAclMib2ObjectsCapabilities = _Hh3cAclMib2ObjectsCapabilities_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 2, 1, 1, 3),
    _Hh3cAclMib2ObjectsCapabilities_Type()
)
hh3cAclMib2ObjectsCapabilities.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cAclMib2ObjectsCapabilities.setStatus("current")


class _Hh3cAclMib2ProcessingStatus_Type(Integer32):
    """Custom type hh3cAclMib2ProcessingStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("processing", 1),
          ("done", 2))
    )


_Hh3cAclMib2ProcessingStatus_Type.__name__ = "Integer32"
_Hh3cAclMib2ProcessingStatus_Object = MibScalar
hh3cAclMib2ProcessingStatus = _Hh3cAclMib2ProcessingStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 2, 1, 1, 4),
    _Hh3cAclMib2ProcessingStatus_Type()
)
hh3cAclMib2ProcessingStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cAclMib2ProcessingStatus.setStatus("current")


class _Hh3cAclMib2ResourceThreshold_Type(Integer32):
    """Custom type hh3cAclMib2ResourceThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Hh3cAclMib2ResourceThreshold_Type.__name__ = "Integer32"
_Hh3cAclMib2ResourceThreshold_Object = MibScalar
hh3cAclMib2ResourceThreshold = _Hh3cAclMib2ResourceThreshold_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 2, 1, 1, 5),
    _Hh3cAclMib2ResourceThreshold_Type()
)
hh3cAclMib2ResourceThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cAclMib2ResourceThreshold.setStatus("current")


class _Hh3cAclMib2ResourceLogInterval_Type(Integer32):
    """Custom type hh3cAclMib2ResourceLogInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 60),
    )


_Hh3cAclMib2ResourceLogInterval_Type.__name__ = "Integer32"
_Hh3cAclMib2ResourceLogInterval_Object = MibScalar
hh3cAclMib2ResourceLogInterval = _Hh3cAclMib2ResourceLogInterval_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 2, 1, 1, 6),
    _Hh3cAclMib2ResourceLogInterval_Type()
)
hh3cAclMib2ResourceLogInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cAclMib2ResourceLogInterval.setStatus("current")
_Hh3cAclMib2CapabilityTable_Object = MibTable
hh3cAclMib2CapabilityTable = _Hh3cAclMib2CapabilityTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 2, 1, 2)
)
if mibBuilder.loadTexts:
    hh3cAclMib2CapabilityTable.setStatus("current")
_Hh3cAclMib2CapabilityEntry_Object = MibTableRow
hh3cAclMib2CapabilityEntry = _Hh3cAclMib2CapabilityEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 2, 1, 2, 1)
)
hh3cAclMib2CapabilityEntry.setIndexNames(
    (0, "HH3C-ACL-MIB", "hh3cAclMib2EntityType"),
    (0, "HH3C-ACL-MIB", "hh3cAclMib2EntityIndex"),
    (0, "HH3C-ACL-MIB", "hh3cAclMib2ModuleIndex"),
    (0, "HH3C-ACL-MIB", "hh3cAclMib2CharacteristicsIndex"),
)
if mibBuilder.loadTexts:
    hh3cAclMib2CapabilityEntry.setStatus("current")


class _Hh3cAclMib2EntityType_Type(Integer32):
    """Custom type hh3cAclMib2EntityType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("system", 1),
          ("interface", 2))
    )


_Hh3cAclMib2EntityType_Type.__name__ = "Integer32"
_Hh3cAclMib2EntityType_Object = MibTableColumn
hh3cAclMib2EntityType = _Hh3cAclMib2EntityType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 2, 1, 2, 1, 1),
    _Hh3cAclMib2EntityType_Type()
)
hh3cAclMib2EntityType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cAclMib2EntityType.setStatus("current")


class _Hh3cAclMib2EntityIndex_Type(Integer32):
    """Custom type hh3cAclMib2EntityIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_Hh3cAclMib2EntityIndex_Type.__name__ = "Integer32"
_Hh3cAclMib2EntityIndex_Object = MibTableColumn
hh3cAclMib2EntityIndex = _Hh3cAclMib2EntityIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 2, 1, 2, 1, 2),
    _Hh3cAclMib2EntityIndex_Type()
)
hh3cAclMib2EntityIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cAclMib2EntityIndex.setStatus("current")


class _Hh3cAclMib2ModuleIndex_Type(Integer32):
    """Custom type hh3cAclMib2ModuleIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("layer3", 1),
          ("layer2", 2),
          ("userDefined", 3))
    )


_Hh3cAclMib2ModuleIndex_Type.__name__ = "Integer32"
_Hh3cAclMib2ModuleIndex_Object = MibTableColumn
hh3cAclMib2ModuleIndex = _Hh3cAclMib2ModuleIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 2, 1, 2, 1, 3),
    _Hh3cAclMib2ModuleIndex_Type()
)
hh3cAclMib2ModuleIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cAclMib2ModuleIndex.setStatus("current")


class _Hh3cAclMib2CharacteristicsIndex_Type(Integer32):
    """Custom type hh3cAclMib2CharacteristicsIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_Hh3cAclMib2CharacteristicsIndex_Type.__name__ = "Integer32"
_Hh3cAclMib2CharacteristicsIndex_Object = MibTableColumn
hh3cAclMib2CharacteristicsIndex = _Hh3cAclMib2CharacteristicsIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 2, 1, 2, 1, 4),
    _Hh3cAclMib2CharacteristicsIndex_Type()
)
hh3cAclMib2CharacteristicsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cAclMib2CharacteristicsIndex.setStatus("current")


class _Hh3cAclMib2CharacteristicsDesc_Type(OctetString):
    """Custom type hh3cAclMib2CharacteristicsDesc based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_Hh3cAclMib2CharacteristicsDesc_Type.__name__ = "OctetString"
_Hh3cAclMib2CharacteristicsDesc_Object = MibTableColumn
hh3cAclMib2CharacteristicsDesc = _Hh3cAclMib2CharacteristicsDesc_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 2, 1, 2, 1, 5),
    _Hh3cAclMib2CharacteristicsDesc_Type()
)
hh3cAclMib2CharacteristicsDesc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cAclMib2CharacteristicsDesc.setStatus("current")
_Hh3cAclMib2CharacteristicsValue_Type = Unsigned32
_Hh3cAclMib2CharacteristicsValue_Object = MibTableColumn
hh3cAclMib2CharacteristicsValue = _Hh3cAclMib2CharacteristicsValue_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 2, 1, 2, 1, 6),
    _Hh3cAclMib2CharacteristicsValue_Type()
)
hh3cAclMib2CharacteristicsValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cAclMib2CharacteristicsValue.setStatus("current")
_Hh3cAclNumberGroupTable_Object = MibTable
hh3cAclNumberGroupTable = _Hh3cAclNumberGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 2, 1, 3)
)
if mibBuilder.loadTexts:
    hh3cAclNumberGroupTable.setStatus("current")
_Hh3cAclNumberGroupEntry_Object = MibTableRow
hh3cAclNumberGroupEntry = _Hh3cAclNumberGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 2, 1, 3, 1)
)
hh3cAclNumberGroupEntry.setIndexNames(
    (0, "HH3C-ACL-MIB", "hh3cAclNumberGroupType"),
    (0, "HH3C-ACL-MIB", "hh3cAclNumberGroupIndex"),
)
if mibBuilder.loadTexts:
    hh3cAclNumberGroupEntry.setStatus("current")


class _Hh3cAclNumberGroupType_Type(Integer32):
    """Custom type hh3cAclNumberGroupType based on Integer32"""
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
        *(("ipv4", 1),
          ("ipv6", 2),
          ("mac", 3),
          ("user", 4))
    )


_Hh3cAclNumberGroupType_Type.__name__ = "Integer32"
_Hh3cAclNumberGroupType_Object = MibTableColumn
hh3cAclNumberGroupType = _Hh3cAclNumberGroupType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 2, 1, 3, 1, 1),
    _Hh3cAclNumberGroupType_Type()
)
hh3cAclNumberGroupType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cAclNumberGroupType.setStatus("current")


class _Hh3cAclNumberGroupIndex_Type(Integer32):
    """Custom type hh3cAclNumberGroupIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2000, 5999),
        ValueRangeConstraint(10000, 42767),
    )


_Hh3cAclNumberGroupIndex_Type.__name__ = "Integer32"
_Hh3cAclNumberGroupIndex_Object = MibTableColumn
hh3cAclNumberGroupIndex = _Hh3cAclNumberGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 2, 1, 3, 1, 2),
    _Hh3cAclNumberGroupIndex_Type()
)
hh3cAclNumberGroupIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cAclNumberGroupIndex.setStatus("current")
_Hh3cAclNumberGroupRowStatus_Type = RowStatus
_Hh3cAclNumberGroupRowStatus_Object = MibTableColumn
hh3cAclNumberGroupRowStatus = _Hh3cAclNumberGroupRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 2, 1, 3, 1, 3),
    _Hh3cAclNumberGroupRowStatus_Type()
)
hh3cAclNumberGroupRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cAclNumberGroupRowStatus.setStatus("current")


class _Hh3cAclNumberGroupMatchOrder_Type(Integer32):
    """Custom type hh3cAclNumberGroupMatchOrder based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("config", 1),
          ("auto", 2))
    )


_Hh3cAclNumberGroupMatchOrder_Type.__name__ = "Integer32"
_Hh3cAclNumberGroupMatchOrder_Object = MibTableColumn
hh3cAclNumberGroupMatchOrder = _Hh3cAclNumberGroupMatchOrder_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 2, 1, 3, 1, 4),
    _Hh3cAclNumberGroupMatchOrder_Type()
)
hh3cAclNumberGroupMatchOrder.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cAclNumberGroupMatchOrder.setStatus("current")


class _Hh3cAclNumberGroupStep_Type(Integer32):
    """Custom type hh3cAclNumberGroupStep based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 20),
    )


_Hh3cAclNumberGroupStep_Type.__name__ = "Integer32"
_Hh3cAclNumberGroupStep_Object = MibTableColumn
hh3cAclNumberGroupStep = _Hh3cAclNumberGroupStep_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 2, 1, 3, 1, 5),
    _Hh3cAclNumberGroupStep_Type()
)
hh3cAclNumberGroupStep.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cAclNumberGroupStep.setStatus("current")


class _Hh3cAclNumberGroupDescription_Type(OctetString):
    """Custom type hh3cAclNumberGroupDescription based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_Hh3cAclNumberGroupDescription_Type.__name__ = "OctetString"
_Hh3cAclNumberGroupDescription_Object = MibTableColumn
hh3cAclNumberGroupDescription = _Hh3cAclNumberGroupDescription_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 2, 1, 3, 1, 6),
    _Hh3cAclNumberGroupDescription_Type()
)
hh3cAclNumberGroupDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cAclNumberGroupDescription.setStatus("current")


class _Hh3cAclNumberGroupCountClear_Type(CounterClear):
    """Custom type hh3cAclNumberGroupCountClear based on CounterClear"""
    defaultValue = 2


_Hh3cAclNumberGroupCountClear_Type.__name__ = "CounterClear"
_Hh3cAclNumberGroupCountClear_Object = MibTableColumn
hh3cAclNumberGroupCountClear = _Hh3cAclNumberGroupCountClear_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 2, 1, 3, 1, 7),
    _Hh3cAclNumberGroupCountClear_Type()
)
hh3cAclNumberGroupCountClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cAclNumberGroupCountClear.setStatus("current")
_Hh3cAclNumberGroupRuleCounter_Type = Counter32
_Hh3cAclNumberGroupRuleCounter_Object = MibTableColumn
hh3cAclNumberGroupRuleCounter = _Hh3cAclNumberGroupRuleCounter_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 2, 1, 3, 1, 8),
    _Hh3cAclNumberGroupRuleCounter_Type()
)
hh3cAclNumberGroupRuleCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cAclNumberGroupRuleCounter.setStatus("current")


class _Hh3cAclNumberGroupName_Type(OctetString):
    """Custom type hh3cAclNumberGroupName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_Hh3cAclNumberGroupName_Type.__name__ = "OctetString"
_Hh3cAclNumberGroupName_Object = MibTableColumn
hh3cAclNumberGroupName = _Hh3cAclNumberGroupName_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 2, 1, 3, 1, 9),
    _Hh3cAclNumberGroupName_Type()
)
hh3cAclNumberGroupName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cAclNumberGroupName.setStatus("current")
_Hh3cAclNamedGroupTable_Object = MibTable
hh3cAclNamedGroupTable = _Hh3cAclNamedGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 2, 1, 4)
)
if mibBuilder.loadTexts:
    hh3cAclNamedGroupTable.setStatus("current")
_Hh3cAclNamedGroupEntry_Object = MibTableRow
hh3cAclNamedGroupEntry = _Hh3cAclNamedGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 2, 1, 4, 1)
)
hh3cAclNamedGroupEntry.setIndexNames(
    (0, "HH3C-ACL-MIB", "hh3cAclNumberGroupType"),
    (0, "HH3C-ACL-MIB", "hh3cAclNamedGroupCategory"),
    (0, "HH3C-ACL-MIB", "hh3cAclNamedGroupName"),
)
if mibBuilder.loadTexts:
    hh3cAclNamedGroupEntry.setStatus("current")


class _Hh3cAclNamedGroupCategory_Type(Integer32):
    """Custom type hh3cAclNamedGroupCategory based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 0),
          ("basic", 1),
          ("advanced", 2))
    )


_Hh3cAclNamedGroupCategory_Type.__name__ = "Integer32"
_Hh3cAclNamedGroupCategory_Object = MibTableColumn
hh3cAclNamedGroupCategory = _Hh3cAclNamedGroupCategory_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 2, 1, 4, 1, 1),
    _Hh3cAclNamedGroupCategory_Type()
)
hh3cAclNamedGroupCategory.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cAclNamedGroupCategory.setStatus("current")


class _Hh3cAclNamedGroupName_Type(OctetString):
    """Custom type hh3cAclNamedGroupName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 63),
    )


_Hh3cAclNamedGroupName_Type.__name__ = "OctetString"
_Hh3cAclNamedGroupName_Object = MibTableColumn
hh3cAclNamedGroupName = _Hh3cAclNamedGroupName_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 2, 1, 4, 1, 2),
    _Hh3cAclNamedGroupName_Type()
)
hh3cAclNamedGroupName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cAclNamedGroupName.setStatus("current")
_Hh3cAclNamedGroupRowStatus_Type = RowStatus
_Hh3cAclNamedGroupRowStatus_Object = MibTableColumn
hh3cAclNamedGroupRowStatus = _Hh3cAclNamedGroupRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 2, 1, 4, 1, 3),
    _Hh3cAclNamedGroupRowStatus_Type()
)
hh3cAclNamedGroupRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cAclNamedGroupRowStatus.setStatus("current")


class _Hh3cAclNamedGroupMatchOrder_Type(Integer32):
    """Custom type hh3cAclNamedGroupMatchOrder based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("config", 1),
          ("auto", 2))
    )


_Hh3cAclNamedGroupMatchOrder_Type.__name__ = "Integer32"
_Hh3cAclNamedGroupMatchOrder_Object = MibTableColumn
hh3cAclNamedGroupMatchOrder = _Hh3cAclNamedGroupMatchOrder_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 2, 1, 4, 1, 4),
    _Hh3cAclNamedGroupMatchOrder_Type()
)
hh3cAclNamedGroupMatchOrder.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cAclNamedGroupMatchOrder.setStatus("current")


class _Hh3cAclNamedGroupStep_Type(Integer32):
    """Custom type hh3cAclNamedGroupStep based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 20),
    )


_Hh3cAclNamedGroupStep_Type.__name__ = "Integer32"
_Hh3cAclNamedGroupStep_Object = MibTableColumn
hh3cAclNamedGroupStep = _Hh3cAclNamedGroupStep_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 2, 1, 4, 1, 5),
    _Hh3cAclNamedGroupStep_Type()
)
hh3cAclNamedGroupStep.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cAclNamedGroupStep.setStatus("current")


class _Hh3cAclNamedGroupDescription_Type(OctetString):
    """Custom type hh3cAclNamedGroupDescription based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_Hh3cAclNamedGroupDescription_Type.__name__ = "OctetString"
_Hh3cAclNamedGroupDescription_Object = MibTableColumn
hh3cAclNamedGroupDescription = _Hh3cAclNamedGroupDescription_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 2, 1, 4, 1, 6),
    _Hh3cAclNamedGroupDescription_Type()
)
hh3cAclNamedGroupDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cAclNamedGroupDescription.setStatus("current")


class _Hh3cAclNamedGroupCountClear_Type(CounterClear):
    """Custom type hh3cAclNamedGroupCountClear based on CounterClear"""
    defaultValue = 2


_Hh3cAclNamedGroupCountClear_Type.__name__ = "CounterClear"
_Hh3cAclNamedGroupCountClear_Object = MibTableColumn
hh3cAclNamedGroupCountClear = _Hh3cAclNamedGroupCountClear_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 2, 1, 4, 1, 7),
    _Hh3cAclNamedGroupCountClear_Type()
)
hh3cAclNamedGroupCountClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cAclNamedGroupCountClear.setStatus("current")
_Hh3cAclNamedGroupRuleCounter_Type = Counter32
_Hh3cAclNamedGroupRuleCounter_Object = MibTableColumn
hh3cAclNamedGroupRuleCounter = _Hh3cAclNamedGroupRuleCounter_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 2, 1, 4, 1, 8),
    _Hh3cAclNamedGroupRuleCounter_Type()
)
hh3cAclNamedGroupRuleCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cAclNamedGroupRuleCounter.setStatus("current")
_Hh3cAclIPAclGroup_ObjectIdentity = ObjectIdentity
hh3cAclIPAclGroup = _Hh3cAclIPAclGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 2, 2)
)
_Hh3cAclIPAclBasicTable_Object = MibTable
hh3cAclIPAclBasicTable = _Hh3cAclIPAclBasicTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 2, 2, 2)
)
if mibBuilder.loadTexts:
    hh3cAclIPAclBasicTable.setStatus("current")
_Hh3cAclIPAclBasicEntry_Object = MibTableRow
hh3cAclIPAclBasicEntry = _Hh3cAclIPAclBasicEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 2, 2, 2, 1)
)
hh3cAclIPAclBasicEntry.setIndexNames(
    (0, "HH3C-ACL-MIB", "hh3cAclNumberGroupType"),
    (0, "HH3C-ACL-MIB", "hh3cAclNumberGroupIndex"),
    (0, "HH3C-ACL-MIB", "hh3cAclIPAclBasicRuleIndex"),
)
if mibBuilder.loadTexts:
    hh3cAclIPAclBasicEntry.setStatus("current")


class _Hh3cAclIPAclBasicRuleIndex_Type(Integer32):
    """Custom type hh3cAclIPAclBasicRuleIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65534),
    )


_Hh3cAclIPAclBasicRuleIndex_Type.__name__ = "Integer32"
_Hh3cAclIPAclBasicRuleIndex_Object = MibTableColumn
hh3cAclIPAclBasicRuleIndex = _Hh3cAclIPAclBasicRuleIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 2, 2, 2, 1, 1),
    _Hh3cAclIPAclBasicRuleIndex_Type()
)
hh3cAclIPAclBasicRuleIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cAclIPAclBasicRuleIndex.setStatus("current")
_Hh3cAclIPAclBasicRowStatus_Type = RowStatus
_Hh3cAclIPAclBasicRowStatus_Object = MibTableColumn
hh3cAclIPAclBasicRowStatus = _Hh3cAclIPAclBasicRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 2, 2, 2, 1, 2),
    _Hh3cAclIPAclBasicRowStatus_Type()
)
hh3cAclIPAclBasicRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cAclIPAclBasicRowStatus.setStatus("current")
_Hh3cAclIPAclBasicAct_Type = RuleAction
_Hh3cAclIPAclBasicAct_Object = MibTableColumn
hh3cAclIPAclBasicAct = _Hh3cAclIPAclBasicAct_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 2, 2, 2, 1, 3),
    _Hh3cAclIPAclBasicAct_Type()
)
hh3cAclIPAclBasicAct.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cAclIPAclBasicAct.setStatus("current")
_Hh3cAclIPAclBasicSrcAddrType_Type = InetAddressType
_Hh3cAclIPAclBasicSrcAddrType_Object = MibTableColumn
hh3cAclIPAclBasicSrcAddrType = _Hh3cAclIPAclBasicSrcAddrType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 2, 2, 2, 1, 4),
    _Hh3cAclIPAclBasicSrcAddrType_Type()
)
hh3cAclIPAclBasicSrcAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cAclIPAclBasicSrcAddrType.setStatus("current")
_Hh3cAclIPAclBasicSrcAddr_Type = InetAddress
_Hh3cAclIPAclBasicSrcAddr_Object = MibTableColumn
hh3cAclIPAclBasicSrcAddr = _Hh3cAclIPAclBasicSrcAddr_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 2, 2, 2, 1, 5),
    _Hh3cAclIPAclBasicSrcAddr_Type()
)
hh3cAclIPAclBasicSrcAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cAclIPAclBasicSrcAddr.setStatus("current")
_Hh3cAclIPAclBasicSrcPrefix_Type = InetAddressPrefixLength
_Hh3cAclIPAclBasicSrcPrefix_Object = MibTableColumn
hh3cAclIPAclBasicSrcPrefix = _Hh3cAclIPAclBasicSrcPrefix_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 2, 2, 2, 1, 6),
    _Hh3cAclIPAclBasicSrcPrefix_Type()
)
hh3cAclIPAclBasicSrcPrefix.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cAclIPAclBasicSrcPrefix.setStatus("current")


class _Hh3cAclIPAclBasicSrcAny_Type(TruthValue):
    """Custom type hh3cAclIPAclBasicSrcAny based on TruthValue"""
    defaultValue = 1


_Hh3cAclIPAclBasicSrcAny_Type.__name__ = "TruthValue"
_Hh3cAclIPAclBasicSrcAny_Object = MibTableColumn
hh3cAclIPAclBasicSrcAny = _Hh3cAclIPAclBasicSrcAny_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 2, 2, 2, 1, 7),
    _Hh3cAclIPAclBasicSrcAny_Type()
)
hh3cAclIPAclBasicSrcAny.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cAclIPAclBasicSrcAny.setStatus("current")
_Hh3cAclIPAclBasicSrcWild_Type = IpAddress
_Hh3cAclIPAclBasicSrcWild_Object = MibTableColumn
hh3cAclIPAclBasicSrcWild = _Hh3cAclIPAclBasicSrcWild_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 2, 2, 2, 1, 8),
    _Hh3cAclIPAclBasicSrcWild_Type()
)
hh3cAclIPAclBasicSrcWild.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cAclIPAclBasicSrcWild.setStatus("current")


class _Hh3cAclIPAclBasicTimeRangeName_Type(OctetString):
    """Custom type hh3cAclIPAclBasicTimeRangeName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Hh3cAclIPAclBasicTimeRangeName_Type.__name__ = "OctetString"
_Hh3cAclIPAclBasicTimeRangeName_Object = MibTableColumn
hh3cAclIPAclBasicTimeRangeName = _Hh3cAclIPAclBasicTimeRangeName_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 2, 2, 2, 1, 9),
    _Hh3cAclIPAclBasicTimeRangeName_Type()
)
hh3cAclIPAclBasicTimeRangeName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cAclIPAclBasicTimeRangeName.setStatus("current")


class _Hh3cAclIPAclBasicFragmentFlag_Type(FragmentFlag):
    """Custom type hh3cAclIPAclBasicFragmentFlag based on FragmentFlag"""
    defaultValue = 0


_Hh3cAclIPAclBasicFragmentFlag_Type.__name__ = "FragmentFlag"
_Hh3cAclIPAclBasicFragmentFlag_Object = MibTableColumn
hh3cAclIPAclBasicFragmentFlag = _Hh3cAclIPAclBasicFragmentFlag_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 2, 2, 2, 1, 10),
    _Hh3cAclIPAclBasicFragmentFlag_Type()
)
hh3cAclIPAclBasicFragmentFlag.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cAclIPAclBasicFragmentFlag.setStatus("current")


class _Hh3cAclIPAclBasicLog_Type(TruthValue):
    """Custom type hh3cAclIPAclBasicLog based on TruthValue"""
    defaultValue = 2


_Hh3cAclIPAclBasicLog_Type.__name__ = "TruthValue"
_Hh3cAclIPAclBasicLog_Object = MibTableColumn
hh3cAclIPAclBasicLog = _Hh3cAclIPAclBasicLog_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 2, 2, 2, 1, 11),
    _Hh3cAclIPAclBasicLog_Type()
)
hh3cAclIPAclBasicLog.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cAclIPAclBasicLog.setStatus("current")
_Hh3cAclIPAclBasicCount_Type = Unsigned32
_Hh3cAclIPAclBasicCount_Object = MibTableColumn
hh3cAclIPAclBasicCount = _Hh3cAclIPAclBasicCount_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 2, 2, 2, 1, 12),
    _Hh3cAclIPAclBasicCount_Type()
)
hh3cAclIPAclBasicCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cAclIPAclBasicCount.setStatus("current")


class _Hh3cAclIPAclBasicCountClear_Type(CounterClear):
    """Custom type hh3cAclIPAclBasicCountClear based on CounterClear"""
    defaultValue = 2


_Hh3cAclIPAclBasicCountClear_Type.__name__ = "CounterClear"
_Hh3cAclIPAclBasicCountClear_Object = MibTableColumn
hh3cAclIPAclBasicCountClear = _Hh3cAclIPAclBasicCountClear_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 2, 2, 2, 1, 13),
    _Hh3cAclIPAclBasicCountClear_Type()
)
hh3cAclIPAclBasicCountClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cAclIPAclBasicCountClear.setStatus("current")


class _Hh3cAclIPAclBasicEnable_Type(TruthValue):
    """Custom type hh3cAclIPAclBasicEnable based on TruthValue"""
    defaultValue = 2


_Hh3cAclIPAclBasicEnable_Type.__name__ = "TruthValue"
_Hh3cAclIPAclBasicEnable_Object = MibTableColumn
hh3cAclIPAclBasicEnable = _Hh3cAclIPAclBasicEnable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 2, 2, 2, 1, 14),
    _Hh3cAclIPAclBasicEnable_Type()
)
hh3cAclIPAclBasicEnable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cAclIPAclBasicEnable.setStatus("current")


class _Hh3cAclIPAclBasicVpnInstanceName_Type(OctetString):
    """Custom type hh3cAclIPAclBasicVpnInstanceName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Hh3cAclIPAclBasicVpnInstanceName_Type.__name__ = "OctetString"
_Hh3cAclIPAclBasicVpnInstanceName_Object = MibTableColumn
hh3cAclIPAclBasicVpnInstanceName = _Hh3cAclIPAclBasicVpnInstanceName_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 2, 2, 2, 1, 15),
    _Hh3cAclIPAclBasicVpnInstanceName_Type()
)
hh3cAclIPAclBasicVpnInstanceName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cAclIPAclBasicVpnInstanceName.setStatus("current")


class _Hh3cAclIPAclBasicComment_Type(OctetString):
    """Custom type hh3cAclIPAclBasicComment based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_Hh3cAclIPAclBasicComment_Type.__name__ = "OctetString"
_Hh3cAclIPAclBasicComment_Object = MibTableColumn
hh3cAclIPAclBasicComment = _Hh3cAclIPAclBasicComment_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 2, 2, 2, 1, 16),
    _Hh3cAclIPAclBasicComment_Type()
)
hh3cAclIPAclBasicComment.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cAclIPAclBasicComment.setStatus("current")


class _Hh3cAclIPAclBasicCounting_Type(TruthValue):
    """Custom type hh3cAclIPAclBasicCounting based on TruthValue"""
    defaultValue = 2


_Hh3cAclIPAclBasicCounting_Type.__name__ = "TruthValue"
_Hh3cAclIPAclBasicCounting_Object = MibTableColumn
hh3cAclIPAclBasicCounting = _Hh3cAclIPAclBasicCounting_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 2, 2, 2, 1, 17),
    _Hh3cAclIPAclBasicCounting_Type()
)
hh3cAclIPAclBasicCounting.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cAclIPAclBasicCounting.setStatus("current")


class _Hh3cAclIPAclBasicRouteTypeAny_Type(TruthValue):
    """Custom type hh3cAclIPAclBasicRouteTypeAny based on TruthValue"""
    defaultValue = 2


_Hh3cAclIPAclBasicRouteTypeAny_Type.__name__ = "TruthValue"
_Hh3cAclIPAclBasicRouteTypeAny_Object = MibTableColumn
hh3cAclIPAclBasicRouteTypeAny = _Hh3cAclIPAclBasicRouteTypeAny_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 2, 2, 2, 1, 18),
    _Hh3cAclIPAclBasicRouteTypeAny_Type()
)
hh3cAclIPAclBasicRouteTypeAny.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cAclIPAclBasicRouteTypeAny.setStatus("current")


class _Hh3cAclIPAclBasicRouteTypeValue_Type(Integer32):
    """Custom type hh3cAclIPAclBasicRouteTypeValue based on Integer32"""
    defaultValue = 65535

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
        ValueRangeConstraint(65535, 65535),
    )


_Hh3cAclIPAclBasicRouteTypeValue_Type.__name__ = "Integer32"
_Hh3cAclIPAclBasicRouteTypeValue_Object = MibTableColumn
hh3cAclIPAclBasicRouteTypeValue = _Hh3cAclIPAclBasicRouteTypeValue_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 2, 2, 2, 1, 19),
    _Hh3cAclIPAclBasicRouteTypeValue_Type()
)
hh3cAclIPAclBasicRouteTypeValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cAclIPAclBasicRouteTypeValue.setStatus("current")
_Hh3cAclIPAclAdvancedTable_Object = MibTable
hh3cAclIPAclAdvancedTable = _Hh3cAclIPAclAdvancedTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 2, 2, 3)
)
if mibBuilder.loadTexts:
    hh3cAclIPAclAdvancedTable.setStatus("current")
_Hh3cAclIPAclAdvancedEntry_Object = MibTableRow
hh3cAclIPAclAdvancedEntry = _Hh3cAclIPAclAdvancedEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 2, 2, 3, 1)
)
hh3cAclIPAclAdvancedEntry.setIndexNames(
    (0, "HH3C-ACL-MIB", "hh3cAclNumberGroupType"),
    (0, "HH3C-ACL-MIB", "hh3cAclNumberGroupIndex"),
    (0, "HH3C-ACL-MIB", "hh3cAclIPAclAdvancedRuleIndex"),
)
if mibBuilder.loadTexts:
    hh3cAclIPAclAdvancedEntry.setStatus("current")


class _Hh3cAclIPAclAdvancedRuleIndex_Type(Integer32):
    """Custom type hh3cAclIPAclAdvancedRuleIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65534),
    )


_Hh3cAclIPAclAdvancedRuleIndex_Type.__name__ = "Integer32"
_Hh3cAclIPAclAdvancedRuleIndex_Object = MibTableColumn
hh3cAclIPAclAdvancedRuleIndex = _Hh3cAclIPAclAdvancedRuleIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 2, 2, 3, 1, 1),
    _Hh3cAclIPAclAdvancedRuleIndex_Type()
)
hh3cAclIPAclAdvancedRuleIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cAclIPAclAdvancedRuleIndex.setStatus("current")
_Hh3cAclIPAclAdvancedRowStatus_Type = RowStatus
_Hh3cAclIPAclAdvancedRowStatus_Object = MibTableColumn
hh3cAclIPAclAdvancedRowStatus = _Hh3cAclIPAclAdvancedRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 2, 2, 3, 1, 2),
    _Hh3cAclIPAclAdvancedRowStatus_Type()
)
hh3cAclIPAclAdvancedRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cAclIPAclAdvancedRowStatus.setStatus("current")
_Hh3cAclIPAclAdvancedAct_Type = RuleAction
_Hh3cAclIPAclAdvancedAct_Object = MibTableColumn
hh3cAclIPAclAdvancedAct = _Hh3cAclIPAclAdvancedAct_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 2, 2, 3, 1, 3),
    _Hh3cAclIPAclAdvancedAct_Type()
)
hh3cAclIPAclAdvancedAct.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cAclIPAclAdvancedAct.setStatus("current")


class _Hh3cAclIPAclAdvancedProtocol_Type(Integer32):
    """Custom type hh3cAclIPAclAdvancedProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_Hh3cAclIPAclAdvancedProtocol_Type.__name__ = "Integer32"
_Hh3cAclIPAclAdvancedProtocol_Object = MibTableColumn
hh3cAclIPAclAdvancedProtocol = _Hh3cAclIPAclAdvancedProtocol_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 2, 2, 3, 1, 4),
    _Hh3cAclIPAclAdvancedProtocol_Type()
)
hh3cAclIPAclAdvancedProtocol.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cAclIPAclAdvancedProtocol.setStatus("current")


class _Hh3cAclIPAclAdvancedAddrFlag_Type(AddressFlag):
    """Custom type hh3cAclIPAclAdvancedAddrFlag based on AddressFlag"""
    defaultValue = 0


_Hh3cAclIPAclAdvancedAddrFlag_Type.__name__ = "AddressFlag"
_Hh3cAclIPAclAdvancedAddrFlag_Object = MibTableColumn
hh3cAclIPAclAdvancedAddrFlag = _Hh3cAclIPAclAdvancedAddrFlag_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 2, 2, 3, 1, 5),
    _Hh3cAclIPAclAdvancedAddrFlag_Type()
)
hh3cAclIPAclAdvancedAddrFlag.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cAclIPAclAdvancedAddrFlag.setStatus("current")
_Hh3cAclIPAclAdvancedSrcAddrType_Type = InetAddressType
_Hh3cAclIPAclAdvancedSrcAddrType_Object = MibTableColumn
hh3cAclIPAclAdvancedSrcAddrType = _Hh3cAclIPAclAdvancedSrcAddrType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 2, 2, 3, 1, 6),
    _Hh3cAclIPAclAdvancedSrcAddrType_Type()
)
hh3cAclIPAclAdvancedSrcAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cAclIPAclAdvancedSrcAddrType.setStatus("current")
_Hh3cAclIPAclAdvancedSrcAddr_Type = InetAddress
_Hh3cAclIPAclAdvancedSrcAddr_Object = MibTableColumn
hh3cAclIPAclAdvancedSrcAddr = _Hh3cAclIPAclAdvancedSrcAddr_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 2, 2, 3, 1, 7),
    _Hh3cAclIPAclAdvancedSrcAddr_Type()
)
hh3cAclIPAclAdvancedSrcAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cAclIPAclAdvancedSrcAddr.setStatus("current")
_Hh3cAclIPAclAdvancedSrcPrefix_Type = InetAddressPrefixLength
_Hh3cAclIPAclAdvancedSrcPrefix_Object = MibTableColumn
hh3cAclIPAclAdvancedSrcPrefix = _Hh3cAclIPAclAdvancedSrcPrefix_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 2, 2, 3, 1, 8),
    _Hh3cAclIPAclAdvancedSrcPrefix_Type()
)
hh3cAclIPAclAdvancedSrcPrefix.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cAclIPAclAdvancedSrcPrefix.setStatus("current")


class _Hh3cAclIPAclAdvancedSrcAny_Type(TruthValue):
    """Custom type hh3cAclIPAclAdvancedSrcAny based on TruthValue"""
    defaultValue = 1


_Hh3cAclIPAclAdvancedSrcAny_Type.__name__ = "TruthValue"
_Hh3cAclIPAclAdvancedSrcAny_Object = MibTableColumn
hh3cAclIPAclAdvancedSrcAny = _Hh3cAclIPAclAdvancedSrcAny_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 2, 2, 3, 1, 9),
    _Hh3cAclIPAclAdvancedSrcAny_Type()
)
hh3cAclIPAclAdvancedSrcAny.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cAclIPAclAdvancedSrcAny.setStatus("current")
_Hh3cAclIPAclAdvancedSrcWild_Type = IpAddress
_Hh3cAclIPAclAdvancedSrcWild_Object = MibTableColumn
hh3cAclIPAclAdvancedSrcWild = _Hh3cAclIPAclAdvancedSrcWild_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 2, 2, 3, 1, 10),
    _Hh3cAclIPAclAdvancedSrcWild_Type()
)
hh3cAclIPAclAdvancedSrcWild.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cAclIPAclAdvancedSrcWild.setStatus("current")


class _Hh3cAclIPAclAdvancedSrcOp_Type(PortOp):
    """Custom type hh3cAclIPAclAdvancedSrcOp based on PortOp"""
    defaultValue = 0


_Hh3cAclIPAclAdvancedSrcOp_Type.__name__ = "PortOp"
_Hh3cAclIPAclAdvancedSrcOp_Object = MibTableColumn
hh3cAclIPAclAdvancedSrcOp = _Hh3cAclIPAclAdvancedSrcOp_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 2, 2, 3, 1, 11),
    _Hh3cAclIPAclAdvancedSrcOp_Type()
)
hh3cAclIPAclAdvancedSrcOp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cAclIPAclAdvancedSrcOp.setStatus("current")


class _Hh3cAclIPAclAdvancedSrcPort1_Type(Integer32):
    """Custom type hh3cAclIPAclAdvancedSrcPort1 based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Hh3cAclIPAclAdvancedSrcPort1_Type.__name__ = "Integer32"
_Hh3cAclIPAclAdvancedSrcPort1_Object = MibTableColumn
hh3cAclIPAclAdvancedSrcPort1 = _Hh3cAclIPAclAdvancedSrcPort1_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 2, 2, 3, 1, 12),
    _Hh3cAclIPAclAdvancedSrcPort1_Type()
)
hh3cAclIPAclAdvancedSrcPort1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cAclIPAclAdvancedSrcPort1.setStatus("current")


class _Hh3cAclIPAclAdvancedSrcPort2_Type(Integer32):
    """Custom type hh3cAclIPAclAdvancedSrcPort2 based on Integer32"""
    defaultValue = 65535

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Hh3cAclIPAclAdvancedSrcPort2_Type.__name__ = "Integer32"
_Hh3cAclIPAclAdvancedSrcPort2_Object = MibTableColumn
hh3cAclIPAclAdvancedSrcPort2 = _Hh3cAclIPAclAdvancedSrcPort2_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 2, 2, 3, 1, 13),
    _Hh3cAclIPAclAdvancedSrcPort2_Type()
)
hh3cAclIPAclAdvancedSrcPort2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cAclIPAclAdvancedSrcPort2.setStatus("current")
_Hh3cAclIPAclAdvancedDestAddrType_Type = InetAddressType
_Hh3cAclIPAclAdvancedDestAddrType_Object = MibTableColumn
hh3cAclIPAclAdvancedDestAddrType = _Hh3cAclIPAclAdvancedDestAddrType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 2, 2, 3, 1, 14),
    _Hh3cAclIPAclAdvancedDestAddrType_Type()
)
hh3cAclIPAclAdvancedDestAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cAclIPAclAdvancedDestAddrType.setStatus("current")
_Hh3cAclIPAclAdvancedDestAddr_Type = InetAddress
_Hh3cAclIPAclAdvancedDestAddr_Object = MibTableColumn
hh3cAclIPAclAdvancedDestAddr = _Hh3cAclIPAclAdvancedDestAddr_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 2, 2, 3, 1, 15),
    _Hh3cAclIPAclAdvancedDestAddr_Type()
)
hh3cAclIPAclAdvancedDestAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cAclIPAclAdvancedDestAddr.setStatus("current")
_Hh3cAclIPAclAdvancedDestPrefix_Type = InetAddressPrefixLength
_Hh3cAclIPAclAdvancedDestPrefix_Object = MibTableColumn
hh3cAclIPAclAdvancedDestPrefix = _Hh3cAclIPAclAdvancedDestPrefix_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 2, 2, 3, 1, 16),
    _Hh3cAclIPAclAdvancedDestPrefix_Type()
)
hh3cAclIPAclAdvancedDestPrefix.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cAclIPAclAdvancedDestPrefix.setStatus("current")


class _Hh3cAclIPAclAdvancedDestAny_Type(TruthValue):
    """Custom type hh3cAclIPAclAdvancedDestAny based on TruthValue"""
    defaultValue = 1


_Hh3cAclIPAclAdvancedDestAny_Type.__name__ = "TruthValue"
_Hh3cAclIPAclAdvancedDestAny_Object = MibTableColumn
hh3cAclIPAclAdvancedDestAny = _Hh3cAclIPAclAdvancedDestAny_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 2, 2, 3, 1, 17),
    _Hh3cAclIPAclAdvancedDestAny_Type()
)
hh3cAclIPAclAdvancedDestAny.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cAclIPAclAdvancedDestAny.setStatus("current")
_Hh3cAclIPAclAdvancedDestWild_Type = IpAddress
_Hh3cAclIPAclAdvancedDestWild_Object = MibTableColumn
hh3cAclIPAclAdvancedDestWild = _Hh3cAclIPAclAdvancedDestWild_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 2, 2, 3, 1, 18),
    _Hh3cAclIPAclAdvancedDestWild_Type()
)
hh3cAclIPAclAdvancedDestWild.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cAclIPAclAdvancedDestWild.setStatus("current")


class _Hh3cAclIPAclAdvancedDestOp_Type(PortOp):
    """Custom type hh3cAclIPAclAdvancedDestOp based on PortOp"""
    defaultValue = 0


_Hh3cAclIPAclAdvancedDestOp_Type.__name__ = "PortOp"
_Hh3cAclIPAclAdvancedDestOp_Object = MibTableColumn
hh3cAclIPAclAdvancedDestOp = _Hh3cAclIPAclAdvancedDestOp_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 2, 2, 3, 1, 19),
    _Hh3cAclIPAclAdvancedDestOp_Type()
)
hh3cAclIPAclAdvancedDestOp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cAclIPAclAdvancedDestOp.setStatus("current")


class _Hh3cAclIPAclAdvancedDestPort1_Type(Integer32):
    """Custom type hh3cAclIPAclAdvancedDestPort1 based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Hh3cAclIPAclAdvancedDestPort1_Type.__name__ = "Integer32"
_Hh3cAclIPAclAdvancedDestPort1_Object = MibTableColumn
hh3cAclIPAclAdvancedDestPort1 = _Hh3cAclIPAclAdvancedDestPort1_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 2, 2, 3, 1, 20),
    _Hh3cAclIPAclAdvancedDestPort1_Type()
)
hh3cAclIPAclAdvancedDestPort1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cAclIPAclAdvancedDestPort1.setStatus("current")


class _Hh3cAclIPAclAdvancedDestPort2_Type(Integer32):
    """Custom type hh3cAclIPAclAdvancedDestPort2 based on Integer32"""
    defaultValue = 65535

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Hh3cAclIPAclAdvancedDestPort2_Type.__name__ = "Integer32"
_Hh3cAclIPAclAdvancedDestPort2_Object = MibTableColumn
hh3cAclIPAclAdvancedDestPort2 = _Hh3cAclIPAclAdvancedDestPort2_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 2, 2, 3, 1, 21),
    _Hh3cAclIPAclAdvancedDestPort2_Type()
)
hh3cAclIPAclAdvancedDestPort2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cAclIPAclAdvancedDestPort2.setStatus("current")


class _Hh3cAclIPAclAdvancedIcmpType_Type(Integer32):
    """Custom type hh3cAclIPAclAdvancedIcmpType based on Integer32"""
    defaultValue = 65535

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
        ValueRangeConstraint(65535, 65535),
    )


_Hh3cAclIPAclAdvancedIcmpType_Type.__name__ = "Integer32"
_Hh3cAclIPAclAdvancedIcmpType_Object = MibTableColumn
hh3cAclIPAclAdvancedIcmpType = _Hh3cAclIPAclAdvancedIcmpType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 2, 2, 3, 1, 22),
    _Hh3cAclIPAclAdvancedIcmpType_Type()
)
hh3cAclIPAclAdvancedIcmpType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cAclIPAclAdvancedIcmpType.setStatus("current")


class _Hh3cAclIPAclAdvancedIcmpCode_Type(Integer32):
    """Custom type hh3cAclIPAclAdvancedIcmpCode based on Integer32"""
    defaultValue = 65535

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
        ValueRangeConstraint(65535, 65535),
    )


_Hh3cAclIPAclAdvancedIcmpCode_Type.__name__ = "Integer32"
_Hh3cAclIPAclAdvancedIcmpCode_Object = MibTableColumn
hh3cAclIPAclAdvancedIcmpCode = _Hh3cAclIPAclAdvancedIcmpCode_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 2, 2, 3, 1, 23),
    _Hh3cAclIPAclAdvancedIcmpCode_Type()
)
hh3cAclIPAclAdvancedIcmpCode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cAclIPAclAdvancedIcmpCode.setStatus("current")


class _Hh3cAclIPAclAdvancedPrecedence_Type(Integer32):
    """Custom type hh3cAclIPAclAdvancedPrecedence based on Integer32"""
    defaultValue = 255

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
        ValueRangeConstraint(255, 255),
    )


_Hh3cAclIPAclAdvancedPrecedence_Type.__name__ = "Integer32"
_Hh3cAclIPAclAdvancedPrecedence_Object = MibTableColumn
hh3cAclIPAclAdvancedPrecedence = _Hh3cAclIPAclAdvancedPrecedence_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 2, 2, 3, 1, 24),
    _Hh3cAclIPAclAdvancedPrecedence_Type()
)
hh3cAclIPAclAdvancedPrecedence.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cAclIPAclAdvancedPrecedence.setStatus("current")


class _Hh3cAclIPAclAdvancedTos_Type(Integer32):
    """Custom type hh3cAclIPAclAdvancedTos based on Integer32"""
    defaultValue = 255

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
        ValueRangeConstraint(255, 255),
    )


_Hh3cAclIPAclAdvancedTos_Type.__name__ = "Integer32"
_Hh3cAclIPAclAdvancedTos_Object = MibTableColumn
hh3cAclIPAclAdvancedTos = _Hh3cAclIPAclAdvancedTos_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 2, 2, 3, 1, 25),
    _Hh3cAclIPAclAdvancedTos_Type()
)
hh3cAclIPAclAdvancedTos.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cAclIPAclAdvancedTos.setStatus("current")


class _Hh3cAclIPAclAdvancedDscp_Type(DSCPValue):
    """Custom type hh3cAclIPAclAdvancedDscp based on DSCPValue"""
    defaultValue = 255


_Hh3cAclIPAclAdvancedDscp_Type.__name__ = "DSCPValue"
_Hh3cAclIPAclAdvancedDscp_Object = MibTableColumn
hh3cAclIPAclAdvancedDscp = _Hh3cAclIPAclAdvancedDscp_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 2, 2, 3, 1, 26),
    _Hh3cAclIPAclAdvancedDscp_Type()
)
hh3cAclIPAclAdvancedDscp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cAclIPAclAdvancedDscp.setStatus("current")


class _Hh3cAclIPAclAdvancedTimeRangeName_Type(OctetString):
    """Custom type hh3cAclIPAclAdvancedTimeRangeName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Hh3cAclIPAclAdvancedTimeRangeName_Type.__name__ = "OctetString"
_Hh3cAclIPAclAdvancedTimeRangeName_Object = MibTableColumn
hh3cAclIPAclAdvancedTimeRangeName = _Hh3cAclIPAclAdvancedTimeRangeName_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 2, 2, 3, 1, 27),
    _Hh3cAclIPAclAdvancedTimeRangeName_Type()
)
hh3cAclIPAclAdvancedTimeRangeName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cAclIPAclAdvancedTimeRangeName.setStatus("current")


class _Hh3cAclIPAclAdvancedTCPFlag_Type(TCPFlag):
    """Custom type hh3cAclIPAclAdvancedTCPFlag based on TCPFlag"""
    defaultValue = 0


_Hh3cAclIPAclAdvancedTCPFlag_Type.__name__ = "TCPFlag"
_Hh3cAclIPAclAdvancedTCPFlag_Object = MibTableColumn
hh3cAclIPAclAdvancedTCPFlag = _Hh3cAclIPAclAdvancedTCPFlag_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 2, 2, 3, 1, 28),
    _Hh3cAclIPAclAdvancedTCPFlag_Type()
)
hh3cAclIPAclAdvancedTCPFlag.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cAclIPAclAdvancedTCPFlag.setStatus("current")


class _Hh3cAclIPAclAdvancedFragmentFlag_Type(FragmentFlag):
    """Custom type hh3cAclIPAclAdvancedFragmentFlag based on FragmentFlag"""
    defaultValue = 0


_Hh3cAclIPAclAdvancedFragmentFlag_Type.__name__ = "FragmentFlag"
_Hh3cAclIPAclAdvancedFragmentFlag_Object = MibTableColumn
hh3cAclIPAclAdvancedFragmentFlag = _Hh3cAclIPAclAdvancedFragmentFlag_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 2, 2, 3, 1, 29),
    _Hh3cAclIPAclAdvancedFragmentFlag_Type()
)
hh3cAclIPAclAdvancedFragmentFlag.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cAclIPAclAdvancedFragmentFlag.setStatus("current")


class _Hh3cAclIPAclAdvancedLog_Type(TruthValue):
    """Custom type hh3cAclIPAclAdvancedLog based on TruthValue"""
    defaultValue = 2


_Hh3cAclIPAclAdvancedLog_Type.__name__ = "TruthValue"
_Hh3cAclIPAclAdvancedLog_Object = MibTableColumn
hh3cAclIPAclAdvancedLog = _Hh3cAclIPAclAdvancedLog_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 2, 2, 3, 1, 30),
    _Hh3cAclIPAclAdvancedLog_Type()
)
hh3cAclIPAclAdvancedLog.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cAclIPAclAdvancedLog.setStatus("current")
_Hh3cAclIPAclAdvancedCount_Type = Unsigned32
_Hh3cAclIPAclAdvancedCount_Object = MibTableColumn
hh3cAclIPAclAdvancedCount = _Hh3cAclIPAclAdvancedCount_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 2, 2, 3, 1, 31),
    _Hh3cAclIPAclAdvancedCount_Type()
)
hh3cAclIPAclAdvancedCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cAclIPAclAdvancedCount.setStatus("current")


class _Hh3cAclIPAclAdvancedCountClear_Type(CounterClear):
    """Custom type hh3cAclIPAclAdvancedCountClear based on CounterClear"""
    defaultValue = 2


_Hh3cAclIPAclAdvancedCountClear_Type.__name__ = "CounterClear"
_Hh3cAclIPAclAdvancedCountClear_Object = MibTableColumn
hh3cAclIPAclAdvancedCountClear = _Hh3cAclIPAclAdvancedCountClear_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 2, 2, 3, 1, 32),
    _Hh3cAclIPAclAdvancedCountClear_Type()
)
hh3cAclIPAclAdvancedCountClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cAclIPAclAdvancedCountClear.setStatus("current")


class _Hh3cAclIPAclAdvancedEnable_Type(TruthValue):
    """Custom type hh3cAclIPAclAdvancedEnable based on TruthValue"""
    defaultValue = 2


_Hh3cAclIPAclAdvancedEnable_Type.__name__ = "TruthValue"
_Hh3cAclIPAclAdvancedEnable_Object = MibTableColumn
hh3cAclIPAclAdvancedEnable = _Hh3cAclIPAclAdvancedEnable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 2, 2, 3, 1, 33),
    _Hh3cAclIPAclAdvancedEnable_Type()
)
hh3cAclIPAclAdvancedEnable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cAclIPAclAdvancedEnable.setStatus("current")


class _Hh3cAclIPAclAdvancedVpnInstanceName_Type(OctetString):
    """Custom type hh3cAclIPAclAdvancedVpnInstanceName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Hh3cAclIPAclAdvancedVpnInstanceName_Type.__name__ = "OctetString"
_Hh3cAclIPAclAdvancedVpnInstanceName_Object = MibTableColumn
hh3cAclIPAclAdvancedVpnInstanceName = _Hh3cAclIPAclAdvancedVpnInstanceName_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 2, 2, 3, 1, 34),
    _Hh3cAclIPAclAdvancedVpnInstanceName_Type()
)
hh3cAclIPAclAdvancedVpnInstanceName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cAclIPAclAdvancedVpnInstanceName.setStatus("current")


class _Hh3cAclIPAclAdvancedComment_Type(OctetString):
    """Custom type hh3cAclIPAclAdvancedComment based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_Hh3cAclIPAclAdvancedComment_Type.__name__ = "OctetString"
_Hh3cAclIPAclAdvancedComment_Object = MibTableColumn
hh3cAclIPAclAdvancedComment = _Hh3cAclIPAclAdvancedComment_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 2, 2, 3, 1, 35),
    _Hh3cAclIPAclAdvancedComment_Type()
)
hh3cAclIPAclAdvancedComment.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cAclIPAclAdvancedComment.setStatus("current")
_Hh3cAclIPAclAdvancedReflective_Type = TruthValue
_Hh3cAclIPAclAdvancedReflective_Object = MibTableColumn
hh3cAclIPAclAdvancedReflective = _Hh3cAclIPAclAdvancedReflective_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 2, 2, 3, 1, 36),
    _Hh3cAclIPAclAdvancedReflective_Type()
)
hh3cAclIPAclAdvancedReflective.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cAclIPAclAdvancedReflective.setStatus("current")


class _Hh3cAclIPAclAdvancedCounting_Type(TruthValue):
    """Custom type hh3cAclIPAclAdvancedCounting based on TruthValue"""
    defaultValue = 2


_Hh3cAclIPAclAdvancedCounting_Type.__name__ = "TruthValue"
_Hh3cAclIPAclAdvancedCounting_Object = MibTableColumn
hh3cAclIPAclAdvancedCounting = _Hh3cAclIPAclAdvancedCounting_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 2, 2, 3, 1, 37),
    _Hh3cAclIPAclAdvancedCounting_Type()
)
hh3cAclIPAclAdvancedCounting.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cAclIPAclAdvancedCounting.setStatus("current")


class _Hh3cAclIPAclAdvancedTCPFlagMask_Type(Bits):
    """Custom type hh3cAclIPAclAdvancedTCPFlagMask based on Bits"""
    defaultBinValue = "0"

    namedValues = NamedValues(
        *(("tcpack", 0),
          ("tcpfin", 1),
          ("tcppsh", 2),
          ("tcprst", 3),
          ("tcpsyn", 4),
          ("tcpurg", 5))
    )

_Hh3cAclIPAclAdvancedTCPFlagMask_Type.__name__ = "Bits"
_Hh3cAclIPAclAdvancedTCPFlagMask_Object = MibTableColumn
hh3cAclIPAclAdvancedTCPFlagMask = _Hh3cAclIPAclAdvancedTCPFlagMask_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 2, 2, 3, 1, 38),
    _Hh3cAclIPAclAdvancedTCPFlagMask_Type()
)
hh3cAclIPAclAdvancedTCPFlagMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cAclIPAclAdvancedTCPFlagMask.setStatus("current")


class _Hh3cAclIPAclAdvancedTCPFlagValue_Type(Bits):
    """Custom type hh3cAclIPAclAdvancedTCPFlagValue based on Bits"""
    defaultBinValue = "0"

    namedValues = NamedValues(
        *(("tcpack", 0),
          ("tcpfin", 1),
          ("tcppsh", 2),
          ("tcprst", 3),
          ("tcpsyn", 4),
          ("tcpurg", 5))
    )

_Hh3cAclIPAclAdvancedTCPFlagValue_Type.__name__ = "Bits"
_Hh3cAclIPAclAdvancedTCPFlagValue_Object = MibTableColumn
hh3cAclIPAclAdvancedTCPFlagValue = _Hh3cAclIPAclAdvancedTCPFlagValue_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 2, 2, 3, 1, 39),
    _Hh3cAclIPAclAdvancedTCPFlagValue_Type()
)
hh3cAclIPAclAdvancedTCPFlagValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cAclIPAclAdvancedTCPFlagValue.setStatus("current")


class _Hh3cAclIPAclAdvancedRouteTypeAny_Type(TruthValue):
    """Custom type hh3cAclIPAclAdvancedRouteTypeAny based on TruthValue"""
    defaultValue = 2


_Hh3cAclIPAclAdvancedRouteTypeAny_Type.__name__ = "TruthValue"
_Hh3cAclIPAclAdvancedRouteTypeAny_Object = MibTableColumn
hh3cAclIPAclAdvancedRouteTypeAny = _Hh3cAclIPAclAdvancedRouteTypeAny_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 2, 2, 3, 1, 40),
    _Hh3cAclIPAclAdvancedRouteTypeAny_Type()
)
hh3cAclIPAclAdvancedRouteTypeAny.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cAclIPAclAdvancedRouteTypeAny.setStatus("current")


class _Hh3cAclIPAclAdvancedRouteTypeValue_Type(Integer32):
    """Custom type hh3cAclIPAclAdvancedRouteTypeValue based on Integer32"""
    defaultValue = 65535

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
        ValueRangeConstraint(65535, 65535),
    )


_Hh3cAclIPAclAdvancedRouteTypeValue_Type.__name__ = "Integer32"
_Hh3cAclIPAclAdvancedRouteTypeValue_Object = MibTableColumn
hh3cAclIPAclAdvancedRouteTypeValue = _Hh3cAclIPAclAdvancedRouteTypeValue_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 2, 2, 3, 1, 41),
    _Hh3cAclIPAclAdvancedRouteTypeValue_Type()
)
hh3cAclIPAclAdvancedRouteTypeValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cAclIPAclAdvancedRouteTypeValue.setStatus("current")


class _Hh3cAclIPAclAdvancedFlowLabel_Type(Unsigned32):
    """Custom type hh3cAclIPAclAdvancedFlowLabel based on Unsigned32"""
    defaultValue = 4294967295

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1048575),
        ValueRangeConstraint(4294967295, 4294967295),
    )


_Hh3cAclIPAclAdvancedFlowLabel_Type.__name__ = "Unsigned32"
_Hh3cAclIPAclAdvancedFlowLabel_Object = MibTableColumn
hh3cAclIPAclAdvancedFlowLabel = _Hh3cAclIPAclAdvancedFlowLabel_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 2, 2, 3, 1, 42),
    _Hh3cAclIPAclAdvancedFlowLabel_Type()
)
hh3cAclIPAclAdvancedFlowLabel.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cAclIPAclAdvancedFlowLabel.setStatus("current")
_Hh3cAclIPAclAdvancedSrcSuffix_Type = Unsigned32
_Hh3cAclIPAclAdvancedSrcSuffix_Object = MibTableColumn
hh3cAclIPAclAdvancedSrcSuffix = _Hh3cAclIPAclAdvancedSrcSuffix_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 2, 2, 3, 1, 43),
    _Hh3cAclIPAclAdvancedSrcSuffix_Type()
)
hh3cAclIPAclAdvancedSrcSuffix.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cAclIPAclAdvancedSrcSuffix.setStatus("current")
_Hh3cAclIPAclAdvancedDestSuffix_Type = Unsigned32
_Hh3cAclIPAclAdvancedDestSuffix_Object = MibTableColumn
hh3cAclIPAclAdvancedDestSuffix = _Hh3cAclIPAclAdvancedDestSuffix_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 2, 2, 3, 1, 44),
    _Hh3cAclIPAclAdvancedDestSuffix_Type()
)
hh3cAclIPAclAdvancedDestSuffix.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cAclIPAclAdvancedDestSuffix.setStatus("current")
_Hh3cAclIPAclNamedBscTable_Object = MibTable
hh3cAclIPAclNamedBscTable = _Hh3cAclIPAclNamedBscTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 2, 2, 4)
)
if mibBuilder.loadTexts:
    hh3cAclIPAclNamedBscTable.setStatus("current")
_Hh3cAclIPAclNamedBscEntry_Object = MibTableRow
hh3cAclIPAclNamedBscEntry = _Hh3cAclIPAclNamedBscEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 2, 2, 4, 1)
)
hh3cAclIPAclNamedBscEntry.setIndexNames(
    (0, "HH3C-ACL-MIB", "hh3cAclNumberGroupType"),
    (0, "HH3C-ACL-MIB", "hh3cAclNamedGroupName"),
    (0, "HH3C-ACL-MIB", "hh3cAclIPAclBasicRuleIndex"),
)
if mibBuilder.loadTexts:
    hh3cAclIPAclNamedBscEntry.setStatus("current")
_Hh3cAclIPAclNamedBscRowStatus_Type = RowStatus
_Hh3cAclIPAclNamedBscRowStatus_Object = MibTableColumn
hh3cAclIPAclNamedBscRowStatus = _Hh3cAclIPAclNamedBscRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 2, 2, 4, 1, 1),
    _Hh3cAclIPAclNamedBscRowStatus_Type()
)
hh3cAclIPAclNamedBscRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cAclIPAclNamedBscRowStatus.setStatus("current")
_Hh3cAclIPAclNamedBscAct_Type = RuleAction
_Hh3cAclIPAclNamedBscAct_Object = MibTableColumn
hh3cAclIPAclNamedBscAct = _Hh3cAclIPAclNamedBscAct_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 2, 2, 4, 1, 2),
    _Hh3cAclIPAclNamedBscAct_Type()
)
hh3cAclIPAclNamedBscAct.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cAclIPAclNamedBscAct.setStatus("current")
_Hh3cAclIPAclNamedBscSrcAddrType_Type = InetAddressType
_Hh3cAclIPAclNamedBscSrcAddrType_Object = MibTableColumn
hh3cAclIPAclNamedBscSrcAddrType = _Hh3cAclIPAclNamedBscSrcAddrType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 2, 2, 4, 1, 3),
    _Hh3cAclIPAclNamedBscSrcAddrType_Type()
)
hh3cAclIPAclNamedBscSrcAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cAclIPAclNamedBscSrcAddrType.setStatus("current")
_Hh3cAclIPAclNamedBscSrcAddr_Type = InetAddress
_Hh3cAclIPAclNamedBscSrcAddr_Object = MibTableColumn
hh3cAclIPAclNamedBscSrcAddr = _Hh3cAclIPAclNamedBscSrcAddr_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 2, 2, 4, 1, 4),
    _Hh3cAclIPAclNamedBscSrcAddr_Type()
)
hh3cAclIPAclNamedBscSrcAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cAclIPAclNamedBscSrcAddr.setStatus("current")
_Hh3cAclIPAclNamedBscSrcPrefix_Type = InetAddressPrefixLength
_Hh3cAclIPAclNamedBscSrcPrefix_Object = MibTableColumn
hh3cAclIPAclNamedBscSrcPrefix = _Hh3cAclIPAclNamedBscSrcPrefix_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 2, 2, 4, 1, 5),
    _Hh3cAclIPAclNamedBscSrcPrefix_Type()
)
hh3cAclIPAclNamedBscSrcPrefix.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cAclIPAclNamedBscSrcPrefix.setStatus("current")


class _Hh3cAclIPAclNamedBscSrcAny_Type(TruthValue):
    """Custom type hh3cAclIPAclNamedBscSrcAny based on TruthValue"""
    defaultValue = 1


_Hh3cAclIPAclNamedBscSrcAny_Type.__name__ = "TruthValue"
_Hh3cAclIPAclNamedBscSrcAny_Object = MibTableColumn
hh3cAclIPAclNamedBscSrcAny = _Hh3cAclIPAclNamedBscSrcAny_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 2, 2, 4, 1, 6),
    _Hh3cAclIPAclNamedBscSrcAny_Type()
)
hh3cAclIPAclNamedBscSrcAny.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cAclIPAclNamedBscSrcAny.setStatus("current")
_Hh3cAclIPAclNamedBscSrcWild_Type = IpAddress
_Hh3cAclIPAclNamedBscSrcWild_Object = MibTableColumn
hh3cAclIPAclNamedBscSrcWild = _Hh3cAclIPAclNamedBscSrcWild_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 2, 2, 4, 1, 7),
    _Hh3cAclIPAclNamedBscSrcWild_Type()
)
hh3cAclIPAclNamedBscSrcWild.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cAclIPAclNamedBscSrcWild.setStatus("current")


class _Hh3cAclIPAclNamedBscTRangeName_Type(OctetString):
    """Custom type hh3cAclIPAclNamedBscTRangeName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Hh3cAclIPAclNamedBscTRangeName_Type.__name__ = "OctetString"
_Hh3cAclIPAclNamedBscTRangeName_Object = MibTableColumn
hh3cAclIPAclNamedBscTRangeName = _Hh3cAclIPAclNamedBscTRangeName_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 2, 2, 4, 1, 8),
    _Hh3cAclIPAclNamedBscTRangeName_Type()
)
hh3cAclIPAclNamedBscTRangeName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cAclIPAclNamedBscTRangeName.setStatus("current")


class _Hh3cAclIPAclNamedBscFragmentFlag_Type(FragmentFlag):
    """Custom type hh3cAclIPAclNamedBscFragmentFlag based on FragmentFlag"""
    defaultValue = 0


_Hh3cAclIPAclNamedBscFragmentFlag_Type.__name__ = "FragmentFlag"
_Hh3cAclIPAclNamedBscFragmentFlag_Object = MibTableColumn
hh3cAclIPAclNamedBscFragmentFlag = _Hh3cAclIPAclNamedBscFragmentFlag_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 2, 2, 4, 1, 9),
    _Hh3cAclIPAclNamedBscFragmentFlag_Type()
)
hh3cAclIPAclNamedBscFragmentFlag.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cAclIPAclNamedBscFragmentFlag.setStatus("current")


class _Hh3cAclIPAclNamedBscLog_Type(TruthValue):
    """Custom type hh3cAclIPAclNamedBscLog based on TruthValue"""
    defaultValue = 2


_Hh3cAclIPAclNamedBscLog_Type.__name__ = "TruthValue"
_Hh3cAclIPAclNamedBscLog_Object = MibTableColumn
hh3cAclIPAclNamedBscLog = _Hh3cAclIPAclNamedBscLog_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 2, 2, 4, 1, 10),
    _Hh3cAclIPAclNamedBscLog_Type()
)
hh3cAclIPAclNamedBscLog.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cAclIPAclNamedBscLog.setStatus("current")
_Hh3cAclIPAclNamedBscCount_Type = Unsigned32
_Hh3cAclIPAclNamedBscCount_Object = MibTableColumn
hh3cAclIPAclNamedBscCount = _Hh3cAclIPAclNamedBscCount_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 2, 2, 4, 1, 11),
    _Hh3cAclIPAclNamedBscCount_Type()
)
hh3cAclIPAclNamedBscCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cAclIPAclNamedBscCount.setStatus("current")


class _Hh3cAclIPAclNamedBscCountClear_Type(CounterClear):
    """Custom type hh3cAclIPAclNamedBscCountClear based on CounterClear"""
    defaultValue = 2


_Hh3cAclIPAclNamedBscCountClear_Type.__name__ = "CounterClear"
_Hh3cAclIPAclNamedBscCountClear_Object = MibTableColumn
hh3cAclIPAclNamedBscCountClear = _Hh3cAclIPAclNamedBscCountClear_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 2, 2, 4, 1, 12),
    _Hh3cAclIPAclNamedBscCountClear_Type()
)
hh3cAclIPAclNamedBscCountClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cAclIPAclNamedBscCountClear.setStatus("current")


class _Hh3cAclIPAclNamedBscEnable_Type(TruthValue):
    """Custom type hh3cAclIPAclNamedBscEnable based on TruthValue"""
    defaultValue = 2


_Hh3cAclIPAclNamedBscEnable_Type.__name__ = "TruthValue"
_Hh3cAclIPAclNamedBscEnable_Object = MibTableColumn
hh3cAclIPAclNamedBscEnable = _Hh3cAclIPAclNamedBscEnable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 2, 2, 4, 1, 13),
    _Hh3cAclIPAclNamedBscEnable_Type()
)
hh3cAclIPAclNamedBscEnable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cAclIPAclNamedBscEnable.setStatus("current")


class _Hh3cAclIPAclNamedBscVpnInstName_Type(OctetString):
    """Custom type hh3cAclIPAclNamedBscVpnInstName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Hh3cAclIPAclNamedBscVpnInstName_Type.__name__ = "OctetString"
_Hh3cAclIPAclNamedBscVpnInstName_Object = MibTableColumn
hh3cAclIPAclNamedBscVpnInstName = _Hh3cAclIPAclNamedBscVpnInstName_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 2, 2, 4, 1, 14),
    _Hh3cAclIPAclNamedBscVpnInstName_Type()
)
hh3cAclIPAclNamedBscVpnInstName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cAclIPAclNamedBscVpnInstName.setStatus("current")


class _Hh3cAclIPAclNamedBscComment_Type(OctetString):
    """Custom type hh3cAclIPAclNamedBscComment based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_Hh3cAclIPAclNamedBscComment_Type.__name__ = "OctetString"
_Hh3cAclIPAclNamedBscComment_Object = MibTableColumn
hh3cAclIPAclNamedBscComment = _Hh3cAclIPAclNamedBscComment_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 2, 2, 4, 1, 15),
    _Hh3cAclIPAclNamedBscComment_Type()
)
hh3cAclIPAclNamedBscComment.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cAclIPAclNamedBscComment.setStatus("current")


class _Hh3cAclIPAclNamedBscCounting_Type(TruthValue):
    """Custom type hh3cAclIPAclNamedBscCounting based on TruthValue"""
    defaultValue = 2


_Hh3cAclIPAclNamedBscCounting_Type.__name__ = "TruthValue"
_Hh3cAclIPAclNamedBscCounting_Object = MibTableColumn
hh3cAclIPAclNamedBscCounting = _Hh3cAclIPAclNamedBscCounting_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 2, 2, 4, 1, 16),
    _Hh3cAclIPAclNamedBscCounting_Type()
)
hh3cAclIPAclNamedBscCounting.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cAclIPAclNamedBscCounting.setStatus("current")


class _Hh3cAclIPAclNamedBscRouteTypeAny_Type(TruthValue):
    """Custom type hh3cAclIPAclNamedBscRouteTypeAny based on TruthValue"""
    defaultValue = 2


_Hh3cAclIPAclNamedBscRouteTypeAny_Type.__name__ = "TruthValue"
_Hh3cAclIPAclNamedBscRouteTypeAny_Object = MibTableColumn
hh3cAclIPAclNamedBscRouteTypeAny = _Hh3cAclIPAclNamedBscRouteTypeAny_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 2, 2, 4, 1, 17),
    _Hh3cAclIPAclNamedBscRouteTypeAny_Type()
)
hh3cAclIPAclNamedBscRouteTypeAny.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cAclIPAclNamedBscRouteTypeAny.setStatus("current")


class _Hh3cAclIPAclNamedBscRouteTypeValue_Type(Integer32):
    """Custom type hh3cAclIPAclNamedBscRouteTypeValue based on Integer32"""
    defaultValue = 65535

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
        ValueRangeConstraint(65535, 65535),
    )


_Hh3cAclIPAclNamedBscRouteTypeValue_Type.__name__ = "Integer32"
_Hh3cAclIPAclNamedBscRouteTypeValue_Object = MibTableColumn
hh3cAclIPAclNamedBscRouteTypeValue = _Hh3cAclIPAclNamedBscRouteTypeValue_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 2, 2, 4, 1, 18),
    _Hh3cAclIPAclNamedBscRouteTypeValue_Type()
)
hh3cAclIPAclNamedBscRouteTypeValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cAclIPAclNamedBscRouteTypeValue.setStatus("current")
_Hh3cAclIPAclNamedAdvTable_Object = MibTable
hh3cAclIPAclNamedAdvTable = _Hh3cAclIPAclNamedAdvTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 2, 2, 5)
)
if mibBuilder.loadTexts:
    hh3cAclIPAclNamedAdvTable.setStatus("current")
_Hh3cAclIPAclNamedAdvEntry_Object = MibTableRow
hh3cAclIPAclNamedAdvEntry = _Hh3cAclIPAclNamedAdvEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 2, 2, 5, 1)
)
hh3cAclIPAclNamedAdvEntry.setIndexNames(
    (0, "HH3C-ACL-MIB", "hh3cAclNumberGroupType"),
    (0, "HH3C-ACL-MIB", "hh3cAclNamedGroupName"),
    (0, "HH3C-ACL-MIB", "hh3cAclIPAclAdvancedRuleIndex"),
)
if mibBuilder.loadTexts:
    hh3cAclIPAclNamedAdvEntry.setStatus("current")
_Hh3cAclIPAclNamedAdvRowStatus_Type = RowStatus
_Hh3cAclIPAclNamedAdvRowStatus_Object = MibTableColumn
hh3cAclIPAclNamedAdvRowStatus = _Hh3cAclIPAclNamedAdvRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 2, 2, 5, 1, 1),
    _Hh3cAclIPAclNamedAdvRowStatus_Type()
)
hh3cAclIPAclNamedAdvRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cAclIPAclNamedAdvRowStatus.setStatus("current")
_Hh3cAclIPAclNamedAdvAct_Type = RuleAction
_Hh3cAclIPAclNamedAdvAct_Object = MibTableColumn
hh3cAclIPAclNamedAdvAct = _Hh3cAclIPAclNamedAdvAct_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 2, 2, 5, 1, 2),
    _Hh3cAclIPAclNamedAdvAct_Type()
)
hh3cAclIPAclNamedAdvAct.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cAclIPAclNamedAdvAct.setStatus("current")


class _Hh3cAclIPAclNamedAdvProtocol_Type(Integer32):
    """Custom type hh3cAclIPAclNamedAdvProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_Hh3cAclIPAclNamedAdvProtocol_Type.__name__ = "Integer32"
_Hh3cAclIPAclNamedAdvProtocol_Object = MibTableColumn
hh3cAclIPAclNamedAdvProtocol = _Hh3cAclIPAclNamedAdvProtocol_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 2, 2, 5, 1, 3),
    _Hh3cAclIPAclNamedAdvProtocol_Type()
)
hh3cAclIPAclNamedAdvProtocol.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cAclIPAclNamedAdvProtocol.setStatus("current")


class _Hh3cAclIPAclNamedAdvAddrFlag_Type(AddressFlag):
    """Custom type hh3cAclIPAclNamedAdvAddrFlag based on AddressFlag"""
    defaultValue = 0


_Hh3cAclIPAclNamedAdvAddrFlag_Type.__name__ = "AddressFlag"
_Hh3cAclIPAclNamedAdvAddrFlag_Object = MibTableColumn
hh3cAclIPAclNamedAdvAddrFlag = _Hh3cAclIPAclNamedAdvAddrFlag_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 2, 2, 5, 1, 4),
    _Hh3cAclIPAclNamedAdvAddrFlag_Type()
)
hh3cAclIPAclNamedAdvAddrFlag.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cAclIPAclNamedAdvAddrFlag.setStatus("current")
_Hh3cAclIPAclNamedAdvSrcAddrType_Type = InetAddressType
_Hh3cAclIPAclNamedAdvSrcAddrType_Object = MibTableColumn
hh3cAclIPAclNamedAdvSrcAddrType = _Hh3cAclIPAclNamedAdvSrcAddrType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 2, 2, 5, 1, 5),
    _Hh3cAclIPAclNamedAdvSrcAddrType_Type()
)
hh3cAclIPAclNamedAdvSrcAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cAclIPAclNamedAdvSrcAddrType.setStatus("current")
_Hh3cAclIPAclNamedAdvSrcAddr_Type = InetAddress
_Hh3cAclIPAclNamedAdvSrcAddr_Object = MibTableColumn
hh3cAclIPAclNamedAdvSrcAddr = _Hh3cAclIPAclNamedAdvSrcAddr_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 2, 2, 5, 1, 6),
    _Hh3cAclIPAclNamedAdvSrcAddr_Type()
)
hh3cAclIPAclNamedAdvSrcAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cAclIPAclNamedAdvSrcAddr.setStatus("current")
_Hh3cAclIPAclNamedAdvSrcPrefix_Type = InetAddressPrefixLength
_Hh3cAclIPAclNamedAdvSrcPrefix_Object = MibTableColumn
hh3cAclIPAclNamedAdvSrcPrefix = _Hh3cAclIPAclNamedAdvSrcPrefix_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 2, 2, 5, 1, 7),
    _Hh3cAclIPAclNamedAdvSrcPrefix_Type()
)
hh3cAclIPAclNamedAdvSrcPrefix.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cAclIPAclNamedAdvSrcPrefix.setStatus("current")


class _Hh3cAclIPAclNamedAdvSrcAny_Type(TruthValue):
    """Custom type hh3cAclIPAclNamedAdvSrcAny based on TruthValue"""
    defaultValue = 1


_Hh3cAclIPAclNamedAdvSrcAny_Type.__name__ = "TruthValue"
_Hh3cAclIPAclNamedAdvSrcAny_Object = MibTableColumn
hh3cAclIPAclNamedAdvSrcAny = _Hh3cAclIPAclNamedAdvSrcAny_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 2, 2, 5, 1, 8),
    _Hh3cAclIPAclNamedAdvSrcAny_Type()
)
hh3cAclIPAclNamedAdvSrcAny.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cAclIPAclNamedAdvSrcAny.setStatus("current")
_Hh3cAclIPAclNamedAdvSrcWild_Type = IpAddress
_Hh3cAclIPAclNamedAdvSrcWild_Object = MibTableColumn
hh3cAclIPAclNamedAdvSrcWild = _Hh3cAclIPAclNamedAdvSrcWild_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 2, 2, 5, 1, 9),
    _Hh3cAclIPAclNamedAdvSrcWild_Type()
)
hh3cAclIPAclNamedAdvSrcWild.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cAclIPAclNamedAdvSrcWild.setStatus("current")


class _Hh3cAclIPAclNamedAdvSrcOp_Type(PortOp):
    """Custom type hh3cAclIPAclNamedAdvSrcOp based on PortOp"""
    defaultValue = 0


_Hh3cAclIPAclNamedAdvSrcOp_Type.__name__ = "PortOp"
_Hh3cAclIPAclNamedAdvSrcOp_Object = MibTableColumn
hh3cAclIPAclNamedAdvSrcOp = _Hh3cAclIPAclNamedAdvSrcOp_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 2, 2, 5, 1, 10),
    _Hh3cAclIPAclNamedAdvSrcOp_Type()
)
hh3cAclIPAclNamedAdvSrcOp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cAclIPAclNamedAdvSrcOp.setStatus("current")


class _Hh3cAclIPAclNamedAdvSrcPort1_Type(Integer32):
    """Custom type hh3cAclIPAclNamedAdvSrcPort1 based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Hh3cAclIPAclNamedAdvSrcPort1_Type.__name__ = "Integer32"
_Hh3cAclIPAclNamedAdvSrcPort1_Object = MibTableColumn
hh3cAclIPAclNamedAdvSrcPort1 = _Hh3cAclIPAclNamedAdvSrcPort1_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 2, 2, 5, 1, 11),
    _Hh3cAclIPAclNamedAdvSrcPort1_Type()
)
hh3cAclIPAclNamedAdvSrcPort1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cAclIPAclNamedAdvSrcPort1.setStatus("current")


class _Hh3cAclIPAclNamedAdvSrcPort2_Type(Integer32):
    """Custom type hh3cAclIPAclNamedAdvSrcPort2 based on Integer32"""
    defaultValue = 65535

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Hh3cAclIPAclNamedAdvSrcPort2_Type.__name__ = "Integer32"
_Hh3cAclIPAclNamedAdvSrcPort2_Object = MibTableColumn
hh3cAclIPAclNamedAdvSrcPort2 = _Hh3cAclIPAclNamedAdvSrcPort2_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 2, 2, 5, 1, 12),
    _Hh3cAclIPAclNamedAdvSrcPort2_Type()
)
hh3cAclIPAclNamedAdvSrcPort2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cAclIPAclNamedAdvSrcPort2.setStatus("current")
_Hh3cAclIPAclNamedAdvDstAddrType_Type = InetAddressType
_Hh3cAclIPAclNamedAdvDstAddrType_Object = MibTableColumn
hh3cAclIPAclNamedAdvDstAddrType = _Hh3cAclIPAclNamedAdvDstAddrType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 2, 2, 5, 1, 13),
    _Hh3cAclIPAclNamedAdvDstAddrType_Type()
)
hh3cAclIPAclNamedAdvDstAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cAclIPAclNamedAdvDstAddrType.setStatus("current")
_Hh3cAclIPAclNamedAdvDstAddr_Type = InetAddress
_Hh3cAclIPAclNamedAdvDstAddr_Object = MibTableColumn
hh3cAclIPAclNamedAdvDstAddr = _Hh3cAclIPAclNamedAdvDstAddr_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 2, 2, 5, 1, 14),
    _Hh3cAclIPAclNamedAdvDstAddr_Type()
)
hh3cAclIPAclNamedAdvDstAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cAclIPAclNamedAdvDstAddr.setStatus("current")
_Hh3cAclIPAclNamedAdvDstPrefix_Type = InetAddressPrefixLength
_Hh3cAclIPAclNamedAdvDstPrefix_Object = MibTableColumn
hh3cAclIPAclNamedAdvDstPrefix = _Hh3cAclIPAclNamedAdvDstPrefix_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 2, 2, 5, 1, 15),
    _Hh3cAclIPAclNamedAdvDstPrefix_Type()
)
hh3cAclIPAclNamedAdvDstPrefix.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cAclIPAclNamedAdvDstPrefix.setStatus("current")


class _Hh3cAclIPAclNamedAdvDstAny_Type(TruthValue):
    """Custom type hh3cAclIPAclNamedAdvDstAny based on TruthValue"""
    defaultValue = 1


_Hh3cAclIPAclNamedAdvDstAny_Type.__name__ = "TruthValue"
_Hh3cAclIPAclNamedAdvDstAny_Object = MibTableColumn
hh3cAclIPAclNamedAdvDstAny = _Hh3cAclIPAclNamedAdvDstAny_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 2, 2, 5, 1, 16),
    _Hh3cAclIPAclNamedAdvDstAny_Type()
)
hh3cAclIPAclNamedAdvDstAny.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cAclIPAclNamedAdvDstAny.setStatus("current")
_Hh3cAclIPAclNamedAdvDstWild_Type = IpAddress
_Hh3cAclIPAclNamedAdvDstWild_Object = MibTableColumn
hh3cAclIPAclNamedAdvDstWild = _Hh3cAclIPAclNamedAdvDstWild_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 2, 2, 5, 1, 17),
    _Hh3cAclIPAclNamedAdvDstWild_Type()
)
hh3cAclIPAclNamedAdvDstWild.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cAclIPAclNamedAdvDstWild.setStatus("current")


class _Hh3cAclIPAclNamedAdvDstOp_Type(PortOp):
    """Custom type hh3cAclIPAclNamedAdvDstOp based on PortOp"""
    defaultValue = 0


_Hh3cAclIPAclNamedAdvDstOp_Type.__name__ = "PortOp"
_Hh3cAclIPAclNamedAdvDstOp_Object = MibTableColumn
hh3cAclIPAclNamedAdvDstOp = _Hh3cAclIPAclNamedAdvDstOp_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 2, 2, 5, 1, 18),
    _Hh3cAclIPAclNamedAdvDstOp_Type()
)
hh3cAclIPAclNamedAdvDstOp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cAclIPAclNamedAdvDstOp.setStatus("current")


class _Hh3cAclIPAclNamedAdvDstPort1_Type(Integer32):
    """Custom type hh3cAclIPAclNamedAdvDstPort1 based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Hh3cAclIPAclNamedAdvDstPort1_Type.__name__ = "Integer32"
_Hh3cAclIPAclNamedAdvDstPort1_Object = MibTableColumn
hh3cAclIPAclNamedAdvDstPort1 = _Hh3cAclIPAclNamedAdvDstPort1_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 2, 2, 5, 1, 19),
    _Hh3cAclIPAclNamedAdvDstPort1_Type()
)
hh3cAclIPAclNamedAdvDstPort1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cAclIPAclNamedAdvDstPort1.setStatus("current")


class _Hh3cAclIPAclNamedAdvDstPort2_Type(Integer32):
    """Custom type hh3cAclIPAclNamedAdvDstPort2 based on Integer32"""
    defaultValue = 65535

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Hh3cAclIPAclNamedAdvDstPort2_Type.__name__ = "Integer32"
_Hh3cAclIPAclNamedAdvDstPort2_Object = MibTableColumn
hh3cAclIPAclNamedAdvDstPort2 = _Hh3cAclIPAclNamedAdvDstPort2_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 2, 2, 5, 1, 20),
    _Hh3cAclIPAclNamedAdvDstPort2_Type()
)
hh3cAclIPAclNamedAdvDstPort2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cAclIPAclNamedAdvDstPort2.setStatus("current")


class _Hh3cAclIPAclNamedAdvIcmpType_Type(Integer32):
    """Custom type hh3cAclIPAclNamedAdvIcmpType based on Integer32"""
    defaultValue = 65535

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
        ValueRangeConstraint(65535, 65535),
    )


_Hh3cAclIPAclNamedAdvIcmpType_Type.__name__ = "Integer32"
_Hh3cAclIPAclNamedAdvIcmpType_Object = MibTableColumn
hh3cAclIPAclNamedAdvIcmpType = _Hh3cAclIPAclNamedAdvIcmpType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 2, 2, 5, 1, 21),
    _Hh3cAclIPAclNamedAdvIcmpType_Type()
)
hh3cAclIPAclNamedAdvIcmpType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cAclIPAclNamedAdvIcmpType.setStatus("current")


class _Hh3cAclIPAclNamedAdvIcmpCode_Type(Integer32):
    """Custom type hh3cAclIPAclNamedAdvIcmpCode based on Integer32"""
    defaultValue = 65535

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
        ValueRangeConstraint(65535, 65535),
    )


_Hh3cAclIPAclNamedAdvIcmpCode_Type.__name__ = "Integer32"
_Hh3cAclIPAclNamedAdvIcmpCode_Object = MibTableColumn
hh3cAclIPAclNamedAdvIcmpCode = _Hh3cAclIPAclNamedAdvIcmpCode_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 2, 2, 5, 1, 22),
    _Hh3cAclIPAclNamedAdvIcmpCode_Type()
)
hh3cAclIPAclNamedAdvIcmpCode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cAclIPAclNamedAdvIcmpCode.setStatus("current")


class _Hh3cAclIPAclNamedAdvPrecedence_Type(Integer32):
    """Custom type hh3cAclIPAclNamedAdvPrecedence based on Integer32"""
    defaultValue = 255

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
        ValueRangeConstraint(255, 255),
    )


_Hh3cAclIPAclNamedAdvPrecedence_Type.__name__ = "Integer32"
_Hh3cAclIPAclNamedAdvPrecedence_Object = MibTableColumn
hh3cAclIPAclNamedAdvPrecedence = _Hh3cAclIPAclNamedAdvPrecedence_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 2, 2, 5, 1, 23),
    _Hh3cAclIPAclNamedAdvPrecedence_Type()
)
hh3cAclIPAclNamedAdvPrecedence.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cAclIPAclNamedAdvPrecedence.setStatus("current")


class _Hh3cAclIPAclNamedAdvTos_Type(Integer32):
    """Custom type hh3cAclIPAclNamedAdvTos based on Integer32"""
    defaultValue = 255

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
        ValueRangeConstraint(255, 255),
    )


_Hh3cAclIPAclNamedAdvTos_Type.__name__ = "Integer32"
_Hh3cAclIPAclNamedAdvTos_Object = MibTableColumn
hh3cAclIPAclNamedAdvTos = _Hh3cAclIPAclNamedAdvTos_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 2, 2, 5, 1, 24),
    _Hh3cAclIPAclNamedAdvTos_Type()
)
hh3cAclIPAclNamedAdvTos.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cAclIPAclNamedAdvTos.setStatus("current")


class _Hh3cAclIPAclNamedAdvDscp_Type(DSCPValue):
    """Custom type hh3cAclIPAclNamedAdvDscp based on DSCPValue"""
    defaultValue = 255


_Hh3cAclIPAclNamedAdvDscp_Type.__name__ = "DSCPValue"
_Hh3cAclIPAclNamedAdvDscp_Object = MibTableColumn
hh3cAclIPAclNamedAdvDscp = _Hh3cAclIPAclNamedAdvDscp_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 2, 2, 5, 1, 25),
    _Hh3cAclIPAclNamedAdvDscp_Type()
)
hh3cAclIPAclNamedAdvDscp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cAclIPAclNamedAdvDscp.setStatus("current")


class _Hh3cAclIPAclNamedAdvTRangeName_Type(OctetString):
    """Custom type hh3cAclIPAclNamedAdvTRangeName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Hh3cAclIPAclNamedAdvTRangeName_Type.__name__ = "OctetString"
_Hh3cAclIPAclNamedAdvTRangeName_Object = MibTableColumn
hh3cAclIPAclNamedAdvTRangeName = _Hh3cAclIPAclNamedAdvTRangeName_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 2, 2, 5, 1, 26),
    _Hh3cAclIPAclNamedAdvTRangeName_Type()
)
hh3cAclIPAclNamedAdvTRangeName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cAclIPAclNamedAdvTRangeName.setStatus("current")


class _Hh3cAclIPAclNamedAdvTCPFlag_Type(TCPFlag):
    """Custom type hh3cAclIPAclNamedAdvTCPFlag based on TCPFlag"""
    defaultValue = 0


_Hh3cAclIPAclNamedAdvTCPFlag_Type.__name__ = "TCPFlag"
_Hh3cAclIPAclNamedAdvTCPFlag_Object = MibTableColumn
hh3cAclIPAclNamedAdvTCPFlag = _Hh3cAclIPAclNamedAdvTCPFlag_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 2, 2, 5, 1, 27),
    _Hh3cAclIPAclNamedAdvTCPFlag_Type()
)
hh3cAclIPAclNamedAdvTCPFlag.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cAclIPAclNamedAdvTCPFlag.setStatus("current")


class _Hh3cAclIPAclNamedAdvFragmentFlag_Type(FragmentFlag):
    """Custom type hh3cAclIPAclNamedAdvFragmentFlag based on FragmentFlag"""
    defaultValue = 0


_Hh3cAclIPAclNamedAdvFragmentFlag_Type.__name__ = "FragmentFlag"
_Hh3cAclIPAclNamedAdvFragmentFlag_Object = MibTableColumn
hh3cAclIPAclNamedAdvFragmentFlag = _Hh3cAclIPAclNamedAdvFragmentFlag_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 2, 2, 5, 1, 28),
    _Hh3cAclIPAclNamedAdvFragmentFlag_Type()
)
hh3cAclIPAclNamedAdvFragmentFlag.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cAclIPAclNamedAdvFragmentFlag.setStatus("current")


class _Hh3cAclIPAclNamedAdvLog_Type(TruthValue):
    """Custom type hh3cAclIPAclNamedAdvLog based on TruthValue"""
    defaultValue = 2


_Hh3cAclIPAclNamedAdvLog_Type.__name__ = "TruthValue"
_Hh3cAclIPAclNamedAdvLog_Object = MibTableColumn
hh3cAclIPAclNamedAdvLog = _Hh3cAclIPAclNamedAdvLog_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 2, 2, 5, 1, 29),
    _Hh3cAclIPAclNamedAdvLog_Type()
)
hh3cAclIPAclNamedAdvLog.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cAclIPAclNamedAdvLog.setStatus("current")
_Hh3cAclIPAclNamedAdvCount_Type = Unsigned32
_Hh3cAclIPAclNamedAdvCount_Object = MibTableColumn
hh3cAclIPAclNamedAdvCount = _Hh3cAclIPAclNamedAdvCount_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 2, 2, 5, 1, 30),
    _Hh3cAclIPAclNamedAdvCount_Type()
)
hh3cAclIPAclNamedAdvCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cAclIPAclNamedAdvCount.setStatus("current")


class _Hh3cAclIPAclNamedAdvCountClear_Type(CounterClear):
    """Custom type hh3cAclIPAclNamedAdvCountClear based on CounterClear"""
    defaultValue = 2


_Hh3cAclIPAclNamedAdvCountClear_Type.__name__ = "CounterClear"
_Hh3cAclIPAclNamedAdvCountClear_Object = MibTableColumn
hh3cAclIPAclNamedAdvCountClear = _Hh3cAclIPAclNamedAdvCountClear_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 2, 2, 5, 1, 31),
    _Hh3cAclIPAclNamedAdvCountClear_Type()
)
hh3cAclIPAclNamedAdvCountClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cAclIPAclNamedAdvCountClear.setStatus("current")


class _Hh3cAclIPAclNamedAdvEnable_Type(TruthValue):
    """Custom type hh3cAclIPAclNamedAdvEnable based on TruthValue"""
    defaultValue = 2


_Hh3cAclIPAclNamedAdvEnable_Type.__name__ = "TruthValue"
_Hh3cAclIPAclNamedAdvEnable_Object = MibTableColumn
hh3cAclIPAclNamedAdvEnable = _Hh3cAclIPAclNamedAdvEnable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 2, 2, 5, 1, 32),
    _Hh3cAclIPAclNamedAdvEnable_Type()
)
hh3cAclIPAclNamedAdvEnable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cAclIPAclNamedAdvEnable.setStatus("current")


class _Hh3cAclIPAclNamedAdvVpnInstName_Type(OctetString):
    """Custom type hh3cAclIPAclNamedAdvVpnInstName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Hh3cAclIPAclNamedAdvVpnInstName_Type.__name__ = "OctetString"
_Hh3cAclIPAclNamedAdvVpnInstName_Object = MibTableColumn
hh3cAclIPAclNamedAdvVpnInstName = _Hh3cAclIPAclNamedAdvVpnInstName_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 2, 2, 5, 1, 33),
    _Hh3cAclIPAclNamedAdvVpnInstName_Type()
)
hh3cAclIPAclNamedAdvVpnInstName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cAclIPAclNamedAdvVpnInstName.setStatus("current")


class _Hh3cAclIPAclNamedAdvComment_Type(OctetString):
    """Custom type hh3cAclIPAclNamedAdvComment based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_Hh3cAclIPAclNamedAdvComment_Type.__name__ = "OctetString"
_Hh3cAclIPAclNamedAdvComment_Object = MibTableColumn
hh3cAclIPAclNamedAdvComment = _Hh3cAclIPAclNamedAdvComment_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 2, 2, 5, 1, 34),
    _Hh3cAclIPAclNamedAdvComment_Type()
)
hh3cAclIPAclNamedAdvComment.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cAclIPAclNamedAdvComment.setStatus("current")
_Hh3cAclIPAclNamedAdvReflective_Type = TruthValue
_Hh3cAclIPAclNamedAdvReflective_Object = MibTableColumn
hh3cAclIPAclNamedAdvReflective = _Hh3cAclIPAclNamedAdvReflective_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 2, 2, 5, 1, 35),
    _Hh3cAclIPAclNamedAdvReflective_Type()
)
hh3cAclIPAclNamedAdvReflective.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cAclIPAclNamedAdvReflective.setStatus("current")


class _Hh3cAclIPAclNamedAdvCounting_Type(TruthValue):
    """Custom type hh3cAclIPAclNamedAdvCounting based on TruthValue"""
    defaultValue = 2


_Hh3cAclIPAclNamedAdvCounting_Type.__name__ = "TruthValue"
_Hh3cAclIPAclNamedAdvCounting_Object = MibTableColumn
hh3cAclIPAclNamedAdvCounting = _Hh3cAclIPAclNamedAdvCounting_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 2, 2, 5, 1, 36),
    _Hh3cAclIPAclNamedAdvCounting_Type()
)
hh3cAclIPAclNamedAdvCounting.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cAclIPAclNamedAdvCounting.setStatus("current")


class _Hh3cAclIPAclNamedAdvTCPFlagMask_Type(Bits):
    """Custom type hh3cAclIPAclNamedAdvTCPFlagMask based on Bits"""
    namedValues = NamedValues(
        *(("tcpack", 0),
          ("tcpfin", 1),
          ("tcppsh", 2),
          ("tcprst", 3),
          ("tcpsyn", 4),
          ("tcpurg", 5))
    )

_Hh3cAclIPAclNamedAdvTCPFlagMask_Type.__name__ = "Bits"
_Hh3cAclIPAclNamedAdvTCPFlagMask_Object = MibTableColumn
hh3cAclIPAclNamedAdvTCPFlagMask = _Hh3cAclIPAclNamedAdvTCPFlagMask_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 2, 2, 5, 1, 37),
    _Hh3cAclIPAclNamedAdvTCPFlagMask_Type()
)
hh3cAclIPAclNamedAdvTCPFlagMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cAclIPAclNamedAdvTCPFlagMask.setStatus("current")


class _Hh3cAclIPAclNamedAdvTCPFlagValue_Type(Bits):
    """Custom type hh3cAclIPAclNamedAdvTCPFlagValue based on Bits"""
    namedValues = NamedValues(
        *(("tcpack", 0),
          ("tcpfin", 1),
          ("tcppsh", 2),
          ("tcprst", 3),
          ("tcpsyn", 4),
          ("tcpurg", 5))
    )

_Hh3cAclIPAclNamedAdvTCPFlagValue_Type.__name__ = "Bits"
_Hh3cAclIPAclNamedAdvTCPFlagValue_Object = MibTableColumn
hh3cAclIPAclNamedAdvTCPFlagValue = _Hh3cAclIPAclNamedAdvTCPFlagValue_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 2, 2, 5, 1, 38),
    _Hh3cAclIPAclNamedAdvTCPFlagValue_Type()
)
hh3cAclIPAclNamedAdvTCPFlagValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cAclIPAclNamedAdvTCPFlagValue.setStatus("current")


class _Hh3cAclIPAclNamedAdvRouteTypeAny_Type(TruthValue):
    """Custom type hh3cAclIPAclNamedAdvRouteTypeAny based on TruthValue"""
    defaultValue = 2


_Hh3cAclIPAclNamedAdvRouteTypeAny_Type.__name__ = "TruthValue"
_Hh3cAclIPAclNamedAdvRouteTypeAny_Object = MibTableColumn
hh3cAclIPAclNamedAdvRouteTypeAny = _Hh3cAclIPAclNamedAdvRouteTypeAny_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 2, 2, 5, 1, 39),
    _Hh3cAclIPAclNamedAdvRouteTypeAny_Type()
)
hh3cAclIPAclNamedAdvRouteTypeAny.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cAclIPAclNamedAdvRouteTypeAny.setStatus("current")


class _Hh3cAclIPAclNamedAdvRouteTypeValue_Type(Integer32):
    """Custom type hh3cAclIPAclNamedAdvRouteTypeValue based on Integer32"""
    defaultValue = 65535

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
        ValueRangeConstraint(65535, 65535),
    )


_Hh3cAclIPAclNamedAdvRouteTypeValue_Type.__name__ = "Integer32"
_Hh3cAclIPAclNamedAdvRouteTypeValue_Object = MibTableColumn
hh3cAclIPAclNamedAdvRouteTypeValue = _Hh3cAclIPAclNamedAdvRouteTypeValue_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 2, 2, 5, 1, 40),
    _Hh3cAclIPAclNamedAdvRouteTypeValue_Type()
)
hh3cAclIPAclNamedAdvRouteTypeValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cAclIPAclNamedAdvRouteTypeValue.setStatus("current")


class _Hh3cAclIPAclNamedAdvFlowLabel_Type(Unsigned32):
    """Custom type hh3cAclIPAclNamedAdvFlowLabel based on Unsigned32"""
    defaultValue = 4294967295

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1048575),
        ValueRangeConstraint(4294967295, 4294967295),
    )


_Hh3cAclIPAclNamedAdvFlowLabel_Type.__name__ = "Unsigned32"
_Hh3cAclIPAclNamedAdvFlowLabel_Object = MibTableColumn
hh3cAclIPAclNamedAdvFlowLabel = _Hh3cAclIPAclNamedAdvFlowLabel_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 2, 2, 5, 1, 41),
    _Hh3cAclIPAclNamedAdvFlowLabel_Type()
)
hh3cAclIPAclNamedAdvFlowLabel.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cAclIPAclNamedAdvFlowLabel.setStatus("current")
_Hh3cAclIPAclNamedAdvSrcSuffix_Type = Unsigned32
_Hh3cAclIPAclNamedAdvSrcSuffix_Object = MibTableColumn
hh3cAclIPAclNamedAdvSrcSuffix = _Hh3cAclIPAclNamedAdvSrcSuffix_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 2, 2, 5, 1, 42),
    _Hh3cAclIPAclNamedAdvSrcSuffix_Type()
)
hh3cAclIPAclNamedAdvSrcSuffix.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cAclIPAclNamedAdvSrcSuffix.setStatus("current")
_Hh3cAclIPAclNamedAdvDstSuffix_Type = Unsigned32
_Hh3cAclIPAclNamedAdvDstSuffix_Object = MibTableColumn
hh3cAclIPAclNamedAdvDstSuffix = _Hh3cAclIPAclNamedAdvDstSuffix_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 2, 2, 5, 1, 43),
    _Hh3cAclIPAclNamedAdvDstSuffix_Type()
)
hh3cAclIPAclNamedAdvDstSuffix.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cAclIPAclNamedAdvDstSuffix.setStatus("current")
_Hh3cAclMACAclGroup_ObjectIdentity = ObjectIdentity
hh3cAclMACAclGroup = _Hh3cAclMACAclGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 2, 3)
)
_Hh3cAclMACTable_Object = MibTable
hh3cAclMACTable = _Hh3cAclMACTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 2, 3, 1)
)
if mibBuilder.loadTexts:
    hh3cAclMACTable.setStatus("current")
_Hh3cAclMACEntry_Object = MibTableRow
hh3cAclMACEntry = _Hh3cAclMACEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 2, 3, 1, 1)
)
hh3cAclMACEntry.setIndexNames(
    (0, "HH3C-ACL-MIB", "hh3cAclNumberGroupType"),
    (0, "HH3C-ACL-MIB", "hh3cAclNumberGroupIndex"),
    (0, "HH3C-ACL-MIB", "hh3cAclMACRuleIndex"),
)
if mibBuilder.loadTexts:
    hh3cAclMACEntry.setStatus("current")


class _Hh3cAclMACRuleIndex_Type(Integer32):
    """Custom type hh3cAclMACRuleIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65534),
    )


_Hh3cAclMACRuleIndex_Type.__name__ = "Integer32"
_Hh3cAclMACRuleIndex_Object = MibTableColumn
hh3cAclMACRuleIndex = _Hh3cAclMACRuleIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 2, 3, 1, 1, 1),
    _Hh3cAclMACRuleIndex_Type()
)
hh3cAclMACRuleIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cAclMACRuleIndex.setStatus("current")
_Hh3cAclMACRowStatus_Type = RowStatus
_Hh3cAclMACRowStatus_Object = MibTableColumn
hh3cAclMACRowStatus = _Hh3cAclMACRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 2, 3, 1, 1, 2),
    _Hh3cAclMACRowStatus_Type()
)
hh3cAclMACRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cAclMACRowStatus.setStatus("current")
_Hh3cAclMACAct_Type = RuleAction
_Hh3cAclMACAct_Object = MibTableColumn
hh3cAclMACAct = _Hh3cAclMACAct_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 2, 3, 1, 1, 3),
    _Hh3cAclMACAct_Type()
)
hh3cAclMACAct.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cAclMACAct.setStatus("current")


class _Hh3cAclMACTypeCode_Type(OctetString):
    """Custom type hh3cAclMACTypeCode based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Hh3cAclMACTypeCode_Type.__name__ = "OctetString"
_Hh3cAclMACTypeCode_Object = MibTableColumn
hh3cAclMACTypeCode = _Hh3cAclMACTypeCode_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 2, 3, 1, 1, 4),
    _Hh3cAclMACTypeCode_Type()
)
hh3cAclMACTypeCode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cAclMACTypeCode.setStatus("current")


class _Hh3cAclMACTypeMask_Type(OctetString):
    """Custom type hh3cAclMACTypeMask based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Hh3cAclMACTypeMask_Type.__name__ = "OctetString"
_Hh3cAclMACTypeMask_Object = MibTableColumn
hh3cAclMACTypeMask = _Hh3cAclMACTypeMask_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 2, 3, 1, 1, 5),
    _Hh3cAclMACTypeMask_Type()
)
hh3cAclMACTypeMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cAclMACTypeMask.setStatus("current")
_Hh3cAclMACSrcMac_Type = MacAddress
_Hh3cAclMACSrcMac_Object = MibTableColumn
hh3cAclMACSrcMac = _Hh3cAclMACSrcMac_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 2, 3, 1, 1, 6),
    _Hh3cAclMACSrcMac_Type()
)
hh3cAclMACSrcMac.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cAclMACSrcMac.setStatus("current")
_Hh3cAclMACSrcMacWild_Type = MacAddress
_Hh3cAclMACSrcMacWild_Object = MibTableColumn
hh3cAclMACSrcMacWild = _Hh3cAclMACSrcMacWild_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 2, 3, 1, 1, 7),
    _Hh3cAclMACSrcMacWild_Type()
)
hh3cAclMACSrcMacWild.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cAclMACSrcMacWild.setStatus("current")
_Hh3cAclMACDestMac_Type = MacAddress
_Hh3cAclMACDestMac_Object = MibTableColumn
hh3cAclMACDestMac = _Hh3cAclMACDestMac_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 2, 3, 1, 1, 8),
    _Hh3cAclMACDestMac_Type()
)
hh3cAclMACDestMac.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cAclMACDestMac.setStatus("current")
_Hh3cAclMACDestMacWild_Type = MacAddress
_Hh3cAclMACDestMacWild_Object = MibTableColumn
hh3cAclMACDestMacWild = _Hh3cAclMACDestMacWild_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 2, 3, 1, 1, 9),
    _Hh3cAclMACDestMacWild_Type()
)
hh3cAclMACDestMacWild.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cAclMACDestMacWild.setStatus("current")


class _Hh3cAclMACLsapCode_Type(OctetString):
    """Custom type hh3cAclMACLsapCode based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Hh3cAclMACLsapCode_Type.__name__ = "OctetString"
_Hh3cAclMACLsapCode_Object = MibTableColumn
hh3cAclMACLsapCode = _Hh3cAclMACLsapCode_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 2, 3, 1, 1, 10),
    _Hh3cAclMACLsapCode_Type()
)
hh3cAclMACLsapCode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cAclMACLsapCode.setStatus("current")


class _Hh3cAclMACLsapMask_Type(OctetString):
    """Custom type hh3cAclMACLsapMask based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Hh3cAclMACLsapMask_Type.__name__ = "OctetString"
_Hh3cAclMACLsapMask_Object = MibTableColumn
hh3cAclMACLsapMask = _Hh3cAclMACLsapMask_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 2, 3, 1, 1, 11),
    _Hh3cAclMACLsapMask_Type()
)
hh3cAclMACLsapMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cAclMACLsapMask.setStatus("current")


class _Hh3cAclMACCos_Type(Integer32):
    """Custom type hh3cAclMACCos based on Integer32"""
    defaultValue = 255

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
        ValueRangeConstraint(255, 255),
    )


_Hh3cAclMACCos_Type.__name__ = "Integer32"
_Hh3cAclMACCos_Object = MibTableColumn
hh3cAclMACCos = _Hh3cAclMACCos_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 2, 3, 1, 1, 12),
    _Hh3cAclMACCos_Type()
)
hh3cAclMACCos.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cAclMACCos.setStatus("current")


class _Hh3cAclMACTimeRangeName_Type(OctetString):
    """Custom type hh3cAclMACTimeRangeName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Hh3cAclMACTimeRangeName_Type.__name__ = "OctetString"
_Hh3cAclMACTimeRangeName_Object = MibTableColumn
hh3cAclMACTimeRangeName = _Hh3cAclMACTimeRangeName_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 2, 3, 1, 1, 13),
    _Hh3cAclMACTimeRangeName_Type()
)
hh3cAclMACTimeRangeName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cAclMACTimeRangeName.setStatus("current")
_Hh3cAclMACCount_Type = Unsigned32
_Hh3cAclMACCount_Object = MibTableColumn
hh3cAclMACCount = _Hh3cAclMACCount_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 2, 3, 1, 1, 14),
    _Hh3cAclMACCount_Type()
)
hh3cAclMACCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cAclMACCount.setStatus("current")


class _Hh3cAclMACCountClear_Type(CounterClear):
    """Custom type hh3cAclMACCountClear based on CounterClear"""
    defaultValue = 2


_Hh3cAclMACCountClear_Type.__name__ = "CounterClear"
_Hh3cAclMACCountClear_Object = MibTableColumn
hh3cAclMACCountClear = _Hh3cAclMACCountClear_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 2, 3, 1, 1, 15),
    _Hh3cAclMACCountClear_Type()
)
hh3cAclMACCountClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cAclMACCountClear.setStatus("current")


class _Hh3cAclMACEnable_Type(TruthValue):
    """Custom type hh3cAclMACEnable based on TruthValue"""
    defaultValue = 2


_Hh3cAclMACEnable_Type.__name__ = "TruthValue"
_Hh3cAclMACEnable_Object = MibTableColumn
hh3cAclMACEnable = _Hh3cAclMACEnable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 2, 3, 1, 1, 16),
    _Hh3cAclMACEnable_Type()
)
hh3cAclMACEnable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cAclMACEnable.setStatus("current")


class _Hh3cAclMACComment_Type(OctetString):
    """Custom type hh3cAclMACComment based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_Hh3cAclMACComment_Type.__name__ = "OctetString"
_Hh3cAclMACComment_Object = MibTableColumn
hh3cAclMACComment = _Hh3cAclMACComment_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 2, 3, 1, 1, 17),
    _Hh3cAclMACComment_Type()
)
hh3cAclMACComment.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cAclMACComment.setStatus("current")


class _Hh3cAclMACLog_Type(TruthValue):
    """Custom type hh3cAclMACLog based on TruthValue"""
    defaultValue = 2


_Hh3cAclMACLog_Type.__name__ = "TruthValue"
_Hh3cAclMACLog_Object = MibTableColumn
hh3cAclMACLog = _Hh3cAclMACLog_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 2, 3, 1, 1, 18),
    _Hh3cAclMACLog_Type()
)
hh3cAclMACLog.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cAclMACLog.setStatus("current")


class _Hh3cAclMACCounting_Type(TruthValue):
    """Custom type hh3cAclMACCounting based on TruthValue"""
    defaultValue = 2


_Hh3cAclMACCounting_Type.__name__ = "TruthValue"
_Hh3cAclMACCounting_Object = MibTableColumn
hh3cAclMACCounting = _Hh3cAclMACCounting_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 2, 3, 1, 1, 19),
    _Hh3cAclMACCounting_Type()
)
hh3cAclMACCounting.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cAclMACCounting.setStatus("current")
_Hh3cAclNamedMACTable_Object = MibTable
hh3cAclNamedMACTable = _Hh3cAclNamedMACTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 2, 3, 2)
)
if mibBuilder.loadTexts:
    hh3cAclNamedMACTable.setStatus("current")
_Hh3cAclNamedMACEntry_Object = MibTableRow
hh3cAclNamedMACEntry = _Hh3cAclNamedMACEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 2, 3, 2, 1)
)
hh3cAclNamedMACEntry.setIndexNames(
    (0, "HH3C-ACL-MIB", "hh3cAclNumberGroupType"),
    (0, "HH3C-ACL-MIB", "hh3cAclNamedGroupName"),
    (0, "HH3C-ACL-MIB", "hh3cAclMACRuleIndex"),
)
if mibBuilder.loadTexts:
    hh3cAclNamedMACEntry.setStatus("current")
_Hh3cAclNamedMACRowStatus_Type = RowStatus
_Hh3cAclNamedMACRowStatus_Object = MibTableColumn
hh3cAclNamedMACRowStatus = _Hh3cAclNamedMACRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 2, 3, 2, 1, 1),
    _Hh3cAclNamedMACRowStatus_Type()
)
hh3cAclNamedMACRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cAclNamedMACRowStatus.setStatus("current")
_Hh3cAclNamedMACAct_Type = RuleAction
_Hh3cAclNamedMACAct_Object = MibTableColumn
hh3cAclNamedMACAct = _Hh3cAclNamedMACAct_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 2, 3, 2, 1, 2),
    _Hh3cAclNamedMACAct_Type()
)
hh3cAclNamedMACAct.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cAclNamedMACAct.setStatus("current")


class _Hh3cAclNamedMACTypeCode_Type(OctetString):
    """Custom type hh3cAclNamedMACTypeCode based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Hh3cAclNamedMACTypeCode_Type.__name__ = "OctetString"
_Hh3cAclNamedMACTypeCode_Object = MibTableColumn
hh3cAclNamedMACTypeCode = _Hh3cAclNamedMACTypeCode_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 2, 3, 2, 1, 3),
    _Hh3cAclNamedMACTypeCode_Type()
)
hh3cAclNamedMACTypeCode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cAclNamedMACTypeCode.setStatus("current")


class _Hh3cAclNamedMACTypeMask_Type(OctetString):
    """Custom type hh3cAclNamedMACTypeMask based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Hh3cAclNamedMACTypeMask_Type.__name__ = "OctetString"
_Hh3cAclNamedMACTypeMask_Object = MibTableColumn
hh3cAclNamedMACTypeMask = _Hh3cAclNamedMACTypeMask_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 2, 3, 2, 1, 4),
    _Hh3cAclNamedMACTypeMask_Type()
)
hh3cAclNamedMACTypeMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cAclNamedMACTypeMask.setStatus("current")
_Hh3cAclNamedMACSrcMac_Type = MacAddress
_Hh3cAclNamedMACSrcMac_Object = MibTableColumn
hh3cAclNamedMACSrcMac = _Hh3cAclNamedMACSrcMac_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 2, 3, 2, 1, 5),
    _Hh3cAclNamedMACSrcMac_Type()
)
hh3cAclNamedMACSrcMac.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cAclNamedMACSrcMac.setStatus("current")
_Hh3cAclNamedMACSrcMacWild_Type = MacAddress
_Hh3cAclNamedMACSrcMacWild_Object = MibTableColumn
hh3cAclNamedMACSrcMacWild = _Hh3cAclNamedMACSrcMacWild_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 2, 3, 2, 1, 6),
    _Hh3cAclNamedMACSrcMacWild_Type()
)
hh3cAclNamedMACSrcMacWild.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cAclNamedMACSrcMacWild.setStatus("current")
_Hh3cAclNamedMACDstMac_Type = MacAddress
_Hh3cAclNamedMACDstMac_Object = MibTableColumn
hh3cAclNamedMACDstMac = _Hh3cAclNamedMACDstMac_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 2, 3, 2, 1, 7),
    _Hh3cAclNamedMACDstMac_Type()
)
hh3cAclNamedMACDstMac.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cAclNamedMACDstMac.setStatus("current")
_Hh3cAclNamedMACDstMacWild_Type = MacAddress
_Hh3cAclNamedMACDstMacWild_Object = MibTableColumn
hh3cAclNamedMACDstMacWild = _Hh3cAclNamedMACDstMacWild_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 2, 3, 2, 1, 8),
    _Hh3cAclNamedMACDstMacWild_Type()
)
hh3cAclNamedMACDstMacWild.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cAclNamedMACDstMacWild.setStatus("current")


class _Hh3cAclNamedMACLsapCode_Type(OctetString):
    """Custom type hh3cAclNamedMACLsapCode based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Hh3cAclNamedMACLsapCode_Type.__name__ = "OctetString"
_Hh3cAclNamedMACLsapCode_Object = MibTableColumn
hh3cAclNamedMACLsapCode = _Hh3cAclNamedMACLsapCode_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 2, 3, 2, 1, 9),
    _Hh3cAclNamedMACLsapCode_Type()
)
hh3cAclNamedMACLsapCode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cAclNamedMACLsapCode.setStatus("current")


class _Hh3cAclNamedMACLsapMask_Type(OctetString):
    """Custom type hh3cAclNamedMACLsapMask based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Hh3cAclNamedMACLsapMask_Type.__name__ = "OctetString"
_Hh3cAclNamedMACLsapMask_Object = MibTableColumn
hh3cAclNamedMACLsapMask = _Hh3cAclNamedMACLsapMask_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 2, 3, 2, 1, 10),
    _Hh3cAclNamedMACLsapMask_Type()
)
hh3cAclNamedMACLsapMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cAclNamedMACLsapMask.setStatus("current")


class _Hh3cAclNamedMACCos_Type(Integer32):
    """Custom type hh3cAclNamedMACCos based on Integer32"""
    defaultValue = 255

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
        ValueRangeConstraint(255, 255),
    )


_Hh3cAclNamedMACCos_Type.__name__ = "Integer32"
_Hh3cAclNamedMACCos_Object = MibTableColumn
hh3cAclNamedMACCos = _Hh3cAclNamedMACCos_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 2, 3, 2, 1, 11),
    _Hh3cAclNamedMACCos_Type()
)
hh3cAclNamedMACCos.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cAclNamedMACCos.setStatus("current")


class _Hh3cAclNamedMACTimeRangeName_Type(OctetString):
    """Custom type hh3cAclNamedMACTimeRangeName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Hh3cAclNamedMACTimeRangeName_Type.__name__ = "OctetString"
_Hh3cAclNamedMACTimeRangeName_Object = MibTableColumn
hh3cAclNamedMACTimeRangeName = _Hh3cAclNamedMACTimeRangeName_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 2, 3, 2, 1, 12),
    _Hh3cAclNamedMACTimeRangeName_Type()
)
hh3cAclNamedMACTimeRangeName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cAclNamedMACTimeRangeName.setStatus("current")
_Hh3cAclNamedMACCount_Type = Unsigned32
_Hh3cAclNamedMACCount_Object = MibTableColumn
hh3cAclNamedMACCount = _Hh3cAclNamedMACCount_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 2, 3, 2, 1, 13),
    _Hh3cAclNamedMACCount_Type()
)
hh3cAclNamedMACCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cAclNamedMACCount.setStatus("current")


class _Hh3cAclNamedMACCountClear_Type(CounterClear):
    """Custom type hh3cAclNamedMACCountClear based on CounterClear"""
    defaultValue = 2


_Hh3cAclNamedMACCountClear_Type.__name__ = "CounterClear"
_Hh3cAclNamedMACCountClear_Object = MibTableColumn
hh3cAclNamedMACCountClear = _Hh3cAclNamedMACCountClear_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 2, 3, 2, 1, 14),
    _Hh3cAclNamedMACCountClear_Type()
)
hh3cAclNamedMACCountClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cAclNamedMACCountClear.setStatus("current")


class _Hh3cAclNamedMACEnable_Type(TruthValue):
    """Custom type hh3cAclNamedMACEnable based on TruthValue"""
    defaultValue = 2


_Hh3cAclNamedMACEnable_Type.__name__ = "TruthValue"
_Hh3cAclNamedMACEnable_Object = MibTableColumn
hh3cAclNamedMACEnable = _Hh3cAclNamedMACEnable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 2, 3, 2, 1, 15),
    _Hh3cAclNamedMACEnable_Type()
)
hh3cAclNamedMACEnable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cAclNamedMACEnable.setStatus("current")


class _Hh3cAclNamedMACComment_Type(OctetString):
    """Custom type hh3cAclNamedMACComment based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_Hh3cAclNamedMACComment_Type.__name__ = "OctetString"
_Hh3cAclNamedMACComment_Object = MibTableColumn
hh3cAclNamedMACComment = _Hh3cAclNamedMACComment_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 2, 3, 2, 1, 16),
    _Hh3cAclNamedMACComment_Type()
)
hh3cAclNamedMACComment.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cAclNamedMACComment.setStatus("current")


class _Hh3cAclNamedMACLog_Type(TruthValue):
    """Custom type hh3cAclNamedMACLog based on TruthValue"""
    defaultValue = 2


_Hh3cAclNamedMACLog_Type.__name__ = "TruthValue"
_Hh3cAclNamedMACLog_Object = MibTableColumn
hh3cAclNamedMACLog = _Hh3cAclNamedMACLog_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 2, 3, 2, 1, 17),
    _Hh3cAclNamedMACLog_Type()
)
hh3cAclNamedMACLog.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cAclNamedMACLog.setStatus("current")


class _Hh3cAclNamedMACCounting_Type(TruthValue):
    """Custom type hh3cAclNamedMACCounting based on TruthValue"""
    defaultValue = 2


_Hh3cAclNamedMACCounting_Type.__name__ = "TruthValue"
_Hh3cAclNamedMACCounting_Object = MibTableColumn
hh3cAclNamedMACCounting = _Hh3cAclNamedMACCounting_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 2, 3, 2, 1, 18),
    _Hh3cAclNamedMACCounting_Type()
)
hh3cAclNamedMACCounting.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cAclNamedMACCounting.setStatus("current")
_Hh3cAclEnUserAclGroup_ObjectIdentity = ObjectIdentity
hh3cAclEnUserAclGroup = _Hh3cAclEnUserAclGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 2, 4)
)
_Hh3cAclEnUserTable_Object = MibTable
hh3cAclEnUserTable = _Hh3cAclEnUserTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 2, 4, 3)
)
if mibBuilder.loadTexts:
    hh3cAclEnUserTable.setStatus("current")
_Hh3cAclEnUserEntry_Object = MibTableRow
hh3cAclEnUserEntry = _Hh3cAclEnUserEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 2, 4, 3, 1)
)
hh3cAclEnUserEntry.setIndexNames(
    (0, "HH3C-ACL-MIB", "hh3cAclNumberGroupType"),
    (0, "HH3C-ACL-MIB", "hh3cAclNumberGroupIndex"),
    (0, "HH3C-ACL-MIB", "hh3cAclEnUserRuleIndex"),
)
if mibBuilder.loadTexts:
    hh3cAclEnUserEntry.setStatus("current")


class _Hh3cAclEnUserRuleIndex_Type(Integer32):
    """Custom type hh3cAclEnUserRuleIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65534),
    )


_Hh3cAclEnUserRuleIndex_Type.__name__ = "Integer32"
_Hh3cAclEnUserRuleIndex_Object = MibTableColumn
hh3cAclEnUserRuleIndex = _Hh3cAclEnUserRuleIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 2, 4, 3, 1, 1),
    _Hh3cAclEnUserRuleIndex_Type()
)
hh3cAclEnUserRuleIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cAclEnUserRuleIndex.setStatus("current")
_Hh3cAclEnUserRowStatus_Type = RowStatus
_Hh3cAclEnUserRowStatus_Object = MibTableColumn
hh3cAclEnUserRowStatus = _Hh3cAclEnUserRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 2, 4, 3, 1, 2),
    _Hh3cAclEnUserRowStatus_Type()
)
hh3cAclEnUserRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cAclEnUserRowStatus.setStatus("current")
_Hh3cAclEnUserAct_Type = RuleAction
_Hh3cAclEnUserAct_Object = MibTableColumn
hh3cAclEnUserAct = _Hh3cAclEnUserAct_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 2, 4, 3, 1, 3),
    _Hh3cAclEnUserAct_Type()
)
hh3cAclEnUserAct.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cAclEnUserAct.setStatus("current")


class _Hh3cAclEnUserStartString_Type(OctetString):
    """Custom type hh3cAclEnUserStartString based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_Hh3cAclEnUserStartString_Type.__name__ = "OctetString"
_Hh3cAclEnUserStartString_Object = MibTableColumn
hh3cAclEnUserStartString = _Hh3cAclEnUserStartString_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 2, 4, 3, 1, 4),
    _Hh3cAclEnUserStartString_Type()
)
hh3cAclEnUserStartString.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cAclEnUserStartString.setStatus("current")


class _Hh3cAclEnUserL2String_Type(OctetString):
    """Custom type hh3cAclEnUserL2String based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_Hh3cAclEnUserL2String_Type.__name__ = "OctetString"
_Hh3cAclEnUserL2String_Object = MibTableColumn
hh3cAclEnUserL2String = _Hh3cAclEnUserL2String_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 2, 4, 3, 1, 5),
    _Hh3cAclEnUserL2String_Type()
)
hh3cAclEnUserL2String.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cAclEnUserL2String.setStatus("current")


class _Hh3cAclEnUserMplsString_Type(OctetString):
    """Custom type hh3cAclEnUserMplsString based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_Hh3cAclEnUserMplsString_Type.__name__ = "OctetString"
_Hh3cAclEnUserMplsString_Object = MibTableColumn
hh3cAclEnUserMplsString = _Hh3cAclEnUserMplsString_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 2, 4, 3, 1, 6),
    _Hh3cAclEnUserMplsString_Type()
)
hh3cAclEnUserMplsString.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cAclEnUserMplsString.setStatus("current")


class _Hh3cAclEnUserIPv4String_Type(OctetString):
    """Custom type hh3cAclEnUserIPv4String based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_Hh3cAclEnUserIPv4String_Type.__name__ = "OctetString"
_Hh3cAclEnUserIPv4String_Object = MibTableColumn
hh3cAclEnUserIPv4String = _Hh3cAclEnUserIPv4String_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 2, 4, 3, 1, 7),
    _Hh3cAclEnUserIPv4String_Type()
)
hh3cAclEnUserIPv4String.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cAclEnUserIPv4String.setStatus("current")


class _Hh3cAclEnUserIPv6String_Type(OctetString):
    """Custom type hh3cAclEnUserIPv6String based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_Hh3cAclEnUserIPv6String_Type.__name__ = "OctetString"
_Hh3cAclEnUserIPv6String_Object = MibTableColumn
hh3cAclEnUserIPv6String = _Hh3cAclEnUserIPv6String_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 2, 4, 3, 1, 8),
    _Hh3cAclEnUserIPv6String_Type()
)
hh3cAclEnUserIPv6String.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cAclEnUserIPv6String.setStatus("current")


class _Hh3cAclEnUserL4String_Type(OctetString):
    """Custom type hh3cAclEnUserL4String based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_Hh3cAclEnUserL4String_Type.__name__ = "OctetString"
_Hh3cAclEnUserL4String_Object = MibTableColumn
hh3cAclEnUserL4String = _Hh3cAclEnUserL4String_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 2, 4, 3, 1, 9),
    _Hh3cAclEnUserL4String_Type()
)
hh3cAclEnUserL4String.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cAclEnUserL4String.setStatus("current")


class _Hh3cAclEnUserL5String_Type(OctetString):
    """Custom type hh3cAclEnUserL5String based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_Hh3cAclEnUserL5String_Type.__name__ = "OctetString"
_Hh3cAclEnUserL5String_Object = MibTableColumn
hh3cAclEnUserL5String = _Hh3cAclEnUserL5String_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 2, 4, 3, 1, 10),
    _Hh3cAclEnUserL5String_Type()
)
hh3cAclEnUserL5String.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cAclEnUserL5String.setStatus("current")


class _Hh3cAclEnUserTimeRangeName_Type(OctetString):
    """Custom type hh3cAclEnUserTimeRangeName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Hh3cAclEnUserTimeRangeName_Type.__name__ = "OctetString"
_Hh3cAclEnUserTimeRangeName_Object = MibTableColumn
hh3cAclEnUserTimeRangeName = _Hh3cAclEnUserTimeRangeName_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 2, 4, 3, 1, 11),
    _Hh3cAclEnUserTimeRangeName_Type()
)
hh3cAclEnUserTimeRangeName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cAclEnUserTimeRangeName.setStatus("current")
_Hh3cAclEnUserCount_Type = Unsigned32
_Hh3cAclEnUserCount_Object = MibTableColumn
hh3cAclEnUserCount = _Hh3cAclEnUserCount_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 2, 4, 3, 1, 12),
    _Hh3cAclEnUserCount_Type()
)
hh3cAclEnUserCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cAclEnUserCount.setStatus("current")
_Hh3cAclEnUserCountClear_Type = CounterClear
_Hh3cAclEnUserCountClear_Object = MibTableColumn
hh3cAclEnUserCountClear = _Hh3cAclEnUserCountClear_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 2, 4, 3, 1, 13),
    _Hh3cAclEnUserCountClear_Type()
)
hh3cAclEnUserCountClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cAclEnUserCountClear.setStatus("current")


class _Hh3cAclEnUserEnable_Type(TruthValue):
    """Custom type hh3cAclEnUserEnable based on TruthValue"""
    defaultValue = 2


_Hh3cAclEnUserEnable_Type.__name__ = "TruthValue"
_Hh3cAclEnUserEnable_Object = MibTableColumn
hh3cAclEnUserEnable = _Hh3cAclEnUserEnable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 2, 4, 3, 1, 14),
    _Hh3cAclEnUserEnable_Type()
)
hh3cAclEnUserEnable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cAclEnUserEnable.setStatus("current")


class _Hh3cAclEnUserComment_Type(OctetString):
    """Custom type hh3cAclEnUserComment based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_Hh3cAclEnUserComment_Type.__name__ = "OctetString"
_Hh3cAclEnUserComment_Object = MibTableColumn
hh3cAclEnUserComment = _Hh3cAclEnUserComment_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 2, 4, 3, 1, 15),
    _Hh3cAclEnUserComment_Type()
)
hh3cAclEnUserComment.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cAclEnUserComment.setStatus("current")


class _Hh3cAclEnUserLog_Type(TruthValue):
    """Custom type hh3cAclEnUserLog based on TruthValue"""
    defaultValue = 2


_Hh3cAclEnUserLog_Type.__name__ = "TruthValue"
_Hh3cAclEnUserLog_Object = MibTableColumn
hh3cAclEnUserLog = _Hh3cAclEnUserLog_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 2, 4, 3, 1, 16),
    _Hh3cAclEnUserLog_Type()
)
hh3cAclEnUserLog.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cAclEnUserLog.setStatus("current")


class _Hh3cAclEnUserCounting_Type(TruthValue):
    """Custom type hh3cAclEnUserCounting based on TruthValue"""
    defaultValue = 2


_Hh3cAclEnUserCounting_Type.__name__ = "TruthValue"
_Hh3cAclEnUserCounting_Object = MibTableColumn
hh3cAclEnUserCounting = _Hh3cAclEnUserCounting_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 2, 4, 3, 1, 17),
    _Hh3cAclEnUserCounting_Type()
)
hh3cAclEnUserCounting.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cAclEnUserCounting.setStatus("current")
_Hh3cAclNamedUserTable_Object = MibTable
hh3cAclNamedUserTable = _Hh3cAclNamedUserTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 2, 4, 4)
)
if mibBuilder.loadTexts:
    hh3cAclNamedUserTable.setStatus("current")
_Hh3cAclNamedUserEntry_Object = MibTableRow
hh3cAclNamedUserEntry = _Hh3cAclNamedUserEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 2, 4, 4, 1)
)
hh3cAclNamedUserEntry.setIndexNames(
    (0, "HH3C-ACL-MIB", "hh3cAclNumberGroupType"),
    (0, "HH3C-ACL-MIB", "hh3cAclNamedGroupName"),
    (0, "HH3C-ACL-MIB", "hh3cAclEnUserRuleIndex"),
)
if mibBuilder.loadTexts:
    hh3cAclNamedUserEntry.setStatus("current")
_Hh3cAclNamedUserRowStatus_Type = RowStatus
_Hh3cAclNamedUserRowStatus_Object = MibTableColumn
hh3cAclNamedUserRowStatus = _Hh3cAclNamedUserRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 2, 4, 4, 1, 1),
    _Hh3cAclNamedUserRowStatus_Type()
)
hh3cAclNamedUserRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cAclNamedUserRowStatus.setStatus("current")
_Hh3cAclNamedUserAct_Type = RuleAction
_Hh3cAclNamedUserAct_Object = MibTableColumn
hh3cAclNamedUserAct = _Hh3cAclNamedUserAct_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 2, 4, 4, 1, 2),
    _Hh3cAclNamedUserAct_Type()
)
hh3cAclNamedUserAct.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cAclNamedUserAct.setStatus("current")


class _Hh3cAclNamedUserStartString_Type(OctetString):
    """Custom type hh3cAclNamedUserStartString based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_Hh3cAclNamedUserStartString_Type.__name__ = "OctetString"
_Hh3cAclNamedUserStartString_Object = MibTableColumn
hh3cAclNamedUserStartString = _Hh3cAclNamedUserStartString_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 2, 4, 4, 1, 3),
    _Hh3cAclNamedUserStartString_Type()
)
hh3cAclNamedUserStartString.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cAclNamedUserStartString.setStatus("current")


class _Hh3cAclNamedUserL2String_Type(OctetString):
    """Custom type hh3cAclNamedUserL2String based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_Hh3cAclNamedUserL2String_Type.__name__ = "OctetString"
_Hh3cAclNamedUserL2String_Object = MibTableColumn
hh3cAclNamedUserL2String = _Hh3cAclNamedUserL2String_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 2, 4, 4, 1, 4),
    _Hh3cAclNamedUserL2String_Type()
)
hh3cAclNamedUserL2String.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cAclNamedUserL2String.setStatus("current")


class _Hh3cAclNamedUserMplsString_Type(OctetString):
    """Custom type hh3cAclNamedUserMplsString based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_Hh3cAclNamedUserMplsString_Type.__name__ = "OctetString"
_Hh3cAclNamedUserMplsString_Object = MibTableColumn
hh3cAclNamedUserMplsString = _Hh3cAclNamedUserMplsString_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 2, 4, 4, 1, 5),
    _Hh3cAclNamedUserMplsString_Type()
)
hh3cAclNamedUserMplsString.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cAclNamedUserMplsString.setStatus("current")


class _Hh3cAclNamedUserIPv4String_Type(OctetString):
    """Custom type hh3cAclNamedUserIPv4String based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_Hh3cAclNamedUserIPv4String_Type.__name__ = "OctetString"
_Hh3cAclNamedUserIPv4String_Object = MibTableColumn
hh3cAclNamedUserIPv4String = _Hh3cAclNamedUserIPv4String_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 2, 4, 4, 1, 6),
    _Hh3cAclNamedUserIPv4String_Type()
)
hh3cAclNamedUserIPv4String.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cAclNamedUserIPv4String.setStatus("current")


class _Hh3cAclNamedUserIPv6String_Type(OctetString):
    """Custom type hh3cAclNamedUserIPv6String based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_Hh3cAclNamedUserIPv6String_Type.__name__ = "OctetString"
_Hh3cAclNamedUserIPv6String_Object = MibTableColumn
hh3cAclNamedUserIPv6String = _Hh3cAclNamedUserIPv6String_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 2, 4, 4, 1, 7),
    _Hh3cAclNamedUserIPv6String_Type()
)
hh3cAclNamedUserIPv6String.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cAclNamedUserIPv6String.setStatus("current")


class _Hh3cAclNamedUserL4String_Type(OctetString):
    """Custom type hh3cAclNamedUserL4String based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_Hh3cAclNamedUserL4String_Type.__name__ = "OctetString"
_Hh3cAclNamedUserL4String_Object = MibTableColumn
hh3cAclNamedUserL4String = _Hh3cAclNamedUserL4String_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 2, 4, 4, 1, 8),
    _Hh3cAclNamedUserL4String_Type()
)
hh3cAclNamedUserL4String.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cAclNamedUserL4String.setStatus("current")


class _Hh3cAclNamedUserL5String_Type(OctetString):
    """Custom type hh3cAclNamedUserL5String based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_Hh3cAclNamedUserL5String_Type.__name__ = "OctetString"
_Hh3cAclNamedUserL5String_Object = MibTableColumn
hh3cAclNamedUserL5String = _Hh3cAclNamedUserL5String_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 2, 4, 4, 1, 9),
    _Hh3cAclNamedUserL5String_Type()
)
hh3cAclNamedUserL5String.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cAclNamedUserL5String.setStatus("current")


class _Hh3cAclNamedUserTimeRangeName_Type(OctetString):
    """Custom type hh3cAclNamedUserTimeRangeName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Hh3cAclNamedUserTimeRangeName_Type.__name__ = "OctetString"
_Hh3cAclNamedUserTimeRangeName_Object = MibTableColumn
hh3cAclNamedUserTimeRangeName = _Hh3cAclNamedUserTimeRangeName_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 2, 4, 4, 1, 10),
    _Hh3cAclNamedUserTimeRangeName_Type()
)
hh3cAclNamedUserTimeRangeName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cAclNamedUserTimeRangeName.setStatus("current")
_Hh3cAclNamedUserCount_Type = Unsigned32
_Hh3cAclNamedUserCount_Object = MibTableColumn
hh3cAclNamedUserCount = _Hh3cAclNamedUserCount_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 2, 4, 4, 1, 11),
    _Hh3cAclNamedUserCount_Type()
)
hh3cAclNamedUserCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cAclNamedUserCount.setStatus("current")
_Hh3cAclNamedUserCountClear_Type = CounterClear
_Hh3cAclNamedUserCountClear_Object = MibTableColumn
hh3cAclNamedUserCountClear = _Hh3cAclNamedUserCountClear_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 2, 4, 4, 1, 12),
    _Hh3cAclNamedUserCountClear_Type()
)
hh3cAclNamedUserCountClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cAclNamedUserCountClear.setStatus("current")


class _Hh3cAclNamedUserEnable_Type(TruthValue):
    """Custom type hh3cAclNamedUserEnable based on TruthValue"""
    defaultValue = 2


_Hh3cAclNamedUserEnable_Type.__name__ = "TruthValue"
_Hh3cAclNamedUserEnable_Object = MibTableColumn
hh3cAclNamedUserEnable = _Hh3cAclNamedUserEnable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 2, 4, 4, 1, 13),
    _Hh3cAclNamedUserEnable_Type()
)
hh3cAclNamedUserEnable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cAclNamedUserEnable.setStatus("current")


class _Hh3cAclNamedUserComment_Type(OctetString):
    """Custom type hh3cAclNamedUserComment based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_Hh3cAclNamedUserComment_Type.__name__ = "OctetString"
_Hh3cAclNamedUserComment_Object = MibTableColumn
hh3cAclNamedUserComment = _Hh3cAclNamedUserComment_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 2, 4, 4, 1, 14),
    _Hh3cAclNamedUserComment_Type()
)
hh3cAclNamedUserComment.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cAclNamedUserComment.setStatus("current")


class _Hh3cAclNamedUserLog_Type(TruthValue):
    """Custom type hh3cAclNamedUserLog based on TruthValue"""
    defaultValue = 2


_Hh3cAclNamedUserLog_Type.__name__ = "TruthValue"
_Hh3cAclNamedUserLog_Object = MibTableColumn
hh3cAclNamedUserLog = _Hh3cAclNamedUserLog_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 2, 4, 4, 1, 15),
    _Hh3cAclNamedUserLog_Type()
)
hh3cAclNamedUserLog.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cAclNamedUserLog.setStatus("current")


class _Hh3cAclNamedUserCounting_Type(TruthValue):
    """Custom type hh3cAclNamedUserCounting based on TruthValue"""
    defaultValue = 2


_Hh3cAclNamedUserCounting_Type.__name__ = "TruthValue"
_Hh3cAclNamedUserCounting_Object = MibTableColumn
hh3cAclNamedUserCounting = _Hh3cAclNamedUserCounting_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 2, 4, 4, 1, 16),
    _Hh3cAclNamedUserCounting_Type()
)
hh3cAclNamedUserCounting.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cAclNamedUserCounting.setStatus("current")
_Hh3cAclResourceGroup_ObjectIdentity = ObjectIdentity
hh3cAclResourceGroup = _Hh3cAclResourceGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 2, 5)
)
_Hh3cAclResourceUsageTable_Object = MibTable
hh3cAclResourceUsageTable = _Hh3cAclResourceUsageTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 2, 5, 1)
)
if mibBuilder.loadTexts:
    hh3cAclResourceUsageTable.setStatus("current")
_Hh3cAclResourceUsageEntry_Object = MibTableRow
hh3cAclResourceUsageEntry = _Hh3cAclResourceUsageEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 2, 5, 1, 1)
)
hh3cAclResourceUsageEntry.setIndexNames(
    (0, "HH3C-ACL-MIB", "hh3cAclResourceChassis"),
    (0, "HH3C-ACL-MIB", "hh3cAclResourceSlot"),
    (0, "HH3C-ACL-MIB", "hh3cAclResourceChip"),
    (0, "HH3C-ACL-MIB", "hh3cAclResourceType"),
)
if mibBuilder.loadTexts:
    hh3cAclResourceUsageEntry.setStatus("current")
_Hh3cAclResourceChassis_Type = Unsigned32
_Hh3cAclResourceChassis_Object = MibTableColumn
hh3cAclResourceChassis = _Hh3cAclResourceChassis_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 2, 5, 1, 1, 1),
    _Hh3cAclResourceChassis_Type()
)
hh3cAclResourceChassis.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cAclResourceChassis.setStatus("current")
_Hh3cAclResourceSlot_Type = Unsigned32
_Hh3cAclResourceSlot_Object = MibTableColumn
hh3cAclResourceSlot = _Hh3cAclResourceSlot_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 2, 5, 1, 1, 2),
    _Hh3cAclResourceSlot_Type()
)
hh3cAclResourceSlot.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cAclResourceSlot.setStatus("current")
_Hh3cAclResourceChip_Type = Unsigned32
_Hh3cAclResourceChip_Object = MibTableColumn
hh3cAclResourceChip = _Hh3cAclResourceChip_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 2, 5, 1, 1, 3),
    _Hh3cAclResourceChip_Type()
)
hh3cAclResourceChip.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cAclResourceChip.setStatus("current")


class _Hh3cAclResourceType_Type(Integer32):
    """Custom type hh3cAclResourceType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_Hh3cAclResourceType_Type.__name__ = "Integer32"
_Hh3cAclResourceType_Object = MibTableColumn
hh3cAclResourceType = _Hh3cAclResourceType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 2, 5, 1, 1, 4),
    _Hh3cAclResourceType_Type()
)
hh3cAclResourceType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cAclResourceType.setStatus("current")


class _Hh3cAclPortRange_Type(OctetString):
    """Custom type hh3cAclPortRange based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_Hh3cAclPortRange_Type.__name__ = "OctetString"
_Hh3cAclPortRange_Object = MibTableColumn
hh3cAclPortRange = _Hh3cAclPortRange_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 2, 5, 1, 1, 5),
    _Hh3cAclPortRange_Type()
)
hh3cAclPortRange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cAclPortRange.setStatus("current")
_Hh3cAclResourceTotal_Type = Unsigned32
_Hh3cAclResourceTotal_Object = MibTableColumn
hh3cAclResourceTotal = _Hh3cAclResourceTotal_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 2, 5, 1, 1, 6),
    _Hh3cAclResourceTotal_Type()
)
hh3cAclResourceTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cAclResourceTotal.setStatus("current")
_Hh3cAclResourceReserved_Type = Unsigned32
_Hh3cAclResourceReserved_Object = MibTableColumn
hh3cAclResourceReserved = _Hh3cAclResourceReserved_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 2, 5, 1, 1, 7),
    _Hh3cAclResourceReserved_Type()
)
hh3cAclResourceReserved.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cAclResourceReserved.setStatus("current")
_Hh3cAclResourceConfigured_Type = Unsigned32
_Hh3cAclResourceConfigured_Object = MibTableColumn
hh3cAclResourceConfigured = _Hh3cAclResourceConfigured_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 2, 5, 1, 1, 8),
    _Hh3cAclResourceConfigured_Type()
)
hh3cAclResourceConfigured.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cAclResourceConfigured.setStatus("current")
_Hh3cAclResourceUsagePercent_Type = Unsigned32
_Hh3cAclResourceUsagePercent_Object = MibTableColumn
hh3cAclResourceUsagePercent = _Hh3cAclResourceUsagePercent_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 2, 5, 1, 1, 9),
    _Hh3cAclResourceUsagePercent_Type()
)
hh3cAclResourceUsagePercent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cAclResourceUsagePercent.setStatus("current")


class _Hh3cAclResourceTypeDescription_Type(OctetString):
    """Custom type hh3cAclResourceTypeDescription based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_Hh3cAclResourceTypeDescription_Type.__name__ = "OctetString"
_Hh3cAclResourceTypeDescription_Object = MibTableColumn
hh3cAclResourceTypeDescription = _Hh3cAclResourceTypeDescription_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 2, 5, 1, 1, 10),
    _Hh3cAclResourceTypeDescription_Type()
)
hh3cAclResourceTypeDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cAclResourceTypeDescription.setStatus("current")
_Hh3cAclIntervalGroup_ObjectIdentity = ObjectIdentity
hh3cAclIntervalGroup = _Hh3cAclIntervalGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 2, 6)
)
_Hh3cAclIntervalTable_Object = MibTable
hh3cAclIntervalTable = _Hh3cAclIntervalTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 2, 6, 1)
)
if mibBuilder.loadTexts:
    hh3cAclIntervalTable.setStatus("current")
_Hh3cAclIntervalEntry_Object = MibTableRow
hh3cAclIntervalEntry = _Hh3cAclIntervalEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 2, 6, 1, 1)
)
hh3cAclIntervalEntry.setIndexNames(
    (0, "HH3C-ACL-MIB", "hh3cAclIntervalType"),
)
if mibBuilder.loadTexts:
    hh3cAclIntervalEntry.setStatus("current")


class _Hh3cAclIntervalType_Type(Integer32):
    """Custom type hh3cAclIntervalType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("logging", 1),
          ("trap", 2))
    )


_Hh3cAclIntervalType_Type.__name__ = "Integer32"
_Hh3cAclIntervalType_Object = MibTableColumn
hh3cAclIntervalType = _Hh3cAclIntervalType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 2, 6, 1, 1, 1),
    _Hh3cAclIntervalType_Type()
)
hh3cAclIntervalType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cAclIntervalType.setStatus("current")


class _Hh3cAclIntervalValue_Type(Integer32):
    """Custom type hh3cAclIntervalValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 1440),
    )


_Hh3cAclIntervalValue_Type.__name__ = "Integer32"
_Hh3cAclIntervalValue_Object = MibTableColumn
hh3cAclIntervalValue = _Hh3cAclIntervalValue_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 2, 6, 1, 1, 2),
    _Hh3cAclIntervalValue_Type()
)
hh3cAclIntervalValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cAclIntervalValue.setStatus("current")
_Hh3cAclIntervalRowStatus_Type = RowStatus
_Hh3cAclIntervalRowStatus_Object = MibTableColumn
hh3cAclIntervalRowStatus = _Hh3cAclIntervalRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 2, 6, 1, 1, 3),
    _Hh3cAclIntervalRowStatus_Type()
)
hh3cAclIntervalRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cAclIntervalRowStatus.setStatus("current")
_Hh3cAclPacketFilterObjects_ObjectIdentity = ObjectIdentity
hh3cAclPacketFilterObjects = _Hh3cAclPacketFilterObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 3)
)
_Hh3cPfilterScalarGroup_ObjectIdentity = ObjectIdentity
hh3cPfilterScalarGroup = _Hh3cPfilterScalarGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 3, 1)
)


class _Hh3cPfilterDefaultAction_Type(Integer32):
    """Custom type hh3cPfilterDefaultAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("permit", 1),
          ("deny", 2))
    )


_Hh3cPfilterDefaultAction_Type.__name__ = "Integer32"
_Hh3cPfilterDefaultAction_Object = MibScalar
hh3cPfilterDefaultAction = _Hh3cPfilterDefaultAction_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 3, 1, 1),
    _Hh3cPfilterDefaultAction_Type()
)
hh3cPfilterDefaultAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cPfilterDefaultAction.setStatus("current")


class _Hh3cPfilterProcessingStatus_Type(Integer32):
    """Custom type hh3cPfilterProcessingStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("processing", 1),
          ("done", 2))
    )


_Hh3cPfilterProcessingStatus_Type.__name__ = "Integer32"
_Hh3cPfilterProcessingStatus_Object = MibScalar
hh3cPfilterProcessingStatus = _Hh3cPfilterProcessingStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 3, 1, 2),
    _Hh3cPfilterProcessingStatus_Type()
)
hh3cPfilterProcessingStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cPfilterProcessingStatus.setStatus("current")
_Hh3cPfilterApplyTable_Object = MibTable
hh3cPfilterApplyTable = _Hh3cPfilterApplyTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 3, 2)
)
if mibBuilder.loadTexts:
    hh3cPfilterApplyTable.setStatus("current")
_Hh3cPfilterApplyEntry_Object = MibTableRow
hh3cPfilterApplyEntry = _Hh3cPfilterApplyEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 3, 2, 1)
)
hh3cPfilterApplyEntry.setIndexNames(
    (0, "HH3C-ACL-MIB", "hh3cPfilterApplyObjType"),
    (0, "HH3C-ACL-MIB", "hh3cPfilterApplyObjIndex"),
    (0, "HH3C-ACL-MIB", "hh3cPfilterApplyDirection"),
    (0, "HH3C-ACL-MIB", "hh3cPfilterApplyAclType"),
    (0, "HH3C-ACL-MIB", "hh3cPfilterApplyAclIndex"),
)
if mibBuilder.loadTexts:
    hh3cPfilterApplyEntry.setStatus("current")


class _Hh3cPfilterApplyObjType_Type(Integer32):
    """Custom type hh3cPfilterApplyObjType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("interface", 1),
          ("vlan", 2),
          ("global", 3))
    )


_Hh3cPfilterApplyObjType_Type.__name__ = "Integer32"
_Hh3cPfilterApplyObjType_Object = MibTableColumn
hh3cPfilterApplyObjType = _Hh3cPfilterApplyObjType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 3, 2, 1, 1),
    _Hh3cPfilterApplyObjType_Type()
)
hh3cPfilterApplyObjType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cPfilterApplyObjType.setStatus("current")


class _Hh3cPfilterApplyObjIndex_Type(Integer32):
    """Custom type hh3cPfilterApplyObjIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_Hh3cPfilterApplyObjIndex_Type.__name__ = "Integer32"
_Hh3cPfilterApplyObjIndex_Object = MibTableColumn
hh3cPfilterApplyObjIndex = _Hh3cPfilterApplyObjIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 3, 2, 1, 2),
    _Hh3cPfilterApplyObjIndex_Type()
)
hh3cPfilterApplyObjIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cPfilterApplyObjIndex.setStatus("current")
_Hh3cPfilterApplyDirection_Type = DirectionType
_Hh3cPfilterApplyDirection_Object = MibTableColumn
hh3cPfilterApplyDirection = _Hh3cPfilterApplyDirection_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 3, 2, 1, 3),
    _Hh3cPfilterApplyDirection_Type()
)
hh3cPfilterApplyDirection.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cPfilterApplyDirection.setStatus("current")


class _Hh3cPfilterApplyAclType_Type(Integer32):
    """Custom type hh3cPfilterApplyAclType based on Integer32"""
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
        *(("ipv4", 1),
          ("ipv6", 2),
          ("default", 3),
          ("mac", 4),
          ("user", 5))
    )


_Hh3cPfilterApplyAclType_Type.__name__ = "Integer32"
_Hh3cPfilterApplyAclType_Object = MibTableColumn
hh3cPfilterApplyAclType = _Hh3cPfilterApplyAclType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 3, 2, 1, 4),
    _Hh3cPfilterApplyAclType_Type()
)
hh3cPfilterApplyAclType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cPfilterApplyAclType.setStatus("current")


class _Hh3cPfilterApplyAclIndex_Type(Integer32):
    """Custom type hh3cPfilterApplyAclIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(2000, 5999),
    )


_Hh3cPfilterApplyAclIndex_Type.__name__ = "Integer32"
_Hh3cPfilterApplyAclIndex_Object = MibTableColumn
hh3cPfilterApplyAclIndex = _Hh3cPfilterApplyAclIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 3, 2, 1, 5),
    _Hh3cPfilterApplyAclIndex_Type()
)
hh3cPfilterApplyAclIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cPfilterApplyAclIndex.setStatus("current")


class _Hh3cPfilterApplyHardCount_Type(TruthValue):
    """Custom type hh3cPfilterApplyHardCount based on TruthValue"""
    defaultValue = 2


_Hh3cPfilterApplyHardCount_Type.__name__ = "TruthValue"
_Hh3cPfilterApplyHardCount_Object = MibTableColumn
hh3cPfilterApplyHardCount = _Hh3cPfilterApplyHardCount_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 3, 2, 1, 6),
    _Hh3cPfilterApplyHardCount_Type()
)
hh3cPfilterApplyHardCount.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cPfilterApplyHardCount.setStatus("current")
_Hh3cPfilterApplySequence_Type = Unsigned32
_Hh3cPfilterApplySequence_Object = MibTableColumn
hh3cPfilterApplySequence = _Hh3cPfilterApplySequence_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 3, 2, 1, 7),
    _Hh3cPfilterApplySequence_Type()
)
hh3cPfilterApplySequence.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cPfilterApplySequence.setStatus("current")
_Hh3cPfilterApplyCountClear_Type = CounterClear
_Hh3cPfilterApplyCountClear_Object = MibTableColumn
hh3cPfilterApplyCountClear = _Hh3cPfilterApplyCountClear_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 3, 2, 1, 8),
    _Hh3cPfilterApplyCountClear_Type()
)
hh3cPfilterApplyCountClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cPfilterApplyCountClear.setStatus("current")
_Hh3cPfilterApplyRowStatus_Type = RowStatus
_Hh3cPfilterApplyRowStatus_Object = MibTableColumn
hh3cPfilterApplyRowStatus = _Hh3cPfilterApplyRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 3, 2, 1, 9),
    _Hh3cPfilterApplyRowStatus_Type()
)
hh3cPfilterApplyRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cPfilterApplyRowStatus.setStatus("current")
_Hh3cPfilterAclGroupRunInfoTable_Object = MibTable
hh3cPfilterAclGroupRunInfoTable = _Hh3cPfilterAclGroupRunInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 3, 3)
)
if mibBuilder.loadTexts:
    hh3cPfilterAclGroupRunInfoTable.setStatus("current")
_Hh3cPfilterAclGroupRunInfoEntry_Object = MibTableRow
hh3cPfilterAclGroupRunInfoEntry = _Hh3cPfilterAclGroupRunInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 3, 3, 1)
)
hh3cPfilterAclGroupRunInfoEntry.setIndexNames(
    (0, "HH3C-ACL-MIB", "hh3cPfilterRunApplyObjType"),
    (0, "HH3C-ACL-MIB", "hh3cPfilterRunApplyObjIndex"),
    (0, "HH3C-ACL-MIB", "hh3cPfilterRunApplyDirection"),
    (0, "HH3C-ACL-MIB", "hh3cPfilterRunApplyAclType"),
    (0, "HH3C-ACL-MIB", "hh3cPfilterRunApplyAclIndex"),
)
if mibBuilder.loadTexts:
    hh3cPfilterAclGroupRunInfoEntry.setStatus("current")


class _Hh3cPfilterRunApplyObjType_Type(Integer32):
    """Custom type hh3cPfilterRunApplyObjType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("interface", 1),
          ("vlan", 2),
          ("global", 3))
    )


_Hh3cPfilterRunApplyObjType_Type.__name__ = "Integer32"
_Hh3cPfilterRunApplyObjType_Object = MibTableColumn
hh3cPfilterRunApplyObjType = _Hh3cPfilterRunApplyObjType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 3, 3, 1, 1),
    _Hh3cPfilterRunApplyObjType_Type()
)
hh3cPfilterRunApplyObjType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cPfilterRunApplyObjType.setStatus("current")


class _Hh3cPfilterRunApplyObjIndex_Type(Integer32):
    """Custom type hh3cPfilterRunApplyObjIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_Hh3cPfilterRunApplyObjIndex_Type.__name__ = "Integer32"
_Hh3cPfilterRunApplyObjIndex_Object = MibTableColumn
hh3cPfilterRunApplyObjIndex = _Hh3cPfilterRunApplyObjIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 3, 3, 1, 2),
    _Hh3cPfilterRunApplyObjIndex_Type()
)
hh3cPfilterRunApplyObjIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cPfilterRunApplyObjIndex.setStatus("current")
_Hh3cPfilterRunApplyDirection_Type = DirectionType
_Hh3cPfilterRunApplyDirection_Object = MibTableColumn
hh3cPfilterRunApplyDirection = _Hh3cPfilterRunApplyDirection_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 3, 3, 1, 3),
    _Hh3cPfilterRunApplyDirection_Type()
)
hh3cPfilterRunApplyDirection.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cPfilterRunApplyDirection.setStatus("current")


class _Hh3cPfilterRunApplyAclType_Type(Integer32):
    """Custom type hh3cPfilterRunApplyAclType based on Integer32"""
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
        *(("ipv4", 1),
          ("ipv6", 2),
          ("default", 3),
          ("mac", 4),
          ("user", 5))
    )


_Hh3cPfilterRunApplyAclType_Type.__name__ = "Integer32"
_Hh3cPfilterRunApplyAclType_Object = MibTableColumn
hh3cPfilterRunApplyAclType = _Hh3cPfilterRunApplyAclType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 3, 3, 1, 4),
    _Hh3cPfilterRunApplyAclType_Type()
)
hh3cPfilterRunApplyAclType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cPfilterRunApplyAclType.setStatus("current")


class _Hh3cPfilterRunApplyAclIndex_Type(Integer32):
    """Custom type hh3cPfilterRunApplyAclIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
        ValueRangeConstraint(2000, 5999),
    )


_Hh3cPfilterRunApplyAclIndex_Type.__name__ = "Integer32"
_Hh3cPfilterRunApplyAclIndex_Object = MibTableColumn
hh3cPfilterRunApplyAclIndex = _Hh3cPfilterRunApplyAclIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 3, 3, 1, 5),
    _Hh3cPfilterRunApplyAclIndex_Type()
)
hh3cPfilterRunApplyAclIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cPfilterRunApplyAclIndex.setStatus("current")


class _Hh3cPfilterAclGroupStatus_Type(Integer32):
    """Custom type hh3cPfilterAclGroupStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("success", 1),
          ("failed", 2),
          ("partialSuccess", 3))
    )


_Hh3cPfilterAclGroupStatus_Type.__name__ = "Integer32"
_Hh3cPfilterAclGroupStatus_Object = MibTableColumn
hh3cPfilterAclGroupStatus = _Hh3cPfilterAclGroupStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 3, 3, 1, 6),
    _Hh3cPfilterAclGroupStatus_Type()
)
hh3cPfilterAclGroupStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cPfilterAclGroupStatus.setStatus("current")


class _Hh3cPfilterAclGroupCountStatus_Type(Integer32):
    """Custom type hh3cPfilterAclGroupCountStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("success", 1),
          ("failed", 2),
          ("partialSuccess", 3))
    )


_Hh3cPfilterAclGroupCountStatus_Type.__name__ = "Integer32"
_Hh3cPfilterAclGroupCountStatus_Object = MibTableColumn
hh3cPfilterAclGroupCountStatus = _Hh3cPfilterAclGroupCountStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 3, 3, 1, 7),
    _Hh3cPfilterAclGroupCountStatus_Type()
)
hh3cPfilterAclGroupCountStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cPfilterAclGroupCountStatus.setStatus("current")
_Hh3cPfilterAclGroupPermitPkts_Type = Counter64
_Hh3cPfilterAclGroupPermitPkts_Object = MibTableColumn
hh3cPfilterAclGroupPermitPkts = _Hh3cPfilterAclGroupPermitPkts_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 3, 3, 1, 8),
    _Hh3cPfilterAclGroupPermitPkts_Type()
)
hh3cPfilterAclGroupPermitPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cPfilterAclGroupPermitPkts.setStatus("current")
_Hh3cPfilterAclGroupPermitBytes_Type = Counter64
_Hh3cPfilterAclGroupPermitBytes_Object = MibTableColumn
hh3cPfilterAclGroupPermitBytes = _Hh3cPfilterAclGroupPermitBytes_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 3, 3, 1, 9),
    _Hh3cPfilterAclGroupPermitBytes_Type()
)
hh3cPfilterAclGroupPermitBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cPfilterAclGroupPermitBytes.setStatus("current")
_Hh3cPfilterAclGroupDenyPkts_Type = Counter64
_Hh3cPfilterAclGroupDenyPkts_Object = MibTableColumn
hh3cPfilterAclGroupDenyPkts = _Hh3cPfilterAclGroupDenyPkts_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 3, 3, 1, 10),
    _Hh3cPfilterAclGroupDenyPkts_Type()
)
hh3cPfilterAclGroupDenyPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cPfilterAclGroupDenyPkts.setStatus("current")
_Hh3cPfilterAclGroupDenyBytes_Type = Counter64
_Hh3cPfilterAclGroupDenyBytes_Object = MibTableColumn
hh3cPfilterAclGroupDenyBytes = _Hh3cPfilterAclGroupDenyBytes_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 3, 3, 1, 11),
    _Hh3cPfilterAclGroupDenyBytes_Type()
)
hh3cPfilterAclGroupDenyBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cPfilterAclGroupDenyBytes.setStatus("current")
_Hh3cPfilterAclRuleRunInfoTable_Object = MibTable
hh3cPfilterAclRuleRunInfoTable = _Hh3cPfilterAclRuleRunInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 3, 4)
)
if mibBuilder.loadTexts:
    hh3cPfilterAclRuleRunInfoTable.setStatus("current")
_Hh3cPfilterAclRuleRunInfoEntry_Object = MibTableRow
hh3cPfilterAclRuleRunInfoEntry = _Hh3cPfilterAclRuleRunInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 3, 4, 1)
)
hh3cPfilterAclRuleRunInfoEntry.setIndexNames(
    (0, "HH3C-ACL-MIB", "hh3cPfilterRunApplyObjType"),
    (0, "HH3C-ACL-MIB", "hh3cPfilterRunApplyObjIndex"),
    (0, "HH3C-ACL-MIB", "hh3cPfilterRunApplyDirection"),
    (0, "HH3C-ACL-MIB", "hh3cPfilterRunApplyAclType"),
    (0, "HH3C-ACL-MIB", "hh3cPfilterRunApplyAclIndex"),
    (0, "HH3C-ACL-MIB", "hh3cPfilterAclRuleIndex"),
)
if mibBuilder.loadTexts:
    hh3cPfilterAclRuleRunInfoEntry.setStatus("current")


class _Hh3cPfilterAclRuleIndex_Type(Integer32):
    """Custom type hh3cPfilterAclRuleIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65534),
    )


_Hh3cPfilterAclRuleIndex_Type.__name__ = "Integer32"
_Hh3cPfilterAclRuleIndex_Object = MibTableColumn
hh3cPfilterAclRuleIndex = _Hh3cPfilterAclRuleIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 3, 4, 1, 1),
    _Hh3cPfilterAclRuleIndex_Type()
)
hh3cPfilterAclRuleIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cPfilterAclRuleIndex.setStatus("current")


class _Hh3cPfilterAclRuleStatus_Type(Integer32):
    """Custom type hh3cPfilterAclRuleStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("success", 1),
          ("failed", 2),
          ("partialSuccess", 3))
    )


_Hh3cPfilterAclRuleStatus_Type.__name__ = "Integer32"
_Hh3cPfilterAclRuleStatus_Object = MibTableColumn
hh3cPfilterAclRuleStatus = _Hh3cPfilterAclRuleStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 3, 4, 1, 2),
    _Hh3cPfilterAclRuleStatus_Type()
)
hh3cPfilterAclRuleStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cPfilterAclRuleStatus.setStatus("current")


class _Hh3cPfilterAclRuleCountStatus_Type(Integer32):
    """Custom type hh3cPfilterAclRuleCountStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("success", 1),
          ("failed", 2),
          ("partialSuccess", 3))
    )


_Hh3cPfilterAclRuleCountStatus_Type.__name__ = "Integer32"
_Hh3cPfilterAclRuleCountStatus_Object = MibTableColumn
hh3cPfilterAclRuleCountStatus = _Hh3cPfilterAclRuleCountStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 3, 4, 1, 3),
    _Hh3cPfilterAclRuleCountStatus_Type()
)
hh3cPfilterAclRuleCountStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cPfilterAclRuleCountStatus.setStatus("current")
_Hh3cPfilterAclRuleMatchPackets_Type = Counter64
_Hh3cPfilterAclRuleMatchPackets_Object = MibTableColumn
hh3cPfilterAclRuleMatchPackets = _Hh3cPfilterAclRuleMatchPackets_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 3, 4, 1, 4),
    _Hh3cPfilterAclRuleMatchPackets_Type()
)
hh3cPfilterAclRuleMatchPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cPfilterAclRuleMatchPackets.setStatus("current")
_Hh3cPfilterAclRuleMatchBytes_Type = Counter64
_Hh3cPfilterAclRuleMatchBytes_Object = MibTableColumn
hh3cPfilterAclRuleMatchBytes = _Hh3cPfilterAclRuleMatchBytes_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 3, 4, 1, 5),
    _Hh3cPfilterAclRuleMatchBytes_Type()
)
hh3cPfilterAclRuleMatchBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cPfilterAclRuleMatchBytes.setStatus("current")
_Hh3cPfilterStatisticSumTable_Object = MibTable
hh3cPfilterStatisticSumTable = _Hh3cPfilterStatisticSumTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 3, 5)
)
if mibBuilder.loadTexts:
    hh3cPfilterStatisticSumTable.setStatus("current")
_Hh3cPfilterStatisticSumEntry_Object = MibTableRow
hh3cPfilterStatisticSumEntry = _Hh3cPfilterStatisticSumEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 3, 5, 1)
)
hh3cPfilterStatisticSumEntry.setIndexNames(
    (0, "HH3C-ACL-MIB", "hh3cPfilterSumDirection"),
    (0, "HH3C-ACL-MIB", "hh3cPfilterSumAclType"),
    (0, "HH3C-ACL-MIB", "hh3cPfilterSumAclIndex"),
    (0, "HH3C-ACL-MIB", "hh3cPfilterSumRuleIndex"),
)
if mibBuilder.loadTexts:
    hh3cPfilterStatisticSumEntry.setStatus("current")
_Hh3cPfilterSumDirection_Type = DirectionType
_Hh3cPfilterSumDirection_Object = MibTableColumn
hh3cPfilterSumDirection = _Hh3cPfilterSumDirection_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 3, 5, 1, 1),
    _Hh3cPfilterSumDirection_Type()
)
hh3cPfilterSumDirection.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cPfilterSumDirection.setStatus("current")


class _Hh3cPfilterSumAclType_Type(Integer32):
    """Custom type hh3cPfilterSumAclType based on Integer32"""
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
        *(("ipv4", 1),
          ("ipv6", 2),
          ("mac", 3),
          ("user", 4))
    )


_Hh3cPfilterSumAclType_Type.__name__ = "Integer32"
_Hh3cPfilterSumAclType_Object = MibTableColumn
hh3cPfilterSumAclType = _Hh3cPfilterSumAclType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 3, 5, 1, 2),
    _Hh3cPfilterSumAclType_Type()
)
hh3cPfilterSumAclType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cPfilterSumAclType.setStatus("current")


class _Hh3cPfilterSumAclIndex_Type(Integer32):
    """Custom type hh3cPfilterSumAclIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2000, 5999),
    )


_Hh3cPfilterSumAclIndex_Type.__name__ = "Integer32"
_Hh3cPfilterSumAclIndex_Object = MibTableColumn
hh3cPfilterSumAclIndex = _Hh3cPfilterSumAclIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 3, 5, 1, 3),
    _Hh3cPfilterSumAclIndex_Type()
)
hh3cPfilterSumAclIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cPfilterSumAclIndex.setStatus("current")


class _Hh3cPfilterSumRuleIndex_Type(Integer32):
    """Custom type hh3cPfilterSumRuleIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65534),
    )


_Hh3cPfilterSumRuleIndex_Type.__name__ = "Integer32"
_Hh3cPfilterSumRuleIndex_Object = MibTableColumn
hh3cPfilterSumRuleIndex = _Hh3cPfilterSumRuleIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 3, 5, 1, 4),
    _Hh3cPfilterSumRuleIndex_Type()
)
hh3cPfilterSumRuleIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cPfilterSumRuleIndex.setStatus("current")
_Hh3cPfilterSumRuleMatchPackets_Type = Counter64
_Hh3cPfilterSumRuleMatchPackets_Object = MibTableColumn
hh3cPfilterSumRuleMatchPackets = _Hh3cPfilterSumRuleMatchPackets_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 3, 5, 1, 5),
    _Hh3cPfilterSumRuleMatchPackets_Type()
)
hh3cPfilterSumRuleMatchPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cPfilterSumRuleMatchPackets.setStatus("current")
_Hh3cPfilterSumRuleMatchBytes_Type = Counter64
_Hh3cPfilterSumRuleMatchBytes_Object = MibTableColumn
hh3cPfilterSumRuleMatchBytes = _Hh3cPfilterSumRuleMatchBytes_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 3, 5, 1, 6),
    _Hh3cPfilterSumRuleMatchBytes_Type()
)
hh3cPfilterSumRuleMatchBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cPfilterSumRuleMatchBytes.setStatus("current")
_Hh3cPfilter2ApplyTable_Object = MibTable
hh3cPfilter2ApplyTable = _Hh3cPfilter2ApplyTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 3, 6)
)
if mibBuilder.loadTexts:
    hh3cPfilter2ApplyTable.setStatus("current")
_Hh3cPfilter2ApplyEntry_Object = MibTableRow
hh3cPfilter2ApplyEntry = _Hh3cPfilter2ApplyEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 3, 6, 1)
)
hh3cPfilter2ApplyEntry.setIndexNames(
    (0, "HH3C-ACL-MIB", "hh3cPfilter2ApplyObjType"),
    (0, "HH3C-ACL-MIB", "hh3cPfilter2ApplyObjIndex"),
    (0, "HH3C-ACL-MIB", "hh3cPfilter2ApplyDirection"),
    (0, "HH3C-ACL-MIB", "hh3cPfilter2ApplyAclType"),
    (0, "HH3C-ACL-MIB", "hh3cPfilter2ApplyAclIndex"),
)
if mibBuilder.loadTexts:
    hh3cPfilter2ApplyEntry.setStatus("current")


class _Hh3cPfilter2ApplyObjType_Type(Integer32):
    """Custom type hh3cPfilter2ApplyObjType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("interface", 1),
          ("vlan", 2),
          ("global", 3))
    )


_Hh3cPfilter2ApplyObjType_Type.__name__ = "Integer32"
_Hh3cPfilter2ApplyObjType_Object = MibTableColumn
hh3cPfilter2ApplyObjType = _Hh3cPfilter2ApplyObjType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 3, 6, 1, 1),
    _Hh3cPfilter2ApplyObjType_Type()
)
hh3cPfilter2ApplyObjType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cPfilter2ApplyObjType.setStatus("current")


class _Hh3cPfilter2ApplyObjIndex_Type(Integer32):
    """Custom type hh3cPfilter2ApplyObjIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_Hh3cPfilter2ApplyObjIndex_Type.__name__ = "Integer32"
_Hh3cPfilter2ApplyObjIndex_Object = MibTableColumn
hh3cPfilter2ApplyObjIndex = _Hh3cPfilter2ApplyObjIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 3, 6, 1, 2),
    _Hh3cPfilter2ApplyObjIndex_Type()
)
hh3cPfilter2ApplyObjIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cPfilter2ApplyObjIndex.setStatus("current")
_Hh3cPfilter2ApplyDirection_Type = DirectionType
_Hh3cPfilter2ApplyDirection_Object = MibTableColumn
hh3cPfilter2ApplyDirection = _Hh3cPfilter2ApplyDirection_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 3, 6, 1, 3),
    _Hh3cPfilter2ApplyDirection_Type()
)
hh3cPfilter2ApplyDirection.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cPfilter2ApplyDirection.setStatus("current")


class _Hh3cPfilter2ApplyAclType_Type(Integer32):
    """Custom type hh3cPfilter2ApplyAclType based on Integer32"""
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
        *(("ipv4", 1),
          ("ipv6", 2),
          ("default", 3),
          ("mac", 4),
          ("user", 5))
    )


_Hh3cPfilter2ApplyAclType_Type.__name__ = "Integer32"
_Hh3cPfilter2ApplyAclType_Object = MibTableColumn
hh3cPfilter2ApplyAclType = _Hh3cPfilter2ApplyAclType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 3, 6, 1, 4),
    _Hh3cPfilter2ApplyAclType_Type()
)
hh3cPfilter2ApplyAclType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cPfilter2ApplyAclType.setStatus("current")


class _Hh3cPfilter2ApplyAclIndex_Type(OctetString):
    """Custom type hh3cPfilter2ApplyAclIndex based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 63),
    )


_Hh3cPfilter2ApplyAclIndex_Type.__name__ = "OctetString"
_Hh3cPfilter2ApplyAclIndex_Object = MibTableColumn
hh3cPfilter2ApplyAclIndex = _Hh3cPfilter2ApplyAclIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 3, 6, 1, 5),
    _Hh3cPfilter2ApplyAclIndex_Type()
)
hh3cPfilter2ApplyAclIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cPfilter2ApplyAclIndex.setStatus("current")


class _Hh3cPfilter2ApplyHardCount_Type(TruthValue):
    """Custom type hh3cPfilter2ApplyHardCount based on TruthValue"""
    defaultValue = 2


_Hh3cPfilter2ApplyHardCount_Type.__name__ = "TruthValue"
_Hh3cPfilter2ApplyHardCount_Object = MibTableColumn
hh3cPfilter2ApplyHardCount = _Hh3cPfilter2ApplyHardCount_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 3, 6, 1, 6),
    _Hh3cPfilter2ApplyHardCount_Type()
)
hh3cPfilter2ApplyHardCount.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cPfilter2ApplyHardCount.setStatus("current")
_Hh3cPfilter2ApplySequence_Type = Unsigned32
_Hh3cPfilter2ApplySequence_Object = MibTableColumn
hh3cPfilter2ApplySequence = _Hh3cPfilter2ApplySequence_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 3, 6, 1, 7),
    _Hh3cPfilter2ApplySequence_Type()
)
hh3cPfilter2ApplySequence.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cPfilter2ApplySequence.setStatus("current")


class _Hh3cPfilter2ApplyCountClear_Type(CounterClear):
    """Custom type hh3cPfilter2ApplyCountClear based on CounterClear"""
    defaultValue = 2


_Hh3cPfilter2ApplyCountClear_Type.__name__ = "CounterClear"
_Hh3cPfilter2ApplyCountClear_Object = MibTableColumn
hh3cPfilter2ApplyCountClear = _Hh3cPfilter2ApplyCountClear_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 3, 6, 1, 8),
    _Hh3cPfilter2ApplyCountClear_Type()
)
hh3cPfilter2ApplyCountClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cPfilter2ApplyCountClear.setStatus("current")
_Hh3cPfilter2ApplyRowStatus_Type = RowStatus
_Hh3cPfilter2ApplyRowStatus_Object = MibTableColumn
hh3cPfilter2ApplyRowStatus = _Hh3cPfilter2ApplyRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 3, 6, 1, 9),
    _Hh3cPfilter2ApplyRowStatus_Type()
)
hh3cPfilter2ApplyRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cPfilter2ApplyRowStatus.setStatus("current")
_Hh3cPfilter2AclGroupRunInfoTable_Object = MibTable
hh3cPfilter2AclGroupRunInfoTable = _Hh3cPfilter2AclGroupRunInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 3, 7)
)
if mibBuilder.loadTexts:
    hh3cPfilter2AclGroupRunInfoTable.setStatus("current")
_Hh3cPfilter2AclGroupRunInfoEntry_Object = MibTableRow
hh3cPfilter2AclGroupRunInfoEntry = _Hh3cPfilter2AclGroupRunInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 3, 7, 1)
)
hh3cPfilter2AclGroupRunInfoEntry.setIndexNames(
    (0, "HH3C-ACL-MIB", "hh3cPfilter2RunApplyObjType"),
    (0, "HH3C-ACL-MIB", "hh3cPfilter2RunApplyObjIndex"),
    (0, "HH3C-ACL-MIB", "hh3cPfilter2RunApplyDirection"),
    (0, "HH3C-ACL-MIB", "hh3cPfilter2RunApplyAclType"),
    (0, "HH3C-ACL-MIB", "hh3cPfilter2RunApplyAclIndex"),
)
if mibBuilder.loadTexts:
    hh3cPfilter2AclGroupRunInfoEntry.setStatus("current")


class _Hh3cPfilter2RunApplyObjType_Type(Integer32):
    """Custom type hh3cPfilter2RunApplyObjType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("interface", 1),
          ("vlan", 2),
          ("global", 3))
    )


_Hh3cPfilter2RunApplyObjType_Type.__name__ = "Integer32"
_Hh3cPfilter2RunApplyObjType_Object = MibTableColumn
hh3cPfilter2RunApplyObjType = _Hh3cPfilter2RunApplyObjType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 3, 7, 1, 1),
    _Hh3cPfilter2RunApplyObjType_Type()
)
hh3cPfilter2RunApplyObjType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cPfilter2RunApplyObjType.setStatus("current")


class _Hh3cPfilter2RunApplyObjIndex_Type(Integer32):
    """Custom type hh3cPfilter2RunApplyObjIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_Hh3cPfilter2RunApplyObjIndex_Type.__name__ = "Integer32"
_Hh3cPfilter2RunApplyObjIndex_Object = MibTableColumn
hh3cPfilter2RunApplyObjIndex = _Hh3cPfilter2RunApplyObjIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 3, 7, 1, 2),
    _Hh3cPfilter2RunApplyObjIndex_Type()
)
hh3cPfilter2RunApplyObjIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cPfilter2RunApplyObjIndex.setStatus("current")
_Hh3cPfilter2RunApplyDirection_Type = DirectionType
_Hh3cPfilter2RunApplyDirection_Object = MibTableColumn
hh3cPfilter2RunApplyDirection = _Hh3cPfilter2RunApplyDirection_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 3, 7, 1, 3),
    _Hh3cPfilter2RunApplyDirection_Type()
)
hh3cPfilter2RunApplyDirection.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cPfilter2RunApplyDirection.setStatus("current")


class _Hh3cPfilter2RunApplyAclType_Type(Integer32):
    """Custom type hh3cPfilter2RunApplyAclType based on Integer32"""
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
        *(("ipv4", 1),
          ("ipv6", 2),
          ("default", 3),
          ("mac", 4),
          ("user", 5))
    )


_Hh3cPfilter2RunApplyAclType_Type.__name__ = "Integer32"
_Hh3cPfilter2RunApplyAclType_Object = MibTableColumn
hh3cPfilter2RunApplyAclType = _Hh3cPfilter2RunApplyAclType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 3, 7, 1, 4),
    _Hh3cPfilter2RunApplyAclType_Type()
)
hh3cPfilter2RunApplyAclType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cPfilter2RunApplyAclType.setStatus("current")


class _Hh3cPfilter2RunApplyAclIndex_Type(OctetString):
    """Custom type hh3cPfilter2RunApplyAclIndex based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 63),
    )


_Hh3cPfilter2RunApplyAclIndex_Type.__name__ = "OctetString"
_Hh3cPfilter2RunApplyAclIndex_Object = MibTableColumn
hh3cPfilter2RunApplyAclIndex = _Hh3cPfilter2RunApplyAclIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 3, 7, 1, 5),
    _Hh3cPfilter2RunApplyAclIndex_Type()
)
hh3cPfilter2RunApplyAclIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cPfilter2RunApplyAclIndex.setStatus("current")


class _Hh3cPfilter2AclGroupStatus_Type(Integer32):
    """Custom type hh3cPfilter2AclGroupStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("success", 1),
          ("failed", 2),
          ("partialSuccess", 3))
    )


_Hh3cPfilter2AclGroupStatus_Type.__name__ = "Integer32"
_Hh3cPfilter2AclGroupStatus_Object = MibTableColumn
hh3cPfilter2AclGroupStatus = _Hh3cPfilter2AclGroupStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 3, 7, 1, 6),
    _Hh3cPfilter2AclGroupStatus_Type()
)
hh3cPfilter2AclGroupStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cPfilter2AclGroupStatus.setStatus("current")


class _Hh3cPfilter2AclGroupCountStatus_Type(Integer32):
    """Custom type hh3cPfilter2AclGroupCountStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("success", 1),
          ("failed", 2),
          ("partialSuccess", 3))
    )


_Hh3cPfilter2AclGroupCountStatus_Type.__name__ = "Integer32"
_Hh3cPfilter2AclGroupCountStatus_Object = MibTableColumn
hh3cPfilter2AclGroupCountStatus = _Hh3cPfilter2AclGroupCountStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 3, 7, 1, 7),
    _Hh3cPfilter2AclGroupCountStatus_Type()
)
hh3cPfilter2AclGroupCountStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cPfilter2AclGroupCountStatus.setStatus("current")
_Hh3cPfilter2AclGroupPermitPkts_Type = Counter64
_Hh3cPfilter2AclGroupPermitPkts_Object = MibTableColumn
hh3cPfilter2AclGroupPermitPkts = _Hh3cPfilter2AclGroupPermitPkts_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 3, 7, 1, 8),
    _Hh3cPfilter2AclGroupPermitPkts_Type()
)
hh3cPfilter2AclGroupPermitPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cPfilter2AclGroupPermitPkts.setStatus("current")
_Hh3cPfilter2AclGroupPermitBytes_Type = Counter64
_Hh3cPfilter2AclGroupPermitBytes_Object = MibTableColumn
hh3cPfilter2AclGroupPermitBytes = _Hh3cPfilter2AclGroupPermitBytes_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 3, 7, 1, 9),
    _Hh3cPfilter2AclGroupPermitBytes_Type()
)
hh3cPfilter2AclGroupPermitBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cPfilter2AclGroupPermitBytes.setStatus("current")
_Hh3cPfilter2AclGroupDenyPkts_Type = Counter64
_Hh3cPfilter2AclGroupDenyPkts_Object = MibTableColumn
hh3cPfilter2AclGroupDenyPkts = _Hh3cPfilter2AclGroupDenyPkts_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 3, 7, 1, 10),
    _Hh3cPfilter2AclGroupDenyPkts_Type()
)
hh3cPfilter2AclGroupDenyPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cPfilter2AclGroupDenyPkts.setStatus("current")
_Hh3cPfilter2AclGroupDenyBytes_Type = Counter64
_Hh3cPfilter2AclGroupDenyBytes_Object = MibTableColumn
hh3cPfilter2AclGroupDenyBytes = _Hh3cPfilter2AclGroupDenyBytes_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 3, 7, 1, 11),
    _Hh3cPfilter2AclGroupDenyBytes_Type()
)
hh3cPfilter2AclGroupDenyBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cPfilter2AclGroupDenyBytes.setStatus("current")
_Hh3cPfilter2AclRuleRunInfoTable_Object = MibTable
hh3cPfilter2AclRuleRunInfoTable = _Hh3cPfilter2AclRuleRunInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 3, 8)
)
if mibBuilder.loadTexts:
    hh3cPfilter2AclRuleRunInfoTable.setStatus("current")
_Hh3cPfilter2AclRuleRunInfoEntry_Object = MibTableRow
hh3cPfilter2AclRuleRunInfoEntry = _Hh3cPfilter2AclRuleRunInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 3, 8, 1)
)
hh3cPfilter2AclRuleRunInfoEntry.setIndexNames(
    (0, "HH3C-ACL-MIB", "hh3cPfilter2RunApplyObjType"),
    (0, "HH3C-ACL-MIB", "hh3cPfilter2RunApplyObjIndex"),
    (0, "HH3C-ACL-MIB", "hh3cPfilter2RunApplyDirection"),
    (0, "HH3C-ACL-MIB", "hh3cPfilter2RunApplyAclType"),
    (0, "HH3C-ACL-MIB", "hh3cPfilter2RunApplyAclIndex"),
    (0, "HH3C-ACL-MIB", "hh3cPfilter2AclRuleIndex"),
)
if mibBuilder.loadTexts:
    hh3cPfilter2AclRuleRunInfoEntry.setStatus("current")


class _Hh3cPfilter2AclRuleIndex_Type(Integer32):
    """Custom type hh3cPfilter2AclRuleIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65534),
    )


_Hh3cPfilter2AclRuleIndex_Type.__name__ = "Integer32"
_Hh3cPfilter2AclRuleIndex_Object = MibTableColumn
hh3cPfilter2AclRuleIndex = _Hh3cPfilter2AclRuleIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 3, 8, 1, 1),
    _Hh3cPfilter2AclRuleIndex_Type()
)
hh3cPfilter2AclRuleIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cPfilter2AclRuleIndex.setStatus("current")


class _Hh3cPfilter2AclRuleStatus_Type(Integer32):
    """Custom type hh3cPfilter2AclRuleStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("success", 1),
          ("failed", 2),
          ("partialSuccess", 3))
    )


_Hh3cPfilter2AclRuleStatus_Type.__name__ = "Integer32"
_Hh3cPfilter2AclRuleStatus_Object = MibTableColumn
hh3cPfilter2AclRuleStatus = _Hh3cPfilter2AclRuleStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 3, 8, 1, 2),
    _Hh3cPfilter2AclRuleStatus_Type()
)
hh3cPfilter2AclRuleStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cPfilter2AclRuleStatus.setStatus("current")


class _Hh3cPfilter2AclRuleCountStatus_Type(Integer32):
    """Custom type hh3cPfilter2AclRuleCountStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("success", 1),
          ("failed", 2),
          ("partialSuccess", 3))
    )


_Hh3cPfilter2AclRuleCountStatus_Type.__name__ = "Integer32"
_Hh3cPfilter2AclRuleCountStatus_Object = MibTableColumn
hh3cPfilter2AclRuleCountStatus = _Hh3cPfilter2AclRuleCountStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 3, 8, 1, 3),
    _Hh3cPfilter2AclRuleCountStatus_Type()
)
hh3cPfilter2AclRuleCountStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cPfilter2AclRuleCountStatus.setStatus("current")
_Hh3cPfilter2AclRuleMatchPackets_Type = Counter64
_Hh3cPfilter2AclRuleMatchPackets_Object = MibTableColumn
hh3cPfilter2AclRuleMatchPackets = _Hh3cPfilter2AclRuleMatchPackets_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 3, 8, 1, 4),
    _Hh3cPfilter2AclRuleMatchPackets_Type()
)
hh3cPfilter2AclRuleMatchPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cPfilter2AclRuleMatchPackets.setStatus("current")
_Hh3cPfilter2AclRuleMatchBytes_Type = Counter64
_Hh3cPfilter2AclRuleMatchBytes_Object = MibTableColumn
hh3cPfilter2AclRuleMatchBytes = _Hh3cPfilter2AclRuleMatchBytes_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 3, 8, 1, 5),
    _Hh3cPfilter2AclRuleMatchBytes_Type()
)
hh3cPfilter2AclRuleMatchBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cPfilter2AclRuleMatchBytes.setStatus("current")
_Hh3cPfilter2StatisticSumTable_Object = MibTable
hh3cPfilter2StatisticSumTable = _Hh3cPfilter2StatisticSumTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 3, 9)
)
if mibBuilder.loadTexts:
    hh3cPfilter2StatisticSumTable.setStatus("current")
_Hh3cPfilter2StatisticSumEntry_Object = MibTableRow
hh3cPfilter2StatisticSumEntry = _Hh3cPfilter2StatisticSumEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 3, 9, 1)
)
hh3cPfilter2StatisticSumEntry.setIndexNames(
    (0, "HH3C-ACL-MIB", "hh3cPfilter2SumDirection"),
    (0, "HH3C-ACL-MIB", "hh3cPfilter2SumAclType"),
    (0, "HH3C-ACL-MIB", "hh3cPfilter2SumAclIndex"),
    (0, "HH3C-ACL-MIB", "hh3cPfilter2SumRuleIndex"),
)
if mibBuilder.loadTexts:
    hh3cPfilter2StatisticSumEntry.setStatus("current")
_Hh3cPfilter2SumDirection_Type = DirectionType
_Hh3cPfilter2SumDirection_Object = MibTableColumn
hh3cPfilter2SumDirection = _Hh3cPfilter2SumDirection_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 3, 9, 1, 1),
    _Hh3cPfilter2SumDirection_Type()
)
hh3cPfilter2SumDirection.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cPfilter2SumDirection.setStatus("current")


class _Hh3cPfilter2SumAclType_Type(Integer32):
    """Custom type hh3cPfilter2SumAclType based on Integer32"""
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
        *(("ipv4", 1),
          ("ipv6", 2),
          ("mac", 3),
          ("user", 4))
    )


_Hh3cPfilter2SumAclType_Type.__name__ = "Integer32"
_Hh3cPfilter2SumAclType_Object = MibTableColumn
hh3cPfilter2SumAclType = _Hh3cPfilter2SumAclType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 3, 9, 1, 2),
    _Hh3cPfilter2SumAclType_Type()
)
hh3cPfilter2SumAclType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cPfilter2SumAclType.setStatus("current")


class _Hh3cPfilter2SumAclIndex_Type(OctetString):
    """Custom type hh3cPfilter2SumAclIndex based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 63),
    )


_Hh3cPfilter2SumAclIndex_Type.__name__ = "OctetString"
_Hh3cPfilter2SumAclIndex_Object = MibTableColumn
hh3cPfilter2SumAclIndex = _Hh3cPfilter2SumAclIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 3, 9, 1, 3),
    _Hh3cPfilter2SumAclIndex_Type()
)
hh3cPfilter2SumAclIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cPfilter2SumAclIndex.setStatus("current")


class _Hh3cPfilter2SumRuleIndex_Type(Integer32):
    """Custom type hh3cPfilter2SumRuleIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65534),
    )


_Hh3cPfilter2SumRuleIndex_Type.__name__ = "Integer32"
_Hh3cPfilter2SumRuleIndex_Object = MibTableColumn
hh3cPfilter2SumRuleIndex = _Hh3cPfilter2SumRuleIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 3, 9, 1, 4),
    _Hh3cPfilter2SumRuleIndex_Type()
)
hh3cPfilter2SumRuleIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cPfilter2SumRuleIndex.setStatus("current")
_Hh3cPfilter2SumRuleMatchPackets_Type = Counter64
_Hh3cPfilter2SumRuleMatchPackets_Object = MibTableColumn
hh3cPfilter2SumRuleMatchPackets = _Hh3cPfilter2SumRuleMatchPackets_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 3, 9, 1, 5),
    _Hh3cPfilter2SumRuleMatchPackets_Type()
)
hh3cPfilter2SumRuleMatchPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cPfilter2SumRuleMatchPackets.setStatus("current")
_Hh3cPfilter2SumRuleMatchBytes_Type = Counter64
_Hh3cPfilter2SumRuleMatchBytes_Object = MibTableColumn
hh3cPfilter2SumRuleMatchBytes = _Hh3cPfilter2SumRuleMatchBytes_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 3, 9, 1, 6),
    _Hh3cPfilter2SumRuleMatchBytes_Type()
)
hh3cPfilter2SumRuleMatchBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cPfilter2SumRuleMatchBytes.setStatus("current")
_Hh3cAclPacketfilterTrapObjects_ObjectIdentity = ObjectIdentity
hh3cAclPacketfilterTrapObjects = _Hh3cAclPacketfilterTrapObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 4)
)
_Hh3cPfilterInterface_Type = OctetString
_Hh3cPfilterInterface_Object = MibScalar
hh3cPfilterInterface = _Hh3cPfilterInterface_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 4, 1),
    _Hh3cPfilterInterface_Type()
)
hh3cPfilterInterface.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cPfilterInterface.setStatus("current")


class _Hh3cPfilterDirection_Type(OctetString):
    """Custom type hh3cPfilterDirection based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_Hh3cPfilterDirection_Type.__name__ = "OctetString"
_Hh3cPfilterDirection_Object = MibScalar
hh3cPfilterDirection = _Hh3cPfilterDirection_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 4, 2),
    _Hh3cPfilterDirection_Type()
)
hh3cPfilterDirection.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cPfilterDirection.setStatus("current")
_Hh3cPfilterACLNumber_Type = Integer32
_Hh3cPfilterACLNumber_Object = MibScalar
hh3cPfilterACLNumber = _Hh3cPfilterACLNumber_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 4, 3),
    _Hh3cPfilterACLNumber_Type()
)
hh3cPfilterACLNumber.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cPfilterACLNumber.setStatus("current")


class _Hh3cPfilterAction_Type(OctetString):
    """Custom type hh3cPfilterAction based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_Hh3cPfilterAction_Type.__name__ = "OctetString"
_Hh3cPfilterAction_Object = MibScalar
hh3cPfilterAction = _Hh3cPfilterAction_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 4, 4),
    _Hh3cPfilterAction_Type()
)
hh3cPfilterAction.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cPfilterAction.setStatus("current")


class _Hh3cMACfilterSourceMac_Type(OctetString):
    """Custom type hh3cMACfilterSourceMac based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_Hh3cMACfilterSourceMac_Type.__name__ = "OctetString"
_Hh3cMACfilterSourceMac_Object = MibScalar
hh3cMACfilterSourceMac = _Hh3cMACfilterSourceMac_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 4, 5),
    _Hh3cMACfilterSourceMac_Type()
)
hh3cMACfilterSourceMac.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cMACfilterSourceMac.setStatus("current")


class _Hh3cMACfilterDestinationMac_Type(OctetString):
    """Custom type hh3cMACfilterDestinationMac based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_Hh3cMACfilterDestinationMac_Type.__name__ = "OctetString"
_Hh3cMACfilterDestinationMac_Object = MibScalar
hh3cMACfilterDestinationMac = _Hh3cMACfilterDestinationMac_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 4, 6),
    _Hh3cMACfilterDestinationMac_Type()
)
hh3cMACfilterDestinationMac.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cMACfilterDestinationMac.setStatus("current")
_Hh3cPfilterPacketNumber_Type = Integer32
_Hh3cPfilterPacketNumber_Object = MibScalar
hh3cPfilterPacketNumber = _Hh3cPfilterPacketNumber_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 4, 7),
    _Hh3cPfilterPacketNumber_Type()
)
hh3cPfilterPacketNumber.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cPfilterPacketNumber.setStatus("current")


class _Hh3cPfilterReceiveInterface_Type(OctetString):
    """Custom type hh3cPfilterReceiveInterface based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_Hh3cPfilterReceiveInterface_Type.__name__ = "OctetString"
_Hh3cPfilterReceiveInterface_Object = MibScalar
hh3cPfilterReceiveInterface = _Hh3cPfilterReceiveInterface_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 4, 8),
    _Hh3cPfilterReceiveInterface_Type()
)
hh3cPfilterReceiveInterface.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cPfilterReceiveInterface.setStatus("current")


class _Hh3cAclPacketIfName_Type(OctetString):
    """Custom type hh3cAclPacketIfName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_Hh3cAclPacketIfName_Type.__name__ = "OctetString"
_Hh3cAclPacketIfName_Object = MibScalar
hh3cAclPacketIfName = _Hh3cAclPacketIfName_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 4, 9),
    _Hh3cAclPacketIfName_Type()
)
hh3cAclPacketIfName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cAclPacketIfName.setStatus("current")
_Hh3cAclPacketDirection_Type = DirectionType
_Hh3cAclPacketDirection_Object = MibScalar
hh3cAclPacketDirection = _Hh3cAclPacketDirection_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 4, 10),
    _Hh3cAclPacketDirection_Type()
)
hh3cAclPacketDirection.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cAclPacketDirection.setStatus("current")


class _Hh3cAclPacketBAGG_Type(Integer32):
    """Custom type hh3cAclPacketBAGG based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2048),
    )


_Hh3cAclPacketBAGG_Type.__name__ = "Integer32"
_Hh3cAclPacketBAGG_Object = MibScalar
hh3cAclPacketBAGG = _Hh3cAclPacketBAGG_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 4, 11),
    _Hh3cAclPacketBAGG_Type()
)
hh3cAclPacketBAGG.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cAclPacketBAGG.setStatus("current")


class _Hh3cAclPacketVlanID_Type(Integer32):
    """Custom type hh3cAclPacketVlanID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_Hh3cAclPacketVlanID_Type.__name__ = "Integer32"
_Hh3cAclPacketVlanID_Object = MibScalar
hh3cAclPacketVlanID = _Hh3cAclPacketVlanID_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 4, 12),
    _Hh3cAclPacketVlanID_Type()
)
hh3cAclPacketVlanID.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cAclPacketVlanID.setStatus("current")


class _Hh3cAclPacketSrcIP_Type(OctetString):
    """Custom type hh3cAclPacketSrcIP based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_Hh3cAclPacketSrcIP_Type.__name__ = "OctetString"
_Hh3cAclPacketSrcIP_Object = MibScalar
hh3cAclPacketSrcIP = _Hh3cAclPacketSrcIP_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 4, 13),
    _Hh3cAclPacketSrcIP_Type()
)
hh3cAclPacketSrcIP.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cAclPacketSrcIP.setStatus("current")


class _Hh3cAclPacketDstIP_Type(OctetString):
    """Custom type hh3cAclPacketDstIP based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_Hh3cAclPacketDstIP_Type.__name__ = "OctetString"
_Hh3cAclPacketDstIP_Object = MibScalar
hh3cAclPacketDstIP = _Hh3cAclPacketDstIP_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 4, 14),
    _Hh3cAclPacketDstIP_Type()
)
hh3cAclPacketDstIP.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cAclPacketDstIP.setStatus("current")


class _Hh3cAclPacketProtocol_Type(Integer32):
    """Custom type hh3cAclPacketProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_Hh3cAclPacketProtocol_Type.__name__ = "Integer32"
_Hh3cAclPacketProtocol_Object = MibScalar
hh3cAclPacketProtocol = _Hh3cAclPacketProtocol_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 4, 15),
    _Hh3cAclPacketProtocol_Type()
)
hh3cAclPacketProtocol.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cAclPacketProtocol.setStatus("current")


class _Hh3cAclPacketDscp_Type(DSCPValue):
    """Custom type hh3cAclPacketDscp based on DSCPValue"""
    defaultValue = 255


_Hh3cAclPacketDscp_Type.__name__ = "DSCPValue"
_Hh3cAclPacketDscp_Object = MibScalar
hh3cAclPacketDscp = _Hh3cAclPacketDscp_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 4, 16),
    _Hh3cAclPacketDscp_Type()
)
hh3cAclPacketDscp.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cAclPacketDscp.setStatus("current")


class _Hh3cAclPacketFlowLabel_Type(Unsigned32):
    """Custom type hh3cAclPacketFlowLabel based on Unsigned32"""
    defaultValue = 4294967295

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1048575),
        ValueRangeConstraint(4294967295, 4294967295),
    )


_Hh3cAclPacketFlowLabel_Type.__name__ = "Unsigned32"
_Hh3cAclPacketFlowLabel_Object = MibScalar
hh3cAclPacketFlowLabel = _Hh3cAclPacketFlowLabel_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 4, 17),
    _Hh3cAclPacketFlowLabel_Type()
)
hh3cAclPacketFlowLabel.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cAclPacketFlowLabel.setStatus("current")


class _Hh3cAclPacketIcmpIgmpType_Type(Integer32):
    """Custom type hh3cAclPacketIcmpIgmpType based on Integer32"""
    defaultValue = 65535

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
        ValueRangeConstraint(65535, 65535),
    )


_Hh3cAclPacketIcmpIgmpType_Type.__name__ = "Integer32"
_Hh3cAclPacketIcmpIgmpType_Object = MibScalar
hh3cAclPacketIcmpIgmpType = _Hh3cAclPacketIcmpIgmpType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 4, 18),
    _Hh3cAclPacketIcmpIgmpType_Type()
)
hh3cAclPacketIcmpIgmpType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cAclPacketIcmpIgmpType.setStatus("current")


class _Hh3cAclPacketIcmpIgmpCode_Type(Integer32):
    """Custom type hh3cAclPacketIcmpIgmpCode based on Integer32"""
    defaultValue = 65535

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
        ValueRangeConstraint(65535, 65535),
    )


_Hh3cAclPacketIcmpIgmpCode_Type.__name__ = "Integer32"
_Hh3cAclPacketIcmpIgmpCode_Object = MibScalar
hh3cAclPacketIcmpIgmpCode = _Hh3cAclPacketIcmpIgmpCode_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 4, 19),
    _Hh3cAclPacketIcmpIgmpCode_Type()
)
hh3cAclPacketIcmpIgmpCode.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cAclPacketIcmpIgmpCode.setStatus("current")


class _Hh3cAclPacketTcpFlags_Type(Integer32):
    """Custom type hh3cAclPacketTcpFlags based on Integer32"""
    defaultValue = 255

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              255)
        )
    )
    namedValues = NamedValues(
        *(("tcpack", 1),
          ("tcpfin", 2),
          ("tcppsh", 3),
          ("tcprst", 4),
          ("tcpsyn", 5),
          ("tcpurg", 6),
          ("invalid", 255))
    )


_Hh3cAclPacketTcpFlags_Type.__name__ = "Integer32"
_Hh3cAclPacketTcpFlags_Object = MibScalar
hh3cAclPacketTcpFlags = _Hh3cAclPacketTcpFlags_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 4, 20),
    _Hh3cAclPacketTcpFlags_Type()
)
hh3cAclPacketTcpFlags.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cAclPacketTcpFlags.setStatus("current")


class _Hh3cAclPacketSrcPort_Type(Integer32):
    """Custom type hh3cAclPacketSrcPort based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Hh3cAclPacketSrcPort_Type.__name__ = "Integer32"
_Hh3cAclPacketSrcPort_Object = MibScalar
hh3cAclPacketSrcPort = _Hh3cAclPacketSrcPort_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 4, 21),
    _Hh3cAclPacketSrcPort_Type()
)
hh3cAclPacketSrcPort.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cAclPacketSrcPort.setStatus("current")


class _Hh3cAclPacketDstPort_Type(Integer32):
    """Custom type hh3cAclPacketDstPort based on Integer32"""
    defaultValue = 65535

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Hh3cAclPacketDstPort_Type.__name__ = "Integer32"
_Hh3cAclPacketDstPort_Object = MibScalar
hh3cAclPacketDstPort = _Hh3cAclPacketDstPort_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 4, 22),
    _Hh3cAclPacketDstPort_Type()
)
hh3cAclPacketDstPort.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cAclPacketDstPort.setStatus("current")
_Hh3cAclPacketSrcMacAddr_Type = MacAddress
_Hh3cAclPacketSrcMacAddr_Object = MibScalar
hh3cAclPacketSrcMacAddr = _Hh3cAclPacketSrcMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 4, 23),
    _Hh3cAclPacketSrcMacAddr_Type()
)
hh3cAclPacketSrcMacAddr.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cAclPacketSrcMacAddr.setStatus("current")
_Hh3cAclPacketDstMacAddr_Type = MacAddress
_Hh3cAclPacketDstMacAddr_Object = MibScalar
hh3cAclPacketDstMacAddr = _Hh3cAclPacketDstMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 4, 24),
    _Hh3cAclPacketDstMacAddr_Type()
)
hh3cAclPacketDstMacAddr.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cAclPacketDstMacAddr.setStatus("current")


class _Hh3cAclPacketMacTypeLen_Type(Integer32):
    """Custom type hh3cAclPacketMacTypeLen based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Hh3cAclPacketMacTypeLen_Type.__name__ = "Integer32"
_Hh3cAclPacketMacTypeLen_Object = MibScalar
hh3cAclPacketMacTypeLen = _Hh3cAclPacketMacTypeLen_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 4, 25),
    _Hh3cAclPacketMacTypeLen_Type()
)
hh3cAclPacketMacTypeLen.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cAclPacketMacTypeLen.setStatus("current")


class _Hh3cAclPacketVlanPCP_Type(Integer32):
    """Custom type hh3cAclPacketVlanPCP based on Integer32"""
    defaultValue = 255

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
        ValueRangeConstraint(255, 255),
    )


_Hh3cAclPacketVlanPCP_Type.__name__ = "Integer32"
_Hh3cAclPacketVlanPCP_Object = MibScalar
hh3cAclPacketVlanPCP = _Hh3cAclPacketVlanPCP_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 4, 26),
    _Hh3cAclPacketVlanPCP_Type()
)
hh3cAclPacketVlanPCP.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cAclPacketVlanPCP.setStatus("current")
_Hh3cAclPacketfilterTrap_ObjectIdentity = ObjectIdentity
hh3cAclPacketfilterTrap = _Hh3cAclPacketfilterTrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 5)
)
_Hh3cPfilterTrapPrefix_ObjectIdentity = ObjectIdentity
hh3cPfilterTrapPrefix = _Hh3cPfilterTrapPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 5, 0)
)
_Hh3cAclTrapObjects_ObjectIdentity = ObjectIdentity
hh3cAclTrapObjects = _Hh3cAclTrapObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 6)
)


class _Hh3cAclResourceTypeName_Type(OctetString):
    """Custom type hh3cAclResourceTypeName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_Hh3cAclResourceTypeName_Type.__name__ = "OctetString"
_Hh3cAclResourceTypeName_Object = MibScalar
hh3cAclResourceTypeName = _Hh3cAclResourceTypeName_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 6, 1),
    _Hh3cAclResourceTypeName_Type()
)
hh3cAclResourceTypeName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cAclResourceTypeName.setStatus("current")


class _Hh3cAclResourceUsage_Type(Integer32):
    """Custom type hh3cAclResourceUsage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_Hh3cAclResourceUsage_Type.__name__ = "Integer32"
_Hh3cAclResourceUsage_Object = MibScalar
hh3cAclResourceUsage = _Hh3cAclResourceUsage_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 6, 2),
    _Hh3cAclResourceUsage_Type()
)
hh3cAclResourceUsage.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cAclResourceUsage.setStatus("current")
_Hh3cAclResourceUsedEntries_Type = Integer32
_Hh3cAclResourceUsedEntries_Object = MibScalar
hh3cAclResourceUsedEntries = _Hh3cAclResourceUsedEntries_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 6, 3),
    _Hh3cAclResourceUsedEntries_Type()
)
hh3cAclResourceUsedEntries.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cAclResourceUsedEntries.setStatus("current")
_Hh3cAclResourceTotalEntries_Type = Integer32
_Hh3cAclResourceTotalEntries_Object = MibScalar
hh3cAclResourceTotalEntries = _Hh3cAclResourceTotalEntries_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 6, 4),
    _Hh3cAclResourceTotalEntries_Type()
)
hh3cAclResourceTotalEntries.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cAclResourceTotalEntries.setStatus("current")
_Hh3cAclResourceChassisID_Type = Integer32
_Hh3cAclResourceChassisID_Object = MibScalar
hh3cAclResourceChassisID = _Hh3cAclResourceChassisID_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 6, 5),
    _Hh3cAclResourceChassisID_Type()
)
hh3cAclResourceChassisID.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cAclResourceChassisID.setStatus("current")
_Hh3cAclResourceSlotID_Type = Integer32
_Hh3cAclResourceSlotID_Object = MibScalar
hh3cAclResourceSlotID = _Hh3cAclResourceSlotID_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 6, 6),
    _Hh3cAclResourceSlotID_Type()
)
hh3cAclResourceSlotID.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cAclResourceSlotID.setStatus("current")
_Hh3cAclTrap_ObjectIdentity = ObjectIdentity
hh3cAclTrap = _Hh3cAclTrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 7)
)
_Hh3cAclTrapPrefix_ObjectIdentity = ObjectIdentity
hh3cAclTrapPrefix = _Hh3cAclTrapPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 7, 0)
)

# Managed Objects groups


# Notification objects

hh3cMACfilterTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 5, 0, 1)
)
hh3cMACfilterTrap.setObjects(
      *(("HH3C-ACL-MIB", "hh3cPfilterInterface"),
        ("HH3C-ACL-MIB", "hh3cPfilterDirection"),
        ("HH3C-ACL-MIB", "hh3cPfilterACLNumber"),
        ("HH3C-ACL-MIB", "hh3cPfilterAction"),
        ("HH3C-ACL-MIB", "hh3cMACfilterSourceMac"),
        ("HH3C-ACL-MIB", "hh3cMACfilterDestinationMac"),
        ("HH3C-ACL-MIB", "hh3cPfilterPacketNumber"),
        ("HH3C-ACL-MIB", "hh3cPfilterReceiveInterface"))
)
if mibBuilder.loadTexts:
    hh3cMACfilterTrap.setStatus(
        "current"
    )

hh3cAclRuleMatchCount = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 5, 0, 2)
)
hh3cAclRuleMatchCount.setObjects(
      *(("HH3C-ACL-MIB", "hh3cPfilter2ApplyObjType"),
        ("HH3C-ACL-MIB", "hh3cPfilter2ApplyObjIndex"),
        ("HH3C-ACL-MIB", "hh3cPfilter2ApplyDirection"),
        ("HH3C-ACL-MIB", "hh3cPfilter2ApplyAclType"),
        ("HH3C-ACL-MIB", "hh3cPfilter2ApplyAclIndex"),
        ("HH3C-ACL-MIB", "hh3cPfilter2AclRuleIndex"),
        ("HH3C-ACL-MIB", "hh3cPfilter2AclRuleMatchPackets"))
)
if mibBuilder.loadTexts:
    hh3cAclRuleMatchCount.setStatus(
        "current"
    )

hh3cAclFirstIPv4PktCaptured = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 5, 0, 3)
)
hh3cAclFirstIPv4PktCaptured.setObjects(
      *(("HH3C-ACL-MIB", "hh3cPfilter2ApplyAclIndex"),
        ("HH3C-ACL-MIB", "hh3cPfilter2AclRuleIndex"),
        ("HH3C-ACL-MIB", "hh3cAclPacketIfName"),
        ("HH3C-ACL-MIB", "hh3cAclPacketDirection"),
        ("HH3C-ACL-MIB", "hh3cAclPacketBAGG"),
        ("HH3C-ACL-MIB", "hh3cAclPacketVlanID"),
        ("HH3C-ACL-MIB", "hh3cAclPacketSrcIP"),
        ("HH3C-ACL-MIB", "hh3cAclPacketDstIP"),
        ("HH3C-ACL-MIB", "hh3cAclPacketProtocol"),
        ("HH3C-ACL-MIB", "hh3cAclPacketDscp"),
        ("HH3C-ACL-MIB", "hh3cAclPacketIcmpIgmpType"),
        ("HH3C-ACL-MIB", "hh3cAclPacketIcmpIgmpCode"),
        ("HH3C-ACL-MIB", "hh3cAclPacketTcpFlags"),
        ("HH3C-ACL-MIB", "hh3cAclPacketSrcPort"),
        ("HH3C-ACL-MIB", "hh3cAclPacketDstPort"))
)
if mibBuilder.loadTexts:
    hh3cAclFirstIPv4PktCaptured.setStatus(
        "current"
    )

hh3cAclFirstIPv6PktCaptured = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 5, 0, 4)
)
hh3cAclFirstIPv6PktCaptured.setObjects(
      *(("HH3C-ACL-MIB", "hh3cPfilter2ApplyAclIndex"),
        ("HH3C-ACL-MIB", "hh3cPfilter2AclRuleIndex"),
        ("HH3C-ACL-MIB", "hh3cAclPacketIfName"),
        ("HH3C-ACL-MIB", "hh3cAclPacketDirection"),
        ("HH3C-ACL-MIB", "hh3cAclPacketBAGG"),
        ("HH3C-ACL-MIB", "hh3cAclPacketVlanID"),
        ("HH3C-ACL-MIB", "hh3cAclPacketSrcIP"),
        ("HH3C-ACL-MIB", "hh3cAclPacketDstIP"),
        ("HH3C-ACL-MIB", "hh3cAclPacketProtocol"),
        ("HH3C-ACL-MIB", "hh3cAclPacketDscp"),
        ("HH3C-ACL-MIB", "hh3cAclPacketFlowLabel"),
        ("HH3C-ACL-MIB", "hh3cAclPacketIcmpIgmpType"),
        ("HH3C-ACL-MIB", "hh3cAclPacketIcmpIgmpCode"),
        ("HH3C-ACL-MIB", "hh3cAclPacketTcpFlags"),
        ("HH3C-ACL-MIB", "hh3cAclPacketSrcPort"),
        ("HH3C-ACL-MIB", "hh3cAclPacketDstPort"))
)
if mibBuilder.loadTexts:
    hh3cAclFirstIPv6PktCaptured.setStatus(
        "current"
    )

hh3cAclFirstEthernetPktCaptured = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 5, 0, 5)
)
hh3cAclFirstEthernetPktCaptured.setObjects(
      *(("HH3C-ACL-MIB", "hh3cPfilter2ApplyAclIndex"),
        ("HH3C-ACL-MIB", "hh3cPfilter2AclRuleIndex"),
        ("HH3C-ACL-MIB", "hh3cAclPacketIfName"),
        ("HH3C-ACL-MIB", "hh3cAclPacketDirection"),
        ("HH3C-ACL-MIB", "hh3cAclPacketBAGG"),
        ("HH3C-ACL-MIB", "hh3cAclPacketVlanID"),
        ("HH3C-ACL-MIB", "hh3cAclPacketSrcMacAddr"),
        ("HH3C-ACL-MIB", "hh3cAclPacketDstMacAddr"),
        ("HH3C-ACL-MIB", "hh3cAclPacketMacTypeLen"),
        ("HH3C-ACL-MIB", "hh3cAclPacketVlanPCP"))
)
if mibBuilder.loadTexts:
    hh3cAclFirstEthernetPktCaptured.setStatus(
        "current"
    )

hh3cAclResourceTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 8, 7, 0, 1)
)
hh3cAclResourceTrap.setObjects(
      *(("HH3C-ACL-MIB", "hh3cAclResourceTypeName"),
        ("HH3C-ACL-MIB", "hh3cAclResourceUsage"),
        ("HH3C-ACL-MIB", "hh3cAclResourceUsedEntries"),
        ("HH3C-ACL-MIB", "hh3cAclResourceTotalEntries"),
        ("HH3C-ACL-MIB", "hh3cAclMib2ResourceThreshold"),
        ("HH3C-ACL-MIB", "hh3cAclResourceChassisID"),
        ("HH3C-ACL-MIB", "hh3cAclResourceSlotID"))
)
if mibBuilder.loadTexts:
    hh3cAclResourceTrap.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HH3C-ACL-MIB",
    **{"RuleAction": RuleAction,
       "CounterClear": CounterClear,
       "PortOp": PortOp,
       "DSCPValue": DSCPValue,
       "TCPFlag": TCPFlag,
       "FragmentFlag": FragmentFlag,
       "AddressFlag": AddressFlag,
       "DirectionType": DirectionType,
       "hh3cAcl": hh3cAcl,
       "hh3cAclMibObjects": hh3cAclMibObjects,
       "hh3cAclMode": hh3cAclMode,
       "hh3cAclNumGroupTable": hh3cAclNumGroupTable,
       "hh3cAclNumGroupEntry": hh3cAclNumGroupEntry,
       "hh3cAclNumGroupAclNum": hh3cAclNumGroupAclNum,
       "hh3cAclNumGroupMatchOrder": hh3cAclNumGroupMatchOrder,
       "hh3cAclNumGroupSubitemNum": hh3cAclNumGroupSubitemNum,
       "hh3cAclNumGroupDescription": hh3cAclNumGroupDescription,
       "hh3cAclNumGroupCountClear": hh3cAclNumGroupCountClear,
       "hh3cAclNumGroupRowStatus": hh3cAclNumGroupRowStatus,
       "hh3cAclNameGroupTable": hh3cAclNameGroupTable,
       "hh3cAclNameGroupEntry": hh3cAclNameGroupEntry,
       "hh3cAclNameGroupIndex": hh3cAclNameGroupIndex,
       "hh3cAclNameGroupCreateName": hh3cAclNameGroupCreateName,
       "hh3cAclNameGroupTypes": hh3cAclNameGroupTypes,
       "hh3cAclNameGroupMatchOrder": hh3cAclNameGroupMatchOrder,
       "hh3cAclNameGroupSubitemNum": hh3cAclNameGroupSubitemNum,
       "hh3cAclNameGroupRowStatus": hh3cAclNameGroupRowStatus,
       "hh3cAclBasicRuleTable": hh3cAclBasicRuleTable,
       "hh3cAclBasicRuleEntry": hh3cAclBasicRuleEntry,
       "hh3cAclBasicAclNum": hh3cAclBasicAclNum,
       "hh3cAclBasicSubitem": hh3cAclBasicSubitem,
       "hh3cAclBasicAct": hh3cAclBasicAct,
       "hh3cAclBasicSrcIp": hh3cAclBasicSrcIp,
       "hh3cAclBasicSrcWild": hh3cAclBasicSrcWild,
       "hh3cAclBasicTimeRangeName": hh3cAclBasicTimeRangeName,
       "hh3cAclBasicFragments": hh3cAclBasicFragments,
       "hh3cAclBasicLog": hh3cAclBasicLog,
       "hh3cAclBasicEnable": hh3cAclBasicEnable,
       "hh3cAclBasicCount": hh3cAclBasicCount,
       "hh3cAclBasicCountClear": hh3cAclBasicCountClear,
       "hh3cAclBasicRowStatus": hh3cAclBasicRowStatus,
       "hh3cAclAdvancedRuleTable": hh3cAclAdvancedRuleTable,
       "hh3cAclAdvancedRuleEntry": hh3cAclAdvancedRuleEntry,
       "hh3cAclAdvancedAclNum": hh3cAclAdvancedAclNum,
       "hh3cAclAdvancedSubitem": hh3cAclAdvancedSubitem,
       "hh3cAclAdvancedAct": hh3cAclAdvancedAct,
       "hh3cAclAdvancedProtocol": hh3cAclAdvancedProtocol,
       "hh3cAclAdvancedSrcIp": hh3cAclAdvancedSrcIp,
       "hh3cAclAdvancedSrcWild": hh3cAclAdvancedSrcWild,
       "hh3cAclAdvancedSrcOp": hh3cAclAdvancedSrcOp,
       "hh3cAclAdvancedSrcPort1": hh3cAclAdvancedSrcPort1,
       "hh3cAclAdvancedSrcPort2": hh3cAclAdvancedSrcPort2,
       "hh3cAclAdvancedDestIp": hh3cAclAdvancedDestIp,
       "hh3cAclAdvancedDestWild": hh3cAclAdvancedDestWild,
       "hh3cAclAdvancedDestOp": hh3cAclAdvancedDestOp,
       "hh3cAclAdvancedDestPort1": hh3cAclAdvancedDestPort1,
       "hh3cAclAdvancedDestPort2": hh3cAclAdvancedDestPort2,
       "hh3cAclAdvancedPrecedence": hh3cAclAdvancedPrecedence,
       "hh3cAclAdvancedTos": hh3cAclAdvancedTos,
       "hh3cAclAdvancedDscp": hh3cAclAdvancedDscp,
       "hh3cAclAdvancedEstablish": hh3cAclAdvancedEstablish,
       "hh3cAclAdvancedTimeRangeName": hh3cAclAdvancedTimeRangeName,
       "hh3cAclAdvancedIcmpType": hh3cAclAdvancedIcmpType,
       "hh3cAclAdvancedIcmpCode": hh3cAclAdvancedIcmpCode,
       "hh3cAclAdvancedFragments": hh3cAclAdvancedFragments,
       "hh3cAclAdvancedLog": hh3cAclAdvancedLog,
       "hh3cAclAdvancedEnable": hh3cAclAdvancedEnable,
       "hh3cAclAdvancedCount": hh3cAclAdvancedCount,
       "hh3cAclAdvancedCountClear": hh3cAclAdvancedCountClear,
       "hh3cAclAdvancedRowStatus": hh3cAclAdvancedRowStatus,
       "hh3cAclIfRuleTable": hh3cAclIfRuleTable,
       "hh3cAclIfRuleEntry": hh3cAclIfRuleEntry,
       "hh3cAclIfAclNum": hh3cAclIfAclNum,
       "hh3cAclIfSubitem": hh3cAclIfSubitem,
       "hh3cAclIfAct": hh3cAclIfAct,
       "hh3cAclIfIndex": hh3cAclIfIndex,
       "hh3cAclIfAny": hh3cAclIfAny,
       "hh3cAclIfTimeRangeName": hh3cAclIfTimeRangeName,
       "hh3cAclIfLog": hh3cAclIfLog,
       "hh3cAclIfEnable": hh3cAclIfEnable,
       "hh3cAclIfCount": hh3cAclIfCount,
       "hh3cAclIfCountClear": hh3cAclIfCountClear,
       "hh3cAclIfRowStatus": hh3cAclIfRowStatus,
       "hh3cAclLinkTable": hh3cAclLinkTable,
       "hh3cAclLinkEntry": hh3cAclLinkEntry,
       "hh3cAclLinkAclNum": hh3cAclLinkAclNum,
       "hh3cAclLinkSubitem": hh3cAclLinkSubitem,
       "hh3cAclLinkAct": hh3cAclLinkAct,
       "hh3cAclLinkProtocol": hh3cAclLinkProtocol,
       "hh3cAclLinkFormatType": hh3cAclLinkFormatType,
       "hh3cAclLinkVlanTag": hh3cAclLinkVlanTag,
       "hh3cAclLinkVlanPri": hh3cAclLinkVlanPri,
       "hh3cAclLinkSrcVlanId": hh3cAclLinkSrcVlanId,
       "hh3cAclLinkSrcMac": hh3cAclLinkSrcMac,
       "hh3cAclLinkSrcMacWild": hh3cAclLinkSrcMacWild,
       "hh3cAclLinkSrcIfIndex": hh3cAclLinkSrcIfIndex,
       "hh3cAclLinkSrcAny": hh3cAclLinkSrcAny,
       "hh3cAclLinkDestVlanId": hh3cAclLinkDestVlanId,
       "hh3cAclLinkDestMac": hh3cAclLinkDestMac,
       "hh3cAclLinkDestMacWild": hh3cAclLinkDestMacWild,
       "hh3cAclLinkDestIfIndex": hh3cAclLinkDestIfIndex,
       "hh3cAclLinkDestAny": hh3cAclLinkDestAny,
       "hh3cAclLinkTimeRangeName": hh3cAclLinkTimeRangeName,
       "hh3cAclLinkEnable": hh3cAclLinkEnable,
       "hh3cAclLinkRowStatus": hh3cAclLinkRowStatus,
       "hh3cAclLinkTypeCode": hh3cAclLinkTypeCode,
       "hh3cAclLinkTypeMask": hh3cAclLinkTypeMask,
       "hh3cAclLinkLsapCode": hh3cAclLinkLsapCode,
       "hh3cAclLinkLsapMask": hh3cAclLinkLsapMask,
       "hh3cAclLinkL2LabelRangeOp": hh3cAclLinkL2LabelRangeOp,
       "hh3cAclLinkL2LabelRangeBegin": hh3cAclLinkL2LabelRangeBegin,
       "hh3cAclLinkL2LabelRangeEnd": hh3cAclLinkL2LabelRangeEnd,
       "hh3cAclLinkMplsExp": hh3cAclLinkMplsExp,
       "hh3cAclUserTable": hh3cAclUserTable,
       "hh3cAclUserEntry": hh3cAclUserEntry,
       "hh3cAclUserAclNum": hh3cAclUserAclNum,
       "hh3cAclUserSubitem": hh3cAclUserSubitem,
       "hh3cAclUserAct": hh3cAclUserAct,
       "hh3cAclUserFormatType": hh3cAclUserFormatType,
       "hh3cAclUserVlanTag": hh3cAclUserVlanTag,
       "hh3cAclUserRuleStr": hh3cAclUserRuleStr,
       "hh3cAclUserRuleMask": hh3cAclUserRuleMask,
       "hh3cAclUserTimeRangeName": hh3cAclUserTimeRangeName,
       "hh3cAclUserEnable": hh3cAclUserEnable,
       "hh3cAclUserRowStatus": hh3cAclUserRowStatus,
       "hh3cAclActiveTable": hh3cAclActiveTable,
       "hh3cAclActiveEntry": hh3cAclActiveEntry,
       "hh3cAclActiveAclIndex": hh3cAclActiveAclIndex,
       "hh3cAclActiveIfIndex": hh3cAclActiveIfIndex,
       "hh3cAclActiveVlanID": hh3cAclActiveVlanID,
       "hh3cAclActiveDirection": hh3cAclActiveDirection,
       "hh3cAclActiveUserAclNum": hh3cAclActiveUserAclNum,
       "hh3cAclActiveUserAclSubitem": hh3cAclActiveUserAclSubitem,
       "hh3cAclActiveIpAclNum": hh3cAclActiveIpAclNum,
       "hh3cAclActiveIpAclSubitem": hh3cAclActiveIpAclSubitem,
       "hh3cAclActiveLinkAclNum": hh3cAclActiveLinkAclNum,
       "hh3cAclActiveLinkAclSubitem": hh3cAclActiveLinkAclSubitem,
       "hh3cAclActiveRuntime": hh3cAclActiveRuntime,
       "hh3cAclActiveRowStatus": hh3cAclActiveRowStatus,
       "hh3cAclIDSTable": hh3cAclIDSTable,
       "hh3cAclIDSEntry": hh3cAclIDSEntry,
       "hh3cAclIDSName": hh3cAclIDSName,
       "hh3cAclIDSSrcMac": hh3cAclIDSSrcMac,
       "hh3cAclIDSDestMac": hh3cAclIDSDestMac,
       "hh3cAclIDSSrcIp": hh3cAclIDSSrcIp,
       "hh3cAclIDSSrcWild": hh3cAclIDSSrcWild,
       "hh3cAclIDSDestIp": hh3cAclIDSDestIp,
       "hh3cAclIDSDestWild": hh3cAclIDSDestWild,
       "hh3cAclIDSSrcPort": hh3cAclIDSSrcPort,
       "hh3cAclIDSDestPort": hh3cAclIDSDestPort,
       "hh3cAclIDSProtocol": hh3cAclIDSProtocol,
       "hh3cAclIDSDenyTime": hh3cAclIDSDenyTime,
       "hh3cAclIDSAct": hh3cAclIDSAct,
       "hh3cAclIDSRowStatus": hh3cAclIDSRowStatus,
       "hh3cAclMib2Objects": hh3cAclMib2Objects,
       "hh3cAclMib2GlobalGroup": hh3cAclMib2GlobalGroup,
       "hh3cAclMib2NodesGroup": hh3cAclMib2NodesGroup,
       "hh3cAclMib2Mode": hh3cAclMib2Mode,
       "hh3cAclMib2Version": hh3cAclMib2Version,
       "hh3cAclMib2ObjectsCapabilities": hh3cAclMib2ObjectsCapabilities,
       "hh3cAclMib2ProcessingStatus": hh3cAclMib2ProcessingStatus,
       "hh3cAclMib2ResourceThreshold": hh3cAclMib2ResourceThreshold,
       "hh3cAclMib2ResourceLogInterval": hh3cAclMib2ResourceLogInterval,
       "hh3cAclMib2CapabilityTable": hh3cAclMib2CapabilityTable,
       "hh3cAclMib2CapabilityEntry": hh3cAclMib2CapabilityEntry,
       "hh3cAclMib2EntityType": hh3cAclMib2EntityType,
       "hh3cAclMib2EntityIndex": hh3cAclMib2EntityIndex,
       "hh3cAclMib2ModuleIndex": hh3cAclMib2ModuleIndex,
       "hh3cAclMib2CharacteristicsIndex": hh3cAclMib2CharacteristicsIndex,
       "hh3cAclMib2CharacteristicsDesc": hh3cAclMib2CharacteristicsDesc,
       "hh3cAclMib2CharacteristicsValue": hh3cAclMib2CharacteristicsValue,
       "hh3cAclNumberGroupTable": hh3cAclNumberGroupTable,
       "hh3cAclNumberGroupEntry": hh3cAclNumberGroupEntry,
       "hh3cAclNumberGroupType": hh3cAclNumberGroupType,
       "hh3cAclNumberGroupIndex": hh3cAclNumberGroupIndex,
       "hh3cAclNumberGroupRowStatus": hh3cAclNumberGroupRowStatus,
       "hh3cAclNumberGroupMatchOrder": hh3cAclNumberGroupMatchOrder,
       "hh3cAclNumberGroupStep": hh3cAclNumberGroupStep,
       "hh3cAclNumberGroupDescription": hh3cAclNumberGroupDescription,
       "hh3cAclNumberGroupCountClear": hh3cAclNumberGroupCountClear,
       "hh3cAclNumberGroupRuleCounter": hh3cAclNumberGroupRuleCounter,
       "hh3cAclNumberGroupName": hh3cAclNumberGroupName,
       "hh3cAclNamedGroupTable": hh3cAclNamedGroupTable,
       "hh3cAclNamedGroupEntry": hh3cAclNamedGroupEntry,
       "hh3cAclNamedGroupCategory": hh3cAclNamedGroupCategory,
       "hh3cAclNamedGroupName": hh3cAclNamedGroupName,
       "hh3cAclNamedGroupRowStatus": hh3cAclNamedGroupRowStatus,
       "hh3cAclNamedGroupMatchOrder": hh3cAclNamedGroupMatchOrder,
       "hh3cAclNamedGroupStep": hh3cAclNamedGroupStep,
       "hh3cAclNamedGroupDescription": hh3cAclNamedGroupDescription,
       "hh3cAclNamedGroupCountClear": hh3cAclNamedGroupCountClear,
       "hh3cAclNamedGroupRuleCounter": hh3cAclNamedGroupRuleCounter,
       "hh3cAclIPAclGroup": hh3cAclIPAclGroup,
       "hh3cAclIPAclBasicTable": hh3cAclIPAclBasicTable,
       "hh3cAclIPAclBasicEntry": hh3cAclIPAclBasicEntry,
       "hh3cAclIPAclBasicRuleIndex": hh3cAclIPAclBasicRuleIndex,
       "hh3cAclIPAclBasicRowStatus": hh3cAclIPAclBasicRowStatus,
       "hh3cAclIPAclBasicAct": hh3cAclIPAclBasicAct,
       "hh3cAclIPAclBasicSrcAddrType": hh3cAclIPAclBasicSrcAddrType,
       "hh3cAclIPAclBasicSrcAddr": hh3cAclIPAclBasicSrcAddr,
       "hh3cAclIPAclBasicSrcPrefix": hh3cAclIPAclBasicSrcPrefix,
       "hh3cAclIPAclBasicSrcAny": hh3cAclIPAclBasicSrcAny,
       "hh3cAclIPAclBasicSrcWild": hh3cAclIPAclBasicSrcWild,
       "hh3cAclIPAclBasicTimeRangeName": hh3cAclIPAclBasicTimeRangeName,
       "hh3cAclIPAclBasicFragmentFlag": hh3cAclIPAclBasicFragmentFlag,
       "hh3cAclIPAclBasicLog": hh3cAclIPAclBasicLog,
       "hh3cAclIPAclBasicCount": hh3cAclIPAclBasicCount,
       "hh3cAclIPAclBasicCountClear": hh3cAclIPAclBasicCountClear,
       "hh3cAclIPAclBasicEnable": hh3cAclIPAclBasicEnable,
       "hh3cAclIPAclBasicVpnInstanceName": hh3cAclIPAclBasicVpnInstanceName,
       "hh3cAclIPAclBasicComment": hh3cAclIPAclBasicComment,
       "hh3cAclIPAclBasicCounting": hh3cAclIPAclBasicCounting,
       "hh3cAclIPAclBasicRouteTypeAny": hh3cAclIPAclBasicRouteTypeAny,
       "hh3cAclIPAclBasicRouteTypeValue": hh3cAclIPAclBasicRouteTypeValue,
       "hh3cAclIPAclAdvancedTable": hh3cAclIPAclAdvancedTable,
       "hh3cAclIPAclAdvancedEntry": hh3cAclIPAclAdvancedEntry,
       "hh3cAclIPAclAdvancedRuleIndex": hh3cAclIPAclAdvancedRuleIndex,
       "hh3cAclIPAclAdvancedRowStatus": hh3cAclIPAclAdvancedRowStatus,
       "hh3cAclIPAclAdvancedAct": hh3cAclIPAclAdvancedAct,
       "hh3cAclIPAclAdvancedProtocol": hh3cAclIPAclAdvancedProtocol,
       "hh3cAclIPAclAdvancedAddrFlag": hh3cAclIPAclAdvancedAddrFlag,
       "hh3cAclIPAclAdvancedSrcAddrType": hh3cAclIPAclAdvancedSrcAddrType,
       "hh3cAclIPAclAdvancedSrcAddr": hh3cAclIPAclAdvancedSrcAddr,
       "hh3cAclIPAclAdvancedSrcPrefix": hh3cAclIPAclAdvancedSrcPrefix,
       "hh3cAclIPAclAdvancedSrcAny": hh3cAclIPAclAdvancedSrcAny,
       "hh3cAclIPAclAdvancedSrcWild": hh3cAclIPAclAdvancedSrcWild,
       "hh3cAclIPAclAdvancedSrcOp": hh3cAclIPAclAdvancedSrcOp,
       "hh3cAclIPAclAdvancedSrcPort1": hh3cAclIPAclAdvancedSrcPort1,
       "hh3cAclIPAclAdvancedSrcPort2": hh3cAclIPAclAdvancedSrcPort2,
       "hh3cAclIPAclAdvancedDestAddrType": hh3cAclIPAclAdvancedDestAddrType,
       "hh3cAclIPAclAdvancedDestAddr": hh3cAclIPAclAdvancedDestAddr,
       "hh3cAclIPAclAdvancedDestPrefix": hh3cAclIPAclAdvancedDestPrefix,
       "hh3cAclIPAclAdvancedDestAny": hh3cAclIPAclAdvancedDestAny,
       "hh3cAclIPAclAdvancedDestWild": hh3cAclIPAclAdvancedDestWild,
       "hh3cAclIPAclAdvancedDestOp": hh3cAclIPAclAdvancedDestOp,
       "hh3cAclIPAclAdvancedDestPort1": hh3cAclIPAclAdvancedDestPort1,
       "hh3cAclIPAclAdvancedDestPort2": hh3cAclIPAclAdvancedDestPort2,
       "hh3cAclIPAclAdvancedIcmpType": hh3cAclIPAclAdvancedIcmpType,
       "hh3cAclIPAclAdvancedIcmpCode": hh3cAclIPAclAdvancedIcmpCode,
       "hh3cAclIPAclAdvancedPrecedence": hh3cAclIPAclAdvancedPrecedence,
       "hh3cAclIPAclAdvancedTos": hh3cAclIPAclAdvancedTos,
       "hh3cAclIPAclAdvancedDscp": hh3cAclIPAclAdvancedDscp,
       "hh3cAclIPAclAdvancedTimeRangeName": hh3cAclIPAclAdvancedTimeRangeName,
       "hh3cAclIPAclAdvancedTCPFlag": hh3cAclIPAclAdvancedTCPFlag,
       "hh3cAclIPAclAdvancedFragmentFlag": hh3cAclIPAclAdvancedFragmentFlag,
       "hh3cAclIPAclAdvancedLog": hh3cAclIPAclAdvancedLog,
       "hh3cAclIPAclAdvancedCount": hh3cAclIPAclAdvancedCount,
       "hh3cAclIPAclAdvancedCountClear": hh3cAclIPAclAdvancedCountClear,
       "hh3cAclIPAclAdvancedEnable": hh3cAclIPAclAdvancedEnable,
       "hh3cAclIPAclAdvancedVpnInstanceName": hh3cAclIPAclAdvancedVpnInstanceName,
       "hh3cAclIPAclAdvancedComment": hh3cAclIPAclAdvancedComment,
       "hh3cAclIPAclAdvancedReflective": hh3cAclIPAclAdvancedReflective,
       "hh3cAclIPAclAdvancedCounting": hh3cAclIPAclAdvancedCounting,
       "hh3cAclIPAclAdvancedTCPFlagMask": hh3cAclIPAclAdvancedTCPFlagMask,
       "hh3cAclIPAclAdvancedTCPFlagValue": hh3cAclIPAclAdvancedTCPFlagValue,
       "hh3cAclIPAclAdvancedRouteTypeAny": hh3cAclIPAclAdvancedRouteTypeAny,
       "hh3cAclIPAclAdvancedRouteTypeValue": hh3cAclIPAclAdvancedRouteTypeValue,
       "hh3cAclIPAclAdvancedFlowLabel": hh3cAclIPAclAdvancedFlowLabel,
       "hh3cAclIPAclAdvancedSrcSuffix": hh3cAclIPAclAdvancedSrcSuffix,
       "hh3cAclIPAclAdvancedDestSuffix": hh3cAclIPAclAdvancedDestSuffix,
       "hh3cAclIPAclNamedBscTable": hh3cAclIPAclNamedBscTable,
       "hh3cAclIPAclNamedBscEntry": hh3cAclIPAclNamedBscEntry,
       "hh3cAclIPAclNamedBscRowStatus": hh3cAclIPAclNamedBscRowStatus,
       "hh3cAclIPAclNamedBscAct": hh3cAclIPAclNamedBscAct,
       "hh3cAclIPAclNamedBscSrcAddrType": hh3cAclIPAclNamedBscSrcAddrType,
       "hh3cAclIPAclNamedBscSrcAddr": hh3cAclIPAclNamedBscSrcAddr,
       "hh3cAclIPAclNamedBscSrcPrefix": hh3cAclIPAclNamedBscSrcPrefix,
       "hh3cAclIPAclNamedBscSrcAny": hh3cAclIPAclNamedBscSrcAny,
       "hh3cAclIPAclNamedBscSrcWild": hh3cAclIPAclNamedBscSrcWild,
       "hh3cAclIPAclNamedBscTRangeName": hh3cAclIPAclNamedBscTRangeName,
       "hh3cAclIPAclNamedBscFragmentFlag": hh3cAclIPAclNamedBscFragmentFlag,
       "hh3cAclIPAclNamedBscLog": hh3cAclIPAclNamedBscLog,
       "hh3cAclIPAclNamedBscCount": hh3cAclIPAclNamedBscCount,
       "hh3cAclIPAclNamedBscCountClear": hh3cAclIPAclNamedBscCountClear,
       "hh3cAclIPAclNamedBscEnable": hh3cAclIPAclNamedBscEnable,
       "hh3cAclIPAclNamedBscVpnInstName": hh3cAclIPAclNamedBscVpnInstName,
       "hh3cAclIPAclNamedBscComment": hh3cAclIPAclNamedBscComment,
       "hh3cAclIPAclNamedBscCounting": hh3cAclIPAclNamedBscCounting,
       "hh3cAclIPAclNamedBscRouteTypeAny": hh3cAclIPAclNamedBscRouteTypeAny,
       "hh3cAclIPAclNamedBscRouteTypeValue": hh3cAclIPAclNamedBscRouteTypeValue,
       "hh3cAclIPAclNamedAdvTable": hh3cAclIPAclNamedAdvTable,
       "hh3cAclIPAclNamedAdvEntry": hh3cAclIPAclNamedAdvEntry,
       "hh3cAclIPAclNamedAdvRowStatus": hh3cAclIPAclNamedAdvRowStatus,
       "hh3cAclIPAclNamedAdvAct": hh3cAclIPAclNamedAdvAct,
       "hh3cAclIPAclNamedAdvProtocol": hh3cAclIPAclNamedAdvProtocol,
       "hh3cAclIPAclNamedAdvAddrFlag": hh3cAclIPAclNamedAdvAddrFlag,
       "hh3cAclIPAclNamedAdvSrcAddrType": hh3cAclIPAclNamedAdvSrcAddrType,
       "hh3cAclIPAclNamedAdvSrcAddr": hh3cAclIPAclNamedAdvSrcAddr,
       "hh3cAclIPAclNamedAdvSrcPrefix": hh3cAclIPAclNamedAdvSrcPrefix,
       "hh3cAclIPAclNamedAdvSrcAny": hh3cAclIPAclNamedAdvSrcAny,
       "hh3cAclIPAclNamedAdvSrcWild": hh3cAclIPAclNamedAdvSrcWild,
       "hh3cAclIPAclNamedAdvSrcOp": hh3cAclIPAclNamedAdvSrcOp,
       "hh3cAclIPAclNamedAdvSrcPort1": hh3cAclIPAclNamedAdvSrcPort1,
       "hh3cAclIPAclNamedAdvSrcPort2": hh3cAclIPAclNamedAdvSrcPort2,
       "hh3cAclIPAclNamedAdvDstAddrType": hh3cAclIPAclNamedAdvDstAddrType,
       "hh3cAclIPAclNamedAdvDstAddr": hh3cAclIPAclNamedAdvDstAddr,
       "hh3cAclIPAclNamedAdvDstPrefix": hh3cAclIPAclNamedAdvDstPrefix,
       "hh3cAclIPAclNamedAdvDstAny": hh3cAclIPAclNamedAdvDstAny,
       "hh3cAclIPAclNamedAdvDstWild": hh3cAclIPAclNamedAdvDstWild,
       "hh3cAclIPAclNamedAdvDstOp": hh3cAclIPAclNamedAdvDstOp,
       "hh3cAclIPAclNamedAdvDstPort1": hh3cAclIPAclNamedAdvDstPort1,
       "hh3cAclIPAclNamedAdvDstPort2": hh3cAclIPAclNamedAdvDstPort2,
       "hh3cAclIPAclNamedAdvIcmpType": hh3cAclIPAclNamedAdvIcmpType,
       "hh3cAclIPAclNamedAdvIcmpCode": hh3cAclIPAclNamedAdvIcmpCode,
       "hh3cAclIPAclNamedAdvPrecedence": hh3cAclIPAclNamedAdvPrecedence,
       "hh3cAclIPAclNamedAdvTos": hh3cAclIPAclNamedAdvTos,
       "hh3cAclIPAclNamedAdvDscp": hh3cAclIPAclNamedAdvDscp,
       "hh3cAclIPAclNamedAdvTRangeName": hh3cAclIPAclNamedAdvTRangeName,
       "hh3cAclIPAclNamedAdvTCPFlag": hh3cAclIPAclNamedAdvTCPFlag,
       "hh3cAclIPAclNamedAdvFragmentFlag": hh3cAclIPAclNamedAdvFragmentFlag,
       "hh3cAclIPAclNamedAdvLog": hh3cAclIPAclNamedAdvLog,
       "hh3cAclIPAclNamedAdvCount": hh3cAclIPAclNamedAdvCount,
       "hh3cAclIPAclNamedAdvCountClear": hh3cAclIPAclNamedAdvCountClear,
       "hh3cAclIPAclNamedAdvEnable": hh3cAclIPAclNamedAdvEnable,
       "hh3cAclIPAclNamedAdvVpnInstName": hh3cAclIPAclNamedAdvVpnInstName,
       "hh3cAclIPAclNamedAdvComment": hh3cAclIPAclNamedAdvComment,
       "hh3cAclIPAclNamedAdvReflective": hh3cAclIPAclNamedAdvReflective,
       "hh3cAclIPAclNamedAdvCounting": hh3cAclIPAclNamedAdvCounting,
       "hh3cAclIPAclNamedAdvTCPFlagMask": hh3cAclIPAclNamedAdvTCPFlagMask,
       "hh3cAclIPAclNamedAdvTCPFlagValue": hh3cAclIPAclNamedAdvTCPFlagValue,
       "hh3cAclIPAclNamedAdvRouteTypeAny": hh3cAclIPAclNamedAdvRouteTypeAny,
       "hh3cAclIPAclNamedAdvRouteTypeValue": hh3cAclIPAclNamedAdvRouteTypeValue,
       "hh3cAclIPAclNamedAdvFlowLabel": hh3cAclIPAclNamedAdvFlowLabel,
       "hh3cAclIPAclNamedAdvSrcSuffix": hh3cAclIPAclNamedAdvSrcSuffix,
       "hh3cAclIPAclNamedAdvDstSuffix": hh3cAclIPAclNamedAdvDstSuffix,
       "hh3cAclMACAclGroup": hh3cAclMACAclGroup,
       "hh3cAclMACTable": hh3cAclMACTable,
       "hh3cAclMACEntry": hh3cAclMACEntry,
       "hh3cAclMACRuleIndex": hh3cAclMACRuleIndex,
       "hh3cAclMACRowStatus": hh3cAclMACRowStatus,
       "hh3cAclMACAct": hh3cAclMACAct,
       "hh3cAclMACTypeCode": hh3cAclMACTypeCode,
       "hh3cAclMACTypeMask": hh3cAclMACTypeMask,
       "hh3cAclMACSrcMac": hh3cAclMACSrcMac,
       "hh3cAclMACSrcMacWild": hh3cAclMACSrcMacWild,
       "hh3cAclMACDestMac": hh3cAclMACDestMac,
       "hh3cAclMACDestMacWild": hh3cAclMACDestMacWild,
       "hh3cAclMACLsapCode": hh3cAclMACLsapCode,
       "hh3cAclMACLsapMask": hh3cAclMACLsapMask,
       "hh3cAclMACCos": hh3cAclMACCos,
       "hh3cAclMACTimeRangeName": hh3cAclMACTimeRangeName,
       "hh3cAclMACCount": hh3cAclMACCount,
       "hh3cAclMACCountClear": hh3cAclMACCountClear,
       "hh3cAclMACEnable": hh3cAclMACEnable,
       "hh3cAclMACComment": hh3cAclMACComment,
       "hh3cAclMACLog": hh3cAclMACLog,
       "hh3cAclMACCounting": hh3cAclMACCounting,
       "hh3cAclNamedMACTable": hh3cAclNamedMACTable,
       "hh3cAclNamedMACEntry": hh3cAclNamedMACEntry,
       "hh3cAclNamedMACRowStatus": hh3cAclNamedMACRowStatus,
       "hh3cAclNamedMACAct": hh3cAclNamedMACAct,
       "hh3cAclNamedMACTypeCode": hh3cAclNamedMACTypeCode,
       "hh3cAclNamedMACTypeMask": hh3cAclNamedMACTypeMask,
       "hh3cAclNamedMACSrcMac": hh3cAclNamedMACSrcMac,
       "hh3cAclNamedMACSrcMacWild": hh3cAclNamedMACSrcMacWild,
       "hh3cAclNamedMACDstMac": hh3cAclNamedMACDstMac,
       "hh3cAclNamedMACDstMacWild": hh3cAclNamedMACDstMacWild,
       "hh3cAclNamedMACLsapCode": hh3cAclNamedMACLsapCode,
       "hh3cAclNamedMACLsapMask": hh3cAclNamedMACLsapMask,
       "hh3cAclNamedMACCos": hh3cAclNamedMACCos,
       "hh3cAclNamedMACTimeRangeName": hh3cAclNamedMACTimeRangeName,
       "hh3cAclNamedMACCount": hh3cAclNamedMACCount,
       "hh3cAclNamedMACCountClear": hh3cAclNamedMACCountClear,
       "hh3cAclNamedMACEnable": hh3cAclNamedMACEnable,
       "hh3cAclNamedMACComment": hh3cAclNamedMACComment,
       "hh3cAclNamedMACLog": hh3cAclNamedMACLog,
       "hh3cAclNamedMACCounting": hh3cAclNamedMACCounting,
       "hh3cAclEnUserAclGroup": hh3cAclEnUserAclGroup,
       "hh3cAclEnUserTable": hh3cAclEnUserTable,
       "hh3cAclEnUserEntry": hh3cAclEnUserEntry,
       "hh3cAclEnUserRuleIndex": hh3cAclEnUserRuleIndex,
       "hh3cAclEnUserRowStatus": hh3cAclEnUserRowStatus,
       "hh3cAclEnUserAct": hh3cAclEnUserAct,
       "hh3cAclEnUserStartString": hh3cAclEnUserStartString,
       "hh3cAclEnUserL2String": hh3cAclEnUserL2String,
       "hh3cAclEnUserMplsString": hh3cAclEnUserMplsString,
       "hh3cAclEnUserIPv4String": hh3cAclEnUserIPv4String,
       "hh3cAclEnUserIPv6String": hh3cAclEnUserIPv6String,
       "hh3cAclEnUserL4String": hh3cAclEnUserL4String,
       "hh3cAclEnUserL5String": hh3cAclEnUserL5String,
       "hh3cAclEnUserTimeRangeName": hh3cAclEnUserTimeRangeName,
       "hh3cAclEnUserCount": hh3cAclEnUserCount,
       "hh3cAclEnUserCountClear": hh3cAclEnUserCountClear,
       "hh3cAclEnUserEnable": hh3cAclEnUserEnable,
       "hh3cAclEnUserComment": hh3cAclEnUserComment,
       "hh3cAclEnUserLog": hh3cAclEnUserLog,
       "hh3cAclEnUserCounting": hh3cAclEnUserCounting,
       "hh3cAclNamedUserTable": hh3cAclNamedUserTable,
       "hh3cAclNamedUserEntry": hh3cAclNamedUserEntry,
       "hh3cAclNamedUserRowStatus": hh3cAclNamedUserRowStatus,
       "hh3cAclNamedUserAct": hh3cAclNamedUserAct,
       "hh3cAclNamedUserStartString": hh3cAclNamedUserStartString,
       "hh3cAclNamedUserL2String": hh3cAclNamedUserL2String,
       "hh3cAclNamedUserMplsString": hh3cAclNamedUserMplsString,
       "hh3cAclNamedUserIPv4String": hh3cAclNamedUserIPv4String,
       "hh3cAclNamedUserIPv6String": hh3cAclNamedUserIPv6String,
       "hh3cAclNamedUserL4String": hh3cAclNamedUserL4String,
       "hh3cAclNamedUserL5String": hh3cAclNamedUserL5String,
       "hh3cAclNamedUserTimeRangeName": hh3cAclNamedUserTimeRangeName,
       "hh3cAclNamedUserCount": hh3cAclNamedUserCount,
       "hh3cAclNamedUserCountClear": hh3cAclNamedUserCountClear,
       "hh3cAclNamedUserEnable": hh3cAclNamedUserEnable,
       "hh3cAclNamedUserComment": hh3cAclNamedUserComment,
       "hh3cAclNamedUserLog": hh3cAclNamedUserLog,
       "hh3cAclNamedUserCounting": hh3cAclNamedUserCounting,
       "hh3cAclResourceGroup": hh3cAclResourceGroup,
       "hh3cAclResourceUsageTable": hh3cAclResourceUsageTable,
       "hh3cAclResourceUsageEntry": hh3cAclResourceUsageEntry,
       "hh3cAclResourceChassis": hh3cAclResourceChassis,
       "hh3cAclResourceSlot": hh3cAclResourceSlot,
       "hh3cAclResourceChip": hh3cAclResourceChip,
       "hh3cAclResourceType": hh3cAclResourceType,
       "hh3cAclPortRange": hh3cAclPortRange,
       "hh3cAclResourceTotal": hh3cAclResourceTotal,
       "hh3cAclResourceReserved": hh3cAclResourceReserved,
       "hh3cAclResourceConfigured": hh3cAclResourceConfigured,
       "hh3cAclResourceUsagePercent": hh3cAclResourceUsagePercent,
       "hh3cAclResourceTypeDescription": hh3cAclResourceTypeDescription,
       "hh3cAclIntervalGroup": hh3cAclIntervalGroup,
       "hh3cAclIntervalTable": hh3cAclIntervalTable,
       "hh3cAclIntervalEntry": hh3cAclIntervalEntry,
       "hh3cAclIntervalType": hh3cAclIntervalType,
       "hh3cAclIntervalValue": hh3cAclIntervalValue,
       "hh3cAclIntervalRowStatus": hh3cAclIntervalRowStatus,
       "hh3cAclPacketFilterObjects": hh3cAclPacketFilterObjects,
       "hh3cPfilterScalarGroup": hh3cPfilterScalarGroup,
       "hh3cPfilterDefaultAction": hh3cPfilterDefaultAction,
       "hh3cPfilterProcessingStatus": hh3cPfilterProcessingStatus,
       "hh3cPfilterApplyTable": hh3cPfilterApplyTable,
       "hh3cPfilterApplyEntry": hh3cPfilterApplyEntry,
       "hh3cPfilterApplyObjType": hh3cPfilterApplyObjType,
       "hh3cPfilterApplyObjIndex": hh3cPfilterApplyObjIndex,
       "hh3cPfilterApplyDirection": hh3cPfilterApplyDirection,
       "hh3cPfilterApplyAclType": hh3cPfilterApplyAclType,
       "hh3cPfilterApplyAclIndex": hh3cPfilterApplyAclIndex,
       "hh3cPfilterApplyHardCount": hh3cPfilterApplyHardCount,
       "hh3cPfilterApplySequence": hh3cPfilterApplySequence,
       "hh3cPfilterApplyCountClear": hh3cPfilterApplyCountClear,
       "hh3cPfilterApplyRowStatus": hh3cPfilterApplyRowStatus,
       "hh3cPfilterAclGroupRunInfoTable": hh3cPfilterAclGroupRunInfoTable,
       "hh3cPfilterAclGroupRunInfoEntry": hh3cPfilterAclGroupRunInfoEntry,
       "hh3cPfilterRunApplyObjType": hh3cPfilterRunApplyObjType,
       "hh3cPfilterRunApplyObjIndex": hh3cPfilterRunApplyObjIndex,
       "hh3cPfilterRunApplyDirection": hh3cPfilterRunApplyDirection,
       "hh3cPfilterRunApplyAclType": hh3cPfilterRunApplyAclType,
       "hh3cPfilterRunApplyAclIndex": hh3cPfilterRunApplyAclIndex,
       "hh3cPfilterAclGroupStatus": hh3cPfilterAclGroupStatus,
       "hh3cPfilterAclGroupCountStatus": hh3cPfilterAclGroupCountStatus,
       "hh3cPfilterAclGroupPermitPkts": hh3cPfilterAclGroupPermitPkts,
       "hh3cPfilterAclGroupPermitBytes": hh3cPfilterAclGroupPermitBytes,
       "hh3cPfilterAclGroupDenyPkts": hh3cPfilterAclGroupDenyPkts,
       "hh3cPfilterAclGroupDenyBytes": hh3cPfilterAclGroupDenyBytes,
       "hh3cPfilterAclRuleRunInfoTable": hh3cPfilterAclRuleRunInfoTable,
       "hh3cPfilterAclRuleRunInfoEntry": hh3cPfilterAclRuleRunInfoEntry,
       "hh3cPfilterAclRuleIndex": hh3cPfilterAclRuleIndex,
       "hh3cPfilterAclRuleStatus": hh3cPfilterAclRuleStatus,
       "hh3cPfilterAclRuleCountStatus": hh3cPfilterAclRuleCountStatus,
       "hh3cPfilterAclRuleMatchPackets": hh3cPfilterAclRuleMatchPackets,
       "hh3cPfilterAclRuleMatchBytes": hh3cPfilterAclRuleMatchBytes,
       "hh3cPfilterStatisticSumTable": hh3cPfilterStatisticSumTable,
       "hh3cPfilterStatisticSumEntry": hh3cPfilterStatisticSumEntry,
       "hh3cPfilterSumDirection": hh3cPfilterSumDirection,
       "hh3cPfilterSumAclType": hh3cPfilterSumAclType,
       "hh3cPfilterSumAclIndex": hh3cPfilterSumAclIndex,
       "hh3cPfilterSumRuleIndex": hh3cPfilterSumRuleIndex,
       "hh3cPfilterSumRuleMatchPackets": hh3cPfilterSumRuleMatchPackets,
       "hh3cPfilterSumRuleMatchBytes": hh3cPfilterSumRuleMatchBytes,
       "hh3cPfilter2ApplyTable": hh3cPfilter2ApplyTable,
       "hh3cPfilter2ApplyEntry": hh3cPfilter2ApplyEntry,
       "hh3cPfilter2ApplyObjType": hh3cPfilter2ApplyObjType,
       "hh3cPfilter2ApplyObjIndex": hh3cPfilter2ApplyObjIndex,
       "hh3cPfilter2ApplyDirection": hh3cPfilter2ApplyDirection,
       "hh3cPfilter2ApplyAclType": hh3cPfilter2ApplyAclType,
       "hh3cPfilter2ApplyAclIndex": hh3cPfilter2ApplyAclIndex,
       "hh3cPfilter2ApplyHardCount": hh3cPfilter2ApplyHardCount,
       "hh3cPfilter2ApplySequence": hh3cPfilter2ApplySequence,
       "hh3cPfilter2ApplyCountClear": hh3cPfilter2ApplyCountClear,
       "hh3cPfilter2ApplyRowStatus": hh3cPfilter2ApplyRowStatus,
       "hh3cPfilter2AclGroupRunInfoTable": hh3cPfilter2AclGroupRunInfoTable,
       "hh3cPfilter2AclGroupRunInfoEntry": hh3cPfilter2AclGroupRunInfoEntry,
       "hh3cPfilter2RunApplyObjType": hh3cPfilter2RunApplyObjType,
       "hh3cPfilter2RunApplyObjIndex": hh3cPfilter2RunApplyObjIndex,
       "hh3cPfilter2RunApplyDirection": hh3cPfilter2RunApplyDirection,
       "hh3cPfilter2RunApplyAclType": hh3cPfilter2RunApplyAclType,
       "hh3cPfilter2RunApplyAclIndex": hh3cPfilter2RunApplyAclIndex,
       "hh3cPfilter2AclGroupStatus": hh3cPfilter2AclGroupStatus,
       "hh3cPfilter2AclGroupCountStatus": hh3cPfilter2AclGroupCountStatus,
       "hh3cPfilter2AclGroupPermitPkts": hh3cPfilter2AclGroupPermitPkts,
       "hh3cPfilter2AclGroupPermitBytes": hh3cPfilter2AclGroupPermitBytes,
       "hh3cPfilter2AclGroupDenyPkts": hh3cPfilter2AclGroupDenyPkts,
       "hh3cPfilter2AclGroupDenyBytes": hh3cPfilter2AclGroupDenyBytes,
       "hh3cPfilter2AclRuleRunInfoTable": hh3cPfilter2AclRuleRunInfoTable,
       "hh3cPfilter2AclRuleRunInfoEntry": hh3cPfilter2AclRuleRunInfoEntry,
       "hh3cPfilter2AclRuleIndex": hh3cPfilter2AclRuleIndex,
       "hh3cPfilter2AclRuleStatus": hh3cPfilter2AclRuleStatus,
       "hh3cPfilter2AclRuleCountStatus": hh3cPfilter2AclRuleCountStatus,
       "hh3cPfilter2AclRuleMatchPackets": hh3cPfilter2AclRuleMatchPackets,
       "hh3cPfilter2AclRuleMatchBytes": hh3cPfilter2AclRuleMatchBytes,
       "hh3cPfilter2StatisticSumTable": hh3cPfilter2StatisticSumTable,
       "hh3cPfilter2StatisticSumEntry": hh3cPfilter2StatisticSumEntry,
       "hh3cPfilter2SumDirection": hh3cPfilter2SumDirection,
       "hh3cPfilter2SumAclType": hh3cPfilter2SumAclType,
       "hh3cPfilter2SumAclIndex": hh3cPfilter2SumAclIndex,
       "hh3cPfilter2SumRuleIndex": hh3cPfilter2SumRuleIndex,
       "hh3cPfilter2SumRuleMatchPackets": hh3cPfilter2SumRuleMatchPackets,
       "hh3cPfilter2SumRuleMatchBytes": hh3cPfilter2SumRuleMatchBytes,
       "hh3cAclPacketfilterTrapObjects": hh3cAclPacketfilterTrapObjects,
       "hh3cPfilterInterface": hh3cPfilterInterface,
       "hh3cPfilterDirection": hh3cPfilterDirection,
       "hh3cPfilterACLNumber": hh3cPfilterACLNumber,
       "hh3cPfilterAction": hh3cPfilterAction,
       "hh3cMACfilterSourceMac": hh3cMACfilterSourceMac,
       "hh3cMACfilterDestinationMac": hh3cMACfilterDestinationMac,
       "hh3cPfilterPacketNumber": hh3cPfilterPacketNumber,
       "hh3cPfilterReceiveInterface": hh3cPfilterReceiveInterface,
       "hh3cAclPacketIfName": hh3cAclPacketIfName,
       "hh3cAclPacketDirection": hh3cAclPacketDirection,
       "hh3cAclPacketBAGG": hh3cAclPacketBAGG,
       "hh3cAclPacketVlanID": hh3cAclPacketVlanID,
       "hh3cAclPacketSrcIP": hh3cAclPacketSrcIP,
       "hh3cAclPacketDstIP": hh3cAclPacketDstIP,
       "hh3cAclPacketProtocol": hh3cAclPacketProtocol,
       "hh3cAclPacketDscp": hh3cAclPacketDscp,
       "hh3cAclPacketFlowLabel": hh3cAclPacketFlowLabel,
       "hh3cAclPacketIcmpIgmpType": hh3cAclPacketIcmpIgmpType,
       "hh3cAclPacketIcmpIgmpCode": hh3cAclPacketIcmpIgmpCode,
       "hh3cAclPacketTcpFlags": hh3cAclPacketTcpFlags,
       "hh3cAclPacketSrcPort": hh3cAclPacketSrcPort,
       "hh3cAclPacketDstPort": hh3cAclPacketDstPort,
       "hh3cAclPacketSrcMacAddr": hh3cAclPacketSrcMacAddr,
       "hh3cAclPacketDstMacAddr": hh3cAclPacketDstMacAddr,
       "hh3cAclPacketMacTypeLen": hh3cAclPacketMacTypeLen,
       "hh3cAclPacketVlanPCP": hh3cAclPacketVlanPCP,
       "hh3cAclPacketfilterTrap": hh3cAclPacketfilterTrap,
       "hh3cPfilterTrapPrefix": hh3cPfilterTrapPrefix,
       "hh3cMACfilterTrap": hh3cMACfilterTrap,
       "hh3cAclRuleMatchCount": hh3cAclRuleMatchCount,
       "hh3cAclFirstIPv4PktCaptured": hh3cAclFirstIPv4PktCaptured,
       "hh3cAclFirstIPv6PktCaptured": hh3cAclFirstIPv6PktCaptured,
       "hh3cAclFirstEthernetPktCaptured": hh3cAclFirstEthernetPktCaptured,
       "hh3cAclTrapObjects": hh3cAclTrapObjects,
       "hh3cAclResourceTypeName": hh3cAclResourceTypeName,
       "hh3cAclResourceUsage": hh3cAclResourceUsage,
       "hh3cAclResourceUsedEntries": hh3cAclResourceUsedEntries,
       "hh3cAclResourceTotalEntries": hh3cAclResourceTotalEntries,
       "hh3cAclResourceChassisID": hh3cAclResourceChassisID,
       "hh3cAclResourceSlotID": hh3cAclResourceSlotID,
       "hh3cAclTrap": hh3cAclTrap,
       "hh3cAclTrapPrefix": hh3cAclTrapPrefix,
       "hh3cAclResourceTrap": hh3cAclResourceTrap}
)
