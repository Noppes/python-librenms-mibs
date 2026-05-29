# SNMP MIB module (AX-SYSTEM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\alaxala\AX-SYSTEM-MIB

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

axSystem = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 1001)
)
if mibBuilder.loadTexts:
    axSystem.setRevisions(
        ("2018-02-13 00:00",
         "2015-12-25 00:00",
         "2014-03-31 00:00",
         "2014-02-28 00:01",
         "2014-02-28 00:00",
         "2013-06-20 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs



class _AxModelType_Type(Integer32):
    """Custom type axModelType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              3000,
              3001,
              3002,
              4000,
              4001,
              4002,
              4100,
              4103)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("ax8608R", 3000),
          ("ax8616R", 3001),
          ("ax8632R", 3002),
          ("ax8608S", 4000),
          ("ax8616S", 4001),
          ("ax8632S", 4002),
          ("ax8308S", 4100),
          ("ax8304S", 4103))
    )


_AxModelType_Type.__name__ = "Integer32"
_AxModelType_Object = MibScalar
axModelType = _AxModelType_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 1001, 1),
    _AxModelType_Type()
)
axModelType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axModelType.setStatus("current")
_AxSoftware_ObjectIdentity = ObjectIdentity
axSoftware = _AxSoftware_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 1001, 2)
)
_AxSoftwareName_Type = DisplayString
_AxSoftwareName_Object = MibScalar
axSoftwareName = _AxSoftwareName_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 1001, 2, 1),
    _AxSoftwareName_Type()
)
axSoftwareName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axSoftwareName.setStatus("current")
_AxSoftwareAbbreviation_Type = DisplayString
_AxSoftwareAbbreviation_Object = MibScalar
axSoftwareAbbreviation = _AxSoftwareAbbreviation_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 1001, 2, 2),
    _AxSoftwareAbbreviation_Type()
)
axSoftwareAbbreviation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axSoftwareAbbreviation.setStatus("current")
_AxSystemMsg_ObjectIdentity = ObjectIdentity
axSystemMsg = _AxSystemMsg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 1001, 3)
)
_AxSystemMsgPrefix_ObjectIdentity = ObjectIdentity
axSystemMsgPrefix = _AxSystemMsgPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 1001, 3, 0)
)
_AxSystemMsgText_Type = DisplayString
_AxSystemMsgText_Object = MibScalar
axSystemMsgText = _AxSystemMsgText_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 1001, 3, 1),
    _AxSystemMsgText_Type()
)
axSystemMsgText.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axSystemMsgText.setStatus("current")
_AxSystemMsgTimeStamp_Type = DisplayString
_AxSystemMsgTimeStamp_Object = MibScalar
axSystemMsgTimeStamp = _AxSystemMsgTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 1001, 3, 2),
    _AxSystemMsgTimeStamp_Type()
)
axSystemMsgTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axSystemMsgTimeStamp.setStatus("current")
_AxSystemMsgLevel_Type = DisplayString
_AxSystemMsgLevel_Object = MibScalar
axSystemMsgLevel = _AxSystemMsgLevel_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 1001, 3, 3),
    _AxSystemMsgLevel_Type()
)
axSystemMsgLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axSystemMsgLevel.setStatus("current")
_AxSystemMsgSwitchCode_Type = OctetString
_AxSystemMsgSwitchCode_Object = MibScalar
axSystemMsgSwitchCode = _AxSystemMsgSwitchCode_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 1001, 3, 4),
    _AxSystemMsgSwitchCode_Type()
)
axSystemMsgSwitchCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axSystemMsgSwitchCode.setStatus("current")
_AxSystemMsgBcuNumber_Type = OctetString
_AxSystemMsgBcuNumber_Object = MibScalar
axSystemMsgBcuNumber = _AxSystemMsgBcuNumber_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 1001, 3, 5),
    _AxSystemMsgBcuNumber_Type()
)
axSystemMsgBcuNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axSystemMsgBcuNumber.setStatus("current")
_AxSystemMsgDuplexCode_Type = OctetString
_AxSystemMsgDuplexCode_Object = MibScalar
axSystemMsgDuplexCode = _AxSystemMsgDuplexCode_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 1001, 3, 6),
    _AxSystemMsgDuplexCode_Type()
)
axSystemMsgDuplexCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axSystemMsgDuplexCode.setStatus("current")
_AxSystemMsgEventType_Type = DisplayString
_AxSystemMsgEventType_Object = MibScalar
axSystemMsgEventType = _AxSystemMsgEventType_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 1001, 3, 7),
    _AxSystemMsgEventType_Type()
)
axSystemMsgEventType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axSystemMsgEventType.setStatus("current")
_AxSystemMsgEventPoint_Type = DisplayString
_AxSystemMsgEventPoint_Object = MibScalar
axSystemMsgEventPoint = _AxSystemMsgEventPoint_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 1001, 3, 8),
    _AxSystemMsgEventPoint_Type()
)
axSystemMsgEventPoint.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axSystemMsgEventPoint.setStatus("current")
_AxSystemMsgEventCode_Type = OctetString
_AxSystemMsgEventCode_Object = MibScalar
axSystemMsgEventCode = _AxSystemMsgEventCode_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 1001, 3, 9),
    _AxSystemMsgEventCode_Type()
)
axSystemMsgEventCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axSystemMsgEventCode.setStatus("current")
_AxSystemMsgAdditionalCode1_Type = OctetString
_AxSystemMsgAdditionalCode1_Object = MibScalar
axSystemMsgAdditionalCode1 = _AxSystemMsgAdditionalCode1_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 1001, 3, 10),
    _AxSystemMsgAdditionalCode1_Type()
)
axSystemMsgAdditionalCode1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axSystemMsgAdditionalCode1.setStatus("current")
_AxSystemMsgAdditionalCode2_Type = OctetString
_AxSystemMsgAdditionalCode2_Object = MibScalar
axSystemMsgAdditionalCode2 = _AxSystemMsgAdditionalCode2_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 1001, 3, 11),
    _AxSystemMsgAdditionalCode2_Type()
)
axSystemMsgAdditionalCode2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axSystemMsgAdditionalCode2.setStatus("current")
_AxSystemMsgMsgText_Type = DisplayString
_AxSystemMsgMsgText_Object = MibScalar
axSystemMsgMsgText = _AxSystemMsgMsgText_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 1001, 3, 12),
    _AxSystemMsgMsgText_Type()
)
axSystemMsgMsgText.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axSystemMsgMsgText.setStatus("current")
_AxSystemAlarm_ObjectIdentity = ObjectIdentity
axSystemAlarm = _AxSystemAlarm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 1001, 4)
)
_AxSystemAlarmTable_Object = MibTable
axSystemAlarmTable = _AxSystemAlarmTable_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 1001, 4, 1)
)
if mibBuilder.loadTexts:
    axSystemAlarmTable.setStatus("current")
_AxSystemAlarmEntry_Object = MibTableRow
axSystemAlarmEntry = _AxSystemAlarmEntry_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 1001, 4, 1, 1)
)
axSystemAlarmEntry.setIndexNames(
    (0, "AX-SYSTEM-MIB", "axSystemAlarmIndex"),
)
if mibBuilder.loadTexts:
    axSystemAlarmEntry.setStatus("current")
_AxSystemAlarmIndex_Type = Integer32
_AxSystemAlarmIndex_Object = MibTableColumn
axSystemAlarmIndex = _AxSystemAlarmIndex_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 1001, 4, 1, 1, 1),
    _AxSystemAlarmIndex_Type()
)
axSystemAlarmIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    axSystemAlarmIndex.setStatus("current")
_AxSystemAlarmEventLevel_Type = DisplayString
_AxSystemAlarmEventLevel_Object = MibTableColumn
axSystemAlarmEventLevel = _AxSystemAlarmEventLevel_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 1001, 4, 1, 1, 2),
    _AxSystemAlarmEventLevel_Type()
)
axSystemAlarmEventLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axSystemAlarmEventLevel.setStatus("current")
_AxSystemAlarmEventType_Type = DisplayString
_AxSystemAlarmEventType_Object = MibTableColumn
axSystemAlarmEventType = _AxSystemAlarmEventType_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 1001, 4, 1, 1, 3),
    _AxSystemAlarmEventType_Type()
)
axSystemAlarmEventType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axSystemAlarmEventType.setStatus("current")
_AxSystemAlarmEventCode_Type = OctetString
_AxSystemAlarmEventCode_Object = MibTableColumn
axSystemAlarmEventCode = _AxSystemAlarmEventCode_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 1001, 4, 1, 1, 4),
    _AxSystemAlarmEventCode_Type()
)
axSystemAlarmEventCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axSystemAlarmEventCode.setStatus("current")
_AxSystemAlarmEventPoint_Type = DisplayString
_AxSystemAlarmEventPoint_Object = MibTableColumn
axSystemAlarmEventPoint = _AxSystemAlarmEventPoint_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 1001, 4, 1, 1, 5),
    _AxSystemAlarmEventPoint_Type()
)
axSystemAlarmEventPoint.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axSystemAlarmEventPoint.setStatus("current")
_AxSystemAlarmMsgText_Type = DisplayString
_AxSystemAlarmMsgText_Object = MibTableColumn
axSystemAlarmMsgText = _AxSystemAlarmMsgText_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 1001, 4, 1, 1, 6),
    _AxSystemAlarmMsgText_Type()
)
axSystemAlarmMsgText.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axSystemAlarmMsgText.setStatus("current")
_AxLicense_ObjectIdentity = ObjectIdentity
axLicense = _AxLicense_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 1001, 6)
)
_AxLicenseNumber_Type = Integer32
_AxLicenseNumber_Object = MibScalar
axLicenseNumber = _AxLicenseNumber_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 1001, 6, 1),
    _AxLicenseNumber_Type()
)
axLicenseNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axLicenseNumber.setStatus("current")
_AxLicenseTable_Object = MibTable
axLicenseTable = _AxLicenseTable_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 1001, 6, 2)
)
if mibBuilder.loadTexts:
    axLicenseTable.setStatus("current")
_AxLicenseEntry_Object = MibTableRow
axLicenseEntry = _AxLicenseEntry_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 1001, 6, 2, 1)
)
axLicenseEntry.setIndexNames(
    (0, "AX-SYSTEM-MIB", "axLicenseIndex"),
)
if mibBuilder.loadTexts:
    axLicenseEntry.setStatus("current")
_AxLicenseIndex_Type = Integer32
_AxLicenseIndex_Object = MibTableColumn
axLicenseIndex = _AxLicenseIndex_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 1001, 6, 2, 1, 1),
    _AxLicenseIndex_Type()
)
axLicenseIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    axLicenseIndex.setStatus("current")
_AxLicenseSerialNumber_Type = DisplayString
_AxLicenseSerialNumber_Object = MibTableColumn
axLicenseSerialNumber = _AxLicenseSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 1001, 6, 2, 1, 2),
    _AxLicenseSerialNumber_Type()
)
axLicenseSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axLicenseSerialNumber.setStatus("current")
_AxLicenseOptionNumber_Type = Integer32
_AxLicenseOptionNumber_Object = MibTableColumn
axLicenseOptionNumber = _AxLicenseOptionNumber_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 1001, 6, 2, 1, 3),
    _AxLicenseOptionNumber_Type()
)
axLicenseOptionNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axLicenseOptionNumber.setStatus("current")
_AxLicenseOptionTable_Object = MibTable
axLicenseOptionTable = _AxLicenseOptionTable_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 1001, 6, 3)
)
if mibBuilder.loadTexts:
    axLicenseOptionTable.setStatus("current")
_AxLicenseOptionEntry_Object = MibTableRow
axLicenseOptionEntry = _AxLicenseOptionEntry_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 1001, 6, 3, 1)
)
axLicenseOptionEntry.setIndexNames(
    (0, "AX-SYSTEM-MIB", "axLicenseIndex"),
    (0, "AX-SYSTEM-MIB", "axLicenseOptionNumberIndex"),
)
if mibBuilder.loadTexts:
    axLicenseOptionEntry.setStatus("current")
_AxLicenseOptionNumberIndex_Type = Integer32
_AxLicenseOptionNumberIndex_Object = MibTableColumn
axLicenseOptionNumberIndex = _AxLicenseOptionNumberIndex_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 1001, 6, 3, 1, 1),
    _AxLicenseOptionNumberIndex_Type()
)
axLicenseOptionNumberIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    axLicenseOptionNumberIndex.setStatus("current")
_AxLicenseOptionSoftwareName_Type = DisplayString
_AxLicenseOptionSoftwareName_Object = MibTableColumn
axLicenseOptionSoftwareName = _AxLicenseOptionSoftwareName_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 1001, 6, 3, 1, 2),
    _AxLicenseOptionSoftwareName_Type()
)
axLicenseOptionSoftwareName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axLicenseOptionSoftwareName.setStatus("current")
_AxLicenseOptionSoftwareAbbreviation_Type = DisplayString
_AxLicenseOptionSoftwareAbbreviation_Object = MibTableColumn
axLicenseOptionSoftwareAbbreviation = _AxLicenseOptionSoftwareAbbreviation_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 1001, 6, 3, 1, 3),
    _AxLicenseOptionSoftwareAbbreviation_Type()
)
axLicenseOptionSoftwareAbbreviation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axLicenseOptionSoftwareAbbreviation.setStatus("current")
_AxSystemConformance_ObjectIdentity = ObjectIdentity
axSystemConformance = _AxSystemConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 1001, 1000)
)
_AxSystemCompliances_ObjectIdentity = ObjectIdentity
axSystemCompliances = _AxSystemCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 1001, 1000, 1)
)
_AxSystemGroups_ObjectIdentity = ObjectIdentity
axSystemGroups = _AxSystemGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 1001, 1000, 2)
)

# Managed Objects groups

axSystemGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 1001, 1000, 2, 1)
)
axSystemGroup.setObjects(
      *(("AX-SYSTEM-MIB", "axModelType"),
        ("AX-SYSTEM-MIB", "axSoftwareName"),
        ("AX-SYSTEM-MIB", "axSoftwareAbbreviation"),
        ("AX-SYSTEM-MIB", "axSystemMsgText"),
        ("AX-SYSTEM-MIB", "axSystemMsgTimeStamp"),
        ("AX-SYSTEM-MIB", "axSystemMsgLevel"),
        ("AX-SYSTEM-MIB", "axSystemMsgSwitchCode"),
        ("AX-SYSTEM-MIB", "axSystemMsgBcuNumber"),
        ("AX-SYSTEM-MIB", "axSystemMsgDuplexCode"),
        ("AX-SYSTEM-MIB", "axSystemMsgEventType"),
        ("AX-SYSTEM-MIB", "axSystemMsgEventPoint"),
        ("AX-SYSTEM-MIB", "axSystemMsgEventCode"),
        ("AX-SYSTEM-MIB", "axSystemMsgAdditionalCode1"),
        ("AX-SYSTEM-MIB", "axSystemMsgAdditionalCode2"),
        ("AX-SYSTEM-MIB", "axSystemMsgMsgText"),
        ("AX-SYSTEM-MIB", "axSystemAlarmEventLevel"),
        ("AX-SYSTEM-MIB", "axSystemAlarmEventType"),
        ("AX-SYSTEM-MIB", "axSystemAlarmEventCode"),
        ("AX-SYSTEM-MIB", "axSystemAlarmEventPoint"),
        ("AX-SYSTEM-MIB", "axSystemAlarmMsgText"),
        ("AX-SYSTEM-MIB", "axLicenseNumber"),
        ("AX-SYSTEM-MIB", "axLicenseSerialNumber"),
        ("AX-SYSTEM-MIB", "axLicenseOptionNumber"),
        ("AX-SYSTEM-MIB", "axLicenseOptionSoftwareName"),
        ("AX-SYSTEM-MIB", "axLicenseOptionSoftwareAbbreviation"))
)
if mibBuilder.loadTexts:
    axSystemGroup.setStatus("current")


# Notification objects

axSystemMsgTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 1001, 3, 0, 1)
)
axSystemMsgTrap.setObjects(
      *(("AX-SYSTEM-MIB", "axSystemMsgText"),
        ("AX-SYSTEM-MIB", "axSystemMsgTimeStamp"),
        ("AX-SYSTEM-MIB", "axSystemMsgLevel"),
        ("AX-SYSTEM-MIB", "axSystemMsgSwitchCode"),
        ("AX-SYSTEM-MIB", "axSystemMsgBcuNumber"),
        ("AX-SYSTEM-MIB", "axSystemMsgDuplexCode"),
        ("AX-SYSTEM-MIB", "axSystemMsgEventType"),
        ("AX-SYSTEM-MIB", "axSystemMsgEventPoint"),
        ("AX-SYSTEM-MIB", "axSystemMsgEventCode"),
        ("AX-SYSTEM-MIB", "axSystemMsgAdditionalCode1"),
        ("AX-SYSTEM-MIB", "axSystemMsgAdditionalCode2"),
        ("AX-SYSTEM-MIB", "axSystemMsgMsgText"))
)
if mibBuilder.loadTexts:
    axSystemMsgTrap.setStatus(
        "current"
    )


# Notifications groups

axSystemNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 1001, 1000, 2, 10)
)
axSystemNotificationGroup.setObjects(
    ("AX-SYSTEM-MIB", "axSystemMsgTrap")
)
if mibBuilder.loadTexts:
    axSystemNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

axSystemCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 1001, 1000, 1, 1)
)
axSystemCompliance.setObjects(
      *(("AX-SYSTEM-MIB", "axSystemGroup"),
        ("AX-SYSTEM-MIB", "axSystemNotificationGroup"))
)
if mibBuilder.loadTexts:
    axSystemCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "AX-SYSTEM-MIB",
    **{"axSystem": axSystem,
       "axModelType": axModelType,
       "axSoftware": axSoftware,
       "axSoftwareName": axSoftwareName,
       "axSoftwareAbbreviation": axSoftwareAbbreviation,
       "axSystemMsg": axSystemMsg,
       "axSystemMsgPrefix": axSystemMsgPrefix,
       "axSystemMsgTrap": axSystemMsgTrap,
       "axSystemMsgText": axSystemMsgText,
       "axSystemMsgTimeStamp": axSystemMsgTimeStamp,
       "axSystemMsgLevel": axSystemMsgLevel,
       "axSystemMsgSwitchCode": axSystemMsgSwitchCode,
       "axSystemMsgBcuNumber": axSystemMsgBcuNumber,
       "axSystemMsgDuplexCode": axSystemMsgDuplexCode,
       "axSystemMsgEventType": axSystemMsgEventType,
       "axSystemMsgEventPoint": axSystemMsgEventPoint,
       "axSystemMsgEventCode": axSystemMsgEventCode,
       "axSystemMsgAdditionalCode1": axSystemMsgAdditionalCode1,
       "axSystemMsgAdditionalCode2": axSystemMsgAdditionalCode2,
       "axSystemMsgMsgText": axSystemMsgMsgText,
       "axSystemAlarm": axSystemAlarm,
       "axSystemAlarmTable": axSystemAlarmTable,
       "axSystemAlarmEntry": axSystemAlarmEntry,
       "axSystemAlarmIndex": axSystemAlarmIndex,
       "axSystemAlarmEventLevel": axSystemAlarmEventLevel,
       "axSystemAlarmEventType": axSystemAlarmEventType,
       "axSystemAlarmEventCode": axSystemAlarmEventCode,
       "axSystemAlarmEventPoint": axSystemAlarmEventPoint,
       "axSystemAlarmMsgText": axSystemAlarmMsgText,
       "axLicense": axLicense,
       "axLicenseNumber": axLicenseNumber,
       "axLicenseTable": axLicenseTable,
       "axLicenseEntry": axLicenseEntry,
       "axLicenseIndex": axLicenseIndex,
       "axLicenseSerialNumber": axLicenseSerialNumber,
       "axLicenseOptionNumber": axLicenseOptionNumber,
       "axLicenseOptionTable": axLicenseOptionTable,
       "axLicenseOptionEntry": axLicenseOptionEntry,
       "axLicenseOptionNumberIndex": axLicenseOptionNumberIndex,
       "axLicenseOptionSoftwareName": axLicenseOptionSoftwareName,
       "axLicenseOptionSoftwareAbbreviation": axLicenseOptionSoftwareAbbreviation,
       "axSystemConformance": axSystemConformance,
       "axSystemCompliances": axSystemCompliances,
       "axSystemCompliance": axSystemCompliance,
       "axSystemGroups": axSystemGroups,
       "axSystemGroup": axSystemGroup,
       "axSystemNotificationGroup": axSystemNotificationGroup}
)
