# SNMP MIB module (PROTECTION-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\sagemcom\PROTECTION-MIB

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

(SagemBoolean,
 Severity) = mibBuilder.importSymbols(
    "EQUIPMENT-MIB",
    "SagemBoolean",
    "Severity")

(sagemDr,) = mibBuilder.importSymbols(
    "SAGEM-DR-MIB",
    "sagemDr")

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

protection = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 1038, 130)
)


# Types definitions



class TrafficStatus(Integer32):
    """Custom type TrafficStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("working", 1),
          ("protection", 2))
    )





class MspInitiator(Integer32):
    """Custom type MspInitiator based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 0),
          ("local", 1),
          ("remote", 2))
    )





class MspFailure(Integer32):
    """Custom type MspFailure based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              4,
              6)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("pam", 1),
          ("scm", 2),
          ("otm", 4),
          ("scmOtm", 6))
    )





class MspPriority(Integer32):
    """Custom type MspPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 0),
          ("highG783", 1),
          ("low", 2))
    )





class MspStatus(Integer32):
    """Custom type MspStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              4,
              6,
              8,
              10,
              11,
              12,
              13,
              14,
              15)
        )
    )
    namedValues = NamedValues(
        *(("noRequest", 0),
          ("doNotRevert", 1),
          ("reverseRequest", 2),
          ("exercise", 4),
          ("waitToRestore", 6),
          ("manualSwitch", 8),
          ("lowSD", 10),
          ("highSD", 11),
          ("lowSF", 12),
          ("highSF", 13),
          ("forcedSwitch", 14),
          ("lockoutProtection", 15))
    )





class MspType(Integer32):
    """Custom type MspType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 0),
          ("onePlusOneOptimized", 1),
          ("onePlusOneCompatible", 2),
          ("oneForN", 3))
    )





class MspDirection(Integer32):
    """Custom type MspDirection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 0),
          ("unidirectionnal", 1),
          ("bidirectionnal", 2))
    )





class MspCommand(Integer32):
    """Custom type MspCommand based on Integer32"""
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
        *(("clear", 0),
          ("lw", 1),
          ("lp", 2),
          ("fsW", 3),
          ("fsP", 4),
          ("msW", 5),
          ("msP", 6),
          ("exer", 7))
    )





class MsSPRingFailure(Integer32):
    """Custom type MsSPRingFailure based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("ato", 1),
          ("arv", 2),
          ("aun", 3),
          ("ptm", 4),
          ("mms", 5),
          ("exr", 6))
    )





class MsSPRingStatus(Integer32):
    """Custom type MsSPRingStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              3,
              5,
              6,
              8,
              11,
              13,
              15,
              19)
        )
    )
    namedValues = NamedValues(
        *(("noRequest", 0),
          ("reverseRequestR", 1),
          ("exerR", 3),
          ("waitToRestore", 5),
          ("manualSwitchR", 6),
          ("sdR", 8),
          ("sfR", 11),
          ("forcedSwitchR", 13),
          ("lockoutProtection", 15),
          ("off", 19))
    )





class MsSPRingCommand(Integer32):
    """Custom type MsSPRingCommand based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(3,
              6,
              13,
              15,
              16,
              19,
              20)
        )
    )
    namedValues = NamedValues(
        *(("exerR", 3),
          ("msR", 6),
          ("fsR", 13),
          ("lpS", 15),
          ("clear", 16),
          ("off", 19),
          ("on", 20))
    )





class MsSPRingID(Integer32):
    """Custom type MsSPRingID based on Integer32"""
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
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              255)
        )
    )
    namedValues = NamedValues(
        *(("node0", 0),
          ("node1", 1),
          ("node2", 2),
          ("node3", 3),
          ("node4", 4),
          ("node5", 5),
          ("node6", 6),
          ("node7", 7),
          ("node8", 8),
          ("node9", 9),
          ("node10", 10),
          ("node11", 11),
          ("node12", 12),
          ("node13", 13),
          ("node14", 14),
          ("node15", 15),
          ("nodeUNK", 255))
    )





class State(Integer32):
    """Custom type State based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("idle", 1),
          ("pass", 2),
          ("switch", 3),
          ("unknown", 4))
    )





class MisconMapType(Integer32):
    """Custom type MisconMapType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("terminated", 1),
          ("passedThrough", 2))
    )





class MsSPRingSide(Integer32):
    """Custom type MsSPRingSide based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("west", 0),
          ("east", 1),
          ("unknown", 2))
    )





class LinkType(Integer32):
    """Custom type LinkType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              10,
              20)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 0),
          ("au", 1),
          ("au4c", 2),
          ("au16c", 3),
          ("tu3", 10),
          ("tu12", 20))
    )





class TriggerCriterion(Integer32):
    """Custom type TriggerCriterion based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("sncI", 1),
          ("sncN", 2),
          ("sncIRdi", 3),
          ("sncNRdi", 4))
    )





class SNCStateProcess(Integer32):
    """Custom type SNCStateProcess based on Integer32"""
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
              9,
              10,
              11,
              12)
        )
    )
    namedValues = NamedValues(
        *(("nrnormal", 0),
          ("nrsecours", 1),
          ("wtr", 2),
          ("dontRev", 3),
          ("mssecours", 4),
          ("msnormal", 5),
          ("sdnormal", 6),
          ("sdsecours", 7),
          ("sfnormal", 8),
          ("fssecours", 9),
          ("sfsecours", 10),
          ("fsnormal", 11),
          ("lockout", 12))
    )





class SNCCommand(Integer32):
    """Custom type SNCCommand based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              19,
              20)
        )
    )
    namedValues = NamedValues(
        *(("clear", 0),
          ("manualWorking", 1),
          ("manualProtection", 2),
          ("forcedWorking", 3),
          ("forcedProtection", 4),
          ("lockout", 5),
          ("off", 19),
          ("on", 20))
    )





class CardpFamily(Integer32):
    """Custom type CardpFamily based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("switch", 1))
    )





class CardpCommand(Integer32):
    """Custom type CardpCommand based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("clear", 0),
          ("manualSwitch", 1))
    )





class CardpStatus(Integer32):
    """Custom type CardpStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notSwitched", 0),
          ("manualSwitch", 1),
          ("automaticSwitch", 2))
    )




# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Msp_ObjectIdentity = ObjectIdentity
msp = _Msp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1038, 130, 10)
)


class _MspNumber_Type(Integer32):
    """Custom type mspNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_MspNumber_Type.__name__ = "Integer32"
_MspNumber_Object = MibScalar
mspNumber = _MspNumber_Object(
    (1, 3, 6, 1, 4, 1, 1038, 130, 10, 1),
    _MspNumber_Type()
)
mspNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mspNumber.setStatus("current")
_MspTable_Object = MibTable
mspTable = _MspTable_Object(
    (1, 3, 6, 1, 4, 1, 1038, 130, 10, 2)
)
if mibBuilder.loadTexts:
    mspTable.setStatus("current")
_MspEntry_Object = MibTableRow
mspEntry = _MspEntry_Object(
    (1, 3, 6, 1, 4, 1, 1038, 130, 10, 2, 1)
)
mspEntry.setIndexNames(
    (0, "PROTECTION-MIB", "mspIndex"),
)
if mibBuilder.loadTexts:
    mspEntry.setStatus("current")


class _MspIndex_Type(Integer32):
    """Custom type mspIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_MspIndex_Type.__name__ = "Integer32"
_MspIndex_Object = MibTableColumn
mspIndex = _MspIndex_Object(
    (1, 3, 6, 1, 4, 1, 1038, 130, 10, 2, 1, 1),
    _MspIndex_Type()
)
mspIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mspIndex.setStatus("current")


class _MspWorkingPointer_Type(Integer32):
    """Custom type mspWorkingPointer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_MspWorkingPointer_Type.__name__ = "Integer32"
_MspWorkingPointer_Object = MibTableColumn
mspWorkingPointer = _MspWorkingPointer_Object(
    (1, 3, 6, 1, 4, 1, 1038, 130, 10, 2, 1, 2),
    _MspWorkingPointer_Type()
)
mspWorkingPointer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mspWorkingPointer.setStatus("current")


class _MspProtectionPointer_Type(Integer32):
    """Custom type mspProtectionPointer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_MspProtectionPointer_Type.__name__ = "Integer32"
_MspProtectionPointer_Object = MibTableColumn
mspProtectionPointer = _MspProtectionPointer_Object(
    (1, 3, 6, 1, 4, 1, 1038, 130, 10, 2, 1, 3),
    _MspProtectionPointer_Type()
)
mspProtectionPointer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mspProtectionPointer.setStatus("current")
_MspType_Type = MspType
_MspType_Object = MibTableColumn
mspType = _MspType_Object(
    (1, 3, 6, 1, 4, 1, 1038, 130, 10, 2, 1, 4),
    _MspType_Type()
)
mspType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mspType.setStatus("current")
_MspDir_Type = MspDirection
_MspDir_Object = MibTableColumn
mspDir = _MspDir_Object(
    (1, 3, 6, 1, 4, 1, 1038, 130, 10, 2, 1, 5),
    _MspDir_Type()
)
mspDir.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mspDir.setStatus("current")
_MspTraffic_Type = TrafficStatus
_MspTraffic_Object = MibTableColumn
mspTraffic = _MspTraffic_Object(
    (1, 3, 6, 1, 4, 1, 1038, 130, 10, 2, 1, 6),
    _MspTraffic_Type()
)
mspTraffic.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mspTraffic.setStatus("current")
_MspRevertive_Type = SagemBoolean
_MspRevertive_Object = MibTableColumn
mspRevertive = _MspRevertive_Object(
    (1, 3, 6, 1, 4, 1, 1038, 130, 10, 2, 1, 7),
    _MspRevertive_Type()
)
mspRevertive.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mspRevertive.setStatus("current")


class _MspWtr_Type(Integer32):
    """Custom type mspWtr based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_MspWtr_Type.__name__ = "Integer32"
_MspWtr_Object = MibTableColumn
mspWtr = _MspWtr_Object(
    (1, 3, 6, 1, 4, 1, 1038, 130, 10, 2, 1, 8),
    _MspWtr_Type()
)
mspWtr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mspWtr.setStatus("current")
_MspSfSdPriority_Type = MspPriority
_MspSfSdPriority_Object = MibTableColumn
mspSfSdPriority = _MspSfSdPriority_Object(
    (1, 3, 6, 1, 4, 1, 1038, 130, 10, 2, 1, 9),
    _MspSfSdPriority_Type()
)
mspSfSdPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mspSfSdPriority.setStatus("current")


class _MspSfSdHoldOffTime_Type(Integer32):
    """Custom type mspSfSdHoldOffTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_MspSfSdHoldOffTime_Type.__name__ = "Integer32"
_MspSfSdHoldOffTime_Object = MibTableColumn
mspSfSdHoldOffTime = _MspSfSdHoldOffTime_Object(
    (1, 3, 6, 1, 4, 1, 1038, 130, 10, 2, 1, 10),
    _MspSfSdHoldOffTime_Type()
)
mspSfSdHoldOffTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mspSfSdHoldOffTime.setStatus("current")
_MspCommand_Type = MspCommand
_MspCommand_Object = MibTableColumn
mspCommand = _MspCommand_Object(
    (1, 3, 6, 1, 4, 1, 1038, 130, 10, 2, 1, 11),
    _MspCommand_Type()
)
mspCommand.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mspCommand.setStatus("current")
_MspInitiator_Type = MspInitiator
_MspInitiator_Object = MibTableColumn
mspInitiator = _MspInitiator_Object(
    (1, 3, 6, 1, 4, 1, 1038, 130, 10, 2, 1, 12),
    _MspInitiator_Type()
)
mspInitiator.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mspInitiator.setStatus("current")
_MspStatus_Type = MspStatus
_MspStatus_Object = MibTableColumn
mspStatus = _MspStatus_Object(
    (1, 3, 6, 1, 4, 1, 1038, 130, 10, 2, 1, 13),
    _MspStatus_Type()
)
mspStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mspStatus.setStatus("current")
_MspMonitor_Type = SagemBoolean
_MspMonitor_Object = MibTableColumn
mspMonitor = _MspMonitor_Object(
    (1, 3, 6, 1, 4, 1, 1038, 130, 10, 2, 1, 14),
    _MspMonitor_Type()
)
mspMonitor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mspMonitor.setStatus("current")
_MspFailure_Type = MspFailure
_MspFailure_Object = MibTableColumn
mspFailure = _MspFailure_Object(
    (1, 3, 6, 1, 4, 1, 1038, 130, 10, 2, 1, 15),
    _MspFailure_Type()
)
mspFailure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mspFailure.setStatus("current")
_MspSeverity_Type = Severity
_MspSeverity_Object = MibTableColumn
mspSeverity = _MspSeverity_Object(
    (1, 3, 6, 1, 4, 1, 1038, 130, 10, 2, 1, 16),
    _MspSeverity_Type()
)
mspSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mspSeverity.setStatus("current")
_MspPam_Type = Severity
_MspPam_Object = MibTableColumn
mspPam = _MspPam_Object(
    (1, 3, 6, 1, 4, 1, 1038, 130, 10, 2, 1, 20),
    _MspPam_Type()
)
mspPam.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mspPam.setStatus("current")
_MspScm_Type = Severity
_MspScm_Object = MibTableColumn
mspScm = _MspScm_Object(
    (1, 3, 6, 1, 4, 1, 1038, 130, 10, 2, 1, 21),
    _MspScm_Type()
)
mspScm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mspScm.setStatus("current")
_MspOtm_Type = Severity
_MspOtm_Object = MibTableColumn
mspOtm = _MspOtm_Object(
    (1, 3, 6, 1, 4, 1, 1038, 130, 10, 2, 1, 22),
    _MspOtm_Type()
)
mspOtm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mspOtm.setStatus("current")
_MsSPRing_ObjectIdentity = ObjectIdentity
msSPRing = _MsSPRing_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1038, 130, 20)
)


class _MsSPRingNumber_Type(Integer32):
    """Custom type msSPRingNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_MsSPRingNumber_Type.__name__ = "Integer32"
_MsSPRingNumber_Object = MibScalar
msSPRingNumber = _MsSPRingNumber_Object(
    (1, 3, 6, 1, 4, 1, 1038, 130, 20, 1),
    _MsSPRingNumber_Type()
)
msSPRingNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msSPRingNumber.setStatus("current")
_MsSPRingTable_Object = MibTable
msSPRingTable = _MsSPRingTable_Object(
    (1, 3, 6, 1, 4, 1, 1038, 130, 20, 6)
)
if mibBuilder.loadTexts:
    msSPRingTable.setStatus("current")
_MsSPRingEntry_Object = MibTableRow
msSPRingEntry = _MsSPRingEntry_Object(
    (1, 3, 6, 1, 4, 1, 1038, 130, 20, 6, 1)
)
msSPRingEntry.setIndexNames(
    (0, "PROTECTION-MIB", "msSPRingIndex"),
)
if mibBuilder.loadTexts:
    msSPRingEntry.setStatus("current")


class _MsSPRingIndex_Type(Integer32):
    """Custom type msSPRingIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_MsSPRingIndex_Type.__name__ = "Integer32"
_MsSPRingIndex_Object = MibTableColumn
msSPRingIndex = _MsSPRingIndex_Object(
    (1, 3, 6, 1, 4, 1, 1038, 130, 20, 6, 1, 1),
    _MsSPRingIndex_Type()
)
msSPRingIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msSPRingIndex.setStatus("current")


class _MsSPRingWestPointer_Type(Integer32):
    """Custom type msSPRingWestPointer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_MsSPRingWestPointer_Type.__name__ = "Integer32"
_MsSPRingWestPointer_Object = MibTableColumn
msSPRingWestPointer = _MsSPRingWestPointer_Object(
    (1, 3, 6, 1, 4, 1, 1038, 130, 20, 6, 1, 2),
    _MsSPRingWestPointer_Type()
)
msSPRingWestPointer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msSPRingWestPointer.setStatus("current")


class _MsSPRingEastPointer_Type(Integer32):
    """Custom type msSPRingEastPointer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_MsSPRingEastPointer_Type.__name__ = "Integer32"
_MsSPRingEastPointer_Object = MibTableColumn
msSPRingEastPointer = _MsSPRingEastPointer_Object(
    (1, 3, 6, 1, 4, 1, 1038, 130, 20, 6, 1, 3),
    _MsSPRingEastPointer_Type()
)
msSPRingEastPointer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msSPRingEastPointer.setStatus("current")


class _MsSPRingWtr_Type(Integer32):
    """Custom type msSPRingWtr based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_MsSPRingWtr_Type.__name__ = "Integer32"
_MsSPRingWtr_Object = MibTableColumn
msSPRingWtr = _MsSPRingWtr_Object(
    (1, 3, 6, 1, 4, 1, 1038, 130, 20, 6, 1, 5),
    _MsSPRingWtr_Type()
)
msSPRingWtr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msSPRingWtr.setStatus("current")


class _MsSPRingSfSdHoldOffTime_Type(Integer32):
    """Custom type msSPRingSfSdHoldOffTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_MsSPRingSfSdHoldOffTime_Type.__name__ = "Integer32"
_MsSPRingSfSdHoldOffTime_Object = MibTableColumn
msSPRingSfSdHoldOffTime = _MsSPRingSfSdHoldOffTime_Object(
    (1, 3, 6, 1, 4, 1, 1038, 130, 20, 6, 1, 6),
    _MsSPRingSfSdHoldOffTime_Type()
)
msSPRingSfSdHoldOffTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msSPRingSfSdHoldOffTime.setStatus("current")


class _MsSPRingCommandSide_Type(Integer32):
    """Custom type msSPRingCommandSide based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_MsSPRingCommandSide_Type.__name__ = "Integer32"
_MsSPRingCommandSide_Object = MibTableColumn
msSPRingCommandSide = _MsSPRingCommandSide_Object(
    (1, 3, 6, 1, 4, 1, 1038, 130, 20, 6, 1, 7),
    _MsSPRingCommandSide_Type()
)
msSPRingCommandSide.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msSPRingCommandSide.setStatus("current")
_MsSPRingCommand_Type = MsSPRingCommand
_MsSPRingCommand_Object = MibTableColumn
msSPRingCommand = _MsSPRingCommand_Object(
    (1, 3, 6, 1, 4, 1, 1038, 130, 20, 6, 1, 8),
    _MsSPRingCommand_Type()
)
msSPRingCommand.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msSPRingCommand.setStatus("current")
_MsSPRingInitiator1_Type = MsSPRingID
_MsSPRingInitiator1_Object = MibTableColumn
msSPRingInitiator1 = _MsSPRingInitiator1_Object(
    (1, 3, 6, 1, 4, 1, 1038, 130, 20, 6, 1, 10),
    _MsSPRingInitiator1_Type()
)
msSPRingInitiator1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msSPRingInitiator1.setStatus("current")
_MsSPRingInitiator2_Type = MsSPRingID
_MsSPRingInitiator2_Object = MibTableColumn
msSPRingInitiator2 = _MsSPRingInitiator2_Object(
    (1, 3, 6, 1, 4, 1, 1038, 130, 20, 6, 1, 11),
    _MsSPRingInitiator2_Type()
)
msSPRingInitiator2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msSPRingInitiator2.setStatus("current")
_MsSPRingMonitor_Type = SagemBoolean
_MsSPRingMonitor_Object = MibTableColumn
msSPRingMonitor = _MsSPRingMonitor_Object(
    (1, 3, 6, 1, 4, 1, 1038, 130, 20, 6, 1, 12),
    _MsSPRingMonitor_Type()
)
msSPRingMonitor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msSPRingMonitor.setStatus("current")
_MsSPRingFailure_Type = MsSPRingFailure
_MsSPRingFailure_Object = MibTableColumn
msSPRingFailure = _MsSPRingFailure_Object(
    (1, 3, 6, 1, 4, 1, 1038, 130, 20, 6, 1, 13),
    _MsSPRingFailure_Type()
)
msSPRingFailure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msSPRingFailure.setStatus("current")
_MsSPRingSeverity_Type = Severity
_MsSPRingSeverity_Object = MibTableColumn
msSPRingSeverity = _MsSPRingSeverity_Object(
    (1, 3, 6, 1, 4, 1, 1038, 130, 20, 6, 1, 14),
    _MsSPRingSeverity_Type()
)
msSPRingSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msSPRingSeverity.setStatus("current")
_MsSPRingAto_Type = Severity
_MsSPRingAto_Object = MibTableColumn
msSPRingAto = _MsSPRingAto_Object(
    (1, 3, 6, 1, 4, 1, 1038, 130, 20, 6, 1, 21),
    _MsSPRingAto_Type()
)
msSPRingAto.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msSPRingAto.setStatus("current")
_MsSPRingArv_Type = Severity
_MsSPRingArv_Object = MibTableColumn
msSPRingArv = _MsSPRingArv_Object(
    (1, 3, 6, 1, 4, 1, 1038, 130, 20, 6, 1, 22),
    _MsSPRingArv_Type()
)
msSPRingArv.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msSPRingArv.setStatus("current")
_MsSPRingAun_Type = Severity
_MsSPRingAun_Object = MibTableColumn
msSPRingAun = _MsSPRingAun_Object(
    (1, 3, 6, 1, 4, 1, 1038, 130, 20, 6, 1, 23),
    _MsSPRingAun_Type()
)
msSPRingAun.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msSPRingAun.setStatus("current")
_MsSPRingPtm_Type = Severity
_MsSPRingPtm_Object = MibTableColumn
msSPRingPtm = _MsSPRingPtm_Object(
    (1, 3, 6, 1, 4, 1, 1038, 130, 20, 6, 1, 24),
    _MsSPRingPtm_Type()
)
msSPRingPtm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msSPRingPtm.setStatus("current")
_MsSPRingMms_Type = Severity
_MsSPRingMms_Object = MibTableColumn
msSPRingMms = _MsSPRingMms_Object(
    (1, 3, 6, 1, 4, 1, 1038, 130, 20, 6, 1, 25),
    _MsSPRingMms_Type()
)
msSPRingMms.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msSPRingMms.setStatus("current")
_MsSPRingExr_Type = Severity
_MsSPRingExr_Object = MibTableColumn
msSPRingExr = _MsSPRingExr_Object(
    (1, 3, 6, 1, 4, 1, 1038, 130, 20, 6, 1, 26),
    _MsSPRingExr_Type()
)
msSPRingExr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msSPRingExr.setStatus("current")
_MsSPRingSimpleFailure_Type = SagemBoolean
_MsSPRingSimpleFailure_Object = MibTableColumn
msSPRingSimpleFailure = _MsSPRingSimpleFailure_Object(
    (1, 3, 6, 1, 4, 1, 1038, 130, 20, 6, 1, 27),
    _MsSPRingSimpleFailure_Type()
)
msSPRingSimpleFailure.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msSPRingSimpleFailure.setStatus("current")
_MsSPRingId_Type = MsSPRingID
_MsSPRingId_Object = MibTableColumn
msSPRingId = _MsSPRingId_Object(
    (1, 3, 6, 1, 4, 1, 1038, 130, 20, 6, 1, 28),
    _MsSPRingId_Type()
)
msSPRingId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msSPRingId.setStatus("current")
_MsSPRingNodeState_Type = State
_MsSPRingNodeState_Object = MibTableColumn
msSPRingNodeState = _MsSPRingNodeState_Object(
    (1, 3, 6, 1, 4, 1, 1038, 130, 20, 6, 1, 29),
    _MsSPRingNodeState_Type()
)
msSPRingNodeState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msSPRingNodeState.setStatus("current")


class _MsSPRingSwitchingSide_Type(Integer32):
    """Custom type msSPRingSwitchingSide based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_MsSPRingSwitchingSide_Type.__name__ = "Integer32"
_MsSPRingSwitchingSide_Object = MibTableColumn
msSPRingSwitchingSide = _MsSPRingSwitchingSide_Object(
    (1, 3, 6, 1, 4, 1, 1038, 130, 20, 6, 1, 30),
    _MsSPRingSwitchingSide_Type()
)
msSPRingSwitchingSide.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msSPRingSwitchingSide.setStatus("current")
_MsSPRingWestTraffic_Type = TrafficStatus
_MsSPRingWestTraffic_Object = MibTableColumn
msSPRingWestTraffic = _MsSPRingWestTraffic_Object(
    (1, 3, 6, 1, 4, 1, 1038, 130, 20, 6, 1, 31),
    _MsSPRingWestTraffic_Type()
)
msSPRingWestTraffic.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msSPRingWestTraffic.setStatus("current")
_MsSPRingEastTraffic_Type = TrafficStatus
_MsSPRingEastTraffic_Object = MibTableColumn
msSPRingEastTraffic = _MsSPRingEastTraffic_Object(
    (1, 3, 6, 1, 4, 1, 1038, 130, 20, 6, 1, 32),
    _MsSPRingEastTraffic_Type()
)
msSPRingEastTraffic.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msSPRingEastTraffic.setStatus("current")
_MsSPRingWestStatus_Type = MsSPRingStatus
_MsSPRingWestStatus_Object = MibTableColumn
msSPRingWestStatus = _MsSPRingWestStatus_Object(
    (1, 3, 6, 1, 4, 1, 1038, 130, 20, 6, 1, 33),
    _MsSPRingWestStatus_Type()
)
msSPRingWestStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msSPRingWestStatus.setStatus("current")
_MsSPRingEastStatus_Type = MsSPRingStatus
_MsSPRingEastStatus_Object = MibTableColumn
msSPRingEastStatus = _MsSPRingEastStatus_Object(
    (1, 3, 6, 1, 4, 1, 1038, 130, 20, 6, 1, 34),
    _MsSPRingEastStatus_Type()
)
msSPRingEastStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msSPRingEastStatus.setStatus("current")
_MsSPRingTopoMapTable_Object = MibTable
msSPRingTopoMapTable = _MsSPRingTopoMapTable_Object(
    (1, 3, 6, 1, 4, 1, 1038, 130, 20, 11)
)
if mibBuilder.loadTexts:
    msSPRingTopoMapTable.setStatus("current")
_MsSPRingTopoMapEntry_Object = MibTableRow
msSPRingTopoMapEntry = _MsSPRingTopoMapEntry_Object(
    (1, 3, 6, 1, 4, 1, 1038, 130, 20, 11, 1)
)
msSPRingTopoMapEntry.setIndexNames(
    (0, "PROTECTION-MIB", "msSPRingTopoMapIndex"),
)
if mibBuilder.loadTexts:
    msSPRingTopoMapEntry.setStatus("current")


class _MsSPRingTopoMapIndex_Type(Integer32):
    """Custom type msSPRingTopoMapIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_MsSPRingTopoMapIndex_Type.__name__ = "Integer32"
_MsSPRingTopoMapIndex_Object = MibTableColumn
msSPRingTopoMapIndex = _MsSPRingTopoMapIndex_Object(
    (1, 3, 6, 1, 4, 1, 1038, 130, 20, 11, 1, 1),
    _MsSPRingTopoMapIndex_Type()
)
msSPRingTopoMapIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msSPRingTopoMapIndex.setStatus("current")
_MsSPRingTopoMapID_Type = MsSPRingID
_MsSPRingTopoMapID_Object = MibTableColumn
msSPRingTopoMapID = _MsSPRingTopoMapID_Object(
    (1, 3, 6, 1, 4, 1, 1038, 130, 20, 11, 1, 2),
    _MsSPRingTopoMapID_Type()
)
msSPRingTopoMapID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msSPRingTopoMapID.setStatus("current")
_MsSPRingMisconMapTable_Object = MibTable
msSPRingMisconMapTable = _MsSPRingMisconMapTable_Object(
    (1, 3, 6, 1, 4, 1, 1038, 130, 20, 21)
)
if mibBuilder.loadTexts:
    msSPRingMisconMapTable.setStatus("current")
_MsSPRingMisconMapEntry_Object = MibTableRow
msSPRingMisconMapEntry = _MsSPRingMisconMapEntry_Object(
    (1, 3, 6, 1, 4, 1, 1038, 130, 20, 21, 1)
)
msSPRingMisconMapEntry.setIndexNames(
    (0, "PROTECTION-MIB", "msSPRingMisconMapIndex"),
)
if mibBuilder.loadTexts:
    msSPRingMisconMapEntry.setStatus("current")


class _MsSPRingMisconMapIndex_Type(Integer32):
    """Custom type msSPRingMisconMapIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_MsSPRingMisconMapIndex_Type.__name__ = "Integer32"
_MsSPRingMisconMapIndex_Object = MibTableColumn
msSPRingMisconMapIndex = _MsSPRingMisconMapIndex_Object(
    (1, 3, 6, 1, 4, 1, 1038, 130, 20, 21, 1, 1),
    _MsSPRingMisconMapIndex_Type()
)
msSPRingMisconMapIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msSPRingMisconMapIndex.setStatus("current")
_MsSPRingMisconMapSide_Type = MsSPRingSide
_MsSPRingMisconMapSide_Object = MibTableColumn
msSPRingMisconMapSide = _MsSPRingMisconMapSide_Object(
    (1, 3, 6, 1, 4, 1, 1038, 130, 20, 21, 1, 2),
    _MsSPRingMisconMapSide_Type()
)
msSPRingMisconMapSide.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msSPRingMisconMapSide.setStatus("current")
_MsSPRingMisconMapIn_Type = MsSPRingID
_MsSPRingMisconMapIn_Object = MibTableColumn
msSPRingMisconMapIn = _MsSPRingMisconMapIn_Object(
    (1, 3, 6, 1, 4, 1, 1038, 130, 20, 21, 1, 3),
    _MsSPRingMisconMapIn_Type()
)
msSPRingMisconMapIn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msSPRingMisconMapIn.setStatus("current")
_MsSPRingMisconMapOut_Type = MsSPRingID
_MsSPRingMisconMapOut_Object = MibTableColumn
msSPRingMisconMapOut = _MsSPRingMisconMapOut_Object(
    (1, 3, 6, 1, 4, 1, 1038, 130, 20, 21, 1, 4),
    _MsSPRingMisconMapOut_Type()
)
msSPRingMisconMapOut.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msSPRingMisconMapOut.setStatus("current")


class _MsSPRingMisconMapTimeSlot_Type(Integer32):
    """Custom type msSPRingMisconMapTimeSlot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_MsSPRingMisconMapTimeSlot_Type.__name__ = "Integer32"
_MsSPRingMisconMapTimeSlot_Object = MibTableColumn
msSPRingMisconMapTimeSlot = _MsSPRingMisconMapTimeSlot_Object(
    (1, 3, 6, 1, 4, 1, 1038, 130, 20, 21, 1, 5),
    _MsSPRingMisconMapTimeSlot_Type()
)
msSPRingMisconMapTimeSlot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msSPRingMisconMapTimeSlot.setStatus("current")
_MsSPRingMisconMapType_Type = MisconMapType
_MsSPRingMisconMapType_Object = MibTableColumn
msSPRingMisconMapType = _MsSPRingMisconMapType_Object(
    (1, 3, 6, 1, 4, 1, 1038, 130, 20, 21, 1, 6),
    _MsSPRingMisconMapType_Type()
)
msSPRingMisconMapType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msSPRingMisconMapType.setStatus("current")
_MsSPRingMisconMapLOAccess_Type = SagemBoolean
_MsSPRingMisconMapLOAccess_Object = MibTableColumn
msSPRingMisconMapLOAccess = _MsSPRingMisconMapLOAccess_Object(
    (1, 3, 6, 1, 4, 1, 1038, 130, 20, 21, 1, 7),
    _MsSPRingMisconMapLOAccess_Type()
)
msSPRingMisconMapLOAccess.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msSPRingMisconMapLOAccess.setStatus("current")
_MsSPRingNUTTable_Object = MibTable
msSPRingNUTTable = _MsSPRingNUTTable_Object(
    (1, 3, 6, 1, 4, 1, 1038, 130, 20, 31)
)
if mibBuilder.loadTexts:
    msSPRingNUTTable.setStatus("current")
_MsSPRingNUTEntry_Object = MibTableRow
msSPRingNUTEntry = _MsSPRingNUTEntry_Object(
    (1, 3, 6, 1, 4, 1, 1038, 130, 20, 31, 1)
)
msSPRingNUTEntry.setIndexNames(
    (0, "PROTECTION-MIB", "msSPRingNUTIndex"),
)
if mibBuilder.loadTexts:
    msSPRingNUTEntry.setStatus("current")


class _MsSPRingNUTIndex_Type(Integer32):
    """Custom type msSPRingNUTIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_MsSPRingNUTIndex_Type.__name__ = "Integer32"
_MsSPRingNUTIndex_Object = MibTableColumn
msSPRingNUTIndex = _MsSPRingNUTIndex_Object(
    (1, 3, 6, 1, 4, 1, 1038, 130, 20, 31, 1, 1),
    _MsSPRingNUTIndex_Type()
)
msSPRingNUTIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msSPRingNUTIndex.setStatus("current")
_MsSPRingNUTisNut_Type = SagemBoolean
_MsSPRingNUTisNut_Object = MibTableColumn
msSPRingNUTisNut = _MsSPRingNUTisNut_Object(
    (1, 3, 6, 1, 4, 1, 1038, 130, 20, 31, 1, 2),
    _MsSPRingNUTisNut_Type()
)
msSPRingNUTisNut.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msSPRingNUTisNut.setStatus("current")
_Sncp_ObjectIdentity = ObjectIdentity
sncp = _Sncp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1038, 130, 30)
)


class _SncNumber_Type(Integer32):
    """Custom type sncNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_SncNumber_Type.__name__ = "Integer32"
_SncNumber_Object = MibScalar
sncNumber = _SncNumber_Object(
    (1, 3, 6, 1, 4, 1, 1038, 130, 30, 1),
    _SncNumber_Type()
)
sncNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sncNumber.setStatus("current")
_SncTable_Object = MibTable
sncTable = _SncTable_Object(
    (1, 3, 6, 1, 4, 1, 1038, 130, 30, 2)
)
if mibBuilder.loadTexts:
    sncTable.setStatus("current")
_SncEntry_Object = MibTableRow
sncEntry = _SncEntry_Object(
    (1, 3, 6, 1, 4, 1, 1038, 130, 30, 2, 1)
)
sncEntry.setIndexNames(
    (0, "PROTECTION-MIB", "sncIndex"),
)
if mibBuilder.loadTexts:
    sncEntry.setStatus("current")


class _SncIndex_Type(Integer32):
    """Custom type sncIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_SncIndex_Type.__name__ = "Integer32"
_SncIndex_Object = MibTableColumn
sncIndex = _SncIndex_Object(
    (1, 3, 6, 1, 4, 1, 1038, 130, 30, 2, 1, 1),
    _SncIndex_Type()
)
sncIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sncIndex.setStatus("current")


class _SncCTPSink_Type(Integer32):
    """Custom type sncCTPSink based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_SncCTPSink_Type.__name__ = "Integer32"
_SncCTPSink_Object = MibTableColumn
sncCTPSink = _SncCTPSink_Object(
    (1, 3, 6, 1, 4, 1, 1038, 130, 30, 2, 1, 2),
    _SncCTPSink_Type()
)
sncCTPSink.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sncCTPSink.setStatus("current")
_SncLinkType_Type = LinkType
_SncLinkType_Object = MibTableColumn
sncLinkType = _SncLinkType_Object(
    (1, 3, 6, 1, 4, 1, 1038, 130, 30, 2, 1, 3),
    _SncLinkType_Type()
)
sncLinkType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sncLinkType.setStatus("current")


class _SncCTPSourceW_Type(Integer32):
    """Custom type sncCTPSourceW based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_SncCTPSourceW_Type.__name__ = "Integer32"
_SncCTPSourceW_Object = MibTableColumn
sncCTPSourceW = _SncCTPSourceW_Object(
    (1, 3, 6, 1, 4, 1, 1038, 130, 30, 2, 1, 4),
    _SncCTPSourceW_Type()
)
sncCTPSourceW.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sncCTPSourceW.setStatus("current")


class _SncCTPSourceP_Type(Integer32):
    """Custom type sncCTPSourceP based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_SncCTPSourceP_Type.__name__ = "Integer32"
_SncCTPSourceP_Object = MibTableColumn
sncCTPSourceP = _SncCTPSourceP_Object(
    (1, 3, 6, 1, 4, 1, 1038, 130, 30, 2, 1, 5),
    _SncCTPSourceP_Type()
)
sncCTPSourceP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sncCTPSourceP.setStatus("current")
_SncTrafficStatus_Type = TrafficStatus
_SncTrafficStatus_Object = MibTableColumn
sncTrafficStatus = _SncTrafficStatus_Object(
    (1, 3, 6, 1, 4, 1, 1038, 130, 30, 2, 1, 6),
    _SncTrafficStatus_Type()
)
sncTrafficStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sncTrafficStatus.setStatus("current")
_SncWorkingTriggerType_Type = TriggerCriterion
_SncWorkingTriggerType_Object = MibTableColumn
sncWorkingTriggerType = _SncWorkingTriggerType_Object(
    (1, 3, 6, 1, 4, 1, 1038, 130, 30, 2, 1, 8),
    _SncWorkingTriggerType_Type()
)
sncWorkingTriggerType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sncWorkingTriggerType.setStatus("current")
_SncProtectionTriggerType_Type = TriggerCriterion
_SncProtectionTriggerType_Object = MibTableColumn
sncProtectionTriggerType = _SncProtectionTriggerType_Object(
    (1, 3, 6, 1, 4, 1, 1038, 130, 30, 2, 1, 9),
    _SncProtectionTriggerType_Type()
)
sncProtectionTriggerType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sncProtectionTriggerType.setStatus("current")
_SncRevertive_Type = SagemBoolean
_SncRevertive_Object = MibTableColumn
sncRevertive = _SncRevertive_Object(
    (1, 3, 6, 1, 4, 1, 1038, 130, 30, 2, 1, 20),
    _SncRevertive_Type()
)
sncRevertive.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sncRevertive.setStatus("current")


class _SncWtr_Type(Integer32):
    """Custom type sncWtr based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_SncWtr_Type.__name__ = "Integer32"
_SncWtr_Object = MibTableColumn
sncWtr = _SncWtr_Object(
    (1, 3, 6, 1, 4, 1, 1038, 130, 30, 2, 1, 21),
    _SncWtr_Type()
)
sncWtr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sncWtr.setStatus("current")
_SncStateProcess_Type = SNCStateProcess
_SncStateProcess_Object = MibTableColumn
sncStateProcess = _SncStateProcess_Object(
    (1, 3, 6, 1, 4, 1, 1038, 130, 30, 2, 1, 22),
    _SncStateProcess_Type()
)
sncStateProcess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sncStateProcess.setStatus("current")


class _SncHoldOffTime_Type(Integer32):
    """Custom type sncHoldOffTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_SncHoldOffTime_Type.__name__ = "Integer32"
_SncHoldOffTime_Object = MibTableColumn
sncHoldOffTime = _SncHoldOffTime_Object(
    (1, 3, 6, 1, 4, 1, 1038, 130, 30, 2, 1, 23),
    _SncHoldOffTime_Type()
)
sncHoldOffTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sncHoldOffTime.setStatus("current")
_SncCommand_Type = SNCCommand
_SncCommand_Object = MibTableColumn
sncCommand = _SncCommand_Object(
    (1, 3, 6, 1, 4, 1, 1038, 130, 30, 2, 1, 24),
    _SncCommand_Type()
)
sncCommand.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sncCommand.setStatus("current")
_Cardp_ObjectIdentity = ObjectIdentity
cardp = _Cardp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1038, 130, 40)
)


class _CardpNumber_Type(Integer32):
    """Custom type cardpNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CardpNumber_Type.__name__ = "Integer32"
_CardpNumber_Object = MibScalar
cardpNumber = _CardpNumber_Object(
    (1, 3, 6, 1, 4, 1, 1038, 130, 40, 1),
    _CardpNumber_Type()
)
cardpNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cardpNumber.setStatus("current")
_CardpTable_Object = MibTable
cardpTable = _CardpTable_Object(
    (1, 3, 6, 1, 4, 1, 1038, 130, 40, 2)
)
if mibBuilder.loadTexts:
    cardpTable.setStatus("current")
_CardpEntry_Object = MibTableRow
cardpEntry = _CardpEntry_Object(
    (1, 3, 6, 1, 4, 1, 1038, 130, 40, 2, 1)
)
cardpEntry.setIndexNames(
    (0, "PROTECTION-MIB", "cardpIndex"),
)
if mibBuilder.loadTexts:
    cardpEntry.setStatus("current")


class _CardpIndex_Type(Integer32):
    """Custom type cardpIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CardpIndex_Type.__name__ = "Integer32"
_CardpIndex_Object = MibTableColumn
cardpIndex = _CardpIndex_Object(
    (1, 3, 6, 1, 4, 1, 1038, 130, 40, 2, 1, 1),
    _CardpIndex_Type()
)
cardpIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cardpIndex.setStatus("current")
_CardpBoardFamily_Type = CardpFamily
_CardpBoardFamily_Object = MibTableColumn
cardpBoardFamily = _CardpBoardFamily_Object(
    (1, 3, 6, 1, 4, 1, 1038, 130, 40, 2, 1, 2),
    _CardpBoardFamily_Type()
)
cardpBoardFamily.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cardpBoardFamily.setStatus("current")


class _CardpReliefIndex_Type(Integer32):
    """Custom type cardpReliefIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CardpReliefIndex_Type.__name__ = "Integer32"
_CardpReliefIndex_Object = MibTableColumn
cardpReliefIndex = _CardpReliefIndex_Object(
    (1, 3, 6, 1, 4, 1, 1038, 130, 40, 2, 1, 3),
    _CardpReliefIndex_Type()
)
cardpReliefIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cardpReliefIndex.setStatus("current")
_CardpTrafficStatus_Type = TrafficStatus
_CardpTrafficStatus_Object = MibTableColumn
cardpTrafficStatus = _CardpTrafficStatus_Object(
    (1, 3, 6, 1, 4, 1, 1038, 130, 40, 2, 1, 4),
    _CardpTrafficStatus_Type()
)
cardpTrafficStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cardpTrafficStatus.setStatus("current")
_CardpCommand_Type = CardpCommand
_CardpCommand_Object = MibTableColumn
cardpCommand = _CardpCommand_Object(
    (1, 3, 6, 1, 4, 1, 1038, 130, 40, 2, 1, 5),
    _CardpCommand_Type()
)
cardpCommand.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cardpCommand.setStatus("current")
_CardpStatus_Type = CardpStatus
_CardpStatus_Object = MibTableColumn
cardpStatus = _CardpStatus_Object(
    (1, 3, 6, 1, 4, 1, 1038, 130, 40, 2, 1, 6),
    _CardpStatus_Type()
)
cardpStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cardpStatus.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "PROTECTION-MIB",
    **{"TrafficStatus": TrafficStatus,
       "MspInitiator": MspInitiator,
       "MspFailure": MspFailure,
       "MspPriority": MspPriority,
       "MspStatus": MspStatus,
       "MspType": MspType,
       "MspDirection": MspDirection,
       "MspCommand": MspCommand,
       "MsSPRingFailure": MsSPRingFailure,
       "MsSPRingStatus": MsSPRingStatus,
       "MsSPRingCommand": MsSPRingCommand,
       "MsSPRingID": MsSPRingID,
       "State": State,
       "MisconMapType": MisconMapType,
       "MsSPRingSide": MsSPRingSide,
       "LinkType": LinkType,
       "TriggerCriterion": TriggerCriterion,
       "SNCStateProcess": SNCStateProcess,
       "SNCCommand": SNCCommand,
       "CardpFamily": CardpFamily,
       "CardpCommand": CardpCommand,
       "CardpStatus": CardpStatus,
       "protection": protection,
       "msp": msp,
       "mspNumber": mspNumber,
       "mspTable": mspTable,
       "mspEntry": mspEntry,
       "mspIndex": mspIndex,
       "mspWorkingPointer": mspWorkingPointer,
       "mspProtectionPointer": mspProtectionPointer,
       "mspType": mspType,
       "mspDir": mspDir,
       "mspTraffic": mspTraffic,
       "mspRevertive": mspRevertive,
       "mspWtr": mspWtr,
       "mspSfSdPriority": mspSfSdPriority,
       "mspSfSdHoldOffTime": mspSfSdHoldOffTime,
       "mspCommand": mspCommand,
       "mspInitiator": mspInitiator,
       "mspStatus": mspStatus,
       "mspMonitor": mspMonitor,
       "mspFailure": mspFailure,
       "mspSeverity": mspSeverity,
       "mspPam": mspPam,
       "mspScm": mspScm,
       "mspOtm": mspOtm,
       "msSPRing": msSPRing,
       "msSPRingNumber": msSPRingNumber,
       "msSPRingTable": msSPRingTable,
       "msSPRingEntry": msSPRingEntry,
       "msSPRingIndex": msSPRingIndex,
       "msSPRingWestPointer": msSPRingWestPointer,
       "msSPRingEastPointer": msSPRingEastPointer,
       "msSPRingWtr": msSPRingWtr,
       "msSPRingSfSdHoldOffTime": msSPRingSfSdHoldOffTime,
       "msSPRingCommandSide": msSPRingCommandSide,
       "msSPRingCommand": msSPRingCommand,
       "msSPRingInitiator1": msSPRingInitiator1,
       "msSPRingInitiator2": msSPRingInitiator2,
       "msSPRingMonitor": msSPRingMonitor,
       "msSPRingFailure": msSPRingFailure,
       "msSPRingSeverity": msSPRingSeverity,
       "msSPRingAto": msSPRingAto,
       "msSPRingArv": msSPRingArv,
       "msSPRingAun": msSPRingAun,
       "msSPRingPtm": msSPRingPtm,
       "msSPRingMms": msSPRingMms,
       "msSPRingExr": msSPRingExr,
       "msSPRingSimpleFailure": msSPRingSimpleFailure,
       "msSPRingId": msSPRingId,
       "msSPRingNodeState": msSPRingNodeState,
       "msSPRingSwitchingSide": msSPRingSwitchingSide,
       "msSPRingWestTraffic": msSPRingWestTraffic,
       "msSPRingEastTraffic": msSPRingEastTraffic,
       "msSPRingWestStatus": msSPRingWestStatus,
       "msSPRingEastStatus": msSPRingEastStatus,
       "msSPRingTopoMapTable": msSPRingTopoMapTable,
       "msSPRingTopoMapEntry": msSPRingTopoMapEntry,
       "msSPRingTopoMapIndex": msSPRingTopoMapIndex,
       "msSPRingTopoMapID": msSPRingTopoMapID,
       "msSPRingMisconMapTable": msSPRingMisconMapTable,
       "msSPRingMisconMapEntry": msSPRingMisconMapEntry,
       "msSPRingMisconMapIndex": msSPRingMisconMapIndex,
       "msSPRingMisconMapSide": msSPRingMisconMapSide,
       "msSPRingMisconMapIn": msSPRingMisconMapIn,
       "msSPRingMisconMapOut": msSPRingMisconMapOut,
       "msSPRingMisconMapTimeSlot": msSPRingMisconMapTimeSlot,
       "msSPRingMisconMapType": msSPRingMisconMapType,
       "msSPRingMisconMapLOAccess": msSPRingMisconMapLOAccess,
       "msSPRingNUTTable": msSPRingNUTTable,
       "msSPRingNUTEntry": msSPRingNUTEntry,
       "msSPRingNUTIndex": msSPRingNUTIndex,
       "msSPRingNUTisNut": msSPRingNUTisNut,
       "sncp": sncp,
       "sncNumber": sncNumber,
       "sncTable": sncTable,
       "sncEntry": sncEntry,
       "sncIndex": sncIndex,
       "sncCTPSink": sncCTPSink,
       "sncLinkType": sncLinkType,
       "sncCTPSourceW": sncCTPSourceW,
       "sncCTPSourceP": sncCTPSourceP,
       "sncTrafficStatus": sncTrafficStatus,
       "sncWorkingTriggerType": sncWorkingTriggerType,
       "sncProtectionTriggerType": sncProtectionTriggerType,
       "sncRevertive": sncRevertive,
       "sncWtr": sncWtr,
       "sncStateProcess": sncStateProcess,
       "sncHoldOffTime": sncHoldOffTime,
       "sncCommand": sncCommand,
       "cardp": cardp,
       "cardpNumber": cardpNumber,
       "cardpTable": cardpTable,
       "cardpEntry": cardpEntry,
       "cardpIndex": cardpIndex,
       "cardpBoardFamily": cardpBoardFamily,
       "cardpReliefIndex": cardpReliefIndex,
       "cardpTrafficStatus": cardpTrafficStatus,
       "cardpCommand": cardpCommand,
       "cardpStatus": cardpStatus}
)
