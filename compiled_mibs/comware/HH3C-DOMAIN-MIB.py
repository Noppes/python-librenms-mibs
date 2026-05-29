# SNMP MIB module (HH3C-DOMAIN-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\comware\HH3C-DOMAIN-MIB

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
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

(Ipv6AddressPrefix,) = mibBuilder.importSymbols(
    "IPV6-TC",
    "Ipv6AddressPrefix")

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

hh3cDomain = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 46)
)
if mibBuilder.loadTexts:
    hh3cDomain.setRevisions(
        ("2021-03-24 00:00",
         "2021-02-02 00:00",
         "2020-11-20 00:00",
         "2020-07-03 00:00",
         "2020-01-16 00:00",
         "2019-03-12 00:00",
         "2018-11-27 00:00",
         "2017-10-13 00:00",
         "2017-06-03 00:00",
         "2013-11-25 00:00",
         "2013-04-25 00:00",
         "2013-02-28 00:00",
         "2012-10-15 00:00",
         "2012-05-20 00:00",
         "2009-08-05 00:00",
         "2008-12-30 00:00",
         "2008-11-25 00:00",
         "2007-03-07 00:00",
         "2006-03-27 00:00",
         "2005-06-30 00:00",
         "2005-03-23 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class Hh3cModeOfDomainScheme(TextualConvention, Integer32):
    status = "current"
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
        *(("none", 1),
          ("local", 2),
          ("radius", 3),
          ("tacacs", 4),
          ("ldap", 5))
    )



class Hh3cAAATypeDomainScheme(TextualConvention, Integer32):
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
        *(("accounting", 1),
          ("authentication", 2),
          ("authorization", 3),
          ("none", 4))
    )



class Hh3cAccessModeofDomainScheme(TextualConvention, Integer32):
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
              12)
        )
    )
    namedValues = NamedValues(
        *(("default", 1),
          ("login", 2),
          ("lanAccess", 3),
          ("portal", 4),
          ("ppp", 5),
          ("gcm", 6),
          ("dvpn", 7),
          ("dhcp", 8),
          ("voice", 9),
          ("superauthen", 10),
          ("command", 11),
          ("reserved", 12))
    )



# MIB Managed Objects in the order of their OIDs

_Hh3cDomainControl_ObjectIdentity = ObjectIdentity
hh3cDomainControl = _Hh3cDomainControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 46, 1)
)


class _Hh3cDomainDefault_Type(OctetString):
    """Custom type hh3cDomainDefault based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_Hh3cDomainDefault_Type.__name__ = "OctetString"
_Hh3cDomainDefault_Object = MibScalar
hh3cDomainDefault = _Hh3cDomainDefault_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 46, 1, 1),
    _Hh3cDomainDefault_Type()
)
hh3cDomainDefault.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDomainDefault.setStatus("current")
_Hh3cDomainTables_ObjectIdentity = ObjectIdentity
hh3cDomainTables = _Hh3cDomainTables_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 46, 2)
)
_Hh3cDomainInfoTable_Object = MibTable
hh3cDomainInfoTable = _Hh3cDomainInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 46, 2, 1)
)
if mibBuilder.loadTexts:
    hh3cDomainInfoTable.setStatus("current")
_Hh3cDomainInfoEntry_Object = MibTableRow
hh3cDomainInfoEntry = _Hh3cDomainInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 46, 2, 1, 1)
)
hh3cDomainInfoEntry.setIndexNames(
    (0, "HH3C-DOMAIN-MIB", "hh3cDomainName"),
)
if mibBuilder.loadTexts:
    hh3cDomainInfoEntry.setStatus("current")


class _Hh3cDomainName_Type(OctetString):
    """Custom type hh3cDomainName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_Hh3cDomainName_Type.__name__ = "OctetString"
_Hh3cDomainName_Object = MibTableColumn
hh3cDomainName = _Hh3cDomainName_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 46, 2, 1, 1, 1),
    _Hh3cDomainName_Type()
)
hh3cDomainName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDomainName.setStatus("current")


class _Hh3cDomainState_Type(Integer32):
    """Custom type hh3cDomainState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("block", 2))
    )


_Hh3cDomainState_Type.__name__ = "Integer32"
_Hh3cDomainState_Object = MibTableColumn
hh3cDomainState = _Hh3cDomainState_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 46, 2, 1, 1, 2),
    _Hh3cDomainState_Type()
)
hh3cDomainState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cDomainState.setStatus("current")
_Hh3cDomainMaxAccessNum_Type = Integer32
_Hh3cDomainMaxAccessNum_Object = MibTableColumn
hh3cDomainMaxAccessNum = _Hh3cDomainMaxAccessNum_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 46, 2, 1, 1, 3),
    _Hh3cDomainMaxAccessNum_Type()
)
hh3cDomainMaxAccessNum.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cDomainMaxAccessNum.setStatus("current")


class _Hh3cDomainVlanAssignMode_Type(Integer32):
    """Custom type hh3cDomainVlanAssignMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("integer", 1),
          ("string", 2),
          ("vlanlist", 3))
    )


_Hh3cDomainVlanAssignMode_Type.__name__ = "Integer32"
_Hh3cDomainVlanAssignMode_Object = MibTableColumn
hh3cDomainVlanAssignMode = _Hh3cDomainVlanAssignMode_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 46, 2, 1, 1, 4),
    _Hh3cDomainVlanAssignMode_Type()
)
hh3cDomainVlanAssignMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cDomainVlanAssignMode.setStatus("current")
_Hh3cDomainIdleCutEnable_Type = TruthValue
_Hh3cDomainIdleCutEnable_Object = MibTableColumn
hh3cDomainIdleCutEnable = _Hh3cDomainIdleCutEnable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 46, 2, 1, 1, 5),
    _Hh3cDomainIdleCutEnable_Type()
)
hh3cDomainIdleCutEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cDomainIdleCutEnable.setStatus("current")
_Hh3cDomainIdleCutMaxTime_Type = Integer32
_Hh3cDomainIdleCutMaxTime_Object = MibTableColumn
hh3cDomainIdleCutMaxTime = _Hh3cDomainIdleCutMaxTime_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 46, 2, 1, 1, 6),
    _Hh3cDomainIdleCutMaxTime_Type()
)
hh3cDomainIdleCutMaxTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cDomainIdleCutMaxTime.setStatus("current")


class _Hh3cDomainIdleCutMinFlow_Type(Integer32):
    """Custom type hh3cDomainIdleCutMinFlow based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10240000),
    )


_Hh3cDomainIdleCutMinFlow_Type.__name__ = "Integer32"
_Hh3cDomainIdleCutMinFlow_Object = MibTableColumn
hh3cDomainIdleCutMinFlow = _Hh3cDomainIdleCutMinFlow_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 46, 2, 1, 1, 7),
    _Hh3cDomainIdleCutMinFlow_Type()
)
hh3cDomainIdleCutMinFlow.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cDomainIdleCutMinFlow.setStatus("current")
_Hh3cDomainMessengerEnable_Type = TruthValue
_Hh3cDomainMessengerEnable_Object = MibTableColumn
hh3cDomainMessengerEnable = _Hh3cDomainMessengerEnable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 46, 2, 1, 1, 8),
    _Hh3cDomainMessengerEnable_Type()
)
hh3cDomainMessengerEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cDomainMessengerEnable.setStatus("current")


class _Hh3cDomainMessengerLimitTime_Type(Integer32):
    """Custom type hh3cDomainMessengerLimitTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 60),
    )


_Hh3cDomainMessengerLimitTime_Type.__name__ = "Integer32"
_Hh3cDomainMessengerLimitTime_Object = MibTableColumn
hh3cDomainMessengerLimitTime = _Hh3cDomainMessengerLimitTime_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 46, 2, 1, 1, 9),
    _Hh3cDomainMessengerLimitTime_Type()
)
hh3cDomainMessengerLimitTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cDomainMessengerLimitTime.setStatus("current")


class _Hh3cDomainMessengerSpanTime_Type(Integer32):
    """Custom type hh3cDomainMessengerSpanTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 60),
    )


_Hh3cDomainMessengerSpanTime_Type.__name__ = "Integer32"
_Hh3cDomainMessengerSpanTime_Object = MibTableColumn
hh3cDomainMessengerSpanTime = _Hh3cDomainMessengerSpanTime_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 46, 2, 1, 1, 10),
    _Hh3cDomainMessengerSpanTime_Type()
)
hh3cDomainMessengerSpanTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cDomainMessengerSpanTime.setStatus("current")
_Hh3cDomainSelfServiceEnable_Type = TruthValue
_Hh3cDomainSelfServiceEnable_Object = MibTableColumn
hh3cDomainSelfServiceEnable = _Hh3cDomainSelfServiceEnable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 46, 2, 1, 1, 11),
    _Hh3cDomainSelfServiceEnable_Type()
)
hh3cDomainSelfServiceEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cDomainSelfServiceEnable.setStatus("current")


class _Hh3cDomainSelfServiceURL_Type(OctetString):
    """Custom type hh3cDomainSelfServiceURL based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_Hh3cDomainSelfServiceURL_Type.__name__ = "OctetString"
_Hh3cDomainSelfServiceURL_Object = MibTableColumn
hh3cDomainSelfServiceURL = _Hh3cDomainSelfServiceURL_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 46, 2, 1, 1, 12),
    _Hh3cDomainSelfServiceURL_Type()
)
hh3cDomainSelfServiceURL.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cDomainSelfServiceURL.setStatus("current")


class _Hh3cDomainAccFailureAction_Type(Integer32):
    """Custom type hh3cDomainAccFailureAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ignore", 1),
          ("reject", 2))
    )


_Hh3cDomainAccFailureAction_Type.__name__ = "Integer32"
_Hh3cDomainAccFailureAction_Object = MibTableColumn
hh3cDomainAccFailureAction = _Hh3cDomainAccFailureAction_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 46, 2, 1, 1, 13),
    _Hh3cDomainAccFailureAction_Type()
)
hh3cDomainAccFailureAction.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cDomainAccFailureAction.setStatus("current")
_Hh3cDomainRowStatus_Type = RowStatus
_Hh3cDomainRowStatus_Object = MibTableColumn
hh3cDomainRowStatus = _Hh3cDomainRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 46, 2, 1, 1, 14),
    _Hh3cDomainRowStatus_Type()
)
hh3cDomainRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cDomainRowStatus.setStatus("current")
_Hh3cDomainCurrentAccessNum_Type = Integer32
_Hh3cDomainCurrentAccessNum_Object = MibTableColumn
hh3cDomainCurrentAccessNum = _Hh3cDomainCurrentAccessNum_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 46, 2, 1, 1, 15),
    _Hh3cDomainCurrentAccessNum_Type()
)
hh3cDomainCurrentAccessNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDomainCurrentAccessNum.setStatus("current")
_Hh3cDomainIdleCutTime_Type = TimeTicks
_Hh3cDomainIdleCutTime_Object = MibTableColumn
hh3cDomainIdleCutTime = _Hh3cDomainIdleCutTime_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 46, 2, 1, 1, 16),
    _Hh3cDomainIdleCutTime_Type()
)
hh3cDomainIdleCutTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDomainIdleCutTime.setStatus("current")


class _Hh3cDomainServiceType_Type(Integer32):
    """Custom type hh3cDomainServiceType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("hsi", 1),
          ("stb", 2),
          ("voip", 3))
    )


_Hh3cDomainServiceType_Type.__name__ = "Integer32"
_Hh3cDomainServiceType_Object = MibTableColumn
hh3cDomainServiceType = _Hh3cDomainServiceType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 46, 2, 1, 1, 17),
    _Hh3cDomainServiceType_Type()
)
hh3cDomainServiceType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cDomainServiceType.setStatus("current")


class _Hh3cDomainIpPoolName_Type(OctetString):
    """Custom type hh3cDomainIpPoolName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_Hh3cDomainIpPoolName_Type.__name__ = "OctetString"
_Hh3cDomainIpPoolName_Object = MibTableColumn
hh3cDomainIpPoolName = _Hh3cDomainIpPoolName_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 46, 2, 1, 1, 18),
    _Hh3cDomainIpPoolName_Type()
)
hh3cDomainIpPoolName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cDomainIpPoolName.setStatus("current")


class _Hh3cDomainIpv6PoolName_Type(OctetString):
    """Custom type hh3cDomainIpv6PoolName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_Hh3cDomainIpv6PoolName_Type.__name__ = "OctetString"
_Hh3cDomainIpv6PoolName_Object = MibTableColumn
hh3cDomainIpv6PoolName = _Hh3cDomainIpv6PoolName_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 46, 2, 1, 1, 19),
    _Hh3cDomainIpv6PoolName_Type()
)
hh3cDomainIpv6PoolName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cDomainIpv6PoolName.setStatus("current")


class _Hh3cDomainIPv4PoolUpperValue_Type(Integer32):
    """Custom type hh3cDomainIPv4PoolUpperValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Hh3cDomainIPv4PoolUpperValue_Type.__name__ = "Integer32"
_Hh3cDomainIPv4PoolUpperValue_Object = MibTableColumn
hh3cDomainIPv4PoolUpperValue = _Hh3cDomainIPv4PoolUpperValue_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 46, 2, 1, 1, 20),
    _Hh3cDomainIPv4PoolUpperValue_Type()
)
hh3cDomainIPv4PoolUpperValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cDomainIPv4PoolUpperValue.setStatus("current")


class _Hh3cDomainIPv4PoolLowerValue_Type(Integer32):
    """Custom type hh3cDomainIPv4PoolLowerValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Hh3cDomainIPv4PoolLowerValue_Type.__name__ = "Integer32"
_Hh3cDomainIPv4PoolLowerValue_Object = MibTableColumn
hh3cDomainIPv4PoolLowerValue = _Hh3cDomainIPv4PoolLowerValue_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 46, 2, 1, 1, 21),
    _Hh3cDomainIPv4PoolLowerValue_Type()
)
hh3cDomainIPv4PoolLowerValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cDomainIPv4PoolLowerValue.setStatus("current")


class _Hh3cDomainIPv6PoolUpperValue_Type(Integer32):
    """Custom type hh3cDomainIPv6PoolUpperValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Hh3cDomainIPv6PoolUpperValue_Type.__name__ = "Integer32"
_Hh3cDomainIPv6PoolUpperValue_Object = MibTableColumn
hh3cDomainIPv6PoolUpperValue = _Hh3cDomainIPv6PoolUpperValue_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 46, 2, 1, 1, 22),
    _Hh3cDomainIPv6PoolUpperValue_Type()
)
hh3cDomainIPv6PoolUpperValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cDomainIPv6PoolUpperValue.setStatus("current")


class _Hh3cDomainIPv6PoolLowerValue_Type(Integer32):
    """Custom type hh3cDomainIPv6PoolLowerValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Hh3cDomainIPv6PoolLowerValue_Type.__name__ = "Integer32"
_Hh3cDomainIPv6PoolLowerValue_Object = MibTableColumn
hh3cDomainIPv6PoolLowerValue = _Hh3cDomainIPv6PoolLowerValue_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 46, 2, 1, 1, 23),
    _Hh3cDomainIPv6PoolLowerValue_Type()
)
hh3cDomainIPv6PoolLowerValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cDomainIPv6PoolLowerValue.setStatus("current")


class _Hh3cDomainIpPoolGroupName_Type(OctetString):
    """Custom type hh3cDomainIpPoolGroupName based on OctetString"""
    defaultValue = OctetString("")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_Hh3cDomainIpPoolGroupName_Type.__name__ = "OctetString"
_Hh3cDomainIpPoolGroupName_Object = MibTableColumn
hh3cDomainIpPoolGroupName = _Hh3cDomainIpPoolGroupName_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 46, 2, 1, 1, 24),
    _Hh3cDomainIpPoolGroupName_Type()
)
hh3cDomainIpPoolGroupName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cDomainIpPoolGroupName.setStatus("current")


class _Hh3cDomainIpv6PoolGroupName_Type(OctetString):
    """Custom type hh3cDomainIpv6PoolGroupName based on OctetString"""
    defaultValue = OctetString("")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_Hh3cDomainIpv6PoolGroupName_Type.__name__ = "OctetString"
_Hh3cDomainIpv6PoolGroupName_Object = MibTableColumn
hh3cDomainIpv6PoolGroupName = _Hh3cDomainIpv6PoolGroupName_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 46, 2, 1, 1, 25),
    _Hh3cDomainIpv6PoolGroupName_Type()
)
hh3cDomainIpv6PoolGroupName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cDomainIpv6PoolGroupName.setStatus("current")


class _Hh3cDomainNdPrefixPoolName_Type(OctetString):
    """Custom type hh3cDomainNdPrefixPoolName based on OctetString"""
    defaultValue = OctetString("")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_Hh3cDomainNdPrefixPoolName_Type.__name__ = "OctetString"
_Hh3cDomainNdPrefixPoolName_Object = MibTableColumn
hh3cDomainNdPrefixPoolName = _Hh3cDomainNdPrefixPoolName_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 46, 2, 1, 1, 26),
    _Hh3cDomainNdPrefixPoolName_Type()
)
hh3cDomainNdPrefixPoolName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cDomainNdPrefixPoolName.setStatus("current")


class _Hh3cDomainNdPrefixPoolGroupName_Type(OctetString):
    """Custom type hh3cDomainNdPrefixPoolGroupName based on OctetString"""
    defaultValue = OctetString("")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_Hh3cDomainNdPrefixPoolGroupName_Type.__name__ = "OctetString"
_Hh3cDomainNdPrefixPoolGroupName_Object = MibTableColumn
hh3cDomainNdPrefixPoolGroupName = _Hh3cDomainNdPrefixPoolGroupName_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 46, 2, 1, 1, 27),
    _Hh3cDomainNdPrefixPoolGroupName_Type()
)
hh3cDomainNdPrefixPoolGroupName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cDomainNdPrefixPoolGroupName.setStatus("current")


class _Hh3cDomainIpv6Prefix_Type(Ipv6AddressPrefix):
    """Custom type hh3cDomainIpv6Prefix based on Ipv6AddressPrefix"""
    defaultValue = OctetString("")


_Hh3cDomainIpv6Prefix_Type.__name__ = "Ipv6AddressPrefix"
_Hh3cDomainIpv6Prefix_Object = MibTableColumn
hh3cDomainIpv6Prefix = _Hh3cDomainIpv6Prefix_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 46, 2, 1, 1, 28),
    _Hh3cDomainIpv6Prefix_Type()
)
hh3cDomainIpv6Prefix.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cDomainIpv6Prefix.setStatus("current")


class _Hh3cDomainIpv6PrefixLength_Type(Integer32):
    """Custom type hh3cDomainIpv6PrefixLength based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Hh3cDomainIpv6PrefixLength_Type.__name__ = "Integer32"
_Hh3cDomainIpv6PrefixLength_Object = MibTableColumn
hh3cDomainIpv6PrefixLength = _Hh3cDomainIpv6PrefixLength_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 46, 2, 1, 1, 29),
    _Hh3cDomainIpv6PrefixLength_Type()
)
hh3cDomainIpv6PrefixLength.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cDomainIpv6PrefixLength.setStatus("current")


class _Hh3cDomainActiveWebServerUrl_Type(OctetString):
    """Custom type hh3cDomainActiveWebServerUrl based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_Hh3cDomainActiveWebServerUrl_Type.__name__ = "OctetString"
_Hh3cDomainActiveWebServerUrl_Object = MibTableColumn
hh3cDomainActiveWebServerUrl = _Hh3cDomainActiveWebServerUrl_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 46, 2, 1, 1, 30),
    _Hh3cDomainActiveWebServerUrl_Type()
)
hh3cDomainActiveWebServerUrl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDomainActiveWebServerUrl.setStatus("current")
_Hh3cDomainSchemeTable_Object = MibTable
hh3cDomainSchemeTable = _Hh3cDomainSchemeTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 46, 2, 2)
)
if mibBuilder.loadTexts:
    hh3cDomainSchemeTable.setStatus("current")
_Hh3cDomainSchemeEntry_Object = MibTableRow
hh3cDomainSchemeEntry = _Hh3cDomainSchemeEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 46, 2, 2, 1)
)
hh3cDomainSchemeEntry.setIndexNames(
    (0, "HH3C-DOMAIN-MIB", "hh3cDomainName"),
    (0, "HH3C-DOMAIN-MIB", "hh3cDomainSchemeIndex"),
)
if mibBuilder.loadTexts:
    hh3cDomainSchemeEntry.setStatus("current")
_Hh3cDomainSchemeIndex_Type = Integer32
_Hh3cDomainSchemeIndex_Object = MibTableColumn
hh3cDomainSchemeIndex = _Hh3cDomainSchemeIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 46, 2, 2, 1, 1),
    _Hh3cDomainSchemeIndex_Type()
)
hh3cDomainSchemeIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cDomainSchemeIndex.setStatus("current")
_Hh3cDomainSchemeMode_Type = Hh3cModeOfDomainScheme
_Hh3cDomainSchemeMode_Object = MibTableColumn
hh3cDomainSchemeMode = _Hh3cDomainSchemeMode_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 46, 2, 2, 1, 2),
    _Hh3cDomainSchemeMode_Type()
)
hh3cDomainSchemeMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cDomainSchemeMode.setStatus("current")


class _Hh3cDomainAuthSchemeName_Type(OctetString):
    """Custom type hh3cDomainAuthSchemeName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Hh3cDomainAuthSchemeName_Type.__name__ = "OctetString"
_Hh3cDomainAuthSchemeName_Object = MibTableColumn
hh3cDomainAuthSchemeName = _Hh3cDomainAuthSchemeName_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 46, 2, 2, 1, 3),
    _Hh3cDomainAuthSchemeName_Type()
)
hh3cDomainAuthSchemeName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cDomainAuthSchemeName.setStatus("current")


class _Hh3cDomainAcctSchemeName_Type(OctetString):
    """Custom type hh3cDomainAcctSchemeName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Hh3cDomainAcctSchemeName_Type.__name__ = "OctetString"
_Hh3cDomainAcctSchemeName_Object = MibTableColumn
hh3cDomainAcctSchemeName = _Hh3cDomainAcctSchemeName_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 46, 2, 2, 1, 4),
    _Hh3cDomainAcctSchemeName_Type()
)
hh3cDomainAcctSchemeName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cDomainAcctSchemeName.setStatus("current")
_Hh3cDomainSchemeRowStatus_Type = RowStatus
_Hh3cDomainSchemeRowStatus_Object = MibTableColumn
hh3cDomainSchemeRowStatus = _Hh3cDomainSchemeRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 46, 2, 2, 1, 5),
    _Hh3cDomainSchemeRowStatus_Type()
)
hh3cDomainSchemeRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cDomainSchemeRowStatus.setStatus("current")
_Hh3cDomainSchemeAAAType_Type = Hh3cAAATypeDomainScheme
_Hh3cDomainSchemeAAAType_Object = MibTableColumn
hh3cDomainSchemeAAAType = _Hh3cDomainSchemeAAAType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 46, 2, 2, 1, 6),
    _Hh3cDomainSchemeAAAType_Type()
)
hh3cDomainSchemeAAAType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cDomainSchemeAAAType.setStatus("current")


class _Hh3cDomainSchemeAAAName_Type(OctetString):
    """Custom type hh3cDomainSchemeAAAName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Hh3cDomainSchemeAAAName_Type.__name__ = "OctetString"
_Hh3cDomainSchemeAAAName_Object = MibTableColumn
hh3cDomainSchemeAAAName = _Hh3cDomainSchemeAAAName_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 46, 2, 2, 1, 7),
    _Hh3cDomainSchemeAAAName_Type()
)
hh3cDomainSchemeAAAName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cDomainSchemeAAAName.setStatus("current")
_Hh3cDomainSchemeAccessMode_Type = Hh3cAccessModeofDomainScheme
_Hh3cDomainSchemeAccessMode_Object = MibTableColumn
hh3cDomainSchemeAccessMode = _Hh3cDomainSchemeAccessMode_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 46, 2, 2, 1, 8),
    _Hh3cDomainSchemeAccessMode_Type()
)
hh3cDomainSchemeAccessMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cDomainSchemeAccessMode.setStatus("current")
_Hh3cDomainIpPoolTable_Object = MibTable
hh3cDomainIpPoolTable = _Hh3cDomainIpPoolTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 46, 2, 3)
)
if mibBuilder.loadTexts:
    hh3cDomainIpPoolTable.setStatus("current")
_Hh3cDomainIpPoolEntry_Object = MibTableRow
hh3cDomainIpPoolEntry = _Hh3cDomainIpPoolEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 46, 2, 3, 1)
)
hh3cDomainIpPoolEntry.setIndexNames(
    (0, "HH3C-DOMAIN-MIB", "hh3cDomainName"),
    (0, "HH3C-DOMAIN-MIB", "hh3cDomainIpPoolNum"),
)
if mibBuilder.loadTexts:
    hh3cDomainIpPoolEntry.setStatus("current")


class _Hh3cDomainIpPoolNum_Type(Integer32):
    """Custom type hh3cDomainIpPoolNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 99),
    )


_Hh3cDomainIpPoolNum_Type.__name__ = "Integer32"
_Hh3cDomainIpPoolNum_Object = MibTableColumn
hh3cDomainIpPoolNum = _Hh3cDomainIpPoolNum_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 46, 2, 3, 1, 1),
    _Hh3cDomainIpPoolNum_Type()
)
hh3cDomainIpPoolNum.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cDomainIpPoolNum.setStatus("current")
_Hh3cDomainIpPoolLowIpAddrType_Type = InetAddressType
_Hh3cDomainIpPoolLowIpAddrType_Object = MibTableColumn
hh3cDomainIpPoolLowIpAddrType = _Hh3cDomainIpPoolLowIpAddrType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 46, 2, 3, 1, 2),
    _Hh3cDomainIpPoolLowIpAddrType_Type()
)
hh3cDomainIpPoolLowIpAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cDomainIpPoolLowIpAddrType.setStatus("current")
_Hh3cDomainIpPoolLowIpAddr_Type = InetAddress
_Hh3cDomainIpPoolLowIpAddr_Object = MibTableColumn
hh3cDomainIpPoolLowIpAddr = _Hh3cDomainIpPoolLowIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 46, 2, 3, 1, 3),
    _Hh3cDomainIpPoolLowIpAddr_Type()
)
hh3cDomainIpPoolLowIpAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cDomainIpPoolLowIpAddr.setStatus("current")
_Hh3cDomainIpPoolLen_Type = Integer32
_Hh3cDomainIpPoolLen_Object = MibTableColumn
hh3cDomainIpPoolLen = _Hh3cDomainIpPoolLen_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 46, 2, 3, 1, 4),
    _Hh3cDomainIpPoolLen_Type()
)
hh3cDomainIpPoolLen.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cDomainIpPoolLen.setStatus("current")
_Hh3cDomainIpPoolRowStatus_Type = RowStatus
_Hh3cDomainIpPoolRowStatus_Object = MibTableColumn
hh3cDomainIpPoolRowStatus = _Hh3cDomainIpPoolRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 46, 2, 3, 1, 5),
    _Hh3cDomainIpPoolRowStatus_Type()
)
hh3cDomainIpPoolRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cDomainIpPoolRowStatus.setStatus("current")
_Hh3cDomainStatTable_Object = MibTable
hh3cDomainStatTable = _Hh3cDomainStatTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 46, 2, 4)
)
if mibBuilder.loadTexts:
    hh3cDomainStatTable.setStatus("current")
_Hh3cDomainStatEntry_Object = MibTableRow
hh3cDomainStatEntry = _Hh3cDomainStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 46, 2, 4, 1)
)
hh3cDomainStatEntry.setIndexNames(
    (0, "HH3C-DOMAIN-MIB", "hh3cDomainName"),
)
if mibBuilder.loadTexts:
    hh3cDomainStatEntry.setStatus("current")
_Hh3cDomainAccessedNum_Type = Unsigned32
_Hh3cDomainAccessedNum_Object = MibTableColumn
hh3cDomainAccessedNum = _Hh3cDomainAccessedNum_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 46, 2, 4, 1, 1),
    _Hh3cDomainAccessedNum_Type()
)
hh3cDomainAccessedNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDomainAccessedNum.setStatus("current")
_Hh3cDomainOnlineNum_Type = Unsigned32
_Hh3cDomainOnlineNum_Object = MibTableColumn
hh3cDomainOnlineNum = _Hh3cDomainOnlineNum_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 46, 2, 4, 1, 2),
    _Hh3cDomainOnlineNum_Type()
)
hh3cDomainOnlineNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDomainOnlineNum.setStatus("current")
_Hh3cDomainOnlinePPPUser_Type = Unsigned32
_Hh3cDomainOnlinePPPUser_Object = MibTableColumn
hh3cDomainOnlinePPPUser = _Hh3cDomainOnlinePPPUser_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 46, 2, 4, 1, 3),
    _Hh3cDomainOnlinePPPUser_Type()
)
hh3cDomainOnlinePPPUser.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDomainOnlinePPPUser.setStatus("current")
_Hh3cDomainOnlineIPoEUser_Type = Unsigned32
_Hh3cDomainOnlineIPoEUser_Object = MibTableColumn
hh3cDomainOnlineIPoEUser = _Hh3cDomainOnlineIPoEUser_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 46, 2, 4, 1, 4),
    _Hh3cDomainOnlineIPoEUser_Type()
)
hh3cDomainOnlineIPoEUser.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDomainOnlineIPoEUser.setStatus("current")
_Hh3cDomainOnlinePPPoEUser_Type = Unsigned32
_Hh3cDomainOnlinePPPoEUser_Object = MibTableColumn
hh3cDomainOnlinePPPoEUser = _Hh3cDomainOnlinePPPoEUser_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 46, 2, 4, 1, 5),
    _Hh3cDomainOnlinePPPoEUser_Type()
)
hh3cDomainOnlinePPPoEUser.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDomainOnlinePPPoEUser.setStatus("current")
_Hh3cDomainOnlinePPPoAUser_Type = Unsigned32
_Hh3cDomainOnlinePPPoAUser_Object = MibTableColumn
hh3cDomainOnlinePPPoAUser = _Hh3cDomainOnlinePPPoAUser_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 46, 2, 4, 1, 6),
    _Hh3cDomainOnlinePPPoAUser_Type()
)
hh3cDomainOnlinePPPoAUser.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDomainOnlinePPPoAUser.setStatus("current")
_Hh3cDomainOnlinePPPoFRUser_Type = Unsigned32
_Hh3cDomainOnlinePPPoFRUser_Object = MibTableColumn
hh3cDomainOnlinePPPoFRUser = _Hh3cDomainOnlinePPPoFRUser_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 46, 2, 4, 1, 7),
    _Hh3cDomainOnlinePPPoFRUser_Type()
)
hh3cDomainOnlinePPPoFRUser.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDomainOnlinePPPoFRUser.setStatus("current")
_Hh3cDomainOnlineLacUser_Type = Unsigned32
_Hh3cDomainOnlineLacUser_Object = MibTableColumn
hh3cDomainOnlineLacUser = _Hh3cDomainOnlineLacUser_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 46, 2, 4, 1, 8),
    _Hh3cDomainOnlineLacUser_Type()
)
hh3cDomainOnlineLacUser.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDomainOnlineLacUser.setStatus("current")
_Hh3cDomainOnlineLnsUser_Type = Unsigned32
_Hh3cDomainOnlineLnsUser_Object = MibTableColumn
hh3cDomainOnlineLnsUser = _Hh3cDomainOnlineLnsUser_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 46, 2, 4, 1, 9),
    _Hh3cDomainOnlineLnsUser_Type()
)
hh3cDomainOnlineLnsUser.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDomainOnlineLnsUser.setStatus("current")
_Hh3cDomainOnlineIPoEBindAuthUser_Type = Unsigned32
_Hh3cDomainOnlineIPoEBindAuthUser_Object = MibTableColumn
hh3cDomainOnlineIPoEBindAuthUser = _Hh3cDomainOnlineIPoEBindAuthUser_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 46, 2, 4, 1, 10),
    _Hh3cDomainOnlineIPoEBindAuthUser_Type()
)
hh3cDomainOnlineIPoEBindAuthUser.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDomainOnlineIPoEBindAuthUser.setStatus("current")
_Hh3cDomainOnlineIPoEWebAuthUser_Type = Unsigned32
_Hh3cDomainOnlineIPoEWebAuthUser_Object = MibTableColumn
hh3cDomainOnlineIPoEWebAuthUser = _Hh3cDomainOnlineIPoEWebAuthUser_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 46, 2, 4, 1, 11),
    _Hh3cDomainOnlineIPoEWebAuthUser_Type()
)
hh3cDomainOnlineIPoEWebAuthUser.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDomainOnlineIPoEWebAuthUser.setStatus("current")
_Hh3cDomainOnlineLeasedUser_Type = Unsigned32
_Hh3cDomainOnlineLeasedUser_Object = MibTableColumn
hh3cDomainOnlineLeasedUser = _Hh3cDomainOnlineLeasedUser_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 46, 2, 4, 1, 12),
    _Hh3cDomainOnlineLeasedUser_Type()
)
hh3cDomainOnlineLeasedUser.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDomainOnlineLeasedUser.setStatus("current")
_Hh3cDomainOnlineIPv4User_Type = Unsigned32
_Hh3cDomainOnlineIPv4User_Object = MibTableColumn
hh3cDomainOnlineIPv4User = _Hh3cDomainOnlineIPv4User_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 46, 2, 4, 1, 13),
    _Hh3cDomainOnlineIPv4User_Type()
)
hh3cDomainOnlineIPv4User.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDomainOnlineIPv4User.setStatus("current")
_Hh3cDomainOnlineIPv6User_Type = Unsigned32
_Hh3cDomainOnlineIPv6User_Object = MibTableColumn
hh3cDomainOnlineIPv6User = _Hh3cDomainOnlineIPv6User_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 46, 2, 4, 1, 14),
    _Hh3cDomainOnlineIPv6User_Type()
)
hh3cDomainOnlineIPv6User.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDomainOnlineIPv6User.setStatus("current")
_Hh3cDomainOnlineDualStackUser_Type = Unsigned32
_Hh3cDomainOnlineDualStackUser_Object = MibTableColumn
hh3cDomainOnlineDualStackUser = _Hh3cDomainOnlineDualStackUser_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 46, 2, 4, 1, 15),
    _Hh3cDomainOnlineDualStackUser_Type()
)
hh3cDomainOnlineDualStackUser.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDomainOnlineDualStackUser.setStatus("current")
_Hh3cDomainIPPoolStatTable_Object = MibTable
hh3cDomainIPPoolStatTable = _Hh3cDomainIPPoolStatTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 46, 2, 5)
)
if mibBuilder.loadTexts:
    hh3cDomainIPPoolStatTable.setStatus("current")
_Hh3cDomainIPPoolStatEntry_Object = MibTableRow
hh3cDomainIPPoolStatEntry = _Hh3cDomainIPPoolStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 46, 2, 5, 1)
)
hh3cDomainIPPoolStatEntry.setIndexNames(
    (0, "HH3C-DOMAIN-MIB", "hh3cDomainName"),
)
if mibBuilder.loadTexts:
    hh3cDomainIPPoolStatEntry.setStatus("current")
_Hh3cDomainIPTotalNum_Type = Unsigned32
_Hh3cDomainIPTotalNum_Object = MibTableColumn
hh3cDomainIPTotalNum = _Hh3cDomainIPTotalNum_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 46, 2, 5, 1, 1),
    _Hh3cDomainIPTotalNum_Type()
)
hh3cDomainIPTotalNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDomainIPTotalNum.setStatus("current")
_Hh3cDomainIPUsedNum_Type = Unsigned32
_Hh3cDomainIPUsedNum_Object = MibTableColumn
hh3cDomainIPUsedNum = _Hh3cDomainIPUsedNum_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 46, 2, 5, 1, 2),
    _Hh3cDomainIPUsedNum_Type()
)
hh3cDomainIPUsedNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDomainIPUsedNum.setStatus("current")
_Hh3cDomainIPConflictNum_Type = Unsigned32
_Hh3cDomainIPConflictNum_Object = MibTableColumn
hh3cDomainIPConflictNum = _Hh3cDomainIPConflictNum_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 46, 2, 5, 1, 3),
    _Hh3cDomainIPConflictNum_Type()
)
hh3cDomainIPConflictNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDomainIPConflictNum.setStatus("current")
_Hh3cDomainIPExcludeNum_Type = Unsigned32
_Hh3cDomainIPExcludeNum_Object = MibTableColumn
hh3cDomainIPExcludeNum = _Hh3cDomainIPExcludeNum_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 46, 2, 5, 1, 4),
    _Hh3cDomainIPExcludeNum_Type()
)
hh3cDomainIPExcludeNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDomainIPExcludeNum.setStatus("current")
_Hh3cDomainIPIdleNum_Type = Unsigned32
_Hh3cDomainIPIdleNum_Object = MibTableColumn
hh3cDomainIPIdleNum = _Hh3cDomainIPIdleNum_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 46, 2, 5, 1, 5),
    _Hh3cDomainIPIdleNum_Type()
)
hh3cDomainIPIdleNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDomainIPIdleNum.setStatus("current")


class _Hh3cDomainIPUsedPercent_Type(OctetString):
    """Custom type hh3cDomainIPUsedPercent based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Hh3cDomainIPUsedPercent_Type.__name__ = "OctetString"
_Hh3cDomainIPUsedPercent_Object = MibTableColumn
hh3cDomainIPUsedPercent = _Hh3cDomainIPUsedPercent_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 46, 2, 5, 1, 6),
    _Hh3cDomainIPUsedPercent_Type()
)
hh3cDomainIPUsedPercent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDomainIPUsedPercent.setStatus("current")
_Hh3cDomainIPv6AddressTotalNum_Type = Unsigned32
_Hh3cDomainIPv6AddressTotalNum_Object = MibTableColumn
hh3cDomainIPv6AddressTotalNum = _Hh3cDomainIPv6AddressTotalNum_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 46, 2, 5, 1, 7),
    _Hh3cDomainIPv6AddressTotalNum_Type()
)
hh3cDomainIPv6AddressTotalNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDomainIPv6AddressTotalNum.setStatus("current")
_Hh3cDomainIPv6AddressUsedNum_Type = Unsigned32
_Hh3cDomainIPv6AddressUsedNum_Object = MibTableColumn
hh3cDomainIPv6AddressUsedNum = _Hh3cDomainIPv6AddressUsedNum_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 46, 2, 5, 1, 8),
    _Hh3cDomainIPv6AddressUsedNum_Type()
)
hh3cDomainIPv6AddressUsedNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDomainIPv6AddressUsedNum.setStatus("current")
_Hh3cDomainIPv6AddressFreeNum_Type = Unsigned32
_Hh3cDomainIPv6AddressFreeNum_Object = MibTableColumn
hh3cDomainIPv6AddressFreeNum = _Hh3cDomainIPv6AddressFreeNum_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 46, 2, 5, 1, 9),
    _Hh3cDomainIPv6AddressFreeNum_Type()
)
hh3cDomainIPv6AddressFreeNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDomainIPv6AddressFreeNum.setStatus("current")
_Hh3cDomainIPv6AddressConflictNum_Type = Unsigned32
_Hh3cDomainIPv6AddressConflictNum_Object = MibTableColumn
hh3cDomainIPv6AddressConflictNum = _Hh3cDomainIPv6AddressConflictNum_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 46, 2, 5, 1, 10),
    _Hh3cDomainIPv6AddressConflictNum_Type()
)
hh3cDomainIPv6AddressConflictNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDomainIPv6AddressConflictNum.setStatus("current")
_Hh3cDomainIPv6AddressExcludeNum_Type = Unsigned32
_Hh3cDomainIPv6AddressExcludeNum_Object = MibTableColumn
hh3cDomainIPv6AddressExcludeNum = _Hh3cDomainIPv6AddressExcludeNum_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 46, 2, 5, 1, 11),
    _Hh3cDomainIPv6AddressExcludeNum_Type()
)
hh3cDomainIPv6AddressExcludeNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDomainIPv6AddressExcludeNum.setStatus("current")


class _Hh3cDomainIPv6AddressUsedPercent_Type(OctetString):
    """Custom type hh3cDomainIPv6AddressUsedPercent based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_Hh3cDomainIPv6AddressUsedPercent_Type.__name__ = "OctetString"
_Hh3cDomainIPv6AddressUsedPercent_Object = MibTableColumn
hh3cDomainIPv6AddressUsedPercent = _Hh3cDomainIPv6AddressUsedPercent_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 46, 2, 5, 1, 12),
    _Hh3cDomainIPv6AddressUsedPercent_Type()
)
hh3cDomainIPv6AddressUsedPercent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDomainIPv6AddressUsedPercent.setStatus("current")
_Hh3cDomainNDRAPrefixTotalNum_Type = Unsigned32
_Hh3cDomainNDRAPrefixTotalNum_Object = MibTableColumn
hh3cDomainNDRAPrefixTotalNum = _Hh3cDomainNDRAPrefixTotalNum_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 46, 2, 5, 1, 13),
    _Hh3cDomainNDRAPrefixTotalNum_Type()
)
hh3cDomainNDRAPrefixTotalNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDomainNDRAPrefixTotalNum.setStatus("current")
_Hh3cDomainNDRAPrefixUsedNum_Type = Unsigned32
_Hh3cDomainNDRAPrefixUsedNum_Object = MibTableColumn
hh3cDomainNDRAPrefixUsedNum = _Hh3cDomainNDRAPrefixUsedNum_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 46, 2, 5, 1, 14),
    _Hh3cDomainNDRAPrefixUsedNum_Type()
)
hh3cDomainNDRAPrefixUsedNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDomainNDRAPrefixUsedNum.setStatus("current")
_Hh3cDomainNDRAPrefixFreeNum_Type = Unsigned32
_Hh3cDomainNDRAPrefixFreeNum_Object = MibTableColumn
hh3cDomainNDRAPrefixFreeNum = _Hh3cDomainNDRAPrefixFreeNum_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 46, 2, 5, 1, 15),
    _Hh3cDomainNDRAPrefixFreeNum_Type()
)
hh3cDomainNDRAPrefixFreeNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDomainNDRAPrefixFreeNum.setStatus("current")
_Hh3cDomainNDRAPrefixConflictNum_Type = Unsigned32
_Hh3cDomainNDRAPrefixConflictNum_Object = MibTableColumn
hh3cDomainNDRAPrefixConflictNum = _Hh3cDomainNDRAPrefixConflictNum_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 46, 2, 5, 1, 16),
    _Hh3cDomainNDRAPrefixConflictNum_Type()
)
hh3cDomainNDRAPrefixConflictNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDomainNDRAPrefixConflictNum.setStatus("current")
_Hh3cDomainNDRAPrefixExcludeNum_Type = Unsigned32
_Hh3cDomainNDRAPrefixExcludeNum_Object = MibTableColumn
hh3cDomainNDRAPrefixExcludeNum = _Hh3cDomainNDRAPrefixExcludeNum_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 46, 2, 5, 1, 17),
    _Hh3cDomainNDRAPrefixExcludeNum_Type()
)
hh3cDomainNDRAPrefixExcludeNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDomainNDRAPrefixExcludeNum.setStatus("current")


class _Hh3cDomainNDRAPrefixUsedPercent_Type(OctetString):
    """Custom type hh3cDomainNDRAPrefixUsedPercent based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_Hh3cDomainNDRAPrefixUsedPercent_Type.__name__ = "OctetString"
_Hh3cDomainNDRAPrefixUsedPercent_Object = MibTableColumn
hh3cDomainNDRAPrefixUsedPercent = _Hh3cDomainNDRAPrefixUsedPercent_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 46, 2, 5, 1, 18),
    _Hh3cDomainNDRAPrefixUsedPercent_Type()
)
hh3cDomainNDRAPrefixUsedPercent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDomainNDRAPrefixUsedPercent.setStatus("current")
_Hh3cDomainPDPrefixTotalNum_Type = Unsigned32
_Hh3cDomainPDPrefixTotalNum_Object = MibTableColumn
hh3cDomainPDPrefixTotalNum = _Hh3cDomainPDPrefixTotalNum_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 46, 2, 5, 1, 19),
    _Hh3cDomainPDPrefixTotalNum_Type()
)
hh3cDomainPDPrefixTotalNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDomainPDPrefixTotalNum.setStatus("current")
_Hh3cDomainPDPrefixUsedNum_Type = Unsigned32
_Hh3cDomainPDPrefixUsedNum_Object = MibTableColumn
hh3cDomainPDPrefixUsedNum = _Hh3cDomainPDPrefixUsedNum_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 46, 2, 5, 1, 20),
    _Hh3cDomainPDPrefixUsedNum_Type()
)
hh3cDomainPDPrefixUsedNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDomainPDPrefixUsedNum.setStatus("current")
_Hh3cDomainPDPrefixFreeNum_Type = Unsigned32
_Hh3cDomainPDPrefixFreeNum_Object = MibTableColumn
hh3cDomainPDPrefixFreeNum = _Hh3cDomainPDPrefixFreeNum_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 46, 2, 5, 1, 21),
    _Hh3cDomainPDPrefixFreeNum_Type()
)
hh3cDomainPDPrefixFreeNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDomainPDPrefixFreeNum.setStatus("current")
_Hh3cDomainPDPrefixConflictNum_Type = Unsigned32
_Hh3cDomainPDPrefixConflictNum_Object = MibTableColumn
hh3cDomainPDPrefixConflictNum = _Hh3cDomainPDPrefixConflictNum_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 46, 2, 5, 1, 22),
    _Hh3cDomainPDPrefixConflictNum_Type()
)
hh3cDomainPDPrefixConflictNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDomainPDPrefixConflictNum.setStatus("current")
_Hh3cDomainPDPrefixExcludeNum_Type = Unsigned32
_Hh3cDomainPDPrefixExcludeNum_Object = MibTableColumn
hh3cDomainPDPrefixExcludeNum = _Hh3cDomainPDPrefixExcludeNum_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 46, 2, 5, 1, 23),
    _Hh3cDomainPDPrefixExcludeNum_Type()
)
hh3cDomainPDPrefixExcludeNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDomainPDPrefixExcludeNum.setStatus("current")


class _Hh3cDomainPDPrefixUsedPercent_Type(OctetString):
    """Custom type hh3cDomainPDPrefixUsedPercent based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_Hh3cDomainPDPrefixUsedPercent_Type.__name__ = "OctetString"
_Hh3cDomainPDPrefixUsedPercent_Object = MibTableColumn
hh3cDomainPDPrefixUsedPercent = _Hh3cDomainPDPrefixUsedPercent_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 46, 2, 5, 1, 24),
    _Hh3cDomainPDPrefixUsedPercent_Type()
)
hh3cDomainPDPrefixUsedPercent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDomainPDPrefixUsedPercent.setStatus("current")
_Hh3cDomainNatBindingTable_Object = MibTable
hh3cDomainNatBindingTable = _Hh3cDomainNatBindingTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 46, 2, 6)
)
if mibBuilder.loadTexts:
    hh3cDomainNatBindingTable.setStatus("current")
_Hh3cDomainNatBindingEntry_Object = MibTableRow
hh3cDomainNatBindingEntry = _Hh3cDomainNatBindingEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 46, 2, 6, 1)
)
hh3cDomainNatBindingEntry.setIndexNames(
    (0, "HH3C-DOMAIN-MIB", "hh3cDomainName"),
    (0, "HH3C-DOMAIN-MIB", "hh3cDomainNatBindingUserGroupName"),
)
if mibBuilder.loadTexts:
    hh3cDomainNatBindingEntry.setStatus("current")


class _Hh3cDomainNatBindingUserGroupName_Type(OctetString):
    """Custom type hh3cDomainNatBindingUserGroupName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_Hh3cDomainNatBindingUserGroupName_Type.__name__ = "OctetString"
_Hh3cDomainNatBindingUserGroupName_Object = MibTableColumn
hh3cDomainNatBindingUserGroupName = _Hh3cDomainNatBindingUserGroupName_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 46, 2, 6, 1, 1),
    _Hh3cDomainNatBindingUserGroupName_Type()
)
hh3cDomainNatBindingUserGroupName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDomainNatBindingUserGroupName.setStatus("current")


class _Hh3cDomainNatBindingNatInstance_Type(OctetString):
    """Custom type hh3cDomainNatBindingNatInstance based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_Hh3cDomainNatBindingNatInstance_Type.__name__ = "OctetString"
_Hh3cDomainNatBindingNatInstance_Object = MibTableColumn
hh3cDomainNatBindingNatInstance = _Hh3cDomainNatBindingNatInstance_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 46, 2, 6, 1, 2),
    _Hh3cDomainNatBindingNatInstance_Type()
)
hh3cDomainNatBindingNatInstance.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cDomainNatBindingNatInstance.setStatus("current")
_Hh3cDomainNatBindingRowStatus_Type = RowStatus
_Hh3cDomainNatBindingRowStatus_Object = MibTableColumn
hh3cDomainNatBindingRowStatus = _Hh3cDomainNatBindingRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 46, 2, 6, 1, 3),
    _Hh3cDomainNatBindingRowStatus_Type()
)
hh3cDomainNatBindingRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cDomainNatBindingRowStatus.setStatus("current")
_Hh3cDomainUpStatTable_Object = MibTable
hh3cDomainUpStatTable = _Hh3cDomainUpStatTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 46, 2, 7)
)
if mibBuilder.loadTexts:
    hh3cDomainUpStatTable.setStatus("current")
_Hh3cDomainUpStatEntry_Object = MibTableRow
hh3cDomainUpStatEntry = _Hh3cDomainUpStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 46, 2, 7, 1)
)
hh3cDomainUpStatEntry.setIndexNames(
    (0, "HH3C-DOMAIN-MIB", "hh3cDomainName"),
    (0, "HH3C-DOMAIN-MIB", "hh3cDomainUpId"),
)
if mibBuilder.loadTexts:
    hh3cDomainUpStatEntry.setStatus("current")


class _Hh3cDomainUpId_Type(Unsigned32):
    """Custom type hh3cDomainUpId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1024, 2047),
    )


_Hh3cDomainUpId_Type.__name__ = "Unsigned32"
_Hh3cDomainUpId_Object = MibTableColumn
hh3cDomainUpId = _Hh3cDomainUpId_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 46, 2, 7, 1, 1),
    _Hh3cDomainUpId_Type()
)
hh3cDomainUpId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cDomainUpId.setStatus("current")
_Hh3cDomainUpAccessedNum_Type = Unsigned32
_Hh3cDomainUpAccessedNum_Object = MibTableColumn
hh3cDomainUpAccessedNum = _Hh3cDomainUpAccessedNum_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 46, 2, 7, 1, 2),
    _Hh3cDomainUpAccessedNum_Type()
)
hh3cDomainUpAccessedNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDomainUpAccessedNum.setStatus("current")
_Hh3cDomainUpOnlineNum_Type = Unsigned32
_Hh3cDomainUpOnlineNum_Object = MibTableColumn
hh3cDomainUpOnlineNum = _Hh3cDomainUpOnlineNum_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 46, 2, 7, 1, 3),
    _Hh3cDomainUpOnlineNum_Type()
)
hh3cDomainUpOnlineNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDomainUpOnlineNum.setStatus("current")
_Hh3cDomainUpOnlinePPPUser_Type = Unsigned32
_Hh3cDomainUpOnlinePPPUser_Object = MibTableColumn
hh3cDomainUpOnlinePPPUser = _Hh3cDomainUpOnlinePPPUser_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 46, 2, 7, 1, 4),
    _Hh3cDomainUpOnlinePPPUser_Type()
)
hh3cDomainUpOnlinePPPUser.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDomainUpOnlinePPPUser.setStatus("current")
_Hh3cDomainUpOnlineIPoEUser_Type = Unsigned32
_Hh3cDomainUpOnlineIPoEUser_Object = MibTableColumn
hh3cDomainUpOnlineIPoEUser = _Hh3cDomainUpOnlineIPoEUser_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 46, 2, 7, 1, 5),
    _Hh3cDomainUpOnlineIPoEUser_Type()
)
hh3cDomainUpOnlineIPoEUser.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDomainUpOnlineIPoEUser.setStatus("current")
_Hh3cDomainUpOnlinePPPoEUser_Type = Unsigned32
_Hh3cDomainUpOnlinePPPoEUser_Object = MibTableColumn
hh3cDomainUpOnlinePPPoEUser = _Hh3cDomainUpOnlinePPPoEUser_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 46, 2, 7, 1, 6),
    _Hh3cDomainUpOnlinePPPoEUser_Type()
)
hh3cDomainUpOnlinePPPoEUser.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDomainUpOnlinePPPoEUser.setStatus("current")
_Hh3cDomainUpOnlinePPPoAUser_Type = Unsigned32
_Hh3cDomainUpOnlinePPPoAUser_Object = MibTableColumn
hh3cDomainUpOnlinePPPoAUser = _Hh3cDomainUpOnlinePPPoAUser_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 46, 2, 7, 1, 7),
    _Hh3cDomainUpOnlinePPPoAUser_Type()
)
hh3cDomainUpOnlinePPPoAUser.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDomainUpOnlinePPPoAUser.setStatus("current")
_Hh3cDomainUpOnlinePPPoFRUser_Type = Unsigned32
_Hh3cDomainUpOnlinePPPoFRUser_Object = MibTableColumn
hh3cDomainUpOnlinePPPoFRUser = _Hh3cDomainUpOnlinePPPoFRUser_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 46, 2, 7, 1, 8),
    _Hh3cDomainUpOnlinePPPoFRUser_Type()
)
hh3cDomainUpOnlinePPPoFRUser.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDomainUpOnlinePPPoFRUser.setStatus("current")
_Hh3cDomainUpOnlineLacUser_Type = Unsigned32
_Hh3cDomainUpOnlineLacUser_Object = MibTableColumn
hh3cDomainUpOnlineLacUser = _Hh3cDomainUpOnlineLacUser_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 46, 2, 7, 1, 9),
    _Hh3cDomainUpOnlineLacUser_Type()
)
hh3cDomainUpOnlineLacUser.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDomainUpOnlineLacUser.setStatus("current")
_Hh3cDomainUpOnlineLnsUser_Type = Unsigned32
_Hh3cDomainUpOnlineLnsUser_Object = MibTableColumn
hh3cDomainUpOnlineLnsUser = _Hh3cDomainUpOnlineLnsUser_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 46, 2, 7, 1, 10),
    _Hh3cDomainUpOnlineLnsUser_Type()
)
hh3cDomainUpOnlineLnsUser.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDomainUpOnlineLnsUser.setStatus("current")
_Hh3cDomainUpOnlineIPoEBindAuthUser_Type = Unsigned32
_Hh3cDomainUpOnlineIPoEBindAuthUser_Object = MibTableColumn
hh3cDomainUpOnlineIPoEBindAuthUser = _Hh3cDomainUpOnlineIPoEBindAuthUser_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 46, 2, 7, 1, 11),
    _Hh3cDomainUpOnlineIPoEBindAuthUser_Type()
)
hh3cDomainUpOnlineIPoEBindAuthUser.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDomainUpOnlineIPoEBindAuthUser.setStatus("current")
_Hh3cDomainUpOnlineIPoEWebAuthUser_Type = Unsigned32
_Hh3cDomainUpOnlineIPoEWebAuthUser_Object = MibTableColumn
hh3cDomainUpOnlineIPoEWebAuthUser = _Hh3cDomainUpOnlineIPoEWebAuthUser_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 46, 2, 7, 1, 12),
    _Hh3cDomainUpOnlineIPoEWebAuthUser_Type()
)
hh3cDomainUpOnlineIPoEWebAuthUser.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDomainUpOnlineIPoEWebAuthUser.setStatus("current")
_Hh3cDomainUpOnlineLeasedUser_Type = Unsigned32
_Hh3cDomainUpOnlineLeasedUser_Object = MibTableColumn
hh3cDomainUpOnlineLeasedUser = _Hh3cDomainUpOnlineLeasedUser_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 46, 2, 7, 1, 13),
    _Hh3cDomainUpOnlineLeasedUser_Type()
)
hh3cDomainUpOnlineLeasedUser.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDomainUpOnlineLeasedUser.setStatus("current")
_Hh3cDomainUpOnlineIPv4User_Type = Unsigned32
_Hh3cDomainUpOnlineIPv4User_Object = MibTableColumn
hh3cDomainUpOnlineIPv4User = _Hh3cDomainUpOnlineIPv4User_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 46, 2, 7, 1, 14),
    _Hh3cDomainUpOnlineIPv4User_Type()
)
hh3cDomainUpOnlineIPv4User.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDomainUpOnlineIPv4User.setStatus("current")
_Hh3cDomainUpOnlineIPv6User_Type = Unsigned32
_Hh3cDomainUpOnlineIPv6User_Object = MibTableColumn
hh3cDomainUpOnlineIPv6User = _Hh3cDomainUpOnlineIPv6User_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 46, 2, 7, 1, 15),
    _Hh3cDomainUpOnlineIPv6User_Type()
)
hh3cDomainUpOnlineIPv6User.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDomainUpOnlineIPv6User.setStatus("current")
_Hh3cDomainUpOnlineDualStackUser_Type = Unsigned32
_Hh3cDomainUpOnlineDualStackUser_Object = MibTableColumn
hh3cDomainUpOnlineDualStackUser = _Hh3cDomainUpOnlineDualStackUser_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 46, 2, 7, 1, 16),
    _Hh3cDomainUpOnlineDualStackUser_Type()
)
hh3cDomainUpOnlineDualStackUser.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDomainUpOnlineDualStackUser.setStatus("current")
_Hh3cDomainGlobalStat_ObjectIdentity = ObjectIdentity
hh3cDomainGlobalStat = _Hh3cDomainGlobalStat_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 46, 3)
)
_Hh3cDomainGlobalAccessedNum_Type = Unsigned32
_Hh3cDomainGlobalAccessedNum_Object = MibScalar
hh3cDomainGlobalAccessedNum = _Hh3cDomainGlobalAccessedNum_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 46, 3, 1),
    _Hh3cDomainGlobalAccessedNum_Type()
)
hh3cDomainGlobalAccessedNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDomainGlobalAccessedNum.setStatus("current")
_Hh3cDomainGlobalOnlineNum_Type = Unsigned32
_Hh3cDomainGlobalOnlineNum_Object = MibScalar
hh3cDomainGlobalOnlineNum = _Hh3cDomainGlobalOnlineNum_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 46, 3, 2),
    _Hh3cDomainGlobalOnlineNum_Type()
)
hh3cDomainGlobalOnlineNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDomainGlobalOnlineNum.setStatus("current")
_Hh3cDomainGlobalOnlinePPPUser_Type = Unsigned32
_Hh3cDomainGlobalOnlinePPPUser_Object = MibScalar
hh3cDomainGlobalOnlinePPPUser = _Hh3cDomainGlobalOnlinePPPUser_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 46, 3, 3),
    _Hh3cDomainGlobalOnlinePPPUser_Type()
)
hh3cDomainGlobalOnlinePPPUser.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDomainGlobalOnlinePPPUser.setStatus("current")
_Hh3cDomainGlobalOnlineIPoEUser_Type = Unsigned32
_Hh3cDomainGlobalOnlineIPoEUser_Object = MibScalar
hh3cDomainGlobalOnlineIPoEUser = _Hh3cDomainGlobalOnlineIPoEUser_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 46, 3, 4),
    _Hh3cDomainGlobalOnlineIPoEUser_Type()
)
hh3cDomainGlobalOnlineIPoEUser.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDomainGlobalOnlineIPoEUser.setStatus("current")
_Hh3cDomainGlobalOnlinePPPoEUser_Type = Unsigned32
_Hh3cDomainGlobalOnlinePPPoEUser_Object = MibScalar
hh3cDomainGlobalOnlinePPPoEUser = _Hh3cDomainGlobalOnlinePPPoEUser_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 46, 3, 5),
    _Hh3cDomainGlobalOnlinePPPoEUser_Type()
)
hh3cDomainGlobalOnlinePPPoEUser.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDomainGlobalOnlinePPPoEUser.setStatus("current")
_Hh3cDomainGlobalOnlinePPPoAUser_Type = Unsigned32
_Hh3cDomainGlobalOnlinePPPoAUser_Object = MibScalar
hh3cDomainGlobalOnlinePPPoAUser = _Hh3cDomainGlobalOnlinePPPoAUser_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 46, 3, 6),
    _Hh3cDomainGlobalOnlinePPPoAUser_Type()
)
hh3cDomainGlobalOnlinePPPoAUser.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDomainGlobalOnlinePPPoAUser.setStatus("current")
_Hh3cDomainGlobalOnlinePPPoFRUser_Type = Unsigned32
_Hh3cDomainGlobalOnlinePPPoFRUser_Object = MibScalar
hh3cDomainGlobalOnlinePPPoFRUser = _Hh3cDomainGlobalOnlinePPPoFRUser_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 46, 3, 7),
    _Hh3cDomainGlobalOnlinePPPoFRUser_Type()
)
hh3cDomainGlobalOnlinePPPoFRUser.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDomainGlobalOnlinePPPoFRUser.setStatus("current")
_Hh3cDomainGlobalOnlineLacUser_Type = Unsigned32
_Hh3cDomainGlobalOnlineLacUser_Object = MibScalar
hh3cDomainGlobalOnlineLacUser = _Hh3cDomainGlobalOnlineLacUser_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 46, 3, 8),
    _Hh3cDomainGlobalOnlineLacUser_Type()
)
hh3cDomainGlobalOnlineLacUser.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDomainGlobalOnlineLacUser.setStatus("current")
_Hh3cDomainGlobalOnlineLnsUser_Type = Unsigned32
_Hh3cDomainGlobalOnlineLnsUser_Object = MibScalar
hh3cDomainGlobalOnlineLnsUser = _Hh3cDomainGlobalOnlineLnsUser_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 46, 3, 9),
    _Hh3cDomainGlobalOnlineLnsUser_Type()
)
hh3cDomainGlobalOnlineLnsUser.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDomainGlobalOnlineLnsUser.setStatus("current")
_Hh3cDomainGlobalOnlineIPoEBindAuthUser_Type = Unsigned32
_Hh3cDomainGlobalOnlineIPoEBindAuthUser_Object = MibScalar
hh3cDomainGlobalOnlineIPoEBindAuthUser = _Hh3cDomainGlobalOnlineIPoEBindAuthUser_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 46, 3, 10),
    _Hh3cDomainGlobalOnlineIPoEBindAuthUser_Type()
)
hh3cDomainGlobalOnlineIPoEBindAuthUser.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDomainGlobalOnlineIPoEBindAuthUser.setStatus("current")
_Hh3cDomainGlobalOnlineIPoEWebAuthUser_Type = Unsigned32
_Hh3cDomainGlobalOnlineIPoEWebAuthUser_Object = MibScalar
hh3cDomainGlobalOnlineIPoEWebAuthUser = _Hh3cDomainGlobalOnlineIPoEWebAuthUser_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 46, 3, 11),
    _Hh3cDomainGlobalOnlineIPoEWebAuthUser_Type()
)
hh3cDomainGlobalOnlineIPoEWebAuthUser.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDomainGlobalOnlineIPoEWebAuthUser.setStatus("current")
_Hh3cDomainGlobalOnlineLeasedUser_Type = Unsigned32
_Hh3cDomainGlobalOnlineLeasedUser_Object = MibScalar
hh3cDomainGlobalOnlineLeasedUser = _Hh3cDomainGlobalOnlineLeasedUser_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 46, 3, 12),
    _Hh3cDomainGlobalOnlineLeasedUser_Type()
)
hh3cDomainGlobalOnlineLeasedUser.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDomainGlobalOnlineLeasedUser.setStatus("current")
_Hh3cDomainGlobalTotalIPv4OnlineNum_Type = Unsigned32
_Hh3cDomainGlobalTotalIPv4OnlineNum_Object = MibScalar
hh3cDomainGlobalTotalIPv4OnlineNum = _Hh3cDomainGlobalTotalIPv4OnlineNum_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 46, 3, 13),
    _Hh3cDomainGlobalTotalIPv4OnlineNum_Type()
)
hh3cDomainGlobalTotalIPv4OnlineNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDomainGlobalTotalIPv4OnlineNum.setStatus("current")
_Hh3cDomainGlobalTotalIPv6OnlineNum_Type = Unsigned32
_Hh3cDomainGlobalTotalIPv6OnlineNum_Object = MibScalar
hh3cDomainGlobalTotalIPv6OnlineNum = _Hh3cDomainGlobalTotalIPv6OnlineNum_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 46, 3, 14),
    _Hh3cDomainGlobalTotalIPv6OnlineNum_Type()
)
hh3cDomainGlobalTotalIPv6OnlineNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDomainGlobalTotalIPv6OnlineNum.setStatus("current")
_Hh3cDomainGlobalTotalDualStackOnlineNum_Type = Unsigned32
_Hh3cDomainGlobalTotalDualStackOnlineNum_Object = MibScalar
hh3cDomainGlobalTotalDualStackOnlineNum = _Hh3cDomainGlobalTotalDualStackOnlineNum_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 46, 3, 15),
    _Hh3cDomainGlobalTotalDualStackOnlineNum_Type()
)
hh3cDomainGlobalTotalDualStackOnlineNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDomainGlobalTotalDualStackOnlineNum.setStatus("current")
_Hh3cDomainTraps_ObjectIdentity = ObjectIdentity
hh3cDomainTraps = _Hh3cDomainTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 46, 5)
)
_Hh3cDomainTrapsDefine_ObjectIdentity = ObjectIdentity
hh3cDomainTrapsDefine = _Hh3cDomainTrapsDefine_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 46, 5, 0)
)

# Managed Objects groups


# Notification objects

hh3cUserIPAllocAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 46, 5, 0, 1)
)
hh3cUserIPAllocAlarm.setObjects(
      *(("HH3C-DOMAIN-MIB", "hh3cDomainIPUsedPercent"),
        ("HH3C-DOMAIN-MIB", "hh3cDomainIPv4PoolUpperValue"),
        ("HH3C-DOMAIN-MIB", "hh3cDomainIPv4PoolLowerValue"))
)
if mibBuilder.loadTexts:
    hh3cUserIPAllocAlarm.setStatus(
        "current"
    )

hh3cUserIPAllocAlarmResume = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 46, 5, 0, 2)
)
hh3cUserIPAllocAlarmResume.setObjects(
      *(("HH3C-DOMAIN-MIB", "hh3cDomainIPUsedPercent"),
        ("HH3C-DOMAIN-MIB", "hh3cDomainIPv4PoolUpperValue"),
        ("HH3C-DOMAIN-MIB", "hh3cDomainIPv4PoolLowerValue"))
)
if mibBuilder.loadTexts:
    hh3cUserIPAllocAlarmResume.setStatus(
        "current"
    )

hh3cUserIPLowerlimitWarningAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 46, 5, 0, 3)
)
hh3cUserIPLowerlimitWarningAlarm.setObjects(
      *(("HH3C-DOMAIN-MIB", "hh3cDomainIPUsedPercent"),
        ("HH3C-DOMAIN-MIB", "hh3cDomainIPv4PoolUpperValue"),
        ("HH3C-DOMAIN-MIB", "hh3cDomainIPv4PoolLowerValue"))
)
if mibBuilder.loadTexts:
    hh3cUserIPLowerlimitWarningAlarm.setStatus(
        "current"
    )

hh3cUserIPLowerlimitWarningResume = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 46, 5, 0, 4)
)
hh3cUserIPLowerlimitWarningResume.setObjects(
      *(("HH3C-DOMAIN-MIB", "hh3cDomainIPUsedPercent"),
        ("HH3C-DOMAIN-MIB", "hh3cDomainIPv4PoolUpperValue"),
        ("HH3C-DOMAIN-MIB", "hh3cDomainIPv4PoolLowerValue"))
)
if mibBuilder.loadTexts:
    hh3cUserIPLowerlimitWarningResume.setStatus(
        "current"
    )

hh3cUserIPv6AllocAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 46, 5, 0, 5)
)
hh3cUserIPv6AllocAlarm.setObjects(
      *(("HH3C-DOMAIN-MIB", "hh3cDomainIPv6AddressUsedPercent"),
        ("HH3C-DOMAIN-MIB", "hh3cDomainIPv6PoolUpperValue"),
        ("HH3C-DOMAIN-MIB", "hh3cDomainIPv6PoolLowerValue"))
)
if mibBuilder.loadTexts:
    hh3cUserIPv6AllocAlarm.setStatus(
        "current"
    )

hh3cUserIPv6AllocAlarmResume = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 46, 5, 0, 6)
)
hh3cUserIPv6AllocAlarmResume.setObjects(
      *(("HH3C-DOMAIN-MIB", "hh3cDomainIPv6AddressUsedPercent"),
        ("HH3C-DOMAIN-MIB", "hh3cDomainIPv6PoolUpperValue"),
        ("HH3C-DOMAIN-MIB", "hh3cDomainIPv6PoolLowerValue"))
)
if mibBuilder.loadTexts:
    hh3cUserIPv6AllocAlarmResume.setStatus(
        "current"
    )

hh3cUserIPv6LowlimitWarnAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 46, 5, 0, 7)
)
hh3cUserIPv6LowlimitWarnAlarm.setObjects(
      *(("HH3C-DOMAIN-MIB", "hh3cDomainIPv6AddressUsedPercent"),
        ("HH3C-DOMAIN-MIB", "hh3cDomainIPv6PoolUpperValue"),
        ("HH3C-DOMAIN-MIB", "hh3cDomainIPv6PoolLowerValue"))
)
if mibBuilder.loadTexts:
    hh3cUserIPv6LowlimitWarnAlarm.setStatus(
        "current"
    )

hh3cUserIPv6LowlimitWarnResume = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 46, 5, 0, 8)
)
hh3cUserIPv6LowlimitWarnResume.setObjects(
      *(("HH3C-DOMAIN-MIB", "hh3cDomainIPv6AddressUsedPercent"),
        ("HH3C-DOMAIN-MIB", "hh3cDomainIPv6PoolUpperValue"),
        ("HH3C-DOMAIN-MIB", "hh3cDomainIPv6PoolLowerValue"))
)
if mibBuilder.loadTexts:
    hh3cUserIPv6LowlimitWarnResume.setStatus(
        "current"
    )

hh3cUserNDRAPfAllocAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 46, 5, 0, 9)
)
hh3cUserNDRAPfAllocAlarm.setObjects(
      *(("HH3C-DOMAIN-MIB", "hh3cDomainNDRAPrefixUsedPercent"),
        ("HH3C-DOMAIN-MIB", "hh3cDomainIPv6PoolUpperValue"),
        ("HH3C-DOMAIN-MIB", "hh3cDomainIPv6PoolLowerValue"))
)
if mibBuilder.loadTexts:
    hh3cUserNDRAPfAllocAlarm.setStatus(
        "current"
    )

hh3cUserNDRAPfAllocAlarmResume = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 46, 5, 0, 10)
)
hh3cUserNDRAPfAllocAlarmResume.setObjects(
      *(("HH3C-DOMAIN-MIB", "hh3cDomainNDRAPrefixUsedPercent"),
        ("HH3C-DOMAIN-MIB", "hh3cDomainIPv6PoolUpperValue"),
        ("HH3C-DOMAIN-MIB", "hh3cDomainIPv6PoolLowerValue"))
)
if mibBuilder.loadTexts:
    hh3cUserNDRAPfAllocAlarmResume.setStatus(
        "current"
    )

hh3cUserNDRAPfLowlimitWarnAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 46, 5, 0, 11)
)
hh3cUserNDRAPfLowlimitWarnAlarm.setObjects(
      *(("HH3C-DOMAIN-MIB", "hh3cDomainNDRAPrefixUsedPercent"),
        ("HH3C-DOMAIN-MIB", "hh3cDomainIPv6PoolUpperValue"),
        ("HH3C-DOMAIN-MIB", "hh3cDomainIPv6PoolLowerValue"))
)
if mibBuilder.loadTexts:
    hh3cUserNDRAPfLowlimitWarnAlarm.setStatus(
        "current"
    )

hh3cUserNDRAPfLowlimitWarnResume = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 46, 5, 0, 12)
)
hh3cUserNDRAPfLowlimitWarnResume.setObjects(
      *(("HH3C-DOMAIN-MIB", "hh3cDomainNDRAPrefixUsedPercent"),
        ("HH3C-DOMAIN-MIB", "hh3cDomainIPv6PoolUpperValue"),
        ("HH3C-DOMAIN-MIB", "hh3cDomainIPv6PoolLowerValue"))
)
if mibBuilder.loadTexts:
    hh3cUserNDRAPfLowlimitWarnResume.setStatus(
        "current"
    )

hh3cUserPDPfAllocAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 46, 5, 0, 13)
)
hh3cUserPDPfAllocAlarm.setObjects(
      *(("HH3C-DOMAIN-MIB", "hh3cDomainPDPrefixUsedPercent"),
        ("HH3C-DOMAIN-MIB", "hh3cDomainIPv6PoolUpperValue"),
        ("HH3C-DOMAIN-MIB", "hh3cDomainIPv6PoolLowerValue"))
)
if mibBuilder.loadTexts:
    hh3cUserPDPfAllocAlarm.setStatus(
        "current"
    )

hh3cUserPDPfAllocAlarmResume = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 46, 5, 0, 14)
)
hh3cUserPDPfAllocAlarmResume.setObjects(
      *(("HH3C-DOMAIN-MIB", "hh3cDomainPDPrefixUsedPercent"),
        ("HH3C-DOMAIN-MIB", "hh3cDomainIPv6PoolUpperValue"),
        ("HH3C-DOMAIN-MIB", "hh3cDomainIPv6PoolLowerValue"))
)
if mibBuilder.loadTexts:
    hh3cUserPDPfAllocAlarmResume.setStatus(
        "current"
    )

hh3cUserPDPfLowlimitWarnAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 46, 5, 0, 15)
)
hh3cUserPDPfLowlimitWarnAlarm.setObjects(
      *(("HH3C-DOMAIN-MIB", "hh3cDomainPDPrefixUsedPercent"),
        ("HH3C-DOMAIN-MIB", "hh3cDomainIPv6PoolUpperValue"),
        ("HH3C-DOMAIN-MIB", "hh3cDomainIPv6PoolLowerValue"))
)
if mibBuilder.loadTexts:
    hh3cUserPDPfLowlimitWarnAlarm.setStatus(
        "current"
    )

hh3cUserPDPfLowlimitWarnResume = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 46, 5, 0, 16)
)
hh3cUserPDPfLowlimitWarnResume.setObjects(
      *(("HH3C-DOMAIN-MIB", "hh3cDomainPDPrefixUsedPercent"),
        ("HH3C-DOMAIN-MIB", "hh3cDomainIPv6PoolUpperValue"),
        ("HH3C-DOMAIN-MIB", "hh3cDomainIPv6PoolLowerValue"))
)
if mibBuilder.loadTexts:
    hh3cUserPDPfLowlimitWarnResume.setStatus(
        "current"
    )

hh3cUserWebServerDownAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 46, 5, 0, 17)
)
hh3cUserWebServerDownAlarm.setObjects(
    ("HH3C-DOMAIN-MIB", "hh3cDomainActiveWebServerUrl")
)
if mibBuilder.loadTexts:
    hh3cUserWebServerDownAlarm.setStatus(
        "current"
    )

hh3cUserWebServerUpAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 46, 5, 0, 18)
)
hh3cUserWebServerUpAlarm.setObjects(
    ("HH3C-DOMAIN-MIB", "hh3cDomainActiveWebServerUrl")
)
if mibBuilder.loadTexts:
    hh3cUserWebServerUpAlarm.setStatus(
        "current"
    )

hh3cUserWebServerChangeAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 46, 5, 0, 19)
)
hh3cUserWebServerChangeAlarm.setObjects(
    ("HH3C-DOMAIN-MIB", "hh3cDomainActiveWebServerUrl")
)
if mibBuilder.loadTexts:
    hh3cUserWebServerChangeAlarm.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HH3C-DOMAIN-MIB",
    **{"Hh3cModeOfDomainScheme": Hh3cModeOfDomainScheme,
       "Hh3cAAATypeDomainScheme": Hh3cAAATypeDomainScheme,
       "Hh3cAccessModeofDomainScheme": Hh3cAccessModeofDomainScheme,
       "hh3cDomain": hh3cDomain,
       "hh3cDomainControl": hh3cDomainControl,
       "hh3cDomainDefault": hh3cDomainDefault,
       "hh3cDomainTables": hh3cDomainTables,
       "hh3cDomainInfoTable": hh3cDomainInfoTable,
       "hh3cDomainInfoEntry": hh3cDomainInfoEntry,
       "hh3cDomainName": hh3cDomainName,
       "hh3cDomainState": hh3cDomainState,
       "hh3cDomainMaxAccessNum": hh3cDomainMaxAccessNum,
       "hh3cDomainVlanAssignMode": hh3cDomainVlanAssignMode,
       "hh3cDomainIdleCutEnable": hh3cDomainIdleCutEnable,
       "hh3cDomainIdleCutMaxTime": hh3cDomainIdleCutMaxTime,
       "hh3cDomainIdleCutMinFlow": hh3cDomainIdleCutMinFlow,
       "hh3cDomainMessengerEnable": hh3cDomainMessengerEnable,
       "hh3cDomainMessengerLimitTime": hh3cDomainMessengerLimitTime,
       "hh3cDomainMessengerSpanTime": hh3cDomainMessengerSpanTime,
       "hh3cDomainSelfServiceEnable": hh3cDomainSelfServiceEnable,
       "hh3cDomainSelfServiceURL": hh3cDomainSelfServiceURL,
       "hh3cDomainAccFailureAction": hh3cDomainAccFailureAction,
       "hh3cDomainRowStatus": hh3cDomainRowStatus,
       "hh3cDomainCurrentAccessNum": hh3cDomainCurrentAccessNum,
       "hh3cDomainIdleCutTime": hh3cDomainIdleCutTime,
       "hh3cDomainServiceType": hh3cDomainServiceType,
       "hh3cDomainIpPoolName": hh3cDomainIpPoolName,
       "hh3cDomainIpv6PoolName": hh3cDomainIpv6PoolName,
       "hh3cDomainIPv4PoolUpperValue": hh3cDomainIPv4PoolUpperValue,
       "hh3cDomainIPv4PoolLowerValue": hh3cDomainIPv4PoolLowerValue,
       "hh3cDomainIPv6PoolUpperValue": hh3cDomainIPv6PoolUpperValue,
       "hh3cDomainIPv6PoolLowerValue": hh3cDomainIPv6PoolLowerValue,
       "hh3cDomainIpPoolGroupName": hh3cDomainIpPoolGroupName,
       "hh3cDomainIpv6PoolGroupName": hh3cDomainIpv6PoolGroupName,
       "hh3cDomainNdPrefixPoolName": hh3cDomainNdPrefixPoolName,
       "hh3cDomainNdPrefixPoolGroupName": hh3cDomainNdPrefixPoolGroupName,
       "hh3cDomainIpv6Prefix": hh3cDomainIpv6Prefix,
       "hh3cDomainIpv6PrefixLength": hh3cDomainIpv6PrefixLength,
       "hh3cDomainActiveWebServerUrl": hh3cDomainActiveWebServerUrl,
       "hh3cDomainSchemeTable": hh3cDomainSchemeTable,
       "hh3cDomainSchemeEntry": hh3cDomainSchemeEntry,
       "hh3cDomainSchemeIndex": hh3cDomainSchemeIndex,
       "hh3cDomainSchemeMode": hh3cDomainSchemeMode,
       "hh3cDomainAuthSchemeName": hh3cDomainAuthSchemeName,
       "hh3cDomainAcctSchemeName": hh3cDomainAcctSchemeName,
       "hh3cDomainSchemeRowStatus": hh3cDomainSchemeRowStatus,
       "hh3cDomainSchemeAAAType": hh3cDomainSchemeAAAType,
       "hh3cDomainSchemeAAAName": hh3cDomainSchemeAAAName,
       "hh3cDomainSchemeAccessMode": hh3cDomainSchemeAccessMode,
       "hh3cDomainIpPoolTable": hh3cDomainIpPoolTable,
       "hh3cDomainIpPoolEntry": hh3cDomainIpPoolEntry,
       "hh3cDomainIpPoolNum": hh3cDomainIpPoolNum,
       "hh3cDomainIpPoolLowIpAddrType": hh3cDomainIpPoolLowIpAddrType,
       "hh3cDomainIpPoolLowIpAddr": hh3cDomainIpPoolLowIpAddr,
       "hh3cDomainIpPoolLen": hh3cDomainIpPoolLen,
       "hh3cDomainIpPoolRowStatus": hh3cDomainIpPoolRowStatus,
       "hh3cDomainStatTable": hh3cDomainStatTable,
       "hh3cDomainStatEntry": hh3cDomainStatEntry,
       "hh3cDomainAccessedNum": hh3cDomainAccessedNum,
       "hh3cDomainOnlineNum": hh3cDomainOnlineNum,
       "hh3cDomainOnlinePPPUser": hh3cDomainOnlinePPPUser,
       "hh3cDomainOnlineIPoEUser": hh3cDomainOnlineIPoEUser,
       "hh3cDomainOnlinePPPoEUser": hh3cDomainOnlinePPPoEUser,
       "hh3cDomainOnlinePPPoAUser": hh3cDomainOnlinePPPoAUser,
       "hh3cDomainOnlinePPPoFRUser": hh3cDomainOnlinePPPoFRUser,
       "hh3cDomainOnlineLacUser": hh3cDomainOnlineLacUser,
       "hh3cDomainOnlineLnsUser": hh3cDomainOnlineLnsUser,
       "hh3cDomainOnlineIPoEBindAuthUser": hh3cDomainOnlineIPoEBindAuthUser,
       "hh3cDomainOnlineIPoEWebAuthUser": hh3cDomainOnlineIPoEWebAuthUser,
       "hh3cDomainOnlineLeasedUser": hh3cDomainOnlineLeasedUser,
       "hh3cDomainOnlineIPv4User": hh3cDomainOnlineIPv4User,
       "hh3cDomainOnlineIPv6User": hh3cDomainOnlineIPv6User,
       "hh3cDomainOnlineDualStackUser": hh3cDomainOnlineDualStackUser,
       "hh3cDomainIPPoolStatTable": hh3cDomainIPPoolStatTable,
       "hh3cDomainIPPoolStatEntry": hh3cDomainIPPoolStatEntry,
       "hh3cDomainIPTotalNum": hh3cDomainIPTotalNum,
       "hh3cDomainIPUsedNum": hh3cDomainIPUsedNum,
       "hh3cDomainIPConflictNum": hh3cDomainIPConflictNum,
       "hh3cDomainIPExcludeNum": hh3cDomainIPExcludeNum,
       "hh3cDomainIPIdleNum": hh3cDomainIPIdleNum,
       "hh3cDomainIPUsedPercent": hh3cDomainIPUsedPercent,
       "hh3cDomainIPv6AddressTotalNum": hh3cDomainIPv6AddressTotalNum,
       "hh3cDomainIPv6AddressUsedNum": hh3cDomainIPv6AddressUsedNum,
       "hh3cDomainIPv6AddressFreeNum": hh3cDomainIPv6AddressFreeNum,
       "hh3cDomainIPv6AddressConflictNum": hh3cDomainIPv6AddressConflictNum,
       "hh3cDomainIPv6AddressExcludeNum": hh3cDomainIPv6AddressExcludeNum,
       "hh3cDomainIPv6AddressUsedPercent": hh3cDomainIPv6AddressUsedPercent,
       "hh3cDomainNDRAPrefixTotalNum": hh3cDomainNDRAPrefixTotalNum,
       "hh3cDomainNDRAPrefixUsedNum": hh3cDomainNDRAPrefixUsedNum,
       "hh3cDomainNDRAPrefixFreeNum": hh3cDomainNDRAPrefixFreeNum,
       "hh3cDomainNDRAPrefixConflictNum": hh3cDomainNDRAPrefixConflictNum,
       "hh3cDomainNDRAPrefixExcludeNum": hh3cDomainNDRAPrefixExcludeNum,
       "hh3cDomainNDRAPrefixUsedPercent": hh3cDomainNDRAPrefixUsedPercent,
       "hh3cDomainPDPrefixTotalNum": hh3cDomainPDPrefixTotalNum,
       "hh3cDomainPDPrefixUsedNum": hh3cDomainPDPrefixUsedNum,
       "hh3cDomainPDPrefixFreeNum": hh3cDomainPDPrefixFreeNum,
       "hh3cDomainPDPrefixConflictNum": hh3cDomainPDPrefixConflictNum,
       "hh3cDomainPDPrefixExcludeNum": hh3cDomainPDPrefixExcludeNum,
       "hh3cDomainPDPrefixUsedPercent": hh3cDomainPDPrefixUsedPercent,
       "hh3cDomainNatBindingTable": hh3cDomainNatBindingTable,
       "hh3cDomainNatBindingEntry": hh3cDomainNatBindingEntry,
       "hh3cDomainNatBindingUserGroupName": hh3cDomainNatBindingUserGroupName,
       "hh3cDomainNatBindingNatInstance": hh3cDomainNatBindingNatInstance,
       "hh3cDomainNatBindingRowStatus": hh3cDomainNatBindingRowStatus,
       "hh3cDomainUpStatTable": hh3cDomainUpStatTable,
       "hh3cDomainUpStatEntry": hh3cDomainUpStatEntry,
       "hh3cDomainUpId": hh3cDomainUpId,
       "hh3cDomainUpAccessedNum": hh3cDomainUpAccessedNum,
       "hh3cDomainUpOnlineNum": hh3cDomainUpOnlineNum,
       "hh3cDomainUpOnlinePPPUser": hh3cDomainUpOnlinePPPUser,
       "hh3cDomainUpOnlineIPoEUser": hh3cDomainUpOnlineIPoEUser,
       "hh3cDomainUpOnlinePPPoEUser": hh3cDomainUpOnlinePPPoEUser,
       "hh3cDomainUpOnlinePPPoAUser": hh3cDomainUpOnlinePPPoAUser,
       "hh3cDomainUpOnlinePPPoFRUser": hh3cDomainUpOnlinePPPoFRUser,
       "hh3cDomainUpOnlineLacUser": hh3cDomainUpOnlineLacUser,
       "hh3cDomainUpOnlineLnsUser": hh3cDomainUpOnlineLnsUser,
       "hh3cDomainUpOnlineIPoEBindAuthUser": hh3cDomainUpOnlineIPoEBindAuthUser,
       "hh3cDomainUpOnlineIPoEWebAuthUser": hh3cDomainUpOnlineIPoEWebAuthUser,
       "hh3cDomainUpOnlineLeasedUser": hh3cDomainUpOnlineLeasedUser,
       "hh3cDomainUpOnlineIPv4User": hh3cDomainUpOnlineIPv4User,
       "hh3cDomainUpOnlineIPv6User": hh3cDomainUpOnlineIPv6User,
       "hh3cDomainUpOnlineDualStackUser": hh3cDomainUpOnlineDualStackUser,
       "hh3cDomainGlobalStat": hh3cDomainGlobalStat,
       "hh3cDomainGlobalAccessedNum": hh3cDomainGlobalAccessedNum,
       "hh3cDomainGlobalOnlineNum": hh3cDomainGlobalOnlineNum,
       "hh3cDomainGlobalOnlinePPPUser": hh3cDomainGlobalOnlinePPPUser,
       "hh3cDomainGlobalOnlineIPoEUser": hh3cDomainGlobalOnlineIPoEUser,
       "hh3cDomainGlobalOnlinePPPoEUser": hh3cDomainGlobalOnlinePPPoEUser,
       "hh3cDomainGlobalOnlinePPPoAUser": hh3cDomainGlobalOnlinePPPoAUser,
       "hh3cDomainGlobalOnlinePPPoFRUser": hh3cDomainGlobalOnlinePPPoFRUser,
       "hh3cDomainGlobalOnlineLacUser": hh3cDomainGlobalOnlineLacUser,
       "hh3cDomainGlobalOnlineLnsUser": hh3cDomainGlobalOnlineLnsUser,
       "hh3cDomainGlobalOnlineIPoEBindAuthUser": hh3cDomainGlobalOnlineIPoEBindAuthUser,
       "hh3cDomainGlobalOnlineIPoEWebAuthUser": hh3cDomainGlobalOnlineIPoEWebAuthUser,
       "hh3cDomainGlobalOnlineLeasedUser": hh3cDomainGlobalOnlineLeasedUser,
       "hh3cDomainGlobalTotalIPv4OnlineNum": hh3cDomainGlobalTotalIPv4OnlineNum,
       "hh3cDomainGlobalTotalIPv6OnlineNum": hh3cDomainGlobalTotalIPv6OnlineNum,
       "hh3cDomainGlobalTotalDualStackOnlineNum": hh3cDomainGlobalTotalDualStackOnlineNum,
       "hh3cDomainTraps": hh3cDomainTraps,
       "hh3cDomainTrapsDefine": hh3cDomainTrapsDefine,
       "hh3cUserIPAllocAlarm": hh3cUserIPAllocAlarm,
       "hh3cUserIPAllocAlarmResume": hh3cUserIPAllocAlarmResume,
       "hh3cUserIPLowerlimitWarningAlarm": hh3cUserIPLowerlimitWarningAlarm,
       "hh3cUserIPLowerlimitWarningResume": hh3cUserIPLowerlimitWarningResume,
       "hh3cUserIPv6AllocAlarm": hh3cUserIPv6AllocAlarm,
       "hh3cUserIPv6AllocAlarmResume": hh3cUserIPv6AllocAlarmResume,
       "hh3cUserIPv6LowlimitWarnAlarm": hh3cUserIPv6LowlimitWarnAlarm,
       "hh3cUserIPv6LowlimitWarnResume": hh3cUserIPv6LowlimitWarnResume,
       "hh3cUserNDRAPfAllocAlarm": hh3cUserNDRAPfAllocAlarm,
       "hh3cUserNDRAPfAllocAlarmResume": hh3cUserNDRAPfAllocAlarmResume,
       "hh3cUserNDRAPfLowlimitWarnAlarm": hh3cUserNDRAPfLowlimitWarnAlarm,
       "hh3cUserNDRAPfLowlimitWarnResume": hh3cUserNDRAPfLowlimitWarnResume,
       "hh3cUserPDPfAllocAlarm": hh3cUserPDPfAllocAlarm,
       "hh3cUserPDPfAllocAlarmResume": hh3cUserPDPfAllocAlarmResume,
       "hh3cUserPDPfLowlimitWarnAlarm": hh3cUserPDPfLowlimitWarnAlarm,
       "hh3cUserPDPfLowlimitWarnResume": hh3cUserPDPfLowlimitWarnResume,
       "hh3cUserWebServerDownAlarm": hh3cUserWebServerDownAlarm,
       "hh3cUserWebServerUpAlarm": hh3cUserWebServerUpAlarm,
       "hh3cUserWebServerChangeAlarm": hh3cUserWebServerChangeAlarm}
)
