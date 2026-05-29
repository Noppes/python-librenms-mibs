# SNMP MIB module (DLINKSW-SSL-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\dlink\DLINKSW-SSL-MIB

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

(dlinkIndustrialCommon,) = mibBuilder.importSymbols(
    "DLINK-ID-REC-MIB",
    "dlinkIndustrialCommon")

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

dlinkSwSslMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 171, 14, 7)
)
if mibBuilder.loadTexts:
    dlinkSwSslMIB.setRevisions(
        ("2016-07-05 00:00",
         "2013-10-30 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_DlinkSslNotifications_ObjectIdentity = ObjectIdentity
dlinkSslNotifications = _DlinkSslNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 14, 7, 0)
)
_DlinkSslObjects_ObjectIdentity = ObjectIdentity
dlinkSslObjects = _DlinkSslObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 14, 7, 1)
)
_DSslCryptoPkiImportCertTable_Object = MibTable
dSslCryptoPkiImportCertTable = _DSslCryptoPkiImportCertTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 7, 1, 1)
)
if mibBuilder.loadTexts:
    dSslCryptoPkiImportCertTable.setStatus("current")
_DSslCryptoPkiImportCertEntry_Object = MibTableRow
dSslCryptoPkiImportCertEntry = _DSslCryptoPkiImportCertEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 7, 1, 1, 1)
)
dSslCryptoPkiImportCertEntry.setIndexNames(
    (0, "DLINKSW-SSL-MIB", "dSslCryPkiImportCertIndex"),
)
if mibBuilder.loadTexts:
    dSslCryptoPkiImportCertEntry.setStatus("current")


class _DSslCryPkiImportCertIndex_Type(Integer32):
    """Custom type dSslCryPkiImportCertIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
    )


_DSslCryPkiImportCertIndex_Type.__name__ = "Integer32"
_DSslCryPkiImportCertIndex_Object = MibTableColumn
dSslCryPkiImportCertIndex = _DSslCryPkiImportCertIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 7, 1, 1, 1, 1),
    _DSslCryPkiImportCertIndex_Type()
)
dSslCryPkiImportCertIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dSslCryPkiImportCertIndex.setStatus("current")


class _DSslCryPkiImportCertTrustPoint_Type(DisplayString):
    """Custom type dSslCryPkiImportCertTrustPoint based on DisplayString"""
    defaultValue = OctetString("")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_DSslCryPkiImportCertTrustPoint_Type.__name__ = "DisplayString"
_DSslCryPkiImportCertTrustPoint_Object = MibTableColumn
dSslCryPkiImportCertTrustPoint = _DSslCryPkiImportCertTrustPoint_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 7, 1, 1, 1, 2),
    _DSslCryPkiImportCertTrustPoint_Type()
)
dSslCryPkiImportCertTrustPoint.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dSslCryPkiImportCertTrustPoint.setStatus("current")


class _DSslCryPkiImportCertSrcType_Type(Integer32):
    """Custom type dSslCryPkiImportCertSrcType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("filesystem", 1),
          ("tftp", 2))
    )


_DSslCryPkiImportCertSrcType_Type.__name__ = "Integer32"
_DSslCryPkiImportCertSrcType_Object = MibTableColumn
dSslCryPkiImportCertSrcType = _DSslCryPkiImportCertSrcType_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 7, 1, 1, 1, 3),
    _DSslCryPkiImportCertSrcType_Type()
)
dSslCryPkiImportCertSrcType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dSslCryPkiImportCertSrcType.setStatus("current")


class _DSslCryPkiImportFilename_Type(DisplayString):
    """Custom type dSslCryPkiImportFilename based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_DSslCryPkiImportFilename_Type.__name__ = "DisplayString"
_DSslCryPkiImportFilename_Object = MibTableColumn
dSslCryPkiImportFilename = _DSslCryPkiImportFilename_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 7, 1, 1, 1, 4),
    _DSslCryPkiImportFilename_Type()
)
dSslCryPkiImportFilename.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dSslCryPkiImportFilename.setStatus("current")
_DSslCryPkiImportCertAddrType_Type = InetAddressType
_DSslCryPkiImportCertAddrType_Object = MibTableColumn
dSslCryPkiImportCertAddrType = _DSslCryPkiImportCertAddrType_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 7, 1, 1, 1, 5),
    _DSslCryPkiImportCertAddrType_Type()
)
dSslCryPkiImportCertAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dSslCryPkiImportCertAddrType.setStatus("current")
_DSslCryPkiImportCertAddr_Type = InetAddress
_DSslCryPkiImportCertAddr_Object = MibTableColumn
dSslCryPkiImportCertAddr = _DSslCryPkiImportCertAddr_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 7, 1, 1, 1, 6),
    _DSslCryPkiImportCertAddr_Type()
)
dSslCryPkiImportCertAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dSslCryPkiImportCertAddr.setStatus("current")


class _DSslCryPkiImportPwdPhrase_Type(DisplayString):
    """Custom type dSslCryPkiImportPwdPhrase based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_DSslCryPkiImportPwdPhrase_Type.__name__ = "DisplayString"
_DSslCryPkiImportPwdPhrase_Object = MibTableColumn
dSslCryPkiImportPwdPhrase = _DSslCryPkiImportPwdPhrase_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 7, 1, 1, 1, 7),
    _DSslCryPkiImportPwdPhrase_Type()
)
dSslCryPkiImportPwdPhrase.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dSslCryPkiImportPwdPhrase.setStatus("current")


class _DSslCryPkiImportFileType_Type(Bits):
    """Custom type dSslCryPkiImportFileType based on Bits"""
    namedValues = NamedValues(
        *(("ca", 0),
          ("local", 1))
    )

_DSslCryPkiImportFileType_Type.__name__ = "Bits"
_DSslCryPkiImportFileType_Object = MibTableColumn
dSslCryPkiImportFileType = _DSslCryPkiImportFileType_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 7, 1, 1, 1, 8),
    _DSslCryPkiImportFileType_Type()
)
dSslCryPkiImportFileType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dSslCryPkiImportFileType.setStatus("current")


class _DSslCryPkiImportErrorStatus_Type(DisplayString):
    """Custom type dSslCryPkiImportErrorStatus based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_DSslCryPkiImportErrorStatus_Type.__name__ = "DisplayString"
_DSslCryPkiImportErrorStatus_Object = MibTableColumn
dSslCryPkiImportErrorStatus = _DSslCryPkiImportErrorStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 7, 1, 1, 1, 9),
    _DSslCryPkiImportErrorStatus_Type()
)
dSslCryPkiImportErrorStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dSslCryPkiImportErrorStatus.setStatus("current")
_DSslCryPkiImportRowStatus_Type = RowStatus
_DSslCryPkiImportRowStatus_Object = MibTableColumn
dSslCryPkiImportRowStatus = _DSslCryPkiImportRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 7, 1, 1, 1, 10),
    _DSslCryPkiImportRowStatus_Type()
)
dSslCryPkiImportRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dSslCryPkiImportRowStatus.setStatus("current")
_DSslConfiguration_ObjectIdentity = ObjectIdentity
dSslConfiguration = _DSslConfiguration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 14, 7, 1, 2)
)
_DSslCryptoPkiTrustpointTable_Object = MibTable
dSslCryptoPkiTrustpointTable = _DSslCryptoPkiTrustpointTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 7, 1, 2, 1)
)
if mibBuilder.loadTexts:
    dSslCryptoPkiTrustpointTable.setStatus("current")
_DSslCryptoPkiTrustpointEntry_Object = MibTableRow
dSslCryptoPkiTrustpointEntry = _DSslCryptoPkiTrustpointEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 7, 1, 2, 1, 1)
)
dSslCryptoPkiTrustpointEntry.setIndexNames(
    (0, "DLINKSW-SSL-MIB", "dSslCryptoPkiTrustpointName"),
)
if mibBuilder.loadTexts:
    dSslCryptoPkiTrustpointEntry.setStatus("current")


class _DSslCryptoPkiTrustpointName_Type(DisplayString):
    """Custom type dSslCryptoPkiTrustpointName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_DSslCryptoPkiTrustpointName_Type.__name__ = "DisplayString"
_DSslCryptoPkiTrustpointName_Object = MibTableColumn
dSslCryptoPkiTrustpointName = _DSslCryptoPkiTrustpointName_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 7, 1, 2, 1, 1, 1),
    _DSslCryptoPkiTrustpointName_Type()
)
dSslCryptoPkiTrustpointName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dSslCryptoPkiTrustpointName.setStatus("current")


class _DSslCryptoPkiTrustpointPrimary_Type(TruthValue):
    """Custom type dSslCryptoPkiTrustpointPrimary based on TruthValue"""
    defaultValue = 2


_DSslCryptoPkiTrustpointPrimary_Type.__name__ = "TruthValue"
_DSslCryptoPkiTrustpointPrimary_Object = MibTableColumn
dSslCryptoPkiTrustpointPrimary = _DSslCryptoPkiTrustpointPrimary_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 7, 1, 2, 1, 1, 2),
    _DSslCryptoPkiTrustpointPrimary_Type()
)
dSslCryptoPkiTrustpointPrimary.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dSslCryptoPkiTrustpointPrimary.setStatus("current")
_DSslCryptoPkiTrustpointRowStatus_Type = RowStatus
_DSslCryptoPkiTrustpointRowStatus_Object = MibTableColumn
dSslCryptoPkiTrustpointRowStatus = _DSslCryptoPkiTrustpointRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 7, 1, 2, 1, 1, 3),
    _DSslCryptoPkiTrustpointRowStatus_Type()
)
dSslCryptoPkiTrustpointRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dSslCryptoPkiTrustpointRowStatus.setStatus("current")
_DSslCryptoPkiCertTable_Object = MibTable
dSslCryptoPkiCertTable = _DSslCryptoPkiCertTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 7, 1, 2, 2)
)
if mibBuilder.loadTexts:
    dSslCryptoPkiCertTable.setStatus("current")
_DSslCryptoPkiCertEntry_Object = MibTableRow
dSslCryptoPkiCertEntry = _DSslCryptoPkiCertEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 7, 1, 2, 2, 1)
)
dSslCryptoPkiCertEntry.setIndexNames(
    (0, "DLINKSW-SSL-MIB", "dSslCryptoPkiTrustpointName"),
    (0, "DLINKSW-SSL-MIB", "dSslCryptoPkiCertName"),
)
if mibBuilder.loadTexts:
    dSslCryptoPkiCertEntry.setStatus("current")


class _DSslCryptoPkiCertName_Type(DisplayString):
    """Custom type dSslCryptoPkiCertName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_DSslCryptoPkiCertName_Type.__name__ = "DisplayString"
_DSslCryptoPkiCertName_Object = MibTableColumn
dSslCryptoPkiCertName = _DSslCryptoPkiCertName_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 7, 1, 2, 2, 1, 1),
    _DSslCryptoPkiCertName_Type()
)
dSslCryptoPkiCertName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dSslCryptoPkiCertName.setStatus("current")


class _DSslCryptoPkiCertCAType_Type(Integer32):
    """Custom type dSslCryptoPkiCertCAType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("ca", 1),
          ("localCertificate", 2),
          ("localPrivateKey", 3))
    )


_DSslCryptoPkiCertCAType_Type.__name__ = "Integer32"
_DSslCryptoPkiCertCAType_Object = MibTableColumn
dSslCryptoPkiCertCAType = _DSslCryptoPkiCertCAType_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 7, 1, 2, 2, 1, 2),
    _DSslCryptoPkiCertCAType_Type()
)
dSslCryptoPkiCertCAType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dSslCryptoPkiCertCAType.setStatus("current")


class _DSslCryptoPkiCertRemoveCtrl_Type(Integer32):
    """Custom type dSslCryptoPkiCertRemoveCtrl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("delete", 1),
          ("noOp", 2))
    )


_DSslCryptoPkiCertRemoveCtrl_Type.__name__ = "Integer32"
_DSslCryptoPkiCertRemoveCtrl_Object = MibTableColumn
dSslCryptoPkiCertRemoveCtrl = _DSslCryptoPkiCertRemoveCtrl_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 7, 1, 2, 2, 1, 3),
    _DSslCryptoPkiCertRemoveCtrl_Type()
)
dSslCryptoPkiCertRemoveCtrl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dSslCryptoPkiCertRemoveCtrl.setStatus("current")
_DSslServicePolicyTable_Object = MibTable
dSslServicePolicyTable = _DSslServicePolicyTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 7, 1, 2, 3)
)
if mibBuilder.loadTexts:
    dSslServicePolicyTable.setStatus("current")
_DSslServicePolicyEntry_Object = MibTableRow
dSslServicePolicyEntry = _DSslServicePolicyEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 7, 1, 2, 3, 1)
)
dSslServicePolicyEntry.setIndexNames(
    (0, "DLINKSW-SSL-MIB", "dSslServicePolicyName"),
)
if mibBuilder.loadTexts:
    dSslServicePolicyEntry.setStatus("current")


class _DSslServicePolicyName_Type(DisplayString):
    """Custom type dSslServicePolicyName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_DSslServicePolicyName_Type.__name__ = "DisplayString"
_DSslServicePolicyName_Object = MibTableColumn
dSslServicePolicyName = _DSslServicePolicyName_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 7, 1, 2, 3, 1, 1),
    _DSslServicePolicyName_Type()
)
dSslServicePolicyName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dSslServicePolicyName.setStatus("current")


class _DSslServicePolicyCipherSuites_Type(Bits):
    """Custom type dSslServicePolicyCipherSuites based on Bits"""
    namedValues = NamedValues(
        *(("dheDss3DesEdeCbcSha", 0),
          ("rsa3desEdeCbcSha", 1),
          ("rsaRc4128Sha", 2),
          ("rsaRc4128Md5", 3),
          ("rsaExportRc440Md5", 4),
          ("rsaAes128CbcSha", 5),
          ("rsaAes256CbcSha", 6),
          ("rsaAes128CbcSha256", 7),
          ("rsaAes256CbcSha256", 8),
          ("dheDssAes256CbcSha", 9),
          ("dheRsaAes256CbcSha", 10))
    )

_DSslServicePolicyCipherSuites_Type.__name__ = "Bits"
_DSslServicePolicyCipherSuites_Object = MibTableColumn
dSslServicePolicyCipherSuites = _DSslServicePolicyCipherSuites_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 7, 1, 2, 3, 1, 2),
    _DSslServicePolicyCipherSuites_Type()
)
dSslServicePolicyCipherSuites.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dSslServicePolicyCipherSuites.setStatus("current")


class _DSslServicePolicyTrustpoint_Type(DisplayString):
    """Custom type dSslServicePolicyTrustpoint based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_DSslServicePolicyTrustpoint_Type.__name__ = "DisplayString"
_DSslServicePolicyTrustpoint_Object = MibTableColumn
dSslServicePolicyTrustpoint = _DSslServicePolicyTrustpoint_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 7, 1, 2, 3, 1, 3),
    _DSslServicePolicyTrustpoint_Type()
)
dSslServicePolicyTrustpoint.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dSslServicePolicyTrustpoint.setStatus("current")


class _DSslServicePolicyCacheTimeout_Type(Unsigned32):
    """Custom type dSslServicePolicyCacheTimeout based on Unsigned32"""
    defaultValue = 600

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(60, 86400),
    )


_DSslServicePolicyCacheTimeout_Type.__name__ = "Unsigned32"
_DSslServicePolicyCacheTimeout_Object = MibTableColumn
dSslServicePolicyCacheTimeout = _DSslServicePolicyCacheTimeout_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 7, 1, 2, 3, 1, 4),
    _DSslServicePolicyCacheTimeout_Type()
)
dSslServicePolicyCacheTimeout.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dSslServicePolicyCacheTimeout.setStatus("current")
_DSslServicePolicyRowStatus_Type = RowStatus
_DSslServicePolicyRowStatus_Object = MibTableColumn
dSslServicePolicyRowStatus = _DSslServicePolicyRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 7, 1, 2, 3, 1, 5),
    _DSslServicePolicyRowStatus_Type()
)
dSslServicePolicyRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dSslServicePolicyRowStatus.setStatus("current")


class _DSslServicePolicyVersions_Type(Bits):
    """Custom type dSslServicePolicyVersions based on Bits"""
    namedValues = NamedValues(
        *(("ssl3_0", 0),
          ("tls1_0", 1),
          ("tls1_1", 2),
          ("tls1_2", 3))
    )

_DSslServicePolicyVersions_Type.__name__ = "Bits"
_DSslServicePolicyVersions_Object = MibTableColumn
dSslServicePolicyVersions = _DSslServicePolicyVersions_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 7, 1, 2, 3, 1, 6),
    _DSslServicePolicyVersions_Type()
)
dSslServicePolicyVersions.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dSslServicePolicyVersions.setStatus("current")
_DlinkSslConformance_ObjectIdentity = ObjectIdentity
dlinkSslConformance = _DlinkSslConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 14, 7, 2)
)
_DlinkSslCompliances_ObjectIdentity = ObjectIdentity
dlinkSslCompliances = _DlinkSslCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 14, 7, 2, 1)
)
_DlinkSslGroups_ObjectIdentity = ObjectIdentity
dlinkSslGroups = _DlinkSslGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 14, 7, 2, 2)
)

# Managed Objects groups

dSslImportCertGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 171, 14, 7, 2, 2, 1)
)
dSslImportCertGroup.setObjects(
      *(("DLINKSW-SSL-MIB", "dSslCryPkiImportCertTrustPoint"),
        ("DLINKSW-SSL-MIB", "dSslCryPkiImportCertSrcType"),
        ("DLINKSW-SSL-MIB", "dSslCryPkiImportFilename"),
        ("DLINKSW-SSL-MIB", "dSslCryPkiImportCertAddrType"),
        ("DLINKSW-SSL-MIB", "dSslCryPkiImportCertAddr"),
        ("DLINKSW-SSL-MIB", "dSslCryPkiImportPwdPhrase"),
        ("DLINKSW-SSL-MIB", "dSslCryPkiImportFileType"),
        ("DLINKSW-SSL-MIB", "dSslCryPkiImportErrorStatus"),
        ("DLINKSW-SSL-MIB", "dSslCryPkiImportRowStatus"))
)
if mibBuilder.loadTexts:
    dSslImportCertGroup.setStatus("current")

dSslTrustPointConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 171, 14, 7, 2, 2, 2)
)
dSslTrustPointConfigGroup.setObjects(
      *(("DLINKSW-SSL-MIB", "dSslCryptoPkiTrustpointPrimary"),
        ("DLINKSW-SSL-MIB", "dSslCryptoPkiTrustpointRowStatus"),
        ("DLINKSW-SSL-MIB", "dSslCryptoPkiCertCAType"),
        ("DLINKSW-SSL-MIB", "dSslCryptoPkiCertRemoveCtrl"))
)
if mibBuilder.loadTexts:
    dSslTrustPointConfigGroup.setStatus("current")

dSslServicePolicyGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 171, 14, 7, 2, 2, 3)
)
dSslServicePolicyGroup.setObjects(
      *(("DLINKSW-SSL-MIB", "dSslServicePolicyCipherSuites"),
        ("DLINKSW-SSL-MIB", "dSslServicePolicyTrustpoint"),
        ("DLINKSW-SSL-MIB", "dSslServicePolicyCacheTimeout"),
        ("DLINKSW-SSL-MIB", "dSslServicePolicyRowStatus"))
)
if mibBuilder.loadTexts:
    dSslServicePolicyGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

dlinkSslCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 171, 14, 7, 2, 1, 1)
)
dlinkSslCompliance.setObjects(
      *(("DLINKSW-SSL-MIB", "dSslImportCertGroup"),
        ("DLINKSW-SSL-MIB", "dSslTrustPointConfigGroup"),
        ("DLINKSW-SSL-MIB", "dSslServicePolicyGroup"))
)
if mibBuilder.loadTexts:
    dlinkSslCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "DLINKSW-SSL-MIB",
    **{"dlinkSwSslMIB": dlinkSwSslMIB,
       "dlinkSslNotifications": dlinkSslNotifications,
       "dlinkSslObjects": dlinkSslObjects,
       "dSslCryptoPkiImportCertTable": dSslCryptoPkiImportCertTable,
       "dSslCryptoPkiImportCertEntry": dSslCryptoPkiImportCertEntry,
       "dSslCryPkiImportCertIndex": dSslCryPkiImportCertIndex,
       "dSslCryPkiImportCertTrustPoint": dSslCryPkiImportCertTrustPoint,
       "dSslCryPkiImportCertSrcType": dSslCryPkiImportCertSrcType,
       "dSslCryPkiImportFilename": dSslCryPkiImportFilename,
       "dSslCryPkiImportCertAddrType": dSslCryPkiImportCertAddrType,
       "dSslCryPkiImportCertAddr": dSslCryPkiImportCertAddr,
       "dSslCryPkiImportPwdPhrase": dSslCryPkiImportPwdPhrase,
       "dSslCryPkiImportFileType": dSslCryPkiImportFileType,
       "dSslCryPkiImportErrorStatus": dSslCryPkiImportErrorStatus,
       "dSslCryPkiImportRowStatus": dSslCryPkiImportRowStatus,
       "dSslConfiguration": dSslConfiguration,
       "dSslCryptoPkiTrustpointTable": dSslCryptoPkiTrustpointTable,
       "dSslCryptoPkiTrustpointEntry": dSslCryptoPkiTrustpointEntry,
       "dSslCryptoPkiTrustpointName": dSslCryptoPkiTrustpointName,
       "dSslCryptoPkiTrustpointPrimary": dSslCryptoPkiTrustpointPrimary,
       "dSslCryptoPkiTrustpointRowStatus": dSslCryptoPkiTrustpointRowStatus,
       "dSslCryptoPkiCertTable": dSslCryptoPkiCertTable,
       "dSslCryptoPkiCertEntry": dSslCryptoPkiCertEntry,
       "dSslCryptoPkiCertName": dSslCryptoPkiCertName,
       "dSslCryptoPkiCertCAType": dSslCryptoPkiCertCAType,
       "dSslCryptoPkiCertRemoveCtrl": dSslCryptoPkiCertRemoveCtrl,
       "dSslServicePolicyTable": dSslServicePolicyTable,
       "dSslServicePolicyEntry": dSslServicePolicyEntry,
       "dSslServicePolicyName": dSslServicePolicyName,
       "dSslServicePolicyCipherSuites": dSslServicePolicyCipherSuites,
       "dSslServicePolicyTrustpoint": dSslServicePolicyTrustpoint,
       "dSslServicePolicyCacheTimeout": dSslServicePolicyCacheTimeout,
       "dSslServicePolicyRowStatus": dSslServicePolicyRowStatus,
       "dSslServicePolicyVersions": dSslServicePolicyVersions,
       "dlinkSslConformance": dlinkSslConformance,
       "dlinkSslCompliances": dlinkSslCompliances,
       "dlinkSslCompliance": dlinkSslCompliance,
       "dlinkSslGroups": dlinkSslGroups,
       "dSslImportCertGroup": dSslImportCertGroup,
       "dSslTrustPointConfigGroup": dSslTrustPointConfigGroup,
       "dSslServicePolicyGroup": dSslServicePolicyGroup}
)
