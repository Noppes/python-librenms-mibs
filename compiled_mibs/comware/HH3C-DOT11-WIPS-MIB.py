# SNMP MIB module (HH3C-DOT11-WIPS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\comware\HH3C-DOT11-WIPS-MIB

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

(hh3cDot11,) = mibBuilder.importSymbols(
    "HH3C-OID-MIB",
    "hh3cDot11")

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

hh3cDot11WIPS = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 15)
)
if mibBuilder.loadTexts:
    hh3cDot11WIPS.setRevisions(
        ("2016-03-28 09:51",
         "2016-02-16 10:51",
         "2015-12-08 15:51",
         "2015-03-31 13:51")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class Hh3cDot11WIPSEnabledStatus(TextualConvention, Integer32):
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



class Hh3cDot11WIPSRtLmtType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              4)
        )
    )
    namedValues = NamedValues(
        *(("ap", 1),
          ("client", 4))
    )



class Hh3cDot11WIPSDeviceType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ap", 1),
          ("client", 2))
    )



class Hh3cDot11WIPSPolicyTypeValue(TextualConvention, Integer32):
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
        *(("classification", 1),
          ("countermeasure", 2),
          ("detect", 3),
          ("signature", 4))
    )



class Hh3cDot11WIPSClassifyType(TextualConvention, Integer32):
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
              12,
              13,
              14,
              15)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("authorizedap", 2),
          ("misconfiguredap", 3),
          ("rogueap", 4),
          ("externalap", 5),
          ("adhoc", 6),
          ("meshap", 7),
          ("potentialauthorizedap", 8),
          ("potentialrogueap", 9),
          ("potentialexternalap", 10),
          ("uncategorizedap", 11),
          ("authorizedclient", 12),
          ("unauthorizedclient", 13),
          ("misassociaionclient", 14),
          ("uncategorizedclient", 15))
    )



class Hh3cDot11WIPSRadioType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4,
              8,
              16,
              32,
              64,
              128)
        )
    )
    namedValues = NamedValues(
        *(("dot11a", 1),
          ("dot11b", 2),
          ("dot11g", 4),
          ("dot11n", 8),
          ("dot11gn", 16),
          ("dot11an", 32),
          ("dot11ac", 64),
          ("dot11gac", 128))
    )



class Hh3cDot11WIPSDevStatus(TextualConvention, Integer32):
    status = "current"
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



class Hh3cDot11WIPSAPType(TextualConvention, Integer32):
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
        *(("normal", 1),
          ("adhoc", 2),
          ("mesh", 3))
    )



class Hh3cDot11WIPSDevClassifyWay(TextualConvention, Integer32):
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
              7)
        )
    )
    namedValues = NamedValues(
        *(("manual", 1),
          ("invalidOUI", 2),
          ("trustlist", 3),
          ("blocklist", 4),
          ("associated", 5),
          ("userdefined", 6),
          ("auto", 7))
    )



class Hh3cDot11WIPSAPClassifyType(TextualConvention, Integer32):
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
              10)
        )
    )
    namedValues = NamedValues(
        *(("authorized", 1),
          ("misconfigured", 2),
          ("rogue", 3),
          ("external", 4),
          ("adhoc", 5),
          ("mesh", 6),
          ("potentialAuthorized", 7),
          ("potentialRogue", 8),
          ("potentialExternal", 9),
          ("uncategorized", 10))
    )



class Hh3cDot11WIPSStaClassifyType(TextualConvention, Integer32):
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
        *(("authorized", 1),
          ("unauthorized", 2),
          ("misassociated", 3),
          ("uncategorized", 4))
    )



class Hh3cDot11WIPSChannel(TextualConvention, Integer32):
    status = "current"
    displayHint = "d"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 224),
    )



class Hh3cDot11WIPSEncryptMethod(TextualConvention, Integer32):
    status = "current"
    displayHint = "d"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )



class Hh3cDot11WIPSAuthMethod(TextualConvention, Integer32):
    status = "current"
    displayHint = "d"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )



class Hh3cDot11WIPSAPSecurityType(TextualConvention, Integer32):
    status = "current"
    displayHint = "d"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )



class Hh3cDot11WIPSMalformedType(TextualConvention, Integer32):
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
              13,
              14,
              15,
              16)
        )
    )
    namedValues = NamedValues(
        *(("duplicatedie", 1),
          ("fatajack", 2),
          ("illegalibssess", 3),
          ("invalidaddresscombination", 4),
          ("invalidassocreq", 5),
          ("invalidauth", 6),
          ("invaliddeauthcode", 7),
          ("invaliddisassoccode", 8),
          ("invalidhtie", 9),
          ("invalidielength", 10),
          ("invalidpktlength", 11),
          ("nullproberesp", 13),
          ("overfloweapolkey", 14),
          ("overflowssid", 15),
          ("redundantie", 16))
    )



class Hh3cDot11WIPSCtmType(TextualConvention, Integer32):
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
        *(("externalAp", 1),
          ("misassociationClient", 2),
          ("misconfiguredAp", 3),
          ("potentialAuthorizedAp", 4),
          ("potentialExternalAp", 5),
          ("potentialRogueAp", 6),
          ("rogueAp", 7),
          ("unauthorizedClient", 8),
          ("uncategorizedAp", 9),
          ("uncategorizedClient", 10),
          ("attack", 11),
          ("adhoc", 12))
    )



class Hh3cDot11WIPSRuleTypes(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("signature", 4),
          ("apclassfication", 5))
    )



class Hh3cDot11WIPSSigFrameTypes(TextualConvention, Integer32):
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
        *(("management", 1),
          ("control", 2),
          ("data", 3))
    )



class Hh3cDot11WIPSSigFrameSubTypes(TextualConvention, Integer32):
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
              7)
        )
    )
    namedValues = NamedValues(
        *(("assocerq", 1),
          ("assocresp", 2),
          ("probereq", 3),
          ("beacon", 4),
          ("disasso", 5),
          ("auth", 6),
          ("deauth", 7))
    )



class Hh3cDot11WIPSSigSsidMatchTypes(TextualConvention, Integer32):
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
        *(("equal", 1),
          ("notequal", 2),
          ("include", 3),
          ("notinclude", 4))
    )



class Hh3cDot11WIPSSigMacMacType(TextualConvention, Integer32):
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
        *(("source", 1),
          ("destination", 2),
          ("bssid", 3))
    )



class Hh3cDot11WIPSManualAPType(TextualConvention, Integer32):
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
        *(("authap", 1),
          ("misconfiguredap", 2),
          ("rogueap", 3),
          ("externalap", 4))
    )



class Hh3cDot11WIPSDtcAckTypes(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              4,
              6,
              7,
              8,
              11,
              12,
              13,
              14,
              16,
              17,
              18,
              19,
              20,
              22,
              23,
              25)
        )
    )
    namedValues = NamedValues(
        *(("apspoof", 1),
          ("clientspoof", 4),
          ("weakiv", 6),
          ("windowsbridge", 7),
          ("fortymhz", 8),
          ("omerta", 11),
          ("disassoc", 12),
          ("deauth", 13),
          ("prohibitedchannel", 14),
          ("authunencryptedap", 16),
          ("authunencryptedclient", 17),
          ("hotspot", 18),
          ("greenmode", 19),
          ("tableoverflow", 20),
          ("mitm", 22),
          ("wirelessbridge", 23),
          ("apchannelchange", 25))
    )



class Hh3cDot11WIPSDtcDevTimeTypes(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("deviceap", 1),
          ("deviceclient", 2))
    )



class Hh3cDot11WIPSFldDctType(TextualConvention, Integer32):
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
              12,
              13,
              14,
              15)
        )
    )
    namedValues = NamedValues(
        *(("associationrequest", 1),
          ("authentication", 2),
          ("beacon", 3),
          ("blockack", 4),
          ("cts", 5),
          ("deauthentication", 6),
          ("disassociation", 7),
          ("eapolstart", 8),
          ("nulldata", 9),
          ("proberequest", 10),
          ("reassociationrequest", 11),
          ("rts", 12),
          ("eapollogoff", 13),
          ("eapfailure", 14),
          ("eapsuccess", 15))
    )



class Hh3cDot11WIPSAPClaAuthMethods(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              5)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("dot1x", 2),
          ("psk", 3),
          ("other", 5))
    )



class Hh3cDot11WIPSAPClassifyCmpType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              3)
        )
    )
    namedValues = NamedValues(
        *(("equal", 1),
          ("include", 3))
    )



class Hh3cDot11WIPSAPClasSsidCmpType(TextualConvention, Integer32):
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
        *(("equal", 1),
          ("notequal", 2),
          ("include", 3),
          ("notinclude", 4))
    )



class Hh3cDot11WIPSAPClaSecurityType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              9)
        )
    )
    namedValues = NamedValues(
        *(("clear", 1),
          ("wpa2", 2),
          ("wpa", 3),
          ("wep", 9))
    )



class Hh3cDot11WIPSAlyAPClaRuleType(TextualConvention, Integer32):
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
        *(("rogue", 1),
          ("external", 2),
          ("misconfigured", 3),
          ("authorized", 4))
    )



class Hh3cDot11WIPSOuiAddress(TextualConvention, OctetString):
    status = "current"
    displayHint = "1x:"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 3),
    )
    fixed_length = 3



# MIB Managed Objects in the order of their OIDs

_Hh3cDot11WIPSConfigGroup_ObjectIdentity = ObjectIdentity
hh3cDot11WIPSConfigGroup = _Hh3cDot11WIPSConfigGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 15, 1)
)
_Hh3cDot11WIPSVsdTable_Object = MibTable
hh3cDot11WIPSVsdTable = _Hh3cDot11WIPSVsdTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 15, 1, 1)
)
if mibBuilder.loadTexts:
    hh3cDot11WIPSVsdTable.setStatus("current")
_Hh3cDot11WIPSVsdEntry_Object = MibTableRow
hh3cDot11WIPSVsdEntry = _Hh3cDot11WIPSVsdEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 15, 1, 1, 1)
)
hh3cDot11WIPSVsdEntry.setIndexNames(
    (0, "HH3C-DOT11-WIPS-MIB", "hh3cDot11WIPSVsdName"),
)
if mibBuilder.loadTexts:
    hh3cDot11WIPSVsdEntry.setStatus("current")


class _Hh3cDot11WIPSVsdName_Type(OctetString):
    """Custom type hh3cDot11WIPSVsdName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 63),
    )


_Hh3cDot11WIPSVsdName_Type.__name__ = "OctetString"
_Hh3cDot11WIPSVsdName_Object = MibTableColumn
hh3cDot11WIPSVsdName = _Hh3cDot11WIPSVsdName_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 15, 1, 1, 1, 1),
    _Hh3cDot11WIPSVsdName_Type()
)
hh3cDot11WIPSVsdName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cDot11WIPSVsdName.setStatus("current")
_Hh3cDot11WIPSVsdRowStatus_Type = RowStatus
_Hh3cDot11WIPSVsdRowStatus_Object = MibTableColumn
hh3cDot11WIPSVsdRowStatus = _Hh3cDot11WIPSVsdRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 15, 1, 1, 1, 2),
    _Hh3cDot11WIPSVsdRowStatus_Type()
)
hh3cDot11WIPSVsdRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cDot11WIPSVsdRowStatus.setStatus("current")


class _Hh3cDot11WIPSVsdDetectPolicy_Type(OctetString):
    """Custom type hh3cDot11WIPSVsdDetectPolicy based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_Hh3cDot11WIPSVsdDetectPolicy_Type.__name__ = "OctetString"
_Hh3cDot11WIPSVsdDetectPolicy_Object = MibTableColumn
hh3cDot11WIPSVsdDetectPolicy = _Hh3cDot11WIPSVsdDetectPolicy_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 15, 1, 1, 1, 3),
    _Hh3cDot11WIPSVsdDetectPolicy_Type()
)
hh3cDot11WIPSVsdDetectPolicy.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cDot11WIPSVsdDetectPolicy.setStatus("current")


class _Hh3cDot11WIPSVsdCtmPolicy_Type(OctetString):
    """Custom type hh3cDot11WIPSVsdCtmPolicy based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_Hh3cDot11WIPSVsdCtmPolicy_Type.__name__ = "OctetString"
_Hh3cDot11WIPSVsdCtmPolicy_Object = MibTableColumn
hh3cDot11WIPSVsdCtmPolicy = _Hh3cDot11WIPSVsdCtmPolicy_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 15, 1, 1, 1, 4),
    _Hh3cDot11WIPSVsdCtmPolicy_Type()
)
hh3cDot11WIPSVsdCtmPolicy.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cDot11WIPSVsdCtmPolicy.setStatus("current")


class _Hh3cDot11WIPSVsdSignaturePolicy_Type(OctetString):
    """Custom type hh3cDot11WIPSVsdSignaturePolicy based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_Hh3cDot11WIPSVsdSignaturePolicy_Type.__name__ = "OctetString"
_Hh3cDot11WIPSVsdSignaturePolicy_Object = MibTableColumn
hh3cDot11WIPSVsdSignaturePolicy = _Hh3cDot11WIPSVsdSignaturePolicy_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 15, 1, 1, 1, 5),
    _Hh3cDot11WIPSVsdSignaturePolicy_Type()
)
hh3cDot11WIPSVsdSignaturePolicy.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cDot11WIPSVsdSignaturePolicy.setStatus("current")


class _Hh3cDot11WIPSVsdClasPolicy_Type(OctetString):
    """Custom type hh3cDot11WIPSVsdClasPolicy based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_Hh3cDot11WIPSVsdClasPolicy_Type.__name__ = "OctetString"
_Hh3cDot11WIPSVsdClasPolicy_Object = MibTableColumn
hh3cDot11WIPSVsdClasPolicy = _Hh3cDot11WIPSVsdClasPolicy_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 15, 1, 1, 1, 6),
    _Hh3cDot11WIPSVsdClasPolicy_Type()
)
hh3cDot11WIPSVsdClasPolicy.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cDot11WIPSVsdClasPolicy.setStatus("current")
_Hh3cDot11WIPSAp2VsdTable_Object = MibTable
hh3cDot11WIPSAp2VsdTable = _Hh3cDot11WIPSAp2VsdTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 15, 1, 2)
)
if mibBuilder.loadTexts:
    hh3cDot11WIPSAp2VsdTable.setStatus("current")
_Hh3cDot11WIPSAp2VsdEntry_Object = MibTableRow
hh3cDot11WIPSAp2VsdEntry = _Hh3cDot11WIPSAp2VsdEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 15, 1, 2, 1)
)
hh3cDot11WIPSAp2VsdEntry.setIndexNames(
    (0, "HH3C-DOT11-WIPS-MIB", "hh3cDot11WIPSAp2VsdApName"),
)
if mibBuilder.loadTexts:
    hh3cDot11WIPSAp2VsdEntry.setStatus("current")


class _Hh3cDot11WIPSAp2VsdApName_Type(OctetString):
    """Custom type hh3cDot11WIPSAp2VsdApName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_Hh3cDot11WIPSAp2VsdApName_Type.__name__ = "OctetString"
_Hh3cDot11WIPSAp2VsdApName_Object = MibTableColumn
hh3cDot11WIPSAp2VsdApName = _Hh3cDot11WIPSAp2VsdApName_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 15, 1, 2, 1, 1),
    _Hh3cDot11WIPSAp2VsdApName_Type()
)
hh3cDot11WIPSAp2VsdApName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cDot11WIPSAp2VsdApName.setStatus("current")
_Hh3cDot11WIPSAp2VsdRowStatus_Type = RowStatus
_Hh3cDot11WIPSAp2VsdRowStatus_Object = MibTableColumn
hh3cDot11WIPSAp2VsdRowStatus = _Hh3cDot11WIPSAp2VsdRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 15, 1, 2, 1, 2),
    _Hh3cDot11WIPSAp2VsdRowStatus_Type()
)
hh3cDot11WIPSAp2VsdRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cDot11WIPSAp2VsdRowStatus.setStatus("current")


class _Hh3cDot11WIPSAp2VsdVsdName_Type(OctetString):
    """Custom type hh3cDot11WIPSAp2VsdVsdName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 63),
    )


_Hh3cDot11WIPSAp2VsdVsdName_Type.__name__ = "OctetString"
_Hh3cDot11WIPSAp2VsdVsdName_Object = MibTableColumn
hh3cDot11WIPSAp2VsdVsdName = _Hh3cDot11WIPSAp2VsdVsdName_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 15, 1, 2, 1, 3),
    _Hh3cDot11WIPSAp2VsdVsdName_Type()
)
hh3cDot11WIPSAp2VsdVsdName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cDot11WIPSAp2VsdVsdName.setStatus("current")
_Hh3cDot11WIPSApRadioTable_Object = MibTable
hh3cDot11WIPSApRadioTable = _Hh3cDot11WIPSApRadioTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 15, 1, 3)
)
if mibBuilder.loadTexts:
    hh3cDot11WIPSApRadioTable.setStatus("current")
_Hh3cDot11WIPSApRadioEntry_Object = MibTableRow
hh3cDot11WIPSApRadioEntry = _Hh3cDot11WIPSApRadioEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 15, 1, 3, 1)
)
hh3cDot11WIPSApRadioEntry.setIndexNames(
    (0, "HH3C-DOT11-WIPS-MIB", "hh3cDot11WIPSApRadioApName"),
    (0, "HH3C-DOT11-WIPS-MIB", "hh3cDot11WIPSApRadioRadioID"),
)
if mibBuilder.loadTexts:
    hh3cDot11WIPSApRadioEntry.setStatus("current")


class _Hh3cDot11WIPSApRadioApName_Type(OctetString):
    """Custom type hh3cDot11WIPSApRadioApName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_Hh3cDot11WIPSApRadioApName_Type.__name__ = "OctetString"
_Hh3cDot11WIPSApRadioApName_Object = MibTableColumn
hh3cDot11WIPSApRadioApName = _Hh3cDot11WIPSApRadioApName_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 15, 1, 3, 1, 1),
    _Hh3cDot11WIPSApRadioApName_Type()
)
hh3cDot11WIPSApRadioApName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cDot11WIPSApRadioApName.setStatus("current")


class _Hh3cDot11WIPSApRadioRadioID_Type(Integer32):
    """Custom type hh3cDot11WIPSApRadioRadioID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_Hh3cDot11WIPSApRadioRadioID_Type.__name__ = "Integer32"
_Hh3cDot11WIPSApRadioRadioID_Object = MibTableColumn
hh3cDot11WIPSApRadioRadioID = _Hh3cDot11WIPSApRadioRadioID_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 15, 1, 3, 1, 2),
    _Hh3cDot11WIPSApRadioRadioID_Type()
)
hh3cDot11WIPSApRadioRadioID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cDot11WIPSApRadioRadioID.setStatus("current")
_Hh3cDot11WIPSApRadioStatus_Type = Hh3cDot11WIPSEnabledStatus
_Hh3cDot11WIPSApRadioStatus_Object = MibTableColumn
hh3cDot11WIPSApRadioStatus = _Hh3cDot11WIPSApRadioStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 15, 1, 3, 1, 3),
    _Hh3cDot11WIPSApRadioStatus_Type()
)
hh3cDot11WIPSApRadioStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDot11WIPSApRadioStatus.setStatus("current")
_Hh3cDot11WIPSRuleTable_Object = MibTable
hh3cDot11WIPSRuleTable = _Hh3cDot11WIPSRuleTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 15, 1, 4)
)
if mibBuilder.loadTexts:
    hh3cDot11WIPSRuleTable.setStatus("current")
_Hh3cDot11WIPSRuleEntry_Object = MibTableRow
hh3cDot11WIPSRuleEntry = _Hh3cDot11WIPSRuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 15, 1, 4, 1)
)
hh3cDot11WIPSRuleEntry.setIndexNames(
    (0, "HH3C-DOT11-WIPS-MIB", "hh3cDot11WIPSRuleType"),
    (0, "HH3C-DOT11-WIPS-MIB", "hh3cDot11WIPSRuleId"),
)
if mibBuilder.loadTexts:
    hh3cDot11WIPSRuleEntry.setStatus("current")
_Hh3cDot11WIPSRuleType_Type = Hh3cDot11WIPSRuleTypes
_Hh3cDot11WIPSRuleType_Object = MibTableColumn
hh3cDot11WIPSRuleType = _Hh3cDot11WIPSRuleType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 15, 1, 4, 1, 1),
    _Hh3cDot11WIPSRuleType_Type()
)
hh3cDot11WIPSRuleType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cDot11WIPSRuleType.setStatus("current")


class _Hh3cDot11WIPSRuleId_Type(Integer32):
    """Custom type hh3cDot11WIPSRuleId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_Hh3cDot11WIPSRuleId_Type.__name__ = "Integer32"
_Hh3cDot11WIPSRuleId_Object = MibTableColumn
hh3cDot11WIPSRuleId = _Hh3cDot11WIPSRuleId_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 15, 1, 4, 1, 2),
    _Hh3cDot11WIPSRuleId_Type()
)
hh3cDot11WIPSRuleId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cDot11WIPSRuleId.setStatus("current")
_Hh3cDot11WIPSRuleRowStatus_Type = RowStatus
_Hh3cDot11WIPSRuleRowStatus_Object = MibTableColumn
hh3cDot11WIPSRuleRowStatus = _Hh3cDot11WIPSRuleRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 15, 1, 4, 1, 3),
    _Hh3cDot11WIPSRuleRowStatus_Type()
)
hh3cDot11WIPSRuleRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cDot11WIPSRuleRowStatus.setStatus("current")
_Hh3cDot11WIPSAlySigRuleTable_Object = MibTable
hh3cDot11WIPSAlySigRuleTable = _Hh3cDot11WIPSAlySigRuleTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 15, 1, 5)
)
if mibBuilder.loadTexts:
    hh3cDot11WIPSAlySigRuleTable.setStatus("current")
_Hh3cDot11WIPSAlySigRuleEntry_Object = MibTableRow
hh3cDot11WIPSAlySigRuleEntry = _Hh3cDot11WIPSAlySigRuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 15, 1, 5, 1)
)
hh3cDot11WIPSAlySigRuleEntry.setIndexNames(
    (0, "HH3C-DOT11-WIPS-MIB", "hh3cDot11WIPSAlySigPolicyName"),
    (0, "HH3C-DOT11-WIPS-MIB", "hh3cDot11WIPSAlySigRuleID"),
)
if mibBuilder.loadTexts:
    hh3cDot11WIPSAlySigRuleEntry.setStatus("current")


class _Hh3cDot11WIPSAlySigPolicyName_Type(OctetString):
    """Custom type hh3cDot11WIPSAlySigPolicyName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 63),
    )


_Hh3cDot11WIPSAlySigPolicyName_Type.__name__ = "OctetString"
_Hh3cDot11WIPSAlySigPolicyName_Object = MibTableColumn
hh3cDot11WIPSAlySigPolicyName = _Hh3cDot11WIPSAlySigPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 15, 1, 5, 1, 1),
    _Hh3cDot11WIPSAlySigPolicyName_Type()
)
hh3cDot11WIPSAlySigPolicyName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cDot11WIPSAlySigPolicyName.setStatus("current")


class _Hh3cDot11WIPSAlySigRuleID_Type(Integer32):
    """Custom type hh3cDot11WIPSAlySigRuleID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_Hh3cDot11WIPSAlySigRuleID_Type.__name__ = "Integer32"
_Hh3cDot11WIPSAlySigRuleID_Object = MibTableColumn
hh3cDot11WIPSAlySigRuleID = _Hh3cDot11WIPSAlySigRuleID_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 15, 1, 5, 1, 2),
    _Hh3cDot11WIPSAlySigRuleID_Type()
)
hh3cDot11WIPSAlySigRuleID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cDot11WIPSAlySigRuleID.setStatus("current")
_Hh3cDot11WIPSAlySigRowStatus_Type = RowStatus
_Hh3cDot11WIPSAlySigRowStatus_Object = MibTableColumn
hh3cDot11WIPSAlySigRowStatus = _Hh3cDot11WIPSAlySigRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 15, 1, 5, 1, 3),
    _Hh3cDot11WIPSAlySigRowStatus_Type()
)
hh3cDot11WIPSAlySigRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cDot11WIPSAlySigRowStatus.setStatus("current")
_Hh3cDot11WIPSAlyClaRuleTable_Object = MibTable
hh3cDot11WIPSAlyClaRuleTable = _Hh3cDot11WIPSAlyClaRuleTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 15, 1, 6)
)
if mibBuilder.loadTexts:
    hh3cDot11WIPSAlyClaRuleTable.setStatus("current")
_Hh3cDot11WIPSAlyClaRuleEntry_Object = MibTableRow
hh3cDot11WIPSAlyClaRuleEntry = _Hh3cDot11WIPSAlyClaRuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 15, 1, 6, 1)
)
hh3cDot11WIPSAlyClaRuleEntry.setIndexNames(
    (0, "HH3C-DOT11-WIPS-MIB", "hh3cDot11WIPSAlyClaPolicyName"),
    (0, "HH3C-DOT11-WIPS-MIB", "hh3cDot11WIPSAlyClasRuleID"),
)
if mibBuilder.loadTexts:
    hh3cDot11WIPSAlyClaRuleEntry.setStatus("current")


class _Hh3cDot11WIPSAlyClaPolicyName_Type(OctetString):
    """Custom type hh3cDot11WIPSAlyClaPolicyName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 63),
    )


_Hh3cDot11WIPSAlyClaPolicyName_Type.__name__ = "OctetString"
_Hh3cDot11WIPSAlyClaPolicyName_Object = MibTableColumn
hh3cDot11WIPSAlyClaPolicyName = _Hh3cDot11WIPSAlyClaPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 15, 1, 6, 1, 1),
    _Hh3cDot11WIPSAlyClaPolicyName_Type()
)
hh3cDot11WIPSAlyClaPolicyName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cDot11WIPSAlyClaPolicyName.setStatus("current")


class _Hh3cDot11WIPSAlyClasRuleID_Type(Integer32):
    """Custom type hh3cDot11WIPSAlyClasRuleID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_Hh3cDot11WIPSAlyClasRuleID_Type.__name__ = "Integer32"
_Hh3cDot11WIPSAlyClasRuleID_Object = MibTableColumn
hh3cDot11WIPSAlyClasRuleID = _Hh3cDot11WIPSAlyClasRuleID_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 15, 1, 6, 1, 2),
    _Hh3cDot11WIPSAlyClasRuleID_Type()
)
hh3cDot11WIPSAlyClasRuleID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cDot11WIPSAlyClasRuleID.setStatus("current")
_Hh3cDot11WIPSAlyClaRuleType_Type = Hh3cDot11WIPSAlyAPClaRuleType
_Hh3cDot11WIPSAlyClaRuleType_Object = MibTableColumn
hh3cDot11WIPSAlyClaRuleType = _Hh3cDot11WIPSAlyClaRuleType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 15, 1, 6, 1, 3),
    _Hh3cDot11WIPSAlyClaRuleType_Type()
)
hh3cDot11WIPSAlyClaRuleType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cDot11WIPSAlyClaRuleType.setStatus("current")


class _Hh3cDot11WIPSAlyClaRuleLevel_Type(Integer32):
    """Custom type hh3cDot11WIPSAlyClaRuleLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_Hh3cDot11WIPSAlyClaRuleLevel_Type.__name__ = "Integer32"
_Hh3cDot11WIPSAlyClaRuleLevel_Object = MibTableColumn
hh3cDot11WIPSAlyClaRuleLevel = _Hh3cDot11WIPSAlyClaRuleLevel_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 15, 1, 6, 1, 4),
    _Hh3cDot11WIPSAlyClaRuleLevel_Type()
)
hh3cDot11WIPSAlyClaRuleLevel.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cDot11WIPSAlyClaRuleLevel.setStatus("current")
_Hh3cDot11WIPSAlyClaRowStatus_Type = RowStatus
_Hh3cDot11WIPSAlyClaRowStatus_Object = MibTableColumn
hh3cDot11WIPSAlyClaRowStatus = _Hh3cDot11WIPSAlyClaRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 15, 1, 6, 1, 5),
    _Hh3cDot11WIPSAlyClaRowStatus_Type()
)
hh3cDot11WIPSAlyClaRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cDot11WIPSAlyClaRowStatus.setStatus("current")
_Hh3cDot11WIPSTrustMacTable_Object = MibTable
hh3cDot11WIPSTrustMacTable = _Hh3cDot11WIPSTrustMacTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 15, 1, 7)
)
if mibBuilder.loadTexts:
    hh3cDot11WIPSTrustMacTable.setStatus("current")
_Hh3cDot11WIPSTrustMacEntry_Object = MibTableRow
hh3cDot11WIPSTrustMacEntry = _Hh3cDot11WIPSTrustMacEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 15, 1, 7, 1)
)
hh3cDot11WIPSTrustMacEntry.setIndexNames(
    (0, "HH3C-DOT11-WIPS-MIB", "hh3cDot11WIPSTrustMacPolicyName"),
    (0, "HH3C-DOT11-WIPS-MIB", "hh3cDot11WIPSTrustMacAddress"),
)
if mibBuilder.loadTexts:
    hh3cDot11WIPSTrustMacEntry.setStatus("current")


class _Hh3cDot11WIPSTrustMacPolicyName_Type(OctetString):
    """Custom type hh3cDot11WIPSTrustMacPolicyName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 63),
    )


_Hh3cDot11WIPSTrustMacPolicyName_Type.__name__ = "OctetString"
_Hh3cDot11WIPSTrustMacPolicyName_Object = MibTableColumn
hh3cDot11WIPSTrustMacPolicyName = _Hh3cDot11WIPSTrustMacPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 15, 1, 7, 1, 1),
    _Hh3cDot11WIPSTrustMacPolicyName_Type()
)
hh3cDot11WIPSTrustMacPolicyName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cDot11WIPSTrustMacPolicyName.setStatus("current")
_Hh3cDot11WIPSTrustMacAddress_Type = MacAddress
_Hh3cDot11WIPSTrustMacAddress_Object = MibTableColumn
hh3cDot11WIPSTrustMacAddress = _Hh3cDot11WIPSTrustMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 15, 1, 7, 1, 2),
    _Hh3cDot11WIPSTrustMacAddress_Type()
)
hh3cDot11WIPSTrustMacAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cDot11WIPSTrustMacAddress.setStatus("current")
_Hh3cDot11WIPSTrustMacRowStatus_Type = RowStatus
_Hh3cDot11WIPSTrustMacRowStatus_Object = MibTableColumn
hh3cDot11WIPSTrustMacRowStatus = _Hh3cDot11WIPSTrustMacRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 15, 1, 7, 1, 3),
    _Hh3cDot11WIPSTrustMacRowStatus_Type()
)
hh3cDot11WIPSTrustMacRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cDot11WIPSTrustMacRowStatus.setStatus("current")
_Hh3cDot11WIPSBlockMacTable_Object = MibTable
hh3cDot11WIPSBlockMacTable = _Hh3cDot11WIPSBlockMacTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 15, 1, 8)
)
if mibBuilder.loadTexts:
    hh3cDot11WIPSBlockMacTable.setStatus("current")
_Hh3cDot11WIPSBlockMacEntry_Object = MibTableRow
hh3cDot11WIPSBlockMacEntry = _Hh3cDot11WIPSBlockMacEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 15, 1, 8, 1)
)
hh3cDot11WIPSBlockMacEntry.setIndexNames(
    (0, "HH3C-DOT11-WIPS-MIB", "hh3cDot11WIPSBlockMacPolicyName"),
    (0, "HH3C-DOT11-WIPS-MIB", "hh3cDot11WIPSBlockMacAddress"),
)
if mibBuilder.loadTexts:
    hh3cDot11WIPSBlockMacEntry.setStatus("current")


class _Hh3cDot11WIPSBlockMacPolicyName_Type(OctetString):
    """Custom type hh3cDot11WIPSBlockMacPolicyName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 63),
    )


_Hh3cDot11WIPSBlockMacPolicyName_Type.__name__ = "OctetString"
_Hh3cDot11WIPSBlockMacPolicyName_Object = MibTableColumn
hh3cDot11WIPSBlockMacPolicyName = _Hh3cDot11WIPSBlockMacPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 15, 1, 8, 1, 1),
    _Hh3cDot11WIPSBlockMacPolicyName_Type()
)
hh3cDot11WIPSBlockMacPolicyName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cDot11WIPSBlockMacPolicyName.setStatus("current")
_Hh3cDot11WIPSBlockMacAddress_Type = MacAddress
_Hh3cDot11WIPSBlockMacAddress_Object = MibTableColumn
hh3cDot11WIPSBlockMacAddress = _Hh3cDot11WIPSBlockMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 15, 1, 8, 1, 2),
    _Hh3cDot11WIPSBlockMacAddress_Type()
)
hh3cDot11WIPSBlockMacAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cDot11WIPSBlockMacAddress.setStatus("current")
_Hh3cDot11WIPSBlockMacRowStatus_Type = RowStatus
_Hh3cDot11WIPSBlockMacRowStatus_Object = MibTableColumn
hh3cDot11WIPSBlockMacRowStatus = _Hh3cDot11WIPSBlockMacRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 15, 1, 8, 1, 3),
    _Hh3cDot11WIPSBlockMacRowStatus_Type()
)
hh3cDot11WIPSBlockMacRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cDot11WIPSBlockMacRowStatus.setStatus("current")
_Hh3cDot11WIPSManulClaTable_Object = MibTable
hh3cDot11WIPSManulClaTable = _Hh3cDot11WIPSManulClaTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 15, 1, 9)
)
if mibBuilder.loadTexts:
    hh3cDot11WIPSManulClaTable.setStatus("current")
_Hh3cDot11WIPSManulClaEntry_Object = MibTableRow
hh3cDot11WIPSManulClaEntry = _Hh3cDot11WIPSManulClaEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 15, 1, 9, 1)
)
hh3cDot11WIPSManulClaEntry.setIndexNames(
    (0, "HH3C-DOT11-WIPS-MIB", "hh3cDot11WIPSManulClaPlyName"),
    (0, "HH3C-DOT11-WIPS-MIB", "hh3cDot11WIPSManulClaMac"),
)
if mibBuilder.loadTexts:
    hh3cDot11WIPSManulClaEntry.setStatus("current")


class _Hh3cDot11WIPSManulClaPlyName_Type(OctetString):
    """Custom type hh3cDot11WIPSManulClaPlyName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 63),
    )


_Hh3cDot11WIPSManulClaPlyName_Type.__name__ = "OctetString"
_Hh3cDot11WIPSManulClaPlyName_Object = MibTableColumn
hh3cDot11WIPSManulClaPlyName = _Hh3cDot11WIPSManulClaPlyName_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 15, 1, 9, 1, 1),
    _Hh3cDot11WIPSManulClaPlyName_Type()
)
hh3cDot11WIPSManulClaPlyName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cDot11WIPSManulClaPlyName.setStatus("current")
_Hh3cDot11WIPSManulClaMac_Type = MacAddress
_Hh3cDot11WIPSManulClaMac_Object = MibTableColumn
hh3cDot11WIPSManulClaMac = _Hh3cDot11WIPSManulClaMac_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 15, 1, 9, 1, 2),
    _Hh3cDot11WIPSManulClaMac_Type()
)
hh3cDot11WIPSManulClaMac.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cDot11WIPSManulClaMac.setStatus("current")
_Hh3cDot11WIPSManulClassifyType_Type = Hh3cDot11WIPSManualAPType
_Hh3cDot11WIPSManulClassifyType_Object = MibTableColumn
hh3cDot11WIPSManulClassifyType = _Hh3cDot11WIPSManulClassifyType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 15, 1, 9, 1, 3),
    _Hh3cDot11WIPSManulClassifyType_Type()
)
hh3cDot11WIPSManulClassifyType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cDot11WIPSManulClassifyType.setStatus("current")
_Hh3cDot11WIPSManuClaRowStatus_Type = RowStatus
_Hh3cDot11WIPSManuClaRowStatus_Object = MibTableColumn
hh3cDot11WIPSManuClaRowStatus = _Hh3cDot11WIPSManuClaRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 15, 1, 9, 1, 4),
    _Hh3cDot11WIPSManuClaRowStatus_Type()
)
hh3cDot11WIPSManuClaRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cDot11WIPSManuClaRowStatus.setStatus("current")
_Hh3cDot11WIPSTrustOuiTable_Object = MibTable
hh3cDot11WIPSTrustOuiTable = _Hh3cDot11WIPSTrustOuiTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 15, 1, 10)
)
if mibBuilder.loadTexts:
    hh3cDot11WIPSTrustOuiTable.setStatus("current")
_Hh3cDot11WIPSTrustOuiEntry_Object = MibTableRow
hh3cDot11WIPSTrustOuiEntry = _Hh3cDot11WIPSTrustOuiEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 15, 1, 10, 1)
)
hh3cDot11WIPSTrustOuiEntry.setIndexNames(
    (0, "HH3C-DOT11-WIPS-MIB", "hh3cDot11WIPSTrustOuiPolicyName"),
    (0, "HH3C-DOT11-WIPS-MIB", "hh3cDot11WIPSTrustOuiMac"),
)
if mibBuilder.loadTexts:
    hh3cDot11WIPSTrustOuiEntry.setStatus("current")


class _Hh3cDot11WIPSTrustOuiPolicyName_Type(OctetString):
    """Custom type hh3cDot11WIPSTrustOuiPolicyName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 63),
    )


_Hh3cDot11WIPSTrustOuiPolicyName_Type.__name__ = "OctetString"
_Hh3cDot11WIPSTrustOuiPolicyName_Object = MibTableColumn
hh3cDot11WIPSTrustOuiPolicyName = _Hh3cDot11WIPSTrustOuiPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 15, 1, 10, 1, 1),
    _Hh3cDot11WIPSTrustOuiPolicyName_Type()
)
hh3cDot11WIPSTrustOuiPolicyName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cDot11WIPSTrustOuiPolicyName.setStatus("current")
_Hh3cDot11WIPSTrustOuiMac_Type = Hh3cDot11WIPSOuiAddress
_Hh3cDot11WIPSTrustOuiMac_Object = MibTableColumn
hh3cDot11WIPSTrustOuiMac = _Hh3cDot11WIPSTrustOuiMac_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 15, 1, 10, 1, 2),
    _Hh3cDot11WIPSTrustOuiMac_Type()
)
hh3cDot11WIPSTrustOuiMac.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cDot11WIPSTrustOuiMac.setStatus("current")
_Hh3cDot11WIPSTrustOuiRowStatus_Type = RowStatus
_Hh3cDot11WIPSTrustOuiRowStatus_Object = MibTableColumn
hh3cDot11WIPSTrustOuiRowStatus = _Hh3cDot11WIPSTrustOuiRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 15, 1, 10, 1, 3),
    _Hh3cDot11WIPSTrustOuiRowStatus_Type()
)
hh3cDot11WIPSTrustOuiRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cDot11WIPSTrustOuiRowStatus.setStatus("current")
_Hh3cDot11WIPSTrustSSidTable_Object = MibTable
hh3cDot11WIPSTrustSSidTable = _Hh3cDot11WIPSTrustSSidTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 15, 1, 11)
)
if mibBuilder.loadTexts:
    hh3cDot11WIPSTrustSSidTable.setStatus("current")
_Hh3cDot11WIPSTrustSSidEntry_Object = MibTableRow
hh3cDot11WIPSTrustSSidEntry = _Hh3cDot11WIPSTrustSSidEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 15, 1, 11, 1)
)
hh3cDot11WIPSTrustSSidEntry.setIndexNames(
    (0, "HH3C-DOT11-WIPS-MIB", "hh3cDot11WIPSTrustSSidPlyName"),
    (0, "HH3C-DOT11-WIPS-MIB", "hh3cDot11WIPSTrustSSidName"),
)
if mibBuilder.loadTexts:
    hh3cDot11WIPSTrustSSidEntry.setStatus("current")


class _Hh3cDot11WIPSTrustSSidPlyName_Type(OctetString):
    """Custom type hh3cDot11WIPSTrustSSidPlyName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 63),
    )


_Hh3cDot11WIPSTrustSSidPlyName_Type.__name__ = "OctetString"
_Hh3cDot11WIPSTrustSSidPlyName_Object = MibTableColumn
hh3cDot11WIPSTrustSSidPlyName = _Hh3cDot11WIPSTrustSSidPlyName_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 15, 1, 11, 1, 1),
    _Hh3cDot11WIPSTrustSSidPlyName_Type()
)
hh3cDot11WIPSTrustSSidPlyName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cDot11WIPSTrustSSidPlyName.setStatus("current")


class _Hh3cDot11WIPSTrustSSidName_Type(OctetString):
    """Custom type hh3cDot11WIPSTrustSSidName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_Hh3cDot11WIPSTrustSSidName_Type.__name__ = "OctetString"
_Hh3cDot11WIPSTrustSSidName_Object = MibTableColumn
hh3cDot11WIPSTrustSSidName = _Hh3cDot11WIPSTrustSSidName_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 15, 1, 11, 1, 2),
    _Hh3cDot11WIPSTrustSSidName_Type()
)
hh3cDot11WIPSTrustSSidName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cDot11WIPSTrustSSidName.setStatus("current")
_Hh3cDot11WIPSTrustSSidRowStatus_Type = RowStatus
_Hh3cDot11WIPSTrustSSidRowStatus_Object = MibTableColumn
hh3cDot11WIPSTrustSSidRowStatus = _Hh3cDot11WIPSTrustSSidRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 15, 1, 11, 1, 3),
    _Hh3cDot11WIPSTrustSSidRowStatus_Type()
)
hh3cDot11WIPSTrustSSidRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cDot11WIPSTrustSSidRowStatus.setStatus("current")
_Hh3cDot11WIPSMalfDtcTable_Object = MibTable
hh3cDot11WIPSMalfDtcTable = _Hh3cDot11WIPSMalfDtcTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 15, 1, 12)
)
if mibBuilder.loadTexts:
    hh3cDot11WIPSMalfDtcTable.setStatus("current")
_Hh3cDot11WIPSMalfDtcEntry_Object = MibTableRow
hh3cDot11WIPSMalfDtcEntry = _Hh3cDot11WIPSMalfDtcEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 15, 1, 12, 1)
)
hh3cDot11WIPSMalfDtcEntry.setIndexNames(
    (0, "HH3C-DOT11-WIPS-MIB", "hh3cDot11WIPSMalfDtcPolicyName"),
    (0, "HH3C-DOT11-WIPS-MIB", "hh3cDot11WIPSMalfDtcType"),
)
if mibBuilder.loadTexts:
    hh3cDot11WIPSMalfDtcEntry.setStatus("current")


class _Hh3cDot11WIPSMalfDtcPolicyName_Type(OctetString):
    """Custom type hh3cDot11WIPSMalfDtcPolicyName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 63),
    )


_Hh3cDot11WIPSMalfDtcPolicyName_Type.__name__ = "OctetString"
_Hh3cDot11WIPSMalfDtcPolicyName_Object = MibTableColumn
hh3cDot11WIPSMalfDtcPolicyName = _Hh3cDot11WIPSMalfDtcPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 15, 1, 12, 1, 1),
    _Hh3cDot11WIPSMalfDtcPolicyName_Type()
)
hh3cDot11WIPSMalfDtcPolicyName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cDot11WIPSMalfDtcPolicyName.setStatus("current")
_Hh3cDot11WIPSMalfDtcType_Type = Hh3cDot11WIPSMalformedType
_Hh3cDot11WIPSMalfDtcType_Object = MibTableColumn
hh3cDot11WIPSMalfDtcType = _Hh3cDot11WIPSMalfDtcType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 15, 1, 12, 1, 2),
    _Hh3cDot11WIPSMalfDtcType_Type()
)
hh3cDot11WIPSMalfDtcType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cDot11WIPSMalfDtcType.setStatus("current")


class _Hh3cDot11WIPSMalfDtcQuietTime_Type(Integer32):
    """Custom type hh3cDot11WIPSMalfDtcQuietTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 604800),
    )


_Hh3cDot11WIPSMalfDtcQuietTime_Type.__name__ = "Integer32"
_Hh3cDot11WIPSMalfDtcQuietTime_Object = MibTableColumn
hh3cDot11WIPSMalfDtcQuietTime = _Hh3cDot11WIPSMalfDtcQuietTime_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 15, 1, 12, 1, 3),
    _Hh3cDot11WIPSMalfDtcQuietTime_Type()
)
hh3cDot11WIPSMalfDtcQuietTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDot11WIPSMalfDtcQuietTime.setStatus("current")
_Hh3cDot11WIPSMalfDtciStatus_Type = Hh3cDot11WIPSEnabledStatus
_Hh3cDot11WIPSMalfDtciStatus_Object = MibTableColumn
hh3cDot11WIPSMalfDtciStatus = _Hh3cDot11WIPSMalfDtciStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 15, 1, 12, 1, 4),
    _Hh3cDot11WIPSMalfDtciStatus_Type()
)
hh3cDot11WIPSMalfDtciStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDot11WIPSMalfDtciStatus.setStatus("current")
_Hh3cDot11WIPSLgeDutTable_Object = MibTable
hh3cDot11WIPSLgeDutTable = _Hh3cDot11WIPSLgeDutTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 15, 1, 13)
)
if mibBuilder.loadTexts:
    hh3cDot11WIPSLgeDutTable.setStatus("current")
_Hh3cDot11WIPSLgeDutEntry_Object = MibTableRow
hh3cDot11WIPSLgeDutEntry = _Hh3cDot11WIPSLgeDutEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 15, 1, 13, 1)
)
hh3cDot11WIPSLgeDutEntry.setIndexNames(
    (0, "HH3C-DOT11-WIPS-MIB", "hh3cDot11WIPSLgeDutPolicyName"),
)
if mibBuilder.loadTexts:
    hh3cDot11WIPSLgeDutEntry.setStatus("current")


class _Hh3cDot11WIPSLgeDutPolicyName_Type(OctetString):
    """Custom type hh3cDot11WIPSLgeDutPolicyName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 63),
    )


_Hh3cDot11WIPSLgeDutPolicyName_Type.__name__ = "OctetString"
_Hh3cDot11WIPSLgeDutPolicyName_Object = MibTableColumn
hh3cDot11WIPSLgeDutPolicyName = _Hh3cDot11WIPSLgeDutPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 15, 1, 13, 1, 1),
    _Hh3cDot11WIPSLgeDutPolicyName_Type()
)
hh3cDot11WIPSLgeDutPolicyName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cDot11WIPSLgeDutPolicyName.setStatus("current")


class _Hh3cDot11WIPSLgeDutThreshold_Type(Integer32):
    """Custom type hh3cDot11WIPSLgeDutThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32767),
    )


_Hh3cDot11WIPSLgeDutThreshold_Type.__name__ = "Integer32"
_Hh3cDot11WIPSLgeDutThreshold_Object = MibTableColumn
hh3cDot11WIPSLgeDutThreshold = _Hh3cDot11WIPSLgeDutThreshold_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 15, 1, 13, 1, 2),
    _Hh3cDot11WIPSLgeDutThreshold_Type()
)
hh3cDot11WIPSLgeDutThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDot11WIPSLgeDutThreshold.setStatus("current")


class _Hh3cDot11WIPSLgeDutQuietTime_Type(Integer32):
    """Custom type hh3cDot11WIPSLgeDutQuietTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 604800),
    )


_Hh3cDot11WIPSLgeDutQuietTime_Type.__name__ = "Integer32"
_Hh3cDot11WIPSLgeDutQuietTime_Object = MibTableColumn
hh3cDot11WIPSLgeDutQuietTime = _Hh3cDot11WIPSLgeDutQuietTime_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 15, 1, 13, 1, 3),
    _Hh3cDot11WIPSLgeDutQuietTime_Type()
)
hh3cDot11WIPSLgeDutQuietTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDot11WIPSLgeDutQuietTime.setStatus("current")
_Hh3cDot11WIPSLgeDutStatus_Type = Hh3cDot11WIPSEnabledStatus
_Hh3cDot11WIPSLgeDutStatus_Object = MibTableColumn
hh3cDot11WIPSLgeDutStatus = _Hh3cDot11WIPSLgeDutStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 15, 1, 13, 1, 4),
    _Hh3cDot11WIPSLgeDutStatus_Type()
)
hh3cDot11WIPSLgeDutStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDot11WIPSLgeDutStatus.setStatus("current")
_Hh3cDot11WIPSRtLmtTable_Object = MibTable
hh3cDot11WIPSRtLmtTable = _Hh3cDot11WIPSRtLmtTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 15, 1, 14)
)
if mibBuilder.loadTexts:
    hh3cDot11WIPSRtLmtTable.setStatus("current")
_Hh3cDot11WIPSRtLmtEntry_Object = MibTableRow
hh3cDot11WIPSRtLmtEntry = _Hh3cDot11WIPSRtLmtEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 15, 1, 14, 1)
)
hh3cDot11WIPSRtLmtEntry.setIndexNames(
    (0, "HH3C-DOT11-WIPS-MIB", "hh3cDot11WIPSRtLmtPolicyName"),
    (0, "HH3C-DOT11-WIPS-MIB", "hh3cDot11WIPSRtLmtRtLmtType"),
)
if mibBuilder.loadTexts:
    hh3cDot11WIPSRtLmtEntry.setStatus("current")


class _Hh3cDot11WIPSRtLmtPolicyName_Type(OctetString):
    """Custom type hh3cDot11WIPSRtLmtPolicyName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 63),
    )


_Hh3cDot11WIPSRtLmtPolicyName_Type.__name__ = "OctetString"
_Hh3cDot11WIPSRtLmtPolicyName_Object = MibTableColumn
hh3cDot11WIPSRtLmtPolicyName = _Hh3cDot11WIPSRtLmtPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 15, 1, 14, 1, 1),
    _Hh3cDot11WIPSRtLmtPolicyName_Type()
)
hh3cDot11WIPSRtLmtPolicyName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cDot11WIPSRtLmtPolicyName.setStatus("current")
_Hh3cDot11WIPSRtLmtRtLmtType_Type = Hh3cDot11WIPSRtLmtType
_Hh3cDot11WIPSRtLmtRtLmtType_Object = MibTableColumn
hh3cDot11WIPSRtLmtRtLmtType = _Hh3cDot11WIPSRtLmtRtLmtType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 15, 1, 14, 1, 2),
    _Hh3cDot11WIPSRtLmtRtLmtType_Type()
)
hh3cDot11WIPSRtLmtRtLmtType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cDot11WIPSRtLmtRtLmtType.setStatus("current")


class _Hh3cDot11WIPSRtLmtInterval_Type(Integer32):
    """Custom type hh3cDot11WIPSRtLmtInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3600),
    )


_Hh3cDot11WIPSRtLmtInterval_Type.__name__ = "Integer32"
_Hh3cDot11WIPSRtLmtInterval_Object = MibTableColumn
hh3cDot11WIPSRtLmtInterval = _Hh3cDot11WIPSRtLmtInterval_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 15, 1, 14, 1, 3),
    _Hh3cDot11WIPSRtLmtInterval_Type()
)
hh3cDot11WIPSRtLmtInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDot11WIPSRtLmtInterval.setStatus("current")


class _Hh3cDot11WIPSRtLmtThreshold_Type(Integer32):
    """Custom type hh3cDot11WIPSRtLmtThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4096),
    )


_Hh3cDot11WIPSRtLmtThreshold_Type.__name__ = "Integer32"
_Hh3cDot11WIPSRtLmtThreshold_Object = MibTableColumn
hh3cDot11WIPSRtLmtThreshold = _Hh3cDot11WIPSRtLmtThreshold_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 15, 1, 14, 1, 4),
    _Hh3cDot11WIPSRtLmtThreshold_Type()
)
hh3cDot11WIPSRtLmtThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDot11WIPSRtLmtThreshold.setStatus("current")


class _Hh3cDot11WIPSRtLmtQuiet_Type(Integer32):
    """Custom type hh3cDot11WIPSRtLmtQuiet based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1200, 3600),
    )


_Hh3cDot11WIPSRtLmtQuiet_Type.__name__ = "Integer32"
_Hh3cDot11WIPSRtLmtQuiet_Object = MibTableColumn
hh3cDot11WIPSRtLmtQuiet = _Hh3cDot11WIPSRtLmtQuiet_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 15, 1, 14, 1, 5),
    _Hh3cDot11WIPSRtLmtQuiet_Type()
)
hh3cDot11WIPSRtLmtQuiet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDot11WIPSRtLmtQuiet.setStatus("current")
_Hh3cDot11WIPSRtLmtStatus_Type = Hh3cDot11WIPSEnabledStatus
_Hh3cDot11WIPSRtLmtStatus_Object = MibTableColumn
hh3cDot11WIPSRtLmtStatus = _Hh3cDot11WIPSRtLmtStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 15, 1, 14, 1, 6),
    _Hh3cDot11WIPSRtLmtStatus_Type()
)
hh3cDot11WIPSRtLmtStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDot11WIPSRtLmtStatus.setStatus("current")
_Hh3cDot11WIPSDtcAckTable_Object = MibTable
hh3cDot11WIPSDtcAckTable = _Hh3cDot11WIPSDtcAckTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 15, 1, 15)
)
if mibBuilder.loadTexts:
    hh3cDot11WIPSDtcAckTable.setStatus("current")
_Hh3cDot11WIPSDtcAckEntry_Object = MibTableRow
hh3cDot11WIPSDtcAckEntry = _Hh3cDot11WIPSDtcAckEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 15, 1, 15, 1)
)
hh3cDot11WIPSDtcAckEntry.setIndexNames(
    (0, "HH3C-DOT11-WIPS-MIB", "hh3cDot11WIPSDtcAckPolicyName"),
    (0, "HH3C-DOT11-WIPS-MIB", "hh3cDot11WIPSDtcAckType"),
)
if mibBuilder.loadTexts:
    hh3cDot11WIPSDtcAckEntry.setStatus("current")


class _Hh3cDot11WIPSDtcAckPolicyName_Type(OctetString):
    """Custom type hh3cDot11WIPSDtcAckPolicyName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 63),
    )


_Hh3cDot11WIPSDtcAckPolicyName_Type.__name__ = "OctetString"
_Hh3cDot11WIPSDtcAckPolicyName_Object = MibTableColumn
hh3cDot11WIPSDtcAckPolicyName = _Hh3cDot11WIPSDtcAckPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 15, 1, 15, 1, 1),
    _Hh3cDot11WIPSDtcAckPolicyName_Type()
)
hh3cDot11WIPSDtcAckPolicyName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cDot11WIPSDtcAckPolicyName.setStatus("current")
_Hh3cDot11WIPSDtcAckType_Type = Hh3cDot11WIPSDtcAckTypes
_Hh3cDot11WIPSDtcAckType_Object = MibTableColumn
hh3cDot11WIPSDtcAckType = _Hh3cDot11WIPSDtcAckType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 15, 1, 15, 1, 2),
    _Hh3cDot11WIPSDtcAckType_Type()
)
hh3cDot11WIPSDtcAckType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cDot11WIPSDtcAckType.setStatus("current")


class _Hh3cDot11WIPSDtcAckQuietTime_Type(Integer32):
    """Custom type hh3cDot11WIPSDtcAckQuietTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 604800),
    )


_Hh3cDot11WIPSDtcAckQuietTime_Type.__name__ = "Integer32"
_Hh3cDot11WIPSDtcAckQuietTime_Object = MibTableColumn
hh3cDot11WIPSDtcAckQuietTime = _Hh3cDot11WIPSDtcAckQuietTime_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 15, 1, 15, 1, 3),
    _Hh3cDot11WIPSDtcAckQuietTime_Type()
)
hh3cDot11WIPSDtcAckQuietTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDot11WIPSDtcAckQuietTime.setStatus("current")


class _Hh3cDot11WIPSDtcAckInterval_Type(Integer32):
    """Custom type hh3cDot11WIPSDtcAckInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3600),
    )


_Hh3cDot11WIPSDtcAckInterval_Type.__name__ = "Integer32"
_Hh3cDot11WIPSDtcAckInterval_Object = MibTableColumn
hh3cDot11WIPSDtcAckInterval = _Hh3cDot11WIPSDtcAckInterval_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 15, 1, 15, 1, 4),
    _Hh3cDot11WIPSDtcAckInterval_Type()
)
hh3cDot11WIPSDtcAckInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDot11WIPSDtcAckInterval.setStatus("current")


class _Hh3cDot11WIPSDtcAckThreshold_Type(Integer32):
    """Custom type hh3cDot11WIPSDtcAckThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100000),
    )


_Hh3cDot11WIPSDtcAckThreshold_Type.__name__ = "Integer32"
_Hh3cDot11WIPSDtcAckThreshold_Object = MibTableColumn
hh3cDot11WIPSDtcAckThreshold = _Hh3cDot11WIPSDtcAckThreshold_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 15, 1, 15, 1, 5),
    _Hh3cDot11WIPSDtcAckThreshold_Type()
)
hh3cDot11WIPSDtcAckThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDot11WIPSDtcAckThreshold.setStatus("current")
_Hh3cDot11WIPSDtcAckStatus_Type = Hh3cDot11WIPSEnabledStatus
_Hh3cDot11WIPSDtcAckStatus_Object = MibTableColumn
hh3cDot11WIPSDtcAckStatus = _Hh3cDot11WIPSDtcAckStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 15, 1, 15, 1, 6),
    _Hh3cDot11WIPSDtcAckStatus_Type()
)
hh3cDot11WIPSDtcAckStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDot11WIPSDtcAckStatus.setStatus("current")
_Hh3cDot11WIPSDtcDevTimeTable_Object = MibTable
hh3cDot11WIPSDtcDevTimeTable = _Hh3cDot11WIPSDtcDevTimeTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 15, 1, 16)
)
if mibBuilder.loadTexts:
    hh3cDot11WIPSDtcDevTimeTable.setStatus("current")
_Hh3cDot11WIPSDtcDevTimeEntry_Object = MibTableRow
hh3cDot11WIPSDtcDevTimeEntry = _Hh3cDot11WIPSDtcDevTimeEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 15, 1, 16, 1)
)
hh3cDot11WIPSDtcDevTimeEntry.setIndexNames(
    (0, "HH3C-DOT11-WIPS-MIB", "hh3cDot11WIPSDtcDevTimePlyName"),
    (0, "HH3C-DOT11-WIPS-MIB", "hh3cDot11WIPSDtcDevTimeType"),
)
if mibBuilder.loadTexts:
    hh3cDot11WIPSDtcDevTimeEntry.setStatus("current")


class _Hh3cDot11WIPSDtcDevTimePlyName_Type(OctetString):
    """Custom type hh3cDot11WIPSDtcDevTimePlyName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 63),
    )


_Hh3cDot11WIPSDtcDevTimePlyName_Type.__name__ = "OctetString"
_Hh3cDot11WIPSDtcDevTimePlyName_Object = MibTableColumn
hh3cDot11WIPSDtcDevTimePlyName = _Hh3cDot11WIPSDtcDevTimePlyName_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 15, 1, 16, 1, 1),
    _Hh3cDot11WIPSDtcDevTimePlyName_Type()
)
hh3cDot11WIPSDtcDevTimePlyName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cDot11WIPSDtcDevTimePlyName.setStatus("current")
_Hh3cDot11WIPSDtcDevTimeType_Type = Hh3cDot11WIPSDtcDevTimeTypes
_Hh3cDot11WIPSDtcDevTimeType_Object = MibTableColumn
hh3cDot11WIPSDtcDevTimeType = _Hh3cDot11WIPSDtcDevTimeType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 15, 1, 16, 1, 2),
    _Hh3cDot11WIPSDtcDevTimeType_Type()
)
hh3cDot11WIPSDtcDevTimeType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cDot11WIPSDtcDevTimeType.setStatus("current")


class _Hh3cDot11WIPSDtcDevTimeInactive_Type(Integer32):
    """Custom type hh3cDot11WIPSDtcDevTimeInactive based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(60, 1200),
    )


_Hh3cDot11WIPSDtcDevTimeInactive_Type.__name__ = "Integer32"
_Hh3cDot11WIPSDtcDevTimeInactive_Object = MibTableColumn
hh3cDot11WIPSDtcDevTimeInactive = _Hh3cDot11WIPSDtcDevTimeInactive_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 15, 1, 16, 1, 3),
    _Hh3cDot11WIPSDtcDevTimeInactive_Type()
)
hh3cDot11WIPSDtcDevTimeInactive.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDot11WIPSDtcDevTimeInactive.setStatus("current")


class _Hh3cDot11WIPSDtcDevTimeAging_Type(Integer32):
    """Custom type hh3cDot11WIPSDtcDevTimeAging based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(120, 86400),
    )


_Hh3cDot11WIPSDtcDevTimeAging_Type.__name__ = "Integer32"
_Hh3cDot11WIPSDtcDevTimeAging_Object = MibTableColumn
hh3cDot11WIPSDtcDevTimeAging = _Hh3cDot11WIPSDtcDevTimeAging_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 15, 1, 16, 1, 4),
    _Hh3cDot11WIPSDtcDevTimeAging_Type()
)
hh3cDot11WIPSDtcDevTimeAging.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDot11WIPSDtcDevTimeAging.setStatus("current")
_Hh3cDot11WIPSDtcDevTimeStatus_Type = Hh3cDot11WIPSEnabledStatus
_Hh3cDot11WIPSDtcDevTimeStatus_Object = MibTableColumn
hh3cDot11WIPSDtcDevTimeStatus = _Hh3cDot11WIPSDtcDevTimeStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 15, 1, 16, 1, 5),
    _Hh3cDot11WIPSDtcDevTimeStatus_Type()
)
hh3cDot11WIPSDtcDevTimeStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDot11WIPSDtcDevTimeStatus.setStatus("current")
_Hh3cDot11WIPSApimperTable_Object = MibTable
hh3cDot11WIPSApimperTable = _Hh3cDot11WIPSApimperTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 15, 1, 17)
)
if mibBuilder.loadTexts:
    hh3cDot11WIPSApimperTable.setStatus("current")
_Hh3cDot11WIPSApimperEntry_Object = MibTableRow
hh3cDot11WIPSApimperEntry = _Hh3cDot11WIPSApimperEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 15, 1, 17, 1)
)
hh3cDot11WIPSApimperEntry.setIndexNames(
    (0, "HH3C-DOT11-WIPS-MIB", "hh3cDot11WIPSApimperPolicyName"),
)
if mibBuilder.loadTexts:
    hh3cDot11WIPSApimperEntry.setStatus("current")


class _Hh3cDot11WIPSApimperPolicyName_Type(OctetString):
    """Custom type hh3cDot11WIPSApimperPolicyName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 63),
    )


_Hh3cDot11WIPSApimperPolicyName_Type.__name__ = "OctetString"
_Hh3cDot11WIPSApimperPolicyName_Object = MibTableColumn
hh3cDot11WIPSApimperPolicyName = _Hh3cDot11WIPSApimperPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 15, 1, 17, 1, 1),
    _Hh3cDot11WIPSApimperPolicyName_Type()
)
hh3cDot11WIPSApimperPolicyName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cDot11WIPSApimperPolicyName.setStatus("current")


class _Hh3cDot11WIPSApimperQuiet_Type(Integer32):
    """Custom type hh3cDot11WIPSApimperQuiet based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 604800),
    )


_Hh3cDot11WIPSApimperQuiet_Type.__name__ = "Integer32"
_Hh3cDot11WIPSApimperQuiet_Object = MibTableColumn
hh3cDot11WIPSApimperQuiet = _Hh3cDot11WIPSApimperQuiet_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 15, 1, 17, 1, 2),
    _Hh3cDot11WIPSApimperQuiet_Type()
)
hh3cDot11WIPSApimperQuiet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDot11WIPSApimperQuiet.setStatus("current")
_Hh3cDot11WIPSApimperStatus_Type = Hh3cDot11WIPSEnabledStatus
_Hh3cDot11WIPSApimperStatus_Object = MibTableColumn
hh3cDot11WIPSApimperStatus = _Hh3cDot11WIPSApimperStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 15, 1, 17, 1, 3),
    _Hh3cDot11WIPSApimperStatus_Type()
)
hh3cDot11WIPSApimperStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDot11WIPSApimperStatus.setStatus("current")
_Hh3cDot11WIPSDctSoftApTable_Object = MibTable
hh3cDot11WIPSDctSoftApTable = _Hh3cDot11WIPSDctSoftApTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 15, 1, 18)
)
if mibBuilder.loadTexts:
    hh3cDot11WIPSDctSoftApTable.setStatus("current")
_Hh3cDot11WIPSDctSoftApEntry_Object = MibTableRow
hh3cDot11WIPSDctSoftApEntry = _Hh3cDot11WIPSDctSoftApEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 15, 1, 18, 1)
)
hh3cDot11WIPSDctSoftApEntry.setIndexNames(
    (0, "HH3C-DOT11-WIPS-MIB", "hh3cDot11WIPSDctSoftApPlyName"),
)
if mibBuilder.loadTexts:
    hh3cDot11WIPSDctSoftApEntry.setStatus("current")


class _Hh3cDot11WIPSDctSoftApPlyName_Type(OctetString):
    """Custom type hh3cDot11WIPSDctSoftApPlyName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 63),
    )


_Hh3cDot11WIPSDctSoftApPlyName_Type.__name__ = "OctetString"
_Hh3cDot11WIPSDctSoftApPlyName_Object = MibTableColumn
hh3cDot11WIPSDctSoftApPlyName = _Hh3cDot11WIPSDctSoftApPlyName_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 15, 1, 18, 1, 1),
    _Hh3cDot11WIPSDctSoftApPlyName_Type()
)
hh3cDot11WIPSDctSoftApPlyName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cDot11WIPSDctSoftApPlyName.setStatus("current")


class _Hh3cDot11WIPSDctSoftApThold_Type(Integer32):
    """Custom type hh3cDot11WIPSDctSoftApThold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 600),
    )


_Hh3cDot11WIPSDctSoftApThold_Type.__name__ = "Integer32"
_Hh3cDot11WIPSDctSoftApThold_Object = MibTableColumn
hh3cDot11WIPSDctSoftApThold = _Hh3cDot11WIPSDctSoftApThold_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 15, 1, 18, 1, 2),
    _Hh3cDot11WIPSDctSoftApThold_Type()
)
hh3cDot11WIPSDctSoftApThold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDot11WIPSDctSoftApThold.setStatus("current")
_Hh3cDot11WIPSDctSoftApStatus_Type = Hh3cDot11WIPSEnabledStatus
_Hh3cDot11WIPSDctSoftApStatus_Object = MibTableColumn
hh3cDot11WIPSDctSoftApStatus = _Hh3cDot11WIPSDctSoftApStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 15, 1, 18, 1, 3),
    _Hh3cDot11WIPSDctSoftApStatus_Type()
)
hh3cDot11WIPSDctSoftApStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDot11WIPSDctSoftApStatus.setStatus("current")
_Hh3cDot11WIPSPowerSaveTable_Object = MibTable
hh3cDot11WIPSPowerSaveTable = _Hh3cDot11WIPSPowerSaveTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 15, 1, 19)
)
if mibBuilder.loadTexts:
    hh3cDot11WIPSPowerSaveTable.setStatus("current")
_Hh3cDot11WIPSPowerSaveEntry_Object = MibTableRow
hh3cDot11WIPSPowerSaveEntry = _Hh3cDot11WIPSPowerSaveEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 15, 1, 19, 1)
)
hh3cDot11WIPSPowerSaveEntry.setIndexNames(
    (0, "HH3C-DOT11-WIPS-MIB", "hh3cDot11WIPSPowerSavePlyName"),
)
if mibBuilder.loadTexts:
    hh3cDot11WIPSPowerSaveEntry.setStatus("current")


class _Hh3cDot11WIPSPowerSavePlyName_Type(OctetString):
    """Custom type hh3cDot11WIPSPowerSavePlyName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 63),
    )


_Hh3cDot11WIPSPowerSavePlyName_Type.__name__ = "OctetString"
_Hh3cDot11WIPSPowerSavePlyName_Object = MibTableColumn
hh3cDot11WIPSPowerSavePlyName = _Hh3cDot11WIPSPowerSavePlyName_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 15, 1, 19, 1, 1),
    _Hh3cDot11WIPSPowerSavePlyName_Type()
)
hh3cDot11WIPSPowerSavePlyName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cDot11WIPSPowerSavePlyName.setStatus("current")


class _Hh3cDot11WIPSPowerSaveInterval_Type(Integer32):
    """Custom type hh3cDot11WIPSPowerSaveInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3600),
    )


_Hh3cDot11WIPSPowerSaveInterval_Type.__name__ = "Integer32"
_Hh3cDot11WIPSPowerSaveInterval_Object = MibTableColumn
hh3cDot11WIPSPowerSaveInterval = _Hh3cDot11WIPSPowerSaveInterval_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 15, 1, 19, 1, 2),
    _Hh3cDot11WIPSPowerSaveInterval_Type()
)
hh3cDot11WIPSPowerSaveInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDot11WIPSPowerSaveInterval.setStatus("current")


class _Hh3cDot11WIPSPowerSaveMinOffPkt_Type(Integer32):
    """Custom type hh3cDot11WIPSPowerSaveMinOffPkt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 150),
    )


_Hh3cDot11WIPSPowerSaveMinOffPkt_Type.__name__ = "Integer32"
_Hh3cDot11WIPSPowerSaveMinOffPkt_Object = MibTableColumn
hh3cDot11WIPSPowerSaveMinOffPkt = _Hh3cDot11WIPSPowerSaveMinOffPkt_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 15, 1, 19, 1, 3),
    _Hh3cDot11WIPSPowerSaveMinOffPkt_Type()
)
hh3cDot11WIPSPowerSaveMinOffPkt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDot11WIPSPowerSaveMinOffPkt.setStatus("current")


class _Hh3cDot11WIPSPowerSaveOnOffPct_Type(Integer32):
    """Custom type hh3cDot11WIPSPowerSaveOnOffPct based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Hh3cDot11WIPSPowerSaveOnOffPct_Type.__name__ = "Integer32"
_Hh3cDot11WIPSPowerSaveOnOffPct_Object = MibTableColumn
hh3cDot11WIPSPowerSaveOnOffPct = _Hh3cDot11WIPSPowerSaveOnOffPct_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 15, 1, 19, 1, 4),
    _Hh3cDot11WIPSPowerSaveOnOffPct_Type()
)
hh3cDot11WIPSPowerSaveOnOffPct.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDot11WIPSPowerSaveOnOffPct.setStatus("current")


class _Hh3cDot11WIPSPowerSaveQuiet_Type(Integer32):
    """Custom type hh3cDot11WIPSPowerSaveQuiet based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 604800),
    )


_Hh3cDot11WIPSPowerSaveQuiet_Type.__name__ = "Integer32"
_Hh3cDot11WIPSPowerSaveQuiet_Object = MibTableColumn
hh3cDot11WIPSPowerSaveQuiet = _Hh3cDot11WIPSPowerSaveQuiet_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 15, 1, 19, 1, 5),
    _Hh3cDot11WIPSPowerSaveQuiet_Type()
)
hh3cDot11WIPSPowerSaveQuiet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDot11WIPSPowerSaveQuiet.setStatus("current")
_Hh3cDot11WIPSPowerSaveStatus_Type = Hh3cDot11WIPSEnabledStatus
_Hh3cDot11WIPSPowerSaveStatus_Object = MibTableColumn
hh3cDot11WIPSPowerSaveStatus = _Hh3cDot11WIPSPowerSaveStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 15, 1, 19, 1, 6),
    _Hh3cDot11WIPSPowerSaveStatus_Type()
)
hh3cDot11WIPSPowerSaveStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDot11WIPSPowerSaveStatus.setStatus("current")
_Hh3cDot11WIPSIgnListMacTable_Object = MibTable
hh3cDot11WIPSIgnListMacTable = _Hh3cDot11WIPSIgnListMacTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 15, 1, 20)
)
if mibBuilder.loadTexts:
    hh3cDot11WIPSIgnListMacTable.setStatus("current")
_Hh3cDot11WIPSIgnListMacEntry_Object = MibTableRow
hh3cDot11WIPSIgnListMacEntry = _Hh3cDot11WIPSIgnListMacEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 15, 1, 20, 1)
)
hh3cDot11WIPSIgnListMacEntry.setIndexNames(
    (0, "HH3C-DOT11-WIPS-MIB", "hh3cDot11WIPSIgnListMacMacAddr"),
)
if mibBuilder.loadTexts:
    hh3cDot11WIPSIgnListMacEntry.setStatus("current")
_Hh3cDot11WIPSIgnListMacMacAddr_Type = MacAddress
_Hh3cDot11WIPSIgnListMacMacAddr_Object = MibTableColumn
hh3cDot11WIPSIgnListMacMacAddr = _Hh3cDot11WIPSIgnListMacMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 15, 1, 20, 1, 1),
    _Hh3cDot11WIPSIgnListMacMacAddr_Type()
)
hh3cDot11WIPSIgnListMacMacAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cDot11WIPSIgnListMacMacAddr.setStatus("current")
_Hh3cDot11WIPSIgnListMacRowStus_Type = RowStatus
_Hh3cDot11WIPSIgnListMacRowStus_Object = MibTableColumn
hh3cDot11WIPSIgnListMacRowStus = _Hh3cDot11WIPSIgnListMacRowStus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 15, 1, 20, 1, 2),
    _Hh3cDot11WIPSIgnListMacRowStus_Type()
)
hh3cDot11WIPSIgnListMacRowStus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cDot11WIPSIgnListMacRowStus.setStatus("current")
_Hh3cDot11WIPSHoneyPotTable_Object = MibTable
hh3cDot11WIPSHoneyPotTable = _Hh3cDot11WIPSHoneyPotTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 15, 1, 21)
)
if mibBuilder.loadTexts:
    hh3cDot11WIPSHoneyPotTable.setStatus("current")
_Hh3cDot11WIPSHoneyPotEntry_Object = MibTableRow
hh3cDot11WIPSHoneyPotEntry = _Hh3cDot11WIPSHoneyPotEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 15, 1, 21, 1)
)
hh3cDot11WIPSHoneyPotEntry.setIndexNames(
    (0, "HH3C-DOT11-WIPS-MIB", "hh3cDot11WIPSHoneyPotPlyName"),
)
if mibBuilder.loadTexts:
    hh3cDot11WIPSHoneyPotEntry.setStatus("current")


class _Hh3cDot11WIPSHoneyPotPlyName_Type(OctetString):
    """Custom type hh3cDot11WIPSHoneyPotPlyName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 63),
    )


_Hh3cDot11WIPSHoneyPotPlyName_Type.__name__ = "OctetString"
_Hh3cDot11WIPSHoneyPotPlyName_Object = MibTableColumn
hh3cDot11WIPSHoneyPotPlyName = _Hh3cDot11WIPSHoneyPotPlyName_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 15, 1, 21, 1, 1),
    _Hh3cDot11WIPSHoneyPotPlyName_Type()
)
hh3cDot11WIPSHoneyPotPlyName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cDot11WIPSHoneyPotPlyName.setStatus("current")


class _Hh3cDot11WIPSHoneyPotSim_Type(Integer32):
    """Custom type hh3cDot11WIPSHoneyPotSim based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(70, 100),
    )


_Hh3cDot11WIPSHoneyPotSim_Type.__name__ = "Integer32"
_Hh3cDot11WIPSHoneyPotSim_Object = MibTableColumn
hh3cDot11WIPSHoneyPotSim = _Hh3cDot11WIPSHoneyPotSim_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 15, 1, 21, 1, 2),
    _Hh3cDot11WIPSHoneyPotSim_Type()
)
hh3cDot11WIPSHoneyPotSim.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDot11WIPSHoneyPotSim.setStatus("current")


class _Hh3cDot11WIPSHoneyPotQuiet_Type(Integer32):
    """Custom type hh3cDot11WIPSHoneyPotQuiet based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 604800),
    )


_Hh3cDot11WIPSHoneyPotQuiet_Type.__name__ = "Integer32"
_Hh3cDot11WIPSHoneyPotQuiet_Object = MibTableColumn
hh3cDot11WIPSHoneyPotQuiet = _Hh3cDot11WIPSHoneyPotQuiet_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 15, 1, 21, 1, 3),
    _Hh3cDot11WIPSHoneyPotQuiet_Type()
)
hh3cDot11WIPSHoneyPotQuiet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDot11WIPSHoneyPotQuiet.setStatus("current")
_Hh3cDot11WIPSHoneyPotStatus_Type = Hh3cDot11WIPSEnabledStatus
_Hh3cDot11WIPSHoneyPotStatus_Object = MibTableColumn
hh3cDot11WIPSHoneyPotStatus = _Hh3cDot11WIPSHoneyPotStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 15, 1, 21, 1, 4),
    _Hh3cDot11WIPSHoneyPotStatus_Type()
)
hh3cDot11WIPSHoneyPotStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDot11WIPSHoneyPotStatus.setStatus("current")
_Hh3cDot11WIPSAPFldTable_Object = MibTable
hh3cDot11WIPSAPFldTable = _Hh3cDot11WIPSAPFldTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 15, 1, 22)
)
if mibBuilder.loadTexts:
    hh3cDot11WIPSAPFldTable.setStatus("current")
_Hh3cDot11WIPSAPFldEntry_Object = MibTableRow
hh3cDot11WIPSAPFldEntry = _Hh3cDot11WIPSAPFldEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 15, 1, 22, 1)
)
hh3cDot11WIPSAPFldEntry.setIndexNames(
    (0, "HH3C-DOT11-WIPS-MIB", "hh3cDot11WIPSAPFldPolicyName"),
)
if mibBuilder.loadTexts:
    hh3cDot11WIPSAPFldEntry.setStatus("current")


class _Hh3cDot11WIPSAPFldPolicyName_Type(OctetString):
    """Custom type hh3cDot11WIPSAPFldPolicyName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 63),
    )


_Hh3cDot11WIPSAPFldPolicyName_Type.__name__ = "OctetString"
_Hh3cDot11WIPSAPFldPolicyName_Object = MibTableColumn
hh3cDot11WIPSAPFldPolicyName = _Hh3cDot11WIPSAPFldPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 15, 1, 22, 1, 1),
    _Hh3cDot11WIPSAPFldPolicyName_Type()
)
hh3cDot11WIPSAPFldPolicyName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cDot11WIPSAPFldPolicyName.setStatus("current")


class _Hh3cDot11WIPSAPFldApnum_Type(Integer32):
    """Custom type hh3cDot11WIPSAPFldApnum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 200),
    )


_Hh3cDot11WIPSAPFldApnum_Type.__name__ = "Integer32"
_Hh3cDot11WIPSAPFldApnum_Object = MibTableColumn
hh3cDot11WIPSAPFldApnum = _Hh3cDot11WIPSAPFldApnum_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 15, 1, 22, 1, 2),
    _Hh3cDot11WIPSAPFldApnum_Type()
)
hh3cDot11WIPSAPFldApnum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDot11WIPSAPFldApnum.setStatus("current")


class _Hh3cDot11WIPSAPFldExceed_Type(Integer32):
    """Custom type hh3cDot11WIPSAPFldExceed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 200),
    )


_Hh3cDot11WIPSAPFldExceed_Type.__name__ = "Integer32"
_Hh3cDot11WIPSAPFldExceed_Object = MibTableColumn
hh3cDot11WIPSAPFldExceed = _Hh3cDot11WIPSAPFldExceed_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 15, 1, 22, 1, 3),
    _Hh3cDot11WIPSAPFldExceed_Type()
)
hh3cDot11WIPSAPFldExceed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDot11WIPSAPFldExceed.setStatus("current")


class _Hh3cDot11WIPSAPFldQuiet_Type(Integer32):
    """Custom type hh3cDot11WIPSAPFldQuiet based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 604800),
    )


_Hh3cDot11WIPSAPFldQuiet_Type.__name__ = "Integer32"
_Hh3cDot11WIPSAPFldQuiet_Object = MibTableColumn
hh3cDot11WIPSAPFldQuiet = _Hh3cDot11WIPSAPFldQuiet_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 15, 1, 22, 1, 4),
    _Hh3cDot11WIPSAPFldQuiet_Type()
)
hh3cDot11WIPSAPFldQuiet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDot11WIPSAPFldQuiet.setStatus("current")
_Hh3cDot11WIPSAPFldStatus_Type = Hh3cDot11WIPSEnabledStatus
_Hh3cDot11WIPSAPFldStatus_Object = MibTableColumn
hh3cDot11WIPSAPFldStatus = _Hh3cDot11WIPSAPFldStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 15, 1, 22, 1, 5),
    _Hh3cDot11WIPSAPFldStatus_Type()
)
hh3cDot11WIPSAPFldStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDot11WIPSAPFldStatus.setStatus("current")
_Hh3cDot11WIPSCtmManualsTable_Object = MibTable
hh3cDot11WIPSCtmManualsTable = _Hh3cDot11WIPSCtmManualsTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 15, 1, 23)
)
if mibBuilder.loadTexts:
    hh3cDot11WIPSCtmManualsTable.setStatus("current")
_Hh3cDot11WIPSCtmManualsEntry_Object = MibTableRow
hh3cDot11WIPSCtmManualsEntry = _Hh3cDot11WIPSCtmManualsEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 15, 1, 23, 1)
)
hh3cDot11WIPSCtmManualsEntry.setIndexNames(
    (0, "HH3C-DOT11-WIPS-MIB", "hh3cDot11WIPSCtmManualsPlyName"),
    (0, "HH3C-DOT11-WIPS-MIB", "hh3cDot11WIPSCtmManualsMacAddr"),
)
if mibBuilder.loadTexts:
    hh3cDot11WIPSCtmManualsEntry.setStatus("current")


class _Hh3cDot11WIPSCtmManualsPlyName_Type(OctetString):
    """Custom type hh3cDot11WIPSCtmManualsPlyName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 63),
    )


_Hh3cDot11WIPSCtmManualsPlyName_Type.__name__ = "OctetString"
_Hh3cDot11WIPSCtmManualsPlyName_Object = MibTableColumn
hh3cDot11WIPSCtmManualsPlyName = _Hh3cDot11WIPSCtmManualsPlyName_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 15, 1, 23, 1, 1),
    _Hh3cDot11WIPSCtmManualsPlyName_Type()
)
hh3cDot11WIPSCtmManualsPlyName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cDot11WIPSCtmManualsPlyName.setStatus("current")
_Hh3cDot11WIPSCtmManualsMacAddr_Type = MacAddress
_Hh3cDot11WIPSCtmManualsMacAddr_Object = MibTableColumn
hh3cDot11WIPSCtmManualsMacAddr = _Hh3cDot11WIPSCtmManualsMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 15, 1, 23, 1, 2),
    _Hh3cDot11WIPSCtmManualsMacAddr_Type()
)
hh3cDot11WIPSCtmManualsMacAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cDot11WIPSCtmManualsMacAddr.setStatus("current")
_Hh3cDot11WIPSCtmManualsRowStus_Type = RowStatus
_Hh3cDot11WIPSCtmManualsRowStus_Object = MibTableColumn
hh3cDot11WIPSCtmManualsRowStus = _Hh3cDot11WIPSCtmManualsRowStus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 15, 1, 23, 1, 3),
    _Hh3cDot11WIPSCtmManualsRowStus_Type()
)
hh3cDot11WIPSCtmManualsRowStus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cDot11WIPSCtmManualsRowStus.setStatus("current")
_Hh3cDot11WIPSCtmSensorTable_Object = MibTable
hh3cDot11WIPSCtmSensorTable = _Hh3cDot11WIPSCtmSensorTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 15, 1, 24)
)
if mibBuilder.loadTexts:
    hh3cDot11WIPSCtmSensorTable.setStatus("current")
_Hh3cDot11WIPSCtmSensorEntry_Object = MibTableRow
hh3cDot11WIPSCtmSensorEntry = _Hh3cDot11WIPSCtmSensorEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 15, 1, 24, 1)
)
hh3cDot11WIPSCtmSensorEntry.setIndexNames(
    (0, "HH3C-DOT11-WIPS-MIB", "hh3cDot11WIPSCtmSensorPolicyName"),
)
if mibBuilder.loadTexts:
    hh3cDot11WIPSCtmSensorEntry.setStatus("current")


class _Hh3cDot11WIPSCtmSensorPolicyName_Type(OctetString):
    """Custom type hh3cDot11WIPSCtmSensorPolicyName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 63),
    )


_Hh3cDot11WIPSCtmSensorPolicyName_Type.__name__ = "OctetString"
_Hh3cDot11WIPSCtmSensorPolicyName_Object = MibTableColumn
hh3cDot11WIPSCtmSensorPolicyName = _Hh3cDot11WIPSCtmSensorPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 15, 1, 24, 1, 1),
    _Hh3cDot11WIPSCtmSensorPolicyName_Type()
)
hh3cDot11WIPSCtmSensorPolicyName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cDot11WIPSCtmSensorPolicyName.setStatus("current")
_Hh3cDot11WIPSCtmSensoriStatus_Type = Hh3cDot11WIPSEnabledStatus
_Hh3cDot11WIPSCtmSensoriStatus_Object = MibTableColumn
hh3cDot11WIPSCtmSensoriStatus = _Hh3cDot11WIPSCtmSensoriStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 15, 1, 24, 1, 2),
    _Hh3cDot11WIPSCtmSensoriStatus_Type()
)
hh3cDot11WIPSCtmSensoriStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDot11WIPSCtmSensoriStatus.setStatus("current")
_Hh3cDot11WIPSInvOuiStateTable_Object = MibTable
hh3cDot11WIPSInvOuiStateTable = _Hh3cDot11WIPSInvOuiStateTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 15, 1, 25)
)
if mibBuilder.loadTexts:
    hh3cDot11WIPSInvOuiStateTable.setStatus("current")
_Hh3cDot11WIPSInvOuiStateEntry_Object = MibTableRow
hh3cDot11WIPSInvOuiStateEntry = _Hh3cDot11WIPSInvOuiStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 15, 1, 25, 1)
)
hh3cDot11WIPSInvOuiStateEntry.setIndexNames(
    (0, "HH3C-DOT11-WIPS-MIB", "hh3cDot11WIPSInvOuiStaPlyName"),
)
if mibBuilder.loadTexts:
    hh3cDot11WIPSInvOuiStateEntry.setStatus("current")


class _Hh3cDot11WIPSInvOuiStaPlyName_Type(OctetString):
    """Custom type hh3cDot11WIPSInvOuiStaPlyName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 63),
    )


_Hh3cDot11WIPSInvOuiStaPlyName_Type.__name__ = "OctetString"
_Hh3cDot11WIPSInvOuiStaPlyName_Object = MibTableColumn
hh3cDot11WIPSInvOuiStaPlyName = _Hh3cDot11WIPSInvOuiStaPlyName_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 15, 1, 25, 1, 1),
    _Hh3cDot11WIPSInvOuiStaPlyName_Type()
)
hh3cDot11WIPSInvOuiStaPlyName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cDot11WIPSInvOuiStaPlyName.setStatus("current")
_Hh3cDot11WIPSInvOuiStaiStatus_Type = Hh3cDot11WIPSEnabledStatus
_Hh3cDot11WIPSInvOuiStaiStatus_Object = MibTableColumn
hh3cDot11WIPSInvOuiStaiStatus = _Hh3cDot11WIPSInvOuiStaiStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 15, 1, 25, 1, 2),
    _Hh3cDot11WIPSInvOuiStaiStatus_Type()
)
hh3cDot11WIPSInvOuiStaiStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDot11WIPSInvOuiStaiStatus.setStatus("current")
_Hh3cDot11WIPSAPClaAuthTable_Object = MibTable
hh3cDot11WIPSAPClaAuthTable = _Hh3cDot11WIPSAPClaAuthTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 15, 1, 26)
)
if mibBuilder.loadTexts:
    hh3cDot11WIPSAPClaAuthTable.setStatus("current")
_Hh3cDot11WIPSAPClaAuthEntry_Object = MibTableRow
hh3cDot11WIPSAPClaAuthEntry = _Hh3cDot11WIPSAPClaAuthEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 15, 1, 26, 1)
)
hh3cDot11WIPSAPClaAuthEntry.setIndexNames(
    (0, "HH3C-DOT11-WIPS-MIB", "hh3cDot11WIPSAPClaAuthRuleID"),
)
if mibBuilder.loadTexts:
    hh3cDot11WIPSAPClaAuthEntry.setStatus("current")


class _Hh3cDot11WIPSAPClaAuthRuleID_Type(Integer32):
    """Custom type hh3cDot11WIPSAPClaAuthRuleID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_Hh3cDot11WIPSAPClaAuthRuleID_Type.__name__ = "Integer32"
_Hh3cDot11WIPSAPClaAuthRuleID_Object = MibTableColumn
hh3cDot11WIPSAPClaAuthRuleID = _Hh3cDot11WIPSAPClaAuthRuleID_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 15, 1, 26, 1, 1),
    _Hh3cDot11WIPSAPClaAuthRuleID_Type()
)
hh3cDot11WIPSAPClaAuthRuleID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cDot11WIPSAPClaAuthRuleID.setStatus("current")
_Hh3cDot11WIPSAPClaAuthMethod_Type = Hh3cDot11WIPSAPClaAuthMethods
_Hh3cDot11WIPSAPClaAuthMethod_Object = MibTableColumn
hh3cDot11WIPSAPClaAuthMethod = _Hh3cDot11WIPSAPClaAuthMethod_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 15, 1, 26, 1, 2),
    _Hh3cDot11WIPSAPClaAuthMethod_Type()
)
hh3cDot11WIPSAPClaAuthMethod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDot11WIPSAPClaAuthMethod.setStatus("current")
_Hh3cDot11WIPSAPClaAuthType_Type = Hh3cDot11WIPSAPClassifyCmpType
_Hh3cDot11WIPSAPClaAuthType_Object = MibTableColumn
hh3cDot11WIPSAPClaAuthType = _Hh3cDot11WIPSAPClaAuthType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 15, 1, 26, 1, 3),
    _Hh3cDot11WIPSAPClaAuthType_Type()
)
hh3cDot11WIPSAPClaAuthType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDot11WIPSAPClaAuthType.setStatus("current")
_Hh3cDot11WIPSAPClaAuthStatus_Type = Hh3cDot11WIPSEnabledStatus
_Hh3cDot11WIPSAPClaAuthStatus_Object = MibTableColumn
hh3cDot11WIPSAPClaAuthStatus = _Hh3cDot11WIPSAPClaAuthStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 15, 1, 26, 1, 4),
    _Hh3cDot11WIPSAPClaAuthStatus_Type()
)
hh3cDot11WIPSAPClaAuthStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDot11WIPSAPClaAuthStatus.setStatus("current")
_Hh3cDot11WIPSAPClaCltOnlTable_Object = MibTable
hh3cDot11WIPSAPClaCltOnlTable = _Hh3cDot11WIPSAPClaCltOnlTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 15, 1, 27)
)
if mibBuilder.loadTexts:
    hh3cDot11WIPSAPClaCltOnlTable.setStatus("current")
_Hh3cDot11WIPSAPClaCltOnlEntry_Object = MibTableRow
hh3cDot11WIPSAPClaCltOnlEntry = _Hh3cDot11WIPSAPClaCltOnlEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 15, 1, 27, 1)
)
hh3cDot11WIPSAPClaCltOnlEntry.setIndexNames(
    (0, "HH3C-DOT11-WIPS-MIB", "hh3cDot11WIPSAPClaCltOnlRuleID"),
)
if mibBuilder.loadTexts:
    hh3cDot11WIPSAPClaCltOnlEntry.setStatus("current")


class _Hh3cDot11WIPSAPClaCltOnlRuleID_Type(Integer32):
    """Custom type hh3cDot11WIPSAPClaCltOnlRuleID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_Hh3cDot11WIPSAPClaCltOnlRuleID_Type.__name__ = "Integer32"
_Hh3cDot11WIPSAPClaCltOnlRuleID_Object = MibTableColumn
hh3cDot11WIPSAPClaCltOnlRuleID = _Hh3cDot11WIPSAPClaCltOnlRuleID_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 15, 1, 27, 1, 1),
    _Hh3cDot11WIPSAPClaCltOnlRuleID_Type()
)
hh3cDot11WIPSAPClaCltOnlRuleID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cDot11WIPSAPClaCltOnlRuleID.setStatus("current")


class _Hh3cDot11WIPSAPClaCltOnlV1_Type(Integer32):
    """Custom type hh3cDot11WIPSAPClaCltOnlV1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Hh3cDot11WIPSAPClaCltOnlV1_Type.__name__ = "Integer32"
_Hh3cDot11WIPSAPClaCltOnlV1_Object = MibTableColumn
hh3cDot11WIPSAPClaCltOnlV1 = _Hh3cDot11WIPSAPClaCltOnlV1_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 15, 1, 27, 1, 2),
    _Hh3cDot11WIPSAPClaCltOnlV1_Type()
)
hh3cDot11WIPSAPClaCltOnlV1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDot11WIPSAPClaCltOnlV1.setStatus("current")


class _Hh3cDot11WIPSAPClaCltOnlV2_Type(Integer32):
    """Custom type hh3cDot11WIPSAPClaCltOnlV2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Hh3cDot11WIPSAPClaCltOnlV2_Type.__name__ = "Integer32"
_Hh3cDot11WIPSAPClaCltOnlV2_Object = MibTableColumn
hh3cDot11WIPSAPClaCltOnlV2 = _Hh3cDot11WIPSAPClaCltOnlV2_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 15, 1, 27, 1, 3),
    _Hh3cDot11WIPSAPClaCltOnlV2_Type()
)
hh3cDot11WIPSAPClaCltOnlV2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDot11WIPSAPClaCltOnlV2.setStatus("current")
_Hh3cDot11WIPSAPClaCltOnlSts_Type = Hh3cDot11WIPSEnabledStatus
_Hh3cDot11WIPSAPClaCltOnlSts_Object = MibTableColumn
hh3cDot11WIPSAPClaCltOnlSts = _Hh3cDot11WIPSAPClaCltOnlSts_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 15, 1, 27, 1, 4),
    _Hh3cDot11WIPSAPClaCltOnlSts_Type()
)
hh3cDot11WIPSAPClaCltOnlSts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDot11WIPSAPClaCltOnlSts.setStatus("current")
_Hh3cDot11WIPSAPClaDiscrTable_Object = MibTable
hh3cDot11WIPSAPClaDiscrTable = _Hh3cDot11WIPSAPClaDiscrTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 15, 1, 28)
)
if mibBuilder.loadTexts:
    hh3cDot11WIPSAPClaDiscrTable.setStatus("current")
_Hh3cDot11WIPSAPClaDiscrEntry_Object = MibTableRow
hh3cDot11WIPSAPClaDiscrEntry = _Hh3cDot11WIPSAPClaDiscrEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 15, 1, 28, 1)
)
hh3cDot11WIPSAPClaDiscrEntry.setIndexNames(
    (0, "HH3C-DOT11-WIPS-MIB", "hh3cDot11WIPSAPClaDiscrRuleID"),
)
if mibBuilder.loadTexts:
    hh3cDot11WIPSAPClaDiscrEntry.setStatus("current")


class _Hh3cDot11WIPSAPClaDiscrRuleID_Type(Integer32):
    """Custom type hh3cDot11WIPSAPClaDiscrRuleID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_Hh3cDot11WIPSAPClaDiscrRuleID_Type.__name__ = "Integer32"
_Hh3cDot11WIPSAPClaDiscrRuleID_Object = MibTableColumn
hh3cDot11WIPSAPClaDiscrRuleID = _Hh3cDot11WIPSAPClaDiscrRuleID_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 15, 1, 28, 1, 1),
    _Hh3cDot11WIPSAPClaDiscrRuleID_Type()
)
hh3cDot11WIPSAPClaDiscrRuleID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cDot11WIPSAPClaDiscrRuleID.setStatus("current")


class _Hh3cDot11WIPSAPClaDiscrV1_Type(Integer32):
    """Custom type hh3cDot11WIPSAPClaDiscrV1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 128),
    )


_Hh3cDot11WIPSAPClaDiscrV1_Type.__name__ = "Integer32"
_Hh3cDot11WIPSAPClaDiscrV1_Object = MibTableColumn
hh3cDot11WIPSAPClaDiscrV1 = _Hh3cDot11WIPSAPClaDiscrV1_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 15, 1, 28, 1, 2),
    _Hh3cDot11WIPSAPClaDiscrV1_Type()
)
hh3cDot11WIPSAPClaDiscrV1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDot11WIPSAPClaDiscrV1.setStatus("current")


class _Hh3cDot11WIPSAPClaDiscrV2_Type(Integer32):
    """Custom type hh3cDot11WIPSAPClaDiscrV2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 128),
    )


_Hh3cDot11WIPSAPClaDiscrV2_Type.__name__ = "Integer32"
_Hh3cDot11WIPSAPClaDiscrV2_Object = MibTableColumn
hh3cDot11WIPSAPClaDiscrV2 = _Hh3cDot11WIPSAPClaDiscrV2_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 15, 1, 28, 1, 3),
    _Hh3cDot11WIPSAPClaDiscrV2_Type()
)
hh3cDot11WIPSAPClaDiscrV2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDot11WIPSAPClaDiscrV2.setStatus("current")
_Hh3cDot11WIPSAPClaDiscrSta_Type = Hh3cDot11WIPSEnabledStatus
_Hh3cDot11WIPSAPClaDiscrSta_Object = MibTableColumn
hh3cDot11WIPSAPClaDiscrSta = _Hh3cDot11WIPSAPClaDiscrSta_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 15, 1, 28, 1, 4),
    _Hh3cDot11WIPSAPClaDiscrSta_Type()
)
hh3cDot11WIPSAPClaDiscrSta.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDot11WIPSAPClaDiscrSta.setStatus("current")
_Hh3cDot11WIPSAPClaRssiTable_Object = MibTable
hh3cDot11WIPSAPClaRssiTable = _Hh3cDot11WIPSAPClaRssiTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 15, 1, 29)
)
if mibBuilder.loadTexts:
    hh3cDot11WIPSAPClaRssiTable.setStatus("current")
_Hh3cDot11WIPSAPClaRssiEntry_Object = MibTableRow
hh3cDot11WIPSAPClaRssiEntry = _Hh3cDot11WIPSAPClaRssiEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 15, 1, 29, 1)
)
hh3cDot11WIPSAPClaRssiEntry.setIndexNames(
    (0, "HH3C-DOT11-WIPS-MIB", "hh3cDot11WIPSAPClaRssiRuleID"),
)
if mibBuilder.loadTexts:
    hh3cDot11WIPSAPClaRssiEntry.setStatus("current")


class _Hh3cDot11WIPSAPClaRssiRuleID_Type(Integer32):
    """Custom type hh3cDot11WIPSAPClaRssiRuleID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_Hh3cDot11WIPSAPClaRssiRuleID_Type.__name__ = "Integer32"
_Hh3cDot11WIPSAPClaRssiRuleID_Object = MibTableColumn
hh3cDot11WIPSAPClaRssiRuleID = _Hh3cDot11WIPSAPClaRssiRuleID_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 15, 1, 29, 1, 1),
    _Hh3cDot11WIPSAPClaRssiRuleID_Type()
)
hh3cDot11WIPSAPClaRssiRuleID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cDot11WIPSAPClaRssiRuleID.setStatus("current")


class _Hh3cDot11WIPSAPClaRssiV1_Type(Integer32):
    """Custom type hh3cDot11WIPSAPClaRssiV1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Hh3cDot11WIPSAPClaRssiV1_Type.__name__ = "Integer32"
_Hh3cDot11WIPSAPClaRssiV1_Object = MibTableColumn
hh3cDot11WIPSAPClaRssiV1 = _Hh3cDot11WIPSAPClaRssiV1_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 15, 1, 29, 1, 2),
    _Hh3cDot11WIPSAPClaRssiV1_Type()
)
hh3cDot11WIPSAPClaRssiV1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDot11WIPSAPClaRssiV1.setStatus("current")


class _Hh3cDot11WIPSAPClaRssiV2_Type(Integer32):
    """Custom type hh3cDot11WIPSAPClaRssiV2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Hh3cDot11WIPSAPClaRssiV2_Type.__name__ = "Integer32"
_Hh3cDot11WIPSAPClaRssiV2_Object = MibTableColumn
hh3cDot11WIPSAPClaRssiV2 = _Hh3cDot11WIPSAPClaRssiV2_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 15, 1, 29, 1, 3),
    _Hh3cDot11WIPSAPClaRssiV2_Type()
)
hh3cDot11WIPSAPClaRssiV2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDot11WIPSAPClaRssiV2.setStatus("current")
_Hh3cDot11WIPSAPClaRssiSta_Type = Hh3cDot11WIPSEnabledStatus
_Hh3cDot11WIPSAPClaRssiSta_Object = MibTableColumn
hh3cDot11WIPSAPClaRssiSta = _Hh3cDot11WIPSAPClaRssiSta_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 15, 1, 29, 1, 4),
    _Hh3cDot11WIPSAPClaRssiSta_Type()
)
hh3cDot11WIPSAPClaRssiSta.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDot11WIPSAPClaRssiSta.setStatus("current")
_Hh3cDot11WIPSAPClaUpdurTable_Object = MibTable
hh3cDot11WIPSAPClaUpdurTable = _Hh3cDot11WIPSAPClaUpdurTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 15, 1, 30)
)
if mibBuilder.loadTexts:
    hh3cDot11WIPSAPClaUpdurTable.setStatus("current")
_Hh3cDot11WIPSAPClaUpdurEntry_Object = MibTableRow
hh3cDot11WIPSAPClaUpdurEntry = _Hh3cDot11WIPSAPClaUpdurEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 15, 1, 30, 1)
)
hh3cDot11WIPSAPClaUpdurEntry.setIndexNames(
    (0, "HH3C-DOT11-WIPS-MIB", "hh3cDot11WIPSAPClaUpdurRuleID"),
)
if mibBuilder.loadTexts:
    hh3cDot11WIPSAPClaUpdurEntry.setStatus("current")


class _Hh3cDot11WIPSAPClaUpdurRuleID_Type(Integer32):
    """Custom type hh3cDot11WIPSAPClaUpdurRuleID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_Hh3cDot11WIPSAPClaUpdurRuleID_Type.__name__ = "Integer32"
_Hh3cDot11WIPSAPClaUpdurRuleID_Object = MibTableColumn
hh3cDot11WIPSAPClaUpdurRuleID = _Hh3cDot11WIPSAPClaUpdurRuleID_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 15, 1, 30, 1, 1),
    _Hh3cDot11WIPSAPClaUpdurRuleID_Type()
)
hh3cDot11WIPSAPClaUpdurRuleID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cDot11WIPSAPClaUpdurRuleID.setStatus("current")


class _Hh3cDot11WIPSAPClaUpdurV1_Type(Integer32):
    """Custom type hh3cDot11WIPSAPClaUpdurV1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2592000),
    )


_Hh3cDot11WIPSAPClaUpdurV1_Type.__name__ = "Integer32"
_Hh3cDot11WIPSAPClaUpdurV1_Object = MibTableColumn
hh3cDot11WIPSAPClaUpdurV1 = _Hh3cDot11WIPSAPClaUpdurV1_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 15, 1, 30, 1, 2),
    _Hh3cDot11WIPSAPClaUpdurV1_Type()
)
hh3cDot11WIPSAPClaUpdurV1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDot11WIPSAPClaUpdurV1.setStatus("current")


class _Hh3cDot11WIPSAPClaUpdurV2_Type(Integer32):
    """Custom type hh3cDot11WIPSAPClaUpdurV2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2592000),
    )


_Hh3cDot11WIPSAPClaUpdurV2_Type.__name__ = "Integer32"
_Hh3cDot11WIPSAPClaUpdurV2_Object = MibTableColumn
hh3cDot11WIPSAPClaUpdurV2 = _Hh3cDot11WIPSAPClaUpdurV2_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 15, 1, 30, 1, 3),
    _Hh3cDot11WIPSAPClaUpdurV2_Type()
)
hh3cDot11WIPSAPClaUpdurV2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDot11WIPSAPClaUpdurV2.setStatus("current")
_Hh3cDot11WIPSAPClaUpdurSta_Type = Hh3cDot11WIPSEnabledStatus
_Hh3cDot11WIPSAPClaUpdurSta_Object = MibTableColumn
hh3cDot11WIPSAPClaUpdurSta = _Hh3cDot11WIPSAPClaUpdurSta_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 15, 1, 30, 1, 4),
    _Hh3cDot11WIPSAPClaUpdurSta_Type()
)
hh3cDot11WIPSAPClaUpdurSta.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDot11WIPSAPClaUpdurSta.setStatus("current")
_Hh3cDot11WIPSAPClaOuiTable_Object = MibTable
hh3cDot11WIPSAPClaOuiTable = _Hh3cDot11WIPSAPClaOuiTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 15, 1, 31)
)
if mibBuilder.loadTexts:
    hh3cDot11WIPSAPClaOuiTable.setStatus("current")
_Hh3cDot11WIPSAPClaOuiEntry_Object = MibTableRow
hh3cDot11WIPSAPClaOuiEntry = _Hh3cDot11WIPSAPClaOuiEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 15, 1, 31, 1)
)
hh3cDot11WIPSAPClaOuiEntry.setIndexNames(
    (0, "HH3C-DOT11-WIPS-MIB", "hh3cDot11WIPSAPClaOuiRuleID"),
)
if mibBuilder.loadTexts:
    hh3cDot11WIPSAPClaOuiEntry.setStatus("current")


class _Hh3cDot11WIPSAPClaOuiRuleID_Type(Integer32):
    """Custom type hh3cDot11WIPSAPClaOuiRuleID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_Hh3cDot11WIPSAPClaOuiRuleID_Type.__name__ = "Integer32"
_Hh3cDot11WIPSAPClaOuiRuleID_Object = MibTableColumn
hh3cDot11WIPSAPClaOuiRuleID = _Hh3cDot11WIPSAPClaOuiRuleID_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 15, 1, 31, 1, 1),
    _Hh3cDot11WIPSAPClaOuiRuleID_Type()
)
hh3cDot11WIPSAPClaOuiRuleID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cDot11WIPSAPClaOuiRuleID.setStatus("current")
_Hh3cDot11WIPSAPClaOuiMac_Type = Hh3cDot11WIPSOuiAddress
_Hh3cDot11WIPSAPClaOuiMac_Object = MibTableColumn
hh3cDot11WIPSAPClaOuiMac = _Hh3cDot11WIPSAPClaOuiMac_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 15, 1, 31, 1, 2),
    _Hh3cDot11WIPSAPClaOuiMac_Type()
)
hh3cDot11WIPSAPClaOuiMac.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDot11WIPSAPClaOuiMac.setStatus("current")
_Hh3cDot11WIPSAPClaOuiStatus_Type = Hh3cDot11WIPSEnabledStatus
_Hh3cDot11WIPSAPClaOuiStatus_Object = MibTableColumn
hh3cDot11WIPSAPClaOuiStatus = _Hh3cDot11WIPSAPClaOuiStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 15, 1, 31, 1, 3),
    _Hh3cDot11WIPSAPClaOuiStatus_Type()
)
hh3cDot11WIPSAPClaOuiStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDot11WIPSAPClaOuiStatus.setStatus("current")
_Hh3cDot11WIPSAPClaSryTable_Object = MibTable
hh3cDot11WIPSAPClaSryTable = _Hh3cDot11WIPSAPClaSryTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 15, 1, 32)
)
if mibBuilder.loadTexts:
    hh3cDot11WIPSAPClaSryTable.setStatus("current")
_Hh3cDot11WIPSAPClaSryEntry_Object = MibTableRow
hh3cDot11WIPSAPClaSryEntry = _Hh3cDot11WIPSAPClaSryEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 15, 1, 32, 1)
)
hh3cDot11WIPSAPClaSryEntry.setIndexNames(
    (0, "HH3C-DOT11-WIPS-MIB", "hh3cDot11WIPSAPClaSryRuleID"),
)
if mibBuilder.loadTexts:
    hh3cDot11WIPSAPClaSryEntry.setStatus("current")


class _Hh3cDot11WIPSAPClaSryRuleID_Type(Integer32):
    """Custom type hh3cDot11WIPSAPClaSryRuleID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_Hh3cDot11WIPSAPClaSryRuleID_Type.__name__ = "Integer32"
_Hh3cDot11WIPSAPClaSryRuleID_Object = MibTableColumn
hh3cDot11WIPSAPClaSryRuleID = _Hh3cDot11WIPSAPClaSryRuleID_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 15, 1, 32, 1, 1),
    _Hh3cDot11WIPSAPClaSryRuleID_Type()
)
hh3cDot11WIPSAPClaSryRuleID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cDot11WIPSAPClaSryRuleID.setStatus("current")
_Hh3cDot11WIPSAPClaSryType_Type = Hh3cDot11WIPSAPClaSecurityType
_Hh3cDot11WIPSAPClaSryType_Object = MibTableColumn
hh3cDot11WIPSAPClaSryType = _Hh3cDot11WIPSAPClaSryType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 15, 1, 32, 1, 2),
    _Hh3cDot11WIPSAPClaSryType_Type()
)
hh3cDot11WIPSAPClaSryType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDot11WIPSAPClaSryType.setStatus("current")
_Hh3cDot11WIPSAPClaSryCmpType_Type = Hh3cDot11WIPSAPClassifyCmpType
_Hh3cDot11WIPSAPClaSryCmpType_Object = MibTableColumn
hh3cDot11WIPSAPClaSryCmpType = _Hh3cDot11WIPSAPClaSryCmpType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 15, 1, 32, 1, 3),
    _Hh3cDot11WIPSAPClaSryCmpType_Type()
)
hh3cDot11WIPSAPClaSryCmpType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDot11WIPSAPClaSryCmpType.setStatus("current")
_Hh3cDot11WIPSAPClaSrySta_Type = Hh3cDot11WIPSEnabledStatus
_Hh3cDot11WIPSAPClaSrySta_Object = MibTableColumn
hh3cDot11WIPSAPClaSrySta = _Hh3cDot11WIPSAPClaSrySta_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 15, 1, 32, 1, 4),
    _Hh3cDot11WIPSAPClaSrySta_Type()
)
hh3cDot11WIPSAPClaSrySta.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDot11WIPSAPClaSrySta.setStatus("current")
_Hh3cDot11WIPSAPClaSsidTable_Object = MibTable
hh3cDot11WIPSAPClaSsidTable = _Hh3cDot11WIPSAPClaSsidTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 15, 1, 33)
)
if mibBuilder.loadTexts:
    hh3cDot11WIPSAPClaSsidTable.setStatus("current")
_Hh3cDot11WIPSAPClaSsidEntry_Object = MibTableRow
hh3cDot11WIPSAPClaSsidEntry = _Hh3cDot11WIPSAPClaSsidEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 15, 1, 33, 1)
)
hh3cDot11WIPSAPClaSsidEntry.setIndexNames(
    (0, "HH3C-DOT11-WIPS-MIB", "hh3cDot11WIPSAPClaSsidRuleID"),
)
if mibBuilder.loadTexts:
    hh3cDot11WIPSAPClaSsidEntry.setStatus("current")


class _Hh3cDot11WIPSAPClaSsidRuleID_Type(Integer32):
    """Custom type hh3cDot11WIPSAPClaSsidRuleID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_Hh3cDot11WIPSAPClaSsidRuleID_Type.__name__ = "Integer32"
_Hh3cDot11WIPSAPClaSsidRuleID_Object = MibTableColumn
hh3cDot11WIPSAPClaSsidRuleID = _Hh3cDot11WIPSAPClaSsidRuleID_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 15, 1, 33, 1, 1),
    _Hh3cDot11WIPSAPClaSsidRuleID_Type()
)
hh3cDot11WIPSAPClaSsidRuleID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cDot11WIPSAPClaSsidRuleID.setStatus("current")


class _Hh3cDot11WIPSAPClaSsidName_Type(OctetString):
    """Custom type hh3cDot11WIPSAPClaSsidName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_Hh3cDot11WIPSAPClaSsidName_Type.__name__ = "OctetString"
_Hh3cDot11WIPSAPClaSsidName_Object = MibTableColumn
hh3cDot11WIPSAPClaSsidName = _Hh3cDot11WIPSAPClaSsidName_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 15, 1, 33, 1, 2),
    _Hh3cDot11WIPSAPClaSsidName_Type()
)
hh3cDot11WIPSAPClaSsidName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDot11WIPSAPClaSsidName.setStatus("current")
_Hh3cDot11WIPSAPClaSsidcase_Type = TruthValue
_Hh3cDot11WIPSAPClaSsidcase_Object = MibTableColumn
hh3cDot11WIPSAPClaSsidcase = _Hh3cDot11WIPSAPClaSsidcase_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 15, 1, 33, 1, 3),
    _Hh3cDot11WIPSAPClaSsidcase_Type()
)
hh3cDot11WIPSAPClaSsidcase.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDot11WIPSAPClaSsidcase.setStatus("current")
_Hh3cDot11WIPSAPClaSsidCmpType_Type = Hh3cDot11WIPSAPClasSsidCmpType
_Hh3cDot11WIPSAPClaSsidCmpType_Object = MibTableColumn
hh3cDot11WIPSAPClaSsidCmpType = _Hh3cDot11WIPSAPClaSsidCmpType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 15, 1, 33, 1, 4),
    _Hh3cDot11WIPSAPClaSsidCmpType_Type()
)
hh3cDot11WIPSAPClaSsidCmpType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDot11WIPSAPClaSsidCmpType.setStatus("current")
_Hh3cDot11WIPSAPClaSsidStatus_Type = Hh3cDot11WIPSEnabledStatus
_Hh3cDot11WIPSAPClaSsidStatus_Object = MibTableColumn
hh3cDot11WIPSAPClaSsidStatus = _Hh3cDot11WIPSAPClaSsidStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 15, 1, 33, 1, 5),
    _Hh3cDot11WIPSAPClaSsidStatus_Type()
)
hh3cDot11WIPSAPClaSsidStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDot11WIPSAPClaSsidStatus.setStatus("current")
_Hh3cDot11WIPSDtcSigTable_Object = MibTable
hh3cDot11WIPSDtcSigTable = _Hh3cDot11WIPSDtcSigTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 15, 1, 34)
)
if mibBuilder.loadTexts:
    hh3cDot11WIPSDtcSigTable.setStatus("current")
_Hh3cDot11WIPSDtcSigEntry_Object = MibTableRow
hh3cDot11WIPSDtcSigEntry = _Hh3cDot11WIPSDtcSigEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 15, 1, 34, 1)
)
hh3cDot11WIPSDtcSigEntry.setIndexNames(
    (0, "HH3C-DOT11-WIPS-MIB", "hh3cDot11WIPSDtcSigPolicyName"),
)
if mibBuilder.loadTexts:
    hh3cDot11WIPSDtcSigEntry.setStatus("current")


class _Hh3cDot11WIPSDtcSigPolicyName_Type(OctetString):
    """Custom type hh3cDot11WIPSDtcSigPolicyName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 63),
    )


_Hh3cDot11WIPSDtcSigPolicyName_Type.__name__ = "OctetString"
_Hh3cDot11WIPSDtcSigPolicyName_Object = MibTableColumn
hh3cDot11WIPSDtcSigPolicyName = _Hh3cDot11WIPSDtcSigPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 15, 1, 34, 1, 1),
    _Hh3cDot11WIPSDtcSigPolicyName_Type()
)
hh3cDot11WIPSDtcSigPolicyName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cDot11WIPSDtcSigPolicyName.setStatus("current")


class _Hh3cDot11WIPSDtcSigInterval_Type(Integer32):
    """Custom type hh3cDot11WIPSDtcSigInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3600),
    )


_Hh3cDot11WIPSDtcSigInterval_Type.__name__ = "Integer32"
_Hh3cDot11WIPSDtcSigInterval_Object = MibTableColumn
hh3cDot11WIPSDtcSigInterval = _Hh3cDot11WIPSDtcSigInterval_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 15, 1, 34, 1, 2),
    _Hh3cDot11WIPSDtcSigInterval_Type()
)
hh3cDot11WIPSDtcSigInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDot11WIPSDtcSigInterval.setStatus("current")


class _Hh3cDot11WIPSDtcSigQuiet_Type(Integer32):
    """Custom type hh3cDot11WIPSDtcSigQuiet based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 604800),
    )


_Hh3cDot11WIPSDtcSigQuiet_Type.__name__ = "Integer32"
_Hh3cDot11WIPSDtcSigQuiet_Object = MibTableColumn
hh3cDot11WIPSDtcSigQuiet = _Hh3cDot11WIPSDtcSigQuiet_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 15, 1, 34, 1, 3),
    _Hh3cDot11WIPSDtcSigQuiet_Type()
)
hh3cDot11WIPSDtcSigQuiet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDot11WIPSDtcSigQuiet.setStatus("current")


class _Hh3cDot11WIPSDtcSigThreshold_Type(Integer32):
    """Custom type hh3cDot11WIPSDtcSigThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100000),
    )


_Hh3cDot11WIPSDtcSigThreshold_Type.__name__ = "Integer32"
_Hh3cDot11WIPSDtcSigThreshold_Object = MibTableColumn
hh3cDot11WIPSDtcSigThreshold = _Hh3cDot11WIPSDtcSigThreshold_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 15, 1, 34, 1, 4),
    _Hh3cDot11WIPSDtcSigThreshold_Type()
)
hh3cDot11WIPSDtcSigThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDot11WIPSDtcSigThreshold.setStatus("current")
_Hh3cDot11WIPSDtcSigStatus_Type = Hh3cDot11WIPSEnabledStatus
_Hh3cDot11WIPSDtcSigStatus_Object = MibTableColumn
hh3cDot11WIPSDtcSigStatus = _Hh3cDot11WIPSDtcSigStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 15, 1, 34, 1, 5),
    _Hh3cDot11WIPSDtcSigStatus_Type()
)
hh3cDot11WIPSDtcSigStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDot11WIPSDtcSigStatus.setStatus("current")
_Hh3cDot11WIPSPolicyTable_Object = MibTable
hh3cDot11WIPSPolicyTable = _Hh3cDot11WIPSPolicyTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 15, 1, 35)
)
if mibBuilder.loadTexts:
    hh3cDot11WIPSPolicyTable.setStatus("current")
_Hh3cDot11WIPSPolicyEntry_Object = MibTableRow
hh3cDot11WIPSPolicyEntry = _Hh3cDot11WIPSPolicyEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 15, 1, 35, 1)
)
hh3cDot11WIPSPolicyEntry.setIndexNames(
    (0, "HH3C-DOT11-WIPS-MIB", "hh3cDot11WIPSPolicyType"),
    (0, "HH3C-DOT11-WIPS-MIB", "hh3cDot11WIPSPolicyName"),
)
if mibBuilder.loadTexts:
    hh3cDot11WIPSPolicyEntry.setStatus("current")
_Hh3cDot11WIPSPolicyType_Type = Hh3cDot11WIPSPolicyTypeValue
_Hh3cDot11WIPSPolicyType_Object = MibTableColumn
hh3cDot11WIPSPolicyType = _Hh3cDot11WIPSPolicyType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 15, 1, 35, 1, 1),
    _Hh3cDot11WIPSPolicyType_Type()
)
hh3cDot11WIPSPolicyType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cDot11WIPSPolicyType.setStatus("current")


class _Hh3cDot11WIPSPolicyName_Type(OctetString):
    """Custom type hh3cDot11WIPSPolicyName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 63),
    )


_Hh3cDot11WIPSPolicyName_Type.__name__ = "OctetString"
_Hh3cDot11WIPSPolicyName_Object = MibTableColumn
hh3cDot11WIPSPolicyName = _Hh3cDot11WIPSPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 15, 1, 35, 1, 2),
    _Hh3cDot11WIPSPolicyName_Type()
)
hh3cDot11WIPSPolicyName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cDot11WIPSPolicyName.setStatus("current")
_Hh3cDot11WIPSPolicyRowStatus_Type = RowStatus
_Hh3cDot11WIPSPolicyRowStatus_Object = MibTableColumn
hh3cDot11WIPSPolicyRowStatus = _Hh3cDot11WIPSPolicyRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 15, 1, 35, 1, 3),
    _Hh3cDot11WIPSPolicyRowStatus_Type()
)
hh3cDot11WIPSPolicyRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cDot11WIPSPolicyRowStatus.setStatus("current")
_Hh3cDot11WIPSSigFrameTypeTable_Object = MibTable
hh3cDot11WIPSSigFrameTypeTable = _Hh3cDot11WIPSSigFrameTypeTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 15, 1, 36)
)
if mibBuilder.loadTexts:
    hh3cDot11WIPSSigFrameTypeTable.setStatus("current")
_Hh3cDot11WIPSSigFrameTypeEntry_Object = MibTableRow
hh3cDot11WIPSSigFrameTypeEntry = _Hh3cDot11WIPSSigFrameTypeEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 15, 1, 36, 1)
)
hh3cDot11WIPSSigFrameTypeEntry.setIndexNames(
    (0, "HH3C-DOT11-WIPS-MIB", "hh3cDot11WIPSSigFrameTypeRuleId"),
)
if mibBuilder.loadTexts:
    hh3cDot11WIPSSigFrameTypeEntry.setStatus("current")


class _Hh3cDot11WIPSSigFrameTypeRuleId_Type(Integer32):
    """Custom type hh3cDot11WIPSSigFrameTypeRuleId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_Hh3cDot11WIPSSigFrameTypeRuleId_Type.__name__ = "Integer32"
_Hh3cDot11WIPSSigFrameTypeRuleId_Object = MibTableColumn
hh3cDot11WIPSSigFrameTypeRuleId = _Hh3cDot11WIPSSigFrameTypeRuleId_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 15, 1, 36, 1, 1),
    _Hh3cDot11WIPSSigFrameTypeRuleId_Type()
)
hh3cDot11WIPSSigFrameTypeRuleId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cDot11WIPSSigFrameTypeRuleId.setStatus("current")
_Hh3cDot11WIPSSigFrameType_Type = Hh3cDot11WIPSSigFrameTypes
_Hh3cDot11WIPSSigFrameType_Object = MibTableColumn
hh3cDot11WIPSSigFrameType = _Hh3cDot11WIPSSigFrameType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 15, 1, 36, 1, 2),
    _Hh3cDot11WIPSSigFrameType_Type()
)
hh3cDot11WIPSSigFrameType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDot11WIPSSigFrameType.setStatus("current")
_Hh3cDot11WIPSSigFrameSubType_Type = Hh3cDot11WIPSSigFrameSubTypes
_Hh3cDot11WIPSSigFrameSubType_Object = MibTableColumn
hh3cDot11WIPSSigFrameSubType = _Hh3cDot11WIPSSigFrameSubType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 15, 1, 36, 1, 3),
    _Hh3cDot11WIPSSigFrameSubType_Type()
)
hh3cDot11WIPSSigFrameSubType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDot11WIPSSigFrameSubType.setStatus("current")
_Hh3cDot11WIPSSigFrameTypeStatus_Type = Hh3cDot11WIPSEnabledStatus
_Hh3cDot11WIPSSigFrameTypeStatus_Object = MibTableColumn
hh3cDot11WIPSSigFrameTypeStatus = _Hh3cDot11WIPSSigFrameTypeStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 15, 1, 36, 1, 4),
    _Hh3cDot11WIPSSigFrameTypeStatus_Type()
)
hh3cDot11WIPSSigFrameTypeStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDot11WIPSSigFrameTypeStatus.setStatus("current")
_Hh3cDot11WIPSCtmTable_Object = MibTable
hh3cDot11WIPSCtmTable = _Hh3cDot11WIPSCtmTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 15, 1, 37)
)
if mibBuilder.loadTexts:
    hh3cDot11WIPSCtmTable.setStatus("current")
_Hh3cDot11WIPSCtmEntry_Object = MibTableRow
hh3cDot11WIPSCtmEntry = _Hh3cDot11WIPSCtmEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 15, 1, 37, 1)
)
hh3cDot11WIPSCtmEntry.setIndexNames(
    (0, "HH3C-DOT11-WIPS-MIB", "hh3cDot11WIPSCtmPolicyName"),
    (0, "HH3C-DOT11-WIPS-MIB", "hh3cDot11WIPSCtmClassifyType"),
)
if mibBuilder.loadTexts:
    hh3cDot11WIPSCtmEntry.setStatus("current")


class _Hh3cDot11WIPSCtmPolicyName_Type(OctetString):
    """Custom type hh3cDot11WIPSCtmPolicyName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 63),
    )


_Hh3cDot11WIPSCtmPolicyName_Type.__name__ = "OctetString"
_Hh3cDot11WIPSCtmPolicyName_Object = MibTableColumn
hh3cDot11WIPSCtmPolicyName = _Hh3cDot11WIPSCtmPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 15, 1, 37, 1, 1),
    _Hh3cDot11WIPSCtmPolicyName_Type()
)
hh3cDot11WIPSCtmPolicyName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cDot11WIPSCtmPolicyName.setStatus("current")
_Hh3cDot11WIPSCtmClassifyType_Type = Hh3cDot11WIPSCtmType
_Hh3cDot11WIPSCtmClassifyType_Object = MibTableColumn
hh3cDot11WIPSCtmClassifyType = _Hh3cDot11WIPSCtmClassifyType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 15, 1, 37, 1, 2),
    _Hh3cDot11WIPSCtmClassifyType_Type()
)
hh3cDot11WIPSCtmClassifyType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cDot11WIPSCtmClassifyType.setStatus("current")
_Hh3cDot11WIPSCtmStatus_Type = Hh3cDot11WIPSEnabledStatus
_Hh3cDot11WIPSCtmStatus_Object = MibTableColumn
hh3cDot11WIPSCtmStatus = _Hh3cDot11WIPSCtmStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 15, 1, 37, 1, 3),
    _Hh3cDot11WIPSCtmStatus_Type()
)
hh3cDot11WIPSCtmStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDot11WIPSCtmStatus.setStatus("current")
_Hh3cDot11WIPSSigPatternTable_Object = MibTable
hh3cDot11WIPSSigPatternTable = _Hh3cDot11WIPSSigPatternTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 15, 1, 38)
)
if mibBuilder.loadTexts:
    hh3cDot11WIPSSigPatternTable.setStatus("current")
_Hh3cDot11WIPSSigPatternEntry_Object = MibTableRow
hh3cDot11WIPSSigPatternEntry = _Hh3cDot11WIPSSigPatternEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 15, 1, 38, 1)
)
hh3cDot11WIPSSigPatternEntry.setIndexNames(
    (0, "HH3C-DOT11-WIPS-MIB", "hh3cDot11WIPSSigPatternRuleId"),
    (0, "HH3C-DOT11-WIPS-MIB", "hh3cDot11WIPSSigPatternNum"),
)
if mibBuilder.loadTexts:
    hh3cDot11WIPSSigPatternEntry.setStatus("current")


class _Hh3cDot11WIPSSigPatternRuleId_Type(Integer32):
    """Custom type hh3cDot11WIPSSigPatternRuleId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_Hh3cDot11WIPSSigPatternRuleId_Type.__name__ = "Integer32"
_Hh3cDot11WIPSSigPatternRuleId_Object = MibTableColumn
hh3cDot11WIPSSigPatternRuleId = _Hh3cDot11WIPSSigPatternRuleId_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 15, 1, 38, 1, 1),
    _Hh3cDot11WIPSSigPatternRuleId_Type()
)
hh3cDot11WIPSSigPatternRuleId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cDot11WIPSSigPatternRuleId.setStatus("current")


class _Hh3cDot11WIPSSigPatternNum_Type(Integer32):
    """Custom type hh3cDot11WIPSSigPatternNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Hh3cDot11WIPSSigPatternNum_Type.__name__ = "Integer32"
_Hh3cDot11WIPSSigPatternNum_Object = MibTableColumn
hh3cDot11WIPSSigPatternNum = _Hh3cDot11WIPSSigPatternNum_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 15, 1, 38, 1, 2),
    _Hh3cDot11WIPSSigPatternNum_Type()
)
hh3cDot11WIPSSigPatternNum.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cDot11WIPSSigPatternNum.setStatus("current")


class _Hh3cDot11WIPSSigPatternOffset_Type(Integer32):
    """Custom type hh3cDot11WIPSSigPatternOffset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2346),
    )


_Hh3cDot11WIPSSigPatternOffset_Type.__name__ = "Integer32"
_Hh3cDot11WIPSSigPatternOffset_Object = MibTableColumn
hh3cDot11WIPSSigPatternOffset = _Hh3cDot11WIPSSigPatternOffset_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 15, 1, 38, 1, 3),
    _Hh3cDot11WIPSSigPatternOffset_Type()
)
hh3cDot11WIPSSigPatternOffset.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cDot11WIPSSigPatternOffset.setStatus("current")


class _Hh3cDot11WIPSSigPatternMask_Type(OctetString):
    """Custom type hh3cDot11WIPSSigPatternMask based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 4),
    )


_Hh3cDot11WIPSSigPatternMask_Type.__name__ = "OctetString"
_Hh3cDot11WIPSSigPatternMask_Object = MibTableColumn
hh3cDot11WIPSSigPatternMask = _Hh3cDot11WIPSSigPatternMask_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 15, 1, 38, 1, 4),
    _Hh3cDot11WIPSSigPatternMask_Type()
)
hh3cDot11WIPSSigPatternMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cDot11WIPSSigPatternMask.setStatus("current")


class _Hh3cDot11WIPSSigPatternValue1_Type(Integer32):
    """Custom type hh3cDot11WIPSSigPatternValue1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Hh3cDot11WIPSSigPatternValue1_Type.__name__ = "Integer32"
_Hh3cDot11WIPSSigPatternValue1_Object = MibTableColumn
hh3cDot11WIPSSigPatternValue1 = _Hh3cDot11WIPSSigPatternValue1_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 15, 1, 38, 1, 5),
    _Hh3cDot11WIPSSigPatternValue1_Type()
)
hh3cDot11WIPSSigPatternValue1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cDot11WIPSSigPatternValue1.setStatus("current")


class _Hh3cDot11WIPSSigPatternValue2_Type(Integer32):
    """Custom type hh3cDot11WIPSSigPatternValue2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Hh3cDot11WIPSSigPatternValue2_Type.__name__ = "Integer32"
_Hh3cDot11WIPSSigPatternValue2_Object = MibTableColumn
hh3cDot11WIPSSigPatternValue2 = _Hh3cDot11WIPSSigPatternValue2_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 15, 1, 38, 1, 6),
    _Hh3cDot11WIPSSigPatternValue2_Type()
)
hh3cDot11WIPSSigPatternValue2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cDot11WIPSSigPatternValue2.setStatus("current")
_Hh3cDot11WIPSSigPatternFromPld_Type = TruthValue
_Hh3cDot11WIPSSigPatternFromPld_Object = MibTableColumn
hh3cDot11WIPSSigPatternFromPld = _Hh3cDot11WIPSSigPatternFromPld_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 15, 1, 38, 1, 7),
    _Hh3cDot11WIPSSigPatternFromPld_Type()
)
hh3cDot11WIPSSigPatternFromPld.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cDot11WIPSSigPatternFromPld.setStatus("current")
_Hh3cDot11WIPSSigPatternRowStatus_Type = RowStatus
_Hh3cDot11WIPSSigPatternRowStatus_Object = MibTableColumn
hh3cDot11WIPSSigPatternRowStatus = _Hh3cDot11WIPSSigPatternRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 15, 1, 38, 1, 8),
    _Hh3cDot11WIPSSigPatternRowStatus_Type()
)
hh3cDot11WIPSSigPatternRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cDot11WIPSSigPatternRowStatus.setStatus("current")
_Hh3cDot11WIPSSigSeqNumTable_Object = MibTable
hh3cDot11WIPSSigSeqNumTable = _Hh3cDot11WIPSSigSeqNumTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 15, 1, 39)
)
if mibBuilder.loadTexts:
    hh3cDot11WIPSSigSeqNumTable.setStatus("current")
_Hh3cDot11WIPSSigSeqNumEntry_Object = MibTableRow
hh3cDot11WIPSSigSeqNumEntry = _Hh3cDot11WIPSSigSeqNumEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 15, 1, 39, 1)
)
hh3cDot11WIPSSigSeqNumEntry.setIndexNames(
    (0, "HH3C-DOT11-WIPS-MIB", "hh3cDot11WIPSSigSeqNumRuleId"),
)
if mibBuilder.loadTexts:
    hh3cDot11WIPSSigSeqNumEntry.setStatus("current")


class _Hh3cDot11WIPSSigSeqNumRuleId_Type(Integer32):
    """Custom type hh3cDot11WIPSSigSeqNumRuleId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_Hh3cDot11WIPSSigSeqNumRuleId_Type.__name__ = "Integer32"
_Hh3cDot11WIPSSigSeqNumRuleId_Object = MibTableColumn
hh3cDot11WIPSSigSeqNumRuleId = _Hh3cDot11WIPSSigSeqNumRuleId_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 15, 1, 39, 1, 1),
    _Hh3cDot11WIPSSigSeqNumRuleId_Type()
)
hh3cDot11WIPSSigSeqNumRuleId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cDot11WIPSSigSeqNumRuleId.setStatus("current")


class _Hh3cDot11WIPSSigSeqNumValue1_Type(Integer32):
    """Custom type hh3cDot11WIPSSigSeqNumValue1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_Hh3cDot11WIPSSigSeqNumValue1_Type.__name__ = "Integer32"
_Hh3cDot11WIPSSigSeqNumValue1_Object = MibTableColumn
hh3cDot11WIPSSigSeqNumValue1 = _Hh3cDot11WIPSSigSeqNumValue1_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 15, 1, 39, 1, 2),
    _Hh3cDot11WIPSSigSeqNumValue1_Type()
)
hh3cDot11WIPSSigSeqNumValue1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDot11WIPSSigSeqNumValue1.setStatus("current")


class _Hh3cDot11WIPSSigSeqNumValue2_Type(Integer32):
    """Custom type hh3cDot11WIPSSigSeqNumValue2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_Hh3cDot11WIPSSigSeqNumValue2_Type.__name__ = "Integer32"
_Hh3cDot11WIPSSigSeqNumValue2_Object = MibTableColumn
hh3cDot11WIPSSigSeqNumValue2 = _Hh3cDot11WIPSSigSeqNumValue2_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 15, 1, 39, 1, 3),
    _Hh3cDot11WIPSSigSeqNumValue2_Type()
)
hh3cDot11WIPSSigSeqNumValue2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDot11WIPSSigSeqNumValue2.setStatus("current")
_Hh3cDot11WIPSSigSeqNumStatus_Type = Hh3cDot11WIPSEnabledStatus
_Hh3cDot11WIPSSigSeqNumStatus_Object = MibTableColumn
hh3cDot11WIPSSigSeqNumStatus = _Hh3cDot11WIPSSigSeqNumStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 15, 1, 39, 1, 4),
    _Hh3cDot11WIPSSigSeqNumStatus_Type()
)
hh3cDot11WIPSSigSeqNumStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDot11WIPSSigSeqNumStatus.setStatus("current")
_Hh3cDot11WIPSSigSsidTable_Object = MibTable
hh3cDot11WIPSSigSsidTable = _Hh3cDot11WIPSSigSsidTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 15, 1, 40)
)
if mibBuilder.loadTexts:
    hh3cDot11WIPSSigSsidTable.setStatus("current")
_Hh3cDot11WIPSSigSsidEntry_Object = MibTableRow
hh3cDot11WIPSSigSsidEntry = _Hh3cDot11WIPSSigSsidEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 15, 1, 40, 1)
)
hh3cDot11WIPSSigSsidEntry.setIndexNames(
    (0, "HH3C-DOT11-WIPS-MIB", "hh3cDot11WIPSSigSsidRuleId"),
)
if mibBuilder.loadTexts:
    hh3cDot11WIPSSigSsidEntry.setStatus("current")


class _Hh3cDot11WIPSSigSsidRuleId_Type(Integer32):
    """Custom type hh3cDot11WIPSSigSsidRuleId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_Hh3cDot11WIPSSigSsidRuleId_Type.__name__ = "Integer32"
_Hh3cDot11WIPSSigSsidRuleId_Object = MibTableColumn
hh3cDot11WIPSSigSsidRuleId = _Hh3cDot11WIPSSigSsidRuleId_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 15, 1, 40, 1, 1),
    _Hh3cDot11WIPSSigSsidRuleId_Type()
)
hh3cDot11WIPSSigSsidRuleId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cDot11WIPSSigSsidRuleId.setStatus("current")


class _Hh3cDot11WIPSSigSsidSsid_Type(OctetString):
    """Custom type hh3cDot11WIPSSigSsidSsid based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_Hh3cDot11WIPSSigSsidSsid_Type.__name__ = "OctetString"
_Hh3cDot11WIPSSigSsidSsid_Object = MibTableColumn
hh3cDot11WIPSSigSsidSsid = _Hh3cDot11WIPSSigSsidSsid_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 15, 1, 40, 1, 2),
    _Hh3cDot11WIPSSigSsidSsid_Type()
)
hh3cDot11WIPSSigSsidSsid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDot11WIPSSigSsidSsid.setStatus("current")
_Hh3cDot11WIPSSigSsidCase_Type = TruthValue
_Hh3cDot11WIPSSigSsidCase_Object = MibTableColumn
hh3cDot11WIPSSigSsidCase = _Hh3cDot11WIPSSigSsidCase_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 15, 1, 40, 1, 3),
    _Hh3cDot11WIPSSigSsidCase_Type()
)
hh3cDot11WIPSSigSsidCase.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDot11WIPSSigSsidCase.setStatus("current")
_Hh3cDot11WIPSSigSsidMatchType_Type = Hh3cDot11WIPSSigSsidMatchTypes
_Hh3cDot11WIPSSigSsidMatchType_Object = MibTableColumn
hh3cDot11WIPSSigSsidMatchType = _Hh3cDot11WIPSSigSsidMatchType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 15, 1, 40, 1, 4),
    _Hh3cDot11WIPSSigSsidMatchType_Type()
)
hh3cDot11WIPSSigSsidMatchType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDot11WIPSSigSsidMatchType.setStatus("current")
_Hh3cDot11WIPSSigSsidStatus_Type = Hh3cDot11WIPSEnabledStatus
_Hh3cDot11WIPSSigSsidStatus_Object = MibTableColumn
hh3cDot11WIPSSigSsidStatus = _Hh3cDot11WIPSSigSsidStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 15, 1, 40, 1, 5),
    _Hh3cDot11WIPSSigSsidStatus_Type()
)
hh3cDot11WIPSSigSsidStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDot11WIPSSigSsidStatus.setStatus("current")
_Hh3cDot11WIPSSigSsidLengthTable_Object = MibTable
hh3cDot11WIPSSigSsidLengthTable = _Hh3cDot11WIPSSigSsidLengthTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 15, 1, 41)
)
if mibBuilder.loadTexts:
    hh3cDot11WIPSSigSsidLengthTable.setStatus("current")
_Hh3cDot11WIPSSigSsidLengthEntry_Object = MibTableRow
hh3cDot11WIPSSigSsidLengthEntry = _Hh3cDot11WIPSSigSsidLengthEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 15, 1, 41, 1)
)
hh3cDot11WIPSSigSsidLengthEntry.setIndexNames(
    (0, "HH3C-DOT11-WIPS-MIB", "hh3cDot11WIPSSigSsidLengthRuleId"),
)
if mibBuilder.loadTexts:
    hh3cDot11WIPSSigSsidLengthEntry.setStatus("current")


class _Hh3cDot11WIPSSigSsidLengthRuleId_Type(Integer32):
    """Custom type hh3cDot11WIPSSigSsidLengthRuleId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_Hh3cDot11WIPSSigSsidLengthRuleId_Type.__name__ = "Integer32"
_Hh3cDot11WIPSSigSsidLengthRuleId_Object = MibTableColumn
hh3cDot11WIPSSigSsidLengthRuleId = _Hh3cDot11WIPSSigSsidLengthRuleId_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 15, 1, 41, 1, 1),
    _Hh3cDot11WIPSSigSsidLengthRuleId_Type()
)
hh3cDot11WIPSSigSsidLengthRuleId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cDot11WIPSSigSsidLengthRuleId.setStatus("current")


class _Hh3cDot11WIPSSigSsidLengthValue1_Type(Integer32):
    """Custom type hh3cDot11WIPSSigSsidLengthValue1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_Hh3cDot11WIPSSigSsidLengthValue1_Type.__name__ = "Integer32"
_Hh3cDot11WIPSSigSsidLengthValue1_Object = MibTableColumn
hh3cDot11WIPSSigSsidLengthValue1 = _Hh3cDot11WIPSSigSsidLengthValue1_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 15, 1, 41, 1, 2),
    _Hh3cDot11WIPSSigSsidLengthValue1_Type()
)
hh3cDot11WIPSSigSsidLengthValue1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDot11WIPSSigSsidLengthValue1.setStatus("current")


class _Hh3cDot11WIPSSigSsidLengthValue2_Type(Integer32):
    """Custom type hh3cDot11WIPSSigSsidLengthValue2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_Hh3cDot11WIPSSigSsidLengthValue2_Type.__name__ = "Integer32"
_Hh3cDot11WIPSSigSsidLengthValue2_Object = MibTableColumn
hh3cDot11WIPSSigSsidLengthValue2 = _Hh3cDot11WIPSSigSsidLengthValue2_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 15, 1, 41, 1, 3),
    _Hh3cDot11WIPSSigSsidLengthValue2_Type()
)
hh3cDot11WIPSSigSsidLengthValue2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDot11WIPSSigSsidLengthValue2.setStatus("current")
_Hh3cDot11WIPSSigSsidLengthStatus_Type = Hh3cDot11WIPSEnabledStatus
_Hh3cDot11WIPSSigSsidLengthStatus_Object = MibTableColumn
hh3cDot11WIPSSigSsidLengthStatus = _Hh3cDot11WIPSSigSsidLengthStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 15, 1, 41, 1, 4),
    _Hh3cDot11WIPSSigSsidLengthStatus_Type()
)
hh3cDot11WIPSSigSsidLengthStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDot11WIPSSigSsidLengthStatus.setStatus("current")
_Hh3cDot11WIPSFldDetectTable_Object = MibTable
hh3cDot11WIPSFldDetectTable = _Hh3cDot11WIPSFldDetectTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 15, 1, 42)
)
if mibBuilder.loadTexts:
    hh3cDot11WIPSFldDetectTable.setStatus("current")
_Hh3cDot11WIPSFldDetectEntry_Object = MibTableRow
hh3cDot11WIPSFldDetectEntry = _Hh3cDot11WIPSFldDetectEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 15, 1, 42, 1)
)
hh3cDot11WIPSFldDetectEntry.setIndexNames(
    (0, "HH3C-DOT11-WIPS-MIB", "hh3cDot11WIPSFldDetectPlyName"),
    (0, "HH3C-DOT11-WIPS-MIB", "hh3cDot11WIPSFldDetectType"),
)
if mibBuilder.loadTexts:
    hh3cDot11WIPSFldDetectEntry.setStatus("current")


class _Hh3cDot11WIPSFldDetectPlyName_Type(OctetString):
    """Custom type hh3cDot11WIPSFldDetectPlyName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 63),
    )


_Hh3cDot11WIPSFldDetectPlyName_Type.__name__ = "OctetString"
_Hh3cDot11WIPSFldDetectPlyName_Object = MibTableColumn
hh3cDot11WIPSFldDetectPlyName = _Hh3cDot11WIPSFldDetectPlyName_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 15, 1, 42, 1, 1),
    _Hh3cDot11WIPSFldDetectPlyName_Type()
)
hh3cDot11WIPSFldDetectPlyName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cDot11WIPSFldDetectPlyName.setStatus("current")
_Hh3cDot11WIPSFldDetectType_Type = Hh3cDot11WIPSFldDctType
_Hh3cDot11WIPSFldDetectType_Object = MibTableColumn
hh3cDot11WIPSFldDetectType = _Hh3cDot11WIPSFldDetectType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 15, 1, 42, 1, 2),
    _Hh3cDot11WIPSFldDetectType_Type()
)
hh3cDot11WIPSFldDetectType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cDot11WIPSFldDetectType.setStatus("current")


class _Hh3cDot11WIPSFldDetectInter_Type(Integer32):
    """Custom type hh3cDot11WIPSFldDetectInter based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3600),
    )


_Hh3cDot11WIPSFldDetectInter_Type.__name__ = "Integer32"
_Hh3cDot11WIPSFldDetectInter_Object = MibTableColumn
hh3cDot11WIPSFldDetectInter = _Hh3cDot11WIPSFldDetectInter_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 15, 1, 42, 1, 3),
    _Hh3cDot11WIPSFldDetectInter_Type()
)
hh3cDot11WIPSFldDetectInter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDot11WIPSFldDetectInter.setStatus("current")


class _Hh3cDot11WIPSFldDetectThresh_Type(Integer32):
    """Custom type hh3cDot11WIPSFldDetectThresh based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100000),
    )


_Hh3cDot11WIPSFldDetectThresh_Type.__name__ = "Integer32"
_Hh3cDot11WIPSFldDetectThresh_Object = MibTableColumn
hh3cDot11WIPSFldDetectThresh = _Hh3cDot11WIPSFldDetectThresh_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 15, 1, 42, 1, 4),
    _Hh3cDot11WIPSFldDetectThresh_Type()
)
hh3cDot11WIPSFldDetectThresh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDot11WIPSFldDetectThresh.setStatus("current")


class _Hh3cDot11WIPSFldDetectQuiet_Type(Integer32):
    """Custom type hh3cDot11WIPSFldDetectQuiet based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 604800),
    )


_Hh3cDot11WIPSFldDetectQuiet_Type.__name__ = "Integer32"
_Hh3cDot11WIPSFldDetectQuiet_Object = MibTableColumn
hh3cDot11WIPSFldDetectQuiet = _Hh3cDot11WIPSFldDetectQuiet_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 15, 1, 42, 1, 5),
    _Hh3cDot11WIPSFldDetectQuiet_Type()
)
hh3cDot11WIPSFldDetectQuiet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDot11WIPSFldDetectQuiet.setStatus("current")
_Hh3cDot11WIPSFldDetectStatus_Type = Hh3cDot11WIPSEnabledStatus
_Hh3cDot11WIPSFldDetectStatus_Object = MibTableColumn
hh3cDot11WIPSFldDetectStatus = _Hh3cDot11WIPSFldDetectStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 15, 1, 42, 1, 6),
    _Hh3cDot11WIPSFldDetectStatus_Type()
)
hh3cDot11WIPSFldDetectStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDot11WIPSFldDetectStatus.setStatus("current")
_Hh3cDot11WIPSSignatureMacTable_Object = MibTable
hh3cDot11WIPSSignatureMacTable = _Hh3cDot11WIPSSignatureMacTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 15, 1, 43)
)
if mibBuilder.loadTexts:
    hh3cDot11WIPSSignatureMacTable.setStatus("current")
_Hh3cDot11WIPSSignatureMacEntry_Object = MibTableRow
hh3cDot11WIPSSignatureMacEntry = _Hh3cDot11WIPSSignatureMacEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 15, 1, 43, 1)
)
hh3cDot11WIPSSignatureMacEntry.setIndexNames(
    (0, "HH3C-DOT11-WIPS-MIB", "hh3cDot11WIPSSignatureMacRuleId"),
)
if mibBuilder.loadTexts:
    hh3cDot11WIPSSignatureMacEntry.setStatus("current")


class _Hh3cDot11WIPSSignatureMacRuleId_Type(Integer32):
    """Custom type hh3cDot11WIPSSignatureMacRuleId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_Hh3cDot11WIPSSignatureMacRuleId_Type.__name__ = "Integer32"
_Hh3cDot11WIPSSignatureMacRuleId_Object = MibTableColumn
hh3cDot11WIPSSignatureMacRuleId = _Hh3cDot11WIPSSignatureMacRuleId_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 15, 1, 43, 1, 1),
    _Hh3cDot11WIPSSignatureMacRuleId_Type()
)
hh3cDot11WIPSSignatureMacRuleId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cDot11WIPSSignatureMacRuleId.setStatus("current")
_Hh3cDot11WIPSSignatureMacMacTyp_Type = Hh3cDot11WIPSSigMacMacType
_Hh3cDot11WIPSSignatureMacMacTyp_Object = MibTableColumn
hh3cDot11WIPSSignatureMacMacTyp = _Hh3cDot11WIPSSignatureMacMacTyp_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 15, 1, 43, 1, 2),
    _Hh3cDot11WIPSSignatureMacMacTyp_Type()
)
hh3cDot11WIPSSignatureMacMacTyp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDot11WIPSSignatureMacMacTyp.setStatus("current")
_Hh3cDot11WIPSSignatureMacMacAdd_Type = MacAddress
_Hh3cDot11WIPSSignatureMacMacAdd_Object = MibTableColumn
hh3cDot11WIPSSignatureMacMacAdd = _Hh3cDot11WIPSSignatureMacMacAdd_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 15, 1, 43, 1, 3),
    _Hh3cDot11WIPSSignatureMacMacAdd_Type()
)
hh3cDot11WIPSSignatureMacMacAdd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDot11WIPSSignatureMacMacAdd.setStatus("current")
_Hh3cDot11WIPSSignatureMacStatus_Type = Hh3cDot11WIPSEnabledStatus
_Hh3cDot11WIPSSignatureMacStatus_Object = MibTableColumn
hh3cDot11WIPSSignatureMacStatus = _Hh3cDot11WIPSSignatureMacStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 15, 1, 43, 1, 4),
    _Hh3cDot11WIPSSignatureMacStatus_Type()
)
hh3cDot11WIPSSignatureMacStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDot11WIPSSignatureMacStatus.setStatus("current")
_Hh3cDot11WIPSNatDetectTable_Object = MibTable
hh3cDot11WIPSNatDetectTable = _Hh3cDot11WIPSNatDetectTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 15, 1, 45)
)
if mibBuilder.loadTexts:
    hh3cDot11WIPSNatDetectTable.setStatus("current")
_Hh3cDot11WIPSNatDetectEntry_Object = MibTableRow
hh3cDot11WIPSNatDetectEntry = _Hh3cDot11WIPSNatDetectEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 15, 1, 45, 1)
)
hh3cDot11WIPSNatDetectEntry.setIndexNames(
    (0, "HH3C-DOT11-WIPS-MIB", "hh3cDot11WIPSNatDetectApName"),
)
if mibBuilder.loadTexts:
    hh3cDot11WIPSNatDetectEntry.setStatus("current")


class _Hh3cDot11WIPSNatDetectApName_Type(OctetString):
    """Custom type hh3cDot11WIPSNatDetectApName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_Hh3cDot11WIPSNatDetectApName_Type.__name__ = "OctetString"
_Hh3cDot11WIPSNatDetectApName_Object = MibTableColumn
hh3cDot11WIPSNatDetectApName = _Hh3cDot11WIPSNatDetectApName_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 15, 1, 45, 1, 1),
    _Hh3cDot11WIPSNatDetectApName_Type()
)
hh3cDot11WIPSNatDetectApName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cDot11WIPSNatDetectApName.setStatus("current")
_Hh3cDot11WIPSNatDetectStatus_Type = Hh3cDot11WIPSEnabledStatus
_Hh3cDot11WIPSNatDetectStatus_Object = MibTableColumn
hh3cDot11WIPSNatDetectStatus = _Hh3cDot11WIPSNatDetectStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 15, 1, 45, 1, 2),
    _Hh3cDot11WIPSNatDetectStatus_Type()
)
hh3cDot11WIPSNatDetectStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDot11WIPSNatDetectStatus.setStatus("current")
_Hh3cDot11WIPSDataGroup_ObjectIdentity = ObjectIdentity
hh3cDot11WIPSDataGroup = _Hh3cDot11WIPSDataGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 15, 2)
)
_Hh3cDot11WIPSDctAPTable_Object = MibTable
hh3cDot11WIPSDctAPTable = _Hh3cDot11WIPSDctAPTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 15, 2, 1)
)
if mibBuilder.loadTexts:
    hh3cDot11WIPSDctAPTable.setStatus("current")
_Hh3cDot11WIPSDctAPEntry_Object = MibTableRow
hh3cDot11WIPSDctAPEntry = _Hh3cDot11WIPSDctAPEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 15, 2, 1, 1)
)
hh3cDot11WIPSDctAPEntry.setIndexNames(
    (0, "HH3C-DOT11-WIPS-MIB", "hh3cDot11WIPSDctAPVSD"),
    (0, "HH3C-DOT11-WIPS-MIB", "hh3cDot11WIPSDctAPMac"),
)
if mibBuilder.loadTexts:
    hh3cDot11WIPSDctAPEntry.setStatus("current")


class _Hh3cDot11WIPSDctAPVSD_Type(OctetString):
    """Custom type hh3cDot11WIPSDctAPVSD based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 63),
    )


_Hh3cDot11WIPSDctAPVSD_Type.__name__ = "OctetString"
_Hh3cDot11WIPSDctAPVSD_Object = MibTableColumn
hh3cDot11WIPSDctAPVSD = _Hh3cDot11WIPSDctAPVSD_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 15, 2, 1, 1, 1),
    _Hh3cDot11WIPSDctAPVSD_Type()
)
hh3cDot11WIPSDctAPVSD.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cDot11WIPSDctAPVSD.setStatus("current")
_Hh3cDot11WIPSDctAPMac_Type = MacAddress
_Hh3cDot11WIPSDctAPMac_Object = MibTableColumn
hh3cDot11WIPSDctAPMac = _Hh3cDot11WIPSDctAPMac_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 15, 2, 1, 1, 2),
    _Hh3cDot11WIPSDctAPMac_Type()
)
hh3cDot11WIPSDctAPMac.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cDot11WIPSDctAPMac.setStatus("current")
_Hh3cDot11WIPSDctAPClassifyWay_Type = Hh3cDot11WIPSDevClassifyWay
_Hh3cDot11WIPSDctAPClassifyWay_Object = MibTableColumn
hh3cDot11WIPSDctAPClassifyWay = _Hh3cDot11WIPSDctAPClassifyWay_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 15, 2, 1, 1, 3),
    _Hh3cDot11WIPSDctAPClassifyWay_Type()
)
hh3cDot11WIPSDctAPClassifyWay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11WIPSDctAPClassifyWay.setStatus("current")
_Hh3cDot11WIPSDctAPClassifyType_Type = Hh3cDot11WIPSAPClassifyType
_Hh3cDot11WIPSDctAPClassifyType_Object = MibTableColumn
hh3cDot11WIPSDctAPClassifyType = _Hh3cDot11WIPSDctAPClassifyType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 15, 2, 1, 1, 4),
    _Hh3cDot11WIPSDctAPClassifyType_Type()
)
hh3cDot11WIPSDctAPClassifyType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11WIPSDctAPClassifyType.setStatus("current")


class _Hh3cDot11WIPSDctAPSeverityLevel_Type(Unsigned32):
    """Custom type hh3cDot11WIPSDctAPSeverityLevel based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Hh3cDot11WIPSDctAPSeverityLevel_Type.__name__ = "Unsigned32"
_Hh3cDot11WIPSDctAPSeverityLevel_Object = MibTableColumn
hh3cDot11WIPSDctAPSeverityLevel = _Hh3cDot11WIPSDctAPSeverityLevel_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 15, 2, 1, 1, 5),
    _Hh3cDot11WIPSDctAPSeverityLevel_Type()
)
hh3cDot11WIPSDctAPSeverityLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11WIPSDctAPSeverityLevel.setStatus("current")
_Hh3cDot11WIPSDctAPStatus_Type = Hh3cDot11WIPSDevStatus
_Hh3cDot11WIPSDctAPStatus_Object = MibTableColumn
hh3cDot11WIPSDctAPStatus = _Hh3cDot11WIPSDctAPStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 15, 2, 1, 1, 6),
    _Hh3cDot11WIPSDctAPStatus_Type()
)
hh3cDot11WIPSDctAPStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11WIPSDctAPStatus.setStatus("current")
_Hh3cDot11WIPSDctAPStatusDut_Type = TimeTicks
_Hh3cDot11WIPSDctAPStatusDut_Object = MibTableColumn
hh3cDot11WIPSDctAPStatusDut = _Hh3cDot11WIPSDctAPStatusDut_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 15, 2, 1, 1, 7),
    _Hh3cDot11WIPSDctAPStatusDut_Type()
)
hh3cDot11WIPSDctAPStatusDut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11WIPSDctAPStatusDut.setStatus("current")


class _Hh3cDot11WIPSDctAPVendor_Type(OctetString):
    """Custom type hh3cDot11WIPSDctAPVendor based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_Hh3cDot11WIPSDctAPVendor_Type.__name__ = "OctetString"
_Hh3cDot11WIPSDctAPVendor_Object = MibTableColumn
hh3cDot11WIPSDctAPVendor = _Hh3cDot11WIPSDctAPVendor_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 15, 2, 1, 1, 8),
    _Hh3cDot11WIPSDctAPVendor_Type()
)
hh3cDot11WIPSDctAPVendor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11WIPSDctAPVendor.setStatus("current")


class _Hh3cDot11WIPSDctAPSSID_Type(OctetString):
    """Custom type hh3cDot11WIPSDctAPSSID based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Hh3cDot11WIPSDctAPSSID_Type.__name__ = "OctetString"
_Hh3cDot11WIPSDctAPSSID_Object = MibTableColumn
hh3cDot11WIPSDctAPSSID = _Hh3cDot11WIPSDctAPSSID_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 15, 2, 1, 1, 9),
    _Hh3cDot11WIPSDctAPSSID_Type()
)
hh3cDot11WIPSDctAPSSID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11WIPSDctAPSSID.setStatus("current")
_Hh3cDot11WIPSDctAPSecurity_Type = Hh3cDot11WIPSAPSecurityType
_Hh3cDot11WIPSDctAPSecurity_Object = MibTableColumn
hh3cDot11WIPSDctAPSecurity = _Hh3cDot11WIPSDctAPSecurity_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 15, 2, 1, 1, 10),
    _Hh3cDot11WIPSDctAPSecurity_Type()
)
hh3cDot11WIPSDctAPSecurity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11WIPSDctAPSecurity.setStatus("current")
_Hh3cDot11WIPSDctAPEncryptMethod_Type = Hh3cDot11WIPSEncryptMethod
_Hh3cDot11WIPSDctAPEncryptMethod_Object = MibTableColumn
hh3cDot11WIPSDctAPEncryptMethod = _Hh3cDot11WIPSDctAPEncryptMethod_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 15, 2, 1, 1, 11),
    _Hh3cDot11WIPSDctAPEncryptMethod_Type()
)
hh3cDot11WIPSDctAPEncryptMethod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11WIPSDctAPEncryptMethod.setStatus("current")
_Hh3cDot11WIPSDctAPAuthMethod_Type = Hh3cDot11WIPSAuthMethod
_Hh3cDot11WIPSDctAPAuthMethod_Object = MibTableColumn
hh3cDot11WIPSDctAPAuthMethod = _Hh3cDot11WIPSDctAPAuthMethod_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 15, 2, 1, 1, 12),
    _Hh3cDot11WIPSDctAPAuthMethod_Type()
)
hh3cDot11WIPSDctAPAuthMethod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11WIPSDctAPAuthMethod.setStatus("current")
_Hh3cDot11WIPSDctAPRadioType_Type = Hh3cDot11WIPSRadioType
_Hh3cDot11WIPSDctAPRadioType_Object = MibTableColumn
hh3cDot11WIPSDctAPRadioType = _Hh3cDot11WIPSDctAPRadioType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 15, 2, 1, 1, 13),
    _Hh3cDot11WIPSDctAPRadioType_Type()
)
hh3cDot11WIPSDctAPRadioType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11WIPSDctAPRadioType.setStatus("current")
_Hh3cDot11WIPSDctAPWorkChannel_Type = Hh3cDot11WIPSChannel
_Hh3cDot11WIPSDctAPWorkChannel_Object = MibTableColumn
hh3cDot11WIPSDctAPWorkChannel = _Hh3cDot11WIPSDctAPWorkChannel_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 15, 2, 1, 1, 14),
    _Hh3cDot11WIPSDctAPWorkChannel_Type()
)
hh3cDot11WIPSDctAPWorkChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11WIPSDctAPWorkChannel.setStatus("current")
_Hh3cDot11WIPSDctAPIsCountered_Type = TruthValue
_Hh3cDot11WIPSDctAPIsCountered_Object = MibTableColumn
hh3cDot11WIPSDctAPIsCountered = _Hh3cDot11WIPSDctAPIsCountered_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 15, 2, 1, 1, 15),
    _Hh3cDot11WIPSDctAPIsCountered_Type()
)
hh3cDot11WIPSDctAPIsCountered.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11WIPSDctAPIsCountered.setStatus("current")
_Hh3cDot11WIPSDctAPAttachStaNum_Type = Integer32
_Hh3cDot11WIPSDctAPAttachStaNum_Object = MibTableColumn
hh3cDot11WIPSDctAPAttachStaNum = _Hh3cDot11WIPSDctAPAttachStaNum_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 15, 2, 1, 1, 16),
    _Hh3cDot11WIPSDctAPAttachStaNum_Type()
)
hh3cDot11WIPSDctAPAttachStaNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11WIPSDctAPAttachStaNum.setStatus("current")
_Hh3cDot11WIPSDctAPRptSensorNum_Type = Integer32
_Hh3cDot11WIPSDctAPRptSensorNum_Object = MibTableColumn
hh3cDot11WIPSDctAPRptSensorNum = _Hh3cDot11WIPSDctAPRptSensorNum_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 15, 2, 1, 1, 17),
    _Hh3cDot11WIPSDctAPRptSensorNum_Type()
)
hh3cDot11WIPSDctAPRptSensorNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11WIPSDctAPRptSensorNum.setStatus("current")
_Hh3cDot11WIPSDctAPIsBdcastSSID_Type = TruthValue
_Hh3cDot11WIPSDctAPIsBdcastSSID_Object = MibTableColumn
hh3cDot11WIPSDctAPIsBdcastSSID = _Hh3cDot11WIPSDctAPIsBdcastSSID_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 15, 2, 1, 1, 18),
    _Hh3cDot11WIPSDctAPIsBdcastSSID_Type()
)
hh3cDot11WIPSDctAPIsBdcastSSID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11WIPSDctAPIsBdcastSSID.setStatus("current")
_Hh3cDot11WIPSDctAPType_Type = Hh3cDot11WIPSAPType
_Hh3cDot11WIPSDctAPType_Object = MibTableColumn
hh3cDot11WIPSDctAPType = _Hh3cDot11WIPSDctAPType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 15, 2, 1, 1, 19),
    _Hh3cDot11WIPSDctAPType_Type()
)
hh3cDot11WIPSDctAPType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11WIPSDctAPType.setStatus("current")
_Hh3cDot11WIPSDctAPIsQosSported_Type = TruthValue
_Hh3cDot11WIPSDctAPIsQosSported_Object = MibTableColumn
hh3cDot11WIPSDctAPIsQosSported = _Hh3cDot11WIPSDctAPIsQosSported_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 15, 2, 1, 1, 20),
    _Hh3cDot11WIPSDctAPIsQosSported_Type()
)
hh3cDot11WIPSDctAPIsQosSported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11WIPSDctAPIsQosSported.setStatus("current")
_Hh3cDot11WIPSDctAPBeaconItv_Type = Integer32
_Hh3cDot11WIPSDctAPBeaconItv_Object = MibTableColumn
hh3cDot11WIPSDctAPBeaconItv = _Hh3cDot11WIPSDctAPBeaconItv_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 15, 2, 1, 1, 21),
    _Hh3cDot11WIPSDctAPBeaconItv_Type()
)
hh3cDot11WIPSDctAPBeaconItv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11WIPSDctAPBeaconItv.setStatus("current")
_Hh3cDot11WIPSDctAPUpDuration_Type = TimeTicks
_Hh3cDot11WIPSDctAPUpDuration_Object = MibTableColumn
hh3cDot11WIPSDctAPUpDuration = _Hh3cDot11WIPSDctAPUpDuration_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 15, 2, 1, 1, 22),
    _Hh3cDot11WIPSDctAPUpDuration_Type()
)
hh3cDot11WIPSDctAPUpDuration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11WIPSDctAPUpDuration.setStatus("current")
_Hh3cDot11WIPSDctStaTable_Object = MibTable
hh3cDot11WIPSDctStaTable = _Hh3cDot11WIPSDctStaTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 15, 2, 2)
)
if mibBuilder.loadTexts:
    hh3cDot11WIPSDctStaTable.setStatus("current")
_Hh3cDot11WIPSDctStaEntry_Object = MibTableRow
hh3cDot11WIPSDctStaEntry = _Hh3cDot11WIPSDctStaEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 15, 2, 2, 1)
)
hh3cDot11WIPSDctStaEntry.setIndexNames(
    (0, "HH3C-DOT11-WIPS-MIB", "hh3cDot11WIPSDctStaVSD"),
    (0, "HH3C-DOT11-WIPS-MIB", "hh3cDot11WIPSDctStaMac"),
)
if mibBuilder.loadTexts:
    hh3cDot11WIPSDctStaEntry.setStatus("current")


class _Hh3cDot11WIPSDctStaVSD_Type(OctetString):
    """Custom type hh3cDot11WIPSDctStaVSD based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 63),
    )


_Hh3cDot11WIPSDctStaVSD_Type.__name__ = "OctetString"
_Hh3cDot11WIPSDctStaVSD_Object = MibTableColumn
hh3cDot11WIPSDctStaVSD = _Hh3cDot11WIPSDctStaVSD_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 15, 2, 2, 1, 1),
    _Hh3cDot11WIPSDctStaVSD_Type()
)
hh3cDot11WIPSDctStaVSD.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cDot11WIPSDctStaVSD.setStatus("current")
_Hh3cDot11WIPSDctStaMac_Type = MacAddress
_Hh3cDot11WIPSDctStaMac_Object = MibTableColumn
hh3cDot11WIPSDctStaMac = _Hh3cDot11WIPSDctStaMac_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 15, 2, 2, 1, 2),
    _Hh3cDot11WIPSDctStaMac_Type()
)
hh3cDot11WIPSDctStaMac.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cDot11WIPSDctStaMac.setStatus("current")
_Hh3cDot11WIPSDctStaAssocBSSID_Type = MacAddress
_Hh3cDot11WIPSDctStaAssocBSSID_Object = MibTableColumn
hh3cDot11WIPSDctStaAssocBSSID = _Hh3cDot11WIPSDctStaAssocBSSID_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 15, 2, 2, 1, 3),
    _Hh3cDot11WIPSDctStaAssocBSSID_Type()
)
hh3cDot11WIPSDctStaAssocBSSID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11WIPSDctStaAssocBSSID.setStatus("current")
_Hh3cDot11WIPSDctStaClassifyWay_Type = Hh3cDot11WIPSDevClassifyWay
_Hh3cDot11WIPSDctStaClassifyWay_Object = MibTableColumn
hh3cDot11WIPSDctStaClassifyWay = _Hh3cDot11WIPSDctStaClassifyWay_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 15, 2, 2, 1, 4),
    _Hh3cDot11WIPSDctStaClassifyWay_Type()
)
hh3cDot11WIPSDctStaClassifyWay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11WIPSDctStaClassifyWay.setStatus("current")
_Hh3cDot11WIPSDctStaClassifyType_Type = Hh3cDot11WIPSStaClassifyType
_Hh3cDot11WIPSDctStaClassifyType_Object = MibTableColumn
hh3cDot11WIPSDctStaClassifyType = _Hh3cDot11WIPSDctStaClassifyType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 15, 2, 2, 1, 5),
    _Hh3cDot11WIPSDctStaClassifyType_Type()
)
hh3cDot11WIPSDctStaClassifyType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11WIPSDctStaClassifyType.setStatus("current")


class _Hh3cDot11WIPSDctStaSeverityLevel_Type(Unsigned32):
    """Custom type hh3cDot11WIPSDctStaSeverityLevel based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Hh3cDot11WIPSDctStaSeverityLevel_Type.__name__ = "Unsigned32"
_Hh3cDot11WIPSDctStaSeverityLevel_Object = MibTableColumn
hh3cDot11WIPSDctStaSeverityLevel = _Hh3cDot11WIPSDctStaSeverityLevel_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 15, 2, 2, 1, 6),
    _Hh3cDot11WIPSDctStaSeverityLevel_Type()
)
hh3cDot11WIPSDctStaSeverityLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11WIPSDctStaSeverityLevel.setStatus("current")
_Hh3cDot11WIPSDctStaIsDissociate_Type = TruthValue
_Hh3cDot11WIPSDctStaIsDissociate_Object = MibTableColumn
hh3cDot11WIPSDctStaIsDissociate = _Hh3cDot11WIPSDctStaIsDissociate_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 15, 2, 2, 1, 7),
    _Hh3cDot11WIPSDctStaIsDissociate_Type()
)
hh3cDot11WIPSDctStaIsDissociate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11WIPSDctStaIsDissociate.setStatus("current")
_Hh3cDot11WIPSDctStaStatus_Type = Hh3cDot11WIPSDevStatus
_Hh3cDot11WIPSDctStaStatus_Object = MibTableColumn
hh3cDot11WIPSDctStaStatus = _Hh3cDot11WIPSDctStaStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 15, 2, 2, 1, 8),
    _Hh3cDot11WIPSDctStaStatus_Type()
)
hh3cDot11WIPSDctStaStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11WIPSDctStaStatus.setStatus("current")
_Hh3cDot11WIPSDctStaStatusDurat_Type = TimeTicks
_Hh3cDot11WIPSDctStaStatusDurat_Object = MibTableColumn
hh3cDot11WIPSDctStaStatusDurat = _Hh3cDot11WIPSDctStaStatusDurat_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 15, 2, 2, 1, 9),
    _Hh3cDot11WIPSDctStaStatusDurat_Type()
)
hh3cDot11WIPSDctStaStatusDurat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11WIPSDctStaStatusDurat.setStatus("current")


class _Hh3cDot11WIPSDctStaVendor_Type(OctetString):
    """Custom type hh3cDot11WIPSDctStaVendor based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_Hh3cDot11WIPSDctStaVendor_Type.__name__ = "OctetString"
_Hh3cDot11WIPSDctStaVendor_Object = MibTableColumn
hh3cDot11WIPSDctStaVendor = _Hh3cDot11WIPSDctStaVendor_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 15, 2, 2, 1, 10),
    _Hh3cDot11WIPSDctStaVendor_Type()
)
hh3cDot11WIPSDctStaVendor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11WIPSDctStaVendor.setStatus("current")
_Hh3cDot11WIPSDctStaRadioType_Type = Hh3cDot11WIPSRadioType
_Hh3cDot11WIPSDctStaRadioType_Object = MibTableColumn
hh3cDot11WIPSDctStaRadioType = _Hh3cDot11WIPSDctStaRadioType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 15, 2, 2, 1, 11),
    _Hh3cDot11WIPSDctStaRadioType_Type()
)
hh3cDot11WIPSDctStaRadioType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11WIPSDctStaRadioType.setStatus("current")
_Hh3cDot11WIPSDctStaRptSensorNum_Type = Integer32
_Hh3cDot11WIPSDctStaRptSensorNum_Object = MibTableColumn
hh3cDot11WIPSDctStaRptSensorNum = _Hh3cDot11WIPSDctStaRptSensorNum_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 15, 2, 2, 1, 12),
    _Hh3cDot11WIPSDctStaRptSensorNum_Type()
)
hh3cDot11WIPSDctStaRptSensorNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11WIPSDctStaRptSensorNum.setStatus("current")
_Hh3cDot11WIPSDctStaWorkChannel_Type = Hh3cDot11WIPSChannel
_Hh3cDot11WIPSDctStaWorkChannel_Object = MibTableColumn
hh3cDot11WIPSDctStaWorkChannel = _Hh3cDot11WIPSDctStaWorkChannel_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 15, 2, 2, 1, 13),
    _Hh3cDot11WIPSDctStaWorkChannel_Type()
)
hh3cDot11WIPSDctStaWorkChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11WIPSDctStaWorkChannel.setStatus("current")
_Hh3cDot11WIPSDctStaIsCountered_Type = TruthValue
_Hh3cDot11WIPSDctStaIsCountered_Object = MibTableColumn
hh3cDot11WIPSDctStaIsCountered = _Hh3cDot11WIPSDctStaIsCountered_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 15, 2, 2, 1, 14),
    _Hh3cDot11WIPSDctStaIsCountered_Type()
)
hh3cDot11WIPSDctStaIsCountered.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11WIPSDctStaIsCountered.setStatus("current")
_Hh3cDot11WIPSApAssoCltTable_Object = MibTable
hh3cDot11WIPSApAssoCltTable = _Hh3cDot11WIPSApAssoCltTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 15, 2, 3)
)
if mibBuilder.loadTexts:
    hh3cDot11WIPSApAssoCltTable.setStatus("current")
_Hh3cDot11WIPSApAssoCltEntry_Object = MibTableRow
hh3cDot11WIPSApAssoCltEntry = _Hh3cDot11WIPSApAssoCltEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 15, 2, 3, 1)
)
hh3cDot11WIPSApAssoCltEntry.setIndexNames(
    (0, "HH3C-DOT11-WIPS-MIB", "hh3cDot11WIPSApAssoCltVSDName"),
    (0, "HH3C-DOT11-WIPS-MIB", "hh3cDot11WIPSApAssoCltApMacAddr"),
    (0, "HH3C-DOT11-WIPS-MIB", "hh3cDot11WIPSApAssoCltClMacAddr"),
)
if mibBuilder.loadTexts:
    hh3cDot11WIPSApAssoCltEntry.setStatus("current")


class _Hh3cDot11WIPSApAssoCltVSDName_Type(OctetString):
    """Custom type hh3cDot11WIPSApAssoCltVSDName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 63),
    )


_Hh3cDot11WIPSApAssoCltVSDName_Type.__name__ = "OctetString"
_Hh3cDot11WIPSApAssoCltVSDName_Object = MibTableColumn
hh3cDot11WIPSApAssoCltVSDName = _Hh3cDot11WIPSApAssoCltVSDName_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 15, 2, 3, 1, 1),
    _Hh3cDot11WIPSApAssoCltVSDName_Type()
)
hh3cDot11WIPSApAssoCltVSDName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cDot11WIPSApAssoCltVSDName.setStatus("current")
_Hh3cDot11WIPSApAssoCltApMacAddr_Type = MacAddress
_Hh3cDot11WIPSApAssoCltApMacAddr_Object = MibTableColumn
hh3cDot11WIPSApAssoCltApMacAddr = _Hh3cDot11WIPSApAssoCltApMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 15, 2, 3, 1, 2),
    _Hh3cDot11WIPSApAssoCltApMacAddr_Type()
)
hh3cDot11WIPSApAssoCltApMacAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cDot11WIPSApAssoCltApMacAddr.setStatus("current")
_Hh3cDot11WIPSApAssoCltClMacAddr_Type = MacAddress
_Hh3cDot11WIPSApAssoCltClMacAddr_Object = MibTableColumn
hh3cDot11WIPSApAssoCltClMacAddr = _Hh3cDot11WIPSApAssoCltClMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 15, 2, 3, 1, 3),
    _Hh3cDot11WIPSApAssoCltClMacAddr_Type()
)
hh3cDot11WIPSApAssoCltClMacAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cDot11WIPSApAssoCltClMacAddr.setStatus("current")
_Hh3cDot11WIPSApAssoCltIsAsso_Type = TruthValue
_Hh3cDot11WIPSApAssoCltIsAsso_Object = MibTableColumn
hh3cDot11WIPSApAssoCltIsAsso = _Hh3cDot11WIPSApAssoCltIsAsso_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 15, 2, 3, 1, 4),
    _Hh3cDot11WIPSApAssoCltIsAsso_Type()
)
hh3cDot11WIPSApAssoCltIsAsso.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11WIPSApAssoCltIsAsso.setStatus("current")
_Hh3cDot11WIPSApRpSenTable_Object = MibTable
hh3cDot11WIPSApRpSenTable = _Hh3cDot11WIPSApRpSenTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 15, 2, 4)
)
if mibBuilder.loadTexts:
    hh3cDot11WIPSApRpSenTable.setStatus("current")
_Hh3cDot11WIPSApRpSenEntry_Object = MibTableRow
hh3cDot11WIPSApRpSenEntry = _Hh3cDot11WIPSApRpSenEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 15, 2, 4, 1)
)
hh3cDot11WIPSApRpSenEntry.setIndexNames(
    (0, "HH3C-DOT11-WIPS-MIB", "hh3cDot11WIPSApRpSenVsdName"),
    (0, "HH3C-DOT11-WIPS-MIB", "hh3cDot11WIPSApRpSenMacAddr"),
    (0, "HH3C-DOT11-WIPS-MIB", "hh3cDot11WIPSApRpSenName"),
)
if mibBuilder.loadTexts:
    hh3cDot11WIPSApRpSenEntry.setStatus("current")


class _Hh3cDot11WIPSApRpSenVsdName_Type(OctetString):
    """Custom type hh3cDot11WIPSApRpSenVsdName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 63),
    )


_Hh3cDot11WIPSApRpSenVsdName_Type.__name__ = "OctetString"
_Hh3cDot11WIPSApRpSenVsdName_Object = MibTableColumn
hh3cDot11WIPSApRpSenVsdName = _Hh3cDot11WIPSApRpSenVsdName_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 15, 2, 4, 1, 1),
    _Hh3cDot11WIPSApRpSenVsdName_Type()
)
hh3cDot11WIPSApRpSenVsdName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cDot11WIPSApRpSenVsdName.setStatus("current")
_Hh3cDot11WIPSApRpSenMacAddr_Type = MacAddress
_Hh3cDot11WIPSApRpSenMacAddr_Object = MibTableColumn
hh3cDot11WIPSApRpSenMacAddr = _Hh3cDot11WIPSApRpSenMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 15, 2, 4, 1, 2),
    _Hh3cDot11WIPSApRpSenMacAddr_Type()
)
hh3cDot11WIPSApRpSenMacAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cDot11WIPSApRpSenMacAddr.setStatus("current")


class _Hh3cDot11WIPSApRpSenName_Type(OctetString):
    """Custom type hh3cDot11WIPSApRpSenName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_Hh3cDot11WIPSApRpSenName_Type.__name__ = "OctetString"
_Hh3cDot11WIPSApRpSenName_Object = MibTableColumn
hh3cDot11WIPSApRpSenName = _Hh3cDot11WIPSApRpSenName_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 15, 2, 4, 1, 3),
    _Hh3cDot11WIPSApRpSenName_Type()
)
hh3cDot11WIPSApRpSenName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cDot11WIPSApRpSenName.setStatus("current")
_Hh3cDot11WIPSApRpSenRadioID_Type = Integer32
_Hh3cDot11WIPSApRpSenRadioID_Object = MibTableColumn
hh3cDot11WIPSApRpSenRadioID = _Hh3cDot11WIPSApRpSenRadioID_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 15, 2, 4, 1, 4),
    _Hh3cDot11WIPSApRpSenRadioID_Type()
)
hh3cDot11WIPSApRpSenRadioID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11WIPSApRpSenRadioID.setStatus("current")
_Hh3cDot11WIPSApRpSenRssi_Type = Integer32
_Hh3cDot11WIPSApRpSenRssi_Object = MibTableColumn
hh3cDot11WIPSApRpSenRssi = _Hh3cDot11WIPSApRpSenRssi_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 15, 2, 4, 1, 5),
    _Hh3cDot11WIPSApRpSenRssi_Type()
)
hh3cDot11WIPSApRpSenRssi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11WIPSApRpSenRssi.setStatus("current")
_Hh3cDot11WIPSApRpSenChannel_Type = Integer32
_Hh3cDot11WIPSApRpSenChannel_Object = MibTableColumn
hh3cDot11WIPSApRpSenChannel = _Hh3cDot11WIPSApRpSenChannel_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 15, 2, 4, 1, 6),
    _Hh3cDot11WIPSApRpSenChannel_Type()
)
hh3cDot11WIPSApRpSenChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11WIPSApRpSenChannel.setStatus("current")


class _Hh3cDot11WIPSApRpSenFirstRpTime_Type(OctetString):
    """Custom type hh3cDot11WIPSApRpSenFirstRpTime based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 256),
    )


_Hh3cDot11WIPSApRpSenFirstRpTime_Type.__name__ = "OctetString"
_Hh3cDot11WIPSApRpSenFirstRpTime_Object = MibTableColumn
hh3cDot11WIPSApRpSenFirstRpTime = _Hh3cDot11WIPSApRpSenFirstRpTime_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 15, 2, 4, 1, 7),
    _Hh3cDot11WIPSApRpSenFirstRpTime_Type()
)
hh3cDot11WIPSApRpSenFirstRpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11WIPSApRpSenFirstRpTime.setStatus("current")


class _Hh3cDot11WIPSApRpSenLastRpTime_Type(OctetString):
    """Custom type hh3cDot11WIPSApRpSenLastRpTime based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 256),
    )


_Hh3cDot11WIPSApRpSenLastRpTime_Type.__name__ = "OctetString"
_Hh3cDot11WIPSApRpSenLastRpTime_Object = MibTableColumn
hh3cDot11WIPSApRpSenLastRpTime = _Hh3cDot11WIPSApRpSenLastRpTime_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 15, 2, 4, 1, 8),
    _Hh3cDot11WIPSApRpSenLastRpTime_Type()
)
hh3cDot11WIPSApRpSenLastRpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11WIPSApRpSenLastRpTime.setStatus("current")
_Hh3cDot11WIPSCtmRecTable_Object = MibTable
hh3cDot11WIPSCtmRecTable = _Hh3cDot11WIPSCtmRecTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 15, 2, 5)
)
if mibBuilder.loadTexts:
    hh3cDot11WIPSCtmRecTable.setStatus("current")
_Hh3cDot11WIPSCtmRecEntry_Object = MibTableRow
hh3cDot11WIPSCtmRecEntry = _Hh3cDot11WIPSCtmRecEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 15, 2, 5, 1)
)
hh3cDot11WIPSCtmRecEntry.setIndexNames(
    (0, "HH3C-DOT11-WIPS-MIB", "hh3cDot11WIPSCtmRecVsdName"),
    (0, "HH3C-DOT11-WIPS-MIB", "hh3cDot11WIPSCtmRecMacAddress"),
    (0, "HH3C-DOT11-WIPS-MIB", "hh3cDot11WIPSCtmRecCount"),
)
if mibBuilder.loadTexts:
    hh3cDot11WIPSCtmRecEntry.setStatus("current")


class _Hh3cDot11WIPSCtmRecVsdName_Type(OctetString):
    """Custom type hh3cDot11WIPSCtmRecVsdName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 63),
    )


_Hh3cDot11WIPSCtmRecVsdName_Type.__name__ = "OctetString"
_Hh3cDot11WIPSCtmRecVsdName_Object = MibTableColumn
hh3cDot11WIPSCtmRecVsdName = _Hh3cDot11WIPSCtmRecVsdName_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 15, 2, 5, 1, 1),
    _Hh3cDot11WIPSCtmRecVsdName_Type()
)
hh3cDot11WIPSCtmRecVsdName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cDot11WIPSCtmRecVsdName.setStatus("current")
_Hh3cDot11WIPSCtmRecMacAddress_Type = MacAddress
_Hh3cDot11WIPSCtmRecMacAddress_Object = MibTableColumn
hh3cDot11WIPSCtmRecMacAddress = _Hh3cDot11WIPSCtmRecMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 15, 2, 5, 1, 2),
    _Hh3cDot11WIPSCtmRecMacAddress_Type()
)
hh3cDot11WIPSCtmRecMacAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cDot11WIPSCtmRecMacAddress.setStatus("current")


class _Hh3cDot11WIPSCtmRecCount_Type(Integer32):
    """Custom type hh3cDot11WIPSCtmRecCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_Hh3cDot11WIPSCtmRecCount_Type.__name__ = "Integer32"
_Hh3cDot11WIPSCtmRecCount_Object = MibTableColumn
hh3cDot11WIPSCtmRecCount = _Hh3cDot11WIPSCtmRecCount_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 15, 2, 5, 1, 3),
    _Hh3cDot11WIPSCtmRecCount_Type()
)
hh3cDot11WIPSCtmRecCount.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cDot11WIPSCtmRecCount.setStatus("current")


class _Hh3cDot11WIPSCtmRecSensorName_Type(OctetString):
    """Custom type hh3cDot11WIPSCtmRecSensorName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_Hh3cDot11WIPSCtmRecSensorName_Type.__name__ = "OctetString"
_Hh3cDot11WIPSCtmRecSensorName_Object = MibTableColumn
hh3cDot11WIPSCtmRecSensorName = _Hh3cDot11WIPSCtmRecSensorName_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 15, 2, 5, 1, 4),
    _Hh3cDot11WIPSCtmRecSensorName_Type()
)
hh3cDot11WIPSCtmRecSensorName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11WIPSCtmRecSensorName.setStatus("current")
_Hh3cDot11WIPSCtmRecDeviceType_Type = Hh3cDot11WIPSDeviceType
_Hh3cDot11WIPSCtmRecDeviceType_Object = MibTableColumn
hh3cDot11WIPSCtmRecDeviceType = _Hh3cDot11WIPSCtmRecDeviceType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 15, 2, 5, 1, 5),
    _Hh3cDot11WIPSCtmRecDeviceType_Type()
)
hh3cDot11WIPSCtmRecDeviceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11WIPSCtmRecDeviceType.setStatus("current")
_Hh3cDot11WIPSCtmRecClassifyType_Type = Hh3cDot11WIPSClassifyType
_Hh3cDot11WIPSCtmRecClassifyType_Object = MibTableColumn
hh3cDot11WIPSCtmRecClassifyType = _Hh3cDot11WIPSCtmRecClassifyType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 15, 2, 5, 1, 6),
    _Hh3cDot11WIPSCtmRecClassifyType_Type()
)
hh3cDot11WIPSCtmRecClassifyType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11WIPSCtmRecClassifyType.setStatus("current")
_Hh3cDot11WIPSCtmRecRadioId_Type = Integer32
_Hh3cDot11WIPSCtmRecRadioId_Object = MibTableColumn
hh3cDot11WIPSCtmRecRadioId = _Hh3cDot11WIPSCtmRecRadioId_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 15, 2, 5, 1, 7),
    _Hh3cDot11WIPSCtmRecRadioId_Type()
)
hh3cDot11WIPSCtmRecRadioId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11WIPSCtmRecRadioId.setStatus("current")


class _Hh3cDot11WIPSCtmRecCounterTime_Type(OctetString):
    """Custom type hh3cDot11WIPSCtmRecCounterTime based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 256),
    )


_Hh3cDot11WIPSCtmRecCounterTime_Type.__name__ = "OctetString"
_Hh3cDot11WIPSCtmRecCounterTime_Object = MibTableColumn
hh3cDot11WIPSCtmRecCounterTime = _Hh3cDot11WIPSCtmRecCounterTime_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 15, 2, 5, 1, 8),
    _Hh3cDot11WIPSCtmRecCounterTime_Type()
)
hh3cDot11WIPSCtmRecCounterTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11WIPSCtmRecCounterTime.setStatus("current")
_Hh3cDot11WIPSDevTable_Object = MibTable
hh3cDot11WIPSDevTable = _Hh3cDot11WIPSDevTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 15, 2, 7)
)
if mibBuilder.loadTexts:
    hh3cDot11WIPSDevTable.setStatus("current")
_Hh3cDot11WIPSDevEntry_Object = MibTableRow
hh3cDot11WIPSDevEntry = _Hh3cDot11WIPSDevEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 15, 2, 7, 1)
)
hh3cDot11WIPSDevEntry.setIndexNames(
    (0, "HH3C-DOT11-WIPS-MIB", "hh3cDot11WIPSDevVSDName"),
)
if mibBuilder.loadTexts:
    hh3cDot11WIPSDevEntry.setStatus("current")


class _Hh3cDot11WIPSDevVSDName_Type(OctetString):
    """Custom type hh3cDot11WIPSDevVSDName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 63),
    )


_Hh3cDot11WIPSDevVSDName_Type.__name__ = "OctetString"
_Hh3cDot11WIPSDevVSDName_Object = MibTableColumn
hh3cDot11WIPSDevVSDName = _Hh3cDot11WIPSDevVSDName_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 15, 2, 7, 1, 1),
    _Hh3cDot11WIPSDevVSDName_Type()
)
hh3cDot11WIPSDevVSDName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cDot11WIPSDevVSDName.setStatus("current")
_Hh3cDot11WIPSDevTotalApNum_Type = Integer32
_Hh3cDot11WIPSDevTotalApNum_Object = MibTableColumn
hh3cDot11WIPSDevTotalApNum = _Hh3cDot11WIPSDevTotalApNum_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 15, 2, 7, 1, 2),
    _Hh3cDot11WIPSDevTotalApNum_Type()
)
hh3cDot11WIPSDevTotalApNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11WIPSDevTotalApNum.setStatus("current")
_Hh3cDot11WIPSDevTotalClinetNum_Type = Integer32
_Hh3cDot11WIPSDevTotalClinetNum_Object = MibTableColumn
hh3cDot11WIPSDevTotalClinetNum = _Hh3cDot11WIPSDevTotalClinetNum_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 15, 2, 7, 1, 3),
    _Hh3cDot11WIPSDevTotalClinetNum_Type()
)
hh3cDot11WIPSDevTotalClinetNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11WIPSDevTotalClinetNum.setStatus("current")
_Hh3cDot11WIPSDevAuthApNum_Type = Integer32
_Hh3cDot11WIPSDevAuthApNum_Object = MibTableColumn
hh3cDot11WIPSDevAuthApNum = _Hh3cDot11WIPSDevAuthApNum_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 15, 2, 7, 1, 4),
    _Hh3cDot11WIPSDevAuthApNum_Type()
)
hh3cDot11WIPSDevAuthApNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11WIPSDevAuthApNum.setStatus("current")
_Hh3cDot11WIPSDevMisConfigApNum_Type = Integer32
_Hh3cDot11WIPSDevMisConfigApNum_Object = MibTableColumn
hh3cDot11WIPSDevMisConfigApNum = _Hh3cDot11WIPSDevMisConfigApNum_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 15, 2, 7, 1, 5),
    _Hh3cDot11WIPSDevMisConfigApNum_Type()
)
hh3cDot11WIPSDevMisConfigApNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11WIPSDevMisConfigApNum.setStatus("current")
_Hh3cDot11WIPSDevRogueApNum_Type = Integer32
_Hh3cDot11WIPSDevRogueApNum_Object = MibTableColumn
hh3cDot11WIPSDevRogueApNum = _Hh3cDot11WIPSDevRogueApNum_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 15, 2, 7, 1, 6),
    _Hh3cDot11WIPSDevRogueApNum_Type()
)
hh3cDot11WIPSDevRogueApNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11WIPSDevRogueApNum.setStatus("current")
_Hh3cDot11WIPSDevExternalApNum_Type = Integer32
_Hh3cDot11WIPSDevExternalApNum_Object = MibTableColumn
hh3cDot11WIPSDevExternalApNum = _Hh3cDot11WIPSDevExternalApNum_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 15, 2, 7, 1, 7),
    _Hh3cDot11WIPSDevExternalApNum_Type()
)
hh3cDot11WIPSDevExternalApNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11WIPSDevExternalApNum.setStatus("current")
_Hh3cDot11WIPSDevAdhocNum_Type = Integer32
_Hh3cDot11WIPSDevAdhocNum_Object = MibTableColumn
hh3cDot11WIPSDevAdhocNum = _Hh3cDot11WIPSDevAdhocNum_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 15, 2, 7, 1, 8),
    _Hh3cDot11WIPSDevAdhocNum_Type()
)
hh3cDot11WIPSDevAdhocNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11WIPSDevAdhocNum.setStatus("current")
_Hh3cDot11WIPSDevMeshApNum_Type = Integer32
_Hh3cDot11WIPSDevMeshApNum_Object = MibTableColumn
hh3cDot11WIPSDevMeshApNum = _Hh3cDot11WIPSDevMeshApNum_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 15, 2, 7, 1, 9),
    _Hh3cDot11WIPSDevMeshApNum_Type()
)
hh3cDot11WIPSDevMeshApNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11WIPSDevMeshApNum.setStatus("current")
_Hh3cDot11WIPSDevpotenAuthApNum_Type = Integer32
_Hh3cDot11WIPSDevpotenAuthApNum_Object = MibTableColumn
hh3cDot11WIPSDevpotenAuthApNum = _Hh3cDot11WIPSDevpotenAuthApNum_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 15, 2, 7, 1, 10),
    _Hh3cDot11WIPSDevpotenAuthApNum_Type()
)
hh3cDot11WIPSDevpotenAuthApNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11WIPSDevpotenAuthApNum.setStatus("current")
_Hh3cDot11WIPSDevpotenRogueApNum_Type = Integer32
_Hh3cDot11WIPSDevpotenRogueApNum_Object = MibTableColumn
hh3cDot11WIPSDevpotenRogueApNum = _Hh3cDot11WIPSDevpotenRogueApNum_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 15, 2, 7, 1, 11),
    _Hh3cDot11WIPSDevpotenRogueApNum_Type()
)
hh3cDot11WIPSDevpotenRogueApNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11WIPSDevpotenRogueApNum.setStatus("current")
_Hh3cDot11WIPSDevPotenExtApNum_Type = Integer32
_Hh3cDot11WIPSDevPotenExtApNum_Object = MibTableColumn
hh3cDot11WIPSDevPotenExtApNum = _Hh3cDot11WIPSDevPotenExtApNum_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 15, 2, 7, 1, 12),
    _Hh3cDot11WIPSDevPotenExtApNum_Type()
)
hh3cDot11WIPSDevPotenExtApNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11WIPSDevPotenExtApNum.setStatus("current")
_Hh3cDot11WIPSDevUncateApNum_Type = Integer32
_Hh3cDot11WIPSDevUncateApNum_Object = MibTableColumn
hh3cDot11WIPSDevUncateApNum = _Hh3cDot11WIPSDevUncateApNum_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 15, 2, 7, 1, 13),
    _Hh3cDot11WIPSDevUncateApNum_Type()
)
hh3cDot11WIPSDevUncateApNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11WIPSDevUncateApNum.setStatus("current")
_Hh3cDot11WIPSDevAuthClinetNum_Type = Integer32
_Hh3cDot11WIPSDevAuthClinetNum_Object = MibTableColumn
hh3cDot11WIPSDevAuthClinetNum = _Hh3cDot11WIPSDevAuthClinetNum_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 15, 2, 7, 1, 14),
    _Hh3cDot11WIPSDevAuthClinetNum_Type()
)
hh3cDot11WIPSDevAuthClinetNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11WIPSDevAuthClinetNum.setStatus("current")
_Hh3cDot11WIPSDevUnauthClinetNum_Type = Integer32
_Hh3cDot11WIPSDevUnauthClinetNum_Object = MibTableColumn
hh3cDot11WIPSDevUnauthClinetNum = _Hh3cDot11WIPSDevUnauthClinetNum_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 15, 2, 7, 1, 15),
    _Hh3cDot11WIPSDevUnauthClinetNum_Type()
)
hh3cDot11WIPSDevUnauthClinetNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11WIPSDevUnauthClinetNum.setStatus("current")
_Hh3cDot11WIPSDevMisAssocltNum_Type = Integer32
_Hh3cDot11WIPSDevMisAssocltNum_Object = MibTableColumn
hh3cDot11WIPSDevMisAssocltNum = _Hh3cDot11WIPSDevMisAssocltNum_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 15, 2, 7, 1, 16),
    _Hh3cDot11WIPSDevMisAssocltNum_Type()
)
hh3cDot11WIPSDevMisAssocltNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11WIPSDevMisAssocltNum.setStatus("current")
_Hh3cDot11WIPSDevUncatecltNum_Type = Integer32
_Hh3cDot11WIPSDevUncatecltNum_Object = MibTableColumn
hh3cDot11WIPSDevUncatecltNum = _Hh3cDot11WIPSDevUncatecltNum_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 15, 2, 7, 1, 17),
    _Hh3cDot11WIPSDevUncatecltNum_Type()
)
hh3cDot11WIPSDevUncatecltNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11WIPSDevUncatecltNum.setStatus("current")
_Hh3cDot11WIPSCtmDevTable_Object = MibTable
hh3cDot11WIPSCtmDevTable = _Hh3cDot11WIPSCtmDevTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 15, 2, 8)
)
if mibBuilder.loadTexts:
    hh3cDot11WIPSCtmDevTable.setStatus("current")
_Hh3cDot11WIPSCtmDevEntry_Object = MibTableRow
hh3cDot11WIPSCtmDevEntry = _Hh3cDot11WIPSCtmDevEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 15, 2, 8, 1)
)
hh3cDot11WIPSCtmDevEntry.setIndexNames(
    (0, "HH3C-DOT11-WIPS-MIB", "hh3cDot11WIPSCtmDevVsdName"),
)
if mibBuilder.loadTexts:
    hh3cDot11WIPSCtmDevEntry.setStatus("current")


class _Hh3cDot11WIPSCtmDevVsdName_Type(OctetString):
    """Custom type hh3cDot11WIPSCtmDevVsdName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 63),
    )


_Hh3cDot11WIPSCtmDevVsdName_Type.__name__ = "OctetString"
_Hh3cDot11WIPSCtmDevVsdName_Object = MibTableColumn
hh3cDot11WIPSCtmDevVsdName = _Hh3cDot11WIPSCtmDevVsdName_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 15, 2, 8, 1, 1),
    _Hh3cDot11WIPSCtmDevVsdName_Type()
)
hh3cDot11WIPSCtmDevVsdName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cDot11WIPSCtmDevVsdName.setStatus("current")
_Hh3cDot11WIPSCtmDevTotalApNum_Type = Integer32
_Hh3cDot11WIPSCtmDevTotalApNum_Object = MibTableColumn
hh3cDot11WIPSCtmDevTotalApNum = _Hh3cDot11WIPSCtmDevTotalApNum_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 15, 2, 8, 1, 2),
    _Hh3cDot11WIPSCtmDevTotalApNum_Type()
)
hh3cDot11WIPSCtmDevTotalApNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11WIPSCtmDevTotalApNum.setStatus("current")
_Hh3cDot11WIPSCtmDevTotalStaNum_Type = Integer32
_Hh3cDot11WIPSCtmDevTotalStaNum_Object = MibTableColumn
hh3cDot11WIPSCtmDevTotalStaNum = _Hh3cDot11WIPSCtmDevTotalStaNum_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 15, 2, 8, 1, 3),
    _Hh3cDot11WIPSCtmDevTotalStaNum_Type()
)
hh3cDot11WIPSCtmDevTotalStaNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11WIPSCtmDevTotalStaNum.setStatus("current")
_Hh3cDot11WIPSCtmDevMisCfgApNum_Type = Integer32
_Hh3cDot11WIPSCtmDevMisCfgApNum_Object = MibTableColumn
hh3cDot11WIPSCtmDevMisCfgApNum = _Hh3cDot11WIPSCtmDevMisCfgApNum_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 15, 2, 8, 1, 4),
    _Hh3cDot11WIPSCtmDevMisCfgApNum_Type()
)
hh3cDot11WIPSCtmDevMisCfgApNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11WIPSCtmDevMisCfgApNum.setStatus("current")
_Hh3cDot11WIPSCtmDevRogueApNum_Type = Integer32
_Hh3cDot11WIPSCtmDevRogueApNum_Object = MibTableColumn
hh3cDot11WIPSCtmDevRogueApNum = _Hh3cDot11WIPSCtmDevRogueApNum_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 15, 2, 8, 1, 5),
    _Hh3cDot11WIPSCtmDevRogueApNum_Type()
)
hh3cDot11WIPSCtmDevRogueApNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11WIPSCtmDevRogueApNum.setStatus("current")
_Hh3cDot11WIPSCtmDevExternalApNum_Type = Integer32
_Hh3cDot11WIPSCtmDevExternalApNum_Object = MibTableColumn
hh3cDot11WIPSCtmDevExternalApNum = _Hh3cDot11WIPSCtmDevExternalApNum_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 15, 2, 8, 1, 6),
    _Hh3cDot11WIPSCtmDevExternalApNum_Type()
)
hh3cDot11WIPSCtmDevExternalApNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11WIPSCtmDevExternalApNum.setStatus("current")
_Hh3cDot11WIPSCtmDevpotAuthApNum_Type = Integer32
_Hh3cDot11WIPSCtmDevpotAuthApNum_Object = MibTableColumn
hh3cDot11WIPSCtmDevpotAuthApNum = _Hh3cDot11WIPSCtmDevpotAuthApNum_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 15, 2, 8, 1, 7),
    _Hh3cDot11WIPSCtmDevpotAuthApNum_Type()
)
hh3cDot11WIPSCtmDevpotAuthApNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11WIPSCtmDevpotAuthApNum.setStatus("current")
_Hh3cDot11WIPSCtmDevpotRguApNum_Type = Integer32
_Hh3cDot11WIPSCtmDevpotRguApNum_Object = MibTableColumn
hh3cDot11WIPSCtmDevpotRguApNum = _Hh3cDot11WIPSCtmDevpotRguApNum_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 15, 2, 8, 1, 8),
    _Hh3cDot11WIPSCtmDevpotRguApNum_Type()
)
hh3cDot11WIPSCtmDevpotRguApNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11WIPSCtmDevpotRguApNum.setStatus("current")
_Hh3cDot11WIPSCtmDevpotenExtApNum_Type = Integer32
_Hh3cDot11WIPSCtmDevpotenExtApNum_Object = MibTableColumn
hh3cDot11WIPSCtmDevpotenExtApNum = _Hh3cDot11WIPSCtmDevpotenExtApNum_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 15, 2, 8, 1, 9),
    _Hh3cDot11WIPSCtmDevpotenExtApNum_Type()
)
hh3cDot11WIPSCtmDevpotenExtApNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11WIPSCtmDevpotenExtApNum.setStatus("current")
_Hh3cDot11WIPSCtmDevUncateApNum_Type = Integer32
_Hh3cDot11WIPSCtmDevUncateApNum_Object = MibTableColumn
hh3cDot11WIPSCtmDevUncateApNum = _Hh3cDot11WIPSCtmDevUncateApNum_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 15, 2, 8, 1, 10),
    _Hh3cDot11WIPSCtmDevUncateApNum_Type()
)
hh3cDot11WIPSCtmDevUncateApNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11WIPSCtmDevUncateApNum.setStatus("current")
_Hh3cDot11WIPSCtmDevUnauthStaNum_Type = Integer32
_Hh3cDot11WIPSCtmDevUnauthStaNum_Object = MibTableColumn
hh3cDot11WIPSCtmDevUnauthStaNum = _Hh3cDot11WIPSCtmDevUnauthStaNum_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 15, 2, 8, 1, 11),
    _Hh3cDot11WIPSCtmDevUnauthStaNum_Type()
)
hh3cDot11WIPSCtmDevUnauthStaNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11WIPSCtmDevUnauthStaNum.setStatus("current")
_Hh3cDot11WIPSCtmDevMisAssCltNum_Type = Integer32
_Hh3cDot11WIPSCtmDevMisAssCltNum_Object = MibTableColumn
hh3cDot11WIPSCtmDevMisAssCltNum = _Hh3cDot11WIPSCtmDevMisAssCltNum_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 15, 2, 8, 1, 12),
    _Hh3cDot11WIPSCtmDevMisAssCltNum_Type()
)
hh3cDot11WIPSCtmDevMisAssCltNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11WIPSCtmDevMisAssCltNum.setStatus("current")
_Hh3cDot11WIPSCtmDevUncatecltNum_Type = Integer32
_Hh3cDot11WIPSCtmDevUncatecltNum_Object = MibTableColumn
hh3cDot11WIPSCtmDevUncatecltNum = _Hh3cDot11WIPSCtmDevUncatecltNum_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 15, 2, 8, 1, 13),
    _Hh3cDot11WIPSCtmDevUncatecltNum_Type()
)
hh3cDot11WIPSCtmDevUncatecltNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11WIPSCtmDevUncatecltNum.setStatus("current")
_Hh3cDot11WIPSCtmDevAttackerNum_Type = Integer32
_Hh3cDot11WIPSCtmDevAttackerNum_Object = MibTableColumn
hh3cDot11WIPSCtmDevAttackerNum = _Hh3cDot11WIPSCtmDevAttackerNum_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 15, 2, 8, 1, 14),
    _Hh3cDot11WIPSCtmDevAttackerNum_Type()
)
hh3cDot11WIPSCtmDevAttackerNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11WIPSCtmDevAttackerNum.setStatus("current")
_Hh3cDot11WIPSCtmDevManuNum_Type = Integer32
_Hh3cDot11WIPSCtmDevManuNum_Object = MibTableColumn
hh3cDot11WIPSCtmDevManuNum = _Hh3cDot11WIPSCtmDevManuNum_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 15, 2, 8, 1, 15),
    _Hh3cDot11WIPSCtmDevManuNum_Type()
)
hh3cDot11WIPSCtmDevManuNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11WIPSCtmDevManuNum.setStatus("current")
_Hh3cDot11WIPSCtmDevStaCauseByAP_Type = Integer32
_Hh3cDot11WIPSCtmDevStaCauseByAP_Object = MibTableColumn
hh3cDot11WIPSCtmDevStaCauseByAP = _Hh3cDot11WIPSCtmDevStaCauseByAP_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 15, 2, 8, 1, 16),
    _Hh3cDot11WIPSCtmDevStaCauseByAP_Type()
)
hh3cDot11WIPSCtmDevStaCauseByAP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11WIPSCtmDevStaCauseByAP.setStatus("current")
_Hh3cDot11WIPSCltRptApTable_Object = MibTable
hh3cDot11WIPSCltRptApTable = _Hh3cDot11WIPSCltRptApTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 15, 2, 11)
)
if mibBuilder.loadTexts:
    hh3cDot11WIPSCltRptApTable.setStatus("current")
_Hh3cDot11WIPSCltRptApEntry_Object = MibTableRow
hh3cDot11WIPSCltRptApEntry = _Hh3cDot11WIPSCltRptApEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 15, 2, 11, 1)
)
hh3cDot11WIPSCltRptApEntry.setIndexNames(
    (0, "HH3C-DOT11-WIPS-MIB", "hh3cDot11WIPSCltRptApVSDName"),
    (0, "HH3C-DOT11-WIPS-MIB", "hh3cDot11WIPSCltRptApDevMac"),
    (0, "HH3C-DOT11-WIPS-MIB", "hh3cDot11WIPSCltRptApSensorName"),
)
if mibBuilder.loadTexts:
    hh3cDot11WIPSCltRptApEntry.setStatus("current")


class _Hh3cDot11WIPSCltRptApVSDName_Type(OctetString):
    """Custom type hh3cDot11WIPSCltRptApVSDName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 63),
    )


_Hh3cDot11WIPSCltRptApVSDName_Type.__name__ = "OctetString"
_Hh3cDot11WIPSCltRptApVSDName_Object = MibTableColumn
hh3cDot11WIPSCltRptApVSDName = _Hh3cDot11WIPSCltRptApVSDName_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 15, 2, 11, 1, 1),
    _Hh3cDot11WIPSCltRptApVSDName_Type()
)
hh3cDot11WIPSCltRptApVSDName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cDot11WIPSCltRptApVSDName.setStatus("current")
_Hh3cDot11WIPSCltRptApDevMac_Type = MacAddress
_Hh3cDot11WIPSCltRptApDevMac_Object = MibTableColumn
hh3cDot11WIPSCltRptApDevMac = _Hh3cDot11WIPSCltRptApDevMac_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 15, 2, 11, 1, 2),
    _Hh3cDot11WIPSCltRptApDevMac_Type()
)
hh3cDot11WIPSCltRptApDevMac.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cDot11WIPSCltRptApDevMac.setStatus("current")


class _Hh3cDot11WIPSCltRptApSensorName_Type(OctetString):
    """Custom type hh3cDot11WIPSCltRptApSensorName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_Hh3cDot11WIPSCltRptApSensorName_Type.__name__ = "OctetString"
_Hh3cDot11WIPSCltRptApSensorName_Object = MibTableColumn
hh3cDot11WIPSCltRptApSensorName = _Hh3cDot11WIPSCltRptApSensorName_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 15, 2, 11, 1, 3),
    _Hh3cDot11WIPSCltRptApSensorName_Type()
)
hh3cDot11WIPSCltRptApSensorName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cDot11WIPSCltRptApSensorName.setStatus("current")
_Hh3cDot11WIPSCltReportApRadioId_Type = Integer32
_Hh3cDot11WIPSCltReportApRadioId_Object = MibTableColumn
hh3cDot11WIPSCltReportApRadioId = _Hh3cDot11WIPSCltReportApRadioId_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 15, 2, 11, 1, 4),
    _Hh3cDot11WIPSCltReportApRadioId_Type()
)
hh3cDot11WIPSCltReportApRadioId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11WIPSCltReportApRadioId.setStatus("current")
_Hh3cDot11WIPSCltRptApRSSI_Type = Integer32
_Hh3cDot11WIPSCltRptApRSSI_Object = MibTableColumn
hh3cDot11WIPSCltRptApRSSI = _Hh3cDot11WIPSCltRptApRSSI_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 15, 2, 11, 1, 5),
    _Hh3cDot11WIPSCltRptApRSSI_Type()
)
hh3cDot11WIPSCltRptApRSSI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11WIPSCltRptApRSSI.setStatus("current")
_Hh3cDot11WIPSCltRptApWorkChannel_Type = Hh3cDot11WIPSChannel
_Hh3cDot11WIPSCltRptApWorkChannel_Object = MibTableColumn
hh3cDot11WIPSCltRptApWorkChannel = _Hh3cDot11WIPSCltRptApWorkChannel_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 15, 2, 11, 1, 6),
    _Hh3cDot11WIPSCltRptApWorkChannel_Type()
)
hh3cDot11WIPSCltRptApWorkChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11WIPSCltRptApWorkChannel.setStatus("current")


class _Hh3cDot11WIPSCltRptApFirstTime_Type(OctetString):
    """Custom type hh3cDot11WIPSCltRptApFirstTime based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 256),
    )


_Hh3cDot11WIPSCltRptApFirstTime_Type.__name__ = "OctetString"
_Hh3cDot11WIPSCltRptApFirstTime_Object = MibTableColumn
hh3cDot11WIPSCltRptApFirstTime = _Hh3cDot11WIPSCltRptApFirstTime_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 15, 2, 11, 1, 7),
    _Hh3cDot11WIPSCltRptApFirstTime_Type()
)
hh3cDot11WIPSCltRptApFirstTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11WIPSCltRptApFirstTime.setStatus("current")


class _Hh3cDot11WIPSCltRptApLastTime_Type(OctetString):
    """Custom type hh3cDot11WIPSCltRptApLastTime based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 256),
    )


_Hh3cDot11WIPSCltRptApLastTime_Type.__name__ = "OctetString"
_Hh3cDot11WIPSCltRptApLastTime_Object = MibTableColumn
hh3cDot11WIPSCltRptApLastTime = _Hh3cDot11WIPSCltRptApLastTime_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 15, 2, 11, 1, 8),
    _Hh3cDot11WIPSCltRptApLastTime_Type()
)
hh3cDot11WIPSCltRptApLastTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11WIPSCltRptApLastTime.setStatus("current")
_Hh3cDot11WIPSCltRptApAssocMac_Type = MacAddress
_Hh3cDot11WIPSCltRptApAssocMac_Object = MibTableColumn
hh3cDot11WIPSCltRptApAssocMac = _Hh3cDot11WIPSCltRptApAssocMac_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 15, 2, 11, 1, 9),
    _Hh3cDot11WIPSCltRptApAssocMac_Type()
)
hh3cDot11WIPSCltRptApAssocMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11WIPSCltRptApAssocMac.setStatus("current")
_Hh3cDot11WIPSNatDtcCltTable_Object = MibTable
hh3cDot11WIPSNatDtcCltTable = _Hh3cDot11WIPSNatDtcCltTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 15, 2, 12)
)
if mibBuilder.loadTexts:
    hh3cDot11WIPSNatDtcCltTable.setStatus("current")
_Hh3cDot11WIPSNatDtcCltEntry_Object = MibTableRow
hh3cDot11WIPSNatDtcCltEntry = _Hh3cDot11WIPSNatDtcCltEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 15, 2, 12, 1)
)
hh3cDot11WIPSNatDtcCltEntry.setIndexNames(
    (0, "HH3C-DOT11-WIPS-MIB", "hh3cDot11WIPSNatDtcCltMac"),
)
if mibBuilder.loadTexts:
    hh3cDot11WIPSNatDtcCltEntry.setStatus("current")
_Hh3cDot11WIPSNatDtcCltMac_Type = MacAddress
_Hh3cDot11WIPSNatDtcCltMac_Object = MibTableColumn
hh3cDot11WIPSNatDtcCltMac = _Hh3cDot11WIPSNatDtcCltMac_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 15, 2, 12, 1, 1),
    _Hh3cDot11WIPSNatDtcCltMac_Type()
)
hh3cDot11WIPSNatDtcCltMac.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cDot11WIPSNatDtcCltMac.setStatus("current")


class _Hh3cDot11WIPSNatDtcCltFirstTime_Type(OctetString):
    """Custom type hh3cDot11WIPSNatDtcCltFirstTime based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 256),
    )


_Hh3cDot11WIPSNatDtcCltFirstTime_Type.__name__ = "OctetString"
_Hh3cDot11WIPSNatDtcCltFirstTime_Object = MibTableColumn
hh3cDot11WIPSNatDtcCltFirstTime = _Hh3cDot11WIPSNatDtcCltFirstTime_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 15, 2, 12, 1, 2),
    _Hh3cDot11WIPSNatDtcCltFirstTime_Type()
)
hh3cDot11WIPSNatDtcCltFirstTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11WIPSNatDtcCltFirstTime.setStatus("current")


class _Hh3cDot11WIPSNatDtcCltLastTime_Type(OctetString):
    """Custom type hh3cDot11WIPSNatDtcCltLastTime based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 256),
    )


_Hh3cDot11WIPSNatDtcCltLastTime_Type.__name__ = "OctetString"
_Hh3cDot11WIPSNatDtcCltLastTime_Object = MibTableColumn
hh3cDot11WIPSNatDtcCltLastTime = _Hh3cDot11WIPSNatDtcCltLastTime_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 15, 2, 12, 1, 3),
    _Hh3cDot11WIPSNatDtcCltLastTime_Type()
)
hh3cDot11WIPSNatDtcCltLastTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11WIPSNatDtcCltLastTime.setStatus("current")
_Hh3cDot11WIPSNatDtcCltDuraTime_Type = Integer32
_Hh3cDot11WIPSNatDtcCltDuraTime_Object = MibTableColumn
hh3cDot11WIPSNatDtcCltDuraTime = _Hh3cDot11WIPSNatDtcCltDuraTime_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 15, 2, 12, 1, 4),
    _Hh3cDot11WIPSNatDtcCltDuraTime_Type()
)
hh3cDot11WIPSNatDtcCltDuraTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11WIPSNatDtcCltDuraTime.setStatus("current")
_Hh3cDot11WIPSAckStaTable_Object = MibTable
hh3cDot11WIPSAckStaTable = _Hh3cDot11WIPSAckStaTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 15, 2, 13)
)
if mibBuilder.loadTexts:
    hh3cDot11WIPSAckStaTable.setStatus("current")
_Hh3cDot11WIPSAckStaEntry_Object = MibTableRow
hh3cDot11WIPSAckStaEntry = _Hh3cDot11WIPSAckStaEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 15, 2, 13, 1)
)
hh3cDot11WIPSAckStaEntry.setIndexNames(
    (0, "HH3C-DOT11-WIPS-MIB", "hh3cDot11WIPSAckStaSensorName"),
)
if mibBuilder.loadTexts:
    hh3cDot11WIPSAckStaEntry.setStatus("current")


class _Hh3cDot11WIPSAckStaSensorName_Type(OctetString):
    """Custom type hh3cDot11WIPSAckStaSensorName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_Hh3cDot11WIPSAckStaSensorName_Type.__name__ = "OctetString"
_Hh3cDot11WIPSAckStaSensorName_Object = MibTableColumn
hh3cDot11WIPSAckStaSensorName = _Hh3cDot11WIPSAckStaSensorName_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 15, 2, 13, 1, 1),
    _Hh3cDot11WIPSAckStaSensorName_Type()
)
hh3cDot11WIPSAckStaSensorName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cDot11WIPSAckStaSensorName.setStatus("current")
_Hh3cDot11WIPSAckStaAssReqFld_Type = Integer32
_Hh3cDot11WIPSAckStaAssReqFld_Object = MibTableColumn
hh3cDot11WIPSAckStaAssReqFld = _Hh3cDot11WIPSAckStaAssReqFld_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 15, 2, 13, 1, 2),
    _Hh3cDot11WIPSAckStaAssReqFld_Type()
)
hh3cDot11WIPSAckStaAssReqFld.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11WIPSAckStaAssReqFld.setStatus("current")
_Hh3cDot11WIPSAckStaAuthFld_Type = Integer32
_Hh3cDot11WIPSAckStaAuthFld_Object = MibTableColumn
hh3cDot11WIPSAckStaAuthFld = _Hh3cDot11WIPSAckStaAuthFld_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 15, 2, 13, 1, 3),
    _Hh3cDot11WIPSAckStaAuthFld_Type()
)
hh3cDot11WIPSAckStaAuthFld.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11WIPSAckStaAuthFld.setStatus("current")
_Hh3cDot11WIPSAckStaBeaconFld_Type = Integer32
_Hh3cDot11WIPSAckStaBeaconFld_Object = MibTableColumn
hh3cDot11WIPSAckStaBeaconFld = _Hh3cDot11WIPSAckStaBeaconFld_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 15, 2, 13, 1, 4),
    _Hh3cDot11WIPSAckStaBeaconFld_Type()
)
hh3cDot11WIPSAckStaBeaconFld.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11WIPSAckStaBeaconFld.setStatus("current")
_Hh3cDot11WIPSAckStaBlkAckFld_Type = Integer32
_Hh3cDot11WIPSAckStaBlkAckFld_Object = MibTableColumn
hh3cDot11WIPSAckStaBlkAckFld = _Hh3cDot11WIPSAckStaBlkAckFld_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 15, 2, 13, 1, 5),
    _Hh3cDot11WIPSAckStaBlkAckFld_Type()
)
hh3cDot11WIPSAckStaBlkAckFld.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11WIPSAckStaBlkAckFld.setStatus("current")
_Hh3cDot11WIPSAckStaCtsFld_Type = Integer32
_Hh3cDot11WIPSAckStaCtsFld_Object = MibTableColumn
hh3cDot11WIPSAckStaCtsFld = _Hh3cDot11WIPSAckStaCtsFld_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 15, 2, 13, 1, 6),
    _Hh3cDot11WIPSAckStaCtsFld_Type()
)
hh3cDot11WIPSAckStaCtsFld.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11WIPSAckStaCtsFld.setStatus("current")
_Hh3cDot11WIPSAckStaDeauthFld_Type = Integer32
_Hh3cDot11WIPSAckStaDeauthFld_Object = MibTableColumn
hh3cDot11WIPSAckStaDeauthFld = _Hh3cDot11WIPSAckStaDeauthFld_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 15, 2, 13, 1, 7),
    _Hh3cDot11WIPSAckStaDeauthFld_Type()
)
hh3cDot11WIPSAckStaDeauthFld.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11WIPSAckStaDeauthFld.setStatus("current")
_Hh3cDot11WIPSAckStaDisassFld_Type = Integer32
_Hh3cDot11WIPSAckStaDisassFld_Object = MibTableColumn
hh3cDot11WIPSAckStaDisassFld = _Hh3cDot11WIPSAckStaDisassFld_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 15, 2, 13, 1, 8),
    _Hh3cDot11WIPSAckStaDisassFld_Type()
)
hh3cDot11WIPSAckStaDisassFld.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11WIPSAckStaDisassFld.setStatus("current")
_Hh3cDot11WIPSAckStaEpolSatFld_Type = Integer32
_Hh3cDot11WIPSAckStaEpolSatFld_Object = MibTableColumn
hh3cDot11WIPSAckStaEpolSatFld = _Hh3cDot11WIPSAckStaEpolSatFld_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 15, 2, 13, 1, 9),
    _Hh3cDot11WIPSAckStaEpolSatFld_Type()
)
hh3cDot11WIPSAckStaEpolSatFld.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11WIPSAckStaEpolSatFld.setStatus("current")
_Hh3cDot11WIPSAckStaNullDataFld_Type = Integer32
_Hh3cDot11WIPSAckStaNullDataFld_Object = MibTableColumn
hh3cDot11WIPSAckStaNullDataFld = _Hh3cDot11WIPSAckStaNullDataFld_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 15, 2, 13, 1, 10),
    _Hh3cDot11WIPSAckStaNullDataFld_Type()
)
hh3cDot11WIPSAckStaNullDataFld.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11WIPSAckStaNullDataFld.setStatus("current")
_Hh3cDot11WIPSAckStaProReqFld_Type = Integer32
_Hh3cDot11WIPSAckStaProReqFld_Object = MibTableColumn
hh3cDot11WIPSAckStaProReqFld = _Hh3cDot11WIPSAckStaProReqFld_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 15, 2, 13, 1, 11),
    _Hh3cDot11WIPSAckStaProReqFld_Type()
)
hh3cDot11WIPSAckStaProReqFld.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11WIPSAckStaProReqFld.setStatus("current")
_Hh3cDot11WIPSAckStaReassFld_Type = Integer32
_Hh3cDot11WIPSAckStaReassFld_Object = MibTableColumn
hh3cDot11WIPSAckStaReassFld = _Hh3cDot11WIPSAckStaReassFld_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 15, 2, 13, 1, 12),
    _Hh3cDot11WIPSAckStaReassFld_Type()
)
hh3cDot11WIPSAckStaReassFld.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11WIPSAckStaReassFld.setStatus("current")
_Hh3cDot11WIPSAckStaRtsFld_Type = Integer32
_Hh3cDot11WIPSAckStaRtsFld_Object = MibTableColumn
hh3cDot11WIPSAckStaRtsFld = _Hh3cDot11WIPSAckStaRtsFld_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 15, 2, 13, 1, 13),
    _Hh3cDot11WIPSAckStaRtsFld_Type()
)
hh3cDot11WIPSAckStaRtsFld.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11WIPSAckStaRtsFld.setStatus("current")
_Hh3cDot11WIPSAckStaEapLgoffFld_Type = Integer32
_Hh3cDot11WIPSAckStaEapLgoffFld_Object = MibTableColumn
hh3cDot11WIPSAckStaEapLgoffFld = _Hh3cDot11WIPSAckStaEapLgoffFld_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 15, 2, 13, 1, 14),
    _Hh3cDot11WIPSAckStaEapLgoffFld_Type()
)
hh3cDot11WIPSAckStaEapLgoffFld.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11WIPSAckStaEapLgoffFld.setStatus("current")
_Hh3cDot11WIPSAckStaEapFailFld_Type = Integer32
_Hh3cDot11WIPSAckStaEapFailFld_Object = MibTableColumn
hh3cDot11WIPSAckStaEapFailFld = _Hh3cDot11WIPSAckStaEapFailFld_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 15, 2, 13, 1, 15),
    _Hh3cDot11WIPSAckStaEapFailFld_Type()
)
hh3cDot11WIPSAckStaEapFailFld.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11WIPSAckStaEapFailFld.setStatus("current")
_Hh3cDot11WIPSAckStaEapSucFld_Type = Integer32
_Hh3cDot11WIPSAckStaEapSucFld_Object = MibTableColumn
hh3cDot11WIPSAckStaEapSucFld = _Hh3cDot11WIPSAckStaEapSucFld_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 15, 2, 13, 1, 16),
    _Hh3cDot11WIPSAckStaEapSucFld_Type()
)
hh3cDot11WIPSAckStaEapSucFld.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11WIPSAckStaEapSucFld.setStatus("current")
_Hh3cDot11WIPSAckStaDupIeMalf_Type = Integer32
_Hh3cDot11WIPSAckStaDupIeMalf_Object = MibTableColumn
hh3cDot11WIPSAckStaDupIeMalf = _Hh3cDot11WIPSAckStaDupIeMalf_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 15, 2, 13, 1, 17),
    _Hh3cDot11WIPSAckStaDupIeMalf_Type()
)
hh3cDot11WIPSAckStaDupIeMalf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11WIPSAckStaDupIeMalf.setStatus("current")
_Hh3cDot11WIPSAckStaFataJackMalf_Type = Integer32
_Hh3cDot11WIPSAckStaFataJackMalf_Object = MibTableColumn
hh3cDot11WIPSAckStaFataJackMalf = _Hh3cDot11WIPSAckStaFataJackMalf_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 15, 2, 13, 1, 18),
    _Hh3cDot11WIPSAckStaFataJackMalf_Type()
)
hh3cDot11WIPSAckStaFataJackMalf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11WIPSAckStaFataJackMalf.setStatus("current")
_Hh3cDot11WIPSAckStaEssMalf_Type = Integer32
_Hh3cDot11WIPSAckStaEssMalf_Object = MibTableColumn
hh3cDot11WIPSAckStaEssMalf = _Hh3cDot11WIPSAckStaEssMalf_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 15, 2, 13, 1, 19),
    _Hh3cDot11WIPSAckStaEssMalf_Type()
)
hh3cDot11WIPSAckStaEssMalf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11WIPSAckStaEssMalf.setStatus("current")
_Hh3cDot11WIPSAckStaInvComMalf_Type = Integer32
_Hh3cDot11WIPSAckStaInvComMalf_Object = MibTableColumn
hh3cDot11WIPSAckStaInvComMalf = _Hh3cDot11WIPSAckStaInvComMalf_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 15, 2, 13, 1, 20),
    _Hh3cDot11WIPSAckStaInvComMalf_Type()
)
hh3cDot11WIPSAckStaInvComMalf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11WIPSAckStaInvComMalf.setStatus("current")
_Hh3cDot11WIPSAckStaInvAssReqMalf_Type = Integer32
_Hh3cDot11WIPSAckStaInvAssReqMalf_Object = MibTableColumn
hh3cDot11WIPSAckStaInvAssReqMalf = _Hh3cDot11WIPSAckStaInvAssReqMalf_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 15, 2, 13, 1, 21),
    _Hh3cDot11WIPSAckStaInvAssReqMalf_Type()
)
hh3cDot11WIPSAckStaInvAssReqMalf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11WIPSAckStaInvAssReqMalf.setStatus("current")
_Hh3cDot11WIPSAckStaInvAuthMalf_Type = Integer32
_Hh3cDot11WIPSAckStaInvAuthMalf_Object = MibTableColumn
hh3cDot11WIPSAckStaInvAuthMalf = _Hh3cDot11WIPSAckStaInvAuthMalf_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 15, 2, 13, 1, 22),
    _Hh3cDot11WIPSAckStaInvAuthMalf_Type()
)
hh3cDot11WIPSAckStaInvAuthMalf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11WIPSAckStaInvAuthMalf.setStatus("current")
_Hh3cDot11WIPSAckStaInvDeauthMalf_Type = Integer32
_Hh3cDot11WIPSAckStaInvDeauthMalf_Object = MibTableColumn
hh3cDot11WIPSAckStaInvDeauthMalf = _Hh3cDot11WIPSAckStaInvDeauthMalf_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 15, 2, 13, 1, 23),
    _Hh3cDot11WIPSAckStaInvDeauthMalf_Type()
)
hh3cDot11WIPSAckStaInvDeauthMalf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11WIPSAckStaInvDeauthMalf.setStatus("current")
_Hh3cDot11WIPSAckStaInvDisMalf_Type = Integer32
_Hh3cDot11WIPSAckStaInvDisMalf_Object = MibTableColumn
hh3cDot11WIPSAckStaInvDisMalf = _Hh3cDot11WIPSAckStaInvDisMalf_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 15, 2, 13, 1, 24),
    _Hh3cDot11WIPSAckStaInvDisMalf_Type()
)
hh3cDot11WIPSAckStaInvDisMalf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11WIPSAckStaInvDisMalf.setStatus("current")
_Hh3cDot11WIPSAckStaInvHtIeMalf_Type = Integer32
_Hh3cDot11WIPSAckStaInvHtIeMalf_Object = MibTableColumn
hh3cDot11WIPSAckStaInvHtIeMalf = _Hh3cDot11WIPSAckStaInvHtIeMalf_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 15, 2, 13, 1, 25),
    _Hh3cDot11WIPSAckStaInvHtIeMalf_Type()
)
hh3cDot11WIPSAckStaInvHtIeMalf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11WIPSAckStaInvHtIeMalf.setStatus("current")
_Hh3cDot11WIPSAckStaInvIeLenMalf_Type = Integer32
_Hh3cDot11WIPSAckStaInvIeLenMalf_Object = MibTableColumn
hh3cDot11WIPSAckStaInvIeLenMalf = _Hh3cDot11WIPSAckStaInvIeLenMalf_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 15, 2, 13, 1, 26),
    _Hh3cDot11WIPSAckStaInvIeLenMalf_Type()
)
hh3cDot11WIPSAckStaInvIeLenMalf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11WIPSAckStaInvIeLenMalf.setStatus("current")
_Hh3cDot11WIPSAckStaInvPktLthMalf_Type = Integer32
_Hh3cDot11WIPSAckStaInvPktLthMalf_Object = MibTableColumn
hh3cDot11WIPSAckStaInvPktLthMalf = _Hh3cDot11WIPSAckStaInvPktLthMalf_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 15, 2, 13, 1, 27),
    _Hh3cDot11WIPSAckStaInvPktLthMalf_Type()
)
hh3cDot11WIPSAckStaInvPktLthMalf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11WIPSAckStaInvPktLthMalf.setStatus("current")
_Hh3cDot11WIPSAckStaLgeDutMalf_Type = Integer32
_Hh3cDot11WIPSAckStaLgeDutMalf_Object = MibTableColumn
hh3cDot11WIPSAckStaLgeDutMalf = _Hh3cDot11WIPSAckStaLgeDutMalf_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 15, 2, 13, 1, 28),
    _Hh3cDot11WIPSAckStaLgeDutMalf_Type()
)
hh3cDot11WIPSAckStaLgeDutMalf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11WIPSAckStaLgeDutMalf.setStatus("current")
_Hh3cDot11WIPSAckStaNProRespMalf_Type = Integer32
_Hh3cDot11WIPSAckStaNProRespMalf_Object = MibTableColumn
hh3cDot11WIPSAckStaNProRespMalf = _Hh3cDot11WIPSAckStaNProRespMalf_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 15, 2, 13, 1, 29),
    _Hh3cDot11WIPSAckStaNProRespMalf_Type()
)
hh3cDot11WIPSAckStaNProRespMalf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11WIPSAckStaNProRespMalf.setStatus("current")
_Hh3cDot11WIPSAckStaOverflEapMalf_Type = Integer32
_Hh3cDot11WIPSAckStaOverflEapMalf_Object = MibTableColumn
hh3cDot11WIPSAckStaOverflEapMalf = _Hh3cDot11WIPSAckStaOverflEapMalf_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 15, 2, 13, 1, 30),
    _Hh3cDot11WIPSAckStaOverflEapMalf_Type()
)
hh3cDot11WIPSAckStaOverflEapMalf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11WIPSAckStaOverflEapMalf.setStatus("current")
_Hh3cDot11WIPSAckStaOverfSsidMalf_Type = Integer32
_Hh3cDot11WIPSAckStaOverfSsidMalf_Object = MibTableColumn
hh3cDot11WIPSAckStaOverfSsidMalf = _Hh3cDot11WIPSAckStaOverfSsidMalf_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 15, 2, 13, 1, 31),
    _Hh3cDot11WIPSAckStaOverfSsidMalf_Type()
)
hh3cDot11WIPSAckStaOverfSsidMalf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11WIPSAckStaOverfSsidMalf.setStatus("current")
_Hh3cDot11WIPSAckStaRedundIeMalf_Type = Integer32
_Hh3cDot11WIPSAckStaRedundIeMalf_Object = MibTableColumn
hh3cDot11WIPSAckStaRedundIeMalf = _Hh3cDot11WIPSAckStaRedundIeMalf_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 15, 2, 13, 1, 32),
    _Hh3cDot11WIPSAckStaRedundIeMalf_Type()
)
hh3cDot11WIPSAckStaRedundIeMalf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11WIPSAckStaRedundIeMalf.setStatus("current")
_Hh3cDot11WIPSAckStaApSpoofAp_Type = Integer32
_Hh3cDot11WIPSAckStaApSpoofAp_Object = MibTableColumn
hh3cDot11WIPSAckStaApSpoofAp = _Hh3cDot11WIPSAckStaApSpoofAp_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 15, 2, 13, 1, 33),
    _Hh3cDot11WIPSAckStaApSpoofAp_Type()
)
hh3cDot11WIPSAckStaApSpoofAp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11WIPSAckStaApSpoofAp.setStatus("current")
_Hh3cDot11WIPSAckStaApSpoofclt_Type = Integer32
_Hh3cDot11WIPSAckStaApSpoofclt_Object = MibTableColumn
hh3cDot11WIPSAckStaApSpoofclt = _Hh3cDot11WIPSAckStaApSpoofclt_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 15, 2, 13, 1, 34),
    _Hh3cDot11WIPSAckStaApSpoofclt_Type()
)
hh3cDot11WIPSAckStaApSpoofclt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11WIPSAckStaApSpoofclt.setStatus("current")
_Hh3cDot11WIPSAckStaApSpoofAdhoc_Type = Integer32
_Hh3cDot11WIPSAckStaApSpoofAdhoc_Object = MibTableColumn
hh3cDot11WIPSAckStaApSpoofAdhoc = _Hh3cDot11WIPSAckStaApSpoofAdhoc_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 15, 2, 13, 1, 35),
    _Hh3cDot11WIPSAckStaApSpoofAdhoc_Type()
)
hh3cDot11WIPSAckStaApSpoofAdhoc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11WIPSAckStaApSpoofAdhoc.setStatus("current")
_Hh3cDot11WIPSAckStaAdhocSpoofAp_Type = Integer32
_Hh3cDot11WIPSAckStaAdhocSpoofAp_Object = MibTableColumn
hh3cDot11WIPSAckStaAdhocSpoofAp = _Hh3cDot11WIPSAckStaAdhocSpoofAp_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 15, 2, 13, 1, 36),
    _Hh3cDot11WIPSAckStaAdhocSpoofAp_Type()
)
hh3cDot11WIPSAckStaAdhocSpoofAp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11WIPSAckStaAdhocSpoofAp.setStatus("current")
_Hh3cDot11WIPSAckStacltSpoofAp_Type = Integer32
_Hh3cDot11WIPSAckStacltSpoofAp_Object = MibTableColumn
hh3cDot11WIPSAckStacltSpoofAp = _Hh3cDot11WIPSAckStacltSpoofAp_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 15, 2, 13, 1, 37),
    _Hh3cDot11WIPSAckStacltSpoofAp_Type()
)
hh3cDot11WIPSAckStacltSpoofAp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11WIPSAckStacltSpoofAp.setStatus("current")
_Hh3cDot11WIPSAckStaWeakIv_Type = Integer32
_Hh3cDot11WIPSAckStaWeakIv_Object = MibTableColumn
hh3cDot11WIPSAckStaWeakIv = _Hh3cDot11WIPSAckStaWeakIv_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 15, 2, 13, 1, 38),
    _Hh3cDot11WIPSAckStaWeakIv_Type()
)
hh3cDot11WIPSAckStaWeakIv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11WIPSAckStaWeakIv.setStatus("current")
_Hh3cDot11WIPSAckStaApRate_Type = Integer32
_Hh3cDot11WIPSAckStaApRate_Object = MibTableColumn
hh3cDot11WIPSAckStaApRate = _Hh3cDot11WIPSAckStaApRate_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 15, 2, 13, 1, 39),
    _Hh3cDot11WIPSAckStaApRate_Type()
)
hh3cDot11WIPSAckStaApRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11WIPSAckStaApRate.setStatus("current")
_Hh3cDot11WIPSAckStacltRate_Type = Integer32
_Hh3cDot11WIPSAckStacltRate_Object = MibTableColumn
hh3cDot11WIPSAckStacltRate = _Hh3cDot11WIPSAckStacltRate_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 15, 2, 13, 1, 40),
    _Hh3cDot11WIPSAckStacltRate_Type()
)
hh3cDot11WIPSAckStacltRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11WIPSAckStacltRate.setStatus("current")
_Hh3cDot11WIPSAckStaSignatureRule_Type = Integer32
_Hh3cDot11WIPSAckStaSignatureRule_Object = MibTableColumn
hh3cDot11WIPSAckStaSignatureRule = _Hh3cDot11WIPSAckStaSignatureRule_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 15, 2, 13, 1, 41),
    _Hh3cDot11WIPSAckStaSignatureRule_Type()
)
hh3cDot11WIPSAckStaSignatureRule.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11WIPSAckStaSignatureRule.setStatus("current")
_Hh3cDot11WIPSAckSta40Mhz_Type = Integer32
_Hh3cDot11WIPSAckSta40Mhz_Object = MibTableColumn
hh3cDot11WIPSAckSta40Mhz = _Hh3cDot11WIPSAckSta40Mhz_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 15, 2, 13, 1, 42),
    _Hh3cDot11WIPSAckSta40Mhz_Type()
)
hh3cDot11WIPSAckSta40Mhz.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11WIPSAckSta40Mhz.setStatus("current")
_Hh3cDot11WIPSAckStaPowerSave_Type = Integer32
_Hh3cDot11WIPSAckStaPowerSave_Object = MibTableColumn
hh3cDot11WIPSAckStaPowerSave = _Hh3cDot11WIPSAckStaPowerSave_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 15, 2, 13, 1, 43),
    _Hh3cDot11WIPSAckStaPowerSave_Type()
)
hh3cDot11WIPSAckStaPowerSave.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11WIPSAckStaPowerSave.setStatus("current")
_Hh3cDot11WIPSAckStaWinBdg_Type = Integer32
_Hh3cDot11WIPSAckStaWinBdg_Object = MibTableColumn
hh3cDot11WIPSAckStaWinBdg = _Hh3cDot11WIPSAckStaWinBdg_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 15, 2, 13, 1, 44),
    _Hh3cDot11WIPSAckStaWinBdg_Type()
)
hh3cDot11WIPSAckStaWinBdg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11WIPSAckStaWinBdg.setStatus("current")
_Hh3cDot11WIPSAckStaOmerta_Type = Integer32
_Hh3cDot11WIPSAckStaOmerta_Object = MibTableColumn
hh3cDot11WIPSAckStaOmerta = _Hh3cDot11WIPSAckStaOmerta_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 15, 2, 13, 1, 45),
    _Hh3cDot11WIPSAckStaOmerta_Type()
)
hh3cDot11WIPSAckStaOmerta.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11WIPSAckStaOmerta.setStatus("current")
_Hh3cDot11WIPSAckStaSoftAp_Type = Integer32
_Hh3cDot11WIPSAckStaSoftAp_Object = MibTableColumn
hh3cDot11WIPSAckStaSoftAp = _Hh3cDot11WIPSAckStaSoftAp_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 15, 2, 13, 1, 46),
    _Hh3cDot11WIPSAckStaSoftAp_Type()
)
hh3cDot11WIPSAckStaSoftAp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11WIPSAckStaSoftAp.setStatus("current")
_Hh3cDot11WIPSAckStaBroadDis_Type = Integer32
_Hh3cDot11WIPSAckStaBroadDis_Object = MibTableColumn
hh3cDot11WIPSAckStaBroadDis = _Hh3cDot11WIPSAckStaBroadDis_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 15, 2, 13, 1, 47),
    _Hh3cDot11WIPSAckStaBroadDis_Type()
)
hh3cDot11WIPSAckStaBroadDis.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11WIPSAckStaBroadDis.setStatus("current")
_Hh3cDot11WIPSAckStaBroadDeauth_Type = Integer32
_Hh3cDot11WIPSAckStaBroadDeauth_Object = MibTableColumn
hh3cDot11WIPSAckStaBroadDeauth = _Hh3cDot11WIPSAckStaBroadDeauth_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 15, 2, 13, 1, 48),
    _Hh3cDot11WIPSAckStaBroadDeauth_Type()
)
hh3cDot11WIPSAckStaBroadDeauth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11WIPSAckStaBroadDeauth.setStatus("current")
_Hh3cDot11WIPSAckStaApImp_Type = Integer32
_Hh3cDot11WIPSAckStaApImp_Object = MibTableColumn
hh3cDot11WIPSAckStaApImp = _Hh3cDot11WIPSAckStaApImp_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 15, 2, 13, 1, 49),
    _Hh3cDot11WIPSAckStaApImp_Type()
)
hh3cDot11WIPSAckStaApImp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11WIPSAckStaApImp.setStatus("current")
_Hh3cDot11WIPSAckStaHtGreenField_Type = Integer32
_Hh3cDot11WIPSAckStaHtGreenField_Object = MibTableColumn
hh3cDot11WIPSAckStaHtGreenField = _Hh3cDot11WIPSAckStaHtGreenField_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 15, 2, 13, 1, 50),
    _Hh3cDot11WIPSAckStaHtGreenField_Type()
)
hh3cDot11WIPSAckStaHtGreenField.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11WIPSAckStaHtGreenField.setStatus("current")
_Hh3cDot11WIPSAckStaWireBdg_Type = Integer32
_Hh3cDot11WIPSAckStaWireBdg_Object = MibTableColumn
hh3cDot11WIPSAckStaWireBdg = _Hh3cDot11WIPSAckStaWireBdg_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 15, 2, 13, 1, 51),
    _Hh3cDot11WIPSAckStaWireBdg_Type()
)
hh3cDot11WIPSAckStaWireBdg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11WIPSAckStaWireBdg.setStatus("current")
_Hh3cDot11WIPSAckStaApFld_Type = Integer32
_Hh3cDot11WIPSAckStaApFld_Object = MibTableColumn
hh3cDot11WIPSAckStaApFld = _Hh3cDot11WIPSAckStaApFld_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 15, 2, 13, 1, 52),
    _Hh3cDot11WIPSAckStaApFld_Type()
)
hh3cDot11WIPSAckStaApFld.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11WIPSAckStaApFld.setStatus("current")
_Hh3cDot11WIPSAckStaAssociaOverf_Type = Integer32
_Hh3cDot11WIPSAckStaAssociaOverf_Object = MibTableColumn
hh3cDot11WIPSAckStaAssociaOverf = _Hh3cDot11WIPSAckStaAssociaOverf_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 15, 2, 13, 1, 53),
    _Hh3cDot11WIPSAckStaAssociaOverf_Type()
)
hh3cDot11WIPSAckStaAssociaOverf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11WIPSAckStaAssociaOverf.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HH3C-DOT11-WIPS-MIB",
    **{"Hh3cDot11WIPSEnabledStatus": Hh3cDot11WIPSEnabledStatus,
       "Hh3cDot11WIPSRtLmtType": Hh3cDot11WIPSRtLmtType,
       "Hh3cDot11WIPSDeviceType": Hh3cDot11WIPSDeviceType,
       "Hh3cDot11WIPSPolicyTypeValue": Hh3cDot11WIPSPolicyTypeValue,
       "Hh3cDot11WIPSClassifyType": Hh3cDot11WIPSClassifyType,
       "Hh3cDot11WIPSRadioType": Hh3cDot11WIPSRadioType,
       "Hh3cDot11WIPSDevStatus": Hh3cDot11WIPSDevStatus,
       "Hh3cDot11WIPSAPType": Hh3cDot11WIPSAPType,
       "Hh3cDot11WIPSDevClassifyWay": Hh3cDot11WIPSDevClassifyWay,
       "Hh3cDot11WIPSAPClassifyType": Hh3cDot11WIPSAPClassifyType,
       "Hh3cDot11WIPSStaClassifyType": Hh3cDot11WIPSStaClassifyType,
       "Hh3cDot11WIPSChannel": Hh3cDot11WIPSChannel,
       "Hh3cDot11WIPSEncryptMethod": Hh3cDot11WIPSEncryptMethod,
       "Hh3cDot11WIPSAuthMethod": Hh3cDot11WIPSAuthMethod,
       "Hh3cDot11WIPSAPSecurityType": Hh3cDot11WIPSAPSecurityType,
       "Hh3cDot11WIPSMalformedType": Hh3cDot11WIPSMalformedType,
       "Hh3cDot11WIPSCtmType": Hh3cDot11WIPSCtmType,
       "Hh3cDot11WIPSRuleTypes": Hh3cDot11WIPSRuleTypes,
       "Hh3cDot11WIPSSigFrameTypes": Hh3cDot11WIPSSigFrameTypes,
       "Hh3cDot11WIPSSigFrameSubTypes": Hh3cDot11WIPSSigFrameSubTypes,
       "Hh3cDot11WIPSSigSsidMatchTypes": Hh3cDot11WIPSSigSsidMatchTypes,
       "Hh3cDot11WIPSSigMacMacType": Hh3cDot11WIPSSigMacMacType,
       "Hh3cDot11WIPSManualAPType": Hh3cDot11WIPSManualAPType,
       "Hh3cDot11WIPSDtcAckTypes": Hh3cDot11WIPSDtcAckTypes,
       "Hh3cDot11WIPSDtcDevTimeTypes": Hh3cDot11WIPSDtcDevTimeTypes,
       "Hh3cDot11WIPSFldDctType": Hh3cDot11WIPSFldDctType,
       "Hh3cDot11WIPSAPClaAuthMethods": Hh3cDot11WIPSAPClaAuthMethods,
       "Hh3cDot11WIPSAPClassifyCmpType": Hh3cDot11WIPSAPClassifyCmpType,
       "Hh3cDot11WIPSAPClasSsidCmpType": Hh3cDot11WIPSAPClasSsidCmpType,
       "Hh3cDot11WIPSAPClaSecurityType": Hh3cDot11WIPSAPClaSecurityType,
       "Hh3cDot11WIPSAlyAPClaRuleType": Hh3cDot11WIPSAlyAPClaRuleType,
       "Hh3cDot11WIPSOuiAddress": Hh3cDot11WIPSOuiAddress,
       "hh3cDot11WIPS": hh3cDot11WIPS,
       "hh3cDot11WIPSConfigGroup": hh3cDot11WIPSConfigGroup,
       "hh3cDot11WIPSVsdTable": hh3cDot11WIPSVsdTable,
       "hh3cDot11WIPSVsdEntry": hh3cDot11WIPSVsdEntry,
       "hh3cDot11WIPSVsdName": hh3cDot11WIPSVsdName,
       "hh3cDot11WIPSVsdRowStatus": hh3cDot11WIPSVsdRowStatus,
       "hh3cDot11WIPSVsdDetectPolicy": hh3cDot11WIPSVsdDetectPolicy,
       "hh3cDot11WIPSVsdCtmPolicy": hh3cDot11WIPSVsdCtmPolicy,
       "hh3cDot11WIPSVsdSignaturePolicy": hh3cDot11WIPSVsdSignaturePolicy,
       "hh3cDot11WIPSVsdClasPolicy": hh3cDot11WIPSVsdClasPolicy,
       "hh3cDot11WIPSAp2VsdTable": hh3cDot11WIPSAp2VsdTable,
       "hh3cDot11WIPSAp2VsdEntry": hh3cDot11WIPSAp2VsdEntry,
       "hh3cDot11WIPSAp2VsdApName": hh3cDot11WIPSAp2VsdApName,
       "hh3cDot11WIPSAp2VsdRowStatus": hh3cDot11WIPSAp2VsdRowStatus,
       "hh3cDot11WIPSAp2VsdVsdName": hh3cDot11WIPSAp2VsdVsdName,
       "hh3cDot11WIPSApRadioTable": hh3cDot11WIPSApRadioTable,
       "hh3cDot11WIPSApRadioEntry": hh3cDot11WIPSApRadioEntry,
       "hh3cDot11WIPSApRadioApName": hh3cDot11WIPSApRadioApName,
       "hh3cDot11WIPSApRadioRadioID": hh3cDot11WIPSApRadioRadioID,
       "hh3cDot11WIPSApRadioStatus": hh3cDot11WIPSApRadioStatus,
       "hh3cDot11WIPSRuleTable": hh3cDot11WIPSRuleTable,
       "hh3cDot11WIPSRuleEntry": hh3cDot11WIPSRuleEntry,
       "hh3cDot11WIPSRuleType": hh3cDot11WIPSRuleType,
       "hh3cDot11WIPSRuleId": hh3cDot11WIPSRuleId,
       "hh3cDot11WIPSRuleRowStatus": hh3cDot11WIPSRuleRowStatus,
       "hh3cDot11WIPSAlySigRuleTable": hh3cDot11WIPSAlySigRuleTable,
       "hh3cDot11WIPSAlySigRuleEntry": hh3cDot11WIPSAlySigRuleEntry,
       "hh3cDot11WIPSAlySigPolicyName": hh3cDot11WIPSAlySigPolicyName,
       "hh3cDot11WIPSAlySigRuleID": hh3cDot11WIPSAlySigRuleID,
       "hh3cDot11WIPSAlySigRowStatus": hh3cDot11WIPSAlySigRowStatus,
       "hh3cDot11WIPSAlyClaRuleTable": hh3cDot11WIPSAlyClaRuleTable,
       "hh3cDot11WIPSAlyClaRuleEntry": hh3cDot11WIPSAlyClaRuleEntry,
       "hh3cDot11WIPSAlyClaPolicyName": hh3cDot11WIPSAlyClaPolicyName,
       "hh3cDot11WIPSAlyClasRuleID": hh3cDot11WIPSAlyClasRuleID,
       "hh3cDot11WIPSAlyClaRuleType": hh3cDot11WIPSAlyClaRuleType,
       "hh3cDot11WIPSAlyClaRuleLevel": hh3cDot11WIPSAlyClaRuleLevel,
       "hh3cDot11WIPSAlyClaRowStatus": hh3cDot11WIPSAlyClaRowStatus,
       "hh3cDot11WIPSTrustMacTable": hh3cDot11WIPSTrustMacTable,
       "hh3cDot11WIPSTrustMacEntry": hh3cDot11WIPSTrustMacEntry,
       "hh3cDot11WIPSTrustMacPolicyName": hh3cDot11WIPSTrustMacPolicyName,
       "hh3cDot11WIPSTrustMacAddress": hh3cDot11WIPSTrustMacAddress,
       "hh3cDot11WIPSTrustMacRowStatus": hh3cDot11WIPSTrustMacRowStatus,
       "hh3cDot11WIPSBlockMacTable": hh3cDot11WIPSBlockMacTable,
       "hh3cDot11WIPSBlockMacEntry": hh3cDot11WIPSBlockMacEntry,
       "hh3cDot11WIPSBlockMacPolicyName": hh3cDot11WIPSBlockMacPolicyName,
       "hh3cDot11WIPSBlockMacAddress": hh3cDot11WIPSBlockMacAddress,
       "hh3cDot11WIPSBlockMacRowStatus": hh3cDot11WIPSBlockMacRowStatus,
       "hh3cDot11WIPSManulClaTable": hh3cDot11WIPSManulClaTable,
       "hh3cDot11WIPSManulClaEntry": hh3cDot11WIPSManulClaEntry,
       "hh3cDot11WIPSManulClaPlyName": hh3cDot11WIPSManulClaPlyName,
       "hh3cDot11WIPSManulClaMac": hh3cDot11WIPSManulClaMac,
       "hh3cDot11WIPSManulClassifyType": hh3cDot11WIPSManulClassifyType,
       "hh3cDot11WIPSManuClaRowStatus": hh3cDot11WIPSManuClaRowStatus,
       "hh3cDot11WIPSTrustOuiTable": hh3cDot11WIPSTrustOuiTable,
       "hh3cDot11WIPSTrustOuiEntry": hh3cDot11WIPSTrustOuiEntry,
       "hh3cDot11WIPSTrustOuiPolicyName": hh3cDot11WIPSTrustOuiPolicyName,
       "hh3cDot11WIPSTrustOuiMac": hh3cDot11WIPSTrustOuiMac,
       "hh3cDot11WIPSTrustOuiRowStatus": hh3cDot11WIPSTrustOuiRowStatus,
       "hh3cDot11WIPSTrustSSidTable": hh3cDot11WIPSTrustSSidTable,
       "hh3cDot11WIPSTrustSSidEntry": hh3cDot11WIPSTrustSSidEntry,
       "hh3cDot11WIPSTrustSSidPlyName": hh3cDot11WIPSTrustSSidPlyName,
       "hh3cDot11WIPSTrustSSidName": hh3cDot11WIPSTrustSSidName,
       "hh3cDot11WIPSTrustSSidRowStatus": hh3cDot11WIPSTrustSSidRowStatus,
       "hh3cDot11WIPSMalfDtcTable": hh3cDot11WIPSMalfDtcTable,
       "hh3cDot11WIPSMalfDtcEntry": hh3cDot11WIPSMalfDtcEntry,
       "hh3cDot11WIPSMalfDtcPolicyName": hh3cDot11WIPSMalfDtcPolicyName,
       "hh3cDot11WIPSMalfDtcType": hh3cDot11WIPSMalfDtcType,
       "hh3cDot11WIPSMalfDtcQuietTime": hh3cDot11WIPSMalfDtcQuietTime,
       "hh3cDot11WIPSMalfDtciStatus": hh3cDot11WIPSMalfDtciStatus,
       "hh3cDot11WIPSLgeDutTable": hh3cDot11WIPSLgeDutTable,
       "hh3cDot11WIPSLgeDutEntry": hh3cDot11WIPSLgeDutEntry,
       "hh3cDot11WIPSLgeDutPolicyName": hh3cDot11WIPSLgeDutPolicyName,
       "hh3cDot11WIPSLgeDutThreshold": hh3cDot11WIPSLgeDutThreshold,
       "hh3cDot11WIPSLgeDutQuietTime": hh3cDot11WIPSLgeDutQuietTime,
       "hh3cDot11WIPSLgeDutStatus": hh3cDot11WIPSLgeDutStatus,
       "hh3cDot11WIPSRtLmtTable": hh3cDot11WIPSRtLmtTable,
       "hh3cDot11WIPSRtLmtEntry": hh3cDot11WIPSRtLmtEntry,
       "hh3cDot11WIPSRtLmtPolicyName": hh3cDot11WIPSRtLmtPolicyName,
       "hh3cDot11WIPSRtLmtRtLmtType": hh3cDot11WIPSRtLmtRtLmtType,
       "hh3cDot11WIPSRtLmtInterval": hh3cDot11WIPSRtLmtInterval,
       "hh3cDot11WIPSRtLmtThreshold": hh3cDot11WIPSRtLmtThreshold,
       "hh3cDot11WIPSRtLmtQuiet": hh3cDot11WIPSRtLmtQuiet,
       "hh3cDot11WIPSRtLmtStatus": hh3cDot11WIPSRtLmtStatus,
       "hh3cDot11WIPSDtcAckTable": hh3cDot11WIPSDtcAckTable,
       "hh3cDot11WIPSDtcAckEntry": hh3cDot11WIPSDtcAckEntry,
       "hh3cDot11WIPSDtcAckPolicyName": hh3cDot11WIPSDtcAckPolicyName,
       "hh3cDot11WIPSDtcAckType": hh3cDot11WIPSDtcAckType,
       "hh3cDot11WIPSDtcAckQuietTime": hh3cDot11WIPSDtcAckQuietTime,
       "hh3cDot11WIPSDtcAckInterval": hh3cDot11WIPSDtcAckInterval,
       "hh3cDot11WIPSDtcAckThreshold": hh3cDot11WIPSDtcAckThreshold,
       "hh3cDot11WIPSDtcAckStatus": hh3cDot11WIPSDtcAckStatus,
       "hh3cDot11WIPSDtcDevTimeTable": hh3cDot11WIPSDtcDevTimeTable,
       "hh3cDot11WIPSDtcDevTimeEntry": hh3cDot11WIPSDtcDevTimeEntry,
       "hh3cDot11WIPSDtcDevTimePlyName": hh3cDot11WIPSDtcDevTimePlyName,
       "hh3cDot11WIPSDtcDevTimeType": hh3cDot11WIPSDtcDevTimeType,
       "hh3cDot11WIPSDtcDevTimeInactive": hh3cDot11WIPSDtcDevTimeInactive,
       "hh3cDot11WIPSDtcDevTimeAging": hh3cDot11WIPSDtcDevTimeAging,
       "hh3cDot11WIPSDtcDevTimeStatus": hh3cDot11WIPSDtcDevTimeStatus,
       "hh3cDot11WIPSApimperTable": hh3cDot11WIPSApimperTable,
       "hh3cDot11WIPSApimperEntry": hh3cDot11WIPSApimperEntry,
       "hh3cDot11WIPSApimperPolicyName": hh3cDot11WIPSApimperPolicyName,
       "hh3cDot11WIPSApimperQuiet": hh3cDot11WIPSApimperQuiet,
       "hh3cDot11WIPSApimperStatus": hh3cDot11WIPSApimperStatus,
       "hh3cDot11WIPSDctSoftApTable": hh3cDot11WIPSDctSoftApTable,
       "hh3cDot11WIPSDctSoftApEntry": hh3cDot11WIPSDctSoftApEntry,
       "hh3cDot11WIPSDctSoftApPlyName": hh3cDot11WIPSDctSoftApPlyName,
       "hh3cDot11WIPSDctSoftApThold": hh3cDot11WIPSDctSoftApThold,
       "hh3cDot11WIPSDctSoftApStatus": hh3cDot11WIPSDctSoftApStatus,
       "hh3cDot11WIPSPowerSaveTable": hh3cDot11WIPSPowerSaveTable,
       "hh3cDot11WIPSPowerSaveEntry": hh3cDot11WIPSPowerSaveEntry,
       "hh3cDot11WIPSPowerSavePlyName": hh3cDot11WIPSPowerSavePlyName,
       "hh3cDot11WIPSPowerSaveInterval": hh3cDot11WIPSPowerSaveInterval,
       "hh3cDot11WIPSPowerSaveMinOffPkt": hh3cDot11WIPSPowerSaveMinOffPkt,
       "hh3cDot11WIPSPowerSaveOnOffPct": hh3cDot11WIPSPowerSaveOnOffPct,
       "hh3cDot11WIPSPowerSaveQuiet": hh3cDot11WIPSPowerSaveQuiet,
       "hh3cDot11WIPSPowerSaveStatus": hh3cDot11WIPSPowerSaveStatus,
       "hh3cDot11WIPSIgnListMacTable": hh3cDot11WIPSIgnListMacTable,
       "hh3cDot11WIPSIgnListMacEntry": hh3cDot11WIPSIgnListMacEntry,
       "hh3cDot11WIPSIgnListMacMacAddr": hh3cDot11WIPSIgnListMacMacAddr,
       "hh3cDot11WIPSIgnListMacRowStus": hh3cDot11WIPSIgnListMacRowStus,
       "hh3cDot11WIPSHoneyPotTable": hh3cDot11WIPSHoneyPotTable,
       "hh3cDot11WIPSHoneyPotEntry": hh3cDot11WIPSHoneyPotEntry,
       "hh3cDot11WIPSHoneyPotPlyName": hh3cDot11WIPSHoneyPotPlyName,
       "hh3cDot11WIPSHoneyPotSim": hh3cDot11WIPSHoneyPotSim,
       "hh3cDot11WIPSHoneyPotQuiet": hh3cDot11WIPSHoneyPotQuiet,
       "hh3cDot11WIPSHoneyPotStatus": hh3cDot11WIPSHoneyPotStatus,
       "hh3cDot11WIPSAPFldTable": hh3cDot11WIPSAPFldTable,
       "hh3cDot11WIPSAPFldEntry": hh3cDot11WIPSAPFldEntry,
       "hh3cDot11WIPSAPFldPolicyName": hh3cDot11WIPSAPFldPolicyName,
       "hh3cDot11WIPSAPFldApnum": hh3cDot11WIPSAPFldApnum,
       "hh3cDot11WIPSAPFldExceed": hh3cDot11WIPSAPFldExceed,
       "hh3cDot11WIPSAPFldQuiet": hh3cDot11WIPSAPFldQuiet,
       "hh3cDot11WIPSAPFldStatus": hh3cDot11WIPSAPFldStatus,
       "hh3cDot11WIPSCtmManualsTable": hh3cDot11WIPSCtmManualsTable,
       "hh3cDot11WIPSCtmManualsEntry": hh3cDot11WIPSCtmManualsEntry,
       "hh3cDot11WIPSCtmManualsPlyName": hh3cDot11WIPSCtmManualsPlyName,
       "hh3cDot11WIPSCtmManualsMacAddr": hh3cDot11WIPSCtmManualsMacAddr,
       "hh3cDot11WIPSCtmManualsRowStus": hh3cDot11WIPSCtmManualsRowStus,
       "hh3cDot11WIPSCtmSensorTable": hh3cDot11WIPSCtmSensorTable,
       "hh3cDot11WIPSCtmSensorEntry": hh3cDot11WIPSCtmSensorEntry,
       "hh3cDot11WIPSCtmSensorPolicyName": hh3cDot11WIPSCtmSensorPolicyName,
       "hh3cDot11WIPSCtmSensoriStatus": hh3cDot11WIPSCtmSensoriStatus,
       "hh3cDot11WIPSInvOuiStateTable": hh3cDot11WIPSInvOuiStateTable,
       "hh3cDot11WIPSInvOuiStateEntry": hh3cDot11WIPSInvOuiStateEntry,
       "hh3cDot11WIPSInvOuiStaPlyName": hh3cDot11WIPSInvOuiStaPlyName,
       "hh3cDot11WIPSInvOuiStaiStatus": hh3cDot11WIPSInvOuiStaiStatus,
       "hh3cDot11WIPSAPClaAuthTable": hh3cDot11WIPSAPClaAuthTable,
       "hh3cDot11WIPSAPClaAuthEntry": hh3cDot11WIPSAPClaAuthEntry,
       "hh3cDot11WIPSAPClaAuthRuleID": hh3cDot11WIPSAPClaAuthRuleID,
       "hh3cDot11WIPSAPClaAuthMethod": hh3cDot11WIPSAPClaAuthMethod,
       "hh3cDot11WIPSAPClaAuthType": hh3cDot11WIPSAPClaAuthType,
       "hh3cDot11WIPSAPClaAuthStatus": hh3cDot11WIPSAPClaAuthStatus,
       "hh3cDot11WIPSAPClaCltOnlTable": hh3cDot11WIPSAPClaCltOnlTable,
       "hh3cDot11WIPSAPClaCltOnlEntry": hh3cDot11WIPSAPClaCltOnlEntry,
       "hh3cDot11WIPSAPClaCltOnlRuleID": hh3cDot11WIPSAPClaCltOnlRuleID,
       "hh3cDot11WIPSAPClaCltOnlV1": hh3cDot11WIPSAPClaCltOnlV1,
       "hh3cDot11WIPSAPClaCltOnlV2": hh3cDot11WIPSAPClaCltOnlV2,
       "hh3cDot11WIPSAPClaCltOnlSts": hh3cDot11WIPSAPClaCltOnlSts,
       "hh3cDot11WIPSAPClaDiscrTable": hh3cDot11WIPSAPClaDiscrTable,
       "hh3cDot11WIPSAPClaDiscrEntry": hh3cDot11WIPSAPClaDiscrEntry,
       "hh3cDot11WIPSAPClaDiscrRuleID": hh3cDot11WIPSAPClaDiscrRuleID,
       "hh3cDot11WIPSAPClaDiscrV1": hh3cDot11WIPSAPClaDiscrV1,
       "hh3cDot11WIPSAPClaDiscrV2": hh3cDot11WIPSAPClaDiscrV2,
       "hh3cDot11WIPSAPClaDiscrSta": hh3cDot11WIPSAPClaDiscrSta,
       "hh3cDot11WIPSAPClaRssiTable": hh3cDot11WIPSAPClaRssiTable,
       "hh3cDot11WIPSAPClaRssiEntry": hh3cDot11WIPSAPClaRssiEntry,
       "hh3cDot11WIPSAPClaRssiRuleID": hh3cDot11WIPSAPClaRssiRuleID,
       "hh3cDot11WIPSAPClaRssiV1": hh3cDot11WIPSAPClaRssiV1,
       "hh3cDot11WIPSAPClaRssiV2": hh3cDot11WIPSAPClaRssiV2,
       "hh3cDot11WIPSAPClaRssiSta": hh3cDot11WIPSAPClaRssiSta,
       "hh3cDot11WIPSAPClaUpdurTable": hh3cDot11WIPSAPClaUpdurTable,
       "hh3cDot11WIPSAPClaUpdurEntry": hh3cDot11WIPSAPClaUpdurEntry,
       "hh3cDot11WIPSAPClaUpdurRuleID": hh3cDot11WIPSAPClaUpdurRuleID,
       "hh3cDot11WIPSAPClaUpdurV1": hh3cDot11WIPSAPClaUpdurV1,
       "hh3cDot11WIPSAPClaUpdurV2": hh3cDot11WIPSAPClaUpdurV2,
       "hh3cDot11WIPSAPClaUpdurSta": hh3cDot11WIPSAPClaUpdurSta,
       "hh3cDot11WIPSAPClaOuiTable": hh3cDot11WIPSAPClaOuiTable,
       "hh3cDot11WIPSAPClaOuiEntry": hh3cDot11WIPSAPClaOuiEntry,
       "hh3cDot11WIPSAPClaOuiRuleID": hh3cDot11WIPSAPClaOuiRuleID,
       "hh3cDot11WIPSAPClaOuiMac": hh3cDot11WIPSAPClaOuiMac,
       "hh3cDot11WIPSAPClaOuiStatus": hh3cDot11WIPSAPClaOuiStatus,
       "hh3cDot11WIPSAPClaSryTable": hh3cDot11WIPSAPClaSryTable,
       "hh3cDot11WIPSAPClaSryEntry": hh3cDot11WIPSAPClaSryEntry,
       "hh3cDot11WIPSAPClaSryRuleID": hh3cDot11WIPSAPClaSryRuleID,
       "hh3cDot11WIPSAPClaSryType": hh3cDot11WIPSAPClaSryType,
       "hh3cDot11WIPSAPClaSryCmpType": hh3cDot11WIPSAPClaSryCmpType,
       "hh3cDot11WIPSAPClaSrySta": hh3cDot11WIPSAPClaSrySta,
       "hh3cDot11WIPSAPClaSsidTable": hh3cDot11WIPSAPClaSsidTable,
       "hh3cDot11WIPSAPClaSsidEntry": hh3cDot11WIPSAPClaSsidEntry,
       "hh3cDot11WIPSAPClaSsidRuleID": hh3cDot11WIPSAPClaSsidRuleID,
       "hh3cDot11WIPSAPClaSsidName": hh3cDot11WIPSAPClaSsidName,
       "hh3cDot11WIPSAPClaSsidcase": hh3cDot11WIPSAPClaSsidcase,
       "hh3cDot11WIPSAPClaSsidCmpType": hh3cDot11WIPSAPClaSsidCmpType,
       "hh3cDot11WIPSAPClaSsidStatus": hh3cDot11WIPSAPClaSsidStatus,
       "hh3cDot11WIPSDtcSigTable": hh3cDot11WIPSDtcSigTable,
       "hh3cDot11WIPSDtcSigEntry": hh3cDot11WIPSDtcSigEntry,
       "hh3cDot11WIPSDtcSigPolicyName": hh3cDot11WIPSDtcSigPolicyName,
       "hh3cDot11WIPSDtcSigInterval": hh3cDot11WIPSDtcSigInterval,
       "hh3cDot11WIPSDtcSigQuiet": hh3cDot11WIPSDtcSigQuiet,
       "hh3cDot11WIPSDtcSigThreshold": hh3cDot11WIPSDtcSigThreshold,
       "hh3cDot11WIPSDtcSigStatus": hh3cDot11WIPSDtcSigStatus,
       "hh3cDot11WIPSPolicyTable": hh3cDot11WIPSPolicyTable,
       "hh3cDot11WIPSPolicyEntry": hh3cDot11WIPSPolicyEntry,
       "hh3cDot11WIPSPolicyType": hh3cDot11WIPSPolicyType,
       "hh3cDot11WIPSPolicyName": hh3cDot11WIPSPolicyName,
       "hh3cDot11WIPSPolicyRowStatus": hh3cDot11WIPSPolicyRowStatus,
       "hh3cDot11WIPSSigFrameTypeTable": hh3cDot11WIPSSigFrameTypeTable,
       "hh3cDot11WIPSSigFrameTypeEntry": hh3cDot11WIPSSigFrameTypeEntry,
       "hh3cDot11WIPSSigFrameTypeRuleId": hh3cDot11WIPSSigFrameTypeRuleId,
       "hh3cDot11WIPSSigFrameType": hh3cDot11WIPSSigFrameType,
       "hh3cDot11WIPSSigFrameSubType": hh3cDot11WIPSSigFrameSubType,
       "hh3cDot11WIPSSigFrameTypeStatus": hh3cDot11WIPSSigFrameTypeStatus,
       "hh3cDot11WIPSCtmTable": hh3cDot11WIPSCtmTable,
       "hh3cDot11WIPSCtmEntry": hh3cDot11WIPSCtmEntry,
       "hh3cDot11WIPSCtmPolicyName": hh3cDot11WIPSCtmPolicyName,
       "hh3cDot11WIPSCtmClassifyType": hh3cDot11WIPSCtmClassifyType,
       "hh3cDot11WIPSCtmStatus": hh3cDot11WIPSCtmStatus,
       "hh3cDot11WIPSSigPatternTable": hh3cDot11WIPSSigPatternTable,
       "hh3cDot11WIPSSigPatternEntry": hh3cDot11WIPSSigPatternEntry,
       "hh3cDot11WIPSSigPatternRuleId": hh3cDot11WIPSSigPatternRuleId,
       "hh3cDot11WIPSSigPatternNum": hh3cDot11WIPSSigPatternNum,
       "hh3cDot11WIPSSigPatternOffset": hh3cDot11WIPSSigPatternOffset,
       "hh3cDot11WIPSSigPatternMask": hh3cDot11WIPSSigPatternMask,
       "hh3cDot11WIPSSigPatternValue1": hh3cDot11WIPSSigPatternValue1,
       "hh3cDot11WIPSSigPatternValue2": hh3cDot11WIPSSigPatternValue2,
       "hh3cDot11WIPSSigPatternFromPld": hh3cDot11WIPSSigPatternFromPld,
       "hh3cDot11WIPSSigPatternRowStatus": hh3cDot11WIPSSigPatternRowStatus,
       "hh3cDot11WIPSSigSeqNumTable": hh3cDot11WIPSSigSeqNumTable,
       "hh3cDot11WIPSSigSeqNumEntry": hh3cDot11WIPSSigSeqNumEntry,
       "hh3cDot11WIPSSigSeqNumRuleId": hh3cDot11WIPSSigSeqNumRuleId,
       "hh3cDot11WIPSSigSeqNumValue1": hh3cDot11WIPSSigSeqNumValue1,
       "hh3cDot11WIPSSigSeqNumValue2": hh3cDot11WIPSSigSeqNumValue2,
       "hh3cDot11WIPSSigSeqNumStatus": hh3cDot11WIPSSigSeqNumStatus,
       "hh3cDot11WIPSSigSsidTable": hh3cDot11WIPSSigSsidTable,
       "hh3cDot11WIPSSigSsidEntry": hh3cDot11WIPSSigSsidEntry,
       "hh3cDot11WIPSSigSsidRuleId": hh3cDot11WIPSSigSsidRuleId,
       "hh3cDot11WIPSSigSsidSsid": hh3cDot11WIPSSigSsidSsid,
       "hh3cDot11WIPSSigSsidCase": hh3cDot11WIPSSigSsidCase,
       "hh3cDot11WIPSSigSsidMatchType": hh3cDot11WIPSSigSsidMatchType,
       "hh3cDot11WIPSSigSsidStatus": hh3cDot11WIPSSigSsidStatus,
       "hh3cDot11WIPSSigSsidLengthTable": hh3cDot11WIPSSigSsidLengthTable,
       "hh3cDot11WIPSSigSsidLengthEntry": hh3cDot11WIPSSigSsidLengthEntry,
       "hh3cDot11WIPSSigSsidLengthRuleId": hh3cDot11WIPSSigSsidLengthRuleId,
       "hh3cDot11WIPSSigSsidLengthValue1": hh3cDot11WIPSSigSsidLengthValue1,
       "hh3cDot11WIPSSigSsidLengthValue2": hh3cDot11WIPSSigSsidLengthValue2,
       "hh3cDot11WIPSSigSsidLengthStatus": hh3cDot11WIPSSigSsidLengthStatus,
       "hh3cDot11WIPSFldDetectTable": hh3cDot11WIPSFldDetectTable,
       "hh3cDot11WIPSFldDetectEntry": hh3cDot11WIPSFldDetectEntry,
       "hh3cDot11WIPSFldDetectPlyName": hh3cDot11WIPSFldDetectPlyName,
       "hh3cDot11WIPSFldDetectType": hh3cDot11WIPSFldDetectType,
       "hh3cDot11WIPSFldDetectInter": hh3cDot11WIPSFldDetectInter,
       "hh3cDot11WIPSFldDetectThresh": hh3cDot11WIPSFldDetectThresh,
       "hh3cDot11WIPSFldDetectQuiet": hh3cDot11WIPSFldDetectQuiet,
       "hh3cDot11WIPSFldDetectStatus": hh3cDot11WIPSFldDetectStatus,
       "hh3cDot11WIPSSignatureMacTable": hh3cDot11WIPSSignatureMacTable,
       "hh3cDot11WIPSSignatureMacEntry": hh3cDot11WIPSSignatureMacEntry,
       "hh3cDot11WIPSSignatureMacRuleId": hh3cDot11WIPSSignatureMacRuleId,
       "hh3cDot11WIPSSignatureMacMacTyp": hh3cDot11WIPSSignatureMacMacTyp,
       "hh3cDot11WIPSSignatureMacMacAdd": hh3cDot11WIPSSignatureMacMacAdd,
       "hh3cDot11WIPSSignatureMacStatus": hh3cDot11WIPSSignatureMacStatus,
       "hh3cDot11WIPSNatDetectTable": hh3cDot11WIPSNatDetectTable,
       "hh3cDot11WIPSNatDetectEntry": hh3cDot11WIPSNatDetectEntry,
       "hh3cDot11WIPSNatDetectApName": hh3cDot11WIPSNatDetectApName,
       "hh3cDot11WIPSNatDetectStatus": hh3cDot11WIPSNatDetectStatus,
       "hh3cDot11WIPSDataGroup": hh3cDot11WIPSDataGroup,
       "hh3cDot11WIPSDctAPTable": hh3cDot11WIPSDctAPTable,
       "hh3cDot11WIPSDctAPEntry": hh3cDot11WIPSDctAPEntry,
       "hh3cDot11WIPSDctAPVSD": hh3cDot11WIPSDctAPVSD,
       "hh3cDot11WIPSDctAPMac": hh3cDot11WIPSDctAPMac,
       "hh3cDot11WIPSDctAPClassifyWay": hh3cDot11WIPSDctAPClassifyWay,
       "hh3cDot11WIPSDctAPClassifyType": hh3cDot11WIPSDctAPClassifyType,
       "hh3cDot11WIPSDctAPSeverityLevel": hh3cDot11WIPSDctAPSeverityLevel,
       "hh3cDot11WIPSDctAPStatus": hh3cDot11WIPSDctAPStatus,
       "hh3cDot11WIPSDctAPStatusDut": hh3cDot11WIPSDctAPStatusDut,
       "hh3cDot11WIPSDctAPVendor": hh3cDot11WIPSDctAPVendor,
       "hh3cDot11WIPSDctAPSSID": hh3cDot11WIPSDctAPSSID,
       "hh3cDot11WIPSDctAPSecurity": hh3cDot11WIPSDctAPSecurity,
       "hh3cDot11WIPSDctAPEncryptMethod": hh3cDot11WIPSDctAPEncryptMethod,
       "hh3cDot11WIPSDctAPAuthMethod": hh3cDot11WIPSDctAPAuthMethod,
       "hh3cDot11WIPSDctAPRadioType": hh3cDot11WIPSDctAPRadioType,
       "hh3cDot11WIPSDctAPWorkChannel": hh3cDot11WIPSDctAPWorkChannel,
       "hh3cDot11WIPSDctAPIsCountered": hh3cDot11WIPSDctAPIsCountered,
       "hh3cDot11WIPSDctAPAttachStaNum": hh3cDot11WIPSDctAPAttachStaNum,
       "hh3cDot11WIPSDctAPRptSensorNum": hh3cDot11WIPSDctAPRptSensorNum,
       "hh3cDot11WIPSDctAPIsBdcastSSID": hh3cDot11WIPSDctAPIsBdcastSSID,
       "hh3cDot11WIPSDctAPType": hh3cDot11WIPSDctAPType,
       "hh3cDot11WIPSDctAPIsQosSported": hh3cDot11WIPSDctAPIsQosSported,
       "hh3cDot11WIPSDctAPBeaconItv": hh3cDot11WIPSDctAPBeaconItv,
       "hh3cDot11WIPSDctAPUpDuration": hh3cDot11WIPSDctAPUpDuration,
       "hh3cDot11WIPSDctStaTable": hh3cDot11WIPSDctStaTable,
       "hh3cDot11WIPSDctStaEntry": hh3cDot11WIPSDctStaEntry,
       "hh3cDot11WIPSDctStaVSD": hh3cDot11WIPSDctStaVSD,
       "hh3cDot11WIPSDctStaMac": hh3cDot11WIPSDctStaMac,
       "hh3cDot11WIPSDctStaAssocBSSID": hh3cDot11WIPSDctStaAssocBSSID,
       "hh3cDot11WIPSDctStaClassifyWay": hh3cDot11WIPSDctStaClassifyWay,
       "hh3cDot11WIPSDctStaClassifyType": hh3cDot11WIPSDctStaClassifyType,
       "hh3cDot11WIPSDctStaSeverityLevel": hh3cDot11WIPSDctStaSeverityLevel,
       "hh3cDot11WIPSDctStaIsDissociate": hh3cDot11WIPSDctStaIsDissociate,
       "hh3cDot11WIPSDctStaStatus": hh3cDot11WIPSDctStaStatus,
       "hh3cDot11WIPSDctStaStatusDurat": hh3cDot11WIPSDctStaStatusDurat,
       "hh3cDot11WIPSDctStaVendor": hh3cDot11WIPSDctStaVendor,
       "hh3cDot11WIPSDctStaRadioType": hh3cDot11WIPSDctStaRadioType,
       "hh3cDot11WIPSDctStaRptSensorNum": hh3cDot11WIPSDctStaRptSensorNum,
       "hh3cDot11WIPSDctStaWorkChannel": hh3cDot11WIPSDctStaWorkChannel,
       "hh3cDot11WIPSDctStaIsCountered": hh3cDot11WIPSDctStaIsCountered,
       "hh3cDot11WIPSApAssoCltTable": hh3cDot11WIPSApAssoCltTable,
       "hh3cDot11WIPSApAssoCltEntry": hh3cDot11WIPSApAssoCltEntry,
       "hh3cDot11WIPSApAssoCltVSDName": hh3cDot11WIPSApAssoCltVSDName,
       "hh3cDot11WIPSApAssoCltApMacAddr": hh3cDot11WIPSApAssoCltApMacAddr,
       "hh3cDot11WIPSApAssoCltClMacAddr": hh3cDot11WIPSApAssoCltClMacAddr,
       "hh3cDot11WIPSApAssoCltIsAsso": hh3cDot11WIPSApAssoCltIsAsso,
       "hh3cDot11WIPSApRpSenTable": hh3cDot11WIPSApRpSenTable,
       "hh3cDot11WIPSApRpSenEntry": hh3cDot11WIPSApRpSenEntry,
       "hh3cDot11WIPSApRpSenVsdName": hh3cDot11WIPSApRpSenVsdName,
       "hh3cDot11WIPSApRpSenMacAddr": hh3cDot11WIPSApRpSenMacAddr,
       "hh3cDot11WIPSApRpSenName": hh3cDot11WIPSApRpSenName,
       "hh3cDot11WIPSApRpSenRadioID": hh3cDot11WIPSApRpSenRadioID,
       "hh3cDot11WIPSApRpSenRssi": hh3cDot11WIPSApRpSenRssi,
       "hh3cDot11WIPSApRpSenChannel": hh3cDot11WIPSApRpSenChannel,
       "hh3cDot11WIPSApRpSenFirstRpTime": hh3cDot11WIPSApRpSenFirstRpTime,
       "hh3cDot11WIPSApRpSenLastRpTime": hh3cDot11WIPSApRpSenLastRpTime,
       "hh3cDot11WIPSCtmRecTable": hh3cDot11WIPSCtmRecTable,
       "hh3cDot11WIPSCtmRecEntry": hh3cDot11WIPSCtmRecEntry,
       "hh3cDot11WIPSCtmRecVsdName": hh3cDot11WIPSCtmRecVsdName,
       "hh3cDot11WIPSCtmRecMacAddress": hh3cDot11WIPSCtmRecMacAddress,
       "hh3cDot11WIPSCtmRecCount": hh3cDot11WIPSCtmRecCount,
       "hh3cDot11WIPSCtmRecSensorName": hh3cDot11WIPSCtmRecSensorName,
       "hh3cDot11WIPSCtmRecDeviceType": hh3cDot11WIPSCtmRecDeviceType,
       "hh3cDot11WIPSCtmRecClassifyType": hh3cDot11WIPSCtmRecClassifyType,
       "hh3cDot11WIPSCtmRecRadioId": hh3cDot11WIPSCtmRecRadioId,
       "hh3cDot11WIPSCtmRecCounterTime": hh3cDot11WIPSCtmRecCounterTime,
       "hh3cDot11WIPSDevTable": hh3cDot11WIPSDevTable,
       "hh3cDot11WIPSDevEntry": hh3cDot11WIPSDevEntry,
       "hh3cDot11WIPSDevVSDName": hh3cDot11WIPSDevVSDName,
       "hh3cDot11WIPSDevTotalApNum": hh3cDot11WIPSDevTotalApNum,
       "hh3cDot11WIPSDevTotalClinetNum": hh3cDot11WIPSDevTotalClinetNum,
       "hh3cDot11WIPSDevAuthApNum": hh3cDot11WIPSDevAuthApNum,
       "hh3cDot11WIPSDevMisConfigApNum": hh3cDot11WIPSDevMisConfigApNum,
       "hh3cDot11WIPSDevRogueApNum": hh3cDot11WIPSDevRogueApNum,
       "hh3cDot11WIPSDevExternalApNum": hh3cDot11WIPSDevExternalApNum,
       "hh3cDot11WIPSDevAdhocNum": hh3cDot11WIPSDevAdhocNum,
       "hh3cDot11WIPSDevMeshApNum": hh3cDot11WIPSDevMeshApNum,
       "hh3cDot11WIPSDevpotenAuthApNum": hh3cDot11WIPSDevpotenAuthApNum,
       "hh3cDot11WIPSDevpotenRogueApNum": hh3cDot11WIPSDevpotenRogueApNum,
       "hh3cDot11WIPSDevPotenExtApNum": hh3cDot11WIPSDevPotenExtApNum,
       "hh3cDot11WIPSDevUncateApNum": hh3cDot11WIPSDevUncateApNum,
       "hh3cDot11WIPSDevAuthClinetNum": hh3cDot11WIPSDevAuthClinetNum,
       "hh3cDot11WIPSDevUnauthClinetNum": hh3cDot11WIPSDevUnauthClinetNum,
       "hh3cDot11WIPSDevMisAssocltNum": hh3cDot11WIPSDevMisAssocltNum,
       "hh3cDot11WIPSDevUncatecltNum": hh3cDot11WIPSDevUncatecltNum,
       "hh3cDot11WIPSCtmDevTable": hh3cDot11WIPSCtmDevTable,
       "hh3cDot11WIPSCtmDevEntry": hh3cDot11WIPSCtmDevEntry,
       "hh3cDot11WIPSCtmDevVsdName": hh3cDot11WIPSCtmDevVsdName,
       "hh3cDot11WIPSCtmDevTotalApNum": hh3cDot11WIPSCtmDevTotalApNum,
       "hh3cDot11WIPSCtmDevTotalStaNum": hh3cDot11WIPSCtmDevTotalStaNum,
       "hh3cDot11WIPSCtmDevMisCfgApNum": hh3cDot11WIPSCtmDevMisCfgApNum,
       "hh3cDot11WIPSCtmDevRogueApNum": hh3cDot11WIPSCtmDevRogueApNum,
       "hh3cDot11WIPSCtmDevExternalApNum": hh3cDot11WIPSCtmDevExternalApNum,
       "hh3cDot11WIPSCtmDevpotAuthApNum": hh3cDot11WIPSCtmDevpotAuthApNum,
       "hh3cDot11WIPSCtmDevpotRguApNum": hh3cDot11WIPSCtmDevpotRguApNum,
       "hh3cDot11WIPSCtmDevpotenExtApNum": hh3cDot11WIPSCtmDevpotenExtApNum,
       "hh3cDot11WIPSCtmDevUncateApNum": hh3cDot11WIPSCtmDevUncateApNum,
       "hh3cDot11WIPSCtmDevUnauthStaNum": hh3cDot11WIPSCtmDevUnauthStaNum,
       "hh3cDot11WIPSCtmDevMisAssCltNum": hh3cDot11WIPSCtmDevMisAssCltNum,
       "hh3cDot11WIPSCtmDevUncatecltNum": hh3cDot11WIPSCtmDevUncatecltNum,
       "hh3cDot11WIPSCtmDevAttackerNum": hh3cDot11WIPSCtmDevAttackerNum,
       "hh3cDot11WIPSCtmDevManuNum": hh3cDot11WIPSCtmDevManuNum,
       "hh3cDot11WIPSCtmDevStaCauseByAP": hh3cDot11WIPSCtmDevStaCauseByAP,
       "hh3cDot11WIPSCltRptApTable": hh3cDot11WIPSCltRptApTable,
       "hh3cDot11WIPSCltRptApEntry": hh3cDot11WIPSCltRptApEntry,
       "hh3cDot11WIPSCltRptApVSDName": hh3cDot11WIPSCltRptApVSDName,
       "hh3cDot11WIPSCltRptApDevMac": hh3cDot11WIPSCltRptApDevMac,
       "hh3cDot11WIPSCltRptApSensorName": hh3cDot11WIPSCltRptApSensorName,
       "hh3cDot11WIPSCltReportApRadioId": hh3cDot11WIPSCltReportApRadioId,
       "hh3cDot11WIPSCltRptApRSSI": hh3cDot11WIPSCltRptApRSSI,
       "hh3cDot11WIPSCltRptApWorkChannel": hh3cDot11WIPSCltRptApWorkChannel,
       "hh3cDot11WIPSCltRptApFirstTime": hh3cDot11WIPSCltRptApFirstTime,
       "hh3cDot11WIPSCltRptApLastTime": hh3cDot11WIPSCltRptApLastTime,
       "hh3cDot11WIPSCltRptApAssocMac": hh3cDot11WIPSCltRptApAssocMac,
       "hh3cDot11WIPSNatDtcCltTable": hh3cDot11WIPSNatDtcCltTable,
       "hh3cDot11WIPSNatDtcCltEntry": hh3cDot11WIPSNatDtcCltEntry,
       "hh3cDot11WIPSNatDtcCltMac": hh3cDot11WIPSNatDtcCltMac,
       "hh3cDot11WIPSNatDtcCltFirstTime": hh3cDot11WIPSNatDtcCltFirstTime,
       "hh3cDot11WIPSNatDtcCltLastTime": hh3cDot11WIPSNatDtcCltLastTime,
       "hh3cDot11WIPSNatDtcCltDuraTime": hh3cDot11WIPSNatDtcCltDuraTime,
       "hh3cDot11WIPSAckStaTable": hh3cDot11WIPSAckStaTable,
       "hh3cDot11WIPSAckStaEntry": hh3cDot11WIPSAckStaEntry,
       "hh3cDot11WIPSAckStaSensorName": hh3cDot11WIPSAckStaSensorName,
       "hh3cDot11WIPSAckStaAssReqFld": hh3cDot11WIPSAckStaAssReqFld,
       "hh3cDot11WIPSAckStaAuthFld": hh3cDot11WIPSAckStaAuthFld,
       "hh3cDot11WIPSAckStaBeaconFld": hh3cDot11WIPSAckStaBeaconFld,
       "hh3cDot11WIPSAckStaBlkAckFld": hh3cDot11WIPSAckStaBlkAckFld,
       "hh3cDot11WIPSAckStaCtsFld": hh3cDot11WIPSAckStaCtsFld,
       "hh3cDot11WIPSAckStaDeauthFld": hh3cDot11WIPSAckStaDeauthFld,
       "hh3cDot11WIPSAckStaDisassFld": hh3cDot11WIPSAckStaDisassFld,
       "hh3cDot11WIPSAckStaEpolSatFld": hh3cDot11WIPSAckStaEpolSatFld,
       "hh3cDot11WIPSAckStaNullDataFld": hh3cDot11WIPSAckStaNullDataFld,
       "hh3cDot11WIPSAckStaProReqFld": hh3cDot11WIPSAckStaProReqFld,
       "hh3cDot11WIPSAckStaReassFld": hh3cDot11WIPSAckStaReassFld,
       "hh3cDot11WIPSAckStaRtsFld": hh3cDot11WIPSAckStaRtsFld,
       "hh3cDot11WIPSAckStaEapLgoffFld": hh3cDot11WIPSAckStaEapLgoffFld,
       "hh3cDot11WIPSAckStaEapFailFld": hh3cDot11WIPSAckStaEapFailFld,
       "hh3cDot11WIPSAckStaEapSucFld": hh3cDot11WIPSAckStaEapSucFld,
       "hh3cDot11WIPSAckStaDupIeMalf": hh3cDot11WIPSAckStaDupIeMalf,
       "hh3cDot11WIPSAckStaFataJackMalf": hh3cDot11WIPSAckStaFataJackMalf,
       "hh3cDot11WIPSAckStaEssMalf": hh3cDot11WIPSAckStaEssMalf,
       "hh3cDot11WIPSAckStaInvComMalf": hh3cDot11WIPSAckStaInvComMalf,
       "hh3cDot11WIPSAckStaInvAssReqMalf": hh3cDot11WIPSAckStaInvAssReqMalf,
       "hh3cDot11WIPSAckStaInvAuthMalf": hh3cDot11WIPSAckStaInvAuthMalf,
       "hh3cDot11WIPSAckStaInvDeauthMalf": hh3cDot11WIPSAckStaInvDeauthMalf,
       "hh3cDot11WIPSAckStaInvDisMalf": hh3cDot11WIPSAckStaInvDisMalf,
       "hh3cDot11WIPSAckStaInvHtIeMalf": hh3cDot11WIPSAckStaInvHtIeMalf,
       "hh3cDot11WIPSAckStaInvIeLenMalf": hh3cDot11WIPSAckStaInvIeLenMalf,
       "hh3cDot11WIPSAckStaInvPktLthMalf": hh3cDot11WIPSAckStaInvPktLthMalf,
       "hh3cDot11WIPSAckStaLgeDutMalf": hh3cDot11WIPSAckStaLgeDutMalf,
       "hh3cDot11WIPSAckStaNProRespMalf": hh3cDot11WIPSAckStaNProRespMalf,
       "hh3cDot11WIPSAckStaOverflEapMalf": hh3cDot11WIPSAckStaOverflEapMalf,
       "hh3cDot11WIPSAckStaOverfSsidMalf": hh3cDot11WIPSAckStaOverfSsidMalf,
       "hh3cDot11WIPSAckStaRedundIeMalf": hh3cDot11WIPSAckStaRedundIeMalf,
       "hh3cDot11WIPSAckStaApSpoofAp": hh3cDot11WIPSAckStaApSpoofAp,
       "hh3cDot11WIPSAckStaApSpoofclt": hh3cDot11WIPSAckStaApSpoofclt,
       "hh3cDot11WIPSAckStaApSpoofAdhoc": hh3cDot11WIPSAckStaApSpoofAdhoc,
       "hh3cDot11WIPSAckStaAdhocSpoofAp": hh3cDot11WIPSAckStaAdhocSpoofAp,
       "hh3cDot11WIPSAckStacltSpoofAp": hh3cDot11WIPSAckStacltSpoofAp,
       "hh3cDot11WIPSAckStaWeakIv": hh3cDot11WIPSAckStaWeakIv,
       "hh3cDot11WIPSAckStaApRate": hh3cDot11WIPSAckStaApRate,
       "hh3cDot11WIPSAckStacltRate": hh3cDot11WIPSAckStacltRate,
       "hh3cDot11WIPSAckStaSignatureRule": hh3cDot11WIPSAckStaSignatureRule,
       "hh3cDot11WIPSAckSta40Mhz": hh3cDot11WIPSAckSta40Mhz,
       "hh3cDot11WIPSAckStaPowerSave": hh3cDot11WIPSAckStaPowerSave,
       "hh3cDot11WIPSAckStaWinBdg": hh3cDot11WIPSAckStaWinBdg,
       "hh3cDot11WIPSAckStaOmerta": hh3cDot11WIPSAckStaOmerta,
       "hh3cDot11WIPSAckStaSoftAp": hh3cDot11WIPSAckStaSoftAp,
       "hh3cDot11WIPSAckStaBroadDis": hh3cDot11WIPSAckStaBroadDis,
       "hh3cDot11WIPSAckStaBroadDeauth": hh3cDot11WIPSAckStaBroadDeauth,
       "hh3cDot11WIPSAckStaApImp": hh3cDot11WIPSAckStaApImp,
       "hh3cDot11WIPSAckStaHtGreenField": hh3cDot11WIPSAckStaHtGreenField,
       "hh3cDot11WIPSAckStaWireBdg": hh3cDot11WIPSAckStaWireBdg,
       "hh3cDot11WIPSAckStaApFld": hh3cDot11WIPSAckStaApFld,
       "hh3cDot11WIPSAckStaAssociaOverf": hh3cDot11WIPSAckStaAssociaOverf}
)
