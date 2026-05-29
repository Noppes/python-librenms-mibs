# SNMP MIB module (MOXA-FIBER-CHECK-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\moxa\MOXA-FIBER-CHECK-MIB

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

(layer2Diagnosic,) = mibBuilder.importSymbols(
    "MOXA-SWITCHING-MIB",
    "layer2Diagnosic")

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
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

mxFiberCheck = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 8691, 603, 5, 3)
)
if mibBuilder.loadTexts:
    mxFiberCheck.setRevisions(
        ("2022-02-17 00:00",
         "2021-08-02 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_FiberCheckNotification_ObjectIdentity = ObjectIdentity
fiberCheckNotification = _FiberCheckNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8691, 603, 5, 3, 0)
)
_FiberCheckConfiguration_ObjectIdentity = ObjectIdentity
fiberCheckConfiguration = _FiberCheckConfiguration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8691, 603, 5, 3, 1)
)
_FiberCheckConfigGeneral_ObjectIdentity = ObjectIdentity
fiberCheckConfigGeneral = _FiberCheckConfigGeneral_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8691, 603, 5, 3, 1, 1)
)
_FiberCheckConfigPortTable_Object = MibTable
fiberCheckConfigPortTable = _FiberCheckConfigPortTable_Object(
    (1, 3, 6, 1, 4, 1, 8691, 603, 5, 3, 1, 1, 1)
)
if mibBuilder.loadTexts:
    fiberCheckConfigPortTable.setStatus("current")
_FiberCheckConfigPortEntry_Object = MibTableRow
fiberCheckConfigPortEntry = _FiberCheckConfigPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 8691, 603, 5, 3, 1, 1, 1, 1)
)
fiberCheckConfigPortEntry.setIndexNames(
    (0, "MOXA-FIBER-CHECK-MIB", "fiberCheckConfigPortIndex"),
)
if mibBuilder.loadTexts:
    fiberCheckConfigPortEntry.setStatus("current")
_FiberCheckConfigPortIndex_Type = Integer32
_FiberCheckConfigPortIndex_Object = MibTableColumn
fiberCheckConfigPortIndex = _FiberCheckConfigPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 8691, 603, 5, 3, 1, 1, 1, 1, 1),
    _FiberCheckConfigPortIndex_Type()
)
fiberCheckConfigPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fiberCheckConfigPortIndex.setStatus("current")


class _FiberCheckConfigMode_Type(Integer32):
    """Custom type fiberCheckConfigMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("auto", 0),
          ("user-defined", 1))
    )


_FiberCheckConfigMode_Type.__name__ = "Integer32"
_FiberCheckConfigMode_Object = MibTableColumn
fiberCheckConfigMode = _FiberCheckConfigMode_Object(
    (1, 3, 6, 1, 4, 1, 8691, 603, 5, 3, 1, 1, 1, 1, 2),
    _FiberCheckConfigMode_Type()
)
fiberCheckConfigMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fiberCheckConfigMode.setStatus("current")
_FiberCheckConfigTemperatureWarnC_Type = DisplayString
_FiberCheckConfigTemperatureWarnC_Object = MibTableColumn
fiberCheckConfigTemperatureWarnC = _FiberCheckConfigTemperatureWarnC_Object(
    (1, 3, 6, 1, 4, 1, 8691, 603, 5, 3, 1, 1, 1, 1, 3),
    _FiberCheckConfigTemperatureWarnC_Type()
)
fiberCheckConfigTemperatureWarnC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fiberCheckConfigTemperatureWarnC.setStatus("current")
_FiberCheckConfigTemperatureWarnF_Type = DisplayString
_FiberCheckConfigTemperatureWarnF_Object = MibTableColumn
fiberCheckConfigTemperatureWarnF = _FiberCheckConfigTemperatureWarnF_Object(
    (1, 3, 6, 1, 4, 1, 8691, 603, 5, 3, 1, 1, 1, 1, 4),
    _FiberCheckConfigTemperatureWarnF_Type()
)
fiberCheckConfigTemperatureWarnF.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fiberCheckConfigTemperatureWarnF.setStatus("current")
_FiberCheckConfigTxPowerWarnHigh_Type = DisplayString
_FiberCheckConfigTxPowerWarnHigh_Object = MibTableColumn
fiberCheckConfigTxPowerWarnHigh = _FiberCheckConfigTxPowerWarnHigh_Object(
    (1, 3, 6, 1, 4, 1, 8691, 603, 5, 3, 1, 1, 1, 1, 5),
    _FiberCheckConfigTxPowerWarnHigh_Type()
)
fiberCheckConfigTxPowerWarnHigh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fiberCheckConfigTxPowerWarnHigh.setStatus("current")
_FiberCheckConfigTxPowerWarnLow_Type = DisplayString
_FiberCheckConfigTxPowerWarnLow_Object = MibTableColumn
fiberCheckConfigTxPowerWarnLow = _FiberCheckConfigTxPowerWarnLow_Object(
    (1, 3, 6, 1, 4, 1, 8691, 603, 5, 3, 1, 1, 1, 1, 6),
    _FiberCheckConfigTxPowerWarnLow_Type()
)
fiberCheckConfigTxPowerWarnLow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fiberCheckConfigTxPowerWarnLow.setStatus("current")
_FiberCheckConfigRxPowerWarnHigh_Type = DisplayString
_FiberCheckConfigRxPowerWarnHigh_Object = MibTableColumn
fiberCheckConfigRxPowerWarnHigh = _FiberCheckConfigRxPowerWarnHigh_Object(
    (1, 3, 6, 1, 4, 1, 8691, 603, 5, 3, 1, 1, 1, 1, 7),
    _FiberCheckConfigRxPowerWarnHigh_Type()
)
fiberCheckConfigRxPowerWarnHigh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fiberCheckConfigRxPowerWarnHigh.setStatus("current")
_FiberCheckConfigRxPowerWarnLow_Type = DisplayString
_FiberCheckConfigRxPowerWarnLow_Object = MibTableColumn
fiberCheckConfigRxPowerWarnLow = _FiberCheckConfigRxPowerWarnLow_Object(
    (1, 3, 6, 1, 4, 1, 8691, 603, 5, 3, 1, 1, 1, 1, 8),
    _FiberCheckConfigRxPowerWarnLow_Type()
)
fiberCheckConfigRxPowerWarnLow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fiberCheckConfigRxPowerWarnLow.setStatus("current")
_FiberCheckConfigResetToDefault_Type = TruthValue
_FiberCheckConfigResetToDefault_Object = MibTableColumn
fiberCheckConfigResetToDefault = _FiberCheckConfigResetToDefault_Object(
    (1, 3, 6, 1, 4, 1, 8691, 603, 5, 3, 1, 1, 1, 1, 9),
    _FiberCheckConfigResetToDefault_Type()
)
fiberCheckConfigResetToDefault.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fiberCheckConfigResetToDefault.setStatus("current")
_FiberCheckStatus_ObjectIdentity = ObjectIdentity
fiberCheckStatus = _FiberCheckStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8691, 603, 5, 3, 2)
)
_FiberCheckStatMonitor_ObjectIdentity = ObjectIdentity
fiberCheckStatMonitor = _FiberCheckStatMonitor_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8691, 603, 5, 3, 2, 1)
)
_FiberCheckStatPortTable_Object = MibTable
fiberCheckStatPortTable = _FiberCheckStatPortTable_Object(
    (1, 3, 6, 1, 4, 1, 8691, 603, 5, 3, 2, 1, 1)
)
if mibBuilder.loadTexts:
    fiberCheckStatPortTable.setStatus("current")
_FiberCheckStatPortEntry_Object = MibTableRow
fiberCheckStatPortEntry = _FiberCheckStatPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 8691, 603, 5, 3, 2, 1, 1, 1)
)
fiberCheckStatPortEntry.setIndexNames(
    (0, "MOXA-FIBER-CHECK-MIB", "fiberCheckStatPortIndex"),
)
if mibBuilder.loadTexts:
    fiberCheckStatPortEntry.setStatus("current")
_FiberCheckStatPortIndex_Type = Integer32
_FiberCheckStatPortIndex_Object = MibTableColumn
fiberCheckStatPortIndex = _FiberCheckStatPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 8691, 603, 5, 3, 2, 1, 1, 1, 1),
    _FiberCheckStatPortIndex_Type()
)
fiberCheckStatPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fiberCheckStatPortIndex.setStatus("current")
_FiberCheckStatModelName_Type = DisplayString
_FiberCheckStatModelName_Object = MibTableColumn
fiberCheckStatModelName = _FiberCheckStatModelName_Object(
    (1, 3, 6, 1, 4, 1, 8691, 603, 5, 3, 2, 1, 1, 1, 2),
    _FiberCheckStatModelName_Type()
)
fiberCheckStatModelName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fiberCheckStatModelName.setStatus("current")
_FiberCheckStatSN_Type = DisplayString
_FiberCheckStatSN_Object = MibTableColumn
fiberCheckStatSN = _FiberCheckStatSN_Object(
    (1, 3, 6, 1, 4, 1, 8691, 603, 5, 3, 2, 1, 1, 1, 3),
    _FiberCheckStatSN_Type()
)
fiberCheckStatSN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fiberCheckStatSN.setStatus("current")
_FiberCheckStatWaveLength_Type = Integer32
_FiberCheckStatWaveLength_Object = MibTableColumn
fiberCheckStatWaveLength = _FiberCheckStatWaveLength_Object(
    (1, 3, 6, 1, 4, 1, 8691, 603, 5, 3, 2, 1, 1, 1, 4),
    _FiberCheckStatWaveLength_Type()
)
fiberCheckStatWaveLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fiberCheckStatWaveLength.setStatus("current")
_FiberCheckStatTemperatureC_Type = DisplayString
_FiberCheckStatTemperatureC_Object = MibTableColumn
fiberCheckStatTemperatureC = _FiberCheckStatTemperatureC_Object(
    (1, 3, 6, 1, 4, 1, 8691, 603, 5, 3, 2, 1, 1, 1, 5),
    _FiberCheckStatTemperatureC_Type()
)
fiberCheckStatTemperatureC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fiberCheckStatTemperatureC.setStatus("current")
_FiberCheckStatTemperatureF_Type = DisplayString
_FiberCheckStatTemperatureF_Object = MibTableColumn
fiberCheckStatTemperatureF = _FiberCheckStatTemperatureF_Object(
    (1, 3, 6, 1, 4, 1, 8691, 603, 5, 3, 2, 1, 1, 1, 6),
    _FiberCheckStatTemperatureF_Type()
)
fiberCheckStatTemperatureF.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fiberCheckStatTemperatureF.setStatus("current")
_FiberCheckStatVoltage_Type = DisplayString
_FiberCheckStatVoltage_Object = MibTableColumn
fiberCheckStatVoltage = _FiberCheckStatVoltage_Object(
    (1, 3, 6, 1, 4, 1, 8691, 603, 5, 3, 2, 1, 1, 1, 7),
    _FiberCheckStatVoltage_Type()
)
fiberCheckStatVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fiberCheckStatVoltage.setStatus("current")
_FiberCheckStatTxPower_Type = DisplayString
_FiberCheckStatTxPower_Object = MibTableColumn
fiberCheckStatTxPower = _FiberCheckStatTxPower_Object(
    (1, 3, 6, 1, 4, 1, 8691, 603, 5, 3, 2, 1, 1, 1, 8),
    _FiberCheckStatTxPower_Type()
)
fiberCheckStatTxPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fiberCheckStatTxPower.setStatus("current")
_FiberCheckStatRxPower_Type = DisplayString
_FiberCheckStatRxPower_Object = MibTableColumn
fiberCheckStatRxPower = _FiberCheckStatRxPower_Object(
    (1, 3, 6, 1, 4, 1, 8691, 603, 5, 3, 2, 1, 1, 1, 9),
    _FiberCheckStatRxPower_Type()
)
fiberCheckStatRxPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fiberCheckStatRxPower.setStatus("current")
_FiberCheckStatTemperatureLimitC_Type = DisplayString
_FiberCheckStatTemperatureLimitC_Object = MibTableColumn
fiberCheckStatTemperatureLimitC = _FiberCheckStatTemperatureLimitC_Object(
    (1, 3, 6, 1, 4, 1, 8691, 603, 5, 3, 2, 1, 1, 1, 10),
    _FiberCheckStatTemperatureLimitC_Type()
)
fiberCheckStatTemperatureLimitC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fiberCheckStatTemperatureLimitC.setStatus("current")
_FiberCheckStatTemperatureLimitF_Type = DisplayString
_FiberCheckStatTemperatureLimitF_Object = MibTableColumn
fiberCheckStatTemperatureLimitF = _FiberCheckStatTemperatureLimitF_Object(
    (1, 3, 6, 1, 4, 1, 8691, 603, 5, 3, 2, 1, 1, 1, 11),
    _FiberCheckStatTemperatureLimitF_Type()
)
fiberCheckStatTemperatureLimitF.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fiberCheckStatTemperatureLimitF.setStatus("current")
_FiberCheckStatTxPowerLimit_Type = DisplayString
_FiberCheckStatTxPowerLimit_Object = MibTableColumn
fiberCheckStatTxPowerLimit = _FiberCheckStatTxPowerLimit_Object(
    (1, 3, 6, 1, 4, 1, 8691, 603, 5, 3, 2, 1, 1, 1, 12),
    _FiberCheckStatTxPowerLimit_Type()
)
fiberCheckStatTxPowerLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fiberCheckStatTxPowerLimit.setStatus("current")
_FiberCheckStatRxPowerLimit_Type = DisplayString
_FiberCheckStatRxPowerLimit_Object = MibTableColumn
fiberCheckStatRxPowerLimit = _FiberCheckStatRxPowerLimit_Object(
    (1, 3, 6, 1, 4, 1, 8691, 603, 5, 3, 2, 1, 1, 1, 13),
    _FiberCheckStatRxPowerLimit_Type()
)
fiberCheckStatRxPowerLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fiberCheckStatRxPowerLimit.setStatus("current")

# Managed Objects groups


# Notification objects

fiberCheckNotifyFiberCheckWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 8691, 603, 5, 3, 0, 1)
)
fiberCheckNotifyFiberCheckWarning.setObjects(
    ("MOXA-FIBER-CHECK-MIB", "fiberCheckStatPortIndex")
)
if mibBuilder.loadTexts:
    fiberCheckNotifyFiberCheckWarning.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "MOXA-FIBER-CHECK-MIB",
    **{"mxFiberCheck": mxFiberCheck,
       "fiberCheckNotification": fiberCheckNotification,
       "fiberCheckNotifyFiberCheckWarning": fiberCheckNotifyFiberCheckWarning,
       "fiberCheckConfiguration": fiberCheckConfiguration,
       "fiberCheckConfigGeneral": fiberCheckConfigGeneral,
       "fiberCheckConfigPortTable": fiberCheckConfigPortTable,
       "fiberCheckConfigPortEntry": fiberCheckConfigPortEntry,
       "fiberCheckConfigPortIndex": fiberCheckConfigPortIndex,
       "fiberCheckConfigMode": fiberCheckConfigMode,
       "fiberCheckConfigTemperatureWarnC": fiberCheckConfigTemperatureWarnC,
       "fiberCheckConfigTemperatureWarnF": fiberCheckConfigTemperatureWarnF,
       "fiberCheckConfigTxPowerWarnHigh": fiberCheckConfigTxPowerWarnHigh,
       "fiberCheckConfigTxPowerWarnLow": fiberCheckConfigTxPowerWarnLow,
       "fiberCheckConfigRxPowerWarnHigh": fiberCheckConfigRxPowerWarnHigh,
       "fiberCheckConfigRxPowerWarnLow": fiberCheckConfigRxPowerWarnLow,
       "fiberCheckConfigResetToDefault": fiberCheckConfigResetToDefault,
       "fiberCheckStatus": fiberCheckStatus,
       "fiberCheckStatMonitor": fiberCheckStatMonitor,
       "fiberCheckStatPortTable": fiberCheckStatPortTable,
       "fiberCheckStatPortEntry": fiberCheckStatPortEntry,
       "fiberCheckStatPortIndex": fiberCheckStatPortIndex,
       "fiberCheckStatModelName": fiberCheckStatModelName,
       "fiberCheckStatSN": fiberCheckStatSN,
       "fiberCheckStatWaveLength": fiberCheckStatWaveLength,
       "fiberCheckStatTemperatureC": fiberCheckStatTemperatureC,
       "fiberCheckStatTemperatureF": fiberCheckStatTemperatureF,
       "fiberCheckStatVoltage": fiberCheckStatVoltage,
       "fiberCheckStatTxPower": fiberCheckStatTxPower,
       "fiberCheckStatRxPower": fiberCheckStatRxPower,
       "fiberCheckStatTemperatureLimitC": fiberCheckStatTemperatureLimitC,
       "fiberCheckStatTemperatureLimitF": fiberCheckStatTemperatureLimitF,
       "fiberCheckStatTxPowerLimit": fiberCheckStatTxPowerLimit,
       "fiberCheckStatRxPowerLimit": fiberCheckStatRxPowerLimit}
)
