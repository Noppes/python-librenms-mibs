# SNMP MIB module (AVIAT-MODEM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\aviat-wtm\AVIAT-MODEM-MIB

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

(AviatModulationType,) = mibBuilder.importSymbols(
    "AVIAT-TEXTCONVENTION-MIB",
    "AviatModulationType")

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

aviatModemModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2509, 9, 3)
)
if mibBuilder.loadTexts:
    aviatModemModule.setRevisions(
        ("2018-09-20 11:30",
         "2017-03-28 01:19",
         "2015-04-28 15:30",
         "2014-09-19 15:05",
         "2014-02-03 22:20",
         "2014-01-21 01:57")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class AviatModemCapacityType(TextualConvention, Gauge32):
    status = "current"
    displayHint = "d"


# MIB Managed Objects in the order of their OIDs

_AviatModemConformance_ObjectIdentity = ObjectIdentity
aviatModemConformance = _AviatModemConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2509, 9, 3, 1)
)
_AviatModemGroups_ObjectIdentity = ObjectIdentity
aviatModemGroups = _AviatModemGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2509, 9, 3, 1, 1)
)
_AviatModemCompliance_ObjectIdentity = ObjectIdentity
aviatModemCompliance = _AviatModemCompliance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2509, 9, 3, 1, 2)
)
_AviatModemMIBObjects_ObjectIdentity = ObjectIdentity
aviatModemMIBObjects = _AviatModemMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2509, 9, 3, 2)
)
_AviatModemTable_Object = MibTable
aviatModemTable = _AviatModemTable_Object(
    (1, 3, 6, 1, 4, 1, 2509, 9, 3, 2, 1)
)
if mibBuilder.loadTexts:
    aviatModemTable.setStatus("current")
_AviatModemEntry_Object = MibTableRow
aviatModemEntry = _AviatModemEntry_Object(
    (1, 3, 6, 1, 4, 1, 2509, 9, 3, 2, 1, 1)
)
aviatModemEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
)
if mibBuilder.loadTexts:
    aviatModemEntry.setStatus("current")
_AviatModemBandwidth_Type = Gauge32
_AviatModemBandwidth_Object = MibTableColumn
aviatModemBandwidth = _AviatModemBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 2509, 9, 3, 2, 1, 1, 1),
    _AviatModemBandwidth_Type()
)
aviatModemBandwidth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aviatModemBandwidth.setStatus("current")
if mibBuilder.loadTexts:
    aviatModemBandwidth.setUnits("kHz")


class _AviatModemModulationType_Type(Integer32):
    """Custom type aviatModemModulationType based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("fixed", 0),
          ("acm256", 1),
          ("acm1024", 2))
    )


_AviatModemModulationType_Type.__name__ = "Integer32"
_AviatModemModulationType_Object = MibTableColumn
aviatModemModulationType = _AviatModemModulationType_Object(
    (1, 3, 6, 1, 4, 1, 2509, 9, 3, 2, 1, 1, 2),
    _AviatModemModulationType_Type()
)
aviatModemModulationType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aviatModemModulationType.setStatus("current")
_AviatModemModulationBase_Type = AviatModulationType
_AviatModemModulationBase_Object = MibTableColumn
aviatModemModulationBase = _AviatModemModulationBase_Object(
    (1, 3, 6, 1, 4, 1, 2509, 9, 3, 2, 1, 1, 3),
    _AviatModemModulationBase_Type()
)
aviatModemModulationBase.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aviatModemModulationBase.setStatus("current")
_AviatModemModulationMax_Type = AviatModulationType
_AviatModemModulationMax_Object = MibTableColumn
aviatModemModulationMax = _AviatModemModulationMax_Object(
    (1, 3, 6, 1, 4, 1, 2509, 9, 3, 2, 1, 1, 4),
    _AviatModemModulationMax_Type()
)
aviatModemModulationMax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aviatModemModulationMax.setStatus("current")
_AviatModemLicensedModulationMask_Type = AviatModulationType
_AviatModemLicensedModulationMask_Object = MibTableColumn
aviatModemLicensedModulationMask = _AviatModemLicensedModulationMask_Object(
    (1, 3, 6, 1, 4, 1, 2509, 9, 3, 2, 1, 1, 5),
    _AviatModemLicensedModulationMask_Type()
)
aviatModemLicensedModulationMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aviatModemLicensedModulationMask.setStatus("current")


class _AviatModemRegulatoryStandard_Type(Integer32):
    """Custom type aviatModemRegulatoryStandard based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("ansi", 2),
          ("etsi", 3))
    )


_AviatModemRegulatoryStandard_Type.__name__ = "Integer32"
_AviatModemRegulatoryStandard_Object = MibTableColumn
aviatModemRegulatoryStandard = _AviatModemRegulatoryStandard_Object(
    (1, 3, 6, 1, 4, 1, 2509, 9, 3, 2, 1, 1, 6),
    _AviatModemRegulatoryStandard_Type()
)
aviatModemRegulatoryStandard.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aviatModemRegulatoryStandard.setStatus("current")


class _AviatModemProfileVersion_Type(Integer32):
    """Custom type aviatModemProfileVersion based on Integer32"""
    defaultValue = 1


_AviatModemProfileVersion_Type.__name__ = "Integer32"
_AviatModemProfileVersion_Object = MibTableColumn
aviatModemProfileVersion = _AviatModemProfileVersion_Object(
    (1, 3, 6, 1, 4, 1, 2509, 9, 3, 2, 1, 1, 7),
    _AviatModemProfileVersion_Type()
)
aviatModemProfileVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aviatModemProfileVersion.setStatus("current")


class _AviatModemCapacity_Type(Integer32):
    """Custom type aviatModemCapacity based on Integer32"""
    defaultValue = 0


_AviatModemCapacity_Type.__name__ = "Integer32"
_AviatModemCapacity_Object = MibTableColumn
aviatModemCapacity = _AviatModemCapacity_Object(
    (1, 3, 6, 1, 4, 1, 2509, 9, 3, 2, 1, 1, 8),
    _AviatModemCapacity_Type()
)
aviatModemCapacity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aviatModemCapacity.setStatus("current")


class _AviatModemL1laLiteEnabled_Type(Integer32):
    """Custom type aviatModemL1laLiteEnabled based on Integer32"""
    defaultValue = 0

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


_AviatModemL1laLiteEnabled_Type.__name__ = "Integer32"
_AviatModemL1laLiteEnabled_Object = MibTableColumn
aviatModemL1laLiteEnabled = _AviatModemL1laLiteEnabled_Object(
    (1, 3, 6, 1, 4, 1, 2509, 9, 3, 2, 1, 1, 9),
    _AviatModemL1laLiteEnabled_Type()
)
aviatModemL1laLiteEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aviatModemL1laLiteEnabled.setStatus("current")


class _AviatModemMLHCEnabled_Type(Integer32):
    """Custom type aviatModemMLHCEnabled based on Integer32"""
    defaultValue = 0

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


_AviatModemMLHCEnabled_Type.__name__ = "Integer32"
_AviatModemMLHCEnabled_Object = MibTableColumn
aviatModemMLHCEnabled = _AviatModemMLHCEnabled_Object(
    (1, 3, 6, 1, 4, 1, 2509, 9, 3, 2, 1, 1, 10),
    _AviatModemMLHCEnabled_Type()
)
aviatModemMLHCEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aviatModemMLHCEnabled.setStatus("current")
_AviatModemCurCapacityTx_Type = AviatModemCapacityType
_AviatModemCurCapacityTx_Object = MibTableColumn
aviatModemCurCapacityTx = _AviatModemCurCapacityTx_Object(
    (1, 3, 6, 1, 4, 1, 2509, 9, 3, 2, 1, 1, 11),
    _AviatModemCurCapacityTx_Type()
)
aviatModemCurCapacityTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aviatModemCurCapacityTx.setStatus("current")
_AviatModemCurCapacityRx_Type = AviatModemCapacityType
_AviatModemCurCapacityRx_Object = MibTableColumn
aviatModemCurCapacityRx = _AviatModemCurCapacityRx_Object(
    (1, 3, 6, 1, 4, 1, 2509, 9, 3, 2, 1, 1, 12),
    _AviatModemCurCapacityRx_Type()
)
aviatModemCurCapacityRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aviatModemCurCapacityRx.setStatus("current")
_AviatModemCurModulationTx_Type = AviatModulationType
_AviatModemCurModulationTx_Object = MibTableColumn
aviatModemCurModulationTx = _AviatModemCurModulationTx_Object(
    (1, 3, 6, 1, 4, 1, 2509, 9, 3, 2, 1, 1, 13),
    _AviatModemCurModulationTx_Type()
)
aviatModemCurModulationTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aviatModemCurModulationTx.setStatus("current")
_AviatModemCurModulationRx_Type = AviatModulationType
_AviatModemCurModulationRx_Object = MibTableColumn
aviatModemCurModulationRx = _AviatModemCurModulationRx_Object(
    (1, 3, 6, 1, 4, 1, 2509, 9, 3, 2, 1, 1, 14),
    _AviatModemCurModulationRx_Type()
)
aviatModemCurModulationRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aviatModemCurModulationRx.setStatus("current")
_AviatModemModulationTable_Object = MibTable
aviatModemModulationTable = _AviatModemModulationTable_Object(
    (1, 3, 6, 1, 4, 1, 2509, 9, 3, 2, 2)
)
if mibBuilder.loadTexts:
    aviatModemModulationTable.setStatus("current")
_AviatModemModulationEntry_Object = MibTableRow
aviatModemModulationEntry = _AviatModemModulationEntry_Object(
    (1, 3, 6, 1, 4, 1, 2509, 9, 3, 2, 2, 1)
)
aviatModemModulationEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
    (0, "AVIAT-MODEM-MIB", "aviatModemModulationIndex"),
)
if mibBuilder.loadTexts:
    aviatModemModulationEntry.setStatus("current")
_AviatModemModulationIndex_Type = Gauge32
_AviatModemModulationIndex_Object = MibTableColumn
aviatModemModulationIndex = _AviatModemModulationIndex_Object(
    (1, 3, 6, 1, 4, 1, 2509, 9, 3, 2, 2, 1, 1),
    _AviatModemModulationIndex_Type()
)
aviatModemModulationIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    aviatModemModulationIndex.setStatus("current")
_AviatModemModulation_Type = AviatModulationType
_AviatModemModulation_Object = MibTableColumn
aviatModemModulation = _AviatModemModulation_Object(
    (1, 3, 6, 1, 4, 1, 2509, 9, 3, 2, 2, 1, 2),
    _AviatModemModulation_Type()
)
aviatModemModulation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aviatModemModulation.setStatus("current")
_AviatModemXpicTable_Object = MibTable
aviatModemXpicTable = _AviatModemXpicTable_Object(
    (1, 3, 6, 1, 4, 1, 2509, 9, 3, 2, 3)
)
if mibBuilder.loadTexts:
    aviatModemXpicTable.setStatus("current")
_AviatModemXpicEntry_Object = MibTableRow
aviatModemXpicEntry = _AviatModemXpicEntry_Object(
    (1, 3, 6, 1, 4, 1, 2509, 9, 3, 2, 3, 1)
)
aviatModemXpicEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
)
if mibBuilder.loadTexts:
    aviatModemXpicEntry.setStatus("current")


class _AviatModemXpicEnable_Type(TruthValue):
    """Custom type aviatModemXpicEnable based on TruthValue"""
    defaultValue = 2


_AviatModemXpicEnable_Type.__name__ = "TruthValue"
_AviatModemXpicEnable_Object = MibTableColumn
aviatModemXpicEnable = _AviatModemXpicEnable_Object(
    (1, 3, 6, 1, 4, 1, 2509, 9, 3, 2, 3, 1, 1),
    _AviatModemXpicEnable_Type()
)
aviatModemXpicEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aviatModemXpicEnable.setStatus("current")
_AviatModemStatusTable_Object = MibTable
aviatModemStatusTable = _AviatModemStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 2509, 9, 3, 2, 4)
)
if mibBuilder.loadTexts:
    aviatModemStatusTable.setStatus("current")
_AviatModemStatusEntry_Object = MibTableRow
aviatModemStatusEntry = _AviatModemStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 2509, 9, 3, 2, 4, 1)
)
aviatModemStatusEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
)
if mibBuilder.loadTexts:
    aviatModemStatusEntry.setStatus("current")


class _AviatModemStatusMaxCapacity_Type(Integer32):
    """Custom type aviatModemStatusMaxCapacity based on Integer32"""
    defaultValue = 0


_AviatModemStatusMaxCapacity_Type.__name__ = "Integer32"
_AviatModemStatusMaxCapacity_Object = MibTableColumn
aviatModemStatusMaxCapacity = _AviatModemStatusMaxCapacity_Object(
    (1, 3, 6, 1, 4, 1, 2509, 9, 3, 2, 4, 1, 1),
    _AviatModemStatusMaxCapacity_Type()
)
aviatModemStatusMaxCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aviatModemStatusMaxCapacity.setStatus("current")


class _AviatModemStatusOper_Type(Integer32):
    """Custom type aviatModemStatusOper based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("up", 1),
          ("down", 2),
          ("testing", 3),
          ("unknown", 4),
          ("dormant", 5),
          ("notPresent", 6),
          ("lowerLayerDown", 7))
    )


_AviatModemStatusOper_Type.__name__ = "Integer32"
_AviatModemStatusOper_Object = MibTableColumn
aviatModemStatusOper = _AviatModemStatusOper_Object(
    (1, 3, 6, 1, 4, 1, 2509, 9, 3, 2, 4, 1, 2),
    _AviatModemStatusOper_Type()
)
aviatModemStatusOper.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aviatModemStatusOper.setStatus("current")
_AviatModemModulationStatsTable_Object = MibTable
aviatModemModulationStatsTable = _AviatModemModulationStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 2509, 9, 3, 2, 5)
)
if mibBuilder.loadTexts:
    aviatModemModulationStatsTable.setStatus("current")
_AviatModemModulationStatsEntry_Object = MibTableRow
aviatModemModulationStatsEntry = _AviatModemModulationStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 2509, 9, 3, 2, 5, 1)
)
aviatModemModulationStatsEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
    (0, "AVIAT-MODEM-MIB", "aviatModemModStatsModulation"),
)
if mibBuilder.loadTexts:
    aviatModemModulationStatsEntry.setStatus("current")
_AviatModemModStatsModulation_Type = AviatModulationType
_AviatModemModStatsModulation_Object = MibTableColumn
aviatModemModStatsModulation = _AviatModemModStatsModulation_Object(
    (1, 3, 6, 1, 4, 1, 2509, 9, 3, 2, 5, 1, 1),
    _AviatModemModStatsModulation_Type()
)
aviatModemModStatsModulation.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    aviatModemModStatsModulation.setStatus("current")
_AviatModemModStatsTxSecs_Type = Counter32
_AviatModemModStatsTxSecs_Object = MibTableColumn
aviatModemModStatsTxSecs = _AviatModemModStatsTxSecs_Object(
    (1, 3, 6, 1, 4, 1, 2509, 9, 3, 2, 5, 1, 2),
    _AviatModemModStatsTxSecs_Type()
)
aviatModemModStatsTxSecs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aviatModemModStatsTxSecs.setStatus("current")
_AviatModemModStatsTxPct_Type = Gauge32
_AviatModemModStatsTxPct_Object = MibTableColumn
aviatModemModStatsTxPct = _AviatModemModStatsTxPct_Object(
    (1, 3, 6, 1, 4, 1, 2509, 9, 3, 2, 5, 1, 4),
    _AviatModemModStatsTxPct_Type()
)
aviatModemModStatsTxPct.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aviatModemModStatsTxPct.setStatus("current")
_AviatModemModStatsRxSecs_Type = Counter32
_AviatModemModStatsRxSecs_Object = MibTableColumn
aviatModemModStatsRxSecs = _AviatModemModStatsRxSecs_Object(
    (1, 3, 6, 1, 4, 1, 2509, 9, 3, 2, 5, 1, 5),
    _AviatModemModStatsRxSecs_Type()
)
aviatModemModStatsRxSecs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aviatModemModStatsRxSecs.setStatus("current")
_AviatModemModStatsRxPct_Type = Gauge32
_AviatModemModStatsRxPct_Object = MibTableColumn
aviatModemModStatsRxPct = _AviatModemModStatsRxPct_Object(
    (1, 3, 6, 1, 4, 1, 2509, 9, 3, 2, 5, 1, 6),
    _AviatModemModStatsRxPct_Type()
)
aviatModemModStatsRxPct.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aviatModemModStatsRxPct.setStatus("current")

# Managed Objects groups

aviatModemObjectGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2509, 9, 3, 1, 1, 1)
)
aviatModemObjectGroup.setObjects(
      *(("AVIAT-MODEM-MIB", "aviatModemBandwidth"),
        ("AVIAT-MODEM-MIB", "aviatModemModulationType"),
        ("AVIAT-MODEM-MIB", "aviatModemModulationBase"),
        ("AVIAT-MODEM-MIB", "aviatModemModulationMax"),
        ("AVIAT-MODEM-MIB", "aviatModemLicensedModulationMask"),
        ("AVIAT-MODEM-MIB", "aviatModemRegulatoryStandard"),
        ("AVIAT-MODEM-MIB", "aviatModemProfileVersion"),
        ("AVIAT-MODEM-MIB", "aviatModemCapacity"),
        ("AVIAT-MODEM-MIB", "aviatModemL1laLiteEnabled"),
        ("AVIAT-MODEM-MIB", "aviatModemModulation"),
        ("AVIAT-MODEM-MIB", "aviatModemStatusMaxCapacity"),
        ("AVIAT-MODEM-MIB", "aviatModemMLHCEnabled"))
)
if mibBuilder.loadTexts:
    aviatModemObjectGroup.setStatus("current")

aviatModemXpicGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2509, 9, 3, 1, 1, 2)
)
aviatModemXpicGroup.setObjects(
    ("AVIAT-MODEM-MIB", "aviatModemXpicEnable")
)
if mibBuilder.loadTexts:
    aviatModemXpicGroup.setStatus("current")

aviatModemModulationStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2509, 9, 3, 1, 1, 3)
)
aviatModemModulationStatsGroup.setObjects(
      *(("AVIAT-MODEM-MIB", "aviatModemModStatsTxSecs"),
        ("AVIAT-MODEM-MIB", "aviatModemModStatsTxPct"),
        ("AVIAT-MODEM-MIB", "aviatModemModStatsRxSecs"),
        ("AVIAT-MODEM-MIB", "aviatModemModStatsRxPct"))
)
if mibBuilder.loadTexts:
    aviatModemModulationStatsGroup.setStatus("current")

aviatModemModulationCurrentGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2509, 9, 3, 1, 1, 4)
)
aviatModemModulationCurrentGroup.setObjects(
      *(("AVIAT-MODEM-MIB", "aviatModemCurCapacityTx"),
        ("AVIAT-MODEM-MIB", "aviatModemCurCapacityRx"),
        ("AVIAT-MODEM-MIB", "aviatModemCurModulationTx"),
        ("AVIAT-MODEM-MIB", "aviatModemCurModulationRx"))
)
if mibBuilder.loadTexts:
    aviatModemModulationCurrentGroup.setStatus("current")

aviatModemStatusGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2509, 9, 3, 1, 1, 5)
)
aviatModemStatusGroup.setObjects(
    ("AVIAT-MODEM-MIB", "aviatModemStatusOper")
)
if mibBuilder.loadTexts:
    aviatModemStatusGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

aviatModemComplV1 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 2509, 9, 3, 1, 2, 1)
)
aviatModemComplV1.setObjects(
      *(("AVIAT-MODEM-MIB", "aviatModemObjectGroup"),
        ("AVIAT-MODEM-MIB", "aviatModemXpicGroup"),
        ("AVIAT-MODEM-MIB", "aviatModemModulationStatsGroup"),
        ("AVIAT-MODEM-MIB", "aviatModemModulationCurrentGroup"),
        ("AVIAT-MODEM-MIB", "aviatModemStatusGroup"))
)
if mibBuilder.loadTexts:
    aviatModemComplV1.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "AVIAT-MODEM-MIB",
    **{"AviatModemCapacityType": AviatModemCapacityType,
       "aviatModemModule": aviatModemModule,
       "aviatModemConformance": aviatModemConformance,
       "aviatModemGroups": aviatModemGroups,
       "aviatModemObjectGroup": aviatModemObjectGroup,
       "aviatModemXpicGroup": aviatModemXpicGroup,
       "aviatModemModulationStatsGroup": aviatModemModulationStatsGroup,
       "aviatModemModulationCurrentGroup": aviatModemModulationCurrentGroup,
       "aviatModemStatusGroup": aviatModemStatusGroup,
       "aviatModemCompliance": aviatModemCompliance,
       "aviatModemComplV1": aviatModemComplV1,
       "aviatModemMIBObjects": aviatModemMIBObjects,
       "aviatModemTable": aviatModemTable,
       "aviatModemEntry": aviatModemEntry,
       "aviatModemBandwidth": aviatModemBandwidth,
       "aviatModemModulationType": aviatModemModulationType,
       "aviatModemModulationBase": aviatModemModulationBase,
       "aviatModemModulationMax": aviatModemModulationMax,
       "aviatModemLicensedModulationMask": aviatModemLicensedModulationMask,
       "aviatModemRegulatoryStandard": aviatModemRegulatoryStandard,
       "aviatModemProfileVersion": aviatModemProfileVersion,
       "aviatModemCapacity": aviatModemCapacity,
       "aviatModemL1laLiteEnabled": aviatModemL1laLiteEnabled,
       "aviatModemMLHCEnabled": aviatModemMLHCEnabled,
       "aviatModemCurCapacityTx": aviatModemCurCapacityTx,
       "aviatModemCurCapacityRx": aviatModemCurCapacityRx,
       "aviatModemCurModulationTx": aviatModemCurModulationTx,
       "aviatModemCurModulationRx": aviatModemCurModulationRx,
       "aviatModemModulationTable": aviatModemModulationTable,
       "aviatModemModulationEntry": aviatModemModulationEntry,
       "aviatModemModulationIndex": aviatModemModulationIndex,
       "aviatModemModulation": aviatModemModulation,
       "aviatModemXpicTable": aviatModemXpicTable,
       "aviatModemXpicEntry": aviatModemXpicEntry,
       "aviatModemXpicEnable": aviatModemXpicEnable,
       "aviatModemStatusTable": aviatModemStatusTable,
       "aviatModemStatusEntry": aviatModemStatusEntry,
       "aviatModemStatusMaxCapacity": aviatModemStatusMaxCapacity,
       "aviatModemStatusOper": aviatModemStatusOper,
       "aviatModemModulationStatsTable": aviatModemModulationStatsTable,
       "aviatModemModulationStatsEntry": aviatModemModulationStatsEntry,
       "aviatModemModStatsModulation": aviatModemModStatsModulation,
       "aviatModemModStatsTxSecs": aviatModemModStatsTxSecs,
       "aviatModemModStatsTxPct": aviatModemModStatsTxPct,
       "aviatModemModStatsRxSecs": aviatModemModStatsRxSecs,
       "aviatModemModStatsRxPct": aviatModemModStatsRxPct}
)
