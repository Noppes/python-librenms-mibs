# SNMP MIB module (LOG-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\sagemcom\LOG-MIB

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

(IntDateTime,
 SagemBoolean,
 Severity) = mibBuilder.importSymbols(
    "EQUIPMENT-MIB",
    "IntDateTime",
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

log = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 1038, 105)
)


# Types definitions



class LogEvent(Integer32):
    """Custom type LogEvent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              10,
              13,
              14,
              20,
              21,
              30)
        )
    )
    namedValues = NamedValues(
        *(("clear", 0),
          ("nonAlarmed", 1),
          ("minor", 2),
          ("major", 3),
          ("critical", 4),
          ("warning", 5),
          ("raise", 10),
          ("event", 13),
          ("switch", 14),
          ("perf", 20),
          ("otherThresholdOverflow", 21),
          ("maintenance", 30))
    )




# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_LogTraps_ObjectIdentity = ObjectIdentity
logTraps = _LogTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1038, 105, 0)
)


class _LogClear_Type(Integer32):
    """Custom type logClear based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            0
        )
    )
    namedValues = NamedValues(
        ("setToClear", 0)
    )


_LogClear_Type.__name__ = "Integer32"
_LogClear_Object = MibScalar
logClear = _LogClear_Object(
    (1, 3, 6, 1, 4, 1, 1038, 105, 1),
    _LogClear_Type()
)
logClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    logClear.setStatus("current")


class _LogCapacity_Type(Integer32):
    """Custom type logCapacity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_LogCapacity_Type.__name__ = "Integer32"
_LogCapacity_Object = MibScalar
logCapacity = _LogCapacity_Object(
    (1, 3, 6, 1, 4, 1, 1038, 105, 2),
    _LogCapacity_Type()
)
logCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    logCapacity.setStatus("current")


class _LogLastEvent_Type(Integer32):
    """Custom type logLastEvent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_LogLastEvent_Type.__name__ = "Integer32"
_LogLastEvent_Object = MibScalar
logLastEvent = _LogLastEvent_Object(
    (1, 3, 6, 1, 4, 1, 1038, 105, 3),
    _LogLastEvent_Type()
)
logLastEvent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    logLastEvent.setStatus("current")


class _LogNumber_Type(Integer32):
    """Custom type logNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_LogNumber_Type.__name__ = "Integer32"
_LogNumber_Object = MibScalar
logNumber = _LogNumber_Object(
    (1, 3, 6, 1, 4, 1, 1038, 105, 4),
    _LogNumber_Type()
)
logNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    logNumber.setStatus("current")
_LogTable_Object = MibTable
logTable = _LogTable_Object(
    (1, 3, 6, 1, 4, 1, 1038, 105, 5)
)
if mibBuilder.loadTexts:
    logTable.setStatus("current")
_LogEntry_Object = MibTableRow
logEntry = _LogEntry_Object(
    (1, 3, 6, 1, 4, 1, 1038, 105, 5, 1)
)
logEntry.setIndexNames(
    (0, "LOG-MIB", "logIndex"),
)
if mibBuilder.loadTexts:
    logEntry.setStatus("current")


class _LogIndex_Type(Integer32):
    """Custom type logIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_LogIndex_Type.__name__ = "Integer32"
_LogIndex_Object = MibTableColumn
logIndex = _LogIndex_Object(
    (1, 3, 6, 1, 4, 1, 1038, 105, 5, 1, 1),
    _LogIndex_Type()
)
logIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    logIndex.setStatus("current")
_LogDate_Type = IntDateTime
_LogDate_Object = MibTableColumn
logDate = _LogDate_Object(
    (1, 3, 6, 1, 4, 1, 1038, 105, 5, 1, 2),
    _LogDate_Type()
)
logDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    logDate.setStatus("current")
_LogObject_Type = ObjectIdentifier
_LogObject_Object = MibTableColumn
logObject = _LogObject_Object(
    (1, 3, 6, 1, 4, 1, 1038, 105, 5, 1, 3),
    _LogObject_Type()
)
logObject.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    logObject.setStatus("current")


class _LogName_Type(DisplayString):
    """Custom type logName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_LogName_Type.__name__ = "DisplayString"
_LogName_Object = MibTableColumn
logName = _LogName_Object(
    (1, 3, 6, 1, 4, 1, 1038, 105, 5, 1, 4),
    _LogName_Type()
)
logName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    logName.setStatus("current")
_LogEvent_Type = LogEvent
_LogEvent_Object = MibTableColumn
logEvent = _LogEvent_Object(
    (1, 3, 6, 1, 4, 1, 1038, 105, 5, 1, 5),
    _LogEvent_Type()
)
logEvent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    logEvent.setStatus("current")


class _LogPC_Type(DisplayString):
    """Custom type logPC based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 50),
    )


_LogPC_Type.__name__ = "DisplayString"
_LogPC_Object = MibTableColumn
logPC = _LogPC_Object(
    (1, 3, 6, 1, 4, 1, 1038, 105, 5, 1, 6),
    _LogPC_Type()
)
logPC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    logPC.setStatus("current")


class _LogAI_Type(DisplayString):
    """Custom type logAI based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_LogAI_Type.__name__ = "DisplayString"
_LogAI_Object = MibTableColumn
logAI = _LogAI_Object(
    (1, 3, 6, 1, 4, 1, 1038, 105, 5, 1, 7),
    _LogAI_Type()
)
logAI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    logAI.setStatus("current")
_LogEquipStatusV2_Type = Severity
_LogEquipStatusV2_Object = MibTableColumn
logEquipStatusV2 = _LogEquipStatusV2_Object(
    (1, 3, 6, 1, 4, 1, 1038, 105, 5, 1, 8),
    _LogEquipStatusV2_Type()
)
logEquipStatusV2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    logEquipStatusV2.setStatus("current")
_LogTrapEnable_Type = SagemBoolean
_LogTrapEnable_Object = MibScalar
logTrapEnable = _LogTrapEnable_Object(
    (1, 3, 6, 1, 4, 1, 1038, 105, 6),
    _LogTrapEnable_Type()
)
logTrapEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    logTrapEnable.setStatus("current")
_LostTrap_ObjectIdentity = ObjectIdentity
lostTrap = _LostTrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1038, 105, 7)
)
_ResendTrapBool_Type = SagemBoolean
_ResendTrapBool_Object = MibScalar
resendTrapBool = _ResendTrapBool_Object(
    (1, 3, 6, 1, 4, 1, 1038, 105, 7, 1),
    _ResendTrapBool_Type()
)
resendTrapBool.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    resendTrapBool.setStatus("current")


class _LogCurrentClear_Type(Integer32):
    """Custom type logCurrentClear based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            0
        )
    )
    namedValues = NamedValues(
        ("setToClear", 0)
    )


_LogCurrentClear_Type.__name__ = "Integer32"
_LogCurrentClear_Object = MibScalar
logCurrentClear = _LogCurrentClear_Object(
    (1, 3, 6, 1, 4, 1, 1038, 105, 101),
    _LogCurrentClear_Type()
)
logCurrentClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    logCurrentClear.setStatus("current")


class _LogCurrentCapacity_Type(Integer32):
    """Custom type logCurrentCapacity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_LogCurrentCapacity_Type.__name__ = "Integer32"
_LogCurrentCapacity_Object = MibScalar
logCurrentCapacity = _LogCurrentCapacity_Object(
    (1, 3, 6, 1, 4, 1, 1038, 105, 102),
    _LogCurrentCapacity_Type()
)
logCurrentCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    logCurrentCapacity.setStatus("current")


class _LogCurrentLastEvent_Type(Integer32):
    """Custom type logCurrentLastEvent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_LogCurrentLastEvent_Type.__name__ = "Integer32"
_LogCurrentLastEvent_Object = MibScalar
logCurrentLastEvent = _LogCurrentLastEvent_Object(
    (1, 3, 6, 1, 4, 1, 1038, 105, 103),
    _LogCurrentLastEvent_Type()
)
logCurrentLastEvent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    logCurrentLastEvent.setStatus("current")


class _LogCurrentNumber_Type(Integer32):
    """Custom type logCurrentNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_LogCurrentNumber_Type.__name__ = "Integer32"
_LogCurrentNumber_Object = MibScalar
logCurrentNumber = _LogCurrentNumber_Object(
    (1, 3, 6, 1, 4, 1, 1038, 105, 104),
    _LogCurrentNumber_Type()
)
logCurrentNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    logCurrentNumber.setStatus("current")
_LogCurrentTable_Object = MibTable
logCurrentTable = _LogCurrentTable_Object(
    (1, 3, 6, 1, 4, 1, 1038, 105, 105)
)
if mibBuilder.loadTexts:
    logCurrentTable.setStatus("current")
_LogCurrentEntry_Object = MibTableRow
logCurrentEntry = _LogCurrentEntry_Object(
    (1, 3, 6, 1, 4, 1, 1038, 105, 105, 1)
)
logCurrentEntry.setIndexNames(
    (0, "LOG-MIB", "logCurrentIndex"),
)
if mibBuilder.loadTexts:
    logCurrentEntry.setStatus("current")


class _LogCurrentIndex_Type(Integer32):
    """Custom type logCurrentIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_LogCurrentIndex_Type.__name__ = "Integer32"
_LogCurrentIndex_Object = MibTableColumn
logCurrentIndex = _LogCurrentIndex_Object(
    (1, 3, 6, 1, 4, 1, 1038, 105, 105, 1, 1),
    _LogCurrentIndex_Type()
)
logCurrentIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    logCurrentIndex.setStatus("current")
_LogCurrentDate_Type = IntDateTime
_LogCurrentDate_Object = MibTableColumn
logCurrentDate = _LogCurrentDate_Object(
    (1, 3, 6, 1, 4, 1, 1038, 105, 105, 1, 2),
    _LogCurrentDate_Type()
)
logCurrentDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    logCurrentDate.setStatus("current")
_LogCurrentObject_Type = ObjectIdentifier
_LogCurrentObject_Object = MibTableColumn
logCurrentObject = _LogCurrentObject_Object(
    (1, 3, 6, 1, 4, 1, 1038, 105, 105, 1, 3),
    _LogCurrentObject_Type()
)
logCurrentObject.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    logCurrentObject.setStatus("current")


class _LogCurrentName_Type(DisplayString):
    """Custom type logCurrentName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_LogCurrentName_Type.__name__ = "DisplayString"
_LogCurrentName_Object = MibTableColumn
logCurrentName = _LogCurrentName_Object(
    (1, 3, 6, 1, 4, 1, 1038, 105, 105, 1, 4),
    _LogCurrentName_Type()
)
logCurrentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    logCurrentName.setStatus("current")
_LogCurrentEvent_Type = LogEvent
_LogCurrentEvent_Object = MibTableColumn
logCurrentEvent = _LogCurrentEvent_Object(
    (1, 3, 6, 1, 4, 1, 1038, 105, 105, 1, 5),
    _LogCurrentEvent_Type()
)
logCurrentEvent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    logCurrentEvent.setStatus("current")


class _LogCurrentPC_Type(DisplayString):
    """Custom type logCurrentPC based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 50),
    )


_LogCurrentPC_Type.__name__ = "DisplayString"
_LogCurrentPC_Object = MibTableColumn
logCurrentPC = _LogCurrentPC_Object(
    (1, 3, 6, 1, 4, 1, 1038, 105, 105, 1, 6),
    _LogCurrentPC_Type()
)
logCurrentPC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    logCurrentPC.setStatus("current")


class _LogCurrentAI_Type(DisplayString):
    """Custom type logCurrentAI based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_LogCurrentAI_Type.__name__ = "DisplayString"
_LogCurrentAI_Object = MibTableColumn
logCurrentAI = _LogCurrentAI_Object(
    (1, 3, 6, 1, 4, 1, 1038, 105, 105, 1, 7),
    _LogCurrentAI_Type()
)
logCurrentAI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    logCurrentAI.setStatus("current")
_LogCurrentStatusV2_Type = Severity
_LogCurrentStatusV2_Object = MibTableColumn
logCurrentStatusV2 = _LogCurrentStatusV2_Object(
    (1, 3, 6, 1, 4, 1, 1038, 105, 105, 1, 8),
    _LogCurrentStatusV2_Type()
)
logCurrentStatusV2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    logCurrentStatusV2.setStatus("current")

# Managed Objects groups


# Notification objects

logTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 1038, 105, 0, 1)
)
logTrap.setObjects(
      *(("LOG-MIB", "logIndex"),
        ("LOG-MIB", "logDate"),
        ("LOG-MIB", "logObject"),
        ("LOG-MIB", "logName"),
        ("LOG-MIB", "logEvent"),
        ("LOG-MIB", "logPC"),
        ("LOG-MIB", "logAI"),
        ("LOG-MIB", "logEquipStatusV2"))
)
if mibBuilder.loadTexts:
    logTrap.setStatus(
        "current"
    )

thresholdTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 1038, 105, 0, 2)
)
thresholdTrap.setObjects(
      *(("LOG-MIB", "logIndex"),
        ("LOG-MIB", "logDate"),
        ("LOG-MIB", "logObject"),
        ("LOG-MIB", "logName"),
        ("LOG-MIB", "logEvent"),
        ("LOG-MIB", "logPC"),
        ("LOG-MIB", "logAI"),
        ("LOG-MIB", "logEquipStatusV2"))
)
if mibBuilder.loadTexts:
    thresholdTrap.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "LOG-MIB",
    **{"LogEvent": LogEvent,
       "log": log,
       "logTraps": logTraps,
       "logTrap": logTrap,
       "thresholdTrap": thresholdTrap,
       "logClear": logClear,
       "logCapacity": logCapacity,
       "logLastEvent": logLastEvent,
       "logNumber": logNumber,
       "logTable": logTable,
       "logEntry": logEntry,
       "logIndex": logIndex,
       "logDate": logDate,
       "logObject": logObject,
       "logName": logName,
       "logEvent": logEvent,
       "logPC": logPC,
       "logAI": logAI,
       "logEquipStatusV2": logEquipStatusV2,
       "logTrapEnable": logTrapEnable,
       "lostTrap": lostTrap,
       "resendTrapBool": resendTrapBool,
       "logCurrentClear": logCurrentClear,
       "logCurrentCapacity": logCurrentCapacity,
       "logCurrentLastEvent": logCurrentLastEvent,
       "logCurrentNumber": logCurrentNumber,
       "logCurrentTable": logCurrentTable,
       "logCurrentEntry": logCurrentEntry,
       "logCurrentIndex": logCurrentIndex,
       "logCurrentDate": logCurrentDate,
       "logCurrentObject": logCurrentObject,
       "logCurrentName": logCurrentName,
       "logCurrentEvent": logCurrentEvent,
       "logCurrentPC": logCurrentPC,
       "logCurrentAI": logCurrentAI,
       "logCurrentStatusV2": logCurrentStatusV2}
)
