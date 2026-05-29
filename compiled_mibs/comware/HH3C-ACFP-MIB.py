# SNMP MIB module (HH3C-ACFP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\comware\HH3C-ACFP-MIB

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

(InetAddressPrefixLength,) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddressPrefixLength")

(Ipv6Address,) = mibBuilder.importSymbols(
    "IPV6-TC",
    "Ipv6Address")

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

hh3cAcfp = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 74)
)
if mibBuilder.loadTexts:
    hh3cAcfp.setRevisions(
        ("2006-07-04 19:36",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Hh3cAcfpObjects_ObjectIdentity = ObjectIdentity
hh3cAcfpObjects = _Hh3cAcfpObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 74, 1)
)
_Hh3cAcfpOAP_ObjectIdentity = ObjectIdentity
hh3cAcfpOAP = _Hh3cAcfpOAP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 74, 1, 1)
)
_Hh3cAcfpServer_ObjectIdentity = ObjectIdentity
hh3cAcfpServer = _Hh3cAcfpServer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 74, 1, 1, 1)
)


class _Hh3cAcfpServerInfo_Type(Bits):
    """Custom type hh3cAcfpServerInfo based on Bits"""
    namedValues = NamedValues(
        *(("ipserver", 0),
          ("redirect", 1),
          ("mirror", 2),
          ("passThrough", 3))
    )

_Hh3cAcfpServerInfo_Type.__name__ = "Bits"
_Hh3cAcfpServerInfo_Object = MibScalar
hh3cAcfpServerInfo = _Hh3cAcfpServerInfo_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 74, 1, 1, 1, 1),
    _Hh3cAcfpServerInfo_Type()
)
hh3cAcfpServerInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cAcfpServerInfo.setStatus("current")


class _Hh3cAcfpServerMaxLifetime_Type(Integer32):
    """Custom type hh3cAcfpServerMaxLifetime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_Hh3cAcfpServerMaxLifetime_Type.__name__ = "Integer32"
_Hh3cAcfpServerMaxLifetime_Object = MibScalar
hh3cAcfpServerMaxLifetime = _Hh3cAcfpServerMaxLifetime_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 74, 1, 1, 1, 2),
    _Hh3cAcfpServerMaxLifetime_Type()
)
hh3cAcfpServerMaxLifetime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cAcfpServerMaxLifetime.setStatus("current")
if mibBuilder.loadTexts:
    hh3cAcfpServerMaxLifetime.setUnits("seconds")
_Hh3cAcfpServerPersistentRules_Type = TruthValue
_Hh3cAcfpServerPersistentRules_Object = MibScalar
hh3cAcfpServerPersistentRules = _Hh3cAcfpServerPersistentRules_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 74, 1, 1, 1, 3),
    _Hh3cAcfpServerPersistentRules_Type()
)
hh3cAcfpServerPersistentRules.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cAcfpServerPersistentRules.setStatus("current")


class _Hh3cAcfpServerCurContextType_Type(Integer32):
    """Custom type hh3cAcfpServerCurContextType based on Integer32"""
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
        *(("no-context", 1),
          ("context-VLANID", 2),
          ("context-HG", 3),
          ("context-FlowID", 4),
          ("context-HGPlus", 5))
    )


_Hh3cAcfpServerCurContextType_Type.__name__ = "Integer32"
_Hh3cAcfpServerCurContextType_Object = MibScalar
hh3cAcfpServerCurContextType = _Hh3cAcfpServerCurContextType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 74, 1, 1, 1, 4),
    _Hh3cAcfpServerCurContextType_Type()
)
hh3cAcfpServerCurContextType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cAcfpServerCurContextType.setStatus("current")
_Hh3cAcfpClientInfo_ObjectIdentity = ObjectIdentity
hh3cAcfpClientInfo = _Hh3cAcfpClientInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 74, 1, 1, 2)
)
_Hh3cAcfpClientInfoTable_Object = MibTable
hh3cAcfpClientInfoTable = _Hh3cAcfpClientInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 74, 1, 1, 2, 1)
)
if mibBuilder.loadTexts:
    hh3cAcfpClientInfoTable.setStatus("current")
_Hh3cAcfpClientInfoEntry_Object = MibTableRow
hh3cAcfpClientInfoEntry = _Hh3cAcfpClientInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 74, 1, 1, 2, 1, 1)
)
hh3cAcfpClientInfoEntry.setIndexNames(
    (0, "HH3C-ACFP-MIB", "hh3cAcfpClientID"),
)
if mibBuilder.loadTexts:
    hh3cAcfpClientInfoEntry.setStatus("current")


class _Hh3cAcfpClientID_Type(Integer32):
    """Custom type hh3cAcfpClientID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Hh3cAcfpClientID_Type.__name__ = "Integer32"
_Hh3cAcfpClientID_Object = MibTableColumn
hh3cAcfpClientID = _Hh3cAcfpClientID_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 74, 1, 1, 2, 1, 1, 1),
    _Hh3cAcfpClientID_Type()
)
hh3cAcfpClientID.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cAcfpClientID.setStatus("current")


class _Hh3cAcfpClientDescription_Type(DisplayString):
    """Custom type hh3cAcfpClientDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_Hh3cAcfpClientDescription_Type.__name__ = "DisplayString"
_Hh3cAcfpClientDescription_Object = MibTableColumn
hh3cAcfpClientDescription = _Hh3cAcfpClientDescription_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 74, 1, 1, 2, 1, 1, 2),
    _Hh3cAcfpClientDescription_Type()
)
hh3cAcfpClientDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cAcfpClientDescription.setStatus("current")


class _Hh3cAcfpClientHwVersion_Type(DisplayString):
    """Custom type hh3cAcfpClientHwVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_Hh3cAcfpClientHwVersion_Type.__name__ = "DisplayString"
_Hh3cAcfpClientHwVersion_Object = MibTableColumn
hh3cAcfpClientHwVersion = _Hh3cAcfpClientHwVersion_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 74, 1, 1, 2, 1, 1, 3),
    _Hh3cAcfpClientHwVersion_Type()
)
hh3cAcfpClientHwVersion.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cAcfpClientHwVersion.setStatus("current")


class _Hh3cAcfpClientOSVersion_Type(DisplayString):
    """Custom type hh3cAcfpClientOSVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_Hh3cAcfpClientOSVersion_Type.__name__ = "DisplayString"
_Hh3cAcfpClientOSVersion_Object = MibTableColumn
hh3cAcfpClientOSVersion = _Hh3cAcfpClientOSVersion_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 74, 1, 1, 2, 1, 1, 4),
    _Hh3cAcfpClientOSVersion_Type()
)
hh3cAcfpClientOSVersion.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cAcfpClientOSVersion.setStatus("current")


class _Hh3cAcfpClientAppVersion_Type(DisplayString):
    """Custom type hh3cAcfpClientAppVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_Hh3cAcfpClientAppVersion_Type.__name__ = "DisplayString"
_Hh3cAcfpClientAppVersion_Object = MibTableColumn
hh3cAcfpClientAppVersion = _Hh3cAcfpClientAppVersion_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 74, 1, 1, 2, 1, 1, 5),
    _Hh3cAcfpClientAppVersion_Type()
)
hh3cAcfpClientAppVersion.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cAcfpClientAppVersion.setStatus("current")
_Hh3cAcfpClientIP_Type = IpAddress
_Hh3cAcfpClientIP_Object = MibTableColumn
hh3cAcfpClientIP = _Hh3cAcfpClientIP_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 74, 1, 1, 2, 1, 1, 6),
    _Hh3cAcfpClientIP_Type()
)
hh3cAcfpClientIP.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cAcfpClientIP.setStatus("current")


class _Hh3cAcfpClientMode_Type(Bits):
    """Custom type hh3cAcfpClientMode based on Bits"""
    defaultHexValue = ""

    namedValues = NamedValues(
        *(("ipserver", 0),
          ("redirect", 1),
          ("mirror", 2),
          ("passThrough", 3))
    )

_Hh3cAcfpClientMode_Type.__name__ = "Bits"
_Hh3cAcfpClientMode_Object = MibTableColumn
hh3cAcfpClientMode = _Hh3cAcfpClientMode_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 74, 1, 1, 2, 1, 1, 7),
    _Hh3cAcfpClientMode_Type()
)
hh3cAcfpClientMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cAcfpClientMode.setStatus("current")
_Hh3cAcfpClientRowStatus_Type = RowStatus
_Hh3cAcfpClientRowStatus_Object = MibTableColumn
hh3cAcfpClientRowStatus = _Hh3cAcfpClientRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 74, 1, 1, 2, 1, 1, 8),
    _Hh3cAcfpClientRowStatus_Type()
)
hh3cAcfpClientRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cAcfpClientRowStatus.setStatus("current")
_Hh3cAcfpPolicy_ObjectIdentity = ObjectIdentity
hh3cAcfpPolicy = _Hh3cAcfpPolicy_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 74, 1, 1, 3)
)
_Hh3cAcfpPolicyTable_Object = MibTable
hh3cAcfpPolicyTable = _Hh3cAcfpPolicyTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 74, 1, 1, 3, 1)
)
if mibBuilder.loadTexts:
    hh3cAcfpPolicyTable.setStatus("current")
_Hh3cAcfpPolicyEntry_Object = MibTableRow
hh3cAcfpPolicyEntry = _Hh3cAcfpPolicyEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 74, 1, 1, 3, 1, 1)
)
hh3cAcfpPolicyEntry.setIndexNames(
    (0, "HH3C-ACFP-MIB", "hh3cAcfpClientID"),
    (0, "HH3C-ACFP-MIB", "hh3cAcfpPolicyIndex"),
)
if mibBuilder.loadTexts:
    hh3cAcfpPolicyEntry.setStatus("current")


class _Hh3cAcfpPolicyIndex_Type(Integer32):
    """Custom type hh3cAcfpPolicyIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Hh3cAcfpPolicyIndex_Type.__name__ = "Integer32"
_Hh3cAcfpPolicyIndex_Object = MibTableColumn
hh3cAcfpPolicyIndex = _Hh3cAcfpPolicyIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 74, 1, 1, 3, 1, 1, 1),
    _Hh3cAcfpPolicyIndex_Type()
)
hh3cAcfpPolicyIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cAcfpPolicyIndex.setStatus("current")


class _Hh3cAcfpPolicyInIfIndex_Type(Integer32):
    """Custom type hh3cAcfpPolicyInIfIndex based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_Hh3cAcfpPolicyInIfIndex_Type.__name__ = "Integer32"
_Hh3cAcfpPolicyInIfIndex_Object = MibTableColumn
hh3cAcfpPolicyInIfIndex = _Hh3cAcfpPolicyInIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 74, 1, 1, 3, 1, 1, 2),
    _Hh3cAcfpPolicyInIfIndex_Type()
)
hh3cAcfpPolicyInIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cAcfpPolicyInIfIndex.setStatus("current")


class _Hh3cAcfpPolicyOutIfIndex_Type(Integer32):
    """Custom type hh3cAcfpPolicyOutIfIndex based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_Hh3cAcfpPolicyOutIfIndex_Type.__name__ = "Integer32"
_Hh3cAcfpPolicyOutIfIndex_Object = MibTableColumn
hh3cAcfpPolicyOutIfIndex = _Hh3cAcfpPolicyOutIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 74, 1, 1, 3, 1, 1, 3),
    _Hh3cAcfpPolicyOutIfIndex_Type()
)
hh3cAcfpPolicyOutIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cAcfpPolicyOutIfIndex.setStatus("current")


class _Hh3cAcfpPolicyDestIfIndex_Type(Integer32):
    """Custom type hh3cAcfpPolicyDestIfIndex based on Integer32"""
    defaultValue = 0


_Hh3cAcfpPolicyDestIfIndex_Type.__name__ = "Integer32"
_Hh3cAcfpPolicyDestIfIndex_Object = MibTableColumn
hh3cAcfpPolicyDestIfIndex = _Hh3cAcfpPolicyDestIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 74, 1, 1, 3, 1, 1, 4),
    _Hh3cAcfpPolicyDestIfIndex_Type()
)
hh3cAcfpPolicyDestIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cAcfpPolicyDestIfIndex.setStatus("current")


class _Hh3cAcfpPolicyContextID_Type(Integer32):
    """Custom type hh3cAcfpPolicyContextID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_Hh3cAcfpPolicyContextID_Type.__name__ = "Integer32"
_Hh3cAcfpPolicyContextID_Object = MibTableColumn
hh3cAcfpPolicyContextID = _Hh3cAcfpPolicyContextID_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 74, 1, 1, 3, 1, 1, 5),
    _Hh3cAcfpPolicyContextID_Type()
)
hh3cAcfpPolicyContextID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cAcfpPolicyContextID.setStatus("current")


class _Hh3cAcfpPolicyAdminStatus_Type(Integer32):
    """Custom type hh3cAcfpPolicyAdminStatus based on Integer32"""
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


_Hh3cAcfpPolicyAdminStatus_Type.__name__ = "Integer32"
_Hh3cAcfpPolicyAdminStatus_Object = MibTableColumn
hh3cAcfpPolicyAdminStatus = _Hh3cAcfpPolicyAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 74, 1, 1, 3, 1, 1, 6),
    _Hh3cAcfpPolicyAdminStatus_Type()
)
hh3cAcfpPolicyAdminStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cAcfpPolicyAdminStatus.setStatus("current")


class _Hh3cAcfpPolicyLifetime_Type(Integer32):
    """Custom type hh3cAcfpPolicyLifetime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_Hh3cAcfpPolicyLifetime_Type.__name__ = "Integer32"
_Hh3cAcfpPolicyLifetime_Object = MibTableColumn
hh3cAcfpPolicyLifetime = _Hh3cAcfpPolicyLifetime_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 74, 1, 1, 3, 1, 1, 7),
    _Hh3cAcfpPolicyLifetime_Type()
)
hh3cAcfpPolicyLifetime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cAcfpPolicyLifetime.setStatus("current")
if mibBuilder.loadTexts:
    hh3cAcfpPolicyLifetime.setUnits("seconds")


class _Hh3cAcfpPolicyTimeStart_Type(OctetString):
    """Custom type hh3cAcfpPolicyTimeStart based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )
    fixed_length = 8


_Hh3cAcfpPolicyTimeStart_Type.__name__ = "OctetString"
_Hh3cAcfpPolicyTimeStart_Object = MibTableColumn
hh3cAcfpPolicyTimeStart = _Hh3cAcfpPolicyTimeStart_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 74, 1, 1, 3, 1, 1, 8),
    _Hh3cAcfpPolicyTimeStart_Type()
)
hh3cAcfpPolicyTimeStart.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cAcfpPolicyTimeStart.setStatus("current")


class _Hh3cAcfpPolicyTimeEnd_Type(OctetString):
    """Custom type hh3cAcfpPolicyTimeEnd based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )
    fixed_length = 8


_Hh3cAcfpPolicyTimeEnd_Type.__name__ = "OctetString"
_Hh3cAcfpPolicyTimeEnd_Object = MibTableColumn
hh3cAcfpPolicyTimeEnd = _Hh3cAcfpPolicyTimeEnd_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 74, 1, 1, 3, 1, 1, 9),
    _Hh3cAcfpPolicyTimeEnd_Type()
)
hh3cAcfpPolicyTimeEnd.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cAcfpPolicyTimeEnd.setStatus("current")
_Hh3cAcfpPolicyRowStatus_Type = RowStatus
_Hh3cAcfpPolicyRowStatus_Object = MibTableColumn
hh3cAcfpPolicyRowStatus = _Hh3cAcfpPolicyRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 74, 1, 1, 3, 1, 1, 10),
    _Hh3cAcfpPolicyRowStatus_Type()
)
hh3cAcfpPolicyRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cAcfpPolicyRowStatus.setStatus("current")


class _Hh3cAcfpPolicyDestIfFailAction_Type(Integer32):
    """Custom type hh3cAcfpPolicyDestIfFailAction based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("delete", 1),
          ("reserve", 2))
    )


_Hh3cAcfpPolicyDestIfFailAction_Type.__name__ = "Integer32"
_Hh3cAcfpPolicyDestIfFailAction_Object = MibTableColumn
hh3cAcfpPolicyDestIfFailAction = _Hh3cAcfpPolicyDestIfFailAction_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 74, 1, 1, 3, 1, 1, 11),
    _Hh3cAcfpPolicyDestIfFailAction_Type()
)
hh3cAcfpPolicyDestIfFailAction.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cAcfpPolicyDestIfFailAction.setStatus("current")


class _Hh3cAcfpPolicyPriority_Type(Integer32):
    """Custom type hh3cAcfpPolicyPriority based on Integer32"""
    defaultValue = 4

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
              8)
        )
    )
    namedValues = NamedValues(
        *(("priority1", 1),
          ("priority2", 2),
          ("priority3", 3),
          ("priority4", 4),
          ("priority5", 5),
          ("priority6", 6),
          ("priority7", 7),
          ("priority8", 8))
    )


_Hh3cAcfpPolicyPriority_Type.__name__ = "Integer32"
_Hh3cAcfpPolicyPriority_Object = MibTableColumn
hh3cAcfpPolicyPriority = _Hh3cAcfpPolicyPriority_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 74, 1, 1, 3, 1, 1, 12),
    _Hh3cAcfpPolicyPriority_Type()
)
hh3cAcfpPolicyPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cAcfpPolicyPriority.setStatus("current")
_Hh3cAcfpRule_ObjectIdentity = ObjectIdentity
hh3cAcfpRule = _Hh3cAcfpRule_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 74, 1, 1, 4)
)
_Hh3cAcfpRuleTable_Object = MibTable
hh3cAcfpRuleTable = _Hh3cAcfpRuleTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 74, 1, 1, 4, 1)
)
if mibBuilder.loadTexts:
    hh3cAcfpRuleTable.setStatus("current")
_Hh3cAcfpRuleEntry_Object = MibTableRow
hh3cAcfpRuleEntry = _Hh3cAcfpRuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 74, 1, 1, 4, 1, 1)
)
hh3cAcfpRuleEntry.setIndexNames(
    (0, "HH3C-ACFP-MIB", "hh3cAcfpClientID"),
    (0, "HH3C-ACFP-MIB", "hh3cAcfpPolicyIndex"),
    (0, "HH3C-ACFP-MIB", "hh3cAcfpRuleIndex"),
)
if mibBuilder.loadTexts:
    hh3cAcfpRuleEntry.setStatus("current")


class _Hh3cAcfpRuleIndex_Type(Integer32):
    """Custom type hh3cAcfpRuleIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Hh3cAcfpRuleIndex_Type.__name__ = "Integer32"
_Hh3cAcfpRuleIndex_Object = MibTableColumn
hh3cAcfpRuleIndex = _Hh3cAcfpRuleIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 74, 1, 1, 4, 1, 1, 1),
    _Hh3cAcfpRuleIndex_Type()
)
hh3cAcfpRuleIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cAcfpRuleIndex.setStatus("current")


class _Hh3cAcfpRuleOperStatus_Type(Integer32):
    """Custom type hh3cAcfpRuleOperStatus based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("success", 1),
          ("fail", 2))
    )


_Hh3cAcfpRuleOperStatus_Type.__name__ = "Integer32"
_Hh3cAcfpRuleOperStatus_Object = MibTableColumn
hh3cAcfpRuleOperStatus = _Hh3cAcfpRuleOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 74, 1, 1, 4, 1, 1, 2),
    _Hh3cAcfpRuleOperStatus_Type()
)
hh3cAcfpRuleOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cAcfpRuleOperStatus.setStatus("current")


class _Hh3cAcfpRuleAction_Type(Integer32):
    """Custom type hh3cAcfpRuleAction based on Integer32"""
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
        *(("permit", 1),
          ("deny", 2),
          ("redirect", 3),
          ("mirror", 4),
          ("rate", 5))
    )


_Hh3cAcfpRuleAction_Type.__name__ = "Integer32"
_Hh3cAcfpRuleAction_Object = MibTableColumn
hh3cAcfpRuleAction = _Hh3cAcfpRuleAction_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 74, 1, 1, 4, 1, 1, 3),
    _Hh3cAcfpRuleAction_Type()
)
hh3cAcfpRuleAction.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cAcfpRuleAction.setStatus("current")


class _Hh3cAcfpRuleAll_Type(TruthValue):
    """Custom type hh3cAcfpRuleAll based on TruthValue"""
    defaultValue = 2


_Hh3cAcfpRuleAll_Type.__name__ = "TruthValue"
_Hh3cAcfpRuleAll_Object = MibTableColumn
hh3cAcfpRuleAll = _Hh3cAcfpRuleAll_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 74, 1, 1, 4, 1, 1, 4),
    _Hh3cAcfpRuleAll_Type()
)
hh3cAcfpRuleAll.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cAcfpRuleAll.setStatus("current")
_Hh3cAcfpRuleSrcMAC_Type = MacAddress
_Hh3cAcfpRuleSrcMAC_Object = MibTableColumn
hh3cAcfpRuleSrcMAC = _Hh3cAcfpRuleSrcMAC_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 74, 1, 1, 4, 1, 1, 5),
    _Hh3cAcfpRuleSrcMAC_Type()
)
hh3cAcfpRuleSrcMAC.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cAcfpRuleSrcMAC.setStatus("current")
_Hh3cAcfpRuleDstMAC_Type = MacAddress
_Hh3cAcfpRuleDstMAC_Object = MibTableColumn
hh3cAcfpRuleDstMAC = _Hh3cAcfpRuleDstMAC_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 74, 1, 1, 4, 1, 1, 6),
    _Hh3cAcfpRuleDstMAC_Type()
)
hh3cAcfpRuleDstMAC.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cAcfpRuleDstMAC.setStatus("current")


class _Hh3cAcfpRuleVlanStart_Type(Integer32):
    """Custom type hh3cAcfpRuleVlanStart based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_Hh3cAcfpRuleVlanStart_Type.__name__ = "Integer32"
_Hh3cAcfpRuleVlanStart_Object = MibTableColumn
hh3cAcfpRuleVlanStart = _Hh3cAcfpRuleVlanStart_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 74, 1, 1, 4, 1, 1, 7),
    _Hh3cAcfpRuleVlanStart_Type()
)
hh3cAcfpRuleVlanStart.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cAcfpRuleVlanStart.setStatus("current")


class _Hh3cAcfpRuleVlanEnd_Type(Integer32):
    """Custom type hh3cAcfpRuleVlanEnd based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_Hh3cAcfpRuleVlanEnd_Type.__name__ = "Integer32"
_Hh3cAcfpRuleVlanEnd_Object = MibTableColumn
hh3cAcfpRuleVlanEnd = _Hh3cAcfpRuleVlanEnd_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 74, 1, 1, 4, 1, 1, 8),
    _Hh3cAcfpRuleVlanEnd_Type()
)
hh3cAcfpRuleVlanEnd.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cAcfpRuleVlanEnd.setStatus("current")


class _Hh3cAcfpRuleProtocol_Type(Integer32):
    """Custom type hh3cAcfpRuleProtocol based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_Hh3cAcfpRuleProtocol_Type.__name__ = "Integer32"
_Hh3cAcfpRuleProtocol_Object = MibTableColumn
hh3cAcfpRuleProtocol = _Hh3cAcfpRuleProtocol_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 74, 1, 1, 4, 1, 1, 9),
    _Hh3cAcfpRuleProtocol_Type()
)
hh3cAcfpRuleProtocol.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cAcfpRuleProtocol.setStatus("current")
_Hh3cAcfpRuleSrcIP_Type = IpAddress
_Hh3cAcfpRuleSrcIP_Object = MibTableColumn
hh3cAcfpRuleSrcIP = _Hh3cAcfpRuleSrcIP_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 74, 1, 1, 4, 1, 1, 10),
    _Hh3cAcfpRuleSrcIP_Type()
)
hh3cAcfpRuleSrcIP.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cAcfpRuleSrcIP.setStatus("current")
_Hh3cAcfpRuleSrcIPMask_Type = IpAddress
_Hh3cAcfpRuleSrcIPMask_Object = MibTableColumn
hh3cAcfpRuleSrcIPMask = _Hh3cAcfpRuleSrcIPMask_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 74, 1, 1, 4, 1, 1, 11),
    _Hh3cAcfpRuleSrcIPMask_Type()
)
hh3cAcfpRuleSrcIPMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cAcfpRuleSrcIPMask.setStatus("current")


class _Hh3cAcfpRuleSrcOp_Type(Integer32):
    """Custom type hh3cAcfpRuleSrcOp based on Integer32"""
    defaultValue = 6

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
        *(("equal", 1),
          ("notEqual", 2),
          ("lessThan", 3),
          ("greaterThan", 4),
          ("range", 5),
          ("invalid", 6))
    )


_Hh3cAcfpRuleSrcOp_Type.__name__ = "Integer32"
_Hh3cAcfpRuleSrcOp_Object = MibTableColumn
hh3cAcfpRuleSrcOp = _Hh3cAcfpRuleSrcOp_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 74, 1, 1, 4, 1, 1, 12),
    _Hh3cAcfpRuleSrcOp_Type()
)
hh3cAcfpRuleSrcOp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cAcfpRuleSrcOp.setStatus("current")


class _Hh3cAcfpRuleSrcStartPort_Type(Integer32):
    """Custom type hh3cAcfpRuleSrcStartPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Hh3cAcfpRuleSrcStartPort_Type.__name__ = "Integer32"
_Hh3cAcfpRuleSrcStartPort_Object = MibTableColumn
hh3cAcfpRuleSrcStartPort = _Hh3cAcfpRuleSrcStartPort_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 74, 1, 1, 4, 1, 1, 13),
    _Hh3cAcfpRuleSrcStartPort_Type()
)
hh3cAcfpRuleSrcStartPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cAcfpRuleSrcStartPort.setStatus("current")


class _Hh3cAcfpRuleSrcEndPort_Type(Integer32):
    """Custom type hh3cAcfpRuleSrcEndPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Hh3cAcfpRuleSrcEndPort_Type.__name__ = "Integer32"
_Hh3cAcfpRuleSrcEndPort_Object = MibTableColumn
hh3cAcfpRuleSrcEndPort = _Hh3cAcfpRuleSrcEndPort_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 74, 1, 1, 4, 1, 1, 14),
    _Hh3cAcfpRuleSrcEndPort_Type()
)
hh3cAcfpRuleSrcEndPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cAcfpRuleSrcEndPort.setStatus("current")
_Hh3cAcfpRuleDstIP_Type = IpAddress
_Hh3cAcfpRuleDstIP_Object = MibTableColumn
hh3cAcfpRuleDstIP = _Hh3cAcfpRuleDstIP_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 74, 1, 1, 4, 1, 1, 15),
    _Hh3cAcfpRuleDstIP_Type()
)
hh3cAcfpRuleDstIP.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cAcfpRuleDstIP.setStatus("current")
_Hh3cAcfpRuleDstIPMask_Type = IpAddress
_Hh3cAcfpRuleDstIPMask_Object = MibTableColumn
hh3cAcfpRuleDstIPMask = _Hh3cAcfpRuleDstIPMask_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 74, 1, 1, 4, 1, 1, 16),
    _Hh3cAcfpRuleDstIPMask_Type()
)
hh3cAcfpRuleDstIPMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cAcfpRuleDstIPMask.setStatus("current")


class _Hh3cAcfpRuleDstOp_Type(Integer32):
    """Custom type hh3cAcfpRuleDstOp based on Integer32"""
    defaultValue = 6

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
        *(("equal", 1),
          ("nonEqual", 2),
          ("lessThan", 3),
          ("greaterThan", 4),
          ("range", 5),
          ("invalid", 6))
    )


_Hh3cAcfpRuleDstOp_Type.__name__ = "Integer32"
_Hh3cAcfpRuleDstOp_Object = MibTableColumn
hh3cAcfpRuleDstOp = _Hh3cAcfpRuleDstOp_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 74, 1, 1, 4, 1, 1, 17),
    _Hh3cAcfpRuleDstOp_Type()
)
hh3cAcfpRuleDstOp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cAcfpRuleDstOp.setStatus("current")


class _Hh3cAcfpRuleDstStartPort_Type(Integer32):
    """Custom type hh3cAcfpRuleDstStartPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Hh3cAcfpRuleDstStartPort_Type.__name__ = "Integer32"
_Hh3cAcfpRuleDstStartPort_Object = MibTableColumn
hh3cAcfpRuleDstStartPort = _Hh3cAcfpRuleDstStartPort_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 74, 1, 1, 4, 1, 1, 18),
    _Hh3cAcfpRuleDstStartPort_Type()
)
hh3cAcfpRuleDstStartPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cAcfpRuleDstStartPort.setStatus("current")


class _Hh3cAcfpRuleDstEndPort_Type(Integer32):
    """Custom type hh3cAcfpRuleDstEndPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Hh3cAcfpRuleDstEndPort_Type.__name__ = "Integer32"
_Hh3cAcfpRuleDstEndPort_Object = MibTableColumn
hh3cAcfpRuleDstEndPort = _Hh3cAcfpRuleDstEndPort_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 74, 1, 1, 4, 1, 1, 19),
    _Hh3cAcfpRuleDstEndPort_Type()
)
hh3cAcfpRuleDstEndPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cAcfpRuleDstEndPort.setStatus("current")


class _Hh3cAcfpRulePrecedence_Type(Integer32):
    """Custom type hh3cAcfpRulePrecedence based on Integer32"""
    defaultValue = 255

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
        ValueRangeConstraint(255, 255),
    )


_Hh3cAcfpRulePrecedence_Type.__name__ = "Integer32"
_Hh3cAcfpRulePrecedence_Object = MibTableColumn
hh3cAcfpRulePrecedence = _Hh3cAcfpRulePrecedence_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 74, 1, 1, 4, 1, 1, 20),
    _Hh3cAcfpRulePrecedence_Type()
)
hh3cAcfpRulePrecedence.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cAcfpRulePrecedence.setStatus("current")


class _Hh3cAcfpRuleTos_Type(Integer32):
    """Custom type hh3cAcfpRuleTos based on Integer32"""
    defaultValue = 255

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
        ValueRangeConstraint(255, 255),
    )


_Hh3cAcfpRuleTos_Type.__name__ = "Integer32"
_Hh3cAcfpRuleTos_Object = MibTableColumn
hh3cAcfpRuleTos = _Hh3cAcfpRuleTos_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 74, 1, 1, 4, 1, 1, 21),
    _Hh3cAcfpRuleTos_Type()
)
hh3cAcfpRuleTos.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cAcfpRuleTos.setStatus("current")


class _Hh3cAcfpRuleDscp_Type(Integer32):
    """Custom type hh3cAcfpRuleDscp based on Integer32"""
    defaultValue = 255

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
        ValueRangeConstraint(255, 255),
    )


_Hh3cAcfpRuleDscp_Type.__name__ = "Integer32"
_Hh3cAcfpRuleDscp_Object = MibTableColumn
hh3cAcfpRuleDscp = _Hh3cAcfpRuleDscp_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 74, 1, 1, 4, 1, 1, 22),
    _Hh3cAcfpRuleDscp_Type()
)
hh3cAcfpRuleDscp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cAcfpRuleDscp.setStatus("current")


class _Hh3cAcfpRuleEstablish_Type(TruthValue):
    """Custom type hh3cAcfpRuleEstablish based on TruthValue"""
    defaultValue = 2


_Hh3cAcfpRuleEstablish_Type.__name__ = "TruthValue"
_Hh3cAcfpRuleEstablish_Object = MibTableColumn
hh3cAcfpRuleEstablish = _Hh3cAcfpRuleEstablish_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 74, 1, 1, 4, 1, 1, 23),
    _Hh3cAcfpRuleEstablish_Type()
)
hh3cAcfpRuleEstablish.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cAcfpRuleEstablish.setStatus("deprecated")


class _Hh3cAcfpRuleFragment_Type(TruthValue):
    """Custom type hh3cAcfpRuleFragment based on TruthValue"""
    defaultValue = 2


_Hh3cAcfpRuleFragment_Type.__name__ = "TruthValue"
_Hh3cAcfpRuleFragment_Object = MibTableColumn
hh3cAcfpRuleFragment = _Hh3cAcfpRuleFragment_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 74, 1, 1, 4, 1, 1, 24),
    _Hh3cAcfpRuleFragment_Type()
)
hh3cAcfpRuleFragment.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cAcfpRuleFragment.setStatus("current")
_Hh3cAcfpRulePacketRate_Type = Integer32
_Hh3cAcfpRulePacketRate_Object = MibTableColumn
hh3cAcfpRulePacketRate = _Hh3cAcfpRulePacketRate_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 74, 1, 1, 4, 1, 1, 25),
    _Hh3cAcfpRulePacketRate_Type()
)
hh3cAcfpRulePacketRate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cAcfpRulePacketRate.setStatus("current")
_Hh3cAcfpRuleRowStatus_Type = RowStatus
_Hh3cAcfpRuleRowStatus_Object = MibTableColumn
hh3cAcfpRuleRowStatus = _Hh3cAcfpRuleRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 74, 1, 1, 4, 1, 1, 26),
    _Hh3cAcfpRuleRowStatus_Type()
)
hh3cAcfpRuleRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cAcfpRuleRowStatus.setStatus("current")


class _Hh3cAcfpRuleTCPFlag_Type(Integer32):
    """Custom type hh3cAcfpRuleTCPFlag based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Hh3cAcfpRuleTCPFlag_Type.__name__ = "Integer32"
_Hh3cAcfpRuleTCPFlag_Object = MibTableColumn
hh3cAcfpRuleTCPFlag = _Hh3cAcfpRuleTCPFlag_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 74, 1, 1, 4, 1, 1, 27),
    _Hh3cAcfpRuleTCPFlag_Type()
)
hh3cAcfpRuleTCPFlag.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cAcfpRuleTCPFlag.setStatus("current")
_Hh3cAcfpRuleSrcIPV6Address_Type = Ipv6Address
_Hh3cAcfpRuleSrcIPV6Address_Object = MibTableColumn
hh3cAcfpRuleSrcIPV6Address = _Hh3cAcfpRuleSrcIPV6Address_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 74, 1, 1, 4, 1, 1, 28),
    _Hh3cAcfpRuleSrcIPV6Address_Type()
)
hh3cAcfpRuleSrcIPV6Address.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cAcfpRuleSrcIPV6Address.setStatus("current")
_Hh3cAcfpRuleSrcPrefixLen_Type = InetAddressPrefixLength
_Hh3cAcfpRuleSrcPrefixLen_Object = MibTableColumn
hh3cAcfpRuleSrcPrefixLen = _Hh3cAcfpRuleSrcPrefixLen_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 74, 1, 1, 4, 1, 1, 29),
    _Hh3cAcfpRuleSrcPrefixLen_Type()
)
hh3cAcfpRuleSrcPrefixLen.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cAcfpRuleSrcPrefixLen.setStatus("current")
_Hh3cAcfpRuleDstIPV6Address_Type = Ipv6Address
_Hh3cAcfpRuleDstIPV6Address_Object = MibTableColumn
hh3cAcfpRuleDstIPV6Address = _Hh3cAcfpRuleDstIPV6Address_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 74, 1, 1, 4, 1, 1, 30),
    _Hh3cAcfpRuleDstIPV6Address_Type()
)
hh3cAcfpRuleDstIPV6Address.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cAcfpRuleDstIPV6Address.setStatus("current")
_Hh3cAcfpRuleDstPrefixLen_Type = InetAddressPrefixLength
_Hh3cAcfpRuleDstPrefixLen_Object = MibTableColumn
hh3cAcfpRuleDstPrefixLen = _Hh3cAcfpRuleDstPrefixLen_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 74, 1, 1, 4, 1, 1, 31),
    _Hh3cAcfpRuleDstPrefixLen_Type()
)
hh3cAcfpRuleDstPrefixLen.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cAcfpRuleDstPrefixLen.setStatus("current")


class _Hh3cAcfpRuleTrafficType_Type(Bits):
    """Custom type hh3cAcfpRuleTrafficType based on Bits"""
    namedValues = NamedValues(
        *(("unicast", 0),
          ("multicast", 1),
          ("broadcast", 2))
    )

_Hh3cAcfpRuleTrafficType_Type.__name__ = "Bits"
_Hh3cAcfpRuleTrafficType_Object = MibTableColumn
hh3cAcfpRuleTrafficType = _Hh3cAcfpRuleTrafficType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 74, 1, 1, 4, 1, 1, 32),
    _Hh3cAcfpRuleTrafficType_Type()
)
hh3cAcfpRuleTrafficType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cAcfpRuleTrafficType.setStatus("current")


class _Hh3cAcfpRuleTypeOrLen_Type(Integer32):
    """Custom type hh3cAcfpRuleTypeOrLen based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Hh3cAcfpRuleTypeOrLen_Type.__name__ = "Integer32"
_Hh3cAcfpRuleTypeOrLen_Object = MibTableColumn
hh3cAcfpRuleTypeOrLen = _Hh3cAcfpRuleTypeOrLen_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 74, 1, 1, 4, 1, 1, 33),
    _Hh3cAcfpRuleTypeOrLen_Type()
)
hh3cAcfpRuleTypeOrLen.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cAcfpRuleTypeOrLen.setStatus("current")
_Hh3cAcfpNotifications_ObjectIdentity = ObjectIdentity
hh3cAcfpNotifications = _Hh3cAcfpNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 74, 1, 1, 5)
)

# Managed Objects groups


# Notification objects

hh3cAcfpCurContextChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 74, 1, 1, 5, 1)
)
hh3cAcfpCurContextChanged.setObjects(
    ("HH3C-ACFP-MIB", "hh3cAcfpServerCurContextType")
)
if mibBuilder.loadTexts:
    hh3cAcfpCurContextChanged.setStatus(
        "current"
    )

hh3cAcfpClientRegister = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 74, 1, 1, 5, 2)
)
hh3cAcfpClientRegister.setObjects(
    ("HH3C-ACFP-MIB", "hh3cAcfpClientID")
)
if mibBuilder.loadTexts:
    hh3cAcfpClientRegister.setStatus(
        "current"
    )

hh3cAcfpClientUnRegister = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 74, 1, 1, 5, 3)
)
hh3cAcfpClientUnRegister.setObjects(
    ("HH3C-ACFP-MIB", "hh3cAcfpClientID")
)
if mibBuilder.loadTexts:
    hh3cAcfpClientUnRegister.setStatus(
        "current"
    )

hh3cAcfpClientDead = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 74, 1, 1, 5, 4)
)
hh3cAcfpClientDead.setObjects(
    ("HH3C-ACFP-MIB", "hh3cAcfpClientID")
)
if mibBuilder.loadTexts:
    hh3cAcfpClientDead.setStatus(
        "current"
    )

hh3cAcfpNotSupportedOAPMode = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 74, 1, 1, 5, 5)
)
hh3cAcfpNotSupportedOAPMode.setObjects(
      *(("HH3C-ACFP-MIB", "hh3cAcfpClientID"),
        ("HH3C-ACFP-MIB", "hh3cAcfpClientMode"),
        ("HH3C-ACFP-MIB", "hh3cAcfpServerInfo"))
)
if mibBuilder.loadTexts:
    hh3cAcfpNotSupportedOAPMode.setStatus(
        "current"
    )

hh3cAcfpLifetimeChangeEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 74, 1, 1, 5, 6)
)
hh3cAcfpLifetimeChangeEvent.setObjects(
    ("HH3C-ACFP-MIB", "hh3cAcfpPolicyLifetime")
)
if mibBuilder.loadTexts:
    hh3cAcfpLifetimeChangeEvent.setStatus(
        "current"
    )

hh3cAcfpRuleCreatedEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 74, 1, 1, 5, 7)
)
hh3cAcfpRuleCreatedEvent.setObjects(
    ("HH3C-ACFP-MIB", "hh3cAcfpRuleIndex")
)
if mibBuilder.loadTexts:
    hh3cAcfpRuleCreatedEvent.setStatus(
        "current"
    )

hh3cAcfpRuleDeletedEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 74, 1, 1, 5, 8)
)
hh3cAcfpRuleDeletedEvent.setObjects(
    ("HH3C-ACFP-MIB", "hh3cAcfpRuleIndex")
)
if mibBuilder.loadTexts:
    hh3cAcfpRuleDeletedEvent.setStatus(
        "current"
    )

hh3cAcfpRuleErrorEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 74, 1, 1, 5, 9)
)
hh3cAcfpRuleErrorEvent.setObjects(
    ("HH3C-ACFP-MIB", "hh3cAcfpRuleIndex")
)
if mibBuilder.loadTexts:
    hh3cAcfpRuleErrorEvent.setStatus(
        "current"
    )

hh3cAcfpLifetimeExpireEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 74, 1, 1, 5, 10)
)
hh3cAcfpLifetimeExpireEvent.setObjects(
    ("HH3C-ACFP-MIB", "hh3cAcfpPolicyLifetime")
)
if mibBuilder.loadTexts:
    hh3cAcfpLifetimeExpireEvent.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HH3C-ACFP-MIB",
    **{"hh3cAcfp": hh3cAcfp,
       "hh3cAcfpObjects": hh3cAcfpObjects,
       "hh3cAcfpOAP": hh3cAcfpOAP,
       "hh3cAcfpServer": hh3cAcfpServer,
       "hh3cAcfpServerInfo": hh3cAcfpServerInfo,
       "hh3cAcfpServerMaxLifetime": hh3cAcfpServerMaxLifetime,
       "hh3cAcfpServerPersistentRules": hh3cAcfpServerPersistentRules,
       "hh3cAcfpServerCurContextType": hh3cAcfpServerCurContextType,
       "hh3cAcfpClientInfo": hh3cAcfpClientInfo,
       "hh3cAcfpClientInfoTable": hh3cAcfpClientInfoTable,
       "hh3cAcfpClientInfoEntry": hh3cAcfpClientInfoEntry,
       "hh3cAcfpClientID": hh3cAcfpClientID,
       "hh3cAcfpClientDescription": hh3cAcfpClientDescription,
       "hh3cAcfpClientHwVersion": hh3cAcfpClientHwVersion,
       "hh3cAcfpClientOSVersion": hh3cAcfpClientOSVersion,
       "hh3cAcfpClientAppVersion": hh3cAcfpClientAppVersion,
       "hh3cAcfpClientIP": hh3cAcfpClientIP,
       "hh3cAcfpClientMode": hh3cAcfpClientMode,
       "hh3cAcfpClientRowStatus": hh3cAcfpClientRowStatus,
       "hh3cAcfpPolicy": hh3cAcfpPolicy,
       "hh3cAcfpPolicyTable": hh3cAcfpPolicyTable,
       "hh3cAcfpPolicyEntry": hh3cAcfpPolicyEntry,
       "hh3cAcfpPolicyIndex": hh3cAcfpPolicyIndex,
       "hh3cAcfpPolicyInIfIndex": hh3cAcfpPolicyInIfIndex,
       "hh3cAcfpPolicyOutIfIndex": hh3cAcfpPolicyOutIfIndex,
       "hh3cAcfpPolicyDestIfIndex": hh3cAcfpPolicyDestIfIndex,
       "hh3cAcfpPolicyContextID": hh3cAcfpPolicyContextID,
       "hh3cAcfpPolicyAdminStatus": hh3cAcfpPolicyAdminStatus,
       "hh3cAcfpPolicyLifetime": hh3cAcfpPolicyLifetime,
       "hh3cAcfpPolicyTimeStart": hh3cAcfpPolicyTimeStart,
       "hh3cAcfpPolicyTimeEnd": hh3cAcfpPolicyTimeEnd,
       "hh3cAcfpPolicyRowStatus": hh3cAcfpPolicyRowStatus,
       "hh3cAcfpPolicyDestIfFailAction": hh3cAcfpPolicyDestIfFailAction,
       "hh3cAcfpPolicyPriority": hh3cAcfpPolicyPriority,
       "hh3cAcfpRule": hh3cAcfpRule,
       "hh3cAcfpRuleTable": hh3cAcfpRuleTable,
       "hh3cAcfpRuleEntry": hh3cAcfpRuleEntry,
       "hh3cAcfpRuleIndex": hh3cAcfpRuleIndex,
       "hh3cAcfpRuleOperStatus": hh3cAcfpRuleOperStatus,
       "hh3cAcfpRuleAction": hh3cAcfpRuleAction,
       "hh3cAcfpRuleAll": hh3cAcfpRuleAll,
       "hh3cAcfpRuleSrcMAC": hh3cAcfpRuleSrcMAC,
       "hh3cAcfpRuleDstMAC": hh3cAcfpRuleDstMAC,
       "hh3cAcfpRuleVlanStart": hh3cAcfpRuleVlanStart,
       "hh3cAcfpRuleVlanEnd": hh3cAcfpRuleVlanEnd,
       "hh3cAcfpRuleProtocol": hh3cAcfpRuleProtocol,
       "hh3cAcfpRuleSrcIP": hh3cAcfpRuleSrcIP,
       "hh3cAcfpRuleSrcIPMask": hh3cAcfpRuleSrcIPMask,
       "hh3cAcfpRuleSrcOp": hh3cAcfpRuleSrcOp,
       "hh3cAcfpRuleSrcStartPort": hh3cAcfpRuleSrcStartPort,
       "hh3cAcfpRuleSrcEndPort": hh3cAcfpRuleSrcEndPort,
       "hh3cAcfpRuleDstIP": hh3cAcfpRuleDstIP,
       "hh3cAcfpRuleDstIPMask": hh3cAcfpRuleDstIPMask,
       "hh3cAcfpRuleDstOp": hh3cAcfpRuleDstOp,
       "hh3cAcfpRuleDstStartPort": hh3cAcfpRuleDstStartPort,
       "hh3cAcfpRuleDstEndPort": hh3cAcfpRuleDstEndPort,
       "hh3cAcfpRulePrecedence": hh3cAcfpRulePrecedence,
       "hh3cAcfpRuleTos": hh3cAcfpRuleTos,
       "hh3cAcfpRuleDscp": hh3cAcfpRuleDscp,
       "hh3cAcfpRuleEstablish": hh3cAcfpRuleEstablish,
       "hh3cAcfpRuleFragment": hh3cAcfpRuleFragment,
       "hh3cAcfpRulePacketRate": hh3cAcfpRulePacketRate,
       "hh3cAcfpRuleRowStatus": hh3cAcfpRuleRowStatus,
       "hh3cAcfpRuleTCPFlag": hh3cAcfpRuleTCPFlag,
       "hh3cAcfpRuleSrcIPV6Address": hh3cAcfpRuleSrcIPV6Address,
       "hh3cAcfpRuleSrcPrefixLen": hh3cAcfpRuleSrcPrefixLen,
       "hh3cAcfpRuleDstIPV6Address": hh3cAcfpRuleDstIPV6Address,
       "hh3cAcfpRuleDstPrefixLen": hh3cAcfpRuleDstPrefixLen,
       "hh3cAcfpRuleTrafficType": hh3cAcfpRuleTrafficType,
       "hh3cAcfpRuleTypeOrLen": hh3cAcfpRuleTypeOrLen,
       "hh3cAcfpNotifications": hh3cAcfpNotifications,
       "hh3cAcfpCurContextChanged": hh3cAcfpCurContextChanged,
       "hh3cAcfpClientRegister": hh3cAcfpClientRegister,
       "hh3cAcfpClientUnRegister": hh3cAcfpClientUnRegister,
       "hh3cAcfpClientDead": hh3cAcfpClientDead,
       "hh3cAcfpNotSupportedOAPMode": hh3cAcfpNotSupportedOAPMode,
       "hh3cAcfpLifetimeChangeEvent": hh3cAcfpLifetimeChangeEvent,
       "hh3cAcfpRuleCreatedEvent": hh3cAcfpRuleCreatedEvent,
       "hh3cAcfpRuleDeletedEvent": hh3cAcfpRuleDeletedEvent,
       "hh3cAcfpRuleErrorEvent": hh3cAcfpRuleErrorEvent,
       "hh3cAcfpLifetimeExpireEvent": hh3cAcfpLifetimeExpireEvent}
)
