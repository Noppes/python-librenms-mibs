# SNMP MIB module (HH3C-WAPI-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\comware\HH3C-WAPI-MIB

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

(ifDescr,
 ifIndex) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifDescr",
    "ifIndex")

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

hh3cwapiMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 77)
)
if mibBuilder.loadTexts:
    hh3cwapiMIB.setRevisions(
        ("2010-12-01 17:57",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Hh3cwapiMIBObjects_ObjectIdentity = ObjectIdentity
hh3cwapiMIBObjects = _Hh3cwapiMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 77, 1)
)
_Hh3cwapiModeEnabled_Type = TruthValue
_Hh3cwapiModeEnabled_Object = MibScalar
hh3cwapiModeEnabled = _Hh3cwapiModeEnabled_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 77, 1, 1),
    _Hh3cwapiModeEnabled_Type()
)
hh3cwapiModeEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cwapiModeEnabled.setStatus("current")


class _Hh3cwapiASIPAddressType_Type(InetAddressType):
    """Custom type hh3cwapiASIPAddressType based on InetAddressType"""
    defaultValue = 1


_Hh3cwapiASIPAddressType_Type.__name__ = "InetAddressType"
_Hh3cwapiASIPAddressType_Object = MibScalar
hh3cwapiASIPAddressType = _Hh3cwapiASIPAddressType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 77, 1, 2),
    _Hh3cwapiASIPAddressType_Type()
)
hh3cwapiASIPAddressType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cwapiASIPAddressType.setStatus("current")
_Hh3cwapiASIPAddress_Type = InetAddress
_Hh3cwapiASIPAddress_Object = MibScalar
hh3cwapiASIPAddress = _Hh3cwapiASIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 77, 1, 3),
    _Hh3cwapiASIPAddress_Type()
)
hh3cwapiASIPAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cwapiASIPAddress.setStatus("current")
_Hh3cwapiCertificateInstalled_Type = TruthValue
_Hh3cwapiCertificateInstalled_Object = MibScalar
hh3cwapiCertificateInstalled = _Hh3cwapiCertificateInstalled_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 77, 1, 4),
    _Hh3cwapiCertificateInstalled_Type()
)
hh3cwapiCertificateInstalled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cwapiCertificateInstalled.setStatus("current")
_Hh3cwapiMIBStatsObjects_ObjectIdentity = ObjectIdentity
hh3cwapiMIBStatsObjects = _Hh3cwapiMIBStatsObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 77, 2)
)
_Hh3cwapiStatsWAISignatureErrors_Type = Counter32
_Hh3cwapiStatsWAISignatureErrors_Object = MibScalar
hh3cwapiStatsWAISignatureErrors = _Hh3cwapiStatsWAISignatureErrors_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 77, 2, 1),
    _Hh3cwapiStatsWAISignatureErrors_Type()
)
hh3cwapiStatsWAISignatureErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cwapiStatsWAISignatureErrors.setStatus("current")
_Hh3cwapiStatsWAIHMACErrors_Type = Counter32
_Hh3cwapiStatsWAIHMACErrors_Object = MibScalar
hh3cwapiStatsWAIHMACErrors = _Hh3cwapiStatsWAIHMACErrors_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 77, 2, 2),
    _Hh3cwapiStatsWAIHMACErrors_Type()
)
hh3cwapiStatsWAIHMACErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cwapiStatsWAIHMACErrors.setStatus("current")
_Hh3cwapiStatsWAIAuthRsltFailures_Type = Counter32
_Hh3cwapiStatsWAIAuthRsltFailures_Object = MibScalar
hh3cwapiStatsWAIAuthRsltFailures = _Hh3cwapiStatsWAIAuthRsltFailures_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 77, 2, 3),
    _Hh3cwapiStatsWAIAuthRsltFailures_Type()
)
hh3cwapiStatsWAIAuthRsltFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cwapiStatsWAIAuthRsltFailures.setStatus("current")
_Hh3cwapiStatsWAIDiscardCounters_Type = Counter32
_Hh3cwapiStatsWAIDiscardCounters_Object = MibScalar
hh3cwapiStatsWAIDiscardCounters = _Hh3cwapiStatsWAIDiscardCounters_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 77, 2, 4),
    _Hh3cwapiStatsWAIDiscardCounters_Type()
)
hh3cwapiStatsWAIDiscardCounters.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cwapiStatsWAIDiscardCounters.setStatus("current")
_Hh3cwapiStatsWAITimeoutCounters_Type = Counter32
_Hh3cwapiStatsWAITimeoutCounters_Object = MibScalar
hh3cwapiStatsWAITimeoutCounters = _Hh3cwapiStatsWAITimeoutCounters_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 77, 2, 5),
    _Hh3cwapiStatsWAITimeoutCounters_Type()
)
hh3cwapiStatsWAITimeoutCounters.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cwapiStatsWAITimeoutCounters.setStatus("current")
_Hh3cwapiStatsWAIFormatErrors_Type = Counter32
_Hh3cwapiStatsWAIFormatErrors_Object = MibScalar
hh3cwapiStatsWAIFormatErrors = _Hh3cwapiStatsWAIFormatErrors_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 77, 2, 6),
    _Hh3cwapiStatsWAIFormatErrors_Type()
)
hh3cwapiStatsWAIFormatErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cwapiStatsWAIFormatErrors.setStatus("current")
_Hh3cwapiStatsWAICtfHskFailures_Type = Counter32
_Hh3cwapiStatsWAICtfHskFailures_Object = MibScalar
hh3cwapiStatsWAICtfHskFailures = _Hh3cwapiStatsWAICtfHskFailures_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 77, 2, 7),
    _Hh3cwapiStatsWAICtfHskFailures_Type()
)
hh3cwapiStatsWAICtfHskFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cwapiStatsWAICtfHskFailures.setStatus("current")
_Hh3cwapiStatsWAIUniHskFailures_Type = Counter32
_Hh3cwapiStatsWAIUniHskFailures_Object = MibScalar
hh3cwapiStatsWAIUniHskFailures = _Hh3cwapiStatsWAIUniHskFailures_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 77, 2, 8),
    _Hh3cwapiStatsWAIUniHskFailures_Type()
)
hh3cwapiStatsWAIUniHskFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cwapiStatsWAIUniHskFailures.setStatus("current")
_Hh3cwapiStatsWAIMulHskFailures_Type = Counter32
_Hh3cwapiStatsWAIMulHskFailures_Object = MibScalar
hh3cwapiStatsWAIMulHskFailures = _Hh3cwapiStatsWAIMulHskFailures_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 77, 2, 9),
    _Hh3cwapiStatsWAIMulHskFailures_Type()
)
hh3cwapiStatsWAIMulHskFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cwapiStatsWAIMulHskFailures.setStatus("current")
_Hh3cwapiMIBTableObjects_ObjectIdentity = ObjectIdentity
hh3cwapiMIBTableObjects = _Hh3cwapiMIBTableObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 77, 3)
)
_Hh3cwapiConfigTable_Object = MibTable
hh3cwapiConfigTable = _Hh3cwapiConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 77, 3, 1)
)
if mibBuilder.loadTexts:
    hh3cwapiConfigTable.setStatus("current")
_Hh3cwapiConfigEntry_Object = MibTableRow
hh3cwapiConfigEntry = _Hh3cwapiConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 77, 3, 1, 1)
)
hh3cwapiConfigEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    hh3cwapiConfigEntry.setStatus("current")
_Hh3cwapiConfigASIPAddressType_Type = InetAddressType
_Hh3cwapiConfigASIPAddressType_Object = MibTableColumn
hh3cwapiConfigASIPAddressType = _Hh3cwapiConfigASIPAddressType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 77, 3, 1, 1, 1),
    _Hh3cwapiConfigASIPAddressType_Type()
)
hh3cwapiConfigASIPAddressType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cwapiConfigASIPAddressType.setStatus("current")
_Hh3cwapiConfigASIPAddress_Type = InetAddress
_Hh3cwapiConfigASIPAddress_Object = MibTableColumn
hh3cwapiConfigASIPAddress = _Hh3cwapiConfigASIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 77, 3, 1, 1, 2),
    _Hh3cwapiConfigASIPAddress_Type()
)
hh3cwapiConfigASIPAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cwapiConfigASIPAddress.setStatus("current")


class _Hh3cwapiConfigAuthMethod_Type(Integer32):
    """Custom type hh3cwapiConfigAuthMethod based on Integer32"""
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
          ("psk", 2),
          ("certificatePsk", 3))
    )


_Hh3cwapiConfigAuthMethod_Type.__name__ = "Integer32"
_Hh3cwapiConfigAuthMethod_Object = MibTableColumn
hh3cwapiConfigAuthMethod = _Hh3cwapiConfigAuthMethod_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 77, 3, 1, 1, 3),
    _Hh3cwapiConfigAuthMethod_Type()
)
hh3cwapiConfigAuthMethod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cwapiConfigAuthMethod.setStatus("current")


class _Hh3cwapiConfigAuthMode_Type(Integer32):
    """Custom type hh3cwapiConfigAuthMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("standard", 1),
          ("radiusExtension", 2))
    )


_Hh3cwapiConfigAuthMode_Type.__name__ = "Integer32"
_Hh3cwapiConfigAuthMode_Object = MibTableColumn
hh3cwapiConfigAuthMode = _Hh3cwapiConfigAuthMode_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 77, 3, 1, 1, 4),
    _Hh3cwapiConfigAuthMode_Type()
)
hh3cwapiConfigAuthMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cwapiConfigAuthMode.setStatus("current")


class _Hh3cwapiConfigISPDomain_Type(OctetString):
    """Custom type hh3cwapiConfigISPDomain based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 24),
    )


_Hh3cwapiConfigISPDomain_Type.__name__ = "OctetString"
_Hh3cwapiConfigISPDomain_Object = MibTableColumn
hh3cwapiConfigISPDomain = _Hh3cwapiConfigISPDomain_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 77, 3, 1, 1, 5),
    _Hh3cwapiConfigISPDomain_Type()
)
hh3cwapiConfigISPDomain.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cwapiConfigISPDomain.setStatus("current")


class _Hh3cwapiConfigCertificateDomain_Type(OctetString):
    """Custom type hh3cwapiConfigCertificateDomain based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 15),
    )


_Hh3cwapiConfigCertificateDomain_Type.__name__ = "OctetString"
_Hh3cwapiConfigCertificateDomain_Object = MibTableColumn
hh3cwapiConfigCertificateDomain = _Hh3cwapiConfigCertificateDomain_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 77, 3, 1, 1, 6),
    _Hh3cwapiConfigCertificateDomain_Type()
)
hh3cwapiConfigCertificateDomain.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cwapiConfigCertificateDomain.setStatus("current")


class _Hh3cwapiConfigASName_Type(OctetString):
    """Custom type hh3cwapiConfigASName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 15),
    )


_Hh3cwapiConfigASName_Type.__name__ = "OctetString"
_Hh3cwapiConfigASName_Object = MibTableColumn
hh3cwapiConfigASName = _Hh3cwapiConfigASName_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 77, 3, 1, 1, 7),
    _Hh3cwapiConfigASName_Type()
)
hh3cwapiConfigASName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cwapiConfigASName.setStatus("current")
_Hh3cwapiConfigBKRekeyEnabled_Type = TruthValue
_Hh3cwapiConfigBKRekeyEnabled_Object = MibTableColumn
hh3cwapiConfigBKRekeyEnabled = _Hh3cwapiConfigBKRekeyEnabled_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 77, 3, 1, 1, 8),
    _Hh3cwapiConfigBKRekeyEnabled_Type()
)
hh3cwapiConfigBKRekeyEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cwapiConfigBKRekeyEnabled.setStatus("current")
_Hh3cwapiConfigExtTable_Object = MibTable
hh3cwapiConfigExtTable = _Hh3cwapiConfigExtTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 77, 3, 2)
)
if mibBuilder.loadTexts:
    hh3cwapiConfigExtTable.setStatus("current")
_Hh3cwapiConfigExtEntry_Object = MibTableRow
hh3cwapiConfigExtEntry = _Hh3cwapiConfigExtEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 77, 3, 2, 1)
)
hh3cwapiConfigExtEntry.setIndexNames(
    (0, "HH3C-WAPI-MIB", "hh3cwapiConfigServicePolicyID"),
)
if mibBuilder.loadTexts:
    hh3cwapiConfigExtEntry.setStatus("current")
_Hh3cwapiConfigServicePolicyID_Type = Integer32
_Hh3cwapiConfigServicePolicyID_Object = MibTableColumn
hh3cwapiConfigServicePolicyID = _Hh3cwapiConfigServicePolicyID_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 77, 3, 2, 1, 1),
    _Hh3cwapiConfigServicePolicyID_Type()
)
hh3cwapiConfigServicePolicyID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cwapiConfigServicePolicyID.setStatus("current")
_Hh3cwapiConfigUnicastCipherEnabled_Type = TruthValue
_Hh3cwapiConfigUnicastCipherEnabled_Object = MibTableColumn
hh3cwapiConfigUnicastCipherEnabled = _Hh3cwapiConfigUnicastCipherEnabled_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 77, 3, 2, 1, 2),
    _Hh3cwapiConfigUnicastCipherEnabled_Type()
)
hh3cwapiConfigUnicastCipherEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cwapiConfigUnicastCipherEnabled.setStatus("current")


class _Hh3cwapiConfigUnicastCipherSize_Type(Unsigned32):
    """Custom type hh3cwapiConfigUnicastCipherSize based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_Hh3cwapiConfigUnicastCipherSize_Type.__name__ = "Unsigned32"
_Hh3cwapiConfigUnicastCipherSize_Object = MibTableColumn
hh3cwapiConfigUnicastCipherSize = _Hh3cwapiConfigUnicastCipherSize_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 77, 3, 2, 1, 3),
    _Hh3cwapiConfigUnicastCipherSize_Type()
)
hh3cwapiConfigUnicastCipherSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cwapiConfigUnicastCipherSize.setStatus("current")
_Hh3cwapiConfigAuthenticationSuiteEnabled_Type = TruthValue
_Hh3cwapiConfigAuthenticationSuiteEnabled_Object = MibTableColumn
hh3cwapiConfigAuthenticationSuiteEnabled = _Hh3cwapiConfigAuthenticationSuiteEnabled_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 77, 3, 2, 1, 4),
    _Hh3cwapiConfigAuthenticationSuiteEnabled_Type()
)
hh3cwapiConfigAuthenticationSuiteEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cwapiConfigAuthenticationSuiteEnabled.setStatus("current")


class _Hh3cwapiConfigAuthenticationSuite_Type(OctetString):
    """Custom type hh3cwapiConfigAuthenticationSuite based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )
    fixed_length = 4


_Hh3cwapiConfigAuthenticationSuite_Type.__name__ = "OctetString"
_Hh3cwapiConfigAuthenticationSuite_Object = MibTableColumn
hh3cwapiConfigAuthenticationSuite = _Hh3cwapiConfigAuthenticationSuite_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 77, 3, 2, 1, 5),
    _Hh3cwapiConfigAuthenticationSuite_Type()
)
hh3cwapiConfigAuthenticationSuite.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cwapiConfigAuthenticationSuite.setStatus("current")
_Hh3cwapiCfgExtASIPAddressType_Type = InetAddressType
_Hh3cwapiCfgExtASIPAddressType_Object = MibTableColumn
hh3cwapiCfgExtASIPAddressType = _Hh3cwapiCfgExtASIPAddressType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 77, 3, 2, 1, 6),
    _Hh3cwapiCfgExtASIPAddressType_Type()
)
hh3cwapiCfgExtASIPAddressType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cwapiCfgExtASIPAddressType.setStatus("current")
_Hh3cwapiCfgExtASIPAddress_Type = InetAddress
_Hh3cwapiCfgExtASIPAddress_Object = MibTableColumn
hh3cwapiCfgExtASIPAddress = _Hh3cwapiCfgExtASIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 77, 3, 2, 1, 7),
    _Hh3cwapiCfgExtASIPAddress_Type()
)
hh3cwapiCfgExtASIPAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cwapiCfgExtASIPAddress.setStatus("current")


class _Hh3cwapiCfgExtASName_Type(OctetString):
    """Custom type hh3cwapiCfgExtASName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 15),
    )


_Hh3cwapiCfgExtASName_Type.__name__ = "OctetString"
_Hh3cwapiCfgExtASName_Object = MibTableColumn
hh3cwapiCfgExtASName = _Hh3cwapiCfgExtASName_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 77, 3, 2, 1, 8),
    _Hh3cwapiCfgExtASName_Type()
)
hh3cwapiCfgExtASName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cwapiCfgExtASName.setStatus("current")


class _Hh3cwapiCfgExtCertDomain_Type(OctetString):
    """Custom type hh3cwapiCfgExtCertDomain based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 15),
    )


_Hh3cwapiCfgExtCertDomain_Type.__name__ = "OctetString"
_Hh3cwapiCfgExtCertDomain_Object = MibTableColumn
hh3cwapiCfgExtCertDomain = _Hh3cwapiCfgExtCertDomain_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 77, 3, 2, 1, 9),
    _Hh3cwapiCfgExtCertDomain_Type()
)
hh3cwapiCfgExtCertDomain.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cwapiCfgExtCertDomain.setStatus("current")
_Hh3cwapiCfgExtCertInstalled_Type = TruthValue
_Hh3cwapiCfgExtCertInstalled_Object = MibTableColumn
hh3cwapiCfgExtCertInstalled = _Hh3cwapiCfgExtCertInstalled_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 77, 3, 2, 1, 10),
    _Hh3cwapiCfgExtCertInstalled_Type()
)
hh3cwapiCfgExtCertInstalled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cwapiCfgExtCertInstalled.setStatus("current")
_Hh3cwapiConfigVersion_Type = Integer32
_Hh3cwapiConfigVersion_Object = MibTableColumn
hh3cwapiConfigVersion = _Hh3cwapiConfigVersion_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 77, 3, 2, 1, 11),
    _Hh3cwapiConfigVersion_Type()
)
hh3cwapiConfigVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cwapiConfigVersion.setStatus("current")
_Hh3cwapiControlledAuthControl_Type = TruthValue
_Hh3cwapiControlledAuthControl_Object = MibTableColumn
hh3cwapiControlledAuthControl = _Hh3cwapiControlledAuthControl_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 77, 3, 2, 1, 12),
    _Hh3cwapiControlledAuthControl_Type()
)
hh3cwapiControlledAuthControl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cwapiControlledAuthControl.setStatus("current")
_Hh3cwapiControlledPortControl_Type = Integer32
_Hh3cwapiControlledPortControl_Object = MibTableColumn
hh3cwapiControlledPortControl = _Hh3cwapiControlledPortControl_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 77, 3, 2, 1, 13),
    _Hh3cwapiControlledPortControl_Type()
)
hh3cwapiControlledPortControl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cwapiControlledPortControl.setStatus("current")
_Hh3cwapiOptionImplemented_Type = TruthValue
_Hh3cwapiOptionImplemented_Object = MibTableColumn
hh3cwapiOptionImplemented = _Hh3cwapiOptionImplemented_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 77, 3, 2, 1, 14),
    _Hh3cwapiOptionImplemented_Type()
)
hh3cwapiOptionImplemented.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cwapiOptionImplemented.setStatus("current")
_Hh3cwapiPreauthImplemented_Type = TruthValue
_Hh3cwapiPreauthImplemented_Object = MibTableColumn
hh3cwapiPreauthImplemented = _Hh3cwapiPreauthImplemented_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 77, 3, 2, 1, 15),
    _Hh3cwapiPreauthImplemented_Type()
)
hh3cwapiPreauthImplemented.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cwapiPreauthImplemented.setStatus("current")
_Hh3cwapiEnabled_Type = TruthValue
_Hh3cwapiEnabled_Object = MibTableColumn
hh3cwapiEnabled = _Hh3cwapiEnabled_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 77, 3, 2, 1, 16),
    _Hh3cwapiEnabled_Type()
)
hh3cwapiEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cwapiEnabled.setStatus("current")
_Hh3cwapiPreauthEnabled_Type = TruthValue
_Hh3cwapiPreauthEnabled_Object = MibTableColumn
hh3cwapiPreauthEnabled = _Hh3cwapiPreauthEnabled_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 77, 3, 2, 1, 17),
    _Hh3cwapiPreauthEnabled_Type()
)
hh3cwapiPreauthEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cwapiPreauthEnabled.setStatus("current")
_Hh3cwapiCfgUniKeysSupported_Type = Unsigned32
_Hh3cwapiCfgUniKeysSupported_Object = MibTableColumn
hh3cwapiCfgUniKeysSupported = _Hh3cwapiCfgUniKeysSupported_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 77, 3, 2, 1, 18),
    _Hh3cwapiCfgUniKeysSupported_Type()
)
hh3cwapiCfgUniKeysSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cwapiCfgUniKeysSupported.setStatus("current")


class _Hh3cwapiCfgUniRekeyMethod_Type(Integer32):
    """Custom type hh3cwapiCfgUniRekeyMethod based on Integer32"""
    defaultValue = 2

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
        *(("disabled", 1),
          ("timeBased", 2),
          ("packetBased", 3),
          ("timepacketBased", 4))
    )


_Hh3cwapiCfgUniRekeyMethod_Type.__name__ = "Integer32"
_Hh3cwapiCfgUniRekeyMethod_Object = MibTableColumn
hh3cwapiCfgUniRekeyMethod = _Hh3cwapiCfgUniRekeyMethod_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 77, 3, 2, 1, 19),
    _Hh3cwapiCfgUniRekeyMethod_Type()
)
hh3cwapiCfgUniRekeyMethod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cwapiCfgUniRekeyMethod.setStatus("current")


class _Hh3cwapiCfgUniRekeyTime_Type(Unsigned32):
    """Custom type hh3cwapiCfgUniRekeyTime based on Unsigned32"""
    defaultValue = 86400

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_Hh3cwapiCfgUniRekeyTime_Type.__name__ = "Unsigned32"
_Hh3cwapiCfgUniRekeyTime_Object = MibTableColumn
hh3cwapiCfgUniRekeyTime = _Hh3cwapiCfgUniRekeyTime_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 77, 3, 2, 1, 20),
    _Hh3cwapiCfgUniRekeyTime_Type()
)
hh3cwapiCfgUniRekeyTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cwapiCfgUniRekeyTime.setStatus("current")
if mibBuilder.loadTexts:
    hh3cwapiCfgUniRekeyTime.setUnits("seconds")


class _Hh3cwapiCfgUniRekeyPackets_Type(Unsigned32):
    """Custom type hh3cwapiCfgUniRekeyPackets based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_Hh3cwapiCfgUniRekeyPackets_Type.__name__ = "Unsigned32"
_Hh3cwapiCfgUniRekeyPackets_Object = MibTableColumn
hh3cwapiCfgUniRekeyPackets = _Hh3cwapiCfgUniRekeyPackets_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 77, 3, 2, 1, 21),
    _Hh3cwapiCfgUniRekeyPackets_Type()
)
hh3cwapiCfgUniRekeyPackets.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cwapiCfgUniRekeyPackets.setStatus("current")
if mibBuilder.loadTexts:
    hh3cwapiCfgUniRekeyPackets.setUnits("1000 packets")


class _Hh3cwapiCfgMultiCipher_Type(OctetString):
    """Custom type hh3cwapiCfgMultiCipher based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )
    fixed_length = 4


_Hh3cwapiCfgMultiCipher_Type.__name__ = "OctetString"
_Hh3cwapiCfgMultiCipher_Object = MibTableColumn
hh3cwapiCfgMultiCipher = _Hh3cwapiCfgMultiCipher_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 77, 3, 2, 1, 22),
    _Hh3cwapiCfgMultiCipher_Type()
)
hh3cwapiCfgMultiCipher.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cwapiCfgMultiCipher.setStatus("current")


class _Hh3cwapiCfgMultiRekeyMethod_Type(Integer32):
    """Custom type hh3cwapiCfgMultiRekeyMethod based on Integer32"""
    defaultValue = 2

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
        *(("disabled", 1),
          ("timeBased", 2),
          ("packetBased", 3),
          ("timepacketBased", 4))
    )


_Hh3cwapiCfgMultiRekeyMethod_Type.__name__ = "Integer32"
_Hh3cwapiCfgMultiRekeyMethod_Object = MibTableColumn
hh3cwapiCfgMultiRekeyMethod = _Hh3cwapiCfgMultiRekeyMethod_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 77, 3, 2, 1, 23),
    _Hh3cwapiCfgMultiRekeyMethod_Type()
)
hh3cwapiCfgMultiRekeyMethod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cwapiCfgMultiRekeyMethod.setStatus("current")


class _Hh3cwapiCfgMultiRekeyTime_Type(Unsigned32):
    """Custom type hh3cwapiCfgMultiRekeyTime based on Unsigned32"""
    defaultValue = 86400

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_Hh3cwapiCfgMultiRekeyTime_Type.__name__ = "Unsigned32"
_Hh3cwapiCfgMultiRekeyTime_Object = MibTableColumn
hh3cwapiCfgMultiRekeyTime = _Hh3cwapiCfgMultiRekeyTime_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 77, 3, 2, 1, 24),
    _Hh3cwapiCfgMultiRekeyTime_Type()
)
hh3cwapiCfgMultiRekeyTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cwapiCfgMultiRekeyTime.setStatus("current")
if mibBuilder.loadTexts:
    hh3cwapiCfgMultiRekeyTime.setUnits("seconds")


class _Hh3cwapiCfgMultiRekeyPackets_Type(Unsigned32):
    """Custom type hh3cwapiCfgMultiRekeyPackets based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_Hh3cwapiCfgMultiRekeyPackets_Type.__name__ = "Unsigned32"
_Hh3cwapiCfgMultiRekeyPackets_Object = MibTableColumn
hh3cwapiCfgMultiRekeyPackets = _Hh3cwapiCfgMultiRekeyPackets_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 77, 3, 2, 1, 25),
    _Hh3cwapiCfgMultiRekeyPackets_Type()
)
hh3cwapiCfgMultiRekeyPackets.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cwapiCfgMultiRekeyPackets.setStatus("current")
if mibBuilder.loadTexts:
    hh3cwapiCfgMultiRekeyPackets.setUnits("1000 packets")
_Hh3cwapiCfgMultiRekeyStrict_Type = TruthValue
_Hh3cwapiCfgMultiRekeyStrict_Object = MibTableColumn
hh3cwapiCfgMultiRekeyStrict = _Hh3cwapiCfgMultiRekeyStrict_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 77, 3, 2, 1, 26),
    _Hh3cwapiCfgMultiRekeyStrict_Type()
)
hh3cwapiCfgMultiRekeyStrict.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cwapiCfgMultiRekeyStrict.setStatus("current")


class _Hh3cwapiCfgPSKValue_Type(OctetString):
    """Custom type hh3cwapiCfgPSKValue based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 32),
    )


_Hh3cwapiCfgPSKValue_Type.__name__ = "OctetString"
_Hh3cwapiCfgPSKValue_Object = MibTableColumn
hh3cwapiCfgPSKValue = _Hh3cwapiCfgPSKValue_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 77, 3, 2, 1, 27),
    _Hh3cwapiCfgPSKValue_Type()
)
hh3cwapiCfgPSKValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cwapiCfgPSKValue.setStatus("current")


class _Hh3cwapiCfgPSKPassPhrase_Type(OctetString):
    """Custom type hh3cwapiCfgPSKPassPhrase based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_Hh3cwapiCfgPSKPassPhrase_Type.__name__ = "OctetString"
_Hh3cwapiCfgPSKPassPhrase_Object = MibTableColumn
hh3cwapiCfgPSKPassPhrase = _Hh3cwapiCfgPSKPassPhrase_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 77, 3, 2, 1, 28),
    _Hh3cwapiCfgPSKPassPhrase_Type()
)
hh3cwapiCfgPSKPassPhrase.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cwapiCfgPSKPassPhrase.setStatus("current")


class _Hh3cwapiCfgCertUpdateCount_Type(Unsigned32):
    """Custom type hh3cwapiCfgCertUpdateCount based on Unsigned32"""
    defaultValue = 3

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_Hh3cwapiCfgCertUpdateCount_Type.__name__ = "Unsigned32"
_Hh3cwapiCfgCertUpdateCount_Object = MibTableColumn
hh3cwapiCfgCertUpdateCount = _Hh3cwapiCfgCertUpdateCount_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 77, 3, 2, 1, 29),
    _Hh3cwapiCfgCertUpdateCount_Type()
)
hh3cwapiCfgCertUpdateCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cwapiCfgCertUpdateCount.setStatus("current")


class _Hh3cwapiCfgMultiUpdateCount_Type(Unsigned32):
    """Custom type hh3cwapiCfgMultiUpdateCount based on Unsigned32"""
    defaultValue = 3

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_Hh3cwapiCfgMultiUpdateCount_Type.__name__ = "Unsigned32"
_Hh3cwapiCfgMultiUpdateCount_Object = MibTableColumn
hh3cwapiCfgMultiUpdateCount = _Hh3cwapiCfgMultiUpdateCount_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 77, 3, 2, 1, 30),
    _Hh3cwapiCfgMultiUpdateCount_Type()
)
hh3cwapiCfgMultiUpdateCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cwapiCfgMultiUpdateCount.setStatus("current")


class _Hh3cwapiCfgUniUpdateCount_Type(Unsigned32):
    """Custom type hh3cwapiCfgUniUpdateCount based on Unsigned32"""
    defaultValue = 3

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_Hh3cwapiCfgUniUpdateCount_Type.__name__ = "Unsigned32"
_Hh3cwapiCfgUniUpdateCount_Object = MibTableColumn
hh3cwapiCfgUniUpdateCount = _Hh3cwapiCfgUniUpdateCount_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 77, 3, 2, 1, 31),
    _Hh3cwapiCfgUniUpdateCount_Type()
)
hh3cwapiCfgUniUpdateCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cwapiCfgUniUpdateCount.setStatus("current")


class _Hh3cwapiCfgMultiCipherSize_Type(Unsigned32):
    """Custom type hh3cwapiCfgMultiCipherSize based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_Hh3cwapiCfgMultiCipherSize_Type.__name__ = "Unsigned32"
_Hh3cwapiCfgMultiCipherSize_Object = MibTableColumn
hh3cwapiCfgMultiCipherSize = _Hh3cwapiCfgMultiCipherSize_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 77, 3, 2, 1, 32),
    _Hh3cwapiCfgMultiCipherSize_Type()
)
hh3cwapiCfgMultiCipherSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cwapiCfgMultiCipherSize.setStatus("current")


class _Hh3cwapiCfgBKLifetime_Type(Unsigned32):
    """Custom type hh3cwapiCfgBKLifetime based on Unsigned32"""
    defaultValue = 43200

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_Hh3cwapiCfgBKLifetime_Type.__name__ = "Unsigned32"
_Hh3cwapiCfgBKLifetime_Object = MibTableColumn
hh3cwapiCfgBKLifetime = _Hh3cwapiCfgBKLifetime_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 77, 3, 2, 1, 33),
    _Hh3cwapiCfgBKLifetime_Type()
)
hh3cwapiCfgBKLifetime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cwapiCfgBKLifetime.setStatus("current")
if mibBuilder.loadTexts:
    hh3cwapiCfgBKLifetime.setUnits("seconds")


class _Hh3cwapiCfgBKReauthThreshold_Type(Unsigned32):
    """Custom type hh3cwapiCfgBKReauthThreshold based on Unsigned32"""
    defaultValue = 70

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_Hh3cwapiCfgBKReauthThreshold_Type.__name__ = "Unsigned32"
_Hh3cwapiCfgBKReauthThreshold_Object = MibTableColumn
hh3cwapiCfgBKReauthThreshold = _Hh3cwapiCfgBKReauthThreshold_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 77, 3, 2, 1, 34),
    _Hh3cwapiCfgBKReauthThreshold_Type()
)
hh3cwapiCfgBKReauthThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cwapiCfgBKReauthThreshold.setStatus("current")
if mibBuilder.loadTexts:
    hh3cwapiCfgBKReauthThreshold.setUnits("percentage")


class _Hh3cwapiCfgSATimeout_Type(Unsigned32):
    """Custom type hh3cwapiCfgSATimeout based on Unsigned32"""
    defaultValue = 60

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_Hh3cwapiCfgSATimeout_Type.__name__ = "Unsigned32"
_Hh3cwapiCfgSATimeout_Object = MibTableColumn
hh3cwapiCfgSATimeout = _Hh3cwapiCfgSATimeout_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 77, 3, 2, 1, 35),
    _Hh3cwapiCfgSATimeout_Type()
)
hh3cwapiCfgSATimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cwapiCfgSATimeout.setStatus("current")
if mibBuilder.loadTexts:
    hh3cwapiCfgSATimeout.setUnits("seconds")


class _Hh3cwapiAuthenSuiteSelected_Type(OctetString):
    """Custom type hh3cwapiAuthenSuiteSelected based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )
    fixed_length = 4


_Hh3cwapiAuthenSuiteSelected_Type.__name__ = "OctetString"
_Hh3cwapiAuthenSuiteSelected_Object = MibTableColumn
hh3cwapiAuthenSuiteSelected = _Hh3cwapiAuthenSuiteSelected_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 77, 3, 2, 1, 36),
    _Hh3cwapiAuthenSuiteSelected_Type()
)
hh3cwapiAuthenSuiteSelected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cwapiAuthenSuiteSelected.setStatus("current")


class _Hh3cwapiUniCipherSelected_Type(OctetString):
    """Custom type hh3cwapiUniCipherSelected based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )
    fixed_length = 4


_Hh3cwapiUniCipherSelected_Type.__name__ = "OctetString"
_Hh3cwapiUniCipherSelected_Object = MibTableColumn
hh3cwapiUniCipherSelected = _Hh3cwapiUniCipherSelected_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 77, 3, 2, 1, 37),
    _Hh3cwapiUniCipherSelected_Type()
)
hh3cwapiUniCipherSelected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cwapiUniCipherSelected.setStatus("current")


class _Hh3cwapiMultiCipherSelected_Type(OctetString):
    """Custom type hh3cwapiMultiCipherSelected based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )
    fixed_length = 4


_Hh3cwapiMultiCipherSelected_Type.__name__ = "OctetString"
_Hh3cwapiMultiCipherSelected_Object = MibTableColumn
hh3cwapiMultiCipherSelected = _Hh3cwapiMultiCipherSelected_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 77, 3, 2, 1, 38),
    _Hh3cwapiMultiCipherSelected_Type()
)
hh3cwapiMultiCipherSelected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cwapiMultiCipherSelected.setStatus("current")


class _Hh3cwapiBKIDUsed_Type(OctetString):
    """Custom type hh3cwapiBKIDUsed based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )
    fixed_length = 16


_Hh3cwapiBKIDUsed_Type.__name__ = "OctetString"
_Hh3cwapiBKIDUsed_Object = MibTableColumn
hh3cwapiBKIDUsed = _Hh3cwapiBKIDUsed_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 77, 3, 2, 1, 39),
    _Hh3cwapiBKIDUsed_Type()
)
hh3cwapiBKIDUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cwapiBKIDUsed.setStatus("current")


class _Hh3cwapiAuthenSuiteRequested_Type(OctetString):
    """Custom type hh3cwapiAuthenSuiteRequested based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )
    fixed_length = 4


_Hh3cwapiAuthenSuiteRequested_Type.__name__ = "OctetString"
_Hh3cwapiAuthenSuiteRequested_Object = MibTableColumn
hh3cwapiAuthenSuiteRequested = _Hh3cwapiAuthenSuiteRequested_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 77, 3, 2, 1, 40),
    _Hh3cwapiAuthenSuiteRequested_Type()
)
hh3cwapiAuthenSuiteRequested.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cwapiAuthenSuiteRequested.setStatus("current")


class _Hh3cwapiUniCipherRequested_Type(OctetString):
    """Custom type hh3cwapiUniCipherRequested based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )
    fixed_length = 4


_Hh3cwapiUniCipherRequested_Type.__name__ = "OctetString"
_Hh3cwapiUniCipherRequested_Object = MibTableColumn
hh3cwapiUniCipherRequested = _Hh3cwapiUniCipherRequested_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 77, 3, 2, 1, 41),
    _Hh3cwapiUniCipherRequested_Type()
)
hh3cwapiUniCipherRequested.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cwapiUniCipherRequested.setStatus("current")


class _Hh3cwapiMultiCipherRequested_Type(OctetString):
    """Custom type hh3cwapiMultiCipherRequested based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )
    fixed_length = 4


_Hh3cwapiMultiCipherRequested_Type.__name__ = "OctetString"
_Hh3cwapiMultiCipherRequested_Object = MibTableColumn
hh3cwapiMultiCipherRequested = _Hh3cwapiMultiCipherRequested_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 77, 3, 2, 1, 42),
    _Hh3cwapiMultiCipherRequested_Type()
)
hh3cwapiMultiCipherRequested.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cwapiMultiCipherRequested.setStatus("current")
_Hh3cwapiStatsTable_Object = MibTable
hh3cwapiStatsTable = _Hh3cwapiStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 77, 3, 3)
)
if mibBuilder.loadTexts:
    hh3cwapiStatsTable.setStatus("current")
_Hh3cwapiStatsEntry_Object = MibTableRow
hh3cwapiStatsEntry = _Hh3cwapiStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 77, 3, 3, 1)
)
hh3cwapiStatsEntry.setIndexNames(
    (0, "HH3C-WAPI-MIB", "hh3cwapiStationMAC"),
)
if mibBuilder.loadTexts:
    hh3cwapiStatsEntry.setStatus("current")
_Hh3cwapiStationMAC_Type = MacAddress
_Hh3cwapiStationMAC_Object = MibTableColumn
hh3cwapiStationMAC = _Hh3cwapiStationMAC_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 77, 3, 3, 1, 1),
    _Hh3cwapiStationMAC_Type()
)
hh3cwapiStationMAC.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cwapiStationMAC.setStatus("current")
_Hh3cwapiStatsSTAAddress_Type = MacAddress
_Hh3cwapiStatsSTAAddress_Object = MibTableColumn
hh3cwapiStatsSTAAddress = _Hh3cwapiStatsSTAAddress_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 77, 3, 3, 1, 2),
    _Hh3cwapiStatsSTAAddress_Type()
)
hh3cwapiStatsSTAAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cwapiStatsSTAAddress.setStatus("current")


class _Hh3cwapiStatsVersion_Type(Unsigned32):
    """Custom type hh3cwapiStatsVersion based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_Hh3cwapiStatsVersion_Type.__name__ = "Unsigned32"
_Hh3cwapiStatsVersion_Object = MibTableColumn
hh3cwapiStatsVersion = _Hh3cwapiStatsVersion_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 77, 3, 3, 1, 3),
    _Hh3cwapiStatsVersion_Type()
)
hh3cwapiStatsVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cwapiStatsVersion.setStatus("current")
_Hh3cwapiStatsCtrlPortStatus_Type = TruthValue
_Hh3cwapiStatsCtrlPortStatus_Object = MibTableColumn
hh3cwapiStatsCtrlPortStatus = _Hh3cwapiStatsCtrlPortStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 77, 3, 3, 1, 4),
    _Hh3cwapiStatsCtrlPortStatus_Type()
)
hh3cwapiStatsCtrlPortStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cwapiStatsCtrlPortStatus.setStatus("current")


class _Hh3cwapiStatsSelectedUniCipher_Type(OctetString):
    """Custom type hh3cwapiStatsSelectedUniCipher based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )
    fixed_length = 4


_Hh3cwapiStatsSelectedUniCipher_Type.__name__ = "OctetString"
_Hh3cwapiStatsSelectedUniCipher_Object = MibTableColumn
hh3cwapiStatsSelectedUniCipher = _Hh3cwapiStatsSelectedUniCipher_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 77, 3, 3, 1, 5),
    _Hh3cwapiStatsSelectedUniCipher_Type()
)
hh3cwapiStatsSelectedUniCipher.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cwapiStatsSelectedUniCipher.setStatus("current")
_Hh3cwapiStatsWPIReplayCnt_Type = Counter32
_Hh3cwapiStatsWPIReplayCnt_Object = MibTableColumn
hh3cwapiStatsWPIReplayCnt = _Hh3cwapiStatsWPIReplayCnt_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 77, 3, 3, 1, 6),
    _Hh3cwapiStatsWPIReplayCnt_Type()
)
hh3cwapiStatsWPIReplayCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cwapiStatsWPIReplayCnt.setStatus("current")
_Hh3cwapiStatsWPIDecryptErr_Type = Counter32
_Hh3cwapiStatsWPIDecryptErr_Object = MibTableColumn
hh3cwapiStatsWPIDecryptErr = _Hh3cwapiStatsWPIDecryptErr_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 77, 3, 3, 1, 7),
    _Hh3cwapiStatsWPIDecryptErr_Type()
)
hh3cwapiStatsWPIDecryptErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cwapiStatsWPIDecryptErr.setStatus("current")
_Hh3cwapiStatsWPIMICErr_Type = Counter32
_Hh3cwapiStatsWPIMICErr_Object = MibTableColumn
hh3cwapiStatsWPIMICErr = _Hh3cwapiStatsWPIMICErr_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 77, 3, 3, 1, 8),
    _Hh3cwapiStatsWPIMICErr_Type()
)
hh3cwapiStatsWPIMICErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cwapiStatsWPIMICErr.setStatus("current")
_Hh3cwapiStatsWAISignatureErr_Type = Counter32
_Hh3cwapiStatsWAISignatureErr_Object = MibTableColumn
hh3cwapiStatsWAISignatureErr = _Hh3cwapiStatsWAISignatureErr_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 77, 3, 3, 1, 9),
    _Hh3cwapiStatsWAISignatureErr_Type()
)
hh3cwapiStatsWAISignatureErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cwapiStatsWAISignatureErr.setStatus("current")
_Hh3cwapiStatsWAIHMACErr_Type = Counter32
_Hh3cwapiStatsWAIHMACErr_Object = MibTableColumn
hh3cwapiStatsWAIHMACErr = _Hh3cwapiStatsWAIHMACErr_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 77, 3, 3, 1, 10),
    _Hh3cwapiStatsWAIHMACErr_Type()
)
hh3cwapiStatsWAIHMACErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cwapiStatsWAIHMACErr.setStatus("current")
_Hh3cwapiStatsWAIAuthenFail_Type = Counter32
_Hh3cwapiStatsWAIAuthenFail_Object = MibTableColumn
hh3cwapiStatsWAIAuthenFail = _Hh3cwapiStatsWAIAuthenFail_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 77, 3, 3, 1, 11),
    _Hh3cwapiStatsWAIAuthenFail_Type()
)
hh3cwapiStatsWAIAuthenFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cwapiStatsWAIAuthenFail.setStatus("current")
_Hh3cwapiStatsWAIDiscardCnt_Type = Counter32
_Hh3cwapiStatsWAIDiscardCnt_Object = MibTableColumn
hh3cwapiStatsWAIDiscardCnt = _Hh3cwapiStatsWAIDiscardCnt_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 77, 3, 3, 1, 12),
    _Hh3cwapiStatsWAIDiscardCnt_Type()
)
hh3cwapiStatsWAIDiscardCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cwapiStatsWAIDiscardCnt.setStatus("current")
_Hh3cwapiStatsWAITimeoutCnt_Type = Counter32
_Hh3cwapiStatsWAITimeoutCnt_Object = MibTableColumn
hh3cwapiStatsWAITimeoutCnt = _Hh3cwapiStatsWAITimeoutCnt_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 77, 3, 3, 1, 13),
    _Hh3cwapiStatsWAITimeoutCnt_Type()
)
hh3cwapiStatsWAITimeoutCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cwapiStatsWAITimeoutCnt.setStatus("current")
_Hh3cwapiStatsWAIFormatErr_Type = Counter32
_Hh3cwapiStatsWAIFormatErr_Object = MibTableColumn
hh3cwapiStatsWAIFormatErr = _Hh3cwapiStatsWAIFormatErr_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 77, 3, 3, 1, 14),
    _Hh3cwapiStatsWAIFormatErr_Type()
)
hh3cwapiStatsWAIFormatErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cwapiStatsWAIFormatErr.setStatus("current")
_Hh3cwapiStatsWAICertFail_Type = Counter32
_Hh3cwapiStatsWAICertFail_Object = MibTableColumn
hh3cwapiStatsWAICertFail = _Hh3cwapiStatsWAICertFail_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 77, 3, 3, 1, 15),
    _Hh3cwapiStatsWAICertFail_Type()
)
hh3cwapiStatsWAICertFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cwapiStatsWAICertFail.setStatus("current")
_Hh3cwapiStatsWAIUniFail_Type = Counter32
_Hh3cwapiStatsWAIUniFail_Object = MibTableColumn
hh3cwapiStatsWAIUniFail = _Hh3cwapiStatsWAIUniFail_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 77, 3, 3, 1, 16),
    _Hh3cwapiStatsWAIUniFail_Type()
)
hh3cwapiStatsWAIUniFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cwapiStatsWAIUniFail.setStatus("current")
_Hh3cwapiStatsWAIMultiFail_Type = Counter32
_Hh3cwapiStatsWAIMultiFail_Object = MibTableColumn
hh3cwapiStatsWAIMultiFail = _Hh3cwapiStatsWAIMultiFail_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 77, 3, 3, 1, 17),
    _Hh3cwapiStatsWAIMultiFail_Type()
)
hh3cwapiStatsWAIMultiFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cwapiStatsWAIMultiFail.setStatus("current")
_Hh3cwapiTrap_ObjectIdentity = ObjectIdentity
hh3cwapiTrap = _Hh3cwapiTrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 77, 4)
)
_Hh3cwapiTrapPrefix_ObjectIdentity = ObjectIdentity
hh3cwapiTrapPrefix = _Hh3cwapiTrapPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 77, 4, 0)
)
_Hh3cwapiTrapInfo_ObjectIdentity = ObjectIdentity
hh3cwapiTrapInfo = _Hh3cwapiTrapInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 77, 4, 1)
)
_Hh3cwapiTrapInfoMacAddr_Type = MacAddress
_Hh3cwapiTrapInfoMacAddr_Object = MibScalar
hh3cwapiTrapInfoMacAddr = _Hh3cwapiTrapInfoMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 77, 4, 1, 1),
    _Hh3cwapiTrapInfoMacAddr_Type()
)
hh3cwapiTrapInfoMacAddr.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cwapiTrapInfoMacAddr.setStatus("current")
_Hh3cwapiTrapInfoAPId_Type = Integer32
_Hh3cwapiTrapInfoAPId_Object = MibScalar
hh3cwapiTrapInfoAPId = _Hh3cwapiTrapInfoAPId_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 77, 4, 1, 2),
    _Hh3cwapiTrapInfoAPId_Type()
)
hh3cwapiTrapInfoAPId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cwapiTrapInfoAPId.setStatus("current")
_Hh3cwapiTrapInfoRadioId_Type = Integer32
_Hh3cwapiTrapInfoRadioId_Object = MibScalar
hh3cwapiTrapInfoRadioId = _Hh3cwapiTrapInfoRadioId_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 77, 4, 1, 3),
    _Hh3cwapiTrapInfoRadioId_Type()
)
hh3cwapiTrapInfoRadioId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cwapiTrapInfoRadioId.setStatus("current")
_Hh3cwapiTrapInfoBSSId_Type = MacAddress
_Hh3cwapiTrapInfoBSSId_Object = MibScalar
hh3cwapiTrapInfoBSSId = _Hh3cwapiTrapInfoBSSId_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 77, 4, 1, 4),
    _Hh3cwapiTrapInfoBSSId_Type()
)
hh3cwapiTrapInfoBSSId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cwapiTrapInfoBSSId.setStatus("current")
_Hh3cwapiTrapInfoAPMacAddr_Type = MacAddress
_Hh3cwapiTrapInfoAPMacAddr_Object = MibScalar
hh3cwapiTrapInfoAPMacAddr = _Hh3cwapiTrapInfoAPMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 77, 4, 1, 5),
    _Hh3cwapiTrapInfoAPMacAddr_Type()
)
hh3cwapiTrapInfoAPMacAddr.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cwapiTrapInfoAPMacAddr.setStatus("current")

# Managed Objects groups


# Notification objects

hh3cwapiUserwithInvalidCertificate = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 77, 4, 0, 1)
)
hh3cwapiUserwithInvalidCertificate.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("IF-MIB", "ifDescr"),
        ("HH3C-WAPI-MIB", "hh3cwapiTrapInfoMacAddr"),
        ("HH3C-WAPI-MIB", "hh3cwapiTrapInfoAPId"),
        ("HH3C-WAPI-MIB", "hh3cwapiTrapInfoRadioId"),
        ("HH3C-WAPI-MIB", "hh3cwapiTrapInfoBSSId"),
        ("HH3C-WAPI-MIB", "hh3cwapiTrapInfoAPMacAddr"))
)
if mibBuilder.loadTexts:
    hh3cwapiUserwithInvalidCertificate.setStatus(
        "current"
    )

hh3cwapiStationReplayAttack = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 77, 4, 0, 2)
)
hh3cwapiStationReplayAttack.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("IF-MIB", "ifDescr"),
        ("HH3C-WAPI-MIB", "hh3cwapiTrapInfoMacAddr"),
        ("HH3C-WAPI-MIB", "hh3cwapiTrapInfoAPId"),
        ("HH3C-WAPI-MIB", "hh3cwapiTrapInfoRadioId"),
        ("HH3C-WAPI-MIB", "hh3cwapiTrapInfoBSSId"),
        ("HH3C-WAPI-MIB", "hh3cwapiTrapInfoAPMacAddr"))
)
if mibBuilder.loadTexts:
    hh3cwapiStationReplayAttack.setStatus(
        "current"
    )

hh3cwapiTamperAttack = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 77, 4, 0, 3)
)
hh3cwapiTamperAttack.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("IF-MIB", "ifDescr"),
        ("HH3C-WAPI-MIB", "hh3cwapiTrapInfoMacAddr"),
        ("HH3C-WAPI-MIB", "hh3cwapiTrapInfoAPId"),
        ("HH3C-WAPI-MIB", "hh3cwapiTrapInfoRadioId"),
        ("HH3C-WAPI-MIB", "hh3cwapiTrapInfoBSSId"),
        ("HH3C-WAPI-MIB", "hh3cwapiTrapInfoAPMacAddr"))
)
if mibBuilder.loadTexts:
    hh3cwapiTamperAttack.setStatus(
        "current"
    )

hh3cwapiLowSafeLevelAttack = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 77, 4, 0, 4)
)
hh3cwapiLowSafeLevelAttack.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("IF-MIB", "ifDescr"),
        ("HH3C-WAPI-MIB", "hh3cwapiTrapInfoMacAddr"),
        ("HH3C-WAPI-MIB", "hh3cwapiTrapInfoAPId"),
        ("HH3C-WAPI-MIB", "hh3cwapiTrapInfoRadioId"),
        ("HH3C-WAPI-MIB", "hh3cwapiTrapInfoBSSId"),
        ("HH3C-WAPI-MIB", "hh3cwapiTrapInfoAPMacAddr"))
)
if mibBuilder.loadTexts:
    hh3cwapiLowSafeLevelAttack.setStatus(
        "current"
    )

hh3cwapiAddressRedirectionAttack = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 77, 4, 0, 5)
)
hh3cwapiAddressRedirectionAttack.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("IF-MIB", "ifDescr"),
        ("HH3C-WAPI-MIB", "hh3cwapiTrapInfoMacAddr"),
        ("HH3C-WAPI-MIB", "hh3cwapiTrapInfoAPId"),
        ("HH3C-WAPI-MIB", "hh3cwapiTrapInfoRadioId"),
        ("HH3C-WAPI-MIB", "hh3cwapiTrapInfoBSSId"),
        ("HH3C-WAPI-MIB", "hh3cwapiTrapInfoAPMacAddr"))
)
if mibBuilder.loadTexts:
    hh3cwapiAddressRedirectionAttack.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HH3C-WAPI-MIB",
    **{"hh3cwapiMIB": hh3cwapiMIB,
       "hh3cwapiMIBObjects": hh3cwapiMIBObjects,
       "hh3cwapiModeEnabled": hh3cwapiModeEnabled,
       "hh3cwapiASIPAddressType": hh3cwapiASIPAddressType,
       "hh3cwapiASIPAddress": hh3cwapiASIPAddress,
       "hh3cwapiCertificateInstalled": hh3cwapiCertificateInstalled,
       "hh3cwapiMIBStatsObjects": hh3cwapiMIBStatsObjects,
       "hh3cwapiStatsWAISignatureErrors": hh3cwapiStatsWAISignatureErrors,
       "hh3cwapiStatsWAIHMACErrors": hh3cwapiStatsWAIHMACErrors,
       "hh3cwapiStatsWAIAuthRsltFailures": hh3cwapiStatsWAIAuthRsltFailures,
       "hh3cwapiStatsWAIDiscardCounters": hh3cwapiStatsWAIDiscardCounters,
       "hh3cwapiStatsWAITimeoutCounters": hh3cwapiStatsWAITimeoutCounters,
       "hh3cwapiStatsWAIFormatErrors": hh3cwapiStatsWAIFormatErrors,
       "hh3cwapiStatsWAICtfHskFailures": hh3cwapiStatsWAICtfHskFailures,
       "hh3cwapiStatsWAIUniHskFailures": hh3cwapiStatsWAIUniHskFailures,
       "hh3cwapiStatsWAIMulHskFailures": hh3cwapiStatsWAIMulHskFailures,
       "hh3cwapiMIBTableObjects": hh3cwapiMIBTableObjects,
       "hh3cwapiConfigTable": hh3cwapiConfigTable,
       "hh3cwapiConfigEntry": hh3cwapiConfigEntry,
       "hh3cwapiConfigASIPAddressType": hh3cwapiConfigASIPAddressType,
       "hh3cwapiConfigASIPAddress": hh3cwapiConfigASIPAddress,
       "hh3cwapiConfigAuthMethod": hh3cwapiConfigAuthMethod,
       "hh3cwapiConfigAuthMode": hh3cwapiConfigAuthMode,
       "hh3cwapiConfigISPDomain": hh3cwapiConfigISPDomain,
       "hh3cwapiConfigCertificateDomain": hh3cwapiConfigCertificateDomain,
       "hh3cwapiConfigASName": hh3cwapiConfigASName,
       "hh3cwapiConfigBKRekeyEnabled": hh3cwapiConfigBKRekeyEnabled,
       "hh3cwapiConfigExtTable": hh3cwapiConfigExtTable,
       "hh3cwapiConfigExtEntry": hh3cwapiConfigExtEntry,
       "hh3cwapiConfigServicePolicyID": hh3cwapiConfigServicePolicyID,
       "hh3cwapiConfigUnicastCipherEnabled": hh3cwapiConfigUnicastCipherEnabled,
       "hh3cwapiConfigUnicastCipherSize": hh3cwapiConfigUnicastCipherSize,
       "hh3cwapiConfigAuthenticationSuiteEnabled": hh3cwapiConfigAuthenticationSuiteEnabled,
       "hh3cwapiConfigAuthenticationSuite": hh3cwapiConfigAuthenticationSuite,
       "hh3cwapiCfgExtASIPAddressType": hh3cwapiCfgExtASIPAddressType,
       "hh3cwapiCfgExtASIPAddress": hh3cwapiCfgExtASIPAddress,
       "hh3cwapiCfgExtASName": hh3cwapiCfgExtASName,
       "hh3cwapiCfgExtCertDomain": hh3cwapiCfgExtCertDomain,
       "hh3cwapiCfgExtCertInstalled": hh3cwapiCfgExtCertInstalled,
       "hh3cwapiConfigVersion": hh3cwapiConfigVersion,
       "hh3cwapiControlledAuthControl": hh3cwapiControlledAuthControl,
       "hh3cwapiControlledPortControl": hh3cwapiControlledPortControl,
       "hh3cwapiOptionImplemented": hh3cwapiOptionImplemented,
       "hh3cwapiPreauthImplemented": hh3cwapiPreauthImplemented,
       "hh3cwapiEnabled": hh3cwapiEnabled,
       "hh3cwapiPreauthEnabled": hh3cwapiPreauthEnabled,
       "hh3cwapiCfgUniKeysSupported": hh3cwapiCfgUniKeysSupported,
       "hh3cwapiCfgUniRekeyMethod": hh3cwapiCfgUniRekeyMethod,
       "hh3cwapiCfgUniRekeyTime": hh3cwapiCfgUniRekeyTime,
       "hh3cwapiCfgUniRekeyPackets": hh3cwapiCfgUniRekeyPackets,
       "hh3cwapiCfgMultiCipher": hh3cwapiCfgMultiCipher,
       "hh3cwapiCfgMultiRekeyMethod": hh3cwapiCfgMultiRekeyMethod,
       "hh3cwapiCfgMultiRekeyTime": hh3cwapiCfgMultiRekeyTime,
       "hh3cwapiCfgMultiRekeyPackets": hh3cwapiCfgMultiRekeyPackets,
       "hh3cwapiCfgMultiRekeyStrict": hh3cwapiCfgMultiRekeyStrict,
       "hh3cwapiCfgPSKValue": hh3cwapiCfgPSKValue,
       "hh3cwapiCfgPSKPassPhrase": hh3cwapiCfgPSKPassPhrase,
       "hh3cwapiCfgCertUpdateCount": hh3cwapiCfgCertUpdateCount,
       "hh3cwapiCfgMultiUpdateCount": hh3cwapiCfgMultiUpdateCount,
       "hh3cwapiCfgUniUpdateCount": hh3cwapiCfgUniUpdateCount,
       "hh3cwapiCfgMultiCipherSize": hh3cwapiCfgMultiCipherSize,
       "hh3cwapiCfgBKLifetime": hh3cwapiCfgBKLifetime,
       "hh3cwapiCfgBKReauthThreshold": hh3cwapiCfgBKReauthThreshold,
       "hh3cwapiCfgSATimeout": hh3cwapiCfgSATimeout,
       "hh3cwapiAuthenSuiteSelected": hh3cwapiAuthenSuiteSelected,
       "hh3cwapiUniCipherSelected": hh3cwapiUniCipherSelected,
       "hh3cwapiMultiCipherSelected": hh3cwapiMultiCipherSelected,
       "hh3cwapiBKIDUsed": hh3cwapiBKIDUsed,
       "hh3cwapiAuthenSuiteRequested": hh3cwapiAuthenSuiteRequested,
       "hh3cwapiUniCipherRequested": hh3cwapiUniCipherRequested,
       "hh3cwapiMultiCipherRequested": hh3cwapiMultiCipherRequested,
       "hh3cwapiStatsTable": hh3cwapiStatsTable,
       "hh3cwapiStatsEntry": hh3cwapiStatsEntry,
       "hh3cwapiStationMAC": hh3cwapiStationMAC,
       "hh3cwapiStatsSTAAddress": hh3cwapiStatsSTAAddress,
       "hh3cwapiStatsVersion": hh3cwapiStatsVersion,
       "hh3cwapiStatsCtrlPortStatus": hh3cwapiStatsCtrlPortStatus,
       "hh3cwapiStatsSelectedUniCipher": hh3cwapiStatsSelectedUniCipher,
       "hh3cwapiStatsWPIReplayCnt": hh3cwapiStatsWPIReplayCnt,
       "hh3cwapiStatsWPIDecryptErr": hh3cwapiStatsWPIDecryptErr,
       "hh3cwapiStatsWPIMICErr": hh3cwapiStatsWPIMICErr,
       "hh3cwapiStatsWAISignatureErr": hh3cwapiStatsWAISignatureErr,
       "hh3cwapiStatsWAIHMACErr": hh3cwapiStatsWAIHMACErr,
       "hh3cwapiStatsWAIAuthenFail": hh3cwapiStatsWAIAuthenFail,
       "hh3cwapiStatsWAIDiscardCnt": hh3cwapiStatsWAIDiscardCnt,
       "hh3cwapiStatsWAITimeoutCnt": hh3cwapiStatsWAITimeoutCnt,
       "hh3cwapiStatsWAIFormatErr": hh3cwapiStatsWAIFormatErr,
       "hh3cwapiStatsWAICertFail": hh3cwapiStatsWAICertFail,
       "hh3cwapiStatsWAIUniFail": hh3cwapiStatsWAIUniFail,
       "hh3cwapiStatsWAIMultiFail": hh3cwapiStatsWAIMultiFail,
       "hh3cwapiTrap": hh3cwapiTrap,
       "hh3cwapiTrapPrefix": hh3cwapiTrapPrefix,
       "hh3cwapiUserwithInvalidCertificate": hh3cwapiUserwithInvalidCertificate,
       "hh3cwapiStationReplayAttack": hh3cwapiStationReplayAttack,
       "hh3cwapiTamperAttack": hh3cwapiTamperAttack,
       "hh3cwapiLowSafeLevelAttack": hh3cwapiLowSafeLevelAttack,
       "hh3cwapiAddressRedirectionAttack": hh3cwapiAddressRedirectionAttack,
       "hh3cwapiTrapInfo": hh3cwapiTrapInfo,
       "hh3cwapiTrapInfoMacAddr": hh3cwapiTrapInfoMacAddr,
       "hh3cwapiTrapInfoAPId": hh3cwapiTrapInfoAPId,
       "hh3cwapiTrapInfoRadioId": hh3cwapiTrapInfoRadioId,
       "hh3cwapiTrapInfoBSSId": hh3cwapiTrapInfoBSSId,
       "hh3cwapiTrapInfoAPMacAddr": hh3cwapiTrapInfoAPMacAddr}
)
