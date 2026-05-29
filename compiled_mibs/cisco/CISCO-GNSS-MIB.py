# SNMP MIB module (CISCO-GNSS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\cisco\CISCO-GNSS-MIB

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

(ciscoMgmt,) = mibBuilder.importSymbols(
    "CISCO-SMI",
    "ciscoMgmt")

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

ciscoGnssMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 862)
)
if mibBuilder.loadTexts:
    ciscoGnssMIB.setRevisions(
        ("2019-05-22 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class OpenCircuitAlarmStatus(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("raise", 1),
          ("clear", 2))
    )



class ShortCircuitAlarmStatus(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("raise", 1),
          ("clear", 2))
    )



class SVCnt(TextualConvention, Integer32):
    status = "current"


class GnssSvVisibilityStatus(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("bad", 1),
          ("good", 2))
    )



class SlotState(TextualConvention, Unsigned32):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )



class SlotInfo(TextualConvention, Unsigned32):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )



class GnssModuleLockStatus(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("down", 1),
          ("up", 2))
    )



class GnssModulePresenceStatus(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("absent", 1),
          ("present", 2))
    )



# MIB Managed Objects in the order of their OIDs

_CiscoGnssMIBNotifs_ObjectIdentity = ObjectIdentity
ciscoGnssMIBNotifs = _CiscoGnssMIBNotifs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 862, 0)
)
_CiscoGnssMIBObjects_ObjectIdentity = ObjectIdentity
ciscoGnssMIBObjects = _CiscoGnssMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 862, 1)
)
_CGnssModuleLockStatus_Type = GnssModuleLockStatus
_CGnssModuleLockStatus_Object = MibScalar
cGnssModuleLockStatus = _CGnssModuleLockStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 862, 1, 1),
    _CGnssModuleLockStatus_Type()
)
cGnssModuleLockStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cGnssModuleLockStatus.setStatus("current")
_CGnssModulePresenceStatus_Type = GnssModulePresenceStatus
_CGnssModulePresenceStatus_Object = MibScalar
cGnssModulePresenceStatus = _CGnssModulePresenceStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 862, 1, 2),
    _CGnssModulePresenceStatus_Type()
)
cGnssModulePresenceStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cGnssModulePresenceStatus.setStatus("current")
_CGnssModuleSlotInfo_Type = SlotInfo
_CGnssModuleSlotInfo_Object = MibScalar
cGnssModuleSlotInfo = _CGnssModuleSlotInfo_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 862, 1, 3),
    _CGnssModuleSlotInfo_Type()
)
cGnssModuleSlotInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cGnssModuleSlotInfo.setStatus("current")
_CGnssModuleSlotState_Type = SlotState
_CGnssModuleSlotState_Object = MibScalar
cGnssModuleSlotState = _CGnssModuleSlotState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 862, 1, 4),
    _CGnssModuleSlotState_Type()
)
cGnssModuleSlotState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cGnssModuleSlotState.setStatus("current")


class _CGnssSatelliteVisibilityStatus_Type(GnssSvVisibilityStatus):
    """Custom type cGnssSatelliteVisibilityStatus based on GnssSvVisibilityStatus"""
    defaultValue = 2


_CGnssSatelliteVisibilityStatus_Type.__name__ = "GnssSvVisibilityStatus"
_CGnssSatelliteVisibilityStatus_Object = MibScalar
cGnssSatelliteVisibilityStatus = _CGnssSatelliteVisibilityStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 862, 1, 5),
    _CGnssSatelliteVisibilityStatus_Type()
)
cGnssSatelliteVisibilityStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cGnssSatelliteVisibilityStatus.setStatus("current")


class _CGnssModuleSatelliteCount_Type(SVCnt):
    """Custom type cGnssModuleSatelliteCount based on SVCnt"""
    defaultValue = 0


_CGnssModuleSatelliteCount_Type.__name__ = "SVCnt"
_CGnssModuleSatelliteCount_Object = MibScalar
cGnssModuleSatelliteCount = _CGnssModuleSatelliteCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 862, 1, 6),
    _CGnssModuleSatelliteCount_Type()
)
cGnssModuleSatelliteCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cGnssModuleSatelliteCount.setStatus("current")
_CGnssModuleSvIdSNR_Type = DisplayString
_CGnssModuleSvIdSNR_Object = MibScalar
cGnssModuleSvIdSNR = _CGnssModuleSvIdSNR_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 862, 1, 7),
    _CGnssModuleSvIdSNR_Type()
)
cGnssModuleSvIdSNR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cGnssModuleSvIdSNR.setStatus("current")


class _CGnssModuleSCAlarmStatus_Type(ShortCircuitAlarmStatus):
    """Custom type cGnssModuleSCAlarmStatus based on ShortCircuitAlarmStatus"""
    defaultValue = 2


_CGnssModuleSCAlarmStatus_Type.__name__ = "ShortCircuitAlarmStatus"
_CGnssModuleSCAlarmStatus_Object = MibScalar
cGnssModuleSCAlarmStatus = _CGnssModuleSCAlarmStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 862, 1, 8),
    _CGnssModuleSCAlarmStatus_Type()
)
cGnssModuleSCAlarmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cGnssModuleSCAlarmStatus.setStatus("current")


class _CGnssModuleOCAlarmStatus_Type(OpenCircuitAlarmStatus):
    """Custom type cGnssModuleOCAlarmStatus based on OpenCircuitAlarmStatus"""
    defaultValue = 2


_CGnssModuleOCAlarmStatus_Type.__name__ = "OpenCircuitAlarmStatus"
_CGnssModuleOCAlarmStatus_Object = MibScalar
cGnssModuleOCAlarmStatus = _CGnssModuleOCAlarmStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 862, 1, 9),
    _CGnssModuleOCAlarmStatus_Type()
)
cGnssModuleOCAlarmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cGnssModuleOCAlarmStatus.setStatus("current")
_CiscoGnssMIBConform_ObjectIdentity = ObjectIdentity
ciscoGnssMIBConform = _CiscoGnssMIBConform_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 862, 2)
)
_CiscoGnssMIBCompliances_ObjectIdentity = ObjectIdentity
ciscoGnssMIBCompliances = _CiscoGnssMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 862, 2, 1)
)
_CiscoGnssMIBGroups_ObjectIdentity = ObjectIdentity
ciscoGnssMIBGroups = _CiscoGnssMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 862, 2, 2)
)

# Managed Objects groups

ciscoGnssMIBMainObjectGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 862, 2, 2, 1)
)
ciscoGnssMIBMainObjectGroup.setObjects(
    ("CISCO-GNSS-MIB", "cGnssModuleLockStatus")
)
if mibBuilder.loadTexts:
    ciscoGnssMIBMainObjectGroup.setStatus("current")


# Notification objects

ciscoGnssModuleLockStatus = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 862, 0, 1)
)
ciscoGnssModuleLockStatus.setObjects(
      *(("CISCO-GNSS-MIB", "cGnssModuleLockStatus"),
        ("CISCO-GNSS-MIB", "cGnssModuleSlotInfo"),
        ("CISCO-GNSS-MIB", "cGnssModuleSlotState"))
)
if mibBuilder.loadTexts:
    ciscoGnssModuleLockStatus.setStatus(
        "current"
    )

ciscoGnssModuleLockClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 862, 0, 2)
)
ciscoGnssModuleLockClear.setObjects(
      *(("CISCO-GNSS-MIB", "cGnssModuleLockStatus"),
        ("CISCO-GNSS-MIB", "cGnssModuleSlotInfo"),
        ("CISCO-GNSS-MIB", "cGnssModuleSlotState"))
)
if mibBuilder.loadTexts:
    ciscoGnssModuleLockClear.setStatus(
        "current"
    )

ciscoGnssModulePresenceStatus = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 862, 0, 3)
)
ciscoGnssModulePresenceStatus.setObjects(
      *(("CISCO-GNSS-MIB", "cGnssModulePresenceStatus"),
        ("CISCO-GNSS-MIB", "cGnssModuleSlotInfo"),
        ("CISCO-GNSS-MIB", "cGnssModuleSlotState"))
)
if mibBuilder.loadTexts:
    ciscoGnssModulePresenceStatus.setStatus(
        "current"
    )

ciscoGnssModulePresenceClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 862, 0, 4)
)
ciscoGnssModulePresenceClear.setObjects(
      *(("CISCO-GNSS-MIB", "cGnssModulePresenceStatus"),
        ("CISCO-GNSS-MIB", "cGnssModuleSlotInfo"),
        ("CISCO-GNSS-MIB", "cGnssModuleSlotState"))
)
if mibBuilder.loadTexts:
    ciscoGnssModulePresenceClear.setStatus(
        "current"
    )

ciscoGnssAntennaSCAlarmStatus = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 862, 0, 5)
)
ciscoGnssAntennaSCAlarmStatus.setObjects(
      *(("CISCO-GNSS-MIB", "cGnssModuleSCAlarmStatus"),
        ("CISCO-GNSS-MIB", "cGnssModuleSlotInfo"),
        ("CISCO-GNSS-MIB", "cGnssModuleSlotState"))
)
if mibBuilder.loadTexts:
    ciscoGnssAntennaSCAlarmStatus.setStatus(
        "current"
    )

ciscoGnssAntennaSCAlarmClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 862, 0, 6)
)
ciscoGnssAntennaSCAlarmClear.setObjects(
      *(("CISCO-GNSS-MIB", "cGnssModuleSCAlarmStatus"),
        ("CISCO-GNSS-MIB", "cGnssModuleSlotInfo"),
        ("CISCO-GNSS-MIB", "cGnssModuleSlotState"))
)
if mibBuilder.loadTexts:
    ciscoGnssAntennaSCAlarmClear.setStatus(
        "current"
    )

ciscoGnssAntennaOCAlarmStatus = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 862, 0, 7)
)
ciscoGnssAntennaOCAlarmStatus.setObjects(
      *(("CISCO-GNSS-MIB", "cGnssModuleSlotInfo"),
        ("CISCO-GNSS-MIB", "cGnssModuleSlotState"),
        ("CISCO-GNSS-MIB", "cGnssModuleOCAlarmStatus"))
)
if mibBuilder.loadTexts:
    ciscoGnssAntennaOCAlarmStatus.setStatus(
        "current"
    )

ciscoGnssAntennaOCAlarmClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 862, 0, 8)
)
ciscoGnssAntennaOCAlarmClear.setObjects(
      *(("CISCO-GNSS-MIB", "cGnssModuleSlotInfo"),
        ("CISCO-GNSS-MIB", "cGnssModuleSlotState"),
        ("CISCO-GNSS-MIB", "cGnssModuleOCAlarmStatus"))
)
if mibBuilder.loadTexts:
    ciscoGnssAntennaOCAlarmClear.setStatus(
        "current"
    )

ciscoGnssSatelliteVisibilityStatus = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 862, 0, 9)
)
ciscoGnssSatelliteVisibilityStatus.setObjects(
      *(("CISCO-GNSS-MIB", "cGnssSatelliteVisibilityStatus"),
        ("CISCO-GNSS-MIB", "cGnssModuleSlotInfo"),
        ("CISCO-GNSS-MIB", "cGnssModuleSlotState"))
)
if mibBuilder.loadTexts:
    ciscoGnssSatelliteVisibilityStatus.setStatus(
        "current"
    )

ciscoGnssSatelliteVisibilityClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 862, 0, 10)
)
ciscoGnssSatelliteVisibilityClear.setObjects(
      *(("CISCO-GNSS-MIB", "cGnssModuleSlotInfo"),
        ("CISCO-GNSS-MIB", "cGnssModuleSlotState"),
        ("CISCO-GNSS-MIB", "cGnssSatelliteVisibilityStatus"))
)
if mibBuilder.loadTexts:
    ciscoGnssSatelliteVisibilityClear.setStatus(
        "current"
    )


# Notifications groups

ciscoGnssMIBNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 862, 2, 2, 2)
)
ciscoGnssMIBNotificationGroup.setObjects(
    ("CISCO-GNSS-MIB", "ciscoGnssModuleLockStatus")
)
if mibBuilder.loadTexts:
    ciscoGnssMIBNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

ciscoGnssMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 862, 2, 1, 1)
)
ciscoGnssMIBCompliance.setObjects(
      *(("CISCO-GNSS-MIB", "ciscoGnssMIBMainObjectGroup"),
        ("CISCO-GNSS-MIB", "ciscoGnssMIBNotificationGroup"))
)
if mibBuilder.loadTexts:
    ciscoGnssMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-GNSS-MIB",
    **{"OpenCircuitAlarmStatus": OpenCircuitAlarmStatus,
       "ShortCircuitAlarmStatus": ShortCircuitAlarmStatus,
       "SVCnt": SVCnt,
       "GnssSvVisibilityStatus": GnssSvVisibilityStatus,
       "SlotState": SlotState,
       "SlotInfo": SlotInfo,
       "GnssModuleLockStatus": GnssModuleLockStatus,
       "GnssModulePresenceStatus": GnssModulePresenceStatus,
       "ciscoGnssMIB": ciscoGnssMIB,
       "ciscoGnssMIBNotifs": ciscoGnssMIBNotifs,
       "ciscoGnssModuleLockStatus": ciscoGnssModuleLockStatus,
       "ciscoGnssModuleLockClear": ciscoGnssModuleLockClear,
       "ciscoGnssModulePresenceStatus": ciscoGnssModulePresenceStatus,
       "ciscoGnssModulePresenceClear": ciscoGnssModulePresenceClear,
       "ciscoGnssAntennaSCAlarmStatus": ciscoGnssAntennaSCAlarmStatus,
       "ciscoGnssAntennaSCAlarmClear": ciscoGnssAntennaSCAlarmClear,
       "ciscoGnssAntennaOCAlarmStatus": ciscoGnssAntennaOCAlarmStatus,
       "ciscoGnssAntennaOCAlarmClear": ciscoGnssAntennaOCAlarmClear,
       "ciscoGnssSatelliteVisibilityStatus": ciscoGnssSatelliteVisibilityStatus,
       "ciscoGnssSatelliteVisibilityClear": ciscoGnssSatelliteVisibilityClear,
       "ciscoGnssMIBObjects": ciscoGnssMIBObjects,
       "cGnssModuleLockStatus": cGnssModuleLockStatus,
       "cGnssModulePresenceStatus": cGnssModulePresenceStatus,
       "cGnssModuleSlotInfo": cGnssModuleSlotInfo,
       "cGnssModuleSlotState": cGnssModuleSlotState,
       "cGnssSatelliteVisibilityStatus": cGnssSatelliteVisibilityStatus,
       "cGnssModuleSatelliteCount": cGnssModuleSatelliteCount,
       "cGnssModuleSvIdSNR": cGnssModuleSvIdSNR,
       "cGnssModuleSCAlarmStatus": cGnssModuleSCAlarmStatus,
       "cGnssModuleOCAlarmStatus": cGnssModuleOCAlarmStatus,
       "ciscoGnssMIBConform": ciscoGnssMIBConform,
       "ciscoGnssMIBCompliances": ciscoGnssMIBCompliances,
       "ciscoGnssMIBCompliance": ciscoGnssMIBCompliance,
       "ciscoGnssMIBGroups": ciscoGnssMIBGroups,
       "ciscoGnssMIBMainObjectGroup": ciscoGnssMIBMainObjectGroup,
       "ciscoGnssMIBNotificationGroup": ciscoGnssMIBNotificationGroup}
)
