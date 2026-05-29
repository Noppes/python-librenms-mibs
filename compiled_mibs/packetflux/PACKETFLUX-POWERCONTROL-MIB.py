# SNMP MIB module (PACKETFLUX-POWERCONTROL-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\packetflux\PACKETFLUX-POWERCONTROL-MIB

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

(Fixed1DecimalDigit,
 Fixed6DecimalDigits) = mibBuilder.importSymbols(
    "PACKETFLUX-TC",
    "Fixed1DecimalDigit",
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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

packetfluxPowerControl = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 32050, 3, 3)
)
if mibBuilder.loadTexts:
    packetfluxPowerControl.setRevisions(
        ("2018-07-07 12:56",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class TimingPulseStyleEnum(TextualConvention, Integer32):
    status = "current"
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
        *(("notsupported", 1),
          ("unknown", 2),
          ("canopy", 3),
          ("cambium", 4))
    )



# MIB Managed Objects in the order of their OIDs

_PowerControlPortsTable_Object = MibTable
powerControlPortsTable = _PowerControlPortsTable_Object(
    (1, 3, 6, 1, 4, 1, 32050, 3, 3, 1)
)
if mibBuilder.loadTexts:
    powerControlPortsTable.setStatus("current")
_PowerControlPortsEntry_Object = MibTableRow
powerControlPortsEntry = _PowerControlPortsEntry_Object(
    (1, 3, 6, 1, 4, 1, 32050, 3, 3, 1, 1)
)
powerControlPortsEntry.setIndexNames(
    (0, "PACKETFLUX-POWERCONTROL-MIB", "portSlotNumber"),
    (0, "PACKETFLUX-POWERCONTROL-MIB", "portPortNumber"),
)
if mibBuilder.loadTexts:
    powerControlPortsEntry.setStatus("current")
_PortSlotNumber_Type = Unsigned32
_PortSlotNumber_Object = MibTableColumn
portSlotNumber = _PortSlotNumber_Object(
    (1, 3, 6, 1, 4, 1, 32050, 3, 3, 1, 1, 1),
    _PortSlotNumber_Type()
)
portSlotNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    portSlotNumber.setStatus("current")
_PortPortNumber_Type = Unsigned32
_PortPortNumber_Object = MibTableColumn
portPortNumber = _PortPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 32050, 3, 3, 1, 1, 2),
    _PortPortNumber_Type()
)
portPortNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    portPortNumber.setStatus("current")
_PortDescription_Type = DisplayString
_PortDescription_Object = MibTableColumn
portDescription = _PortDescription_Object(
    (1, 3, 6, 1, 4, 1, 32050, 3, 3, 1, 1, 3),
    _PortDescription_Type()
)
portDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portDescription.setStatus("current")
_PortPowerEnabled_Type = TruthValue
_PortPowerEnabled_Object = MibTableColumn
portPowerEnabled = _PortPowerEnabled_Object(
    (1, 3, 6, 1, 4, 1, 32050, 3, 3, 1, 1, 4),
    _PortPowerEnabled_Type()
)
portPowerEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portPowerEnabled.setStatus("current")
_PortPowerTripped_Type = TruthValue
_PortPowerTripped_Object = MibTableColumn
portPowerTripped = _PortPowerTripped_Object(
    (1, 3, 6, 1, 4, 1, 32050, 3, 3, 1, 1, 5),
    _PortPowerTripped_Type()
)
portPowerTripped.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portPowerTripped.setStatus("current")
_PortCycleTimeout_Type = Fixed1DecimalDigit
_PortCycleTimeout_Object = MibTableColumn
portCycleTimeout = _PortCycleTimeout_Object(
    (1, 3, 6, 1, 4, 1, 32050, 3, 3, 1, 1, 6),
    _PortCycleTimeout_Type()
)
portCycleTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portCycleTimeout.setStatus("current")
if mibBuilder.loadTexts:
    portCycleTimeout.setUnits("S")
_PortPowerEnabledAtReset_Type = TruthValue
_PortPowerEnabledAtReset_Object = MibTableColumn
portPowerEnabledAtReset = _PortPowerEnabledAtReset_Object(
    (1, 3, 6, 1, 4, 1, 32050, 3, 3, 1, 1, 7),
    _PortPowerEnabledAtReset_Type()
)
portPowerEnabledAtReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portPowerEnabledAtReset.setStatus("current")
_PortTimingPulseEnabled_Type = TruthValue
_PortTimingPulseEnabled_Object = MibTableColumn
portTimingPulseEnabled = _PortTimingPulseEnabled_Object(
    (1, 3, 6, 1, 4, 1, 32050, 3, 3, 1, 1, 8),
    _PortTimingPulseEnabled_Type()
)
portTimingPulseEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portTimingPulseEnabled.setStatus("current")
_PortTimingPulseEnabledAtReset_Type = TruthValue
_PortTimingPulseEnabledAtReset_Object = MibTableColumn
portTimingPulseEnabledAtReset = _PortTimingPulseEnabledAtReset_Object(
    (1, 3, 6, 1, 4, 1, 32050, 3, 3, 1, 1, 9),
    _PortTimingPulseEnabledAtReset_Type()
)
portTimingPulseEnabledAtReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portTimingPulseEnabledAtReset.setStatus("current")
_PortTimingPulseStyle_Type = TimingPulseStyleEnum
_PortTimingPulseStyle_Object = MibTableColumn
portTimingPulseStyle = _PortTimingPulseStyle_Object(
    (1, 3, 6, 1, 4, 1, 32050, 3, 3, 1, 1, 10),
    _PortTimingPulseStyle_Type()
)
portTimingPulseStyle.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portTimingPulseStyle.setStatus("current")
_PortOutputVoltage_Type = Fixed6DecimalDigits
_PortOutputVoltage_Object = MibTableColumn
portOutputVoltage = _PortOutputVoltage_Object(
    (1, 3, 6, 1, 4, 1, 32050, 3, 3, 1, 1, 11),
    _PortOutputVoltage_Type()
)
portOutputVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portOutputVoltage.setStatus("current")
if mibBuilder.loadTexts:
    portOutputVoltage.setUnits("V")
_PortCurrent_Type = Fixed6DecimalDigits
_PortCurrent_Object = MibTableColumn
portCurrent = _PortCurrent_Object(
    (1, 3, 6, 1, 4, 1, 32050, 3, 3, 1, 1, 12),
    _PortCurrent_Type()
)
portCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portCurrent.setStatus("current")
if mibBuilder.loadTexts:
    portCurrent.setUnits("A")
_PortNumberOfPowerTransitions_Type = Counter32
_PortNumberOfPowerTransitions_Object = MibTableColumn
portNumberOfPowerTransitions = _PortNumberOfPowerTransitions_Object(
    (1, 3, 6, 1, 4, 1, 32050, 3, 3, 1, 1, 13),
    _PortNumberOfPowerTransitions_Type()
)
portNumberOfPowerTransitions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portNumberOfPowerTransitions.setStatus("current")
_PortNumberOfTripEvents_Type = Counter32
_PortNumberOfTripEvents_Object = MibTableColumn
portNumberOfTripEvents = _PortNumberOfTripEvents_Object(
    (1, 3, 6, 1, 4, 1, 32050, 3, 3, 1, 1, 14),
    _PortNumberOfTripEvents_Type()
)
portNumberOfTripEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portNumberOfTripEvents.setStatus("current")
_PacketfluxPowerControlConformance_ObjectIdentity = ObjectIdentity
packetfluxPowerControlConformance = _PacketfluxPowerControlConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 32050, 3, 3, 127)
)
_PacketfluxPowerControlGroups_ObjectIdentity = ObjectIdentity
packetfluxPowerControlGroups = _PacketfluxPowerControlGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 32050, 3, 3, 127, 1)
)

# Managed Objects groups

packetfluxPowerControlAllObjects = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 32050, 3, 3, 127, 1, 1)
)
packetfluxPowerControlAllObjects.setObjects(
      *(("PACKETFLUX-POWERCONTROL-MIB", "portCurrent"),
        ("PACKETFLUX-POWERCONTROL-MIB", "portCycleTimeout"),
        ("PACKETFLUX-POWERCONTROL-MIB", "portDescription"),
        ("PACKETFLUX-POWERCONTROL-MIB", "portNumberOfPowerTransitions"),
        ("PACKETFLUX-POWERCONTROL-MIB", "portNumberOfTripEvents"),
        ("PACKETFLUX-POWERCONTROL-MIB", "portOutputVoltage"),
        ("PACKETFLUX-POWERCONTROL-MIB", "portPowerEnabled"),
        ("PACKETFLUX-POWERCONTROL-MIB", "portPowerEnabledAtReset"),
        ("PACKETFLUX-POWERCONTROL-MIB", "portPowerTripped"),
        ("PACKETFLUX-POWERCONTROL-MIB", "portTimingPulseEnabled"),
        ("PACKETFLUX-POWERCONTROL-MIB", "portTimingPulseEnabledAtReset"),
        ("PACKETFLUX-POWERCONTROL-MIB", "portTimingPulseStyle"))
)
if mibBuilder.loadTexts:
    packetfluxPowerControlAllObjects.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "PACKETFLUX-POWERCONTROL-MIB",
    **{"TimingPulseStyleEnum": TimingPulseStyleEnum,
       "packetfluxPowerControl": packetfluxPowerControl,
       "powerControlPortsTable": powerControlPortsTable,
       "powerControlPortsEntry": powerControlPortsEntry,
       "portSlotNumber": portSlotNumber,
       "portPortNumber": portPortNumber,
       "portDescription": portDescription,
       "portPowerEnabled": portPowerEnabled,
       "portPowerTripped": portPowerTripped,
       "portCycleTimeout": portCycleTimeout,
       "portPowerEnabledAtReset": portPowerEnabledAtReset,
       "portTimingPulseEnabled": portTimingPulseEnabled,
       "portTimingPulseEnabledAtReset": portTimingPulseEnabledAtReset,
       "portTimingPulseStyle": portTimingPulseStyle,
       "portOutputVoltage": portOutputVoltage,
       "portCurrent": portCurrent,
       "portNumberOfPowerTransitions": portNumberOfPowerTransitions,
       "portNumberOfTripEvents": portNumberOfTripEvents,
       "packetfluxPowerControlConformance": packetfluxPowerControlConformance,
       "packetfluxPowerControlGroups": packetfluxPowerControlGroups,
       "packetfluxPowerControlAllObjects": packetfluxPowerControlAllObjects}
)
