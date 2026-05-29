# SNMP MIB module (PRVT-PW-TDM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\telco-systems\binos\PRVT-PW-TDM-MIB

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

(switch,) = mibBuilder.importSymbols(
    "PRVT-SWITCH-MIB",
    "switch")

(PerfCurrentCount,
 PerfIntervalCount) = mibBuilder.importSymbols(
    "PerfHist-TC-MIB",
    "PerfCurrentCount",
    "PerfIntervalCount")

(PortList,) = mibBuilder.importSymbols(
    "Q-BRIDGE-MIB",
    "PortList")

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
 transmission) = mibBuilder.importSymbols(
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
    "transmission")

(DisplayString,
 PhysAddress,
 RowStatus,
 StorageType,
 TextualConvention,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "StorageType",
    "TextualConvention",
    "TimeStamp",
    "TruthValue")


# MODULE-IDENTITY

prvtPwVcTDMMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 200, 2)
)
if mibBuilder.loadTexts:
    prvtPwVcTDMMIB.setRevisions(
        ("2019-02-27 00:00",
         "2009-07-07 00:00",
         "2009-07-01 00:00",
         "2009-03-06 00:00",
         "2009-03-05 00:00",
         "2009-02-18 00:00",
         "2009-01-15 00:00",
         "2008-06-19 00:00",
         "2006-07-24 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class PrvtPwVcTDMCfgIndex(TextualConvention, Unsigned32):
    status = "current"


class TimeSlotList(TextualConvention, OctetString):
    status = "current"


class PrvtPwVcTDMCfgInterface(TextualConvention, IpAddress):
    status = "current"


class InterfaceTimeSlot(TextualConvention, OctetString):
    status = "current"


# MIB Managed Objects in the order of their OIDs

_PrvtPwVc_ObjectIdentity = ObjectIdentity
prvtPwVc = _PrvtPwVc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 200)
)
_PrvtPwVcTDMObjects_ObjectIdentity = ObjectIdentity
prvtPwVcTDMObjects = _PrvtPwVcTDMObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 200, 2, 1)
)
_PrvtPwVcTDMTable_Object = MibTable
prvtPwVcTDMTable = _PrvtPwVcTDMTable_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 200, 2, 1, 1)
)
if mibBuilder.loadTexts:
    prvtPwVcTDMTable.setStatus("current")
_PrvtPwVcTDMEntry_Object = MibTableRow
prvtPwVcTDMEntry = _PrvtPwVcTDMEntry_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 200, 2, 1, 1, 1)
)
prvtPwVcTDMEntry.setIndexNames(
    (0, "PRVT-PW-TDM-MIB", "prvtPwVcTDMModuleId"),
    (0, "PRVT-PW-TDM-MIB", "prvtPwVcTDMCircuitId"),
)
if mibBuilder.loadTexts:
    prvtPwVcTDMEntry.setStatus("current")


class _PrvtPwVcTDMModuleId_Type(Integer32):
    """Custom type prvtPwVcTDMModuleId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_PrvtPwVcTDMModuleId_Type.__name__ = "Integer32"
_PrvtPwVcTDMModuleId_Object = MibTableColumn
prvtPwVcTDMModuleId = _PrvtPwVcTDMModuleId_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 200, 2, 1, 1, 1, 1),
    _PrvtPwVcTDMModuleId_Type()
)
prvtPwVcTDMModuleId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtPwVcTDMModuleId.setStatus("current")


class _PrvtPwVcTDMCircuitId_Type(Integer32):
    """Custom type prvtPwVcTDMCircuitId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_PrvtPwVcTDMCircuitId_Type.__name__ = "Integer32"
_PrvtPwVcTDMCircuitId_Object = MibTableColumn
prvtPwVcTDMCircuitId = _PrvtPwVcTDMCircuitId_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 200, 2, 1, 1, 1, 2),
    _PrvtPwVcTDMCircuitId_Type()
)
prvtPwVcTDMCircuitId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtPwVcTDMCircuitId.setStatus("current")


class _PrvtPwVcTDMType_Type(Integer32):
    """Custom type prvtPwVcTDMType based on Integer32"""
    defaultValue = 3

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
              9,
              10)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("ds1", 2),
          ("e1", 3),
          ("ds3", 4),
          ("e3", 5),
          ("octetAlignedT1", 6),
          ("nXds0", 7),
          ("nXds0WithCASe1", 8),
          ("nXds0WithCASds1Esf", 9),
          ("nXds0WithCASds1Sf", 10))
    )


_PrvtPwVcTDMType_Type.__name__ = "Integer32"
_PrvtPwVcTDMType_Object = MibTableColumn
prvtPwVcTDMType = _PrvtPwVcTDMType_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 200, 2, 1, 1, 1, 3),
    _PrvtPwVcTDMType_Type()
)
prvtPwVcTDMType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtPwVcTDMType.setStatus("current")
_PrvtPwVcRelTDMCfgIndex_Type = PrvtPwVcTDMCfgIndex
_PrvtPwVcRelTDMCfgIndex_Object = MibTableColumn
prvtPwVcRelTDMCfgIndex = _PrvtPwVcRelTDMCfgIndex_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 200, 2, 1, 1, 1, 4),
    _PrvtPwVcRelTDMCfgIndex_Type()
)
prvtPwVcRelTDMCfgIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtPwVcRelTDMCfgIndex.setStatus("current")


class _PrvtPwVcTDMTimeElapsed_Type(Integer32):
    """Custom type prvtPwVcTDMTimeElapsed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 900),
    )


_PrvtPwVcTDMTimeElapsed_Type.__name__ = "Integer32"
_PrvtPwVcTDMTimeElapsed_Object = MibTableColumn
prvtPwVcTDMTimeElapsed = _PrvtPwVcTDMTimeElapsed_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 200, 2, 1, 1, 1, 5),
    _PrvtPwVcTDMTimeElapsed_Type()
)
prvtPwVcTDMTimeElapsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtPwVcTDMTimeElapsed.setStatus("current")


class _PrvtPwVcTDMValidIntervals_Type(Integer32):
    """Custom type prvtPwVcTDMValidIntervals based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 96),
    )


_PrvtPwVcTDMValidIntervals_Type.__name__ = "Integer32"
_PrvtPwVcTDMValidIntervals_Object = MibTableColumn
prvtPwVcTDMValidIntervals = _PrvtPwVcTDMValidIntervals_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 200, 2, 1, 1, 1, 6),
    _PrvtPwVcTDMValidIntervals_Type()
)
prvtPwVcTDMValidIntervals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtPwVcTDMValidIntervals.setStatus("current")


class _PrvtPwVcTDMCurrentIndications_Type(Bits):
    """Custom type prvtPwVcTDMCurrentIndications based on Bits"""
    namedValues = NamedValues(
        *(("other", 0),
          ("strayPacket", 1),
          ("malformedPacket", 2),
          ("excessivePktLossRate", 3),
          ("bufferOverrun", 4),
          ("bufferUnderrun", 5),
          ("remotePktLoss", 6),
          ("packetLoss", 7),
          ("tdmFault", 8),
          ("packetsLbitCounter", 9),
          ("packetsRbitCounter", 10))
    )

_PrvtPwVcTDMCurrentIndications_Type.__name__ = "Bits"
_PrvtPwVcTDMCurrentIndications_Object = MibTableColumn
prvtPwVcTDMCurrentIndications = _PrvtPwVcTDMCurrentIndications_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 200, 2, 1, 1, 1, 7),
    _PrvtPwVcTDMCurrentIndications_Type()
)
prvtPwVcTDMCurrentIndications.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtPwVcTDMCurrentIndications.setStatus("current")


class _PrvtPwVcTDMLatchedIndications_Type(Bits):
    """Custom type prvtPwVcTDMLatchedIndications based on Bits"""
    namedValues = NamedValues(
        *(("other", 0),
          ("staryPacket", 1),
          ("malformedPacket", 2),
          ("excessivePktLossRate", 3),
          ("bufferOverrun", 4),
          ("bufferUnderrun", 5),
          ("remotePktLoss", 6),
          ("packetLoss", 7),
          ("tdmFault", 8),
          ("packetsLbitCounter", 9),
          ("packetsRbitCounter", 10))
    )

_PrvtPwVcTDMLatchedIndications_Type.__name__ = "Bits"
_PrvtPwVcTDMLatchedIndications_Object = MibTableColumn
prvtPwVcTDMLatchedIndications = _PrvtPwVcTDMLatchedIndications_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 200, 2, 1, 1, 1, 8),
    _PrvtPwVcTDMLatchedIndications_Type()
)
prvtPwVcTDMLatchedIndications.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtPwVcTDMLatchedIndications.setStatus("current")
_PrvtPwVcTDMLastEsTimeStamp_Type = TimeStamp
_PrvtPwVcTDMLastEsTimeStamp_Object = MibTableColumn
prvtPwVcTDMLastEsTimeStamp = _PrvtPwVcTDMLastEsTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 200, 2, 1, 1, 1, 9),
    _PrvtPwVcTDMLastEsTimeStamp_Type()
)
prvtPwVcTDMLastEsTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtPwVcTDMLastEsTimeStamp.setStatus("current")


class _PrvtPwVcTDMEmulationMode_Type(Integer32):
    """Custom type prvtPwVcTDMEmulationMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("undefined", 0),
          ("structured", 1),
          ("unstuctured", 2))
    )


_PrvtPwVcTDMEmulationMode_Type.__name__ = "Integer32"
_PrvtPwVcTDMEmulationMode_Object = MibTableColumn
prvtPwVcTDMEmulationMode = _PrvtPwVcTDMEmulationMode_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 200, 2, 1, 1, 1, 10),
    _PrvtPwVcTDMEmulationMode_Type()
)
prvtPwVcTDMEmulationMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtPwVcTDMEmulationMode.setStatus("current")


class _PrvtPwVcTDMOperStatus_Type(Integer32):
    """Custom type prvtPwVcTDMOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("up", 1),
          ("down", 2))
    )


_PrvtPwVcTDMOperStatus_Type.__name__ = "Integer32"
_PrvtPwVcTDMOperStatus_Object = MibTableColumn
prvtPwVcTDMOperStatus = _PrvtPwVcTDMOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 200, 2, 1, 1, 1, 11),
    _PrvtPwVcTDMOperStatus_Type()
)
prvtPwVcTDMOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtPwVcTDMOperStatus.setStatus("current")


class _PrvtPwVcTDMClearCircuitStatistics_Type(Integer32):
    """Custom type prvtPwVcTDMClearCircuitStatistics based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("clear", 1))
    )


_PrvtPwVcTDMClearCircuitStatistics_Type.__name__ = "Integer32"
_PrvtPwVcTDMClearCircuitStatistics_Object = MibTableColumn
prvtPwVcTDMClearCircuitStatistics = _PrvtPwVcTDMClearCircuitStatistics_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 200, 2, 1, 1, 1, 12),
    _PrvtPwVcTDMClearCircuitStatistics_Type()
)
prvtPwVcTDMClearCircuitStatistics.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prvtPwVcTDMClearCircuitStatistics.setStatus("current")
_PrvtPwVcTDMCfgTable_Object = MibTable
prvtPwVcTDMCfgTable = _PrvtPwVcTDMCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 200, 2, 1, 3)
)
if mibBuilder.loadTexts:
    prvtPwVcTDMCfgTable.setStatus("current")
_PrvtPwVcTDMCfgEntry_Object = MibTableRow
prvtPwVcTDMCfgEntry = _PrvtPwVcTDMCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 200, 2, 1, 3, 1)
)
prvtPwVcTDMCfgEntry.setIndexNames(
    (0, "PRVT-PW-TDM-MIB", "prvtPwVcTDMModuleId"),
    (0, "PRVT-PW-TDM-MIB", "prvtPwVcTDMCircuitId"),
)
if mibBuilder.loadTexts:
    prvtPwVcTDMCfgEntry.setStatus("current")
_PrvtPwVcTDMCfgPayloadSize_Type = Unsigned32
_PrvtPwVcTDMCfgPayloadSize_Object = MibTableColumn
prvtPwVcTDMCfgPayloadSize = _PrvtPwVcTDMCfgPayloadSize_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 200, 2, 1, 3, 1, 1),
    _PrvtPwVcTDMCfgPayloadSize_Type()
)
prvtPwVcTDMCfgPayloadSize.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    prvtPwVcTDMCfgPayloadSize.setStatus("current")
_PrvtPwVcTDMCfgPktReorder_Type = TruthValue
_PrvtPwVcTDMCfgPktReorder_Object = MibTableColumn
prvtPwVcTDMCfgPktReorder = _PrvtPwVcTDMCfgPktReorder_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 200, 2, 1, 3, 1, 2),
    _PrvtPwVcTDMCfgPktReorder_Type()
)
prvtPwVcTDMCfgPktReorder.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    prvtPwVcTDMCfgPktReorder.setStatus("current")


class _PrvtPwVcTDMCfgRtpHdrUsed_Type(TruthValue):
    """Custom type prvtPwVcTDMCfgRtpHdrUsed based on TruthValue"""
    defaultValue = 2


_PrvtPwVcTDMCfgRtpHdrUsed_Type.__name__ = "TruthValue"
_PrvtPwVcTDMCfgRtpHdrUsed_Object = MibTableColumn
prvtPwVcTDMCfgRtpHdrUsed = _PrvtPwVcTDMCfgRtpHdrUsed_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 200, 2, 1, 3, 1, 3),
    _PrvtPwVcTDMCfgRtpHdrUsed_Type()
)
prvtPwVcTDMCfgRtpHdrUsed.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    prvtPwVcTDMCfgRtpHdrUsed.setStatus("current")


class _PrvtPwVcTDMCfgJtrBfrDepth_Type(Unsigned32):
    """Custom type prvtPwVcTDMCfgJtrBfrDepth based on Unsigned32"""
    defaultValue = 3

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 200),
    )


_PrvtPwVcTDMCfgJtrBfrDepth_Type.__name__ = "Unsigned32"
_PrvtPwVcTDMCfgJtrBfrDepth_Object = MibTableColumn
prvtPwVcTDMCfgJtrBfrDepth = _PrvtPwVcTDMCfgJtrBfrDepth_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 200, 2, 1, 3, 1, 4),
    _PrvtPwVcTDMCfgJtrBfrDepth_Type()
)
prvtPwVcTDMCfgJtrBfrDepth.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    prvtPwVcTDMCfgJtrBfrDepth.setStatus("current")
if mibBuilder.loadTexts:
    prvtPwVcTDMCfgJtrBfrDepth.setUnits("millisecond")


class _PrvtPwVcTDMCfgChannelGroup_Type(Integer32):
    """Custom type prvtPwVcTDMCfgChannelGroup based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 128),
    )


_PrvtPwVcTDMCfgChannelGroup_Type.__name__ = "Integer32"
_PrvtPwVcTDMCfgChannelGroup_Object = MibTableColumn
prvtPwVcTDMCfgChannelGroup = _PrvtPwVcTDMCfgChannelGroup_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 200, 2, 1, 3, 1, 5),
    _PrvtPwVcTDMCfgChannelGroup_Type()
)
prvtPwVcTDMCfgChannelGroup.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    prvtPwVcTDMCfgChannelGroup.setStatus("current")
_PrvtPwVcTDMCfgPorts_Type = OctetString
_PrvtPwVcTDMCfgPorts_Object = MibTableColumn
prvtPwVcTDMCfgPorts = _PrvtPwVcTDMCfgPorts_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 200, 2, 1, 3, 1, 6),
    _PrvtPwVcTDMCfgPorts_Type()
)
prvtPwVcTDMCfgPorts.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    prvtPwVcTDMCfgPorts.setStatus("current")


class _PrvtPwVcTDMCfgPeerIpType_Type(Integer32):
    """Custom type prvtPwVcTDMCfgPeerIpType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(4,
              6,
              16)
        )
    )
    namedValues = NamedValues(
        *(("ipv4", 4),
          ("ipv6", 6),
          ("dns", 16))
    )


_PrvtPwVcTDMCfgPeerIpType_Type.__name__ = "Integer32"
_PrvtPwVcTDMCfgPeerIpType_Object = MibTableColumn
prvtPwVcTDMCfgPeerIpType = _PrvtPwVcTDMCfgPeerIpType_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 200, 2, 1, 3, 1, 7),
    _PrvtPwVcTDMCfgPeerIpType_Type()
)
prvtPwVcTDMCfgPeerIpType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    prvtPwVcTDMCfgPeerIpType.setStatus("current")
_PrvtPwVcTDMCfgPeerIpAddress_Type = IpAddress
_PrvtPwVcTDMCfgPeerIpAddress_Object = MibTableColumn
prvtPwVcTDMCfgPeerIpAddress = _PrvtPwVcTDMCfgPeerIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 200, 2, 1, 3, 1, 8),
    _PrvtPwVcTDMCfgPeerIpAddress_Type()
)
prvtPwVcTDMCfgPeerIpAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    prvtPwVcTDMCfgPeerIpAddress.setStatus("current")


class _PrvtPwVcTDMCfgPeerPort_Type(Integer32):
    """Custom type prvtPwVcTDMCfgPeerPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_PrvtPwVcTDMCfgPeerPort_Type.__name__ = "Integer32"
_PrvtPwVcTDMCfgPeerPort_Object = MibTableColumn
prvtPwVcTDMCfgPeerPort = _PrvtPwVcTDMCfgPeerPort_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 200, 2, 1, 3, 1, 9),
    _PrvtPwVcTDMCfgPeerPort_Type()
)
prvtPwVcTDMCfgPeerPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    prvtPwVcTDMCfgPeerPort.setStatus("current")
_PrvtPwVcTDMCfgPeerMAC_Type = OctetString
_PrvtPwVcTDMCfgPeerMAC_Object = MibTableColumn
prvtPwVcTDMCfgPeerMAC = _PrvtPwVcTDMCfgPeerMAC_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 200, 2, 1, 3, 1, 10),
    _PrvtPwVcTDMCfgPeerMAC_Type()
)
prvtPwVcTDMCfgPeerMAC.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    prvtPwVcTDMCfgPeerMAC.setStatus("current")
_PrvtPwVcTDMCfgPeerEcid_Type = Integer32
_PrvtPwVcTDMCfgPeerEcid_Object = MibTableColumn
prvtPwVcTDMCfgPeerEcid = _PrvtPwVcTDMCfgPeerEcid_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 200, 2, 1, 3, 1, 11),
    _PrvtPwVcTDMCfgPeerEcid_Type()
)
prvtPwVcTDMCfgPeerEcid.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    prvtPwVcTDMCfgPeerEcid.setStatus("current")
_PrvtPwVcTDMCfgPeerOosEcid_Type = Integer32
_PrvtPwVcTDMCfgPeerOosEcid_Object = MibTableColumn
prvtPwVcTDMCfgPeerOosEcid = _PrvtPwVcTDMCfgPeerOosEcid_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 200, 2, 1, 3, 1, 12),
    _PrvtPwVcTDMCfgPeerOosEcid_Type()
)
prvtPwVcTDMCfgPeerOosEcid.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    prvtPwVcTDMCfgPeerOosEcid.setStatus("current")


class _PrvtPwVcTDMCfgVlanId_Type(Integer32):
    """Custom type prvtPwVcTDMCfgVlanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 4094),
    )


_PrvtPwVcTDMCfgVlanId_Type.__name__ = "Integer32"
_PrvtPwVcTDMCfgVlanId_Object = MibTableColumn
prvtPwVcTDMCfgVlanId = _PrvtPwVcTDMCfgVlanId_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 200, 2, 1, 3, 1, 13),
    _PrvtPwVcTDMCfgVlanId_Type()
)
prvtPwVcTDMCfgVlanId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    prvtPwVcTDMCfgVlanId.setStatus("current")


class _PrvtPwVcTDMCfgVlanPrio_Type(Integer32):
    """Custom type prvtPwVcTDMCfgVlanPrio based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_PrvtPwVcTDMCfgVlanPrio_Type.__name__ = "Integer32"
_PrvtPwVcTDMCfgVlanPrio_Object = MibTableColumn
prvtPwVcTDMCfgVlanPrio = _PrvtPwVcTDMCfgVlanPrio_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 200, 2, 1, 3, 1, 14),
    _PrvtPwVcTDMCfgVlanPrio_Type()
)
prvtPwVcTDMCfgVlanPrio.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    prvtPwVcTDMCfgVlanPrio.setStatus("current")


class _PrvtPwVcTDMCfgLocalPort_Type(Integer32):
    """Custom type prvtPwVcTDMCfgLocalPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_PrvtPwVcTDMCfgLocalPort_Type.__name__ = "Integer32"
_PrvtPwVcTDMCfgLocalPort_Object = MibTableColumn
prvtPwVcTDMCfgLocalPort = _PrvtPwVcTDMCfgLocalPort_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 200, 2, 1, 3, 1, 15),
    _PrvtPwVcTDMCfgLocalPort_Type()
)
prvtPwVcTDMCfgLocalPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    prvtPwVcTDMCfgLocalPort.setStatus("current")
_PrvtPwVcTDMCfgEcid_Type = Integer32
_PrvtPwVcTDMCfgEcid_Object = MibTableColumn
prvtPwVcTDMCfgEcid = _PrvtPwVcTDMCfgEcid_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 200, 2, 1, 3, 1, 16),
    _PrvtPwVcTDMCfgEcid_Type()
)
prvtPwVcTDMCfgEcid.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    prvtPwVcTDMCfgEcid.setStatus("current")
_PrvtPwVcTDMCfgOosEcid_Type = Integer32
_PrvtPwVcTDMCfgOosEcid_Object = MibTableColumn
prvtPwVcTDMCfgOosEcid = _PrvtPwVcTDMCfgOosEcid_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 200, 2, 1, 3, 1, 17),
    _PrvtPwVcTDMCfgOosEcid_Type()
)
prvtPwVcTDMCfgOosEcid.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    prvtPwVcTDMCfgOosEcid.setStatus("current")


class _PrvtPwVcTDMCfgProtocol_Type(Integer32):
    """Custom type prvtPwVcTDMCfgProtocol based on Integer32"""
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
        *(("undefined", 0),
          ("satop", 1),
          ("cesopsn", 2),
          ("metro-ethernet", 3),
          ("mpls", 4))
    )


_PrvtPwVcTDMCfgProtocol_Type.__name__ = "Integer32"
_PrvtPwVcTDMCfgProtocol_Object = MibTableColumn
prvtPwVcTDMCfgProtocol = _PrvtPwVcTDMCfgProtocol_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 200, 2, 1, 3, 1, 18),
    _PrvtPwVcTDMCfgProtocol_Type()
)
prvtPwVcTDMCfgProtocol.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    prvtPwVcTDMCfgProtocol.setStatus("current")


class _PrvtPwVcTDMCfgAdminStatus_Type(Integer32):
    """Custom type prvtPwVcTDMCfgAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_PrvtPwVcTDMCfgAdminStatus_Type.__name__ = "Integer32"
_PrvtPwVcTDMCfgAdminStatus_Object = MibTableColumn
prvtPwVcTDMCfgAdminStatus = _PrvtPwVcTDMCfgAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 200, 2, 1, 3, 1, 19),
    _PrvtPwVcTDMCfgAdminStatus_Type()
)
prvtPwVcTDMCfgAdminStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    prvtPwVcTDMCfgAdminStatus.setStatus("current")
_PrvtPwVcTDMCfgRowStatus_Type = RowStatus
_PrvtPwVcTDMCfgRowStatus_Object = MibTableColumn
prvtPwVcTDMCfgRowStatus = _PrvtPwVcTDMCfgRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 200, 2, 1, 3, 1, 20),
    _PrvtPwVcTDMCfgRowStatus_Type()
)
prvtPwVcTDMCfgRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    prvtPwVcTDMCfgRowStatus.setStatus("current")


class _PrvtPwVcTDMCfgRtp_Type(Integer32):
    """Custom type prvtPwVcTDMCfgRtp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("true", 1),
          ("false", 2))
    )


_PrvtPwVcTDMCfgRtp_Type.__name__ = "Integer32"
_PrvtPwVcTDMCfgRtp_Object = MibTableColumn
prvtPwVcTDMCfgRtp = _PrvtPwVcTDMCfgRtp_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 200, 2, 1, 3, 1, 21),
    _PrvtPwVcTDMCfgRtp_Type()
)
prvtPwVcTDMCfgRtp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    prvtPwVcTDMCfgRtp.setStatus("current")


class _PrvtPwVcTDMCfgOosPort_Type(Unsigned32):
    """Custom type prvtPwVcTDMCfgOosPort based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_PrvtPwVcTDMCfgOosPort_Type.__name__ = "Unsigned32"
_PrvtPwVcTDMCfgOosPort_Object = MibTableColumn
prvtPwVcTDMCfgOosPort = _PrvtPwVcTDMCfgOosPort_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 200, 2, 1, 3, 1, 22),
    _PrvtPwVcTDMCfgOosPort_Type()
)
prvtPwVcTDMCfgOosPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    prvtPwVcTDMCfgOosPort.setStatus("current")


class _PrvtPwVcTDMCfgPayloadSuppression_Type(Integer32):
    """Custom type prvtPwVcTDMCfgPayloadSuppression based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_PrvtPwVcTDMCfgPayloadSuppression_Type.__name__ = "Integer32"
_PrvtPwVcTDMCfgPayloadSuppression_Object = MibTableColumn
prvtPwVcTDMCfgPayloadSuppression = _PrvtPwVcTDMCfgPayloadSuppression_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 200, 2, 1, 3, 1, 23),
    _PrvtPwVcTDMCfgPayloadSuppression_Type()
)
prvtPwVcTDMCfgPayloadSuppression.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    prvtPwVcTDMCfgPayloadSuppression.setStatus("current")
_PrvtPwVcTDMCfgInterface_Type = PrvtPwVcTDMCfgInterface
_PrvtPwVcTDMCfgInterface_Object = MibTableColumn
prvtPwVcTDMCfgInterface = _PrvtPwVcTDMCfgInterface_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 200, 2, 1, 3, 1, 24),
    _PrvtPwVcTDMCfgInterface_Type()
)
prvtPwVcTDMCfgInterface.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    prvtPwVcTDMCfgInterface.setStatus("current")


class _PrvtPwVcTDMCfgIpTos_Type(Integer32):
    """Custom type prvtPwVcTDMCfgIpTos based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_PrvtPwVcTDMCfgIpTos_Type.__name__ = "Integer32"
_PrvtPwVcTDMCfgIpTos_Object = MibTableColumn
prvtPwVcTDMCfgIpTos = _PrvtPwVcTDMCfgIpTos_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 200, 2, 1, 3, 1, 25),
    _PrvtPwVcTDMCfgIpTos_Type()
)
prvtPwVcTDMCfgIpTos.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    prvtPwVcTDMCfgIpTos.setStatus("current")


class _PrvtPwVcTDMCfgIpOosTos_Type(Integer32):
    """Custom type prvtPwVcTDMCfgIpOosTos based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_PrvtPwVcTDMCfgIpOosTos_Type.__name__ = "Integer32"
_PrvtPwVcTDMCfgIpOosTos_Object = MibTableColumn
prvtPwVcTDMCfgIpOosTos = _PrvtPwVcTDMCfgIpOosTos_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 200, 2, 1, 3, 1, 26),
    _PrvtPwVcTDMCfgIpOosTos_Type()
)
prvtPwVcTDMCfgIpOosTos.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    prvtPwVcTDMCfgIpOosTos.setStatus("current")


class _PrvtPwVcTDMCfgPeerOosPort_Type(Integer32):
    """Custom type prvtPwVcTDMCfgPeerOosPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_PrvtPwVcTDMCfgPeerOosPort_Type.__name__ = "Integer32"
_PrvtPwVcTDMCfgPeerOosPort_Object = MibTableColumn
prvtPwVcTDMCfgPeerOosPort = _PrvtPwVcTDMCfgPeerOosPort_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 200, 2, 1, 3, 1, 27),
    _PrvtPwVcTDMCfgPeerOosPort_Type()
)
prvtPwVcTDMCfgPeerOosPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    prvtPwVcTDMCfgPeerOosPort.setStatus("current")


class _PrvtPwVcTDMCfgMplsLocalLabel_Type(Unsigned32):
    """Custom type prvtPwVcTDMCfgMplsLocalLabel based on Unsigned32"""
    defaultValue = 15

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1048575),
    )


_PrvtPwVcTDMCfgMplsLocalLabel_Type.__name__ = "Unsigned32"
_PrvtPwVcTDMCfgMplsLocalLabel_Object = MibTableColumn
prvtPwVcTDMCfgMplsLocalLabel = _PrvtPwVcTDMCfgMplsLocalLabel_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 200, 2, 1, 3, 1, 28),
    _PrvtPwVcTDMCfgMplsLocalLabel_Type()
)
prvtPwVcTDMCfgMplsLocalLabel.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    prvtPwVcTDMCfgMplsLocalLabel.setStatus("current")


class _PrvtPwVcTDMCfgMplsPeerLabel_Type(Unsigned32):
    """Custom type prvtPwVcTDMCfgMplsPeerLabel based on Unsigned32"""
    defaultValue = 15

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1048575),
    )


_PrvtPwVcTDMCfgMplsPeerLabel_Type.__name__ = "Unsigned32"
_PrvtPwVcTDMCfgMplsPeerLabel_Object = MibTableColumn
prvtPwVcTDMCfgMplsPeerLabel = _PrvtPwVcTDMCfgMplsPeerLabel_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 200, 2, 1, 3, 1, 29),
    _PrvtPwVcTDMCfgMplsPeerLabel_Type()
)
prvtPwVcTDMCfgMplsPeerLabel.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    prvtPwVcTDMCfgMplsPeerLabel.setStatus("current")


class _PrvtPwVcTDMCfgMplsTTL_Type(Integer32):
    """Custom type prvtPwVcTDMCfgMplsTTL based on Integer32"""
    defaultValue = 255

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 255),
    )


_PrvtPwVcTDMCfgMplsTTL_Type.__name__ = "Integer32"
_PrvtPwVcTDMCfgMplsTTL_Object = MibTableColumn
prvtPwVcTDMCfgMplsTTL = _PrvtPwVcTDMCfgMplsTTL_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 200, 2, 1, 3, 1, 30),
    _PrvtPwVcTDMCfgMplsTTL_Type()
)
prvtPwVcTDMCfgMplsTTL.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    prvtPwVcTDMCfgMplsTTL.setStatus("current")


class _PrvtPwVcTDMCfgMplsExp_Type(Integer32):
    """Custom type prvtPwVcTDMCfgMplsExp based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_PrvtPwVcTDMCfgMplsExp_Type.__name__ = "Integer32"
_PrvtPwVcTDMCfgMplsExp_Object = MibTableColumn
prvtPwVcTDMCfgMplsExp = _PrvtPwVcTDMCfgMplsExp_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 200, 2, 1, 3, 1, 31),
    _PrvtPwVcTDMCfgMplsExp_Type()
)
prvtPwVcTDMCfgMplsExp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    prvtPwVcTDMCfgMplsExp.setStatus("current")


class _PrvtPwVcTDMCfgMplsOosLocalLabel_Type(Unsigned32):
    """Custom type prvtPwVcTDMCfgMplsOosLocalLabel based on Unsigned32"""
    defaultValue = 255

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1048575),
    )


_PrvtPwVcTDMCfgMplsOosLocalLabel_Type.__name__ = "Unsigned32"
_PrvtPwVcTDMCfgMplsOosLocalLabel_Object = MibTableColumn
prvtPwVcTDMCfgMplsOosLocalLabel = _PrvtPwVcTDMCfgMplsOosLocalLabel_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 200, 2, 1, 3, 1, 32),
    _PrvtPwVcTDMCfgMplsOosLocalLabel_Type()
)
prvtPwVcTDMCfgMplsOosLocalLabel.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    prvtPwVcTDMCfgMplsOosLocalLabel.setStatus("current")


class _PrvtPwVcTDMCfgMplsOosPeerLabel_Type(Unsigned32):
    """Custom type prvtPwVcTDMCfgMplsOosPeerLabel based on Unsigned32"""
    defaultValue = 255

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1048575),
    )


_PrvtPwVcTDMCfgMplsOosPeerLabel_Type.__name__ = "Unsigned32"
_PrvtPwVcTDMCfgMplsOosPeerLabel_Object = MibTableColumn
prvtPwVcTDMCfgMplsOosPeerLabel = _PrvtPwVcTDMCfgMplsOosPeerLabel_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 200, 2, 1, 3, 1, 33),
    _PrvtPwVcTDMCfgMplsOosPeerLabel_Type()
)
prvtPwVcTDMCfgMplsOosPeerLabel.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    prvtPwVcTDMCfgMplsOosPeerLabel.setStatus("current")


class _PrvtPwVcTDMCfgMplsOosTTL_Type(Integer32):
    """Custom type prvtPwVcTDMCfgMplsOosTTL based on Integer32"""
    defaultValue = 255

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 255),
    )


_PrvtPwVcTDMCfgMplsOosTTL_Type.__name__ = "Integer32"
_PrvtPwVcTDMCfgMplsOosTTL_Object = MibTableColumn
prvtPwVcTDMCfgMplsOosTTL = _PrvtPwVcTDMCfgMplsOosTTL_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 200, 2, 1, 3, 1, 34),
    _PrvtPwVcTDMCfgMplsOosTTL_Type()
)
prvtPwVcTDMCfgMplsOosTTL.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    prvtPwVcTDMCfgMplsOosTTL.setStatus("current")


class _PrvtPwVcTDMCfgMplsOosExp_Type(Integer32):
    """Custom type prvtPwVcTDMCfgMplsOosExp based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_PrvtPwVcTDMCfgMplsOosExp_Type.__name__ = "Integer32"
_PrvtPwVcTDMCfgMplsOosExp_Object = MibTableColumn
prvtPwVcTDMCfgMplsOosExp = _PrvtPwVcTDMCfgMplsOosExp_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 200, 2, 1, 3, 1, 35),
    _PrvtPwVcTDMCfgMplsOosExp_Type()
)
prvtPwVcTDMCfgMplsOosExp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    prvtPwVcTDMCfgMplsOosExp.setStatus("current")


class _PrvtPwVcTDMCfgRtpOosPayload_Type(Integer32):
    """Custom type prvtPwVcTDMCfgRtpOosPayload based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 127),
    )


_PrvtPwVcTDMCfgRtpOosPayload_Type.__name__ = "Integer32"
_PrvtPwVcTDMCfgRtpOosPayload_Object = MibTableColumn
prvtPwVcTDMCfgRtpOosPayload = _PrvtPwVcTDMCfgRtpOosPayload_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 200, 2, 1, 3, 1, 36),
    _PrvtPwVcTDMCfgRtpOosPayload_Type()
)
prvtPwVcTDMCfgRtpOosPayload.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    prvtPwVcTDMCfgRtpOosPayload.setStatus("current")


class _PrvtPwVcTDMCfgRtpPayload_Type(Integer32):
    """Custom type prvtPwVcTDMCfgRtpPayload based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 127),
    )


_PrvtPwVcTDMCfgRtpPayload_Type.__name__ = "Integer32"
_PrvtPwVcTDMCfgRtpPayload_Object = MibTableColumn
prvtPwVcTDMCfgRtpPayload = _PrvtPwVcTDMCfgRtpPayload_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 200, 2, 1, 3, 1, 37),
    _PrvtPwVcTDMCfgRtpPayload_Type()
)
prvtPwVcTDMCfgRtpPayload.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    prvtPwVcTDMCfgRtpPayload.setStatus("current")
_PrvtTDMChannelGrpTable_Object = MibTable
prvtTDMChannelGrpTable = _PrvtTDMChannelGrpTable_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 200, 2, 1, 4)
)
if mibBuilder.loadTexts:
    prvtTDMChannelGrpTable.setStatus("current")
_PrvtTDMChannelGrpEntry_Object = MibTableRow
prvtTDMChannelGrpEntry = _PrvtTDMChannelGrpEntry_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 200, 2, 1, 4, 1)
)
prvtTDMChannelGrpEntry.setIndexNames(
    (0, "PRVT-PW-TDM-MIB", "prvtTDMChannelGrpModuleID"),
    (0, "PRVT-PW-TDM-MIB", "prvtTDMChannelGrpID"),
)
if mibBuilder.loadTexts:
    prvtTDMChannelGrpEntry.setStatus("current")
_PrvtTDMChannelGrpModuleID_Type = Unsigned32
_PrvtTDMChannelGrpModuleID_Object = MibTableColumn
prvtTDMChannelGrpModuleID = _PrvtTDMChannelGrpModuleID_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 200, 2, 1, 4, 1, 1),
    _PrvtTDMChannelGrpModuleID_Type()
)
prvtTDMChannelGrpModuleID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtTDMChannelGrpModuleID.setStatus("current")
_PrvtTDMChannelGrpID_Type = Unsigned32
_PrvtTDMChannelGrpID_Object = MibTableColumn
prvtTDMChannelGrpID = _PrvtTDMChannelGrpID_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 200, 2, 1, 4, 1, 2),
    _PrvtTDMChannelGrpID_Type()
)
prvtTDMChannelGrpID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtTDMChannelGrpID.setStatus("current")


class _PrvtTDMChannelGrpCfgError_Type(Integer32):
    """Custom type prvtTDMChannelGrpCfgError based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("noError", 0),
          ("channelGroupAtached", 1))
    )


_PrvtTDMChannelGrpCfgError_Type.__name__ = "Integer32"
_PrvtTDMChannelGrpCfgError_Object = MibTableColumn
prvtTDMChannelGrpCfgError = _PrvtTDMChannelGrpCfgError_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 200, 2, 1, 4, 1, 3),
    _PrvtTDMChannelGrpCfgError_Type()
)
prvtTDMChannelGrpCfgError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtTDMChannelGrpCfgError.setStatus("current")
_PrvtTDMChannelGrpTimeSlots_Type = TimeSlotList
_PrvtTDMChannelGrpTimeSlots_Object = MibTableColumn
prvtTDMChannelGrpTimeSlots = _PrvtTDMChannelGrpTimeSlots_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 200, 2, 1, 4, 1, 4),
    _PrvtTDMChannelGrpTimeSlots_Type()
)
prvtTDMChannelGrpTimeSlots.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prvtTDMChannelGrpTimeSlots.setStatus("current")
_PrvtTDMChannelGrpOC3TimeSlots_Type = InterfaceTimeSlot
_PrvtTDMChannelGrpOC3TimeSlots_Object = MibTableColumn
prvtTDMChannelGrpOC3TimeSlots = _PrvtTDMChannelGrpOC3TimeSlots_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 200, 2, 1, 4, 1, 5),
    _PrvtTDMChannelGrpOC3TimeSlots_Type()
)
prvtTDMChannelGrpOC3TimeSlots.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prvtTDMChannelGrpOC3TimeSlots.setStatus("current")
_PrvtPwVcTDMPerfCurrentTable_Object = MibTable
prvtPwVcTDMPerfCurrentTable = _PrvtPwVcTDMPerfCurrentTable_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 200, 2, 1, 5)
)
if mibBuilder.loadTexts:
    prvtPwVcTDMPerfCurrentTable.setStatus("current")
_PrvtPwVcTDMPerfCurrentEntry_Object = MibTableRow
prvtPwVcTDMPerfCurrentEntry = _PrvtPwVcTDMPerfCurrentEntry_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 200, 2, 1, 5, 1)
)
prvtPwVcTDMPerfCurrentEntry.setIndexNames(
    (0, "PRVT-PW-TDM-MIB", "prvtPwVcTDMModuleId"),
    (0, "PRVT-PW-TDM-MIB", "prvtPwVcTDMCircuitId"),
)
if mibBuilder.loadTexts:
    prvtPwVcTDMPerfCurrentEntry.setStatus("current")
_PrvtPwVcTDMPerfCurrentPktsOoseq_Type = Counter32
_PrvtPwVcTDMPerfCurrentPktsOoseq_Object = MibTableColumn
prvtPwVcTDMPerfCurrentPktsOoseq = _PrvtPwVcTDMPerfCurrentPktsOoseq_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 200, 2, 1, 5, 1, 1),
    _PrvtPwVcTDMPerfCurrentPktsOoseq_Type()
)
prvtPwVcTDMPerfCurrentPktsOoseq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtPwVcTDMPerfCurrentPktsOoseq.setStatus("current")
_PrvtPwVcTDMPerfCurrentJtrBfrUnderruns_Type = Counter32
_PrvtPwVcTDMPerfCurrentJtrBfrUnderruns_Object = MibTableColumn
prvtPwVcTDMPerfCurrentJtrBfrUnderruns = _PrvtPwVcTDMPerfCurrentJtrBfrUnderruns_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 200, 2, 1, 5, 1, 2),
    _PrvtPwVcTDMPerfCurrentJtrBfrUnderruns_Type()
)
prvtPwVcTDMPerfCurrentJtrBfrUnderruns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtPwVcTDMPerfCurrentJtrBfrUnderruns.setStatus("current")
_PrvtPwVcTDMPerfCurrentJtrBfrOverruns_Type = Counter32
_PrvtPwVcTDMPerfCurrentJtrBfrOverruns_Object = MibTableColumn
prvtPwVcTDMPerfCurrentJtrBfrOverruns = _PrvtPwVcTDMPerfCurrentJtrBfrOverruns_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 200, 2, 1, 5, 1, 3),
    _PrvtPwVcTDMPerfCurrentJtrBfrOverruns_Type()
)
prvtPwVcTDMPerfCurrentJtrBfrOverruns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtPwVcTDMPerfCurrentJtrBfrOverruns.setStatus("current")
_PrvtPwVcTDMPerfCurrentMalformedPkt_Type = Counter32
_PrvtPwVcTDMPerfCurrentMalformedPkt_Object = MibTableColumn
prvtPwVcTDMPerfCurrentMalformedPkt = _PrvtPwVcTDMPerfCurrentMalformedPkt_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 200, 2, 1, 5, 1, 4),
    _PrvtPwVcTDMPerfCurrentMalformedPkt_Type()
)
prvtPwVcTDMPerfCurrentMalformedPkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtPwVcTDMPerfCurrentMalformedPkt.setStatus("current")
_PrvtPwVcTDMPerfCurrentNearEndFC_Type = Counter32
_PrvtPwVcTDMPerfCurrentNearEndFC_Object = MibTableColumn
prvtPwVcTDMPerfCurrentNearEndFC = _PrvtPwVcTDMPerfCurrentNearEndFC_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 200, 2, 1, 5, 1, 5),
    _PrvtPwVcTDMPerfCurrentNearEndFC_Type()
)
prvtPwVcTDMPerfCurrentNearEndFC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtPwVcTDMPerfCurrentNearEndFC.setStatus("current")
_PrvtPwVcTDMPerfCurrentFarEndFC_Type = Counter32
_PrvtPwVcTDMPerfCurrentFarEndFC_Object = MibTableColumn
prvtPwVcTDMPerfCurrentFarEndFC = _PrvtPwVcTDMPerfCurrentFarEndFC_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 200, 2, 1, 5, 1, 6),
    _PrvtPwVcTDMPerfCurrentFarEndFC_Type()
)
prvtPwVcTDMPerfCurrentFarEndFC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtPwVcTDMPerfCurrentFarEndFC.setStatus("current")
_PrvtPwVcTDMPerfIntervalTable_Object = MibTable
prvtPwVcTDMPerfIntervalTable = _PrvtPwVcTDMPerfIntervalTable_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 200, 2, 1, 6)
)
if mibBuilder.loadTexts:
    prvtPwVcTDMPerfIntervalTable.setStatus("current")
_PrvtPwVcTDMPerfIntervalEntry_Object = MibTableRow
prvtPwVcTDMPerfIntervalEntry = _PrvtPwVcTDMPerfIntervalEntry_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 200, 2, 1, 6, 1)
)
prvtPwVcTDMPerfIntervalEntry.setIndexNames(
    (0, "PRVT-PW-TDM-MIB", "prvtPwVcTDMModuleId"),
    (0, "PRVT-PW-TDM-MIB", "prvtPwVcTDMCircuitId"),
    (0, "PRVT-PW-TDM-MIB", "prvtPwVcTDMPerfIntervalNumber"),
)
if mibBuilder.loadTexts:
    prvtPwVcTDMPerfIntervalEntry.setStatus("current")
_PrvtPwVcTDMPerfIntervalNumber_Type = Unsigned32
_PrvtPwVcTDMPerfIntervalNumber_Object = MibTableColumn
prvtPwVcTDMPerfIntervalNumber = _PrvtPwVcTDMPerfIntervalNumber_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 200, 2, 1, 6, 1, 1),
    _PrvtPwVcTDMPerfIntervalNumber_Type()
)
prvtPwVcTDMPerfIntervalNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    prvtPwVcTDMPerfIntervalNumber.setStatus("current")
_PrvtPwVcTDMPerfIntervalValidData_Type = TruthValue
_PrvtPwVcTDMPerfIntervalValidData_Object = MibTableColumn
prvtPwVcTDMPerfIntervalValidData = _PrvtPwVcTDMPerfIntervalValidData_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 200, 2, 1, 6, 1, 2),
    _PrvtPwVcTDMPerfIntervalValidData_Type()
)
prvtPwVcTDMPerfIntervalValidData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtPwVcTDMPerfIntervalValidData.setStatus("current")
_PrvtPwVcTDMPerfIntervalDuration_Type = Integer32
_PrvtPwVcTDMPerfIntervalDuration_Object = MibTableColumn
prvtPwVcTDMPerfIntervalDuration = _PrvtPwVcTDMPerfIntervalDuration_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 200, 2, 1, 6, 1, 3),
    _PrvtPwVcTDMPerfIntervalDuration_Type()
)
prvtPwVcTDMPerfIntervalDuration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtPwVcTDMPerfIntervalDuration.setStatus("current")
_PrvtPwVcTDMPerfIntervalPktsOoseq_Type = Counter32
_PrvtPwVcTDMPerfIntervalPktsOoseq_Object = MibTableColumn
prvtPwVcTDMPerfIntervalPktsOoseq = _PrvtPwVcTDMPerfIntervalPktsOoseq_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 200, 2, 1, 6, 1, 4),
    _PrvtPwVcTDMPerfIntervalPktsOoseq_Type()
)
prvtPwVcTDMPerfIntervalPktsOoseq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtPwVcTDMPerfIntervalPktsOoseq.setStatus("current")
_PrvtPwVcTDMPerfIntervalJtrBfrUnderruns_Type = Counter32
_PrvtPwVcTDMPerfIntervalJtrBfrUnderruns_Object = MibTableColumn
prvtPwVcTDMPerfIntervalJtrBfrUnderruns = _PrvtPwVcTDMPerfIntervalJtrBfrUnderruns_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 200, 2, 1, 6, 1, 5),
    _PrvtPwVcTDMPerfIntervalJtrBfrUnderruns_Type()
)
prvtPwVcTDMPerfIntervalJtrBfrUnderruns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtPwVcTDMPerfIntervalJtrBfrUnderruns.setStatus("current")
_PrvtPwVcTDMPerfIntervalJtrBfrOverruns_Type = Counter32
_PrvtPwVcTDMPerfIntervalJtrBfrOverruns_Object = MibTableColumn
prvtPwVcTDMPerfIntervalJtrBfrOverruns = _PrvtPwVcTDMPerfIntervalJtrBfrOverruns_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 200, 2, 1, 6, 1, 6),
    _PrvtPwVcTDMPerfIntervalJtrBfrOverruns_Type()
)
prvtPwVcTDMPerfIntervalJtrBfrOverruns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtPwVcTDMPerfIntervalJtrBfrOverruns.setStatus("current")
_PrvtPwVcTDMPerfIntervalMalformedPkt_Type = Counter32
_PrvtPwVcTDMPerfIntervalMalformedPkt_Object = MibTableColumn
prvtPwVcTDMPerfIntervalMalformedPkt = _PrvtPwVcTDMPerfIntervalMalformedPkt_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 200, 2, 1, 6, 1, 7),
    _PrvtPwVcTDMPerfIntervalMalformedPkt_Type()
)
prvtPwVcTDMPerfIntervalMalformedPkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtPwVcTDMPerfIntervalMalformedPkt.setStatus("current")
_PrvtPwVcTDMPerfIntervalNearEndFC_Type = Counter32
_PrvtPwVcTDMPerfIntervalNearEndFC_Object = MibTableColumn
prvtPwVcTDMPerfIntervalNearEndFC = _PrvtPwVcTDMPerfIntervalNearEndFC_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 200, 2, 1, 6, 1, 8),
    _PrvtPwVcTDMPerfIntervalNearEndFC_Type()
)
prvtPwVcTDMPerfIntervalNearEndFC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtPwVcTDMPerfIntervalNearEndFC.setStatus("current")
_PrvtPwVcTDMPerfIntervalFarEndFC_Type = Counter32
_PrvtPwVcTDMPerfIntervalFarEndFC_Object = MibTableColumn
prvtPwVcTDMPerfIntervalFarEndFC = _PrvtPwVcTDMPerfIntervalFarEndFC_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 200, 2, 1, 6, 1, 9),
    _PrvtPwVcTDMPerfIntervalFarEndFC_Type()
)
prvtPwVcTDMPerfIntervalFarEndFC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtPwVcTDMPerfIntervalFarEndFC.setStatus("current")
_PrvtPwVcTDMPerfTable_Object = MibTable
prvtPwVcTDMPerfTable = _PrvtPwVcTDMPerfTable_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 200, 2, 1, 7)
)
if mibBuilder.loadTexts:
    prvtPwVcTDMPerfTable.setStatus("current")
_PrvtPwVcTDMPerfEntry_Object = MibTableRow
prvtPwVcTDMPerfEntry = _PrvtPwVcTDMPerfEntry_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 200, 2, 1, 7, 1)
)
prvtPwVcTDMPerfEntry.setIndexNames(
    (0, "PRVT-PW-TDM-MIB", "prvtPwVcTDMModuleId"),
    (0, "PRVT-PW-TDM-MIB", "prvtPwVcTDMCircuitId"),
)
if mibBuilder.loadTexts:
    prvtPwVcTDMPerfEntry.setStatus("current")
_PrvtPwVcTDMPerfPktsOoseq_Type = Counter32
_PrvtPwVcTDMPerfPktsOoseq_Object = MibTableColumn
prvtPwVcTDMPerfPktsOoseq = _PrvtPwVcTDMPerfPktsOoseq_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 200, 2, 1, 7, 1, 1),
    _PrvtPwVcTDMPerfPktsOoseq_Type()
)
prvtPwVcTDMPerfPktsOoseq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtPwVcTDMPerfPktsOoseq.setStatus("current")
_PrvtPwVcTDMPerfJtrBfrUnderruns_Type = Counter32
_PrvtPwVcTDMPerfJtrBfrUnderruns_Object = MibTableColumn
prvtPwVcTDMPerfJtrBfrUnderruns = _PrvtPwVcTDMPerfJtrBfrUnderruns_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 200, 2, 1, 7, 1, 2),
    _PrvtPwVcTDMPerfJtrBfrUnderruns_Type()
)
prvtPwVcTDMPerfJtrBfrUnderruns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtPwVcTDMPerfJtrBfrUnderruns.setStatus("current")
_PrvtPwVcTDMPerfJtrBfrOverruns_Type = Counter32
_PrvtPwVcTDMPerfJtrBfrOverruns_Object = MibTableColumn
prvtPwVcTDMPerfJtrBfrOverruns = _PrvtPwVcTDMPerfJtrBfrOverruns_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 200, 2, 1, 7, 1, 3),
    _PrvtPwVcTDMPerfJtrBfrOverruns_Type()
)
prvtPwVcTDMPerfJtrBfrOverruns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtPwVcTDMPerfJtrBfrOverruns.setStatus("current")
_PrvtPwVcTDMPerfMalformedPkt_Type = Counter32
_PrvtPwVcTDMPerfMalformedPkt_Object = MibTableColumn
prvtPwVcTDMPerfMalformedPkt = _PrvtPwVcTDMPerfMalformedPkt_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 200, 2, 1, 7, 1, 4),
    _PrvtPwVcTDMPerfMalformedPkt_Type()
)
prvtPwVcTDMPerfMalformedPkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtPwVcTDMPerfMalformedPkt.setStatus("current")
_PrvtPwVcTDMPerfDiscontinuityTime_Type = TimeStamp
_PrvtPwVcTDMPerfDiscontinuityTime_Object = MibTableColumn
prvtPwVcTDMPerfDiscontinuityTime = _PrvtPwVcTDMPerfDiscontinuityTime_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 200, 2, 1, 7, 1, 5),
    _PrvtPwVcTDMPerfDiscontinuityTime_Type()
)
prvtPwVcTDMPerfDiscontinuityTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtPwVcTDMPerfDiscontinuityTime.setStatus("current")
_PrvtPwVcTDMPerfNearEndFC_Type = Counter32
_PrvtPwVcTDMPerfNearEndFC_Object = MibTableColumn
prvtPwVcTDMPerfNearEndFC = _PrvtPwVcTDMPerfNearEndFC_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 200, 2, 1, 7, 1, 6),
    _PrvtPwVcTDMPerfNearEndFC_Type()
)
prvtPwVcTDMPerfNearEndFC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtPwVcTDMPerfNearEndFC.setStatus("current")
_PrvtPwVcTDMPerfFarEndFC_Type = Counter32
_PrvtPwVcTDMPerfFarEndFC_Object = MibTableColumn
prvtPwVcTDMPerfFarEndFC = _PrvtPwVcTDMPerfFarEndFC_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 200, 2, 1, 7, 1, 7),
    _PrvtPwVcTDMPerfFarEndFC_Type()
)
prvtPwVcTDMPerfFarEndFC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtPwVcTDMPerfFarEndFC.setStatus("current")
_PrvtPwVcTDMAlarmTable_Object = MibTable
prvtPwVcTDMAlarmTable = _PrvtPwVcTDMAlarmTable_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 200, 2, 1, 8)
)
if mibBuilder.loadTexts:
    prvtPwVcTDMAlarmTable.setStatus("current")
_PrvtPwVcTDMAlarmEntry_Object = MibTableRow
prvtPwVcTDMAlarmEntry = _PrvtPwVcTDMAlarmEntry_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 200, 2, 1, 8, 1)
)
prvtPwVcTDMAlarmEntry.setIndexNames(
    (0, "PRVT-PW-TDM-MIB", "prvtPwVcTDMModuleId"),
    (0, "PRVT-PW-TDM-MIB", "prvtPwVcTDMCircuitId"),
    (0, "PRVT-PW-TDM-MIB", "prvtPwVcTDMAlarmIndex"),
)
if mibBuilder.loadTexts:
    prvtPwVcTDMAlarmEntry.setStatus("current")
_PrvtPwVcTDMAlarmIndex_Type = Gauge32
_PrvtPwVcTDMAlarmIndex_Object = MibTableColumn
prvtPwVcTDMAlarmIndex = _PrvtPwVcTDMAlarmIndex_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 200, 2, 1, 8, 1, 1),
    _PrvtPwVcTDMAlarmIndex_Type()
)
prvtPwVcTDMAlarmIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    prvtPwVcTDMAlarmIndex.setStatus("current")
_PrvtPwVcTDMAlarmVariable_Type = ObjectIdentifier
_PrvtPwVcTDMAlarmVariable_Object = MibTableColumn
prvtPwVcTDMAlarmVariable = _PrvtPwVcTDMAlarmVariable_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 200, 2, 1, 8, 1, 2),
    _PrvtPwVcTDMAlarmVariable_Type()
)
prvtPwVcTDMAlarmVariable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtPwVcTDMAlarmVariable.setStatus("current")
_PrvtPwVcTDMAlarmThreshold_Type = Integer32
_PrvtPwVcTDMAlarmThreshold_Object = MibTableColumn
prvtPwVcTDMAlarmThreshold = _PrvtPwVcTDMAlarmThreshold_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 200, 2, 1, 8, 1, 3),
    _PrvtPwVcTDMAlarmThreshold_Type()
)
prvtPwVcTDMAlarmThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prvtPwVcTDMAlarmThreshold.setStatus("current")
_PrvtPwVcTDMAlarmValue_Type = Integer32
_PrvtPwVcTDMAlarmValue_Object = MibTableColumn
prvtPwVcTDMAlarmValue = _PrvtPwVcTDMAlarmValue_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 200, 2, 1, 8, 1, 4),
    _PrvtPwVcTDMAlarmValue_Type()
)
prvtPwVcTDMAlarmValue.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    prvtPwVcTDMAlarmValue.setStatus("current")
_PrvtPwVcTDMTraps_ObjectIdentity = ObjectIdentity
prvtPwVcTDMTraps = _PrvtPwVcTDMTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 200, 2, 2)
)
_PrvtPwVcTDMConformance_ObjectIdentity = ObjectIdentity
prvtPwVcTDMConformance = _PrvtPwVcTDMConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 200, 2, 3)
)
_PrvtPwVcTDMGroups_ObjectIdentity = ObjectIdentity
prvtPwVcTDMGroups = _PrvtPwVcTDMGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 200, 2, 3, 1)
)
_PrvtPwVcTDMCompliances_ObjectIdentity = ObjectIdentity
prvtPwVcTDMCompliances = _PrvtPwVcTDMCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 200, 2, 3, 2)
)

# Managed Objects groups

prvtPwVcTDMGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 200, 2, 3, 1, 1)
)
prvtPwVcTDMGroup.setObjects(
      *(("PRVT-PW-TDM-MIB", "prvtPwVcTDMType"),
        ("PRVT-PW-TDM-MIB", "prvtPwVcRelTDMCfgIndex"),
        ("PRVT-PW-TDM-MIB", "prvtPwVcTDMTimeElapsed"),
        ("PRVT-PW-TDM-MIB", "prvtPwVcTDMValidIntervals"),
        ("PRVT-PW-TDM-MIB", "prvtPwVcTDMCurrentIndications"),
        ("PRVT-PW-TDM-MIB", "prvtPwVcTDMLatchedIndications"),
        ("PRVT-PW-TDM-MIB", "prvtPwVcTDMLastEsTimeStamp"),
        ("PRVT-PW-TDM-MIB", "prvtPwVcTDMCfgPayloadSize"),
        ("PRVT-PW-TDM-MIB", "prvtPwVcTDMCfgPktReorder"),
        ("PRVT-PW-TDM-MIB", "prvtPwVcTDMCfgRtpHdrUsed"),
        ("PRVT-PW-TDM-MIB", "prvtPwVcTDMCfgJtrBfrDepth"))
)
if mibBuilder.loadTexts:
    prvtPwVcTDMGroup.setStatus("current")

prvtPwVcTDMPerfCurrentGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 200, 2, 3, 1, 2)
)
prvtPwVcTDMPerfCurrentGroup.setObjects(
      *(("PRVT-PW-TDM-MIB", "prvtPwVcTDMPerfCurrentPktsOoseq"),
        ("PRVT-PW-TDM-MIB", "prvtPwVcTDMPerfCurrentJtrBfrUnderruns"),
        ("PRVT-PW-TDM-MIB", "prvtPwVcTDMPerfCurrentJtrBfrOverruns"),
        ("PRVT-PW-TDM-MIB", "prvtPwVcTDMPerfCurrentMalformedPkt"),
        ("PRVT-PW-TDM-MIB", "prvtPwVcTDMPerfNearEndFC"),
        ("PRVT-PW-TDM-MIB", "prvtPwVcTDMPerfFarEndFC"))
)
if mibBuilder.loadTexts:
    prvtPwVcTDMPerfCurrentGroup.setStatus("current")

prvtPwVcTDMPerfIntervalGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 200, 2, 3, 1, 3)
)
prvtPwVcTDMPerfIntervalGroup.setObjects(
      *(("PRVT-PW-TDM-MIB", "prvtPwVcTDMPerfIntervalPktsOoseq"),
        ("PRVT-PW-TDM-MIB", "prvtPwVcTDMPerfIntervalJtrBfrUnderruns"),
        ("PRVT-PW-TDM-MIB", "prvtPwVcTDMPerfIntervalJtrBfrOverruns"),
        ("PRVT-PW-TDM-MIB", "prvtPwVcTDMPerfIntervalMalformedPkt"),
        ("PRVT-PW-TDM-MIB", "prvtPwVcTDMPerfNearEndFC"),
        ("PRVT-PW-TDM-MIB", "prvtPwVcTDMPerfFarEndFC"),
        ("PRVT-PW-TDM-MIB", "prvtPwVcTDMPerfIntervalValidData"),
        ("PRVT-PW-TDM-MIB", "prvtPwVcTDMPerfIntervalDuration"))
)
if mibBuilder.loadTexts:
    prvtPwVcTDMPerfIntervalGroup.setStatus("current")

prvtPwVcTDMPerfGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 200, 2, 3, 1, 4)
)
prvtPwVcTDMPerfGroup.setObjects(
      *(("PRVT-PW-TDM-MIB", "prvtPwVcTDMPerfPktsOoseq"),
        ("PRVT-PW-TDM-MIB", "prvtPwVcTDMPerfJtrBfrUnderruns"),
        ("PRVT-PW-TDM-MIB", "prvtPwVcTDMPerfJtrBfrOverruns"),
        ("PRVT-PW-TDM-MIB", "prvtPwVcTDMPerfMalformedPkt"),
        ("PRVT-PW-TDM-MIB", "prvtPwVcTDMPerfNearEndFC"),
        ("PRVT-PW-TDM-MIB", "prvtPwVcTDMPerfFarEndFC"),
        ("PRVT-PW-TDM-MIB", "prvtPwVcTDMPerfDiscontinuityTime"))
)
if mibBuilder.loadTexts:
    prvtPwVcTDMPerfGroup.setStatus("current")


# Notification objects

prvtPwVcTDMAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 200, 2, 2, 1)
)
prvtPwVcTDMAlarm.setObjects(
      *(("PRVT-PW-TDM-MIB", "prvtPwVcTDMAlarmVariable"),
        ("PRVT-PW-TDM-MIB", "prvtPwVcTDMAlarmThreshold"),
        ("PRVT-PW-TDM-MIB", "prvtPwVcTDMAlarmValue"))
)
if mibBuilder.loadTexts:
    prvtPwVcTDMAlarm.setStatus(
        "current"
    )

prvtPwVcTDMStatusChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 200, 2, 2, 2)
)
prvtPwVcTDMStatusChange.setObjects(
      *(("PRVT-PW-TDM-MIB", "prvtPwVcTDMOperStatus"),
        ("PRVT-PW-TDM-MIB", "prvtPwVcTDMCfgAdminStatus"))
)
if mibBuilder.loadTexts:
    prvtPwVcTDMStatusChange.setStatus(
        "current"
    )


# Notifications groups

prvtPwVcTDMNotificationsGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 200, 2, 3, 1, 5)
)
prvtPwVcTDMNotificationsGroup.setObjects(
      *(("PRVT-PW-TDM-MIB", "prvtPwVcTDMAlarm"),
        ("PRVT-PW-TDM-MIB", "prvtPwVcTDMStatusChange"))
)
if mibBuilder.loadTexts:
    prvtPwVcTDMNotificationsGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

prvtPwTDMModuleCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 200, 2, 3, 2, 1)
)
prvtPwTDMModuleCompliance.setObjects(
      *(("PRVT-PW-TDM-MIB", "prvtPwVcTDMGroup"),
        ("PRVT-PW-TDM-MIB", "prvtPwVcTDMPerfCurrentGroup"),
        ("PRVT-PW-TDM-MIB", "prvtPwVcTDMPerfIntervalGroup"),
        ("PRVT-PW-TDM-MIB", "prvtPwVcTDMPerfGroup"),
        ("PRVT-PW-TDM-MIB", "prvtPwVcTDMNotificationsGroup"))
)
if mibBuilder.loadTexts:
    prvtPwTDMModuleCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "PRVT-PW-TDM-MIB",
    **{"PrvtPwVcTDMCfgIndex": PrvtPwVcTDMCfgIndex,
       "TimeSlotList": TimeSlotList,
       "PrvtPwVcTDMCfgInterface": PrvtPwVcTDMCfgInterface,
       "InterfaceTimeSlot": InterfaceTimeSlot,
       "prvtPwVc": prvtPwVc,
       "prvtPwVcTDMMIB": prvtPwVcTDMMIB,
       "prvtPwVcTDMObjects": prvtPwVcTDMObjects,
       "prvtPwVcTDMTable": prvtPwVcTDMTable,
       "prvtPwVcTDMEntry": prvtPwVcTDMEntry,
       "prvtPwVcTDMModuleId": prvtPwVcTDMModuleId,
       "prvtPwVcTDMCircuitId": prvtPwVcTDMCircuitId,
       "prvtPwVcTDMType": prvtPwVcTDMType,
       "prvtPwVcRelTDMCfgIndex": prvtPwVcRelTDMCfgIndex,
       "prvtPwVcTDMTimeElapsed": prvtPwVcTDMTimeElapsed,
       "prvtPwVcTDMValidIntervals": prvtPwVcTDMValidIntervals,
       "prvtPwVcTDMCurrentIndications": prvtPwVcTDMCurrentIndications,
       "prvtPwVcTDMLatchedIndications": prvtPwVcTDMLatchedIndications,
       "prvtPwVcTDMLastEsTimeStamp": prvtPwVcTDMLastEsTimeStamp,
       "prvtPwVcTDMEmulationMode": prvtPwVcTDMEmulationMode,
       "prvtPwVcTDMOperStatus": prvtPwVcTDMOperStatus,
       "prvtPwVcTDMClearCircuitStatistics": prvtPwVcTDMClearCircuitStatistics,
       "prvtPwVcTDMCfgTable": prvtPwVcTDMCfgTable,
       "prvtPwVcTDMCfgEntry": prvtPwVcTDMCfgEntry,
       "prvtPwVcTDMCfgPayloadSize": prvtPwVcTDMCfgPayloadSize,
       "prvtPwVcTDMCfgPktReorder": prvtPwVcTDMCfgPktReorder,
       "prvtPwVcTDMCfgRtpHdrUsed": prvtPwVcTDMCfgRtpHdrUsed,
       "prvtPwVcTDMCfgJtrBfrDepth": prvtPwVcTDMCfgJtrBfrDepth,
       "prvtPwVcTDMCfgChannelGroup": prvtPwVcTDMCfgChannelGroup,
       "prvtPwVcTDMCfgPorts": prvtPwVcTDMCfgPorts,
       "prvtPwVcTDMCfgPeerIpType": prvtPwVcTDMCfgPeerIpType,
       "prvtPwVcTDMCfgPeerIpAddress": prvtPwVcTDMCfgPeerIpAddress,
       "prvtPwVcTDMCfgPeerPort": prvtPwVcTDMCfgPeerPort,
       "prvtPwVcTDMCfgPeerMAC": prvtPwVcTDMCfgPeerMAC,
       "prvtPwVcTDMCfgPeerEcid": prvtPwVcTDMCfgPeerEcid,
       "prvtPwVcTDMCfgPeerOosEcid": prvtPwVcTDMCfgPeerOosEcid,
       "prvtPwVcTDMCfgVlanId": prvtPwVcTDMCfgVlanId,
       "prvtPwVcTDMCfgVlanPrio": prvtPwVcTDMCfgVlanPrio,
       "prvtPwVcTDMCfgLocalPort": prvtPwVcTDMCfgLocalPort,
       "prvtPwVcTDMCfgEcid": prvtPwVcTDMCfgEcid,
       "prvtPwVcTDMCfgOosEcid": prvtPwVcTDMCfgOosEcid,
       "prvtPwVcTDMCfgProtocol": prvtPwVcTDMCfgProtocol,
       "prvtPwVcTDMCfgAdminStatus": prvtPwVcTDMCfgAdminStatus,
       "prvtPwVcTDMCfgRowStatus": prvtPwVcTDMCfgRowStatus,
       "prvtPwVcTDMCfgRtp": prvtPwVcTDMCfgRtp,
       "prvtPwVcTDMCfgOosPort": prvtPwVcTDMCfgOosPort,
       "prvtPwVcTDMCfgPayloadSuppression": prvtPwVcTDMCfgPayloadSuppression,
       "prvtPwVcTDMCfgInterface": prvtPwVcTDMCfgInterface,
       "prvtPwVcTDMCfgIpTos": prvtPwVcTDMCfgIpTos,
       "prvtPwVcTDMCfgIpOosTos": prvtPwVcTDMCfgIpOosTos,
       "prvtPwVcTDMCfgPeerOosPort": prvtPwVcTDMCfgPeerOosPort,
       "prvtPwVcTDMCfgMplsLocalLabel": prvtPwVcTDMCfgMplsLocalLabel,
       "prvtPwVcTDMCfgMplsPeerLabel": prvtPwVcTDMCfgMplsPeerLabel,
       "prvtPwVcTDMCfgMplsTTL": prvtPwVcTDMCfgMplsTTL,
       "prvtPwVcTDMCfgMplsExp": prvtPwVcTDMCfgMplsExp,
       "prvtPwVcTDMCfgMplsOosLocalLabel": prvtPwVcTDMCfgMplsOosLocalLabel,
       "prvtPwVcTDMCfgMplsOosPeerLabel": prvtPwVcTDMCfgMplsOosPeerLabel,
       "prvtPwVcTDMCfgMplsOosTTL": prvtPwVcTDMCfgMplsOosTTL,
       "prvtPwVcTDMCfgMplsOosExp": prvtPwVcTDMCfgMplsOosExp,
       "prvtPwVcTDMCfgRtpOosPayload": prvtPwVcTDMCfgRtpOosPayload,
       "prvtPwVcTDMCfgRtpPayload": prvtPwVcTDMCfgRtpPayload,
       "prvtTDMChannelGrpTable": prvtTDMChannelGrpTable,
       "prvtTDMChannelGrpEntry": prvtTDMChannelGrpEntry,
       "prvtTDMChannelGrpModuleID": prvtTDMChannelGrpModuleID,
       "prvtTDMChannelGrpID": prvtTDMChannelGrpID,
       "prvtTDMChannelGrpCfgError": prvtTDMChannelGrpCfgError,
       "prvtTDMChannelGrpTimeSlots": prvtTDMChannelGrpTimeSlots,
       "prvtTDMChannelGrpOC3TimeSlots": prvtTDMChannelGrpOC3TimeSlots,
       "prvtPwVcTDMPerfCurrentTable": prvtPwVcTDMPerfCurrentTable,
       "prvtPwVcTDMPerfCurrentEntry": prvtPwVcTDMPerfCurrentEntry,
       "prvtPwVcTDMPerfCurrentPktsOoseq": prvtPwVcTDMPerfCurrentPktsOoseq,
       "prvtPwVcTDMPerfCurrentJtrBfrUnderruns": prvtPwVcTDMPerfCurrentJtrBfrUnderruns,
       "prvtPwVcTDMPerfCurrentJtrBfrOverruns": prvtPwVcTDMPerfCurrentJtrBfrOverruns,
       "prvtPwVcTDMPerfCurrentMalformedPkt": prvtPwVcTDMPerfCurrentMalformedPkt,
       "prvtPwVcTDMPerfCurrentNearEndFC": prvtPwVcTDMPerfCurrentNearEndFC,
       "prvtPwVcTDMPerfCurrentFarEndFC": prvtPwVcTDMPerfCurrentFarEndFC,
       "prvtPwVcTDMPerfIntervalTable": prvtPwVcTDMPerfIntervalTable,
       "prvtPwVcTDMPerfIntervalEntry": prvtPwVcTDMPerfIntervalEntry,
       "prvtPwVcTDMPerfIntervalNumber": prvtPwVcTDMPerfIntervalNumber,
       "prvtPwVcTDMPerfIntervalValidData": prvtPwVcTDMPerfIntervalValidData,
       "prvtPwVcTDMPerfIntervalDuration": prvtPwVcTDMPerfIntervalDuration,
       "prvtPwVcTDMPerfIntervalPktsOoseq": prvtPwVcTDMPerfIntervalPktsOoseq,
       "prvtPwVcTDMPerfIntervalJtrBfrUnderruns": prvtPwVcTDMPerfIntervalJtrBfrUnderruns,
       "prvtPwVcTDMPerfIntervalJtrBfrOverruns": prvtPwVcTDMPerfIntervalJtrBfrOverruns,
       "prvtPwVcTDMPerfIntervalMalformedPkt": prvtPwVcTDMPerfIntervalMalformedPkt,
       "prvtPwVcTDMPerfIntervalNearEndFC": prvtPwVcTDMPerfIntervalNearEndFC,
       "prvtPwVcTDMPerfIntervalFarEndFC": prvtPwVcTDMPerfIntervalFarEndFC,
       "prvtPwVcTDMPerfTable": prvtPwVcTDMPerfTable,
       "prvtPwVcTDMPerfEntry": prvtPwVcTDMPerfEntry,
       "prvtPwVcTDMPerfPktsOoseq": prvtPwVcTDMPerfPktsOoseq,
       "prvtPwVcTDMPerfJtrBfrUnderruns": prvtPwVcTDMPerfJtrBfrUnderruns,
       "prvtPwVcTDMPerfJtrBfrOverruns": prvtPwVcTDMPerfJtrBfrOverruns,
       "prvtPwVcTDMPerfMalformedPkt": prvtPwVcTDMPerfMalformedPkt,
       "prvtPwVcTDMPerfDiscontinuityTime": prvtPwVcTDMPerfDiscontinuityTime,
       "prvtPwVcTDMPerfNearEndFC": prvtPwVcTDMPerfNearEndFC,
       "prvtPwVcTDMPerfFarEndFC": prvtPwVcTDMPerfFarEndFC,
       "prvtPwVcTDMAlarmTable": prvtPwVcTDMAlarmTable,
       "prvtPwVcTDMAlarmEntry": prvtPwVcTDMAlarmEntry,
       "prvtPwVcTDMAlarmIndex": prvtPwVcTDMAlarmIndex,
       "prvtPwVcTDMAlarmVariable": prvtPwVcTDMAlarmVariable,
       "prvtPwVcTDMAlarmThreshold": prvtPwVcTDMAlarmThreshold,
       "prvtPwVcTDMAlarmValue": prvtPwVcTDMAlarmValue,
       "prvtPwVcTDMTraps": prvtPwVcTDMTraps,
       "prvtPwVcTDMAlarm": prvtPwVcTDMAlarm,
       "prvtPwVcTDMStatusChange": prvtPwVcTDMStatusChange,
       "prvtPwVcTDMConformance": prvtPwVcTDMConformance,
       "prvtPwVcTDMGroups": prvtPwVcTDMGroups,
       "prvtPwVcTDMGroup": prvtPwVcTDMGroup,
       "prvtPwVcTDMPerfCurrentGroup": prvtPwVcTDMPerfCurrentGroup,
       "prvtPwVcTDMPerfIntervalGroup": prvtPwVcTDMPerfIntervalGroup,
       "prvtPwVcTDMPerfGroup": prvtPwVcTDMPerfGroup,
       "prvtPwVcTDMNotificationsGroup": prvtPwVcTDMNotificationsGroup,
       "prvtPwVcTDMCompliances": prvtPwVcTDMCompliances,
       "prvtPwTDMModuleCompliance": prvtPwTDMModuleCompliance}
)
