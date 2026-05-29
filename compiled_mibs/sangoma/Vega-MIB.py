# SNMP MIB module (Vega-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\sangoma\Vega-MIB

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

(ModuleCompliance,
 NotificationGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup")

(sysDescr,) = mibBuilder.importSymbols(
    "SNMPv2-MIB",
    "sysDescr")

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
 NotificationType,
 TimeTicks,
 Unsigned32,
 enterprises,
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
    "NotificationType",
    "TimeTicks",
    "Unsigned32",
    "enterprises",
    "iso")

(DisplayString,
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



class InterfaceIndex(TextualConvention, Integer32):
    status = "current"
    displayHint = "d"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )



class SipUsrIndex(TextualConvention, Integer32):
    status = "current"
    displayHint = "d"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )



# MIB Managed Objects in the order of their OIDs

_Vega_ObjectIdentity = ObjectIdentity
vega = _Vega_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4686)
)
_Vsplatform_ObjectIdentity = ObjectIdentity
vsplatform = _Vsplatform_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4686, 11)
)
_CallStats_ObjectIdentity = ObjectIdentity
callStats = _CallStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4686, 11, 1)
)
_NoCircuits_Type = Integer32
_NoCircuits_Object = MibScalar
noCircuits = _NoCircuits_Object(
    (1, 3, 6, 1, 4, 1, 4686, 11, 1, 1),
    _NoCircuits_Type()
)
noCircuits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    noCircuits.setStatus("mandatory")
_UpTime_Type = Integer32
_UpTime_Object = MibScalar
upTime = _UpTime_Object(
    (1, 3, 6, 1, 4, 1, 4686, 11, 1, 2),
    _UpTime_Type()
)
upTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upTime.setStatus("mandatory")
_DownTime_Type = Integer32
_DownTime_Object = MibScalar
downTime = _DownTime_Object(
    (1, 3, 6, 1, 4, 1, 4686, 11, 1, 3),
    _DownTime_Type()
)
downTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    downTime.setStatus("mandatory")
_StartTime_Type = Integer32
_StartTime_Object = MibScalar
startTime = _StartTime_Object(
    (1, 3, 6, 1, 4, 1, 4686, 11, 1, 4),
    _StartTime_Type()
)
startTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    startTime.setStatus("mandatory")
_EndTime_Type = Integer32
_EndTime_Object = MibScalar
endTime = _EndTime_Object(
    (1, 3, 6, 1, 4, 1, 4686, 11, 1, 5),
    _EndTime_Type()
)
endTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    endTime.setStatus("mandatory")
_InboundCalls_Type = Counter32
_InboundCalls_Object = MibScalar
inboundCalls = _InboundCalls_Object(
    (1, 3, 6, 1, 4, 1, 4686, 11, 1, 6),
    _InboundCalls_Type()
)
inboundCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inboundCalls.setStatus("mandatory")
_InboundAnswered_Type = Counter32
_InboundAnswered_Object = MibScalar
inboundAnswered = _InboundAnswered_Object(
    (1, 3, 6, 1, 4, 1, 4686, 11, 1, 7),
    _InboundAnswered_Type()
)
inboundAnswered.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inboundAnswered.setStatus("mandatory")
_InboundBusy_Type = Counter32
_InboundBusy_Object = MibScalar
inboundBusy = _InboundBusy_Object(
    (1, 3, 6, 1, 4, 1, 4686, 11, 1, 8),
    _InboundBusy_Type()
)
inboundBusy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inboundBusy.setStatus("mandatory")
_InboundNoAnswer_Type = Counter32
_InboundNoAnswer_Object = MibScalar
inboundNoAnswer = _InboundNoAnswer_Object(
    (1, 3, 6, 1, 4, 1, 4686, 11, 1, 9),
    _InboundNoAnswer_Type()
)
inboundNoAnswer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inboundNoAnswer.setStatus("mandatory")
_InboundTermReject_Type = Counter32
_InboundTermReject_Object = MibScalar
inboundTermReject = _InboundTermReject_Object(
    (1, 3, 6, 1, 4, 1, 4686, 11, 1, 10),
    _InboundTermReject_Type()
)
inboundTermReject.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inboundTermReject.setStatus("mandatory")
_OutboundCalls_Type = Counter32
_OutboundCalls_Object = MibScalar
outboundCalls = _OutboundCalls_Object(
    (1, 3, 6, 1, 4, 1, 4686, 11, 1, 11),
    _OutboundCalls_Type()
)
outboundCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outboundCalls.setStatus("mandatory")
_OutboundAnswered_Type = Counter32
_OutboundAnswered_Object = MibScalar
outboundAnswered = _OutboundAnswered_Object(
    (1, 3, 6, 1, 4, 1, 4686, 11, 1, 12),
    _OutboundAnswered_Type()
)
outboundAnswered.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outboundAnswered.setStatus("mandatory")
_OutboundBusy_Type = Counter32
_OutboundBusy_Object = MibScalar
outboundBusy = _OutboundBusy_Object(
    (1, 3, 6, 1, 4, 1, 4686, 11, 1, 13),
    _OutboundBusy_Type()
)
outboundBusy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outboundBusy.setStatus("mandatory")
_OutboundNoAnswer_Type = Counter32
_OutboundNoAnswer_Object = MibScalar
outboundNoAnswer = _OutboundNoAnswer_Object(
    (1, 3, 6, 1, 4, 1, 4686, 11, 1, 14),
    _OutboundNoAnswer_Type()
)
outboundNoAnswer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outboundNoAnswer.setStatus("mandatory")
_OutboundTermReject_Type = Counter32
_OutboundTermReject_Object = MibScalar
outboundTermReject = _OutboundTermReject_Object(
    (1, 3, 6, 1, 4, 1, 4686, 11, 1, 15),
    _OutboundTermReject_Type()
)
outboundTermReject.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outboundTermReject.setStatus("mandatory")
_InboundCurrUse_Type = Counter32
_InboundCurrUse_Object = MibScalar
inboundCurrUse = _InboundCurrUse_Object(
    (1, 3, 6, 1, 4, 1, 4686, 11, 1, 16),
    _InboundCurrUse_Type()
)
inboundCurrUse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inboundCurrUse.setStatus("mandatory")
_OutboundCurrUse_Type = Counter32
_OutboundCurrUse_Object = MibScalar
outboundCurrUse = _OutboundCurrUse_Object(
    (1, 3, 6, 1, 4, 1, 4686, 11, 1, 17),
    _OutboundCurrUse_Type()
)
outboundCurrUse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outboundCurrUse.setStatus("mandatory")
_InboundMaxUse_Type = Counter32
_InboundMaxUse_Object = MibScalar
inboundMaxUse = _InboundMaxUse_Object(
    (1, 3, 6, 1, 4, 1, 4686, 11, 1, 18),
    _InboundMaxUse_Type()
)
inboundMaxUse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inboundMaxUse.setStatus("mandatory")
_OutboundMaxUse_Type = Counter32
_OutboundMaxUse_Object = MibScalar
outboundMaxUse = _OutboundMaxUse_Object(
    (1, 3, 6, 1, 4, 1, 4686, 11, 1, 19),
    _OutboundMaxUse_Type()
)
outboundMaxUse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outboundMaxUse.setStatus("mandatory")
_AllMaxUse_Type = Counter32
_AllMaxUse_Object = MibScalar
allMaxUse = _AllMaxUse_Object(
    (1, 3, 6, 1, 4, 1, 4686, 11, 1, 20),
    _AllMaxUse_Type()
)
allMaxUse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    allMaxUse.setStatus("mandatory")
_InboundAvAnswer_Type = Integer32
_InboundAvAnswer_Object = MibScalar
inboundAvAnswer = _InboundAvAnswer_Object(
    (1, 3, 6, 1, 4, 1, 4686, 11, 1, 21),
    _InboundAvAnswer_Type()
)
inboundAvAnswer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inboundAvAnswer.setStatus("mandatory")
_OutboundAvAnswer_Type = Integer32
_OutboundAvAnswer_Object = MibScalar
outboundAvAnswer = _OutboundAvAnswer_Object(
    (1, 3, 6, 1, 4, 1, 4686, 11, 1, 22),
    _OutboundAvAnswer_Type()
)
outboundAvAnswer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outboundAvAnswer.setStatus("mandatory")
_InboundAvCall_Type = Integer32
_InboundAvCall_Object = MibScalar
inboundAvCall = _InboundAvCall_Object(
    (1, 3, 6, 1, 4, 1, 4686, 11, 1, 23),
    _InboundAvCall_Type()
)
inboundAvCall.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inboundAvCall.setStatus("mandatory")
_InboundMaxCall_Type = Integer32
_InboundMaxCall_Object = MibScalar
inboundMaxCall = _InboundMaxCall_Object(
    (1, 3, 6, 1, 4, 1, 4686, 11, 1, 24),
    _InboundMaxCall_Type()
)
inboundMaxCall.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inboundMaxCall.setStatus("mandatory")
_OutboundAvCall_Type = Integer32
_OutboundAvCall_Object = MibScalar
outboundAvCall = _OutboundAvCall_Object(
    (1, 3, 6, 1, 4, 1, 4686, 11, 1, 25),
    _OutboundAvCall_Type()
)
outboundAvCall.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outboundAvCall.setStatus("mandatory")
_OutboundMaxCall_Type = Integer32
_OutboundMaxCall_Object = MibScalar
outboundMaxCall = _OutboundMaxCall_Object(
    (1, 3, 6, 1, 4, 1, 4686, 11, 1, 26),
    _OutboundMaxCall_Type()
)
outboundMaxCall.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outboundMaxCall.setStatus("mandatory")
_InboundAvDialSucc_Type = Integer32
_InboundAvDialSucc_Object = MibScalar
inboundAvDialSucc = _InboundAvDialSucc_Object(
    (1, 3, 6, 1, 4, 1, 4686, 11, 1, 27),
    _InboundAvDialSucc_Type()
)
inboundAvDialSucc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inboundAvDialSucc.setStatus("mandatory")
_OutboundAvDialSucc_Type = Integer32
_OutboundAvDialSucc_Object = MibScalar
outboundAvDialSucc = _OutboundAvDialSucc_Object(
    (1, 3, 6, 1, 4, 1, 4686, 11, 1, 28),
    _OutboundAvDialSucc_Type()
)
outboundAvDialSucc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outboundAvDialSucc.setStatus("mandatory")
_InboundAvDialFail_Type = Integer32
_InboundAvDialFail_Object = MibScalar
inboundAvDialFail = _InboundAvDialFail_Object(
    (1, 3, 6, 1, 4, 1, 4686, 11, 1, 29),
    _InboundAvDialFail_Type()
)
inboundAvDialFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inboundAvDialFail.setStatus("mandatory")
_OutboundAvDialFail_Type = Integer32
_OutboundAvDialFail_Object = MibScalar
outboundAvDialFail = _OutboundAvDialFail_Object(
    (1, 3, 6, 1, 4, 1, 4686, 11, 1, 30),
    _OutboundAvDialFail_Type()
)
outboundAvDialFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outboundAvDialFail.setStatus("mandatory")
_AverageJitter_Type = Integer32
_AverageJitter_Object = MibScalar
averageJitter = _AverageJitter_Object(
    (1, 3, 6, 1, 4, 1, 4686, 11, 1, 31),
    _AverageJitter_Type()
)
averageJitter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    averageJitter.setStatus("mandatory")
_MaximumJitter_Type = Integer32
_MaximumJitter_Object = MibScalar
maximumJitter = _MaximumJitter_Object(
    (1, 3, 6, 1, 4, 1, 4686, 11, 1, 32),
    _MaximumJitter_Type()
)
maximumJitter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    maximumJitter.setStatus("mandatory")
_AverageLoss_Type = Integer32
_AverageLoss_Object = MibScalar
averageLoss = _AverageLoss_Object(
    (1, 3, 6, 1, 4, 1, 4686, 11, 1, 33),
    _AverageLoss_Type()
)
averageLoss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    averageLoss.setStatus("mandatory")
_MaximumLoss_Type = Integer32
_MaximumLoss_Object = MibScalar
maximumLoss = _MaximumLoss_Object(
    (1, 3, 6, 1, 4, 1, 4686, 11, 1, 34),
    _MaximumLoss_Type()
)
maximumLoss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    maximumLoss.setStatus("mandatory")
_IfFanState_Type = OctetString
_IfFanState_Object = MibTableColumn
ifFanState = _IfFanState_Object(
    (1, 3, 6, 1, 4, 1, 4686, 11, 1, 35),
    _IfFanState_Type()
)
ifFanState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifFanState.setStatus("mandatory")
_IfPowerStatus_Type = OctetString
_IfPowerStatus_Object = MibTableColumn
ifPowerStatus = _IfPowerStatus_Object(
    (1, 3, 6, 1, 4, 1, 4686, 11, 1, 36),
    _IfPowerStatus_Type()
)
ifPowerStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifPowerStatus.setStatus("mandatory")
_Interfaces_ObjectIdentity = ObjectIdentity
interfaces = _Interfaces_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4686, 11, 2)
)
_IfNumber_Type = Integer32
_IfNumber_Object = MibScalar
ifNumber = _IfNumber_Object(
    (1, 3, 6, 1, 4, 1, 4686, 11, 2, 1),
    _IfNumber_Type()
)
ifNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifNumber.setStatus("current")
_IfTable_Object = MibTable
ifTable = _IfTable_Object(
    (1, 3, 6, 1, 4, 1, 4686, 11, 2, 2)
)
if mibBuilder.loadTexts:
    ifTable.setStatus("current")
_IfEntry_Object = MibTableRow
ifEntry = _IfEntry_Object(
    (1, 3, 6, 1, 4, 1, 4686, 11, 2, 2, 1)
)
ifEntry.setIndexNames(
    (0, "Vega-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    ifEntry.setStatus("current")
_IfIndex_Type = InterfaceIndex
_IfIndex_Object = MibTableColumn
ifIndex = _IfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4686, 11, 2, 2, 1, 1),
    _IfIndex_Type()
)
ifIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifIndex.setStatus("current")
_IfType_Type = Integer32
_IfType_Object = MibTableColumn
ifType = _IfType_Object(
    (1, 3, 6, 1, 4, 1, 4686, 11, 2, 2, 1, 2),
    _IfType_Type()
)
ifType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifType.setStatus("current")
_IfNoCircuits_Type = Integer32
_IfNoCircuits_Object = MibTableColumn
ifNoCircuits = _IfNoCircuits_Object(
    (1, 3, 6, 1, 4, 1, 4686, 11, 2, 2, 1, 3),
    _IfNoCircuits_Type()
)
ifNoCircuits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifNoCircuits.setStatus("current")
_IfUpTime_Type = Integer32
_IfUpTime_Object = MibTableColumn
ifUpTime = _IfUpTime_Object(
    (1, 3, 6, 1, 4, 1, 4686, 11, 2, 2, 1, 4),
    _IfUpTime_Type()
)
ifUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifUpTime.setStatus("current")
_IfDownTime_Type = Integer32
_IfDownTime_Object = MibTableColumn
ifDownTime = _IfDownTime_Object(
    (1, 3, 6, 1, 4, 1, 4686, 11, 2, 2, 1, 5),
    _IfDownTime_Type()
)
ifDownTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifDownTime.setStatus("current")
_IfStartTime_Type = Integer32
_IfStartTime_Object = MibTableColumn
ifStartTime = _IfStartTime_Object(
    (1, 3, 6, 1, 4, 1, 4686, 11, 2, 2, 1, 6),
    _IfStartTime_Type()
)
ifStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifStartTime.setStatus("current")
_IfEndTime_Type = Integer32
_IfEndTime_Object = MibTableColumn
ifEndTime = _IfEndTime_Object(
    (1, 3, 6, 1, 4, 1, 4686, 11, 2, 2, 1, 7),
    _IfEndTime_Type()
)
ifEndTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifEndTime.setStatus("current")
_IfInboundCalls_Type = Counter32
_IfInboundCalls_Object = MibTableColumn
ifInboundCalls = _IfInboundCalls_Object(
    (1, 3, 6, 1, 4, 1, 4686, 11, 2, 2, 1, 8),
    _IfInboundCalls_Type()
)
ifInboundCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifInboundCalls.setStatus("current")
_IfInboundAnswered_Type = Counter32
_IfInboundAnswered_Object = MibTableColumn
ifInboundAnswered = _IfInboundAnswered_Object(
    (1, 3, 6, 1, 4, 1, 4686, 11, 2, 2, 1, 9),
    _IfInboundAnswered_Type()
)
ifInboundAnswered.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifInboundAnswered.setStatus("current")
_IfInboundBusy_Type = Counter32
_IfInboundBusy_Object = MibTableColumn
ifInboundBusy = _IfInboundBusy_Object(
    (1, 3, 6, 1, 4, 1, 4686, 11, 2, 2, 1, 10),
    _IfInboundBusy_Type()
)
ifInboundBusy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifInboundBusy.setStatus("current")
_IfInboundNoAnswer_Type = Counter32
_IfInboundNoAnswer_Object = MibTableColumn
ifInboundNoAnswer = _IfInboundNoAnswer_Object(
    (1, 3, 6, 1, 4, 1, 4686, 11, 2, 2, 1, 11),
    _IfInboundNoAnswer_Type()
)
ifInboundNoAnswer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifInboundNoAnswer.setStatus("current")
_IfInboundTermReject_Type = Counter32
_IfInboundTermReject_Object = MibTableColumn
ifInboundTermReject = _IfInboundTermReject_Object(
    (1, 3, 6, 1, 4, 1, 4686, 11, 2, 2, 1, 12),
    _IfInboundTermReject_Type()
)
ifInboundTermReject.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifInboundTermReject.setStatus("current")
_IfOutboundCalls_Type = Counter32
_IfOutboundCalls_Object = MibTableColumn
ifOutboundCalls = _IfOutboundCalls_Object(
    (1, 3, 6, 1, 4, 1, 4686, 11, 2, 2, 1, 13),
    _IfOutboundCalls_Type()
)
ifOutboundCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifOutboundCalls.setStatus("current")
_IfOutboundAnswered_Type = Counter32
_IfOutboundAnswered_Object = MibTableColumn
ifOutboundAnswered = _IfOutboundAnswered_Object(
    (1, 3, 6, 1, 4, 1, 4686, 11, 2, 2, 1, 14),
    _IfOutboundAnswered_Type()
)
ifOutboundAnswered.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifOutboundAnswered.setStatus("current")
_IfOutboundBusy_Type = Counter32
_IfOutboundBusy_Object = MibTableColumn
ifOutboundBusy = _IfOutboundBusy_Object(
    (1, 3, 6, 1, 4, 1, 4686, 11, 2, 2, 1, 15),
    _IfOutboundBusy_Type()
)
ifOutboundBusy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifOutboundBusy.setStatus("current")
_IfOutboundNoAnswer_Type = Counter32
_IfOutboundNoAnswer_Object = MibTableColumn
ifOutboundNoAnswer = _IfOutboundNoAnswer_Object(
    (1, 3, 6, 1, 4, 1, 4686, 11, 2, 2, 1, 16),
    _IfOutboundNoAnswer_Type()
)
ifOutboundNoAnswer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifOutboundNoAnswer.setStatus("current")
_IfOutboundTermReject_Type = Counter32
_IfOutboundTermReject_Object = MibTableColumn
ifOutboundTermReject = _IfOutboundTermReject_Object(
    (1, 3, 6, 1, 4, 1, 4686, 11, 2, 2, 1, 17),
    _IfOutboundTermReject_Type()
)
ifOutboundTermReject.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifOutboundTermReject.setStatus("current")
_IfInboundCurrUse_Type = Counter32
_IfInboundCurrUse_Object = MibTableColumn
ifInboundCurrUse = _IfInboundCurrUse_Object(
    (1, 3, 6, 1, 4, 1, 4686, 11, 2, 2, 1, 18),
    _IfInboundCurrUse_Type()
)
ifInboundCurrUse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifInboundCurrUse.setStatus("current")
_IfOutboundCurrUse_Type = Counter32
_IfOutboundCurrUse_Object = MibTableColumn
ifOutboundCurrUse = _IfOutboundCurrUse_Object(
    (1, 3, 6, 1, 4, 1, 4686, 11, 2, 2, 1, 19),
    _IfOutboundCurrUse_Type()
)
ifOutboundCurrUse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifOutboundCurrUse.setStatus("current")
_IfInboundMaxUse_Type = Counter32
_IfInboundMaxUse_Object = MibTableColumn
ifInboundMaxUse = _IfInboundMaxUse_Object(
    (1, 3, 6, 1, 4, 1, 4686, 11, 2, 2, 1, 20),
    _IfInboundMaxUse_Type()
)
ifInboundMaxUse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifInboundMaxUse.setStatus("current")
_IfOutboundMaxUse_Type = Counter32
_IfOutboundMaxUse_Object = MibTableColumn
ifOutboundMaxUse = _IfOutboundMaxUse_Object(
    (1, 3, 6, 1, 4, 1, 4686, 11, 2, 2, 1, 21),
    _IfOutboundMaxUse_Type()
)
ifOutboundMaxUse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifOutboundMaxUse.setStatus("current")
_IfAllMaxUse_Type = Counter32
_IfAllMaxUse_Object = MibTableColumn
ifAllMaxUse = _IfAllMaxUse_Object(
    (1, 3, 6, 1, 4, 1, 4686, 11, 2, 2, 1, 22),
    _IfAllMaxUse_Type()
)
ifAllMaxUse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifAllMaxUse.setStatus("current")
_IfInboundAvAnswer_Type = Integer32
_IfInboundAvAnswer_Object = MibTableColumn
ifInboundAvAnswer = _IfInboundAvAnswer_Object(
    (1, 3, 6, 1, 4, 1, 4686, 11, 2, 2, 1, 23),
    _IfInboundAvAnswer_Type()
)
ifInboundAvAnswer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifInboundAvAnswer.setStatus("current")
_IfOutboundAvAnswer_Type = Integer32
_IfOutboundAvAnswer_Object = MibTableColumn
ifOutboundAvAnswer = _IfOutboundAvAnswer_Object(
    (1, 3, 6, 1, 4, 1, 4686, 11, 2, 2, 1, 24),
    _IfOutboundAvAnswer_Type()
)
ifOutboundAvAnswer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifOutboundAvAnswer.setStatus("current")
_IfInboundAvCall_Type = Integer32
_IfInboundAvCall_Object = MibTableColumn
ifInboundAvCall = _IfInboundAvCall_Object(
    (1, 3, 6, 1, 4, 1, 4686, 11, 2, 2, 1, 25),
    _IfInboundAvCall_Type()
)
ifInboundAvCall.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifInboundAvCall.setStatus("current")
_IfInboundMaxCall_Type = Integer32
_IfInboundMaxCall_Object = MibTableColumn
ifInboundMaxCall = _IfInboundMaxCall_Object(
    (1, 3, 6, 1, 4, 1, 4686, 11, 2, 2, 1, 26),
    _IfInboundMaxCall_Type()
)
ifInboundMaxCall.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifInboundMaxCall.setStatus("current")
_IfOutboundAvCall_Type = Integer32
_IfOutboundAvCall_Object = MibTableColumn
ifOutboundAvCall = _IfOutboundAvCall_Object(
    (1, 3, 6, 1, 4, 1, 4686, 11, 2, 2, 1, 27),
    _IfOutboundAvCall_Type()
)
ifOutboundAvCall.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifOutboundAvCall.setStatus("current")
_IfOutboundMaxCall_Type = Integer32
_IfOutboundMaxCall_Object = MibTableColumn
ifOutboundMaxCall = _IfOutboundMaxCall_Object(
    (1, 3, 6, 1, 4, 1, 4686, 11, 2, 2, 1, 28),
    _IfOutboundMaxCall_Type()
)
ifOutboundMaxCall.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifOutboundMaxCall.setStatus("current")
_IfInboundAvDialSucc_Type = Integer32
_IfInboundAvDialSucc_Object = MibTableColumn
ifInboundAvDialSucc = _IfInboundAvDialSucc_Object(
    (1, 3, 6, 1, 4, 1, 4686, 11, 2, 2, 1, 29),
    _IfInboundAvDialSucc_Type()
)
ifInboundAvDialSucc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifInboundAvDialSucc.setStatus("current")
_IfOutboundAvDialSucc_Type = Integer32
_IfOutboundAvDialSucc_Object = MibTableColumn
ifOutboundAvDialSucc = _IfOutboundAvDialSucc_Object(
    (1, 3, 6, 1, 4, 1, 4686, 11, 2, 2, 1, 30),
    _IfOutboundAvDialSucc_Type()
)
ifOutboundAvDialSucc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifOutboundAvDialSucc.setStatus("current")
_IfInboundAvDialFail_Type = Integer32
_IfInboundAvDialFail_Object = MibTableColumn
ifInboundAvDialFail = _IfInboundAvDialFail_Object(
    (1, 3, 6, 1, 4, 1, 4686, 11, 2, 2, 1, 31),
    _IfInboundAvDialFail_Type()
)
ifInboundAvDialFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifInboundAvDialFail.setStatus("current")
_IfOutboundAvDialFail_Type = Integer32
_IfOutboundAvDialFail_Object = MibTableColumn
ifOutboundAvDialFail = _IfOutboundAvDialFail_Object(
    (1, 3, 6, 1, 4, 1, 4686, 11, 2, 2, 1, 32),
    _IfOutboundAvDialFail_Type()
)
ifOutboundAvDialFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifOutboundAvDialFail.setStatus("current")
_IfAverageJitter_Type = Integer32
_IfAverageJitter_Object = MibTableColumn
ifAverageJitter = _IfAverageJitter_Object(
    (1, 3, 6, 1, 4, 1, 4686, 11, 2, 2, 1, 33),
    _IfAverageJitter_Type()
)
ifAverageJitter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifAverageJitter.setStatus("current")
_IfMaximumJitter_Type = Integer32
_IfMaximumJitter_Object = MibTableColumn
ifMaximumJitter = _IfMaximumJitter_Object(
    (1, 3, 6, 1, 4, 1, 4686, 11, 2, 2, 1, 34),
    _IfMaximumJitter_Type()
)
ifMaximumJitter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifMaximumJitter.setStatus("current")
_IfAverageLoss_Type = Integer32
_IfAverageLoss_Object = MibTableColumn
ifAverageLoss = _IfAverageLoss_Object(
    (1, 3, 6, 1, 4, 1, 4686, 11, 2, 2, 1, 35),
    _IfAverageLoss_Type()
)
ifAverageLoss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifAverageLoss.setStatus("current")
_IfMaximumLoss_Type = Integer32
_IfMaximumLoss_Object = MibTableColumn
ifMaximumLoss = _IfMaximumLoss_Object(
    (1, 3, 6, 1, 4, 1, 4686, 11, 2, 2, 1, 36),
    _IfMaximumLoss_Type()
)
ifMaximumLoss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifMaximumLoss.setStatus("current")
_SipUsrTable_Object = MibTable
sipUsrTable = _SipUsrTable_Object(
    (1, 3, 6, 1, 4, 1, 4686, 11, 2, 3)
)
if mibBuilder.loadTexts:
    sipUsrTable.setStatus("current")
_SipUsrEntry_Object = MibTableRow
sipUsrEntry = _SipUsrEntry_Object(
    (1, 3, 6, 1, 4, 1, 4686, 11, 2, 3, 1)
)
sipUsrEntry.setIndexNames(
    (0, "Vega-MIB", "sipIndex"),
)
if mibBuilder.loadTexts:
    sipUsrEntry.setStatus("current")
_SipIndex_Type = SipUsrIndex
_SipIndex_Object = MibTableColumn
sipIndex = _SipIndex_Object(
    (1, 3, 6, 1, 4, 1, 4686, 11, 2, 3, 1, 1),
    _SipIndex_Type()
)
sipIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sipIndex.setStatus("current")
_SipRegisterUser_Type = Integer32
_SipRegisterUser_Object = MibTableColumn
sipRegisterUser = _SipRegisterUser_Object(
    (1, 3, 6, 1, 4, 1, 4686, 11, 2, 3, 1, 2),
    _SipRegisterUser_Type()
)
sipRegisterUser.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sipRegisterUser.setStatus("current")
_SipRegisterStatus_Type = OctetString
_SipRegisterStatus_Object = MibTableColumn
sipRegisterStatus = _SipRegisterStatus_Object(
    (1, 3, 6, 1, 4, 1, 4686, 11, 2, 3, 1, 3),
    _SipRegisterStatus_Type()
)
sipRegisterStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sipRegisterStatus.setStatus("current")
_SipRegisterAddress_Type = OctetString
_SipRegisterAddress_Object = MibTableColumn
sipRegisterAddress = _SipRegisterAddress_Object(
    (1, 3, 6, 1, 4, 1, 4686, 11, 2, 3, 1, 4),
    _SipRegisterAddress_Type()
)
sipRegisterAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sipRegisterAddress.setStatus("current")
_SipRegisterRegistrar_Type = OctetString
_SipRegisterRegistrar_Object = MibTableColumn
sipRegisterRegistrar = _SipRegisterRegistrar_Object(
    (1, 3, 6, 1, 4, 1, 4686, 11, 2, 3, 1, 5),
    _SipRegisterRegistrar_Type()
)
sipRegisterRegistrar.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sipRegisterRegistrar.setStatus("current")
_SipRegisterContact_Type = OctetString
_SipRegisterContact_Object = MibTableColumn
sipRegisterContact = _SipRegisterContact_Object(
    (1, 3, 6, 1, 4, 1, 4686, 11, 2, 3, 1, 6),
    _SipRegisterContact_Type()
)
sipRegisterContact.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sipRegisterContact.setStatus("current")
_SipRegisterSipProfile_Type = Integer32
_SipRegisterSipProfile_Object = MibTableColumn
sipRegisterSipProfile = _SipRegisterSipProfile_Object(
    (1, 3, 6, 1, 4, 1, 4686, 11, 2, 3, 1, 7),
    _SipRegisterSipProfile_Type()
)
sipRegisterSipProfile.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sipRegisterSipProfile.setStatus("current")
_SipRegisterTTL_Type = Integer32
_SipRegisterTTL_Object = MibTableColumn
sipRegisterTTL = _SipRegisterTTL_Object(
    (1, 3, 6, 1, 4, 1, 4686, 11, 2, 3, 1, 8),
    _SipRegisterTTL_Type()
)
sipRegisterTTL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sipRegisterTTL.setStatus("current")

# Managed Objects groups


# Notification objects

fileServerOrFileNotFound = NotificationType(
    (1, 3, 6, 1, 4, 1, 4686, 11, 0, 1)
)
if mibBuilder.loadTexts:
    fileServerOrFileNotFound.setStatus(
        ""
    )

scriptFileTooBig = NotificationType(
    (1, 3, 6, 1, 4, 1, 4686, 11, 0, 2)
)
if mibBuilder.loadTexts:
    scriptFileTooBig.setStatus(
        ""
    )

fileServerUnknownError = NotificationType(
    (1, 3, 6, 1, 4, 1, 4686, 11, 0, 3)
)
if mibBuilder.loadTexts:
    fileServerUnknownError.setStatus(
        ""
    )

fileDoesNotExist = NotificationType(
    (1, 3, 6, 1, 4, 1, 4686, 11, 0, 4)
)
if mibBuilder.loadTexts:
    fileDoesNotExist.setStatus(
        ""
    )

recurFileServerGetError = NotificationType(
    (1, 3, 6, 1, 4, 1, 4686, 11, 0, 5)
)
if mibBuilder.loadTexts:
    recurFileServerGetError.setStatus(
        ""
    )

fileServerGetMemoryError = NotificationType(
    (1, 3, 6, 1, 4, 1, 4686, 11, 0, 6)
)
if mibBuilder.loadTexts:
    fileServerGetMemoryError.setStatus(
        ""
    )

lanInterfaceNotActive = NotificationType(
    (1, 3, 6, 1, 4, 1, 4686, 11, 0, 7)
)
if mibBuilder.loadTexts:
    lanInterfaceNotActive.setStatus(
        ""
    )

ftpNotConfigured = NotificationType(
    (1, 3, 6, 1, 4, 1, 4686, 11, 0, 8)
)
if mibBuilder.loadTexts:
    ftpNotConfigured.setStatus(
        ""
    )

invalidUserParams = NotificationType(
    (1, 3, 6, 1, 4, 1, 4686, 11, 0, 9)
)
if mibBuilder.loadTexts:
    invalidUserParams.setStatus(
        ""
    )

serverUnavailable = NotificationType(
    (1, 3, 6, 1, 4, 1, 4686, 11, 0, 10)
)
if mibBuilder.loadTexts:
    serverUnavailable.setStatus(
        ""
    )

systemNotReady = NotificationType(
    (1, 3, 6, 1, 4, 1, 4686, 11, 0, 11)
)
if mibBuilder.loadTexts:
    systemNotReady.setStatus(
        ""
    )

tftpNotConfigured = NotificationType(
    (1, 3, 6, 1, 4, 1, 4686, 11, 0, 12)
)
if mibBuilder.loadTexts:
    tftpNotConfigured.setStatus(
        ""
    )

httpNotConfigured = NotificationType(
    (1, 3, 6, 1, 4, 1, 4686, 11, 0, 13)
)
if mibBuilder.loadTexts:
    httpNotConfigured.setStatus(
        ""
    )

httpsNotConfigured = NotificationType(
    (1, 3, 6, 1, 4, 1, 4686, 11, 0, 14)
)
if mibBuilder.loadTexts:
    httpsNotConfigured.setStatus(
        ""
    )

configNotLoaded = NotificationType(
    (1, 3, 6, 1, 4, 1, 4686, 11, 0, 21)
)
if mibBuilder.loadTexts:
    configNotLoaded.setStatus(
        ""
    )

firmwareNotLoaded = NotificationType(
    (1, 3, 6, 1, 4, 1, 4686, 11, 0, 22)
)
if mibBuilder.loadTexts:
    firmwareNotLoaded.setStatus(
        ""
    )

configLoaded = NotificationType(
    (1, 3, 6, 1, 4, 1, 4686, 11, 0, 23)
)
if mibBuilder.loadTexts:
    configLoaded.setStatus(
        ""
    )

firmwareLoaded = NotificationType(
    (1, 3, 6, 1, 4, 1, 4686, 11, 0, 24)
)
if mibBuilder.loadTexts:
    firmwareLoaded.setStatus(
        ""
    )

bypassRelayActivated = NotificationType(
    (1, 3, 6, 1, 4, 1, 4686, 11, 0, 25)
)
if mibBuilder.loadTexts:
    bypassRelayActivated.setStatus(
        ""
    )

pktLossThresholdExceed = NotificationType(
    (1, 3, 6, 1, 4, 1, 4686, 11, 0, 30)
)
if mibBuilder.loadTexts:
    pktLossThresholdExceed.setStatus(
        ""
    )

playoutThresholdExceed = NotificationType(
    (1, 3, 6, 1, 4, 1, 4686, 11, 0, 31)
)
if mibBuilder.loadTexts:
    playoutThresholdExceed.setStatus(
        ""
    )

jitterThresholdExceed = NotificationType(
    (1, 3, 6, 1, 4, 1, 4686, 11, 0, 32)
)
if mibBuilder.loadTexts:
    jitterThresholdExceed.setStatus(
        ""
    )

sysFanFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 4686, 11, 0, 40)
)
if mibBuilder.loadTexts:
    sysFanFailed.setStatus(
        ""
    )

sysFanOK = NotificationType(
    (1, 3, 6, 1, 4, 1, 4686, 11, 0, 41)
)
if mibBuilder.loadTexts:
    sysFanOK.setStatus(
        ""
    )

sysOverTempIndication = NotificationType(
    (1, 3, 6, 1, 4, 1, 4686, 11, 0, 42)
)
if mibBuilder.loadTexts:
    sysOverTempIndication.setStatus(
        ""
    )

sysOverTempOK = NotificationType(
    (1, 3, 6, 1, 4, 1, 4686, 11, 0, 43)
)
if mibBuilder.loadTexts:
    sysOverTempOK.setStatus(
        ""
    )

sysOverPower = NotificationType(
    (1, 3, 6, 1, 4, 1, 4686, 11, 0, 44)
)
if mibBuilder.loadTexts:
    sysOverPower.setStatus(
        ""
    )

sysOverPowerOK = NotificationType(
    (1, 3, 6, 1, 4, 1, 4686, 11, 0, 45)
)
if mibBuilder.loadTexts:
    sysOverPowerOK.setStatus(
        ""
    )

fxsPortShutDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 4686, 11, 0, 46)
)
if mibBuilder.loadTexts:
    fxsPortShutDown.setStatus(
        ""
    )

sipRegistrationSuccess = NotificationType(
    (1, 3, 6, 1, 4, 1, 4686, 11, 0, 50)
)
sipRegistrationSuccess.setObjects(
    ("SNMPv2-MIB", "sysDescr")
)
if mibBuilder.loadTexts:
    sipRegistrationSuccess.setStatus(
        ""
    )

sipRegistrationFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 4686, 11, 0, 51)
)
sipRegistrationFailure.setObjects(
    ("SNMPv2-MIB", "sysDescr")
)
if mibBuilder.loadTexts:
    sipRegistrationFailure.setStatus(
        ""
    )

sipUnRegistered = NotificationType(
    (1, 3, 6, 1, 4, 1, 4686, 11, 0, 52)
)
sipUnRegistered.setObjects(
    ("SNMPv2-MIB", "sysDescr")
)
if mibBuilder.loadTexts:
    sipUnRegistered.setStatus(
        ""
    )

iSDNLinkUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 4686, 11, 0, 60)
)
iSDNLinkUp.setObjects(
    ("SNMPv2-MIB", "sysDescr")
)
if mibBuilder.loadTexts:
    iSDNLinkUp.setStatus(
        ""
    )

iSDNLinkDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 4686, 11, 0, 61)
)
iSDNLinkDown.setObjects(
    ("SNMPv2-MIB", "sysDescr")
)
if mibBuilder.loadTexts:
    iSDNLinkDown.setStatus(
        ""
    )

lANLinkUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 4686, 11, 0, 62)
)
lANLinkUp.setObjects(
    ("SNMPv2-MIB", "sysDescr")
)
if mibBuilder.loadTexts:
    lANLinkUp.setStatus(
        ""
    )

lANLinkDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 4686, 11, 0, 63)
)
lANLinkDown.setObjects(
    ("SNMPv2-MIB", "sysDescr")
)
if mibBuilder.loadTexts:
    lANLinkDown.setStatus(
        ""
    )

cOLDSTART = NotificationType(
    (1, 3, 6, 1, 4, 1, 4686, 11, 0, 64)
)
cOLDSTART.setObjects(
    ("SNMPv2-MIB", "sysDescr")
)
if mibBuilder.loadTexts:
    cOLDSTART.setStatus(
        ""
    )

wARMSTART = NotificationType(
    (1, 3, 6, 1, 4, 1, 4686, 11, 0, 65)
)
wARMSTART.setObjects(
    ("SNMPv2-MIB", "sysDescr")
)
if mibBuilder.loadTexts:
    wARMSTART.setStatus(
        ""
    )

dspFatalError = NotificationType(
    (1, 3, 6, 1, 4, 1, 4686, 11, 0, 66)
)
dspFatalError.setObjects(
    ("SNMPv2-MIB", "sysDescr")
)
if mibBuilder.loadTexts:
    dspFatalError.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Vega-MIB",
    **{"InterfaceIndex": InterfaceIndex,
       "SipUsrIndex": SipUsrIndex,
       "vega": vega,
       "vsplatform": vsplatform,
       "fileServerOrFileNotFound": fileServerOrFileNotFound,
       "scriptFileTooBig": scriptFileTooBig,
       "fileServerUnknownError": fileServerUnknownError,
       "fileDoesNotExist": fileDoesNotExist,
       "recurFileServerGetError": recurFileServerGetError,
       "fileServerGetMemoryError": fileServerGetMemoryError,
       "lanInterfaceNotActive": lanInterfaceNotActive,
       "ftpNotConfigured": ftpNotConfigured,
       "invalidUserParams": invalidUserParams,
       "serverUnavailable": serverUnavailable,
       "systemNotReady": systemNotReady,
       "tftpNotConfigured": tftpNotConfigured,
       "httpNotConfigured": httpNotConfigured,
       "httpsNotConfigured": httpsNotConfigured,
       "configNotLoaded": configNotLoaded,
       "firmwareNotLoaded": firmwareNotLoaded,
       "configLoaded": configLoaded,
       "firmwareLoaded": firmwareLoaded,
       "bypassRelayActivated": bypassRelayActivated,
       "pktLossThresholdExceed": pktLossThresholdExceed,
       "playoutThresholdExceed": playoutThresholdExceed,
       "jitterThresholdExceed": jitterThresholdExceed,
       "sysFanFailed": sysFanFailed,
       "sysFanOK": sysFanOK,
       "sysOverTempIndication": sysOverTempIndication,
       "sysOverTempOK": sysOverTempOK,
       "sysOverPower": sysOverPower,
       "sysOverPowerOK": sysOverPowerOK,
       "fxsPortShutDown": fxsPortShutDown,
       "sipRegistrationSuccess": sipRegistrationSuccess,
       "sipRegistrationFailure": sipRegistrationFailure,
       "sipUnRegistered": sipUnRegistered,
       "iSDNLinkUp": iSDNLinkUp,
       "iSDNLinkDown": iSDNLinkDown,
       "lANLinkUp": lANLinkUp,
       "lANLinkDown": lANLinkDown,
       "cOLDSTART": cOLDSTART,
       "wARMSTART": wARMSTART,
       "dspFatalError": dspFatalError,
       "callStats": callStats,
       "noCircuits": noCircuits,
       "upTime": upTime,
       "downTime": downTime,
       "startTime": startTime,
       "endTime": endTime,
       "inboundCalls": inboundCalls,
       "inboundAnswered": inboundAnswered,
       "inboundBusy": inboundBusy,
       "inboundNoAnswer": inboundNoAnswer,
       "inboundTermReject": inboundTermReject,
       "outboundCalls": outboundCalls,
       "outboundAnswered": outboundAnswered,
       "outboundBusy": outboundBusy,
       "outboundNoAnswer": outboundNoAnswer,
       "outboundTermReject": outboundTermReject,
       "inboundCurrUse": inboundCurrUse,
       "outboundCurrUse": outboundCurrUse,
       "inboundMaxUse": inboundMaxUse,
       "outboundMaxUse": outboundMaxUse,
       "allMaxUse": allMaxUse,
       "inboundAvAnswer": inboundAvAnswer,
       "outboundAvAnswer": outboundAvAnswer,
       "inboundAvCall": inboundAvCall,
       "inboundMaxCall": inboundMaxCall,
       "outboundAvCall": outboundAvCall,
       "outboundMaxCall": outboundMaxCall,
       "inboundAvDialSucc": inboundAvDialSucc,
       "outboundAvDialSucc": outboundAvDialSucc,
       "inboundAvDialFail": inboundAvDialFail,
       "outboundAvDialFail": outboundAvDialFail,
       "averageJitter": averageJitter,
       "maximumJitter": maximumJitter,
       "averageLoss": averageLoss,
       "maximumLoss": maximumLoss,
       "ifFanState": ifFanState,
       "ifPowerStatus": ifPowerStatus,
       "interfaces": interfaces,
       "ifNumber": ifNumber,
       "ifTable": ifTable,
       "ifEntry": ifEntry,
       "ifIndex": ifIndex,
       "ifType": ifType,
       "ifNoCircuits": ifNoCircuits,
       "ifUpTime": ifUpTime,
       "ifDownTime": ifDownTime,
       "ifStartTime": ifStartTime,
       "ifEndTime": ifEndTime,
       "ifInboundCalls": ifInboundCalls,
       "ifInboundAnswered": ifInboundAnswered,
       "ifInboundBusy": ifInboundBusy,
       "ifInboundNoAnswer": ifInboundNoAnswer,
       "ifInboundTermReject": ifInboundTermReject,
       "ifOutboundCalls": ifOutboundCalls,
       "ifOutboundAnswered": ifOutboundAnswered,
       "ifOutboundBusy": ifOutboundBusy,
       "ifOutboundNoAnswer": ifOutboundNoAnswer,
       "ifOutboundTermReject": ifOutboundTermReject,
       "ifInboundCurrUse": ifInboundCurrUse,
       "ifOutboundCurrUse": ifOutboundCurrUse,
       "ifInboundMaxUse": ifInboundMaxUse,
       "ifOutboundMaxUse": ifOutboundMaxUse,
       "ifAllMaxUse": ifAllMaxUse,
       "ifInboundAvAnswer": ifInboundAvAnswer,
       "ifOutboundAvAnswer": ifOutboundAvAnswer,
       "ifInboundAvCall": ifInboundAvCall,
       "ifInboundMaxCall": ifInboundMaxCall,
       "ifOutboundAvCall": ifOutboundAvCall,
       "ifOutboundMaxCall": ifOutboundMaxCall,
       "ifInboundAvDialSucc": ifInboundAvDialSucc,
       "ifOutboundAvDialSucc": ifOutboundAvDialSucc,
       "ifInboundAvDialFail": ifInboundAvDialFail,
       "ifOutboundAvDialFail": ifOutboundAvDialFail,
       "ifAverageJitter": ifAverageJitter,
       "ifMaximumJitter": ifMaximumJitter,
       "ifAverageLoss": ifAverageLoss,
       "ifMaximumLoss": ifMaximumLoss,
       "sipUsrTable": sipUsrTable,
       "sipUsrEntry": sipUsrEntry,
       "sipIndex": sipIndex,
       "sipRegisterUser": sipRegisterUser,
       "sipRegisterStatus": sipRegisterStatus,
       "sipRegisterAddress": sipRegisterAddress,
       "sipRegisterRegistrar": sipRegisterRegistrar,
       "sipRegisterContact": sipRegisterContact,
       "sipRegisterSipProfile": sipRegisterSipProfile,
       "sipRegisterTTL": sipRegisterTTL}
)
