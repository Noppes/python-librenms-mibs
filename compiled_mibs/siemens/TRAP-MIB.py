# SNMP MIB module (TRAP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\siemens\TRAP-MIB

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
 NotificationType,
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
    "NotificationType",
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

(agtConnectedDevice,
 agtPortIndex,
 agtSWVersion,
 deviceLinkAlarm,
 deviceLinkIndex,
 deviceLinkName,
 devicePortIndex) = mibBuilder.importSymbols(
    "ULAF2-MIB",
    "agtConnectedDevice",
    "agtPortIndex",
    "agtSWVersion",
    "deviceLinkAlarm",
    "deviceLinkIndex",
    "deviceLinkName",
    "devicePortIndex")

(cmrwLocalTokenTicket,
 extendedTrapsType) = mibBuilder.importSymbols(
    "ULAFPLUS-MIB",
    "cmrwLocalTokenTicket",
    "extendedTrapsType")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs


# Managed Objects groups


# Notification objects

warmStart = NotificationType(
    (1, 3, 6, 1, 4, 1, 1887, 1, 1, 1, 2, 1, 1, 0, 17)
)
warmStart.setObjects(
    ("ULAF2-MIB", "agtSWVersion")
)
if mibBuilder.loadTexts:
    warmStart.setStatus(
        ""
    )

deviceLinkDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 1887, 1, 1, 1, 2, 2, 2, 1, 1, 0, 12)
)
deviceLinkDown.setObjects(
    ("ULAF2-MIB", "agtPortIndex")
)
if mibBuilder.loadTexts:
    deviceLinkDown.setStatus(
        ""
    )

deviceLinkUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 1887, 1, 1, 1, 2, 2, 2, 1, 1, 0, 13)
)
deviceLinkUp.setObjects(
      *(("ULAF2-MIB", "agtPortIndex"),
        ("ULAF2-MIB", "agtConnectedDevice"))
)
if mibBuilder.loadTexts:
    deviceLinkUp.setStatus(
        ""
    )

lineLinkDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 1887, 1, 1, 3, 2, 2, 1, 1, 1, 0, 10)
)
lineLinkDown.setObjects(
      *(("ULAF2-MIB", "devicePortIndex"),
        ("ULAF2-MIB", "deviceLinkIndex"))
)
if mibBuilder.loadTexts:
    lineLinkDown.setStatus(
        ""
    )

lineLinkUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 1887, 1, 1, 3, 2, 2, 1, 1, 1, 0, 11)
)
lineLinkUp.setObjects(
      *(("ULAF2-MIB", "devicePortIndex"),
        ("ULAF2-MIB", "deviceLinkIndex"),
        ("ULAF2-MIB", "deviceLinkName"),
        ("ULAF2-MIB", "deviceLinkAlarm"))
)
if mibBuilder.loadTexts:
    lineLinkUp.setStatus(
        ""
    )

urgentAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 1887, 1, 1, 3, 2, 2, 1, 1, 1, 0, 18)
)
urgentAlarm.setObjects(
      *(("ULAF2-MIB", "devicePortIndex"),
        ("ULAF2-MIB", "deviceLinkIndex"),
        ("ULAF2-MIB", "deviceLinkAlarm"))
)
if mibBuilder.loadTexts:
    urgentAlarm.setStatus(
        ""
    )

nonUrgentAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 1887, 1, 1, 3, 2, 2, 1, 1, 1, 0, 19)
)
nonUrgentAlarm.setObjects(
      *(("ULAF2-MIB", "devicePortIndex"),
        ("ULAF2-MIB", "deviceLinkIndex"),
        ("ULAF2-MIB", "deviceLinkAlarm"))
)
if mibBuilder.loadTexts:
    nonUrgentAlarm.setStatus(
        ""
    )

noAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 1887, 1, 1, 3, 2, 2, 1, 1, 1, 0, 22)
)
noAlarm.setObjects(
      *(("ULAF2-MIB", "devicePortIndex"),
        ("ULAF2-MIB", "deviceLinkIndex"),
        ("ULAF2-MIB", "deviceLinkAlarm"))
)
if mibBuilder.loadTexts:
    noAlarm.setStatus(
        ""
    )

loopChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 1887, 1, 1, 3, 2, 2, 1, 1, 1, 0, 25)
)
loopChange.setObjects(
      *(("ULAF2-MIB", "devicePortIndex"),
        ("ULAF2-MIB", "deviceLinkIndex"))
)
if mibBuilder.loadTexts:
    loopChange.setStatus(
        ""
    )

accessChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 1887, 1, 1, 3, 2, 2, 1, 1, 1, 0, 26)
)
accessChange.setObjects(
      *(("ULAF2-MIB", "devicePortIndex"),
        ("ULAF2-MIB", "deviceLinkIndex"),
        ("ULAFPLUS-MIB", "cmrwLocalTokenTicket"))
)
if mibBuilder.loadTexts:
    accessChange.setStatus(
        ""
    )

perform15min = NotificationType(
    (1, 3, 6, 1, 4, 1, 1887, 1, 1, 3, 2, 2, 1, 1, 1, 0, 27)
)
perform15min.setObjects(
      *(("ULAF2-MIB", "devicePortIndex"),
        ("ULAF2-MIB", "deviceLinkIndex"))
)
if mibBuilder.loadTexts:
    perform15min.setStatus(
        ""
    )

perform24h = NotificationType(
    (1, 3, 6, 1, 4, 1, 1887, 1, 1, 3, 2, 2, 1, 1, 1, 0, 28)
)
perform24h.setObjects(
      *(("ULAF2-MIB", "devicePortIndex"),
        ("ULAF2-MIB", "deviceLinkIndex"))
)
if mibBuilder.loadTexts:
    perform24h.setStatus(
        ""
    )

rebootPlus = NotificationType(
    (1, 3, 6, 1, 4, 1, 1887, 1, 1, 3, 2, 2, 1, 1, 1, 0, 29)
)
rebootPlus.setObjects(
      *(("ULAF2-MIB", "devicePortIndex"),
        ("ULAF2-MIB", "deviceLinkIndex"))
)
if mibBuilder.loadTexts:
    rebootPlus.setStatus(
        ""
    )

berMeasurement = NotificationType(
    (1, 3, 6, 1, 4, 1, 1887, 1, 1, 3, 2, 2, 1, 1, 1, 0, 30)
)
berMeasurement.setObjects(
      *(("ULAF2-MIB", "devicePortIndex"),
        ("ULAF2-MIB", "deviceLinkIndex"))
)
if mibBuilder.loadTexts:
    berMeasurement.setStatus(
        ""
    )

flashErased = NotificationType(
    (1, 3, 6, 1, 4, 1, 1887, 1, 1, 3, 2, 2, 1, 1, 1, 0, 31)
)
flashErased.setObjects(
      *(("ULAF2-MIB", "devicePortIndex"),
        ("ULAF2-MIB", "deviceLinkIndex"))
)
if mibBuilder.loadTexts:
    flashErased.setStatus(
        ""
    )

extendedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 1887, 1, 1, 3, 2, 2, 1, 1, 1, 0, 32)
)
extendedTrap.setObjects(
      *(("ULAF2-MIB", "devicePortIndex"),
        ("ULAF2-MIB", "deviceLinkIndex"),
        ("ULAFPLUS-MIB", "extendedTrapsType"))
)
if mibBuilder.loadTexts:
    extendedTrap.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TRAP-MIB",
    **{"warmStart": warmStart,
       "deviceLinkDown": deviceLinkDown,
       "deviceLinkUp": deviceLinkUp,
       "lineLinkDown": lineLinkDown,
       "lineLinkUp": lineLinkUp,
       "urgentAlarm": urgentAlarm,
       "nonUrgentAlarm": nonUrgentAlarm,
       "noAlarm": noAlarm,
       "loopChange": loopChange,
       "accessChange": accessChange,
       "perform15min": perform15min,
       "perform24h": perform24h,
       "rebootPlus": rebootPlus,
       "berMeasurement": berMeasurement,
       "flashErased": flashErased,
       "extendedTrap": extendedTrap}
)
