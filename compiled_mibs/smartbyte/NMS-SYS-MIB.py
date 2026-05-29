# SNMP MIB module (NMS-SYS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\smartbyte\NMS-SYS-MIB

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

(nmsModule,) = mibBuilder.importSymbols(
    "NMS",
    "nmsModule")

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

sysModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 56166, 1, 2, 1)
)
if mibBuilder.loadTexts:
    sysModule.setRevisions(
        ("2025-11-21 11:11",
         "2025-02-13 11:38",
         "2020-10-16 11:42")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Sys_ObjectIdentity = ObjectIdentity
sys = _Sys_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 56166, 1, 2)
)
_CpuUtilized_Type = Integer32
_CpuUtilized_Object = MibScalar
cpuUtilized = _CpuUtilized_Object(
    (1, 3, 6, 1, 4, 1, 56166, 1, 2, 1, 1),
    _CpuUtilized_Type()
)
cpuUtilized.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpuUtilized.setStatus("current")
_MemUtilized_Type = Integer32
_MemUtilized_Object = MibScalar
memUtilized = _MemUtilized_Object(
    (1, 3, 6, 1, 4, 1, 56166, 1, 2, 1, 2),
    _MemUtilized_Type()
)
memUtilized.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    memUtilized.setStatus("current")
_CpuIdle_Type = Integer32
_CpuIdle_Object = MibScalar
cpuIdle = _CpuIdle_Object(
    (1, 3, 6, 1, 4, 1, 56166, 1, 2, 1, 3),
    _CpuIdle_Type()
)
cpuIdle.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpuIdle.setStatus("current")
_MemTotalReal_Type = Integer32
_MemTotalReal_Object = MibScalar
memTotalReal = _MemTotalReal_Object(
    (1, 3, 6, 1, 4, 1, 56166, 1, 2, 1, 4),
    _MemTotalReal_Type()
)
memTotalReal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    memTotalReal.setStatus("current")
if mibBuilder.loadTexts:
    memTotalReal.setUnits("kB")
_MemAvailReal_Type = Integer32
_MemAvailReal_Object = MibScalar
memAvailReal = _MemAvailReal_Object(
    (1, 3, 6, 1, 4, 1, 56166, 1, 2, 1, 5),
    _MemAvailReal_Type()
)
memAvailReal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    memAvailReal.setStatus("current")
if mibBuilder.loadTexts:
    memAvailReal.setUnits("kB")
_Operations_ObjectIdentity = ObjectIdentity
operations = _Operations_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 56166, 1, 2, 2)
)


class _ConfigurationOper_Type(Integer32):
    """Custom type configurationOper based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("save", 1),
          ("empty", 2),
          ("default", 3))
    )


_ConfigurationOper_Type.__name__ = "Integer32"
_ConfigurationOper_Object = MibScalar
configurationOper = _ConfigurationOper_Object(
    (1, 3, 6, 1, 4, 1, 56166, 1, 2, 2, 1),
    _ConfigurationOper_Type()
)
configurationOper.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configurationOper.setStatus("current")


class _PowerOper_Type(Integer32):
    """Custom type powerOper based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("on", 1),
          ("off", 2),
          ("reset", 3))
    )


_PowerOper_Type.__name__ = "Integer32"
_PowerOper_Object = MibScalar
powerOper = _PowerOper_Object(
    (1, 3, 6, 1, 4, 1, 56166, 1, 2, 2, 2),
    _PowerOper_Type()
)
powerOper.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    powerOper.setStatus("current")
_PowerTable_Object = MibTable
powerTable = _PowerTable_Object(
    (1, 3, 6, 1, 4, 1, 56166, 1, 2, 3)
)
if mibBuilder.loadTexts:
    powerTable.setStatus("current")
_PowerEntry_Object = MibTableRow
powerEntry = _PowerEntry_Object(
    (1, 3, 6, 1, 4, 1, 56166, 1, 2, 3, 1)
)
powerEntry.setIndexNames(
    (0, "NMS-SYS-MIB", "powerIndex"),
)
if mibBuilder.loadTexts:
    powerEntry.setStatus("current")


class _PowerIndex_Type(Gauge32):
    """Custom type powerIndex based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_PowerIndex_Type.__name__ = "Gauge32"
_PowerIndex_Object = MibTableColumn
powerIndex = _PowerIndex_Object(
    (1, 3, 6, 1, 4, 1, 56166, 1, 2, 3, 1, 1),
    _PowerIndex_Type()
)
powerIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    powerIndex.setStatus("current")


class _PowerType_Type(Integer32):
    """Custom type powerType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 0),
          ("ac", 1),
          ("dc", 2))
    )


_PowerType_Type.__name__ = "Integer32"
_PowerType_Object = MibTableColumn
powerType = _PowerType_Object(
    (1, 3, 6, 1, 4, 1, 56166, 1, 2, 3, 1, 2),
    _PowerType_Type()
)
powerType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerType.setStatus("current")


class _PowerState_Type(Integer32):
    """Custom type powerState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("on", 1),
          ("off", 2))
    )


_PowerState_Type.__name__ = "Integer32"
_PowerState_Object = MibTableColumn
powerState = _PowerState_Object(
    (1, 3, 6, 1, 4, 1, 56166, 1, 2, 3, 1, 3),
    _PowerState_Type()
)
powerState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    powerState.setStatus("current")
_PowerVoltage_Type = Integer32
_PowerVoltage_Object = MibTableColumn
powerVoltage = _PowerVoltage_Object(
    (1, 3, 6, 1, 4, 1, 56166, 1, 2, 3, 1, 4),
    _PowerVoltage_Type()
)
powerVoltage.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    powerVoltage.setStatus("current")
_TemperatureTable_Object = MibTable
temperatureTable = _TemperatureTable_Object(
    (1, 3, 6, 1, 4, 1, 56166, 1, 2, 4)
)
if mibBuilder.loadTexts:
    temperatureTable.setStatus("current")
_TemperatureEntry_Object = MibTableRow
temperatureEntry = _TemperatureEntry_Object(
    (1, 3, 6, 1, 4, 1, 56166, 1, 2, 4, 1)
)
temperatureEntry.setIndexNames(
    (0, "NMS-SYS-MIB", "temperatureIndex"),
)
if mibBuilder.loadTexts:
    temperatureEntry.setStatus("current")
_TemperatureIndex_Type = Integer32
_TemperatureIndex_Object = MibTableColumn
temperatureIndex = _TemperatureIndex_Object(
    (1, 3, 6, 1, 4, 1, 56166, 1, 2, 4, 1, 1),
    _TemperatureIndex_Type()
)
temperatureIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    temperatureIndex.setStatus("current")
_TemperatureValue_Type = Integer32
_TemperatureValue_Object = MibTableColumn
temperatureValue = _TemperatureValue_Object(
    (1, 3, 6, 1, 4, 1, 56166, 1, 2, 4, 1, 2),
    _TemperatureValue_Type()
)
temperatureValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    temperatureValue.setStatus("current")
_FanStatusTable_Object = MibTable
fanStatusTable = _FanStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 56166, 1, 2, 5)
)
if mibBuilder.loadTexts:
    fanStatusTable.setStatus("current")
_FanStatusEntry_Object = MibTableRow
fanStatusEntry = _FanStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 56166, 1, 2, 5, 1)
)
fanStatusEntry.setIndexNames(
    (0, "NMS-SYS-MIB", "fanIndex"),
)
if mibBuilder.loadTexts:
    fanStatusEntry.setStatus("current")
_FanIndex_Type = Integer32
_FanIndex_Object = MibTableColumn
fanIndex = _FanIndex_Object(
    (1, 3, 6, 1, 4, 1, 56166, 1, 2, 5, 1, 1),
    _FanIndex_Type()
)
fanIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fanIndex.setStatus("current")


class _FanSpeedStatus_Type(Integer32):
    """Custom type fanSpeedStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 0),
          ("low", 1),
          ("medium", 2),
          ("high", 3))
    )


_FanSpeedStatus_Type.__name__ = "Integer32"
_FanSpeedStatus_Object = MibTableColumn
fanSpeedStatus = _FanSpeedStatus_Object(
    (1, 3, 6, 1, 4, 1, 56166, 1, 2, 5, 1, 2),
    _FanSpeedStatus_Type()
)
fanSpeedStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fanSpeedStatus.setStatus("current")


class _FanStatus_Type(Integer32):
    """Custom type fanStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("normal", 1),
          ("failure", 2))
    )


_FanStatus_Type.__name__ = "Integer32"
_FanStatus_Object = MibTableColumn
fanStatus = _FanStatus_Object(
    (1, 3, 6, 1, 4, 1, 56166, 1, 2, 5, 1, 3),
    _FanStatus_Type()
)
fanStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fanStatus.setStatus("current")
_SysTraps_ObjectIdentity = ObjectIdentity
sysTraps = _SysTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 56166, 1, 2, 7)
)
_SysGroups_ObjectIdentity = ObjectIdentity
sysGroups = _SysGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 56166, 1, 2, 8)
)

# Managed Objects groups

sysTableGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 56166, 1, 2, 8, 1)
)
sysTableGroup.setObjects(
      *(("NMS-SYS-MIB", "configurationOper"),
        ("NMS-SYS-MIB", "powerOper"),
        ("NMS-SYS-MIB", "powerIndex"),
        ("NMS-SYS-MIB", "powerType"),
        ("NMS-SYS-MIB", "powerState"),
        ("NMS-SYS-MIB", "powerVoltage"))
)
if mibBuilder.loadTexts:
    sysTableGroup.setStatus("current")


# Notification objects

powerChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 56166, 1, 2, 7, 1)
)
powerChange.setObjects(
      *(("NMS-SYS-MIB", "powerIndex"),
        ("NMS-SYS-MIB", "powerType"),
        ("NMS-SYS-MIB", "powerState"),
        ("NMS-SYS-MIB", "powerVoltage"))
)
if mibBuilder.loadTexts:
    powerChange.setStatus(
        "current"
    )

batteryLow = NotificationType(
    (1, 3, 6, 1, 4, 1, 56166, 1, 2, 7, 2)
)
batteryLow.setObjects(
    ("NMS-SYS-MIB", "powerIndex")
)
if mibBuilder.loadTexts:
    batteryLow.setStatus(
        "current"
    )

batteryRecover = NotificationType(
    (1, 3, 6, 1, 4, 1, 56166, 1, 2, 7, 3)
)
batteryRecover.setObjects(
    ("NMS-SYS-MIB", "powerIndex")
)
if mibBuilder.loadTexts:
    batteryRecover.setStatus(
        "current"
    )

fanFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 56166, 1, 2, 7, 4)
)
fanFailure.setObjects(
    ("NMS-SYS-MIB", "fanIndex")
)
if mibBuilder.loadTexts:
    fanFailure.setStatus(
        "current"
    )

fanNormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 56166, 1, 2, 7, 5)
)
fanNormal.setObjects(
    ("NMS-SYS-MIB", "fanIndex")
)
if mibBuilder.loadTexts:
    fanNormal.setStatus(
        "current"
    )

fanSpeedStatusChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 56166, 1, 2, 7, 6)
)
fanSpeedStatusChange.setObjects(
      *(("NMS-SYS-MIB", "fanIndex"),
        ("NMS-SYS-MIB", "fanSpeedStatus"))
)
if mibBuilder.loadTexts:
    fanSpeedStatusChange.setStatus(
        "current"
    )


# Notifications groups

sysTrapGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 56166, 1, 2, 8, 2)
)
sysTrapGroup.setObjects(
      *(("NMS-SYS-MIB", "powerChange"),
        ("NMS-SYS-MIB", "batteryLow"),
        ("NMS-SYS-MIB", "batteryRecover"))
)
if mibBuilder.loadTexts:
    sysTrapGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "NMS-SYS-MIB",
    **{"sys": sys,
       "sysModule": sysModule,
       "cpuUtilized": cpuUtilized,
       "memUtilized": memUtilized,
       "cpuIdle": cpuIdle,
       "memTotalReal": memTotalReal,
       "memAvailReal": memAvailReal,
       "operations": operations,
       "configurationOper": configurationOper,
       "powerOper": powerOper,
       "powerTable": powerTable,
       "powerEntry": powerEntry,
       "powerIndex": powerIndex,
       "powerType": powerType,
       "powerState": powerState,
       "powerVoltage": powerVoltage,
       "temperatureTable": temperatureTable,
       "temperatureEntry": temperatureEntry,
       "temperatureIndex": temperatureIndex,
       "temperatureValue": temperatureValue,
       "fanStatusTable": fanStatusTable,
       "fanStatusEntry": fanStatusEntry,
       "fanIndex": fanIndex,
       "fanSpeedStatus": fanSpeedStatus,
       "fanStatus": fanStatus,
       "sysTraps": sysTraps,
       "powerChange": powerChange,
       "batteryLow": batteryLow,
       "batteryRecover": batteryRecover,
       "fanFailure": fanFailure,
       "fanNormal": fanNormal,
       "fanSpeedStatusChange": fanSpeedStatusChange,
       "sysGroups": sysGroups,
       "sysTableGroup": sysTableGroup,
       "sysTrapGroup": sysTrapGroup}
)
