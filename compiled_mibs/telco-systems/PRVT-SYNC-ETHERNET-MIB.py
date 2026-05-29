# SNMP MIB module (PRVT-SYNC-ETHERNET-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\telco-systems\binox\PRVT-SYNC-ETHERNET-MIB

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

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

(switch,) = mibBuilder.importSymbols(
    "PRVT-SWITCH-MIB",
    "switch")

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

(DateAndTime,
 DisplayString,
 PhysAddress,
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

prvtSyncEthernetMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 170)
)
if mibBuilder.loadTexts:
    prvtSyncEthernetMIB.setRevisions(
        ("2010-11-10 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class PrvtSyncEthernetQualityLevelType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              4,
              8,
              11,
              15,
              16,
              17,
              20,
              23,
              26,
              28,
              29,
              30,
              31,
              64,
              65)
        )
    )
    namedValues = NamedValues(
        *(("prc", 2),
          ("ssuA", 4),
          ("ssuB", 8),
          ("sec", 11),
          ("dnu", 15),
          ("stu", 16),
          ("prs", 17),
          ("tnc", 20),
          ("st2", 23),
          ("st3", 26),
          ("smc", 28),
          ("st3e", 29),
          ("prov", 30),
          ("dus", 31),
          ("invalid", 64),
          ("failed", 65))
    )



# MIB Managed Objects in the order of their OIDs

_PrvtSyncEthernetMIBNotifications_ObjectIdentity = ObjectIdentity
prvtSyncEthernetMIBNotifications = _PrvtSyncEthernetMIBNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 170, 0)
)
_PrvtSyncEthernetMIBObjects_ObjectIdentity = ObjectIdentity
prvtSyncEthernetMIBObjects = _PrvtSyncEthernetMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 170, 1)
)


class _SyncEthernetHoldOffTime_Type(Integer32):
    """Custom type syncEthernetHoldOffTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(300, 1800),
    )


_SyncEthernetHoldOffTime_Type.__name__ = "Integer32"
_SyncEthernetHoldOffTime_Object = MibScalar
syncEthernetHoldOffTime = _SyncEthernetHoldOffTime_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 170, 1, 1),
    _SyncEthernetHoldOffTime_Type()
)
syncEthernetHoldOffTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    syncEthernetHoldOffTime.setStatus("current")


class _SyncEthernetWaitToRestoreTime_Type(Integer32):
    """Custom type syncEthernetWaitToRestoreTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 12),
    )


_SyncEthernetWaitToRestoreTime_Type.__name__ = "Integer32"
_SyncEthernetWaitToRestoreTime_Object = MibScalar
syncEthernetWaitToRestoreTime = _SyncEthernetWaitToRestoreTime_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 170, 1, 2),
    _SyncEthernetWaitToRestoreTime_Type()
)
syncEthernetWaitToRestoreTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    syncEthernetWaitToRestoreTime.setStatus("current")


class _SyncEthernetG781OptionMode_Type(Integer32):
    """Custom type syncEthernetG781OptionMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("option1", 1),
          ("option2", 2))
    )


_SyncEthernetG781OptionMode_Type.__name__ = "Integer32"
_SyncEthernetG781OptionMode_Object = MibScalar
syncEthernetG781OptionMode = _SyncEthernetG781OptionMode_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 170, 1, 3),
    _SyncEthernetG781OptionMode_Type()
)
syncEthernetG781OptionMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    syncEthernetG781OptionMode.setStatus("current")
_SyncEthernetClockSourceTable_Object = MibTable
syncEthernetClockSourceTable = _SyncEthernetClockSourceTable_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 170, 1, 10)
)
if mibBuilder.loadTexts:
    syncEthernetClockSourceTable.setStatus("current")
_SyncEthernetClockSourceEntry_Object = MibTableRow
syncEthernetClockSourceEntry = _SyncEthernetClockSourceEntry_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 170, 1, 10, 1)
)
syncEthernetClockSourceEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    syncEthernetClockSourceEntry.setStatus("current")
_SyncEthernetClockSourceRowStatus_Type = RowStatus
_SyncEthernetClockSourceRowStatus_Object = MibTableColumn
syncEthernetClockSourceRowStatus = _SyncEthernetClockSourceRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 170, 1, 10, 1, 2),
    _SyncEthernetClockSourceRowStatus_Type()
)
syncEthernetClockSourceRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    syncEthernetClockSourceRowStatus.setStatus("current")


class _SyncEthernetClockSourceAdminStatus_Type(Integer32):
    """Custom type syncEthernetClockSourceAdminStatus based on Integer32"""
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


_SyncEthernetClockSourceAdminStatus_Type.__name__ = "Integer32"
_SyncEthernetClockSourceAdminStatus_Object = MibTableColumn
syncEthernetClockSourceAdminStatus = _SyncEthernetClockSourceAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 170, 1, 10, 1, 3),
    _SyncEthernetClockSourceAdminStatus_Type()
)
syncEthernetClockSourceAdminStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    syncEthernetClockSourceAdminStatus.setStatus("current")
_SyncEthernetClockSourceEsmc_Type = TruthValue
_SyncEthernetClockSourceEsmc_Object = MibTableColumn
syncEthernetClockSourceEsmc = _SyncEthernetClockSourceEsmc_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 170, 1, 10, 1, 4),
    _SyncEthernetClockSourceEsmc_Type()
)
syncEthernetClockSourceEsmc.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    syncEthernetClockSourceEsmc.setStatus("current")


class _SyncEthernetClockSourceFrequency_Type(Unsigned32):
    """Custom type syncEthernetClockSourceFrequency based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2431),
    )


_SyncEthernetClockSourceFrequency_Type.__name__ = "Unsigned32"
_SyncEthernetClockSourceFrequency_Object = MibTableColumn
syncEthernetClockSourceFrequency = _SyncEthernetClockSourceFrequency_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 170, 1, 10, 1, 5),
    _SyncEthernetClockSourceFrequency_Type()
)
syncEthernetClockSourceFrequency.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    syncEthernetClockSourceFrequency.setStatus("current")
_SyncEthernetClockSourceQuality_Type = PrvtSyncEthernetQualityLevelType
_SyncEthernetClockSourceQuality_Object = MibTableColumn
syncEthernetClockSourceQuality = _SyncEthernetClockSourceQuality_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 170, 1, 10, 1, 6),
    _SyncEthernetClockSourceQuality_Type()
)
syncEthernetClockSourceQuality.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    syncEthernetClockSourceQuality.setStatus("current")
_SyncEthernetClockSourceQualityChangeNotify_Type = TruthValue
_SyncEthernetClockSourceQualityChangeNotify_Object = MibTableColumn
syncEthernetClockSourceQualityChangeNotify = _SyncEthernetClockSourceQualityChangeNotify_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 170, 1, 10, 1, 7),
    _SyncEthernetClockSourceQualityChangeNotify_Type()
)
syncEthernetClockSourceQualityChangeNotify.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    syncEthernetClockSourceQualityChangeNotify.setStatus("current")
_SyncEthernetClockSourceRecvQualityLevel_Type = PrvtSyncEthernetQualityLevelType
_SyncEthernetClockSourceRecvQualityLevel_Object = MibTableColumn
syncEthernetClockSourceRecvQualityLevel = _SyncEthernetClockSourceRecvQualityLevel_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 170, 1, 10, 1, 8),
    _SyncEthernetClockSourceRecvQualityLevel_Type()
)
syncEthernetClockSourceRecvQualityLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    syncEthernetClockSourceRecvQualityLevel.setStatus("current")
_SyncEthernetClockSourceLastRecvEsmcPduTime_Type = DateAndTime
_SyncEthernetClockSourceLastRecvEsmcPduTime_Object = MibTableColumn
syncEthernetClockSourceLastRecvEsmcPduTime = _SyncEthernetClockSourceLastRecvEsmcPduTime_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 170, 1, 10, 1, 9),
    _SyncEthernetClockSourceLastRecvEsmcPduTime_Type()
)
syncEthernetClockSourceLastRecvEsmcPduTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    syncEthernetClockSourceLastRecvEsmcPduTime.setStatus("current")
_SyncEthernetClockSourceLastRecvEsmcErrorPduTime_Type = DateAndTime
_SyncEthernetClockSourceLastRecvEsmcErrorPduTime_Object = MibTableColumn
syncEthernetClockSourceLastRecvEsmcErrorPduTime = _SyncEthernetClockSourceLastRecvEsmcErrorPduTime_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 170, 1, 10, 1, 10),
    _SyncEthernetClockSourceLastRecvEsmcErrorPduTime_Type()
)
syncEthernetClockSourceLastRecvEsmcErrorPduTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    syncEthernetClockSourceLastRecvEsmcErrorPduTime.setStatus("current")


class _SyncEthernetClockSourceLastRecvEsmcPduType_Type(Unsigned32):
    """Custom type syncEthernetClockSourceLastRecvEsmcPduType based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_SyncEthernetClockSourceLastRecvEsmcPduType_Type.__name__ = "Unsigned32"
_SyncEthernetClockSourceLastRecvEsmcPduType_Object = MibTableColumn
syncEthernetClockSourceLastRecvEsmcPduType = _SyncEthernetClockSourceLastRecvEsmcPduType_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 170, 1, 10, 1, 11),
    _SyncEthernetClockSourceLastRecvEsmcPduType_Type()
)
syncEthernetClockSourceLastRecvEsmcPduType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    syncEthernetClockSourceLastRecvEsmcPduType.setStatus("current")


class _SyncEthernetClockSourceLastRecvLastError_Type(Unsigned32):
    """Custom type syncEthernetClockSourceLastRecvLastError based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_SyncEthernetClockSourceLastRecvLastError_Type.__name__ = "Unsigned32"
_SyncEthernetClockSourceLastRecvLastError_Object = MibTableColumn
syncEthernetClockSourceLastRecvLastError = _SyncEthernetClockSourceLastRecvLastError_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 170, 1, 10, 1, 12),
    _SyncEthernetClockSourceLastRecvLastError_Type()
)
syncEthernetClockSourceLastRecvLastError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    syncEthernetClockSourceLastRecvLastError.setStatus("current")
_SyncEthernetClockSourceNumRecvEsmcPdu_Type = Unsigned32
_SyncEthernetClockSourceNumRecvEsmcPdu_Object = MibTableColumn
syncEthernetClockSourceNumRecvEsmcPdu = _SyncEthernetClockSourceNumRecvEsmcPdu_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 170, 1, 10, 1, 13),
    _SyncEthernetClockSourceNumRecvEsmcPdu_Type()
)
syncEthernetClockSourceNumRecvEsmcPdu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    syncEthernetClockSourceNumRecvEsmcPdu.setStatus("current")
_SyncEthernetClockSourceNumDiscEsmcPdu_Type = Unsigned32
_SyncEthernetClockSourceNumDiscEsmcPdu_Object = MibTableColumn
syncEthernetClockSourceNumDiscEsmcPdu = _SyncEthernetClockSourceNumDiscEsmcPdu_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 170, 1, 10, 1, 14),
    _SyncEthernetClockSourceNumDiscEsmcPdu_Type()
)
syncEthernetClockSourceNumDiscEsmcPdu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    syncEthernetClockSourceNumDiscEsmcPdu.setStatus("current")
_SyncEthernetClockSourceNumSignalFail_Type = Unsigned32
_SyncEthernetClockSourceNumSignalFail_Object = MibTableColumn
syncEthernetClockSourceNumSignalFail = _SyncEthernetClockSourceNumSignalFail_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 170, 1, 10, 1, 15),
    _SyncEthernetClockSourceNumSignalFail_Type()
)
syncEthernetClockSourceNumSignalFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    syncEthernetClockSourceNumSignalFail.setStatus("current")
_SyncEthernetClockSourceQualityInvalidNotify_Type = TruthValue
_SyncEthernetClockSourceQualityInvalidNotify_Object = MibTableColumn
syncEthernetClockSourceQualityInvalidNotify = _SyncEthernetClockSourceQualityInvalidNotify_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 170, 1, 10, 1, 16),
    _SyncEthernetClockSourceQualityInvalidNotify_Type()
)
syncEthernetClockSourceQualityInvalidNotify.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    syncEthernetClockSourceQualityInvalidNotify.setStatus("current")
_SyncEthernetClockSourceEsmcInvalidNotify_Type = TruthValue
_SyncEthernetClockSourceEsmcInvalidNotify_Object = MibTableColumn
syncEthernetClockSourceEsmcInvalidNotify = _SyncEthernetClockSourceEsmcInvalidNotify_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 170, 1, 10, 1, 17),
    _SyncEthernetClockSourceEsmcInvalidNotify_Type()
)
syncEthernetClockSourceEsmcInvalidNotify.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    syncEthernetClockSourceEsmcInvalidNotify.setStatus("current")
_SyncEthernetClockOutputTable_Object = MibTable
syncEthernetClockOutputTable = _SyncEthernetClockOutputTable_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 170, 1, 12)
)
if mibBuilder.loadTexts:
    syncEthernetClockOutputTable.setStatus("current")
_SyncEthernetClockOutputEntry_Object = MibTableRow
syncEthernetClockOutputEntry = _SyncEthernetClockOutputEntry_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 170, 1, 12, 1)
)
syncEthernetClockOutputEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    syncEthernetClockOutputEntry.setStatus("current")
_SyncEthernetClockOutputRowStatus_Type = RowStatus
_SyncEthernetClockOutputRowStatus_Object = MibTableColumn
syncEthernetClockOutputRowStatus = _SyncEthernetClockOutputRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 170, 1, 12, 1, 2),
    _SyncEthernetClockOutputRowStatus_Type()
)
syncEthernetClockOutputRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    syncEthernetClockOutputRowStatus.setStatus("current")
_SyncEthernetClockOutputEsmc_Type = TruthValue
_SyncEthernetClockOutputEsmc_Object = MibTableColumn
syncEthernetClockOutputEsmc = _SyncEthernetClockOutputEsmc_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 170, 1, 12, 1, 3),
    _SyncEthernetClockOutputEsmc_Type()
)
syncEthernetClockOutputEsmc.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    syncEthernetClockOutputEsmc.setStatus("current")


class _SyncEthernetClockOutputFrequency_Type(Unsigned32):
    """Custom type syncEthernetClockOutputFrequency based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2431),
    )


_SyncEthernetClockOutputFrequency_Type.__name__ = "Unsigned32"
_SyncEthernetClockOutputFrequency_Object = MibTableColumn
syncEthernetClockOutputFrequency = _SyncEthernetClockOutputFrequency_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 170, 1, 12, 1, 4),
    _SyncEthernetClockOutputFrequency_Type()
)
syncEthernetClockOutputFrequency.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    syncEthernetClockOutputFrequency.setStatus("current")


class _SyncEthernetClockOutputDpll_Type(Integer32):
    """Custom type syncEthernetClockOutputDpll based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_SyncEthernetClockOutputDpll_Type.__name__ = "Integer32"
_SyncEthernetClockOutputDpll_Object = MibTableColumn
syncEthernetClockOutputDpll = _SyncEthernetClockOutputDpll_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 170, 1, 12, 1, 5),
    _SyncEthernetClockOutputDpll_Type()
)
syncEthernetClockOutputDpll.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    syncEthernetClockOutputDpll.setStatus("current")
_SyncEthernetClockOutputQualityLevel_Type = PrvtSyncEthernetQualityLevelType
_SyncEthernetClockOutputQualityLevel_Object = MibTableColumn
syncEthernetClockOutputQualityLevel = _SyncEthernetClockOutputQualityLevel_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 170, 1, 12, 1, 6),
    _SyncEthernetClockOutputQualityLevel_Type()
)
syncEthernetClockOutputQualityLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    syncEthernetClockOutputQualityLevel.setStatus("current")
_SyncEthernetClockOutputLastQualityLevelChange_Type = DateAndTime
_SyncEthernetClockOutputLastQualityLevelChange_Object = MibTableColumn
syncEthernetClockOutputLastQualityLevelChange = _SyncEthernetClockOutputLastQualityLevelChange_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 170, 1, 12, 1, 7),
    _SyncEthernetClockOutputLastQualityLevelChange_Type()
)
syncEthernetClockOutputLastQualityLevelChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    syncEthernetClockOutputLastQualityLevelChange.setStatus("current")
_SyncEthernetClockOutputMsgEvent_Type = TruthValue
_SyncEthernetClockOutputMsgEvent_Object = MibTableColumn
syncEthernetClockOutputMsgEvent = _SyncEthernetClockOutputMsgEvent_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 170, 1, 12, 1, 8),
    _SyncEthernetClockOutputMsgEvent_Type()
)
syncEthernetClockOutputMsgEvent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    syncEthernetClockOutputMsgEvent.setStatus("current")
_SyncEthernetClockOutputNumTransmittedEsmcPdu_Type = Unsigned32
_SyncEthernetClockOutputNumTransmittedEsmcPdu_Object = MibTableColumn
syncEthernetClockOutputNumTransmittedEsmcPdu = _SyncEthernetClockOutputNumTransmittedEsmcPdu_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 170, 1, 12, 1, 9),
    _SyncEthernetClockOutputNumTransmittedEsmcPdu_Type()
)
syncEthernetClockOutputNumTransmittedEsmcPdu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    syncEthernetClockOutputNumTransmittedEsmcPdu.setStatus("current")
_SyncEthernetClockOutputNumTransmittedEventEsmcPdu_Type = Unsigned32
_SyncEthernetClockOutputNumTransmittedEventEsmcPdu_Object = MibTableColumn
syncEthernetClockOutputNumTransmittedEventEsmcPdu = _SyncEthernetClockOutputNumTransmittedEventEsmcPdu_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 170, 1, 12, 1, 10),
    _SyncEthernetClockOutputNumTransmittedEventEsmcPdu_Type()
)
syncEthernetClockOutputNumTransmittedEventEsmcPdu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    syncEthernetClockOutputNumTransmittedEventEsmcPdu.setStatus("current")
_SyncEthernetDpllTable_Object = MibTable
syncEthernetDpllTable = _SyncEthernetDpllTable_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 170, 1, 14)
)
if mibBuilder.loadTexts:
    syncEthernetDpllTable.setStatus("current")
_SyncEthernetDpllEntry_Object = MibTableRow
syncEthernetDpllEntry = _SyncEthernetDpllEntry_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 170, 1, 14, 1)
)
syncEthernetDpllEntry.setIndexNames(
    (0, "PRVT-SYNC-ETHERNET-MIB", "syncEthernetDpllModuleId"),
)
if mibBuilder.loadTexts:
    syncEthernetDpllEntry.setStatus("current")


class _SyncEthernetDpllModuleId_Type(Integer32):
    """Custom type syncEthernetDpllModuleId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_SyncEthernetDpllModuleId_Type.__name__ = "Integer32"
_SyncEthernetDpllModuleId_Object = MibTableColumn
syncEthernetDpllModuleId = _SyncEthernetDpllModuleId_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 170, 1, 14, 1, 1),
    _SyncEthernetDpllModuleId_Type()
)
syncEthernetDpllModuleId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    syncEthernetDpllModuleId.setStatus("current")
_SyncEthernetDpllRowStatus_Type = RowStatus
_SyncEthernetDpllRowStatus_Object = MibTableColumn
syncEthernetDpllRowStatus = _SyncEthernetDpllRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 170, 1, 14, 1, 2),
    _SyncEthernetDpllRowStatus_Type()
)
syncEthernetDpllRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    syncEthernetDpllRowStatus.setStatus("current")


class _SyncEthernetDpllAdminStatus_Type(Integer32):
    """Custom type syncEthernetDpllAdminStatus based on Integer32"""
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


_SyncEthernetDpllAdminStatus_Type.__name__ = "Integer32"
_SyncEthernetDpllAdminStatus_Object = MibTableColumn
syncEthernetDpllAdminStatus = _SyncEthernetDpllAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 170, 1, 14, 1, 3),
    _SyncEthernetDpllAdminStatus_Type()
)
syncEthernetDpllAdminStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    syncEthernetDpllAdminStatus.setStatus("current")


class _SyncEthernetDpllReferenceSelection_Type(Integer32):
    """Custom type syncEthernetDpllReferenceSelection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("freerun", 1),
          ("static", 2),
          ("g781", 3))
    )


_SyncEthernetDpllReferenceSelection_Type.__name__ = "Integer32"
_SyncEthernetDpllReferenceSelection_Object = MibTableColumn
syncEthernetDpllReferenceSelection = _SyncEthernetDpllReferenceSelection_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 170, 1, 14, 1, 4),
    _SyncEthernetDpllReferenceSelection_Type()
)
syncEthernetDpllReferenceSelection.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    syncEthernetDpllReferenceSelection.setStatus("current")
_SyncEthernetDpllEnableQualityLevel_Type = TruthValue
_SyncEthernetDpllEnableQualityLevel_Object = MibTableColumn
syncEthernetDpllEnableQualityLevel = _SyncEthernetDpllEnableQualityLevel_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 170, 1, 14, 1, 5),
    _SyncEthernetDpllEnableQualityLevel_Type()
)
syncEthernetDpllEnableQualityLevel.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    syncEthernetDpllEnableQualityLevel.setStatus("current")
_SyncEthernetDpllStatusChangeNotify_Type = TruthValue
_SyncEthernetDpllStatusChangeNotify_Object = MibTableColumn
syncEthernetDpllStatusChangeNotify = _SyncEthernetDpllStatusChangeNotify_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 170, 1, 14, 1, 6),
    _SyncEthernetDpllStatusChangeNotify_Type()
)
syncEthernetDpllStatusChangeNotify.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    syncEthernetDpllStatusChangeNotify.setStatus("current")
_SyncEthernetDpllReferenceChangeNotify_Type = TruthValue
_SyncEthernetDpllReferenceChangeNotify_Object = MibTableColumn
syncEthernetDpllReferenceChangeNotify = _SyncEthernetDpllReferenceChangeNotify_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 170, 1, 14, 1, 7),
    _SyncEthernetDpllReferenceChangeNotify_Type()
)
syncEthernetDpllReferenceChangeNotify.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    syncEthernetDpllReferenceChangeNotify.setStatus("current")


class _SyncEthernetDpllStatus_Type(Integer32):
    """Custom type syncEthernetDpllStatus based on Integer32"""
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
        *(("freerun", 0),
          ("locked", 1),
          ("holdover", 2),
          ("refFailure", 3))
    )


_SyncEthernetDpllStatus_Type.__name__ = "Integer32"
_SyncEthernetDpllStatus_Object = MibTableColumn
syncEthernetDpllStatus = _SyncEthernetDpllStatus_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 170, 1, 14, 1, 8),
    _SyncEthernetDpllStatus_Type()
)
syncEthernetDpllStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    syncEthernetDpllStatus.setStatus("current")
_SyncEthernetDpllStatusLastChange_Type = DateAndTime
_SyncEthernetDpllStatusLastChange_Object = MibTableColumn
syncEthernetDpllStatusLastChange = _SyncEthernetDpllStatusLastChange_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 170, 1, 14, 1, 9),
    _SyncEthernetDpllStatusLastChange_Type()
)
syncEthernetDpllStatusLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    syncEthernetDpllStatusLastChange.setStatus("current")
_SyncEthernetDpllSystemQualityLevel_Type = PrvtSyncEthernetQualityLevelType
_SyncEthernetDpllSystemQualityLevel_Object = MibTableColumn
syncEthernetDpllSystemQualityLevel = _SyncEthernetDpllSystemQualityLevel_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 170, 1, 14, 1, 10),
    _SyncEthernetDpllSystemQualityLevel_Type()
)
syncEthernetDpllSystemQualityLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    syncEthernetDpllSystemQualityLevel.setStatus("current")
_SyncEthernetDpllSystemQualityLevelLastChange_Type = DateAndTime
_SyncEthernetDpllSystemQualityLevelLastChange_Object = MibTableColumn
syncEthernetDpllSystemQualityLevelLastChange = _SyncEthernetDpllSystemQualityLevelLastChange_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 170, 1, 14, 1, 11),
    _SyncEthernetDpllSystemQualityLevelLastChange_Type()
)
syncEthernetDpllSystemQualityLevelLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    syncEthernetDpllSystemQualityLevelLastChange.setStatus("current")
_SyncEthernetDpllSelectedReferenceClock_Type = OctetString
_SyncEthernetDpllSelectedReferenceClock_Object = MibTableColumn
syncEthernetDpllSelectedReferenceClock = _SyncEthernetDpllSelectedReferenceClock_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 170, 1, 14, 1, 12),
    _SyncEthernetDpllSelectedReferenceClock_Type()
)
syncEthernetDpllSelectedReferenceClock.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    syncEthernetDpllSelectedReferenceClock.setStatus("current")
_SyncEthernetDpllSelectedReferenceClockChange_Type = DateAndTime
_SyncEthernetDpllSelectedReferenceClockChange_Object = MibTableColumn
syncEthernetDpllSelectedReferenceClockChange = _SyncEthernetDpllSelectedReferenceClockChange_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 170, 1, 14, 1, 13),
    _SyncEthernetDpllSelectedReferenceClockChange_Type()
)
syncEthernetDpllSelectedReferenceClockChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    syncEthernetDpllSelectedReferenceClockChange.setStatus("current")
_SyncEthernetDpllClkRefTable_Object = MibTable
syncEthernetDpllClkRefTable = _SyncEthernetDpllClkRefTable_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 170, 1, 16)
)
if mibBuilder.loadTexts:
    syncEthernetDpllClkRefTable.setStatus("current")
_SyncEthernetDpllClkRefEntry_Object = MibTableRow
syncEthernetDpllClkRefEntry = _SyncEthernetDpllClkRefEntry_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 170, 1, 16, 1)
)
syncEthernetDpllClkRefEntry.setIndexNames(
    (0, "PRVT-SYNC-ETHERNET-MIB", "syncEthernetDpllModuleId"),
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    syncEthernetDpllClkRefEntry.setStatus("current")
_SyncEthernetDpllClkRefRowStatus_Type = RowStatus
_SyncEthernetDpllClkRefRowStatus_Object = MibTableColumn
syncEthernetDpllClkRefRowStatus = _SyncEthernetDpllClkRefRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 170, 1, 16, 1, 2),
    _SyncEthernetDpllClkRefRowStatus_Type()
)
syncEthernetDpllClkRefRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    syncEthernetDpllClkRefRowStatus.setStatus("current")


class _SyncEthernetDpllClkRefPriority_Type(Unsigned32):
    """Custom type syncEthernetDpllClkRefPriority based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 256),
    )


_SyncEthernetDpllClkRefPriority_Type.__name__ = "Unsigned32"
_SyncEthernetDpllClkRefPriority_Object = MibTableColumn
syncEthernetDpllClkRefPriority = _SyncEthernetDpllClkRefPriority_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 170, 1, 16, 1, 3),
    _SyncEthernetDpllClkRefPriority_Type()
)
syncEthernetDpllClkRefPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    syncEthernetDpllClkRefPriority.setStatus("current")
_SyncEthernetDpllClkRefLockOut_Type = TruthValue
_SyncEthernetDpllClkRefLockOut_Object = MibTableColumn
syncEthernetDpllClkRefLockOut = _SyncEthernetDpllClkRefLockOut_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 170, 1, 16, 1, 4),
    _SyncEthernetDpllClkRefLockOut_Type()
)
syncEthernetDpllClkRefLockOut.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    syncEthernetDpllClkRefLockOut.setStatus("current")
_SyncEthernetDpllClkRefFailStatus_Type = Integer32
_SyncEthernetDpllClkRefFailStatus_Object = MibTableColumn
syncEthernetDpllClkRefFailStatus = _SyncEthernetDpllClkRefFailStatus_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 170, 1, 16, 1, 5),
    _SyncEthernetDpllClkRefFailStatus_Type()
)
syncEthernetDpllClkRefFailStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    syncEthernetDpllClkRefFailStatus.setStatus("current")

# Managed Objects groups


# Notification objects

syncEthernetInvalidESMC = NotificationType(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 170, 0, 1)
)
syncEthernetInvalidESMC.setObjects(
    ("PRVT-SYNC-ETHERNET-MIB", "syncEthernetClockSourceLastRecvLastError")
)
if mibBuilder.loadTexts:
    syncEthernetInvalidESMC.setStatus(
        "current"
    )

syncEthernetQualityLevelChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 170, 0, 2)
)
syncEthernetQualityLevelChange.setObjects(
    ("PRVT-SYNC-ETHERNET-MIB", "syncEthernetClockSourceQuality")
)
if mibBuilder.loadTexts:
    syncEthernetQualityLevelChange.setStatus(
        "current"
    )

syncEthernetInvalidQualityLevelReceived = NotificationType(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 170, 0, 3)
)
syncEthernetInvalidQualityLevelReceived.setObjects(
    ("PRVT-SYNC-ETHERNET-MIB", "syncEthernetClockSourceRecvQualityLevel")
)
if mibBuilder.loadTexts:
    syncEthernetInvalidQualityLevelReceived.setStatus(
        "current"
    )

syncEthernetDPLLReferenceChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 170, 0, 4)
)
syncEthernetDPLLReferenceChange.setObjects(
    ("PRVT-SYNC-ETHERNET-MIB", "syncEthernetDpllSelectedReferenceClockChange")
)
if mibBuilder.loadTexts:
    syncEthernetDPLLReferenceChange.setStatus(
        "current"
    )

syncEthernetDPLLChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 170, 0, 5)
)
syncEthernetDPLLChanged.setObjects(
    ("PRVT-SYNC-ETHERNET-MIB", "syncEthernetDpllStatus")
)
if mibBuilder.loadTexts:
    syncEthernetDPLLChanged.setStatus(
        "current"
    )

syncEthernetDPLLLockFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 170, 0, 6)
)
syncEthernetDPLLLockFailed.setObjects(
    ("PRVT-SYNC-ETHERNET-MIB", "syncEthernetDpllClkRefFailStatus")
)
if mibBuilder.loadTexts:
    syncEthernetDPLLLockFailed.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "PRVT-SYNC-ETHERNET-MIB",
    **{"PrvtSyncEthernetQualityLevelType": PrvtSyncEthernetQualityLevelType,
       "prvtSyncEthernetMIB": prvtSyncEthernetMIB,
       "prvtSyncEthernetMIBNotifications": prvtSyncEthernetMIBNotifications,
       "syncEthernetInvalidESMC": syncEthernetInvalidESMC,
       "syncEthernetQualityLevelChange": syncEthernetQualityLevelChange,
       "syncEthernetInvalidQualityLevelReceived": syncEthernetInvalidQualityLevelReceived,
       "syncEthernetDPLLReferenceChange": syncEthernetDPLLReferenceChange,
       "syncEthernetDPLLChanged": syncEthernetDPLLChanged,
       "syncEthernetDPLLLockFailed": syncEthernetDPLLLockFailed,
       "prvtSyncEthernetMIBObjects": prvtSyncEthernetMIBObjects,
       "syncEthernetHoldOffTime": syncEthernetHoldOffTime,
       "syncEthernetWaitToRestoreTime": syncEthernetWaitToRestoreTime,
       "syncEthernetG781OptionMode": syncEthernetG781OptionMode,
       "syncEthernetClockSourceTable": syncEthernetClockSourceTable,
       "syncEthernetClockSourceEntry": syncEthernetClockSourceEntry,
       "syncEthernetClockSourceRowStatus": syncEthernetClockSourceRowStatus,
       "syncEthernetClockSourceAdminStatus": syncEthernetClockSourceAdminStatus,
       "syncEthernetClockSourceEsmc": syncEthernetClockSourceEsmc,
       "syncEthernetClockSourceFrequency": syncEthernetClockSourceFrequency,
       "syncEthernetClockSourceQuality": syncEthernetClockSourceQuality,
       "syncEthernetClockSourceQualityChangeNotify": syncEthernetClockSourceQualityChangeNotify,
       "syncEthernetClockSourceRecvQualityLevel": syncEthernetClockSourceRecvQualityLevel,
       "syncEthernetClockSourceLastRecvEsmcPduTime": syncEthernetClockSourceLastRecvEsmcPduTime,
       "syncEthernetClockSourceLastRecvEsmcErrorPduTime": syncEthernetClockSourceLastRecvEsmcErrorPduTime,
       "syncEthernetClockSourceLastRecvEsmcPduType": syncEthernetClockSourceLastRecvEsmcPduType,
       "syncEthernetClockSourceLastRecvLastError": syncEthernetClockSourceLastRecvLastError,
       "syncEthernetClockSourceNumRecvEsmcPdu": syncEthernetClockSourceNumRecvEsmcPdu,
       "syncEthernetClockSourceNumDiscEsmcPdu": syncEthernetClockSourceNumDiscEsmcPdu,
       "syncEthernetClockSourceNumSignalFail": syncEthernetClockSourceNumSignalFail,
       "syncEthernetClockSourceQualityInvalidNotify": syncEthernetClockSourceQualityInvalidNotify,
       "syncEthernetClockSourceEsmcInvalidNotify": syncEthernetClockSourceEsmcInvalidNotify,
       "syncEthernetClockOutputTable": syncEthernetClockOutputTable,
       "syncEthernetClockOutputEntry": syncEthernetClockOutputEntry,
       "syncEthernetClockOutputRowStatus": syncEthernetClockOutputRowStatus,
       "syncEthernetClockOutputEsmc": syncEthernetClockOutputEsmc,
       "syncEthernetClockOutputFrequency": syncEthernetClockOutputFrequency,
       "syncEthernetClockOutputDpll": syncEthernetClockOutputDpll,
       "syncEthernetClockOutputQualityLevel": syncEthernetClockOutputQualityLevel,
       "syncEthernetClockOutputLastQualityLevelChange": syncEthernetClockOutputLastQualityLevelChange,
       "syncEthernetClockOutputMsgEvent": syncEthernetClockOutputMsgEvent,
       "syncEthernetClockOutputNumTransmittedEsmcPdu": syncEthernetClockOutputNumTransmittedEsmcPdu,
       "syncEthernetClockOutputNumTransmittedEventEsmcPdu": syncEthernetClockOutputNumTransmittedEventEsmcPdu,
       "syncEthernetDpllTable": syncEthernetDpllTable,
       "syncEthernetDpllEntry": syncEthernetDpllEntry,
       "syncEthernetDpllModuleId": syncEthernetDpllModuleId,
       "syncEthernetDpllRowStatus": syncEthernetDpllRowStatus,
       "syncEthernetDpllAdminStatus": syncEthernetDpllAdminStatus,
       "syncEthernetDpllReferenceSelection": syncEthernetDpllReferenceSelection,
       "syncEthernetDpllEnableQualityLevel": syncEthernetDpllEnableQualityLevel,
       "syncEthernetDpllStatusChangeNotify": syncEthernetDpllStatusChangeNotify,
       "syncEthernetDpllReferenceChangeNotify": syncEthernetDpllReferenceChangeNotify,
       "syncEthernetDpllStatus": syncEthernetDpllStatus,
       "syncEthernetDpllStatusLastChange": syncEthernetDpllStatusLastChange,
       "syncEthernetDpllSystemQualityLevel": syncEthernetDpllSystemQualityLevel,
       "syncEthernetDpllSystemQualityLevelLastChange": syncEthernetDpllSystemQualityLevelLastChange,
       "syncEthernetDpllSelectedReferenceClock": syncEthernetDpllSelectedReferenceClock,
       "syncEthernetDpllSelectedReferenceClockChange": syncEthernetDpllSelectedReferenceClockChange,
       "syncEthernetDpllClkRefTable": syncEthernetDpllClkRefTable,
       "syncEthernetDpllClkRefEntry": syncEthernetDpllClkRefEntry,
       "syncEthernetDpllClkRefRowStatus": syncEthernetDpllClkRefRowStatus,
       "syncEthernetDpllClkRefPriority": syncEthernetDpllClkRefPriority,
       "syncEthernetDpllClkRefLockOut": syncEthernetDpllClkRefLockOut,
       "syncEthernetDpllClkRefFailStatus": syncEthernetDpllClkRefFailStatus}
)
