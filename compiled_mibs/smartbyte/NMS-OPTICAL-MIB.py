# SNMP MIB module (NMS-OPTICAL-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\smartbyte\NMS-OPTICAL-MIB

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

opticalModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 56166, 1, 8, 1)
)
if mibBuilder.loadTexts:
    opticalModule.setRevisions(
        ("2023-12-08 11:37",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Optical_ObjectIdentity = ObjectIdentity
optical = _Optical_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 56166, 1, 8)
)
_OpticalModuleInfoTable_Object = MibTable
opticalModuleInfoTable = _OpticalModuleInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 56166, 1, 8, 2)
)
if mibBuilder.loadTexts:
    opticalModuleInfoTable.setStatus("current")
_OpticalModuleInfoEntry_Object = MibTableRow
opticalModuleInfoEntry = _OpticalModuleInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 56166, 1, 8, 2, 1)
)
opticalModuleInfoEntry.setIndexNames(
    (0, "NMS-OPTICAL-MIB", "opticalPortIndex"),
)
if mibBuilder.loadTexts:
    opticalModuleInfoEntry.setStatus("current")


class _OpticalPortIndex_Type(Integer32):
    """Custom type opticalPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_OpticalPortIndex_Type.__name__ = "Integer32"
_OpticalPortIndex_Object = MibTableColumn
opticalPortIndex = _OpticalPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 56166, 1, 8, 2, 1, 1),
    _OpticalPortIndex_Type()
)
opticalPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    opticalPortIndex.setStatus("current")


class _OpticalTransceiverType_Type(OctetString):
    """Custom type opticalTransceiverType based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_OpticalTransceiverType_Type.__name__ = "OctetString"
_OpticalTransceiverType_Object = MibTableColumn
opticalTransceiverType = _OpticalTransceiverType_Object(
    (1, 3, 6, 1, 4, 1, 56166, 1, 8, 2, 1, 2),
    _OpticalTransceiverType_Type()
)
opticalTransceiverType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    opticalTransceiverType.setStatus("current")


class _OpticalConnectType_Type(OctetString):
    """Custom type opticalConnectType based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_OpticalConnectType_Type.__name__ = "OctetString"
_OpticalConnectType_Object = MibTableColumn
opticalConnectType = _OpticalConnectType_Object(
    (1, 3, 6, 1, 4, 1, 56166, 1, 8, 2, 1, 3),
    _OpticalConnectType_Type()
)
opticalConnectType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    opticalConnectType.setStatus("current")
_OpticalWaveLength_Type = Integer32
_OpticalWaveLength_Object = MibTableColumn
opticalWaveLength = _OpticalWaveLength_Object(
    (1, 3, 6, 1, 4, 1, 56166, 1, 8, 2, 1, 4),
    _OpticalWaveLength_Type()
)
opticalWaveLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    opticalWaveLength.setStatus("current")


class _OpticalVendorName_Type(OctetString):
    """Custom type opticalVendorName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_OpticalVendorName_Type.__name__ = "OctetString"
_OpticalVendorName_Object = MibTableColumn
opticalVendorName = _OpticalVendorName_Object(
    (1, 3, 6, 1, 4, 1, 56166, 1, 8, 2, 1, 5),
    _OpticalVendorName_Type()
)
opticalVendorName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    opticalVendorName.setStatus("current")


class _OpticalSerialNumber_Type(OctetString):
    """Custom type opticalSerialNumber based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_OpticalSerialNumber_Type.__name__ = "OctetString"
_OpticalSerialNumber_Object = MibTableColumn
opticalSerialNumber = _OpticalSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 56166, 1, 8, 2, 1, 6),
    _OpticalSerialNumber_Type()
)
opticalSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    opticalSerialNumber.setStatus("current")


class _OpticalPartNumber_Type(OctetString):
    """Custom type opticalPartNumber based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_OpticalPartNumber_Type.__name__ = "OctetString"
_OpticalPartNumber_Object = MibTableColumn
opticalPartNumber = _OpticalPartNumber_Object(
    (1, 3, 6, 1, 4, 1, 56166, 1, 8, 2, 1, 7),
    _OpticalPartNumber_Type()
)
opticalPartNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    opticalPartNumber.setStatus("current")
_OpticalTransferDistance_Type = Integer32
_OpticalTransferDistance_Object = MibTableColumn
opticalTransferDistance = _OpticalTransferDistance_Object(
    (1, 3, 6, 1, 4, 1, 56166, 1, 8, 2, 1, 8),
    _OpticalTransferDistance_Type()
)
opticalTransferDistance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    opticalTransferDistance.setStatus("current")


class _OpticalSupportDDM_Type(Integer32):
    """Custom type opticalSupportDDM based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("support", 1),
          ("notSupport", 2))
    )


_OpticalSupportDDM_Type.__name__ = "Integer32"
_OpticalSupportDDM_Object = MibTableColumn
opticalSupportDDM = _OpticalSupportDDM_Object(
    (1, 3, 6, 1, 4, 1, 56166, 1, 8, 2, 1, 9),
    _OpticalSupportDDM_Type()
)
opticalSupportDDM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    opticalSupportDDM.setStatus("current")
_OpticalTemperature_Type = Integer32
_OpticalTemperature_Object = MibTableColumn
opticalTemperature = _OpticalTemperature_Object(
    (1, 3, 6, 1, 4, 1, 56166, 1, 8, 2, 1, 10),
    _OpticalTemperature_Type()
)
opticalTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    opticalTemperature.setStatus("current")
_OpticalVoltage_Type = Integer32
_OpticalVoltage_Object = MibTableColumn
opticalVoltage = _OpticalVoltage_Object(
    (1, 3, 6, 1, 4, 1, 56166, 1, 8, 2, 1, 11),
    _OpticalVoltage_Type()
)
opticalVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    opticalVoltage.setStatus("current")
_OpticalBiasCurrent_Type = Integer32
_OpticalBiasCurrent_Object = MibTableColumn
opticalBiasCurrent = _OpticalBiasCurrent_Object(
    (1, 3, 6, 1, 4, 1, 56166, 1, 8, 2, 1, 12),
    _OpticalBiasCurrent_Type()
)
opticalBiasCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    opticalBiasCurrent.setStatus("current")
_OpticalRxPower_Type = Integer32
_OpticalRxPower_Object = MibTableColumn
opticalRxPower = _OpticalRxPower_Object(
    (1, 3, 6, 1, 4, 1, 56166, 1, 8, 2, 1, 13),
    _OpticalRxPower_Type()
)
opticalRxPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    opticalRxPower.setStatus("current")
_OpticalTxPower_Type = Integer32
_OpticalTxPower_Object = MibTableColumn
opticalTxPower = _OpticalTxPower_Object(
    (1, 3, 6, 1, 4, 1, 56166, 1, 8, 2, 1, 14),
    _OpticalTxPower_Type()
)
opticalTxPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    opticalTxPower.setStatus("current")


class _OpticalTempHiAlarm_Type(Integer32):
    """Custom type opticalTempHiAlarm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-255, 255),
    )


_OpticalTempHiAlarm_Type.__name__ = "Integer32"
_OpticalTempHiAlarm_Object = MibTableColumn
opticalTempHiAlarm = _OpticalTempHiAlarm_Object(
    (1, 3, 6, 1, 4, 1, 56166, 1, 8, 2, 1, 15),
    _OpticalTempHiAlarm_Type()
)
opticalTempHiAlarm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    opticalTempHiAlarm.setStatus("current")


class _OpticalTempHiWarn_Type(Integer32):
    """Custom type opticalTempHiWarn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-255, 255),
    )


_OpticalTempHiWarn_Type.__name__ = "Integer32"
_OpticalTempHiWarn_Object = MibTableColumn
opticalTempHiWarn = _OpticalTempHiWarn_Object(
    (1, 3, 6, 1, 4, 1, 56166, 1, 8, 2, 1, 16),
    _OpticalTempHiWarn_Type()
)
opticalTempHiWarn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    opticalTempHiWarn.setStatus("current")


class _OpticalTempLoWarn_Type(Integer32):
    """Custom type opticalTempLoWarn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-255, 255),
    )


_OpticalTempLoWarn_Type.__name__ = "Integer32"
_OpticalTempLoWarn_Object = MibTableColumn
opticalTempLoWarn = _OpticalTempLoWarn_Object(
    (1, 3, 6, 1, 4, 1, 56166, 1, 8, 2, 1, 17),
    _OpticalTempLoWarn_Type()
)
opticalTempLoWarn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    opticalTempLoWarn.setStatus("current")


class _OpticalTempLoAlarm_Type(Integer32):
    """Custom type opticalTempLoAlarm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-255, 255),
    )


_OpticalTempLoAlarm_Type.__name__ = "Integer32"
_OpticalTempLoAlarm_Object = MibTableColumn
opticalTempLoAlarm = _OpticalTempLoAlarm_Object(
    (1, 3, 6, 1, 4, 1, 56166, 1, 8, 2, 1, 18),
    _OpticalTempLoAlarm_Type()
)
opticalTempLoAlarm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    opticalTempLoAlarm.setStatus("current")


class _OpticalVoltHiAlarm_Type(Integer32):
    """Custom type opticalVoltHiAlarm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 500),
    )


_OpticalVoltHiAlarm_Type.__name__ = "Integer32"
_OpticalVoltHiAlarm_Object = MibTableColumn
opticalVoltHiAlarm = _OpticalVoltHiAlarm_Object(
    (1, 3, 6, 1, 4, 1, 56166, 1, 8, 2, 1, 19),
    _OpticalVoltHiAlarm_Type()
)
opticalVoltHiAlarm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    opticalVoltHiAlarm.setStatus("current")


class _OpticalVoltHiWarn_Type(Integer32):
    """Custom type opticalVoltHiWarn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 500),
    )


_OpticalVoltHiWarn_Type.__name__ = "Integer32"
_OpticalVoltHiWarn_Object = MibTableColumn
opticalVoltHiWarn = _OpticalVoltHiWarn_Object(
    (1, 3, 6, 1, 4, 1, 56166, 1, 8, 2, 1, 20),
    _OpticalVoltHiWarn_Type()
)
opticalVoltHiWarn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    opticalVoltHiWarn.setStatus("current")


class _OpticalVoltLoWarn_Type(Integer32):
    """Custom type opticalVoltLoWarn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 500),
    )


_OpticalVoltLoWarn_Type.__name__ = "Integer32"
_OpticalVoltLoWarn_Object = MibTableColumn
opticalVoltLoWarn = _OpticalVoltLoWarn_Object(
    (1, 3, 6, 1, 4, 1, 56166, 1, 8, 2, 1, 21),
    _OpticalVoltLoWarn_Type()
)
opticalVoltLoWarn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    opticalVoltLoWarn.setStatus("current")


class _OpticalVoltLoAlarm_Type(Integer32):
    """Custom type opticalVoltLoAlarm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 500),
    )


_OpticalVoltLoAlarm_Type.__name__ = "Integer32"
_OpticalVoltLoAlarm_Object = MibTableColumn
opticalVoltLoAlarm = _OpticalVoltLoAlarm_Object(
    (1, 3, 6, 1, 4, 1, 56166, 1, 8, 2, 1, 22),
    _OpticalVoltLoAlarm_Type()
)
opticalVoltLoAlarm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    opticalVoltLoAlarm.setStatus("current")


class _OpticalBiasHiAlarm_Type(Integer32):
    """Custom type opticalBiasHiAlarm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 50000),
    )


_OpticalBiasHiAlarm_Type.__name__ = "Integer32"
_OpticalBiasHiAlarm_Object = MibTableColumn
opticalBiasHiAlarm = _OpticalBiasHiAlarm_Object(
    (1, 3, 6, 1, 4, 1, 56166, 1, 8, 2, 1, 23),
    _OpticalBiasHiAlarm_Type()
)
opticalBiasHiAlarm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    opticalBiasHiAlarm.setStatus("current")


class _OpticalBiasHiWarn_Type(Integer32):
    """Custom type opticalBiasHiWarn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 50000),
    )


_OpticalBiasHiWarn_Type.__name__ = "Integer32"
_OpticalBiasHiWarn_Object = MibTableColumn
opticalBiasHiWarn = _OpticalBiasHiWarn_Object(
    (1, 3, 6, 1, 4, 1, 56166, 1, 8, 2, 1, 24),
    _OpticalBiasHiWarn_Type()
)
opticalBiasHiWarn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    opticalBiasHiWarn.setStatus("current")


class _OpticalBiasLoWarn_Type(Integer32):
    """Custom type opticalBiasLoWarn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 50000),
    )


_OpticalBiasLoWarn_Type.__name__ = "Integer32"
_OpticalBiasLoWarn_Object = MibTableColumn
opticalBiasLoWarn = _OpticalBiasLoWarn_Object(
    (1, 3, 6, 1, 4, 1, 56166, 1, 8, 2, 1, 25),
    _OpticalBiasLoWarn_Type()
)
opticalBiasLoWarn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    opticalBiasLoWarn.setStatus("current")


class _OpticalBiasLoAlarm_Type(Integer32):
    """Custom type opticalBiasLoAlarm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 50000),
    )


_OpticalBiasLoAlarm_Type.__name__ = "Integer32"
_OpticalBiasLoAlarm_Object = MibTableColumn
opticalBiasLoAlarm = _OpticalBiasLoAlarm_Object(
    (1, 3, 6, 1, 4, 1, 56166, 1, 8, 2, 1, 26),
    _OpticalBiasLoAlarm_Type()
)
opticalBiasLoAlarm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    opticalBiasLoAlarm.setStatus("current")


class _OpticalRxHiAlarm_Type(Integer32):
    """Custom type opticalRxHiAlarm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-4000, 1000),
    )


_OpticalRxHiAlarm_Type.__name__ = "Integer32"
_OpticalRxHiAlarm_Object = MibTableColumn
opticalRxHiAlarm = _OpticalRxHiAlarm_Object(
    (1, 3, 6, 1, 4, 1, 56166, 1, 8, 2, 1, 27),
    _OpticalRxHiAlarm_Type()
)
opticalRxHiAlarm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    opticalRxHiAlarm.setStatus("current")


class _OpticalRxHiWarn_Type(Integer32):
    """Custom type opticalRxHiWarn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-4000, 1000),
    )


_OpticalRxHiWarn_Type.__name__ = "Integer32"
_OpticalRxHiWarn_Object = MibTableColumn
opticalRxHiWarn = _OpticalRxHiWarn_Object(
    (1, 3, 6, 1, 4, 1, 56166, 1, 8, 2, 1, 28),
    _OpticalRxHiWarn_Type()
)
opticalRxHiWarn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    opticalRxHiWarn.setStatus("current")


class _OpticalRxLoWarn_Type(Integer32):
    """Custom type opticalRxLoWarn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-4000, 1000),
    )


_OpticalRxLoWarn_Type.__name__ = "Integer32"
_OpticalRxLoWarn_Object = MibTableColumn
opticalRxLoWarn = _OpticalRxLoWarn_Object(
    (1, 3, 6, 1, 4, 1, 56166, 1, 8, 2, 1, 29),
    _OpticalRxLoWarn_Type()
)
opticalRxLoWarn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    opticalRxLoWarn.setStatus("current")


class _OpticalRxLoAlarm_Type(Integer32):
    """Custom type opticalRxLoAlarm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-4000, 1000),
    )


_OpticalRxLoAlarm_Type.__name__ = "Integer32"
_OpticalRxLoAlarm_Object = MibTableColumn
opticalRxLoAlarm = _OpticalRxLoAlarm_Object(
    (1, 3, 6, 1, 4, 1, 56166, 1, 8, 2, 1, 30),
    _OpticalRxLoAlarm_Type()
)
opticalRxLoAlarm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    opticalRxLoAlarm.setStatus("current")


class _OpticalTxHiAlarm_Type(Integer32):
    """Custom type opticalTxHiAlarm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-4000, 1000),
    )


_OpticalTxHiAlarm_Type.__name__ = "Integer32"
_OpticalTxHiAlarm_Object = MibTableColumn
opticalTxHiAlarm = _OpticalTxHiAlarm_Object(
    (1, 3, 6, 1, 4, 1, 56166, 1, 8, 2, 1, 31),
    _OpticalTxHiAlarm_Type()
)
opticalTxHiAlarm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    opticalTxHiAlarm.setStatus("current")


class _OpticalTxHiWarn_Type(Integer32):
    """Custom type opticalTxHiWarn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-4000, 1000),
    )


_OpticalTxHiWarn_Type.__name__ = "Integer32"
_OpticalTxHiWarn_Object = MibTableColumn
opticalTxHiWarn = _OpticalTxHiWarn_Object(
    (1, 3, 6, 1, 4, 1, 56166, 1, 8, 2, 1, 32),
    _OpticalTxHiWarn_Type()
)
opticalTxHiWarn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    opticalTxHiWarn.setStatus("current")


class _OpticalTxLoWarn_Type(Integer32):
    """Custom type opticalTxLoWarn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-4000, 1000),
    )


_OpticalTxLoWarn_Type.__name__ = "Integer32"
_OpticalTxLoWarn_Object = MibTableColumn
opticalTxLoWarn = _OpticalTxLoWarn_Object(
    (1, 3, 6, 1, 4, 1, 56166, 1, 8, 2, 1, 33),
    _OpticalTxLoWarn_Type()
)
opticalTxLoWarn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    opticalTxLoWarn.setStatus("current")


class _OpticalTxLoAlarm_Type(Integer32):
    """Custom type opticalTxLoAlarm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-4000, 1000),
    )


_OpticalTxLoAlarm_Type.__name__ = "Integer32"
_OpticalTxLoAlarm_Object = MibTableColumn
opticalTxLoAlarm = _OpticalTxLoAlarm_Object(
    (1, 3, 6, 1, 4, 1, 56166, 1, 8, 2, 1, 34),
    _OpticalTxLoAlarm_Type()
)
opticalTxLoAlarm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    opticalTxLoAlarm.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "NMS-OPTICAL-MIB",
    **{"optical": optical,
       "opticalModule": opticalModule,
       "opticalModuleInfoTable": opticalModuleInfoTable,
       "opticalModuleInfoEntry": opticalModuleInfoEntry,
       "opticalPortIndex": opticalPortIndex,
       "opticalTransceiverType": opticalTransceiverType,
       "opticalConnectType": opticalConnectType,
       "opticalWaveLength": opticalWaveLength,
       "opticalVendorName": opticalVendorName,
       "opticalSerialNumber": opticalSerialNumber,
       "opticalPartNumber": opticalPartNumber,
       "opticalTransferDistance": opticalTransferDistance,
       "opticalSupportDDM": opticalSupportDDM,
       "opticalTemperature": opticalTemperature,
       "opticalVoltage": opticalVoltage,
       "opticalBiasCurrent": opticalBiasCurrent,
       "opticalRxPower": opticalRxPower,
       "opticalTxPower": opticalTxPower,
       "opticalTempHiAlarm": opticalTempHiAlarm,
       "opticalTempHiWarn": opticalTempHiWarn,
       "opticalTempLoWarn": opticalTempLoWarn,
       "opticalTempLoAlarm": opticalTempLoAlarm,
       "opticalVoltHiAlarm": opticalVoltHiAlarm,
       "opticalVoltHiWarn": opticalVoltHiWarn,
       "opticalVoltLoWarn": opticalVoltLoWarn,
       "opticalVoltLoAlarm": opticalVoltLoAlarm,
       "opticalBiasHiAlarm": opticalBiasHiAlarm,
       "opticalBiasHiWarn": opticalBiasHiWarn,
       "opticalBiasLoWarn": opticalBiasLoWarn,
       "opticalBiasLoAlarm": opticalBiasLoAlarm,
       "opticalRxHiAlarm": opticalRxHiAlarm,
       "opticalRxHiWarn": opticalRxHiWarn,
       "opticalRxLoWarn": opticalRxLoWarn,
       "opticalRxLoAlarm": opticalRxLoAlarm,
       "opticalTxHiAlarm": opticalTxHiAlarm,
       "opticalTxHiWarn": opticalTxHiWarn,
       "opticalTxLoWarn": opticalTxLoWarn,
       "opticalTxLoAlarm": opticalTxLoAlarm}
)
