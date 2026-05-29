# SNMP MIB module (PRVT-SYS-INFO-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\telco-systems\binos\PRVT-SYS-INFO-MIB

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

(ipSwitch,
 prvt_products) = mibBuilder.importSymbols(
    "PRVT-SWITCH-MIB",
    "ipSwitch",
    "prvt-products")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

prvtSysInfMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 738, 1, 111, 2)
)
if mibBuilder.loadTexts:
    prvtSysInfMib.setRevisions(
        ("2008-01-01 00:00",
         "2005-10-05 00:00",
         "2005-02-16 00:00",
         "2003-12-09 00:00",
         "2003-05-13 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Software_ObjectIdentity = ObjectIdentity
software = _Software_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 738, 1, 111)
)
_PrvtSysInfNotifications_ObjectIdentity = ObjectIdentity
prvtSysInfNotifications = _PrvtSysInfNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 738, 1, 111, 2, 0)
)
_PrvtSysInfObjects_ObjectIdentity = ObjectIdentity
prvtSysInfObjects = _PrvtSysInfObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 738, 1, 111, 2, 1)
)
_SysMemory_ObjectIdentity = ObjectIdentity
sysMemory = _SysMemory_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 738, 1, 111, 2, 1, 1)
)
_NumBytesFree_Type = Integer32
_NumBytesFree_Object = MibScalar
numBytesFree = _NumBytesFree_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 111, 2, 1, 1, 1),
    _NumBytesFree_Type()
)
numBytesFree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    numBytesFree.setStatus("current")
_NumBlocksFree_Type = Integer32
_NumBlocksFree_Object = MibScalar
numBlocksFree = _NumBlocksFree_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 111, 2, 1, 1, 2),
    _NumBlocksFree_Type()
)
numBlocksFree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    numBlocksFree.setStatus("current")
_AvgBlockSizeFree_Type = Integer32
_AvgBlockSizeFree_Object = MibScalar
avgBlockSizeFree = _AvgBlockSizeFree_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 111, 2, 1, 1, 3),
    _AvgBlockSizeFree_Type()
)
avgBlockSizeFree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    avgBlockSizeFree.setStatus("current")
_MaxBlockSizeFree_Type = Integer32
_MaxBlockSizeFree_Object = MibScalar
maxBlockSizeFree = _MaxBlockSizeFree_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 111, 2, 1, 1, 4),
    _MaxBlockSizeFree_Type()
)
maxBlockSizeFree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    maxBlockSizeFree.setStatus("current")
_NumBytesAlloc_Type = Integer32
_NumBytesAlloc_Object = MibScalar
numBytesAlloc = _NumBytesAlloc_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 111, 2, 1, 1, 5),
    _NumBytesAlloc_Type()
)
numBytesAlloc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    numBytesAlloc.setStatus("current")
_NumBlocksAlloc_Type = Integer32
_NumBlocksAlloc_Object = MibScalar
numBlocksAlloc = _NumBlocksAlloc_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 111, 2, 1, 1, 6),
    _NumBlocksAlloc_Type()
)
numBlocksAlloc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    numBlocksAlloc.setStatus("current")
_AvgBlockSizeAlloc_Type = Integer32
_AvgBlockSizeAlloc_Object = MibScalar
avgBlockSizeAlloc = _AvgBlockSizeAlloc_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 111, 2, 1, 1, 7),
    _AvgBlockSizeAlloc_Type()
)
avgBlockSizeAlloc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    avgBlockSizeAlloc.setStatus("current")
_SysTask_ObjectIdentity = ObjectIdentity
sysTask = _SysTask_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 738, 1, 111, 2, 1, 2)
)
_TaskTable_Object = MibTable
taskTable = _TaskTable_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 111, 2, 1, 2, 1)
)
if mibBuilder.loadTexts:
    taskTable.setStatus("current")
_TaskEntry_Object = MibTableRow
taskEntry = _TaskEntry_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 111, 2, 1, 2, 1, 1)
)
taskEntry.setIndexNames(
    (0, "PRVT-SYS-INFO-MIB", "taskId"),
)
if mibBuilder.loadTexts:
    taskEntry.setStatus("current")


class _TaskId_Type(Integer32):
    """Custom type taskId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_TaskId_Type.__name__ = "Integer32"
_TaskId_Object = MibTableColumn
taskId = _TaskId_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 111, 2, 1, 2, 1, 1, 1),
    _TaskId_Type()
)
taskId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    taskId.setStatus("current")
_TaskName_Type = DisplayString
_TaskName_Object = MibTableColumn
taskName = _TaskName_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 111, 2, 1, 2, 1, 1, 2),
    _TaskName_Type()
)
taskName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    taskName.setStatus("current")
_TaskPriority_Type = Integer32
_TaskPriority_Object = MibTableColumn
taskPriority = _TaskPriority_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 111, 2, 1, 2, 1, 1, 3),
    _TaskPriority_Type()
)
taskPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    taskPriority.setStatus("current")


class _TaskStatus_Type(Integer32):
    """Custom type taskStatus based on Integer32"""
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
        *(("task-ready", 1),
          ("task-suspended", 2),
          ("task-delay", 3),
          ("task-deleted", 4),
          ("task-pend", 5))
    )


_TaskStatus_Type.__name__ = "Integer32"
_TaskStatus_Object = MibTableColumn
taskStatus = _TaskStatus_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 111, 2, 1, 2, 1, 1, 4),
    _TaskStatus_Type()
)
taskStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    taskStatus.setStatus("current")


class _TaskOptions_Type(Bits):
    """Custom type taskOptions based on Bits"""
    namedValues = NamedValues(
        *(("task-supervisor-mode", 0),
          ("task-unbreakable", 1),
          ("task-dealloc-stack", 2),
          ("task-fp-task", 3),
          ("task-stdio", 4),
          ("task-reserved-1", 5),
          ("task-reserved-2", 6),
          ("task-private-env", 7),
          ("task-no-stack-fill", 8))
    )

_TaskOptions_Type.__name__ = "Bits"
_TaskOptions_Object = MibTableColumn
taskOptions = _TaskOptions_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 111, 2, 1, 2, 1, 1, 5),
    _TaskOptions_Type()
)
taskOptions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    taskOptions.setStatus("current")
_TaskMain_Type = DisplayString
_TaskMain_Object = MibTableColumn
taskMain = _TaskMain_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 111, 2, 1, 2, 1, 1, 6),
    _TaskMain_Type()
)
taskMain.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    taskMain.setStatus("current")
_TaskStackPtr_Type = Unsigned32
_TaskStackPtr_Object = MibTableColumn
taskStackPtr = _TaskStackPtr_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 111, 2, 1, 2, 1, 1, 7),
    _TaskStackPtr_Type()
)
taskStackPtr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    taskStackPtr.setStatus("current")
_TaskStackBase_Type = Unsigned32
_TaskStackBase_Object = MibTableColumn
taskStackBase = _TaskStackBase_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 111, 2, 1, 2, 1, 1, 8),
    _TaskStackBase_Type()
)
taskStackBase.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    taskStackBase.setStatus("current")
_TaskStackPos_Type = Unsigned32
_TaskStackPos_Object = MibTableColumn
taskStackPos = _TaskStackPos_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 111, 2, 1, 2, 1, 1, 9),
    _TaskStackPos_Type()
)
taskStackPos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    taskStackPos.setStatus("current")
_TaskStackEnd_Type = Unsigned32
_TaskStackEnd_Object = MibTableColumn
taskStackEnd = _TaskStackEnd_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 111, 2, 1, 2, 1, 1, 10),
    _TaskStackEnd_Type()
)
taskStackEnd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    taskStackEnd.setStatus("current")
_TaskStackSize_Type = Unsigned32
_TaskStackSize_Object = MibTableColumn
taskStackSize = _TaskStackSize_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 111, 2, 1, 2, 1, 1, 11),
    _TaskStackSize_Type()
)
taskStackSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    taskStackSize.setStatus("current")
_TaskStackSizeUsage_Type = Unsigned32
_TaskStackSizeUsage_Object = MibTableColumn
taskStackSizeUsage = _TaskStackSizeUsage_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 111, 2, 1, 2, 1, 1, 12),
    _TaskStackSizeUsage_Type()
)
taskStackSizeUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    taskStackSizeUsage.setStatus("current")
_TaskStackMaxUsed_Type = Unsigned32
_TaskStackMaxUsed_Object = MibTableColumn
taskStackMaxUsed = _TaskStackMaxUsed_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 111, 2, 1, 2, 1, 1, 13),
    _TaskStackMaxUsed_Type()
)
taskStackMaxUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    taskStackMaxUsed.setStatus("current")
_TaskStackFree_Type = Unsigned32
_TaskStackFree_Object = MibTableColumn
taskStackFree = _TaskStackFree_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 111, 2, 1, 2, 1, 1, 14),
    _TaskStackFree_Type()
)
taskStackFree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    taskStackFree.setStatus("current")
_TaskErrorStatus_Type = Integer32
_TaskErrorStatus_Object = MibTableColumn
taskErrorStatus = _TaskErrorStatus_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 111, 2, 1, 2, 1, 1, 15),
    _TaskErrorStatus_Type()
)
taskErrorStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    taskErrorStatus.setStatus("current")
_PrvtSysInfConformance_ObjectIdentity = ObjectIdentity
prvtSysInfConformance = _PrvtSysInfConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 738, 1, 111, 2, 2)
)
_SysInfMIBGroups_ObjectIdentity = ObjectIdentity
sysInfMIBGroups = _SysInfMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 738, 1, 111, 2, 2, 2)
)

# Managed Objects groups


# Notification objects

taskSuspended = NotificationType(
    (1, 3, 6, 1, 4, 1, 738, 1, 111, 2, 0, 1)
)
taskSuspended.setObjects(
      *(("PRVT-SYS-INFO-MIB", "taskName"),
        ("PRVT-SYS-INFO-MIB", "taskId"))
)
if mibBuilder.loadTexts:
    taskSuspended.setStatus(
        "current"
    )


# Notifications groups

sysInfNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 738, 1, 111, 2, 2, 2, 3)
)
sysInfNotificationGroup.setObjects(
    ("PRVT-SYS-INFO-MIB", "taskSuspended")
)
if mibBuilder.loadTexts:
    sysInfNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "PRVT-SYS-INFO-MIB",
    **{"software": software,
       "prvtSysInfMib": prvtSysInfMib,
       "prvtSysInfNotifications": prvtSysInfNotifications,
       "taskSuspended": taskSuspended,
       "prvtSysInfObjects": prvtSysInfObjects,
       "sysMemory": sysMemory,
       "numBytesFree": numBytesFree,
       "numBlocksFree": numBlocksFree,
       "avgBlockSizeFree": avgBlockSizeFree,
       "maxBlockSizeFree": maxBlockSizeFree,
       "numBytesAlloc": numBytesAlloc,
       "numBlocksAlloc": numBlocksAlloc,
       "avgBlockSizeAlloc": avgBlockSizeAlloc,
       "sysTask": sysTask,
       "taskTable": taskTable,
       "taskEntry": taskEntry,
       "taskId": taskId,
       "taskName": taskName,
       "taskPriority": taskPriority,
       "taskStatus": taskStatus,
       "taskOptions": taskOptions,
       "taskMain": taskMain,
       "taskStackPtr": taskStackPtr,
       "taskStackBase": taskStackBase,
       "taskStackPos": taskStackPos,
       "taskStackEnd": taskStackEnd,
       "taskStackSize": taskStackSize,
       "taskStackSizeUsage": taskStackSizeUsage,
       "taskStackMaxUsed": taskStackMaxUsed,
       "taskStackFree": taskStackFree,
       "taskErrorStatus": taskErrorStatus,
       "prvtSysInfConformance": prvtSysInfConformance,
       "sysInfMIBGroups": sysInfMIBGroups,
       "sysInfNotificationGroup": sysInfNotificationGroup}
)
