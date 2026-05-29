# SNMP MIB module (ALCATEL-IND1-DOT1X-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\nokia\aos6\ALCATEL-IND1-DOT1X-MIB

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

(softentIND1Dot1X,) = mibBuilder.importSymbols(
    "ALCATEL-IND1-BASE",
    "softentIND1Dot1X")

(dot1xPaePortNumber,) = mibBuilder.importSymbols(
    "IEEE8021-PAE-MIB",
    "dot1xPaePortNumber")

(InterfaceIndex,
 InterfaceIndexOrZero) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex",
    "InterfaceIndexOrZero")

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
 TextualConvention,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "TextualConvention",
    "TimeStamp",
    "TruthValue")


# MODULE-IDENTITY

alcatelIND1Dot1XMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 30, 1)
)
if mibBuilder.loadTexts:
    alcatelIND1Dot1XMIB.setRevisions(
        ("2019-10-07 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class ALADot1xClassificationPolicyType(TextualConvention, Integer32):
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
              19,
              20,
              21,
              22,
              29)
        )
    )
    namedValues = NamedValues(
        *(("dotXAuthentication", 0),
          ("macAuthentication", 1),
          ("groupMobilityRules", 2),
          ("vlanId", 3),
          ("defaultVlan", 4),
          ("block", 5),
          ("internalUseOnlyA", 6),
          ("internalUseOnlyB", 7),
          ("internalUseOnlyC", 8),
          ("captivePortalAuthentication", 9),
          ("captivePortalGroupMobility", 10),
          ("captivePortalDefaultVlan", 11),
          ("captivePortalVlanId", 12),
          ("captivePortalBlock", 13),
          ("captivePortalUnknown", 14),
          ("captivePortalUnpAuthSrv", 15),
          ("captivePortalUnpUsrCfg", 16),
          ("captivePortalUnpAAArule", 17),
          ("authServerUNP", 18),
          ("userConfigUNP", 19),
          ("aaaRuleUNP", 20),
          ("aaaAuthSvrDownUNP", 21),
          ("aaaAuthSvrDownBlock", 22),
          ("aaaAuthSvrDownVpUnp", 29))
    )



class ALADot1xAuthenticationType(TextualConvention, Integer32):
    status = "current"
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
        *(("noAuthentication", 0),
          ("dotXAuthentication", 1),
          ("macAuthentication", 2),
          ("captivePortal", 3))
    )



class ALADot1xAuthenticationResult(TextualConvention, Integer32):
    status = "current"
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
        *(("notApplicable", 0),
          ("inProgress", 1),
          ("success", 2),
          ("fail", 3))
    )



class ALADot1xMacLearntState(TextualConvention, Integer32):
    status = "current"
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
        *(("bridging", 0),
          ("filtering", 1),
          ("hicInProgress", 2),
          ("qmrInProgress", 3))
    )



class ALADot1xMacQueryType(TextualConvention, Integer32):
    status = "current"
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
        *(("all", 0),
          ("supplicant", 1),
          ("nonSupplicant", 2),
          ("captivePortal", 3))
    )



class ALADot1xDeviceType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("supplicant", 1),
          ("nonSupplicant", 2))
    )



class ALADot1xHicFlag(TextualConvention, Integer32):
    status = "current"
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



class AlaPassThroughStatus(TextualConvention, Integer32):
    status = "current"
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



# MIB Managed Objects in the order of their OIDs

_AlaIND1Dot1XMIBObjects_ObjectIdentity = ObjectIdentity
alaIND1Dot1XMIBObjects = _AlaIND1Dot1XMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 30, 1, 1)
)
if mibBuilder.loadTexts:
    alaIND1Dot1XMIBObjects.setStatus("current")
_AlaDot1xPortTable_Object = MibTable
alaDot1xPortTable = _AlaDot1xPortTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 30, 1, 1, 1)
)
if mibBuilder.loadTexts:
    alaDot1xPortTable.setStatus("deprecated")
_AlaDot1xPortEntry_Object = MibTableRow
alaDot1xPortEntry = _AlaDot1xPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 30, 1, 1, 1, 1)
)
alaDot1xPortEntry.setIndexNames(
    (0, "IEEE8021-PAE-MIB", "dot1xPaePortNumber"),
)
if mibBuilder.loadTexts:
    alaDot1xPortEntry.setStatus("deprecated")


class _AlaDot1xPortSlotNumber_Type(Integer32):
    """Custom type alaDot1xPortSlotNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_AlaDot1xPortSlotNumber_Type.__name__ = "Integer32"
_AlaDot1xPortSlotNumber_Object = MibTableColumn
alaDot1xPortSlotNumber = _AlaDot1xPortSlotNumber_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 30, 1, 1, 1, 1, 1),
    _AlaDot1xPortSlotNumber_Type()
)
alaDot1xPortSlotNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaDot1xPortSlotNumber.setStatus("deprecated")


class _AlaDot1xPortPortNumber_Type(Integer32):
    """Custom type alaDot1xPortPortNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 48),
    )


_AlaDot1xPortPortNumber_Type.__name__ = "Integer32"
_AlaDot1xPortPortNumber_Object = MibTableColumn
alaDot1xPortPortNumber = _AlaDot1xPortPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 30, 1, 1, 1, 1, 2),
    _AlaDot1xPortPortNumber_Type()
)
alaDot1xPortPortNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaDot1xPortPortNumber.setStatus("deprecated")
_AlaDot1xPortMACAddress_Type = MacAddress
_AlaDot1xPortMACAddress_Object = MibTableColumn
alaDot1xPortMACAddress = _AlaDot1xPortMACAddress_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 30, 1, 1, 1, 1, 3),
    _AlaDot1xPortMACAddress_Type()
)
alaDot1xPortMACAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaDot1xPortMACAddress.setStatus("deprecated")


class _AlaDot1xPortVlan_Type(Integer32):
    """Custom type alaDot1xPortVlan based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4096),
    )


_AlaDot1xPortVlan_Type.__name__ = "Integer32"
_AlaDot1xPortVlan_Object = MibTableColumn
alaDot1xPortVlan = _AlaDot1xPortVlan_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 30, 1, 1, 1, 1, 4),
    _AlaDot1xPortVlan_Type()
)
alaDot1xPortVlan.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaDot1xPortVlan.setStatus("deprecated")


class _AlaDot1xPortProtocol_Type(Integer32):
    """Custom type alaDot1xPortProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 6),
    )


_AlaDot1xPortProtocol_Type.__name__ = "Integer32"
_AlaDot1xPortProtocol_Object = MibTableColumn
alaDot1xPortProtocol = _AlaDot1xPortProtocol_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 30, 1, 1, 1, 1, 5),
    _AlaDot1xPortProtocol_Type()
)
alaDot1xPortProtocol.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaDot1xPortProtocol.setStatus("deprecated")
_AlaDot1xPortUserName_Type = DisplayString
_AlaDot1xPortUserName_Object = MibTableColumn
alaDot1xPortUserName = _AlaDot1xPortUserName_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 30, 1, 1, 1, 1, 6),
    _AlaDot1xPortUserName_Type()
)
alaDot1xPortUserName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaDot1xPortUserName.setStatus("deprecated")


class _AlaDot1xPortState_Type(Integer32):
    """Custom type alaDot1xPortState based on Integer32"""
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
              10)
        )
    )
    namedValues = NamedValues(
        *(("initialize", 1),
          ("disconnected", 2),
          ("connecting", 3),
          ("authenticating", 4),
          ("authenticated", 5),
          ("aborting", 6),
          ("held", 7),
          ("forceAuthenticated", 8),
          ("forceUnauthenticated", 9),
          ("authenticatedLocally", 10))
    )


_AlaDot1xPortState_Type.__name__ = "Integer32"
_AlaDot1xPortState_Object = MibTableColumn
alaDot1xPortState = _AlaDot1xPortState_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 30, 1, 1, 1, 1, 7),
    _AlaDot1xPortState_Type()
)
alaDot1xPortState.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaDot1xPortState.setStatus("deprecated")
_AlaDot1xSupplicantPolicyUsed_Type = ALADot1xClassificationPolicyType
_AlaDot1xSupplicantPolicyUsed_Object = MibTableColumn
alaDot1xSupplicantPolicyUsed = _AlaDot1xSupplicantPolicyUsed_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 30, 1, 1, 1, 1, 8),
    _AlaDot1xSupplicantPolicyUsed_Type()
)
alaDot1xSupplicantPolicyUsed.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaDot1xSupplicantPolicyUsed.setStatus("deprecated")
_AlaDot1xAuthFailReason_Type = DisplayString
_AlaDot1xAuthFailReason_Object = MibTableColumn
alaDot1xAuthFailReason = _AlaDot1xAuthFailReason_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 30, 1, 1, 1, 1, 9),
    _AlaDot1xAuthFailReason_Type()
)
alaDot1xAuthFailReason.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaDot1xAuthFailReason.setStatus("deprecated")
_AlaDot1xReAuthCount_Type = Integer32
_AlaDot1xReAuthCount_Object = MibTableColumn
alaDot1xReAuthCount = _AlaDot1xReAuthCount_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 30, 1, 1, 1, 1, 10),
    _AlaDot1xReAuthCount_Type()
)
alaDot1xReAuthCount.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaDot1xReAuthCount.setStatus("deprecated")
_AlaDot1xLastSuccessTime_Type = DisplayString
_AlaDot1xLastSuccessTime_Object = MibTableColumn
alaDot1xLastSuccessTime = _AlaDot1xLastSuccessTime_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 30, 1, 1, 1, 1, 11),
    _AlaDot1xLastSuccessTime_Type()
)
alaDot1xLastSuccessTime.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaDot1xLastSuccessTime.setStatus("deprecated")
_AlaDot1xPortLookupTable_Object = MibTable
alaDot1xPortLookupTable = _AlaDot1xPortLookupTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 30, 1, 1, 2)
)
if mibBuilder.loadTexts:
    alaDot1xPortLookupTable.setStatus("current")
_AlaDot1xPortLookupEntry_Object = MibTableRow
alaDot1xPortLookupEntry = _AlaDot1xPortLookupEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 30, 1, 1, 2, 1)
)
alaDot1xPortLookupEntry.setIndexNames(
    (0, "ALCATEL-IND1-DOT1X-MIB", "alaDot1xPortLookupSlotNumber"),
    (0, "ALCATEL-IND1-DOT1X-MIB", "alaDot1xPortLookupPortNumber"),
    (0, "ALCATEL-IND1-DOT1X-MIB", "alaDot1xPortLookupMACAddress"),
)
if mibBuilder.loadTexts:
    alaDot1xPortLookupEntry.setStatus("current")


class _AlaDot1xPortLookupSlotNumber_Type(Integer32):
    """Custom type alaDot1xPortLookupSlotNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_AlaDot1xPortLookupSlotNumber_Type.__name__ = "Integer32"
_AlaDot1xPortLookupSlotNumber_Object = MibTableColumn
alaDot1xPortLookupSlotNumber = _AlaDot1xPortLookupSlotNumber_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 30, 1, 1, 2, 1, 1),
    _AlaDot1xPortLookupSlotNumber_Type()
)
alaDot1xPortLookupSlotNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaDot1xPortLookupSlotNumber.setStatus("current")


class _AlaDot1xPortLookupPortNumber_Type(Integer32):
    """Custom type alaDot1xPortLookupPortNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 48),
    )


_AlaDot1xPortLookupPortNumber_Type.__name__ = "Integer32"
_AlaDot1xPortLookupPortNumber_Object = MibTableColumn
alaDot1xPortLookupPortNumber = _AlaDot1xPortLookupPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 30, 1, 1, 2, 1, 2),
    _AlaDot1xPortLookupPortNumber_Type()
)
alaDot1xPortLookupPortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaDot1xPortLookupPortNumber.setStatus("current")
_AlaDot1xPortLookupMACAddress_Type = MacAddress
_AlaDot1xPortLookupMACAddress_Object = MibTableColumn
alaDot1xPortLookupMACAddress = _AlaDot1xPortLookupMACAddress_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 30, 1, 1, 2, 1, 3),
    _AlaDot1xPortLookupMACAddress_Type()
)
alaDot1xPortLookupMACAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaDot1xPortLookupMACAddress.setStatus("current")
_AlaDot1xPortLookupInterfaceNumber_Type = InterfaceIndex
_AlaDot1xPortLookupInterfaceNumber_Object = MibTableColumn
alaDot1xPortLookupInterfaceNumber = _AlaDot1xPortLookupInterfaceNumber_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 30, 1, 1, 2, 1, 4),
    _AlaDot1xPortLookupInterfaceNumber_Type()
)
alaDot1xPortLookupInterfaceNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaDot1xPortLookupInterfaceNumber.setStatus("current")
_AlaDot1xMacTable_Object = MibTable
alaDot1xMacTable = _AlaDot1xMacTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 30, 1, 1, 4)
)
if mibBuilder.loadTexts:
    alaDot1xMacTable.setStatus("current")
_AlaDot1xMacEntry_Object = MibTableRow
alaDot1xMacEntry = _AlaDot1xMacEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 30, 1, 1, 4, 1)
)
alaDot1xMacEntry.setIndexNames(
    (0, "ALCATEL-IND1-DOT1X-MIB", "alaDot1xMACAddress"),
)
if mibBuilder.loadTexts:
    alaDot1xMacEntry.setStatus("current")
_AlaDot1xMACAddress_Type = MacAddress
_AlaDot1xMACAddress_Object = MibTableColumn
alaDot1xMACAddress = _AlaDot1xMACAddress_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 30, 1, 1, 4, 1, 1),
    _AlaDot1xMACAddress_Type()
)
alaDot1xMACAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaDot1xMACAddress.setStatus("current")
_AlaDot1xMacIfIndex_Type = InterfaceIndex
_AlaDot1xMacIfIndex_Object = MibTableColumn
alaDot1xMacIfIndex = _AlaDot1xMacIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 30, 1, 1, 4, 1, 2),
    _AlaDot1xMacIfIndex_Type()
)
alaDot1xMacIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaDot1xMacIfIndex.setStatus("current")


class _AlaDot1xMacSlotNumber_Type(Integer32):
    """Custom type alaDot1xMacSlotNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_AlaDot1xMacSlotNumber_Type.__name__ = "Integer32"
_AlaDot1xMacSlotNumber_Object = MibTableColumn
alaDot1xMacSlotNumber = _AlaDot1xMacSlotNumber_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 30, 1, 1, 4, 1, 3),
    _AlaDot1xMacSlotNumber_Type()
)
alaDot1xMacSlotNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaDot1xMacSlotNumber.setStatus("current")


class _AlaDot1xMacPortNumber_Type(Integer32):
    """Custom type alaDot1xMacPortNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 48),
    )


_AlaDot1xMacPortNumber_Type.__name__ = "Integer32"
_AlaDot1xMacPortNumber_Object = MibTableColumn
alaDot1xMacPortNumber = _AlaDot1xMacPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 30, 1, 1, 4, 1, 4),
    _AlaDot1xMacPortNumber_Type()
)
alaDot1xMacPortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaDot1xMacPortNumber.setStatus("current")


class _AlaDot1xMacVlan_Type(Integer32):
    """Custom type alaDot1xMacVlan based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4096),
    )


_AlaDot1xMacVlan_Type.__name__ = "Integer32"
_AlaDot1xMacVlan_Object = MibTableColumn
alaDot1xMacVlan = _AlaDot1xMacVlan_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 30, 1, 1, 4, 1, 5),
    _AlaDot1xMacVlan_Type()
)
alaDot1xMacVlan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaDot1xMacVlan.setStatus("current")


class _AlaDot1xMacProtocol_Type(Integer32):
    """Custom type alaDot1xMacProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 6),
    )


_AlaDot1xMacProtocol_Type.__name__ = "Integer32"
_AlaDot1xMacProtocol_Object = MibTableColumn
alaDot1xMacProtocol = _AlaDot1xMacProtocol_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 30, 1, 1, 4, 1, 6),
    _AlaDot1xMacProtocol_Type()
)
alaDot1xMacProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaDot1xMacProtocol.setStatus("current")


class _AlaDot1xMacUserName_Type(DisplayString):
    """Custom type alaDot1xMacUserName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_AlaDot1xMacUserName_Type.__name__ = "DisplayString"
_AlaDot1xMacUserName_Object = MibTableColumn
alaDot1xMacUserName = _AlaDot1xMacUserName_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 30, 1, 1, 4, 1, 7),
    _AlaDot1xMacUserName_Type()
)
alaDot1xMacUserName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaDot1xMacUserName.setStatus("current")


class _AlaDot1xMacState_Type(Integer32):
    """Custom type alaDot1xMacState based on Integer32"""
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
              10)
        )
    )
    namedValues = NamedValues(
        *(("initialize", 1),
          ("disconnected", 2),
          ("connecting", 3),
          ("authenticating", 4),
          ("authenticated", 5),
          ("aborting", 6),
          ("held", 7),
          ("forceAuthenticated", 8),
          ("forceUnauthenticated", 9),
          ("authenticatedLocally", 10))
    )


_AlaDot1xMacState_Type.__name__ = "Integer32"
_AlaDot1xMacState_Object = MibTableColumn
alaDot1xMacState = _AlaDot1xMacState_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 30, 1, 1, 4, 1, 8),
    _AlaDot1xMacState_Type()
)
alaDot1xMacState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaDot1xMacState.setStatus("current")
_AlaDot1xMacSupplicantPolicyUsed_Type = ALADot1xClassificationPolicyType
_AlaDot1xMacSupplicantPolicyUsed_Object = MibTableColumn
alaDot1xMacSupplicantPolicyUsed = _AlaDot1xMacSupplicantPolicyUsed_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 30, 1, 1, 4, 1, 9),
    _AlaDot1xMacSupplicantPolicyUsed_Type()
)
alaDot1xMacSupplicantPolicyUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaDot1xMacSupplicantPolicyUsed.setStatus("current")
_AlaDot1xHicEnabledMAC_Type = ALADot1xHicFlag
_AlaDot1xHicEnabledMAC_Object = MibTableColumn
alaDot1xHicEnabledMAC = _AlaDot1xHicEnabledMAC_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 30, 1, 1, 4, 1, 10),
    _AlaDot1xHicEnabledMAC_Type()
)
alaDot1xHicEnabledMAC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaDot1xHicEnabledMAC.setStatus("deprecated")
_AlaDot1xNonSupplicantTable_Object = MibTable
alaDot1xNonSupplicantTable = _AlaDot1xNonSupplicantTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 30, 1, 1, 5)
)
if mibBuilder.loadTexts:
    alaDot1xNonSupplicantTable.setStatus("current")
_AlaDot1xNonSupplicantEntry_Object = MibTableRow
alaDot1xNonSupplicantEntry = _AlaDot1xNonSupplicantEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 30, 1, 1, 5, 1)
)
alaDot1xNonSupplicantEntry.setIndexNames(
    (0, "ALCATEL-IND1-DOT1X-MIB", "alaDot1xNonSupplicantIntfNum"),
    (0, "ALCATEL-IND1-DOT1X-MIB", "alaDot1xNonSupplicantMACAddress"),
)
if mibBuilder.loadTexts:
    alaDot1xNonSupplicantEntry.setStatus("current")
_AlaDot1xNonSupplicantIntfNum_Type = InterfaceIndex
_AlaDot1xNonSupplicantIntfNum_Object = MibTableColumn
alaDot1xNonSupplicantIntfNum = _AlaDot1xNonSupplicantIntfNum_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 30, 1, 1, 5, 1, 1),
    _AlaDot1xNonSupplicantIntfNum_Type()
)
alaDot1xNonSupplicantIntfNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaDot1xNonSupplicantIntfNum.setStatus("current")
_AlaDot1xNonSupplicantMACAddress_Type = MacAddress
_AlaDot1xNonSupplicantMACAddress_Object = MibTableColumn
alaDot1xNonSupplicantMACAddress = _AlaDot1xNonSupplicantMACAddress_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 30, 1, 1, 5, 1, 2),
    _AlaDot1xNonSupplicantMACAddress_Type()
)
alaDot1xNonSupplicantMACAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaDot1xNonSupplicantMACAddress.setStatus("current")


class _AlaDot1xNonSupplicantVlanID_Type(Integer32):
    """Custom type alaDot1xNonSupplicantVlanID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4096),
    )


_AlaDot1xNonSupplicantVlanID_Type.__name__ = "Integer32"
_AlaDot1xNonSupplicantVlanID_Object = MibTableColumn
alaDot1xNonSupplicantVlanID = _AlaDot1xNonSupplicantVlanID_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 30, 1, 1, 5, 1, 3),
    _AlaDot1xNonSupplicantVlanID_Type()
)
alaDot1xNonSupplicantVlanID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaDot1xNonSupplicantVlanID.setStatus("current")
_AlaDot1xNonSupplicantPolicyUsed_Type = ALADot1xClassificationPolicyType
_AlaDot1xNonSupplicantPolicyUsed_Object = MibTableColumn
alaDot1xNonSupplicantPolicyUsed = _AlaDot1xNonSupplicantPolicyUsed_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 30, 1, 1, 5, 1, 4),
    _AlaDot1xNonSupplicantPolicyUsed_Type()
)
alaDot1xNonSupplicantPolicyUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaDot1xNonSupplicantPolicyUsed.setStatus("current")


class _AlaDot1xAuthenticationStatus_Type(Integer32):
    """Custom type alaDot1xAuthenticationStatus based on Integer32"""
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
        *(("idle", 1),
          ("inProgress", 2),
          ("authenticated", 3),
          ("failed", 4),
          ("failedTimeout", 5),
          ("failedNoServer", 6),
          ("failedNoResources", 7))
    )


_AlaDot1xAuthenticationStatus_Type.__name__ = "Integer32"
_AlaDot1xAuthenticationStatus_Object = MibTableColumn
alaDot1xAuthenticationStatus = _AlaDot1xAuthenticationStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 30, 1, 1, 5, 1, 5),
    _AlaDot1xAuthenticationStatus_Type()
)
alaDot1xAuthenticationStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaDot1xAuthenticationStatus.setStatus("current")
_AlaDot1xNonSupplicantHicEnabledMAC_Type = ALADot1xHicFlag
_AlaDot1xNonSupplicantHicEnabledMAC_Object = MibTableColumn
alaDot1xNonSupplicantHicEnabledMAC = _AlaDot1xNonSupplicantHicEnabledMAC_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 30, 1, 1, 5, 1, 6),
    _AlaDot1xNonSupplicantHicEnabledMAC_Type()
)
alaDot1xNonSupplicantHicEnabledMAC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaDot1xNonSupplicantHicEnabledMAC.setStatus("current")
_AlaDot1xNonSupplicantUserName_Type = DisplayString
_AlaDot1xNonSupplicantUserName_Object = MibTableColumn
alaDot1xNonSupplicantUserName = _AlaDot1xNonSupplicantUserName_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 30, 1, 1, 5, 1, 7),
    _AlaDot1xNonSupplicantUserName_Type()
)
alaDot1xNonSupplicantUserName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaDot1xNonSupplicantUserName.setStatus("current")
_AlaDot1xAuthPolicyTable_Object = MibTable
alaDot1xAuthPolicyTable = _AlaDot1xAuthPolicyTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 30, 1, 1, 6)
)
if mibBuilder.loadTexts:
    alaDot1xAuthPolicyTable.setStatus("current")
_AlaDot1xAuthPolicyEntry_Object = MibTableRow
alaDot1xAuthPolicyEntry = _AlaDot1xAuthPolicyEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 30, 1, 1, 6, 1)
)
alaDot1xAuthPolicyEntry.setIndexNames(
    (0, "ALCATEL-IND1-DOT1X-MIB", "alaDot1xAuthPolicyIntfNumber"),
)
if mibBuilder.loadTexts:
    alaDot1xAuthPolicyEntry.setStatus("current")
_AlaDot1xAuthPolicyIntfNumber_Type = InterfaceIndex
_AlaDot1xAuthPolicyIntfNumber_Object = MibTableColumn
alaDot1xAuthPolicyIntfNumber = _AlaDot1xAuthPolicyIntfNumber_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 30, 1, 1, 6, 1, 1),
    _AlaDot1xAuthPolicyIntfNumber_Type()
)
alaDot1xAuthPolicyIntfNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaDot1xAuthPolicyIntfNumber.setStatus("current")


class _AlaDot1xNonSuppPolicy_Type(DisplayString):
    """Custom type alaDot1xNonSuppPolicy based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_AlaDot1xNonSuppPolicy_Type.__name__ = "DisplayString"
_AlaDot1xNonSuppPolicy_Object = MibTableColumn
alaDot1xNonSuppPolicy = _AlaDot1xNonSuppPolicy_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 30, 1, 1, 6, 1, 2),
    _AlaDot1xNonSuppPolicy_Type()
)
alaDot1xNonSuppPolicy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaDot1xNonSuppPolicy.setStatus("current")


class _AlaDot1xSuppPolicy_Type(DisplayString):
    """Custom type alaDot1xSuppPolicy based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_AlaDot1xSuppPolicy_Type.__name__ = "DisplayString"
_AlaDot1xSuppPolicy_Object = MibTableColumn
alaDot1xSuppPolicy = _AlaDot1xSuppPolicy_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 30, 1, 1, 6, 1, 3),
    _AlaDot1xSuppPolicy_Type()
)
alaDot1xSuppPolicy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaDot1xSuppPolicy.setStatus("current")


class _AlaDot1xPollingCnt_Type(Integer32):
    """Custom type alaDot1xPollingCnt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 99),
    )


_AlaDot1xPollingCnt_Type.__name__ = "Integer32"
_AlaDot1xPollingCnt_Object = MibTableColumn
alaDot1xPollingCnt = _AlaDot1xPollingCnt_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 30, 1, 1, 6, 1, 4),
    _AlaDot1xPollingCnt_Type()
)
alaDot1xPollingCnt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaDot1xPollingCnt.setStatus("current")


class _AlaDot1xCaptivePortalPolicy_Type(DisplayString):
    """Custom type alaDot1xCaptivePortalPolicy based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_AlaDot1xCaptivePortalPolicy_Type.__name__ = "DisplayString"
_AlaDot1xCaptivePortalPolicy_Object = MibTableColumn
alaDot1xCaptivePortalPolicy = _AlaDot1xCaptivePortalPolicy_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 30, 1, 1, 6, 1, 5),
    _AlaDot1xCaptivePortalPolicy_Type()
)
alaDot1xCaptivePortalPolicy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaDot1xCaptivePortalPolicy.setStatus("current")


class _AlaDot1xCPortalSessionLimit_Type(Integer32):
    """Custom type alaDot1xCPortalSessionLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 999),
    )


_AlaDot1xCPortalSessionLimit_Type.__name__ = "Integer32"
_AlaDot1xCPortalSessionLimit_Object = MibTableColumn
alaDot1xCPortalSessionLimit = _AlaDot1xCPortalSessionLimit_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 30, 1, 1, 6, 1, 6),
    _AlaDot1xCPortalSessionLimit_Type()
)
alaDot1xCPortalSessionLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaDot1xCPortalSessionLimit.setStatus("current")


class _AlaDot1xCPortalRetryCnt_Type(Integer32):
    """Custom type alaDot1xCPortalRetryCnt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 999),
    )


_AlaDot1xCPortalRetryCnt_Type.__name__ = "Integer32"
_AlaDot1xCPortalRetryCnt_Object = MibTableColumn
alaDot1xCPortalRetryCnt = _AlaDot1xCPortalRetryCnt_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 30, 1, 1, 6, 1, 7),
    _AlaDot1xCPortalRetryCnt_Type()
)
alaDot1xCPortalRetryCnt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaDot1xCPortalRetryCnt.setStatus("current")


class _AlaDot1xSupplicantBypass_Type(Integer32):
    """Custom type alaDot1xSupplicantBypass based on Integer32"""
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


_AlaDot1xSupplicantBypass_Type.__name__ = "Integer32"
_AlaDot1xSupplicantBypass_Object = MibTableColumn
alaDot1xSupplicantBypass = _AlaDot1xSupplicantBypass_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 30, 1, 1, 6, 1, 8),
    _AlaDot1xSupplicantBypass_Type()
)
alaDot1xSupplicantBypass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaDot1xSupplicantBypass.setStatus("current")


class _AlaDot1xSBAllowEAP_Type(Integer32):
    """Custom type alaDot1xSBAllowEAP based on Integer32"""
    defaultValue = 4

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
        *(("pass", 1),
          ("fail", 2),
          ("noauth", 3),
          ("none", 4))
    )


_AlaDot1xSBAllowEAP_Type.__name__ = "Integer32"
_AlaDot1xSBAllowEAP_Object = MibTableColumn
alaDot1xSBAllowEAP = _AlaDot1xSBAllowEAP_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 30, 1, 1, 6, 1, 9),
    _AlaDot1xSBAllowEAP_Type()
)
alaDot1xSBAllowEAP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaDot1xSBAllowEAP.setStatus("current")


class _AlaDot1xCPortalInactivityLogout_Type(Integer32):
    """Custom type alaDot1xCPortalInactivityLogout based on Integer32"""
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


_AlaDot1xCPortalInactivityLogout_Type.__name__ = "Integer32"
_AlaDot1xCPortalInactivityLogout_Object = MibTableColumn
alaDot1xCPortalInactivityLogout = _AlaDot1xCPortalInactivityLogout_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 30, 1, 1, 6, 1, 10),
    _AlaDot1xCPortalInactivityLogout_Type()
)
alaDot1xCPortalInactivityLogout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaDot1xCPortalInactivityLogout.setStatus("current")


class _AlaDot1xNonSuppSessTimeoutStatus_Type(Integer32):
    """Custom type alaDot1xNonSuppSessTimeoutStatus based on Integer32"""
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


_AlaDot1xNonSuppSessTimeoutStatus_Type.__name__ = "Integer32"
_AlaDot1xNonSuppSessTimeoutStatus_Object = MibTableColumn
alaDot1xNonSuppSessTimeoutStatus = _AlaDot1xNonSuppSessTimeoutStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 30, 1, 1, 6, 1, 11),
    _AlaDot1xNonSuppSessTimeoutStatus_Type()
)
alaDot1xNonSuppSessTimeoutStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaDot1xNonSuppSessTimeoutStatus.setStatus("current")


class _AlaDot1xNonSuppSessTimeoutIntrvl_Type(Integer32):
    """Custom type alaDot1xNonSuppSessTimeoutIntrvl based on Integer32"""
    defaultValue = 43200


_AlaDot1xNonSuppSessTimeoutIntrvl_Type.__name__ = "Integer32"
_AlaDot1xNonSuppSessTimeoutIntrvl_Object = MibTableColumn
alaDot1xNonSuppSessTimeoutIntrvl = _AlaDot1xNonSuppSessTimeoutIntrvl_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 30, 1, 1, 6, 1, 12),
    _AlaDot1xNonSuppSessTimeoutIntrvl_Type()
)
alaDot1xNonSuppSessTimeoutIntrvl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaDot1xNonSuppSessTimeoutIntrvl.setStatus("current")


class _AlaDot1xNonSuppSessTimeoutTrustRadStatus_Type(Integer32):
    """Custom type alaDot1xNonSuppSessTimeoutTrustRadStatus based on Integer32"""
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


_AlaDot1xNonSuppSessTimeoutTrustRadStatus_Type.__name__ = "Integer32"
_AlaDot1xNonSuppSessTimeoutTrustRadStatus_Object = MibTableColumn
alaDot1xNonSuppSessTimeoutTrustRadStatus = _AlaDot1xNonSuppSessTimeoutTrustRadStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 30, 1, 1, 6, 1, 13),
    _AlaDot1xNonSuppSessTimeoutTrustRadStatus_Type()
)
alaDot1xNonSuppSessTimeoutTrustRadStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaDot1xNonSuppSessTimeoutTrustRadStatus.setStatus("current")


class _AlaDot1xSuppTrustRadiusEnabled_Type(Integer32):
    """Custom type alaDot1xSuppTrustRadiusEnabled based on Integer32"""
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


_AlaDot1xSuppTrustRadiusEnabled_Type.__name__ = "Integer32"
_AlaDot1xSuppTrustRadiusEnabled_Object = MibTableColumn
alaDot1xSuppTrustRadiusEnabled = _AlaDot1xSuppTrustRadiusEnabled_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 30, 1, 1, 6, 1, 14),
    _AlaDot1xSuppTrustRadiusEnabled_Type()
)
alaDot1xSuppTrustRadiusEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaDot1xSuppTrustRadiusEnabled.setStatus("current")


class _AlaDot1xNonSupInactivityLogout_Type(Integer32):
    """Custom type alaDot1xNonSupInactivityLogout based on Integer32"""
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


_AlaDot1xNonSupInactivityLogout_Type.__name__ = "Integer32"
_AlaDot1xNonSupInactivityLogout_Object = MibTableColumn
alaDot1xNonSupInactivityLogout = _AlaDot1xNonSupInactivityLogout_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 30, 1, 1, 6, 1, 15),
    _AlaDot1xNonSupInactivityLogout_Type()
)
alaDot1xNonSupInactivityLogout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaDot1xNonSupInactivityLogout.setStatus("current")


class _AlaDot1xPerPortAPModeStatus_Type(Integer32):
    """Custom type alaDot1xPerPortAPModeStatus based on Integer32"""
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


_AlaDot1xPerPortAPModeStatus_Type.__name__ = "Integer32"
_AlaDot1xPerPortAPModeStatus_Object = MibTableColumn
alaDot1xPerPortAPModeStatus = _AlaDot1xPerPortAPModeStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 30, 1, 1, 6, 1, 16),
    _AlaDot1xPerPortAPModeStatus_Type()
)
alaDot1xPerPortAPModeStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaDot1xPerPortAPModeStatus.setStatus("current")


class _AlaDot1xPerPortForceL3Learning_Type(Integer32):
    """Custom type alaDot1xPerPortForceL3Learning based on Integer32"""
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


_AlaDot1xPerPortForceL3Learning_Type.__name__ = "Integer32"
_AlaDot1xPerPortForceL3Learning_Object = MibTableColumn
alaDot1xPerPortForceL3Learning = _AlaDot1xPerPortForceL3Learning_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 30, 1, 1, 6, 1, 17),
    _AlaDot1xPerPortForceL3Learning_Type()
)
alaDot1xPerPortForceL3Learning.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaDot1xPerPortForceL3Learning.setStatus("current")


class _AlaDot1xPerPortForceL3LearningPortBounce_Type(Integer32):
    """Custom type alaDot1xPerPortForceL3LearningPortBounce based on Integer32"""
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


_AlaDot1xPerPortForceL3LearningPortBounce_Type.__name__ = "Integer32"
_AlaDot1xPerPortForceL3LearningPortBounce_Object = MibTableColumn
alaDot1xPerPortForceL3LearningPortBounce = _AlaDot1xPerPortForceL3LearningPortBounce_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 30, 1, 1, 6, 1, 18),
    _AlaDot1xPerPortForceL3LearningPortBounce_Type()
)
alaDot1xPerPortForceL3LearningPortBounce.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaDot1xPerPortForceL3LearningPortBounce.setStatus("current")
_AlaDot1xCportalConfig_ObjectIdentity = ObjectIdentity
alaDot1xCportalConfig = _AlaDot1xCportalConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 30, 1, 1, 7)
)
_AlaDot1xCPortalIpAddress_Type = IpAddress
_AlaDot1xCPortalIpAddress_Object = MibScalar
alaDot1xCPortalIpAddress = _AlaDot1xCPortalIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 30, 1, 1, 7, 1),
    _AlaDot1xCPortalIpAddress_Type()
)
alaDot1xCPortalIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaDot1xCPortalIpAddress.setStatus("current")


class _AlaDot1xCPortalProxyURL_Type(SnmpAdminString):
    """Custom type alaDot1xCPortalProxyURL based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_AlaDot1xCPortalProxyURL_Type.__name__ = "SnmpAdminString"
_AlaDot1xCPortalProxyURL_Object = MibScalar
alaDot1xCPortalProxyURL = _AlaDot1xCPortalProxyURL_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 30, 1, 1, 7, 2),
    _AlaDot1xCPortalProxyURL_Type()
)
alaDot1xCPortalProxyURL.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaDot1xCPortalProxyURL.setStatus("current")


class _AlaDot1xCPortalPostAuthSuccessRedirectURL_Type(SnmpAdminString):
    """Custom type alaDot1xCPortalPostAuthSuccessRedirectURL based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_AlaDot1xCPortalPostAuthSuccessRedirectURL_Type.__name__ = "SnmpAdminString"
_AlaDot1xCPortalPostAuthSuccessRedirectURL_Object = MibScalar
alaDot1xCPortalPostAuthSuccessRedirectURL = _AlaDot1xCPortalPostAuthSuccessRedirectURL_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 30, 1, 1, 7, 3),
    _AlaDot1xCPortalPostAuthSuccessRedirectURL_Type()
)
alaDot1xCPortalPostAuthSuccessRedirectURL.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaDot1xCPortalPostAuthSuccessRedirectURL.setStatus("current")


class _AlaDot1xCPortalPostAuthFailRedirectURL_Type(SnmpAdminString):
    """Custom type alaDot1xCPortalPostAuthFailRedirectURL based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_AlaDot1xCPortalPostAuthFailRedirectURL_Type.__name__ = "SnmpAdminString"
_AlaDot1xCPortalPostAuthFailRedirectURL_Object = MibScalar
alaDot1xCPortalPostAuthFailRedirectURL = _AlaDot1xCPortalPostAuthFailRedirectURL_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 30, 1, 1, 7, 4),
    _AlaDot1xCPortalPostAuthFailRedirectURL_Type()
)
alaDot1xCPortalPostAuthFailRedirectURL.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaDot1xCPortalPostAuthFailRedirectURL.setStatus("current")


class _AlaDot1xCPortalDNSKeyword1_Type(SnmpAdminString):
    """Custom type alaDot1xCPortalDNSKeyword1 based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_AlaDot1xCPortalDNSKeyword1_Type.__name__ = "SnmpAdminString"
_AlaDot1xCPortalDNSKeyword1_Object = MibScalar
alaDot1xCPortalDNSKeyword1 = _AlaDot1xCPortalDNSKeyword1_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 30, 1, 1, 7, 5),
    _AlaDot1xCPortalDNSKeyword1_Type()
)
alaDot1xCPortalDNSKeyword1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaDot1xCPortalDNSKeyword1.setStatus("current")


class _AlaDot1xCPortalDNSKeyword2_Type(SnmpAdminString):
    """Custom type alaDot1xCPortalDNSKeyword2 based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_AlaDot1xCPortalDNSKeyword2_Type.__name__ = "SnmpAdminString"
_AlaDot1xCPortalDNSKeyword2_Object = MibScalar
alaDot1xCPortalDNSKeyword2 = _AlaDot1xCPortalDNSKeyword2_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 30, 1, 1, 7, 6),
    _AlaDot1xCPortalDNSKeyword2_Type()
)
alaDot1xCPortalDNSKeyword2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaDot1xCPortalDNSKeyword2.setStatus("current")


class _AlaDot1xCPortalDNSKeyword3_Type(SnmpAdminString):
    """Custom type alaDot1xCPortalDNSKeyword3 based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_AlaDot1xCPortalDNSKeyword3_Type.__name__ = "SnmpAdminString"
_AlaDot1xCPortalDNSKeyword3_Object = MibScalar
alaDot1xCPortalDNSKeyword3 = _AlaDot1xCPortalDNSKeyword3_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 30, 1, 1, 7, 7),
    _AlaDot1xCPortalDNSKeyword3_Type()
)
alaDot1xCPortalDNSKeyword3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaDot1xCPortalDNSKeyword3.setStatus("current")


class _AlaDot1xCPortalDNSKeyword4_Type(SnmpAdminString):
    """Custom type alaDot1xCPortalDNSKeyword4 based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_AlaDot1xCPortalDNSKeyword4_Type.__name__ = "SnmpAdminString"
_AlaDot1xCPortalDNSKeyword4_Object = MibScalar
alaDot1xCPortalDNSKeyword4 = _AlaDot1xCPortalDNSKeyword4_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 30, 1, 1, 7, 8),
    _AlaDot1xCPortalDNSKeyword4_Type()
)
alaDot1xCPortalDNSKeyword4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaDot1xCPortalDNSKeyword4.setStatus("current")


class _AlaDot1xCPortalProxyPort_Type(Integer32):
    """Custom type alaDot1xCPortalProxyPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_AlaDot1xCPortalProxyPort_Type.__name__ = "Integer32"
_AlaDot1xCPortalProxyPort_Object = MibScalar
alaDot1xCPortalProxyPort = _AlaDot1xCPortalProxyPort_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 30, 1, 1, 7, 9),
    _AlaDot1xCPortalProxyPort_Type()
)
alaDot1xCPortalProxyPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaDot1xCPortalProxyPort.setStatus("current")


class _AlaDot1xCPortalRedirectString_Type(SnmpAdminString):
    """Custom type alaDot1xCPortalRedirectString based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_AlaDot1xCPortalRedirectString_Type.__name__ = "SnmpAdminString"
_AlaDot1xCPortalRedirectString_Object = MibScalar
alaDot1xCPortalRedirectString = _AlaDot1xCPortalRedirectString_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 30, 1, 1, 7, 10),
    _AlaDot1xCPortalRedirectString_Type()
)
alaDot1xCPortalRedirectString.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaDot1xCPortalRedirectString.setStatus("current")
_AlaDot1xDeviceStatusTable_Object = MibTable
alaDot1xDeviceStatusTable = _AlaDot1xDeviceStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 30, 1, 1, 8)
)
if mibBuilder.loadTexts:
    alaDot1xDeviceStatusTable.setStatus("current")
_AlaDot1xDeviceStatusEntry_Object = MibTableRow
alaDot1xDeviceStatusEntry = _AlaDot1xDeviceStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 30, 1, 1, 8, 1)
)
alaDot1xDeviceStatusEntry.setIndexNames(
    (0, "ALCATEL-IND1-DOT1X-MIB", "alaDot1xDeviceStatusMacQueryType"),
    (0, "ALCATEL-IND1-DOT1X-MIB", "alaDot1xDeviceStatusSlotNumber"),
    (0, "ALCATEL-IND1-DOT1X-MIB", "alaDot1xDeviceStatusPortNumber"),
    (0, "ALCATEL-IND1-DOT1X-MIB", "alaDot1xDeviceStatusMACAddress"),
    (0, "ALCATEL-IND1-DOT1X-MIB", "alaDot1xDeviceStatusDeviceType"),
)
if mibBuilder.loadTexts:
    alaDot1xDeviceStatusEntry.setStatus("current")
_AlaDot1xDeviceStatusMacQueryType_Type = ALADot1xMacQueryType
_AlaDot1xDeviceStatusMacQueryType_Object = MibTableColumn
alaDot1xDeviceStatusMacQueryType = _AlaDot1xDeviceStatusMacQueryType_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 30, 1, 1, 8, 1, 1),
    _AlaDot1xDeviceStatusMacQueryType_Type()
)
alaDot1xDeviceStatusMacQueryType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaDot1xDeviceStatusMacQueryType.setStatus("current")


class _AlaDot1xDeviceStatusSlotNumber_Type(Integer32):
    """Custom type alaDot1xDeviceStatusSlotNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_AlaDot1xDeviceStatusSlotNumber_Type.__name__ = "Integer32"
_AlaDot1xDeviceStatusSlotNumber_Object = MibTableColumn
alaDot1xDeviceStatusSlotNumber = _AlaDot1xDeviceStatusSlotNumber_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 30, 1, 1, 8, 1, 2),
    _AlaDot1xDeviceStatusSlotNumber_Type()
)
alaDot1xDeviceStatusSlotNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaDot1xDeviceStatusSlotNumber.setStatus("current")


class _AlaDot1xDeviceStatusPortNumber_Type(Integer32):
    """Custom type alaDot1xDeviceStatusPortNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 48),
    )


_AlaDot1xDeviceStatusPortNumber_Type.__name__ = "Integer32"
_AlaDot1xDeviceStatusPortNumber_Object = MibTableColumn
alaDot1xDeviceStatusPortNumber = _AlaDot1xDeviceStatusPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 30, 1, 1, 8, 1, 3),
    _AlaDot1xDeviceStatusPortNumber_Type()
)
alaDot1xDeviceStatusPortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaDot1xDeviceStatusPortNumber.setStatus("current")
_AlaDot1xDeviceStatusMACAddress_Type = MacAddress
_AlaDot1xDeviceStatusMACAddress_Object = MibTableColumn
alaDot1xDeviceStatusMACAddress = _AlaDot1xDeviceStatusMACAddress_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 30, 1, 1, 8, 1, 4),
    _AlaDot1xDeviceStatusMACAddress_Type()
)
alaDot1xDeviceStatusMACAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaDot1xDeviceStatusMACAddress.setStatus("current")
_AlaDot1xDeviceStatusDeviceType_Type = ALADot1xDeviceType
_AlaDot1xDeviceStatusDeviceType_Object = MibTableColumn
alaDot1xDeviceStatusDeviceType = _AlaDot1xDeviceStatusDeviceType_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 30, 1, 1, 8, 1, 5),
    _AlaDot1xDeviceStatusDeviceType_Type()
)
alaDot1xDeviceStatusDeviceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaDot1xDeviceStatusDeviceType.setStatus("current")


class _AlaDot1xDeviceStatusVlan_Type(Integer32):
    """Custom type alaDot1xDeviceStatusVlan based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4096),
    )


_AlaDot1xDeviceStatusVlan_Type.__name__ = "Integer32"
_AlaDot1xDeviceStatusVlan_Object = MibTableColumn
alaDot1xDeviceStatusVlan = _AlaDot1xDeviceStatusVlan_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 30, 1, 1, 8, 1, 6),
    _AlaDot1xDeviceStatusVlan_Type()
)
alaDot1xDeviceStatusVlan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaDot1xDeviceStatusVlan.setStatus("current")
_AlaDot1xDeviceStatusIPAddress_Type = IpAddress
_AlaDot1xDeviceStatusIPAddress_Object = MibTableColumn
alaDot1xDeviceStatusIPAddress = _AlaDot1xDeviceStatusIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 30, 1, 1, 8, 1, 7),
    _AlaDot1xDeviceStatusIPAddress_Type()
)
alaDot1xDeviceStatusIPAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaDot1xDeviceStatusIPAddress.setStatus("current")
_AlaDot1xDeviceStatusUserName_Type = SnmpAdminString
_AlaDot1xDeviceStatusUserName_Object = MibTableColumn
alaDot1xDeviceStatusUserName = _AlaDot1xDeviceStatusUserName_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 30, 1, 1, 8, 1, 8),
    _AlaDot1xDeviceStatusUserName_Type()
)
alaDot1xDeviceStatusUserName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaDot1xDeviceStatusUserName.setStatus("current")
_AlaDot1xDeviceStatusProfileUsed_Type = SnmpAdminString
_AlaDot1xDeviceStatusProfileUsed_Object = MibTableColumn
alaDot1xDeviceStatusProfileUsed = _AlaDot1xDeviceStatusProfileUsed_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 30, 1, 1, 8, 1, 9),
    _AlaDot1xDeviceStatusProfileUsed_Type()
)
alaDot1xDeviceStatusProfileUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaDot1xDeviceStatusProfileUsed.setStatus("current")
_AlaDot1xDeviceStatusAuthType_Type = ALADot1xAuthenticationType
_AlaDot1xDeviceStatusAuthType_Object = MibTableColumn
alaDot1xDeviceStatusAuthType = _AlaDot1xDeviceStatusAuthType_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 30, 1, 1, 8, 1, 10),
    _AlaDot1xDeviceStatusAuthType_Type()
)
alaDot1xDeviceStatusAuthType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaDot1xDeviceStatusAuthType.setStatus("current")
_AlaDot1xDeviceStatusPolicyUsed_Type = ALADot1xClassificationPolicyType
_AlaDot1xDeviceStatusPolicyUsed_Object = MibTableColumn
alaDot1xDeviceStatusPolicyUsed = _AlaDot1xDeviceStatusPolicyUsed_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 30, 1, 1, 8, 1, 11),
    _AlaDot1xDeviceStatusPolicyUsed_Type()
)
alaDot1xDeviceStatusPolicyUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaDot1xDeviceStatusPolicyUsed.setStatus("current")
_AlaDot1xDeviceStatusAuthResult_Type = ALADot1xAuthenticationResult
_AlaDot1xDeviceStatusAuthResult_Object = MibTableColumn
alaDot1xDeviceStatusAuthResult = _AlaDot1xDeviceStatusAuthResult_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 30, 1, 1, 8, 1, 12),
    _AlaDot1xDeviceStatusAuthResult_Type()
)
alaDot1xDeviceStatusAuthResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaDot1xDeviceStatusAuthResult.setStatus("current")
_AlaDot1xDeviceStatusMacLearntState_Type = ALADot1xMacLearntState
_AlaDot1xDeviceStatusMacLearntState_Object = MibTableColumn
alaDot1xDeviceStatusMacLearntState = _AlaDot1xDeviceStatusMacLearntState_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 30, 1, 1, 8, 1, 13),
    _AlaDot1xDeviceStatusMacLearntState_Type()
)
alaDot1xDeviceStatusMacLearntState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaDot1xDeviceStatusMacLearntState.setStatus("current")
_AlaDot1xDeviceStatusTimeLearned_Type = TimeStamp
_AlaDot1xDeviceStatusTimeLearned_Object = MibTableColumn
alaDot1xDeviceStatusTimeLearned = _AlaDot1xDeviceStatusTimeLearned_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 30, 1, 1, 8, 1, 14),
    _AlaDot1xDeviceStatusTimeLearned_Type()
)
alaDot1xDeviceStatusTimeLearned.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaDot1xDeviceStatusTimeLearned.setStatus("current")
_AlaDot1xDeviceStatusCaptivePortalUsed_Type = TruthValue
_AlaDot1xDeviceStatusCaptivePortalUsed_Object = MibTableColumn
alaDot1xDeviceStatusCaptivePortalUsed = _AlaDot1xDeviceStatusCaptivePortalUsed_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 30, 1, 1, 8, 1, 15),
    _AlaDot1xDeviceStatusCaptivePortalUsed_Type()
)
alaDot1xDeviceStatusCaptivePortalUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaDot1xDeviceStatusCaptivePortalUsed.setStatus("current")


class _AlaDot1xDeviceStatusHicResult_Type(Integer32):
    """Custom type alaDot1xDeviceStatusHicResult based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 9),
    )


_AlaDot1xDeviceStatusHicResult_Type.__name__ = "Integer32"
_AlaDot1xDeviceStatusHicResult_Object = MibTableColumn
alaDot1xDeviceStatusHicResult = _AlaDot1xDeviceStatusHicResult_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 30, 1, 1, 8, 1, 16),
    _AlaDot1xDeviceStatusHicResult_Type()
)
alaDot1xDeviceStatusHicResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaDot1xDeviceStatusHicResult.setStatus("current")
_AlaDot1xAdminLogoutParams_ObjectIdentity = ObjectIdentity
alaDot1xAdminLogoutParams = _AlaDot1xAdminLogoutParams_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 30, 1, 1, 9)
)


class _AlaDot1xAdminLogoutType_Type(Integer32):
    """Custom type alaDot1xAdminLogoutType based on Integer32"""
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
        *(("noOperation", 0),
          ("macAddress", 1),
          ("username", 2),
          ("networkProfileName", 3),
          ("interfaceId", 4))
    )


_AlaDot1xAdminLogoutType_Type.__name__ = "Integer32"
_AlaDot1xAdminLogoutType_Object = MibScalar
alaDot1xAdminLogoutType = _AlaDot1xAdminLogoutType_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 30, 1, 1, 9, 1),
    _AlaDot1xAdminLogoutType_Type()
)
alaDot1xAdminLogoutType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaDot1xAdminLogoutType.setStatus("current")
_AlaDot1xAdminLogoutMacAddress_Type = MacAddress
_AlaDot1xAdminLogoutMacAddress_Object = MibScalar
alaDot1xAdminLogoutMacAddress = _AlaDot1xAdminLogoutMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 30, 1, 1, 9, 2),
    _AlaDot1xAdminLogoutMacAddress_Type()
)
alaDot1xAdminLogoutMacAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaDot1xAdminLogoutMacAddress.setStatus("current")


class _AlaDot1xAdminLogoutUserName_Type(SnmpAdminString):
    """Custom type alaDot1xAdminLogoutUserName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AlaDot1xAdminLogoutUserName_Type.__name__ = "SnmpAdminString"
_AlaDot1xAdminLogoutUserName_Object = MibScalar
alaDot1xAdminLogoutUserName = _AlaDot1xAdminLogoutUserName_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 30, 1, 1, 9, 3),
    _AlaDot1xAdminLogoutUserName_Type()
)
alaDot1xAdminLogoutUserName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaDot1xAdminLogoutUserName.setStatus("current")


class _AlaDot1xAdminLogoutNetworkProfileName_Type(SnmpAdminString):
    """Custom type alaDot1xAdminLogoutNetworkProfileName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AlaDot1xAdminLogoutNetworkProfileName_Type.__name__ = "SnmpAdminString"
_AlaDot1xAdminLogoutNetworkProfileName_Object = MibScalar
alaDot1xAdminLogoutNetworkProfileName = _AlaDot1xAdminLogoutNetworkProfileName_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 30, 1, 1, 9, 4),
    _AlaDot1xAdminLogoutNetworkProfileName_Type()
)
alaDot1xAdminLogoutNetworkProfileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaDot1xAdminLogoutNetworkProfileName.setStatus("current")
_AlaDot1xAdminLogoutInterfaceId_Type = InterfaceIndexOrZero
_AlaDot1xAdminLogoutInterfaceId_Object = MibScalar
alaDot1xAdminLogoutInterfaceId = _AlaDot1xAdminLogoutInterfaceId_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 30, 1, 1, 9, 5),
    _AlaDot1xAdminLogoutInterfaceId_Type()
)
alaDot1xAdminLogoutInterfaceId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaDot1xAdminLogoutInterfaceId.setStatus("current")
_AlaDot1xAuthServerTimeout_ObjectIdentity = ObjectIdentity
alaDot1xAuthServerTimeout = _AlaDot1xAuthServerTimeout_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 30, 1, 1, 10)
)


class _AlaDot1xAuthSvrTimeoutPolicy_Type(DisplayString):
    """Custom type alaDot1xAuthSvrTimeoutPolicy based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_AlaDot1xAuthSvrTimeoutPolicy_Type.__name__ = "DisplayString"
_AlaDot1xAuthSvrTimeoutPolicy_Object = MibScalar
alaDot1xAuthSvrTimeoutPolicy = _AlaDot1xAuthSvrTimeoutPolicy_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 30, 1, 1, 10, 1),
    _AlaDot1xAuthSvrTimeoutPolicy_Type()
)
alaDot1xAuthSvrTimeoutPolicy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaDot1xAuthSvrTimeoutPolicy.setStatus("current")


class _AlaDot1xAuthSvrTimeoutReAuthPeriod_Type(Integer32):
    """Custom type alaDot1xAuthSvrTimeoutReAuthPeriod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(30, 43200),
    )


_AlaDot1xAuthSvrTimeoutReAuthPeriod_Type.__name__ = "Integer32"
_AlaDot1xAuthSvrTimeoutReAuthPeriod_Object = MibScalar
alaDot1xAuthSvrTimeoutReAuthPeriod = _AlaDot1xAuthSvrTimeoutReAuthPeriod_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 30, 1, 1, 10, 2),
    _AlaDot1xAuthSvrTimeoutReAuthPeriod_Type()
)
alaDot1xAuthSvrTimeoutReAuthPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaDot1xAuthSvrTimeoutReAuthPeriod.setStatus("current")


class _AlaDot1xAuthSvrTimeoutStatus_Type(Integer32):
    """Custom type alaDot1xAuthSvrTimeoutStatus based on Integer32"""
    defaultValue = 2

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


_AlaDot1xAuthSvrTimeoutStatus_Type.__name__ = "Integer32"
_AlaDot1xAuthSvrTimeoutStatus_Object = MibScalar
alaDot1xAuthSvrTimeoutStatus = _AlaDot1xAuthSvrTimeoutStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 30, 1, 1, 10, 3),
    _AlaDot1xAuthSvrTimeoutStatus_Type()
)
alaDot1xAuthSvrTimeoutStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaDot1xAuthSvrTimeoutStatus.setStatus("current")


class _AlaDot1xAuthSvrTimeoutVoicePolicy_Type(DisplayString):
    """Custom type alaDot1xAuthSvrTimeoutVoicePolicy based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_AlaDot1xAuthSvrTimeoutVoicePolicy_Type.__name__ = "DisplayString"
_AlaDot1xAuthSvrTimeoutVoicePolicy_Object = MibScalar
alaDot1xAuthSvrTimeoutVoicePolicy = _AlaDot1xAuthSvrTimeoutVoicePolicy_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 30, 1, 1, 10, 4),
    _AlaDot1xAuthSvrTimeoutVoicePolicy_Type()
)
alaDot1xAuthSvrTimeoutVoicePolicy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaDot1xAuthSvrTimeoutVoicePolicy.setStatus("current")


class _AlaDot1xAuthSvrPollingStatus_Type(Integer32):
    """Custom type alaDot1xAuthSvrPollingStatus based on Integer32"""
    defaultValue = 2

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


_AlaDot1xAuthSvrPollingStatus_Type.__name__ = "Integer32"
_AlaDot1xAuthSvrPollingStatus_Object = MibScalar
alaDot1xAuthSvrPollingStatus = _AlaDot1xAuthSvrPollingStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 30, 1, 1, 10, 5),
    _AlaDot1xAuthSvrPollingStatus_Type()
)
alaDot1xAuthSvrPollingStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaDot1xAuthSvrPollingStatus.setStatus("current")


class _AlaDot1xAuthSvrDownMacPersistency_Type(Integer32):
    """Custom type alaDot1xAuthSvrDownMacPersistency based on Integer32"""
    defaultValue = 2

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


_AlaDot1xAuthSvrDownMacPersistency_Type.__name__ = "Integer32"
_AlaDot1xAuthSvrDownMacPersistency_Object = MibScalar
alaDot1xAuthSvrDownMacPersistency = _AlaDot1xAuthSvrDownMacPersistency_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 30, 1, 1, 10, 6),
    _AlaDot1xAuthSvrDownMacPersistency_Type()
)
alaDot1xAuthSvrDownMacPersistency.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaDot1xAuthSvrDownMacPersistency.setStatus("current")
_AlaDot1xDelayLearningPeriod_Type = Integer32
_AlaDot1xDelayLearningPeriod_Object = MibScalar
alaDot1xDelayLearningPeriod = _AlaDot1xDelayLearningPeriod_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 30, 1, 1, 10, 7),
    _AlaDot1xDelayLearningPeriod_Type()
)
alaDot1xDelayLearningPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaDot1xDelayLearningPeriod.setStatus("current")


class _AlaDot1xAPModeStatus_Type(Integer32):
    """Custom type alaDot1xAPModeStatus based on Integer32"""
    defaultValue = 1

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


_AlaDot1xAPModeStatus_Type.__name__ = "Integer32"
_AlaDot1xAPModeStatus_Object = MibScalar
alaDot1xAPModeStatus = _AlaDot1xAPModeStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 30, 1, 1, 10, 8),
    _AlaDot1xAPModeStatus_Type()
)
alaDot1xAPModeStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaDot1xAPModeStatus.setStatus("current")


class _AlaDot1xEAPVersionStatus_Type(Integer32):
    """Custom type alaDot1xEAPVersionStatus based on Integer32"""
    defaultValue = 2

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


_AlaDot1xEAPVersionStatus_Type.__name__ = "Integer32"
_AlaDot1xEAPVersionStatus_Object = MibScalar
alaDot1xEAPVersionStatus = _AlaDot1xEAPVersionStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 30, 1, 1, 10, 9),
    _AlaDot1xEAPVersionStatus_Type()
)
alaDot1xEAPVersionStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaDot1xEAPVersionStatus.setStatus("current")


class _AlaDot1xForceL3Learning_Type(Integer32):
    """Custom type alaDot1xForceL3Learning based on Integer32"""
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


_AlaDot1xForceL3Learning_Type.__name__ = "Integer32"
_AlaDot1xForceL3Learning_Object = MibScalar
alaDot1xForceL3Learning = _AlaDot1xForceL3Learning_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 30, 1, 1, 10, 10),
    _AlaDot1xForceL3Learning_Type()
)
alaDot1xForceL3Learning.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaDot1xForceL3Learning.setStatus("current")


class _AlaDot1xForceL3LearningPortBounce_Type(Integer32):
    """Custom type alaDot1xForceL3LearningPortBounce based on Integer32"""
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


_AlaDot1xForceL3LearningPortBounce_Type.__name__ = "Integer32"
_AlaDot1xForceL3LearningPortBounce_Object = MibScalar
alaDot1xForceL3LearningPortBounce = _AlaDot1xForceL3LearningPortBounce_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 30, 1, 1, 10, 11),
    _AlaDot1xForceL3LearningPortBounce_Type()
)
alaDot1xForceL3LearningPortBounce.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaDot1xForceL3LearningPortBounce.setStatus("current")
_AlaPassthroughConfig_ObjectIdentity = ObjectIdentity
alaPassthroughConfig = _AlaPassthroughConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 30, 1, 1, 11)
)
_AlaDot1xPassthroughStatus_Type = AlaPassThroughStatus
_AlaDot1xPassthroughStatus_Object = MibScalar
alaDot1xPassthroughStatus = _AlaDot1xPassthroughStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 30, 1, 1, 11, 1),
    _AlaDot1xPassthroughStatus_Type()
)
alaDot1xPassthroughStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaDot1xPassthroughStatus.setStatus("current")
_AlaAvlanPassthroughStatus_Type = AlaPassThroughStatus
_AlaAvlanPassthroughStatus_Object = MibScalar
alaAvlanPassthroughStatus = _AlaAvlanPassthroughStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 30, 1, 1, 11, 2),
    _AlaAvlanPassthroughStatus_Type()
)
alaAvlanPassthroughStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaAvlanPassthroughStatus.setStatus("current")
_AlaCportalPassthroughStatus_Type = AlaPassThroughStatus
_AlaCportalPassthroughStatus_Object = MibScalar
alaCportalPassthroughStatus = _AlaCportalPassthroughStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 30, 1, 1, 11, 3),
    _AlaCportalPassthroughStatus_Type()
)
alaCportalPassthroughStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaCportalPassthroughStatus.setStatus("current")
_AlaKerberosPortTable_Object = MibTable
alaKerberosPortTable = _AlaKerberosPortTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 30, 1, 1, 12)
)
if mibBuilder.loadTexts:
    alaKerberosPortTable.setStatus("current")
_AlaKerberosPortEntry_Object = MibTableRow
alaKerberosPortEntry = _AlaKerberosPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 30, 1, 1, 12, 1)
)
alaKerberosPortEntry.setIndexNames(
    (0, "ALCATEL-IND1-DOT1X-MIB", "alaKerberosPortIfIndex"),
)
if mibBuilder.loadTexts:
    alaKerberosPortEntry.setStatus("current")
_AlaKerberosPortIfIndex_Type = InterfaceIndex
_AlaKerberosPortIfIndex_Object = MibTableColumn
alaKerberosPortIfIndex = _AlaKerberosPortIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 30, 1, 1, 12, 1, 1),
    _AlaKerberosPortIfIndex_Type()
)
alaKerberosPortIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaKerberosPortIfIndex.setStatus("current")


class _AlaKerberosPortStatus_Type(Integer32):
    """Custom type alaKerberosPortStatus based on Integer32"""
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


_AlaKerberosPortStatus_Type.__name__ = "Integer32"
_AlaKerberosPortStatus_Object = MibTableColumn
alaKerberosPortStatus = _AlaKerberosPortStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 30, 1, 1, 12, 1, 2),
    _AlaKerberosPortStatus_Type()
)
alaKerberosPortStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaKerberosPortStatus.setStatus("current")
_AlaDot1xCrlUnpTable_Object = MibTable
alaDot1xCrlUnpTable = _AlaDot1xCrlUnpTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 30, 1, 1, 13)
)
if mibBuilder.loadTexts:
    alaDot1xCrlUnpTable.setStatus("current")
_AlaDot1xCrlUnpEntry_Object = MibTableRow
alaDot1xCrlUnpEntry = _AlaDot1xCrlUnpEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 30, 1, 1, 13, 1)
)
alaDot1xCrlUnpEntry.setIndexNames(
    (0, "ALCATEL-IND1-DOT1X-MIB", "alaDot1xCrlIfIndex"),
)
if mibBuilder.loadTexts:
    alaDot1xCrlUnpEntry.setStatus("current")
_AlaDot1xCrlIfIndex_Type = InterfaceIndex
_AlaDot1xCrlIfIndex_Object = MibTableColumn
alaDot1xCrlIfIndex = _AlaDot1xCrlIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 30, 1, 1, 13, 1, 1),
    _AlaDot1xCrlIfIndex_Type()
)
alaDot1xCrlIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaDot1xCrlIfIndex.setStatus("current")


class _AlaDot1xCrlIngBw_Type(Integer32):
    """Custom type alaDot1xCrlIngBw based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 10485760),
    )


_AlaDot1xCrlIngBw_Type.__name__ = "Integer32"
_AlaDot1xCrlIngBw_Object = MibTableColumn
alaDot1xCrlIngBw = _AlaDot1xCrlIngBw_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 30, 1, 1, 13, 1, 2),
    _AlaDot1xCrlIngBw_Type()
)
alaDot1xCrlIngBw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaDot1xCrlIngBw.setStatus("current")


class _AlaDot1xCrlEgrBw_Type(Integer32):
    """Custom type alaDot1xCrlEgrBw based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 10485760),
    )


_AlaDot1xCrlEgrBw_Type.__name__ = "Integer32"
_AlaDot1xCrlEgrBw_Object = MibTableColumn
alaDot1xCrlEgrBw = _AlaDot1xCrlEgrBw_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 30, 1, 1, 13, 1, 3),
    _AlaDot1xCrlEgrBw_Type()
)
alaDot1xCrlEgrBw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaDot1xCrlEgrBw.setStatus("current")


class _AlaDot1xCrlIngTypeFlag_Type(Integer32):
    """Custom type alaDot1xCrlIngTypeFlag based on Integer32"""
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
        *(("notapplicable", 0),
          ("unp", 1),
          ("qos", 2))
    )


_AlaDot1xCrlIngTypeFlag_Type.__name__ = "Integer32"
_AlaDot1xCrlIngTypeFlag_Object = MibTableColumn
alaDot1xCrlIngTypeFlag = _AlaDot1xCrlIngTypeFlag_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 30, 1, 1, 13, 1, 4),
    _AlaDot1xCrlIngTypeFlag_Type()
)
alaDot1xCrlIngTypeFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaDot1xCrlIngTypeFlag.setStatus("current")


class _AlaDot1xCrlEgrTypeFlag_Type(Integer32):
    """Custom type alaDot1xCrlEgrTypeFlag based on Integer32"""
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
        *(("notapplicable", 0),
          ("unp", 1),
          ("qos", 2))
    )


_AlaDot1xCrlEgrTypeFlag_Type.__name__ = "Integer32"
_AlaDot1xCrlEgrTypeFlag_Object = MibTableColumn
alaDot1xCrlEgrTypeFlag = _AlaDot1xCrlEgrTypeFlag_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 30, 1, 1, 13, 1, 5),
    _AlaDot1xCrlEgrTypeFlag_Type()
)
alaDot1xCrlEgrTypeFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaDot1xCrlEgrTypeFlag.setStatus("current")


class _AlaDot1xCrlDefDepth_Type(Integer32):
    """Custom type alaDot1xCrlDefDepth based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 131072),
    )


_AlaDot1xCrlDefDepth_Type.__name__ = "Integer32"
_AlaDot1xCrlDefDepth_Object = MibTableColumn
alaDot1xCrlDefDepth = _AlaDot1xCrlDefDepth_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 30, 1, 1, 13, 1, 6),
    _AlaDot1xCrlDefDepth_Type()
)
alaDot1xCrlDefDepth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaDot1xCrlDefDepth.setStatus("current")


class _AlaDot1xCrlIngProfile_Type(SnmpAdminString):
    """Custom type alaDot1xCrlIngProfile based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_AlaDot1xCrlIngProfile_Type.__name__ = "SnmpAdminString"
_AlaDot1xCrlIngProfile_Object = MibTableColumn
alaDot1xCrlIngProfile = _AlaDot1xCrlIngProfile_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 30, 1, 1, 13, 1, 7),
    _AlaDot1xCrlIngProfile_Type()
)
alaDot1xCrlIngProfile.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaDot1xCrlIngProfile.setStatus("current")


class _AlaDot1xCrlEgrProfile_Type(SnmpAdminString):
    """Custom type alaDot1xCrlEgrProfile based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_AlaDot1xCrlEgrProfile_Type.__name__ = "SnmpAdminString"
_AlaDot1xCrlEgrProfile_Object = MibTableColumn
alaDot1xCrlEgrProfile = _AlaDot1xCrlEgrProfile_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 30, 1, 1, 13, 1, 8),
    _AlaDot1xCrlEgrProfile_Type()
)
alaDot1xCrlEgrProfile.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaDot1xCrlEgrProfile.setStatus("current")
_AlaRedirectByodHostTable_Object = MibTable
alaRedirectByodHostTable = _AlaRedirectByodHostTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 30, 1, 1, 14)
)
if mibBuilder.loadTexts:
    alaRedirectByodHostTable.setStatus("current")
_AlaRedirectByodHostEntry_Object = MibTableRow
alaRedirectByodHostEntry = _AlaRedirectByodHostEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 30, 1, 1, 14, 1)
)
alaRedirectByodHostEntry.setIndexNames(
    (0, "ALCATEL-IND1-DOT1X-MIB", "alaByodHostStateQueryType"),
    (0, "ALCATEL-IND1-DOT1X-MIB", "alaByodHostStateSlotNumber"),
    (0, "ALCATEL-IND1-DOT1X-MIB", "alaByodHostStatePortNumber"),
    (0, "ALCATEL-IND1-DOT1X-MIB", "alaByodHostStateMacAddress"),
    (0, "ALCATEL-IND1-DOT1X-MIB", "alaByodHostStateDeviceType"),
)
if mibBuilder.loadTexts:
    alaRedirectByodHostEntry.setStatus("current")
_AlaByodHostStateQueryType_Type = ALADot1xMacQueryType
_AlaByodHostStateQueryType_Object = MibTableColumn
alaByodHostStateQueryType = _AlaByodHostStateQueryType_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 30, 1, 1, 14, 1, 1),
    _AlaByodHostStateQueryType_Type()
)
alaByodHostStateQueryType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaByodHostStateQueryType.setStatus("current")


class _AlaByodHostStateSlotNumber_Type(Integer32):
    """Custom type alaByodHostStateSlotNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_AlaByodHostStateSlotNumber_Type.__name__ = "Integer32"
_AlaByodHostStateSlotNumber_Object = MibTableColumn
alaByodHostStateSlotNumber = _AlaByodHostStateSlotNumber_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 30, 1, 1, 14, 1, 2),
    _AlaByodHostStateSlotNumber_Type()
)
alaByodHostStateSlotNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaByodHostStateSlotNumber.setStatus("current")


class _AlaByodHostStatePortNumber_Type(Integer32):
    """Custom type alaByodHostStatePortNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 48),
    )


_AlaByodHostStatePortNumber_Type.__name__ = "Integer32"
_AlaByodHostStatePortNumber_Object = MibTableColumn
alaByodHostStatePortNumber = _AlaByodHostStatePortNumber_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 30, 1, 1, 14, 1, 3),
    _AlaByodHostStatePortNumber_Type()
)
alaByodHostStatePortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaByodHostStatePortNumber.setStatus("current")
_AlaByodHostStateMacAddress_Type = MacAddress
_AlaByodHostStateMacAddress_Object = MibTableColumn
alaByodHostStateMacAddress = _AlaByodHostStateMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 30, 1, 1, 14, 1, 4),
    _AlaByodHostStateMacAddress_Type()
)
alaByodHostStateMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaByodHostStateMacAddress.setStatus("current")
_AlaByodHostStateDeviceType_Type = ALADot1xDeviceType
_AlaByodHostStateDeviceType_Object = MibTableColumn
alaByodHostStateDeviceType = _AlaByodHostStateDeviceType_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 30, 1, 1, 14, 1, 5),
    _AlaByodHostStateDeviceType_Type()
)
alaByodHostStateDeviceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaByodHostStateDeviceType.setStatus("current")


class _AlaByodHostProgressStatus_Type(SnmpAdminString):
    """Custom type alaByodHostProgressStatus based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_AlaByodHostProgressStatus_Type.__name__ = "SnmpAdminString"
_AlaByodHostProgressStatus_Object = MibTableColumn
alaByodHostProgressStatus = _AlaByodHostProgressStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 30, 1, 1, 14, 1, 6),
    _AlaByodHostProgressStatus_Type()
)
alaByodHostProgressStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaByodHostProgressStatus.setStatus("current")
_AlaRedirectByodHostUnpTable_Object = MibTable
alaRedirectByodHostUnpTable = _AlaRedirectByodHostUnpTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 30, 1, 1, 15)
)
if mibBuilder.loadTexts:
    alaRedirectByodHostUnpTable.setStatus("current")
_AlaRedirectByodHostUnpEntry_Object = MibTableRow
alaRedirectByodHostUnpEntry = _AlaRedirectByodHostUnpEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 30, 1, 1, 15, 1)
)
alaRedirectByodHostUnpEntry.setIndexNames(
    (0, "ALCATEL-IND1-DOT1X-MIB", "alaByodClientMacQueryType"),
    (0, "ALCATEL-IND1-DOT1X-MIB", "alaByodClientSlotNumber"),
    (0, "ALCATEL-IND1-DOT1X-MIB", "alaByodClientPortNumber"),
    (0, "ALCATEL-IND1-DOT1X-MIB", "alaByodClientMacAddress"),
    (0, "ALCATEL-IND1-DOT1X-MIB", "alaByodClientDeviceType"),
)
if mibBuilder.loadTexts:
    alaRedirectByodHostUnpEntry.setStatus("current")
_AlaByodClientMacQueryType_Type = ALADot1xMacQueryType
_AlaByodClientMacQueryType_Object = MibTableColumn
alaByodClientMacQueryType = _AlaByodClientMacQueryType_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 30, 1, 1, 15, 1, 1),
    _AlaByodClientMacQueryType_Type()
)
alaByodClientMacQueryType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaByodClientMacQueryType.setStatus("current")


class _AlaByodClientSlotNumber_Type(Integer32):
    """Custom type alaByodClientSlotNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_AlaByodClientSlotNumber_Type.__name__ = "Integer32"
_AlaByodClientSlotNumber_Object = MibTableColumn
alaByodClientSlotNumber = _AlaByodClientSlotNumber_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 30, 1, 1, 15, 1, 2),
    _AlaByodClientSlotNumber_Type()
)
alaByodClientSlotNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaByodClientSlotNumber.setStatus("current")


class _AlaByodClientPortNumber_Type(Integer32):
    """Custom type alaByodClientPortNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 48),
    )


_AlaByodClientPortNumber_Type.__name__ = "Integer32"
_AlaByodClientPortNumber_Object = MibTableColumn
alaByodClientPortNumber = _AlaByodClientPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 30, 1, 1, 15, 1, 3),
    _AlaByodClientPortNumber_Type()
)
alaByodClientPortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaByodClientPortNumber.setStatus("current")
_AlaByodClientMacAddress_Type = MacAddress
_AlaByodClientMacAddress_Object = MibTableColumn
alaByodClientMacAddress = _AlaByodClientMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 30, 1, 1, 15, 1, 4),
    _AlaByodClientMacAddress_Type()
)
alaByodClientMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaByodClientMacAddress.setStatus("current")
_AlaByodClientDeviceType_Type = ALADot1xDeviceType
_AlaByodClientDeviceType_Object = MibTableColumn
alaByodClientDeviceType = _AlaByodClientDeviceType_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 30, 1, 1, 15, 1, 5),
    _AlaByodClientDeviceType_Type()
)
alaByodClientDeviceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaByodClientDeviceType.setStatus("current")


class _AlaByodPreviousUNP_Type(SnmpAdminString):
    """Custom type alaByodPreviousUNP based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_AlaByodPreviousUNP_Type.__name__ = "SnmpAdminString"
_AlaByodPreviousUNP_Object = MibTableColumn
alaByodPreviousUNP = _AlaByodPreviousUNP_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 30, 1, 1, 15, 1, 6),
    _AlaByodPreviousUNP_Type()
)
alaByodPreviousUNP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaByodPreviousUNP.setStatus("current")


class _AlaByodNewUNP_Type(SnmpAdminString):
    """Custom type alaByodNewUNP based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_AlaByodNewUNP_Type.__name__ = "SnmpAdminString"
_AlaByodNewUNP_Object = MibTableColumn
alaByodNewUNP = _AlaByodNewUNP_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 30, 1, 1, 15, 1, 7),
    _AlaByodNewUNP_Type()
)
alaByodNewUNP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaByodNewUNP.setStatus("current")


class _AlaByodCOAStatus_Type(SnmpAdminString):
    """Custom type alaByodCOAStatus based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_AlaByodCOAStatus_Type.__name__ = "SnmpAdminString"
_AlaByodCOAStatus_Object = MibTableColumn
alaByodCOAStatus = _AlaByodCOAStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 30, 1, 1, 15, 1, 8),
    _AlaByodCOAStatus_Type()
)
alaByodCOAStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaByodCOAStatus.setStatus("current")
_AlaIND1Dot1XMIBConformance_ObjectIdentity = ObjectIdentity
alaIND1Dot1XMIBConformance = _AlaIND1Dot1XMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 30, 1, 2)
)
if mibBuilder.loadTexts:
    alaIND1Dot1XMIBConformance.setStatus("current")
_AlaIND1Dot1XMIBGroups_ObjectIdentity = ObjectIdentity
alaIND1Dot1XMIBGroups = _AlaIND1Dot1XMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 30, 1, 2, 1)
)
if mibBuilder.loadTexts:
    alaIND1Dot1XMIBGroups.setStatus("current")

# Managed Objects groups

alaDot1xPortLookupGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 30, 1, 2, 1, 2)
)
alaDot1xPortLookupGroup.setObjects(
      *(("ALCATEL-IND1-DOT1X-MIB", "alaDot1xPortLookupSlotNumber"),
        ("ALCATEL-IND1-DOT1X-MIB", "alaDot1xPortLookupPortNumber"),
        ("ALCATEL-IND1-DOT1X-MIB", "alaDot1xPortLookupMACAddress"),
        ("ALCATEL-IND1-DOT1X-MIB", "alaDot1xPortLookupInterfaceNumber"))
)
if mibBuilder.loadTexts:
    alaDot1xPortLookupGroup.setStatus("current")

alaINDDot1XPolicyGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 30, 1, 2, 1, 3)
)
alaINDDot1XPolicyGroup.setObjects(
      *(("ALCATEL-IND1-DOT1X-MIB", "alaDot1xNonSuppPolicy"),
        ("ALCATEL-IND1-DOT1X-MIB", "alaDot1xSuppPolicy"),
        ("ALCATEL-IND1-DOT1X-MIB", "alaDot1xPollingCnt"),
        ("ALCATEL-IND1-DOT1X-MIB", "alaDot1xCaptivePortalPolicy"),
        ("ALCATEL-IND1-DOT1X-MIB", "alaDot1xCPortalSessionLimit"),
        ("ALCATEL-IND1-DOT1X-MIB", "alaDot1xCPortalRetryCnt"),
        ("ALCATEL-IND1-DOT1X-MIB", "alaDot1xSupplicantBypass"),
        ("ALCATEL-IND1-DOT1X-MIB", "alaDot1xSBAllowEAP"),
        ("ALCATEL-IND1-DOT1X-MIB", "alaDot1xCPortalInactivityLogout"))
)
if mibBuilder.loadTexts:
    alaINDDot1XPolicyGroup.setStatus("current")

alaINDDot1XDeviceStatusGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 30, 1, 2, 1, 4)
)
alaINDDot1XDeviceStatusGroup.setObjects(
      *(("ALCATEL-IND1-DOT1X-MIB", "alaDot1xDeviceStatusVlan"),
        ("ALCATEL-IND1-DOT1X-MIB", "alaDot1xDeviceStatusIPAddress"),
        ("ALCATEL-IND1-DOT1X-MIB", "alaDot1xDeviceStatusUserName"),
        ("ALCATEL-IND1-DOT1X-MIB", "alaDot1xDeviceStatusProfileUsed"),
        ("ALCATEL-IND1-DOT1X-MIB", "alaDot1xDeviceStatusAuthType"),
        ("ALCATEL-IND1-DOT1X-MIB", "alaDot1xDeviceStatusPolicyUsed"),
        ("ALCATEL-IND1-DOT1X-MIB", "alaDot1xDeviceStatusAuthResult"),
        ("ALCATEL-IND1-DOT1X-MIB", "alaDot1xDeviceStatusMacLearntState"),
        ("ALCATEL-IND1-DOT1X-MIB", "alaDot1xDeviceStatusTimeLearned"),
        ("ALCATEL-IND1-DOT1X-MIB", "alaDot1xDeviceStatusCaptivePortalUsed"),
        ("ALCATEL-IND1-DOT1X-MIB", "alaDot1xDeviceStatusHicResult"))
)
if mibBuilder.loadTexts:
    alaINDDot1XDeviceStatusGroup.setStatus("current")

alaDot1xAuthSvrTimeoutGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 30, 1, 2, 1, 5)
)
alaDot1xAuthSvrTimeoutGroup.setObjects(
      *(("ALCATEL-IND1-DOT1X-MIB", "alaDot1xAuthSvrTimeoutPolicy"),
        ("ALCATEL-IND1-DOT1X-MIB", "alaDot1xAuthSvrTimeoutReAuthPeriod"),
        ("ALCATEL-IND1-DOT1X-MIB", "alaDot1xAuthSvrTimeoutStatus"),
        ("ALCATEL-IND1-DOT1X-MIB", "alaDot1xAuthSvrTimeoutVoicePolicy"),
        ("ALCATEL-IND1-DOT1X-MIB", "alaDot1xAuthSvrPollingStatus"),
        ("ALCATEL-IND1-DOT1X-MIB", "alaDot1xAuthSvrDownMacPersistency"),
        ("ALCATEL-IND1-DOT1X-MIB", "alaDot1xDelayLearningPeriod"),
        ("ALCATEL-IND1-DOT1X-MIB", "alaDot1xAPModeStatus"),
        ("ALCATEL-IND1-DOT1X-MIB", "alaDot1xEAPVersionStatus"),
        ("ALCATEL-IND1-DOT1X-MIB", "alaDot1xForceL3Learning"),
        ("ALCATEL-IND1-DOT1X-MIB", "alaDot1xForceL3LearningPortBounce"))
)
if mibBuilder.loadTexts:
    alaDot1xAuthSvrTimeoutGroup.setStatus("current")

alaPassthroughConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 30, 1, 2, 1, 6)
)
alaPassthroughConfigGroup.setObjects(
      *(("ALCATEL-IND1-DOT1X-MIB", "alaDot1xPassthroughStatus"),
        ("ALCATEL-IND1-DOT1X-MIB", "alaAvlanPassthroughStatus"),
        ("ALCATEL-IND1-DOT1X-MIB", "alaCportalPassthroughStatus"))
)
if mibBuilder.loadTexts:
    alaPassthroughConfigGroup.setStatus("current")

alaDot1xAdminLogoutParamsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 30, 1, 2, 1, 7)
)
alaDot1xAdminLogoutParamsGroup.setObjects(
      *(("ALCATEL-IND1-DOT1X-MIB", "alaDot1xAdminLogoutType"),
        ("ALCATEL-IND1-DOT1X-MIB", "alaDot1xAdminLogoutMacAddress"),
        ("ALCATEL-IND1-DOT1X-MIB", "alaDot1xAdminLogoutUserName"),
        ("ALCATEL-IND1-DOT1X-MIB", "alaDot1xAdminLogoutNetworkProfileName"),
        ("ALCATEL-IND1-DOT1X-MIB", "alaDot1xAdminLogoutInterfaceId"))
)
if mibBuilder.loadTexts:
    alaDot1xAdminLogoutParamsGroup.setStatus("current")

alaDot1xNonSupplicantEntryGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 30, 1, 2, 1, 8)
)
alaDot1xNonSupplicantEntryGroup.setObjects(
      *(("ALCATEL-IND1-DOT1X-MIB", "alaDot1xNonSupplicantIntfNum"),
        ("ALCATEL-IND1-DOT1X-MIB", "alaDot1xNonSupplicantMACAddress"),
        ("ALCATEL-IND1-DOT1X-MIB", "alaDot1xNonSupplicantVlanID"),
        ("ALCATEL-IND1-DOT1X-MIB", "alaDot1xNonSupplicantPolicyUsed"),
        ("ALCATEL-IND1-DOT1X-MIB", "alaDot1xAuthenticationStatus"),
        ("ALCATEL-IND1-DOT1X-MIB", "alaDot1xNonSupplicantHicEnabledMAC"))
)
if mibBuilder.loadTexts:
    alaDot1xNonSupplicantEntryGroup.setStatus("current")

alaDot1xCportalConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 30, 1, 2, 1, 9)
)
alaDot1xCportalConfigGroup.setObjects(
      *(("ALCATEL-IND1-DOT1X-MIB", "alaDot1xCPortalIpAddress"),
        ("ALCATEL-IND1-DOT1X-MIB", "alaDot1xCPortalProxyURL"),
        ("ALCATEL-IND1-DOT1X-MIB", "alaDot1xCPortalPostAuthSuccessRedirectURL"),
        ("ALCATEL-IND1-DOT1X-MIB", "alaDot1xCPortalPostAuthFailRedirectURL"),
        ("ALCATEL-IND1-DOT1X-MIB", "alaDot1xCPortalDNSKeyword1"),
        ("ALCATEL-IND1-DOT1X-MIB", "alaDot1xCPortalDNSKeyword2"),
        ("ALCATEL-IND1-DOT1X-MIB", "alaDot1xCPortalDNSKeyword3"),
        ("ALCATEL-IND1-DOT1X-MIB", "alaDot1xCPortalDNSKeyword4"),
        ("ALCATEL-IND1-DOT1X-MIB", "alaDot1xCPortalProxyPort"),
        ("ALCATEL-IND1-DOT1X-MIB", "alaDot1xCPortalRedirectString"))
)
if mibBuilder.loadTexts:
    alaDot1xCportalConfigGroup.setStatus("current")

alaDot1xMacEntryGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 30, 1, 2, 1, 10)
)
alaDot1xMacEntryGroup.setObjects(
      *(("ALCATEL-IND1-DOT1X-MIB", "alaDot1xMacIfIndex"),
        ("ALCATEL-IND1-DOT1X-MIB", "alaDot1xHicEnabledMAC"),
        ("ALCATEL-IND1-DOT1X-MIB", "alaDot1xMacSlotNumber"),
        ("ALCATEL-IND1-DOT1X-MIB", "alaDot1xMacPortNumber"),
        ("ALCATEL-IND1-DOT1X-MIB", "alaDot1xMacVlan"),
        ("ALCATEL-IND1-DOT1X-MIB", "alaDot1xMacProtocol"),
        ("ALCATEL-IND1-DOT1X-MIB", "alaDot1xMacUserName"),
        ("ALCATEL-IND1-DOT1X-MIB", "alaDot1xMacState"),
        ("ALCATEL-IND1-DOT1X-MIB", "alaDot1xMacSupplicantPolicyUsed"))
)
if mibBuilder.loadTexts:
    alaDot1xMacEntryGroup.setStatus("current")

alaKerberosPortGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 30, 1, 2, 1, 11)
)
alaKerberosPortGroup.setObjects(
    ("ALCATEL-IND1-DOT1X-MIB", "alaKerberosPortStatus")
)
if mibBuilder.loadTexts:
    alaKerberosPortGroup.setStatus("current")

alaDot1xCrlUnpStatusGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 30, 1, 2, 1, 12)
)
alaDot1xCrlUnpStatusGroup.setObjects(
      *(("ALCATEL-IND1-DOT1X-MIB", "alaDot1xCrlIngBw"),
        ("ALCATEL-IND1-DOT1X-MIB", "alaDot1xCrlEgrBw"),
        ("ALCATEL-IND1-DOT1X-MIB", "alaDot1xCrlIngTypeFlag"),
        ("ALCATEL-IND1-DOT1X-MIB", "alaDot1xCrlEgrTypeFlag"),
        ("ALCATEL-IND1-DOT1X-MIB", "alaDot1xCrlDefDepth"),
        ("ALCATEL-IND1-DOT1X-MIB", "alaDot1xCrlIngProfile"),
        ("ALCATEL-IND1-DOT1X-MIB", "alaDot1xCrlEgrProfile"))
)
if mibBuilder.loadTexts:
    alaDot1xCrlUnpStatusGroup.setStatus("current")

alaINDDot1XRedirectByodHostGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 30, 1, 2, 1, 13)
)
alaINDDot1XRedirectByodHostGroup.setObjects(
    ("ALCATEL-IND1-DOT1X-MIB", "alaByodHostProgressStatus")
)
if mibBuilder.loadTexts:
    alaINDDot1XRedirectByodHostGroup.setStatus("current")

alaINDDot1XRedirectByodHostUnpGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 30, 1, 2, 1, 14)
)
alaINDDot1XRedirectByodHostUnpGroup.setObjects(
      *(("ALCATEL-IND1-DOT1X-MIB", "alaByodPreviousUNP"),
        ("ALCATEL-IND1-DOT1X-MIB", "alaByodNewUNP"),
        ("ALCATEL-IND1-DOT1X-MIB", "alaByodCOAStatus"))
)
if mibBuilder.loadTexts:
    alaINDDot1XRedirectByodHostUnpGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

alaIND1Dot1XMIBCompliances = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 30, 1, 2, 2)
)
alaIND1Dot1XMIBCompliances.setObjects(
      *(("ALCATEL-IND1-DOT1X-MIB", "alaDot1xPortLookupGroup"),
        ("ALCATEL-IND1-DOT1X-MIB", "alaINDDot1XPolicyGroup"),
        ("ALCATEL-IND1-DOT1X-MIB", "alaINDDot1XDeviceStatusGroup"),
        ("ALCATEL-IND1-DOT1X-MIB", "alaDot1xAuthSvrTimeoutGroup"),
        ("ALCATEL-IND1-DOT1X-MIB", "alaPassthroughConfigGroup"),
        ("ALCATEL-IND1-DOT1X-MIB", "alaDot1xAdminLogoutParamsGroup"),
        ("ALCATEL-IND1-DOT1X-MIB", "alaDot1xNonSupplicantEntryGroup"),
        ("ALCATEL-IND1-DOT1X-MIB", "alaDot1xCportalConfigGroup"),
        ("ALCATEL-IND1-DOT1X-MIB", "alaDot1xMacEntryGroup"),
        ("ALCATEL-IND1-DOT1X-MIB", "alaKerberosPortGroup"),
        ("ALCATEL-IND1-DOT1X-MIB", "alaDot1xCrlUnpStatusGroup"),
        ("ALCATEL-IND1-DOT1X-MIB", "alaINDDot1XRedirectByodHostGroup"),
        ("ALCATEL-IND1-DOT1X-MIB", "alaINDDot1XRedirectByodHostUnpGroup"))
)
if mibBuilder.loadTexts:
    alaIND1Dot1XMIBCompliances.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ALCATEL-IND1-DOT1X-MIB",
    **{"ALADot1xClassificationPolicyType": ALADot1xClassificationPolicyType,
       "ALADot1xAuthenticationType": ALADot1xAuthenticationType,
       "ALADot1xAuthenticationResult": ALADot1xAuthenticationResult,
       "ALADot1xMacLearntState": ALADot1xMacLearntState,
       "ALADot1xMacQueryType": ALADot1xMacQueryType,
       "ALADot1xDeviceType": ALADot1xDeviceType,
       "ALADot1xHicFlag": ALADot1xHicFlag,
       "AlaPassThroughStatus": AlaPassThroughStatus,
       "alcatelIND1Dot1XMIB": alcatelIND1Dot1XMIB,
       "alaIND1Dot1XMIBObjects": alaIND1Dot1XMIBObjects,
       "alaDot1xPortTable": alaDot1xPortTable,
       "alaDot1xPortEntry": alaDot1xPortEntry,
       "alaDot1xPortSlotNumber": alaDot1xPortSlotNumber,
       "alaDot1xPortPortNumber": alaDot1xPortPortNumber,
       "alaDot1xPortMACAddress": alaDot1xPortMACAddress,
       "alaDot1xPortVlan": alaDot1xPortVlan,
       "alaDot1xPortProtocol": alaDot1xPortProtocol,
       "alaDot1xPortUserName": alaDot1xPortUserName,
       "alaDot1xPortState": alaDot1xPortState,
       "alaDot1xSupplicantPolicyUsed": alaDot1xSupplicantPolicyUsed,
       "alaDot1xAuthFailReason": alaDot1xAuthFailReason,
       "alaDot1xReAuthCount": alaDot1xReAuthCount,
       "alaDot1xLastSuccessTime": alaDot1xLastSuccessTime,
       "alaDot1xPortLookupTable": alaDot1xPortLookupTable,
       "alaDot1xPortLookupEntry": alaDot1xPortLookupEntry,
       "alaDot1xPortLookupSlotNumber": alaDot1xPortLookupSlotNumber,
       "alaDot1xPortLookupPortNumber": alaDot1xPortLookupPortNumber,
       "alaDot1xPortLookupMACAddress": alaDot1xPortLookupMACAddress,
       "alaDot1xPortLookupInterfaceNumber": alaDot1xPortLookupInterfaceNumber,
       "alaDot1xMacTable": alaDot1xMacTable,
       "alaDot1xMacEntry": alaDot1xMacEntry,
       "alaDot1xMACAddress": alaDot1xMACAddress,
       "alaDot1xMacIfIndex": alaDot1xMacIfIndex,
       "alaDot1xMacSlotNumber": alaDot1xMacSlotNumber,
       "alaDot1xMacPortNumber": alaDot1xMacPortNumber,
       "alaDot1xMacVlan": alaDot1xMacVlan,
       "alaDot1xMacProtocol": alaDot1xMacProtocol,
       "alaDot1xMacUserName": alaDot1xMacUserName,
       "alaDot1xMacState": alaDot1xMacState,
       "alaDot1xMacSupplicantPolicyUsed": alaDot1xMacSupplicantPolicyUsed,
       "alaDot1xHicEnabledMAC": alaDot1xHicEnabledMAC,
       "alaDot1xNonSupplicantTable": alaDot1xNonSupplicantTable,
       "alaDot1xNonSupplicantEntry": alaDot1xNonSupplicantEntry,
       "alaDot1xNonSupplicantIntfNum": alaDot1xNonSupplicantIntfNum,
       "alaDot1xNonSupplicantMACAddress": alaDot1xNonSupplicantMACAddress,
       "alaDot1xNonSupplicantVlanID": alaDot1xNonSupplicantVlanID,
       "alaDot1xNonSupplicantPolicyUsed": alaDot1xNonSupplicantPolicyUsed,
       "alaDot1xAuthenticationStatus": alaDot1xAuthenticationStatus,
       "alaDot1xNonSupplicantHicEnabledMAC": alaDot1xNonSupplicantHicEnabledMAC,
       "alaDot1xNonSupplicantUserName": alaDot1xNonSupplicantUserName,
       "alaDot1xAuthPolicyTable": alaDot1xAuthPolicyTable,
       "alaDot1xAuthPolicyEntry": alaDot1xAuthPolicyEntry,
       "alaDot1xAuthPolicyIntfNumber": alaDot1xAuthPolicyIntfNumber,
       "alaDot1xNonSuppPolicy": alaDot1xNonSuppPolicy,
       "alaDot1xSuppPolicy": alaDot1xSuppPolicy,
       "alaDot1xPollingCnt": alaDot1xPollingCnt,
       "alaDot1xCaptivePortalPolicy": alaDot1xCaptivePortalPolicy,
       "alaDot1xCPortalSessionLimit": alaDot1xCPortalSessionLimit,
       "alaDot1xCPortalRetryCnt": alaDot1xCPortalRetryCnt,
       "alaDot1xSupplicantBypass": alaDot1xSupplicantBypass,
       "alaDot1xSBAllowEAP": alaDot1xSBAllowEAP,
       "alaDot1xCPortalInactivityLogout": alaDot1xCPortalInactivityLogout,
       "alaDot1xNonSuppSessTimeoutStatus": alaDot1xNonSuppSessTimeoutStatus,
       "alaDot1xNonSuppSessTimeoutIntrvl": alaDot1xNonSuppSessTimeoutIntrvl,
       "alaDot1xNonSuppSessTimeoutTrustRadStatus": alaDot1xNonSuppSessTimeoutTrustRadStatus,
       "alaDot1xSuppTrustRadiusEnabled": alaDot1xSuppTrustRadiusEnabled,
       "alaDot1xNonSupInactivityLogout": alaDot1xNonSupInactivityLogout,
       "alaDot1xPerPortAPModeStatus": alaDot1xPerPortAPModeStatus,
       "alaDot1xPerPortForceL3Learning": alaDot1xPerPortForceL3Learning,
       "alaDot1xPerPortForceL3LearningPortBounce": alaDot1xPerPortForceL3LearningPortBounce,
       "alaDot1xCportalConfig": alaDot1xCportalConfig,
       "alaDot1xCPortalIpAddress": alaDot1xCPortalIpAddress,
       "alaDot1xCPortalProxyURL": alaDot1xCPortalProxyURL,
       "alaDot1xCPortalPostAuthSuccessRedirectURL": alaDot1xCPortalPostAuthSuccessRedirectURL,
       "alaDot1xCPortalPostAuthFailRedirectURL": alaDot1xCPortalPostAuthFailRedirectURL,
       "alaDot1xCPortalDNSKeyword1": alaDot1xCPortalDNSKeyword1,
       "alaDot1xCPortalDNSKeyword2": alaDot1xCPortalDNSKeyword2,
       "alaDot1xCPortalDNSKeyword3": alaDot1xCPortalDNSKeyword3,
       "alaDot1xCPortalDNSKeyword4": alaDot1xCPortalDNSKeyword4,
       "alaDot1xCPortalProxyPort": alaDot1xCPortalProxyPort,
       "alaDot1xCPortalRedirectString": alaDot1xCPortalRedirectString,
       "alaDot1xDeviceStatusTable": alaDot1xDeviceStatusTable,
       "alaDot1xDeviceStatusEntry": alaDot1xDeviceStatusEntry,
       "alaDot1xDeviceStatusMacQueryType": alaDot1xDeviceStatusMacQueryType,
       "alaDot1xDeviceStatusSlotNumber": alaDot1xDeviceStatusSlotNumber,
       "alaDot1xDeviceStatusPortNumber": alaDot1xDeviceStatusPortNumber,
       "alaDot1xDeviceStatusMACAddress": alaDot1xDeviceStatusMACAddress,
       "alaDot1xDeviceStatusDeviceType": alaDot1xDeviceStatusDeviceType,
       "alaDot1xDeviceStatusVlan": alaDot1xDeviceStatusVlan,
       "alaDot1xDeviceStatusIPAddress": alaDot1xDeviceStatusIPAddress,
       "alaDot1xDeviceStatusUserName": alaDot1xDeviceStatusUserName,
       "alaDot1xDeviceStatusProfileUsed": alaDot1xDeviceStatusProfileUsed,
       "alaDot1xDeviceStatusAuthType": alaDot1xDeviceStatusAuthType,
       "alaDot1xDeviceStatusPolicyUsed": alaDot1xDeviceStatusPolicyUsed,
       "alaDot1xDeviceStatusAuthResult": alaDot1xDeviceStatusAuthResult,
       "alaDot1xDeviceStatusMacLearntState": alaDot1xDeviceStatusMacLearntState,
       "alaDot1xDeviceStatusTimeLearned": alaDot1xDeviceStatusTimeLearned,
       "alaDot1xDeviceStatusCaptivePortalUsed": alaDot1xDeviceStatusCaptivePortalUsed,
       "alaDot1xDeviceStatusHicResult": alaDot1xDeviceStatusHicResult,
       "alaDot1xAdminLogoutParams": alaDot1xAdminLogoutParams,
       "alaDot1xAdminLogoutType": alaDot1xAdminLogoutType,
       "alaDot1xAdminLogoutMacAddress": alaDot1xAdminLogoutMacAddress,
       "alaDot1xAdminLogoutUserName": alaDot1xAdminLogoutUserName,
       "alaDot1xAdminLogoutNetworkProfileName": alaDot1xAdminLogoutNetworkProfileName,
       "alaDot1xAdminLogoutInterfaceId": alaDot1xAdminLogoutInterfaceId,
       "alaDot1xAuthServerTimeout": alaDot1xAuthServerTimeout,
       "alaDot1xAuthSvrTimeoutPolicy": alaDot1xAuthSvrTimeoutPolicy,
       "alaDot1xAuthSvrTimeoutReAuthPeriod": alaDot1xAuthSvrTimeoutReAuthPeriod,
       "alaDot1xAuthSvrTimeoutStatus": alaDot1xAuthSvrTimeoutStatus,
       "alaDot1xAuthSvrTimeoutVoicePolicy": alaDot1xAuthSvrTimeoutVoicePolicy,
       "alaDot1xAuthSvrPollingStatus": alaDot1xAuthSvrPollingStatus,
       "alaDot1xAuthSvrDownMacPersistency": alaDot1xAuthSvrDownMacPersistency,
       "alaDot1xDelayLearningPeriod": alaDot1xDelayLearningPeriod,
       "alaDot1xAPModeStatus": alaDot1xAPModeStatus,
       "alaDot1xEAPVersionStatus": alaDot1xEAPVersionStatus,
       "alaDot1xForceL3Learning": alaDot1xForceL3Learning,
       "alaDot1xForceL3LearningPortBounce": alaDot1xForceL3LearningPortBounce,
       "alaPassthroughConfig": alaPassthroughConfig,
       "alaDot1xPassthroughStatus": alaDot1xPassthroughStatus,
       "alaAvlanPassthroughStatus": alaAvlanPassthroughStatus,
       "alaCportalPassthroughStatus": alaCportalPassthroughStatus,
       "alaKerberosPortTable": alaKerberosPortTable,
       "alaKerberosPortEntry": alaKerberosPortEntry,
       "alaKerberosPortIfIndex": alaKerberosPortIfIndex,
       "alaKerberosPortStatus": alaKerberosPortStatus,
       "alaDot1xCrlUnpTable": alaDot1xCrlUnpTable,
       "alaDot1xCrlUnpEntry": alaDot1xCrlUnpEntry,
       "alaDot1xCrlIfIndex": alaDot1xCrlIfIndex,
       "alaDot1xCrlIngBw": alaDot1xCrlIngBw,
       "alaDot1xCrlEgrBw": alaDot1xCrlEgrBw,
       "alaDot1xCrlIngTypeFlag": alaDot1xCrlIngTypeFlag,
       "alaDot1xCrlEgrTypeFlag": alaDot1xCrlEgrTypeFlag,
       "alaDot1xCrlDefDepth": alaDot1xCrlDefDepth,
       "alaDot1xCrlIngProfile": alaDot1xCrlIngProfile,
       "alaDot1xCrlEgrProfile": alaDot1xCrlEgrProfile,
       "alaRedirectByodHostTable": alaRedirectByodHostTable,
       "alaRedirectByodHostEntry": alaRedirectByodHostEntry,
       "alaByodHostStateQueryType": alaByodHostStateQueryType,
       "alaByodHostStateSlotNumber": alaByodHostStateSlotNumber,
       "alaByodHostStatePortNumber": alaByodHostStatePortNumber,
       "alaByodHostStateMacAddress": alaByodHostStateMacAddress,
       "alaByodHostStateDeviceType": alaByodHostStateDeviceType,
       "alaByodHostProgressStatus": alaByodHostProgressStatus,
       "alaRedirectByodHostUnpTable": alaRedirectByodHostUnpTable,
       "alaRedirectByodHostUnpEntry": alaRedirectByodHostUnpEntry,
       "alaByodClientMacQueryType": alaByodClientMacQueryType,
       "alaByodClientSlotNumber": alaByodClientSlotNumber,
       "alaByodClientPortNumber": alaByodClientPortNumber,
       "alaByodClientMacAddress": alaByodClientMacAddress,
       "alaByodClientDeviceType": alaByodClientDeviceType,
       "alaByodPreviousUNP": alaByodPreviousUNP,
       "alaByodNewUNP": alaByodNewUNP,
       "alaByodCOAStatus": alaByodCOAStatus,
       "alaIND1Dot1XMIBConformance": alaIND1Dot1XMIBConformance,
       "alaIND1Dot1XMIBGroups": alaIND1Dot1XMIBGroups,
       "alaDot1xPortLookupGroup": alaDot1xPortLookupGroup,
       "alaINDDot1XPolicyGroup": alaINDDot1XPolicyGroup,
       "alaINDDot1XDeviceStatusGroup": alaINDDot1XDeviceStatusGroup,
       "alaDot1xAuthSvrTimeoutGroup": alaDot1xAuthSvrTimeoutGroup,
       "alaPassthroughConfigGroup": alaPassthroughConfigGroup,
       "alaDot1xAdminLogoutParamsGroup": alaDot1xAdminLogoutParamsGroup,
       "alaDot1xNonSupplicantEntryGroup": alaDot1xNonSupplicantEntryGroup,
       "alaDot1xCportalConfigGroup": alaDot1xCportalConfigGroup,
       "alaDot1xMacEntryGroup": alaDot1xMacEntryGroup,
       "alaKerberosPortGroup": alaKerberosPortGroup,
       "alaDot1xCrlUnpStatusGroup": alaDot1xCrlUnpStatusGroup,
       "alaINDDot1XRedirectByodHostGroup": alaINDDot1XRedirectByodHostGroup,
       "alaINDDot1XRedirectByodHostUnpGroup": alaINDDot1XRedirectByodHostUnpGroup,
       "alaIND1Dot1XMIBCompliances": alaIND1Dot1XMIBCompliances}
)
