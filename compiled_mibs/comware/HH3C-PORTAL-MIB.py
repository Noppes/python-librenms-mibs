# SNMP MIB module (HH3C-PORTAL-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\comware\HH3C-PORTAL-MIB

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

(InterfaceIndex,
 ifIndex) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex",
    "ifIndex")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

hh3cPortal = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 99)
)
if mibBuilder.loadTexts:
    hh3cPortal.setRevisions(
        ("2016-07-14 10:20",
         "2015-10-08 10:20")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class Hh3cPortalAuthMethod(TextualConvention, Integer32):
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
        *(("invalid", 1),
          ("direct", 2),
          ("layer3", 3),
          ("redhcp", 4))
    )



# MIB Managed Objects in the order of their OIDs

_Hh3cPortalConfig_ObjectIdentity = ObjectIdentity
hh3cPortalConfig = _Hh3cPortalConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 99, 1)
)
_Hh3cPortalMaxUserNumber_Type = Integer32
_Hh3cPortalMaxUserNumber_Object = MibScalar
hh3cPortalMaxUserNumber = _Hh3cPortalMaxUserNumber_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 99, 1, 1),
    _Hh3cPortalMaxUserNumber_Type()
)
hh3cPortalMaxUserNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cPortalMaxUserNumber.setStatus("current")
_Hh3cPortalCurrentUserNumber_Type = Integer32
_Hh3cPortalCurrentUserNumber_Object = MibScalar
hh3cPortalCurrentUserNumber = _Hh3cPortalCurrentUserNumber_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 99, 1, 2),
    _Hh3cPortalCurrentUserNumber_Type()
)
hh3cPortalCurrentUserNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cPortalCurrentUserNumber.setStatus("current")


class _Hh3cPortalStatus_Type(Integer32):
    """Custom type hh3cPortalStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enabled", 1),
          ("disabled", 2))
    )


_Hh3cPortalStatus_Type.__name__ = "Integer32"
_Hh3cPortalStatus_Object = MibScalar
hh3cPortalStatus = _Hh3cPortalStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 99, 1, 3),
    _Hh3cPortalStatus_Type()
)
hh3cPortalStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cPortalStatus.setStatus("current")
_Hh3cPortalUserNumberUpperLimit_Type = Integer32
_Hh3cPortalUserNumberUpperLimit_Object = MibScalar
hh3cPortalUserNumberUpperLimit = _Hh3cPortalUserNumberUpperLimit_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 99, 1, 4),
    _Hh3cPortalUserNumberUpperLimit_Type()
)
hh3cPortalUserNumberUpperLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cPortalUserNumberUpperLimit.setStatus("current")
_Hh3cPortalNasId_Type = OctetString
_Hh3cPortalNasId_Object = MibScalar
hh3cPortalNasId = _Hh3cPortalNasId_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 99, 1, 5),
    _Hh3cPortalNasId_Type()
)
hh3cPortalNasId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cPortalNasId.setStatus("current")
_Hh3cPortalTables_ObjectIdentity = ObjectIdentity
hh3cPortalTables = _Hh3cPortalTables_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 99, 2)
)
_Hh3cPortalServerTable_Object = MibTable
hh3cPortalServerTable = _Hh3cPortalServerTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 99, 2, 1)
)
if mibBuilder.loadTexts:
    hh3cPortalServerTable.setStatus("current")
_Hh3cPortalServerEntry_Object = MibTableRow
hh3cPortalServerEntry = _Hh3cPortalServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 99, 2, 1, 1)
)
hh3cPortalServerEntry.setIndexNames(
    (0, "HH3C-PORTAL-MIB", "hh3cPortalServerName"),
)
if mibBuilder.loadTexts:
    hh3cPortalServerEntry.setStatus("current")


class _Hh3cPortalServerName_Type(OctetString):
    """Custom type hh3cPortalServerName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_Hh3cPortalServerName_Type.__name__ = "OctetString"
_Hh3cPortalServerName_Object = MibTableColumn
hh3cPortalServerName = _Hh3cPortalServerName_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 99, 2, 1, 1, 1),
    _Hh3cPortalServerName_Type()
)
hh3cPortalServerName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cPortalServerName.setStatus("current")


class _Hh3cPortalServerUrl_Type(OctetString):
    """Custom type hh3cPortalServerUrl based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 127),
    )


_Hh3cPortalServerUrl_Type.__name__ = "OctetString"
_Hh3cPortalServerUrl_Object = MibTableColumn
hh3cPortalServerUrl = _Hh3cPortalServerUrl_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 99, 2, 1, 1, 2),
    _Hh3cPortalServerUrl_Type()
)
hh3cPortalServerUrl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cPortalServerUrl.setStatus("current")


class _Hh3cPortalServerPort_Type(Integer32):
    """Custom type hh3cPortalServerPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65534),
    )


_Hh3cPortalServerPort_Type.__name__ = "Integer32"
_Hh3cPortalServerPort_Object = MibTableColumn
hh3cPortalServerPort = _Hh3cPortalServerPort_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 99, 2, 1, 1, 3),
    _Hh3cPortalServerPort_Type()
)
hh3cPortalServerPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cPortalServerPort.setStatus("current")
_Hh3cPortalIfInfoTable_Object = MibTable
hh3cPortalIfInfoTable = _Hh3cPortalIfInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 99, 2, 2)
)
if mibBuilder.loadTexts:
    hh3cPortalIfInfoTable.setStatus("current")
_Hh3cPortalIfInfoEntry_Object = MibTableRow
hh3cPortalIfInfoEntry = _Hh3cPortalIfInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 99, 2, 2, 1)
)
hh3cPortalIfInfoEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    hh3cPortalIfInfoEntry.setStatus("current")
_Hh3cPortalAuthReqNumber_Type = Integer32
_Hh3cPortalAuthReqNumber_Object = MibTableColumn
hh3cPortalAuthReqNumber = _Hh3cPortalAuthReqNumber_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 99, 2, 2, 1, 1),
    _Hh3cPortalAuthReqNumber_Type()
)
hh3cPortalAuthReqNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cPortalAuthReqNumber.setStatus("current")
_Hh3cPortalAuthSuccNumber_Type = Integer32
_Hh3cPortalAuthSuccNumber_Object = MibTableColumn
hh3cPortalAuthSuccNumber = _Hh3cPortalAuthSuccNumber_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 99, 2, 2, 1, 2),
    _Hh3cPortalAuthSuccNumber_Type()
)
hh3cPortalAuthSuccNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cPortalAuthSuccNumber.setStatus("current")
_Hh3cPortalAuthFailNumber_Type = Integer32
_Hh3cPortalAuthFailNumber_Object = MibTableColumn
hh3cPortalAuthFailNumber = _Hh3cPortalAuthFailNumber_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 99, 2, 2, 1, 3),
    _Hh3cPortalAuthFailNumber_Type()
)
hh3cPortalAuthFailNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cPortalAuthFailNumber.setStatus("current")
_Hh3cPortalIfServerTable_Object = MibTable
hh3cPortalIfServerTable = _Hh3cPortalIfServerTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 99, 2, 3)
)
if mibBuilder.loadTexts:
    hh3cPortalIfServerTable.setStatus("current")
_Hh3cPortalIfServerEntry_Object = MibTableRow
hh3cPortalIfServerEntry = _Hh3cPortalIfServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 99, 2, 3, 1)
)
hh3cPortalIfServerEntry.setIndexNames(
    (0, "HH3C-PORTAL-MIB", "hh3cPortalIfServerIndex"),
)
if mibBuilder.loadTexts:
    hh3cPortalIfServerEntry.setStatus("current")


class _Hh3cPortalIfServerIndex_Type(Integer32):
    """Custom type hh3cPortalIfServerIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_Hh3cPortalIfServerIndex_Type.__name__ = "Integer32"
_Hh3cPortalIfServerIndex_Object = MibTableColumn
hh3cPortalIfServerIndex = _Hh3cPortalIfServerIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 99, 2, 3, 1, 1),
    _Hh3cPortalIfServerIndex_Type()
)
hh3cPortalIfServerIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cPortalIfServerIndex.setStatus("current")
_Hh3cPortalIfServerUrl_Type = OctetString
_Hh3cPortalIfServerUrl_Object = MibTableColumn
hh3cPortalIfServerUrl = _Hh3cPortalIfServerUrl_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 99, 2, 3, 1, 2),
    _Hh3cPortalIfServerUrl_Type()
)
hh3cPortalIfServerUrl.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cPortalIfServerUrl.setStatus("current")
_Hh3cPortalIfServerRowStatus_Type = RowStatus
_Hh3cPortalIfServerRowStatus_Object = MibTableColumn
hh3cPortalIfServerRowStatus = _Hh3cPortalIfServerRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 99, 2, 3, 1, 3),
    _Hh3cPortalIfServerRowStatus_Type()
)
hh3cPortalIfServerRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cPortalIfServerRowStatus.setStatus("current")
_Hh3cPortalIfVlanNasIDTable_Object = MibTable
hh3cPortalIfVlanNasIDTable = _Hh3cPortalIfVlanNasIDTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 99, 2, 4)
)
if mibBuilder.loadTexts:
    hh3cPortalIfVlanNasIDTable.setStatus("current")
_Hh3cPortalIfVlanNasIDEntry_Object = MibTableRow
hh3cPortalIfVlanNasIDEntry = _Hh3cPortalIfVlanNasIDEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 99, 2, 4, 1)
)
hh3cPortalIfVlanNasIDEntry.setIndexNames(
    (0, "HH3C-PORTAL-MIB", "hh3cPortalIfVlanNasIDIfIndex"),
    (0, "HH3C-PORTAL-MIB", "hh3cPortalIfVlanNasIDVlanID"),
)
if mibBuilder.loadTexts:
    hh3cPortalIfVlanNasIDEntry.setStatus("current")
_Hh3cPortalIfVlanNasIDIfIndex_Type = InterfaceIndex
_Hh3cPortalIfVlanNasIDIfIndex_Object = MibTableColumn
hh3cPortalIfVlanNasIDIfIndex = _Hh3cPortalIfVlanNasIDIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 99, 2, 4, 1, 1),
    _Hh3cPortalIfVlanNasIDIfIndex_Type()
)
hh3cPortalIfVlanNasIDIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cPortalIfVlanNasIDIfIndex.setStatus("current")


class _Hh3cPortalIfVlanNasIDVlanID_Type(Integer32):
    """Custom type hh3cPortalIfVlanNasIDVlanID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Hh3cPortalIfVlanNasIDVlanID_Type.__name__ = "Integer32"
_Hh3cPortalIfVlanNasIDVlanID_Object = MibTableColumn
hh3cPortalIfVlanNasIDVlanID = _Hh3cPortalIfVlanNasIDVlanID_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 99, 2, 4, 1, 2),
    _Hh3cPortalIfVlanNasIDVlanID_Type()
)
hh3cPortalIfVlanNasIDVlanID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cPortalIfVlanNasIDVlanID.setStatus("current")


class _Hh3cPortalIfVlanNasIDNasID_Type(OctetString):
    """Custom type hh3cPortalIfVlanNasIDNasID based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_Hh3cPortalIfVlanNasIDNasID_Type.__name__ = "OctetString"
_Hh3cPortalIfVlanNasIDNasID_Object = MibTableColumn
hh3cPortalIfVlanNasIDNasID = _Hh3cPortalIfVlanNasIDNasID_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 99, 2, 4, 1, 3),
    _Hh3cPortalIfVlanNasIDNasID_Type()
)
hh3cPortalIfVlanNasIDNasID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cPortalIfVlanNasIDNasID.setStatus("current")
_Hh3cPortalSSIDFreeRuleTable_Object = MibTable
hh3cPortalSSIDFreeRuleTable = _Hh3cPortalSSIDFreeRuleTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 99, 2, 5)
)
if mibBuilder.loadTexts:
    hh3cPortalSSIDFreeRuleTable.setStatus("current")
_Hh3cPortalSSIDFreeRuleEntry_Object = MibTableRow
hh3cPortalSSIDFreeRuleEntry = _Hh3cPortalSSIDFreeRuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 99, 2, 5, 1)
)
hh3cPortalSSIDFreeRuleEntry.setIndexNames(
    (0, "HH3C-PORTAL-MIB", "hh3cPortalSSIDFreeRuleIndex"),
)
if mibBuilder.loadTexts:
    hh3cPortalSSIDFreeRuleEntry.setStatus("current")


class _Hh3cPortalSSIDFreeRuleIndex_Type(Integer32):
    """Custom type hh3cPortalSSIDFreeRuleIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_Hh3cPortalSSIDFreeRuleIndex_Type.__name__ = "Integer32"
_Hh3cPortalSSIDFreeRuleIndex_Object = MibTableColumn
hh3cPortalSSIDFreeRuleIndex = _Hh3cPortalSSIDFreeRuleIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 99, 2, 5, 1, 1),
    _Hh3cPortalSSIDFreeRuleIndex_Type()
)
hh3cPortalSSIDFreeRuleIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cPortalSSIDFreeRuleIndex.setStatus("current")


class _Hh3cPortalSSIDFreeRuleSrcSSID_Type(OctetString):
    """Custom type hh3cPortalSSIDFreeRuleSrcSSID based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_Hh3cPortalSSIDFreeRuleSrcSSID_Type.__name__ = "OctetString"
_Hh3cPortalSSIDFreeRuleSrcSSID_Object = MibTableColumn
hh3cPortalSSIDFreeRuleSrcSSID = _Hh3cPortalSSIDFreeRuleSrcSSID_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 99, 2, 5, 1, 2),
    _Hh3cPortalSSIDFreeRuleSrcSSID_Type()
)
hh3cPortalSSIDFreeRuleSrcSSID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cPortalSSIDFreeRuleSrcSSID.setStatus("current")
_Hh3cPortalSSIDFreeRuleRowStatus_Type = RowStatus
_Hh3cPortalSSIDFreeRuleRowStatus_Object = MibTableColumn
hh3cPortalSSIDFreeRuleRowStatus = _Hh3cPortalSSIDFreeRuleRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 99, 2, 5, 1, 3),
    _Hh3cPortalSSIDFreeRuleRowStatus_Type()
)
hh3cPortalSSIDFreeRuleRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cPortalSSIDFreeRuleRowStatus.setStatus("current")


class _Hh3cPortalSSIDFreeRuleSrcSpot_Type(OctetString):
    """Custom type hh3cPortalSSIDFreeRuleSrcSpot based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_Hh3cPortalSSIDFreeRuleSrcSpot_Type.__name__ = "OctetString"
_Hh3cPortalSSIDFreeRuleSrcSpot_Object = MibTableColumn
hh3cPortalSSIDFreeRuleSrcSpot = _Hh3cPortalSSIDFreeRuleSrcSpot_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 99, 2, 5, 1, 4),
    _Hh3cPortalSSIDFreeRuleSrcSpot_Type()
)
hh3cPortalSSIDFreeRuleSrcSpot.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cPortalSSIDFreeRuleSrcSpot.setStatus("current")
_Hh3cPortalMacTriggerSrvTable_Object = MibTable
hh3cPortalMacTriggerSrvTable = _Hh3cPortalMacTriggerSrvTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 99, 2, 6)
)
if mibBuilder.loadTexts:
    hh3cPortalMacTriggerSrvTable.setStatus("current")
_Hh3cPortalMacTriggerSrvEntry_Object = MibTableRow
hh3cPortalMacTriggerSrvEntry = _Hh3cPortalMacTriggerSrvEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 99, 2, 6, 1)
)
hh3cPortalMacTriggerSrvEntry.setIndexNames(
    (0, "HH3C-PORTAL-MIB", "hh3cPortalMacTriggerSrvIndex"),
)
if mibBuilder.loadTexts:
    hh3cPortalMacTriggerSrvEntry.setStatus("current")


class _Hh3cPortalMacTriggerSrvIndex_Type(Integer32):
    """Custom type hh3cPortalMacTriggerSrvIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_Hh3cPortalMacTriggerSrvIndex_Type.__name__ = "Integer32"
_Hh3cPortalMacTriggerSrvIndex_Object = MibTableColumn
hh3cPortalMacTriggerSrvIndex = _Hh3cPortalMacTriggerSrvIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 99, 2, 6, 1, 1),
    _Hh3cPortalMacTriggerSrvIndex_Type()
)
hh3cPortalMacTriggerSrvIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cPortalMacTriggerSrvIndex.setStatus("current")
_Hh3cPortalMacTriggerSrvIPAddrType_Type = InetAddressType
_Hh3cPortalMacTriggerSrvIPAddrType_Object = MibTableColumn
hh3cPortalMacTriggerSrvIPAddrType = _Hh3cPortalMacTriggerSrvIPAddrType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 99, 2, 6, 1, 2),
    _Hh3cPortalMacTriggerSrvIPAddrType_Type()
)
hh3cPortalMacTriggerSrvIPAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cPortalMacTriggerSrvIPAddrType.setStatus("current")
_Hh3cPortalMacTriggerSrvIP_Type = InetAddress
_Hh3cPortalMacTriggerSrvIP_Object = MibTableColumn
hh3cPortalMacTriggerSrvIP = _Hh3cPortalMacTriggerSrvIP_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 99, 2, 6, 1, 3),
    _Hh3cPortalMacTriggerSrvIP_Type()
)
hh3cPortalMacTriggerSrvIP.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cPortalMacTriggerSrvIP.setStatus("current")


class _Hh3cPortalMacTriggerSrvPort_Type(Integer32):
    """Custom type hh3cPortalMacTriggerSrvPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65534),
    )


_Hh3cPortalMacTriggerSrvPort_Type.__name__ = "Integer32"
_Hh3cPortalMacTriggerSrvPort_Object = MibTableColumn
hh3cPortalMacTriggerSrvPort = _Hh3cPortalMacTriggerSrvPort_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 99, 2, 6, 1, 4),
    _Hh3cPortalMacTriggerSrvPort_Type()
)
hh3cPortalMacTriggerSrvPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cPortalMacTriggerSrvPort.setStatus("current")
_Hh3cPortalMacTriggerSrvRowStatus_Type = RowStatus
_Hh3cPortalMacTriggerSrvRowStatus_Object = MibTableColumn
hh3cPortalMacTriggerSrvRowStatus = _Hh3cPortalMacTriggerSrvRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 99, 2, 6, 1, 5),
    _Hh3cPortalMacTriggerSrvRowStatus_Type()
)
hh3cPortalMacTriggerSrvRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cPortalMacTriggerSrvRowStatus.setStatus("current")
_Hh3cPortalMacTriggerOnIfTable_Object = MibTable
hh3cPortalMacTriggerOnIfTable = _Hh3cPortalMacTriggerOnIfTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 99, 2, 7)
)
if mibBuilder.loadTexts:
    hh3cPortalMacTriggerOnIfTable.setStatus("current")
_Hh3cPortalMacTriggerOnIfEntry_Object = MibTableRow
hh3cPortalMacTriggerOnIfEntry = _Hh3cPortalMacTriggerOnIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 99, 2, 7, 1)
)
hh3cPortalMacTriggerOnIfEntry.setIndexNames(
    (0, "HH3C-PORTAL-MIB", "hh3cPortalMacTriggerOnIfIfIndex"),
)
if mibBuilder.loadTexts:
    hh3cPortalMacTriggerOnIfEntry.setStatus("current")
_Hh3cPortalMacTriggerOnIfIfIndex_Type = InterfaceIndex
_Hh3cPortalMacTriggerOnIfIfIndex_Object = MibTableColumn
hh3cPortalMacTriggerOnIfIfIndex = _Hh3cPortalMacTriggerOnIfIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 99, 2, 7, 1, 1),
    _Hh3cPortalMacTriggerOnIfIfIndex_Type()
)
hh3cPortalMacTriggerOnIfIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cPortalMacTriggerOnIfIfIndex.setStatus("current")


class _Hh3cPortalMacTriggerOnIfDetctFlowPeriod_Type(Integer32):
    """Custom type hh3cPortalMacTriggerOnIfDetctFlowPeriod based on Integer32"""
    defaultValue = 300


_Hh3cPortalMacTriggerOnIfDetctFlowPeriod_Type.__name__ = "Integer32"
_Hh3cPortalMacTriggerOnIfDetctFlowPeriod_Object = MibTableColumn
hh3cPortalMacTriggerOnIfDetctFlowPeriod = _Hh3cPortalMacTriggerOnIfDetctFlowPeriod_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 99, 2, 7, 1, 2),
    _Hh3cPortalMacTriggerOnIfDetctFlowPeriod_Type()
)
hh3cPortalMacTriggerOnIfDetctFlowPeriod.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cPortalMacTriggerOnIfDetctFlowPeriod.setStatus("current")
if mibBuilder.loadTexts:
    hh3cPortalMacTriggerOnIfDetctFlowPeriod.setUnits("seconds")


class _Hh3cPortalMacTriggerOnIfThresholdFlow_Type(Unsigned32):
    """Custom type hh3cPortalMacTriggerOnIfThresholdFlow based on Unsigned32"""
    defaultValue = 0


_Hh3cPortalMacTriggerOnIfThresholdFlow_Type.__name__ = "Unsigned32"
_Hh3cPortalMacTriggerOnIfThresholdFlow_Object = MibTableColumn
hh3cPortalMacTriggerOnIfThresholdFlow = _Hh3cPortalMacTriggerOnIfThresholdFlow_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 99, 2, 7, 1, 3),
    _Hh3cPortalMacTriggerOnIfThresholdFlow_Type()
)
hh3cPortalMacTriggerOnIfThresholdFlow.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cPortalMacTriggerOnIfThresholdFlow.setStatus("current")
if mibBuilder.loadTexts:
    hh3cPortalMacTriggerOnIfThresholdFlow.setUnits("bytes")
_Hh3cPortalMacTriggerOnIfRowStatus_Type = RowStatus
_Hh3cPortalMacTriggerOnIfRowStatus_Object = MibTableColumn
hh3cPortalMacTriggerOnIfRowStatus = _Hh3cPortalMacTriggerOnIfRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 99, 2, 7, 1, 4),
    _Hh3cPortalMacTriggerOnIfRowStatus_Type()
)
hh3cPortalMacTriggerOnIfRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cPortalMacTriggerOnIfRowStatus.setStatus("current")
_Hh3cPortalFreeRuleTable_Object = MibTable
hh3cPortalFreeRuleTable = _Hh3cPortalFreeRuleTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 99, 2, 8)
)
if mibBuilder.loadTexts:
    hh3cPortalFreeRuleTable.setStatus("current")
_Hh3cPortalFreeRuleEntry_Object = MibTableRow
hh3cPortalFreeRuleEntry = _Hh3cPortalFreeRuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 99, 2, 8, 1)
)
hh3cPortalFreeRuleEntry.setIndexNames(
    (0, "HH3C-PORTAL-MIB", "hh3cPortalFreeRuleIndex"),
)
if mibBuilder.loadTexts:
    hh3cPortalFreeRuleEntry.setStatus("current")


class _Hh3cPortalFreeRuleIndex_Type(Integer32):
    """Custom type hh3cPortalFreeRuleIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_Hh3cPortalFreeRuleIndex_Type.__name__ = "Integer32"
_Hh3cPortalFreeRuleIndex_Object = MibTableColumn
hh3cPortalFreeRuleIndex = _Hh3cPortalFreeRuleIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 99, 2, 8, 1, 1),
    _Hh3cPortalFreeRuleIndex_Type()
)
hh3cPortalFreeRuleIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cPortalFreeRuleIndex.setStatus("current")
_Hh3cPortalFreeRuleSrcIfIndex_Type = InterfaceIndex
_Hh3cPortalFreeRuleSrcIfIndex_Object = MibTableColumn
hh3cPortalFreeRuleSrcIfIndex = _Hh3cPortalFreeRuleSrcIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 99, 2, 8, 1, 2),
    _Hh3cPortalFreeRuleSrcIfIndex_Type()
)
hh3cPortalFreeRuleSrcIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cPortalFreeRuleSrcIfIndex.setStatus("current")
_Hh3cPortalFreeRuleSrcVlanID_Type = Integer32
_Hh3cPortalFreeRuleSrcVlanID_Object = MibTableColumn
hh3cPortalFreeRuleSrcVlanID = _Hh3cPortalFreeRuleSrcVlanID_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 99, 2, 8, 1, 3),
    _Hh3cPortalFreeRuleSrcVlanID_Type()
)
hh3cPortalFreeRuleSrcVlanID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cPortalFreeRuleSrcVlanID.setStatus("current")
_Hh3cPortalFreeRuleSrcMac_Type = MacAddress
_Hh3cPortalFreeRuleSrcMac_Object = MibTableColumn
hh3cPortalFreeRuleSrcMac = _Hh3cPortalFreeRuleSrcMac_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 99, 2, 8, 1, 4),
    _Hh3cPortalFreeRuleSrcMac_Type()
)
hh3cPortalFreeRuleSrcMac.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cPortalFreeRuleSrcMac.setStatus("current")
_Hh3cPortalFreeRuleAddrType_Type = InetAddressType
_Hh3cPortalFreeRuleAddrType_Object = MibTableColumn
hh3cPortalFreeRuleAddrType = _Hh3cPortalFreeRuleAddrType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 99, 2, 8, 1, 5),
    _Hh3cPortalFreeRuleAddrType_Type()
)
hh3cPortalFreeRuleAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cPortalFreeRuleAddrType.setStatus("current")
_Hh3cPortalFreeRuleSrcAddr_Type = InetAddress
_Hh3cPortalFreeRuleSrcAddr_Object = MibTableColumn
hh3cPortalFreeRuleSrcAddr = _Hh3cPortalFreeRuleSrcAddr_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 99, 2, 8, 1, 6),
    _Hh3cPortalFreeRuleSrcAddr_Type()
)
hh3cPortalFreeRuleSrcAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cPortalFreeRuleSrcAddr.setStatus("current")
_Hh3cPortalFreeRuleSrcPrefix_Type = InetAddressPrefixLength
_Hh3cPortalFreeRuleSrcPrefix_Object = MibTableColumn
hh3cPortalFreeRuleSrcPrefix = _Hh3cPortalFreeRuleSrcPrefix_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 99, 2, 8, 1, 7),
    _Hh3cPortalFreeRuleSrcPrefix_Type()
)
hh3cPortalFreeRuleSrcPrefix.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cPortalFreeRuleSrcPrefix.setStatus("current")
_Hh3cPortalFreeRuleDstAddr_Type = InetAddress
_Hh3cPortalFreeRuleDstAddr_Object = MibTableColumn
hh3cPortalFreeRuleDstAddr = _Hh3cPortalFreeRuleDstAddr_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 99, 2, 8, 1, 8),
    _Hh3cPortalFreeRuleDstAddr_Type()
)
hh3cPortalFreeRuleDstAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cPortalFreeRuleDstAddr.setStatus("current")
_Hh3cPortalFreeRuleDstPrefix_Type = InetAddressPrefixLength
_Hh3cPortalFreeRuleDstPrefix_Object = MibTableColumn
hh3cPortalFreeRuleDstPrefix = _Hh3cPortalFreeRuleDstPrefix_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 99, 2, 8, 1, 9),
    _Hh3cPortalFreeRuleDstPrefix_Type()
)
hh3cPortalFreeRuleDstPrefix.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cPortalFreeRuleDstPrefix.setStatus("current")


class _Hh3cPortalFreeRuleProtocol_Type(Integer32):
    """Custom type hh3cPortalFreeRuleProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              6,
              17)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 0),
          ("tcp", 6),
          ("udp", 17))
    )


_Hh3cPortalFreeRuleProtocol_Type.__name__ = "Integer32"
_Hh3cPortalFreeRuleProtocol_Object = MibTableColumn
hh3cPortalFreeRuleProtocol = _Hh3cPortalFreeRuleProtocol_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 99, 2, 8, 1, 10),
    _Hh3cPortalFreeRuleProtocol_Type()
)
hh3cPortalFreeRuleProtocol.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cPortalFreeRuleProtocol.setStatus("current")
_Hh3cPortalFreeRuleSrcPort_Type = Integer32
_Hh3cPortalFreeRuleSrcPort_Object = MibTableColumn
hh3cPortalFreeRuleSrcPort = _Hh3cPortalFreeRuleSrcPort_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 99, 2, 8, 1, 11),
    _Hh3cPortalFreeRuleSrcPort_Type()
)
hh3cPortalFreeRuleSrcPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cPortalFreeRuleSrcPort.setStatus("current")
_Hh3cPortalFreeRuleDstPort_Type = Integer32
_Hh3cPortalFreeRuleDstPort_Object = MibTableColumn
hh3cPortalFreeRuleDstPort = _Hh3cPortalFreeRuleDstPort_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 99, 2, 8, 1, 12),
    _Hh3cPortalFreeRuleDstPort_Type()
)
hh3cPortalFreeRuleDstPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cPortalFreeRuleDstPort.setStatus("current")
_Hh3cPortalFreeRuleRowStatus_Type = RowStatus
_Hh3cPortalFreeRuleRowStatus_Object = MibTableColumn
hh3cPortalFreeRuleRowStatus = _Hh3cPortalFreeRuleRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 99, 2, 8, 1, 13),
    _Hh3cPortalFreeRuleRowStatus_Type()
)
hh3cPortalFreeRuleRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cPortalFreeRuleRowStatus.setStatus("current")
_Hh3cPortalForbiddenRuleTable_Object = MibTable
hh3cPortalForbiddenRuleTable = _Hh3cPortalForbiddenRuleTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 99, 2, 9)
)
if mibBuilder.loadTexts:
    hh3cPortalForbiddenRuleTable.setStatus("current")
_Hh3cPortalForbiddenRuleEntry_Object = MibTableRow
hh3cPortalForbiddenRuleEntry = _Hh3cPortalForbiddenRuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 99, 2, 9, 1)
)
hh3cPortalForbiddenRuleEntry.setIndexNames(
    (0, "HH3C-PORTAL-MIB", "hh3cPortalForbiddenRuleIndex"),
)
if mibBuilder.loadTexts:
    hh3cPortalForbiddenRuleEntry.setStatus("current")


class _Hh3cPortalForbiddenRuleIndex_Type(Integer32):
    """Custom type hh3cPortalForbiddenRuleIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_Hh3cPortalForbiddenRuleIndex_Type.__name__ = "Integer32"
_Hh3cPortalForbiddenRuleIndex_Object = MibTableColumn
hh3cPortalForbiddenRuleIndex = _Hh3cPortalForbiddenRuleIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 99, 2, 9, 1, 1),
    _Hh3cPortalForbiddenRuleIndex_Type()
)
hh3cPortalForbiddenRuleIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cPortalForbiddenRuleIndex.setStatus("current")
_Hh3cPortalForbiddenRuleSrcIfIndex_Type = InterfaceIndex
_Hh3cPortalForbiddenRuleSrcIfIndex_Object = MibTableColumn
hh3cPortalForbiddenRuleSrcIfIndex = _Hh3cPortalForbiddenRuleSrcIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 99, 2, 9, 1, 2),
    _Hh3cPortalForbiddenRuleSrcIfIndex_Type()
)
hh3cPortalForbiddenRuleSrcIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cPortalForbiddenRuleSrcIfIndex.setStatus("current")
_Hh3cPortalForbiddenRuleSrcVlanID_Type = Integer32
_Hh3cPortalForbiddenRuleSrcVlanID_Object = MibTableColumn
hh3cPortalForbiddenRuleSrcVlanID = _Hh3cPortalForbiddenRuleSrcVlanID_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 99, 2, 9, 1, 3),
    _Hh3cPortalForbiddenRuleSrcVlanID_Type()
)
hh3cPortalForbiddenRuleSrcVlanID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cPortalForbiddenRuleSrcVlanID.setStatus("current")
_Hh3cPortalForbiddenRuleSrcMac_Type = MacAddress
_Hh3cPortalForbiddenRuleSrcMac_Object = MibTableColumn
hh3cPortalForbiddenRuleSrcMac = _Hh3cPortalForbiddenRuleSrcMac_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 99, 2, 9, 1, 4),
    _Hh3cPortalForbiddenRuleSrcMac_Type()
)
hh3cPortalForbiddenRuleSrcMac.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cPortalForbiddenRuleSrcMac.setStatus("current")
_Hh3cPortalForbiddenRuleAddrType_Type = InetAddressType
_Hh3cPortalForbiddenRuleAddrType_Object = MibTableColumn
hh3cPortalForbiddenRuleAddrType = _Hh3cPortalForbiddenRuleAddrType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 99, 2, 9, 1, 5),
    _Hh3cPortalForbiddenRuleAddrType_Type()
)
hh3cPortalForbiddenRuleAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cPortalForbiddenRuleAddrType.setStatus("current")
_Hh3cPortalForbiddenRuleSrcAddr_Type = InetAddress
_Hh3cPortalForbiddenRuleSrcAddr_Object = MibTableColumn
hh3cPortalForbiddenRuleSrcAddr = _Hh3cPortalForbiddenRuleSrcAddr_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 99, 2, 9, 1, 6),
    _Hh3cPortalForbiddenRuleSrcAddr_Type()
)
hh3cPortalForbiddenRuleSrcAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cPortalForbiddenRuleSrcAddr.setStatus("current")
_Hh3cPortalForbiddenRuleSrcPrefix_Type = InetAddressPrefixLength
_Hh3cPortalForbiddenRuleSrcPrefix_Object = MibTableColumn
hh3cPortalForbiddenRuleSrcPrefix = _Hh3cPortalForbiddenRuleSrcPrefix_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 99, 2, 9, 1, 7),
    _Hh3cPortalForbiddenRuleSrcPrefix_Type()
)
hh3cPortalForbiddenRuleSrcPrefix.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cPortalForbiddenRuleSrcPrefix.setStatus("current")
_Hh3cPortalForbiddenRuleDstAddr_Type = InetAddress
_Hh3cPortalForbiddenRuleDstAddr_Object = MibTableColumn
hh3cPortalForbiddenRuleDstAddr = _Hh3cPortalForbiddenRuleDstAddr_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 99, 2, 9, 1, 8),
    _Hh3cPortalForbiddenRuleDstAddr_Type()
)
hh3cPortalForbiddenRuleDstAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cPortalForbiddenRuleDstAddr.setStatus("current")
_Hh3cPortalForbiddenRuleDstPrefix_Type = InetAddressPrefixLength
_Hh3cPortalForbiddenRuleDstPrefix_Object = MibTableColumn
hh3cPortalForbiddenRuleDstPrefix = _Hh3cPortalForbiddenRuleDstPrefix_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 99, 2, 9, 1, 9),
    _Hh3cPortalForbiddenRuleDstPrefix_Type()
)
hh3cPortalForbiddenRuleDstPrefix.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cPortalForbiddenRuleDstPrefix.setStatus("current")


class _Hh3cPortalForbiddenRuleProtocol_Type(Integer32):
    """Custom type hh3cPortalForbiddenRuleProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              6,
              17)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 0),
          ("tcp", 6),
          ("udp", 17))
    )


_Hh3cPortalForbiddenRuleProtocol_Type.__name__ = "Integer32"
_Hh3cPortalForbiddenRuleProtocol_Object = MibTableColumn
hh3cPortalForbiddenRuleProtocol = _Hh3cPortalForbiddenRuleProtocol_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 99, 2, 9, 1, 10),
    _Hh3cPortalForbiddenRuleProtocol_Type()
)
hh3cPortalForbiddenRuleProtocol.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cPortalForbiddenRuleProtocol.setStatus("current")
_Hh3cPortalForbiddenRuleSrcPort_Type = Integer32
_Hh3cPortalForbiddenRuleSrcPort_Object = MibTableColumn
hh3cPortalForbiddenRuleSrcPort = _Hh3cPortalForbiddenRuleSrcPort_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 99, 2, 9, 1, 11),
    _Hh3cPortalForbiddenRuleSrcPort_Type()
)
hh3cPortalForbiddenRuleSrcPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cPortalForbiddenRuleSrcPort.setStatus("current")
_Hh3cPortalForbiddenRuleDstPort_Type = Integer32
_Hh3cPortalForbiddenRuleDstPort_Object = MibTableColumn
hh3cPortalForbiddenRuleDstPort = _Hh3cPortalForbiddenRuleDstPort_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 99, 2, 9, 1, 12),
    _Hh3cPortalForbiddenRuleDstPort_Type()
)
hh3cPortalForbiddenRuleDstPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cPortalForbiddenRuleDstPort.setStatus("current")
_Hh3cPortalForbiddenRuleRowStatus_Type = RowStatus
_Hh3cPortalForbiddenRuleRowStatus_Object = MibTableColumn
hh3cPortalForbiddenRuleRowStatus = _Hh3cPortalForbiddenRuleRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 99, 2, 9, 1, 13),
    _Hh3cPortalForbiddenRuleRowStatus_Type()
)
hh3cPortalForbiddenRuleRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cPortalForbiddenRuleRowStatus.setStatus("current")


class _Hh3cPortalForbiddenRuleSsidName_Type(OctetString):
    """Custom type hh3cPortalForbiddenRuleSsidName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_Hh3cPortalForbiddenRuleSsidName_Type.__name__ = "OctetString"
_Hh3cPortalForbiddenRuleSsidName_Object = MibTableColumn
hh3cPortalForbiddenRuleSsidName = _Hh3cPortalForbiddenRuleSsidName_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 99, 2, 9, 1, 14),
    _Hh3cPortalForbiddenRuleSsidName_Type()
)
hh3cPortalForbiddenRuleSsidName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cPortalForbiddenRuleSsidName.setStatus("current")
_Hh3cPortalTraps_ObjectIdentity = ObjectIdentity
hh3cPortalTraps = _Hh3cPortalTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 99, 3)
)
_Hh3cPortalTrapPrefix_ObjectIdentity = ObjectIdentity
hh3cPortalTrapPrefix = _Hh3cPortalTrapPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 99, 3, 0)
)
_Hh3cPortalTrapVarObjects_ObjectIdentity = ObjectIdentity
hh3cPortalTrapVarObjects = _Hh3cPortalTrapVarObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 99, 3, 1)
)
_Hh3cPortalFirstTrapTime_Type = TimeTicks
_Hh3cPortalFirstTrapTime_Object = MibScalar
hh3cPortalFirstTrapTime = _Hh3cPortalFirstTrapTime_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 99, 3, 1, 1),
    _Hh3cPortalFirstTrapTime_Type()
)
hh3cPortalFirstTrapTime.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cPortalFirstTrapTime.setStatus("current")
_Hh3cPortalServerIP_Type = InetAddressIPv4
_Hh3cPortalServerIP_Object = MibScalar
hh3cPortalServerIP = _Hh3cPortalServerIP_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 99, 3, 1, 2),
    _Hh3cPortalServerIP_Type()
)
hh3cPortalServerIP.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cPortalServerIP.setStatus("current")
_Hh3cPortalStatistic_ObjectIdentity = ObjectIdentity
hh3cPortalStatistic = _Hh3cPortalStatistic_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 99, 4)
)
_Hh3cPortalStatAuthReq_Type = Counter64
_Hh3cPortalStatAuthReq_Object = MibScalar
hh3cPortalStatAuthReq = _Hh3cPortalStatAuthReq_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 99, 4, 1),
    _Hh3cPortalStatAuthReq_Type()
)
hh3cPortalStatAuthReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cPortalStatAuthReq.setStatus("current")
_Hh3cPortalStatAckLogout_Type = Counter64
_Hh3cPortalStatAckLogout_Object = MibScalar
hh3cPortalStatAckLogout = _Hh3cPortalStatAckLogout_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 99, 4, 2),
    _Hh3cPortalStatAckLogout_Type()
)
hh3cPortalStatAckLogout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cPortalStatAckLogout.setStatus("current")
_Hh3cPortalStatNotifyLogout_Type = Counter64
_Hh3cPortalStatNotifyLogout_Object = MibScalar
hh3cPortalStatNotifyLogout = _Hh3cPortalStatNotifyLogout_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 99, 4, 3),
    _Hh3cPortalStatNotifyLogout_Type()
)
hh3cPortalStatNotifyLogout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cPortalStatNotifyLogout.setStatus("current")
_Hh3cPortalStatChallengeTimeout_Type = Counter64
_Hh3cPortalStatChallengeTimeout_Object = MibScalar
hh3cPortalStatChallengeTimeout = _Hh3cPortalStatChallengeTimeout_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 99, 4, 4),
    _Hh3cPortalStatChallengeTimeout_Type()
)
hh3cPortalStatChallengeTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cPortalStatChallengeTimeout.setStatus("current")
_Hh3cPortalStatChallengeBusy_Type = Counter64
_Hh3cPortalStatChallengeBusy_Object = MibScalar
hh3cPortalStatChallengeBusy = _Hh3cPortalStatChallengeBusy_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 99, 4, 5),
    _Hh3cPortalStatChallengeBusy_Type()
)
hh3cPortalStatChallengeBusy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cPortalStatChallengeBusy.setStatus("current")
_Hh3cPortalStatChallengeFail_Type = Counter64
_Hh3cPortalStatChallengeFail_Object = MibScalar
hh3cPortalStatChallengeFail = _Hh3cPortalStatChallengeFail_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 99, 4, 6),
    _Hh3cPortalStatChallengeFail_Type()
)
hh3cPortalStatChallengeFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cPortalStatChallengeFail.setStatus("current")
_Hh3cPortalStatAuthTimeout_Type = Counter64
_Hh3cPortalStatAuthTimeout_Object = MibScalar
hh3cPortalStatAuthTimeout = _Hh3cPortalStatAuthTimeout_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 99, 4, 7),
    _Hh3cPortalStatAuthTimeout_Type()
)
hh3cPortalStatAuthTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cPortalStatAuthTimeout.setStatus("current")
_Hh3cPortalStatAuthFail_Type = Counter64
_Hh3cPortalStatAuthFail_Object = MibScalar
hh3cPortalStatAuthFail = _Hh3cPortalStatAuthFail_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 99, 4, 8),
    _Hh3cPortalStatAuthFail_Type()
)
hh3cPortalStatAuthFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cPortalStatAuthFail.setStatus("current")
_Hh3cPortalStatPwdError_Type = Counter64
_Hh3cPortalStatPwdError_Object = MibScalar
hh3cPortalStatPwdError = _Hh3cPortalStatPwdError_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 99, 4, 9),
    _Hh3cPortalStatPwdError_Type()
)
hh3cPortalStatPwdError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cPortalStatPwdError.setStatus("current")
_Hh3cPortalStatAuthBusy_Type = Counter64
_Hh3cPortalStatAuthBusy_Object = MibScalar
hh3cPortalStatAuthBusy = _Hh3cPortalStatAuthBusy_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 99, 4, 10),
    _Hh3cPortalStatAuthBusy_Type()
)
hh3cPortalStatAuthBusy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cPortalStatAuthBusy.setStatus("current")
_Hh3cPortalStatAuthDisordered_Type = Counter64
_Hh3cPortalStatAuthDisordered_Object = MibScalar
hh3cPortalStatAuthDisordered = _Hh3cPortalStatAuthDisordered_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 99, 4, 11),
    _Hh3cPortalStatAuthDisordered_Type()
)
hh3cPortalStatAuthDisordered.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cPortalStatAuthDisordered.setStatus("current")
_Hh3cPortalStatAuthUnknownError_Type = Counter64
_Hh3cPortalStatAuthUnknownError_Object = MibScalar
hh3cPortalStatAuthUnknownError = _Hh3cPortalStatAuthUnknownError_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 99, 4, 12),
    _Hh3cPortalStatAuthUnknownError_Type()
)
hh3cPortalStatAuthUnknownError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cPortalStatAuthUnknownError.setStatus("current")
_Hh3cPortalStatAuthResp_Type = Counter64
_Hh3cPortalStatAuthResp_Object = MibScalar
hh3cPortalStatAuthResp = _Hh3cPortalStatAuthResp_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 99, 4, 13),
    _Hh3cPortalStatAuthResp_Type()
)
hh3cPortalStatAuthResp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cPortalStatAuthResp.setStatus("current")
_Hh3cPortalStatChallengeReq_Type = Counter64
_Hh3cPortalStatChallengeReq_Object = MibScalar
hh3cPortalStatChallengeReq = _Hh3cPortalStatChallengeReq_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 99, 4, 14),
    _Hh3cPortalStatChallengeReq_Type()
)
hh3cPortalStatChallengeReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cPortalStatChallengeReq.setStatus("current")
_Hh3cPortalStatChallengeResp_Type = Counter64
_Hh3cPortalStatChallengeResp_Object = MibScalar
hh3cPortalStatChallengeResp = _Hh3cPortalStatChallengeResp_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 99, 4, 15),
    _Hh3cPortalStatChallengeResp_Type()
)
hh3cPortalStatChallengeResp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cPortalStatChallengeResp.setStatus("current")
_Hh3cPortalStatHttpReq_Type = Counter64
_Hh3cPortalStatHttpReq_Object = MibScalar
hh3cPortalStatHttpReq = _Hh3cPortalStatHttpReq_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 99, 4, 16),
    _Hh3cPortalStatHttpReq_Type()
)
hh3cPortalStatHttpReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cPortalStatHttpReq.setStatus("current")
_Hh3cPortalStatHttpResp_Type = Counter64
_Hh3cPortalStatHttpResp_Object = MibScalar
hh3cPortalStatHttpResp = _Hh3cPortalStatHttpResp_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 99, 4, 17),
    _Hh3cPortalStatHttpResp_Type()
)
hh3cPortalStatHttpResp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cPortalStatHttpResp.setStatus("current")
_Hh3cPortalStatHttpsReq_Type = Counter64
_Hh3cPortalStatHttpsReq_Object = MibScalar
hh3cPortalStatHttpsReq = _Hh3cPortalStatHttpsReq_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 99, 4, 18),
    _Hh3cPortalStatHttpsReq_Type()
)
hh3cPortalStatHttpsReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cPortalStatHttpsReq.setStatus("current")
_Hh3cPortalStatHttpsResp_Type = Counter64
_Hh3cPortalStatHttpsResp_Object = MibScalar
hh3cPortalStatHttpsResp = _Hh3cPortalStatHttpsResp_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 99, 4, 19),
    _Hh3cPortalStatHttpsResp_Type()
)
hh3cPortalStatHttpsResp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cPortalStatHttpsResp.setStatus("current")
_Hh3cPortalPktStatistic_ObjectIdentity = ObjectIdentity
hh3cPortalPktStatistic = _Hh3cPortalPktStatistic_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 99, 5)
)
_Hh3cPortalPktStaReqAuthNum_Type = Counter64
_Hh3cPortalPktStaReqAuthNum_Object = MibScalar
hh3cPortalPktStaReqAuthNum = _Hh3cPortalPktStaReqAuthNum_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 99, 5, 1),
    _Hh3cPortalPktStaReqAuthNum_Type()
)
hh3cPortalPktStaReqAuthNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cPortalPktStaReqAuthNum.setStatus("current")
_Hh3cPortalPktStaAckAuthSuccess_Type = Counter64
_Hh3cPortalPktStaAckAuthSuccess_Object = MibScalar
hh3cPortalPktStaAckAuthSuccess = _Hh3cPortalPktStaAckAuthSuccess_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 99, 5, 2),
    _Hh3cPortalPktStaAckAuthSuccess_Type()
)
hh3cPortalPktStaAckAuthSuccess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cPortalPktStaAckAuthSuccess.setStatus("current")
_Hh3cPortalPktStaAckAuthReject_Type = Counter64
_Hh3cPortalPktStaAckAuthReject_Object = MibScalar
hh3cPortalPktStaAckAuthReject = _Hh3cPortalPktStaAckAuthReject_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 99, 5, 3),
    _Hh3cPortalPktStaAckAuthReject_Type()
)
hh3cPortalPktStaAckAuthReject.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cPortalPktStaAckAuthReject.setStatus("current")
_Hh3cPortalPktStaAckAuthEstablish_Type = Counter64
_Hh3cPortalPktStaAckAuthEstablish_Object = MibScalar
hh3cPortalPktStaAckAuthEstablish = _Hh3cPortalPktStaAckAuthEstablish_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 99, 5, 4),
    _Hh3cPortalPktStaAckAuthEstablish_Type()
)
hh3cPortalPktStaAckAuthEstablish.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cPortalPktStaAckAuthEstablish.setStatus("current")
_Hh3cPortalPktStaAckAuthBusy_Type = Counter64
_Hh3cPortalPktStaAckAuthBusy_Object = MibScalar
hh3cPortalPktStaAckAuthBusy = _Hh3cPortalPktStaAckAuthBusy_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 99, 5, 5),
    _Hh3cPortalPktStaAckAuthBusy_Type()
)
hh3cPortalPktStaAckAuthBusy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cPortalPktStaAckAuthBusy.setStatus("current")
_Hh3cPortalPktStaAckAuthAuthFail_Type = Counter64
_Hh3cPortalPktStaAckAuthAuthFail_Object = MibScalar
hh3cPortalPktStaAckAuthAuthFail = _Hh3cPortalPktStaAckAuthAuthFail_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 99, 5, 6),
    _Hh3cPortalPktStaAckAuthAuthFail_Type()
)
hh3cPortalPktStaAckAuthAuthFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cPortalPktStaAckAuthAuthFail.setStatus("current")
_Hh3cPortalPktStaReqChallengeNum_Type = Counter64
_Hh3cPortalPktStaReqChallengeNum_Object = MibScalar
hh3cPortalPktStaReqChallengeNum = _Hh3cPortalPktStaReqChallengeNum_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 99, 5, 7),
    _Hh3cPortalPktStaReqChallengeNum_Type()
)
hh3cPortalPktStaReqChallengeNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cPortalPktStaReqChallengeNum.setStatus("current")
_Hh3cPortalPktStaAckChallengeSuccess_Type = Counter64
_Hh3cPortalPktStaAckChallengeSuccess_Object = MibScalar
hh3cPortalPktStaAckChallengeSuccess = _Hh3cPortalPktStaAckChallengeSuccess_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 99, 5, 8),
    _Hh3cPortalPktStaAckChallengeSuccess_Type()
)
hh3cPortalPktStaAckChallengeSuccess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cPortalPktStaAckChallengeSuccess.setStatus("current")
_Hh3cPortalPktStaAckChallengeReject_Type = Counter64
_Hh3cPortalPktStaAckChallengeReject_Object = MibScalar
hh3cPortalPktStaAckChallengeReject = _Hh3cPortalPktStaAckChallengeReject_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 99, 5, 9),
    _Hh3cPortalPktStaAckChallengeReject_Type()
)
hh3cPortalPktStaAckChallengeReject.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cPortalPktStaAckChallengeReject.setStatus("current")
_Hh3cPortalPktStaAckChallengeEstablish_Type = Counter64
_Hh3cPortalPktStaAckChallengeEstablish_Object = MibScalar
hh3cPortalPktStaAckChallengeEstablish = _Hh3cPortalPktStaAckChallengeEstablish_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 99, 5, 10),
    _Hh3cPortalPktStaAckChallengeEstablish_Type()
)
hh3cPortalPktStaAckChallengeEstablish.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cPortalPktStaAckChallengeEstablish.setStatus("current")
_Hh3cPortalPktStaAckChallengeBusy_Type = Counter64
_Hh3cPortalPktStaAckChallengeBusy_Object = MibScalar
hh3cPortalPktStaAckChallengeBusy = _Hh3cPortalPktStaAckChallengeBusy_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 99, 5, 11),
    _Hh3cPortalPktStaAckChallengeBusy_Type()
)
hh3cPortalPktStaAckChallengeBusy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cPortalPktStaAckChallengeBusy.setStatus("current")
_Hh3cPortalPktStaAckChallengeAuthFail_Type = Counter64
_Hh3cPortalPktStaAckChallengeAuthFail_Object = MibScalar
hh3cPortalPktStaAckChallengeAuthFail = _Hh3cPortalPktStaAckChallengeAuthFail_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 99, 5, 12),
    _Hh3cPortalPktStaAckChallengeAuthFail_Type()
)
hh3cPortalPktStaAckChallengeAuthFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cPortalPktStaAckChallengeAuthFail.setStatus("current")
_Hh3cPortalExtConfig_ObjectIdentity = ObjectIdentity
hh3cPortalExtConfig = _Hh3cPortalExtConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 99, 6)
)
_Hh3cPortalExtMaxUserNumber_Type = Unsigned32
_Hh3cPortalExtMaxUserNumber_Object = MibScalar
hh3cPortalExtMaxUserNumber = _Hh3cPortalExtMaxUserNumber_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 99, 6, 1),
    _Hh3cPortalExtMaxUserNumber_Type()
)
hh3cPortalExtMaxUserNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cPortalExtMaxUserNumber.setStatus("current")
_Hh3cPortalExtCurrentUserNumber_Type = Unsigned32
_Hh3cPortalExtCurrentUserNumber_Object = MibScalar
hh3cPortalExtCurrentUserNumber = _Hh3cPortalExtCurrentUserNumber_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 99, 6, 2),
    _Hh3cPortalExtCurrentUserNumber_Type()
)
hh3cPortalExtCurrentUserNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cPortalExtCurrentUserNumber.setStatus("current")


class _Hh3cPortalExtStatus_Type(Integer32):
    """Custom type hh3cPortalExtStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enabled", 1),
          ("disabled", 2))
    )


_Hh3cPortalExtStatus_Type.__name__ = "Integer32"
_Hh3cPortalExtStatus_Object = MibScalar
hh3cPortalExtStatus = _Hh3cPortalExtStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 99, 6, 3),
    _Hh3cPortalExtStatus_Type()
)
hh3cPortalExtStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cPortalExtStatus.setStatus("current")
_Hh3cPortalExtTables_ObjectIdentity = ObjectIdentity
hh3cPortalExtTables = _Hh3cPortalExtTables_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 99, 7)
)
_Hh3cPortalExtSrvTable_Object = MibTable
hh3cPortalExtSrvTable = _Hh3cPortalExtSrvTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 99, 7, 1)
)
if mibBuilder.loadTexts:
    hh3cPortalExtSrvTable.setStatus("current")
_Hh3cPortalExtSrvEntry_Object = MibTableRow
hh3cPortalExtSrvEntry = _Hh3cPortalExtSrvEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 99, 7, 1, 1)
)
hh3cPortalExtSrvEntry.setIndexNames(
    (0, "HH3C-PORTAL-MIB", "hh3cPortalExtSrvName"),
)
if mibBuilder.loadTexts:
    hh3cPortalExtSrvEntry.setStatus("current")


class _Hh3cPortalExtSrvName_Type(OctetString):
    """Custom type hh3cPortalExtSrvName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_Hh3cPortalExtSrvName_Type.__name__ = "OctetString"
_Hh3cPortalExtSrvName_Object = MibTableColumn
hh3cPortalExtSrvName = _Hh3cPortalExtSrvName_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 99, 7, 1, 1, 1),
    _Hh3cPortalExtSrvName_Type()
)
hh3cPortalExtSrvName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cPortalExtSrvName.setStatus("current")
_Hh3cPortalExtSrvIPAddrType_Type = InetAddressType
_Hh3cPortalExtSrvIPAddrType_Object = MibTableColumn
hh3cPortalExtSrvIPAddrType = _Hh3cPortalExtSrvIPAddrType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 99, 7, 1, 1, 2),
    _Hh3cPortalExtSrvIPAddrType_Type()
)
hh3cPortalExtSrvIPAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cPortalExtSrvIPAddrType.setStatus("current")
_Hh3cPortalExtSrvIP_Type = InetAddress
_Hh3cPortalExtSrvIP_Object = MibTableColumn
hh3cPortalExtSrvIP = _Hh3cPortalExtSrvIP_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 99, 7, 1, 1, 3),
    _Hh3cPortalExtSrvIP_Type()
)
hh3cPortalExtSrvIP.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cPortalExtSrvIP.setStatus("current")
_Hh3cPortalExtSrvPort_Type = Integer32
_Hh3cPortalExtSrvPort_Object = MibTableColumn
hh3cPortalExtSrvPort = _Hh3cPortalExtSrvPort_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 99, 7, 1, 1, 4),
    _Hh3cPortalExtSrvPort_Type()
)
hh3cPortalExtSrvPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cPortalExtSrvPort.setStatus("current")
_Hh3cPortalExtSrvRowStatus_Type = RowStatus
_Hh3cPortalExtSrvRowStatus_Object = MibTableColumn
hh3cPortalExtSrvRowStatus = _Hh3cPortalExtSrvRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 99, 7, 1, 1, 5),
    _Hh3cPortalExtSrvRowStatus_Type()
)
hh3cPortalExtSrvRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cPortalExtSrvRowStatus.setStatus("current")
_Hh3cPortalExtWebSrvTable_Object = MibTable
hh3cPortalExtWebSrvTable = _Hh3cPortalExtWebSrvTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 99, 7, 2)
)
if mibBuilder.loadTexts:
    hh3cPortalExtWebSrvTable.setStatus("current")
_Hh3cPortalExtWebSrvEntry_Object = MibTableRow
hh3cPortalExtWebSrvEntry = _Hh3cPortalExtWebSrvEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 99, 7, 2, 1)
)
hh3cPortalExtWebSrvEntry.setIndexNames(
    (0, "HH3C-PORTAL-MIB", "hh3cPortalExtWebSrvName"),
)
if mibBuilder.loadTexts:
    hh3cPortalExtWebSrvEntry.setStatus("current")


class _Hh3cPortalExtWebSrvName_Type(OctetString):
    """Custom type hh3cPortalExtWebSrvName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_Hh3cPortalExtWebSrvName_Type.__name__ = "OctetString"
_Hh3cPortalExtWebSrvName_Object = MibTableColumn
hh3cPortalExtWebSrvName = _Hh3cPortalExtWebSrvName_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 99, 7, 2, 1, 1),
    _Hh3cPortalExtWebSrvName_Type()
)
hh3cPortalExtWebSrvName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cPortalExtWebSrvName.setStatus("current")
_Hh3cPortalExtWebSrvUrl_Type = OctetString
_Hh3cPortalExtWebSrvUrl_Object = MibTableColumn
hh3cPortalExtWebSrvUrl = _Hh3cPortalExtWebSrvUrl_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 99, 7, 2, 1, 2),
    _Hh3cPortalExtWebSrvUrl_Type()
)
hh3cPortalExtWebSrvUrl.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cPortalExtWebSrvUrl.setStatus("current")
_Hh3cPortalExtWebSrvRowStatus_Type = RowStatus
_Hh3cPortalExtWebSrvRowStatus_Object = MibTableColumn
hh3cPortalExtWebSrvRowStatus = _Hh3cPortalExtWebSrvRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 99, 7, 2, 1, 3),
    _Hh3cPortalExtWebSrvRowStatus_Type()
)
hh3cPortalExtWebSrvRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cPortalExtWebSrvRowStatus.setStatus("current")
_Hh3cPortalExtMTSrvTable_Object = MibTable
hh3cPortalExtMTSrvTable = _Hh3cPortalExtMTSrvTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 99, 7, 3)
)
if mibBuilder.loadTexts:
    hh3cPortalExtMTSrvTable.setStatus("current")
_Hh3cPortalExtMTSrvEntry_Object = MibTableRow
hh3cPortalExtMTSrvEntry = _Hh3cPortalExtMTSrvEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 99, 7, 3, 1)
)
hh3cPortalExtMTSrvEntry.setIndexNames(
    (0, "HH3C-PORTAL-MIB", "hh3cPortalExtMTSrvName"),
)
if mibBuilder.loadTexts:
    hh3cPortalExtMTSrvEntry.setStatus("current")


class _Hh3cPortalExtMTSrvName_Type(OctetString):
    """Custom type hh3cPortalExtMTSrvName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_Hh3cPortalExtMTSrvName_Type.__name__ = "OctetString"
_Hh3cPortalExtMTSrvName_Object = MibTableColumn
hh3cPortalExtMTSrvName = _Hh3cPortalExtMTSrvName_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 99, 7, 3, 1, 1),
    _Hh3cPortalExtMTSrvName_Type()
)
hh3cPortalExtMTSrvName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cPortalExtMTSrvName.setStatus("current")
_Hh3cPortalExtMTSrvIPAddrType_Type = InetAddressType
_Hh3cPortalExtMTSrvIPAddrType_Object = MibTableColumn
hh3cPortalExtMTSrvIPAddrType = _Hh3cPortalExtMTSrvIPAddrType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 99, 7, 3, 1, 2),
    _Hh3cPortalExtMTSrvIPAddrType_Type()
)
hh3cPortalExtMTSrvIPAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cPortalExtMTSrvIPAddrType.setStatus("current")
_Hh3cPortalExtMTSrvIP_Type = InetAddress
_Hh3cPortalExtMTSrvIP_Object = MibTableColumn
hh3cPortalExtMTSrvIP = _Hh3cPortalExtMTSrvIP_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 99, 7, 3, 1, 3),
    _Hh3cPortalExtMTSrvIP_Type()
)
hh3cPortalExtMTSrvIP.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cPortalExtMTSrvIP.setStatus("current")


class _Hh3cPortalExtMTSrvPort_Type(Integer32):
    """Custom type hh3cPortalExtMTSrvPort based on Integer32"""
    defaultValue = 50100


_Hh3cPortalExtMTSrvPort_Type.__name__ = "Integer32"
_Hh3cPortalExtMTSrvPort_Object = MibTableColumn
hh3cPortalExtMTSrvPort = _Hh3cPortalExtMTSrvPort_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 99, 7, 3, 1, 4),
    _Hh3cPortalExtMTSrvPort_Type()
)
hh3cPortalExtMTSrvPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cPortalExtMTSrvPort.setStatus("current")


class _Hh3cPortalExtMTDetctFlowPeriod_Type(Integer32):
    """Custom type hh3cPortalExtMTDetctFlowPeriod based on Integer32"""
    defaultValue = 300


_Hh3cPortalExtMTDetctFlowPeriod_Type.__name__ = "Integer32"
_Hh3cPortalExtMTDetctFlowPeriod_Object = MibTableColumn
hh3cPortalExtMTDetctFlowPeriod = _Hh3cPortalExtMTDetctFlowPeriod_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 99, 7, 3, 1, 5),
    _Hh3cPortalExtMTDetctFlowPeriod_Type()
)
hh3cPortalExtMTDetctFlowPeriod.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cPortalExtMTDetctFlowPeriod.setStatus("current")
if mibBuilder.loadTexts:
    hh3cPortalExtMTDetctFlowPeriod.setUnits("seconds")


class _Hh3cPortalExtMTThresholdFlow_Type(Unsigned32):
    """Custom type hh3cPortalExtMTThresholdFlow based on Unsigned32"""
    defaultValue = 0


_Hh3cPortalExtMTThresholdFlow_Type.__name__ = "Unsigned32"
_Hh3cPortalExtMTThresholdFlow_Object = MibTableColumn
hh3cPortalExtMTThresholdFlow = _Hh3cPortalExtMTThresholdFlow_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 99, 7, 3, 1, 6),
    _Hh3cPortalExtMTThresholdFlow_Type()
)
hh3cPortalExtMTThresholdFlow.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cPortalExtMTThresholdFlow.setStatus("current")
if mibBuilder.loadTexts:
    hh3cPortalExtMTThresholdFlow.setUnits("bytes")
_Hh3cPortalExtMTSrvRowStatus_Type = RowStatus
_Hh3cPortalExtMTSrvRowStatus_Object = MibTableColumn
hh3cPortalExtMTSrvRowStatus = _Hh3cPortalExtMTSrvRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 99, 7, 3, 1, 7),
    _Hh3cPortalExtMTSrvRowStatus_Type()
)
hh3cPortalExtMTSrvRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cPortalExtMTSrvRowStatus.setStatus("current")
_Hh3cPortalExtIfConfigTable_Object = MibTable
hh3cPortalExtIfConfigTable = _Hh3cPortalExtIfConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 99, 7, 4)
)
if mibBuilder.loadTexts:
    hh3cPortalExtIfConfigTable.setStatus("current")
_Hh3cPortalExtIfConfigEntry_Object = MibTableRow
hh3cPortalExtIfConfigEntry = _Hh3cPortalExtIfConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 99, 7, 4, 1)
)
hh3cPortalExtIfConfigEntry.setIndexNames(
    (0, "HH3C-PORTAL-MIB", "hh3cPortalExtIfIndex"),
)
if mibBuilder.loadTexts:
    hh3cPortalExtIfConfigEntry.setStatus("current")
_Hh3cPortalExtIfIndex_Type = InterfaceIndex
_Hh3cPortalExtIfIndex_Object = MibTableColumn
hh3cPortalExtIfIndex = _Hh3cPortalExtIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 99, 7, 4, 1, 1),
    _Hh3cPortalExtIfIndex_Type()
)
hh3cPortalExtIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cPortalExtIfIndex.setStatus("current")
_Hh3cPortalExtIfWebSrvName_Type = OctetString
_Hh3cPortalExtIfWebSrvName_Object = MibTableColumn
hh3cPortalExtIfWebSrvName = _Hh3cPortalExtIfWebSrvName_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 99, 7, 4, 1, 2),
    _Hh3cPortalExtIfWebSrvName_Type()
)
hh3cPortalExtIfWebSrvName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cPortalExtIfWebSrvName.setStatus("current")
_Hh3cPortalExtIfDomainName_Type = OctetString
_Hh3cPortalExtIfDomainName_Object = MibTableColumn
hh3cPortalExtIfDomainName = _Hh3cPortalExtIfDomainName_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 99, 7, 4, 1, 3),
    _Hh3cPortalExtIfDomainName_Type()
)
hh3cPortalExtIfDomainName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cPortalExtIfDomainName.setStatus("current")
_Hh3cPortalExtIfAuthMethod_Type = Hh3cPortalAuthMethod
_Hh3cPortalExtIfAuthMethod_Object = MibTableColumn
hh3cPortalExtIfAuthMethod = _Hh3cPortalExtIfAuthMethod_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 99, 7, 4, 1, 4),
    _Hh3cPortalExtIfAuthMethod_Type()
)
hh3cPortalExtIfAuthMethod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cPortalExtIfAuthMethod.setStatus("current")
_Hh3cPortalExtIfMTSrvName_Type = OctetString
_Hh3cPortalExtIfMTSrvName_Object = MibTableColumn
hh3cPortalExtIfMTSrvName = _Hh3cPortalExtIfMTSrvName_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 99, 7, 4, 1, 5),
    _Hh3cPortalExtIfMTSrvName_Type()
)
hh3cPortalExtIfMTSrvName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cPortalExtIfMTSrvName.setStatus("current")
_Hh3cPortalExtIfMaxUser_Type = Unsigned32
_Hh3cPortalExtIfMaxUser_Object = MibTableColumn
hh3cPortalExtIfMaxUser = _Hh3cPortalExtIfMaxUser_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 99, 7, 4, 1, 6),
    _Hh3cPortalExtIfMaxUser_Type()
)
hh3cPortalExtIfMaxUser.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cPortalExtIfMaxUser.setStatus("current")
_Hh3cPortalExtIfIpv6ConfigTable_Object = MibTable
hh3cPortalExtIfIpv6ConfigTable = _Hh3cPortalExtIfIpv6ConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 99, 7, 5)
)
if mibBuilder.loadTexts:
    hh3cPortalExtIfIpv6ConfigTable.setStatus("current")
_Hh3cPortalExtIfIpv6ConfigEntry_Object = MibTableRow
hh3cPortalExtIfIpv6ConfigEntry = _Hh3cPortalExtIfIpv6ConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 99, 7, 5, 1)
)
hh3cPortalExtIfIpv6ConfigEntry.setIndexNames(
    (0, "HH3C-PORTAL-MIB", "hh3cPortalExtIfIpv6Index"),
)
if mibBuilder.loadTexts:
    hh3cPortalExtIfIpv6ConfigEntry.setStatus("current")
_Hh3cPortalExtIfIpv6Index_Type = InterfaceIndex
_Hh3cPortalExtIfIpv6Index_Object = MibTableColumn
hh3cPortalExtIfIpv6Index = _Hh3cPortalExtIfIpv6Index_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 99, 7, 5, 1, 1),
    _Hh3cPortalExtIfIpv6Index_Type()
)
hh3cPortalExtIfIpv6Index.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cPortalExtIfIpv6Index.setStatus("current")
_Hh3cPortalExtIfIpv6WebSrvName_Type = OctetString
_Hh3cPortalExtIfIpv6WebSrvName_Object = MibTableColumn
hh3cPortalExtIfIpv6WebSrvName = _Hh3cPortalExtIfIpv6WebSrvName_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 99, 7, 5, 1, 2),
    _Hh3cPortalExtIfIpv6WebSrvName_Type()
)
hh3cPortalExtIfIpv6WebSrvName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cPortalExtIfIpv6WebSrvName.setStatus("current")
_Hh3cPortalExtIfIpv6DomainName_Type = OctetString
_Hh3cPortalExtIfIpv6DomainName_Object = MibTableColumn
hh3cPortalExtIfIpv6DomainName = _Hh3cPortalExtIfIpv6DomainName_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 99, 7, 5, 1, 3),
    _Hh3cPortalExtIfIpv6DomainName_Type()
)
hh3cPortalExtIfIpv6DomainName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cPortalExtIfIpv6DomainName.setStatus("current")
_Hh3cPortalExtIfIpv6AuthMethod_Type = Hh3cPortalAuthMethod
_Hh3cPortalExtIfIpv6AuthMethod_Object = MibTableColumn
hh3cPortalExtIfIpv6AuthMethod = _Hh3cPortalExtIfIpv6AuthMethod_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 99, 7, 5, 1, 4),
    _Hh3cPortalExtIfIpv6AuthMethod_Type()
)
hh3cPortalExtIfIpv6AuthMethod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cPortalExtIfIpv6AuthMethod.setStatus("current")
_Hh3cPortalExtIfIpv6MaxUser_Type = Unsigned32
_Hh3cPortalExtIfIpv6MaxUser_Object = MibTableColumn
hh3cPortalExtIfIpv6MaxUser = _Hh3cPortalExtIfIpv6MaxUser_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 99, 7, 5, 1, 5),
    _Hh3cPortalExtIfIpv6MaxUser_Type()
)
hh3cPortalExtIfIpv6MaxUser.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cPortalExtIfIpv6MaxUser.setStatus("current")
_Hh3cPortalDot11SrvTable_Object = MibTable
hh3cPortalDot11SrvTable = _Hh3cPortalDot11SrvTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 99, 7, 6)
)
if mibBuilder.loadTexts:
    hh3cPortalDot11SrvTable.setStatus("current")
_Hh3cPortalDot11SrvEntry_Object = MibTableRow
hh3cPortalDot11SrvEntry = _Hh3cPortalDot11SrvEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 99, 7, 6, 1)
)
hh3cPortalDot11SrvEntry.setIndexNames(
    (0, "HH3C-PORTAL-MIB", "hh3cPortalDot11SrvTemName"),
)
if mibBuilder.loadTexts:
    hh3cPortalDot11SrvEntry.setStatus("current")


class _Hh3cPortalDot11SrvTemName_Type(OctetString):
    """Custom type hh3cPortalDot11SrvTemName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 63),
    )


_Hh3cPortalDot11SrvTemName_Type.__name__ = "OctetString"
_Hh3cPortalDot11SrvTemName_Object = MibTableColumn
hh3cPortalDot11SrvTemName = _Hh3cPortalDot11SrvTemName_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 99, 7, 6, 1, 1),
    _Hh3cPortalDot11SrvTemName_Type()
)
hh3cPortalDot11SrvTemName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cPortalDot11SrvTemName.setStatus("current")
_Hh3cPortalDot11WebSrvName_Type = OctetString
_Hh3cPortalDot11WebSrvName_Object = MibTableColumn
hh3cPortalDot11WebSrvName = _Hh3cPortalDot11WebSrvName_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 99, 7, 6, 1, 2),
    _Hh3cPortalDot11WebSrvName_Type()
)
hh3cPortalDot11WebSrvName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cPortalDot11WebSrvName.setStatus("current")
_Hh3cPortalDot11DomainName_Type = OctetString
_Hh3cPortalDot11DomainName_Object = MibTableColumn
hh3cPortalDot11DomainName = _Hh3cPortalDot11DomainName_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 99, 7, 6, 1, 3),
    _Hh3cPortalDot11DomainName_Type()
)
hh3cPortalDot11DomainName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cPortalDot11DomainName.setStatus("current")
_Hh3cPortalDot11AuthMethod_Type = Hh3cPortalAuthMethod
_Hh3cPortalDot11AuthMethod_Object = MibTableColumn
hh3cPortalDot11AuthMethod = _Hh3cPortalDot11AuthMethod_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 99, 7, 6, 1, 4),
    _Hh3cPortalDot11AuthMethod_Type()
)
hh3cPortalDot11AuthMethod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cPortalDot11AuthMethod.setStatus("current")
_Hh3cPortalDot11MTSrvName_Type = OctetString
_Hh3cPortalDot11MTSrvName_Object = MibTableColumn
hh3cPortalDot11MTSrvName = _Hh3cPortalDot11MTSrvName_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 99, 7, 6, 1, 5),
    _Hh3cPortalDot11MTSrvName_Type()
)
hh3cPortalDot11MTSrvName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cPortalDot11MTSrvName.setStatus("current")
_Hh3cPortalDot11MaxUser_Type = Unsigned32
_Hh3cPortalDot11MaxUser_Object = MibTableColumn
hh3cPortalDot11MaxUser = _Hh3cPortalDot11MaxUser_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 99, 7, 6, 1, 6),
    _Hh3cPortalDot11MaxUser_Type()
)
hh3cPortalDot11MaxUser.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cPortalDot11MaxUser.setStatus("current")
_Hh3cPortalDot11Ipv6SrvTable_Object = MibTable
hh3cPortalDot11Ipv6SrvTable = _Hh3cPortalDot11Ipv6SrvTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 99, 7, 7)
)
if mibBuilder.loadTexts:
    hh3cPortalDot11Ipv6SrvTable.setStatus("current")
_Hh3cPortalDot11Ipv6SrvEntry_Object = MibTableRow
hh3cPortalDot11Ipv6SrvEntry = _Hh3cPortalDot11Ipv6SrvEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 99, 7, 7, 1)
)
hh3cPortalDot11Ipv6SrvEntry.setIndexNames(
    (0, "HH3C-PORTAL-MIB", "hh3cPortalDot11Ipv6SrvTemName"),
)
if mibBuilder.loadTexts:
    hh3cPortalDot11Ipv6SrvEntry.setStatus("current")


class _Hh3cPortalDot11Ipv6SrvTemName_Type(OctetString):
    """Custom type hh3cPortalDot11Ipv6SrvTemName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 63),
    )


_Hh3cPortalDot11Ipv6SrvTemName_Type.__name__ = "OctetString"
_Hh3cPortalDot11Ipv6SrvTemName_Object = MibTableColumn
hh3cPortalDot11Ipv6SrvTemName = _Hh3cPortalDot11Ipv6SrvTemName_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 99, 7, 7, 1, 1),
    _Hh3cPortalDot11Ipv6SrvTemName_Type()
)
hh3cPortalDot11Ipv6SrvTemName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cPortalDot11Ipv6SrvTemName.setStatus("current")
_Hh3cPortalDot11Ipv6WebSrvName_Type = OctetString
_Hh3cPortalDot11Ipv6WebSrvName_Object = MibTableColumn
hh3cPortalDot11Ipv6WebSrvName = _Hh3cPortalDot11Ipv6WebSrvName_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 99, 7, 7, 1, 2),
    _Hh3cPortalDot11Ipv6WebSrvName_Type()
)
hh3cPortalDot11Ipv6WebSrvName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cPortalDot11Ipv6WebSrvName.setStatus("current")
_Hh3cPortalDot11Ipv6DomainName_Type = OctetString
_Hh3cPortalDot11Ipv6DomainName_Object = MibTableColumn
hh3cPortalDot11Ipv6DomainName = _Hh3cPortalDot11Ipv6DomainName_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 99, 7, 7, 1, 3),
    _Hh3cPortalDot11Ipv6DomainName_Type()
)
hh3cPortalDot11Ipv6DomainName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cPortalDot11Ipv6DomainName.setStatus("current")
_Hh3cPortalDot11Ipv6AuthMethod_Type = Hh3cPortalAuthMethod
_Hh3cPortalDot11Ipv6AuthMethod_Object = MibTableColumn
hh3cPortalDot11Ipv6AuthMethod = _Hh3cPortalDot11Ipv6AuthMethod_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 99, 7, 7, 1, 4),
    _Hh3cPortalDot11Ipv6AuthMethod_Type()
)
hh3cPortalDot11Ipv6AuthMethod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cPortalDot11Ipv6AuthMethod.setStatus("current")
_Hh3cPortalDot11Ipv6MaxUser_Type = Unsigned32
_Hh3cPortalDot11Ipv6MaxUser_Object = MibTableColumn
hh3cPortalDot11Ipv6MaxUser = _Hh3cPortalDot11Ipv6MaxUser_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 99, 7, 7, 1, 5),
    _Hh3cPortalDot11Ipv6MaxUser_Type()
)
hh3cPortalDot11Ipv6MaxUser.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cPortalDot11Ipv6MaxUser.setStatus("current")

# Managed Objects groups


# Notification objects

hh3cPortalServerLost = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 99, 3, 0, 1)
)
hh3cPortalServerLost.setObjects(
      *(("HH3C-PORTAL-MIB", "hh3cPortalServerName"),
        ("HH3C-PORTAL-MIB", "hh3cPortalFirstTrapTime"),
        ("HH3C-PORTAL-MIB", "hh3cPortalServerIP"),
        ("HH3C-PORTAL-MIB", "hh3cPortalServerPort"))
)
if mibBuilder.loadTexts:
    hh3cPortalServerLost.setStatus(
        "current"
    )

hh3cPortalServerGet = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 99, 3, 0, 2)
)
hh3cPortalServerGet.setObjects(
      *(("HH3C-PORTAL-MIB", "hh3cPortalServerName"),
        ("HH3C-PORTAL-MIB", "hh3cPortalFirstTrapTime"),
        ("HH3C-PORTAL-MIB", "hh3cPortalServerIP"),
        ("HH3C-PORTAL-MIB", "hh3cPortalServerPort"))
)
if mibBuilder.loadTexts:
    hh3cPortalServerGet.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HH3C-PORTAL-MIB",
    **{"Hh3cPortalAuthMethod": Hh3cPortalAuthMethod,
       "hh3cPortal": hh3cPortal,
       "hh3cPortalConfig": hh3cPortalConfig,
       "hh3cPortalMaxUserNumber": hh3cPortalMaxUserNumber,
       "hh3cPortalCurrentUserNumber": hh3cPortalCurrentUserNumber,
       "hh3cPortalStatus": hh3cPortalStatus,
       "hh3cPortalUserNumberUpperLimit": hh3cPortalUserNumberUpperLimit,
       "hh3cPortalNasId": hh3cPortalNasId,
       "hh3cPortalTables": hh3cPortalTables,
       "hh3cPortalServerTable": hh3cPortalServerTable,
       "hh3cPortalServerEntry": hh3cPortalServerEntry,
       "hh3cPortalServerName": hh3cPortalServerName,
       "hh3cPortalServerUrl": hh3cPortalServerUrl,
       "hh3cPortalServerPort": hh3cPortalServerPort,
       "hh3cPortalIfInfoTable": hh3cPortalIfInfoTable,
       "hh3cPortalIfInfoEntry": hh3cPortalIfInfoEntry,
       "hh3cPortalAuthReqNumber": hh3cPortalAuthReqNumber,
       "hh3cPortalAuthSuccNumber": hh3cPortalAuthSuccNumber,
       "hh3cPortalAuthFailNumber": hh3cPortalAuthFailNumber,
       "hh3cPortalIfServerTable": hh3cPortalIfServerTable,
       "hh3cPortalIfServerEntry": hh3cPortalIfServerEntry,
       "hh3cPortalIfServerIndex": hh3cPortalIfServerIndex,
       "hh3cPortalIfServerUrl": hh3cPortalIfServerUrl,
       "hh3cPortalIfServerRowStatus": hh3cPortalIfServerRowStatus,
       "hh3cPortalIfVlanNasIDTable": hh3cPortalIfVlanNasIDTable,
       "hh3cPortalIfVlanNasIDEntry": hh3cPortalIfVlanNasIDEntry,
       "hh3cPortalIfVlanNasIDIfIndex": hh3cPortalIfVlanNasIDIfIndex,
       "hh3cPortalIfVlanNasIDVlanID": hh3cPortalIfVlanNasIDVlanID,
       "hh3cPortalIfVlanNasIDNasID": hh3cPortalIfVlanNasIDNasID,
       "hh3cPortalSSIDFreeRuleTable": hh3cPortalSSIDFreeRuleTable,
       "hh3cPortalSSIDFreeRuleEntry": hh3cPortalSSIDFreeRuleEntry,
       "hh3cPortalSSIDFreeRuleIndex": hh3cPortalSSIDFreeRuleIndex,
       "hh3cPortalSSIDFreeRuleSrcSSID": hh3cPortalSSIDFreeRuleSrcSSID,
       "hh3cPortalSSIDFreeRuleRowStatus": hh3cPortalSSIDFreeRuleRowStatus,
       "hh3cPortalSSIDFreeRuleSrcSpot": hh3cPortalSSIDFreeRuleSrcSpot,
       "hh3cPortalMacTriggerSrvTable": hh3cPortalMacTriggerSrvTable,
       "hh3cPortalMacTriggerSrvEntry": hh3cPortalMacTriggerSrvEntry,
       "hh3cPortalMacTriggerSrvIndex": hh3cPortalMacTriggerSrvIndex,
       "hh3cPortalMacTriggerSrvIPAddrType": hh3cPortalMacTriggerSrvIPAddrType,
       "hh3cPortalMacTriggerSrvIP": hh3cPortalMacTriggerSrvIP,
       "hh3cPortalMacTriggerSrvPort": hh3cPortalMacTriggerSrvPort,
       "hh3cPortalMacTriggerSrvRowStatus": hh3cPortalMacTriggerSrvRowStatus,
       "hh3cPortalMacTriggerOnIfTable": hh3cPortalMacTriggerOnIfTable,
       "hh3cPortalMacTriggerOnIfEntry": hh3cPortalMacTriggerOnIfEntry,
       "hh3cPortalMacTriggerOnIfIfIndex": hh3cPortalMacTriggerOnIfIfIndex,
       "hh3cPortalMacTriggerOnIfDetctFlowPeriod": hh3cPortalMacTriggerOnIfDetctFlowPeriod,
       "hh3cPortalMacTriggerOnIfThresholdFlow": hh3cPortalMacTriggerOnIfThresholdFlow,
       "hh3cPortalMacTriggerOnIfRowStatus": hh3cPortalMacTriggerOnIfRowStatus,
       "hh3cPortalFreeRuleTable": hh3cPortalFreeRuleTable,
       "hh3cPortalFreeRuleEntry": hh3cPortalFreeRuleEntry,
       "hh3cPortalFreeRuleIndex": hh3cPortalFreeRuleIndex,
       "hh3cPortalFreeRuleSrcIfIndex": hh3cPortalFreeRuleSrcIfIndex,
       "hh3cPortalFreeRuleSrcVlanID": hh3cPortalFreeRuleSrcVlanID,
       "hh3cPortalFreeRuleSrcMac": hh3cPortalFreeRuleSrcMac,
       "hh3cPortalFreeRuleAddrType": hh3cPortalFreeRuleAddrType,
       "hh3cPortalFreeRuleSrcAddr": hh3cPortalFreeRuleSrcAddr,
       "hh3cPortalFreeRuleSrcPrefix": hh3cPortalFreeRuleSrcPrefix,
       "hh3cPortalFreeRuleDstAddr": hh3cPortalFreeRuleDstAddr,
       "hh3cPortalFreeRuleDstPrefix": hh3cPortalFreeRuleDstPrefix,
       "hh3cPortalFreeRuleProtocol": hh3cPortalFreeRuleProtocol,
       "hh3cPortalFreeRuleSrcPort": hh3cPortalFreeRuleSrcPort,
       "hh3cPortalFreeRuleDstPort": hh3cPortalFreeRuleDstPort,
       "hh3cPortalFreeRuleRowStatus": hh3cPortalFreeRuleRowStatus,
       "hh3cPortalForbiddenRuleTable": hh3cPortalForbiddenRuleTable,
       "hh3cPortalForbiddenRuleEntry": hh3cPortalForbiddenRuleEntry,
       "hh3cPortalForbiddenRuleIndex": hh3cPortalForbiddenRuleIndex,
       "hh3cPortalForbiddenRuleSrcIfIndex": hh3cPortalForbiddenRuleSrcIfIndex,
       "hh3cPortalForbiddenRuleSrcVlanID": hh3cPortalForbiddenRuleSrcVlanID,
       "hh3cPortalForbiddenRuleSrcMac": hh3cPortalForbiddenRuleSrcMac,
       "hh3cPortalForbiddenRuleAddrType": hh3cPortalForbiddenRuleAddrType,
       "hh3cPortalForbiddenRuleSrcAddr": hh3cPortalForbiddenRuleSrcAddr,
       "hh3cPortalForbiddenRuleSrcPrefix": hh3cPortalForbiddenRuleSrcPrefix,
       "hh3cPortalForbiddenRuleDstAddr": hh3cPortalForbiddenRuleDstAddr,
       "hh3cPortalForbiddenRuleDstPrefix": hh3cPortalForbiddenRuleDstPrefix,
       "hh3cPortalForbiddenRuleProtocol": hh3cPortalForbiddenRuleProtocol,
       "hh3cPortalForbiddenRuleSrcPort": hh3cPortalForbiddenRuleSrcPort,
       "hh3cPortalForbiddenRuleDstPort": hh3cPortalForbiddenRuleDstPort,
       "hh3cPortalForbiddenRuleRowStatus": hh3cPortalForbiddenRuleRowStatus,
       "hh3cPortalForbiddenRuleSsidName": hh3cPortalForbiddenRuleSsidName,
       "hh3cPortalTraps": hh3cPortalTraps,
       "hh3cPortalTrapPrefix": hh3cPortalTrapPrefix,
       "hh3cPortalServerLost": hh3cPortalServerLost,
       "hh3cPortalServerGet": hh3cPortalServerGet,
       "hh3cPortalTrapVarObjects": hh3cPortalTrapVarObjects,
       "hh3cPortalFirstTrapTime": hh3cPortalFirstTrapTime,
       "hh3cPortalServerIP": hh3cPortalServerIP,
       "hh3cPortalStatistic": hh3cPortalStatistic,
       "hh3cPortalStatAuthReq": hh3cPortalStatAuthReq,
       "hh3cPortalStatAckLogout": hh3cPortalStatAckLogout,
       "hh3cPortalStatNotifyLogout": hh3cPortalStatNotifyLogout,
       "hh3cPortalStatChallengeTimeout": hh3cPortalStatChallengeTimeout,
       "hh3cPortalStatChallengeBusy": hh3cPortalStatChallengeBusy,
       "hh3cPortalStatChallengeFail": hh3cPortalStatChallengeFail,
       "hh3cPortalStatAuthTimeout": hh3cPortalStatAuthTimeout,
       "hh3cPortalStatAuthFail": hh3cPortalStatAuthFail,
       "hh3cPortalStatPwdError": hh3cPortalStatPwdError,
       "hh3cPortalStatAuthBusy": hh3cPortalStatAuthBusy,
       "hh3cPortalStatAuthDisordered": hh3cPortalStatAuthDisordered,
       "hh3cPortalStatAuthUnknownError": hh3cPortalStatAuthUnknownError,
       "hh3cPortalStatAuthResp": hh3cPortalStatAuthResp,
       "hh3cPortalStatChallengeReq": hh3cPortalStatChallengeReq,
       "hh3cPortalStatChallengeResp": hh3cPortalStatChallengeResp,
       "hh3cPortalStatHttpReq": hh3cPortalStatHttpReq,
       "hh3cPortalStatHttpResp": hh3cPortalStatHttpResp,
       "hh3cPortalStatHttpsReq": hh3cPortalStatHttpsReq,
       "hh3cPortalStatHttpsResp": hh3cPortalStatHttpsResp,
       "hh3cPortalPktStatistic": hh3cPortalPktStatistic,
       "hh3cPortalPktStaReqAuthNum": hh3cPortalPktStaReqAuthNum,
       "hh3cPortalPktStaAckAuthSuccess": hh3cPortalPktStaAckAuthSuccess,
       "hh3cPortalPktStaAckAuthReject": hh3cPortalPktStaAckAuthReject,
       "hh3cPortalPktStaAckAuthEstablish": hh3cPortalPktStaAckAuthEstablish,
       "hh3cPortalPktStaAckAuthBusy": hh3cPortalPktStaAckAuthBusy,
       "hh3cPortalPktStaAckAuthAuthFail": hh3cPortalPktStaAckAuthAuthFail,
       "hh3cPortalPktStaReqChallengeNum": hh3cPortalPktStaReqChallengeNum,
       "hh3cPortalPktStaAckChallengeSuccess": hh3cPortalPktStaAckChallengeSuccess,
       "hh3cPortalPktStaAckChallengeReject": hh3cPortalPktStaAckChallengeReject,
       "hh3cPortalPktStaAckChallengeEstablish": hh3cPortalPktStaAckChallengeEstablish,
       "hh3cPortalPktStaAckChallengeBusy": hh3cPortalPktStaAckChallengeBusy,
       "hh3cPortalPktStaAckChallengeAuthFail": hh3cPortalPktStaAckChallengeAuthFail,
       "hh3cPortalExtConfig": hh3cPortalExtConfig,
       "hh3cPortalExtMaxUserNumber": hh3cPortalExtMaxUserNumber,
       "hh3cPortalExtCurrentUserNumber": hh3cPortalExtCurrentUserNumber,
       "hh3cPortalExtStatus": hh3cPortalExtStatus,
       "hh3cPortalExtTables": hh3cPortalExtTables,
       "hh3cPortalExtSrvTable": hh3cPortalExtSrvTable,
       "hh3cPortalExtSrvEntry": hh3cPortalExtSrvEntry,
       "hh3cPortalExtSrvName": hh3cPortalExtSrvName,
       "hh3cPortalExtSrvIPAddrType": hh3cPortalExtSrvIPAddrType,
       "hh3cPortalExtSrvIP": hh3cPortalExtSrvIP,
       "hh3cPortalExtSrvPort": hh3cPortalExtSrvPort,
       "hh3cPortalExtSrvRowStatus": hh3cPortalExtSrvRowStatus,
       "hh3cPortalExtWebSrvTable": hh3cPortalExtWebSrvTable,
       "hh3cPortalExtWebSrvEntry": hh3cPortalExtWebSrvEntry,
       "hh3cPortalExtWebSrvName": hh3cPortalExtWebSrvName,
       "hh3cPortalExtWebSrvUrl": hh3cPortalExtWebSrvUrl,
       "hh3cPortalExtWebSrvRowStatus": hh3cPortalExtWebSrvRowStatus,
       "hh3cPortalExtMTSrvTable": hh3cPortalExtMTSrvTable,
       "hh3cPortalExtMTSrvEntry": hh3cPortalExtMTSrvEntry,
       "hh3cPortalExtMTSrvName": hh3cPortalExtMTSrvName,
       "hh3cPortalExtMTSrvIPAddrType": hh3cPortalExtMTSrvIPAddrType,
       "hh3cPortalExtMTSrvIP": hh3cPortalExtMTSrvIP,
       "hh3cPortalExtMTSrvPort": hh3cPortalExtMTSrvPort,
       "hh3cPortalExtMTDetctFlowPeriod": hh3cPortalExtMTDetctFlowPeriod,
       "hh3cPortalExtMTThresholdFlow": hh3cPortalExtMTThresholdFlow,
       "hh3cPortalExtMTSrvRowStatus": hh3cPortalExtMTSrvRowStatus,
       "hh3cPortalExtIfConfigTable": hh3cPortalExtIfConfigTable,
       "hh3cPortalExtIfConfigEntry": hh3cPortalExtIfConfigEntry,
       "hh3cPortalExtIfIndex": hh3cPortalExtIfIndex,
       "hh3cPortalExtIfWebSrvName": hh3cPortalExtIfWebSrvName,
       "hh3cPortalExtIfDomainName": hh3cPortalExtIfDomainName,
       "hh3cPortalExtIfAuthMethod": hh3cPortalExtIfAuthMethod,
       "hh3cPortalExtIfMTSrvName": hh3cPortalExtIfMTSrvName,
       "hh3cPortalExtIfMaxUser": hh3cPortalExtIfMaxUser,
       "hh3cPortalExtIfIpv6ConfigTable": hh3cPortalExtIfIpv6ConfigTable,
       "hh3cPortalExtIfIpv6ConfigEntry": hh3cPortalExtIfIpv6ConfigEntry,
       "hh3cPortalExtIfIpv6Index": hh3cPortalExtIfIpv6Index,
       "hh3cPortalExtIfIpv6WebSrvName": hh3cPortalExtIfIpv6WebSrvName,
       "hh3cPortalExtIfIpv6DomainName": hh3cPortalExtIfIpv6DomainName,
       "hh3cPortalExtIfIpv6AuthMethod": hh3cPortalExtIfIpv6AuthMethod,
       "hh3cPortalExtIfIpv6MaxUser": hh3cPortalExtIfIpv6MaxUser,
       "hh3cPortalDot11SrvTable": hh3cPortalDot11SrvTable,
       "hh3cPortalDot11SrvEntry": hh3cPortalDot11SrvEntry,
       "hh3cPortalDot11SrvTemName": hh3cPortalDot11SrvTemName,
       "hh3cPortalDot11WebSrvName": hh3cPortalDot11WebSrvName,
       "hh3cPortalDot11DomainName": hh3cPortalDot11DomainName,
       "hh3cPortalDot11AuthMethod": hh3cPortalDot11AuthMethod,
       "hh3cPortalDot11MTSrvName": hh3cPortalDot11MTSrvName,
       "hh3cPortalDot11MaxUser": hh3cPortalDot11MaxUser,
       "hh3cPortalDot11Ipv6SrvTable": hh3cPortalDot11Ipv6SrvTable,
       "hh3cPortalDot11Ipv6SrvEntry": hh3cPortalDot11Ipv6SrvEntry,
       "hh3cPortalDot11Ipv6SrvTemName": hh3cPortalDot11Ipv6SrvTemName,
       "hh3cPortalDot11Ipv6WebSrvName": hh3cPortalDot11Ipv6WebSrvName,
       "hh3cPortalDot11Ipv6DomainName": hh3cPortalDot11Ipv6DomainName,
       "hh3cPortalDot11Ipv6AuthMethod": hh3cPortalDot11Ipv6AuthMethod,
       "hh3cPortalDot11Ipv6MaxUser": hh3cPortalDot11Ipv6MaxUser}
)
