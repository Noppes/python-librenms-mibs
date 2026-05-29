# SNMP MIB module (ALTEON-CHEETAH-LAYER7-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\alteonos\ALTEON-CHEETAH-LAYER7-MIB

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

(aws_switch,) = mibBuilder.importSymbols(
    "ALTEON-ROOT-MIB",
    "aws-switch")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

layer7 = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5)
)
if mibBuilder.loadTexts:
    layer7.setRevisions(
        ("2004-09-01 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Layer7Configs_ObjectIdentity = ObjectIdentity
layer7Configs = _Layer7Configs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 1)
)
_UrlCfg_ObjectIdentity = ObjectIdentity
urlCfg = _UrlCfg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 1, 1)
)
_SlbUrlRedir_ObjectIdentity = ObjectIdentity
slbUrlRedir = _SlbUrlRedir_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 1, 1, 1)
)


class _SlbCurCfgUrlRedirNonGetOrigSrv_Type(Integer32):
    """Custom type slbCurCfgUrlRedirNonGetOrigSrv based on Integer32"""
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


_SlbCurCfgUrlRedirNonGetOrigSrv_Type.__name__ = "Integer32"
_SlbCurCfgUrlRedirNonGetOrigSrv_Object = MibScalar
slbCurCfgUrlRedirNonGetOrigSrv = _SlbCurCfgUrlRedirNonGetOrigSrv_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 1, 1, 1, 3),
    _SlbCurCfgUrlRedirNonGetOrigSrv_Type()
)
slbCurCfgUrlRedirNonGetOrigSrv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbCurCfgUrlRedirNonGetOrigSrv.setStatus("current")


class _SlbNewCfgUrlRedirNonGetOrigSrv_Type(Integer32):
    """Custom type slbNewCfgUrlRedirNonGetOrigSrv based on Integer32"""
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


_SlbNewCfgUrlRedirNonGetOrigSrv_Type.__name__ = "Integer32"
_SlbNewCfgUrlRedirNonGetOrigSrv_Object = MibScalar
slbNewCfgUrlRedirNonGetOrigSrv = _SlbNewCfgUrlRedirNonGetOrigSrv_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 1, 1, 1, 4),
    _SlbNewCfgUrlRedirNonGetOrigSrv_Type()
)
slbNewCfgUrlRedirNonGetOrigSrv.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slbNewCfgUrlRedirNonGetOrigSrv.setStatus("current")


class _SlbCurCfgUrlRedirCookieOrigSrv_Type(Integer32):
    """Custom type slbCurCfgUrlRedirCookieOrigSrv based on Integer32"""
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


_SlbCurCfgUrlRedirCookieOrigSrv_Type.__name__ = "Integer32"
_SlbCurCfgUrlRedirCookieOrigSrv_Object = MibScalar
slbCurCfgUrlRedirCookieOrigSrv = _SlbCurCfgUrlRedirCookieOrigSrv_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 1, 1, 1, 5),
    _SlbCurCfgUrlRedirCookieOrigSrv_Type()
)
slbCurCfgUrlRedirCookieOrigSrv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbCurCfgUrlRedirCookieOrigSrv.setStatus("current")


class _SlbNewCfgUrlRedirCookieOrigSrv_Type(Integer32):
    """Custom type slbNewCfgUrlRedirCookieOrigSrv based on Integer32"""
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


_SlbNewCfgUrlRedirCookieOrigSrv_Type.__name__ = "Integer32"
_SlbNewCfgUrlRedirCookieOrigSrv_Object = MibScalar
slbNewCfgUrlRedirCookieOrigSrv = _SlbNewCfgUrlRedirCookieOrigSrv_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 1, 1, 1, 6),
    _SlbNewCfgUrlRedirCookieOrigSrv_Type()
)
slbNewCfgUrlRedirCookieOrigSrv.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slbNewCfgUrlRedirCookieOrigSrv.setStatus("current")


class _SlbCurCfgUrlRedirNoCacheOrigSrv_Type(Integer32):
    """Custom type slbCurCfgUrlRedirNoCacheOrigSrv based on Integer32"""
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


_SlbCurCfgUrlRedirNoCacheOrigSrv_Type.__name__ = "Integer32"
_SlbCurCfgUrlRedirNoCacheOrigSrv_Object = MibScalar
slbCurCfgUrlRedirNoCacheOrigSrv = _SlbCurCfgUrlRedirNoCacheOrigSrv_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 1, 1, 1, 7),
    _SlbCurCfgUrlRedirNoCacheOrigSrv_Type()
)
slbCurCfgUrlRedirNoCacheOrigSrv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbCurCfgUrlRedirNoCacheOrigSrv.setStatus("current")


class _SlbNewCfgUrlRedirNoCacheOrigSrv_Type(Integer32):
    """Custom type slbNewCfgUrlRedirNoCacheOrigSrv based on Integer32"""
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


_SlbNewCfgUrlRedirNoCacheOrigSrv_Type.__name__ = "Integer32"
_SlbNewCfgUrlRedirNoCacheOrigSrv_Object = MibScalar
slbNewCfgUrlRedirNoCacheOrigSrv = _SlbNewCfgUrlRedirNoCacheOrigSrv_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 1, 1, 1, 8),
    _SlbNewCfgUrlRedirNoCacheOrigSrv_Type()
)
slbNewCfgUrlRedirNoCacheOrigSrv.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slbNewCfgUrlRedirNoCacheOrigSrv.setStatus("current")


class _SlbCurCfgUrlRedirUriHashLength_Type(Integer32):
    """Custom type slbCurCfgUrlRedirUriHashLength based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_SlbCurCfgUrlRedirUriHashLength_Type.__name__ = "Integer32"
_SlbCurCfgUrlRedirUriHashLength_Object = MibScalar
slbCurCfgUrlRedirUriHashLength = _SlbCurCfgUrlRedirUriHashLength_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 1, 1, 1, 9),
    _SlbCurCfgUrlRedirUriHashLength_Type()
)
slbCurCfgUrlRedirUriHashLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbCurCfgUrlRedirUriHashLength.setStatus("current")


class _SlbNewCfgUrlRedirUriHashLength_Type(Integer32):
    """Custom type slbNewCfgUrlRedirUriHashLength based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_SlbNewCfgUrlRedirUriHashLength_Type.__name__ = "Integer32"
_SlbNewCfgUrlRedirUriHashLength_Object = MibScalar
slbNewCfgUrlRedirUriHashLength = _SlbNewCfgUrlRedirUriHashLength_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 1, 1, 1, 10),
    _SlbNewCfgUrlRedirUriHashLength_Type()
)
slbNewCfgUrlRedirUriHashLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slbNewCfgUrlRedirUriHashLength.setStatus("current")


class _SlbCurCfgUrlRedirHeader_Type(Integer32):
    """Custom type slbCurCfgUrlRedirHeader based on Integer32"""
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


_SlbCurCfgUrlRedirHeader_Type.__name__ = "Integer32"
_SlbCurCfgUrlRedirHeader_Object = MibScalar
slbCurCfgUrlRedirHeader = _SlbCurCfgUrlRedirHeader_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 1, 1, 1, 11),
    _SlbCurCfgUrlRedirHeader_Type()
)
slbCurCfgUrlRedirHeader.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbCurCfgUrlRedirHeader.setStatus("current")


class _SlbNewCfgUrlRedirHeader_Type(Integer32):
    """Custom type slbNewCfgUrlRedirHeader based on Integer32"""
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


_SlbNewCfgUrlRedirHeader_Type.__name__ = "Integer32"
_SlbNewCfgUrlRedirHeader_Object = MibScalar
slbNewCfgUrlRedirHeader = _SlbNewCfgUrlRedirHeader_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 1, 1, 1, 12),
    _SlbNewCfgUrlRedirHeader_Type()
)
slbNewCfgUrlRedirHeader.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slbNewCfgUrlRedirHeader.setStatus("current")


class _SlbCurCfgUrlRedirHeaderName_Type(DisplayString):
    """Custom type slbCurCfgUrlRedirHeaderName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_SlbCurCfgUrlRedirHeaderName_Type.__name__ = "DisplayString"
_SlbCurCfgUrlRedirHeaderName_Object = MibScalar
slbCurCfgUrlRedirHeaderName = _SlbCurCfgUrlRedirHeaderName_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 1, 1, 1, 13),
    _SlbCurCfgUrlRedirHeaderName_Type()
)
slbCurCfgUrlRedirHeaderName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbCurCfgUrlRedirHeaderName.setStatus("current")


class _SlbNewCfgUrlRedirHeaderName_Type(DisplayString):
    """Custom type slbNewCfgUrlRedirHeaderName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_SlbNewCfgUrlRedirHeaderName_Type.__name__ = "DisplayString"
_SlbNewCfgUrlRedirHeaderName_Object = MibScalar
slbNewCfgUrlRedirHeaderName = _SlbNewCfgUrlRedirHeaderName_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 1, 1, 1, 14),
    _SlbNewCfgUrlRedirHeaderName_Type()
)
slbNewCfgUrlRedirHeaderName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slbNewCfgUrlRedirHeaderName.setStatus("current")
_SlbUrlBalance_ObjectIdentity = ObjectIdentity
slbUrlBalance = _SlbUrlBalance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 1, 1, 2)
)
_SlbUrlLbPathTableMaxSize_Type = Integer32
_SlbUrlLbPathTableMaxSize_Object = MibScalar
slbUrlLbPathTableMaxSize = _SlbUrlLbPathTableMaxSize_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 1, 1, 2, 1),
    _SlbUrlLbPathTableMaxSize_Type()
)
slbUrlLbPathTableMaxSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbUrlLbPathTableMaxSize.setStatus("current")
_SlbCurCfgUrlLbPathTable_Object = MibTable
slbCurCfgUrlLbPathTable = _SlbCurCfgUrlLbPathTable_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 1, 1, 2, 2)
)
if mibBuilder.loadTexts:
    slbCurCfgUrlLbPathTable.setStatus("current")
_SlbCurCfgUrlLbPathTableEntry_Object = MibTableRow
slbCurCfgUrlLbPathTableEntry = _SlbCurCfgUrlLbPathTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 1, 1, 2, 2, 1)
)
slbCurCfgUrlLbPathTableEntry.setIndexNames(
    (0, "ALTEON-CHEETAH-LAYER7-MIB", "slbCurCfgUrlLbPathIndex"),
)
if mibBuilder.loadTexts:
    slbCurCfgUrlLbPathTableEntry.setStatus("current")
_SlbCurCfgUrlLbPathIndex_Type = Integer32
_SlbCurCfgUrlLbPathIndex_Object = MibTableColumn
slbCurCfgUrlLbPathIndex = _SlbCurCfgUrlLbPathIndex_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 1, 1, 2, 2, 1, 1),
    _SlbCurCfgUrlLbPathIndex_Type()
)
slbCurCfgUrlLbPathIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbCurCfgUrlLbPathIndex.setStatus("current")


class _SlbCurCfgUrlLbPathString_Type(DisplayString):
    """Custom type slbCurCfgUrlLbPathString based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 96),
    )


_SlbCurCfgUrlLbPathString_Type.__name__ = "DisplayString"
_SlbCurCfgUrlLbPathString_Object = MibTableColumn
slbCurCfgUrlLbPathString = _SlbCurCfgUrlLbPathString_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 1, 1, 2, 2, 1, 2),
    _SlbCurCfgUrlLbPathString_Type()
)
slbCurCfgUrlLbPathString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbCurCfgUrlLbPathString.setStatus("current")
_SlbCurCfgUrlLbBwmContract_Type = Integer32
_SlbCurCfgUrlLbBwmContract_Object = MibTableColumn
slbCurCfgUrlLbBwmContract = _SlbCurCfgUrlLbBwmContract_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 1, 1, 2, 2, 1, 3),
    _SlbCurCfgUrlLbBwmContract_Type()
)
slbCurCfgUrlLbBwmContract.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbCurCfgUrlLbBwmContract.setStatus("current")


class _SlbCurCfgUrlLbPathHTTPHeader_Type(DisplayString):
    """Custom type slbCurCfgUrlLbPathHTTPHeader based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_SlbCurCfgUrlLbPathHTTPHeader_Type.__name__ = "DisplayString"
_SlbCurCfgUrlLbPathHTTPHeader_Object = MibTableColumn
slbCurCfgUrlLbPathHTTPHeader = _SlbCurCfgUrlLbPathHTTPHeader_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 1, 1, 2, 2, 1, 4),
    _SlbCurCfgUrlLbPathHTTPHeader_Type()
)
slbCurCfgUrlLbPathHTTPHeader.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbCurCfgUrlLbPathHTTPHeader.setStatus("current")


class _SlbCurCfgUrlLbPathHTTPHeaderValue_Type(DisplayString):
    """Custom type slbCurCfgUrlLbPathHTTPHeaderValue based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 48),
    )


_SlbCurCfgUrlLbPathHTTPHeaderValue_Type.__name__ = "DisplayString"
_SlbCurCfgUrlLbPathHTTPHeaderValue_Object = MibTableColumn
slbCurCfgUrlLbPathHTTPHeaderValue = _SlbCurCfgUrlLbPathHTTPHeaderValue_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 1, 1, 2, 2, 1, 5),
    _SlbCurCfgUrlLbPathHTTPHeaderValue_Type()
)
slbCurCfgUrlLbPathHTTPHeaderValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbCurCfgUrlLbPathHTTPHeaderValue.setStatus("current")


class _SlbCurCfgUrlLbPathPatternStringType_Type(Integer32):
    """Custom type slbCurCfgUrlLbPathPatternStringType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("ascii", 1),
          ("binary", 2),
          ("none", 3))
    )


_SlbCurCfgUrlLbPathPatternStringType_Type.__name__ = "Integer32"
_SlbCurCfgUrlLbPathPatternStringType_Object = MibTableColumn
slbCurCfgUrlLbPathPatternStringType = _SlbCurCfgUrlLbPathPatternStringType_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 1, 1, 2, 2, 1, 6),
    _SlbCurCfgUrlLbPathPatternStringType_Type()
)
slbCurCfgUrlLbPathPatternStringType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbCurCfgUrlLbPathPatternStringType.setStatus("current")


class _SlbCurCfgUrlLbPathOffset_Type(Integer32):
    """Custom type slbCurCfgUrlLbPathOffset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1500),
    )


_SlbCurCfgUrlLbPathOffset_Type.__name__ = "Integer32"
_SlbCurCfgUrlLbPathOffset_Object = MibTableColumn
slbCurCfgUrlLbPathOffset = _SlbCurCfgUrlLbPathOffset_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 1, 1, 2, 2, 1, 7),
    _SlbCurCfgUrlLbPathOffset_Type()
)
slbCurCfgUrlLbPathOffset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbCurCfgUrlLbPathOffset.setStatus("current")


class _SlbCurCfgUrlLbPathDepth_Type(Integer32):
    """Custom type slbCurCfgUrlLbPathDepth based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1500),
    )


_SlbCurCfgUrlLbPathDepth_Type.__name__ = "Integer32"
_SlbCurCfgUrlLbPathDepth_Object = MibTableColumn
slbCurCfgUrlLbPathDepth = _SlbCurCfgUrlLbPathDepth_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 1, 1, 2, 2, 1, 8),
    _SlbCurCfgUrlLbPathDepth_Type()
)
slbCurCfgUrlLbPathDepth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbCurCfgUrlLbPathDepth.setStatus("current")


class _SlbCurCfgUrlLbPathOper_Type(Integer32):
    """Custom type slbCurCfgUrlLbPathOper based on Integer32"""
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
        *(("eq", 1),
          ("gt", 2),
          ("lt", 3),
          ("none", 4))
    )


_SlbCurCfgUrlLbPathOper_Type.__name__ = "Integer32"
_SlbCurCfgUrlLbPathOper_Object = MibTableColumn
slbCurCfgUrlLbPathOper = _SlbCurCfgUrlLbPathOper_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 1, 1, 2, 2, 1, 9),
    _SlbCurCfgUrlLbPathOper_Type()
)
slbCurCfgUrlLbPathOper.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbCurCfgUrlLbPathOper.setStatus("current")
_SlbNewCfgUrlLbPathTable_Object = MibTable
slbNewCfgUrlLbPathTable = _SlbNewCfgUrlLbPathTable_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 1, 1, 2, 3)
)
if mibBuilder.loadTexts:
    slbNewCfgUrlLbPathTable.setStatus("current")
_SlbNewCfgUrlLbPathTableEntry_Object = MibTableRow
slbNewCfgUrlLbPathTableEntry = _SlbNewCfgUrlLbPathTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 1, 1, 2, 3, 1)
)
slbNewCfgUrlLbPathTableEntry.setIndexNames(
    (0, "ALTEON-CHEETAH-LAYER7-MIB", "slbNewCfgUrlLbPathIndex"),
)
if mibBuilder.loadTexts:
    slbNewCfgUrlLbPathTableEntry.setStatus("current")
_SlbNewCfgUrlLbPathIndex_Type = Integer32
_SlbNewCfgUrlLbPathIndex_Object = MibTableColumn
slbNewCfgUrlLbPathIndex = _SlbNewCfgUrlLbPathIndex_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 1, 1, 2, 3, 1, 1),
    _SlbNewCfgUrlLbPathIndex_Type()
)
slbNewCfgUrlLbPathIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbNewCfgUrlLbPathIndex.setStatus("current")


class _SlbNewCfgUrlLbPathString_Type(DisplayString):
    """Custom type slbNewCfgUrlLbPathString based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 96),
    )


_SlbNewCfgUrlLbPathString_Type.__name__ = "DisplayString"
_SlbNewCfgUrlLbPathString_Object = MibTableColumn
slbNewCfgUrlLbPathString = _SlbNewCfgUrlLbPathString_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 1, 1, 2, 3, 1, 2),
    _SlbNewCfgUrlLbPathString_Type()
)
slbNewCfgUrlLbPathString.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    slbNewCfgUrlLbPathString.setStatus("current")


class _SlbNewCfgUrlLbPathDelete_Type(Integer32):
    """Custom type slbNewCfgUrlLbPathDelete based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("delete", 2))
    )


_SlbNewCfgUrlLbPathDelete_Type.__name__ = "Integer32"
_SlbNewCfgUrlLbPathDelete_Object = MibTableColumn
slbNewCfgUrlLbPathDelete = _SlbNewCfgUrlLbPathDelete_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 1, 1, 2, 3, 1, 3),
    _SlbNewCfgUrlLbPathDelete_Type()
)
slbNewCfgUrlLbPathDelete.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    slbNewCfgUrlLbPathDelete.setStatus("current")
_SlbNewCfgUrlLbBwmContract_Type = Integer32
_SlbNewCfgUrlLbBwmContract_Object = MibTableColumn
slbNewCfgUrlLbBwmContract = _SlbNewCfgUrlLbBwmContract_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 1, 1, 2, 3, 1, 4),
    _SlbNewCfgUrlLbBwmContract_Type()
)
slbNewCfgUrlLbBwmContract.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    slbNewCfgUrlLbBwmContract.setStatus("current")


class _SlbNewCfgUrlLbPathHTTPHeader_Type(DisplayString):
    """Custom type slbNewCfgUrlLbPathHTTPHeader based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 48),
    )


_SlbNewCfgUrlLbPathHTTPHeader_Type.__name__ = "DisplayString"
_SlbNewCfgUrlLbPathHTTPHeader_Object = MibTableColumn
slbNewCfgUrlLbPathHTTPHeader = _SlbNewCfgUrlLbPathHTTPHeader_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 1, 1, 2, 3, 1, 5),
    _SlbNewCfgUrlLbPathHTTPHeader_Type()
)
slbNewCfgUrlLbPathHTTPHeader.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    slbNewCfgUrlLbPathHTTPHeader.setStatus("current")


class _SlbNewCfgUrlLbPathHTTPHeaderValue_Type(DisplayString):
    """Custom type slbNewCfgUrlLbPathHTTPHeaderValue based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 48),
    )


_SlbNewCfgUrlLbPathHTTPHeaderValue_Type.__name__ = "DisplayString"
_SlbNewCfgUrlLbPathHTTPHeaderValue_Object = MibTableColumn
slbNewCfgUrlLbPathHTTPHeaderValue = _SlbNewCfgUrlLbPathHTTPHeaderValue_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 1, 1, 2, 3, 1, 6),
    _SlbNewCfgUrlLbPathHTTPHeaderValue_Type()
)
slbNewCfgUrlLbPathHTTPHeaderValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    slbNewCfgUrlLbPathHTTPHeaderValue.setStatus("current")


class _SlbNewCfgUrlLbPathPatternStringType_Type(Integer32):
    """Custom type slbNewCfgUrlLbPathPatternStringType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("ascii", 1),
          ("binary", 2),
          ("none", 3))
    )


_SlbNewCfgUrlLbPathPatternStringType_Type.__name__ = "Integer32"
_SlbNewCfgUrlLbPathPatternStringType_Object = MibTableColumn
slbNewCfgUrlLbPathPatternStringType = _SlbNewCfgUrlLbPathPatternStringType_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 1, 1, 2, 3, 1, 7),
    _SlbNewCfgUrlLbPathPatternStringType_Type()
)
slbNewCfgUrlLbPathPatternStringType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    slbNewCfgUrlLbPathPatternStringType.setStatus("current")


class _SlbNewCfgUrlLbPathOffset_Type(Integer32):
    """Custom type slbNewCfgUrlLbPathOffset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1500),
    )


_SlbNewCfgUrlLbPathOffset_Type.__name__ = "Integer32"
_SlbNewCfgUrlLbPathOffset_Object = MibTableColumn
slbNewCfgUrlLbPathOffset = _SlbNewCfgUrlLbPathOffset_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 1, 1, 2, 3, 1, 8),
    _SlbNewCfgUrlLbPathOffset_Type()
)
slbNewCfgUrlLbPathOffset.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    slbNewCfgUrlLbPathOffset.setStatus("current")


class _SlbNewCfgUrlLbPathDepth_Type(Integer32):
    """Custom type slbNewCfgUrlLbPathDepth based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1500),
    )


_SlbNewCfgUrlLbPathDepth_Type.__name__ = "Integer32"
_SlbNewCfgUrlLbPathDepth_Object = MibTableColumn
slbNewCfgUrlLbPathDepth = _SlbNewCfgUrlLbPathDepth_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 1, 1, 2, 3, 1, 9),
    _SlbNewCfgUrlLbPathDepth_Type()
)
slbNewCfgUrlLbPathDepth.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    slbNewCfgUrlLbPathDepth.setStatus("current")


class _SlbNewCfgUrlLbPathOper_Type(Integer32):
    """Custom type slbNewCfgUrlLbPathOper based on Integer32"""
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
        *(("eq", 1),
          ("gt", 2),
          ("lt", 3),
          ("none", 4))
    )


_SlbNewCfgUrlLbPathOper_Type.__name__ = "Integer32"
_SlbNewCfgUrlLbPathOper_Object = MibTableColumn
slbNewCfgUrlLbPathOper = _SlbNewCfgUrlLbPathOper_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 1, 1, 2, 3, 1, 10),
    _SlbNewCfgUrlLbPathOper_Type()
)
slbNewCfgUrlLbPathOper.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    slbNewCfgUrlLbPathOper.setStatus("current")


class _SlbCurCfgUrlLbErrorMsg_Type(DisplayString):
    """Custom type slbCurCfgUrlLbErrorMsg based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_SlbCurCfgUrlLbErrorMsg_Type.__name__ = "DisplayString"
_SlbCurCfgUrlLbErrorMsg_Object = MibScalar
slbCurCfgUrlLbErrorMsg = _SlbCurCfgUrlLbErrorMsg_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 1, 1, 2, 4),
    _SlbCurCfgUrlLbErrorMsg_Type()
)
slbCurCfgUrlLbErrorMsg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbCurCfgUrlLbErrorMsg.setStatus("current")


class _SlbNewCfgUrlLbErrorMsg_Type(DisplayString):
    """Custom type slbNewCfgUrlLbErrorMsg based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_SlbNewCfgUrlLbErrorMsg_Type.__name__ = "DisplayString"
_SlbNewCfgUrlLbErrorMsg_Object = MibScalar
slbNewCfgUrlLbErrorMsg = _SlbNewCfgUrlLbErrorMsg_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 1, 1, 2, 5),
    _SlbNewCfgUrlLbErrorMsg_Type()
)
slbNewCfgUrlLbErrorMsg.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slbNewCfgUrlLbErrorMsg.setStatus("current")


class _SlbCurCfgUrlLbCaseSensitiveStrMatch_Type(Integer32):
    """Custom type slbCurCfgUrlLbCaseSensitiveStrMatch based on Integer32"""
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


_SlbCurCfgUrlLbCaseSensitiveStrMatch_Type.__name__ = "Integer32"
_SlbCurCfgUrlLbCaseSensitiveStrMatch_Object = MibScalar
slbCurCfgUrlLbCaseSensitiveStrMatch = _SlbCurCfgUrlLbCaseSensitiveStrMatch_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 1, 1, 2, 6),
    _SlbCurCfgUrlLbCaseSensitiveStrMatch_Type()
)
slbCurCfgUrlLbCaseSensitiveStrMatch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbCurCfgUrlLbCaseSensitiveStrMatch.setStatus("current")


class _SlbNewCfgUrlLbCaseSensitiveStrMatch_Type(Integer32):
    """Custom type slbNewCfgUrlLbCaseSensitiveStrMatch based on Integer32"""
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


_SlbNewCfgUrlLbCaseSensitiveStrMatch_Type.__name__ = "Integer32"
_SlbNewCfgUrlLbCaseSensitiveStrMatch_Object = MibScalar
slbNewCfgUrlLbCaseSensitiveStrMatch = _SlbNewCfgUrlLbCaseSensitiveStrMatch_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 1, 1, 2, 7),
    _SlbNewCfgUrlLbCaseSensitiveStrMatch_Type()
)
slbNewCfgUrlLbCaseSensitiveStrMatch.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slbNewCfgUrlLbCaseSensitiveStrMatch.setStatus("current")
_SlbUrlHttpMethods_ObjectIdentity = ObjectIdentity
slbUrlHttpMethods = _SlbUrlHttpMethods_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 1, 1, 3)
)
_SlbUrlHttpMethodsTableMaxSize_Type = Integer32
_SlbUrlHttpMethodsTableMaxSize_Object = MibScalar
slbUrlHttpMethodsTableMaxSize = _SlbUrlHttpMethodsTableMaxSize_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 1, 1, 3, 1),
    _SlbUrlHttpMethodsTableMaxSize_Type()
)
slbUrlHttpMethodsTableMaxSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbUrlHttpMethodsTableMaxSize.setStatus("current")
_SlbCurCfgUrlHttpMethodsTable_Object = MibTable
slbCurCfgUrlHttpMethodsTable = _SlbCurCfgUrlHttpMethodsTable_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 1, 1, 3, 2)
)
if mibBuilder.loadTexts:
    slbCurCfgUrlHttpMethodsTable.setStatus("current")
_SlbCurCfgUrlHttpMethodsTableEntry_Object = MibTableRow
slbCurCfgUrlHttpMethodsTableEntry = _SlbCurCfgUrlHttpMethodsTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 1, 1, 3, 2, 1)
)
slbCurCfgUrlHttpMethodsTableEntry.setIndexNames(
    (0, "ALTEON-CHEETAH-LAYER7-MIB", "slbCurCfgUrlHttpMethodIndex"),
)
if mibBuilder.loadTexts:
    slbCurCfgUrlHttpMethodsTableEntry.setStatus("current")
_SlbCurCfgUrlHttpMethodIndex_Type = Integer32
_SlbCurCfgUrlHttpMethodIndex_Object = MibTableColumn
slbCurCfgUrlHttpMethodIndex = _SlbCurCfgUrlHttpMethodIndex_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 1, 1, 3, 2, 1, 1),
    _SlbCurCfgUrlHttpMethodIndex_Type()
)
slbCurCfgUrlHttpMethodIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbCurCfgUrlHttpMethodIndex.setStatus("current")


class _SlbCurCfgUrlHttpMethodString_Type(DisplayString):
    """Custom type slbCurCfgUrlHttpMethodString based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_SlbCurCfgUrlHttpMethodString_Type.__name__ = "DisplayString"
_SlbCurCfgUrlHttpMethodString_Object = MibTableColumn
slbCurCfgUrlHttpMethodString = _SlbCurCfgUrlHttpMethodString_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 1, 1, 3, 2, 1, 2),
    _SlbCurCfgUrlHttpMethodString_Type()
)
slbCurCfgUrlHttpMethodString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbCurCfgUrlHttpMethodString.setStatus("current")
_SlbNewCfgUrlHttpMethodsTable_Object = MibTable
slbNewCfgUrlHttpMethodsTable = _SlbNewCfgUrlHttpMethodsTable_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 1, 1, 3, 3)
)
if mibBuilder.loadTexts:
    slbNewCfgUrlHttpMethodsTable.setStatus("current")
_SlbNewCfgUrlHttpMethodsTableEntry_Object = MibTableRow
slbNewCfgUrlHttpMethodsTableEntry = _SlbNewCfgUrlHttpMethodsTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 1, 1, 3, 3, 1)
)
slbNewCfgUrlHttpMethodsTableEntry.setIndexNames(
    (0, "ALTEON-CHEETAH-LAYER7-MIB", "slbNewCfgUrlHttpMethodIndex"),
)
if mibBuilder.loadTexts:
    slbNewCfgUrlHttpMethodsTableEntry.setStatus("current")
_SlbNewCfgUrlHttpMethodIndex_Type = Integer32
_SlbNewCfgUrlHttpMethodIndex_Object = MibTableColumn
slbNewCfgUrlHttpMethodIndex = _SlbNewCfgUrlHttpMethodIndex_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 1, 1, 3, 3, 1, 1),
    _SlbNewCfgUrlHttpMethodIndex_Type()
)
slbNewCfgUrlHttpMethodIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbNewCfgUrlHttpMethodIndex.setStatus("current")


class _SlbNewCfgUrlHttpMethodString_Type(DisplayString):
    """Custom type slbNewCfgUrlHttpMethodString based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_SlbNewCfgUrlHttpMethodString_Type.__name__ = "DisplayString"
_SlbNewCfgUrlHttpMethodString_Object = MibTableColumn
slbNewCfgUrlHttpMethodString = _SlbNewCfgUrlHttpMethodString_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 1, 1, 3, 3, 1, 2),
    _SlbNewCfgUrlHttpMethodString_Type()
)
slbNewCfgUrlHttpMethodString.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    slbNewCfgUrlHttpMethodString.setStatus("current")


class _SlbNewCfgUrlHttpMethodDelete_Type(Integer32):
    """Custom type slbNewCfgUrlHttpMethodDelete based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("delete", 2))
    )


_SlbNewCfgUrlHttpMethodDelete_Type.__name__ = "Integer32"
_SlbNewCfgUrlHttpMethodDelete_Object = MibTableColumn
slbNewCfgUrlHttpMethodDelete = _SlbNewCfgUrlHttpMethodDelete_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 1, 1, 3, 3, 1, 3),
    _SlbNewCfgUrlHttpMethodDelete_Type()
)
slbNewCfgUrlHttpMethodDelete.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    slbNewCfgUrlHttpMethodDelete.setStatus("current")
_Layer7GeneralCfg_ObjectIdentity = ObjectIdentity
layer7GeneralCfg = _Layer7GeneralCfg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 1, 2)
)


class _Layer7CurCfgDbindTimeout_Type(Integer32):
    """Custom type layer7CurCfgDbindTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 60),
    )


_Layer7CurCfgDbindTimeout_Type.__name__ = "Integer32"
_Layer7CurCfgDbindTimeout_Object = MibScalar
layer7CurCfgDbindTimeout = _Layer7CurCfgDbindTimeout_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 1, 2, 1),
    _Layer7CurCfgDbindTimeout_Type()
)
layer7CurCfgDbindTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    layer7CurCfgDbindTimeout.setStatus("current")


class _Layer7NewCfgDbindTimeout_Type(Integer32):
    """Custom type layer7NewCfgDbindTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 60),
    )


_Layer7NewCfgDbindTimeout_Type.__name__ = "Integer32"
_Layer7NewCfgDbindTimeout_Object = MibScalar
layer7NewCfgDbindTimeout = _Layer7NewCfgDbindTimeout_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 1, 2, 2),
    _Layer7NewCfgDbindTimeout_Type()
)
layer7NewCfgDbindTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    layer7NewCfgDbindTimeout.setStatus("current")
_SdpCfg_ObjectIdentity = ObjectIdentity
sdpCfg = _SdpCfg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 1, 3)
)
_SlbSdpTableMaxSize_Type = Integer32
_SlbSdpTableMaxSize_Object = MibScalar
slbSdpTableMaxSize = _SlbSdpTableMaxSize_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 1, 3, 1),
    _SlbSdpTableMaxSize_Type()
)
slbSdpTableMaxSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbSdpTableMaxSize.setStatus("current")
_SlbCurCfgSdpTable_Object = MibTable
slbCurCfgSdpTable = _SlbCurCfgSdpTable_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 1, 3, 2)
)
if mibBuilder.loadTexts:
    slbCurCfgSdpTable.setStatus("current")
_SlbCurCfgSdpTableEntry_Object = MibTableRow
slbCurCfgSdpTableEntry = _SlbCurCfgSdpTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 1, 3, 2, 1)
)
slbCurCfgSdpTableEntry.setIndexNames(
    (0, "ALTEON-CHEETAH-LAYER7-MIB", "slbCurCfgSdpIndex"),
)
if mibBuilder.loadTexts:
    slbCurCfgSdpTableEntry.setStatus("current")
_SlbCurCfgSdpIndex_Type = Integer32
_SlbCurCfgSdpIndex_Object = MibTableColumn
slbCurCfgSdpIndex = _SlbCurCfgSdpIndex_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 1, 3, 2, 1, 1),
    _SlbCurCfgSdpIndex_Type()
)
slbCurCfgSdpIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbCurCfgSdpIndex.setStatus("current")
_SlbCurCfgSdpPrivAddr_Type = IpAddress
_SlbCurCfgSdpPrivAddr_Object = MibTableColumn
slbCurCfgSdpPrivAddr = _SlbCurCfgSdpPrivAddr_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 1, 3, 2, 1, 2),
    _SlbCurCfgSdpPrivAddr_Type()
)
slbCurCfgSdpPrivAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbCurCfgSdpPrivAddr.setStatus("current")
_SlbCurCfgSdpPublicAddr_Type = IpAddress
_SlbCurCfgSdpPublicAddr_Object = MibTableColumn
slbCurCfgSdpPublicAddr = _SlbCurCfgSdpPublicAddr_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 1, 3, 2, 1, 3),
    _SlbCurCfgSdpPublicAddr_Type()
)
slbCurCfgSdpPublicAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbCurCfgSdpPublicAddr.setStatus("current")
_SlbNewCfgSdpTable_Object = MibTable
slbNewCfgSdpTable = _SlbNewCfgSdpTable_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 1, 3, 3)
)
if mibBuilder.loadTexts:
    slbNewCfgSdpTable.setStatus("current")
_SlbNewCfgSdpTableEntry_Object = MibTableRow
slbNewCfgSdpTableEntry = _SlbNewCfgSdpTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 1, 3, 3, 1)
)
slbNewCfgSdpTableEntry.setIndexNames(
    (0, "ALTEON-CHEETAH-LAYER7-MIB", "slbCurCfgSdpIndex"),
)
if mibBuilder.loadTexts:
    slbNewCfgSdpTableEntry.setStatus("current")
_SlbNewCfgSdpIndex_Type = Integer32
_SlbNewCfgSdpIndex_Object = MibTableColumn
slbNewCfgSdpIndex = _SlbNewCfgSdpIndex_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 1, 3, 3, 1, 1),
    _SlbNewCfgSdpIndex_Type()
)
slbNewCfgSdpIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbNewCfgSdpIndex.setStatus("current")
_SlbNewCfgSdpPrivAddr_Type = IpAddress
_SlbNewCfgSdpPrivAddr_Object = MibTableColumn
slbNewCfgSdpPrivAddr = _SlbNewCfgSdpPrivAddr_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 1, 3, 3, 1, 2),
    _SlbNewCfgSdpPrivAddr_Type()
)
slbNewCfgSdpPrivAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    slbNewCfgSdpPrivAddr.setStatus("current")
_SlbNewCfgSdpPublicAddr_Type = IpAddress
_SlbNewCfgSdpPublicAddr_Object = MibTableColumn
slbNewCfgSdpPublicAddr = _SlbNewCfgSdpPublicAddr_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 1, 3, 3, 1, 3),
    _SlbNewCfgSdpPublicAddr_Type()
)
slbNewCfgSdpPublicAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    slbNewCfgSdpPublicAddr.setStatus("current")


class _SlbNewCfgSdpDelete_Type(Integer32):
    """Custom type slbNewCfgSdpDelete based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("delete", 2))
    )


_SlbNewCfgSdpDelete_Type.__name__ = "Integer32"
_SlbNewCfgSdpDelete_Object = MibTableColumn
slbNewCfgSdpDelete = _SlbNewCfgSdpDelete_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 1, 3, 3, 1, 4),
    _SlbNewCfgSdpDelete_Type()
)
slbNewCfgSdpDelete.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    slbNewCfgSdpDelete.setStatus("current")
_Layer7Stats_ObjectIdentity = ObjectIdentity
layer7Stats = _Layer7Stats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 2)
)
_UrlStats_ObjectIdentity = ObjectIdentity
urlStats = _UrlStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 2, 1)
)
_UrlRedirStats_ObjectIdentity = ObjectIdentity
urlRedirStats = _UrlRedirStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 2, 1, 1)
)
_UrlStatRedRedirs_Type = Counter32
_UrlStatRedRedirs_Object = MibScalar
urlStatRedRedirs = _UrlStatRedRedirs_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 2, 1, 1, 1),
    _UrlStatRedRedirs_Type()
)
urlStatRedRedirs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    urlStatRedRedirs.setStatus("current")
_UrlStatRedOrigSrvs_Type = Counter32
_UrlStatRedOrigSrvs_Object = MibScalar
urlStatRedOrigSrvs = _UrlStatRedOrigSrvs_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 2, 1, 1, 2),
    _UrlStatRedOrigSrvs_Type()
)
urlStatRedOrigSrvs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    urlStatRedOrigSrvs.setStatus("current")
_UrlStatRedNonGets_Type = Counter32
_UrlStatRedNonGets_Object = MibScalar
urlStatRedNonGets = _UrlStatRedNonGets_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 2, 1, 1, 3),
    _UrlStatRedNonGets_Type()
)
urlStatRedNonGets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    urlStatRedNonGets.setStatus("current")
_UrlStatRedCookie_Type = Counter32
_UrlStatRedCookie_Object = MibScalar
urlStatRedCookie = _UrlStatRedCookie_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 2, 1, 1, 4),
    _UrlStatRedCookie_Type()
)
urlStatRedCookie.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    urlStatRedCookie.setStatus("current")
_UrlStatRedNoCache_Type = Counter32
_UrlStatRedNoCache_Object = MibScalar
urlStatRedNoCache = _UrlStatRedNoCache_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 2, 1, 1, 5),
    _UrlStatRedNoCache_Type()
)
urlStatRedNoCache.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    urlStatRedNoCache.setStatus("current")
_UrlStatRedStraightOrigSrvs_Type = Counter32
_UrlStatRedStraightOrigSrvs_Object = MibScalar
urlStatRedStraightOrigSrvs = _UrlStatRedStraightOrigSrvs_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 2, 1, 1, 6),
    _UrlStatRedStraightOrigSrvs_Type()
)
urlStatRedStraightOrigSrvs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    urlStatRedStraightOrigSrvs.setStatus("current")
_UrlStatRedRtspCacheSrvs_Type = Counter32
_UrlStatRedRtspCacheSrvs_Object = MibScalar
urlStatRedRtspCacheSrvs = _UrlStatRedRtspCacheSrvs_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 2, 1, 1, 7),
    _UrlStatRedRtspCacheSrvs_Type()
)
urlStatRedRtspCacheSrvs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    urlStatRedRtspCacheSrvs.setStatus("current")
_UrlStatRedRtspOrigSrvs_Type = Counter32
_UrlStatRedRtspOrigSrvs_Object = MibScalar
urlStatRedRtspOrigSrvs = _UrlStatRedRtspOrigSrvs_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 2, 1, 1, 8),
    _UrlStatRedRtspOrigSrvs_Type()
)
urlStatRedRtspOrigSrvs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    urlStatRedRtspOrigSrvs.setStatus("current")
_UrlSlbStats_ObjectIdentity = ObjectIdentity
urlSlbStats = _UrlSlbStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 2, 1, 2)
)
_UrlStatSlbPathTable_Object = MibTable
urlStatSlbPathTable = _UrlStatSlbPathTable_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 2, 1, 2, 1)
)
if mibBuilder.loadTexts:
    urlStatSlbPathTable.setStatus("current")
_UrlStatSlbPathTableEntry_Object = MibTableRow
urlStatSlbPathTableEntry = _UrlStatSlbPathTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 2, 1, 2, 1, 1)
)
urlStatSlbPathTableEntry.setIndexNames(
    (0, "ALTEON-CHEETAH-LAYER7-MIB", "urlStatSlbPathIndex"),
)
if mibBuilder.loadTexts:
    urlStatSlbPathTableEntry.setStatus("current")
_UrlStatSlbPathIndex_Type = Integer32
_UrlStatSlbPathIndex_Object = MibTableColumn
urlStatSlbPathIndex = _UrlStatSlbPathIndex_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 2, 1, 2, 1, 1, 1),
    _UrlStatSlbPathIndex_Type()
)
urlStatSlbPathIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    urlStatSlbPathIndex.setStatus("current")
_UrlStatSlbPathHits_Type = Counter32
_UrlStatSlbPathHits_Object = MibTableColumn
urlStatSlbPathHits = _UrlStatSlbPathHits_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 2, 1, 2, 1, 1, 2),
    _UrlStatSlbPathHits_Type()
)
urlStatSlbPathHits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    urlStatSlbPathHits.setStatus("current")
_UrlMaintStats_ObjectIdentity = ObjectIdentity
urlMaintStats = _UrlMaintStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 2, 1, 3)
)
_UrlMaintStatClientReset_Type = Counter32
_UrlMaintStatClientReset_Object = MibScalar
urlMaintStatClientReset = _UrlMaintStatClientReset_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 2, 1, 3, 1),
    _UrlMaintStatClientReset_Type()
)
urlMaintStatClientReset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    urlMaintStatClientReset.setStatus("current")
_UrlMaintStatServerReset_Type = Counter32
_UrlMaintStatServerReset_Object = MibScalar
urlMaintStatServerReset = _UrlMaintStatServerReset_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 2, 1, 3, 2),
    _UrlMaintStatServerReset_Type()
)
urlMaintStatServerReset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    urlMaintStatServerReset.setStatus("current")
_UrlMaintStatConnSplicing_Type = Counter32
_UrlMaintStatConnSplicing_Object = MibScalar
urlMaintStatConnSplicing = _UrlMaintStatConnSplicing_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 2, 1, 3, 3),
    _UrlMaintStatConnSplicing_Type()
)
urlMaintStatConnSplicing.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    urlMaintStatConnSplicing.setStatus("current")
_UrlMaintStatHalfOpens_Type = Gauge32
_UrlMaintStatHalfOpens_Object = MibScalar
urlMaintStatHalfOpens = _UrlMaintStatHalfOpens_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 2, 1, 3, 4),
    _UrlMaintStatHalfOpens_Type()
)
urlMaintStatHalfOpens.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    urlMaintStatHalfOpens.setStatus("current")
_UrlMaintStatSwitchRetries_Type = Counter32
_UrlMaintStatSwitchRetries_Object = MibScalar
urlMaintStatSwitchRetries = _UrlMaintStatSwitchRetries_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 2, 1, 3, 5),
    _UrlMaintStatSwitchRetries_Type()
)
urlMaintStatSwitchRetries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    urlMaintStatSwitchRetries.setStatus("current")
_UrlMaintStatRandomEarlyDrops_Type = Counter32
_UrlMaintStatRandomEarlyDrops_Object = MibScalar
urlMaintStatRandomEarlyDrops = _UrlMaintStatRandomEarlyDrops_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 2, 1, 3, 6),
    _UrlMaintStatRandomEarlyDrops_Type()
)
urlMaintStatRandomEarlyDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    urlMaintStatRandomEarlyDrops.setStatus("current")
_UrlMaintStatReqTooLong_Type = Counter32
_UrlMaintStatReqTooLong_Object = MibScalar
urlMaintStatReqTooLong = _UrlMaintStatReqTooLong_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 2, 1, 3, 7),
    _UrlMaintStatReqTooLong_Type()
)
urlMaintStatReqTooLong.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    urlMaintStatReqTooLong.setStatus("current")
_UrlMaintStatInvalidHandshakes_Type = Counter32
_UrlMaintStatInvalidHandshakes_Object = MibScalar
urlMaintStatInvalidHandshakes = _UrlMaintStatInvalidHandshakes_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 2, 1, 3, 8),
    _UrlMaintStatInvalidHandshakes_Type()
)
urlMaintStatInvalidHandshakes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    urlMaintStatInvalidHandshakes.setStatus("current")
_UrlMaintStatCurSPMemUnits_Type = Gauge32
_UrlMaintStatCurSPMemUnits_Object = MibScalar
urlMaintStatCurSPMemUnits = _UrlMaintStatCurSPMemUnits_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 2, 1, 3, 9),
    _UrlMaintStatCurSPMemUnits_Type()
)
urlMaintStatCurSPMemUnits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    urlMaintStatCurSPMemUnits.setStatus("current")
_UrlMaintStatCurSEQBufEntries_Type = Gauge32
_UrlMaintStatCurSEQBufEntries_Object = MibScalar
urlMaintStatCurSEQBufEntries = _UrlMaintStatCurSEQBufEntries_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 2, 1, 3, 10),
    _UrlMaintStatCurSEQBufEntries_Type()
)
urlMaintStatCurSEQBufEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    urlMaintStatCurSEQBufEntries.setStatus("current")
_UrlMaintStatHighestSEQBufEntries_Type = Counter32
_UrlMaintStatHighestSEQBufEntries_Object = MibScalar
urlMaintStatHighestSEQBufEntries = _UrlMaintStatHighestSEQBufEntries_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 2, 1, 3, 11),
    _UrlMaintStatHighestSEQBufEntries_Type()
)
urlMaintStatHighestSEQBufEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    urlMaintStatHighestSEQBufEntries.setStatus("current")
_UrlMaintStatCurDataBufUse_Type = Gauge32
_UrlMaintStatCurDataBufUse_Object = MibScalar
urlMaintStatCurDataBufUse = _UrlMaintStatCurDataBufUse_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 2, 1, 3, 12),
    _UrlMaintStatCurDataBufUse_Type()
)
urlMaintStatCurDataBufUse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    urlMaintStatCurDataBufUse.setStatus("current")
_UrlMaintStatHighestDataBufUse_Type = Counter32
_UrlMaintStatHighestDataBufUse_Object = MibScalar
urlMaintStatHighestDataBufUse = _UrlMaintStatHighestDataBufUse_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 2, 1, 3, 13),
    _UrlMaintStatHighestDataBufUse_Type()
)
urlMaintStatHighestDataBufUse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    urlMaintStatHighestDataBufUse.setStatus("current")
_UrlMaintStatCurSPBufEntries_Type = Gauge32
_UrlMaintStatCurSPBufEntries_Object = MibScalar
urlMaintStatCurSPBufEntries = _UrlMaintStatCurSPBufEntries_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 2, 1, 3, 14),
    _UrlMaintStatCurSPBufEntries_Type()
)
urlMaintStatCurSPBufEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    urlMaintStatCurSPBufEntries.setStatus("current")
_UrlMaintStatHighestSPBufEntries_Type = Counter32
_UrlMaintStatHighestSPBufEntries_Object = MibScalar
urlMaintStatHighestSPBufEntries = _UrlMaintStatHighestSPBufEntries_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 2, 1, 3, 15),
    _UrlMaintStatHighestSPBufEntries_Type()
)
urlMaintStatHighestSPBufEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    urlMaintStatHighestSPBufEntries.setStatus("current")
_UrlMaintStatTotalNonZeroSEQAlloc_Type = Counter32
_UrlMaintStatTotalNonZeroSEQAlloc_Object = MibScalar
urlMaintStatTotalNonZeroSEQAlloc = _UrlMaintStatTotalNonZeroSEQAlloc_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 2, 1, 3, 16),
    _UrlMaintStatTotalNonZeroSEQAlloc_Type()
)
urlMaintStatTotalNonZeroSEQAlloc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    urlMaintStatTotalNonZeroSEQAlloc.setStatus("current")
_UrlMaintStatTotalSEQBufAllocs_Type = Counter32
_UrlMaintStatTotalSEQBufAllocs_Object = MibScalar
urlMaintStatTotalSEQBufAllocs = _UrlMaintStatTotalSEQBufAllocs_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 2, 1, 3, 17),
    _UrlMaintStatTotalSEQBufAllocs_Type()
)
urlMaintStatTotalSEQBufAllocs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    urlMaintStatTotalSEQBufAllocs.setStatus("current")
_UrlMaintStatTotalSEQBufFrees_Type = Counter32
_UrlMaintStatTotalSEQBufFrees_Object = MibScalar
urlMaintStatTotalSEQBufFrees = _UrlMaintStatTotalSEQBufFrees_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 2, 1, 3, 18),
    _UrlMaintStatTotalSEQBufFrees_Type()
)
urlMaintStatTotalSEQBufFrees.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    urlMaintStatTotalSEQBufFrees.setStatus("current")
_UrlMaintStatTotalDataBufAllocs_Type = Counter32
_UrlMaintStatTotalDataBufAllocs_Object = MibScalar
urlMaintStatTotalDataBufAllocs = _UrlMaintStatTotalDataBufAllocs_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 2, 1, 3, 19),
    _UrlMaintStatTotalDataBufAllocs_Type()
)
urlMaintStatTotalDataBufAllocs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    urlMaintStatTotalDataBufAllocs.setStatus("current")
_UrlMaintStatTotalDataBufFrees_Type = Counter32
_UrlMaintStatTotalDataBufFrees_Object = MibScalar
urlMaintStatTotalDataBufFrees = _UrlMaintStatTotalDataBufFrees_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 2, 1, 3, 20),
    _UrlMaintStatTotalDataBufFrees_Type()
)
urlMaintStatTotalDataBufFrees.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    urlMaintStatTotalDataBufFrees.setStatus("current")
_UrlMaintStatSeqBufAllocFails_Type = Counter32
_UrlMaintStatSeqBufAllocFails_Object = MibScalar
urlMaintStatSeqBufAllocFails = _UrlMaintStatSeqBufAllocFails_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 2, 1, 3, 21),
    _UrlMaintStatSeqBufAllocFails_Type()
)
urlMaintStatSeqBufAllocFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    urlMaintStatSeqBufAllocFails.setStatus("current")
_UrlMaintStatUBufAllocFails_Type = Counter32
_UrlMaintStatUBufAllocFails_Object = MibScalar
urlMaintStatUBufAllocFails = _UrlMaintStatUBufAllocFails_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 2, 1, 3, 22),
    _UrlMaintStatUBufAllocFails_Type()
)
urlMaintStatUBufAllocFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    urlMaintStatUBufAllocFails.setStatus("current")
_UrlMaintStatMaxSessPerBucket_Type = Counter32
_UrlMaintStatMaxSessPerBucket_Object = MibScalar
urlMaintStatMaxSessPerBucket = _UrlMaintStatMaxSessPerBucket_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 2, 1, 3, 23),
    _UrlMaintStatMaxSessPerBucket_Type()
)
urlMaintStatMaxSessPerBucket.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    urlMaintStatMaxSessPerBucket.setStatus("current")
_UrlMaintStatMaxFramesPerSess_Type = Counter32
_UrlMaintStatMaxFramesPerSess_Object = MibScalar
urlMaintStatMaxFramesPerSess = _UrlMaintStatMaxFramesPerSess_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 2, 1, 3, 24),
    _UrlMaintStatMaxFramesPerSess_Type()
)
urlMaintStatMaxFramesPerSess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    urlMaintStatMaxFramesPerSess.setStatus("current")
_UrlMaintStatMaxBytesBuffered_Type = Counter32
_UrlMaintStatMaxBytesBuffered_Object = MibScalar
urlMaintStatMaxBytesBuffered = _UrlMaintStatMaxBytesBuffered_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 2, 1, 3, 25),
    _UrlMaintStatMaxBytesBuffered_Type()
)
urlMaintStatMaxBytesBuffered.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    urlMaintStatMaxBytesBuffered.setStatus("current")
_UrlMaintStatInvalidMethods_Type = Counter32
_UrlMaintStatInvalidMethods_Object = MibScalar
urlMaintStatInvalidMethods = _UrlMaintStatInvalidMethods_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 2, 1, 3, 26),
    _UrlMaintStatInvalidMethods_Type()
)
urlMaintStatInvalidMethods.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    urlMaintStatInvalidMethods.setStatus("current")
_UrlMaintStatAgedSessions_Type = Counter32
_UrlMaintStatAgedSessions_Object = MibScalar
urlMaintStatAgedSessions = _UrlMaintStatAgedSessions_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 2, 1, 3, 27),
    _UrlMaintStatAgedSessions_Type()
)
urlMaintStatAgedSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    urlMaintStatAgedSessions.setStatus("current")
_UrlMaintStatLowestSPMemUnits_Type = Gauge32
_UrlMaintStatLowestSPMemUnits_Object = MibScalar
urlMaintStatLowestSPMemUnits = _UrlMaintStatLowestSPMemUnits_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 2, 1, 3, 28),
    _UrlMaintStatLowestSPMemUnits_Type()
)
urlMaintStatLowestSPMemUnits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    urlMaintStatLowestSPMemUnits.setStatus("current")
_UrlSpMaintStatsTable_Object = MibTable
urlSpMaintStatsTable = _UrlSpMaintStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 2, 1, 4)
)
if mibBuilder.loadTexts:
    urlSpMaintStatsTable.setStatus("current")
_UrlSpMaintStatsTableEntry_Object = MibTableRow
urlSpMaintStatsTableEntry = _UrlSpMaintStatsTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 2, 1, 4, 1)
)
urlSpMaintStatsTableEntry.setIndexNames(
    (0, "ALTEON-CHEETAH-LAYER7-MIB", "urlSpMaintStatsSpIndex"),
)
if mibBuilder.loadTexts:
    urlSpMaintStatsTableEntry.setStatus("current")
_UrlSpMaintStatsSpIndex_Type = Integer32
_UrlSpMaintStatsSpIndex_Object = MibTableColumn
urlSpMaintStatsSpIndex = _UrlSpMaintStatsSpIndex_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 2, 1, 4, 1, 1),
    _UrlSpMaintStatsSpIndex_Type()
)
urlSpMaintStatsSpIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    urlSpMaintStatsSpIndex.setStatus("current")
_UrlSpMaintStatsCurMemUnits_Type = Gauge32
_UrlSpMaintStatsCurMemUnits_Object = MibTableColumn
urlSpMaintStatsCurMemUnits = _UrlSpMaintStatsCurMemUnits_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 2, 1, 4, 1, 2),
    _UrlSpMaintStatsCurMemUnits_Type()
)
urlSpMaintStatsCurMemUnits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    urlSpMaintStatsCurMemUnits.setStatus("current")
_UrlSpMaintStatsLowestMemUnits_Type = Gauge32
_UrlSpMaintStatsLowestMemUnits_Object = MibTableColumn
urlSpMaintStatsLowestMemUnits = _UrlSpMaintStatsLowestMemUnits_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 2, 1, 4, 1, 3),
    _UrlSpMaintStatsLowestMemUnits_Type()
)
urlSpMaintStatsLowestMemUnits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    urlSpMaintStatsLowestMemUnits.setStatus("current")
_ConnPoolingStats_ObjectIdentity = ObjectIdentity
connPoolingStats = _ConnPoolingStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 2, 2)
)
_CurrOpenedServerConns_Type = Counter32
_CurrOpenedServerConns_Object = MibScalar
currOpenedServerConns = _CurrOpenedServerConns_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 2, 2, 1),
    _CurrOpenedServerConns_Type()
)
currOpenedServerConns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    currOpenedServerConns.setStatus("current")
_ActiveServerConns_Type = Gauge32
_ActiveServerConns_Object = MibScalar
activeServerConns = _ActiveServerConns_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 2, 2, 2),
    _ActiveServerConns_Type()
)
activeServerConns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    activeServerConns.setStatus("current")
_AvailServerConns_Type = Gauge32
_AvailServerConns_Object = MibScalar
availServerConns = _AvailServerConns_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 2, 2, 3),
    _AvailServerConns_Type()
)
availServerConns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    availServerConns.setStatus("current")
_AgedOutClientConns_Type = Counter32
_AgedOutClientConns_Object = MibScalar
agedOutClientConns = _AgedOutClientConns_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 2, 2, 4),
    _AgedOutClientConns_Type()
)
agedOutClientConns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agedOutClientConns.setStatus("current")
_AgedOutServerConns_Type = Counter32
_AgedOutServerConns_Object = MibScalar
agedOutServerConns = _AgedOutServerConns_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 2, 2, 5),
    _AgedOutServerConns_Type()
)
agedOutServerConns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agedOutServerConns.setStatus("current")
_Layer7Info_ObjectIdentity = ObjectIdentity
layer7Info = _Layer7Info_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 3)
)
_SlbParsing_ObjectIdentity = ObjectIdentity
slbParsing = _SlbParsing_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 3, 1)
)


class _SlbParsingString_Type(DisplayString):
    """Custom type slbParsingString based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 22),
    )


_SlbParsingString_Type.__name__ = "DisplayString"
_SlbParsingString_Object = MibScalar
slbParsingString = _SlbParsingString_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 3, 1, 1),
    _SlbParsingString_Type()
)
slbParsingString.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slbParsingString.setStatus("current")
_SlbParsingVip_Type = IpAddress
_SlbParsingVip_Object = MibScalar
slbParsingVip = _SlbParsingVip_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 3, 1, 2),
    _SlbParsingVip_Type()
)
slbParsingVip.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbParsingVip.setStatus("current")
_SlbParsingRip_Type = IpAddress
_SlbParsingRip_Object = MibScalar
slbParsingRip = _SlbParsingRip_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 3, 1, 3),
    _SlbParsingRip_Type()
)
slbParsingRip.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbParsingRip.setStatus("current")


class _SlbParsingRport_Type(Integer32):
    """Custom type slbParsingRport based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_SlbParsingRport_Type.__name__ = "Integer32"
_SlbParsingRport_Object = MibScalar
slbParsingRport = _SlbParsingRport_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 3, 1, 4),
    _SlbParsingRport_Type()
)
slbParsingRport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slbParsingRport.setStatus("current")
_Layer7Oper_ObjectIdentity = ObjectIdentity
layer7Oper = _Layer7Oper_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1872, 2, 5, 5, 4)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ALTEON-CHEETAH-LAYER7-MIB",
    **{"layer7": layer7,
       "layer7Configs": layer7Configs,
       "urlCfg": urlCfg,
       "slbUrlRedir": slbUrlRedir,
       "slbCurCfgUrlRedirNonGetOrigSrv": slbCurCfgUrlRedirNonGetOrigSrv,
       "slbNewCfgUrlRedirNonGetOrigSrv": slbNewCfgUrlRedirNonGetOrigSrv,
       "slbCurCfgUrlRedirCookieOrigSrv": slbCurCfgUrlRedirCookieOrigSrv,
       "slbNewCfgUrlRedirCookieOrigSrv": slbNewCfgUrlRedirCookieOrigSrv,
       "slbCurCfgUrlRedirNoCacheOrigSrv": slbCurCfgUrlRedirNoCacheOrigSrv,
       "slbNewCfgUrlRedirNoCacheOrigSrv": slbNewCfgUrlRedirNoCacheOrigSrv,
       "slbCurCfgUrlRedirUriHashLength": slbCurCfgUrlRedirUriHashLength,
       "slbNewCfgUrlRedirUriHashLength": slbNewCfgUrlRedirUriHashLength,
       "slbCurCfgUrlRedirHeader": slbCurCfgUrlRedirHeader,
       "slbNewCfgUrlRedirHeader": slbNewCfgUrlRedirHeader,
       "slbCurCfgUrlRedirHeaderName": slbCurCfgUrlRedirHeaderName,
       "slbNewCfgUrlRedirHeaderName": slbNewCfgUrlRedirHeaderName,
       "slbUrlBalance": slbUrlBalance,
       "slbUrlLbPathTableMaxSize": slbUrlLbPathTableMaxSize,
       "slbCurCfgUrlLbPathTable": slbCurCfgUrlLbPathTable,
       "slbCurCfgUrlLbPathTableEntry": slbCurCfgUrlLbPathTableEntry,
       "slbCurCfgUrlLbPathIndex": slbCurCfgUrlLbPathIndex,
       "slbCurCfgUrlLbPathString": slbCurCfgUrlLbPathString,
       "slbCurCfgUrlLbBwmContract": slbCurCfgUrlLbBwmContract,
       "slbCurCfgUrlLbPathHTTPHeader": slbCurCfgUrlLbPathHTTPHeader,
       "slbCurCfgUrlLbPathHTTPHeaderValue": slbCurCfgUrlLbPathHTTPHeaderValue,
       "slbCurCfgUrlLbPathPatternStringType": slbCurCfgUrlLbPathPatternStringType,
       "slbCurCfgUrlLbPathOffset": slbCurCfgUrlLbPathOffset,
       "slbCurCfgUrlLbPathDepth": slbCurCfgUrlLbPathDepth,
       "slbCurCfgUrlLbPathOper": slbCurCfgUrlLbPathOper,
       "slbNewCfgUrlLbPathTable": slbNewCfgUrlLbPathTable,
       "slbNewCfgUrlLbPathTableEntry": slbNewCfgUrlLbPathTableEntry,
       "slbNewCfgUrlLbPathIndex": slbNewCfgUrlLbPathIndex,
       "slbNewCfgUrlLbPathString": slbNewCfgUrlLbPathString,
       "slbNewCfgUrlLbPathDelete": slbNewCfgUrlLbPathDelete,
       "slbNewCfgUrlLbBwmContract": slbNewCfgUrlLbBwmContract,
       "slbNewCfgUrlLbPathHTTPHeader": slbNewCfgUrlLbPathHTTPHeader,
       "slbNewCfgUrlLbPathHTTPHeaderValue": slbNewCfgUrlLbPathHTTPHeaderValue,
       "slbNewCfgUrlLbPathPatternStringType": slbNewCfgUrlLbPathPatternStringType,
       "slbNewCfgUrlLbPathOffset": slbNewCfgUrlLbPathOffset,
       "slbNewCfgUrlLbPathDepth": slbNewCfgUrlLbPathDepth,
       "slbNewCfgUrlLbPathOper": slbNewCfgUrlLbPathOper,
       "slbCurCfgUrlLbErrorMsg": slbCurCfgUrlLbErrorMsg,
       "slbNewCfgUrlLbErrorMsg": slbNewCfgUrlLbErrorMsg,
       "slbCurCfgUrlLbCaseSensitiveStrMatch": slbCurCfgUrlLbCaseSensitiveStrMatch,
       "slbNewCfgUrlLbCaseSensitiveStrMatch": slbNewCfgUrlLbCaseSensitiveStrMatch,
       "slbUrlHttpMethods": slbUrlHttpMethods,
       "slbUrlHttpMethodsTableMaxSize": slbUrlHttpMethodsTableMaxSize,
       "slbCurCfgUrlHttpMethodsTable": slbCurCfgUrlHttpMethodsTable,
       "slbCurCfgUrlHttpMethodsTableEntry": slbCurCfgUrlHttpMethodsTableEntry,
       "slbCurCfgUrlHttpMethodIndex": slbCurCfgUrlHttpMethodIndex,
       "slbCurCfgUrlHttpMethodString": slbCurCfgUrlHttpMethodString,
       "slbNewCfgUrlHttpMethodsTable": slbNewCfgUrlHttpMethodsTable,
       "slbNewCfgUrlHttpMethodsTableEntry": slbNewCfgUrlHttpMethodsTableEntry,
       "slbNewCfgUrlHttpMethodIndex": slbNewCfgUrlHttpMethodIndex,
       "slbNewCfgUrlHttpMethodString": slbNewCfgUrlHttpMethodString,
       "slbNewCfgUrlHttpMethodDelete": slbNewCfgUrlHttpMethodDelete,
       "layer7GeneralCfg": layer7GeneralCfg,
       "layer7CurCfgDbindTimeout": layer7CurCfgDbindTimeout,
       "layer7NewCfgDbindTimeout": layer7NewCfgDbindTimeout,
       "sdpCfg": sdpCfg,
       "slbSdpTableMaxSize": slbSdpTableMaxSize,
       "slbCurCfgSdpTable": slbCurCfgSdpTable,
       "slbCurCfgSdpTableEntry": slbCurCfgSdpTableEntry,
       "slbCurCfgSdpIndex": slbCurCfgSdpIndex,
       "slbCurCfgSdpPrivAddr": slbCurCfgSdpPrivAddr,
       "slbCurCfgSdpPublicAddr": slbCurCfgSdpPublicAddr,
       "slbNewCfgSdpTable": slbNewCfgSdpTable,
       "slbNewCfgSdpTableEntry": slbNewCfgSdpTableEntry,
       "slbNewCfgSdpIndex": slbNewCfgSdpIndex,
       "slbNewCfgSdpPrivAddr": slbNewCfgSdpPrivAddr,
       "slbNewCfgSdpPublicAddr": slbNewCfgSdpPublicAddr,
       "slbNewCfgSdpDelete": slbNewCfgSdpDelete,
       "layer7Stats": layer7Stats,
       "urlStats": urlStats,
       "urlRedirStats": urlRedirStats,
       "urlStatRedRedirs": urlStatRedRedirs,
       "urlStatRedOrigSrvs": urlStatRedOrigSrvs,
       "urlStatRedNonGets": urlStatRedNonGets,
       "urlStatRedCookie": urlStatRedCookie,
       "urlStatRedNoCache": urlStatRedNoCache,
       "urlStatRedStraightOrigSrvs": urlStatRedStraightOrigSrvs,
       "urlStatRedRtspCacheSrvs": urlStatRedRtspCacheSrvs,
       "urlStatRedRtspOrigSrvs": urlStatRedRtspOrigSrvs,
       "urlSlbStats": urlSlbStats,
       "urlStatSlbPathTable": urlStatSlbPathTable,
       "urlStatSlbPathTableEntry": urlStatSlbPathTableEntry,
       "urlStatSlbPathIndex": urlStatSlbPathIndex,
       "urlStatSlbPathHits": urlStatSlbPathHits,
       "urlMaintStats": urlMaintStats,
       "urlMaintStatClientReset": urlMaintStatClientReset,
       "urlMaintStatServerReset": urlMaintStatServerReset,
       "urlMaintStatConnSplicing": urlMaintStatConnSplicing,
       "urlMaintStatHalfOpens": urlMaintStatHalfOpens,
       "urlMaintStatSwitchRetries": urlMaintStatSwitchRetries,
       "urlMaintStatRandomEarlyDrops": urlMaintStatRandomEarlyDrops,
       "urlMaintStatReqTooLong": urlMaintStatReqTooLong,
       "urlMaintStatInvalidHandshakes": urlMaintStatInvalidHandshakes,
       "urlMaintStatCurSPMemUnits": urlMaintStatCurSPMemUnits,
       "urlMaintStatCurSEQBufEntries": urlMaintStatCurSEQBufEntries,
       "urlMaintStatHighestSEQBufEntries": urlMaintStatHighestSEQBufEntries,
       "urlMaintStatCurDataBufUse": urlMaintStatCurDataBufUse,
       "urlMaintStatHighestDataBufUse": urlMaintStatHighestDataBufUse,
       "urlMaintStatCurSPBufEntries": urlMaintStatCurSPBufEntries,
       "urlMaintStatHighestSPBufEntries": urlMaintStatHighestSPBufEntries,
       "urlMaintStatTotalNonZeroSEQAlloc": urlMaintStatTotalNonZeroSEQAlloc,
       "urlMaintStatTotalSEQBufAllocs": urlMaintStatTotalSEQBufAllocs,
       "urlMaintStatTotalSEQBufFrees": urlMaintStatTotalSEQBufFrees,
       "urlMaintStatTotalDataBufAllocs": urlMaintStatTotalDataBufAllocs,
       "urlMaintStatTotalDataBufFrees": urlMaintStatTotalDataBufFrees,
       "urlMaintStatSeqBufAllocFails": urlMaintStatSeqBufAllocFails,
       "urlMaintStatUBufAllocFails": urlMaintStatUBufAllocFails,
       "urlMaintStatMaxSessPerBucket": urlMaintStatMaxSessPerBucket,
       "urlMaintStatMaxFramesPerSess": urlMaintStatMaxFramesPerSess,
       "urlMaintStatMaxBytesBuffered": urlMaintStatMaxBytesBuffered,
       "urlMaintStatInvalidMethods": urlMaintStatInvalidMethods,
       "urlMaintStatAgedSessions": urlMaintStatAgedSessions,
       "urlMaintStatLowestSPMemUnits": urlMaintStatLowestSPMemUnits,
       "urlSpMaintStatsTable": urlSpMaintStatsTable,
       "urlSpMaintStatsTableEntry": urlSpMaintStatsTableEntry,
       "urlSpMaintStatsSpIndex": urlSpMaintStatsSpIndex,
       "urlSpMaintStatsCurMemUnits": urlSpMaintStatsCurMemUnits,
       "urlSpMaintStatsLowestMemUnits": urlSpMaintStatsLowestMemUnits,
       "connPoolingStats": connPoolingStats,
       "currOpenedServerConns": currOpenedServerConns,
       "activeServerConns": activeServerConns,
       "availServerConns": availServerConns,
       "agedOutClientConns": agedOutClientConns,
       "agedOutServerConns": agedOutServerConns,
       "layer7Info": layer7Info,
       "slbParsing": slbParsing,
       "slbParsingString": slbParsingString,
       "slbParsingVip": slbParsingVip,
       "slbParsingRip": slbParsingRip,
       "slbParsingRport": slbParsingRport,
       "layer7Oper": layer7Oper}
)
