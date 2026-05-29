# SNMP MIB module (SPRIF-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\sagemcom\SPRIF-MIB

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

(SagemBoolean,) = mibBuilder.importSymbols(
    "EQUIPMENT-MIB",
    "SagemBoolean")

(sagemDr,) = mibBuilder.importSymbols(
    "SAGEM-DR-MIB",
    "sagemDr")

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

sprif = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 1038, 180)
)


# Types definitions



class NodeId(Integer32):
    """Custom type NodeId based on Integer32"""
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
              255)
        )
    )
    namedValues = NamedValues(
        *(("node0", 0),
          ("node1", 1),
          ("node2", 2),
          ("node3", 3),
          ("node4", 4),
          ("node5", 5),
          ("node6", 6),
          ("node7", 7),
          ("node8", 8),
          ("node9", 9),
          ("node10", 10),
          ("node11", 11),
          ("node12", 12),
          ("node13", 13),
          ("node14", 14),
          ("node15", 15),
          ("nodeUNK", 255))
    )





class STATE(Integer32):
    """Custom type STATE based on Integer32"""
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
        *(("off", 0),
          ("idle", 1),
          ("pass", 2),
          ("switch", 3),
          ("unknown", 4))
    )





class SWITCHSTATUS(Integer32):
    """Custom type SWITCHSTATUS based on Integer32"""
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
        *(("notSw", 0),
          ("br", 1),
          ("sw", 2),
          ("brsw", 3),
          ("unknown", 4))
    )





class K1ASK(Integer32):
    """Custom type K1ASK based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              3,
              5,
              6,
              8,
              11,
              13,
              15)
        )
    )
    namedValues = NamedValues(
        *(("nr", 0),
          ("rr", 1),
          ("exerr", 3),
          ("wtr", 5),
          ("msr", 6),
          ("sdr", 8),
          ("sfr", 11),
          ("fsr", 13),
          ("lps", 15))
    )





class LOGTYPE(Integer32):
    """Custom type LOGTYPE based on Integer32"""
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
        *(("receiveK", 0),
          ("transmitK", 1),
          ("opCmd", 2),
          ("failure", 3),
          ("timer", 4),
          ("unknown", 5))
    )





class LOCALCOMMAND(Integer32):
    """Custom type LOCALCOMMAND based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              3,
              5,
              6,
              13,
              15,
              16,
              17,
              18,
              19,
              20)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("exerr", 3),
          ("wtr", 5),
          ("msr", 6),
          ("fsr", 13),
          ("lps", 15),
          ("clear", 16),
          ("lowr", 17),
          ("lopas", 18),
          ("off", 19),
          ("on", 20))
    )





class LOCALFAIL(Integer32):
    """Custom type LOCALFAIL based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              8,
              11,
              24,
              27)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("sd", 8),
          ("sf", 11),
          ("endsd", 24),
          ("endsf", 27))
    )





class K2STAT(Integer32):
    """Custom type K2STAT based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("idle", 0),
          ("br", 1),
          ("brsw", 2),
          ("extra", 3),
          ("msrdi", 6),
          ("msais", 7))
    )





class K2PATH(Integer32):
    """Custom type K2PATH based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("short", 0),
          ("long", 1))
    )





class TrafficStatus(Integer32):
    """Custom type TrafficStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 0),
          ("working", 1),
          ("protection", 2))
    )





class LINE(Integer32):
    """Custom type LINE based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("west", 0),
          ("east", 1),
          ("unknown", 2))
    )





class TIMER(Integer32):
    """Custom type TIMER based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("stop", 0),
          ("start", 1),
          ("restart", 2))
    )




# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Debug_ObjectIdentity = ObjectIdentity
debug = _Debug_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1038, 180, 10)
)


class _DebugNumber_Type(Integer32):
    """Custom type debugNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_DebugNumber_Type.__name__ = "Integer32"
_DebugNumber_Object = MibScalar
debugNumber = _DebugNumber_Object(
    (1, 3, 6, 1, 4, 1, 1038, 180, 10, 1),
    _DebugNumber_Type()
)
debugNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    debugNumber.setStatus("current")
_DebugTable_Object = MibTable
debugTable = _DebugTable_Object(
    (1, 3, 6, 1, 4, 1, 1038, 180, 10, 2)
)
if mibBuilder.loadTexts:
    debugTable.setStatus("current")
_DebugEntry_Object = MibTableRow
debugEntry = _DebugEntry_Object(
    (1, 3, 6, 1, 4, 1, 1038, 180, 10, 2, 1)
)
debugEntry.setIndexNames(
    (0, "SPRIF-MIB", "debugIndex"),
)
if mibBuilder.loadTexts:
    debugEntry.setStatus("current")


class _DebugIndex_Type(Integer32):
    """Custom type debugIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_DebugIndex_Type.__name__ = "Integer32"
_DebugIndex_Object = MibTableColumn
debugIndex = _DebugIndex_Object(
    (1, 3, 6, 1, 4, 1, 1038, 180, 10, 2, 1, 1),
    _DebugIndex_Type()
)
debugIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    debugIndex.setStatus("current")


class _DebugDate_Type(Integer32):
    """Custom type debugDate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_DebugDate_Type.__name__ = "Integer32"
_DebugDate_Object = MibTableColumn
debugDate = _DebugDate_Object(
    (1, 3, 6, 1, 4, 1, 1038, 180, 10, 2, 1, 2),
    _DebugDate_Type()
)
debugDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    debugDate.setStatus("current")
_DebugNodeID_Type = NodeId
_DebugNodeID_Object = MibTableColumn
debugNodeID = _DebugNodeID_Object(
    (1, 3, 6, 1, 4, 1, 1038, 180, 10, 2, 1, 3),
    _DebugNodeID_Type()
)
debugNodeID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    debugNodeID.setStatus("current")
_DebugLogType_Type = LOGTYPE
_DebugLogType_Object = MibTableColumn
debugLogType = _DebugLogType_Object(
    (1, 3, 6, 1, 4, 1, 1038, 180, 10, 2, 1, 4),
    _DebugLogType_Type()
)
debugLogType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    debugLogType.setStatus("current")
_DebugLine_Type = LINE
_DebugLine_Object = MibTableColumn
debugLine = _DebugLine_Object(
    (1, 3, 6, 1, 4, 1, 1038, 180, 10, 2, 1, 5),
    _DebugLine_Type()
)
debugLine.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    debugLine.setStatus("current")
_DebugNodeState_Type = STATE
_DebugNodeState_Object = MibTableColumn
debugNodeState = _DebugNodeState_Object(
    (1, 3, 6, 1, 4, 1, 1038, 180, 10, 2, 1, 6),
    _DebugNodeState_Type()
)
debugNodeState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    debugNodeState.setStatus("current")
_DebugTrafficStatus_Type = TrafficStatus
_DebugTrafficStatus_Object = MibTableColumn
debugTrafficStatus = _DebugTrafficStatus_Object(
    (1, 3, 6, 1, 4, 1, 1038, 180, 10, 2, 1, 7),
    _DebugTrafficStatus_Type()
)
debugTrafficStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    debugTrafficStatus.setStatus("current")
_DebugSwitchingState_Type = SWITCHSTATUS
_DebugSwitchingState_Object = MibTableColumn
debugSwitchingState = _DebugSwitchingState_Object(
    (1, 3, 6, 1, 4, 1, 1038, 180, 10, 2, 1, 8),
    _DebugSwitchingState_Type()
)
debugSwitchingState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    debugSwitchingState.setStatus("current")
_DebugTxK1Ask_Type = K1ASK
_DebugTxK1Ask_Object = MibTableColumn
debugTxK1Ask = _DebugTxK1Ask_Object(
    (1, 3, 6, 1, 4, 1, 1038, 180, 10, 2, 1, 9),
    _DebugTxK1Ask_Type()
)
debugTxK1Ask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    debugTxK1Ask.setStatus("current")
_DebugTxK1Dst_Type = NodeId
_DebugTxK1Dst_Object = MibTableColumn
debugTxK1Dst = _DebugTxK1Dst_Object(
    (1, 3, 6, 1, 4, 1, 1038, 180, 10, 2, 1, 10),
    _DebugTxK1Dst_Type()
)
debugTxK1Dst.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    debugTxK1Dst.setStatus("current")
_DebugTxK2Src_Type = NodeId
_DebugTxK2Src_Object = MibTableColumn
debugTxK2Src = _DebugTxK2Src_Object(
    (1, 3, 6, 1, 4, 1, 1038, 180, 10, 2, 1, 11),
    _DebugTxK2Src_Type()
)
debugTxK2Src.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    debugTxK2Src.setStatus("current")
_DebugTxK2Path_Type = K2PATH
_DebugTxK2Path_Object = MibTableColumn
debugTxK2Path = _DebugTxK2Path_Object(
    (1, 3, 6, 1, 4, 1, 1038, 180, 10, 2, 1, 12),
    _DebugTxK2Path_Type()
)
debugTxK2Path.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    debugTxK2Path.setStatus("current")
_DebugTxK2Stat_Type = K2STAT
_DebugTxK2Stat_Object = MibTableColumn
debugTxK2Stat = _DebugTxK2Stat_Object(
    (1, 3, 6, 1, 4, 1, 1038, 180, 10, 2, 1, 13),
    _DebugTxK2Stat_Type()
)
debugTxK2Stat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    debugTxK2Stat.setStatus("current")
_DebugRxK1Ask_Type = K1ASK
_DebugRxK1Ask_Object = MibTableColumn
debugRxK1Ask = _DebugRxK1Ask_Object(
    (1, 3, 6, 1, 4, 1, 1038, 180, 10, 2, 1, 14),
    _DebugRxK1Ask_Type()
)
debugRxK1Ask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    debugRxK1Ask.setStatus("current")
_DebugRxK1Dst_Type = NodeId
_DebugRxK1Dst_Object = MibTableColumn
debugRxK1Dst = _DebugRxK1Dst_Object(
    (1, 3, 6, 1, 4, 1, 1038, 180, 10, 2, 1, 15),
    _DebugRxK1Dst_Type()
)
debugRxK1Dst.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    debugRxK1Dst.setStatus("current")
_DebugRxK2Src_Type = NodeId
_DebugRxK2Src_Object = MibTableColumn
debugRxK2Src = _DebugRxK2Src_Object(
    (1, 3, 6, 1, 4, 1, 1038, 180, 10, 2, 1, 16),
    _DebugRxK2Src_Type()
)
debugRxK2Src.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    debugRxK2Src.setStatus("current")
_DebugRxK2Path_Type = K2PATH
_DebugRxK2Path_Object = MibTableColumn
debugRxK2Path = _DebugRxK2Path_Object(
    (1, 3, 6, 1, 4, 1, 1038, 180, 10, 2, 1, 17),
    _DebugRxK2Path_Type()
)
debugRxK2Path.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    debugRxK2Path.setStatus("current")
_DebugRxK2Stat_Type = K2STAT
_DebugRxK2Stat_Object = MibTableColumn
debugRxK2Stat = _DebugRxK2Stat_Object(
    (1, 3, 6, 1, 4, 1, 1038, 180, 10, 2, 1, 18),
    _DebugRxK2Stat_Type()
)
debugRxK2Stat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    debugRxK2Stat.setStatus("current")


class _DebugWtr_Type(Integer32):
    """Custom type debugWtr based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_DebugWtr_Type.__name__ = "Integer32"
_DebugWtr_Object = MibTableColumn
debugWtr = _DebugWtr_Object(
    (1, 3, 6, 1, 4, 1, 1038, 180, 10, 2, 1, 19),
    _DebugWtr_Type()
)
debugWtr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    debugWtr.setStatus("current")
_DebugLastDistantCommand_Type = K1ASK
_DebugLastDistantCommand_Object = MibTableColumn
debugLastDistantCommand = _DebugLastDistantCommand_Object(
    (1, 3, 6, 1, 4, 1, 1038, 180, 10, 2, 1, 20),
    _DebugLastDistantCommand_Type()
)
debugLastDistantCommand.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    debugLastDistantCommand.setStatus("current")
_DebugLastDetectedFailure_Type = LOCALFAIL
_DebugLastDetectedFailure_Object = MibTableColumn
debugLastDetectedFailure = _DebugLastDetectedFailure_Object(
    (1, 3, 6, 1, 4, 1, 1038, 180, 10, 2, 1, 21),
    _DebugLastDetectedFailure_Type()
)
debugLastDetectedFailure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    debugLastDetectedFailure.setStatus("current")
_DebugLastLocalCommand_Type = LOCALCOMMAND
_DebugLastLocalCommand_Object = MibTableColumn
debugLastLocalCommand = _DebugLastLocalCommand_Object(
    (1, 3, 6, 1, 4, 1, 1038, 180, 10, 2, 1, 22),
    _DebugLastLocalCommand_Type()
)
debugLastLocalCommand.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    debugLastLocalCommand.setStatus("current")
_DebugTimerAction_Type = TIMER
_DebugTimerAction_Object = MibTableColumn
debugTimerAction = _DebugTimerAction_Object(
    (1, 3, 6, 1, 4, 1, 1038, 180, 10, 2, 1, 23),
    _DebugTimerAction_Type()
)
debugTimerAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    debugTimerAction.setStatus("current")


class _DebugActivated_Type(Integer32):
    """Custom type debugActivated based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_DebugActivated_Type.__name__ = "Integer32"
_DebugActivated_Object = MibScalar
debugActivated = _DebugActivated_Object(
    (1, 3, 6, 1, 4, 1, 1038, 180, 10, 3),
    _DebugActivated_Type()
)
debugActivated.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    debugActivated.setStatus("current")
_Debug3_ObjectIdentity = ObjectIdentity
debug3 = _Debug3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1038, 180, 30)
)
_Debug3Table_Object = MibTable
debug3Table = _Debug3Table_Object(
    (1, 3, 6, 1, 4, 1, 1038, 180, 30, 2)
)
if mibBuilder.loadTexts:
    debug3Table.setStatus("current")
_Debug3Entry_Object = MibTableRow
debug3Entry = _Debug3Entry_Object(
    (1, 3, 6, 1, 4, 1, 1038, 180, 30, 2, 1)
)
debug3Entry.setIndexNames(
    (0, "SPRIF-MIB", "debugIndex"),
)
if mibBuilder.loadTexts:
    debug3Entry.setStatus("current")


class _Debug3Date_Type(Integer32):
    """Custom type debug3Date based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_Debug3Date_Type.__name__ = "Integer32"
_Debug3Date_Object = MibTableColumn
debug3Date = _Debug3Date_Object(
    (1, 3, 6, 1, 4, 1, 1038, 180, 30, 2, 1, 2),
    _Debug3Date_Type()
)
debug3Date.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    debug3Date.setStatus("current")
_Debug3Line_Type = LINE
_Debug3Line_Object = MibTableColumn
debug3Line = _Debug3Line_Object(
    (1, 3, 6, 1, 4, 1, 1038, 180, 30, 2, 1, 5),
    _Debug3Line_Type()
)
debug3Line.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    debug3Line.setStatus("current")
_Debug3arv_Type = SagemBoolean
_Debug3arv_Object = MibTableColumn
debug3arv = _Debug3arv_Object(
    (1, 3, 6, 1, 4, 1, 1038, 180, 30, 2, 1, 23),
    _Debug3arv_Type()
)
debug3arv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    debug3arv.setStatus("current")
_Debug3ato_Type = SagemBoolean
_Debug3ato_Object = MibTableColumn
debug3ato = _Debug3ato_Object(
    (1, 3, 6, 1, 4, 1, 1038, 180, 30, 2, 1, 24),
    _Debug3ato_Type()
)
debug3ato.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    debug3ato.setStatus("current")
_Debug3aun_Type = SagemBoolean
_Debug3aun_Object = MibTableColumn
debug3aun = _Debug3aun_Object(
    (1, 3, 6, 1, 4, 1, 1038, 180, 30, 2, 1, 25),
    _Debug3aun_Type()
)
debug3aun.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    debug3aun.setStatus("current")
_Debug3ptm_Type = SagemBoolean
_Debug3ptm_Object = MibTableColumn
debug3ptm = _Debug3ptm_Object(
    (1, 3, 6, 1, 4, 1, 1038, 180, 30, 2, 1, 26),
    _Debug3ptm_Type()
)
debug3ptm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    debug3ptm.setStatus("current")
_Debug3mms_Type = SagemBoolean
_Debug3mms_Object = MibTableColumn
debug3mms = _Debug3mms_Object(
    (1, 3, 6, 1, 4, 1, 1038, 180, 30, 2, 1, 27),
    _Debug3mms_Type()
)
debug3mms.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    debug3mms.setStatus("current")
_Debug3exr_Type = SagemBoolean
_Debug3exr_Object = MibTableColumn
debug3exr = _Debug3exr_Object(
    (1, 3, 6, 1, 4, 1, 1038, 180, 30, 2, 1, 28),
    _Debug3exr_Type()
)
debug3exr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    debug3exr.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SPRIF-MIB",
    **{"NodeId": NodeId,
       "STATE": STATE,
       "SWITCHSTATUS": SWITCHSTATUS,
       "K1ASK": K1ASK,
       "LOGTYPE": LOGTYPE,
       "LOCALCOMMAND": LOCALCOMMAND,
       "LOCALFAIL": LOCALFAIL,
       "K2STAT": K2STAT,
       "K2PATH": K2PATH,
       "TrafficStatus": TrafficStatus,
       "LINE": LINE,
       "TIMER": TIMER,
       "sprif": sprif,
       "debug": debug,
       "debugNumber": debugNumber,
       "debugTable": debugTable,
       "debugEntry": debugEntry,
       "debugIndex": debugIndex,
       "debugDate": debugDate,
       "debugNodeID": debugNodeID,
       "debugLogType": debugLogType,
       "debugLine": debugLine,
       "debugNodeState": debugNodeState,
       "debugTrafficStatus": debugTrafficStatus,
       "debugSwitchingState": debugSwitchingState,
       "debugTxK1Ask": debugTxK1Ask,
       "debugTxK1Dst": debugTxK1Dst,
       "debugTxK2Src": debugTxK2Src,
       "debugTxK2Path": debugTxK2Path,
       "debugTxK2Stat": debugTxK2Stat,
       "debugRxK1Ask": debugRxK1Ask,
       "debugRxK1Dst": debugRxK1Dst,
       "debugRxK2Src": debugRxK2Src,
       "debugRxK2Path": debugRxK2Path,
       "debugRxK2Stat": debugRxK2Stat,
       "debugWtr": debugWtr,
       "debugLastDistantCommand": debugLastDistantCommand,
       "debugLastDetectedFailure": debugLastDetectedFailure,
       "debugLastLocalCommand": debugLastLocalCommand,
       "debugTimerAction": debugTimerAction,
       "debugActivated": debugActivated,
       "debug3": debug3,
       "debug3Table": debug3Table,
       "debug3Entry": debug3Entry,
       "debug3Date": debug3Date,
       "debug3Line": debug3Line,
       "debug3arv": debug3arv,
       "debug3ato": debug3ato,
       "debug3aun": debug3aun,
       "debug3ptm": debug3ptm,
       "debug3mms": debug3mms,
       "debug3exr": debug3exr}
)
