# SNMP MIB module (AVIAT-RF-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\aviat-wtm\AVIAT-RF-MIB

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

(AviatDecibel,
 AviatModulationType,
 AviatPowerLevel,
 AviatRfuSideBandType) = mibBuilder.importSymbols(
    "AVIAT-TEXTCONVENTION-MIB",
    "AviatDecibel",
    "AviatModulationType",
    "AviatPowerLevel",
    "AviatRfuSideBandType")

(entPhysicalIndex,) = mibBuilder.importSymbols(
    "ENTITY-MIB",
    "entPhysicalIndex")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention",
    "TruthValue")

(aviatModules,) = mibBuilder.importSymbols(
    "STXN-GLOBALREGISTER-MIB",
    "aviatModules")


# MODULE-IDENTITY

aviatRfModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2509, 9, 5)
)
if mibBuilder.loadTexts:
    aviatRfModule.setRevisions(
        ("2015-11-05 14:30",
         "2015-07-29 08:45",
         "2015-02-10 09:48",
         "2015-01-27 02:46",
         "2014-11-07 02:47",
         "2014-01-21 01:57")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AviatRfConformance_ObjectIdentity = ObjectIdentity
aviatRfConformance = _AviatRfConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2509, 9, 5, 1)
)
_AviatRfGroups_ObjectIdentity = ObjectIdentity
aviatRfGroups = _AviatRfGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2509, 9, 5, 1, 1)
)
_AviatRfCompliance_ObjectIdentity = ObjectIdentity
aviatRfCompliance = _AviatRfCompliance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2509, 9, 5, 1, 2)
)
_AviatRfMIBObjects_ObjectIdentity = ObjectIdentity
aviatRfMIBObjects = _AviatRfMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2509, 9, 5, 2)
)
_AviatRfConfigTable_Object = MibTable
aviatRfConfigTable = _AviatRfConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 2509, 9, 5, 2, 1)
)
if mibBuilder.loadTexts:
    aviatRfConfigTable.setStatus("current")
_AviatRfConfigEntry_Object = MibTableRow
aviatRfConfigEntry = _AviatRfConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 2509, 9, 5, 2, 1, 1)
)
aviatRfConfigEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
)
if mibBuilder.loadTexts:
    aviatRfConfigEntry.setStatus("current")


class _AviatRfFreqTx_Type(Integer32):
    """Custom type aviatRfFreqTx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AviatRfFreqTx_Type.__name__ = "Integer32"
_AviatRfFreqTx_Object = MibTableColumn
aviatRfFreqTx = _AviatRfFreqTx_Object(
    (1, 3, 6, 1, 4, 1, 2509, 9, 5, 2, 1, 1, 1),
    _AviatRfFreqTx_Type()
)
aviatRfFreqTx.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aviatRfFreqTx.setStatus("current")
if mibBuilder.loadTexts:
    aviatRfFreqTx.setUnits("kHz")


class _AviatRfFreqRx_Type(Integer32):
    """Custom type aviatRfFreqRx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AviatRfFreqRx_Type.__name__ = "Integer32"
_AviatRfFreqRx_Object = MibTableColumn
aviatRfFreqRx = _AviatRfFreqRx_Object(
    (1, 3, 6, 1, 4, 1, 2509, 9, 5, 2, 1, 1, 2),
    _AviatRfFreqRx_Type()
)
aviatRfFreqRx.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aviatRfFreqRx.setStatus("current")
if mibBuilder.loadTexts:
    aviatRfFreqRx.setUnits("kHz")
_AviatRfPowerSet_Type = AviatPowerLevel
_AviatRfPowerSet_Object = MibTableColumn
aviatRfPowerSet = _AviatRfPowerSet_Object(
    (1, 3, 6, 1, 4, 1, 2509, 9, 5, 2, 1, 1, 3),
    _AviatRfPowerSet_Type()
)
aviatRfPowerSet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aviatRfPowerSet.setStatus("current")
if mibBuilder.loadTexts:
    aviatRfPowerSet.setUnits("0.1 dBm")


class _AviatRfTxMute_Type(TruthValue):
    """Custom type aviatRfTxMute based on TruthValue"""
    defaultValue = 1


_AviatRfTxMute_Type.__name__ = "TruthValue"
_AviatRfTxMute_Object = MibTableColumn
aviatRfTxMute = _AviatRfTxMute_Object(
    (1, 3, 6, 1, 4, 1, 2509, 9, 5, 2, 1, 1, 4),
    _AviatRfTxMute_Type()
)
aviatRfTxMute.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aviatRfTxMute.setStatus("current")


class _AviatRfHighGain_Type(TruthValue):
    """Custom type aviatRfHighGain based on TruthValue"""
    defaultValue = 2


_AviatRfHighGain_Type.__name__ = "TruthValue"
_AviatRfHighGain_Object = MibTableColumn
aviatRfHighGain = _AviatRfHighGain_Object(
    (1, 3, 6, 1, 4, 1, 2509, 9, 5, 2, 1, 1, 5),
    _AviatRfHighGain_Type()
)
aviatRfHighGain.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aviatRfHighGain.setStatus("current")


class _AviatRfBandSelection_Type(Integer32):
    """Custom type aviatRfBandSelection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("upper5g8", 1),
          ("lower6g", 2))
    )


_AviatRfBandSelection_Type.__name__ = "Integer32"
_AviatRfBandSelection_Object = MibTableColumn
aviatRfBandSelection = _AviatRfBandSelection_Object(
    (1, 3, 6, 1, 4, 1, 2509, 9, 5, 2, 1, 1, 6),
    _AviatRfBandSelection_Type()
)
aviatRfBandSelection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aviatRfBandSelection.setStatus("current")
_AviatRfATPCTable_Object = MibTable
aviatRfATPCTable = _AviatRfATPCTable_Object(
    (1, 3, 6, 1, 4, 1, 2509, 9, 5, 2, 2)
)
if mibBuilder.loadTexts:
    aviatRfATPCTable.setStatus("current")
_AviatRfATPCEntry_Object = MibTableRow
aviatRfATPCEntry = _AviatRfATPCEntry_Object(
    (1, 3, 6, 1, 4, 1, 2509, 9, 5, 2, 2, 1)
)
aviatRfATPCEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
)
if mibBuilder.loadTexts:
    aviatRfATPCEntry.setStatus("current")
_AviatRfATPCEnabled_Type = TruthValue
_AviatRfATPCEnabled_Object = MibTableColumn
aviatRfATPCEnabled = _AviatRfATPCEnabled_Object(
    (1, 3, 6, 1, 4, 1, 2509, 9, 5, 2, 2, 1, 1),
    _AviatRfATPCEnabled_Type()
)
aviatRfATPCEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aviatRfATPCEnabled.setStatus("current")


class _AviatRfATPCTargetFadeMargin_Type(AviatDecibel):
    """Custom type aviatRfATPCTargetFadeMargin based on AviatDecibel"""
    defaultValue = 100


_AviatRfATPCTargetFadeMargin_Type.__name__ = "AviatDecibel"
_AviatRfATPCTargetFadeMargin_Object = MibTableColumn
aviatRfATPCTargetFadeMargin = _AviatRfATPCTargetFadeMargin_Object(
    (1, 3, 6, 1, 4, 1, 2509, 9, 5, 2, 2, 1, 2),
    _AviatRfATPCTargetFadeMargin_Type()
)
aviatRfATPCTargetFadeMargin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aviatRfATPCTargetFadeMargin.setStatus("current")
if mibBuilder.loadTexts:
    aviatRfATPCTargetFadeMargin.setUnits("0.1 dB")


class _AviatRfATPCMaximumPower_Type(AviatPowerLevel):
    """Custom type aviatRfATPCMaximumPower based on AviatPowerLevel"""
    defaultValue = 200


_AviatRfATPCMaximumPower_Type.__name__ = "AviatPowerLevel"
_AviatRfATPCMaximumPower_Object = MibTableColumn
aviatRfATPCMaximumPower = _AviatRfATPCMaximumPower_Object(
    (1, 3, 6, 1, 4, 1, 2509, 9, 5, 2, 2, 1, 3),
    _AviatRfATPCMaximumPower_Type()
)
aviatRfATPCMaximumPower.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aviatRfATPCMaximumPower.setStatus("current")
if mibBuilder.loadTexts:
    aviatRfATPCMaximumPower.setUnits("0.1 dBm")


class _AviatRfATPCMinimumPower_Type(AviatPowerLevel):
    """Custom type aviatRfATPCMinimumPower based on AviatPowerLevel"""
    defaultValue = 0


_AviatRfATPCMinimumPower_Type.__name__ = "AviatPowerLevel"
_AviatRfATPCMinimumPower_Object = MibTableColumn
aviatRfATPCMinimumPower = _AviatRfATPCMinimumPower_Object(
    (1, 3, 6, 1, 4, 1, 2509, 9, 5, 2, 2, 1, 4),
    _AviatRfATPCMinimumPower_Type()
)
aviatRfATPCMinimumPower.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aviatRfATPCMinimumPower.setStatus("current")
if mibBuilder.loadTexts:
    aviatRfATPCMinimumPower.setUnits("0.1 dBm")


class _AviatRfATPCFCCCompliant_Type(TruthValue):
    """Custom type aviatRfATPCFCCCompliant based on TruthValue"""
    defaultValue = 2


_AviatRfATPCFCCCompliant_Type.__name__ = "TruthValue"
_AviatRfATPCFCCCompliant_Object = MibTableColumn
aviatRfATPCFCCCompliant = _AviatRfATPCFCCCompliant_Object(
    (1, 3, 6, 1, 4, 1, 2509, 9, 5, 2, 2, 1, 5),
    _AviatRfATPCFCCCompliant_Type()
)
aviatRfATPCFCCCompliant.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aviatRfATPCFCCCompliant.setStatus("current")
_AviatRfuCapabilityTable_Object = MibTable
aviatRfuCapabilityTable = _AviatRfuCapabilityTable_Object(
    (1, 3, 6, 1, 4, 1, 2509, 9, 5, 2, 3)
)
if mibBuilder.loadTexts:
    aviatRfuCapabilityTable.setStatus("current")
_AviatRfuCapabilityEntry_Object = MibTableRow
aviatRfuCapabilityEntry = _AviatRfuCapabilityEntry_Object(
    (1, 3, 6, 1, 4, 1, 2509, 9, 5, 2, 3, 1)
)
aviatRfuCapabilityEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
)
if mibBuilder.loadTexts:
    aviatRfuCapabilityEntry.setStatus("current")
_AviatRfuTxFreqMax_Type = Integer32
_AviatRfuTxFreqMax_Object = MibTableColumn
aviatRfuTxFreqMax = _AviatRfuTxFreqMax_Object(
    (1, 3, 6, 1, 4, 1, 2509, 9, 5, 2, 3, 1, 1),
    _AviatRfuTxFreqMax_Type()
)
aviatRfuTxFreqMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aviatRfuTxFreqMax.setStatus("current")
_AviatRfuTxFreqMin_Type = Integer32
_AviatRfuTxFreqMin_Object = MibTableColumn
aviatRfuTxFreqMin = _AviatRfuTxFreqMin_Object(
    (1, 3, 6, 1, 4, 1, 2509, 9, 5, 2, 3, 1, 2),
    _AviatRfuTxFreqMin_Type()
)
aviatRfuTxFreqMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aviatRfuTxFreqMin.setStatus("current")
_AviatRfuRxFreqMax_Type = Integer32
_AviatRfuRxFreqMax_Object = MibTableColumn
aviatRfuRxFreqMax = _AviatRfuRxFreqMax_Object(
    (1, 3, 6, 1, 4, 1, 2509, 9, 5, 2, 3, 1, 3),
    _AviatRfuRxFreqMax_Type()
)
aviatRfuRxFreqMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aviatRfuRxFreqMax.setStatus("current")
_AviatRfuRxFreqMin_Type = Integer32
_AviatRfuRxFreqMin_Object = MibTableColumn
aviatRfuRxFreqMin = _AviatRfuRxFreqMin_Object(
    (1, 3, 6, 1, 4, 1, 2509, 9, 5, 2, 3, 1, 4),
    _AviatRfuRxFreqMin_Type()
)
aviatRfuRxFreqMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aviatRfuRxFreqMin.setStatus("current")
_AviatRfuFreqStepMin_Type = Integer32
_AviatRfuFreqStepMin_Object = MibTableColumn
aviatRfuFreqStepMin = _AviatRfuFreqStepMin_Object(
    (1, 3, 6, 1, 4, 1, 2509, 9, 5, 2, 3, 1, 5),
    _AviatRfuFreqStepMin_Type()
)
aviatRfuFreqStepMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aviatRfuFreqStepMin.setStatus("current")
_AviatRfuBandwidthMax_Type = Integer32
_AviatRfuBandwidthMax_Object = MibTableColumn
aviatRfuBandwidthMax = _AviatRfuBandwidthMax_Object(
    (1, 3, 6, 1, 4, 1, 2509, 9, 5, 2, 3, 1, 6),
    _AviatRfuBandwidthMax_Type()
)
aviatRfuBandwidthMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aviatRfuBandwidthMax.setStatus("current")
_AviatRfuTxRxSpacingMax_Type = Integer32
_AviatRfuTxRxSpacingMax_Object = MibTableColumn
aviatRfuTxRxSpacingMax = _AviatRfuTxRxSpacingMax_Object(
    (1, 3, 6, 1, 4, 1, 2509, 9, 5, 2, 3, 1, 7),
    _AviatRfuTxRxSpacingMax_Type()
)
aviatRfuTxRxSpacingMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aviatRfuTxRxSpacingMax.setStatus("current")
_AviatRfuTxRxSpacingMin_Type = Integer32
_AviatRfuTxRxSpacingMin_Object = MibTableColumn
aviatRfuTxRxSpacingMin = _AviatRfuTxRxSpacingMin_Object(
    (1, 3, 6, 1, 4, 1, 2509, 9, 5, 2, 3, 1, 8),
    _AviatRfuTxRxSpacingMin_Type()
)
aviatRfuTxRxSpacingMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aviatRfuTxRxSpacingMin.setStatus("current")
_AviatRfuTxPowerMax_Type = Integer32
_AviatRfuTxPowerMax_Object = MibTableColumn
aviatRfuTxPowerMax = _AviatRfuTxPowerMax_Object(
    (1, 3, 6, 1, 4, 1, 2509, 9, 5, 2, 3, 1, 9),
    _AviatRfuTxPowerMax_Type()
)
aviatRfuTxPowerMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aviatRfuTxPowerMax.setStatus("current")
_AviatRfuTxPowerMin_Type = Integer32
_AviatRfuTxPowerMin_Object = MibTableColumn
aviatRfuTxPowerMin = _AviatRfuTxPowerMin_Object(
    (1, 3, 6, 1, 4, 1, 2509, 9, 5, 2, 3, 1, 10),
    _AviatRfuTxPowerMin_Type()
)
aviatRfuTxPowerMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aviatRfuTxPowerMin.setStatus("current")
_AviatRfuPowerStep_Type = Integer32
_AviatRfuPowerStep_Object = MibTableColumn
aviatRfuPowerStep = _AviatRfuPowerStep_Object(
    (1, 3, 6, 1, 4, 1, 2509, 9, 5, 2, 3, 1, 11),
    _AviatRfuPowerStep_Type()
)
aviatRfuPowerStep.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aviatRfuPowerStep.setStatus("current")
_AviatRfuNoiseFigure_Type = Integer32
_AviatRfuNoiseFigure_Object = MibTableColumn
aviatRfuNoiseFigure = _AviatRfuNoiseFigure_Object(
    (1, 3, 6, 1, 4, 1, 2509, 9, 5, 2, 3, 1, 12),
    _AviatRfuNoiseFigure_Type()
)
aviatRfuNoiseFigure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aviatRfuNoiseFigure.setStatus("current")
_AviatRfuModulationMax_Type = AviatModulationType
_AviatRfuModulationMax_Object = MibTableColumn
aviatRfuModulationMax = _AviatRfuModulationMax_Object(
    (1, 3, 6, 1, 4, 1, 2509, 9, 5, 2, 3, 1, 13),
    _AviatRfuModulationMax_Type()
)
aviatRfuModulationMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aviatRfuModulationMax.setStatus("current")
_AviatRfuTxRxSpacingPreset_Type = TruthValue
_AviatRfuTxRxSpacingPreset_Object = MibTableColumn
aviatRfuTxRxSpacingPreset = _AviatRfuTxRxSpacingPreset_Object(
    (1, 3, 6, 1, 4, 1, 2509, 9, 5, 2, 3, 1, 14),
    _AviatRfuTxRxSpacingPreset_Type()
)
aviatRfuTxRxSpacingPreset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aviatRfuTxRxSpacingPreset.setStatus("current")
_AviatRfuTxSideBand_Type = AviatRfuSideBandType
_AviatRfuTxSideBand_Object = MibTableColumn
aviatRfuTxSideBand = _AviatRfuTxSideBand_Object(
    (1, 3, 6, 1, 4, 1, 2509, 9, 5, 2, 3, 1, 15),
    _AviatRfuTxSideBand_Type()
)
aviatRfuTxSideBand.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aviatRfuTxSideBand.setStatus("current")
_AviatRfuTxPowerLimit_Type = Integer32
_AviatRfuTxPowerLimit_Object = MibTableColumn
aviatRfuTxPowerLimit = _AviatRfuTxPowerLimit_Object(
    (1, 3, 6, 1, 4, 1, 2509, 9, 5, 2, 3, 1, 16),
    _AviatRfuTxPowerLimit_Type()
)
aviatRfuTxPowerLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aviatRfuTxPowerLimit.setStatus("current")
_AviatRfuTxSpacingTable_Object = MibTable
aviatRfuTxSpacingTable = _AviatRfuTxSpacingTable_Object(
    (1, 3, 6, 1, 4, 1, 2509, 9, 5, 2, 4)
)
if mibBuilder.loadTexts:
    aviatRfuTxSpacingTable.setStatus("current")
_AviatRfuTxSpacingEntry_Object = MibTableRow
aviatRfuTxSpacingEntry = _AviatRfuTxSpacingEntry_Object(
    (1, 3, 6, 1, 4, 1, 2509, 9, 5, 2, 4, 1)
)
aviatRfuTxSpacingEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
    (0, "AVIAT-RF-MIB", "aviatRfuTxSpacingIndex"),
)
if mibBuilder.loadTexts:
    aviatRfuTxSpacingEntry.setStatus("current")
_AviatRfuTxSpacingIndex_Type = Gauge32
_AviatRfuTxSpacingIndex_Object = MibTableColumn
aviatRfuTxSpacingIndex = _AviatRfuTxSpacingIndex_Object(
    (1, 3, 6, 1, 4, 1, 2509, 9, 5, 2, 4, 1, 1),
    _AviatRfuTxSpacingIndex_Type()
)
aviatRfuTxSpacingIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    aviatRfuTxSpacingIndex.setStatus("current")
_AviatRfuTxSpacingFreq_Type = Integer32
_AviatRfuTxSpacingFreq_Object = MibTableColumn
aviatRfuTxSpacingFreq = _AviatRfuTxSpacingFreq_Object(
    (1, 3, 6, 1, 4, 1, 2509, 9, 5, 2, 4, 1, 2),
    _AviatRfuTxSpacingFreq_Type()
)
aviatRfuTxSpacingFreq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aviatRfuTxSpacingFreq.setStatus("current")
_AviatRfuDetailsTable_Object = MibTable
aviatRfuDetailsTable = _AviatRfuDetailsTable_Object(
    (1, 3, 6, 1, 4, 1, 2509, 9, 5, 2, 5)
)
if mibBuilder.loadTexts:
    aviatRfuDetailsTable.setStatus("current")
_AviatRfuDetailsEntry_Object = MibTableRow
aviatRfuDetailsEntry = _AviatRfuDetailsEntry_Object(
    (1, 3, 6, 1, 4, 1, 2509, 9, 5, 2, 5, 1)
)
aviatRfuDetailsEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
)
if mibBuilder.loadTexts:
    aviatRfuDetailsEntry.setStatus("current")
_AviatRfuType_Type = Integer32
_AviatRfuType_Object = MibTableColumn
aviatRfuType = _AviatRfuType_Object(
    (1, 3, 6, 1, 4, 1, 2509, 9, 5, 2, 5, 1, 1),
    _AviatRfuType_Type()
)
aviatRfuType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aviatRfuType.setStatus("current")
_AviatRfuFreqBand_Type = Integer32
_AviatRfuFreqBand_Object = MibTableColumn
aviatRfuFreqBand = _AviatRfuFreqBand_Object(
    (1, 3, 6, 1, 4, 1, 2509, 9, 5, 2, 5, 1, 2),
    _AviatRfuFreqBand_Type()
)
aviatRfuFreqBand.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aviatRfuFreqBand.setStatus("current")
_AviatRfuPowerAmp_Type = Integer32
_AviatRfuPowerAmp_Object = MibTableColumn
aviatRfuPowerAmp = _AviatRfuPowerAmp_Object(
    (1, 3, 6, 1, 4, 1, 2509, 9, 5, 2, 5, 1, 3),
    _AviatRfuPowerAmp_Type()
)
aviatRfuPowerAmp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aviatRfuPowerAmp.setStatus("current")


class _AviatRfuSemiconductorTech_Type(Integer32):
    """Custom type aviatRfuSemiconductorTech based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("gaas", 0),
          ("gan", 1))
    )


_AviatRfuSemiconductorTech_Type.__name__ = "Integer32"
_AviatRfuSemiconductorTech_Object = MibTableColumn
aviatRfuSemiconductorTech = _AviatRfuSemiconductorTech_Object(
    (1, 3, 6, 1, 4, 1, 2509, 9, 5, 2, 5, 1, 4),
    _AviatRfuSemiconductorTech_Type()
)
aviatRfuSemiconductorTech.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aviatRfuSemiconductorTech.setStatus("current")
_AviatRfuUnlicensed5G8Cap_Type = TruthValue
_AviatRfuUnlicensed5G8Cap_Object = MibTableColumn
aviatRfuUnlicensed5G8Cap = _AviatRfuUnlicensed5G8Cap_Object(
    (1, 3, 6, 1, 4, 1, 2509, 9, 5, 2, 5, 1, 5),
    _AviatRfuUnlicensed5G8Cap_Type()
)
aviatRfuUnlicensed5G8Cap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aviatRfuUnlicensed5G8Cap.setStatus("current")
_AviatRfuExternalCoaxPresent_Type = TruthValue
_AviatRfuExternalCoaxPresent_Object = MibTableColumn
aviatRfuExternalCoaxPresent = _AviatRfuExternalCoaxPresent_Object(
    (1, 3, 6, 1, 4, 1, 2509, 9, 5, 2, 5, 1, 6),
    _AviatRfuExternalCoaxPresent_Type()
)
aviatRfuExternalCoaxPresent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aviatRfuExternalCoaxPresent.setStatus("current")

# Managed Objects groups

aviatRfObjectGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2509, 9, 5, 1, 1, 1)
)
aviatRfObjectGroup.setObjects(
      *(("AVIAT-RF-MIB", "aviatRfFreqTx"),
        ("AVIAT-RF-MIB", "aviatRfFreqRx"),
        ("AVIAT-RF-MIB", "aviatRfPowerSet"),
        ("AVIAT-RF-MIB", "aviatRfTxMute"),
        ("AVIAT-RF-MIB", "aviatRfHighGain"),
        ("AVIAT-RF-MIB", "aviatRfBandSelection"),
        ("AVIAT-RF-MIB", "aviatRfATPCEnabled"),
        ("AVIAT-RF-MIB", "aviatRfATPCTargetFadeMargin"),
        ("AVIAT-RF-MIB", "aviatRfATPCMaximumPower"),
        ("AVIAT-RF-MIB", "aviatRfATPCMinimumPower"),
        ("AVIAT-RF-MIB", "aviatRfATPCFCCCompliant"),
        ("AVIAT-RF-MIB", "aviatRfuTxFreqMax"),
        ("AVIAT-RF-MIB", "aviatRfuTxFreqMin"),
        ("AVIAT-RF-MIB", "aviatRfuRxFreqMax"),
        ("AVIAT-RF-MIB", "aviatRfuRxFreqMin"),
        ("AVIAT-RF-MIB", "aviatRfuFreqStepMin"),
        ("AVIAT-RF-MIB", "aviatRfuBandwidthMax"),
        ("AVIAT-RF-MIB", "aviatRfuTxRxSpacingMax"),
        ("AVIAT-RF-MIB", "aviatRfuTxRxSpacingMin"),
        ("AVIAT-RF-MIB", "aviatRfuTxPowerMax"),
        ("AVIAT-RF-MIB", "aviatRfuTxPowerMin"),
        ("AVIAT-RF-MIB", "aviatRfuPowerStep"),
        ("AVIAT-RF-MIB", "aviatRfuNoiseFigure"),
        ("AVIAT-RF-MIB", "aviatRfuModulationMax"),
        ("AVIAT-RF-MIB", "aviatRfuTxRxSpacingPreset"),
        ("AVIAT-RF-MIB", "aviatRfuTxSideBand"),
        ("AVIAT-RF-MIB", "aviatRfuTxPowerLimit"),
        ("AVIAT-RF-MIB", "aviatRfuTxSpacingFreq"),
        ("AVIAT-RF-MIB", "aviatRfuType"),
        ("AVIAT-RF-MIB", "aviatRfuFreqBand"),
        ("AVIAT-RF-MIB", "aviatRfuPowerAmp"),
        ("AVIAT-RF-MIB", "aviatRfuSemiconductorTech"),
        ("AVIAT-RF-MIB", "aviatRfuUnlicensed5G8Cap"),
        ("AVIAT-RF-MIB", "aviatRfuExternalCoaxPresent"))
)
if mibBuilder.loadTexts:
    aviatRfObjectGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

aviatRfComplV1 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 2509, 9, 5, 1, 2, 1)
)
aviatRfComplV1.setObjects(
    ("AVIAT-RF-MIB", "aviatRfObjectGroup")
)
if mibBuilder.loadTexts:
    aviatRfComplV1.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "AVIAT-RF-MIB",
    **{"aviatRfModule": aviatRfModule,
       "aviatRfConformance": aviatRfConformance,
       "aviatRfGroups": aviatRfGroups,
       "aviatRfObjectGroup": aviatRfObjectGroup,
       "aviatRfCompliance": aviatRfCompliance,
       "aviatRfComplV1": aviatRfComplV1,
       "aviatRfMIBObjects": aviatRfMIBObjects,
       "aviatRfConfigTable": aviatRfConfigTable,
       "aviatRfConfigEntry": aviatRfConfigEntry,
       "aviatRfFreqTx": aviatRfFreqTx,
       "aviatRfFreqRx": aviatRfFreqRx,
       "aviatRfPowerSet": aviatRfPowerSet,
       "aviatRfTxMute": aviatRfTxMute,
       "aviatRfHighGain": aviatRfHighGain,
       "aviatRfBandSelection": aviatRfBandSelection,
       "aviatRfATPCTable": aviatRfATPCTable,
       "aviatRfATPCEntry": aviatRfATPCEntry,
       "aviatRfATPCEnabled": aviatRfATPCEnabled,
       "aviatRfATPCTargetFadeMargin": aviatRfATPCTargetFadeMargin,
       "aviatRfATPCMaximumPower": aviatRfATPCMaximumPower,
       "aviatRfATPCMinimumPower": aviatRfATPCMinimumPower,
       "aviatRfATPCFCCCompliant": aviatRfATPCFCCCompliant,
       "aviatRfuCapabilityTable": aviatRfuCapabilityTable,
       "aviatRfuCapabilityEntry": aviatRfuCapabilityEntry,
       "aviatRfuTxFreqMax": aviatRfuTxFreqMax,
       "aviatRfuTxFreqMin": aviatRfuTxFreqMin,
       "aviatRfuRxFreqMax": aviatRfuRxFreqMax,
       "aviatRfuRxFreqMin": aviatRfuRxFreqMin,
       "aviatRfuFreqStepMin": aviatRfuFreqStepMin,
       "aviatRfuBandwidthMax": aviatRfuBandwidthMax,
       "aviatRfuTxRxSpacingMax": aviatRfuTxRxSpacingMax,
       "aviatRfuTxRxSpacingMin": aviatRfuTxRxSpacingMin,
       "aviatRfuTxPowerMax": aviatRfuTxPowerMax,
       "aviatRfuTxPowerMin": aviatRfuTxPowerMin,
       "aviatRfuPowerStep": aviatRfuPowerStep,
       "aviatRfuNoiseFigure": aviatRfuNoiseFigure,
       "aviatRfuModulationMax": aviatRfuModulationMax,
       "aviatRfuTxRxSpacingPreset": aviatRfuTxRxSpacingPreset,
       "aviatRfuTxSideBand": aviatRfuTxSideBand,
       "aviatRfuTxPowerLimit": aviatRfuTxPowerLimit,
       "aviatRfuTxSpacingTable": aviatRfuTxSpacingTable,
       "aviatRfuTxSpacingEntry": aviatRfuTxSpacingEntry,
       "aviatRfuTxSpacingIndex": aviatRfuTxSpacingIndex,
       "aviatRfuTxSpacingFreq": aviatRfuTxSpacingFreq,
       "aviatRfuDetailsTable": aviatRfuDetailsTable,
       "aviatRfuDetailsEntry": aviatRfuDetailsEntry,
       "aviatRfuType": aviatRfuType,
       "aviatRfuFreqBand": aviatRfuFreqBand,
       "aviatRfuPowerAmp": aviatRfuPowerAmp,
       "aviatRfuSemiconductorTech": aviatRfuSemiconductorTech,
       "aviatRfuUnlicensed5G8Cap": aviatRfuUnlicensed5G8Cap,
       "aviatRfuExternalCoaxPresent": aviatRfuExternalCoaxPresent}
)
