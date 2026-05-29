# SNMP MIB module (G6-POE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\microsens\G6-POE-MIB

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

(g6,) = mibBuilder.importSymbols(
    "MICROSENS-G6-MIB",
    "g6")

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
 enterprises,
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
    "enterprises",
    "iso")

(DisplayString,
 MacAddress,
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

device = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1)
)
if mibBuilder.loadTexts:
    device.setRevisions(
        ("2023-02-14 11:27",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Poe_ObjectIdentity = ObjectIdentity
poe = _Poe_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 33)
)


class _PoePoeMaxPowerAvailable_Type(Integer32):
    """Custom type poePoeMaxPowerAvailable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_PoePoeMaxPowerAvailable_Type.__name__ = "Integer32"
_PoePoeMaxPowerAvailable_Object = MibScalar
poePoeMaxPowerAvailable = _PoePoeMaxPowerAvailable_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 33, 1),
    _PoePoeMaxPowerAvailable_Type()
)
poePoeMaxPowerAvailable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    poePoeMaxPowerAvailable.setStatus("current")
_PoeRestartPoePort_Type = DisplayString
_PoeRestartPoePort_Object = MibScalar
poeRestartPoePort = _PoeRestartPoePort_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 33, 2),
    _PoeRestartPoePort_Type()
)
poeRestartPoePort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    poeRestartPoePort.setStatus("current")
_PoeRestartEnergyPort_Type = DisplayString
_PoeRestartEnergyPort_Object = MibScalar
poeRestartEnergyPort = _PoeRestartEnergyPort_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 33, 3),
    _PoeRestartEnergyPort_Type()
)
poeRestartEnergyPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    poeRestartEnergyPort.setStatus("current")
_ConfigTable_Object = MibTable
configTable = _ConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 33, 4)
)
if mibBuilder.loadTexts:
    configTable.setStatus("current")
_ConfigEntry_Object = MibTableRow
configEntry = _ConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 33, 4, 1)
)
configEntry.setIndexNames(
    (0, "G6-POE-MIB", "configPortIndex"),
)
if mibBuilder.loadTexts:
    configEntry.setStatus("current")


class _ConfigPortIndex_Type(Integer32):
    """Custom type configPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 24),
    )


_ConfigPortIndex_Type.__name__ = "Integer32"
_ConfigPortIndex_Object = MibTableColumn
configPortIndex = _ConfigPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 33, 4, 1, 1),
    _ConfigPortIndex_Type()
)
configPortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    configPortIndex.setStatus("current")


class _ConfigMode_Type(Integer32):
    """Custom type configMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("automatic", 1),
          ("class0", 2),
          ("class1", 3),
          ("class2", 4),
          ("class3", 5),
          ("class4", 6),
          ("forcedOn", 7))
    )


_ConfigMode_Type.__name__ = "Integer32"
_ConfigMode_Object = MibTableColumn
configMode = _ConfigMode_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 33, 4, 1, 2),
    _ConfigMode_Type()
)
configMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configMode.setStatus("current")


class _ConfigPriorityPort_Type(Integer32):
    """Custom type configPriorityPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_ConfigPriorityPort_Type.__name__ = "Integer32"
_ConfigPriorityPort_Object = MibTableColumn
configPriorityPort = _ConfigPriorityPort_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 33, 4, 1, 3),
    _ConfigPriorityPort_Type()
)
configPriorityPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configPriorityPort.setStatus("current")


class _ConfigEnablePoePlus_Type(Integer32):
    """Custom type configEnablePoePlus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1),
          ("lldpControlled", 2))
    )


_ConfigEnablePoePlus_Type.__name__ = "Integer32"
_ConfigEnablePoePlus_Object = MibTableColumn
configEnablePoePlus = _ConfigEnablePoePlus_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 33, 4, 1, 4),
    _ConfigEnablePoePlus_Type()
)
configEnablePoePlus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configEnablePoePlus.setStatus("current")
_WatchdogTable_Object = MibTable
watchdogTable = _WatchdogTable_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 33, 5)
)
if mibBuilder.loadTexts:
    watchdogTable.setStatus("current")
_WatchdogEntry_Object = MibTableRow
watchdogEntry = _WatchdogEntry_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 33, 5, 1)
)
watchdogEntry.setIndexNames(
    (0, "G6-POE-MIB", "watchdogPortIndex"),
)
if mibBuilder.loadTexts:
    watchdogEntry.setStatus("current")


class _WatchdogPortIndex_Type(Integer32):
    """Custom type watchdogPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 24),
    )


_WatchdogPortIndex_Type.__name__ = "Integer32"
_WatchdogPortIndex_Object = MibTableColumn
watchdogPortIndex = _WatchdogPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 33, 5, 1, 1),
    _WatchdogPortIndex_Type()
)
watchdogPortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    watchdogPortIndex.setStatus("current")


class _WatchdogTestMethod_Type(Integer32):
    """Custom type watchdogTestMethod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("ping", 1),
          ("rmon", 2))
    )


_WatchdogTestMethod_Type.__name__ = "Integer32"
_WatchdogTestMethod_Object = MibTableColumn
watchdogTestMethod = _WatchdogTestMethod_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 33, 5, 1, 2),
    _WatchdogTestMethod_Type()
)
watchdogTestMethod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    watchdogTestMethod.setStatus("current")
_WatchdogStartDelay_Type = Unsigned32
_WatchdogStartDelay_Object = MibTableColumn
watchdogStartDelay = _WatchdogStartDelay_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 33, 5, 1, 3),
    _WatchdogStartDelay_Type()
)
watchdogStartDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    watchdogStartDelay.setStatus("current")
_WatchdogCheckInterval_Type = Unsigned32
_WatchdogCheckInterval_Object = MibTableColumn
watchdogCheckInterval = _WatchdogCheckInterval_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 33, 5, 1, 4),
    _WatchdogCheckInterval_Type()
)
watchdogCheckInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    watchdogCheckInterval.setStatus("current")
_WatchdogRecheckInterval_Type = Unsigned32
_WatchdogRecheckInterval_Object = MibTableColumn
watchdogRecheckInterval = _WatchdogRecheckInterval_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 33, 5, 1, 5),
    _WatchdogRecheckInterval_Type()
)
watchdogRecheckInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    watchdogRecheckInterval.setStatus("current")
_WatchdogTolerableFailures_Type = Unsigned32
_WatchdogTolerableFailures_Object = MibTableColumn
watchdogTolerableFailures = _WatchdogTolerableFailures_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 33, 5, 1, 6),
    _WatchdogTolerableFailures_Type()
)
watchdogTolerableFailures.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    watchdogTolerableFailures.setStatus("current")
_WatchdogMinimumRmonPackets_Type = Unsigned32
_WatchdogMinimumRmonPackets_Object = MibTableColumn
watchdogMinimumRmonPackets = _WatchdogMinimumRmonPackets_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 33, 5, 1, 7),
    _WatchdogMinimumRmonPackets_Type()
)
watchdogMinimumRmonPackets.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    watchdogMinimumRmonPackets.setStatus("current")
_WatchdogCheckedAddress_Type = DisplayString
_WatchdogCheckedAddress_Object = MibTableColumn
watchdogCheckedAddress = _WatchdogCheckedAddress_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 33, 5, 1, 8),
    _WatchdogCheckedAddress_Type()
)
watchdogCheckedAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    watchdogCheckedAddress.setStatus("current")
_WatchdogClearStatistics_Type = DisplayString
_WatchdogClearStatistics_Object = MibTableColumn
watchdogClearStatistics = _WatchdogClearStatistics_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 33, 5, 1, 9),
    _WatchdogClearStatistics_Type()
)
watchdogClearStatistics.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    watchdogClearStatistics.setStatus("current")
_PoeTotalPowerConsumed_Type = Unsigned32
_PoeTotalPowerConsumed_Object = MibScalar
poeTotalPowerConsumed = _PoeTotalPowerConsumed_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 33, 100),
    _PoeTotalPowerConsumed_Type()
)
poeTotalPowerConsumed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    poeTotalPowerConsumed.setStatus("current")
_StatusTable_Object = MibTable
statusTable = _StatusTable_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 33, 101)
)
if mibBuilder.loadTexts:
    statusTable.setStatus("current")
_StatusEntry_Object = MibTableRow
statusEntry = _StatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 33, 101, 1)
)
statusEntry.setIndexNames(
    (0, "G6-POE-MIB", "statusPortIndex"),
)
if mibBuilder.loadTexts:
    statusEntry.setStatus("current")


class _StatusPortIndex_Type(Integer32):
    """Custom type statusPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 31),
    )


_StatusPortIndex_Type.__name__ = "Integer32"
_StatusPortIndex_Object = MibTableColumn
statusPortIndex = _StatusPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 33, 101, 1, 1),
    _StatusPortIndex_Type()
)
statusPortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    statusPortIndex.setStatus("current")


class _StatusCondition_Type(Integer32):
    """Custom type statusCondition based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("powerOff", 1),
          ("discovering", 2),
          ("powered", 3),
          ("classMismatch", 4),
          ("shortCircuit", 5),
          ("rejected", 6),
          ("overCurrent", 7),
          ("overTemp", 8),
          ("voltageTooLow", 9))
    )


_StatusCondition_Type.__name__ = "Integer32"
_StatusCondition_Object = MibTableColumn
statusCondition = _StatusCondition_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 33, 101, 1, 2),
    _StatusCondition_Type()
)
statusCondition.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statusCondition.setStatus("current")


class _StatusDeterminedClass_Type(Integer32):
    """Custom type statusDeterminedClass based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              7,
              255)
        )
    )
    namedValues = NamedValues(
        *(("isClass0", 0),
          ("isClass1", 1),
          ("isClass2", 2),
          ("isClass3", 3),
          ("isClass4", 4),
          ("isOverload", 5),
          ("probesNotEqual", 7),
          ("isUnknown", 255))
    )


_StatusDeterminedClass_Type.__name__ = "Integer32"
_StatusDeterminedClass_Object = MibTableColumn
statusDeterminedClass = _StatusDeterminedClass_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 33, 101, 1, 3),
    _StatusDeterminedClass_Type()
)
statusDeterminedClass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statusDeterminedClass.setStatus("current")


class _StatusOutputCurrent_Type(Integer32):
    """Custom type statusOutputCurrent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_StatusOutputCurrent_Type.__name__ = "Integer32"
_StatusOutputCurrent_Object = MibTableColumn
statusOutputCurrent = _StatusOutputCurrent_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 33, 101, 1, 4),
    _StatusOutputCurrent_Type()
)
statusOutputCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statusOutputCurrent.setStatus("current")


class _StatusOutputVoltage_Type(Integer32):
    """Custom type statusOutputVoltage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_StatusOutputVoltage_Type.__name__ = "Integer32"
_StatusOutputVoltage_Object = MibTableColumn
statusOutputVoltage = _StatusOutputVoltage_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 33, 101, 1, 5),
    _StatusOutputVoltage_Type()
)
statusOutputVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statusOutputVoltage.setStatus("current")


class _StatusOutputPower_Type(Integer32):
    """Custom type statusOutputPower based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_StatusOutputPower_Type.__name__ = "Integer32"
_StatusOutputPower_Object = MibTableColumn
statusOutputPower = _StatusOutputPower_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 33, 101, 1, 6),
    _StatusOutputPower_Type()
)
statusOutputPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statusOutputPower.setStatus("current")
_StatusPowerDeniedCounter_Type = Unsigned32
_StatusPowerDeniedCounter_Object = MibTableColumn
statusPowerDeniedCounter = _StatusPowerDeniedCounter_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 33, 101, 1, 7),
    _StatusPowerDeniedCounter_Type()
)
statusPowerDeniedCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statusPowerDeniedCounter.setStatus("current")
_StatusOverCurrentCounter_Type = Unsigned32
_StatusOverCurrentCounter_Object = MibTableColumn
statusOverCurrentCounter = _StatusOverCurrentCounter_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 33, 101, 1, 8),
    _StatusOverCurrentCounter_Type()
)
statusOverCurrentCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statusOverCurrentCounter.setStatus("current")
_StatusShortCircuitCounter_Type = Unsigned32
_StatusShortCircuitCounter_Object = MibTableColumn
statusShortCircuitCounter = _StatusShortCircuitCounter_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 33, 101, 1, 9),
    _StatusShortCircuitCounter_Type()
)
statusShortCircuitCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statusShortCircuitCounter.setStatus("current")
_StatusNumberOfChecks_Type = Unsigned32
_StatusNumberOfChecks_Object = MibTableColumn
statusNumberOfChecks = _StatusNumberOfChecks_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 33, 101, 1, 10),
    _StatusNumberOfChecks_Type()
)
statusNumberOfChecks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statusNumberOfChecks.setStatus("current")
_StatusNumberOfFailures_Type = Unsigned32
_StatusNumberOfFailures_Object = MibTableColumn
statusNumberOfFailures = _StatusNumberOfFailures_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 33, 101, 1, 11),
    _StatusNumberOfFailures_Type()
)
statusNumberOfFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statusNumberOfFailures.setStatus("current")
_StatusPoeRestartCounter_Type = Unsigned32
_StatusPoeRestartCounter_Object = MibTableColumn
statusPoeRestartCounter = _StatusPoeRestartCounter_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 33, 101, 1, 12),
    _StatusPoeRestartCounter_Type()
)
statusPoeRestartCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statusPoeRestartCounter.setStatus("current")
_EnergySuppliedTable_Object = MibTable
energySuppliedTable = _EnergySuppliedTable_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 33, 102)
)
if mibBuilder.loadTexts:
    energySuppliedTable.setStatus("current")
_EnergySuppliedEntry_Object = MibTableRow
energySuppliedEntry = _EnergySuppliedEntry_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 33, 102, 1)
)
energySuppliedEntry.setIndexNames(
    (0, "G6-POE-MIB", "energySuppliedPortIndex"),
)
if mibBuilder.loadTexts:
    energySuppliedEntry.setStatus("current")


class _EnergySuppliedPortIndex_Type(Integer32):
    """Custom type energySuppliedPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 31),
    )


_EnergySuppliedPortIndex_Type.__name__ = "Integer32"
_EnergySuppliedPortIndex_Object = MibTableColumn
energySuppliedPortIndex = _EnergySuppliedPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 33, 102, 1, 1),
    _EnergySuppliedPortIndex_Type()
)
energySuppliedPortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    energySuppliedPortIndex.setStatus("current")
_EnergySuppliedTimeOfValueRestart_Type = Counter32
_EnergySuppliedTimeOfValueRestart_Object = MibTableColumn
energySuppliedTimeOfValueRestart = _EnergySuppliedTimeOfValueRestart_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 33, 102, 1, 2),
    _EnergySuppliedTimeOfValueRestart_Type()
)
energySuppliedTimeOfValueRestart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    energySuppliedTimeOfValueRestart.setStatus("current")
_EnergySuppliedTimeSinceValueRestart_Type = Counter32
_EnergySuppliedTimeSinceValueRestart_Object = MibTableColumn
energySuppliedTimeSinceValueRestart = _EnergySuppliedTimeSinceValueRestart_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 33, 102, 1, 3),
    _EnergySuppliedTimeSinceValueRestart_Type()
)
energySuppliedTimeSinceValueRestart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    energySuppliedTimeSinceValueRestart.setStatus("current")
_EnergySuppliedLastSecond_Type = Unsigned32
_EnergySuppliedLastSecond_Object = MibTableColumn
energySuppliedLastSecond = _EnergySuppliedLastSecond_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 33, 102, 1, 4),
    _EnergySuppliedLastSecond_Type()
)
energySuppliedLastSecond.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    energySuppliedLastSecond.setStatus("current")
_EnergySuppliedAccumulated_Type = Unsigned32
_EnergySuppliedAccumulated_Object = MibTableColumn
energySuppliedAccumulated = _EnergySuppliedAccumulated_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 33, 102, 1, 5),
    _EnergySuppliedAccumulated_Type()
)
energySuppliedAccumulated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    energySuppliedAccumulated.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "G6-POE-MIB",
    **{"device": device,
       "poe": poe,
       "poePoeMaxPowerAvailable": poePoeMaxPowerAvailable,
       "poeRestartPoePort": poeRestartPoePort,
       "poeRestartEnergyPort": poeRestartEnergyPort,
       "configTable": configTable,
       "configEntry": configEntry,
       "configPortIndex": configPortIndex,
       "configMode": configMode,
       "configPriorityPort": configPriorityPort,
       "configEnablePoePlus": configEnablePoePlus,
       "watchdogTable": watchdogTable,
       "watchdogEntry": watchdogEntry,
       "watchdogPortIndex": watchdogPortIndex,
       "watchdogTestMethod": watchdogTestMethod,
       "watchdogStartDelay": watchdogStartDelay,
       "watchdogCheckInterval": watchdogCheckInterval,
       "watchdogRecheckInterval": watchdogRecheckInterval,
       "watchdogTolerableFailures": watchdogTolerableFailures,
       "watchdogMinimumRmonPackets": watchdogMinimumRmonPackets,
       "watchdogCheckedAddress": watchdogCheckedAddress,
       "watchdogClearStatistics": watchdogClearStatistics,
       "poeTotalPowerConsumed": poeTotalPowerConsumed,
       "statusTable": statusTable,
       "statusEntry": statusEntry,
       "statusPortIndex": statusPortIndex,
       "statusCondition": statusCondition,
       "statusDeterminedClass": statusDeterminedClass,
       "statusOutputCurrent": statusOutputCurrent,
       "statusOutputVoltage": statusOutputVoltage,
       "statusOutputPower": statusOutputPower,
       "statusPowerDeniedCounter": statusPowerDeniedCounter,
       "statusOverCurrentCounter": statusOverCurrentCounter,
       "statusShortCircuitCounter": statusShortCircuitCounter,
       "statusNumberOfChecks": statusNumberOfChecks,
       "statusNumberOfFailures": statusNumberOfFailures,
       "statusPoeRestartCounter": statusPoeRestartCounter,
       "energySuppliedTable": energySuppliedTable,
       "energySuppliedEntry": energySuppliedEntry,
       "energySuppliedPortIndex": energySuppliedPortIndex,
       "energySuppliedTimeOfValueRestart": energySuppliedTimeOfValueRestart,
       "energySuppliedTimeSinceValueRestart": energySuppliedTimeSinceValueRestart,
       "energySuppliedLastSecond": energySuppliedLastSecond,
       "energySuppliedAccumulated": energySuppliedAccumulated}
)
