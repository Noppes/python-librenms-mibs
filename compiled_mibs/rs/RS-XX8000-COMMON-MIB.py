# SNMP MIB module (RS-XX8000-COMMON-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\rs\RS-XX8000-COMMON-MIB

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

(rsProdBroadcastTransmitter,
 rsRegModules) = mibBuilder.importSymbols(
    "RS-COMMON-MIB",
    "rsProdBroadcastTransmitter",
    "rsRegModules")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "PhysAddress",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

rsXx8000MibModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2566, 149, 1, 163)
)
if mibBuilder.loadTexts:
    rsXx8000MibModule.setRevisions(
        ("2011-05-11 08:00",
         "2011-02-23 08:00",
         "2010-05-06 08:00",
         "2009-12-08 08:00",
         "2009-09-10 08:00",
         "2009-06-26 09:00",
         "2009-06-03 09:00",
         "2009-04-30 09:00",
         "2009-03-13 09:00",
         "2009-02-10 16:00",
         "2008-12-12 14:00",
         "2008-10-20 09:00",
         "2008-10-10 09:00",
         "2008-09-30 09:00",
         "2008-09-03 09:00",
         "2008-07-23 15:30",
         "2008-06-16 09:00",
         "2008-06-10 08:00",
         "2008-06-02 10:30",
         "2008-05-13 15:00",
         "2008-04-23 11:00",
         "2008-02-18 13:30",
         "2008-02-11 12:00",
         "2008-02-06 12:00",
         "2007-12-17 12:00",
         "2007-10-02 10:00",
         "2007-09-04 13:00",
         "2007-06-29 10:00",
         "2007-05-16 10:00",
         "2007-03-14 10:00",
         "2006-12-21 10:00",
         "2006-11-20 10:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class ReadableString(TextualConvention, OctetString):
    status = "current"
    displayHint = "255a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )



class FloatingPoint(TextualConvention, OctetString):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 63),
    )



class TimeOfDay(TextualConvention, OctetString):
    status = "current"
    displayHint = "1d:1d:1d"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
        ValueSizeConstraint(3, 3),
    )



class EventMask(TextualConvention, Integer32):
    status = "current"
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



class EventPriority(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )



class EventClass(TextualConvention, Integer32):
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
        *(("fault", 1),
          ("warning", 2),
          ("info", 3))
    )



class EventState(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("inactive", 2))
    )



class EventMaxEntryNumber(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 999),
    )



class SwitchOnOff(TextualConvention, Integer32):
    status = "current"
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



class Trigger(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("idle", 1),
          ("trigger", 2))
    )



class LogbookEntryMessagesNetCCU(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(3,
              4,
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
              30,
              37,
              38,
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
              51,
              52,
              53,
              54,
              55,
              56,
              57,
              58,
              59,
              60,
              61,
              62,
              70,
              81,
              82,
              83,
              84,
              85,
              86,
              87,
              88,
              89,
              90,
              91,
              92,
              93,
              95,
              96,
              97,
              98,
              99,
              100,
              101,
              102,
              103,
              104,
              107,
              108,
              109)
        )
    )
    namedValues = NamedValues(
        *(("local", 3),
          ("rfOn", 4),
          ("excAutoReady", 6),
          ("excAutoChanged", 7),
          ("ostAutoReady", 8),
          ("ostAutoChanged", 9),
          ("rfOnSound1", 10),
          ("rfOnSound2", 11),
          ("activeExcA", 12),
          ("activeExcB", 13),
          ("activeOstA", 14),
          ("activeOstB", 15),
          ("rfOnVision", 16),
          ("rfOnActiveExc", 17),
          ("rfOnDLoad", 18),
          ("rfOkDLoad", 19),
          ("swBackupStarted", 20),
          ("swBackupDone", 21),
          ("swBackupFailed", 22),
          ("swRestoreStarted", 23),
          ("swRestoreDone", 24),
          ("swRestoreFailed", 25),
          ("optionKeyExpired", 30),
          ("txModeSwitchOverStarted", 37),
          ("txModeSwitchOverEnded", 38),
          ("reboot", 40),
          ("rfLoopProgram", 41),
          ("rfLoopReserve", 42),
          ("rfWarning", 43),
          ("reflectionWarning", 44),
          ("intPwrSupply", 45),
          ("extPwrSupply", 46),
          ("rfVisionWarning", 47),
          ("rfSound1Warning", 48),
          ("rfSound2Warning", 49),
          ("fanFault", 51),
          ("sumWarningRec", 52),
          ("sumWarningExcA", 53),
          ("sumWarningExcB", 54),
          ("sumWarningOstA", 55),
          ("sumWarningOstB", 56),
          ("rfDLoadWarning", 57),
          ("rfDLoadReflection", 58),
          ("receiverConnect", 59),
          ("receiverSumFault", 60),
          ("txModeInconsistent", 61),
          ("boardTemperatureWarning", 62),
          ("optionKeyWillExpire", 70),
          ("powerSupply", 81),
          ("rfFail", 82),
          ("reflectionFault", 83),
          ("boardTemperature", 84),
          ("excSwitch", 85),
          ("ostSwitch", 86),
          ("connectionExcA", 87),
          ("connectionExcB", 88),
          ("connectionOstA", 89),
          ("connectionOstB", 90),
          ("rfVision", 91),
          ("rfSound1Fault", 92),
          ("rfSound2Fault", 93),
          ("connectionRec", 95),
          ("summaryFaultRec", 96),
          ("summaryFaultExcA", 97),
          ("summaryFaultExcB", 98),
          ("summaryFaultOstA", 99),
          ("summaryFaultOstB", 100),
          ("rfDLoadFault", 101),
          ("rfDLoadReflectionFault", 102),
          ("apaConnect", 103),
          ("absorber", 104),
          ("monitorFaultExcA", 107),
          ("monitorFaultExcB", 108),
          ("txModeSwitchOverFailed", 109))
    )



class LogbookEntryMessagesExcTv(TextualConvention, Integer32):
    status = "current"
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
              28,
              30,
              37,
              38,
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
              50,
              51,
              52,
              53,
              54,
              55,
              56,
              57,
              58,
              59,
              60,
              61,
              62,
              63,
              64,
              65,
              66,
              67,
              68,
              69,
              70,
              71,
              72,
              73,
              74,
              75,
              76,
              77,
              78,
              100,
              101,
              102,
              103,
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
              170,
              171,
              172,
              173,
              174,
              175,
              176,
              177,
              180,
              181,
              182,
              183,
              184,
              185,
              186,
              187,
              188,
              189,
              190,
              191,
              192,
              193,
              194,
              195,
              196,
              197,
              198,
              199,
              205,
              210,
              211,
              212,
              213,
              214,
              215,
              220,
              221,
              222,
              223,
              230,
              231,
              240,
              241,
              250,
              251,
              256,
              260,
              261,
              262,
              263,
              264,
              265,
              266,
              267,
              268,
              269,
              270,
              271,
              272,
              273,
              274,
              280,
              300,
              301,
              320,
              321,
              322,
              323,
              400,
              401,
              402,
              403,
              404,
              405,
              406,
              407,
              408,
              409,
              410,
              411,
              412,
              413,
              500,
              501,
              502,
              503,
              550,
              551,
              552,
              553,
              554,
              555,
              556,
              557,
              600,
              601,
              602,
              603,
              604,
              605,
              606,
              607,
              608,
              640,
              641,
              642,
              643,
              644,
              650,
              651,
              652,
              653,
              654,
              655,
              656,
              657,
              658,
              659,
              660,
              661,
              662,
              663,
              664,
              665,
              666,
              667,
              675,
              676,
              677,
              678,
              679,
              680,
              681,
              682,
              683,
              684,
              685,
              686,
              687,
              688,
              689,
              690,
              691,
              692,
              700,
              701,
              702,
              703,
              704,
              705,
              706,
              707,
              708,
              709,
              710,
              711,
              712,
              713,
              714,
              715,
              716,
              717,
              725,
              726,
              727,
              728,
              729,
              730,
              731,
              732,
              733,
              734,
              735,
              736,
              737,
              738,
              739,
              740,
              741,
              742,
              770,
              771,
              772,
              800,
              801,
              802,
              803,
              804,
              805,
              806,
              807,
              808)
        )
    )
    namedValues = NamedValues(
        *(("excReboot", 0),
          ("excSumFault", 1),
          ("excSumWarning", 2),
          ("excLocal", 3),
          ("excExciterOn", 4),
          ("excRfOk", 5),
          ("excNoInput", 6),
          ("excReference", 7),
          ("excRfOn", 8),
          ("excMute", 9),
          ("excRelieveReq", 10),
          ("excSwDiag", 11),
          ("excOneFan", 12),
          ("excNoCCUComm", 13),
          ("excSwUpdated", 14),
          ("excBiosUpdated", 15),
          ("excPowerSupply", 16),
          ("excTemperature", 17),
          ("excFans", 18),
          ("excHwMainboard", 19),
          ("excHwCfCard", 20),
          ("excOutputOpen", 21),
          ("excRebootRqst", 22),
          ("excHwEEPROM", 23),
          ("excWatchdog", 24),
          ("excRfFail", 25),
          ("excLoopOpen", 26),
          ("excNoFPGA", 27),
          ("excCarrierLock", 28),
          ("excInputFail", 30),
          ("excOptionExpired", 37),
          ("excOptionWillEnd", 38),
          ("excFPGAConfig", 40),
          ("excHwIIFBoard", 41),
          ("excHwRfBoard", 42),
          ("excHwSynth1", 43),
          ("excHwSynth2", 44),
          ("excHwSynth3", 45),
          ("excMuteAudio1", 46),
          ("excMuteAudio2", 47),
          ("excVideoInp1", 48),
          ("excVideoInp2", 49),
          ("excVideoInpAct", 50),
          ("excRfOutExcV", 51),
          ("excRfOutAntV", 52),
          ("excRfOutExcA1", 53),
          ("excRfOutAntA1", 54),
          ("excRfOutExcA2", 55),
          ("excRfOutAntA2", 56),
          ("excClippingAntInp", 57),
          ("excNoHeadroomAnt", 58),
          ("excAudioMode", 59),
          ("excWhiteLine", 60),
          ("excWhiteLineLnAmp", 61),
          ("excWhiteLineLnAmpW", 62),
          ("excSyncCheck", 63),
          ("excWhiteLimiter", 64),
          ("excDevLimAud1", 65),
          ("excDevLimAud2", 66),
          ("excVideoInpClip", 67),
          ("excAud1InpClip", 68),
          ("excAud2InpClip", 69),
          ("excNICAM728Data", 70),
          ("excNICAM728Carr", 71),
          ("excAud2OutClip", 72),
          ("excRfMonFail", 73),
          ("excRfVideoFail", 74),
          ("excRfAudio1Fail", 75),
          ("excRfAudio2Fail", 76),
          ("excAudioLoopOpen", 77),
          ("excVideoLoopOpen", 78),
          ("excTestMode", 100),
          ("excExtRefFail", 101),
          ("excExtRefWeak", 102),
          ("excExtPPSFail", 103),
          ("excInputSwitched", 104),
          ("excInputFail2", 105),
          ("excWrongDatarate", 106),
          ("excFifoOverUnderflow", 107),
          ("excDelayChanged", 108),
          ("excSFNDelay", 109),
          ("excNoMIP", 110),
          ("excWrongMFArrivalTime", 111),
          ("excExtPPSAsynchron", 112),
          ("excPacketUnlock", 113),
          ("excMaxDelayChanged", 114),
          ("excReferenceAbsent", 115),
          ("excNoPPS", 116),
          ("excRfFailAmplifier", 117),
          ("excWarningAmplifier", 118),
          ("excAmpOverflow", 119),
          ("excModError", 120),
          ("excFLOModErr", 121),
          ("excInput1", 122),
          ("excInput2", 123),
          ("excInput1LP", 124),
          ("excInput2LP", 125),
          ("excNoReserveAvailable", 126),
          ("excSynthesizerUnlocked", 127),
          ("excSFNIdleRegulation", 128),
          ("excAmpVSWR", 170),
          ("excAmpTempWarn", 171),
          ("excAmpTempFault", 172),
          ("excAmpRegulation", 173),
          ("excAmpTransistor", 174),
          ("excAmpReducedPower", 175),
          ("excHWAmpEEPROM", 176),
          ("excRFWarningAmp", 177),
          ("excModSfnRAMInitErr", 180),
          ("excModTransportErr", 181),
          ("excModFIFOParErr", 182),
          ("excModFIFOSeqErr", 183),
          ("excModSfnBufEmpty", 184),
          ("excModSfnBufFull", 185),
          ("excModSsfMultiple", 186),
          ("excModSsfMissing", 187),
          ("excModLofTS1", 188),
          ("excModLofTS2", 189),
          ("excModCoreStall", 190),
          ("excModIqInactive", 191),
          ("excModMtiVersErr", 192),
          ("excModCoreReset", 193),
          ("excModConfigChanged", 194),
          ("excSFNBuffer", 195),
          ("excModIdleMode", 196),
          ("excSFNBufferTooEmpty", 197),
          ("excModMemError", 198),
          ("excSfnBufferTooFull", 199),
          ("excMissingSIP", 205),
          ("excTCLevelOutOfRange", 210),
          ("excTCLevelOverflow", 211),
          ("excInputFail3", 212),
          ("excInputWarning", 213),
          ("excEchoWarning", 214),
          ("xlxInputStepProtection", 215),
          ("excExt1PPSReference", 220),
          ("excInt1PPSReference", 221),
          ("exc5MHzReference", 222),
          ("exc10MHzReference", 223),
          ("excPrecorrectionSetupInfo", 230),
          ("excPrecorrectionSetupFail", 231),
          ("excFramecounter", 240),
          ("excMissingIIP", 241),
          ("excPSUOvertemp", 250),
          ("excPowerSupplyWarning", 251),
          ("excNSUConnected", 256),
          ("excMonHWError", 260),
          ("excRecvRxAUXHWError", 261),
          ("excRecvHWError", 262),
          ("excMonNoFrontendLock", 263),
          ("excRecvAUXNoFrontendLock", 264),
          ("excRecvNoFrontendLock", 265),
          ("excMonBadInputSignal", 266),
          ("excRecvAUXBadInputSignal", 267),
          ("excRecvBadInputSignal", 268),
          ("excMonNoInputSignal", 269),
          ("excRecvAUXWarningInputSignal", 270),
          ("excRecvWarningInputSignal", 271),
          ("excMonAUXHWError", 272),
          ("excMonAUXNoFrontendLock", 273),
          ("excMonAUXBadInputSignal", 274),
          ("excMonitorNoInputFail", 280),
          ("excNoSfnData", 300),
          ("excNoMobileDtvContent", 301),
          ("excInput1Available", 320),
          ("excInput2Available", 321),
          ("excInput1LPAvailable", 322),
          ("excInput2LPAvailable", 323),
          ("excRfTest", 400),
          ("excPRBSInsertion", 401),
          ("excTestEnsemble", 402),
          ("excInvalidTII", 403),
          ("excTIITransmission", 404),
          ("excTxModeChange", 405),
          ("excTIIChange", 406),
          ("excNullTIST", 407),
          ("excTISTJitter", 408),
          ("excTS1FrameLock", 409),
          ("excTS2FrameLock", 410),
          ("excCrcViolationRateTooHigh", 411),
          ("excSeamlessReady", 412),
          ("excTestFIC", 413),
          ("dvbt2NoL1Present", 500),
          ("dvbt2InvalidConfiguration", 501),
          ("dvbT2UnsupportedConfiguration", 502),
          ("dvbt2BandwidthMismatch", 503),
          ("iqHeader1Integrity", 550),
          ("iqHeader2Integrity", 551),
          ("iqHeader1Issues", 552),
          ("iqHeader2Issues", 553),
          ("iqInputRegulation", 554),
          ("iqWrongConfiguration", 555),
          ("iqTseMute", 556),
          ("iqInputOrder", 557),
          ("sx801PowerFail7Vpositive", 600),
          ("sx801PowerFail7Vnegative", 601),
          ("sx801PowerFail12V", 602),
          ("preAmpTemperatureFault", 603),
          ("preAmpRFFault", 604),
          ("parIoExcLink", 605),
          ("parIoTxLink", 606),
          ("parIoGpIoLink", 607),
          ("rfBoardRFFault", 608),
          ("sx801PhaseError", 640),
          ("sx801ReflectionWarning", 641),
          ("sx801ReflectionFault", 642),
          ("sx801RfWarning", 643),
          ("sx801AmplShutdown", 644),
          ("sx801PA1Supply1TooHot", 650),
          ("sx801PA1Supply2TooHot", 651),
          ("sx801PA1ReserveSupplyTooHot", 652),
          ("sx801PA1Supply1Fail", 653),
          ("sx801PA1Supply2Fail", 654),
          ("sx801PA1ReserveSupplyFail", 655),
          ("sx801PA1AcFail", 656),
          ("sx801PA1BlowerFail", 657),
          ("sx801PA1TransistorFail", 658),
          ("sx801PA1DriverFail", 659),
          ("sx801PA1RfInFail", 660),
          ("sx801PA1Reflection", 661),
          ("sx801PA1VSWR", 662),
          ("sx801PA1PowerFail", 663),
          ("sx801PA1Regulation", 664),
          ("sx801PA1Temperature", 665),
          ("sx801PA1Communication", 666),
          ("sx801PA1Update", 667),
          ("sx801PA2Supply1TooHot", 675),
          ("sx801PA2Supply2TooHot", 676),
          ("sx801PA2ReserveSupplyTooHot", 677),
          ("sx801PA2Supply1Fail", 678),
          ("sx801PA2Supply2Fail", 679),
          ("sx801PA2ReserveSupplyFail", 680),
          ("sx801PA2AcFail", 681),
          ("sx801PA2BlowerFail", 682),
          ("sx801PA2TransistorFail", 683),
          ("sx801PA2DriverFail", 684),
          ("sx801PA2RfInFail", 685),
          ("sx801PA2Reflection", 686),
          ("sx801PA2VSWR", 687),
          ("sx801PA2PowerFail", 688),
          ("sx801PA2Regulation", 689),
          ("sx801PA2Temperature", 690),
          ("sx801PA2Communication", 691),
          ("sx801PA2Update", 692),
          ("pa3Supply1TooHot", 700),
          ("pa3Supply2TooHot", 701),
          ("pa3ReserveSupplyTooHot", 702),
          ("pa3Supply1Fault", 703),
          ("pa3Supply2Fault", 704),
          ("pa3ReserveSupplyFault", 705),
          ("pa3ACFault", 706),
          ("pa3BlowerFault", 707),
          ("pa3TransistorFault", 708),
          ("pa3DriverFault", 709),
          ("pa3RFinFault", 710),
          ("pa3Reflection", 711),
          ("pa3VSWR", 712),
          ("pa3PowerFault", 713),
          ("pa3Regulation", 714),
          ("pa3Temperature", 715),
          ("pa3Communication", 716),
          ("pa3Update", 717),
          ("pa4Supply1TooHot", 725),
          ("pa4Supply2TooHot", 726),
          ("pa4ReserveSupplyTooHot", 727),
          ("pa4Supply1Fault", 728),
          ("pa4Supply2Fault", 729),
          ("pa4ReserveSupplyFault", 730),
          ("pa4ACFault", 731),
          ("pa4BlowerFault", 732),
          ("pa4TransistorFault", 733),
          ("pa4DriverFault", 734),
          ("pa4RFinFault", 735),
          ("pa4Reflection", 736),
          ("pa4VSWR", 737),
          ("pa4PowerFault", 738),
          ("pa4Regulation", 739),
          ("pa4Temperature", 740),
          ("pa4Communication", 741),
          ("pa4Update", 742),
          ("tse800NoConnect", 770),
          ("tse800Warning", 771),
          ("tse800Fault", 772),
          ("automaticOn", 800),
          ("automaticFault", 801),
          ("autoCtrlExcActive", 802),
          ("autoPrgmExcActive", 803),
          ("changeoverByUser", 804),
          ("changeoverByAuto", 805),
          ("automaticReady", 806),
          ("autoPrgmExcNoConnect", 807),
          ("autoPrgmExcFault", 808))
    )



class LogbookEntryMessagesExcDVB(TextualConvention, Integer32):
    status = "obsolete"
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
              12,
              13,
              16,
              17,
              18,
              19,
              20,
              21,
              23,
              25,
              26,
              28,
              30,
              37,
              38,
              40,
              41,
              42,
              43,
              44,
              45,
              100,
              101,
              102,
              103,
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
              127)
        )
    )
    namedValues = NamedValues(
        *(("excReboot", 0),
          ("excSummaryFault", 1),
          ("excSummaryWarning", 2),
          ("excLocal", 3),
          ("excOn", 4),
          ("excRfOk", 5),
          ("excNoInput", 6),
          ("excReferenceFail", 7),
          ("excRfOn", 8),
          ("excMute", 9),
          ("excFanWarning", 12),
          ("excNoCommunicationToNetCCU", 13),
          ("excPowerSupply", 16),
          ("excBoardTemperature", 17),
          ("excFanFault", 18),
          ("excSelfTest", 19),
          ("excHwCfCard", 20),
          ("excOutputOpen", 21),
          ("excHwEeprom", 23),
          ("excRfFail", 25),
          ("excLoop", 26),
          ("excCarrierLock", 28),
          ("excInputFault", 30),
          ("excOptionExpired", 37),
          ("excOptionExpires", 38),
          ("excHwFpgaConfig", 40),
          ("excHwIifBoard", 41),
          ("excHwRfBoard", 42),
          ("excHwSynth1", 43),
          ("excHwSynth2", 44),
          ("excHwSynth3", 45),
          ("excTestMode", 100),
          ("excExtRefFail", 101),
          ("excExtRefWeak", 102),
          ("excExtPPSFail", 103),
          ("excWrongConfig", 104),
          ("excInputFail", 105),
          ("excWrongDatarate", 106),
          ("excFifoWarning", 107),
          ("excExtDelayChanged", 108),
          ("excWrongDelay", 109),
          ("excNoMIP", 110),
          ("excWrongMFArrivalTime", 111),
          ("excExtPPSAsynchron", 112),
          ("excPacketUnlock", 113),
          ("excMaxDelayChanged", 114),
          ("excNoReference", 115),
          ("excNoPPS", 116),
          ("excRfFailAmplifier", 117),
          ("excWarningAmplifier", 118),
          ("excOverflowAmplifier", 119),
          ("excSynthUnlock", 127))
    )



class LogbookEntryMessagesExcFM(TextualConvention, Integer32):
    status = "current"
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
              13,
              15,
              16,
              21,
              23,
              25,
              26,
              27,
              28,
              30,
              32,
              33,
              34,
              36,
              37,
              38,
              41,
              42,
              43,
              47,
              48,
              49,
              50,
              51,
              67,
              71,
              81,
              84,
              85,
              86,
              87,
              88,
              89,
              90,
              91,
              92,
              93,
              94,
              95,
              97,
              98,
              99,
              100,
              101,
              102,
              103,
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
              125)
        )
    )
    namedValues = NamedValues(
        *(("excReboot", 0),
          ("excSummaryFault", 1),
          ("excSummaryWarning", 2),
          ("excLocal", 3),
          ("excOn", 4),
          ("excRfOk", 5),
          ("excNoInput", 6),
          ("excReferenceFail", 7),
          ("excRfOn", 8),
          ("excMute", 9),
          ("excNoCommunicationToNetCCU", 13),
          ("excBiosUpdated", 15),
          ("excPowerSupply", 16),
          ("excOutputOpen", 21),
          ("excEEPROMError", 23),
          ("excRfFail", 25),
          ("excLoop", 26),
          ("excFPGANotLoaded", 27),
          ("excCarrierLock", 28),
          ("excInputFault", 30),
          ("ostSummaryFault", 32),
          ("excSoftFault", 33),
          ("ostSoftFault", 34),
          ("ostSummaryWarning", 36),
          ("excOptionKeyExpired", 37),
          ("excOptionKeyWarning", 38),
          ("excTemperatureWarning", 41),
          ("excTemperatureFault", 42),
          ("excRfUnitFault", 43),
          ("excFan1NotOk", 47),
          ("excFan2NotOk", 48),
          ("excMainPLLUnlocked", 49),
          ("excMainUPCUnlocked", 50),
          ("excMainCLKUnlocked", 51),
          ("exc12VFanWarning", 67),
          ("exc12VRackControllerWarning", 71),
          ("excInfoFrequencyChanged", 81),
          ("excLevelAESLeftTooLow", 84),
          ("excLevelAESRightTooLow", 85),
          ("excLevelMPXTooLow", 86),
          ("excNoDataInput", 87),
          ("excLevelAFLeftTooLow", 88),
          ("excLevelAFRightTooLow", 89),
          ("excLevelAUX1TooLow", 90),
          ("excLevelAUX2TooLow", 91),
          ("excLevelAUX3TooLow", 92),
          ("excLevelAESLeftTooHigh", 93),
          ("excLevelAESRightTooHigh", 94),
          ("excLevelMPXTooHigh", 95),
          ("excLevelAFLeftTooHigh", 97),
          ("excLevelAFRightTooHigh", 98),
          ("excLevelAUX1TooHigh", 99),
          ("excLevelAUX2TooHigh", 100),
          ("excLevelAUX3TooHigh", 101),
          ("excAESNoClock", 102),
          ("excAESParityBiphaseError", 103),
          ("excAESStateNotValid", 104),
          ("excInpCh1NotOk", 105),
          ("excInpCh2NotOk", 106),
          ("excInpCh1Active", 107),
          ("excInpCh2Active", 108),
          ("excInpAutomaticActive", 109),
          ("recSummaryWarning", 110),
          ("recSummaryFault", 111),
          ("ostRfPresent", 112),
          ("recRfWarning", 113),
          ("recCarrierNotPresent", 114),
          ("recNoConnection", 115),
          ("ostRfWarn", 116),
          ("ostRfFault", 117),
          ("ostNoInput", 118),
          ("recRfFault", 119),
          ("recRfPresent", 120),
          ("ostPowerRegulationActive", 121),
          ("ostTemperatureWarning", 122),
          ("ostSwrWarning", 123),
          ("ostSwrFault", 124),
          ("ostNoConnection", 125))
    )



class LogbookEntryMessagesOST(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(42,
              43,
              44,
              45,
              46,
              47,
              48,
              49,
              50,
              51,
              52,
              53,
              54,
              58,
              59,
              60,
              61,
              62,
              63,
              64,
              65,
              66,
              67,
              68,
              69,
              70,
              71,
              72,
              73,
              76,
              77,
              78,
              79,
              80,
              81,
              82,
              83,
              84,
              85,
              86,
              87,
              88,
              89,
              90,
              91,
              92,
              93,
              94,
              95,
              96,
              97,
              98,
              99,
              100,
              101,
              102,
              103,
              104,
              105,
              106,
              107,
              108,
              109,
              110,
              111,
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
              129)
        )
    )
    namedValues = NamedValues(
        *(("ostRfOn", 42),
          ("ostRfOk", 43),
          ("ostRfReduced", 44),
          ("ostNoInput", 45),
          ("ostRfWarning", 46),
          ("ostReflectionWarning", 47),
          ("ostRackWarning", 48),
          ("ostCoolingWarning", 49),
          ("ostRfFail", 50),
          ("ostReflectionFault", 51),
          ("ostACFault", 52),
          ("ostCoolingFault", 53),
          ("ostCommunicationFault", 54),
          ("rackLinkOk", 58),
          ("rackOn", 59),
          ("reducedRfExcA", 60),
          ("reducedRfExcB", 61),
          ("rackGpiWarning", 62),
          ("rackFan1Fault", 63),
          ("rackFan2Fault", 64),
          ("rackCoolingSumWarning", 65),
          ("rackAmplifierSumFault", 66),
          ("rackGpiFault", 67),
          ("rackTemperatureFault", 68),
          ("rackACFault", 69),
          ("rackCoolingSumFault", 70),
          ("rackTempFaultAbs1", 71),
          ("rackTempFaultAbs2", 72),
          ("rackDCFault", 73),
          ("ampNumberDiffers", 76),
          ("ampOn", 77),
          ("ampDCOk", 78),
          ("ampACOk", 79),
          ("ampRfInFail", 80),
          ("ampRfFail", 81),
          ("ampReflectionFault", 82),
          ("ampTemperatureFault", 83),
          ("ampFanFault", 84),
          ("ampTransistorFault", 85),
          ("pucFault", 86),
          ("pucWarning", 87),
          ("pucLink", 88),
          ("pucFan1Link", 89),
          ("pucFan2Link", 90),
          ("pucFan3Link", 91),
          ("pucFan4Link", 92),
          ("pucPump1Link", 93),
          ("pucPump2Link", 94),
          ("pucOn", 95),
          ("pucFan1", 96),
          ("pucFan2", 97),
          ("pucFan3", 98),
          ("pucFan4", 99),
          ("pucPump1", 100),
          ("pucPump2", 101),
          ("pucPressure", 102),
          ("pucMaintenance", 103),
          ("pucConfig", 104),
          ("pucFan1Fault", 105),
          ("pucFan2Fault", 106),
          ("pucFan3Fault", 107),
          ("pucFan4Fault", 108),
          ("pucPump1Fault", 109),
          ("pucPump2Fault", 110),
          ("pucPressureFault", 111),
          ("pucFilter", 117),
          ("pucPuOff", 118),
          ("rackProbeNotCalibrated", 119),
          ("rackTemperatureWarning", 120),
          ("rackSumFault", 121),
          ("rackAbsorberFault", 122),
          ("rackOvervoltageProtection", 123),
          ("psu1Fault", 124),
          ("psu2Fault", 125),
          ("psuRFault", 126),
          ("ampDriverFault", 127),
          ("ctxPowerFault", 128),
          ("ampRegulationFault", 129))
    )



class LogbookEntryMessagesNSU(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(3,
              5,
              6,
              7,
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
              28,
              29,
              30,
              31,
              32,
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
              50,
              51,
              52,
              53,
              54,
              55,
              56,
              57,
              58,
              59,
              60,
              61,
              62,
              63,
              64,
              65,
              66,
              67,
              68,
              69,
              70,
              80,
              81,
              82,
              83,
              84,
              85,
              86,
              87,
              88,
              89,
              90,
              91,
              92,
              93,
              94,
              95,
              96,
              97,
              98,
              99,
              100,
              101,
              102,
              103,
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
              122,
              123,
              124,
              196,
              197,
              198,
              200,
              201,
              226)
        )
    )
    namedValues = NamedValues(
        *(("local", 3),
          ("automaticOn", 5),
          ("automaticReady", 6),
          ("automaticChangeover", 7),
          ("swBackupStarted", 10),
          ("program1RfOn", 11),
          ("program2RfOn", 12),
          ("program3RfOn", 13),
          ("program4RfOn", 14),
          ("program5RfOn", 15),
          ("program6RfOn", 16),
          ("program7RfOn", 17),
          ("program8RfOn", 18),
          ("programReserveRfOn", 19),
          ("swBackupDone", 20),
          ("txA1ToDummyLoad", 21),
          ("txA2ToDummyLoad", 22),
          ("txA3ToDummyLoad", 23),
          ("txA4ToDummyLoad", 24),
          ("txA5ToDummyLoad", 25),
          ("txA6ToDummyLoad", 26),
          ("txA7ToDummyLoad", 27),
          ("txA8ToDummyLoad", 28),
          ("txBToDummyLoad", 29),
          ("optionkeyExpired", 30),
          ("txA1Local", 31),
          ("txA2Local", 32),
          ("txA3Local", 33),
          ("txA4Local", 34),
          ("txA5Local", 35),
          ("txA6Local", 36),
          ("txA7Local", 37),
          ("txA8Local", 38),
          ("txBLocal", 39),
          ("reboot", 40),
          ("txA1SumWarning", 41),
          ("txA2SumWarning", 42),
          ("txA3SumWarning", 43),
          ("txA4SumWarning", 44),
          ("txA5SumWarning", 45),
          ("txA6SumWarning", 46),
          ("txA7SumWarning", 47),
          ("txA8SumWarning", 48),
          ("txBSumWarning", 49),
          ("swBackupFailed", 50),
          ("txA1NoConnect", 51),
          ("txA2NoConnect", 52),
          ("txA3NoConnect", 53),
          ("txA4NoConnect", 54),
          ("txA5NoConnect", 55),
          ("txA6NoConnect", 56),
          ("txA7NoConnect", 57),
          ("txA8NoConnect", 58),
          ("txBNoConnect", 59),
          ("swRestoreStarted", 60),
          ("txA1SumFault", 61),
          ("txA2SumFault", 62),
          ("txA3SumFault", 63),
          ("txA4SumFault", 64),
          ("txA5SumFault", 65),
          ("txA6SumFault", 66),
          ("txA7SumFault", 67),
          ("txA8SumFault", 68),
          ("txBSumFault", 69),
          ("swRestoreDone", 70),
          ("swRestoreFailed", 80),
          ("connBoardTxA1Updating", 81),
          ("connBoardTxA2Updating", 82),
          ("connBoardTxA3Updating", 83),
          ("connBoardTxA4Updating", 84),
          ("connBoardTxA5Updating", 85),
          ("connBoardTxA6Updating", 86),
          ("connBoardTxA7Updating", 87),
          ("connBoardTxA8Updating", 88),
          ("connBoardTxBUpdating", 89),
          ("inputSwitchUpdating", 90),
          ("connBoardTxA1SumWarning", 91),
          ("connBoardTxA2SumWarning", 92),
          ("connBoardTxA3SumWarning", 93),
          ("connBoardTxA4SumWarning", 94),
          ("connBoardTxA5SumWarning", 95),
          ("connBoardTxA6SumWarning", 96),
          ("connBoardTxA7SumWarning", 97),
          ("connBoardTxA8SumWarning", 98),
          ("connBoardTxBSumWarning", 99),
          ("inputSwitchSumWarning", 100),
          ("fanFault", 101),
          ("sumWngRCV", 102),
          ("rcvNoConnect", 103),
          ("sumFltRCV", 104),
          ("optionkeyWillExpire", 105),
          ("powerSupply", 106),
          ("boardTemperature", 107),
          ("automaticFault", 108),
          ("rcvNoConnectx", 109),
          ("sumFltRCVx", 110),
          ("connBoardTxA1SumFault", 111),
          ("connBoardTxA2SumFault", 112),
          ("connBoardTxA3SumFault", 113),
          ("connBoardTxA4SumFault", 114),
          ("connBoardTxA5SumFault", 115),
          ("connBoardTxA6SumFault", 116),
          ("connBoardTxA7SumFault", 117),
          ("connBoardTxA8SumFault", 118),
          ("connBoardTxBSumFault", 119),
          ("inputSwitchSumFault", 120),
          ("outputSwitch", 122),
          ("inputSwitchChangeOver", 123),
          ("txBParameterSet", 124),
          ("antennaRedundancySumWarning", 196),
          ("tcbTxBPowerSupply", 197),
          ("txBPosition", 198),
          ("intPwrSupply", 200),
          ("extPwrSupply", 201),
          ("antennaRedundancySumFault", 226))
    )



class LogbookEntryMessagesXV703(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              7,
              8,
              9,
              10,
              11,
              12,
              14,
              15,
              16,
              17,
              18,
              19,
              20,
              21,
              22)
        )
    )
    namedValues = NamedValues(
        *(("noNetCCUConnection", 0),
          ("summaryFault", 1),
          ("summaryWarning", 2),
          ("local", 3),
          ("on", 4),
          ("ok", 5),
          ("fanWarning", 7),
          ("rfOn", 8),
          ("updatedBIOS", 9),
          ("powerSupply", 10),
          ("boardTemperature", 11),
          ("fanFault", 12),
          ("reboot", 14),
          ("loopOpen", 15),
          ("noConnection", 16),
          ("ampFail", 17),
          ("ifrPllFail", 18),
          ("rfiPllFail", 19),
          ("refFreqFail", 20),
          ("pInFail", 21),
          ("rfFail", 22))
    )



class LogbookEntrySlope(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("set", 1),
          ("reset", 2))
    )



class LogbookMaxEntryNumber(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )



class IndexTransmitter(TextualConvention, Integer32):
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
        *(("transmitterB", 1),
          ("transmitterA1", 2),
          ("transmitterA2", 3),
          ("transmitterA3", 4),
          ("transmitterA4", 5),
          ("transmitterA5", 6),
          ("transmitterA6", 7),
          ("transmitterA7", 8),
          ("transmitterA8", 9))
    )



class IndexRack(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )



class IndexAmplifier(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )



class IndexProgram(TextualConvention, Integer32):
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
        *(("programRes", 1),
          ("program1", 2),
          ("program2", 3),
          ("program3", 4),
          ("program4", 5),
          ("program5", 6),
          ("program6", 7),
          ("program7", 8),
          ("program8", 9))
    )



class IndexAB(TextualConvention, Integer32):
    status = "current"
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



class ProdInfoModuleNameTv(TextualConvention, Integer32):
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
              50,
              100,
              101)
        )
    )
    namedValues = NamedValues(
        *(("exciter", 1),
          ("exciterMainboard", 2),
          ("exciterInputInterface", 3),
          ("exciterRfBoard", 4),
          ("exciterSynth1", 5),
          ("exciterSynth2", 6),
          ("exciterSynth3", 7),
          ("netCCU", 50),
          ("rackcontroller", 100),
          ("amplifier", 101))
    )



class ProdInfoModuleNameFm(TextualConvention, Integer32):
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
              50,
              100,
              101)
        )
    )
    namedValues = NamedValues(
        *(("exciter", 1),
          ("exciterMainboard", 2),
          ("exciterBootprog", 3),
          ("exciterBootload", 4),
          ("exciterOs", 5),
          ("exciterFpga", 6),
          ("netCCU", 50),
          ("rackcontroller", 100),
          ("amplifier", 101))
    )



class ProdInfoModuleNameNsu(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            70
        )
    )
    namedValues = NamedValues(
        ("tcBoard", 70)
    )



class LogbookEntryMessagesExcATV(TextualConvention, Integer32):
    status = "obsolete"
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
              23,
              25,
              26,
              27,
              28,
              30,
              37,
              38,
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
              50,
              51,
              52,
              53,
              54,
              55,
              56,
              57,
              58,
              59,
              60,
              61,
              62,
              63,
              64,
              65,
              66,
              67,
              68,
              69,
              70,
              71,
              72,
              73,
              74,
              75,
              76,
              77,
              78,
              100,
              101,
              102,
              103,
              104,
              106,
              107,
              108,
              109,
              110,
              111,
              113,
              114,
              115,
              116,
              117,
              118,
              119,
              127)
        )
    )
    namedValues = NamedValues(
        *(("reboot", 0),
          ("summaryFault", 1),
          ("summaryWarning", 2),
          ("local", 3),
          ("exciterOn", 4),
          ("rfOk", 5),
          ("noInput", 6),
          ("reference", 7),
          ("rfOn", 8),
          ("mute", 9),
          ("relieveReq", 10),
          ("oneFan", 12),
          ("noCcuComm", 13),
          ("swUpdated", 14),
          ("biosUpdated", 15),
          ("powerSupply", 16),
          ("temperature", 17),
          ("fans", 18),
          ("hwMainboard", 19),
          ("hwCfCard", 20),
          ("outputOpen", 21),
          ("hwEEPROM", 23),
          ("rfFail", 25),
          ("loopOpen", 26),
          ("noFPGA", 27),
          ("carrierLock", 28),
          ("inputFail", 30),
          ("optionExpired", 37),
          ("optionWillEnd", 38),
          ("fpgaConfig", 40),
          ("hwIifBoard", 41),
          ("hwRfBoard", 42),
          ("hwSynth1", 43),
          ("hwSynth2", 44),
          ("hwSynth3", 45),
          ("muteAudio1", 46),
          ("muteAudio2", 47),
          ("videoInput1", 48),
          ("videoInput2", 49),
          ("videoInputAct", 50),
          ("rfOutExcV", 51),
          ("rfOutAntV", 52),
          ("rfOutExcA1", 53),
          ("rfOutAntA1", 54),
          ("rfOutExcA2", 55),
          ("rfOutAntA2", 56),
          ("clippingAntennaInput", 57),
          ("noHeadroomAntenna", 58),
          ("audioMode", 59),
          ("whiteLine", 60),
          ("whiteLineLnAmp", 61),
          ("whiteLineLnAmpW", 62),
          ("syncCheck", 63),
          ("whiteLimiter", 64),
          ("devLimAud1", 65),
          ("devLimAud2", 66),
          ("videoInputClipping", 67),
          ("aud1InpClip", 68),
          ("aud2InpClip", 69),
          ("nicam728Data", 70),
          ("nicam728Carr", 71),
          ("aud2OutClip", 72),
          ("rfMonFail", 73),
          ("rfVideoFail", 74),
          ("rfAudio1Fail", 75),
          ("rfAudio2Fail", 76),
          ("audioLoopOpen", 77),
          ("videoLoopOpen", 78),
          ("testMode", 100),
          ("extRefFail", 101),
          ("extRefWeak", 102),
          ("extPpsFail", 103),
          ("wrongConfig", 104),
          ("wrongDatarate", 106),
          ("fifoOverUnderFlow", 107),
          ("delayChanged", 108),
          ("wrongDelay", 109),
          ("noMIP", 110),
          ("wrongMfArrivalTime", 111),
          ("packetUnlock", 113),
          ("maxDelayChanged", 114),
          ("referenceAbsent", 115),
          ("noPPS", 116),
          ("rfFailAmplifier", 117),
          ("warningAmplifier", 118),
          ("amplifierOverflow", 119),
          ("synthesizerUnlocked", 127))
    )



class LockState(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("locked", 1),
          ("unlocked", 2))
    )



class EqualizerCalibrationState(TextualConvention, Integer32):
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
        *(("inactive", 1),
          ("active", 2),
          ("warning", 3),
          ("fail", 4))
    )



class TvStandard(TextualConvention, Integer32):
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
              9,
              100)
        )
    )
    namedValues = NamedValues(
        *(("atv", 1),
          ("dvb", 2),
          ("atsc", 3),
          ("dtmb", 4),
          ("mediaFLO", 5),
          ("test", 6),
          ("dab", 7),
          ("isdbt", 8),
          ("dvbt2", 9),
          ("inconsistent", 100))
    )



class AtvStandard(TextualConvention, Integer32):
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
              9,
              10,
              11,
              12,
              13)
        )
    )
    namedValues = NamedValues(
        *(("bg", 1),
          ("m", 2),
          ("m1", 3),
          ("n", 4),
          ("dk", 5),
          ("i", 6),
          ("i1", 7),
          ("dkfm2", 8),
          ("l", 9),
          ("k1", 10),
          ("h", 11),
          ("b", 12),
          ("g", 13))
    )



class InputSource(TextualConvention, Integer32):
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
        *(("bnc", 1),
          ("rx", 2),
          ("sat", 3),
          ("ip", 4),
          ("reserved", 5),
          ("tp", 6),
          ("vf", 7),
          ("t2Mi", 8),
          ("iq", 9))
    )



class Sx801AmplifierState(TextualConvention, Integer32):
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
        *(("off", 1),
          ("warning", 2),
          ("ok", 3),
          ("unknown", 4))
    )



class FailDelayMode(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("always", 1),
          ("ifQualified", 2))
    )



class FailDelayStatus(TextualConvention, Integer32):
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
        *(("off", 1),
          ("warning", 2),
          ("ok", 3))
    )



# MIB Managed Objects in the order of their OIDs

_RsXx8000_ObjectIdentity = ObjectIdentity
rsXx8000 = _RsXx8000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167)
)
if mibBuilder.loadTexts:
    rsXx8000.setStatus("current")
_RsXx8000Common_ObjectIdentity = ObjectIdentity
rsXx8000Common = _RsXx8000Common_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 1)
)
if mibBuilder.loadTexts:
    rsXx8000Common.setStatus("current")
_RsXx8000CommonObjs_ObjectIdentity = ObjectIdentity
rsXx8000CommonObjs = _RsXx8000CommonObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 1, 1)
)
_ProductInformation_ObjectIdentity = ObjectIdentity
productInformation = _ProductInformation_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 1, 1, 1)
)
_SerialNumber_Type = ReadableString
_SerialNumber_Object = MibScalar
serialNumber = _SerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 1, 1, 1, 2),
    _SerialNumber_Type()
)
serialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serialNumber.setStatus("current")
_IdentNumberSW_Type = ReadableString
_IdentNumberSW_Object = MibScalar
identNumberSW = _IdentNumberSW_Object(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 1, 1, 1, 3),
    _IdentNumberSW_Type()
)
identNumberSW.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    identNumberSW.setStatus("current")
_VersionNumberSW_Type = ReadableString
_VersionNumberSW_Object = MibScalar
versionNumberSW = _VersionNumberSW_Object(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 1, 1, 1, 4),
    _VersionNumberSW_Type()
)
versionNumberSW.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    versionNumberSW.setStatus("current")
_IdentNumberHW_Type = ReadableString
_IdentNumberHW_Object = MibScalar
identNumberHW = _IdentNumberHW_Object(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 1, 1, 1, 5),
    _IdentNumberHW_Type()
)
identNumberHW.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    identNumberHW.setStatus("current")
_VersionNumberHW_Type = ReadableString
_VersionNumberHW_Object = MibScalar
versionNumberHW = _VersionNumberHW_Object(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 1, 1, 1, 6),
    _VersionNumberHW_Type()
)
versionNumberHW.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    versionNumberHW.setStatus("current")
_SnmpConfig_ObjectIdentity = ObjectIdentity
snmpConfig = _SnmpConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 1, 1, 2)
)
_TrapSinkTable_Object = MibTable
trapSinkTable = _TrapSinkTable_Object(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 1, 1, 2, 2)
)
if mibBuilder.loadTexts:
    trapSinkTable.setStatus("current")
_TrapSinkEntry_Object = MibTableRow
trapSinkEntry = _TrapSinkEntry_Object(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 1, 1, 2, 2, 1)
)
trapSinkEntry.setIndexNames(
    (0, "RS-XX8000-COMMON-MIB", "trapSinkNumber"),
)
if mibBuilder.loadTexts:
    trapSinkEntry.setStatus("current")


class _TrapSinkNumber_Type(Integer32):
    """Custom type trapSinkNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_TrapSinkNumber_Type.__name__ = "Integer32"
_TrapSinkNumber_Object = MibTableColumn
trapSinkNumber = _TrapSinkNumber_Object(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 1, 1, 2, 2, 1, 1),
    _TrapSinkNumber_Type()
)
trapSinkNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    trapSinkNumber.setStatus("current")


class _TrapSinkVersion_Type(Integer32):
    """Custom type trapSinkVersion based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("v1Trap", 1),
          ("v2Trap", 2),
          ("v2Inform", 3))
    )


_TrapSinkVersion_Type.__name__ = "Integer32"
_TrapSinkVersion_Object = MibTableColumn
trapSinkVersion = _TrapSinkVersion_Object(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 1, 1, 2, 2, 1, 2),
    _TrapSinkVersion_Type()
)
trapSinkVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trapSinkVersion.setStatus("current")
_TrapSinkAddress_Type = IpAddress
_TrapSinkAddress_Object = MibTableColumn
trapSinkAddress = _TrapSinkAddress_Object(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 1, 1, 2, 2, 1, 3),
    _TrapSinkAddress_Type()
)
trapSinkAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trapSinkAddress.setStatus("current")


class _TrapSinkPort_Type(Integer32):
    """Custom type trapSinkPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_TrapSinkPort_Type.__name__ = "Integer32"
_TrapSinkPort_Object = MibTableColumn
trapSinkPort = _TrapSinkPort_Object(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 1, 1, 2, 2, 1, 4),
    _TrapSinkPort_Type()
)
trapSinkPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trapSinkPort.setStatus("current")
_TrapSinkCommunity_Type = ReadableString
_TrapSinkCommunity_Object = MibTableColumn
trapSinkCommunity = _TrapSinkCommunity_Object(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 1, 1, 2, 2, 1, 5),
    _TrapSinkCommunity_Type()
)
trapSinkCommunity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trapSinkCommunity.setStatus("current")


class _TrapSinkInformRetry_Type(Integer32):
    """Custom type trapSinkInformRetry based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_TrapSinkInformRetry_Type.__name__ = "Integer32"
_TrapSinkInformRetry_Object = MibTableColumn
trapSinkInformRetry = _TrapSinkInformRetry_Object(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 1, 1, 2, 2, 1, 6),
    _TrapSinkInformRetry_Type()
)
trapSinkInformRetry.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trapSinkInformRetry.setStatus("current")


class _TrapSinkInformTimeout_Type(Integer32):
    """Custom type trapSinkInformTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_TrapSinkInformTimeout_Type.__name__ = "Integer32"
_TrapSinkInformTimeout_Object = MibTableColumn
trapSinkInformTimeout = _TrapSinkInformTimeout_Object(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 1, 1, 2, 2, 1, 7),
    _TrapSinkInformTimeout_Type()
)
trapSinkInformTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trapSinkInformTimeout.setStatus("current")
if mibBuilder.loadTexts:
    trapSinkInformTimeout.setUnits("seconds")


class _TrapSinkInformUnacknowledged_Type(Integer32):
    """Custom type trapSinkInformUnacknowledged based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_TrapSinkInformUnacknowledged_Type.__name__ = "Integer32"
_TrapSinkInformUnacknowledged_Object = MibTableColumn
trapSinkInformUnacknowledged = _TrapSinkInformUnacknowledged_Object(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 1, 1, 2, 2, 1, 8),
    _TrapSinkInformUnacknowledged_Type()
)
trapSinkInformUnacknowledged.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trapSinkInformUnacknowledged.setStatus("obsolete")
_TrapSinkUse_Type = TruthValue
_TrapSinkUse_Object = MibTableColumn
trapSinkUse = _TrapSinkUse_Object(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 1, 1, 2, 2, 1, 9),
    _TrapSinkUse_Type()
)
trapSinkUse.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trapSinkUse.setStatus("current")
_SendTestTrap_Type = Trigger
_SendTestTrap_Object = MibScalar
sendTestTrap = _SendTestTrap_Object(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 1, 1, 2, 3),
    _SendTestTrap_Type()
)
sendTestTrap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sendTestTrap.setStatus("current")
_IrtTrapsAllOn_Type = Trigger
_IrtTrapsAllOn_Object = MibScalar
irtTrapsAllOn = _IrtTrapsAllOn_Object(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 1, 1, 2, 4),
    _IrtTrapsAllOn_Type()
)
irtTrapsAllOn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    irtTrapsAllOn.setStatus("current")
_IrtTrapsAllOff_Type = Trigger
_IrtTrapsAllOff_Object = MibScalar
irtTrapsAllOff = _IrtTrapsAllOff_Object(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 1, 1, 2, 5),
    _IrtTrapsAllOff_Type()
)
irtTrapsAllOff.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    irtTrapsAllOff.setStatus("current")
_RsTrapsAllOn_Type = Trigger
_RsTrapsAllOn_Object = MibScalar
rsTrapsAllOn = _RsTrapsAllOn_Object(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 1, 1, 2, 6),
    _RsTrapsAllOn_Type()
)
rsTrapsAllOn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsTrapsAllOn.setStatus("current")
_RsTrapsAllOff_Type = Trigger
_RsTrapsAllOff_Object = MibScalar
rsTrapsAllOff = _RsTrapsAllOff_Object(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 1, 1, 2, 7),
    _RsTrapsAllOff_Type()
)
rsTrapsAllOff.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsTrapsAllOff.setStatus("current")
_RsTrapsAllFaultsOn_Type = Trigger
_RsTrapsAllFaultsOn_Object = MibScalar
rsTrapsAllFaultsOn = _RsTrapsAllFaultsOn_Object(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 1, 1, 2, 8),
    _RsTrapsAllFaultsOn_Type()
)
rsTrapsAllFaultsOn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsTrapsAllFaultsOn.setStatus("current")
_RsTrapsAllFaultsOff_Type = Trigger
_RsTrapsAllFaultsOff_Object = MibScalar
rsTrapsAllFaultsOff = _RsTrapsAllFaultsOff_Object(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 1, 1, 2, 9),
    _RsTrapsAllFaultsOff_Type()
)
rsTrapsAllFaultsOff.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsTrapsAllFaultsOff.setStatus("current")
_RsTrapsAllWarningsOn_Type = Trigger
_RsTrapsAllWarningsOn_Object = MibScalar
rsTrapsAllWarningsOn = _RsTrapsAllWarningsOn_Object(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 1, 1, 2, 10),
    _RsTrapsAllWarningsOn_Type()
)
rsTrapsAllWarningsOn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsTrapsAllWarningsOn.setStatus("current")
_RsTrapsAllWarningsOff_Type = Trigger
_RsTrapsAllWarningsOff_Object = MibScalar
rsTrapsAllWarningsOff = _RsTrapsAllWarningsOff_Object(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 1, 1, 2, 11),
    _RsTrapsAllWarningsOff_Type()
)
rsTrapsAllWarningsOff.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsTrapsAllWarningsOff.setStatus("current")
_TransmitterConfig_ObjectIdentity = ObjectIdentity
transmitterConfig = _TransmitterConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 1, 1, 3)
)
_DateTime_Type = DateAndTime
_DateTime_Object = MibScalar
dateTime = _DateTime_Object(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 1, 1, 3, 1),
    _DateTime_Type()
)
dateTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dateTime.setStatus("current")
_Ntp_ObjectIdentity = ObjectIdentity
ntp = _Ntp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 1, 1, 3, 2)
)


class _NtpMode_Type(Integer32):
    """Custom type ntpMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 1),
          ("disabled", 2),
          ("stepAdjust", 4))
    )


_NtpMode_Type.__name__ = "Integer32"
_NtpMode_Object = MibScalar
ntpMode = _NtpMode_Object(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 1, 1, 3, 2, 1),
    _NtpMode_Type()
)
ntpMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntpMode.setStatus("current")


class _NtpSyncTimeInterval_Type(Integer32):
    """Custom type ntpSyncTimeInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(6, 1440),
    )


_NtpSyncTimeInterval_Type.__name__ = "Integer32"
_NtpSyncTimeInterval_Object = MibScalar
ntpSyncTimeInterval = _NtpSyncTimeInterval_Object(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 1, 1, 3, 2, 2),
    _NtpSyncTimeInterval_Type()
)
ntpSyncTimeInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntpSyncTimeInterval.setStatus("current")
if mibBuilder.loadTexts:
    ntpSyncTimeInterval.setUnits("minute")
_NtpServerAddrTable_Object = MibTable
ntpServerAddrTable = _NtpServerAddrTable_Object(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 1, 1, 3, 2, 3)
)
if mibBuilder.loadTexts:
    ntpServerAddrTable.setStatus("current")
_NtpServerAddrEntry_Object = MibTableRow
ntpServerAddrEntry = _NtpServerAddrEntry_Object(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 1, 1, 3, 2, 3, 1)
)
ntpServerAddrEntry.setIndexNames(
    (0, "RS-XX8000-COMMON-MIB", "ntpServerAddrIdx"),
)
if mibBuilder.loadTexts:
    ntpServerAddrEntry.setStatus("current")


class _NtpServerAddrIdx_Type(Integer32):
    """Custom type ntpServerAddrIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
    )


_NtpServerAddrIdx_Type.__name__ = "Integer32"
_NtpServerAddrIdx_Object = MibTableColumn
ntpServerAddrIdx = _NtpServerAddrIdx_Object(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 1, 1, 3, 2, 3, 1, 1),
    _NtpServerAddrIdx_Type()
)
ntpServerAddrIdx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ntpServerAddrIdx.setStatus("current")
_NtpServerAddress_Type = ReadableString
_NtpServerAddress_Object = MibTableColumn
ntpServerAddress = _NtpServerAddress_Object(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 1, 1, 3, 2, 3, 1, 2),
    _NtpServerAddress_Type()
)
ntpServerAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntpServerAddress.setStatus("current")


class _NtpState_Type(Integer32):
    """Custom type ntpState based on Integer32"""
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
        *(("unknown", 1),
          ("disabled", 2),
          ("enabled", 3),
          ("notRunning", 4),
          ("syncFailed", 5),
          ("synchronizing", 6),
          ("syncOk", 7))
    )


_NtpState_Type.__name__ = "Integer32"
_NtpState_Object = MibScalar
ntpState = _NtpState_Object(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 1, 1, 3, 2, 4),
    _NtpState_Type()
)
ntpState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntpState.setStatus("current")
_NtpLastSync_Type = DateAndTime
_NtpLastSync_Object = MibScalar
ntpLastSync = _NtpLastSync_Object(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 1, 1, 3, 2, 5),
    _NtpLastSync_Type()
)
ntpLastSync.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntpLastSync.setStatus("current")
_SwMaintenance_ObjectIdentity = ObjectIdentity
swMaintenance = _SwMaintenance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 1, 1, 3, 5)
)
_Restart_Type = Trigger
_Restart_Object = MibScalar
restart = _Restart_Object(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 1, 1, 3, 5, 1),
    _Restart_Type()
)
restart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    restart.setStatus("current")
_SwUpdate_ObjectIdentity = ObjectIdentity
swUpdate = _SwUpdate_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 1, 1, 3, 5, 5)
)
_SwUpdateStart_Type = Trigger
_SwUpdateStart_Object = MibScalar
swUpdateStart = _SwUpdateStart_Object(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 1, 1, 3, 5, 5, 2),
    _SwUpdateStart_Type()
)
swUpdateStart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swUpdateStart.setStatus("current")


class _SwUpdateMode_Type(Integer32):
    """Custom type swUpdateMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("manual", 1),
          ("permanent", 2))
    )


_SwUpdateMode_Type.__name__ = "Integer32"
_SwUpdateMode_Object = MibScalar
swUpdateMode = _SwUpdateMode_Object(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 1, 1, 3, 5, 5, 3),
    _SwUpdateMode_Type()
)
swUpdateMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swUpdateMode.setStatus("current")


class _SwUpdateDeviceName_Type(ReadableString):
    """Custom type swUpdateDeviceName based on ReadableString"""
    subtypeSpec = ReadableString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 30),
    )


_SwUpdateDeviceName_Type.__name__ = "ReadableString"
_SwUpdateDeviceName_Object = MibScalar
swUpdateDeviceName = _SwUpdateDeviceName_Object(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 1, 1, 3, 5, 5, 4),
    _SwUpdateDeviceName_Type()
)
swUpdateDeviceName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swUpdateDeviceName.setStatus("current")


class _SwUpdateDeviceGroup_Type(ReadableString):
    """Custom type swUpdateDeviceGroup based on ReadableString"""
    subtypeSpec = ReadableString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 30),
    )


_SwUpdateDeviceGroup_Type.__name__ = "ReadableString"
_SwUpdateDeviceGroup_Object = MibScalar
swUpdateDeviceGroup = _SwUpdateDeviceGroup_Object(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 1, 1, 3, 5, 5, 5),
    _SwUpdateDeviceGroup_Type()
)
swUpdateDeviceGroup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swUpdateDeviceGroup.setStatus("current")
_RsXx8000CommonEvents_ObjectIdentity = ObjectIdentity
rsXx8000CommonEvents = _RsXx8000CommonEvents_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 1, 2)
)
_RsXx8000EventsV2_ObjectIdentity = ObjectIdentity
rsXx8000EventsV2 = _RsXx8000EventsV2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 1, 2, 0)
)
_EventTx_ObjectIdentity = ObjectIdentity
eventTx = _EventTx_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 1, 2, 0, 10)
)
_EventsTxV2_ObjectIdentity = ObjectIdentity
eventsTxV2 = _EventsTxV2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 1, 2, 0, 10, 0)
)
if mibBuilder.loadTexts:
    eventsTxV2.setStatus("current")
_EventsTxTable_Object = MibTable
eventsTxTable = _EventsTxTable_Object(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 1, 2, 0, 10, 1)
)
if mibBuilder.loadTexts:
    eventsTxTable.setStatus("current")
_EventsTxEntry_Object = MibTableRow
eventsTxEntry = _EventsTxEntry_Object(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 1, 2, 0, 10, 1, 1)
)
eventsTxEntry.setIndexNames(
    (0, "RS-XX8000-COMMON-MIB", "eventTxNameIdx"),
)
if mibBuilder.loadTexts:
    eventsTxEntry.setStatus("current")
_EventTxNameIdx_Type = EventMaxEntryNumber
_EventTxNameIdx_Object = MibTableColumn
eventTxNameIdx = _EventTxNameIdx_Object(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 1, 2, 0, 10, 1, 1, 1),
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
              2)
        )
    )
    namedValues = NamedValues(
        *(("swUpdateStarted", 1),
          ("ntpSyncFailed", 2))
    )


_EventTxName_Type.__name__ = "Integer32"
_EventTxName_Object = MibTableColumn
eventTxName = _EventTxName_Object(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 1, 2, 0, 10, 1, 1, 2),
    _EventTxName_Type()
)
eventTxName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eventTxName.setStatus("current")
_EventTxMask_Type = EventMask
_EventTxMask_Object = MibTableColumn
eventTxMask = _EventTxMask_Object(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 1, 2, 0, 10, 1, 1, 3),
    _EventTxMask_Type()
)
eventTxMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eventTxMask.setStatus("current")
_EventTxPriority_Type = EventPriority
_EventTxPriority_Object = MibTableColumn
eventTxPriority = _EventTxPriority_Object(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 1, 2, 0, 10, 1, 1, 4),
    _EventTxPriority_Type()
)
eventTxPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eventTxPriority.setStatus("current")
_EventTxEvent_Type = EventState
_EventTxEvent_Object = MibTableColumn
eventTxEvent = _EventTxEvent_Object(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 1, 2, 0, 10, 1, 1, 5),
    _EventTxEvent_Type()
)
eventTxEvent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eventTxEvent.setStatus("current")
_EventHistory_ObjectIdentity = ObjectIdentity
eventHistory = _EventHistory_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 1, 2, 1)
)
if mibBuilder.loadTexts:
    eventHistory.setStatus("current")
_CounterEvents_Type = Counter32
_CounterEvents_Object = MibScalar
counterEvents = _CounterEvents_Object(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 1, 2, 1, 1),
    _CounterEvents_Type()
)
counterEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    counterEvents.setStatus("current")
_EventHistoryTable_Object = MibTable
eventHistoryTable = _EventHistoryTable_Object(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 1, 2, 1, 2)
)
if mibBuilder.loadTexts:
    eventHistoryTable.setStatus("current")
_EventHistoryEntry_Object = MibTableRow
eventHistoryEntry = _EventHistoryEntry_Object(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 1, 2, 1, 2, 1)
)
eventHistoryEntry.setIndexNames(
    (0, "RS-XX8000-COMMON-MIB", "eventHistoryNumber"),
)
if mibBuilder.loadTexts:
    eventHistoryEntry.setStatus("current")


class _EventHistoryNumber_Type(Integer32):
    """Custom type eventHistoryNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_EventHistoryNumber_Type.__name__ = "Integer32"
_EventHistoryNumber_Object = MibTableColumn
eventHistoryNumber = _EventHistoryNumber_Object(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 1, 2, 1, 2, 1, 1),
    _EventHistoryNumber_Type()
)
eventHistoryNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    eventHistoryNumber.setStatus("current")


class _EventHistoryModule_Type(Integer32):
    """Custom type eventHistoryModule based on Integer32"""
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
              14)
        )
    )
    namedValues = NamedValues(
        *(("switchoverUnit", 1),
          ("netccu", 2),
          ("exciterA", 3),
          ("exciterB", 4),
          ("outputstageA", 5),
          ("outputstageB", 6),
          ("dvbReceiver", 7),
          ("pumpA", 8),
          ("pumpB", 9),
          ("antenna", 10),
          ("gps", 11),
          ("dvbRecMon", 12),
          ("gpParIO", 13),
          ("program", 14))
    )


_EventHistoryModule_Type.__name__ = "Integer32"
_EventHistoryModule_Object = MibTableColumn
eventHistoryModule = _EventHistoryModule_Object(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 1, 2, 1, 2, 1, 2),
    _EventHistoryModule_Type()
)
eventHistoryModule.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eventHistoryModule.setStatus("current")
_EventHistoryEvent_Type = Integer32
_EventHistoryEvent_Object = MibTableColumn
eventHistoryEvent = _EventHistoryEvent_Object(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 1, 2, 1, 2, 1, 3),
    _EventHistoryEvent_Type()
)
eventHistoryEvent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eventHistoryEvent.setStatus("current")
_EventHistoryEventState_Type = EventState
_EventHistoryEventState_Object = MibTableColumn
eventHistoryEventState = _EventHistoryEventState_Object(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 1, 2, 1, 2, 1, 4),
    _EventHistoryEventState_Type()
)
eventHistoryEventState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eventHistoryEventState.setStatus("current")
_EventHistoryEventDate_Type = DateAndTime
_EventHistoryEventDate_Object = MibTableColumn
eventHistoryEventDate = _EventHistoryEventDate_Object(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 1, 2, 1, 2, 1, 5),
    _EventHistoryEventDate_Type()
)
eventHistoryEventDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eventHistoryEventDate.setStatus("current")
_EventHistoryTx_Type = IndexTransmitter
_EventHistoryTx_Object = MibTableColumn
eventHistoryTx = _EventHistoryTx_Object(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 1, 2, 1, 2, 1, 101),
    _EventHistoryTx_Type()
)
eventHistoryTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eventHistoryTx.setStatus("current")
_EventMapObjects_ObjectIdentity = ObjectIdentity
eventMapObjects = _EventMapObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 1, 2, 3)
)
_EventAlarmPriority_Type = EventPriority
_EventAlarmPriority_Object = MibScalar
eventAlarmPriority = _EventAlarmPriority_Object(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 1, 2, 3, 1),
    _EventAlarmPriority_Type()
)
eventAlarmPriority.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    eventAlarmPriority.setStatus("current")
_EventAlarmClass_Type = EventClass
_EventAlarmClass_Object = MibScalar
eventAlarmClass = _EventAlarmClass_Object(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 1, 2, 3, 2),
    _EventAlarmClass_Type()
)
eventAlarmClass.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    eventAlarmClass.setStatus("current")
_EventEvent_Type = EventState
_EventEvent_Object = MibScalar
eventEvent = _EventEvent_Object(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 1, 2, 3, 3),
    _EventEvent_Type()
)
eventEvent.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    eventEvent.setStatus("current")
_IndexTransmitter_Type = IndexTransmitter
_IndexTransmitter_Object = MibScalar
indexTransmitter = _IndexTransmitter_Object(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 1, 2, 3, 4),
    _IndexTransmitter_Type()
)
indexTransmitter.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    indexTransmitter.setStatus("current")
_IndexAB_Type = IndexAB
_IndexAB_Object = MibScalar
indexAB = _IndexAB_Object(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 1, 2, 3, 5),
    _IndexAB_Type()
)
indexAB.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    indexAB.setStatus("current")
_IndexRack_Type = IndexRack
_IndexRack_Object = MibScalar
indexRack = _IndexRack_Object(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 1, 2, 3, 6),
    _IndexRack_Type()
)
indexRack.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    indexRack.setStatus("current")
_IndexAmplifier_Type = IndexAmplifier
_IndexAmplifier_Object = MibScalar
indexAmplifier = _IndexAmplifier_Object(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 1, 2, 3, 7),
    _IndexAmplifier_Type()
)
indexAmplifier.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    indexAmplifier.setStatus("current")
_IndexProgram_Type = IndexProgram
_IndexProgram_Object = MibScalar
indexProgram = _IndexProgram_Object(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 1, 2, 3, 8),
    _IndexProgram_Type()
)
indexProgram.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    indexProgram.setStatus("current")
_RsXx8000CommonConf_ObjectIdentity = ObjectIdentity
rsXx8000CommonConf = _RsXx8000CommonConf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 1, 3)
)
_RsXx8000CommonGroups_ObjectIdentity = ObjectIdentity
rsXx8000CommonGroups = _RsXx8000CommonGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 1, 3, 1)
)
_RsXx8000CommonCompls_ObjectIdentity = ObjectIdentity
rsXx8000CommonCompls = _RsXx8000CommonCompls_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 1, 3, 2)
)

# Managed Objects groups

groupEventTest = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 1, 3, 1, 6)
)
groupEventTest.setObjects(
    ("RS-XX8000-COMMON-MIB", "sendTestTrap")
)
if mibBuilder.loadTexts:
    groupEventTest.setStatus("current")

groupEventHistory = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 1, 3, 1, 8)
)
groupEventHistory.setObjects(
      *(("RS-XX8000-COMMON-MIB", "counterEvents"),
        ("RS-XX8000-COMMON-MIB", "eventHistoryModule"),
        ("RS-XX8000-COMMON-MIB", "eventHistoryEvent"),
        ("RS-XX8000-COMMON-MIB", "eventHistoryEventState"),
        ("RS-XX8000-COMMON-MIB", "eventHistoryEventDate"),
        ("RS-XX8000-COMMON-MIB", "eventHistoryTx"))
)
if mibBuilder.loadTexts:
    groupEventHistory.setStatus("current")

groupEventObjects = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 1, 3, 1, 9)
)
groupEventObjects.setObjects(
      *(("RS-XX8000-COMMON-MIB", "eventTxName"),
        ("RS-XX8000-COMMON-MIB", "eventTxMask"),
        ("RS-XX8000-COMMON-MIB", "eventTxPriority"),
        ("RS-XX8000-COMMON-MIB", "eventTxEvent"),
        ("RS-XX8000-COMMON-MIB", "eventAlarmPriority"),
        ("RS-XX8000-COMMON-MIB", "eventAlarmClass"),
        ("RS-XX8000-COMMON-MIB", "eventEvent"),
        ("RS-XX8000-COMMON-MIB", "indexTransmitter"),
        ("RS-XX8000-COMMON-MIB", "indexAB"),
        ("RS-XX8000-COMMON-MIB", "indexRack"),
        ("RS-XX8000-COMMON-MIB", "indexAmplifier"),
        ("RS-XX8000-COMMON-MIB", "indexProgram"))
)
if mibBuilder.loadTexts:
    groupEventObjects.setStatus("current")

groupProductInformation = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 1, 3, 1, 11)
)
groupProductInformation.setObjects(
      *(("RS-XX8000-COMMON-MIB", "serialNumber"),
        ("RS-XX8000-COMMON-MIB", "identNumberSW"),
        ("RS-XX8000-COMMON-MIB", "versionNumberSW"),
        ("RS-XX8000-COMMON-MIB", "identNumberHW"),
        ("RS-XX8000-COMMON-MIB", "versionNumberHW"))
)
if mibBuilder.loadTexts:
    groupProductInformation.setStatus("current")

groupSnmpConfig = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 1, 3, 1, 12)
)
groupSnmpConfig.setObjects(
      *(("RS-XX8000-COMMON-MIB", "trapSinkVersion"),
        ("RS-XX8000-COMMON-MIB", "trapSinkAddress"),
        ("RS-XX8000-COMMON-MIB", "trapSinkPort"),
        ("RS-XX8000-COMMON-MIB", "trapSinkCommunity"),
        ("RS-XX8000-COMMON-MIB", "trapSinkInformRetry"),
        ("RS-XX8000-COMMON-MIB", "trapSinkInformTimeout"),
        ("RS-XX8000-COMMON-MIB", "trapSinkUse"),
        ("RS-XX8000-COMMON-MIB", "irtTrapsAllOn"),
        ("RS-XX8000-COMMON-MIB", "irtTrapsAllOff"),
        ("RS-XX8000-COMMON-MIB", "rsTrapsAllOn"),
        ("RS-XX8000-COMMON-MIB", "rsTrapsAllOff"),
        ("RS-XX8000-COMMON-MIB", "rsTrapsAllFaultsOn"),
        ("RS-XX8000-COMMON-MIB", "rsTrapsAllFaultsOff"),
        ("RS-XX8000-COMMON-MIB", "rsTrapsAllWarningsOn"),
        ("RS-XX8000-COMMON-MIB", "rsTrapsAllWarningsOff"))
)
if mibBuilder.loadTexts:
    groupSnmpConfig.setStatus("current")

groupTransmitterConfig = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 1, 3, 1, 13)
)
groupTransmitterConfig.setObjects(
    ("RS-XX8000-COMMON-MIB", "dateTime")
)
if mibBuilder.loadTexts:
    groupTransmitterConfig.setStatus("current")

groupNTP = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 1, 3, 1, 14)
)
groupNTP.setObjects(
      *(("RS-XX8000-COMMON-MIB", "ntpMode"),
        ("RS-XX8000-COMMON-MIB", "ntpSyncTimeInterval"),
        ("RS-XX8000-COMMON-MIB", "ntpServerAddress"),
        ("RS-XX8000-COMMON-MIB", "ntpState"),
        ("RS-XX8000-COMMON-MIB", "ntpLastSync"))
)
if mibBuilder.loadTexts:
    groupNTP.setStatus("current")

groupSwMaintenance = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 1, 3, 1, 15)
)
groupSwMaintenance.setObjects(
      *(("RS-XX8000-COMMON-MIB", "restart"),
        ("RS-XX8000-COMMON-MIB", "swUpdateStart"),
        ("RS-XX8000-COMMON-MIB", "swUpdateMode"),
        ("RS-XX8000-COMMON-MIB", "swUpdateDeviceName"),
        ("RS-XX8000-COMMON-MIB", "swUpdateDeviceGroup"))
)
if mibBuilder.loadTexts:
    groupSwMaintenance.setStatus("current")

groupObsoletedObjects = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 1, 3, 1, 17)
)
groupObsoletedObjects.setObjects(
    ("RS-XX8000-COMMON-MIB", "trapSinkInformUnacknowledged")
)
if mibBuilder.loadTexts:
    groupObsoletedObjects.setStatus("obsolete")


# Notification objects

testTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 1, 2, 0, 1)
)
testTrap.setObjects(
      *(("RS-XX8000-COMMON-MIB", "serialNumber"),
        ("RS-XX8000-COMMON-MIB", "counterEvents"))
)
if mibBuilder.loadTexts:
    testTrap.setStatus(
        "current"
    )

swUpdateStarted = NotificationType(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 1, 2, 0, 10, 0, 1)
)
swUpdateStarted.setObjects(
      *(("RS-XX8000-COMMON-MIB", "eventAlarmPriority"),
        ("RS-XX8000-COMMON-MIB", "eventAlarmClass"),
        ("RS-XX8000-COMMON-MIB", "eventEvent"))
)
if mibBuilder.loadTexts:
    swUpdateStarted.setStatus(
        "current"
    )

ntpSyncFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 1, 2, 0, 10, 0, 2)
)
ntpSyncFailed.setObjects(
      *(("RS-XX8000-COMMON-MIB", "eventAlarmPriority"),
        ("RS-XX8000-COMMON-MIB", "eventAlarmClass"),
        ("RS-XX8000-COMMON-MIB", "eventEvent"))
)
if mibBuilder.loadTexts:
    ntpSyncFailed.setStatus(
        "current"
    )


# Notifications groups

groupNotifyTest = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 1, 3, 1, 1)
)
groupNotifyTest.setObjects(
    ("RS-XX8000-COMMON-MIB", "testTrap")
)
if mibBuilder.loadTexts:
    groupNotifyTest.setStatus(
        "current"
    )

groupNotify = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 1, 3, 1, 2)
)
groupNotify.setObjects(
    ("RS-XX8000-COMMON-MIB", "swUpdateStarted")
)
if mibBuilder.loadTexts:
    groupNotify.setStatus(
        "current"
    )

groupNotifyNTP = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 1, 3, 1, 16)
)
groupNotifyNTP.setObjects(
    ("RS-XX8000-COMMON-MIB", "ntpSyncFailed")
)
if mibBuilder.loadTexts:
    groupNotifyNTP.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

xx8000BasicCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 2566, 127, 1, 2, 167, 1, 3, 2, 1)
)
xx8000BasicCompliance.setObjects(
      *(("RS-XX8000-COMMON-MIB", "groupNotifyTest"),
        ("RS-XX8000-COMMON-MIB", "groupNotify"),
        ("RS-XX8000-COMMON-MIB", "groupEventTest"),
        ("RS-XX8000-COMMON-MIB", "groupEventHistory"),
        ("RS-XX8000-COMMON-MIB", "groupEventObjects"),
        ("RS-XX8000-COMMON-MIB", "groupProductInformation"),
        ("RS-XX8000-COMMON-MIB", "groupSnmpConfig"),
        ("RS-XX8000-COMMON-MIB", "groupTransmitterConfig"),
        ("RS-XX8000-COMMON-MIB", "groupSwMaintenance"),
        ("RS-XX8000-COMMON-MIB", "groupNTP"),
        ("RS-XX8000-COMMON-MIB", "groupNotifyNTP"))
)
if mibBuilder.loadTexts:
    xx8000BasicCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RS-XX8000-COMMON-MIB",
    **{"ReadableString": ReadableString,
       "FloatingPoint": FloatingPoint,
       "TimeOfDay": TimeOfDay,
       "EventMask": EventMask,
       "EventPriority": EventPriority,
       "EventClass": EventClass,
       "EventState": EventState,
       "EventMaxEntryNumber": EventMaxEntryNumber,
       "SwitchOnOff": SwitchOnOff,
       "Trigger": Trigger,
       "LogbookEntryMessagesNetCCU": LogbookEntryMessagesNetCCU,
       "LogbookEntryMessagesExcTv": LogbookEntryMessagesExcTv,
       "LogbookEntryMessagesExcDVB": LogbookEntryMessagesExcDVB,
       "LogbookEntryMessagesExcFM": LogbookEntryMessagesExcFM,
       "LogbookEntryMessagesOST": LogbookEntryMessagesOST,
       "LogbookEntryMessagesNSU": LogbookEntryMessagesNSU,
       "LogbookEntryMessagesXV703": LogbookEntryMessagesXV703,
       "LogbookEntrySlope": LogbookEntrySlope,
       "LogbookMaxEntryNumber": LogbookMaxEntryNumber,
       "IndexTransmitter": IndexTransmitter,
       "IndexRack": IndexRack,
       "IndexAmplifier": IndexAmplifier,
       "IndexProgram": IndexProgram,
       "IndexAB": IndexAB,
       "ProdInfoModuleNameTv": ProdInfoModuleNameTv,
       "ProdInfoModuleNameFm": ProdInfoModuleNameFm,
       "ProdInfoModuleNameNsu": ProdInfoModuleNameNsu,
       "LogbookEntryMessagesExcATV": LogbookEntryMessagesExcATV,
       "LockState": LockState,
       "EqualizerCalibrationState": EqualizerCalibrationState,
       "TvStandard": TvStandard,
       "AtvStandard": AtvStandard,
       "InputSource": InputSource,
       "Sx801AmplifierState": Sx801AmplifierState,
       "FailDelayMode": FailDelayMode,
       "FailDelayStatus": FailDelayStatus,
       "rsXx8000": rsXx8000,
       "rsXx8000Common": rsXx8000Common,
       "rsXx8000CommonObjs": rsXx8000CommonObjs,
       "productInformation": productInformation,
       "serialNumber": serialNumber,
       "identNumberSW": identNumberSW,
       "versionNumberSW": versionNumberSW,
       "identNumberHW": identNumberHW,
       "versionNumberHW": versionNumberHW,
       "snmpConfig": snmpConfig,
       "trapSinkTable": trapSinkTable,
       "trapSinkEntry": trapSinkEntry,
       "trapSinkNumber": trapSinkNumber,
       "trapSinkVersion": trapSinkVersion,
       "trapSinkAddress": trapSinkAddress,
       "trapSinkPort": trapSinkPort,
       "trapSinkCommunity": trapSinkCommunity,
       "trapSinkInformRetry": trapSinkInformRetry,
       "trapSinkInformTimeout": trapSinkInformTimeout,
       "trapSinkInformUnacknowledged": trapSinkInformUnacknowledged,
       "trapSinkUse": trapSinkUse,
       "sendTestTrap": sendTestTrap,
       "irtTrapsAllOn": irtTrapsAllOn,
       "irtTrapsAllOff": irtTrapsAllOff,
       "rsTrapsAllOn": rsTrapsAllOn,
       "rsTrapsAllOff": rsTrapsAllOff,
       "rsTrapsAllFaultsOn": rsTrapsAllFaultsOn,
       "rsTrapsAllFaultsOff": rsTrapsAllFaultsOff,
       "rsTrapsAllWarningsOn": rsTrapsAllWarningsOn,
       "rsTrapsAllWarningsOff": rsTrapsAllWarningsOff,
       "transmitterConfig": transmitterConfig,
       "dateTime": dateTime,
       "ntp": ntp,
       "ntpMode": ntpMode,
       "ntpSyncTimeInterval": ntpSyncTimeInterval,
       "ntpServerAddrTable": ntpServerAddrTable,
       "ntpServerAddrEntry": ntpServerAddrEntry,
       "ntpServerAddrIdx": ntpServerAddrIdx,
       "ntpServerAddress": ntpServerAddress,
       "ntpState": ntpState,
       "ntpLastSync": ntpLastSync,
       "swMaintenance": swMaintenance,
       "restart": restart,
       "swUpdate": swUpdate,
       "swUpdateStart": swUpdateStart,
       "swUpdateMode": swUpdateMode,
       "swUpdateDeviceName": swUpdateDeviceName,
       "swUpdateDeviceGroup": swUpdateDeviceGroup,
       "rsXx8000CommonEvents": rsXx8000CommonEvents,
       "rsXx8000EventsV2": rsXx8000EventsV2,
       "testTrap": testTrap,
       "eventTx": eventTx,
       "eventsTxV2": eventsTxV2,
       "swUpdateStarted": swUpdateStarted,
       "ntpSyncFailed": ntpSyncFailed,
       "eventsTxTable": eventsTxTable,
       "eventsTxEntry": eventsTxEntry,
       "eventTxNameIdx": eventTxNameIdx,
       "eventTxName": eventTxName,
       "eventTxMask": eventTxMask,
       "eventTxPriority": eventTxPriority,
       "eventTxEvent": eventTxEvent,
       "eventHistory": eventHistory,
       "counterEvents": counterEvents,
       "eventHistoryTable": eventHistoryTable,
       "eventHistoryEntry": eventHistoryEntry,
       "eventHistoryNumber": eventHistoryNumber,
       "eventHistoryModule": eventHistoryModule,
       "eventHistoryEvent": eventHistoryEvent,
       "eventHistoryEventState": eventHistoryEventState,
       "eventHistoryEventDate": eventHistoryEventDate,
       "eventHistoryTx": eventHistoryTx,
       "eventMapObjects": eventMapObjects,
       "eventAlarmPriority": eventAlarmPriority,
       "eventAlarmClass": eventAlarmClass,
       "eventEvent": eventEvent,
       "indexTransmitter": indexTransmitter,
       "indexAB": indexAB,
       "indexRack": indexRack,
       "indexAmplifier": indexAmplifier,
       "indexProgram": indexProgram,
       "rsXx8000CommonConf": rsXx8000CommonConf,
       "rsXx8000CommonGroups": rsXx8000CommonGroups,
       "groupNotifyTest": groupNotifyTest,
       "groupNotify": groupNotify,
       "groupEventTest": groupEventTest,
       "groupEventHistory": groupEventHistory,
       "groupEventObjects": groupEventObjects,
       "groupProductInformation": groupProductInformation,
       "groupSnmpConfig": groupSnmpConfig,
       "groupTransmitterConfig": groupTransmitterConfig,
       "groupNTP": groupNTP,
       "groupSwMaintenance": groupSwMaintenance,
       "groupNotifyNTP": groupNotifyNTP,
       "groupObsoletedObjects": groupObsoletedObjects,
       "rsXx8000CommonCompls": rsXx8000CommonCompls,
       "xx8000BasicCompliance": xx8000BasicCompliance,
       "rsXx8000MibModule": rsXx8000MibModule}
)
