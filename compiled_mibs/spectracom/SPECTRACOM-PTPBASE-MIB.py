# SNMP MIB module (SPECTRACOM-PTPBASE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\spectracom\SPECTRACOM-PTPBASE-MIB

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

(InterfaceIndexOrZero,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndexOrZero")

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
 iso,
 mib_2) = mibBuilder.importSymbols(
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
    "iso",
    "mib-2")

(AutonomousType,
 DisplayString,
 PhysAddress,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "AutonomousType",
    "DisplayString",
    "PhysAddress",
    "TextualConvention",
    "TruthValue")

(specModules,
 specProducts) = mibBuilder.importSymbols(
    "SPECTRACOM-GLOBAL-REG-MIB",
    "specModules",
    "specProducts")


# MODULE-IDENTITY

ptpbaseMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 18837, 1, 1, 7)
)
if mibBuilder.loadTexts:
    ptpbaseMIB.setRevisions(
        ("2023-01-11 00:00",
         "2022-12-07 00:00",
         "2017-05-30 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class PtpClockDomainType(TextualConvention, Unsigned32):
    status = "current"
    displayHint = "d"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )



class PtpClockIdentity(TextualConvention, OctetString):
    status = "current"
    displayHint = "255a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )
    fixed_length = 8



class PtpClockInstanceType(TextualConvention, Unsigned32):
    status = "current"
    displayHint = "d"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )



class PtpClockIntervalBase2(TextualConvention, Integer32):
    status = "current"
    displayHint = "d"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-128, 127),
    )



class PtpClockMechanismType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              254)
        )
    )
    namedValues = NamedValues(
        *(("e2e", 1),
          ("p2p", 2),
          ("disabled", 254))
    )



class PtpClockPortNumber(TextualConvention, Unsigned32):
    status = "current"
    displayHint = "d"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )



class PtpClockPortState(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
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
        *(("initializing", 1),
          ("faulty", 2),
          ("disabled", 3),
          ("listening", 4),
          ("preMaster", 5),
          ("master", 6),
          ("passive", 7),
          ("uncalibrated", 8),
          ("slave", 9))
    )



class PtpClockPortTransportTypeAddress(TextualConvention, OctetString):
    status = "current"
    displayHint = "255a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )



class PtpClockProfileType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("default", 1),
          ("telecom", 2),
          ("vendorspecific", 3))
    )



class PtpClockQualityAccuracyType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(32,
              33,
              34,
              35,
              36,
              37,
              38,
              39,
              40,
              41,
              42,
              43,
              44,
              45,
              46,
              47,
              48,
              49,
              254)
        )
    )
    namedValues = NamedValues(
        *(("nanoSecond25", 32),
          ("nanoSecond100", 33),
          ("nanoSecond250", 34),
          ("microSec1", 35),
          ("microSec2dot5", 36),
          ("microSec10", 37),
          ("microSec25", 38),
          ("microSec100", 39),
          ("microSec250", 40),
          ("milliSec1", 41),
          ("milliSec2dot5", 42),
          ("milliSec10", 43),
          ("milliSec25", 44),
          ("milliSec100", 45),
          ("milliSec250", 46),
          ("second1", 47),
          ("second10", 48),
          ("secondGreater10", 49),
          ("unknown", 254))
    )



class PtpClockQualityClassType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(6,
              7,
              13,
              14,
              52,
              58)
        )
    )
    namedValues = NamedValues(
        *(("clockclass6", 6),
          ("clockclass7", 7),
          ("clockclass13", 13),
          ("clockclass14", 14),
          ("clockclass52", 52),
          ("clockclass58", 58))
    )



class PtpClockRoleType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("master", 1),
          ("slave", 2))
    )



class PtpClockStateType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("freerun", 1),
          ("holdover", 2),
          ("acquiring", 3),
          ("frequencyLocked", 4),
          ("phaseAligned", 5))
    )



class PtpClockTimeInterval(TextualConvention, OctetString):
    status = "current"
    displayHint = "255a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )



class PtpClockTimeSourceType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(16,
              32,
              48,
              64,
              80,
              96,
              144,
              160)
        )
    )
    namedValues = NamedValues(
        *(("atomicClock", 16),
          ("gps", 32),
          ("terrestrialRadio", 48),
          ("ptp", 64),
          ("ntp", 80),
          ("handSet", 96),
          ("other", 144),
          ("internalOscillator", 160))
    )



class PtpClockTxModeType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("unicast", 1),
          ("multicast", 2),
          ("multicastmix", 3))
    )



class PtpClockType(TextualConvention, Integer32):
    status = "current"
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
        *(("ordinaryClock", 1),
          ("boundaryClock", 2),
          ("transparentClock", 3),
          ("boundaryNode", 4))
    )



# MIB Managed Objects in the order of their OIDs

_PtpbaseSnmpObjs_ObjectIdentity = ObjectIdentity
ptpbaseSnmpObjs = _PtpbaseSnmpObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18837, 3, 5)
)
_PtpbaseMIBNotifs_ObjectIdentity = ObjectIdentity
ptpbaseMIBNotifs = _PtpbaseMIBNotifs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18837, 3, 5, 0)
)
_PtpbaseMIBObjects_ObjectIdentity = ObjectIdentity
ptpbaseMIBObjects = _PtpbaseMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18837, 3, 5, 1)
)
_PtpbaseMIBSystemInfo_ObjectIdentity = ObjectIdentity
ptpbaseMIBSystemInfo = _PtpbaseMIBSystemInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18837, 3, 5, 1, 1)
)
_PtpbaseSystemTable_Object = MibTable
ptpbaseSystemTable = _PtpbaseSystemTable_Object(
    (1, 3, 6, 1, 4, 1, 18837, 3, 5, 1, 1, 1)
)
if mibBuilder.loadTexts:
    ptpbaseSystemTable.setStatus("current")
_PtpbaseSystemEntry_Object = MibTableRow
ptpbaseSystemEntry = _PtpbaseSystemEntry_Object(
    (1, 3, 6, 1, 4, 1, 18837, 3, 5, 1, 1, 1, 1)
)
ptpbaseSystemEntry.setIndexNames(
    (0, "SPECTRACOM-PTPBASE-MIB", "ptpDomainIndex"),
    (0, "SPECTRACOM-PTPBASE-MIB", "ptpInstanceIndex"),
)
if mibBuilder.loadTexts:
    ptpbaseSystemEntry.setStatus("current")
_PtpDomainIndex_Type = PtpClockDomainType
_PtpDomainIndex_Object = MibTableColumn
ptpDomainIndex = _PtpDomainIndex_Object(
    (1, 3, 6, 1, 4, 1, 18837, 3, 5, 1, 1, 1, 1, 1),
    _PtpDomainIndex_Type()
)
ptpDomainIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ptpDomainIndex.setStatus("current")
_PtpInstanceIndex_Type = PtpClockInstanceType
_PtpInstanceIndex_Object = MibTableColumn
ptpInstanceIndex = _PtpInstanceIndex_Object(
    (1, 3, 6, 1, 4, 1, 18837, 3, 5, 1, 1, 1, 1, 2),
    _PtpInstanceIndex_Type()
)
ptpInstanceIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ptpInstanceIndex.setStatus("current")
_PtpDomainClockPortsTotal_Type = Gauge32
_PtpDomainClockPortsTotal_Object = MibTableColumn
ptpDomainClockPortsTotal = _PtpDomainClockPortsTotal_Object(
    (1, 3, 6, 1, 4, 1, 18837, 3, 5, 1, 1, 1, 1, 3),
    _PtpDomainClockPortsTotal_Type()
)
ptpDomainClockPortsTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ptpDomainClockPortsTotal.setStatus("current")
if mibBuilder.loadTexts:
    ptpDomainClockPortsTotal.setUnits("ptp ports")
_PtpbaseSystemDomainTable_Object = MibTable
ptpbaseSystemDomainTable = _PtpbaseSystemDomainTable_Object(
    (1, 3, 6, 1, 4, 1, 18837, 3, 5, 1, 1, 2)
)
if mibBuilder.loadTexts:
    ptpbaseSystemDomainTable.setStatus("current")
_PtpbaseSystemDomainEntry_Object = MibTableRow
ptpbaseSystemDomainEntry = _PtpbaseSystemDomainEntry_Object(
    (1, 3, 6, 1, 4, 1, 18837, 3, 5, 1, 1, 2, 1)
)
ptpbaseSystemDomainEntry.setIndexNames(
    (0, "SPECTRACOM-PTPBASE-MIB", "ptpbaseSystemDomainClockTypeIndex"),
)
if mibBuilder.loadTexts:
    ptpbaseSystemDomainEntry.setStatus("current")
_PtpbaseSystemDomainClockTypeIndex_Type = PtpClockType
_PtpbaseSystemDomainClockTypeIndex_Object = MibTableColumn
ptpbaseSystemDomainClockTypeIndex = _PtpbaseSystemDomainClockTypeIndex_Object(
    (1, 3, 6, 1, 4, 1, 18837, 3, 5, 1, 1, 2, 1, 1),
    _PtpbaseSystemDomainClockTypeIndex_Type()
)
ptpbaseSystemDomainClockTypeIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ptpbaseSystemDomainClockTypeIndex.setStatus("current")
_PtpbaseSystemDomainTotals_Type = Unsigned32
_PtpbaseSystemDomainTotals_Object = MibTableColumn
ptpbaseSystemDomainTotals = _PtpbaseSystemDomainTotals_Object(
    (1, 3, 6, 1, 4, 1, 18837, 3, 5, 1, 1, 2, 1, 2),
    _PtpbaseSystemDomainTotals_Type()
)
ptpbaseSystemDomainTotals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ptpbaseSystemDomainTotals.setStatus("current")
if mibBuilder.loadTexts:
    ptpbaseSystemDomainTotals.setUnits("domains")
_PtpbaseSystemProfile_Type = PtpClockProfileType
_PtpbaseSystemProfile_Object = MibScalar
ptpbaseSystemProfile = _PtpbaseSystemProfile_Object(
    (1, 3, 6, 1, 4, 1, 18837, 3, 5, 1, 1, 3),
    _PtpbaseSystemProfile_Type()
)
ptpbaseSystemProfile.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ptpbaseSystemProfile.setStatus("current")
_PtpbaseMIBClockInfo_ObjectIdentity = ObjectIdentity
ptpbaseMIBClockInfo = _PtpbaseMIBClockInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18837, 3, 5, 1, 2)
)
_PtpbaseClockCurrentDSTable_Object = MibTable
ptpbaseClockCurrentDSTable = _PtpbaseClockCurrentDSTable_Object(
    (1, 3, 6, 1, 4, 1, 18837, 3, 5, 1, 2, 1)
)
if mibBuilder.loadTexts:
    ptpbaseClockCurrentDSTable.setStatus("current")
_PtpbaseClockCurrentDSEntry_Object = MibTableRow
ptpbaseClockCurrentDSEntry = _PtpbaseClockCurrentDSEntry_Object(
    (1, 3, 6, 1, 4, 1, 18837, 3, 5, 1, 2, 1, 1)
)
ptpbaseClockCurrentDSEntry.setIndexNames(
    (0, "SPECTRACOM-PTPBASE-MIB", "ptpbaseClockCurrentDSDomainIndex"),
    (0, "SPECTRACOM-PTPBASE-MIB", "ptpbaseClockCurrentDSClockTypeIndex"),
    (0, "SPECTRACOM-PTPBASE-MIB", "ptpbaseClockCurrentDSInstanceIndex"),
)
if mibBuilder.loadTexts:
    ptpbaseClockCurrentDSEntry.setStatus("current")
_PtpbaseClockCurrentDSDomainIndex_Type = PtpClockDomainType
_PtpbaseClockCurrentDSDomainIndex_Object = MibTableColumn
ptpbaseClockCurrentDSDomainIndex = _PtpbaseClockCurrentDSDomainIndex_Object(
    (1, 3, 6, 1, 4, 1, 18837, 3, 5, 1, 2, 1, 1, 1),
    _PtpbaseClockCurrentDSDomainIndex_Type()
)
ptpbaseClockCurrentDSDomainIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ptpbaseClockCurrentDSDomainIndex.setStatus("current")
_PtpbaseClockCurrentDSClockTypeIndex_Type = PtpClockType
_PtpbaseClockCurrentDSClockTypeIndex_Object = MibTableColumn
ptpbaseClockCurrentDSClockTypeIndex = _PtpbaseClockCurrentDSClockTypeIndex_Object(
    (1, 3, 6, 1, 4, 1, 18837, 3, 5, 1, 2, 1, 1, 2),
    _PtpbaseClockCurrentDSClockTypeIndex_Type()
)
ptpbaseClockCurrentDSClockTypeIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ptpbaseClockCurrentDSClockTypeIndex.setStatus("current")
_PtpbaseClockCurrentDSInstanceIndex_Type = PtpClockInstanceType
_PtpbaseClockCurrentDSInstanceIndex_Object = MibTableColumn
ptpbaseClockCurrentDSInstanceIndex = _PtpbaseClockCurrentDSInstanceIndex_Object(
    (1, 3, 6, 1, 4, 1, 18837, 3, 5, 1, 2, 1, 1, 3),
    _PtpbaseClockCurrentDSInstanceIndex_Type()
)
ptpbaseClockCurrentDSInstanceIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ptpbaseClockCurrentDSInstanceIndex.setStatus("current")
_PtpbaseClockCurrentDSStepsRemoved_Type = Unsigned32
_PtpbaseClockCurrentDSStepsRemoved_Object = MibTableColumn
ptpbaseClockCurrentDSStepsRemoved = _PtpbaseClockCurrentDSStepsRemoved_Object(
    (1, 3, 6, 1, 4, 1, 18837, 3, 5, 1, 2, 1, 1, 4),
    _PtpbaseClockCurrentDSStepsRemoved_Type()
)
ptpbaseClockCurrentDSStepsRemoved.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ptpbaseClockCurrentDSStepsRemoved.setStatus("current")
if mibBuilder.loadTexts:
    ptpbaseClockCurrentDSStepsRemoved.setUnits("Steps")
_PtpbaseClockCurrentDSOffsetFromMaster_Type = PtpClockTimeInterval
_PtpbaseClockCurrentDSOffsetFromMaster_Object = MibTableColumn
ptpbaseClockCurrentDSOffsetFromMaster = _PtpbaseClockCurrentDSOffsetFromMaster_Object(
    (1, 3, 6, 1, 4, 1, 18837, 3, 5, 1, 2, 1, 1, 5),
    _PtpbaseClockCurrentDSOffsetFromMaster_Type()
)
ptpbaseClockCurrentDSOffsetFromMaster.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ptpbaseClockCurrentDSOffsetFromMaster.setStatus("current")
if mibBuilder.loadTexts:
    ptpbaseClockCurrentDSOffsetFromMaster.setUnits("Time Interval")
_PtpbaseClockCurrentDSMeanPathDelay_Type = PtpClockTimeInterval
_PtpbaseClockCurrentDSMeanPathDelay_Object = MibTableColumn
ptpbaseClockCurrentDSMeanPathDelay = _PtpbaseClockCurrentDSMeanPathDelay_Object(
    (1, 3, 6, 1, 4, 1, 18837, 3, 5, 1, 2, 1, 1, 6),
    _PtpbaseClockCurrentDSMeanPathDelay_Type()
)
ptpbaseClockCurrentDSMeanPathDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ptpbaseClockCurrentDSMeanPathDelay.setStatus("current")
if mibBuilder.loadTexts:
    ptpbaseClockCurrentDSMeanPathDelay.setUnits("Time Interval")
_PtpbaseClockParentDSTable_Object = MibTable
ptpbaseClockParentDSTable = _PtpbaseClockParentDSTable_Object(
    (1, 3, 6, 1, 4, 1, 18837, 3, 5, 1, 2, 2)
)
if mibBuilder.loadTexts:
    ptpbaseClockParentDSTable.setStatus("current")
_PtpbaseClockParentDSEntry_Object = MibTableRow
ptpbaseClockParentDSEntry = _PtpbaseClockParentDSEntry_Object(
    (1, 3, 6, 1, 4, 1, 18837, 3, 5, 1, 2, 2, 1)
)
ptpbaseClockParentDSEntry.setIndexNames(
    (0, "SPECTRACOM-PTPBASE-MIB", "ptpbaseClockParentDSDomainIndex"),
    (0, "SPECTRACOM-PTPBASE-MIB", "ptpbaseClockParentDSClockTypeIndex"),
    (0, "SPECTRACOM-PTPBASE-MIB", "ptpbaseClockParentDSInstanceIndex"),
)
if mibBuilder.loadTexts:
    ptpbaseClockParentDSEntry.setStatus("current")
_PtpbaseClockParentDSDomainIndex_Type = PtpClockDomainType
_PtpbaseClockParentDSDomainIndex_Object = MibTableColumn
ptpbaseClockParentDSDomainIndex = _PtpbaseClockParentDSDomainIndex_Object(
    (1, 3, 6, 1, 4, 1, 18837, 3, 5, 1, 2, 2, 1, 1),
    _PtpbaseClockParentDSDomainIndex_Type()
)
ptpbaseClockParentDSDomainIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ptpbaseClockParentDSDomainIndex.setStatus("current")
_PtpbaseClockParentDSClockTypeIndex_Type = PtpClockType
_PtpbaseClockParentDSClockTypeIndex_Object = MibTableColumn
ptpbaseClockParentDSClockTypeIndex = _PtpbaseClockParentDSClockTypeIndex_Object(
    (1, 3, 6, 1, 4, 1, 18837, 3, 5, 1, 2, 2, 1, 2),
    _PtpbaseClockParentDSClockTypeIndex_Type()
)
ptpbaseClockParentDSClockTypeIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ptpbaseClockParentDSClockTypeIndex.setStatus("current")
_PtpbaseClockParentDSInstanceIndex_Type = PtpClockInstanceType
_PtpbaseClockParentDSInstanceIndex_Object = MibTableColumn
ptpbaseClockParentDSInstanceIndex = _PtpbaseClockParentDSInstanceIndex_Object(
    (1, 3, 6, 1, 4, 1, 18837, 3, 5, 1, 2, 2, 1, 3),
    _PtpbaseClockParentDSInstanceIndex_Type()
)
ptpbaseClockParentDSInstanceIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ptpbaseClockParentDSInstanceIndex.setStatus("current")


class _PtpbaseClockParentDSParentPortIdentity_Type(OctetString):
    """Custom type ptpbaseClockParentDSParentPortIdentity based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 256),
    )


_PtpbaseClockParentDSParentPortIdentity_Type.__name__ = "OctetString"
_PtpbaseClockParentDSParentPortIdentity_Object = MibTableColumn
ptpbaseClockParentDSParentPortIdentity = _PtpbaseClockParentDSParentPortIdentity_Object(
    (1, 3, 6, 1, 4, 1, 18837, 3, 5, 1, 2, 2, 1, 4),
    _PtpbaseClockParentDSParentPortIdentity_Type()
)
ptpbaseClockParentDSParentPortIdentity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ptpbaseClockParentDSParentPortIdentity.setStatus("current")
_PtpbaseClockParentDSParentStats_Type = TruthValue
_PtpbaseClockParentDSParentStats_Object = MibTableColumn
ptpbaseClockParentDSParentStats = _PtpbaseClockParentDSParentStats_Object(
    (1, 3, 6, 1, 4, 1, 18837, 3, 5, 1, 2, 2, 1, 5),
    _PtpbaseClockParentDSParentStats_Type()
)
ptpbaseClockParentDSParentStats.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ptpbaseClockParentDSParentStats.setStatus("current")


class _PtpbaseClockParentDSOffset_Type(PtpClockIntervalBase2):
    """Custom type ptpbaseClockParentDSOffset based on PtpClockIntervalBase2"""
    subtypeSpec = PtpClockIntervalBase2.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-128, 127),
    )


_PtpbaseClockParentDSOffset_Type.__name__ = "PtpClockIntervalBase2"
_PtpbaseClockParentDSOffset_Object = MibTableColumn
ptpbaseClockParentDSOffset = _PtpbaseClockParentDSOffset_Object(
    (1, 3, 6, 1, 4, 1, 18837, 3, 5, 1, 2, 2, 1, 6),
    _PtpbaseClockParentDSOffset_Type()
)
ptpbaseClockParentDSOffset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ptpbaseClockParentDSOffset.setStatus("current")
_PtpbaseClockParentDSClockPhChRate_Type = Integer32
_PtpbaseClockParentDSClockPhChRate_Object = MibTableColumn
ptpbaseClockParentDSClockPhChRate = _PtpbaseClockParentDSClockPhChRate_Object(
    (1, 3, 6, 1, 4, 1, 18837, 3, 5, 1, 2, 2, 1, 7),
    _PtpbaseClockParentDSClockPhChRate_Type()
)
ptpbaseClockParentDSClockPhChRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ptpbaseClockParentDSClockPhChRate.setStatus("current")
_PtpbaseClockParentDSGMClockIdentity_Type = PtpClockIdentity
_PtpbaseClockParentDSGMClockIdentity_Object = MibTableColumn
ptpbaseClockParentDSGMClockIdentity = _PtpbaseClockParentDSGMClockIdentity_Object(
    (1, 3, 6, 1, 4, 1, 18837, 3, 5, 1, 2, 2, 1, 8),
    _PtpbaseClockParentDSGMClockIdentity_Type()
)
ptpbaseClockParentDSGMClockIdentity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ptpbaseClockParentDSGMClockIdentity.setStatus("current")
_PtpbaseClockParentDSGMClockPriority1_Type = Unsigned32
_PtpbaseClockParentDSGMClockPriority1_Object = MibTableColumn
ptpbaseClockParentDSGMClockPriority1 = _PtpbaseClockParentDSGMClockPriority1_Object(
    (1, 3, 6, 1, 4, 1, 18837, 3, 5, 1, 2, 2, 1, 9),
    _PtpbaseClockParentDSGMClockPriority1_Type()
)
ptpbaseClockParentDSGMClockPriority1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ptpbaseClockParentDSGMClockPriority1.setStatus("current")
_PtpbaseClockParentDSGMClockPriority2_Type = Unsigned32
_PtpbaseClockParentDSGMClockPriority2_Object = MibTableColumn
ptpbaseClockParentDSGMClockPriority2 = _PtpbaseClockParentDSGMClockPriority2_Object(
    (1, 3, 6, 1, 4, 1, 18837, 3, 5, 1, 2, 2, 1, 10),
    _PtpbaseClockParentDSGMClockPriority2_Type()
)
ptpbaseClockParentDSGMClockPriority2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ptpbaseClockParentDSGMClockPriority2.setStatus("current")
_PtpbaseClockParentDSGMClockQualityClass_Type = PtpClockQualityClassType
_PtpbaseClockParentDSGMClockQualityClass_Object = MibTableColumn
ptpbaseClockParentDSGMClockQualityClass = _PtpbaseClockParentDSGMClockQualityClass_Object(
    (1, 3, 6, 1, 4, 1, 18837, 3, 5, 1, 2, 2, 1, 11),
    _PtpbaseClockParentDSGMClockQualityClass_Type()
)
ptpbaseClockParentDSGMClockQualityClass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ptpbaseClockParentDSGMClockQualityClass.setStatus("current")
_PtpbaseClockParentDSGMClockQualityAccuracy_Type = PtpClockQualityAccuracyType
_PtpbaseClockParentDSGMClockQualityAccuracy_Object = MibTableColumn
ptpbaseClockParentDSGMClockQualityAccuracy = _PtpbaseClockParentDSGMClockQualityAccuracy_Object(
    (1, 3, 6, 1, 4, 1, 18837, 3, 5, 1, 2, 2, 1, 12),
    _PtpbaseClockParentDSGMClockQualityAccuracy_Type()
)
ptpbaseClockParentDSGMClockQualityAccuracy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ptpbaseClockParentDSGMClockQualityAccuracy.setStatus("current")
_PtpbaseClockParentDSGMClockQualityOffset_Type = Unsigned32
_PtpbaseClockParentDSGMClockQualityOffset_Object = MibTableColumn
ptpbaseClockParentDSGMClockQualityOffset = _PtpbaseClockParentDSGMClockQualityOffset_Object(
    (1, 3, 6, 1, 4, 1, 18837, 3, 5, 1, 2, 2, 1, 13),
    _PtpbaseClockParentDSGMClockQualityOffset_Type()
)
ptpbaseClockParentDSGMClockQualityOffset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ptpbaseClockParentDSGMClockQualityOffset.setStatus("current")
_PtpbaseClockDefaultDSTable_Object = MibTable
ptpbaseClockDefaultDSTable = _PtpbaseClockDefaultDSTable_Object(
    (1, 3, 6, 1, 4, 1, 18837, 3, 5, 1, 2, 3)
)
if mibBuilder.loadTexts:
    ptpbaseClockDefaultDSTable.setStatus("current")
_PtpbaseClockDefaultDSEntry_Object = MibTableRow
ptpbaseClockDefaultDSEntry = _PtpbaseClockDefaultDSEntry_Object(
    (1, 3, 6, 1, 4, 1, 18837, 3, 5, 1, 2, 3, 1)
)
ptpbaseClockDefaultDSEntry.setIndexNames(
    (0, "SPECTRACOM-PTPBASE-MIB", "ptpbaseClockDefaultDSDomainIndex"),
    (0, "SPECTRACOM-PTPBASE-MIB", "ptpbaseClockDefaultDSClockTypeIndex"),
    (0, "SPECTRACOM-PTPBASE-MIB", "ptpbaseClockDefaultDSInstanceIndex"),
)
if mibBuilder.loadTexts:
    ptpbaseClockDefaultDSEntry.setStatus("current")
_PtpbaseClockDefaultDSDomainIndex_Type = PtpClockDomainType
_PtpbaseClockDefaultDSDomainIndex_Object = MibTableColumn
ptpbaseClockDefaultDSDomainIndex = _PtpbaseClockDefaultDSDomainIndex_Object(
    (1, 3, 6, 1, 4, 1, 18837, 3, 5, 1, 2, 3, 1, 1),
    _PtpbaseClockDefaultDSDomainIndex_Type()
)
ptpbaseClockDefaultDSDomainIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ptpbaseClockDefaultDSDomainIndex.setStatus("current")
_PtpbaseClockDefaultDSClockTypeIndex_Type = PtpClockType
_PtpbaseClockDefaultDSClockTypeIndex_Object = MibTableColumn
ptpbaseClockDefaultDSClockTypeIndex = _PtpbaseClockDefaultDSClockTypeIndex_Object(
    (1, 3, 6, 1, 4, 1, 18837, 3, 5, 1, 2, 3, 1, 2),
    _PtpbaseClockDefaultDSClockTypeIndex_Type()
)
ptpbaseClockDefaultDSClockTypeIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ptpbaseClockDefaultDSClockTypeIndex.setStatus("current")
_PtpbaseClockDefaultDSInstanceIndex_Type = PtpClockInstanceType
_PtpbaseClockDefaultDSInstanceIndex_Object = MibTableColumn
ptpbaseClockDefaultDSInstanceIndex = _PtpbaseClockDefaultDSInstanceIndex_Object(
    (1, 3, 6, 1, 4, 1, 18837, 3, 5, 1, 2, 3, 1, 3),
    _PtpbaseClockDefaultDSInstanceIndex_Type()
)
ptpbaseClockDefaultDSInstanceIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ptpbaseClockDefaultDSInstanceIndex.setStatus("current")
_PtpbaseClockDefaultDSTwoStepFlag_Type = TruthValue
_PtpbaseClockDefaultDSTwoStepFlag_Object = MibTableColumn
ptpbaseClockDefaultDSTwoStepFlag = _PtpbaseClockDefaultDSTwoStepFlag_Object(
    (1, 3, 6, 1, 4, 1, 18837, 3, 5, 1, 2, 3, 1, 4),
    _PtpbaseClockDefaultDSTwoStepFlag_Type()
)
ptpbaseClockDefaultDSTwoStepFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ptpbaseClockDefaultDSTwoStepFlag.setStatus("current")
_PtpbaseClockDefaultDSClockIdentity_Type = PtpClockIdentity
_PtpbaseClockDefaultDSClockIdentity_Object = MibTableColumn
ptpbaseClockDefaultDSClockIdentity = _PtpbaseClockDefaultDSClockIdentity_Object(
    (1, 3, 6, 1, 4, 1, 18837, 3, 5, 1, 2, 3, 1, 5),
    _PtpbaseClockDefaultDSClockIdentity_Type()
)
ptpbaseClockDefaultDSClockIdentity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ptpbaseClockDefaultDSClockIdentity.setStatus("current")
_PtpbaseClockDefaultDSPriority1_Type = Unsigned32
_PtpbaseClockDefaultDSPriority1_Object = MibTableColumn
ptpbaseClockDefaultDSPriority1 = _PtpbaseClockDefaultDSPriority1_Object(
    (1, 3, 6, 1, 4, 1, 18837, 3, 5, 1, 2, 3, 1, 6),
    _PtpbaseClockDefaultDSPriority1_Type()
)
ptpbaseClockDefaultDSPriority1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ptpbaseClockDefaultDSPriority1.setStatus("current")
_PtpbaseClockDefaultDSPriority2_Type = Unsigned32
_PtpbaseClockDefaultDSPriority2_Object = MibTableColumn
ptpbaseClockDefaultDSPriority2 = _PtpbaseClockDefaultDSPriority2_Object(
    (1, 3, 6, 1, 4, 1, 18837, 3, 5, 1, 2, 3, 1, 7),
    _PtpbaseClockDefaultDSPriority2_Type()
)
ptpbaseClockDefaultDSPriority2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ptpbaseClockDefaultDSPriority2.setStatus("current")
_PtpbaseClockDefaultDSSlaveOnly_Type = TruthValue
_PtpbaseClockDefaultDSSlaveOnly_Object = MibTableColumn
ptpbaseClockDefaultDSSlaveOnly = _PtpbaseClockDefaultDSSlaveOnly_Object(
    (1, 3, 6, 1, 4, 1, 18837, 3, 5, 1, 2, 3, 1, 8),
    _PtpbaseClockDefaultDSSlaveOnly_Type()
)
ptpbaseClockDefaultDSSlaveOnly.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ptpbaseClockDefaultDSSlaveOnly.setStatus("current")
_PtpbaseClockDefaultDSQualityClass_Type = PtpClockQualityClassType
_PtpbaseClockDefaultDSQualityClass_Object = MibTableColumn
ptpbaseClockDefaultDSQualityClass = _PtpbaseClockDefaultDSQualityClass_Object(
    (1, 3, 6, 1, 4, 1, 18837, 3, 5, 1, 2, 3, 1, 9),
    _PtpbaseClockDefaultDSQualityClass_Type()
)
ptpbaseClockDefaultDSQualityClass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ptpbaseClockDefaultDSQualityClass.setStatus("current")
_PtpbaseClockDefaultDSQualityAccuracy_Type = PtpClockQualityAccuracyType
_PtpbaseClockDefaultDSQualityAccuracy_Object = MibTableColumn
ptpbaseClockDefaultDSQualityAccuracy = _PtpbaseClockDefaultDSQualityAccuracy_Object(
    (1, 3, 6, 1, 4, 1, 18837, 3, 5, 1, 2, 3, 1, 10),
    _PtpbaseClockDefaultDSQualityAccuracy_Type()
)
ptpbaseClockDefaultDSQualityAccuracy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ptpbaseClockDefaultDSQualityAccuracy.setStatus("current")
_PtpbaseClockDefaultDSQualityOffset_Type = Integer32
_PtpbaseClockDefaultDSQualityOffset_Object = MibTableColumn
ptpbaseClockDefaultDSQualityOffset = _PtpbaseClockDefaultDSQualityOffset_Object(
    (1, 3, 6, 1, 4, 1, 18837, 3, 5, 1, 2, 3, 1, 11),
    _PtpbaseClockDefaultDSQualityOffset_Type()
)
ptpbaseClockDefaultDSQualityOffset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ptpbaseClockDefaultDSQualityOffset.setStatus("current")
_PtpbaseClockRunningTable_Object = MibTable
ptpbaseClockRunningTable = _PtpbaseClockRunningTable_Object(
    (1, 3, 6, 1, 4, 1, 18837, 3, 5, 1, 2, 4)
)
if mibBuilder.loadTexts:
    ptpbaseClockRunningTable.setStatus("current")
_PtpbaseClockRunningEntry_Object = MibTableRow
ptpbaseClockRunningEntry = _PtpbaseClockRunningEntry_Object(
    (1, 3, 6, 1, 4, 1, 18837, 3, 5, 1, 2, 4, 1)
)
ptpbaseClockRunningEntry.setIndexNames(
    (0, "SPECTRACOM-PTPBASE-MIB", "ptpbaseClockRunningDomainIndex"),
    (0, "SPECTRACOM-PTPBASE-MIB", "ptpbaseClockRunningClockTypeIndex"),
    (0, "SPECTRACOM-PTPBASE-MIB", "ptpbaseClockRunningInstanceIndex"),
)
if mibBuilder.loadTexts:
    ptpbaseClockRunningEntry.setStatus("current")
_PtpbaseClockRunningDomainIndex_Type = PtpClockDomainType
_PtpbaseClockRunningDomainIndex_Object = MibTableColumn
ptpbaseClockRunningDomainIndex = _PtpbaseClockRunningDomainIndex_Object(
    (1, 3, 6, 1, 4, 1, 18837, 3, 5, 1, 2, 4, 1, 1),
    _PtpbaseClockRunningDomainIndex_Type()
)
ptpbaseClockRunningDomainIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ptpbaseClockRunningDomainIndex.setStatus("current")
_PtpbaseClockRunningClockTypeIndex_Type = PtpClockType
_PtpbaseClockRunningClockTypeIndex_Object = MibTableColumn
ptpbaseClockRunningClockTypeIndex = _PtpbaseClockRunningClockTypeIndex_Object(
    (1, 3, 6, 1, 4, 1, 18837, 3, 5, 1, 2, 4, 1, 2),
    _PtpbaseClockRunningClockTypeIndex_Type()
)
ptpbaseClockRunningClockTypeIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ptpbaseClockRunningClockTypeIndex.setStatus("current")
_PtpbaseClockRunningInstanceIndex_Type = PtpClockInstanceType
_PtpbaseClockRunningInstanceIndex_Object = MibTableColumn
ptpbaseClockRunningInstanceIndex = _PtpbaseClockRunningInstanceIndex_Object(
    (1, 3, 6, 1, 4, 1, 18837, 3, 5, 1, 2, 4, 1, 3),
    _PtpbaseClockRunningInstanceIndex_Type()
)
ptpbaseClockRunningInstanceIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ptpbaseClockRunningInstanceIndex.setStatus("current")
_PtpbaseClockRunningState_Type = PtpClockStateType
_PtpbaseClockRunningState_Object = MibTableColumn
ptpbaseClockRunningState = _PtpbaseClockRunningState_Object(
    (1, 3, 6, 1, 4, 1, 18837, 3, 5, 1, 2, 4, 1, 4),
    _PtpbaseClockRunningState_Type()
)
ptpbaseClockRunningState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ptpbaseClockRunningState.setStatus("current")
_PtpbaseClockRunningPacketsSent_Type = Counter64
_PtpbaseClockRunningPacketsSent_Object = MibTableColumn
ptpbaseClockRunningPacketsSent = _PtpbaseClockRunningPacketsSent_Object(
    (1, 3, 6, 1, 4, 1, 18837, 3, 5, 1, 2, 4, 1, 5),
    _PtpbaseClockRunningPacketsSent_Type()
)
ptpbaseClockRunningPacketsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ptpbaseClockRunningPacketsSent.setStatus("current")
_PtpbaseClockRunningPacketsReceived_Type = Counter64
_PtpbaseClockRunningPacketsReceived_Object = MibTableColumn
ptpbaseClockRunningPacketsReceived = _PtpbaseClockRunningPacketsReceived_Object(
    (1, 3, 6, 1, 4, 1, 18837, 3, 5, 1, 2, 4, 1, 6),
    _PtpbaseClockRunningPacketsReceived_Type()
)
ptpbaseClockRunningPacketsReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ptpbaseClockRunningPacketsReceived.setStatus("current")
_PtpbaseClockTimePropertiesDSTable_Object = MibTable
ptpbaseClockTimePropertiesDSTable = _PtpbaseClockTimePropertiesDSTable_Object(
    (1, 3, 6, 1, 4, 1, 18837, 3, 5, 1, 2, 5)
)
if mibBuilder.loadTexts:
    ptpbaseClockTimePropertiesDSTable.setStatus("current")
_PtpbaseClockTimePropertiesDSEntry_Object = MibTableRow
ptpbaseClockTimePropertiesDSEntry = _PtpbaseClockTimePropertiesDSEntry_Object(
    (1, 3, 6, 1, 4, 1, 18837, 3, 5, 1, 2, 5, 1)
)
ptpbaseClockTimePropertiesDSEntry.setIndexNames(
    (0, "SPECTRACOM-PTPBASE-MIB", "ptpbaseClockTimePropertiesDSDomainIndex"),
    (0, "SPECTRACOM-PTPBASE-MIB", "ptpbaseClockTimePropertiesDSClockTypeIndex"),
    (0, "SPECTRACOM-PTPBASE-MIB", "ptpbaseClockTimePropertiesDSInstanceIndex"),
)
if mibBuilder.loadTexts:
    ptpbaseClockTimePropertiesDSEntry.setStatus("current")
_PtpbaseClockTimePropertiesDSDomainIndex_Type = PtpClockDomainType
_PtpbaseClockTimePropertiesDSDomainIndex_Object = MibTableColumn
ptpbaseClockTimePropertiesDSDomainIndex = _PtpbaseClockTimePropertiesDSDomainIndex_Object(
    (1, 3, 6, 1, 4, 1, 18837, 3, 5, 1, 2, 5, 1, 1),
    _PtpbaseClockTimePropertiesDSDomainIndex_Type()
)
ptpbaseClockTimePropertiesDSDomainIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ptpbaseClockTimePropertiesDSDomainIndex.setStatus("current")
_PtpbaseClockTimePropertiesDSClockTypeIndex_Type = PtpClockType
_PtpbaseClockTimePropertiesDSClockTypeIndex_Object = MibTableColumn
ptpbaseClockTimePropertiesDSClockTypeIndex = _PtpbaseClockTimePropertiesDSClockTypeIndex_Object(
    (1, 3, 6, 1, 4, 1, 18837, 3, 5, 1, 2, 5, 1, 2),
    _PtpbaseClockTimePropertiesDSClockTypeIndex_Type()
)
ptpbaseClockTimePropertiesDSClockTypeIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ptpbaseClockTimePropertiesDSClockTypeIndex.setStatus("current")
_PtpbaseClockTimePropertiesDSInstanceIndex_Type = PtpClockInstanceType
_PtpbaseClockTimePropertiesDSInstanceIndex_Object = MibTableColumn
ptpbaseClockTimePropertiesDSInstanceIndex = _PtpbaseClockTimePropertiesDSInstanceIndex_Object(
    (1, 3, 6, 1, 4, 1, 18837, 3, 5, 1, 2, 5, 1, 3),
    _PtpbaseClockTimePropertiesDSInstanceIndex_Type()
)
ptpbaseClockTimePropertiesDSInstanceIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ptpbaseClockTimePropertiesDSInstanceIndex.setStatus("current")
_PtpbaseClockTimePropertiesDSCurrentUTCOffsetValid_Type = TruthValue
_PtpbaseClockTimePropertiesDSCurrentUTCOffsetValid_Object = MibTableColumn
ptpbaseClockTimePropertiesDSCurrentUTCOffsetValid = _PtpbaseClockTimePropertiesDSCurrentUTCOffsetValid_Object(
    (1, 3, 6, 1, 4, 1, 18837, 3, 5, 1, 2, 5, 1, 4),
    _PtpbaseClockTimePropertiesDSCurrentUTCOffsetValid_Type()
)
ptpbaseClockTimePropertiesDSCurrentUTCOffsetValid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ptpbaseClockTimePropertiesDSCurrentUTCOffsetValid.setStatus("current")
_PtpbaseClockTimePropertiesDSCurrentUTCOffset_Type = Integer32
_PtpbaseClockTimePropertiesDSCurrentUTCOffset_Object = MibTableColumn
ptpbaseClockTimePropertiesDSCurrentUTCOffset = _PtpbaseClockTimePropertiesDSCurrentUTCOffset_Object(
    (1, 3, 6, 1, 4, 1, 18837, 3, 5, 1, 2, 5, 1, 5),
    _PtpbaseClockTimePropertiesDSCurrentUTCOffset_Type()
)
ptpbaseClockTimePropertiesDSCurrentUTCOffset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ptpbaseClockTimePropertiesDSCurrentUTCOffset.setStatus("current")
_PtpbaseClockTimePropertiesDSLeap59_Type = TruthValue
_PtpbaseClockTimePropertiesDSLeap59_Object = MibTableColumn
ptpbaseClockTimePropertiesDSLeap59 = _PtpbaseClockTimePropertiesDSLeap59_Object(
    (1, 3, 6, 1, 4, 1, 18837, 3, 5, 1, 2, 5, 1, 6),
    _PtpbaseClockTimePropertiesDSLeap59_Type()
)
ptpbaseClockTimePropertiesDSLeap59.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ptpbaseClockTimePropertiesDSLeap59.setStatus("current")
_PtpbaseClockTimePropertiesDSLeap61_Type = TruthValue
_PtpbaseClockTimePropertiesDSLeap61_Object = MibTableColumn
ptpbaseClockTimePropertiesDSLeap61 = _PtpbaseClockTimePropertiesDSLeap61_Object(
    (1, 3, 6, 1, 4, 1, 18837, 3, 5, 1, 2, 5, 1, 7),
    _PtpbaseClockTimePropertiesDSLeap61_Type()
)
ptpbaseClockTimePropertiesDSLeap61.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ptpbaseClockTimePropertiesDSLeap61.setStatus("current")
_PtpbaseClockTimePropertiesDSTimeTraceable_Type = TruthValue
_PtpbaseClockTimePropertiesDSTimeTraceable_Object = MibTableColumn
ptpbaseClockTimePropertiesDSTimeTraceable = _PtpbaseClockTimePropertiesDSTimeTraceable_Object(
    (1, 3, 6, 1, 4, 1, 18837, 3, 5, 1, 2, 5, 1, 8),
    _PtpbaseClockTimePropertiesDSTimeTraceable_Type()
)
ptpbaseClockTimePropertiesDSTimeTraceable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ptpbaseClockTimePropertiesDSTimeTraceable.setStatus("current")
_PtpbaseClockTimePropertiesDSFreqTraceable_Type = TruthValue
_PtpbaseClockTimePropertiesDSFreqTraceable_Object = MibTableColumn
ptpbaseClockTimePropertiesDSFreqTraceable = _PtpbaseClockTimePropertiesDSFreqTraceable_Object(
    (1, 3, 6, 1, 4, 1, 18837, 3, 5, 1, 2, 5, 1, 9),
    _PtpbaseClockTimePropertiesDSFreqTraceable_Type()
)
ptpbaseClockTimePropertiesDSFreqTraceable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ptpbaseClockTimePropertiesDSFreqTraceable.setStatus("current")
_PtpbaseClockTimePropertiesDSPTPTimescale_Type = TruthValue
_PtpbaseClockTimePropertiesDSPTPTimescale_Object = MibTableColumn
ptpbaseClockTimePropertiesDSPTPTimescale = _PtpbaseClockTimePropertiesDSPTPTimescale_Object(
    (1, 3, 6, 1, 4, 1, 18837, 3, 5, 1, 2, 5, 1, 10),
    _PtpbaseClockTimePropertiesDSPTPTimescale_Type()
)
ptpbaseClockTimePropertiesDSPTPTimescale.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ptpbaseClockTimePropertiesDSPTPTimescale.setStatus("current")
_PtpbaseClockTimePropertiesDSSource_Type = PtpClockTimeSourceType
_PtpbaseClockTimePropertiesDSSource_Object = MibTableColumn
ptpbaseClockTimePropertiesDSSource = _PtpbaseClockTimePropertiesDSSource_Object(
    (1, 3, 6, 1, 4, 1, 18837, 3, 5, 1, 2, 5, 1, 11),
    _PtpbaseClockTimePropertiesDSSource_Type()
)
ptpbaseClockTimePropertiesDSSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ptpbaseClockTimePropertiesDSSource.setStatus("current")
_PtpbaseClockTransDefaultDSTable_Object = MibTable
ptpbaseClockTransDefaultDSTable = _PtpbaseClockTransDefaultDSTable_Object(
    (1, 3, 6, 1, 4, 1, 18837, 3, 5, 1, 2, 6)
)
if mibBuilder.loadTexts:
    ptpbaseClockTransDefaultDSTable.setStatus("current")
_PtpbaseClockTransDefaultDSEntry_Object = MibTableRow
ptpbaseClockTransDefaultDSEntry = _PtpbaseClockTransDefaultDSEntry_Object(
    (1, 3, 6, 1, 4, 1, 18837, 3, 5, 1, 2, 6, 1)
)
ptpbaseClockTransDefaultDSEntry.setIndexNames(
    (0, "SPECTRACOM-PTPBASE-MIB", "ptpbaseClockTransDefaultDSDomainIndex"),
    (0, "SPECTRACOM-PTPBASE-MIB", "ptpbaseClockTransDefaultDSInstanceIndex"),
)
if mibBuilder.loadTexts:
    ptpbaseClockTransDefaultDSEntry.setStatus("current")
_PtpbaseClockTransDefaultDSDomainIndex_Type = PtpClockDomainType
_PtpbaseClockTransDefaultDSDomainIndex_Object = MibTableColumn
ptpbaseClockTransDefaultDSDomainIndex = _PtpbaseClockTransDefaultDSDomainIndex_Object(
    (1, 3, 6, 1, 4, 1, 18837, 3, 5, 1, 2, 6, 1, 1),
    _PtpbaseClockTransDefaultDSDomainIndex_Type()
)
ptpbaseClockTransDefaultDSDomainIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ptpbaseClockTransDefaultDSDomainIndex.setStatus("current")
_PtpbaseClockTransDefaultDSInstanceIndex_Type = PtpClockInstanceType
_PtpbaseClockTransDefaultDSInstanceIndex_Object = MibTableColumn
ptpbaseClockTransDefaultDSInstanceIndex = _PtpbaseClockTransDefaultDSInstanceIndex_Object(
    (1, 3, 6, 1, 4, 1, 18837, 3, 5, 1, 2, 6, 1, 2),
    _PtpbaseClockTransDefaultDSInstanceIndex_Type()
)
ptpbaseClockTransDefaultDSInstanceIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ptpbaseClockTransDefaultDSInstanceIndex.setStatus("current")
_PtpbaseClockTransDefaultDSClockIdentity_Type = PtpClockIdentity
_PtpbaseClockTransDefaultDSClockIdentity_Object = MibTableColumn
ptpbaseClockTransDefaultDSClockIdentity = _PtpbaseClockTransDefaultDSClockIdentity_Object(
    (1, 3, 6, 1, 4, 1, 18837, 3, 5, 1, 2, 6, 1, 3),
    _PtpbaseClockTransDefaultDSClockIdentity_Type()
)
ptpbaseClockTransDefaultDSClockIdentity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ptpbaseClockTransDefaultDSClockIdentity.setStatus("current")
_PtpbaseClockTransDefaultDSNumOfPorts_Type = Counter32
_PtpbaseClockTransDefaultDSNumOfPorts_Object = MibTableColumn
ptpbaseClockTransDefaultDSNumOfPorts = _PtpbaseClockTransDefaultDSNumOfPorts_Object(
    (1, 3, 6, 1, 4, 1, 18837, 3, 5, 1, 2, 6, 1, 4),
    _PtpbaseClockTransDefaultDSNumOfPorts_Type()
)
ptpbaseClockTransDefaultDSNumOfPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ptpbaseClockTransDefaultDSNumOfPorts.setStatus("current")
_PtpbaseClockTransDefaultDSDelay_Type = PtpClockMechanismType
_PtpbaseClockTransDefaultDSDelay_Object = MibTableColumn
ptpbaseClockTransDefaultDSDelay = _PtpbaseClockTransDefaultDSDelay_Object(
    (1, 3, 6, 1, 4, 1, 18837, 3, 5, 1, 2, 6, 1, 5),
    _PtpbaseClockTransDefaultDSDelay_Type()
)
ptpbaseClockTransDefaultDSDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ptpbaseClockTransDefaultDSDelay.setStatus("current")
_PtpbaseClockTransDefaultDSPrimaryDomain_Type = PtpClockDomainType
_PtpbaseClockTransDefaultDSPrimaryDomain_Object = MibTableColumn
ptpbaseClockTransDefaultDSPrimaryDomain = _PtpbaseClockTransDefaultDSPrimaryDomain_Object(
    (1, 3, 6, 1, 4, 1, 18837, 3, 5, 1, 2, 6, 1, 6),
    _PtpbaseClockTransDefaultDSPrimaryDomain_Type()
)
ptpbaseClockTransDefaultDSPrimaryDomain.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ptpbaseClockTransDefaultDSPrimaryDomain.setStatus("current")
_PtpbaseClockPortTable_Object = MibTable
ptpbaseClockPortTable = _PtpbaseClockPortTable_Object(
    (1, 3, 6, 1, 4, 1, 18837, 3, 5, 1, 2, 7)
)
if mibBuilder.loadTexts:
    ptpbaseClockPortTable.setStatus("current")
_PtpbaseClockPortEntry_Object = MibTableRow
ptpbaseClockPortEntry = _PtpbaseClockPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 18837, 3, 5, 1, 2, 7, 1)
)
ptpbaseClockPortEntry.setIndexNames(
    (0, "SPECTRACOM-PTPBASE-MIB", "ptpbaseClockPortDomainIndex"),
    (0, "SPECTRACOM-PTPBASE-MIB", "ptpbaseClockPortClockTypeIndex"),
    (0, "SPECTRACOM-PTPBASE-MIB", "ptpbaseClockPortClockInstanceIndex"),
    (0, "SPECTRACOM-PTPBASE-MIB", "ptpbaseClockPortTablePortNumberIndex"),
)
if mibBuilder.loadTexts:
    ptpbaseClockPortEntry.setStatus("current")
_PtpbaseClockPortDomainIndex_Type = PtpClockDomainType
_PtpbaseClockPortDomainIndex_Object = MibTableColumn
ptpbaseClockPortDomainIndex = _PtpbaseClockPortDomainIndex_Object(
    (1, 3, 6, 1, 4, 1, 18837, 3, 5, 1, 2, 7, 1, 1),
    _PtpbaseClockPortDomainIndex_Type()
)
ptpbaseClockPortDomainIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ptpbaseClockPortDomainIndex.setStatus("current")
_PtpbaseClockPortClockTypeIndex_Type = PtpClockType
_PtpbaseClockPortClockTypeIndex_Object = MibTableColumn
ptpbaseClockPortClockTypeIndex = _PtpbaseClockPortClockTypeIndex_Object(
    (1, 3, 6, 1, 4, 1, 18837, 3, 5, 1, 2, 7, 1, 2),
    _PtpbaseClockPortClockTypeIndex_Type()
)
ptpbaseClockPortClockTypeIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ptpbaseClockPortClockTypeIndex.setStatus("current")
_PtpbaseClockPortClockInstanceIndex_Type = PtpClockInstanceType
_PtpbaseClockPortClockInstanceIndex_Object = MibTableColumn
ptpbaseClockPortClockInstanceIndex = _PtpbaseClockPortClockInstanceIndex_Object(
    (1, 3, 6, 1, 4, 1, 18837, 3, 5, 1, 2, 7, 1, 3),
    _PtpbaseClockPortClockInstanceIndex_Type()
)
ptpbaseClockPortClockInstanceIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ptpbaseClockPortClockInstanceIndex.setStatus("current")
_PtpbaseClockPortTablePortNumberIndex_Type = PtpClockPortNumber
_PtpbaseClockPortTablePortNumberIndex_Object = MibTableColumn
ptpbaseClockPortTablePortNumberIndex = _PtpbaseClockPortTablePortNumberIndex_Object(
    (1, 3, 6, 1, 4, 1, 18837, 3, 5, 1, 2, 7, 1, 4),
    _PtpbaseClockPortTablePortNumberIndex_Type()
)
ptpbaseClockPortTablePortNumberIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ptpbaseClockPortTablePortNumberIndex.setStatus("current")


class _PtpbaseClockPortName_Type(DisplayString):
    """Custom type ptpbaseClockPortName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_PtpbaseClockPortName_Type.__name__ = "DisplayString"
_PtpbaseClockPortName_Object = MibTableColumn
ptpbaseClockPortName = _PtpbaseClockPortName_Object(
    (1, 3, 6, 1, 4, 1, 18837, 3, 5, 1, 2, 7, 1, 5),
    _PtpbaseClockPortName_Type()
)
ptpbaseClockPortName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ptpbaseClockPortName.setStatus("current")
_PtpbaseClockPortRole_Type = PtpClockRoleType
_PtpbaseClockPortRole_Object = MibTableColumn
ptpbaseClockPortRole = _PtpbaseClockPortRole_Object(
    (1, 3, 6, 1, 4, 1, 18837, 3, 5, 1, 2, 7, 1, 6),
    _PtpbaseClockPortRole_Type()
)
ptpbaseClockPortRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ptpbaseClockPortRole.setStatus("current")
_PtpbaseClockPortSyncTwoStep_Type = TruthValue
_PtpbaseClockPortSyncTwoStep_Object = MibTableColumn
ptpbaseClockPortSyncTwoStep = _PtpbaseClockPortSyncTwoStep_Object(
    (1, 3, 6, 1, 4, 1, 18837, 3, 5, 1, 2, 7, 1, 7),
    _PtpbaseClockPortSyncTwoStep_Type()
)
ptpbaseClockPortSyncTwoStep.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ptpbaseClockPortSyncTwoStep.setStatus("current")
_PtpbaseClockPortCurrentPeerAddressType_Type = AutonomousType
_PtpbaseClockPortCurrentPeerAddressType_Object = MibTableColumn
ptpbaseClockPortCurrentPeerAddressType = _PtpbaseClockPortCurrentPeerAddressType_Object(
    (1, 3, 6, 1, 4, 1, 18837, 3, 5, 1, 2, 7, 1, 8),
    _PtpbaseClockPortCurrentPeerAddressType_Type()
)
ptpbaseClockPortCurrentPeerAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ptpbaseClockPortCurrentPeerAddressType.setStatus("current")
_PtpbaseClockPortCurrentPeerAddress_Type = PtpClockPortTransportTypeAddress
_PtpbaseClockPortCurrentPeerAddress_Object = MibTableColumn
ptpbaseClockPortCurrentPeerAddress = _PtpbaseClockPortCurrentPeerAddress_Object(
    (1, 3, 6, 1, 4, 1, 18837, 3, 5, 1, 2, 7, 1, 9),
    _PtpbaseClockPortCurrentPeerAddress_Type()
)
ptpbaseClockPortCurrentPeerAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ptpbaseClockPortCurrentPeerAddress.setStatus("current")
_PtpbaseClockPortNumOfAssociatedPorts_Type = Gauge32
_PtpbaseClockPortNumOfAssociatedPorts_Object = MibTableColumn
ptpbaseClockPortNumOfAssociatedPorts = _PtpbaseClockPortNumOfAssociatedPorts_Object(
    (1, 3, 6, 1, 4, 1, 18837, 3, 5, 1, 2, 7, 1, 10),
    _PtpbaseClockPortNumOfAssociatedPorts_Type()
)
ptpbaseClockPortNumOfAssociatedPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ptpbaseClockPortNumOfAssociatedPorts.setStatus("current")
_PtpbaseClockPortDSTable_Object = MibTable
ptpbaseClockPortDSTable = _PtpbaseClockPortDSTable_Object(
    (1, 3, 6, 1, 4, 1, 18837, 3, 5, 1, 2, 8)
)
if mibBuilder.loadTexts:
    ptpbaseClockPortDSTable.setStatus("current")
_PtpbaseClockPortDSEntry_Object = MibTableRow
ptpbaseClockPortDSEntry = _PtpbaseClockPortDSEntry_Object(
    (1, 3, 6, 1, 4, 1, 18837, 3, 5, 1, 2, 8, 1)
)
ptpbaseClockPortDSEntry.setIndexNames(
    (0, "SPECTRACOM-PTPBASE-MIB", "ptpbaseClockPortDSDomainIndex"),
    (0, "SPECTRACOM-PTPBASE-MIB", "ptpbaseClockPortDSClockTypeIndex"),
    (0, "SPECTRACOM-PTPBASE-MIB", "ptpbaseClockPortDSClockInstanceIndex"),
    (0, "SPECTRACOM-PTPBASE-MIB", "ptpbaseClockPortDSPortNumberIndex"),
)
if mibBuilder.loadTexts:
    ptpbaseClockPortDSEntry.setStatus("current")
_PtpbaseClockPortDSDomainIndex_Type = PtpClockDomainType
_PtpbaseClockPortDSDomainIndex_Object = MibTableColumn
ptpbaseClockPortDSDomainIndex = _PtpbaseClockPortDSDomainIndex_Object(
    (1, 3, 6, 1, 4, 1, 18837, 3, 5, 1, 2, 8, 1, 1),
    _PtpbaseClockPortDSDomainIndex_Type()
)
ptpbaseClockPortDSDomainIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ptpbaseClockPortDSDomainIndex.setStatus("current")
_PtpbaseClockPortDSClockTypeIndex_Type = PtpClockType
_PtpbaseClockPortDSClockTypeIndex_Object = MibTableColumn
ptpbaseClockPortDSClockTypeIndex = _PtpbaseClockPortDSClockTypeIndex_Object(
    (1, 3, 6, 1, 4, 1, 18837, 3, 5, 1, 2, 8, 1, 2),
    _PtpbaseClockPortDSClockTypeIndex_Type()
)
ptpbaseClockPortDSClockTypeIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ptpbaseClockPortDSClockTypeIndex.setStatus("current")
_PtpbaseClockPortDSClockInstanceIndex_Type = PtpClockInstanceType
_PtpbaseClockPortDSClockInstanceIndex_Object = MibTableColumn
ptpbaseClockPortDSClockInstanceIndex = _PtpbaseClockPortDSClockInstanceIndex_Object(
    (1, 3, 6, 1, 4, 1, 18837, 3, 5, 1, 2, 8, 1, 3),
    _PtpbaseClockPortDSClockInstanceIndex_Type()
)
ptpbaseClockPortDSClockInstanceIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ptpbaseClockPortDSClockInstanceIndex.setStatus("current")
_PtpbaseClockPortDSPortNumberIndex_Type = PtpClockPortNumber
_PtpbaseClockPortDSPortNumberIndex_Object = MibTableColumn
ptpbaseClockPortDSPortNumberIndex = _PtpbaseClockPortDSPortNumberIndex_Object(
    (1, 3, 6, 1, 4, 1, 18837, 3, 5, 1, 2, 8, 1, 4),
    _PtpbaseClockPortDSPortNumberIndex_Type()
)
ptpbaseClockPortDSPortNumberIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ptpbaseClockPortDSPortNumberIndex.setStatus("current")


class _PtpbaseClockPortDSName_Type(DisplayString):
    """Custom type ptpbaseClockPortDSName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_PtpbaseClockPortDSName_Type.__name__ = "DisplayString"
_PtpbaseClockPortDSName_Object = MibTableColumn
ptpbaseClockPortDSName = _PtpbaseClockPortDSName_Object(
    (1, 3, 6, 1, 4, 1, 18837, 3, 5, 1, 2, 8, 1, 5),
    _PtpbaseClockPortDSName_Type()
)
ptpbaseClockPortDSName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ptpbaseClockPortDSName.setStatus("current")


class _PtpbaseClockPortDSPortIdentity_Type(OctetString):
    """Custom type ptpbaseClockPortDSPortIdentity based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 256),
    )


_PtpbaseClockPortDSPortIdentity_Type.__name__ = "OctetString"
_PtpbaseClockPortDSPortIdentity_Object = MibTableColumn
ptpbaseClockPortDSPortIdentity = _PtpbaseClockPortDSPortIdentity_Object(
    (1, 3, 6, 1, 4, 1, 18837, 3, 5, 1, 2, 8, 1, 6),
    _PtpbaseClockPortDSPortIdentity_Type()
)
ptpbaseClockPortDSPortIdentity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ptpbaseClockPortDSPortIdentity.setStatus("current")
_PtpbaseClockPortDSlogAnnouncementInterval_Type = PtpClockIntervalBase2
_PtpbaseClockPortDSlogAnnouncementInterval_Object = MibTableColumn
ptpbaseClockPortDSlogAnnouncementInterval = _PtpbaseClockPortDSlogAnnouncementInterval_Object(
    (1, 3, 6, 1, 4, 1, 18837, 3, 5, 1, 2, 8, 1, 7),
    _PtpbaseClockPortDSlogAnnouncementInterval_Type()
)
ptpbaseClockPortDSlogAnnouncementInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ptpbaseClockPortDSlogAnnouncementInterval.setStatus("current")
if mibBuilder.loadTexts:
    ptpbaseClockPortDSlogAnnouncementInterval.setUnits("Time Interval")
_PtpbaseClockPortDSAnnounceRctTimeout_Type = Integer32
_PtpbaseClockPortDSAnnounceRctTimeout_Object = MibTableColumn
ptpbaseClockPortDSAnnounceRctTimeout = _PtpbaseClockPortDSAnnounceRctTimeout_Object(
    (1, 3, 6, 1, 4, 1, 18837, 3, 5, 1, 2, 8, 1, 8),
    _PtpbaseClockPortDSAnnounceRctTimeout_Type()
)
ptpbaseClockPortDSAnnounceRctTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ptpbaseClockPortDSAnnounceRctTimeout.setStatus("current")
_PtpbaseClockPortDSlogSyncInterval_Type = PtpClockIntervalBase2
_PtpbaseClockPortDSlogSyncInterval_Object = MibTableColumn
ptpbaseClockPortDSlogSyncInterval = _PtpbaseClockPortDSlogSyncInterval_Object(
    (1, 3, 6, 1, 4, 1, 18837, 3, 5, 1, 2, 8, 1, 9),
    _PtpbaseClockPortDSlogSyncInterval_Type()
)
ptpbaseClockPortDSlogSyncInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ptpbaseClockPortDSlogSyncInterval.setStatus("current")
if mibBuilder.loadTexts:
    ptpbaseClockPortDSlogSyncInterval.setUnits("Time Interval")
_PtpbaseClockPortDSMinDelayReqInterval_Type = Integer32
_PtpbaseClockPortDSMinDelayReqInterval_Object = MibTableColumn
ptpbaseClockPortDSMinDelayReqInterval = _PtpbaseClockPortDSMinDelayReqInterval_Object(
    (1, 3, 6, 1, 4, 1, 18837, 3, 5, 1, 2, 8, 1, 10),
    _PtpbaseClockPortDSMinDelayReqInterval_Type()
)
ptpbaseClockPortDSMinDelayReqInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ptpbaseClockPortDSMinDelayReqInterval.setStatus("current")
_PtpbaseClockPortDSPeerDelayReqInterval_Type = Integer32
_PtpbaseClockPortDSPeerDelayReqInterval_Object = MibTableColumn
ptpbaseClockPortDSPeerDelayReqInterval = _PtpbaseClockPortDSPeerDelayReqInterval_Object(
    (1, 3, 6, 1, 4, 1, 18837, 3, 5, 1, 2, 8, 1, 11),
    _PtpbaseClockPortDSPeerDelayReqInterval_Type()
)
ptpbaseClockPortDSPeerDelayReqInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ptpbaseClockPortDSPeerDelayReqInterval.setStatus("current")
_PtpbaseClockPortDSDelayMech_Type = PtpClockMechanismType
_PtpbaseClockPortDSDelayMech_Object = MibTableColumn
ptpbaseClockPortDSDelayMech = _PtpbaseClockPortDSDelayMech_Object(
    (1, 3, 6, 1, 4, 1, 18837, 3, 5, 1, 2, 8, 1, 12),
    _PtpbaseClockPortDSDelayMech_Type()
)
ptpbaseClockPortDSDelayMech.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ptpbaseClockPortDSDelayMech.setStatus("current")
_PtpbaseClockPortDSPeerMeanPathDelay_Type = PtpClockTimeInterval
_PtpbaseClockPortDSPeerMeanPathDelay_Object = MibTableColumn
ptpbaseClockPortDSPeerMeanPathDelay = _PtpbaseClockPortDSPeerMeanPathDelay_Object(
    (1, 3, 6, 1, 4, 1, 18837, 3, 5, 1, 2, 8, 1, 13),
    _PtpbaseClockPortDSPeerMeanPathDelay_Type()
)
ptpbaseClockPortDSPeerMeanPathDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ptpbaseClockPortDSPeerMeanPathDelay.setStatus("current")
if mibBuilder.loadTexts:
    ptpbaseClockPortDSPeerMeanPathDelay.setUnits("Time Interval")
_PtpbaseClockPortDSGrantDuration_Type = Unsigned32
_PtpbaseClockPortDSGrantDuration_Object = MibTableColumn
ptpbaseClockPortDSGrantDuration = _PtpbaseClockPortDSGrantDuration_Object(
    (1, 3, 6, 1, 4, 1, 18837, 3, 5, 1, 2, 8, 1, 14),
    _PtpbaseClockPortDSGrantDuration_Type()
)
ptpbaseClockPortDSGrantDuration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ptpbaseClockPortDSGrantDuration.setStatus("current")
if mibBuilder.loadTexts:
    ptpbaseClockPortDSGrantDuration.setUnits("seconds")
_PtpbaseClockPortDSPTPVersion_Type = Unsigned32
_PtpbaseClockPortDSPTPVersion_Object = MibTableColumn
ptpbaseClockPortDSPTPVersion = _PtpbaseClockPortDSPTPVersion_Object(
    (1, 3, 6, 1, 4, 1, 18837, 3, 5, 1, 2, 8, 1, 15),
    _PtpbaseClockPortDSPTPVersion_Type()
)
ptpbaseClockPortDSPTPVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ptpbaseClockPortDSPTPVersion.setStatus("current")
_PtpbaseClockPortRunningTable_Object = MibTable
ptpbaseClockPortRunningTable = _PtpbaseClockPortRunningTable_Object(
    (1, 3, 6, 1, 4, 1, 18837, 3, 5, 1, 2, 9)
)
if mibBuilder.loadTexts:
    ptpbaseClockPortRunningTable.setStatus("current")
_PtpbaseClockPortRunningEntry_Object = MibTableRow
ptpbaseClockPortRunningEntry = _PtpbaseClockPortRunningEntry_Object(
    (1, 3, 6, 1, 4, 1, 18837, 3, 5, 1, 2, 9, 1)
)
ptpbaseClockPortRunningEntry.setIndexNames(
    (0, "SPECTRACOM-PTPBASE-MIB", "ptpbaseClockPortRunningDomainIndex"),
    (0, "SPECTRACOM-PTPBASE-MIB", "ptpbaseClockPortRunningClockTypeIndex"),
    (0, "SPECTRACOM-PTPBASE-MIB", "ptpbaseClockPortRunningClockInstanceIndex"),
    (0, "SPECTRACOM-PTPBASE-MIB", "ptpbaseClockPortRunningPortNumberIndex"),
)
if mibBuilder.loadTexts:
    ptpbaseClockPortRunningEntry.setStatus("current")
_PtpbaseClockPortRunningDomainIndex_Type = PtpClockDomainType
_PtpbaseClockPortRunningDomainIndex_Object = MibTableColumn
ptpbaseClockPortRunningDomainIndex = _PtpbaseClockPortRunningDomainIndex_Object(
    (1, 3, 6, 1, 4, 1, 18837, 3, 5, 1, 2, 9, 1, 1),
    _PtpbaseClockPortRunningDomainIndex_Type()
)
ptpbaseClockPortRunningDomainIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ptpbaseClockPortRunningDomainIndex.setStatus("current")
_PtpbaseClockPortRunningClockTypeIndex_Type = PtpClockType
_PtpbaseClockPortRunningClockTypeIndex_Object = MibTableColumn
ptpbaseClockPortRunningClockTypeIndex = _PtpbaseClockPortRunningClockTypeIndex_Object(
    (1, 3, 6, 1, 4, 1, 18837, 3, 5, 1, 2, 9, 1, 2),
    _PtpbaseClockPortRunningClockTypeIndex_Type()
)
ptpbaseClockPortRunningClockTypeIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ptpbaseClockPortRunningClockTypeIndex.setStatus("current")
_PtpbaseClockPortRunningClockInstanceIndex_Type = PtpClockInstanceType
_PtpbaseClockPortRunningClockInstanceIndex_Object = MibTableColumn
ptpbaseClockPortRunningClockInstanceIndex = _PtpbaseClockPortRunningClockInstanceIndex_Object(
    (1, 3, 6, 1, 4, 1, 18837, 3, 5, 1, 2, 9, 1, 3),
    _PtpbaseClockPortRunningClockInstanceIndex_Type()
)
ptpbaseClockPortRunningClockInstanceIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ptpbaseClockPortRunningClockInstanceIndex.setStatus("current")
_PtpbaseClockPortRunningPortNumberIndex_Type = PtpClockPortNumber
_PtpbaseClockPortRunningPortNumberIndex_Object = MibTableColumn
ptpbaseClockPortRunningPortNumberIndex = _PtpbaseClockPortRunningPortNumberIndex_Object(
    (1, 3, 6, 1, 4, 1, 18837, 3, 5, 1, 2, 9, 1, 4),
    _PtpbaseClockPortRunningPortNumberIndex_Type()
)
ptpbaseClockPortRunningPortNumberIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ptpbaseClockPortRunningPortNumberIndex.setStatus("current")


class _PtpbaseClockPortRunningName_Type(DisplayString):
    """Custom type ptpbaseClockPortRunningName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_PtpbaseClockPortRunningName_Type.__name__ = "DisplayString"
_PtpbaseClockPortRunningName_Object = MibTableColumn
ptpbaseClockPortRunningName = _PtpbaseClockPortRunningName_Object(
    (1, 3, 6, 1, 4, 1, 18837, 3, 5, 1, 2, 9, 1, 5),
    _PtpbaseClockPortRunningName_Type()
)
ptpbaseClockPortRunningName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ptpbaseClockPortRunningName.setStatus("current")
_PtpbaseClockPortRunningState_Type = PtpClockPortState
_PtpbaseClockPortRunningState_Object = MibTableColumn
ptpbaseClockPortRunningState = _PtpbaseClockPortRunningState_Object(
    (1, 3, 6, 1, 4, 1, 18837, 3, 5, 1, 2, 9, 1, 6),
    _PtpbaseClockPortRunningState_Type()
)
ptpbaseClockPortRunningState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ptpbaseClockPortRunningState.setStatus("current")
_PtpbaseClockPortRunningRole_Type = PtpClockRoleType
_PtpbaseClockPortRunningRole_Object = MibTableColumn
ptpbaseClockPortRunningRole = _PtpbaseClockPortRunningRole_Object(
    (1, 3, 6, 1, 4, 1, 18837, 3, 5, 1, 2, 9, 1, 7),
    _PtpbaseClockPortRunningRole_Type()
)
ptpbaseClockPortRunningRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ptpbaseClockPortRunningRole.setStatus("current")
_PtpbaseClockPortRunningInterfaceIndex_Type = InterfaceIndexOrZero
_PtpbaseClockPortRunningInterfaceIndex_Object = MibTableColumn
ptpbaseClockPortRunningInterfaceIndex = _PtpbaseClockPortRunningInterfaceIndex_Object(
    (1, 3, 6, 1, 4, 1, 18837, 3, 5, 1, 2, 9, 1, 8),
    _PtpbaseClockPortRunningInterfaceIndex_Type()
)
ptpbaseClockPortRunningInterfaceIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ptpbaseClockPortRunningInterfaceIndex.setStatus("current")
_PtpbaseClockPortRunningTransport_Type = AutonomousType
_PtpbaseClockPortRunningTransport_Object = MibTableColumn
ptpbaseClockPortRunningTransport = _PtpbaseClockPortRunningTransport_Object(
    (1, 3, 6, 1, 4, 1, 18837, 3, 5, 1, 2, 9, 1, 9),
    _PtpbaseClockPortRunningTransport_Type()
)
ptpbaseClockPortRunningTransport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ptpbaseClockPortRunningTransport.setStatus("current")
_PtpbaseClockPortRunningEncapsulationType_Type = AutonomousType
_PtpbaseClockPortRunningEncapsulationType_Object = MibTableColumn
ptpbaseClockPortRunningEncapsulationType = _PtpbaseClockPortRunningEncapsulationType_Object(
    (1, 3, 6, 1, 4, 1, 18837, 3, 5, 1, 2, 9, 1, 10),
    _PtpbaseClockPortRunningEncapsulationType_Type()
)
ptpbaseClockPortRunningEncapsulationType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ptpbaseClockPortRunningEncapsulationType.setStatus("current")
_PtpbaseClockPortRunningTxMode_Type = PtpClockTxModeType
_PtpbaseClockPortRunningTxMode_Object = MibTableColumn
ptpbaseClockPortRunningTxMode = _PtpbaseClockPortRunningTxMode_Object(
    (1, 3, 6, 1, 4, 1, 18837, 3, 5, 1, 2, 9, 1, 11),
    _PtpbaseClockPortRunningTxMode_Type()
)
ptpbaseClockPortRunningTxMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ptpbaseClockPortRunningTxMode.setStatus("current")
_PtpbaseClockPortRunningRxMode_Type = PtpClockTxModeType
_PtpbaseClockPortRunningRxMode_Object = MibTableColumn
ptpbaseClockPortRunningRxMode = _PtpbaseClockPortRunningRxMode_Object(
    (1, 3, 6, 1, 4, 1, 18837, 3, 5, 1, 2, 9, 1, 12),
    _PtpbaseClockPortRunningRxMode_Type()
)
ptpbaseClockPortRunningRxMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ptpbaseClockPortRunningRxMode.setStatus("current")
_PtpbaseClockPortRunningPacketsReceived_Type = Counter64
_PtpbaseClockPortRunningPacketsReceived_Object = MibTableColumn
ptpbaseClockPortRunningPacketsReceived = _PtpbaseClockPortRunningPacketsReceived_Object(
    (1, 3, 6, 1, 4, 1, 18837, 3, 5, 1, 2, 9, 1, 13),
    _PtpbaseClockPortRunningPacketsReceived_Type()
)
ptpbaseClockPortRunningPacketsReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ptpbaseClockPortRunningPacketsReceived.setStatus("current")
if mibBuilder.loadTexts:
    ptpbaseClockPortRunningPacketsReceived.setUnits("packets")
_PtpbaseClockPortRunningPacketsSent_Type = Counter64
_PtpbaseClockPortRunningPacketsSent_Object = MibTableColumn
ptpbaseClockPortRunningPacketsSent = _PtpbaseClockPortRunningPacketsSent_Object(
    (1, 3, 6, 1, 4, 1, 18837, 3, 5, 1, 2, 9, 1, 14),
    _PtpbaseClockPortRunningPacketsSent_Type()
)
ptpbaseClockPortRunningPacketsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ptpbaseClockPortRunningPacketsSent.setStatus("current")
if mibBuilder.loadTexts:
    ptpbaseClockPortRunningPacketsSent.setUnits("packets")
_PtpbaseClockPortTransDSTable_Object = MibTable
ptpbaseClockPortTransDSTable = _PtpbaseClockPortTransDSTable_Object(
    (1, 3, 6, 1, 4, 1, 18837, 3, 5, 1, 2, 10)
)
if mibBuilder.loadTexts:
    ptpbaseClockPortTransDSTable.setStatus("current")
_PtpbaseClockPortTransDSEntry_Object = MibTableRow
ptpbaseClockPortTransDSEntry = _PtpbaseClockPortTransDSEntry_Object(
    (1, 3, 6, 1, 4, 1, 18837, 3, 5, 1, 2, 10, 1)
)
ptpbaseClockPortTransDSEntry.setIndexNames(
    (0, "SPECTRACOM-PTPBASE-MIB", "ptpbaseClockPortTransDSDomainIndex"),
    (0, "SPECTRACOM-PTPBASE-MIB", "ptpbaseClockPortTransDSInstanceIndex"),
    (0, "SPECTRACOM-PTPBASE-MIB", "ptpbaseClockPortTransDSPortNumberIndex"),
)
if mibBuilder.loadTexts:
    ptpbaseClockPortTransDSEntry.setStatus("current")
_PtpbaseClockPortTransDSDomainIndex_Type = PtpClockDomainType
_PtpbaseClockPortTransDSDomainIndex_Object = MibTableColumn
ptpbaseClockPortTransDSDomainIndex = _PtpbaseClockPortTransDSDomainIndex_Object(
    (1, 3, 6, 1, 4, 1, 18837, 3, 5, 1, 2, 10, 1, 1),
    _PtpbaseClockPortTransDSDomainIndex_Type()
)
ptpbaseClockPortTransDSDomainIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ptpbaseClockPortTransDSDomainIndex.setStatus("current")
_PtpbaseClockPortTransDSInstanceIndex_Type = PtpClockInstanceType
_PtpbaseClockPortTransDSInstanceIndex_Object = MibTableColumn
ptpbaseClockPortTransDSInstanceIndex = _PtpbaseClockPortTransDSInstanceIndex_Object(
    (1, 3, 6, 1, 4, 1, 18837, 3, 5, 1, 2, 10, 1, 2),
    _PtpbaseClockPortTransDSInstanceIndex_Type()
)
ptpbaseClockPortTransDSInstanceIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ptpbaseClockPortTransDSInstanceIndex.setStatus("current")
_PtpbaseClockPortTransDSPortNumberIndex_Type = PtpClockPortNumber
_PtpbaseClockPortTransDSPortNumberIndex_Object = MibTableColumn
ptpbaseClockPortTransDSPortNumberIndex = _PtpbaseClockPortTransDSPortNumberIndex_Object(
    (1, 3, 6, 1, 4, 1, 18837, 3, 5, 1, 2, 10, 1, 3),
    _PtpbaseClockPortTransDSPortNumberIndex_Type()
)
ptpbaseClockPortTransDSPortNumberIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ptpbaseClockPortTransDSPortNumberIndex.setStatus("current")
_PtpbaseClockPortTransDSPortIdentity_Type = PtpClockIdentity
_PtpbaseClockPortTransDSPortIdentity_Object = MibTableColumn
ptpbaseClockPortTransDSPortIdentity = _PtpbaseClockPortTransDSPortIdentity_Object(
    (1, 3, 6, 1, 4, 1, 18837, 3, 5, 1, 2, 10, 1, 4),
    _PtpbaseClockPortTransDSPortIdentity_Type()
)
ptpbaseClockPortTransDSPortIdentity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ptpbaseClockPortTransDSPortIdentity.setStatus("current")
_PtpbaseClockPortTransDSlogMinPdelayReqInt_Type = PtpClockIntervalBase2
_PtpbaseClockPortTransDSlogMinPdelayReqInt_Object = MibTableColumn
ptpbaseClockPortTransDSlogMinPdelayReqInt = _PtpbaseClockPortTransDSlogMinPdelayReqInt_Object(
    (1, 3, 6, 1, 4, 1, 18837, 3, 5, 1, 2, 10, 1, 5),
    _PtpbaseClockPortTransDSlogMinPdelayReqInt_Type()
)
ptpbaseClockPortTransDSlogMinPdelayReqInt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ptpbaseClockPortTransDSlogMinPdelayReqInt.setStatus("current")
_PtpbaseClockPortTransDSFaultyFlag_Type = TruthValue
_PtpbaseClockPortTransDSFaultyFlag_Object = MibTableColumn
ptpbaseClockPortTransDSFaultyFlag = _PtpbaseClockPortTransDSFaultyFlag_Object(
    (1, 3, 6, 1, 4, 1, 18837, 3, 5, 1, 2, 10, 1, 6),
    _PtpbaseClockPortTransDSFaultyFlag_Type()
)
ptpbaseClockPortTransDSFaultyFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ptpbaseClockPortTransDSFaultyFlag.setStatus("current")
_PtpbaseClockPortTransDSPeerMeanPathDelay_Type = PtpClockTimeInterval
_PtpbaseClockPortTransDSPeerMeanPathDelay_Object = MibTableColumn
ptpbaseClockPortTransDSPeerMeanPathDelay = _PtpbaseClockPortTransDSPeerMeanPathDelay_Object(
    (1, 3, 6, 1, 4, 1, 18837, 3, 5, 1, 2, 10, 1, 7),
    _PtpbaseClockPortTransDSPeerMeanPathDelay_Type()
)
ptpbaseClockPortTransDSPeerMeanPathDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ptpbaseClockPortTransDSPeerMeanPathDelay.setStatus("current")
if mibBuilder.loadTexts:
    ptpbaseClockPortTransDSPeerMeanPathDelay.setUnits("Time Interval")
_PtpbaseClockPortAssociateTable_Object = MibTable
ptpbaseClockPortAssociateTable = _PtpbaseClockPortAssociateTable_Object(
    (1, 3, 6, 1, 4, 1, 18837, 3, 5, 1, 2, 11)
)
if mibBuilder.loadTexts:
    ptpbaseClockPortAssociateTable.setStatus("current")
_PtpbaseClockPortAssociateEntry_Object = MibTableRow
ptpbaseClockPortAssociateEntry = _PtpbaseClockPortAssociateEntry_Object(
    (1, 3, 6, 1, 4, 1, 18837, 3, 5, 1, 2, 11, 1)
)
ptpbaseClockPortAssociateEntry.setIndexNames(
    (0, "SPECTRACOM-PTPBASE-MIB", "ptpClockPortCurrentDomainIndex"),
    (0, "SPECTRACOM-PTPBASE-MIB", "ptpClockPortCurrentClockTypeIndex"),
    (0, "SPECTRACOM-PTPBASE-MIB", "ptpClockPortCurrentClockInstanceIndex"),
    (0, "SPECTRACOM-PTPBASE-MIB", "ptpClockPortCurrentPortNumberIndex"),
    (0, "SPECTRACOM-PTPBASE-MIB", "ptpbaseClockPortAssociatePortIndex"),
)
if mibBuilder.loadTexts:
    ptpbaseClockPortAssociateEntry.setStatus("current")
_PtpClockPortCurrentDomainIndex_Type = PtpClockDomainType
_PtpClockPortCurrentDomainIndex_Object = MibTableColumn
ptpClockPortCurrentDomainIndex = _PtpClockPortCurrentDomainIndex_Object(
    (1, 3, 6, 1, 4, 1, 18837, 3, 5, 1, 2, 11, 1, 1),
    _PtpClockPortCurrentDomainIndex_Type()
)
ptpClockPortCurrentDomainIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ptpClockPortCurrentDomainIndex.setStatus("current")
_PtpClockPortCurrentClockTypeIndex_Type = PtpClockType
_PtpClockPortCurrentClockTypeIndex_Object = MibTableColumn
ptpClockPortCurrentClockTypeIndex = _PtpClockPortCurrentClockTypeIndex_Object(
    (1, 3, 6, 1, 4, 1, 18837, 3, 5, 1, 2, 11, 1, 2),
    _PtpClockPortCurrentClockTypeIndex_Type()
)
ptpClockPortCurrentClockTypeIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ptpClockPortCurrentClockTypeIndex.setStatus("current")
_PtpClockPortCurrentClockInstanceIndex_Type = PtpClockInstanceType
_PtpClockPortCurrentClockInstanceIndex_Object = MibTableColumn
ptpClockPortCurrentClockInstanceIndex = _PtpClockPortCurrentClockInstanceIndex_Object(
    (1, 3, 6, 1, 4, 1, 18837, 3, 5, 1, 2, 11, 1, 3),
    _PtpClockPortCurrentClockInstanceIndex_Type()
)
ptpClockPortCurrentClockInstanceIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ptpClockPortCurrentClockInstanceIndex.setStatus("current")
_PtpClockPortCurrentPortNumberIndex_Type = PtpClockPortNumber
_PtpClockPortCurrentPortNumberIndex_Object = MibTableColumn
ptpClockPortCurrentPortNumberIndex = _PtpClockPortCurrentPortNumberIndex_Object(
    (1, 3, 6, 1, 4, 1, 18837, 3, 5, 1, 2, 11, 1, 4),
    _PtpClockPortCurrentPortNumberIndex_Type()
)
ptpClockPortCurrentPortNumberIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ptpClockPortCurrentPortNumberIndex.setStatus("current")


class _PtpbaseClockPortAssociatePortIndex_Type(Unsigned32):
    """Custom type ptpbaseClockPortAssociatePortIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_PtpbaseClockPortAssociatePortIndex_Type.__name__ = "Unsigned32"
_PtpbaseClockPortAssociatePortIndex_Object = MibTableColumn
ptpbaseClockPortAssociatePortIndex = _PtpbaseClockPortAssociatePortIndex_Object(
    (1, 3, 6, 1, 4, 1, 18837, 3, 5, 1, 2, 11, 1, 5),
    _PtpbaseClockPortAssociatePortIndex_Type()
)
ptpbaseClockPortAssociatePortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ptpbaseClockPortAssociatePortIndex.setStatus("current")
_PtpbaseClockPortAssociateAddressType_Type = AutonomousType
_PtpbaseClockPortAssociateAddressType_Object = MibTableColumn
ptpbaseClockPortAssociateAddressType = _PtpbaseClockPortAssociateAddressType_Object(
    (1, 3, 6, 1, 4, 1, 18837, 3, 5, 1, 2, 11, 1, 6),
    _PtpbaseClockPortAssociateAddressType_Type()
)
ptpbaseClockPortAssociateAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ptpbaseClockPortAssociateAddressType.setStatus("current")
_PtpbaseClockPortAssociateAddress_Type = PtpClockPortTransportTypeAddress
_PtpbaseClockPortAssociateAddress_Object = MibTableColumn
ptpbaseClockPortAssociateAddress = _PtpbaseClockPortAssociateAddress_Object(
    (1, 3, 6, 1, 4, 1, 18837, 3, 5, 1, 2, 11, 1, 7),
    _PtpbaseClockPortAssociateAddress_Type()
)
ptpbaseClockPortAssociateAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ptpbaseClockPortAssociateAddress.setStatus("current")
_PtpbaseClockPortAssociatePacketsSent_Type = Counter64
_PtpbaseClockPortAssociatePacketsSent_Object = MibTableColumn
ptpbaseClockPortAssociatePacketsSent = _PtpbaseClockPortAssociatePacketsSent_Object(
    (1, 3, 6, 1, 4, 1, 18837, 3, 5, 1, 2, 11, 1, 8),
    _PtpbaseClockPortAssociatePacketsSent_Type()
)
ptpbaseClockPortAssociatePacketsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ptpbaseClockPortAssociatePacketsSent.setStatus("current")
if mibBuilder.loadTexts:
    ptpbaseClockPortAssociatePacketsSent.setUnits("packets")
_PtpbaseClockPortAssociatePacketsReceived_Type = Counter64
_PtpbaseClockPortAssociatePacketsReceived_Object = MibTableColumn
ptpbaseClockPortAssociatePacketsReceived = _PtpbaseClockPortAssociatePacketsReceived_Object(
    (1, 3, 6, 1, 4, 1, 18837, 3, 5, 1, 2, 11, 1, 9),
    _PtpbaseClockPortAssociatePacketsReceived_Type()
)
ptpbaseClockPortAssociatePacketsReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ptpbaseClockPortAssociatePacketsReceived.setStatus("current")
if mibBuilder.loadTexts:
    ptpbaseClockPortAssociatePacketsReceived.setUnits("packets")
_PtpbaseClockPortAssociateInErrors_Type = Counter64
_PtpbaseClockPortAssociateInErrors_Object = MibTableColumn
ptpbaseClockPortAssociateInErrors = _PtpbaseClockPortAssociateInErrors_Object(
    (1, 3, 6, 1, 4, 1, 18837, 3, 5, 1, 2, 11, 1, 10),
    _PtpbaseClockPortAssociateInErrors_Type()
)
ptpbaseClockPortAssociateInErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ptpbaseClockPortAssociateInErrors.setStatus("current")
if mibBuilder.loadTexts:
    ptpbaseClockPortAssociateInErrors.setUnits("packets")
_PtpbaseClockPortAssociateOutErrors_Type = Counter64
_PtpbaseClockPortAssociateOutErrors_Object = MibTableColumn
ptpbaseClockPortAssociateOutErrors = _PtpbaseClockPortAssociateOutErrors_Object(
    (1, 3, 6, 1, 4, 1, 18837, 3, 5, 1, 2, 11, 1, 11),
    _PtpbaseClockPortAssociateOutErrors_Type()
)
ptpbaseClockPortAssociateOutErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ptpbaseClockPortAssociateOutErrors.setStatus("current")
if mibBuilder.loadTexts:
    ptpbaseClockPortAssociateOutErrors.setUnits("packets")
_PtpbaseWellKnownTransportTypes_ObjectIdentity = ObjectIdentity
ptpbaseWellKnownTransportTypes = _PtpbaseWellKnownTransportTypes_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18837, 3, 5, 1, 2, 12)
)
_PtpbaseTransportTypeIPversion4_ObjectIdentity = ObjectIdentity
ptpbaseTransportTypeIPversion4 = _PtpbaseTransportTypeIPversion4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18837, 3, 5, 1, 2, 12, 1)
)
if mibBuilder.loadTexts:
    ptpbaseTransportTypeIPversion4.setStatus("current")
_PtpbaseTransportTypeIPversion6_ObjectIdentity = ObjectIdentity
ptpbaseTransportTypeIPversion6 = _PtpbaseTransportTypeIPversion6_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18837, 3, 5, 1, 2, 12, 2)
)
if mibBuilder.loadTexts:
    ptpbaseTransportTypeIPversion6.setStatus("current")
_PtpbaseTransportTypeEthernet_ObjectIdentity = ObjectIdentity
ptpbaseTransportTypeEthernet = _PtpbaseTransportTypeEthernet_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18837, 3, 5, 1, 2, 12, 3)
)
if mibBuilder.loadTexts:
    ptpbaseTransportTypeEthernet.setStatus("current")
_PtpbaseTransportTypeDeviceNET_ObjectIdentity = ObjectIdentity
ptpbaseTransportTypeDeviceNET = _PtpbaseTransportTypeDeviceNET_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18837, 3, 5, 1, 2, 12, 4)
)
if mibBuilder.loadTexts:
    ptpbaseTransportTypeDeviceNET.setStatus("current")
_PtpbaseTransportTypeControlNET_ObjectIdentity = ObjectIdentity
ptpbaseTransportTypeControlNET = _PtpbaseTransportTypeControlNET_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18837, 3, 5, 1, 2, 12, 5)
)
if mibBuilder.loadTexts:
    ptpbaseTransportTypeControlNET.setStatus("current")
_PtpbaseTransportTypeIEC61158_ObjectIdentity = ObjectIdentity
ptpbaseTransportTypeIEC61158 = _PtpbaseTransportTypeIEC61158_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18837, 3, 5, 1, 2, 12, 6)
)
if mibBuilder.loadTexts:
    ptpbaseTransportTypeIEC61158.setStatus("current")
_PtpbaseWellKnownEncapsulationTypes_ObjectIdentity = ObjectIdentity
ptpbaseWellKnownEncapsulationTypes = _PtpbaseWellKnownEncapsulationTypes_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18837, 3, 5, 1, 2, 13)
)
_PtpbaseEncapsulationTypeEthernet_ObjectIdentity = ObjectIdentity
ptpbaseEncapsulationTypeEthernet = _PtpbaseEncapsulationTypeEthernet_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18837, 3, 5, 1, 2, 13, 1)
)
if mibBuilder.loadTexts:
    ptpbaseEncapsulationTypeEthernet.setStatus("current")
_PtpbaseEncapsulationTypeVLAN_ObjectIdentity = ObjectIdentity
ptpbaseEncapsulationTypeVLAN = _PtpbaseEncapsulationTypeVLAN_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18837, 3, 5, 1, 2, 13, 2)
)
if mibBuilder.loadTexts:
    ptpbaseEncapsulationTypeVLAN.setStatus("current")
_PtpbaseEncapsulationTypeUDPIPLSP_ObjectIdentity = ObjectIdentity
ptpbaseEncapsulationTypeUDPIPLSP = _PtpbaseEncapsulationTypeUDPIPLSP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18837, 3, 5, 1, 2, 13, 3)
)
if mibBuilder.loadTexts:
    ptpbaseEncapsulationTypeUDPIPLSP.setStatus("current")
_PtpbaseEncapsulationTypePWUDPIPLSP_ObjectIdentity = ObjectIdentity
ptpbaseEncapsulationTypePWUDPIPLSP = _PtpbaseEncapsulationTypePWUDPIPLSP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18837, 3, 5, 1, 2, 13, 4)
)
if mibBuilder.loadTexts:
    ptpbaseEncapsulationTypePWUDPIPLSP.setStatus("current")
_PtpbaseEncapsulationTypePWEthernetLSP_ObjectIdentity = ObjectIdentity
ptpbaseEncapsulationTypePWEthernetLSP = _PtpbaseEncapsulationTypePWEthernetLSP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18837, 3, 5, 1, 2, 13, 5)
)
if mibBuilder.loadTexts:
    ptpbaseEncapsulationTypePWEthernetLSP.setStatus("current")
_PtpbaseMIBConformance_ObjectIdentity = ObjectIdentity
ptpbaseMIBConformance = _PtpbaseMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18837, 3, 5, 2)
)
_PtpbaseMIBCompliances_ObjectIdentity = ObjectIdentity
ptpbaseMIBCompliances = _PtpbaseMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18837, 3, 5, 2, 1)
)
_PtpbaseMIBGroups_ObjectIdentity = ObjectIdentity
ptpbaseMIBGroups = _PtpbaseMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18837, 3, 5, 2, 2)
)

# Managed Objects groups

ptpbaseMIBSystemInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 18837, 3, 5, 2, 2, 1)
)
ptpbaseMIBSystemInfoGroup.setObjects(
      *(("SPECTRACOM-PTPBASE-MIB", "ptpbaseSystemDomainTotals"),
        ("SPECTRACOM-PTPBASE-MIB", "ptpDomainClockPortsTotal"),
        ("SPECTRACOM-PTPBASE-MIB", "ptpbaseSystemProfile"))
)
if mibBuilder.loadTexts:
    ptpbaseMIBSystemInfoGroup.setStatus("current")

ptpbaseMIBClockCurrentDSGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 18837, 3, 5, 2, 2, 2)
)
ptpbaseMIBClockCurrentDSGroup.setObjects(
      *(("SPECTRACOM-PTPBASE-MIB", "ptpbaseClockCurrentDSStepsRemoved"),
        ("SPECTRACOM-PTPBASE-MIB", "ptpbaseClockCurrentDSOffsetFromMaster"),
        ("SPECTRACOM-PTPBASE-MIB", "ptpbaseClockCurrentDSMeanPathDelay"))
)
if mibBuilder.loadTexts:
    ptpbaseMIBClockCurrentDSGroup.setStatus("current")

ptpbaseMIBClockParentDSGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 18837, 3, 5, 2, 2, 3)
)
ptpbaseMIBClockParentDSGroup.setObjects(
      *(("SPECTRACOM-PTPBASE-MIB", "ptpbaseClockParentDSParentPortIdentity"),
        ("SPECTRACOM-PTPBASE-MIB", "ptpbaseClockParentDSParentStats"),
        ("SPECTRACOM-PTPBASE-MIB", "ptpbaseClockParentDSOffset"),
        ("SPECTRACOM-PTPBASE-MIB", "ptpbaseClockParentDSClockPhChRate"),
        ("SPECTRACOM-PTPBASE-MIB", "ptpbaseClockParentDSGMClockIdentity"),
        ("SPECTRACOM-PTPBASE-MIB", "ptpbaseClockParentDSGMClockPriority1"),
        ("SPECTRACOM-PTPBASE-MIB", "ptpbaseClockParentDSGMClockPriority2"),
        ("SPECTRACOM-PTPBASE-MIB", "ptpbaseClockParentDSGMClockQualityClass"),
        ("SPECTRACOM-PTPBASE-MIB", "ptpbaseClockParentDSGMClockQualityAccuracy"),
        ("SPECTRACOM-PTPBASE-MIB", "ptpbaseClockParentDSGMClockQualityOffset"))
)
if mibBuilder.loadTexts:
    ptpbaseMIBClockParentDSGroup.setStatus("current")

ptpbaseMIBClockDefaultDSGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 18837, 3, 5, 2, 2, 4)
)
ptpbaseMIBClockDefaultDSGroup.setObjects(
      *(("SPECTRACOM-PTPBASE-MIB", "ptpbaseClockDefaultDSTwoStepFlag"),
        ("SPECTRACOM-PTPBASE-MIB", "ptpbaseClockDefaultDSClockIdentity"),
        ("SPECTRACOM-PTPBASE-MIB", "ptpbaseClockDefaultDSPriority1"),
        ("SPECTRACOM-PTPBASE-MIB", "ptpbaseClockDefaultDSPriority2"),
        ("SPECTRACOM-PTPBASE-MIB", "ptpbaseClockDefaultDSSlaveOnly"),
        ("SPECTRACOM-PTPBASE-MIB", "ptpbaseClockDefaultDSQualityClass"),
        ("SPECTRACOM-PTPBASE-MIB", "ptpbaseClockDefaultDSQualityAccuracy"),
        ("SPECTRACOM-PTPBASE-MIB", "ptpbaseClockDefaultDSQualityOffset"))
)
if mibBuilder.loadTexts:
    ptpbaseMIBClockDefaultDSGroup.setStatus("current")

ptpbaseMIBClockRunningGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 18837, 3, 5, 2, 2, 5)
)
ptpbaseMIBClockRunningGroup.setObjects(
      *(("SPECTRACOM-PTPBASE-MIB", "ptpbaseClockRunningState"),
        ("SPECTRACOM-PTPBASE-MIB", "ptpbaseClockRunningPacketsSent"),
        ("SPECTRACOM-PTPBASE-MIB", "ptpbaseClockRunningPacketsReceived"))
)
if mibBuilder.loadTexts:
    ptpbaseMIBClockRunningGroup.setStatus("current")

ptpbaseMIBClockTimepropertiesGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 18837, 3, 5, 2, 2, 6)
)
ptpbaseMIBClockTimepropertiesGroup.setObjects(
      *(("SPECTRACOM-PTPBASE-MIB", "ptpbaseClockTimePropertiesDSCurrentUTCOffsetValid"),
        ("SPECTRACOM-PTPBASE-MIB", "ptpbaseClockTimePropertiesDSCurrentUTCOffset"),
        ("SPECTRACOM-PTPBASE-MIB", "ptpbaseClockTimePropertiesDSLeap59"),
        ("SPECTRACOM-PTPBASE-MIB", "ptpbaseClockTimePropertiesDSLeap61"),
        ("SPECTRACOM-PTPBASE-MIB", "ptpbaseClockTimePropertiesDSTimeTraceable"),
        ("SPECTRACOM-PTPBASE-MIB", "ptpbaseClockTimePropertiesDSFreqTraceable"),
        ("SPECTRACOM-PTPBASE-MIB", "ptpbaseClockTimePropertiesDSPTPTimescale"),
        ("SPECTRACOM-PTPBASE-MIB", "ptpbaseClockTimePropertiesDSSource"))
)
if mibBuilder.loadTexts:
    ptpbaseMIBClockTimepropertiesGroup.setStatus("current")

ptpbaseMIBClockTranparentDSGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 18837, 3, 5, 2, 2, 7)
)
ptpbaseMIBClockTranparentDSGroup.setObjects(
      *(("SPECTRACOM-PTPBASE-MIB", "ptpbaseClockTransDefaultDSClockIdentity"),
        ("SPECTRACOM-PTPBASE-MIB", "ptpbaseClockTransDefaultDSNumOfPorts"),
        ("SPECTRACOM-PTPBASE-MIB", "ptpbaseClockTransDefaultDSDelay"),
        ("SPECTRACOM-PTPBASE-MIB", "ptpbaseClockTransDefaultDSPrimaryDomain"))
)
if mibBuilder.loadTexts:
    ptpbaseMIBClockTranparentDSGroup.setStatus("current")

ptpbaseMIBClockPortGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 18837, 3, 5, 2, 2, 8)
)
ptpbaseMIBClockPortGroup.setObjects(
      *(("SPECTRACOM-PTPBASE-MIB", "ptpbaseClockPortName"),
        ("SPECTRACOM-PTPBASE-MIB", "ptpbaseClockPortSyncTwoStep"),
        ("SPECTRACOM-PTPBASE-MIB", "ptpbaseClockPortCurrentPeerAddress"),
        ("SPECTRACOM-PTPBASE-MIB", "ptpbaseClockPortNumOfAssociatedPorts"),
        ("SPECTRACOM-PTPBASE-MIB", "ptpbaseClockPortCurrentPeerAddressType"),
        ("SPECTRACOM-PTPBASE-MIB", "ptpbaseClockPortRole"))
)
if mibBuilder.loadTexts:
    ptpbaseMIBClockPortGroup.setStatus("current")

ptpbaseMIBClockPortDSGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 18837, 3, 5, 2, 2, 9)
)
ptpbaseMIBClockPortDSGroup.setObjects(
      *(("SPECTRACOM-PTPBASE-MIB", "ptpbaseClockPortDSName"),
        ("SPECTRACOM-PTPBASE-MIB", "ptpbaseClockPortDSPortIdentity"),
        ("SPECTRACOM-PTPBASE-MIB", "ptpbaseClockPortDSlogAnnouncementInterval"),
        ("SPECTRACOM-PTPBASE-MIB", "ptpbaseClockPortDSAnnounceRctTimeout"),
        ("SPECTRACOM-PTPBASE-MIB", "ptpbaseClockPortDSlogSyncInterval"),
        ("SPECTRACOM-PTPBASE-MIB", "ptpbaseClockPortDSMinDelayReqInterval"),
        ("SPECTRACOM-PTPBASE-MIB", "ptpbaseClockPortDSPeerDelayReqInterval"),
        ("SPECTRACOM-PTPBASE-MIB", "ptpbaseClockPortDSDelayMech"),
        ("SPECTRACOM-PTPBASE-MIB", "ptpbaseClockPortDSPeerMeanPathDelay"),
        ("SPECTRACOM-PTPBASE-MIB", "ptpbaseClockPortDSGrantDuration"),
        ("SPECTRACOM-PTPBASE-MIB", "ptpbaseClockPortDSPTPVersion"))
)
if mibBuilder.loadTexts:
    ptpbaseMIBClockPortDSGroup.setStatus("current")

ptpbaseMIBClockPortRunningGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 18837, 3, 5, 2, 2, 10)
)
ptpbaseMIBClockPortRunningGroup.setObjects(
      *(("SPECTRACOM-PTPBASE-MIB", "ptpbaseClockPortRunningName"),
        ("SPECTRACOM-PTPBASE-MIB", "ptpbaseClockPortRunningState"),
        ("SPECTRACOM-PTPBASE-MIB", "ptpbaseClockPortRunningRole"),
        ("SPECTRACOM-PTPBASE-MIB", "ptpbaseClockPortRunningInterfaceIndex"),
        ("SPECTRACOM-PTPBASE-MIB", "ptpbaseClockPortRunningTransport"),
        ("SPECTRACOM-PTPBASE-MIB", "ptpbaseClockPortRunningEncapsulationType"),
        ("SPECTRACOM-PTPBASE-MIB", "ptpbaseClockPortRunningTxMode"),
        ("SPECTRACOM-PTPBASE-MIB", "ptpbaseClockPortRunningRxMode"),
        ("SPECTRACOM-PTPBASE-MIB", "ptpbaseClockPortRunningPacketsReceived"),
        ("SPECTRACOM-PTPBASE-MIB", "ptpbaseClockPortRunningPacketsSent"))
)
if mibBuilder.loadTexts:
    ptpbaseMIBClockPortRunningGroup.setStatus("current")

ptpbaseMIBClockPortTransDSGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 18837, 3, 5, 2, 2, 11)
)
ptpbaseMIBClockPortTransDSGroup.setObjects(
      *(("SPECTRACOM-PTPBASE-MIB", "ptpbaseClockPortTransDSPortIdentity"),
        ("SPECTRACOM-PTPBASE-MIB", "ptpbaseClockPortTransDSlogMinPdelayReqInt"),
        ("SPECTRACOM-PTPBASE-MIB", "ptpbaseClockPortTransDSFaultyFlag"),
        ("SPECTRACOM-PTPBASE-MIB", "ptpbaseClockPortTransDSPeerMeanPathDelay"))
)
if mibBuilder.loadTexts:
    ptpbaseMIBClockPortTransDSGroup.setStatus("current")

ptpbaseMIBClockPortAssociateGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 18837, 3, 5, 2, 2, 12)
)
ptpbaseMIBClockPortAssociateGroup.setObjects(
      *(("SPECTRACOM-PTPBASE-MIB", "ptpbaseClockPortAssociatePacketsSent"),
        ("SPECTRACOM-PTPBASE-MIB", "ptpbaseClockPortAssociatePacketsReceived"),
        ("SPECTRACOM-PTPBASE-MIB", "ptpbaseClockPortAssociateAddress"),
        ("SPECTRACOM-PTPBASE-MIB", "ptpbaseClockPortAssociateAddressType"),
        ("SPECTRACOM-PTPBASE-MIB", "ptpbaseClockPortAssociateInErrors"),
        ("SPECTRACOM-PTPBASE-MIB", "ptpbaseClockPortAssociateOutErrors"))
)
if mibBuilder.loadTexts:
    ptpbaseMIBClockPortAssociateGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

ptpbaseMIBCompliancesSystemInfo = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 18837, 3, 5, 2, 1, 1)
)
ptpbaseMIBCompliancesSystemInfo.setObjects(
    ("SPECTRACOM-PTPBASE-MIB", "ptpbaseMIBSystemInfoGroup")
)
if mibBuilder.loadTexts:
    ptpbaseMIBCompliancesSystemInfo.setStatus(
        "current"
    )

ptpbaseMIBCompliancesClockInfo = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 18837, 3, 5, 2, 1, 2)
)
ptpbaseMIBCompliancesClockInfo.setObjects(
      *(("SPECTRACOM-PTPBASE-MIB", "ptpbaseMIBClockCurrentDSGroup"),
        ("SPECTRACOM-PTPBASE-MIB", "ptpbaseMIBClockParentDSGroup"),
        ("SPECTRACOM-PTPBASE-MIB", "ptpbaseMIBClockDefaultDSGroup"),
        ("SPECTRACOM-PTPBASE-MIB", "ptpbaseMIBClockRunningGroup"),
        ("SPECTRACOM-PTPBASE-MIB", "ptpbaseMIBClockTimepropertiesGroup"))
)
if mibBuilder.loadTexts:
    ptpbaseMIBCompliancesClockInfo.setStatus(
        "current"
    )

ptpbaseMIBCompliancesClockPortInfo = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 18837, 3, 5, 2, 1, 3)
)
ptpbaseMIBCompliancesClockPortInfo.setObjects(
      *(("SPECTRACOM-PTPBASE-MIB", "ptpbaseMIBClockPortGroup"),
        ("SPECTRACOM-PTPBASE-MIB", "ptpbaseMIBClockPortDSGroup"),
        ("SPECTRACOM-PTPBASE-MIB", "ptpbaseMIBClockPortRunningGroup"),
        ("SPECTRACOM-PTPBASE-MIB", "ptpbaseMIBClockPortAssociateGroup"))
)
if mibBuilder.loadTexts:
    ptpbaseMIBCompliancesClockPortInfo.setStatus(
        "current"
    )

ptpbaseMIBCompliancesTransparentClockInfo = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 18837, 3, 5, 2, 1, 4)
)
ptpbaseMIBCompliancesTransparentClockInfo.setObjects(
      *(("SPECTRACOM-PTPBASE-MIB", "ptpbaseMIBClockTranparentDSGroup"),
        ("SPECTRACOM-PTPBASE-MIB", "ptpbaseMIBClockPortTransDSGroup"))
)
if mibBuilder.loadTexts:
    ptpbaseMIBCompliancesTransparentClockInfo.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SPECTRACOM-PTPBASE-MIB",
    **{"PtpClockDomainType": PtpClockDomainType,
       "PtpClockIdentity": PtpClockIdentity,
       "PtpClockInstanceType": PtpClockInstanceType,
       "PtpClockIntervalBase2": PtpClockIntervalBase2,
       "PtpClockMechanismType": PtpClockMechanismType,
       "PtpClockPortNumber": PtpClockPortNumber,
       "PtpClockPortState": PtpClockPortState,
       "PtpClockPortTransportTypeAddress": PtpClockPortTransportTypeAddress,
       "PtpClockProfileType": PtpClockProfileType,
       "PtpClockQualityAccuracyType": PtpClockQualityAccuracyType,
       "PtpClockQualityClassType": PtpClockQualityClassType,
       "PtpClockRoleType": PtpClockRoleType,
       "PtpClockStateType": PtpClockStateType,
       "PtpClockTimeInterval": PtpClockTimeInterval,
       "PtpClockTimeSourceType": PtpClockTimeSourceType,
       "PtpClockTxModeType": PtpClockTxModeType,
       "PtpClockType": PtpClockType,
       "ptpbaseMIB": ptpbaseMIB,
       "ptpbaseSnmpObjs": ptpbaseSnmpObjs,
       "ptpbaseMIBNotifs": ptpbaseMIBNotifs,
       "ptpbaseMIBObjects": ptpbaseMIBObjects,
       "ptpbaseMIBSystemInfo": ptpbaseMIBSystemInfo,
       "ptpbaseSystemTable": ptpbaseSystemTable,
       "ptpbaseSystemEntry": ptpbaseSystemEntry,
       "ptpDomainIndex": ptpDomainIndex,
       "ptpInstanceIndex": ptpInstanceIndex,
       "ptpDomainClockPortsTotal": ptpDomainClockPortsTotal,
       "ptpbaseSystemDomainTable": ptpbaseSystemDomainTable,
       "ptpbaseSystemDomainEntry": ptpbaseSystemDomainEntry,
       "ptpbaseSystemDomainClockTypeIndex": ptpbaseSystemDomainClockTypeIndex,
       "ptpbaseSystemDomainTotals": ptpbaseSystemDomainTotals,
       "ptpbaseSystemProfile": ptpbaseSystemProfile,
       "ptpbaseMIBClockInfo": ptpbaseMIBClockInfo,
       "ptpbaseClockCurrentDSTable": ptpbaseClockCurrentDSTable,
       "ptpbaseClockCurrentDSEntry": ptpbaseClockCurrentDSEntry,
       "ptpbaseClockCurrentDSDomainIndex": ptpbaseClockCurrentDSDomainIndex,
       "ptpbaseClockCurrentDSClockTypeIndex": ptpbaseClockCurrentDSClockTypeIndex,
       "ptpbaseClockCurrentDSInstanceIndex": ptpbaseClockCurrentDSInstanceIndex,
       "ptpbaseClockCurrentDSStepsRemoved": ptpbaseClockCurrentDSStepsRemoved,
       "ptpbaseClockCurrentDSOffsetFromMaster": ptpbaseClockCurrentDSOffsetFromMaster,
       "ptpbaseClockCurrentDSMeanPathDelay": ptpbaseClockCurrentDSMeanPathDelay,
       "ptpbaseClockParentDSTable": ptpbaseClockParentDSTable,
       "ptpbaseClockParentDSEntry": ptpbaseClockParentDSEntry,
       "ptpbaseClockParentDSDomainIndex": ptpbaseClockParentDSDomainIndex,
       "ptpbaseClockParentDSClockTypeIndex": ptpbaseClockParentDSClockTypeIndex,
       "ptpbaseClockParentDSInstanceIndex": ptpbaseClockParentDSInstanceIndex,
       "ptpbaseClockParentDSParentPortIdentity": ptpbaseClockParentDSParentPortIdentity,
       "ptpbaseClockParentDSParentStats": ptpbaseClockParentDSParentStats,
       "ptpbaseClockParentDSOffset": ptpbaseClockParentDSOffset,
       "ptpbaseClockParentDSClockPhChRate": ptpbaseClockParentDSClockPhChRate,
       "ptpbaseClockParentDSGMClockIdentity": ptpbaseClockParentDSGMClockIdentity,
       "ptpbaseClockParentDSGMClockPriority1": ptpbaseClockParentDSGMClockPriority1,
       "ptpbaseClockParentDSGMClockPriority2": ptpbaseClockParentDSGMClockPriority2,
       "ptpbaseClockParentDSGMClockQualityClass": ptpbaseClockParentDSGMClockQualityClass,
       "ptpbaseClockParentDSGMClockQualityAccuracy": ptpbaseClockParentDSGMClockQualityAccuracy,
       "ptpbaseClockParentDSGMClockQualityOffset": ptpbaseClockParentDSGMClockQualityOffset,
       "ptpbaseClockDefaultDSTable": ptpbaseClockDefaultDSTable,
       "ptpbaseClockDefaultDSEntry": ptpbaseClockDefaultDSEntry,
       "ptpbaseClockDefaultDSDomainIndex": ptpbaseClockDefaultDSDomainIndex,
       "ptpbaseClockDefaultDSClockTypeIndex": ptpbaseClockDefaultDSClockTypeIndex,
       "ptpbaseClockDefaultDSInstanceIndex": ptpbaseClockDefaultDSInstanceIndex,
       "ptpbaseClockDefaultDSTwoStepFlag": ptpbaseClockDefaultDSTwoStepFlag,
       "ptpbaseClockDefaultDSClockIdentity": ptpbaseClockDefaultDSClockIdentity,
       "ptpbaseClockDefaultDSPriority1": ptpbaseClockDefaultDSPriority1,
       "ptpbaseClockDefaultDSPriority2": ptpbaseClockDefaultDSPriority2,
       "ptpbaseClockDefaultDSSlaveOnly": ptpbaseClockDefaultDSSlaveOnly,
       "ptpbaseClockDefaultDSQualityClass": ptpbaseClockDefaultDSQualityClass,
       "ptpbaseClockDefaultDSQualityAccuracy": ptpbaseClockDefaultDSQualityAccuracy,
       "ptpbaseClockDefaultDSQualityOffset": ptpbaseClockDefaultDSQualityOffset,
       "ptpbaseClockRunningTable": ptpbaseClockRunningTable,
       "ptpbaseClockRunningEntry": ptpbaseClockRunningEntry,
       "ptpbaseClockRunningDomainIndex": ptpbaseClockRunningDomainIndex,
       "ptpbaseClockRunningClockTypeIndex": ptpbaseClockRunningClockTypeIndex,
       "ptpbaseClockRunningInstanceIndex": ptpbaseClockRunningInstanceIndex,
       "ptpbaseClockRunningState": ptpbaseClockRunningState,
       "ptpbaseClockRunningPacketsSent": ptpbaseClockRunningPacketsSent,
       "ptpbaseClockRunningPacketsReceived": ptpbaseClockRunningPacketsReceived,
       "ptpbaseClockTimePropertiesDSTable": ptpbaseClockTimePropertiesDSTable,
       "ptpbaseClockTimePropertiesDSEntry": ptpbaseClockTimePropertiesDSEntry,
       "ptpbaseClockTimePropertiesDSDomainIndex": ptpbaseClockTimePropertiesDSDomainIndex,
       "ptpbaseClockTimePropertiesDSClockTypeIndex": ptpbaseClockTimePropertiesDSClockTypeIndex,
       "ptpbaseClockTimePropertiesDSInstanceIndex": ptpbaseClockTimePropertiesDSInstanceIndex,
       "ptpbaseClockTimePropertiesDSCurrentUTCOffsetValid": ptpbaseClockTimePropertiesDSCurrentUTCOffsetValid,
       "ptpbaseClockTimePropertiesDSCurrentUTCOffset": ptpbaseClockTimePropertiesDSCurrentUTCOffset,
       "ptpbaseClockTimePropertiesDSLeap59": ptpbaseClockTimePropertiesDSLeap59,
       "ptpbaseClockTimePropertiesDSLeap61": ptpbaseClockTimePropertiesDSLeap61,
       "ptpbaseClockTimePropertiesDSTimeTraceable": ptpbaseClockTimePropertiesDSTimeTraceable,
       "ptpbaseClockTimePropertiesDSFreqTraceable": ptpbaseClockTimePropertiesDSFreqTraceable,
       "ptpbaseClockTimePropertiesDSPTPTimescale": ptpbaseClockTimePropertiesDSPTPTimescale,
       "ptpbaseClockTimePropertiesDSSource": ptpbaseClockTimePropertiesDSSource,
       "ptpbaseClockTransDefaultDSTable": ptpbaseClockTransDefaultDSTable,
       "ptpbaseClockTransDefaultDSEntry": ptpbaseClockTransDefaultDSEntry,
       "ptpbaseClockTransDefaultDSDomainIndex": ptpbaseClockTransDefaultDSDomainIndex,
       "ptpbaseClockTransDefaultDSInstanceIndex": ptpbaseClockTransDefaultDSInstanceIndex,
       "ptpbaseClockTransDefaultDSClockIdentity": ptpbaseClockTransDefaultDSClockIdentity,
       "ptpbaseClockTransDefaultDSNumOfPorts": ptpbaseClockTransDefaultDSNumOfPorts,
       "ptpbaseClockTransDefaultDSDelay": ptpbaseClockTransDefaultDSDelay,
       "ptpbaseClockTransDefaultDSPrimaryDomain": ptpbaseClockTransDefaultDSPrimaryDomain,
       "ptpbaseClockPortTable": ptpbaseClockPortTable,
       "ptpbaseClockPortEntry": ptpbaseClockPortEntry,
       "ptpbaseClockPortDomainIndex": ptpbaseClockPortDomainIndex,
       "ptpbaseClockPortClockTypeIndex": ptpbaseClockPortClockTypeIndex,
       "ptpbaseClockPortClockInstanceIndex": ptpbaseClockPortClockInstanceIndex,
       "ptpbaseClockPortTablePortNumberIndex": ptpbaseClockPortTablePortNumberIndex,
       "ptpbaseClockPortName": ptpbaseClockPortName,
       "ptpbaseClockPortRole": ptpbaseClockPortRole,
       "ptpbaseClockPortSyncTwoStep": ptpbaseClockPortSyncTwoStep,
       "ptpbaseClockPortCurrentPeerAddressType": ptpbaseClockPortCurrentPeerAddressType,
       "ptpbaseClockPortCurrentPeerAddress": ptpbaseClockPortCurrentPeerAddress,
       "ptpbaseClockPortNumOfAssociatedPorts": ptpbaseClockPortNumOfAssociatedPorts,
       "ptpbaseClockPortDSTable": ptpbaseClockPortDSTable,
       "ptpbaseClockPortDSEntry": ptpbaseClockPortDSEntry,
       "ptpbaseClockPortDSDomainIndex": ptpbaseClockPortDSDomainIndex,
       "ptpbaseClockPortDSClockTypeIndex": ptpbaseClockPortDSClockTypeIndex,
       "ptpbaseClockPortDSClockInstanceIndex": ptpbaseClockPortDSClockInstanceIndex,
       "ptpbaseClockPortDSPortNumberIndex": ptpbaseClockPortDSPortNumberIndex,
       "ptpbaseClockPortDSName": ptpbaseClockPortDSName,
       "ptpbaseClockPortDSPortIdentity": ptpbaseClockPortDSPortIdentity,
       "ptpbaseClockPortDSlogAnnouncementInterval": ptpbaseClockPortDSlogAnnouncementInterval,
       "ptpbaseClockPortDSAnnounceRctTimeout": ptpbaseClockPortDSAnnounceRctTimeout,
       "ptpbaseClockPortDSlogSyncInterval": ptpbaseClockPortDSlogSyncInterval,
       "ptpbaseClockPortDSMinDelayReqInterval": ptpbaseClockPortDSMinDelayReqInterval,
       "ptpbaseClockPortDSPeerDelayReqInterval": ptpbaseClockPortDSPeerDelayReqInterval,
       "ptpbaseClockPortDSDelayMech": ptpbaseClockPortDSDelayMech,
       "ptpbaseClockPortDSPeerMeanPathDelay": ptpbaseClockPortDSPeerMeanPathDelay,
       "ptpbaseClockPortDSGrantDuration": ptpbaseClockPortDSGrantDuration,
       "ptpbaseClockPortDSPTPVersion": ptpbaseClockPortDSPTPVersion,
       "ptpbaseClockPortRunningTable": ptpbaseClockPortRunningTable,
       "ptpbaseClockPortRunningEntry": ptpbaseClockPortRunningEntry,
       "ptpbaseClockPortRunningDomainIndex": ptpbaseClockPortRunningDomainIndex,
       "ptpbaseClockPortRunningClockTypeIndex": ptpbaseClockPortRunningClockTypeIndex,
       "ptpbaseClockPortRunningClockInstanceIndex": ptpbaseClockPortRunningClockInstanceIndex,
       "ptpbaseClockPortRunningPortNumberIndex": ptpbaseClockPortRunningPortNumberIndex,
       "ptpbaseClockPortRunningName": ptpbaseClockPortRunningName,
       "ptpbaseClockPortRunningState": ptpbaseClockPortRunningState,
       "ptpbaseClockPortRunningRole": ptpbaseClockPortRunningRole,
       "ptpbaseClockPortRunningInterfaceIndex": ptpbaseClockPortRunningInterfaceIndex,
       "ptpbaseClockPortRunningTransport": ptpbaseClockPortRunningTransport,
       "ptpbaseClockPortRunningEncapsulationType": ptpbaseClockPortRunningEncapsulationType,
       "ptpbaseClockPortRunningTxMode": ptpbaseClockPortRunningTxMode,
       "ptpbaseClockPortRunningRxMode": ptpbaseClockPortRunningRxMode,
       "ptpbaseClockPortRunningPacketsReceived": ptpbaseClockPortRunningPacketsReceived,
       "ptpbaseClockPortRunningPacketsSent": ptpbaseClockPortRunningPacketsSent,
       "ptpbaseClockPortTransDSTable": ptpbaseClockPortTransDSTable,
       "ptpbaseClockPortTransDSEntry": ptpbaseClockPortTransDSEntry,
       "ptpbaseClockPortTransDSDomainIndex": ptpbaseClockPortTransDSDomainIndex,
       "ptpbaseClockPortTransDSInstanceIndex": ptpbaseClockPortTransDSInstanceIndex,
       "ptpbaseClockPortTransDSPortNumberIndex": ptpbaseClockPortTransDSPortNumberIndex,
       "ptpbaseClockPortTransDSPortIdentity": ptpbaseClockPortTransDSPortIdentity,
       "ptpbaseClockPortTransDSlogMinPdelayReqInt": ptpbaseClockPortTransDSlogMinPdelayReqInt,
       "ptpbaseClockPortTransDSFaultyFlag": ptpbaseClockPortTransDSFaultyFlag,
       "ptpbaseClockPortTransDSPeerMeanPathDelay": ptpbaseClockPortTransDSPeerMeanPathDelay,
       "ptpbaseClockPortAssociateTable": ptpbaseClockPortAssociateTable,
       "ptpbaseClockPortAssociateEntry": ptpbaseClockPortAssociateEntry,
       "ptpClockPortCurrentDomainIndex": ptpClockPortCurrentDomainIndex,
       "ptpClockPortCurrentClockTypeIndex": ptpClockPortCurrentClockTypeIndex,
       "ptpClockPortCurrentClockInstanceIndex": ptpClockPortCurrentClockInstanceIndex,
       "ptpClockPortCurrentPortNumberIndex": ptpClockPortCurrentPortNumberIndex,
       "ptpbaseClockPortAssociatePortIndex": ptpbaseClockPortAssociatePortIndex,
       "ptpbaseClockPortAssociateAddressType": ptpbaseClockPortAssociateAddressType,
       "ptpbaseClockPortAssociateAddress": ptpbaseClockPortAssociateAddress,
       "ptpbaseClockPortAssociatePacketsSent": ptpbaseClockPortAssociatePacketsSent,
       "ptpbaseClockPortAssociatePacketsReceived": ptpbaseClockPortAssociatePacketsReceived,
       "ptpbaseClockPortAssociateInErrors": ptpbaseClockPortAssociateInErrors,
       "ptpbaseClockPortAssociateOutErrors": ptpbaseClockPortAssociateOutErrors,
       "ptpbaseWellKnownTransportTypes": ptpbaseWellKnownTransportTypes,
       "ptpbaseTransportTypeIPversion4": ptpbaseTransportTypeIPversion4,
       "ptpbaseTransportTypeIPversion6": ptpbaseTransportTypeIPversion6,
       "ptpbaseTransportTypeEthernet": ptpbaseTransportTypeEthernet,
       "ptpbaseTransportTypeDeviceNET": ptpbaseTransportTypeDeviceNET,
       "ptpbaseTransportTypeControlNET": ptpbaseTransportTypeControlNET,
       "ptpbaseTransportTypeIEC61158": ptpbaseTransportTypeIEC61158,
       "ptpbaseWellKnownEncapsulationTypes": ptpbaseWellKnownEncapsulationTypes,
       "ptpbaseEncapsulationTypeEthernet": ptpbaseEncapsulationTypeEthernet,
       "ptpbaseEncapsulationTypeVLAN": ptpbaseEncapsulationTypeVLAN,
       "ptpbaseEncapsulationTypeUDPIPLSP": ptpbaseEncapsulationTypeUDPIPLSP,
       "ptpbaseEncapsulationTypePWUDPIPLSP": ptpbaseEncapsulationTypePWUDPIPLSP,
       "ptpbaseEncapsulationTypePWEthernetLSP": ptpbaseEncapsulationTypePWEthernetLSP,
       "ptpbaseMIBConformance": ptpbaseMIBConformance,
       "ptpbaseMIBCompliances": ptpbaseMIBCompliances,
       "ptpbaseMIBCompliancesSystemInfo": ptpbaseMIBCompliancesSystemInfo,
       "ptpbaseMIBCompliancesClockInfo": ptpbaseMIBCompliancesClockInfo,
       "ptpbaseMIBCompliancesClockPortInfo": ptpbaseMIBCompliancesClockPortInfo,
       "ptpbaseMIBCompliancesTransparentClockInfo": ptpbaseMIBCompliancesTransparentClockInfo,
       "ptpbaseMIBGroups": ptpbaseMIBGroups,
       "ptpbaseMIBSystemInfoGroup": ptpbaseMIBSystemInfoGroup,
       "ptpbaseMIBClockCurrentDSGroup": ptpbaseMIBClockCurrentDSGroup,
       "ptpbaseMIBClockParentDSGroup": ptpbaseMIBClockParentDSGroup,
       "ptpbaseMIBClockDefaultDSGroup": ptpbaseMIBClockDefaultDSGroup,
       "ptpbaseMIBClockRunningGroup": ptpbaseMIBClockRunningGroup,
       "ptpbaseMIBClockTimepropertiesGroup": ptpbaseMIBClockTimepropertiesGroup,
       "ptpbaseMIBClockTranparentDSGroup": ptpbaseMIBClockTranparentDSGroup,
       "ptpbaseMIBClockPortGroup": ptpbaseMIBClockPortGroup,
       "ptpbaseMIBClockPortDSGroup": ptpbaseMIBClockPortDSGroup,
       "ptpbaseMIBClockPortRunningGroup": ptpbaseMIBClockPortRunningGroup,
       "ptpbaseMIBClockPortTransDSGroup": ptpbaseMIBClockPortTransDSGroup,
       "ptpbaseMIBClockPortAssociateGroup": ptpbaseMIBClockPortAssociateGroup}
)
