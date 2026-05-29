# SNMP MIB module (PACKETFLUX-SENSORS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\packetflux\PACKETFLUX-SENSORS-MIB

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

(packetfluxFeatureSpecific,) = mibBuilder.importSymbols(
    "PACKETFLUX-SMI",
    "packetfluxFeatureSpecific")

(Fixed2DecimalDigits,
 Fixed6DecimalDigits) = mibBuilder.importSymbols(
    "PACKETFLUX-TC",
    "Fixed2DecimalDigits",
    "Fixed6DecimalDigits")

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

packetfluxSensors = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 32050, 3, 2)
)
if mibBuilder.loadTexts:
    packetfluxSensors.setRevisions(
        ("2020-04-12 05:59",
         "2018-07-08 11:26")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_VoltageSensorTable_Object = MibTable
voltageSensorTable = _VoltageSensorTable_Object(
    (1, 3, 6, 1, 4, 1, 32050, 3, 2, 1)
)
if mibBuilder.loadTexts:
    voltageSensorTable.setStatus("current")
_VoltageSensorEntry_Object = MibTableRow
voltageSensorEntry = _VoltageSensorEntry_Object(
    (1, 3, 6, 1, 4, 1, 32050, 3, 2, 1, 1)
)
voltageSensorEntry.setIndexNames(
    (0, "PACKETFLUX-SENSORS-MIB", "voltageSensorSlot"),
    (0, "PACKETFLUX-SENSORS-MIB", "voltageSensorIndex"),
)
if mibBuilder.loadTexts:
    voltageSensorEntry.setStatus("current")
_VoltageSensorSlot_Type = Unsigned32
_VoltageSensorSlot_Object = MibTableColumn
voltageSensorSlot = _VoltageSensorSlot_Object(
    (1, 3, 6, 1, 4, 1, 32050, 3, 2, 1, 1, 1),
    _VoltageSensorSlot_Type()
)
voltageSensorSlot.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    voltageSensorSlot.setStatus("current")
_VoltageSensorIndex_Type = Unsigned32
_VoltageSensorIndex_Object = MibTableColumn
voltageSensorIndex = _VoltageSensorIndex_Object(
    (1, 3, 6, 1, 4, 1, 32050, 3, 2, 1, 1, 2),
    _VoltageSensorIndex_Type()
)
voltageSensorIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    voltageSensorIndex.setStatus("current")
_VoltageSensorDescription_Type = DisplayString
_VoltageSensorDescription_Object = MibTableColumn
voltageSensorDescription = _VoltageSensorDescription_Object(
    (1, 3, 6, 1, 4, 1, 32050, 3, 2, 1, 1, 3),
    _VoltageSensorDescription_Type()
)
voltageSensorDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    voltageSensorDescription.setStatus("current")
_VoltageSensorValue_Type = Fixed6DecimalDigits
_VoltageSensorValue_Object = MibTableColumn
voltageSensorValue = _VoltageSensorValue_Object(
    (1, 3, 6, 1, 4, 1, 32050, 3, 2, 1, 1, 4),
    _VoltageSensorValue_Type()
)
voltageSensorValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voltageSensorValue.setStatus("current")
if mibBuilder.loadTexts:
    voltageSensorValue.setUnits("V")
_VoltageSensorFunction_Type = DisplayString
_VoltageSensorFunction_Object = MibTableColumn
voltageSensorFunction = _VoltageSensorFunction_Object(
    (1, 3, 6, 1, 4, 1, 32050, 3, 2, 1, 1, 5),
    _VoltageSensorFunction_Type()
)
voltageSensorFunction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voltageSensorFunction.setStatus("current")
_CurrentSensorTable_Object = MibTable
currentSensorTable = _CurrentSensorTable_Object(
    (1, 3, 6, 1, 4, 1, 32050, 3, 2, 2)
)
if mibBuilder.loadTexts:
    currentSensorTable.setStatus("current")
_CurrentSensorEntry_Object = MibTableRow
currentSensorEntry = _CurrentSensorEntry_Object(
    (1, 3, 6, 1, 4, 1, 32050, 3, 2, 2, 1)
)
currentSensorEntry.setIndexNames(
    (0, "PACKETFLUX-SENSORS-MIB", "currentSensorSlot"),
    (0, "PACKETFLUX-SENSORS-MIB", "currentSensorIndex"),
)
if mibBuilder.loadTexts:
    currentSensorEntry.setStatus("current")
_CurrentSensorSlot_Type = Unsigned32
_CurrentSensorSlot_Object = MibTableColumn
currentSensorSlot = _CurrentSensorSlot_Object(
    (1, 3, 6, 1, 4, 1, 32050, 3, 2, 2, 1, 1),
    _CurrentSensorSlot_Type()
)
currentSensorSlot.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    currentSensorSlot.setStatus("current")
_CurrentSensorIndex_Type = Unsigned32
_CurrentSensorIndex_Object = MibTableColumn
currentSensorIndex = _CurrentSensorIndex_Object(
    (1, 3, 6, 1, 4, 1, 32050, 3, 2, 2, 1, 2),
    _CurrentSensorIndex_Type()
)
currentSensorIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    currentSensorIndex.setStatus("current")
_CurrentSensorDescription_Type = DisplayString
_CurrentSensorDescription_Object = MibTableColumn
currentSensorDescription = _CurrentSensorDescription_Object(
    (1, 3, 6, 1, 4, 1, 32050, 3, 2, 2, 1, 3),
    _CurrentSensorDescription_Type()
)
currentSensorDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    currentSensorDescription.setStatus("current")
_CurrentSensorValue_Type = Fixed6DecimalDigits
_CurrentSensorValue_Object = MibTableColumn
currentSensorValue = _CurrentSensorValue_Object(
    (1, 3, 6, 1, 4, 1, 32050, 3, 2, 2, 1, 4),
    _CurrentSensorValue_Type()
)
currentSensorValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    currentSensorValue.setStatus("current")
if mibBuilder.loadTexts:
    currentSensorValue.setUnits("A")
_CurrentSensorFunction_Type = DisplayString
_CurrentSensorFunction_Object = MibTableColumn
currentSensorFunction = _CurrentSensorFunction_Object(
    (1, 3, 6, 1, 4, 1, 32050, 3, 2, 2, 1, 5),
    _CurrentSensorFunction_Type()
)
currentSensorFunction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    currentSensorFunction.setStatus("current")
_TemperatureSensorTable_Object = MibTable
temperatureSensorTable = _TemperatureSensorTable_Object(
    (1, 3, 6, 1, 4, 1, 32050, 3, 2, 3)
)
if mibBuilder.loadTexts:
    temperatureSensorTable.setStatus("current")
_TemperatureSensorEntry_Object = MibTableRow
temperatureSensorEntry = _TemperatureSensorEntry_Object(
    (1, 3, 6, 1, 4, 1, 32050, 3, 2, 3, 1)
)
temperatureSensorEntry.setIndexNames(
    (0, "PACKETFLUX-SENSORS-MIB", "temperatureSensorSlot"),
    (0, "PACKETFLUX-SENSORS-MIB", "temperatureSensorIndex"),
)
if mibBuilder.loadTexts:
    temperatureSensorEntry.setStatus("current")
_TemperatureSensorSlot_Type = Unsigned32
_TemperatureSensorSlot_Object = MibTableColumn
temperatureSensorSlot = _TemperatureSensorSlot_Object(
    (1, 3, 6, 1, 4, 1, 32050, 3, 2, 3, 1, 1),
    _TemperatureSensorSlot_Type()
)
temperatureSensorSlot.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    temperatureSensorSlot.setStatus("current")
_TemperatureSensorIndex_Type = Unsigned32
_TemperatureSensorIndex_Object = MibTableColumn
temperatureSensorIndex = _TemperatureSensorIndex_Object(
    (1, 3, 6, 1, 4, 1, 32050, 3, 2, 3, 1, 2),
    _TemperatureSensorIndex_Type()
)
temperatureSensorIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    temperatureSensorIndex.setStatus("current")
_TemperatureSensorDescription_Type = DisplayString
_TemperatureSensorDescription_Object = MibTableColumn
temperatureSensorDescription = _TemperatureSensorDescription_Object(
    (1, 3, 6, 1, 4, 1, 32050, 3, 2, 3, 1, 3),
    _TemperatureSensorDescription_Type()
)
temperatureSensorDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    temperatureSensorDescription.setStatus("current")
_TemperatureSensorValue_Type = Fixed2DecimalDigits
_TemperatureSensorValue_Object = MibTableColumn
temperatureSensorValue = _TemperatureSensorValue_Object(
    (1, 3, 6, 1, 4, 1, 32050, 3, 2, 3, 1, 4),
    _TemperatureSensorValue_Type()
)
temperatureSensorValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    temperatureSensorValue.setStatus("current")
if mibBuilder.loadTexts:
    temperatureSensorValue.setUnits("C")
_TemperatureSensorFunction_Type = DisplayString
_TemperatureSensorFunction_Object = MibTableColumn
temperatureSensorFunction = _TemperatureSensorFunction_Object(
    (1, 3, 6, 1, 4, 1, 32050, 3, 2, 3, 1, 5),
    _TemperatureSensorFunction_Type()
)
temperatureSensorFunction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    temperatureSensorFunction.setStatus("current")
_ResistanceSensorTable_Object = MibTable
resistanceSensorTable = _ResistanceSensorTable_Object(
    (1, 3, 6, 1, 4, 1, 32050, 3, 2, 4)
)
if mibBuilder.loadTexts:
    resistanceSensorTable.setStatus("current")
_ResistanceSensorEntry_Object = MibTableRow
resistanceSensorEntry = _ResistanceSensorEntry_Object(
    (1, 3, 6, 1, 4, 1, 32050, 3, 2, 4, 1)
)
resistanceSensorEntry.setIndexNames(
    (0, "PACKETFLUX-SENSORS-MIB", "resistanceSensorSlot"),
    (0, "PACKETFLUX-SENSORS-MIB", "resistanceSensorIndex"),
)
if mibBuilder.loadTexts:
    resistanceSensorEntry.setStatus("current")
_ResistanceSensorSlot_Type = Unsigned32
_ResistanceSensorSlot_Object = MibTableColumn
resistanceSensorSlot = _ResistanceSensorSlot_Object(
    (1, 3, 6, 1, 4, 1, 32050, 3, 2, 4, 1, 1),
    _ResistanceSensorSlot_Type()
)
resistanceSensorSlot.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    resistanceSensorSlot.setStatus("current")
_ResistanceSensorIndex_Type = Unsigned32
_ResistanceSensorIndex_Object = MibTableColumn
resistanceSensorIndex = _ResistanceSensorIndex_Object(
    (1, 3, 6, 1, 4, 1, 32050, 3, 2, 4, 1, 2),
    _ResistanceSensorIndex_Type()
)
resistanceSensorIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    resistanceSensorIndex.setStatus("current")
_ResistanceSensorDescription_Type = DisplayString
_ResistanceSensorDescription_Object = MibTableColumn
resistanceSensorDescription = _ResistanceSensorDescription_Object(
    (1, 3, 6, 1, 4, 1, 32050, 3, 2, 4, 1, 3),
    _ResistanceSensorDescription_Type()
)
resistanceSensorDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    resistanceSensorDescription.setStatus("current")
_ResistanceSensorValue_Type = Fixed2DecimalDigits
_ResistanceSensorValue_Object = MibTableColumn
resistanceSensorValue = _ResistanceSensorValue_Object(
    (1, 3, 6, 1, 4, 1, 32050, 3, 2, 4, 1, 4),
    _ResistanceSensorValue_Type()
)
resistanceSensorValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    resistanceSensorValue.setStatus("current")
if mibBuilder.loadTexts:
    resistanceSensorValue.setUnits("C")
_ResistanceSensorFunction_Type = DisplayString
_ResistanceSensorFunction_Object = MibTableColumn
resistanceSensorFunction = _ResistanceSensorFunction_Object(
    (1, 3, 6, 1, 4, 1, 32050, 3, 2, 4, 1, 5),
    _ResistanceSensorFunction_Type()
)
resistanceSensorFunction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    resistanceSensorFunction.setStatus("current")
_PacketfluxSensorsConformance_ObjectIdentity = ObjectIdentity
packetfluxSensorsConformance = _PacketfluxSensorsConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 32050, 3, 2, 128)
)
_PacketfluxSensorsGroups_ObjectIdentity = ObjectIdentity
packetfluxSensorsGroups = _PacketfluxSensorsGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 32050, 3, 2, 128, 1)
)

# Managed Objects groups

packetfluxSensorsMibAllObjects = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 32050, 3, 2, 128, 1, 1)
)
packetfluxSensorsMibAllObjects.setObjects(
      *(("PACKETFLUX-SENSORS-MIB", "currentSensorDescription"),
        ("PACKETFLUX-SENSORS-MIB", "currentSensorFunction"),
        ("PACKETFLUX-SENSORS-MIB", "currentSensorValue"),
        ("PACKETFLUX-SENSORS-MIB", "temperatureSensorDescription"),
        ("PACKETFLUX-SENSORS-MIB", "temperatureSensorFunction"),
        ("PACKETFLUX-SENSORS-MIB", "temperatureSensorValue"),
        ("PACKETFLUX-SENSORS-MIB", "resistanceSensorDescription"),
        ("PACKETFLUX-SENSORS-MIB", "resistanceSensorFunction"),
        ("PACKETFLUX-SENSORS-MIB", "resistanceSensorValue"),
        ("PACKETFLUX-SENSORS-MIB", "voltageSensorDescription"),
        ("PACKETFLUX-SENSORS-MIB", "voltageSensorFunction"),
        ("PACKETFLUX-SENSORS-MIB", "voltageSensorValue"))
)
if mibBuilder.loadTexts:
    packetfluxSensorsMibAllObjects.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "PACKETFLUX-SENSORS-MIB",
    **{"packetfluxSensors": packetfluxSensors,
       "voltageSensorTable": voltageSensorTable,
       "voltageSensorEntry": voltageSensorEntry,
       "voltageSensorSlot": voltageSensorSlot,
       "voltageSensorIndex": voltageSensorIndex,
       "voltageSensorDescription": voltageSensorDescription,
       "voltageSensorValue": voltageSensorValue,
       "voltageSensorFunction": voltageSensorFunction,
       "currentSensorTable": currentSensorTable,
       "currentSensorEntry": currentSensorEntry,
       "currentSensorSlot": currentSensorSlot,
       "currentSensorIndex": currentSensorIndex,
       "currentSensorDescription": currentSensorDescription,
       "currentSensorValue": currentSensorValue,
       "currentSensorFunction": currentSensorFunction,
       "temperatureSensorTable": temperatureSensorTable,
       "temperatureSensorEntry": temperatureSensorEntry,
       "temperatureSensorSlot": temperatureSensorSlot,
       "temperatureSensorIndex": temperatureSensorIndex,
       "temperatureSensorDescription": temperatureSensorDescription,
       "temperatureSensorValue": temperatureSensorValue,
       "temperatureSensorFunction": temperatureSensorFunction,
       "resistanceSensorTable": resistanceSensorTable,
       "resistanceSensorEntry": resistanceSensorEntry,
       "resistanceSensorSlot": resistanceSensorSlot,
       "resistanceSensorIndex": resistanceSensorIndex,
       "resistanceSensorDescription": resistanceSensorDescription,
       "resistanceSensorValue": resistanceSensorValue,
       "resistanceSensorFunction": resistanceSensorFunction,
       "packetfluxSensorsConformance": packetfluxSensorsConformance,
       "packetfluxSensorsGroups": packetfluxSensorsGroups,
       "packetfluxSensorsMibAllObjects": packetfluxSensorsMibAllObjects}
)
