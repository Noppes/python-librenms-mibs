# SNMP MIB module (LIEBERT-GP-SRC-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\liebert\LIEBERT-GP-SRC-MIB

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

(lgpSrc,
 liebertSrcModuleReg) = mibBuilder.importSymbols(
    "LIEBERT-GP-REGISTRATION-MIB",
    "lgpSrc",
    "liebertSrcModuleReg")

(ModuleCompliance,
 NotificationGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup")

(sysUpTime,) = mibBuilder.importSymbols(
    "SNMPv2-MIB",
    "sysUpTime")

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

liebertGlobalProductsSrcModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 1, 12, 1)
)
if mibBuilder.loadTexts:
    liebertGlobalProductsSrcModule.setRevisions(
        ("2017-11-10 00:00",
         "2017-10-16 00:00",
         "2017-08-18 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_LgpSrcTable_Object = MibTable
lgpSrcTable = _LgpSrcTable_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 10, 1)
)
if mibBuilder.loadTexts:
    lgpSrcTable.setStatus("current")
_LgpSrcEntry_Object = MibTableRow
lgpSrcEntry = _LgpSrcEntry_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 10, 1, 1)
)
lgpSrcEntry.setIndexNames(
    (0, "LIEBERT-GP-SRC-MIB", "lgpSrcDevId"),
)
if mibBuilder.loadTexts:
    lgpSrcEntry.setStatus("current")
_LgpSrcDevId_Type = Unsigned32
_LgpSrcDevId_Object = MibTableColumn
lgpSrcDevId = _LgpSrcDevId_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 10, 1, 1, 1),
    _LgpSrcDevId_Type()
)
lgpSrcDevId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpSrcDevId.setStatus("current")
_LgpSrcDevAddress_Type = Unsigned32
_LgpSrcDevAddress_Object = MibTableColumn
lgpSrcDevAddress = _LgpSrcDevAddress_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 10, 1, 1, 2),
    _LgpSrcDevAddress_Type()
)
lgpSrcDevAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpSrcDevAddress.setStatus("current")


class _LgpSrcDevState_Type(Integer32):
    """Custom type lgpSrcDevState based on Integer32"""
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
        *(("enabled", 1),
          ("standbyOffline", 2),
          ("unavailableOffline", 3),
          ("absent", 4))
    )


_LgpSrcDevState_Type.__name__ = "Integer32"
_LgpSrcDevState_Object = MibTableColumn
lgpSrcDevState = _LgpSrcDevState_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 10, 1, 1, 3),
    _LgpSrcDevState_Type()
)
lgpSrcDevState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpSrcDevState.setStatus("current")


class _LgpSrcDevTemperatureDegF_Type(Integer32):
    """Custom type lgpSrcDevTemperatureDegF based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            2147483647
        )
    )
    namedValues = NamedValues(
        ("unknown", 2147483647)
    )


_LgpSrcDevTemperatureDegF_Type.__name__ = "Integer32"
_LgpSrcDevTemperatureDegF_Object = MibTableColumn
lgpSrcDevTemperatureDegF = _LgpSrcDevTemperatureDegF_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 10, 1, 1, 4),
    _LgpSrcDevTemperatureDegF_Type()
)
lgpSrcDevTemperatureDegF.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpSrcDevTemperatureDegF.setStatus("current")


class _LgpSrcDevTemperatureSetpointDegF_Type(Integer32):
    """Custom type lgpSrcDevTemperatureSetpointDegF based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            2147483647
        )
    )
    namedValues = NamedValues(
        ("unknown", 2147483647)
    )


_LgpSrcDevTemperatureSetpointDegF_Type.__name__ = "Integer32"
_LgpSrcDevTemperatureSetpointDegF_Object = MibTableColumn
lgpSrcDevTemperatureSetpointDegF = _LgpSrcDevTemperatureSetpointDegF_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 10, 1, 1, 5),
    _LgpSrcDevTemperatureSetpointDegF_Type()
)
lgpSrcDevTemperatureSetpointDegF.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgpSrcDevTemperatureSetpointDegF.setStatus("current")


class _LgpSrcDevTemperatureDegC_Type(Integer32):
    """Custom type lgpSrcDevTemperatureDegC based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            2147483647
        )
    )
    namedValues = NamedValues(
        ("unknown", 2147483647)
    )


_LgpSrcDevTemperatureDegC_Type.__name__ = "Integer32"
_LgpSrcDevTemperatureDegC_Object = MibTableColumn
lgpSrcDevTemperatureDegC = _LgpSrcDevTemperatureDegC_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 10, 1, 1, 6),
    _LgpSrcDevTemperatureDegC_Type()
)
lgpSrcDevTemperatureDegC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpSrcDevTemperatureDegC.setStatus("current")


class _LgpSrcDevTemperatureSetpointDegC_Type(Integer32):
    """Custom type lgpSrcDevTemperatureSetpointDegC based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            2147483647
        )
    )
    namedValues = NamedValues(
        ("unknown", 2147483647)
    )


_LgpSrcDevTemperatureSetpointDegC_Type.__name__ = "Integer32"
_LgpSrcDevTemperatureSetpointDegC_Object = MibTableColumn
lgpSrcDevTemperatureSetpointDegC = _LgpSrcDevTemperatureSetpointDegC_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 10, 1, 1, 7),
    _LgpSrcDevTemperatureSetpointDegC_Type()
)
lgpSrcDevTemperatureSetpointDegC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgpSrcDevTemperatureSetpointDegC.setStatus("current")


class _LgpSrcDevFanSpeed_Type(Integer32):
    """Custom type lgpSrcDevFanSpeed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              2147483647)
        )
    )
    namedValues = NamedValues(
        *(("low", 1),
          ("middle", 2),
          ("high", 3),
          ("auto", 4),
          ("unknown", 2147483647))
    )


_LgpSrcDevFanSpeed_Type.__name__ = "Integer32"
_LgpSrcDevFanSpeed_Object = MibTableColumn
lgpSrcDevFanSpeed = _LgpSrcDevFanSpeed_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 10, 1, 1, 8),
    _LgpSrcDevFanSpeed_Type()
)
lgpSrcDevFanSpeed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgpSrcDevFanSpeed.setStatus("current")


class _LgpSrcDevPowerStatus_Type(Integer32):
    """Custom type lgpSrcDevPowerStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2147483647)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1),
          ("unknown", 2147483647))
    )


_LgpSrcDevPowerStatus_Type.__name__ = "Integer32"
_LgpSrcDevPowerStatus_Object = MibTableColumn
lgpSrcDevPowerStatus = _LgpSrcDevPowerStatus_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 10, 1, 1, 9),
    _LgpSrcDevPowerStatus_Type()
)
lgpSrcDevPowerStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgpSrcDevPowerStatus.setStatus("current")


class _LgpSrcDevOperatingMode_Type(Integer32):
    """Custom type lgpSrcDevOperatingMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              2147483647)
        )
    )
    namedValues = NamedValues(
        *(("cooling", 0),
          ("dehumidify", 1),
          ("fan", 2),
          ("ai", 3),
          ("heating", 4),
          ("unknown", 2147483647))
    )


_LgpSrcDevOperatingMode_Type.__name__ = "Integer32"
_LgpSrcDevOperatingMode_Object = MibTableColumn
lgpSrcDevOperatingMode = _LgpSrcDevOperatingMode_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 10, 1, 1, 10),
    _LgpSrcDevOperatingMode_Type()
)
lgpSrcDevOperatingMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgpSrcDevOperatingMode.setStatus("current")


class _LgpSrcDevTemperatureHighThresholdDegF_Type(Integer32):
    """Custom type lgpSrcDevTemperatureHighThresholdDegF based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            2147483647
        )
    )
    namedValues = NamedValues(
        ("unknown", 2147483647)
    )


_LgpSrcDevTemperatureHighThresholdDegF_Type.__name__ = "Integer32"
_LgpSrcDevTemperatureHighThresholdDegF_Object = MibTableColumn
lgpSrcDevTemperatureHighThresholdDegF = _LgpSrcDevTemperatureHighThresholdDegF_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 10, 1, 1, 11),
    _LgpSrcDevTemperatureHighThresholdDegF_Type()
)
lgpSrcDevTemperatureHighThresholdDegF.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgpSrcDevTemperatureHighThresholdDegF.setStatus("current")
if mibBuilder.loadTexts:
    lgpSrcDevTemperatureHighThresholdDegF.setUnits("degrees Fahrenheit")


class _LgpSrcDevTemperatureLowThresholdDegF_Type(Integer32):
    """Custom type lgpSrcDevTemperatureLowThresholdDegF based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            2147483647
        )
    )
    namedValues = NamedValues(
        ("unknown", 2147483647)
    )


_LgpSrcDevTemperatureLowThresholdDegF_Type.__name__ = "Integer32"
_LgpSrcDevTemperatureLowThresholdDegF_Object = MibTableColumn
lgpSrcDevTemperatureLowThresholdDegF = _LgpSrcDevTemperatureLowThresholdDegF_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 10, 1, 1, 12),
    _LgpSrcDevTemperatureLowThresholdDegF_Type()
)
lgpSrcDevTemperatureLowThresholdDegF.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgpSrcDevTemperatureLowThresholdDegF.setStatus("current")
if mibBuilder.loadTexts:
    lgpSrcDevTemperatureLowThresholdDegF.setUnits("degrees Fahrenheit")


class _LgpSrcDevTemperatureHighThresholdDegC_Type(Integer32):
    """Custom type lgpSrcDevTemperatureHighThresholdDegC based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            2147483647
        )
    )
    namedValues = NamedValues(
        ("unknown", 2147483647)
    )


_LgpSrcDevTemperatureHighThresholdDegC_Type.__name__ = "Integer32"
_LgpSrcDevTemperatureHighThresholdDegC_Object = MibTableColumn
lgpSrcDevTemperatureHighThresholdDegC = _LgpSrcDevTemperatureHighThresholdDegC_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 10, 1, 1, 13),
    _LgpSrcDevTemperatureHighThresholdDegC_Type()
)
lgpSrcDevTemperatureHighThresholdDegC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgpSrcDevTemperatureHighThresholdDegC.setStatus("current")
if mibBuilder.loadTexts:
    lgpSrcDevTemperatureHighThresholdDegC.setUnits("degrees Celsius")


class _LgpSrcDevTemperatureLowThresholdDegC_Type(Integer32):
    """Custom type lgpSrcDevTemperatureLowThresholdDegC based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            2147483647
        )
    )
    namedValues = NamedValues(
        ("unknown", 2147483647)
    )


_LgpSrcDevTemperatureLowThresholdDegC_Type.__name__ = "Integer32"
_LgpSrcDevTemperatureLowThresholdDegC_Object = MibTableColumn
lgpSrcDevTemperatureLowThresholdDegC = _LgpSrcDevTemperatureLowThresholdDegC_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 10, 1, 1, 14),
    _LgpSrcDevTemperatureLowThresholdDegC_Type()
)
lgpSrcDevTemperatureLowThresholdDegC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgpSrcDevTemperatureLowThresholdDegC.setStatus("current")
if mibBuilder.loadTexts:
    lgpSrcDevTemperatureLowThresholdDegC.setUnits("degrees Celsius")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "LIEBERT-GP-SRC-MIB",
    **{"liebertGlobalProductsSrcModule": liebertGlobalProductsSrcModule,
       "lgpSrcTable": lgpSrcTable,
       "lgpSrcEntry": lgpSrcEntry,
       "lgpSrcDevId": lgpSrcDevId,
       "lgpSrcDevAddress": lgpSrcDevAddress,
       "lgpSrcDevState": lgpSrcDevState,
       "lgpSrcDevTemperatureDegF": lgpSrcDevTemperatureDegF,
       "lgpSrcDevTemperatureSetpointDegF": lgpSrcDevTemperatureSetpointDegF,
       "lgpSrcDevTemperatureDegC": lgpSrcDevTemperatureDegC,
       "lgpSrcDevTemperatureSetpointDegC": lgpSrcDevTemperatureSetpointDegC,
       "lgpSrcDevFanSpeed": lgpSrcDevFanSpeed,
       "lgpSrcDevPowerStatus": lgpSrcDevPowerStatus,
       "lgpSrcDevOperatingMode": lgpSrcDevOperatingMode,
       "lgpSrcDevTemperatureHighThresholdDegF": lgpSrcDevTemperatureHighThresholdDegF,
       "lgpSrcDevTemperatureLowThresholdDegF": lgpSrcDevTemperatureLowThresholdDegF,
       "lgpSrcDevTemperatureHighThresholdDegC": lgpSrcDevTemperatureHighThresholdDegC,
       "lgpSrcDevTemperatureLowThresholdDegC": lgpSrcDevTemperatureLowThresholdDegC}
)
