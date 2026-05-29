# SNMP MIB module (PRVT-LMM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\telco-systems\binox\PRVT-LMM-MIB

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

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

prvtLmmMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 172)
)
if mibBuilder.loadTexts:
    prvtLmmMIB.setRevisions(
        ("2011-10-11 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_PrvtLmmNotifications_ObjectIdentity = ObjectIdentity
prvtLmmNotifications = _PrvtLmmNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 172, 0)
)
_PrvtLmmObjects_ObjectIdentity = ObjectIdentity
prvtLmmObjects = _PrvtLmmObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 172, 1)
)
_PrvtLmmShutdown_Type = TruthValue
_PrvtLmmShutdown_Object = MibScalar
prvtLmmShutdown = _PrvtLmmShutdown_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 172, 1, 1),
    _PrvtLmmShutdown_Type()
)
prvtLmmShutdown.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prvtLmmShutdown.setStatus("current")
_PrvtLmmDebug_Type = TruthValue
_PrvtLmmDebug_Object = MibScalar
prvtLmmDebug = _PrvtLmmDebug_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 172, 1, 2),
    _PrvtLmmDebug_Type()
)
prvtLmmDebug.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prvtLmmDebug.setStatus("current")
_PrvtLmmPeriod_Type = Integer32
_PrvtLmmPeriod_Object = MibScalar
prvtLmmPeriod = _PrvtLmmPeriod_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 172, 1, 3),
    _PrvtLmmPeriod_Type()
)
prvtLmmPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prvtLmmPeriod.setStatus("current")
_PrvtLmmTrap_Type = TruthValue
_PrvtLmmTrap_Object = MibScalar
prvtLmmTrap = _PrvtLmmTrap_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 172, 1, 4),
    _PrvtLmmTrap_Type()
)
prvtLmmTrap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prvtLmmTrap.setStatus("current")
_PrvtLmmLog_Type = TruthValue
_PrvtLmmLog_Object = MibScalar
prvtLmmLog = _PrvtLmmLog_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 172, 1, 5),
    _PrvtLmmLog_Type()
)
prvtLmmLog.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prvtLmmLog.setStatus("current")
_PrvtLmmLed_Type = TruthValue
_PrvtLmmLed_Object = MibScalar
prvtLmmLed = _PrvtLmmLed_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 172, 1, 6),
    _PrvtLmmLed_Type()
)
prvtLmmLed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prvtLmmLed.setStatus("current")


class _PrvtLmmTemperatureHighThreshold_Type(Integer32):
    """Custom type prvtLmmTemperatureHighThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-128, 128),
    )


_PrvtLmmTemperatureHighThreshold_Type.__name__ = "Integer32"
_PrvtLmmTemperatureHighThreshold_Object = MibScalar
prvtLmmTemperatureHighThreshold = _PrvtLmmTemperatureHighThreshold_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 172, 1, 7),
    _PrvtLmmTemperatureHighThreshold_Type()
)
prvtLmmTemperatureHighThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prvtLmmTemperatureHighThreshold.setStatus("current")


class _PrvtLmmTemperatureLowThreshold_Type(Integer32):
    """Custom type prvtLmmTemperatureLowThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-128, 128),
    )


_PrvtLmmTemperatureLowThreshold_Type.__name__ = "Integer32"
_PrvtLmmTemperatureLowThreshold_Object = MibScalar
prvtLmmTemperatureLowThreshold = _PrvtLmmTemperatureLowThreshold_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 172, 1, 8),
    _PrvtLmmTemperatureLowThreshold_Type()
)
prvtLmmTemperatureLowThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prvtLmmTemperatureLowThreshold.setStatus("current")


class _PrvtLmmRxPowerLowThreshold_Type(Integer32):
    """Custom type prvtLmmRxPowerLowThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-40, 8),
    )


_PrvtLmmRxPowerLowThreshold_Type.__name__ = "Integer32"
_PrvtLmmRxPowerLowThreshold_Object = MibScalar
prvtLmmRxPowerLowThreshold = _PrvtLmmRxPowerLowThreshold_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 172, 1, 9),
    _PrvtLmmRxPowerLowThreshold_Type()
)
prvtLmmRxPowerLowThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prvtLmmRxPowerLowThreshold.setStatus("current")


class _PrvtLmmRxPowerHighThreshold_Type(Integer32):
    """Custom type prvtLmmRxPowerHighThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-40, 8),
    )


_PrvtLmmRxPowerHighThreshold_Type.__name__ = "Integer32"
_PrvtLmmRxPowerHighThreshold_Object = MibScalar
prvtLmmRxPowerHighThreshold = _PrvtLmmRxPowerHighThreshold_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 172, 1, 10),
    _PrvtLmmRxPowerHighThreshold_Type()
)
prvtLmmRxPowerHighThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prvtLmmRxPowerHighThreshold.setStatus("current")


class _PrvtLmmTxPowerLowThreshold_Type(Integer32):
    """Custom type prvtLmmTxPowerLowThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-40, 8),
    )


_PrvtLmmTxPowerLowThreshold_Type.__name__ = "Integer32"
_PrvtLmmTxPowerLowThreshold_Object = MibScalar
prvtLmmTxPowerLowThreshold = _PrvtLmmTxPowerLowThreshold_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 172, 1, 11),
    _PrvtLmmTxPowerLowThreshold_Type()
)
prvtLmmTxPowerLowThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prvtLmmTxPowerLowThreshold.setStatus("current")


class _PrvtLmmTxPowerHighThreshold_Type(Integer32):
    """Custom type prvtLmmTxPowerHighThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-40, 8),
    )


_PrvtLmmTxPowerHighThreshold_Type.__name__ = "Integer32"
_PrvtLmmTxPowerHighThreshold_Object = MibScalar
prvtLmmTxPowerHighThreshold = _PrvtLmmTxPowerHighThreshold_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 172, 1, 12),
    _PrvtLmmTxPowerHighThreshold_Type()
)
prvtLmmTxPowerHighThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prvtLmmTxPowerHighThreshold.setStatus("current")
_PrvtLmmInterfaceTable_Object = MibTable
prvtLmmInterfaceTable = _PrvtLmmInterfaceTable_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 172, 1, 13)
)
if mibBuilder.loadTexts:
    prvtLmmInterfaceTable.setStatus("current")
_PrvtLmmInterfaceEntry_Object = MibTableRow
prvtLmmInterfaceEntry = _PrvtLmmInterfaceEntry_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 172, 1, 13, 1)
)
prvtLmmInterfaceEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    prvtLmmInterfaceEntry.setStatus("current")
_PrvtLmmInterfaceShutdown_Type = TruthValue
_PrvtLmmInterfaceShutdown_Object = MibTableColumn
prvtLmmInterfaceShutdown = _PrvtLmmInterfaceShutdown_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 172, 1, 13, 1, 1),
    _PrvtLmmInterfaceShutdown_Type()
)
prvtLmmInterfaceShutdown.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prvtLmmInterfaceShutdown.setStatus("current")


class _PrvtLmmInterfaceTempLowThreshold_Type(Integer32):
    """Custom type prvtLmmInterfaceTempLowThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-128, 128),
    )


_PrvtLmmInterfaceTempLowThreshold_Type.__name__ = "Integer32"
_PrvtLmmInterfaceTempLowThreshold_Object = MibTableColumn
prvtLmmInterfaceTempLowThreshold = _PrvtLmmInterfaceTempLowThreshold_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 172, 1, 13, 1, 2),
    _PrvtLmmInterfaceTempLowThreshold_Type()
)
prvtLmmInterfaceTempLowThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prvtLmmInterfaceTempLowThreshold.setStatus("current")


class _PrvtLmmInterfaceTempHighThreshold_Type(Integer32):
    """Custom type prvtLmmInterfaceTempHighThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-128, 128),
    )


_PrvtLmmInterfaceTempHighThreshold_Type.__name__ = "Integer32"
_PrvtLmmInterfaceTempHighThreshold_Object = MibTableColumn
prvtLmmInterfaceTempHighThreshold = _PrvtLmmInterfaceTempHighThreshold_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 172, 1, 13, 1, 3),
    _PrvtLmmInterfaceTempHighThreshold_Type()
)
prvtLmmInterfaceTempHighThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prvtLmmInterfaceTempHighThreshold.setStatus("current")
_PrvtLmmInterfaceTempValue_Type = Integer32
_PrvtLmmInterfaceTempValue_Object = MibTableColumn
prvtLmmInterfaceTempValue = _PrvtLmmInterfaceTempValue_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 172, 1, 13, 1, 4),
    _PrvtLmmInterfaceTempValue_Type()
)
prvtLmmInterfaceTempValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtLmmInterfaceTempValue.setStatus("current")
_PrvtLmmInterfaceTempThresholdLo_Type = Integer32
_PrvtLmmInterfaceTempThresholdLo_Object = MibTableColumn
prvtLmmInterfaceTempThresholdLo = _PrvtLmmInterfaceTempThresholdLo_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 172, 1, 13, 1, 5),
    _PrvtLmmInterfaceTempThresholdLo_Type()
)
prvtLmmInterfaceTempThresholdLo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtLmmInterfaceTempThresholdLo.setStatus("current")
_PrvtLmmInterfaceTempThresholdHi_Type = Integer32
_PrvtLmmInterfaceTempThresholdHi_Object = MibTableColumn
prvtLmmInterfaceTempThresholdHi = _PrvtLmmInterfaceTempThresholdHi_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 172, 1, 13, 1, 6),
    _PrvtLmmInterfaceTempThresholdHi_Type()
)
prvtLmmInterfaceTempThresholdHi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtLmmInterfaceTempThresholdHi.setStatus("current")
_PrvtLmmInterfaceTempTestState_Type = TruthValue
_PrvtLmmInterfaceTempTestState_Object = MibTableColumn
prvtLmmInterfaceTempTestState = _PrvtLmmInterfaceTempTestState_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 172, 1, 13, 1, 7),
    _PrvtLmmInterfaceTempTestState_Type()
)
prvtLmmInterfaceTempTestState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtLmmInterfaceTempTestState.setStatus("current")


class _PrvtLmmInterfaceRxPowerLowThreshold_Type(Integer32):
    """Custom type prvtLmmInterfaceRxPowerLowThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-40, 8),
    )


_PrvtLmmInterfaceRxPowerLowThreshold_Type.__name__ = "Integer32"
_PrvtLmmInterfaceRxPowerLowThreshold_Object = MibTableColumn
prvtLmmInterfaceRxPowerLowThreshold = _PrvtLmmInterfaceRxPowerLowThreshold_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 172, 1, 13, 1, 8),
    _PrvtLmmInterfaceRxPowerLowThreshold_Type()
)
prvtLmmInterfaceRxPowerLowThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prvtLmmInterfaceRxPowerLowThreshold.setStatus("current")


class _PrvtLmmInterfaceRxPowerHighThreshold_Type(Integer32):
    """Custom type prvtLmmInterfaceRxPowerHighThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-40, 8),
    )


_PrvtLmmInterfaceRxPowerHighThreshold_Type.__name__ = "Integer32"
_PrvtLmmInterfaceRxPowerHighThreshold_Object = MibTableColumn
prvtLmmInterfaceRxPowerHighThreshold = _PrvtLmmInterfaceRxPowerHighThreshold_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 172, 1, 13, 1, 9),
    _PrvtLmmInterfaceRxPowerHighThreshold_Type()
)
prvtLmmInterfaceRxPowerHighThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prvtLmmInterfaceRxPowerHighThreshold.setStatus("current")
_PrvtLmmInterfaceRxPowerValue_Type = Integer32
_PrvtLmmInterfaceRxPowerValue_Object = MibTableColumn
prvtLmmInterfaceRxPowerValue = _PrvtLmmInterfaceRxPowerValue_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 172, 1, 13, 1, 10),
    _PrvtLmmInterfaceRxPowerValue_Type()
)
prvtLmmInterfaceRxPowerValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtLmmInterfaceRxPowerValue.setStatus("current")
_PrvtLmmInterfaceRxPowerThresholdRxLo_Type = Integer32
_PrvtLmmInterfaceRxPowerThresholdRxLo_Object = MibTableColumn
prvtLmmInterfaceRxPowerThresholdRxLo = _PrvtLmmInterfaceRxPowerThresholdRxLo_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 172, 1, 13, 1, 11),
    _PrvtLmmInterfaceRxPowerThresholdRxLo_Type()
)
prvtLmmInterfaceRxPowerThresholdRxLo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtLmmInterfaceRxPowerThresholdRxLo.setStatus("current")
_PrvtLmmInterfaceRxPowerThresholdRxHi_Type = Integer32
_PrvtLmmInterfaceRxPowerThresholdRxHi_Object = MibTableColumn
prvtLmmInterfaceRxPowerThresholdRxHi = _PrvtLmmInterfaceRxPowerThresholdRxHi_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 172, 1, 13, 1, 12),
    _PrvtLmmInterfaceRxPowerThresholdRxHi_Type()
)
prvtLmmInterfaceRxPowerThresholdRxHi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtLmmInterfaceRxPowerThresholdRxHi.setStatus("current")
_PrvtLmmInterfaceRxPowerTestState_Type = TruthValue
_PrvtLmmInterfaceRxPowerTestState_Object = MibTableColumn
prvtLmmInterfaceRxPowerTestState = _PrvtLmmInterfaceRxPowerTestState_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 172, 1, 13, 1, 13),
    _PrvtLmmInterfaceRxPowerTestState_Type()
)
prvtLmmInterfaceRxPowerTestState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtLmmInterfaceRxPowerTestState.setStatus("current")


class _PrvtLmmInterfaceTxPowerLowThreshold_Type(Integer32):
    """Custom type prvtLmmInterfaceTxPowerLowThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-40, 8),
    )


_PrvtLmmInterfaceTxPowerLowThreshold_Type.__name__ = "Integer32"
_PrvtLmmInterfaceTxPowerLowThreshold_Object = MibTableColumn
prvtLmmInterfaceTxPowerLowThreshold = _PrvtLmmInterfaceTxPowerLowThreshold_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 172, 1, 13, 1, 14),
    _PrvtLmmInterfaceTxPowerLowThreshold_Type()
)
prvtLmmInterfaceTxPowerLowThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prvtLmmInterfaceTxPowerLowThreshold.setStatus("current")


class _PrvtLmmInterfaceTxPowerHighThreshold_Type(Integer32):
    """Custom type prvtLmmInterfaceTxPowerHighThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-40, 8),
    )


_PrvtLmmInterfaceTxPowerHighThreshold_Type.__name__ = "Integer32"
_PrvtLmmInterfaceTxPowerHighThreshold_Object = MibTableColumn
prvtLmmInterfaceTxPowerHighThreshold = _PrvtLmmInterfaceTxPowerHighThreshold_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 172, 1, 13, 1, 15),
    _PrvtLmmInterfaceTxPowerHighThreshold_Type()
)
prvtLmmInterfaceTxPowerHighThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prvtLmmInterfaceTxPowerHighThreshold.setStatus("current")
_PrvtLmmInterfaceTxPowerValue_Type = Integer32
_PrvtLmmInterfaceTxPowerValue_Object = MibTableColumn
prvtLmmInterfaceTxPowerValue = _PrvtLmmInterfaceTxPowerValue_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 172, 1, 13, 1, 16),
    _PrvtLmmInterfaceTxPowerValue_Type()
)
prvtLmmInterfaceTxPowerValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtLmmInterfaceTxPowerValue.setStatus("current")
_PrvtLmmInterfaceTxPowerThresholdTxLo_Type = Integer32
_PrvtLmmInterfaceTxPowerThresholdTxLo_Object = MibTableColumn
prvtLmmInterfaceTxPowerThresholdTxLo = _PrvtLmmInterfaceTxPowerThresholdTxLo_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 172, 1, 13, 1, 17),
    _PrvtLmmInterfaceTxPowerThresholdTxLo_Type()
)
prvtLmmInterfaceTxPowerThresholdTxLo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtLmmInterfaceTxPowerThresholdTxLo.setStatus("current")
_PrvtLmmInterfaceTxPowerThresholdTxHi_Type = Integer32
_PrvtLmmInterfaceTxPowerThresholdTxHi_Object = MibTableColumn
prvtLmmInterfaceTxPowerThresholdTxHi = _PrvtLmmInterfaceTxPowerThresholdTxHi_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 172, 1, 13, 1, 18),
    _PrvtLmmInterfaceTxPowerThresholdTxHi_Type()
)
prvtLmmInterfaceTxPowerThresholdTxHi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtLmmInterfaceTxPowerThresholdTxHi.setStatus("current")
_PrvtLmmInterfaceTxPowerTestState_Type = TruthValue
_PrvtLmmInterfaceTxPowerTestState_Object = MibTableColumn
prvtLmmInterfaceTxPowerTestState = _PrvtLmmInterfaceTxPowerTestState_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 172, 1, 13, 1, 19),
    _PrvtLmmInterfaceTxPowerTestState_Type()
)
prvtLmmInterfaceTxPowerTestState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtLmmInterfaceTxPowerTestState.setStatus("current")
_PrvtLmmInterfaceOperStatus_Type = TruthValue
_PrvtLmmInterfaceOperStatus_Object = MibTableColumn
prvtLmmInterfaceOperStatus = _PrvtLmmInterfaceOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 172, 1, 13, 1, 20),
    _PrvtLmmInterfaceOperStatus_Type()
)
prvtLmmInterfaceOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtLmmInterfaceOperStatus.setStatus("current")

# Managed Objects groups


# Notification objects

prvtLmmTemperatureThresholdCrossed = NotificationType(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 172, 0, 1)
)
prvtLmmTemperatureThresholdCrossed.setObjects(
      *(("PRVT-LMM-MIB", "prvtLmmInterfaceTempValue"),
        ("PRVT-LMM-MIB", "prvtLmmInterfaceTempThresholdHi"),
        ("PRVT-LMM-MIB", "prvtLmmInterfaceTempThresholdLo"))
)
if mibBuilder.loadTexts:
    prvtLmmTemperatureThresholdCrossed.setStatus(
        "current"
    )

prvtLmmTxPowerThresholdCrossed = NotificationType(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 172, 0, 2)
)
prvtLmmTxPowerThresholdCrossed.setObjects(
      *(("PRVT-LMM-MIB", "prvtLmmInterfaceTxPowerValue"),
        ("PRVT-LMM-MIB", "prvtLmmInterfaceTxPowerThresholdTxHi"),
        ("PRVT-LMM-MIB", "prvtLmmInterfaceTxPowerThresholdTxLo"))
)
if mibBuilder.loadTexts:
    prvtLmmTxPowerThresholdCrossed.setStatus(
        "current"
    )

prvtLmmRxPowerThresholdCrossed = NotificationType(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 172, 0, 3)
)
prvtLmmRxPowerThresholdCrossed.setObjects(
      *(("PRVT-LMM-MIB", "prvtLmmInterfaceRxPowerValue"),
        ("PRVT-LMM-MIB", "prvtLmmInterfaceRxPowerThresholdRxHi"),
        ("PRVT-LMM-MIB", "prvtLmmInterfaceRxPowerThresholdRxLo"))
)
if mibBuilder.loadTexts:
    prvtLmmRxPowerThresholdCrossed.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "PRVT-LMM-MIB",
    **{"prvtLmmMIB": prvtLmmMIB,
       "prvtLmmNotifications": prvtLmmNotifications,
       "prvtLmmTemperatureThresholdCrossed": prvtLmmTemperatureThresholdCrossed,
       "prvtLmmTxPowerThresholdCrossed": prvtLmmTxPowerThresholdCrossed,
       "prvtLmmRxPowerThresholdCrossed": prvtLmmRxPowerThresholdCrossed,
       "prvtLmmObjects": prvtLmmObjects,
       "prvtLmmShutdown": prvtLmmShutdown,
       "prvtLmmDebug": prvtLmmDebug,
       "prvtLmmPeriod": prvtLmmPeriod,
       "prvtLmmTrap": prvtLmmTrap,
       "prvtLmmLog": prvtLmmLog,
       "prvtLmmLed": prvtLmmLed,
       "prvtLmmTemperatureHighThreshold": prvtLmmTemperatureHighThreshold,
       "prvtLmmTemperatureLowThreshold": prvtLmmTemperatureLowThreshold,
       "prvtLmmRxPowerLowThreshold": prvtLmmRxPowerLowThreshold,
       "prvtLmmRxPowerHighThreshold": prvtLmmRxPowerHighThreshold,
       "prvtLmmTxPowerLowThreshold": prvtLmmTxPowerLowThreshold,
       "prvtLmmTxPowerHighThreshold": prvtLmmTxPowerHighThreshold,
       "prvtLmmInterfaceTable": prvtLmmInterfaceTable,
       "prvtLmmInterfaceEntry": prvtLmmInterfaceEntry,
       "prvtLmmInterfaceShutdown": prvtLmmInterfaceShutdown,
       "prvtLmmInterfaceTempLowThreshold": prvtLmmInterfaceTempLowThreshold,
       "prvtLmmInterfaceTempHighThreshold": prvtLmmInterfaceTempHighThreshold,
       "prvtLmmInterfaceTempValue": prvtLmmInterfaceTempValue,
       "prvtLmmInterfaceTempThresholdLo": prvtLmmInterfaceTempThresholdLo,
       "prvtLmmInterfaceTempThresholdHi": prvtLmmInterfaceTempThresholdHi,
       "prvtLmmInterfaceTempTestState": prvtLmmInterfaceTempTestState,
       "prvtLmmInterfaceRxPowerLowThreshold": prvtLmmInterfaceRxPowerLowThreshold,
       "prvtLmmInterfaceRxPowerHighThreshold": prvtLmmInterfaceRxPowerHighThreshold,
       "prvtLmmInterfaceRxPowerValue": prvtLmmInterfaceRxPowerValue,
       "prvtLmmInterfaceRxPowerThresholdRxLo": prvtLmmInterfaceRxPowerThresholdRxLo,
       "prvtLmmInterfaceRxPowerThresholdRxHi": prvtLmmInterfaceRxPowerThresholdRxHi,
       "prvtLmmInterfaceRxPowerTestState": prvtLmmInterfaceRxPowerTestState,
       "prvtLmmInterfaceTxPowerLowThreshold": prvtLmmInterfaceTxPowerLowThreshold,
       "prvtLmmInterfaceTxPowerHighThreshold": prvtLmmInterfaceTxPowerHighThreshold,
       "prvtLmmInterfaceTxPowerValue": prvtLmmInterfaceTxPowerValue,
       "prvtLmmInterfaceTxPowerThresholdTxLo": prvtLmmInterfaceTxPowerThresholdTxLo,
       "prvtLmmInterfaceTxPowerThresholdTxHi": prvtLmmInterfaceTxPowerThresholdTxHi,
       "prvtLmmInterfaceTxPowerTestState": prvtLmmInterfaceTxPowerTestState,
       "prvtLmmInterfaceOperStatus": prvtLmmInterfaceOperStatus}
)
