# SNMP MIB module (RS-XX8000-DVB-TX-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\rs\RS-XX8000-DVB-TX-MIB

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

(EqualizerCalibrationState,
 EventClass,
 EventMask,
 EventMaxEntryNumber,
 EventPriority,
 EventState,
 FailDelayMode,
 FailDelayStatus,
 FloatingPoint,
 IndexAB,
 IndexAmplifier,
 IndexRack,
 InputSource,
 LogbookEntryMessagesExcTv,
 LogbookEntryMessagesNetCCU,
 LogbookEntryMessagesOST,
 LogbookEntrySlope,
 LogbookMaxEntryNumber,
 ProdInfoModuleNameTv,
 ReadableString,
 SwitchOnOff,
 Sx801AmplifierState,
 TimeOfDay,
 Trigger,
 TvStandard,
 eventAlarmClass,
 eventAlarmPriority,
 eventEvent,
 indexAB,
 indexAmplifier,
 indexRack,
 rsXx8000,
 rsXx8000MibModule) = mibBuilder.importSymbols(
    "RS-XX8000-COMMON-MIB",
    "EqualizerCalibrationState",
    "EventClass",
    "EventMask",
    "EventMaxEntryNumber",
    "EventPriority",
    "EventState",
    "FailDelayMode",
    "FailDelayStatus",
    "FloatingPoint",
    "IndexAB",
    "IndexAmplifier",
    "IndexRack",
    "InputSource",
    "LogbookEntryMessagesExcTv",
    "LogbookEntryMessagesNetCCU",
    "LogbookEntryMessagesOST",
    "LogbookEntrySlope",
    "LogbookMaxEntryNumber",
    "ProdInfoModuleNameTv",
    "ReadableString",
    "SwitchOnOff",
    "Sx801AmplifierState",
    "TimeOfDay",
    "Trigger",
    "TvStandard",
    "eventAlarmClass",
    "eventAlarmPriority",
    "eventEvent",
    "indexAB",
    "indexAmplifier",
    "indexRack",
    "rsXx8000",
    "rsXx8000MibModule")

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

rsXx8000DvbTxMibModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2566, 149, 1, 163, 3)
)
if mibBuilder.loadTexts:
    rsXx8000DvbTxMibModule.setRevisions(
        ("2012-11-01 08:00",
         "2012-09-03 08:00",
         "2011-05-12 08:00",
         "2011-02-28 08:00",
         "2010-12-02 08:00",
         "2010-10-13 08:00",
         "2010-05-21 08:00",
         "2010-04-16 08:00",
         "2010-02-02 08:00",
         "2010-01-29 08:00",
         "2010-01-12 08:00",
         "2009-12-18 08:00",
         "2009-11-26 08:00",
         "2009-11-13 08:00",
         "2009-10-08 08:00",
         "2009-09-10 08:00",
         "2009-07-16 08:00",
         "2009-06-26 08:00",
         "2009-06-17 09:00",
         "2009-05-28 09:00",
         "2009-03-30 09:00",
         "2009-02-12 15:00",
         "2009-01-29 09:00",
         "2009-01-06 16:00",
         "2008-12-12 14:30",
         "2008-10-23 08:00",
         "2008-10-08 10:30",
         "2008-09-10 15:00",
         "2008-08-29 10:00",
         "2008-08-26 09:00",
         "2008-07-23 10:00",
         "2008-05-05 09:30",
         "2008-03-31 11:00",
         "2007-12-07 17:00",
         "2007-09-10 11:00",
         "2007-08-09 14:00",
         "2007-07-11 16:00",
         "2007-03-08 10:00",
         "2006-12-21 10:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_RsXx8000DvbTx_ObjectIdentity = ObjectIdentity
rsXx8000DvbTx = _RsXx8000DvbTx_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 4)
)
if mibBuilder.loadTexts:
    rsXx8000DvbTx.setStatus("current")
_RsXx8000DvbTxObjs_ObjectIdentity = ObjectIdentity
rsXx8000DvbTxObjs = _RsXx8000DvbTxObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 4, 1)
)
_CommandsTxTable_Object = MibTable
commandsTxTable = _CommandsTxTable_Object(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 4, 1, 1)
)
if mibBuilder.loadTexts:
    commandsTxTable.setStatus("current")
_CommandsTxEntry_Object = MibTableRow
commandsTxEntry = _CommandsTxEntry_Object(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 4, 1, 1, 1)
)
commandsTxEntry.setIndexNames(
    (0, "RS-XX8000-DVB-TX-MIB", "cmdDeviceIdx"),
)
if mibBuilder.loadTexts:
    commandsTxEntry.setStatus("current")
_CmdTxResetSumFault_Type = Trigger
_CmdTxResetSumFault_Object = MibTableColumn
cmdTxResetSumFault = _CmdTxResetSumFault_Object(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 4, 1, 1, 1, 1),
    _CmdTxResetSumFault_Type()
)
cmdTxResetSumFault.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmdTxResetSumFault.setStatus("current")


class _CmdTxParametersetLoad_Type(Integer32):
    """Custom type cmdTxParametersetLoad based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_CmdTxParametersetLoad_Type.__name__ = "Integer32"
_CmdTxParametersetLoad_Object = MibTableColumn
cmdTxParametersetLoad = _CmdTxParametersetLoad_Object(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 4, 1, 1, 1, 2),
    _CmdTxParametersetLoad_Type()
)
cmdTxParametersetLoad.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmdTxParametersetLoad.setStatus("current")


class _CmdTxParametersetSave_Type(Integer32):
    """Custom type cmdTxParametersetSave based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_CmdTxParametersetSave_Type.__name__ = "Integer32"
_CmdTxParametersetSave_Object = MibTableColumn
cmdTxParametersetSave = _CmdTxParametersetSave_Object(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 4, 1, 1, 1, 3),
    _CmdTxParametersetSave_Type()
)
cmdTxParametersetSave.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmdTxParametersetSave.setStatus("current")
_CmdTxParametersetReSave_Type = Trigger
_CmdTxParametersetReSave_Object = MibTableColumn
cmdTxParametersetReSave = _CmdTxParametersetReSave_Object(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 4, 1, 1, 1, 4),
    _CmdTxParametersetReSave_Type()
)
cmdTxParametersetReSave.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmdTxParametersetReSave.setStatus("obsolete")
_CmdTxOperationModeProgram_Type = SwitchOnOff
_CmdTxOperationModeProgram_Object = MibTableColumn
cmdTxOperationModeProgram = _CmdTxOperationModeProgram_Object(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 4, 1, 1, 1, 5),
    _CmdTxOperationModeProgram_Type()
)
cmdTxOperationModeProgram.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmdTxOperationModeProgram.setStatus("current")
_CmdTxOperationModeReserve_Type = SwitchOnOff
_CmdTxOperationModeReserve_Object = MibTableColumn
cmdTxOperationModeReserve = _CmdTxOperationModeReserve_Object(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 4, 1, 1, 1, 6),
    _CmdTxOperationModeReserve_Type()
)
cmdTxOperationModeReserve.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmdTxOperationModeReserve.setStatus("current")
_CmdTxOpModeExcAutomatic_Type = SwitchOnOff
_CmdTxOpModeExcAutomatic_Object = MibTableColumn
cmdTxOpModeExcAutomatic = _CmdTxOpModeExcAutomatic_Object(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 4, 1, 1, 1, 7),
    _CmdTxOpModeExcAutomatic_Type()
)
cmdTxOpModeExcAutomatic.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmdTxOpModeExcAutomatic.setStatus("current")
_CmdTxOpModeOstAutomatic_Type = SwitchOnOff
_CmdTxOpModeOstAutomatic_Object = MibTableColumn
cmdTxOpModeOstAutomatic = _CmdTxOpModeOstAutomatic_Object(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 4, 1, 1, 1, 8),
    _CmdTxOpModeOstAutomatic_Type()
)
cmdTxOpModeOstAutomatic.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmdTxOpModeOstAutomatic.setStatus("current")
_CmdTxPreselectExciter_Type = IndexAB
_CmdTxPreselectExciter_Object = MibTableColumn
cmdTxPreselectExciter = _CmdTxPreselectExciter_Object(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 4, 1, 1, 1, 9),
    _CmdTxPreselectExciter_Type()
)
cmdTxPreselectExciter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmdTxPreselectExciter.setStatus("current")


class _CmdTxPreselectOutputstage_Type(Integer32):
    """Custom type cmdTxPreselectOutputstage based on Integer32"""
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
        *(("outputstageA", 1),
          ("outputstageB", 2),
          ("bothToAntenna", 3),
          ("bothToDummyLoad", 4))
    )


_CmdTxPreselectOutputstage_Type.__name__ = "Integer32"
_CmdTxPreselectOutputstage_Object = MibTableColumn
cmdTxPreselectOutputstage = _CmdTxPreselectOutputstage_Object(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 4, 1, 1, 1, 10),
    _CmdTxPreselectOutputstage_Type()
)
cmdTxPreselectOutputstage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmdTxPreselectOutputstage.setStatus("current")


class _CmdTxDelayTimeExcAutomatic_Type(Integer32):
    """Custom type cmdTxDelayTimeExcAutomatic based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 60),
    )


_CmdTxDelayTimeExcAutomatic_Type.__name__ = "Integer32"
_CmdTxDelayTimeExcAutomatic_Object = MibTableColumn
cmdTxDelayTimeExcAutomatic = _CmdTxDelayTimeExcAutomatic_Object(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 4, 1, 1, 1, 11),
    _CmdTxDelayTimeExcAutomatic_Type()
)
cmdTxDelayTimeExcAutomatic.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmdTxDelayTimeExcAutomatic.setStatus("current")
if mibBuilder.loadTexts:
    cmdTxDelayTimeExcAutomatic.setUnits("seconds")


class _CmdTxDelayTimeOstAutomatic_Type(Integer32):
    """Custom type cmdTxDelayTimeOstAutomatic based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 60),
    )


_CmdTxDelayTimeOstAutomatic_Type.__name__ = "Integer32"
_CmdTxDelayTimeOstAutomatic_Object = MibTableColumn
cmdTxDelayTimeOstAutomatic = _CmdTxDelayTimeOstAutomatic_Object(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 4, 1, 1, 1, 12),
    _CmdTxDelayTimeOstAutomatic_Type()
)
cmdTxDelayTimeOstAutomatic.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmdTxDelayTimeOstAutomatic.setStatus("current")
if mibBuilder.loadTexts:
    cmdTxDelayTimeOstAutomatic.setUnits("seconds")


class _CmdTxRfSwitch_Type(Integer32):
    """Custom type cmdTxRfSwitch based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("antenna", 1),
          ("dummyLoad", 2))
    )


_CmdTxRfSwitch_Type.__name__ = "Integer32"
_CmdTxRfSwitch_Object = MibTableColumn
cmdTxRfSwitch = _CmdTxRfSwitch_Object(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 4, 1, 1, 1, 13),
    _CmdTxRfSwitch_Type()
)
cmdTxRfSwitch.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmdTxRfSwitch.setStatus("current")
_CmdTxSystemMode_Type = TvStandard
_CmdTxSystemMode_Object = MibTableColumn
cmdTxSystemMode = _CmdTxSystemMode_Object(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 4, 1, 1, 1, 15),
    _CmdTxSystemMode_Type()
)
cmdTxSystemMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmdTxSystemMode.setStatus("current")
_CmdTxProgramExciterPrio_Type = SwitchOnOff
_CmdTxProgramExciterPrio_Object = MibTableColumn
cmdTxProgramExciterPrio = _CmdTxProgramExciterPrio_Object(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 4, 1, 1, 1, 20),
    _CmdTxProgramExciterPrio_Type()
)
cmdTxProgramExciterPrio.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmdTxProgramExciterPrio.setStatus("current")
_CmdTxChangeOver_Type = Trigger
_CmdTxChangeOver_Object = MibTableColumn
cmdTxChangeOver = _CmdTxChangeOver_Object(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 4, 1, 1, 1, 21),
    _CmdTxChangeOver_Type()
)
cmdTxChangeOver.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmdTxChangeOver.setStatus("current")


class _CmdTxSwitchPosition_Type(Integer32):
    """Custom type cmdTxSwitchPosition based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("undefined", 1),
          ("controlExcOnAmp", 2),
          ("programExcOnAmp", 3))
    )


_CmdTxSwitchPosition_Type.__name__ = "Integer32"
_CmdTxSwitchPosition_Object = MibTableColumn
cmdTxSwitchPosition = _CmdTxSwitchPosition_Object(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 4, 1, 1, 1, 22),
    _CmdTxSwitchPosition_Type()
)
cmdTxSwitchPosition.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmdTxSwitchPosition.setStatus("current")
_CmdDeviceIdx_Type = IndexAB
_CmdDeviceIdx_Object = MibTableColumn
cmdDeviceIdx = _CmdDeviceIdx_Object(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 4, 1, 1, 1, 30),
    _CmdDeviceIdx_Type()
)
cmdDeviceIdx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cmdDeviceIdx.setStatus("current")
_CmdExcOpModeInputAutomatic_Type = SwitchOnOff
_CmdExcOpModeInputAutomatic_Object = MibTableColumn
cmdExcOpModeInputAutomatic = _CmdExcOpModeInputAutomatic_Object(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 4, 1, 1, 1, 31),
    _CmdExcOpModeInputAutomatic_Type()
)
cmdExcOpModeInputAutomatic.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmdExcOpModeInputAutomatic.setStatus("current")


class _CmdExcPreselectInput_Type(Integer32):
    """Custom type cmdExcPreselectInput based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("input1", 1),
          ("input2", 2))
    )


_CmdExcPreselectInput_Type.__name__ = "Integer32"
_CmdExcPreselectInput_Object = MibTableColumn
cmdExcPreselectInput = _CmdExcPreselectInput_Object(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 4, 1, 1, 1, 32),
    _CmdExcPreselectInput_Type()
)
cmdExcPreselectInput.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmdExcPreselectInput.setStatus("current")


class _CmdExcMode_Type(Integer32):
    """Custom type cmdExcMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dvbT", 1),
          ("dvbH", 2))
    )


_CmdExcMode_Type.__name__ = "Integer32"
_CmdExcMode_Object = MibTableColumn
cmdExcMode = _CmdExcMode_Object(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 4, 1, 1, 1, 33),
    _CmdExcMode_Type()
)
cmdExcMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmdExcMode.setStatus("current")


class _CmdExcNetworkMode_Type(Integer32):
    """Custom type cmdExcNetworkMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("mfn", 1),
          ("sfn", 2))
    )


_CmdExcNetworkMode_Type.__name__ = "Integer32"
_CmdExcNetworkMode_Object = MibTableColumn
cmdExcNetworkMode = _CmdExcNetworkMode_Object(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 4, 1, 1, 1, 34),
    _CmdExcNetworkMode_Type()
)
cmdExcNetworkMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmdExcNetworkMode.setStatus("current")


class _CmdExcTPSSource_Type(Integer32):
    """Custom type cmdExcTPSSource based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("manualPresets", 1),
          ("mip", 2))
    )


_CmdExcTPSSource_Type.__name__ = "Integer32"
_CmdExcTPSSource_Object = MibTableColumn
cmdExcTPSSource = _CmdExcTPSSource_Object(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 4, 1, 1, 1, 35),
    _CmdExcTPSSource_Type()
)
cmdExcTPSSource.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmdExcTPSSource.setStatus("current")
_CmdExcEnableCellID_Type = SwitchOnOff
_CmdExcEnableCellID_Object = MibTableColumn
cmdExcEnableCellID = _CmdExcEnableCellID_Object(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 4, 1, 1, 1, 36),
    _CmdExcEnableCellID_Type()
)
cmdExcEnableCellID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmdExcEnableCellID.setStatus("current")


class _CmdExcTxAddress_Type(Integer32):
    """Custom type cmdExcTxAddress based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CmdExcTxAddress_Type.__name__ = "Integer32"
_CmdExcTxAddress_Object = MibTableColumn
cmdExcTxAddress = _CmdExcTxAddress_Object(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 4, 1, 1, 1, 37),
    _CmdExcTxAddress_Type()
)
cmdExcTxAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmdExcTxAddress.setStatus("current")
_CmdExcTxAutomatic_Type = SwitchOnOff
_CmdExcTxAutomatic_Object = MibTableColumn
cmdExcTxAutomatic = _CmdExcTxAutomatic_Object(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 4, 1, 1, 1, 38),
    _CmdExcTxAutomatic_Type()
)
cmdExcTxAutomatic.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmdExcTxAutomatic.setStatus("current")
_CmdExcInputAutoSwitch_Type = SwitchOnOff
_CmdExcInputAutoSwitch_Object = MibTableColumn
cmdExcInputAutoSwitch = _CmdExcInputAutoSwitch_Object(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 4, 1, 1, 1, 39),
    _CmdExcInputAutoSwitch_Type()
)
cmdExcInputAutoSwitch.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmdExcInputAutoSwitch.setStatus("deprecated")
_CmdExcInputSeamless_Type = SwitchOnOff
_CmdExcInputSeamless_Object = MibTableColumn
cmdExcInputSeamless = _CmdExcInputSeamless_Object(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 4, 1, 1, 1, 40),
    _CmdExcInputSeamless_Type()
)
cmdExcInputSeamless.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmdExcInputSeamless.setStatus("current")


class _CmdExcInputPriority_Type(Integer32):
    """Custom type cmdExcInputPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("equal", 1),
          ("prior", 2))
    )


_CmdExcInputPriority_Type.__name__ = "Integer32"
_CmdExcInputPriority_Object = MibTableColumn
cmdExcInputPriority = _CmdExcInputPriority_Object(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 4, 1, 1, 1, 41),
    _CmdExcInputPriority_Type()
)
cmdExcInputPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmdExcInputPriority.setStatus("current")


class _CmdExcInputCheckTimeForward_Type(Integer32):
    """Custom type cmdExcInputCheckTimeForward based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 600),
    )


_CmdExcInputCheckTimeForward_Type.__name__ = "Integer32"
_CmdExcInputCheckTimeForward_Object = MibTableColumn
cmdExcInputCheckTimeForward = _CmdExcInputCheckTimeForward_Object(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 4, 1, 1, 1, 42),
    _CmdExcInputCheckTimeForward_Type()
)
cmdExcInputCheckTimeForward.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmdExcInputCheckTimeForward.setStatus("current")
if mibBuilder.loadTexts:
    cmdExcInputCheckTimeForward.setUnits("seconds")


class _CmdExcInputCheckTimeSwitchback_Type(Integer32):
    """Custom type cmdExcInputCheckTimeSwitchback based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 600),
    )


_CmdExcInputCheckTimeSwitchback_Type.__name__ = "Integer32"
_CmdExcInputCheckTimeSwitchback_Object = MibTableColumn
cmdExcInputCheckTimeSwitchback = _CmdExcInputCheckTimeSwitchback_Object(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 4, 1, 1, 1, 43),
    _CmdExcInputCheckTimeSwitchback_Type()
)
cmdExcInputCheckTimeSwitchback.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmdExcInputCheckTimeSwitchback.setStatus("current")
if mibBuilder.loadTexts:
    cmdExcInputCheckTimeSwitchback.setUnits("seconds")


class _CmdExcInputMuteOnFail_Type(Integer32):
    """Custom type cmdExcInputMuteOnFail based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("mute", 1),
          ("noMute", 2))
    )


_CmdExcInputMuteOnFail_Type.__name__ = "Integer32"
_CmdExcInputMuteOnFail_Object = MibTableColumn
cmdExcInputMuteOnFail = _CmdExcInputMuteOnFail_Object(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 4, 1, 1, 1, 44),
    _CmdExcInputMuteOnFail_Type()
)
cmdExcInputMuteOnFail.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmdExcInputMuteOnFail.setStatus("current")


class _CmdExcInputManualPreseletionHP1_Type(Integer32):
    """Custom type cmdExcInputManualPreseletionHP1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("auto", 1),
          ("asi", 2),
          ("smpte", 3))
    )


_CmdExcInputManualPreseletionHP1_Type.__name__ = "Integer32"
_CmdExcInputManualPreseletionHP1_Object = MibTableColumn
cmdExcInputManualPreseletionHP1 = _CmdExcInputManualPreseletionHP1_Object(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 4, 1, 1, 1, 45),
    _CmdExcInputManualPreseletionHP1_Type()
)
cmdExcInputManualPreseletionHP1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmdExcInputManualPreseletionHP1.setStatus("current")


class _CmdExcInputManualPreseletionHP2_Type(Integer32):
    """Custom type cmdExcInputManualPreseletionHP2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("auto", 1),
          ("asi", 2),
          ("smpte", 3))
    )


_CmdExcInputManualPreseletionHP2_Type.__name__ = "Integer32"
_CmdExcInputManualPreseletionHP2_Object = MibTableColumn
cmdExcInputManualPreseletionHP2 = _CmdExcInputManualPreseletionHP2_Object(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 4, 1, 1, 1, 46),
    _CmdExcInputManualPreseletionHP2_Type()
)
cmdExcInputManualPreseletionHP2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmdExcInputManualPreseletionHP2.setStatus("current")


class _CmdExcInputManualPreseletionLP1_Type(Integer32):
    """Custom type cmdExcInputManualPreseletionLP1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("auto", 1),
          ("asi", 2),
          ("smpte", 3))
    )


_CmdExcInputManualPreseletionLP1_Type.__name__ = "Integer32"
_CmdExcInputManualPreseletionLP1_Object = MibTableColumn
cmdExcInputManualPreseletionLP1 = _CmdExcInputManualPreseletionLP1_Object(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 4, 1, 1, 1, 47),
    _CmdExcInputManualPreseletionLP1_Type()
)
cmdExcInputManualPreseletionLP1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmdExcInputManualPreseletionLP1.setStatus("current")


class _CmdExcInputManualPreseletionLP2_Type(Integer32):
    """Custom type cmdExcInputManualPreseletionLP2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("auto", 1),
          ("asi", 2),
          ("smpte", 3))
    )


_CmdExcInputManualPreseletionLP2_Type.__name__ = "Integer32"
_CmdExcInputManualPreseletionLP2_Object = MibTableColumn
cmdExcInputManualPreseletionLP2 = _CmdExcInputManualPreseletionLP2_Object(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 4, 1, 1, 1, 48),
    _CmdExcInputManualPreseletionLP2_Type()
)
cmdExcInputManualPreseletionLP2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmdExcInputManualPreseletionLP2.setStatus("current")


class _CmdExcTPSManualBandwidth_Type(Integer32):
    """Custom type cmdExcTPSManualBandwidth based on Integer32"""
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
        *(("mhz5", 1),
          ("mhz6", 2),
          ("mhz7", 3),
          ("mhz8", 4))
    )


_CmdExcTPSManualBandwidth_Type.__name__ = "Integer32"
_CmdExcTPSManualBandwidth_Object = MibTableColumn
cmdExcTPSManualBandwidth = _CmdExcTPSManualBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 4, 1, 1, 1, 49),
    _CmdExcTPSManualBandwidth_Type()
)
cmdExcTPSManualBandwidth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmdExcTPSManualBandwidth.setStatus("current")


class _CmdExcTPSManualFFTLength_Type(Integer32):
    """Custom type cmdExcTPSManualFFTLength based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("k2", 1),
          ("k8", 2),
          ("k4", 3))
    )


_CmdExcTPSManualFFTLength_Type.__name__ = "Integer32"
_CmdExcTPSManualFFTLength_Object = MibTableColumn
cmdExcTPSManualFFTLength = _CmdExcTPSManualFFTLength_Object(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 4, 1, 1, 1, 50),
    _CmdExcTPSManualFFTLength_Type()
)
cmdExcTPSManualFFTLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmdExcTPSManualFFTLength.setStatus("current")


class _CmdExcTPSManualGuardInterval_Type(Integer32):
    """Custom type cmdExcTPSManualGuardInterval based on Integer32"""
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
        *(("oneOf32", 1),
          ("oneOf16", 2),
          ("oneOf8", 3),
          ("oneOf4", 4))
    )


_CmdExcTPSManualGuardInterval_Type.__name__ = "Integer32"
_CmdExcTPSManualGuardInterval_Object = MibTableColumn
cmdExcTPSManualGuardInterval = _CmdExcTPSManualGuardInterval_Object(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 4, 1, 1, 1, 51),
    _CmdExcTPSManualGuardInterval_Type()
)
cmdExcTPSManualGuardInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmdExcTPSManualGuardInterval.setStatus("current")


class _CmdExcTPSManualConstellation_Type(Integer32):
    """Custom type cmdExcTPSManualConstellation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("qpsk", 1),
          ("qam16", 2),
          ("qam64", 3))
    )


_CmdExcTPSManualConstellation_Type.__name__ = "Integer32"
_CmdExcTPSManualConstellation_Object = MibTableColumn
cmdExcTPSManualConstellation = _CmdExcTPSManualConstellation_Object(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 4, 1, 1, 1, 52),
    _CmdExcTPSManualConstellation_Type()
)
cmdExcTPSManualConstellation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmdExcTPSManualConstellation.setStatus("current")


class _CmdExcTPSManualAlpha_Type(Integer32):
    """Custom type cmdExcTPSManualAlpha based on Integer32"""
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
        *(("noHierarchy", 1),
          ("one", 2),
          ("two", 3),
          ("four", 4))
    )


_CmdExcTPSManualAlpha_Type.__name__ = "Integer32"
_CmdExcTPSManualAlpha_Object = MibTableColumn
cmdExcTPSManualAlpha = _CmdExcTPSManualAlpha_Object(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 4, 1, 1, 1, 53),
    _CmdExcTPSManualAlpha_Type()
)
cmdExcTPSManualAlpha.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmdExcTPSManualAlpha.setStatus("obsolete")


class _CmdExcTPSManualCellID_Type(Integer32):
    """Custom type cmdExcTPSManualCellID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CmdExcTPSManualCellID_Type.__name__ = "Integer32"
_CmdExcTPSManualCellID_Object = MibTableColumn
cmdExcTPSManualCellID = _CmdExcTPSManualCellID_Object(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 4, 1, 1, 1, 54),
    _CmdExcTPSManualCellID_Type()
)
cmdExcTPSManualCellID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmdExcTPSManualCellID.setStatus("current")


class _CmdExcTPSManualInterleaver_Type(Integer32):
    """Custom type cmdExcTPSManualInterleaver based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("indepth", 1),
          ("nat", 2))
    )


_CmdExcTPSManualInterleaver_Type.__name__ = "Integer32"
_CmdExcTPSManualInterleaver_Object = MibTableColumn
cmdExcTPSManualInterleaver = _CmdExcTPSManualInterleaver_Object(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 4, 1, 1, 1, 55),
    _CmdExcTPSManualInterleaver_Type()
)
cmdExcTPSManualInterleaver.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmdExcTPSManualInterleaver.setStatus("current")


class _CmdExcTPSManualCoderateHP_Type(Integer32):
    """Custom type cmdExcTPSManualCoderateHP based on Integer32"""
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
        *(("oneOf2", 1),
          ("twoOf3", 2),
          ("threeOf4", 3),
          ("fiveOf6", 4),
          ("sevenOf8", 5))
    )


_CmdExcTPSManualCoderateHP_Type.__name__ = "Integer32"
_CmdExcTPSManualCoderateHP_Object = MibTableColumn
cmdExcTPSManualCoderateHP = _CmdExcTPSManualCoderateHP_Object(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 4, 1, 1, 1, 56),
    _CmdExcTPSManualCoderateHP_Type()
)
cmdExcTPSManualCoderateHP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmdExcTPSManualCoderateHP.setStatus("current")


class _CmdExcTPSManualCoderateLP_Type(Integer32):
    """Custom type cmdExcTPSManualCoderateLP based on Integer32"""
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
        *(("oneOf2", 1),
          ("twoOf3", 2),
          ("threeOf4", 3),
          ("fiveOf6", 4),
          ("sevenOf8", 5))
    )


_CmdExcTPSManualCoderateLP_Type.__name__ = "Integer32"
_CmdExcTPSManualCoderateLP_Object = MibTableColumn
cmdExcTPSManualCoderateLP = _CmdExcTPSManualCoderateLP_Object(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 4, 1, 1, 1, 57),
    _CmdExcTPSManualCoderateLP_Type()
)
cmdExcTPSManualCoderateLP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmdExcTPSManualCoderateLP.setStatus("current")
_CmdExcTPSManualTimeSlicingHP_Type = SwitchOnOff
_CmdExcTPSManualTimeSlicingHP_Object = MibTableColumn
cmdExcTPSManualTimeSlicingHP = _CmdExcTPSManualTimeSlicingHP_Object(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 4, 1, 1, 1, 58),
    _CmdExcTPSManualTimeSlicingHP_Type()
)
cmdExcTPSManualTimeSlicingHP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmdExcTPSManualTimeSlicingHP.setStatus("current")
_CmdExcTPSManualTimeSlicingLP_Type = SwitchOnOff
_CmdExcTPSManualTimeSlicingLP_Object = MibTableColumn
cmdExcTPSManualTimeSlicingLP = _CmdExcTPSManualTimeSlicingLP_Object(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 4, 1, 1, 1, 59),
    _CmdExcTPSManualTimeSlicingLP_Type()
)
cmdExcTPSManualTimeSlicingLP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmdExcTPSManualTimeSlicingLP.setStatus("current")
_CmdExcTPSManualFECHP_Type = SwitchOnOff
_CmdExcTPSManualFECHP_Object = MibTableColumn
cmdExcTPSManualFECHP = _CmdExcTPSManualFECHP_Object(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 4, 1, 1, 1, 60),
    _CmdExcTPSManualFECHP_Type()
)
cmdExcTPSManualFECHP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmdExcTPSManualFECHP.setStatus("current")
_CmdExcTPSManualFECLP_Type = SwitchOnOff
_CmdExcTPSManualFECLP_Object = MibTableColumn
cmdExcTPSManualFECLP = _CmdExcTPSManualFECLP_Object(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 4, 1, 1, 1, 61),
    _CmdExcTPSManualFECLP_Type()
)
cmdExcTPSManualFECLP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmdExcTPSManualFECLP.setStatus("current")
_CmdExcSFNStaticDelay_Type = FloatingPoint
_CmdExcSFNStaticDelay_Object = MibTableColumn
cmdExcSFNStaticDelay = _CmdExcSFNStaticDelay_Object(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 4, 1, 1, 1, 62),
    _CmdExcSFNStaticDelay_Type()
)
cmdExcSFNStaticDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmdExcSFNStaticDelay.setStatus("current")
if mibBuilder.loadTexts:
    cmdExcSFNStaticDelay.setUnits("Microseconds")


class _CmdExcSFNDeviationTime_Type(Integer32):
    """Custom type cmdExcSFNDeviationTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_CmdExcSFNDeviationTime_Type.__name__ = "Integer32"
_CmdExcSFNDeviationTime_Object = MibTableColumn
cmdExcSFNDeviationTime = _CmdExcSFNDeviationTime_Object(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 4, 1, 1, 1, 63),
    _CmdExcSFNDeviationTime_Type()
)
cmdExcSFNDeviationTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmdExcSFNDeviationTime.setStatus("current")
if mibBuilder.loadTexts:
    cmdExcSFNDeviationTime.setUnits("Microseconds")


class _CmdExcFrequency_Type(Integer32):
    """Custom type cmdExcFrequency based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(47000000, 1500000000),
    )


_CmdExcFrequency_Type.__name__ = "Integer32"
_CmdExcFrequency_Object = MibTableColumn
cmdExcFrequency = _CmdExcFrequency_Object(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 4, 1, 1, 1, 64),
    _CmdExcFrequency_Type()
)
cmdExcFrequency.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmdExcFrequency.setStatus("current")
if mibBuilder.loadTexts:
    cmdExcFrequency.setUnits("Hertz")


class _CmdExcReferenceSource_Type(Integer32):
    """Custom type cmdExcReferenceSource based on Integer32"""
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
        *(("intern", 1),
          ("extern5Mhz", 2),
          ("extern10Mhz", 3),
          ("extern1PPS", 4),
          ("internGPS", 5))
    )


_CmdExcReferenceSource_Type.__name__ = "Integer32"
_CmdExcReferenceSource_Object = MibTableColumn
cmdExcReferenceSource = _CmdExcReferenceSource_Object(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 4, 1, 1, 1, 65),
    _CmdExcReferenceSource_Type()
)
cmdExcReferenceSource.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmdExcReferenceSource.setStatus("current")


class _CmdExcMuteOnPPSFail_Type(Integer32):
    """Custom type cmdExcMuteOnPPSFail based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("onlyAtStartup", 2),
          ("afterFailDelayTime", 3))
    )


_CmdExcMuteOnPPSFail_Type.__name__ = "Integer32"
_CmdExcMuteOnPPSFail_Object = MibTableColumn
cmdExcMuteOnPPSFail = _CmdExcMuteOnPPSFail_Object(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 4, 1, 1, 1, 66),
    _CmdExcMuteOnPPSFail_Type()
)
cmdExcMuteOnPPSFail.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmdExcMuteOnPPSFail.setStatus("current")


class _CmdExcMuteOnReferenceFail_Type(Integer32):
    """Custom type cmdExcMuteOnReferenceFail based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("onlyAtStartup", 2),
          ("afterFailDelayTime", 3))
    )


_CmdExcMuteOnReferenceFail_Type.__name__ = "Integer32"
_CmdExcMuteOnReferenceFail_Object = MibTableColumn
cmdExcMuteOnReferenceFail = _CmdExcMuteOnReferenceFail_Object(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 4, 1, 1, 1, 67),
    _CmdExcMuteOnReferenceFail_Type()
)
cmdExcMuteOnReferenceFail.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmdExcMuteOnReferenceFail.setStatus("current")


class _CmdExcRefFailDelayTime_Type(Integer32):
    """Custom type cmdExcRefFailDelayTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 24),
    )


_CmdExcRefFailDelayTime_Type.__name__ = "Integer32"
_CmdExcRefFailDelayTime_Object = MibTableColumn
cmdExcRefFailDelayTime = _CmdExcRefFailDelayTime_Object(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 4, 1, 1, 1, 68),
    _CmdExcRefFailDelayTime_Type()
)
cmdExcRefFailDelayTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmdExcRefFailDelayTime.setStatus("current")
if mibBuilder.loadTexts:
    cmdExcRefFailDelayTime.setUnits("Hours")


class _CmdExcTypeLossOfInput_Type(Integer32):
    """Custom type cmdExcTypeLossOfInput based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("warning", 1),
          ("fault", 2))
    )


_CmdExcTypeLossOfInput_Type.__name__ = "Integer32"
_CmdExcTypeLossOfInput_Object = MibTableColumn
cmdExcTypeLossOfInput = _CmdExcTypeLossOfInput_Object(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 4, 1, 1, 1, 69),
    _CmdExcTypeLossOfInput_Type()
)
cmdExcTypeLossOfInput.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmdExcTypeLossOfInput.setStatus("current")
_CmdExcRfOutput_Type = SwitchOnOff
_CmdExcRfOutput_Object = MibTableColumn
cmdExcRfOutput = _CmdExcRfOutput_Object(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 4, 1, 1, 1, 70),
    _CmdExcRfOutput_Type()
)
cmdExcRfOutput.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmdExcRfOutput.setStatus("current")
_CmdExcRfOutputRegulation_Type = SwitchOnOff
_CmdExcRfOutputRegulation_Object = MibTableColumn
cmdExcRfOutputRegulation = _CmdExcRfOutputRegulation_Object(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 4, 1, 1, 1, 71),
    _CmdExcRfOutputRegulation_Type()
)
cmdExcRfOutputRegulation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmdExcRfOutputRegulation.setStatus("current")
_CmdExcRfOutputManualRfLevel_Type = FloatingPoint
_CmdExcRfOutputManualRfLevel_Object = MibTableColumn
cmdExcRfOutputManualRfLevel = _CmdExcRfOutputManualRfLevel_Object(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 4, 1, 1, 1, 72),
    _CmdExcRfOutputManualRfLevel_Type()
)
cmdExcRfOutputManualRfLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmdExcRfOutputManualRfLevel.setStatus("current")
if mibBuilder.loadTexts:
    cmdExcRfOutputManualRfLevel.setUnits("Percent")


class _CmdExcRfOutputAttenuation_Type(Integer32):
    """Custom type cmdExcRfOutputAttenuation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 9),
    )


_CmdExcRfOutputAttenuation_Type.__name__ = "Integer32"
_CmdExcRfOutputAttenuation_Object = MibTableColumn
cmdExcRfOutputAttenuation = _CmdExcRfOutputAttenuation_Object(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 4, 1, 1, 1, 73),
    _CmdExcRfOutputAttenuation_Type()
)
cmdExcRfOutputAttenuation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmdExcRfOutputAttenuation.setStatus("current")
if mibBuilder.loadTexts:
    cmdExcRfOutputAttenuation.setUnits("dB")
_CmdExcRfOutputRfSlope_Type = FloatingPoint
_CmdExcRfOutputRfSlope_Object = MibTableColumn
cmdExcRfOutputRfSlope = _CmdExcRfOutputRfSlope_Object(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 4, 1, 1, 1, 74),
    _CmdExcRfOutputRfSlope_Type()
)
cmdExcRfOutputRfSlope.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmdExcRfOutputRfSlope.setStatus("current")
if mibBuilder.loadTexts:
    cmdExcRfOutputRfSlope.setUnits("Percent")
_CmdExcRfOutputModulationSlope_Type = FloatingPoint
_CmdExcRfOutputModulationSlope_Object = MibTableColumn
cmdExcRfOutputModulationSlope = _CmdExcRfOutputModulationSlope_Object(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 4, 1, 1, 1, 75),
    _CmdExcRfOutputModulationSlope_Type()
)
cmdExcRfOutputModulationSlope.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmdExcRfOutputModulationSlope.setStatus("current")
if mibBuilder.loadTexts:
    cmdExcRfOutputModulationSlope.setUnits("Percent")


class _CmdExcRfIqAdjustStart_Type(Integer32):
    """Custom type cmdExcRfIqAdjustStart based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("break", 1),
          ("start", 2))
    )


_CmdExcRfIqAdjustStart_Type.__name__ = "Integer32"
_CmdExcRfIqAdjustStart_Object = MibTableColumn
cmdExcRfIqAdjustStart = _CmdExcRfIqAdjustStart_Object(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 4, 1, 1, 1, 77),
    _CmdExcRfIqAdjustStart_Type()
)
cmdExcRfIqAdjustStart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmdExcRfIqAdjustStart.setStatus("current")
_CmdExcRfIqAdjustTestsignal_Type = SwitchOnOff
_CmdExcRfIqAdjustTestsignal_Object = MibTableColumn
cmdExcRfIqAdjustTestsignal = _CmdExcRfIqAdjustTestsignal_Object(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 4, 1, 1, 1, 78),
    _CmdExcRfIqAdjustTestsignal_Type()
)
cmdExcRfIqAdjustTestsignal.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmdExcRfIqAdjustTestsignal.setStatus("current")


class _CmdExcRfIqAdjustBiasCoarseI_Type(Integer32):
    """Custom type cmdExcRfIqAdjustBiasCoarseI based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1023, 1023),
    )


_CmdExcRfIqAdjustBiasCoarseI_Type.__name__ = "Integer32"
_CmdExcRfIqAdjustBiasCoarseI_Object = MibTableColumn
cmdExcRfIqAdjustBiasCoarseI = _CmdExcRfIqAdjustBiasCoarseI_Object(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 4, 1, 1, 1, 79),
    _CmdExcRfIqAdjustBiasCoarseI_Type()
)
cmdExcRfIqAdjustBiasCoarseI.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmdExcRfIqAdjustBiasCoarseI.setStatus("current")


class _CmdExcRfIqAdjustBiasCoarseQ_Type(Integer32):
    """Custom type cmdExcRfIqAdjustBiasCoarseQ based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1023, 1023),
    )


_CmdExcRfIqAdjustBiasCoarseQ_Type.__name__ = "Integer32"
_CmdExcRfIqAdjustBiasCoarseQ_Object = MibTableColumn
cmdExcRfIqAdjustBiasCoarseQ = _CmdExcRfIqAdjustBiasCoarseQ_Object(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 4, 1, 1, 1, 80),
    _CmdExcRfIqAdjustBiasCoarseQ_Type()
)
cmdExcRfIqAdjustBiasCoarseQ.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmdExcRfIqAdjustBiasCoarseQ.setStatus("current")


class _CmdExcRfIqAdjustBiasFineI_Type(Integer32):
    """Custom type cmdExcRfIqAdjustBiasFineI based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-32767, 32767),
    )


_CmdExcRfIqAdjustBiasFineI_Type.__name__ = "Integer32"
_CmdExcRfIqAdjustBiasFineI_Object = MibTableColumn
cmdExcRfIqAdjustBiasFineI = _CmdExcRfIqAdjustBiasFineI_Object(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 4, 1, 1, 1, 81),
    _CmdExcRfIqAdjustBiasFineI_Type()
)
cmdExcRfIqAdjustBiasFineI.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmdExcRfIqAdjustBiasFineI.setStatus("current")


class _CmdExcRfIqAdjustBiasFineQ_Type(Integer32):
    """Custom type cmdExcRfIqAdjustBiasFineQ based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-32767, 32767),
    )


_CmdExcRfIqAdjustBiasFineQ_Type.__name__ = "Integer32"
_CmdExcRfIqAdjustBiasFineQ_Object = MibTableColumn
cmdExcRfIqAdjustBiasFineQ = _CmdExcRfIqAdjustBiasFineQ_Object(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 4, 1, 1, 1, 82),
    _CmdExcRfIqAdjustBiasFineQ_Type()
)
cmdExcRfIqAdjustBiasFineQ.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmdExcRfIqAdjustBiasFineQ.setStatus("current")


class _CmdExcRfIqAdjustGainI_Type(Integer32):
    """Custom type cmdExcRfIqAdjustGainI based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CmdExcRfIqAdjustGainI_Type.__name__ = "Integer32"
_CmdExcRfIqAdjustGainI_Object = MibTableColumn
cmdExcRfIqAdjustGainI = _CmdExcRfIqAdjustGainI_Object(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 4, 1, 1, 1, 83),
    _CmdExcRfIqAdjustGainI_Type()
)
cmdExcRfIqAdjustGainI.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmdExcRfIqAdjustGainI.setStatus("current")


class _CmdExcRfIqAdjustGainQ_Type(Integer32):
    """Custom type cmdExcRfIqAdjustGainQ based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CmdExcRfIqAdjustGainQ_Type.__name__ = "Integer32"
_CmdExcRfIqAdjustGainQ_Object = MibTableColumn
cmdExcRfIqAdjustGainQ = _CmdExcRfIqAdjustGainQ_Object(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 4, 1, 1, 1, 84),
    _CmdExcRfIqAdjustGainQ_Type()
)
cmdExcRfIqAdjustGainQ.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmdExcRfIqAdjustGainQ.setStatus("current")
_CmdExcRfIqAdjustPhase_Type = FloatingPoint
_CmdExcRfIqAdjustPhase_Object = MibTableColumn
cmdExcRfIqAdjustPhase = _CmdExcRfIqAdjustPhase_Object(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 4, 1, 1, 1, 85),
    _CmdExcRfIqAdjustPhase_Type()
)
cmdExcRfIqAdjustPhase.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmdExcRfIqAdjustPhase.setStatus("current")
_CmdExcInput1Source_Type = InputSource
_CmdExcInput1Source_Object = MibTableColumn
cmdExcInput1Source = _CmdExcInput1Source_Object(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 4, 1, 1, 1, 86),
    _CmdExcInput1Source_Type()
)
cmdExcInput1Source.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmdExcInput1Source.setStatus("current")
_CmdExcInput2Source_Type = InputSource
_CmdExcInput2Source_Object = MibTableColumn
cmdExcInput2Source = _CmdExcInput2Source_Object(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 4, 1, 1, 1, 87),
    _CmdExcInput2Source_Type()
)
cmdExcInput2Source.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmdExcInput2Source.setStatus("current")
_CmdExcInpAutoReadyAfterChangeOv_Type = SwitchOnOff
_CmdExcInpAutoReadyAfterChangeOv_Object = MibTableColumn
cmdExcInpAutoReadyAfterChangeOv = _CmdExcInpAutoReadyAfterChangeOv_Object(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 4, 1, 1, 1, 88),
    _CmdExcInpAutoReadyAfterChangeOv_Type()
)
cmdExcInpAutoReadyAfterChangeOv.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmdExcInpAutoReadyAfterChangeOv.setStatus("current")


class _CmdExcInputFailDelayTime_Type(Integer32):
    """Custom type cmdExcInputFailDelayTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 600),
    )


_CmdExcInputFailDelayTime_Type.__name__ = "Integer32"
_CmdExcInputFailDelayTime_Object = MibTableColumn
cmdExcInputFailDelayTime = _CmdExcInputFailDelayTime_Object(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 4, 1, 1, 1, 89),
    _CmdExcInputFailDelayTime_Type()
)
cmdExcInputFailDelayTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmdExcInputFailDelayTime.setStatus("current")
if mibBuilder.loadTexts:
    cmdExcInputFailDelayTime.setUnits("Seconds")


class _CmdExcTransmitterType_Type(Integer32):
    """Custom type cmdExcTransmitterType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("atv", 1),
          ("dvb", 2),
          ("atsc", 3))
    )


_CmdExcTransmitterType_Type.__name__ = "Integer32"
_CmdExcTransmitterType_Object = MibTableColumn
cmdExcTransmitterType = _CmdExcTransmitterType_Object(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 4, 1, 1, 1, 90),
    _CmdExcTransmitterType_Type()
)
cmdExcTransmitterType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmdExcTransmitterType.setStatus("current")
_CmdExcTimeScheduler_Type = SwitchOnOff
_CmdExcTimeScheduler_Object = MibTableColumn
cmdExcTimeScheduler = _CmdExcTimeScheduler_Object(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 4, 1, 1, 1, 91),
    _CmdExcTimeScheduler_Type()
)
cmdExcTimeScheduler.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmdExcTimeScheduler.setStatus("current")


class _CmdExcMuteCondition_Type(Integer32):
    """Custom type cmdExcMuteCondition based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("onAllFaults", 1),
          ("notBeforeSyncLoss", 2))
    )


_CmdExcMuteCondition_Type.__name__ = "Integer32"
_CmdExcMuteCondition_Object = MibTableColumn
cmdExcMuteCondition = _CmdExcMuteCondition_Object(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 4, 1, 1, 1, 92),
    _CmdExcMuteCondition_Type()
)
cmdExcMuteCondition.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmdExcMuteCondition.setStatus("current")
_CmdExcRfWarningLimit_Type = FloatingPoint
_CmdExcRfWarningLimit_Object = MibTableColumn
cmdExcRfWarningLimit = _CmdExcRfWarningLimit_Object(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 4, 1, 1, 1, 97),
    _CmdExcRfWarningLimit_Type()
)
cmdExcRfWarningLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmdExcRfWarningLimit.setStatus("current")
if mibBuilder.loadTexts:
    cmdExcRfWarningLimit.setUnits("dB")
_CmdExcRfFailLimit_Type = FloatingPoint
_CmdExcRfFailLimit_Object = MibTableColumn
cmdExcRfFailLimit = _CmdExcRfFailLimit_Object(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 4, 1, 1, 1, 98),
    _CmdExcRfFailLimit_Type()
)
cmdExcRfFailLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmdExcRfFailLimit.setStatus("current")
if mibBuilder.loadTexts:
    cmdExcRfFailLimit.setUnits("dB")
_CmdExcOutputPower_Type = FloatingPoint
_CmdExcOutputPower_Object = MibTableColumn
cmdExcOutputPower = _CmdExcOutputPower_Object(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 4, 1, 1, 1, 99),
    _CmdExcOutputPower_Type()
)
cmdExcOutputPower.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmdExcOutputPower.setStatus("current")
if mibBuilder.loadTexts:
    cmdExcOutputPower.setUnits("W")
_CmdOstRefVoltageVision_Type = FloatingPoint
_CmdOstRefVoltageVision_Object = MibTableColumn
cmdOstRefVoltageVision = _CmdOstRefVoltageVision_Object(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 4, 1, 1, 1, 100),
    _CmdOstRefVoltageVision_Type()
)
cmdOstRefVoltageVision.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmdOstRefVoltageVision.setStatus("current")
if mibBuilder.loadTexts:
    cmdOstRefVoltageVision.setUnits("Percent")


class _CmdOstMaxOutletTempThreshold_Type(Integer32):
    """Custom type cmdOstMaxOutletTempThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(45, 65),
    )


_CmdOstMaxOutletTempThreshold_Type.__name__ = "Integer32"
_CmdOstMaxOutletTempThreshold_Object = MibTableColumn
cmdOstMaxOutletTempThreshold = _CmdOstMaxOutletTempThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 4, 1, 1, 1, 101),
    _CmdOstMaxOutletTempThreshold_Type()
)
cmdOstMaxOutletTempThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmdOstMaxOutletTempThreshold.setStatus("current")
if mibBuilder.loadTexts:
    cmdOstMaxOutletTempThreshold.setUnits("Degree Celsius")


class _CmdExcMonitoringOutput_Type(Integer32):
    """Custom type cmdExcMonitoringOutput based on Integer32"""
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
        *(("off", 1),
          ("reference10MHz", 2),
          ("generated1PPS", 3),
          ("kHz1", 4),
          ("pulse1PPS", 5))
    )


_CmdExcMonitoringOutput_Type.__name__ = "Integer32"
_CmdExcMonitoringOutput_Object = MibTableColumn
cmdExcMonitoringOutput = _CmdExcMonitoringOutput_Object(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 4, 1, 1, 1, 110),
    _CmdExcMonitoringOutput_Type()
)
cmdExcMonitoringOutput.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmdExcMonitoringOutput.setStatus("current")


class _CmdExcOcxoAdjust_Type(Integer32):
    """Custom type cmdExcOcxoAdjust based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CmdExcOcxoAdjust_Type.__name__ = "Integer32"
_CmdExcOcxoAdjust_Object = MibTableColumn
cmdExcOcxoAdjust = _CmdExcOcxoAdjust_Object(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 4, 1, 1, 1, 111),
    _CmdExcOcxoAdjust_Type()
)
cmdExcOcxoAdjust.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmdExcOcxoAdjust.setStatus("current")
_CmdExcExpectInputReserve_Type = SwitchOnOff
_CmdExcExpectInputReserve_Object = MibTableColumn
cmdExcExpectInputReserve = _CmdExcExpectInputReserve_Object(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 4, 1, 1, 1, 112),
    _CmdExcExpectInputReserve_Type()
)
cmdExcExpectInputReserve.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmdExcExpectInputReserve.setStatus("current")
_CmdExcEnablePcrReset_Type = SwitchOnOff
_CmdExcEnablePcrReset_Object = MibTableColumn
cmdExcEnablePcrReset = _CmdExcEnablePcrReset_Object(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 4, 1, 1, 1, 113),
    _CmdExcEnablePcrReset_Type()
)
cmdExcEnablePcrReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmdExcEnablePcrReset.setStatus("obsolete")
_CmdExcTimeForDailyPcrReset_Type = TimeOfDay
_CmdExcTimeForDailyPcrReset_Object = MibTableColumn
cmdExcTimeForDailyPcrReset = _CmdExcTimeForDailyPcrReset_Object(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 4, 1, 1, 1, 114),
    _CmdExcTimeForDailyPcrReset_Type()
)
cmdExcTimeForDailyPcrReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmdExcTimeForDailyPcrReset.setStatus("obsolete")
_CmdExcFailDelayMode_Type = FailDelayMode
_CmdExcFailDelayMode_Object = MibTableColumn
cmdExcFailDelayMode = _CmdExcFailDelayMode_Object(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 4, 1, 1, 1, 115),
    _CmdExcFailDelayMode_Type()
)
cmdExcFailDelayMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmdExcFailDelayMode.setStatus("current")
_SummaryInfo_ObjectIdentity = ObjectIdentity
summaryInfo = _SummaryInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 4, 1, 2)
)
_SummaryFaultTx_Type = TruthValue
_SummaryFaultTx_Object = MibScalar
summaryFaultTx = _SummaryFaultTx_Object(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 4, 1, 2, 1),
    _SummaryFaultTx_Type()
)
summaryFaultTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    summaryFaultTx.setStatus("current")
_SummaryWarningTx_Type = TruthValue
_SummaryWarningTx_Object = MibScalar
summaryWarningTx = _SummaryWarningTx_Object(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 4, 1, 2, 2),
    _SummaryWarningTx_Type()
)
summaryWarningTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    summaryWarningTx.setStatus("current")
_LocalModeTx_Type = TruthValue
_LocalModeTx_Object = MibScalar
localModeTx = _LocalModeTx_Object(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 4, 1, 2, 3),
    _LocalModeTx_Type()
)
localModeTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    localModeTx.setStatus("current")
_RfOnTx_Type = TruthValue
_RfOnTx_Object = MibScalar
rfOnTx = _RfOnTx_Object(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 4, 1, 2, 4),
    _RfOnTx_Type()
)
rfOnTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rfOnTx.setStatus("current")
_ForwardPower_Type = FloatingPoint
_ForwardPower_Object = MibScalar
forwardPower = _ForwardPower_Object(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 4, 1, 2, 5),
    _ForwardPower_Type()
)
forwardPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    forwardPower.setStatus("current")
if mibBuilder.loadTexts:
    forwardPower.setUnits("Watt")
_ReflectedPower_Type = FloatingPoint
_ReflectedPower_Object = MibScalar
reflectedPower = _ReflectedPower_Object(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 4, 1, 2, 6),
    _ReflectedPower_Type()
)
reflectedPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    reflectedPower.setStatus("current")
if mibBuilder.loadTexts:
    reflectedPower.setUnits("Watt")
_SummaryFaultExcA_Type = TruthValue
_SummaryFaultExcA_Object = MibScalar
summaryFaultExcA = _SummaryFaultExcA_Object(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 4, 1, 2, 7),
    _SummaryFaultExcA_Type()
)
summaryFaultExcA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    summaryFaultExcA.setStatus("current")
_SummaryFaultOstA_Type = TruthValue
_SummaryFaultOstA_Object = MibScalar
summaryFaultOstA = _SummaryFaultOstA_Object(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 4, 1, 2, 8),
    _SummaryFaultOstA_Type()
)
summaryFaultOstA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    summaryFaultOstA.setStatus("current")
_SummaryFaultExcB_Type = TruthValue
_SummaryFaultExcB_Object = MibScalar
summaryFaultExcB = _SummaryFaultExcB_Object(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 4, 1, 2, 9),
    _SummaryFaultExcB_Type()
)
summaryFaultExcB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    summaryFaultExcB.setStatus("current")
_SummaryFaultOstB_Type = TruthValue
_SummaryFaultOstB_Object = MibScalar
summaryFaultOstB = _SummaryFaultOstB_Object(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 4, 1, 2, 10),
    _SummaryFaultOstB_Type()
)
summaryFaultOstB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    summaryFaultOstB.setStatus("current")
_ExciterAutomaticReady_Type = TruthValue
_ExciterAutomaticReady_Object = MibScalar
exciterAutomaticReady = _ExciterAutomaticReady_Object(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 4, 1, 2, 11),
    _ExciterAutomaticReady_Type()
)
exciterAutomaticReady.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exciterAutomaticReady.setStatus("current")
_ExciterAutomaticChanged_Type = TruthValue
_ExciterAutomaticChanged_Object = MibScalar
exciterAutomaticChanged = _ExciterAutomaticChanged_Object(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 4, 1, 2, 12),
    _ExciterAutomaticChanged_Type()
)
exciterAutomaticChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exciterAutomaticChanged.setStatus("current")
_ExciterAutomaticFault_Type = TruthValue
_ExciterAutomaticFault_Object = MibScalar
exciterAutomaticFault = _ExciterAutomaticFault_Object(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 4, 1, 2, 13),
    _ExciterAutomaticFault_Type()
)
exciterAutomaticFault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exciterAutomaticFault.setStatus("current")
_OutputstageAutomaticReady_Type = TruthValue
_OutputstageAutomaticReady_Object = MibScalar
outputstageAutomaticReady = _OutputstageAutomaticReady_Object(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 4, 1, 2, 14),
    _OutputstageAutomaticReady_Type()
)
outputstageAutomaticReady.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outputstageAutomaticReady.setStatus("current")
_OutputstageAutomaticChanged_Type = TruthValue
_OutputstageAutomaticChanged_Object = MibScalar
outputstageAutomaticChanged = _OutputstageAutomaticChanged_Object(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 4, 1, 2, 15),
    _OutputstageAutomaticChanged_Type()
)
outputstageAutomaticChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outputstageAutomaticChanged.setStatus("current")
_OutputstageAutomaticFault_Type = TruthValue
_OutputstageAutomaticFault_Object = MibScalar
outputstageAutomaticFault = _OutputstageAutomaticFault_Object(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 4, 1, 2, 16),
    _OutputstageAutomaticFault_Type()
)
outputstageAutomaticFault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outputstageAutomaticFault.setStatus("current")
_NoConnectionExcA_Type = TruthValue
_NoConnectionExcA_Object = MibScalar
noConnectionExcA = _NoConnectionExcA_Object(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 4, 1, 2, 17),
    _NoConnectionExcA_Type()
)
noConnectionExcA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    noConnectionExcA.setStatus("current")
_NoConnectionOstA_Type = TruthValue
_NoConnectionOstA_Object = MibScalar
noConnectionOstA = _NoConnectionOstA_Object(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 4, 1, 2, 18),
    _NoConnectionOstA_Type()
)
noConnectionOstA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    noConnectionOstA.setStatus("current")
_NoConnectionExcB_Type = TruthValue
_NoConnectionExcB_Object = MibScalar
noConnectionExcB = _NoConnectionExcB_Object(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 4, 1, 2, 19),
    _NoConnectionExcB_Type()
)
noConnectionExcB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    noConnectionExcB.setStatus("current")
_NoConnectionOstB_Type = TruthValue
_NoConnectionOstB_Object = MibScalar
noConnectionOstB = _NoConnectionOstB_Object(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 4, 1, 2, 20),
    _NoConnectionOstB_Type()
)
noConnectionOstB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    noConnectionOstB.setStatus("current")
_ActiveExcA_Type = TruthValue
_ActiveExcA_Object = MibScalar
activeExcA = _ActiveExcA_Object(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 4, 1, 2, 21),
    _ActiveExcA_Type()
)
activeExcA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    activeExcA.setStatus("current")
_ActiveOstA_Type = TruthValue
_ActiveOstA_Object = MibScalar
activeOstA = _ActiveOstA_Object(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 4, 1, 2, 22),
    _ActiveOstA_Type()
)
activeOstA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    activeOstA.setStatus("current")
_ActiveExcB_Type = TruthValue
_ActiveExcB_Object = MibScalar
activeExcB = _ActiveExcB_Object(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 4, 1, 2, 23),
    _ActiveExcB_Type()
)
activeExcB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    activeExcB.setStatus("current")
_ActiveOstB_Type = TruthValue
_ActiveOstB_Object = MibScalar
activeOstB = _ActiveOstB_Object(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 4, 1, 2, 24),
    _ActiveOstB_Type()
)
activeOstB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    activeOstB.setStatus("current")
_ForwardPowerOstA_Type = FloatingPoint
_ForwardPowerOstA_Object = MibScalar
forwardPowerOstA = _ForwardPowerOstA_Object(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 4, 1, 2, 25),
    _ForwardPowerOstA_Type()
)
forwardPowerOstA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    forwardPowerOstA.setStatus("current")
if mibBuilder.loadTexts:
    forwardPowerOstA.setUnits("Watt")
_ReflectedPowerOstA_Type = FloatingPoint
_ReflectedPowerOstA_Object = MibScalar
reflectedPowerOstA = _ReflectedPowerOstA_Object(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 4, 1, 2, 26),
    _ReflectedPowerOstA_Type()
)
reflectedPowerOstA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    reflectedPowerOstA.setStatus("current")
if mibBuilder.loadTexts:
    reflectedPowerOstA.setUnits("Watt")
_ForwardPowerOstB_Type = FloatingPoint
_ForwardPowerOstB_Object = MibScalar
forwardPowerOstB = _ForwardPowerOstB_Object(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 4, 1, 2, 27),
    _ForwardPowerOstB_Type()
)
forwardPowerOstB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    forwardPowerOstB.setStatus("current")
if mibBuilder.loadTexts:
    forwardPowerOstB.setUnits("Watt")
_ReflectedPowerOstB_Type = FloatingPoint
_ReflectedPowerOstB_Object = MibScalar
reflectedPowerOstB = _ReflectedPowerOstB_Object(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 4, 1, 2, 28),
    _ReflectedPowerOstB_Type()
)
reflectedPowerOstB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    reflectedPowerOstB.setStatus("current")
if mibBuilder.loadTexts:
    reflectedPowerOstB.setUnits("Watt")
_PowerSupply_Type = FloatingPoint
_PowerSupply_Object = MibScalar
powerSupply = _PowerSupply_Object(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 4, 1, 2, 29),
    _PowerSupply_Type()
)
powerSupply.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerSupply.setStatus("current")
if mibBuilder.loadTexts:
    powerSupply.setUnits("volt")
_AdditionalPowerSupply_Type = TruthValue
_AdditionalPowerSupply_Object = MibScalar
additionalPowerSupply = _AdditionalPowerSupply_Object(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 4, 1, 2, 30),
    _AdditionalPowerSupply_Type()
)
additionalPowerSupply.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    additionalPowerSupply.setStatus("current")
_InternalPowerSupply_Type = FloatingPoint
_InternalPowerSupply_Object = MibScalar
internalPowerSupply = _InternalPowerSupply_Object(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 4, 1, 2, 31),
    _InternalPowerSupply_Type()
)
internalPowerSupply.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    internalPowerSupply.setStatus("current")
if mibBuilder.loadTexts:
    internalPowerSupply.setUnits("volt")
_ExternalPowerSupply_Type = FloatingPoint
_ExternalPowerSupply_Object = MibScalar
externalPowerSupply = _ExternalPowerSupply_Object(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 4, 1, 2, 32),
    _ExternalPowerSupply_Type()
)
externalPowerSupply.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    externalPowerSupply.setStatus("current")
if mibBuilder.loadTexts:
    externalPowerSupply.setUnits("volt")
_DetailedInfo_ObjectIdentity = ObjectIdentity
detailedInfo = _DetailedInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 4, 1, 3)
)
_ExcInputTable_Object = MibTable
excInputTable = _ExcInputTable_Object(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 4, 1, 3, 2)
)
if mibBuilder.loadTexts:
    excInputTable.setStatus("current")
_ExcInputEntry_Object = MibTableRow
excInputEntry = _ExcInputEntry_Object(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 4, 1, 3, 2, 1)
)
excInputEntry.setIndexNames(
    (0, "RS-XX8000-DVB-TX-MIB", "excInputExcIdx"),
    (0, "RS-XX8000-DVB-TX-MIB", "excInputChannelIdx"),
)
if mibBuilder.loadTexts:
    excInputEntry.setStatus("current")
_ExcInputExcIdx_Type = IndexAB
_ExcInputExcIdx_Object = MibTableColumn
excInputExcIdx = _ExcInputExcIdx_Object(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 4, 1, 3, 2, 1, 1),
    _ExcInputExcIdx_Type()
)
excInputExcIdx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    excInputExcIdx.setStatus("current")


class _ExcInputChannelIdx_Type(Integer32):
    """Custom type excInputChannelIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 6),
    )


_ExcInputChannelIdx_Type.__name__ = "Integer32"
_ExcInputChannelIdx_Object = MibTableColumn
excInputChannelIdx = _ExcInputChannelIdx_Object(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 4, 1, 3, 2, 1, 2),
    _ExcInputChannelIdx_Type()
)
excInputChannelIdx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    excInputChannelIdx.setStatus("current")


class _ExcInputChannelName_Type(Integer32):
    """Custom type excInputChannelName based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("hp1", 1),
          ("hp2", 2),
          ("lp1", 3),
          ("lp2", 4),
          ("activeHP", 5),
          ("activeLP", 6))
    )


_ExcInputChannelName_Type.__name__ = "Integer32"
_ExcInputChannelName_Object = MibTableColumn
excInputChannelName = _ExcInputChannelName_Object(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 4, 1, 3, 2, 1, 3),
    _ExcInputChannelName_Type()
)
excInputChannelName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    excInputChannelName.setStatus("current")
_ExcInputConnected_Type = TruthValue
_ExcInputConnected_Object = MibTableColumn
excInputConnected = _ExcInputConnected_Object(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 4, 1, 3, 2, 1, 4),
    _ExcInputConnected_Type()
)
excInputConnected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    excInputConnected.setStatus("current")
_ExcInputSeamless_Type = TruthValue
_ExcInputSeamless_Object = MibTableColumn
excInputSeamless = _ExcInputSeamless_Object(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 4, 1, 3, 2, 1, 5),
    _ExcInputSeamless_Type()
)
excInputSeamless.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    excInputSeamless.setStatus("current")
_ExcInputPreselected_Type = TruthValue
_ExcInputPreselected_Object = MibTableColumn
excInputPreselected = _ExcInputPreselected_Object(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 4, 1, 3, 2, 1, 6),
    _ExcInputPreselected_Type()
)
excInputPreselected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    excInputPreselected.setStatus("current")
_ExcInputActive_Type = TruthValue
_ExcInputActive_Object = MibTableColumn
excInputActive = _ExcInputActive_Object(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 4, 1, 3, 2, 1, 7),
    _ExcInputActive_Type()
)
excInputActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    excInputActive.setStatus("current")
_ExcInputMipFail_Type = TruthValue
_ExcInputMipFail_Object = MibTableColumn
excInputMipFail = _ExcInputMipFail_Object(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 4, 1, 3, 2, 1, 8),
    _ExcInputMipFail_Type()
)
excInputMipFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    excInputMipFail.setStatus("current")


class _ExcInputBandwidth_Type(Integer32):
    """Custom type excInputBandwidth based on Integer32"""
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
        *(("mhz5", 1),
          ("mhz6", 2),
          ("mhz7", 3),
          ("mhz8", 4))
    )


_ExcInputBandwidth_Type.__name__ = "Integer32"
_ExcInputBandwidth_Object = MibTableColumn
excInputBandwidth = _ExcInputBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 4, 1, 3, 2, 1, 9),
    _ExcInputBandwidth_Type()
)
excInputBandwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    excInputBandwidth.setStatus("current")


class _ExcInputFFTLength_Type(Integer32):
    """Custom type excInputFFTLength based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("k2", 1),
          ("k8", 2),
          ("k4", 3))
    )


_ExcInputFFTLength_Type.__name__ = "Integer32"
_ExcInputFFTLength_Object = MibTableColumn
excInputFFTLength = _ExcInputFFTLength_Object(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 4, 1, 3, 2, 1, 10),
    _ExcInputFFTLength_Type()
)
excInputFFTLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    excInputFFTLength.setStatus("current")


class _ExcInputGuardInterval_Type(Integer32):
    """Custom type excInputGuardInterval based on Integer32"""
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
        *(("oneOf32", 1),
          ("oneOf16", 2),
          ("oneOf8", 3),
          ("oneOf4", 4))
    )


_ExcInputGuardInterval_Type.__name__ = "Integer32"
_ExcInputGuardInterval_Object = MibTableColumn
excInputGuardInterval = _ExcInputGuardInterval_Object(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 4, 1, 3, 2, 1, 11),
    _ExcInputGuardInterval_Type()
)
excInputGuardInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    excInputGuardInterval.setStatus("current")


class _ExcInputConstellation_Type(Integer32):
    """Custom type excInputConstellation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("qpsk", 1),
          ("qam16", 2),
          ("qam64", 3))
    )


_ExcInputConstellation_Type.__name__ = "Integer32"
_ExcInputConstellation_Object = MibTableColumn
excInputConstellation = _ExcInputConstellation_Object(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 4, 1, 3, 2, 1, 12),
    _ExcInputConstellation_Type()
)
excInputConstellation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    excInputConstellation.setStatus("current")


class _ExcInputAlpha_Type(Integer32):
    """Custom type excInputAlpha based on Integer32"""
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
        *(("noHierarchy", 1),
          ("one", 2),
          ("two", 3),
          ("four", 4))
    )


_ExcInputAlpha_Type.__name__ = "Integer32"
_ExcInputAlpha_Object = MibTableColumn
excInputAlpha = _ExcInputAlpha_Object(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 4, 1, 3, 2, 1, 13),
    _ExcInputAlpha_Type()
)
excInputAlpha.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    excInputAlpha.setStatus("obsolete")


class _ExcInputCellID_Type(Integer32):
    """Custom type excInputCellID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_ExcInputCellID_Type.__name__ = "Integer32"
_ExcInputCellID_Object = MibTableColumn
excInputCellID = _ExcInputCellID_Object(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 4, 1, 3, 2, 1, 14),
    _ExcInputCellID_Type()
)
excInputCellID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    excInputCellID.setStatus("current")


class _ExcInputInterleaver_Type(Integer32):
    """Custom type excInputInterleaver based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("indepth", 1),
          ("nat", 2))
    )


_ExcInputInterleaver_Type.__name__ = "Integer32"
_ExcInputInterleaver_Object = MibTableColumn
excInputInterleaver = _ExcInputInterleaver_Object(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 4, 1, 3, 2, 1, 15),
    _ExcInputInterleaver_Type()
)
excInputInterleaver.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    excInputInterleaver.setStatus("current")


class _ExcInputCodeRate_Type(Integer32):
    """Custom type excInputCodeRate based on Integer32"""
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
        *(("oneOf2", 1),
          ("twoOf3", 2),
          ("threeOf4", 3),
          ("fiveOf6", 4),
          ("sevenOf8", 5))
    )


_ExcInputCodeRate_Type.__name__ = "Integer32"
_ExcInputCodeRate_Object = MibTableColumn
excInputCodeRate = _ExcInputCodeRate_Object(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 4, 1, 3, 2, 1, 16),
    _ExcInputCodeRate_Type()
)
excInputCodeRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    excInputCodeRate.setStatus("current")


class _ExcInputPacketLength_Type(Integer32):
    """Custom type excInputPacketLength based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(188, 208),
    )


_ExcInputPacketLength_Type.__name__ = "Integer32"
_ExcInputPacketLength_Object = MibTableColumn
excInputPacketLength = _ExcInputPacketLength_Object(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 4, 1, 3, 2, 1, 17),
    _ExcInputPacketLength_Type()
)
excInputPacketLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    excInputPacketLength.setStatus("current")
_ExcInputMeasuredDatarate_Type = Integer32
_ExcInputMeasuredDatarate_Object = MibTableColumn
excInputMeasuredDatarate = _ExcInputMeasuredDatarate_Object(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 4, 1, 3, 2, 1, 18),
    _ExcInputMeasuredDatarate_Type()
)
excInputMeasuredDatarate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    excInputMeasuredDatarate.setStatus("current")
_ExcInputRequiredDatarate_Type = Integer32
_ExcInputRequiredDatarate_Object = MibTableColumn
excInputRequiredDatarate = _ExcInputRequiredDatarate_Object(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 4, 1, 3, 2, 1, 19),
    _ExcInputRequiredDatarate_Type()
)
excInputRequiredDatarate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    excInputRequiredDatarate.setStatus("current")


class _ExcInputMaximumDelay_Type(Integer32):
    """Custom type excInputMaximumDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100000000),
    )


_ExcInputMaximumDelay_Type.__name__ = "Integer32"
_ExcInputMaximumDelay_Object = MibTableColumn
excInputMaximumDelay = _ExcInputMaximumDelay_Object(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 4, 1, 3, 2, 1, 20),
    _ExcInputMaximumDelay_Type()
)
excInputMaximumDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    excInputMaximumDelay.setStatus("current")
if mibBuilder.loadTexts:
    excInputMaximumDelay.setUnits("Nanoseconds")
_OstTable_Object = MibTable
ostTable = _OstTable_Object(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 4, 1, 3, 3)
)
if mibBuilder.loadTexts:
    ostTable.setStatus("current")
_OstEntry_Object = MibTableRow
ostEntry = _OstEntry_Object(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 4, 1, 3, 3, 1)
)
ostEntry.setIndexNames(
    (0, "RS-XX8000-DVB-TX-MIB", "ostIdx"),
    (0, "RS-XX8000-DVB-TX-MIB", "ostRackIdx"),
    (0, "RS-XX8000-DVB-TX-MIB", "ostRackAmpIdx"),
)
if mibBuilder.loadTexts:
    ostEntry.setStatus("current")
_OstIdx_Type = IndexAB
_OstIdx_Object = MibTableColumn
ostIdx = _OstIdx_Object(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 4, 1, 3, 3, 1, 1),
    _OstIdx_Type()
)
ostIdx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ostIdx.setStatus("current")
_OstRackIdx_Type = IndexRack
_OstRackIdx_Object = MibTableColumn
ostRackIdx = _OstRackIdx_Object(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 4, 1, 3, 3, 1, 2),
    _OstRackIdx_Type()
)
ostRackIdx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ostRackIdx.setStatus("current")
_OstRackInletTemperature_Type = FloatingPoint
_OstRackInletTemperature_Object = MibTableColumn
ostRackInletTemperature = _OstRackInletTemperature_Object(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 4, 1, 3, 3, 1, 3),
    _OstRackInletTemperature_Type()
)
ostRackInletTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ostRackInletTemperature.setStatus("current")
if mibBuilder.loadTexts:
    ostRackInletTemperature.setUnits("Degree Celsius")
_OstRackOutletTemperature_Type = FloatingPoint
_OstRackOutletTemperature_Object = MibTableColumn
ostRackOutletTemperature = _OstRackOutletTemperature_Object(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 4, 1, 3, 3, 1, 4),
    _OstRackOutletTemperature_Type()
)
ostRackOutletTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ostRackOutletTemperature.setStatus("current")
if mibBuilder.loadTexts:
    ostRackOutletTemperature.setUnits("Degree Celsius")
_OstRackAuxPowerSupply_Type = FloatingPoint
_OstRackAuxPowerSupply_Object = MibTableColumn
ostRackAuxPowerSupply = _OstRackAuxPowerSupply_Object(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 4, 1, 3, 3, 1, 5),
    _OstRackAuxPowerSupply_Type()
)
ostRackAuxPowerSupply.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ostRackAuxPowerSupply.setStatus("current")
if mibBuilder.loadTexts:
    ostRackAuxPowerSupply.setUnits("Volt")
_OstRackAmpIdx_Type = IndexAmplifier
_OstRackAmpIdx_Object = MibTableColumn
ostRackAmpIdx = _OstRackAmpIdx_Object(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 4, 1, 3, 3, 1, 400),
    _OstRackAmpIdx_Type()
)
ostRackAmpIdx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ostRackAmpIdx.setStatus("current")
_OstRackAmpI1A_Type = FloatingPoint
_OstRackAmpI1A_Object = MibTableColumn
ostRackAmpI1A = _OstRackAmpI1A_Object(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 4, 1, 3, 3, 1, 401),
    _OstRackAmpI1A_Type()
)
ostRackAmpI1A.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ostRackAmpI1A.setStatus("current")
if mibBuilder.loadTexts:
    ostRackAmpI1A.setUnits("Ampere")
_OstRackAmpI2A_Type = FloatingPoint
_OstRackAmpI2A_Object = MibTableColumn
ostRackAmpI2A = _OstRackAmpI2A_Object(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 4, 1, 3, 3, 1, 402),
    _OstRackAmpI2A_Type()
)
ostRackAmpI2A.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ostRackAmpI2A.setStatus("current")
if mibBuilder.loadTexts:
    ostRackAmpI2A.setUnits("Ampere")
_OstRackAmpI3A_Type = FloatingPoint
_OstRackAmpI3A_Object = MibTableColumn
ostRackAmpI3A = _OstRackAmpI3A_Object(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 4, 1, 3, 3, 1, 403),
    _OstRackAmpI3A_Type()
)
ostRackAmpI3A.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ostRackAmpI3A.setStatus("current")
if mibBuilder.loadTexts:
    ostRackAmpI3A.setUnits("Ampere")
_OstRackAmpI4A_Type = FloatingPoint
_OstRackAmpI4A_Object = MibTableColumn
ostRackAmpI4A = _OstRackAmpI4A_Object(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 4, 1, 3, 3, 1, 404),
    _OstRackAmpI4A_Type()
)
ostRackAmpI4A.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ostRackAmpI4A.setStatus("current")
if mibBuilder.loadTexts:
    ostRackAmpI4A.setUnits("Ampere")
_OstRackAmpI1B_Type = FloatingPoint
_OstRackAmpI1B_Object = MibTableColumn
ostRackAmpI1B = _OstRackAmpI1B_Object(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 4, 1, 3, 3, 1, 405),
    _OstRackAmpI1B_Type()
)
ostRackAmpI1B.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ostRackAmpI1B.setStatus("current")
if mibBuilder.loadTexts:
    ostRackAmpI1B.setUnits("Ampere")
_OstRackAmpI2B_Type = FloatingPoint
_OstRackAmpI2B_Object = MibTableColumn
ostRackAmpI2B = _OstRackAmpI2B_Object(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 4, 1, 3, 3, 1, 406),
    _OstRackAmpI2B_Type()
)
ostRackAmpI2B.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ostRackAmpI2B.setStatus("current")
if mibBuilder.loadTexts:
    ostRackAmpI2B.setUnits("Ampere")
_OstRackAmpI3B_Type = FloatingPoint
_OstRackAmpI3B_Object = MibTableColumn
ostRackAmpI3B = _OstRackAmpI3B_Object(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 4, 1, 3, 3, 1, 407),
    _OstRackAmpI3B_Type()
)
ostRackAmpI3B.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ostRackAmpI3B.setStatus("current")
if mibBuilder.loadTexts:
    ostRackAmpI3B.setUnits("Ampere")
_OstRackAmpI4B_Type = FloatingPoint
_OstRackAmpI4B_Object = MibTableColumn
ostRackAmpI4B = _OstRackAmpI4B_Object(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 4, 1, 3, 3, 1, 408),
    _OstRackAmpI4B_Type()
)
ostRackAmpI4B.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ostRackAmpI4B.setStatus("current")
if mibBuilder.loadTexts:
    ostRackAmpI4B.setUnits("Ampere")
_OstRackAmpIDrv_Type = FloatingPoint
_OstRackAmpIDrv_Object = MibTableColumn
ostRackAmpIDrv = _OstRackAmpIDrv_Object(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 4, 1, 3, 3, 1, 409),
    _OstRackAmpIDrv_Type()
)
ostRackAmpIDrv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ostRackAmpIDrv.setStatus("current")
if mibBuilder.loadTexts:
    ostRackAmpIDrv.setUnits("Ampere")
_OstRackAmpUDc_Type = FloatingPoint
_OstRackAmpUDc_Object = MibTableColumn
ostRackAmpUDc = _OstRackAmpUDc_Object(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 4, 1, 3, 3, 1, 410),
    _OstRackAmpUDc_Type()
)
ostRackAmpUDc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ostRackAmpUDc.setStatus("current")
if mibBuilder.loadTexts:
    ostRackAmpUDc.setUnits("Volt")
_OstRackAmpIDc_Type = FloatingPoint
_OstRackAmpIDc_Object = MibTableColumn
ostRackAmpIDc = _OstRackAmpIDc_Object(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 4, 1, 3, 3, 1, 411),
    _OstRackAmpIDc_Type()
)
ostRackAmpIDc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ostRackAmpIDc.setStatus("current")
if mibBuilder.loadTexts:
    ostRackAmpIDc.setUnits("Ampere")
_OstRackAmpUDcControl_Type = FloatingPoint
_OstRackAmpUDcControl_Object = MibTableColumn
ostRackAmpUDcControl = _OstRackAmpUDcControl_Object(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 4, 1, 3, 3, 1, 412),
    _OstRackAmpUDcControl_Type()
)
ostRackAmpUDcControl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ostRackAmpUDcControl.setStatus("current")
if mibBuilder.loadTexts:
    ostRackAmpUDcControl.setUnits("Volt")
_OstRackAmpUReg_Type = FloatingPoint
_OstRackAmpUReg_Object = MibTableColumn
ostRackAmpUReg = _OstRackAmpUReg_Object(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 4, 1, 3, 3, 1, 413),
    _OstRackAmpUReg_Type()
)
ostRackAmpUReg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ostRackAmpUReg.setStatus("current")
if mibBuilder.loadTexts:
    ostRackAmpUReg.setUnits("Volt")
_OstRackAmpPowerA_Type = FloatingPoint
_OstRackAmpPowerA_Object = MibTableColumn
ostRackAmpPowerA = _OstRackAmpPowerA_Object(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 4, 1, 3, 3, 1, 414),
    _OstRackAmpPowerA_Type()
)
ostRackAmpPowerA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ostRackAmpPowerA.setStatus("current")
if mibBuilder.loadTexts:
    ostRackAmpPowerA.setUnits("Volt")
_OstRackAmpPowerB_Type = FloatingPoint
_OstRackAmpPowerB_Object = MibTableColumn
ostRackAmpPowerB = _OstRackAmpPowerB_Object(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 4, 1, 3, 3, 1, 415),
    _OstRackAmpPowerB_Type()
)
ostRackAmpPowerB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ostRackAmpPowerB.setStatus("current")
if mibBuilder.loadTexts:
    ostRackAmpPowerB.setUnits("Volt")
_OstRackAmpPowerOut_Type = FloatingPoint
_OstRackAmpPowerOut_Object = MibTableColumn
ostRackAmpPowerOut = _OstRackAmpPowerOut_Object(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 4, 1, 3, 3, 1, 416),
    _OstRackAmpPowerOut_Type()
)
ostRackAmpPowerOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ostRackAmpPowerOut.setStatus("current")
if mibBuilder.loadTexts:
    ostRackAmpPowerOut.setUnits("Volt")
_OstRackAmpPowerReflection_Type = FloatingPoint
_OstRackAmpPowerReflection_Object = MibTableColumn
ostRackAmpPowerReflection = _OstRackAmpPowerReflection_Object(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 4, 1, 3, 3, 1, 417),
    _OstRackAmpPowerReflection_Type()
)
ostRackAmpPowerReflection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ostRackAmpPowerReflection.setStatus("current")
if mibBuilder.loadTexts:
    ostRackAmpPowerReflection.setUnits("Volt")
_OstRackAmpPowerReference_Type = FloatingPoint
_OstRackAmpPowerReference_Object = MibTableColumn
ostRackAmpPowerReference = _OstRackAmpPowerReference_Object(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 4, 1, 3, 3, 1, 418),
    _OstRackAmpPowerReference_Type()
)
ostRackAmpPowerReference.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ostRackAmpPowerReference.setStatus("current")
if mibBuilder.loadTexts:
    ostRackAmpPowerReference.setUnits("Volt")
_OstRackAmpDeltaPhase_Type = FloatingPoint
_OstRackAmpDeltaPhase_Object = MibTableColumn
ostRackAmpDeltaPhase = _OstRackAmpDeltaPhase_Object(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 4, 1, 3, 3, 1, 419),
    _OstRackAmpDeltaPhase_Type()
)
ostRackAmpDeltaPhase.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ostRackAmpDeltaPhase.setStatus("current")
if mibBuilder.loadTexts:
    ostRackAmpDeltaPhase.setUnits("Percent")
_OstRackAmpCmdDeltaPhase_Type = FloatingPoint
_OstRackAmpCmdDeltaPhase_Object = MibTableColumn
ostRackAmpCmdDeltaPhase = _OstRackAmpCmdDeltaPhase_Object(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 4, 1, 3, 3, 1, 420),
    _OstRackAmpCmdDeltaPhase_Type()
)
ostRackAmpCmdDeltaPhase.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ostRackAmpCmdDeltaPhase.setStatus("current")
if mibBuilder.loadTexts:
    ostRackAmpCmdDeltaPhase.setUnits("Percent")
_ExciterStatusTable_Object = MibTable
exciterStatusTable = _ExciterStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 4, 1, 3, 20)
)
if mibBuilder.loadTexts:
    exciterStatusTable.setStatus("current")
_ExciterStatusEntry_Object = MibTableRow
exciterStatusEntry = _ExciterStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 4, 1, 3, 20, 1)
)
exciterStatusEntry.setIndexNames(
    (0, "RS-XX8000-DVB-TX-MIB", "excStatusExcIdx"),
)
if mibBuilder.loadTexts:
    exciterStatusEntry.setStatus("current")
_ExcStatusExcIdx_Type = IndexAB
_ExcStatusExcIdx_Object = MibTableColumn
excStatusExcIdx = _ExcStatusExcIdx_Object(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 4, 1, 3, 20, 1, 3),
    _ExcStatusExcIdx_Type()
)
excStatusExcIdx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    excStatusExcIdx.setStatus("current")
_ExcStatusRfOutputAgcRegulation_Type = FloatingPoint
_ExcStatusRfOutputAgcRegulation_Object = MibTableColumn
excStatusRfOutputAgcRegulation = _ExcStatusRfOutputAgcRegulation_Object(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 4, 1, 3, 20, 1, 4),
    _ExcStatusRfOutputAgcRegulation_Type()
)
excStatusRfOutputAgcRegulation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    excStatusRfOutputAgcRegulation.setStatus("current")
if mibBuilder.loadTexts:
    excStatusRfOutputAgcRegulation.setUnits("Percent")


class _ExcStatusRfIqAdjustAuto_Type(Integer32):
    """Custom type excStatusRfIqAdjustAuto based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("notAdjusted", 1),
          ("inProgress", 2),
          ("adjusted", 3))
    )


_ExcStatusRfIqAdjustAuto_Type.__name__ = "Integer32"
_ExcStatusRfIqAdjustAuto_Object = MibTableColumn
excStatusRfIqAdjustAuto = _ExcStatusRfIqAdjustAuto_Object(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 4, 1, 3, 20, 1, 5),
    _ExcStatusRfIqAdjustAuto_Type()
)
excStatusRfIqAdjustAuto.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    excStatusRfIqAdjustAuto.setStatus("current")
if mibBuilder.loadTexts:
    excStatusRfIqAdjustAuto.setUnits("Percent")
_ExcStatusRfIqAdjustLO1Frequency_Type = FloatingPoint
_ExcStatusRfIqAdjustLO1Frequency_Object = MibTableColumn
excStatusRfIqAdjustLO1Frequency = _ExcStatusRfIqAdjustLO1Frequency_Object(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 4, 1, 3, 20, 1, 6),
    _ExcStatusRfIqAdjustLO1Frequency_Type()
)
excStatusRfIqAdjustLO1Frequency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    excStatusRfIqAdjustLO1Frequency.setStatus("current")
if mibBuilder.loadTexts:
    excStatusRfIqAdjustLO1Frequency.setUnits("MHz")
_ExcStatusNominalPower_Type = Integer32
_ExcStatusNominalPower_Object = MibTableColumn
excStatusNominalPower = _ExcStatusNominalPower_Object(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 4, 1, 3, 20, 1, 7),
    _ExcStatusNominalPower_Type()
)
excStatusNominalPower.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    excStatusNominalPower.setStatus("current")
if mibBuilder.loadTexts:
    excStatusNominalPower.setUnits("W")
_ExcStatusVSWR_Type = FloatingPoint
_ExcStatusVSWR_Object = MibTableColumn
excStatusVSWR = _ExcStatusVSWR_Object(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 4, 1, 3, 20, 1, 9),
    _ExcStatusVSWR_Type()
)
excStatusVSWR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    excStatusVSWR.setStatus("current")
_ExcStatusSfnDelayProcessing_Type = FloatingPoint
_ExcStatusSfnDelayProcessing_Object = MibTableColumn
excStatusSfnDelayProcessing = _ExcStatusSfnDelayProcessing_Object(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 4, 1, 3, 20, 1, 13),
    _ExcStatusSfnDelayProcessing_Type()
)
excStatusSfnDelayProcessing.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    excStatusSfnDelayProcessing.setStatus("current")
if mibBuilder.loadTexts:
    excStatusSfnDelayProcessing.setUnits("Microseconds")
_ExcStatusSfnDelayDynamic_Type = FloatingPoint
_ExcStatusSfnDelayDynamic_Object = MibTableColumn
excStatusSfnDelayDynamic = _ExcStatusSfnDelayDynamic_Object(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 4, 1, 3, 20, 1, 14),
    _ExcStatusSfnDelayDynamic_Type()
)
excStatusSfnDelayDynamic.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    excStatusSfnDelayDynamic.setStatus("current")
if mibBuilder.loadTexts:
    excStatusSfnDelayDynamic.setUnits("Microseconds")
_ExcStatusSfnDelayNetwork_Type = FloatingPoint
_ExcStatusSfnDelayNetwork_Object = MibTableColumn
excStatusSfnDelayNetwork = _ExcStatusSfnDelayNetwork_Object(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 4, 1, 3, 20, 1, 15),
    _ExcStatusSfnDelayNetwork_Type()
)
excStatusSfnDelayNetwork.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    excStatusSfnDelayNetwork.setStatus("current")
if mibBuilder.loadTexts:
    excStatusSfnDelayNetwork.setUnits("Microseconds")
_ExcStatusSfnDelayTxOffset_Type = FloatingPoint
_ExcStatusSfnDelayTxOffset_Object = MibTableColumn
excStatusSfnDelayTxOffset = _ExcStatusSfnDelayTxOffset_Object(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 4, 1, 3, 20, 1, 16),
    _ExcStatusSfnDelayTxOffset_Type()
)
excStatusSfnDelayTxOffset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    excStatusSfnDelayTxOffset.setStatus("current")
if mibBuilder.loadTexts:
    excStatusSfnDelayTxOffset.setUnits("Microseconds")
_ExcStatusSfnDelayMaximum_Type = FloatingPoint
_ExcStatusSfnDelayMaximum_Object = MibTableColumn
excStatusSfnDelayMaximum = _ExcStatusSfnDelayMaximum_Object(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 4, 1, 3, 20, 1, 17),
    _ExcStatusSfnDelayMaximum_Type()
)
excStatusSfnDelayMaximum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    excStatusSfnDelayMaximum.setStatus("current")
if mibBuilder.loadTexts:
    excStatusSfnDelayMaximum.setUnits("Microseconds")
_ExcStatusSfnDelayTotal_Type = FloatingPoint
_ExcStatusSfnDelayTotal_Object = MibTableColumn
excStatusSfnDelayTotal = _ExcStatusSfnDelayTotal_Object(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 4, 1, 3, 20, 1, 18),
    _ExcStatusSfnDelayTotal_Type()
)
excStatusSfnDelayTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    excStatusSfnDelayTotal.setStatus("current")
if mibBuilder.loadTexts:
    excStatusSfnDelayTotal.setUnits("Microseconds")


class _ExcStatusAmplifierControl_Type(Integer32):
    """Custom type excStatusAmplifierControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("on", 1),
          ("off", 2))
    )


_ExcStatusAmplifierControl_Type.__name__ = "Integer32"
_ExcStatusAmplifierControl_Object = MibTableColumn
excStatusAmplifierControl = _ExcStatusAmplifierControl_Object(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 4, 1, 3, 20, 1, 20),
    _ExcStatusAmplifierControl_Type()
)
excStatusAmplifierControl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    excStatusAmplifierControl.setStatus("current")
_ExcStatusReqDataRateHP_Type = Integer32
_ExcStatusReqDataRateHP_Object = MibTableColumn
excStatusReqDataRateHP = _ExcStatusReqDataRateHP_Object(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 4, 1, 3, 20, 1, 30),
    _ExcStatusReqDataRateHP_Type()
)
excStatusReqDataRateHP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    excStatusReqDataRateHP.setStatus("current")
if mibBuilder.loadTexts:
    excStatusReqDataRateHP.setUnits("bit per seconds")
_ExcStatusReqDataRateLP_Type = Integer32
_ExcStatusReqDataRateLP_Object = MibTableColumn
excStatusReqDataRateLP = _ExcStatusReqDataRateLP_Object(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 4, 1, 3, 20, 1, 31),
    _ExcStatusReqDataRateLP_Type()
)
excStatusReqDataRateLP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    excStatusReqDataRateLP.setStatus("current")
if mibBuilder.loadTexts:
    excStatusReqDataRateLP.setUnits("bit per seconds")
_ExcStatusFailDelay_Type = FailDelayStatus
_ExcStatusFailDelay_Object = MibTableColumn
excStatusFailDelay = _ExcStatusFailDelay_Object(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 4, 1, 3, 20, 1, 40),
    _ExcStatusFailDelay_Type()
)
excStatusFailDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    excStatusFailDelay.setStatus("current")
_ExciterPrecorrectionTable_Object = MibTable
exciterPrecorrectionTable = _ExciterPrecorrectionTable_Object(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 4, 1, 3, 21)
)
if mibBuilder.loadTexts:
    exciterPrecorrectionTable.setStatus("current")
_ExciterPrecorrectionEntry_Object = MibTableRow
exciterPrecorrectionEntry = _ExciterPrecorrectionEntry_Object(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 4, 1, 3, 21, 1)
)
exciterPrecorrectionEntry.setIndexNames(
    (0, "RS-XX8000-DVB-TX-MIB", "excPrecExcIdx"),
)
if mibBuilder.loadTexts:
    exciterPrecorrectionEntry.setStatus("current")
_ExcPrecExcIdx_Type = IndexAB
_ExcPrecExcIdx_Object = MibTableColumn
excPrecExcIdx = _ExcPrecExcIdx_Object(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 4, 1, 3, 21, 1, 3),
    _ExcPrecExcIdx_Type()
)
excPrecExcIdx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    excPrecExcIdx.setStatus("current")
_ExcPrecLinCorrection_Type = SwitchOnOff
_ExcPrecLinCorrection_Object = MibTableColumn
excPrecLinCorrection = _ExcPrecLinCorrection_Object(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 4, 1, 3, 21, 1, 4),
    _ExcPrecLinCorrection_Type()
)
excPrecLinCorrection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    excPrecLinCorrection.setStatus("current")


class _ExcPrecLinAutomaticADE_Type(Integer32):
    """Custom type excPrecLinAutomaticADE based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("manual", 1),
          ("automatic", 2),
          ("adaptive", 3))
    )


_ExcPrecLinAutomaticADE_Type.__name__ = "Integer32"
_ExcPrecLinAutomaticADE_Object = MibTableColumn
excPrecLinAutomaticADE = _ExcPrecLinAutomaticADE_Object(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 4, 1, 3, 21, 1, 5),
    _ExcPrecLinAutomaticADE_Type()
)
excPrecLinAutomaticADE.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    excPrecLinAutomaticADE.setStatus("current")
_ExcPrecLinMaxAmplitudeRipple_Type = FloatingPoint
_ExcPrecLinMaxAmplitudeRipple_Object = MibTableColumn
excPrecLinMaxAmplitudeRipple = _ExcPrecLinMaxAmplitudeRipple_Object(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 4, 1, 3, 21, 1, 6),
    _ExcPrecLinMaxAmplitudeRipple_Type()
)
excPrecLinMaxAmplitudeRipple.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    excPrecLinMaxAmplitudeRipple.setStatus("current")
if mibBuilder.loadTexts:
    excPrecLinMaxAmplitudeRipple.setUnits("dB")


class _ExcPrecLinMaxGroupDelayRipple_Type(Integer32):
    """Custom type excPrecLinMaxGroupDelayRipple based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 500),
    )


_ExcPrecLinMaxGroupDelayRipple_Type.__name__ = "Integer32"
_ExcPrecLinMaxGroupDelayRipple_Object = MibTableColumn
excPrecLinMaxGroupDelayRipple = _ExcPrecLinMaxGroupDelayRipple_Object(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 4, 1, 3, 21, 1, 7),
    _ExcPrecLinMaxGroupDelayRipple_Type()
)
excPrecLinMaxGroupDelayRipple.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    excPrecLinMaxGroupDelayRipple.setStatus("current")
if mibBuilder.loadTexts:
    excPrecLinMaxGroupDelayRipple.setUnits("Nanoseconds")
_ExcPrecLinAmplitudeRipple_Type = FloatingPoint
_ExcPrecLinAmplitudeRipple_Object = MibTableColumn
excPrecLinAmplitudeRipple = _ExcPrecLinAmplitudeRipple_Object(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 4, 1, 3, 21, 1, 8),
    _ExcPrecLinAmplitudeRipple_Type()
)
excPrecLinAmplitudeRipple.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    excPrecLinAmplitudeRipple.setStatus("current")
if mibBuilder.loadTexts:
    excPrecLinAmplitudeRipple.setUnits("dB")
_ExcPrecLinGroupDelayRipple_Type = Integer32
_ExcPrecLinGroupDelayRipple_Object = MibTableColumn
excPrecLinGroupDelayRipple = _ExcPrecLinGroupDelayRipple_Object(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 4, 1, 3, 21, 1, 9),
    _ExcPrecLinGroupDelayRipple_Type()
)
excPrecLinGroupDelayRipple.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    excPrecLinGroupDelayRipple.setStatus("current")
if mibBuilder.loadTexts:
    excPrecLinGroupDelayRipple.setUnits("Nanoseconds")


class _ExcPrecLinInputLevel_Type(Integer32):
    """Custom type excPrecLinInputLevel based on Integer32"""
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
        *(("tooHigh", 1),
          ("ok", 2),
          ("tooLow", 3),
          ("failure", 4))
    )


_ExcPrecLinInputLevel_Type.__name__ = "Integer32"
_ExcPrecLinInputLevel_Object = MibTableColumn
excPrecLinInputLevel = _ExcPrecLinInputLevel_Object(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 4, 1, 3, 21, 1, 10),
    _ExcPrecLinInputLevel_Type()
)
excPrecLinInputLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    excPrecLinInputLevel.setStatus("current")


class _ExcPrecLinAutomatic_Type(Integer32):
    """Custom type excPrecLinAutomatic based on Integer32"""
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
        *(("disabled", 1),
          ("active", 2),
          ("calculate", 3),
          ("measure", 4))
    )


_ExcPrecLinAutomatic_Type.__name__ = "Integer32"
_ExcPrecLinAutomatic_Object = MibTableColumn
excPrecLinAutomatic = _ExcPrecLinAutomatic_Object(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 4, 1, 3, 21, 1, 11),
    _ExcPrecLinAutomatic_Type()
)
excPrecLinAutomatic.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    excPrecLinAutomatic.setStatus("current")
_ExcPrecNonlinCorrection_Type = SwitchOnOff
_ExcPrecNonlinCorrection_Object = MibTableColumn
excPrecNonlinCorrection = _ExcPrecNonlinCorrection_Object(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 4, 1, 3, 21, 1, 12),
    _ExcPrecNonlinCorrection_Type()
)
excPrecNonlinCorrection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    excPrecNonlinCorrection.setStatus("current")


class _ExcPrecNonlinAutomaticADE_Type(Integer32):
    """Custom type excPrecNonlinAutomaticADE based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("manual", 1),
          ("automatic", 2),
          ("adaptive", 3))
    )


_ExcPrecNonlinAutomaticADE_Type.__name__ = "Integer32"
_ExcPrecNonlinAutomaticADE_Object = MibTableColumn
excPrecNonlinAutomaticADE = _ExcPrecNonlinAutomaticADE_Object(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 4, 1, 3, 21, 1, 13),
    _ExcPrecNonlinAutomaticADE_Type()
)
excPrecNonlinAutomaticADE.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    excPrecNonlinAutomaticADE.setStatus("current")
_ExcPrecNonlinThresholdShoulders_Type = FloatingPoint
_ExcPrecNonlinThresholdShoulders_Object = MibTableColumn
excPrecNonlinThresholdShoulders = _ExcPrecNonlinThresholdShoulders_Object(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 4, 1, 3, 21, 1, 14),
    _ExcPrecNonlinThresholdShoulders_Type()
)
excPrecNonlinThresholdShoulders.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    excPrecNonlinThresholdShoulders.setStatus("current")
if mibBuilder.loadTexts:
    excPrecNonlinThresholdShoulders.setUnits("dB")
_ExcPrecNonlinShoulderLeft_Type = FloatingPoint
_ExcPrecNonlinShoulderLeft_Object = MibTableColumn
excPrecNonlinShoulderLeft = _ExcPrecNonlinShoulderLeft_Object(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 4, 1, 3, 21, 1, 15),
    _ExcPrecNonlinShoulderLeft_Type()
)
excPrecNonlinShoulderLeft.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    excPrecNonlinShoulderLeft.setStatus("current")
if mibBuilder.loadTexts:
    excPrecNonlinShoulderLeft.setUnits("dB")
_ExcPrecNonlinShoulderRight_Type = FloatingPoint
_ExcPrecNonlinShoulderRight_Object = MibTableColumn
excPrecNonlinShoulderRight = _ExcPrecNonlinShoulderRight_Object(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 4, 1, 3, 21, 1, 16),
    _ExcPrecNonlinShoulderRight_Type()
)
excPrecNonlinShoulderRight.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    excPrecNonlinShoulderRight.setStatus("current")
if mibBuilder.loadTexts:
    excPrecNonlinShoulderRight.setUnits("dB")


class _ExcPrecNonlinInputLevel_Type(Integer32):
    """Custom type excPrecNonlinInputLevel based on Integer32"""
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
        *(("tooHigh", 1),
          ("ok", 2),
          ("tooLow", 3),
          ("failure", 4))
    )


_ExcPrecNonlinInputLevel_Type.__name__ = "Integer32"
_ExcPrecNonlinInputLevel_Object = MibTableColumn
excPrecNonlinInputLevel = _ExcPrecNonlinInputLevel_Object(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 4, 1, 3, 21, 1, 17),
    _ExcPrecNonlinInputLevel_Type()
)
excPrecNonlinInputLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    excPrecNonlinInputLevel.setStatus("current")


class _ExcPrecNonlinAutomatic_Type(Integer32):
    """Custom type excPrecNonlinAutomatic based on Integer32"""
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
        *(("disabled", 1),
          ("active", 2),
          ("calculate", 3),
          ("measure", 4))
    )


_ExcPrecNonlinAutomatic_Type.__name__ = "Integer32"
_ExcPrecNonlinAutomatic_Object = MibTableColumn
excPrecNonlinAutomatic = _ExcPrecNonlinAutomatic_Object(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 4, 1, 3, 21, 1, 18),
    _ExcPrecNonlinAutomatic_Type()
)
excPrecNonlinAutomatic.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    excPrecNonlinAutomatic.setStatus("current")
_ExcPrecUserState_Type = EqualizerCalibrationState
_ExcPrecUserState_Object = MibTableColumn
excPrecUserState = _ExcPrecUserState_Object(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 4, 1, 3, 21, 1, 100),
    _ExcPrecUserState_Type()
)
excPrecUserState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    excPrecUserState.setStatus("current")
_ExcPrecFactoryState_Type = EqualizerCalibrationState
_ExcPrecFactoryState_Object = MibTableColumn
excPrecFactoryState = _ExcPrecFactoryState_Object(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 4, 1, 3, 21, 1, 101),
    _ExcPrecFactoryState_Type()
)
excPrecFactoryState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    excPrecFactoryState.setStatus("current")


class _ExcPrecRestoreCurrentSettings_Type(Integer32):
    """Custom type excPrecRestoreCurrentSettings based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("stop", 1),
          ("start", 2))
    )


_ExcPrecRestoreCurrentSettings_Type.__name__ = "Integer32"
_ExcPrecRestoreCurrentSettings_Object = MibTableColumn
excPrecRestoreCurrentSettings = _ExcPrecRestoreCurrentSettings_Object(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 4, 1, 3, 21, 1, 102),
    _ExcPrecRestoreCurrentSettings_Type()
)
excPrecRestoreCurrentSettings.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    excPrecRestoreCurrentSettings.setStatus("current")


class _ExcPrecRestoreAllSettings_Type(Integer32):
    """Custom type excPrecRestoreAllSettings based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("stop", 1),
          ("start", 2))
    )


_ExcPrecRestoreAllSettings_Type.__name__ = "Integer32"
_ExcPrecRestoreAllSettings_Object = MibTableColumn
excPrecRestoreAllSettings = _ExcPrecRestoreAllSettings_Object(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 4, 1, 3, 21, 1, 103),
    _ExcPrecRestoreAllSettings_Type()
)
excPrecRestoreAllSettings.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    excPrecRestoreAllSettings.setStatus("current")
_ConfigurationTable_Object = MibTable
configurationTable = _ConfigurationTable_Object(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 4, 1, 3, 30)
)
if mibBuilder.loadTexts:
    configurationTable.setStatus("current")
_ConfigurationEntry_Object = MibTableRow
configurationEntry = _ConfigurationEntry_Object(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 4, 1, 3, 30, 1)
)
configurationEntry.setIndexNames(
    (0, "RS-XX8000-DVB-TX-MIB", "configTvStandardIdx"),
)
if mibBuilder.loadTexts:
    configurationEntry.setStatus("current")
_ConfigTvStandardIdx_Type = TvStandard
_ConfigTvStandardIdx_Object = MibTableColumn
configTvStandardIdx = _ConfigTvStandardIdx_Object(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 4, 1, 3, 30, 1, 3),
    _ConfigTvStandardIdx_Type()
)
configTvStandardIdx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    configTvStandardIdx.setStatus("current")
_ConfigTvStandardName_Type = TvStandard
_ConfigTvStandardName_Object = MibTableColumn
configTvStandardName = _ConfigTvStandardName_Object(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 4, 1, 3, 30, 1, 5),
    _ConfigTvStandardName_Type()
)
configTvStandardName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    configTvStandardName.setStatus("current")


class _ConfigRxFrequency_Type(Integer32):
    """Custom type configRxFrequency based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(160000000, 910000000),
    )


_ConfigRxFrequency_Type.__name__ = "Integer32"
_ConfigRxFrequency_Object = MibTableColumn
configRxFrequency = _ConfigRxFrequency_Object(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 4, 1, 3, 30, 1, 6),
    _ConfigRxFrequency_Type()
)
configRxFrequency.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configRxFrequency.setStatus("current")
if mibBuilder.loadTexts:
    configRxFrequency.setUnits("Hz")


class _ConfigFrequency_Type(Integer32):
    """Custom type configFrequency based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(47000000, 1500000000),
    )


_ConfigFrequency_Type.__name__ = "Integer32"
_ConfigFrequency_Object = MibTableColumn
configFrequency = _ConfigFrequency_Object(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 4, 1, 3, 30, 1, 7),
    _ConfigFrequency_Type()
)
configFrequency.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configFrequency.setStatus("current")
if mibBuilder.loadTexts:
    configFrequency.setUnits("Hz")
_ConfigPower_Type = FloatingPoint
_ConfigPower_Object = MibTableColumn
configPower = _ConfigPower_Object(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 4, 1, 3, 30, 1, 8),
    _ConfigPower_Type()
)
configPower.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configPower.setStatus("current")
if mibBuilder.loadTexts:
    configPower.setUnits("W")
_ConfigInputSource_Type = InputSource
_ConfigInputSource_Object = MibTableColumn
configInputSource = _ConfigInputSource_Object(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 4, 1, 3, 30, 1, 9),
    _ConfigInputSource_Type()
)
configInputSource.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configInputSource.setStatus("current")
_TimeSchedulerTable_Object = MibTable
timeSchedulerTable = _TimeSchedulerTable_Object(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 4, 1, 3, 31)
)
if mibBuilder.loadTexts:
    timeSchedulerTable.setStatus("current")
_TimeSchedulerEntry_Object = MibTableRow
timeSchedulerEntry = _TimeSchedulerEntry_Object(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 4, 1, 3, 31, 1)
)
timeSchedulerEntry.setIndexNames(
    (0, "RS-XX8000-DVB-TX-MIB", "schedulerDateTimeIdx"),
)
if mibBuilder.loadTexts:
    timeSchedulerEntry.setStatus("current")
_SchedulerDateTimeIdx_Type = DateAndTime
_SchedulerDateTimeIdx_Object = MibTableColumn
schedulerDateTimeIdx = _SchedulerDateTimeIdx_Object(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 4, 1, 3, 31, 1, 3),
    _SchedulerDateTimeIdx_Type()
)
schedulerDateTimeIdx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    schedulerDateTimeIdx.setStatus("current")
_SchedulerRowStatus_Type = RowStatus
_SchedulerRowStatus_Object = MibTableColumn
schedulerRowStatus = _SchedulerRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 4, 1, 3, 31, 1, 5),
    _SchedulerRowStatus_Type()
)
schedulerRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    schedulerRowStatus.setStatus("current")


class _SchedulerEvent_Type(Integer32):
    """Custom type schedulerEvent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("daily", 1),
          ("once", 2))
    )


_SchedulerEvent_Type.__name__ = "Integer32"
_SchedulerEvent_Object = MibTableColumn
schedulerEvent = _SchedulerEvent_Object(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 4, 1, 3, 31, 1, 6),
    _SchedulerEvent_Type()
)
schedulerEvent.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    schedulerEvent.setStatus("current")
_SchedulerDateTime_Type = DateAndTime
_SchedulerDateTime_Object = MibTableColumn
schedulerDateTime = _SchedulerDateTime_Object(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 4, 1, 3, 31, 1, 7),
    _SchedulerDateTime_Type()
)
schedulerDateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    schedulerDateTime.setStatus("current")
_SchedulerTvStandard_Type = TvStandard
_SchedulerTvStandard_Object = MibTableColumn
schedulerTvStandard = _SchedulerTvStandard_Object(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 4, 1, 3, 31, 1, 8),
    _SchedulerTvStandard_Type()
)
schedulerTvStandard.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    schedulerTvStandard.setStatus("current")
_Configuration2Table_Object = MibTable
configuration2Table = _Configuration2Table_Object(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 4, 1, 3, 32)
)
if mibBuilder.loadTexts:
    configuration2Table.setStatus("current")
_Configuration2Entry_Object = MibTableRow
configuration2Entry = _Configuration2Entry_Object(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 4, 1, 3, 32, 1)
)
if mibBuilder.loadTexts:
    configuration2Entry.setStatus("current")
_Config2TvStandardName_Type = TvStandard
_Config2TvStandardName_Object = MibTableColumn
config2TvStandardName = _Config2TvStandardName_Object(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 4, 1, 3, 32, 1, 5),
    _Config2TvStandardName_Type()
)
config2TvStandardName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    config2TvStandardName.setStatus("current")


class _Config2RxFrequency_Type(Integer32):
    """Custom type config2RxFrequency based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(160000000, 910000000),
    )


_Config2RxFrequency_Type.__name__ = "Integer32"
_Config2RxFrequency_Object = MibTableColumn
config2RxFrequency = _Config2RxFrequency_Object(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 4, 1, 3, 32, 1, 6),
    _Config2RxFrequency_Type()
)
config2RxFrequency.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    config2RxFrequency.setStatus("current")
if mibBuilder.loadTexts:
    config2RxFrequency.setUnits("Hz")


class _Config2Frequency_Type(Integer32):
    """Custom type config2Frequency based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(47000000, 1500000000),
    )


_Config2Frequency_Type.__name__ = "Integer32"
_Config2Frequency_Object = MibTableColumn
config2Frequency = _Config2Frequency_Object(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 4, 1, 3, 32, 1, 7),
    _Config2Frequency_Type()
)
config2Frequency.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    config2Frequency.setStatus("current")
if mibBuilder.loadTexts:
    config2Frequency.setUnits("Hz")
_Config2Power_Type = FloatingPoint
_Config2Power_Object = MibTableColumn
config2Power = _Config2Power_Object(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 4, 1, 3, 32, 1, 8),
    _Config2Power_Type()
)
config2Power.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    config2Power.setStatus("current")
if mibBuilder.loadTexts:
    config2Power.setUnits("W")
_Config2InputSource_Type = InputSource
_Config2InputSource_Object = MibTableColumn
config2InputSource = _Config2InputSource_Object(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 4, 1, 3, 32, 1, 9),
    _Config2InputSource_Type()
)
config2InputSource.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    config2InputSource.setStatus("current")
_ProductInfoTable_Object = MibTable
productInfoTable = _ProductInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 4, 1, 3, 100)
)
if mibBuilder.loadTexts:
    productInfoTable.setStatus("current")
_ProductInfoEntry_Object = MibTableRow
productInfoEntry = _ProductInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 4, 1, 3, 100, 1)
)
productInfoEntry.setIndexNames(
    (0, "RS-XX8000-DVB-TX-MIB", "prodInfoModuleIdx"),
    (0, "RS-XX8000-DVB-TX-MIB", "prodInfoDeviceIdx"),
    (0, "RS-XX8000-DVB-TX-MIB", "prodInfoRackIdx"),
    (0, "RS-XX8000-DVB-TX-MIB", "prodInfoAmpIdx"),
)
if mibBuilder.loadTexts:
    productInfoEntry.setStatus("current")
_ProdInfoModuleIdx_Type = ProdInfoModuleNameTv
_ProdInfoModuleIdx_Object = MibTableColumn
prodInfoModuleIdx = _ProdInfoModuleIdx_Object(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 4, 1, 3, 100, 1, 1),
    _ProdInfoModuleIdx_Type()
)
prodInfoModuleIdx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    prodInfoModuleIdx.setStatus("current")
_ProdInfoDeviceIdx_Type = IndexAB
_ProdInfoDeviceIdx_Object = MibTableColumn
prodInfoDeviceIdx = _ProdInfoDeviceIdx_Object(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 4, 1, 3, 100, 1, 2),
    _ProdInfoDeviceIdx_Type()
)
prodInfoDeviceIdx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    prodInfoDeviceIdx.setStatus("current")
_ProdInfoRackIdx_Type = IndexRack
_ProdInfoRackIdx_Object = MibTableColumn
prodInfoRackIdx = _ProdInfoRackIdx_Object(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 4, 1, 3, 100, 1, 3),
    _ProdInfoRackIdx_Type()
)
prodInfoRackIdx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    prodInfoRackIdx.setStatus("current")
_ProdInfoAmpIdx_Type = IndexAmplifier
_ProdInfoAmpIdx_Object = MibTableColumn
prodInfoAmpIdx = _ProdInfoAmpIdx_Object(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 4, 1, 3, 100, 1, 4),
    _ProdInfoAmpIdx_Type()
)
prodInfoAmpIdx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    prodInfoAmpIdx.setStatus("current")
_ProdInfoModuleName_Type = ProdInfoModuleNameTv
_ProdInfoModuleName_Object = MibTableColumn
prodInfoModuleName = _ProdInfoModuleName_Object(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 4, 1, 3, 100, 1, 5),
    _ProdInfoModuleName_Type()
)
prodInfoModuleName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prodInfoModuleName.setStatus("current")
_ProdInfoSerialNumber_Type = ReadableString
_ProdInfoSerialNumber_Object = MibTableColumn
prodInfoSerialNumber = _ProdInfoSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 4, 1, 3, 100, 1, 6),
    _ProdInfoSerialNumber_Type()
)
prodInfoSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prodInfoSerialNumber.setStatus("current")
_ProdInfoIdentNumberSW_Type = ReadableString
_ProdInfoIdentNumberSW_Object = MibTableColumn
prodInfoIdentNumberSW = _ProdInfoIdentNumberSW_Object(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 4, 1, 3, 100, 1, 7),
    _ProdInfoIdentNumberSW_Type()
)
prodInfoIdentNumberSW.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prodInfoIdentNumberSW.setStatus("current")
_ProdInfoVersionNumberSW_Type = ReadableString
_ProdInfoVersionNumberSW_Object = MibTableColumn
prodInfoVersionNumberSW = _ProdInfoVersionNumberSW_Object(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 4, 1, 3, 100, 1, 8),
    _ProdInfoVersionNumberSW_Type()
)
prodInfoVersionNumberSW.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prodInfoVersionNumberSW.setStatus("current")
_ProdInfoIdentNumberHW_Type = ReadableString
_ProdInfoIdentNumberHW_Object = MibTableColumn
prodInfoIdentNumberHW = _ProdInfoIdentNumberHW_Object(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 4, 1, 3, 100, 1, 9),
    _ProdInfoIdentNumberHW_Type()
)
prodInfoIdentNumberHW.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prodInfoIdentNumberHW.setStatus("current")
_ProdInfoVersionNumberHW_Type = ReadableString
_ProdInfoVersionNumberHW_Object = MibTableColumn
prodInfoVersionNumberHW = _ProdInfoVersionNumberHW_Object(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 4, 1, 3, 100, 1, 10),
    _ProdInfoVersionNumberHW_Type()
)
prodInfoVersionNumberHW.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prodInfoVersionNumberHW.setStatus("current")
_ProductInfoProductDateHW_Type = DateAndTime
_ProductInfoProductDateHW_Object = MibTableColumn
productInfoProductDateHW = _ProductInfoProductDateHW_Object(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 4, 1, 3, 100, 1, 11),
    _ProductInfoProductDateHW_Type()
)
productInfoProductDateHW.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    productInfoProductDateHW.setStatus("current")
_Logbook_ObjectIdentity = ObjectIdentity
logbook = _Logbook_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 4, 1, 4)
)
_NetCCUNumberOfEntries_Type = LogbookMaxEntryNumber
_NetCCUNumberOfEntries_Object = MibScalar
netCCUNumberOfEntries = _NetCCUNumberOfEntries_Object(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 4, 1, 4, 1),
    _NetCCUNumberOfEntries_Type()
)
netCCUNumberOfEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netCCUNumberOfEntries.setStatus("current")
_NetCCULogbookClear_Type = Trigger
_NetCCULogbookClear_Object = MibScalar
netCCULogbookClear = _NetCCULogbookClear_Object(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 4, 1, 4, 2),
    _NetCCULogbookClear_Type()
)
netCCULogbookClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    netCCULogbookClear.setStatus("current")
_NetCCULogbookTable_Object = MibTable
netCCULogbookTable = _NetCCULogbookTable_Object(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 4, 1, 4, 3)
)
if mibBuilder.loadTexts:
    netCCULogbookTable.setStatus("current")
_NetCCULogbookEntry_Object = MibTableRow
netCCULogbookEntry = _NetCCULogbookEntry_Object(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 4, 1, 4, 3, 1)
)
netCCULogbookEntry.setIndexNames(
    (0, "RS-XX8000-DVB-TX-MIB", "netCCULogbookEntryIdx"),
)
if mibBuilder.loadTexts:
    netCCULogbookEntry.setStatus("current")
_NetCCULogbookEntryIdx_Type = LogbookMaxEntryNumber
_NetCCULogbookEntryIdx_Object = MibTableColumn
netCCULogbookEntryIdx = _NetCCULogbookEntryIdx_Object(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 4, 1, 4, 3, 1, 1),
    _NetCCULogbookEntryIdx_Type()
)
netCCULogbookEntryIdx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    netCCULogbookEntryIdx.setStatus("current")
_NetCCULogbookEntryNbr_Type = LogbookMaxEntryNumber
_NetCCULogbookEntryNbr_Object = MibTableColumn
netCCULogbookEntryNbr = _NetCCULogbookEntryNbr_Object(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 4, 1, 4, 3, 1, 2),
    _NetCCULogbookEntryNbr_Type()
)
netCCULogbookEntryNbr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netCCULogbookEntryNbr.setStatus("current")
_NetCCULogbookType_Type = EventClass
_NetCCULogbookType_Object = MibTableColumn
netCCULogbookType = _NetCCULogbookType_Object(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 4, 1, 4, 3, 1, 3),
    _NetCCULogbookType_Type()
)
netCCULogbookType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netCCULogbookType.setStatus("current")
_NetCCULogbookSlope_Type = LogbookEntrySlope
_NetCCULogbookSlope_Object = MibTableColumn
netCCULogbookSlope = _NetCCULogbookSlope_Object(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 4, 1, 4, 3, 1, 4),
    _NetCCULogbookSlope_Type()
)
netCCULogbookSlope.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netCCULogbookSlope.setStatus("current")
_NetCCULogbookMessage_Type = LogbookEntryMessagesNetCCU
_NetCCULogbookMessage_Object = MibTableColumn
netCCULogbookMessage = _NetCCULogbookMessage_Object(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 4, 1, 4, 3, 1, 5),
    _NetCCULogbookMessage_Type()
)
netCCULogbookMessage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netCCULogbookMessage.setStatus("current")
_NetCCULogbookDateTime_Type = DateAndTime
_NetCCULogbookDateTime_Object = MibTableColumn
netCCULogbookDateTime = _NetCCULogbookDateTime_Object(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 4, 1, 4, 3, 1, 6),
    _NetCCULogbookDateTime_Type()
)
netCCULogbookDateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netCCULogbookDateTime.setStatus("current")
_ExciterANumberOfEntries_Type = LogbookMaxEntryNumber
_ExciterANumberOfEntries_Object = MibScalar
exciterANumberOfEntries = _ExciterANumberOfEntries_Object(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 4, 1, 4, 4),
    _ExciterANumberOfEntries_Type()
)
exciterANumberOfEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exciterANumberOfEntries.setStatus("current")
_ExciterALogbookClear_Type = Trigger
_ExciterALogbookClear_Object = MibScalar
exciterALogbookClear = _ExciterALogbookClear_Object(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 4, 1, 4, 5),
    _ExciterALogbookClear_Type()
)
exciterALogbookClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    exciterALogbookClear.setStatus("current")
_ExciterALogbookTable_Object = MibTable
exciterALogbookTable = _ExciterALogbookTable_Object(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 4, 1, 4, 6)
)
if mibBuilder.loadTexts:
    exciterALogbookTable.setStatus("current")
_ExciterALogbookEntry_Object = MibTableRow
exciterALogbookEntry = _ExciterALogbookEntry_Object(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 4, 1, 4, 6, 1)
)
exciterALogbookEntry.setIndexNames(
    (0, "RS-XX8000-DVB-TX-MIB", "excALogbookEntryIdx"),
)
if mibBuilder.loadTexts:
    exciterALogbookEntry.setStatus("current")
_ExcALogbookEntryIdx_Type = LogbookMaxEntryNumber
_ExcALogbookEntryIdx_Object = MibTableColumn
excALogbookEntryIdx = _ExcALogbookEntryIdx_Object(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 4, 1, 4, 6, 1, 1),
    _ExcALogbookEntryIdx_Type()
)
excALogbookEntryIdx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    excALogbookEntryIdx.setStatus("current")
_ExcALogbookEntryNbr_Type = LogbookMaxEntryNumber
_ExcALogbookEntryNbr_Object = MibTableColumn
excALogbookEntryNbr = _ExcALogbookEntryNbr_Object(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 4, 1, 4, 6, 1, 2),
    _ExcALogbookEntryNbr_Type()
)
excALogbookEntryNbr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    excALogbookEntryNbr.setStatus("current")
_ExcALogbookType_Type = EventClass
_ExcALogbookType_Object = MibTableColumn
excALogbookType = _ExcALogbookType_Object(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 4, 1, 4, 6, 1, 3),
    _ExcALogbookType_Type()
)
excALogbookType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    excALogbookType.setStatus("current")
_ExcALogbookSlope_Type = LogbookEntrySlope
_ExcALogbookSlope_Object = MibTableColumn
excALogbookSlope = _ExcALogbookSlope_Object(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 4, 1, 4, 6, 1, 4),
    _ExcALogbookSlope_Type()
)
excALogbookSlope.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    excALogbookSlope.setStatus("current")
_ExcALogbookMessage_Type = LogbookEntryMessagesExcTv
_ExcALogbookMessage_Object = MibTableColumn
excALogbookMessage = _ExcALogbookMessage_Object(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 4, 1, 4, 6, 1, 5),
    _ExcALogbookMessage_Type()
)
excALogbookMessage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    excALogbookMessage.setStatus("current")
_ExcALogbookDateTime_Type = DateAndTime
_ExcALogbookDateTime_Object = MibTableColumn
excALogbookDateTime = _ExcALogbookDateTime_Object(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 4, 1, 4, 6, 1, 6),
    _ExcALogbookDateTime_Type()
)
excALogbookDateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    excALogbookDateTime.setStatus("current")
_OutputstageANumberOfEntries_Type = LogbookMaxEntryNumber
_OutputstageANumberOfEntries_Object = MibScalar
outputstageANumberOfEntries = _OutputstageANumberOfEntries_Object(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 4, 1, 4, 7),
    _OutputstageANumberOfEntries_Type()
)
outputstageANumberOfEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outputstageANumberOfEntries.setStatus("current")
_OutputstageALogbookClear_Type = Trigger
_OutputstageALogbookClear_Object = MibScalar
outputstageALogbookClear = _OutputstageALogbookClear_Object(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 4, 1, 4, 8),
    _OutputstageALogbookClear_Type()
)
outputstageALogbookClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outputstageALogbookClear.setStatus("current")
_OutputstageALogbookTable_Object = MibTable
outputstageALogbookTable = _OutputstageALogbookTable_Object(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 4, 1, 4, 9)
)
if mibBuilder.loadTexts:
    outputstageALogbookTable.setStatus("current")
_OutputstageALogbookEntry_Object = MibTableRow
outputstageALogbookEntry = _OutputstageALogbookEntry_Object(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 4, 1, 4, 9, 1)
)
outputstageALogbookEntry.setIndexNames(
    (0, "RS-XX8000-DVB-TX-MIB", "ostALogbookEntryIdx"),
)
if mibBuilder.loadTexts:
    outputstageALogbookEntry.setStatus("current")
_OstALogbookEntryIdx_Type = LogbookMaxEntryNumber
_OstALogbookEntryIdx_Object = MibTableColumn
ostALogbookEntryIdx = _OstALogbookEntryIdx_Object(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 4, 1, 4, 9, 1, 1),
    _OstALogbookEntryIdx_Type()
)
ostALogbookEntryIdx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ostALogbookEntryIdx.setStatus("current")
_OstALogbookEntryNbr_Type = LogbookMaxEntryNumber
_OstALogbookEntryNbr_Object = MibTableColumn
ostALogbookEntryNbr = _OstALogbookEntryNbr_Object(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 4, 1, 4, 9, 1, 2),
    _OstALogbookEntryNbr_Type()
)
ostALogbookEntryNbr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ostALogbookEntryNbr.setStatus("current")
_OstALogbookType_Type = EventClass
_OstALogbookType_Object = MibTableColumn
ostALogbookType = _OstALogbookType_Object(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 4, 1, 4, 9, 1, 3),
    _OstALogbookType_Type()
)
ostALogbookType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ostALogbookType.setStatus("current")
_OstALogbookSlope_Type = LogbookEntrySlope
_OstALogbookSlope_Object = MibTableColumn
ostALogbookSlope = _OstALogbookSlope_Object(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 4, 1, 4, 9, 1, 4),
    _OstALogbookSlope_Type()
)
ostALogbookSlope.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ostALogbookSlope.setStatus("current")
_OstALogbookMessage_Type = LogbookEntryMessagesOST
_OstALogbookMessage_Object = MibTableColumn
ostALogbookMessage = _OstALogbookMessage_Object(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 4, 1, 4, 9, 1, 5),
    _OstALogbookMessage_Type()
)
ostALogbookMessage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ostALogbookMessage.setStatus("current")
_OstALogbookDateTime_Type = DateAndTime
_OstALogbookDateTime_Object = MibTableColumn
ostALogbookDateTime = _OstALogbookDateTime_Object(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 4, 1, 4, 9, 1, 6),
    _OstALogbookDateTime_Type()
)
ostALogbookDateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ostALogbookDateTime.setStatus("current")
_ExciterBNumberOfEntries_Type = LogbookMaxEntryNumber
_ExciterBNumberOfEntries_Object = MibScalar
exciterBNumberOfEntries = _ExciterBNumberOfEntries_Object(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 4, 1, 4, 10),
    _ExciterBNumberOfEntries_Type()
)
exciterBNumberOfEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    exciterBNumberOfEntries.setStatus("current")
_ExciterBLogbookClear_Type = Trigger
_ExciterBLogbookClear_Object = MibScalar
exciterBLogbookClear = _ExciterBLogbookClear_Object(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 4, 1, 4, 11),
    _ExciterBLogbookClear_Type()
)
exciterBLogbookClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    exciterBLogbookClear.setStatus("current")
_ExciterBLogbookTable_Object = MibTable
exciterBLogbookTable = _ExciterBLogbookTable_Object(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 4, 1, 4, 12)
)
if mibBuilder.loadTexts:
    exciterBLogbookTable.setStatus("current")
_ExciterBLogbookEntry_Object = MibTableRow
exciterBLogbookEntry = _ExciterBLogbookEntry_Object(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 4, 1, 4, 12, 1)
)
exciterBLogbookEntry.setIndexNames(
    (0, "RS-XX8000-DVB-TX-MIB", "excBLogbookEntryIdx"),
)
if mibBuilder.loadTexts:
    exciterBLogbookEntry.setStatus("current")
_ExcBLogbookEntryIdx_Type = LogbookMaxEntryNumber
_ExcBLogbookEntryIdx_Object = MibTableColumn
excBLogbookEntryIdx = _ExcBLogbookEntryIdx_Object(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 4, 1, 4, 12, 1, 1),
    _ExcBLogbookEntryIdx_Type()
)
excBLogbookEntryIdx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    excBLogbookEntryIdx.setStatus("current")
_ExcBLogbookEntryNbr_Type = LogbookMaxEntryNumber
_ExcBLogbookEntryNbr_Object = MibTableColumn
excBLogbookEntryNbr = _ExcBLogbookEntryNbr_Object(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 4, 1, 4, 12, 1, 2),
    _ExcBLogbookEntryNbr_Type()
)
excBLogbookEntryNbr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    excBLogbookEntryNbr.setStatus("current")
_ExcBLogbookType_Type = EventClass
_ExcBLogbookType_Object = MibTableColumn
excBLogbookType = _ExcBLogbookType_Object(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 4, 1, 4, 12, 1, 3),
    _ExcBLogbookType_Type()
)
excBLogbookType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    excBLogbookType.setStatus("current")
_ExcBLogbookSlope_Type = LogbookEntrySlope
_ExcBLogbookSlope_Object = MibTableColumn
excBLogbookSlope = _ExcBLogbookSlope_Object(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 4, 1, 4, 12, 1, 4),
    _ExcBLogbookSlope_Type()
)
excBLogbookSlope.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    excBLogbookSlope.setStatus("current")
_ExcBLogbookMessage_Type = LogbookEntryMessagesExcTv
_ExcBLogbookMessage_Object = MibTableColumn
excBLogbookMessage = _ExcBLogbookMessage_Object(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 4, 1, 4, 12, 1, 5),
    _ExcBLogbookMessage_Type()
)
excBLogbookMessage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    excBLogbookMessage.setStatus("current")
_ExcBLogbookDateTime_Type = DateAndTime
_ExcBLogbookDateTime_Object = MibTableColumn
excBLogbookDateTime = _ExcBLogbookDateTime_Object(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 4, 1, 4, 12, 1, 6),
    _ExcBLogbookDateTime_Type()
)
excBLogbookDateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    excBLogbookDateTime.setStatus("current")
_OutputstageBNumberOfEntries_Type = LogbookMaxEntryNumber
_OutputstageBNumberOfEntries_Object = MibScalar
outputstageBNumberOfEntries = _OutputstageBNumberOfEntries_Object(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 4, 1, 4, 13),
    _OutputstageBNumberOfEntries_Type()
)
outputstageBNumberOfEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outputstageBNumberOfEntries.setStatus("current")
_OutputstageBLogbookClear_Type = Trigger
_OutputstageBLogbookClear_Object = MibScalar
outputstageBLogbookClear = _OutputstageBLogbookClear_Object(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 4, 1, 4, 14),
    _OutputstageBLogbookClear_Type()
)
outputstageBLogbookClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outputstageBLogbookClear.setStatus("current")
_OutputstageBLogbookTable_Object = MibTable
outputstageBLogbookTable = _OutputstageBLogbookTable_Object(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 4, 1, 4, 15)
)
if mibBuilder.loadTexts:
    outputstageBLogbookTable.setStatus("current")
_OutputstageBLogbookEntry_Object = MibTableRow
outputstageBLogbookEntry = _OutputstageBLogbookEntry_Object(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 4, 1, 4, 15, 1)
)
outputstageBLogbookEntry.setIndexNames(
    (0, "RS-XX8000-DVB-TX-MIB", "ostBLogbookEntryIdx"),
)
if mibBuilder.loadTexts:
    outputstageBLogbookEntry.setStatus("current")
_OstBLogbookEntryIdx_Type = LogbookMaxEntryNumber
_OstBLogbookEntryIdx_Object = MibTableColumn
ostBLogbookEntryIdx = _OstBLogbookEntryIdx_Object(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 4, 1, 4, 15, 1, 1),
    _OstBLogbookEntryIdx_Type()
)
ostBLogbookEntryIdx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ostBLogbookEntryIdx.setStatus("current")
_OstBLogbookEntryNbr_Type = LogbookMaxEntryNumber
_OstBLogbookEntryNbr_Object = MibTableColumn
ostBLogbookEntryNbr = _OstBLogbookEntryNbr_Object(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 4, 1, 4, 15, 1, 2),
    _OstBLogbookEntryNbr_Type()
)
ostBLogbookEntryNbr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ostBLogbookEntryNbr.setStatus("current")
_OstBLogbookType_Type = EventClass
_OstBLogbookType_Object = MibTableColumn
ostBLogbookType = _OstBLogbookType_Object(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 4, 1, 4, 15, 1, 3),
    _OstBLogbookType_Type()
)
ostBLogbookType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ostBLogbookType.setStatus("current")
_OstBLogbookSlope_Type = LogbookEntrySlope
_OstBLogbookSlope_Object = MibTableColumn
ostBLogbookSlope = _OstBLogbookSlope_Object(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 4, 1, 4, 15, 1, 4),
    _OstBLogbookSlope_Type()
)
ostBLogbookSlope.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ostBLogbookSlope.setStatus("current")
_OstBLogbookMessage_Type = LogbookEntryMessagesOST
_OstBLogbookMessage_Object = MibTableColumn
ostBLogbookMessage = _OstBLogbookMessage_Object(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 4, 1, 4, 15, 1, 5),
    _OstBLogbookMessage_Type()
)
ostBLogbookMessage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ostBLogbookMessage.setStatus("current")
_OstBLogbookDateTime_Type = DateAndTime
_OstBLogbookDateTime_Object = MibTableColumn
ostBLogbookDateTime = _OstBLogbookDateTime_Object(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 4, 1, 4, 15, 1, 6),
    _OstBLogbookDateTime_Type()
)
ostBLogbookDateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ostBLogbookDateTime.setStatus("current")
_RfProbesTable_Object = MibTable
rfProbesTable = _RfProbesTable_Object(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 4, 1, 5)
)
if mibBuilder.loadTexts:
    rfProbesTable.setStatus("current")
_RfProbesEntry_Object = MibTableRow
rfProbesEntry = _RfProbesEntry_Object(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 4, 1, 5, 1)
)
rfProbesEntry.setIndexNames(
    (0, "RS-XX8000-DVB-TX-MIB", "rfProbesOstIdx"),
)
if mibBuilder.loadTexts:
    rfProbesEntry.setStatus("current")
_RfProbesNetCCURfProbe1_Type = FloatingPoint
_RfProbesNetCCURfProbe1_Object = MibTableColumn
rfProbesNetCCURfProbe1 = _RfProbesNetCCURfProbe1_Object(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 4, 1, 5, 1, 1),
    _RfProbesNetCCURfProbe1_Type()
)
rfProbesNetCCURfProbe1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rfProbesNetCCURfProbe1.setStatus("current")
if mibBuilder.loadTexts:
    rfProbesNetCCURfProbe1.setUnits("Volt")
_RfProbesNetCCURfProbe2_Type = FloatingPoint
_RfProbesNetCCURfProbe2_Object = MibTableColumn
rfProbesNetCCURfProbe2 = _RfProbesNetCCURfProbe2_Object(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 4, 1, 5, 1, 2),
    _RfProbesNetCCURfProbe2_Type()
)
rfProbesNetCCURfProbe2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rfProbesNetCCURfProbe2.setStatus("current")
if mibBuilder.loadTexts:
    rfProbesNetCCURfProbe2.setUnits("Volt")
_RfProbesAntFwdNominal_Type = FloatingPoint
_RfProbesAntFwdNominal_Object = MibTableColumn
rfProbesAntFwdNominal = _RfProbesAntFwdNominal_Object(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 4, 1, 5, 1, 3),
    _RfProbesAntFwdNominal_Type()
)
rfProbesAntFwdNominal.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rfProbesAntFwdNominal.setStatus("current")
if mibBuilder.loadTexts:
    rfProbesAntFwdNominal.setUnits("Watt")
_RfProbesAntFwdWarningLimit_Type = FloatingPoint
_RfProbesAntFwdWarningLimit_Object = MibTableColumn
rfProbesAntFwdWarningLimit = _RfProbesAntFwdWarningLimit_Object(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 4, 1, 5, 1, 4),
    _RfProbesAntFwdWarningLimit_Type()
)
rfProbesAntFwdWarningLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rfProbesAntFwdWarningLimit.setStatus("current")
if mibBuilder.loadTexts:
    rfProbesAntFwdWarningLimit.setUnits("dB")
_RfProbesAntFwdFailLimit_Type = FloatingPoint
_RfProbesAntFwdFailLimit_Object = MibTableColumn
rfProbesAntFwdFailLimit = _RfProbesAntFwdFailLimit_Object(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 4, 1, 5, 1, 5),
    _RfProbesAntFwdFailLimit_Type()
)
rfProbesAntFwdFailLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rfProbesAntFwdFailLimit.setStatus("current")
if mibBuilder.loadTexts:
    rfProbesAntFwdFailLimit.setUnits("dB")


class _RfProbesAntFwdDelayTimeRfFail_Type(Integer32):
    """Custom type rfProbesAntFwdDelayTimeRfFail based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 20),
    )


_RfProbesAntFwdDelayTimeRfFail_Type.__name__ = "Integer32"
_RfProbesAntFwdDelayTimeRfFail_Object = MibTableColumn
rfProbesAntFwdDelayTimeRfFail = _RfProbesAntFwdDelayTimeRfFail_Object(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 4, 1, 5, 1, 6),
    _RfProbesAntFwdDelayTimeRfFail_Type()
)
rfProbesAntFwdDelayTimeRfFail.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rfProbesAntFwdDelayTimeRfFail.setStatus("current")
if mibBuilder.loadTexts:
    rfProbesAntFwdDelayTimeRfFail.setUnits("seconds")
_RfProbesAntFwdSetOffset_Type = Trigger
_RfProbesAntFwdSetOffset_Object = MibTableColumn
rfProbesAntFwdSetOffset = _RfProbesAntFwdSetOffset_Object(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 4, 1, 5, 1, 7),
    _RfProbesAntFwdSetOffset_Type()
)
rfProbesAntFwdSetOffset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rfProbesAntFwdSetOffset.setStatus("current")
_RfProbesAntFwdSetGain_Type = Trigger
_RfProbesAntFwdSetGain_Object = MibTableColumn
rfProbesAntFwdSetGain = _RfProbesAntFwdSetGain_Object(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 4, 1, 5, 1, 8),
    _RfProbesAntFwdSetGain_Type()
)
rfProbesAntFwdSetGain.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rfProbesAntFwdSetGain.setStatus("current")
_RfProbesAntReflWarningLimit_Type = FloatingPoint
_RfProbesAntReflWarningLimit_Object = MibTableColumn
rfProbesAntReflWarningLimit = _RfProbesAntReflWarningLimit_Object(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 4, 1, 5, 1, 9),
    _RfProbesAntReflWarningLimit_Type()
)
rfProbesAntReflWarningLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rfProbesAntReflWarningLimit.setStatus("current")
if mibBuilder.loadTexts:
    rfProbesAntReflWarningLimit.setUnits("dB")
_RfProbesAntReflSetOffset_Type = Trigger
_RfProbesAntReflSetOffset_Object = MibTableColumn
rfProbesAntReflSetOffset = _RfProbesAntReflSetOffset_Object(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 4, 1, 5, 1, 10),
    _RfProbesAntReflSetOffset_Type()
)
rfProbesAntReflSetOffset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rfProbesAntReflSetOffset.setStatus("current")
_RfProbesAntReflSetGain_Type = Trigger
_RfProbesAntReflSetGain_Object = MibTableColumn
rfProbesAntReflSetGain = _RfProbesAntReflSetGain_Object(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 4, 1, 5, 1, 11),
    _RfProbesAntReflSetGain_Type()
)
rfProbesAntReflSetGain.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rfProbesAntReflSetGain.setStatus("current")
_RfProbesDLFwdNominal_Type = FloatingPoint
_RfProbesDLFwdNominal_Object = MibTableColumn
rfProbesDLFwdNominal = _RfProbesDLFwdNominal_Object(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 4, 1, 5, 1, 12),
    _RfProbesDLFwdNominal_Type()
)
rfProbesDLFwdNominal.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rfProbesDLFwdNominal.setStatus("current")
if mibBuilder.loadTexts:
    rfProbesDLFwdNominal.setUnits("Watt")
_RfProbesDLFwdWarningLimit_Type = FloatingPoint
_RfProbesDLFwdWarningLimit_Object = MibTableColumn
rfProbesDLFwdWarningLimit = _RfProbesDLFwdWarningLimit_Object(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 4, 1, 5, 1, 13),
    _RfProbesDLFwdWarningLimit_Type()
)
rfProbesDLFwdWarningLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rfProbesDLFwdWarningLimit.setStatus("current")
if mibBuilder.loadTexts:
    rfProbesDLFwdWarningLimit.setUnits("dB")
_RfProbesDLFwdFailLimit_Type = FloatingPoint
_RfProbesDLFwdFailLimit_Object = MibTableColumn
rfProbesDLFwdFailLimit = _RfProbesDLFwdFailLimit_Object(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 4, 1, 5, 1, 14),
    _RfProbesDLFwdFailLimit_Type()
)
rfProbesDLFwdFailLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rfProbesDLFwdFailLimit.setStatus("current")
if mibBuilder.loadTexts:
    rfProbesDLFwdFailLimit.setUnits("dB")


class _RfProbesDLFwdDelayTimeRfFail_Type(Integer32):
    """Custom type rfProbesDLFwdDelayTimeRfFail based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 20),
    )


_RfProbesDLFwdDelayTimeRfFail_Type.__name__ = "Integer32"
_RfProbesDLFwdDelayTimeRfFail_Object = MibTableColumn
rfProbesDLFwdDelayTimeRfFail = _RfProbesDLFwdDelayTimeRfFail_Object(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 4, 1, 5, 1, 15),
    _RfProbesDLFwdDelayTimeRfFail_Type()
)
rfProbesDLFwdDelayTimeRfFail.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rfProbesDLFwdDelayTimeRfFail.setStatus("current")
if mibBuilder.loadTexts:
    rfProbesDLFwdDelayTimeRfFail.setUnits("seconds")
_RfProbesDLFwdSetOffset_Type = Trigger
_RfProbesDLFwdSetOffset_Object = MibTableColumn
rfProbesDLFwdSetOffset = _RfProbesDLFwdSetOffset_Object(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 4, 1, 5, 1, 16),
    _RfProbesDLFwdSetOffset_Type()
)
rfProbesDLFwdSetOffset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rfProbesDLFwdSetOffset.setStatus("current")
_RfProbesDLFwdSetGain_Type = Trigger
_RfProbesDLFwdSetGain_Object = MibTableColumn
rfProbesDLFwdSetGain = _RfProbesDLFwdSetGain_Object(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 4, 1, 5, 1, 17),
    _RfProbesDLFwdSetGain_Type()
)
rfProbesDLFwdSetGain.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rfProbesDLFwdSetGain.setStatus("current")
_RfProbesDLReflWarningLimit_Type = FloatingPoint
_RfProbesDLReflWarningLimit_Object = MibTableColumn
rfProbesDLReflWarningLimit = _RfProbesDLReflWarningLimit_Object(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 4, 1, 5, 1, 18),
    _RfProbesDLReflWarningLimit_Type()
)
rfProbesDLReflWarningLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rfProbesDLReflWarningLimit.setStatus("current")
if mibBuilder.loadTexts:
    rfProbesDLReflWarningLimit.setUnits("dB")
_RfProbesDLReflSetOffset_Type = Trigger
_RfProbesDLReflSetOffset_Object = MibTableColumn
rfProbesDLReflSetOffset = _RfProbesDLReflSetOffset_Object(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 4, 1, 5, 1, 19),
    _RfProbesDLReflSetOffset_Type()
)
rfProbesDLReflSetOffset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rfProbesDLReflSetOffset.setStatus("current")
_RfProbesDLReflSetGain_Type = Trigger
_RfProbesDLReflSetGain_Object = MibTableColumn
rfProbesDLReflSetGain = _RfProbesDLReflSetGain_Object(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 4, 1, 5, 1, 20),
    _RfProbesDLReflSetGain_Type()
)
rfProbesDLReflSetGain.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rfProbesDLReflSetGain.setStatus("current")
_RfProbesOstIdx_Type = IndexAB
_RfProbesOstIdx_Object = MibTableColumn
rfProbesOstIdx = _RfProbesOstIdx_Object(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 4, 1, 5, 1, 21),
    _RfProbesOstIdx_Type()
)
rfProbesOstIdx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rfProbesOstIdx.setStatus("current")
_RfProbesOstFwdNominal_Type = FloatingPoint
_RfProbesOstFwdNominal_Object = MibTableColumn
rfProbesOstFwdNominal = _RfProbesOstFwdNominal_Object(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 4, 1, 5, 1, 22),
    _RfProbesOstFwdNominal_Type()
)
rfProbesOstFwdNominal.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rfProbesOstFwdNominal.setStatus("current")
if mibBuilder.loadTexts:
    rfProbesOstFwdNominal.setUnits("Watt")
_RfProbesOstFwdWarningLimit_Type = FloatingPoint
_RfProbesOstFwdWarningLimit_Object = MibTableColumn
rfProbesOstFwdWarningLimit = _RfProbesOstFwdWarningLimit_Object(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 4, 1, 5, 1, 23),
    _RfProbesOstFwdWarningLimit_Type()
)
rfProbesOstFwdWarningLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rfProbesOstFwdWarningLimit.setStatus("current")
if mibBuilder.loadTexts:
    rfProbesOstFwdWarningLimit.setUnits("dB")
_RfProbesOstFwdFailLimit_Type = FloatingPoint
_RfProbesOstFwdFailLimit_Object = MibTableColumn
rfProbesOstFwdFailLimit = _RfProbesOstFwdFailLimit_Object(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 4, 1, 5, 1, 24),
    _RfProbesOstFwdFailLimit_Type()
)
rfProbesOstFwdFailLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rfProbesOstFwdFailLimit.setStatus("current")
if mibBuilder.loadTexts:
    rfProbesOstFwdFailLimit.setUnits("dB")


class _RfProbesOstFwdDelayTimeRfFail_Type(Integer32):
    """Custom type rfProbesOstFwdDelayTimeRfFail based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 20),
    )


_RfProbesOstFwdDelayTimeRfFail_Type.__name__ = "Integer32"
_RfProbesOstFwdDelayTimeRfFail_Object = MibTableColumn
rfProbesOstFwdDelayTimeRfFail = _RfProbesOstFwdDelayTimeRfFail_Object(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 4, 1, 5, 1, 25),
    _RfProbesOstFwdDelayTimeRfFail_Type()
)
rfProbesOstFwdDelayTimeRfFail.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rfProbesOstFwdDelayTimeRfFail.setStatus("current")
if mibBuilder.loadTexts:
    rfProbesOstFwdDelayTimeRfFail.setUnits("seconds")
_RfProbesOstFwdSetOffset_Type = Trigger
_RfProbesOstFwdSetOffset_Object = MibTableColumn
rfProbesOstFwdSetOffset = _RfProbesOstFwdSetOffset_Object(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 4, 1, 5, 1, 26),
    _RfProbesOstFwdSetOffset_Type()
)
rfProbesOstFwdSetOffset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rfProbesOstFwdSetOffset.setStatus("current")
_RfProbesOstFwdSetGain_Type = Trigger
_RfProbesOstFwdSetGain_Object = MibTableColumn
rfProbesOstFwdSetGain = _RfProbesOstFwdSetGain_Object(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 4, 1, 5, 1, 27),
    _RfProbesOstFwdSetGain_Type()
)
rfProbesOstFwdSetGain.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rfProbesOstFwdSetGain.setStatus("current")
_RfProbesOstReflWarningLimit_Type = FloatingPoint
_RfProbesOstReflWarningLimit_Object = MibTableColumn
rfProbesOstReflWarningLimit = _RfProbesOstReflWarningLimit_Object(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 4, 1, 5, 1, 28),
    _RfProbesOstReflWarningLimit_Type()
)
rfProbesOstReflWarningLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rfProbesOstReflWarningLimit.setStatus("current")
if mibBuilder.loadTexts:
    rfProbesOstReflWarningLimit.setUnits("dB")
_RfProbesOstReflSetOffset_Type = Trigger
_RfProbesOstReflSetOffset_Object = MibTableColumn
rfProbesOstReflSetOffset = _RfProbesOstReflSetOffset_Object(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 4, 1, 5, 1, 29),
    _RfProbesOstReflSetOffset_Type()
)
rfProbesOstReflSetOffset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rfProbesOstReflSetOffset.setStatus("current")
_RfProbesOstReflSetGain_Type = Trigger
_RfProbesOstReflSetGain_Object = MibTableColumn
rfProbesOstReflSetGain = _RfProbesOstReflSetGain_Object(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 4, 1, 5, 1, 30),
    _RfProbesOstReflSetGain_Type()
)
rfProbesOstReflSetGain.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rfProbesOstReflSetGain.setStatus("current")
_RackTable_Object = MibTable
rackTable = _RackTable_Object(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 4, 1, 6)
)
if mibBuilder.loadTexts:
    rackTable.setStatus("current")
_RackEntry_Object = MibTableRow
rackEntry = _RackEntry_Object(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 4, 1, 6, 1)
)
rackEntry.setIndexNames(
    (0, "RS-XX8000-DVB-TX-MIB", "ostDeviceIdx"),
    (0, "RS-XX8000-DVB-TX-MIB", "rackIdx"),
    (0, "RS-XX8000-DVB-TX-MIB", "rackRfProbeIdx"),
)
if mibBuilder.loadTexts:
    rackEntry.setStatus("current")
_OstDeviceIdx_Type = IndexAB
_OstDeviceIdx_Object = MibTableColumn
ostDeviceIdx = _OstDeviceIdx_Object(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 4, 1, 6, 1, 2),
    _OstDeviceIdx_Type()
)
ostDeviceIdx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ostDeviceIdx.setStatus("current")
_RackIdx_Type = IndexRack
_RackIdx_Object = MibTableColumn
rackIdx = _RackIdx_Object(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 4, 1, 6, 1, 3),
    _RackIdx_Type()
)
rackIdx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rackIdx.setStatus("current")


class _RackRfProbeIdx_Type(Integer32):
    """Custom type rackRfProbeIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("forward", 1),
          ("reflected", 2))
    )


_RackRfProbeIdx_Type.__name__ = "Integer32"
_RackRfProbeIdx_Object = MibTableColumn
rackRfProbeIdx = _RackRfProbeIdx_Object(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 4, 1, 6, 1, 4),
    _RackRfProbeIdx_Type()
)
rackRfProbeIdx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rackRfProbeIdx.setStatus("current")


class _AmplifiersPerRack_Type(Integer32):
    """Custom type amplifiersPerRack based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_AmplifiersPerRack_Type.__name__ = "Integer32"
_AmplifiersPerRack_Object = MibTableColumn
amplifiersPerRack = _AmplifiersPerRack_Object(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 4, 1, 6, 1, 6),
    _AmplifiersPerRack_Type()
)
amplifiersPerRack.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    amplifiersPerRack.setStatus("current")
_RackRfEventSignalling_Type = TruthValue
_RackRfEventSignalling_Object = MibTableColumn
rackRfEventSignalling = _RackRfEventSignalling_Object(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 4, 1, 6, 1, 7),
    _RackRfEventSignalling_Type()
)
rackRfEventSignalling.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rackRfEventSignalling.setStatus("current")
_RackReferenceVoltage_Type = FloatingPoint
_RackReferenceVoltage_Object = MibTableColumn
rackReferenceVoltage = _RackReferenceVoltage_Object(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 4, 1, 6, 1, 8),
    _RackReferenceVoltage_Type()
)
rackReferenceVoltage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rackReferenceVoltage.setStatus("current")
if mibBuilder.loadTexts:
    rackReferenceVoltage.setUnits("percent")
_AmplifiersPowerSupply_Type = FloatingPoint
_AmplifiersPowerSupply_Object = MibTableColumn
amplifiersPowerSupply = _AmplifiersPowerSupply_Object(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 4, 1, 6, 1, 9),
    _AmplifiersPowerSupply_Type()
)
amplifiersPowerSupply.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    amplifiersPowerSupply.setStatus("current")
if mibBuilder.loadTexts:
    amplifiersPowerSupply.setUnits("percent")


class _RackGeneralPurposeInput_Type(Integer32):
    """Custom type rackGeneralPurposeInput based on Integer32"""
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
        *(("unused", 1),
          ("doorOpen", 2),
          ("extCoolingWarning", 3),
          ("extCoolingFault", 4))
    )


_RackGeneralPurposeInput_Type.__name__ = "Integer32"
_RackGeneralPurposeInput_Object = MibTableColumn
rackGeneralPurposeInput = _RackGeneralPurposeInput_Object(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 4, 1, 6, 1, 10),
    _RackGeneralPurposeInput_Type()
)
rackGeneralPurposeInput.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rackGeneralPurposeInput.setStatus("current")
_RackOnOff_Type = SwitchOnOff
_RackOnOff_Object = MibTableColumn
rackOnOff = _RackOnOff_Object(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 4, 1, 6, 1, 20),
    _RackOnOff_Type()
)
rackOnOff.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rackOnOff.setStatus("current")
_RfProbePresent_Type = TruthValue
_RfProbePresent_Object = MibTableColumn
rfProbePresent = _RfProbePresent_Object(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 4, 1, 6, 1, 50),
    _RfProbePresent_Type()
)
rfProbePresent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rfProbePresent.setStatus("current")


class _RfProbeConfigurationLabel_Type(ReadableString):
    """Custom type rfProbeConfigurationLabel based on ReadableString"""
    subtypeSpec = ReadableString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 12),
    )


_RfProbeConfigurationLabel_Type.__name__ = "ReadableString"
_RfProbeConfigurationLabel_Object = MibTableColumn
rfProbeConfigurationLabel = _RfProbeConfigurationLabel_Object(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 4, 1, 6, 1, 51),
    _RfProbeConfigurationLabel_Type()
)
rfProbeConfigurationLabel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rfProbeConfigurationLabel.setStatus("obsolete")


class _RfProbeConfigurationNominalValue_Type(Integer32):
    """Custom type rfProbeConfigurationNominalValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100000),
    )


_RfProbeConfigurationNominalValue_Type.__name__ = "Integer32"
_RfProbeConfigurationNominalValue_Object = MibTableColumn
rfProbeConfigurationNominalValue = _RfProbeConfigurationNominalValue_Object(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 4, 1, 6, 1, 52),
    _RfProbeConfigurationNominalValue_Type()
)
rfProbeConfigurationNominalValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rfProbeConfigurationNominalValue.setStatus("current")
if mibBuilder.loadTexts:
    rfProbeConfigurationNominalValue.setUnits("W")
_RfProbeThresholdRfFailLimit_Type = FloatingPoint
_RfProbeThresholdRfFailLimit_Object = MibTableColumn
rfProbeThresholdRfFailLimit = _RfProbeThresholdRfFailLimit_Object(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 4, 1, 6, 1, 55),
    _RfProbeThresholdRfFailLimit_Type()
)
rfProbeThresholdRfFailLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rfProbeThresholdRfFailLimit.setStatus("current")
if mibBuilder.loadTexts:
    rfProbeThresholdRfFailLimit.setUnits("dB")


class _RfProbeThresholdTimeoutRfFailCtr_Type(Integer32):
    """Custom type rfProbeThresholdTimeoutRfFailCtr based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 20),
    )


_RfProbeThresholdTimeoutRfFailCtr_Type.__name__ = "Integer32"
_RfProbeThresholdTimeoutRfFailCtr_Object = MibTableColumn
rfProbeThresholdTimeoutRfFailCtr = _RfProbeThresholdTimeoutRfFailCtr_Object(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 4, 1, 6, 1, 56),
    _RfProbeThresholdTimeoutRfFailCtr_Type()
)
rfProbeThresholdTimeoutRfFailCtr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rfProbeThresholdTimeoutRfFailCtr.setStatus("current")
if mibBuilder.loadTexts:
    rfProbeThresholdTimeoutRfFailCtr.setUnits("s")
_RfProbeThresholdWarningLimit_Type = FloatingPoint
_RfProbeThresholdWarningLimit_Object = MibTableColumn
rfProbeThresholdWarningLimit = _RfProbeThresholdWarningLimit_Object(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 4, 1, 6, 1, 57),
    _RfProbeThresholdWarningLimit_Type()
)
rfProbeThresholdWarningLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rfProbeThresholdWarningLimit.setStatus("current")
if mibBuilder.loadTexts:
    rfProbeThresholdWarningLimit.setUnits("dB")
_RfProbeCalibrationGain_Type = FloatingPoint
_RfProbeCalibrationGain_Object = MibTableColumn
rfProbeCalibrationGain = _RfProbeCalibrationGain_Object(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 4, 1, 6, 1, 60),
    _RfProbeCalibrationGain_Type()
)
rfProbeCalibrationGain.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rfProbeCalibrationGain.setStatus("current")
if mibBuilder.loadTexts:
    rfProbeCalibrationGain.setUnits("V")
_RfProbeCalibrationOffset_Type = FloatingPoint
_RfProbeCalibrationOffset_Object = MibTableColumn
rfProbeCalibrationOffset = _RfProbeCalibrationOffset_Object(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 4, 1, 6, 1, 61),
    _RfProbeCalibrationOffset_Type()
)
rfProbeCalibrationOffset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rfProbeCalibrationOffset.setStatus("current")
if mibBuilder.loadTexts:
    rfProbeCalibrationOffset.setUnits("V")
_RfProbeCalibrationSetGain_Type = Trigger
_RfProbeCalibrationSetGain_Object = MibTableColumn
rfProbeCalibrationSetGain = _RfProbeCalibrationSetGain_Object(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 4, 1, 6, 1, 62),
    _RfProbeCalibrationSetGain_Type()
)
rfProbeCalibrationSetGain.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rfProbeCalibrationSetGain.setStatus("current")
_RfProbeCalibrationSetOffset_Type = Trigger
_RfProbeCalibrationSetOffset_Object = MibTableColumn
rfProbeCalibrationSetOffset = _RfProbeCalibrationSetOffset_Object(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 4, 1, 6, 1, 63),
    _RfProbeCalibrationSetOffset_Type()
)
rfProbeCalibrationSetOffset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rfProbeCalibrationSetOffset.setStatus("current")
_RfProbeMeasuredValue_Type = FloatingPoint
_RfProbeMeasuredValue_Object = MibTableColumn
rfProbeMeasuredValue = _RfProbeMeasuredValue_Object(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 4, 1, 6, 1, 65),
    _RfProbeMeasuredValue_Type()
)
rfProbeMeasuredValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rfProbeMeasuredValue.setStatus("current")
if mibBuilder.loadTexts:
    rfProbeMeasuredValue.setUnits("W")
_Sx801AmplifierTable_Object = MibTable
sx801AmplifierTable = _Sx801AmplifierTable_Object(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 4, 1, 7)
)
if mibBuilder.loadTexts:
    sx801AmplifierTable.setStatus("current")
_Sx801AmplifierEntry_Object = MibTableRow
sx801AmplifierEntry = _Sx801AmplifierEntry_Object(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 4, 1, 7, 1)
)
sx801AmplifierEntry.setIndexNames(
    (0, "RS-XX8000-DVB-TX-MIB", "sx801AmpIdx"),
)
if mibBuilder.loadTexts:
    sx801AmplifierEntry.setStatus("current")
_Sx801AmpIdx_Type = IndexAmplifier
_Sx801AmpIdx_Object = MibTableColumn
sx801AmpIdx = _Sx801AmpIdx_Object(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 4, 1, 7, 1, 1),
    _Sx801AmpIdx_Type()
)
sx801AmpIdx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sx801AmpIdx.setStatus("current")
_Sx801AmpRfOut_Type = Sx801AmplifierState
_Sx801AmpRfOut_Object = MibTableColumn
sx801AmpRfOut = _Sx801AmpRfOut_Object(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 4, 1, 7, 1, 2),
    _Sx801AmpRfOut_Type()
)
sx801AmpRfOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sx801AmpRfOut.setStatus("current")
_Sx801AmpRfIn_Type = Sx801AmplifierState
_Sx801AmpRfIn_Object = MibTableColumn
sx801AmpRfIn = _Sx801AmpRfIn_Object(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 4, 1, 7, 1, 3),
    _Sx801AmpRfIn_Type()
)
sx801AmpRfIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sx801AmpRfIn.setStatus("current")


class _Sx801AmpReflection_Type(Integer32):
    """Custom type sx801AmpReflection based on Integer32"""
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
        *(("off", 1),
          ("warning", 2),
          ("unknown", 3),
          ("fault", 4))
    )


_Sx801AmpReflection_Type.__name__ = "Integer32"
_Sx801AmpReflection_Object = MibTableColumn
sx801AmpReflection = _Sx801AmpReflection_Object(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 4, 1, 7, 1, 4),
    _Sx801AmpReflection_Type()
)
sx801AmpReflection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sx801AmpReflection.setStatus("current")


class _Sx801AmpOn_Type(Integer32):
    """Custom type sx801AmpOn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 3),
          ("unknown", 4))
    )


_Sx801AmpOn_Type.__name__ = "Integer32"
_Sx801AmpOn_Object = MibTableColumn
sx801AmpOn = _Sx801AmpOn_Object(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 4, 1, 7, 1, 5),
    _Sx801AmpOn_Type()
)
sx801AmpOn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sx801AmpOn.setStatus("current")
_Sx801AmpAC_Type = Sx801AmplifierState
_Sx801AmpAC_Object = MibTableColumn
sx801AmpAC = _Sx801AmpAC_Object(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 4, 1, 7, 1, 6),
    _Sx801AmpAC_Type()
)
sx801AmpAC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sx801AmpAC.setStatus("current")


class _Sx801AmpCommunication_Type(Integer32):
    """Custom type sx801AmpCommunication based on Integer32"""
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
        *(("off", 1),
          ("unknown", 2),
          ("ok", 3),
          ("fault", 4))
    )


_Sx801AmpCommunication_Type.__name__ = "Integer32"
_Sx801AmpCommunication_Object = MibTableColumn
sx801AmpCommunication = _Sx801AmpCommunication_Object(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 4, 1, 7, 1, 7),
    _Sx801AmpCommunication_Type()
)
sx801AmpCommunication.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sx801AmpCommunication.setStatus("current")
_Sx801AmpTransistor_Type = Sx801AmplifierState
_Sx801AmpTransistor_Object = MibTableColumn
sx801AmpTransistor = _Sx801AmpTransistor_Object(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 4, 1, 7, 1, 8),
    _Sx801AmpTransistor_Type()
)
sx801AmpTransistor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sx801AmpTransistor.setStatus("current")
_Sx801AmpDriver_Type = Sx801AmplifierState
_Sx801AmpDriver_Object = MibTableColumn
sx801AmpDriver = _Sx801AmpDriver_Object(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 4, 1, 7, 1, 9),
    _Sx801AmpDriver_Type()
)
sx801AmpDriver.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sx801AmpDriver.setStatus("current")
_Sx801AmpTemperature_Type = Sx801AmplifierState
_Sx801AmpTemperature_Object = MibTableColumn
sx801AmpTemperature = _Sx801AmpTemperature_Object(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 4, 1, 7, 1, 10),
    _Sx801AmpTemperature_Type()
)
sx801AmpTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sx801AmpTemperature.setStatus("current")
_Sx801AmpBlower_Type = Sx801AmplifierState
_Sx801AmpBlower_Object = MibTableColumn
sx801AmpBlower = _Sx801AmpBlower_Object(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 4, 1, 7, 1, 11),
    _Sx801AmpBlower_Type()
)
sx801AmpBlower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sx801AmpBlower.setStatus("current")
_Sx801AmpRegulation_Type = Sx801AmplifierState
_Sx801AmpRegulation_Object = MibTableColumn
sx801AmpRegulation = _Sx801AmpRegulation_Object(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 4, 1, 7, 1, 12),
    _Sx801AmpRegulation_Type()
)
sx801AmpRegulation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sx801AmpRegulation.setStatus("current")
_Sx801AmpUpdate_Type = TruthValue
_Sx801AmpUpdate_Object = MibTableColumn
sx801AmpUpdate = _Sx801AmpUpdate_Object(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 4, 1, 7, 1, 13),
    _Sx801AmpUpdate_Type()
)
sx801AmpUpdate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sx801AmpUpdate.setStatus("current")
_Sx801Supply1Temperature_Type = Sx801AmplifierState
_Sx801Supply1Temperature_Object = MibTableColumn
sx801Supply1Temperature = _Sx801Supply1Temperature_Object(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 4, 1, 7, 1, 14),
    _Sx801Supply1Temperature_Type()
)
sx801Supply1Temperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sx801Supply1Temperature.setStatus("current")
_Sx801Supply2Temperature_Type = Sx801AmplifierState
_Sx801Supply2Temperature_Object = MibTableColumn
sx801Supply2Temperature = _Sx801Supply2Temperature_Object(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 4, 1, 7, 1, 15),
    _Sx801Supply2Temperature_Type()
)
sx801Supply2Temperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sx801Supply2Temperature.setStatus("current")
_Sx801SupplyRTemperature_Type = Sx801AmplifierState
_Sx801SupplyRTemperature_Object = MibTableColumn
sx801SupplyRTemperature = _Sx801SupplyRTemperature_Object(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 4, 1, 7, 1, 16),
    _Sx801SupplyRTemperature_Type()
)
sx801SupplyRTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sx801SupplyRTemperature.setStatus("current")
_Sx801Supply1DC_Type = Sx801AmplifierState
_Sx801Supply1DC_Object = MibTableColumn
sx801Supply1DC = _Sx801Supply1DC_Object(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 4, 1, 7, 1, 17),
    _Sx801Supply1DC_Type()
)
sx801Supply1DC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sx801Supply1DC.setStatus("current")
_Sx801Supply2DC_Type = Sx801AmplifierState
_Sx801Supply2DC_Object = MibTableColumn
sx801Supply2DC = _Sx801Supply2DC_Object(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 4, 1, 7, 1, 18),
    _Sx801Supply2DC_Type()
)
sx801Supply2DC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sx801Supply2DC.setStatus("current")
_Sx801SupplyRDC_Type = Sx801AmplifierState
_Sx801SupplyRDC_Object = MibTableColumn
sx801SupplyRDC = _Sx801SupplyRDC_Object(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 4, 1, 7, 1, 19),
    _Sx801SupplyRDC_Type()
)
sx801SupplyRDC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sx801SupplyRDC.setStatus("current")
_Sx801AmpValueI1_Type = FloatingPoint
_Sx801AmpValueI1_Object = MibTableColumn
sx801AmpValueI1 = _Sx801AmpValueI1_Object(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 4, 1, 7, 1, 50),
    _Sx801AmpValueI1_Type()
)
sx801AmpValueI1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sx801AmpValueI1.setStatus("current")
if mibBuilder.loadTexts:
    sx801AmpValueI1.setUnits("Ampere")
_Sx801AmpValueI2_Type = FloatingPoint
_Sx801AmpValueI2_Object = MibTableColumn
sx801AmpValueI2 = _Sx801AmpValueI2_Object(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 4, 1, 7, 1, 51),
    _Sx801AmpValueI2_Type()
)
sx801AmpValueI2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sx801AmpValueI2.setStatus("current")
if mibBuilder.loadTexts:
    sx801AmpValueI2.setUnits("Ampere")
_Sx801AmpValueI3_Type = FloatingPoint
_Sx801AmpValueI3_Object = MibTableColumn
sx801AmpValueI3 = _Sx801AmpValueI3_Object(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 4, 1, 7, 1, 52),
    _Sx801AmpValueI3_Type()
)
sx801AmpValueI3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sx801AmpValueI3.setStatus("current")
if mibBuilder.loadTexts:
    sx801AmpValueI3.setUnits("Ampere")
_Sx801AmpValueI4_Type = FloatingPoint
_Sx801AmpValueI4_Object = MibTableColumn
sx801AmpValueI4 = _Sx801AmpValueI4_Object(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 4, 1, 7, 1, 53),
    _Sx801AmpValueI4_Type()
)
sx801AmpValueI4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sx801AmpValueI4.setStatus("current")
if mibBuilder.loadTexts:
    sx801AmpValueI4.setUnits("Ampere")
_Sx801AmpValueIPre_Type = FloatingPoint
_Sx801AmpValueIPre_Object = MibTableColumn
sx801AmpValueIPre = _Sx801AmpValueIPre_Object(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 4, 1, 7, 1, 54),
    _Sx801AmpValueIPre_Type()
)
sx801AmpValueIPre.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sx801AmpValueIPre.setStatus("current")
if mibBuilder.loadTexts:
    sx801AmpValueIPre.setUnits("Ampere")
_Sx801AmpValueIDrv1_Type = FloatingPoint
_Sx801AmpValueIDrv1_Object = MibTableColumn
sx801AmpValueIDrv1 = _Sx801AmpValueIDrv1_Object(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 4, 1, 7, 1, 55),
    _Sx801AmpValueIDrv1_Type()
)
sx801AmpValueIDrv1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sx801AmpValueIDrv1.setStatus("current")
if mibBuilder.loadTexts:
    sx801AmpValueIDrv1.setUnits("Ampere")
_Sx801AmpValueIDrv2_Type = FloatingPoint
_Sx801AmpValueIDrv2_Object = MibTableColumn
sx801AmpValueIDrv2 = _Sx801AmpValueIDrv2_Object(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 4, 1, 7, 1, 56),
    _Sx801AmpValueIDrv2_Type()
)
sx801AmpValueIDrv2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sx801AmpValueIDrv2.setStatus("current")
if mibBuilder.loadTexts:
    sx801AmpValueIDrv2.setUnits("Ampere")
_Sx801AmpValuePowerOut_Type = FloatingPoint
_Sx801AmpValuePowerOut_Object = MibTableColumn
sx801AmpValuePowerOut = _Sx801AmpValuePowerOut_Object(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 4, 1, 7, 1, 57),
    _Sx801AmpValuePowerOut_Type()
)
sx801AmpValuePowerOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sx801AmpValuePowerOut.setStatus("current")
if mibBuilder.loadTexts:
    sx801AmpValuePowerOut.setUnits("Watt")
_Sx801AmpValueReflection_Type = FloatingPoint
_Sx801AmpValueReflection_Object = MibTableColumn
sx801AmpValueReflection = _Sx801AmpValueReflection_Object(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 4, 1, 7, 1, 58),
    _Sx801AmpValueReflection_Type()
)
sx801AmpValueReflection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sx801AmpValueReflection.setStatus("current")
if mibBuilder.loadTexts:
    sx801AmpValueReflection.setUnits("Watt")
_Sx801AmpValueVRef_Type = FloatingPoint
_Sx801AmpValueVRef_Object = MibTableColumn
sx801AmpValueVRef = _Sx801AmpValueVRef_Object(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 4, 1, 7, 1, 59),
    _Sx801AmpValueVRef_Type()
)
sx801AmpValueVRef.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sx801AmpValueVRef.setStatus("current")
if mibBuilder.loadTexts:
    sx801AmpValueVRef.setUnits("Volt")
_Sx801AmpValueVReg_Type = FloatingPoint
_Sx801AmpValueVReg_Object = MibTableColumn
sx801AmpValueVReg = _Sx801AmpValueVReg_Object(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 4, 1, 7, 1, 60),
    _Sx801AmpValueVReg_Type()
)
sx801AmpValueVReg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sx801AmpValueVReg.setStatus("current")
if mibBuilder.loadTexts:
    sx801AmpValueVReg.setUnits("Volt")
_Sx801AmpValueTemperature_Type = FloatingPoint
_Sx801AmpValueTemperature_Object = MibTableColumn
sx801AmpValueTemperature = _Sx801AmpValueTemperature_Object(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 4, 1, 7, 1, 61),
    _Sx801AmpValueTemperature_Type()
)
sx801AmpValueTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sx801AmpValueTemperature.setStatus("current")
if mibBuilder.loadTexts:
    sx801AmpValueTemperature.setUnits("degree Celsius")
_Sx801AmpValueMonAtt_Type = FloatingPoint
_Sx801AmpValueMonAtt_Object = MibTableColumn
sx801AmpValueMonAtt = _Sx801AmpValueMonAtt_Object(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 4, 1, 7, 1, 62),
    _Sx801AmpValueMonAtt_Type()
)
sx801AmpValueMonAtt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sx801AmpValueMonAtt.setStatus("current")
if mibBuilder.loadTexts:
    sx801AmpValueMonAtt.setUnits("dB")
_Sx801AmpValueVAux1_Type = FloatingPoint
_Sx801AmpValueVAux1_Object = MibTableColumn
sx801AmpValueVAux1 = _Sx801AmpValueVAux1_Object(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 4, 1, 7, 1, 63),
    _Sx801AmpValueVAux1_Type()
)
sx801AmpValueVAux1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sx801AmpValueVAux1.setStatus("current")
if mibBuilder.loadTexts:
    sx801AmpValueVAux1.setUnits("Volt")
_Sx801AmpValueVAux2_Type = FloatingPoint
_Sx801AmpValueVAux2_Object = MibTableColumn
sx801AmpValueVAux2 = _Sx801AmpValueVAux2_Object(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 4, 1, 7, 1, 64),
    _Sx801AmpValueVAux2_Type()
)
sx801AmpValueVAux2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sx801AmpValueVAux2.setStatus("current")
if mibBuilder.loadTexts:
    sx801AmpValueVAux2.setUnits("Volt")
_Sx801Supply1ValuePwr_Type = FloatingPoint
_Sx801Supply1ValuePwr_Object = MibTableColumn
sx801Supply1ValuePwr = _Sx801Supply1ValuePwr_Object(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 4, 1, 7, 1, 65),
    _Sx801Supply1ValuePwr_Type()
)
sx801Supply1ValuePwr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sx801Supply1ValuePwr.setStatus("current")
if mibBuilder.loadTexts:
    sx801Supply1ValuePwr.setUnits("Volt")
_Sx801Supply2ValuePwr_Type = FloatingPoint
_Sx801Supply2ValuePwr_Object = MibTableColumn
sx801Supply2ValuePwr = _Sx801Supply2ValuePwr_Object(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 4, 1, 7, 1, 66),
    _Sx801Supply2ValuePwr_Type()
)
sx801Supply2ValuePwr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sx801Supply2ValuePwr.setStatus("current")
if mibBuilder.loadTexts:
    sx801Supply2ValuePwr.setUnits("Volt")
_Sx801Supply1ValueDc_Type = FloatingPoint
_Sx801Supply1ValueDc_Object = MibTableColumn
sx801Supply1ValueDc = _Sx801Supply1ValueDc_Object(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 4, 1, 7, 1, 67),
    _Sx801Supply1ValueDc_Type()
)
sx801Supply1ValueDc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sx801Supply1ValueDc.setStatus("current")
if mibBuilder.loadTexts:
    sx801Supply1ValueDc.setUnits("Volt")
_Sx801Supply2ValueDc_Type = FloatingPoint
_Sx801Supply2ValueDc_Object = MibTableColumn
sx801Supply2ValueDc = _Sx801Supply2ValueDc_Object(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 4, 1, 7, 1, 68),
    _Sx801Supply2ValueDc_Type()
)
sx801Supply2ValueDc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sx801Supply2ValueDc.setStatus("current")
if mibBuilder.loadTexts:
    sx801Supply2ValueDc.setUnits("Volt")
_RsXx8000DvbTxEvents_ObjectIdentity = ObjectIdentity
rsXx8000DvbTxEvents = _RsXx8000DvbTxEvents_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 4, 3)
)
_EventTx_ObjectIdentity = ObjectIdentity
eventTx = _EventTx_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 4, 3, 2)
)
_EventsTxV2_ObjectIdentity = ObjectIdentity
eventsTxV2 = _EventsTxV2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 4, 3, 2, 0)
)
if mibBuilder.loadTexts:
    eventsTxV2.setStatus("current")
_EventsTxTable_Object = MibTable
eventsTxTable = _EventsTxTable_Object(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 4, 3, 2, 1)
)
if mibBuilder.loadTexts:
    eventsTxTable.setStatus("current")
_EventsTxEntry_Object = MibTableRow
eventsTxEntry = _EventsTxEntry_Object(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 4, 3, 2, 1, 1)
)
eventsTxEntry.setIndexNames(
    (0, "RS-XX8000-DVB-TX-MIB", "eventTxABIdx"),
    (0, "RS-XX8000-DVB-TX-MIB", "eventTxRackIdx"),
    (0, "RS-XX8000-DVB-TX-MIB", "eventTxAmpIdx"),
    (0, "RS-XX8000-DVB-TX-MIB", "eventTxNameIdx"),
)
if mibBuilder.loadTexts:
    eventsTxEntry.setStatus("current")


class _EventTxABIdx_Type(Integer32):
    """Custom type eventTxABIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("a", 1),
          ("b", 2))
    )


_EventTxABIdx_Type.__name__ = "Integer32"
_EventTxABIdx_Object = MibTableColumn
eventTxABIdx = _EventTxABIdx_Object(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 4, 3, 2, 1, 1, 1),
    _EventTxABIdx_Type()
)
eventTxABIdx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    eventTxABIdx.setStatus("current")


class _EventTxRackIdx_Type(Integer32):
    """Custom type eventTxRackIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_EventTxRackIdx_Type.__name__ = "Integer32"
_EventTxRackIdx_Object = MibTableColumn
eventTxRackIdx = _EventTxRackIdx_Object(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 4, 3, 2, 1, 1, 2),
    _EventTxRackIdx_Type()
)
eventTxRackIdx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    eventTxRackIdx.setStatus("current")


class _EventTxAmpIdx_Type(Integer32):
    """Custom type eventTxAmpIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_EventTxAmpIdx_Type.__name__ = "Integer32"
_EventTxAmpIdx_Object = MibTableColumn
eventTxAmpIdx = _EventTxAmpIdx_Object(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 4, 3, 2, 1, 1, 3),
    _EventTxAmpIdx_Type()
)
eventTxAmpIdx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    eventTxAmpIdx.setStatus("current")
_EventTxNameIdx_Type = EventMaxEntryNumber
_EventTxNameIdx_Object = MibTableColumn
eventTxNameIdx = _EventTxNameIdx_Object(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 4, 3, 2, 1, 1, 4),
    _EventTxNameIdx_Type()
)
eventTxNameIdx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    eventTxNameIdx.setStatus("current")


class _EventTxName_Type(Integer32):
    """Custom type eventTxName based on Integer32"""
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
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19,
              20,
              21,
              22,
              23,
              24,
              25,
              26,
              27,
              30,
              31,
              35,
              36,
              37,
              38,
              100,
              101,
              102,
              104,
              105,
              106,
              107,
              108,
              109,
              110,
              111,
              112,
              113,
              114,
              115,
              116,
              117,
              118,
              119,
              120,
              121,
              122,
              123,
              124,
              125,
              126,
              127,
              128,
              129,
              130,
              131,
              132,
              133,
              200,
              201,
              202,
              203,
              204,
              205,
              206,
              207,
              208,
              209,
              210,
              211,
              212,
              213,
              300,
              301,
              302,
              303,
              304,
              305,
              306,
              307,
              308,
              309,
              310,
              311,
              312,
              313,
              314,
              315,
              318,
              319,
              320,
              321,
              322,
              323,
              330,
              331,
              335,
              400,
              401,
              402,
              403,
              404,
              405,
              406,
              407,
              408,
              409)
        )
    )
    namedValues = NamedValues(
        *(("txSummaryFault", 1),
          ("txSummaryWarning", 2),
          ("txLocal", 3),
          ("txRfOn", 4),
          ("txRfOk", 5),
          ("txParamSetSubDeviceDiffers", 6),
          ("txParamSetValuesChanged", 7),
          ("txRfLoopProgram", 8),
          ("txRfLoopReserve", 9),
          ("txRfWarning", 10),
          ("txReflectionWarning", 11),
          ("txNetCCUFanFault", 12),
          ("txNetCCUPowerSupply", 13),
          ("txRfFail", 14),
          ("txReflectionFault", 15),
          ("txNetCCUBoardTemperatureFault", 16),
          ("txNetCCUNoConnectionToExcA", 17),
          ("txNetCCUNoConnectionToOstA", 18),
          ("txNetCCUNoConnectionToExcB", 19),
          ("txNetCCUNoConnectionToOstB", 20),
          ("txAutomaticExcReady", 21),
          ("txAutomaticExcChanged", 22),
          ("txAutomaticExcFault", 23),
          ("txAutomaticOstReady", 24),
          ("txAutomaticOstChanged", 25),
          ("txAutomaticOstFault", 26),
          ("txNetCCUBoardTemperatureWarning", 27),
          ("txInternalPowerSupplyWarning", 30),
          ("txExternalPowerSupplyWarning", 31),
          ("txModeSwitchOverStarted", 35),
          ("txModeSwitchOverEnded", 36),
          ("txModeInconsistent", 37),
          ("txModeSwitchOverFailed", 38),
          ("txExcSummaryFault", 100),
          ("txExcSummaryWarning", 101),
          ("txExcLocal", 102),
          ("txExcRfOk", 104),
          ("txExcInputNoConnectHP1", 105),
          ("txExcInputNoConnectLP1", 106),
          ("txExcInputNoConnectHP2", 107),
          ("txExcInputNoConnectLP2", 108),
          ("txExcInputActiveHP1", 109),
          ("txExcInputActiveLP1", 110),
          ("txExcInputActiveHP2", 111),
          ("txExcInputActiveLP2", 112),
          ("txExcOn", 113),
          ("txExcRfOn", 114),
          ("txExcNoInput", 115),
          ("txExcRfLoop", 116),
          ("txExcRfFail", 117),
          ("txExcSelfTest", 118),
          ("txExcOutputOpen", 119),
          ("txExcBoardTemperatureWarning", 120),
          ("txExcFanWarning", 121),
          ("txExcFanFault", 122),
          ("txExcFifoWarning", 123),
          ("txExcTestSignal", 124),
          ("txExcSFNDelay", 125),
          ("txExcWrongDatarate", 126),
          ("txExcMute", 127),
          ("txExcPPSFail", 128),
          ("txExcReferenceFail", 129),
          ("txExcMIPFail", 130),
          ("txExcInputAutomaticSwitchReady", 131),
          ("txExcInputAutomaticChangedOver", 132),
          ("txExcInputReseveMissing", 133),
          ("txOstSummaryFault", 200),
          ("txOstSummaryWarning", 201),
          ("txOstRfOn", 202),
          ("txOstRfOk", 203),
          ("txOstNoInput", 204),
          ("txOstRfWarning", 205),
          ("txOstReflectionWarning", 206),
          ("txOstRackWarning", 207),
          ("txOstCoolingWarning", 208),
          ("txOstRfFail", 209),
          ("txOstReflectionFault", 210),
          ("txOstACFault", 211),
          ("txOstCoolingFault", 212),
          ("txOstCommFault", 213),
          ("txRackSumFault", 300),
          ("txRackSumWarning", 301),
          ("txRackOn", 302),
          ("txRackGpiWarning", 303),
          ("txRackFan1Fault", 304),
          ("txRackFan2Fault", 305),
          ("txRackCoolingSumWarning", 306),
          ("txRackAmplifierSumFault", 307),
          ("txRackNoLink", 308),
          ("txRackGpiFault", 309),
          ("txRackTemperatureFault", 310),
          ("txRackACFault", 311),
          ("txRackCoolingSumFault", 312),
          ("txRackTempFaultAbs1", 313),
          ("txRackTempFaultAbs2", 314),
          ("txRackDCFault", 315),
          ("txRackRfOn", 318),
          ("txRackRfOk", 319),
          ("txRackRfWarning", 320),
          ("txRackRfFault", 321),
          ("txRackReflectionWarning", 322),
          ("txRackReflectionFault", 323),
          ("txRackProbeNotCalibrated", 330),
          ("txRackTemperatureWarning", 331),
          ("txRackOvervoltProtectWarning", 335),
          ("txAmpSumFault", 400),
          ("txAmpSumWarning", 401),
          ("txAmpPowerOn", 402),
          ("txAmpDCOk", 403),
          ("txAmpACOk", 404),
          ("txAmpRfInFail", 405),
          ("txAmpRfFail", 406),
          ("txAmpReflectionFault", 407),
          ("txAmpTemperatureFault", 408),
          ("txAmpTransistorFault", 409))
    )


_EventTxName_Type.__name__ = "Integer32"
_EventTxName_Object = MibTableColumn
eventTxName = _EventTxName_Object(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 4, 3, 2, 1, 1, 5),
    _EventTxName_Type()
)
eventTxName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eventTxName.setStatus("current")
_EventTxMask_Type = EventMask
_EventTxMask_Object = MibTableColumn
eventTxMask = _EventTxMask_Object(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 4, 3, 2, 1, 1, 6),
    _EventTxMask_Type()
)
eventTxMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eventTxMask.setStatus("current")
_EventTxPriority_Type = EventPriority
_EventTxPriority_Object = MibTableColumn
eventTxPriority = _EventTxPriority_Object(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 4, 3, 2, 1, 1, 7),
    _EventTxPriority_Type()
)
eventTxPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eventTxPriority.setStatus("current")
_EventTxEvent_Type = EventState
_EventTxEvent_Object = MibTableColumn
eventTxEvent = _EventTxEvent_Object(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 4, 3, 2, 1, 1, 8),
    _EventTxEvent_Type()
)
eventTxEvent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eventTxEvent.setStatus("current")
_RsXx8000DvbTxConf_ObjectIdentity = ObjectIdentity
rsXx8000DvbTxConf = _RsXx8000DvbTxConf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 4, 5)
)
_RsXx8000DvbTxGroups_ObjectIdentity = ObjectIdentity
rsXx8000DvbTxGroups = _RsXx8000DvbTxGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 4, 5, 1)
)
_RsXx8000DvbTxCompl_ObjectIdentity = ObjectIdentity
rsXx8000DvbTxCompl = _RsXx8000DvbTxCompl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 4, 5, 3)
)
configurationEntry.registerAugmentions(
    ("RS-XX8000-DVB-TX-MIB",
     "configuration2Entry")
)
configuration2Entry.setIndexNames(*configurationEntry.getIndexNames())

# Managed Objects groups

groupEvents = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 4, 5, 1, 1)
)
groupEvents.setObjects(
      *(("RS-XX8000-DVB-TX-MIB", "eventTxName"),
        ("RS-XX8000-DVB-TX-MIB", "eventTxMask"),
        ("RS-XX8000-DVB-TX-MIB", "eventTxPriority"),
        ("RS-XX8000-DVB-TX-MIB", "eventTxEvent"))
)
if mibBuilder.loadTexts:
    groupEvents.setStatus("current")

groupTxCommon = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 4, 5, 1, 2)
)
groupTxCommon.setObjects(
      *(("RS-XX8000-DVB-TX-MIB", "cmdTxResetSumFault"),
        ("RS-XX8000-DVB-TX-MIB", "cmdTxParametersetLoad"),
        ("RS-XX8000-DVB-TX-MIB", "cmdTxParametersetSave"),
        ("RS-XX8000-DVB-TX-MIB", "cmdTxOperationModeProgram"),
        ("RS-XX8000-DVB-TX-MIB", "summaryFaultTx"),
        ("RS-XX8000-DVB-TX-MIB", "summaryWarningTx"),
        ("RS-XX8000-DVB-TX-MIB", "localModeTx"),
        ("RS-XX8000-DVB-TX-MIB", "rfOnTx"),
        ("RS-XX8000-DVB-TX-MIB", "forwardPower"),
        ("RS-XX8000-DVB-TX-MIB", "summaryFaultExcA"))
)
if mibBuilder.loadTexts:
    groupTxCommon.setStatus("current")

groupDualDrive = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 4, 5, 1, 4)
)
groupDualDrive.setObjects(
      *(("RS-XX8000-DVB-TX-MIB", "cmdTxOperationModeReserve"),
        ("RS-XX8000-DVB-TX-MIB", "cmdTxOpModeExcAutomatic"),
        ("RS-XX8000-DVB-TX-MIB", "cmdTxPreselectExciter"),
        ("RS-XX8000-DVB-TX-MIB", "cmdTxDelayTimeExcAutomatic"),
        ("RS-XX8000-DVB-TX-MIB", "exciterBNumberOfEntries"),
        ("RS-XX8000-DVB-TX-MIB", "exciterBLogbookClear"),
        ("RS-XX8000-DVB-TX-MIB", "excBLogbookEntryNbr"),
        ("RS-XX8000-DVB-TX-MIB", "excBLogbookType"),
        ("RS-XX8000-DVB-TX-MIB", "excBLogbookSlope"),
        ("RS-XX8000-DVB-TX-MIB", "excBLogbookMessage"),
        ("RS-XX8000-DVB-TX-MIB", "excBLogbookDateTime"),
        ("RS-XX8000-DVB-TX-MIB", "summaryFaultExcB"),
        ("RS-XX8000-DVB-TX-MIB", "exciterAutomaticReady"),
        ("RS-XX8000-DVB-TX-MIB", "exciterAutomaticChanged"),
        ("RS-XX8000-DVB-TX-MIB", "exciterAutomaticFault"),
        ("RS-XX8000-DVB-TX-MIB", "noConnectionExcB"),
        ("RS-XX8000-DVB-TX-MIB", "activeExcA"),
        ("RS-XX8000-DVB-TX-MIB", "activeExcB"))
)
if mibBuilder.loadTexts:
    groupDualDrive.setStatus("current")

groupPowerReserve = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 4, 5, 1, 6)
)
groupPowerReserve.setObjects(
      *(("RS-XX8000-DVB-TX-MIB", "cmdTxOpModeOstAutomatic"),
        ("RS-XX8000-DVB-TX-MIB", "cmdTxPreselectOutputstage"),
        ("RS-XX8000-DVB-TX-MIB", "cmdTxDelayTimeOstAutomatic"),
        ("RS-XX8000-DVB-TX-MIB", "summaryFaultOstB"),
        ("RS-XX8000-DVB-TX-MIB", "outputstageAutomaticReady"),
        ("RS-XX8000-DVB-TX-MIB", "outputstageAutomaticChanged"),
        ("RS-XX8000-DVB-TX-MIB", "outputstageAutomaticFault"),
        ("RS-XX8000-DVB-TX-MIB", "noConnectionOstB"),
        ("RS-XX8000-DVB-TX-MIB", "activeOstA"),
        ("RS-XX8000-DVB-TX-MIB", "activeOstB"))
)
if mibBuilder.loadTexts:
    groupPowerReserve.setStatus("current")

groupCommonMP = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 4, 5, 1, 8)
)
groupCommonMP.setObjects(
      *(("RS-XX8000-DVB-TX-MIB", "cmdOstRefVoltageVision"),
        ("RS-XX8000-DVB-TX-MIB", "cmdOstMaxOutletTempThreshold"),
        ("RS-XX8000-DVB-TX-MIB", "outputstageANumberOfEntries"),
        ("RS-XX8000-DVB-TX-MIB", "outputstageALogbookClear"),
        ("RS-XX8000-DVB-TX-MIB", "ostALogbookEntryNbr"),
        ("RS-XX8000-DVB-TX-MIB", "ostALogbookType"),
        ("RS-XX8000-DVB-TX-MIB", "ostALogbookSlope"),
        ("RS-XX8000-DVB-TX-MIB", "ostALogbookMessage"),
        ("RS-XX8000-DVB-TX-MIB", "ostALogbookDateTime"),
        ("RS-XX8000-DVB-TX-MIB", "reflectedPower"),
        ("RS-XX8000-DVB-TX-MIB", "ostRackInletTemperature"),
        ("RS-XX8000-DVB-TX-MIB", "ostRackOutletTemperature"),
        ("RS-XX8000-DVB-TX-MIB", "ostRackAuxPowerSupply"),
        ("RS-XX8000-DVB-TX-MIB", "amplifiersPerRack"),
        ("RS-XX8000-DVB-TX-MIB", "rackRfEventSignalling"),
        ("RS-XX8000-DVB-TX-MIB", "rackGeneralPurposeInput"),
        ("RS-XX8000-DVB-TX-MIB", "rfProbePresent"),
        ("RS-XX8000-DVB-TX-MIB", "rfProbeConfigurationNominalValue"),
        ("RS-XX8000-DVB-TX-MIB", "rfProbeThresholdRfFailLimit"),
        ("RS-XX8000-DVB-TX-MIB", "rfProbeThresholdTimeoutRfFailCtr"),
        ("RS-XX8000-DVB-TX-MIB", "rfProbeThresholdWarningLimit"),
        ("RS-XX8000-DVB-TX-MIB", "rfProbeCalibrationGain"),
        ("RS-XX8000-DVB-TX-MIB", "rfProbeCalibrationOffset"),
        ("RS-XX8000-DVB-TX-MIB", "rfProbeCalibrationSetGain"),
        ("RS-XX8000-DVB-TX-MIB", "rfProbeCalibrationSetOffset"),
        ("RS-XX8000-DVB-TX-MIB", "rfProbeMeasuredValue"))
)
if mibBuilder.loadTexts:
    groupCommonMP.setStatus("current")

groupCommonNetCCU = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 4, 5, 1, 10)
)
groupCommonNetCCU.setObjects(
      *(("RS-XX8000-DVB-TX-MIB", "netCCUNumberOfEntries"),
        ("RS-XX8000-DVB-TX-MIB", "netCCULogbookClear"),
        ("RS-XX8000-DVB-TX-MIB", "netCCULogbookEntryNbr"),
        ("RS-XX8000-DVB-TX-MIB", "netCCULogbookType"),
        ("RS-XX8000-DVB-TX-MIB", "netCCULogbookSlope"),
        ("RS-XX8000-DVB-TX-MIB", "netCCULogbookMessage"),
        ("RS-XX8000-DVB-TX-MIB", "netCCULogbookDateTime"),
        ("RS-XX8000-DVB-TX-MIB", "powerSupply"),
        ("RS-XX8000-DVB-TX-MIB", "cmdTxSystemMode"),
        ("RS-XX8000-DVB-TX-MIB", "additionalPowerSupply"),
        ("RS-XX8000-DVB-TX-MIB", "summaryFaultOstA"),
        ("RS-XX8000-DVB-TX-MIB", "noConnectionExcA"),
        ("RS-XX8000-DVB-TX-MIB", "noConnectionOstA"))
)
if mibBuilder.loadTexts:
    groupCommonNetCCU.setStatus("current")

groupOstBLogbook = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 4, 5, 1, 12)
)
groupOstBLogbook.setObjects(
      *(("RS-XX8000-DVB-TX-MIB", "outputstageBNumberOfEntries"),
        ("RS-XX8000-DVB-TX-MIB", "outputstageBLogbookClear"),
        ("RS-XX8000-DVB-TX-MIB", "ostBLogbookEntryNbr"),
        ("RS-XX8000-DVB-TX-MIB", "ostBLogbookType"),
        ("RS-XX8000-DVB-TX-MIB", "ostBLogbookSlope"),
        ("RS-XX8000-DVB-TX-MIB", "ostBLogbookMessage"),
        ("RS-XX8000-DVB-TX-MIB", "ostBLogbookDateTime"))
)
if mibBuilder.loadTexts:
    groupOstBLogbook.setStatus("current")

groupSumProbe = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 4, 5, 1, 14)
)
groupSumProbe.setObjects(
      *(("RS-XX8000-DVB-TX-MIB", "forwardPowerOstA"),
        ("RS-XX8000-DVB-TX-MIB", "reflectedPowerOstA"),
        ("RS-XX8000-DVB-TX-MIB", "forwardPowerOstB"),
        ("RS-XX8000-DVB-TX-MIB", "reflectedPowerOstB"))
)
if mibBuilder.loadTexts:
    groupSumProbe.setStatus("current")

groupProductInfo = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 4, 5, 1, 18)
)
groupProductInfo.setObjects(
      *(("RS-XX8000-DVB-TX-MIB", "prodInfoModuleName"),
        ("RS-XX8000-DVB-TX-MIB", "prodInfoSerialNumber"),
        ("RS-XX8000-DVB-TX-MIB", "prodInfoIdentNumberSW"),
        ("RS-XX8000-DVB-TX-MIB", "prodInfoVersionNumberSW"),
        ("RS-XX8000-DVB-TX-MIB", "productInfoProductDateHW"),
        ("RS-XX8000-DVB-TX-MIB", "prodInfoIdentNumberHW"),
        ("RS-XX8000-DVB-TX-MIB", "prodInfoVersionNumberHW"))
)
if mibBuilder.loadTexts:
    groupProductInfo.setStatus("current")

groupAmpMeasureValues = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 4, 5, 1, 19)
)
groupAmpMeasureValues.setObjects(
      *(("RS-XX8000-DVB-TX-MIB", "ostRackAmpI1A"),
        ("RS-XX8000-DVB-TX-MIB", "ostRackAmpI2A"),
        ("RS-XX8000-DVB-TX-MIB", "ostRackAmpI3A"),
        ("RS-XX8000-DVB-TX-MIB", "ostRackAmpI4A"),
        ("RS-XX8000-DVB-TX-MIB", "ostRackAmpI1B"),
        ("RS-XX8000-DVB-TX-MIB", "ostRackAmpI2B"),
        ("RS-XX8000-DVB-TX-MIB", "ostRackAmpI3B"),
        ("RS-XX8000-DVB-TX-MIB", "ostRackAmpI4B"),
        ("RS-XX8000-DVB-TX-MIB", "ostRackAmpIDrv"),
        ("RS-XX8000-DVB-TX-MIB", "ostRackAmpUDc"),
        ("RS-XX8000-DVB-TX-MIB", "ostRackAmpIDc"),
        ("RS-XX8000-DVB-TX-MIB", "ostRackAmpUDcControl"),
        ("RS-XX8000-DVB-TX-MIB", "ostRackAmpUReg"),
        ("RS-XX8000-DVB-TX-MIB", "ostRackAmpPowerA"),
        ("RS-XX8000-DVB-TX-MIB", "ostRackAmpPowerB"),
        ("RS-XX8000-DVB-TX-MIB", "ostRackAmpPowerOut"),
        ("RS-XX8000-DVB-TX-MIB", "ostRackAmpPowerReflection"),
        ("RS-XX8000-DVB-TX-MIB", "ostRackAmpPowerReference"),
        ("RS-XX8000-DVB-TX-MIB", "ostRackAmpDeltaPhase"),
        ("RS-XX8000-DVB-TX-MIB", "ostRackAmpCmdDeltaPhase"))
)
if mibBuilder.loadTexts:
    groupAmpMeasureValues.setStatus("current")

groupRfProbes = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 4, 5, 1, 21)
)
groupRfProbes.setObjects(
      *(("RS-XX8000-DVB-TX-MIB", "rfProbesNetCCURfProbe1"),
        ("RS-XX8000-DVB-TX-MIB", "rfProbesNetCCURfProbe2"),
        ("RS-XX8000-DVB-TX-MIB", "rfProbesAntFwdNominal"),
        ("RS-XX8000-DVB-TX-MIB", "rfProbesAntFwdWarningLimit"),
        ("RS-XX8000-DVB-TX-MIB", "rfProbesAntFwdFailLimit"),
        ("RS-XX8000-DVB-TX-MIB", "rfProbesAntFwdDelayTimeRfFail"),
        ("RS-XX8000-DVB-TX-MIB", "rfProbesAntFwdSetOffset"),
        ("RS-XX8000-DVB-TX-MIB", "rfProbesAntFwdSetGain"),
        ("RS-XX8000-DVB-TX-MIB", "rfProbesAntReflWarningLimit"),
        ("RS-XX8000-DVB-TX-MIB", "rfProbesAntReflSetOffset"),
        ("RS-XX8000-DVB-TX-MIB", "rfProbesAntReflSetGain"),
        ("RS-XX8000-DVB-TX-MIB", "rfProbesOstFwdNominal"),
        ("RS-XX8000-DVB-TX-MIB", "rfProbesOstFwdWarningLimit"),
        ("RS-XX8000-DVB-TX-MIB", "rfProbesOstFwdFailLimit"),
        ("RS-XX8000-DVB-TX-MIB", "rfProbesOstFwdDelayTimeRfFail"),
        ("RS-XX8000-DVB-TX-MIB", "rfProbesOstFwdSetOffset"),
        ("RS-XX8000-DVB-TX-MIB", "rfProbesOstFwdSetGain"),
        ("RS-XX8000-DVB-TX-MIB", "rfProbesOstReflWarningLimit"),
        ("RS-XX8000-DVB-TX-MIB", "rfProbesOstReflSetOffset"),
        ("RS-XX8000-DVB-TX-MIB", "rfProbesOstReflSetGain"))
)
if mibBuilder.loadTexts:
    groupRfProbes.setStatus("current")

groupDummyLoadRF = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 4, 5, 1, 22)
)
groupDummyLoadRF.setObjects(
      *(("RS-XX8000-DVB-TX-MIB", "rfProbesDLFwdNominal"),
        ("RS-XX8000-DVB-TX-MIB", "rfProbesDLFwdWarningLimit"),
        ("RS-XX8000-DVB-TX-MIB", "rfProbesDLFwdFailLimit"),
        ("RS-XX8000-DVB-TX-MIB", "rfProbesDLFwdDelayTimeRfFail"),
        ("RS-XX8000-DVB-TX-MIB", "rfProbesDLFwdSetOffset"),
        ("RS-XX8000-DVB-TX-MIB", "rfProbesDLFwdSetGain"),
        ("RS-XX8000-DVB-TX-MIB", "rfProbesDLReflWarningLimit"),
        ("RS-XX8000-DVB-TX-MIB", "rfProbesDLReflSetOffset"),
        ("RS-XX8000-DVB-TX-MIB", "rfProbesDLReflSetGain"))
)
if mibBuilder.loadTexts:
    groupDummyLoadRF.setStatus("current")

groupExcCommon = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 4, 5, 1, 23)
)
groupExcCommon.setObjects(
      *(("RS-XX8000-DVB-TX-MIB", "cmdExcOpModeInputAutomatic"),
        ("RS-XX8000-DVB-TX-MIB", "cmdExcPreselectInput"),
        ("RS-XX8000-DVB-TX-MIB", "cmdExcMode"),
        ("RS-XX8000-DVB-TX-MIB", "cmdExcNetworkMode"),
        ("RS-XX8000-DVB-TX-MIB", "cmdExcTPSSource"),
        ("RS-XX8000-DVB-TX-MIB", "cmdExcEnableCellID"),
        ("RS-XX8000-DVB-TX-MIB", "cmdExcTxAddress"),
        ("RS-XX8000-DVB-TX-MIB", "cmdExcTxAutomatic"),
        ("RS-XX8000-DVB-TX-MIB", "cmdExcInputSeamless"),
        ("RS-XX8000-DVB-TX-MIB", "cmdExcInputPriority"),
        ("RS-XX8000-DVB-TX-MIB", "cmdExcInputCheckTimeForward"),
        ("RS-XX8000-DVB-TX-MIB", "cmdExcInputCheckTimeSwitchback"),
        ("RS-XX8000-DVB-TX-MIB", "cmdExcInputMuteOnFail"),
        ("RS-XX8000-DVB-TX-MIB", "cmdExcInputManualPreseletionHP1"),
        ("RS-XX8000-DVB-TX-MIB", "cmdExcInputManualPreseletionHP2"),
        ("RS-XX8000-DVB-TX-MIB", "cmdExcInputManualPreseletionLP1"),
        ("RS-XX8000-DVB-TX-MIB", "cmdExcInputManualPreseletionLP2"),
        ("RS-XX8000-DVB-TX-MIB", "cmdExcTPSManualBandwidth"),
        ("RS-XX8000-DVB-TX-MIB", "cmdExcTPSManualFFTLength"),
        ("RS-XX8000-DVB-TX-MIB", "cmdExcTPSManualGuardInterval"),
        ("RS-XX8000-DVB-TX-MIB", "cmdExcTPSManualConstellation"),
        ("RS-XX8000-DVB-TX-MIB", "cmdExcTPSManualCellID"),
        ("RS-XX8000-DVB-TX-MIB", "cmdExcTPSManualInterleaver"),
        ("RS-XX8000-DVB-TX-MIB", "cmdExcTPSManualCoderateHP"),
        ("RS-XX8000-DVB-TX-MIB", "cmdExcTPSManualCoderateLP"),
        ("RS-XX8000-DVB-TX-MIB", "cmdExcTPSManualTimeSlicingHP"),
        ("RS-XX8000-DVB-TX-MIB", "cmdExcTPSManualTimeSlicingLP"),
        ("RS-XX8000-DVB-TX-MIB", "cmdExcTPSManualFECHP"),
        ("RS-XX8000-DVB-TX-MIB", "cmdExcTPSManualFECLP"),
        ("RS-XX8000-DVB-TX-MIB", "cmdExcSFNStaticDelay"),
        ("RS-XX8000-DVB-TX-MIB", "cmdExcSFNDeviationTime"),
        ("RS-XX8000-DVB-TX-MIB", "cmdExcFrequency"),
        ("RS-XX8000-DVB-TX-MIB", "cmdExcReferenceSource"),
        ("RS-XX8000-DVB-TX-MIB", "cmdExcMuteOnPPSFail"),
        ("RS-XX8000-DVB-TX-MIB", "cmdExcMuteOnReferenceFail"),
        ("RS-XX8000-DVB-TX-MIB", "cmdExcTypeLossOfInput"),
        ("RS-XX8000-DVB-TX-MIB", "cmdExcRfOutput"),
        ("RS-XX8000-DVB-TX-MIB", "cmdExcRfOutputAttenuation"),
        ("RS-XX8000-DVB-TX-MIB", "cmdExcRfOutputRfSlope"),
        ("RS-XX8000-DVB-TX-MIB", "cmdExcRfOutputModulationSlope"),
        ("RS-XX8000-DVB-TX-MIB", "cmdExcRfIqAdjustTestsignal"),
        ("RS-XX8000-DVB-TX-MIB", "cmdExcRfIqAdjustBiasCoarseI"),
        ("RS-XX8000-DVB-TX-MIB", "cmdExcRfIqAdjustBiasCoarseQ"),
        ("RS-XX8000-DVB-TX-MIB", "cmdExcRfIqAdjustBiasFineI"),
        ("RS-XX8000-DVB-TX-MIB", "cmdExcRfIqAdjustBiasFineQ"),
        ("RS-XX8000-DVB-TX-MIB", "cmdExcRfIqAdjustGainI"),
        ("RS-XX8000-DVB-TX-MIB", "cmdExcRfIqAdjustGainQ"),
        ("RS-XX8000-DVB-TX-MIB", "cmdExcRfIqAdjustPhase"),
        ("RS-XX8000-DVB-TX-MIB", "cmdExcInpAutoReadyAfterChangeOv"),
        ("RS-XX8000-DVB-TX-MIB", "excInputChannelName"),
        ("RS-XX8000-DVB-TX-MIB", "excInputConnected"),
        ("RS-XX8000-DVB-TX-MIB", "excInputSeamless"),
        ("RS-XX8000-DVB-TX-MIB", "excInputPreselected"),
        ("RS-XX8000-DVB-TX-MIB", "excInputActive"),
        ("RS-XX8000-DVB-TX-MIB", "excInputMipFail"),
        ("RS-XX8000-DVB-TX-MIB", "excInputBandwidth"),
        ("RS-XX8000-DVB-TX-MIB", "excInputFFTLength"),
        ("RS-XX8000-DVB-TX-MIB", "excInputGuardInterval"),
        ("RS-XX8000-DVB-TX-MIB", "excInputConstellation"),
        ("RS-XX8000-DVB-TX-MIB", "excInputCellID"),
        ("RS-XX8000-DVB-TX-MIB", "excInputInterleaver"),
        ("RS-XX8000-DVB-TX-MIB", "excInputCodeRate"),
        ("RS-XX8000-DVB-TX-MIB", "excInputPacketLength"),
        ("RS-XX8000-DVB-TX-MIB", "excInputMeasuredDatarate"),
        ("RS-XX8000-DVB-TX-MIB", "excInputRequiredDatarate"),
        ("RS-XX8000-DVB-TX-MIB", "excInputMaximumDelay"),
        ("RS-XX8000-DVB-TX-MIB", "exciterANumberOfEntries"),
        ("RS-XX8000-DVB-TX-MIB", "exciterALogbookClear"),
        ("RS-XX8000-DVB-TX-MIB", "excALogbookEntryNbr"),
        ("RS-XX8000-DVB-TX-MIB", "excALogbookType"),
        ("RS-XX8000-DVB-TX-MIB", "excALogbookSlope"),
        ("RS-XX8000-DVB-TX-MIB", "excALogbookMessage"),
        ("RS-XX8000-DVB-TX-MIB", "excALogbookDateTime"),
        ("RS-XX8000-DVB-TX-MIB", "cmdExcOcxoAdjust"),
        ("RS-XX8000-DVB-TX-MIB", "cmdExcExpectInputReserve"),
        ("RS-XX8000-DVB-TX-MIB", "excStatusReqDataRateLP"),
        ("RS-XX8000-DVB-TX-MIB", "excStatusReqDataRateHP"),
        ("RS-XX8000-DVB-TX-MIB", "excStatusAmplifierControl"),
        ("RS-XX8000-DVB-TX-MIB", "excStatusFailDelay"),
        ("RS-XX8000-DVB-TX-MIB", "cmdExcFailDelayMode"),
        ("RS-XX8000-DVB-TX-MIB", "cmdExcInputFailDelayTime"),
        ("RS-XX8000-DVB-TX-MIB", "cmdExcRefFailDelayTime"))
)
if mibBuilder.loadTexts:
    groupExcCommon.setStatus("current")

groupExcAdditionalSx800 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 4, 5, 1, 24)
)
groupExcAdditionalSx800.setObjects(
      *(("RS-XX8000-DVB-TX-MIB", "cmdExcRfOutputRegulation"),
        ("RS-XX8000-DVB-TX-MIB", "cmdExcRfOutputManualRfLevel"),
        ("RS-XX8000-DVB-TX-MIB", "cmdExcRfIqAdjustStart"))
)
if mibBuilder.loadTexts:
    groupExcAdditionalSx800.setStatus("current")

groupExcAdditionalSLx = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 4, 5, 1, 25)
)
groupExcAdditionalSLx.setObjects(
      *(("RS-XX8000-DVB-TX-MIB", "cmdExcInput1Source"),
        ("RS-XX8000-DVB-TX-MIB", "cmdExcInput2Source"))
)
if mibBuilder.loadTexts:
    groupExcAdditionalSLx.setStatus("current")

groupExciterStatus = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 4, 5, 1, 27)
)
groupExciterStatus.setObjects(
      *(("RS-XX8000-DVB-TX-MIB", "excStatusRfOutputAgcRegulation"),
        ("RS-XX8000-DVB-TX-MIB", "excStatusRfIqAdjustAuto"),
        ("RS-XX8000-DVB-TX-MIB", "excStatusRfIqAdjustLO1Frequency"),
        ("RS-XX8000-DVB-TX-MIB", "excStatusSfnDelayProcessing"),
        ("RS-XX8000-DVB-TX-MIB", "excStatusSfnDelayDynamic"),
        ("RS-XX8000-DVB-TX-MIB", "excStatusSfnDelayNetwork"),
        ("RS-XX8000-DVB-TX-MIB", "excStatusSfnDelayTxOffset"),
        ("RS-XX8000-DVB-TX-MIB", "excStatusSfnDelayMaximum"),
        ("RS-XX8000-DVB-TX-MIB", "excStatusSfnDelayTotal"),
        ("RS-XX8000-DVB-TX-MIB", "excStatusNominalPower"))
)
if mibBuilder.loadTexts:
    groupExciterStatus.setStatus("current")

groupExciterPrecorrection = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 4, 5, 1, 28)
)
groupExciterPrecorrection.setObjects(
      *(("RS-XX8000-DVB-TX-MIB", "excPrecLinCorrection"),
        ("RS-XX8000-DVB-TX-MIB", "excPrecLinAutomaticADE"),
        ("RS-XX8000-DVB-TX-MIB", "excPrecLinMaxAmplitudeRipple"),
        ("RS-XX8000-DVB-TX-MIB", "excPrecLinMaxGroupDelayRipple"),
        ("RS-XX8000-DVB-TX-MIB", "excPrecLinAmplitudeRipple"),
        ("RS-XX8000-DVB-TX-MIB", "excPrecLinGroupDelayRipple"),
        ("RS-XX8000-DVB-TX-MIB", "excPrecLinInputLevel"),
        ("RS-XX8000-DVB-TX-MIB", "excPrecLinAutomatic"),
        ("RS-XX8000-DVB-TX-MIB", "excPrecNonlinCorrection"),
        ("RS-XX8000-DVB-TX-MIB", "excPrecNonlinAutomaticADE"),
        ("RS-XX8000-DVB-TX-MIB", "excPrecNonlinThresholdShoulders"),
        ("RS-XX8000-DVB-TX-MIB", "excPrecNonlinShoulderLeft"),
        ("RS-XX8000-DVB-TX-MIB", "excPrecNonlinShoulderRight"),
        ("RS-XX8000-DVB-TX-MIB", "excPrecNonlinInputLevel"),
        ("RS-XX8000-DVB-TX-MIB", "excPrecNonlinAutomatic"))
)
if mibBuilder.loadTexts:
    groupExciterPrecorrection.setStatus("current")

groupSLx = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 4, 5, 1, 29)
)
groupSLx.setObjects(
      *(("RS-XX8000-DVB-TX-MIB", "cmdExcTransmitterType"),
        ("RS-XX8000-DVB-TX-MIB", "cmdExcTimeScheduler"),
        ("RS-XX8000-DVB-TX-MIB", "excPrecUserState"),
        ("RS-XX8000-DVB-TX-MIB", "excPrecFactoryState"),
        ("RS-XX8000-DVB-TX-MIB", "excPrecRestoreCurrentSettings"),
        ("RS-XX8000-DVB-TX-MIB", "excPrecRestoreAllSettings"),
        ("RS-XX8000-DVB-TX-MIB", "configTvStandardName"),
        ("RS-XX8000-DVB-TX-MIB", "configFrequency"),
        ("RS-XX8000-DVB-TX-MIB", "configPower"),
        ("RS-XX8000-DVB-TX-MIB", "schedulerRowStatus"),
        ("RS-XX8000-DVB-TX-MIB", "schedulerEvent"),
        ("RS-XX8000-DVB-TX-MIB", "schedulerDateTime"),
        ("RS-XX8000-DVB-TX-MIB", "config2InputSource"),
        ("RS-XX8000-DVB-TX-MIB", "config2Power"),
        ("RS-XX8000-DVB-TX-MIB", "config2Frequency"),
        ("RS-XX8000-DVB-TX-MIB", "config2RxFrequency"),
        ("RS-XX8000-DVB-TX-MIB", "config2TvStandardName"),
        ("RS-XX8000-DVB-TX-MIB", "excStatusVSWR"),
        ("RS-XX8000-DVB-TX-MIB", "cmdExcMuteCondition"),
        ("RS-XX8000-DVB-TX-MIB", "schedulerTvStandard"),
        ("RS-XX8000-DVB-TX-MIB", "configRxFrequency"),
        ("RS-XX8000-DVB-TX-MIB", "configInputSource"))
)
if mibBuilder.loadTexts:
    groupSLx.setStatus("current")

groupObjectsACU = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 4, 5, 1, 30)
)
groupObjectsACU.setObjects(
      *(("RS-XX8000-DVB-TX-MIB", "cmdExcRfWarningLimit"),
        ("RS-XX8000-DVB-TX-MIB", "cmdExcRfFailLimit"),
        ("RS-XX8000-DVB-TX-MIB", "cmdExcOutputPower"),
        ("RS-XX8000-DVB-TX-MIB", "cmdExcMonitoringOutput"))
)
if mibBuilder.loadTexts:
    groupObjectsACU.setStatus("current")

groupIndependentRacks = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 4, 5, 1, 31)
)
groupIndependentRacks.setObjects(
      *(("RS-XX8000-DVB-TX-MIB", "rackReferenceVoltage"),
        ("RS-XX8000-DVB-TX-MIB", "amplifiersPowerSupply"),
        ("RS-XX8000-DVB-TX-MIB", "rackOnOff"))
)
if mibBuilder.loadTexts:
    groupIndependentRacks.setStatus("current")

groupObjectsRE = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 4, 5, 1, 32)
)
groupObjectsRE.setObjects(
    ("RS-XX8000-DVB-TX-MIB", "summaryFaultExcA")
)
if mibBuilder.loadTexts:
    groupObjectsRE.setStatus("current")

groupObjsAdditionalPowerSupply = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 4, 5, 1, 36)
)
groupObjsAdditionalPowerSupply.setObjects(
      *(("RS-XX8000-DVB-TX-MIB", "internalPowerSupply"),
        ("RS-XX8000-DVB-TX-MIB", "externalPowerSupply"))
)
if mibBuilder.loadTexts:
    groupObjsAdditionalPowerSupply.setStatus("current")

groupObjectsControlExciter = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 4, 5, 1, 37)
)
groupObjectsControlExciter.setObjects(
      *(("RS-XX8000-DVB-TX-MIB", "cmdTxOperationModeReserve"),
        ("RS-XX8000-DVB-TX-MIB", "cmdTxOpModeExcAutomatic"),
        ("RS-XX8000-DVB-TX-MIB", "cmdTxDelayTimeExcAutomatic"),
        ("RS-XX8000-DVB-TX-MIB", "summaryFaultExcB"),
        ("RS-XX8000-DVB-TX-MIB", "exciterAutomaticReady"),
        ("RS-XX8000-DVB-TX-MIB", "exciterAutomaticChanged"),
        ("RS-XX8000-DVB-TX-MIB", "exciterAutomaticFault"),
        ("RS-XX8000-DVB-TX-MIB", "noConnectionExcB"),
        ("RS-XX8000-DVB-TX-MIB", "activeExcB"),
        ("RS-XX8000-DVB-TX-MIB", "cmdTxProgramExciterPrio"),
        ("RS-XX8000-DVB-TX-MIB", "cmdTxChangeOver"),
        ("RS-XX8000-DVB-TX-MIB", "cmdTxSwitchPosition"))
)
if mibBuilder.loadTexts:
    groupObjectsControlExciter.setStatus("current")

groupObjectsSingleEnded = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 4, 5, 1, 38)
)
groupObjectsSingleEnded.setObjects(
    ("RS-XX8000-DVB-TX-MIB", "cmdTxRfSwitch")
)
if mibBuilder.loadTexts:
    groupObjectsSingleEnded.setStatus("current")

groupObjectsSx801Amplifier = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 4, 5, 1, 39)
)
groupObjectsSx801Amplifier.setObjects(
      *(("RS-XX8000-DVB-TX-MIB", "sx801AmpRfOut"),
        ("RS-XX8000-DVB-TX-MIB", "sx801AmpRfIn"),
        ("RS-XX8000-DVB-TX-MIB", "sx801AmpReflection"),
        ("RS-XX8000-DVB-TX-MIB", "sx801AmpOn"),
        ("RS-XX8000-DVB-TX-MIB", "sx801AmpAC"),
        ("RS-XX8000-DVB-TX-MIB", "sx801AmpCommunication"),
        ("RS-XX8000-DVB-TX-MIB", "sx801AmpTransistor"),
        ("RS-XX8000-DVB-TX-MIB", "sx801AmpDriver"),
        ("RS-XX8000-DVB-TX-MIB", "sx801AmpTemperature"),
        ("RS-XX8000-DVB-TX-MIB", "sx801AmpBlower"),
        ("RS-XX8000-DVB-TX-MIB", "sx801AmpRegulation"),
        ("RS-XX8000-DVB-TX-MIB", "sx801AmpUpdate"),
        ("RS-XX8000-DVB-TX-MIB", "sx801Supply1Temperature"),
        ("RS-XX8000-DVB-TX-MIB", "sx801Supply2Temperature"),
        ("RS-XX8000-DVB-TX-MIB", "sx801SupplyRTemperature"),
        ("RS-XX8000-DVB-TX-MIB", "sx801Supply1DC"),
        ("RS-XX8000-DVB-TX-MIB", "sx801Supply2DC"),
        ("RS-XX8000-DVB-TX-MIB", "sx801SupplyRDC"),
        ("RS-XX8000-DVB-TX-MIB", "sx801AmpValueI1"),
        ("RS-XX8000-DVB-TX-MIB", "sx801AmpValueI2"),
        ("RS-XX8000-DVB-TX-MIB", "sx801AmpValueI3"),
        ("RS-XX8000-DVB-TX-MIB", "sx801AmpValueI4"),
        ("RS-XX8000-DVB-TX-MIB", "sx801AmpValueIPre"),
        ("RS-XX8000-DVB-TX-MIB", "sx801AmpValueIDrv1"),
        ("RS-XX8000-DVB-TX-MIB", "sx801AmpValueIDrv2"),
        ("RS-XX8000-DVB-TX-MIB", "sx801AmpValuePowerOut"),
        ("RS-XX8000-DVB-TX-MIB", "sx801AmpValueReflection"),
        ("RS-XX8000-DVB-TX-MIB", "sx801AmpValueVRef"),
        ("RS-XX8000-DVB-TX-MIB", "sx801AmpValueVReg"),
        ("RS-XX8000-DVB-TX-MIB", "sx801AmpValueTemperature"),
        ("RS-XX8000-DVB-TX-MIB", "sx801AmpValueMonAtt"),
        ("RS-XX8000-DVB-TX-MIB", "sx801AmpValueVAux1"),
        ("RS-XX8000-DVB-TX-MIB", "sx801AmpValueVAux2"),
        ("RS-XX8000-DVB-TX-MIB", "sx801Supply1ValuePwr"),
        ("RS-XX8000-DVB-TX-MIB", "sx801Supply2ValuePwr"),
        ("RS-XX8000-DVB-TX-MIB", "sx801Supply1ValueDc"),
        ("RS-XX8000-DVB-TX-MIB", "sx801Supply2ValueDc"))
)
if mibBuilder.loadTexts:
    groupObjectsSx801Amplifier.setStatus("current")

groupObsoleted = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 4, 5, 1, 99)
)
groupObsoleted.setObjects(
      *(("RS-XX8000-DVB-TX-MIB", "cmdTxParametersetReSave"),
        ("RS-XX8000-DVB-TX-MIB", "cmdExcTimeForDailyPcrReset"),
        ("RS-XX8000-DVB-TX-MIB", "cmdExcEnablePcrReset"),
        ("RS-XX8000-DVB-TX-MIB", "excInputAlpha"),
        ("RS-XX8000-DVB-TX-MIB", "cmdExcTPSManualAlpha"),
        ("RS-XX8000-DVB-TX-MIB", "rfProbeConfigurationLabel"),
        ("RS-XX8000-DVB-TX-MIB", "cmdExcInputAutoSwitch"))
)
if mibBuilder.loadTexts:
    groupObsoleted.setStatus("obsolete")


# Notification objects

txSummaryFault = NotificationType(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 4, 3, 2, 0, 1)
)
txSummaryFault.setObjects(
      *(("RS-XX8000-COMMON-MIB", "eventAlarmPriority"),
        ("RS-XX8000-COMMON-MIB", "eventAlarmClass"),
        ("RS-XX8000-COMMON-MIB", "eventEvent"))
)
if mibBuilder.loadTexts:
    txSummaryFault.setStatus(
        "current"
    )

txSummaryWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 4, 3, 2, 0, 2)
)
txSummaryWarning.setObjects(
      *(("RS-XX8000-COMMON-MIB", "eventAlarmPriority"),
        ("RS-XX8000-COMMON-MIB", "eventAlarmClass"),
        ("RS-XX8000-COMMON-MIB", "eventEvent"))
)
if mibBuilder.loadTexts:
    txSummaryWarning.setStatus(
        "current"
    )

txLocal = NotificationType(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 4, 3, 2, 0, 3)
)
txLocal.setObjects(
      *(("RS-XX8000-COMMON-MIB", "eventAlarmPriority"),
        ("RS-XX8000-COMMON-MIB", "eventAlarmClass"),
        ("RS-XX8000-COMMON-MIB", "eventEvent"))
)
if mibBuilder.loadTexts:
    txLocal.setStatus(
        "current"
    )

txRfOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 4, 3, 2, 0, 4)
)
txRfOn.setObjects(
      *(("RS-XX8000-COMMON-MIB", "eventAlarmPriority"),
        ("RS-XX8000-COMMON-MIB", "eventAlarmClass"),
        ("RS-XX8000-COMMON-MIB", "eventEvent"))
)
if mibBuilder.loadTexts:
    txRfOn.setStatus(
        "current"
    )

txRfOk = NotificationType(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 4, 3, 2, 0, 5)
)
txRfOk.setObjects(
      *(("RS-XX8000-COMMON-MIB", "eventAlarmPriority"),
        ("RS-XX8000-COMMON-MIB", "eventAlarmClass"),
        ("RS-XX8000-COMMON-MIB", "eventEvent"))
)
if mibBuilder.loadTexts:
    txRfOk.setStatus(
        "current"
    )

txParamSetSubDeviceDiffers = NotificationType(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 4, 3, 2, 0, 6)
)
txParamSetSubDeviceDiffers.setObjects(
      *(("RS-XX8000-COMMON-MIB", "eventAlarmPriority"),
        ("RS-XX8000-COMMON-MIB", "eventAlarmClass"),
        ("RS-XX8000-COMMON-MIB", "eventEvent"))
)
if mibBuilder.loadTexts:
    txParamSetSubDeviceDiffers.setStatus(
        "obsolete"
    )

txParamSetValuesChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 4, 3, 2, 0, 7)
)
txParamSetValuesChanged.setObjects(
      *(("RS-XX8000-COMMON-MIB", "eventAlarmPriority"),
        ("RS-XX8000-COMMON-MIB", "eventAlarmClass"),
        ("RS-XX8000-COMMON-MIB", "eventEvent"))
)
if mibBuilder.loadTexts:
    txParamSetValuesChanged.setStatus(
        "current"
    )

txRfLoopProgram = NotificationType(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 4, 3, 2, 0, 8)
)
txRfLoopProgram.setObjects(
      *(("RS-XX8000-COMMON-MIB", "eventAlarmPriority"),
        ("RS-XX8000-COMMON-MIB", "eventAlarmClass"),
        ("RS-XX8000-COMMON-MIB", "eventEvent"))
)
if mibBuilder.loadTexts:
    txRfLoopProgram.setStatus(
        "current"
    )

txRfLoopReserve = NotificationType(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 4, 3, 2, 0, 9)
)
txRfLoopReserve.setObjects(
      *(("RS-XX8000-COMMON-MIB", "eventAlarmPriority"),
        ("RS-XX8000-COMMON-MIB", "eventAlarmClass"),
        ("RS-XX8000-COMMON-MIB", "eventEvent"))
)
if mibBuilder.loadTexts:
    txRfLoopReserve.setStatus(
        "current"
    )

txRfWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 4, 3, 2, 0, 10)
)
txRfWarning.setObjects(
      *(("RS-XX8000-COMMON-MIB", "eventAlarmPriority"),
        ("RS-XX8000-COMMON-MIB", "eventAlarmClass"),
        ("RS-XX8000-COMMON-MIB", "eventEvent"))
)
if mibBuilder.loadTexts:
    txRfWarning.setStatus(
        "current"
    )

txReflectionWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 4, 3, 2, 0, 11)
)
txReflectionWarning.setObjects(
      *(("RS-XX8000-COMMON-MIB", "eventAlarmPriority"),
        ("RS-XX8000-COMMON-MIB", "eventAlarmClass"),
        ("RS-XX8000-COMMON-MIB", "eventEvent"))
)
if mibBuilder.loadTexts:
    txReflectionWarning.setStatus(
        "current"
    )

txNetCCUFanFault = NotificationType(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 4, 3, 2, 0, 12)
)
txNetCCUFanFault.setObjects(
      *(("RS-XX8000-COMMON-MIB", "eventAlarmPriority"),
        ("RS-XX8000-COMMON-MIB", "eventAlarmClass"),
        ("RS-XX8000-COMMON-MIB", "eventEvent"))
)
if mibBuilder.loadTexts:
    txNetCCUFanFault.setStatus(
        "current"
    )

txNetCCUPowerSupply = NotificationType(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 4, 3, 2, 0, 13)
)
txNetCCUPowerSupply.setObjects(
      *(("RS-XX8000-COMMON-MIB", "eventAlarmPriority"),
        ("RS-XX8000-COMMON-MIB", "eventAlarmClass"),
        ("RS-XX8000-COMMON-MIB", "eventEvent"))
)
if mibBuilder.loadTexts:
    txNetCCUPowerSupply.setStatus(
        "current"
    )

txRfFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 4, 3, 2, 0, 14)
)
txRfFail.setObjects(
      *(("RS-XX8000-COMMON-MIB", "eventAlarmPriority"),
        ("RS-XX8000-COMMON-MIB", "eventAlarmClass"),
        ("RS-XX8000-COMMON-MIB", "eventEvent"))
)
if mibBuilder.loadTexts:
    txRfFail.setStatus(
        "current"
    )

txReflectionFault = NotificationType(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 4, 3, 2, 0, 15)
)
txReflectionFault.setObjects(
      *(("RS-XX8000-COMMON-MIB", "eventAlarmPriority"),
        ("RS-XX8000-COMMON-MIB", "eventAlarmClass"),
        ("RS-XX8000-COMMON-MIB", "eventEvent"))
)
if mibBuilder.loadTexts:
    txReflectionFault.setStatus(
        "current"
    )

txNetCCUBoardTemperatureFault = NotificationType(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 4, 3, 2, 0, 16)
)
txNetCCUBoardTemperatureFault.setObjects(
      *(("RS-XX8000-COMMON-MIB", "eventAlarmPriority"),
        ("RS-XX8000-COMMON-MIB", "eventAlarmClass"),
        ("RS-XX8000-COMMON-MIB", "eventEvent"))
)
if mibBuilder.loadTexts:
    txNetCCUBoardTemperatureFault.setStatus(
        "deprecated"
    )

txNetCCUNoConnectionToExcA = NotificationType(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 4, 3, 2, 0, 17)
)
txNetCCUNoConnectionToExcA.setObjects(
      *(("RS-XX8000-COMMON-MIB", "eventAlarmPriority"),
        ("RS-XX8000-COMMON-MIB", "eventAlarmClass"),
        ("RS-XX8000-COMMON-MIB", "eventEvent"))
)
if mibBuilder.loadTexts:
    txNetCCUNoConnectionToExcA.setStatus(
        "current"
    )

txNetCCUNoConnectionToOstA = NotificationType(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 4, 3, 2, 0, 18)
)
txNetCCUNoConnectionToOstA.setObjects(
      *(("RS-XX8000-COMMON-MIB", "eventAlarmPriority"),
        ("RS-XX8000-COMMON-MIB", "eventAlarmClass"),
        ("RS-XX8000-COMMON-MIB", "eventEvent"))
)
if mibBuilder.loadTexts:
    txNetCCUNoConnectionToOstA.setStatus(
        "current"
    )

txNetCCUNoConnectionToExcB = NotificationType(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 4, 3, 2, 0, 19)
)
txNetCCUNoConnectionToExcB.setObjects(
      *(("RS-XX8000-COMMON-MIB", "eventAlarmPriority"),
        ("RS-XX8000-COMMON-MIB", "eventAlarmClass"),
        ("RS-XX8000-COMMON-MIB", "eventEvent"))
)
if mibBuilder.loadTexts:
    txNetCCUNoConnectionToExcB.setStatus(
        "current"
    )

txNetCCUNoConnectionToOstB = NotificationType(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 4, 3, 2, 0, 20)
)
txNetCCUNoConnectionToOstB.setObjects(
      *(("RS-XX8000-COMMON-MIB", "eventAlarmPriority"),
        ("RS-XX8000-COMMON-MIB", "eventAlarmClass"),
        ("RS-XX8000-COMMON-MIB", "eventEvent"))
)
if mibBuilder.loadTexts:
    txNetCCUNoConnectionToOstB.setStatus(
        "current"
    )

txAutomaticExcReady = NotificationType(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 4, 3, 2, 0, 21)
)
txAutomaticExcReady.setObjects(
      *(("RS-XX8000-COMMON-MIB", "eventAlarmPriority"),
        ("RS-XX8000-COMMON-MIB", "eventAlarmClass"),
        ("RS-XX8000-COMMON-MIB", "eventEvent"))
)
if mibBuilder.loadTexts:
    txAutomaticExcReady.setStatus(
        "current"
    )

txAutomaticExcChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 4, 3, 2, 0, 22)
)
txAutomaticExcChanged.setObjects(
      *(("RS-XX8000-COMMON-MIB", "eventAlarmPriority"),
        ("RS-XX8000-COMMON-MIB", "eventAlarmClass"),
        ("RS-XX8000-COMMON-MIB", "eventEvent"))
)
if mibBuilder.loadTexts:
    txAutomaticExcChanged.setStatus(
        "current"
    )

txAutomaticExcFault = NotificationType(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 4, 3, 2, 0, 23)
)
txAutomaticExcFault.setObjects(
      *(("RS-XX8000-COMMON-MIB", "eventAlarmPriority"),
        ("RS-XX8000-COMMON-MIB", "eventAlarmClass"),
        ("RS-XX8000-COMMON-MIB", "eventEvent"))
)
if mibBuilder.loadTexts:
    txAutomaticExcFault.setStatus(
        "current"
    )

txAutomaticOstReady = NotificationType(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 4, 3, 2, 0, 24)
)
txAutomaticOstReady.setObjects(
      *(("RS-XX8000-COMMON-MIB", "eventAlarmPriority"),
        ("RS-XX8000-COMMON-MIB", "eventAlarmClass"),
        ("RS-XX8000-COMMON-MIB", "eventEvent"))
)
if mibBuilder.loadTexts:
    txAutomaticOstReady.setStatus(
        "current"
    )

txAutomaticOstChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 4, 3, 2, 0, 25)
)
txAutomaticOstChanged.setObjects(
      *(("RS-XX8000-COMMON-MIB", "eventAlarmPriority"),
        ("RS-XX8000-COMMON-MIB", "eventAlarmClass"),
        ("RS-XX8000-COMMON-MIB", "eventEvent"))
)
if mibBuilder.loadTexts:
    txAutomaticOstChanged.setStatus(
        "current"
    )

txAutomaticOstFault = NotificationType(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 4, 3, 2, 0, 26)
)
txAutomaticOstFault.setObjects(
      *(("RS-XX8000-COMMON-MIB", "eventAlarmPriority"),
        ("RS-XX8000-COMMON-MIB", "eventAlarmClass"),
        ("RS-XX8000-COMMON-MIB", "eventEvent"))
)
if mibBuilder.loadTexts:
    txAutomaticOstFault.setStatus(
        "current"
    )

txNetCCUBoardTemperatureWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 4, 3, 2, 0, 27)
)
txNetCCUBoardTemperatureWarning.setObjects(
      *(("RS-XX8000-COMMON-MIB", "eventAlarmPriority"),
        ("RS-XX8000-COMMON-MIB", "eventAlarmClass"),
        ("RS-XX8000-COMMON-MIB", "eventEvent"))
)
if mibBuilder.loadTexts:
    txNetCCUBoardTemperatureWarning.setStatus(
        "current"
    )

txInternalPowerSupplyWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 4, 3, 2, 0, 30)
)
txInternalPowerSupplyWarning.setObjects(
      *(("RS-XX8000-COMMON-MIB", "eventAlarmPriority"),
        ("RS-XX8000-COMMON-MIB", "eventAlarmClass"),
        ("RS-XX8000-COMMON-MIB", "eventEvent"))
)
if mibBuilder.loadTexts:
    txInternalPowerSupplyWarning.setStatus(
        "current"
    )

txExternalPowerSupplyWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 4, 3, 2, 0, 31)
)
txExternalPowerSupplyWarning.setObjects(
      *(("RS-XX8000-COMMON-MIB", "eventAlarmPriority"),
        ("RS-XX8000-COMMON-MIB", "eventAlarmClass"),
        ("RS-XX8000-COMMON-MIB", "eventEvent"))
)
if mibBuilder.loadTexts:
    txExternalPowerSupplyWarning.setStatus(
        "current"
    )

txModeSwitchOverStarted = NotificationType(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 4, 3, 2, 0, 35)
)
txModeSwitchOverStarted.setObjects(
      *(("RS-XX8000-COMMON-MIB", "eventAlarmPriority"),
        ("RS-XX8000-COMMON-MIB", "eventAlarmClass"),
        ("RS-XX8000-COMMON-MIB", "eventEvent"))
)
if mibBuilder.loadTexts:
    txModeSwitchOverStarted.setStatus(
        "current"
    )

txModeSwitchOverEnded = NotificationType(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 4, 3, 2, 0, 36)
)
txModeSwitchOverEnded.setObjects(
      *(("RS-XX8000-COMMON-MIB", "eventAlarmPriority"),
        ("RS-XX8000-COMMON-MIB", "eventAlarmClass"),
        ("RS-XX8000-COMMON-MIB", "eventEvent"))
)
if mibBuilder.loadTexts:
    txModeSwitchOverEnded.setStatus(
        "current"
    )

txModeInconsistent = NotificationType(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 4, 3, 2, 0, 37)
)
txModeInconsistent.setObjects(
      *(("RS-XX8000-COMMON-MIB", "eventAlarmPriority"),
        ("RS-XX8000-COMMON-MIB", "eventAlarmClass"),
        ("RS-XX8000-COMMON-MIB", "eventEvent"))
)
if mibBuilder.loadTexts:
    txModeInconsistent.setStatus(
        "current"
    )

txModeSwitchOverFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 4, 3, 2, 0, 38)
)
txModeSwitchOverFailed.setObjects(
      *(("RS-XX8000-COMMON-MIB", "eventAlarmPriority"),
        ("RS-XX8000-COMMON-MIB", "eventAlarmClass"),
        ("RS-XX8000-COMMON-MIB", "eventEvent"))
)
if mibBuilder.loadTexts:
    txModeSwitchOverFailed.setStatus(
        "current"
    )

txExcSummaryFault = NotificationType(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 4, 3, 2, 0, 100)
)
txExcSummaryFault.setObjects(
      *(("RS-XX8000-COMMON-MIB", "eventAlarmPriority"),
        ("RS-XX8000-COMMON-MIB", "eventAlarmClass"),
        ("RS-XX8000-COMMON-MIB", "eventEvent"),
        ("RS-XX8000-COMMON-MIB", "indexAB"))
)
if mibBuilder.loadTexts:
    txExcSummaryFault.setStatus(
        "current"
    )

txExcSummaryWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 4, 3, 2, 0, 101)
)
txExcSummaryWarning.setObjects(
      *(("RS-XX8000-COMMON-MIB", "eventAlarmPriority"),
        ("RS-XX8000-COMMON-MIB", "eventAlarmClass"),
        ("RS-XX8000-COMMON-MIB", "eventEvent"),
        ("RS-XX8000-COMMON-MIB", "indexAB"))
)
if mibBuilder.loadTexts:
    txExcSummaryWarning.setStatus(
        "current"
    )

txExcLocal = NotificationType(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 4, 3, 2, 0, 102)
)
txExcLocal.setObjects(
      *(("RS-XX8000-COMMON-MIB", "eventAlarmPriority"),
        ("RS-XX8000-COMMON-MIB", "eventAlarmClass"),
        ("RS-XX8000-COMMON-MIB", "eventEvent"),
        ("RS-XX8000-COMMON-MIB", "indexAB"))
)
if mibBuilder.loadTexts:
    txExcLocal.setStatus(
        "current"
    )

txExcRfOk = NotificationType(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 4, 3, 2, 0, 104)
)
txExcRfOk.setObjects(
      *(("RS-XX8000-COMMON-MIB", "eventAlarmPriority"),
        ("RS-XX8000-COMMON-MIB", "eventAlarmClass"),
        ("RS-XX8000-COMMON-MIB", "eventEvent"),
        ("RS-XX8000-COMMON-MIB", "indexAB"))
)
if mibBuilder.loadTexts:
    txExcRfOk.setStatus(
        "current"
    )

txExcInputNoConnectHP1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 4, 3, 2, 0, 105)
)
txExcInputNoConnectHP1.setObjects(
      *(("RS-XX8000-COMMON-MIB", "eventAlarmPriority"),
        ("RS-XX8000-COMMON-MIB", "eventAlarmClass"),
        ("RS-XX8000-COMMON-MIB", "eventEvent"),
        ("RS-XX8000-COMMON-MIB", "indexAB"))
)
if mibBuilder.loadTexts:
    txExcInputNoConnectHP1.setStatus(
        "current"
    )

txExcInputNoConnectLP1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 4, 3, 2, 0, 106)
)
txExcInputNoConnectLP1.setObjects(
      *(("RS-XX8000-COMMON-MIB", "eventAlarmPriority"),
        ("RS-XX8000-COMMON-MIB", "eventAlarmClass"),
        ("RS-XX8000-COMMON-MIB", "eventEvent"),
        ("RS-XX8000-COMMON-MIB", "indexAB"))
)
if mibBuilder.loadTexts:
    txExcInputNoConnectLP1.setStatus(
        "current"
    )

txExcInputNoConnectHP2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 4, 3, 2, 0, 107)
)
txExcInputNoConnectHP2.setObjects(
      *(("RS-XX8000-COMMON-MIB", "eventAlarmPriority"),
        ("RS-XX8000-COMMON-MIB", "eventAlarmClass"),
        ("RS-XX8000-COMMON-MIB", "eventEvent"),
        ("RS-XX8000-COMMON-MIB", "indexAB"))
)
if mibBuilder.loadTexts:
    txExcInputNoConnectHP2.setStatus(
        "current"
    )

txExcInputNoConnectLP2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 4, 3, 2, 0, 108)
)
txExcInputNoConnectLP2.setObjects(
      *(("RS-XX8000-COMMON-MIB", "eventAlarmPriority"),
        ("RS-XX8000-COMMON-MIB", "eventAlarmClass"),
        ("RS-XX8000-COMMON-MIB", "eventEvent"),
        ("RS-XX8000-COMMON-MIB", "indexAB"))
)
if mibBuilder.loadTexts:
    txExcInputNoConnectLP2.setStatus(
        "current"
    )

txExcInputActiveHP1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 4, 3, 2, 0, 109)
)
txExcInputActiveHP1.setObjects(
      *(("RS-XX8000-COMMON-MIB", "eventAlarmPriority"),
        ("RS-XX8000-COMMON-MIB", "eventAlarmClass"),
        ("RS-XX8000-COMMON-MIB", "eventEvent"),
        ("RS-XX8000-COMMON-MIB", "indexAB"))
)
if mibBuilder.loadTexts:
    txExcInputActiveHP1.setStatus(
        "current"
    )

txExcInputActiveLP1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 4, 3, 2, 0, 110)
)
txExcInputActiveLP1.setObjects(
      *(("RS-XX8000-COMMON-MIB", "eventAlarmPriority"),
        ("RS-XX8000-COMMON-MIB", "eventAlarmClass"),
        ("RS-XX8000-COMMON-MIB", "eventEvent"),
        ("RS-XX8000-COMMON-MIB", "indexAB"))
)
if mibBuilder.loadTexts:
    txExcInputActiveLP1.setStatus(
        "current"
    )

txExcInputActiveHP2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 4, 3, 2, 0, 111)
)
txExcInputActiveHP2.setObjects(
      *(("RS-XX8000-COMMON-MIB", "eventAlarmPriority"),
        ("RS-XX8000-COMMON-MIB", "eventAlarmClass"),
        ("RS-XX8000-COMMON-MIB", "eventEvent"),
        ("RS-XX8000-COMMON-MIB", "indexAB"))
)
if mibBuilder.loadTexts:
    txExcInputActiveHP2.setStatus(
        "current"
    )

txExcInputActiveLP2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 4, 3, 2, 0, 112)
)
txExcInputActiveLP2.setObjects(
      *(("RS-XX8000-COMMON-MIB", "eventAlarmPriority"),
        ("RS-XX8000-COMMON-MIB", "eventAlarmClass"),
        ("RS-XX8000-COMMON-MIB", "eventEvent"),
        ("RS-XX8000-COMMON-MIB", "indexAB"))
)
if mibBuilder.loadTexts:
    txExcInputActiveLP2.setStatus(
        "current"
    )

txExcOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 4, 3, 2, 0, 113)
)
txExcOn.setObjects(
      *(("RS-XX8000-COMMON-MIB", "eventAlarmPriority"),
        ("RS-XX8000-COMMON-MIB", "eventAlarmClass"),
        ("RS-XX8000-COMMON-MIB", "eventEvent"),
        ("RS-XX8000-COMMON-MIB", "indexAB"))
)
if mibBuilder.loadTexts:
    txExcOn.setStatus(
        "current"
    )

txExcRfOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 4, 3, 2, 0, 114)
)
txExcRfOn.setObjects(
      *(("RS-XX8000-COMMON-MIB", "eventAlarmPriority"),
        ("RS-XX8000-COMMON-MIB", "eventAlarmClass"),
        ("RS-XX8000-COMMON-MIB", "eventEvent"),
        ("RS-XX8000-COMMON-MIB", "indexAB"))
)
if mibBuilder.loadTexts:
    txExcRfOn.setStatus(
        "current"
    )

txExcNoInput = NotificationType(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 4, 3, 2, 0, 115)
)
txExcNoInput.setObjects(
      *(("RS-XX8000-COMMON-MIB", "eventAlarmPriority"),
        ("RS-XX8000-COMMON-MIB", "eventAlarmClass"),
        ("RS-XX8000-COMMON-MIB", "eventEvent"),
        ("RS-XX8000-COMMON-MIB", "indexAB"))
)
if mibBuilder.loadTexts:
    txExcNoInput.setStatus(
        "current"
    )

txExcRfLoop = NotificationType(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 4, 3, 2, 0, 116)
)
txExcRfLoop.setObjects(
      *(("RS-XX8000-COMMON-MIB", "eventAlarmPriority"),
        ("RS-XX8000-COMMON-MIB", "eventAlarmClass"),
        ("RS-XX8000-COMMON-MIB", "eventEvent"),
        ("RS-XX8000-COMMON-MIB", "indexAB"))
)
if mibBuilder.loadTexts:
    txExcRfLoop.setStatus(
        "current"
    )

txExcRfFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 4, 3, 2, 0, 117)
)
txExcRfFail.setObjects(
      *(("RS-XX8000-COMMON-MIB", "eventAlarmPriority"),
        ("RS-XX8000-COMMON-MIB", "eventAlarmClass"),
        ("RS-XX8000-COMMON-MIB", "eventEvent"),
        ("RS-XX8000-COMMON-MIB", "indexAB"))
)
if mibBuilder.loadTexts:
    txExcRfFail.setStatus(
        "current"
    )

txExcSelfTest = NotificationType(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 4, 3, 2, 0, 118)
)
txExcSelfTest.setObjects(
      *(("RS-XX8000-COMMON-MIB", "eventAlarmPriority"),
        ("RS-XX8000-COMMON-MIB", "eventAlarmClass"),
        ("RS-XX8000-COMMON-MIB", "eventEvent"),
        ("RS-XX8000-COMMON-MIB", "indexAB"))
)
if mibBuilder.loadTexts:
    txExcSelfTest.setStatus(
        "current"
    )

txExcOutputOpen = NotificationType(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 4, 3, 2, 0, 119)
)
txExcOutputOpen.setObjects(
      *(("RS-XX8000-COMMON-MIB", "eventAlarmPriority"),
        ("RS-XX8000-COMMON-MIB", "eventAlarmClass"),
        ("RS-XX8000-COMMON-MIB", "eventEvent"),
        ("RS-XX8000-COMMON-MIB", "indexAB"))
)
if mibBuilder.loadTexts:
    txExcOutputOpen.setStatus(
        "current"
    )

txExcBoardTemperatureWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 4, 3, 2, 0, 120)
)
txExcBoardTemperatureWarning.setObjects(
      *(("RS-XX8000-COMMON-MIB", "eventAlarmPriority"),
        ("RS-XX8000-COMMON-MIB", "eventAlarmClass"),
        ("RS-XX8000-COMMON-MIB", "eventEvent"),
        ("RS-XX8000-COMMON-MIB", "indexAB"))
)
if mibBuilder.loadTexts:
    txExcBoardTemperatureWarning.setStatus(
        "current"
    )

txExcFanWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 4, 3, 2, 0, 121)
)
txExcFanWarning.setObjects(
      *(("RS-XX8000-COMMON-MIB", "eventAlarmPriority"),
        ("RS-XX8000-COMMON-MIB", "eventAlarmClass"),
        ("RS-XX8000-COMMON-MIB", "eventEvent"),
        ("RS-XX8000-COMMON-MIB", "indexAB"))
)
if mibBuilder.loadTexts:
    txExcFanWarning.setStatus(
        "current"
    )

txExcFanFault = NotificationType(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 4, 3, 2, 0, 122)
)
txExcFanFault.setObjects(
      *(("RS-XX8000-COMMON-MIB", "eventAlarmPriority"),
        ("RS-XX8000-COMMON-MIB", "eventAlarmClass"),
        ("RS-XX8000-COMMON-MIB", "eventEvent"),
        ("RS-XX8000-COMMON-MIB", "indexAB"))
)
if mibBuilder.loadTexts:
    txExcFanFault.setStatus(
        "current"
    )

txExcFifoWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 4, 3, 2, 0, 123)
)
txExcFifoWarning.setObjects(
      *(("RS-XX8000-COMMON-MIB", "eventAlarmPriority"),
        ("RS-XX8000-COMMON-MIB", "eventAlarmClass"),
        ("RS-XX8000-COMMON-MIB", "eventEvent"),
        ("RS-XX8000-COMMON-MIB", "indexAB"))
)
if mibBuilder.loadTexts:
    txExcFifoWarning.setStatus(
        "current"
    )

txExcTestSignal = NotificationType(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 4, 3, 2, 0, 124)
)
txExcTestSignal.setObjects(
      *(("RS-XX8000-COMMON-MIB", "eventAlarmPriority"),
        ("RS-XX8000-COMMON-MIB", "eventAlarmClass"),
        ("RS-XX8000-COMMON-MIB", "eventEvent"),
        ("RS-XX8000-COMMON-MIB", "indexAB"))
)
if mibBuilder.loadTexts:
    txExcTestSignal.setStatus(
        "current"
    )

txExcSFNDelay = NotificationType(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 4, 3, 2, 0, 125)
)
txExcSFNDelay.setObjects(
      *(("RS-XX8000-COMMON-MIB", "eventAlarmPriority"),
        ("RS-XX8000-COMMON-MIB", "eventAlarmClass"),
        ("RS-XX8000-COMMON-MIB", "eventEvent"),
        ("RS-XX8000-COMMON-MIB", "indexAB"))
)
if mibBuilder.loadTexts:
    txExcSFNDelay.setStatus(
        "current"
    )

txExcWrongDatarate = NotificationType(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 4, 3, 2, 0, 126)
)
txExcWrongDatarate.setObjects(
      *(("RS-XX8000-COMMON-MIB", "eventAlarmPriority"),
        ("RS-XX8000-COMMON-MIB", "eventAlarmClass"),
        ("RS-XX8000-COMMON-MIB", "eventEvent"),
        ("RS-XX8000-COMMON-MIB", "indexAB"))
)
if mibBuilder.loadTexts:
    txExcWrongDatarate.setStatus(
        "current"
    )

txExcMute = NotificationType(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 4, 3, 2, 0, 127)
)
txExcMute.setObjects(
      *(("RS-XX8000-COMMON-MIB", "eventAlarmPriority"),
        ("RS-XX8000-COMMON-MIB", "eventAlarmClass"),
        ("RS-XX8000-COMMON-MIB", "eventEvent"),
        ("RS-XX8000-COMMON-MIB", "indexAB"))
)
if mibBuilder.loadTexts:
    txExcMute.setStatus(
        "current"
    )

txExcPPSFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 4, 3, 2, 0, 128)
)
txExcPPSFail.setObjects(
      *(("RS-XX8000-COMMON-MIB", "eventAlarmPriority"),
        ("RS-XX8000-COMMON-MIB", "eventAlarmClass"),
        ("RS-XX8000-COMMON-MIB", "eventEvent"),
        ("RS-XX8000-COMMON-MIB", "indexAB"))
)
if mibBuilder.loadTexts:
    txExcPPSFail.setStatus(
        "current"
    )

txExcReferenceFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 4, 3, 2, 0, 129)
)
txExcReferenceFail.setObjects(
      *(("RS-XX8000-COMMON-MIB", "eventAlarmPriority"),
        ("RS-XX8000-COMMON-MIB", "eventAlarmClass"),
        ("RS-XX8000-COMMON-MIB", "eventEvent"),
        ("RS-XX8000-COMMON-MIB", "indexAB"))
)
if mibBuilder.loadTexts:
    txExcReferenceFail.setStatus(
        "current"
    )

txExcMIPFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 4, 3, 2, 0, 130)
)
txExcMIPFail.setObjects(
      *(("RS-XX8000-COMMON-MIB", "eventAlarmPriority"),
        ("RS-XX8000-COMMON-MIB", "eventAlarmClass"),
        ("RS-XX8000-COMMON-MIB", "eventEvent"),
        ("RS-XX8000-COMMON-MIB", "indexAB"))
)
if mibBuilder.loadTexts:
    txExcMIPFail.setStatus(
        "current"
    )

txExcInputAutomaticSwitchReady = NotificationType(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 4, 3, 2, 0, 131)
)
txExcInputAutomaticSwitchReady.setObjects(
      *(("RS-XX8000-COMMON-MIB", "eventAlarmPriority"),
        ("RS-XX8000-COMMON-MIB", "eventAlarmClass"),
        ("RS-XX8000-COMMON-MIB", "eventEvent"),
        ("RS-XX8000-COMMON-MIB", "indexAB"))
)
if mibBuilder.loadTexts:
    txExcInputAutomaticSwitchReady.setStatus(
        "current"
    )

txExcInputAutomaticChangedOver = NotificationType(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 4, 3, 2, 0, 132)
)
txExcInputAutomaticChangedOver.setObjects(
      *(("RS-XX8000-COMMON-MIB", "eventAlarmPriority"),
        ("RS-XX8000-COMMON-MIB", "eventAlarmClass"),
        ("RS-XX8000-COMMON-MIB", "eventEvent"),
        ("RS-XX8000-COMMON-MIB", "indexAB"))
)
if mibBuilder.loadTexts:
    txExcInputAutomaticChangedOver.setStatus(
        "current"
    )

txExcInputReseveMissing = NotificationType(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 4, 3, 2, 0, 133)
)
if mibBuilder.loadTexts:
    txExcInputReseveMissing.setStatus(
        "current"
    )

txOstSummaryFault = NotificationType(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 4, 3, 2, 0, 200)
)
txOstSummaryFault.setObjects(
      *(("RS-XX8000-COMMON-MIB", "eventAlarmPriority"),
        ("RS-XX8000-COMMON-MIB", "eventAlarmClass"),
        ("RS-XX8000-COMMON-MIB", "eventEvent"),
        ("RS-XX8000-COMMON-MIB", "indexAB"))
)
if mibBuilder.loadTexts:
    txOstSummaryFault.setStatus(
        "current"
    )

txOstSummaryWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 4, 3, 2, 0, 201)
)
txOstSummaryWarning.setObjects(
      *(("RS-XX8000-COMMON-MIB", "eventAlarmPriority"),
        ("RS-XX8000-COMMON-MIB", "eventAlarmClass"),
        ("RS-XX8000-COMMON-MIB", "eventEvent"),
        ("RS-XX8000-COMMON-MIB", "indexAB"))
)
if mibBuilder.loadTexts:
    txOstSummaryWarning.setStatus(
        "current"
    )

txOstRfOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 4, 3, 2, 0, 202)
)
txOstRfOn.setObjects(
      *(("RS-XX8000-COMMON-MIB", "eventAlarmPriority"),
        ("RS-XX8000-COMMON-MIB", "eventAlarmClass"),
        ("RS-XX8000-COMMON-MIB", "eventEvent"),
        ("RS-XX8000-COMMON-MIB", "indexAB"))
)
if mibBuilder.loadTexts:
    txOstRfOn.setStatus(
        "current"
    )

txOstRfOk = NotificationType(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 4, 3, 2, 0, 203)
)
txOstRfOk.setObjects(
      *(("RS-XX8000-COMMON-MIB", "eventAlarmPriority"),
        ("RS-XX8000-COMMON-MIB", "eventAlarmClass"),
        ("RS-XX8000-COMMON-MIB", "eventEvent"),
        ("RS-XX8000-COMMON-MIB", "indexAB"))
)
if mibBuilder.loadTexts:
    txOstRfOk.setStatus(
        "current"
    )

txOstNoInput = NotificationType(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 4, 3, 2, 0, 204)
)
txOstNoInput.setObjects(
      *(("RS-XX8000-COMMON-MIB", "eventAlarmPriority"),
        ("RS-XX8000-COMMON-MIB", "eventAlarmClass"),
        ("RS-XX8000-COMMON-MIB", "eventEvent"),
        ("RS-XX8000-COMMON-MIB", "indexAB"))
)
if mibBuilder.loadTexts:
    txOstNoInput.setStatus(
        "current"
    )

txOstRfWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 4, 3, 2, 0, 205)
)
txOstRfWarning.setObjects(
      *(("RS-XX8000-COMMON-MIB", "eventAlarmPriority"),
        ("RS-XX8000-COMMON-MIB", "eventAlarmClass"),
        ("RS-XX8000-COMMON-MIB", "eventEvent"),
        ("RS-XX8000-COMMON-MIB", "indexAB"))
)
if mibBuilder.loadTexts:
    txOstRfWarning.setStatus(
        "current"
    )

txOstReflectionWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 4, 3, 2, 0, 206)
)
txOstReflectionWarning.setObjects(
      *(("RS-XX8000-COMMON-MIB", "eventAlarmPriority"),
        ("RS-XX8000-COMMON-MIB", "eventAlarmClass"),
        ("RS-XX8000-COMMON-MIB", "eventEvent"),
        ("RS-XX8000-COMMON-MIB", "indexAB"))
)
if mibBuilder.loadTexts:
    txOstReflectionWarning.setStatus(
        "current"
    )

txOstRackWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 4, 3, 2, 0, 207)
)
txOstRackWarning.setObjects(
      *(("RS-XX8000-COMMON-MIB", "eventAlarmPriority"),
        ("RS-XX8000-COMMON-MIB", "eventAlarmClass"),
        ("RS-XX8000-COMMON-MIB", "eventEvent"),
        ("RS-XX8000-COMMON-MIB", "indexAB"))
)
if mibBuilder.loadTexts:
    txOstRackWarning.setStatus(
        "current"
    )

txOstCoolingWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 4, 3, 2, 0, 208)
)
txOstCoolingWarning.setObjects(
      *(("RS-XX8000-COMMON-MIB", "eventAlarmPriority"),
        ("RS-XX8000-COMMON-MIB", "eventAlarmClass"),
        ("RS-XX8000-COMMON-MIB", "eventEvent"),
        ("RS-XX8000-COMMON-MIB", "indexAB"))
)
if mibBuilder.loadTexts:
    txOstCoolingWarning.setStatus(
        "current"
    )

txOstRfFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 4, 3, 2, 0, 209)
)
txOstRfFail.setObjects(
      *(("RS-XX8000-COMMON-MIB", "eventAlarmPriority"),
        ("RS-XX8000-COMMON-MIB", "eventAlarmClass"),
        ("RS-XX8000-COMMON-MIB", "eventEvent"),
        ("RS-XX8000-COMMON-MIB", "indexAB"))
)
if mibBuilder.loadTexts:
    txOstRfFail.setStatus(
        "current"
    )

txOstReflectionFault = NotificationType(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 4, 3, 2, 0, 210)
)
txOstReflectionFault.setObjects(
      *(("RS-XX8000-COMMON-MIB", "eventAlarmPriority"),
        ("RS-XX8000-COMMON-MIB", "eventAlarmClass"),
        ("RS-XX8000-COMMON-MIB", "eventEvent"),
        ("RS-XX8000-COMMON-MIB", "indexAB"))
)
if mibBuilder.loadTexts:
    txOstReflectionFault.setStatus(
        "current"
    )

txOstACFault = NotificationType(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 4, 3, 2, 0, 211)
)
txOstACFault.setObjects(
      *(("RS-XX8000-COMMON-MIB", "eventAlarmPriority"),
        ("RS-XX8000-COMMON-MIB", "eventAlarmClass"),
        ("RS-XX8000-COMMON-MIB", "eventEvent"),
        ("RS-XX8000-COMMON-MIB", "indexAB"))
)
if mibBuilder.loadTexts:
    txOstACFault.setStatus(
        "current"
    )

txOstCoolingFault = NotificationType(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 4, 3, 2, 0, 212)
)
txOstCoolingFault.setObjects(
      *(("RS-XX8000-COMMON-MIB", "eventAlarmPriority"),
        ("RS-XX8000-COMMON-MIB", "eventAlarmClass"),
        ("RS-XX8000-COMMON-MIB", "eventEvent"),
        ("RS-XX8000-COMMON-MIB", "indexAB"))
)
if mibBuilder.loadTexts:
    txOstCoolingFault.setStatus(
        "current"
    )

txOstCommFault = NotificationType(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 4, 3, 2, 0, 213)
)
txOstCommFault.setObjects(
      *(("RS-XX8000-COMMON-MIB", "eventAlarmPriority"),
        ("RS-XX8000-COMMON-MIB", "eventAlarmClass"),
        ("RS-XX8000-COMMON-MIB", "eventEvent"),
        ("RS-XX8000-COMMON-MIB", "indexAB"))
)
if mibBuilder.loadTexts:
    txOstCommFault.setStatus(
        "current"
    )

txRackSumFault = NotificationType(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 4, 3, 2, 0, 300)
)
txRackSumFault.setObjects(
      *(("RS-XX8000-COMMON-MIB", "eventAlarmPriority"),
        ("RS-XX8000-COMMON-MIB", "eventAlarmClass"),
        ("RS-XX8000-COMMON-MIB", "eventEvent"),
        ("RS-XX8000-COMMON-MIB", "indexAB"),
        ("RS-XX8000-COMMON-MIB", "indexRack"))
)
if mibBuilder.loadTexts:
    txRackSumFault.setStatus(
        "current"
    )

txRackSumWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 4, 3, 2, 0, 301)
)
txRackSumWarning.setObjects(
      *(("RS-XX8000-COMMON-MIB", "eventAlarmPriority"),
        ("RS-XX8000-COMMON-MIB", "eventAlarmClass"),
        ("RS-XX8000-COMMON-MIB", "eventEvent"),
        ("RS-XX8000-COMMON-MIB", "indexAB"),
        ("RS-XX8000-COMMON-MIB", "indexRack"))
)
if mibBuilder.loadTexts:
    txRackSumWarning.setStatus(
        "current"
    )

txRackOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 4, 3, 2, 0, 302)
)
txRackOn.setObjects(
      *(("RS-XX8000-COMMON-MIB", "eventAlarmPriority"),
        ("RS-XX8000-COMMON-MIB", "eventAlarmClass"),
        ("RS-XX8000-COMMON-MIB", "eventEvent"),
        ("RS-XX8000-COMMON-MIB", "indexAB"),
        ("RS-XX8000-COMMON-MIB", "indexRack"))
)
if mibBuilder.loadTexts:
    txRackOn.setStatus(
        "current"
    )

txRackGpiWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 4, 3, 2, 0, 303)
)
txRackGpiWarning.setObjects(
      *(("RS-XX8000-COMMON-MIB", "eventAlarmPriority"),
        ("RS-XX8000-COMMON-MIB", "eventAlarmClass"),
        ("RS-XX8000-COMMON-MIB", "eventEvent"),
        ("RS-XX8000-COMMON-MIB", "indexAB"),
        ("RS-XX8000-COMMON-MIB", "indexRack"))
)
if mibBuilder.loadTexts:
    txRackGpiWarning.setStatus(
        "current"
    )

txRackFan1Fault = NotificationType(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 4, 3, 2, 0, 304)
)
txRackFan1Fault.setObjects(
      *(("RS-XX8000-COMMON-MIB", "eventAlarmPriority"),
        ("RS-XX8000-COMMON-MIB", "eventAlarmClass"),
        ("RS-XX8000-COMMON-MIB", "eventEvent"),
        ("RS-XX8000-COMMON-MIB", "indexAB"),
        ("RS-XX8000-COMMON-MIB", "indexRack"))
)
if mibBuilder.loadTexts:
    txRackFan1Fault.setStatus(
        "current"
    )

txRackFan2Fault = NotificationType(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 4, 3, 2, 0, 305)
)
txRackFan2Fault.setObjects(
      *(("RS-XX8000-COMMON-MIB", "eventAlarmPriority"),
        ("RS-XX8000-COMMON-MIB", "eventAlarmClass"),
        ("RS-XX8000-COMMON-MIB", "eventEvent"),
        ("RS-XX8000-COMMON-MIB", "indexAB"),
        ("RS-XX8000-COMMON-MIB", "indexRack"))
)
if mibBuilder.loadTexts:
    txRackFan2Fault.setStatus(
        "current"
    )

txRackCoolingSumWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 4, 3, 2, 0, 306)
)
txRackCoolingSumWarning.setObjects(
      *(("RS-XX8000-COMMON-MIB", "eventAlarmPriority"),
        ("RS-XX8000-COMMON-MIB", "eventAlarmClass"),
        ("RS-XX8000-COMMON-MIB", "eventEvent"),
        ("RS-XX8000-COMMON-MIB", "indexAB"),
        ("RS-XX8000-COMMON-MIB", "indexRack"))
)
if mibBuilder.loadTexts:
    txRackCoolingSumWarning.setStatus(
        "current"
    )

txRackAmplifierSumFault = NotificationType(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 4, 3, 2, 0, 307)
)
txRackAmplifierSumFault.setObjects(
      *(("RS-XX8000-COMMON-MIB", "eventAlarmPriority"),
        ("RS-XX8000-COMMON-MIB", "eventAlarmClass"),
        ("RS-XX8000-COMMON-MIB", "eventEvent"),
        ("RS-XX8000-COMMON-MIB", "indexAB"),
        ("RS-XX8000-COMMON-MIB", "indexRack"))
)
if mibBuilder.loadTexts:
    txRackAmplifierSumFault.setStatus(
        "current"
    )

txRackNoLink = NotificationType(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 4, 3, 2, 0, 308)
)
txRackNoLink.setObjects(
      *(("RS-XX8000-COMMON-MIB", "eventAlarmPriority"),
        ("RS-XX8000-COMMON-MIB", "eventAlarmClass"),
        ("RS-XX8000-COMMON-MIB", "eventEvent"),
        ("RS-XX8000-COMMON-MIB", "indexAB"),
        ("RS-XX8000-COMMON-MIB", "indexRack"))
)
if mibBuilder.loadTexts:
    txRackNoLink.setStatus(
        "current"
    )

txRackGpiFault = NotificationType(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 4, 3, 2, 0, 309)
)
txRackGpiFault.setObjects(
      *(("RS-XX8000-COMMON-MIB", "eventAlarmPriority"),
        ("RS-XX8000-COMMON-MIB", "eventAlarmClass"),
        ("RS-XX8000-COMMON-MIB", "eventEvent"),
        ("RS-XX8000-COMMON-MIB", "indexAB"),
        ("RS-XX8000-COMMON-MIB", "indexRack"))
)
if mibBuilder.loadTexts:
    txRackGpiFault.setStatus(
        "current"
    )

txRackTemperatureFault = NotificationType(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 4, 3, 2, 0, 310)
)
txRackTemperatureFault.setObjects(
      *(("RS-XX8000-COMMON-MIB", "eventAlarmPriority"),
        ("RS-XX8000-COMMON-MIB", "eventAlarmClass"),
        ("RS-XX8000-COMMON-MIB", "eventEvent"),
        ("RS-XX8000-COMMON-MIB", "indexAB"),
        ("RS-XX8000-COMMON-MIB", "indexRack"))
)
if mibBuilder.loadTexts:
    txRackTemperatureFault.setStatus(
        "current"
    )

txRackACFault = NotificationType(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 4, 3, 2, 0, 311)
)
txRackACFault.setObjects(
      *(("RS-XX8000-COMMON-MIB", "eventAlarmPriority"),
        ("RS-XX8000-COMMON-MIB", "eventAlarmClass"),
        ("RS-XX8000-COMMON-MIB", "eventEvent"),
        ("RS-XX8000-COMMON-MIB", "indexAB"),
        ("RS-XX8000-COMMON-MIB", "indexRack"))
)
if mibBuilder.loadTexts:
    txRackACFault.setStatus(
        "current"
    )

txRackCoolingSumFault = NotificationType(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 4, 3, 2, 0, 312)
)
txRackCoolingSumFault.setObjects(
      *(("RS-XX8000-COMMON-MIB", "eventAlarmPriority"),
        ("RS-XX8000-COMMON-MIB", "eventAlarmClass"),
        ("RS-XX8000-COMMON-MIB", "eventEvent"),
        ("RS-XX8000-COMMON-MIB", "indexAB"),
        ("RS-XX8000-COMMON-MIB", "indexRack"))
)
if mibBuilder.loadTexts:
    txRackCoolingSumFault.setStatus(
        "current"
    )

txRackTempFaultAbs1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 4, 3, 2, 0, 313)
)
txRackTempFaultAbs1.setObjects(
      *(("RS-XX8000-COMMON-MIB", "eventAlarmPriority"),
        ("RS-XX8000-COMMON-MIB", "eventAlarmClass"),
        ("RS-XX8000-COMMON-MIB", "eventEvent"),
        ("RS-XX8000-COMMON-MIB", "indexAB"),
        ("RS-XX8000-COMMON-MIB", "indexRack"))
)
if mibBuilder.loadTexts:
    txRackTempFaultAbs1.setStatus(
        "current"
    )

txRackTempFaultAbs2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 4, 3, 2, 0, 314)
)
txRackTempFaultAbs2.setObjects(
      *(("RS-XX8000-COMMON-MIB", "eventAlarmPriority"),
        ("RS-XX8000-COMMON-MIB", "eventAlarmClass"),
        ("RS-XX8000-COMMON-MIB", "eventEvent"),
        ("RS-XX8000-COMMON-MIB", "indexAB"),
        ("RS-XX8000-COMMON-MIB", "indexRack"))
)
if mibBuilder.loadTexts:
    txRackTempFaultAbs2.setStatus(
        "current"
    )

txRackDCFault = NotificationType(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 4, 3, 2, 0, 315)
)
txRackDCFault.setObjects(
      *(("RS-XX8000-COMMON-MIB", "eventAlarmPriority"),
        ("RS-XX8000-COMMON-MIB", "eventAlarmClass"),
        ("RS-XX8000-COMMON-MIB", "eventEvent"),
        ("RS-XX8000-COMMON-MIB", "indexAB"),
        ("RS-XX8000-COMMON-MIB", "indexRack"))
)
if mibBuilder.loadTexts:
    txRackDCFault.setStatus(
        "current"
    )

txRackRfOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 4, 3, 2, 0, 318)
)
txRackRfOn.setObjects(
      *(("RS-XX8000-COMMON-MIB", "eventAlarmPriority"),
        ("RS-XX8000-COMMON-MIB", "eventAlarmClass"),
        ("RS-XX8000-COMMON-MIB", "eventEvent"),
        ("RS-XX8000-COMMON-MIB", "indexAB"),
        ("RS-XX8000-COMMON-MIB", "indexRack"))
)
if mibBuilder.loadTexts:
    txRackRfOn.setStatus(
        "current"
    )

txRackRfOk = NotificationType(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 4, 3, 2, 0, 319)
)
txRackRfOk.setObjects(
      *(("RS-XX8000-COMMON-MIB", "eventAlarmPriority"),
        ("RS-XX8000-COMMON-MIB", "eventAlarmClass"),
        ("RS-XX8000-COMMON-MIB", "eventEvent"),
        ("RS-XX8000-COMMON-MIB", "indexAB"),
        ("RS-XX8000-COMMON-MIB", "indexRack"))
)
if mibBuilder.loadTexts:
    txRackRfOk.setStatus(
        "current"
    )

txRackRfWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 4, 3, 2, 0, 320)
)
txRackRfWarning.setObjects(
      *(("RS-XX8000-COMMON-MIB", "eventAlarmPriority"),
        ("RS-XX8000-COMMON-MIB", "eventAlarmClass"),
        ("RS-XX8000-COMMON-MIB", "eventEvent"),
        ("RS-XX8000-COMMON-MIB", "indexAB"),
        ("RS-XX8000-COMMON-MIB", "indexRack"))
)
if mibBuilder.loadTexts:
    txRackRfWarning.setStatus(
        "current"
    )

txRackRfFault = NotificationType(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 4, 3, 2, 0, 321)
)
txRackRfFault.setObjects(
      *(("RS-XX8000-COMMON-MIB", "eventAlarmPriority"),
        ("RS-XX8000-COMMON-MIB", "eventAlarmClass"),
        ("RS-XX8000-COMMON-MIB", "eventEvent"),
        ("RS-XX8000-COMMON-MIB", "indexAB"),
        ("RS-XX8000-COMMON-MIB", "indexRack"))
)
if mibBuilder.loadTexts:
    txRackRfFault.setStatus(
        "current"
    )

txRackReflectionWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 4, 3, 2, 0, 322)
)
txRackReflectionWarning.setObjects(
      *(("RS-XX8000-COMMON-MIB", "eventAlarmPriority"),
        ("RS-XX8000-COMMON-MIB", "eventAlarmClass"),
        ("RS-XX8000-COMMON-MIB", "eventEvent"),
        ("RS-XX8000-COMMON-MIB", "indexAB"),
        ("RS-XX8000-COMMON-MIB", "indexRack"))
)
if mibBuilder.loadTexts:
    txRackReflectionWarning.setStatus(
        "current"
    )

txRackReflectionFault = NotificationType(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 4, 3, 2, 0, 323)
)
txRackReflectionFault.setObjects(
      *(("RS-XX8000-COMMON-MIB", "eventAlarmPriority"),
        ("RS-XX8000-COMMON-MIB", "eventAlarmClass"),
        ("RS-XX8000-COMMON-MIB", "eventEvent"),
        ("RS-XX8000-COMMON-MIB", "indexAB"),
        ("RS-XX8000-COMMON-MIB", "indexRack"))
)
if mibBuilder.loadTexts:
    txRackReflectionFault.setStatus(
        "current"
    )

txRackProbeNotCalibrated = NotificationType(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 4, 3, 2, 0, 330)
)
txRackProbeNotCalibrated.setObjects(
      *(("RS-XX8000-COMMON-MIB", "eventAlarmPriority"),
        ("RS-XX8000-COMMON-MIB", "eventAlarmClass"),
        ("RS-XX8000-COMMON-MIB", "eventEvent"),
        ("RS-XX8000-COMMON-MIB", "indexAB"),
        ("RS-XX8000-COMMON-MIB", "indexRack"))
)
if mibBuilder.loadTexts:
    txRackProbeNotCalibrated.setStatus(
        "current"
    )

txRackTemperatureWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 4, 3, 2, 0, 331)
)
txRackTemperatureWarning.setObjects(
      *(("RS-XX8000-COMMON-MIB", "eventAlarmPriority"),
        ("RS-XX8000-COMMON-MIB", "eventAlarmClass"),
        ("RS-XX8000-COMMON-MIB", "eventEvent"),
        ("RS-XX8000-COMMON-MIB", "indexAB"),
        ("RS-XX8000-COMMON-MIB", "indexRack"))
)
if mibBuilder.loadTexts:
    txRackTemperatureWarning.setStatus(
        "current"
    )

txRackOvervoltProtectWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 4, 3, 2, 0, 335)
)
txRackOvervoltProtectWarning.setObjects(
      *(("RS-XX8000-COMMON-MIB", "eventAlarmPriority"),
        ("RS-XX8000-COMMON-MIB", "eventAlarmClass"),
        ("RS-XX8000-COMMON-MIB", "eventEvent"),
        ("RS-XX8000-COMMON-MIB", "indexAB"),
        ("RS-XX8000-COMMON-MIB", "indexRack"))
)
if mibBuilder.loadTexts:
    txRackOvervoltProtectWarning.setStatus(
        "current"
    )

txAmpSumFault = NotificationType(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 4, 3, 2, 0, 400)
)
txAmpSumFault.setObjects(
      *(("RS-XX8000-COMMON-MIB", "eventAlarmPriority"),
        ("RS-XX8000-COMMON-MIB", "eventAlarmClass"),
        ("RS-XX8000-COMMON-MIB", "eventEvent"),
        ("RS-XX8000-COMMON-MIB", "indexAB"),
        ("RS-XX8000-COMMON-MIB", "indexRack"),
        ("RS-XX8000-COMMON-MIB", "indexAmplifier"))
)
if mibBuilder.loadTexts:
    txAmpSumFault.setStatus(
        "current"
    )

txAmpSumWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 4, 3, 2, 0, 401)
)
txAmpSumWarning.setObjects(
      *(("RS-XX8000-COMMON-MIB", "eventAlarmPriority"),
        ("RS-XX8000-COMMON-MIB", "eventAlarmClass"),
        ("RS-XX8000-COMMON-MIB", "eventEvent"),
        ("RS-XX8000-COMMON-MIB", "indexAB"),
        ("RS-XX8000-COMMON-MIB", "indexRack"),
        ("RS-XX8000-COMMON-MIB", "indexAmplifier"))
)
if mibBuilder.loadTexts:
    txAmpSumWarning.setStatus(
        "current"
    )

txAmpPowerOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 4, 3, 2, 0, 402)
)
txAmpPowerOn.setObjects(
      *(("RS-XX8000-COMMON-MIB", "eventAlarmPriority"),
        ("RS-XX8000-COMMON-MIB", "eventAlarmClass"),
        ("RS-XX8000-COMMON-MIB", "eventEvent"),
        ("RS-XX8000-COMMON-MIB", "indexAB"),
        ("RS-XX8000-COMMON-MIB", "indexRack"),
        ("RS-XX8000-COMMON-MIB", "indexAmplifier"))
)
if mibBuilder.loadTexts:
    txAmpPowerOn.setStatus(
        "current"
    )

txAmpDCOk = NotificationType(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 4, 3, 2, 0, 403)
)
txAmpDCOk.setObjects(
      *(("RS-XX8000-COMMON-MIB", "eventAlarmPriority"),
        ("RS-XX8000-COMMON-MIB", "eventAlarmClass"),
        ("RS-XX8000-COMMON-MIB", "eventEvent"),
        ("RS-XX8000-COMMON-MIB", "indexAB"),
        ("RS-XX8000-COMMON-MIB", "indexRack"),
        ("RS-XX8000-COMMON-MIB", "indexAmplifier"))
)
if mibBuilder.loadTexts:
    txAmpDCOk.setStatus(
        "current"
    )

txAmpACOk = NotificationType(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 4, 3, 2, 0, 404)
)
txAmpACOk.setObjects(
      *(("RS-XX8000-COMMON-MIB", "eventAlarmPriority"),
        ("RS-XX8000-COMMON-MIB", "eventAlarmClass"),
        ("RS-XX8000-COMMON-MIB", "eventEvent"),
        ("RS-XX8000-COMMON-MIB", "indexAB"),
        ("RS-XX8000-COMMON-MIB", "indexRack"),
        ("RS-XX8000-COMMON-MIB", "indexAmplifier"))
)
if mibBuilder.loadTexts:
    txAmpACOk.setStatus(
        "current"
    )

txAmpRfInFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 4, 3, 2, 0, 405)
)
txAmpRfInFail.setObjects(
      *(("RS-XX8000-COMMON-MIB", "eventAlarmPriority"),
        ("RS-XX8000-COMMON-MIB", "eventAlarmClass"),
        ("RS-XX8000-COMMON-MIB", "eventEvent"),
        ("RS-XX8000-COMMON-MIB", "indexAB"),
        ("RS-XX8000-COMMON-MIB", "indexRack"),
        ("RS-XX8000-COMMON-MIB", "indexAmplifier"))
)
if mibBuilder.loadTexts:
    txAmpRfInFail.setStatus(
        "current"
    )

txAmpRfFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 4, 3, 2, 0, 406)
)
txAmpRfFail.setObjects(
      *(("RS-XX8000-COMMON-MIB", "eventAlarmPriority"),
        ("RS-XX8000-COMMON-MIB", "eventAlarmClass"),
        ("RS-XX8000-COMMON-MIB", "eventEvent"),
        ("RS-XX8000-COMMON-MIB", "indexAB"),
        ("RS-XX8000-COMMON-MIB", "indexRack"),
        ("RS-XX8000-COMMON-MIB", "indexAmplifier"))
)
if mibBuilder.loadTexts:
    txAmpRfFail.setStatus(
        "current"
    )

txAmpReflectionFault = NotificationType(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 4, 3, 2, 0, 407)
)
txAmpReflectionFault.setObjects(
      *(("RS-XX8000-COMMON-MIB", "eventAlarmPriority"),
        ("RS-XX8000-COMMON-MIB", "eventAlarmClass"),
        ("RS-XX8000-COMMON-MIB", "eventEvent"),
        ("RS-XX8000-COMMON-MIB", "indexAB"),
        ("RS-XX8000-COMMON-MIB", "indexRack"),
        ("RS-XX8000-COMMON-MIB", "indexAmplifier"))
)
if mibBuilder.loadTexts:
    txAmpReflectionFault.setStatus(
        "current"
    )

txAmpTemperatureFault = NotificationType(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 4, 3, 2, 0, 408)
)
txAmpTemperatureFault.setObjects(
      *(("RS-XX8000-COMMON-MIB", "eventAlarmPriority"),
        ("RS-XX8000-COMMON-MIB", "eventAlarmClass"),
        ("RS-XX8000-COMMON-MIB", "eventEvent"),
        ("RS-XX8000-COMMON-MIB", "indexAB"),
        ("RS-XX8000-COMMON-MIB", "indexRack"),
        ("RS-XX8000-COMMON-MIB", "indexAmplifier"))
)
if mibBuilder.loadTexts:
    txAmpTemperatureFault.setStatus(
        "current"
    )

txAmpTransistorFault = NotificationType(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 4, 3, 2, 0, 409)
)
txAmpTransistorFault.setObjects(
      *(("RS-XX8000-COMMON-MIB", "eventAlarmPriority"),
        ("RS-XX8000-COMMON-MIB", "eventAlarmClass"),
        ("RS-XX8000-COMMON-MIB", "eventEvent"),
        ("RS-XX8000-COMMON-MIB", "indexAB"),
        ("RS-XX8000-COMMON-MIB", "indexRack"),
        ("RS-XX8000-COMMON-MIB", "indexAmplifier"))
)
if mibBuilder.loadTexts:
    txAmpTransistorFault.setStatus(
        "current"
    )


# Notifications groups

groupEventsTxCommon = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 4, 5, 1, 3)
)
groupEventsTxCommon.setObjects(
      *(("RS-XX8000-DVB-TX-MIB", "txSummaryFault"),
        ("RS-XX8000-DVB-TX-MIB", "txSummaryWarning"),
        ("RS-XX8000-DVB-TX-MIB", "txLocal"),
        ("RS-XX8000-DVB-TX-MIB", "txRfOn"),
        ("RS-XX8000-DVB-TX-MIB", "txParamSetValuesChanged"),
        ("RS-XX8000-DVB-TX-MIB", "txRfLoopProgram"),
        ("RS-XX8000-DVB-TX-MIB", "txRfFail"),
        ("RS-XX8000-DVB-TX-MIB", "txOstSummaryFault"),
        ("RS-XX8000-DVB-TX-MIB", "txOstSummaryWarning"),
        ("RS-XX8000-DVB-TX-MIB", "txRfOk"),
        ("RS-XX8000-DVB-TX-MIB", "txOstRfOn"),
        ("RS-XX8000-DVB-TX-MIB", "txRfWarning"))
)
if mibBuilder.loadTexts:
    groupEventsTxCommon.setStatus(
        "current"
    )

groupEventsDualDrive = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 4, 5, 1, 5)
)
groupEventsDualDrive.setObjects(
      *(("RS-XX8000-DVB-TX-MIB", "txRfLoopReserve"),
        ("RS-XX8000-DVB-TX-MIB", "txNetCCUNoConnectionToExcB"),
        ("RS-XX8000-DVB-TX-MIB", "txAutomaticExcReady"),
        ("RS-XX8000-DVB-TX-MIB", "txAutomaticExcChanged"),
        ("RS-XX8000-DVB-TX-MIB", "txAutomaticExcFault"))
)
if mibBuilder.loadTexts:
    groupEventsDualDrive.setStatus(
        "current"
    )

groupEventsPowerReserve = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 4, 5, 1, 7)
)
groupEventsPowerReserve.setObjects(
      *(("RS-XX8000-DVB-TX-MIB", "txNetCCUNoConnectionToOstB"),
        ("RS-XX8000-DVB-TX-MIB", "txAutomaticOstReady"),
        ("RS-XX8000-DVB-TX-MIB", "txAutomaticOstChanged"),
        ("RS-XX8000-DVB-TX-MIB", "txAutomaticOstFault"))
)
if mibBuilder.loadTexts:
    groupEventsPowerReserve.setStatus(
        "current"
    )

groupEventsCommonMP = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 4, 5, 1, 9)
)
groupEventsCommonMP.setObjects(
      *(("RS-XX8000-DVB-TX-MIB", "txReflectionWarning"),
        ("RS-XX8000-DVB-TX-MIB", "txReflectionFault"),
        ("RS-XX8000-DVB-TX-MIB", "txOstRfOk"),
        ("RS-XX8000-DVB-TX-MIB", "txOstNoInput"),
        ("RS-XX8000-DVB-TX-MIB", "txOstRfWarning"),
        ("RS-XX8000-DVB-TX-MIB", "txOstReflectionWarning"),
        ("RS-XX8000-DVB-TX-MIB", "txOstRackWarning"),
        ("RS-XX8000-DVB-TX-MIB", "txOstCoolingWarning"),
        ("RS-XX8000-DVB-TX-MIB", "txOstRfFail"),
        ("RS-XX8000-DVB-TX-MIB", "txOstReflectionFault"),
        ("RS-XX8000-DVB-TX-MIB", "txOstACFault"),
        ("RS-XX8000-DVB-TX-MIB", "txOstCoolingFault"),
        ("RS-XX8000-DVB-TX-MIB", "txOstCommFault"),
        ("RS-XX8000-DVB-TX-MIB", "txRackSumFault"),
        ("RS-XX8000-DVB-TX-MIB", "txRackSumWarning"),
        ("RS-XX8000-DVB-TX-MIB", "txRackOn"),
        ("RS-XX8000-DVB-TX-MIB", "txRackGpiWarning"),
        ("RS-XX8000-DVB-TX-MIB", "txRackFan1Fault"),
        ("RS-XX8000-DVB-TX-MIB", "txRackFan2Fault"),
        ("RS-XX8000-DVB-TX-MIB", "txRackCoolingSumWarning"),
        ("RS-XX8000-DVB-TX-MIB", "txRackAmplifierSumFault"),
        ("RS-XX8000-DVB-TX-MIB", "txRackNoLink"),
        ("RS-XX8000-DVB-TX-MIB", "txRackGpiFault"),
        ("RS-XX8000-DVB-TX-MIB", "txRackTemperatureFault"),
        ("RS-XX8000-DVB-TX-MIB", "txRackACFault"),
        ("RS-XX8000-DVB-TX-MIB", "txRackCoolingSumFault"),
        ("RS-XX8000-DVB-TX-MIB", "txRackTempFaultAbs1"),
        ("RS-XX8000-DVB-TX-MIB", "txRackTempFaultAbs2"),
        ("RS-XX8000-DVB-TX-MIB", "txRackDCFault"),
        ("RS-XX8000-DVB-TX-MIB", "txRackRfWarning"),
        ("RS-XX8000-DVB-TX-MIB", "txRackRfFault"),
        ("RS-XX8000-DVB-TX-MIB", "txRackReflectionWarning"),
        ("RS-XX8000-DVB-TX-MIB", "txRackReflectionFault"),
        ("RS-XX8000-DVB-TX-MIB", "txRackRfOk"),
        ("RS-XX8000-DVB-TX-MIB", "txRackRfOn"),
        ("RS-XX8000-DVB-TX-MIB", "txRackOvervoltProtectWarning"),
        ("RS-XX8000-DVB-TX-MIB", "txRackTemperatureWarning"),
        ("RS-XX8000-DVB-TX-MIB", "txRackProbeNotCalibrated"))
)
if mibBuilder.loadTexts:
    groupEventsCommonMP.setStatus(
        "current"
    )

groupEventsCommonNetCCU = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 4, 5, 1, 11)
)
groupEventsCommonNetCCU.setObjects(
      *(("RS-XX8000-DVB-TX-MIB", "txNetCCUFanFault"),
        ("RS-XX8000-DVB-TX-MIB", "txNetCCUPowerSupply"),
        ("RS-XX8000-DVB-TX-MIB", "txNetCCUNoConnectionToExcA"),
        ("RS-XX8000-DVB-TX-MIB", "txNetCCUNoConnectionToOstA"),
        ("RS-XX8000-DVB-TX-MIB", "txModeSwitchOverStarted"),
        ("RS-XX8000-DVB-TX-MIB", "txModeSwitchOverEnded"),
        ("RS-XX8000-DVB-TX-MIB", "txModeInconsistent"),
        ("RS-XX8000-DVB-TX-MIB", "txModeSwitchOverFailed"),
        ("RS-XX8000-DVB-TX-MIB", "txNetCCUBoardTemperatureWarning"))
)
if mibBuilder.loadTexts:
    groupEventsCommonNetCCU.setStatus(
        "current"
    )

groupEventsAmplifier = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 4, 5, 1, 20)
)
groupEventsAmplifier.setObjects(
      *(("RS-XX8000-DVB-TX-MIB", "txAmpSumFault"),
        ("RS-XX8000-DVB-TX-MIB", "txAmpSumWarning"),
        ("RS-XX8000-DVB-TX-MIB", "txAmpPowerOn"),
        ("RS-XX8000-DVB-TX-MIB", "txAmpDCOk"),
        ("RS-XX8000-DVB-TX-MIB", "txAmpACOk"),
        ("RS-XX8000-DVB-TX-MIB", "txAmpRfInFail"),
        ("RS-XX8000-DVB-TX-MIB", "txAmpRfFail"),
        ("RS-XX8000-DVB-TX-MIB", "txAmpReflectionFault"),
        ("RS-XX8000-DVB-TX-MIB", "txAmpTemperatureFault"),
        ("RS-XX8000-DVB-TX-MIB", "txAmpTransistorFault"))
)
if mibBuilder.loadTexts:
    groupEventsAmplifier.setStatus(
        "current"
    )

groupEventsExciter = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 4, 5, 1, 26)
)
groupEventsExciter.setObjects(
      *(("RS-XX8000-DVB-TX-MIB", "txExcSummaryFault"),
        ("RS-XX8000-DVB-TX-MIB", "txExcSummaryWarning"),
        ("RS-XX8000-DVB-TX-MIB", "txExcInputNoConnectHP1"),
        ("RS-XX8000-DVB-TX-MIB", "txExcInputNoConnectLP1"),
        ("RS-XX8000-DVB-TX-MIB", "txExcInputNoConnectHP2"),
        ("RS-XX8000-DVB-TX-MIB", "txExcInputNoConnectLP2"),
        ("RS-XX8000-DVB-TX-MIB", "txExcInputActiveHP1"),
        ("RS-XX8000-DVB-TX-MIB", "txExcInputActiveLP1"),
        ("RS-XX8000-DVB-TX-MIB", "txExcInputActiveHP2"),
        ("RS-XX8000-DVB-TX-MIB", "txExcInputActiveLP2"),
        ("RS-XX8000-DVB-TX-MIB", "txExcOn"),
        ("RS-XX8000-DVB-TX-MIB", "txExcRfOn"),
        ("RS-XX8000-DVB-TX-MIB", "txExcNoInput"),
        ("RS-XX8000-DVB-TX-MIB", "txExcRfLoop"),
        ("RS-XX8000-DVB-TX-MIB", "txExcRfFail"),
        ("RS-XX8000-DVB-TX-MIB", "txExcSelfTest"),
        ("RS-XX8000-DVB-TX-MIB", "txExcOutputOpen"),
        ("RS-XX8000-DVB-TX-MIB", "txExcBoardTemperatureWarning"),
        ("RS-XX8000-DVB-TX-MIB", "txExcFanWarning"),
        ("RS-XX8000-DVB-TX-MIB", "txExcFanFault"),
        ("RS-XX8000-DVB-TX-MIB", "txExcFifoWarning"),
        ("RS-XX8000-DVB-TX-MIB", "txExcTestSignal"),
        ("RS-XX8000-DVB-TX-MIB", "txExcSFNDelay"),
        ("RS-XX8000-DVB-TX-MIB", "txExcWrongDatarate"),
        ("RS-XX8000-DVB-TX-MIB", "txExcMute"),
        ("RS-XX8000-DVB-TX-MIB", "txExcPPSFail"),
        ("RS-XX8000-DVB-TX-MIB", "txExcReferenceFail"),
        ("RS-XX8000-DVB-TX-MIB", "txExcMIPFail"),
        ("RS-XX8000-DVB-TX-MIB", "txExcInputAutomaticSwitchReady"),
        ("RS-XX8000-DVB-TX-MIB", "txExcRfOk"),
        ("RS-XX8000-DVB-TX-MIB", "txExcInputReseveMissing"),
        ("RS-XX8000-DVB-TX-MIB", "txExcInputAutomaticChangedOver"),
        ("RS-XX8000-DVB-TX-MIB", "txExcLocal"))
)
if mibBuilder.loadTexts:
    groupEventsExciter.setStatus(
        "current"
    )

groupEventsControlExciter = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 4, 5, 1, 34)
)
groupEventsControlExciter.setObjects(
      *(("RS-XX8000-DVB-TX-MIB", "txNetCCUNoConnectionToExcB"),
        ("RS-XX8000-DVB-TX-MIB", "txAutomaticExcReady"),
        ("RS-XX8000-DVB-TX-MIB", "txAutomaticExcChanged"),
        ("RS-XX8000-DVB-TX-MIB", "txAutomaticExcFault"))
)
if mibBuilder.loadTexts:
    groupEventsControlExciter.setStatus(
        "current"
    )

groupEventsAdditionalPowerSupply = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 4, 5, 1, 35)
)
groupEventsAdditionalPowerSupply.setObjects(
      *(("RS-XX8000-DVB-TX-MIB", "txInternalPowerSupplyWarning"),
        ("RS-XX8000-DVB-TX-MIB", "txExternalPowerSupplyWarning"))
)
if mibBuilder.loadTexts:
    groupEventsAdditionalPowerSupply.setStatus(
        "current"
    )

groupEventsObsoleted = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 4, 5, 1, 100)
)
groupEventsObsoleted.setObjects(
      *(("RS-XX8000-DVB-TX-MIB", "txParamSetSubDeviceDiffers"),
        ("RS-XX8000-DVB-TX-MIB", "txNetCCUBoardTemperatureFault"))
)
if mibBuilder.loadTexts:
    groupEventsObsoleted.setStatus(
        "obsolete"
    )


# Agent capabilities


# Module compliance

rsXx8000DVBSingleTxMP = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 4, 5, 3, 1)
)
rsXx8000DVBSingleTxMP.setObjects(
      *(("RS-XX8000-DVB-TX-MIB", "groupTxCommon"),
        ("RS-XX8000-DVB-TX-MIB", "groupCommonMP"),
        ("RS-XX8000-DVB-TX-MIB", "groupCommonNetCCU"),
        ("RS-XX8000-DVB-TX-MIB", "groupExcCommon"),
        ("RS-XX8000-DVB-TX-MIB", "groupEvents"),
        ("RS-XX8000-DVB-TX-MIB", "groupProductInfo"),
        ("RS-XX8000-DVB-TX-MIB", "groupRfProbes"),
        ("RS-XX8000-DVB-TX-MIB", "groupExciterStatus"),
        ("RS-XX8000-DVB-TX-MIB", "groupExciterPrecorrection"),
        ("RS-XX8000-DVB-TX-MIB", "groupEventsExciter"),
        ("RS-XX8000-DVB-TX-MIB", "groupEventsCommonNetCCU"),
        ("RS-XX8000-DVB-TX-MIB", "groupObjectsSingleEnded"),
        ("RS-XX8000-DVB-TX-MIB", "groupEventsCommonMP"),
        ("RS-XX8000-DVB-TX-MIB", "groupEventsTxCommon"),
        ("RS-XX8000-DVB-TX-MIB", "groupIndependentRacks"),
        ("RS-XX8000-DVB-TX-MIB", "groupExcAdditionalSx800"),
        ("RS-XX8000-DVB-TX-MIB", "groupEventsAdditionalPowerSupply"),
        ("RS-XX8000-DVB-TX-MIB", "groupAmpMeasureValues"),
        ("RS-XX8000-DVB-TX-MIB", "groupEventsAmplifier"),
        ("RS-XX8000-DVB-TX-MIB", "groupObjsAdditionalPowerSupply"))
)
if mibBuilder.loadTexts:
    rsXx8000DVBSingleTxMP.setStatus(
        "current"
    )

rsXx8000DVBDualDriveMP = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 4, 5, 3, 2)
)
rsXx8000DVBDualDriveMP.setObjects(
      *(("RS-XX8000-DVB-TX-MIB", "groupTxCommon"),
        ("RS-XX8000-DVB-TX-MIB", "groupCommonMP"),
        ("RS-XX8000-DVB-TX-MIB", "groupCommonNetCCU"),
        ("RS-XX8000-DVB-TX-MIB", "groupExcCommon"),
        ("RS-XX8000-DVB-TX-MIB", "groupDualDrive"),
        ("RS-XX8000-DVB-TX-MIB", "groupEvents"),
        ("RS-XX8000-DVB-TX-MIB", "groupProductInfo"),
        ("RS-XX8000-DVB-TX-MIB", "groupRfProbes"),
        ("RS-XX8000-DVB-TX-MIB", "groupExciterStatus"),
        ("RS-XX8000-DVB-TX-MIB", "groupExciterPrecorrection"),
        ("RS-XX8000-DVB-TX-MIB", "groupEventsExciter"),
        ("RS-XX8000-DVB-TX-MIB", "groupEventsCommonNetCCU"),
        ("RS-XX8000-DVB-TX-MIB", "groupEventsCommonMP"),
        ("RS-XX8000-DVB-TX-MIB", "groupObjectsSingleEnded"),
        ("RS-XX8000-DVB-TX-MIB", "groupEventsDualDrive"),
        ("RS-XX8000-DVB-TX-MIB", "groupEventsTxCommon"),
        ("RS-XX8000-DVB-TX-MIB", "groupIndependentRacks"),
        ("RS-XX8000-DVB-TX-MIB", "groupExcAdditionalSx800"),
        ("RS-XX8000-DVB-TX-MIB", "groupEventsAdditionalPowerSupply"),
        ("RS-XX8000-DVB-TX-MIB", "groupAmpMeasureValues"),
        ("RS-XX8000-DVB-TX-MIB", "groupEventsAmplifier"),
        ("RS-XX8000-DVB-TX-MIB", "groupObjsAdditionalPowerSupply"))
)
if mibBuilder.loadTexts:
    rsXx8000DVBDualDriveMP.setStatus(
        "current"
    )

rsXx8000DVBPowerReserveMP = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 4, 5, 3, 3)
)
rsXx8000DVBPowerReserveMP.setObjects(
      *(("RS-XX8000-DVB-TX-MIB", "groupTxCommon"),
        ("RS-XX8000-DVB-TX-MIB", "groupEvents"),
        ("RS-XX8000-DVB-TX-MIB", "groupProductInfo"),
        ("RS-XX8000-DVB-TX-MIB", "groupRfProbes"),
        ("RS-XX8000-DVB-TX-MIB", "groupExciterStatus"),
        ("RS-XX8000-DVB-TX-MIB", "groupExcCommon"),
        ("RS-XX8000-DVB-TX-MIB", "groupExciterPrecorrection"),
        ("RS-XX8000-DVB-TX-MIB", "groupDualDrive"),
        ("RS-XX8000-DVB-TX-MIB", "groupPowerReserve"),
        ("RS-XX8000-DVB-TX-MIB", "groupCommonMP"),
        ("RS-XX8000-DVB-TX-MIB", "groupCommonNetCCU"),
        ("RS-XX8000-DVB-TX-MIB", "groupOstBLogbook"),
        ("RS-XX8000-DVB-TX-MIB", "groupEventsExciter"),
        ("RS-XX8000-DVB-TX-MIB", "groupEventsCommonNetCCU"),
        ("RS-XX8000-DVB-TX-MIB", "groupEventsCommonMP"),
        ("RS-XX8000-DVB-TX-MIB", "groupEventsPowerReserve"),
        ("RS-XX8000-DVB-TX-MIB", "groupEventsDualDrive"),
        ("RS-XX8000-DVB-TX-MIB", "groupEventsTxCommon"),
        ("RS-XX8000-DVB-TX-MIB", "groupIndependentRacks"),
        ("RS-XX8000-DVB-TX-MIB", "groupSumProbe"),
        ("RS-XX8000-DVB-TX-MIB", "groupExcAdditionalSx800"),
        ("RS-XX8000-DVB-TX-MIB", "groupEventsAdditionalPowerSupply"),
        ("RS-XX8000-DVB-TX-MIB", "groupAmpMeasureValues"),
        ("RS-XX8000-DVB-TX-MIB", "groupEventsAmplifier"),
        ("RS-XX8000-DVB-TX-MIB", "groupObjsAdditionalPowerSupply"),
        ("RS-XX8000-DVB-TX-MIB", "groupDummyLoadRF"))
)
if mibBuilder.loadTexts:
    rsXx8000DVBPowerReserveMP.setStatus(
        "current"
    )

rsXx8000DVBSingleTxLP = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 4, 5, 3, 5)
)
rsXx8000DVBSingleTxLP.setObjects(
      *(("RS-XX8000-DVB-TX-MIB", "groupEvents"),
        ("RS-XX8000-DVB-TX-MIB", "groupExciterStatus"),
        ("RS-XX8000-DVB-TX-MIB", "groupExciterPrecorrection"),
        ("RS-XX8000-DVB-TX-MIB", "groupExcAdditionalSLx"),
        ("RS-XX8000-DVB-TX-MIB", "groupExcCommon"),
        ("RS-XX8000-DVB-TX-MIB", "groupCommonNetCCU"),
        ("RS-XX8000-DVB-TX-MIB", "groupTxCommon"),
        ("RS-XX8000-DVB-TX-MIB", "groupEventsExciter"),
        ("RS-XX8000-DVB-TX-MIB", "groupEventsCommonNetCCU"),
        ("RS-XX8000-DVB-TX-MIB", "groupEventsTxCommon"),
        ("RS-XX8000-DVB-TX-MIB", "groupEventsAdditionalPowerSupply"),
        ("RS-XX8000-DVB-TX-MIB", "groupObjsAdditionalPowerSupply"))
)
if mibBuilder.loadTexts:
    rsXx8000DVBSingleTxLP.setStatus(
        "current"
    )

rsXx8000DVBDualDriveLP = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 4, 5, 3, 6)
)
rsXx8000DVBDualDriveLP.setObjects(
      *(("RS-XX8000-DVB-TX-MIB", "groupEvents"),
        ("RS-XX8000-DVB-TX-MIB", "groupExciterStatus"),
        ("RS-XX8000-DVB-TX-MIB", "groupExciterPrecorrection"),
        ("RS-XX8000-DVB-TX-MIB", "groupExcAdditionalSLx"),
        ("RS-XX8000-DVB-TX-MIB", "groupExcCommon"),
        ("RS-XX8000-DVB-TX-MIB", "groupCommonNetCCU"),
        ("RS-XX8000-DVB-TX-MIB", "groupDualDrive"),
        ("RS-XX8000-DVB-TX-MIB", "groupTxCommon"),
        ("RS-XX8000-DVB-TX-MIB", "groupEventsExciter"),
        ("RS-XX8000-DVB-TX-MIB", "groupEventsCommonNetCCU"),
        ("RS-XX8000-DVB-TX-MIB", "groupEventsDualDrive"),
        ("RS-XX8000-DVB-TX-MIB", "groupEventsTxCommon"),
        ("RS-XX8000-DVB-TX-MIB", "groupEventsAdditionalPowerSupply"),
        ("RS-XX8000-DVB-TX-MIB", "groupObjsAdditionalPowerSupply"))
)
if mibBuilder.loadTexts:
    rsXx8000DVBDualDriveLP.setStatus(
        "current"
    )

rsXx8000DVBPowerReserveLP = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 4, 5, 3, 7)
)
rsXx8000DVBPowerReserveLP.setObjects(
      *(("RS-XX8000-DVB-TX-MIB", "groupEvents"),
        ("RS-XX8000-DVB-TX-MIB", "groupExciterStatus"),
        ("RS-XX8000-DVB-TX-MIB", "groupExciterPrecorrection"),
        ("RS-XX8000-DVB-TX-MIB", "groupExcAdditionalSLx"),
        ("RS-XX8000-DVB-TX-MIB", "groupExcCommon"),
        ("RS-XX8000-DVB-TX-MIB", "groupCommonNetCCU"),
        ("RS-XX8000-DVB-TX-MIB", "groupPowerReserve"),
        ("RS-XX8000-DVB-TX-MIB", "groupDualDrive"),
        ("RS-XX8000-DVB-TX-MIB", "groupTxCommon"),
        ("RS-XX8000-DVB-TX-MIB", "groupEventsExciter"),
        ("RS-XX8000-DVB-TX-MIB", "groupEventsCommonNetCCU"),
        ("RS-XX8000-DVB-TX-MIB", "groupEventsPowerReserve"),
        ("RS-XX8000-DVB-TX-MIB", "groupEventsDualDrive"),
        ("RS-XX8000-DVB-TX-MIB", "groupEventsTxCommon"),
        ("RS-XX8000-DVB-TX-MIB", "groupEventsAdditionalPowerSupply"),
        ("RS-XX8000-DVB-TX-MIB", "groupObjsAdditionalPowerSupply"))
)
if mibBuilder.loadTexts:
    rsXx8000DVBPowerReserveLP.setStatus(
        "current"
    )

rsXx8000DVBSingleTxLPNoNetCCU = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 4, 5, 3, 9)
)
rsXx8000DVBSingleTxLPNoNetCCU.setObjects(
      *(("RS-XX8000-DVB-TX-MIB", "groupEvents"),
        ("RS-XX8000-DVB-TX-MIB", "groupExciterStatus"),
        ("RS-XX8000-DVB-TX-MIB", "groupExciterPrecorrection"),
        ("RS-XX8000-DVB-TX-MIB", "groupExcAdditionalSLx"),
        ("RS-XX8000-DVB-TX-MIB", "groupExcCommon"),
        ("RS-XX8000-DVB-TX-MIB", "groupTxCommon"),
        ("RS-XX8000-DVB-TX-MIB", "groupEventsExciter"),
        ("RS-XX8000-DVB-TX-MIB", "groupEventsTxCommon"))
)
if mibBuilder.loadTexts:
    rsXx8000DVBSingleTxLPNoNetCCU.setStatus(
        "current"
    )

rsXx8000DVBSLx = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 4, 5, 3, 10)
)
rsXx8000DVBSLx.setObjects(
      *(("RS-XX8000-DVB-TX-MIB", "groupEvents"),
        ("RS-XX8000-DVB-TX-MIB", "groupExciterStatus"),
        ("RS-XX8000-DVB-TX-MIB", "groupExciterPrecorrection"),
        ("RS-XX8000-DVB-TX-MIB", "groupSLx"),
        ("RS-XX8000-DVB-TX-MIB", "groupObjectsACU"),
        ("RS-XX8000-DVB-TX-MIB", "groupExcCommon"),
        ("RS-XX8000-DVB-TX-MIB", "groupTxCommon"),
        ("RS-XX8000-DVB-TX-MIB", "groupEventsExciter"),
        ("RS-XX8000-DVB-TX-MIB", "groupEventsTxCommon"))
)
if mibBuilder.loadTexts:
    rsXx8000DVBSLx.setStatus(
        "current"
    )

rsXx8000DVBExciterOnly = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 4, 5, 3, 11)
)
rsXx8000DVBExciterOnly.setObjects(
      *(("RS-XX8000-DVB-TX-MIB", "groupProductInfo"),
        ("RS-XX8000-DVB-TX-MIB", "groupExciterStatus"),
        ("RS-XX8000-DVB-TX-MIB", "groupEvents"),
        ("RS-XX8000-DVB-TX-MIB", "groupObjectsRE"),
        ("RS-XX8000-DVB-TX-MIB", "groupObjectsSx801Amplifier"),
        ("RS-XX8000-DVB-TX-MIB", "groupExciterPrecorrection"),
        ("RS-XX8000-DVB-TX-MIB", "groupExcCommon"),
        ("RS-XX8000-DVB-TX-MIB", "groupEventsExciter"),
        ("RS-XX8000-DVB-TX-MIB", "groupSLx"))
)
if mibBuilder.loadTexts:
    rsXx8000DVBExciterOnly.setStatus(
        "current"
    )

rsXx8000DVBSx801ControlExciter = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 4, 5, 3, 12)
)
rsXx8000DVBSx801ControlExciter.setObjects(
      *(("RS-XX8000-DVB-TX-MIB", "groupTxCommon"),
        ("RS-XX8000-DVB-TX-MIB", "groupExcCommon"),
        ("RS-XX8000-DVB-TX-MIB", "groupEvents"),
        ("RS-XX8000-DVB-TX-MIB", "groupExciterStatus"),
        ("RS-XX8000-DVB-TX-MIB", "groupExciterPrecorrection"),
        ("RS-XX8000-DVB-TX-MIB", "groupSLx"),
        ("RS-XX8000-DVB-TX-MIB", "groupObjectsACU"),
        ("RS-XX8000-DVB-TX-MIB", "groupObjectsSx801Amplifier"),
        ("RS-XX8000-DVB-TX-MIB", "groupEventsExciter"),
        ("RS-XX8000-DVB-TX-MIB", "groupEventsTxCommon"),
        ("RS-XX8000-DVB-TX-MIB", "groupEventsControlExciter"),
        ("RS-XX8000-DVB-TX-MIB", "groupObjectsControlExciter"))
)
if mibBuilder.loadTexts:
    rsXx8000DVBSx801ControlExciter.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RS-XX8000-DVB-TX-MIB",
    **{"rsXx8000DvbTx": rsXx8000DvbTx,
       "rsXx8000DvbTxObjs": rsXx8000DvbTxObjs,
       "commandsTxTable": commandsTxTable,
       "commandsTxEntry": commandsTxEntry,
       "cmdTxResetSumFault": cmdTxResetSumFault,
       "cmdTxParametersetLoad": cmdTxParametersetLoad,
       "cmdTxParametersetSave": cmdTxParametersetSave,
       "cmdTxParametersetReSave": cmdTxParametersetReSave,
       "cmdTxOperationModeProgram": cmdTxOperationModeProgram,
       "cmdTxOperationModeReserve": cmdTxOperationModeReserve,
       "cmdTxOpModeExcAutomatic": cmdTxOpModeExcAutomatic,
       "cmdTxOpModeOstAutomatic": cmdTxOpModeOstAutomatic,
       "cmdTxPreselectExciter": cmdTxPreselectExciter,
       "cmdTxPreselectOutputstage": cmdTxPreselectOutputstage,
       "cmdTxDelayTimeExcAutomatic": cmdTxDelayTimeExcAutomatic,
       "cmdTxDelayTimeOstAutomatic": cmdTxDelayTimeOstAutomatic,
       "cmdTxRfSwitch": cmdTxRfSwitch,
       "cmdTxSystemMode": cmdTxSystemMode,
       "cmdTxProgramExciterPrio": cmdTxProgramExciterPrio,
       "cmdTxChangeOver": cmdTxChangeOver,
       "cmdTxSwitchPosition": cmdTxSwitchPosition,
       "cmdDeviceIdx": cmdDeviceIdx,
       "cmdExcOpModeInputAutomatic": cmdExcOpModeInputAutomatic,
       "cmdExcPreselectInput": cmdExcPreselectInput,
       "cmdExcMode": cmdExcMode,
       "cmdExcNetworkMode": cmdExcNetworkMode,
       "cmdExcTPSSource": cmdExcTPSSource,
       "cmdExcEnableCellID": cmdExcEnableCellID,
       "cmdExcTxAddress": cmdExcTxAddress,
       "cmdExcTxAutomatic": cmdExcTxAutomatic,
       "cmdExcInputAutoSwitch": cmdExcInputAutoSwitch,
       "cmdExcInputSeamless": cmdExcInputSeamless,
       "cmdExcInputPriority": cmdExcInputPriority,
       "cmdExcInputCheckTimeForward": cmdExcInputCheckTimeForward,
       "cmdExcInputCheckTimeSwitchback": cmdExcInputCheckTimeSwitchback,
       "cmdExcInputMuteOnFail": cmdExcInputMuteOnFail,
       "cmdExcInputManualPreseletionHP1": cmdExcInputManualPreseletionHP1,
       "cmdExcInputManualPreseletionHP2": cmdExcInputManualPreseletionHP2,
       "cmdExcInputManualPreseletionLP1": cmdExcInputManualPreseletionLP1,
       "cmdExcInputManualPreseletionLP2": cmdExcInputManualPreseletionLP2,
       "cmdExcTPSManualBandwidth": cmdExcTPSManualBandwidth,
       "cmdExcTPSManualFFTLength": cmdExcTPSManualFFTLength,
       "cmdExcTPSManualGuardInterval": cmdExcTPSManualGuardInterval,
       "cmdExcTPSManualConstellation": cmdExcTPSManualConstellation,
       "cmdExcTPSManualAlpha": cmdExcTPSManualAlpha,
       "cmdExcTPSManualCellID": cmdExcTPSManualCellID,
       "cmdExcTPSManualInterleaver": cmdExcTPSManualInterleaver,
       "cmdExcTPSManualCoderateHP": cmdExcTPSManualCoderateHP,
       "cmdExcTPSManualCoderateLP": cmdExcTPSManualCoderateLP,
       "cmdExcTPSManualTimeSlicingHP": cmdExcTPSManualTimeSlicingHP,
       "cmdExcTPSManualTimeSlicingLP": cmdExcTPSManualTimeSlicingLP,
       "cmdExcTPSManualFECHP": cmdExcTPSManualFECHP,
       "cmdExcTPSManualFECLP": cmdExcTPSManualFECLP,
       "cmdExcSFNStaticDelay": cmdExcSFNStaticDelay,
       "cmdExcSFNDeviationTime": cmdExcSFNDeviationTime,
       "cmdExcFrequency": cmdExcFrequency,
       "cmdExcReferenceSource": cmdExcReferenceSource,
       "cmdExcMuteOnPPSFail": cmdExcMuteOnPPSFail,
       "cmdExcMuteOnReferenceFail": cmdExcMuteOnReferenceFail,
       "cmdExcRefFailDelayTime": cmdExcRefFailDelayTime,
       "cmdExcTypeLossOfInput": cmdExcTypeLossOfInput,
       "cmdExcRfOutput": cmdExcRfOutput,
       "cmdExcRfOutputRegulation": cmdExcRfOutputRegulation,
       "cmdExcRfOutputManualRfLevel": cmdExcRfOutputManualRfLevel,
       "cmdExcRfOutputAttenuation": cmdExcRfOutputAttenuation,
       "cmdExcRfOutputRfSlope": cmdExcRfOutputRfSlope,
       "cmdExcRfOutputModulationSlope": cmdExcRfOutputModulationSlope,
       "cmdExcRfIqAdjustStart": cmdExcRfIqAdjustStart,
       "cmdExcRfIqAdjustTestsignal": cmdExcRfIqAdjustTestsignal,
       "cmdExcRfIqAdjustBiasCoarseI": cmdExcRfIqAdjustBiasCoarseI,
       "cmdExcRfIqAdjustBiasCoarseQ": cmdExcRfIqAdjustBiasCoarseQ,
       "cmdExcRfIqAdjustBiasFineI": cmdExcRfIqAdjustBiasFineI,
       "cmdExcRfIqAdjustBiasFineQ": cmdExcRfIqAdjustBiasFineQ,
       "cmdExcRfIqAdjustGainI": cmdExcRfIqAdjustGainI,
       "cmdExcRfIqAdjustGainQ": cmdExcRfIqAdjustGainQ,
       "cmdExcRfIqAdjustPhase": cmdExcRfIqAdjustPhase,
       "cmdExcInput1Source": cmdExcInput1Source,
       "cmdExcInput2Source": cmdExcInput2Source,
       "cmdExcInpAutoReadyAfterChangeOv": cmdExcInpAutoReadyAfterChangeOv,
       "cmdExcInputFailDelayTime": cmdExcInputFailDelayTime,
       "cmdExcTransmitterType": cmdExcTransmitterType,
       "cmdExcTimeScheduler": cmdExcTimeScheduler,
       "cmdExcMuteCondition": cmdExcMuteCondition,
       "cmdExcRfWarningLimit": cmdExcRfWarningLimit,
       "cmdExcRfFailLimit": cmdExcRfFailLimit,
       "cmdExcOutputPower": cmdExcOutputPower,
       "cmdOstRefVoltageVision": cmdOstRefVoltageVision,
       "cmdOstMaxOutletTempThreshold": cmdOstMaxOutletTempThreshold,
       "cmdExcMonitoringOutput": cmdExcMonitoringOutput,
       "cmdExcOcxoAdjust": cmdExcOcxoAdjust,
       "cmdExcExpectInputReserve": cmdExcExpectInputReserve,
       "cmdExcEnablePcrReset": cmdExcEnablePcrReset,
       "cmdExcTimeForDailyPcrReset": cmdExcTimeForDailyPcrReset,
       "cmdExcFailDelayMode": cmdExcFailDelayMode,
       "summaryInfo": summaryInfo,
       "summaryFaultTx": summaryFaultTx,
       "summaryWarningTx": summaryWarningTx,
       "localModeTx": localModeTx,
       "rfOnTx": rfOnTx,
       "forwardPower": forwardPower,
       "reflectedPower": reflectedPower,
       "summaryFaultExcA": summaryFaultExcA,
       "summaryFaultOstA": summaryFaultOstA,
       "summaryFaultExcB": summaryFaultExcB,
       "summaryFaultOstB": summaryFaultOstB,
       "exciterAutomaticReady": exciterAutomaticReady,
       "exciterAutomaticChanged": exciterAutomaticChanged,
       "exciterAutomaticFault": exciterAutomaticFault,
       "outputstageAutomaticReady": outputstageAutomaticReady,
       "outputstageAutomaticChanged": outputstageAutomaticChanged,
       "outputstageAutomaticFault": outputstageAutomaticFault,
       "noConnectionExcA": noConnectionExcA,
       "noConnectionOstA": noConnectionOstA,
       "noConnectionExcB": noConnectionExcB,
       "noConnectionOstB": noConnectionOstB,
       "activeExcA": activeExcA,
       "activeOstA": activeOstA,
       "activeExcB": activeExcB,
       "activeOstB": activeOstB,
       "forwardPowerOstA": forwardPowerOstA,
       "reflectedPowerOstA": reflectedPowerOstA,
       "forwardPowerOstB": forwardPowerOstB,
       "reflectedPowerOstB": reflectedPowerOstB,
       "powerSupply": powerSupply,
       "additionalPowerSupply": additionalPowerSupply,
       "internalPowerSupply": internalPowerSupply,
       "externalPowerSupply": externalPowerSupply,
       "detailedInfo": detailedInfo,
       "excInputTable": excInputTable,
       "excInputEntry": excInputEntry,
       "excInputExcIdx": excInputExcIdx,
       "excInputChannelIdx": excInputChannelIdx,
       "excInputChannelName": excInputChannelName,
       "excInputConnected": excInputConnected,
       "excInputSeamless": excInputSeamless,
       "excInputPreselected": excInputPreselected,
       "excInputActive": excInputActive,
       "excInputMipFail": excInputMipFail,
       "excInputBandwidth": excInputBandwidth,
       "excInputFFTLength": excInputFFTLength,
       "excInputGuardInterval": excInputGuardInterval,
       "excInputConstellation": excInputConstellation,
       "excInputAlpha": excInputAlpha,
       "excInputCellID": excInputCellID,
       "excInputInterleaver": excInputInterleaver,
       "excInputCodeRate": excInputCodeRate,
       "excInputPacketLength": excInputPacketLength,
       "excInputMeasuredDatarate": excInputMeasuredDatarate,
       "excInputRequiredDatarate": excInputRequiredDatarate,
       "excInputMaximumDelay": excInputMaximumDelay,
       "ostTable": ostTable,
       "ostEntry": ostEntry,
       "ostIdx": ostIdx,
       "ostRackIdx": ostRackIdx,
       "ostRackInletTemperature": ostRackInletTemperature,
       "ostRackOutletTemperature": ostRackOutletTemperature,
       "ostRackAuxPowerSupply": ostRackAuxPowerSupply,
       "ostRackAmpIdx": ostRackAmpIdx,
       "ostRackAmpI1A": ostRackAmpI1A,
       "ostRackAmpI2A": ostRackAmpI2A,
       "ostRackAmpI3A": ostRackAmpI3A,
       "ostRackAmpI4A": ostRackAmpI4A,
       "ostRackAmpI1B": ostRackAmpI1B,
       "ostRackAmpI2B": ostRackAmpI2B,
       "ostRackAmpI3B": ostRackAmpI3B,
       "ostRackAmpI4B": ostRackAmpI4B,
       "ostRackAmpIDrv": ostRackAmpIDrv,
       "ostRackAmpUDc": ostRackAmpUDc,
       "ostRackAmpIDc": ostRackAmpIDc,
       "ostRackAmpUDcControl": ostRackAmpUDcControl,
       "ostRackAmpUReg": ostRackAmpUReg,
       "ostRackAmpPowerA": ostRackAmpPowerA,
       "ostRackAmpPowerB": ostRackAmpPowerB,
       "ostRackAmpPowerOut": ostRackAmpPowerOut,
       "ostRackAmpPowerReflection": ostRackAmpPowerReflection,
       "ostRackAmpPowerReference": ostRackAmpPowerReference,
       "ostRackAmpDeltaPhase": ostRackAmpDeltaPhase,
       "ostRackAmpCmdDeltaPhase": ostRackAmpCmdDeltaPhase,
       "exciterStatusTable": exciterStatusTable,
       "exciterStatusEntry": exciterStatusEntry,
       "excStatusExcIdx": excStatusExcIdx,
       "excStatusRfOutputAgcRegulation": excStatusRfOutputAgcRegulation,
       "excStatusRfIqAdjustAuto": excStatusRfIqAdjustAuto,
       "excStatusRfIqAdjustLO1Frequency": excStatusRfIqAdjustLO1Frequency,
       "excStatusNominalPower": excStatusNominalPower,
       "excStatusVSWR": excStatusVSWR,
       "excStatusSfnDelayProcessing": excStatusSfnDelayProcessing,
       "excStatusSfnDelayDynamic": excStatusSfnDelayDynamic,
       "excStatusSfnDelayNetwork": excStatusSfnDelayNetwork,
       "excStatusSfnDelayTxOffset": excStatusSfnDelayTxOffset,
       "excStatusSfnDelayMaximum": excStatusSfnDelayMaximum,
       "excStatusSfnDelayTotal": excStatusSfnDelayTotal,
       "excStatusAmplifierControl": excStatusAmplifierControl,
       "excStatusReqDataRateHP": excStatusReqDataRateHP,
       "excStatusReqDataRateLP": excStatusReqDataRateLP,
       "excStatusFailDelay": excStatusFailDelay,
       "exciterPrecorrectionTable": exciterPrecorrectionTable,
       "exciterPrecorrectionEntry": exciterPrecorrectionEntry,
       "excPrecExcIdx": excPrecExcIdx,
       "excPrecLinCorrection": excPrecLinCorrection,
       "excPrecLinAutomaticADE": excPrecLinAutomaticADE,
       "excPrecLinMaxAmplitudeRipple": excPrecLinMaxAmplitudeRipple,
       "excPrecLinMaxGroupDelayRipple": excPrecLinMaxGroupDelayRipple,
       "excPrecLinAmplitudeRipple": excPrecLinAmplitudeRipple,
       "excPrecLinGroupDelayRipple": excPrecLinGroupDelayRipple,
       "excPrecLinInputLevel": excPrecLinInputLevel,
       "excPrecLinAutomatic": excPrecLinAutomatic,
       "excPrecNonlinCorrection": excPrecNonlinCorrection,
       "excPrecNonlinAutomaticADE": excPrecNonlinAutomaticADE,
       "excPrecNonlinThresholdShoulders": excPrecNonlinThresholdShoulders,
       "excPrecNonlinShoulderLeft": excPrecNonlinShoulderLeft,
       "excPrecNonlinShoulderRight": excPrecNonlinShoulderRight,
       "excPrecNonlinInputLevel": excPrecNonlinInputLevel,
       "excPrecNonlinAutomatic": excPrecNonlinAutomatic,
       "excPrecUserState": excPrecUserState,
       "excPrecFactoryState": excPrecFactoryState,
       "excPrecRestoreCurrentSettings": excPrecRestoreCurrentSettings,
       "excPrecRestoreAllSettings": excPrecRestoreAllSettings,
       "configurationTable": configurationTable,
       "configurationEntry": configurationEntry,
       "configTvStandardIdx": configTvStandardIdx,
       "configTvStandardName": configTvStandardName,
       "configRxFrequency": configRxFrequency,
       "configFrequency": configFrequency,
       "configPower": configPower,
       "configInputSource": configInputSource,
       "timeSchedulerTable": timeSchedulerTable,
       "timeSchedulerEntry": timeSchedulerEntry,
       "schedulerDateTimeIdx": schedulerDateTimeIdx,
       "schedulerRowStatus": schedulerRowStatus,
       "schedulerEvent": schedulerEvent,
       "schedulerDateTime": schedulerDateTime,
       "schedulerTvStandard": schedulerTvStandard,
       "configuration2Table": configuration2Table,
       "configuration2Entry": configuration2Entry,
       "config2TvStandardName": config2TvStandardName,
       "config2RxFrequency": config2RxFrequency,
       "config2Frequency": config2Frequency,
       "config2Power": config2Power,
       "config2InputSource": config2InputSource,
       "productInfoTable": productInfoTable,
       "productInfoEntry": productInfoEntry,
       "prodInfoModuleIdx": prodInfoModuleIdx,
       "prodInfoDeviceIdx": prodInfoDeviceIdx,
       "prodInfoRackIdx": prodInfoRackIdx,
       "prodInfoAmpIdx": prodInfoAmpIdx,
       "prodInfoModuleName": prodInfoModuleName,
       "prodInfoSerialNumber": prodInfoSerialNumber,
       "prodInfoIdentNumberSW": prodInfoIdentNumberSW,
       "prodInfoVersionNumberSW": prodInfoVersionNumberSW,
       "prodInfoIdentNumberHW": prodInfoIdentNumberHW,
       "prodInfoVersionNumberHW": prodInfoVersionNumberHW,
       "productInfoProductDateHW": productInfoProductDateHW,
       "logbook": logbook,
       "netCCUNumberOfEntries": netCCUNumberOfEntries,
       "netCCULogbookClear": netCCULogbookClear,
       "netCCULogbookTable": netCCULogbookTable,
       "netCCULogbookEntry": netCCULogbookEntry,
       "netCCULogbookEntryIdx": netCCULogbookEntryIdx,
       "netCCULogbookEntryNbr": netCCULogbookEntryNbr,
       "netCCULogbookType": netCCULogbookType,
       "netCCULogbookSlope": netCCULogbookSlope,
       "netCCULogbookMessage": netCCULogbookMessage,
       "netCCULogbookDateTime": netCCULogbookDateTime,
       "exciterANumberOfEntries": exciterANumberOfEntries,
       "exciterALogbookClear": exciterALogbookClear,
       "exciterALogbookTable": exciterALogbookTable,
       "exciterALogbookEntry": exciterALogbookEntry,
       "excALogbookEntryIdx": excALogbookEntryIdx,
       "excALogbookEntryNbr": excALogbookEntryNbr,
       "excALogbookType": excALogbookType,
       "excALogbookSlope": excALogbookSlope,
       "excALogbookMessage": excALogbookMessage,
       "excALogbookDateTime": excALogbookDateTime,
       "outputstageANumberOfEntries": outputstageANumberOfEntries,
       "outputstageALogbookClear": outputstageALogbookClear,
       "outputstageALogbookTable": outputstageALogbookTable,
       "outputstageALogbookEntry": outputstageALogbookEntry,
       "ostALogbookEntryIdx": ostALogbookEntryIdx,
       "ostALogbookEntryNbr": ostALogbookEntryNbr,
       "ostALogbookType": ostALogbookType,
       "ostALogbookSlope": ostALogbookSlope,
       "ostALogbookMessage": ostALogbookMessage,
       "ostALogbookDateTime": ostALogbookDateTime,
       "exciterBNumberOfEntries": exciterBNumberOfEntries,
       "exciterBLogbookClear": exciterBLogbookClear,
       "exciterBLogbookTable": exciterBLogbookTable,
       "exciterBLogbookEntry": exciterBLogbookEntry,
       "excBLogbookEntryIdx": excBLogbookEntryIdx,
       "excBLogbookEntryNbr": excBLogbookEntryNbr,
       "excBLogbookType": excBLogbookType,
       "excBLogbookSlope": excBLogbookSlope,
       "excBLogbookMessage": excBLogbookMessage,
       "excBLogbookDateTime": excBLogbookDateTime,
       "outputstageBNumberOfEntries": outputstageBNumberOfEntries,
       "outputstageBLogbookClear": outputstageBLogbookClear,
       "outputstageBLogbookTable": outputstageBLogbookTable,
       "outputstageBLogbookEntry": outputstageBLogbookEntry,
       "ostBLogbookEntryIdx": ostBLogbookEntryIdx,
       "ostBLogbookEntryNbr": ostBLogbookEntryNbr,
       "ostBLogbookType": ostBLogbookType,
       "ostBLogbookSlope": ostBLogbookSlope,
       "ostBLogbookMessage": ostBLogbookMessage,
       "ostBLogbookDateTime": ostBLogbookDateTime,
       "rfProbesTable": rfProbesTable,
       "rfProbesEntry": rfProbesEntry,
       "rfProbesNetCCURfProbe1": rfProbesNetCCURfProbe1,
       "rfProbesNetCCURfProbe2": rfProbesNetCCURfProbe2,
       "rfProbesAntFwdNominal": rfProbesAntFwdNominal,
       "rfProbesAntFwdWarningLimit": rfProbesAntFwdWarningLimit,
       "rfProbesAntFwdFailLimit": rfProbesAntFwdFailLimit,
       "rfProbesAntFwdDelayTimeRfFail": rfProbesAntFwdDelayTimeRfFail,
       "rfProbesAntFwdSetOffset": rfProbesAntFwdSetOffset,
       "rfProbesAntFwdSetGain": rfProbesAntFwdSetGain,
       "rfProbesAntReflWarningLimit": rfProbesAntReflWarningLimit,
       "rfProbesAntReflSetOffset": rfProbesAntReflSetOffset,
       "rfProbesAntReflSetGain": rfProbesAntReflSetGain,
       "rfProbesDLFwdNominal": rfProbesDLFwdNominal,
       "rfProbesDLFwdWarningLimit": rfProbesDLFwdWarningLimit,
       "rfProbesDLFwdFailLimit": rfProbesDLFwdFailLimit,
       "rfProbesDLFwdDelayTimeRfFail": rfProbesDLFwdDelayTimeRfFail,
       "rfProbesDLFwdSetOffset": rfProbesDLFwdSetOffset,
       "rfProbesDLFwdSetGain": rfProbesDLFwdSetGain,
       "rfProbesDLReflWarningLimit": rfProbesDLReflWarningLimit,
       "rfProbesDLReflSetOffset": rfProbesDLReflSetOffset,
       "rfProbesDLReflSetGain": rfProbesDLReflSetGain,
       "rfProbesOstIdx": rfProbesOstIdx,
       "rfProbesOstFwdNominal": rfProbesOstFwdNominal,
       "rfProbesOstFwdWarningLimit": rfProbesOstFwdWarningLimit,
       "rfProbesOstFwdFailLimit": rfProbesOstFwdFailLimit,
       "rfProbesOstFwdDelayTimeRfFail": rfProbesOstFwdDelayTimeRfFail,
       "rfProbesOstFwdSetOffset": rfProbesOstFwdSetOffset,
       "rfProbesOstFwdSetGain": rfProbesOstFwdSetGain,
       "rfProbesOstReflWarningLimit": rfProbesOstReflWarningLimit,
       "rfProbesOstReflSetOffset": rfProbesOstReflSetOffset,
       "rfProbesOstReflSetGain": rfProbesOstReflSetGain,
       "rackTable": rackTable,
       "rackEntry": rackEntry,
       "ostDeviceIdx": ostDeviceIdx,
       "rackIdx": rackIdx,
       "rackRfProbeIdx": rackRfProbeIdx,
       "amplifiersPerRack": amplifiersPerRack,
       "rackRfEventSignalling": rackRfEventSignalling,
       "rackReferenceVoltage": rackReferenceVoltage,
       "amplifiersPowerSupply": amplifiersPowerSupply,
       "rackGeneralPurposeInput": rackGeneralPurposeInput,
       "rackOnOff": rackOnOff,
       "rfProbePresent": rfProbePresent,
       "rfProbeConfigurationLabel": rfProbeConfigurationLabel,
       "rfProbeConfigurationNominalValue": rfProbeConfigurationNominalValue,
       "rfProbeThresholdRfFailLimit": rfProbeThresholdRfFailLimit,
       "rfProbeThresholdTimeoutRfFailCtr": rfProbeThresholdTimeoutRfFailCtr,
       "rfProbeThresholdWarningLimit": rfProbeThresholdWarningLimit,
       "rfProbeCalibrationGain": rfProbeCalibrationGain,
       "rfProbeCalibrationOffset": rfProbeCalibrationOffset,
       "rfProbeCalibrationSetGain": rfProbeCalibrationSetGain,
       "rfProbeCalibrationSetOffset": rfProbeCalibrationSetOffset,
       "rfProbeMeasuredValue": rfProbeMeasuredValue,
       "sx801AmplifierTable": sx801AmplifierTable,
       "sx801AmplifierEntry": sx801AmplifierEntry,
       "sx801AmpIdx": sx801AmpIdx,
       "sx801AmpRfOut": sx801AmpRfOut,
       "sx801AmpRfIn": sx801AmpRfIn,
       "sx801AmpReflection": sx801AmpReflection,
       "sx801AmpOn": sx801AmpOn,
       "sx801AmpAC": sx801AmpAC,
       "sx801AmpCommunication": sx801AmpCommunication,
       "sx801AmpTransistor": sx801AmpTransistor,
       "sx801AmpDriver": sx801AmpDriver,
       "sx801AmpTemperature": sx801AmpTemperature,
       "sx801AmpBlower": sx801AmpBlower,
       "sx801AmpRegulation": sx801AmpRegulation,
       "sx801AmpUpdate": sx801AmpUpdate,
       "sx801Supply1Temperature": sx801Supply1Temperature,
       "sx801Supply2Temperature": sx801Supply2Temperature,
       "sx801SupplyRTemperature": sx801SupplyRTemperature,
       "sx801Supply1DC": sx801Supply1DC,
       "sx801Supply2DC": sx801Supply2DC,
       "sx801SupplyRDC": sx801SupplyRDC,
       "sx801AmpValueI1": sx801AmpValueI1,
       "sx801AmpValueI2": sx801AmpValueI2,
       "sx801AmpValueI3": sx801AmpValueI3,
       "sx801AmpValueI4": sx801AmpValueI4,
       "sx801AmpValueIPre": sx801AmpValueIPre,
       "sx801AmpValueIDrv1": sx801AmpValueIDrv1,
       "sx801AmpValueIDrv2": sx801AmpValueIDrv2,
       "sx801AmpValuePowerOut": sx801AmpValuePowerOut,
       "sx801AmpValueReflection": sx801AmpValueReflection,
       "sx801AmpValueVRef": sx801AmpValueVRef,
       "sx801AmpValueVReg": sx801AmpValueVReg,
       "sx801AmpValueTemperature": sx801AmpValueTemperature,
       "sx801AmpValueMonAtt": sx801AmpValueMonAtt,
       "sx801AmpValueVAux1": sx801AmpValueVAux1,
       "sx801AmpValueVAux2": sx801AmpValueVAux2,
       "sx801Supply1ValuePwr": sx801Supply1ValuePwr,
       "sx801Supply2ValuePwr": sx801Supply2ValuePwr,
       "sx801Supply1ValueDc": sx801Supply1ValueDc,
       "sx801Supply2ValueDc": sx801Supply2ValueDc,
       "rsXx8000DvbTxEvents": rsXx8000DvbTxEvents,
       "eventTx": eventTx,
       "eventsTxV2": eventsTxV2,
       "txSummaryFault": txSummaryFault,
       "txSummaryWarning": txSummaryWarning,
       "txLocal": txLocal,
       "txRfOn": txRfOn,
       "txRfOk": txRfOk,
       "txParamSetSubDeviceDiffers": txParamSetSubDeviceDiffers,
       "txParamSetValuesChanged": txParamSetValuesChanged,
       "txRfLoopProgram": txRfLoopProgram,
       "txRfLoopReserve": txRfLoopReserve,
       "txRfWarning": txRfWarning,
       "txReflectionWarning": txReflectionWarning,
       "txNetCCUFanFault": txNetCCUFanFault,
       "txNetCCUPowerSupply": txNetCCUPowerSupply,
       "txRfFail": txRfFail,
       "txReflectionFault": txReflectionFault,
       "txNetCCUBoardTemperatureFault": txNetCCUBoardTemperatureFault,
       "txNetCCUNoConnectionToExcA": txNetCCUNoConnectionToExcA,
       "txNetCCUNoConnectionToOstA": txNetCCUNoConnectionToOstA,
       "txNetCCUNoConnectionToExcB": txNetCCUNoConnectionToExcB,
       "txNetCCUNoConnectionToOstB": txNetCCUNoConnectionToOstB,
       "txAutomaticExcReady": txAutomaticExcReady,
       "txAutomaticExcChanged": txAutomaticExcChanged,
       "txAutomaticExcFault": txAutomaticExcFault,
       "txAutomaticOstReady": txAutomaticOstReady,
       "txAutomaticOstChanged": txAutomaticOstChanged,
       "txAutomaticOstFault": txAutomaticOstFault,
       "txNetCCUBoardTemperatureWarning": txNetCCUBoardTemperatureWarning,
       "txInternalPowerSupplyWarning": txInternalPowerSupplyWarning,
       "txExternalPowerSupplyWarning": txExternalPowerSupplyWarning,
       "txModeSwitchOverStarted": txModeSwitchOverStarted,
       "txModeSwitchOverEnded": txModeSwitchOverEnded,
       "txModeInconsistent": txModeInconsistent,
       "txModeSwitchOverFailed": txModeSwitchOverFailed,
       "txExcSummaryFault": txExcSummaryFault,
       "txExcSummaryWarning": txExcSummaryWarning,
       "txExcLocal": txExcLocal,
       "txExcRfOk": txExcRfOk,
       "txExcInputNoConnectHP1": txExcInputNoConnectHP1,
       "txExcInputNoConnectLP1": txExcInputNoConnectLP1,
       "txExcInputNoConnectHP2": txExcInputNoConnectHP2,
       "txExcInputNoConnectLP2": txExcInputNoConnectLP2,
       "txExcInputActiveHP1": txExcInputActiveHP1,
       "txExcInputActiveLP1": txExcInputActiveLP1,
       "txExcInputActiveHP2": txExcInputActiveHP2,
       "txExcInputActiveLP2": txExcInputActiveLP2,
       "txExcOn": txExcOn,
       "txExcRfOn": txExcRfOn,
       "txExcNoInput": txExcNoInput,
       "txExcRfLoop": txExcRfLoop,
       "txExcRfFail": txExcRfFail,
       "txExcSelfTest": txExcSelfTest,
       "txExcOutputOpen": txExcOutputOpen,
       "txExcBoardTemperatureWarning": txExcBoardTemperatureWarning,
       "txExcFanWarning": txExcFanWarning,
       "txExcFanFault": txExcFanFault,
       "txExcFifoWarning": txExcFifoWarning,
       "txExcTestSignal": txExcTestSignal,
       "txExcSFNDelay": txExcSFNDelay,
       "txExcWrongDatarate": txExcWrongDatarate,
       "txExcMute": txExcMute,
       "txExcPPSFail": txExcPPSFail,
       "txExcReferenceFail": txExcReferenceFail,
       "txExcMIPFail": txExcMIPFail,
       "txExcInputAutomaticSwitchReady": txExcInputAutomaticSwitchReady,
       "txExcInputAutomaticChangedOver": txExcInputAutomaticChangedOver,
       "txExcInputReseveMissing": txExcInputReseveMissing,
       "txOstSummaryFault": txOstSummaryFault,
       "txOstSummaryWarning": txOstSummaryWarning,
       "txOstRfOn": txOstRfOn,
       "txOstRfOk": txOstRfOk,
       "txOstNoInput": txOstNoInput,
       "txOstRfWarning": txOstRfWarning,
       "txOstReflectionWarning": txOstReflectionWarning,
       "txOstRackWarning": txOstRackWarning,
       "txOstCoolingWarning": txOstCoolingWarning,
       "txOstRfFail": txOstRfFail,
       "txOstReflectionFault": txOstReflectionFault,
       "txOstACFault": txOstACFault,
       "txOstCoolingFault": txOstCoolingFault,
       "txOstCommFault": txOstCommFault,
       "txRackSumFault": txRackSumFault,
       "txRackSumWarning": txRackSumWarning,
       "txRackOn": txRackOn,
       "txRackGpiWarning": txRackGpiWarning,
       "txRackFan1Fault": txRackFan1Fault,
       "txRackFan2Fault": txRackFan2Fault,
       "txRackCoolingSumWarning": txRackCoolingSumWarning,
       "txRackAmplifierSumFault": txRackAmplifierSumFault,
       "txRackNoLink": txRackNoLink,
       "txRackGpiFault": txRackGpiFault,
       "txRackTemperatureFault": txRackTemperatureFault,
       "txRackACFault": txRackACFault,
       "txRackCoolingSumFault": txRackCoolingSumFault,
       "txRackTempFaultAbs1": txRackTempFaultAbs1,
       "txRackTempFaultAbs2": txRackTempFaultAbs2,
       "txRackDCFault": txRackDCFault,
       "txRackRfOn": txRackRfOn,
       "txRackRfOk": txRackRfOk,
       "txRackRfWarning": txRackRfWarning,
       "txRackRfFault": txRackRfFault,
       "txRackReflectionWarning": txRackReflectionWarning,
       "txRackReflectionFault": txRackReflectionFault,
       "txRackProbeNotCalibrated": txRackProbeNotCalibrated,
       "txRackTemperatureWarning": txRackTemperatureWarning,
       "txRackOvervoltProtectWarning": txRackOvervoltProtectWarning,
       "txAmpSumFault": txAmpSumFault,
       "txAmpSumWarning": txAmpSumWarning,
       "txAmpPowerOn": txAmpPowerOn,
       "txAmpDCOk": txAmpDCOk,
       "txAmpACOk": txAmpACOk,
       "txAmpRfInFail": txAmpRfInFail,
       "txAmpRfFail": txAmpRfFail,
       "txAmpReflectionFault": txAmpReflectionFault,
       "txAmpTemperatureFault": txAmpTemperatureFault,
       "txAmpTransistorFault": txAmpTransistorFault,
       "eventsTxTable": eventsTxTable,
       "eventsTxEntry": eventsTxEntry,
       "eventTxABIdx": eventTxABIdx,
       "eventTxRackIdx": eventTxRackIdx,
       "eventTxAmpIdx": eventTxAmpIdx,
       "eventTxNameIdx": eventTxNameIdx,
       "eventTxName": eventTxName,
       "eventTxMask": eventTxMask,
       "eventTxPriority": eventTxPriority,
       "eventTxEvent": eventTxEvent,
       "rsXx8000DvbTxConf": rsXx8000DvbTxConf,
       "rsXx8000DvbTxGroups": rsXx8000DvbTxGroups,
       "groupEvents": groupEvents,
       "groupTxCommon": groupTxCommon,
       "groupEventsTxCommon": groupEventsTxCommon,
       "groupDualDrive": groupDualDrive,
       "groupEventsDualDrive": groupEventsDualDrive,
       "groupPowerReserve": groupPowerReserve,
       "groupEventsPowerReserve": groupEventsPowerReserve,
       "groupCommonMP": groupCommonMP,
       "groupEventsCommonMP": groupEventsCommonMP,
       "groupCommonNetCCU": groupCommonNetCCU,
       "groupEventsCommonNetCCU": groupEventsCommonNetCCU,
       "groupOstBLogbook": groupOstBLogbook,
       "groupSumProbe": groupSumProbe,
       "groupProductInfo": groupProductInfo,
       "groupAmpMeasureValues": groupAmpMeasureValues,
       "groupEventsAmplifier": groupEventsAmplifier,
       "groupRfProbes": groupRfProbes,
       "groupDummyLoadRF": groupDummyLoadRF,
       "groupExcCommon": groupExcCommon,
       "groupExcAdditionalSx800": groupExcAdditionalSx800,
       "groupExcAdditionalSLx": groupExcAdditionalSLx,
       "groupEventsExciter": groupEventsExciter,
       "groupExciterStatus": groupExciterStatus,
       "groupExciterPrecorrection": groupExciterPrecorrection,
       "groupSLx": groupSLx,
       "groupObjectsACU": groupObjectsACU,
       "groupIndependentRacks": groupIndependentRacks,
       "groupObjectsRE": groupObjectsRE,
       "groupEventsControlExciter": groupEventsControlExciter,
       "groupEventsAdditionalPowerSupply": groupEventsAdditionalPowerSupply,
       "groupObjsAdditionalPowerSupply": groupObjsAdditionalPowerSupply,
       "groupObjectsControlExciter": groupObjectsControlExciter,
       "groupObjectsSingleEnded": groupObjectsSingleEnded,
       "groupObjectsSx801Amplifier": groupObjectsSx801Amplifier,
       "groupObsoleted": groupObsoleted,
       "groupEventsObsoleted": groupEventsObsoleted,
       "rsXx8000DvbTxCompl": rsXx8000DvbTxCompl,
       "rsXx8000DVBSingleTxMP": rsXx8000DVBSingleTxMP,
       "rsXx8000DVBDualDriveMP": rsXx8000DVBDualDriveMP,
       "rsXx8000DVBPowerReserveMP": rsXx8000DVBPowerReserveMP,
       "rsXx8000DVBSingleTxLP": rsXx8000DVBSingleTxLP,
       "rsXx8000DVBDualDriveLP": rsXx8000DVBDualDriveLP,
       "rsXx8000DVBPowerReserveLP": rsXx8000DVBPowerReserveLP,
       "rsXx8000DVBSingleTxLPNoNetCCU": rsXx8000DVBSingleTxLPNoNetCCU,
       "rsXx8000DVBSLx": rsXx8000DVBSLx,
       "rsXx8000DVBExciterOnly": rsXx8000DVBExciterOnly,
       "rsXx8000DVBSx801ControlExciter": rsXx8000DVBSx801ControlExciter,
       "rsXx8000DvbTxMibModule": rsXx8000DvbTxMibModule}
)
