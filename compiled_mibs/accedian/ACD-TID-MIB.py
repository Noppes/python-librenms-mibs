# SNMP MIB module (ACD-TID-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\accedian\ACD-TID-MIB

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

(acdMibs,) = mibBuilder.importSymbols(
    "ACCEDIAN-SMI",
    "acdMibs")

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

acdTid = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 22420, 2, 14)
)
if mibBuilder.loadTexts:
    acdTid.setRevisions(
        ("2012-11-05 22:00",
         "2011-11-11 01:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class AcdTidType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("configuration", 1),
          ("status", 2))
    )



# MIB Managed Objects in the order of their OIDs

_AcdTidNotifications_ObjectIdentity = ObjectIdentity
acdTidNotifications = _AcdTidNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22420, 2, 14, 0)
)
_AcdTidNotificationPrefix_ObjectIdentity = ObjectIdentity
acdTidNotificationPrefix = _AcdTidNotificationPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22420, 2, 14, 0, 0)
)
_AcdTidMIBObjects_ObjectIdentity = ObjectIdentity
acdTidMIBObjects = _AcdTidMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22420, 2, 14, 1)
)
_AcdTidGeneral_ObjectIdentity = ObjectIdentity
acdTidGeneral = _AcdTidGeneral_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22420, 2, 14, 1, 1)
)
_AcdTidCfgLastChangeTid_Type = Unsigned32
_AcdTidCfgLastChangeTid_Object = MibScalar
acdTidCfgLastChangeTid = _AcdTidCfgLastChangeTid_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 14, 1, 1, 1),
    _AcdTidCfgLastChangeTid_Type()
)
acdTidCfgLastChangeTid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdTidCfgLastChangeTid.setStatus("current")
_AcdTidStatusLastChangeTid_Type = Unsigned32
_AcdTidStatusLastChangeTid_Object = MibScalar
acdTidStatusLastChangeTid = _AcdTidStatusLastChangeTid_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 14, 1, 1, 2),
    _AcdTidStatusLastChangeTid_Type()
)
acdTidStatusLastChangeTid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdTidStatusLastChangeTid.setStatus("current")
_AcdTidInfo_ObjectIdentity = ObjectIdentity
acdTidInfo = _AcdTidInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22420, 2, 14, 1, 2)
)
_AcdTidInfoTable_Object = MibTable
acdTidInfoTable = _AcdTidInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 14, 1, 2, 1)
)
if mibBuilder.loadTexts:
    acdTidInfoTable.setStatus("current")
_AcdTidInfoEntry_Object = MibTableRow
acdTidInfoEntry = _AcdTidInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 14, 1, 2, 1, 1)
)
acdTidInfoEntry.setIndexNames(
    (0, "ACD-TID-MIB", "acdTidInfoIndex"),
)
if mibBuilder.loadTexts:
    acdTidInfoEntry.setStatus("current")
_AcdTidInfoIndex_Type = Unsigned32
_AcdTidInfoIndex_Object = MibTableColumn
acdTidInfoIndex = _AcdTidInfoIndex_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 14, 1, 2, 1, 1, 1),
    _AcdTidInfoIndex_Type()
)
acdTidInfoIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    acdTidInfoIndex.setStatus("current")
_AcdTidInfoOID_Type = ObjectIdentifier
_AcdTidInfoOID_Object = MibTableColumn
acdTidInfoOID = _AcdTidInfoOID_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 14, 1, 2, 1, 1, 2),
    _AcdTidInfoOID_Type()
)
acdTidInfoOID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdTidInfoOID.setStatus("current")
_AcdTidInfoType_Type = AcdTidType
_AcdTidInfoType_Object = MibTableColumn
acdTidInfoType = _AcdTidInfoType_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 14, 1, 2, 1, 1, 3),
    _AcdTidInfoType_Type()
)
acdTidInfoType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdTidInfoType.setStatus("current")
_AcdTidInfoDescr_Type = DisplayString
_AcdTidInfoDescr_Object = MibTableColumn
acdTidInfoDescr = _AcdTidInfoDescr_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 14, 1, 2, 1, 1, 4),
    _AcdTidInfoDescr_Type()
)
acdTidInfoDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdTidInfoDescr.setStatus("current")
_AcdTidInfoLastChangeTid_Type = Unsigned32
_AcdTidInfoLastChangeTid_Object = MibTableColumn
acdTidInfoLastChangeTid = _AcdTidInfoLastChangeTid_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 14, 1, 2, 1, 1, 5),
    _AcdTidInfoLastChangeTid_Type()
)
acdTidInfoLastChangeTid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdTidInfoLastChangeTid.setStatus("current")
_AcdTidGlobalCfg_ObjectIdentity = ObjectIdentity
acdTidGlobalCfg = _AcdTidGlobalCfg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22420, 2, 14, 1, 3)
)
_AcdTidglobalCfgChangeCount_Type = Unsigned32
_AcdTidglobalCfgChangeCount_Object = MibScalar
acdTidglobalCfgChangeCount = _AcdTidglobalCfgChangeCount_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 14, 1, 3, 2),
    _AcdTidglobalCfgChangeCount_Type()
)
acdTidglobalCfgChangeCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdTidglobalCfgChangeCount.setStatus("current")
_AcdTidConformance_ObjectIdentity = ObjectIdentity
acdTidConformance = _AcdTidConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22420, 2, 14, 2)
)
_AcdTidCompliances_ObjectIdentity = ObjectIdentity
acdTidCompliances = _AcdTidCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22420, 2, 14, 2, 1)
)
_AcdTidGroups_ObjectIdentity = ObjectIdentity
acdTidGroups = _AcdTidGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22420, 2, 14, 2, 2)
)

# Managed Objects groups

acdTidGeneralGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 22420, 2, 14, 2, 2, 1)
)
acdTidGeneralGroup.setObjects(
      *(("ACD-TID-MIB", "acdTidCfgLastChangeTid"),
        ("ACD-TID-MIB", "acdTidStatusLastChangeTid"))
)
if mibBuilder.loadTexts:
    acdTidGeneralGroup.setStatus("current")

acdTidTableGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 22420, 2, 14, 2, 2, 2)
)
acdTidTableGroup.setObjects(
      *(("ACD-TID-MIB", "acdTidInfoOID"),
        ("ACD-TID-MIB", "acdTidInfoType"),
        ("ACD-TID-MIB", "acdTidInfoDescr"),
        ("ACD-TID-MIB", "acdTidInfoLastChangeTid"))
)
if mibBuilder.loadTexts:
    acdTidTableGroup.setStatus("current")

acdTidGlobalCfgGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 22420, 2, 14, 2, 2, 3)
)
acdTidGlobalCfgGroup.setObjects(
    ("ACD-TID-MIB", "acdTidglobalCfgChangeCount")
)
if mibBuilder.loadTexts:
    acdTidGlobalCfgGroup.setStatus("current")


# Notification objects

acdTidGlobalCfgChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 22420, 2, 14, 0, 0, 1)
)
acdTidGlobalCfgChange.setObjects(
    ("ACD-TID-MIB", "acdTidglobalCfgChangeCount")
)
if mibBuilder.loadTexts:
    acdTidGlobalCfgChange.setStatus(
        "current"
    )


# Notifications groups

acdTidNotificationsGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 22420, 2, 14, 2, 2, 4)
)
acdTidNotificationsGroup.setObjects(
    ("ACD-TID-MIB", "acdTidGlobalCfgChange")
)
if mibBuilder.loadTexts:
    acdTidNotificationsGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

acdTidCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 22420, 2, 14, 2, 1, 1)
)
acdTidCompliance.setObjects(
      *(("ACD-TID-MIB", "acdTidGeneralGroup"),
        ("ACD-TID-MIB", "acdTidTableGroup"),
        ("ACD-TID-MIB", "acdTidGlobalCfgGroup"),
        ("ACD-TID-MIB", "acdTidNotificationsGroup"))
)
if mibBuilder.loadTexts:
    acdTidCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ACD-TID-MIB",
    **{"AcdTidType": AcdTidType,
       "acdTid": acdTid,
       "acdTidNotifications": acdTidNotifications,
       "acdTidNotificationPrefix": acdTidNotificationPrefix,
       "acdTidGlobalCfgChange": acdTidGlobalCfgChange,
       "acdTidMIBObjects": acdTidMIBObjects,
       "acdTidGeneral": acdTidGeneral,
       "acdTidCfgLastChangeTid": acdTidCfgLastChangeTid,
       "acdTidStatusLastChangeTid": acdTidStatusLastChangeTid,
       "acdTidInfo": acdTidInfo,
       "acdTidInfoTable": acdTidInfoTable,
       "acdTidInfoEntry": acdTidInfoEntry,
       "acdTidInfoIndex": acdTidInfoIndex,
       "acdTidInfoOID": acdTidInfoOID,
       "acdTidInfoType": acdTidInfoType,
       "acdTidInfoDescr": acdTidInfoDescr,
       "acdTidInfoLastChangeTid": acdTidInfoLastChangeTid,
       "acdTidGlobalCfg": acdTidGlobalCfg,
       "acdTidglobalCfgChangeCount": acdTidglobalCfgChangeCount,
       "acdTidConformance": acdTidConformance,
       "acdTidCompliances": acdTidCompliances,
       "acdTidCompliance": acdTidCompliance,
       "acdTidGroups": acdTidGroups,
       "acdTidGeneralGroup": acdTidGeneralGroup,
       "acdTidTableGroup": acdTidTableGroup,
       "acdTidGlobalCfgGroup": acdTidGlobalCfgGroup,
       "acdTidNotificationsGroup": acdTidNotificationsGroup}
)
