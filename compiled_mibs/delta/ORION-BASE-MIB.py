# SNMP MIB module (ORION-BASE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\delta\ORION-BASE-MIB

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

(modules,
 orion) = mibBuilder.importSymbols(
    "GLOBAL-REG",
    "modules",
    "orion")

(InetAddress,) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress")

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
 enterprises,
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
    "enterprises",
    "iso")

(DisplayString,
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

orionBaseMibModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 20246, 2, 1, 1, 2)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_OrionBaseMib_ObjectIdentity = ObjectIdentity
orionBaseMib = _OrionBaseMib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1)
)
_ControllerConfs_ObjectIdentity = ObjectIdentity
controllerConfs = _ControllerConfs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 1)
)
_ControllerGroups_ObjectIdentity = ObjectIdentity
controllerGroups = _ControllerGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 1, 1)
)
_ControllerCompl_ObjectIdentity = ObjectIdentity
controllerCompl = _ControllerCompl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 1, 2)
)
_ControllerObjects_ObjectIdentity = ObjectIdentity
controllerObjects = _ControllerObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2)
)
_DcSystemInfo_ObjectIdentity = ObjectIdentity
dcSystemInfo = _DcSystemInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 1)
)


class _DcSiteName_Type(DisplayString):
    """Custom type dcSiteName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_DcSiteName_Type.__name__ = "DisplayString"
_DcSiteName_Object = MibScalar
dcSiteName = _DcSiteName_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 1, 1),
    _DcSiteName_Type()
)
dcSiteName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dcSiteName.setStatus("current")


class _DcSystemName_Type(DisplayString):
    """Custom type dcSystemName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_DcSystemName_Type.__name__ = "DisplayString"
_DcSystemName_Object = MibScalar
dcSystemName = _DcSystemName_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 1, 2),
    _DcSystemName_Type()
)
dcSystemName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dcSystemName.setStatus("current")


class _DcSystemDateTime_Type(DisplayString):
    """Custom type dcSystemDateTime based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(19, 19),
    )
    fixed_length = 19


_DcSystemDateTime_Type.__name__ = "DisplayString"
_DcSystemDateTime_Object = MibScalar
dcSystemDateTime = _DcSystemDateTime_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 1, 3),
    _DcSystemDateTime_Type()
)
dcSystemDateTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dcSystemDateTime.setStatus("current")


class _DcSoftwareVersion_Type(DisplayString):
    """Custom type dcSoftwareVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(10, 12),
    )


_DcSoftwareVersion_Type.__name__ = "DisplayString"
_DcSoftwareVersion_Object = MibScalar
dcSoftwareVersion = _DcSoftwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 1, 4),
    _DcSoftwareVersion_Type()
)
dcSoftwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcSoftwareVersion.setStatus("current")


class _DcCreateInventoryReport_Type(Integer32):
    """Custom type dcCreateInventoryReport based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("create", 1)
    )


_DcCreateInventoryReport_Type.__name__ = "Integer32"
_DcCreateInventoryReport_Object = MibScalar
dcCreateInventoryReport = _DcCreateInventoryReport_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 1, 5),
    _DcCreateInventoryReport_Type()
)
dcCreateInventoryReport.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dcCreateInventoryReport.setStatus("current")
_DcSystemAlarms_ObjectIdentity = ObjectIdentity
dcSystemAlarms = _DcSystemAlarms_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 2)
)
_DcEventHistoryTable_Object = MibTable
dcEventHistoryTable = _DcEventHistoryTable_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 2, 1)
)
if mibBuilder.loadTexts:
    dcEventHistoryTable.setStatus("current")
_DcEventHistoryEntry_Object = MibTableRow
dcEventHistoryEntry = _DcEventHistoryEntry_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 2, 1, 1)
)
dcEventHistoryEntry.setIndexNames(
    (0, "ORION-BASE-MIB", "dcEventHistoryIndex"),
)
if mibBuilder.loadTexts:
    dcEventHistoryEntry.setStatus("current")


class _DcEventHistoryIndex_Type(Integer32):
    """Custom type dcEventHistoryIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10000),
    )


_DcEventHistoryIndex_Type.__name__ = "Integer32"
_DcEventHistoryIndex_Object = MibTableColumn
dcEventHistoryIndex = _DcEventHistoryIndex_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 2, 1, 1, 1),
    _DcEventHistoryIndex_Type()
)
dcEventHistoryIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dcEventHistoryIndex.setStatus("current")


class _DcEventHistoryTimestamp_Type(DisplayString):
    """Custom type dcEventHistoryTimestamp based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(19, 19),
    )
    fixed_length = 19


_DcEventHistoryTimestamp_Type.__name__ = "DisplayString"
_DcEventHistoryTimestamp_Object = MibTableColumn
dcEventHistoryTimestamp = _DcEventHistoryTimestamp_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 2, 1, 1, 2),
    _DcEventHistoryTimestamp_Type()
)
dcEventHistoryTimestamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcEventHistoryTimestamp.setStatus("current")


class _DcEventHistoryMessage_Type(DisplayString):
    """Custom type dcEventHistoryMessage based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_DcEventHistoryMessage_Type.__name__ = "DisplayString"
_DcEventHistoryMessage_Object = MibTableColumn
dcEventHistoryMessage = _DcEventHistoryMessage_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 2, 1, 1, 3),
    _DcEventHistoryMessage_Type()
)
dcEventHistoryMessage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcEventHistoryMessage.setStatus("current")
_DcAlarmTable_Object = MibTable
dcAlarmTable = _DcAlarmTable_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 2, 2)
)
if mibBuilder.loadTexts:
    dcAlarmTable.setStatus("current")
_DcAlarmEntry_Object = MibTableRow
dcAlarmEntry = _DcAlarmEntry_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 2, 2, 1)
)
dcAlarmEntry.setIndexNames(
    (0, "ORION-BASE-MIB", "dcAlarmIndex"),
)
if mibBuilder.loadTexts:
    dcAlarmEntry.setStatus("current")


class _DcAlarmIndex_Type(Integer32):
    """Custom type dcAlarmIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_DcAlarmIndex_Type.__name__ = "Integer32"
_DcAlarmIndex_Object = MibTableColumn
dcAlarmIndex = _DcAlarmIndex_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 2, 2, 1, 1),
    _DcAlarmIndex_Type()
)
dcAlarmIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dcAlarmIndex.setStatus("current")


class _DcAlarmEventCategory_Type(Integer32):
    """Custom type dcAlarmEventCategory based on Integer32"""
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
          ("urgent", 2),
          ("nonUrgent", 3),
          ("critical", 4),
          ("allAlarm", 5))
    )


_DcAlarmEventCategory_Type.__name__ = "Integer32"
_DcAlarmEventCategory_Object = MibTableColumn
dcAlarmEventCategory = _DcAlarmEventCategory_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 2, 2, 1, 2),
    _DcAlarmEventCategory_Type()
)
dcAlarmEventCategory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcAlarmEventCategory.setStatus("current")


class _DcAlarmEventName_Type(DisplayString):
    """Custom type dcAlarmEventName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 35),
    )


_DcAlarmEventName_Type.__name__ = "DisplayString"
_DcAlarmEventName_Object = MibTableColumn
dcAlarmEventName = _DcAlarmEventName_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 2, 2, 1, 3),
    _DcAlarmEventName_Type()
)
dcAlarmEventName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcAlarmEventName.setStatus("current")
_DcAlarmEventIdentifier_Type = Gauge32
_DcAlarmEventIdentifier_Object = MibTableColumn
dcAlarmEventIdentifier = _DcAlarmEventIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 2, 2, 1, 4),
    _DcAlarmEventIdentifier_Type()
)
dcAlarmEventIdentifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcAlarmEventIdentifier.setStatus("current")


class _DcAlarmEventValue_Type(Integer32):
    """Custom type dcAlarmEventValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              3)
        )
    )
    namedValues = NamedValues(
        *(("false", 1),
          ("true", 3))
    )


_DcAlarmEventValue_Type.__name__ = "Integer32"
_DcAlarmEventValue_Object = MibTableColumn
dcAlarmEventValue = _DcAlarmEventValue_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 2, 2, 1, 5),
    _DcAlarmEventValue_Type()
)
dcAlarmEventValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcAlarmEventValue.setStatus("current")
_DcNumberUrgentAlarms_Type = Gauge32
_DcNumberUrgentAlarms_Object = MibScalar
dcNumberUrgentAlarms = _DcNumberUrgentAlarms_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 2, 3),
    _DcNumberUrgentAlarms_Type()
)
dcNumberUrgentAlarms.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcNumberUrgentAlarms.setStatus("current")
_DcNumberNonUrgentAlarms_Type = Gauge32
_DcNumberNonUrgentAlarms_Object = MibScalar
dcNumberNonUrgentAlarms = _DcNumberNonUrgentAlarms_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 2, 4),
    _DcNumberNonUrgentAlarms_Type()
)
dcNumberNonUrgentAlarms.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcNumberNonUrgentAlarms.setStatus("current")


class _DcMainsFailureAlarm_Type(Integer32):
    """Custom type dcMainsFailureAlarm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("inactive", 1),
          ("active", 2))
    )


_DcMainsFailureAlarm_Type.__name__ = "Integer32"
_DcMainsFailureAlarm_Object = MibScalar
dcMainsFailureAlarm = _DcMainsFailureAlarm_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 2, 5),
    _DcMainsFailureAlarm_Type()
)
dcMainsFailureAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcMainsFailureAlarm.setStatus("current")
_DcUrgentAlarmIdentifier_Type = Gauge32
_DcUrgentAlarmIdentifier_Object = MibScalar
dcUrgentAlarmIdentifier = _DcUrgentAlarmIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 2, 6),
    _DcUrgentAlarmIdentifier_Type()
)
dcUrgentAlarmIdentifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcUrgentAlarmIdentifier.setStatus("current")


class _DcUrgentAlarmValue_Type(Integer32):
    """Custom type dcUrgentAlarmValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("false", 1),
          ("indeterminate", 2),
          ("true", 3))
    )


_DcUrgentAlarmValue_Type.__name__ = "Integer32"
_DcUrgentAlarmValue_Object = MibScalar
dcUrgentAlarmValue = _DcUrgentAlarmValue_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 2, 7),
    _DcUrgentAlarmValue_Type()
)
dcUrgentAlarmValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcUrgentAlarmValue.setStatus("current")
_DcNonUrgentAlarmIdentifier_Type = Gauge32
_DcNonUrgentAlarmIdentifier_Object = MibScalar
dcNonUrgentAlarmIdentifier = _DcNonUrgentAlarmIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 2, 8),
    _DcNonUrgentAlarmIdentifier_Type()
)
dcNonUrgentAlarmIdentifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcNonUrgentAlarmIdentifier.setStatus("current")


class _DcNonUrgentAlarmValue_Type(Integer32):
    """Custom type dcNonUrgentAlarmValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("false", 1),
          ("indeterminate", 2),
          ("true", 3))
    )


_DcNonUrgentAlarmValue_Type.__name__ = "Integer32"
_DcNonUrgentAlarmValue_Object = MibScalar
dcNonUrgentAlarmValue = _DcNonUrgentAlarmValue_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 2, 9),
    _DcNonUrgentAlarmValue_Type()
)
dcNonUrgentAlarmValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcNonUrgentAlarmValue.setStatus("current")


class _DcUrgentAlarmName_Type(DisplayString):
    """Custom type dcUrgentAlarmName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 35),
    )


_DcUrgentAlarmName_Type.__name__ = "DisplayString"
_DcUrgentAlarmName_Object = MibScalar
dcUrgentAlarmName = _DcUrgentAlarmName_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 2, 10),
    _DcUrgentAlarmName_Type()
)
dcUrgentAlarmName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcUrgentAlarmName.setStatus("current")


class _DcNonUrgentAlarmName_Type(DisplayString):
    """Custom type dcNonUrgentAlarmName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 35),
    )


_DcNonUrgentAlarmName_Type.__name__ = "DisplayString"
_DcNonUrgentAlarmName_Object = MibScalar
dcNonUrgentAlarmName = _DcNonUrgentAlarmName_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 2, 11),
    _DcNonUrgentAlarmName_Type()
)
dcNonUrgentAlarmName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcNonUrgentAlarmName.setStatus("current")
_DcGenericAlarmTable_Object = MibTable
dcGenericAlarmTable = _DcGenericAlarmTable_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 2, 12)
)
if mibBuilder.loadTexts:
    dcGenericAlarmTable.setStatus("current")
_DcGenericAlarmEntry_Object = MibTableRow
dcGenericAlarmEntry = _DcGenericAlarmEntry_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 2, 12, 1)
)
dcGenericAlarmEntry.setIndexNames(
    (0, "ORION-BASE-MIB", "dcGenericAlarmIndex"),
)
if mibBuilder.loadTexts:
    dcGenericAlarmEntry.setStatus("current")


class _DcGenericAlarmIndex_Type(Integer32):
    """Custom type dcGenericAlarmIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_DcGenericAlarmIndex_Type.__name__ = "Integer32"
_DcGenericAlarmIndex_Object = MibTableColumn
dcGenericAlarmIndex = _DcGenericAlarmIndex_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 2, 12, 1, 1),
    _DcGenericAlarmIndex_Type()
)
dcGenericAlarmIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dcGenericAlarmIndex.setStatus("current")


class _DcGenericAlarmEventName_Type(DisplayString):
    """Custom type dcGenericAlarmEventName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 35),
    )


_DcGenericAlarmEventName_Type.__name__ = "DisplayString"
_DcGenericAlarmEventName_Object = MibTableColumn
dcGenericAlarmEventName = _DcGenericAlarmEventName_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 2, 12, 1, 2),
    _DcGenericAlarmEventName_Type()
)
dcGenericAlarmEventName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcGenericAlarmEventName.setStatus("current")
_DcGenericAlarmEventIdentifier_Type = Gauge32
_DcGenericAlarmEventIdentifier_Object = MibTableColumn
dcGenericAlarmEventIdentifier = _DcGenericAlarmEventIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 2, 12, 1, 3),
    _DcGenericAlarmEventIdentifier_Type()
)
dcGenericAlarmEventIdentifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcGenericAlarmEventIdentifier.setStatus("current")


class _DcGenericAlarmEventValue_Type(Integer32):
    """Custom type dcGenericAlarmEventValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 1),
          ("true", 2))
    )


_DcGenericAlarmEventValue_Type.__name__ = "Integer32"
_DcGenericAlarmEventValue_Object = MibTableColumn
dcGenericAlarmEventValue = _DcGenericAlarmEventValue_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 2, 12, 1, 4),
    _DcGenericAlarmEventValue_Type()
)
dcGenericAlarmEventValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcGenericAlarmEventValue.setStatus("current")
_DcNumberCriticalAlarms_Type = Gauge32
_DcNumberCriticalAlarms_Object = MibScalar
dcNumberCriticalAlarms = _DcNumberCriticalAlarms_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 2, 13),
    _DcNumberCriticalAlarms_Type()
)
dcNumberCriticalAlarms.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcNumberCriticalAlarms.setStatus("current")
_DcCriticalAlarmIdentifier_Type = Gauge32
_DcCriticalAlarmIdentifier_Object = MibScalar
dcCriticalAlarmIdentifier = _DcCriticalAlarmIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 2, 14),
    _DcCriticalAlarmIdentifier_Type()
)
dcCriticalAlarmIdentifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcCriticalAlarmIdentifier.setStatus("current")


class _DcCriticalAlarmValue_Type(Integer32):
    """Custom type dcCriticalAlarmValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("false", 1),
          ("indeterminate", 2),
          ("true", 3))
    )


_DcCriticalAlarmValue_Type.__name__ = "Integer32"
_DcCriticalAlarmValue_Object = MibScalar
dcCriticalAlarmValue = _DcCriticalAlarmValue_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 2, 15),
    _DcCriticalAlarmValue_Type()
)
dcCriticalAlarmValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcCriticalAlarmValue.setStatus("current")


class _DcCriticalAlarmName_Type(DisplayString):
    """Custom type dcCriticalAlarmName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 35),
    )


_DcCriticalAlarmName_Type.__name__ = "DisplayString"
_DcCriticalAlarmName_Object = MibScalar
dcCriticalAlarmName = _DcCriticalAlarmName_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 2, 16),
    _DcCriticalAlarmName_Type()
)
dcCriticalAlarmName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcCriticalAlarmName.setStatus("current")
_DcNumberAllAlarms_Type = Gauge32
_DcNumberAllAlarms_Object = MibScalar
dcNumberAllAlarms = _DcNumberAllAlarms_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 2, 17),
    _DcNumberAllAlarms_Type()
)
dcNumberAllAlarms.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcNumberAllAlarms.setStatus("current")
_DcAllAlarmIdentifier_Type = Gauge32
_DcAllAlarmIdentifier_Object = MibScalar
dcAllAlarmIdentifier = _DcAllAlarmIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 2, 18),
    _DcAllAlarmIdentifier_Type()
)
dcAllAlarmIdentifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcAllAlarmIdentifier.setStatus("current")


class _DcAllAlarmValue_Type(Integer32):
    """Custom type dcAllAlarmValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("false", 1),
          ("indeterminate", 2),
          ("true", 3))
    )


_DcAllAlarmValue_Type.__name__ = "Integer32"
_DcAllAlarmValue_Object = MibScalar
dcAllAlarmValue = _DcAllAlarmValue_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 2, 19),
    _DcAllAlarmValue_Type()
)
dcAllAlarmValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcAllAlarmValue.setStatus("current")


class _DcAllAlarmName_Type(DisplayString):
    """Custom type dcAllAlarmName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 35),
    )


_DcAllAlarmName_Type.__name__ = "DisplayString"
_DcAllAlarmName_Object = MibScalar
dcAllAlarmName = _DcAllAlarmName_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 2, 20),
    _DcAllAlarmName_Type()
)
dcAllAlarmName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcAllAlarmName.setStatus("current")
_DcSystemMonitor_ObjectIdentity = ObjectIdentity
dcSystemMonitor = _DcSystemMonitor_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 3)
)
_DcSystemVoltage_Type = Integer32
_DcSystemVoltage_Object = MibScalar
dcSystemVoltage = _DcSystemVoltage_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 3, 1),
    _DcSystemVoltage_Type()
)
dcSystemVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcSystemVoltage.setStatus("current")
if mibBuilder.loadTexts:
    dcSystemVoltage.setUnits("10 mV")
_DcLoadCurrent_Type = Integer32
_DcLoadCurrent_Object = MibScalar
dcLoadCurrent = _DcLoadCurrent_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 3, 2),
    _DcLoadCurrent_Type()
)
dcLoadCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcLoadCurrent.setStatus("current")
if mibBuilder.loadTexts:
    dcLoadCurrent.setUnits("100 mA")
_DcBatteryCurrent_Type = Integer32
_DcBatteryCurrent_Object = MibScalar
dcBatteryCurrent = _DcBatteryCurrent_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 3, 3),
    _DcBatteryCurrent_Type()
)
dcBatteryCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcBatteryCurrent.setStatus("current")
if mibBuilder.loadTexts:
    dcBatteryCurrent.setUnits("100 mA")
_DcBatteryTemperature_Type = Integer32
_DcBatteryTemperature_Object = MibScalar
dcBatteryTemperature = _DcBatteryTemperature_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 3, 4),
    _DcBatteryTemperature_Type()
)
dcBatteryTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcBatteryTemperature.setStatus("current")
if mibBuilder.loadTexts:
    dcBatteryTemperature.setUnits("0.1 degree")


class _DcChargeState_Type(Integer32):
    """Custom type dcChargeState based on Integer32"""
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
        *(("float", 1),
          ("discharge", 2),
          ("equalize", 3),
          ("boost", 4),
          ("battTest", 5),
          ("recharge", 6),
          ("sepCharge", 7),
          ("evCtrlCharge", 8))
    )


_DcChargeState_Type.__name__ = "Integer32"
_DcChargeState_Object = MibScalar
dcChargeState = _DcChargeState_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 3, 5),
    _DcChargeState_Type()
)
dcChargeState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcChargeState.setStatus("current")


class _DcCurrentLimit_Type(Integer32):
    """Custom type dcCurrentLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("inactive", 1),
          ("active", 2))
    )


_DcCurrentLimit_Type.__name__ = "Integer32"
_DcCurrentLimit_Object = MibScalar
dcCurrentLimit = _DcCurrentLimit_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 3, 6),
    _DcCurrentLimit_Type()
)
dcCurrentLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcCurrentLimit.setStatus("current")
_DcRectifierCurrent_Type = Integer32
_DcRectifierCurrent_Object = MibScalar
dcRectifierCurrent = _DcRectifierCurrent_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 3, 7),
    _DcRectifierCurrent_Type()
)
dcRectifierCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcRectifierCurrent.setStatus("current")
if mibBuilder.loadTexts:
    dcRectifierCurrent.setUnits("100 mA")
_DcSystemPower_Type = Integer32
_DcSystemPower_Object = MibScalar
dcSystemPower = _DcSystemPower_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 3, 8),
    _DcSystemPower_Type()
)
dcSystemPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcSystemPower.setStatus("current")
if mibBuilder.loadTexts:
    dcSystemPower.setUnits("1 W")
_DcRectifier_ObjectIdentity = ObjectIdentity
dcRectifier = _DcRectifier_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 4)
)


class _DcNumberRectifiers_Type(Gauge32):
    """Custom type dcNumberRectifiers based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_DcNumberRectifiers_Type.__name__ = "Gauge32"
_DcNumberRectifiers_Object = MibScalar
dcNumberRectifiers = _DcNumberRectifiers_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 4, 1),
    _DcNumberRectifiers_Type()
)
dcNumberRectifiers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcNumberRectifiers.setStatus("current")


class _DcNumberRectifiersFailure_Type(Gauge32):
    """Custom type dcNumberRectifiersFailure based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_DcNumberRectifiersFailure_Type.__name__ = "Gauge32"
_DcNumberRectifiersFailure_Object = MibScalar
dcNumberRectifiersFailure = _DcNumberRectifiersFailure_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 4, 2),
    _DcNumberRectifiersFailure_Type()
)
dcNumberRectifiersFailure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcNumberRectifiersFailure.setStatus("current")


class _DcNumberRectifiersOkay_Type(Gauge32):
    """Custom type dcNumberRectifiersOkay based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_DcNumberRectifiersOkay_Type.__name__ = "Gauge32"
_DcNumberRectifiersOkay_Object = MibScalar
dcNumberRectifiersOkay = _DcNumberRectifiersOkay_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 4, 3),
    _DcNumberRectifiersOkay_Type()
)
dcNumberRectifiersOkay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcNumberRectifiersOkay.setStatus("current")
_DcRectifierTable_Object = MibTable
dcRectifierTable = _DcRectifierTable_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 4, 4)
)
if mibBuilder.loadTexts:
    dcRectifierTable.setStatus("current")
_DcRectifierEntry_Object = MibTableRow
dcRectifierEntry = _DcRectifierEntry_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 4, 4, 1)
)
dcRectifierEntry.setIndexNames(
    (0, "ORION-BASE-MIB", "dcRectifierIndex"),
)
if mibBuilder.loadTexts:
    dcRectifierEntry.setStatus("current")


class _DcRectifierIndex_Type(Integer32):
    """Custom type dcRectifierIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 128),
    )


_DcRectifierIndex_Type.__name__ = "Integer32"
_DcRectifierIndex_Object = MibTableColumn
dcRectifierIndex = _DcRectifierIndex_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 4, 4, 1, 1),
    _DcRectifierIndex_Type()
)
dcRectifierIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dcRectifierIndex.setStatus("current")


class _DcRectifierIdentifier_Type(DisplayString):
    """Custom type dcRectifierIdentifier based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_DcRectifierIdentifier_Type.__name__ = "DisplayString"
_DcRectifierIdentifier_Object = MibTableColumn
dcRectifierIdentifier = _DcRectifierIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 4, 4, 1, 2),
    _DcRectifierIdentifier_Type()
)
dcRectifierIdentifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcRectifierIdentifier.setStatus("current")


class _DcRectifierSlotState_Type(Integer32):
    """Custom type dcRectifierSlotState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("noPos", 1),
          ("empty", 2),
          ("lost", 3),
          ("new", 4),
          ("off", 5),
          ("on", 6))
    )


_DcRectifierSlotState_Type.__name__ = "Integer32"
_DcRectifierSlotState_Object = MibTableColumn
dcRectifierSlotState = _DcRectifierSlotState_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 4, 4, 1, 3),
    _DcRectifierSlotState_Type()
)
dcRectifierSlotState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcRectifierSlotState.setStatus("current")


class _DcRectifierMainStatus_Type(Integer32):
    """Custom type dcRectifierMainStatus based on Integer32"""
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
        *(("unknown", 1),
          ("on", 2),
          ("remoteOff", 3),
          ("off", 4),
          ("temporaryInternalOff", 5),
          ("latchedInternalOff", 6),
          ("error", 7),
          ("notAuthenticated", 8))
    )


_DcRectifierMainStatus_Type.__name__ = "Integer32"
_DcRectifierMainStatus_Object = MibTableColumn
dcRectifierMainStatus = _DcRectifierMainStatus_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 4, 4, 1, 4),
    _DcRectifierMainStatus_Type()
)
dcRectifierMainStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcRectifierMainStatus.setStatus("current")


class _DcRectifierConfiguration_Type(Integer32):
    """Custom type dcRectifierConfiguration based on Integer32"""
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
        *(("unknown", 1),
          ("ok", 2),
          ("default", 3),
          ("error", 4))
    )


_DcRectifierConfiguration_Type.__name__ = "Integer32"
_DcRectifierConfiguration_Object = MibTableColumn
dcRectifierConfiguration = _DcRectifierConfiguration_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 4, 4, 1, 5),
    _DcRectifierConfiguration_Type()
)
dcRectifierConfiguration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcRectifierConfiguration.setStatus("current")
_DcRectifierIout_Type = Integer32
_DcRectifierIout_Object = MibTableColumn
dcRectifierIout = _DcRectifierIout_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 4, 4, 1, 6),
    _DcRectifierIout_Type()
)
dcRectifierIout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcRectifierIout.setStatus("current")
if mibBuilder.loadTexts:
    dcRectifierIout.setUnits("100 mA")
_DcRectifierPout_Type = Integer32
_DcRectifierPout_Object = MibTableColumn
dcRectifierPout = _DcRectifierPout_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 4, 4, 1, 7),
    _DcRectifierPout_Type()
)
dcRectifierPout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcRectifierPout.setStatus("current")
if mibBuilder.loadTexts:
    dcRectifierPout.setUnits("W")
_DcRectifierGroupTable_Object = MibTable
dcRectifierGroupTable = _DcRectifierGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 4, 5)
)
if mibBuilder.loadTexts:
    dcRectifierGroupTable.setStatus("current")
_DcRectifierGroupEntry_Object = MibTableRow
dcRectifierGroupEntry = _DcRectifierGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 4, 5, 1)
)
dcRectifierGroupEntry.setIndexNames(
    (0, "ORION-BASE-MIB", "dcRectifierGroupIndex"),
)
if mibBuilder.loadTexts:
    dcRectifierGroupEntry.setStatus("current")


class _DcRectifierGroupIndex_Type(Integer32):
    """Custom type dcRectifierGroupIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
    )


_DcRectifierGroupIndex_Type.__name__ = "Integer32"
_DcRectifierGroupIndex_Object = MibTableColumn
dcRectifierGroupIndex = _DcRectifierGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 4, 5, 1, 1),
    _DcRectifierGroupIndex_Type()
)
dcRectifierGroupIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dcRectifierGroupIndex.setStatus("current")


class _DcRectifierGroupName_Type(DisplayString):
    """Custom type dcRectifierGroupName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_DcRectifierGroupName_Type.__name__ = "DisplayString"
_DcRectifierGroupName_Object = MibTableColumn
dcRectifierGroupName = _DcRectifierGroupName_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 4, 5, 1, 2),
    _DcRectifierGroupName_Type()
)
dcRectifierGroupName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcRectifierGroupName.setStatus("current")


class _DcRectifierGroupRectifierType_Type(Integer32):
    """Custom type dcRectifierGroupRectifierType based on Integer32"""
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
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19,
              20,
              21,
              22,
              23,
              24,
              25,
              26,
              27,
              28,
              29,
              30,
              31,
              32,
              33,
              34,
              35,
              36,
              37,
              38,
              39)
        )
    )
    namedValues = NamedValues(
        *(("unknown48V", 1),
          ("fR48V2000W", 2),
          ("dPR1200B48", 3),
          ("dPR1500B48", 4),
          ("dPR600B48", 5),
          ("dPR7200B48", 6),
          ("fR48to60V2000W", 7),
          ("unknown24V", 8),
          ("unknown60V", 9),
          ("dPR600B60", 10),
          ("dPR3500B48", 11),
          ("dPR3500B24", 12),
          ("dPR300B48", 13),
          ("dPR1600B48", 14),
          ("dPR2700B48", 15),
          ("dPR2400B48", 16),
          ("dPR4000B48", 17),
          ("dPR2900B48", 18),
          ("dPR4000B48to60", 19),
          ("dPR850B48", 20),
          ("dPR2000B48", 21),
          ("dPR6000B48A1", 22),
          ("dPR6000B48B1", 23),
          ("dPR4815B", 24),
          ("dPR24100B", 25),
          ("dPR3000", 26),
          ("eSR4856FF", 27),
          ("dPR2900F48A1", 28),
          ("dPR4000B48A5", 29),
          ("dPR6000B48A1forChineseMarket", 30),
          ("dPR2500F48A1", 31),
          ("dPR3000B48", 32),
          ("dPR1000B48", 33),
          ("dPR12000240", 34),
          ("dPR12000336", 35),
          ("dPR3000B48A4", 36),
          ("dPR1800B48A1", 37),
          ("dPR1800B48A2", 38),
          ("dPR6000B48A2", 39))
    )


_DcRectifierGroupRectifierType_Type.__name__ = "Integer32"
_DcRectifierGroupRectifierType_Object = MibTableColumn
dcRectifierGroupRectifierType = _DcRectifierGroupRectifierType_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 4, 5, 1, 3),
    _DcRectifierGroupRectifierType_Type()
)
dcRectifierGroupRectifierType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcRectifierGroupRectifierType.setStatus("current")
_DcRectifierGroupDefaultVoltage_Type = Integer32
_DcRectifierGroupDefaultVoltage_Object = MibTableColumn
dcRectifierGroupDefaultVoltage = _DcRectifierGroupDefaultVoltage_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 4, 5, 1, 4),
    _DcRectifierGroupDefaultVoltage_Type()
)
dcRectifierGroupDefaultVoltage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dcRectifierGroupDefaultVoltage.setStatus("current")
if mibBuilder.loadTexts:
    dcRectifierGroupDefaultVoltage.setUnits("10 mV")
_DcRectifierGroupDefaultCurrentLimit_Type = Integer32
_DcRectifierGroupDefaultCurrentLimit_Object = MibTableColumn
dcRectifierGroupDefaultCurrentLimit = _DcRectifierGroupDefaultCurrentLimit_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 4, 5, 1, 5),
    _DcRectifierGroupDefaultCurrentLimit_Type()
)
dcRectifierGroupDefaultCurrentLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dcRectifierGroupDefaultCurrentLimit.setStatus("current")
if mibBuilder.loadTexts:
    dcRectifierGroupDefaultCurrentLimit.setUnits("100 mA")
_DcRectifierGroupDefaultPowerLimit_Type = Integer32
_DcRectifierGroupDefaultPowerLimit_Object = MibTableColumn
dcRectifierGroupDefaultPowerLimit = _DcRectifierGroupDefaultPowerLimit_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 4, 5, 1, 6),
    _DcRectifierGroupDefaultPowerLimit_Type()
)
dcRectifierGroupDefaultPowerLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dcRectifierGroupDefaultPowerLimit.setStatus("current")
if mibBuilder.loadTexts:
    dcRectifierGroupDefaultPowerLimit.setUnits("1 W")
_DcRectifierGroupInputLowOff_Type = Integer32
_DcRectifierGroupInputLowOff_Object = MibTableColumn
dcRectifierGroupInputLowOff = _DcRectifierGroupInputLowOff_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 4, 5, 1, 7),
    _DcRectifierGroupInputLowOff_Type()
)
dcRectifierGroupInputLowOff.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dcRectifierGroupInputLowOff.setStatus("current")
if mibBuilder.loadTexts:
    dcRectifierGroupInputLowOff.setUnits("100 mV")
_DcRectifierGroupInputLowOn_Type = Integer32
_DcRectifierGroupInputLowOn_Object = MibTableColumn
dcRectifierGroupInputLowOn = _DcRectifierGroupInputLowOn_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 4, 5, 1, 8),
    _DcRectifierGroupInputLowOn_Type()
)
dcRectifierGroupInputLowOn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dcRectifierGroupInputLowOn.setStatus("current")
if mibBuilder.loadTexts:
    dcRectifierGroupInputLowOn.setUnits("100 mV")
_DcRectifierGroupStartupVoltage_Type = Integer32
_DcRectifierGroupStartupVoltage_Object = MibTableColumn
dcRectifierGroupStartupVoltage = _DcRectifierGroupStartupVoltage_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 4, 5, 1, 9),
    _DcRectifierGroupStartupVoltage_Type()
)
dcRectifierGroupStartupVoltage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dcRectifierGroupStartupVoltage.setStatus("current")
if mibBuilder.loadTexts:
    dcRectifierGroupStartupVoltage.setUnits("10 mV")
_DcRectifierGroupStartupCurrentLimit_Type = Integer32
_DcRectifierGroupStartupCurrentLimit_Object = MibTableColumn
dcRectifierGroupStartupCurrentLimit = _DcRectifierGroupStartupCurrentLimit_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 4, 5, 1, 10),
    _DcRectifierGroupStartupCurrentLimit_Type()
)
dcRectifierGroupStartupCurrentLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dcRectifierGroupStartupCurrentLimit.setStatus("current")
if mibBuilder.loadTexts:
    dcRectifierGroupStartupCurrentLimit.setUnits("100 mA")
_DcRectifierGroupStartupPowerLimit_Type = Integer32
_DcRectifierGroupStartupPowerLimit_Object = MibTableColumn
dcRectifierGroupStartupPowerLimit = _DcRectifierGroupStartupPowerLimit_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 4, 5, 1, 11),
    _DcRectifierGroupStartupPowerLimit_Type()
)
dcRectifierGroupStartupPowerLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dcRectifierGroupStartupPowerLimit.setStatus("current")
if mibBuilder.loadTexts:
    dcRectifierGroupStartupPowerLimit.setUnits("1 W")
_DcRectifierGroupStartupLimitTime_Type = Gauge32
_DcRectifierGroupStartupLimitTime_Object = MibTableColumn
dcRectifierGroupStartupLimitTime = _DcRectifierGroupStartupLimitTime_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 4, 5, 1, 12),
    _DcRectifierGroupStartupLimitTime_Type()
)
dcRectifierGroupStartupLimitTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dcRectifierGroupStartupLimitTime.setStatus("current")
if mibBuilder.loadTexts:
    dcRectifierGroupStartupLimitTime.setUnits("10 ms")
_DcRectifierGroupPowerupDelay_Type = Gauge32
_DcRectifierGroupPowerupDelay_Object = MibTableColumn
dcRectifierGroupPowerupDelay = _DcRectifierGroupPowerupDelay_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 4, 5, 1, 13),
    _DcRectifierGroupPowerupDelay_Type()
)
dcRectifierGroupPowerupDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dcRectifierGroupPowerupDelay.setStatus("current")
if mibBuilder.loadTexts:
    dcRectifierGroupPowerupDelay.setUnits("10 ms")
_DcRectifierGroupPowerupTime_Type = Gauge32
_DcRectifierGroupPowerupTime_Object = MibTableColumn
dcRectifierGroupPowerupTime = _DcRectifierGroupPowerupTime_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 4, 5, 1, 14),
    _DcRectifierGroupPowerupTime_Type()
)
dcRectifierGroupPowerupTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dcRectifierGroupPowerupTime.setStatus("current")
if mibBuilder.loadTexts:
    dcRectifierGroupPowerupTime.setUnits("10 ms")
_DcRectifierGroupUmaxOff_Type = Integer32
_DcRectifierGroupUmaxOff_Object = MibTableColumn
dcRectifierGroupUmaxOff = _DcRectifierGroupUmaxOff_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 4, 5, 1, 15),
    _DcRectifierGroupUmaxOff_Type()
)
dcRectifierGroupUmaxOff.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dcRectifierGroupUmaxOff.setStatus("current")
if mibBuilder.loadTexts:
    dcRectifierGroupUmaxOff.setUnits("10 mV")
_DcRectifierFunctions_ObjectIdentity = ObjectIdentity
dcRectifierFunctions = _DcRectifierFunctions_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 4, 6)
)
_DcEfficiencyCycling_ObjectIdentity = ObjectIdentity
dcEfficiencyCycling = _DcEfficiencyCycling_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 4, 6, 1)
)


class _DcEfficiencyCyclingEnabled_Type(Integer32):
    """Custom type dcEfficiencyCyclingEnabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_DcEfficiencyCyclingEnabled_Type.__name__ = "Integer32"
_DcEfficiencyCyclingEnabled_Object = MibScalar
dcEfficiencyCyclingEnabled = _DcEfficiencyCyclingEnabled_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 4, 6, 1, 1),
    _DcEfficiencyCyclingEnabled_Type()
)
dcEfficiencyCyclingEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dcEfficiencyCyclingEnabled.setStatus("current")


class _DcLimitSwitchingTimes_Type(Integer32):
    """Custom type dcLimitSwitchingTimes based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_DcLimitSwitchingTimes_Type.__name__ = "Integer32"
_DcLimitSwitchingTimes_Object = MibScalar
dcLimitSwitchingTimes = _DcLimitSwitchingTimes_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 4, 6, 1, 2),
    _DcLimitSwitchingTimes_Type()
)
dcLimitSwitchingTimes.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dcLimitSwitchingTimes.setStatus("current")


class _DcForceCyclingType_Type(Integer32):
    """Custom type dcForceCyclingType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("never", 1),
          ("day", 2),
          ("thirtydays", 3))
    )


_DcForceCyclingType_Type.__name__ = "Integer32"
_DcForceCyclingType_Object = MibScalar
dcForceCyclingType = _DcForceCyclingType_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 4, 6, 1, 3),
    _DcForceCyclingType_Type()
)
dcForceCyclingType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dcForceCyclingType.setStatus("current")
_DcMinimumPowerReserve_Type = Integer32
_DcMinimumPowerReserve_Object = MibScalar
dcMinimumPowerReserve = _DcMinimumPowerReserve_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 4, 6, 1, 4),
    _DcMinimumPowerReserve_Type()
)
dcMinimumPowerReserve.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dcMinimumPowerReserve.setStatus("current")
if mibBuilder.loadTexts:
    dcMinimumPowerReserve.setUnits("1 W")
_DcMinimumRectifierPower_Type = Integer32
_DcMinimumRectifierPower_Object = MibScalar
dcMinimumRectifierPower = _DcMinimumRectifierPower_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 4, 6, 1, 5),
    _DcMinimumRectifierPower_Type()
)
dcMinimumRectifierPower.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dcMinimumRectifierPower.setStatus("current")
if mibBuilder.loadTexts:
    dcMinimumRectifierPower.setUnits("1 W")
_DcPowerLimitation_ObjectIdentity = ObjectIdentity
dcPowerLimitation = _DcPowerLimitation_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 4, 6, 2)
)
_DcPowerLimitationTable_Object = MibTable
dcPowerLimitationTable = _DcPowerLimitationTable_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 4, 6, 2, 1)
)
if mibBuilder.loadTexts:
    dcPowerLimitationTable.setStatus("current")
_DcPowerLimitationEntry_Object = MibTableRow
dcPowerLimitationEntry = _DcPowerLimitationEntry_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 4, 6, 2, 1, 1)
)
dcPowerLimitationEntry.setIndexNames(
    (0, "ORION-BASE-MIB", "dcPowerLimitationIndex"),
)
if mibBuilder.loadTexts:
    dcPowerLimitationEntry.setStatus("current")


class _DcPowerLimitationIndex_Type(Integer32):
    """Custom type dcPowerLimitationIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_DcPowerLimitationIndex_Type.__name__ = "Integer32"
_DcPowerLimitationIndex_Object = MibTableColumn
dcPowerLimitationIndex = _DcPowerLimitationIndex_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 4, 6, 2, 1, 1, 1),
    _DcPowerLimitationIndex_Type()
)
dcPowerLimitationIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dcPowerLimitationIndex.setStatus("current")


class _DcPowerLimitationEventName_Type(DisplayString):
    """Custom type dcPowerLimitationEventName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 35),
    )


_DcPowerLimitationEventName_Type.__name__ = "DisplayString"
_DcPowerLimitationEventName_Object = MibTableColumn
dcPowerLimitationEventName = _DcPowerLimitationEventName_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 4, 6, 2, 1, 1, 2),
    _DcPowerLimitationEventName_Type()
)
dcPowerLimitationEventName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcPowerLimitationEventName.setStatus("current")


class _DcPowerLimitationStatus_Type(Integer32):
    """Custom type dcPowerLimitationStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("inactive", 2),
          ("powerLimit", 3))
    )


_DcPowerLimitationStatus_Type.__name__ = "Integer32"
_DcPowerLimitationStatus_Object = MibTableColumn
dcPowerLimitationStatus = _DcPowerLimitationStatus_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 4, 6, 2, 1, 1, 3),
    _DcPowerLimitationStatus_Type()
)
dcPowerLimitationStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcPowerLimitationStatus.setStatus("current")


class _DcPowerLimitationType_Type(Integer32):
    """Custom type dcPowerLimitationType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dynamic", 1),
          ("fixedLimit", 2))
    )


_DcPowerLimitationType_Type.__name__ = "Integer32"
_DcPowerLimitationType_Object = MibTableColumn
dcPowerLimitationType = _DcPowerLimitationType_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 4, 6, 2, 1, 1, 4),
    _DcPowerLimitationType_Type()
)
dcPowerLimitationType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcPowerLimitationType.setStatus("current")
_DcMaxTotalRectifierPower_Type = Integer32
_DcMaxTotalRectifierPower_Object = MibTableColumn
dcMaxTotalRectifierPower = _DcMaxTotalRectifierPower_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 4, 6, 2, 1, 1, 5),
    _DcMaxTotalRectifierPower_Type()
)
dcMaxTotalRectifierPower.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dcMaxTotalRectifierPower.setStatus("current")
if mibBuilder.loadTexts:
    dcMaxTotalRectifierPower.setUnits("1 W")


class _DcPowerLimitationNoBatteryDischarge_Type(Integer32):
    """Custom type dcPowerLimitationNoBatteryDischarge based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_DcPowerLimitationNoBatteryDischarge_Type.__name__ = "Integer32"
_DcPowerLimitationNoBatteryDischarge_Object = MibTableColumn
dcPowerLimitationNoBatteryDischarge = _DcPowerLimitationNoBatteryDischarge_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 4, 6, 2, 1, 1, 6),
    _DcPowerLimitationNoBatteryDischarge_Type()
)
dcPowerLimitationNoBatteryDischarge.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dcPowerLimitationNoBatteryDischarge.setStatus("current")
_DcBattery_ObjectIdentity = ObjectIdentity
dcBattery = _DcBattery_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 5)
)
_DcFloatCharge_ObjectIdentity = ObjectIdentity
dcFloatCharge = _DcFloatCharge_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 5, 1)
)
_DcUsys20_Type = Integer32
_DcUsys20_Object = MibScalar
dcUsys20 = _DcUsys20_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 5, 1, 1),
    _DcUsys20_Type()
)
dcUsys20.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dcUsys20.setStatus("current")
if mibBuilder.loadTexts:
    dcUsys20.setUnits("10 mV")
_DcBatteryTest_ObjectIdentity = ObjectIdentity
dcBatteryTest = _DcBatteryTest_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 5, 2)
)
_DcBatteryTestParameter_ObjectIdentity = ObjectIdentity
dcBatteryTestParameter = _DcBatteryTestParameter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 5, 2, 1)
)
_DcBatteryTestUsupport_Type = Integer32
_DcBatteryTestUsupport_Object = MibScalar
dcBatteryTestUsupport = _DcBatteryTestUsupport_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 5, 2, 1, 1),
    _DcBatteryTestUsupport_Type()
)
dcBatteryTestUsupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcBatteryTestUsupport.setStatus("obsolete")
if mibBuilder.loadTexts:
    dcBatteryTestUsupport.setUnits("10 mV")
_DcBatteryTestDuration_Type = Gauge32
_DcBatteryTestDuration_Object = MibScalar
dcBatteryTestDuration = _DcBatteryTestDuration_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 5, 2, 1, 2),
    _DcBatteryTestDuration_Type()
)
dcBatteryTestDuration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcBatteryTestDuration.setStatus("obsolete")
if mibBuilder.loadTexts:
    dcBatteryTestDuration.setUnits("minute")
_DcBatteryTestInterval_Type = Gauge32
_DcBatteryTestInterval_Object = MibScalar
dcBatteryTestInterval = _DcBatteryTestInterval_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 5, 2, 1, 3),
    _DcBatteryTestInterval_Type()
)
dcBatteryTestInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcBatteryTestInterval.setStatus("obsolete")
if mibBuilder.loadTexts:
    dcBatteryTestInterval.setUnits("days")
_DcBatteryTestDischargeCurrent_Type = Integer32
_DcBatteryTestDischargeCurrent_Object = MibScalar
dcBatteryTestDischargeCurrent = _DcBatteryTestDischargeCurrent_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 5, 2, 1, 4),
    _DcBatteryTestDischargeCurrent_Type()
)
dcBatteryTestDischargeCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcBatteryTestDischargeCurrent.setStatus("obsolete")
if mibBuilder.loadTexts:
    dcBatteryTestDischargeCurrent.setUnits("100 mA")
_DcBatteryTestMinDuration_Type = Gauge32
_DcBatteryTestMinDuration_Object = MibScalar
dcBatteryTestMinDuration = _DcBatteryTestMinDuration_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 5, 2, 1, 5),
    _DcBatteryTestMinDuration_Type()
)
dcBatteryTestMinDuration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcBatteryTestMinDuration.setStatus("obsolete")
if mibBuilder.loadTexts:
    dcBatteryTestMinDuration.setUnits("minutes")
_DcBatteryTestVoltageWithinUfloat_Type = Integer32
_DcBatteryTestVoltageWithinUfloat_Object = MibScalar
dcBatteryTestVoltageWithinUfloat = _DcBatteryTestVoltageWithinUfloat_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 5, 2, 1, 6),
    _DcBatteryTestVoltageWithinUfloat_Type()
)
dcBatteryTestVoltageWithinUfloat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcBatteryTestVoltageWithinUfloat.setStatus("obsolete")
if mibBuilder.loadTexts:
    dcBatteryTestVoltageWithinUfloat.setUnits("10 mV")
_DcBatteryTestVoltageWithinUfloatPeriod_Type = Gauge32
_DcBatteryTestVoltageWithinUfloatPeriod_Object = MibScalar
dcBatteryTestVoltageWithinUfloatPeriod = _DcBatteryTestVoltageWithinUfloatPeriod_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 5, 2, 1, 7),
    _DcBatteryTestVoltageWithinUfloatPeriod_Type()
)
dcBatteryTestVoltageWithinUfloatPeriod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcBatteryTestVoltageWithinUfloatPeriod.setStatus("obsolete")
if mibBuilder.loadTexts:
    dcBatteryTestVoltageWithinUfloatPeriod.setUnits("days")
_DcBatteryTestTempFrom_Type = Integer32
_DcBatteryTestTempFrom_Object = MibScalar
dcBatteryTestTempFrom = _DcBatteryTestTempFrom_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 5, 2, 1, 8),
    _DcBatteryTestTempFrom_Type()
)
dcBatteryTestTempFrom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcBatteryTestTempFrom.setStatus("obsolete")
if mibBuilder.loadTexts:
    dcBatteryTestTempFrom.setUnits("0.1 degree")
_DcBatteryTestTempTo_Type = Integer32
_DcBatteryTestTempTo_Object = MibScalar
dcBatteryTestTempTo = _DcBatteryTestTempTo_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 5, 2, 1, 9),
    _DcBatteryTestTempTo_Type()
)
dcBatteryTestTempTo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcBatteryTestTempTo.setStatus("obsolete")
if mibBuilder.loadTexts:
    dcBatteryTestTempTo.setUnits("0.1 degree")


class _DcBatteryTestIntervalEnabled_Type(Integer32):
    """Custom type dcBatteryTestIntervalEnabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_DcBatteryTestIntervalEnabled_Type.__name__ = "Integer32"
_DcBatteryTestIntervalEnabled_Object = MibScalar
dcBatteryTestIntervalEnabled = _DcBatteryTestIntervalEnabled_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 5, 2, 1, 10),
    _DcBatteryTestIntervalEnabled_Type()
)
dcBatteryTestIntervalEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcBatteryTestIntervalEnabled.setStatus("obsolete")


class _DcBatteryTestStartTimeFrom_Type(DisplayString):
    """Custom type dcBatteryTestStartTimeFrom based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )
    fixed_length = 8


_DcBatteryTestStartTimeFrom_Type.__name__ = "DisplayString"
_DcBatteryTestStartTimeFrom_Object = MibScalar
dcBatteryTestStartTimeFrom = _DcBatteryTestStartTimeFrom_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 5, 2, 1, 11),
    _DcBatteryTestStartTimeFrom_Type()
)
dcBatteryTestStartTimeFrom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcBatteryTestStartTimeFrom.setStatus("obsolete")


class _DcBatteryTestStartTimeTo_Type(DisplayString):
    """Custom type dcBatteryTestStartTimeTo based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )
    fixed_length = 8


_DcBatteryTestStartTimeTo_Type.__name__ = "DisplayString"
_DcBatteryTestStartTimeTo_Object = MibScalar
dcBatteryTestStartTimeTo = _DcBatteryTestStartTimeTo_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 5, 2, 1, 12),
    _DcBatteryTestStartTimeTo_Type()
)
dcBatteryTestStartTimeTo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcBatteryTestStartTimeTo.setStatus("obsolete")
_DcBatteryTestResults_ObjectIdentity = ObjectIdentity
dcBatteryTestResults = _DcBatteryTestResults_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 5, 2, 2)
)


class _DcBatteryTestDateTime_Type(DisplayString):
    """Custom type dcBatteryTestDateTime based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(19, 19),
    )
    fixed_length = 19


_DcBatteryTestDateTime_Type.__name__ = "DisplayString"
_DcBatteryTestDateTime_Object = MibScalar
dcBatteryTestDateTime = _DcBatteryTestDateTime_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 5, 2, 2, 1),
    _DcBatteryTestDateTime_Type()
)
dcBatteryTestDateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcBatteryTestDateTime.setStatus("obsolete")


class _DcBatteryTestResult_Type(Integer32):
    """Custom type dcBatteryTestResult based on Integer32"""
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
        *(("none", 1),
          ("failed", 2),
          ("aborted", 3),
          ("loadFailure", 4),
          ("okay", 5),
          ("abortedManual", 6),
          ("abortedEvCtrlCharge", 7),
          ("abortedInhibitEv", 8))
    )


_DcBatteryTestResult_Type.__name__ = "Integer32"
_DcBatteryTestResult_Object = MibScalar
dcBatteryTestResult = _DcBatteryTestResult_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 5, 2, 2, 2),
    _DcBatteryTestResult_Type()
)
dcBatteryTestResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcBatteryTestResult.setStatus("obsolete")
_DcBatteryTestEndVoltage_Type = Integer32
_DcBatteryTestEndVoltage_Object = MibScalar
dcBatteryTestEndVoltage = _DcBatteryTestEndVoltage_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 5, 2, 2, 3),
    _DcBatteryTestEndVoltage_Type()
)
dcBatteryTestEndVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcBatteryTestEndVoltage.setStatus("obsolete")
if mibBuilder.loadTexts:
    dcBatteryTestEndVoltage.setUnits("10 mV")


class _DcBatteryTestControl_Type(Integer32):
    """Custom type dcBatteryTestControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("start", 1),
          ("stop", 2))
    )


_DcBatteryTestControl_Type.__name__ = "Integer32"
_DcBatteryTestControl_Object = MibScalar
dcBatteryTestControl = _DcBatteryTestControl_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 5, 2, 3),
    _DcBatteryTestControl_Type()
)
dcBatteryTestControl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcBatteryTestControl.setStatus("obsolete")


class _DcBatteryTestStatus_Type(Integer32):
    """Custom type dcBatteryTestStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("inactive", 1),
          ("starting", 2),
          ("stopping", 3),
          ("constantCurrent", 4),
          ("recovery", 5),
          ("realLoad", 6))
    )


_DcBatteryTestStatus_Type.__name__ = "Integer32"
_DcBatteryTestStatus_Object = MibScalar
dcBatteryTestStatus = _DcBatteryTestStatus_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 5, 2, 4),
    _DcBatteryTestStatus_Type()
)
dcBatteryTestStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcBatteryTestStatus.setStatus("obsolete")


class _DcBatteryTestFailureEvent_Type(Integer32):
    """Custom type dcBatteryTestFailureEvent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("reset", 1)
    )


_DcBatteryTestFailureEvent_Type.__name__ = "Integer32"
_DcBatteryTestFailureEvent_Object = MibScalar
dcBatteryTestFailureEvent = _DcBatteryTestFailureEvent_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 5, 2, 5),
    _DcBatteryTestFailureEvent_Type()
)
dcBatteryTestFailureEvent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcBatteryTestFailureEvent.setStatus("obsolete")


class _DcBatteryTestType_Type(Integer32):
    """Custom type dcBatteryTestType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("constantCurrent", 2),
          ("realLoad", 3))
    )


_DcBatteryTestType_Type.__name__ = "Integer32"
_DcBatteryTestType_Object = MibScalar
dcBatteryTestType = _DcBatteryTestType_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 5, 2, 6),
    _DcBatteryTestType_Type()
)
dcBatteryTestType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcBatteryTestType.setStatus("obsolete")
_DcBatteryTestTable_Object = MibTable
dcBatteryTestTable = _DcBatteryTestTable_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 5, 2, 7)
)
if mibBuilder.loadTexts:
    dcBatteryTestTable.setStatus("current")
_DcBatteryTestTableEntry_Object = MibTableRow
dcBatteryTestTableEntry = _DcBatteryTestTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 5, 2, 7, 1)
)
dcBatteryTestTableEntry.setIndexNames(
    (0, "ORION-BASE-MIB", "dcBatteryTestTableIndex"),
)
if mibBuilder.loadTexts:
    dcBatteryTestTableEntry.setStatus("current")


class _DcBatteryTestTableIndex_Type(Integer32):
    """Custom type dcBatteryTestTableIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10000),
    )


_DcBatteryTestTableIndex_Type.__name__ = "Integer32"
_DcBatteryTestTableIndex_Object = MibTableColumn
dcBatteryTestTableIndex = _DcBatteryTestTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 5, 2, 7, 1, 1),
    _DcBatteryTestTableIndex_Type()
)
dcBatteryTestTableIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dcBatteryTestTableIndex.setStatus("current")
_DcBatteryTestTablePriority_Type = Unsigned32
_DcBatteryTestTablePriority_Object = MibTableColumn
dcBatteryTestTablePriority = _DcBatteryTestTablePriority_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 5, 2, 7, 1, 2),
    _DcBatteryTestTablePriority_Type()
)
dcBatteryTestTablePriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcBatteryTestTablePriority.setStatus("current")


class _DcBatteryTestTableName_Type(DisplayString):
    """Custom type dcBatteryTestTableName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(32, 32),
    )
    fixed_length = 32


_DcBatteryTestTableName_Type.__name__ = "DisplayString"
_DcBatteryTestTableName_Object = MibTableColumn
dcBatteryTestTableName = _DcBatteryTestTableName_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 5, 2, 7, 1, 3),
    _DcBatteryTestTableName_Type()
)
dcBatteryTestTableName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcBatteryTestTableName.setStatus("current")


class _DcBatteryTestTableType_Type(Integer32):
    """Custom type dcBatteryTestTableType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("constantCurrent", 2),
          ("realLoad", 3))
    )


_DcBatteryTestTableType_Type.__name__ = "Integer32"
_DcBatteryTestTableType_Object = MibTableColumn
dcBatteryTestTableType = _DcBatteryTestTableType_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 5, 2, 7, 1, 4),
    _DcBatteryTestTableType_Type()
)
dcBatteryTestTableType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dcBatteryTestTableType.setStatus("current")


class _DcBatteryTestTableStatus_Type(Integer32):
    """Custom type dcBatteryTestTableStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("inactive", 1),
          ("starting", 2),
          ("stopping", 3),
          ("constantCurrent", 4),
          ("recovery", 5),
          ("realLoad", 6))
    )


_DcBatteryTestTableStatus_Type.__name__ = "Integer32"
_DcBatteryTestTableStatus_Object = MibTableColumn
dcBatteryTestTableStatus = _DcBatteryTestTableStatus_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 5, 2, 7, 1, 5),
    _DcBatteryTestTableStatus_Type()
)
dcBatteryTestTableStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcBatteryTestTableStatus.setStatus("current")
_DcBatteryTestTableUsupport_Type = Integer32
_DcBatteryTestTableUsupport_Object = MibTableColumn
dcBatteryTestTableUsupport = _DcBatteryTestTableUsupport_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 5, 2, 7, 1, 6),
    _DcBatteryTestTableUsupport_Type()
)
dcBatteryTestTableUsupport.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dcBatteryTestTableUsupport.setStatus("current")
if mibBuilder.loadTexts:
    dcBatteryTestTableUsupport.setUnits("10 mV")
_DcBatteryTestTableDuration_Type = Gauge32
_DcBatteryTestTableDuration_Object = MibTableColumn
dcBatteryTestTableDuration = _DcBatteryTestTableDuration_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 5, 2, 7, 1, 7),
    _DcBatteryTestTableDuration_Type()
)
dcBatteryTestTableDuration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dcBatteryTestTableDuration.setStatus("current")
if mibBuilder.loadTexts:
    dcBatteryTestTableDuration.setUnits("minute")
_DcBatteryTestTableInterval_Type = Gauge32
_DcBatteryTestTableInterval_Object = MibTableColumn
dcBatteryTestTableInterval = _DcBatteryTestTableInterval_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 5, 2, 7, 1, 8),
    _DcBatteryTestTableInterval_Type()
)
dcBatteryTestTableInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dcBatteryTestTableInterval.setStatus("current")
if mibBuilder.loadTexts:
    dcBatteryTestTableInterval.setUnits("days")
_DcBatteryTestTableDischargeCurrent_Type = Integer32
_DcBatteryTestTableDischargeCurrent_Object = MibTableColumn
dcBatteryTestTableDischargeCurrent = _DcBatteryTestTableDischargeCurrent_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 5, 2, 7, 1, 9),
    _DcBatteryTestTableDischargeCurrent_Type()
)
dcBatteryTestTableDischargeCurrent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dcBatteryTestTableDischargeCurrent.setStatus("current")
if mibBuilder.loadTexts:
    dcBatteryTestTableDischargeCurrent.setUnits("100 mA")
_DcBatteryTestTableMinDuration_Type = Gauge32
_DcBatteryTestTableMinDuration_Object = MibTableColumn
dcBatteryTestTableMinDuration = _DcBatteryTestTableMinDuration_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 5, 2, 7, 1, 10),
    _DcBatteryTestTableMinDuration_Type()
)
dcBatteryTestTableMinDuration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dcBatteryTestTableMinDuration.setStatus("current")
if mibBuilder.loadTexts:
    dcBatteryTestTableMinDuration.setUnits("minutes")
_DcBatteryTestTableVoltageWithinUfloat_Type = Integer32
_DcBatteryTestTableVoltageWithinUfloat_Object = MibTableColumn
dcBatteryTestTableVoltageWithinUfloat = _DcBatteryTestTableVoltageWithinUfloat_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 5, 2, 7, 1, 11),
    _DcBatteryTestTableVoltageWithinUfloat_Type()
)
dcBatteryTestTableVoltageWithinUfloat.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dcBatteryTestTableVoltageWithinUfloat.setStatus("current")
if mibBuilder.loadTexts:
    dcBatteryTestTableVoltageWithinUfloat.setUnits("10 mV")
_DcBatteryTestTableVoltageWithinUfloatPeriod_Type = Gauge32
_DcBatteryTestTableVoltageWithinUfloatPeriod_Object = MibTableColumn
dcBatteryTestTableVoltageWithinUfloatPeriod = _DcBatteryTestTableVoltageWithinUfloatPeriod_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 5, 2, 7, 1, 12),
    _DcBatteryTestTableVoltageWithinUfloatPeriod_Type()
)
dcBatteryTestTableVoltageWithinUfloatPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dcBatteryTestTableVoltageWithinUfloatPeriod.setStatus("current")
if mibBuilder.loadTexts:
    dcBatteryTestTableVoltageWithinUfloatPeriod.setUnits("days")
_DcBatteryTestTableTempFrom_Type = Integer32
_DcBatteryTestTableTempFrom_Object = MibTableColumn
dcBatteryTestTableTempFrom = _DcBatteryTestTableTempFrom_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 5, 2, 7, 1, 13),
    _DcBatteryTestTableTempFrom_Type()
)
dcBatteryTestTableTempFrom.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dcBatteryTestTableTempFrom.setStatus("current")
if mibBuilder.loadTexts:
    dcBatteryTestTableTempFrom.setUnits("0.1 degree")
_DcBatteryTestTableTempTo_Type = Integer32
_DcBatteryTestTableTempTo_Object = MibTableColumn
dcBatteryTestTableTempTo = _DcBatteryTestTableTempTo_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 5, 2, 7, 1, 14),
    _DcBatteryTestTableTempTo_Type()
)
dcBatteryTestTableTempTo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dcBatteryTestTableTempTo.setStatus("current")
if mibBuilder.loadTexts:
    dcBatteryTestTableTempTo.setUnits("0.1 degree")


class _DcBatteryTestTableIntervalEnabled_Type(Integer32):
    """Custom type dcBatteryTestTableIntervalEnabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_DcBatteryTestTableIntervalEnabled_Type.__name__ = "Integer32"
_DcBatteryTestTableIntervalEnabled_Object = MibTableColumn
dcBatteryTestTableIntervalEnabled = _DcBatteryTestTableIntervalEnabled_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 5, 2, 7, 1, 15),
    _DcBatteryTestTableIntervalEnabled_Type()
)
dcBatteryTestTableIntervalEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dcBatteryTestTableIntervalEnabled.setStatus("current")


class _DcBatteryTestTableStartTimeFrom_Type(DisplayString):
    """Custom type dcBatteryTestTableStartTimeFrom based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )
    fixed_length = 8


_DcBatteryTestTableStartTimeFrom_Type.__name__ = "DisplayString"
_DcBatteryTestTableStartTimeFrom_Object = MibTableColumn
dcBatteryTestTableStartTimeFrom = _DcBatteryTestTableStartTimeFrom_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 5, 2, 7, 1, 16),
    _DcBatteryTestTableStartTimeFrom_Type()
)
dcBatteryTestTableStartTimeFrom.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dcBatteryTestTableStartTimeFrom.setStatus("current")


class _DcBatteryTestTableStartTimeTo_Type(DisplayString):
    """Custom type dcBatteryTestTableStartTimeTo based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )
    fixed_length = 8


_DcBatteryTestTableStartTimeTo_Type.__name__ = "DisplayString"
_DcBatteryTestTableStartTimeTo_Object = MibTableColumn
dcBatteryTestTableStartTimeTo = _DcBatteryTestTableStartTimeTo_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 5, 2, 7, 1, 17),
    _DcBatteryTestTableStartTimeTo_Type()
)
dcBatteryTestTableStartTimeTo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dcBatteryTestTableStartTimeTo.setStatus("current")


class _DcBatteryTestTableControl_Type(Integer32):
    """Custom type dcBatteryTestTableControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("start", 1),
          ("stop", 2))
    )


_DcBatteryTestTableControl_Type.__name__ = "Integer32"
_DcBatteryTestTableControl_Object = MibTableColumn
dcBatteryTestTableControl = _DcBatteryTestTableControl_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 5, 2, 7, 1, 18),
    _DcBatteryTestTableControl_Type()
)
dcBatteryTestTableControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dcBatteryTestTableControl.setStatus("current")


class _DcBatteryTestTableFailureEvent_Type(Integer32):
    """Custom type dcBatteryTestTableFailureEvent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("reset", 1)
    )


_DcBatteryTestTableFailureEvent_Type.__name__ = "Integer32"
_DcBatteryTestTableFailureEvent_Object = MibTableColumn
dcBatteryTestTableFailureEvent = _DcBatteryTestTableFailureEvent_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 5, 2, 7, 1, 19),
    _DcBatteryTestTableFailureEvent_Type()
)
dcBatteryTestTableFailureEvent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dcBatteryTestTableFailureEvent.setStatus("current")
_DcBatteryTestResultTable_Object = MibTable
dcBatteryTestResultTable = _DcBatteryTestResultTable_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 5, 2, 8)
)
if mibBuilder.loadTexts:
    dcBatteryTestResultTable.setStatus("current")
_DcBatteryTestResultTableEntry_Object = MibTableRow
dcBatteryTestResultTableEntry = _DcBatteryTestResultTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 5, 2, 8, 1)
)
dcBatteryTestResultTableEntry.setIndexNames(
    (0, "ORION-BASE-MIB", "dcBatteryTestResultTableIndex"),
)
if mibBuilder.loadTexts:
    dcBatteryTestResultTableEntry.setStatus("current")


class _DcBatteryTestResultTableIndex_Type(Integer32):
    """Custom type dcBatteryTestResultTableIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10000),
    )


_DcBatteryTestResultTableIndex_Type.__name__ = "Integer32"
_DcBatteryTestResultTableIndex_Object = MibTableColumn
dcBatteryTestResultTableIndex = _DcBatteryTestResultTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 5, 2, 8, 1, 1),
    _DcBatteryTestResultTableIndex_Type()
)
dcBatteryTestResultTableIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dcBatteryTestResultTableIndex.setStatus("current")
_DcBatteryTestResultTablePriority_Type = Unsigned32
_DcBatteryTestResultTablePriority_Object = MibTableColumn
dcBatteryTestResultTablePriority = _DcBatteryTestResultTablePriority_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 5, 2, 8, 1, 2),
    _DcBatteryTestResultTablePriority_Type()
)
dcBatteryTestResultTablePriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcBatteryTestResultTablePriority.setStatus("current")


class _DcBatteryTestResultTableName_Type(DisplayString):
    """Custom type dcBatteryTestResultTableName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(32, 32),
    )
    fixed_length = 32


_DcBatteryTestResultTableName_Type.__name__ = "DisplayString"
_DcBatteryTestResultTableName_Object = MibTableColumn
dcBatteryTestResultTableName = _DcBatteryTestResultTableName_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 5, 2, 8, 1, 3),
    _DcBatteryTestResultTableName_Type()
)
dcBatteryTestResultTableName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcBatteryTestResultTableName.setStatus("current")


class _DcBatteryTestResultTableDateTime_Type(DisplayString):
    """Custom type dcBatteryTestResultTableDateTime based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(19, 19),
    )
    fixed_length = 19


_DcBatteryTestResultTableDateTime_Type.__name__ = "DisplayString"
_DcBatteryTestResultTableDateTime_Object = MibTableColumn
dcBatteryTestResultTableDateTime = _DcBatteryTestResultTableDateTime_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 5, 2, 8, 1, 4),
    _DcBatteryTestResultTableDateTime_Type()
)
dcBatteryTestResultTableDateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcBatteryTestResultTableDateTime.setStatus("current")


class _DcBatteryTestResultTableResult_Type(Integer32):
    """Custom type dcBatteryTestResultTableResult based on Integer32"""
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
        *(("none", 1),
          ("failed", 2),
          ("aborted", 3),
          ("loadFailure", 4),
          ("okay", 5),
          ("abortedManual", 6),
          ("abortedEvCtrlCharge", 7),
          ("abortedInhibitEv", 8))
    )


_DcBatteryTestResultTableResult_Type.__name__ = "Integer32"
_DcBatteryTestResultTableResult_Object = MibTableColumn
dcBatteryTestResultTableResult = _DcBatteryTestResultTableResult_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 5, 2, 8, 1, 5),
    _DcBatteryTestResultTableResult_Type()
)
dcBatteryTestResultTableResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcBatteryTestResultTableResult.setStatus("current")
_DcBatteryTestResultTableEndVoltage_Type = Integer32
_DcBatteryTestResultTableEndVoltage_Object = MibTableColumn
dcBatteryTestResultTableEndVoltage = _DcBatteryTestResultTableEndVoltage_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 5, 2, 8, 1, 6),
    _DcBatteryTestResultTableEndVoltage_Type()
)
dcBatteryTestResultTableEndVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcBatteryTestResultTableEndVoltage.setStatus("current")
if mibBuilder.loadTexts:
    dcBatteryTestResultTableEndVoltage.setUnits("10 mV")
_DcBatteryParameter_ObjectIdentity = ObjectIdentity
dcBatteryParameter = _DcBatteryParameter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 5, 3)
)
_DcTotalBatteryCapacity_Type = Gauge32
_DcTotalBatteryCapacity_Object = MibScalar
dcTotalBatteryCapacity = _DcTotalBatteryCapacity_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 5, 3, 1),
    _DcTotalBatteryCapacity_Type()
)
dcTotalBatteryCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcTotalBatteryCapacity.setStatus("current")
if mibBuilder.loadTexts:
    dcTotalBatteryCapacity.setUnits("100 mAh")
_DcBatteryStringTable_Object = MibTable
dcBatteryStringTable = _DcBatteryStringTable_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 5, 3, 2)
)
if mibBuilder.loadTexts:
    dcBatteryStringTable.setStatus("current")
_DcBatteryStringEntry_Object = MibTableRow
dcBatteryStringEntry = _DcBatteryStringEntry_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 5, 3, 2, 1)
)
dcBatteryStringEntry.setIndexNames(
    (0, "ORION-BASE-MIB", "dcBatteryStringIndex"),
)
if mibBuilder.loadTexts:
    dcBatteryStringEntry.setStatus("current")


class _DcBatteryStringIndex_Type(Integer32):
    """Custom type dcBatteryStringIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_DcBatteryStringIndex_Type.__name__ = "Integer32"
_DcBatteryStringIndex_Object = MibTableColumn
dcBatteryStringIndex = _DcBatteryStringIndex_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 5, 3, 2, 1, 1),
    _DcBatteryStringIndex_Type()
)
dcBatteryStringIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dcBatteryStringIndex.setStatus("current")


class _DcBatteryStringName_Type(DisplayString):
    """Custom type dcBatteryStringName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_DcBatteryStringName_Type.__name__ = "DisplayString"
_DcBatteryStringName_Object = MibTableColumn
dcBatteryStringName = _DcBatteryStringName_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 5, 3, 2, 1, 2),
    _DcBatteryStringName_Type()
)
dcBatteryStringName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcBatteryStringName.setStatus("current")
_DcBatteryStringMaxIBatt_Type = Integer32
_DcBatteryStringMaxIBatt_Object = MibTableColumn
dcBatteryStringMaxIBatt = _DcBatteryStringMaxIBatt_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 5, 3, 2, 1, 3),
    _DcBatteryStringMaxIBatt_Type()
)
dcBatteryStringMaxIBatt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dcBatteryStringMaxIBatt.setStatus("current")
if mibBuilder.loadTexts:
    dcBatteryStringMaxIBatt.setUnits("100 mA")
_DcBatteryStringCapacity_Type = Gauge32
_DcBatteryStringCapacity_Object = MibTableColumn
dcBatteryStringCapacity = _DcBatteryStringCapacity_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 5, 3, 2, 1, 4),
    _DcBatteryStringCapacity_Type()
)
dcBatteryStringCapacity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dcBatteryStringCapacity.setStatus("current")
if mibBuilder.loadTexts:
    dcBatteryStringCapacity.setUnits("100 mAh")
_DcLossOfBackupTime_ObjectIdentity = ObjectIdentity
dcLossOfBackupTime = _DcLossOfBackupTime_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 5, 3, 3)
)


class _DcLossOfBackupTimeEnabled_Type(Integer32):
    """Custom type dcLossOfBackupTimeEnabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_DcLossOfBackupTimeEnabled_Type.__name__ = "Integer32"
_DcLossOfBackupTimeEnabled_Object = MibScalar
dcLossOfBackupTimeEnabled = _DcLossOfBackupTimeEnabled_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 5, 3, 3, 1),
    _DcLossOfBackupTimeEnabled_Type()
)
dcLossOfBackupTimeEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dcLossOfBackupTimeEnabled.setStatus("current")


class _DcLossOfBackupTimeStatus_Type(Integer32):
    """Custom type dcLossOfBackupTimeStatus based on Integer32"""
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
        *(("inactive", 1),
          ("ok", 2),
          ("occured", 3),
          ("fail", 4))
    )


_DcLossOfBackupTimeStatus_Type.__name__ = "Integer32"
_DcLossOfBackupTimeStatus_Object = MibScalar
dcLossOfBackupTimeStatus = _DcLossOfBackupTimeStatus_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 5, 3, 3, 2),
    _DcLossOfBackupTimeStatus_Type()
)
dcLossOfBackupTimeStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcLossOfBackupTimeStatus.setStatus("current")
_DcExpectedBackupTime_Type = Gauge32
_DcExpectedBackupTime_Object = MibScalar
dcExpectedBackupTime = _DcExpectedBackupTime_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 5, 3, 3, 3),
    _DcExpectedBackupTime_Type()
)
dcExpectedBackupTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dcExpectedBackupTime.setStatus("current")
if mibBuilder.loadTexts:
    dcExpectedBackupTime.setUnits("minutes")
_DcBatteryLithiumTable_Object = MibTable
dcBatteryLithiumTable = _DcBatteryLithiumTable_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 5, 3, 4)
)
if mibBuilder.loadTexts:
    dcBatteryLithiumTable.setStatus("current")
_DcBatteryLithiumEntry_Object = MibTableRow
dcBatteryLithiumEntry = _DcBatteryLithiumEntry_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 5, 3, 4, 1)
)
dcBatteryLithiumEntry.setIndexNames(
    (0, "ORION-BASE-MIB", "dcBatteryLithiumIndex"),
)
if mibBuilder.loadTexts:
    dcBatteryLithiumEntry.setStatus("current")


class _DcBatteryLithiumIndex_Type(Integer32):
    """Custom type dcBatteryLithiumIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_DcBatteryLithiumIndex_Type.__name__ = "Integer32"
_DcBatteryLithiumIndex_Object = MibTableColumn
dcBatteryLithiumIndex = _DcBatteryLithiumIndex_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 5, 3, 4, 1, 1),
    _DcBatteryLithiumIndex_Type()
)
dcBatteryLithiumIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dcBatteryLithiumIndex.setStatus("current")


class _DcBatteryLithiumName_Type(DisplayString):
    """Custom type dcBatteryLithiumName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_DcBatteryLithiumName_Type.__name__ = "DisplayString"
_DcBatteryLithiumName_Object = MibTableColumn
dcBatteryLithiumName = _DcBatteryLithiumName_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 5, 3, 4, 1, 2),
    _DcBatteryLithiumName_Type()
)
dcBatteryLithiumName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcBatteryLithiumName.setStatus("current")


class _DcBatteryLithiumMainState_Type(Integer32):
    """Custom type dcBatteryLithiumMainState based on Integer32"""
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
              7)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 0),
          ("unknown", 1),
          ("missing", 2),
          ("ok", 3),
          ("warning", 4),
          ("alarm", 5),
          ("error", 6),
          ("remoteOff", 7))
    )


_DcBatteryLithiumMainState_Type.__name__ = "Integer32"
_DcBatteryLithiumMainState_Object = MibTableColumn
dcBatteryLithiumMainState = _DcBatteryLithiumMainState_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 5, 3, 4, 1, 3),
    _DcBatteryLithiumMainState_Type()
)
dcBatteryLithiumMainState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcBatteryLithiumMainState.setStatus("current")


class _DcBatteryLithiumSubState_Type(Integer32):
    """Custom type dcBatteryLithiumSubState based on Integer32"""
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
              11)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 0),
          ("na", 1),
          ("unknown", 2),
          ("float", 3),
          ("charge", 4),
          ("discharge", 5),
          ("highvoltage", 6),
          ("lowvoltage", 7),
          ("temperature", 8),
          ("highcurrent", 9),
          ("internalfailure", 10),
          ("lowSoC", 11))
    )


_DcBatteryLithiumSubState_Type.__name__ = "Integer32"
_DcBatteryLithiumSubState_Object = MibTableColumn
dcBatteryLithiumSubState = _DcBatteryLithiumSubState_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 5, 3, 4, 1, 4),
    _DcBatteryLithiumSubState_Type()
)
dcBatteryLithiumSubState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcBatteryLithiumSubState.setStatus("current")
_DcBatteryLithiumCurrent_Type = Integer32
_DcBatteryLithiumCurrent_Object = MibTableColumn
dcBatteryLithiumCurrent = _DcBatteryLithiumCurrent_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 5, 3, 4, 1, 5),
    _DcBatteryLithiumCurrent_Type()
)
dcBatteryLithiumCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcBatteryLithiumCurrent.setStatus("current")
if mibBuilder.loadTexts:
    dcBatteryLithiumCurrent.setUnits("100 mA")
_DcBatteryLithiumStateOfCharge_Type = Gauge32
_DcBatteryLithiumStateOfCharge_Object = MibTableColumn
dcBatteryLithiumStateOfCharge = _DcBatteryLithiumStateOfCharge_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 5, 3, 4, 1, 6),
    _DcBatteryLithiumStateOfCharge_Type()
)
dcBatteryLithiumStateOfCharge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcBatteryLithiumStateOfCharge.setStatus("current")
if mibBuilder.loadTexts:
    dcBatteryLithiumStateOfCharge.setUnits("%")


class _DcBatteryLithiumInstallationDate_Type(DisplayString):
    """Custom type dcBatteryLithiumInstallationDate based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 11),
    )


_DcBatteryLithiumInstallationDate_Type.__name__ = "DisplayString"
_DcBatteryLithiumInstallationDate_Object = MibTableColumn
dcBatteryLithiumInstallationDate = _DcBatteryLithiumInstallationDate_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 5, 3, 4, 1, 7),
    _DcBatteryLithiumInstallationDate_Type()
)
dcBatteryLithiumInstallationDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcBatteryLithiumInstallationDate.setStatus("current")
_DcBatteryLithiumSoH_Type = Gauge32
_DcBatteryLithiumSoH_Object = MibTableColumn
dcBatteryLithiumSoH = _DcBatteryLithiumSoH_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 5, 3, 4, 1, 8),
    _DcBatteryLithiumSoH_Type()
)
dcBatteryLithiumSoH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcBatteryLithiumSoH.setStatus("current")
if mibBuilder.loadTexts:
    dcBatteryLithiumSoH.setUnits("%")
_DcBatteryLifePredictionTable_Object = MibTable
dcBatteryLifePredictionTable = _DcBatteryLifePredictionTable_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 5, 3, 5)
)
if mibBuilder.loadTexts:
    dcBatteryLifePredictionTable.setStatus("current")
_DcBatteryLifePredictionEntry_Object = MibTableRow
dcBatteryLifePredictionEntry = _DcBatteryLifePredictionEntry_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 5, 3, 5, 1)
)
dcBatteryLifePredictionEntry.setIndexNames(
    (0, "ORION-BASE-MIB", "dcBatteryLifePredictionIndex"),
)
if mibBuilder.loadTexts:
    dcBatteryLifePredictionEntry.setStatus("current")


class _DcBatteryLifePredictionIndex_Type(Integer32):
    """Custom type dcBatteryLifePredictionIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_DcBatteryLifePredictionIndex_Type.__name__ = "Integer32"
_DcBatteryLifePredictionIndex_Object = MibTableColumn
dcBatteryLifePredictionIndex = _DcBatteryLifePredictionIndex_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 5, 3, 5, 1, 1),
    _DcBatteryLifePredictionIndex_Type()
)
dcBatteryLifePredictionIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dcBatteryLifePredictionIndex.setStatus("current")


class _DcBatteryLifePredictionName_Type(DisplayString):
    """Custom type dcBatteryLifePredictionName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_DcBatteryLifePredictionName_Type.__name__ = "DisplayString"
_DcBatteryLifePredictionName_Object = MibTableColumn
dcBatteryLifePredictionName = _DcBatteryLifePredictionName_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 5, 3, 5, 1, 2),
    _DcBatteryLifePredictionName_Type()
)
dcBatteryLifePredictionName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcBatteryLifePredictionName.setStatus("current")
_DcBatteryLifePredictionRemainingDays_Type = Gauge32
_DcBatteryLifePredictionRemainingDays_Object = MibTableColumn
dcBatteryLifePredictionRemainingDays = _DcBatteryLifePredictionRemainingDays_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 5, 3, 5, 1, 3),
    _DcBatteryLifePredictionRemainingDays_Type()
)
dcBatteryLifePredictionRemainingDays.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcBatteryLifePredictionRemainingDays.setStatus("current")
_DcBatteryLifePredictionInstallationDate_Type = DisplayString
_DcBatteryLifePredictionInstallationDate_Object = MibTableColumn
dcBatteryLifePredictionInstallationDate = _DcBatteryLifePredictionInstallationDate_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 5, 3, 5, 1, 4),
    _DcBatteryLifePredictionInstallationDate_Type()
)
dcBatteryLifePredictionInstallationDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcBatteryLifePredictionInstallationDate.setStatus("current")
_DcBatteryLifePredictionSoH_Type = Gauge32
_DcBatteryLifePredictionSoH_Object = MibTableColumn
dcBatteryLifePredictionSoH = _DcBatteryLifePredictionSoH_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 5, 3, 5, 1, 5),
    _DcBatteryLifePredictionSoH_Type()
)
dcBatteryLifePredictionSoH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcBatteryLifePredictionSoH.setStatus("current")


class _DcBatteryLifePredictionStatus_Type(Integer32):
    """Custom type dcBatteryLifePredictionStatus based on Integer32"""
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
        *(("inactive", 1),
          ("ok", 2),
          ("warning", 3),
          ("fail", 4))
    )


_DcBatteryLifePredictionStatus_Type.__name__ = "Integer32"
_DcBatteryLifePredictionStatus_Object = MibScalar
dcBatteryLifePredictionStatus = _DcBatteryLifePredictionStatus_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 5, 3, 6),
    _DcBatteryLifePredictionStatus_Type()
)
dcBatteryLifePredictionStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcBatteryLifePredictionStatus.setStatus("current")


class _DcBatteryChargingCurrentLimitEnable_Type(Integer32):
    """Custom type dcBatteryChargingCurrentLimitEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_DcBatteryChargingCurrentLimitEnable_Type.__name__ = "Integer32"
_DcBatteryChargingCurrentLimitEnable_Object = MibScalar
dcBatteryChargingCurrentLimitEnable = _DcBatteryChargingCurrentLimitEnable_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 5, 3, 7),
    _DcBatteryChargingCurrentLimitEnable_Type()
)
dcBatteryChargingCurrentLimitEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dcBatteryChargingCurrentLimitEnable.setStatus("current")


class _DcBatteryTotalChargingCurrentLimitEnable_Type(Integer32):
    """Custom type dcBatteryTotalChargingCurrentLimitEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_DcBatteryTotalChargingCurrentLimitEnable_Type.__name__ = "Integer32"
_DcBatteryTotalChargingCurrentLimitEnable_Object = MibScalar
dcBatteryTotalChargingCurrentLimitEnable = _DcBatteryTotalChargingCurrentLimitEnable_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 5, 3, 8),
    _DcBatteryTotalChargingCurrentLimitEnable_Type()
)
dcBatteryTotalChargingCurrentLimitEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dcBatteryTotalChargingCurrentLimitEnable.setStatus("current")
_DcBatteryTotalMaxIBatt_Type = Integer32
_DcBatteryTotalMaxIBatt_Object = MibScalar
dcBatteryTotalMaxIBatt = _DcBatteryTotalMaxIBatt_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 5, 3, 9),
    _DcBatteryTotalMaxIBatt_Type()
)
dcBatteryTotalMaxIBatt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dcBatteryTotalMaxIBatt.setStatus("current")
if mibBuilder.loadTexts:
    dcBatteryTotalMaxIBatt.setUnits("100 mA")
_DcEqualize_ObjectIdentity = ObjectIdentity
dcEqualize = _DcEqualize_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 5, 4)
)


class _DcEqualizeControl_Type(Integer32):
    """Custom type dcEqualizeControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("start", 1),
          ("stop", 2))
    )


_DcEqualizeControl_Type.__name__ = "Integer32"
_DcEqualizeControl_Object = MibScalar
dcEqualizeControl = _DcEqualizeControl_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 5, 4, 1),
    _DcEqualizeControl_Type()
)
dcEqualizeControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dcEqualizeControl.setStatus("current")


class _DcEqualizeStatus_Type(Integer32):
    """Custom type dcEqualizeStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("inactive", 1),
          ("starting", 2),
          ("stopping", 3),
          ("preparing", 4),
          ("cooking", 5),
          ("recovering", 6))
    )


_DcEqualizeStatus_Type.__name__ = "Integer32"
_DcEqualizeStatus_Object = MibScalar
dcEqualizeStatus = _DcEqualizeStatus_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 5, 4, 2),
    _DcEqualizeStatus_Type()
)
dcEqualizeStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcEqualizeStatus.setStatus("current")


class _DcEqualizeEnabled_Type(Integer32):
    """Custom type dcEqualizeEnabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_DcEqualizeEnabled_Type.__name__ = "Integer32"
_DcEqualizeEnabled_Object = MibScalar
dcEqualizeEnabled = _DcEqualizeEnabled_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 5, 4, 3),
    _DcEqualizeEnabled_Type()
)
dcEqualizeEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dcEqualizeEnabled.setStatus("current")
_DcEqualizeParameter_ObjectIdentity = ObjectIdentity
dcEqualizeParameter = _DcEqualizeParameter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 5, 4, 4)
)
_DcEqualizeVoltage_Type = Integer32
_DcEqualizeVoltage_Object = MibScalar
dcEqualizeVoltage = _DcEqualizeVoltage_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 5, 4, 4, 1),
    _DcEqualizeVoltage_Type()
)
dcEqualizeVoltage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dcEqualizeVoltage.setStatus("current")
if mibBuilder.loadTexts:
    dcEqualizeVoltage.setUnits("10 mV")
_DcEqualizeDuration_Type = Gauge32
_DcEqualizeDuration_Object = MibScalar
dcEqualizeDuration = _DcEqualizeDuration_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 5, 4, 4, 2),
    _DcEqualizeDuration_Type()
)
dcEqualizeDuration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dcEqualizeDuration.setStatus("current")
if mibBuilder.loadTexts:
    dcEqualizeDuration.setUnits("minutes")


class _DcEqualizeUseBattRoomFanEnabled_Type(Integer32):
    """Custom type dcEqualizeUseBattRoomFanEnabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_DcEqualizeUseBattRoomFanEnabled_Type.__name__ = "Integer32"
_DcEqualizeUseBattRoomFanEnabled_Object = MibScalar
dcEqualizeUseBattRoomFanEnabled = _DcEqualizeUseBattRoomFanEnabled_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 5, 4, 4, 3),
    _DcEqualizeUseBattRoomFanEnabled_Type()
)
dcEqualizeUseBattRoomFanEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dcEqualizeUseBattRoomFanEnabled.setStatus("current")
_DcEqualizeLeadTime_Type = Gauge32
_DcEqualizeLeadTime_Object = MibScalar
dcEqualizeLeadTime = _DcEqualizeLeadTime_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 5, 4, 4, 4),
    _DcEqualizeLeadTime_Type()
)
dcEqualizeLeadTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dcEqualizeLeadTime.setStatus("current")
if mibBuilder.loadTexts:
    dcEqualizeLeadTime.setUnits("minutes")
_DcEqualizeTimeLag_Type = Gauge32
_DcEqualizeTimeLag_Object = MibScalar
dcEqualizeTimeLag = _DcEqualizeTimeLag_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 5, 4, 4, 5),
    _DcEqualizeTimeLag_Type()
)
dcEqualizeTimeLag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dcEqualizeTimeLag.setStatus("current")
if mibBuilder.loadTexts:
    dcEqualizeTimeLag.setUnits("minutes")
_DcEqualizeInterval_Type = Gauge32
_DcEqualizeInterval_Object = MibScalar
dcEqualizeInterval = _DcEqualizeInterval_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 5, 4, 4, 6),
    _DcEqualizeInterval_Type()
)
dcEqualizeInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dcEqualizeInterval.setStatus("current")
if mibBuilder.loadTexts:
    dcEqualizeInterval.setUnits("days")


class _DcEqualizeStartTimeIntervalFrom_Type(DisplayString):
    """Custom type dcEqualizeStartTimeIntervalFrom based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )
    fixed_length = 8


_DcEqualizeStartTimeIntervalFrom_Type.__name__ = "DisplayString"
_DcEqualizeStartTimeIntervalFrom_Object = MibScalar
dcEqualizeStartTimeIntervalFrom = _DcEqualizeStartTimeIntervalFrom_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 5, 4, 4, 7),
    _DcEqualizeStartTimeIntervalFrom_Type()
)
dcEqualizeStartTimeIntervalFrom.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dcEqualizeStartTimeIntervalFrom.setStatus("current")


class _DcEqualizeStartTimeIntervalTo_Type(DisplayString):
    """Custom type dcEqualizeStartTimeIntervalTo based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )
    fixed_length = 8


_DcEqualizeStartTimeIntervalTo_Type.__name__ = "DisplayString"
_DcEqualizeStartTimeIntervalTo_Object = MibScalar
dcEqualizeStartTimeIntervalTo = _DcEqualizeStartTimeIntervalTo_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 5, 4, 4, 8),
    _DcEqualizeStartTimeIntervalTo_Type()
)
dcEqualizeStartTimeIntervalTo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dcEqualizeStartTimeIntervalTo.setStatus("current")
_DcEqualizeInhibitAfterBoost_Type = Gauge32
_DcEqualizeInhibitAfterBoost_Object = MibScalar
dcEqualizeInhibitAfterBoost = _DcEqualizeInhibitAfterBoost_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 5, 4, 4, 9),
    _DcEqualizeInhibitAfterBoost_Type()
)
dcEqualizeInhibitAfterBoost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dcEqualizeInhibitAfterBoost.setStatus("current")
if mibBuilder.loadTexts:
    dcEqualizeInhibitAfterBoost.setUnits("hours")
_DcBoostCharge_ObjectIdentity = ObjectIdentity
dcBoostCharge = _DcBoostCharge_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 5, 5)
)


class _DcBoostChargeControl_Type(Integer32):
    """Custom type dcBoostChargeControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("start", 1),
          ("stop", 2))
    )


_DcBoostChargeControl_Type.__name__ = "Integer32"
_DcBoostChargeControl_Object = MibScalar
dcBoostChargeControl = _DcBoostChargeControl_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 5, 5, 1),
    _DcBoostChargeControl_Type()
)
dcBoostChargeControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dcBoostChargeControl.setStatus("current")


class _DcBoostChargeStatus_Type(Integer32):
    """Custom type dcBoostChargeStatus based on Integer32"""
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
        *(("inactive", 1),
          ("starting", 2),
          ("stopping", 3),
          ("cooking", 4),
          ("recovering", 5))
    )


_DcBoostChargeStatus_Type.__name__ = "Integer32"
_DcBoostChargeStatus_Object = MibScalar
dcBoostChargeStatus = _DcBoostChargeStatus_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 5, 5, 2),
    _DcBoostChargeStatus_Type()
)
dcBoostChargeStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcBoostChargeStatus.setStatus("current")


class _DcBoostChargeType_Type(Integer32):
    """Custom type dcBoostChargeType based on Integer32"""
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
        *(("none", 1),
          ("currentBased", 2),
          ("timeBased", 3),
          ("energyBased", 4))
    )


_DcBoostChargeType_Type.__name__ = "Integer32"
_DcBoostChargeType_Object = MibScalar
dcBoostChargeType = _DcBoostChargeType_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 5, 5, 3),
    _DcBoostChargeType_Type()
)
dcBoostChargeType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dcBoostChargeType.setStatus("current")
_DcBoostChargeParameter_ObjectIdentity = ObjectIdentity
dcBoostChargeParameter = _DcBoostChargeParameter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 5, 5, 4)
)
_DcBoostChargeVoltage_Type = Integer32
_DcBoostChargeVoltage_Object = MibScalar
dcBoostChargeVoltage = _DcBoostChargeVoltage_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 5, 5, 4, 1),
    _DcBoostChargeVoltage_Type()
)
dcBoostChargeVoltage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dcBoostChargeVoltage.setStatus("current")
if mibBuilder.loadTexts:
    dcBoostChargeVoltage.setUnits("10 mV")
_DcBoostChargeMaxDuration_Type = Gauge32
_DcBoostChargeMaxDuration_Object = MibScalar
dcBoostChargeMaxDuration = _DcBoostChargeMaxDuration_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 5, 5, 4, 2),
    _DcBoostChargeMaxDuration_Type()
)
dcBoostChargeMaxDuration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dcBoostChargeMaxDuration.setStatus("current")
if mibBuilder.loadTexts:
    dcBoostChargeMaxDuration.setUnits("hours")


class _DcBoostChargeUseBattRoomFanEnabled_Type(Integer32):
    """Custom type dcBoostChargeUseBattRoomFanEnabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_DcBoostChargeUseBattRoomFanEnabled_Type.__name__ = "Integer32"
_DcBoostChargeUseBattRoomFanEnabled_Object = MibScalar
dcBoostChargeUseBattRoomFanEnabled = _DcBoostChargeUseBattRoomFanEnabled_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 5, 5, 4, 3),
    _DcBoostChargeUseBattRoomFanEnabled_Type()
)
dcBoostChargeUseBattRoomFanEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dcBoostChargeUseBattRoomFanEnabled.setStatus("current")
_DcBoostChargeTimeLag_Type = Gauge32
_DcBoostChargeTimeLag_Object = MibScalar
dcBoostChargeTimeLag = _DcBoostChargeTimeLag_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 5, 5, 4, 4),
    _DcBoostChargeTimeLag_Type()
)
dcBoostChargeTimeLag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dcBoostChargeTimeLag.setStatus("current")
if mibBuilder.loadTexts:
    dcBoostChargeTimeLag.setUnits("minutes")
_DcBoostChargeIstart_Type = Integer32
_DcBoostChargeIstart_Object = MibScalar
dcBoostChargeIstart = _DcBoostChargeIstart_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 5, 5, 4, 5),
    _DcBoostChargeIstart_Type()
)
dcBoostChargeIstart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dcBoostChargeIstart.setStatus("current")
if mibBuilder.loadTexts:
    dcBoostChargeIstart.setUnits("100 mA")
_DcBoostChargeIstop_Type = Integer32
_DcBoostChargeIstop_Object = MibScalar
dcBoostChargeIstop = _DcBoostChargeIstop_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 5, 5, 4, 6),
    _DcBoostChargeIstop_Type()
)
dcBoostChargeIstop.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dcBoostChargeIstop.setStatus("current")
if mibBuilder.loadTexts:
    dcBoostChargeIstop.setUnits("100 mA")
_DcBoostChargeInhibitTime_Type = Gauge32
_DcBoostChargeInhibitTime_Object = MibScalar
dcBoostChargeInhibitTime = _DcBoostChargeInhibitTime_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 5, 5, 4, 7),
    _DcBoostChargeInhibitTime_Type()
)
dcBoostChargeInhibitTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dcBoostChargeInhibitTime.setStatus("current")
if mibBuilder.loadTexts:
    dcBoostChargeInhibitTime.setUnits("hours")
_DcBoostChargeSoCBelow_Type = Gauge32
_DcBoostChargeSoCBelow_Object = MibScalar
dcBoostChargeSoCBelow = _DcBoostChargeSoCBelow_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 5, 5, 4, 8),
    _DcBoostChargeSoCBelow_Type()
)
dcBoostChargeSoCBelow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dcBoostChargeSoCBelow.setStatus("current")
if mibBuilder.loadTexts:
    dcBoostChargeSoCBelow.setUnits("%")
_DcSystemVoltageSupervision_ObjectIdentity = ObjectIdentity
dcSystemVoltageSupervision = _DcSystemVoltageSupervision_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 5, 6)
)
_DcUaMax_Type = Integer32
_DcUaMax_Object = MibScalar
dcUaMax = _DcUaMax_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 5, 6, 1),
    _DcUaMax_Type()
)
dcUaMax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dcUaMax.setStatus("current")
if mibBuilder.loadTexts:
    dcUaMax.setUnits("10 mV")
_DcUaMin_Type = Integer32
_DcUaMin_Object = MibScalar
dcUaMin = _DcUaMin_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 5, 6, 2),
    _DcUaMin_Type()
)
dcUaMin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dcUaMin.setStatus("current")
if mibBuilder.loadTexts:
    dcUaMin.setUnits("10 mV")
_DcUsMax_Type = Integer32
_DcUsMax_Object = MibScalar
dcUsMax = _DcUsMax_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 5, 6, 3),
    _DcUsMax_Type()
)
dcUsMax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dcUsMax.setStatus("current")
if mibBuilder.loadTexts:
    dcUsMax.setUnits("10 mV")
_DcUsMin_Type = Integer32
_DcUsMin_Object = MibScalar
dcUsMin = _DcUsMin_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 5, 6, 4),
    _DcUsMin_Type()
)
dcUsMin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dcUsMin.setStatus("current")
if mibBuilder.loadTexts:
    dcUsMin.setUnits("10 mV")
_DcBoD_Type = Integer32
_DcBoD_Object = MibScalar
dcBoD = _DcBoD_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 5, 6, 5),
    _DcBoD_Type()
)
dcBoD.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dcBoD.setStatus("current")
if mibBuilder.loadTexts:
    dcBoD.setUnits("10 mV")
_DcHysteresis_Type = Integer32
_DcHysteresis_Object = MibScalar
dcHysteresis = _DcHysteresis_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 5, 6, 6),
    _DcHysteresis_Type()
)
dcHysteresis.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dcHysteresis.setStatus("current")
if mibBuilder.loadTexts:
    dcHysteresis.setUnits("10 mV")


class _DcSuppressUaLowEnabled_Type(Integer32):
    """Custom type dcSuppressUaLowEnabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_DcSuppressUaLowEnabled_Type.__name__ = "Integer32"
_DcSuppressUaLowEnabled_Object = MibScalar
dcSuppressUaLowEnabled = _DcSuppressUaLowEnabled_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 5, 6, 7),
    _DcSuppressUaLowEnabled_Type()
)
dcSuppressUaLowEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dcSuppressUaLowEnabled.setStatus("current")


class _DcSuppressUsLowEnabled_Type(Integer32):
    """Custom type dcSuppressUsLowEnabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_DcSuppressUsLowEnabled_Type.__name__ = "Integer32"
_DcSuppressUsLowEnabled_Object = MibScalar
dcSuppressUsLowEnabled = _DcSuppressUsLowEnabled_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 5, 6, 8),
    _DcSuppressUsLowEnabled_Type()
)
dcSuppressUsLowEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dcSuppressUsLowEnabled.setStatus("current")


class _DcEnableUsTempComp_Type(Integer32):
    """Custom type dcEnableUsTempComp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_DcEnableUsTempComp_Type.__name__ = "Integer32"
_DcEnableUsTempComp_Object = MibScalar
dcEnableUsTempComp = _DcEnableUsTempComp_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 5, 6, 9),
    _DcEnableUsTempComp_Type()
)
dcEnableUsTempComp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dcEnableUsTempComp.setStatus("current")
_DcEvtCtrlCharge_ObjectIdentity = ObjectIdentity
dcEvtCtrlCharge = _DcEvtCtrlCharge_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 5, 7)
)


class _DcEvtCtrlChargeStatus_Type(Integer32):
    """Custom type dcEvtCtrlChargeStatus based on Integer32"""
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
        *(("inactive", 1),
          ("voltageControlled", 2),
          ("noBatteryCharge", 3),
          ("currentLimitation", 4),
          ("suppressed", 5))
    )


_DcEvtCtrlChargeStatus_Type.__name__ = "Integer32"
_DcEvtCtrlChargeStatus_Object = MibScalar
dcEvtCtrlChargeStatus = _DcEvtCtrlChargeStatus_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 5, 7, 1),
    _DcEvtCtrlChargeStatus_Type()
)
dcEvtCtrlChargeStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcEvtCtrlChargeStatus.setStatus("obsolete")


class _DcEvtCtrlChargeType_Type(Integer32):
    """Custom type dcEvtCtrlChargeType based on Integer32"""
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
        *(("none", 1),
          ("voltageControlled", 2),
          ("noBatteryCharge", 3),
          ("currentLimitation", 4))
    )


_DcEvtCtrlChargeType_Type.__name__ = "Integer32"
_DcEvtCtrlChargeType_Object = MibScalar
dcEvtCtrlChargeType = _DcEvtCtrlChargeType_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 5, 7, 2),
    _DcEvtCtrlChargeType_Type()
)
dcEvtCtrlChargeType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcEvtCtrlChargeType.setStatus("obsolete")
_DcEvtCtrlChargeParameter_ObjectIdentity = ObjectIdentity
dcEvtCtrlChargeParameter = _DcEvtCtrlChargeParameter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 5, 7, 3)
)
_DcEvtCtrlChargeVoltage_Type = Integer32
_DcEvtCtrlChargeVoltage_Object = MibScalar
dcEvtCtrlChargeVoltage = _DcEvtCtrlChargeVoltage_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 5, 7, 3, 1),
    _DcEvtCtrlChargeVoltage_Type()
)
dcEvtCtrlChargeVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcEvtCtrlChargeVoltage.setStatus("obsolete")
if mibBuilder.loadTexts:
    dcEvtCtrlChargeVoltage.setUnits("10 mV")


class _DcEvtCtrlChargeTempCompEnabled_Type(Integer32):
    """Custom type dcEvtCtrlChargeTempCompEnabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_DcEvtCtrlChargeTempCompEnabled_Type.__name__ = "Integer32"
_DcEvtCtrlChargeTempCompEnabled_Object = MibScalar
dcEvtCtrlChargeTempCompEnabled = _DcEvtCtrlChargeTempCompEnabled_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 5, 7, 3, 2),
    _DcEvtCtrlChargeTempCompEnabled_Type()
)
dcEvtCtrlChargeTempCompEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcEvtCtrlChargeTempCompEnabled.setStatus("obsolete")
_DcEvtCtrlChargeMaxIBatt_Type = Integer32
_DcEvtCtrlChargeMaxIBatt_Object = MibScalar
dcEvtCtrlChargeMaxIBatt = _DcEvtCtrlChargeMaxIBatt_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 5, 7, 3, 3),
    _DcEvtCtrlChargeMaxIBatt_Type()
)
dcEvtCtrlChargeMaxIBatt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcEvtCtrlChargeMaxIBatt.setStatus("obsolete")
if mibBuilder.loadTexts:
    dcEvtCtrlChargeMaxIBatt.setUnits("100 mA")
_DcEventControlledChargeTable_Object = MibTable
dcEventControlledChargeTable = _DcEventControlledChargeTable_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 5, 7, 4)
)
if mibBuilder.loadTexts:
    dcEventControlledChargeTable.setStatus("current")
_DcEventControlledChargeTableEntry_Object = MibTableRow
dcEventControlledChargeTableEntry = _DcEventControlledChargeTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 5, 7, 4, 1)
)
dcEventControlledChargeTableEntry.setIndexNames(
    (0, "ORION-BASE-MIB", "dcEventControlledChargeTableIndex"),
)
if mibBuilder.loadTexts:
    dcEventControlledChargeTableEntry.setStatus("current")


class _DcEventControlledChargeTableIndex_Type(Integer32):
    """Custom type dcEventControlledChargeTableIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10000),
    )


_DcEventControlledChargeTableIndex_Type.__name__ = "Integer32"
_DcEventControlledChargeTableIndex_Object = MibTableColumn
dcEventControlledChargeTableIndex = _DcEventControlledChargeTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 5, 7, 4, 1, 1),
    _DcEventControlledChargeTableIndex_Type()
)
dcEventControlledChargeTableIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dcEventControlledChargeTableIndex.setStatus("current")
_DcEventControlledChargeTablePriority_Type = Unsigned32
_DcEventControlledChargeTablePriority_Object = MibTableColumn
dcEventControlledChargeTablePriority = _DcEventControlledChargeTablePriority_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 5, 7, 4, 1, 2),
    _DcEventControlledChargeTablePriority_Type()
)
dcEventControlledChargeTablePriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcEventControlledChargeTablePriority.setStatus("current")


class _DcEventControlledChargeTableName_Type(DisplayString):
    """Custom type dcEventControlledChargeTableName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(32, 32),
    )
    fixed_length = 32


_DcEventControlledChargeTableName_Type.__name__ = "DisplayString"
_DcEventControlledChargeTableName_Object = MibTableColumn
dcEventControlledChargeTableName = _DcEventControlledChargeTableName_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 5, 7, 4, 1, 3),
    _DcEventControlledChargeTableName_Type()
)
dcEventControlledChargeTableName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcEventControlledChargeTableName.setStatus("current")


class _DcEventControlledChargeTableActivationInput_Type(DisplayString):
    """Custom type dcEventControlledChargeTableActivationInput based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(32, 32),
    )
    fixed_length = 32


_DcEventControlledChargeTableActivationInput_Type.__name__ = "DisplayString"
_DcEventControlledChargeTableActivationInput_Object = MibTableColumn
dcEventControlledChargeTableActivationInput = _DcEventControlledChargeTableActivationInput_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 5, 7, 4, 1, 4),
    _DcEventControlledChargeTableActivationInput_Type()
)
dcEventControlledChargeTableActivationInput.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcEventControlledChargeTableActivationInput.setStatus("current")


class _DcEventControlledChargeTableStatus_Type(Integer32):
    """Custom type dcEventControlledChargeTableStatus based on Integer32"""
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
        *(("inactive", 1),
          ("voltageControlled", 2),
          ("noBatteryCharge", 3),
          ("currentLimitation", 4),
          ("suppressed", 5))
    )


_DcEventControlledChargeTableStatus_Type.__name__ = "Integer32"
_DcEventControlledChargeTableStatus_Object = MibTableColumn
dcEventControlledChargeTableStatus = _DcEventControlledChargeTableStatus_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 5, 7, 4, 1, 5),
    _DcEventControlledChargeTableStatus_Type()
)
dcEventControlledChargeTableStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcEventControlledChargeTableStatus.setStatus("current")


class _DcEventControlledChargeTableType_Type(Integer32):
    """Custom type dcEventControlledChargeTableType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("voltageControlled", 1),
          ("noBatteryCharge", 2),
          ("currentLimitation", 3))
    )


_DcEventControlledChargeTableType_Type.__name__ = "Integer32"
_DcEventControlledChargeTableType_Object = MibTableColumn
dcEventControlledChargeTableType = _DcEventControlledChargeTableType_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 5, 7, 4, 1, 6),
    _DcEventControlledChargeTableType_Type()
)
dcEventControlledChargeTableType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dcEventControlledChargeTableType.setStatus("current")
_DcEventControlledChargeTableVoltage_Type = Integer32
_DcEventControlledChargeTableVoltage_Object = MibTableColumn
dcEventControlledChargeTableVoltage = _DcEventControlledChargeTableVoltage_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 5, 7, 4, 1, 7),
    _DcEventControlledChargeTableVoltage_Type()
)
dcEventControlledChargeTableVoltage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dcEventControlledChargeTableVoltage.setStatus("current")
if mibBuilder.loadTexts:
    dcEventControlledChargeTableVoltage.setUnits("10mV")
_DcEventControlledChargeTableMaxIBatt_Type = Integer32
_DcEventControlledChargeTableMaxIBatt_Object = MibTableColumn
dcEventControlledChargeTableMaxIBatt = _DcEventControlledChargeTableMaxIBatt_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 5, 7, 4, 1, 8),
    _DcEventControlledChargeTableMaxIBatt_Type()
)
dcEventControlledChargeTableMaxIBatt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dcEventControlledChargeTableMaxIBatt.setStatus("current")
if mibBuilder.loadTexts:
    dcEventControlledChargeTableMaxIBatt.setUnits("100mA")


class _DcEventControlledChargeTableTempCompEnabled_Type(Integer32):
    """Custom type dcEventControlledChargeTableTempCompEnabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_DcEventControlledChargeTableTempCompEnabled_Type.__name__ = "Integer32"
_DcEventControlledChargeTableTempCompEnabled_Object = MibTableColumn
dcEventControlledChargeTableTempCompEnabled = _DcEventControlledChargeTableTempCompEnabled_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 5, 7, 4, 1, 9),
    _DcEventControlledChargeTableTempCompEnabled_Type()
)
dcEventControlledChargeTableTempCompEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dcEventControlledChargeTableTempCompEnabled.setStatus("current")
_DcTempComp_ObjectIdentity = ObjectIdentity
dcTempComp = _DcTempComp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 5, 8)
)


class _DcTempCompType_Type(Integer32):
    """Custom type dcTempCompType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("linear", 2),
          ("multi-stage", 3))
    )


_DcTempCompType_Type.__name__ = "Integer32"
_DcTempCompType_Object = MibScalar
dcTempCompType = _DcTempCompType_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 5, 8, 1),
    _DcTempCompType_Type()
)
dcTempCompType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dcTempCompType.setStatus("current")
_DcSlope_Type = Integer32
_DcSlope_Object = MibScalar
dcSlope = _DcSlope_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 5, 8, 2),
    _DcSlope_Type()
)
dcSlope.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dcSlope.setStatus("current")
if mibBuilder.loadTexts:
    dcSlope.setUnits("-1 mV/degree")
_DcStartTemp_Type = Integer32
_DcStartTemp_Object = MibScalar
dcStartTemp = _DcStartTemp_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 5, 8, 3),
    _DcStartTemp_Type()
)
dcStartTemp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dcStartTemp.setStatus("current")
if mibBuilder.loadTexts:
    dcStartTemp.setUnits("0.1 degree")
_DcStopTemp_Type = Integer32
_DcStopTemp_Object = MibScalar
dcStopTemp = _DcStopTemp_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 5, 8, 4),
    _DcStopTemp_Type()
)
dcStopTemp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dcStopTemp.setStatus("current")
if mibBuilder.loadTexts:
    dcStopTemp.setUnits("0.1 degree")
_DcMaxVoltage_Type = Integer32
_DcMaxVoltage_Object = MibScalar
dcMaxVoltage = _DcMaxVoltage_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 5, 8, 5),
    _DcMaxVoltage_Type()
)
dcMaxVoltage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dcMaxVoltage.setStatus("current")
if mibBuilder.loadTexts:
    dcMaxVoltage.setUnits("10 mV")
_DcLowStopVoltage_Type = Integer32
_DcLowStopVoltage_Object = MibScalar
dcLowStopVoltage = _DcLowStopVoltage_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 5, 8, 6),
    _DcLowStopVoltage_Type()
)
dcLowStopVoltage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dcLowStopVoltage.setStatus("current")
if mibBuilder.loadTexts:
    dcLowStopVoltage.setUnits("10 mV")
_DcLowStartTemp_Type = Integer32
_DcLowStartTemp_Object = MibScalar
dcLowStartTemp = _DcLowStartTemp_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 5, 8, 7),
    _DcLowStartTemp_Type()
)
dcLowStartTemp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dcLowStartTemp.setStatus("current")
if mibBuilder.loadTexts:
    dcLowStartTemp.setUnits("0.1 degree")
_DcLowTempSlope_Type = Integer32
_DcLowTempSlope_Object = MibScalar
dcLowTempSlope = _DcLowTempSlope_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 5, 8, 8),
    _DcLowTempSlope_Type()
)
dcLowTempSlope.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dcLowTempSlope.setStatus("current")
if mibBuilder.loadTexts:
    dcLowTempSlope.setUnits("-1 mV/degree")
_DcHighStartTemp_Type = Integer32
_DcHighStartTemp_Object = MibScalar
dcHighStartTemp = _DcHighStartTemp_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 5, 8, 9),
    _DcHighStartTemp_Type()
)
dcHighStartTemp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dcHighStartTemp.setStatus("current")
if mibBuilder.loadTexts:
    dcHighStartTemp.setUnits("0.1 degree")
_DcHighTempSlope_Type = Integer32
_DcHighTempSlope_Object = MibScalar
dcHighTempSlope = _DcHighTempSlope_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 5, 8, 10),
    _DcHighTempSlope_Type()
)
dcHighTempSlope.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dcHighTempSlope.setStatus("current")
if mibBuilder.loadTexts:
    dcHighTempSlope.setUnits("-1 mV/degree")
_DcHighStopVoltage_Type = Integer32
_DcHighStopVoltage_Object = MibScalar
dcHighStopVoltage = _DcHighStopVoltage_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 5, 8, 11),
    _DcHighStopVoltage_Type()
)
dcHighStopVoltage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dcHighStopVoltage.setStatus("current")
if mibBuilder.loadTexts:
    dcHighStopVoltage.setUnits("10 mV")
_DcRunawayTemp_Type = Integer32
_DcRunawayTemp_Object = MibScalar
dcRunawayTemp = _DcRunawayTemp_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 5, 8, 12),
    _DcRunawayTemp_Type()
)
dcRunawayTemp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dcRunawayTemp.setStatus("current")
if mibBuilder.loadTexts:
    dcRunawayTemp.setUnits("0.1 degree")
_DcRunawayVoltage_Type = Integer32
_DcRunawayVoltage_Object = MibScalar
dcRunawayVoltage = _DcRunawayVoltage_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 5, 8, 13),
    _DcRunawayVoltage_Type()
)
dcRunawayVoltage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dcRunawayVoltage.setStatus("current")
if mibBuilder.loadTexts:
    dcRunawayVoltage.setUnits("10 mV")
_DcTempSupervision_ObjectIdentity = ObjectIdentity
dcTempSupervision = _DcTempSupervision_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 5, 9)
)
_DcHighTemp_Type = Integer32
_DcHighTemp_Object = MibScalar
dcHighTemp = _DcHighTemp_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 5, 9, 1),
    _DcHighTemp_Type()
)
dcHighTemp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dcHighTemp.setStatus("current")
if mibBuilder.loadTexts:
    dcHighTemp.setUnits("0.1 degree")
_DcHighTempHyst_Type = Integer32
_DcHighTempHyst_Object = MibScalar
dcHighTempHyst = _DcHighTempHyst_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 5, 9, 2),
    _DcHighTempHyst_Type()
)
dcHighTempHyst.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dcHighTempHyst.setStatus("current")
if mibBuilder.loadTexts:
    dcHighTempHyst.setUnits("0.1 degree")
_DcBatteryType_ObjectIdentity = ObjectIdentity
dcBatteryType = _DcBatteryType_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 5, 10)
)


class _DcBatteryTypeSelect_Type(Integer32):
    """Custom type dcBatteryTypeSelect based on Integer32"""
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
        *(("no", 1),
          ("lead-acid", 2),
          ("lithium", 3),
          ("nickel-cadmium", 4),
          ("hybrid-lead-acid", 5))
    )


_DcBatteryTypeSelect_Type.__name__ = "Integer32"
_DcBatteryTypeSelect_Object = MibScalar
dcBatteryTypeSelect = _DcBatteryTypeSelect_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 5, 10, 1),
    _DcBatteryTypeSelect_Type()
)
dcBatteryTypeSelect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcBatteryTypeSelect.setStatus("current")
_DcInputOutput_ObjectIdentity = ObjectIdentity
dcInputOutput = _DcInputOutput_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 6)
)
_DcControlEventTable_Object = MibTable
dcControlEventTable = _DcControlEventTable_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 6, 1)
)
if mibBuilder.loadTexts:
    dcControlEventTable.setStatus("current")
_DcControlEventEntry_Object = MibTableRow
dcControlEventEntry = _DcControlEventEntry_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 6, 1, 1)
)
dcControlEventEntry.setIndexNames(
    (0, "ORION-BASE-MIB", "dcControlEventIndex"),
)
if mibBuilder.loadTexts:
    dcControlEventEntry.setStatus("current")


class _DcControlEventIndex_Type(Integer32):
    """Custom type dcControlEventIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_DcControlEventIndex_Type.__name__ = "Integer32"
_DcControlEventIndex_Object = MibTableColumn
dcControlEventIndex = _DcControlEventIndex_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 6, 1, 1, 1),
    _DcControlEventIndex_Type()
)
dcControlEventIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dcControlEventIndex.setStatus("current")


class _DcControlEventName_Type(DisplayString):
    """Custom type dcControlEventName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 35),
    )


_DcControlEventName_Type.__name__ = "DisplayString"
_DcControlEventName_Object = MibTableColumn
dcControlEventName = _DcControlEventName_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 6, 1, 1, 2),
    _DcControlEventName_Type()
)
dcControlEventName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcControlEventName.setStatus("current")
_DcControlEventIdentifier_Type = Gauge32
_DcControlEventIdentifier_Object = MibTableColumn
dcControlEventIdentifier = _DcControlEventIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 6, 1, 1, 3),
    _DcControlEventIdentifier_Type()
)
dcControlEventIdentifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcControlEventIdentifier.setStatus("current")


class _DcControlEventValue_Type(Integer32):
    """Custom type dcControlEventValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 1),
          ("true", 2))
    )


_DcControlEventValue_Type.__name__ = "Integer32"
_DcControlEventValue_Object = MibTableColumn
dcControlEventValue = _DcControlEventValue_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 6, 1, 1, 4),
    _DcControlEventValue_Type()
)
dcControlEventValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dcControlEventValue.setStatus("current")
_DcMisc_ObjectIdentity = ObjectIdentity
dcMisc = _DcMisc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 7)
)
_DcTrapDestinationTable_Object = MibTable
dcTrapDestinationTable = _DcTrapDestinationTable_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 7, 1)
)
if mibBuilder.loadTexts:
    dcTrapDestinationTable.setStatus("obsolete")
_DcTrapDestinationEntry_Object = MibTableRow
dcTrapDestinationEntry = _DcTrapDestinationEntry_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 7, 1, 1)
)
dcTrapDestinationEntry.setIndexNames(
    (0, "ORION-BASE-MIB", "dcTrapDestinationIndex"),
)
if mibBuilder.loadTexts:
    dcTrapDestinationEntry.setStatus("obsolete")


class _DcTrapDestinationIndex_Type(Integer32):
    """Custom type dcTrapDestinationIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_DcTrapDestinationIndex_Type.__name__ = "Integer32"
_DcTrapDestinationIndex_Object = MibTableColumn
dcTrapDestinationIndex = _DcTrapDestinationIndex_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 7, 1, 1, 1),
    _DcTrapDestinationIndex_Type()
)
dcTrapDestinationIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dcTrapDestinationIndex.setStatus("obsolete")
_DcTrapDestinationIp_Type = IpAddress
_DcTrapDestinationIp_Object = MibTableColumn
dcTrapDestinationIp = _DcTrapDestinationIp_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 7, 1, 1, 2),
    _DcTrapDestinationIp_Type()
)
dcTrapDestinationIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dcTrapDestinationIp.setStatus("obsolete")
_DcTrapDestinationPort_Type = Gauge32
_DcTrapDestinationPort_Object = MibTableColumn
dcTrapDestinationPort = _DcTrapDestinationPort_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 7, 1, 1, 3),
    _DcTrapDestinationPort_Type()
)
dcTrapDestinationPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dcTrapDestinationPort.setStatus("obsolete")


class _DcTrapDestinationUser_Type(DisplayString):
    """Custom type dcTrapDestinationUser based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_DcTrapDestinationUser_Type.__name__ = "DisplayString"
_DcTrapDestinationUser_Object = MibTableColumn
dcTrapDestinationUser = _DcTrapDestinationUser_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 7, 1, 1, 4),
    _DcTrapDestinationUser_Type()
)
dcTrapDestinationUser.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dcTrapDestinationUser.setStatus("obsolete")


class _DcFileProcessingStatus_Type(Integer32):
    """Custom type dcFileProcessingStatus based on Integer32"""
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
        *(("idle", 1),
          ("inProgress", 2),
          ("successful", 3),
          ("error", 4),
          ("unknown", 5))
    )


_DcFileProcessingStatus_Type.__name__ = "Integer32"
_DcFileProcessingStatus_Object = MibScalar
dcFileProcessingStatus = _DcFileProcessingStatus_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 7, 2),
    _DcFileProcessingStatus_Type()
)
dcFileProcessingStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcFileProcessingStatus.setStatus("current")


class _DcResendActiveAlarmTraps_Type(Integer32):
    """Custom type dcResendActiveAlarmTraps based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("resend", 1)
    )


_DcResendActiveAlarmTraps_Type.__name__ = "Integer32"
_DcResendActiveAlarmTraps_Object = MibScalar
dcResendActiveAlarmTraps = _DcResendActiveAlarmTraps_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 7, 4),
    _DcResendActiveAlarmTraps_Type()
)
dcResendActiveAlarmTraps.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dcResendActiveAlarmTraps.setStatus("current")


class _DcRebootController_Type(Integer32):
    """Custom type dcRebootController based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("reboot", 1)
    )


_DcRebootController_Type.__name__ = "Integer32"
_DcRebootController_Object = MibScalar
dcRebootController = _DcRebootController_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 7, 5),
    _DcRebootController_Type()
)
dcRebootController.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dcRebootController.setStatus("current")
_DcTrapDestinationv2Table_Object = MibTable
dcTrapDestinationv2Table = _DcTrapDestinationv2Table_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 7, 6)
)
if mibBuilder.loadTexts:
    dcTrapDestinationv2Table.setStatus("current")
_DcTrapDestinationv2Entry_Object = MibTableRow
dcTrapDestinationv2Entry = _DcTrapDestinationv2Entry_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 7, 6, 1)
)
dcTrapDestinationv2Entry.setIndexNames(
    (0, "ORION-BASE-MIB", "dcTrapDestinationv2Index"),
)
if mibBuilder.loadTexts:
    dcTrapDestinationv2Entry.setStatus("current")


class _DcTrapDestinationv2Index_Type(Integer32):
    """Custom type dcTrapDestinationv2Index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_DcTrapDestinationv2Index_Type.__name__ = "Integer32"
_DcTrapDestinationv2Index_Object = MibTableColumn
dcTrapDestinationv2Index = _DcTrapDestinationv2Index_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 7, 6, 1, 1),
    _DcTrapDestinationv2Index_Type()
)
dcTrapDestinationv2Index.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dcTrapDestinationv2Index.setStatus("current")
_DcTrapDestinationv2_Type = DisplayString
_DcTrapDestinationv2_Object = MibTableColumn
dcTrapDestinationv2 = _DcTrapDestinationv2_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 7, 6, 1, 2),
    _DcTrapDestinationv2_Type()
)
dcTrapDestinationv2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dcTrapDestinationv2.setStatus("current")
_DcTrapDestinationv2Port_Type = Gauge32
_DcTrapDestinationv2Port_Object = MibTableColumn
dcTrapDestinationv2Port = _DcTrapDestinationv2Port_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 7, 6, 1, 3),
    _DcTrapDestinationv2Port_Type()
)
dcTrapDestinationv2Port.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dcTrapDestinationv2Port.setStatus("current")


class _DcTrapDestinationv2User_Type(DisplayString):
    """Custom type dcTrapDestinationv2User based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_DcTrapDestinationv2User_Type.__name__ = "DisplayString"
_DcTrapDestinationv2User_Object = MibTableColumn
dcTrapDestinationv2User = _DcTrapDestinationv2User_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 7, 6, 1, 4),
    _DcTrapDestinationv2User_Type()
)
dcTrapDestinationv2User.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dcTrapDestinationv2User.setStatus("current")
_DcConfig_ObjectIdentity = ObjectIdentity
dcConfig = _DcConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 8)
)
_DcDefaultLogEventTable_Object = MibTable
dcDefaultLogEventTable = _DcDefaultLogEventTable_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 8, 1)
)
if mibBuilder.loadTexts:
    dcDefaultLogEventTable.setStatus("current")
_DcDefaultLogEventEntry_Object = MibTableRow
dcDefaultLogEventEntry = _DcDefaultLogEventEntry_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 8, 1, 1)
)
dcDefaultLogEventEntry.setIndexNames(
    (0, "ORION-BASE-MIB", "dcDefaultLogEventIndex"),
)
if mibBuilder.loadTexts:
    dcDefaultLogEventEntry.setStatus("current")


class _DcDefaultLogEventIndex_Type(Integer32):
    """Custom type dcDefaultLogEventIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_DcDefaultLogEventIndex_Type.__name__ = "Integer32"
_DcDefaultLogEventIndex_Object = MibTableColumn
dcDefaultLogEventIndex = _DcDefaultLogEventIndex_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 8, 1, 1, 1),
    _DcDefaultLogEventIndex_Type()
)
dcDefaultLogEventIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dcDefaultLogEventIndex.setStatus("current")


class _DcDefaultLogEventName_Type(DisplayString):
    """Custom type dcDefaultLogEventName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 35),
    )


_DcDefaultLogEventName_Type.__name__ = "DisplayString"
_DcDefaultLogEventName_Object = MibTableColumn
dcDefaultLogEventName = _DcDefaultLogEventName_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 8, 1, 1, 2),
    _DcDefaultLogEventName_Type()
)
dcDefaultLogEventName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcDefaultLogEventName.setStatus("current")


class _DcDefaultLogEventLogged_Type(Integer32):
    """Custom type dcDefaultLogEventLogged based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_DcDefaultLogEventLogged_Type.__name__ = "Integer32"
_DcDefaultLogEventLogged_Object = MibTableColumn
dcDefaultLogEventLogged = _DcDefaultLogEventLogged_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 8, 1, 1, 3),
    _DcDefaultLogEventLogged_Type()
)
dcDefaultLogEventLogged.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dcDefaultLogEventLogged.setStatus("current")
_DcEventProcessingEventTable_Object = MibTable
dcEventProcessingEventTable = _DcEventProcessingEventTable_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 8, 2)
)
if mibBuilder.loadTexts:
    dcEventProcessingEventTable.setStatus("current")
_DcEventProcessingEventEntry_Object = MibTableRow
dcEventProcessingEventEntry = _DcEventProcessingEventEntry_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 8, 2, 1)
)
dcEventProcessingEventEntry.setIndexNames(
    (0, "ORION-BASE-MIB", "dcEventProcessingEventIndex"),
)
if mibBuilder.loadTexts:
    dcEventProcessingEventEntry.setStatus("current")


class _DcEventProcessingEventIndex_Type(Integer32):
    """Custom type dcEventProcessingEventIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_DcEventProcessingEventIndex_Type.__name__ = "Integer32"
_DcEventProcessingEventIndex_Object = MibTableColumn
dcEventProcessingEventIndex = _DcEventProcessingEventIndex_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 8, 2, 1, 1),
    _DcEventProcessingEventIndex_Type()
)
dcEventProcessingEventIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dcEventProcessingEventIndex.setStatus("current")


class _DcEventProcessingEventName_Type(DisplayString):
    """Custom type dcEventProcessingEventName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 35),
    )


_DcEventProcessingEventName_Type.__name__ = "DisplayString"
_DcEventProcessingEventName_Object = MibTableColumn
dcEventProcessingEventName = _DcEventProcessingEventName_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 8, 2, 1, 2),
    _DcEventProcessingEventName_Type()
)
dcEventProcessingEventName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcEventProcessingEventName.setStatus("current")


class _DcEventProcessingEventAssigned_Type(Integer32):
    """Custom type dcEventProcessingEventAssigned based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_DcEventProcessingEventAssigned_Type.__name__ = "Integer32"
_DcEventProcessingEventAssigned_Object = MibTableColumn
dcEventProcessingEventAssigned = _DcEventProcessingEventAssigned_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 8, 2, 1, 3),
    _DcEventProcessingEventAssigned_Type()
)
dcEventProcessingEventAssigned.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dcEventProcessingEventAssigned.setStatus("current")


class _DcEventProcessingEventType_Type(Integer32):
    """Custom type dcEventProcessingEventType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 1),
          ("eventOR", 2))
    )


_DcEventProcessingEventType_Type.__name__ = "Integer32"
_DcEventProcessingEventType_Object = MibTableColumn
dcEventProcessingEventType = _DcEventProcessingEventType_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 8, 2, 1, 4),
    _DcEventProcessingEventType_Type()
)
dcEventProcessingEventType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcEventProcessingEventType.setStatus("current")
_DcEventProcessingEventSelected_Type = Gauge32
_DcEventProcessingEventSelected_Object = MibScalar
dcEventProcessingEventSelected = _DcEventProcessingEventSelected_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 8, 3),
    _DcEventProcessingEventSelected_Type()
)
dcEventProcessingEventSelected.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dcEventProcessingEventSelected.setStatus("current")
_DcLvdTable_Object = MibTable
dcLvdTable = _DcLvdTable_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 8, 4)
)
if mibBuilder.loadTexts:
    dcLvdTable.setStatus("current")
_DcLvdEntry_Object = MibTableRow
dcLvdEntry = _DcLvdEntry_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 8, 4, 1)
)
dcLvdEntry.setIndexNames(
    (0, "ORION-BASE-MIB", "dcLvdIndex"),
)
if mibBuilder.loadTexts:
    dcLvdEntry.setStatus("current")


class _DcLvdIndex_Type(Integer32):
    """Custom type dcLvdIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 96),
    )


_DcLvdIndex_Type.__name__ = "Integer32"
_DcLvdIndex_Object = MibTableColumn
dcLvdIndex = _DcLvdIndex_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 8, 4, 1, 1),
    _DcLvdIndex_Type()
)
dcLvdIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dcLvdIndex.setStatus("current")


class _DcLvdName_Type(DisplayString):
    """Custom type dcLvdName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_DcLvdName_Type.__name__ = "DisplayString"
_DcLvdName_Object = MibTableColumn
dcLvdName = _DcLvdName_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 8, 4, 1, 2),
    _DcLvdName_Type()
)
dcLvdName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcLvdName.setStatus("current")


class _DcLvdDisconnectDelay_Type(DisplayString):
    """Custom type dcLvdDisconnectDelay based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )
    fixed_length = 8


_DcLvdDisconnectDelay_Type.__name__ = "DisplayString"
_DcLvdDisconnectDelay_Object = MibTableColumn
dcLvdDisconnectDelay = _DcLvdDisconnectDelay_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 8, 4, 1, 3),
    _DcLvdDisconnectDelay_Type()
)
dcLvdDisconnectDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dcLvdDisconnectDelay.setStatus("current")


class _DcLvdType_Type(Integer32):
    """Custom type dcLvdType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("eventControlled", 1),
          ("utControlled", 2))
    )


_DcLvdType_Type.__name__ = "Integer32"
_DcLvdType_Object = MibTableColumn
dcLvdType = _DcLvdType_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 8, 4, 1, 4),
    _DcLvdType_Type()
)
dcLvdType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcLvdType.setStatus("current")
_DcLvdVoltageThreshold_Type = Integer32
_DcLvdVoltageThreshold_Object = MibTableColumn
dcLvdVoltageThreshold = _DcLvdVoltageThreshold_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 8, 4, 1, 5),
    _DcLvdVoltageThreshold_Type()
)
dcLvdVoltageThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dcLvdVoltageThreshold.setStatus("current")
if mibBuilder.loadTexts:
    dcLvdVoltageThreshold.setUnits("10 mV")
_DcLvdVoltageHysteresis_Type = Integer32
_DcLvdVoltageHysteresis_Object = MibTableColumn
dcLvdVoltageHysteresis = _DcLvdVoltageHysteresis_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 8, 4, 1, 6),
    _DcLvdVoltageHysteresis_Type()
)
dcLvdVoltageHysteresis.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dcLvdVoltageHysteresis.setStatus("current")
if mibBuilder.loadTexts:
    dcLvdVoltageHysteresis.setUnits("10 mV")


class _DcLvdControlEvent_Type(DisplayString):
    """Custom type dcLvdControlEvent based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 35),
    )


_DcLvdControlEvent_Type.__name__ = "DisplayString"
_DcLvdControlEvent_Object = MibTableColumn
dcLvdControlEvent = _DcLvdControlEvent_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 8, 4, 1, 7),
    _DcLvdControlEvent_Type()
)
dcLvdControlEvent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcLvdControlEvent.setStatus("current")


class _DcLvdMonitoringEvent_Type(DisplayString):
    """Custom type dcLvdMonitoringEvent based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 35),
    )


_DcLvdMonitoringEvent_Type.__name__ = "DisplayString"
_DcLvdMonitoringEvent_Object = MibTableColumn
dcLvdMonitoringEvent = _DcLvdMonitoringEvent_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 8, 4, 1, 8),
    _DcLvdMonitoringEvent_Type()
)
dcLvdMonitoringEvent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcLvdMonitoringEvent.setStatus("current")
_DcEventDefinitionTable_Object = MibTable
dcEventDefinitionTable = _DcEventDefinitionTable_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 8, 5)
)
if mibBuilder.loadTexts:
    dcEventDefinitionTable.setStatus("current")
_DcEventDefinitionEntry_Object = MibTableRow
dcEventDefinitionEntry = _DcEventDefinitionEntry_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 8, 5, 1)
)
dcEventDefinitionEntry.setIndexNames(
    (0, "ORION-BASE-MIB", "dcEventIndex"),
)
if mibBuilder.loadTexts:
    dcEventDefinitionEntry.setStatus("current")


class _DcEventIndex_Type(Integer32):
    """Custom type dcEventIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 20),
    )


_DcEventIndex_Type.__name__ = "Integer32"
_DcEventIndex_Object = MibTableColumn
dcEventIndex = _DcEventIndex_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 8, 5, 1, 1),
    _DcEventIndex_Type()
)
dcEventIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dcEventIndex.setStatus("current")


class _DcEventName_Type(DisplayString):
    """Custom type dcEventName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 35),
    )


_DcEventName_Type.__name__ = "DisplayString"
_DcEventName_Object = MibTableColumn
dcEventName = _DcEventName_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 8, 5, 1, 2),
    _DcEventName_Type()
)
dcEventName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcEventName.setStatus("current")
_DcThreshold_Type = Integer32
_DcThreshold_Object = MibTableColumn
dcThreshold = _DcThreshold_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 8, 5, 1, 3),
    _DcThreshold_Type()
)
dcThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dcThreshold.setStatus("current")
_DcThresholdHysteresis_Type = Integer32
_DcThresholdHysteresis_Object = MibTableColumn
dcThresholdHysteresis = _DcThresholdHysteresis_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 8, 5, 1, 4),
    _DcThresholdHysteresis_Type()
)
dcThresholdHysteresis.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dcThresholdHysteresis.setStatus("current")


class _DcUnit_Type(Integer32):
    """Custom type dcUnit based on Integer32"""
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
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18)
        )
    )
    namedValues = NamedValues(
        *(("unitUnknown", 1),
          ("unitNone", 2),
          ("unit10mVdc", 3),
          ("unit10mVac", 4),
          ("unit100mA", 5),
          ("unit100mAh", 6),
          ("unit100mDegree", 7),
          ("unit100mDegreeCoefficient", 8),
          ("unitWatt", 9),
          ("unitWattHour", 10),
          ("unitKilowattHour", 11),
          ("unitSeconds", 12),
          ("unitPercent", 13),
          ("unitHertz", 14),
          ("unitVoltAmpere", 15),
          ("unitVoltAmpereReactive", 16),
          ("unitVoltAmpereReactiveHour", 17),
          ("unitVoltAmpereHour", 18))
    )


_DcUnit_Type.__name__ = "Integer32"
_DcUnit_Object = MibTableColumn
dcUnit = _DcUnit_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 8, 5, 1, 5),
    _DcUnit_Type()
)
dcUnit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcUnit.setStatus("current")
_DcFilterTable_Object = MibTable
dcFilterTable = _DcFilterTable_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 8, 6)
)
if mibBuilder.loadTexts:
    dcFilterTable.setStatus("current")
_DcFilterEntry_Object = MibTableRow
dcFilterEntry = _DcFilterEntry_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 8, 6, 1)
)
dcFilterEntry.setIndexNames(
    (0, "ORION-BASE-MIB", "dcFilterIndex"),
)
if mibBuilder.loadTexts:
    dcFilterEntry.setStatus("current")


class _DcFilterIndex_Type(Integer32):
    """Custom type dcFilterIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 20),
    )


_DcFilterIndex_Type.__name__ = "Integer32"
_DcFilterIndex_Object = MibTableColumn
dcFilterIndex = _DcFilterIndex_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 8, 6, 1, 1),
    _DcFilterIndex_Type()
)
dcFilterIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dcFilterIndex.setStatus("current")


class _DcFilterName_Type(DisplayString):
    """Custom type dcFilterName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 35),
    )


_DcFilterName_Type.__name__ = "DisplayString"
_DcFilterName_Object = MibTableColumn
dcFilterName = _DcFilterName_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 8, 6, 1, 2),
    _DcFilterName_Type()
)
dcFilterName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcFilterName.setStatus("current")


class _DcTrueForMin_Type(DisplayString):
    """Custom type dcTrueForMin based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 35),
    )


_DcTrueForMin_Type.__name__ = "DisplayString"
_DcTrueForMin_Object = MibTableColumn
dcTrueForMin = _DcTrueForMin_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 8, 6, 1, 3),
    _DcTrueForMin_Type()
)
dcTrueForMin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dcTrueForMin.setStatus("current")


class _DcFalseForMin_Type(DisplayString):
    """Custom type dcFalseForMin based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 35),
    )


_DcFalseForMin_Type.__name__ = "DisplayString"
_DcFalseForMin_Object = MibTableColumn
dcFalseForMin = _DcFalseForMin_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 8, 6, 1, 4),
    _DcFalseForMin_Type()
)
dcFalseForMin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dcFalseForMin.setStatus("current")
_DcTimerTable_Object = MibTable
dcTimerTable = _DcTimerTable_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 8, 7)
)
if mibBuilder.loadTexts:
    dcTimerTable.setStatus("current")
_DcTimerEntry_Object = MibTableRow
dcTimerEntry = _DcTimerEntry_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 8, 7, 1)
)
dcTimerEntry.setIndexNames(
    (0, "ORION-BASE-MIB", "dcTimerIndex"),
)
if mibBuilder.loadTexts:
    dcTimerEntry.setStatus("current")


class _DcTimerIndex_Type(Integer32):
    """Custom type dcTimerIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 20),
    )


_DcTimerIndex_Type.__name__ = "Integer32"
_DcTimerIndex_Object = MibTableColumn
dcTimerIndex = _DcTimerIndex_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 8, 7, 1, 1),
    _DcTimerIndex_Type()
)
dcTimerIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dcTimerIndex.setStatus("current")


class _DcTimerName_Type(DisplayString):
    """Custom type dcTimerName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 35),
    )


_DcTimerName_Type.__name__ = "DisplayString"
_DcTimerName_Object = MibTableColumn
dcTimerName = _DcTimerName_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 8, 7, 1, 2),
    _DcTimerName_Type()
)
dcTimerName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcTimerName.setStatus("current")


class _DcStartTime_Type(DisplayString):
    """Custom type dcStartTime based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_DcStartTime_Type.__name__ = "DisplayString"
_DcStartTime_Object = MibTableColumn
dcStartTime = _DcStartTime_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 8, 7, 1, 3),
    _DcStartTime_Type()
)
dcStartTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dcStartTime.setStatus("current")


class _DcStartDaySu_Type(Integer32):
    """Custom type dcStartDaySu based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_DcStartDaySu_Type.__name__ = "Integer32"
_DcStartDaySu_Object = MibTableColumn
dcStartDaySu = _DcStartDaySu_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 8, 7, 1, 4),
    _DcStartDaySu_Type()
)
dcStartDaySu.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dcStartDaySu.setStatus("current")


class _DcStartDayMo_Type(Integer32):
    """Custom type dcStartDayMo based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_DcStartDayMo_Type.__name__ = "Integer32"
_DcStartDayMo_Object = MibTableColumn
dcStartDayMo = _DcStartDayMo_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 8, 7, 1, 5),
    _DcStartDayMo_Type()
)
dcStartDayMo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dcStartDayMo.setStatus("current")


class _DcStartDayTu_Type(Integer32):
    """Custom type dcStartDayTu based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_DcStartDayTu_Type.__name__ = "Integer32"
_DcStartDayTu_Object = MibTableColumn
dcStartDayTu = _DcStartDayTu_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 8, 7, 1, 6),
    _DcStartDayTu_Type()
)
dcStartDayTu.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dcStartDayTu.setStatus("current")


class _DcStartDayWe_Type(Integer32):
    """Custom type dcStartDayWe based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_DcStartDayWe_Type.__name__ = "Integer32"
_DcStartDayWe_Object = MibTableColumn
dcStartDayWe = _DcStartDayWe_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 8, 7, 1, 7),
    _DcStartDayWe_Type()
)
dcStartDayWe.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dcStartDayWe.setStatus("current")


class _DcStartDayTh_Type(Integer32):
    """Custom type dcStartDayTh based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_DcStartDayTh_Type.__name__ = "Integer32"
_DcStartDayTh_Object = MibTableColumn
dcStartDayTh = _DcStartDayTh_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 8, 7, 1, 8),
    _DcStartDayTh_Type()
)
dcStartDayTh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dcStartDayTh.setStatus("current")


class _DcStartDayFr_Type(Integer32):
    """Custom type dcStartDayFr based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_DcStartDayFr_Type.__name__ = "Integer32"
_DcStartDayFr_Object = MibTableColumn
dcStartDayFr = _DcStartDayFr_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 8, 7, 1, 9),
    _DcStartDayFr_Type()
)
dcStartDayFr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dcStartDayFr.setStatus("current")


class _DcStartDaySa_Type(Integer32):
    """Custom type dcStartDaySa based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_DcStartDaySa_Type.__name__ = "Integer32"
_DcStartDaySa_Object = MibTableColumn
dcStartDaySa = _DcStartDaySa_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 8, 7, 1, 10),
    _DcStartDaySa_Type()
)
dcStartDaySa.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dcStartDaySa.setStatus("current")


class _DcEndTime_Type(DisplayString):
    """Custom type dcEndTime based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_DcEndTime_Type.__name__ = "DisplayString"
_DcEndTime_Object = MibTableColumn
dcEndTime = _DcEndTime_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 8, 7, 1, 11),
    _DcEndTime_Type()
)
dcEndTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dcEndTime.setStatus("current")


class _DcEndDaySu_Type(Integer32):
    """Custom type dcEndDaySu based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_DcEndDaySu_Type.__name__ = "Integer32"
_DcEndDaySu_Object = MibTableColumn
dcEndDaySu = _DcEndDaySu_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 8, 7, 1, 12),
    _DcEndDaySu_Type()
)
dcEndDaySu.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dcEndDaySu.setStatus("current")


class _DcEndDayMo_Type(Integer32):
    """Custom type dcEndDayMo based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_DcEndDayMo_Type.__name__ = "Integer32"
_DcEndDayMo_Object = MibTableColumn
dcEndDayMo = _DcEndDayMo_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 8, 7, 1, 13),
    _DcEndDayMo_Type()
)
dcEndDayMo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dcEndDayMo.setStatus("current")


class _DcEndDayTu_Type(Integer32):
    """Custom type dcEndDayTu based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_DcEndDayTu_Type.__name__ = "Integer32"
_DcEndDayTu_Object = MibTableColumn
dcEndDayTu = _DcEndDayTu_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 8, 7, 1, 14),
    _DcEndDayTu_Type()
)
dcEndDayTu.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dcEndDayTu.setStatus("current")


class _DcEndDayWe_Type(Integer32):
    """Custom type dcEndDayWe based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_DcEndDayWe_Type.__name__ = "Integer32"
_DcEndDayWe_Object = MibTableColumn
dcEndDayWe = _DcEndDayWe_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 8, 7, 1, 15),
    _DcEndDayWe_Type()
)
dcEndDayWe.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dcEndDayWe.setStatus("current")


class _DcEndDayTh_Type(Integer32):
    """Custom type dcEndDayTh based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_DcEndDayTh_Type.__name__ = "Integer32"
_DcEndDayTh_Object = MibTableColumn
dcEndDayTh = _DcEndDayTh_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 8, 7, 1, 16),
    _DcEndDayTh_Type()
)
dcEndDayTh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dcEndDayTh.setStatus("current")


class _DcEndDayFr_Type(Integer32):
    """Custom type dcEndDayFr based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_DcEndDayFr_Type.__name__ = "Integer32"
_DcEndDayFr_Object = MibTableColumn
dcEndDayFr = _DcEndDayFr_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 8, 7, 1, 17),
    _DcEndDayFr_Type()
)
dcEndDayFr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dcEndDayFr.setStatus("current")


class _DcEndDaySa_Type(Integer32):
    """Custom type dcEndDaySa based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_DcEndDaySa_Type.__name__ = "Integer32"
_DcEndDaySa_Object = MibTableColumn
dcEndDaySa = _DcEndDaySa_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 8, 7, 1, 18),
    _DcEndDaySa_Type()
)
dcEndDaySa.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dcEndDaySa.setStatus("current")
_DcMeasurement_ObjectIdentity = ObjectIdentity
dcMeasurement = _DcMeasurement_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 9)
)
_DcMeasurementTable_Object = MibTable
dcMeasurementTable = _DcMeasurementTable_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 9, 1)
)
if mibBuilder.loadTexts:
    dcMeasurementTable.setStatus("current")
_DcMeasurementEntry_Object = MibTableRow
dcMeasurementEntry = _DcMeasurementEntry_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 9, 1, 1)
)
dcMeasurementEntry.setIndexNames(
    (0, "ORION-BASE-MIB", "dcMeasurementIndex"),
)
if mibBuilder.loadTexts:
    dcMeasurementEntry.setStatus("current")


class _DcMeasurementIndex_Type(Integer32):
    """Custom type dcMeasurementIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 500),
    )


_DcMeasurementIndex_Type.__name__ = "Integer32"
_DcMeasurementIndex_Object = MibTableColumn
dcMeasurementIndex = _DcMeasurementIndex_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 9, 1, 1, 1),
    _DcMeasurementIndex_Type()
)
dcMeasurementIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dcMeasurementIndex.setStatus("current")


class _DcMeasurementName_Type(DisplayString):
    """Custom type dcMeasurementName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_DcMeasurementName_Type.__name__ = "DisplayString"
_DcMeasurementName_Object = MibTableColumn
dcMeasurementName = _DcMeasurementName_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 9, 1, 1, 2),
    _DcMeasurementName_Type()
)
dcMeasurementName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcMeasurementName.setStatus("current")
_DcMeasurementValue_Type = Integer32
_DcMeasurementValue_Object = MibTableColumn
dcMeasurementValue = _DcMeasurementValue_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 9, 1, 1, 3),
    _DcMeasurementValue_Type()
)
dcMeasurementValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcMeasurementValue.setStatus("current")
_DcMeasurementScaleFactor_Type = Integer32
_DcMeasurementScaleFactor_Object = MibTableColumn
dcMeasurementScaleFactor = _DcMeasurementScaleFactor_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 9, 1, 1, 4),
    _DcMeasurementScaleFactor_Type()
)
dcMeasurementScaleFactor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcMeasurementScaleFactor.setStatus("current")


class _DcMeasurementUnit_Type(Integer32):
    """Custom type dcMeasurementUnit based on Integer32"""
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
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 1),
          ("none", 2),
          ("voltDC", 3),
          ("voltAC", 4),
          ("ampere", 5),
          ("ampereHour", 6),
          ("temperature", 7),
          ("temperatureCoefficient", 8),
          ("watt", 9),
          ("wattHour", 10),
          ("seconds", 11),
          ("percent", 12),
          ("hertz", 13),
          ("voltAmpere", 14),
          ("voltAmpereReactive", 15),
          ("voltAmpereReactiveHour", 16),
          ("voltAmpereHour", 17))
    )


_DcMeasurementUnit_Type.__name__ = "Integer32"
_DcMeasurementUnit_Object = MibTableColumn
dcMeasurementUnit = _DcMeasurementUnit_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 9, 1, 1, 5),
    _DcMeasurementUnit_Type()
)
dcMeasurementUnit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcMeasurementUnit.setStatus("current")
_DcMeterPanel_ObjectIdentity = ObjectIdentity
dcMeterPanel = _DcMeterPanel_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 10)
)
_DcMeterPanelEventTable_Object = MibTable
dcMeterPanelEventTable = _DcMeterPanelEventTable_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 10, 1)
)
if mibBuilder.loadTexts:
    dcMeterPanelEventTable.setStatus("current")
_DcMeterPanelEventEntry_Object = MibTableRow
dcMeterPanelEventEntry = _DcMeterPanelEventEntry_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 10, 1, 1)
)
dcMeterPanelEventEntry.setIndexNames(
    (0, "ORION-BASE-MIB", "dcMeterPanelEventIndex"),
)
if mibBuilder.loadTexts:
    dcMeterPanelEventEntry.setStatus("current")


class _DcMeterPanelEventIndex_Type(Integer32):
    """Custom type dcMeterPanelEventIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 128),
    )


_DcMeterPanelEventIndex_Type.__name__ = "Integer32"
_DcMeterPanelEventIndex_Object = MibTableColumn
dcMeterPanelEventIndex = _DcMeterPanelEventIndex_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 10, 1, 1, 1),
    _DcMeterPanelEventIndex_Type()
)
dcMeterPanelEventIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dcMeterPanelEventIndex.setStatus("current")


class _DcMeterPanelEventName_Type(DisplayString):
    """Custom type dcMeterPanelEventName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_DcMeterPanelEventName_Type.__name__ = "DisplayString"
_DcMeterPanelEventName_Object = MibTableColumn
dcMeterPanelEventName = _DcMeterPanelEventName_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 10, 1, 1, 2),
    _DcMeterPanelEventName_Type()
)
dcMeterPanelEventName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcMeterPanelEventName.setStatus("current")


class _DcMeterPanelEventValue_Type(Integer32):
    """Custom type dcMeterPanelEventValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("false", 1),
          ("indeterminate", 2),
          ("true", 3))
    )


_DcMeterPanelEventValue_Type.__name__ = "Integer32"
_DcMeterPanelEventValue_Object = MibTableColumn
dcMeterPanelEventValue = _DcMeterPanelEventValue_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 10, 1, 1, 3),
    _DcMeterPanelEventValue_Type()
)
dcMeterPanelEventValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcMeterPanelEventValue.setStatus("current")
_DcMeterPanelEventHourMeterValue_Type = Gauge32
_DcMeterPanelEventHourMeterValue_Object = MibTableColumn
dcMeterPanelEventHourMeterValue = _DcMeterPanelEventHourMeterValue_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 10, 1, 1, 4),
    _DcMeterPanelEventHourMeterValue_Type()
)
dcMeterPanelEventHourMeterValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcMeterPanelEventHourMeterValue.setStatus("current")
if mibBuilder.loadTexts:
    dcMeterPanelEventHourMeterValue.setUnits("seconds")
_DcMeterPanelMeasurementTable_Object = MibTable
dcMeterPanelMeasurementTable = _DcMeterPanelMeasurementTable_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 10, 2)
)
if mibBuilder.loadTexts:
    dcMeterPanelMeasurementTable.setStatus("current")
_DcMeterPanelMeasurementEntry_Object = MibTableRow
dcMeterPanelMeasurementEntry = _DcMeterPanelMeasurementEntry_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 10, 2, 1)
)
dcMeterPanelMeasurementEntry.setIndexNames(
    (0, "ORION-BASE-MIB", "dcMeterPanelMeasurementIndex"),
)
if mibBuilder.loadTexts:
    dcMeterPanelMeasurementEntry.setStatus("current")


class _DcMeterPanelMeasurementIndex_Type(Integer32):
    """Custom type dcMeterPanelMeasurementIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 128),
    )


_DcMeterPanelMeasurementIndex_Type.__name__ = "Integer32"
_DcMeterPanelMeasurementIndex_Object = MibTableColumn
dcMeterPanelMeasurementIndex = _DcMeterPanelMeasurementIndex_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 10, 2, 1, 1),
    _DcMeterPanelMeasurementIndex_Type()
)
dcMeterPanelMeasurementIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dcMeterPanelMeasurementIndex.setStatus("current")


class _DcMeterPanelMeasurementName_Type(DisplayString):
    """Custom type dcMeterPanelMeasurementName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_DcMeterPanelMeasurementName_Type.__name__ = "DisplayString"
_DcMeterPanelMeasurementName_Object = MibTableColumn
dcMeterPanelMeasurementName = _DcMeterPanelMeasurementName_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 10, 2, 1, 2),
    _DcMeterPanelMeasurementName_Type()
)
dcMeterPanelMeasurementName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcMeterPanelMeasurementName.setStatus("current")
_DcMeterPanelMeasurementValue_Type = DisplayString
_DcMeterPanelMeasurementValue_Object = MibTableColumn
dcMeterPanelMeasurementValue = _DcMeterPanelMeasurementValue_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 10, 2, 1, 3),
    _DcMeterPanelMeasurementValue_Type()
)
dcMeterPanelMeasurementValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcMeterPanelMeasurementValue.setStatus("current")


class _DcMeterPanelMeasurementUnit_Type(DisplayString):
    """Custom type dcMeterPanelMeasurementUnit based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_DcMeterPanelMeasurementUnit_Type.__name__ = "DisplayString"
_DcMeterPanelMeasurementUnit_Object = MibTableColumn
dcMeterPanelMeasurementUnit = _DcMeterPanelMeasurementUnit_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 10, 2, 1, 4),
    _DcMeterPanelMeasurementUnit_Type()
)
dcMeterPanelMeasurementUnit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcMeterPanelMeasurementUnit.setStatus("current")
_DcPVC_ObjectIdentity = ObjectIdentity
dcPVC = _DcPVC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 11)
)


class _DcNumberPVCs_Type(Gauge32):
    """Custom type dcNumberPVCs based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32),
    )


_DcNumberPVCs_Type.__name__ = "Gauge32"
_DcNumberPVCs_Object = MibScalar
dcNumberPVCs = _DcNumberPVCs_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 11, 1),
    _DcNumberPVCs_Type()
)
dcNumberPVCs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcNumberPVCs.setStatus("current")


class _DcNumberPVCsFailure_Type(Gauge32):
    """Custom type dcNumberPVCsFailure based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32),
    )


_DcNumberPVCsFailure_Type.__name__ = "Gauge32"
_DcNumberPVCsFailure_Object = MibScalar
dcNumberPVCsFailure = _DcNumberPVCsFailure_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 11, 2),
    _DcNumberPVCsFailure_Type()
)
dcNumberPVCsFailure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcNumberPVCsFailure.setStatus("current")


class _DcNumberPVCsOkay_Type(Gauge32):
    """Custom type dcNumberPVCsOkay based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32),
    )


_DcNumberPVCsOkay_Type.__name__ = "Gauge32"
_DcNumberPVCsOkay_Object = MibScalar
dcNumberPVCsOkay = _DcNumberPVCsOkay_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 11, 3),
    _DcNumberPVCsOkay_Type()
)
dcNumberPVCsOkay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcNumberPVCsOkay.setStatus("current")
_DcPVCTable_Object = MibTable
dcPVCTable = _DcPVCTable_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 11, 4)
)
if mibBuilder.loadTexts:
    dcPVCTable.setStatus("current")
_DcPVCEntry_Object = MibTableRow
dcPVCEntry = _DcPVCEntry_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 11, 4, 1)
)
dcPVCEntry.setIndexNames(
    (0, "ORION-BASE-MIB", "dcPVCIndex"),
)
if mibBuilder.loadTexts:
    dcPVCEntry.setStatus("current")


class _DcPVCIndex_Type(Integer32):
    """Custom type dcPVCIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_DcPVCIndex_Type.__name__ = "Integer32"
_DcPVCIndex_Object = MibTableColumn
dcPVCIndex = _DcPVCIndex_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 11, 4, 1, 1),
    _DcPVCIndex_Type()
)
dcPVCIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dcPVCIndex.setStatus("current")


class _DcPVCIdentifier_Type(DisplayString):
    """Custom type dcPVCIdentifier based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_DcPVCIdentifier_Type.__name__ = "DisplayString"
_DcPVCIdentifier_Object = MibTableColumn
dcPVCIdentifier = _DcPVCIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 11, 4, 1, 2),
    _DcPVCIdentifier_Type()
)
dcPVCIdentifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcPVCIdentifier.setStatus("current")


class _DcPVCSlotState_Type(Integer32):
    """Custom type dcPVCSlotState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("noPos", 1),
          ("empty", 2),
          ("lost", 3),
          ("new", 4),
          ("off", 5),
          ("on", 6))
    )


_DcPVCSlotState_Type.__name__ = "Integer32"
_DcPVCSlotState_Object = MibTableColumn
dcPVCSlotState = _DcPVCSlotState_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 11, 4, 1, 3),
    _DcPVCSlotState_Type()
)
dcPVCSlotState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcPVCSlotState.setStatus("current")


class _DcPVCMainStatus_Type(Integer32):
    """Custom type dcPVCMainStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 1),
          ("on", 2),
          ("remoteOff", 3),
          ("off", 4),
          ("temporaryInternalOff", 5),
          ("latchedInternalOff", 6),
          ("error", 7))
    )


_DcPVCMainStatus_Type.__name__ = "Integer32"
_DcPVCMainStatus_Object = MibTableColumn
dcPVCMainStatus = _DcPVCMainStatus_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 11, 4, 1, 4),
    _DcPVCMainStatus_Type()
)
dcPVCMainStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcPVCMainStatus.setStatus("current")


class _DcPVCSubStatus_Type(Integer32):
    """Custom type dcPVCSubStatus based on Integer32"""
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
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 1),
          ("notAvailable", 2),
          ("mppt", 3),
          ("voltageMode", 4),
          ("outputCurrentLimit", 5),
          ("outputPowerLimit", 6),
          ("inputCurrentLimit", 7),
          ("inputPowerLimit", 8),
          ("inputVoltageOutsideRange", 9),
          ("sunset", 10),
          ("breakerOpen", 11),
          ("startUpDelay", 12),
          ("otp", 13),
          ("ovp", 14),
          ("fanFailure", 15))
    )


_DcPVCSubStatus_Type.__name__ = "Integer32"
_DcPVCSubStatus_Object = MibTableColumn
dcPVCSubStatus = _DcPVCSubStatus_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 11, 4, 1, 5),
    _DcPVCSubStatus_Type()
)
dcPVCSubStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcPVCSubStatus.setStatus("current")


class _DcPVCConfiguration_Type(Integer32):
    """Custom type dcPVCConfiguration based on Integer32"""
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
          ("ok", 2),
          ("default", 3),
          ("outsideLimts", 4),
          ("invalid", 5))
    )


_DcPVCConfiguration_Type.__name__ = "Integer32"
_DcPVCConfiguration_Object = MibTableColumn
dcPVCConfiguration = _DcPVCConfiguration_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 11, 4, 1, 6),
    _DcPVCConfiguration_Type()
)
dcPVCConfiguration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcPVCConfiguration.setStatus("current")
_DcPVCIout_Type = Integer32
_DcPVCIout_Object = MibTableColumn
dcPVCIout = _DcPVCIout_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 11, 4, 1, 7),
    _DcPVCIout_Type()
)
dcPVCIout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcPVCIout.setStatus("current")
if mibBuilder.loadTexts:
    dcPVCIout.setUnits("100 mA")
_DcPVCUout_Type = Integer32
_DcPVCUout_Object = MibTableColumn
dcPVCUout = _DcPVCUout_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 11, 4, 1, 8),
    _DcPVCUout_Type()
)
dcPVCUout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcPVCUout.setStatus("current")
if mibBuilder.loadTexts:
    dcPVCUout.setUnits("10 mV")
_DcPVCIin_Type = Integer32
_DcPVCIin_Object = MibTableColumn
dcPVCIin = _DcPVCIin_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 11, 4, 1, 9),
    _DcPVCIin_Type()
)
dcPVCIin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcPVCIin.setStatus("current")
if mibBuilder.loadTexts:
    dcPVCIin.setUnits("100 mA")
_DcPVCUin_Type = Integer32
_DcPVCUin_Object = MibTableColumn
dcPVCUin = _DcPVCUin_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 11, 4, 1, 10),
    _DcPVCUin_Type()
)
dcPVCUin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcPVCUin.setStatus("current")
if mibBuilder.loadTexts:
    dcPVCUin.setUnits("100 mV")
_DcPVCGroupTable_Object = MibTable
dcPVCGroupTable = _DcPVCGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 11, 5)
)
if mibBuilder.loadTexts:
    dcPVCGroupTable.setStatus("current")
_DcPVCGroupEntry_Object = MibTableRow
dcPVCGroupEntry = _DcPVCGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 11, 5, 1)
)
dcPVCGroupEntry.setIndexNames(
    (0, "ORION-BASE-MIB", "dcPVCGroupIndex"),
)
if mibBuilder.loadTexts:
    dcPVCGroupEntry.setStatus("current")


class _DcPVCGroupIndex_Type(Integer32):
    """Custom type dcPVCGroupIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
    )


_DcPVCGroupIndex_Type.__name__ = "Integer32"
_DcPVCGroupIndex_Object = MibTableColumn
dcPVCGroupIndex = _DcPVCGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 11, 5, 1, 1),
    _DcPVCGroupIndex_Type()
)
dcPVCGroupIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dcPVCGroupIndex.setStatus("current")


class _DcPVCGroupPVCType_Type(Integer32):
    """Custom type dcPVCGroupPVCType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("unknown48V", 1),
          ("pvc2200B48", 2))
    )


_DcPVCGroupPVCType_Type.__name__ = "Integer32"
_DcPVCGroupPVCType_Object = MibTableColumn
dcPVCGroupPVCType = _DcPVCGroupPVCType_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 11, 5, 1, 2),
    _DcPVCGroupPVCType_Type()
)
dcPVCGroupPVCType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcPVCGroupPVCType.setStatus("current")
_DcPVCGroupVoltage_Type = Integer32
_DcPVCGroupVoltage_Object = MibTableColumn
dcPVCGroupVoltage = _DcPVCGroupVoltage_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 11, 5, 1, 3),
    _DcPVCGroupVoltage_Type()
)
dcPVCGroupVoltage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dcPVCGroupVoltage.setStatus("current")
if mibBuilder.loadTexts:
    dcPVCGroupVoltage.setUnits("10 mV")
_DcPVCGroupVPGM_Type = Integer32
_DcPVCGroupVPGM_Object = MibTableColumn
dcPVCGroupVPGM = _DcPVCGroupVPGM_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 11, 5, 1, 4),
    _DcPVCGroupVPGM_Type()
)
dcPVCGroupVPGM.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dcPVCGroupVPGM.setStatus("current")
if mibBuilder.loadTexts:
    dcPVCGroupVPGM.setUnits("10 mV")
_DcPVCGroupInputLowOff_Type = Integer32
_DcPVCGroupInputLowOff_Object = MibTableColumn
dcPVCGroupInputLowOff = _DcPVCGroupInputLowOff_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 11, 5, 1, 5),
    _DcPVCGroupInputLowOff_Type()
)
dcPVCGroupInputLowOff.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dcPVCGroupInputLowOff.setStatus("current")
if mibBuilder.loadTexts:
    dcPVCGroupInputLowOff.setUnits("100 mV")
_DcPVCGroupInputLowOn_Type = Integer32
_DcPVCGroupInputLowOn_Object = MibTableColumn
dcPVCGroupInputLowOn = _DcPVCGroupInputLowOn_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 11, 5, 1, 6),
    _DcPVCGroupInputLowOn_Type()
)
dcPVCGroupInputLowOn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dcPVCGroupInputLowOn.setStatus("current")
if mibBuilder.loadTexts:
    dcPVCGroupInputLowOn.setUnits("100 mV")
_DcPVCGroupStartUpDelay_Type = Gauge32
_DcPVCGroupStartUpDelay_Object = MibTableColumn
dcPVCGroupStartUpDelay = _DcPVCGroupStartUpDelay_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 11, 5, 1, 7),
    _DcPVCGroupStartUpDelay_Type()
)
dcPVCGroupStartUpDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dcPVCGroupStartUpDelay.setStatus("current")
if mibBuilder.loadTexts:
    dcPVCGroupStartUpDelay.setUnits("seconds")
_DcPVCGroupOvpLimit_Type = Integer32
_DcPVCGroupOvpLimit_Object = MibTableColumn
dcPVCGroupOvpLimit = _DcPVCGroupOvpLimit_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 11, 5, 1, 8),
    _DcPVCGroupOvpLimit_Type()
)
dcPVCGroupOvpLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dcPVCGroupOvpLimit.setStatus("current")
if mibBuilder.loadTexts:
    dcPVCGroupOvpLimit.setUnits("10 mV")
_DcPVCGroupAlarmDelay_Type = Gauge32
_DcPVCGroupAlarmDelay_Object = MibTableColumn
dcPVCGroupAlarmDelay = _DcPVCGroupAlarmDelay_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 11, 5, 1, 9),
    _DcPVCGroupAlarmDelay_Type()
)
dcPVCGroupAlarmDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dcPVCGroupAlarmDelay.setStatus("current")
if mibBuilder.loadTexts:
    dcPVCGroupAlarmDelay.setUnits("seconds")
_DcInventory_ObjectIdentity = ObjectIdentity
dcInventory = _DcInventory_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 12)
)
_DcInventoryTable_Object = MibTable
dcInventoryTable = _DcInventoryTable_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 12, 1)
)
if mibBuilder.loadTexts:
    dcInventoryTable.setStatus("current")
_DcInventoryEntry_Object = MibTableRow
dcInventoryEntry = _DcInventoryEntry_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 12, 1, 1)
)
dcInventoryEntry.setIndexNames(
    (0, "ORION-BASE-MIB", "dcInventoryIndex"),
)
if mibBuilder.loadTexts:
    dcInventoryEntry.setStatus("current")


class _DcInventoryIndex_Type(Integer32):
    """Custom type dcInventoryIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10000),
    )


_DcInventoryIndex_Type.__name__ = "Integer32"
_DcInventoryIndex_Object = MibTableColumn
dcInventoryIndex = _DcInventoryIndex_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 12, 1, 1, 1),
    _DcInventoryIndex_Type()
)
dcInventoryIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dcInventoryIndex.setStatus("current")


class _DcInventoryType_Type(DisplayString):
    """Custom type dcInventoryType based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_DcInventoryType_Type.__name__ = "DisplayString"
_DcInventoryType_Object = MibTableColumn
dcInventoryType = _DcInventoryType_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 12, 1, 1, 2),
    _DcInventoryType_Type()
)
dcInventoryType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcInventoryType.setStatus("current")


class _DcInventoryName_Type(DisplayString):
    """Custom type dcInventoryName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_DcInventoryName_Type.__name__ = "DisplayString"
_DcInventoryName_Object = MibTableColumn
dcInventoryName = _DcInventoryName_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 12, 1, 1, 3),
    _DcInventoryName_Type()
)
dcInventoryName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcInventoryName.setStatus("current")


class _DcInventorySwVersion_Type(DisplayString):
    """Custom type dcInventorySwVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_DcInventorySwVersion_Type.__name__ = "DisplayString"
_DcInventorySwVersion_Object = MibTableColumn
dcInventorySwVersion = _DcInventorySwVersion_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 12, 1, 1, 4),
    _DcInventorySwVersion_Type()
)
dcInventorySwVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcInventorySwVersion.setStatus("current")


class _DcInventoryBuildVersion_Type(DisplayString):
    """Custom type dcInventoryBuildVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_DcInventoryBuildVersion_Type.__name__ = "DisplayString"
_DcInventoryBuildVersion_Object = MibTableColumn
dcInventoryBuildVersion = _DcInventoryBuildVersion_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 12, 1, 1, 5),
    _DcInventoryBuildVersion_Type()
)
dcInventoryBuildVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcInventoryBuildVersion.setStatus("current")


class _DcInventoryPartNb_Type(DisplayString):
    """Custom type dcInventoryPartNb based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_DcInventoryPartNb_Type.__name__ = "DisplayString"
_DcInventoryPartNb_Object = MibTableColumn
dcInventoryPartNb = _DcInventoryPartNb_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 12, 1, 1, 6),
    _DcInventoryPartNb_Type()
)
dcInventoryPartNb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcInventoryPartNb.setStatus("current")


class _DcInventorySerialNb_Type(DisplayString):
    """Custom type dcInventorySerialNb based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_DcInventorySerialNb_Type.__name__ = "DisplayString"
_DcInventorySerialNb_Object = MibTableColumn
dcInventorySerialNb = _DcInventorySerialNb_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 12, 1, 1, 7),
    _DcInventorySerialNb_Type()
)
dcInventorySerialNb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcInventorySerialNb.setStatus("current")


class _DcInventoryTopLevel_Type(DisplayString):
    """Custom type dcInventoryTopLevel based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_DcInventoryTopLevel_Type.__name__ = "DisplayString"
_DcInventoryTopLevel_Object = MibTableColumn
dcInventoryTopLevel = _DcInventoryTopLevel_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 12, 1, 1, 8),
    _DcInventoryTopLevel_Type()
)
dcInventoryTopLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcInventoryTopLevel.setStatus("current")
_DcIP_ObjectIdentity = ObjectIdentity
dcIP = _DcIP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 13)
)
_DcIPv4_ObjectIdentity = ObjectIdentity
dcIPv4 = _DcIPv4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 13, 1)
)
_DcIPv4Address_Type = InetAddress
_DcIPv4Address_Object = MibScalar
dcIPv4Address = _DcIPv4Address_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 13, 1, 1),
    _DcIPv4Address_Type()
)
dcIPv4Address.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcIPv4Address.setStatus("current")
_DcIPv4SubnetMask_Type = InetAddress
_DcIPv4SubnetMask_Object = MibScalar
dcIPv4SubnetMask = _DcIPv4SubnetMask_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 13, 1, 2),
    _DcIPv4SubnetMask_Type()
)
dcIPv4SubnetMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcIPv4SubnetMask.setStatus("current")
_DcIPv4Gateway_Type = InetAddress
_DcIPv4Gateway_Object = MibScalar
dcIPv4Gateway = _DcIPv4Gateway_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 13, 1, 3),
    _DcIPv4Gateway_Type()
)
dcIPv4Gateway.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcIPv4Gateway.setStatus("current")
_DcIPv4DNS_Type = InetAddress
_DcIPv4DNS_Object = MibScalar
dcIPv4DNS = _DcIPv4DNS_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 13, 1, 4),
    _DcIPv4DNS_Type()
)
dcIPv4DNS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcIPv4DNS.setStatus("current")
_DcIPv6_ObjectIdentity = ObjectIdentity
dcIPv6 = _DcIPv6_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 13, 2)
)
_DcIPv6LinkLocalAddress_Type = InetAddress
_DcIPv6LinkLocalAddress_Object = MibScalar
dcIPv6LinkLocalAddress = _DcIPv6LinkLocalAddress_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 13, 2, 1),
    _DcIPv6LinkLocalAddress_Type()
)
dcIPv6LinkLocalAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcIPv6LinkLocalAddress.setStatus("current")
_DcIPv6Address_Type = InetAddress
_DcIPv6Address_Object = MibScalar
dcIPv6Address = _DcIPv6Address_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 13, 2, 2),
    _DcIPv6Address_Type()
)
dcIPv6Address.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcIPv6Address.setStatus("current")
_DcIPv6Gateway_Type = InetAddress
_DcIPv6Gateway_Object = MibScalar
dcIPv6Gateway = _DcIPv6Gateway_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 13, 2, 3),
    _DcIPv6Gateway_Type()
)
dcIPv6Gateway.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcIPv6Gateway.setStatus("current")
_DcIPv6DNSAuto_Type = InetAddress
_DcIPv6DNSAuto_Object = MibScalar
dcIPv6DNSAuto = _DcIPv6DNSAuto_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 13, 2, 4),
    _DcIPv6DNSAuto_Type()
)
dcIPv6DNSAuto.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcIPv6DNSAuto.setStatus("current")
_DcIPv6DNSManual_Type = InetAddress
_DcIPv6DNSManual_Object = MibScalar
dcIPv6DNSManual = _DcIPv6DNSManual_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 13, 2, 5),
    _DcIPv6DNSManual_Type()
)
dcIPv6DNSManual.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcIPv6DNSManual.setStatus("current")
_DcAircon_ObjectIdentity = ObjectIdentity
dcAircon = _DcAircon_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 14)
)
_DcAirconTable_Object = MibTable
dcAirconTable = _DcAirconTable_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 14, 1)
)
if mibBuilder.loadTexts:
    dcAirconTable.setStatus("current")
_DcAirconEntry_Object = MibTableRow
dcAirconEntry = _DcAirconEntry_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 14, 1, 1)
)
dcAirconEntry.setIndexNames(
    (0, "ORION-BASE-MIB", "dcAirconIndex"),
    (0, "ORION-BASE-MIB", "dcCoolingPlanIndex"),
)
if mibBuilder.loadTexts:
    dcAirconEntry.setStatus("current")


class _DcAirconIndex_Type(Integer32):
    """Custom type dcAirconIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10000),
    )


_DcAirconIndex_Type.__name__ = "Integer32"
_DcAirconIndex_Object = MibTableColumn
dcAirconIndex = _DcAirconIndex_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 14, 1, 1, 1),
    _DcAirconIndex_Type()
)
dcAirconIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dcAirconIndex.setStatus("current")


class _DcCoolingPlanIndex_Type(Integer32):
    """Custom type dcCoolingPlanIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10000),
    )


_DcCoolingPlanIndex_Type.__name__ = "Integer32"
_DcCoolingPlanIndex_Object = MibTableColumn
dcCoolingPlanIndex = _DcCoolingPlanIndex_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 14, 1, 1, 2),
    _DcCoolingPlanIndex_Type()
)
dcCoolingPlanIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dcCoolingPlanIndex.setStatus("current")
_DcAirconName_Type = DisplayString
_DcAirconName_Object = MibTableColumn
dcAirconName = _DcAirconName_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 14, 1, 1, 3),
    _DcAirconName_Type()
)
dcAirconName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcAirconName.setStatus("current")


class _DcAirconMainStatus_Type(Integer32):
    """Custom type dcAirconMainStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 1),
          ("on", 2),
          ("remoteOff", 3),
          ("standby", 4),
          ("warning", 5),
          ("temporaryInternalOff", 6))
    )


_DcAirconMainStatus_Type.__name__ = "Integer32"
_DcAirconMainStatus_Object = MibTableColumn
dcAirconMainStatus = _DcAirconMainStatus_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 14, 1, 1, 4),
    _DcAirconMainStatus_Type()
)
dcAirconMainStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcAirconMainStatus.setStatus("current")


class _DcAirconSubStatus_Type(Integer32):
    """Custom type dcAirconSubStatus based on Integer32"""
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
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              14,
              15)
        )
    )
    namedValues = NamedValues(
        *(("na", 1),
          ("unknown", 2),
          ("cooling", 3),
          ("silentCooling", 4),
          ("selfTest", 5),
          ("heating", 6),
          ("targetTemperatureReached", 7),
          ("localOff", 8),
          ("forceVentilation", 9),
          ("systemProtection", 10),
          ("temperatureAbnormal", 11),
          ("temperatureSensorFault", 12),
          ("fanFault", 13),
          ("controlDeviceFault", 14),
          ("heatExchangeSystemFault", 14),
          ("environmentalAbnormalAlarm", 15))
    )


_DcAirconSubStatus_Type.__name__ = "Integer32"
_DcAirconSubStatus_Object = MibTableColumn
dcAirconSubStatus = _DcAirconSubStatus_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 14, 1, 1, 5),
    _DcAirconSubStatus_Type()
)
dcAirconSubStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcAirconSubStatus.setStatus("current")


class _DcAirconConfiguration_Type(Integer32):
    """Custom type dcAirconConfiguration based on Integer32"""
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
        *(("ok", 1),
          ("default", 2),
          ("outsideLimit", 3),
          ("invalid", 4))
    )


_DcAirconConfiguration_Type.__name__ = "Integer32"
_DcAirconConfiguration_Object = MibTableColumn
dcAirconConfiguration = _DcAirconConfiguration_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 14, 1, 1, 6),
    _DcAirconConfiguration_Type()
)
dcAirconConfiguration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcAirconConfiguration.setStatus("current")
_DcAirconPlanName_Type = DisplayString
_DcAirconPlanName_Object = MibTableColumn
dcAirconPlanName = _DcAirconPlanName_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 14, 1, 1, 7),
    _DcAirconPlanName_Type()
)
dcAirconPlanName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcAirconPlanName.setStatus("current")
_DcAirconRoomTemp_Type = Integer32
_DcAirconRoomTemp_Object = MibTableColumn
dcAirconRoomTemp = _DcAirconRoomTemp_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 14, 1, 1, 8),
    _DcAirconRoomTemp_Type()
)
dcAirconRoomTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcAirconRoomTemp.setStatus("current")
if mibBuilder.loadTexts:
    dcAirconRoomTemp.setUnits("0.1 degree")
_DcCoolingPlanActivationInput_Type = DisplayString
_DcCoolingPlanActivationInput_Object = MibTableColumn
dcCoolingPlanActivationInput = _DcCoolingPlanActivationInput_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 14, 1, 1, 9),
    _DcCoolingPlanActivationInput_Type()
)
dcCoolingPlanActivationInput.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcCoolingPlanActivationInput.setStatus("current")


class _DcCoolingPlanPriority_Type(Integer32):
    """Custom type dcCoolingPlanPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("priority1", 1),
          ("priority2", 2),
          ("priority3", 3),
          ("priority4", 4),
          ("priority5", 5),
          ("lowest", 6))
    )


_DcCoolingPlanPriority_Type.__name__ = "Integer32"
_DcCoolingPlanPriority_Object = MibTableColumn
dcCoolingPlanPriority = _DcCoolingPlanPriority_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 14, 1, 1, 10),
    _DcCoolingPlanPriority_Type()
)
dcCoolingPlanPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcCoolingPlanPriority.setStatus("current")


class _DcCoolingPlanStatus_Type(Integer32):
    """Custom type dcCoolingPlanStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("inactive", 1),
          ("active", 2),
          ("suppressed", 3))
    )


_DcCoolingPlanStatus_Type.__name__ = "Integer32"
_DcCoolingPlanStatus_Object = MibTableColumn
dcCoolingPlanStatus = _DcCoolingPlanStatus_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 14, 1, 1, 11),
    _DcCoolingPlanStatus_Type()
)
dcCoolingPlanStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcCoolingPlanStatus.setStatus("current")


class _DcCoolingPlanTargetTemp_Type(Integer32):
    """Custom type dcCoolingPlanTargetTemp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(250, 1040),
    )


_DcCoolingPlanTargetTemp_Type.__name__ = "Integer32"
_DcCoolingPlanTargetTemp_Object = MibTableColumn
dcCoolingPlanTargetTemp = _DcCoolingPlanTargetTemp_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 14, 1, 1, 12),
    _DcCoolingPlanTargetTemp_Type()
)
dcCoolingPlanTargetTemp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dcCoolingPlanTargetTemp.setStatus("current")
if mibBuilder.loadTexts:
    dcCoolingPlanTargetTemp.setUnits("0.1 degree")


class _DcCoolingPlanOperatingMode_Type(Integer32):
    """Custom type dcCoolingPlanOperatingMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("normal", 1),
          ("silent", 2),
          ("off", 3))
    )


_DcCoolingPlanOperatingMode_Type.__name__ = "Integer32"
_DcCoolingPlanOperatingMode_Object = MibTableColumn
dcCoolingPlanOperatingMode = _DcCoolingPlanOperatingMode_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 14, 1, 1, 13),
    _DcCoolingPlanOperatingMode_Type()
)
dcCoolingPlanOperatingMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dcCoolingPlanOperatingMode.setStatus("current")


class _DcCoolingPlanStandbyFanSpeed_Type(Integer32):
    """Custom type dcCoolingPlanStandbyFanSpeed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("low", 2),
          ("high", 3))
    )


_DcCoolingPlanStandbyFanSpeed_Type.__name__ = "Integer32"
_DcCoolingPlanStandbyFanSpeed_Object = MibTableColumn
dcCoolingPlanStandbyFanSpeed = _DcCoolingPlanStandbyFanSpeed_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 14, 1, 1, 14),
    _DcCoolingPlanStandbyFanSpeed_Type()
)
dcCoolingPlanStandbyFanSpeed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dcCoolingPlanStandbyFanSpeed.setStatus("current")


class _DcCoolingPlanHeaterStartTemp_Type(Integer32):
    """Custom type dcCoolingPlanHeaterStartTemp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-100, 590),
    )


_DcCoolingPlanHeaterStartTemp_Type.__name__ = "Integer32"
_DcCoolingPlanHeaterStartTemp_Object = MibTableColumn
dcCoolingPlanHeaterStartTemp = _DcCoolingPlanHeaterStartTemp_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 14, 1, 1, 15),
    _DcCoolingPlanHeaterStartTemp_Type()
)
dcCoolingPlanHeaterStartTemp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dcCoolingPlanHeaterStartTemp.setStatus("current")
if mibBuilder.loadTexts:
    dcCoolingPlanHeaterStartTemp.setUnits("0.1 degree")


class _DcCoolingPlanHeaterHyst_Type(Integer32):
    """Custom type dcCoolingPlanHeaterHyst based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 180),
    )


_DcCoolingPlanHeaterHyst_Type.__name__ = "Integer32"
_DcCoolingPlanHeaterHyst_Object = MibTableColumn
dcCoolingPlanHeaterHyst = _DcCoolingPlanHeaterHyst_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 14, 1, 1, 16),
    _DcCoolingPlanHeaterHyst_Type()
)
dcCoolingPlanHeaterHyst.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dcCoolingPlanHeaterHyst.setStatus("current")
if mibBuilder.loadTexts:
    dcCoolingPlanHeaterHyst.setUnits("0.1 degree")


class _DcCoolingPlanHeaterControl_Type(Integer32):
    """Custom type dcCoolingPlanHeaterControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("auto", 1),
          ("manual", 2))
    )


_DcCoolingPlanHeaterControl_Type.__name__ = "Integer32"
_DcCoolingPlanHeaterControl_Object = MibTableColumn
dcCoolingPlanHeaterControl = _DcCoolingPlanHeaterControl_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 14, 1, 1, 17),
    _DcCoolingPlanHeaterControl_Type()
)
dcCoolingPlanHeaterControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dcCoolingPlanHeaterControl.setStatus("current")
_DcInverter_ObjectIdentity = ObjectIdentity
dcInverter = _DcInverter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 15)
)
_DcInverterGroupTable_Object = MibTable
dcInverterGroupTable = _DcInverterGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 15, 1)
)
if mibBuilder.loadTexts:
    dcInverterGroupTable.setStatus("current")
_DcInverterGroupEntry_Object = MibTableRow
dcInverterGroupEntry = _DcInverterGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 15, 1, 1)
)
dcInverterGroupEntry.setIndexNames(
    (0, "ORION-BASE-MIB", "dcInverterGroupIndex"),
)
if mibBuilder.loadTexts:
    dcInverterGroupEntry.setStatus("current")


class _DcInverterGroupIndex_Type(Integer32):
    """Custom type dcInverterGroupIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
    )


_DcInverterGroupIndex_Type.__name__ = "Integer32"
_DcInverterGroupIndex_Object = MibTableColumn
dcInverterGroupIndex = _DcInverterGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 15, 1, 1, 1),
    _DcInverterGroupIndex_Type()
)
dcInverterGroupIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dcInverterGroupIndex.setStatus("current")


class _DcInverterGroupState_Type(Integer32):
    """Custom type dcInverterGroupState based on Integer32"""
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
        *(("invalid", 1),
          ("noAlarm", 2),
          ("nonUrgentAlarm", 3),
          ("urgentAlarm", 4))
    )


_DcInverterGroupState_Type.__name__ = "Integer32"
_DcInverterGroupState_Object = MibTableColumn
dcInverterGroupState = _DcInverterGroupState_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 15, 1, 1, 2),
    _DcInverterGroupState_Type()
)
dcInverterGroupState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcInverterGroupState.setStatus("current")


class _DcInverterGroupLoadPosition_Type(Integer32):
    """Custom type dcInverterGroupLoadPosition based on Integer32"""
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
        *(("invalid", 1),
          ("ac", 2),
          ("dc", 3),
          ("mixed", 4),
          ("unknown", 5))
    )


_DcInverterGroupLoadPosition_Type.__name__ = "Integer32"
_DcInverterGroupLoadPosition_Object = MibTableColumn
dcInverterGroupLoadPosition = _DcInverterGroupLoadPosition_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 15, 1, 1, 3),
    _DcInverterGroupLoadPosition_Type()
)
dcInverterGroupLoadPosition.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcInverterGroupLoadPosition.setStatus("current")
_DcInverterGroupNbrOfConfigInverters_Type = Gauge32
_DcInverterGroupNbrOfConfigInverters_Object = MibTableColumn
dcInverterGroupNbrOfConfigInverters = _DcInverterGroupNbrOfConfigInverters_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 15, 1, 1, 4),
    _DcInverterGroupNbrOfConfigInverters_Type()
)
dcInverterGroupNbrOfConfigInverters.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcInverterGroupNbrOfConfigInverters.setStatus("current")
_DcInverterGroupNbrOfPresentInverters_Type = Gauge32
_DcInverterGroupNbrOfPresentInverters_Object = MibTableColumn
dcInverterGroupNbrOfPresentInverters = _DcInverterGroupNbrOfPresentInverters_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 15, 1, 1, 5),
    _DcInverterGroupNbrOfPresentInverters_Type()
)
dcInverterGroupNbrOfPresentInverters.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcInverterGroupNbrOfPresentInverters.setStatus("current")
_DcInverterGroupPhase_Type = Gauge32
_DcInverterGroupPhase_Object = MibTableColumn
dcInverterGroupPhase = _DcInverterGroupPhase_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 15, 1, 1, 6),
    _DcInverterGroupPhase_Type()
)
dcInverterGroupPhase.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcInverterGroupPhase.setStatus("current")
_DcInverterGroupDcVoltage_Type = Integer32
_DcInverterGroupDcVoltage_Object = MibTableColumn
dcInverterGroupDcVoltage = _DcInverterGroupDcVoltage_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 15, 1, 1, 7),
    _DcInverterGroupDcVoltage_Type()
)
dcInverterGroupDcVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcInverterGroupDcVoltage.setStatus("current")
if mibBuilder.loadTexts:
    dcInverterGroupDcVoltage.setUnits("10 mV")
_DcInverterGroupInputDcPower_Type = Integer32
_DcInverterGroupInputDcPower_Object = MibTableColumn
dcInverterGroupInputDcPower = _DcInverterGroupInputDcPower_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 15, 1, 1, 8),
    _DcInverterGroupInputDcPower_Type()
)
dcInverterGroupInputDcPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcInverterGroupInputDcPower.setStatus("current")
if mibBuilder.loadTexts:
    dcInverterGroupInputDcPower.setUnits("1 W")
_DcInverterGroupInputVoltage1_Type = Integer32
_DcInverterGroupInputVoltage1_Object = MibTableColumn
dcInverterGroupInputVoltage1 = _DcInverterGroupInputVoltage1_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 15, 1, 1, 9),
    _DcInverterGroupInputVoltage1_Type()
)
dcInverterGroupInputVoltage1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcInverterGroupInputVoltage1.setStatus("current")
if mibBuilder.loadTexts:
    dcInverterGroupInputVoltage1.setUnits("100 mV")
_DcInverterGroupInputVoltage2_Type = Integer32
_DcInverterGroupInputVoltage2_Object = MibTableColumn
dcInverterGroupInputVoltage2 = _DcInverterGroupInputVoltage2_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 15, 1, 1, 10),
    _DcInverterGroupInputVoltage2_Type()
)
dcInverterGroupInputVoltage2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcInverterGroupInputVoltage2.setStatus("current")
if mibBuilder.loadTexts:
    dcInverterGroupInputVoltage2.setUnits("100 mV")
_DcInverterGroupInputVoltage3_Type = Integer32
_DcInverterGroupInputVoltage3_Object = MibTableColumn
dcInverterGroupInputVoltage3 = _DcInverterGroupInputVoltage3_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 15, 1, 1, 11),
    _DcInverterGroupInputVoltage3_Type()
)
dcInverterGroupInputVoltage3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcInverterGroupInputVoltage3.setStatus("current")
if mibBuilder.loadTexts:
    dcInverterGroupInputVoltage3.setUnits("100 mV")
_DcInverterGroupInputApparentPower1_Type = Integer32
_DcInverterGroupInputApparentPower1_Object = MibTableColumn
dcInverterGroupInputApparentPower1 = _DcInverterGroupInputApparentPower1_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 15, 1, 1, 12),
    _DcInverterGroupInputApparentPower1_Type()
)
dcInverterGroupInputApparentPower1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcInverterGroupInputApparentPower1.setStatus("current")
if mibBuilder.loadTexts:
    dcInverterGroupInputApparentPower1.setUnits("1 VA")
_DcInverterGroupInputApparentPower2_Type = Integer32
_DcInverterGroupInputApparentPower2_Object = MibTableColumn
dcInverterGroupInputApparentPower2 = _DcInverterGroupInputApparentPower2_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 15, 1, 1, 13),
    _DcInverterGroupInputApparentPower2_Type()
)
dcInverterGroupInputApparentPower2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcInverterGroupInputApparentPower2.setStatus("current")
if mibBuilder.loadTexts:
    dcInverterGroupInputApparentPower2.setUnits("1 VA")
_DcInverterGroupInputApparentPower3_Type = Integer32
_DcInverterGroupInputApparentPower3_Object = MibTableColumn
dcInverterGroupInputApparentPower3 = _DcInverterGroupInputApparentPower3_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 15, 1, 1, 14),
    _DcInverterGroupInputApparentPower3_Type()
)
dcInverterGroupInputApparentPower3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcInverterGroupInputApparentPower3.setStatus("current")
if mibBuilder.loadTexts:
    dcInverterGroupInputApparentPower3.setUnits("1 VA")
_DcInverterGroupInputFrequency_Type = Gauge32
_DcInverterGroupInputFrequency_Object = MibTableColumn
dcInverterGroupInputFrequency = _DcInverterGroupInputFrequency_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 15, 1, 1, 15),
    _DcInverterGroupInputFrequency_Type()
)
dcInverterGroupInputFrequency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcInverterGroupInputFrequency.setStatus("current")
if mibBuilder.loadTexts:
    dcInverterGroupInputFrequency.setUnits("10 mHz")
_DcInverterGroupOutputVoltage1_Type = Integer32
_DcInverterGroupOutputVoltage1_Object = MibTableColumn
dcInverterGroupOutputVoltage1 = _DcInverterGroupOutputVoltage1_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 15, 1, 1, 16),
    _DcInverterGroupOutputVoltage1_Type()
)
dcInverterGroupOutputVoltage1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcInverterGroupOutputVoltage1.setStatus("current")
if mibBuilder.loadTexts:
    dcInverterGroupOutputVoltage1.setUnits("100 mV")
_DcInverterGroupOutputVoltage2_Type = Integer32
_DcInverterGroupOutputVoltage2_Object = MibTableColumn
dcInverterGroupOutputVoltage2 = _DcInverterGroupOutputVoltage2_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 15, 1, 1, 17),
    _DcInverterGroupOutputVoltage2_Type()
)
dcInverterGroupOutputVoltage2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcInverterGroupOutputVoltage2.setStatus("current")
if mibBuilder.loadTexts:
    dcInverterGroupOutputVoltage2.setUnits("100 mV")
_DcInverterGroupOutputVoltage3_Type = Integer32
_DcInverterGroupOutputVoltage3_Object = MibTableColumn
dcInverterGroupOutputVoltage3 = _DcInverterGroupOutputVoltage3_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 15, 1, 1, 18),
    _DcInverterGroupOutputVoltage3_Type()
)
dcInverterGroupOutputVoltage3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcInverterGroupOutputVoltage3.setStatus("current")
if mibBuilder.loadTexts:
    dcInverterGroupOutputVoltage3.setUnits("100 mV")
_DcInverterGroupOutputApparentPower1_Type = Integer32
_DcInverterGroupOutputApparentPower1_Object = MibTableColumn
dcInverterGroupOutputApparentPower1 = _DcInverterGroupOutputApparentPower1_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 15, 1, 1, 19),
    _DcInverterGroupOutputApparentPower1_Type()
)
dcInverterGroupOutputApparentPower1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcInverterGroupOutputApparentPower1.setStatus("current")
if mibBuilder.loadTexts:
    dcInverterGroupOutputApparentPower1.setUnits("1 VA")
_DcInverterGroupOutputApparentPower2_Type = Integer32
_DcInverterGroupOutputApparentPower2_Object = MibTableColumn
dcInverterGroupOutputApparentPower2 = _DcInverterGroupOutputApparentPower2_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 15, 1, 1, 20),
    _DcInverterGroupOutputApparentPower2_Type()
)
dcInverterGroupOutputApparentPower2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcInverterGroupOutputApparentPower2.setStatus("current")
if mibBuilder.loadTexts:
    dcInverterGroupOutputApparentPower2.setUnits("1 VA")
_DcInverterGroupOutputApparentPower3_Type = Integer32
_DcInverterGroupOutputApparentPower3_Object = MibTableColumn
dcInverterGroupOutputApparentPower3 = _DcInverterGroupOutputApparentPower3_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 15, 1, 1, 21),
    _DcInverterGroupOutputApparentPower3_Type()
)
dcInverterGroupOutputApparentPower3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcInverterGroupOutputApparentPower3.setStatus("current")
if mibBuilder.loadTexts:
    dcInverterGroupOutputApparentPower3.setUnits("1 VA")
_DcInverterGroupOutputFrequency_Type = Gauge32
_DcInverterGroupOutputFrequency_Object = MibTableColumn
dcInverterGroupOutputFrequency = _DcInverterGroupOutputFrequency_Object(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 2, 15, 1, 1, 22),
    _DcInverterGroupOutputFrequency_Type()
)
dcInverterGroupOutputFrequency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcInverterGroupOutputFrequency.setStatus("current")
if mibBuilder.loadTexts:
    dcInverterGroupOutputFrequency.setUnits("10 mHz")
_ControllerEvents_ObjectIdentity = ObjectIdentity
controllerEvents = _ControllerEvents_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 3)
)
_ControllerEventObjects_ObjectIdentity = ObjectIdentity
controllerEventObjects = _ControllerEventObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 3, 1)
)
_ControllerEventsV2_ObjectIdentity = ObjectIdentity
controllerEventsV2 = _ControllerEventsV2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 3, 1, 0)
)

# Managed Objects groups

systemInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 1, 1, 1)
)
systemInfoGroup.setObjects(
      *(("ORION-BASE-MIB", "dcSiteName"),
        ("ORION-BASE-MIB", "dcSystemName"),
        ("ORION-BASE-MIB", "dcSystemDateTime"),
        ("ORION-BASE-MIB", "dcSoftwareVersion"),
        ("ORION-BASE-MIB", "dcCreateInventoryReport"))
)
if mibBuilder.loadTexts:
    systemInfoGroup.setStatus("current")

systemAlarmGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 1, 1, 2)
)
systemAlarmGroup.setObjects(
      *(("ORION-BASE-MIB", "dcNumberUrgentAlarms"),
        ("ORION-BASE-MIB", "dcNumberNonUrgentAlarms"),
        ("ORION-BASE-MIB", "dcMainsFailureAlarm"),
        ("ORION-BASE-MIB", "dcUrgentAlarmIdentifier"),
        ("ORION-BASE-MIB", "dcUrgentAlarmValue"),
        ("ORION-BASE-MIB", "dcNonUrgentAlarmIdentifier"),
        ("ORION-BASE-MIB", "dcNonUrgentAlarmValue"),
        ("ORION-BASE-MIB", "dcUrgentAlarmName"),
        ("ORION-BASE-MIB", "dcNonUrgentAlarmName"),
        ("ORION-BASE-MIB", "dcNumberCriticalAlarms"),
        ("ORION-BASE-MIB", "dcCriticalAlarmIdentifier"),
        ("ORION-BASE-MIB", "dcCriticalAlarmValue"),
        ("ORION-BASE-MIB", "dcCriticalAlarmName"),
        ("ORION-BASE-MIB", "dcNumberAllAlarms"),
        ("ORION-BASE-MIB", "dcAllAlarmIdentifier"),
        ("ORION-BASE-MIB", "dcAllAlarmValue"),
        ("ORION-BASE-MIB", "dcAllAlarmName"))
)
if mibBuilder.loadTexts:
    systemAlarmGroup.setStatus("current")

systemMonitorGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 1, 1, 3)
)
systemMonitorGroup.setObjects(
      *(("ORION-BASE-MIB", "dcSystemVoltage"),
        ("ORION-BASE-MIB", "dcLoadCurrent"),
        ("ORION-BASE-MIB", "dcBatteryCurrent"),
        ("ORION-BASE-MIB", "dcBatteryTemperature"),
        ("ORION-BASE-MIB", "dcChargeState"),
        ("ORION-BASE-MIB", "dcCurrentLimit"),
        ("ORION-BASE-MIB", "dcRectifierCurrent"),
        ("ORION-BASE-MIB", "dcSystemPower"))
)
if mibBuilder.loadTexts:
    systemMonitorGroup.setStatus("current")

rectifierGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 1, 1, 4)
)
rectifierGroup.setObjects(
      *(("ORION-BASE-MIB", "dcNumberRectifiers"),
        ("ORION-BASE-MIB", "dcNumberRectifiersFailure"),
        ("ORION-BASE-MIB", "dcNumberRectifiersOkay"),
        ("ORION-BASE-MIB", "dcEfficiencyCyclingEnabled"),
        ("ORION-BASE-MIB", "dcLimitSwitchingTimes"),
        ("ORION-BASE-MIB", "dcForceCyclingType"),
        ("ORION-BASE-MIB", "dcMinimumPowerReserve"),
        ("ORION-BASE-MIB", "dcMinimumRectifierPower"))
)
if mibBuilder.loadTexts:
    rectifierGroup.setStatus("current")

eventHistoryTableGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 1, 1, 5)
)
eventHistoryTableGroup.setObjects(
      *(("ORION-BASE-MIB", "dcEventHistoryTimestamp"),
        ("ORION-BASE-MIB", "dcEventHistoryMessage"))
)
if mibBuilder.loadTexts:
    eventHistoryTableGroup.setStatus("current")

alarmTableGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 1, 1, 6)
)
alarmTableGroup.setObjects(
      *(("ORION-BASE-MIB", "dcAlarmEventCategory"),
        ("ORION-BASE-MIB", "dcAlarmEventName"),
        ("ORION-BASE-MIB", "dcAlarmEventIdentifier"),
        ("ORION-BASE-MIB", "dcAlarmEventValue"))
)
if mibBuilder.loadTexts:
    alarmTableGroup.setStatus("current")

rectifierTableGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 1, 1, 7)
)
rectifierTableGroup.setObjects(
      *(("ORION-BASE-MIB", "dcRectifierIdentifier"),
        ("ORION-BASE-MIB", "dcRectifierSlotState"),
        ("ORION-BASE-MIB", "dcRectifierMainStatus"),
        ("ORION-BASE-MIB", "dcRectifierConfiguration"),
        ("ORION-BASE-MIB", "dcRectifierIout"),
        ("ORION-BASE-MIB", "dcRectifierPout"))
)
if mibBuilder.loadTexts:
    rectifierTableGroup.setStatus("current")

genericAlarmTableGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 1, 1, 9)
)
genericAlarmTableGroup.setObjects(
      *(("ORION-BASE-MIB", "dcGenericAlarmEventIdentifier"),
        ("ORION-BASE-MIB", "dcGenericAlarmEventName"),
        ("ORION-BASE-MIB", "dcGenericAlarmEventValue"))
)
if mibBuilder.loadTexts:
    genericAlarmTableGroup.setStatus("current")

batteryGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 1, 1, 10)
)
batteryGroup.setObjects(
      *(("ORION-BASE-MIB", "dcUsys20"),
        ("ORION-BASE-MIB", "dcTempCompType"),
        ("ORION-BASE-MIB", "dcSlope"),
        ("ORION-BASE-MIB", "dcStartTemp"),
        ("ORION-BASE-MIB", "dcStopTemp"),
        ("ORION-BASE-MIB", "dcMaxVoltage"),
        ("ORION-BASE-MIB", "dcLowStopVoltage"),
        ("ORION-BASE-MIB", "dcLowStartTemp"),
        ("ORION-BASE-MIB", "dcLowTempSlope"),
        ("ORION-BASE-MIB", "dcHighStartTemp"),
        ("ORION-BASE-MIB", "dcHighTempSlope"),
        ("ORION-BASE-MIB", "dcHighStopVoltage"),
        ("ORION-BASE-MIB", "dcRunawayTemp"),
        ("ORION-BASE-MIB", "dcRunawayVoltage"),
        ("ORION-BASE-MIB", "dcBatteryTestUsupport"),
        ("ORION-BASE-MIB", "dcBatteryTestDuration"),
        ("ORION-BASE-MIB", "dcBatteryTestInterval"),
        ("ORION-BASE-MIB", "dcBatteryTestDischargeCurrent"),
        ("ORION-BASE-MIB", "dcBatteryTestMinDuration"),
        ("ORION-BASE-MIB", "dcBatteryTestVoltageWithinUfloat"),
        ("ORION-BASE-MIB", "dcBatteryTestVoltageWithinUfloatPeriod"),
        ("ORION-BASE-MIB", "dcBatteryTestTempFrom"),
        ("ORION-BASE-MIB", "dcBatteryTestTempTo"),
        ("ORION-BASE-MIB", "dcBatteryTestIntervalEnabled"),
        ("ORION-BASE-MIB", "dcBatteryTestStartTimeFrom"),
        ("ORION-BASE-MIB", "dcBatteryTestStartTimeTo"),
        ("ORION-BASE-MIB", "dcBatteryTestDateTime"),
        ("ORION-BASE-MIB", "dcBatteryTestResult"),
        ("ORION-BASE-MIB", "dcBatteryTestEndVoltage"),
        ("ORION-BASE-MIB", "dcBatteryTestControl"),
        ("ORION-BASE-MIB", "dcBatteryTestStatus"),
        ("ORION-BASE-MIB", "dcBatteryTestFailureEvent"),
        ("ORION-BASE-MIB", "dcBatteryTestType"),
        ("ORION-BASE-MIB", "dcTotalBatteryCapacity"),
        ("ORION-BASE-MIB", "dcBatteryLifePredictionStatus"),
        ("ORION-BASE-MIB", "dcBatteryChargingCurrentLimitEnable"),
        ("ORION-BASE-MIB", "dcBatteryTotalChargingCurrentLimitEnable"),
        ("ORION-BASE-MIB", "dcBatteryTotalMaxIBatt"),
        ("ORION-BASE-MIB", "dcLossOfBackupTimeEnabled"),
        ("ORION-BASE-MIB", "dcLossOfBackupTimeStatus"),
        ("ORION-BASE-MIB", "dcExpectedBackupTime"),
        ("ORION-BASE-MIB", "dcEqualizeControl"),
        ("ORION-BASE-MIB", "dcEqualizeStatus"),
        ("ORION-BASE-MIB", "dcEqualizeEnabled"),
        ("ORION-BASE-MIB", "dcEqualizeVoltage"),
        ("ORION-BASE-MIB", "dcEqualizeDuration"),
        ("ORION-BASE-MIB", "dcEqualizeUseBattRoomFanEnabled"),
        ("ORION-BASE-MIB", "dcEqualizeLeadTime"),
        ("ORION-BASE-MIB", "dcEqualizeTimeLag"),
        ("ORION-BASE-MIB", "dcEqualizeInterval"),
        ("ORION-BASE-MIB", "dcEqualizeStartTimeIntervalFrom"),
        ("ORION-BASE-MIB", "dcEqualizeStartTimeIntervalTo"),
        ("ORION-BASE-MIB", "dcEqualizeInhibitAfterBoost"),
        ("ORION-BASE-MIB", "dcBoostChargeControl"),
        ("ORION-BASE-MIB", "dcBoostChargeStatus"),
        ("ORION-BASE-MIB", "dcBoostChargeType"),
        ("ORION-BASE-MIB", "dcBoostChargeVoltage"),
        ("ORION-BASE-MIB", "dcBoostChargeMaxDuration"),
        ("ORION-BASE-MIB", "dcBoostChargeUseBattRoomFanEnabled"),
        ("ORION-BASE-MIB", "dcBoostChargeTimeLag"),
        ("ORION-BASE-MIB", "dcBoostChargeIstart"),
        ("ORION-BASE-MIB", "dcBoostChargeIstop"),
        ("ORION-BASE-MIB", "dcBoostChargeInhibitTime"),
        ("ORION-BASE-MIB", "dcBoostChargeSoCBelow"),
        ("ORION-BASE-MIB", "dcUaMax"),
        ("ORION-BASE-MIB", "dcUaMin"),
        ("ORION-BASE-MIB", "dcUsMax"),
        ("ORION-BASE-MIB", "dcUsMin"),
        ("ORION-BASE-MIB", "dcBoD"),
        ("ORION-BASE-MIB", "dcHysteresis"),
        ("ORION-BASE-MIB", "dcSuppressUaLowEnabled"),
        ("ORION-BASE-MIB", "dcSuppressUsLowEnabled"),
        ("ORION-BASE-MIB", "dcEnableUsTempComp"),
        ("ORION-BASE-MIB", "dcEvtCtrlChargeStatus"),
        ("ORION-BASE-MIB", "dcEvtCtrlChargeType"),
        ("ORION-BASE-MIB", "dcEvtCtrlChargeVoltage"),
        ("ORION-BASE-MIB", "dcEvtCtrlChargeTempCompEnabled"),
        ("ORION-BASE-MIB", "dcEvtCtrlChargeMaxIBatt"),
        ("ORION-BASE-MIB", "dcHighTemp"),
        ("ORION-BASE-MIB", "dcHighTempHyst"),
        ("ORION-BASE-MIB", "dcBatteryTypeSelect"))
)
if mibBuilder.loadTexts:
    batteryGroup.setStatus("current")

controlEventTableGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 1, 1, 11)
)
controlEventTableGroup.setObjects(
      *(("ORION-BASE-MIB", "dcControlEventName"),
        ("ORION-BASE-MIB", "dcControlEventIdentifier"),
        ("ORION-BASE-MIB", "dcControlEventValue"))
)
if mibBuilder.loadTexts:
    controlEventTableGroup.setStatus("current")

trapDestinationTableGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 1, 1, 12)
)
trapDestinationTableGroup.setObjects(
      *(("ORION-BASE-MIB", "dcTrapDestinationIp"),
        ("ORION-BASE-MIB", "dcTrapDestinationPort"),
        ("ORION-BASE-MIB", "dcTrapDestinationUser"))
)
if mibBuilder.loadTexts:
    trapDestinationTableGroup.setStatus("current")

miscGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 1, 1, 13)
)
miscGroup.setObjects(
      *(("ORION-BASE-MIB", "dcFileProcessingStatus"),
        ("ORION-BASE-MIB", "dcResendActiveAlarmTraps"),
        ("ORION-BASE-MIB", "dcRebootController"))
)
if mibBuilder.loadTexts:
    miscGroup.setStatus("current")

rectifierGroupTableGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 1, 1, 14)
)
rectifierGroupTableGroup.setObjects(
      *(("ORION-BASE-MIB", "dcRectifierGroupName"),
        ("ORION-BASE-MIB", "dcRectifierGroupRectifierType"),
        ("ORION-BASE-MIB", "dcRectifierGroupDefaultVoltage"),
        ("ORION-BASE-MIB", "dcRectifierGroupDefaultCurrentLimit"),
        ("ORION-BASE-MIB", "dcRectifierGroupDefaultPowerLimit"),
        ("ORION-BASE-MIB", "dcRectifierGroupInputLowOff"),
        ("ORION-BASE-MIB", "dcRectifierGroupInputLowOn"),
        ("ORION-BASE-MIB", "dcRectifierGroupStartupVoltage"),
        ("ORION-BASE-MIB", "dcRectifierGroupStartupCurrentLimit"),
        ("ORION-BASE-MIB", "dcRectifierGroupStartupPowerLimit"),
        ("ORION-BASE-MIB", "dcRectifierGroupStartupLimitTime"),
        ("ORION-BASE-MIB", "dcRectifierGroupPowerupDelay"),
        ("ORION-BASE-MIB", "dcRectifierGroupPowerupTime"),
        ("ORION-BASE-MIB", "dcRectifierGroupUmaxOff"))
)
if mibBuilder.loadTexts:
    rectifierGroupTableGroup.setStatus("current")

batteryStringTableGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 1, 1, 15)
)
batteryStringTableGroup.setObjects(
      *(("ORION-BASE-MIB", "dcBatteryStringName"),
        ("ORION-BASE-MIB", "dcBatteryStringMaxIBatt"),
        ("ORION-BASE-MIB", "dcBatteryStringCapacity"))
)
if mibBuilder.loadTexts:
    batteryStringTableGroup.setStatus("current")

defaultLogEventTableGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 1, 1, 16)
)
defaultLogEventTableGroup.setObjects(
      *(("ORION-BASE-MIB", "dcDefaultLogEventName"),
        ("ORION-BASE-MIB", "dcDefaultLogEventLogged"))
)
if mibBuilder.loadTexts:
    defaultLogEventTableGroup.setStatus("current")

eventProcessingEventTableGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 1, 1, 17)
)
eventProcessingEventTableGroup.setObjects(
      *(("ORION-BASE-MIB", "dcEventProcessingEventName"),
        ("ORION-BASE-MIB", "dcEventProcessingEventAssigned"),
        ("ORION-BASE-MIB", "dcEventProcessingEventType"),
        ("ORION-BASE-MIB", "dcEventProcessingEventSelected"))
)
if mibBuilder.loadTexts:
    eventProcessingEventTableGroup.setStatus("current")

lvdTableGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 1, 1, 18)
)
lvdTableGroup.setObjects(
      *(("ORION-BASE-MIB", "dcLvdName"),
        ("ORION-BASE-MIB", "dcLvdDisconnectDelay"),
        ("ORION-BASE-MIB", "dcLvdType"),
        ("ORION-BASE-MIB", "dcLvdVoltageThreshold"),
        ("ORION-BASE-MIB", "dcLvdVoltageHysteresis"),
        ("ORION-BASE-MIB", "dcLvdControlEvent"),
        ("ORION-BASE-MIB", "dcLvdMonitoringEvent"))
)
if mibBuilder.loadTexts:
    lvdTableGroup.setStatus("current")

powerLimitationTableGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 1, 1, 19)
)
powerLimitationTableGroup.setObjects(
      *(("ORION-BASE-MIB", "dcPowerLimitationEventName"),
        ("ORION-BASE-MIB", "dcPowerLimitationStatus"),
        ("ORION-BASE-MIB", "dcPowerLimitationType"),
        ("ORION-BASE-MIB", "dcMaxTotalRectifierPower"),
        ("ORION-BASE-MIB", "dcPowerLimitationNoBatteryDischarge"))
)
if mibBuilder.loadTexts:
    powerLimitationTableGroup.setStatus("current")

measurementTableGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 1, 1, 20)
)
measurementTableGroup.setObjects(
      *(("ORION-BASE-MIB", "dcMeasurementName"),
        ("ORION-BASE-MIB", "dcMeasurementValue"),
        ("ORION-BASE-MIB", "dcMeasurementScaleFactor"),
        ("ORION-BASE-MIB", "dcMeasurementUnit"))
)
if mibBuilder.loadTexts:
    measurementTableGroup.setStatus("current")

meterPanelEventTableGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 1, 1, 21)
)
meterPanelEventTableGroup.setObjects(
      *(("ORION-BASE-MIB", "dcMeterPanelEventName"),
        ("ORION-BASE-MIB", "dcMeterPanelEventValue"),
        ("ORION-BASE-MIB", "dcMeterPanelEventHourMeterValue"))
)
if mibBuilder.loadTexts:
    meterPanelEventTableGroup.setStatus("current")

meterPanelmeasurementTableGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 1, 1, 22)
)
meterPanelmeasurementTableGroup.setObjects(
      *(("ORION-BASE-MIB", "dcMeterPanelMeasurementName"),
        ("ORION-BASE-MIB", "dcMeterPanelMeasurementValue"),
        ("ORION-BASE-MIB", "dcMeterPanelMeasurementUnit"))
)
if mibBuilder.loadTexts:
    meterPanelmeasurementTableGroup.setStatus("current")

batteryLithiumTableGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 1, 1, 23)
)
batteryLithiumTableGroup.setObjects(
      *(("ORION-BASE-MIB", "dcBatteryLithiumName"),
        ("ORION-BASE-MIB", "dcBatteryLithiumMainState"),
        ("ORION-BASE-MIB", "dcBatteryLithiumSubState"),
        ("ORION-BASE-MIB", "dcBatteryLithiumCurrent"),
        ("ORION-BASE-MIB", "dcBatteryLithiumStateOfCharge"),
        ("ORION-BASE-MIB", "dcBatteryLithiumInstallationDate"),
        ("ORION-BASE-MIB", "dcBatteryLithiumSoH"))
)
if mibBuilder.loadTexts:
    batteryLithiumTableGroup.setStatus("current")

batteryLifePredictionTableGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 1, 1, 24)
)
batteryLifePredictionTableGroup.setObjects(
      *(("ORION-BASE-MIB", "dcBatteryLifePredictionName"),
        ("ORION-BASE-MIB", "dcBatteryLifePredictionRemainingDays"),
        ("ORION-BASE-MIB", "dcBatteryLifePredictionInstallationDate"),
        ("ORION-BASE-MIB", "dcBatteryLifePredictionSoH"))
)
if mibBuilder.loadTexts:
    batteryLifePredictionTableGroup.setStatus("current")

pvcGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 1, 1, 25)
)
pvcGroup.setObjects(
      *(("ORION-BASE-MIB", "dcNumberPVCs"),
        ("ORION-BASE-MIB", "dcNumberPVCsFailure"),
        ("ORION-BASE-MIB", "dcNumberPVCsOkay"))
)
if mibBuilder.loadTexts:
    pvcGroup.setStatus("current")

pvcTableGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 1, 1, 26)
)
pvcTableGroup.setObjects(
      *(("ORION-BASE-MIB", "dcPVCIdentifier"),
        ("ORION-BASE-MIB", "dcPVCSlotState"),
        ("ORION-BASE-MIB", "dcPVCMainStatus"),
        ("ORION-BASE-MIB", "dcPVCSubStatus"),
        ("ORION-BASE-MIB", "dcPVCConfiguration"),
        ("ORION-BASE-MIB", "dcPVCIout"),
        ("ORION-BASE-MIB", "dcPVCUout"),
        ("ORION-BASE-MIB", "dcPVCIin"),
        ("ORION-BASE-MIB", "dcPVCUin"))
)
if mibBuilder.loadTexts:
    pvcTableGroup.setStatus("current")

pvcGroupTableGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 1, 1, 27)
)
pvcGroupTableGroup.setObjects(
      *(("ORION-BASE-MIB", "dcPVCGroupPVCType"),
        ("ORION-BASE-MIB", "dcPVCGroupVoltage"),
        ("ORION-BASE-MIB", "dcPVCGroupVPGM"),
        ("ORION-BASE-MIB", "dcPVCGroupInputLowOff"),
        ("ORION-BASE-MIB", "dcPVCGroupInputLowOn"),
        ("ORION-BASE-MIB", "dcPVCGroupStartUpDelay"),
        ("ORION-BASE-MIB", "dcPVCGroupOvpLimit"),
        ("ORION-BASE-MIB", "dcPVCGroupAlarmDelay"))
)
if mibBuilder.loadTexts:
    pvcGroupTableGroup.setStatus("current")

inventoryTableGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 1, 1, 28)
)
inventoryTableGroup.setObjects(
      *(("ORION-BASE-MIB", "dcInventoryType"),
        ("ORION-BASE-MIB", "dcInventoryName"),
        ("ORION-BASE-MIB", "dcInventorySwVersion"),
        ("ORION-BASE-MIB", "dcInventoryBuildVersion"),
        ("ORION-BASE-MIB", "dcInventoryPartNb"),
        ("ORION-BASE-MIB", "dcInventorySerialNb"),
        ("ORION-BASE-MIB", "dcInventoryTopLevel"))
)
if mibBuilder.loadTexts:
    inventoryTableGroup.setStatus("current")

eventDefinitionTableGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 1, 1, 29)
)
eventDefinitionTableGroup.setObjects(
      *(("ORION-BASE-MIB", "dcEventName"),
        ("ORION-BASE-MIB", "dcThreshold"),
        ("ORION-BASE-MIB", "dcThresholdHysteresis"),
        ("ORION-BASE-MIB", "dcUnit"))
)
if mibBuilder.loadTexts:
    eventDefinitionTableGroup.setStatus("current")

filterTableGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 1, 1, 30)
)
filterTableGroup.setObjects(
      *(("ORION-BASE-MIB", "dcFilterName"),
        ("ORION-BASE-MIB", "dcTrueForMin"),
        ("ORION-BASE-MIB", "dcFalseForMin"))
)
if mibBuilder.loadTexts:
    filterTableGroup.setStatus("current")

timerTableGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 1, 1, 31)
)
timerTableGroup.setObjects(
      *(("ORION-BASE-MIB", "dcTimerName"),
        ("ORION-BASE-MIB", "dcStartTime"),
        ("ORION-BASE-MIB", "dcStartDaySu"),
        ("ORION-BASE-MIB", "dcStartDayMo"),
        ("ORION-BASE-MIB", "dcStartDayTu"),
        ("ORION-BASE-MIB", "dcStartDayWe"),
        ("ORION-BASE-MIB", "dcStartDayTh"),
        ("ORION-BASE-MIB", "dcStartDayFr"),
        ("ORION-BASE-MIB", "dcStartDaySa"),
        ("ORION-BASE-MIB", "dcEndTime"),
        ("ORION-BASE-MIB", "dcEndDaySu"),
        ("ORION-BASE-MIB", "dcEndDayMo"),
        ("ORION-BASE-MIB", "dcEndDayTu"),
        ("ORION-BASE-MIB", "dcEndDayWe"),
        ("ORION-BASE-MIB", "dcEndDayTh"),
        ("ORION-BASE-MIB", "dcEndDayFr"),
        ("ORION-BASE-MIB", "dcEndDaySa"))
)
if mibBuilder.loadTexts:
    timerTableGroup.setStatus("current")

ipGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 1, 1, 32)
)
ipGroup.setObjects(
      *(("ORION-BASE-MIB", "dcIPv4Address"),
        ("ORION-BASE-MIB", "dcIPv4SubnetMask"),
        ("ORION-BASE-MIB", "dcIPv4Gateway"),
        ("ORION-BASE-MIB", "dcIPv4DNS"),
        ("ORION-BASE-MIB", "dcIPv6LinkLocalAddress"),
        ("ORION-BASE-MIB", "dcIPv6Address"),
        ("ORION-BASE-MIB", "dcIPv6Gateway"),
        ("ORION-BASE-MIB", "dcIPv6DNSAuto"),
        ("ORION-BASE-MIB", "dcIPv6DNSManual"))
)
if mibBuilder.loadTexts:
    ipGroup.setStatus("current")

newTrapDestinationTableGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 1, 1, 33)
)
newTrapDestinationTableGroup.setObjects(
      *(("ORION-BASE-MIB", "dcTrapDestinationv2"),
        ("ORION-BASE-MIB", "dcTrapDestinationv2Port"),
        ("ORION-BASE-MIB", "dcTrapDestinationv2User"))
)
if mibBuilder.loadTexts:
    newTrapDestinationTableGroup.setStatus("current")

airconTableGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 1, 1, 34)
)
airconTableGroup.setObjects(
      *(("ORION-BASE-MIB", "dcAirconName"),
        ("ORION-BASE-MIB", "dcAirconMainStatus"),
        ("ORION-BASE-MIB", "dcAirconSubStatus"),
        ("ORION-BASE-MIB", "dcAirconConfiguration"),
        ("ORION-BASE-MIB", "dcAirconPlanName"),
        ("ORION-BASE-MIB", "dcAirconRoomTemp"),
        ("ORION-BASE-MIB", "dcCoolingPlanActivationInput"),
        ("ORION-BASE-MIB", "dcCoolingPlanPriority"),
        ("ORION-BASE-MIB", "dcCoolingPlanStatus"),
        ("ORION-BASE-MIB", "dcCoolingPlanTargetTemp"),
        ("ORION-BASE-MIB", "dcCoolingPlanOperatingMode"),
        ("ORION-BASE-MIB", "dcCoolingPlanStandbyFanSpeed"),
        ("ORION-BASE-MIB", "dcCoolingPlanHeaterStartTemp"),
        ("ORION-BASE-MIB", "dcCoolingPlanHeaterHyst"),
        ("ORION-BASE-MIB", "dcCoolingPlanHeaterControl"))
)
if mibBuilder.loadTexts:
    airconTableGroup.setStatus("current")

inverterGroupTableGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 1, 1, 35)
)
inverterGroupTableGroup.setObjects(
      *(("ORION-BASE-MIB", "dcInverterGroupLoadPosition"),
        ("ORION-BASE-MIB", "dcInverterGroupNbrOfConfigInverters"),
        ("ORION-BASE-MIB", "dcInverterGroupNbrOfPresentInverters"),
        ("ORION-BASE-MIB", "dcInverterGroupState"),
        ("ORION-BASE-MIB", "dcInverterGroupPhase"),
        ("ORION-BASE-MIB", "dcInverterGroupOutputVoltage1"),
        ("ORION-BASE-MIB", "dcInverterGroupOutputVoltage2"),
        ("ORION-BASE-MIB", "dcInverterGroupOutputVoltage3"),
        ("ORION-BASE-MIB", "dcInverterGroupOutputApparentPower1"),
        ("ORION-BASE-MIB", "dcInverterGroupOutputApparentPower2"),
        ("ORION-BASE-MIB", "dcInverterGroupOutputApparentPower3"),
        ("ORION-BASE-MIB", "dcInverterGroupOutputFrequency"),
        ("ORION-BASE-MIB", "dcInverterGroupInputVoltage1"),
        ("ORION-BASE-MIB", "dcInverterGroupInputVoltage2"),
        ("ORION-BASE-MIB", "dcInverterGroupInputVoltage3"),
        ("ORION-BASE-MIB", "dcInverterGroupInputApparentPower1"),
        ("ORION-BASE-MIB", "dcInverterGroupInputApparentPower2"),
        ("ORION-BASE-MIB", "dcInverterGroupInputApparentPower3"),
        ("ORION-BASE-MIB", "dcInverterGroupInputFrequency"),
        ("ORION-BASE-MIB", "dcInverterGroupDcVoltage"),
        ("ORION-BASE-MIB", "dcInverterGroupInputDcPower"))
)
if mibBuilder.loadTexts:
    inverterGroupTableGroup.setStatus("current")

eventCtrlChargeTableTableGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 1, 1, 36)
)
eventCtrlChargeTableTableGroup.setObjects(
      *(("ORION-BASE-MIB", "dcEventControlledChargeTablePriority"),
        ("ORION-BASE-MIB", "dcEventControlledChargeTableName"),
        ("ORION-BASE-MIB", "dcEventControlledChargeTableActivationInput"),
        ("ORION-BASE-MIB", "dcEventControlledChargeTableStatus"),
        ("ORION-BASE-MIB", "dcEventControlledChargeTableType"),
        ("ORION-BASE-MIB", "dcEventControlledChargeTableVoltage"),
        ("ORION-BASE-MIB", "dcEventControlledChargeTableMaxIBatt"),
        ("ORION-BASE-MIB", "dcEventControlledChargeTableTempCompEnabled"))
)
if mibBuilder.loadTexts:
    eventCtrlChargeTableTableGroup.setStatus("current")

batteryTestTableTableGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 1, 1, 37)
)
batteryTestTableTableGroup.setObjects(
      *(("ORION-BASE-MIB", "dcBatteryTestTablePriority"),
        ("ORION-BASE-MIB", "dcBatteryTestTableName"),
        ("ORION-BASE-MIB", "dcBatteryTestTableType"),
        ("ORION-BASE-MIB", "dcBatteryTestTableStatus"),
        ("ORION-BASE-MIB", "dcBatteryTestTableUsupport"),
        ("ORION-BASE-MIB", "dcBatteryTestTableDuration"),
        ("ORION-BASE-MIB", "dcBatteryTestTableInterval"),
        ("ORION-BASE-MIB", "dcBatteryTestTableDischargeCurrent"),
        ("ORION-BASE-MIB", "dcBatteryTestTableMinDuration"),
        ("ORION-BASE-MIB", "dcBatteryTestTableVoltageWithinUfloat"),
        ("ORION-BASE-MIB", "dcBatteryTestTableVoltageWithinUfloatPeriod"),
        ("ORION-BASE-MIB", "dcBatteryTestTableTempFrom"),
        ("ORION-BASE-MIB", "dcBatteryTestTableTempTo"),
        ("ORION-BASE-MIB", "dcBatteryTestTableIntervalEnabled"),
        ("ORION-BASE-MIB", "dcBatteryTestTableStartTimeFrom"),
        ("ORION-BASE-MIB", "dcBatteryTestTableStartTimeTo"),
        ("ORION-BASE-MIB", "dcBatteryTestTableControl"),
        ("ORION-BASE-MIB", "dcBatteryTestTableFailureEvent"))
)
if mibBuilder.loadTexts:
    batteryTestTableTableGroup.setStatus("current")

batteryTestResultTableTableGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 1, 1, 38)
)
batteryTestResultTableTableGroup.setObjects(
      *(("ORION-BASE-MIB", "dcBatteryTestResultTablePriority"),
        ("ORION-BASE-MIB", "dcBatteryTestResultTableName"),
        ("ORION-BASE-MIB", "dcBatteryTestResultTableDateTime"),
        ("ORION-BASE-MIB", "dcBatteryTestResultTableResult"),
        ("ORION-BASE-MIB", "dcBatteryTestResultTableEndVoltage"))
)
if mibBuilder.loadTexts:
    batteryTestResultTableTableGroup.setStatus("current")


# Notification objects

systemNonUrgentAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 3, 1, 0, 1)
)
systemNonUrgentAlarm.setObjects(
      *(("ORION-BASE-MIB", "dcSiteName"),
        ("ORION-BASE-MIB", "dcSystemName"),
        ("ORION-BASE-MIB", "dcSystemDateTime"),
        ("ORION-BASE-MIB", "dcNumberNonUrgentAlarms"),
        ("ORION-BASE-MIB", "dcNonUrgentAlarmIdentifier"),
        ("ORION-BASE-MIB", "dcNonUrgentAlarmValue"),
        ("ORION-BASE-MIB", "dcNonUrgentAlarmName"))
)
if mibBuilder.loadTexts:
    systemNonUrgentAlarm.setStatus(
        "current"
    )

systemUrgentAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 3, 1, 0, 2)
)
systemUrgentAlarm.setObjects(
      *(("ORION-BASE-MIB", "dcSiteName"),
        ("ORION-BASE-MIB", "dcSystemName"),
        ("ORION-BASE-MIB", "dcSystemDateTime"),
        ("ORION-BASE-MIB", "dcNumberUrgentAlarms"),
        ("ORION-BASE-MIB", "dcUrgentAlarmIdentifier"),
        ("ORION-BASE-MIB", "dcUrgentAlarmValue"),
        ("ORION-BASE-MIB", "dcUrgentAlarmName"))
)
if mibBuilder.loadTexts:
    systemUrgentAlarm.setStatus(
        "current"
    )

systemCriticalAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 3, 1, 0, 3)
)
systemCriticalAlarm.setObjects(
      *(("ORION-BASE-MIB", "dcSiteName"),
        ("ORION-BASE-MIB", "dcSystemName"),
        ("ORION-BASE-MIB", "dcSystemDateTime"),
        ("ORION-BASE-MIB", "dcNumberCriticalAlarms"),
        ("ORION-BASE-MIB", "dcCriticalAlarmIdentifier"),
        ("ORION-BASE-MIB", "dcCriticalAlarmValue"),
        ("ORION-BASE-MIB", "dcCriticalAlarmName"))
)
if mibBuilder.loadTexts:
    systemCriticalAlarm.setStatus(
        "current"
    )

systemAllAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 3, 1, 0, 4)
)
systemAllAlarm.setObjects(
      *(("ORION-BASE-MIB", "dcSiteName"),
        ("ORION-BASE-MIB", "dcSystemName"),
        ("ORION-BASE-MIB", "dcSystemDateTime"),
        ("ORION-BASE-MIB", "dcNumberAllAlarms"),
        ("ORION-BASE-MIB", "dcAllAlarmIdentifier"),
        ("ORION-BASE-MIB", "dcAllAlarmValue"),
        ("ORION-BASE-MIB", "dcAllAlarmName"))
)
if mibBuilder.loadTexts:
    systemAllAlarm.setStatus(
        "current"
    )


# Notifications groups

notificationsGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 1, 1, 8)
)
notificationsGroup.setObjects(
      *(("ORION-BASE-MIB", "systemNonUrgentAlarm"),
        ("ORION-BASE-MIB", "systemUrgentAlarm"),
        ("ORION-BASE-MIB", "systemCriticalAlarm"),
        ("ORION-BASE-MIB", "systemAllAlarm"))
)
if mibBuilder.loadTexts:
    notificationsGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

controllerBasicCompl = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 20246, 2, 3, 1, 1, 1, 1, 2, 1)
)
controllerBasicCompl.setObjects(
      *(("ORION-BASE-MIB", "systemInfoGroup"),
        ("ORION-BASE-MIB", "systemAlarmGroup"),
        ("ORION-BASE-MIB", "systemMonitorGroup"),
        ("ORION-BASE-MIB", "alarmTableGroup"),
        ("ORION-BASE-MIB", "notificationsGroup"))
)
if mibBuilder.loadTexts:
    controllerBasicCompl.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ORION-BASE-MIB",
    **{"orionBaseMibModule": orionBaseMibModule,
       "orionBaseMib": orionBaseMib,
       "controllerConfs": controllerConfs,
       "controllerGroups": controllerGroups,
       "systemInfoGroup": systemInfoGroup,
       "systemAlarmGroup": systemAlarmGroup,
       "systemMonitorGroup": systemMonitorGroup,
       "rectifierGroup": rectifierGroup,
       "eventHistoryTableGroup": eventHistoryTableGroup,
       "alarmTableGroup": alarmTableGroup,
       "rectifierTableGroup": rectifierTableGroup,
       "notificationsGroup": notificationsGroup,
       "genericAlarmTableGroup": genericAlarmTableGroup,
       "batteryGroup": batteryGroup,
       "controlEventTableGroup": controlEventTableGroup,
       "trapDestinationTableGroup": trapDestinationTableGroup,
       "miscGroup": miscGroup,
       "rectifierGroupTableGroup": rectifierGroupTableGroup,
       "batteryStringTableGroup": batteryStringTableGroup,
       "defaultLogEventTableGroup": defaultLogEventTableGroup,
       "eventProcessingEventTableGroup": eventProcessingEventTableGroup,
       "lvdTableGroup": lvdTableGroup,
       "powerLimitationTableGroup": powerLimitationTableGroup,
       "measurementTableGroup": measurementTableGroup,
       "meterPanelEventTableGroup": meterPanelEventTableGroup,
       "meterPanelmeasurementTableGroup": meterPanelmeasurementTableGroup,
       "batteryLithiumTableGroup": batteryLithiumTableGroup,
       "batteryLifePredictionTableGroup": batteryLifePredictionTableGroup,
       "pvcGroup": pvcGroup,
       "pvcTableGroup": pvcTableGroup,
       "pvcGroupTableGroup": pvcGroupTableGroup,
       "inventoryTableGroup": inventoryTableGroup,
       "eventDefinitionTableGroup": eventDefinitionTableGroup,
       "filterTableGroup": filterTableGroup,
       "timerTableGroup": timerTableGroup,
       "ipGroup": ipGroup,
       "newTrapDestinationTableGroup": newTrapDestinationTableGroup,
       "airconTableGroup": airconTableGroup,
       "inverterGroupTableGroup": inverterGroupTableGroup,
       "eventCtrlChargeTableTableGroup": eventCtrlChargeTableTableGroup,
       "batteryTestTableTableGroup": batteryTestTableTableGroup,
       "batteryTestResultTableTableGroup": batteryTestResultTableTableGroup,
       "controllerCompl": controllerCompl,
       "controllerBasicCompl": controllerBasicCompl,
       "controllerObjects": controllerObjects,
       "dcSystemInfo": dcSystemInfo,
       "dcSiteName": dcSiteName,
       "dcSystemName": dcSystemName,
       "dcSystemDateTime": dcSystemDateTime,
       "dcSoftwareVersion": dcSoftwareVersion,
       "dcCreateInventoryReport": dcCreateInventoryReport,
       "dcSystemAlarms": dcSystemAlarms,
       "dcEventHistoryTable": dcEventHistoryTable,
       "dcEventHistoryEntry": dcEventHistoryEntry,
       "dcEventHistoryIndex": dcEventHistoryIndex,
       "dcEventHistoryTimestamp": dcEventHistoryTimestamp,
       "dcEventHistoryMessage": dcEventHistoryMessage,
       "dcAlarmTable": dcAlarmTable,
       "dcAlarmEntry": dcAlarmEntry,
       "dcAlarmIndex": dcAlarmIndex,
       "dcAlarmEventCategory": dcAlarmEventCategory,
       "dcAlarmEventName": dcAlarmEventName,
       "dcAlarmEventIdentifier": dcAlarmEventIdentifier,
       "dcAlarmEventValue": dcAlarmEventValue,
       "dcNumberUrgentAlarms": dcNumberUrgentAlarms,
       "dcNumberNonUrgentAlarms": dcNumberNonUrgentAlarms,
       "dcMainsFailureAlarm": dcMainsFailureAlarm,
       "dcUrgentAlarmIdentifier": dcUrgentAlarmIdentifier,
       "dcUrgentAlarmValue": dcUrgentAlarmValue,
       "dcNonUrgentAlarmIdentifier": dcNonUrgentAlarmIdentifier,
       "dcNonUrgentAlarmValue": dcNonUrgentAlarmValue,
       "dcUrgentAlarmName": dcUrgentAlarmName,
       "dcNonUrgentAlarmName": dcNonUrgentAlarmName,
       "dcGenericAlarmTable": dcGenericAlarmTable,
       "dcGenericAlarmEntry": dcGenericAlarmEntry,
       "dcGenericAlarmIndex": dcGenericAlarmIndex,
       "dcGenericAlarmEventName": dcGenericAlarmEventName,
       "dcGenericAlarmEventIdentifier": dcGenericAlarmEventIdentifier,
       "dcGenericAlarmEventValue": dcGenericAlarmEventValue,
       "dcNumberCriticalAlarms": dcNumberCriticalAlarms,
       "dcCriticalAlarmIdentifier": dcCriticalAlarmIdentifier,
       "dcCriticalAlarmValue": dcCriticalAlarmValue,
       "dcCriticalAlarmName": dcCriticalAlarmName,
       "dcNumberAllAlarms": dcNumberAllAlarms,
       "dcAllAlarmIdentifier": dcAllAlarmIdentifier,
       "dcAllAlarmValue": dcAllAlarmValue,
       "dcAllAlarmName": dcAllAlarmName,
       "dcSystemMonitor": dcSystemMonitor,
       "dcSystemVoltage": dcSystemVoltage,
       "dcLoadCurrent": dcLoadCurrent,
       "dcBatteryCurrent": dcBatteryCurrent,
       "dcBatteryTemperature": dcBatteryTemperature,
       "dcChargeState": dcChargeState,
       "dcCurrentLimit": dcCurrentLimit,
       "dcRectifierCurrent": dcRectifierCurrent,
       "dcSystemPower": dcSystemPower,
       "dcRectifier": dcRectifier,
       "dcNumberRectifiers": dcNumberRectifiers,
       "dcNumberRectifiersFailure": dcNumberRectifiersFailure,
       "dcNumberRectifiersOkay": dcNumberRectifiersOkay,
       "dcRectifierTable": dcRectifierTable,
       "dcRectifierEntry": dcRectifierEntry,
       "dcRectifierIndex": dcRectifierIndex,
       "dcRectifierIdentifier": dcRectifierIdentifier,
       "dcRectifierSlotState": dcRectifierSlotState,
       "dcRectifierMainStatus": dcRectifierMainStatus,
       "dcRectifierConfiguration": dcRectifierConfiguration,
       "dcRectifierIout": dcRectifierIout,
       "dcRectifierPout": dcRectifierPout,
       "dcRectifierGroupTable": dcRectifierGroupTable,
       "dcRectifierGroupEntry": dcRectifierGroupEntry,
       "dcRectifierGroupIndex": dcRectifierGroupIndex,
       "dcRectifierGroupName": dcRectifierGroupName,
       "dcRectifierGroupRectifierType": dcRectifierGroupRectifierType,
       "dcRectifierGroupDefaultVoltage": dcRectifierGroupDefaultVoltage,
       "dcRectifierGroupDefaultCurrentLimit": dcRectifierGroupDefaultCurrentLimit,
       "dcRectifierGroupDefaultPowerLimit": dcRectifierGroupDefaultPowerLimit,
       "dcRectifierGroupInputLowOff": dcRectifierGroupInputLowOff,
       "dcRectifierGroupInputLowOn": dcRectifierGroupInputLowOn,
       "dcRectifierGroupStartupVoltage": dcRectifierGroupStartupVoltage,
       "dcRectifierGroupStartupCurrentLimit": dcRectifierGroupStartupCurrentLimit,
       "dcRectifierGroupStartupPowerLimit": dcRectifierGroupStartupPowerLimit,
       "dcRectifierGroupStartupLimitTime": dcRectifierGroupStartupLimitTime,
       "dcRectifierGroupPowerupDelay": dcRectifierGroupPowerupDelay,
       "dcRectifierGroupPowerupTime": dcRectifierGroupPowerupTime,
       "dcRectifierGroupUmaxOff": dcRectifierGroupUmaxOff,
       "dcRectifierFunctions": dcRectifierFunctions,
       "dcEfficiencyCycling": dcEfficiencyCycling,
       "dcEfficiencyCyclingEnabled": dcEfficiencyCyclingEnabled,
       "dcLimitSwitchingTimes": dcLimitSwitchingTimes,
       "dcForceCyclingType": dcForceCyclingType,
       "dcMinimumPowerReserve": dcMinimumPowerReserve,
       "dcMinimumRectifierPower": dcMinimumRectifierPower,
       "dcPowerLimitation": dcPowerLimitation,
       "dcPowerLimitationTable": dcPowerLimitationTable,
       "dcPowerLimitationEntry": dcPowerLimitationEntry,
       "dcPowerLimitationIndex": dcPowerLimitationIndex,
       "dcPowerLimitationEventName": dcPowerLimitationEventName,
       "dcPowerLimitationStatus": dcPowerLimitationStatus,
       "dcPowerLimitationType": dcPowerLimitationType,
       "dcMaxTotalRectifierPower": dcMaxTotalRectifierPower,
       "dcPowerLimitationNoBatteryDischarge": dcPowerLimitationNoBatteryDischarge,
       "dcBattery": dcBattery,
       "dcFloatCharge": dcFloatCharge,
       "dcUsys20": dcUsys20,
       "dcBatteryTest": dcBatteryTest,
       "dcBatteryTestParameter": dcBatteryTestParameter,
       "dcBatteryTestUsupport": dcBatteryTestUsupport,
       "dcBatteryTestDuration": dcBatteryTestDuration,
       "dcBatteryTestInterval": dcBatteryTestInterval,
       "dcBatteryTestDischargeCurrent": dcBatteryTestDischargeCurrent,
       "dcBatteryTestMinDuration": dcBatteryTestMinDuration,
       "dcBatteryTestVoltageWithinUfloat": dcBatteryTestVoltageWithinUfloat,
       "dcBatteryTestVoltageWithinUfloatPeriod": dcBatteryTestVoltageWithinUfloatPeriod,
       "dcBatteryTestTempFrom": dcBatteryTestTempFrom,
       "dcBatteryTestTempTo": dcBatteryTestTempTo,
       "dcBatteryTestIntervalEnabled": dcBatteryTestIntervalEnabled,
       "dcBatteryTestStartTimeFrom": dcBatteryTestStartTimeFrom,
       "dcBatteryTestStartTimeTo": dcBatteryTestStartTimeTo,
       "dcBatteryTestResults": dcBatteryTestResults,
       "dcBatteryTestDateTime": dcBatteryTestDateTime,
       "dcBatteryTestResult": dcBatteryTestResult,
       "dcBatteryTestEndVoltage": dcBatteryTestEndVoltage,
       "dcBatteryTestControl": dcBatteryTestControl,
       "dcBatteryTestStatus": dcBatteryTestStatus,
       "dcBatteryTestFailureEvent": dcBatteryTestFailureEvent,
       "dcBatteryTestType": dcBatteryTestType,
       "dcBatteryTestTable": dcBatteryTestTable,
       "dcBatteryTestTableEntry": dcBatteryTestTableEntry,
       "dcBatteryTestTableIndex": dcBatteryTestTableIndex,
       "dcBatteryTestTablePriority": dcBatteryTestTablePriority,
       "dcBatteryTestTableName": dcBatteryTestTableName,
       "dcBatteryTestTableType": dcBatteryTestTableType,
       "dcBatteryTestTableStatus": dcBatteryTestTableStatus,
       "dcBatteryTestTableUsupport": dcBatteryTestTableUsupport,
       "dcBatteryTestTableDuration": dcBatteryTestTableDuration,
       "dcBatteryTestTableInterval": dcBatteryTestTableInterval,
       "dcBatteryTestTableDischargeCurrent": dcBatteryTestTableDischargeCurrent,
       "dcBatteryTestTableMinDuration": dcBatteryTestTableMinDuration,
       "dcBatteryTestTableVoltageWithinUfloat": dcBatteryTestTableVoltageWithinUfloat,
       "dcBatteryTestTableVoltageWithinUfloatPeriod": dcBatteryTestTableVoltageWithinUfloatPeriod,
       "dcBatteryTestTableTempFrom": dcBatteryTestTableTempFrom,
       "dcBatteryTestTableTempTo": dcBatteryTestTableTempTo,
       "dcBatteryTestTableIntervalEnabled": dcBatteryTestTableIntervalEnabled,
       "dcBatteryTestTableStartTimeFrom": dcBatteryTestTableStartTimeFrom,
       "dcBatteryTestTableStartTimeTo": dcBatteryTestTableStartTimeTo,
       "dcBatteryTestTableControl": dcBatteryTestTableControl,
       "dcBatteryTestTableFailureEvent": dcBatteryTestTableFailureEvent,
       "dcBatteryTestResultTable": dcBatteryTestResultTable,
       "dcBatteryTestResultTableEntry": dcBatteryTestResultTableEntry,
       "dcBatteryTestResultTableIndex": dcBatteryTestResultTableIndex,
       "dcBatteryTestResultTablePriority": dcBatteryTestResultTablePriority,
       "dcBatteryTestResultTableName": dcBatteryTestResultTableName,
       "dcBatteryTestResultTableDateTime": dcBatteryTestResultTableDateTime,
       "dcBatteryTestResultTableResult": dcBatteryTestResultTableResult,
       "dcBatteryTestResultTableEndVoltage": dcBatteryTestResultTableEndVoltage,
       "dcBatteryParameter": dcBatteryParameter,
       "dcTotalBatteryCapacity": dcTotalBatteryCapacity,
       "dcBatteryStringTable": dcBatteryStringTable,
       "dcBatteryStringEntry": dcBatteryStringEntry,
       "dcBatteryStringIndex": dcBatteryStringIndex,
       "dcBatteryStringName": dcBatteryStringName,
       "dcBatteryStringMaxIBatt": dcBatteryStringMaxIBatt,
       "dcBatteryStringCapacity": dcBatteryStringCapacity,
       "dcLossOfBackupTime": dcLossOfBackupTime,
       "dcLossOfBackupTimeEnabled": dcLossOfBackupTimeEnabled,
       "dcLossOfBackupTimeStatus": dcLossOfBackupTimeStatus,
       "dcExpectedBackupTime": dcExpectedBackupTime,
       "dcBatteryLithiumTable": dcBatteryLithiumTable,
       "dcBatteryLithiumEntry": dcBatteryLithiumEntry,
       "dcBatteryLithiumIndex": dcBatteryLithiumIndex,
       "dcBatteryLithiumName": dcBatteryLithiumName,
       "dcBatteryLithiumMainState": dcBatteryLithiumMainState,
       "dcBatteryLithiumSubState": dcBatteryLithiumSubState,
       "dcBatteryLithiumCurrent": dcBatteryLithiumCurrent,
       "dcBatteryLithiumStateOfCharge": dcBatteryLithiumStateOfCharge,
       "dcBatteryLithiumInstallationDate": dcBatteryLithiumInstallationDate,
       "dcBatteryLithiumSoH": dcBatteryLithiumSoH,
       "dcBatteryLifePredictionTable": dcBatteryLifePredictionTable,
       "dcBatteryLifePredictionEntry": dcBatteryLifePredictionEntry,
       "dcBatteryLifePredictionIndex": dcBatteryLifePredictionIndex,
       "dcBatteryLifePredictionName": dcBatteryLifePredictionName,
       "dcBatteryLifePredictionRemainingDays": dcBatteryLifePredictionRemainingDays,
       "dcBatteryLifePredictionInstallationDate": dcBatteryLifePredictionInstallationDate,
       "dcBatteryLifePredictionSoH": dcBatteryLifePredictionSoH,
       "dcBatteryLifePredictionStatus": dcBatteryLifePredictionStatus,
       "dcBatteryChargingCurrentLimitEnable": dcBatteryChargingCurrentLimitEnable,
       "dcBatteryTotalChargingCurrentLimitEnable": dcBatteryTotalChargingCurrentLimitEnable,
       "dcBatteryTotalMaxIBatt": dcBatteryTotalMaxIBatt,
       "dcEqualize": dcEqualize,
       "dcEqualizeControl": dcEqualizeControl,
       "dcEqualizeStatus": dcEqualizeStatus,
       "dcEqualizeEnabled": dcEqualizeEnabled,
       "dcEqualizeParameter": dcEqualizeParameter,
       "dcEqualizeVoltage": dcEqualizeVoltage,
       "dcEqualizeDuration": dcEqualizeDuration,
       "dcEqualizeUseBattRoomFanEnabled": dcEqualizeUseBattRoomFanEnabled,
       "dcEqualizeLeadTime": dcEqualizeLeadTime,
       "dcEqualizeTimeLag": dcEqualizeTimeLag,
       "dcEqualizeInterval": dcEqualizeInterval,
       "dcEqualizeStartTimeIntervalFrom": dcEqualizeStartTimeIntervalFrom,
       "dcEqualizeStartTimeIntervalTo": dcEqualizeStartTimeIntervalTo,
       "dcEqualizeInhibitAfterBoost": dcEqualizeInhibitAfterBoost,
       "dcBoostCharge": dcBoostCharge,
       "dcBoostChargeControl": dcBoostChargeControl,
       "dcBoostChargeStatus": dcBoostChargeStatus,
       "dcBoostChargeType": dcBoostChargeType,
       "dcBoostChargeParameter": dcBoostChargeParameter,
       "dcBoostChargeVoltage": dcBoostChargeVoltage,
       "dcBoostChargeMaxDuration": dcBoostChargeMaxDuration,
       "dcBoostChargeUseBattRoomFanEnabled": dcBoostChargeUseBattRoomFanEnabled,
       "dcBoostChargeTimeLag": dcBoostChargeTimeLag,
       "dcBoostChargeIstart": dcBoostChargeIstart,
       "dcBoostChargeIstop": dcBoostChargeIstop,
       "dcBoostChargeInhibitTime": dcBoostChargeInhibitTime,
       "dcBoostChargeSoCBelow": dcBoostChargeSoCBelow,
       "dcSystemVoltageSupervision": dcSystemVoltageSupervision,
       "dcUaMax": dcUaMax,
       "dcUaMin": dcUaMin,
       "dcUsMax": dcUsMax,
       "dcUsMin": dcUsMin,
       "dcBoD": dcBoD,
       "dcHysteresis": dcHysteresis,
       "dcSuppressUaLowEnabled": dcSuppressUaLowEnabled,
       "dcSuppressUsLowEnabled": dcSuppressUsLowEnabled,
       "dcEnableUsTempComp": dcEnableUsTempComp,
       "dcEvtCtrlCharge": dcEvtCtrlCharge,
       "dcEvtCtrlChargeStatus": dcEvtCtrlChargeStatus,
       "dcEvtCtrlChargeType": dcEvtCtrlChargeType,
       "dcEvtCtrlChargeParameter": dcEvtCtrlChargeParameter,
       "dcEvtCtrlChargeVoltage": dcEvtCtrlChargeVoltage,
       "dcEvtCtrlChargeTempCompEnabled": dcEvtCtrlChargeTempCompEnabled,
       "dcEvtCtrlChargeMaxIBatt": dcEvtCtrlChargeMaxIBatt,
       "dcEventControlledChargeTable": dcEventControlledChargeTable,
       "dcEventControlledChargeTableEntry": dcEventControlledChargeTableEntry,
       "dcEventControlledChargeTableIndex": dcEventControlledChargeTableIndex,
       "dcEventControlledChargeTablePriority": dcEventControlledChargeTablePriority,
       "dcEventControlledChargeTableName": dcEventControlledChargeTableName,
       "dcEventControlledChargeTableActivationInput": dcEventControlledChargeTableActivationInput,
       "dcEventControlledChargeTableStatus": dcEventControlledChargeTableStatus,
       "dcEventControlledChargeTableType": dcEventControlledChargeTableType,
       "dcEventControlledChargeTableVoltage": dcEventControlledChargeTableVoltage,
       "dcEventControlledChargeTableMaxIBatt": dcEventControlledChargeTableMaxIBatt,
       "dcEventControlledChargeTableTempCompEnabled": dcEventControlledChargeTableTempCompEnabled,
       "dcTempComp": dcTempComp,
       "dcTempCompType": dcTempCompType,
       "dcSlope": dcSlope,
       "dcStartTemp": dcStartTemp,
       "dcStopTemp": dcStopTemp,
       "dcMaxVoltage": dcMaxVoltage,
       "dcLowStopVoltage": dcLowStopVoltage,
       "dcLowStartTemp": dcLowStartTemp,
       "dcLowTempSlope": dcLowTempSlope,
       "dcHighStartTemp": dcHighStartTemp,
       "dcHighTempSlope": dcHighTempSlope,
       "dcHighStopVoltage": dcHighStopVoltage,
       "dcRunawayTemp": dcRunawayTemp,
       "dcRunawayVoltage": dcRunawayVoltage,
       "dcTempSupervision": dcTempSupervision,
       "dcHighTemp": dcHighTemp,
       "dcHighTempHyst": dcHighTempHyst,
       "dcBatteryType": dcBatteryType,
       "dcBatteryTypeSelect": dcBatteryTypeSelect,
       "dcInputOutput": dcInputOutput,
       "dcControlEventTable": dcControlEventTable,
       "dcControlEventEntry": dcControlEventEntry,
       "dcControlEventIndex": dcControlEventIndex,
       "dcControlEventName": dcControlEventName,
       "dcControlEventIdentifier": dcControlEventIdentifier,
       "dcControlEventValue": dcControlEventValue,
       "dcMisc": dcMisc,
       "dcTrapDestinationTable": dcTrapDestinationTable,
       "dcTrapDestinationEntry": dcTrapDestinationEntry,
       "dcTrapDestinationIndex": dcTrapDestinationIndex,
       "dcTrapDestinationIp": dcTrapDestinationIp,
       "dcTrapDestinationPort": dcTrapDestinationPort,
       "dcTrapDestinationUser": dcTrapDestinationUser,
       "dcFileProcessingStatus": dcFileProcessingStatus,
       "dcResendActiveAlarmTraps": dcResendActiveAlarmTraps,
       "dcRebootController": dcRebootController,
       "dcTrapDestinationv2Table": dcTrapDestinationv2Table,
       "dcTrapDestinationv2Entry": dcTrapDestinationv2Entry,
       "dcTrapDestinationv2Index": dcTrapDestinationv2Index,
       "dcTrapDestinationv2": dcTrapDestinationv2,
       "dcTrapDestinationv2Port": dcTrapDestinationv2Port,
       "dcTrapDestinationv2User": dcTrapDestinationv2User,
       "dcConfig": dcConfig,
       "dcDefaultLogEventTable": dcDefaultLogEventTable,
       "dcDefaultLogEventEntry": dcDefaultLogEventEntry,
       "dcDefaultLogEventIndex": dcDefaultLogEventIndex,
       "dcDefaultLogEventName": dcDefaultLogEventName,
       "dcDefaultLogEventLogged": dcDefaultLogEventLogged,
       "dcEventProcessingEventTable": dcEventProcessingEventTable,
       "dcEventProcessingEventEntry": dcEventProcessingEventEntry,
       "dcEventProcessingEventIndex": dcEventProcessingEventIndex,
       "dcEventProcessingEventName": dcEventProcessingEventName,
       "dcEventProcessingEventAssigned": dcEventProcessingEventAssigned,
       "dcEventProcessingEventType": dcEventProcessingEventType,
       "dcEventProcessingEventSelected": dcEventProcessingEventSelected,
       "dcLvdTable": dcLvdTable,
       "dcLvdEntry": dcLvdEntry,
       "dcLvdIndex": dcLvdIndex,
       "dcLvdName": dcLvdName,
       "dcLvdDisconnectDelay": dcLvdDisconnectDelay,
       "dcLvdType": dcLvdType,
       "dcLvdVoltageThreshold": dcLvdVoltageThreshold,
       "dcLvdVoltageHysteresis": dcLvdVoltageHysteresis,
       "dcLvdControlEvent": dcLvdControlEvent,
       "dcLvdMonitoringEvent": dcLvdMonitoringEvent,
       "dcEventDefinitionTable": dcEventDefinitionTable,
       "dcEventDefinitionEntry": dcEventDefinitionEntry,
       "dcEventIndex": dcEventIndex,
       "dcEventName": dcEventName,
       "dcThreshold": dcThreshold,
       "dcThresholdHysteresis": dcThresholdHysteresis,
       "dcUnit": dcUnit,
       "dcFilterTable": dcFilterTable,
       "dcFilterEntry": dcFilterEntry,
       "dcFilterIndex": dcFilterIndex,
       "dcFilterName": dcFilterName,
       "dcTrueForMin": dcTrueForMin,
       "dcFalseForMin": dcFalseForMin,
       "dcTimerTable": dcTimerTable,
       "dcTimerEntry": dcTimerEntry,
       "dcTimerIndex": dcTimerIndex,
       "dcTimerName": dcTimerName,
       "dcStartTime": dcStartTime,
       "dcStartDaySu": dcStartDaySu,
       "dcStartDayMo": dcStartDayMo,
       "dcStartDayTu": dcStartDayTu,
       "dcStartDayWe": dcStartDayWe,
       "dcStartDayTh": dcStartDayTh,
       "dcStartDayFr": dcStartDayFr,
       "dcStartDaySa": dcStartDaySa,
       "dcEndTime": dcEndTime,
       "dcEndDaySu": dcEndDaySu,
       "dcEndDayMo": dcEndDayMo,
       "dcEndDayTu": dcEndDayTu,
       "dcEndDayWe": dcEndDayWe,
       "dcEndDayTh": dcEndDayTh,
       "dcEndDayFr": dcEndDayFr,
       "dcEndDaySa": dcEndDaySa,
       "dcMeasurement": dcMeasurement,
       "dcMeasurementTable": dcMeasurementTable,
       "dcMeasurementEntry": dcMeasurementEntry,
       "dcMeasurementIndex": dcMeasurementIndex,
       "dcMeasurementName": dcMeasurementName,
       "dcMeasurementValue": dcMeasurementValue,
       "dcMeasurementScaleFactor": dcMeasurementScaleFactor,
       "dcMeasurementUnit": dcMeasurementUnit,
       "dcMeterPanel": dcMeterPanel,
       "dcMeterPanelEventTable": dcMeterPanelEventTable,
       "dcMeterPanelEventEntry": dcMeterPanelEventEntry,
       "dcMeterPanelEventIndex": dcMeterPanelEventIndex,
       "dcMeterPanelEventName": dcMeterPanelEventName,
       "dcMeterPanelEventValue": dcMeterPanelEventValue,
       "dcMeterPanelEventHourMeterValue": dcMeterPanelEventHourMeterValue,
       "dcMeterPanelMeasurementTable": dcMeterPanelMeasurementTable,
       "dcMeterPanelMeasurementEntry": dcMeterPanelMeasurementEntry,
       "dcMeterPanelMeasurementIndex": dcMeterPanelMeasurementIndex,
       "dcMeterPanelMeasurementName": dcMeterPanelMeasurementName,
       "dcMeterPanelMeasurementValue": dcMeterPanelMeasurementValue,
       "dcMeterPanelMeasurementUnit": dcMeterPanelMeasurementUnit,
       "dcPVC": dcPVC,
       "dcNumberPVCs": dcNumberPVCs,
       "dcNumberPVCsFailure": dcNumberPVCsFailure,
       "dcNumberPVCsOkay": dcNumberPVCsOkay,
       "dcPVCTable": dcPVCTable,
       "dcPVCEntry": dcPVCEntry,
       "dcPVCIndex": dcPVCIndex,
       "dcPVCIdentifier": dcPVCIdentifier,
       "dcPVCSlotState": dcPVCSlotState,
       "dcPVCMainStatus": dcPVCMainStatus,
       "dcPVCSubStatus": dcPVCSubStatus,
       "dcPVCConfiguration": dcPVCConfiguration,
       "dcPVCIout": dcPVCIout,
       "dcPVCUout": dcPVCUout,
       "dcPVCIin": dcPVCIin,
       "dcPVCUin": dcPVCUin,
       "dcPVCGroupTable": dcPVCGroupTable,
       "dcPVCGroupEntry": dcPVCGroupEntry,
       "dcPVCGroupIndex": dcPVCGroupIndex,
       "dcPVCGroupPVCType": dcPVCGroupPVCType,
       "dcPVCGroupVoltage": dcPVCGroupVoltage,
       "dcPVCGroupVPGM": dcPVCGroupVPGM,
       "dcPVCGroupInputLowOff": dcPVCGroupInputLowOff,
       "dcPVCGroupInputLowOn": dcPVCGroupInputLowOn,
       "dcPVCGroupStartUpDelay": dcPVCGroupStartUpDelay,
       "dcPVCGroupOvpLimit": dcPVCGroupOvpLimit,
       "dcPVCGroupAlarmDelay": dcPVCGroupAlarmDelay,
       "dcInventory": dcInventory,
       "dcInventoryTable": dcInventoryTable,
       "dcInventoryEntry": dcInventoryEntry,
       "dcInventoryIndex": dcInventoryIndex,
       "dcInventoryType": dcInventoryType,
       "dcInventoryName": dcInventoryName,
       "dcInventorySwVersion": dcInventorySwVersion,
       "dcInventoryBuildVersion": dcInventoryBuildVersion,
       "dcInventoryPartNb": dcInventoryPartNb,
       "dcInventorySerialNb": dcInventorySerialNb,
       "dcInventoryTopLevel": dcInventoryTopLevel,
       "dcIP": dcIP,
       "dcIPv4": dcIPv4,
       "dcIPv4Address": dcIPv4Address,
       "dcIPv4SubnetMask": dcIPv4SubnetMask,
       "dcIPv4Gateway": dcIPv4Gateway,
       "dcIPv4DNS": dcIPv4DNS,
       "dcIPv6": dcIPv6,
       "dcIPv6LinkLocalAddress": dcIPv6LinkLocalAddress,
       "dcIPv6Address": dcIPv6Address,
       "dcIPv6Gateway": dcIPv6Gateway,
       "dcIPv6DNSAuto": dcIPv6DNSAuto,
       "dcIPv6DNSManual": dcIPv6DNSManual,
       "dcAircon": dcAircon,
       "dcAirconTable": dcAirconTable,
       "dcAirconEntry": dcAirconEntry,
       "dcAirconIndex": dcAirconIndex,
       "dcCoolingPlanIndex": dcCoolingPlanIndex,
       "dcAirconName": dcAirconName,
       "dcAirconMainStatus": dcAirconMainStatus,
       "dcAirconSubStatus": dcAirconSubStatus,
       "dcAirconConfiguration": dcAirconConfiguration,
       "dcAirconPlanName": dcAirconPlanName,
       "dcAirconRoomTemp": dcAirconRoomTemp,
       "dcCoolingPlanActivationInput": dcCoolingPlanActivationInput,
       "dcCoolingPlanPriority": dcCoolingPlanPriority,
       "dcCoolingPlanStatus": dcCoolingPlanStatus,
       "dcCoolingPlanTargetTemp": dcCoolingPlanTargetTemp,
       "dcCoolingPlanOperatingMode": dcCoolingPlanOperatingMode,
       "dcCoolingPlanStandbyFanSpeed": dcCoolingPlanStandbyFanSpeed,
       "dcCoolingPlanHeaterStartTemp": dcCoolingPlanHeaterStartTemp,
       "dcCoolingPlanHeaterHyst": dcCoolingPlanHeaterHyst,
       "dcCoolingPlanHeaterControl": dcCoolingPlanHeaterControl,
       "dcInverter": dcInverter,
       "dcInverterGroupTable": dcInverterGroupTable,
       "dcInverterGroupEntry": dcInverterGroupEntry,
       "dcInverterGroupIndex": dcInverterGroupIndex,
       "dcInverterGroupState": dcInverterGroupState,
       "dcInverterGroupLoadPosition": dcInverterGroupLoadPosition,
       "dcInverterGroupNbrOfConfigInverters": dcInverterGroupNbrOfConfigInverters,
       "dcInverterGroupNbrOfPresentInverters": dcInverterGroupNbrOfPresentInverters,
       "dcInverterGroupPhase": dcInverterGroupPhase,
       "dcInverterGroupDcVoltage": dcInverterGroupDcVoltage,
       "dcInverterGroupInputDcPower": dcInverterGroupInputDcPower,
       "dcInverterGroupInputVoltage1": dcInverterGroupInputVoltage1,
       "dcInverterGroupInputVoltage2": dcInverterGroupInputVoltage2,
       "dcInverterGroupInputVoltage3": dcInverterGroupInputVoltage3,
       "dcInverterGroupInputApparentPower1": dcInverterGroupInputApparentPower1,
       "dcInverterGroupInputApparentPower2": dcInverterGroupInputApparentPower2,
       "dcInverterGroupInputApparentPower3": dcInverterGroupInputApparentPower3,
       "dcInverterGroupInputFrequency": dcInverterGroupInputFrequency,
       "dcInverterGroupOutputVoltage1": dcInverterGroupOutputVoltage1,
       "dcInverterGroupOutputVoltage2": dcInverterGroupOutputVoltage2,
       "dcInverterGroupOutputVoltage3": dcInverterGroupOutputVoltage3,
       "dcInverterGroupOutputApparentPower1": dcInverterGroupOutputApparentPower1,
       "dcInverterGroupOutputApparentPower2": dcInverterGroupOutputApparentPower2,
       "dcInverterGroupOutputApparentPower3": dcInverterGroupOutputApparentPower3,
       "dcInverterGroupOutputFrequency": dcInverterGroupOutputFrequency,
       "controllerEvents": controllerEvents,
       "controllerEventObjects": controllerEventObjects,
       "controllerEventsV2": controllerEventsV2,
       "systemNonUrgentAlarm": systemNonUrgentAlarm,
       "systemUrgentAlarm": systemUrgentAlarm,
       "systemCriticalAlarm": systemCriticalAlarm,
       "systemAllAlarm": systemAllAlarm}
)
