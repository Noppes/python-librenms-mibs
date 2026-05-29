# SNMP MIB module (SDH-ETS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\sagemcom\SDH-ETS-MIB

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

sdhEts = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 1038, 110)
)


# Types definitions



class SpiTTPFailure(Integer32):
    """Custom type SpiTTPFailure based on Integer32"""
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
        *(("none", 0),
          ("los", 1),
          ("tf", 2),
          ("losTf", 3))
    )





class Loopback(Integer32):
    """Custom type Loopback based on Integer32"""
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
        *(("none", 0),
          ("line", 1),
          ("equipment", 2),
          ("lineEquipement", 3))
    )





class STMLevel(Integer32):
    """Custom type STMLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              4,
              16,
              64)
        )
    )
    namedValues = NamedValues(
        *(("stm1", 1),
          ("stm4", 4),
          ("stm16", 16),
          ("stm64", 64))
    )





class SpiTTPType(Integer32):
    """Custom type SpiTTPType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("electrical", 0),
          ("optical", 1))
    )





class RsTTPFailure(Integer32):
    """Custom type RsTTPFailure based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("lof", 1))
    )





class EOWMode(Integer32):
    """Custom type EOWMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("codirectional", 0),
          ("contradirectional", 1))
    )





class ProtectionType(Integer32):
    """Custom type ProtectionType based on Integer32"""
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
          ("msp", 1),
          ("msSPRing", 2))
    )





class MsTTPFailure(Integer32):
    """Custom type MsTTPFailure based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              4,
              8,
              12)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("ais", 1),
          ("eber", 2),
          ("sd", 4),
          ("rdi", 8),
          ("sdRdi", 12))
    )





class MsaSrcType(Integer32):
    """Custom type MsaSrcType based on Integer32"""
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
          ("msa", 1),
          ("vc4", 2))
    )





class MsaSinkType(Integer32):
    """Custom type MsaSinkType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("msa", 0),
          ("mst", 1))
    )





class CTPStatus(Integer32):
    """Custom type CTPStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("free", 0),
          ("used", 1))
    )





class Au4CTPFailure(Integer32):
    """Custom type Au4CTPFailure based on Integer32"""
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
        *(("none", 0),
          ("ais", 1),
          ("lop", 2),
          ("lom", 3))
    )





class Au4CTPCnxType(Integer32):
    """Custom type Au4CTPCnxType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              4,
              16,
              20)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("au", 1),
          ("au4c", 4),
          ("au16c", 16),
          ("tu", 20))
    )





class Vc4TTPSinkType(Integer32):
    """Custom type Vc4TTPSinkType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("mst", 1),
          ("nspi", 2))
    )





class Vc4TTPTraceMode(Integer32):
    """Custom type Vc4TTPTraceMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              16)
        )
    )
    namedValues = NamedValues(
        *(("size1", 1),
          ("size16", 16))
    )





class Vc4TTPSignalLabel(Integer32):
    """Custom type Vc4TTPSignalLabel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("unequiped", 0),
          ("unspecified", 1),
          ("tug", 2),
          ("all1", 255))
    )





class Vc4TTPFailure(Integer32):
    """Custom type Vc4TTPFailure based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              6,
              8,
              9,
              10,
              11,
              16,
              17,
              18,
              19)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("rdi", 1),
          ("sd", 2),
          ("sdRdi", 3),
          ("uneq", 4),
          ("uneqSd", 6),
          ("plm", 8),
          ("plmRdi", 9),
          ("plmSd", 10),
          ("plmRdiSd", 11),
          ("tim", 16),
          ("timRdi", 17),
          ("timSd", 18),
          ("timRdiSd", 19))
    )





class Tu3CTPFailure(Integer32):
    """Custom type Tu3CTPFailure based on Integer32"""
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
          ("ais", 1),
          ("lop", 2))
    )





class Tu12CTPFailure(Integer32):
    """Custom type Tu12CTPFailure based on Integer32"""
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
          ("ais", 1),
          ("lop", 2))
    )





class Vc3TTPSinkType(Integer32):
    """Custom type Vc3TTPSinkType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("vc4", 1),
          ("nspi", 2))
    )





class Vc3TTPSignalLabel(Integer32):
    """Custom type Vc3TTPSignalLabel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              4,
              7)
        )
    )
    namedValues = NamedValues(
        *(("unequiped", 0),
          ("unspecified", 1),
          ("mapping3445", 4),
          ("all1", 7))
    )





class VcLoFailure(Integer32):
    """Custom type VcLoFailure based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              6,
              8,
              9,
              10,
              11,
              16,
              17,
              18,
              19)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("rdi", 1),
          ("sd", 2),
          ("sdRdi", 3),
          ("uneq", 4),
          ("uneqSd", 6),
          ("plm", 8),
          ("plmRdi", 9),
          ("plmSd", 10),
          ("plmRdiSd", 11),
          ("tim", 16),
          ("timRdi", 17),
          ("timSd", 18),
          ("timRdiSd", 19))
    )





class Vc12TTPSinkType(Integer32):
    """Custom type Vc12TTPSinkType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("vc4", 1),
          ("nspi", 2))
    )





class Vc12TTPSignalLabel(Integer32):
    """Custom type Vc12TTPSignalLabel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              7)
        )
    )
    namedValues = NamedValues(
        *(("unequiped", 0),
          ("unspecified", 1),
          ("asyncBit", 2),
          ("all1", 7))
    )





class NspiSrcType(Integer32):
    """Custom type NspiSrcType based on Integer32"""
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
        *(("vc12", 1),
          ("vc3", 2),
          ("vc4", 3),
          ("channel", 4))
    )





class NspiTTPFailure(Integer32):
    """Custom type NspiTTPFailure based on Integer32"""
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
          ("los", 1),
          ("ais", 2))
    )





class NspiTTPType(Integer32):
    """Custom type NspiTTPType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              10,
              20,
              30)
        )
    )
    namedValues = NamedValues(
        *(("g703R75ohm", 1),
          ("g703R120ohm", 2),
          ("x21", 10),
          ("ethernet", 20),
          ("atm", 30))
    )





class NspiTTPLevel(Integer32):
    """Custom type NspiTTPLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              10,
              34,
              45,
              100,
              140,
              1000)
        )
    )
    namedValues = NamedValues(
        *(("rate2Mb", 2),
          ("rate10Mb", 10),
          ("rate34Mb", 34),
          ("rate45Mb", 45),
          ("rate100Mb", 100),
          ("rate140Mb", 140),
          ("rate1Gb", 1000))
    )





class ChannelEncaps(Integer32):
    """Custom type ChannelEncaps based on Integer32"""
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
        *(("none", 0),
          ("atm", 1),
          ("pos", 2),
          ("gfp", 3))
    )





class ChannelConcat(Integer32):
    """Custom type ChannelConcat based on Integer32"""
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
          ("virtual", 1),
          ("contiguous", 2))
    )





class ChannelFailure(Integer32):
    """Custom type ChannelFailure based on Integer32"""
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
        *(("none", 0),
          ("loa", 1),
          ("lom", 2),
          ("sqm", 3))
    )




# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_SpiTTP_ObjectIdentity = ObjectIdentity
spiTTP = _SpiTTP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1038, 110, 10)
)


class _SpiTTPNumber_Type(Integer32):
    """Custom type spiTTPNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_SpiTTPNumber_Type.__name__ = "Integer32"
_SpiTTPNumber_Object = MibScalar
spiTTPNumber = _SpiTTPNumber_Object(
    (1, 3, 6, 1, 4, 1, 1038, 110, 10, 1),
    _SpiTTPNumber_Type()
)
spiTTPNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    spiTTPNumber.setStatus("current")
_SpiTTPTable_Object = MibTable
spiTTPTable = _SpiTTPTable_Object(
    (1, 3, 6, 1, 4, 1, 1038, 110, 10, 2)
)
if mibBuilder.loadTexts:
    spiTTPTable.setStatus("current")
_SpiTTPEntry_Object = MibTableRow
spiTTPEntry = _SpiTTPEntry_Object(
    (1, 3, 6, 1, 4, 1, 1038, 110, 10, 2, 1)
)
spiTTPEntry.setIndexNames(
    (0, "SDH-ETS-MIB", "spiTTPIndex"),
)
if mibBuilder.loadTexts:
    spiTTPEntry.setStatus("current")


class _SpiTTPIndex_Type(Integer32):
    """Custom type spiTTPIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_SpiTTPIndex_Type.__name__ = "Integer32"
_SpiTTPIndex_Object = MibTableColumn
spiTTPIndex = _SpiTTPIndex_Object(
    (1, 3, 6, 1, 4, 1, 1038, 110, 10, 2, 1, 1),
    _SpiTTPIndex_Type()
)
spiTTPIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    spiTTPIndex.setStatus("current")
_SpiTTPStmLevel_Type = STMLevel
_SpiTTPStmLevel_Object = MibTableColumn
spiTTPStmLevel = _SpiTTPStmLevel_Object(
    (1, 3, 6, 1, 4, 1, 1038, 110, 10, 2, 1, 2),
    _SpiTTPStmLevel_Type()
)
spiTTPStmLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    spiTTPStmLevel.setStatus("current")
_SpiTTPType_Type = SpiTTPType
_SpiTTPType_Object = MibTableColumn
spiTTPType = _SpiTTPType_Object(
    (1, 3, 6, 1, 4, 1, 1038, 110, 10, 2, 1, 3),
    _SpiTTPType_Type()
)
spiTTPType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    spiTTPType.setStatus("current")
_SpiTTPName_Type = DisplayString
_SpiTTPName_Object = MibTableColumn
spiTTPName = _SpiTTPName_Object(
    (1, 3, 6, 1, 4, 1, 1038, 110, 10, 2, 1, 4),
    _SpiTTPName_Type()
)
spiTTPName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    spiTTPName.setStatus("current")


class _SpiTTPBoardIndex_Type(Integer32):
    """Custom type spiTTPBoardIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_SpiTTPBoardIndex_Type.__name__ = "Integer32"
_SpiTTPBoardIndex_Object = MibTableColumn
spiTTPBoardIndex = _SpiTTPBoardIndex_Object(
    (1, 3, 6, 1, 4, 1, 1038, 110, 10, 2, 1, 5),
    _SpiTTPBoardIndex_Type()
)
spiTTPBoardIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    spiTTPBoardIndex.setStatus("current")


class _SpiTTPBoardAcces_Type(Integer32):
    """Custom type spiTTPBoardAcces based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_SpiTTPBoardAcces_Type.__name__ = "Integer32"
_SpiTTPBoardAcces_Object = MibTableColumn
spiTTPBoardAcces = _SpiTTPBoardAcces_Object(
    (1, 3, 6, 1, 4, 1, 1038, 110, 10, 2, 1, 6),
    _SpiTTPBoardAcces_Type()
)
spiTTPBoardAcces.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    spiTTPBoardAcces.setStatus("current")
_SpiTTPMonitor_Type = SagemBoolean
_SpiTTPMonitor_Object = MibTableColumn
spiTTPMonitor = _SpiTTPMonitor_Object(
    (1, 3, 6, 1, 4, 1, 1038, 110, 10, 2, 1, 7),
    _SpiTTPMonitor_Type()
)
spiTTPMonitor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    spiTTPMonitor.setStatus("current")
_SpiTTPFailure_Type = SpiTTPFailure
_SpiTTPFailure_Object = MibTableColumn
spiTTPFailure = _SpiTTPFailure_Object(
    (1, 3, 6, 1, 4, 1, 1038, 110, 10, 2, 1, 8),
    _SpiTTPFailure_Type()
)
spiTTPFailure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    spiTTPFailure.setStatus("current")
_SpiTTPSeverity_Type = Severity
_SpiTTPSeverity_Object = MibTableColumn
spiTTPSeverity = _SpiTTPSeverity_Object(
    (1, 3, 6, 1, 4, 1, 1038, 110, 10, 2, 1, 9),
    _SpiTTPSeverity_Type()
)
spiTTPSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    spiTTPSeverity.setStatus("current")
_SpiTTPLoopback_Type = Loopback
_SpiTTPLoopback_Object = MibTableColumn
spiTTPLoopback = _SpiTTPLoopback_Object(
    (1, 3, 6, 1, 4, 1, 1038, 110, 10, 2, 1, 10),
    _SpiTTPLoopback_Type()
)
spiTTPLoopback.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    spiTTPLoopback.setStatus("current")
_SpiTTPLos_Type = Severity
_SpiTTPLos_Object = MibTableColumn
spiTTPLos = _SpiTTPLos_Object(
    (1, 3, 6, 1, 4, 1, 1038, 110, 10, 2, 1, 20),
    _SpiTTPLos_Type()
)
spiTTPLos.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    spiTTPLos.setStatus("current")
_SpiTTPTf_Type = Severity
_SpiTTPTf_Object = MibTableColumn
spiTTPTf = _SpiTTPTf_Object(
    (1, 3, 6, 1, 4, 1, 1038, 110, 10, 2, 1, 21),
    _SpiTTPTf_Type()
)
spiTTPTf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    spiTTPTf.setStatus("current")
_RsTTP_ObjectIdentity = ObjectIdentity
rsTTP = _RsTTP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1038, 110, 20)
)
_RsTTPTable_Object = MibTable
rsTTPTable = _RsTTPTable_Object(
    (1, 3, 6, 1, 4, 1, 1038, 110, 20, 2)
)
if mibBuilder.loadTexts:
    rsTTPTable.setStatus("current")
_RsTTPEntry_Object = MibTableRow
rsTTPEntry = _RsTTPEntry_Object(
    (1, 3, 6, 1, 4, 1, 1038, 110, 20, 2, 1)
)
rsTTPEntry.setIndexNames(
    (0, "SDH-ETS-MIB", "rsTTPIndex"),
)
if mibBuilder.loadTexts:
    rsTTPEntry.setStatus("current")


class _RsTTPIndex_Type(Integer32):
    """Custom type rsTTPIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_RsTTPIndex_Type.__name__ = "Integer32"
_RsTTPIndex_Object = MibTableColumn
rsTTPIndex = _RsTTPIndex_Object(
    (1, 3, 6, 1, 4, 1, 1038, 110, 20, 2, 1, 1),
    _RsTTPIndex_Type()
)
rsTTPIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsTTPIndex.setStatus("current")
_RsTTPMonitor_Type = SagemBoolean
_RsTTPMonitor_Object = MibTableColumn
rsTTPMonitor = _RsTTPMonitor_Object(
    (1, 3, 6, 1, 4, 1, 1038, 110, 20, 2, 1, 2),
    _RsTTPMonitor_Type()
)
rsTTPMonitor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsTTPMonitor.setStatus("current")
_RsTTPName_Type = DisplayString
_RsTTPName_Object = MibTableColumn
rsTTPName = _RsTTPName_Object(
    (1, 3, 6, 1, 4, 1, 1038, 110, 20, 2, 1, 3),
    _RsTTPName_Type()
)
rsTTPName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsTTPName.setStatus("current")
_RsTTPFailure_Type = RsTTPFailure
_RsTTPFailure_Object = MibTableColumn
rsTTPFailure = _RsTTPFailure_Object(
    (1, 3, 6, 1, 4, 1, 1038, 110, 20, 2, 1, 4),
    _RsTTPFailure_Type()
)
rsTTPFailure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsTTPFailure.setStatus("current")
_RsTTPSeverity_Type = Severity
_RsTTPSeverity_Object = MibTableColumn
rsTTPSeverity = _RsTTPSeverity_Object(
    (1, 3, 6, 1, 4, 1, 1038, 110, 20, 2, 1, 5),
    _RsTTPSeverity_Type()
)
rsTTPSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsTTPSeverity.setStatus("current")
_RsTTPEOWMode_Type = EOWMode
_RsTTPEOWMode_Object = MibTableColumn
rsTTPEOWMode = _RsTTPEOWMode_Object(
    (1, 3, 6, 1, 4, 1, 1038, 110, 20, 2, 1, 8),
    _RsTTPEOWMode_Type()
)
rsTTPEOWMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsTTPEOWMode.setStatus("current")


class _RsTTPE1SrcPointer_Type(Integer32):
    """Custom type rsTTPE1SrcPointer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_RsTTPE1SrcPointer_Type.__name__ = "Integer32"
_RsTTPE1SrcPointer_Object = MibTableColumn
rsTTPE1SrcPointer = _RsTTPE1SrcPointer_Object(
    (1, 3, 6, 1, 4, 1, 1038, 110, 20, 2, 1, 9),
    _RsTTPE1SrcPointer_Type()
)
rsTTPE1SrcPointer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsTTPE1SrcPointer.setStatus("current")


class _RsTTPF1SrcPointer_Type(Integer32):
    """Custom type rsTTPF1SrcPointer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_RsTTPF1SrcPointer_Type.__name__ = "Integer32"
_RsTTPF1SrcPointer_Object = MibTableColumn
rsTTPF1SrcPointer = _RsTTPF1SrcPointer_Object(
    (1, 3, 6, 1, 4, 1, 1038, 110, 20, 2, 1, 10),
    _RsTTPF1SrcPointer_Type()
)
rsTTPF1SrcPointer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsTTPF1SrcPointer.setStatus("current")


class _RsTTPSesThreshold_Type(Integer32):
    """Custom type rsTTPSesThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_RsTTPSesThreshold_Type.__name__ = "Integer32"
_RsTTPSesThreshold_Object = MibTableColumn
rsTTPSesThreshold = _RsTTPSesThreshold_Object(
    (1, 3, 6, 1, 4, 1, 1038, 110, 20, 2, 1, 11),
    _RsTTPSesThreshold_Type()
)
rsTTPSesThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsTTPSesThreshold.setStatus("current")


class _RsTTPEOWByteLine_Type(Integer32):
    """Custom type rsTTPEOWByteLine based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_RsTTPEOWByteLine_Type.__name__ = "Integer32"
_RsTTPEOWByteLine_Object = MibTableColumn
rsTTPEOWByteLine = _RsTTPEOWByteLine_Object(
    (1, 3, 6, 1, 4, 1, 1038, 110, 20, 2, 1, 12),
    _RsTTPEOWByteLine_Type()
)
rsTTPEOWByteLine.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsTTPEOWByteLine.setStatus("current")


class _RsTTPEOWByteColumn_Type(Integer32):
    """Custom type rsTTPEOWByteColumn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_RsTTPEOWByteColumn_Type.__name__ = "Integer32"
_RsTTPEOWByteColumn_Object = MibTableColumn
rsTTPEOWByteColumn = _RsTTPEOWByteColumn_Object(
    (1, 3, 6, 1, 4, 1, 1038, 110, 20, 2, 1, 13),
    _RsTTPEOWByteColumn_Type()
)
rsTTPEOWByteColumn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsTTPEOWByteColumn.setStatus("current")
_RsTTPLof_Type = Severity
_RsTTPLof_Object = MibTableColumn
rsTTPLof = _RsTTPLof_Object(
    (1, 3, 6, 1, 4, 1, 1038, 110, 20, 2, 1, 20),
    _RsTTPLof_Type()
)
rsTTPLof.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsTTPLof.setStatus("current")
_RsCTP_ObjectIdentity = ObjectIdentity
rsCTP = _RsCTP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1038, 110, 25)
)
_MsTTP_ObjectIdentity = ObjectIdentity
msTTP = _MsTTP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1038, 110, 30)
)
_MsTTPTable_Object = MibTable
msTTPTable = _MsTTPTable_Object(
    (1, 3, 6, 1, 4, 1, 1038, 110, 30, 2)
)
if mibBuilder.loadTexts:
    msTTPTable.setStatus("current")
_MsTTPEntry_Object = MibTableRow
msTTPEntry = _MsTTPEntry_Object(
    (1, 3, 6, 1, 4, 1, 1038, 110, 30, 2, 1)
)
msTTPEntry.setIndexNames(
    (0, "SDH-ETS-MIB", "msTTPIndex"),
)
if mibBuilder.loadTexts:
    msTTPEntry.setStatus("current")


class _MsTTPIndex_Type(Integer32):
    """Custom type msTTPIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_MsTTPIndex_Type.__name__ = "Integer32"
_MsTTPIndex_Object = MibTableColumn
msTTPIndex = _MsTTPIndex_Object(
    (1, 3, 6, 1, 4, 1, 1038, 110, 30, 2, 1, 1),
    _MsTTPIndex_Type()
)
msTTPIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msTTPIndex.setStatus("current")
_MsTTPProtectionType_Type = ProtectionType
_MsTTPProtectionType_Object = MibTableColumn
msTTPProtectionType = _MsTTPProtectionType_Object(
    (1, 3, 6, 1, 4, 1, 1038, 110, 30, 2, 1, 2),
    _MsTTPProtectionType_Type()
)
msTTPProtectionType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msTTPProtectionType.setStatus("current")
_MsTTPMonitor_Type = SagemBoolean
_MsTTPMonitor_Object = MibTableColumn
msTTPMonitor = _MsTTPMonitor_Object(
    (1, 3, 6, 1, 4, 1, 1038, 110, 30, 2, 1, 3),
    _MsTTPMonitor_Type()
)
msTTPMonitor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msTTPMonitor.setStatus("current")
_MsTTPName_Type = DisplayString
_MsTTPName_Object = MibTableColumn
msTTPName = _MsTTPName_Object(
    (1, 3, 6, 1, 4, 1, 1038, 110, 30, 2, 1, 4),
    _MsTTPName_Type()
)
msTTPName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msTTPName.setStatus("current")
_MsTTPFailure_Type = MsTTPFailure
_MsTTPFailure_Object = MibTableColumn
msTTPFailure = _MsTTPFailure_Object(
    (1, 3, 6, 1, 4, 1, 1038, 110, 30, 2, 1, 5),
    _MsTTPFailure_Type()
)
msTTPFailure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msTTPFailure.setStatus("current")
_MsTTPSeverity_Type = Severity
_MsTTPSeverity_Object = MibTableColumn
msTTPSeverity = _MsTTPSeverity_Object(
    (1, 3, 6, 1, 4, 1, 1038, 110, 30, 2, 1, 6),
    _MsTTPSeverity_Type()
)
msTTPSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msTTPSeverity.setStatus("current")
_MsTTPEOWMode_Type = EOWMode
_MsTTPEOWMode_Object = MibTableColumn
msTTPEOWMode = _MsTTPEOWMode_Object(
    (1, 3, 6, 1, 4, 1, 1038, 110, 30, 2, 1, 7),
    _MsTTPEOWMode_Type()
)
msTTPEOWMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msTTPEOWMode.setStatus("current")


class _MsTTPE2SrcPointer_Type(Integer32):
    """Custom type msTTPE2SrcPointer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_MsTTPE2SrcPointer_Type.__name__ = "Integer32"
_MsTTPE2SrcPointer_Object = MibTableColumn
msTTPE2SrcPointer = _MsTTPE2SrcPointer_Object(
    (1, 3, 6, 1, 4, 1, 1038, 110, 30, 2, 1, 8),
    _MsTTPE2SrcPointer_Type()
)
msTTPE2SrcPointer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msTTPE2SrcPointer.setStatus("current")


class _MsTTPEOWByteLine_Type(Integer32):
    """Custom type msTTPEOWByteLine based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_MsTTPEOWByteLine_Type.__name__ = "Integer32"
_MsTTPEOWByteLine_Object = MibTableColumn
msTTPEOWByteLine = _MsTTPEOWByteLine_Object(
    (1, 3, 6, 1, 4, 1, 1038, 110, 30, 2, 1, 9),
    _MsTTPEOWByteLine_Type()
)
msTTPEOWByteLine.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msTTPEOWByteLine.setStatus("current")


class _MsTTPEOWByteColumn_Type(Integer32):
    """Custom type msTTPEOWByteColumn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_MsTTPEOWByteColumn_Type.__name__ = "Integer32"
_MsTTPEOWByteColumn_Object = MibTableColumn
msTTPEOWByteColumn = _MsTTPEOWByteColumn_Object(
    (1, 3, 6, 1, 4, 1, 1038, 110, 30, 2, 1, 10),
    _MsTTPEOWByteColumn_Type()
)
msTTPEOWByteColumn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msTTPEOWByteColumn.setStatus("current")
_MsTTPMonEber_Type = SagemBoolean
_MsTTPMonEber_Object = MibTableColumn
msTTPMonEber = _MsTTPMonEber_Object(
    (1, 3, 6, 1, 4, 1, 1038, 110, 30, 2, 1, 11),
    _MsTTPMonEber_Type()
)
msTTPMonEber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msTTPMonEber.setStatus("current")


class _MsTTPSdThreshold_Type(Integer32):
    """Custom type msTTPSdThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_MsTTPSdThreshold_Type.__name__ = "Integer32"
_MsTTPSdThreshold_Object = MibTableColumn
msTTPSdThreshold = _MsTTPSdThreshold_Object(
    (1, 3, 6, 1, 4, 1, 1038, 110, 30, 2, 1, 12),
    _MsTTPSdThreshold_Type()
)
msTTPSdThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msTTPSdThreshold.setStatus("current")


class _MsTTPSesThreshold_Type(Integer32):
    """Custom type msTTPSesThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_MsTTPSesThreshold_Type.__name__ = "Integer32"
_MsTTPSesThreshold_Object = MibTableColumn
msTTPSesThreshold = _MsTTPSesThreshold_Object(
    (1, 3, 6, 1, 4, 1, 1038, 110, 30, 2, 1, 13),
    _MsTTPSesThreshold_Type()
)
msTTPSesThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msTTPSesThreshold.setStatus("current")
_MsTTPEber_Type = Severity
_MsTTPEber_Object = MibTableColumn
msTTPEber = _MsTTPEber_Object(
    (1, 3, 6, 1, 4, 1, 1038, 110, 30, 2, 1, 20),
    _MsTTPEber_Type()
)
msTTPEber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msTTPEber.setStatus("current")
_MsTTPSd_Type = Severity
_MsTTPSd_Object = MibTableColumn
msTTPSd = _MsTTPSd_Object(
    (1, 3, 6, 1, 4, 1, 1038, 110, 30, 2, 1, 21),
    _MsTTPSd_Type()
)
msTTPSd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msTTPSd.setStatus("current")
_MsTTPRdi_Type = Severity
_MsTTPRdi_Object = MibTableColumn
msTTPRdi = _MsTTPRdi_Object(
    (1, 3, 6, 1, 4, 1, 1038, 110, 30, 2, 1, 22),
    _MsTTPRdi_Type()
)
msTTPRdi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msTTPRdi.setStatus("current")
_MsCTP_ObjectIdentity = ObjectIdentity
msCTP = _MsCTP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1038, 110, 35)
)
_Msa_ObjectIdentity = ObjectIdentity
msa = _Msa_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1038, 110, 60)
)
_MsaTable_Object = MibTable
msaTable = _MsaTable_Object(
    (1, 3, 6, 1, 4, 1, 1038, 110, 60, 2)
)
if mibBuilder.loadTexts:
    msaTable.setStatus("current")
_MsaEntry_Object = MibTableRow
msaEntry = _MsaEntry_Object(
    (1, 3, 6, 1, 4, 1, 1038, 110, 60, 2, 1)
)
msaEntry.setIndexNames(
    (0, "SDH-ETS-MIB", "msaIndex"),
)
if mibBuilder.loadTexts:
    msaEntry.setStatus("current")


class _MsaIndex_Type(Integer32):
    """Custom type msaIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_MsaIndex_Type.__name__ = "Integer32"
_MsaIndex_Object = MibTableColumn
msaIndex = _MsaIndex_Object(
    (1, 3, 6, 1, 4, 1, 1038, 110, 60, 2, 1, 1),
    _MsaIndex_Type()
)
msaIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msaIndex.setStatus("current")
_MsaSTMLevel_Type = STMLevel
_MsaSTMLevel_Object = MibTableColumn
msaSTMLevel = _MsaSTMLevel_Object(
    (1, 3, 6, 1, 4, 1, 1038, 110, 60, 2, 1, 2),
    _MsaSTMLevel_Type()
)
msaSTMLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msaSTMLevel.setStatus("current")
_MsaSinkType_Type = MsaSinkType
_MsaSinkType_Object = MibTableColumn
msaSinkType = _MsaSinkType_Object(
    (1, 3, 6, 1, 4, 1, 1038, 110, 60, 2, 1, 3),
    _MsaSinkType_Type()
)
msaSinkType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msaSinkType.setStatus("current")


class _MsaSinkPointer_Type(Integer32):
    """Custom type msaSinkPointer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_MsaSinkPointer_Type.__name__ = "Integer32"
_MsaSinkPointer_Object = MibTableColumn
msaSinkPointer = _MsaSinkPointer_Object(
    (1, 3, 6, 1, 4, 1, 1038, 110, 60, 2, 1, 4),
    _MsaSinkPointer_Type()
)
msaSinkPointer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msaSinkPointer.setStatus("current")
_MsaName_Type = DisplayString
_MsaName_Object = MibTableColumn
msaName = _MsaName_Object(
    (1, 3, 6, 1, 4, 1, 1038, 110, 60, 2, 1, 5),
    _MsaName_Type()
)
msaName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msaName.setStatus("current")
_MsaSrc1Type_Type = MsaSrcType
_MsaSrc1Type_Object = MibTableColumn
msaSrc1Type = _MsaSrc1Type_Object(
    (1, 3, 6, 1, 4, 1, 1038, 110, 60, 2, 1, 6),
    _MsaSrc1Type_Type()
)
msaSrc1Type.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msaSrc1Type.setStatus("current")
_MsaSrc2Type_Type = MsaSrcType
_MsaSrc2Type_Object = MibTableColumn
msaSrc2Type = _MsaSrc2Type_Object(
    (1, 3, 6, 1, 4, 1, 1038, 110, 60, 2, 1, 7),
    _MsaSrc2Type_Type()
)
msaSrc2Type.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msaSrc2Type.setStatus("current")
_MsaSrc3Type_Type = MsaSrcType
_MsaSrc3Type_Object = MibTableColumn
msaSrc3Type = _MsaSrc3Type_Object(
    (1, 3, 6, 1, 4, 1, 1038, 110, 60, 2, 1, 8),
    _MsaSrc3Type_Type()
)
msaSrc3Type.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msaSrc3Type.setStatus("current")
_MsaSrc4Type_Type = MsaSrcType
_MsaSrc4Type_Object = MibTableColumn
msaSrc4Type = _MsaSrc4Type_Object(
    (1, 3, 6, 1, 4, 1, 1038, 110, 60, 2, 1, 9),
    _MsaSrc4Type_Type()
)
msaSrc4Type.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msaSrc4Type.setStatus("current")


class _MsaSrc1Pointer_Type(Integer32):
    """Custom type msaSrc1Pointer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_MsaSrc1Pointer_Type.__name__ = "Integer32"
_MsaSrc1Pointer_Object = MibTableColumn
msaSrc1Pointer = _MsaSrc1Pointer_Object(
    (1, 3, 6, 1, 4, 1, 1038, 110, 60, 2, 1, 10),
    _MsaSrc1Pointer_Type()
)
msaSrc1Pointer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msaSrc1Pointer.setStatus("current")


class _MsaSrc2Pointer_Type(Integer32):
    """Custom type msaSrc2Pointer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_MsaSrc2Pointer_Type.__name__ = "Integer32"
_MsaSrc2Pointer_Object = MibTableColumn
msaSrc2Pointer = _MsaSrc2Pointer_Object(
    (1, 3, 6, 1, 4, 1, 1038, 110, 60, 2, 1, 11),
    _MsaSrc2Pointer_Type()
)
msaSrc2Pointer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msaSrc2Pointer.setStatus("current")


class _MsaSrc3Pointer_Type(Integer32):
    """Custom type msaSrc3Pointer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_MsaSrc3Pointer_Type.__name__ = "Integer32"
_MsaSrc3Pointer_Object = MibTableColumn
msaSrc3Pointer = _MsaSrc3Pointer_Object(
    (1, 3, 6, 1, 4, 1, 1038, 110, 60, 2, 1, 12),
    _MsaSrc3Pointer_Type()
)
msaSrc3Pointer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msaSrc3Pointer.setStatus("current")


class _MsaSrc4Pointer_Type(Integer32):
    """Custom type msaSrc4Pointer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_MsaSrc4Pointer_Type.__name__ = "Integer32"
_MsaSrc4Pointer_Object = MibTableColumn
msaSrc4Pointer = _MsaSrc4Pointer_Object(
    (1, 3, 6, 1, 4, 1, 1038, 110, 60, 2, 1, 13),
    _MsaSrc4Pointer_Type()
)
msaSrc4Pointer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msaSrc4Pointer.setStatus("current")
_Au4CTP_ObjectIdentity = ObjectIdentity
au4CTP = _Au4CTP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1038, 110, 70)
)


class _Au4CTPNumber_Type(Integer32):
    """Custom type au4CTPNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_Au4CTPNumber_Type.__name__ = "Integer32"
_Au4CTPNumber_Object = MibScalar
au4CTPNumber = _Au4CTPNumber_Object(
    (1, 3, 6, 1, 4, 1, 1038, 110, 70, 1),
    _Au4CTPNumber_Type()
)
au4CTPNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    au4CTPNumber.setStatus("current")
_Au4CTPTable_Object = MibTable
au4CTPTable = _Au4CTPTable_Object(
    (1, 3, 6, 1, 4, 1, 1038, 110, 70, 2)
)
if mibBuilder.loadTexts:
    au4CTPTable.setStatus("current")
_Au4CTPEntry_Object = MibTableRow
au4CTPEntry = _Au4CTPEntry_Object(
    (1, 3, 6, 1, 4, 1, 1038, 110, 70, 2, 1)
)
au4CTPEntry.setIndexNames(
    (0, "SDH-ETS-MIB", "au4CTPIndex"),
)
if mibBuilder.loadTexts:
    au4CTPEntry.setStatus("current")


class _Au4CTPIndex_Type(Integer32):
    """Custom type au4CTPIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_Au4CTPIndex_Type.__name__ = "Integer32"
_Au4CTPIndex_Object = MibTableColumn
au4CTPIndex = _Au4CTPIndex_Object(
    (1, 3, 6, 1, 4, 1, 1038, 110, 70, 2, 1, 1),
    _Au4CTPIndex_Type()
)
au4CTPIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    au4CTPIndex.setStatus("current")
_Au4CTPStatus_Type = CTPStatus
_Au4CTPStatus_Object = MibTableColumn
au4CTPStatus = _Au4CTPStatus_Object(
    (1, 3, 6, 1, 4, 1, 1038, 110, 70, 2, 1, 2),
    _Au4CTPStatus_Type()
)
au4CTPStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    au4CTPStatus.setStatus("current")
_Au4CTPCnxType_Type = Au4CTPCnxType
_Au4CTPCnxType_Object = MibTableColumn
au4CTPCnxType = _Au4CTPCnxType_Object(
    (1, 3, 6, 1, 4, 1, 1038, 110, 70, 2, 1, 3),
    _Au4CTPCnxType_Type()
)
au4CTPCnxType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    au4CTPCnxType.setStatus("current")
_Au4CTPName_Type = DisplayString
_Au4CTPName_Object = MibTableColumn
au4CTPName = _Au4CTPName_Object(
    (1, 3, 6, 1, 4, 1, 1038, 110, 70, 2, 1, 4),
    _Au4CTPName_Type()
)
au4CTPName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    au4CTPName.setStatus("current")
_Au4CTPMonitor_Type = SagemBoolean
_Au4CTPMonitor_Object = MibTableColumn
au4CTPMonitor = _Au4CTPMonitor_Object(
    (1, 3, 6, 1, 4, 1, 1038, 110, 70, 2, 1, 6),
    _Au4CTPMonitor_Type()
)
au4CTPMonitor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    au4CTPMonitor.setStatus("current")
_Au4CTPFailure_Type = Au4CTPFailure
_Au4CTPFailure_Object = MibTableColumn
au4CTPFailure = _Au4CTPFailure_Object(
    (1, 3, 6, 1, 4, 1, 1038, 110, 70, 2, 1, 7),
    _Au4CTPFailure_Type()
)
au4CTPFailure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    au4CTPFailure.setStatus("current")
_Au4CTPSeverity_Type = Severity
_Au4CTPSeverity_Object = MibTableColumn
au4CTPSeverity = _Au4CTPSeverity_Object(
    (1, 3, 6, 1, 4, 1, 1038, 110, 70, 2, 1, 8),
    _Au4CTPSeverity_Type()
)
au4CTPSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    au4CTPSeverity.setStatus("current")
_Au4CTPAis_Type = Severity
_Au4CTPAis_Object = MibTableColumn
au4CTPAis = _Au4CTPAis_Object(
    (1, 3, 6, 1, 4, 1, 1038, 110, 70, 2, 1, 20),
    _Au4CTPAis_Type()
)
au4CTPAis.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    au4CTPAis.setStatus("current")
_Au4CTPLop_Type = Severity
_Au4CTPLop_Object = MibTableColumn
au4CTPLop = _Au4CTPLop_Object(
    (1, 3, 6, 1, 4, 1, 1038, 110, 70, 2, 1, 21),
    _Au4CTPLop_Type()
)
au4CTPLop.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    au4CTPLop.setStatus("current")
_Au4CTPLom_Type = Severity
_Au4CTPLom_Object = MibTableColumn
au4CTPLom = _Au4CTPLom_Object(
    (1, 3, 6, 1, 4, 1, 1038, 110, 70, 2, 1, 22),
    _Au4CTPLom_Type()
)
au4CTPLom.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    au4CTPLom.setStatus("current")
_Vc4TTP_ObjectIdentity = ObjectIdentity
vc4TTP = _Vc4TTP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1038, 110, 100)
)


class _Vc4TTPNumber_Type(Integer32):
    """Custom type vc4TTPNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_Vc4TTPNumber_Type.__name__ = "Integer32"
_Vc4TTPNumber_Object = MibScalar
vc4TTPNumber = _Vc4TTPNumber_Object(
    (1, 3, 6, 1, 4, 1, 1038, 110, 100, 1),
    _Vc4TTPNumber_Type()
)
vc4TTPNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vc4TTPNumber.setStatus("current")
_Vc4TTPTable_Object = MibTable
vc4TTPTable = _Vc4TTPTable_Object(
    (1, 3, 6, 1, 4, 1, 1038, 110, 100, 2)
)
if mibBuilder.loadTexts:
    vc4TTPTable.setStatus("current")
_Vc4TTPEntry_Object = MibTableRow
vc4TTPEntry = _Vc4TTPEntry_Object(
    (1, 3, 6, 1, 4, 1, 1038, 110, 100, 2, 1)
)
vc4TTPEntry.setIndexNames(
    (0, "SDH-ETS-MIB", "vc4TTPIndex"),
)
if mibBuilder.loadTexts:
    vc4TTPEntry.setStatus("current")


class _Vc4TTPIndex_Type(Integer32):
    """Custom type vc4TTPIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_Vc4TTPIndex_Type.__name__ = "Integer32"
_Vc4TTPIndex_Object = MibTableColumn
vc4TTPIndex = _Vc4TTPIndex_Object(
    (1, 3, 6, 1, 4, 1, 1038, 110, 100, 2, 1, 1),
    _Vc4TTPIndex_Type()
)
vc4TTPIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vc4TTPIndex.setStatus("current")


class _Vc4TTPSinkPointer_Type(Integer32):
    """Custom type vc4TTPSinkPointer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_Vc4TTPSinkPointer_Type.__name__ = "Integer32"
_Vc4TTPSinkPointer_Object = MibTableColumn
vc4TTPSinkPointer = _Vc4TTPSinkPointer_Object(
    (1, 3, 6, 1, 4, 1, 1038, 110, 100, 2, 1, 2),
    _Vc4TTPSinkPointer_Type()
)
vc4TTPSinkPointer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vc4TTPSinkPointer.setStatus("current")
_Vc4TTPSinkType_Type = Vc4TTPSinkType
_Vc4TTPSinkType_Object = MibTableColumn
vc4TTPSinkType = _Vc4TTPSinkType_Object(
    (1, 3, 6, 1, 4, 1, 1038, 110, 100, 2, 1, 3),
    _Vc4TTPSinkType_Type()
)
vc4TTPSinkType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vc4TTPSinkType.setStatus("current")
_Vc4TTPName_Type = DisplayString
_Vc4TTPName_Object = MibTableColumn
vc4TTPName = _Vc4TTPName_Object(
    (1, 3, 6, 1, 4, 1, 1038, 110, 100, 2, 1, 5),
    _Vc4TTPName_Type()
)
vc4TTPName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vc4TTPName.setStatus("current")
_Vc4TTPMonitor_Type = SagemBoolean
_Vc4TTPMonitor_Object = MibTableColumn
vc4TTPMonitor = _Vc4TTPMonitor_Object(
    (1, 3, 6, 1, 4, 1, 1038, 110, 100, 2, 1, 6),
    _Vc4TTPMonitor_Type()
)
vc4TTPMonitor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vc4TTPMonitor.setStatus("current")
_Vc4TTPFailure_Type = Vc4TTPFailure
_Vc4TTPFailure_Object = MibTableColumn
vc4TTPFailure = _Vc4TTPFailure_Object(
    (1, 3, 6, 1, 4, 1, 1038, 110, 100, 2, 1, 7),
    _Vc4TTPFailure_Type()
)
vc4TTPFailure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vc4TTPFailure.setStatus("current")
_Vc4TTPSeverity_Type = Severity
_Vc4TTPSeverity_Object = MibTableColumn
vc4TTPSeverity = _Vc4TTPSeverity_Object(
    (1, 3, 6, 1, 4, 1, 1038, 110, 100, 2, 1, 8),
    _Vc4TTPSeverity_Type()
)
vc4TTPSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vc4TTPSeverity.setStatus("current")
_Vc4TTPTraceMode_Type = Vc4TTPTraceMode
_Vc4TTPTraceMode_Object = MibTableColumn
vc4TTPTraceMode = _Vc4TTPTraceMode_Object(
    (1, 3, 6, 1, 4, 1, 1038, 110, 100, 2, 1, 9),
    _Vc4TTPTraceMode_Type()
)
vc4TTPTraceMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vc4TTPTraceMode.setStatus("current")


class _Vc4TTPPathTraceExpected_Type(OctetString):
    """Custom type vc4TTPPathTraceExpected based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )
    fixed_length = 16


_Vc4TTPPathTraceExpected_Type.__name__ = "OctetString"
_Vc4TTPPathTraceExpected_Object = MibTableColumn
vc4TTPPathTraceExpected = _Vc4TTPPathTraceExpected_Object(
    (1, 3, 6, 1, 4, 1, 1038, 110, 100, 2, 1, 11),
    _Vc4TTPPathTraceExpected_Type()
)
vc4TTPPathTraceExpected.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vc4TTPPathTraceExpected.setStatus("current")


class _Vc4TTPPathTraceSent_Type(OctetString):
    """Custom type vc4TTPPathTraceSent based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )
    fixed_length = 16


_Vc4TTPPathTraceSent_Type.__name__ = "OctetString"
_Vc4TTPPathTraceSent_Object = MibTableColumn
vc4TTPPathTraceSent = _Vc4TTPPathTraceSent_Object(
    (1, 3, 6, 1, 4, 1, 1038, 110, 100, 2, 1, 12),
    _Vc4TTPPathTraceSent_Type()
)
vc4TTPPathTraceSent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vc4TTPPathTraceSent.setStatus("current")


class _Vc4TTPPathTraceReceived_Type(OctetString):
    """Custom type vc4TTPPathTraceReceived based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )
    fixed_length = 16


_Vc4TTPPathTraceReceived_Type.__name__ = "OctetString"
_Vc4TTPPathTraceReceived_Object = MibTableColumn
vc4TTPPathTraceReceived = _Vc4TTPPathTraceReceived_Object(
    (1, 3, 6, 1, 4, 1, 1038, 110, 100, 2, 1, 13),
    _Vc4TTPPathTraceReceived_Type()
)
vc4TTPPathTraceReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vc4TTPPathTraceReceived.setStatus("current")
_Vc4TTPLabelExpected_Type = Vc4TTPSignalLabel
_Vc4TTPLabelExpected_Object = MibTableColumn
vc4TTPLabelExpected = _Vc4TTPLabelExpected_Object(
    (1, 3, 6, 1, 4, 1, 1038, 110, 100, 2, 1, 14),
    _Vc4TTPLabelExpected_Type()
)
vc4TTPLabelExpected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vc4TTPLabelExpected.setStatus("current")
_Vc4TTPLabelSent_Type = Vc4TTPSignalLabel
_Vc4TTPLabelSent_Object = MibTableColumn
vc4TTPLabelSent = _Vc4TTPLabelSent_Object(
    (1, 3, 6, 1, 4, 1, 1038, 110, 100, 2, 1, 15),
    _Vc4TTPLabelSent_Type()
)
vc4TTPLabelSent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vc4TTPLabelSent.setStatus("current")
_Vc4TTPLabelReceived_Type = Vc4TTPSignalLabel
_Vc4TTPLabelReceived_Object = MibTableColumn
vc4TTPLabelReceived = _Vc4TTPLabelReceived_Object(
    (1, 3, 6, 1, 4, 1, 1038, 110, 100, 2, 1, 16),
    _Vc4TTPLabelReceived_Type()
)
vc4TTPLabelReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vc4TTPLabelReceived.setStatus("current")


class _Vc4TTPSdThreshold_Type(Integer32):
    """Custom type vc4TTPSdThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_Vc4TTPSdThreshold_Type.__name__ = "Integer32"
_Vc4TTPSdThreshold_Object = MibTableColumn
vc4TTPSdThreshold = _Vc4TTPSdThreshold_Object(
    (1, 3, 6, 1, 4, 1, 1038, 110, 100, 2, 1, 17),
    _Vc4TTPSdThreshold_Type()
)
vc4TTPSdThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vc4TTPSdThreshold.setStatus("current")


class _Vc4TTPSesThreshold_Type(Integer32):
    """Custom type vc4TTPSesThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_Vc4TTPSesThreshold_Type.__name__ = "Integer32"
_Vc4TTPSesThreshold_Object = MibTableColumn
vc4TTPSesThreshold = _Vc4TTPSesThreshold_Object(
    (1, 3, 6, 1, 4, 1, 1038, 110, 100, 2, 1, 18),
    _Vc4TTPSesThreshold_Type()
)
vc4TTPSesThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vc4TTPSesThreshold.setStatus("current")
_Vc4TTPBidirectionnal_Type = SagemBoolean
_Vc4TTPBidirectionnal_Object = MibTableColumn
vc4TTPBidirectionnal = _Vc4TTPBidirectionnal_Object(
    (1, 3, 6, 1, 4, 1, 1038, 110, 100, 2, 1, 19),
    _Vc4TTPBidirectionnal_Type()
)
vc4TTPBidirectionnal.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vc4TTPBidirectionnal.setStatus("current")
_Vc4TTPRdi_Type = Severity
_Vc4TTPRdi_Object = MibTableColumn
vc4TTPRdi = _Vc4TTPRdi_Object(
    (1, 3, 6, 1, 4, 1, 1038, 110, 100, 2, 1, 20),
    _Vc4TTPRdi_Type()
)
vc4TTPRdi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vc4TTPRdi.setStatus("current")
_Vc4TTPSd_Type = Severity
_Vc4TTPSd_Object = MibTableColumn
vc4TTPSd = _Vc4TTPSd_Object(
    (1, 3, 6, 1, 4, 1, 1038, 110, 100, 2, 1, 21),
    _Vc4TTPSd_Type()
)
vc4TTPSd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vc4TTPSd.setStatus("current")
_Vc4TTPUneq_Type = Severity
_Vc4TTPUneq_Object = MibTableColumn
vc4TTPUneq = _Vc4TTPUneq_Object(
    (1, 3, 6, 1, 4, 1, 1038, 110, 100, 2, 1, 22),
    _Vc4TTPUneq_Type()
)
vc4TTPUneq.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vc4TTPUneq.setStatus("current")
_Vc4TTPPlm_Type = Severity
_Vc4TTPPlm_Object = MibTableColumn
vc4TTPPlm = _Vc4TTPPlm_Object(
    (1, 3, 6, 1, 4, 1, 1038, 110, 100, 2, 1, 23),
    _Vc4TTPPlm_Type()
)
vc4TTPPlm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vc4TTPPlm.setStatus("current")
_Vc4TTPTimDis_Type = SagemBoolean
_Vc4TTPTimDis_Object = MibTableColumn
vc4TTPTimDis = _Vc4TTPTimDis_Object(
    (1, 3, 6, 1, 4, 1, 1038, 110, 100, 2, 1, 24),
    _Vc4TTPTimDis_Type()
)
vc4TTPTimDis.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vc4TTPTimDis.setStatus("current")
_Vc4TTPTim_Type = Severity
_Vc4TTPTim_Object = MibTableColumn
vc4TTPTim = _Vc4TTPTim_Object(
    (1, 3, 6, 1, 4, 1, 1038, 110, 100, 2, 1, 25),
    _Vc4TTPTim_Type()
)
vc4TTPTim.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vc4TTPTim.setStatus("current")
_Tu3CTP_ObjectIdentity = ObjectIdentity
tu3CTP = _Tu3CTP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1038, 110, 120)
)


class _Tu3CTPNumber_Type(Integer32):
    """Custom type tu3CTPNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_Tu3CTPNumber_Type.__name__ = "Integer32"
_Tu3CTPNumber_Object = MibScalar
tu3CTPNumber = _Tu3CTPNumber_Object(
    (1, 3, 6, 1, 4, 1, 1038, 110, 120, 1),
    _Tu3CTPNumber_Type()
)
tu3CTPNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tu3CTPNumber.setStatus("current")
_Tu3CTPTable_Object = MibTable
tu3CTPTable = _Tu3CTPTable_Object(
    (1, 3, 6, 1, 4, 1, 1038, 110, 120, 2)
)
if mibBuilder.loadTexts:
    tu3CTPTable.setStatus("current")
_Tu3CTPEntry_Object = MibTableRow
tu3CTPEntry = _Tu3CTPEntry_Object(
    (1, 3, 6, 1, 4, 1, 1038, 110, 120, 2, 1)
)
tu3CTPEntry.setIndexNames(
    (0, "SDH-ETS-MIB", "tu3CTPIndex"),
)
if mibBuilder.loadTexts:
    tu3CTPEntry.setStatus("current")


class _Tu3CTPIndex_Type(Integer32):
    """Custom type tu3CTPIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_Tu3CTPIndex_Type.__name__ = "Integer32"
_Tu3CTPIndex_Object = MibTableColumn
tu3CTPIndex = _Tu3CTPIndex_Object(
    (1, 3, 6, 1, 4, 1, 1038, 110, 120, 2, 1, 1),
    _Tu3CTPIndex_Type()
)
tu3CTPIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tu3CTPIndex.setStatus("current")
_Tu3CTPStatus_Type = CTPStatus
_Tu3CTPStatus_Object = MibTableColumn
tu3CTPStatus = _Tu3CTPStatus_Object(
    (1, 3, 6, 1, 4, 1, 1038, 110, 120, 2, 1, 2),
    _Tu3CTPStatus_Type()
)
tu3CTPStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tu3CTPStatus.setStatus("current")
_Tu3CTPName_Type = DisplayString
_Tu3CTPName_Object = MibTableColumn
tu3CTPName = _Tu3CTPName_Object(
    (1, 3, 6, 1, 4, 1, 1038, 110, 120, 2, 1, 5),
    _Tu3CTPName_Type()
)
tu3CTPName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tu3CTPName.setStatus("current")
_Tu3CTPMonitor_Type = SagemBoolean
_Tu3CTPMonitor_Object = MibTableColumn
tu3CTPMonitor = _Tu3CTPMonitor_Object(
    (1, 3, 6, 1, 4, 1, 1038, 110, 120, 2, 1, 6),
    _Tu3CTPMonitor_Type()
)
tu3CTPMonitor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tu3CTPMonitor.setStatus("current")
_Tu3CTPFailure_Type = Tu3CTPFailure
_Tu3CTPFailure_Object = MibTableColumn
tu3CTPFailure = _Tu3CTPFailure_Object(
    (1, 3, 6, 1, 4, 1, 1038, 110, 120, 2, 1, 7),
    _Tu3CTPFailure_Type()
)
tu3CTPFailure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tu3CTPFailure.setStatus("current")
_Tu3CTPSeverity_Type = Severity
_Tu3CTPSeverity_Object = MibTableColumn
tu3CTPSeverity = _Tu3CTPSeverity_Object(
    (1, 3, 6, 1, 4, 1, 1038, 110, 120, 2, 1, 8),
    _Tu3CTPSeverity_Type()
)
tu3CTPSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tu3CTPSeverity.setStatus("current")
_Tu3CTPAis_Type = Severity
_Tu3CTPAis_Object = MibTableColumn
tu3CTPAis = _Tu3CTPAis_Object(
    (1, 3, 6, 1, 4, 1, 1038, 110, 120, 2, 1, 20),
    _Tu3CTPAis_Type()
)
tu3CTPAis.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tu3CTPAis.setStatus("current")
_Tu3CTPLop_Type = Severity
_Tu3CTPLop_Object = MibTableColumn
tu3CTPLop = _Tu3CTPLop_Object(
    (1, 3, 6, 1, 4, 1, 1038, 110, 120, 2, 1, 21),
    _Tu3CTPLop_Type()
)
tu3CTPLop.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tu3CTPLop.setStatus("current")
_Vc3TTP_ObjectIdentity = ObjectIdentity
vc3TTP = _Vc3TTP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1038, 110, 130)
)


class _Vc3TTPNumber_Type(Integer32):
    """Custom type vc3TTPNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_Vc3TTPNumber_Type.__name__ = "Integer32"
_Vc3TTPNumber_Object = MibScalar
vc3TTPNumber = _Vc3TTPNumber_Object(
    (1, 3, 6, 1, 4, 1, 1038, 110, 130, 1),
    _Vc3TTPNumber_Type()
)
vc3TTPNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vc3TTPNumber.setStatus("current")
_Vc3TTPTable_Object = MibTable
vc3TTPTable = _Vc3TTPTable_Object(
    (1, 3, 6, 1, 4, 1, 1038, 110, 130, 2)
)
if mibBuilder.loadTexts:
    vc3TTPTable.setStatus("current")
_Vc3TTPEntry_Object = MibTableRow
vc3TTPEntry = _Vc3TTPEntry_Object(
    (1, 3, 6, 1, 4, 1, 1038, 110, 130, 2, 1)
)
vc3TTPEntry.setIndexNames(
    (0, "SDH-ETS-MIB", "vc3TTPIndex"),
)
if mibBuilder.loadTexts:
    vc3TTPEntry.setStatus("current")


class _Vc3TTPIndex_Type(Integer32):
    """Custom type vc3TTPIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_Vc3TTPIndex_Type.__name__ = "Integer32"
_Vc3TTPIndex_Object = MibTableColumn
vc3TTPIndex = _Vc3TTPIndex_Object(
    (1, 3, 6, 1, 4, 1, 1038, 110, 130, 2, 1, 1),
    _Vc3TTPIndex_Type()
)
vc3TTPIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vc3TTPIndex.setStatus("current")


class _Vc3TTPSinkPointer_Type(Integer32):
    """Custom type vc3TTPSinkPointer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_Vc3TTPSinkPointer_Type.__name__ = "Integer32"
_Vc3TTPSinkPointer_Object = MibTableColumn
vc3TTPSinkPointer = _Vc3TTPSinkPointer_Object(
    (1, 3, 6, 1, 4, 1, 1038, 110, 130, 2, 1, 2),
    _Vc3TTPSinkPointer_Type()
)
vc3TTPSinkPointer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vc3TTPSinkPointer.setStatus("current")
_Vc3TTPSinkType_Type = Vc3TTPSinkType
_Vc3TTPSinkType_Object = MibTableColumn
vc3TTPSinkType = _Vc3TTPSinkType_Object(
    (1, 3, 6, 1, 4, 1, 1038, 110, 130, 2, 1, 3),
    _Vc3TTPSinkType_Type()
)
vc3TTPSinkType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vc3TTPSinkType.setStatus("current")
_Vc3TTPName_Type = DisplayString
_Vc3TTPName_Object = MibTableColumn
vc3TTPName = _Vc3TTPName_Object(
    (1, 3, 6, 1, 4, 1, 1038, 110, 130, 2, 1, 5),
    _Vc3TTPName_Type()
)
vc3TTPName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vc3TTPName.setStatus("current")
_Vc3TTPMonitor_Type = SagemBoolean
_Vc3TTPMonitor_Object = MibTableColumn
vc3TTPMonitor = _Vc3TTPMonitor_Object(
    (1, 3, 6, 1, 4, 1, 1038, 110, 130, 2, 1, 6),
    _Vc3TTPMonitor_Type()
)
vc3TTPMonitor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vc3TTPMonitor.setStatus("current")
_Vc3TTPFailure_Type = VcLoFailure
_Vc3TTPFailure_Object = MibTableColumn
vc3TTPFailure = _Vc3TTPFailure_Object(
    (1, 3, 6, 1, 4, 1, 1038, 110, 130, 2, 1, 7),
    _Vc3TTPFailure_Type()
)
vc3TTPFailure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vc3TTPFailure.setStatus("current")
_Vc3TTPSeverity_Type = Severity
_Vc3TTPSeverity_Object = MibTableColumn
vc3TTPSeverity = _Vc3TTPSeverity_Object(
    (1, 3, 6, 1, 4, 1, 1038, 110, 130, 2, 1, 8),
    _Vc3TTPSeverity_Type()
)
vc3TTPSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vc3TTPSeverity.setStatus("current")


class _Vc3TTPPathTraceExpected_Type(OctetString):
    """Custom type vc3TTPPathTraceExpected based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )
    fixed_length = 16


_Vc3TTPPathTraceExpected_Type.__name__ = "OctetString"
_Vc3TTPPathTraceExpected_Object = MibTableColumn
vc3TTPPathTraceExpected = _Vc3TTPPathTraceExpected_Object(
    (1, 3, 6, 1, 4, 1, 1038, 110, 130, 2, 1, 9),
    _Vc3TTPPathTraceExpected_Type()
)
vc3TTPPathTraceExpected.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vc3TTPPathTraceExpected.setStatus("current")


class _Vc3TTPPathTraceSent_Type(OctetString):
    """Custom type vc3TTPPathTraceSent based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 15),
    )


_Vc3TTPPathTraceSent_Type.__name__ = "OctetString"
_Vc3TTPPathTraceSent_Object = MibTableColumn
vc3TTPPathTraceSent = _Vc3TTPPathTraceSent_Object(
    (1, 3, 6, 1, 4, 1, 1038, 110, 130, 2, 1, 10),
    _Vc3TTPPathTraceSent_Type()
)
vc3TTPPathTraceSent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vc3TTPPathTraceSent.setStatus("current")


class _Vc3TTPPathTraceReceived_Type(OctetString):
    """Custom type vc3TTPPathTraceReceived based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(15, 15),
    )
    fixed_length = 15


_Vc3TTPPathTraceReceived_Type.__name__ = "OctetString"
_Vc3TTPPathTraceReceived_Object = MibTableColumn
vc3TTPPathTraceReceived = _Vc3TTPPathTraceReceived_Object(
    (1, 3, 6, 1, 4, 1, 1038, 110, 130, 2, 1, 11),
    _Vc3TTPPathTraceReceived_Type()
)
vc3TTPPathTraceReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vc3TTPPathTraceReceived.setStatus("current")
_Vc3TTPLabelExpected_Type = Vc3TTPSignalLabel
_Vc3TTPLabelExpected_Object = MibTableColumn
vc3TTPLabelExpected = _Vc3TTPLabelExpected_Object(
    (1, 3, 6, 1, 4, 1, 1038, 110, 130, 2, 1, 12),
    _Vc3TTPLabelExpected_Type()
)
vc3TTPLabelExpected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vc3TTPLabelExpected.setStatus("current")
_Vc3TTPLabelSent_Type = Vc3TTPSignalLabel
_Vc3TTPLabelSent_Object = MibTableColumn
vc3TTPLabelSent = _Vc3TTPLabelSent_Object(
    (1, 3, 6, 1, 4, 1, 1038, 110, 130, 2, 1, 13),
    _Vc3TTPLabelSent_Type()
)
vc3TTPLabelSent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vc3TTPLabelSent.setStatus("current")
_Vc3TTPLabelReceived_Type = Vc3TTPSignalLabel
_Vc3TTPLabelReceived_Object = MibTableColumn
vc3TTPLabelReceived = _Vc3TTPLabelReceived_Object(
    (1, 3, 6, 1, 4, 1, 1038, 110, 130, 2, 1, 14),
    _Vc3TTPLabelReceived_Type()
)
vc3TTPLabelReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vc3TTPLabelReceived.setStatus("current")


class _Vc3TTPSdThreshold_Type(Integer32):
    """Custom type vc3TTPSdThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_Vc3TTPSdThreshold_Type.__name__ = "Integer32"
_Vc3TTPSdThreshold_Object = MibTableColumn
vc3TTPSdThreshold = _Vc3TTPSdThreshold_Object(
    (1, 3, 6, 1, 4, 1, 1038, 110, 130, 2, 1, 15),
    _Vc3TTPSdThreshold_Type()
)
vc3TTPSdThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vc3TTPSdThreshold.setStatus("current")


class _Vc3TTPSesThreshold_Type(Integer32):
    """Custom type vc3TTPSesThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_Vc3TTPSesThreshold_Type.__name__ = "Integer32"
_Vc3TTPSesThreshold_Object = MibTableColumn
vc3TTPSesThreshold = _Vc3TTPSesThreshold_Object(
    (1, 3, 6, 1, 4, 1, 1038, 110, 130, 2, 1, 16),
    _Vc3TTPSesThreshold_Type()
)
vc3TTPSesThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vc3TTPSesThreshold.setStatus("current")
_Vc3TTPBidirectionnal_Type = SagemBoolean
_Vc3TTPBidirectionnal_Object = MibTableColumn
vc3TTPBidirectionnal = _Vc3TTPBidirectionnal_Object(
    (1, 3, 6, 1, 4, 1, 1038, 110, 130, 2, 1, 17),
    _Vc3TTPBidirectionnal_Type()
)
vc3TTPBidirectionnal.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vc3TTPBidirectionnal.setStatus("current")
_Vc3TTPRdi_Type = Severity
_Vc3TTPRdi_Object = MibTableColumn
vc3TTPRdi = _Vc3TTPRdi_Object(
    (1, 3, 6, 1, 4, 1, 1038, 110, 130, 2, 1, 20),
    _Vc3TTPRdi_Type()
)
vc3TTPRdi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vc3TTPRdi.setStatus("current")
_Vc3TTPSd_Type = Severity
_Vc3TTPSd_Object = MibTableColumn
vc3TTPSd = _Vc3TTPSd_Object(
    (1, 3, 6, 1, 4, 1, 1038, 110, 130, 2, 1, 21),
    _Vc3TTPSd_Type()
)
vc3TTPSd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vc3TTPSd.setStatus("current")
_Vc3TTPUneq_Type = Severity
_Vc3TTPUneq_Object = MibTableColumn
vc3TTPUneq = _Vc3TTPUneq_Object(
    (1, 3, 6, 1, 4, 1, 1038, 110, 130, 2, 1, 22),
    _Vc3TTPUneq_Type()
)
vc3TTPUneq.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vc3TTPUneq.setStatus("current")
_Vc3TTPPlm_Type = Severity
_Vc3TTPPlm_Object = MibTableColumn
vc3TTPPlm = _Vc3TTPPlm_Object(
    (1, 3, 6, 1, 4, 1, 1038, 110, 130, 2, 1, 23),
    _Vc3TTPPlm_Type()
)
vc3TTPPlm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vc3TTPPlm.setStatus("current")
_Vc3TTPTim_Type = Severity
_Vc3TTPTim_Object = MibTableColumn
vc3TTPTim = _Vc3TTPTim_Object(
    (1, 3, 6, 1, 4, 1, 1038, 110, 130, 2, 1, 24),
    _Vc3TTPTim_Type()
)
vc3TTPTim.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vc3TTPTim.setStatus("current")
_Tu12CTP_ObjectIdentity = ObjectIdentity
tu12CTP = _Tu12CTP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1038, 110, 140)
)


class _Tu12CTPNumber_Type(Integer32):
    """Custom type tu12CTPNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_Tu12CTPNumber_Type.__name__ = "Integer32"
_Tu12CTPNumber_Object = MibScalar
tu12CTPNumber = _Tu12CTPNumber_Object(
    (1, 3, 6, 1, 4, 1, 1038, 110, 140, 1),
    _Tu12CTPNumber_Type()
)
tu12CTPNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tu12CTPNumber.setStatus("current")
_Tu12CTPTable_Object = MibTable
tu12CTPTable = _Tu12CTPTable_Object(
    (1, 3, 6, 1, 4, 1, 1038, 110, 140, 2)
)
if mibBuilder.loadTexts:
    tu12CTPTable.setStatus("current")
_Tu12CTPEntry_Object = MibTableRow
tu12CTPEntry = _Tu12CTPEntry_Object(
    (1, 3, 6, 1, 4, 1, 1038, 110, 140, 2, 1)
)
tu12CTPEntry.setIndexNames(
    (0, "SDH-ETS-MIB", "tu12CTPIndex"),
)
if mibBuilder.loadTexts:
    tu12CTPEntry.setStatus("current")


class _Tu12CTPIndex_Type(Integer32):
    """Custom type tu12CTPIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_Tu12CTPIndex_Type.__name__ = "Integer32"
_Tu12CTPIndex_Object = MibTableColumn
tu12CTPIndex = _Tu12CTPIndex_Object(
    (1, 3, 6, 1, 4, 1, 1038, 110, 140, 2, 1, 1),
    _Tu12CTPIndex_Type()
)
tu12CTPIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tu12CTPIndex.setStatus("current")
_Tu12CTPStatus_Type = CTPStatus
_Tu12CTPStatus_Object = MibTableColumn
tu12CTPStatus = _Tu12CTPStatus_Object(
    (1, 3, 6, 1, 4, 1, 1038, 110, 140, 2, 1, 2),
    _Tu12CTPStatus_Type()
)
tu12CTPStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tu12CTPStatus.setStatus("current")
_Tu12CTPName_Type = DisplayString
_Tu12CTPName_Object = MibTableColumn
tu12CTPName = _Tu12CTPName_Object(
    (1, 3, 6, 1, 4, 1, 1038, 110, 140, 2, 1, 5),
    _Tu12CTPName_Type()
)
tu12CTPName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tu12CTPName.setStatus("current")
_Tu12CTPMonitor_Type = SagemBoolean
_Tu12CTPMonitor_Object = MibTableColumn
tu12CTPMonitor = _Tu12CTPMonitor_Object(
    (1, 3, 6, 1, 4, 1, 1038, 110, 140, 2, 1, 6),
    _Tu12CTPMonitor_Type()
)
tu12CTPMonitor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tu12CTPMonitor.setStatus("current")
_Tu12CTPFailure_Type = Tu12CTPFailure
_Tu12CTPFailure_Object = MibTableColumn
tu12CTPFailure = _Tu12CTPFailure_Object(
    (1, 3, 6, 1, 4, 1, 1038, 110, 140, 2, 1, 7),
    _Tu12CTPFailure_Type()
)
tu12CTPFailure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tu12CTPFailure.setStatus("current")
_Tu12CTPSeverity_Type = Severity
_Tu12CTPSeverity_Object = MibTableColumn
tu12CTPSeverity = _Tu12CTPSeverity_Object(
    (1, 3, 6, 1, 4, 1, 1038, 110, 140, 2, 1, 8),
    _Tu12CTPSeverity_Type()
)
tu12CTPSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tu12CTPSeverity.setStatus("current")
_Tu12CTPAis_Type = Severity
_Tu12CTPAis_Object = MibTableColumn
tu12CTPAis = _Tu12CTPAis_Object(
    (1, 3, 6, 1, 4, 1, 1038, 110, 140, 2, 1, 20),
    _Tu12CTPAis_Type()
)
tu12CTPAis.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tu12CTPAis.setStatus("current")
_Tu12CTPLop_Type = Severity
_Tu12CTPLop_Object = MibTableColumn
tu12CTPLop = _Tu12CTPLop_Object(
    (1, 3, 6, 1, 4, 1, 1038, 110, 140, 2, 1, 21),
    _Tu12CTPLop_Type()
)
tu12CTPLop.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tu12CTPLop.setStatus("current")
_Vc12TTP_ObjectIdentity = ObjectIdentity
vc12TTP = _Vc12TTP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1038, 110, 150)
)


class _Vc12TTPNumber_Type(Integer32):
    """Custom type vc12TTPNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_Vc12TTPNumber_Type.__name__ = "Integer32"
_Vc12TTPNumber_Object = MibScalar
vc12TTPNumber = _Vc12TTPNumber_Object(
    (1, 3, 6, 1, 4, 1, 1038, 110, 150, 1),
    _Vc12TTPNumber_Type()
)
vc12TTPNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vc12TTPNumber.setStatus("current")
_Vc12TTPTable_Object = MibTable
vc12TTPTable = _Vc12TTPTable_Object(
    (1, 3, 6, 1, 4, 1, 1038, 110, 150, 2)
)
if mibBuilder.loadTexts:
    vc12TTPTable.setStatus("current")
_Vc12TTPEntry_Object = MibTableRow
vc12TTPEntry = _Vc12TTPEntry_Object(
    (1, 3, 6, 1, 4, 1, 1038, 110, 150, 2, 1)
)
vc12TTPEntry.setIndexNames(
    (0, "SDH-ETS-MIB", "vc12TTPIndex"),
)
if mibBuilder.loadTexts:
    vc12TTPEntry.setStatus("current")


class _Vc12TTPIndex_Type(Integer32):
    """Custom type vc12TTPIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_Vc12TTPIndex_Type.__name__ = "Integer32"
_Vc12TTPIndex_Object = MibTableColumn
vc12TTPIndex = _Vc12TTPIndex_Object(
    (1, 3, 6, 1, 4, 1, 1038, 110, 150, 2, 1, 1),
    _Vc12TTPIndex_Type()
)
vc12TTPIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vc12TTPIndex.setStatus("current")


class _Vc12TTPSinkPointer_Type(Integer32):
    """Custom type vc12TTPSinkPointer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_Vc12TTPSinkPointer_Type.__name__ = "Integer32"
_Vc12TTPSinkPointer_Object = MibTableColumn
vc12TTPSinkPointer = _Vc12TTPSinkPointer_Object(
    (1, 3, 6, 1, 4, 1, 1038, 110, 150, 2, 1, 2),
    _Vc12TTPSinkPointer_Type()
)
vc12TTPSinkPointer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vc12TTPSinkPointer.setStatus("current")
_Vc12TTPSinkType_Type = Vc12TTPSinkType
_Vc12TTPSinkType_Object = MibTableColumn
vc12TTPSinkType = _Vc12TTPSinkType_Object(
    (1, 3, 6, 1, 4, 1, 1038, 110, 150, 2, 1, 3),
    _Vc12TTPSinkType_Type()
)
vc12TTPSinkType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vc12TTPSinkType.setStatus("current")
_Vc12TTPName_Type = DisplayString
_Vc12TTPName_Object = MibTableColumn
vc12TTPName = _Vc12TTPName_Object(
    (1, 3, 6, 1, 4, 1, 1038, 110, 150, 2, 1, 5),
    _Vc12TTPName_Type()
)
vc12TTPName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vc12TTPName.setStatus("current")
_Vc12TTPMonitor_Type = SagemBoolean
_Vc12TTPMonitor_Object = MibTableColumn
vc12TTPMonitor = _Vc12TTPMonitor_Object(
    (1, 3, 6, 1, 4, 1, 1038, 110, 150, 2, 1, 6),
    _Vc12TTPMonitor_Type()
)
vc12TTPMonitor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vc12TTPMonitor.setStatus("current")
_Vc12TTPFailure_Type = VcLoFailure
_Vc12TTPFailure_Object = MibTableColumn
vc12TTPFailure = _Vc12TTPFailure_Object(
    (1, 3, 6, 1, 4, 1, 1038, 110, 150, 2, 1, 7),
    _Vc12TTPFailure_Type()
)
vc12TTPFailure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vc12TTPFailure.setStatus("current")
_Vc12TTPSeverity_Type = Severity
_Vc12TTPSeverity_Object = MibTableColumn
vc12TTPSeverity = _Vc12TTPSeverity_Object(
    (1, 3, 6, 1, 4, 1, 1038, 110, 150, 2, 1, 8),
    _Vc12TTPSeverity_Type()
)
vc12TTPSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vc12TTPSeverity.setStatus("current")


class _Vc12TTPPathTraceExpected_Type(OctetString):
    """Custom type vc12TTPPathTraceExpected based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )
    fixed_length = 16


_Vc12TTPPathTraceExpected_Type.__name__ = "OctetString"
_Vc12TTPPathTraceExpected_Object = MibTableColumn
vc12TTPPathTraceExpected = _Vc12TTPPathTraceExpected_Object(
    (1, 3, 6, 1, 4, 1, 1038, 110, 150, 2, 1, 9),
    _Vc12TTPPathTraceExpected_Type()
)
vc12TTPPathTraceExpected.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vc12TTPPathTraceExpected.setStatus("current")


class _Vc12TTPPathTraceSent_Type(OctetString):
    """Custom type vc12TTPPathTraceSent based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )
    fixed_length = 16


_Vc12TTPPathTraceSent_Type.__name__ = "OctetString"
_Vc12TTPPathTraceSent_Object = MibTableColumn
vc12TTPPathTraceSent = _Vc12TTPPathTraceSent_Object(
    (1, 3, 6, 1, 4, 1, 1038, 110, 150, 2, 1, 10),
    _Vc12TTPPathTraceSent_Type()
)
vc12TTPPathTraceSent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vc12TTPPathTraceSent.setStatus("current")


class _Vc12TTPPathTraceReceived_Type(OctetString):
    """Custom type vc12TTPPathTraceReceived based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )
    fixed_length = 16


_Vc12TTPPathTraceReceived_Type.__name__ = "OctetString"
_Vc12TTPPathTraceReceived_Object = MibTableColumn
vc12TTPPathTraceReceived = _Vc12TTPPathTraceReceived_Object(
    (1, 3, 6, 1, 4, 1, 1038, 110, 150, 2, 1, 11),
    _Vc12TTPPathTraceReceived_Type()
)
vc12TTPPathTraceReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vc12TTPPathTraceReceived.setStatus("current")
_Vc12TTPLabelExpected_Type = Vc12TTPSignalLabel
_Vc12TTPLabelExpected_Object = MibTableColumn
vc12TTPLabelExpected = _Vc12TTPLabelExpected_Object(
    (1, 3, 6, 1, 4, 1, 1038, 110, 150, 2, 1, 12),
    _Vc12TTPLabelExpected_Type()
)
vc12TTPLabelExpected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vc12TTPLabelExpected.setStatus("current")
_Vc12TTPLabelSent_Type = Vc12TTPSignalLabel
_Vc12TTPLabelSent_Object = MibTableColumn
vc12TTPLabelSent = _Vc12TTPLabelSent_Object(
    (1, 3, 6, 1, 4, 1, 1038, 110, 150, 2, 1, 13),
    _Vc12TTPLabelSent_Type()
)
vc12TTPLabelSent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vc12TTPLabelSent.setStatus("current")
_Vc12TTPLabelReceived_Type = Vc12TTPSignalLabel
_Vc12TTPLabelReceived_Object = MibTableColumn
vc12TTPLabelReceived = _Vc12TTPLabelReceived_Object(
    (1, 3, 6, 1, 4, 1, 1038, 110, 150, 2, 1, 14),
    _Vc12TTPLabelReceived_Type()
)
vc12TTPLabelReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vc12TTPLabelReceived.setStatus("current")


class _Vc12TTPSdThreshold_Type(Integer32):
    """Custom type vc12TTPSdThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_Vc12TTPSdThreshold_Type.__name__ = "Integer32"
_Vc12TTPSdThreshold_Object = MibTableColumn
vc12TTPSdThreshold = _Vc12TTPSdThreshold_Object(
    (1, 3, 6, 1, 4, 1, 1038, 110, 150, 2, 1, 15),
    _Vc12TTPSdThreshold_Type()
)
vc12TTPSdThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vc12TTPSdThreshold.setStatus("current")


class _Vc12TTPSesThreshold_Type(Integer32):
    """Custom type vc12TTPSesThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_Vc12TTPSesThreshold_Type.__name__ = "Integer32"
_Vc12TTPSesThreshold_Object = MibTableColumn
vc12TTPSesThreshold = _Vc12TTPSesThreshold_Object(
    (1, 3, 6, 1, 4, 1, 1038, 110, 150, 2, 1, 16),
    _Vc12TTPSesThreshold_Type()
)
vc12TTPSesThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vc12TTPSesThreshold.setStatus("current")
_Vc12TTPBidirectionnal_Type = SagemBoolean
_Vc12TTPBidirectionnal_Object = MibTableColumn
vc12TTPBidirectionnal = _Vc12TTPBidirectionnal_Object(
    (1, 3, 6, 1, 4, 1, 1038, 110, 150, 2, 1, 17),
    _Vc12TTPBidirectionnal_Type()
)
vc12TTPBidirectionnal.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vc12TTPBidirectionnal.setStatus("current")
_Vc12TTPRdi_Type = Severity
_Vc12TTPRdi_Object = MibTableColumn
vc12TTPRdi = _Vc12TTPRdi_Object(
    (1, 3, 6, 1, 4, 1, 1038, 110, 150, 2, 1, 20),
    _Vc12TTPRdi_Type()
)
vc12TTPRdi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vc12TTPRdi.setStatus("current")
_Vc12TTPSd_Type = Severity
_Vc12TTPSd_Object = MibTableColumn
vc12TTPSd = _Vc12TTPSd_Object(
    (1, 3, 6, 1, 4, 1, 1038, 110, 150, 2, 1, 21),
    _Vc12TTPSd_Type()
)
vc12TTPSd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vc12TTPSd.setStatus("current")
_Vc12TTPUneq_Type = Severity
_Vc12TTPUneq_Object = MibTableColumn
vc12TTPUneq = _Vc12TTPUneq_Object(
    (1, 3, 6, 1, 4, 1, 1038, 110, 150, 2, 1, 22),
    _Vc12TTPUneq_Type()
)
vc12TTPUneq.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vc12TTPUneq.setStatus("current")
_Vc12TTPPlm_Type = Severity
_Vc12TTPPlm_Object = MibTableColumn
vc12TTPPlm = _Vc12TTPPlm_Object(
    (1, 3, 6, 1, 4, 1, 1038, 110, 150, 2, 1, 23),
    _Vc12TTPPlm_Type()
)
vc12TTPPlm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vc12TTPPlm.setStatus("current")
_Vc12TTPTim_Type = Severity
_Vc12TTPTim_Object = MibTableColumn
vc12TTPTim = _Vc12TTPTim_Object(
    (1, 3, 6, 1, 4, 1, 1038, 110, 150, 2, 1, 24),
    _Vc12TTPTim_Type()
)
vc12TTPTim.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vc12TTPTim.setStatus("current")
_NspiCTP_ObjectIdentity = ObjectIdentity
nspiCTP = _NspiCTP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1038, 110, 160)
)


class _NspiCTPNumber_Type(Integer32):
    """Custom type nspiCTPNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_NspiCTPNumber_Type.__name__ = "Integer32"
_NspiCTPNumber_Object = MibScalar
nspiCTPNumber = _NspiCTPNumber_Object(
    (1, 3, 6, 1, 4, 1, 1038, 110, 160, 1),
    _NspiCTPNumber_Type()
)
nspiCTPNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nspiCTPNumber.setStatus("current")
_NspiCTPTable_Object = MibTable
nspiCTPTable = _NspiCTPTable_Object(
    (1, 3, 6, 1, 4, 1, 1038, 110, 160, 2)
)
if mibBuilder.loadTexts:
    nspiCTPTable.setStatus("current")
_NspiCTPEntry_Object = MibTableRow
nspiCTPEntry = _NspiCTPEntry_Object(
    (1, 3, 6, 1, 4, 1, 1038, 110, 160, 2, 1)
)
nspiCTPEntry.setIndexNames(
    (0, "SDH-ETS-MIB", "nspiCTPIndex"),
)
if mibBuilder.loadTexts:
    nspiCTPEntry.setStatus("current")


class _NspiCTPIndex_Type(Integer32):
    """Custom type nspiCTPIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_NspiCTPIndex_Type.__name__ = "Integer32"
_NspiCTPIndex_Object = MibTableColumn
nspiCTPIndex = _NspiCTPIndex_Object(
    (1, 3, 6, 1, 4, 1, 1038, 110, 160, 2, 1, 1),
    _NspiCTPIndex_Type()
)
nspiCTPIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nspiCTPIndex.setStatus("current")
_NspiCTPTTPType_Type = NspiSrcType
_NspiCTPTTPType_Object = MibTableColumn
nspiCTPTTPType = _NspiCTPTTPType_Object(
    (1, 3, 6, 1, 4, 1, 1038, 110, 160, 2, 1, 2),
    _NspiCTPTTPType_Type()
)
nspiCTPTTPType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nspiCTPTTPType.setStatus("current")
_NspiCTPStatus_Type = CTPStatus
_NspiCTPStatus_Object = MibTableColumn
nspiCTPStatus = _NspiCTPStatus_Object(
    (1, 3, 6, 1, 4, 1, 1038, 110, 160, 2, 1, 3),
    _NspiCTPStatus_Type()
)
nspiCTPStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nspiCTPStatus.setStatus("current")
_NspiCTPName_Type = DisplayString
_NspiCTPName_Object = MibTableColumn
nspiCTPName = _NspiCTPName_Object(
    (1, 3, 6, 1, 4, 1, 1038, 110, 160, 2, 1, 4),
    _NspiCTPName_Type()
)
nspiCTPName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nspiCTPName.setStatus("current")
_NspiTTP_ObjectIdentity = ObjectIdentity
nspiTTP = _NspiTTP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1038, 110, 170)
)


class _NspiTTPNumber_Type(Integer32):
    """Custom type nspiTTPNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_NspiTTPNumber_Type.__name__ = "Integer32"
_NspiTTPNumber_Object = MibScalar
nspiTTPNumber = _NspiTTPNumber_Object(
    (1, 3, 6, 1, 4, 1, 1038, 110, 170, 1),
    _NspiTTPNumber_Type()
)
nspiTTPNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nspiTTPNumber.setStatus("current")
_NspiTTPTable_Object = MibTable
nspiTTPTable = _NspiTTPTable_Object(
    (1, 3, 6, 1, 4, 1, 1038, 110, 170, 2)
)
if mibBuilder.loadTexts:
    nspiTTPTable.setStatus("current")
_NspiTTPEntry_Object = MibTableRow
nspiTTPEntry = _NspiTTPEntry_Object(
    (1, 3, 6, 1, 4, 1, 1038, 110, 170, 2, 1)
)
nspiTTPEntry.setIndexNames(
    (0, "SDH-ETS-MIB", "nspiTTPIndex"),
)
if mibBuilder.loadTexts:
    nspiTTPEntry.setStatus("current")


class _NspiTTPIndex_Type(Integer32):
    """Custom type nspiTTPIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_NspiTTPIndex_Type.__name__ = "Integer32"
_NspiTTPIndex_Object = MibTableColumn
nspiTTPIndex = _NspiTTPIndex_Object(
    (1, 3, 6, 1, 4, 1, 1038, 110, 170, 2, 1, 1),
    _NspiTTPIndex_Type()
)
nspiTTPIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nspiTTPIndex.setStatus("current")
_NspiTTPType_Type = NspiTTPType
_NspiTTPType_Object = MibTableColumn
nspiTTPType = _NspiTTPType_Object(
    (1, 3, 6, 1, 4, 1, 1038, 110, 170, 2, 1, 2),
    _NspiTTPType_Type()
)
nspiTTPType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nspiTTPType.setStatus("current")
_NspiTTPLevel_Type = NspiTTPLevel
_NspiTTPLevel_Object = MibTableColumn
nspiTTPLevel = _NspiTTPLevel_Object(
    (1, 3, 6, 1, 4, 1, 1038, 110, 170, 2, 1, 3),
    _NspiTTPLevel_Type()
)
nspiTTPLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nspiTTPLevel.setStatus("current")
_NspiTTPName_Type = DisplayString
_NspiTTPName_Object = MibTableColumn
nspiTTPName = _NspiTTPName_Object(
    (1, 3, 6, 1, 4, 1, 1038, 110, 170, 2, 1, 4),
    _NspiTTPName_Type()
)
nspiTTPName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nspiTTPName.setStatus("current")


class _NspiTTPBoardIndex_Type(Integer32):
    """Custom type nspiTTPBoardIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_NspiTTPBoardIndex_Type.__name__ = "Integer32"
_NspiTTPBoardIndex_Object = MibTableColumn
nspiTTPBoardIndex = _NspiTTPBoardIndex_Object(
    (1, 3, 6, 1, 4, 1, 1038, 110, 170, 2, 1, 5),
    _NspiTTPBoardIndex_Type()
)
nspiTTPBoardIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nspiTTPBoardIndex.setStatus("current")


class _NspiTTPBoardAcces_Type(Integer32):
    """Custom type nspiTTPBoardAcces based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_NspiTTPBoardAcces_Type.__name__ = "Integer32"
_NspiTTPBoardAcces_Object = MibTableColumn
nspiTTPBoardAcces = _NspiTTPBoardAcces_Object(
    (1, 3, 6, 1, 4, 1, 1038, 110, 170, 2, 1, 6),
    _NspiTTPBoardAcces_Type()
)
nspiTTPBoardAcces.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nspiTTPBoardAcces.setStatus("current")
_NspiTTPSrcType_Type = NspiSrcType
_NspiTTPSrcType_Object = MibTableColumn
nspiTTPSrcType = _NspiTTPSrcType_Object(
    (1, 3, 6, 1, 4, 1, 1038, 110, 170, 2, 1, 7),
    _NspiTTPSrcType_Type()
)
nspiTTPSrcType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nspiTTPSrcType.setStatus("current")


class _NspiTTPSrcPointer_Type(Integer32):
    """Custom type nspiTTPSrcPointer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_NspiTTPSrcPointer_Type.__name__ = "Integer32"
_NspiTTPSrcPointer_Object = MibTableColumn
nspiTTPSrcPointer = _NspiTTPSrcPointer_Object(
    (1, 3, 6, 1, 4, 1, 1038, 110, 170, 2, 1, 8),
    _NspiTTPSrcPointer_Type()
)
nspiTTPSrcPointer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nspiTTPSrcPointer.setStatus("current")
_NspiTTPMonitor_Type = SagemBoolean
_NspiTTPMonitor_Object = MibTableColumn
nspiTTPMonitor = _NspiTTPMonitor_Object(
    (1, 3, 6, 1, 4, 1, 1038, 110, 170, 2, 1, 9),
    _NspiTTPMonitor_Type()
)
nspiTTPMonitor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nspiTTPMonitor.setStatus("current")
_NspiTTPFailure_Type = NspiTTPFailure
_NspiTTPFailure_Object = MibTableColumn
nspiTTPFailure = _NspiTTPFailure_Object(
    (1, 3, 6, 1, 4, 1, 1038, 110, 170, 2, 1, 10),
    _NspiTTPFailure_Type()
)
nspiTTPFailure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nspiTTPFailure.setStatus("current")
_NspiTTPSeverity_Type = Severity
_NspiTTPSeverity_Object = MibTableColumn
nspiTTPSeverity = _NspiTTPSeverity_Object(
    (1, 3, 6, 1, 4, 1, 1038, 110, 170, 2, 1, 11),
    _NspiTTPSeverity_Type()
)
nspiTTPSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nspiTTPSeverity.setStatus("current")
_NspiTTPLoopback_Type = Loopback
_NspiTTPLoopback_Object = MibTableColumn
nspiTTPLoopback = _NspiTTPLoopback_Object(
    (1, 3, 6, 1, 4, 1, 1038, 110, 170, 2, 1, 14),
    _NspiTTPLoopback_Type()
)
nspiTTPLoopback.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nspiTTPLoopback.setStatus("current")
_NspiTTPLos_Type = Severity
_NspiTTPLos_Object = MibTableColumn
nspiTTPLos = _NspiTTPLos_Object(
    (1, 3, 6, 1, 4, 1, 1038, 110, 170, 2, 1, 20),
    _NspiTTPLos_Type()
)
nspiTTPLos.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nspiTTPLos.setStatus("current")
_NspiTTPAis_Type = Severity
_NspiTTPAis_Object = MibTableColumn
nspiTTPAis = _NspiTTPAis_Object(
    (1, 3, 6, 1, 4, 1, 1038, 110, 170, 2, 1, 21),
    _NspiTTPAis_Type()
)
nspiTTPAis.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nspiTTPAis.setStatus("current")
_Channel_ObjectIdentity = ObjectIdentity
channel = _Channel_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1038, 110, 180)
)


class _ChannelNumber_Type(Integer32):
    """Custom type channelNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_ChannelNumber_Type.__name__ = "Integer32"
_ChannelNumber_Object = MibScalar
channelNumber = _ChannelNumber_Object(
    (1, 3, 6, 1, 4, 1, 1038, 110, 180, 1),
    _ChannelNumber_Type()
)
channelNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    channelNumber.setStatus("current")
_ChannelTable_Object = MibTable
channelTable = _ChannelTable_Object(
    (1, 3, 6, 1, 4, 1, 1038, 110, 180, 2)
)
if mibBuilder.loadTexts:
    channelTable.setStatus("current")
_ChannelEntry_Object = MibTableRow
channelEntry = _ChannelEntry_Object(
    (1, 3, 6, 1, 4, 1, 1038, 110, 180, 2, 1)
)
channelEntry.setIndexNames(
    (0, "SDH-ETS-MIB", "channelIndex"),
)
if mibBuilder.loadTexts:
    channelEntry.setStatus("current")


class _ChannelIndex_Type(Integer32):
    """Custom type channelIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_ChannelIndex_Type.__name__ = "Integer32"
_ChannelIndex_Object = MibTableColumn
channelIndex = _ChannelIndex_Object(
    (1, 3, 6, 1, 4, 1, 1038, 110, 180, 2, 1, 1),
    _ChannelIndex_Type()
)
channelIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    channelIndex.setStatus("current")
_ChannelEncaps_Type = ChannelEncaps
_ChannelEncaps_Object = MibTableColumn
channelEncaps = _ChannelEncaps_Object(
    (1, 3, 6, 1, 4, 1, 1038, 110, 180, 2, 1, 2),
    _ChannelEncaps_Type()
)
channelEncaps.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    channelEncaps.setStatus("current")


class _ChannelNbVc4_Type(Integer32):
    """Custom type channelNbVc4 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_ChannelNbVc4_Type.__name__ = "Integer32"
_ChannelNbVc4_Object = MibTableColumn
channelNbVc4 = _ChannelNbVc4_Object(
    (1, 3, 6, 1, 4, 1, 1038, 110, 180, 2, 1, 5),
    _ChannelNbVc4_Type()
)
channelNbVc4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    channelNbVc4.setStatus("current")


class _ChannelNbVc3_Type(Integer32):
    """Custom type channelNbVc3 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_ChannelNbVc3_Type.__name__ = "Integer32"
_ChannelNbVc3_Object = MibTableColumn
channelNbVc3 = _ChannelNbVc3_Object(
    (1, 3, 6, 1, 4, 1, 1038, 110, 180, 2, 1, 6),
    _ChannelNbVc3_Type()
)
channelNbVc3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    channelNbVc3.setStatus("current")


class _ChannelNbVc12_Type(Integer32):
    """Custom type channelNbVc12 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_ChannelNbVc12_Type.__name__ = "Integer32"
_ChannelNbVc12_Object = MibTableColumn
channelNbVc12 = _ChannelNbVc12_Object(
    (1, 3, 6, 1, 4, 1, 1038, 110, 180, 2, 1, 7),
    _ChannelNbVc12_Type()
)
channelNbVc12.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    channelNbVc12.setStatus("current")
_ChannelConcat_Type = ChannelConcat
_ChannelConcat_Object = MibTableColumn
channelConcat = _ChannelConcat_Object(
    (1, 3, 6, 1, 4, 1, 1038, 110, 180, 2, 1, 8),
    _ChannelConcat_Type()
)
channelConcat.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    channelConcat.setStatus("current")


class _ChannelAdminStatus_Type(Integer32):
    """Custom type channelAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("up", 1),
          ("down", 2),
          ("testing", 3))
    )


_ChannelAdminStatus_Type.__name__ = "Integer32"
_ChannelAdminStatus_Object = MibTableColumn
channelAdminStatus = _ChannelAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 1038, 110, 180, 2, 1, 9),
    _ChannelAdminStatus_Type()
)
channelAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    channelAdminStatus.setStatus("current")


class _ChannelOperStatus_Type(Integer32):
    """Custom type channelOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("up", 1),
          ("down", 2),
          ("testing", 3))
    )


_ChannelOperStatus_Type.__name__ = "Integer32"
_ChannelOperStatus_Object = MibTableColumn
channelOperStatus = _ChannelOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 1038, 110, 180, 2, 1, 10),
    _ChannelOperStatus_Type()
)
channelOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    channelOperStatus.setStatus("current")


class _ChannelFirstIndex_Type(Integer32):
    """Custom type channelFirstIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_ChannelFirstIndex_Type.__name__ = "Integer32"
_ChannelFirstIndex_Object = MibTableColumn
channelFirstIndex = _ChannelFirstIndex_Object(
    (1, 3, 6, 1, 4, 1, 1038, 110, 180, 2, 1, 11),
    _ChannelFirstIndex_Type()
)
channelFirstIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    channelFirstIndex.setStatus("current")


class _ChannelDelay_Type(Integer32):
    """Custom type channelDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_ChannelDelay_Type.__name__ = "Integer32"
_ChannelDelay_Object = MibTableColumn
channelDelay = _ChannelDelay_Object(
    (1, 3, 6, 1, 4, 1, 1038, 110, 180, 2, 1, 12),
    _ChannelDelay_Type()
)
channelDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    channelDelay.setStatus("current")
_ChannelMonitor_Type = SagemBoolean
_ChannelMonitor_Object = MibTableColumn
channelMonitor = _ChannelMonitor_Object(
    (1, 3, 6, 1, 4, 1, 1038, 110, 180, 2, 1, 13),
    _ChannelMonitor_Type()
)
channelMonitor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    channelMonitor.setStatus("current")
_ChannelFailure_Type = ChannelFailure
_ChannelFailure_Object = MibTableColumn
channelFailure = _ChannelFailure_Object(
    (1, 3, 6, 1, 4, 1, 1038, 110, 180, 2, 1, 14),
    _ChannelFailure_Type()
)
channelFailure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    channelFailure.setStatus("current")
_ChannelSeverity_Type = Severity
_ChannelSeverity_Object = MibTableColumn
channelSeverity = _ChannelSeverity_Object(
    (1, 3, 6, 1, 4, 1, 1038, 110, 180, 2, 1, 15),
    _ChannelSeverity_Type()
)
channelSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    channelSeverity.setStatus("current")
_ChannelLoa_Type = Severity
_ChannelLoa_Object = MibTableColumn
channelLoa = _ChannelLoa_Object(
    (1, 3, 6, 1, 4, 1, 1038, 110, 180, 2, 1, 16),
    _ChannelLoa_Type()
)
channelLoa.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    channelLoa.setStatus("current")
_ChannelLom_Type = Severity
_ChannelLom_Object = MibTableColumn
channelLom = _ChannelLom_Object(
    (1, 3, 6, 1, 4, 1, 1038, 110, 180, 2, 1, 17),
    _ChannelLom_Type()
)
channelLom.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    channelLom.setStatus("current")
_ChannelSqm_Type = Severity
_ChannelSqm_Object = MibTableColumn
channelSqm = _ChannelSqm_Object(
    (1, 3, 6, 1, 4, 1, 1038, 110, 180, 2, 1, 18),
    _ChannelSqm_Type()
)
channelSqm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    channelSqm.setStatus("current")
_Bandwidth_ObjectIdentity = ObjectIdentity
bandwidth = _Bandwidth_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1038, 110, 190)
)


class _BandwidthNumber_Type(Integer32):
    """Custom type bandwidthNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_BandwidthNumber_Type.__name__ = "Integer32"
_BandwidthNumber_Object = MibScalar
bandwidthNumber = _BandwidthNumber_Object(
    (1, 3, 6, 1, 4, 1, 1038, 110, 190, 1),
    _BandwidthNumber_Type()
)
bandwidthNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bandwidthNumber.setStatus("current")
_BandwidthTable_Object = MibTable
bandwidthTable = _BandwidthTable_Object(
    (1, 3, 6, 1, 4, 1, 1038, 110, 190, 2)
)
if mibBuilder.loadTexts:
    bandwidthTable.setStatus("current")
_BandwidthEntry_Object = MibTableRow
bandwidthEntry = _BandwidthEntry_Object(
    (1, 3, 6, 1, 4, 1, 1038, 110, 190, 2, 1)
)
bandwidthEntry.setIndexNames(
    (0, "SDH-ETS-MIB", "bandwidthIndex"),
)
if mibBuilder.loadTexts:
    bandwidthEntry.setStatus("current")


class _BandwidthIndex_Type(Integer32):
    """Custom type bandwidthIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_BandwidthIndex_Type.__name__ = "Integer32"
_BandwidthIndex_Object = MibTableColumn
bandwidthIndex = _BandwidthIndex_Object(
    (1, 3, 6, 1, 4, 1, 1038, 110, 190, 2, 1, 1),
    _BandwidthIndex_Type()
)
bandwidthIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bandwidthIndex.setStatus("current")


class _BandwidthBoardIndex_Type(Integer32):
    """Custom type bandwidthBoardIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_BandwidthBoardIndex_Type.__name__ = "Integer32"
_BandwidthBoardIndex_Object = MibTableColumn
bandwidthBoardIndex = _BandwidthBoardIndex_Object(
    (1, 3, 6, 1, 4, 1, 1038, 110, 190, 2, 1, 2),
    _BandwidthBoardIndex_Type()
)
bandwidthBoardIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bandwidthBoardIndex.setStatus("current")
_BandwidthSrcType_Type = NspiSrcType
_BandwidthSrcType_Object = MibTableColumn
bandwidthSrcType = _BandwidthSrcType_Object(
    (1, 3, 6, 1, 4, 1, 1038, 110, 190, 2, 1, 3),
    _BandwidthSrcType_Type()
)
bandwidthSrcType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bandwidthSrcType.setStatus("current")


class _BandwidthSrcPointer_Type(Integer32):
    """Custom type bandwidthSrcPointer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_BandwidthSrcPointer_Type.__name__ = "Integer32"
_BandwidthSrcPointer_Object = MibTableColumn
bandwidthSrcPointer = _BandwidthSrcPointer_Object(
    (1, 3, 6, 1, 4, 1, 1038, 110, 190, 2, 1, 4),
    _BandwidthSrcPointer_Type()
)
bandwidthSrcPointer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bandwidthSrcPointer.setStatus("current")
_BandwidthSinkType_Type = NspiSrcType
_BandwidthSinkType_Object = MibTableColumn
bandwidthSinkType = _BandwidthSinkType_Object(
    (1, 3, 6, 1, 4, 1, 1038, 110, 190, 2, 1, 5),
    _BandwidthSinkType_Type()
)
bandwidthSinkType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bandwidthSinkType.setStatus("current")


class _BandwidthSinkPointer_Type(Integer32):
    """Custom type bandwidthSinkPointer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_BandwidthSinkPointer_Type.__name__ = "Integer32"
_BandwidthSinkPointer_Object = MibTableColumn
bandwidthSinkPointer = _BandwidthSinkPointer_Object(
    (1, 3, 6, 1, 4, 1, 1038, 110, 190, 2, 1, 6),
    _BandwidthSinkPointer_Type()
)
bandwidthSinkPointer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bandwidthSinkPointer.setStatus("current")


class _BandwidthAdminStatus_Type(Integer32):
    """Custom type bandwidthAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("up", 1),
          ("down", 2),
          ("testing", 3))
    )


_BandwidthAdminStatus_Type.__name__ = "Integer32"
_BandwidthAdminStatus_Object = MibTableColumn
bandwidthAdminStatus = _BandwidthAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 1038, 110, 190, 2, 1, 7),
    _BandwidthAdminStatus_Type()
)
bandwidthAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bandwidthAdminStatus.setStatus("current")


class _BandwidthOperStatus_Type(Integer32):
    """Custom type bandwidthOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("up", 1),
          ("down", 2),
          ("testing", 3))
    )


_BandwidthOperStatus_Type.__name__ = "Integer32"
_BandwidthOperStatus_Object = MibTableColumn
bandwidthOperStatus = _BandwidthOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 1038, 110, 190, 2, 1, 8),
    _BandwidthOperStatus_Type()
)
bandwidthOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bandwidthOperStatus.setStatus("current")


class _BandwidthPrevIndex_Type(Integer32):
    """Custom type bandwidthPrevIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_BandwidthPrevIndex_Type.__name__ = "Integer32"
_BandwidthPrevIndex_Object = MibTableColumn
bandwidthPrevIndex = _BandwidthPrevIndex_Object(
    (1, 3, 6, 1, 4, 1, 1038, 110, 190, 2, 1, 9),
    _BandwidthPrevIndex_Type()
)
bandwidthPrevIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bandwidthPrevIndex.setStatus("current")


class _BandwidthNextIndex_Type(Integer32):
    """Custom type bandwidthNextIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_BandwidthNextIndex_Type.__name__ = "Integer32"
_BandwidthNextIndex_Object = MibTableColumn
bandwidthNextIndex = _BandwidthNextIndex_Object(
    (1, 3, 6, 1, 4, 1, 1038, 110, 190, 2, 1, 10),
    _BandwidthNextIndex_Type()
)
bandwidthNextIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bandwidthNextIndex.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SDH-ETS-MIB",
    **{"SpiTTPFailure": SpiTTPFailure,
       "Loopback": Loopback,
       "STMLevel": STMLevel,
       "SpiTTPType": SpiTTPType,
       "RsTTPFailure": RsTTPFailure,
       "EOWMode": EOWMode,
       "ProtectionType": ProtectionType,
       "MsTTPFailure": MsTTPFailure,
       "MsaSrcType": MsaSrcType,
       "MsaSinkType": MsaSinkType,
       "CTPStatus": CTPStatus,
       "Au4CTPFailure": Au4CTPFailure,
       "Au4CTPCnxType": Au4CTPCnxType,
       "Vc4TTPSinkType": Vc4TTPSinkType,
       "Vc4TTPTraceMode": Vc4TTPTraceMode,
       "Vc4TTPSignalLabel": Vc4TTPSignalLabel,
       "Vc4TTPFailure": Vc4TTPFailure,
       "Tu3CTPFailure": Tu3CTPFailure,
       "Tu12CTPFailure": Tu12CTPFailure,
       "Vc3TTPSinkType": Vc3TTPSinkType,
       "Vc3TTPSignalLabel": Vc3TTPSignalLabel,
       "VcLoFailure": VcLoFailure,
       "Vc12TTPSinkType": Vc12TTPSinkType,
       "Vc12TTPSignalLabel": Vc12TTPSignalLabel,
       "NspiSrcType": NspiSrcType,
       "NspiTTPFailure": NspiTTPFailure,
       "NspiTTPType": NspiTTPType,
       "NspiTTPLevel": NspiTTPLevel,
       "ChannelEncaps": ChannelEncaps,
       "ChannelConcat": ChannelConcat,
       "ChannelFailure": ChannelFailure,
       "sdhEts": sdhEts,
       "spiTTP": spiTTP,
       "spiTTPNumber": spiTTPNumber,
       "spiTTPTable": spiTTPTable,
       "spiTTPEntry": spiTTPEntry,
       "spiTTPIndex": spiTTPIndex,
       "spiTTPStmLevel": spiTTPStmLevel,
       "spiTTPType": spiTTPType,
       "spiTTPName": spiTTPName,
       "spiTTPBoardIndex": spiTTPBoardIndex,
       "spiTTPBoardAcces": spiTTPBoardAcces,
       "spiTTPMonitor": spiTTPMonitor,
       "spiTTPFailure": spiTTPFailure,
       "spiTTPSeverity": spiTTPSeverity,
       "spiTTPLoopback": spiTTPLoopback,
       "spiTTPLos": spiTTPLos,
       "spiTTPTf": spiTTPTf,
       "rsTTP": rsTTP,
       "rsTTPTable": rsTTPTable,
       "rsTTPEntry": rsTTPEntry,
       "rsTTPIndex": rsTTPIndex,
       "rsTTPMonitor": rsTTPMonitor,
       "rsTTPName": rsTTPName,
       "rsTTPFailure": rsTTPFailure,
       "rsTTPSeverity": rsTTPSeverity,
       "rsTTPEOWMode": rsTTPEOWMode,
       "rsTTPE1SrcPointer": rsTTPE1SrcPointer,
       "rsTTPF1SrcPointer": rsTTPF1SrcPointer,
       "rsTTPSesThreshold": rsTTPSesThreshold,
       "rsTTPEOWByteLine": rsTTPEOWByteLine,
       "rsTTPEOWByteColumn": rsTTPEOWByteColumn,
       "rsTTPLof": rsTTPLof,
       "rsCTP": rsCTP,
       "msTTP": msTTP,
       "msTTPTable": msTTPTable,
       "msTTPEntry": msTTPEntry,
       "msTTPIndex": msTTPIndex,
       "msTTPProtectionType": msTTPProtectionType,
       "msTTPMonitor": msTTPMonitor,
       "msTTPName": msTTPName,
       "msTTPFailure": msTTPFailure,
       "msTTPSeverity": msTTPSeverity,
       "msTTPEOWMode": msTTPEOWMode,
       "msTTPE2SrcPointer": msTTPE2SrcPointer,
       "msTTPEOWByteLine": msTTPEOWByteLine,
       "msTTPEOWByteColumn": msTTPEOWByteColumn,
       "msTTPMonEber": msTTPMonEber,
       "msTTPSdThreshold": msTTPSdThreshold,
       "msTTPSesThreshold": msTTPSesThreshold,
       "msTTPEber": msTTPEber,
       "msTTPSd": msTTPSd,
       "msTTPRdi": msTTPRdi,
       "msCTP": msCTP,
       "msa": msa,
       "msaTable": msaTable,
       "msaEntry": msaEntry,
       "msaIndex": msaIndex,
       "msaSTMLevel": msaSTMLevel,
       "msaSinkType": msaSinkType,
       "msaSinkPointer": msaSinkPointer,
       "msaName": msaName,
       "msaSrc1Type": msaSrc1Type,
       "msaSrc2Type": msaSrc2Type,
       "msaSrc3Type": msaSrc3Type,
       "msaSrc4Type": msaSrc4Type,
       "msaSrc1Pointer": msaSrc1Pointer,
       "msaSrc2Pointer": msaSrc2Pointer,
       "msaSrc3Pointer": msaSrc3Pointer,
       "msaSrc4Pointer": msaSrc4Pointer,
       "au4CTP": au4CTP,
       "au4CTPNumber": au4CTPNumber,
       "au4CTPTable": au4CTPTable,
       "au4CTPEntry": au4CTPEntry,
       "au4CTPIndex": au4CTPIndex,
       "au4CTPStatus": au4CTPStatus,
       "au4CTPCnxType": au4CTPCnxType,
       "au4CTPName": au4CTPName,
       "au4CTPMonitor": au4CTPMonitor,
       "au4CTPFailure": au4CTPFailure,
       "au4CTPSeverity": au4CTPSeverity,
       "au4CTPAis": au4CTPAis,
       "au4CTPLop": au4CTPLop,
       "au4CTPLom": au4CTPLom,
       "vc4TTP": vc4TTP,
       "vc4TTPNumber": vc4TTPNumber,
       "vc4TTPTable": vc4TTPTable,
       "vc4TTPEntry": vc4TTPEntry,
       "vc4TTPIndex": vc4TTPIndex,
       "vc4TTPSinkPointer": vc4TTPSinkPointer,
       "vc4TTPSinkType": vc4TTPSinkType,
       "vc4TTPName": vc4TTPName,
       "vc4TTPMonitor": vc4TTPMonitor,
       "vc4TTPFailure": vc4TTPFailure,
       "vc4TTPSeverity": vc4TTPSeverity,
       "vc4TTPTraceMode": vc4TTPTraceMode,
       "vc4TTPPathTraceExpected": vc4TTPPathTraceExpected,
       "vc4TTPPathTraceSent": vc4TTPPathTraceSent,
       "vc4TTPPathTraceReceived": vc4TTPPathTraceReceived,
       "vc4TTPLabelExpected": vc4TTPLabelExpected,
       "vc4TTPLabelSent": vc4TTPLabelSent,
       "vc4TTPLabelReceived": vc4TTPLabelReceived,
       "vc4TTPSdThreshold": vc4TTPSdThreshold,
       "vc4TTPSesThreshold": vc4TTPSesThreshold,
       "vc4TTPBidirectionnal": vc4TTPBidirectionnal,
       "vc4TTPRdi": vc4TTPRdi,
       "vc4TTPSd": vc4TTPSd,
       "vc4TTPUneq": vc4TTPUneq,
       "vc4TTPPlm": vc4TTPPlm,
       "vc4TTPTimDis": vc4TTPTimDis,
       "vc4TTPTim": vc4TTPTim,
       "tu3CTP": tu3CTP,
       "tu3CTPNumber": tu3CTPNumber,
       "tu3CTPTable": tu3CTPTable,
       "tu3CTPEntry": tu3CTPEntry,
       "tu3CTPIndex": tu3CTPIndex,
       "tu3CTPStatus": tu3CTPStatus,
       "tu3CTPName": tu3CTPName,
       "tu3CTPMonitor": tu3CTPMonitor,
       "tu3CTPFailure": tu3CTPFailure,
       "tu3CTPSeverity": tu3CTPSeverity,
       "tu3CTPAis": tu3CTPAis,
       "tu3CTPLop": tu3CTPLop,
       "vc3TTP": vc3TTP,
       "vc3TTPNumber": vc3TTPNumber,
       "vc3TTPTable": vc3TTPTable,
       "vc3TTPEntry": vc3TTPEntry,
       "vc3TTPIndex": vc3TTPIndex,
       "vc3TTPSinkPointer": vc3TTPSinkPointer,
       "vc3TTPSinkType": vc3TTPSinkType,
       "vc3TTPName": vc3TTPName,
       "vc3TTPMonitor": vc3TTPMonitor,
       "vc3TTPFailure": vc3TTPFailure,
       "vc3TTPSeverity": vc3TTPSeverity,
       "vc3TTPPathTraceExpected": vc3TTPPathTraceExpected,
       "vc3TTPPathTraceSent": vc3TTPPathTraceSent,
       "vc3TTPPathTraceReceived": vc3TTPPathTraceReceived,
       "vc3TTPLabelExpected": vc3TTPLabelExpected,
       "vc3TTPLabelSent": vc3TTPLabelSent,
       "vc3TTPLabelReceived": vc3TTPLabelReceived,
       "vc3TTPSdThreshold": vc3TTPSdThreshold,
       "vc3TTPSesThreshold": vc3TTPSesThreshold,
       "vc3TTPBidirectionnal": vc3TTPBidirectionnal,
       "vc3TTPRdi": vc3TTPRdi,
       "vc3TTPSd": vc3TTPSd,
       "vc3TTPUneq": vc3TTPUneq,
       "vc3TTPPlm": vc3TTPPlm,
       "vc3TTPTim": vc3TTPTim,
       "tu12CTP": tu12CTP,
       "tu12CTPNumber": tu12CTPNumber,
       "tu12CTPTable": tu12CTPTable,
       "tu12CTPEntry": tu12CTPEntry,
       "tu12CTPIndex": tu12CTPIndex,
       "tu12CTPStatus": tu12CTPStatus,
       "tu12CTPName": tu12CTPName,
       "tu12CTPMonitor": tu12CTPMonitor,
       "tu12CTPFailure": tu12CTPFailure,
       "tu12CTPSeverity": tu12CTPSeverity,
       "tu12CTPAis": tu12CTPAis,
       "tu12CTPLop": tu12CTPLop,
       "vc12TTP": vc12TTP,
       "vc12TTPNumber": vc12TTPNumber,
       "vc12TTPTable": vc12TTPTable,
       "vc12TTPEntry": vc12TTPEntry,
       "vc12TTPIndex": vc12TTPIndex,
       "vc12TTPSinkPointer": vc12TTPSinkPointer,
       "vc12TTPSinkType": vc12TTPSinkType,
       "vc12TTPName": vc12TTPName,
       "vc12TTPMonitor": vc12TTPMonitor,
       "vc12TTPFailure": vc12TTPFailure,
       "vc12TTPSeverity": vc12TTPSeverity,
       "vc12TTPPathTraceExpected": vc12TTPPathTraceExpected,
       "vc12TTPPathTraceSent": vc12TTPPathTraceSent,
       "vc12TTPPathTraceReceived": vc12TTPPathTraceReceived,
       "vc12TTPLabelExpected": vc12TTPLabelExpected,
       "vc12TTPLabelSent": vc12TTPLabelSent,
       "vc12TTPLabelReceived": vc12TTPLabelReceived,
       "vc12TTPSdThreshold": vc12TTPSdThreshold,
       "vc12TTPSesThreshold": vc12TTPSesThreshold,
       "vc12TTPBidirectionnal": vc12TTPBidirectionnal,
       "vc12TTPRdi": vc12TTPRdi,
       "vc12TTPSd": vc12TTPSd,
       "vc12TTPUneq": vc12TTPUneq,
       "vc12TTPPlm": vc12TTPPlm,
       "vc12TTPTim": vc12TTPTim,
       "nspiCTP": nspiCTP,
       "nspiCTPNumber": nspiCTPNumber,
       "nspiCTPTable": nspiCTPTable,
       "nspiCTPEntry": nspiCTPEntry,
       "nspiCTPIndex": nspiCTPIndex,
       "nspiCTPTTPType": nspiCTPTTPType,
       "nspiCTPStatus": nspiCTPStatus,
       "nspiCTPName": nspiCTPName,
       "nspiTTP": nspiTTP,
       "nspiTTPNumber": nspiTTPNumber,
       "nspiTTPTable": nspiTTPTable,
       "nspiTTPEntry": nspiTTPEntry,
       "nspiTTPIndex": nspiTTPIndex,
       "nspiTTPType": nspiTTPType,
       "nspiTTPLevel": nspiTTPLevel,
       "nspiTTPName": nspiTTPName,
       "nspiTTPBoardIndex": nspiTTPBoardIndex,
       "nspiTTPBoardAcces": nspiTTPBoardAcces,
       "nspiTTPSrcType": nspiTTPSrcType,
       "nspiTTPSrcPointer": nspiTTPSrcPointer,
       "nspiTTPMonitor": nspiTTPMonitor,
       "nspiTTPFailure": nspiTTPFailure,
       "nspiTTPSeverity": nspiTTPSeverity,
       "nspiTTPLoopback": nspiTTPLoopback,
       "nspiTTPLos": nspiTTPLos,
       "nspiTTPAis": nspiTTPAis,
       "channel": channel,
       "channelNumber": channelNumber,
       "channelTable": channelTable,
       "channelEntry": channelEntry,
       "channelIndex": channelIndex,
       "channelEncaps": channelEncaps,
       "channelNbVc4": channelNbVc4,
       "channelNbVc3": channelNbVc3,
       "channelNbVc12": channelNbVc12,
       "channelConcat": channelConcat,
       "channelAdminStatus": channelAdminStatus,
       "channelOperStatus": channelOperStatus,
       "channelFirstIndex": channelFirstIndex,
       "channelDelay": channelDelay,
       "channelMonitor": channelMonitor,
       "channelFailure": channelFailure,
       "channelSeverity": channelSeverity,
       "channelLoa": channelLoa,
       "channelLom": channelLom,
       "channelSqm": channelSqm,
       "bandwidth": bandwidth,
       "bandwidthNumber": bandwidthNumber,
       "bandwidthTable": bandwidthTable,
       "bandwidthEntry": bandwidthEntry,
       "bandwidthIndex": bandwidthIndex,
       "bandwidthBoardIndex": bandwidthBoardIndex,
       "bandwidthSrcType": bandwidthSrcType,
       "bandwidthSrcPointer": bandwidthSrcPointer,
       "bandwidthSinkType": bandwidthSinkType,
       "bandwidthSinkPointer": bandwidthSinkPointer,
       "bandwidthAdminStatus": bandwidthAdminStatus,
       "bandwidthOperStatus": bandwidthOperStatus,
       "bandwidthPrevIndex": bandwidthPrevIndex,
       "bandwidthNextIndex": bandwidthNextIndex}
)
