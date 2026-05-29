# SNMP MIB module (ALPHA-RECTIFIER-SYS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\alpha\ALPHA-RECTIFIER-SYS-MIB

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

(ScaledNumber,
 simple) = mibBuilder.importSymbols(
    "ALPHA-RESOURCE-MIB",
    "ScaledNumber",
    "simple")

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

rectifierSystem = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 7309, 5, 3, 1)
)
if mibBuilder.loadTexts:
    rectifierSystem.setRevisions(
        ("2019-12-12 00:00",
         "2017-04-06 00:00",
         "2015-07-28 00:00",
         "2015-07-23 00:00",
         "2015-06-23 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_RectSysTotalOutputCurrent_Type = ScaledNumber
_RectSysTotalOutputCurrent_Object = MibScalar
rectSysTotalOutputCurrent = _RectSysTotalOutputCurrent_Object(
    (1, 3, 6, 1, 4, 1, 7309, 5, 3, 1, 1),
    _RectSysTotalOutputCurrent_Type()
)
rectSysTotalOutputCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rectSysTotalOutputCurrent.setStatus("current")
_RectSysTotalOutputPower_Type = ScaledNumber
_RectSysTotalOutputPower_Object = MibScalar
rectSysTotalOutputPower = _RectSysTotalOutputPower_Object(
    (1, 3, 6, 1, 4, 1, 7309, 5, 3, 1, 2),
    _RectSysTotalOutputPower_Type()
)
rectSysTotalOutputPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rectSysTotalOutputPower.setStatus("current")
_RectSysTotalCapacityInstalledAmps_Type = ScaledNumber
_RectSysTotalCapacityInstalledAmps_Object = MibScalar
rectSysTotalCapacityInstalledAmps = _RectSysTotalCapacityInstalledAmps_Object(
    (1, 3, 6, 1, 4, 1, 7309, 5, 3, 1, 3),
    _RectSysTotalCapacityInstalledAmps_Type()
)
rectSysTotalCapacityInstalledAmps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rectSysTotalCapacityInstalledAmps.setStatus("current")
_RectSysTotalCapacityInstalledPower_Type = ScaledNumber
_RectSysTotalCapacityInstalledPower_Object = MibScalar
rectSysTotalCapacityInstalledPower = _RectSysTotalCapacityInstalledPower_Object(
    (1, 3, 6, 1, 4, 1, 7309, 5, 3, 1, 4),
    _RectSysTotalCapacityInstalledPower_Type()
)
rectSysTotalCapacityInstalledPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rectSysTotalCapacityInstalledPower.setStatus("current")
_RectSysAverageRectifierOutputVoltage_Type = ScaledNumber
_RectSysAverageRectifierOutputVoltage_Object = MibScalar
rectSysAverageRectifierOutputVoltage = _RectSysAverageRectifierOutputVoltage_Object(
    (1, 3, 6, 1, 4, 1, 7309, 5, 3, 1, 5),
    _RectSysAverageRectifierOutputVoltage_Type()
)
rectSysAverageRectifierOutputVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rectSysAverageRectifierOutputVoltage.setStatus("current")
_RectSysAverageRectifierACInputVoltage_Type = ScaledNumber
_RectSysAverageRectifierACInputVoltage_Object = MibScalar
rectSysAverageRectifierACInputVoltage = _RectSysAverageRectifierACInputVoltage_Object(
    (1, 3, 6, 1, 4, 1, 7309, 5, 3, 1, 6),
    _RectSysAverageRectifierACInputVoltage_Type()
)
rectSysAverageRectifierACInputVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rectSysAverageRectifierACInputVoltage.setStatus("current")
_RectSysAveragePhase1Voltage_Type = ScaledNumber
_RectSysAveragePhase1Voltage_Object = MibScalar
rectSysAveragePhase1Voltage = _RectSysAveragePhase1Voltage_Object(
    (1, 3, 6, 1, 4, 1, 7309, 5, 3, 1, 7),
    _RectSysAveragePhase1Voltage_Type()
)
rectSysAveragePhase1Voltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rectSysAveragePhase1Voltage.setStatus("current")
_RectSysAveragePhase2Voltage_Type = ScaledNumber
_RectSysAveragePhase2Voltage_Object = MibScalar
rectSysAveragePhase2Voltage = _RectSysAveragePhase2Voltage_Object(
    (1, 3, 6, 1, 4, 1, 7309, 5, 3, 1, 8),
    _RectSysAveragePhase2Voltage_Type()
)
rectSysAveragePhase2Voltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rectSysAveragePhase2Voltage.setStatus("current")
_RectSysAveragePhase3Voltage_Type = ScaledNumber
_RectSysAveragePhase3Voltage_Object = MibScalar
rectSysAveragePhase3Voltage = _RectSysAveragePhase3Voltage_Object(
    (1, 3, 6, 1, 4, 1, 7309, 5, 3, 1, 9),
    _RectSysAveragePhase3Voltage_Type()
)
rectSysAveragePhase3Voltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rectSysAveragePhase3Voltage.setStatus("current")
_RectSysSystemVoltage_Type = ScaledNumber
_RectSysSystemVoltage_Object = MibScalar
rectSysSystemVoltage = _RectSysSystemVoltage_Object(
    (1, 3, 6, 1, 4, 1, 7309, 5, 3, 1, 10),
    _RectSysSystemVoltage_Type()
)
rectSysSystemVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rectSysSystemVoltage.setStatus("current")
_RectSysTotalLoadCurrent_Type = ScaledNumber
_RectSysTotalLoadCurrent_Object = MibScalar
rectSysTotalLoadCurrent = _RectSysTotalLoadCurrent_Object(
    (1, 3, 6, 1, 4, 1, 7309, 5, 3, 1, 11),
    _RectSysTotalLoadCurrent_Type()
)
rectSysTotalLoadCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rectSysTotalLoadCurrent.setStatus("current")
_RectSysBatteryVoltage_Type = ScaledNumber
_RectSysBatteryVoltage_Object = MibScalar
rectSysBatteryVoltage = _RectSysBatteryVoltage_Object(
    (1, 3, 6, 1, 4, 1, 7309, 5, 3, 1, 12),
    _RectSysBatteryVoltage_Type()
)
rectSysBatteryVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rectSysBatteryVoltage.setStatus("current")
_RectSysBatteryCurrent_Type = ScaledNumber
_RectSysBatteryCurrent_Object = MibScalar
rectSysBatteryCurrent = _RectSysBatteryCurrent_Object(
    (1, 3, 6, 1, 4, 1, 7309, 5, 3, 1, 13),
    _RectSysBatteryCurrent_Type()
)
rectSysBatteryCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rectSysBatteryCurrent.setStatus("current")
_RectSysBatteryTemperature_Type = ScaledNumber
_RectSysBatteryTemperature_Object = MibScalar
rectSysBatteryTemperature = _RectSysBatteryTemperature_Object(
    (1, 3, 6, 1, 4, 1, 7309, 5, 3, 1, 14),
    _RectSysBatteryTemperature_Type()
)
rectSysBatteryTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rectSysBatteryTemperature.setStatus("current")
_RectSysSystemNumber_Type = ScaledNumber
_RectSysSystemNumber_Object = MibScalar
rectSysSystemNumber = _RectSysSystemNumber_Object(
    (1, 3, 6, 1, 4, 1, 7309, 5, 3, 1, 15),
    _RectSysSystemNumber_Type()
)
rectSysSystemNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rectSysSystemNumber.setStatus("current")
_RectSysEstimatedRequiredCapacityInWatts_Type = ScaledNumber
_RectSysEstimatedRequiredCapacityInWatts_Object = MibScalar
rectSysEstimatedRequiredCapacityInWatts = _RectSysEstimatedRequiredCapacityInWatts_Object(
    (1, 3, 6, 1, 4, 1, 7309, 5, 3, 1, 16),
    _RectSysEstimatedRequiredCapacityInWatts_Type()
)
rectSysEstimatedRequiredCapacityInWatts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rectSysEstimatedRequiredCapacityInWatts.setStatus("current")
_RectSysEstimatedRequiredCapacityInAmps_Type = ScaledNumber
_RectSysEstimatedRequiredCapacityInAmps_Object = MibScalar
rectSysEstimatedRequiredCapacityInAmps = _RectSysEstimatedRequiredCapacityInAmps_Object(
    (1, 3, 6, 1, 4, 1, 7309, 5, 3, 1, 17),
    _RectSysEstimatedRequiredCapacityInAmps_Type()
)
rectSysEstimatedRequiredCapacityInAmps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rectSysEstimatedRequiredCapacityInAmps.setStatus("current")
_RectSysEstimatedAvailableCapacityInWatts_Type = ScaledNumber
_RectSysEstimatedAvailableCapacityInWatts_Object = MibScalar
rectSysEstimatedAvailableCapacityInWatts = _RectSysEstimatedAvailableCapacityInWatts_Object(
    (1, 3, 6, 1, 4, 1, 7309, 5, 3, 1, 18),
    _RectSysEstimatedAvailableCapacityInWatts_Type()
)
rectSysEstimatedAvailableCapacityInWatts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rectSysEstimatedAvailableCapacityInWatts.setStatus("current")
_RectSysEstimatedAvailableCapacityInAmps_Type = ScaledNumber
_RectSysEstimatedAvailableCapacityInAmps_Object = MibScalar
rectSysEstimatedAvailableCapacityInAmps = _RectSysEstimatedAvailableCapacityInAmps_Object(
    (1, 3, 6, 1, 4, 1, 7309, 5, 3, 1, 19),
    _RectSysEstimatedAvailableCapacityInAmps_Type()
)
rectSysEstimatedAvailableCapacityInAmps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rectSysEstimatedAvailableCapacityInAmps.setStatus("current")
_RectSysEstimatedRedundantCapacityInWatts_Type = ScaledNumber
_RectSysEstimatedRedundantCapacityInWatts_Object = MibScalar
rectSysEstimatedRedundantCapacityInWatts = _RectSysEstimatedRedundantCapacityInWatts_Object(
    (1, 3, 6, 1, 4, 1, 7309, 5, 3, 1, 20),
    _RectSysEstimatedRedundantCapacityInWatts_Type()
)
rectSysEstimatedRedundantCapacityInWatts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rectSysEstimatedRedundantCapacityInWatts.setStatus("current")
_RectSysEstimatedRedundantCapacityInAmps_Type = ScaledNumber
_RectSysEstimatedRedundantCapacityInAmps_Object = MibScalar
rectSysEstimatedRedundantCapacityInAmps = _RectSysEstimatedRedundantCapacityInAmps_Object(
    (1, 3, 6, 1, 4, 1, 7309, 5, 3, 1, 21),
    _RectSysEstimatedRedundantCapacityInAmps_Type()
)
rectSysEstimatedRedundantCapacityInAmps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rectSysEstimatedRedundantCapacityInAmps.setStatus("current")
_RectSysEstimatedStandbyCapacityInWatts_Type = ScaledNumber
_RectSysEstimatedStandbyCapacityInWatts_Object = MibScalar
rectSysEstimatedStandbyCapacityInWatts = _RectSysEstimatedStandbyCapacityInWatts_Object(
    (1, 3, 6, 1, 4, 1, 7309, 5, 3, 1, 22),
    _RectSysEstimatedStandbyCapacityInWatts_Type()
)
rectSysEstimatedStandbyCapacityInWatts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rectSysEstimatedStandbyCapacityInWatts.setStatus("current")
_RectSysEstimatedStandbyCapacityInAmps_Type = ScaledNumber
_RectSysEstimatedStandbyCapacityInAmps_Object = MibScalar
rectSysEstimatedStandbyCapacityInAmps = _RectSysEstimatedStandbyCapacityInAmps_Object(
    (1, 3, 6, 1, 4, 1, 7309, 5, 3, 1, 23),
    _RectSysEstimatedStandbyCapacityInAmps_Type()
)
rectSysEstimatedStandbyCapacityInAmps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rectSysEstimatedStandbyCapacityInAmps.setStatus("current")
_RectSysPowerAveragePower_Type = ScaledNumber
_RectSysPowerAveragePower_Object = MibScalar
rectSysPowerAveragePower = _RectSysPowerAveragePower_Object(
    (1, 3, 6, 1, 4, 1, 7309, 5, 3, 1, 24),
    _RectSysPowerAveragePower_Type()
)
rectSysPowerAveragePower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rectSysPowerAveragePower.setStatus("current")
_RectSysModulesSupplyingPower_Type = ScaledNumber
_RectSysModulesSupplyingPower_Object = MibScalar
rectSysModulesSupplyingPower = _RectSysModulesSupplyingPower_Object(
    (1, 3, 6, 1, 4, 1, 7309, 5, 3, 1, 25),
    _RectSysModulesSupplyingPower_Type()
)
rectSysModulesSupplyingPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rectSysModulesSupplyingPower.setStatus("current")
_RectSysModulesInStandby_Type = ScaledNumber
_RectSysModulesInStandby_Object = MibScalar
rectSysModulesInStandby = _RectSysModulesInStandby_Object(
    (1, 3, 6, 1, 4, 1, 7309, 5, 3, 1, 26),
    _RectSysModulesInStandby_Type()
)
rectSysModulesInStandby.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rectSysModulesInStandby.setStatus("current")
_RectSysEstimatedCapacityRemainingCurrent_Type = ScaledNumber
_RectSysEstimatedCapacityRemainingCurrent_Object = MibScalar
rectSysEstimatedCapacityRemainingCurrent = _RectSysEstimatedCapacityRemainingCurrent_Object(
    (1, 3, 6, 1, 4, 1, 7309, 5, 3, 1, 28),
    _RectSysEstimatedCapacityRemainingCurrent_Type()
)
rectSysEstimatedCapacityRemainingCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rectSysEstimatedCapacityRemainingCurrent.setStatus("current")
_RectSysEstimatedCapacityRemainingPower_Type = ScaledNumber
_RectSysEstimatedCapacityRemainingPower_Object = MibScalar
rectSysEstimatedCapacityRemainingPower = _RectSysEstimatedCapacityRemainingPower_Object(
    (1, 3, 6, 1, 4, 1, 7309, 5, 3, 1, 29),
    _RectSysEstimatedCapacityRemainingPower_Type()
)
rectSysEstimatedCapacityRemainingPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rectSysEstimatedCapacityRemainingPower.setStatus("current")
_RectSysEstimatedSOCPercent_Type = ScaledNumber
_RectSysEstimatedSOCPercent_Object = MibScalar
rectSysEstimatedSOCPercent = _RectSysEstimatedSOCPercent_Object(
    (1, 3, 6, 1, 4, 1, 7309, 5, 3, 1, 30),
    _RectSysEstimatedSOCPercent_Type()
)
rectSysEstimatedSOCPercent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rectSysEstimatedSOCPercent.setStatus("current")
_RectSysEstimatedBatteryRuntime_Type = ScaledNumber
_RectSysEstimatedBatteryRuntime_Object = MibScalar
rectSysEstimatedBatteryRuntime = _RectSysEstimatedBatteryRuntime_Object(
    (1, 3, 6, 1, 4, 1, 7309, 5, 3, 1, 31),
    _RectSysEstimatedBatteryRuntime_Type()
)
rectSysEstimatedBatteryRuntime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rectSysEstimatedBatteryRuntime.setStatus("current")
_RectSysEstimatedBatteryHealthPercent_Type = ScaledNumber
_RectSysEstimatedBatteryHealthPercent_Object = MibScalar
rectSysEstimatedBatteryHealthPercent = _RectSysEstimatedBatteryHealthPercent_Object(
    (1, 3, 6, 1, 4, 1, 7309, 5, 3, 1, 32),
    _RectSysEstimatedBatteryHealthPercent_Type()
)
rectSysEstimatedBatteryHealthPercent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rectSysEstimatedBatteryHealthPercent.setStatus("current")
_RectNumberOfAcquiredRectifiers_Type = ScaledNumber
_RectNumberOfAcquiredRectifiers_Object = MibScalar
rectNumberOfAcquiredRectifiers = _RectNumberOfAcquiredRectifiers_Object(
    (1, 3, 6, 1, 4, 1, 7309, 5, 3, 1, 33),
    _RectNumberOfAcquiredRectifiers_Type()
)
rectNumberOfAcquiredRectifiers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rectNumberOfAcquiredRectifiers.setStatus("current")
_RectNumberOfSourcingRectifiers_Type = ScaledNumber
_RectNumberOfSourcingRectifiers_Object = MibScalar
rectNumberOfSourcingRectifiers = _RectNumberOfSourcingRectifiers_Object(
    (1, 3, 6, 1, 4, 1, 7309, 5, 3, 1, 34),
    _RectNumberOfSourcingRectifiers_Type()
)
rectNumberOfSourcingRectifiers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rectNumberOfSourcingRectifiers.setStatus("current")
_RectNumberOfFailedRectifiers_Type = ScaledNumber
_RectNumberOfFailedRectifiers_Object = MibScalar
rectNumberOfFailedRectifiers = _RectNumberOfFailedRectifiers_Object(
    (1, 3, 6, 1, 4, 1, 7309, 5, 3, 1, 35),
    _RectNumberOfFailedRectifiers_Type()
)
rectNumberOfFailedRectifiers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rectNumberOfFailedRectifiers.setStatus("current")
_RectNumberOfMinorAlertRectifiers_Type = ScaledNumber
_RectNumberOfMinorAlertRectifiers_Object = MibScalar
rectNumberOfMinorAlertRectifiers = _RectNumberOfMinorAlertRectifiers_Object(
    (1, 3, 6, 1, 4, 1, 7309, 5, 3, 1, 36),
    _RectNumberOfMinorAlertRectifiers_Type()
)
rectNumberOfMinorAlertRectifiers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rectNumberOfMinorAlertRectifiers.setStatus("current")
_RectNumberOfCommsLostRectifiers_Type = ScaledNumber
_RectNumberOfCommsLostRectifiers_Object = MibScalar
rectNumberOfCommsLostRectifiers = _RectNumberOfCommsLostRectifiers_Object(
    (1, 3, 6, 1, 4, 1, 7309, 5, 3, 1, 37),
    _RectNumberOfCommsLostRectifiers_Type()
)
rectNumberOfCommsLostRectifiers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rectNumberOfCommsLostRectifiers.setStatus("current")
_RectNumberOfCommsNormalRectifiers_Type = ScaledNumber
_RectNumberOfCommsNormalRectifiers_Object = MibScalar
rectNumberOfCommsNormalRectifiers = _RectNumberOfCommsNormalRectifiers_Object(
    (1, 3, 6, 1, 4, 1, 7309, 5, 3, 1, 38),
    _RectNumberOfCommsNormalRectifiers_Type()
)
rectNumberOfCommsNormalRectifiers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rectNumberOfCommsNormalRectifiers.setStatus("current")
_RectNumberOfACFailedRectifiers_Type = ScaledNumber
_RectNumberOfACFailedRectifiers_Object = MibScalar
rectNumberOfACFailedRectifiers = _RectNumberOfACFailedRectifiers_Object(
    (1, 3, 6, 1, 4, 1, 7309, 5, 3, 1, 39),
    _RectNumberOfACFailedRectifiers_Type()
)
rectNumberOfACFailedRectifiers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rectNumberOfACFailedRectifiers.setStatus("current")
_RectNumberOfRectifiersWithConfigError_Type = ScaledNumber
_RectNumberOfRectifiersWithConfigError_Object = MibScalar
rectNumberOfRectifiersWithConfigError = _RectNumberOfRectifiersWithConfigError_Object(
    (1, 3, 6, 1, 4, 1, 7309, 5, 3, 1, 40),
    _RectNumberOfRectifiersWithConfigError_Type()
)
rectNumberOfRectifiersWithConfigError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rectNumberOfRectifiersWithConfigError.setStatus("current")
_RectNumberOfRectifiersInPowerLimit_Type = ScaledNumber
_RectNumberOfRectifiersInPowerLimit_Object = MibScalar
rectNumberOfRectifiersInPowerLimit = _RectNumberOfRectifiersInPowerLimit_Object(
    (1, 3, 6, 1, 4, 1, 7309, 5, 3, 1, 41),
    _RectNumberOfRectifiersInPowerLimit_Type()
)
rectNumberOfRectifiersInPowerLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rectNumberOfRectifiersInPowerLimit.setStatus("current")
_RectNumberOfRectifiersInCurrentLimit_Type = ScaledNumber
_RectNumberOfRectifiersInCurrentLimit_Object = MibScalar
rectNumberOfRectifiersInCurrentLimit = _RectNumberOfRectifiersInCurrentLimit_Object(
    (1, 3, 6, 1, 4, 1, 7309, 5, 3, 1, 42),
    _RectNumberOfRectifiersInCurrentLimit_Type()
)
rectNumberOfRectifiersInCurrentLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rectNumberOfRectifiersInCurrentLimit.setStatus("current")
_RectNumberOfFanFailRectifiers_Type = ScaledNumber
_RectNumberOfFanFailRectifiers_Object = MibScalar
rectNumberOfFanFailRectifiers = _RectNumberOfFanFailRectifiers_Object(
    (1, 3, 6, 1, 4, 1, 7309, 5, 3, 1, 43),
    _RectNumberOfFanFailRectifiers_Type()
)
rectNumberOfFanFailRectifiers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rectNumberOfFanFailRectifiers.setStatus("current")
_RectNumberOfRectifiersInBootloader_Type = ScaledNumber
_RectNumberOfRectifiersInBootloader_Object = MibScalar
rectNumberOfRectifiersInBootloader = _RectNumberOfRectifiersInBootloader_Object(
    (1, 3, 6, 1, 4, 1, 7309, 5, 3, 1, 44),
    _RectNumberOfRectifiersInBootloader_Type()
)
rectNumberOfRectifiersInBootloader.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rectNumberOfRectifiersInBootloader.setStatus("current")
_RectMaxRectifierAmbientTemperature_Type = ScaledNumber
_RectMaxRectifierAmbientTemperature_Object = MibScalar
rectMaxRectifierAmbientTemperature = _RectMaxRectifierAmbientTemperature_Object(
    (1, 3, 6, 1, 4, 1, 7309, 5, 3, 1, 45),
    _RectMaxRectifierAmbientTemperature_Type()
)
rectMaxRectifierAmbientTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rectMaxRectifierAmbientTemperature.setStatus("current")
_Conformance_ObjectIdentity = ObjectIdentity
conformance = _Conformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7309, 5, 3, 1, 100)
)
_Compliances_ObjectIdentity = ObjectIdentity
compliances = _Compliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7309, 5, 3, 1, 100, 1)
)
_RectifierGroups_ObjectIdentity = ObjectIdentity
rectifierGroups = _RectifierGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7309, 5, 3, 1, 100, 2)
)

# Managed Objects groups

rectifierGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7309, 5, 3, 1, 100, 2, 1)
)
rectifierGroup.setObjects(
      *(("ALPHA-RECTIFIER-SYS-MIB", "rectSysTotalOutputCurrent"),
        ("ALPHA-RECTIFIER-SYS-MIB", "rectSysTotalOutputPower"),
        ("ALPHA-RECTIFIER-SYS-MIB", "rectSysTotalCapacityInstalledAmps"),
        ("ALPHA-RECTIFIER-SYS-MIB", "rectSysTotalCapacityInstalledPower"),
        ("ALPHA-RECTIFIER-SYS-MIB", "rectSysAverageRectifierOutputVoltage"),
        ("ALPHA-RECTIFIER-SYS-MIB", "rectSysAverageRectifierACInputVoltage"),
        ("ALPHA-RECTIFIER-SYS-MIB", "rectSysAveragePhase1Voltage"),
        ("ALPHA-RECTIFIER-SYS-MIB", "rectSysAveragePhase2Voltage"),
        ("ALPHA-RECTIFIER-SYS-MIB", "rectSysAveragePhase3Voltage"),
        ("ALPHA-RECTIFIER-SYS-MIB", "rectSysSystemVoltage"),
        ("ALPHA-RECTIFIER-SYS-MIB", "rectSysTotalLoadCurrent"),
        ("ALPHA-RECTIFIER-SYS-MIB", "rectSysBatteryVoltage"),
        ("ALPHA-RECTIFIER-SYS-MIB", "rectSysBatteryCurrent"),
        ("ALPHA-RECTIFIER-SYS-MIB", "rectSysBatteryTemperature"),
        ("ALPHA-RECTIFIER-SYS-MIB", "rectSysSystemNumber"),
        ("ALPHA-RECTIFIER-SYS-MIB", "rectSysEstimatedRequiredCapacityInWatts"),
        ("ALPHA-RECTIFIER-SYS-MIB", "rectSysEstimatedRequiredCapacityInAmps"),
        ("ALPHA-RECTIFIER-SYS-MIB", "rectSysEstimatedAvailableCapacityInWatts"),
        ("ALPHA-RECTIFIER-SYS-MIB", "rectSysEstimatedAvailableCapacityInAmps"),
        ("ALPHA-RECTIFIER-SYS-MIB", "rectSysEstimatedRedundantCapacityInWatts"),
        ("ALPHA-RECTIFIER-SYS-MIB", "rectSysEstimatedRedundantCapacityInAmps"),
        ("ALPHA-RECTIFIER-SYS-MIB", "rectSysEstimatedStandbyCapacityInWatts"),
        ("ALPHA-RECTIFIER-SYS-MIB", "rectSysEstimatedStandbyCapacityInAmps"),
        ("ALPHA-RECTIFIER-SYS-MIB", "rectSysPowerAveragePower"),
        ("ALPHA-RECTIFIER-SYS-MIB", "rectSysModulesSupplyingPower"),
        ("ALPHA-RECTIFIER-SYS-MIB", "rectSysModulesInStandby"),
        ("ALPHA-RECTIFIER-SYS-MIB", "rectSysEstimatedCapacityRemainingCurrent"),
        ("ALPHA-RECTIFIER-SYS-MIB", "rectSysEstimatedCapacityRemainingPower"),
        ("ALPHA-RECTIFIER-SYS-MIB", "rectSysEstimatedSOCPercent"),
        ("ALPHA-RECTIFIER-SYS-MIB", "rectSysEstimatedBatteryRuntime"),
        ("ALPHA-RECTIFIER-SYS-MIB", "rectSysEstimatedBatteryHealthPercent"),
        ("ALPHA-RECTIFIER-SYS-MIB", "rectNumberOfAcquiredRectifiers"),
        ("ALPHA-RECTIFIER-SYS-MIB", "rectNumberOfSourcingRectifiers"),
        ("ALPHA-RECTIFIER-SYS-MIB", "rectNumberOfFailedRectifiers"),
        ("ALPHA-RECTIFIER-SYS-MIB", "rectNumberOfMinorAlertRectifiers"),
        ("ALPHA-RECTIFIER-SYS-MIB", "rectNumberOfCommsLostRectifiers"),
        ("ALPHA-RECTIFIER-SYS-MIB", "rectNumberOfCommsNormalRectifiers"),
        ("ALPHA-RECTIFIER-SYS-MIB", "rectNumberOfACFailedRectifiers"),
        ("ALPHA-RECTIFIER-SYS-MIB", "rectNumberOfRectifiersWithConfigError"),
        ("ALPHA-RECTIFIER-SYS-MIB", "rectNumberOfRectifiersInPowerLimit"),
        ("ALPHA-RECTIFIER-SYS-MIB", "rectNumberOfRectifiersInCurrentLimit"),
        ("ALPHA-RECTIFIER-SYS-MIB", "rectNumberOfFanFailRectifiers"),
        ("ALPHA-RECTIFIER-SYS-MIB", "rectNumberOfRectifiersInBootloader"),
        ("ALPHA-RECTIFIER-SYS-MIB", "rectMaxRectifierAmbientTemperature"))
)
if mibBuilder.loadTexts:
    rectifierGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 7309, 5, 3, 1, 100, 1, 1)
)
compliance.setObjects(
    ("ALPHA-RECTIFIER-SYS-MIB", "rectifierGroup")
)
if mibBuilder.loadTexts:
    compliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ALPHA-RECTIFIER-SYS-MIB",
    **{"rectifierSystem": rectifierSystem,
       "rectSysTotalOutputCurrent": rectSysTotalOutputCurrent,
       "rectSysTotalOutputPower": rectSysTotalOutputPower,
       "rectSysTotalCapacityInstalledAmps": rectSysTotalCapacityInstalledAmps,
       "rectSysTotalCapacityInstalledPower": rectSysTotalCapacityInstalledPower,
       "rectSysAverageRectifierOutputVoltage": rectSysAverageRectifierOutputVoltage,
       "rectSysAverageRectifierACInputVoltage": rectSysAverageRectifierACInputVoltage,
       "rectSysAveragePhase1Voltage": rectSysAveragePhase1Voltage,
       "rectSysAveragePhase2Voltage": rectSysAveragePhase2Voltage,
       "rectSysAveragePhase3Voltage": rectSysAveragePhase3Voltage,
       "rectSysSystemVoltage": rectSysSystemVoltage,
       "rectSysTotalLoadCurrent": rectSysTotalLoadCurrent,
       "rectSysBatteryVoltage": rectSysBatteryVoltage,
       "rectSysBatteryCurrent": rectSysBatteryCurrent,
       "rectSysBatteryTemperature": rectSysBatteryTemperature,
       "rectSysSystemNumber": rectSysSystemNumber,
       "rectSysEstimatedRequiredCapacityInWatts": rectSysEstimatedRequiredCapacityInWatts,
       "rectSysEstimatedRequiredCapacityInAmps": rectSysEstimatedRequiredCapacityInAmps,
       "rectSysEstimatedAvailableCapacityInWatts": rectSysEstimatedAvailableCapacityInWatts,
       "rectSysEstimatedAvailableCapacityInAmps": rectSysEstimatedAvailableCapacityInAmps,
       "rectSysEstimatedRedundantCapacityInWatts": rectSysEstimatedRedundantCapacityInWatts,
       "rectSysEstimatedRedundantCapacityInAmps": rectSysEstimatedRedundantCapacityInAmps,
       "rectSysEstimatedStandbyCapacityInWatts": rectSysEstimatedStandbyCapacityInWatts,
       "rectSysEstimatedStandbyCapacityInAmps": rectSysEstimatedStandbyCapacityInAmps,
       "rectSysPowerAveragePower": rectSysPowerAveragePower,
       "rectSysModulesSupplyingPower": rectSysModulesSupplyingPower,
       "rectSysModulesInStandby": rectSysModulesInStandby,
       "rectSysEstimatedCapacityRemainingCurrent": rectSysEstimatedCapacityRemainingCurrent,
       "rectSysEstimatedCapacityRemainingPower": rectSysEstimatedCapacityRemainingPower,
       "rectSysEstimatedSOCPercent": rectSysEstimatedSOCPercent,
       "rectSysEstimatedBatteryRuntime": rectSysEstimatedBatteryRuntime,
       "rectSysEstimatedBatteryHealthPercent": rectSysEstimatedBatteryHealthPercent,
       "rectNumberOfAcquiredRectifiers": rectNumberOfAcquiredRectifiers,
       "rectNumberOfSourcingRectifiers": rectNumberOfSourcingRectifiers,
       "rectNumberOfFailedRectifiers": rectNumberOfFailedRectifiers,
       "rectNumberOfMinorAlertRectifiers": rectNumberOfMinorAlertRectifiers,
       "rectNumberOfCommsLostRectifiers": rectNumberOfCommsLostRectifiers,
       "rectNumberOfCommsNormalRectifiers": rectNumberOfCommsNormalRectifiers,
       "rectNumberOfACFailedRectifiers": rectNumberOfACFailedRectifiers,
       "rectNumberOfRectifiersWithConfigError": rectNumberOfRectifiersWithConfigError,
       "rectNumberOfRectifiersInPowerLimit": rectNumberOfRectifiersInPowerLimit,
       "rectNumberOfRectifiersInCurrentLimit": rectNumberOfRectifiersInCurrentLimit,
       "rectNumberOfFanFailRectifiers": rectNumberOfFanFailRectifiers,
       "rectNumberOfRectifiersInBootloader": rectNumberOfRectifiersInBootloader,
       "rectMaxRectifierAmbientTemperature": rectMaxRectifierAmbientTemperature,
       "conformance": conformance,
       "compliances": compliances,
       "compliance": compliance,
       "rectifierGroups": rectifierGroups,
       "rectifierGroup": rectifierGroup}
)
