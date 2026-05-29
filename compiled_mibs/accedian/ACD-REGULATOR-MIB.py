# SNMP MIB module (ACD-REGULATOR-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\accedian\ACD-REGULATOR-MIB

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

(acdMibs,) = mibBuilder.importSymbols(
    "ACCEDIAN-SMI",
    "acdMibs")

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

(DateAndTime,
 DisplayString,
 PhysAddress,
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

acdRegulator = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 22420, 2, 6)
)
if mibBuilder.loadTexts:
    acdRegulator.setRevisions(
        ("2017-02-21 01:00",
         "2016-09-23 01:00",
         "2016-05-26 01:00",
         "2014-06-09 00:00",
         "2013-12-01 00:00",
         "2012-01-10 01:00",
         "2011-10-10 01:00",
         "2010-11-10 01:00",
         "2008-05-01 01:00",
         "2008-02-06 01:00",
         "2007-03-28 01:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AcdRegulatorTable_Object = MibTable
acdRegulatorTable = _AcdRegulatorTable_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 6, 1)
)
if mibBuilder.loadTexts:
    acdRegulatorTable.setStatus("current")
_AcdRegulatorEntry_Object = MibTableRow
acdRegulatorEntry = _AcdRegulatorEntry_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 6, 1, 1)
)
acdRegulatorEntry.setIndexNames(
    (0, "ACD-REGULATOR-MIB", "acdRegulatorID"),
)
if mibBuilder.loadTexts:
    acdRegulatorEntry.setStatus("current")
_AcdRegulatorID_Type = Unsigned32
_AcdRegulatorID_Object = MibTableColumn
acdRegulatorID = _AcdRegulatorID_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 6, 1, 1, 1),
    _AcdRegulatorID_Type()
)
acdRegulatorID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    acdRegulatorID.setStatus("current")


class _AcdRegulatorName_Type(DisplayString):
    """Custom type acdRegulatorName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_AcdRegulatorName_Type.__name__ = "DisplayString"
_AcdRegulatorName_Object = MibTableColumn
acdRegulatorName = _AcdRegulatorName_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 6, 1, 1, 2),
    _AcdRegulatorName_Type()
)
acdRegulatorName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acdRegulatorName.setStatus("current")


class _AcdRegulatorCir_Type(Unsigned32):
    """Custom type acdRegulatorCir based on Unsigned32"""
    defaultValue = 20000


_AcdRegulatorCir_Type.__name__ = "Unsigned32"
_AcdRegulatorCir_Object = MibTableColumn
acdRegulatorCir = _AcdRegulatorCir_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 6, 1, 1, 3),
    _AcdRegulatorCir_Type()
)
acdRegulatorCir.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acdRegulatorCir.setStatus("current")
if mibBuilder.loadTexts:
    acdRegulatorCir.setUnits("Kbps")


class _AcdRegulatorCbs_Type(Unsigned32):
    """Custom type acdRegulatorCbs based on Unsigned32"""
    defaultValue = 8


_AcdRegulatorCbs_Type.__name__ = "Unsigned32"
_AcdRegulatorCbs_Object = MibTableColumn
acdRegulatorCbs = _AcdRegulatorCbs_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 6, 1, 1, 4),
    _AcdRegulatorCbs_Type()
)
acdRegulatorCbs.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acdRegulatorCbs.setStatus("current")
if mibBuilder.loadTexts:
    acdRegulatorCbs.setUnits("KiB")


class _AcdRegulatorEir_Type(Unsigned32):
    """Custom type acdRegulatorEir based on Unsigned32"""
    defaultValue = 1000


_AcdRegulatorEir_Type.__name__ = "Unsigned32"
_AcdRegulatorEir_Object = MibTableColumn
acdRegulatorEir = _AcdRegulatorEir_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 6, 1, 1, 5),
    _AcdRegulatorEir_Type()
)
acdRegulatorEir.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acdRegulatorEir.setStatus("current")
if mibBuilder.loadTexts:
    acdRegulatorEir.setUnits("Kbps")


class _AcdRegulatorEbs_Type(Unsigned32):
    """Custom type acdRegulatorEbs based on Unsigned32"""
    defaultValue = 8


_AcdRegulatorEbs_Type.__name__ = "Unsigned32"
_AcdRegulatorEbs_Object = MibTableColumn
acdRegulatorEbs = _AcdRegulatorEbs_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 6, 1, 1, 6),
    _AcdRegulatorEbs_Type()
)
acdRegulatorEbs.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acdRegulatorEbs.setStatus("current")
if mibBuilder.loadTexts:
    acdRegulatorEbs.setUnits("KiB")


class _AcdRegulatorIsBlind_Type(TruthValue):
    """Custom type acdRegulatorIsBlind based on TruthValue"""
    defaultValue = 2


_AcdRegulatorIsBlind_Type.__name__ = "TruthValue"
_AcdRegulatorIsBlind_Object = MibTableColumn
acdRegulatorIsBlind = _AcdRegulatorIsBlind_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 6, 1, 1, 7),
    _AcdRegulatorIsBlind_Type()
)
acdRegulatorIsBlind.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acdRegulatorIsBlind.setStatus("current")


class _AcdRegulatorIsCouple_Type(TruthValue):
    """Custom type acdRegulatorIsCouple based on TruthValue"""
    defaultValue = 2


_AcdRegulatorIsCouple_Type.__name__ = "TruthValue"
_AcdRegulatorIsCouple_Object = MibTableColumn
acdRegulatorIsCouple = _AcdRegulatorIsCouple_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 6, 1, 1, 8),
    _AcdRegulatorIsCouple_Type()
)
acdRegulatorIsCouple.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acdRegulatorIsCouple.setStatus("current")
_AcdRegulatorRowStatus_Type = RowStatus
_AcdRegulatorRowStatus_Object = MibTableColumn
acdRegulatorRowStatus = _AcdRegulatorRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 6, 1, 1, 9),
    _AcdRegulatorRowStatus_Type()
)
acdRegulatorRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acdRegulatorRowStatus.setStatus("current")


class _AcdRegulatorWorkingRate_Type(Integer32):
    """Custom type acdRegulatorWorkingRate based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("layer1", 1),
          ("layer2", 2))
    )


_AcdRegulatorWorkingRate_Type.__name__ = "Integer32"
_AcdRegulatorWorkingRate_Object = MibTableColumn
acdRegulatorWorkingRate = _AcdRegulatorWorkingRate_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 6, 1, 1, 10),
    _AcdRegulatorWorkingRate_Type()
)
acdRegulatorWorkingRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdRegulatorWorkingRate.setStatus("current")


class _AcdRegulatorCirMax_Type(Unsigned32):
    """Custom type acdRegulatorCirMax based on Unsigned32"""
    defaultValue = 20000


_AcdRegulatorCirMax_Type.__name__ = "Unsigned32"
_AcdRegulatorCirMax_Object = MibTableColumn
acdRegulatorCirMax = _AcdRegulatorCirMax_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 6, 1, 1, 11),
    _AcdRegulatorCirMax_Type()
)
acdRegulatorCirMax.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acdRegulatorCirMax.setStatus("current")
if mibBuilder.loadTexts:
    acdRegulatorCirMax.setUnits("Kbps")


class _AcdRegulatorEirMax_Type(Unsigned32):
    """Custom type acdRegulatorEirMax based on Unsigned32"""
    defaultValue = 1000


_AcdRegulatorEirMax_Type.__name__ = "Unsigned32"
_AcdRegulatorEirMax_Object = MibTableColumn
acdRegulatorEirMax = _AcdRegulatorEirMax_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 6, 1, 1, 12),
    _AcdRegulatorEirMax_Type()
)
acdRegulatorEirMax.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acdRegulatorEirMax.setStatus("current")
if mibBuilder.loadTexts:
    acdRegulatorEirMax.setUnits("Kbps")
_AcdRegulatorStatsTable_Object = MibTable
acdRegulatorStatsTable = _AcdRegulatorStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 6, 2)
)
if mibBuilder.loadTexts:
    acdRegulatorStatsTable.setStatus("current")
_AcdRegulatorStatsEntry_Object = MibTableRow
acdRegulatorStatsEntry = _AcdRegulatorStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 6, 2, 1)
)
acdRegulatorStatsEntry.setIndexNames(
    (0, "ACD-REGULATOR-MIB", "acdRegulatorStatsID"),
)
if mibBuilder.loadTexts:
    acdRegulatorStatsEntry.setStatus("current")
_AcdRegulatorStatsID_Type = Unsigned32
_AcdRegulatorStatsID_Object = MibTableColumn
acdRegulatorStatsID = _AcdRegulatorStatsID_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 6, 2, 1, 1),
    _AcdRegulatorStatsID_Type()
)
acdRegulatorStatsID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    acdRegulatorStatsID.setStatus("current")
_AcdRegulatorStatsAcceptOctets_Type = Counter32
_AcdRegulatorStatsAcceptOctets_Object = MibTableColumn
acdRegulatorStatsAcceptOctets = _AcdRegulatorStatsAcceptOctets_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 6, 2, 1, 2),
    _AcdRegulatorStatsAcceptOctets_Type()
)
acdRegulatorStatsAcceptOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdRegulatorStatsAcceptOctets.setStatus("current")
if mibBuilder.loadTexts:
    acdRegulatorStatsAcceptOctets.setUnits("Octets")
_AcdRegulatorStatsAcceptOverflowOctets_Type = Counter32
_AcdRegulatorStatsAcceptOverflowOctets_Object = MibTableColumn
acdRegulatorStatsAcceptOverflowOctets = _AcdRegulatorStatsAcceptOverflowOctets_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 6, 2, 1, 3),
    _AcdRegulatorStatsAcceptOverflowOctets_Type()
)
acdRegulatorStatsAcceptOverflowOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdRegulatorStatsAcceptOverflowOctets.setStatus("current")
_AcdRegulatorStatsAcceptHCOctets_Type = Counter64
_AcdRegulatorStatsAcceptHCOctets_Object = MibTableColumn
acdRegulatorStatsAcceptHCOctets = _AcdRegulatorStatsAcceptHCOctets_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 6, 2, 1, 4),
    _AcdRegulatorStatsAcceptHCOctets_Type()
)
acdRegulatorStatsAcceptHCOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdRegulatorStatsAcceptHCOctets.setStatus("current")
if mibBuilder.loadTexts:
    acdRegulatorStatsAcceptHCOctets.setUnits("Octets")
_AcdRegulatorStatsAcceptPkts_Type = Counter32
_AcdRegulatorStatsAcceptPkts_Object = MibTableColumn
acdRegulatorStatsAcceptPkts = _AcdRegulatorStatsAcceptPkts_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 6, 2, 1, 5),
    _AcdRegulatorStatsAcceptPkts_Type()
)
acdRegulatorStatsAcceptPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdRegulatorStatsAcceptPkts.setStatus("current")
if mibBuilder.loadTexts:
    acdRegulatorStatsAcceptPkts.setUnits("Packets")
_AcdRegulatorStatsAcceptOverflowPkts_Type = Counter32
_AcdRegulatorStatsAcceptOverflowPkts_Object = MibTableColumn
acdRegulatorStatsAcceptOverflowPkts = _AcdRegulatorStatsAcceptOverflowPkts_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 6, 2, 1, 6),
    _AcdRegulatorStatsAcceptOverflowPkts_Type()
)
acdRegulatorStatsAcceptOverflowPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdRegulatorStatsAcceptOverflowPkts.setStatus("current")
_AcdRegulatorStatsAcceptHCPkts_Type = Counter64
_AcdRegulatorStatsAcceptHCPkts_Object = MibTableColumn
acdRegulatorStatsAcceptHCPkts = _AcdRegulatorStatsAcceptHCPkts_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 6, 2, 1, 7),
    _AcdRegulatorStatsAcceptHCPkts_Type()
)
acdRegulatorStatsAcceptHCPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdRegulatorStatsAcceptHCPkts.setStatus("current")
if mibBuilder.loadTexts:
    acdRegulatorStatsAcceptHCPkts.setUnits("Packets")
_AcdRegulatorStatsAcceptRate_Type = Gauge32
_AcdRegulatorStatsAcceptRate_Object = MibTableColumn
acdRegulatorStatsAcceptRate = _AcdRegulatorStatsAcceptRate_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 6, 2, 1, 8),
    _AcdRegulatorStatsAcceptRate_Type()
)
acdRegulatorStatsAcceptRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdRegulatorStatsAcceptRate.setStatus("current")
if mibBuilder.loadTexts:
    acdRegulatorStatsAcceptRate.setUnits("Kbps")
_AcdRegulatorStatsDropOctets_Type = Counter32
_AcdRegulatorStatsDropOctets_Object = MibTableColumn
acdRegulatorStatsDropOctets = _AcdRegulatorStatsDropOctets_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 6, 2, 1, 9),
    _AcdRegulatorStatsDropOctets_Type()
)
acdRegulatorStatsDropOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdRegulatorStatsDropOctets.setStatus("current")
if mibBuilder.loadTexts:
    acdRegulatorStatsDropOctets.setUnits("Octets")
_AcdRegulatorStatsDropOverflowOctets_Type = Counter32
_AcdRegulatorStatsDropOverflowOctets_Object = MibTableColumn
acdRegulatorStatsDropOverflowOctets = _AcdRegulatorStatsDropOverflowOctets_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 6, 2, 1, 10),
    _AcdRegulatorStatsDropOverflowOctets_Type()
)
acdRegulatorStatsDropOverflowOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdRegulatorStatsDropOverflowOctets.setStatus("current")
_AcdRegulatorStatsDropHCOctets_Type = Counter64
_AcdRegulatorStatsDropHCOctets_Object = MibTableColumn
acdRegulatorStatsDropHCOctets = _AcdRegulatorStatsDropHCOctets_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 6, 2, 1, 11),
    _AcdRegulatorStatsDropHCOctets_Type()
)
acdRegulatorStatsDropHCOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdRegulatorStatsDropHCOctets.setStatus("current")
if mibBuilder.loadTexts:
    acdRegulatorStatsDropHCOctets.setUnits("Octets")
_AcdRegulatorStatsDropPkts_Type = Counter32
_AcdRegulatorStatsDropPkts_Object = MibTableColumn
acdRegulatorStatsDropPkts = _AcdRegulatorStatsDropPkts_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 6, 2, 1, 12),
    _AcdRegulatorStatsDropPkts_Type()
)
acdRegulatorStatsDropPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdRegulatorStatsDropPkts.setStatus("current")
if mibBuilder.loadTexts:
    acdRegulatorStatsDropPkts.setUnits("Packets")
_AcdRegulatorStatsDropOverflowPkts_Type = Counter32
_AcdRegulatorStatsDropOverflowPkts_Object = MibTableColumn
acdRegulatorStatsDropOverflowPkts = _AcdRegulatorStatsDropOverflowPkts_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 6, 2, 1, 13),
    _AcdRegulatorStatsDropOverflowPkts_Type()
)
acdRegulatorStatsDropOverflowPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdRegulatorStatsDropOverflowPkts.setStatus("current")
_AcdRegulatorStatsDropHCPkts_Type = Counter64
_AcdRegulatorStatsDropHCPkts_Object = MibTableColumn
acdRegulatorStatsDropHCPkts = _AcdRegulatorStatsDropHCPkts_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 6, 2, 1, 14),
    _AcdRegulatorStatsDropHCPkts_Type()
)
acdRegulatorStatsDropHCPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdRegulatorStatsDropHCPkts.setStatus("current")
if mibBuilder.loadTexts:
    acdRegulatorStatsDropHCPkts.setUnits("Packets")
_AcdRegulatorStatsDropRate_Type = Gauge32
_AcdRegulatorStatsDropRate_Object = MibTableColumn
acdRegulatorStatsDropRate = _AcdRegulatorStatsDropRate_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 6, 2, 1, 15),
    _AcdRegulatorStatsDropRate_Type()
)
acdRegulatorStatsDropRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdRegulatorStatsDropRate.setStatus("current")
if mibBuilder.loadTexts:
    acdRegulatorStatsDropRate.setUnits("Kbps")
_AcdRegulatorStatsGreenHCOctets_Type = Counter64
_AcdRegulatorStatsGreenHCOctets_Object = MibTableColumn
acdRegulatorStatsGreenHCOctets = _AcdRegulatorStatsGreenHCOctets_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 6, 2, 1, 16),
    _AcdRegulatorStatsGreenHCOctets_Type()
)
acdRegulatorStatsGreenHCOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdRegulatorStatsGreenHCOctets.setStatus("current")
if mibBuilder.loadTexts:
    acdRegulatorStatsGreenHCOctets.setUnits("Octets")
_AcdRegulatorStatsGreenHCPkts_Type = Counter64
_AcdRegulatorStatsGreenHCPkts_Object = MibTableColumn
acdRegulatorStatsGreenHCPkts = _AcdRegulatorStatsGreenHCPkts_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 6, 2, 1, 17),
    _AcdRegulatorStatsGreenHCPkts_Type()
)
acdRegulatorStatsGreenHCPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdRegulatorStatsGreenHCPkts.setStatus("current")
if mibBuilder.loadTexts:
    acdRegulatorStatsGreenHCPkts.setUnits("Packets")
_AcdRegulatorStatsYellowHCOctets_Type = Counter64
_AcdRegulatorStatsYellowHCOctets_Object = MibTableColumn
acdRegulatorStatsYellowHCOctets = _AcdRegulatorStatsYellowHCOctets_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 6, 2, 1, 18),
    _AcdRegulatorStatsYellowHCOctets_Type()
)
acdRegulatorStatsYellowHCOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdRegulatorStatsYellowHCOctets.setStatus("current")
if mibBuilder.loadTexts:
    acdRegulatorStatsYellowHCOctets.setUnits("Octets")
_AcdRegulatorStatsYellowHCPkts_Type = Counter64
_AcdRegulatorStatsYellowHCPkts_Object = MibTableColumn
acdRegulatorStatsYellowHCPkts = _AcdRegulatorStatsYellowHCPkts_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 6, 2, 1, 19),
    _AcdRegulatorStatsYellowHCPkts_Type()
)
acdRegulatorStatsYellowHCPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdRegulatorStatsYellowHCPkts.setStatus("current")
if mibBuilder.loadTexts:
    acdRegulatorStatsYellowHCPkts.setUnits("Packets")
_AcdRegulatorStatsRedHCOctets_Type = Counter64
_AcdRegulatorStatsRedHCOctets_Object = MibTableColumn
acdRegulatorStatsRedHCOctets = _AcdRegulatorStatsRedHCOctets_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 6, 2, 1, 20),
    _AcdRegulatorStatsRedHCOctets_Type()
)
acdRegulatorStatsRedHCOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdRegulatorStatsRedHCOctets.setStatus("current")
if mibBuilder.loadTexts:
    acdRegulatorStatsRedHCOctets.setUnits("Octets")
_AcdRegulatorStatsRedHCPkts_Type = Counter64
_AcdRegulatorStatsRedHCPkts_Object = MibTableColumn
acdRegulatorStatsRedHCPkts = _AcdRegulatorStatsRedHCPkts_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 6, 2, 1, 21),
    _AcdRegulatorStatsRedHCPkts_Type()
)
acdRegulatorStatsRedHCPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdRegulatorStatsRedHCPkts.setStatus("current")
if mibBuilder.loadTexts:
    acdRegulatorStatsRedHCPkts.setUnits("Packets")
_AcdRegulatorStatsGreenRate_Type = Gauge32
_AcdRegulatorStatsGreenRate_Object = MibTableColumn
acdRegulatorStatsGreenRate = _AcdRegulatorStatsGreenRate_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 6, 2, 1, 22),
    _AcdRegulatorStatsGreenRate_Type()
)
acdRegulatorStatsGreenRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdRegulatorStatsGreenRate.setStatus("current")
if mibBuilder.loadTexts:
    acdRegulatorStatsGreenRate.setUnits("Kbps")
_AcdRegulatorStatsYellowRate_Type = Gauge32
_AcdRegulatorStatsYellowRate_Object = MibTableColumn
acdRegulatorStatsYellowRate = _AcdRegulatorStatsYellowRate_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 6, 2, 1, 23),
    _AcdRegulatorStatsYellowRate_Type()
)
acdRegulatorStatsYellowRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdRegulatorStatsYellowRate.setStatus("current")
if mibBuilder.loadTexts:
    acdRegulatorStatsYellowRate.setUnits("Kbps")
_AcdRegulatorStatsRedRate_Type = Gauge32
_AcdRegulatorStatsRedRate_Object = MibTableColumn
acdRegulatorStatsRedRate = _AcdRegulatorStatsRedRate_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 6, 2, 1, 24),
    _AcdRegulatorStatsRedRate_Type()
)
acdRegulatorStatsRedRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdRegulatorStatsRedRate.setStatus("current")
if mibBuilder.loadTexts:
    acdRegulatorStatsRedRate.setUnits("Kbps")
_AcdRegulatorHistStatsTable_Object = MibTable
acdRegulatorHistStatsTable = _AcdRegulatorHistStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 6, 3)
)
if mibBuilder.loadTexts:
    acdRegulatorHistStatsTable.setStatus("current")
_AcdRegulatorHistStatsEntry_Object = MibTableRow
acdRegulatorHistStatsEntry = _AcdRegulatorHistStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 6, 3, 1)
)
acdRegulatorHistStatsEntry.setIndexNames(
    (0, "ACD-REGULATOR-MIB", "acdRegulatorHistStatsID"),
    (0, "ACD-REGULATOR-MIB", "acdRegulatorHistStatsSampleIndex"),
)
if mibBuilder.loadTexts:
    acdRegulatorHistStatsEntry.setStatus("current")
_AcdRegulatorHistStatsID_Type = Unsigned32
_AcdRegulatorHistStatsID_Object = MibTableColumn
acdRegulatorHistStatsID = _AcdRegulatorHistStatsID_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 6, 3, 1, 1),
    _AcdRegulatorHistStatsID_Type()
)
acdRegulatorHistStatsID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdRegulatorHistStatsID.setStatus("current")
_AcdRegulatorHistStatsSampleIndex_Type = Unsigned32
_AcdRegulatorHistStatsSampleIndex_Object = MibTableColumn
acdRegulatorHistStatsSampleIndex = _AcdRegulatorHistStatsSampleIndex_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 6, 3, 1, 2),
    _AcdRegulatorHistStatsSampleIndex_Type()
)
acdRegulatorHistStatsSampleIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdRegulatorHistStatsSampleIndex.setStatus("current")


class _AcdRegulatorHistStatsStatus_Type(Integer32):
    """Custom type acdRegulatorHistStatsStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("valid", 1),
          ("invalid", 2))
    )


_AcdRegulatorHistStatsStatus_Type.__name__ = "Integer32"
_AcdRegulatorHistStatsStatus_Object = MibTableColumn
acdRegulatorHistStatsStatus = _AcdRegulatorHistStatsStatus_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 6, 3, 1, 3),
    _AcdRegulatorHistStatsStatus_Type()
)
acdRegulatorHistStatsStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdRegulatorHistStatsStatus.setStatus("current")
_AcdRegulatorHistStatsDuration_Type = Unsigned32
_AcdRegulatorHistStatsDuration_Object = MibTableColumn
acdRegulatorHistStatsDuration = _AcdRegulatorHistStatsDuration_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 6, 3, 1, 4),
    _AcdRegulatorHistStatsDuration_Type()
)
acdRegulatorHistStatsDuration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdRegulatorHistStatsDuration.setStatus("current")
_AcdRegulatorHistStatsIntervalEnd_Type = DateAndTime
_AcdRegulatorHistStatsIntervalEnd_Object = MibTableColumn
acdRegulatorHistStatsIntervalEnd = _AcdRegulatorHistStatsIntervalEnd_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 6, 3, 1, 5),
    _AcdRegulatorHistStatsIntervalEnd_Type()
)
acdRegulatorHistStatsIntervalEnd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdRegulatorHistStatsIntervalEnd.setStatus("current")
_AcdRegulatorHistStatsAcceptOctets_Type = Counter32
_AcdRegulatorHistStatsAcceptOctets_Object = MibTableColumn
acdRegulatorHistStatsAcceptOctets = _AcdRegulatorHistStatsAcceptOctets_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 6, 3, 1, 6),
    _AcdRegulatorHistStatsAcceptOctets_Type()
)
acdRegulatorHistStatsAcceptOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdRegulatorHistStatsAcceptOctets.setStatus("current")
if mibBuilder.loadTexts:
    acdRegulatorHistStatsAcceptOctets.setUnits("Octets")
_AcdRegulatorHistStatsAcceptOverflowOctets_Type = Counter32
_AcdRegulatorHistStatsAcceptOverflowOctets_Object = MibTableColumn
acdRegulatorHistStatsAcceptOverflowOctets = _AcdRegulatorHistStatsAcceptOverflowOctets_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 6, 3, 1, 7),
    _AcdRegulatorHistStatsAcceptOverflowOctets_Type()
)
acdRegulatorHistStatsAcceptOverflowOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdRegulatorHistStatsAcceptOverflowOctets.setStatus("current")
_AcdRegulatorHistStatsAcceptHCOctets_Type = Counter64
_AcdRegulatorHistStatsAcceptHCOctets_Object = MibTableColumn
acdRegulatorHistStatsAcceptHCOctets = _AcdRegulatorHistStatsAcceptHCOctets_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 6, 3, 1, 8),
    _AcdRegulatorHistStatsAcceptHCOctets_Type()
)
acdRegulatorHistStatsAcceptHCOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdRegulatorHistStatsAcceptHCOctets.setStatus("current")
if mibBuilder.loadTexts:
    acdRegulatorHistStatsAcceptHCOctets.setUnits("Octets")
_AcdRegulatorHistStatsAcceptPkts_Type = Counter32
_AcdRegulatorHistStatsAcceptPkts_Object = MibTableColumn
acdRegulatorHistStatsAcceptPkts = _AcdRegulatorHistStatsAcceptPkts_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 6, 3, 1, 9),
    _AcdRegulatorHistStatsAcceptPkts_Type()
)
acdRegulatorHistStatsAcceptPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdRegulatorHistStatsAcceptPkts.setStatus("current")
if mibBuilder.loadTexts:
    acdRegulatorHistStatsAcceptPkts.setUnits("Packets")
_AcdRegulatorHistStatsAcceptOverflowPkts_Type = Counter32
_AcdRegulatorHistStatsAcceptOverflowPkts_Object = MibTableColumn
acdRegulatorHistStatsAcceptOverflowPkts = _AcdRegulatorHistStatsAcceptOverflowPkts_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 6, 3, 1, 10),
    _AcdRegulatorHistStatsAcceptOverflowPkts_Type()
)
acdRegulatorHistStatsAcceptOverflowPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdRegulatorHistStatsAcceptOverflowPkts.setStatus("current")
_AcdRegulatorHistStatsAcceptHCPkts_Type = Counter64
_AcdRegulatorHistStatsAcceptHCPkts_Object = MibTableColumn
acdRegulatorHistStatsAcceptHCPkts = _AcdRegulatorHistStatsAcceptHCPkts_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 6, 3, 1, 11),
    _AcdRegulatorHistStatsAcceptHCPkts_Type()
)
acdRegulatorHistStatsAcceptHCPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdRegulatorHistStatsAcceptHCPkts.setStatus("current")
if mibBuilder.loadTexts:
    acdRegulatorHistStatsAcceptHCPkts.setUnits("Packets")
_AcdRegulatorHistStatsAcceptAvgRate_Type = Gauge32
_AcdRegulatorHistStatsAcceptAvgRate_Object = MibTableColumn
acdRegulatorHistStatsAcceptAvgRate = _AcdRegulatorHistStatsAcceptAvgRate_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 6, 3, 1, 12),
    _AcdRegulatorHistStatsAcceptAvgRate_Type()
)
acdRegulatorHistStatsAcceptAvgRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdRegulatorHistStatsAcceptAvgRate.setStatus("current")
if mibBuilder.loadTexts:
    acdRegulatorHistStatsAcceptAvgRate.setUnits("Kbps")
_AcdRegulatorHistStatsAcceptMinRate_Type = Gauge32
_AcdRegulatorHistStatsAcceptMinRate_Object = MibTableColumn
acdRegulatorHistStatsAcceptMinRate = _AcdRegulatorHistStatsAcceptMinRate_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 6, 3, 1, 13),
    _AcdRegulatorHistStatsAcceptMinRate_Type()
)
acdRegulatorHistStatsAcceptMinRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdRegulatorHistStatsAcceptMinRate.setStatus("current")
if mibBuilder.loadTexts:
    acdRegulatorHistStatsAcceptMinRate.setUnits("Kbps")
_AcdRegulatorHistStatsAcceptMaxRate_Type = Gauge32
_AcdRegulatorHistStatsAcceptMaxRate_Object = MibTableColumn
acdRegulatorHistStatsAcceptMaxRate = _AcdRegulatorHistStatsAcceptMaxRate_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 6, 3, 1, 14),
    _AcdRegulatorHistStatsAcceptMaxRate_Type()
)
acdRegulatorHistStatsAcceptMaxRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdRegulatorHistStatsAcceptMaxRate.setStatus("current")
if mibBuilder.loadTexts:
    acdRegulatorHistStatsAcceptMaxRate.setUnits("Kbps")
_AcdRegulatorHistStatsDropOctets_Type = Counter32
_AcdRegulatorHistStatsDropOctets_Object = MibTableColumn
acdRegulatorHistStatsDropOctets = _AcdRegulatorHistStatsDropOctets_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 6, 3, 1, 15),
    _AcdRegulatorHistStatsDropOctets_Type()
)
acdRegulatorHistStatsDropOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdRegulatorHistStatsDropOctets.setStatus("current")
if mibBuilder.loadTexts:
    acdRegulatorHistStatsDropOctets.setUnits("Octets")
_AcdRegulatorHistStatsDropOverflowOctets_Type = Counter32
_AcdRegulatorHistStatsDropOverflowOctets_Object = MibTableColumn
acdRegulatorHistStatsDropOverflowOctets = _AcdRegulatorHistStatsDropOverflowOctets_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 6, 3, 1, 16),
    _AcdRegulatorHistStatsDropOverflowOctets_Type()
)
acdRegulatorHistStatsDropOverflowOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdRegulatorHistStatsDropOverflowOctets.setStatus("current")
_AcdRegulatorHistStatsDropHCOctets_Type = Counter64
_AcdRegulatorHistStatsDropHCOctets_Object = MibTableColumn
acdRegulatorHistStatsDropHCOctets = _AcdRegulatorHistStatsDropHCOctets_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 6, 3, 1, 17),
    _AcdRegulatorHistStatsDropHCOctets_Type()
)
acdRegulatorHistStatsDropHCOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdRegulatorHistStatsDropHCOctets.setStatus("current")
if mibBuilder.loadTexts:
    acdRegulatorHistStatsDropHCOctets.setUnits("Octets")
_AcdRegulatorHistStatsDropPkts_Type = Counter32
_AcdRegulatorHistStatsDropPkts_Object = MibTableColumn
acdRegulatorHistStatsDropPkts = _AcdRegulatorHistStatsDropPkts_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 6, 3, 1, 18),
    _AcdRegulatorHistStatsDropPkts_Type()
)
acdRegulatorHistStatsDropPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdRegulatorHistStatsDropPkts.setStatus("current")
if mibBuilder.loadTexts:
    acdRegulatorHistStatsDropPkts.setUnits("Packets")
_AcdRegulatorHistStatsDropOverflowPkts_Type = Counter32
_AcdRegulatorHistStatsDropOverflowPkts_Object = MibTableColumn
acdRegulatorHistStatsDropOverflowPkts = _AcdRegulatorHistStatsDropOverflowPkts_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 6, 3, 1, 19),
    _AcdRegulatorHistStatsDropOverflowPkts_Type()
)
acdRegulatorHistStatsDropOverflowPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdRegulatorHistStatsDropOverflowPkts.setStatus("current")
_AcdRegulatorHistStatsDropHCPkts_Type = Counter64
_AcdRegulatorHistStatsDropHCPkts_Object = MibTableColumn
acdRegulatorHistStatsDropHCPkts = _AcdRegulatorHistStatsDropHCPkts_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 6, 3, 1, 20),
    _AcdRegulatorHistStatsDropHCPkts_Type()
)
acdRegulatorHistStatsDropHCPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdRegulatorHistStatsDropHCPkts.setStatus("current")
if mibBuilder.loadTexts:
    acdRegulatorHistStatsDropHCPkts.setUnits("Packets")
_AcdRegulatorHistStatsDropAvgRate_Type = Gauge32
_AcdRegulatorHistStatsDropAvgRate_Object = MibTableColumn
acdRegulatorHistStatsDropAvgRate = _AcdRegulatorHistStatsDropAvgRate_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 6, 3, 1, 21),
    _AcdRegulatorHistStatsDropAvgRate_Type()
)
acdRegulatorHistStatsDropAvgRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdRegulatorHistStatsDropAvgRate.setStatus("current")
if mibBuilder.loadTexts:
    acdRegulatorHistStatsDropAvgRate.setUnits("Kbps")
_AcdRegulatorHistStatsDropMinRate_Type = Gauge32
_AcdRegulatorHistStatsDropMinRate_Object = MibTableColumn
acdRegulatorHistStatsDropMinRate = _AcdRegulatorHistStatsDropMinRate_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 6, 3, 1, 22),
    _AcdRegulatorHistStatsDropMinRate_Type()
)
acdRegulatorHistStatsDropMinRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdRegulatorHistStatsDropMinRate.setStatus("current")
if mibBuilder.loadTexts:
    acdRegulatorHistStatsDropMinRate.setUnits("Kbps")
_AcdRegulatorHistStatsDropMaxRate_Type = Gauge32
_AcdRegulatorHistStatsDropMaxRate_Object = MibTableColumn
acdRegulatorHistStatsDropMaxRate = _AcdRegulatorHistStatsDropMaxRate_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 6, 3, 1, 23),
    _AcdRegulatorHistStatsDropMaxRate_Type()
)
acdRegulatorHistStatsDropMaxRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdRegulatorHistStatsDropMaxRate.setStatus("current")
if mibBuilder.loadTexts:
    acdRegulatorHistStatsDropMaxRate.setUnits("Kbps")
_AcdRegulatorHistStatsGreenHCOctets_Type = Counter64
_AcdRegulatorHistStatsGreenHCOctets_Object = MibTableColumn
acdRegulatorHistStatsGreenHCOctets = _AcdRegulatorHistStatsGreenHCOctets_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 6, 3, 1, 24),
    _AcdRegulatorHistStatsGreenHCOctets_Type()
)
acdRegulatorHistStatsGreenHCOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdRegulatorHistStatsGreenHCOctets.setStatus("current")
if mibBuilder.loadTexts:
    acdRegulatorHistStatsGreenHCOctets.setUnits("Octets")
_AcdRegulatorHistStatsGreenHCPkts_Type = Counter64
_AcdRegulatorHistStatsGreenHCPkts_Object = MibTableColumn
acdRegulatorHistStatsGreenHCPkts = _AcdRegulatorHistStatsGreenHCPkts_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 6, 3, 1, 25),
    _AcdRegulatorHistStatsGreenHCPkts_Type()
)
acdRegulatorHistStatsGreenHCPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdRegulatorHistStatsGreenHCPkts.setStatus("current")
if mibBuilder.loadTexts:
    acdRegulatorHistStatsGreenHCPkts.setUnits("Packets")
_AcdRegulatorHistStatsYellowHCOctets_Type = Counter64
_AcdRegulatorHistStatsYellowHCOctets_Object = MibTableColumn
acdRegulatorHistStatsYellowHCOctets = _AcdRegulatorHistStatsYellowHCOctets_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 6, 3, 1, 26),
    _AcdRegulatorHistStatsYellowHCOctets_Type()
)
acdRegulatorHistStatsYellowHCOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdRegulatorHistStatsYellowHCOctets.setStatus("current")
if mibBuilder.loadTexts:
    acdRegulatorHistStatsYellowHCOctets.setUnits("Octets")
_AcdRegulatorHistStatsYellowHCPkts_Type = Counter64
_AcdRegulatorHistStatsYellowHCPkts_Object = MibTableColumn
acdRegulatorHistStatsYellowHCPkts = _AcdRegulatorHistStatsYellowHCPkts_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 6, 3, 1, 27),
    _AcdRegulatorHistStatsYellowHCPkts_Type()
)
acdRegulatorHistStatsYellowHCPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdRegulatorHistStatsYellowHCPkts.setStatus("current")
if mibBuilder.loadTexts:
    acdRegulatorHistStatsYellowHCPkts.setUnits("Packets")
_AcdRegulatorHistStatsRedHCOctets_Type = Counter64
_AcdRegulatorHistStatsRedHCOctets_Object = MibTableColumn
acdRegulatorHistStatsRedHCOctets = _AcdRegulatorHistStatsRedHCOctets_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 6, 3, 1, 28),
    _AcdRegulatorHistStatsRedHCOctets_Type()
)
acdRegulatorHistStatsRedHCOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdRegulatorHistStatsRedHCOctets.setStatus("current")
if mibBuilder.loadTexts:
    acdRegulatorHistStatsRedHCOctets.setUnits("Octets")
_AcdRegulatorHistStatsRedHCPkts_Type = Counter64
_AcdRegulatorHistStatsRedHCPkts_Object = MibTableColumn
acdRegulatorHistStatsRedHCPkts = _AcdRegulatorHistStatsRedHCPkts_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 6, 3, 1, 29),
    _AcdRegulatorHistStatsRedHCPkts_Type()
)
acdRegulatorHistStatsRedHCPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdRegulatorHistStatsRedHCPkts.setStatus("current")
if mibBuilder.loadTexts:
    acdRegulatorHistStatsRedHCPkts.setUnits("Packets")
_AcdRegulatorHistStatsGreenAvgRate_Type = Gauge32
_AcdRegulatorHistStatsGreenAvgRate_Object = MibTableColumn
acdRegulatorHistStatsGreenAvgRate = _AcdRegulatorHistStatsGreenAvgRate_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 6, 3, 1, 30),
    _AcdRegulatorHistStatsGreenAvgRate_Type()
)
acdRegulatorHistStatsGreenAvgRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdRegulatorHistStatsGreenAvgRate.setStatus("current")
if mibBuilder.loadTexts:
    acdRegulatorHistStatsGreenAvgRate.setUnits("Kbps")
_AcdRegulatorHistStatsGreenMinRate_Type = Gauge32
_AcdRegulatorHistStatsGreenMinRate_Object = MibTableColumn
acdRegulatorHistStatsGreenMinRate = _AcdRegulatorHistStatsGreenMinRate_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 6, 3, 1, 31),
    _AcdRegulatorHistStatsGreenMinRate_Type()
)
acdRegulatorHistStatsGreenMinRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdRegulatorHistStatsGreenMinRate.setStatus("current")
if mibBuilder.loadTexts:
    acdRegulatorHistStatsGreenMinRate.setUnits("Kbps")
_AcdRegulatorHistStatsGreenMaxRate_Type = Gauge32
_AcdRegulatorHistStatsGreenMaxRate_Object = MibTableColumn
acdRegulatorHistStatsGreenMaxRate = _AcdRegulatorHistStatsGreenMaxRate_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 6, 3, 1, 32),
    _AcdRegulatorHistStatsGreenMaxRate_Type()
)
acdRegulatorHistStatsGreenMaxRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdRegulatorHistStatsGreenMaxRate.setStatus("current")
if mibBuilder.loadTexts:
    acdRegulatorHistStatsGreenMaxRate.setUnits("Kbps")
_AcdRegulatorHistStatsYellowAvgRate_Type = Gauge32
_AcdRegulatorHistStatsYellowAvgRate_Object = MibTableColumn
acdRegulatorHistStatsYellowAvgRate = _AcdRegulatorHistStatsYellowAvgRate_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 6, 3, 1, 33),
    _AcdRegulatorHistStatsYellowAvgRate_Type()
)
acdRegulatorHistStatsYellowAvgRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdRegulatorHistStatsYellowAvgRate.setStatus("current")
if mibBuilder.loadTexts:
    acdRegulatorHistStatsYellowAvgRate.setUnits("Kbps")
_AcdRegulatorHistStatsYellowMinRate_Type = Gauge32
_AcdRegulatorHistStatsYellowMinRate_Object = MibTableColumn
acdRegulatorHistStatsYellowMinRate = _AcdRegulatorHistStatsYellowMinRate_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 6, 3, 1, 34),
    _AcdRegulatorHistStatsYellowMinRate_Type()
)
acdRegulatorHistStatsYellowMinRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdRegulatorHistStatsYellowMinRate.setStatus("current")
if mibBuilder.loadTexts:
    acdRegulatorHistStatsYellowMinRate.setUnits("Kbps")
_AcdRegulatorHistStatsYellowMaxRate_Type = Gauge32
_AcdRegulatorHistStatsYellowMaxRate_Object = MibTableColumn
acdRegulatorHistStatsYellowMaxRate = _AcdRegulatorHistStatsYellowMaxRate_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 6, 3, 1, 35),
    _AcdRegulatorHistStatsYellowMaxRate_Type()
)
acdRegulatorHistStatsYellowMaxRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdRegulatorHistStatsYellowMaxRate.setStatus("current")
if mibBuilder.loadTexts:
    acdRegulatorHistStatsYellowMaxRate.setUnits("Kbps")
_AcdRegulatorHistStatsRedAvgRate_Type = Gauge32
_AcdRegulatorHistStatsRedAvgRate_Object = MibTableColumn
acdRegulatorHistStatsRedAvgRate = _AcdRegulatorHistStatsRedAvgRate_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 6, 3, 1, 36),
    _AcdRegulatorHistStatsRedAvgRate_Type()
)
acdRegulatorHistStatsRedAvgRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdRegulatorHistStatsRedAvgRate.setStatus("current")
if mibBuilder.loadTexts:
    acdRegulatorHistStatsRedAvgRate.setUnits("Kbps")
_AcdRegulatorHistStatsRedMinRate_Type = Gauge32
_AcdRegulatorHistStatsRedMinRate_Object = MibTableColumn
acdRegulatorHistStatsRedMinRate = _AcdRegulatorHistStatsRedMinRate_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 6, 3, 1, 37),
    _AcdRegulatorHistStatsRedMinRate_Type()
)
acdRegulatorHistStatsRedMinRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdRegulatorHistStatsRedMinRate.setStatus("current")
if mibBuilder.loadTexts:
    acdRegulatorHistStatsRedMinRate.setUnits("Kbps")
_AcdRegulatorHistStatsRedMaxRate_Type = Gauge32
_AcdRegulatorHistStatsRedMaxRate_Object = MibTableColumn
acdRegulatorHistStatsRedMaxRate = _AcdRegulatorHistStatsRedMaxRate_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 6, 3, 1, 38),
    _AcdRegulatorHistStatsRedMaxRate_Type()
)
acdRegulatorHistStatsRedMaxRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdRegulatorHistStatsRedMaxRate.setStatus("current")
if mibBuilder.loadTexts:
    acdRegulatorHistStatsRedMaxRate.setUnits("Kbps")
_AcdRegulatorNotifications_ObjectIdentity = ObjectIdentity
acdRegulatorNotifications = _AcdRegulatorNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22420, 2, 6, 4)
)
_AcdRegulatorMIBObjects_ObjectIdentity = ObjectIdentity
acdRegulatorMIBObjects = _AcdRegulatorMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22420, 2, 6, 5)
)
_AcdRegulatorTableTid_ObjectIdentity = ObjectIdentity
acdRegulatorTableTid = _AcdRegulatorTableTid_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22420, 2, 6, 5, 1)
)
_AcdRegulatorTableLastChangeTid_Type = Unsigned32
_AcdRegulatorTableLastChangeTid_Object = MibScalar
acdRegulatorTableLastChangeTid = _AcdRegulatorTableLastChangeTid_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 6, 5, 1, 1),
    _AcdRegulatorTableLastChangeTid_Type()
)
acdRegulatorTableLastChangeTid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdRegulatorTableLastChangeTid.setStatus("current")
_AcdRegulatorConformance_ObjectIdentity = ObjectIdentity
acdRegulatorConformance = _AcdRegulatorConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22420, 2, 6, 6)
)
_AcdRegulatorCompliances_ObjectIdentity = ObjectIdentity
acdRegulatorCompliances = _AcdRegulatorCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22420, 2, 6, 6, 1)
)
_AcdRegulatorGroups_ObjectIdentity = ObjectIdentity
acdRegulatorGroups = _AcdRegulatorGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22420, 2, 6, 6, 2)
)

# Managed Objects groups

acdRegulatorGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 22420, 2, 6, 6, 2, 1)
)
acdRegulatorGroup.setObjects(
      *(("ACD-REGULATOR-MIB", "acdRegulatorName"),
        ("ACD-REGULATOR-MIB", "acdRegulatorCir"),
        ("ACD-REGULATOR-MIB", "acdRegulatorCbs"),
        ("ACD-REGULATOR-MIB", "acdRegulatorEir"),
        ("ACD-REGULATOR-MIB", "acdRegulatorEbs"),
        ("ACD-REGULATOR-MIB", "acdRegulatorIsBlind"),
        ("ACD-REGULATOR-MIB", "acdRegulatorIsCouple"),
        ("ACD-REGULATOR-MIB", "acdRegulatorRowStatus"),
        ("ACD-REGULATOR-MIB", "acdRegulatorWorkingRate"),
        ("ACD-REGULATOR-MIB", "acdRegulatorCirMax"),
        ("ACD-REGULATOR-MIB", "acdRegulatorEirMax"))
)
if mibBuilder.loadTexts:
    acdRegulatorGroup.setStatus("current")

acdRegulatorStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 22420, 2, 6, 6, 2, 2)
)
acdRegulatorStatsGroup.setObjects(
      *(("ACD-REGULATOR-MIB", "acdRegulatorStatsAcceptOctets"),
        ("ACD-REGULATOR-MIB", "acdRegulatorStatsAcceptOverflowOctets"),
        ("ACD-REGULATOR-MIB", "acdRegulatorStatsAcceptHCOctets"),
        ("ACD-REGULATOR-MIB", "acdRegulatorStatsAcceptPkts"),
        ("ACD-REGULATOR-MIB", "acdRegulatorStatsAcceptOverflowPkts"),
        ("ACD-REGULATOR-MIB", "acdRegulatorStatsAcceptHCPkts"),
        ("ACD-REGULATOR-MIB", "acdRegulatorStatsAcceptRate"),
        ("ACD-REGULATOR-MIB", "acdRegulatorStatsDropOctets"),
        ("ACD-REGULATOR-MIB", "acdRegulatorStatsDropOverflowOctets"),
        ("ACD-REGULATOR-MIB", "acdRegulatorStatsDropHCOctets"),
        ("ACD-REGULATOR-MIB", "acdRegulatorStatsDropPkts"),
        ("ACD-REGULATOR-MIB", "acdRegulatorStatsDropOverflowPkts"),
        ("ACD-REGULATOR-MIB", "acdRegulatorStatsDropHCPkts"),
        ("ACD-REGULATOR-MIB", "acdRegulatorStatsDropRate"),
        ("ACD-REGULATOR-MIB", "acdRegulatorStatsGreenHCOctets"),
        ("ACD-REGULATOR-MIB", "acdRegulatorStatsGreenHCPkts"),
        ("ACD-REGULATOR-MIB", "acdRegulatorStatsYellowHCOctets"),
        ("ACD-REGULATOR-MIB", "acdRegulatorStatsYellowHCPkts"),
        ("ACD-REGULATOR-MIB", "acdRegulatorStatsRedHCOctets"),
        ("ACD-REGULATOR-MIB", "acdRegulatorStatsRedHCPkts"),
        ("ACD-REGULATOR-MIB", "acdRegulatorStatsGreenRate"),
        ("ACD-REGULATOR-MIB", "acdRegulatorStatsYellowRate"),
        ("ACD-REGULATOR-MIB", "acdRegulatorStatsRedRate"))
)
if mibBuilder.loadTexts:
    acdRegulatorStatsGroup.setStatus("current")

acdRegulatorHistStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 22420, 2, 6, 6, 2, 3)
)
acdRegulatorHistStatsGroup.setObjects(
      *(("ACD-REGULATOR-MIB", "acdRegulatorHistStatsID"),
        ("ACD-REGULATOR-MIB", "acdRegulatorHistStatsSampleIndex"),
        ("ACD-REGULATOR-MIB", "acdRegulatorHistStatsStatus"),
        ("ACD-REGULATOR-MIB", "acdRegulatorHistStatsDuration"),
        ("ACD-REGULATOR-MIB", "acdRegulatorHistStatsIntervalEnd"),
        ("ACD-REGULATOR-MIB", "acdRegulatorHistStatsAcceptOctets"),
        ("ACD-REGULATOR-MIB", "acdRegulatorHistStatsAcceptOverflowOctets"),
        ("ACD-REGULATOR-MIB", "acdRegulatorHistStatsAcceptHCOctets"),
        ("ACD-REGULATOR-MIB", "acdRegulatorHistStatsAcceptPkts"),
        ("ACD-REGULATOR-MIB", "acdRegulatorHistStatsAcceptOverflowPkts"),
        ("ACD-REGULATOR-MIB", "acdRegulatorHistStatsAcceptHCPkts"),
        ("ACD-REGULATOR-MIB", "acdRegulatorHistStatsAcceptAvgRate"),
        ("ACD-REGULATOR-MIB", "acdRegulatorHistStatsAcceptMinRate"),
        ("ACD-REGULATOR-MIB", "acdRegulatorHistStatsAcceptMaxRate"),
        ("ACD-REGULATOR-MIB", "acdRegulatorHistStatsDropOctets"),
        ("ACD-REGULATOR-MIB", "acdRegulatorHistStatsDropOverflowOctets"),
        ("ACD-REGULATOR-MIB", "acdRegulatorHistStatsDropHCOctets"),
        ("ACD-REGULATOR-MIB", "acdRegulatorHistStatsDropPkts"),
        ("ACD-REGULATOR-MIB", "acdRegulatorHistStatsDropOverflowPkts"),
        ("ACD-REGULATOR-MIB", "acdRegulatorHistStatsDropHCPkts"),
        ("ACD-REGULATOR-MIB", "acdRegulatorHistStatsDropAvgRate"),
        ("ACD-REGULATOR-MIB", "acdRegulatorHistStatsDropMinRate"),
        ("ACD-REGULATOR-MIB", "acdRegulatorHistStatsDropMaxRate"),
        ("ACD-REGULATOR-MIB", "acdRegulatorHistStatsGreenHCOctets"),
        ("ACD-REGULATOR-MIB", "acdRegulatorHistStatsGreenHCPkts"),
        ("ACD-REGULATOR-MIB", "acdRegulatorHistStatsYellowHCOctets"),
        ("ACD-REGULATOR-MIB", "acdRegulatorHistStatsYellowHCPkts"),
        ("ACD-REGULATOR-MIB", "acdRegulatorHistStatsRedHCOctets"),
        ("ACD-REGULATOR-MIB", "acdRegulatorHistStatsRedHCPkts"),
        ("ACD-REGULATOR-MIB", "acdRegulatorHistStatsGreenAvgRate"),
        ("ACD-REGULATOR-MIB", "acdRegulatorHistStatsGreenMinRate"),
        ("ACD-REGULATOR-MIB", "acdRegulatorHistStatsGreenMaxRate"),
        ("ACD-REGULATOR-MIB", "acdRegulatorHistStatsYellowAvgRate"),
        ("ACD-REGULATOR-MIB", "acdRegulatorHistStatsYellowMinRate"),
        ("ACD-REGULATOR-MIB", "acdRegulatorHistStatsYellowMaxRate"),
        ("ACD-REGULATOR-MIB", "acdRegulatorHistStatsRedAvgRate"),
        ("ACD-REGULATOR-MIB", "acdRegulatorHistStatsRedMinRate"),
        ("ACD-REGULATOR-MIB", "acdRegulatorHistStatsRedMaxRate"))
)
if mibBuilder.loadTexts:
    acdRegulatorHistStatsGroup.setStatus("current")

acdRegulatorTidGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 22420, 2, 6, 6, 2, 4)
)
acdRegulatorTidGroup.setObjects(
    ("ACD-REGULATOR-MIB", "acdRegulatorTableLastChangeTid")
)
if mibBuilder.loadTexts:
    acdRegulatorTidGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

acdRegulatorCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 22420, 2, 6, 6, 1, 1)
)
acdRegulatorCompliance.setObjects(
      *(("ACD-REGULATOR-MIB", "acdRegulatorGroup"),
        ("ACD-REGULATOR-MIB", "acdRegulatorStatsGroup"),
        ("ACD-REGULATOR-MIB", "acdRegulatorHistStatsGroup"),
        ("ACD-REGULATOR-MIB", "acdRegulatorTidGroup"))
)
if mibBuilder.loadTexts:
    acdRegulatorCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ACD-REGULATOR-MIB",
    **{"acdRegulator": acdRegulator,
       "acdRegulatorTable": acdRegulatorTable,
       "acdRegulatorEntry": acdRegulatorEntry,
       "acdRegulatorID": acdRegulatorID,
       "acdRegulatorName": acdRegulatorName,
       "acdRegulatorCir": acdRegulatorCir,
       "acdRegulatorCbs": acdRegulatorCbs,
       "acdRegulatorEir": acdRegulatorEir,
       "acdRegulatorEbs": acdRegulatorEbs,
       "acdRegulatorIsBlind": acdRegulatorIsBlind,
       "acdRegulatorIsCouple": acdRegulatorIsCouple,
       "acdRegulatorRowStatus": acdRegulatorRowStatus,
       "acdRegulatorWorkingRate": acdRegulatorWorkingRate,
       "acdRegulatorCirMax": acdRegulatorCirMax,
       "acdRegulatorEirMax": acdRegulatorEirMax,
       "acdRegulatorStatsTable": acdRegulatorStatsTable,
       "acdRegulatorStatsEntry": acdRegulatorStatsEntry,
       "acdRegulatorStatsID": acdRegulatorStatsID,
       "acdRegulatorStatsAcceptOctets": acdRegulatorStatsAcceptOctets,
       "acdRegulatorStatsAcceptOverflowOctets": acdRegulatorStatsAcceptOverflowOctets,
       "acdRegulatorStatsAcceptHCOctets": acdRegulatorStatsAcceptHCOctets,
       "acdRegulatorStatsAcceptPkts": acdRegulatorStatsAcceptPkts,
       "acdRegulatorStatsAcceptOverflowPkts": acdRegulatorStatsAcceptOverflowPkts,
       "acdRegulatorStatsAcceptHCPkts": acdRegulatorStatsAcceptHCPkts,
       "acdRegulatorStatsAcceptRate": acdRegulatorStatsAcceptRate,
       "acdRegulatorStatsDropOctets": acdRegulatorStatsDropOctets,
       "acdRegulatorStatsDropOverflowOctets": acdRegulatorStatsDropOverflowOctets,
       "acdRegulatorStatsDropHCOctets": acdRegulatorStatsDropHCOctets,
       "acdRegulatorStatsDropPkts": acdRegulatorStatsDropPkts,
       "acdRegulatorStatsDropOverflowPkts": acdRegulatorStatsDropOverflowPkts,
       "acdRegulatorStatsDropHCPkts": acdRegulatorStatsDropHCPkts,
       "acdRegulatorStatsDropRate": acdRegulatorStatsDropRate,
       "acdRegulatorStatsGreenHCOctets": acdRegulatorStatsGreenHCOctets,
       "acdRegulatorStatsGreenHCPkts": acdRegulatorStatsGreenHCPkts,
       "acdRegulatorStatsYellowHCOctets": acdRegulatorStatsYellowHCOctets,
       "acdRegulatorStatsYellowHCPkts": acdRegulatorStatsYellowHCPkts,
       "acdRegulatorStatsRedHCOctets": acdRegulatorStatsRedHCOctets,
       "acdRegulatorStatsRedHCPkts": acdRegulatorStatsRedHCPkts,
       "acdRegulatorStatsGreenRate": acdRegulatorStatsGreenRate,
       "acdRegulatorStatsYellowRate": acdRegulatorStatsYellowRate,
       "acdRegulatorStatsRedRate": acdRegulatorStatsRedRate,
       "acdRegulatorHistStatsTable": acdRegulatorHistStatsTable,
       "acdRegulatorHistStatsEntry": acdRegulatorHistStatsEntry,
       "acdRegulatorHistStatsID": acdRegulatorHistStatsID,
       "acdRegulatorHistStatsSampleIndex": acdRegulatorHistStatsSampleIndex,
       "acdRegulatorHistStatsStatus": acdRegulatorHistStatsStatus,
       "acdRegulatorHistStatsDuration": acdRegulatorHistStatsDuration,
       "acdRegulatorHistStatsIntervalEnd": acdRegulatorHistStatsIntervalEnd,
       "acdRegulatorHistStatsAcceptOctets": acdRegulatorHistStatsAcceptOctets,
       "acdRegulatorHistStatsAcceptOverflowOctets": acdRegulatorHistStatsAcceptOverflowOctets,
       "acdRegulatorHistStatsAcceptHCOctets": acdRegulatorHistStatsAcceptHCOctets,
       "acdRegulatorHistStatsAcceptPkts": acdRegulatorHistStatsAcceptPkts,
       "acdRegulatorHistStatsAcceptOverflowPkts": acdRegulatorHistStatsAcceptOverflowPkts,
       "acdRegulatorHistStatsAcceptHCPkts": acdRegulatorHistStatsAcceptHCPkts,
       "acdRegulatorHistStatsAcceptAvgRate": acdRegulatorHistStatsAcceptAvgRate,
       "acdRegulatorHistStatsAcceptMinRate": acdRegulatorHistStatsAcceptMinRate,
       "acdRegulatorHistStatsAcceptMaxRate": acdRegulatorHistStatsAcceptMaxRate,
       "acdRegulatorHistStatsDropOctets": acdRegulatorHistStatsDropOctets,
       "acdRegulatorHistStatsDropOverflowOctets": acdRegulatorHistStatsDropOverflowOctets,
       "acdRegulatorHistStatsDropHCOctets": acdRegulatorHistStatsDropHCOctets,
       "acdRegulatorHistStatsDropPkts": acdRegulatorHistStatsDropPkts,
       "acdRegulatorHistStatsDropOverflowPkts": acdRegulatorHistStatsDropOverflowPkts,
       "acdRegulatorHistStatsDropHCPkts": acdRegulatorHistStatsDropHCPkts,
       "acdRegulatorHistStatsDropAvgRate": acdRegulatorHistStatsDropAvgRate,
       "acdRegulatorHistStatsDropMinRate": acdRegulatorHistStatsDropMinRate,
       "acdRegulatorHistStatsDropMaxRate": acdRegulatorHistStatsDropMaxRate,
       "acdRegulatorHistStatsGreenHCOctets": acdRegulatorHistStatsGreenHCOctets,
       "acdRegulatorHistStatsGreenHCPkts": acdRegulatorHistStatsGreenHCPkts,
       "acdRegulatorHistStatsYellowHCOctets": acdRegulatorHistStatsYellowHCOctets,
       "acdRegulatorHistStatsYellowHCPkts": acdRegulatorHistStatsYellowHCPkts,
       "acdRegulatorHistStatsRedHCOctets": acdRegulatorHistStatsRedHCOctets,
       "acdRegulatorHistStatsRedHCPkts": acdRegulatorHistStatsRedHCPkts,
       "acdRegulatorHistStatsGreenAvgRate": acdRegulatorHistStatsGreenAvgRate,
       "acdRegulatorHistStatsGreenMinRate": acdRegulatorHistStatsGreenMinRate,
       "acdRegulatorHistStatsGreenMaxRate": acdRegulatorHistStatsGreenMaxRate,
       "acdRegulatorHistStatsYellowAvgRate": acdRegulatorHistStatsYellowAvgRate,
       "acdRegulatorHistStatsYellowMinRate": acdRegulatorHistStatsYellowMinRate,
       "acdRegulatorHistStatsYellowMaxRate": acdRegulatorHistStatsYellowMaxRate,
       "acdRegulatorHistStatsRedAvgRate": acdRegulatorHistStatsRedAvgRate,
       "acdRegulatorHistStatsRedMinRate": acdRegulatorHistStatsRedMinRate,
       "acdRegulatorHistStatsRedMaxRate": acdRegulatorHistStatsRedMaxRate,
       "acdRegulatorNotifications": acdRegulatorNotifications,
       "acdRegulatorMIBObjects": acdRegulatorMIBObjects,
       "acdRegulatorTableTid": acdRegulatorTableTid,
       "acdRegulatorTableLastChangeTid": acdRegulatorTableLastChangeTid,
       "acdRegulatorConformance": acdRegulatorConformance,
       "acdRegulatorCompliances": acdRegulatorCompliances,
       "acdRegulatorCompliance": acdRegulatorCompliance,
       "acdRegulatorGroups": acdRegulatorGroups,
       "acdRegulatorGroup": acdRegulatorGroup,
       "acdRegulatorStatsGroup": acdRegulatorStatsGroup,
       "acdRegulatorHistStatsGroup": acdRegulatorHistStatsGroup,
       "acdRegulatorTidGroup": acdRegulatorTidGroup}
)
