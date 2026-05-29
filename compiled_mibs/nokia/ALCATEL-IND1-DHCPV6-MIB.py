# SNMP MIB module (ALCATEL-IND1-DHCPV6-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\nokia\aos7\ALCATEL-IND1-DHCPV6-MIB

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

(softentIND1Ipv6,) = mibBuilder.importSymbols(
    "ALCATEL-IND1-BASE",
    "softentIND1Ipv6")

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

(ipv6IfIndex,) = mibBuilder.importSymbols(
    "IPV6-MIB",
    "ipv6IfIndex")

(Ipv6Address,
 Ipv6IfIndexOrZero) = mibBuilder.importSymbols(
    "IPV6-TC",
    "Ipv6Address",
    "Ipv6IfIndexOrZero")

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

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
 PhysAddress,
 RowStatus,
 TextualConvention,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TimeStamp",
    "TruthValue")


# MODULE-IDENTITY

alcatelIND1DHCPv6MIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 29, 2)
)
if mibBuilder.loadTexts:
    alcatelIND1DHCPv6MIB.setRevisions(
        ("2019-11-27 00:00",
         "2018-12-05 00:00",
         "2018-07-09 00:00",
         "2013-03-22 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class AlaDHCPv6GuardTrustedSourceIfIndex(TextualConvention, Integer32):
    status = "current"
    displayHint = "d"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )



# MIB Managed Objects in the order of their OIDs

_AlcatelIND1DHCPv6MIBNotifications_ObjectIdentity = ObjectIdentity
alcatelIND1DHCPv6MIBNotifications = _AlcatelIND1DHCPv6MIBNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 29, 2, 0)
)
_AlcatelIND1DHCPv6MIBObjects_ObjectIdentity = ObjectIdentity
alcatelIND1DHCPv6MIBObjects = _AlcatelIND1DHCPv6MIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 29, 2, 1)
)
_AlaDHCPv6RelayConfig_ObjectIdentity = ObjectIdentity
alaDHCPv6RelayConfig = _AlaDHCPv6RelayConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 29, 2, 1, 1)
)


class _AlaDHCPv6RelayAdminStatus_Type(Integer32):
    """Custom type alaDHCPv6RelayAdminStatus based on Integer32"""
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


_AlaDHCPv6RelayAdminStatus_Type.__name__ = "Integer32"
_AlaDHCPv6RelayAdminStatus_Object = MibScalar
alaDHCPv6RelayAdminStatus = _AlaDHCPv6RelayAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 29, 2, 1, 1, 1),
    _AlaDHCPv6RelayAdminStatus_Type()
)
alaDHCPv6RelayAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaDHCPv6RelayAdminStatus.setStatus("current")


class _AlaDHCPv6RelayMaximumHops_Type(Unsigned32):
    """Custom type alaDHCPv6RelayMaximumHops based on Unsigned32"""
    defaultValue = 32

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_AlaDHCPv6RelayMaximumHops_Type.__name__ = "Unsigned32"
_AlaDHCPv6RelayMaximumHops_Object = MibScalar
alaDHCPv6RelayMaximumHops = _AlaDHCPv6RelayMaximumHops_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 29, 2, 1, 1, 2),
    _AlaDHCPv6RelayMaximumHops_Type()
)
alaDHCPv6RelayMaximumHops.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaDHCPv6RelayMaximumHops.setStatus("current")


class _AlaDHCPv6RelayInterfaceIDStatus_Type(Integer32):
    """Custom type alaDHCPv6RelayInterfaceIDStatus based on Integer32"""
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


_AlaDHCPv6RelayInterfaceIDStatus_Type.__name__ = "Integer32"
_AlaDHCPv6RelayInterfaceIDStatus_Object = MibScalar
alaDHCPv6RelayInterfaceIDStatus = _AlaDHCPv6RelayInterfaceIDStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 29, 2, 1, 1, 3),
    _AlaDHCPv6RelayInterfaceIDStatus_Type()
)
alaDHCPv6RelayInterfaceIDStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaDHCPv6RelayInterfaceIDStatus.setStatus("current")


class _AlaDHCPv6RelayInterfaceIDPrefix_Type(SnmpAdminString):
    """Custom type alaDHCPv6RelayInterfaceIDPrefix based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_AlaDHCPv6RelayInterfaceIDPrefix_Type.__name__ = "SnmpAdminString"
_AlaDHCPv6RelayInterfaceIDPrefix_Object = MibScalar
alaDHCPv6RelayInterfaceIDPrefix = _AlaDHCPv6RelayInterfaceIDPrefix_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 29, 2, 1, 1, 4),
    _AlaDHCPv6RelayInterfaceIDPrefix_Type()
)
alaDHCPv6RelayInterfaceIDPrefix.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaDHCPv6RelayInterfaceIDPrefix.setStatus("current")


class _AlaDHCPv6RelayRemoteIDStatus_Type(Integer32):
    """Custom type alaDHCPv6RelayRemoteIDStatus based on Integer32"""
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


_AlaDHCPv6RelayRemoteIDStatus_Type.__name__ = "Integer32"
_AlaDHCPv6RelayRemoteIDStatus_Object = MibScalar
alaDHCPv6RelayRemoteIDStatus = _AlaDHCPv6RelayRemoteIDStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 29, 2, 1, 1, 5),
    _AlaDHCPv6RelayRemoteIDStatus_Type()
)
alaDHCPv6RelayRemoteIDStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaDHCPv6RelayRemoteIDStatus.setStatus("current")


class _AlaDHCPv6RelayRemoteIDFormatType_Type(Integer32):
    """Custom type alaDHCPv6RelayRemoteIDFormatType based on Integer32"""
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
        *(("baseMac", 1),
          ("systemName", 2),
          ("vlan", 3),
          ("userString", 4),
          ("interfaceAlias", 5),
          ("autoInterfaceAlias", 6),
          ("disable", 7))
    )


_AlaDHCPv6RelayRemoteIDFormatType_Type.__name__ = "Integer32"
_AlaDHCPv6RelayRemoteIDFormatType_Object = MibScalar
alaDHCPv6RelayRemoteIDFormatType = _AlaDHCPv6RelayRemoteIDFormatType_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 29, 2, 1, 1, 6),
    _AlaDHCPv6RelayRemoteIDFormatType_Type()
)
alaDHCPv6RelayRemoteIDFormatType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaDHCPv6RelayRemoteIDFormatType.setStatus("current")


class _AlaDHCPv6RelayRemoteIDStringValue_Type(SnmpAdminString):
    """Custom type alaDHCPv6RelayRemoteIDStringValue based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_AlaDHCPv6RelayRemoteIDStringValue_Type.__name__ = "SnmpAdminString"
_AlaDHCPv6RelayRemoteIDStringValue_Object = MibScalar
alaDHCPv6RelayRemoteIDStringValue = _AlaDHCPv6RelayRemoteIDStringValue_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 29, 2, 1, 1, 7),
    _AlaDHCPv6RelayRemoteIDStringValue_Type()
)
alaDHCPv6RelayRemoteIDStringValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaDHCPv6RelayRemoteIDStringValue.setStatus("current")


class _AlaDHCPv6RelayRemoteIDEnterpriseNumber_Type(Unsigned32):
    """Custom type alaDHCPv6RelayRemoteIDEnterpriseNumber based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 4294967295),
    )


_AlaDHCPv6RelayRemoteIDEnterpriseNumber_Type.__name__ = "Unsigned32"
_AlaDHCPv6RelayRemoteIDEnterpriseNumber_Object = MibScalar
alaDHCPv6RelayRemoteIDEnterpriseNumber = _AlaDHCPv6RelayRemoteIDEnterpriseNumber_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 29, 2, 1, 1, 8),
    _AlaDHCPv6RelayRemoteIDEnterpriseNumber_Type()
)
alaDHCPv6RelayRemoteIDEnterpriseNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaDHCPv6RelayRemoteIDEnterpriseNumber.setStatus("current")
_AlaDHCPv6SrvConfig_ObjectIdentity = ObjectIdentity
alaDHCPv6SrvConfig = _AlaDHCPv6SrvConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 29, 2, 1, 2)
)


class _AlaDHCPv6SrvGlobalConfigStatus_Type(Integer32):
    """Custom type alaDHCPv6SrvGlobalConfigStatus based on Integer32"""
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


_AlaDHCPv6SrvGlobalConfigStatus_Type.__name__ = "Integer32"
_AlaDHCPv6SrvGlobalConfigStatus_Object = MibScalar
alaDHCPv6SrvGlobalConfigStatus = _AlaDHCPv6SrvGlobalConfigStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 29, 2, 1, 2, 1),
    _AlaDHCPv6SrvGlobalConfigStatus_Type()
)
alaDHCPv6SrvGlobalConfigStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaDHCPv6SrvGlobalConfigStatus.setStatus("current")


class _AlaDHCPv6SrvGlobalRestart_Type(Integer32):
    """Custom type alaDHCPv6SrvGlobalRestart based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("inactive", 1),
          ("restart", 2))
    )


_AlaDHCPv6SrvGlobalRestart_Type.__name__ = "Integer32"
_AlaDHCPv6SrvGlobalRestart_Object = MibScalar
alaDHCPv6SrvGlobalRestart = _AlaDHCPv6SrvGlobalRestart_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 29, 2, 1, 2, 2),
    _AlaDHCPv6SrvGlobalRestart_Type()
)
alaDHCPv6SrvGlobalRestart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaDHCPv6SrvGlobalRestart.setStatus("current")


class _AlaDHCPv6SrvGlobalClearStat_Type(Integer32):
    """Custom type alaDHCPv6SrvGlobalClearStat based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("default", 1),
          ("reset", 2))
    )


_AlaDHCPv6SrvGlobalClearStat_Type.__name__ = "Integer32"
_AlaDHCPv6SrvGlobalClearStat_Object = MibScalar
alaDHCPv6SrvGlobalClearStat = _AlaDHCPv6SrvGlobalClearStat_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 29, 2, 1, 2, 3),
    _AlaDHCPv6SrvGlobalClearStat_Type()
)
alaDHCPv6SrvGlobalClearStat.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaDHCPv6SrvGlobalClearStat.setStatus("current")
_AlaDHCPv6RelayInterfaceTable_Object = MibTable
alaDHCPv6RelayInterfaceTable = _AlaDHCPv6RelayInterfaceTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 29, 2, 1, 3)
)
if mibBuilder.loadTexts:
    alaDHCPv6RelayInterfaceTable.setStatus("current")
_AlaDHCPv6RelayInterfaceEntry_Object = MibTableRow
alaDHCPv6RelayInterfaceEntry = _AlaDHCPv6RelayInterfaceEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 29, 2, 1, 3, 1)
)
alaDHCPv6RelayInterfaceEntry.setIndexNames(
    (0, "IPV6-MIB", "ipv6IfIndex"),
)
if mibBuilder.loadTexts:
    alaDHCPv6RelayInterfaceEntry.setStatus("current")


class _AlaDHCPv6RelayInterfaceAdminStatus_Type(Integer32):
    """Custom type alaDHCPv6RelayInterfaceAdminStatus based on Integer32"""
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


_AlaDHCPv6RelayInterfaceAdminStatus_Type.__name__ = "Integer32"
_AlaDHCPv6RelayInterfaceAdminStatus_Object = MibTableColumn
alaDHCPv6RelayInterfaceAdminStatus = _AlaDHCPv6RelayInterfaceAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 29, 2, 1, 3, 1, 1),
    _AlaDHCPv6RelayInterfaceAdminStatus_Type()
)
alaDHCPv6RelayInterfaceAdminStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaDHCPv6RelayInterfaceAdminStatus.setStatus("current")
_AlaDHCPv6RelayDestinationTable_Object = MibTable
alaDHCPv6RelayDestinationTable = _AlaDHCPv6RelayDestinationTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 29, 2, 1, 4)
)
if mibBuilder.loadTexts:
    alaDHCPv6RelayDestinationTable.setStatus("current")
_AlaDHCPv6RelayDestinationEntry_Object = MibTableRow
alaDHCPv6RelayDestinationEntry = _AlaDHCPv6RelayDestinationEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 29, 2, 1, 4, 1)
)
alaDHCPv6RelayDestinationEntry.setIndexNames(
    (0, "IPV6-MIB", "ipv6IfIndex"),
    (0, "ALCATEL-IND1-DHCPV6-MIB", "alaDHCPv6RelayDestinationAddressType"),
    (0, "ALCATEL-IND1-DHCPV6-MIB", "alaDHCPv6RelayDestinationAddress"),
)
if mibBuilder.loadTexts:
    alaDHCPv6RelayDestinationEntry.setStatus("current")
_AlaDHCPv6RelayDestinationAddressType_Type = InetAddressType
_AlaDHCPv6RelayDestinationAddressType_Object = MibTableColumn
alaDHCPv6RelayDestinationAddressType = _AlaDHCPv6RelayDestinationAddressType_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 29, 2, 1, 4, 1, 1),
    _AlaDHCPv6RelayDestinationAddressType_Type()
)
alaDHCPv6RelayDestinationAddressType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaDHCPv6RelayDestinationAddressType.setStatus("current")
_AlaDHCPv6RelayDestinationAddress_Type = InetAddress
_AlaDHCPv6RelayDestinationAddress_Object = MibTableColumn
alaDHCPv6RelayDestinationAddress = _AlaDHCPv6RelayDestinationAddress_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 29, 2, 1, 4, 1, 2),
    _AlaDHCPv6RelayDestinationAddress_Type()
)
alaDHCPv6RelayDestinationAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaDHCPv6RelayDestinationAddress.setStatus("current")
_AlaDHCPv6RelayDestinationRowStatus_Type = RowStatus
_AlaDHCPv6RelayDestinationRowStatus_Object = MibTableColumn
alaDHCPv6RelayDestinationRowStatus = _AlaDHCPv6RelayDestinationRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 29, 2, 1, 4, 1, 3),
    _AlaDHCPv6RelayDestinationRowStatus_Type()
)
alaDHCPv6RelayDestinationRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaDHCPv6RelayDestinationRowStatus.setStatus("current")
_AlaDHCPv6SrvLease_ObjectIdentity = ObjectIdentity
alaDHCPv6SrvLease = _AlaDHCPv6SrvLease_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 29, 2, 1, 5)
)
_AlaDHCPv6SrvLeaseTable_Object = MibTable
alaDHCPv6SrvLeaseTable = _AlaDHCPv6SrvLeaseTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 29, 2, 1, 5, 1)
)
if mibBuilder.loadTexts:
    alaDHCPv6SrvLeaseTable.setStatus("current")
_AlaDHCPv6SrvLeaseEntry_Object = MibTableRow
alaDHCPv6SrvLeaseEntry = _AlaDHCPv6SrvLeaseEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 29, 2, 1, 5, 1, 1)
)
alaDHCPv6SrvLeaseEntry.setIndexNames(
    (0, "ALCATEL-IND1-DHCPV6-MIB", "alaDHCPv6SrvLeaseIpv6Address"),
)
if mibBuilder.loadTexts:
    alaDHCPv6SrvLeaseEntry.setStatus("current")
_AlaDHCPv6SrvLeaseIpv6Address_Type = Ipv6Address
_AlaDHCPv6SrvLeaseIpv6Address_Object = MibTableColumn
alaDHCPv6SrvLeaseIpv6Address = _AlaDHCPv6SrvLeaseIpv6Address_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 29, 2, 1, 5, 1, 1, 1),
    _AlaDHCPv6SrvLeaseIpv6Address_Type()
)
alaDHCPv6SrvLeaseIpv6Address.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaDHCPv6SrvLeaseIpv6Address.setStatus("current")
_AlaDHCPv6SrvLeaseLeaseGrant_Type = DateAndTime
_AlaDHCPv6SrvLeaseLeaseGrant_Object = MibTableColumn
alaDHCPv6SrvLeaseLeaseGrant = _AlaDHCPv6SrvLeaseLeaseGrant_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 29, 2, 1, 5, 1, 1, 2),
    _AlaDHCPv6SrvLeaseLeaseGrant_Type()
)
alaDHCPv6SrvLeaseLeaseGrant.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaDHCPv6SrvLeaseLeaseGrant.setStatus("current")
_AlaDHCPv6SrvLeasePrefLeaseExpiry_Type = DateAndTime
_AlaDHCPv6SrvLeasePrefLeaseExpiry_Object = MibTableColumn
alaDHCPv6SrvLeasePrefLeaseExpiry = _AlaDHCPv6SrvLeasePrefLeaseExpiry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 29, 2, 1, 5, 1, 1, 3),
    _AlaDHCPv6SrvLeasePrefLeaseExpiry_Type()
)
alaDHCPv6SrvLeasePrefLeaseExpiry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaDHCPv6SrvLeasePrefLeaseExpiry.setStatus("current")
_AlaDHCPv6SrvLeaseValidLeaseExpiry_Type = DateAndTime
_AlaDHCPv6SrvLeaseValidLeaseExpiry_Object = MibTableColumn
alaDHCPv6SrvLeaseValidLeaseExpiry = _AlaDHCPv6SrvLeaseValidLeaseExpiry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 29, 2, 1, 5, 1, 1, 4),
    _AlaDHCPv6SrvLeaseValidLeaseExpiry_Type()
)
alaDHCPv6SrvLeaseValidLeaseExpiry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaDHCPv6SrvLeaseValidLeaseExpiry.setStatus("current")


class _AlaDHCPv6SrvLeaseType_Type(Integer32):
    """Custom type alaDHCPv6SrvLeaseType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("unavailable", 1),
          ("dynamic", 2),
          ("manual", 3))
    )


_AlaDHCPv6SrvLeaseType_Type.__name__ = "Integer32"
_AlaDHCPv6SrvLeaseType_Object = MibTableColumn
alaDHCPv6SrvLeaseType = _AlaDHCPv6SrvLeaseType_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 29, 2, 1, 5, 1, 1, 5),
    _AlaDHCPv6SrvLeaseType_Type()
)
alaDHCPv6SrvLeaseType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaDHCPv6SrvLeaseType.setStatus("current")
_AlaDHCPv6SrvTrapsObj_ObjectIdentity = ObjectIdentity
alaDHCPv6SrvTrapsObj = _AlaDHCPv6SrvTrapsObj_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 29, 2, 1, 6)
)


class _AlaDHCPv6SrvLeaseThresholdStatus_Type(Integer32):
    """Custom type alaDHCPv6SrvLeaseThresholdStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("crossedBelow80Threshold", 1),
          ("crossedAbove80Threshold", 2),
          ("reached100Threshold", 3))
    )


_AlaDHCPv6SrvLeaseThresholdStatus_Type.__name__ = "Integer32"
_AlaDHCPv6SrvLeaseThresholdStatus_Object = MibScalar
alaDHCPv6SrvLeaseThresholdStatus = _AlaDHCPv6SrvLeaseThresholdStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 29, 2, 1, 6, 1),
    _AlaDHCPv6SrvLeaseThresholdStatus_Type()
)
alaDHCPv6SrvLeaseThresholdStatus.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    alaDHCPv6SrvLeaseThresholdStatus.setStatus("current")
_AlaDHCPv6SrvSubnetDescriptor_Type = DisplayString
_AlaDHCPv6SrvSubnetDescriptor_Object = MibScalar
alaDHCPv6SrvSubnetDescriptor = _AlaDHCPv6SrvSubnetDescriptor_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 29, 2, 1, 6, 2),
    _AlaDHCPv6SrvSubnetDescriptor_Type()
)
alaDHCPv6SrvSubnetDescriptor.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    alaDHCPv6SrvSubnetDescriptor.setStatus("current")
_AlaDHCPv6GuardInterfaceTable_Object = MibTable
alaDHCPv6GuardInterfaceTable = _AlaDHCPv6GuardInterfaceTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 29, 2, 1, 7)
)
if mibBuilder.loadTexts:
    alaDHCPv6GuardInterfaceTable.setStatus("current")
_AlaDHCPv6GuardInterfaceEntry_Object = MibTableRow
alaDHCPv6GuardInterfaceEntry = _AlaDHCPv6GuardInterfaceEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 29, 2, 1, 7, 1)
)
alaDHCPv6GuardInterfaceEntry.setIndexNames(
    (0, "IPV6-MIB", "ipv6IfIndex"),
)
if mibBuilder.loadTexts:
    alaDHCPv6GuardInterfaceEntry.setStatus("current")


class _AlaDHCPv6GuardInterfaceAdminStatus_Type(Integer32):
    """Custom type alaDHCPv6GuardInterfaceAdminStatus based on Integer32"""
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


_AlaDHCPv6GuardInterfaceAdminStatus_Type.__name__ = "Integer32"
_AlaDHCPv6GuardInterfaceAdminStatus_Object = MibTableColumn
alaDHCPv6GuardInterfaceAdminStatus = _AlaDHCPv6GuardInterfaceAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 29, 2, 1, 7, 1, 1),
    _AlaDHCPv6GuardInterfaceAdminStatus_Type()
)
alaDHCPv6GuardInterfaceAdminStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaDHCPv6GuardInterfaceAdminStatus.setStatus("current")
_AlaDHCPv6GuardInterfaceRowStatus_Type = RowStatus
_AlaDHCPv6GuardInterfaceRowStatus_Object = MibTableColumn
alaDHCPv6GuardInterfaceRowStatus = _AlaDHCPv6GuardInterfaceRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 29, 2, 1, 7, 1, 2),
    _AlaDHCPv6GuardInterfaceRowStatus_Type()
)
alaDHCPv6GuardInterfaceRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaDHCPv6GuardInterfaceRowStatus.setStatus("current")


class _AlaDHCPv6GuardInterfaceClient_Type(Integer32):
    """Custom type alaDHCPv6GuardInterfaceClient based on Integer32"""
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


_AlaDHCPv6GuardInterfaceClient_Type.__name__ = "Integer32"
_AlaDHCPv6GuardInterfaceClient_Object = MibTableColumn
alaDHCPv6GuardInterfaceClient = _AlaDHCPv6GuardInterfaceClient_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 29, 2, 1, 7, 1, 3),
    _AlaDHCPv6GuardInterfaceClient_Type()
)
alaDHCPv6GuardInterfaceClient.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaDHCPv6GuardInterfaceClient.setStatus("current")


class _AlaDHCPv6GuardInterfaceLDRAAdminStatus_Type(Integer32):
    """Custom type alaDHCPv6GuardInterfaceLDRAAdminStatus based on Integer32"""
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


_AlaDHCPv6GuardInterfaceLDRAAdminStatus_Type.__name__ = "Integer32"
_AlaDHCPv6GuardInterfaceLDRAAdminStatus_Object = MibTableColumn
alaDHCPv6GuardInterfaceLDRAAdminStatus = _AlaDHCPv6GuardInterfaceLDRAAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 29, 2, 1, 7, 1, 4),
    _AlaDHCPv6GuardInterfaceLDRAAdminStatus_Type()
)
alaDHCPv6GuardInterfaceLDRAAdminStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaDHCPv6GuardInterfaceLDRAAdminStatus.setStatus("current")
_AlaDHCPv6GuardTrustedSourceTable_Object = MibTable
alaDHCPv6GuardTrustedSourceTable = _AlaDHCPv6GuardTrustedSourceTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 29, 2, 1, 8)
)
if mibBuilder.loadTexts:
    alaDHCPv6GuardTrustedSourceTable.setStatus("current")
_AlaDHCPv6GuardTrustedSourceEntry_Object = MibTableRow
alaDHCPv6GuardTrustedSourceEntry = _AlaDHCPv6GuardTrustedSourceEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 29, 2, 1, 8, 1)
)
alaDHCPv6GuardTrustedSourceEntry.setIndexNames(
    (0, "IPV6-MIB", "ipv6IfIndex"),
    (0, "ALCATEL-IND1-DHCPV6-MIB", "alaDHCPv6GuardTrustedSourceIfIndex"),
)
if mibBuilder.loadTexts:
    alaDHCPv6GuardTrustedSourceEntry.setStatus("current")
_AlaDHCPv6GuardTrustedSourceIfIndex_Type = AlaDHCPv6GuardTrustedSourceIfIndex
_AlaDHCPv6GuardTrustedSourceIfIndex_Object = MibTableColumn
alaDHCPv6GuardTrustedSourceIfIndex = _AlaDHCPv6GuardTrustedSourceIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 29, 2, 1, 8, 1, 1),
    _AlaDHCPv6GuardTrustedSourceIfIndex_Type()
)
alaDHCPv6GuardTrustedSourceIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaDHCPv6GuardTrustedSourceIfIndex.setStatus("current")
_AlaDHCPv6GuardTrustedSourceRowStatus_Type = RowStatus
_AlaDHCPv6GuardTrustedSourceRowStatus_Object = MibTableColumn
alaDHCPv6GuardTrustedSourceRowStatus = _AlaDHCPv6GuardTrustedSourceRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 29, 2, 1, 8, 1, 2),
    _AlaDHCPv6GuardTrustedSourceRowStatus_Type()
)
alaDHCPv6GuardTrustedSourceRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaDHCPv6GuardTrustedSourceRowStatus.setStatus("current")
_AlaDHCPv6SnoopingInterfaceTable_Object = MibTable
alaDHCPv6SnoopingInterfaceTable = _AlaDHCPv6SnoopingInterfaceTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 29, 2, 1, 9)
)
if mibBuilder.loadTexts:
    alaDHCPv6SnoopingInterfaceTable.setStatus("current")
_AlaDHCPv6SnoopingInterfaceEntry_Object = MibTableRow
alaDHCPv6SnoopingInterfaceEntry = _AlaDHCPv6SnoopingInterfaceEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 29, 2, 1, 9, 1)
)
alaDHCPv6SnoopingInterfaceEntry.setIndexNames(
    (0, "ALCATEL-IND1-DHCPV6-MIB", "alaDHCPv6SnoopingInterfaceIndex"),
)
if mibBuilder.loadTexts:
    alaDHCPv6SnoopingInterfaceEntry.setStatus("current")
_AlaDHCPv6SnoopingInterfaceIndex_Type = Ipv6IfIndexOrZero
_AlaDHCPv6SnoopingInterfaceIndex_Object = MibTableColumn
alaDHCPv6SnoopingInterfaceIndex = _AlaDHCPv6SnoopingInterfaceIndex_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 29, 2, 1, 9, 1, 1),
    _AlaDHCPv6SnoopingInterfaceIndex_Type()
)
alaDHCPv6SnoopingInterfaceIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaDHCPv6SnoopingInterfaceIndex.setStatus("current")


class _AlaDHCPv6SnoopingInterfaceAdminStatus_Type(Integer32):
    """Custom type alaDHCPv6SnoopingInterfaceAdminStatus based on Integer32"""
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


_AlaDHCPv6SnoopingInterfaceAdminStatus_Type.__name__ = "Integer32"
_AlaDHCPv6SnoopingInterfaceAdminStatus_Object = MibTableColumn
alaDHCPv6SnoopingInterfaceAdminStatus = _AlaDHCPv6SnoopingInterfaceAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 29, 2, 1, 9, 1, 2),
    _AlaDHCPv6SnoopingInterfaceAdminStatus_Type()
)
alaDHCPv6SnoopingInterfaceAdminStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaDHCPv6SnoopingInterfaceAdminStatus.setStatus("current")
_AlaDHCPv6SnoopingInterfaceRowStatus_Type = RowStatus
_AlaDHCPv6SnoopingInterfaceRowStatus_Object = MibTableColumn
alaDHCPv6SnoopingInterfaceRowStatus = _AlaDHCPv6SnoopingInterfaceRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 29, 2, 1, 9, 1, 3),
    _AlaDHCPv6SnoopingInterfaceRowStatus_Type()
)
alaDHCPv6SnoopingInterfaceRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaDHCPv6SnoopingInterfaceRowStatus.setStatus("current")
_AlaDHCPv6BindingConfig_ObjectIdentity = ObjectIdentity
alaDHCPv6BindingConfig = _AlaDHCPv6BindingConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 29, 2, 1, 10)
)


class _AlaDHCPv6BindingTimeout_Type(Unsigned32):
    """Custom type alaDHCPv6BindingTimeout based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 600),
    )


_AlaDHCPv6BindingTimeout_Type.__name__ = "Unsigned32"
_AlaDHCPv6BindingTimeout_Object = MibScalar
alaDHCPv6BindingTimeout = _AlaDHCPv6BindingTimeout_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 29, 2, 1, 10, 1),
    _AlaDHCPv6BindingTimeout_Type()
)
alaDHCPv6BindingTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaDHCPv6BindingTimeout.setStatus("current")
if mibBuilder.loadTexts:
    alaDHCPv6BindingTimeout.setUnits("seconds")


class _AlaDHCPv6BindingAction_Type(Integer32):
    """Custom type alaDHCPv6BindingAction based on Integer32"""
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
          ("purge", 1),
          ("renew", 2),
          ("save", 3))
    )


_AlaDHCPv6BindingAction_Type.__name__ = "Integer32"
_AlaDHCPv6BindingAction_Object = MibScalar
alaDHCPv6BindingAction = _AlaDHCPv6BindingAction_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 29, 2, 1, 10, 2),
    _AlaDHCPv6BindingAction_Type()
)
alaDHCPv6BindingAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaDHCPv6BindingAction.setStatus("current")


class _AlaDHCPv6BindingPersistency_Type(Integer32):
    """Custom type alaDHCPv6BindingPersistency based on Integer32"""
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


_AlaDHCPv6BindingPersistency_Type.__name__ = "Integer32"
_AlaDHCPv6BindingPersistency_Object = MibScalar
alaDHCPv6BindingPersistency = _AlaDHCPv6BindingPersistency_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 29, 2, 1, 10, 3),
    _AlaDHCPv6BindingPersistency_Type()
)
alaDHCPv6BindingPersistency.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaDHCPv6BindingPersistency.setStatus("current")
_AlaDHCPv6BindingTable_Object = MibTable
alaDHCPv6BindingTable = _AlaDHCPv6BindingTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 29, 2, 1, 11)
)
if mibBuilder.loadTexts:
    alaDHCPv6BindingTable.setStatus("current")
_AlaDHCPv6BindingEntry_Object = MibTableRow
alaDHCPv6BindingEntry = _AlaDHCPv6BindingEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 29, 2, 1, 11, 1)
)
alaDHCPv6BindingEntry.setIndexNames(
    (0, "ALCATEL-IND1-DHCPV6-MIB", "alaDHCPv6BindingInterfaceIndex"),
    (0, "ALCATEL-IND1-DHCPV6-MIB", "alaDHCPv6BindingLinkLocalAddress"),
)
if mibBuilder.loadTexts:
    alaDHCPv6BindingEntry.setStatus("current")
_AlaDHCPv6BindingInterfaceIndex_Type = Unsigned32
_AlaDHCPv6BindingInterfaceIndex_Object = MibTableColumn
alaDHCPv6BindingInterfaceIndex = _AlaDHCPv6BindingInterfaceIndex_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 29, 2, 1, 11, 1, 1),
    _AlaDHCPv6BindingInterfaceIndex_Type()
)
alaDHCPv6BindingInterfaceIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaDHCPv6BindingInterfaceIndex.setStatus("current")
_AlaDHCPv6BindingLinkLocalAddress_Type = Ipv6Address
_AlaDHCPv6BindingLinkLocalAddress_Object = MibTableColumn
alaDHCPv6BindingLinkLocalAddress = _AlaDHCPv6BindingLinkLocalAddress_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 29, 2, 1, 11, 1, 2),
    _AlaDHCPv6BindingLinkLocalAddress_Type()
)
alaDHCPv6BindingLinkLocalAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaDHCPv6BindingLinkLocalAddress.setStatus("current")
_AlaDHCPv6BindingPortIfIndex_Type = Unsigned32
_AlaDHCPv6BindingPortIfIndex_Object = MibTableColumn
alaDHCPv6BindingPortIfIndex = _AlaDHCPv6BindingPortIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 29, 2, 1, 11, 1, 3),
    _AlaDHCPv6BindingPortIfIndex_Type()
)
alaDHCPv6BindingPortIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaDHCPv6BindingPortIfIndex.setStatus("current")
_AlaDHCPv6BindingGlobalAddress_Type = Ipv6Address
_AlaDHCPv6BindingGlobalAddress_Object = MibTableColumn
alaDHCPv6BindingGlobalAddress = _AlaDHCPv6BindingGlobalAddress_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 29, 2, 1, 11, 1, 4),
    _AlaDHCPv6BindingGlobalAddress_Type()
)
alaDHCPv6BindingGlobalAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaDHCPv6BindingGlobalAddress.setStatus("current")


class _AlaDHCPv6BindingLeaseTime_Type(Integer32):
    """Custom type alaDHCPv6BindingLeaseTime based on Integer32"""
    defaultValue = -1


_AlaDHCPv6BindingLeaseTime_Type.__name__ = "Integer32"
_AlaDHCPv6BindingLeaseTime_Object = MibTableColumn
alaDHCPv6BindingLeaseTime = _AlaDHCPv6BindingLeaseTime_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 29, 2, 1, 11, 1, 5),
    _AlaDHCPv6BindingLeaseTime_Type()
)
alaDHCPv6BindingLeaseTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaDHCPv6BindingLeaseTime.setStatus("current")
_AlaDHCPv6BindingPhysAddress_Type = PhysAddress
_AlaDHCPv6BindingPhysAddress_Object = MibTableColumn
alaDHCPv6BindingPhysAddress = _AlaDHCPv6BindingPhysAddress_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 29, 2, 1, 11, 1, 6),
    _AlaDHCPv6BindingPhysAddress_Type()
)
alaDHCPv6BindingPhysAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaDHCPv6BindingPhysAddress.setStatus("current")


class _AlaDHCPv6BindingType_Type(Integer32):
    """Custom type alaDHCPv6BindingType based on Integer32"""
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


_AlaDHCPv6BindingType_Type.__name__ = "Integer32"
_AlaDHCPv6BindingType_Object = MibTableColumn
alaDHCPv6BindingType = _AlaDHCPv6BindingType_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 29, 2, 1, 11, 1, 7),
    _AlaDHCPv6BindingType_Type()
)
alaDHCPv6BindingType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaDHCPv6BindingType.setStatus("current")
_AlaDHCPv6BindingRowStatus_Type = RowStatus
_AlaDHCPv6BindingRowStatus_Object = MibTableColumn
alaDHCPv6BindingRowStatus = _AlaDHCPv6BindingRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 29, 2, 1, 11, 1, 8),
    _AlaDHCPv6BindingRowStatus_Type()
)
alaDHCPv6BindingRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaDHCPv6BindingRowStatus.setStatus("current")
_AlaDHCPv6SourceFilterInterfaceTable_Object = MibTable
alaDHCPv6SourceFilterInterfaceTable = _AlaDHCPv6SourceFilterInterfaceTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 29, 2, 1, 12)
)
if mibBuilder.loadTexts:
    alaDHCPv6SourceFilterInterfaceTable.setStatus("current")
_AlaDHCPv6SourceFilterInterfaceEntry_Object = MibTableRow
alaDHCPv6SourceFilterInterfaceEntry = _AlaDHCPv6SourceFilterInterfaceEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 29, 2, 1, 12, 1)
)
alaDHCPv6SourceFilterInterfaceEntry.setIndexNames(
    (0, "ALCATEL-IND1-DHCPV6-MIB", "alaDHCPv6SourceFilterInterfaceIndex"),
)
if mibBuilder.loadTexts:
    alaDHCPv6SourceFilterInterfaceEntry.setStatus("current")
_AlaDHCPv6SourceFilterInterfaceIndex_Type = Unsigned32
_AlaDHCPv6SourceFilterInterfaceIndex_Object = MibTableColumn
alaDHCPv6SourceFilterInterfaceIndex = _AlaDHCPv6SourceFilterInterfaceIndex_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 29, 2, 1, 12, 1, 1),
    _AlaDHCPv6SourceFilterInterfaceIndex_Type()
)
alaDHCPv6SourceFilterInterfaceIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaDHCPv6SourceFilterInterfaceIndex.setStatus("current")
_AlaDHCPv6SourceFilterInterfaceRowStatus_Type = RowStatus
_AlaDHCPv6SourceFilterInterfaceRowStatus_Object = MibTableColumn
alaDHCPv6SourceFilterInterfaceRowStatus = _AlaDHCPv6SourceFilterInterfaceRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 29, 2, 1, 12, 1, 2),
    _AlaDHCPv6SourceFilterInterfaceRowStatus_Type()
)
alaDHCPv6SourceFilterInterfaceRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaDHCPv6SourceFilterInterfaceRowStatus.setStatus("current")
_AlaDHCPv6SourceFilterPortTable_Object = MibTable
alaDHCPv6SourceFilterPortTable = _AlaDHCPv6SourceFilterPortTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 29, 2, 1, 13)
)
if mibBuilder.loadTexts:
    alaDHCPv6SourceFilterPortTable.setStatus("current")
_AlaDHCPv6SourceFilterPortEntry_Object = MibTableRow
alaDHCPv6SourceFilterPortEntry = _AlaDHCPv6SourceFilterPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 29, 2, 1, 13, 1)
)
alaDHCPv6SourceFilterPortEntry.setIndexNames(
    (0, "ALCATEL-IND1-DHCPV6-MIB", "alaDHCPv6SourceFilterPortIndex"),
)
if mibBuilder.loadTexts:
    alaDHCPv6SourceFilterPortEntry.setStatus("current")
_AlaDHCPv6SourceFilterPortIndex_Type = Unsigned32
_AlaDHCPv6SourceFilterPortIndex_Object = MibTableColumn
alaDHCPv6SourceFilterPortIndex = _AlaDHCPv6SourceFilterPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 29, 2, 1, 13, 1, 1),
    _AlaDHCPv6SourceFilterPortIndex_Type()
)
alaDHCPv6SourceFilterPortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaDHCPv6SourceFilterPortIndex.setStatus("current")
_AlaDHCPv6SourceFilterPortRowStatus_Type = RowStatus
_AlaDHCPv6SourceFilterPortRowStatus_Object = MibTableColumn
alaDHCPv6SourceFilterPortRowStatus = _AlaDHCPv6SourceFilterPortRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 29, 2, 1, 13, 1, 2),
    _AlaDHCPv6SourceFilterPortRowStatus_Type()
)
alaDHCPv6SourceFilterPortRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaDHCPv6SourceFilterPortRowStatus.setStatus("current")
_AlaDhcpv6IsfTrapsObj_ObjectIdentity = ObjectIdentity
alaDhcpv6IsfTrapsObj = _AlaDhcpv6IsfTrapsObj_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 29, 2, 1, 14)
)


class _AlaDhcpv6IsfTcamFailMsg_Type(SnmpAdminString):
    """Custom type alaDhcpv6IsfTcamFailMsg based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_AlaDhcpv6IsfTcamFailMsg_Type.__name__ = "SnmpAdminString"
_AlaDhcpv6IsfTcamFailMsg_Object = MibScalar
alaDhcpv6IsfTcamFailMsg = _AlaDhcpv6IsfTcamFailMsg_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 29, 2, 1, 14, 1),
    _AlaDhcpv6IsfTcamFailMsg_Type()
)
alaDhcpv6IsfTcamFailMsg.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    alaDhcpv6IsfTcamFailMsg.setStatus("current")
_AlaDHCPv6SnoopingSourceFilter_ObjectIdentity = ObjectIdentity
alaDHCPv6SnoopingSourceFilter = _AlaDHCPv6SnoopingSourceFilter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 29, 2, 1, 15)
)


class _AlaDHCPv6SnoopingSourceFilterAdminState_Type(Integer32):
    """Custom type alaDHCPv6SnoopingSourceFilterAdminState based on Integer32"""
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


_AlaDHCPv6SnoopingSourceFilterAdminState_Type.__name__ = "Integer32"
_AlaDHCPv6SnoopingSourceFilterAdminState_Object = MibScalar
alaDHCPv6SnoopingSourceFilterAdminState = _AlaDHCPv6SnoopingSourceFilterAdminState_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 29, 2, 1, 15, 1),
    _AlaDHCPv6SnoopingSourceFilterAdminState_Type()
)
alaDHCPv6SnoopingSourceFilterAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaDHCPv6SnoopingSourceFilterAdminState.setStatus("current")
_AlaDHCPv6SrvStats_ObjectIdentity = ObjectIdentity
alaDHCPv6SrvStats = _AlaDHCPv6SrvStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 29, 2, 1, 16)
)


class _AlaDHCPv6SrvStatsServerName_Type(SnmpAdminString):
    """Custom type alaDHCPv6SrvStatsServerName based on SnmpAdminString"""
    defaultValue = OctetString("")

    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_AlaDHCPv6SrvStatsServerName_Type.__name__ = "SnmpAdminString"
_AlaDHCPv6SrvStatsServerName_Object = MibScalar
alaDHCPv6SrvStatsServerName = _AlaDHCPv6SrvStatsServerName_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 29, 2, 1, 16, 1),
    _AlaDHCPv6SrvStatsServerName_Type()
)
alaDHCPv6SrvStatsServerName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaDHCPv6SrvStatsServerName.setStatus("current")


class _AlaDHCPv6SrvStatsServerStatus_Type(Integer32):
    """Custom type alaDHCPv6SrvStatsServerStatus based on Integer32"""
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


_AlaDHCPv6SrvStatsServerStatus_Type.__name__ = "Integer32"
_AlaDHCPv6SrvStatsServerStatus_Object = MibScalar
alaDHCPv6SrvStatsServerStatus = _AlaDHCPv6SrvStatsServerStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 29, 2, 1, 16, 2),
    _AlaDHCPv6SrvStatsServerStatus_Type()
)
alaDHCPv6SrvStatsServerStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaDHCPv6SrvStatsServerStatus.setStatus("current")
_AlaDHCPv6SrvStatsTotalSubnetsManaged_Type = Integer32
_AlaDHCPv6SrvStatsTotalSubnetsManaged_Object = MibScalar
alaDHCPv6SrvStatsTotalSubnetsManaged = _AlaDHCPv6SrvStatsTotalSubnetsManaged_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 29, 2, 1, 16, 3),
    _AlaDHCPv6SrvStatsTotalSubnetsManaged_Type()
)
alaDHCPv6SrvStatsTotalSubnetsManaged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaDHCPv6SrvStatsTotalSubnetsManaged.setStatus("current")
_AlaDHCPv6SrvStatsTotalSubnetsUsed_Type = Integer32
_AlaDHCPv6SrvStatsTotalSubnetsUsed_Object = MibScalar
alaDHCPv6SrvStatsTotalSubnetsUsed = _AlaDHCPv6SrvStatsTotalSubnetsUsed_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 29, 2, 1, 16, 4),
    _AlaDHCPv6SrvStatsTotalSubnetsUsed_Type()
)
alaDHCPv6SrvStatsTotalSubnetsUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaDHCPv6SrvStatsTotalSubnetsUsed.setStatus("current")
_AlaDHCPv6SrvStatsTotalSubnetsUnused_Type = Integer32
_AlaDHCPv6SrvStatsTotalSubnetsUnused_Object = MibScalar
alaDHCPv6SrvStatsTotalSubnetsUnused = _AlaDHCPv6SrvStatsTotalSubnetsUnused_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 29, 2, 1, 16, 5),
    _AlaDHCPv6SrvStatsTotalSubnetsUnused_Type()
)
alaDHCPv6SrvStatsTotalSubnetsUnused.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaDHCPv6SrvStatsTotalSubnetsUnused.setStatus("current")
_AlaDHCPv6SrvStatsTotalSubnetsFull_Type = Integer32
_AlaDHCPv6SrvStatsTotalSubnetsFull_Object = MibScalar
alaDHCPv6SrvStatsTotalSubnetsFull = _AlaDHCPv6SrvStatsTotalSubnetsFull_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 29, 2, 1, 16, 6),
    _AlaDHCPv6SrvStatsTotalSubnetsFull_Type()
)
alaDHCPv6SrvStatsTotalSubnetsFull.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaDHCPv6SrvStatsTotalSubnetsFull.setStatus("current")


class _AlaDHCPv6SrvStatsServerUpTime_Type(TimeTicks):
    """Custom type alaDHCPv6SrvStatsServerUpTime based on TimeTicks"""
    defaultValue = 0


_AlaDHCPv6SrvStatsServerUpTime_Type.__name__ = "TimeTicks"
_AlaDHCPv6SrvStatsServerUpTime_Object = MibScalar
alaDHCPv6SrvStatsServerUpTime = _AlaDHCPv6SrvStatsServerUpTime_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 29, 2, 1, 16, 7),
    _AlaDHCPv6SrvStatsServerUpTime_Type()
)
alaDHCPv6SrvStatsServerUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaDHCPv6SrvStatsServerUpTime.setStatus("current")
_AlaDHCPv6SrvStatsLeaseDbSyncTime_Type = Integer32
_AlaDHCPv6SrvStatsLeaseDbSyncTime_Object = MibScalar
alaDHCPv6SrvStatsLeaseDbSyncTime = _AlaDHCPv6SrvStatsLeaseDbSyncTime_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 29, 2, 1, 16, 8),
    _AlaDHCPv6SrvStatsLeaseDbSyncTime_Type()
)
alaDHCPv6SrvStatsLeaseDbSyncTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaDHCPv6SrvStatsLeaseDbSyncTime.setStatus("current")
_AlaDHCPv6SrvStatsLastSyncTime_Type = DateAndTime
_AlaDHCPv6SrvStatsLastSyncTime_Object = MibScalar
alaDHCPv6SrvStatsLastSyncTime = _AlaDHCPv6SrvStatsLastSyncTime_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 29, 2, 1, 16, 9),
    _AlaDHCPv6SrvStatsLastSyncTime_Type()
)
alaDHCPv6SrvStatsLastSyncTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaDHCPv6SrvStatsLastSyncTime.setStatus("current")
_AlaDHCPv6SrvStatsNextSyncTime_Type = DateAndTime
_AlaDHCPv6SrvStatsNextSyncTime_Object = MibScalar
alaDHCPv6SrvStatsNextSyncTime = _AlaDHCPv6SrvStatsNextSyncTime_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 29, 2, 1, 16, 10),
    _AlaDHCPv6SrvStatsNextSyncTime_Type()
)
alaDHCPv6SrvStatsNextSyncTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaDHCPv6SrvStatsNextSyncTime.setStatus("current")
_AlaDHCPv6GuardServiceTable_Object = MibTable
alaDHCPv6GuardServiceTable = _AlaDHCPv6GuardServiceTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 29, 2, 1, 17)
)
if mibBuilder.loadTexts:
    alaDHCPv6GuardServiceTable.setStatus("current")
_AlaDHCPv6GuardServiceEntry_Object = MibTableRow
alaDHCPv6GuardServiceEntry = _AlaDHCPv6GuardServiceEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 29, 2, 1, 17, 1)
)
alaDHCPv6GuardServiceEntry.setIndexNames(
    (0, "ALCATEL-IND1-DHCPV6-MIB", "alaDHCPv6GuardServiceId"),
)
if mibBuilder.loadTexts:
    alaDHCPv6GuardServiceEntry.setStatus("current")
_AlaDHCPv6GuardServiceId_Type = Unsigned32
_AlaDHCPv6GuardServiceId_Object = MibTableColumn
alaDHCPv6GuardServiceId = _AlaDHCPv6GuardServiceId_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 29, 2, 1, 17, 1, 1),
    _AlaDHCPv6GuardServiceId_Type()
)
alaDHCPv6GuardServiceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaDHCPv6GuardServiceId.setStatus("current")


class _AlaDHCPv6GuardServiceAdminStatus_Type(Integer32):
    """Custom type alaDHCPv6GuardServiceAdminStatus based on Integer32"""
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


_AlaDHCPv6GuardServiceAdminStatus_Type.__name__ = "Integer32"
_AlaDHCPv6GuardServiceAdminStatus_Object = MibTableColumn
alaDHCPv6GuardServiceAdminStatus = _AlaDHCPv6GuardServiceAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 29, 2, 1, 17, 1, 2),
    _AlaDHCPv6GuardServiceAdminStatus_Type()
)
alaDHCPv6GuardServiceAdminStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaDHCPv6GuardServiceAdminStatus.setStatus("current")


class _AlaDHCPv6GuardServiceClient_Type(Integer32):
    """Custom type alaDHCPv6GuardServiceClient based on Integer32"""
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


_AlaDHCPv6GuardServiceClient_Type.__name__ = "Integer32"
_AlaDHCPv6GuardServiceClient_Object = MibTableColumn
alaDHCPv6GuardServiceClient = _AlaDHCPv6GuardServiceClient_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 29, 2, 1, 17, 1, 3),
    _AlaDHCPv6GuardServiceClient_Type()
)
alaDHCPv6GuardServiceClient.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaDHCPv6GuardServiceClient.setStatus("current")
_AlaDHCPv6GuardServiceRowStatus_Type = RowStatus
_AlaDHCPv6GuardServiceRowStatus_Object = MibTableColumn
alaDHCPv6GuardServiceRowStatus = _AlaDHCPv6GuardServiceRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 29, 2, 1, 17, 1, 4),
    _AlaDHCPv6GuardServiceRowStatus_Type()
)
alaDHCPv6GuardServiceRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaDHCPv6GuardServiceRowStatus.setStatus("current")
_AlaDHCPv6SnoopingServiceTable_Object = MibTable
alaDHCPv6SnoopingServiceTable = _AlaDHCPv6SnoopingServiceTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 29, 2, 1, 18)
)
if mibBuilder.loadTexts:
    alaDHCPv6SnoopingServiceTable.setStatus("current")
_AlaDHCPv6SnoopingServiceEntry_Object = MibTableRow
alaDHCPv6SnoopingServiceEntry = _AlaDHCPv6SnoopingServiceEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 29, 2, 1, 18, 1)
)
alaDHCPv6SnoopingServiceEntry.setIndexNames(
    (0, "ALCATEL-IND1-DHCPV6-MIB", "alaDHCPv6SnoopingServiceId"),
)
if mibBuilder.loadTexts:
    alaDHCPv6SnoopingServiceEntry.setStatus("current")
_AlaDHCPv6SnoopingServiceId_Type = Unsigned32
_AlaDHCPv6SnoopingServiceId_Object = MibTableColumn
alaDHCPv6SnoopingServiceId = _AlaDHCPv6SnoopingServiceId_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 29, 2, 1, 18, 1, 1),
    _AlaDHCPv6SnoopingServiceId_Type()
)
alaDHCPv6SnoopingServiceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaDHCPv6SnoopingServiceId.setStatus("current")


class _AlaDHCPv6SnoopingServiceAdminStatus_Type(Integer32):
    """Custom type alaDHCPv6SnoopingServiceAdminStatus based on Integer32"""
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


_AlaDHCPv6SnoopingServiceAdminStatus_Type.__name__ = "Integer32"
_AlaDHCPv6SnoopingServiceAdminStatus_Object = MibTableColumn
alaDHCPv6SnoopingServiceAdminStatus = _AlaDHCPv6SnoopingServiceAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 29, 2, 1, 18, 1, 2),
    _AlaDHCPv6SnoopingServiceAdminStatus_Type()
)
alaDHCPv6SnoopingServiceAdminStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaDHCPv6SnoopingServiceAdminStatus.setStatus("current")
_AlaDHCPv6SnoopingServiceRowStatus_Type = RowStatus
_AlaDHCPv6SnoopingServiceRowStatus_Object = MibTableColumn
alaDHCPv6SnoopingServiceRowStatus = _AlaDHCPv6SnoopingServiceRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 29, 2, 1, 18, 1, 3),
    _AlaDHCPv6SnoopingServiceRowStatus_Type()
)
alaDHCPv6SnoopingServiceRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaDHCPv6SnoopingServiceRowStatus.setStatus("current")
_AlaDHCPv6BindingServiceTable_Object = MibTable
alaDHCPv6BindingServiceTable = _AlaDHCPv6BindingServiceTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 29, 2, 1, 19)
)
if mibBuilder.loadTexts:
    alaDHCPv6BindingServiceTable.setStatus("current")
_AlaDHCPv6BindingServiceEntry_Object = MibTableRow
alaDHCPv6BindingServiceEntry = _AlaDHCPv6BindingServiceEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 29, 2, 1, 19, 1)
)
alaDHCPv6BindingServiceEntry.setIndexNames(
    (0, "ALCATEL-IND1-DHCPV6-MIB", "alaDHCPv6BindingServiceId"),
    (0, "ALCATEL-IND1-DHCPV6-MIB", "alaDHCPv6BindingServiceLinkLocalAddressType"),
    (0, "ALCATEL-IND1-DHCPV6-MIB", "alaDHCPv6BindingServiceLinkLocalAddress"),
)
if mibBuilder.loadTexts:
    alaDHCPv6BindingServiceEntry.setStatus("current")
_AlaDHCPv6BindingServiceId_Type = Unsigned32
_AlaDHCPv6BindingServiceId_Object = MibTableColumn
alaDHCPv6BindingServiceId = _AlaDHCPv6BindingServiceId_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 29, 2, 1, 19, 1, 1),
    _AlaDHCPv6BindingServiceId_Type()
)
alaDHCPv6BindingServiceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaDHCPv6BindingServiceId.setStatus("current")


class _AlaDHCPv6BindingServiceLinkLocalAddressType_Type(InetAddressType):
    """Custom type alaDHCPv6BindingServiceLinkLocalAddressType based on InetAddressType"""
    subtypeSpec = InetAddressType.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            2
        )
    )
    namedValues = NamedValues(
        ("ipv6", 2)
    )


_AlaDHCPv6BindingServiceLinkLocalAddressType_Type.__name__ = "InetAddressType"
_AlaDHCPv6BindingServiceLinkLocalAddressType_Object = MibTableColumn
alaDHCPv6BindingServiceLinkLocalAddressType = _AlaDHCPv6BindingServiceLinkLocalAddressType_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 29, 2, 1, 19, 1, 2),
    _AlaDHCPv6BindingServiceLinkLocalAddressType_Type()
)
alaDHCPv6BindingServiceLinkLocalAddressType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaDHCPv6BindingServiceLinkLocalAddressType.setStatus("current")
_AlaDHCPv6BindingServiceLinkLocalAddress_Type = InetAddress
_AlaDHCPv6BindingServiceLinkLocalAddress_Object = MibTableColumn
alaDHCPv6BindingServiceLinkLocalAddress = _AlaDHCPv6BindingServiceLinkLocalAddress_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 29, 2, 1, 19, 1, 3),
    _AlaDHCPv6BindingServiceLinkLocalAddress_Type()
)
alaDHCPv6BindingServiceLinkLocalAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaDHCPv6BindingServiceLinkLocalAddress.setStatus("current")
_AlaDHCPv6BindingServicePortIfIndex_Type = Unsigned32
_AlaDHCPv6BindingServicePortIfIndex_Object = MibTableColumn
alaDHCPv6BindingServicePortIfIndex = _AlaDHCPv6BindingServicePortIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 29, 2, 1, 19, 1, 4),
    _AlaDHCPv6BindingServicePortIfIndex_Type()
)
alaDHCPv6BindingServicePortIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaDHCPv6BindingServicePortIfIndex.setStatus("current")
_AlaDHCPv6BindingServiceEncapVal_Type = Unsigned32
_AlaDHCPv6BindingServiceEncapVal_Object = MibTableColumn
alaDHCPv6BindingServiceEncapVal = _AlaDHCPv6BindingServiceEncapVal_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 29, 2, 1, 19, 1, 5),
    _AlaDHCPv6BindingServiceEncapVal_Type()
)
alaDHCPv6BindingServiceEncapVal.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaDHCPv6BindingServiceEncapVal.setStatus("current")


class _AlaDHCPv6BindingServiceGlobalAddressType_Type(InetAddressType):
    """Custom type alaDHCPv6BindingServiceGlobalAddressType based on InetAddressType"""
    subtypeSpec = InetAddressType.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            2
        )
    )
    namedValues = NamedValues(
        ("ipv6", 2)
    )


_AlaDHCPv6BindingServiceGlobalAddressType_Type.__name__ = "InetAddressType"
_AlaDHCPv6BindingServiceGlobalAddressType_Object = MibTableColumn
alaDHCPv6BindingServiceGlobalAddressType = _AlaDHCPv6BindingServiceGlobalAddressType_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 29, 2, 1, 19, 1, 6),
    _AlaDHCPv6BindingServiceGlobalAddressType_Type()
)
alaDHCPv6BindingServiceGlobalAddressType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaDHCPv6BindingServiceGlobalAddressType.setStatus("current")
_AlaDHCPv6BindingServiceGlobalAddress_Type = InetAddress
_AlaDHCPv6BindingServiceGlobalAddress_Object = MibTableColumn
alaDHCPv6BindingServiceGlobalAddress = _AlaDHCPv6BindingServiceGlobalAddress_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 29, 2, 1, 19, 1, 7),
    _AlaDHCPv6BindingServiceGlobalAddress_Type()
)
alaDHCPv6BindingServiceGlobalAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaDHCPv6BindingServiceGlobalAddress.setStatus("current")


class _AlaDHCPv6BindingServiceLeaseTime_Type(Integer32):
    """Custom type alaDHCPv6BindingServiceLeaseTime based on Integer32"""
    defaultValue = -1


_AlaDHCPv6BindingServiceLeaseTime_Type.__name__ = "Integer32"
_AlaDHCPv6BindingServiceLeaseTime_Object = MibTableColumn
alaDHCPv6BindingServiceLeaseTime = _AlaDHCPv6BindingServiceLeaseTime_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 29, 2, 1, 19, 1, 8),
    _AlaDHCPv6BindingServiceLeaseTime_Type()
)
alaDHCPv6BindingServiceLeaseTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaDHCPv6BindingServiceLeaseTime.setStatus("current")
_AlaDHCPv6BindingServicePhysAddress_Type = PhysAddress
_AlaDHCPv6BindingServicePhysAddress_Object = MibTableColumn
alaDHCPv6BindingServicePhysAddress = _AlaDHCPv6BindingServicePhysAddress_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 29, 2, 1, 19, 1, 9),
    _AlaDHCPv6BindingServicePhysAddress_Type()
)
alaDHCPv6BindingServicePhysAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaDHCPv6BindingServicePhysAddress.setStatus("current")


class _AlaDHCPv6BindingServiceType_Type(Integer32):
    """Custom type alaDHCPv6BindingServiceType based on Integer32"""
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


_AlaDHCPv6BindingServiceType_Type.__name__ = "Integer32"
_AlaDHCPv6BindingServiceType_Object = MibTableColumn
alaDHCPv6BindingServiceType = _AlaDHCPv6BindingServiceType_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 29, 2, 1, 19, 1, 10),
    _AlaDHCPv6BindingServiceType_Type()
)
alaDHCPv6BindingServiceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaDHCPv6BindingServiceType.setStatus("current")
_AlaDHCPv6BindingServiceRowStatus_Type = RowStatus
_AlaDHCPv6BindingServiceRowStatus_Object = MibTableColumn
alaDHCPv6BindingServiceRowStatus = _AlaDHCPv6BindingServiceRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 29, 2, 1, 19, 1, 11),
    _AlaDHCPv6BindingServiceRowStatus_Type()
)
alaDHCPv6BindingServiceRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaDHCPv6BindingServiceRowStatus.setStatus("current")
_AlaDHCPv6GuardServiceTrustSourceTable_Object = MibTable
alaDHCPv6GuardServiceTrustSourceTable = _AlaDHCPv6GuardServiceTrustSourceTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 29, 2, 1, 20)
)
if mibBuilder.loadTexts:
    alaDHCPv6GuardServiceTrustSourceTable.setStatus("current")
_AlaDHCPv6GuardServiceTrustSourceEntry_Object = MibTableRow
alaDHCPv6GuardServiceTrustSourceEntry = _AlaDHCPv6GuardServiceTrustSourceEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 29, 2, 1, 20, 1)
)
alaDHCPv6GuardServiceTrustSourceEntry.setIndexNames(
    (0, "ALCATEL-IND1-DHCPV6-MIB", "alaDHCPv6GuardServiceTrustSourceServiceId"),
    (0, "ALCATEL-IND1-DHCPV6-MIB", "alaDHCPv6GuardServiceTrustSourceSdpId"),
)
if mibBuilder.loadTexts:
    alaDHCPv6GuardServiceTrustSourceEntry.setStatus("current")
_AlaDHCPv6GuardServiceTrustSourceServiceId_Type = Unsigned32
_AlaDHCPv6GuardServiceTrustSourceServiceId_Object = MibTableColumn
alaDHCPv6GuardServiceTrustSourceServiceId = _AlaDHCPv6GuardServiceTrustSourceServiceId_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 29, 2, 1, 20, 1, 1),
    _AlaDHCPv6GuardServiceTrustSourceServiceId_Type()
)
alaDHCPv6GuardServiceTrustSourceServiceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaDHCPv6GuardServiceTrustSourceServiceId.setStatus("current")
_AlaDHCPv6GuardServiceTrustSourceSdpId_Type = Unsigned32
_AlaDHCPv6GuardServiceTrustSourceSdpId_Object = MibTableColumn
alaDHCPv6GuardServiceTrustSourceSdpId = _AlaDHCPv6GuardServiceTrustSourceSdpId_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 29, 2, 1, 20, 1, 2),
    _AlaDHCPv6GuardServiceTrustSourceSdpId_Type()
)
alaDHCPv6GuardServiceTrustSourceSdpId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaDHCPv6GuardServiceTrustSourceSdpId.setStatus("current")


class _AlaDHCPv6GuardServiceTrustSourceType_Type(Integer32):
    """Custom type alaDHCPv6GuardServiceTrustSourceType based on Integer32"""
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


_AlaDHCPv6GuardServiceTrustSourceType_Type.__name__ = "Integer32"
_AlaDHCPv6GuardServiceTrustSourceType_Object = MibTableColumn
alaDHCPv6GuardServiceTrustSourceType = _AlaDHCPv6GuardServiceTrustSourceType_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 29, 2, 1, 20, 1, 3),
    _AlaDHCPv6GuardServiceTrustSourceType_Type()
)
alaDHCPv6GuardServiceTrustSourceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaDHCPv6GuardServiceTrustSourceType.setStatus("current")
_AlaDHCPv6SourceFilterServiceTable_Object = MibTable
alaDHCPv6SourceFilterServiceTable = _AlaDHCPv6SourceFilterServiceTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 29, 2, 1, 21)
)
if mibBuilder.loadTexts:
    alaDHCPv6SourceFilterServiceTable.setStatus("current")
_AlaDHCPv6SourceFilterServiceEntry_Object = MibTableRow
alaDHCPv6SourceFilterServiceEntry = _AlaDHCPv6SourceFilterServiceEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 29, 2, 1, 21, 1)
)
alaDHCPv6SourceFilterServiceEntry.setIndexNames(
    (0, "ALCATEL-IND1-DHCPV6-MIB", "alaDHCPv6SourceFilterServiceIndex"),
)
if mibBuilder.loadTexts:
    alaDHCPv6SourceFilterServiceEntry.setStatus("current")
_AlaDHCPv6SourceFilterServiceIndex_Type = Unsigned32
_AlaDHCPv6SourceFilterServiceIndex_Object = MibTableColumn
alaDHCPv6SourceFilterServiceIndex = _AlaDHCPv6SourceFilterServiceIndex_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 29, 2, 1, 21, 1, 1),
    _AlaDHCPv6SourceFilterServiceIndex_Type()
)
alaDHCPv6SourceFilterServiceIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaDHCPv6SourceFilterServiceIndex.setStatus("current")
_AlaDHCPv6SourceFilterServiceRowStatus_Type = RowStatus
_AlaDHCPv6SourceFilterServiceRowStatus_Object = MibTableColumn
alaDHCPv6SourceFilterServiceRowStatus = _AlaDHCPv6SourceFilterServiceRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 29, 2, 1, 21, 1, 2),
    _AlaDHCPv6SourceFilterServiceRowStatus_Type()
)
alaDHCPv6SourceFilterServiceRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaDHCPv6SourceFilterServiceRowStatus.setStatus("current")
_AlcatelIND1DHCPv6MIBConformance_ObjectIdentity = ObjectIdentity
alcatelIND1DHCPv6MIBConformance = _AlcatelIND1DHCPv6MIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 29, 2, 2)
)
_AlcatelIND1DHCPv6MIBCompliances_ObjectIdentity = ObjectIdentity
alcatelIND1DHCPv6MIBCompliances = _AlcatelIND1DHCPv6MIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 29, 2, 2, 1)
)
_AlcatelIND1DHCPv6MIBGroups_ObjectIdentity = ObjectIdentity
alcatelIND1DHCPv6MIBGroups = _AlcatelIND1DHCPv6MIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 29, 2, 2, 2)
)

# Managed Objects groups

alaDHCPv6RelayGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 29, 2, 2, 2, 1)
)
alaDHCPv6RelayGroup.setObjects(
      *(("ALCATEL-IND1-DHCPV6-MIB", "alaDHCPv6RelayAdminStatus"),
        ("ALCATEL-IND1-DHCPV6-MIB", "alaDHCPv6RelayInterfaceAdminStatus"),
        ("ALCATEL-IND1-DHCPV6-MIB", "alaDHCPv6RelayDestinationRowStatus"),
        ("ALCATEL-IND1-DHCPV6-MIB", "alaDHCPv6RelayMaximumHops"),
        ("ALCATEL-IND1-DHCPV6-MIB", "alaDHCPv6RelayInterfaceIDStatus"),
        ("ALCATEL-IND1-DHCPV6-MIB", "alaDHCPv6RelayInterfaceIDPrefix"),
        ("ALCATEL-IND1-DHCPV6-MIB", "alaDHCPv6RelayRemoteIDStatus"),
        ("ALCATEL-IND1-DHCPV6-MIB", "alaDHCPv6RelayRemoteIDFormatType"),
        ("ALCATEL-IND1-DHCPV6-MIB", "alaDHCPv6RelayRemoteIDStringValue"),
        ("ALCATEL-IND1-DHCPV6-MIB", "alaDHCPv6RelayRemoteIDEnterpriseNumber"))
)
if mibBuilder.loadTexts:
    alaDHCPv6RelayGroup.setStatus("current")

alaDHCPv6SrvGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 29, 2, 2, 2, 2)
)
alaDHCPv6SrvGroup.setObjects(
      *(("ALCATEL-IND1-DHCPV6-MIB", "alaDHCPv6SrvGlobalConfigStatus"),
        ("ALCATEL-IND1-DHCPV6-MIB", "alaDHCPv6SrvGlobalRestart"),
        ("ALCATEL-IND1-DHCPV6-MIB", "alaDHCPv6SrvGlobalClearStat"),
        ("ALCATEL-IND1-DHCPV6-MIB", "alaDHCPv6SrvLeaseLeaseGrant"),
        ("ALCATEL-IND1-DHCPV6-MIB", "alaDHCPv6SrvLeasePrefLeaseExpiry"),
        ("ALCATEL-IND1-DHCPV6-MIB", "alaDHCPv6SrvLeaseValidLeaseExpiry"),
        ("ALCATEL-IND1-DHCPV6-MIB", "alaDHCPv6SrvLeaseType"))
)
if mibBuilder.loadTexts:
    alaDHCPv6SrvGroup.setStatus("current")

alaDHCPv6SrvLeaseUtilizationThresholdGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 29, 2, 2, 2, 4)
)
alaDHCPv6SrvLeaseUtilizationThresholdGroup.setObjects(
      *(("ALCATEL-IND1-DHCPV6-MIB", "alaDHCPv6SrvLeaseThresholdStatus"),
        ("ALCATEL-IND1-DHCPV6-MIB", "alaDHCPv6SrvSubnetDescriptor"))
)
if mibBuilder.loadTexts:
    alaDHCPv6SrvLeaseUtilizationThresholdGroup.setStatus("current")

alaDHCPv6GuardInterfaceGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 29, 2, 2, 2, 5)
)
alaDHCPv6GuardInterfaceGroup.setObjects(
      *(("ALCATEL-IND1-DHCPV6-MIB", "alaDHCPv6GuardInterfaceAdminStatus"),
        ("ALCATEL-IND1-DHCPV6-MIB", "alaDHCPv6GuardInterfaceRowStatus"),
        ("ALCATEL-IND1-DHCPV6-MIB", "alaDHCPv6GuardInterfaceClient"),
        ("ALCATEL-IND1-DHCPV6-MIB", "alaDHCPv6GuardInterfaceLDRAAdminStatus"))
)
if mibBuilder.loadTexts:
    alaDHCPv6GuardInterfaceGroup.setStatus("current")

alaDHCPv6GuardTrustedGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 29, 2, 2, 2, 6)
)
alaDHCPv6GuardTrustedGroup.setObjects(
    ("ALCATEL-IND1-DHCPV6-MIB", "alaDHCPv6GuardTrustedSourceRowStatus")
)
if mibBuilder.loadTexts:
    alaDHCPv6GuardTrustedGroup.setStatus("current")

alaDHCPv6SnoopingGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 29, 2, 2, 2, 7)
)
alaDHCPv6SnoopingGroup.setObjects(
      *(("ALCATEL-IND1-DHCPV6-MIB", "alaDHCPv6SnoopingInterfaceAdminStatus"),
        ("ALCATEL-IND1-DHCPV6-MIB", "alaDHCPv6SnoopingInterfaceRowStatus"),
        ("ALCATEL-IND1-DHCPV6-MIB", "alaDHCPv6BindingTimeout"),
        ("ALCATEL-IND1-DHCPV6-MIB", "alaDHCPv6BindingAction"),
        ("ALCATEL-IND1-DHCPV6-MIB", "alaDHCPv6BindingPersistency"),
        ("ALCATEL-IND1-DHCPV6-MIB", "alaDHCPv6BindingPortIfIndex"),
        ("ALCATEL-IND1-DHCPV6-MIB", "alaDHCPv6BindingGlobalAddress"),
        ("ALCATEL-IND1-DHCPV6-MIB", "alaDHCPv6BindingLeaseTime"),
        ("ALCATEL-IND1-DHCPV6-MIB", "alaDHCPv6BindingPhysAddress"),
        ("ALCATEL-IND1-DHCPV6-MIB", "alaDHCPv6BindingType"),
        ("ALCATEL-IND1-DHCPV6-MIB", "alaDHCPv6BindingRowStatus"),
        ("ALCATEL-IND1-DHCPV6-MIB", "alaDHCPv6SourceFilterInterfaceRowStatus"),
        ("ALCATEL-IND1-DHCPV6-MIB", "alaDHCPv6SourceFilterPortRowStatus"),
        ("ALCATEL-IND1-DHCPV6-MIB", "alaDHCPv6SnoopingSourceFilterAdminState"),
        ("ALCATEL-IND1-DHCPV6-MIB", "alaDHCPv6SourceFilterServiceRowStatus"))
)
if mibBuilder.loadTexts:
    alaDHCPv6SnoopingGroup.setStatus("current")

alaDHCPv6IsfNotificationsObjectsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 29, 2, 2, 2, 9)
)
alaDHCPv6IsfNotificationsObjectsGroup.setObjects(
    ("ALCATEL-IND1-DHCPV6-MIB", "alaDhcpv6IsfTcamFailMsg")
)
if mibBuilder.loadTexts:
    alaDHCPv6IsfNotificationsObjectsGroup.setStatus("current")

alaDHCPv6SrvStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 29, 2, 2, 2, 10)
)
alaDHCPv6SrvStatsGroup.setObjects(
      *(("ALCATEL-IND1-DHCPV6-MIB", "alaDHCPv6SrvStatsServerName"),
        ("ALCATEL-IND1-DHCPV6-MIB", "alaDHCPv6SrvStatsServerStatus"),
        ("ALCATEL-IND1-DHCPV6-MIB", "alaDHCPv6SrvStatsTotalSubnetsManaged"),
        ("ALCATEL-IND1-DHCPV6-MIB", "alaDHCPv6SrvStatsTotalSubnetsUsed"),
        ("ALCATEL-IND1-DHCPV6-MIB", "alaDHCPv6SrvStatsTotalSubnetsUnused"),
        ("ALCATEL-IND1-DHCPV6-MIB", "alaDHCPv6SrvStatsTotalSubnetsFull"),
        ("ALCATEL-IND1-DHCPV6-MIB", "alaDHCPv6SrvStatsServerUpTime"),
        ("ALCATEL-IND1-DHCPV6-MIB", "alaDHCPv6SrvStatsLeaseDbSyncTime"),
        ("ALCATEL-IND1-DHCPV6-MIB", "alaDHCPv6SrvStatsLastSyncTime"),
        ("ALCATEL-IND1-DHCPV6-MIB", "alaDHCPv6SrvStatsNextSyncTime"))
)
if mibBuilder.loadTexts:
    alaDHCPv6SrvStatsGroup.setStatus("current")

alaDHCPv6GuardServiceGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 29, 2, 2, 2, 11)
)
alaDHCPv6GuardServiceGroup.setObjects(
      *(("ALCATEL-IND1-DHCPV6-MIB", "alaDHCPv6GuardServiceAdminStatus"),
        ("ALCATEL-IND1-DHCPV6-MIB", "alaDHCPv6GuardServiceClient"),
        ("ALCATEL-IND1-DHCPV6-MIB", "alaDHCPv6GuardServiceRowStatus"))
)
if mibBuilder.loadTexts:
    alaDHCPv6GuardServiceGroup.setStatus("current")

alaDHCPv6SnoopingServiceGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 29, 2, 2, 2, 12)
)
alaDHCPv6SnoopingServiceGroup.setObjects(
      *(("ALCATEL-IND1-DHCPV6-MIB", "alaDHCPv6SnoopingServiceAdminStatus"),
        ("ALCATEL-IND1-DHCPV6-MIB", "alaDHCPv6SnoopingServiceRowStatus"))
)
if mibBuilder.loadTexts:
    alaDHCPv6SnoopingServiceGroup.setStatus("current")

alaDHCPv6BindingServiceGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 29, 2, 2, 2, 13)
)
alaDHCPv6BindingServiceGroup.setObjects(
      *(("ALCATEL-IND1-DHCPV6-MIB", "alaDHCPv6BindingServicePortIfIndex"),
        ("ALCATEL-IND1-DHCPV6-MIB", "alaDHCPv6BindingServiceEncapVal"),
        ("ALCATEL-IND1-DHCPV6-MIB", "alaDHCPv6BindingServiceGlobalAddressType"),
        ("ALCATEL-IND1-DHCPV6-MIB", "alaDHCPv6BindingServiceGlobalAddress"),
        ("ALCATEL-IND1-DHCPV6-MIB", "alaDHCPv6BindingServiceLeaseTime"),
        ("ALCATEL-IND1-DHCPV6-MIB", "alaDHCPv6BindingServicePhysAddress"),
        ("ALCATEL-IND1-DHCPV6-MIB", "alaDHCPv6BindingServiceType"),
        ("ALCATEL-IND1-DHCPV6-MIB", "alaDHCPv6BindingServiceRowStatus"))
)
if mibBuilder.loadTexts:
    alaDHCPv6BindingServiceGroup.setStatus("current")

alaDHCPv6GuardServiceTrustSourceGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 29, 2, 2, 2, 14)
)
alaDHCPv6GuardServiceTrustSourceGroup.setObjects(
    ("ALCATEL-IND1-DHCPV6-MIB", "alaDHCPv6GuardServiceTrustSourceType")
)
if mibBuilder.loadTexts:
    alaDHCPv6GuardServiceTrustSourceGroup.setStatus("current")


# Notification objects

alaDHCPv6SrvLeaseUtilizationThresholdTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 29, 2, 0, 1)
)
alaDHCPv6SrvLeaseUtilizationThresholdTrap.setObjects(
      *(("ALCATEL-IND1-DHCPV6-MIB", "alaDHCPv6SrvLeaseThresholdStatus"),
        ("ALCATEL-IND1-DHCPV6-MIB", "alaDHCPv6SrvSubnetDescriptor"))
)
if mibBuilder.loadTexts:
    alaDHCPv6SrvLeaseUtilizationThresholdTrap.setStatus(
        "current"
    )

alaDhcpv6IsfTcamFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 29, 2, 0, 2)
)
alaDhcpv6IsfTcamFail.setObjects(
    ("ALCATEL-IND1-DHCPV6-MIB", "alaDhcpv6IsfTcamFailMsg")
)
if mibBuilder.loadTexts:
    alaDhcpv6IsfTcamFail.setStatus(
        "current"
    )


# Notifications groups

alaDHCPv6SrvNotificationsGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 29, 2, 2, 2, 3)
)
alaDHCPv6SrvNotificationsGroup.setObjects(
    ("ALCATEL-IND1-DHCPV6-MIB", "alaDHCPv6SrvLeaseUtilizationThresholdTrap")
)
if mibBuilder.loadTexts:
    alaDHCPv6SrvNotificationsGroup.setStatus(
        "current"
    )

alaDHCPv6IsfNotificationsGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 29, 2, 2, 2, 8)
)
alaDHCPv6IsfNotificationsGroup.setObjects(
    ("ALCATEL-IND1-DHCPV6-MIB", "alaDhcpv6IsfTcamFail")
)
if mibBuilder.loadTexts:
    alaDHCPv6IsfNotificationsGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

alaDHCPv6Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 29, 2, 2, 1, 1)
)
alaDHCPv6Compliance.setObjects(
      *(("ALCATEL-IND1-DHCPV6-MIB", "alaDHCPv6RelayGroup"),
        ("ALCATEL-IND1-DHCPV6-MIB", "alaDHCPv6SrvGroup"),
        ("ALCATEL-IND1-DHCPV6-MIB", "alaDHCPv6SrvNotificationsGroup"),
        ("ALCATEL-IND1-DHCPV6-MIB", "alaDHCPv6SrvLeaseUtilizationThresholdGroup"),
        ("ALCATEL-IND1-DHCPV6-MIB", "alaDHCPv6GuardInterfaceGroup"),
        ("ALCATEL-IND1-DHCPV6-MIB", "alaDHCPv6GuardTrustedGroup"),
        ("ALCATEL-IND1-DHCPV6-MIB", "alaDHCPv6SnoopingGroup"),
        ("ALCATEL-IND1-DHCPV6-MIB", "alaDHCPv6IsfNotificationsGroup"),
        ("ALCATEL-IND1-DHCPV6-MIB", "alaDHCPv6SrvStatsGroup"),
        ("ALCATEL-IND1-DHCPV6-MIB", "alaDHCPv6GuardServiceGroup"),
        ("ALCATEL-IND1-DHCPV6-MIB", "alaDHCPv6SnoopingServiceGroup"),
        ("ALCATEL-IND1-DHCPV6-MIB", "alaDHCPv6BindingServiceGroup"))
)
if mibBuilder.loadTexts:
    alaDHCPv6Compliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ALCATEL-IND1-DHCPV6-MIB",
    **{"AlaDHCPv6GuardTrustedSourceIfIndex": AlaDHCPv6GuardTrustedSourceIfIndex,
       "alcatelIND1DHCPv6MIB": alcatelIND1DHCPv6MIB,
       "alcatelIND1DHCPv6MIBNotifications": alcatelIND1DHCPv6MIBNotifications,
       "alaDHCPv6SrvLeaseUtilizationThresholdTrap": alaDHCPv6SrvLeaseUtilizationThresholdTrap,
       "alaDhcpv6IsfTcamFail": alaDhcpv6IsfTcamFail,
       "alcatelIND1DHCPv6MIBObjects": alcatelIND1DHCPv6MIBObjects,
       "alaDHCPv6RelayConfig": alaDHCPv6RelayConfig,
       "alaDHCPv6RelayAdminStatus": alaDHCPv6RelayAdminStatus,
       "alaDHCPv6RelayMaximumHops": alaDHCPv6RelayMaximumHops,
       "alaDHCPv6RelayInterfaceIDStatus": alaDHCPv6RelayInterfaceIDStatus,
       "alaDHCPv6RelayInterfaceIDPrefix": alaDHCPv6RelayInterfaceIDPrefix,
       "alaDHCPv6RelayRemoteIDStatus": alaDHCPv6RelayRemoteIDStatus,
       "alaDHCPv6RelayRemoteIDFormatType": alaDHCPv6RelayRemoteIDFormatType,
       "alaDHCPv6RelayRemoteIDStringValue": alaDHCPv6RelayRemoteIDStringValue,
       "alaDHCPv6RelayRemoteIDEnterpriseNumber": alaDHCPv6RelayRemoteIDEnterpriseNumber,
       "alaDHCPv6SrvConfig": alaDHCPv6SrvConfig,
       "alaDHCPv6SrvGlobalConfigStatus": alaDHCPv6SrvGlobalConfigStatus,
       "alaDHCPv6SrvGlobalRestart": alaDHCPv6SrvGlobalRestart,
       "alaDHCPv6SrvGlobalClearStat": alaDHCPv6SrvGlobalClearStat,
       "alaDHCPv6RelayInterfaceTable": alaDHCPv6RelayInterfaceTable,
       "alaDHCPv6RelayInterfaceEntry": alaDHCPv6RelayInterfaceEntry,
       "alaDHCPv6RelayInterfaceAdminStatus": alaDHCPv6RelayInterfaceAdminStatus,
       "alaDHCPv6RelayDestinationTable": alaDHCPv6RelayDestinationTable,
       "alaDHCPv6RelayDestinationEntry": alaDHCPv6RelayDestinationEntry,
       "alaDHCPv6RelayDestinationAddressType": alaDHCPv6RelayDestinationAddressType,
       "alaDHCPv6RelayDestinationAddress": alaDHCPv6RelayDestinationAddress,
       "alaDHCPv6RelayDestinationRowStatus": alaDHCPv6RelayDestinationRowStatus,
       "alaDHCPv6SrvLease": alaDHCPv6SrvLease,
       "alaDHCPv6SrvLeaseTable": alaDHCPv6SrvLeaseTable,
       "alaDHCPv6SrvLeaseEntry": alaDHCPv6SrvLeaseEntry,
       "alaDHCPv6SrvLeaseIpv6Address": alaDHCPv6SrvLeaseIpv6Address,
       "alaDHCPv6SrvLeaseLeaseGrant": alaDHCPv6SrvLeaseLeaseGrant,
       "alaDHCPv6SrvLeasePrefLeaseExpiry": alaDHCPv6SrvLeasePrefLeaseExpiry,
       "alaDHCPv6SrvLeaseValidLeaseExpiry": alaDHCPv6SrvLeaseValidLeaseExpiry,
       "alaDHCPv6SrvLeaseType": alaDHCPv6SrvLeaseType,
       "alaDHCPv6SrvTrapsObj": alaDHCPv6SrvTrapsObj,
       "alaDHCPv6SrvLeaseThresholdStatus": alaDHCPv6SrvLeaseThresholdStatus,
       "alaDHCPv6SrvSubnetDescriptor": alaDHCPv6SrvSubnetDescriptor,
       "alaDHCPv6GuardInterfaceTable": alaDHCPv6GuardInterfaceTable,
       "alaDHCPv6GuardInterfaceEntry": alaDHCPv6GuardInterfaceEntry,
       "alaDHCPv6GuardInterfaceAdminStatus": alaDHCPv6GuardInterfaceAdminStatus,
       "alaDHCPv6GuardInterfaceRowStatus": alaDHCPv6GuardInterfaceRowStatus,
       "alaDHCPv6GuardInterfaceClient": alaDHCPv6GuardInterfaceClient,
       "alaDHCPv6GuardInterfaceLDRAAdminStatus": alaDHCPv6GuardInterfaceLDRAAdminStatus,
       "alaDHCPv6GuardTrustedSourceTable": alaDHCPv6GuardTrustedSourceTable,
       "alaDHCPv6GuardTrustedSourceEntry": alaDHCPv6GuardTrustedSourceEntry,
       "alaDHCPv6GuardTrustedSourceIfIndex": alaDHCPv6GuardTrustedSourceIfIndex,
       "alaDHCPv6GuardTrustedSourceRowStatus": alaDHCPv6GuardTrustedSourceRowStatus,
       "alaDHCPv6SnoopingInterfaceTable": alaDHCPv6SnoopingInterfaceTable,
       "alaDHCPv6SnoopingInterfaceEntry": alaDHCPv6SnoopingInterfaceEntry,
       "alaDHCPv6SnoopingInterfaceIndex": alaDHCPv6SnoopingInterfaceIndex,
       "alaDHCPv6SnoopingInterfaceAdminStatus": alaDHCPv6SnoopingInterfaceAdminStatus,
       "alaDHCPv6SnoopingInterfaceRowStatus": alaDHCPv6SnoopingInterfaceRowStatus,
       "alaDHCPv6BindingConfig": alaDHCPv6BindingConfig,
       "alaDHCPv6BindingTimeout": alaDHCPv6BindingTimeout,
       "alaDHCPv6BindingAction": alaDHCPv6BindingAction,
       "alaDHCPv6BindingPersistency": alaDHCPv6BindingPersistency,
       "alaDHCPv6BindingTable": alaDHCPv6BindingTable,
       "alaDHCPv6BindingEntry": alaDHCPv6BindingEntry,
       "alaDHCPv6BindingInterfaceIndex": alaDHCPv6BindingInterfaceIndex,
       "alaDHCPv6BindingLinkLocalAddress": alaDHCPv6BindingLinkLocalAddress,
       "alaDHCPv6BindingPortIfIndex": alaDHCPv6BindingPortIfIndex,
       "alaDHCPv6BindingGlobalAddress": alaDHCPv6BindingGlobalAddress,
       "alaDHCPv6BindingLeaseTime": alaDHCPv6BindingLeaseTime,
       "alaDHCPv6BindingPhysAddress": alaDHCPv6BindingPhysAddress,
       "alaDHCPv6BindingType": alaDHCPv6BindingType,
       "alaDHCPv6BindingRowStatus": alaDHCPv6BindingRowStatus,
       "alaDHCPv6SourceFilterInterfaceTable": alaDHCPv6SourceFilterInterfaceTable,
       "alaDHCPv6SourceFilterInterfaceEntry": alaDHCPv6SourceFilterInterfaceEntry,
       "alaDHCPv6SourceFilterInterfaceIndex": alaDHCPv6SourceFilterInterfaceIndex,
       "alaDHCPv6SourceFilterInterfaceRowStatus": alaDHCPv6SourceFilterInterfaceRowStatus,
       "alaDHCPv6SourceFilterPortTable": alaDHCPv6SourceFilterPortTable,
       "alaDHCPv6SourceFilterPortEntry": alaDHCPv6SourceFilterPortEntry,
       "alaDHCPv6SourceFilterPortIndex": alaDHCPv6SourceFilterPortIndex,
       "alaDHCPv6SourceFilterPortRowStatus": alaDHCPv6SourceFilterPortRowStatus,
       "alaDhcpv6IsfTrapsObj": alaDhcpv6IsfTrapsObj,
       "alaDhcpv6IsfTcamFailMsg": alaDhcpv6IsfTcamFailMsg,
       "alaDHCPv6SnoopingSourceFilter": alaDHCPv6SnoopingSourceFilter,
       "alaDHCPv6SnoopingSourceFilterAdminState": alaDHCPv6SnoopingSourceFilterAdminState,
       "alaDHCPv6SrvStats": alaDHCPv6SrvStats,
       "alaDHCPv6SrvStatsServerName": alaDHCPv6SrvStatsServerName,
       "alaDHCPv6SrvStatsServerStatus": alaDHCPv6SrvStatsServerStatus,
       "alaDHCPv6SrvStatsTotalSubnetsManaged": alaDHCPv6SrvStatsTotalSubnetsManaged,
       "alaDHCPv6SrvStatsTotalSubnetsUsed": alaDHCPv6SrvStatsTotalSubnetsUsed,
       "alaDHCPv6SrvStatsTotalSubnetsUnused": alaDHCPv6SrvStatsTotalSubnetsUnused,
       "alaDHCPv6SrvStatsTotalSubnetsFull": alaDHCPv6SrvStatsTotalSubnetsFull,
       "alaDHCPv6SrvStatsServerUpTime": alaDHCPv6SrvStatsServerUpTime,
       "alaDHCPv6SrvStatsLeaseDbSyncTime": alaDHCPv6SrvStatsLeaseDbSyncTime,
       "alaDHCPv6SrvStatsLastSyncTime": alaDHCPv6SrvStatsLastSyncTime,
       "alaDHCPv6SrvStatsNextSyncTime": alaDHCPv6SrvStatsNextSyncTime,
       "alaDHCPv6GuardServiceTable": alaDHCPv6GuardServiceTable,
       "alaDHCPv6GuardServiceEntry": alaDHCPv6GuardServiceEntry,
       "alaDHCPv6GuardServiceId": alaDHCPv6GuardServiceId,
       "alaDHCPv6GuardServiceAdminStatus": alaDHCPv6GuardServiceAdminStatus,
       "alaDHCPv6GuardServiceClient": alaDHCPv6GuardServiceClient,
       "alaDHCPv6GuardServiceRowStatus": alaDHCPv6GuardServiceRowStatus,
       "alaDHCPv6SnoopingServiceTable": alaDHCPv6SnoopingServiceTable,
       "alaDHCPv6SnoopingServiceEntry": alaDHCPv6SnoopingServiceEntry,
       "alaDHCPv6SnoopingServiceId": alaDHCPv6SnoopingServiceId,
       "alaDHCPv6SnoopingServiceAdminStatus": alaDHCPv6SnoopingServiceAdminStatus,
       "alaDHCPv6SnoopingServiceRowStatus": alaDHCPv6SnoopingServiceRowStatus,
       "alaDHCPv6BindingServiceTable": alaDHCPv6BindingServiceTable,
       "alaDHCPv6BindingServiceEntry": alaDHCPv6BindingServiceEntry,
       "alaDHCPv6BindingServiceId": alaDHCPv6BindingServiceId,
       "alaDHCPv6BindingServiceLinkLocalAddressType": alaDHCPv6BindingServiceLinkLocalAddressType,
       "alaDHCPv6BindingServiceLinkLocalAddress": alaDHCPv6BindingServiceLinkLocalAddress,
       "alaDHCPv6BindingServicePortIfIndex": alaDHCPv6BindingServicePortIfIndex,
       "alaDHCPv6BindingServiceEncapVal": alaDHCPv6BindingServiceEncapVal,
       "alaDHCPv6BindingServiceGlobalAddressType": alaDHCPv6BindingServiceGlobalAddressType,
       "alaDHCPv6BindingServiceGlobalAddress": alaDHCPv6BindingServiceGlobalAddress,
       "alaDHCPv6BindingServiceLeaseTime": alaDHCPv6BindingServiceLeaseTime,
       "alaDHCPv6BindingServicePhysAddress": alaDHCPv6BindingServicePhysAddress,
       "alaDHCPv6BindingServiceType": alaDHCPv6BindingServiceType,
       "alaDHCPv6BindingServiceRowStatus": alaDHCPv6BindingServiceRowStatus,
       "alaDHCPv6GuardServiceTrustSourceTable": alaDHCPv6GuardServiceTrustSourceTable,
       "alaDHCPv6GuardServiceTrustSourceEntry": alaDHCPv6GuardServiceTrustSourceEntry,
       "alaDHCPv6GuardServiceTrustSourceServiceId": alaDHCPv6GuardServiceTrustSourceServiceId,
       "alaDHCPv6GuardServiceTrustSourceSdpId": alaDHCPv6GuardServiceTrustSourceSdpId,
       "alaDHCPv6GuardServiceTrustSourceType": alaDHCPv6GuardServiceTrustSourceType,
       "alaDHCPv6SourceFilterServiceTable": alaDHCPv6SourceFilterServiceTable,
       "alaDHCPv6SourceFilterServiceEntry": alaDHCPv6SourceFilterServiceEntry,
       "alaDHCPv6SourceFilterServiceIndex": alaDHCPv6SourceFilterServiceIndex,
       "alaDHCPv6SourceFilterServiceRowStatus": alaDHCPv6SourceFilterServiceRowStatus,
       "alcatelIND1DHCPv6MIBConformance": alcatelIND1DHCPv6MIBConformance,
       "alcatelIND1DHCPv6MIBCompliances": alcatelIND1DHCPv6MIBCompliances,
       "alaDHCPv6Compliance": alaDHCPv6Compliance,
       "alcatelIND1DHCPv6MIBGroups": alcatelIND1DHCPv6MIBGroups,
       "alaDHCPv6RelayGroup": alaDHCPv6RelayGroup,
       "alaDHCPv6SrvGroup": alaDHCPv6SrvGroup,
       "alaDHCPv6SrvNotificationsGroup": alaDHCPv6SrvNotificationsGroup,
       "alaDHCPv6SrvLeaseUtilizationThresholdGroup": alaDHCPv6SrvLeaseUtilizationThresholdGroup,
       "alaDHCPv6GuardInterfaceGroup": alaDHCPv6GuardInterfaceGroup,
       "alaDHCPv6GuardTrustedGroup": alaDHCPv6GuardTrustedGroup,
       "alaDHCPv6SnoopingGroup": alaDHCPv6SnoopingGroup,
       "alaDHCPv6IsfNotificationsGroup": alaDHCPv6IsfNotificationsGroup,
       "alaDHCPv6IsfNotificationsObjectsGroup": alaDHCPv6IsfNotificationsObjectsGroup,
       "alaDHCPv6SrvStatsGroup": alaDHCPv6SrvStatsGroup,
       "alaDHCPv6GuardServiceGroup": alaDHCPv6GuardServiceGroup,
       "alaDHCPv6SnoopingServiceGroup": alaDHCPv6SnoopingServiceGroup,
       "alaDHCPv6BindingServiceGroup": alaDHCPv6BindingServiceGroup,
       "alaDHCPv6GuardServiceTrustSourceGroup": alaDHCPv6GuardServiceTrustSourceGroup}
)
