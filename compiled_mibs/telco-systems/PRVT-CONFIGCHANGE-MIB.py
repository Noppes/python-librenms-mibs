# SNMP MIB module (PRVT-CONFIGCHANGE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\telco-systems\binos\PRVT-CONFIGCHANGE-MIB

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

(DisplayString,
 PhysAddress,
 RowPointer,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowPointer",
    "TextualConvention")


# MODULE-IDENTITY

prvtConfigChangeMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 150)
)
if mibBuilder.loadTexts:
    prvtConfigChangeMIB.setRevisions(
        ("2009-07-13 00:00",
         "2006-11-20 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_PrvtConfigChangeNotifications_ObjectIdentity = ObjectIdentity
prvtConfigChangeNotifications = _PrvtConfigChangeNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 150, 0)
)
_PrvtConfigChangeObjects_ObjectIdentity = ObjectIdentity
prvtConfigChangeObjects = _PrvtConfigChangeObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 150, 1)
)
_PrvtConfigChangeAlarmOID_Type = ObjectIdentifier
_PrvtConfigChangeAlarmOID_Object = MibScalar
prvtConfigChangeAlarmOID = _PrvtConfigChangeAlarmOID_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 150, 1, 1),
    _PrvtConfigChangeAlarmOID_Type()
)
prvtConfigChangeAlarmOID.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    prvtConfigChangeAlarmOID.setStatus("current")
_PrvtConfigChangeAlarmRow_Type = RowPointer
_PrvtConfigChangeAlarmRow_Object = MibScalar
prvtConfigChangeAlarmRow = _PrvtConfigChangeAlarmRow_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 150, 1, 2),
    _PrvtConfigChangeAlarmRow_Type()
)
prvtConfigChangeAlarmRow.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    prvtConfigChangeAlarmRow.setStatus("current")
_CliConfigChangeNodePrompt_Type = DisplayString
_CliConfigChangeNodePrompt_Object = MibScalar
cliConfigChangeNodePrompt = _CliConfigChangeNodePrompt_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 150, 1, 3),
    _CliConfigChangeNodePrompt_Type()
)
cliConfigChangeNodePrompt.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cliConfigChangeNodePrompt.setStatus("current")
_CliConfigChangeCommand_Type = DisplayString
_CliConfigChangeCommand_Object = MibScalar
cliConfigChangeCommand = _CliConfigChangeCommand_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 150, 1, 4),
    _CliConfigChangeCommand_Type()
)
cliConfigChangeCommand.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cliConfigChangeCommand.setStatus("current")


class _SnmpServerStatus_Type(Integer32):
    """Custom type snmpServerStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enabled", 1),
          ("disabled", 2))
    )


_SnmpServerStatus_Type.__name__ = "Integer32"
_SnmpServerStatus_Object = MibScalar
snmpServerStatus = _SnmpServerStatus_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 150, 1, 5),
    _SnmpServerStatus_Type()
)
snmpServerStatus.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    snmpServerStatus.setStatus("current")
_PrvtConfigChangeConformance_ObjectIdentity = ObjectIdentity
prvtConfigChangeConformance = _PrvtConfigChangeConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 150, 3)
)

# Managed Objects groups


# Notification objects

prvtConfigChangeAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 150, 0, 1)
)
prvtConfigChangeAlarm.setObjects(
      *(("PRVT-CONFIGCHANGE-MIB", "prvtConfigChangeAlarmOID"),
        ("PRVT-CONFIGCHANGE-MIB", "prvtConfigChangeAlarmRow"))
)
if mibBuilder.loadTexts:
    prvtConfigChangeAlarm.setStatus(
        "current"
    )

cliConfigurationChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 150, 0, 2)
)
cliConfigurationChange.setObjects(
      *(("PRVT-CONFIGCHANGE-MIB", "cliConfigChangeNodePrompt"),
        ("PRVT-CONFIGCHANGE-MIB", "cliConfigChangeCommand"))
)
if mibBuilder.loadTexts:
    cliConfigurationChange.setStatus(
        "current"
    )

snmpServerStatusChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 150, 0, 3)
)
snmpServerStatusChange.setObjects(
    ("PRVT-CONFIGCHANGE-MIB", "snmpServerStatus")
)
if mibBuilder.loadTexts:
    snmpServerStatusChange.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "PRVT-CONFIGCHANGE-MIB",
    **{"prvtConfigChangeMIB": prvtConfigChangeMIB,
       "prvtConfigChangeNotifications": prvtConfigChangeNotifications,
       "prvtConfigChangeAlarm": prvtConfigChangeAlarm,
       "cliConfigurationChange": cliConfigurationChange,
       "snmpServerStatusChange": snmpServerStatusChange,
       "prvtConfigChangeObjects": prvtConfigChangeObjects,
       "prvtConfigChangeAlarmOID": prvtConfigChangeAlarmOID,
       "prvtConfigChangeAlarmRow": prvtConfigChangeAlarmRow,
       "cliConfigChangeNodePrompt": cliConfigChangeNodePrompt,
       "cliConfigChangeCommand": cliConfigChangeCommand,
       "snmpServerStatus": snmpServerStatus,
       "prvtConfigChangeConformance": prvtConfigChangeConformance}
)
