# SNMP MIB module (PRVT-ELMI-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\telco-systems\binos\PRVT-ELMI-MIB

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

(InterfaceIndex,
 ifIndex) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex",
    "ifIndex")

(switch,) = mibBuilder.importSymbols(
    "PRVT-SWITCH-MIB",
    "switch")

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
 iso,
 transmission) = mibBuilder.importSymbols(
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
    "iso",
    "transmission")

(DisplayString,
 PhysAddress,
 RowStatus,
 StorageType,
 TextualConvention,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "StorageType",
    "TextualConvention",
    "TimeStamp",
    "TruthValue")


# MODULE-IDENTITY

prvtELMIMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 120)
)
if mibBuilder.loadTexts:
    prvtELMIMib.setRevisions(
        ("2009-07-13 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_PrvtELMINotifications_ObjectIdentity = ObjectIdentity
prvtELMINotifications = _PrvtELMINotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 120, 0)
)
_PrvtELMIObjects_ObjectIdentity = ObjectIdentity
prvtELMIObjects = _PrvtELMIObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 120, 1)
)


class _PrvtELMIEnable_Type(Integer32):
    """Custom type prvtELMIEnable based on Integer32"""
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


_PrvtELMIEnable_Type.__name__ = "Integer32"
_PrvtELMIEnable_Object = MibScalar
prvtELMIEnable = _PrvtELMIEnable_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 120, 1, 1),
    _PrvtELMIEnable_Type()
)
prvtELMIEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prvtELMIEnable.setStatus("current")
_PrvtELMICfgTable_Object = MibTable
prvtELMICfgTable = _PrvtELMICfgTable_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 120, 1, 2)
)
if mibBuilder.loadTexts:
    prvtELMICfgTable.setStatus("current")
_PrvtELMICfgEntry_Object = MibTableRow
prvtELMICfgEntry = _PrvtELMICfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 120, 1, 2, 1)
)
prvtELMICfgEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    prvtELMICfgEntry.setStatus("current")


class _PrvtELMIIfEnable_Type(Integer32):
    """Custom type prvtELMIIfEnable based on Integer32"""
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


_PrvtELMIIfEnable_Type.__name__ = "Integer32"
_PrvtELMIIfEnable_Object = MibTableColumn
prvtELMIIfEnable = _PrvtELMIIfEnable_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 120, 1, 2, 1, 1),
    _PrvtELMIIfEnable_Type()
)
prvtELMIIfEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prvtELMIIfEnable.setStatus("current")


class _PrvtELMIIfMode_Type(Integer32):
    """Custom type prvtELMIIfMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("uni-n", 1),
          ("uni-c", 2))
    )


_PrvtELMIIfMode_Type.__name__ = "Integer32"
_PrvtELMIIfMode_Object = MibTableColumn
prvtELMIIfMode = _PrvtELMIIfMode_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 120, 1, 2, 1, 2),
    _PrvtELMIIfMode_Type()
)
prvtELMIIfMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prvtELMIIfMode.setStatus("current")


class _PrvtELMIPollingCnt_Type(Integer32):
    """Custom type prvtELMIPollingCnt based on Integer32"""
    defaultValue = 360

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_PrvtELMIPollingCnt_Type.__name__ = "Integer32"
_PrvtELMIPollingCnt_Object = MibTableColumn
prvtELMIPollingCnt = _PrvtELMIPollingCnt_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 120, 1, 2, 1, 3),
    _PrvtELMIPollingCnt_Type()
)
prvtELMIPollingCnt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prvtELMIPollingCnt.setStatus("current")


class _PrvtELMIPollingTimer_Type(Integer32):
    """Custom type prvtELMIPollingTimer based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 30),
    )


_PrvtELMIPollingTimer_Type.__name__ = "Integer32"
_PrvtELMIPollingTimer_Object = MibTableColumn
prvtELMIPollingTimer = _PrvtELMIPollingTimer_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 120, 1, 2, 1, 4),
    _PrvtELMIPollingTimer_Type()
)
prvtELMIPollingTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prvtELMIPollingTimer.setStatus("current")


class _PrvtELMIVerifPollTimer_Type(Integer32):
    """Custom type prvtELMIVerifPollTimer based on Integer32"""
    defaultValue = 15

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 30),
    )


_PrvtELMIVerifPollTimer_Type.__name__ = "Integer32"
_PrvtELMIVerifPollTimer_Object = MibTableColumn
prvtELMIVerifPollTimer = _PrvtELMIVerifPollTimer_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 120, 1, 2, 1, 5),
    _PrvtELMIVerifPollTimer_Type()
)
prvtELMIVerifPollTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prvtELMIVerifPollTimer.setStatus("current")


class _PrvtELMIStatusCnt_Type(Integer32):
    """Custom type prvtELMIStatusCnt based on Integer32"""
    defaultValue = 4

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 10),
    )


_PrvtELMIStatusCnt_Type.__name__ = "Integer32"
_PrvtELMIStatusCnt_Object = MibTableColumn
prvtELMIStatusCnt = _PrvtELMIStatusCnt_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 120, 1, 2, 1, 6),
    _PrvtELMIStatusCnt_Type()
)
prvtELMIStatusCnt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prvtELMIStatusCnt.setStatus("current")


class _PrvtELMIClearStatistics_Type(Integer32):
    """Custom type prvtELMIClearStatistics based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("clear", 1))
    )


_PrvtELMIClearStatistics_Type.__name__ = "Integer32"
_PrvtELMIClearStatistics_Object = MibTableColumn
prvtELMIClearStatistics = _PrvtELMIClearStatistics_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 120, 1, 2, 1, 7),
    _PrvtELMIClearStatistics_Type()
)
prvtELMIClearStatistics.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prvtELMIClearStatistics.setStatus("current")


class _PrvtELMIMapEvcCEVlanType_Type(Integer32):
    """Custom type prvtELMIMapEvcCEVlanType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("allToOneBundling", 1),
          ("serviceMultiplexingWithNoBund", 2),
          ("budling", 3))
    )


_PrvtELMIMapEvcCEVlanType_Type.__name__ = "Integer32"
_PrvtELMIMapEvcCEVlanType_Object = MibTableColumn
prvtELMIMapEvcCEVlanType = _PrvtELMIMapEvcCEVlanType_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 120, 1, 2, 1, 8),
    _PrvtELMIMapEvcCEVlanType_Type()
)
prvtELMIMapEvcCEVlanType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtELMIMapEvcCEVlanType.setStatus("current")
_PrvtELMIStatisticsTable_Object = MibTable
prvtELMIStatisticsTable = _PrvtELMIStatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 120, 1, 3)
)
if mibBuilder.loadTexts:
    prvtELMIStatisticsTable.setStatus("current")
_PrvtELMIStatisticsEntry_Object = MibTableRow
prvtELMIStatisticsEntry = _PrvtELMIStatisticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 120, 1, 3, 1)
)
prvtELMIStatisticsEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    prvtELMIStatisticsEntry.setStatus("current")


class _PrvtELMIStatusChange_Type(Integer32):
    """Custom type prvtELMIStatusChange based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("up", 1),
          ("down", 2))
    )


_PrvtELMIStatusChange_Type.__name__ = "Integer32"
_PrvtELMIStatusChange_Object = MibTableColumn
prvtELMIStatusChange = _PrvtELMIStatusChange_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 120, 1, 3, 1, 1),
    _PrvtELMIStatusChange_Type()
)
prvtELMIStatusChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtELMIStatusChange.setStatus("current")
_PrvtELMILastFullReport_Type = TimeStamp
_PrvtELMILastFullReport_Object = MibTableColumn
prvtELMILastFullReport = _PrvtELMILastFullReport_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 120, 1, 3, 1, 2),
    _PrvtELMILastFullReport_Type()
)
prvtELMILastFullReport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtELMILastFullReport.setStatus("current")
_PrvtELMITimeOuts_Type = Integer32
_PrvtELMITimeOuts_Object = MibTableColumn
prvtELMITimeOuts = _PrvtELMITimeOuts_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 120, 1, 3, 1, 3),
    _PrvtELMITimeOuts_Type()
)
prvtELMITimeOuts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtELMITimeOuts.setStatus("current")
_PrvtELMIMsgISN_Type = Integer32
_PrvtELMIMsgISN_Object = MibTableColumn
prvtELMIMsgISN = _PrvtELMIMsgISN_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 120, 1, 3, 1, 4),
    _PrvtELMIMsgISN_Type()
)
prvtELMIMsgISN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtELMIMsgISN.setStatus("current")
_PrvtELMIInavlidProtocolVers_Type = Integer32
_PrvtELMIInavlidProtocolVers_Object = MibTableColumn
prvtELMIInavlidProtocolVers = _PrvtELMIInavlidProtocolVers_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 120, 1, 3, 1, 5),
    _PrvtELMIInavlidProtocolVers_Type()
)
prvtELMIInavlidProtocolVers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtELMIInavlidProtocolVers.setStatus("current")
_PrvtELMIEVCInvalidRefId_Type = Integer32
_PrvtELMIEVCInvalidRefId_Object = MibTableColumn
prvtELMIEVCInvalidRefId = _PrvtELMIEVCInvalidRefId_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 120, 1, 3, 1, 6),
    _PrvtELMIEVCInvalidRefId_Type()
)
prvtELMIEVCInvalidRefId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtELMIEVCInvalidRefId.setStatus("current")
_PrvtELMIInavlidMsgType_Type = Integer32
_PrvtELMIInavlidMsgType_Object = MibTableColumn
prvtELMIInavlidMsgType = _PrvtELMIInavlidMsgType_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 120, 1, 3, 1, 7),
    _PrvtELMIInavlidMsgType_Type()
)
prvtELMIInavlidMsgType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtELMIInavlidMsgType.setStatus("current")
_PrvtELMIOOSIE_Type = Integer32
_PrvtELMIOOSIE_Object = MibTableColumn
prvtELMIOOSIE = _PrvtELMIOOSIE_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 120, 1, 3, 1, 8),
    _PrvtELMIOOSIE_Type()
)
prvtELMIOOSIE.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtELMIOOSIE.setStatus("current")
_PrvtELMIDuplicateIE_Type = Integer32
_PrvtELMIDuplicateIE_Object = MibTableColumn
prvtELMIDuplicateIE = _PrvtELMIDuplicateIE_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 120, 1, 3, 1, 9),
    _PrvtELMIDuplicateIE_Type()
)
prvtELMIDuplicateIE.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtELMIDuplicateIE.setStatus("current")
_PrvtELMIMandatoryIEMissing_Type = Integer32
_PrvtELMIMandatoryIEMissing_Object = MibTableColumn
prvtELMIMandatoryIEMissing = _PrvtELMIMandatoryIEMissing_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 120, 1, 3, 1, 10),
    _PrvtELMIMandatoryIEMissing_Type()
)
prvtELMIMandatoryIEMissing.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtELMIMandatoryIEMissing.setStatus("current")
_PrvtELMIInavlidMandatoryIE_Type = Integer32
_PrvtELMIInavlidMandatoryIE_Object = MibTableColumn
prvtELMIInavlidMandatoryIE = _PrvtELMIInavlidMandatoryIE_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 120, 1, 3, 1, 11),
    _PrvtELMIInavlidMandatoryIE_Type()
)
prvtELMIInavlidMandatoryIE.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtELMIInavlidMandatoryIE.setStatus("current")
_PrvtELMIInvalidNonMandatoryIE_Type = Integer32
_PrvtELMIInvalidNonMandatoryIE_Object = MibTableColumn
prvtELMIInvalidNonMandatoryIE = _PrvtELMIInvalidNonMandatoryIE_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 120, 1, 3, 1, 12),
    _PrvtELMIInvalidNonMandatoryIE_Type()
)
prvtELMIInvalidNonMandatoryIE.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtELMIInvalidNonMandatoryIE.setStatus("current")
_PrvtELMIUnrecognizedIE_Type = Integer32
_PrvtELMIUnrecognizedIE_Object = MibTableColumn
prvtELMIUnrecognizedIE = _PrvtELMIUnrecognizedIE_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 120, 1, 3, 1, 13),
    _PrvtELMIUnrecognizedIE_Type()
)
prvtELMIUnrecognizedIE.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtELMIUnrecognizedIE.setStatus("current")
_PrvtELMIUnexpectedIE_Type = Integer32
_PrvtELMIUnexpectedIE_Object = MibTableColumn
prvtELMIUnexpectedIE = _PrvtELMIUnexpectedIE_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 120, 1, 3, 1, 14),
    _PrvtELMIUnexpectedIE_Type()
)
prvtELMIUnexpectedIE.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtELMIUnexpectedIE.setStatus("current")
_PrvtELMIShortMessage_Type = Integer32
_PrvtELMIShortMessage_Object = MibTableColumn
prvtELMIShortMessage = _PrvtELMIShortMessage_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 120, 1, 3, 1, 15),
    _PrvtELMIShortMessage_Type()
)
prvtELMIShortMessage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtELMIShortMessage.setStatus("current")
_PrvtELMIEVCTable_Object = MibTable
prvtELMIEVCTable = _PrvtELMIEVCTable_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 120, 1, 4)
)
if mibBuilder.loadTexts:
    prvtELMIEVCTable.setStatus("current")
_PrvtELMIEVCEntry_Object = MibTableRow
prvtELMIEVCEntry = _PrvtELMIEVCEntry_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 120, 1, 4, 1)
)
prvtELMIEVCEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "PRVT-ELMI-MIB", "prvtELMIEVCId"),
)
if mibBuilder.loadTexts:
    prvtELMIEVCEntry.setStatus("current")


class _PrvtELMIEVCId_Type(Integer32):
    """Custom type prvtELMIEVCId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_PrvtELMIEVCId_Type.__name__ = "Integer32"
_PrvtELMIEVCId_Object = MibTableColumn
prvtELMIEVCId = _PrvtELMIEVCId_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 120, 1, 4, 1, 1),
    _PrvtELMIEVCId_Type()
)
prvtELMIEVCId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    prvtELMIEVCId.setStatus("current")
_PrvtELMIServicesId_Type = Unsigned32
_PrvtELMIServicesId_Object = MibTableColumn
prvtELMIServicesId = _PrvtELMIServicesId_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 120, 1, 4, 1, 2),
    _PrvtELMIServicesId_Type()
)
prvtELMIServicesId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtELMIServicesId.setStatus("current")


class _PrvtELMIEVCStatus_Type(Integer32):
    """Custom type prvtELMIEVCStatus based on Integer32"""
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
        *(("non-active", 0),
          ("new-non-active", 1),
          ("active", 2),
          ("new-active", 3),
          ("partially-active", 4),
          ("new-partially-active", 5))
    )


_PrvtELMIEVCStatus_Type.__name__ = "Integer32"
_PrvtELMIEVCStatus_Object = MibTableColumn
prvtELMIEVCStatus = _PrvtELMIEVCStatus_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 120, 1, 4, 1, 3),
    _PrvtELMIEVCStatus_Type()
)
prvtELMIEVCStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtELMIEVCStatus.setStatus("current")


class _PrvtELMIEVCType_Type(Integer32):
    """Custom type prvtELMIEVCType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("point-to-point", 1),
          ("multi-point-to-point", 2))
    )


_PrvtELMIEVCType_Type.__name__ = "Integer32"
_PrvtELMIEVCType_Object = MibTableColumn
prvtELMIEVCType = _PrvtELMIEVCType_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 120, 1, 4, 1, 4),
    _PrvtELMIEVCType_Type()
)
prvtELMIEVCType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtELMIEVCType.setStatus("current")
_PrvtELMIMapEvcCEVlanTable_Object = MibTable
prvtELMIMapEvcCEVlanTable = _PrvtELMIMapEvcCEVlanTable_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 120, 1, 5)
)
if mibBuilder.loadTexts:
    prvtELMIMapEvcCEVlanTable.setStatus("current")
_PrvtELMIMapEvcCEVlanEntry_Object = MibTableRow
prvtELMIMapEvcCEVlanEntry = _PrvtELMIMapEvcCEVlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 120, 1, 5, 1)
)
prvtELMIMapEvcCEVlanEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "PRVT-ELMI-MIB", "prvtELMIMapEVCId"),
    (0, "PRVT-ELMI-MIB", "prvtELMIMapCeVlanId"),
)
if mibBuilder.loadTexts:
    prvtELMIMapEvcCEVlanEntry.setStatus("current")


class _PrvtELMIMapEVCId_Type(Integer32):
    """Custom type prvtELMIMapEVCId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_PrvtELMIMapEVCId_Type.__name__ = "Integer32"
_PrvtELMIMapEVCId_Object = MibTableColumn
prvtELMIMapEVCId = _PrvtELMIMapEVCId_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 120, 1, 5, 1, 1),
    _PrvtELMIMapEVCId_Type()
)
prvtELMIMapEVCId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtELMIMapEVCId.setStatus("current")


class _PrvtELMIMapCeVlanId_Type(Integer32):
    """Custom type prvtELMIMapCeVlanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_PrvtELMIMapCeVlanId_Type.__name__ = "Integer32"
_PrvtELMIMapCeVlanId_Object = MibTableColumn
prvtELMIMapCeVlanId = _PrvtELMIMapCeVlanId_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 120, 1, 5, 1, 2),
    _PrvtELMIMapCeVlanId_Type()
)
prvtELMIMapCeVlanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtELMIMapCeVlanId.setStatus("current")
_PrvtELMIConformance_ObjectIdentity = ObjectIdentity
prvtELMIConformance = _PrvtELMIConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 120, 2)
)

# Managed Objects groups


# Notification objects

prvtELMIStatus = NotificationType(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 120, 0, 1)
)
prvtELMIStatus.setObjects(
      *(("PRVT-ELMI-MIB", "prvtELMIEnable"),
        ("PRVT-ELMI-MIB", "prvtELMIStatusChange"))
)
if mibBuilder.loadTexts:
    prvtELMIStatus.setStatus(
        "current"
    )

prvtELMIChangeEVC = NotificationType(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 120, 0, 2)
)
prvtELMIChangeEVC.setObjects(
    ("PRVT-ELMI-MIB", "prvtELMIEVCId")
)
if mibBuilder.loadTexts:
    prvtELMIChangeEVC.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "PRVT-ELMI-MIB",
    **{"prvtELMIMib": prvtELMIMib,
       "prvtELMINotifications": prvtELMINotifications,
       "prvtELMIStatus": prvtELMIStatus,
       "prvtELMIChangeEVC": prvtELMIChangeEVC,
       "prvtELMIObjects": prvtELMIObjects,
       "prvtELMIEnable": prvtELMIEnable,
       "prvtELMICfgTable": prvtELMICfgTable,
       "prvtELMICfgEntry": prvtELMICfgEntry,
       "prvtELMIIfEnable": prvtELMIIfEnable,
       "prvtELMIIfMode": prvtELMIIfMode,
       "prvtELMIPollingCnt": prvtELMIPollingCnt,
       "prvtELMIPollingTimer": prvtELMIPollingTimer,
       "prvtELMIVerifPollTimer": prvtELMIVerifPollTimer,
       "prvtELMIStatusCnt": prvtELMIStatusCnt,
       "prvtELMIClearStatistics": prvtELMIClearStatistics,
       "prvtELMIMapEvcCEVlanType": prvtELMIMapEvcCEVlanType,
       "prvtELMIStatisticsTable": prvtELMIStatisticsTable,
       "prvtELMIStatisticsEntry": prvtELMIStatisticsEntry,
       "prvtELMIStatusChange": prvtELMIStatusChange,
       "prvtELMILastFullReport": prvtELMILastFullReport,
       "prvtELMITimeOuts": prvtELMITimeOuts,
       "prvtELMIMsgISN": prvtELMIMsgISN,
       "prvtELMIInavlidProtocolVers": prvtELMIInavlidProtocolVers,
       "prvtELMIEVCInvalidRefId": prvtELMIEVCInvalidRefId,
       "prvtELMIInavlidMsgType": prvtELMIInavlidMsgType,
       "prvtELMIOOSIE": prvtELMIOOSIE,
       "prvtELMIDuplicateIE": prvtELMIDuplicateIE,
       "prvtELMIMandatoryIEMissing": prvtELMIMandatoryIEMissing,
       "prvtELMIInavlidMandatoryIE": prvtELMIInavlidMandatoryIE,
       "prvtELMIInvalidNonMandatoryIE": prvtELMIInvalidNonMandatoryIE,
       "prvtELMIUnrecognizedIE": prvtELMIUnrecognizedIE,
       "prvtELMIUnexpectedIE": prvtELMIUnexpectedIE,
       "prvtELMIShortMessage": prvtELMIShortMessage,
       "prvtELMIEVCTable": prvtELMIEVCTable,
       "prvtELMIEVCEntry": prvtELMIEVCEntry,
       "prvtELMIEVCId": prvtELMIEVCId,
       "prvtELMIServicesId": prvtELMIServicesId,
       "prvtELMIEVCStatus": prvtELMIEVCStatus,
       "prvtELMIEVCType": prvtELMIEVCType,
       "prvtELMIMapEvcCEVlanTable": prvtELMIMapEvcCEVlanTable,
       "prvtELMIMapEvcCEVlanEntry": prvtELMIMapEvcCEVlanEntry,
       "prvtELMIMapEVCId": prvtELMIMapEVCId,
       "prvtELMIMapCeVlanId": prvtELMIMapCeVlanId,
       "prvtELMIConformance": prvtELMIConformance}
)
