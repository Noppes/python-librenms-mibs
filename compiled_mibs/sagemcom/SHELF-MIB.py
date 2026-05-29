# SNMP MIB module (SHELF-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\sagemcom\SHELF-MIB

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

(SagemBoolean,
 Severity) = mibBuilder.importSymbols(
    "EQUIPMENT-MIB",
    "SagemBoolean",
    "Severity")

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

shelf = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 1038, 150)
)


# Types definitions



class ProtectionType(Integer32):
    """Custom type ProtectionType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("cardp", 1))
    )





class BoardFailure(Integer32):
    """Custom type BoardFailure based on Integer32"""
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
        *(("none", 0),
          ("missing", 1),
          ("mismatch", 2),
          ("defective", 3))
    )





class LedStatus(Integer32):
    """Custom type LedStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 1),
          ("green", 2),
          ("yellow", 3),
          ("orange", 4),
          ("red", 5))
    )





class LedType(Integer32):
    """Custom type LedType based on Integer32"""
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("status1", 1),
          ("status2", 2),
          ("online", 3),
          ("traffic", 4),
          ("major", 5),
          ("minor", 6),
          ("ether", 7),
          ("halfFull", 8))
    )





class HoldTime(Integer32):
    """Custom type HoldTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              3,
              10,
              30)
        )
    )
    namedValues = NamedValues(
        *(("hold01sec", 1),
          ("hold03sec", 3),
          ("hold10sec", 10),
          ("hold30sec", 30))
    )





class EOWClockMode(Integer32):
    """Custom type EOWClockMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("codirectionnal", 0),
          ("contradirSlave", 1),
          ("contradirMaster", 2))
    )





class EOWType(Integer32):
    """Custom type EOWType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("rsE1", 1),
          ("rsF1", 2),
          ("rsOther", 3),
          ("msE2", 4),
          ("aux", 5))
    )




# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AdrHotReset_Type = SagemBoolean
_AdrHotReset_Object = MibScalar
adrHotReset = _AdrHotReset_Object(
    (1, 3, 6, 1, 4, 1, 1038, 150, 1),
    _AdrHotReset_Type()
)
adrHotReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adrHotReset.setStatus("current")
_Led_ObjectIdentity = ObjectIdentity
led = _Led_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1038, 150, 2)
)


class _LedNumber_Type(Integer32):
    """Custom type ledNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_LedNumber_Type.__name__ = "Integer32"
_LedNumber_Object = MibScalar
ledNumber = _LedNumber_Object(
    (1, 3, 6, 1, 4, 1, 1038, 150, 2, 1),
    _LedNumber_Type()
)
ledNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ledNumber.setStatus("current")
_LedTable_Object = MibTable
ledTable = _LedTable_Object(
    (1, 3, 6, 1, 4, 1, 1038, 150, 2, 2)
)
if mibBuilder.loadTexts:
    ledTable.setStatus("current")
_LedEntry_Object = MibTableRow
ledEntry = _LedEntry_Object(
    (1, 3, 6, 1, 4, 1, 1038, 150, 2, 2, 1)
)
ledEntry.setIndexNames(
    (0, "SHELF-MIB", "ledIndex"),
)
if mibBuilder.loadTexts:
    ledEntry.setStatus("current")


class _LedIndex_Type(Integer32):
    """Custom type ledIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_LedIndex_Type.__name__ = "Integer32"
_LedIndex_Object = MibTableColumn
ledIndex = _LedIndex_Object(
    (1, 3, 6, 1, 4, 1, 1038, 150, 2, 2, 1, 1),
    _LedIndex_Type()
)
ledIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ledIndex.setStatus("current")


class _LedPosition_Type(Integer32):
    """Custom type ledPosition based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_LedPosition_Type.__name__ = "Integer32"
_LedPosition_Object = MibTableColumn
ledPosition = _LedPosition_Object(
    (1, 3, 6, 1, 4, 1, 1038, 150, 2, 2, 1, 2),
    _LedPosition_Type()
)
ledPosition.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ledPosition.setStatus("current")
_LedType_Type = LedType
_LedType_Object = MibTableColumn
ledType = _LedType_Object(
    (1, 3, 6, 1, 4, 1, 1038, 150, 2, 2, 1, 3),
    _LedType_Type()
)
ledType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ledType.setStatus("current")
_LedStatus_Type = LedStatus
_LedStatus_Object = MibTableColumn
ledStatus = _LedStatus_Object(
    (1, 3, 6, 1, 4, 1, 1038, 150, 2, 2, 1, 4),
    _LedStatus_Type()
)
ledStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ledStatus.setStatus("current")
_HoldTime_ObjectIdentity = ObjectIdentity
holdTime = _HoldTime_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1038, 150, 3)
)
_AdrFailHoldOffTime_Type = HoldTime
_AdrFailHoldOffTime_Object = MibScalar
adrFailHoldOffTime = _AdrFailHoldOffTime_Object(
    (1, 3, 6, 1, 4, 1, 1038, 150, 3, 1),
    _AdrFailHoldOffTime_Type()
)
adrFailHoldOffTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adrFailHoldOffTime.setStatus("current")
_AdrFailHoldOnTime_Type = HoldTime
_AdrFailHoldOnTime_Object = MibScalar
adrFailHoldOnTime = _AdrFailHoldOnTime_Object(
    (1, 3, 6, 1, 4, 1, 1038, 150, 3, 2),
    _AdrFailHoldOnTime_Type()
)
adrFailHoldOnTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adrFailHoldOnTime.setStatus("current")
_Board_ObjectIdentity = ObjectIdentity
board = _Board_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1038, 150, 20)
)


class _BoardNumber_Type(Integer32):
    """Custom type boardNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_BoardNumber_Type.__name__ = "Integer32"
_BoardNumber_Object = MibScalar
boardNumber = _BoardNumber_Object(
    (1, 3, 6, 1, 4, 1, 1038, 150, 20, 1),
    _BoardNumber_Type()
)
boardNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    boardNumber.setStatus("current")
_BoardTable_Object = MibTable
boardTable = _BoardTable_Object(
    (1, 3, 6, 1, 4, 1, 1038, 150, 20, 2)
)
if mibBuilder.loadTexts:
    boardTable.setStatus("current")
_BoardEntry_Object = MibTableRow
boardEntry = _BoardEntry_Object(
    (1, 3, 6, 1, 4, 1, 1038, 150, 20, 2, 1)
)
boardEntry.setIndexNames(
    (0, "SHELF-MIB", "boardIndex"),
)
if mibBuilder.loadTexts:
    boardEntry.setStatus("current")


class _BoardIndex_Type(Integer32):
    """Custom type boardIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_BoardIndex_Type.__name__ = "Integer32"
_BoardIndex_Object = MibTableColumn
boardIndex = _BoardIndex_Object(
    (1, 3, 6, 1, 4, 1, 1038, 150, 20, 2, 1, 1),
    _BoardIndex_Type()
)
boardIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    boardIndex.setStatus("current")
_BoardSlotName_Type = DisplayString
_BoardSlotName_Object = MibTableColumn
boardSlotName = _BoardSlotName_Object(
    (1, 3, 6, 1, 4, 1, 1038, 150, 20, 2, 1, 2),
    _BoardSlotName_Type()
)
boardSlotName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    boardSlotName.setStatus("current")


class _BoardExpectType_Type(Integer32):
    """Custom type boardExpectType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_BoardExpectType_Type.__name__ = "Integer32"
_BoardExpectType_Object = MibTableColumn
boardExpectType = _BoardExpectType_Object(
    (1, 3, 6, 1, 4, 1, 1038, 150, 20, 2, 1, 3),
    _BoardExpectType_Type()
)
boardExpectType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    boardExpectType.setStatus("current")


class _BoardInsertType_Type(Integer32):
    """Custom type boardInsertType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_BoardInsertType_Type.__name__ = "Integer32"
_BoardInsertType_Object = MibTableColumn
boardInsertType = _BoardInsertType_Object(
    (1, 3, 6, 1, 4, 1, 1038, 150, 20, 2, 1, 4),
    _BoardInsertType_Type()
)
boardInsertType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    boardInsertType.setStatus("current")
_BoardExpectFamily_Type = DisplayString
_BoardExpectFamily_Object = MibTableColumn
boardExpectFamily = _BoardExpectFamily_Object(
    (1, 3, 6, 1, 4, 1, 1038, 150, 20, 2, 1, 5),
    _BoardExpectFamily_Type()
)
boardExpectFamily.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    boardExpectFamily.setStatus("current")
_BoardInsertFamily_Type = DisplayString
_BoardInsertFamily_Object = MibTableColumn
boardInsertFamily = _BoardInsertFamily_Object(
    (1, 3, 6, 1, 4, 1, 1038, 150, 20, 2, 1, 6),
    _BoardInsertFamily_Type()
)
boardInsertFamily.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    boardInsertFamily.setStatus("current")
_BoardActive_Type = SagemBoolean
_BoardActive_Object = MibTableColumn
boardActive = _BoardActive_Object(
    (1, 3, 6, 1, 4, 1, 1038, 150, 20, 2, 1, 7),
    _BoardActive_Type()
)
boardActive.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    boardActive.setStatus("current")


class _BoardFirstPortIndex_Type(Integer32):
    """Custom type boardFirstPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_BoardFirstPortIndex_Type.__name__ = "Integer32"
_BoardFirstPortIndex_Object = MibTableColumn
boardFirstPortIndex = _BoardFirstPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 1038, 150, 20, 2, 1, 8),
    _BoardFirstPortIndex_Type()
)
boardFirstPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    boardFirstPortIndex.setStatus("current")
_BoardProtectionType_Type = ProtectionType
_BoardProtectionType_Object = MibTableColumn
boardProtectionType = _BoardProtectionType_Object(
    (1, 3, 6, 1, 4, 1, 1038, 150, 20, 2, 1, 9),
    _BoardProtectionType_Type()
)
boardProtectionType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    boardProtectionType.setStatus("current")
_BoardMonitor_Type = SagemBoolean
_BoardMonitor_Object = MibTableColumn
boardMonitor = _BoardMonitor_Object(
    (1, 3, 6, 1, 4, 1, 1038, 150, 20, 2, 1, 10),
    _BoardMonitor_Type()
)
boardMonitor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    boardMonitor.setStatus("current")
_BoardFailure_Type = BoardFailure
_BoardFailure_Object = MibTableColumn
boardFailure = _BoardFailure_Object(
    (1, 3, 6, 1, 4, 1, 1038, 150, 20, 2, 1, 11),
    _BoardFailure_Type()
)
boardFailure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    boardFailure.setStatus("current")
_BoardSeverity_Type = Severity
_BoardSeverity_Object = MibTableColumn
boardSeverity = _BoardSeverity_Object(
    (1, 3, 6, 1, 4, 1, 1038, 150, 20, 2, 1, 12),
    _BoardSeverity_Type()
)
boardSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    boardSeverity.setStatus("current")
_BoardMissingSev_Type = Severity
_BoardMissingSev_Object = MibTableColumn
boardMissingSev = _BoardMissingSev_Object(
    (1, 3, 6, 1, 4, 1, 1038, 150, 20, 2, 1, 13),
    _BoardMissingSev_Type()
)
boardMissingSev.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    boardMissingSev.setStatus("current")
_BoardMismatchSev_Type = Severity
_BoardMismatchSev_Object = MibTableColumn
boardMismatchSev = _BoardMismatchSev_Object(
    (1, 3, 6, 1, 4, 1, 1038, 150, 20, 2, 1, 14),
    _BoardMismatchSev_Type()
)
boardMismatchSev.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    boardMismatchSev.setStatus("current")
_BoardDefectiveSev_Type = Severity
_BoardDefectiveSev_Object = MibTableColumn
boardDefectiveSev = _BoardDefectiveSev_Object(
    (1, 3, 6, 1, 4, 1, 1038, 150, 20, 2, 1, 15),
    _BoardDefectiveSev_Type()
)
boardDefectiveSev.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    boardDefectiveSev.setStatus("current")
_BoardList_ObjectIdentity = ObjectIdentity
boardList = _BoardList_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1038, 150, 30)
)


class _BoardListNumber_Type(Integer32):
    """Custom type boardListNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_BoardListNumber_Type.__name__ = "Integer32"
_BoardListNumber_Object = MibScalar
boardListNumber = _BoardListNumber_Object(
    (1, 3, 6, 1, 4, 1, 1038, 150, 30, 1),
    _BoardListNumber_Type()
)
boardListNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    boardListNumber.setStatus("current")
_BoardListTable_Object = MibTable
boardListTable = _BoardListTable_Object(
    (1, 3, 6, 1, 4, 1, 1038, 150, 30, 2)
)
if mibBuilder.loadTexts:
    boardListTable.setStatus("current")
_BoardListEntry_Object = MibTableRow
boardListEntry = _BoardListEntry_Object(
    (1, 3, 6, 1, 4, 1, 1038, 150, 30, 2, 1)
)
boardListEntry.setIndexNames(
    (0, "SHELF-MIB", "boardListIndex"),
)
if mibBuilder.loadTexts:
    boardListEntry.setStatus("current")


class _BoardListIndex_Type(Integer32):
    """Custom type boardListIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_BoardListIndex_Type.__name__ = "Integer32"
_BoardListIndex_Object = MibTableColumn
boardListIndex = _BoardListIndex_Object(
    (1, 3, 6, 1, 4, 1, 1038, 150, 30, 2, 1, 1),
    _BoardListIndex_Type()
)
boardListIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    boardListIndex.setStatus("current")


class _BoardListSlot_Type(Integer32):
    """Custom type boardListSlot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_BoardListSlot_Type.__name__ = "Integer32"
_BoardListSlot_Object = MibTableColumn
boardListSlot = _BoardListSlot_Object(
    (1, 3, 6, 1, 4, 1, 1038, 150, 30, 2, 1, 2),
    _BoardListSlot_Type()
)
boardListSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    boardListSlot.setStatus("current")
_BoardListType_Type = DisplayString
_BoardListType_Object = MibTableColumn
boardListType = _BoardListType_Object(
    (1, 3, 6, 1, 4, 1, 1038, 150, 30, 2, 1, 3),
    _BoardListType_Type()
)
boardListType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    boardListType.setStatus("current")
_SoftInv_ObjectIdentity = ObjectIdentity
softInv = _SoftInv_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1038, 150, 40)
)


class _SoftInventoryNumber_Type(Integer32):
    """Custom type softInventoryNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_SoftInventoryNumber_Type.__name__ = "Integer32"
_SoftInventoryNumber_Object = MibScalar
softInventoryNumber = _SoftInventoryNumber_Object(
    (1, 3, 6, 1, 4, 1, 1038, 150, 40, 1),
    _SoftInventoryNumber_Type()
)
softInventoryNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    softInventoryNumber.setStatus("current")
_SoftInventoryTable_Object = MibTable
softInventoryTable = _SoftInventoryTable_Object(
    (1, 3, 6, 1, 4, 1, 1038, 150, 40, 2)
)
if mibBuilder.loadTexts:
    softInventoryTable.setStatus("current")
_SoftInventoryEntry_Object = MibTableRow
softInventoryEntry = _SoftInventoryEntry_Object(
    (1, 3, 6, 1, 4, 1, 1038, 150, 40, 2, 1)
)
softInventoryEntry.setIndexNames(
    (0, "SHELF-MIB", "softInventoryIndex"),
)
if mibBuilder.loadTexts:
    softInventoryEntry.setStatus("current")


class _SoftInventoryIndex_Type(Integer32):
    """Custom type softInventoryIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_SoftInventoryIndex_Type.__name__ = "Integer32"
_SoftInventoryIndex_Object = MibTableColumn
softInventoryIndex = _SoftInventoryIndex_Object(
    (1, 3, 6, 1, 4, 1, 1038, 150, 40, 2, 1, 1),
    _SoftInventoryIndex_Type()
)
softInventoryIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    softInventoryIndex.setStatus("current")


class _SoftInventoryBoard_Type(Integer32):
    """Custom type softInventoryBoard based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_SoftInventoryBoard_Type.__name__ = "Integer32"
_SoftInventoryBoard_Object = MibTableColumn
softInventoryBoard = _SoftInventoryBoard_Object(
    (1, 3, 6, 1, 4, 1, 1038, 150, 40, 2, 1, 2),
    _SoftInventoryBoard_Type()
)
softInventoryBoard.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    softInventoryBoard.setStatus("current")
_SoftInventoryType_Type = DisplayString
_SoftInventoryType_Object = MibTableColumn
softInventoryType = _SoftInventoryType_Object(
    (1, 3, 6, 1, 4, 1, 1038, 150, 40, 2, 1, 3),
    _SoftInventoryType_Type()
)
softInventoryType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    softInventoryType.setStatus("current")
_SoftInventoryCode_Type = DisplayString
_SoftInventoryCode_Object = MibTableColumn
softInventoryCode = _SoftInventoryCode_Object(
    (1, 3, 6, 1, 4, 1, 1038, 150, 40, 2, 1, 4),
    _SoftInventoryCode_Type()
)
softInventoryCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    softInventoryCode.setStatus("current")
_SoftInventoryExt_Type = DisplayString
_SoftInventoryExt_Object = MibTableColumn
softInventoryExt = _SoftInventoryExt_Object(
    (1, 3, 6, 1, 4, 1, 1038, 150, 40, 2, 1, 5),
    _SoftInventoryExt_Type()
)
softInventoryExt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    softInventoryExt.setStatus("current")
_HardInv_ObjectIdentity = ObjectIdentity
hardInv = _HardInv_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1038, 150, 50)
)


class _HardInventoryNumber_Type(Integer32):
    """Custom type hardInventoryNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_HardInventoryNumber_Type.__name__ = "Integer32"
_HardInventoryNumber_Object = MibScalar
hardInventoryNumber = _HardInventoryNumber_Object(
    (1, 3, 6, 1, 4, 1, 1038, 150, 50, 1),
    _HardInventoryNumber_Type()
)
hardInventoryNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hardInventoryNumber.setStatus("current")
_HardInventoryTable_Object = MibTable
hardInventoryTable = _HardInventoryTable_Object(
    (1, 3, 6, 1, 4, 1, 1038, 150, 50, 2)
)
if mibBuilder.loadTexts:
    hardInventoryTable.setStatus("current")
_HardInventoryEntry_Object = MibTableRow
hardInventoryEntry = _HardInventoryEntry_Object(
    (1, 3, 6, 1, 4, 1, 1038, 150, 50, 2, 1)
)
hardInventoryEntry.setIndexNames(
    (0, "SHELF-MIB", "hardInventoryIndex"),
)
if mibBuilder.loadTexts:
    hardInventoryEntry.setStatus("current")


class _HardInventoryIndex_Type(Integer32):
    """Custom type hardInventoryIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_HardInventoryIndex_Type.__name__ = "Integer32"
_HardInventoryIndex_Object = MibTableColumn
hardInventoryIndex = _HardInventoryIndex_Object(
    (1, 3, 6, 1, 4, 1, 1038, 150, 50, 2, 1, 1),
    _HardInventoryIndex_Type()
)
hardInventoryIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hardInventoryIndex.setStatus("current")
_HardInventoryBoard_Type = DisplayString
_HardInventoryBoard_Object = MibTableColumn
hardInventoryBoard = _HardInventoryBoard_Object(
    (1, 3, 6, 1, 4, 1, 1038, 150, 50, 2, 1, 2),
    _HardInventoryBoard_Type()
)
hardInventoryBoard.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hardInventoryBoard.setStatus("current")
_HardInventoryDescr_Type = DisplayString
_HardInventoryDescr_Object = MibTableColumn
hardInventoryDescr = _HardInventoryDescr_Object(
    (1, 3, 6, 1, 4, 1, 1038, 150, 50, 2, 1, 3),
    _HardInventoryDescr_Type()
)
hardInventoryDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hardInventoryDescr.setStatus("current")
_Laser_ObjectIdentity = ObjectIdentity
laser = _Laser_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1038, 150, 100)
)


class _LaserNumber_Type(Integer32):
    """Custom type laserNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_LaserNumber_Type.__name__ = "Integer32"
_LaserNumber_Object = MibScalar
laserNumber = _LaserNumber_Object(
    (1, 3, 6, 1, 4, 1, 1038, 150, 100, 1),
    _LaserNumber_Type()
)
laserNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    laserNumber.setStatus("current")
_LaserTable_Object = MibTable
laserTable = _LaserTable_Object(
    (1, 3, 6, 1, 4, 1, 1038, 150, 100, 2)
)
if mibBuilder.loadTexts:
    laserTable.setStatus("current")
_LaserEntry_Object = MibTableRow
laserEntry = _LaserEntry_Object(
    (1, 3, 6, 1, 4, 1, 1038, 150, 100, 2, 1)
)
laserEntry.setIndexNames(
    (0, "SHELF-MIB", "laserIndex"),
)
if mibBuilder.loadTexts:
    laserEntry.setStatus("current")


class _LaserIndex_Type(Integer32):
    """Custom type laserIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_LaserIndex_Type.__name__ = "Integer32"
_LaserIndex_Object = MibTableColumn
laserIndex = _LaserIndex_Object(
    (1, 3, 6, 1, 4, 1, 1038, 150, 100, 2, 1, 1),
    _LaserIndex_Type()
)
laserIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    laserIndex.setStatus("current")
_LaserTxEnable_Type = SagemBoolean
_LaserTxEnable_Object = MibTableColumn
laserTxEnable = _LaserTxEnable_Object(
    (1, 3, 6, 1, 4, 1, 1038, 150, 100, 2, 1, 2),
    _LaserTxEnable_Type()
)
laserTxEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    laserTxEnable.setStatus("current")
_LaserALSEnable_Type = SagemBoolean
_LaserALSEnable_Object = MibTableColumn
laserALSEnable = _LaserALSEnable_Object(
    (1, 3, 6, 1, 4, 1, 1038, 150, 100, 2, 1, 3),
    _LaserALSEnable_Type()
)
laserALSEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    laserALSEnable.setStatus("current")
_LaserALSRestart2s_Type = SagemBoolean
_LaserALSRestart2s_Object = MibTableColumn
laserALSRestart2s = _LaserALSRestart2s_Object(
    (1, 3, 6, 1, 4, 1, 1038, 150, 100, 2, 1, 4),
    _LaserALSRestart2s_Type()
)
laserALSRestart2s.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    laserALSRestart2s.setStatus("current")
_LaserALSRestart90s_Type = SagemBoolean
_LaserALSRestart90s_Object = MibTableColumn
laserALSRestart90s = _LaserALSRestart90s_Object(
    (1, 3, 6, 1, 4, 1, 1038, 150, 100, 2, 1, 5),
    _LaserALSRestart90s_Type()
)
laserALSRestart90s.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    laserALSRestart90s.setStatus("current")
_Eow_ObjectIdentity = ObjectIdentity
eow = _Eow_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1038, 150, 120)
)


class _EowNumber_Type(Integer32):
    """Custom type eowNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_EowNumber_Type.__name__ = "Integer32"
_EowNumber_Object = MibScalar
eowNumber = _EowNumber_Object(
    (1, 3, 6, 1, 4, 1, 1038, 150, 120, 1),
    _EowNumber_Type()
)
eowNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eowNumber.setStatus("current")
_EowTable_Object = MibTable
eowTable = _EowTable_Object(
    (1, 3, 6, 1, 4, 1, 1038, 150, 120, 2)
)
if mibBuilder.loadTexts:
    eowTable.setStatus("current")
_EowEntry_Object = MibTableRow
eowEntry = _EowEntry_Object(
    (1, 3, 6, 1, 4, 1, 1038, 150, 120, 2, 1)
)
eowEntry.setIndexNames(
    (0, "SHELF-MIB", "eowIndex"),
)
if mibBuilder.loadTexts:
    eowEntry.setStatus("current")


class _EowIndex_Type(Integer32):
    """Custom type eowIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_EowIndex_Type.__name__ = "Integer32"
_EowIndex_Object = MibTableColumn
eowIndex = _EowIndex_Object(
    (1, 3, 6, 1, 4, 1, 1038, 150, 120, 2, 1, 1),
    _EowIndex_Type()
)
eowIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eowIndex.setStatus("current")
_EowName_Type = DisplayString
_EowName_Object = MibTableColumn
eowName = _EowName_Object(
    (1, 3, 6, 1, 4, 1, 1038, 150, 120, 2, 1, 2),
    _EowName_Type()
)
eowName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eowName.setStatus("current")
_EowSrcType_Type = EOWType
_EowSrcType_Object = MibTableColumn
eowSrcType = _EowSrcType_Object(
    (1, 3, 6, 1, 4, 1, 1038, 150, 120, 2, 1, 6),
    _EowSrcType_Type()
)
eowSrcType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eowSrcType.setStatus("current")


class _EowSrcPtr_Type(Integer32):
    """Custom type eowSrcPtr based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_EowSrcPtr_Type.__name__ = "Integer32"
_EowSrcPtr_Object = MibTableColumn
eowSrcPtr = _EowSrcPtr_Object(
    (1, 3, 6, 1, 4, 1, 1038, 150, 120, 2, 1, 7),
    _EowSrcPtr_Type()
)
eowSrcPtr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eowSrcPtr.setStatus("current")
_EowSinkType_Type = EOWType
_EowSinkType_Object = MibTableColumn
eowSinkType = _EowSinkType_Object(
    (1, 3, 6, 1, 4, 1, 1038, 150, 120, 2, 1, 8),
    _EowSinkType_Type()
)
eowSinkType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eowSinkType.setStatus("current")


class _EowSinkPtr_Type(Integer32):
    """Custom type eowSinkPtr based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_EowSinkPtr_Type.__name__ = "Integer32"
_EowSinkPtr_Object = MibTableColumn
eowSinkPtr = _EowSinkPtr_Object(
    (1, 3, 6, 1, 4, 1, 1038, 150, 120, 2, 1, 9),
    _EowSinkPtr_Type()
)
eowSinkPtr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eowSinkPtr.setStatus("current")
_EowClockMode_Type = EOWClockMode
_EowClockMode_Object = MibTableColumn
eowClockMode = _EowClockMode_Object(
    (1, 3, 6, 1, 4, 1, 1038, 150, 120, 2, 1, 10),
    _EowClockMode_Type()
)
eowClockMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eowClockMode.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SHELF-MIB",
    **{"ProtectionType": ProtectionType,
       "BoardFailure": BoardFailure,
       "LedStatus": LedStatus,
       "LedType": LedType,
       "HoldTime": HoldTime,
       "EOWClockMode": EOWClockMode,
       "EOWType": EOWType,
       "shelf": shelf,
       "adrHotReset": adrHotReset,
       "led": led,
       "ledNumber": ledNumber,
       "ledTable": ledTable,
       "ledEntry": ledEntry,
       "ledIndex": ledIndex,
       "ledPosition": ledPosition,
       "ledType": ledType,
       "ledStatus": ledStatus,
       "holdTime": holdTime,
       "adrFailHoldOffTime": adrFailHoldOffTime,
       "adrFailHoldOnTime": adrFailHoldOnTime,
       "board": board,
       "boardNumber": boardNumber,
       "boardTable": boardTable,
       "boardEntry": boardEntry,
       "boardIndex": boardIndex,
       "boardSlotName": boardSlotName,
       "boardExpectType": boardExpectType,
       "boardInsertType": boardInsertType,
       "boardExpectFamily": boardExpectFamily,
       "boardInsertFamily": boardInsertFamily,
       "boardActive": boardActive,
       "boardFirstPortIndex": boardFirstPortIndex,
       "boardProtectionType": boardProtectionType,
       "boardMonitor": boardMonitor,
       "boardFailure": boardFailure,
       "boardSeverity": boardSeverity,
       "boardMissingSev": boardMissingSev,
       "boardMismatchSev": boardMismatchSev,
       "boardDefectiveSev": boardDefectiveSev,
       "boardList": boardList,
       "boardListNumber": boardListNumber,
       "boardListTable": boardListTable,
       "boardListEntry": boardListEntry,
       "boardListIndex": boardListIndex,
       "boardListSlot": boardListSlot,
       "boardListType": boardListType,
       "softInv": softInv,
       "softInventoryNumber": softInventoryNumber,
       "softInventoryTable": softInventoryTable,
       "softInventoryEntry": softInventoryEntry,
       "softInventoryIndex": softInventoryIndex,
       "softInventoryBoard": softInventoryBoard,
       "softInventoryType": softInventoryType,
       "softInventoryCode": softInventoryCode,
       "softInventoryExt": softInventoryExt,
       "hardInv": hardInv,
       "hardInventoryNumber": hardInventoryNumber,
       "hardInventoryTable": hardInventoryTable,
       "hardInventoryEntry": hardInventoryEntry,
       "hardInventoryIndex": hardInventoryIndex,
       "hardInventoryBoard": hardInventoryBoard,
       "hardInventoryDescr": hardInventoryDescr,
       "laser": laser,
       "laserNumber": laserNumber,
       "laserTable": laserTable,
       "laserEntry": laserEntry,
       "laserIndex": laserIndex,
       "laserTxEnable": laserTxEnable,
       "laserALSEnable": laserALSEnable,
       "laserALSRestart2s": laserALSRestart2s,
       "laserALSRestart90s": laserALSRestart90s,
       "eow": eow,
       "eowNumber": eowNumber,
       "eowTable": eowTable,
       "eowEntry": eowEntry,
       "eowIndex": eowIndex,
       "eowName": eowName,
       "eowSrcType": eowSrcType,
       "eowSrcPtr": eowSrcPtr,
       "eowSinkType": eowSinkType,
       "eowSinkPtr": eowSinkPtr,
       "eowClockMode": eowClockMode}
)
