# SNMP MIB module (AX-SMCSERVICE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\alaxala\AX-SMCSERVICE-MIB

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

(axMib,) = mibBuilder.importSymbols(
    "AX-SMI-MIB",
    "axMib")

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

axSmcServiceInformation = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 1003)
)
if mibBuilder.loadTexts:
    axSmcServiceInformation.setRevisions(
        ("2014-11-14 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AxSmcServiceTable_Object = MibTable
axSmcServiceTable = _AxSmcServiceTable_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 1003, 1)
)
if mibBuilder.loadTexts:
    axSmcServiceTable.setStatus("current")
_AxSmcServiceEntry_Object = MibTableRow
axSmcServiceEntry = _AxSmcServiceEntry_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 1003, 1, 1)
)
axSmcServiceEntry.setIndexNames(
    (0, "AX-SMCSERVICE-MIB", "axSmcServiceId"),
)
if mibBuilder.loadTexts:
    axSmcServiceEntry.setStatus("current")
_AxSmcServiceId_Type = Integer32
_AxSmcServiceId_Object = MibTableColumn
axSmcServiceId = _AxSmcServiceId_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 1003, 1, 1, 1),
    _AxSmcServiceId_Type()
)
axSmcServiceId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axSmcServiceId.setStatus("current")
_AxSmcServiceName_Type = DisplayString
_AxSmcServiceName_Object = MibTableColumn
axSmcServiceName = _AxSmcServiceName_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 1003, 1, 1, 2),
    _AxSmcServiceName_Type()
)
axSmcServiceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axSmcServiceName.setStatus("current")
_AxSmcServiceNifNo_Type = Integer32
_AxSmcServiceNifNo_Object = MibTableColumn
axSmcServiceNifNo = _AxSmcServiceNifNo_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 1003, 1, 1, 3),
    _AxSmcServiceNifNo_Type()
)
axSmcServiceNifNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axSmcServiceNifNo.setStatus("current")
_AxSmcServiceType_Type = DisplayString
_AxSmcServiceType_Object = MibTableColumn
axSmcServiceType = _AxSmcServiceType_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 1003, 1, 1, 4),
    _AxSmcServiceType_Type()
)
axSmcServiceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axSmcServiceType.setStatus("current")
_AxSmcServiceAttachedGroupId_Type = Integer32
_AxSmcServiceAttachedGroupId_Object = MibTableColumn
axSmcServiceAttachedGroupId = _AxSmcServiceAttachedGroupId_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 1003, 1, 1, 5),
    _AxSmcServiceAttachedGroupId_Type()
)
axSmcServiceAttachedGroupId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axSmcServiceAttachedGroupId.setStatus("current")
_AxSmcServiceAttachedGroupName_Type = DisplayString
_AxSmcServiceAttachedGroupName_Object = MibTableColumn
axSmcServiceAttachedGroupName = _AxSmcServiceAttachedGroupName_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 1003, 1, 1, 6),
    _AxSmcServiceAttachedGroupName_Type()
)
axSmcServiceAttachedGroupName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axSmcServiceAttachedGroupName.setStatus("current")


class _AxSmcServiceStatus_Type(Integer32):
    """Custom type axSmcServiceStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              99)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("standby", 2),
          ("outOfService", 3),
          ("unknown", 99))
    )


_AxSmcServiceStatus_Type.__name__ = "Integer32"
_AxSmcServiceStatus_Object = MibTableColumn
axSmcServiceStatus = _AxSmcServiceStatus_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 1003, 1, 1, 7),
    _AxSmcServiceStatus_Type()
)
axSmcServiceStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axSmcServiceStatus.setStatus("current")
_AxSmcServiceUpTime_Type = DisplayString
_AxSmcServiceUpTime_Object = MibTableColumn
axSmcServiceUpTime = _AxSmcServiceUpTime_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 1003, 1, 1, 8),
    _AxSmcServiceUpTime_Type()
)
axSmcServiceUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axSmcServiceUpTime.setStatus("current")
_AxSmcServiceGroupTable_Object = MibTable
axSmcServiceGroupTable = _AxSmcServiceGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 1003, 2)
)
if mibBuilder.loadTexts:
    axSmcServiceGroupTable.setStatus("current")
_AxSmcServiceGroupEntry_Object = MibTableRow
axSmcServiceGroupEntry = _AxSmcServiceGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 1003, 2, 1)
)
axSmcServiceGroupEntry.setIndexNames(
    (0, "AX-SMCSERVICE-MIB", "axSmcServiceGroupId"),
)
if mibBuilder.loadTexts:
    axSmcServiceGroupEntry.setStatus("current")
_AxSmcServiceGroupId_Type = Integer32
_AxSmcServiceGroupId_Object = MibTableColumn
axSmcServiceGroupId = _AxSmcServiceGroupId_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 1003, 2, 1, 1),
    _AxSmcServiceGroupId_Type()
)
axSmcServiceGroupId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axSmcServiceGroupId.setStatus("current")
_AxSmcServiceGroupName_Type = DisplayString
_AxSmcServiceGroupName_Object = MibTableColumn
axSmcServiceGroupName = _AxSmcServiceGroupName_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 1003, 2, 1, 2),
    _AxSmcServiceGroupName_Type()
)
axSmcServiceGroupName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axSmcServiceGroupName.setStatus("current")


class _AxSmcServiceGroupRedundancyType_Type(Integer32):
    """Custom type axSmcServiceGroupRedundancyType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              99)
        )
    )
    namedValues = NamedValues(
        *(("allActive", 1),
          ("activeStandby", 2),
          ("unknown", 99))
    )


_AxSmcServiceGroupRedundancyType_Type.__name__ = "Integer32"
_AxSmcServiceGroupRedundancyType_Object = MibTableColumn
axSmcServiceGroupRedundancyType = _AxSmcServiceGroupRedundancyType_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 1003, 2, 1, 3),
    _AxSmcServiceGroupRedundancyType_Type()
)
axSmcServiceGroupRedundancyType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axSmcServiceGroupRedundancyType.setStatus("current")
_AxSmcServiceGroupAttachedApplicationId_Type = Integer32
_AxSmcServiceGroupAttachedApplicationId_Object = MibTableColumn
axSmcServiceGroupAttachedApplicationId = _AxSmcServiceGroupAttachedApplicationId_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 1003, 2, 1, 4),
    _AxSmcServiceGroupAttachedApplicationId_Type()
)
axSmcServiceGroupAttachedApplicationId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axSmcServiceGroupAttachedApplicationId.setStatus("current")
_AxSmcServiceGroupAttachedApplicationName_Type = DisplayString
_AxSmcServiceGroupAttachedApplicationName_Object = MibTableColumn
axSmcServiceGroupAttachedApplicationName = _AxSmcServiceGroupAttachedApplicationName_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 1003, 2, 1, 5),
    _AxSmcServiceGroupAttachedApplicationName_Type()
)
axSmcServiceGroupAttachedApplicationName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axSmcServiceGroupAttachedApplicationName.setStatus("current")


class _AxSmcServiceGroupRedundancyStatus_Type(Integer32):
    """Custom type axSmcServiceGroupRedundancyStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              99)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 1),
          ("duplex", 2),
          ("simplex", 3),
          ("unknown", 99))
    )


_AxSmcServiceGroupRedundancyStatus_Type.__name__ = "Integer32"
_AxSmcServiceGroupRedundancyStatus_Object = MibTableColumn
axSmcServiceGroupRedundancyStatus = _AxSmcServiceGroupRedundancyStatus_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 1003, 2, 1, 6),
    _AxSmcServiceGroupRedundancyStatus_Type()
)
axSmcServiceGroupRedundancyStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axSmcServiceGroupRedundancyStatus.setStatus("current")
_AxSmcApplicationTable_Object = MibTable
axSmcApplicationTable = _AxSmcApplicationTable_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 1003, 3)
)
if mibBuilder.loadTexts:
    axSmcApplicationTable.setStatus("current")
_AxSmcApplicationEntry_Object = MibTableRow
axSmcApplicationEntry = _AxSmcApplicationEntry_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 1003, 3, 1)
)
axSmcApplicationEntry.setIndexNames(
    (0, "AX-SMCSERVICE-MIB", "axSmcApplicationId"),
)
if mibBuilder.loadTexts:
    axSmcApplicationEntry.setStatus("current")
_AxSmcApplicationId_Type = Integer32
_AxSmcApplicationId_Object = MibTableColumn
axSmcApplicationId = _AxSmcApplicationId_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 1003, 3, 1, 1),
    _AxSmcApplicationId_Type()
)
axSmcApplicationId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axSmcApplicationId.setStatus("current")
_AxSmcApplicationName_Type = DisplayString
_AxSmcApplicationName_Object = MibTableColumn
axSmcApplicationName = _AxSmcApplicationName_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 1003, 3, 1, 2),
    _AxSmcApplicationName_Type()
)
axSmcApplicationName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axSmcApplicationName.setStatus("current")
_AxSmcServiceTraps_ObjectIdentity = ObjectIdentity
axSmcServiceTraps = _AxSmcServiceTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 1003, 4)
)
_AxSmcServiceTrapsPrefix_ObjectIdentity = ObjectIdentity
axSmcServiceTrapsPrefix = _AxSmcServiceTrapsPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 1003, 4, 0)
)
_AxSmcConformance_ObjectIdentity = ObjectIdentity
axSmcConformance = _AxSmcConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 1003, 1000)
)
_AxSmcCompliances_ObjectIdentity = ObjectIdentity
axSmcCompliances = _AxSmcCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 1003, 1000, 1)
)
_AxSmcGroups_ObjectIdentity = ObjectIdentity
axSmcGroups = _AxSmcGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 1003, 1000, 2)
)

# Managed Objects groups

axSmcGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 1003, 1000, 2, 1)
)
axSmcGroup.setObjects(
      *(("AX-SMCSERVICE-MIB", "axSmcServiceId"),
        ("AX-SMCSERVICE-MIB", "axSmcServiceName"),
        ("AX-SMCSERVICE-MIB", "axSmcServiceNifNo"),
        ("AX-SMCSERVICE-MIB", "axSmcServiceType"),
        ("AX-SMCSERVICE-MIB", "axSmcServiceAttachedGroupId"),
        ("AX-SMCSERVICE-MIB", "axSmcServiceAttachedGroupName"),
        ("AX-SMCSERVICE-MIB", "axSmcServiceStatus"),
        ("AX-SMCSERVICE-MIB", "axSmcServiceUpTime"),
        ("AX-SMCSERVICE-MIB", "axSmcServiceGroupId"),
        ("AX-SMCSERVICE-MIB", "axSmcServiceGroupName"),
        ("AX-SMCSERVICE-MIB", "axSmcServiceGroupRedundancyType"),
        ("AX-SMCSERVICE-MIB", "axSmcServiceGroupAttachedApplicationId"),
        ("AX-SMCSERVICE-MIB", "axSmcServiceGroupAttachedApplicationName"),
        ("AX-SMCSERVICE-MIB", "axSmcServiceGroupRedundancyStatus"),
        ("AX-SMCSERVICE-MIB", "axSmcApplicationId"),
        ("AX-SMCSERVICE-MIB", "axSmcApplicationName"))
)
if mibBuilder.loadTexts:
    axSmcGroup.setStatus("current")


# Notification objects

axSmcServiceStateChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 1003, 4, 0, 1)
)
axSmcServiceStateChange.setObjects(
      *(("AX-SMCSERVICE-MIB", "axSmcServiceId"),
        ("AX-SMCSERVICE-MIB", "axSmcServiceName"),
        ("AX-SMCSERVICE-MIB", "axSmcServiceStatus"))
)
if mibBuilder.loadTexts:
    axSmcServiceStateChange.setStatus(
        "current"
    )

axSmcServiceGroupDuplexToSimplexTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 1003, 4, 0, 2)
)
axSmcServiceGroupDuplexToSimplexTrap.setObjects(
      *(("AX-SMCSERVICE-MIB", "axSmcServiceGroupId"),
        ("AX-SMCSERVICE-MIB", "axSmcServiceGroupName"))
)
if mibBuilder.loadTexts:
    axSmcServiceGroupDuplexToSimplexTrap.setStatus(
        "current"
    )

axSmcServiceGroupSimplexToDuplexTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 1003, 4, 0, 3)
)
axSmcServiceGroupSimplexToDuplexTrap.setObjects(
      *(("AX-SMCSERVICE-MIB", "axSmcServiceGroupId"),
        ("AX-SMCSERVICE-MIB", "axSmcServiceGroupName"))
)
if mibBuilder.loadTexts:
    axSmcServiceGroupSimplexToDuplexTrap.setStatus(
        "current"
    )

axSmcServiceGroupSwitchOver = NotificationType(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 1003, 4, 0, 4)
)
axSmcServiceGroupSwitchOver.setObjects(
      *(("AX-SMCSERVICE-MIB", "axSmcServiceGroupId"),
        ("AX-SMCSERVICE-MIB", "axSmcServiceGroupName"))
)
if mibBuilder.loadTexts:
    axSmcServiceGroupSwitchOver.setStatus(
        "current"
    )


# Notifications groups

axSmcTrapGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 1003, 1000, 2, 10)
)
axSmcTrapGroup.setObjects(
      *(("AX-SMCSERVICE-MIB", "axSmcServiceStateChange"),
        ("AX-SMCSERVICE-MIB", "axSmcServiceGroupDuplexToSimplexTrap"),
        ("AX-SMCSERVICE-MIB", "axSmcServiceGroupSimplexToDuplexTrap"),
        ("AX-SMCSERVICE-MIB", "axSmcServiceGroupSwitchOver"))
)
if mibBuilder.loadTexts:
    axSmcTrapGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

axSmcCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 1003, 1000, 1, 1)
)
axSmcCompliance.setObjects(
      *(("AX-SMCSERVICE-MIB", "axSmcGroup"),
        ("AX-SMCSERVICE-MIB", "axSmcTrapGroup"))
)
if mibBuilder.loadTexts:
    axSmcCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "AX-SMCSERVICE-MIB",
    **{"axSmcServiceInformation": axSmcServiceInformation,
       "axSmcServiceTable": axSmcServiceTable,
       "axSmcServiceEntry": axSmcServiceEntry,
       "axSmcServiceId": axSmcServiceId,
       "axSmcServiceName": axSmcServiceName,
       "axSmcServiceNifNo": axSmcServiceNifNo,
       "axSmcServiceType": axSmcServiceType,
       "axSmcServiceAttachedGroupId": axSmcServiceAttachedGroupId,
       "axSmcServiceAttachedGroupName": axSmcServiceAttachedGroupName,
       "axSmcServiceStatus": axSmcServiceStatus,
       "axSmcServiceUpTime": axSmcServiceUpTime,
       "axSmcServiceGroupTable": axSmcServiceGroupTable,
       "axSmcServiceGroupEntry": axSmcServiceGroupEntry,
       "axSmcServiceGroupId": axSmcServiceGroupId,
       "axSmcServiceGroupName": axSmcServiceGroupName,
       "axSmcServiceGroupRedundancyType": axSmcServiceGroupRedundancyType,
       "axSmcServiceGroupAttachedApplicationId": axSmcServiceGroupAttachedApplicationId,
       "axSmcServiceGroupAttachedApplicationName": axSmcServiceGroupAttachedApplicationName,
       "axSmcServiceGroupRedundancyStatus": axSmcServiceGroupRedundancyStatus,
       "axSmcApplicationTable": axSmcApplicationTable,
       "axSmcApplicationEntry": axSmcApplicationEntry,
       "axSmcApplicationId": axSmcApplicationId,
       "axSmcApplicationName": axSmcApplicationName,
       "axSmcServiceTraps": axSmcServiceTraps,
       "axSmcServiceTrapsPrefix": axSmcServiceTrapsPrefix,
       "axSmcServiceStateChange": axSmcServiceStateChange,
       "axSmcServiceGroupDuplexToSimplexTrap": axSmcServiceGroupDuplexToSimplexTrap,
       "axSmcServiceGroupSimplexToDuplexTrap": axSmcServiceGroupSimplexToDuplexTrap,
       "axSmcServiceGroupSwitchOver": axSmcServiceGroupSwitchOver,
       "axSmcConformance": axSmcConformance,
       "axSmcCompliances": axSmcCompliances,
       "axSmcCompliance": axSmcCompliance,
       "axSmcGroups": axSmcGroups,
       "axSmcGroup": axSmcGroup,
       "axSmcTrapGroup": axSmcTrapGroup}
)
