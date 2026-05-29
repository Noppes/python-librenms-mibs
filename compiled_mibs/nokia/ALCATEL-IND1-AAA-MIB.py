# SNMP MIB module (ALCATEL-IND1-AAA-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\nokia\aos6\ALCATEL-IND1-AAA-MIB

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

(alaAaaTraps,
 softentIND1AAA) = mibBuilder.importSymbols(
    "ALCATEL-IND1-BASE",
    "alaAaaTraps",
    "softentIND1AAA")

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

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

(DisplayString,
 MacAddress,
 PhysAddress,
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

alcatelIND1AAAMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1)
)
if mibBuilder.loadTexts:
    alcatelIND1AAAMIB.setRevisions(
        ("2019-10-07 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class AaasRadNasPortTypeConvention(TextualConvention, Integer32):
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
              15,
              16,
              17,
              18,
              19)
        )
    )
    namedValues = NamedValues(
        *(("async", 0),
          ("sync", 1),
          ("isdn-sync", 2),
          ("isdn-async-v120", 3),
          ("isdn-async-v110", 4),
          ("virtual", 5),
          ("piafs", 6),
          ("hdlc-clear-channel", 7),
          ("x25", 8),
          ("x75", 9),
          ("g3-fax", 10),
          ("sdsl-symmetric-dsl", 11),
          ("adsl-cap-asymmetric-dsl", 12),
          ("adsl-dmt", 13),
          ("idsl", 14),
          ("ethernet", 15),
          ("xdsl", 16),
          ("cable", 17),
          ("wireless-other", 18),
          ("wireless-ieee-802-11", 19))
    )



# MIB Managed Objects in the order of their OIDs

_AlcatelIND1AAAMIBObjects_ObjectIdentity = ObjectIdentity
alcatelIND1AAAMIBObjects = _AlcatelIND1AAAMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 1)
)
if mibBuilder.loadTexts:
    alcatelIND1AAAMIBObjects.setStatus("current")
_AaaServerMIB_ObjectIdentity = ObjectIdentity
aaaServerMIB = _AaaServerMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 1, 1)
)
_AaaServerTable_Object = MibTable
aaaServerTable = _AaaServerTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 1, 1, 1)
)
if mibBuilder.loadTexts:
    aaaServerTable.setStatus("current")
_AaaServerEntry_Object = MibTableRow
aaaServerEntry = _AaaServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 1, 1, 1, 1)
)
aaaServerEntry.setIndexNames(
    (0, "ALCATEL-IND1-AAA-MIB", "aaasName"),
)
if mibBuilder.loadTexts:
    aaaServerEntry.setStatus("current")


class _AaasName_Type(DisplayString):
    """Custom type aaasName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AaasName_Type.__name__ = "DisplayString"
_AaasName_Object = MibTableColumn
aaasName = _AaasName_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 1, 1, 1, 1, 1),
    _AaasName_Type()
)
aaasName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aaasName.setStatus("current")


class _AaasProtocol_Type(Integer32):
    """Custom type aaasProtocol based on Integer32"""
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
        *(("radius", 1),
          ("ldap", 2),
          ("ace", 3),
          ("tacacs", 4))
    )


_AaasProtocol_Type.__name__ = "Integer32"
_AaasProtocol_Object = MibTableColumn
aaasProtocol = _AaasProtocol_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 1, 1, 1, 1, 2),
    _AaasProtocol_Type()
)
aaasProtocol.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aaasProtocol.setStatus("current")


class _AaasHostName_Type(DisplayString):
    """Custom type aaasHostName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_AaasHostName_Type.__name__ = "DisplayString"
_AaasHostName_Object = MibTableColumn
aaasHostName = _AaasHostName_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 1, 1, 1, 1, 3),
    _AaasHostName_Type()
)
aaasHostName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aaasHostName.setStatus("current")
_AaasIpAddress_Type = IpAddress
_AaasIpAddress_Object = MibTableColumn
aaasIpAddress = _AaasIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 1, 1, 1, 1, 4),
    _AaasIpAddress_Type()
)
aaasIpAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aaasIpAddress.setStatus("current")


class _AaasHostName2_Type(DisplayString):
    """Custom type aaasHostName2 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_AaasHostName2_Type.__name__ = "DisplayString"
_AaasHostName2_Object = MibTableColumn
aaasHostName2 = _AaasHostName2_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 1, 1, 1, 1, 5),
    _AaasHostName2_Type()
)
aaasHostName2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aaasHostName2.setStatus("current")
_AaasIpAddress2_Type = IpAddress
_AaasIpAddress2_Object = MibTableColumn
aaasIpAddress2 = _AaasIpAddress2_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 1, 1, 1, 1, 6),
    _AaasIpAddress2_Type()
)
aaasIpAddress2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aaasIpAddress2.setStatus("current")


class _AaasRetries_Type(Integer32):
    """Custom type aaasRetries based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32),
    )


_AaasRetries_Type.__name__ = "Integer32"
_AaasRetries_Object = MibTableColumn
aaasRetries = _AaasRetries_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 1, 1, 1, 1, 7),
    _AaasRetries_Type()
)
aaasRetries.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aaasRetries.setStatus("current")


class _AaasTimout_Type(Integer32):
    """Custom type aaasTimout based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 30),
    )


_AaasTimout_Type.__name__ = "Integer32"
_AaasTimout_Object = MibTableColumn
aaasTimout = _AaasTimout_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 1, 1, 1, 1, 8),
    _AaasTimout_Type()
)
aaasTimout.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aaasTimout.setStatus("current")


class _AaasRadKey_Type(DisplayString):
    """Custom type aaasRadKey based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_AaasRadKey_Type.__name__ = "DisplayString"
_AaasRadKey_Object = MibTableColumn
aaasRadKey = _AaasRadKey_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 1, 1, 1, 1, 9),
    _AaasRadKey_Type()
)
aaasRadKey.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aaasRadKey.setStatus("current")


class _AaasRadAuthPort_Type(Integer32):
    """Custom type aaasRadAuthPort based on Integer32"""
    defaultValue = 1645

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AaasRadAuthPort_Type.__name__ = "Integer32"
_AaasRadAuthPort_Object = MibTableColumn
aaasRadAuthPort = _AaasRadAuthPort_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 1, 1, 1, 1, 10),
    _AaasRadAuthPort_Type()
)
aaasRadAuthPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aaasRadAuthPort.setStatus("current")


class _AaasRadAcctPort_Type(Integer32):
    """Custom type aaasRadAcctPort based on Integer32"""
    defaultValue = 1646

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AaasRadAcctPort_Type.__name__ = "Integer32"
_AaasRadAcctPort_Object = MibTableColumn
aaasRadAcctPort = _AaasRadAcctPort_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 1, 1, 1, 1, 11),
    _AaasRadAcctPort_Type()
)
aaasRadAcctPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aaasRadAcctPort.setStatus("current")


class _AaasLdapPort_Type(Integer32):
    """Custom type aaasLdapPort based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AaasLdapPort_Type.__name__ = "Integer32"
_AaasLdapPort_Object = MibTableColumn
aaasLdapPort = _AaasLdapPort_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 1, 1, 1, 1, 12),
    _AaasLdapPort_Type()
)
aaasLdapPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aaasLdapPort.setStatus("current")


class _AaasLdapDn_Type(DisplayString):
    """Custom type aaasLdapDn based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_AaasLdapDn_Type.__name__ = "DisplayString"
_AaasLdapDn_Object = MibTableColumn
aaasLdapDn = _AaasLdapDn_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 1, 1, 1, 1, 13),
    _AaasLdapDn_Type()
)
aaasLdapDn.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aaasLdapDn.setStatus("current")


class _AaasLdapPasswd_Type(DisplayString):
    """Custom type aaasLdapPasswd based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AaasLdapPasswd_Type.__name__ = "DisplayString"
_AaasLdapPasswd_Object = MibTableColumn
aaasLdapPasswd = _AaasLdapPasswd_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 1, 1, 1, 1, 14),
    _AaasLdapPasswd_Type()
)
aaasLdapPasswd.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aaasLdapPasswd.setStatus("current")


class _AaasLdapSearchBase_Type(DisplayString):
    """Custom type aaasLdapSearchBase based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_AaasLdapSearchBase_Type.__name__ = "DisplayString"
_AaasLdapSearchBase_Object = MibTableColumn
aaasLdapSearchBase = _AaasLdapSearchBase_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 1, 1, 1, 1, 15),
    _AaasLdapSearchBase_Type()
)
aaasLdapSearchBase.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aaasLdapSearchBase.setStatus("current")


class _AaasLdapServType_Type(Integer32):
    """Custom type aaasLdapServType based on Integer32"""
    defaultValue = 2

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
        *(("ns", 0),
          ("generic", 1),
          ("netscape", 2),
          ("novell", 3),
          ("sun", 4),
          ("microsoft", 5))
    )


_AaasLdapServType_Type.__name__ = "Integer32"
_AaasLdapServType_Object = MibTableColumn
aaasLdapServType = _AaasLdapServType_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 1, 1, 1, 1, 16),
    _AaasLdapServType_Type()
)
aaasLdapServType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aaasLdapServType.setStatus("current")


class _AaasLdapEnableSsl_Type(Integer32):
    """Custom type aaasLdapEnableSsl based on Integer32"""
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
        *(("ns", 0),
          ("true", 1),
          ("false", 2))
    )


_AaasLdapEnableSsl_Type.__name__ = "Integer32"
_AaasLdapEnableSsl_Object = MibTableColumn
aaasLdapEnableSsl = _AaasLdapEnableSsl_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 1, 1, 1, 1, 17),
    _AaasLdapEnableSsl_Type()
)
aaasLdapEnableSsl.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aaasLdapEnableSsl.setStatus("current")


class _AaasAceClear_Type(Integer32):
    """Custom type aaasAceClear based on Integer32"""
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
        *(("ns", 0),
          ("true", 1),
          ("false", 2))
    )


_AaasAceClear_Type.__name__ = "Integer32"
_AaasAceClear_Object = MibTableColumn
aaasAceClear = _AaasAceClear_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 1, 1, 1, 1, 18),
    _AaasAceClear_Type()
)
aaasAceClear.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aaasAceClear.setStatus("current")


class _AaasRowStatus_Type(RowStatus):
    """Custom type aaasRowStatus based on RowStatus"""
    defaultValue = 2


_AaasRowStatus_Type.__name__ = "RowStatus"
_AaasRowStatus_Object = MibTableColumn
aaasRowStatus = _AaasRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 1, 1, 1, 1, 19),
    _AaasRowStatus_Type()
)
aaasRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aaasRowStatus.setStatus("current")


class _AaasTacacsKey_Type(DisplayString):
    """Custom type aaasTacacsKey based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_AaasTacacsKey_Type.__name__ = "DisplayString"
_AaasTacacsKey_Object = MibTableColumn
aaasTacacsKey = _AaasTacacsKey_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 1, 1, 1, 1, 20),
    _AaasTacacsKey_Type()
)
aaasTacacsKey.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aaasTacacsKey.setStatus("current")


class _AaasTacacsPort_Type(Integer32):
    """Custom type aaasTacacsPort based on Integer32"""
    defaultValue = 49

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AaasTacacsPort_Type.__name__ = "Integer32"
_AaasTacacsPort_Object = MibTableColumn
aaasTacacsPort = _AaasTacacsPort_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 1, 1, 1, 1, 21),
    _AaasTacacsPort_Type()
)
aaasTacacsPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aaasTacacsPort.setStatus("current")


class _AaasHttpPort_Type(Integer32):
    """Custom type aaasHttpPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AaasHttpPort_Type.__name__ = "Integer32"
_AaasHttpPort_Object = MibTableColumn
aaasHttpPort = _AaasHttpPort_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 1, 1, 1, 1, 22),
    _AaasHttpPort_Type()
)
aaasHttpPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aaasHttpPort.setStatus("current")


class _AaasHttpDirectory_Type(DisplayString):
    """Custom type aaasHttpDirectory based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_AaasHttpDirectory_Type.__name__ = "DisplayString"
_AaasHttpDirectory_Object = MibTableColumn
aaasHttpDirectory = _AaasHttpDirectory_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 1, 1, 1, 1, 23),
    _AaasHttpDirectory_Type()
)
aaasHttpDirectory.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aaasHttpDirectory.setStatus("current")


class _AaasHttpProxyHostName_Type(DisplayString):
    """Custom type aaasHttpProxyHostName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_AaasHttpProxyHostName_Type.__name__ = "DisplayString"
_AaasHttpProxyHostName_Object = MibTableColumn
aaasHttpProxyHostName = _AaasHttpProxyHostName_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 1, 1, 1, 1, 24),
    _AaasHttpProxyHostName_Type()
)
aaasHttpProxyHostName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aaasHttpProxyHostName.setStatus("current")
_AaasHttpProxyIpAddress_Type = IpAddress
_AaasHttpProxyIpAddress_Object = MibTableColumn
aaasHttpProxyIpAddress = _AaasHttpProxyIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 1, 1, 1, 1, 25),
    _AaasHttpProxyIpAddress_Type()
)
aaasHttpProxyIpAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aaasHttpProxyIpAddress.setStatus("current")


class _AaasHttpProxyPort_Type(Integer32):
    """Custom type aaasHttpProxyPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AaasHttpProxyPort_Type.__name__ = "Integer32"
_AaasHttpProxyPort_Object = MibTableColumn
aaasHttpProxyPort = _AaasHttpProxyPort_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 1, 1, 1, 1, 26),
    _AaasHttpProxyPort_Type()
)
aaasHttpProxyPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aaasHttpProxyPort.setStatus("current")


class _AaasVrfName_Type(DisplayString):
    """Custom type aaasVrfName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AaasVrfName_Type.__name__ = "DisplayString"
_AaasVrfName_Object = MibTableColumn
aaasVrfName = _AaasVrfName_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 1, 1, 1, 1, 27),
    _AaasVrfName_Type()
)
aaasVrfName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aaasVrfName.setStatus("current")


class _AaasRadMacAddrCase_Type(Integer32):
    """Custom type aaasRadMacAddrCase based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("uppercase", 0),
          ("lowercase", 1))
    )


_AaasRadMacAddrCase_Type.__name__ = "Integer32"
_AaasRadMacAddrCase_Object = MibTableColumn
aaasRadMacAddrCase = _AaasRadMacAddrCase_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 1, 1, 1, 1, 28),
    _AaasRadMacAddrCase_Type()
)
aaasRadMacAddrCase.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aaasRadMacAddrCase.setStatus("current")


class _AaasRadNasPort_Type(Integer32):
    """Custom type aaasRadNasPort based on Integer32"""
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
        *(("default", 0),
          ("ifindex", 1),
          ("not-applicable", 2))
    )


_AaasRadNasPort_Type.__name__ = "Integer32"
_AaasRadNasPort_Object = MibTableColumn
aaasRadNasPort = _AaasRadNasPort_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 1, 1, 1, 1, 29),
    _AaasRadNasPort_Type()
)
aaasRadNasPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aaasRadNasPort.setStatus("current")


class _AaasRadNasPortId_Type(Integer32):
    """Custom type aaasRadNasPortId based on Integer32"""
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


_AaasRadNasPortId_Type.__name__ = "Integer32"
_AaasRadNasPortId_Object = MibTableColumn
aaasRadNasPortId = _AaasRadNasPortId_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 1, 1, 1, 1, 30),
    _AaasRadNasPortId_Type()
)
aaasRadNasPortId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aaasRadNasPortId.setStatus("current")


class _AaasRadNasPortType_Type(AaasRadNasPortTypeConvention):
    """Custom type aaasRadNasPortType based on AaasRadNasPortTypeConvention"""
    defaultValue = 15


_AaasRadNasPortType_Type.__name__ = "AaasRadNasPortTypeConvention"
_AaasRadNasPortType_Object = MibTableColumn
aaasRadNasPortType = _AaasRadNasPortType_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 1, 1, 1, 1, 31),
    _AaasRadNasPortType_Type()
)
aaasRadNasPortType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aaasRadNasPortType.setStatus("current")


class _AaasRadMacAddrFormat_Type(Integer32):
    """Custom type aaasRadMacAddrFormat based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("uppercase", 0),
          ("lowercase", 1))
    )


_AaasRadMacAddrFormat_Type.__name__ = "Integer32"
_AaasRadMacAddrFormat_Object = MibTableColumn
aaasRadMacAddrFormat = _AaasRadMacAddrFormat_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 1, 1, 1, 1, 32),
    _AaasRadMacAddrFormat_Type()
)
aaasRadMacAddrFormat.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aaasRadMacAddrFormat.setStatus("current")


class _AaasRadUniqueAcctSessionId_Type(Integer32):
    """Custom type aaasRadUniqueAcctSessionId based on Integer32"""
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


_AaasRadUniqueAcctSessionId_Type.__name__ = "Integer32"
_AaasRadUniqueAcctSessionId_Object = MibTableColumn
aaasRadUniqueAcctSessionId = _AaasRadUniqueAcctSessionId_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 1, 1, 1, 1, 33),
    _AaasRadUniqueAcctSessionId_Type()
)
aaasRadUniqueAcctSessionId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aaasRadUniqueAcctSessionId.setStatus("current")


class _AaasRadMacAddrCaseStatus_Type(Integer32):
    """Custom type aaasRadMacAddrCaseStatus based on Integer32"""
    defaultValue = 0

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


_AaasRadMacAddrCaseStatus_Type.__name__ = "Integer32"
_AaasRadMacAddrCaseStatus_Object = MibTableColumn
aaasRadMacAddrCaseStatus = _AaasRadMacAddrCaseStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 1, 1, 1, 1, 34),
    _AaasRadMacAddrCaseStatus_Type()
)
aaasRadMacAddrCaseStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aaasRadMacAddrCaseStatus.setStatus("current")


class _AaasRadServerStatus_Type(Integer32):
    """Custom type aaasRadServerStatus based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("down", 0),
          ("up", 1))
    )


_AaasRadServerStatus_Type.__name__ = "Integer32"
_AaasRadServerStatus_Object = MibTableColumn
aaasRadServerStatus = _AaasRadServerStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 1, 1, 1, 1, 35),
    _AaasRadServerStatus_Type()
)
aaasRadServerStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aaasRadServerStatus.setStatus("current")


class _AaasRadHealthstatus_Type(Integer32):
    """Custom type aaasRadHealthstatus based on Integer32"""
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


_AaasRadHealthstatus_Type.__name__ = "Integer32"
_AaasRadHealthstatus_Object = MibTableColumn
aaasRadHealthstatus = _AaasRadHealthstatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 1, 1, 1, 1, 36),
    _AaasRadHealthstatus_Type()
)
aaasRadHealthstatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aaasRadHealthstatus.setStatus("current")


class _AaasRadPollInterval_Type(Integer32):
    """Custom type aaasRadPollInterval based on Integer32"""
    defaultValue = 50


_AaasRadPollInterval_Type.__name__ = "Integer32"
_AaasRadPollInterval_Object = MibTableColumn
aaasRadPollInterval = _AaasRadPollInterval_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 1, 1, 1, 1, 37),
    _AaasRadPollInterval_Type()
)
aaasRadPollInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aaasRadPollInterval.setStatus("current")


class _AaasRadFailoverStatus_Type(Integer32):
    """Custom type aaasRadFailoverStatus based on Integer32"""
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


_AaasRadFailoverStatus_Type.__name__ = "Integer32"
_AaasRadFailoverStatus_Object = MibTableColumn
aaasRadFailoverStatus = _AaasRadFailoverStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 1, 1, 1, 1, 38),
    _AaasRadFailoverStatus_Type()
)
aaasRadFailoverStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aaasRadFailoverStatus.setStatus("current")
_AaasRadUser_Type = DisplayString
_AaasRadUser_Object = MibTableColumn
aaasRadUser = _AaasRadUser_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 1, 1, 1, 1, 39),
    _AaasRadUser_Type()
)
aaasRadUser.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aaasRadUser.setStatus("current")
_AaasRadPasswd_Type = DisplayString
_AaasRadPasswd_Object = MibTableColumn
aaasRadPasswd = _AaasRadPasswd_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 1, 1, 1, 1, 40),
    _AaasRadPasswd_Type()
)
aaasRadPasswd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aaasRadPasswd.setStatus("current")


class _AaaRadServerPrimaryStatus_Type(Integer32):
    """Custom type aaaRadServerPrimaryStatus based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("down", 0),
          ("up", 1))
    )


_AaaRadServerPrimaryStatus_Type.__name__ = "Integer32"
_AaaRadServerPrimaryStatus_Object = MibTableColumn
aaaRadServerPrimaryStatus = _AaaRadServerPrimaryStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 1, 1, 1, 1, 41),
    _AaaRadServerPrimaryStatus_Type()
)
aaaRadServerPrimaryStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aaaRadServerPrimaryStatus.setStatus("current")


class _AaaRadServerBackupStatus_Type(Integer32):
    """Custom type aaaRadServerBackupStatus based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("down", 0),
          ("up", 1))
    )


_AaaRadServerBackupStatus_Type.__name__ = "Integer32"
_AaaRadServerBackupStatus_Object = MibTableColumn
aaaRadServerBackupStatus = _AaaRadServerBackupStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 1, 1, 1, 1, 42),
    _AaaRadServerBackupStatus_Type()
)
aaaRadServerBackupStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aaaRadServerBackupStatus.setStatus("current")
_AaasRadKeyHash_Type = DisplayString
_AaasRadKeyHash_Object = MibTableColumn
aaasRadKeyHash = _AaasRadKeyHash_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 1, 1, 1, 1, 43),
    _AaasRadKeyHash_Type()
)
aaasRadKeyHash.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aaasRadKeyHash.setStatus("current")
_AaaRadPrimSerNbUpToDown_Type = Integer32
_AaaRadPrimSerNbUpToDown_Object = MibTableColumn
aaaRadPrimSerNbUpToDown = _AaaRadPrimSerNbUpToDown_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 1, 1, 1, 1, 44),
    _AaaRadPrimSerNbUpToDown_Type()
)
aaaRadPrimSerNbUpToDown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aaaRadPrimSerNbUpToDown.setStatus("current")
_AaaRadPrimSerNbDownToUp_Type = Integer32
_AaaRadPrimSerNbDownToUp_Object = MibTableColumn
aaaRadPrimSerNbDownToUp = _AaaRadPrimSerNbDownToUp_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 1, 1, 1, 1, 45),
    _AaaRadPrimSerNbDownToUp_Type()
)
aaaRadPrimSerNbDownToUp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aaaRadPrimSerNbDownToUp.setStatus("current")
_AaaRadPrimServUpTime_Type = DisplayString
_AaaRadPrimServUpTime_Object = MibTableColumn
aaaRadPrimServUpTime = _AaaRadPrimServUpTime_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 1, 1, 1, 1, 46),
    _AaaRadPrimServUpTime_Type()
)
aaaRadPrimServUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aaaRadPrimServUpTime.setStatus("current")
_AaaRadPrimServDownTime_Type = DisplayString
_AaaRadPrimServDownTime_Object = MibTableColumn
aaaRadPrimServDownTime = _AaaRadPrimServDownTime_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 1, 1, 1, 1, 47),
    _AaaRadPrimServDownTime_Type()
)
aaaRadPrimServDownTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aaaRadPrimServDownTime.setStatus("current")
_AaaRadBkupSerNbUpToDown_Type = Integer32
_AaaRadBkupSerNbUpToDown_Object = MibTableColumn
aaaRadBkupSerNbUpToDown = _AaaRadBkupSerNbUpToDown_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 1, 1, 1, 1, 48),
    _AaaRadBkupSerNbUpToDown_Type()
)
aaaRadBkupSerNbUpToDown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aaaRadBkupSerNbUpToDown.setStatus("current")
_AaaRadBkupSerNbDownToUp_Type = Integer32
_AaaRadBkupSerNbDownToUp_Object = MibTableColumn
aaaRadBkupSerNbDownToUp = _AaaRadBkupSerNbDownToUp_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 1, 1, 1, 1, 49),
    _AaaRadBkupSerNbDownToUp_Type()
)
aaaRadBkupSerNbDownToUp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aaaRadBkupSerNbDownToUp.setStatus("current")
_AaaRadBkupServUpTime_Type = DisplayString
_AaaRadBkupServUpTime_Object = MibTableColumn
aaaRadBkupServUpTime = _AaaRadBkupServUpTime_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 1, 1, 1, 1, 50),
    _AaaRadBkupServUpTime_Type()
)
aaaRadBkupServUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aaaRadBkupServUpTime.setStatus("current")
_AaaRadBkupServDownTime_Type = DisplayString
_AaaRadBkupServDownTime_Object = MibTableColumn
aaaRadBkupServDownTime = _AaaRadBkupServDownTime_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 1, 1, 1, 1, 51),
    _AaaRadBkupServDownTime_Type()
)
aaaRadBkupServDownTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aaaRadBkupServDownTime.setStatus("current")
_AaasTacacsKeyHash_Type = DisplayString
_AaasTacacsKeyHash_Object = MibTableColumn
aaasTacacsKeyHash = _AaasTacacsKeyHash_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 1, 1, 1, 1, 52),
    _AaasTacacsKeyHash_Type()
)
aaasTacacsKeyHash.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aaasTacacsKeyHash.setStatus("current")
_AaasRadSalt_Type = DisplayString
_AaasRadSalt_Object = MibTableColumn
aaasRadSalt = _AaasRadSalt_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 1, 1, 1, 1, 53),
    _AaasRadSalt_Type()
)
aaasRadSalt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aaasRadSalt.setStatus("current")
_AaasRadSaltHash_Type = DisplayString
_AaasRadSaltHash_Object = MibTableColumn
aaasRadSaltHash = _AaasRadSaltHash_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 1, 1, 1, 1, 54),
    _AaasRadSaltHash_Type()
)
aaasRadSaltHash.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aaasRadSaltHash.setStatus("current")
_AaasTacacsSalt_Type = DisplayString
_AaasTacacsSalt_Object = MibTableColumn
aaasTacacsSalt = _AaasTacacsSalt_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 1, 1, 1, 1, 55),
    _AaasTacacsSalt_Type()
)
aaasTacacsSalt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aaasTacacsSalt.setStatus("current")
_AaasTacacsSaltHash_Type = DisplayString
_AaasTacacsSaltHash_Object = MibTableColumn
aaasTacacsSaltHash = _AaasTacacsSaltHash_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 1, 1, 1, 1, 56),
    _AaasTacacsSaltHash_Type()
)
aaasTacacsSaltHash.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aaasTacacsSaltHash.setStatus("current")
_AaasLdapSalt_Type = DisplayString
_AaasLdapSalt_Object = MibTableColumn
aaasLdapSalt = _AaasLdapSalt_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 1, 1, 1, 1, 57),
    _AaasLdapSalt_Type()
)
aaasLdapSalt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aaasLdapSalt.setStatus("current")
_AaasLdapSaltHash_Type = DisplayString
_AaasLdapSaltHash_Object = MibTableColumn
aaasLdapSaltHash = _AaasLdapSaltHash_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 1, 1, 1, 1, 58),
    _AaasLdapSaltHash_Type()
)
aaasLdapSaltHash.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aaasLdapSaltHash.setStatus("current")
_AaasLdapPasswdHash_Type = DisplayString
_AaasLdapPasswdHash_Object = MibTableColumn
aaasLdapPasswdHash = _AaasLdapPasswdHash_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 1, 1, 1, 1, 59),
    _AaasLdapPasswdHash_Type()
)
aaasLdapPasswdHash.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aaasLdapPasswdHash.setStatus("current")


class _AaaTacacsServerCmdAuthorization_Type(Integer32):
    """Custom type aaaTacacsServerCmdAuthorization based on Integer32"""
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


_AaaTacacsServerCmdAuthorization_Type.__name__ = "Integer32"
_AaaTacacsServerCmdAuthorization_Object = MibScalar
aaaTacacsServerCmdAuthorization = _AaaTacacsServerCmdAuthorization_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 1, 1, 2),
    _AaaTacacsServerCmdAuthorization_Type()
)
aaaTacacsServerCmdAuthorization.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aaaTacacsServerCmdAuthorization.setStatus("current")


class _AaaTacacsServerWaitTime_Type(Integer32):
    """Custom type aaaTacacsServerWaitTime based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 200),
    )


_AaaTacacsServerWaitTime_Type.__name__ = "Integer32"
_AaaTacacsServerWaitTime_Object = MibScalar
aaaTacacsServerWaitTime = _AaaTacacsServerWaitTime_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 1, 1, 3),
    _AaaTacacsServerWaitTime_Type()
)
aaaTacacsServerWaitTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aaaTacacsServerWaitTime.setStatus("current")
_AaaAuthAcctMIB_ObjectIdentity = ObjectIdentity
aaaAuthAcctMIB = _AaaAuthAcctMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 1, 2)
)
_AaaAuthVlanTable_Object = MibTable
aaaAuthVlanTable = _AaaAuthVlanTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 1, 2, 1)
)
if mibBuilder.loadTexts:
    aaaAuthVlanTable.setStatus("current")
_AaaAuthVlanEntry_Object = MibTableRow
aaaAuthVlanEntry = _AaaAuthVlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 1, 2, 1, 1)
)
aaaAuthVlanEntry.setIndexNames(
    (0, "ALCATEL-IND1-AAA-MIB", "aaatvVlan"),
)
if mibBuilder.loadTexts:
    aaaAuthVlanEntry.setStatus("current")


class _AaatvVlan_Type(Integer32):
    """Custom type aaatvVlan based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AaatvVlan_Type.__name__ = "Integer32"
_AaatvVlan_Object = MibTableColumn
aaatvVlan = _AaatvVlan_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 1, 2, 1, 1, 1),
    _AaatvVlan_Type()
)
aaatvVlan.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aaatvVlan.setStatus("current")


class _AaatvName1_Type(DisplayString):
    """Custom type aaatvName1 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AaatvName1_Type.__name__ = "DisplayString"
_AaatvName1_Object = MibTableColumn
aaatvName1 = _AaatvName1_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 1, 2, 1, 1, 2),
    _AaatvName1_Type()
)
aaatvName1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aaatvName1.setStatus("current")


class _AaatvName2_Type(DisplayString):
    """Custom type aaatvName2 based on DisplayString"""
    defaultValue = OctetString("")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AaatvName2_Type.__name__ = "DisplayString"
_AaatvName2_Object = MibTableColumn
aaatvName2 = _AaatvName2_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 1, 2, 1, 1, 3),
    _AaatvName2_Type()
)
aaatvName2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aaatvName2.setStatus("current")


class _AaatvName3_Type(DisplayString):
    """Custom type aaatvName3 based on DisplayString"""
    defaultValue = OctetString("")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AaatvName3_Type.__name__ = "DisplayString"
_AaatvName3_Object = MibTableColumn
aaatvName3 = _AaatvName3_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 1, 2, 1, 1, 4),
    _AaatvName3_Type()
)
aaatvName3.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aaatvName3.setStatus("current")


class _AaatvName4_Type(DisplayString):
    """Custom type aaatvName4 based on DisplayString"""
    defaultValue = OctetString("")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AaatvName4_Type.__name__ = "DisplayString"
_AaatvName4_Object = MibTableColumn
aaatvName4 = _AaatvName4_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 1, 2, 1, 1, 5),
    _AaatvName4_Type()
)
aaatvName4.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aaatvName4.setStatus("current")


class _AaatvRowStatus_Type(RowStatus):
    """Custom type aaatvRowStatus based on RowStatus"""
    defaultValue = 2


_AaatvRowStatus_Type.__name__ = "RowStatus"
_AaatvRowStatus_Object = MibTableColumn
aaatvRowStatus = _AaatvRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 1, 2, 1, 1, 6),
    _AaatvRowStatus_Type()
)
aaatvRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aaatvRowStatus.setStatus("current")


class _AaatvCertificate_Type(Integer32):
    """Custom type aaatvCertificate based on Integer32"""
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
        *(("noCertificate", 0),
          ("certificateOnly", 1),
          ("certificateWithPassword", 2))
    )


_AaatvCertificate_Type.__name__ = "Integer32"
_AaatvCertificate_Object = MibTableColumn
aaatvCertificate = _AaatvCertificate_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 1, 2, 1, 1, 7),
    _AaatvCertificate_Type()
)
aaatvCertificate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aaatvCertificate.setStatus("current")
_AaaAuthSATable_Object = MibTable
aaaAuthSATable = _AaaAuthSATable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 1, 2, 2)
)
if mibBuilder.loadTexts:
    aaaAuthSATable.setStatus("current")
_AaaAuthSAEntry_Object = MibTableRow
aaaAuthSAEntry = _AaaAuthSAEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 1, 2, 2, 1)
)
aaaAuthSAEntry.setIndexNames(
    (0, "ALCATEL-IND1-AAA-MIB", "aaatsInterface"),
)
if mibBuilder.loadTexts:
    aaaAuthSAEntry.setStatus("current")


class _AaatsInterface_Type(Integer32):
    """Custom type aaatsInterface based on Integer32"""
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
        *(("default", 1),
          ("console", 2),
          ("telnet", 3),
          ("ftp", 4),
          ("http", 5),
          ("snmp", 6),
          ("ssh", 7))
    )


_AaatsInterface_Type.__name__ = "Integer32"
_AaatsInterface_Object = MibTableColumn
aaatsInterface = _AaatsInterface_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 1, 2, 2, 1, 1),
    _AaatsInterface_Type()
)
aaatsInterface.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aaatsInterface.setStatus("current")


class _AaatsName1_Type(DisplayString):
    """Custom type aaatsName1 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AaatsName1_Type.__name__ = "DisplayString"
_AaatsName1_Object = MibTableColumn
aaatsName1 = _AaatsName1_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 1, 2, 2, 1, 2),
    _AaatsName1_Type()
)
aaatsName1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aaatsName1.setStatus("current")


class _AaatsName2_Type(DisplayString):
    """Custom type aaatsName2 based on DisplayString"""
    defaultValue = OctetString("")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AaatsName2_Type.__name__ = "DisplayString"
_AaatsName2_Object = MibTableColumn
aaatsName2 = _AaatsName2_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 1, 2, 2, 1, 3),
    _AaatsName2_Type()
)
aaatsName2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aaatsName2.setStatus("current")


class _AaatsName3_Type(DisplayString):
    """Custom type aaatsName3 based on DisplayString"""
    defaultValue = OctetString("")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AaatsName3_Type.__name__ = "DisplayString"
_AaatsName3_Object = MibTableColumn
aaatsName3 = _AaatsName3_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 1, 2, 2, 1, 4),
    _AaatsName3_Type()
)
aaatsName3.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aaatsName3.setStatus("current")


class _AaatsName4_Type(DisplayString):
    """Custom type aaatsName4 based on DisplayString"""
    defaultValue = OctetString("")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AaatsName4_Type.__name__ = "DisplayString"
_AaatsName4_Object = MibTableColumn
aaatsName4 = _AaatsName4_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 1, 2, 2, 1, 5),
    _AaatsName4_Type()
)
aaatsName4.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aaatsName4.setStatus("current")


class _AaatsName5_Type(DisplayString):
    """Custom type aaatsName5 based on DisplayString"""
    defaultValue = OctetString("")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AaatsName5_Type.__name__ = "DisplayString"
_AaatsName5_Object = MibTableColumn
aaatsName5 = _AaatsName5_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 1, 2, 2, 1, 6),
    _AaatsName5_Type()
)
aaatsName5.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aaatsName5.setStatus("current")


class _AaatsRowStatus_Type(RowStatus):
    """Custom type aaatsRowStatus based on RowStatus"""
    defaultValue = 2


_AaatsRowStatus_Type.__name__ = "RowStatus"
_AaatsRowStatus_Object = MibTableColumn
aaatsRowStatus = _AaatsRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 1, 2, 2, 1, 7),
    _AaatsRowStatus_Type()
)
aaatsRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aaatsRowStatus.setStatus("current")


class _AaatsCertificate_Type(Integer32):
    """Custom type aaatsCertificate based on Integer32"""
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
        *(("noCertificate", 0),
          ("certificateOnly", 1),
          ("certificateWithPassword", 2))
    )


_AaatsCertificate_Type.__name__ = "Integer32"
_AaatsCertificate_Object = MibTableColumn
aaatsCertificate = _AaatsCertificate_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 1, 2, 2, 1, 8),
    _AaatsCertificate_Type()
)
aaatsCertificate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aaatsCertificate.setStatus("current")
_AaaAcctVlanTable_Object = MibTable
aaaAcctVlanTable = _AaaAcctVlanTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 1, 2, 3)
)
if mibBuilder.loadTexts:
    aaaAcctVlanTable.setStatus("current")
_AaaAcctVlanEntry_Object = MibTableRow
aaaAcctVlanEntry = _AaaAcctVlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 1, 2, 3, 1)
)
aaaAcctVlanEntry.setIndexNames(
    (0, "ALCATEL-IND1-AAA-MIB", "aaacvVlan"),
)
if mibBuilder.loadTexts:
    aaaAcctVlanEntry.setStatus("current")


class _AaacvVlan_Type(Integer32):
    """Custom type aaacvVlan based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AaacvVlan_Type.__name__ = "Integer32"
_AaacvVlan_Object = MibTableColumn
aaacvVlan = _AaacvVlan_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 1, 2, 3, 1, 1),
    _AaacvVlan_Type()
)
aaacvVlan.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aaacvVlan.setStatus("current")


class _AaacvName1_Type(DisplayString):
    """Custom type aaacvName1 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AaacvName1_Type.__name__ = "DisplayString"
_AaacvName1_Object = MibTableColumn
aaacvName1 = _AaacvName1_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 1, 2, 3, 1, 2),
    _AaacvName1_Type()
)
aaacvName1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aaacvName1.setStatus("current")


class _AaacvName2_Type(DisplayString):
    """Custom type aaacvName2 based on DisplayString"""
    defaultValue = OctetString("")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AaacvName2_Type.__name__ = "DisplayString"
_AaacvName2_Object = MibTableColumn
aaacvName2 = _AaacvName2_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 1, 2, 3, 1, 3),
    _AaacvName2_Type()
)
aaacvName2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aaacvName2.setStatus("current")


class _AaacvName3_Type(DisplayString):
    """Custom type aaacvName3 based on DisplayString"""
    defaultValue = OctetString("")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AaacvName3_Type.__name__ = "DisplayString"
_AaacvName3_Object = MibTableColumn
aaacvName3 = _AaacvName3_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 1, 2, 3, 1, 4),
    _AaacvName3_Type()
)
aaacvName3.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aaacvName3.setStatus("current")


class _AaacvName4_Type(DisplayString):
    """Custom type aaacvName4 based on DisplayString"""
    defaultValue = OctetString("")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AaacvName4_Type.__name__ = "DisplayString"
_AaacvName4_Object = MibTableColumn
aaacvName4 = _AaacvName4_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 1, 2, 3, 1, 5),
    _AaacvName4_Type()
)
aaacvName4.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aaacvName4.setStatus("current")


class _AaacvRowStatus_Type(RowStatus):
    """Custom type aaacvRowStatus based on RowStatus"""
    defaultValue = 2


_AaacvRowStatus_Type.__name__ = "RowStatus"
_AaacvRowStatus_Object = MibTableColumn
aaacvRowStatus = _AaacvRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 1, 2, 3, 1, 6),
    _AaacvRowStatus_Type()
)
aaacvRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aaacvRowStatus.setStatus("current")
_AaaAcctSATable_Object = MibTable
aaaAcctSATable = _AaaAcctSATable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 1, 2, 4)
)
if mibBuilder.loadTexts:
    aaaAcctSATable.setStatus("current")
_AaaAcctSAEntry_Object = MibTableRow
aaaAcctSAEntry = _AaaAcctSAEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 1, 2, 4, 1)
)
aaaAcctSAEntry.setIndexNames(
    (0, "ALCATEL-IND1-AAA-MIB", "aaacsInterface"),
)
if mibBuilder.loadTexts:
    aaaAcctSAEntry.setStatus("current")


class _AaacsInterface_Type(Integer32):
    """Custom type aaacsInterface based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
    )


_AaacsInterface_Type.__name__ = "Integer32"
_AaacsInterface_Object = MibTableColumn
aaacsInterface = _AaacsInterface_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 1, 2, 4, 1, 1),
    _AaacsInterface_Type()
)
aaacsInterface.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aaacsInterface.setStatus("current")


class _AaacsName1_Type(DisplayString):
    """Custom type aaacsName1 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AaacsName1_Type.__name__ = "DisplayString"
_AaacsName1_Object = MibTableColumn
aaacsName1 = _AaacsName1_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 1, 2, 4, 1, 2),
    _AaacsName1_Type()
)
aaacsName1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aaacsName1.setStatus("current")


class _AaacsName2_Type(DisplayString):
    """Custom type aaacsName2 based on DisplayString"""
    defaultValue = OctetString("")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AaacsName2_Type.__name__ = "DisplayString"
_AaacsName2_Object = MibTableColumn
aaacsName2 = _AaacsName2_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 1, 2, 4, 1, 3),
    _AaacsName2_Type()
)
aaacsName2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aaacsName2.setStatus("current")


class _AaacsName3_Type(DisplayString):
    """Custom type aaacsName3 based on DisplayString"""
    defaultValue = OctetString("")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AaacsName3_Type.__name__ = "DisplayString"
_AaacsName3_Object = MibTableColumn
aaacsName3 = _AaacsName3_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 1, 2, 4, 1, 4),
    _AaacsName3_Type()
)
aaacsName3.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aaacsName3.setStatus("current")


class _AaacsName4_Type(DisplayString):
    """Custom type aaacsName4 based on DisplayString"""
    defaultValue = OctetString("")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AaacsName4_Type.__name__ = "DisplayString"
_AaacsName4_Object = MibTableColumn
aaacsName4 = _AaacsName4_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 1, 2, 4, 1, 5),
    _AaacsName4_Type()
)
aaacsName4.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aaacsName4.setStatus("current")


class _AaacsRowStatus_Type(RowStatus):
    """Custom type aaacsRowStatus based on RowStatus"""
    defaultValue = 2


_AaacsRowStatus_Type.__name__ = "RowStatus"
_AaacsRowStatus_Object = MibTableColumn
aaacsRowStatus = _AaacsRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 1, 2, 4, 1, 6),
    _AaacsRowStatus_Type()
)
aaacsRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aaacsRowStatus.setStatus("current")


class _AaaAccountingSessionIdStatus_Type(Integer32):
    """Custom type aaaAccountingSessionIdStatus based on Integer32"""
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


_AaaAccountingSessionIdStatus_Type.__name__ = "Integer32"
_AaaAccountingSessionIdStatus_Object = MibTableColumn
aaaAccountingSessionIdStatus = _AaaAccountingSessionIdStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 1, 2, 4, 1, 7),
    _AaaAccountingSessionIdStatus_Type()
)
aaaAccountingSessionIdStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aaaAccountingSessionIdStatus.setStatus("current")


class _AaacsName5_Type(DisplayString):
    """Custom type aaacsName5 based on DisplayString"""
    defaultValue = OctetString("")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AaacsName5_Type.__name__ = "DisplayString"
_AaacsName5_Object = MibTableColumn
aaacsName5 = _AaacsName5_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 1, 2, 4, 1, 8),
    _AaacsName5_Type()
)
aaacsName5.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aaacsName5.setStatus("current")
_AaaAuth8021xTable_Object = MibTable
aaaAuth8021xTable = _AaaAuth8021xTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 1, 2, 5)
)
if mibBuilder.loadTexts:
    aaaAuth8021xTable.setStatus("current")
_AaaAuth8021xEntry_Object = MibTableRow
aaaAuth8021xEntry = _AaaAuth8021xEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 1, 2, 5, 1)
)
aaaAuth8021xEntry.setIndexNames(
    (0, "ALCATEL-IND1-AAA-MIB", "aaatxInterface"),
)
if mibBuilder.loadTexts:
    aaaAuth8021xEntry.setStatus("current")


class _AaatxInterface_Type(Integer32):
    """Custom type aaatxInterface based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
    )


_AaatxInterface_Type.__name__ = "Integer32"
_AaatxInterface_Object = MibTableColumn
aaatxInterface = _AaatxInterface_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 1, 2, 5, 1, 1),
    _AaatxInterface_Type()
)
aaatxInterface.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aaatxInterface.setStatus("current")


class _AaatxName1_Type(DisplayString):
    """Custom type aaatxName1 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AaatxName1_Type.__name__ = "DisplayString"
_AaatxName1_Object = MibTableColumn
aaatxName1 = _AaatxName1_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 1, 2, 5, 1, 2),
    _AaatxName1_Type()
)
aaatxName1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aaatxName1.setStatus("current")


class _AaatxName2_Type(DisplayString):
    """Custom type aaatxName2 based on DisplayString"""
    defaultValue = OctetString("")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AaatxName2_Type.__name__ = "DisplayString"
_AaatxName2_Object = MibTableColumn
aaatxName2 = _AaatxName2_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 1, 2, 5, 1, 3),
    _AaatxName2_Type()
)
aaatxName2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aaatxName2.setStatus("current")


class _AaatxName3_Type(DisplayString):
    """Custom type aaatxName3 based on DisplayString"""
    defaultValue = OctetString("")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AaatxName3_Type.__name__ = "DisplayString"
_AaatxName3_Object = MibTableColumn
aaatxName3 = _AaatxName3_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 1, 2, 5, 1, 4),
    _AaatxName3_Type()
)
aaatxName3.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aaatxName3.setStatus("current")


class _AaatxName4_Type(DisplayString):
    """Custom type aaatxName4 based on DisplayString"""
    defaultValue = OctetString("")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AaatxName4_Type.__name__ = "DisplayString"
_AaatxName4_Object = MibTableColumn
aaatxName4 = _AaatxName4_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 1, 2, 5, 1, 5),
    _AaatxName4_Type()
)
aaatxName4.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aaatxName4.setStatus("current")


class _AaatxOpen_Type(Integer32):
    """Custom type aaatxOpen based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("global", 1),
          ("unique", 2))
    )


_AaatxOpen_Type.__name__ = "Integer32"
_AaatxOpen_Object = MibTableColumn
aaatxOpen = _AaatxOpen_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 1, 2, 5, 1, 6),
    _AaatxOpen_Type()
)
aaatxOpen.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aaatxOpen.setStatus("current")


class _AaatxRowStatus_Type(RowStatus):
    """Custom type aaatxRowStatus based on RowStatus"""
    defaultValue = 2


_AaatxRowStatus_Type.__name__ = "RowStatus"
_AaatxRowStatus_Object = MibTableColumn
aaatxRowStatus = _AaatxRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 1, 2, 5, 1, 7),
    _AaatxRowStatus_Type()
)
aaatxRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aaatxRowStatus.setStatus("current")


class _AaatxName5_Type(DisplayString):
    """Custom type aaatxName5 based on DisplayString"""
    defaultValue = OctetString("")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AaatxName5_Type.__name__ = "DisplayString"
_AaatxName5_Object = MibTableColumn
aaatxName5 = _AaatxName5_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 1, 2, 5, 1, 8),
    _AaatxName5_Type()
)
aaatxName5.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aaatxName5.setStatus("current")
_AaaAcct8021xTable_Object = MibTable
aaaAcct8021xTable = _AaaAcct8021xTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 1, 2, 6)
)
if mibBuilder.loadTexts:
    aaaAcct8021xTable.setStatus("current")
_AaaAcct8021xEntry_Object = MibTableRow
aaaAcct8021xEntry = _AaaAcct8021xEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 1, 2, 6, 1)
)
aaaAcct8021xEntry.setIndexNames(
    (0, "ALCATEL-IND1-AAA-MIB", "aaacxInterface"),
)
if mibBuilder.loadTexts:
    aaaAcct8021xEntry.setStatus("current")


class _AaacxInterface_Type(Integer32):
    """Custom type aaacxInterface based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
    )


_AaacxInterface_Type.__name__ = "Integer32"
_AaacxInterface_Object = MibTableColumn
aaacxInterface = _AaacxInterface_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 1, 2, 6, 1, 1),
    _AaacxInterface_Type()
)
aaacxInterface.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aaacxInterface.setStatus("current")


class _AaacxName1_Type(DisplayString):
    """Custom type aaacxName1 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AaacxName1_Type.__name__ = "DisplayString"
_AaacxName1_Object = MibTableColumn
aaacxName1 = _AaacxName1_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 1, 2, 6, 1, 2),
    _AaacxName1_Type()
)
aaacxName1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aaacxName1.setStatus("current")


class _AaacxName2_Type(DisplayString):
    """Custom type aaacxName2 based on DisplayString"""
    defaultValue = OctetString("")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AaacxName2_Type.__name__ = "DisplayString"
_AaacxName2_Object = MibTableColumn
aaacxName2 = _AaacxName2_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 1, 2, 6, 1, 3),
    _AaacxName2_Type()
)
aaacxName2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aaacxName2.setStatus("current")


class _AaacxName3_Type(DisplayString):
    """Custom type aaacxName3 based on DisplayString"""
    defaultValue = OctetString("")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AaacxName3_Type.__name__ = "DisplayString"
_AaacxName3_Object = MibTableColumn
aaacxName3 = _AaacxName3_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 1, 2, 6, 1, 4),
    _AaacxName3_Type()
)
aaacxName3.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aaacxName3.setStatus("current")


class _AaacxName4_Type(DisplayString):
    """Custom type aaacxName4 based on DisplayString"""
    defaultValue = OctetString("")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AaacxName4_Type.__name__ = "DisplayString"
_AaacxName4_Object = MibTableColumn
aaacxName4 = _AaacxName4_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 1, 2, 6, 1, 5),
    _AaacxName4_Type()
)
aaacxName4.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aaacxName4.setStatus("current")


class _AaacxRowStatus_Type(RowStatus):
    """Custom type aaacxRowStatus based on RowStatus"""
    defaultValue = 2


_AaacxRowStatus_Type.__name__ = "RowStatus"
_AaacxRowStatus_Object = MibTableColumn
aaacxRowStatus = _AaacxRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 1, 2, 6, 1, 6),
    _AaacxRowStatus_Type()
)
aaacxRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aaacxRowStatus.setStatus("current")


class _AaacxName5_Type(DisplayString):
    """Custom type aaacxName5 based on DisplayString"""
    defaultValue = OctetString("")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AaacxName5_Type.__name__ = "DisplayString"
_AaacxName5_Object = MibTableColumn
aaacxName5 = _AaacxName5_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 1, 2, 6, 1, 7),
    _AaacxName5_Type()
)
aaacxName5.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aaacxName5.setStatus("current")
_AaaPkiTable_Object = MibTable
aaaPkiTable = _AaaPkiTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 1, 2, 7)
)
if mibBuilder.loadTexts:
    aaaPkiTable.setStatus("current")
_AaaPkiEntry_Object = MibTableRow
aaaPkiEntry = _AaaPkiEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 1, 2, 7, 1)
)
aaaPkiEntry.setIndexNames(
    (0, "ALCATEL-IND1-AAA-MIB", "aaatpInterface"),
)
if mibBuilder.loadTexts:
    aaaPkiEntry.setStatus("current")


class _AaatpInterface_Type(Integer32):
    """Custom type aaatpInterface based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
    )


_AaatpInterface_Type.__name__ = "Integer32"
_AaatpInterface_Object = MibTableColumn
aaatpInterface = _AaatpInterface_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 1, 2, 7, 1, 1),
    _AaatpInterface_Type()
)
aaatpInterface.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aaatpInterface.setStatus("current")


class _AaatpName1_Type(DisplayString):
    """Custom type aaatpName1 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AaatpName1_Type.__name__ = "DisplayString"
_AaatpName1_Object = MibTableColumn
aaatpName1 = _AaatpName1_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 1, 2, 7, 1, 2),
    _AaatpName1_Type()
)
aaatpName1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aaatpName1.setStatus("current")


class _AaatpName2_Type(DisplayString):
    """Custom type aaatpName2 based on DisplayString"""
    defaultValue = OctetString("")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AaatpName2_Type.__name__ = "DisplayString"
_AaatpName2_Object = MibTableColumn
aaatpName2 = _AaatpName2_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 1, 2, 7, 1, 3),
    _AaatpName2_Type()
)
aaatpName2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aaatpName2.setStatus("current")


class _AaatpName3_Type(DisplayString):
    """Custom type aaatpName3 based on DisplayString"""
    defaultValue = OctetString("")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AaatpName3_Type.__name__ = "DisplayString"
_AaatpName3_Object = MibTableColumn
aaatpName3 = _AaatpName3_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 1, 2, 7, 1, 4),
    _AaatpName3_Type()
)
aaatpName3.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aaatpName3.setStatus("current")


class _AaatpName4_Type(DisplayString):
    """Custom type aaatpName4 based on DisplayString"""
    defaultValue = OctetString("")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AaatpName4_Type.__name__ = "DisplayString"
_AaatpName4_Object = MibTableColumn
aaatpName4 = _AaatpName4_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 1, 2, 7, 1, 5),
    _AaatpName4_Type()
)
aaatpName4.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aaatpName4.setStatus("current")


class _AaatpLevel_Type(Integer32):
    """Custom type aaatpLevel based on Integer32"""
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
        *(("certificate", 1),
          ("notRevoked", 2),
          ("repository", 3))
    )


_AaatpLevel_Type.__name__ = "Integer32"
_AaatpLevel_Object = MibTableColumn
aaatpLevel = _AaatpLevel_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 1, 2, 7, 1, 6),
    _AaatpLevel_Type()
)
aaatpLevel.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aaatpLevel.setStatus("current")


class _AaatpRowStatus_Type(RowStatus):
    """Custom type aaatpRowStatus based on RowStatus"""
    defaultValue = 2


_AaatpRowStatus_Type.__name__ = "RowStatus"
_AaatpRowStatus_Object = MibTableColumn
aaatpRowStatus = _AaatpRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 1, 2, 7, 1, 7),
    _AaatpRowStatus_Type()
)
aaatpRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aaatpRowStatus.setStatus("current")
_AaaAuthMACTable_Object = MibTable
aaaAuthMACTable = _AaaAuthMACTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 1, 2, 8)
)
if mibBuilder.loadTexts:
    aaaAuthMACTable.setStatus("current")
_AaaAuthMACEntry_Object = MibTableRow
aaaAuthMACEntry = _AaaAuthMACEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 1, 2, 8, 1)
)
aaaAuthMACEntry.setIndexNames(
    (0, "ALCATEL-IND1-AAA-MIB", "aaatxInterface"),
)
if mibBuilder.loadTexts:
    aaaAuthMACEntry.setStatus("current")


class _AaaMacInterface_Type(Integer32):
    """Custom type aaaMacInterface based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
    )


_AaaMacInterface_Type.__name__ = "Integer32"
_AaaMacInterface_Object = MibTableColumn
aaaMacInterface = _AaaMacInterface_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 1, 2, 8, 1, 1),
    _AaaMacInterface_Type()
)
aaaMacInterface.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aaaMacInterface.setStatus("current")


class _AaaMacSrvrName1_Type(DisplayString):
    """Custom type aaaMacSrvrName1 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AaaMacSrvrName1_Type.__name__ = "DisplayString"
_AaaMacSrvrName1_Object = MibTableColumn
aaaMacSrvrName1 = _AaaMacSrvrName1_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 1, 2, 8, 1, 2),
    _AaaMacSrvrName1_Type()
)
aaaMacSrvrName1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aaaMacSrvrName1.setStatus("current")


class _AaaMacSrvrName2_Type(DisplayString):
    """Custom type aaaMacSrvrName2 based on DisplayString"""
    defaultValue = OctetString("")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AaaMacSrvrName2_Type.__name__ = "DisplayString"
_AaaMacSrvrName2_Object = MibTableColumn
aaaMacSrvrName2 = _AaaMacSrvrName2_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 1, 2, 8, 1, 3),
    _AaaMacSrvrName2_Type()
)
aaaMacSrvrName2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aaaMacSrvrName2.setStatus("current")


class _AaaMacSrvrName3_Type(DisplayString):
    """Custom type aaaMacSrvrName3 based on DisplayString"""
    defaultValue = OctetString("")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AaaMacSrvrName3_Type.__name__ = "DisplayString"
_AaaMacSrvrName3_Object = MibTableColumn
aaaMacSrvrName3 = _AaaMacSrvrName3_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 1, 2, 8, 1, 4),
    _AaaMacSrvrName3_Type()
)
aaaMacSrvrName3.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aaaMacSrvrName3.setStatus("current")


class _AaaMacSrvrName4_Type(DisplayString):
    """Custom type aaaMacSrvrName4 based on DisplayString"""
    defaultValue = OctetString("")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AaaMacSrvrName4_Type.__name__ = "DisplayString"
_AaaMacSrvrName4_Object = MibTableColumn
aaaMacSrvrName4 = _AaaMacSrvrName4_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 1, 2, 8, 1, 5),
    _AaaMacSrvrName4_Type()
)
aaaMacSrvrName4.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aaaMacSrvrName4.setStatus("current")


class _AaaMacSrvrRowStatus_Type(RowStatus):
    """Custom type aaaMacSrvrRowStatus based on RowStatus"""
    defaultValue = 2


_AaaMacSrvrRowStatus_Type.__name__ = "RowStatus"
_AaaMacSrvrRowStatus_Object = MibTableColumn
aaaMacSrvrRowStatus = _AaaMacSrvrRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 1, 2, 8, 1, 6),
    _AaaMacSrvrRowStatus_Type()
)
aaaMacSrvrRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aaaMacSrvrRowStatus.setStatus("current")


class _AaaMacSrvrName5_Type(DisplayString):
    """Custom type aaaMacSrvrName5 based on DisplayString"""
    defaultValue = OctetString("")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AaaMacSrvrName5_Type.__name__ = "DisplayString"
_AaaMacSrvrName5_Object = MibTableColumn
aaaMacSrvrName5 = _AaaMacSrvrName5_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 1, 2, 8, 1, 7),
    _AaaMacSrvrName5_Type()
)
aaaMacSrvrName5.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aaaMacSrvrName5.setStatus("current")
_AaaAcctCmdTable_Object = MibTable
aaaAcctCmdTable = _AaaAcctCmdTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 1, 2, 9)
)
if mibBuilder.loadTexts:
    aaaAcctCmdTable.setStatus("current")
_AaaAcctCmdEntry_Object = MibTableRow
aaaAcctCmdEntry = _AaaAcctCmdEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 1, 2, 9, 1)
)
aaaAcctCmdEntry.setIndexNames(
    (0, "ALCATEL-IND1-AAA-MIB", "aaacmdInterface"),
)
if mibBuilder.loadTexts:
    aaaAcctCmdEntry.setStatus("current")


class _AaacmdInterface_Type(Integer32):
    """Custom type aaacmdInterface based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
    )


_AaacmdInterface_Type.__name__ = "Integer32"
_AaacmdInterface_Object = MibTableColumn
aaacmdInterface = _AaacmdInterface_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 1, 2, 9, 1, 1),
    _AaacmdInterface_Type()
)
aaacmdInterface.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aaacmdInterface.setStatus("current")


class _AaacmdSrvName1_Type(DisplayString):
    """Custom type aaacmdSrvName1 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AaacmdSrvName1_Type.__name__ = "DisplayString"
_AaacmdSrvName1_Object = MibTableColumn
aaacmdSrvName1 = _AaacmdSrvName1_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 1, 2, 9, 1, 2),
    _AaacmdSrvName1_Type()
)
aaacmdSrvName1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aaacmdSrvName1.setStatus("current")


class _AaacmdSrvName2_Type(DisplayString):
    """Custom type aaacmdSrvName2 based on DisplayString"""
    defaultValue = OctetString("")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AaacmdSrvName2_Type.__name__ = "DisplayString"
_AaacmdSrvName2_Object = MibTableColumn
aaacmdSrvName2 = _AaacmdSrvName2_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 1, 2, 9, 1, 3),
    _AaacmdSrvName2_Type()
)
aaacmdSrvName2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aaacmdSrvName2.setStatus("current")


class _AaacmdSrvName3_Type(DisplayString):
    """Custom type aaacmdSrvName3 based on DisplayString"""
    defaultValue = OctetString("")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AaacmdSrvName3_Type.__name__ = "DisplayString"
_AaacmdSrvName3_Object = MibTableColumn
aaacmdSrvName3 = _AaacmdSrvName3_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 1, 2, 9, 1, 4),
    _AaacmdSrvName3_Type()
)
aaacmdSrvName3.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aaacmdSrvName3.setStatus("current")


class _AaacmdSrvName4_Type(DisplayString):
    """Custom type aaacmdSrvName4 based on DisplayString"""
    defaultValue = OctetString("")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AaacmdSrvName4_Type.__name__ = "DisplayString"
_AaacmdSrvName4_Object = MibTableColumn
aaacmdSrvName4 = _AaacmdSrvName4_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 1, 2, 9, 1, 5),
    _AaacmdSrvName4_Type()
)
aaacmdSrvName4.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aaacmdSrvName4.setStatus("current")


class _AaacmdRowStatus_Type(RowStatus):
    """Custom type aaacmdRowStatus based on RowStatus"""
    defaultValue = 2


_AaacmdRowStatus_Type.__name__ = "RowStatus"
_AaacmdRowStatus_Object = MibTableColumn
aaacmdRowStatus = _AaacmdRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 1, 2, 9, 1, 6),
    _AaacmdRowStatus_Type()
)
aaacmdRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aaacmdRowStatus.setStatus("current")


class _AaacmdSrvName5_Type(DisplayString):
    """Custom type aaacmdSrvName5 based on DisplayString"""
    defaultValue = OctetString("")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AaacmdSrvName5_Type.__name__ = "DisplayString"
_AaacmdSrvName5_Object = MibTableColumn
aaacmdSrvName5 = _AaacmdSrvName5_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 1, 2, 9, 1, 7),
    _AaacmdSrvName5_Type()
)
aaacmdSrvName5.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aaacmdSrvName5.setStatus("current")
_AaaAcctMACTable_Object = MibTable
aaaAcctMACTable = _AaaAcctMACTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 1, 2, 10)
)
if mibBuilder.loadTexts:
    aaaAcctMACTable.setStatus("current")
_AaaAcctMACEntry_Object = MibTableRow
aaaAcctMACEntry = _AaaAcctMACEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 1, 2, 10, 1)
)
aaaAcctMACEntry.setIndexNames(
    (0, "ALCATEL-IND1-AAA-MIB", "aaaAcctSvrInterface"),
)
if mibBuilder.loadTexts:
    aaaAcctMACEntry.setStatus("current")


class _AaaAcctSvrInterface_Type(Integer32):
    """Custom type aaaAcctSvrInterface based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
    )


_AaaAcctSvrInterface_Type.__name__ = "Integer32"
_AaaAcctSvrInterface_Object = MibTableColumn
aaaAcctSvrInterface = _AaaAcctSvrInterface_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 1, 2, 10, 1, 1),
    _AaaAcctSvrInterface_Type()
)
aaaAcctSvrInterface.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aaaAcctSvrInterface.setStatus("current")


class _AaaAcctSvr1_Type(SnmpAdminString):
    """Custom type aaaAcctSvr1 based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AaaAcctSvr1_Type.__name__ = "SnmpAdminString"
_AaaAcctSvr1_Object = MibTableColumn
aaaAcctSvr1 = _AaaAcctSvr1_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 1, 2, 10, 1, 2),
    _AaaAcctSvr1_Type()
)
aaaAcctSvr1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aaaAcctSvr1.setStatus("current")


class _AaaAcctSvr2_Type(SnmpAdminString):
    """Custom type aaaAcctSvr2 based on SnmpAdminString"""
    defaultValue = OctetString("")

    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AaaAcctSvr2_Type.__name__ = "SnmpAdminString"
_AaaAcctSvr2_Object = MibTableColumn
aaaAcctSvr2 = _AaaAcctSvr2_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 1, 2, 10, 1, 3),
    _AaaAcctSvr2_Type()
)
aaaAcctSvr2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aaaAcctSvr2.setStatus("current")


class _AaaAcctSvr3_Type(SnmpAdminString):
    """Custom type aaaAcctSvr3 based on SnmpAdminString"""
    defaultValue = OctetString("")

    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AaaAcctSvr3_Type.__name__ = "SnmpAdminString"
_AaaAcctSvr3_Object = MibTableColumn
aaaAcctSvr3 = _AaaAcctSvr3_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 1, 2, 10, 1, 4),
    _AaaAcctSvr3_Type()
)
aaaAcctSvr3.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aaaAcctSvr3.setStatus("current")


class _AaaAcctSvr4_Type(SnmpAdminString):
    """Custom type aaaAcctSvr4 based on SnmpAdminString"""
    defaultValue = OctetString("")

    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AaaAcctSvr4_Type.__name__ = "SnmpAdminString"
_AaaAcctSvr4_Object = MibTableColumn
aaaAcctSvr4 = _AaaAcctSvr4_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 1, 2, 10, 1, 5),
    _AaaAcctSvr4_Type()
)
aaaAcctSvr4.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aaaAcctSvr4.setStatus("current")


class _AaaAcctSvrRowStatus_Type(RowStatus):
    """Custom type aaaAcctSvrRowStatus based on RowStatus"""
    defaultValue = 2


_AaaAcctSvrRowStatus_Type.__name__ = "RowStatus"
_AaaAcctSvrRowStatus_Object = MibTableColumn
aaaAcctSvrRowStatus = _AaaAcctSvrRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 1, 2, 10, 1, 6),
    _AaaAcctSvrRowStatus_Type()
)
aaaAcctSvrRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aaaAcctSvrRowStatus.setStatus("current")


class _AaaAcctSvr5_Type(SnmpAdminString):
    """Custom type aaaAcctSvr5 based on SnmpAdminString"""
    defaultValue = OctetString("")

    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AaaAcctSvr5_Type.__name__ = "SnmpAdminString"
_AaaAcctSvr5_Object = MibTableColumn
aaaAcctSvr5 = _AaaAcctSvr5_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 1, 2, 10, 1, 7),
    _AaaAcctSvr5_Type()
)
aaaAcctSvr5.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aaaAcctSvr5.setStatus("current")
_AaaUserMIB_ObjectIdentity = ObjectIdentity
aaaUserMIB = _AaaUserMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 1, 3)
)
_AaaUserTable_Object = MibTable
aaaUserTable = _AaaUserTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 1, 3, 1)
)
if mibBuilder.loadTexts:
    aaaUserTable.setStatus("current")
_AaaUserEntry_Object = MibTableRow
aaaUserEntry = _AaaUserEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 1, 3, 1, 1)
)
aaaUserEntry.setIndexNames(
    (0, "ALCATEL-IND1-AAA-MIB", "aaauUserName"),
)
if mibBuilder.loadTexts:
    aaaUserEntry.setStatus("current")


class _AaauUserName_Type(DisplayString):
    """Custom type aaauUserName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_AaauUserName_Type.__name__ = "DisplayString"
_AaauUserName_Object = MibTableColumn
aaauUserName = _AaauUserName_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 1, 3, 1, 1, 1),
    _AaauUserName_Type()
)
aaauUserName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aaauUserName.setStatus("current")


class _AaauPassword_Type(DisplayString):
    """Custom type aaauPassword based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 47),
    )


_AaauPassword_Type.__name__ = "DisplayString"
_AaauPassword_Object = MibTableColumn
aaauPassword = _AaauPassword_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 1, 3, 1, 1, 2),
    _AaauPassword_Type()
)
aaauPassword.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aaauPassword.setStatus("current")


class _AaauReadRight1_Type(Unsigned32):
    """Custom type aaauReadRight1 based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_AaauReadRight1_Type.__name__ = "Unsigned32"
_AaauReadRight1_Object = MibTableColumn
aaauReadRight1 = _AaauReadRight1_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 1, 3, 1, 1, 3),
    _AaauReadRight1_Type()
)
aaauReadRight1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aaauReadRight1.setStatus("current")


class _AaauReadRight2_Type(Unsigned32):
    """Custom type aaauReadRight2 based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_AaauReadRight2_Type.__name__ = "Unsigned32"
_AaauReadRight2_Object = MibTableColumn
aaauReadRight2 = _AaauReadRight2_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 1, 3, 1, 1, 4),
    _AaauReadRight2_Type()
)
aaauReadRight2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aaauReadRight2.setStatus("current")


class _AaauWriteRight1_Type(Unsigned32):
    """Custom type aaauWriteRight1 based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_AaauWriteRight1_Type.__name__ = "Unsigned32"
_AaauWriteRight1_Object = MibTableColumn
aaauWriteRight1 = _AaauWriteRight1_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 1, 3, 1, 1, 5),
    _AaauWriteRight1_Type()
)
aaauWriteRight1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aaauWriteRight1.setStatus("current")


class _AaauWriteRight2_Type(Unsigned32):
    """Custom type aaauWriteRight2 based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_AaauWriteRight2_Type.__name__ = "Unsigned32"
_AaauWriteRight2_Object = MibTableColumn
aaauWriteRight2 = _AaauWriteRight2_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 1, 3, 1, 1, 6),
    _AaauWriteRight2_Type()
)
aaauWriteRight2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aaauWriteRight2.setStatus("current")


class _AaauProfile_Type(Integer32):
    """Custom type aaauProfile based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AaauProfile_Type.__name__ = "Integer32"
_AaauProfile_Object = MibTableColumn
aaauProfile = _AaauProfile_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 1, 3, 1, 1, 7),
    _AaauProfile_Type()
)
aaauProfile.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aaauProfile.setStatus("obsolete")


class _AaauSnmpLevel_Type(Integer32):
    """Custom type aaauSnmpLevel based on Integer32"""
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
              13,
              14,
              15,
              16,
              17,
              18,
              19,
              20)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("noauth", 2),
          ("sha", 3),
          ("md5", 4),
          ("shaDes", 5),
          ("md5Des", 6),
          ("shaAes", 7),
          ("shaAes192", 8),
          ("shaAes256", 9),
          ("sha3Des", 10),
          ("sha224", 11),
          ("sha256", 12),
          ("sha224Aes", 13),
          ("sha224Aes192", 14),
          ("sha224Aes256", 15),
          ("sha2243Des", 16),
          ("sha256Aes", 17),
          ("sha256Aes192", 18),
          ("sha256Aes256", 19),
          ("sha2563Des", 20))
    )


_AaauSnmpLevel_Type.__name__ = "Integer32"
_AaauSnmpLevel_Object = MibTableColumn
aaauSnmpLevel = _AaauSnmpLevel_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 1, 3, 1, 1, 8),
    _AaauSnmpLevel_Type()
)
aaauSnmpLevel.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aaauSnmpLevel.setStatus("current")


class _AaauSnmpAuthKey_Type(OctetString):
    """Custom type aaauSnmpAuthKey based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_AaauSnmpAuthKey_Type.__name__ = "OctetString"
_AaauSnmpAuthKey_Object = MibTableColumn
aaauSnmpAuthKey = _AaauSnmpAuthKey_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 1, 3, 1, 1, 9),
    _AaauSnmpAuthKey_Type()
)
aaauSnmpAuthKey.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aaauSnmpAuthKey.setStatus("current")


class _AaauRowStatus_Type(RowStatus):
    """Custom type aaauRowStatus based on RowStatus"""
    defaultValue = 2


_AaauRowStatus_Type.__name__ = "RowStatus"
_AaauRowStatus_Object = MibTableColumn
aaauRowStatus = _AaauRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 1, 3, 1, 1, 10),
    _AaauRowStatus_Type()
)
aaauRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aaauRowStatus.setStatus("current")


class _AaauOldPassword_Type(DisplayString):
    """Custom type aaauOldPassword based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 47),
    )


_AaauOldPassword_Type.__name__ = "DisplayString"
_AaauOldPassword_Object = MibTableColumn
aaauOldPassword = _AaauOldPassword_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 1, 3, 1, 1, 11),
    _AaauOldPassword_Type()
)
aaauOldPassword.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aaauOldPassword.setStatus("current")


class _AaauEndUserProfile_Type(DisplayString):
    """Custom type aaauEndUserProfile based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AaauEndUserProfile_Type.__name__ = "DisplayString"
_AaauEndUserProfile_Object = MibTableColumn
aaauEndUserProfile = _AaauEndUserProfile_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 1, 3, 1, 1, 12),
    _AaauEndUserProfile_Type()
)
aaauEndUserProfile.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aaauEndUserProfile.setStatus("current")


class _AaauPasswordExpirationDate_Type(DisplayString):
    """Custom type aaauPasswordExpirationDate based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_AaauPasswordExpirationDate_Type.__name__ = "DisplayString"
_AaauPasswordExpirationDate_Object = MibTableColumn
aaauPasswordExpirationDate = _AaauPasswordExpirationDate_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 1, 3, 1, 1, 13),
    _AaauPasswordExpirationDate_Type()
)
aaauPasswordExpirationDate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aaauPasswordExpirationDate.setStatus("current")


class _AaauPasswordExpirationInMinute_Type(Integer32):
    """Custom type aaauPasswordExpirationInMinute based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 216000),
    )


_AaauPasswordExpirationInMinute_Type.__name__ = "Integer32"
_AaauPasswordExpirationInMinute_Object = MibTableColumn
aaauPasswordExpirationInMinute = _AaauPasswordExpirationInMinute_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 1, 3, 1, 1, 14),
    _AaauPasswordExpirationInMinute_Type()
)
aaauPasswordExpirationInMinute.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aaauPasswordExpirationInMinute.setStatus("current")


class _AaauPasswordAllowModifyDate_Type(DisplayString):
    """Custom type aaauPasswordAllowModifyDate based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_AaauPasswordAllowModifyDate_Type.__name__ = "DisplayString"
_AaauPasswordAllowModifyDate_Object = MibTableColumn
aaauPasswordAllowModifyDate = _AaauPasswordAllowModifyDate_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 1, 3, 1, 1, 15),
    _AaauPasswordAllowModifyDate_Type()
)
aaauPasswordAllowModifyDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aaauPasswordAllowModifyDate.setStatus("current")


class _AaauPasswordLockoutEnable_Type(Integer32):
    """Custom type aaauPasswordLockoutEnable based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("lockout", 1),
          ("unlock", 2),
          ("expired", 3))
    )


_AaauPasswordLockoutEnable_Type.__name__ = "Integer32"
_AaauPasswordLockoutEnable_Object = MibTableColumn
aaauPasswordLockoutEnable = _AaauPasswordLockoutEnable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 1, 3, 1, 1, 16),
    _AaauPasswordLockoutEnable_Type()
)
aaauPasswordLockoutEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aaauPasswordLockoutEnable.setStatus("current")


class _AaauBadAtempts_Type(Integer32):
    """Custom type aaauBadAtempts based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 999),
    )


_AaauBadAtempts_Type.__name__ = "Integer32"
_AaauBadAtempts_Object = MibTableColumn
aaauBadAtempts = _AaauBadAtempts_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 1, 3, 1, 1, 17),
    _AaauBadAtempts_Type()
)
aaauBadAtempts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aaauBadAtempts.setStatus("current")


class _AaauSnmpOnly_Type(Integer32):
    """Custom type aaauSnmpOnly based on Integer32"""
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


_AaauSnmpOnly_Type.__name__ = "Integer32"
_AaauSnmpOnly_Object = MibTableColumn
aaauSnmpOnly = _AaauSnmpOnly_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 1, 3, 1, 1, 18),
    _AaauSnmpOnly_Type()
)
aaauSnmpOnly.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aaauSnmpOnly.setStatus("current")


class _AaauSnmpPrivPassword_Type(DisplayString):
    """Custom type aaauSnmpPrivPassword based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 30),
    )


_AaauSnmpPrivPassword_Type.__name__ = "DisplayString"
_AaauSnmpPrivPassword_Object = MibTableColumn
aaauSnmpPrivPassword = _AaauSnmpPrivPassword_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 1, 3, 1, 1, 19),
    _AaauSnmpPrivPassword_Type()
)
aaauSnmpPrivPassword.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aaauSnmpPrivPassword.setStatus("current")


class _AaauReadRightView_Type(DisplayString):
    """Custom type aaauReadRightView based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 30),
    )


_AaauReadRightView_Type.__name__ = "DisplayString"
_AaauReadRightView_Object = MibTableColumn
aaauReadRightView = _AaauReadRightView_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 1, 3, 1, 1, 20),
    _AaauReadRightView_Type()
)
aaauReadRightView.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aaauReadRightView.setStatus("current")


class _AaauWriteRightView_Type(DisplayString):
    """Custom type aaauWriteRightView based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 30),
    )


_AaauWriteRightView_Type.__name__ = "DisplayString"
_AaauWriteRightView_Object = MibTableColumn
aaauWriteRightView = _AaauWriteRightView_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 1, 3, 1, 1, 21),
    _AaauWriteRightView_Type()
)
aaauWriteRightView.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aaauWriteRightView.setStatus("current")
_AaaAuthenticatedUserTable_Object = MibTable
aaaAuthenticatedUserTable = _AaaAuthenticatedUserTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 1, 4)
)
if mibBuilder.loadTexts:
    aaaAuthenticatedUserTable.setStatus("current")
_AaaAuthenticatedUserEntry_Object = MibTableRow
aaaAuthenticatedUserEntry = _AaaAuthenticatedUserEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 1, 4, 1)
)
aaaAuthenticatedUserEntry.setIndexNames(
    (0, "ALCATEL-IND1-AAA-MIB", "aaaaMacAddress"),
)
if mibBuilder.loadTexts:
    aaaAuthenticatedUserEntry.setStatus("current")
_AaaaMacAddress_Type = MacAddress
_AaaaMacAddress_Object = MibTableColumn
aaaaMacAddress = _AaaaMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 1, 4, 1, 1),
    _AaaaMacAddress_Type()
)
aaaaMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aaaaMacAddress.setStatus("current")


class _AaaaUserName_Type(DisplayString):
    """Custom type aaaaUserName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AaaaUserName_Type.__name__ = "DisplayString"
_AaaaUserName_Object = MibTableColumn
aaaaUserName = _AaaaUserName_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 1, 4, 1, 2),
    _AaaaUserName_Type()
)
aaaaUserName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aaaaUserName.setStatus("current")


class _AaaaSlot_Type(Integer32):
    """Custom type aaaaSlot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AaaaSlot_Type.__name__ = "Integer32"
_AaaaSlot_Object = MibTableColumn
aaaaSlot = _AaaaSlot_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 1, 4, 1, 3),
    _AaaaSlot_Type()
)
aaaaSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aaaaSlot.setStatus("current")


class _AaaaPort_Type(Integer32):
    """Custom type aaaaPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AaaaPort_Type.__name__ = "Integer32"
_AaaaPort_Object = MibTableColumn
aaaaPort = _AaaaPort_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 1, 4, 1, 4),
    _AaaaPort_Type()
)
aaaaPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aaaaPort.setStatus("current")


class _AaaaVlan_Type(Integer32):
    """Custom type aaaaVlan based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AaaaVlan_Type.__name__ = "Integer32"
_AaaaVlan_Object = MibTableColumn
aaaaVlan = _AaaaVlan_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 1, 4, 1, 5),
    _AaaaVlan_Type()
)
aaaaVlan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aaaaVlan.setStatus("current")


class _AaaaDrop_Type(Integer32):
    """Custom type aaaaDrop based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("true", 1),
          ("false", 2))
    )


_AaaaDrop_Type.__name__ = "Integer32"
_AaaaDrop_Object = MibTableColumn
aaaaDrop = _AaaaDrop_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 1, 4, 1, 6),
    _AaaaDrop_Type()
)
aaaaDrop.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aaaaDrop.setStatus("current")
_AaaAvlanConfig_ObjectIdentity = ObjectIdentity
aaaAvlanConfig = _AaaAvlanConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 1, 5)
)


class _AaaAvlanDnsName_Type(DisplayString):
    """Custom type aaaAvlanDnsName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_AaaAvlanDnsName_Type.__name__ = "DisplayString"
_AaaAvlanDnsName_Object = MibScalar
aaaAvlanDnsName = _AaaAvlanDnsName_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 1, 5, 1),
    _AaaAvlanDnsName_Type()
)
aaaAvlanDnsName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aaaAvlanDnsName.setStatus("current")
_AaaAvlanDhcpDefGateway_Type = IpAddress
_AaaAvlanDhcpDefGateway_Object = MibScalar
aaaAvlanDhcpDefGateway = _AaaAvlanDhcpDefGateway_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 1, 5, 2),
    _AaaAvlanDhcpDefGateway_Type()
)
aaaAvlanDhcpDefGateway.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aaaAvlanDhcpDefGateway.setStatus("current")


class _AaaAvlanDefaultTraffic_Type(Integer32):
    """Custom type aaaAvlanDefaultTraffic based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ns", 0),
          ("true", 1),
          ("false", 2))
    )


_AaaAvlanDefaultTraffic_Type.__name__ = "Integer32"
_AaaAvlanDefaultTraffic_Object = MibScalar
aaaAvlanDefaultTraffic = _AaaAvlanDefaultTraffic_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 1, 5, 3),
    _AaaAvlanDefaultTraffic_Type()
)
aaaAvlanDefaultTraffic.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aaaAvlanDefaultTraffic.setStatus("current")


class _AaaAvlanPortBound_Type(Integer32):
    """Custom type aaaAvlanPortBound based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ns", 0),
          ("true", 1),
          ("false", 2))
    )


_AaaAvlanPortBound_Type.__name__ = "Integer32"
_AaaAvlanPortBound_Object = MibScalar
aaaAvlanPortBound = _AaaAvlanPortBound_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 1, 5, 4),
    _AaaAvlanPortBound_Type()
)
aaaAvlanPortBound.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aaaAvlanPortBound.setStatus("current")


class _AaaAvlanLanguage_Type(Integer32):
    """Custom type aaaAvlanLanguage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ns", 0),
          ("true", 1),
          ("false", 2))
    )


_AaaAvlanLanguage_Type.__name__ = "Integer32"
_AaaAvlanLanguage_Object = MibScalar
aaaAvlanLanguage = _AaaAvlanLanguage_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 1, 5, 5),
    _AaaAvlanLanguage_Type()
)
aaaAvlanLanguage.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aaaAvlanLanguage.setStatus("current")
_AaaAsaConfig_ObjectIdentity = ObjectIdentity
aaaAsaConfig = _AaaAsaConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 1, 6)
)


class _AaaAsaPasswordSizeMin_Type(Integer32):
    """Custom type aaaAsaPasswordSizeMin based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 14),
    )


_AaaAsaPasswordSizeMin_Type.__name__ = "Integer32"
_AaaAsaPasswordSizeMin_Object = MibScalar
aaaAsaPasswordSizeMin = _AaaAsaPasswordSizeMin_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 1, 6, 1),
    _AaaAsaPasswordSizeMin_Type()
)
aaaAsaPasswordSizeMin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aaaAsaPasswordSizeMin.setStatus("current")


class _AaaAsaDefaultPasswordExpirationInDays_Type(Integer32):
    """Custom type aaaAsaDefaultPasswordExpirationInDays based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 150),
    )


_AaaAsaDefaultPasswordExpirationInDays_Type.__name__ = "Integer32"
_AaaAsaDefaultPasswordExpirationInDays_Object = MibScalar
aaaAsaDefaultPasswordExpirationInDays = _AaaAsaDefaultPasswordExpirationInDays_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 1, 6, 2),
    _AaaAsaDefaultPasswordExpirationInDays_Type()
)
aaaAsaDefaultPasswordExpirationInDays.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aaaAsaDefaultPasswordExpirationInDays.setStatus("current")


class _AaaAsaPasswordContainUserName_Type(Integer32):
    """Custom type aaaAsaPasswordContainUserName based on Integer32"""
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


_AaaAsaPasswordContainUserName_Type.__name__ = "Integer32"
_AaaAsaPasswordContainUserName_Object = MibScalar
aaaAsaPasswordContainUserName = _AaaAsaPasswordContainUserName_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 1, 6, 3),
    _AaaAsaPasswordContainUserName_Type()
)
aaaAsaPasswordContainUserName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aaaAsaPasswordContainUserName.setStatus("current")


class _AaaAsaPasswordMinUpperCase_Type(Integer32):
    """Custom type aaaAsaPasswordMinUpperCase based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_AaaAsaPasswordMinUpperCase_Type.__name__ = "Integer32"
_AaaAsaPasswordMinUpperCase_Object = MibScalar
aaaAsaPasswordMinUpperCase = _AaaAsaPasswordMinUpperCase_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 1, 6, 4),
    _AaaAsaPasswordMinUpperCase_Type()
)
aaaAsaPasswordMinUpperCase.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aaaAsaPasswordMinUpperCase.setStatus("current")


class _AaaAsaPasswordMinLowerCase_Type(Integer32):
    """Custom type aaaAsaPasswordMinLowerCase based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_AaaAsaPasswordMinLowerCase_Type.__name__ = "Integer32"
_AaaAsaPasswordMinLowerCase_Object = MibScalar
aaaAsaPasswordMinLowerCase = _AaaAsaPasswordMinLowerCase_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 1, 6, 5),
    _AaaAsaPasswordMinLowerCase_Type()
)
aaaAsaPasswordMinLowerCase.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aaaAsaPasswordMinLowerCase.setStatus("current")


class _AaaAsaPasswordMinDigit_Type(Integer32):
    """Custom type aaaAsaPasswordMinDigit based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_AaaAsaPasswordMinDigit_Type.__name__ = "Integer32"
_AaaAsaPasswordMinDigit_Object = MibScalar
aaaAsaPasswordMinDigit = _AaaAsaPasswordMinDigit_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 1, 6, 6),
    _AaaAsaPasswordMinDigit_Type()
)
aaaAsaPasswordMinDigit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aaaAsaPasswordMinDigit.setStatus("current")


class _AaaAsaPasswordMinNonAlphan_Type(Integer32):
    """Custom type aaaAsaPasswordMinNonAlphan based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_AaaAsaPasswordMinNonAlphan_Type.__name__ = "Integer32"
_AaaAsaPasswordMinNonAlphan_Object = MibScalar
aaaAsaPasswordMinNonAlphan = _AaaAsaPasswordMinNonAlphan_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 1, 6, 7),
    _AaaAsaPasswordMinNonAlphan_Type()
)
aaaAsaPasswordMinNonAlphan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aaaAsaPasswordMinNonAlphan.setStatus("current")


class _AaaAsaPasswordHistory_Type(Integer32):
    """Custom type aaaAsaPasswordHistory based on Integer32"""
    defaultValue = 4

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 24),
    )


_AaaAsaPasswordHistory_Type.__name__ = "Integer32"
_AaaAsaPasswordHistory_Object = MibScalar
aaaAsaPasswordHistory = _AaaAsaPasswordHistory_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 1, 6, 8),
    _AaaAsaPasswordHistory_Type()
)
aaaAsaPasswordHistory.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aaaAsaPasswordHistory.setStatus("current")


class _AaaAsaPasswordMinAge_Type(Integer32):
    """Custom type aaaAsaPasswordMinAge based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 150),
    )


_AaaAsaPasswordMinAge_Type.__name__ = "Integer32"
_AaaAsaPasswordMinAge_Object = MibScalar
aaaAsaPasswordMinAge = _AaaAsaPasswordMinAge_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 1, 6, 9),
    _AaaAsaPasswordMinAge_Type()
)
aaaAsaPasswordMinAge.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aaaAsaPasswordMinAge.setStatus("current")


class _AaaAsaLockoutWindow_Type(Integer32):
    """Custom type aaaAsaLockoutWindow based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 99999),
    )


_AaaAsaLockoutWindow_Type.__name__ = "Integer32"
_AaaAsaLockoutWindow_Object = MibScalar
aaaAsaLockoutWindow = _AaaAsaLockoutWindow_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 1, 6, 10),
    _AaaAsaLockoutWindow_Type()
)
aaaAsaLockoutWindow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aaaAsaLockoutWindow.setStatus("current")


class _AaaAsaLockoutDuration_Type(Integer32):
    """Custom type aaaAsaLockoutDuration based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 99999),
    )


_AaaAsaLockoutDuration_Type.__name__ = "Integer32"
_AaaAsaLockoutDuration_Object = MibScalar
aaaAsaLockoutDuration = _AaaAsaLockoutDuration_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 1, 6, 11),
    _AaaAsaLockoutDuration_Type()
)
aaaAsaLockoutDuration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aaaAsaLockoutDuration.setStatus("current")


class _AaaAsaLockoutThreshold_Type(Integer32):
    """Custom type aaaAsaLockoutThreshold based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 999),
    )


_AaaAsaLockoutThreshold_Type.__name__ = "Integer32"
_AaaAsaLockoutThreshold_Object = MibScalar
aaaAsaLockoutThreshold = _AaaAsaLockoutThreshold_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 1, 6, 12),
    _AaaAsaLockoutThreshold_Type()
)
aaaAsaLockoutThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aaaAsaLockoutThreshold.setStatus("current")


class _AaaAsaROUserPingTrtEnable_Type(Integer32):
    """Custom type aaaAsaROUserPingTrtEnable based on Integer32"""
    defaultValue = 0

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


_AaaAsaROUserPingTrtEnable_Type.__name__ = "Integer32"
_AaaAsaROUserPingTrtEnable_Object = MibScalar
aaaAsaROUserPingTrtEnable = _AaaAsaROUserPingTrtEnable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 1, 6, 13),
    _AaaAsaROUserPingTrtEnable_Type()
)
aaaAsaROUserPingTrtEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aaaAsaROUserPingTrtEnable.setStatus("obsolete")


class _AaaAsaAccessPolicyAdminConsoleOnly_Type(Integer32):
    """Custom type aaaAsaAccessPolicyAdminConsoleOnly based on Integer32"""
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


_AaaAsaAccessPolicyAdminConsoleOnly_Type.__name__ = "Integer32"
_AaaAsaAccessPolicyAdminConsoleOnly_Object = MibScalar
aaaAsaAccessPolicyAdminConsoleOnly = _AaaAsaAccessPolicyAdminConsoleOnly_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 1, 6, 14),
    _AaaAsaAccessPolicyAdminConsoleOnly_Type()
)
aaaAsaAccessPolicyAdminConsoleOnly.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aaaAsaAccessPolicyAdminConsoleOnly.setStatus("current")


class _AaaAsaCertPassword_Type(DisplayString):
    """Custom type aaaAsaCertPassword based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AaaAsaCertPassword_Type.__name__ = "DisplayString"
_AaaAsaCertPassword_Object = MibScalar
aaaAsaCertPassword = _AaaAsaCertPassword_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 1, 6, 15),
    _AaaAsaCertPassword_Type()
)
aaaAsaCertPassword.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aaaAsaCertPassword.setStatus("current")


class _AaaAsaAccessMode_Type(Integer32):
    """Custom type aaaAsaAccessMode based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("default", 0),
          ("enhanced", 1))
    )


_AaaAsaAccessMode_Type.__name__ = "Integer32"
_AaaAsaAccessMode_Object = MibScalar
aaaAsaAccessMode = _AaaAsaAccessMode_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 1, 6, 16),
    _AaaAsaAccessMode_Type()
)
aaaAsaAccessMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aaaAsaAccessMode.setStatus("current")


class _AaaAsaIpLockoutThreshold_Type(Integer32):
    """Custom type aaaAsaIpLockoutThreshold based on Integer32"""
    defaultValue = 6

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 999),
    )


_AaaAsaIpLockoutThreshold_Type.__name__ = "Integer32"
_AaaAsaIpLockoutThreshold_Object = MibScalar
aaaAsaIpLockoutThreshold = _AaaAsaIpLockoutThreshold_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 1, 6, 17),
    _AaaAsaIpLockoutThreshold_Type()
)
aaaAsaIpLockoutThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aaaAsaIpLockoutThreshold.setStatus("current")


class _AaaSwitchAccessMgmtStationState_Type(Integer32):
    """Custom type aaaSwitchAccessMgmtStationState based on Integer32"""
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


_AaaSwitchAccessMgmtStationState_Type.__name__ = "Integer32"
_AaaSwitchAccessMgmtStationState_Object = MibScalar
aaaSwitchAccessMgmtStationState = _AaaSwitchAccessMgmtStationState_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 1, 6, 18),
    _AaaSwitchAccessMgmtStationState_Type()
)
aaaSwitchAccessMgmtStationState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aaaSwitchAccessMgmtStationState.setStatus("current")
_AaaAvlanAddressTable_Object = MibTable
aaaAvlanAddressTable = _AaaAvlanAddressTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 1, 7)
)
if mibBuilder.loadTexts:
    aaaAvlanAddressTable.setStatus("current")
_AaaAvlanAddressEntry_Object = MibTableRow
aaaAvlanAddressEntry = _AaaAvlanAddressEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 1, 7, 1)
)
aaaAvlanAddressEntry.setIndexNames(
    (0, "ALCATEL-IND1-AAA-MIB", "aaaAvlanId"),
)
if mibBuilder.loadTexts:
    aaaAvlanAddressEntry.setStatus("current")


class _AaaAvlanId_Type(Integer32):
    """Custom type aaaAvlanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_AaaAvlanId_Type.__name__ = "Integer32"
_AaaAvlanId_Object = MibTableColumn
aaaAvlanId = _AaaAvlanId_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 1, 7, 1, 1),
    _AaaAvlanId_Type()
)
aaaAvlanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aaaAvlanId.setStatus("current")
_AaaAvlanIpAddress_Type = IpAddress
_AaaAvlanIpAddress_Object = MibTableColumn
aaaAvlanIpAddress = _AaaAvlanIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 1, 7, 1, 2),
    _AaaAvlanIpAddress_Type()
)
aaaAvlanIpAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aaaAvlanIpAddress.setStatus("current")
_AaaUserNetProfileTable_Object = MibTable
aaaUserNetProfileTable = _AaaUserNetProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 1, 8)
)
if mibBuilder.loadTexts:
    aaaUserNetProfileTable.setStatus("current")
_AaaUserNetProfileEntry_Object = MibTableRow
aaaUserNetProfileEntry = _AaaUserNetProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 1, 8, 1)
)
aaaUserNetProfileEntry.setIndexNames(
    (0, "ALCATEL-IND1-AAA-MIB", "aaaUserNetProfileName"),
)
if mibBuilder.loadTexts:
    aaaUserNetProfileEntry.setStatus("current")


class _AaaUserNetProfileName_Type(DisplayString):
    """Custom type aaaUserNetProfileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_AaaUserNetProfileName_Type.__name__ = "DisplayString"
_AaaUserNetProfileName_Object = MibTableColumn
aaaUserNetProfileName = _AaaUserNetProfileName_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 1, 8, 1, 1),
    _AaaUserNetProfileName_Type()
)
aaaUserNetProfileName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    aaaUserNetProfileName.setStatus("current")


class _AaaUserNetProfileVlanID_Type(Integer32):
    """Custom type aaaUserNetProfileVlanID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_AaaUserNetProfileVlanID_Type.__name__ = "Integer32"
_AaaUserNetProfileVlanID_Object = MibTableColumn
aaaUserNetProfileVlanID = _AaaUserNetProfileVlanID_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 1, 8, 1, 2),
    _AaaUserNetProfileVlanID_Type()
)
aaaUserNetProfileVlanID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aaaUserNetProfileVlanID.setStatus("current")
_AaaUserNetProfileRowStatus_Type = RowStatus
_AaaUserNetProfileRowStatus_Object = MibTableColumn
aaaUserNetProfileRowStatus = _AaaUserNetProfileRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 1, 8, 1, 3),
    _AaaUserNetProfileRowStatus_Type()
)
aaaUserNetProfileRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aaaUserNetProfileRowStatus.setStatus("current")


class _AaaUserNetProfileHICflag_Type(Integer32):
    """Custom type aaaUserNetProfileHICflag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_AaaUserNetProfileHICflag_Type.__name__ = "Integer32"
_AaaUserNetProfileHICflag_Object = MibTableColumn
aaaUserNetProfileHICflag = _AaaUserNetProfileHICflag_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 1, 8, 1, 4),
    _AaaUserNetProfileHICflag_Type()
)
aaaUserNetProfileHICflag.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aaaUserNetProfileHICflag.setStatus("current")


class _AaaUserNetProfileQosPolicyListName_Type(DisplayString):
    """Custom type aaaUserNetProfileQosPolicyListName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_AaaUserNetProfileQosPolicyListName_Type.__name__ = "DisplayString"
_AaaUserNetProfileQosPolicyListName_Object = MibTableColumn
aaaUserNetProfileQosPolicyListName = _AaaUserNetProfileQosPolicyListName_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 1, 8, 1, 5),
    _AaaUserNetProfileQosPolicyListName_Type()
)
aaaUserNetProfileQosPolicyListName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aaaUserNetProfileQosPolicyListName.setStatus("current")


class _AaaUserNetProfileMaxIngressBw_Type(Integer32):
    """Custom type aaaUserNetProfileMaxIngressBw based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 10000000),
    )


_AaaUserNetProfileMaxIngressBw_Type.__name__ = "Integer32"
_AaaUserNetProfileMaxIngressBw_Object = MibTableColumn
aaaUserNetProfileMaxIngressBw = _AaaUserNetProfileMaxIngressBw_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 1, 8, 1, 6),
    _AaaUserNetProfileMaxIngressBw_Type()
)
aaaUserNetProfileMaxIngressBw.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aaaUserNetProfileMaxIngressBw.setStatus("current")


class _AaaUserNetProfileMaxEgressBw_Type(Integer32):
    """Custom type aaaUserNetProfileMaxEgressBw based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 10000000),
    )


_AaaUserNetProfileMaxEgressBw_Type.__name__ = "Integer32"
_AaaUserNetProfileMaxEgressBw_Object = MibTableColumn
aaaUserNetProfileMaxEgressBw = _AaaUserNetProfileMaxEgressBw_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 1, 8, 1, 7),
    _AaaUserNetProfileMaxEgressBw_Type()
)
aaaUserNetProfileMaxEgressBw.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aaaUserNetProfileMaxEgressBw.setStatus("current")


class _AaaUserNetProfileMaxDefaultDepth_Type(Integer32):
    """Custom type aaaUserNetProfileMaxDefaultDepth based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 131072),
    )


_AaaUserNetProfileMaxDefaultDepth_Type.__name__ = "Integer32"
_AaaUserNetProfileMaxDefaultDepth_Object = MibTableColumn
aaaUserNetProfileMaxDefaultDepth = _AaaUserNetProfileMaxDefaultDepth_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 1, 8, 1, 8),
    _AaaUserNetProfileMaxDefaultDepth_Type()
)
aaaUserNetProfileMaxDefaultDepth.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aaaUserNetProfileMaxDefaultDepth.setStatus("current")


class _AaaUserNetworkProfileRedirectUrl_Type(SnmpAdminString):
    """Custom type aaaUserNetworkProfileRedirectUrl based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_AaaUserNetworkProfileRedirectUrl_Type.__name__ = "SnmpAdminString"
_AaaUserNetworkProfileRedirectUrl_Object = MibTableColumn
aaaUserNetworkProfileRedirectUrl = _AaaUserNetworkProfileRedirectUrl_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 1, 8, 1, 9),
    _AaaUserNetworkProfileRedirectUrl_Type()
)
aaaUserNetworkProfileRedirectUrl.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aaaUserNetworkProfileRedirectUrl.setStatus("current")


class _AaaRadAgentConfig_Type(Integer32):
    """Custom type aaaRadAgentConfig based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_AaaRadAgentConfig_Type.__name__ = "Integer32"
_AaaRadAgentConfig_Object = MibScalar
aaaRadAgentConfig = _AaaRadAgentConfig_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 1, 9),
    _AaaRadAgentConfig_Type()
)
aaaRadAgentConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aaaRadAgentConfig.setStatus("obsolete")
_AaaRadAgentIP_Type = IpAddress
_AaaRadAgentIP_Object = MibScalar
aaaRadAgentIP = _AaaRadAgentIP_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 1, 10),
    _AaaRadAgentIP_Type()
)
aaaRadAgentIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aaaRadAgentIP.setStatus("obsolete")
_AaaHicConfig_ObjectIdentity = ObjectIdentity
aaaHicConfig = _AaaHicConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 1, 11)
)
_AaaHicSvrTable_Object = MibTable
aaaHicSvrTable = _AaaHicSvrTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 1, 11, 1)
)
if mibBuilder.loadTexts:
    aaaHicSvrTable.setStatus("current")
_AaaHicSvrEntry_Object = MibTableRow
aaaHicSvrEntry = _AaaHicSvrEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 1, 11, 1, 1)
)
aaaHicSvrEntry.setIndexNames(
    (0, "ALCATEL-IND1-AAA-MIB", "aaaHicSvrName"),
)
if mibBuilder.loadTexts:
    aaaHicSvrEntry.setStatus("current")


class _AaaHicSvrName_Type(SnmpAdminString):
    """Custom type aaaHicSvrName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_AaaHicSvrName_Type.__name__ = "SnmpAdminString"
_AaaHicSvrName_Object = MibTableColumn
aaaHicSvrName = _AaaHicSvrName_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 1, 11, 1, 1, 1),
    _AaaHicSvrName_Type()
)
aaaHicSvrName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    aaaHicSvrName.setStatus("current")
_AaaHicSvrIpAddr_Type = IpAddress
_AaaHicSvrIpAddr_Object = MibTableColumn
aaaHicSvrIpAddr = _AaaHicSvrIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 1, 11, 1, 1, 2),
    _AaaHicSvrIpAddr_Type()
)
aaaHicSvrIpAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aaaHicSvrIpAddr.setStatus("current")


class _AaaHicSvrPort_Type(Integer32):
    """Custom type aaaHicSvrPort based on Integer32"""
    defaultValue = 11707

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1025, 65535),
    )


_AaaHicSvrPort_Type.__name__ = "Integer32"
_AaaHicSvrPort_Object = MibTableColumn
aaaHicSvrPort = _AaaHicSvrPort_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 1, 11, 1, 1, 3),
    _AaaHicSvrPort_Type()
)
aaaHicSvrPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aaaHicSvrPort.setStatus("current")


class _AaaHicSvrKey_Type(SnmpAdminString):
    """Custom type aaaHicSvrKey based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_AaaHicSvrKey_Type.__name__ = "SnmpAdminString"
_AaaHicSvrKey_Object = MibTableColumn
aaaHicSvrKey = _AaaHicSvrKey_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 1, 11, 1, 1, 4),
    _AaaHicSvrKey_Type()
)
aaaHicSvrKey.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aaaHicSvrKey.setStatus("current")
_AaaHicSvrRowStatus_Type = RowStatus
_AaaHicSvrRowStatus_Object = MibTableColumn
aaaHicSvrRowStatus = _AaaHicSvrRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 1, 11, 1, 1, 5),
    _AaaHicSvrRowStatus_Type()
)
aaaHicSvrRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aaaHicSvrRowStatus.setStatus("current")


class _AaaHicSvrStatus_Type(Integer32):
    """Custom type aaaHicSvrStatus based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("down", 1),
          ("up", 2))
    )


_AaaHicSvrStatus_Type.__name__ = "Integer32"
_AaaHicSvrStatus_Object = MibTableColumn
aaaHicSvrStatus = _AaaHicSvrStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 1, 11, 1, 1, 6),
    _AaaHicSvrStatus_Type()
)
aaaHicSvrStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aaaHicSvrStatus.setStatus("current")


class _AaaHicSvrRole_Type(Integer32):
    """Custom type aaaHicSvrRole based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("primary", 1),
          ("backup", 2))
    )


_AaaHicSvrRole_Type.__name__ = "Integer32"
_AaaHicSvrRole_Object = MibTableColumn
aaaHicSvrRole = _AaaHicSvrRole_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 1, 11, 1, 1, 7),
    _AaaHicSvrRole_Type()
)
aaaHicSvrRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aaaHicSvrRole.setStatus("current")


class _AaaHicSvrConnection_Type(Integer32):
    """Custom type aaaHicSvrConnection based on Integer32"""
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
          ("inactive", 2))
    )


_AaaHicSvrConnection_Type.__name__ = "Integer32"
_AaaHicSvrConnection_Object = MibTableColumn
aaaHicSvrConnection = _AaaHicSvrConnection_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 1, 11, 1, 1, 8),
    _AaaHicSvrConnection_Type()
)
aaaHicSvrConnection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aaaHicSvrConnection.setStatus("current")
_AaaHicAllowedTable_Object = MibTable
aaaHicAllowedTable = _AaaHicAllowedTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 1, 11, 2)
)
if mibBuilder.loadTexts:
    aaaHicAllowedTable.setStatus("current")
_AaaHicAllowedEntry_Object = MibTableRow
aaaHicAllowedEntry = _AaaHicAllowedEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 1, 11, 2, 1)
)
aaaHicAllowedEntry.setIndexNames(
    (0, "ALCATEL-IND1-AAA-MIB", "aaaHicAllowedName"),
)
if mibBuilder.loadTexts:
    aaaHicAllowedEntry.setStatus("current")


class _AaaHicAllowedName_Type(SnmpAdminString):
    """Custom type aaaHicAllowedName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_AaaHicAllowedName_Type.__name__ = "SnmpAdminString"
_AaaHicAllowedName_Object = MibTableColumn
aaaHicAllowedName = _AaaHicAllowedName_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 1, 11, 2, 1, 1),
    _AaaHicAllowedName_Type()
)
aaaHicAllowedName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    aaaHicAllowedName.setStatus("current")
_AaaHicAllowedIpAddr_Type = IpAddress
_AaaHicAllowedIpAddr_Object = MibTableColumn
aaaHicAllowedIpAddr = _AaaHicAllowedIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 1, 11, 2, 1, 2),
    _AaaHicAllowedIpAddr_Type()
)
aaaHicAllowedIpAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aaaHicAllowedIpAddr.setStatus("current")


class _AaaHicAllowedIpMask_Type(IpAddress):
    """Custom type aaaHicAllowedIpMask based on IpAddress"""
    defaultHexValue = "ffffffff"


_AaaHicAllowedIpMask_Type.__name__ = "IpAddress"
_AaaHicAllowedIpMask_Object = MibTableColumn
aaaHicAllowedIpMask = _AaaHicAllowedIpMask_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 1, 11, 2, 1, 3),
    _AaaHicAllowedIpMask_Type()
)
aaaHicAllowedIpMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aaaHicAllowedIpMask.setStatus("current")
_AaaHicAllowedRowStatus_Type = RowStatus
_AaaHicAllowedRowStatus_Object = MibTableColumn
aaaHicAllowedRowStatus = _AaaHicAllowedRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 1, 11, 2, 1, 4),
    _AaaHicAllowedRowStatus_Type()
)
aaaHicAllowedRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aaaHicAllowedRowStatus.setStatus("current")
_AaaHicOverrideTable_Object = MibTable
aaaHicOverrideTable = _AaaHicOverrideTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 1, 11, 3)
)
if mibBuilder.loadTexts:
    aaaHicOverrideTable.setStatus("current")
_AaaHicOverrideEntry_Object = MibTableRow
aaaHicOverrideEntry = _AaaHicOverrideEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 1, 11, 3, 1)
)
aaaHicOverrideEntry.setIndexNames(
    (0, "ALCATEL-IND1-AAA-MIB", "aaaHicOverrideMac"),
)
if mibBuilder.loadTexts:
    aaaHicOverrideEntry.setStatus("current")
_AaaHicOverrideMac_Type = MacAddress
_AaaHicOverrideMac_Object = MibTableColumn
aaaHicOverrideMac = _AaaHicOverrideMac_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 1, 11, 3, 1, 1),
    _AaaHicOverrideMac_Type()
)
aaaHicOverrideMac.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    aaaHicOverrideMac.setStatus("current")


class _AaaHicOverrideStatus_Type(Integer32):
    """Custom type aaaHicOverrideStatus based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enforce", 1),
          ("bypass", 2))
    )


_AaaHicOverrideStatus_Type.__name__ = "Integer32"
_AaaHicOverrideStatus_Object = MibTableColumn
aaaHicOverrideStatus = _AaaHicOverrideStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 1, 11, 3, 1, 2),
    _AaaHicOverrideStatus_Type()
)
aaaHicOverrideStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aaaHicOverrideStatus.setStatus("current")
_AaaHicOverrideRowStatus_Type = RowStatus
_AaaHicOverrideRowStatus_Object = MibTableColumn
aaaHicOverrideRowStatus = _AaaHicOverrideRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 1, 11, 3, 1, 3),
    _AaaHicOverrideRowStatus_Type()
)
aaaHicOverrideRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aaaHicOverrideRowStatus.setStatus("current")
_AaaHicHostTable_Object = MibTable
aaaHicHostTable = _AaaHicHostTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 1, 11, 4)
)
if mibBuilder.loadTexts:
    aaaHicHostTable.setStatus("current")
_AaaHicHostEntry_Object = MibTableRow
aaaHicHostEntry = _AaaHicHostEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 1, 11, 4, 1)
)
aaaHicHostEntry.setIndexNames(
    (0, "ALCATEL-IND1-AAA-MIB", "aaaHicHostMac"),
)
if mibBuilder.loadTexts:
    aaaHicHostEntry.setStatus("current")
_AaaHicHostMac_Type = MacAddress
_AaaHicHostMac_Object = MibTableColumn
aaaHicHostMac = _AaaHicHostMac_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 1, 11, 4, 1, 1),
    _AaaHicHostMac_Type()
)
aaaHicHostMac.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    aaaHicHostMac.setStatus("current")


class _AaaHicHostStatus_Type(Integer32):
    """Custom type aaaHicHostStatus based on Integer32"""
    defaultValue = 3

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
        *(("inprogress", 1),
          ("success", 2),
          ("fail", 3),
          ("timeout", 4))
    )


_AaaHicHostStatus_Type.__name__ = "Integer32"
_AaaHicHostStatus_Object = MibTableColumn
aaaHicHostStatus = _AaaHicHostStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 1, 11, 4, 1, 2),
    _AaaHicHostStatus_Type()
)
aaaHicHostStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aaaHicHostStatus.setStatus("current")
_AaaHicConfigInfo_ObjectIdentity = ObjectIdentity
aaaHicConfigInfo = _AaaHicConfigInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 1, 11, 5)
)


class _AaaHicStatus_Type(Integer32):
    """Custom type aaaHicStatus based on Integer32"""
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


_AaaHicStatus_Type.__name__ = "Integer32"
_AaaHicStatus_Object = MibScalar
aaaHicStatus = _AaaHicStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 1, 11, 5, 1),
    _AaaHicStatus_Type()
)
aaaHicStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aaaHicStatus.setStatus("current")


class _AaaHicAllowed1Name_Type(SnmpAdminString):
    """Custom type aaaHicAllowed1Name based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_AaaHicAllowed1Name_Type.__name__ = "SnmpAdminString"
_AaaHicAllowed1Name_Object = MibScalar
aaaHicAllowed1Name = _AaaHicAllowed1Name_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 1, 11, 5, 2),
    _AaaHicAllowed1Name_Type()
)
aaaHicAllowed1Name.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aaaHicAllowed1Name.setStatus("current")


class _AaaHicAllowed2Name_Type(SnmpAdminString):
    """Custom type aaaHicAllowed2Name based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_AaaHicAllowed2Name_Type.__name__ = "SnmpAdminString"
_AaaHicAllowed2Name_Object = MibScalar
aaaHicAllowed2Name = _AaaHicAllowed2Name_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 1, 11, 5, 3),
    _AaaHicAllowed2Name_Type()
)
aaaHicAllowed2Name.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aaaHicAllowed2Name.setStatus("current")


class _AaaHicAllowed3Name_Type(SnmpAdminString):
    """Custom type aaaHicAllowed3Name based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_AaaHicAllowed3Name_Type.__name__ = "SnmpAdminString"
_AaaHicAllowed3Name_Object = MibScalar
aaaHicAllowed3Name = _AaaHicAllowed3Name_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 1, 11, 5, 4),
    _AaaHicAllowed3Name_Type()
)
aaaHicAllowed3Name.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aaaHicAllowed3Name.setStatus("current")


class _AaaHicAllowed4Name_Type(SnmpAdminString):
    """Custom type aaaHicAllowed4Name based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_AaaHicAllowed4Name_Type.__name__ = "SnmpAdminString"
_AaaHicAllowed4Name_Object = MibScalar
aaaHicAllowed4Name = _AaaHicAllowed4Name_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 1, 11, 5, 5),
    _AaaHicAllowed4Name_Type()
)
aaaHicAllowed4Name.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aaaHicAllowed4Name.setStatus("current")


class _AaaHicWebAgentDownloadUrl_Type(SnmpAdminString):
    """Custom type aaaHicWebAgentDownloadUrl based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_AaaHicWebAgentDownloadUrl_Type.__name__ = "SnmpAdminString"
_AaaHicWebAgentDownloadUrl_Object = MibScalar
aaaHicWebAgentDownloadUrl = _AaaHicWebAgentDownloadUrl_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 1, 11, 5, 6),
    _AaaHicWebAgentDownloadUrl_Type()
)
aaaHicWebAgentDownloadUrl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aaaHicWebAgentDownloadUrl.setStatus("current")


class _AaaHicCustomHttpProxyPort_Type(Integer32):
    """Custom type aaaHicCustomHttpProxyPort based on Integer32"""
    defaultValue = 8080

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1025, 65535),
    )


_AaaHicCustomHttpProxyPort_Type.__name__ = "Integer32"
_AaaHicCustomHttpProxyPort_Object = MibScalar
aaaHicCustomHttpProxyPort = _AaaHicCustomHttpProxyPort_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 1, 11, 5, 7),
    _AaaHicCustomHttpProxyPort_Type()
)
aaaHicCustomHttpProxyPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aaaHicCustomHttpProxyPort.setStatus("current")


class _AaaHicBgPollInterval_Type(Integer32):
    """Custom type aaaHicBgPollInterval based on Integer32"""
    defaultValue = 16

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(16, 256),
    )


_AaaHicBgPollInterval_Type.__name__ = "Integer32"
_AaaHicBgPollInterval_Object = MibScalar
aaaHicBgPollInterval = _AaaHicBgPollInterval_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 1, 11, 5, 8),
    _AaaHicBgPollInterval_Type()
)
aaaHicBgPollInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aaaHicBgPollInterval.setStatus("current")
if mibBuilder.loadTexts:
    aaaHicBgPollInterval.setUnits("seconds")


class _AaaHicSvrFailMode_Type(Integer32):
    """Custom type aaaHicSvrFailMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("hold", 1),
          ("passthrough", 2))
    )


_AaaHicSvrFailMode_Type.__name__ = "Integer32"
_AaaHicSvrFailMode_Object = MibScalar
aaaHicSvrFailMode = _AaaHicSvrFailMode_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 1, 11, 5, 9),
    _AaaHicSvrFailMode_Type()
)
aaaHicSvrFailMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aaaHicSvrFailMode.setStatus("current")
_AaaUNPIpNetRuleTable_Object = MibTable
aaaUNPIpNetRuleTable = _AaaUNPIpNetRuleTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 1, 12)
)
if mibBuilder.loadTexts:
    aaaUNPIpNetRuleTable.setStatus("current")
_AaaUNPIpNetRuleEntry_Object = MibTableRow
aaaUNPIpNetRuleEntry = _AaaUNPIpNetRuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 1, 12, 1)
)
aaaUNPIpNetRuleEntry.setIndexNames(
    (0, "ALCATEL-IND1-AAA-MIB", "aaaUNPIpNetRuleAddrType"),
    (0, "ALCATEL-IND1-AAA-MIB", "aaaUNPIpNetRuleAddr"),
    (0, "ALCATEL-IND1-AAA-MIB", "aaaUNPIpNetRuleMask"),
)
if mibBuilder.loadTexts:
    aaaUNPIpNetRuleEntry.setStatus("current")
_AaaUNPIpNetRuleAddrType_Type = InetAddressType
_AaaUNPIpNetRuleAddrType_Object = MibTableColumn
aaaUNPIpNetRuleAddrType = _AaaUNPIpNetRuleAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 1, 12, 1, 1),
    _AaaUNPIpNetRuleAddrType_Type()
)
aaaUNPIpNetRuleAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    aaaUNPIpNetRuleAddrType.setStatus("current")
_AaaUNPIpNetRuleAddr_Type = InetAddress
_AaaUNPIpNetRuleAddr_Object = MibTableColumn
aaaUNPIpNetRuleAddr = _AaaUNPIpNetRuleAddr_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 1, 12, 1, 2),
    _AaaUNPIpNetRuleAddr_Type()
)
aaaUNPIpNetRuleAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    aaaUNPIpNetRuleAddr.setStatus("current")
_AaaUNPIpNetRuleMask_Type = InetAddress
_AaaUNPIpNetRuleMask_Object = MibTableColumn
aaaUNPIpNetRuleMask = _AaaUNPIpNetRuleMask_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 1, 12, 1, 3),
    _AaaUNPIpNetRuleMask_Type()
)
aaaUNPIpNetRuleMask.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    aaaUNPIpNetRuleMask.setStatus("current")


class _AaaUNPIpNetRuleProfileName_Type(SnmpAdminString):
    """Custom type aaaUNPIpNetRuleProfileName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_AaaUNPIpNetRuleProfileName_Type.__name__ = "SnmpAdminString"
_AaaUNPIpNetRuleProfileName_Object = MibTableColumn
aaaUNPIpNetRuleProfileName = _AaaUNPIpNetRuleProfileName_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 1, 12, 1, 4),
    _AaaUNPIpNetRuleProfileName_Type()
)
aaaUNPIpNetRuleProfileName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aaaUNPIpNetRuleProfileName.setStatus("current")
_AaaUNPIpNetRuleRowStatus_Type = RowStatus
_AaaUNPIpNetRuleRowStatus_Object = MibTableColumn
aaaUNPIpNetRuleRowStatus = _AaaUNPIpNetRuleRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 1, 12, 1, 5),
    _AaaUNPIpNetRuleRowStatus_Type()
)
aaaUNPIpNetRuleRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aaaUNPIpNetRuleRowStatus.setStatus("current")
_AaaUNPMacRuleTable_Object = MibTable
aaaUNPMacRuleTable = _AaaUNPMacRuleTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 1, 13)
)
if mibBuilder.loadTexts:
    aaaUNPMacRuleTable.setStatus("current")
_AaaUNPMacRuleEntry_Object = MibTableRow
aaaUNPMacRuleEntry = _AaaUNPMacRuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 1, 13, 1)
)
aaaUNPMacRuleEntry.setIndexNames(
    (0, "ALCATEL-IND1-AAA-MIB", "aaaUNPMacRuleAddr"),
)
if mibBuilder.loadTexts:
    aaaUNPMacRuleEntry.setStatus("current")
_AaaUNPMacRuleAddr_Type = MacAddress
_AaaUNPMacRuleAddr_Object = MibTableColumn
aaaUNPMacRuleAddr = _AaaUNPMacRuleAddr_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 1, 13, 1, 1),
    _AaaUNPMacRuleAddr_Type()
)
aaaUNPMacRuleAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    aaaUNPMacRuleAddr.setStatus("current")


class _AaaUNPMacRuleProfileName_Type(SnmpAdminString):
    """Custom type aaaUNPMacRuleProfileName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_AaaUNPMacRuleProfileName_Type.__name__ = "SnmpAdminString"
_AaaUNPMacRuleProfileName_Object = MibTableColumn
aaaUNPMacRuleProfileName = _AaaUNPMacRuleProfileName_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 1, 13, 1, 2),
    _AaaUNPMacRuleProfileName_Type()
)
aaaUNPMacRuleProfileName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aaaUNPMacRuleProfileName.setStatus("current")
_AaaUNPMacRuleRowStatus_Type = RowStatus
_AaaUNPMacRuleRowStatus_Object = MibTableColumn
aaaUNPMacRuleRowStatus = _AaaUNPMacRuleRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 1, 13, 1, 3),
    _AaaUNPMacRuleRowStatus_Type()
)
aaaUNPMacRuleRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aaaUNPMacRuleRowStatus.setStatus("current")
_AaaUNPMacRangeRuleTable_Object = MibTable
aaaUNPMacRangeRuleTable = _AaaUNPMacRangeRuleTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 1, 14)
)
if mibBuilder.loadTexts:
    aaaUNPMacRangeRuleTable.setStatus("current")
_AaaUNPMacRangeRuleEntry_Object = MibTableRow
aaaUNPMacRangeRuleEntry = _AaaUNPMacRangeRuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 1, 14, 1)
)
aaaUNPMacRangeRuleEntry.setIndexNames(
    (0, "ALCATEL-IND1-AAA-MIB", "aaaUNPMacRangeRuleLoAddr"),
)
if mibBuilder.loadTexts:
    aaaUNPMacRangeRuleEntry.setStatus("current")
_AaaUNPMacRangeRuleLoAddr_Type = MacAddress
_AaaUNPMacRangeRuleLoAddr_Object = MibTableColumn
aaaUNPMacRangeRuleLoAddr = _AaaUNPMacRangeRuleLoAddr_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 1, 14, 1, 1),
    _AaaUNPMacRangeRuleLoAddr_Type()
)
aaaUNPMacRangeRuleLoAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    aaaUNPMacRangeRuleLoAddr.setStatus("current")
_AaaUNPMacRangeRuleHiAddr_Type = MacAddress
_AaaUNPMacRangeRuleHiAddr_Object = MibTableColumn
aaaUNPMacRangeRuleHiAddr = _AaaUNPMacRangeRuleHiAddr_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 1, 14, 1, 2),
    _AaaUNPMacRangeRuleHiAddr_Type()
)
aaaUNPMacRangeRuleHiAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aaaUNPMacRangeRuleHiAddr.setStatus("current")


class _AaaUNPMacRangeRuleProfileName_Type(SnmpAdminString):
    """Custom type aaaUNPMacRangeRuleProfileName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_AaaUNPMacRangeRuleProfileName_Type.__name__ = "SnmpAdminString"
_AaaUNPMacRangeRuleProfileName_Object = MibTableColumn
aaaUNPMacRangeRuleProfileName = _AaaUNPMacRangeRuleProfileName_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 1, 14, 1, 3),
    _AaaUNPMacRangeRuleProfileName_Type()
)
aaaUNPMacRangeRuleProfileName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aaaUNPMacRangeRuleProfileName.setStatus("current")
_AaaUNPMacRangeRuleRowStatus_Type = RowStatus
_AaaUNPMacRangeRuleRowStatus_Object = MibTableColumn
aaaUNPMacRangeRuleRowStatus = _AaaUNPMacRangeRuleRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 1, 14, 1, 4),
    _AaaUNPMacRangeRuleRowStatus_Type()
)
aaaUNPMacRangeRuleRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aaaUNPMacRangeRuleRowStatus.setStatus("current")
_AaaHicSvrDownUnpMapTable_Object = MibTable
aaaHicSvrDownUnpMapTable = _AaaHicSvrDownUnpMapTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 1, 15)
)
if mibBuilder.loadTexts:
    aaaHicSvrDownUnpMapTable.setStatus("current")
_AaaHicSvrDownUnpMapEntry_Object = MibTableRow
aaaHicSvrDownUnpMapEntry = _AaaHicSvrDownUnpMapEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 1, 15, 1)
)
aaaHicSvrDownUnpMapEntry.setIndexNames(
    (0, "ALCATEL-IND1-AAA-MIB", "aaaHicSvrDownUnpName"),
)
if mibBuilder.loadTexts:
    aaaHicSvrDownUnpMapEntry.setStatus("current")


class _AaaHicSvrDownUnpName_Type(SnmpAdminString):
    """Custom type aaaHicSvrDownUnpName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_AaaHicSvrDownUnpName_Type.__name__ = "SnmpAdminString"
_AaaHicSvrDownUnpName_Object = MibTableColumn
aaaHicSvrDownUnpName = _AaaHicSvrDownUnpName_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 1, 15, 1, 1),
    _AaaHicSvrDownUnpName_Type()
)
aaaHicSvrDownUnpName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    aaaHicSvrDownUnpName.setStatus("current")


class _AaaHicSvrDownMappedUnpName_Type(SnmpAdminString):
    """Custom type aaaHicSvrDownMappedUnpName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_AaaHicSvrDownMappedUnpName_Type.__name__ = "SnmpAdminString"
_AaaHicSvrDownMappedUnpName_Object = MibTableColumn
aaaHicSvrDownMappedUnpName = _AaaHicSvrDownMappedUnpName_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 1, 15, 1, 2),
    _AaaHicSvrDownMappedUnpName_Type()
)
aaaHicSvrDownMappedUnpName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aaaHicSvrDownMappedUnpName.setStatus("current")
_AaaHicSvrDownUnpRowStatus_Type = RowStatus
_AaaHicSvrDownUnpRowStatus_Object = MibTableColumn
aaaHicSvrDownUnpRowStatus = _AaaHicSvrDownUnpRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 1, 15, 1, 3),
    _AaaHicSvrDownUnpRowStatus_Type()
)
aaaHicSvrDownUnpRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aaaHicSvrDownUnpRowStatus.setStatus("current")
_AaaRedirectConfig_ObjectIdentity = ObjectIdentity
aaaRedirectConfig = _AaaRedirectConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 1, 16)
)
_AaaRedirectServerTable_Object = MibTable
aaaRedirectServerTable = _AaaRedirectServerTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 1, 16, 1)
)
if mibBuilder.loadTexts:
    aaaRedirectServerTable.setStatus("current")
_AaaRedirectServerEntry_Object = MibTableRow
aaaRedirectServerEntry = _AaaRedirectServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 1, 16, 1, 1)
)
aaaRedirectServerEntry.setIndexNames(
    (0, "ALCATEL-IND1-AAA-MIB", "aaaRedirectServerName"),
)
if mibBuilder.loadTexts:
    aaaRedirectServerEntry.setStatus("current")


class _AaaRedirectServerName_Type(SnmpAdminString):
    """Custom type aaaRedirectServerName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_AaaRedirectServerName_Type.__name__ = "SnmpAdminString"
_AaaRedirectServerName_Object = MibTableColumn
aaaRedirectServerName = _AaaRedirectServerName_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 1, 16, 1, 1, 1),
    _AaaRedirectServerName_Type()
)
aaaRedirectServerName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    aaaRedirectServerName.setStatus("current")
_AaaRedirectServerIpAddress_Type = IpAddress
_AaaRedirectServerIpAddress_Object = MibTableColumn
aaaRedirectServerIpAddress = _AaaRedirectServerIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 1, 16, 1, 1, 2),
    _AaaRedirectServerIpAddress_Type()
)
aaaRedirectServerIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aaaRedirectServerIpAddress.setStatus("current")


class _AaaRedirectServerUrl1_Type(SnmpAdminString):
    """Custom type aaaRedirectServerUrl1 based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_AaaRedirectServerUrl1_Type.__name__ = "SnmpAdminString"
_AaaRedirectServerUrl1_Object = MibTableColumn
aaaRedirectServerUrl1 = _AaaRedirectServerUrl1_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 1, 16, 1, 1, 3),
    _AaaRedirectServerUrl1_Type()
)
aaaRedirectServerUrl1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aaaRedirectServerUrl1.setStatus("current")


class _AaaRedirectServerUrl2_Type(SnmpAdminString):
    """Custom type aaaRedirectServerUrl2 based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_AaaRedirectServerUrl2_Type.__name__ = "SnmpAdminString"
_AaaRedirectServerUrl2_Object = MibTableColumn
aaaRedirectServerUrl2 = _AaaRedirectServerUrl2_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 1, 16, 1, 1, 4),
    _AaaRedirectServerUrl2_Type()
)
aaaRedirectServerUrl2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aaaRedirectServerUrl2.setStatus("current")


class _AaaRedirectServerUrl3_Type(SnmpAdminString):
    """Custom type aaaRedirectServerUrl3 based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_AaaRedirectServerUrl3_Type.__name__ = "SnmpAdminString"
_AaaRedirectServerUrl3_Object = MibTableColumn
aaaRedirectServerUrl3 = _AaaRedirectServerUrl3_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 1, 16, 1, 1, 5),
    _AaaRedirectServerUrl3_Type()
)
aaaRedirectServerUrl3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aaaRedirectServerUrl3.setStatus("current")


class _AaaRedirectServerUrl4_Type(SnmpAdminString):
    """Custom type aaaRedirectServerUrl4 based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_AaaRedirectServerUrl4_Type.__name__ = "SnmpAdminString"
_AaaRedirectServerUrl4_Object = MibTableColumn
aaaRedirectServerUrl4 = _AaaRedirectServerUrl4_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 1, 16, 1, 1, 6),
    _AaaRedirectServerUrl4_Type()
)
aaaRedirectServerUrl4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aaaRedirectServerUrl4.setStatus("current")


class _AaaRedirectServerUrl5_Type(SnmpAdminString):
    """Custom type aaaRedirectServerUrl5 based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_AaaRedirectServerUrl5_Type.__name__ = "SnmpAdminString"
_AaaRedirectServerUrl5_Object = MibTableColumn
aaaRedirectServerUrl5 = _AaaRedirectServerUrl5_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 1, 16, 1, 1, 7),
    _AaaRedirectServerUrl5_Type()
)
aaaRedirectServerUrl5.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aaaRedirectServerUrl5.setStatus("current")
_AaaRedirectSvrConfigRowStatus_Type = RowStatus
_AaaRedirectSvrConfigRowStatus_Object = MibTableColumn
aaaRedirectSvrConfigRowStatus = _AaaRedirectSvrConfigRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 1, 16, 1, 1, 8),
    _AaaRedirectSvrConfigRowStatus_Type()
)
aaaRedirectSvrConfigRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aaaRedirectSvrConfigRowStatus.setStatus("current")


class _AaaRedirectServerHostName_Type(DisplayString):
    """Custom type aaaRedirectServerHostName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_AaaRedirectServerHostName_Type.__name__ = "DisplayString"
_AaaRedirectServerHostName_Object = MibTableColumn
aaaRedirectServerHostName = _AaaRedirectServerHostName_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 1, 16, 1, 1, 9),
    _AaaRedirectServerHostName_Type()
)
aaaRedirectServerHostName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aaaRedirectServerHostName.setStatus("current")
_AaaRedirectUrlConfigTable_Object = MibTable
aaaRedirectUrlConfigTable = _AaaRedirectUrlConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 1, 16, 2)
)
if mibBuilder.loadTexts:
    aaaRedirectUrlConfigTable.setStatus("current")
_AaaRedirectURLEntry_Object = MibTableRow
aaaRedirectURLEntry = _AaaRedirectURLEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 1, 16, 2, 1)
)
aaaRedirectURLEntry.setIndexNames(
    (0, "ALCATEL-IND1-AAA-MIB", "aaaRedirectServerUrlName"),
)
if mibBuilder.loadTexts:
    aaaRedirectURLEntry.setStatus("current")


class _AaaRedirectServerUrlName_Type(SnmpAdminString):
    """Custom type aaaRedirectServerUrlName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_AaaRedirectServerUrlName_Type.__name__ = "SnmpAdminString"
_AaaRedirectServerUrlName_Object = MibTableColumn
aaaRedirectServerUrlName = _AaaRedirectServerUrlName_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 1, 16, 2, 1, 1),
    _AaaRedirectServerUrlName_Type()
)
aaaRedirectServerUrlName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    aaaRedirectServerUrlName.setStatus("current")


class _AaaRedirectServerUrl_Type(SnmpAdminString):
    """Custom type aaaRedirectServerUrl based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 252),
    )


_AaaRedirectServerUrl_Type.__name__ = "SnmpAdminString"
_AaaRedirectServerUrl_Object = MibTableColumn
aaaRedirectServerUrl = _AaaRedirectServerUrl_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 1, 16, 2, 1, 2),
    _AaaRedirectServerUrl_Type()
)
aaaRedirectServerUrl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aaaRedirectServerUrl.setStatus("current")
_AaaRedirectServerRowStatus_Type = RowStatus
_AaaRedirectServerRowStatus_Object = MibTableColumn
aaaRedirectServerRowStatus = _AaaRedirectServerRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 1, 16, 2, 1, 3),
    _AaaRedirectServerRowStatus_Type()
)
aaaRedirectServerRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aaaRedirectServerRowStatus.setStatus("current")
_AaaRedirectGlobalConfig_ObjectIdentity = ObjectIdentity
aaaRedirectGlobalConfig = _AaaRedirectGlobalConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 1, 16, 3)
)


class _AaaRedirectPauseTimerConfig_Type(Integer32):
    """Custom type aaaRedirectPauseTimerConfig based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 300),
    )


_AaaRedirectPauseTimerConfig_Type.__name__ = "Integer32"
_AaaRedirectPauseTimerConfig_Object = MibScalar
aaaRedirectPauseTimerConfig = _AaaRedirectPauseTimerConfig_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 1, 16, 3, 1),
    _AaaRedirectPauseTimerConfig_Type()
)
aaaRedirectPauseTimerConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aaaRedirectPauseTimerConfig.setStatus("current")


class _AaaPortBounceConfig_Type(Integer32):
    """Custom type aaaPortBounceConfig based on Integer32"""
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


_AaaPortBounceConfig_Type.__name__ = "Integer32"
_AaaPortBounceConfig_Object = MibScalar
aaaPortBounceConfig = _AaaPortBounceConfig_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 1, 16, 3, 2),
    _AaaPortBounceConfig_Type()
)
aaaPortBounceConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aaaPortBounceConfig.setStatus("current")


class _AaaRedirectProxyServerPort_Type(Integer32):
    """Custom type aaaRedirectProxyServerPort based on Integer32"""
    defaultValue = 8080

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1024, 49151),
    )


_AaaRedirectProxyServerPort_Type.__name__ = "Integer32"
_AaaRedirectProxyServerPort_Object = MibScalar
aaaRedirectProxyServerPort = _AaaRedirectProxyServerPort_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 1, 16, 3, 3),
    _AaaRedirectProxyServerPort_Type()
)
aaaRedirectProxyServerPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aaaRedirectProxyServerPort.setStatus("current")
_AaaPortBounceInterfaceTable_Object = MibTable
aaaPortBounceInterfaceTable = _AaaPortBounceInterfaceTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 1, 16, 4)
)
if mibBuilder.loadTexts:
    aaaPortBounceInterfaceTable.setStatus("current")
_AaaPortBounceInterfaceEntry_Object = MibTableRow
aaaPortBounceInterfaceEntry = _AaaPortBounceInterfaceEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 1, 16, 4, 1)
)
aaaPortBounceInterfaceEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    aaaPortBounceInterfaceEntry.setStatus("current")
_AaaPortBouncePortSlot_Type = Integer32
_AaaPortBouncePortSlot_Object = MibTableColumn
aaaPortBouncePortSlot = _AaaPortBouncePortSlot_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 1, 16, 4, 1, 1),
    _AaaPortBouncePortSlot_Type()
)
aaaPortBouncePortSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aaaPortBouncePortSlot.setStatus("current")
_AaaPortBounceIF_Type = Integer32
_AaaPortBounceIF_Object = MibTableColumn
aaaPortBounceIF = _AaaPortBounceIF_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 1, 16, 4, 1, 2),
    _AaaPortBounceIF_Type()
)
aaaPortBounceIF.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aaaPortBounceIF.setStatus("current")


class _AaaPortBounceStatus_Type(Integer32):
    """Custom type aaaPortBounceStatus based on Integer32"""
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


_AaaPortBounceStatus_Type.__name__ = "Integer32"
_AaaPortBounceStatus_Object = MibTableColumn
aaaPortBounceStatus = _AaaPortBounceStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 1, 16, 4, 1, 3),
    _AaaPortBounceStatus_Type()
)
aaaPortBounceStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aaaPortBounceStatus.setStatus("current")
_AaaBYODWhiteListTable_Object = MibTable
aaaBYODWhiteListTable = _AaaBYODWhiteListTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 1, 16, 5)
)
if mibBuilder.loadTexts:
    aaaBYODWhiteListTable.setStatus("current")
_AaaBYODWhiteListEntry_Object = MibTableRow
aaaBYODWhiteListEntry = _AaaBYODWhiteListEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 1, 16, 5, 1)
)
aaaBYODWhiteListEntry.setIndexNames(
    (0, "ALCATEL-IND1-AAA-MIB", "aaaBYODWhiteListIPAddress"),
    (0, "ALCATEL-IND1-AAA-MIB", "aaaBYODWhiteListIPMask"),
)
if mibBuilder.loadTexts:
    aaaBYODWhiteListEntry.setStatus("current")
_AaaBYODWhiteListIPAddress_Type = IpAddress
_AaaBYODWhiteListIPAddress_Object = MibTableColumn
aaaBYODWhiteListIPAddress = _AaaBYODWhiteListIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 1, 16, 5, 1, 1),
    _AaaBYODWhiteListIPAddress_Type()
)
aaaBYODWhiteListIPAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aaaBYODWhiteListIPAddress.setStatus("current")
_AaaBYODWhiteListIPMask_Type = IpAddress
_AaaBYODWhiteListIPMask_Object = MibTableColumn
aaaBYODWhiteListIPMask = _AaaBYODWhiteListIPMask_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 1, 16, 5, 1, 2),
    _AaaBYODWhiteListIPMask_Type()
)
aaaBYODWhiteListIPMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aaaBYODWhiteListIPMask.setStatus("current")
_AaaBYODWhiteListRowStatus_Type = RowStatus
_AaaBYODWhiteListRowStatus_Object = MibTableColumn
aaaBYODWhiteListRowStatus = _AaaBYODWhiteListRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 1, 16, 5, 1, 3),
    _AaaBYODWhiteListRowStatus_Type()
)
aaaBYODWhiteListRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aaaBYODWhiteListRowStatus.setStatus("current")
_AaaSwitchAccessConfig_ObjectIdentity = ObjectIdentity
aaaSwitchAccessConfig = _AaaSwitchAccessConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 1, 17)
)
_AaaSwitchAccessMgmtStationTable_Object = MibTable
aaaSwitchAccessMgmtStationTable = _AaaSwitchAccessMgmtStationTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 1, 17, 1)
)
if mibBuilder.loadTexts:
    aaaSwitchAccessMgmtStationTable.setStatus("current")
_AaaSwitchAccessMgmtStationEntry_Object = MibTableRow
aaaSwitchAccessMgmtStationEntry = _AaaSwitchAccessMgmtStationEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 1, 17, 1, 1)
)
aaaSwitchAccessMgmtStationEntry.setIndexNames(
    (0, "ALCATEL-IND1-AAA-MIB", "aaaSwitchAccessMgmtStationIpAddress"),
)
if mibBuilder.loadTexts:
    aaaSwitchAccessMgmtStationEntry.setStatus("current")
_AaaSwitchAccessMgmtStationIpAddress_Type = IpAddress
_AaaSwitchAccessMgmtStationIpAddress_Object = MibTableColumn
aaaSwitchAccessMgmtStationIpAddress = _AaaSwitchAccessMgmtStationIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 1, 17, 1, 1, 1),
    _AaaSwitchAccessMgmtStationIpAddress_Type()
)
aaaSwitchAccessMgmtStationIpAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aaaSwitchAccessMgmtStationIpAddress.setStatus("current")
_AaaSwitchAccessMgmtStationIpAddressMask_Type = IpAddress
_AaaSwitchAccessMgmtStationIpAddressMask_Object = MibTableColumn
aaaSwitchAccessMgmtStationIpAddressMask = _AaaSwitchAccessMgmtStationIpAddressMask_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 1, 17, 1, 1, 2),
    _AaaSwitchAccessMgmtStationIpAddressMask_Type()
)
aaaSwitchAccessMgmtStationIpAddressMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aaaSwitchAccessMgmtStationIpAddressMask.setStatus("current")


class _AaaSwitchAccessMgmtStationRowStatus_Type(Integer32):
    """Custom type aaaSwitchAccessMgmtStationRowStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_AaaSwitchAccessMgmtStationRowStatus_Type.__name__ = "Integer32"
_AaaSwitchAccessMgmtStationRowStatus_Object = MibTableColumn
aaaSwitchAccessMgmtStationRowStatus = _AaaSwitchAccessMgmtStationRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 1, 17, 1, 1, 3),
    _AaaSwitchAccessMgmtStationRowStatus_Type()
)
aaaSwitchAccessMgmtStationRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aaaSwitchAccessMgmtStationRowStatus.setStatus("current")
_AaaSwitchAccessBannedIpTable_Object = MibTable
aaaSwitchAccessBannedIpTable = _AaaSwitchAccessBannedIpTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 1, 17, 2)
)
if mibBuilder.loadTexts:
    aaaSwitchAccessBannedIpTable.setStatus("current")
_AaaSwitchAccessBannedIpEntry_Object = MibTableRow
aaaSwitchAccessBannedIpEntry = _AaaSwitchAccessBannedIpEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 1, 17, 2, 1)
)
aaaSwitchAccessBannedIpEntry.setIndexNames(
    (0, "ALCATEL-IND1-AAA-MIB", "aaaSwitchAccessBannedIpAddress"),
)
if mibBuilder.loadTexts:
    aaaSwitchAccessBannedIpEntry.setStatus("current")
_AaaSwitchAccessBannedIpAddress_Type = IpAddress
_AaaSwitchAccessBannedIpAddress_Object = MibTableColumn
aaaSwitchAccessBannedIpAddress = _AaaSwitchAccessBannedIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 1, 17, 2, 1, 1),
    _AaaSwitchAccessBannedIpAddress_Type()
)
aaaSwitchAccessBannedIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aaaSwitchAccessBannedIpAddress.setStatus("current")


class _AaaSwitchAccessBannedIpRowStatus_Type(Unsigned32):
    """Custom type aaaSwitchAccessBannedIpRowStatus based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4194967295),
    )


_AaaSwitchAccessBannedIpRowStatus_Type.__name__ = "Unsigned32"
_AaaSwitchAccessBannedIpRowStatus_Object = MibTableColumn
aaaSwitchAccessBannedIpRowStatus = _AaaSwitchAccessBannedIpRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 1, 17, 2, 1, 2),
    _AaaSwitchAccessBannedIpRowStatus_Type()
)
aaaSwitchAccessBannedIpRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aaaSwitchAccessBannedIpRowStatus.setStatus("current")
_AaaSwitchAccessPrivMaskTable_Object = MibTable
aaaSwitchAccessPrivMaskTable = _AaaSwitchAccessPrivMaskTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 1, 17, 3)
)
if mibBuilder.loadTexts:
    aaaSwitchAccessPrivMaskTable.setStatus("current")
_AaaSwitchAccessPrivMaskEntry_Object = MibTableRow
aaaSwitchAccessPrivMaskEntry = _AaaSwitchAccessPrivMaskEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 1, 17, 3, 1)
)
aaaSwitchAccessPrivMaskEntry.setIndexNames(
    (0, "ALCATEL-IND1-AAA-MIB", "aaaSwitchAccessType"),
)
if mibBuilder.loadTexts:
    aaaSwitchAccessPrivMaskEntry.setStatus("current")


class _AaaSwitchAccessType_Type(DisplayString):
    """Custom type aaaSwitchAccessType based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_AaaSwitchAccessType_Type.__name__ = "DisplayString"
_AaaSwitchAccessType_Object = MibTableColumn
aaaSwitchAccessType = _AaaSwitchAccessType_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 1, 17, 3, 1, 1),
    _AaaSwitchAccessType_Type()
)
aaaSwitchAccessType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aaaSwitchAccessType.setStatus("current")


class _AaaSwitchAccessReadRight1_Type(Unsigned32):
    """Custom type aaaSwitchAccessReadRight1 based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_AaaSwitchAccessReadRight1_Type.__name__ = "Unsigned32"
_AaaSwitchAccessReadRight1_Object = MibTableColumn
aaaSwitchAccessReadRight1 = _AaaSwitchAccessReadRight1_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 1, 17, 3, 1, 2),
    _AaaSwitchAccessReadRight1_Type()
)
aaaSwitchAccessReadRight1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aaaSwitchAccessReadRight1.setStatus("current")


class _AaaSwitchAccessReadRight2_Type(Unsigned32):
    """Custom type aaaSwitchAccessReadRight2 based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_AaaSwitchAccessReadRight2_Type.__name__ = "Unsigned32"
_AaaSwitchAccessReadRight2_Object = MibTableColumn
aaaSwitchAccessReadRight2 = _AaaSwitchAccessReadRight2_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 1, 17, 3, 1, 3),
    _AaaSwitchAccessReadRight2_Type()
)
aaaSwitchAccessReadRight2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aaaSwitchAccessReadRight2.setStatus("current")


class _AaaSwitchAccessWriteRight1_Type(Unsigned32):
    """Custom type aaaSwitchAccessWriteRight1 based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_AaaSwitchAccessWriteRight1_Type.__name__ = "Unsigned32"
_AaaSwitchAccessWriteRight1_Object = MibTableColumn
aaaSwitchAccessWriteRight1 = _AaaSwitchAccessWriteRight1_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 1, 17, 3, 1, 4),
    _AaaSwitchAccessWriteRight1_Type()
)
aaaSwitchAccessWriteRight1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aaaSwitchAccessWriteRight1.setStatus("current")


class _AaaSwitchAccessWriteRight2_Type(Unsigned32):
    """Custom type aaaSwitchAccessWriteRight2 based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_AaaSwitchAccessWriteRight2_Type.__name__ = "Unsigned32"
_AaaSwitchAccessWriteRight2_Object = MibTableColumn
aaaSwitchAccessWriteRight2 = _AaaSwitchAccessWriteRight2_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 1, 17, 3, 1, 5),
    _AaaSwitchAccessWriteRight2_Type()
)
aaaSwitchAccessWriteRight2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aaaSwitchAccessWriteRight2.setStatus("current")


class _AaaSwitchAccessPrivMaskRowStatus_Type(RowStatus):
    """Custom type aaaSwitchAccessPrivMaskRowStatus based on RowStatus"""
    defaultValue = 2


_AaaSwitchAccessPrivMaskRowStatus_Type.__name__ = "RowStatus"
_AaaSwitchAccessPrivMaskRowStatus_Object = MibTableColumn
aaaSwitchAccessPrivMaskRowStatus = _AaaSwitchAccessPrivMaskRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 1, 17, 3, 1, 6),
    _AaaSwitchAccessPrivMaskRowStatus_Type()
)
aaaSwitchAccessPrivMaskRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aaaSwitchAccessPrivMaskRowStatus.setStatus("current")
_AlaAaaTlsConfig_ObjectIdentity = ObjectIdentity
alaAaaTlsConfig = _AlaAaaTlsConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 1, 18)
)
_AlaAaaTlsBaseConfig_ObjectIdentity = ObjectIdentity
alaAaaTlsBaseConfig = _AlaAaaTlsBaseConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 1, 18, 1)
)


class _AlaAaaTlsCaFileName_Type(SnmpAdminString):
    """Custom type alaAaaTlsCaFileName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_AlaAaaTlsCaFileName_Type.__name__ = "SnmpAdminString"
_AlaAaaTlsCaFileName_Object = MibScalar
alaAaaTlsCaFileName = _AlaAaaTlsCaFileName_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 1, 18, 1, 1),
    _AlaAaaTlsCaFileName_Type()
)
alaAaaTlsCaFileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaAaaTlsCaFileName.setStatus("current")


class _AlaAaaTlsCrlFileName_Type(SnmpAdminString):
    """Custom type alaAaaTlsCrlFileName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_AlaAaaTlsCrlFileName_Type.__name__ = "SnmpAdminString"
_AlaAaaTlsCrlFileName_Object = MibScalar
alaAaaTlsCrlFileName = _AlaAaaTlsCrlFileName_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 1, 18, 1, 2),
    _AlaAaaTlsCrlFileName_Type()
)
alaAaaTlsCrlFileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaAaaTlsCrlFileName.setStatus("current")


class _AlaAaaTlsKeyFileName_Type(SnmpAdminString):
    """Custom type alaAaaTlsKeyFileName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_AlaAaaTlsKeyFileName_Type.__name__ = "SnmpAdminString"
_AlaAaaTlsKeyFileName_Object = MibScalar
alaAaaTlsKeyFileName = _AlaAaaTlsKeyFileName_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 1, 18, 1, 3),
    _AlaAaaTlsKeyFileName_Type()
)
alaAaaTlsKeyFileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaAaaTlsKeyFileName.setStatus("current")


class _AlaAaaTlsCertFileName_Type(SnmpAdminString):
    """Custom type alaAaaTlsCertFileName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_AlaAaaTlsCertFileName_Type.__name__ = "SnmpAdminString"
_AlaAaaTlsCertFileName_Object = MibScalar
alaAaaTlsCertFileName = _AlaAaaTlsCertFileName_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 1, 18, 1, 4),
    _AlaAaaTlsCertFileName_Type()
)
alaAaaTlsCertFileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaAaaTlsCertFileName.setStatus("current")
_AlaAaaTlsSelfSignedCert_ObjectIdentity = ObjectIdentity
alaAaaTlsSelfSignedCert = _AlaAaaTlsSelfSignedCert_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 1, 18, 2)
)


class _AlaAaaTlsSelfSignedCertFileName_Type(SnmpAdminString):
    """Custom type alaAaaTlsSelfSignedCertFileName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_AlaAaaTlsSelfSignedCertFileName_Type.__name__ = "SnmpAdminString"
_AlaAaaTlsSelfSignedCertFileName_Object = MibScalar
alaAaaTlsSelfSignedCertFileName = _AlaAaaTlsSelfSignedCertFileName_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 1, 18, 2, 1),
    _AlaAaaTlsSelfSignedCertFileName_Type()
)
alaAaaTlsSelfSignedCertFileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaAaaTlsSelfSignedCertFileName.setStatus("current")


class _AlaAaaTlsSelfSignedCertKeyFileName_Type(SnmpAdminString):
    """Custom type alaAaaTlsSelfSignedCertKeyFileName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_AlaAaaTlsSelfSignedCertKeyFileName_Type.__name__ = "SnmpAdminString"
_AlaAaaTlsSelfSignedCertKeyFileName_Object = MibScalar
alaAaaTlsSelfSignedCertKeyFileName = _AlaAaaTlsSelfSignedCertKeyFileName_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 1, 18, 2, 2),
    _AlaAaaTlsSelfSignedCertKeyFileName_Type()
)
alaAaaTlsSelfSignedCertKeyFileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaAaaTlsSelfSignedCertKeyFileName.setStatus("current")


class _AlaAaaTlsSelfSignedCertValidPeriod_Type(Integer32):
    """Custom type alaAaaTlsSelfSignedCertValidPeriod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3650),
    )


_AlaAaaTlsSelfSignedCertValidPeriod_Type.__name__ = "Integer32"
_AlaAaaTlsSelfSignedCertValidPeriod_Object = MibScalar
alaAaaTlsSelfSignedCertValidPeriod = _AlaAaaTlsSelfSignedCertValidPeriod_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 1, 18, 2, 3),
    _AlaAaaTlsSelfSignedCertValidPeriod_Type()
)
alaAaaTlsSelfSignedCertValidPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaAaaTlsSelfSignedCertValidPeriod.setStatus("current")


class _AlaAaaTlsSelfSignedCertCommonName_Type(SnmpAdminString):
    """Custom type alaAaaTlsSelfSignedCertCommonName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AlaAaaTlsSelfSignedCertCommonName_Type.__name__ = "SnmpAdminString"
_AlaAaaTlsSelfSignedCertCommonName_Object = MibScalar
alaAaaTlsSelfSignedCertCommonName = _AlaAaaTlsSelfSignedCertCommonName_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 1, 18, 2, 4),
    _AlaAaaTlsSelfSignedCertCommonName_Type()
)
alaAaaTlsSelfSignedCertCommonName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaAaaTlsSelfSignedCertCommonName.setStatus("current")


class _AlaAaaTlsSelfSignedCertOrgName_Type(SnmpAdminString):
    """Custom type alaAaaTlsSelfSignedCertOrgName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AlaAaaTlsSelfSignedCertOrgName_Type.__name__ = "SnmpAdminString"
_AlaAaaTlsSelfSignedCertOrgName_Object = MibScalar
alaAaaTlsSelfSignedCertOrgName = _AlaAaaTlsSelfSignedCertOrgName_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 1, 18, 2, 5),
    _AlaAaaTlsSelfSignedCertOrgName_Type()
)
alaAaaTlsSelfSignedCertOrgName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaAaaTlsSelfSignedCertOrgName.setStatus("current")


class _AlaAaaTlsSelfSignedCertOrgUnit_Type(SnmpAdminString):
    """Custom type alaAaaTlsSelfSignedCertOrgUnit based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AlaAaaTlsSelfSignedCertOrgUnit_Type.__name__ = "SnmpAdminString"
_AlaAaaTlsSelfSignedCertOrgUnit_Object = MibScalar
alaAaaTlsSelfSignedCertOrgUnit = _AlaAaaTlsSelfSignedCertOrgUnit_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 1, 18, 2, 6),
    _AlaAaaTlsSelfSignedCertOrgUnit_Type()
)
alaAaaTlsSelfSignedCertOrgUnit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaAaaTlsSelfSignedCertOrgUnit.setStatus("current")


class _AlaAaaTlsSelfSignedCertLocality_Type(SnmpAdminString):
    """Custom type alaAaaTlsSelfSignedCertLocality based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AlaAaaTlsSelfSignedCertLocality_Type.__name__ = "SnmpAdminString"
_AlaAaaTlsSelfSignedCertLocality_Object = MibScalar
alaAaaTlsSelfSignedCertLocality = _AlaAaaTlsSelfSignedCertLocality_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 1, 18, 2, 7),
    _AlaAaaTlsSelfSignedCertLocality_Type()
)
alaAaaTlsSelfSignedCertLocality.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaAaaTlsSelfSignedCertLocality.setStatus("current")


class _AlaAaaTlsSelfSignedCertState_Type(SnmpAdminString):
    """Custom type alaAaaTlsSelfSignedCertState based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AlaAaaTlsSelfSignedCertState_Type.__name__ = "SnmpAdminString"
_AlaAaaTlsSelfSignedCertState_Object = MibScalar
alaAaaTlsSelfSignedCertState = _AlaAaaTlsSelfSignedCertState_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 1, 18, 2, 8),
    _AlaAaaTlsSelfSignedCertState_Type()
)
alaAaaTlsSelfSignedCertState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaAaaTlsSelfSignedCertState.setStatus("current")


class _AlaAaaTlsSelfSignedCertCountry_Type(SnmpAdminString):
    """Custom type alaAaaTlsSelfSignedCertCountry based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )
    fixed_length = 2


_AlaAaaTlsSelfSignedCertCountry_Type.__name__ = "SnmpAdminString"
_AlaAaaTlsSelfSignedCertCountry_Object = MibScalar
alaAaaTlsSelfSignedCertCountry = _AlaAaaTlsSelfSignedCertCountry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 1, 18, 2, 9),
    _AlaAaaTlsSelfSignedCertCountry_Type()
)
alaAaaTlsSelfSignedCertCountry.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaAaaTlsSelfSignedCertCountry.setStatus("current")


class _AlaAaaTlsSelfSignedCertAction_Type(Integer32):
    """Custom type alaAaaTlsSelfSignedCertAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("create", 1),
          ("delete", 2))
    )


_AlaAaaTlsSelfSignedCertAction_Type.__name__ = "Integer32"
_AlaAaaTlsSelfSignedCertAction_Object = MibScalar
alaAaaTlsSelfSignedCertAction = _AlaAaaTlsSelfSignedCertAction_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 1, 18, 2, 10),
    _AlaAaaTlsSelfSignedCertAction_Type()
)
alaAaaTlsSelfSignedCertAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaAaaTlsSelfSignedCertAction.setStatus("current")
_AlaAaaTlsCsr_ObjectIdentity = ObjectIdentity
alaAaaTlsCsr = _AlaAaaTlsCsr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 1, 18, 3)
)


class _AlaAaaTlsCsrFileName_Type(SnmpAdminString):
    """Custom type alaAaaTlsCsrFileName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_AlaAaaTlsCsrFileName_Type.__name__ = "SnmpAdminString"
_AlaAaaTlsCsrFileName_Object = MibScalar
alaAaaTlsCsrFileName = _AlaAaaTlsCsrFileName_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 1, 18, 3, 1),
    _AlaAaaTlsCsrFileName_Type()
)
alaAaaTlsCsrFileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaAaaTlsCsrFileName.setStatus("current")


class _AlaAaaTlsCsrKeyFileName_Type(SnmpAdminString):
    """Custom type alaAaaTlsCsrKeyFileName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_AlaAaaTlsCsrKeyFileName_Type.__name__ = "SnmpAdminString"
_AlaAaaTlsCsrKeyFileName_Object = MibScalar
alaAaaTlsCsrKeyFileName = _AlaAaaTlsCsrKeyFileName_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 1, 18, 3, 2),
    _AlaAaaTlsCsrKeyFileName_Type()
)
alaAaaTlsCsrKeyFileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaAaaTlsCsrKeyFileName.setStatus("current")


class _AlaAaaTlsCsrCommonName_Type(SnmpAdminString):
    """Custom type alaAaaTlsCsrCommonName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AlaAaaTlsCsrCommonName_Type.__name__ = "SnmpAdminString"
_AlaAaaTlsCsrCommonName_Object = MibScalar
alaAaaTlsCsrCommonName = _AlaAaaTlsCsrCommonName_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 1, 18, 3, 3),
    _AlaAaaTlsCsrCommonName_Type()
)
alaAaaTlsCsrCommonName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaAaaTlsCsrCommonName.setStatus("current")


class _AlaAaaTlsCsrOrgName_Type(SnmpAdminString):
    """Custom type alaAaaTlsCsrOrgName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AlaAaaTlsCsrOrgName_Type.__name__ = "SnmpAdminString"
_AlaAaaTlsCsrOrgName_Object = MibScalar
alaAaaTlsCsrOrgName = _AlaAaaTlsCsrOrgName_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 1, 18, 3, 4),
    _AlaAaaTlsCsrOrgName_Type()
)
alaAaaTlsCsrOrgName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaAaaTlsCsrOrgName.setStatus("current")


class _AlaAaaTlsCsrOrgUnit_Type(SnmpAdminString):
    """Custom type alaAaaTlsCsrOrgUnit based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AlaAaaTlsCsrOrgUnit_Type.__name__ = "SnmpAdminString"
_AlaAaaTlsCsrOrgUnit_Object = MibScalar
alaAaaTlsCsrOrgUnit = _AlaAaaTlsCsrOrgUnit_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 1, 18, 3, 5),
    _AlaAaaTlsCsrOrgUnit_Type()
)
alaAaaTlsCsrOrgUnit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaAaaTlsCsrOrgUnit.setStatus("current")


class _AlaAaaTlsCsrLocality_Type(SnmpAdminString):
    """Custom type alaAaaTlsCsrLocality based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AlaAaaTlsCsrLocality_Type.__name__ = "SnmpAdminString"
_AlaAaaTlsCsrLocality_Object = MibScalar
alaAaaTlsCsrLocality = _AlaAaaTlsCsrLocality_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 1, 18, 3, 6),
    _AlaAaaTlsCsrLocality_Type()
)
alaAaaTlsCsrLocality.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaAaaTlsCsrLocality.setStatus("current")


class _AlaAaaTlsCsrState_Type(SnmpAdminString):
    """Custom type alaAaaTlsCsrState based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AlaAaaTlsCsrState_Type.__name__ = "SnmpAdminString"
_AlaAaaTlsCsrState_Object = MibScalar
alaAaaTlsCsrState = _AlaAaaTlsCsrState_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 1, 18, 3, 7),
    _AlaAaaTlsCsrState_Type()
)
alaAaaTlsCsrState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaAaaTlsCsrState.setStatus("current")


class _AlaAaaTlsCsrCountry_Type(SnmpAdminString):
    """Custom type alaAaaTlsCsrCountry based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )
    fixed_length = 2


_AlaAaaTlsCsrCountry_Type.__name__ = "SnmpAdminString"
_AlaAaaTlsCsrCountry_Object = MibScalar
alaAaaTlsCsrCountry = _AlaAaaTlsCsrCountry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 1, 18, 3, 8),
    _AlaAaaTlsCsrCountry_Type()
)
alaAaaTlsCsrCountry.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaAaaTlsCsrCountry.setStatus("current")
_AaaUNPLldpRuleConfig_ObjectIdentity = ObjectIdentity
aaaUNPLldpRuleConfig = _AaaUNPLldpRuleConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 1, 19)
)


class _AaaUNPLldpRuleProfileName_Type(SnmpAdminString):
    """Custom type aaaUNPLldpRuleProfileName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_AaaUNPLldpRuleProfileName_Type.__name__ = "SnmpAdminString"
_AaaUNPLldpRuleProfileName_Object = MibScalar
aaaUNPLldpRuleProfileName = _AaaUNPLldpRuleProfileName_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 1, 19, 1),
    _AaaUNPLldpRuleProfileName_Type()
)
aaaUNPLldpRuleProfileName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aaaUNPLldpRuleProfileName.setStatus("current")
_AlaAaaRadClientGlobalAttr_ObjectIdentity = ObjectIdentity
alaAaaRadClientGlobalAttr = _AlaAaaRadClientGlobalAttr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 1, 20)
)


class _AlaAaaRadNasIdentifier_Type(SnmpAdminString):
    """Custom type alaAaaRadNasIdentifier based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_AlaAaaRadNasIdentifier_Type.__name__ = "SnmpAdminString"
_AlaAaaRadNasIdentifier_Object = MibScalar
alaAaaRadNasIdentifier = _AlaAaaRadNasIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 1, 20, 1),
    _AlaAaaRadNasIdentifier_Type()
)
alaAaaRadNasIdentifier.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaAaaRadNasIdentifier.setStatus("current")
_AlaAaaRadClientNasIpAddr_ObjectIdentity = ObjectIdentity
alaAaaRadClientNasIpAddr = _AlaAaaRadClientNasIpAddr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 1, 21)
)


class _AlaAaaRadNasIpState_Type(Integer32):
    """Custom type alaAaaRadNasIpState based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("default", 0),
          ("localipaddr", 1))
    )


_AlaAaaRadNasIpState_Type.__name__ = "Integer32"
_AlaAaaRadNasIpState_Object = MibScalar
alaAaaRadNasIpState = _AlaAaaRadNasIpState_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 1, 21, 1),
    _AlaAaaRadNasIpState_Type()
)
alaAaaRadNasIpState.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaAaaRadNasIpState.setStatus("current")


class _AlaAaaRadNasIpField_Type(IpAddress):
    """Custom type alaAaaRadNasIpField based on IpAddress"""
    defaultHexValue = "00000000"


_AlaAaaRadNasIpField_Type.__name__ = "IpAddress"
_AlaAaaRadNasIpField_Object = MibScalar
alaAaaRadNasIpField = _AlaAaaRadNasIpField_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 1, 21, 2),
    _AlaAaaRadNasIpField_Type()
)
alaAaaRadNasIpField.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaAaaRadNasIpField.setStatus("current")
_AlcatelIND1AAAMIBConformance_ObjectIdentity = ObjectIdentity
alcatelIND1AAAMIBConformance = _AlcatelIND1AAAMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 2)
)
if mibBuilder.loadTexts:
    alcatelIND1AAAMIBConformance.setStatus("current")
_AlcatelIND1AAAMIBGroups_ObjectIdentity = ObjectIdentity
alcatelIND1AAAMIBGroups = _AlcatelIND1AAAMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 2, 1)
)
if mibBuilder.loadTexts:
    alcatelIND1AAAMIBGroups.setStatus("current")
_AlcatelIND1AAAMIBCompliances_ObjectIdentity = ObjectIdentity
alcatelIND1AAAMIBCompliances = _AlcatelIND1AAAMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 2, 2)
)
if mibBuilder.loadTexts:
    alcatelIND1AAAMIBCompliances.setStatus("current")
_AlaAaaTrapsDesc_ObjectIdentity = ObjectIdentity
alaAaaTrapsDesc = _AlaAaaTrapsDesc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 3, 2, 21, 1)
)
_AlaAaaTrapsDescRoot_ObjectIdentity = ObjectIdentity
alaAaaTrapsDescRoot = _AlaAaaTrapsDescRoot_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 3, 2, 21, 1, 0)
)
_AlaAaaTrapsObj_ObjectIdentity = ObjectIdentity
alaAaaTrapsObj = _AlaAaaTrapsObj_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 3, 2, 21, 2)
)
_AaaHSvrIpAddress_Type = IpAddress
_AaaHSvrIpAddress_Object = MibScalar
aaaHSvrIpAddress = _AaaHSvrIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 3, 2, 21, 2, 1),
    _AaaHSvrIpAddress_Type()
)
aaaHSvrIpAddress.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    aaaHSvrIpAddress.setStatus("current")
_AaaHSvrCurrIpAddress_Type = IpAddress
_AaaHSvrCurrIpAddress_Object = MibScalar
aaaHSvrCurrIpAddress = _AaaHSvrCurrIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 3, 2, 21, 2, 2),
    _AaaHSvrCurrIpAddress_Type()
)
aaaHSvrCurrIpAddress.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    aaaHSvrCurrIpAddress.setStatus("current")
_AaaHSvrRole_Type = Integer32
_AaaHSvrRole_Object = MibScalar
aaaHSvrRole = _AaaHSvrRole_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 3, 2, 21, 2, 3),
    _AaaHSvrRole_Type()
)
aaaHSvrRole.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    aaaHSvrRole.setStatus("current")
_AaaHSvrName_Type = DisplayString
_AaaHSvrName_Object = MibScalar
aaaHSvrName = _AaaHSvrName_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 3, 2, 21, 2, 4),
    _AaaHSvrName_Type()
)
aaaHSvrName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    aaaHSvrName.setStatus("current")
_AlaAaaAuthTrapsDesc_ObjectIdentity = ObjectIdentity
alaAaaAuthTrapsDesc = _AlaAaaAuthTrapsDesc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 3, 2, 21, 3)
)
_AlaAaaAuthTrapsDescRoot_ObjectIdentity = ObjectIdentity
alaAaaAuthTrapsDescRoot = _AlaAaaAuthTrapsDescRoot_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 3, 2, 21, 3, 0)
)
_AlaAaaAuthTrapsObj_ObjectIdentity = ObjectIdentity
alaAaaAuthTrapsObj = _AlaAaaAuthTrapsObj_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 3, 2, 21, 4)
)
_AaaAuthSysName_Type = DisplayString
_AaaAuthSysName_Object = MibScalar
aaaAuthSysName = _AaaAuthSysName_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 3, 2, 21, 4, 1),
    _AaaAuthSysName_Type()
)
aaaAuthSysName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    aaaAuthSysName.setStatus("current")
_AaaAuthIpAddress_Type = IpAddress
_AaaAuthIpAddress_Object = MibScalar
aaaAuthIpAddress = _AaaAuthIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 3, 2, 21, 4, 2),
    _AaaAuthIpAddress_Type()
)
aaaAuthIpAddress.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    aaaAuthIpAddress.setStatus("current")
_AaaAuthPort_Type = Integer32
_AaaAuthPort_Object = MibScalar
aaaAuthPort = _AaaAuthPort_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 3, 2, 21, 4, 3),
    _AaaAuthPort_Type()
)
aaaAuthPort.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    aaaAuthPort.setStatus("current")
_AaaAuthUserName_Type = DisplayString
_AaaAuthUserName_Object = MibScalar
aaaAuthUserName = _AaaAuthUserName_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 3, 2, 21, 4, 4),
    _AaaAuthUserName_Type()
)
aaaAuthUserName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    aaaAuthUserName.setStatus("current")
_AaaAuthType_Type = DisplayString
_AaaAuthType_Object = MibScalar
aaaAuthType = _AaaAuthType_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 3, 2, 21, 4, 5),
    _AaaAuthType_Type()
)
aaaAuthType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    aaaAuthType.setStatus("current")
_AaaAuthFailureReason_Type = Integer32
_AaaAuthFailureReason_Object = MibScalar
aaaAuthFailureReason = _AaaAuthFailureReason_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 3, 2, 21, 4, 6),
    _AaaAuthFailureReason_Type()
)
aaaAuthFailureReason.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    aaaAuthFailureReason.setStatus("current")
_AlaAaaRadiusTrapsDesc_ObjectIdentity = ObjectIdentity
alaAaaRadiusTrapsDesc = _AlaAaaRadiusTrapsDesc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 3, 2, 21, 5)
)
_AlaAaaRadiusTrapsDescRoot_ObjectIdentity = ObjectIdentity
alaAaaRadiusTrapsDescRoot = _AlaAaaRadiusTrapsDescRoot_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 3, 2, 21, 5, 0)
)

# Managed Objects groups

aaaServerMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 2, 1, 1)
)
aaaServerMIBGroup.setObjects(
      *(("ALCATEL-IND1-AAA-MIB", "aaasName"),
        ("ALCATEL-IND1-AAA-MIB", "aaasProtocol"),
        ("ALCATEL-IND1-AAA-MIB", "aaasHostName"),
        ("ALCATEL-IND1-AAA-MIB", "aaasIpAddress"),
        ("ALCATEL-IND1-AAA-MIB", "aaasHostName2"),
        ("ALCATEL-IND1-AAA-MIB", "aaasIpAddress2"),
        ("ALCATEL-IND1-AAA-MIB", "aaasRetries"),
        ("ALCATEL-IND1-AAA-MIB", "aaasTimout"),
        ("ALCATEL-IND1-AAA-MIB", "aaasRadKey"),
        ("ALCATEL-IND1-AAA-MIB", "aaasRadAuthPort"),
        ("ALCATEL-IND1-AAA-MIB", "aaasRadAcctPort"),
        ("ALCATEL-IND1-AAA-MIB", "aaasLdapPort"),
        ("ALCATEL-IND1-AAA-MIB", "aaasLdapDn"),
        ("ALCATEL-IND1-AAA-MIB", "aaasLdapPasswd"),
        ("ALCATEL-IND1-AAA-MIB", "aaasLdapSearchBase"),
        ("ALCATEL-IND1-AAA-MIB", "aaasLdapServType"),
        ("ALCATEL-IND1-AAA-MIB", "aaasLdapEnableSsl"),
        ("ALCATEL-IND1-AAA-MIB", "aaasAceClear"),
        ("ALCATEL-IND1-AAA-MIB", "aaasRowStatus"),
        ("ALCATEL-IND1-AAA-MIB", "aaasTacacsKey"),
        ("ALCATEL-IND1-AAA-MIB", "aaasTacacsPort"),
        ("ALCATEL-IND1-AAA-MIB", "aaasHttpPort"),
        ("ALCATEL-IND1-AAA-MIB", "aaasHttpDirectory"),
        ("ALCATEL-IND1-AAA-MIB", "aaasHttpProxyHostName"),
        ("ALCATEL-IND1-AAA-MIB", "aaasHttpProxyIpAddress"),
        ("ALCATEL-IND1-AAA-MIB", "aaasHttpProxyPort"),
        ("ALCATEL-IND1-AAA-MIB", "aaasVrfName"),
        ("ALCATEL-IND1-AAA-MIB", "aaasRadMacAddrCase"),
        ("ALCATEL-IND1-AAA-MIB", "aaaTacacsServerCmdAuthorization"),
        ("ALCATEL-IND1-AAA-MIB", "aaasRadNasPort"),
        ("ALCATEL-IND1-AAA-MIB", "aaasRadNasPortId"),
        ("ALCATEL-IND1-AAA-MIB", "aaasRadNasPortType"),
        ("ALCATEL-IND1-AAA-MIB", "aaasRadMacAddrFormat"),
        ("ALCATEL-IND1-AAA-MIB", "aaasRadUniqueAcctSessionId"),
        ("ALCATEL-IND1-AAA-MIB", "aaasRadMacAddrCaseStatus"),
        ("ALCATEL-IND1-AAA-MIB", "aaasRadServerStatus"),
        ("ALCATEL-IND1-AAA-MIB", "aaasRadHealthstatus"),
        ("ALCATEL-IND1-AAA-MIB", "aaasRadPollInterval"),
        ("ALCATEL-IND1-AAA-MIB", "aaasRadFailoverStatus"),
        ("ALCATEL-IND1-AAA-MIB", "aaasRadUser"),
        ("ALCATEL-IND1-AAA-MIB", "aaasRadPasswd"),
        ("ALCATEL-IND1-AAA-MIB", "aaaRadServerPrimaryStatus"),
        ("ALCATEL-IND1-AAA-MIB", "aaaRadServerBackupStatus"),
        ("ALCATEL-IND1-AAA-MIB", "aaasRadKeyHash"),
        ("ALCATEL-IND1-AAA-MIB", "aaaRadPrimSerNbUpToDown"),
        ("ALCATEL-IND1-AAA-MIB", "aaaRadPrimSerNbDownToUp"),
        ("ALCATEL-IND1-AAA-MIB", "aaaRadPrimServUpTime"),
        ("ALCATEL-IND1-AAA-MIB", "aaaRadPrimServDownTime"),
        ("ALCATEL-IND1-AAA-MIB", "aaaRadBkupSerNbUpToDown"),
        ("ALCATEL-IND1-AAA-MIB", "aaaRadBkupSerNbDownToUp"),
        ("ALCATEL-IND1-AAA-MIB", "aaaRadBkupServUpTime"),
        ("ALCATEL-IND1-AAA-MIB", "aaaRadBkupServDownTime"),
        ("ALCATEL-IND1-AAA-MIB", "aaasRadSalt"),
        ("ALCATEL-IND1-AAA-MIB", "aaasRadSaltHash"))
)
if mibBuilder.loadTexts:
    aaaServerMIBGroup.setStatus("current")

aaaAuthAcctGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 2, 1, 2)
)
aaaAuthAcctGroup.setObjects(
      *(("ALCATEL-IND1-AAA-MIB", "aaatvVlan"),
        ("ALCATEL-IND1-AAA-MIB", "aaatvName1"),
        ("ALCATEL-IND1-AAA-MIB", "aaatvName2"),
        ("ALCATEL-IND1-AAA-MIB", "aaatvName3"),
        ("ALCATEL-IND1-AAA-MIB", "aaatvName4"),
        ("ALCATEL-IND1-AAA-MIB", "aaatvRowStatus"),
        ("ALCATEL-IND1-AAA-MIB", "aaatvCertificate"),
        ("ALCATEL-IND1-AAA-MIB", "aaatsInterface"),
        ("ALCATEL-IND1-AAA-MIB", "aaatsName1"),
        ("ALCATEL-IND1-AAA-MIB", "aaatsName2"),
        ("ALCATEL-IND1-AAA-MIB", "aaatsName3"),
        ("ALCATEL-IND1-AAA-MIB", "aaatsName4"),
        ("ALCATEL-IND1-AAA-MIB", "aaatsRowStatus"),
        ("ALCATEL-IND1-AAA-MIB", "aaatsCertificate"),
        ("ALCATEL-IND1-AAA-MIB", "aaatsName5"),
        ("ALCATEL-IND1-AAA-MIB", "aaacvVlan"),
        ("ALCATEL-IND1-AAA-MIB", "aaacvName1"),
        ("ALCATEL-IND1-AAA-MIB", "aaacvName2"),
        ("ALCATEL-IND1-AAA-MIB", "aaacvName3"),
        ("ALCATEL-IND1-AAA-MIB", "aaacvName4"),
        ("ALCATEL-IND1-AAA-MIB", "aaacvRowStatus"),
        ("ALCATEL-IND1-AAA-MIB", "aaacsInterface"),
        ("ALCATEL-IND1-AAA-MIB", "aaacsName1"),
        ("ALCATEL-IND1-AAA-MIB", "aaacsName2"),
        ("ALCATEL-IND1-AAA-MIB", "aaacsName3"),
        ("ALCATEL-IND1-AAA-MIB", "aaacsName4"),
        ("ALCATEL-IND1-AAA-MIB", "aaacsRowStatus"),
        ("ALCATEL-IND1-AAA-MIB", "aaatxInterface"),
        ("ALCATEL-IND1-AAA-MIB", "aaatxName1"),
        ("ALCATEL-IND1-AAA-MIB", "aaatxName2"),
        ("ALCATEL-IND1-AAA-MIB", "aaatxName3"),
        ("ALCATEL-IND1-AAA-MIB", "aaatxName4"),
        ("ALCATEL-IND1-AAA-MIB", "aaatxOpen"),
        ("ALCATEL-IND1-AAA-MIB", "aaatxRowStatus"),
        ("ALCATEL-IND1-AAA-MIB", "aaatxName5"),
        ("ALCATEL-IND1-AAA-MIB", "aaacxInterface"),
        ("ALCATEL-IND1-AAA-MIB", "aaacxName1"),
        ("ALCATEL-IND1-AAA-MIB", "aaacxName2"),
        ("ALCATEL-IND1-AAA-MIB", "aaacxName3"),
        ("ALCATEL-IND1-AAA-MIB", "aaacxName4"),
        ("ALCATEL-IND1-AAA-MIB", "aaacxRowStatus"),
        ("ALCATEL-IND1-AAA-MIB", "aaaAcctSvrInterface"),
        ("ALCATEL-IND1-AAA-MIB", "aaaAcctSvr1"),
        ("ALCATEL-IND1-AAA-MIB", "aaaAcctSvr2"),
        ("ALCATEL-IND1-AAA-MIB", "aaaAcctSvr3"),
        ("ALCATEL-IND1-AAA-MIB", "aaaAcctSvr4"),
        ("ALCATEL-IND1-AAA-MIB", "aaaAcctSvrRowStatus"),
        ("ALCATEL-IND1-AAA-MIB", "aaatpInterface"),
        ("ALCATEL-IND1-AAA-MIB", "aaatpName1"),
        ("ALCATEL-IND1-AAA-MIB", "aaatpName2"),
        ("ALCATEL-IND1-AAA-MIB", "aaatpName3"),
        ("ALCATEL-IND1-AAA-MIB", "aaatpName4"),
        ("ALCATEL-IND1-AAA-MIB", "aaatpLevel"),
        ("ALCATEL-IND1-AAA-MIB", "aaatpRowStatus"),
        ("ALCATEL-IND1-AAA-MIB", "aaacmdInterface"),
        ("ALCATEL-IND1-AAA-MIB", "aaacmdSrvName1"),
        ("ALCATEL-IND1-AAA-MIB", "aaacmdSrvName2"),
        ("ALCATEL-IND1-AAA-MIB", "aaacmdSrvName3"),
        ("ALCATEL-IND1-AAA-MIB", "aaacmdSrvName4"),
        ("ALCATEL-IND1-AAA-MIB", "aaacmdRowStatus"))
)
if mibBuilder.loadTexts:
    aaaAuthAcctGroup.setStatus("current")

aaaUserMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 2, 1, 3)
)
aaaUserMIBGroup.setObjects(
      *(("ALCATEL-IND1-AAA-MIB", "aaauUserName"),
        ("ALCATEL-IND1-AAA-MIB", "aaauPassword"),
        ("ALCATEL-IND1-AAA-MIB", "aaauReadRight1"),
        ("ALCATEL-IND1-AAA-MIB", "aaauReadRight2"),
        ("ALCATEL-IND1-AAA-MIB", "aaauWriteRight1"),
        ("ALCATEL-IND1-AAA-MIB", "aaauWriteRight2"),
        ("ALCATEL-IND1-AAA-MIB", "aaauProfile"),
        ("ALCATEL-IND1-AAA-MIB", "aaauSnmpLevel"),
        ("ALCATEL-IND1-AAA-MIB", "aaauSnmpAuthKey"),
        ("ALCATEL-IND1-AAA-MIB", "aaauRowStatus"),
        ("ALCATEL-IND1-AAA-MIB", "aaauOldPassword"),
        ("ALCATEL-IND1-AAA-MIB", "aaauEndUserProfile"),
        ("ALCATEL-IND1-AAA-MIB", "aaauPasswordExpirationDate"),
        ("ALCATEL-IND1-AAA-MIB", "aaauPasswordExpirationInMinute"),
        ("ALCATEL-IND1-AAA-MIB", "aaauPasswordAllowModifyDate"),
        ("ALCATEL-IND1-AAA-MIB", "aaauPasswordLockoutEnable"),
        ("ALCATEL-IND1-AAA-MIB", "aaauBadAtempts"),
        ("ALCATEL-IND1-AAA-MIB", "aaaAsaPasswordSizeMin"),
        ("ALCATEL-IND1-AAA-MIB", "aaaAsaDefaultPasswordExpirationInDays"),
        ("ALCATEL-IND1-AAA-MIB", "aaaAsaPasswordContainUserName"),
        ("ALCATEL-IND1-AAA-MIB", "aaaAsaPasswordMinUpperCase"),
        ("ALCATEL-IND1-AAA-MIB", "aaaAsaPasswordMinLowerCase"),
        ("ALCATEL-IND1-AAA-MIB", "aaaAsaPasswordMinDigit"),
        ("ALCATEL-IND1-AAA-MIB", "aaaAsaPasswordMinNonAlphan"),
        ("ALCATEL-IND1-AAA-MIB", "aaaAsaPasswordHistory"),
        ("ALCATEL-IND1-AAA-MIB", "aaaAsaPasswordMinAge"),
        ("ALCATEL-IND1-AAA-MIB", "aaaAsaLockoutWindow"),
        ("ALCATEL-IND1-AAA-MIB", "aaaAsaLockoutDuration"),
        ("ALCATEL-IND1-AAA-MIB", "aaaAsaLockoutThreshold"),
        ("ALCATEL-IND1-AAA-MIB", "aaauSnmpPrivPassword"),
        ("ALCATEL-IND1-AAA-MIB", "aaauSnmpOnly"),
        ("ALCATEL-IND1-AAA-MIB", "aaaAsaROUserPingTrtEnable"),
        ("ALCATEL-IND1-AAA-MIB", "aaaAsaAccessPolicyAdminConsoleOnly"),
        ("ALCATEL-IND1-AAA-MIB", "aaaAsaCertPassword"),
        ("ALCATEL-IND1-AAA-MIB", "aaaAsaAccessMode"),
        ("ALCATEL-IND1-AAA-MIB", "aaaAsaIpLockoutThreshold"),
        ("ALCATEL-IND1-AAA-MIB", "aaaSwitchAccessMgmtStationState"))
)
if mibBuilder.loadTexts:
    aaaUserMIBGroup.setStatus("current")

aaaHicGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 2, 1, 4)
)
aaaHicGroup.setObjects(
      *(("ALCATEL-IND1-AAA-MIB", "aaaHicSvrIpAddr"),
        ("ALCATEL-IND1-AAA-MIB", "aaaHicSvrPort"),
        ("ALCATEL-IND1-AAA-MIB", "aaaHicSvrKey"),
        ("ALCATEL-IND1-AAA-MIB", "aaaHicSvrRowStatus"),
        ("ALCATEL-IND1-AAA-MIB", "aaaHicSvrStatus"),
        ("ALCATEL-IND1-AAA-MIB", "aaaHicSvrRole"),
        ("ALCATEL-IND1-AAA-MIB", "aaaHicSvrConnection"),
        ("ALCATEL-IND1-AAA-MIB", "aaaHicAllowedIpAddr"),
        ("ALCATEL-IND1-AAA-MIB", "aaaHicAllowedRowStatus"),
        ("ALCATEL-IND1-AAA-MIB", "aaaHicAllowedIpMask"),
        ("ALCATEL-IND1-AAA-MIB", "aaaHicOverrideStatus"),
        ("ALCATEL-IND1-AAA-MIB", "aaaHicOverrideRowStatus"),
        ("ALCATEL-IND1-AAA-MIB", "aaaHicHostStatus"),
        ("ALCATEL-IND1-AAA-MIB", "aaaHicStatus"),
        ("ALCATEL-IND1-AAA-MIB", "aaaHicAllowed1Name"),
        ("ALCATEL-IND1-AAA-MIB", "aaaHicAllowed2Name"),
        ("ALCATEL-IND1-AAA-MIB", "aaaHicAllowed3Name"),
        ("ALCATEL-IND1-AAA-MIB", "aaaHicAllowed4Name"),
        ("ALCATEL-IND1-AAA-MIB", "aaaHicWebAgentDownloadUrl"),
        ("ALCATEL-IND1-AAA-MIB", "aaaHicCustomHttpProxyPort"),
        ("ALCATEL-IND1-AAA-MIB", "aaaHicBgPollInterval"),
        ("ALCATEL-IND1-AAA-MIB", "aaaHicSvrFailMode"),
        ("ALCATEL-IND1-AAA-MIB", "aaaHicSvrDownMappedUnpName"),
        ("ALCATEL-IND1-AAA-MIB", "aaaHicSvrDownUnpRowStatus"),
        ("ALCATEL-IND1-AAA-MIB", "aaaHSvrIpAddress"),
        ("ALCATEL-IND1-AAA-MIB", "aaaHSvrCurrIpAddress"),
        ("ALCATEL-IND1-AAA-MIB", "aaaHSvrRole"),
        ("ALCATEL-IND1-AAA-MIB", "aaaHSvrName"),
        ("ALCATEL-IND1-AAA-MIB", "aaaMacInterface"),
        ("ALCATEL-IND1-AAA-MIB", "aaaMacSrvrName1"),
        ("ALCATEL-IND1-AAA-MIB", "aaaMacSrvrName2"),
        ("ALCATEL-IND1-AAA-MIB", "aaaMacSrvrName3"),
        ("ALCATEL-IND1-AAA-MIB", "aaaMacSrvrName4"),
        ("ALCATEL-IND1-AAA-MIB", "aaaMacSrvrRowStatus"),
        ("ALCATEL-IND1-AAA-MIB", "aaaMacSrvrName5"),
        ("ALCATEL-IND1-AAA-MIB", "aaaRadAgentConfig"),
        ("ALCATEL-IND1-AAA-MIB", "aaaRadAgentIP"),
        ("ALCATEL-IND1-AAA-MIB", "aaaUNPIpNetRuleProfileName"),
        ("ALCATEL-IND1-AAA-MIB", "aaaUNPIpNetRuleRowStatus"))
)
if mibBuilder.loadTexts:
    aaaHicGroup.setStatus("current")

aaaVlanGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 2, 1, 6)
)
aaaVlanGroup.setObjects(
      *(("ALCATEL-IND1-AAA-MIB", "aaaAvlanDnsName"),
        ("ALCATEL-IND1-AAA-MIB", "aaaAvlanDhcpDefGateway"),
        ("ALCATEL-IND1-AAA-MIB", "aaaAvlanDefaultTraffic"),
        ("ALCATEL-IND1-AAA-MIB", "aaaAvlanPortBound"),
        ("ALCATEL-IND1-AAA-MIB", "aaaAvlanLanguage"),
        ("ALCATEL-IND1-AAA-MIB", "aaaAvlanId"),
        ("ALCATEL-IND1-AAA-MIB", "aaaAvlanIpAddress"))
)
if mibBuilder.loadTexts:
    aaaVlanGroup.setStatus("current")

aaaUNPMacRangeRuleGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 2, 1, 7)
)
aaaUNPMacRangeRuleGroup.setObjects(
      *(("ALCATEL-IND1-AAA-MIB", "aaaUNPMacRangeRuleHiAddr"),
        ("ALCATEL-IND1-AAA-MIB", "aaaUNPMacRangeRuleProfileName"),
        ("ALCATEL-IND1-AAA-MIB", "aaaUNPMacRangeRuleRowStatus"))
)
if mibBuilder.loadTexts:
    aaaUNPMacRangeRuleGroup.setStatus("current")

aaaUNPMacRuleGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 2, 1, 8)
)
aaaUNPMacRuleGroup.setObjects(
      *(("ALCATEL-IND1-AAA-MIB", "aaaUNPMacRuleProfileName"),
        ("ALCATEL-IND1-AAA-MIB", "aaaUNPMacRuleRowStatus"))
)
if mibBuilder.loadTexts:
    aaaUNPMacRuleGroup.setStatus("current")

aaaUserNetProfileGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 2, 1, 9)
)
aaaUserNetProfileGroup.setObjects(
      *(("ALCATEL-IND1-AAA-MIB", "aaaUserNetProfileVlanID"),
        ("ALCATEL-IND1-AAA-MIB", "aaaUserNetProfileRowStatus"),
        ("ALCATEL-IND1-AAA-MIB", "aaaUserNetProfileHICflag"),
        ("ALCATEL-IND1-AAA-MIB", "aaaUserNetProfileQosPolicyListName"),
        ("ALCATEL-IND1-AAA-MIB", "aaaUserNetProfileMaxIngressBw"),
        ("ALCATEL-IND1-AAA-MIB", "aaaUserNetProfileMaxEgressBw"),
        ("ALCATEL-IND1-AAA-MIB", "aaaUserNetProfileMaxDefaultDepth"),
        ("ALCATEL-IND1-AAA-MIB", "aaaUserNetworkProfileRedirectUrl"))
)
if mibBuilder.loadTexts:
    aaaUserNetProfileGroup.setStatus("current")

aaaAuthenticatedUserGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 2, 1, 10)
)
aaaAuthenticatedUserGroup.setObjects(
      *(("ALCATEL-IND1-AAA-MIB", "aaaaUserName"),
        ("ALCATEL-IND1-AAA-MIB", "aaaaSlot"),
        ("ALCATEL-IND1-AAA-MIB", "aaaaPort"),
        ("ALCATEL-IND1-AAA-MIB", "aaaaVlan"),
        ("ALCATEL-IND1-AAA-MIB", "aaaaDrop"),
        ("ALCATEL-IND1-AAA-MIB", "aaaaMacAddress"))
)
if mibBuilder.loadTexts:
    aaaAuthenticatedUserGroup.setStatus("current")

aaaAuthFailureTrapGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 2, 1, 11)
)
aaaAuthFailureTrapGroup.setObjects(
      *(("ALCATEL-IND1-AAA-MIB", "aaaAuthSysName"),
        ("ALCATEL-IND1-AAA-MIB", "aaaAuthIpAddress"),
        ("ALCATEL-IND1-AAA-MIB", "aaaAuthPort"),
        ("ALCATEL-IND1-AAA-MIB", "aaaAuthUserName"),
        ("ALCATEL-IND1-AAA-MIB", "aaaAuthType"),
        ("ALCATEL-IND1-AAA-MIB", "aaaAuthFailureReason"))
)
if mibBuilder.loadTexts:
    aaaAuthFailureTrapGroup.setStatus("current")

aaaRedirectGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 2, 1, 12)
)
aaaRedirectGroup.setObjects(
      *(("ALCATEL-IND1-AAA-MIB", "aaaRedirectServerIpAddress"),
        ("ALCATEL-IND1-AAA-MIB", "aaaRedirectServerUrl1"),
        ("ALCATEL-IND1-AAA-MIB", "aaaRedirectServerUrl2"),
        ("ALCATEL-IND1-AAA-MIB", "aaaRedirectServerUrl3"),
        ("ALCATEL-IND1-AAA-MIB", "aaaRedirectServerUrl4"),
        ("ALCATEL-IND1-AAA-MIB", "aaaRedirectServerUrl5"),
        ("ALCATEL-IND1-AAA-MIB", "aaaRedirectSvrConfigRowStatus"),
        ("ALCATEL-IND1-AAA-MIB", "aaaRedirectServerHostName"),
        ("ALCATEL-IND1-AAA-MIB", "aaaRedirectServerUrl"),
        ("ALCATEL-IND1-AAA-MIB", "aaaRedirectServerRowStatus"),
        ("ALCATEL-IND1-AAA-MIB", "aaaRedirectPauseTimerConfig"),
        ("ALCATEL-IND1-AAA-MIB", "aaaPortBounceConfig"),
        ("ALCATEL-IND1-AAA-MIB", "aaaPortBounceStatus"),
        ("ALCATEL-IND1-AAA-MIB", "aaaBYODWhiteListIPAddress"),
        ("ALCATEL-IND1-AAA-MIB", "aaaBYODWhiteListIPMask"),
        ("ALCATEL-IND1-AAA-MIB", "aaaBYODWhiteListRowStatus"))
)
if mibBuilder.loadTexts:
    aaaRedirectGroup.setStatus("current")


# Notification objects

aaaHicServerTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 3, 2, 21, 1, 0, 1)
)
aaaHicServerTrap.setObjects(
      *(("ALCATEL-IND1-AAA-MIB", "aaaHSvrIpAddress"),
        ("ALCATEL-IND1-AAA-MIB", "aaaHSvrRole"),
        ("ALCATEL-IND1-AAA-MIB", "aaaHSvrName"))
)
if mibBuilder.loadTexts:
    aaaHicServerTrap.setStatus(
        "current"
    )

aaaHicServerChangeTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 3, 2, 21, 1, 0, 2)
)
aaaHicServerChangeTrap.setObjects(
      *(("ALCATEL-IND1-AAA-MIB", "aaaHSvrIpAddress"),
        ("ALCATEL-IND1-AAA-MIB", "aaaHSvrCurrIpAddress"))
)
if mibBuilder.loadTexts:
    aaaHicServerChangeTrap.setStatus(
        "current"
    )

aaaHicServerUpTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 3, 2, 21, 1, 0, 3)
)
aaaHicServerUpTrap.setObjects(
      *(("ALCATEL-IND1-AAA-MIB", "aaaHSvrIpAddress"),
        ("ALCATEL-IND1-AAA-MIB", "aaaHSvrRole"),
        ("ALCATEL-IND1-AAA-MIB", "aaaHSvrName"))
)
if mibBuilder.loadTexts:
    aaaHicServerUpTrap.setStatus(
        "current"
    )

aaaAuthenticationFailureTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 3, 2, 21, 3, 0, 1)
)
aaaAuthenticationFailureTrap.setObjects(
      *(("ALCATEL-IND1-AAA-MIB", "aaaAuthSysName"),
        ("ALCATEL-IND1-AAA-MIB", "aaaAuthIpAddress"),
        ("ALCATEL-IND1-AAA-MIB", "aaaAuthPort"),
        ("ALCATEL-IND1-AAA-MIB", "aaaAuthUserName"),
        ("ALCATEL-IND1-AAA-MIB", "aaaAuthType"),
        ("ALCATEL-IND1-AAA-MIB", "aaaAuthFailureReason"))
)
if mibBuilder.loadTexts:
    aaaAuthenticationFailureTrap.setStatus(
        "current"
    )

aaaRadiusServerUpTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 3, 2, 21, 5, 0, 1)
)
aaaRadiusServerUpTrap.setObjects(
      *(("ALCATEL-IND1-AAA-MIB", "aaasIpAddress"),
        ("ALCATEL-IND1-AAA-MIB", "aaasIpAddress2"))
)
if mibBuilder.loadTexts:
    aaaRadiusServerUpTrap.setStatus(
        "current"
    )

aaaRadiusServerDownTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 3, 2, 21, 5, 0, 2)
)
aaaRadiusServerDownTrap.setObjects(
      *(("ALCATEL-IND1-AAA-MIB", "aaasIpAddress"),
        ("ALCATEL-IND1-AAA-MIB", "aaasIpAddress2"))
)
if mibBuilder.loadTexts:
    aaaRadiusServerDownTrap.setStatus(
        "current"
    )


# Notifications groups

aaaTrapsGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 2, 1, 5)
)
aaaTrapsGroup.setObjects(
      *(("ALCATEL-IND1-AAA-MIB", "aaaHicServerTrap"),
        ("ALCATEL-IND1-AAA-MIB", "aaaHicServerChangeTrap"),
        ("ALCATEL-IND1-AAA-MIB", "aaaHicServerUpTrap"),
        ("ALCATEL-IND1-AAA-MIB", "aaaAuthenticationFailureTrap"),
        ("ALCATEL-IND1-AAA-MIB", "aaaRadiusServerUpTrap"),
        ("ALCATEL-IND1-AAA-MIB", "aaaRadiusServerDownTrap"))
)
if mibBuilder.loadTexts:
    aaaTrapsGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

alcatelIND1AAAMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 15, 1, 2, 2, 1)
)
alcatelIND1AAAMIBCompliance.setObjects(
      *(("ALCATEL-IND1-AAA-MIB", "aaaServerMIBGroup"),
        ("ALCATEL-IND1-AAA-MIB", "aaaAuthAcctGroup"),
        ("ALCATEL-IND1-AAA-MIB", "aaaUserMIBGroup"),
        ("ALCATEL-IND1-AAA-MIB", "aaaHicGroup"),
        ("ALCATEL-IND1-AAA-MIB", "aaaVlanGroup"),
        ("ALCATEL-IND1-AAA-MIB", "aaaUNPMacRangeRuleGroup"),
        ("ALCATEL-IND1-AAA-MIB", "aaaUNPMacRuleGroup"),
        ("ALCATEL-IND1-AAA-MIB", "aaaUserNetProfileGroup"),
        ("ALCATEL-IND1-AAA-MIB", "aaaAuthenticatedUserGroup"),
        ("ALCATEL-IND1-AAA-MIB", "aaaAuthFailureTrapGroup"),
        ("ALCATEL-IND1-AAA-MIB", "aaaRedirectGroup"))
)
if mibBuilder.loadTexts:
    alcatelIND1AAAMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ALCATEL-IND1-AAA-MIB",
    **{"AaasRadNasPortTypeConvention": AaasRadNasPortTypeConvention,
       "alcatelIND1AAAMIB": alcatelIND1AAAMIB,
       "alcatelIND1AAAMIBObjects": alcatelIND1AAAMIBObjects,
       "aaaServerMIB": aaaServerMIB,
       "aaaServerTable": aaaServerTable,
       "aaaServerEntry": aaaServerEntry,
       "aaasName": aaasName,
       "aaasProtocol": aaasProtocol,
       "aaasHostName": aaasHostName,
       "aaasIpAddress": aaasIpAddress,
       "aaasHostName2": aaasHostName2,
       "aaasIpAddress2": aaasIpAddress2,
       "aaasRetries": aaasRetries,
       "aaasTimout": aaasTimout,
       "aaasRadKey": aaasRadKey,
       "aaasRadAuthPort": aaasRadAuthPort,
       "aaasRadAcctPort": aaasRadAcctPort,
       "aaasLdapPort": aaasLdapPort,
       "aaasLdapDn": aaasLdapDn,
       "aaasLdapPasswd": aaasLdapPasswd,
       "aaasLdapSearchBase": aaasLdapSearchBase,
       "aaasLdapServType": aaasLdapServType,
       "aaasLdapEnableSsl": aaasLdapEnableSsl,
       "aaasAceClear": aaasAceClear,
       "aaasRowStatus": aaasRowStatus,
       "aaasTacacsKey": aaasTacacsKey,
       "aaasTacacsPort": aaasTacacsPort,
       "aaasHttpPort": aaasHttpPort,
       "aaasHttpDirectory": aaasHttpDirectory,
       "aaasHttpProxyHostName": aaasHttpProxyHostName,
       "aaasHttpProxyIpAddress": aaasHttpProxyIpAddress,
       "aaasHttpProxyPort": aaasHttpProxyPort,
       "aaasVrfName": aaasVrfName,
       "aaasRadMacAddrCase": aaasRadMacAddrCase,
       "aaasRadNasPort": aaasRadNasPort,
       "aaasRadNasPortId": aaasRadNasPortId,
       "aaasRadNasPortType": aaasRadNasPortType,
       "aaasRadMacAddrFormat": aaasRadMacAddrFormat,
       "aaasRadUniqueAcctSessionId": aaasRadUniqueAcctSessionId,
       "aaasRadMacAddrCaseStatus": aaasRadMacAddrCaseStatus,
       "aaasRadServerStatus": aaasRadServerStatus,
       "aaasRadHealthstatus": aaasRadHealthstatus,
       "aaasRadPollInterval": aaasRadPollInterval,
       "aaasRadFailoverStatus": aaasRadFailoverStatus,
       "aaasRadUser": aaasRadUser,
       "aaasRadPasswd": aaasRadPasswd,
       "aaaRadServerPrimaryStatus": aaaRadServerPrimaryStatus,
       "aaaRadServerBackupStatus": aaaRadServerBackupStatus,
       "aaasRadKeyHash": aaasRadKeyHash,
       "aaaRadPrimSerNbUpToDown": aaaRadPrimSerNbUpToDown,
       "aaaRadPrimSerNbDownToUp": aaaRadPrimSerNbDownToUp,
       "aaaRadPrimServUpTime": aaaRadPrimServUpTime,
       "aaaRadPrimServDownTime": aaaRadPrimServDownTime,
       "aaaRadBkupSerNbUpToDown": aaaRadBkupSerNbUpToDown,
       "aaaRadBkupSerNbDownToUp": aaaRadBkupSerNbDownToUp,
       "aaaRadBkupServUpTime": aaaRadBkupServUpTime,
       "aaaRadBkupServDownTime": aaaRadBkupServDownTime,
       "aaasTacacsKeyHash": aaasTacacsKeyHash,
       "aaasRadSalt": aaasRadSalt,
       "aaasRadSaltHash": aaasRadSaltHash,
       "aaasTacacsSalt": aaasTacacsSalt,
       "aaasTacacsSaltHash": aaasTacacsSaltHash,
       "aaasLdapSalt": aaasLdapSalt,
       "aaasLdapSaltHash": aaasLdapSaltHash,
       "aaasLdapPasswdHash": aaasLdapPasswdHash,
       "aaaTacacsServerCmdAuthorization": aaaTacacsServerCmdAuthorization,
       "aaaTacacsServerWaitTime": aaaTacacsServerWaitTime,
       "aaaAuthAcctMIB": aaaAuthAcctMIB,
       "aaaAuthVlanTable": aaaAuthVlanTable,
       "aaaAuthVlanEntry": aaaAuthVlanEntry,
       "aaatvVlan": aaatvVlan,
       "aaatvName1": aaatvName1,
       "aaatvName2": aaatvName2,
       "aaatvName3": aaatvName3,
       "aaatvName4": aaatvName4,
       "aaatvRowStatus": aaatvRowStatus,
       "aaatvCertificate": aaatvCertificate,
       "aaaAuthSATable": aaaAuthSATable,
       "aaaAuthSAEntry": aaaAuthSAEntry,
       "aaatsInterface": aaatsInterface,
       "aaatsName1": aaatsName1,
       "aaatsName2": aaatsName2,
       "aaatsName3": aaatsName3,
       "aaatsName4": aaatsName4,
       "aaatsName5": aaatsName5,
       "aaatsRowStatus": aaatsRowStatus,
       "aaatsCertificate": aaatsCertificate,
       "aaaAcctVlanTable": aaaAcctVlanTable,
       "aaaAcctVlanEntry": aaaAcctVlanEntry,
       "aaacvVlan": aaacvVlan,
       "aaacvName1": aaacvName1,
       "aaacvName2": aaacvName2,
       "aaacvName3": aaacvName3,
       "aaacvName4": aaacvName4,
       "aaacvRowStatus": aaacvRowStatus,
       "aaaAcctSATable": aaaAcctSATable,
       "aaaAcctSAEntry": aaaAcctSAEntry,
       "aaacsInterface": aaacsInterface,
       "aaacsName1": aaacsName1,
       "aaacsName2": aaacsName2,
       "aaacsName3": aaacsName3,
       "aaacsName4": aaacsName4,
       "aaacsRowStatus": aaacsRowStatus,
       "aaaAccountingSessionIdStatus": aaaAccountingSessionIdStatus,
       "aaacsName5": aaacsName5,
       "aaaAuth8021xTable": aaaAuth8021xTable,
       "aaaAuth8021xEntry": aaaAuth8021xEntry,
       "aaatxInterface": aaatxInterface,
       "aaatxName1": aaatxName1,
       "aaatxName2": aaatxName2,
       "aaatxName3": aaatxName3,
       "aaatxName4": aaatxName4,
       "aaatxOpen": aaatxOpen,
       "aaatxRowStatus": aaatxRowStatus,
       "aaatxName5": aaatxName5,
       "aaaAcct8021xTable": aaaAcct8021xTable,
       "aaaAcct8021xEntry": aaaAcct8021xEntry,
       "aaacxInterface": aaacxInterface,
       "aaacxName1": aaacxName1,
       "aaacxName2": aaacxName2,
       "aaacxName3": aaacxName3,
       "aaacxName4": aaacxName4,
       "aaacxRowStatus": aaacxRowStatus,
       "aaacxName5": aaacxName5,
       "aaaPkiTable": aaaPkiTable,
       "aaaPkiEntry": aaaPkiEntry,
       "aaatpInterface": aaatpInterface,
       "aaatpName1": aaatpName1,
       "aaatpName2": aaatpName2,
       "aaatpName3": aaatpName3,
       "aaatpName4": aaatpName4,
       "aaatpLevel": aaatpLevel,
       "aaatpRowStatus": aaatpRowStatus,
       "aaaAuthMACTable": aaaAuthMACTable,
       "aaaAuthMACEntry": aaaAuthMACEntry,
       "aaaMacInterface": aaaMacInterface,
       "aaaMacSrvrName1": aaaMacSrvrName1,
       "aaaMacSrvrName2": aaaMacSrvrName2,
       "aaaMacSrvrName3": aaaMacSrvrName3,
       "aaaMacSrvrName4": aaaMacSrvrName4,
       "aaaMacSrvrRowStatus": aaaMacSrvrRowStatus,
       "aaaMacSrvrName5": aaaMacSrvrName5,
       "aaaAcctCmdTable": aaaAcctCmdTable,
       "aaaAcctCmdEntry": aaaAcctCmdEntry,
       "aaacmdInterface": aaacmdInterface,
       "aaacmdSrvName1": aaacmdSrvName1,
       "aaacmdSrvName2": aaacmdSrvName2,
       "aaacmdSrvName3": aaacmdSrvName3,
       "aaacmdSrvName4": aaacmdSrvName4,
       "aaacmdRowStatus": aaacmdRowStatus,
       "aaacmdSrvName5": aaacmdSrvName5,
       "aaaAcctMACTable": aaaAcctMACTable,
       "aaaAcctMACEntry": aaaAcctMACEntry,
       "aaaAcctSvrInterface": aaaAcctSvrInterface,
       "aaaAcctSvr1": aaaAcctSvr1,
       "aaaAcctSvr2": aaaAcctSvr2,
       "aaaAcctSvr3": aaaAcctSvr3,
       "aaaAcctSvr4": aaaAcctSvr4,
       "aaaAcctSvrRowStatus": aaaAcctSvrRowStatus,
       "aaaAcctSvr5": aaaAcctSvr5,
       "aaaUserMIB": aaaUserMIB,
       "aaaUserTable": aaaUserTable,
       "aaaUserEntry": aaaUserEntry,
       "aaauUserName": aaauUserName,
       "aaauPassword": aaauPassword,
       "aaauReadRight1": aaauReadRight1,
       "aaauReadRight2": aaauReadRight2,
       "aaauWriteRight1": aaauWriteRight1,
       "aaauWriteRight2": aaauWriteRight2,
       "aaauProfile": aaauProfile,
       "aaauSnmpLevel": aaauSnmpLevel,
       "aaauSnmpAuthKey": aaauSnmpAuthKey,
       "aaauRowStatus": aaauRowStatus,
       "aaauOldPassword": aaauOldPassword,
       "aaauEndUserProfile": aaauEndUserProfile,
       "aaauPasswordExpirationDate": aaauPasswordExpirationDate,
       "aaauPasswordExpirationInMinute": aaauPasswordExpirationInMinute,
       "aaauPasswordAllowModifyDate": aaauPasswordAllowModifyDate,
       "aaauPasswordLockoutEnable": aaauPasswordLockoutEnable,
       "aaauBadAtempts": aaauBadAtempts,
       "aaauSnmpOnly": aaauSnmpOnly,
       "aaauSnmpPrivPassword": aaauSnmpPrivPassword,
       "aaauReadRightView": aaauReadRightView,
       "aaauWriteRightView": aaauWriteRightView,
       "aaaAuthenticatedUserTable": aaaAuthenticatedUserTable,
       "aaaAuthenticatedUserEntry": aaaAuthenticatedUserEntry,
       "aaaaMacAddress": aaaaMacAddress,
       "aaaaUserName": aaaaUserName,
       "aaaaSlot": aaaaSlot,
       "aaaaPort": aaaaPort,
       "aaaaVlan": aaaaVlan,
       "aaaaDrop": aaaaDrop,
       "aaaAvlanConfig": aaaAvlanConfig,
       "aaaAvlanDnsName": aaaAvlanDnsName,
       "aaaAvlanDhcpDefGateway": aaaAvlanDhcpDefGateway,
       "aaaAvlanDefaultTraffic": aaaAvlanDefaultTraffic,
       "aaaAvlanPortBound": aaaAvlanPortBound,
       "aaaAvlanLanguage": aaaAvlanLanguage,
       "aaaAsaConfig": aaaAsaConfig,
       "aaaAsaPasswordSizeMin": aaaAsaPasswordSizeMin,
       "aaaAsaDefaultPasswordExpirationInDays": aaaAsaDefaultPasswordExpirationInDays,
       "aaaAsaPasswordContainUserName": aaaAsaPasswordContainUserName,
       "aaaAsaPasswordMinUpperCase": aaaAsaPasswordMinUpperCase,
       "aaaAsaPasswordMinLowerCase": aaaAsaPasswordMinLowerCase,
       "aaaAsaPasswordMinDigit": aaaAsaPasswordMinDigit,
       "aaaAsaPasswordMinNonAlphan": aaaAsaPasswordMinNonAlphan,
       "aaaAsaPasswordHistory": aaaAsaPasswordHistory,
       "aaaAsaPasswordMinAge": aaaAsaPasswordMinAge,
       "aaaAsaLockoutWindow": aaaAsaLockoutWindow,
       "aaaAsaLockoutDuration": aaaAsaLockoutDuration,
       "aaaAsaLockoutThreshold": aaaAsaLockoutThreshold,
       "aaaAsaROUserPingTrtEnable": aaaAsaROUserPingTrtEnable,
       "aaaAsaAccessPolicyAdminConsoleOnly": aaaAsaAccessPolicyAdminConsoleOnly,
       "aaaAsaCertPassword": aaaAsaCertPassword,
       "aaaAsaAccessMode": aaaAsaAccessMode,
       "aaaAsaIpLockoutThreshold": aaaAsaIpLockoutThreshold,
       "aaaSwitchAccessMgmtStationState": aaaSwitchAccessMgmtStationState,
       "aaaAvlanAddressTable": aaaAvlanAddressTable,
       "aaaAvlanAddressEntry": aaaAvlanAddressEntry,
       "aaaAvlanId": aaaAvlanId,
       "aaaAvlanIpAddress": aaaAvlanIpAddress,
       "aaaUserNetProfileTable": aaaUserNetProfileTable,
       "aaaUserNetProfileEntry": aaaUserNetProfileEntry,
       "aaaUserNetProfileName": aaaUserNetProfileName,
       "aaaUserNetProfileVlanID": aaaUserNetProfileVlanID,
       "aaaUserNetProfileRowStatus": aaaUserNetProfileRowStatus,
       "aaaUserNetProfileHICflag": aaaUserNetProfileHICflag,
       "aaaUserNetProfileQosPolicyListName": aaaUserNetProfileQosPolicyListName,
       "aaaUserNetProfileMaxIngressBw": aaaUserNetProfileMaxIngressBw,
       "aaaUserNetProfileMaxEgressBw": aaaUserNetProfileMaxEgressBw,
       "aaaUserNetProfileMaxDefaultDepth": aaaUserNetProfileMaxDefaultDepth,
       "aaaUserNetworkProfileRedirectUrl": aaaUserNetworkProfileRedirectUrl,
       "aaaRadAgentConfig": aaaRadAgentConfig,
       "aaaRadAgentIP": aaaRadAgentIP,
       "aaaHicConfig": aaaHicConfig,
       "aaaHicSvrTable": aaaHicSvrTable,
       "aaaHicSvrEntry": aaaHicSvrEntry,
       "aaaHicSvrName": aaaHicSvrName,
       "aaaHicSvrIpAddr": aaaHicSvrIpAddr,
       "aaaHicSvrPort": aaaHicSvrPort,
       "aaaHicSvrKey": aaaHicSvrKey,
       "aaaHicSvrRowStatus": aaaHicSvrRowStatus,
       "aaaHicSvrStatus": aaaHicSvrStatus,
       "aaaHicSvrRole": aaaHicSvrRole,
       "aaaHicSvrConnection": aaaHicSvrConnection,
       "aaaHicAllowedTable": aaaHicAllowedTable,
       "aaaHicAllowedEntry": aaaHicAllowedEntry,
       "aaaHicAllowedName": aaaHicAllowedName,
       "aaaHicAllowedIpAddr": aaaHicAllowedIpAddr,
       "aaaHicAllowedIpMask": aaaHicAllowedIpMask,
       "aaaHicAllowedRowStatus": aaaHicAllowedRowStatus,
       "aaaHicOverrideTable": aaaHicOverrideTable,
       "aaaHicOverrideEntry": aaaHicOverrideEntry,
       "aaaHicOverrideMac": aaaHicOverrideMac,
       "aaaHicOverrideStatus": aaaHicOverrideStatus,
       "aaaHicOverrideRowStatus": aaaHicOverrideRowStatus,
       "aaaHicHostTable": aaaHicHostTable,
       "aaaHicHostEntry": aaaHicHostEntry,
       "aaaHicHostMac": aaaHicHostMac,
       "aaaHicHostStatus": aaaHicHostStatus,
       "aaaHicConfigInfo": aaaHicConfigInfo,
       "aaaHicStatus": aaaHicStatus,
       "aaaHicAllowed1Name": aaaHicAllowed1Name,
       "aaaHicAllowed2Name": aaaHicAllowed2Name,
       "aaaHicAllowed3Name": aaaHicAllowed3Name,
       "aaaHicAllowed4Name": aaaHicAllowed4Name,
       "aaaHicWebAgentDownloadUrl": aaaHicWebAgentDownloadUrl,
       "aaaHicCustomHttpProxyPort": aaaHicCustomHttpProxyPort,
       "aaaHicBgPollInterval": aaaHicBgPollInterval,
       "aaaHicSvrFailMode": aaaHicSvrFailMode,
       "aaaUNPIpNetRuleTable": aaaUNPIpNetRuleTable,
       "aaaUNPIpNetRuleEntry": aaaUNPIpNetRuleEntry,
       "aaaUNPIpNetRuleAddrType": aaaUNPIpNetRuleAddrType,
       "aaaUNPIpNetRuleAddr": aaaUNPIpNetRuleAddr,
       "aaaUNPIpNetRuleMask": aaaUNPIpNetRuleMask,
       "aaaUNPIpNetRuleProfileName": aaaUNPIpNetRuleProfileName,
       "aaaUNPIpNetRuleRowStatus": aaaUNPIpNetRuleRowStatus,
       "aaaUNPMacRuleTable": aaaUNPMacRuleTable,
       "aaaUNPMacRuleEntry": aaaUNPMacRuleEntry,
       "aaaUNPMacRuleAddr": aaaUNPMacRuleAddr,
       "aaaUNPMacRuleProfileName": aaaUNPMacRuleProfileName,
       "aaaUNPMacRuleRowStatus": aaaUNPMacRuleRowStatus,
       "aaaUNPMacRangeRuleTable": aaaUNPMacRangeRuleTable,
       "aaaUNPMacRangeRuleEntry": aaaUNPMacRangeRuleEntry,
       "aaaUNPMacRangeRuleLoAddr": aaaUNPMacRangeRuleLoAddr,
       "aaaUNPMacRangeRuleHiAddr": aaaUNPMacRangeRuleHiAddr,
       "aaaUNPMacRangeRuleProfileName": aaaUNPMacRangeRuleProfileName,
       "aaaUNPMacRangeRuleRowStatus": aaaUNPMacRangeRuleRowStatus,
       "aaaHicSvrDownUnpMapTable": aaaHicSvrDownUnpMapTable,
       "aaaHicSvrDownUnpMapEntry": aaaHicSvrDownUnpMapEntry,
       "aaaHicSvrDownUnpName": aaaHicSvrDownUnpName,
       "aaaHicSvrDownMappedUnpName": aaaHicSvrDownMappedUnpName,
       "aaaHicSvrDownUnpRowStatus": aaaHicSvrDownUnpRowStatus,
       "aaaRedirectConfig": aaaRedirectConfig,
       "aaaRedirectServerTable": aaaRedirectServerTable,
       "aaaRedirectServerEntry": aaaRedirectServerEntry,
       "aaaRedirectServerName": aaaRedirectServerName,
       "aaaRedirectServerIpAddress": aaaRedirectServerIpAddress,
       "aaaRedirectServerUrl1": aaaRedirectServerUrl1,
       "aaaRedirectServerUrl2": aaaRedirectServerUrl2,
       "aaaRedirectServerUrl3": aaaRedirectServerUrl3,
       "aaaRedirectServerUrl4": aaaRedirectServerUrl4,
       "aaaRedirectServerUrl5": aaaRedirectServerUrl5,
       "aaaRedirectSvrConfigRowStatus": aaaRedirectSvrConfigRowStatus,
       "aaaRedirectServerHostName": aaaRedirectServerHostName,
       "aaaRedirectUrlConfigTable": aaaRedirectUrlConfigTable,
       "aaaRedirectURLEntry": aaaRedirectURLEntry,
       "aaaRedirectServerUrlName": aaaRedirectServerUrlName,
       "aaaRedirectServerUrl": aaaRedirectServerUrl,
       "aaaRedirectServerRowStatus": aaaRedirectServerRowStatus,
       "aaaRedirectGlobalConfig": aaaRedirectGlobalConfig,
       "aaaRedirectPauseTimerConfig": aaaRedirectPauseTimerConfig,
       "aaaPortBounceConfig": aaaPortBounceConfig,
       "aaaRedirectProxyServerPort": aaaRedirectProxyServerPort,
       "aaaPortBounceInterfaceTable": aaaPortBounceInterfaceTable,
       "aaaPortBounceInterfaceEntry": aaaPortBounceInterfaceEntry,
       "aaaPortBouncePortSlot": aaaPortBouncePortSlot,
       "aaaPortBounceIF": aaaPortBounceIF,
       "aaaPortBounceStatus": aaaPortBounceStatus,
       "aaaBYODWhiteListTable": aaaBYODWhiteListTable,
       "aaaBYODWhiteListEntry": aaaBYODWhiteListEntry,
       "aaaBYODWhiteListIPAddress": aaaBYODWhiteListIPAddress,
       "aaaBYODWhiteListIPMask": aaaBYODWhiteListIPMask,
       "aaaBYODWhiteListRowStatus": aaaBYODWhiteListRowStatus,
       "aaaSwitchAccessConfig": aaaSwitchAccessConfig,
       "aaaSwitchAccessMgmtStationTable": aaaSwitchAccessMgmtStationTable,
       "aaaSwitchAccessMgmtStationEntry": aaaSwitchAccessMgmtStationEntry,
       "aaaSwitchAccessMgmtStationIpAddress": aaaSwitchAccessMgmtStationIpAddress,
       "aaaSwitchAccessMgmtStationIpAddressMask": aaaSwitchAccessMgmtStationIpAddressMask,
       "aaaSwitchAccessMgmtStationRowStatus": aaaSwitchAccessMgmtStationRowStatus,
       "aaaSwitchAccessBannedIpTable": aaaSwitchAccessBannedIpTable,
       "aaaSwitchAccessBannedIpEntry": aaaSwitchAccessBannedIpEntry,
       "aaaSwitchAccessBannedIpAddress": aaaSwitchAccessBannedIpAddress,
       "aaaSwitchAccessBannedIpRowStatus": aaaSwitchAccessBannedIpRowStatus,
       "aaaSwitchAccessPrivMaskTable": aaaSwitchAccessPrivMaskTable,
       "aaaSwitchAccessPrivMaskEntry": aaaSwitchAccessPrivMaskEntry,
       "aaaSwitchAccessType": aaaSwitchAccessType,
       "aaaSwitchAccessReadRight1": aaaSwitchAccessReadRight1,
       "aaaSwitchAccessReadRight2": aaaSwitchAccessReadRight2,
       "aaaSwitchAccessWriteRight1": aaaSwitchAccessWriteRight1,
       "aaaSwitchAccessWriteRight2": aaaSwitchAccessWriteRight2,
       "aaaSwitchAccessPrivMaskRowStatus": aaaSwitchAccessPrivMaskRowStatus,
       "alaAaaTlsConfig": alaAaaTlsConfig,
       "alaAaaTlsBaseConfig": alaAaaTlsBaseConfig,
       "alaAaaTlsCaFileName": alaAaaTlsCaFileName,
       "alaAaaTlsCrlFileName": alaAaaTlsCrlFileName,
       "alaAaaTlsKeyFileName": alaAaaTlsKeyFileName,
       "alaAaaTlsCertFileName": alaAaaTlsCertFileName,
       "alaAaaTlsSelfSignedCert": alaAaaTlsSelfSignedCert,
       "alaAaaTlsSelfSignedCertFileName": alaAaaTlsSelfSignedCertFileName,
       "alaAaaTlsSelfSignedCertKeyFileName": alaAaaTlsSelfSignedCertKeyFileName,
       "alaAaaTlsSelfSignedCertValidPeriod": alaAaaTlsSelfSignedCertValidPeriod,
       "alaAaaTlsSelfSignedCertCommonName": alaAaaTlsSelfSignedCertCommonName,
       "alaAaaTlsSelfSignedCertOrgName": alaAaaTlsSelfSignedCertOrgName,
       "alaAaaTlsSelfSignedCertOrgUnit": alaAaaTlsSelfSignedCertOrgUnit,
       "alaAaaTlsSelfSignedCertLocality": alaAaaTlsSelfSignedCertLocality,
       "alaAaaTlsSelfSignedCertState": alaAaaTlsSelfSignedCertState,
       "alaAaaTlsSelfSignedCertCountry": alaAaaTlsSelfSignedCertCountry,
       "alaAaaTlsSelfSignedCertAction": alaAaaTlsSelfSignedCertAction,
       "alaAaaTlsCsr": alaAaaTlsCsr,
       "alaAaaTlsCsrFileName": alaAaaTlsCsrFileName,
       "alaAaaTlsCsrKeyFileName": alaAaaTlsCsrKeyFileName,
       "alaAaaTlsCsrCommonName": alaAaaTlsCsrCommonName,
       "alaAaaTlsCsrOrgName": alaAaaTlsCsrOrgName,
       "alaAaaTlsCsrOrgUnit": alaAaaTlsCsrOrgUnit,
       "alaAaaTlsCsrLocality": alaAaaTlsCsrLocality,
       "alaAaaTlsCsrState": alaAaaTlsCsrState,
       "alaAaaTlsCsrCountry": alaAaaTlsCsrCountry,
       "aaaUNPLldpRuleConfig": aaaUNPLldpRuleConfig,
       "aaaUNPLldpRuleProfileName": aaaUNPLldpRuleProfileName,
       "alaAaaRadClientGlobalAttr": alaAaaRadClientGlobalAttr,
       "alaAaaRadNasIdentifier": alaAaaRadNasIdentifier,
       "alaAaaRadClientNasIpAddr": alaAaaRadClientNasIpAddr,
       "alaAaaRadNasIpState": alaAaaRadNasIpState,
       "alaAaaRadNasIpField": alaAaaRadNasIpField,
       "alcatelIND1AAAMIBConformance": alcatelIND1AAAMIBConformance,
       "alcatelIND1AAAMIBGroups": alcatelIND1AAAMIBGroups,
       "aaaServerMIBGroup": aaaServerMIBGroup,
       "aaaAuthAcctGroup": aaaAuthAcctGroup,
       "aaaUserMIBGroup": aaaUserMIBGroup,
       "aaaHicGroup": aaaHicGroup,
       "aaaTrapsGroup": aaaTrapsGroup,
       "aaaVlanGroup": aaaVlanGroup,
       "aaaUNPMacRangeRuleGroup": aaaUNPMacRangeRuleGroup,
       "aaaUNPMacRuleGroup": aaaUNPMacRuleGroup,
       "aaaUserNetProfileGroup": aaaUserNetProfileGroup,
       "aaaAuthenticatedUserGroup": aaaAuthenticatedUserGroup,
       "aaaAuthFailureTrapGroup": aaaAuthFailureTrapGroup,
       "aaaRedirectGroup": aaaRedirectGroup,
       "alcatelIND1AAAMIBCompliances": alcatelIND1AAAMIBCompliances,
       "alcatelIND1AAAMIBCompliance": alcatelIND1AAAMIBCompliance,
       "alaAaaTrapsDesc": alaAaaTrapsDesc,
       "alaAaaTrapsDescRoot": alaAaaTrapsDescRoot,
       "aaaHicServerTrap": aaaHicServerTrap,
       "aaaHicServerChangeTrap": aaaHicServerChangeTrap,
       "aaaHicServerUpTrap": aaaHicServerUpTrap,
       "alaAaaTrapsObj": alaAaaTrapsObj,
       "aaaHSvrIpAddress": aaaHSvrIpAddress,
       "aaaHSvrCurrIpAddress": aaaHSvrCurrIpAddress,
       "aaaHSvrRole": aaaHSvrRole,
       "aaaHSvrName": aaaHSvrName,
       "alaAaaAuthTrapsDesc": alaAaaAuthTrapsDesc,
       "alaAaaAuthTrapsDescRoot": alaAaaAuthTrapsDescRoot,
       "aaaAuthenticationFailureTrap": aaaAuthenticationFailureTrap,
       "alaAaaAuthTrapsObj": alaAaaAuthTrapsObj,
       "aaaAuthSysName": aaaAuthSysName,
       "aaaAuthIpAddress": aaaAuthIpAddress,
       "aaaAuthPort": aaaAuthPort,
       "aaaAuthUserName": aaaAuthUserName,
       "aaaAuthType": aaaAuthType,
       "aaaAuthFailureReason": aaaAuthFailureReason,
       "alaAaaRadiusTrapsDesc": alaAaaRadiusTrapsDesc,
       "alaAaaRadiusTrapsDescRoot": alaAaaRadiusTrapsDescRoot,
       "aaaRadiusServerUpTrap": aaaRadiusServerUpTrap,
       "aaaRadiusServerDownTrap": aaaRadiusServerDownTrap}
)
