# SNMP MIB module (HH3C-SNMP-EXT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\comware\HH3C-SNMP-EXT-MIB

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

(SnmpAdminString,
 SnmpSecurityModel) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString",
    "SnmpSecurityModel")

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

hh3cSnmpExt = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 104)
)
if mibBuilder.loadTexts:
    hh3cSnmpExt.setRevisions(
        ("2019-04-16 00:00",
         "2016-08-08 00:00",
         "2016-04-13 02:00",
         "2015-01-20 09:00",
         "2014-08-12 03:03",
         "2013-05-16 00:00",
         "2013-04-08 00:00",
         "2011-08-11 00:00",
         "2010-03-12 00:00",
         "2009-04-07 17:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Hh3cSnmpExtScalarObjects_ObjectIdentity = ObjectIdentity
hh3cSnmpExtScalarObjects = _Hh3cSnmpExtScalarObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 104, 1)
)


class _Hh3cSnmpExtSnmpChannel_Type(Integer32):
    """Custom type hh3cSnmpExtSnmpChannel based on Integer32"""
    defaultValue = 161

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_Hh3cSnmpExtSnmpChannel_Type.__name__ = "Integer32"
_Hh3cSnmpExtSnmpChannel_Object = MibScalar
hh3cSnmpExtSnmpChannel = _Hh3cSnmpExtSnmpChannel_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 104, 1, 1),
    _Hh3cSnmpExtSnmpChannel_Type()
)
hh3cSnmpExtSnmpChannel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cSnmpExtSnmpChannel.setStatus("current")


class _Hh3cSnmpExtReadCommunitySingle_Type(SnmpAdminString):
    """Custom type hh3cSnmpExtReadCommunitySingle based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_Hh3cSnmpExtReadCommunitySingle_Type.__name__ = "SnmpAdminString"
_Hh3cSnmpExtReadCommunitySingle_Object = MibScalar
hh3cSnmpExtReadCommunitySingle = _Hh3cSnmpExtReadCommunitySingle_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 104, 1, 2),
    _Hh3cSnmpExtReadCommunitySingle_Type()
)
hh3cSnmpExtReadCommunitySingle.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cSnmpExtReadCommunitySingle.setStatus("current")


class _Hh3cSnmpExtWriteCommunitySingle_Type(SnmpAdminString):
    """Custom type hh3cSnmpExtWriteCommunitySingle based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_Hh3cSnmpExtWriteCommunitySingle_Type.__name__ = "SnmpAdminString"
_Hh3cSnmpExtWriteCommunitySingle_Object = MibScalar
hh3cSnmpExtWriteCommunitySingle = _Hh3cSnmpExtWriteCommunitySingle_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 104, 1, 3),
    _Hh3cSnmpExtWriteCommunitySingle_Type()
)
hh3cSnmpExtWriteCommunitySingle.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cSnmpExtWriteCommunitySingle.setStatus("current")


class _Hh3cSnmpExtMaxContextNum_Type(Integer32):
    """Custom type hh3cSnmpExtMaxContextNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_Hh3cSnmpExtMaxContextNum_Type.__name__ = "Integer32"
_Hh3cSnmpExtMaxContextNum_Object = MibScalar
hh3cSnmpExtMaxContextNum = _Hh3cSnmpExtMaxContextNum_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 104, 1, 4),
    _Hh3cSnmpExtMaxContextNum_Type()
)
hh3cSnmpExtMaxContextNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cSnmpExtMaxContextNum.setStatus("current")


class _Hh3cSnmpExtVersion_Type(Bits):
    """Custom type hh3cSnmpExtVersion based on Bits"""
    namedValues = NamedValues(
        *(("snmpV1", 0),
          ("snmpV2c", 1),
          ("snmpV3", 2))
    )

_Hh3cSnmpExtVersion_Type.__name__ = "Bits"
_Hh3cSnmpExtVersion_Object = MibScalar
hh3cSnmpExtVersion = _Hh3cSnmpExtVersion_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 104, 1, 5),
    _Hh3cSnmpExtVersion_Type()
)
hh3cSnmpExtVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cSnmpExtVersion.setStatus("current")


class _Hh3cSnmpExtTrapSource_Type(SnmpAdminString):
    """Custom type hh3cSnmpExtTrapSource based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_Hh3cSnmpExtTrapSource_Type.__name__ = "SnmpAdminString"
_Hh3cSnmpExtTrapSource_Object = MibScalar
hh3cSnmpExtTrapSource = _Hh3cSnmpExtTrapSource_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 104, 1, 6),
    _Hh3cSnmpExtTrapSource_Type()
)
hh3cSnmpExtTrapSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cSnmpExtTrapSource.setStatus("current")


class _Hh3cSnmpExtInformSource_Type(SnmpAdminString):
    """Custom type hh3cSnmpExtInformSource based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_Hh3cSnmpExtInformSource_Type.__name__ = "SnmpAdminString"
_Hh3cSnmpExtInformSource_Object = MibScalar
hh3cSnmpExtInformSource = _Hh3cSnmpExtInformSource_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 104, 1, 7),
    _Hh3cSnmpExtInformSource_Type()
)
hh3cSnmpExtInformSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cSnmpExtInformSource.setStatus("current")


class _Hh3cSnmpExtAclNum_Type(Integer32):
    """Custom type hh3cSnmpExtAclNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(2000, 3999),
    )


_Hh3cSnmpExtAclNum_Type.__name__ = "Integer32"
_Hh3cSnmpExtAclNum_Object = MibScalar
hh3cSnmpExtAclNum = _Hh3cSnmpExtAclNum_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 104, 1, 8),
    _Hh3cSnmpExtAclNum_Type()
)
hh3cSnmpExtAclNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cSnmpExtAclNum.setStatus("current")


class _Hh3cSnmpExtAclName_Type(OctetString):
    """Custom type hh3cSnmpExtAclName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_Hh3cSnmpExtAclName_Type.__name__ = "OctetString"
_Hh3cSnmpExtAclName_Object = MibScalar
hh3cSnmpExtAclName = _Hh3cSnmpExtAclName_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 104, 1, 9),
    _Hh3cSnmpExtAclName_Type()
)
hh3cSnmpExtAclName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cSnmpExtAclName.setStatus("current")


class _Hh3cSnmpExtIPv6AclNum_Type(Integer32):
    """Custom type hh3cSnmpExtIPv6AclNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(2000, 3999),
    )


_Hh3cSnmpExtIPv6AclNum_Type.__name__ = "Integer32"
_Hh3cSnmpExtIPv6AclNum_Object = MibScalar
hh3cSnmpExtIPv6AclNum = _Hh3cSnmpExtIPv6AclNum_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 104, 1, 10),
    _Hh3cSnmpExtIPv6AclNum_Type()
)
hh3cSnmpExtIPv6AclNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cSnmpExtIPv6AclNum.setStatus("current")


class _Hh3cSnmpExtIPv6AclName_Type(OctetString):
    """Custom type hh3cSnmpExtIPv6AclName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_Hh3cSnmpExtIPv6AclName_Type.__name__ = "OctetString"
_Hh3cSnmpExtIPv6AclName_Object = MibScalar
hh3cSnmpExtIPv6AclName = _Hh3cSnmpExtIPv6AclName_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 104, 1, 11),
    _Hh3cSnmpExtIPv6AclName_Type()
)
hh3cSnmpExtIPv6AclName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cSnmpExtIPv6AclName.setStatus("current")
_Hh3cSnmpExtTables_ObjectIdentity = ObjectIdentity
hh3cSnmpExtTables = _Hh3cSnmpExtTables_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 104, 2)
)
_Hh3cSnmpExtCommunityTable_Object = MibTable
hh3cSnmpExtCommunityTable = _Hh3cSnmpExtCommunityTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 104, 2, 1)
)
if mibBuilder.loadTexts:
    hh3cSnmpExtCommunityTable.setStatus("current")
_Hh3cSnmpExtCommunityEntry_Object = MibTableRow
hh3cSnmpExtCommunityEntry = _Hh3cSnmpExtCommunityEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 104, 2, 1, 1)
)
hh3cSnmpExtCommunityEntry.setIndexNames(
    (0, "HH3C-SNMP-EXT-MIB", "hh3cSnmpExtCommunitySecurityLevel"),
    (0, "HH3C-SNMP-EXT-MIB", "hh3cSnmpExtCommunitySecurityName"),
)
if mibBuilder.loadTexts:
    hh3cSnmpExtCommunityEntry.setStatus("current")
_Hh3cSnmpExtCommunitySecurityLevel_Type = SnmpSecurityModel
_Hh3cSnmpExtCommunitySecurityLevel_Object = MibTableColumn
hh3cSnmpExtCommunitySecurityLevel = _Hh3cSnmpExtCommunitySecurityLevel_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 104, 2, 1, 1, 1),
    _Hh3cSnmpExtCommunitySecurityLevel_Type()
)
hh3cSnmpExtCommunitySecurityLevel.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cSnmpExtCommunitySecurityLevel.setStatus("current")


class _Hh3cSnmpExtCommunitySecurityName_Type(SnmpAdminString):
    """Custom type hh3cSnmpExtCommunitySecurityName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_Hh3cSnmpExtCommunitySecurityName_Type.__name__ = "SnmpAdminString"
_Hh3cSnmpExtCommunitySecurityName_Object = MibTableColumn
hh3cSnmpExtCommunitySecurityName = _Hh3cSnmpExtCommunitySecurityName_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 104, 2, 1, 1, 2),
    _Hh3cSnmpExtCommunitySecurityName_Type()
)
hh3cSnmpExtCommunitySecurityName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cSnmpExtCommunitySecurityName.setStatus("current")


class _Hh3cSnmpExtCommunityName_Type(OctetString):
    """Custom type hh3cSnmpExtCommunityName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_Hh3cSnmpExtCommunityName_Type.__name__ = "OctetString"
_Hh3cSnmpExtCommunityName_Object = MibTableColumn
hh3cSnmpExtCommunityName = _Hh3cSnmpExtCommunityName_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 104, 2, 1, 1, 3),
    _Hh3cSnmpExtCommunityName_Type()
)
hh3cSnmpExtCommunityName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cSnmpExtCommunityName.setStatus("current")


class _Hh3cSnmpExtCommunityAclNum_Type(Integer32):
    """Custom type hh3cSnmpExtCommunityAclNum based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(2000, 3999),
    )


_Hh3cSnmpExtCommunityAclNum_Type.__name__ = "Integer32"
_Hh3cSnmpExtCommunityAclNum_Object = MibTableColumn
hh3cSnmpExtCommunityAclNum = _Hh3cSnmpExtCommunityAclNum_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 104, 2, 1, 1, 4),
    _Hh3cSnmpExtCommunityAclNum_Type()
)
hh3cSnmpExtCommunityAclNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cSnmpExtCommunityAclNum.setStatus("current")


class _Hh3cSnmpExtCommunityIPv6AclNum_Type(Integer32):
    """Custom type hh3cSnmpExtCommunityIPv6AclNum based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(2000, 3999),
    )


_Hh3cSnmpExtCommunityIPv6AclNum_Type.__name__ = "Integer32"
_Hh3cSnmpExtCommunityIPv6AclNum_Object = MibTableColumn
hh3cSnmpExtCommunityIPv6AclNum = _Hh3cSnmpExtCommunityIPv6AclNum_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 104, 2, 1, 1, 5),
    _Hh3cSnmpExtCommunityIPv6AclNum_Type()
)
hh3cSnmpExtCommunityIPv6AclNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cSnmpExtCommunityIPv6AclNum.setStatus("current")
_Hh3cSnmpCommunityExTable_Object = MibTable
hh3cSnmpCommunityExTable = _Hh3cSnmpCommunityExTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 104, 2, 2)
)
if mibBuilder.loadTexts:
    hh3cSnmpCommunityExTable.setStatus("current")
_Hh3cSnmpCommunityExEntry_Object = MibTableRow
hh3cSnmpCommunityExEntry = _Hh3cSnmpCommunityExEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 104, 2, 2, 1)
)
hh3cSnmpCommunityExEntry.setIndexNames(
    (0, "HH3C-SNMP-EXT-MIB", "hh3cSnmpCommunityExName"),
)
if mibBuilder.loadTexts:
    hh3cSnmpCommunityExEntry.setStatus("current")


class _Hh3cSnmpCommunityExName_Type(OctetString):
    """Custom type hh3cSnmpCommunityExName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_Hh3cSnmpCommunityExName_Type.__name__ = "OctetString"
_Hh3cSnmpCommunityExName_Object = MibTableColumn
hh3cSnmpCommunityExName = _Hh3cSnmpCommunityExName_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 104, 2, 2, 1, 1),
    _Hh3cSnmpCommunityExName_Type()
)
hh3cSnmpCommunityExName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cSnmpCommunityExName.setStatus("current")


class _Hh3cSnmpCommunityExWrite_Type(TruthValue):
    """Custom type hh3cSnmpCommunityExWrite based on TruthValue"""
    defaultValue = 2


_Hh3cSnmpCommunityExWrite_Type.__name__ = "TruthValue"
_Hh3cSnmpCommunityExWrite_Object = MibTableColumn
hh3cSnmpCommunityExWrite = _Hh3cSnmpCommunityExWrite_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 104, 2, 2, 1, 2),
    _Hh3cSnmpCommunityExWrite_Type()
)
hh3cSnmpCommunityExWrite.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cSnmpCommunityExWrite.setStatus("current")


class _Hh3cSnmpCommunityExViewName_Type(OctetString):
    """Custom type hh3cSnmpCommunityExViewName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_Hh3cSnmpCommunityExViewName_Type.__name__ = "OctetString"
_Hh3cSnmpCommunityExViewName_Object = MibTableColumn
hh3cSnmpCommunityExViewName = _Hh3cSnmpCommunityExViewName_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 104, 2, 2, 1, 3),
    _Hh3cSnmpCommunityExViewName_Type()
)
hh3cSnmpCommunityExViewName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cSnmpCommunityExViewName.setStatus("current")


class _Hh3cSnmpCommunityExAclNum_Type(Integer32):
    """Custom type hh3cSnmpCommunityExAclNum based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(2000, 2999),
    )


_Hh3cSnmpCommunityExAclNum_Type.__name__ = "Integer32"
_Hh3cSnmpCommunityExAclNum_Object = MibTableColumn
hh3cSnmpCommunityExAclNum = _Hh3cSnmpCommunityExAclNum_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 104, 2, 2, 1, 4),
    _Hh3cSnmpCommunityExAclNum_Type()
)
hh3cSnmpCommunityExAclNum.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cSnmpCommunityExAclNum.setStatus("current")
_Hh3cSnmpCommunityExRowStatus_Type = RowStatus
_Hh3cSnmpCommunityExRowStatus_Object = MibTableColumn
hh3cSnmpCommunityExRowStatus = _Hh3cSnmpCommunityExRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 104, 2, 2, 1, 5),
    _Hh3cSnmpCommunityExRowStatus_Type()
)
hh3cSnmpCommunityExRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cSnmpCommunityExRowStatus.setStatus("current")
_Hh3cSnmpExtContextTable_Object = MibTable
hh3cSnmpExtContextTable = _Hh3cSnmpExtContextTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 104, 2, 3)
)
if mibBuilder.loadTexts:
    hh3cSnmpExtContextTable.setStatus("current")
_Hh3cSnmpExtContextEntry_Object = MibTableRow
hh3cSnmpExtContextEntry = _Hh3cSnmpExtContextEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 104, 2, 3, 1)
)
hh3cSnmpExtContextEntry.setIndexNames(
    (0, "HH3C-SNMP-EXT-MIB", "hh3cSnmpExtContextName"),
)
if mibBuilder.loadTexts:
    hh3cSnmpExtContextEntry.setStatus("current")


class _Hh3cSnmpExtContextName_Type(SnmpAdminString):
    """Custom type hh3cSnmpExtContextName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_Hh3cSnmpExtContextName_Type.__name__ = "SnmpAdminString"
_Hh3cSnmpExtContextName_Object = MibTableColumn
hh3cSnmpExtContextName = _Hh3cSnmpExtContextName_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 104, 2, 3, 1, 1),
    _Hh3cSnmpExtContextName_Type()
)
hh3cSnmpExtContextName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cSnmpExtContextName.setStatus("current")
_Hh3cSnmpExtContextRowStatus_Type = RowStatus
_Hh3cSnmpExtContextRowStatus_Object = MibTableColumn
hh3cSnmpExtContextRowStatus = _Hh3cSnmpExtContextRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 104, 2, 3, 1, 2),
    _Hh3cSnmpExtContextRowStatus_Type()
)
hh3cSnmpExtContextRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cSnmpExtContextRowStatus.setStatus("current")
_Hh3cSnmpExtNotifications_ObjectIdentity = ObjectIdentity
hh3cSnmpExtNotifications = _Hh3cSnmpExtNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 104, 3)
)
_Hh3cSnmpExtPrivProtocols_ObjectIdentity = ObjectIdentity
hh3cSnmpExtPrivProtocols = _Hh3cSnmpExtPrivProtocols_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 104, 4)
)
_Hh3cSnmpExtAESCfb192PrivProtocol_ObjectIdentity = ObjectIdentity
hh3cSnmpExtAESCfb192PrivProtocol = _Hh3cSnmpExtAESCfb192PrivProtocol_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 104, 4, 1)
)
if mibBuilder.loadTexts:
    hh3cSnmpExtAESCfb192PrivProtocol.setStatus("current")
_Hh3cSnmpExtAESCfb256PrivProtocol_ObjectIdentity = ObjectIdentity
hh3cSnmpExtAESCfb256PrivProtocol = _Hh3cSnmpExtAESCfb256PrivProtocol_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 104, 4, 2)
)
if mibBuilder.loadTexts:
    hh3cSnmpExtAESCfb256PrivProtocol.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HH3C-SNMP-EXT-MIB",
    **{"hh3cSnmpExt": hh3cSnmpExt,
       "hh3cSnmpExtScalarObjects": hh3cSnmpExtScalarObjects,
       "hh3cSnmpExtSnmpChannel": hh3cSnmpExtSnmpChannel,
       "hh3cSnmpExtReadCommunitySingle": hh3cSnmpExtReadCommunitySingle,
       "hh3cSnmpExtWriteCommunitySingle": hh3cSnmpExtWriteCommunitySingle,
       "hh3cSnmpExtMaxContextNum": hh3cSnmpExtMaxContextNum,
       "hh3cSnmpExtVersion": hh3cSnmpExtVersion,
       "hh3cSnmpExtTrapSource": hh3cSnmpExtTrapSource,
       "hh3cSnmpExtInformSource": hh3cSnmpExtInformSource,
       "hh3cSnmpExtAclNum": hh3cSnmpExtAclNum,
       "hh3cSnmpExtAclName": hh3cSnmpExtAclName,
       "hh3cSnmpExtIPv6AclNum": hh3cSnmpExtIPv6AclNum,
       "hh3cSnmpExtIPv6AclName": hh3cSnmpExtIPv6AclName,
       "hh3cSnmpExtTables": hh3cSnmpExtTables,
       "hh3cSnmpExtCommunityTable": hh3cSnmpExtCommunityTable,
       "hh3cSnmpExtCommunityEntry": hh3cSnmpExtCommunityEntry,
       "hh3cSnmpExtCommunitySecurityLevel": hh3cSnmpExtCommunitySecurityLevel,
       "hh3cSnmpExtCommunitySecurityName": hh3cSnmpExtCommunitySecurityName,
       "hh3cSnmpExtCommunityName": hh3cSnmpExtCommunityName,
       "hh3cSnmpExtCommunityAclNum": hh3cSnmpExtCommunityAclNum,
       "hh3cSnmpExtCommunityIPv6AclNum": hh3cSnmpExtCommunityIPv6AclNum,
       "hh3cSnmpCommunityExTable": hh3cSnmpCommunityExTable,
       "hh3cSnmpCommunityExEntry": hh3cSnmpCommunityExEntry,
       "hh3cSnmpCommunityExName": hh3cSnmpCommunityExName,
       "hh3cSnmpCommunityExWrite": hh3cSnmpCommunityExWrite,
       "hh3cSnmpCommunityExViewName": hh3cSnmpCommunityExViewName,
       "hh3cSnmpCommunityExAclNum": hh3cSnmpCommunityExAclNum,
       "hh3cSnmpCommunityExRowStatus": hh3cSnmpCommunityExRowStatus,
       "hh3cSnmpExtContextTable": hh3cSnmpExtContextTable,
       "hh3cSnmpExtContextEntry": hh3cSnmpExtContextEntry,
       "hh3cSnmpExtContextName": hh3cSnmpExtContextName,
       "hh3cSnmpExtContextRowStatus": hh3cSnmpExtContextRowStatus,
       "hh3cSnmpExtNotifications": hh3cSnmpExtNotifications,
       "hh3cSnmpExtPrivProtocols": hh3cSnmpExtPrivProtocols,
       "hh3cSnmpExtAESCfb192PrivProtocol": hh3cSnmpExtAESCfb192PrivProtocol,
       "hh3cSnmpExtAESCfb256PrivProtocol": hh3cSnmpExtAESCfb256PrivProtocol}
)
