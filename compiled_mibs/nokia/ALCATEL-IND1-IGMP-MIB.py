# SNMP MIB module (ALCATEL-IND1-IGMP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\nokia\aos6\ALCATEL-IND1-IGMP-MIB

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

(softentIND1Igmp,) = mibBuilder.importSymbols(
    "ALCATEL-IND1-BASE",
    "softentIND1Igmp")

(InterfaceIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex")

(InetAddress,
 InetAddressIPv4,
 InetAddressPrefixLength,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressIPv4",
    "InetAddressPrefixLength",
    "InetAddressType")

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
 PhysAddress,
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

alcatelIND1IgmpMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 34, 1)
)
if mibBuilder.loadTexts:
    alcatelIND1IgmpMIB.setRevisions(
        ("2009-03-31 00:00",
         "2008-09-10 00:00",
         "2008-08-08 00:00",
         "2007-04-03 00:00",
         "2019-10-07 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AlcatelIND1IgmpMIBObjects_ObjectIdentity = ObjectIdentity
alcatelIND1IgmpMIBObjects = _AlcatelIND1IgmpMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 34, 1, 1)
)
_AlaIgmp_ObjectIdentity = ObjectIdentity
alaIgmp = _AlaIgmp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 34, 1, 1, 1)
)


class _AlaIgmpStatus_Type(Integer32):
    """Custom type alaIgmpStatus based on Integer32"""
    defaultValue = 2

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


_AlaIgmpStatus_Type.__name__ = "Integer32"
_AlaIgmpStatus_Object = MibScalar
alaIgmpStatus = _AlaIgmpStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 34, 1, 1, 1, 1),
    _AlaIgmpStatus_Type()
)
alaIgmpStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaIgmpStatus.setStatus("current")


class _AlaIgmpQuerying_Type(Integer32):
    """Custom type alaIgmpQuerying based on Integer32"""
    defaultValue = 2

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


_AlaIgmpQuerying_Type.__name__ = "Integer32"
_AlaIgmpQuerying_Object = MibScalar
alaIgmpQuerying = _AlaIgmpQuerying_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 34, 1, 1, 1, 2),
    _AlaIgmpQuerying_Type()
)
alaIgmpQuerying.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaIgmpQuerying.setStatus("current")


class _AlaIgmpSpoofing_Type(Integer32):
    """Custom type alaIgmpSpoofing based on Integer32"""
    defaultValue = 2

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


_AlaIgmpSpoofing_Type.__name__ = "Integer32"
_AlaIgmpSpoofing_Object = MibScalar
alaIgmpSpoofing = _AlaIgmpSpoofing_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 34, 1, 1, 1, 3),
    _AlaIgmpSpoofing_Type()
)
alaIgmpSpoofing.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaIgmpSpoofing.setStatus("current")


class _AlaIgmpZapping_Type(Integer32):
    """Custom type alaIgmpZapping based on Integer32"""
    defaultValue = 2

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


_AlaIgmpZapping_Type.__name__ = "Integer32"
_AlaIgmpZapping_Object = MibScalar
alaIgmpZapping = _AlaIgmpZapping_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 34, 1, 1, 1, 4),
    _AlaIgmpZapping_Type()
)
alaIgmpZapping.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaIgmpZapping.setStatus("current")


class _AlaIgmpVersion_Type(Unsigned32):
    """Custom type alaIgmpVersion based on Unsigned32"""
    defaultValue = 2


_AlaIgmpVersion_Type.__name__ = "Unsigned32"
_AlaIgmpVersion_Object = MibScalar
alaIgmpVersion = _AlaIgmpVersion_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 34, 1, 1, 1, 5),
    _AlaIgmpVersion_Type()
)
alaIgmpVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaIgmpVersion.setStatus("current")


class _AlaIgmpRobustness_Type(Unsigned32):
    """Custom type alaIgmpRobustness based on Unsigned32"""
    defaultValue = 2


_AlaIgmpRobustness_Type.__name__ = "Unsigned32"
_AlaIgmpRobustness_Object = MibScalar
alaIgmpRobustness = _AlaIgmpRobustness_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 34, 1, 1, 1, 6),
    _AlaIgmpRobustness_Type()
)
alaIgmpRobustness.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaIgmpRobustness.setStatus("current")


class _AlaIgmpQueryInterval_Type(Unsigned32):
    """Custom type alaIgmpQueryInterval based on Unsigned32"""
    defaultValue = 125


_AlaIgmpQueryInterval_Type.__name__ = "Unsigned32"
_AlaIgmpQueryInterval_Object = MibScalar
alaIgmpQueryInterval = _AlaIgmpQueryInterval_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 34, 1, 1, 1, 7),
    _AlaIgmpQueryInterval_Type()
)
alaIgmpQueryInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaIgmpQueryInterval.setStatus("current")
if mibBuilder.loadTexts:
    alaIgmpQueryInterval.setUnits("seconds")


class _AlaIgmpQueryResponseInterval_Type(Unsigned32):
    """Custom type alaIgmpQueryResponseInterval based on Unsigned32"""
    defaultValue = 100


_AlaIgmpQueryResponseInterval_Type.__name__ = "Unsigned32"
_AlaIgmpQueryResponseInterval_Object = MibScalar
alaIgmpQueryResponseInterval = _AlaIgmpQueryResponseInterval_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 34, 1, 1, 1, 8),
    _AlaIgmpQueryResponseInterval_Type()
)
alaIgmpQueryResponseInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaIgmpQueryResponseInterval.setStatus("current")
if mibBuilder.loadTexts:
    alaIgmpQueryResponseInterval.setUnits("tenths of seconds")


class _AlaIgmpLastMemberQueryInterval_Type(Unsigned32):
    """Custom type alaIgmpLastMemberQueryInterval based on Unsigned32"""
    defaultValue = 10


_AlaIgmpLastMemberQueryInterval_Type.__name__ = "Unsigned32"
_AlaIgmpLastMemberQueryInterval_Object = MibScalar
alaIgmpLastMemberQueryInterval = _AlaIgmpLastMemberQueryInterval_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 34, 1, 1, 1, 9),
    _AlaIgmpLastMemberQueryInterval_Type()
)
alaIgmpLastMemberQueryInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaIgmpLastMemberQueryInterval.setStatus("current")
if mibBuilder.loadTexts:
    alaIgmpLastMemberQueryInterval.setUnits("tenths of seconds")


class _AlaIgmpRouterTimeout_Type(Unsigned32):
    """Custom type alaIgmpRouterTimeout based on Unsigned32"""
    defaultValue = 90


_AlaIgmpRouterTimeout_Type.__name__ = "Unsigned32"
_AlaIgmpRouterTimeout_Object = MibScalar
alaIgmpRouterTimeout = _AlaIgmpRouterTimeout_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 34, 1, 1, 1, 10),
    _AlaIgmpRouterTimeout_Type()
)
alaIgmpRouterTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaIgmpRouterTimeout.setStatus("current")
if mibBuilder.loadTexts:
    alaIgmpRouterTimeout.setUnits("seconds")


class _AlaIgmpSourceTimeout_Type(Unsigned32):
    """Custom type alaIgmpSourceTimeout based on Unsigned32"""
    defaultValue = 30


_AlaIgmpSourceTimeout_Type.__name__ = "Unsigned32"
_AlaIgmpSourceTimeout_Object = MibScalar
alaIgmpSourceTimeout = _AlaIgmpSourceTimeout_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 34, 1, 1, 1, 11),
    _AlaIgmpSourceTimeout_Type()
)
alaIgmpSourceTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaIgmpSourceTimeout.setStatus("current")
if mibBuilder.loadTexts:
    alaIgmpSourceTimeout.setUnits("seconds")


class _AlaIgmpProxying_Type(Integer32):
    """Custom type alaIgmpProxying based on Integer32"""
    defaultValue = 2

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


_AlaIgmpProxying_Type.__name__ = "Integer32"
_AlaIgmpProxying_Object = MibScalar
alaIgmpProxying = _AlaIgmpProxying_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 34, 1, 1, 1, 12),
    _AlaIgmpProxying_Type()
)
alaIgmpProxying.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaIgmpProxying.setStatus("current")


class _AlaIgmpUnsolicitedReportInterval_Type(Unsigned32):
    """Custom type alaIgmpUnsolicitedReportInterval based on Unsigned32"""
    defaultValue = 1


_AlaIgmpUnsolicitedReportInterval_Type.__name__ = "Unsigned32"
_AlaIgmpUnsolicitedReportInterval_Object = MibScalar
alaIgmpUnsolicitedReportInterval = _AlaIgmpUnsolicitedReportInterval_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 34, 1, 1, 1, 13),
    _AlaIgmpUnsolicitedReportInterval_Type()
)
alaIgmpUnsolicitedReportInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaIgmpUnsolicitedReportInterval.setStatus("current")
if mibBuilder.loadTexts:
    alaIgmpUnsolicitedReportInterval.setUnits("seconds")


class _AlaIgmpQuerierForwarding_Type(Integer32):
    """Custom type alaIgmpQuerierForwarding based on Integer32"""
    defaultValue = 2

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


_AlaIgmpQuerierForwarding_Type.__name__ = "Integer32"
_AlaIgmpQuerierForwarding_Object = MibScalar
alaIgmpQuerierForwarding = _AlaIgmpQuerierForwarding_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 34, 1, 1, 1, 14),
    _AlaIgmpQuerierForwarding_Type()
)
alaIgmpQuerierForwarding.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaIgmpQuerierForwarding.setStatus("current")


class _AlaIgmpMaxGroupLimit_Type(Unsigned32):
    """Custom type alaIgmpMaxGroupLimit based on Unsigned32"""
    defaultValue = 0


_AlaIgmpMaxGroupLimit_Type.__name__ = "Unsigned32"
_AlaIgmpMaxGroupLimit_Object = MibScalar
alaIgmpMaxGroupLimit = _AlaIgmpMaxGroupLimit_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 34, 1, 1, 1, 15),
    _AlaIgmpMaxGroupLimit_Type()
)
alaIgmpMaxGroupLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaIgmpMaxGroupLimit.setStatus("current")


class _AlaIgmpMaxGroupExceedAction_Type(Integer32):
    """Custom type alaIgmpMaxGroupExceedAction based on Integer32"""
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
          ("drop", 1),
          ("replace", 2))
    )


_AlaIgmpMaxGroupExceedAction_Type.__name__ = "Integer32"
_AlaIgmpMaxGroupExceedAction_Object = MibScalar
alaIgmpMaxGroupExceedAction = _AlaIgmpMaxGroupExceedAction_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 34, 1, 1, 1, 16),
    _AlaIgmpMaxGroupExceedAction_Type()
)
alaIgmpMaxGroupExceedAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaIgmpMaxGroupExceedAction.setStatus("current")


class _AlaIgmpFloodUnknown_Type(Integer32):
    """Custom type alaIgmpFloodUnknown based on Integer32"""
    defaultValue = 2

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


_AlaIgmpFloodUnknown_Type.__name__ = "Integer32"
_AlaIgmpFloodUnknown_Object = MibScalar
alaIgmpFloodUnknown = _AlaIgmpFloodUnknown_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 34, 1, 1, 1, 17),
    _AlaIgmpFloodUnknown_Type()
)
alaIgmpFloodUnknown.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaIgmpFloodUnknown.setStatus("current")


class _AlaIgmpHelperAddressType_Type(InetAddressType):
    """Custom type alaIgmpHelperAddressType based on InetAddressType"""
    subtypeSpec = InetAddressType.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
    )


_AlaIgmpHelperAddressType_Type.__name__ = "InetAddressType"
_AlaIgmpHelperAddressType_Object = MibScalar
alaIgmpHelperAddressType = _AlaIgmpHelperAddressType_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 34, 1, 1, 1, 18),
    _AlaIgmpHelperAddressType_Type()
)
alaIgmpHelperAddressType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaIgmpHelperAddressType.setStatus("current")


class _AlaIgmpHelperAddress_Type(InetAddress):
    """Custom type alaIgmpHelperAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )
    fixed_length = 4


_AlaIgmpHelperAddress_Type.__name__ = "InetAddress"
_AlaIgmpHelperAddress_Object = MibScalar
alaIgmpHelperAddress = _AlaIgmpHelperAddress_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 34, 1, 1, 1, 19),
    _AlaIgmpHelperAddress_Type()
)
alaIgmpHelperAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaIgmpHelperAddress.setStatus("current")


class _AlaIgmpBufferPacket_Type(Integer32):
    """Custom type alaIgmpBufferPacket based on Integer32"""
    defaultValue = 2

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


_AlaIgmpBufferPacket_Type.__name__ = "Integer32"
_AlaIgmpBufferPacket_Object = MibScalar
alaIgmpBufferPacket = _AlaIgmpBufferPacket_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 34, 1, 1, 1, 20),
    _AlaIgmpBufferPacket_Type()
)
alaIgmpBufferPacket.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaIgmpBufferPacket.setStatus("current")


class _AlaIgmpIndexSharing_Type(Integer32):
    """Custom type alaIgmpIndexSharing based on Integer32"""
    defaultValue = 2

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


_AlaIgmpIndexSharing_Type.__name__ = "Integer32"
_AlaIgmpIndexSharing_Object = MibScalar
alaIgmpIndexSharing = _AlaIgmpIndexSharing_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 34, 1, 1, 1, 21),
    _AlaIgmpIndexSharing_Type()
)
alaIgmpIndexSharing.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaIgmpIndexSharing.setStatus("current")


class _AlaDynamicControlStatus_Type(Integer32):
    """Custom type alaDynamicControlStatus based on Integer32"""
    defaultValue = 2

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


_AlaDynamicControlStatus_Type.__name__ = "Integer32"
_AlaDynamicControlStatus_Object = MibScalar
alaDynamicControlStatus = _AlaDynamicControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 34, 1, 1, 1, 22),
    _AlaDynamicControlStatus_Type()
)
alaDynamicControlStatus.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaDynamicControlStatus.setStatus("current")


class _AlaDynamicControlIpv4Status_Type(Integer32):
    """Custom type alaDynamicControlIpv4Status based on Integer32"""
    defaultValue = 2

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


_AlaDynamicControlIpv4Status_Type.__name__ = "Integer32"
_AlaDynamicControlIpv4Status_Object = MibScalar
alaDynamicControlIpv4Status = _AlaDynamicControlIpv4Status_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 34, 1, 1, 1, 23),
    _AlaDynamicControlIpv4Status_Type()
)
alaDynamicControlIpv4Status.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaDynamicControlIpv4Status.setStatus("current")


class _AlaIgmpStaticNeighborFastLearning_Type(Integer32):
    """Custom type alaIgmpStaticNeighborFastLearning based on Integer32"""
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


_AlaIgmpStaticNeighborFastLearning_Type.__name__ = "Integer32"
_AlaIgmpStaticNeighborFastLearning_Object = MibScalar
alaIgmpStaticNeighborFastLearning = _AlaIgmpStaticNeighborFastLearning_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 34, 1, 1, 1, 25),
    _AlaIgmpStaticNeighborFastLearning_Type()
)
alaIgmpStaticNeighborFastLearning.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaIgmpStaticNeighborFastLearning.setStatus("current")


class _AlaIgmpStarg_Type(Integer32):
    """Custom type alaIgmpStarg based on Integer32"""
    defaultValue = 2

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


_AlaIgmpStarg_Type.__name__ = "Integer32"
_AlaIgmpStarg_Object = MibScalar
alaIgmpStarg = _AlaIgmpStarg_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 34, 1, 1, 1, 26),
    _AlaIgmpStarg_Type()
)
alaIgmpStarg.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaIgmpStarg.setStatus("current")
_AlaIgmpVlan_ObjectIdentity = ObjectIdentity
alaIgmpVlan = _AlaIgmpVlan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 34, 1, 1, 2)
)
_AlaIgmpVlanTable_Object = MibTable
alaIgmpVlanTable = _AlaIgmpVlanTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 34, 1, 1, 2, 1)
)
if mibBuilder.loadTexts:
    alaIgmpVlanTable.setStatus("current")
_AlaIgmpVlanEntry_Object = MibTableRow
alaIgmpVlanEntry = _AlaIgmpVlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 34, 1, 1, 2, 1, 1)
)
alaIgmpVlanEntry.setIndexNames(
    (0, "ALCATEL-IND1-IGMP-MIB", "alaIgmpVlanIndex"),
)
if mibBuilder.loadTexts:
    alaIgmpVlanEntry.setStatus("current")
_AlaIgmpVlanIndex_Type = Unsigned32
_AlaIgmpVlanIndex_Object = MibTableColumn
alaIgmpVlanIndex = _AlaIgmpVlanIndex_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 34, 1, 1, 2, 1, 1, 1),
    _AlaIgmpVlanIndex_Type()
)
alaIgmpVlanIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaIgmpVlanIndex.setStatus("current")


class _AlaIgmpVlanStatus_Type(Integer32):
    """Custom type alaIgmpVlanStatus based on Integer32"""
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


_AlaIgmpVlanStatus_Type.__name__ = "Integer32"
_AlaIgmpVlanStatus_Object = MibTableColumn
alaIgmpVlanStatus = _AlaIgmpVlanStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 34, 1, 1, 2, 1, 1, 2),
    _AlaIgmpVlanStatus_Type()
)
alaIgmpVlanStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaIgmpVlanStatus.setStatus("current")


class _AlaIgmpVlanQuerying_Type(Integer32):
    """Custom type alaIgmpVlanQuerying based on Integer32"""
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


_AlaIgmpVlanQuerying_Type.__name__ = "Integer32"
_AlaIgmpVlanQuerying_Object = MibTableColumn
alaIgmpVlanQuerying = _AlaIgmpVlanQuerying_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 34, 1, 1, 2, 1, 1, 3),
    _AlaIgmpVlanQuerying_Type()
)
alaIgmpVlanQuerying.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaIgmpVlanQuerying.setStatus("current")


class _AlaIgmpVlanSpoofing_Type(Integer32):
    """Custom type alaIgmpVlanSpoofing based on Integer32"""
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


_AlaIgmpVlanSpoofing_Type.__name__ = "Integer32"
_AlaIgmpVlanSpoofing_Object = MibTableColumn
alaIgmpVlanSpoofing = _AlaIgmpVlanSpoofing_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 34, 1, 1, 2, 1, 1, 4),
    _AlaIgmpVlanSpoofing_Type()
)
alaIgmpVlanSpoofing.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaIgmpVlanSpoofing.setStatus("current")


class _AlaIgmpVlanZapping_Type(Integer32):
    """Custom type alaIgmpVlanZapping based on Integer32"""
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


_AlaIgmpVlanZapping_Type.__name__ = "Integer32"
_AlaIgmpVlanZapping_Object = MibTableColumn
alaIgmpVlanZapping = _AlaIgmpVlanZapping_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 34, 1, 1, 2, 1, 1, 5),
    _AlaIgmpVlanZapping_Type()
)
alaIgmpVlanZapping.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaIgmpVlanZapping.setStatus("current")
_AlaIgmpVlanVersion_Type = Unsigned32
_AlaIgmpVlanVersion_Object = MibTableColumn
alaIgmpVlanVersion = _AlaIgmpVlanVersion_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 34, 1, 1, 2, 1, 1, 6),
    _AlaIgmpVlanVersion_Type()
)
alaIgmpVlanVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaIgmpVlanVersion.setStatus("current")
_AlaIgmpVlanRobustness_Type = Unsigned32
_AlaIgmpVlanRobustness_Object = MibTableColumn
alaIgmpVlanRobustness = _AlaIgmpVlanRobustness_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 34, 1, 1, 2, 1, 1, 7),
    _AlaIgmpVlanRobustness_Type()
)
alaIgmpVlanRobustness.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaIgmpVlanRobustness.setStatus("current")
_AlaIgmpVlanQueryInterval_Type = Unsigned32
_AlaIgmpVlanQueryInterval_Object = MibTableColumn
alaIgmpVlanQueryInterval = _AlaIgmpVlanQueryInterval_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 34, 1, 1, 2, 1, 1, 8),
    _AlaIgmpVlanQueryInterval_Type()
)
alaIgmpVlanQueryInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaIgmpVlanQueryInterval.setStatus("current")
if mibBuilder.loadTexts:
    alaIgmpVlanQueryInterval.setUnits("seconds")
_AlaIgmpVlanQueryResponseInterval_Type = Unsigned32
_AlaIgmpVlanQueryResponseInterval_Object = MibTableColumn
alaIgmpVlanQueryResponseInterval = _AlaIgmpVlanQueryResponseInterval_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 34, 1, 1, 2, 1, 1, 9),
    _AlaIgmpVlanQueryResponseInterval_Type()
)
alaIgmpVlanQueryResponseInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaIgmpVlanQueryResponseInterval.setStatus("current")
if mibBuilder.loadTexts:
    alaIgmpVlanQueryResponseInterval.setUnits("tenths of seconds")
_AlaIgmpVlanLastMemberQueryInterval_Type = Unsigned32
_AlaIgmpVlanLastMemberQueryInterval_Object = MibTableColumn
alaIgmpVlanLastMemberQueryInterval = _AlaIgmpVlanLastMemberQueryInterval_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 34, 1, 1, 2, 1, 1, 10),
    _AlaIgmpVlanLastMemberQueryInterval_Type()
)
alaIgmpVlanLastMemberQueryInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaIgmpVlanLastMemberQueryInterval.setStatus("current")
if mibBuilder.loadTexts:
    alaIgmpVlanLastMemberQueryInterval.setUnits("tenths of seconds")
_AlaIgmpVlanRouterTimeout_Type = Unsigned32
_AlaIgmpVlanRouterTimeout_Object = MibTableColumn
alaIgmpVlanRouterTimeout = _AlaIgmpVlanRouterTimeout_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 34, 1, 1, 2, 1, 1, 11),
    _AlaIgmpVlanRouterTimeout_Type()
)
alaIgmpVlanRouterTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaIgmpVlanRouterTimeout.setStatus("current")
if mibBuilder.loadTexts:
    alaIgmpVlanRouterTimeout.setUnits("seconds")
_AlaIgmpVlanSourceTimeout_Type = Unsigned32
_AlaIgmpVlanSourceTimeout_Object = MibTableColumn
alaIgmpVlanSourceTimeout = _AlaIgmpVlanSourceTimeout_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 34, 1, 1, 2, 1, 1, 12),
    _AlaIgmpVlanSourceTimeout_Type()
)
alaIgmpVlanSourceTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaIgmpVlanSourceTimeout.setStatus("current")
if mibBuilder.loadTexts:
    alaIgmpVlanSourceTimeout.setUnits("seconds")


class _AlaIgmpVlanProxying_Type(Integer32):
    """Custom type alaIgmpVlanProxying based on Integer32"""
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


_AlaIgmpVlanProxying_Type.__name__ = "Integer32"
_AlaIgmpVlanProxying_Object = MibTableColumn
alaIgmpVlanProxying = _AlaIgmpVlanProxying_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 34, 1, 1, 2, 1, 1, 13),
    _AlaIgmpVlanProxying_Type()
)
alaIgmpVlanProxying.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaIgmpVlanProxying.setStatus("current")
_AlaIgmpVlanUnsolicitedReportInterval_Type = Unsigned32
_AlaIgmpVlanUnsolicitedReportInterval_Object = MibTableColumn
alaIgmpVlanUnsolicitedReportInterval = _AlaIgmpVlanUnsolicitedReportInterval_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 34, 1, 1, 2, 1, 1, 14),
    _AlaIgmpVlanUnsolicitedReportInterval_Type()
)
alaIgmpVlanUnsolicitedReportInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaIgmpVlanUnsolicitedReportInterval.setStatus("current")
if mibBuilder.loadTexts:
    alaIgmpVlanUnsolicitedReportInterval.setUnits("seconds")


class _AlaIgmpVlanQuerierForwarding_Type(Integer32):
    """Custom type alaIgmpVlanQuerierForwarding based on Integer32"""
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


_AlaIgmpVlanQuerierForwarding_Type.__name__ = "Integer32"
_AlaIgmpVlanQuerierForwarding_Object = MibTableColumn
alaIgmpVlanQuerierForwarding = _AlaIgmpVlanQuerierForwarding_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 34, 1, 1, 2, 1, 1, 15),
    _AlaIgmpVlanQuerierForwarding_Type()
)
alaIgmpVlanQuerierForwarding.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaIgmpVlanQuerierForwarding.setStatus("current")


class _AlaIgmpVlanMaxGroupLimit_Type(Unsigned32):
    """Custom type alaIgmpVlanMaxGroupLimit based on Unsigned32"""
    defaultValue = 0


_AlaIgmpVlanMaxGroupLimit_Type.__name__ = "Unsigned32"
_AlaIgmpVlanMaxGroupLimit_Object = MibTableColumn
alaIgmpVlanMaxGroupLimit = _AlaIgmpVlanMaxGroupLimit_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 34, 1, 1, 2, 1, 1, 16),
    _AlaIgmpVlanMaxGroupLimit_Type()
)
alaIgmpVlanMaxGroupLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaIgmpVlanMaxGroupLimit.setStatus("current")


class _AlaIgmpVlanMaxGroupExceedAction_Type(Integer32):
    """Custom type alaIgmpVlanMaxGroupExceedAction based on Integer32"""
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
          ("drop", 1),
          ("replace", 2))
    )


_AlaIgmpVlanMaxGroupExceedAction_Type.__name__ = "Integer32"
_AlaIgmpVlanMaxGroupExceedAction_Object = MibTableColumn
alaIgmpVlanMaxGroupExceedAction = _AlaIgmpVlanMaxGroupExceedAction_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 34, 1, 1, 2, 1, 1, 17),
    _AlaIgmpVlanMaxGroupExceedAction_Type()
)
alaIgmpVlanMaxGroupExceedAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaIgmpVlanMaxGroupExceedAction.setStatus("current")


class _AlaIgmpVlanSpoofAddressType_Type(InetAddressType):
    """Custom type alaIgmpVlanSpoofAddressType based on InetAddressType"""
    subtypeSpec = InetAddressType.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_AlaIgmpVlanSpoofAddressType_Type.__name__ = "InetAddressType"
_AlaIgmpVlanSpoofAddressType_Object = MibTableColumn
alaIgmpVlanSpoofAddressType = _AlaIgmpVlanSpoofAddressType_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 34, 1, 1, 2, 1, 1, 18),
    _AlaIgmpVlanSpoofAddressType_Type()
)
alaIgmpVlanSpoofAddressType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaIgmpVlanSpoofAddressType.setStatus("obsolete")
_AlaIgmpVlanSpoofAddress_Type = InetAddress
_AlaIgmpVlanSpoofAddress_Object = MibTableColumn
alaIgmpVlanSpoofAddress = _AlaIgmpVlanSpoofAddress_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 34, 1, 1, 2, 1, 1, 19),
    _AlaIgmpVlanSpoofAddress_Type()
)
alaIgmpVlanSpoofAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaIgmpVlanSpoofAddress.setStatus("obsolete")


class _AlaIgmpVlanIndexSharing_Type(Integer32):
    """Custom type alaIgmpVlanIndexSharing based on Integer32"""
    defaultValue = 2

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


_AlaIgmpVlanIndexSharing_Type.__name__ = "Integer32"
_AlaIgmpVlanIndexSharing_Object = MibTableColumn
alaIgmpVlanIndexSharing = _AlaIgmpVlanIndexSharing_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 34, 1, 1, 2, 1, 1, 20),
    _AlaIgmpVlanIndexSharing_Type()
)
alaIgmpVlanIndexSharing.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaIgmpVlanIndexSharing.setStatus("current")


class _AlaIgmpVlanStarg_Type(Integer32):
    """Custom type alaIgmpVlanStarg based on Integer32"""
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


_AlaIgmpVlanStarg_Type.__name__ = "Integer32"
_AlaIgmpVlanStarg_Object = MibTableColumn
alaIgmpVlanStarg = _AlaIgmpVlanStarg_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 34, 1, 1, 2, 1, 1, 21),
    _AlaIgmpVlanStarg_Type()
)
alaIgmpVlanStarg.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaIgmpVlanStarg.setStatus("current")
_AlaIgmpMember_ObjectIdentity = ObjectIdentity
alaIgmpMember = _AlaIgmpMember_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 34, 1, 1, 3)
)
_AlaIgmpMemberTable_Object = MibTable
alaIgmpMemberTable = _AlaIgmpMemberTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 34, 1, 1, 3, 1)
)
if mibBuilder.loadTexts:
    alaIgmpMemberTable.setStatus("current")
_AlaIgmpMemberEntry_Object = MibTableRow
alaIgmpMemberEntry = _AlaIgmpMemberEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 34, 1, 1, 3, 1, 1)
)
alaIgmpMemberEntry.setIndexNames(
    (0, "ALCATEL-IND1-IGMP-MIB", "alaIgmpMemberVlan"),
    (0, "ALCATEL-IND1-IGMP-MIB", "alaIgmpMemberIfIndex"),
    (0, "ALCATEL-IND1-IGMP-MIB", "alaIgmpMemberGroupAddress"),
    (0, "ALCATEL-IND1-IGMP-MIB", "alaIgmpMemberSourceAddress"),
)
if mibBuilder.loadTexts:
    alaIgmpMemberEntry.setStatus("current")
_AlaIgmpMemberVlan_Type = Unsigned32
_AlaIgmpMemberVlan_Object = MibTableColumn
alaIgmpMemberVlan = _AlaIgmpMemberVlan_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 34, 1, 1, 3, 1, 1, 1),
    _AlaIgmpMemberVlan_Type()
)
alaIgmpMemberVlan.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaIgmpMemberVlan.setStatus("current")
_AlaIgmpMemberIfIndex_Type = InterfaceIndex
_AlaIgmpMemberIfIndex_Object = MibTableColumn
alaIgmpMemberIfIndex = _AlaIgmpMemberIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 34, 1, 1, 3, 1, 1, 2),
    _AlaIgmpMemberIfIndex_Type()
)
alaIgmpMemberIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaIgmpMemberIfIndex.setStatus("current")
_AlaIgmpMemberGroupAddress_Type = InetAddressIPv4
_AlaIgmpMemberGroupAddress_Object = MibTableColumn
alaIgmpMemberGroupAddress = _AlaIgmpMemberGroupAddress_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 34, 1, 1, 3, 1, 1, 3),
    _AlaIgmpMemberGroupAddress_Type()
)
alaIgmpMemberGroupAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaIgmpMemberGroupAddress.setStatus("current")
_AlaIgmpMemberSourceAddress_Type = InetAddressIPv4
_AlaIgmpMemberSourceAddress_Object = MibTableColumn
alaIgmpMemberSourceAddress = _AlaIgmpMemberSourceAddress_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 34, 1, 1, 3, 1, 1, 4),
    _AlaIgmpMemberSourceAddress_Type()
)
alaIgmpMemberSourceAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaIgmpMemberSourceAddress.setStatus("current")


class _AlaIgmpMemberMode_Type(Integer32):
    """Custom type alaIgmpMemberMode based on Integer32"""
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


_AlaIgmpMemberMode_Type.__name__ = "Integer32"
_AlaIgmpMemberMode_Object = MibTableColumn
alaIgmpMemberMode = _AlaIgmpMemberMode_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 34, 1, 1, 3, 1, 1, 5),
    _AlaIgmpMemberMode_Type()
)
alaIgmpMemberMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaIgmpMemberMode.setStatus("current")
_AlaIgmpMemberCount_Type = Counter32
_AlaIgmpMemberCount_Object = MibTableColumn
alaIgmpMemberCount = _AlaIgmpMemberCount_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 34, 1, 1, 3, 1, 1, 6),
    _AlaIgmpMemberCount_Type()
)
alaIgmpMemberCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaIgmpMemberCount.setStatus("current")
_AlaIgmpMemberTimeout_Type = TimeTicks
_AlaIgmpMemberTimeout_Object = MibTableColumn
alaIgmpMemberTimeout = _AlaIgmpMemberTimeout_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 34, 1, 1, 3, 1, 1, 7),
    _AlaIgmpMemberTimeout_Type()
)
alaIgmpMemberTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaIgmpMemberTimeout.setStatus("current")
_AlaIgmpStaticMember_ObjectIdentity = ObjectIdentity
alaIgmpStaticMember = _AlaIgmpStaticMember_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 34, 1, 1, 4)
)
_AlaIgmpStaticMemberTable_Object = MibTable
alaIgmpStaticMemberTable = _AlaIgmpStaticMemberTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 34, 1, 1, 4, 1)
)
if mibBuilder.loadTexts:
    alaIgmpStaticMemberTable.setStatus("current")
_AlaIgmpStaticMemberEntry_Object = MibTableRow
alaIgmpStaticMemberEntry = _AlaIgmpStaticMemberEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 34, 1, 1, 4, 1, 1)
)
alaIgmpStaticMemberEntry.setIndexNames(
    (0, "ALCATEL-IND1-IGMP-MIB", "alaIgmpStaticMemberVlan"),
    (0, "ALCATEL-IND1-IGMP-MIB", "alaIgmpStaticMemberIfIndex"),
    (0, "ALCATEL-IND1-IGMP-MIB", "alaIgmpStaticMemberGroupAddress"),
)
if mibBuilder.loadTexts:
    alaIgmpStaticMemberEntry.setStatus("current")
_AlaIgmpStaticMemberVlan_Type = Unsigned32
_AlaIgmpStaticMemberVlan_Object = MibTableColumn
alaIgmpStaticMemberVlan = _AlaIgmpStaticMemberVlan_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 34, 1, 1, 4, 1, 1, 1),
    _AlaIgmpStaticMemberVlan_Type()
)
alaIgmpStaticMemberVlan.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaIgmpStaticMemberVlan.setStatus("current")
_AlaIgmpStaticMemberIfIndex_Type = InterfaceIndex
_AlaIgmpStaticMemberIfIndex_Object = MibTableColumn
alaIgmpStaticMemberIfIndex = _AlaIgmpStaticMemberIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 34, 1, 1, 4, 1, 1, 2),
    _AlaIgmpStaticMemberIfIndex_Type()
)
alaIgmpStaticMemberIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaIgmpStaticMemberIfIndex.setStatus("current")
_AlaIgmpStaticMemberGroupAddress_Type = InetAddressIPv4
_AlaIgmpStaticMemberGroupAddress_Object = MibTableColumn
alaIgmpStaticMemberGroupAddress = _AlaIgmpStaticMemberGroupAddress_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 34, 1, 1, 4, 1, 1, 3),
    _AlaIgmpStaticMemberGroupAddress_Type()
)
alaIgmpStaticMemberGroupAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaIgmpStaticMemberGroupAddress.setStatus("current")
_AlaIgmpStaticMemberRowStatus_Type = RowStatus
_AlaIgmpStaticMemberRowStatus_Object = MibTableColumn
alaIgmpStaticMemberRowStatus = _AlaIgmpStaticMemberRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 34, 1, 1, 4, 1, 1, 4),
    _AlaIgmpStaticMemberRowStatus_Type()
)
alaIgmpStaticMemberRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaIgmpStaticMemberRowStatus.setStatus("current")
_AlaIgmpNeighbor_ObjectIdentity = ObjectIdentity
alaIgmpNeighbor = _AlaIgmpNeighbor_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 34, 1, 1, 5)
)
_AlaIgmpNeighborTable_Object = MibTable
alaIgmpNeighborTable = _AlaIgmpNeighborTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 34, 1, 1, 5, 1)
)
if mibBuilder.loadTexts:
    alaIgmpNeighborTable.setStatus("current")
_AlaIgmpNeighborEntry_Object = MibTableRow
alaIgmpNeighborEntry = _AlaIgmpNeighborEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 34, 1, 1, 5, 1, 1)
)
alaIgmpNeighborEntry.setIndexNames(
    (0, "ALCATEL-IND1-IGMP-MIB", "alaIgmpNeighborVlan"),
    (0, "ALCATEL-IND1-IGMP-MIB", "alaIgmpNeighborIfIndex"),
    (0, "ALCATEL-IND1-IGMP-MIB", "alaIgmpNeighborHostAddress"),
)
if mibBuilder.loadTexts:
    alaIgmpNeighborEntry.setStatus("current")
_AlaIgmpNeighborVlan_Type = Unsigned32
_AlaIgmpNeighborVlan_Object = MibTableColumn
alaIgmpNeighborVlan = _AlaIgmpNeighborVlan_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 34, 1, 1, 5, 1, 1, 1),
    _AlaIgmpNeighborVlan_Type()
)
alaIgmpNeighborVlan.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaIgmpNeighborVlan.setStatus("current")
_AlaIgmpNeighborIfIndex_Type = InterfaceIndex
_AlaIgmpNeighborIfIndex_Object = MibTableColumn
alaIgmpNeighborIfIndex = _AlaIgmpNeighborIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 34, 1, 1, 5, 1, 1, 2),
    _AlaIgmpNeighborIfIndex_Type()
)
alaIgmpNeighborIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaIgmpNeighborIfIndex.setStatus("current")
_AlaIgmpNeighborHostAddress_Type = InetAddressIPv4
_AlaIgmpNeighborHostAddress_Object = MibTableColumn
alaIgmpNeighborHostAddress = _AlaIgmpNeighborHostAddress_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 34, 1, 1, 5, 1, 1, 3),
    _AlaIgmpNeighborHostAddress_Type()
)
alaIgmpNeighborHostAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaIgmpNeighborHostAddress.setStatus("current")
_AlaIgmpNeighborCount_Type = Counter32
_AlaIgmpNeighborCount_Object = MibTableColumn
alaIgmpNeighborCount = _AlaIgmpNeighborCount_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 34, 1, 1, 5, 1, 1, 4),
    _AlaIgmpNeighborCount_Type()
)
alaIgmpNeighborCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaIgmpNeighborCount.setStatus("current")
_AlaIgmpNeighborTimeout_Type = TimeTicks
_AlaIgmpNeighborTimeout_Object = MibTableColumn
alaIgmpNeighborTimeout = _AlaIgmpNeighborTimeout_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 34, 1, 1, 5, 1, 1, 5),
    _AlaIgmpNeighborTimeout_Type()
)
alaIgmpNeighborTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaIgmpNeighborTimeout.setStatus("current")
_AlaIgmpStaticNeighbor_ObjectIdentity = ObjectIdentity
alaIgmpStaticNeighbor = _AlaIgmpStaticNeighbor_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 34, 1, 1, 6)
)
_AlaIgmpStaticNeighborTable_Object = MibTable
alaIgmpStaticNeighborTable = _AlaIgmpStaticNeighborTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 34, 1, 1, 6, 1)
)
if mibBuilder.loadTexts:
    alaIgmpStaticNeighborTable.setStatus("current")
_AlaIgmpStaticNeighborEntry_Object = MibTableRow
alaIgmpStaticNeighborEntry = _AlaIgmpStaticNeighborEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 34, 1, 1, 6, 1, 1)
)
alaIgmpStaticNeighborEntry.setIndexNames(
    (0, "ALCATEL-IND1-IGMP-MIB", "alaIgmpStaticNeighborVlan"),
    (0, "ALCATEL-IND1-IGMP-MIB", "alaIgmpStaticNeighborIfIndex"),
)
if mibBuilder.loadTexts:
    alaIgmpStaticNeighborEntry.setStatus("current")
_AlaIgmpStaticNeighborVlan_Type = Unsigned32
_AlaIgmpStaticNeighborVlan_Object = MibTableColumn
alaIgmpStaticNeighborVlan = _AlaIgmpStaticNeighborVlan_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 34, 1, 1, 6, 1, 1, 1),
    _AlaIgmpStaticNeighborVlan_Type()
)
alaIgmpStaticNeighborVlan.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaIgmpStaticNeighborVlan.setStatus("current")
_AlaIgmpStaticNeighborIfIndex_Type = InterfaceIndex
_AlaIgmpStaticNeighborIfIndex_Object = MibTableColumn
alaIgmpStaticNeighborIfIndex = _AlaIgmpStaticNeighborIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 34, 1, 1, 6, 1, 1, 2),
    _AlaIgmpStaticNeighborIfIndex_Type()
)
alaIgmpStaticNeighborIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaIgmpStaticNeighborIfIndex.setStatus("current")
_AlaIgmpStaticNeighborRowStatus_Type = RowStatus
_AlaIgmpStaticNeighborRowStatus_Object = MibTableColumn
alaIgmpStaticNeighborRowStatus = _AlaIgmpStaticNeighborRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 34, 1, 1, 6, 1, 1, 3),
    _AlaIgmpStaticNeighborRowStatus_Type()
)
alaIgmpStaticNeighborRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaIgmpStaticNeighborRowStatus.setStatus("current")
_AlaIgmpQuerier_ObjectIdentity = ObjectIdentity
alaIgmpQuerier = _AlaIgmpQuerier_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 34, 1, 1, 7)
)
_AlaIgmpQuerierTable_Object = MibTable
alaIgmpQuerierTable = _AlaIgmpQuerierTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 34, 1, 1, 7, 1)
)
if mibBuilder.loadTexts:
    alaIgmpQuerierTable.setStatus("current")
_AlaIgmpQuerierEntry_Object = MibTableRow
alaIgmpQuerierEntry = _AlaIgmpQuerierEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 34, 1, 1, 7, 1, 1)
)
alaIgmpQuerierEntry.setIndexNames(
    (0, "ALCATEL-IND1-IGMP-MIB", "alaIgmpQuerierVlan"),
    (0, "ALCATEL-IND1-IGMP-MIB", "alaIgmpQuerierIfIndex"),
    (0, "ALCATEL-IND1-IGMP-MIB", "alaIgmpQuerierHostAddress"),
)
if mibBuilder.loadTexts:
    alaIgmpQuerierEntry.setStatus("current")
_AlaIgmpQuerierVlan_Type = Unsigned32
_AlaIgmpQuerierVlan_Object = MibTableColumn
alaIgmpQuerierVlan = _AlaIgmpQuerierVlan_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 34, 1, 1, 7, 1, 1, 1),
    _AlaIgmpQuerierVlan_Type()
)
alaIgmpQuerierVlan.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaIgmpQuerierVlan.setStatus("current")
_AlaIgmpQuerierIfIndex_Type = InterfaceIndex
_AlaIgmpQuerierIfIndex_Object = MibTableColumn
alaIgmpQuerierIfIndex = _AlaIgmpQuerierIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 34, 1, 1, 7, 1, 1, 2),
    _AlaIgmpQuerierIfIndex_Type()
)
alaIgmpQuerierIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaIgmpQuerierIfIndex.setStatus("current")
_AlaIgmpQuerierHostAddress_Type = InetAddressIPv4
_AlaIgmpQuerierHostAddress_Object = MibTableColumn
alaIgmpQuerierHostAddress = _AlaIgmpQuerierHostAddress_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 34, 1, 1, 7, 1, 1, 3),
    _AlaIgmpQuerierHostAddress_Type()
)
alaIgmpQuerierHostAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaIgmpQuerierHostAddress.setStatus("current")
_AlaIgmpQuerierCount_Type = Counter32
_AlaIgmpQuerierCount_Object = MibTableColumn
alaIgmpQuerierCount = _AlaIgmpQuerierCount_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 34, 1, 1, 7, 1, 1, 4),
    _AlaIgmpQuerierCount_Type()
)
alaIgmpQuerierCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaIgmpQuerierCount.setStatus("current")
_AlaIgmpQuerierTimeout_Type = TimeTicks
_AlaIgmpQuerierTimeout_Object = MibTableColumn
alaIgmpQuerierTimeout = _AlaIgmpQuerierTimeout_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 34, 1, 1, 7, 1, 1, 5),
    _AlaIgmpQuerierTimeout_Type()
)
alaIgmpQuerierTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaIgmpQuerierTimeout.setStatus("current")
_AlaIgmpStaticQuerier_ObjectIdentity = ObjectIdentity
alaIgmpStaticQuerier = _AlaIgmpStaticQuerier_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 34, 1, 1, 8)
)
_AlaIgmpStaticQuerierTable_Object = MibTable
alaIgmpStaticQuerierTable = _AlaIgmpStaticQuerierTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 34, 1, 1, 8, 1)
)
if mibBuilder.loadTexts:
    alaIgmpStaticQuerierTable.setStatus("current")
_AlaIgmpStaticQuerierEntry_Object = MibTableRow
alaIgmpStaticQuerierEntry = _AlaIgmpStaticQuerierEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 34, 1, 1, 8, 1, 1)
)
alaIgmpStaticQuerierEntry.setIndexNames(
    (0, "ALCATEL-IND1-IGMP-MIB", "alaIgmpStaticQuerierVlan"),
    (0, "ALCATEL-IND1-IGMP-MIB", "alaIgmpStaticQuerierIfIndex"),
)
if mibBuilder.loadTexts:
    alaIgmpStaticQuerierEntry.setStatus("current")
_AlaIgmpStaticQuerierVlan_Type = Unsigned32
_AlaIgmpStaticQuerierVlan_Object = MibTableColumn
alaIgmpStaticQuerierVlan = _AlaIgmpStaticQuerierVlan_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 34, 1, 1, 8, 1, 1, 1),
    _AlaIgmpStaticQuerierVlan_Type()
)
alaIgmpStaticQuerierVlan.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaIgmpStaticQuerierVlan.setStatus("current")
_AlaIgmpStaticQuerierIfIndex_Type = InterfaceIndex
_AlaIgmpStaticQuerierIfIndex_Object = MibTableColumn
alaIgmpStaticQuerierIfIndex = _AlaIgmpStaticQuerierIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 34, 1, 1, 8, 1, 1, 2),
    _AlaIgmpStaticQuerierIfIndex_Type()
)
alaIgmpStaticQuerierIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaIgmpStaticQuerierIfIndex.setStatus("current")
_AlaIgmpStaticQuerierRowStatus_Type = RowStatus
_AlaIgmpStaticQuerierRowStatus_Object = MibTableColumn
alaIgmpStaticQuerierRowStatus = _AlaIgmpStaticQuerierRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 34, 1, 1, 8, 1, 1, 3),
    _AlaIgmpStaticQuerierRowStatus_Type()
)
alaIgmpStaticQuerierRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaIgmpStaticQuerierRowStatus.setStatus("current")
_AlaIgmpSource_ObjectIdentity = ObjectIdentity
alaIgmpSource = _AlaIgmpSource_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 34, 1, 1, 9)
)
_AlaIgmpSourceTable_Object = MibTable
alaIgmpSourceTable = _AlaIgmpSourceTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 34, 1, 1, 9, 1)
)
if mibBuilder.loadTexts:
    alaIgmpSourceTable.setStatus("current")
_AlaIgmpSourceEntry_Object = MibTableRow
alaIgmpSourceEntry = _AlaIgmpSourceEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 34, 1, 1, 9, 1, 1)
)
alaIgmpSourceEntry.setIndexNames(
    (0, "ALCATEL-IND1-IGMP-MIB", "alaIgmpSourceVlan"),
    (0, "ALCATEL-IND1-IGMP-MIB", "alaIgmpSourceGroupAddress"),
    (0, "ALCATEL-IND1-IGMP-MIB", "alaIgmpSourceHostAddress"),
    (0, "ALCATEL-IND1-IGMP-MIB", "alaIgmpSourceDestAddress"),
    (0, "ALCATEL-IND1-IGMP-MIB", "alaIgmpSourceOrigAddress"),
)
if mibBuilder.loadTexts:
    alaIgmpSourceEntry.setStatus("current")
_AlaIgmpSourceVlan_Type = Unsigned32
_AlaIgmpSourceVlan_Object = MibTableColumn
alaIgmpSourceVlan = _AlaIgmpSourceVlan_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 34, 1, 1, 9, 1, 1, 1),
    _AlaIgmpSourceVlan_Type()
)
alaIgmpSourceVlan.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaIgmpSourceVlan.setStatus("current")
_AlaIgmpSourceIfIndex_Type = InterfaceIndex
_AlaIgmpSourceIfIndex_Object = MibTableColumn
alaIgmpSourceIfIndex = _AlaIgmpSourceIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 34, 1, 1, 9, 1, 1, 2),
    _AlaIgmpSourceIfIndex_Type()
)
alaIgmpSourceIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaIgmpSourceIfIndex.setStatus("current")
_AlaIgmpSourceGroupAddress_Type = InetAddressIPv4
_AlaIgmpSourceGroupAddress_Object = MibTableColumn
alaIgmpSourceGroupAddress = _AlaIgmpSourceGroupAddress_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 34, 1, 1, 9, 1, 1, 3),
    _AlaIgmpSourceGroupAddress_Type()
)
alaIgmpSourceGroupAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaIgmpSourceGroupAddress.setStatus("current")
_AlaIgmpSourceHostAddress_Type = InetAddressIPv4
_AlaIgmpSourceHostAddress_Object = MibTableColumn
alaIgmpSourceHostAddress = _AlaIgmpSourceHostAddress_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 34, 1, 1, 9, 1, 1, 4),
    _AlaIgmpSourceHostAddress_Type()
)
alaIgmpSourceHostAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaIgmpSourceHostAddress.setStatus("current")
_AlaIgmpSourceDestAddress_Type = InetAddressIPv4
_AlaIgmpSourceDestAddress_Object = MibTableColumn
alaIgmpSourceDestAddress = _AlaIgmpSourceDestAddress_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 34, 1, 1, 9, 1, 1, 5),
    _AlaIgmpSourceDestAddress_Type()
)
alaIgmpSourceDestAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaIgmpSourceDestAddress.setStatus("current")
_AlaIgmpSourceOrigAddress_Type = InetAddressIPv4
_AlaIgmpSourceOrigAddress_Object = MibTableColumn
alaIgmpSourceOrigAddress = _AlaIgmpSourceOrigAddress_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 34, 1, 1, 9, 1, 1, 6),
    _AlaIgmpSourceOrigAddress_Type()
)
alaIgmpSourceOrigAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaIgmpSourceOrigAddress.setStatus("current")


class _AlaIgmpSourceType_Type(Integer32):
    """Custom type alaIgmpSourceType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("mcast", 1),
          ("pim", 2),
          ("ipip", 3))
    )


_AlaIgmpSourceType_Type.__name__ = "Integer32"
_AlaIgmpSourceType_Object = MibTableColumn
alaIgmpSourceType = _AlaIgmpSourceType_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 34, 1, 1, 9, 1, 1, 7),
    _AlaIgmpSourceType_Type()
)
alaIgmpSourceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaIgmpSourceType.setStatus("current")
_AlaIgmpForward_ObjectIdentity = ObjectIdentity
alaIgmpForward = _AlaIgmpForward_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 34, 1, 1, 10)
)
_AlaIgmpForwardTable_Object = MibTable
alaIgmpForwardTable = _AlaIgmpForwardTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 34, 1, 1, 10, 1)
)
if mibBuilder.loadTexts:
    alaIgmpForwardTable.setStatus("current")
_AlaIgmpForwardEntry_Object = MibTableRow
alaIgmpForwardEntry = _AlaIgmpForwardEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 34, 1, 1, 10, 1, 1)
)
alaIgmpForwardEntry.setIndexNames(
    (0, "ALCATEL-IND1-IGMP-MIB", "alaIgmpForwardVlan"),
    (0, "ALCATEL-IND1-IGMP-MIB", "alaIgmpForwardGroupAddress"),
    (0, "ALCATEL-IND1-IGMP-MIB", "alaIgmpForwardHostAddress"),
    (0, "ALCATEL-IND1-IGMP-MIB", "alaIgmpForwardDestAddress"),
    (0, "ALCATEL-IND1-IGMP-MIB", "alaIgmpForwardOrigAddress"),
    (0, "ALCATEL-IND1-IGMP-MIB", "alaIgmpForwardNextVlan"),
    (0, "ALCATEL-IND1-IGMP-MIB", "alaIgmpForwardNextIfIndex"),
)
if mibBuilder.loadTexts:
    alaIgmpForwardEntry.setStatus("current")
_AlaIgmpForwardVlan_Type = Unsigned32
_AlaIgmpForwardVlan_Object = MibTableColumn
alaIgmpForwardVlan = _AlaIgmpForwardVlan_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 34, 1, 1, 10, 1, 1, 1),
    _AlaIgmpForwardVlan_Type()
)
alaIgmpForwardVlan.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaIgmpForwardVlan.setStatus("current")
_AlaIgmpForwardIfIndex_Type = InterfaceIndex
_AlaIgmpForwardIfIndex_Object = MibTableColumn
alaIgmpForwardIfIndex = _AlaIgmpForwardIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 34, 1, 1, 10, 1, 1, 2),
    _AlaIgmpForwardIfIndex_Type()
)
alaIgmpForwardIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaIgmpForwardIfIndex.setStatus("current")
_AlaIgmpForwardGroupAddress_Type = InetAddressIPv4
_AlaIgmpForwardGroupAddress_Object = MibTableColumn
alaIgmpForwardGroupAddress = _AlaIgmpForwardGroupAddress_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 34, 1, 1, 10, 1, 1, 3),
    _AlaIgmpForwardGroupAddress_Type()
)
alaIgmpForwardGroupAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaIgmpForwardGroupAddress.setStatus("current")
_AlaIgmpForwardHostAddress_Type = InetAddressIPv4
_AlaIgmpForwardHostAddress_Object = MibTableColumn
alaIgmpForwardHostAddress = _AlaIgmpForwardHostAddress_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 34, 1, 1, 10, 1, 1, 4),
    _AlaIgmpForwardHostAddress_Type()
)
alaIgmpForwardHostAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaIgmpForwardHostAddress.setStatus("current")
_AlaIgmpForwardDestAddress_Type = InetAddressIPv4
_AlaIgmpForwardDestAddress_Object = MibTableColumn
alaIgmpForwardDestAddress = _AlaIgmpForwardDestAddress_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 34, 1, 1, 10, 1, 1, 5),
    _AlaIgmpForwardDestAddress_Type()
)
alaIgmpForwardDestAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaIgmpForwardDestAddress.setStatus("current")
_AlaIgmpForwardOrigAddress_Type = InetAddressIPv4
_AlaIgmpForwardOrigAddress_Object = MibTableColumn
alaIgmpForwardOrigAddress = _AlaIgmpForwardOrigAddress_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 34, 1, 1, 10, 1, 1, 6),
    _AlaIgmpForwardOrigAddress_Type()
)
alaIgmpForwardOrigAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaIgmpForwardOrigAddress.setStatus("current")


class _AlaIgmpForwardType_Type(Integer32):
    """Custom type alaIgmpForwardType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("mcast", 1),
          ("pim", 2),
          ("ipip", 3))
    )


_AlaIgmpForwardType_Type.__name__ = "Integer32"
_AlaIgmpForwardType_Object = MibTableColumn
alaIgmpForwardType = _AlaIgmpForwardType_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 34, 1, 1, 10, 1, 1, 7),
    _AlaIgmpForwardType_Type()
)
alaIgmpForwardType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaIgmpForwardType.setStatus("current")
_AlaIgmpForwardNextVlan_Type = Unsigned32
_AlaIgmpForwardNextVlan_Object = MibTableColumn
alaIgmpForwardNextVlan = _AlaIgmpForwardNextVlan_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 34, 1, 1, 10, 1, 1, 8),
    _AlaIgmpForwardNextVlan_Type()
)
alaIgmpForwardNextVlan.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaIgmpForwardNextVlan.setStatus("current")
_AlaIgmpForwardNextIfIndex_Type = InterfaceIndex
_AlaIgmpForwardNextIfIndex_Object = MibTableColumn
alaIgmpForwardNextIfIndex = _AlaIgmpForwardNextIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 34, 1, 1, 10, 1, 1, 9),
    _AlaIgmpForwardNextIfIndex_Type()
)
alaIgmpForwardNextIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaIgmpForwardNextIfIndex.setStatus("current")


class _AlaIgmpForwardNextType_Type(Integer32):
    """Custom type alaIgmpForwardNextType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("mcast", 1),
          ("pim", 2),
          ("ipip", 3))
    )


_AlaIgmpForwardNextType_Type.__name__ = "Integer32"
_AlaIgmpForwardNextType_Object = MibTableColumn
alaIgmpForwardNextType = _AlaIgmpForwardNextType_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 34, 1, 1, 10, 1, 1, 10),
    _AlaIgmpForwardNextType_Type()
)
alaIgmpForwardNextType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaIgmpForwardNextType.setStatus("current")
_AlaIgmpTunnel_ObjectIdentity = ObjectIdentity
alaIgmpTunnel = _AlaIgmpTunnel_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 34, 1, 1, 11)
)
_AlaIgmpTunnelTable_Object = MibTable
alaIgmpTunnelTable = _AlaIgmpTunnelTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 34, 1, 1, 11, 1)
)
if mibBuilder.loadTexts:
    alaIgmpTunnelTable.setStatus("current")
_AlaIgmpTunnelEntry_Object = MibTableRow
alaIgmpTunnelEntry = _AlaIgmpTunnelEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 34, 1, 1, 11, 1, 1)
)
alaIgmpTunnelEntry.setIndexNames(
    (0, "ALCATEL-IND1-IGMP-MIB", "alaIgmpTunnelVlan"),
    (0, "ALCATEL-IND1-IGMP-MIB", "alaIgmpTunnelGroupAddress"),
    (0, "ALCATEL-IND1-IGMP-MIB", "alaIgmpTunnelHostAddress"),
    (0, "ALCATEL-IND1-IGMP-MIB", "alaIgmpTunnelDestAddress"),
    (0, "ALCATEL-IND1-IGMP-MIB", "alaIgmpTunnelOrigAddress"),
    (0, "ALCATEL-IND1-IGMP-MIB", "alaIgmpTunnelNextDestAddress"),
)
if mibBuilder.loadTexts:
    alaIgmpTunnelEntry.setStatus("current")
_AlaIgmpTunnelVlan_Type = Unsigned32
_AlaIgmpTunnelVlan_Object = MibTableColumn
alaIgmpTunnelVlan = _AlaIgmpTunnelVlan_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 34, 1, 1, 11, 1, 1, 1),
    _AlaIgmpTunnelVlan_Type()
)
alaIgmpTunnelVlan.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaIgmpTunnelVlan.setStatus("current")
_AlaIgmpTunnelIfIndex_Type = InterfaceIndex
_AlaIgmpTunnelIfIndex_Object = MibTableColumn
alaIgmpTunnelIfIndex = _AlaIgmpTunnelIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 34, 1, 1, 11, 1, 1, 2),
    _AlaIgmpTunnelIfIndex_Type()
)
alaIgmpTunnelIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaIgmpTunnelIfIndex.setStatus("current")
_AlaIgmpTunnelGroupAddress_Type = InetAddressIPv4
_AlaIgmpTunnelGroupAddress_Object = MibTableColumn
alaIgmpTunnelGroupAddress = _AlaIgmpTunnelGroupAddress_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 34, 1, 1, 11, 1, 1, 3),
    _AlaIgmpTunnelGroupAddress_Type()
)
alaIgmpTunnelGroupAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaIgmpTunnelGroupAddress.setStatus("current")
_AlaIgmpTunnelHostAddress_Type = InetAddressIPv4
_AlaIgmpTunnelHostAddress_Object = MibTableColumn
alaIgmpTunnelHostAddress = _AlaIgmpTunnelHostAddress_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 34, 1, 1, 11, 1, 1, 4),
    _AlaIgmpTunnelHostAddress_Type()
)
alaIgmpTunnelHostAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaIgmpTunnelHostAddress.setStatus("current")
_AlaIgmpTunnelDestAddress_Type = InetAddressIPv4
_AlaIgmpTunnelDestAddress_Object = MibTableColumn
alaIgmpTunnelDestAddress = _AlaIgmpTunnelDestAddress_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 34, 1, 1, 11, 1, 1, 5),
    _AlaIgmpTunnelDestAddress_Type()
)
alaIgmpTunnelDestAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaIgmpTunnelDestAddress.setStatus("current")
_AlaIgmpTunnelOrigAddress_Type = InetAddressIPv4
_AlaIgmpTunnelOrigAddress_Object = MibTableColumn
alaIgmpTunnelOrigAddress = _AlaIgmpTunnelOrigAddress_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 34, 1, 1, 11, 1, 1, 6),
    _AlaIgmpTunnelOrigAddress_Type()
)
alaIgmpTunnelOrigAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaIgmpTunnelOrigAddress.setStatus("current")


class _AlaIgmpTunnelType_Type(Integer32):
    """Custom type alaIgmpTunnelType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("mcast", 1),
          ("pim", 2),
          ("ipip", 3))
    )


_AlaIgmpTunnelType_Type.__name__ = "Integer32"
_AlaIgmpTunnelType_Object = MibTableColumn
alaIgmpTunnelType = _AlaIgmpTunnelType_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 34, 1, 1, 11, 1, 1, 7),
    _AlaIgmpTunnelType_Type()
)
alaIgmpTunnelType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaIgmpTunnelType.setStatus("current")
_AlaIgmpTunnelNextDestAddress_Type = InetAddressIPv4
_AlaIgmpTunnelNextDestAddress_Object = MibTableColumn
alaIgmpTunnelNextDestAddress = _AlaIgmpTunnelNextDestAddress_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 34, 1, 1, 11, 1, 1, 8),
    _AlaIgmpTunnelNextDestAddress_Type()
)
alaIgmpTunnelNextDestAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaIgmpTunnelNextDestAddress.setStatus("current")


class _AlaIgmpTunnelNextType_Type(Integer32):
    """Custom type alaIgmpTunnelNextType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("mcast", 1),
          ("pim", 2),
          ("ipip", 3))
    )


_AlaIgmpTunnelNextType_Type.__name__ = "Integer32"
_AlaIgmpTunnelNextType_Object = MibTableColumn
alaIgmpTunnelNextType = _AlaIgmpTunnelNextType_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 34, 1, 1, 11, 1, 1, 9),
    _AlaIgmpTunnelNextType_Type()
)
alaIgmpTunnelNextType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaIgmpTunnelNextType.setStatus("current")
_AlaIgmpPort_ObjectIdentity = ObjectIdentity
alaIgmpPort = _AlaIgmpPort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 34, 1, 1, 12)
)
_AlaIgmpPortTable_Object = MibTable
alaIgmpPortTable = _AlaIgmpPortTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 34, 1, 1, 12, 1)
)
if mibBuilder.loadTexts:
    alaIgmpPortTable.setStatus("current")
_AlaIgmpPortEntry_Object = MibTableRow
alaIgmpPortEntry = _AlaIgmpPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 34, 1, 1, 12, 1, 1)
)
alaIgmpPortEntry.setIndexNames(
    (0, "ALCATEL-IND1-IGMP-MIB", "alaIgmpPortIfIndex"),
)
if mibBuilder.loadTexts:
    alaIgmpPortEntry.setStatus("current")
_AlaIgmpPortIfIndex_Type = InterfaceIndex
_AlaIgmpPortIfIndex_Object = MibTableColumn
alaIgmpPortIfIndex = _AlaIgmpPortIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 34, 1, 1, 12, 1, 1, 1),
    _AlaIgmpPortIfIndex_Type()
)
alaIgmpPortIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaIgmpPortIfIndex.setStatus("current")


class _AlaIgmpPortMaxGroupLimit_Type(Unsigned32):
    """Custom type alaIgmpPortMaxGroupLimit based on Unsigned32"""
    defaultValue = 0


_AlaIgmpPortMaxGroupLimit_Type.__name__ = "Unsigned32"
_AlaIgmpPortMaxGroupLimit_Object = MibTableColumn
alaIgmpPortMaxGroupLimit = _AlaIgmpPortMaxGroupLimit_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 34, 1, 1, 12, 1, 1, 2),
    _AlaIgmpPortMaxGroupLimit_Type()
)
alaIgmpPortMaxGroupLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaIgmpPortMaxGroupLimit.setStatus("current")


class _AlaIgmpPortMaxGroupExceedAction_Type(Integer32):
    """Custom type alaIgmpPortMaxGroupExceedAction based on Integer32"""
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
          ("drop", 1),
          ("replace", 2))
    )


_AlaIgmpPortMaxGroupExceedAction_Type.__name__ = "Integer32"
_AlaIgmpPortMaxGroupExceedAction_Object = MibTableColumn
alaIgmpPortMaxGroupExceedAction = _AlaIgmpPortMaxGroupExceedAction_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 34, 1, 1, 12, 1, 1, 3),
    _AlaIgmpPortMaxGroupExceedAction_Type()
)
alaIgmpPortMaxGroupExceedAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaIgmpPortMaxGroupExceedAction.setStatus("current")
_AlaIgmpPortVlan_ObjectIdentity = ObjectIdentity
alaIgmpPortVlan = _AlaIgmpPortVlan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 34, 1, 1, 13)
)
_AlaIgmpPortVlanTable_Object = MibTable
alaIgmpPortVlanTable = _AlaIgmpPortVlanTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 34, 1, 1, 13, 1)
)
if mibBuilder.loadTexts:
    alaIgmpPortVlanTable.setStatus("current")
_AlaIgmpPortVlanEntry_Object = MibTableRow
alaIgmpPortVlanEntry = _AlaIgmpPortVlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 34, 1, 1, 13, 1, 1)
)
alaIgmpPortVlanEntry.setIndexNames(
    (0, "ALCATEL-IND1-IGMP-MIB", "alaIgmpPortIfIndex"),
    (0, "ALCATEL-IND1-IGMP-MIB", "alaIgmpVlanId"),
)
if mibBuilder.loadTexts:
    alaIgmpPortVlanEntry.setStatus("current")
_AlaIgmpVlanId_Type = Unsigned32
_AlaIgmpVlanId_Object = MibTableColumn
alaIgmpVlanId = _AlaIgmpVlanId_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 34, 1, 1, 13, 1, 1, 1),
    _AlaIgmpVlanId_Type()
)
alaIgmpVlanId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaIgmpVlanId.setStatus("current")
_AlaIgmpPortVlanCurrentGroupCount_Type = Unsigned32
_AlaIgmpPortVlanCurrentGroupCount_Object = MibTableColumn
alaIgmpPortVlanCurrentGroupCount = _AlaIgmpPortVlanCurrentGroupCount_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 34, 1, 1, 13, 1, 1, 2),
    _AlaIgmpPortVlanCurrentGroupCount_Type()
)
alaIgmpPortVlanCurrentGroupCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaIgmpPortVlanCurrentGroupCount.setStatus("current")
_AlaIgmpPortVlanMaxGroupLimit_Type = Unsigned32
_AlaIgmpPortVlanMaxGroupLimit_Object = MibTableColumn
alaIgmpPortVlanMaxGroupLimit = _AlaIgmpPortVlanMaxGroupLimit_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 34, 1, 1, 13, 1, 1, 3),
    _AlaIgmpPortVlanMaxGroupLimit_Type()
)
alaIgmpPortVlanMaxGroupLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaIgmpPortVlanMaxGroupLimit.setStatus("current")


class _AlaIgmpPortVlanMaxGroupExceedAction_Type(Integer32):
    """Custom type alaIgmpPortVlanMaxGroupExceedAction based on Integer32"""
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
          ("drop", 1),
          ("replace", 2))
    )


_AlaIgmpPortVlanMaxGroupExceedAction_Type.__name__ = "Integer32"
_AlaIgmpPortVlanMaxGroupExceedAction_Object = MibTableColumn
alaIgmpPortVlanMaxGroupExceedAction = _AlaIgmpPortVlanMaxGroupExceedAction_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 34, 1, 1, 13, 1, 1, 4),
    _AlaIgmpPortVlanMaxGroupExceedAction_Type()
)
alaIgmpPortVlanMaxGroupExceedAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaIgmpPortVlanMaxGroupExceedAction.setStatus("current")
_AlaIgmpStaticMemberReceiverVlan_ObjectIdentity = ObjectIdentity
alaIgmpStaticMemberReceiverVlan = _AlaIgmpStaticMemberReceiverVlan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 34, 1, 1, 14)
)
_AlaIgmpStaticMemberReceiverVlanTable_Object = MibTable
alaIgmpStaticMemberReceiverVlanTable = _AlaIgmpStaticMemberReceiverVlanTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 34, 1, 1, 14, 1)
)
if mibBuilder.loadTexts:
    alaIgmpStaticMemberReceiverVlanTable.setStatus("current")
_AlaIgmpStaticMemberReceiverVlanEntry_Object = MibTableRow
alaIgmpStaticMemberReceiverVlanEntry = _AlaIgmpStaticMemberReceiverVlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 34, 1, 1, 14, 1, 1)
)
alaIgmpStaticMemberReceiverVlanEntry.setIndexNames(
    (0, "ALCATEL-IND1-IGMP-MIB", "alaIgmpStaticMemberReceiverVlanMemberVlan"),
    (0, "ALCATEL-IND1-IGMP-MIB", "alaIgmpStaticMemberReceiverVlanPortIfIndex"),
    (0, "ALCATEL-IND1-IGMP-MIB", "alaIgmpStaticMemberReceiverVlanGroupAddress"),
    (0, "ALCATEL-IND1-IGMP-MIB", "alaIgmpStaticMemberReceiverVlanId"),
)
if mibBuilder.loadTexts:
    alaIgmpStaticMemberReceiverVlanEntry.setStatus("current")
_AlaIgmpStaticMemberReceiverVlanMemberVlan_Type = Unsigned32
_AlaIgmpStaticMemberReceiverVlanMemberVlan_Object = MibTableColumn
alaIgmpStaticMemberReceiverVlanMemberVlan = _AlaIgmpStaticMemberReceiverVlanMemberVlan_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 34, 1, 1, 14, 1, 1, 1),
    _AlaIgmpStaticMemberReceiverVlanMemberVlan_Type()
)
alaIgmpStaticMemberReceiverVlanMemberVlan.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaIgmpStaticMemberReceiverVlanMemberVlan.setStatus("current")
_AlaIgmpStaticMemberReceiverVlanPortIfIndex_Type = InterfaceIndex
_AlaIgmpStaticMemberReceiverVlanPortIfIndex_Object = MibTableColumn
alaIgmpStaticMemberReceiverVlanPortIfIndex = _AlaIgmpStaticMemberReceiverVlanPortIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 34, 1, 1, 14, 1, 1, 2),
    _AlaIgmpStaticMemberReceiverVlanPortIfIndex_Type()
)
alaIgmpStaticMemberReceiverVlanPortIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaIgmpStaticMemberReceiverVlanPortIfIndex.setStatus("current")
_AlaIgmpStaticMemberReceiverVlanGroupAddress_Type = InetAddressIPv4
_AlaIgmpStaticMemberReceiverVlanGroupAddress_Object = MibTableColumn
alaIgmpStaticMemberReceiverVlanGroupAddress = _AlaIgmpStaticMemberReceiverVlanGroupAddress_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 34, 1, 1, 14, 1, 1, 3),
    _AlaIgmpStaticMemberReceiverVlanGroupAddress_Type()
)
alaIgmpStaticMemberReceiverVlanGroupAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaIgmpStaticMemberReceiverVlanGroupAddress.setStatus("current")
_AlaIgmpStaticMemberReceiverVlanId_Type = Unsigned32
_AlaIgmpStaticMemberReceiverVlanId_Object = MibTableColumn
alaIgmpStaticMemberReceiverVlanId = _AlaIgmpStaticMemberReceiverVlanId_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 34, 1, 1, 14, 1, 1, 4),
    _AlaIgmpStaticMemberReceiverVlanId_Type()
)
alaIgmpStaticMemberReceiverVlanId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaIgmpStaticMemberReceiverVlanId.setStatus("current")
_AlaIgmpStaticMemberReceiverVlanRowStatus_Type = RowStatus
_AlaIgmpStaticMemberReceiverVlanRowStatus_Object = MibTableColumn
alaIgmpStaticMemberReceiverVlanRowStatus = _AlaIgmpStaticMemberReceiverVlanRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 34, 1, 1, 14, 1, 1, 5),
    _AlaIgmpStaticMemberReceiverVlanRowStatus_Type()
)
alaIgmpStaticMemberReceiverVlanRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaIgmpStaticMemberReceiverVlanRowStatus.setStatus("current")
_AlaIgmpReceiverVlanMember_ObjectIdentity = ObjectIdentity
alaIgmpReceiverVlanMember = _AlaIgmpReceiverVlanMember_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 34, 1, 1, 15)
)
_AlaIgmpReceiverVlanMemberTable_Object = MibTable
alaIgmpReceiverVlanMemberTable = _AlaIgmpReceiverVlanMemberTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 34, 1, 1, 15, 1)
)
if mibBuilder.loadTexts:
    alaIgmpReceiverVlanMemberTable.setStatus("current")
_AlaIgmpReceiverVlanMemberEntry_Object = MibTableRow
alaIgmpReceiverVlanMemberEntry = _AlaIgmpReceiverVlanMemberEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 34, 1, 1, 15, 1, 1)
)
alaIgmpReceiverVlanMemberEntry.setIndexNames(
    (0, "ALCATEL-IND1-IGMP-MIB", "alaIgmpReceiverVlanMemberVlan"),
    (0, "ALCATEL-IND1-IGMP-MIB", "alaIgmpReceiverVlanMemberIfIndex"),
    (0, "ALCATEL-IND1-IGMP-MIB", "alaIgmpReceiverVlanMemberGroupAddress"),
    (0, "ALCATEL-IND1-IGMP-MIB", "alaIgmpReceiverVlanMemberSourceAddress"),
    (0, "ALCATEL-IND1-IGMP-MIB", "alaIgmpReceiverVlanMemberReceiverVlan"),
)
if mibBuilder.loadTexts:
    alaIgmpReceiverVlanMemberEntry.setStatus("current")
_AlaIgmpReceiverVlanMemberVlan_Type = Unsigned32
_AlaIgmpReceiverVlanMemberVlan_Object = MibTableColumn
alaIgmpReceiverVlanMemberVlan = _AlaIgmpReceiverVlanMemberVlan_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 34, 1, 1, 15, 1, 1, 1),
    _AlaIgmpReceiverVlanMemberVlan_Type()
)
alaIgmpReceiverVlanMemberVlan.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaIgmpReceiverVlanMemberVlan.setStatus("current")
_AlaIgmpReceiverVlanMemberIfIndex_Type = InterfaceIndex
_AlaIgmpReceiverVlanMemberIfIndex_Object = MibTableColumn
alaIgmpReceiverVlanMemberIfIndex = _AlaIgmpReceiverVlanMemberIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 34, 1, 1, 15, 1, 1, 2),
    _AlaIgmpReceiverVlanMemberIfIndex_Type()
)
alaIgmpReceiverVlanMemberIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaIgmpReceiverVlanMemberIfIndex.setStatus("current")
_AlaIgmpReceiverVlanMemberGroupAddress_Type = InetAddressIPv4
_AlaIgmpReceiverVlanMemberGroupAddress_Object = MibTableColumn
alaIgmpReceiverVlanMemberGroupAddress = _AlaIgmpReceiverVlanMemberGroupAddress_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 34, 1, 1, 15, 1, 1, 3),
    _AlaIgmpReceiverVlanMemberGroupAddress_Type()
)
alaIgmpReceiverVlanMemberGroupAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaIgmpReceiverVlanMemberGroupAddress.setStatus("current")
_AlaIgmpReceiverVlanMemberSourceAddress_Type = InetAddressIPv4
_AlaIgmpReceiverVlanMemberSourceAddress_Object = MibTableColumn
alaIgmpReceiverVlanMemberSourceAddress = _AlaIgmpReceiverVlanMemberSourceAddress_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 34, 1, 1, 15, 1, 1, 4),
    _AlaIgmpReceiverVlanMemberSourceAddress_Type()
)
alaIgmpReceiverVlanMemberSourceAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaIgmpReceiverVlanMemberSourceAddress.setStatus("current")
_AlaIgmpReceiverVlanMemberReceiverVlan_Type = Unsigned32
_AlaIgmpReceiverVlanMemberReceiverVlan_Object = MibTableColumn
alaIgmpReceiverVlanMemberReceiverVlan = _AlaIgmpReceiverVlanMemberReceiverVlan_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 34, 1, 1, 15, 1, 1, 5),
    _AlaIgmpReceiverVlanMemberReceiverVlan_Type()
)
alaIgmpReceiverVlanMemberReceiverVlan.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaIgmpReceiverVlanMemberReceiverVlan.setStatus("current")


class _AlaIgmpReceiverVlanMemberMode_Type(Integer32):
    """Custom type alaIgmpReceiverVlanMemberMode based on Integer32"""
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


_AlaIgmpReceiverVlanMemberMode_Type.__name__ = "Integer32"
_AlaIgmpReceiverVlanMemberMode_Object = MibTableColumn
alaIgmpReceiverVlanMemberMode = _AlaIgmpReceiverVlanMemberMode_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 34, 1, 1, 15, 1, 1, 6),
    _AlaIgmpReceiverVlanMemberMode_Type()
)
alaIgmpReceiverVlanMemberMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaIgmpReceiverVlanMemberMode.setStatus("current")
_AlaIgmpReceiverVlanMemberCount_Type = Counter32
_AlaIgmpReceiverVlanMemberCount_Object = MibTableColumn
alaIgmpReceiverVlanMemberCount = _AlaIgmpReceiverVlanMemberCount_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 34, 1, 1, 15, 1, 1, 7),
    _AlaIgmpReceiverVlanMemberCount_Type()
)
alaIgmpReceiverVlanMemberCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaIgmpReceiverVlanMemberCount.setStatus("current")
_AlaIgmpReceiverVlanMemberTimeout_Type = TimeTicks
_AlaIgmpReceiverVlanMemberTimeout_Object = MibTableColumn
alaIgmpReceiverVlanMemberTimeout = _AlaIgmpReceiverVlanMemberTimeout_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 34, 1, 1, 15, 1, 1, 8),
    _AlaIgmpReceiverVlanMemberTimeout_Type()
)
alaIgmpReceiverVlanMemberTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaIgmpReceiverVlanMemberTimeout.setStatus("current")
_AlaIgmpReceiverVlanForward_ObjectIdentity = ObjectIdentity
alaIgmpReceiverVlanForward = _AlaIgmpReceiverVlanForward_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 34, 1, 1, 16)
)
_AlaIgmpReceiverVlanForwardTable_Object = MibTable
alaIgmpReceiverVlanForwardTable = _AlaIgmpReceiverVlanForwardTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 34, 1, 1, 16, 1)
)
if mibBuilder.loadTexts:
    alaIgmpReceiverVlanForwardTable.setStatus("current")
_AlaIgmpReceiverVlanForwardEntry_Object = MibTableRow
alaIgmpReceiverVlanForwardEntry = _AlaIgmpReceiverVlanForwardEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 34, 1, 1, 16, 1, 1)
)
alaIgmpReceiverVlanForwardEntry.setIndexNames(
    (0, "ALCATEL-IND1-IGMP-MIB", "alaIgmpReceiverVlanForwardVlan"),
    (0, "ALCATEL-IND1-IGMP-MIB", "alaIgmpReceiverVlanForwardGroupAddress"),
    (0, "ALCATEL-IND1-IGMP-MIB", "alaIgmpReceiverVlanForwardHostAddress"),
    (0, "ALCATEL-IND1-IGMP-MIB", "alaIgmpReceiverVlanForwardDestAddress"),
    (0, "ALCATEL-IND1-IGMP-MIB", "alaIgmpReceiverVlanForwardOrigAddress"),
    (0, "ALCATEL-IND1-IGMP-MIB", "alaIgmpReceiverVlanForwardNextVlan"),
    (0, "ALCATEL-IND1-IGMP-MIB", "alaIgmpReceiverVlanForwardNextIfIndex"),
    (0, "ALCATEL-IND1-IGMP-MIB", "alaIgmpReceiverVlanForwardReceiverVlan"),
)
if mibBuilder.loadTexts:
    alaIgmpReceiverVlanForwardEntry.setStatus("current")
_AlaIgmpReceiverVlanForwardVlan_Type = Unsigned32
_AlaIgmpReceiverVlanForwardVlan_Object = MibTableColumn
alaIgmpReceiverVlanForwardVlan = _AlaIgmpReceiverVlanForwardVlan_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 34, 1, 1, 16, 1, 1, 1),
    _AlaIgmpReceiverVlanForwardVlan_Type()
)
alaIgmpReceiverVlanForwardVlan.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaIgmpReceiverVlanForwardVlan.setStatus("current")
_AlaIgmpReceiverVlanForwardIfIndex_Type = InterfaceIndex
_AlaIgmpReceiverVlanForwardIfIndex_Object = MibTableColumn
alaIgmpReceiverVlanForwardIfIndex = _AlaIgmpReceiverVlanForwardIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 34, 1, 1, 16, 1, 1, 2),
    _AlaIgmpReceiverVlanForwardIfIndex_Type()
)
alaIgmpReceiverVlanForwardIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaIgmpReceiverVlanForwardIfIndex.setStatus("current")
_AlaIgmpReceiverVlanForwardGroupAddress_Type = InetAddressIPv4
_AlaIgmpReceiverVlanForwardGroupAddress_Object = MibTableColumn
alaIgmpReceiverVlanForwardGroupAddress = _AlaIgmpReceiverVlanForwardGroupAddress_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 34, 1, 1, 16, 1, 1, 3),
    _AlaIgmpReceiverVlanForwardGroupAddress_Type()
)
alaIgmpReceiverVlanForwardGroupAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaIgmpReceiverVlanForwardGroupAddress.setStatus("current")
_AlaIgmpReceiverVlanForwardHostAddress_Type = InetAddressIPv4
_AlaIgmpReceiverVlanForwardHostAddress_Object = MibTableColumn
alaIgmpReceiverVlanForwardHostAddress = _AlaIgmpReceiverVlanForwardHostAddress_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 34, 1, 1, 16, 1, 1, 4),
    _AlaIgmpReceiverVlanForwardHostAddress_Type()
)
alaIgmpReceiverVlanForwardHostAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaIgmpReceiverVlanForwardHostAddress.setStatus("current")
_AlaIgmpReceiverVlanForwardDestAddress_Type = InetAddressIPv4
_AlaIgmpReceiverVlanForwardDestAddress_Object = MibTableColumn
alaIgmpReceiverVlanForwardDestAddress = _AlaIgmpReceiverVlanForwardDestAddress_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 34, 1, 1, 16, 1, 1, 5),
    _AlaIgmpReceiverVlanForwardDestAddress_Type()
)
alaIgmpReceiverVlanForwardDestAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaIgmpReceiverVlanForwardDestAddress.setStatus("current")
_AlaIgmpReceiverVlanForwardOrigAddress_Type = InetAddressIPv4
_AlaIgmpReceiverVlanForwardOrigAddress_Object = MibTableColumn
alaIgmpReceiverVlanForwardOrigAddress = _AlaIgmpReceiverVlanForwardOrigAddress_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 34, 1, 1, 16, 1, 1, 6),
    _AlaIgmpReceiverVlanForwardOrigAddress_Type()
)
alaIgmpReceiverVlanForwardOrigAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaIgmpReceiverVlanForwardOrigAddress.setStatus("current")


class _AlaIgmpReceiverVlanForwardType_Type(Integer32):
    """Custom type alaIgmpReceiverVlanForwardType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("mcast", 1),
          ("pim", 2),
          ("ipip", 3))
    )


_AlaIgmpReceiverVlanForwardType_Type.__name__ = "Integer32"
_AlaIgmpReceiverVlanForwardType_Object = MibTableColumn
alaIgmpReceiverVlanForwardType = _AlaIgmpReceiverVlanForwardType_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 34, 1, 1, 16, 1, 1, 7),
    _AlaIgmpReceiverVlanForwardType_Type()
)
alaIgmpReceiverVlanForwardType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaIgmpReceiverVlanForwardType.setStatus("current")
_AlaIgmpReceiverVlanForwardNextVlan_Type = Unsigned32
_AlaIgmpReceiverVlanForwardNextVlan_Object = MibTableColumn
alaIgmpReceiverVlanForwardNextVlan = _AlaIgmpReceiverVlanForwardNextVlan_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 34, 1, 1, 16, 1, 1, 8),
    _AlaIgmpReceiverVlanForwardNextVlan_Type()
)
alaIgmpReceiverVlanForwardNextVlan.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaIgmpReceiverVlanForwardNextVlan.setStatus("current")
_AlaIgmpReceiverVlanForwardNextIfIndex_Type = InterfaceIndex
_AlaIgmpReceiverVlanForwardNextIfIndex_Object = MibTableColumn
alaIgmpReceiverVlanForwardNextIfIndex = _AlaIgmpReceiverVlanForwardNextIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 34, 1, 1, 16, 1, 1, 9),
    _AlaIgmpReceiverVlanForwardNextIfIndex_Type()
)
alaIgmpReceiverVlanForwardNextIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaIgmpReceiverVlanForwardNextIfIndex.setStatus("current")


class _AlaIgmpReceiverVlanForwardNextType_Type(Integer32):
    """Custom type alaIgmpReceiverVlanForwardNextType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("mcast", 1),
          ("pim", 2),
          ("ipip", 3))
    )


_AlaIgmpReceiverVlanForwardNextType_Type.__name__ = "Integer32"
_AlaIgmpReceiverVlanForwardNextType_Object = MibTableColumn
alaIgmpReceiverVlanForwardNextType = _AlaIgmpReceiverVlanForwardNextType_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 34, 1, 1, 16, 1, 1, 10),
    _AlaIgmpReceiverVlanForwardNextType_Type()
)
alaIgmpReceiverVlanForwardNextType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaIgmpReceiverVlanForwardNextType.setStatus("current")
_AlaIgmpReceiverVlanForwardReceiverVlan_Type = Unsigned32
_AlaIgmpReceiverVlanForwardReceiverVlan_Object = MibTableColumn
alaIgmpReceiverVlanForwardReceiverVlan = _AlaIgmpReceiverVlanForwardReceiverVlan_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 34, 1, 1, 16, 1, 1, 11),
    _AlaIgmpReceiverVlanForwardReceiverVlan_Type()
)
alaIgmpReceiverVlanForwardReceiverVlan.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaIgmpReceiverVlanForwardReceiverVlan.setStatus("current")
_AlaIgmpStaticSsmMap_ObjectIdentity = ObjectIdentity
alaIgmpStaticSsmMap = _AlaIgmpStaticSsmMap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 34, 1, 1, 17)
)
_AlaIgmpStaticSsmMapTable_Object = MibTable
alaIgmpStaticSsmMapTable = _AlaIgmpStaticSsmMapTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 34, 1, 1, 17, 1)
)
if mibBuilder.loadTexts:
    alaIgmpStaticSsmMapTable.setStatus("current")
_AlaIgmpStaticSsmMapEntry_Object = MibTableRow
alaIgmpStaticSsmMapEntry = _AlaIgmpStaticSsmMapEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 34, 1, 1, 17, 1, 1)
)
alaIgmpStaticSsmMapEntry.setIndexNames(
    (0, "ALCATEL-IND1-IGMP-MIB", "alaIgmpStaticSsmMapGrpAddressType"),
    (0, "ALCATEL-IND1-IGMP-MIB", "alaIgmpStaticSsmMapGrpAddress"),
    (0, "ALCATEL-IND1-IGMP-MIB", "alaIgmpStaticSsmMapSrcAddressType"),
    (0, "ALCATEL-IND1-IGMP-MIB", "alaIgmpStaticSsmMapSrcAddress"),
    (0, "ALCATEL-IND1-IGMP-MIB", "alaIgmpStaticSsmMapGrpPrefixLength"),
)
if mibBuilder.loadTexts:
    alaIgmpStaticSsmMapEntry.setStatus("current")


class _AlaIgmpStaticSsmMapGrpAddressType_Type(InetAddressType):
    """Custom type alaIgmpStaticSsmMapGrpAddressType based on InetAddressType"""
    subtypeSpec = InetAddressType.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
    )


_AlaIgmpStaticSsmMapGrpAddressType_Type.__name__ = "InetAddressType"
_AlaIgmpStaticSsmMapGrpAddressType_Object = MibTableColumn
alaIgmpStaticSsmMapGrpAddressType = _AlaIgmpStaticSsmMapGrpAddressType_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 34, 1, 1, 17, 1, 1, 1),
    _AlaIgmpStaticSsmMapGrpAddressType_Type()
)
alaIgmpStaticSsmMapGrpAddressType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaIgmpStaticSsmMapGrpAddressType.setStatus("current")
_AlaIgmpStaticSsmMapGrpAddress_Type = InetAddress
_AlaIgmpStaticSsmMapGrpAddress_Object = MibTableColumn
alaIgmpStaticSsmMapGrpAddress = _AlaIgmpStaticSsmMapGrpAddress_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 34, 1, 1, 17, 1, 1, 2),
    _AlaIgmpStaticSsmMapGrpAddress_Type()
)
alaIgmpStaticSsmMapGrpAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaIgmpStaticSsmMapGrpAddress.setStatus("current")


class _AlaIgmpStaticSsmMapSrcAddressType_Type(InetAddressType):
    """Custom type alaIgmpStaticSsmMapSrcAddressType based on InetAddressType"""
    subtypeSpec = InetAddressType.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
    )


_AlaIgmpStaticSsmMapSrcAddressType_Type.__name__ = "InetAddressType"
_AlaIgmpStaticSsmMapSrcAddressType_Object = MibTableColumn
alaIgmpStaticSsmMapSrcAddressType = _AlaIgmpStaticSsmMapSrcAddressType_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 34, 1, 1, 17, 1, 1, 3),
    _AlaIgmpStaticSsmMapSrcAddressType_Type()
)
alaIgmpStaticSsmMapSrcAddressType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaIgmpStaticSsmMapSrcAddressType.setStatus("current")
_AlaIgmpStaticSsmMapSrcAddress_Type = InetAddress
_AlaIgmpStaticSsmMapSrcAddress_Object = MibTableColumn
alaIgmpStaticSsmMapSrcAddress = _AlaIgmpStaticSsmMapSrcAddress_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 34, 1, 1, 17, 1, 1, 4),
    _AlaIgmpStaticSsmMapSrcAddress_Type()
)
alaIgmpStaticSsmMapSrcAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaIgmpStaticSsmMapSrcAddress.setStatus("current")


class _AlaIgmpStaticSsmMapGrpPrefixLength_Type(InetAddressPrefixLength):
    """Custom type alaIgmpStaticSsmMapGrpPrefixLength based on InetAddressPrefixLength"""
    subtypeSpec = InetAddressPrefixLength.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(4, 32),
    )


_AlaIgmpStaticSsmMapGrpPrefixLength_Type.__name__ = "InetAddressPrefixLength"
_AlaIgmpStaticSsmMapGrpPrefixLength_Object = MibTableColumn
alaIgmpStaticSsmMapGrpPrefixLength = _AlaIgmpStaticSsmMapGrpPrefixLength_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 34, 1, 1, 17, 1, 1, 5),
    _AlaIgmpStaticSsmMapGrpPrefixLength_Type()
)
alaIgmpStaticSsmMapGrpPrefixLength.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaIgmpStaticSsmMapGrpPrefixLength.setStatus("current")
_AlaIgmpStaticSsmMapRowStatus_Type = RowStatus
_AlaIgmpStaticSsmMapRowStatus_Object = MibTableColumn
alaIgmpStaticSsmMapRowStatus = _AlaIgmpStaticSsmMapRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 34, 1, 1, 17, 1, 1, 6),
    _AlaIgmpStaticSsmMapRowStatus_Type()
)
alaIgmpStaticSsmMapRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaIgmpStaticSsmMapRowStatus.setStatus("current")
_AlcatelIND1IgmpMIBConformance_ObjectIdentity = ObjectIdentity
alcatelIND1IgmpMIBConformance = _AlcatelIND1IgmpMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 34, 1, 2)
)
_AlcatelIND1IgmpMIBCompliances_ObjectIdentity = ObjectIdentity
alcatelIND1IgmpMIBCompliances = _AlcatelIND1IgmpMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 34, 1, 2, 1)
)
_AlcatelIND1IgmpMIBGroups_ObjectIdentity = ObjectIdentity
alcatelIND1IgmpMIBGroups = _AlcatelIND1IgmpMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 34, 1, 2, 2)
)

# Managed Objects groups

alaIgmpGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 34, 1, 2, 2, 1)
)
alaIgmpGroup.setObjects(
      *(("ALCATEL-IND1-IGMP-MIB", "alaIgmpStatus"),
        ("ALCATEL-IND1-IGMP-MIB", "alaIgmpQuerying"),
        ("ALCATEL-IND1-IGMP-MIB", "alaIgmpSpoofing"),
        ("ALCATEL-IND1-IGMP-MIB", "alaIgmpZapping"),
        ("ALCATEL-IND1-IGMP-MIB", "alaIgmpVersion"),
        ("ALCATEL-IND1-IGMP-MIB", "alaIgmpRobustness"),
        ("ALCATEL-IND1-IGMP-MIB", "alaIgmpQueryInterval"),
        ("ALCATEL-IND1-IGMP-MIB", "alaIgmpQueryResponseInterval"),
        ("ALCATEL-IND1-IGMP-MIB", "alaIgmpLastMemberQueryInterval"),
        ("ALCATEL-IND1-IGMP-MIB", "alaIgmpRouterTimeout"),
        ("ALCATEL-IND1-IGMP-MIB", "alaIgmpSourceTimeout"),
        ("ALCATEL-IND1-IGMP-MIB", "alaIgmpProxying"),
        ("ALCATEL-IND1-IGMP-MIB", "alaIgmpUnsolicitedReportInterval"),
        ("ALCATEL-IND1-IGMP-MIB", "alaIgmpQuerierForwarding"),
        ("ALCATEL-IND1-IGMP-MIB", "alaIgmpMaxGroupLimit"),
        ("ALCATEL-IND1-IGMP-MIB", "alaIgmpMaxGroupExceedAction"),
        ("ALCATEL-IND1-IGMP-MIB", "alaIgmpFloodUnknown"),
        ("ALCATEL-IND1-IGMP-MIB", "alaIgmpHelperAddressType"),
        ("ALCATEL-IND1-IGMP-MIB", "alaIgmpHelperAddress"),
        ("ALCATEL-IND1-IGMP-MIB", "alaIgmpBufferPacket"),
        ("ALCATEL-IND1-IGMP-MIB", "alaDynamicControlIpv4Status"),
        ("ALCATEL-IND1-IGMP-MIB", "alaIgmpStaticNeighborFastLearning"),
        ("ALCATEL-IND1-IGMP-MIB", "alaIgmpStarg"))
)
if mibBuilder.loadTexts:
    alaIgmpGroup.setStatus("current")

alaIgmpVlanGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 34, 1, 2, 2, 2)
)
alaIgmpVlanGroup.setObjects(
      *(("ALCATEL-IND1-IGMP-MIB", "alaIgmpVlanStatus"),
        ("ALCATEL-IND1-IGMP-MIB", "alaIgmpVlanQuerying"),
        ("ALCATEL-IND1-IGMP-MIB", "alaIgmpVlanSpoofing"),
        ("ALCATEL-IND1-IGMP-MIB", "alaIgmpVlanZapping"),
        ("ALCATEL-IND1-IGMP-MIB", "alaIgmpVlanVersion"),
        ("ALCATEL-IND1-IGMP-MIB", "alaIgmpVlanRobustness"),
        ("ALCATEL-IND1-IGMP-MIB", "alaIgmpVlanQueryInterval"),
        ("ALCATEL-IND1-IGMP-MIB", "alaIgmpVlanQueryResponseInterval"),
        ("ALCATEL-IND1-IGMP-MIB", "alaIgmpVlanLastMemberQueryInterval"),
        ("ALCATEL-IND1-IGMP-MIB", "alaIgmpVlanRouterTimeout"),
        ("ALCATEL-IND1-IGMP-MIB", "alaIgmpVlanSourceTimeout"),
        ("ALCATEL-IND1-IGMP-MIB", "alaIgmpVlanProxying"),
        ("ALCATEL-IND1-IGMP-MIB", "alaIgmpVlanUnsolicitedReportInterval"),
        ("ALCATEL-IND1-IGMP-MIB", "alaIgmpVlanQuerierForwarding"),
        ("ALCATEL-IND1-IGMP-MIB", "alaIgmpVlanMaxGroupLimit"),
        ("ALCATEL-IND1-IGMP-MIB", "alaIgmpVlanMaxGroupExceedAction"),
        ("ALCATEL-IND1-IGMP-MIB", "alaIgmpVlanSpoofAddressType"),
        ("ALCATEL-IND1-IGMP-MIB", "alaIgmpVlanSpoofAddress"),
        ("ALCATEL-IND1-IGMP-MIB", "alaIgmpVlanIndexSharing"),
        ("ALCATEL-IND1-IGMP-MIB", "alaIgmpVlanStarg"))
)
if mibBuilder.loadTexts:
    alaIgmpVlanGroup.setStatus("current")

alaIgmpMemberGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 34, 1, 2, 2, 3)
)
alaIgmpMemberGroup.setObjects(
      *(("ALCATEL-IND1-IGMP-MIB", "alaIgmpMemberMode"),
        ("ALCATEL-IND1-IGMP-MIB", "alaIgmpMemberCount"),
        ("ALCATEL-IND1-IGMP-MIB", "alaIgmpMemberTimeout"))
)
if mibBuilder.loadTexts:
    alaIgmpMemberGroup.setStatus("current")

alaIgmpStaticMemberGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 34, 1, 2, 2, 4)
)
alaIgmpStaticMemberGroup.setObjects(
    ("ALCATEL-IND1-IGMP-MIB", "alaIgmpStaticMemberRowStatus")
)
if mibBuilder.loadTexts:
    alaIgmpStaticMemberGroup.setStatus("current")

alaIgmpNeighborGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 34, 1, 2, 2, 5)
)
alaIgmpNeighborGroup.setObjects(
      *(("ALCATEL-IND1-IGMP-MIB", "alaIgmpNeighborCount"),
        ("ALCATEL-IND1-IGMP-MIB", "alaIgmpNeighborTimeout"))
)
if mibBuilder.loadTexts:
    alaIgmpNeighborGroup.setStatus("current")

alaIgmpStaticNeighborGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 34, 1, 2, 2, 6)
)
alaIgmpStaticNeighborGroup.setObjects(
    ("ALCATEL-IND1-IGMP-MIB", "alaIgmpStaticNeighborRowStatus")
)
if mibBuilder.loadTexts:
    alaIgmpStaticNeighborGroup.setStatus("current")

alaIgmpQuerierGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 34, 1, 2, 2, 7)
)
alaIgmpQuerierGroup.setObjects(
      *(("ALCATEL-IND1-IGMP-MIB", "alaIgmpQuerierCount"),
        ("ALCATEL-IND1-IGMP-MIB", "alaIgmpQuerierTimeout"))
)
if mibBuilder.loadTexts:
    alaIgmpQuerierGroup.setStatus("current")

alaIgmpStaticQuerierGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 34, 1, 2, 2, 8)
)
alaIgmpStaticQuerierGroup.setObjects(
    ("ALCATEL-IND1-IGMP-MIB", "alaIgmpStaticQuerierRowStatus")
)
if mibBuilder.loadTexts:
    alaIgmpStaticQuerierGroup.setStatus("current")

alaIgmpSourceGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 34, 1, 2, 2, 9)
)
alaIgmpSourceGroup.setObjects(
      *(("ALCATEL-IND1-IGMP-MIB", "alaIgmpSourceIfIndex"),
        ("ALCATEL-IND1-IGMP-MIB", "alaIgmpSourceType"))
)
if mibBuilder.loadTexts:
    alaIgmpSourceGroup.setStatus("current")

alaIgmpForwardGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 34, 1, 2, 2, 10)
)
alaIgmpForwardGroup.setObjects(
      *(("ALCATEL-IND1-IGMP-MIB", "alaIgmpForwardIfIndex"),
        ("ALCATEL-IND1-IGMP-MIB", "alaIgmpForwardType"),
        ("ALCATEL-IND1-IGMP-MIB", "alaIgmpForwardNextType"))
)
if mibBuilder.loadTexts:
    alaIgmpForwardGroup.setStatus("current")

alaIgmpTunnelGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 34, 1, 2, 2, 11)
)
alaIgmpTunnelGroup.setObjects(
      *(("ALCATEL-IND1-IGMP-MIB", "alaIgmpTunnelIfIndex"),
        ("ALCATEL-IND1-IGMP-MIB", "alaIgmpTunnelType"),
        ("ALCATEL-IND1-IGMP-MIB", "alaIgmpTunnelNextType"))
)
if mibBuilder.loadTexts:
    alaIgmpTunnelGroup.setStatus("current")

alaIgmpPortGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 34, 1, 2, 2, 12)
)
alaIgmpPortGroup.setObjects(
      *(("ALCATEL-IND1-IGMP-MIB", "alaIgmpPortMaxGroupLimit"),
        ("ALCATEL-IND1-IGMP-MIB", "alaIgmpPortMaxGroupExceedAction"))
)
if mibBuilder.loadTexts:
    alaIgmpPortGroup.setStatus("current")

alaIgmpPortVlanGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 34, 1, 2, 2, 13)
)
alaIgmpPortVlanGroup.setObjects(
      *(("ALCATEL-IND1-IGMP-MIB", "alaIgmpPortVlanCurrentGroupCount"),
        ("ALCATEL-IND1-IGMP-MIB", "alaIgmpPortVlanMaxGroupLimit"),
        ("ALCATEL-IND1-IGMP-MIB", "alaIgmpPortVlanMaxGroupExceedAction"))
)
if mibBuilder.loadTexts:
    alaIgmpPortVlanGroup.setStatus("current")

alaIgmpStaticMemberReceiverVlanGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 34, 1, 2, 2, 14)
)
alaIgmpStaticMemberReceiverVlanGroup.setObjects(
    ("ALCATEL-IND1-IGMP-MIB", "alaIgmpStaticMemberReceiverVlanRowStatus")
)
if mibBuilder.loadTexts:
    alaIgmpStaticMemberReceiverVlanGroup.setStatus("current")

alaIgmpReceiverVlanMemberGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 34, 1, 2, 2, 15)
)
alaIgmpReceiverVlanMemberGroup.setObjects(
      *(("ALCATEL-IND1-IGMP-MIB", "alaIgmpReceiverVlanMemberMode"),
        ("ALCATEL-IND1-IGMP-MIB", "alaIgmpReceiverVlanMemberCount"),
        ("ALCATEL-IND1-IGMP-MIB", "alaIgmpReceiverVlanMemberTimeout"))
)
if mibBuilder.loadTexts:
    alaIgmpReceiverVlanMemberGroup.setStatus("current")

alaIgmpReceiverVlanForwardGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 34, 1, 2, 2, 16)
)
alaIgmpReceiverVlanForwardGroup.setObjects(
      *(("ALCATEL-IND1-IGMP-MIB", "alaIgmpReceiverVlanForwardIfIndex"),
        ("ALCATEL-IND1-IGMP-MIB", "alaIgmpReceiverVlanForwardType"),
        ("ALCATEL-IND1-IGMP-MIB", "alaIgmpReceiverVlanForwardNextType"))
)
if mibBuilder.loadTexts:
    alaIgmpReceiverVlanForwardGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

alaIgmpCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 34, 1, 2, 1, 1)
)
alaIgmpCompliance.setObjects(
      *(("ALCATEL-IND1-IGMP-MIB", "alaIgmpGroup"),
        ("ALCATEL-IND1-IGMP-MIB", "alaIgmpVlanGroup"),
        ("ALCATEL-IND1-IGMP-MIB", "alaIgmpMemberGroup"),
        ("ALCATEL-IND1-IGMP-MIB", "alaIgmpStaticMemberGroup"),
        ("ALCATEL-IND1-IGMP-MIB", "alaIgmpNeighborGroup"),
        ("ALCATEL-IND1-IGMP-MIB", "alaIgmpStaticNeighborGroup"),
        ("ALCATEL-IND1-IGMP-MIB", "alaIgmpQuerierGroup"),
        ("ALCATEL-IND1-IGMP-MIB", "alaIgmpStaticQuerierGroup"),
        ("ALCATEL-IND1-IGMP-MIB", "alaIgmpSourceGroup"),
        ("ALCATEL-IND1-IGMP-MIB", "alaIgmpForwardGroup"),
        ("ALCATEL-IND1-IGMP-MIB", "alaIgmpTunnelGroup"),
        ("ALCATEL-IND1-IGMP-MIB", "alaIgmpPortGroup"),
        ("ALCATEL-IND1-IGMP-MIB", "alaIgmpPortVlanGroup"),
        ("ALCATEL-IND1-IGMP-MIB", "alaIgmpStaticMemberReceiverVlanGroup"),
        ("ALCATEL-IND1-IGMP-MIB", "alaIgmpReceiverVlanMemberGroup"),
        ("ALCATEL-IND1-IGMP-MIB", "alaIgmpReceiverVlanForwardGroup"))
)
if mibBuilder.loadTexts:
    alaIgmpCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ALCATEL-IND1-IGMP-MIB",
    **{"alcatelIND1IgmpMIB": alcatelIND1IgmpMIB,
       "alcatelIND1IgmpMIBObjects": alcatelIND1IgmpMIBObjects,
       "alaIgmp": alaIgmp,
       "alaIgmpStatus": alaIgmpStatus,
       "alaIgmpQuerying": alaIgmpQuerying,
       "alaIgmpSpoofing": alaIgmpSpoofing,
       "alaIgmpZapping": alaIgmpZapping,
       "alaIgmpVersion": alaIgmpVersion,
       "alaIgmpRobustness": alaIgmpRobustness,
       "alaIgmpQueryInterval": alaIgmpQueryInterval,
       "alaIgmpQueryResponseInterval": alaIgmpQueryResponseInterval,
       "alaIgmpLastMemberQueryInterval": alaIgmpLastMemberQueryInterval,
       "alaIgmpRouterTimeout": alaIgmpRouterTimeout,
       "alaIgmpSourceTimeout": alaIgmpSourceTimeout,
       "alaIgmpProxying": alaIgmpProxying,
       "alaIgmpUnsolicitedReportInterval": alaIgmpUnsolicitedReportInterval,
       "alaIgmpQuerierForwarding": alaIgmpQuerierForwarding,
       "alaIgmpMaxGroupLimit": alaIgmpMaxGroupLimit,
       "alaIgmpMaxGroupExceedAction": alaIgmpMaxGroupExceedAction,
       "alaIgmpFloodUnknown": alaIgmpFloodUnknown,
       "alaIgmpHelperAddressType": alaIgmpHelperAddressType,
       "alaIgmpHelperAddress": alaIgmpHelperAddress,
       "alaIgmpBufferPacket": alaIgmpBufferPacket,
       "alaIgmpIndexSharing": alaIgmpIndexSharing,
       "alaDynamicControlStatus": alaDynamicControlStatus,
       "alaDynamicControlIpv4Status": alaDynamicControlIpv4Status,
       "alaIgmpStaticNeighborFastLearning": alaIgmpStaticNeighborFastLearning,
       "alaIgmpStarg": alaIgmpStarg,
       "alaIgmpVlan": alaIgmpVlan,
       "alaIgmpVlanTable": alaIgmpVlanTable,
       "alaIgmpVlanEntry": alaIgmpVlanEntry,
       "alaIgmpVlanIndex": alaIgmpVlanIndex,
       "alaIgmpVlanStatus": alaIgmpVlanStatus,
       "alaIgmpVlanQuerying": alaIgmpVlanQuerying,
       "alaIgmpVlanSpoofing": alaIgmpVlanSpoofing,
       "alaIgmpVlanZapping": alaIgmpVlanZapping,
       "alaIgmpVlanVersion": alaIgmpVlanVersion,
       "alaIgmpVlanRobustness": alaIgmpVlanRobustness,
       "alaIgmpVlanQueryInterval": alaIgmpVlanQueryInterval,
       "alaIgmpVlanQueryResponseInterval": alaIgmpVlanQueryResponseInterval,
       "alaIgmpVlanLastMemberQueryInterval": alaIgmpVlanLastMemberQueryInterval,
       "alaIgmpVlanRouterTimeout": alaIgmpVlanRouterTimeout,
       "alaIgmpVlanSourceTimeout": alaIgmpVlanSourceTimeout,
       "alaIgmpVlanProxying": alaIgmpVlanProxying,
       "alaIgmpVlanUnsolicitedReportInterval": alaIgmpVlanUnsolicitedReportInterval,
       "alaIgmpVlanQuerierForwarding": alaIgmpVlanQuerierForwarding,
       "alaIgmpVlanMaxGroupLimit": alaIgmpVlanMaxGroupLimit,
       "alaIgmpVlanMaxGroupExceedAction": alaIgmpVlanMaxGroupExceedAction,
       "alaIgmpVlanSpoofAddressType": alaIgmpVlanSpoofAddressType,
       "alaIgmpVlanSpoofAddress": alaIgmpVlanSpoofAddress,
       "alaIgmpVlanIndexSharing": alaIgmpVlanIndexSharing,
       "alaIgmpVlanStarg": alaIgmpVlanStarg,
       "alaIgmpMember": alaIgmpMember,
       "alaIgmpMemberTable": alaIgmpMemberTable,
       "alaIgmpMemberEntry": alaIgmpMemberEntry,
       "alaIgmpMemberVlan": alaIgmpMemberVlan,
       "alaIgmpMemberIfIndex": alaIgmpMemberIfIndex,
       "alaIgmpMemberGroupAddress": alaIgmpMemberGroupAddress,
       "alaIgmpMemberSourceAddress": alaIgmpMemberSourceAddress,
       "alaIgmpMemberMode": alaIgmpMemberMode,
       "alaIgmpMemberCount": alaIgmpMemberCount,
       "alaIgmpMemberTimeout": alaIgmpMemberTimeout,
       "alaIgmpStaticMember": alaIgmpStaticMember,
       "alaIgmpStaticMemberTable": alaIgmpStaticMemberTable,
       "alaIgmpStaticMemberEntry": alaIgmpStaticMemberEntry,
       "alaIgmpStaticMemberVlan": alaIgmpStaticMemberVlan,
       "alaIgmpStaticMemberIfIndex": alaIgmpStaticMemberIfIndex,
       "alaIgmpStaticMemberGroupAddress": alaIgmpStaticMemberGroupAddress,
       "alaIgmpStaticMemberRowStatus": alaIgmpStaticMemberRowStatus,
       "alaIgmpNeighbor": alaIgmpNeighbor,
       "alaIgmpNeighborTable": alaIgmpNeighborTable,
       "alaIgmpNeighborEntry": alaIgmpNeighborEntry,
       "alaIgmpNeighborVlan": alaIgmpNeighborVlan,
       "alaIgmpNeighborIfIndex": alaIgmpNeighborIfIndex,
       "alaIgmpNeighborHostAddress": alaIgmpNeighborHostAddress,
       "alaIgmpNeighborCount": alaIgmpNeighborCount,
       "alaIgmpNeighborTimeout": alaIgmpNeighborTimeout,
       "alaIgmpStaticNeighbor": alaIgmpStaticNeighbor,
       "alaIgmpStaticNeighborTable": alaIgmpStaticNeighborTable,
       "alaIgmpStaticNeighborEntry": alaIgmpStaticNeighborEntry,
       "alaIgmpStaticNeighborVlan": alaIgmpStaticNeighborVlan,
       "alaIgmpStaticNeighborIfIndex": alaIgmpStaticNeighborIfIndex,
       "alaIgmpStaticNeighborRowStatus": alaIgmpStaticNeighborRowStatus,
       "alaIgmpQuerier": alaIgmpQuerier,
       "alaIgmpQuerierTable": alaIgmpQuerierTable,
       "alaIgmpQuerierEntry": alaIgmpQuerierEntry,
       "alaIgmpQuerierVlan": alaIgmpQuerierVlan,
       "alaIgmpQuerierIfIndex": alaIgmpQuerierIfIndex,
       "alaIgmpQuerierHostAddress": alaIgmpQuerierHostAddress,
       "alaIgmpQuerierCount": alaIgmpQuerierCount,
       "alaIgmpQuerierTimeout": alaIgmpQuerierTimeout,
       "alaIgmpStaticQuerier": alaIgmpStaticQuerier,
       "alaIgmpStaticQuerierTable": alaIgmpStaticQuerierTable,
       "alaIgmpStaticQuerierEntry": alaIgmpStaticQuerierEntry,
       "alaIgmpStaticQuerierVlan": alaIgmpStaticQuerierVlan,
       "alaIgmpStaticQuerierIfIndex": alaIgmpStaticQuerierIfIndex,
       "alaIgmpStaticQuerierRowStatus": alaIgmpStaticQuerierRowStatus,
       "alaIgmpSource": alaIgmpSource,
       "alaIgmpSourceTable": alaIgmpSourceTable,
       "alaIgmpSourceEntry": alaIgmpSourceEntry,
       "alaIgmpSourceVlan": alaIgmpSourceVlan,
       "alaIgmpSourceIfIndex": alaIgmpSourceIfIndex,
       "alaIgmpSourceGroupAddress": alaIgmpSourceGroupAddress,
       "alaIgmpSourceHostAddress": alaIgmpSourceHostAddress,
       "alaIgmpSourceDestAddress": alaIgmpSourceDestAddress,
       "alaIgmpSourceOrigAddress": alaIgmpSourceOrigAddress,
       "alaIgmpSourceType": alaIgmpSourceType,
       "alaIgmpForward": alaIgmpForward,
       "alaIgmpForwardTable": alaIgmpForwardTable,
       "alaIgmpForwardEntry": alaIgmpForwardEntry,
       "alaIgmpForwardVlan": alaIgmpForwardVlan,
       "alaIgmpForwardIfIndex": alaIgmpForwardIfIndex,
       "alaIgmpForwardGroupAddress": alaIgmpForwardGroupAddress,
       "alaIgmpForwardHostAddress": alaIgmpForwardHostAddress,
       "alaIgmpForwardDestAddress": alaIgmpForwardDestAddress,
       "alaIgmpForwardOrigAddress": alaIgmpForwardOrigAddress,
       "alaIgmpForwardType": alaIgmpForwardType,
       "alaIgmpForwardNextVlan": alaIgmpForwardNextVlan,
       "alaIgmpForwardNextIfIndex": alaIgmpForwardNextIfIndex,
       "alaIgmpForwardNextType": alaIgmpForwardNextType,
       "alaIgmpTunnel": alaIgmpTunnel,
       "alaIgmpTunnelTable": alaIgmpTunnelTable,
       "alaIgmpTunnelEntry": alaIgmpTunnelEntry,
       "alaIgmpTunnelVlan": alaIgmpTunnelVlan,
       "alaIgmpTunnelIfIndex": alaIgmpTunnelIfIndex,
       "alaIgmpTunnelGroupAddress": alaIgmpTunnelGroupAddress,
       "alaIgmpTunnelHostAddress": alaIgmpTunnelHostAddress,
       "alaIgmpTunnelDestAddress": alaIgmpTunnelDestAddress,
       "alaIgmpTunnelOrigAddress": alaIgmpTunnelOrigAddress,
       "alaIgmpTunnelType": alaIgmpTunnelType,
       "alaIgmpTunnelNextDestAddress": alaIgmpTunnelNextDestAddress,
       "alaIgmpTunnelNextType": alaIgmpTunnelNextType,
       "alaIgmpPort": alaIgmpPort,
       "alaIgmpPortTable": alaIgmpPortTable,
       "alaIgmpPortEntry": alaIgmpPortEntry,
       "alaIgmpPortIfIndex": alaIgmpPortIfIndex,
       "alaIgmpPortMaxGroupLimit": alaIgmpPortMaxGroupLimit,
       "alaIgmpPortMaxGroupExceedAction": alaIgmpPortMaxGroupExceedAction,
       "alaIgmpPortVlan": alaIgmpPortVlan,
       "alaIgmpPortVlanTable": alaIgmpPortVlanTable,
       "alaIgmpPortVlanEntry": alaIgmpPortVlanEntry,
       "alaIgmpVlanId": alaIgmpVlanId,
       "alaIgmpPortVlanCurrentGroupCount": alaIgmpPortVlanCurrentGroupCount,
       "alaIgmpPortVlanMaxGroupLimit": alaIgmpPortVlanMaxGroupLimit,
       "alaIgmpPortVlanMaxGroupExceedAction": alaIgmpPortVlanMaxGroupExceedAction,
       "alaIgmpStaticMemberReceiverVlan": alaIgmpStaticMemberReceiverVlan,
       "alaIgmpStaticMemberReceiverVlanTable": alaIgmpStaticMemberReceiverVlanTable,
       "alaIgmpStaticMemberReceiverVlanEntry": alaIgmpStaticMemberReceiverVlanEntry,
       "alaIgmpStaticMemberReceiverVlanMemberVlan": alaIgmpStaticMemberReceiverVlanMemberVlan,
       "alaIgmpStaticMemberReceiverVlanPortIfIndex": alaIgmpStaticMemberReceiverVlanPortIfIndex,
       "alaIgmpStaticMemberReceiverVlanGroupAddress": alaIgmpStaticMemberReceiverVlanGroupAddress,
       "alaIgmpStaticMemberReceiverVlanId": alaIgmpStaticMemberReceiverVlanId,
       "alaIgmpStaticMemberReceiverVlanRowStatus": alaIgmpStaticMemberReceiverVlanRowStatus,
       "alaIgmpReceiverVlanMember": alaIgmpReceiverVlanMember,
       "alaIgmpReceiverVlanMemberTable": alaIgmpReceiverVlanMemberTable,
       "alaIgmpReceiverVlanMemberEntry": alaIgmpReceiverVlanMemberEntry,
       "alaIgmpReceiverVlanMemberVlan": alaIgmpReceiverVlanMemberVlan,
       "alaIgmpReceiverVlanMemberIfIndex": alaIgmpReceiverVlanMemberIfIndex,
       "alaIgmpReceiverVlanMemberGroupAddress": alaIgmpReceiverVlanMemberGroupAddress,
       "alaIgmpReceiverVlanMemberSourceAddress": alaIgmpReceiverVlanMemberSourceAddress,
       "alaIgmpReceiverVlanMemberReceiverVlan": alaIgmpReceiverVlanMemberReceiverVlan,
       "alaIgmpReceiverVlanMemberMode": alaIgmpReceiverVlanMemberMode,
       "alaIgmpReceiverVlanMemberCount": alaIgmpReceiverVlanMemberCount,
       "alaIgmpReceiverVlanMemberTimeout": alaIgmpReceiverVlanMemberTimeout,
       "alaIgmpReceiverVlanForward": alaIgmpReceiverVlanForward,
       "alaIgmpReceiverVlanForwardTable": alaIgmpReceiverVlanForwardTable,
       "alaIgmpReceiverVlanForwardEntry": alaIgmpReceiverVlanForwardEntry,
       "alaIgmpReceiverVlanForwardVlan": alaIgmpReceiverVlanForwardVlan,
       "alaIgmpReceiverVlanForwardIfIndex": alaIgmpReceiverVlanForwardIfIndex,
       "alaIgmpReceiverVlanForwardGroupAddress": alaIgmpReceiverVlanForwardGroupAddress,
       "alaIgmpReceiverVlanForwardHostAddress": alaIgmpReceiverVlanForwardHostAddress,
       "alaIgmpReceiverVlanForwardDestAddress": alaIgmpReceiverVlanForwardDestAddress,
       "alaIgmpReceiverVlanForwardOrigAddress": alaIgmpReceiverVlanForwardOrigAddress,
       "alaIgmpReceiverVlanForwardType": alaIgmpReceiverVlanForwardType,
       "alaIgmpReceiverVlanForwardNextVlan": alaIgmpReceiverVlanForwardNextVlan,
       "alaIgmpReceiverVlanForwardNextIfIndex": alaIgmpReceiverVlanForwardNextIfIndex,
       "alaIgmpReceiverVlanForwardNextType": alaIgmpReceiverVlanForwardNextType,
       "alaIgmpReceiverVlanForwardReceiverVlan": alaIgmpReceiverVlanForwardReceiverVlan,
       "alaIgmpStaticSsmMap": alaIgmpStaticSsmMap,
       "alaIgmpStaticSsmMapTable": alaIgmpStaticSsmMapTable,
       "alaIgmpStaticSsmMapEntry": alaIgmpStaticSsmMapEntry,
       "alaIgmpStaticSsmMapGrpAddressType": alaIgmpStaticSsmMapGrpAddressType,
       "alaIgmpStaticSsmMapGrpAddress": alaIgmpStaticSsmMapGrpAddress,
       "alaIgmpStaticSsmMapSrcAddressType": alaIgmpStaticSsmMapSrcAddressType,
       "alaIgmpStaticSsmMapSrcAddress": alaIgmpStaticSsmMapSrcAddress,
       "alaIgmpStaticSsmMapGrpPrefixLength": alaIgmpStaticSsmMapGrpPrefixLength,
       "alaIgmpStaticSsmMapRowStatus": alaIgmpStaticSsmMapRowStatus,
       "alcatelIND1IgmpMIBConformance": alcatelIND1IgmpMIBConformance,
       "alcatelIND1IgmpMIBCompliances": alcatelIND1IgmpMIBCompliances,
       "alaIgmpCompliance": alaIgmpCompliance,
       "alcatelIND1IgmpMIBGroups": alcatelIND1IgmpMIBGroups,
       "alaIgmpGroup": alaIgmpGroup,
       "alaIgmpVlanGroup": alaIgmpVlanGroup,
       "alaIgmpMemberGroup": alaIgmpMemberGroup,
       "alaIgmpStaticMemberGroup": alaIgmpStaticMemberGroup,
       "alaIgmpNeighborGroup": alaIgmpNeighborGroup,
       "alaIgmpStaticNeighborGroup": alaIgmpStaticNeighborGroup,
       "alaIgmpQuerierGroup": alaIgmpQuerierGroup,
       "alaIgmpStaticQuerierGroup": alaIgmpStaticQuerierGroup,
       "alaIgmpSourceGroup": alaIgmpSourceGroup,
       "alaIgmpForwardGroup": alaIgmpForwardGroup,
       "alaIgmpTunnelGroup": alaIgmpTunnelGroup,
       "alaIgmpPortGroup": alaIgmpPortGroup,
       "alaIgmpPortVlanGroup": alaIgmpPortVlanGroup,
       "alaIgmpStaticMemberReceiverVlanGroup": alaIgmpStaticMemberReceiverVlanGroup,
       "alaIgmpReceiverVlanMemberGroup": alaIgmpReceiverVlanMemberGroup,
       "alaIgmpReceiverVlanForwardGroup": alaIgmpReceiverVlanForwardGroup}
)
