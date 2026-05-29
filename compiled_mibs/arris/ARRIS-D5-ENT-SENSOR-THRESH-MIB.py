# SNMP MIB module (ARRIS-D5-ENT-SENSOR-THRESH-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\arris\d5\ARRIS-D5-ENT-SENSOR-THRESH-MIB

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

(arrisD5UEQam,
 arrisGlobalAccessMib,
 arrisGlobalAccessProductUas,
 cm110,
 cmts1500,
 cmtsC3,
 cmtsC4,
 cmtsCommon,
 cmtsMSAS,
 mrcController,
 packetport,
 tcm,
 ttm,
 ttp) = mibBuilder.importSymbols(
    "ARRIS-MIB",
    "arrisD5UEQam",
    "arrisGlobalAccessMib",
    "arrisGlobalAccessProductUas",
    "cm110",
    "cmts1500",
    "cmtsC3",
    "cmtsC4",
    "cmtsCommon",
    "cmtsMSAS",
    "mrcController",
    "packetport",
    "tcm",
    "ttm",
    "ttp")

(entPhysicalIndex,
 entityPhysicalGroup) = mibBuilder.importSymbols(
    "ENTITY-MIB",
    "entPhysicalIndex",
    "entityPhysicalGroup")

(entPhySensorEntry,
 entPhySensorOperStatus,
 entPhySensorPrecision,
 entPhySensorScale,
 entPhySensorType,
 entPhySensorUnitsDisplay,
 entPhySensorValue,
 entPhySensorValueTimeStamp,
 entPhySensorValueUpdateRate,
 entitySensorCompliance,
 entitySensorValueGroup) = mibBuilder.importSymbols(
    "ENTITY-SENSOR-MIB",
    "entPhySensorEntry",
    "entPhySensorOperStatus",
    "entPhySensorPrecision",
    "entPhySensorScale",
    "entPhySensorType",
    "entPhySensorUnitsDisplay",
    "entPhySensorValue",
    "entPhySensorValueTimeStamp",
    "entPhySensorValueUpdateRate",
    "entitySensorCompliance",
    "entitySensorValueGroup")

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

arrisEntSensorThreshMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4115, 1, 8, 1, 4)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_EntThreshObjects_ObjectIdentity = ObjectIdentity
entThreshObjects = _EntThreshObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4115, 1, 8, 1, 4, 1)
)
_EntThreshTable_Object = MibTable
entThreshTable = _EntThreshTable_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 8, 1, 4, 1, 1)
)
if mibBuilder.loadTexts:
    entThreshTable.setStatus("current")
_EntThreshEntry_Object = MibTableRow
entThreshEntry = _EntThreshEntry_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 8, 1, 4, 1, 1, 1)
)
if mibBuilder.loadTexts:
    entThreshEntry.setStatus("current")
_EntLowerWarnThresh_Type = Integer32
_EntLowerWarnThresh_Object = MibTableColumn
entLowerWarnThresh = _EntLowerWarnThresh_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 8, 1, 4, 1, 1, 1, 1),
    _EntLowerWarnThresh_Type()
)
entLowerWarnThresh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    entLowerWarnThresh.setStatus("current")
_EntUpperWarnThresh_Type = Integer32
_EntUpperWarnThresh_Object = MibTableColumn
entUpperWarnThresh = _EntUpperWarnThresh_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 8, 1, 4, 1, 1, 1, 2),
    _EntUpperWarnThresh_Type()
)
entUpperWarnThresh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    entUpperWarnThresh.setStatus("current")
_EntLowerFatalThresh_Type = Integer32
_EntLowerFatalThresh_Object = MibTableColumn
entLowerFatalThresh = _EntLowerFatalThresh_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 8, 1, 4, 1, 1, 1, 3),
    _EntLowerFatalThresh_Type()
)
entLowerFatalThresh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    entLowerFatalThresh.setStatus("current")
_EntUpperFatalThresh_Type = Integer32
_EntUpperFatalThresh_Object = MibTableColumn
entUpperFatalThresh = _EntUpperFatalThresh_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 8, 1, 4, 1, 1, 1, 4),
    _EntUpperFatalThresh_Type()
)
entUpperFatalThresh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    entUpperFatalThresh.setStatus("current")
_EntThreshConformance_ObjectIdentity = ObjectIdentity
entThreshConformance = _EntThreshConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4115, 1, 8, 1, 4, 2)
)
_EntThreshCompliances_ObjectIdentity = ObjectIdentity
entThreshCompliances = _EntThreshCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4115, 1, 8, 1, 4, 2, 1)
)
_EntThreshGroups_ObjectIdentity = ObjectIdentity
entThreshGroups = _EntThreshGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4115, 1, 8, 1, 4, 2, 2)
)
entPhySensorEntry.registerAugmentions(
    ("ARRIS-D5-ENT-SENSOR-THRESH-MIB",
     "entThreshEntry")
)
entThreshEntry.setIndexNames(*entPhySensorEntry.getIndexNames())

# Managed Objects groups

entThreshValueGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4115, 1, 8, 1, 4, 2, 2, 1)
)
entThreshValueGroup.setObjects(
      *(("ARRIS-D5-ENT-SENSOR-THRESH-MIB", "entLowerWarnThresh"),
        ("ARRIS-D5-ENT-SENSOR-THRESH-MIB", "entUpperWarnThresh"),
        ("ARRIS-D5-ENT-SENSOR-THRESH-MIB", "entUpperFatalThresh"),
        ("ARRIS-D5-ENT-SENSOR-THRESH-MIB", "entLowerFatalThresh"))
)
if mibBuilder.loadTexts:
    entThreshValueGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

entThreshCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4115, 1, 8, 1, 4, 2, 1, 1)
)
entThreshCompliance.setObjects(
    ("ARRIS-D5-ENT-SENSOR-THRESH-MIB", "entThreshValueGroup")
)
if mibBuilder.loadTexts:
    entThreshCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ARRIS-D5-ENT-SENSOR-THRESH-MIB",
    **{"arrisEntSensorThreshMIB": arrisEntSensorThreshMIB,
       "entThreshObjects": entThreshObjects,
       "entThreshTable": entThreshTable,
       "entThreshEntry": entThreshEntry,
       "entLowerWarnThresh": entLowerWarnThresh,
       "entUpperWarnThresh": entUpperWarnThresh,
       "entLowerFatalThresh": entLowerFatalThresh,
       "entUpperFatalThresh": entUpperFatalThresh,
       "entThreshConformance": entThreshConformance,
       "entThreshCompliances": entThreshCompliances,
       "entThreshCompliance": entThreshCompliance,
       "entThreshGroups": entThreshGroups,
       "entThreshValueGroup": entThreshValueGroup}
)
