# SNMP MIB module (HH3C-EVC-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\comware\HH3C-EVC-MIB

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

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

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

hh3cEvc = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 106)
)
if mibBuilder.loadTexts:
    hh3cEvc.setRevisions(
        ("2009-08-08 10:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class Hh3cEvcSrvInstRewriteType(TextualConvention, Integer32):
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
              10)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("nestSvlan", 1),
          ("nestCvlan", 2),
          ("nestSvlanCvlan", 3),
          ("stripSvlan", 4),
          ("stripCvlan", 5),
          ("stripSvlanCvlan", 6),
          ("remark1To1", 7),
          ("remark1To2", 8),
          ("remark2To1", 9),
          ("remark2To2", 10))
    )



# MIB Managed Objects in the order of their OIDs

_Hh3cEvcObjects_ObjectIdentity = ObjectIdentity
hh3cEvcObjects = _Hh3cEvcObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 106, 1)
)
_Hh3cEvcScalarGroup_ObjectIdentity = ObjectIdentity
hh3cEvcScalarGroup = _Hh3cEvcScalarGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 106, 1, 1)
)


class _Hh3cEvcSrvInstEncapCapabilities_Type(Bits):
    """Custom type hh3cEvcSrvInstEncapCapabilities based on Bits"""
    namedValues = NamedValues(
        *(("encapDefault", 0),
          ("encapUntagged", 1),
          ("encapTagged", 2),
          ("encapSvlanId", 3),
          ("encapSvlanIdList", 4),
          ("encapSvlanIdOnlyTagged", 5),
          ("encapSvlanIdCvlanId", 6),
          ("encapSvlanIdCvlanIdList", 7),
          ("encapCvlanId", 8),
          ("encapCvlanIdList", 9))
    )

_Hh3cEvcSrvInstEncapCapabilities_Type.__name__ = "Bits"
_Hh3cEvcSrvInstEncapCapabilities_Object = MibScalar
hh3cEvcSrvInstEncapCapabilities = _Hh3cEvcSrvInstEncapCapabilities_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 106, 1, 1, 1),
    _Hh3cEvcSrvInstEncapCapabilities_Type()
)
hh3cEvcSrvInstEncapCapabilities.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cEvcSrvInstEncapCapabilities.setStatus("current")
_Hh3cEvcPortMaxSrvInstNum_Type = Integer32
_Hh3cEvcPortMaxSrvInstNum_Object = MibScalar
hh3cEvcPortMaxSrvInstNum = _Hh3cEvcPortMaxSrvInstNum_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 106, 1, 1, 2),
    _Hh3cEvcPortMaxSrvInstNum_Type()
)
hh3cEvcPortMaxSrvInstNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cEvcPortMaxSrvInstNum.setStatus("current")
_Hh3cEvcSrvInstTable_Object = MibTable
hh3cEvcSrvInstTable = _Hh3cEvcSrvInstTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 106, 1, 2)
)
if mibBuilder.loadTexts:
    hh3cEvcSrvInstTable.setStatus("current")
_Hh3cEvcSrvInstEntry_Object = MibTableRow
hh3cEvcSrvInstEntry = _Hh3cEvcSrvInstEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 106, 1, 2, 1)
)
hh3cEvcSrvInstEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "HH3C-EVC-MIB", "hh3cEvcSrvInstId"),
)
if mibBuilder.loadTexts:
    hh3cEvcSrvInstEntry.setStatus("current")


class _Hh3cEvcSrvInstId_Type(Integer32):
    """Custom type hh3cEvcSrvInstId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Hh3cEvcSrvInstId_Type.__name__ = "Integer32"
_Hh3cEvcSrvInstId_Object = MibTableColumn
hh3cEvcSrvInstId = _Hh3cEvcSrvInstId_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 106, 1, 2, 1, 1),
    _Hh3cEvcSrvInstId_Type()
)
hh3cEvcSrvInstId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cEvcSrvInstId.setStatus("current")


class _Hh3cEvcSrvInstEncap_Type(Integer32):
    """Custom type hh3cEvcSrvInstEncap based on Integer32"""
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
              9)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("default", 1),
          ("untagged", 2),
          ("tagged", 3),
          ("svlanIdList", 4),
          ("svlanIdListOnlyTagged", 5),
          ("svlanIdCvlanId", 6),
          ("svlanIdCvlanIdList", 7),
          ("svlanIdCvlanIdAll", 8),
          ("cvlanIdList", 9))
    )


_Hh3cEvcSrvInstEncap_Type.__name__ = "Integer32"
_Hh3cEvcSrvInstEncap_Object = MibTableColumn
hh3cEvcSrvInstEncap = _Hh3cEvcSrvInstEncap_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 106, 1, 2, 1, 2),
    _Hh3cEvcSrvInstEncap_Type()
)
hh3cEvcSrvInstEncap.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cEvcSrvInstEncap.setStatus("current")


class _Hh3cEvcSrvInstSvlanIdListLow_Type(OctetString):
    """Custom type hh3cEvcSrvInstSvlanIdListLow based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_Hh3cEvcSrvInstSvlanIdListLow_Type.__name__ = "OctetString"
_Hh3cEvcSrvInstSvlanIdListLow_Object = MibTableColumn
hh3cEvcSrvInstSvlanIdListLow = _Hh3cEvcSrvInstSvlanIdListLow_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 106, 1, 2, 1, 3),
    _Hh3cEvcSrvInstSvlanIdListLow_Type()
)
hh3cEvcSrvInstSvlanIdListLow.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cEvcSrvInstSvlanIdListLow.setStatus("current")


class _Hh3cEvcSrvInstSvlanIdListHigh_Type(OctetString):
    """Custom type hh3cEvcSrvInstSvlanIdListHigh based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_Hh3cEvcSrvInstSvlanIdListHigh_Type.__name__ = "OctetString"
_Hh3cEvcSrvInstSvlanIdListHigh_Object = MibTableColumn
hh3cEvcSrvInstSvlanIdListHigh = _Hh3cEvcSrvInstSvlanIdListHigh_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 106, 1, 2, 1, 4),
    _Hh3cEvcSrvInstSvlanIdListHigh_Type()
)
hh3cEvcSrvInstSvlanIdListHigh.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cEvcSrvInstSvlanIdListHigh.setStatus("current")
_Hh3cEvcSrvInstRowStatus_Type = RowStatus
_Hh3cEvcSrvInstRowStatus_Object = MibTableColumn
hh3cEvcSrvInstRowStatus = _Hh3cEvcSrvInstRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 106, 1, 2, 1, 5),
    _Hh3cEvcSrvInstRowStatus_Type()
)
hh3cEvcSrvInstRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cEvcSrvInstRowStatus.setStatus("current")


class _Hh3cEvcSrvInstEnableInStat_Type(TruthValue):
    """Custom type hh3cEvcSrvInstEnableInStat based on TruthValue"""
    defaultValue = 2


_Hh3cEvcSrvInstEnableInStat_Type.__name__ = "TruthValue"
_Hh3cEvcSrvInstEnableInStat_Object = MibTableColumn
hh3cEvcSrvInstEnableInStat = _Hh3cEvcSrvInstEnableInStat_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 106, 1, 2, 1, 6),
    _Hh3cEvcSrvInstEnableInStat_Type()
)
hh3cEvcSrvInstEnableInStat.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cEvcSrvInstEnableInStat.setStatus("current")


class _Hh3cEvcSrvInstEnableOutStat_Type(TruthValue):
    """Custom type hh3cEvcSrvInstEnableOutStat based on TruthValue"""
    defaultValue = 2


_Hh3cEvcSrvInstEnableOutStat_Type.__name__ = "TruthValue"
_Hh3cEvcSrvInstEnableOutStat_Object = MibTableColumn
hh3cEvcSrvInstEnableOutStat = _Hh3cEvcSrvInstEnableOutStat_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 106, 1, 2, 1, 7),
    _Hh3cEvcSrvInstEnableOutStat_Type()
)
hh3cEvcSrvInstEnableOutStat.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cEvcSrvInstEnableOutStat.setStatus("current")


class _Hh3cEvcSrvInstCvlanIdListLow_Type(OctetString):
    """Custom type hh3cEvcSrvInstCvlanIdListLow based on OctetString"""
    defaultHexValue = ""

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_Hh3cEvcSrvInstCvlanIdListLow_Type.__name__ = "OctetString"
_Hh3cEvcSrvInstCvlanIdListLow_Object = MibTableColumn
hh3cEvcSrvInstCvlanIdListLow = _Hh3cEvcSrvInstCvlanIdListLow_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 106, 1, 2, 1, 8),
    _Hh3cEvcSrvInstCvlanIdListLow_Type()
)
hh3cEvcSrvInstCvlanIdListLow.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cEvcSrvInstCvlanIdListLow.setStatus("current")


class _Hh3cEvcSrvInstCvlanIdListHigh_Type(OctetString):
    """Custom type hh3cEvcSrvInstCvlanIdListHigh based on OctetString"""
    defaultHexValue = ""

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_Hh3cEvcSrvInstCvlanIdListHigh_Type.__name__ = "OctetString"
_Hh3cEvcSrvInstCvlanIdListHigh_Object = MibTableColumn
hh3cEvcSrvInstCvlanIdListHigh = _Hh3cEvcSrvInstCvlanIdListHigh_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 106, 1, 2, 1, 9),
    _Hh3cEvcSrvInstCvlanIdListHigh_Type()
)
hh3cEvcSrvInstCvlanIdListHigh.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cEvcSrvInstCvlanIdListHigh.setStatus("current")
_Hh3cEvcSrvInstInRewriteType_Type = Hh3cEvcSrvInstRewriteType
_Hh3cEvcSrvInstInRewriteType_Object = MibTableColumn
hh3cEvcSrvInstInRewriteType = _Hh3cEvcSrvInstInRewriteType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 106, 1, 2, 1, 10),
    _Hh3cEvcSrvInstInRewriteType_Type()
)
hh3cEvcSrvInstInRewriteType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cEvcSrvInstInRewriteType.setStatus("current")


class _Hh3cEvcSrvInstInRewriteSvlanId_Type(Integer32):
    """Custom type hh3cEvcSrvInstInRewriteSvlanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Hh3cEvcSrvInstInRewriteSvlanId_Type.__name__ = "Integer32"
_Hh3cEvcSrvInstInRewriteSvlanId_Object = MibTableColumn
hh3cEvcSrvInstInRewriteSvlanId = _Hh3cEvcSrvInstInRewriteSvlanId_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 106, 1, 2, 1, 11),
    _Hh3cEvcSrvInstInRewriteSvlanId_Type()
)
hh3cEvcSrvInstInRewriteSvlanId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cEvcSrvInstInRewriteSvlanId.setStatus("current")


class _Hh3cEvcSrvInstInRewriteCvlanId_Type(Integer32):
    """Custom type hh3cEvcSrvInstInRewriteCvlanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Hh3cEvcSrvInstInRewriteCvlanId_Type.__name__ = "Integer32"
_Hh3cEvcSrvInstInRewriteCvlanId_Object = MibTableColumn
hh3cEvcSrvInstInRewriteCvlanId = _Hh3cEvcSrvInstInRewriteCvlanId_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 106, 1, 2, 1, 12),
    _Hh3cEvcSrvInstInRewriteCvlanId_Type()
)
hh3cEvcSrvInstInRewriteCvlanId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cEvcSrvInstInRewriteCvlanId.setStatus("current")


class _Hh3cEvcSrvInstInRewriteSymm_Type(TruthValue):
    """Custom type hh3cEvcSrvInstInRewriteSymm based on TruthValue"""
    defaultValue = 2


_Hh3cEvcSrvInstInRewriteSymm_Type.__name__ = "TruthValue"
_Hh3cEvcSrvInstInRewriteSymm_Object = MibTableColumn
hh3cEvcSrvInstInRewriteSymm = _Hh3cEvcSrvInstInRewriteSymm_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 106, 1, 2, 1, 13),
    _Hh3cEvcSrvInstInRewriteSymm_Type()
)
hh3cEvcSrvInstInRewriteSymm.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cEvcSrvInstInRewriteSymm.setStatus("current")
_Hh3cEvcSrvInstOutRewriteType_Type = Hh3cEvcSrvInstRewriteType
_Hh3cEvcSrvInstOutRewriteType_Object = MibTableColumn
hh3cEvcSrvInstOutRewriteType = _Hh3cEvcSrvInstOutRewriteType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 106, 1, 2, 1, 14),
    _Hh3cEvcSrvInstOutRewriteType_Type()
)
hh3cEvcSrvInstOutRewriteType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cEvcSrvInstOutRewriteType.setStatus("current")


class _Hh3cEvcSrvInstOutRewriteSvlanId_Type(Integer32):
    """Custom type hh3cEvcSrvInstOutRewriteSvlanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Hh3cEvcSrvInstOutRewriteSvlanId_Type.__name__ = "Integer32"
_Hh3cEvcSrvInstOutRewriteSvlanId_Object = MibTableColumn
hh3cEvcSrvInstOutRewriteSvlanId = _Hh3cEvcSrvInstOutRewriteSvlanId_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 106, 1, 2, 1, 15),
    _Hh3cEvcSrvInstOutRewriteSvlanId_Type()
)
hh3cEvcSrvInstOutRewriteSvlanId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cEvcSrvInstOutRewriteSvlanId.setStatus("current")


class _Hh3cEvcSrvInstOutRewriteCvlanId_Type(Integer32):
    """Custom type hh3cEvcSrvInstOutRewriteCvlanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Hh3cEvcSrvInstOutRewriteCvlanId_Type.__name__ = "Integer32"
_Hh3cEvcSrvInstOutRewriteCvlanId_Object = MibTableColumn
hh3cEvcSrvInstOutRewriteCvlanId = _Hh3cEvcSrvInstOutRewriteCvlanId_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 106, 1, 2, 1, 16),
    _Hh3cEvcSrvInstOutRewriteCvlanId_Type()
)
hh3cEvcSrvInstOutRewriteCvlanId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cEvcSrvInstOutRewriteCvlanId.setStatus("current")
_Hh3cEvcSrvInstCarTable_Object = MibTable
hh3cEvcSrvInstCarTable = _Hh3cEvcSrvInstCarTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 106, 1, 3)
)
if mibBuilder.loadTexts:
    hh3cEvcSrvInstCarTable.setStatus("current")
_Hh3cEvcSrvInstCarEntry_Object = MibTableRow
hh3cEvcSrvInstCarEntry = _Hh3cEvcSrvInstCarEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 106, 1, 3, 1)
)
hh3cEvcSrvInstCarEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "HH3C-EVC-MIB", "hh3cEvcSrvInstId"),
)
if mibBuilder.loadTexts:
    hh3cEvcSrvInstCarEntry.setStatus("current")
_Hh3cEvcSrvInstInCarIndex_Type = Integer32
_Hh3cEvcSrvInstInCarIndex_Object = MibTableColumn
hh3cEvcSrvInstInCarIndex = _Hh3cEvcSrvInstInCarIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 106, 1, 3, 1, 1),
    _Hh3cEvcSrvInstInCarIndex_Type()
)
hh3cEvcSrvInstInCarIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cEvcSrvInstInCarIndex.setStatus("current")
_Hh3cEvcSrvInstOutCarIndex_Type = Integer32
_Hh3cEvcSrvInstOutCarIndex_Object = MibTableColumn
hh3cEvcSrvInstOutCarIndex = _Hh3cEvcSrvInstOutCarIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 106, 1, 3, 1, 2),
    _Hh3cEvcSrvInstOutCarIndex_Type()
)
hh3cEvcSrvInstOutCarIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cEvcSrvInstOutCarIndex.setStatus("current")
_Hh3cEvcSrvInstStatInfoTable_Object = MibTable
hh3cEvcSrvInstStatInfoTable = _Hh3cEvcSrvInstStatInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 106, 1, 4)
)
if mibBuilder.loadTexts:
    hh3cEvcSrvInstStatInfoTable.setStatus("current")
_Hh3cEvcSrvInstStatInfoEntry_Object = MibTableRow
hh3cEvcSrvInstStatInfoEntry = _Hh3cEvcSrvInstStatInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 106, 1, 4, 1)
)
hh3cEvcSrvInstStatInfoEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "HH3C-EVC-MIB", "hh3cEvcSrvInstId"),
)
if mibBuilder.loadTexts:
    hh3cEvcSrvInstStatInfoEntry.setStatus("current")
_Hh3cEvcSrvInstInPackets_Type = Counter64
_Hh3cEvcSrvInstInPackets_Object = MibTableColumn
hh3cEvcSrvInstInPackets = _Hh3cEvcSrvInstInPackets_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 106, 1, 4, 1, 1),
    _Hh3cEvcSrvInstInPackets_Type()
)
hh3cEvcSrvInstInPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cEvcSrvInstInPackets.setStatus("current")
if mibBuilder.loadTexts:
    hh3cEvcSrvInstInPackets.setUnits("packets")
_Hh3cEvcSrvInstInBytes_Type = Counter64
_Hh3cEvcSrvInstInBytes_Object = MibTableColumn
hh3cEvcSrvInstInBytes = _Hh3cEvcSrvInstInBytes_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 106, 1, 4, 1, 2),
    _Hh3cEvcSrvInstInBytes_Type()
)
hh3cEvcSrvInstInBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cEvcSrvInstInBytes.setStatus("current")
if mibBuilder.loadTexts:
    hh3cEvcSrvInstInBytes.setUnits("bytes")
_Hh3cEvcSrvInstOutPackets_Type = Counter64
_Hh3cEvcSrvInstOutPackets_Object = MibTableColumn
hh3cEvcSrvInstOutPackets = _Hh3cEvcSrvInstOutPackets_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 106, 1, 4, 1, 3),
    _Hh3cEvcSrvInstOutPackets_Type()
)
hh3cEvcSrvInstOutPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cEvcSrvInstOutPackets.setStatus("current")
if mibBuilder.loadTexts:
    hh3cEvcSrvInstOutPackets.setUnits("packets")
_Hh3cEvcSrvInstOutBytes_Type = Counter64
_Hh3cEvcSrvInstOutBytes_Object = MibTableColumn
hh3cEvcSrvInstOutBytes = _Hh3cEvcSrvInstOutBytes_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 106, 1, 4, 1, 4),
    _Hh3cEvcSrvInstOutBytes_Type()
)
hh3cEvcSrvInstOutBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cEvcSrvInstOutBytes.setStatus("current")
if mibBuilder.loadTexts:
    hh3cEvcSrvInstOutBytes.setUnits("bytes")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HH3C-EVC-MIB",
    **{"Hh3cEvcSrvInstRewriteType": Hh3cEvcSrvInstRewriteType,
       "hh3cEvc": hh3cEvc,
       "hh3cEvcObjects": hh3cEvcObjects,
       "hh3cEvcScalarGroup": hh3cEvcScalarGroup,
       "hh3cEvcSrvInstEncapCapabilities": hh3cEvcSrvInstEncapCapabilities,
       "hh3cEvcPortMaxSrvInstNum": hh3cEvcPortMaxSrvInstNum,
       "hh3cEvcSrvInstTable": hh3cEvcSrvInstTable,
       "hh3cEvcSrvInstEntry": hh3cEvcSrvInstEntry,
       "hh3cEvcSrvInstId": hh3cEvcSrvInstId,
       "hh3cEvcSrvInstEncap": hh3cEvcSrvInstEncap,
       "hh3cEvcSrvInstSvlanIdListLow": hh3cEvcSrvInstSvlanIdListLow,
       "hh3cEvcSrvInstSvlanIdListHigh": hh3cEvcSrvInstSvlanIdListHigh,
       "hh3cEvcSrvInstRowStatus": hh3cEvcSrvInstRowStatus,
       "hh3cEvcSrvInstEnableInStat": hh3cEvcSrvInstEnableInStat,
       "hh3cEvcSrvInstEnableOutStat": hh3cEvcSrvInstEnableOutStat,
       "hh3cEvcSrvInstCvlanIdListLow": hh3cEvcSrvInstCvlanIdListLow,
       "hh3cEvcSrvInstCvlanIdListHigh": hh3cEvcSrvInstCvlanIdListHigh,
       "hh3cEvcSrvInstInRewriteType": hh3cEvcSrvInstInRewriteType,
       "hh3cEvcSrvInstInRewriteSvlanId": hh3cEvcSrvInstInRewriteSvlanId,
       "hh3cEvcSrvInstInRewriteCvlanId": hh3cEvcSrvInstInRewriteCvlanId,
       "hh3cEvcSrvInstInRewriteSymm": hh3cEvcSrvInstInRewriteSymm,
       "hh3cEvcSrvInstOutRewriteType": hh3cEvcSrvInstOutRewriteType,
       "hh3cEvcSrvInstOutRewriteSvlanId": hh3cEvcSrvInstOutRewriteSvlanId,
       "hh3cEvcSrvInstOutRewriteCvlanId": hh3cEvcSrvInstOutRewriteCvlanId,
       "hh3cEvcSrvInstCarTable": hh3cEvcSrvInstCarTable,
       "hh3cEvcSrvInstCarEntry": hh3cEvcSrvInstCarEntry,
       "hh3cEvcSrvInstInCarIndex": hh3cEvcSrvInstInCarIndex,
       "hh3cEvcSrvInstOutCarIndex": hh3cEvcSrvInstOutCarIndex,
       "hh3cEvcSrvInstStatInfoTable": hh3cEvcSrvInstStatInfoTable,
       "hh3cEvcSrvInstStatInfoEntry": hh3cEvcSrvInstStatInfoEntry,
       "hh3cEvcSrvInstInPackets": hh3cEvcSrvInstInPackets,
       "hh3cEvcSrvInstInBytes": hh3cEvcSrvInstInBytes,
       "hh3cEvcSrvInstOutPackets": hh3cEvcSrvInstOutPackets,
       "hh3cEvcSrvInstOutBytes": hh3cEvcSrvInstOutBytes}
)
