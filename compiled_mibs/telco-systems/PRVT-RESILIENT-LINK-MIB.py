# SNMP MIB module (PRVT-RESILIENT-LINK-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\telco-systems\binos\PRVT-RESILIENT-LINK-MIB

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

prvtResilientLinkMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 102)
)
if mibBuilder.loadTexts:
    prvtResilientLinkMib.setRevisions(
        ("2005-02-16 00:00",
         "2003-05-06 00:00",
         "2002-01-28 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_PrvtResilientLinkNotifications_ObjectIdentity = ObjectIdentity
prvtResilientLinkNotifications = _PrvtResilientLinkNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 102, 0)
)
_ResilientLinkConfig_ObjectIdentity = ObjectIdentity
resilientLinkConfig = _ResilientLinkConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 102, 1)
)
_ResilientLinkConfigTable_Object = MibTable
resilientLinkConfigTable = _ResilientLinkConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 102, 1, 1)
)
if mibBuilder.loadTexts:
    resilientLinkConfigTable.setStatus("current")
_ResilientLinkConfigEntry_Object = MibTableRow
resilientLinkConfigEntry = _ResilientLinkConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 102, 1, 1, 1)
)
resilientLinkConfigEntry.setIndexNames(
    (0, "PRVT-RESILIENT-LINK-MIB", "resilientLinkIndex"),
)
if mibBuilder.loadTexts:
    resilientLinkConfigEntry.setStatus("current")


class _ResilientLinkIndex_Type(Integer32):
    """Custom type resilientLinkIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 256),
    )


_ResilientLinkIndex_Type.__name__ = "Integer32"
_ResilientLinkIndex_Object = MibTableColumn
resilientLinkIndex = _ResilientLinkIndex_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 102, 1, 1, 1, 1),
    _ResilientLinkIndex_Type()
)
resilientLinkIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    resilientLinkIndex.setStatus("current")


class _ResilientLinkEnable_Type(Integer32):
    """Custom type resilientLinkEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_ResilientLinkEnable_Type.__name__ = "Integer32"
_ResilientLinkEnable_Object = MibTableColumn
resilientLinkEnable = _ResilientLinkEnable_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 102, 1, 1, 1, 2),
    _ResilientLinkEnable_Type()
)
resilientLinkEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    resilientLinkEnable.setStatus("current")
_ResilientLinkPort1ifIndex_Type = Integer32
_ResilientLinkPort1ifIndex_Object = MibTableColumn
resilientLinkPort1ifIndex = _ResilientLinkPort1ifIndex_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 102, 1, 1, 1, 3),
    _ResilientLinkPort1ifIndex_Type()
)
resilientLinkPort1ifIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    resilientLinkPort1ifIndex.setStatus("current")
_ResilientLinkPort2ifIndex_Type = Integer32
_ResilientLinkPort2ifIndex_Object = MibTableColumn
resilientLinkPort2ifIndex = _ResilientLinkPort2ifIndex_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 102, 1, 1, 1, 4),
    _ResilientLinkPort2ifIndex_Type()
)
resilientLinkPort2ifIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    resilientLinkPort2ifIndex.setStatus("current")
_ResilientLinkPreferredPort_Type = Integer32
_ResilientLinkPreferredPort_Object = MibTableColumn
resilientLinkPreferredPort = _ResilientLinkPreferredPort_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 102, 1, 1, 1, 5),
    _ResilientLinkPreferredPort_Type()
)
resilientLinkPreferredPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    resilientLinkPreferredPort.setStatus("current")
_ResilientLinkActivePort_Type = Integer32
_ResilientLinkActivePort_Object = MibTableColumn
resilientLinkActivePort = _ResilientLinkActivePort_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 102, 1, 1, 1, 6),
    _ResilientLinkActivePort_Type()
)
resilientLinkActivePort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    resilientLinkActivePort.setStatus("current")
_ResilientLinkStatus_ObjectIdentity = ObjectIdentity
resilientLinkStatus = _ResilientLinkStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 102, 2)
)
_ResilientLinkStatusTable_Object = MibTable
resilientLinkStatusTable = _ResilientLinkStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 102, 2, 2)
)
if mibBuilder.loadTexts:
    resilientLinkStatusTable.setStatus("current")
_ResilientLinkStatusEntry_Object = MibTableRow
resilientLinkStatusEntry = _ResilientLinkStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 102, 2, 2, 1)
)
resilientLinkStatusEntry.setIndexNames(
    (0, "PRVT-RESILIENT-LINK-MIB", "resilientLinkIndex"),
)
if mibBuilder.loadTexts:
    resilientLinkStatusEntry.setStatus("current")


class _ResilientLinkConnectedPort_Type(Integer32):
    """Custom type resilientLinkConnectedPort based on Integer32"""
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
        *(("notConnected", 1),
          ("port1Connected", 2),
          ("port2Connected", 3),
          ("port1and2Connected", 4))
    )


_ResilientLinkConnectedPort_Type.__name__ = "Integer32"
_ResilientLinkConnectedPort_Object = MibTableColumn
resilientLinkConnectedPort = _ResilientLinkConnectedPort_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 102, 2, 2, 1, 1),
    _ResilientLinkConnectedPort_Type()
)
resilientLinkConnectedPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    resilientLinkConnectedPort.setStatus("current")


class _ResilientLinkCurrentActivePort_Type(Integer32):
    """Custom type resilientLinkCurrentActivePort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("noActivePort", 1),
          ("port1Active", 2),
          ("port2Active", 3))
    )


_ResilientLinkCurrentActivePort_Type.__name__ = "Integer32"
_ResilientLinkCurrentActivePort_Object = MibTableColumn
resilientLinkCurrentActivePort = _ResilientLinkCurrentActivePort_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 102, 2, 2, 1, 2),
    _ResilientLinkCurrentActivePort_Type()
)
resilientLinkCurrentActivePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    resilientLinkCurrentActivePort.setStatus("current")
_PrvtResilientLinkConformance_ObjectIdentity = ObjectIdentity
prvtResilientLinkConformance = _PrvtResilientLinkConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 102, 3)
)
_PrvtResilientLinkMIBGroups_ObjectIdentity = ObjectIdentity
prvtResilientLinkMIBGroups = _PrvtResilientLinkMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 102, 3, 2)
)

# Managed Objects groups


# Notification objects

resilientLinkStatusChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 102, 0, 1)
)
resilientLinkStatusChange.setObjects(
      *(("PRVT-RESILIENT-LINK-MIB", "resilientLinkIndex"),
        ("PRVT-RESILIENT-LINK-MIB", "resilientLinkConnectedPort"),
        ("PRVT-RESILIENT-LINK-MIB", "resilientLinkCurrentActivePort"))
)
if mibBuilder.loadTexts:
    resilientLinkStatusChange.setStatus(
        "current"
    )


# Notifications groups

resilientLinkNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 102, 3, 2, 3)
)
resilientLinkNotificationGroup.setObjects(
    ("PRVT-RESILIENT-LINK-MIB", "resilientLinkStatusChange")
)
if mibBuilder.loadTexts:
    resilientLinkNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "PRVT-RESILIENT-LINK-MIB",
    **{"prvtResilientLinkMib": prvtResilientLinkMib,
       "prvtResilientLinkNotifications": prvtResilientLinkNotifications,
       "resilientLinkStatusChange": resilientLinkStatusChange,
       "resilientLinkConfig": resilientLinkConfig,
       "resilientLinkConfigTable": resilientLinkConfigTable,
       "resilientLinkConfigEntry": resilientLinkConfigEntry,
       "resilientLinkIndex": resilientLinkIndex,
       "resilientLinkEnable": resilientLinkEnable,
       "resilientLinkPort1ifIndex": resilientLinkPort1ifIndex,
       "resilientLinkPort2ifIndex": resilientLinkPort2ifIndex,
       "resilientLinkPreferredPort": resilientLinkPreferredPort,
       "resilientLinkActivePort": resilientLinkActivePort,
       "resilientLinkStatus": resilientLinkStatus,
       "resilientLinkStatusTable": resilientLinkStatusTable,
       "resilientLinkStatusEntry": resilientLinkStatusEntry,
       "resilientLinkConnectedPort": resilientLinkConnectedPort,
       "resilientLinkCurrentActivePort": resilientLinkCurrentActivePort,
       "prvtResilientLinkConformance": prvtResilientLinkConformance,
       "prvtResilientLinkMIBGroups": prvtResilientLinkMIBGroups,
       "resilientLinkNotificationGroup": resilientLinkNotificationGroup}
)
