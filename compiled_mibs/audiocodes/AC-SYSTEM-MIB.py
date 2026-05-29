# SNMP MIB module (AC-SYSTEM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\audiocodes\AC-SYSTEM-MIB

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

(acBoardMibs,
 acGeneric,
 acProducts,
 acRegistrations,
 audioCodes) = mibBuilder.importSymbols(
    "AUDIOCODES-TYPES-MIB",
    "acBoardMibs",
    "acGeneric",
    "acProducts",
    "acRegistrations",
    "audioCodes")

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

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
    "TimeTicks",
    "Unsigned32",
    "enterprises",
    "iso")

(DateAndTime,
 DisplayString,
 PhysAddress,
 RowPointer,
 RowStatus,
 TAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "PhysAddress",
    "RowPointer",
    "RowStatus",
    "TAddress",
    "TextualConvention")


# MODULE-IDENTITY

acSystem = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AcSystemConfiguration_ObjectIdentity = ObjectIdentity
acSystemConfiguration = _AcSystemConfiguration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1)
)
_AcSysControl_ObjectIdentity = ObjectIdentity
acSysControl = _AcSysControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 1)
)


class _AcSysControlProtocolType_Type(Integer32):
    """Custom type acSysControlProtocolType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              4,
              8)
        )
    )
    namedValues = NamedValues(
        *(("controlProtocol-None", 0),
          ("controlProtocol-MGCP", 1),
          ("controlProtocol-MEGACO", 2),
          ("controlProtocol-H323", 4),
          ("controlProtocol-SIP", 8))
    )


_AcSysControlProtocolType_Type.__name__ = "Integer32"
_AcSysControlProtocolType_Object = MibScalar
acSysControlProtocolType = _AcSysControlProtocolType_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 1, 1),
    _AcSysControlProtocolType_Type()
)
acSysControlProtocolType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acSysControlProtocolType.setStatus("obsolete")


class _AcSysControlTrunkingToAnalogFunctionalityProfile_Type(Integer32):
    """Custom type acSysControlTrunkingToAnalogFunctionalityProfile based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("cASAnalog", 1))
    )


_AcSysControlTrunkingToAnalogFunctionalityProfile_Type.__name__ = "Integer32"
_AcSysControlTrunkingToAnalogFunctionalityProfile_Object = MibScalar
acSysControlTrunkingToAnalogFunctionalityProfile = _AcSysControlTrunkingToAnalogFunctionalityProfile_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 1, 2),
    _AcSysControlTrunkingToAnalogFunctionalityProfile_Type()
)
acSysControlTrunkingToAnalogFunctionalityProfile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acSysControlTrunkingToAnalogFunctionalityProfile.setStatus("current")
_AcSysTDM_ObjectIdentity = ObjectIdentity
acSysTDM = _AcSysTDM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 2)
)
_AcSysTDMClock_ObjectIdentity = ObjectIdentity
acSysTDMClock = _AcSysTDMClock_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 2, 1)
)


class _AcSysTDMClockSource_Type(Integer32):
    """Custom type acSysTDMClockSource based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              3,
              4,
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
              22)
        )
    )
    namedValues = NamedValues(
        *(("internal", 1),
          ("mVIP", 3),
          ("network", 4),
          ("h110-A", 8),
          ("h110-B", 9),
          ("netReference1", 10),
          ("netReference2", 11),
          ("sC-2M", 12),
          ("sC-4M", 13),
          ("sC-8M", 14),
          ("bITS", 15),
          ("network-b", 16),
          ("aTM-OC3", 17),
          ("aTM-OC3-B", 18),
          ("aTM-OC12", 19),
          ("network-DS3-1", 20),
          ("network-DS3-2", 21),
          ("network-DS3-3", 22))
    )


_AcSysTDMClockSource_Type.__name__ = "Integer32"
_AcSysTDMClockSource_Object = MibScalar
acSysTDMClockSource = _AcSysTDMClockSource_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 2, 1, 1),
    _AcSysTDMClockSource_Type()
)
acSysTDMClockSource.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acSysTDMClockSource.setStatus("current")


class _AcSysTDMClockEnableFallBack_Type(Integer32):
    """Custom type acSysTDMClockEnableFallBack based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("manual", 0),
          ("autoNon-Revertive", 1),
          ("auto-Revertive", 2))
    )


_AcSysTDMClockEnableFallBack_Type.__name__ = "Integer32"
_AcSysTDMClockEnableFallBack_Object = MibScalar
acSysTDMClockEnableFallBack = _AcSysTDMClockEnableFallBack_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 2, 1, 2),
    _AcSysTDMClockEnableFallBack_Type()
)
acSysTDMClockEnableFallBack.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acSysTDMClockEnableFallBack.setStatus("current")


class _AcSysTDMClockLocalReference_Type(Unsigned32):
    """Custom type acSysTDMClockLocalReference based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 256),
    )


_AcSysTDMClockLocalReference_Type.__name__ = "Unsigned32"
_AcSysTDMClockLocalReference_Object = MibScalar
acSysTDMClockLocalReference = _AcSysTDMClockLocalReference_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 2, 1, 3),
    _AcSysTDMClockLocalReference_Type()
)
acSysTDMClockLocalReference.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acSysTDMClockLocalReference.setStatus("current")


class _AcSysTDMClockMasterSlaveSelection_Type(Integer32):
    """Custom type acSysTDMClockMasterSlaveSelection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("acTDMBusSlaveMode", 0),
          ("acTDMBusMasterMode", 1),
          ("acH110BusSecondaryMasterMode", 2))
    )


_AcSysTDMClockMasterSlaveSelection_Type.__name__ = "Integer32"
_AcSysTDMClockMasterSlaveSelection_Object = MibScalar
acSysTDMClockMasterSlaveSelection = _AcSysTDMClockMasterSlaveSelection_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 2, 1, 4),
    _AcSysTDMClockMasterSlaveSelection_Type()
)
acSysTDMClockMasterSlaveSelection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acSysTDMClockMasterSlaveSelection.setStatus("current")


class _AcSysTDMClockNetRefSpeed_Type(Integer32):
    """Custom type acSysTDMClockNetRefSpeed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("acTH110BusNetRefSpeed-8khz", 0),
          ("acTH110BusNetRefSpeed-1544khz", 1),
          ("acTH110BusNetRefSpeed-20488khz", 2))
    )


_AcSysTDMClockNetRefSpeed_Type.__name__ = "Integer32"
_AcSysTDMClockNetRefSpeed_Object = MibScalar
acSysTDMClockNetRefSpeed = _AcSysTDMClockNetRefSpeed_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 2, 1, 5),
    _AcSysTDMClockNetRefSpeed_Type()
)
acSysTDMClockNetRefSpeed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acSysTDMClockNetRefSpeed.setStatus("current")


class _AcSysTDMClockAutoFallBackEnable_Type(Integer32):
    """Custom type acSysTDMClockAutoFallBackEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_AcSysTDMClockAutoFallBackEnable_Type.__name__ = "Integer32"
_AcSysTDMClockAutoFallBackEnable_Object = MibScalar
acSysTDMClockAutoFallBackEnable = _AcSysTDMClockAutoFallBackEnable_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 2, 1, 6),
    _AcSysTDMClockAutoFallBackEnable_Type()
)
acSysTDMClockAutoFallBackEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acSysTDMClockAutoFallBackEnable.setStatus("current")


class _AcSysTDMClockAutoFallBackRevertingEnable_Type(Integer32):
    """Custom type acSysTDMClockAutoFallBackRevertingEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_AcSysTDMClockAutoFallBackRevertingEnable_Type.__name__ = "Integer32"
_AcSysTDMClockAutoFallBackRevertingEnable_Object = MibScalar
acSysTDMClockAutoFallBackRevertingEnable = _AcSysTDMClockAutoFallBackRevertingEnable_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 2, 1, 7),
    _AcSysTDMClockAutoFallBackRevertingEnable_Type()
)
acSysTDMClockAutoFallBackRevertingEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acSysTDMClockAutoFallBackRevertingEnable.setStatus("current")


class _AcSysTDMClockBitsReference_Type(Unsigned32):
    """Custom type acSysTDMClockBitsReference based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_AcSysTDMClockBitsReference_Type.__name__ = "Unsigned32"
_AcSysTDMClockBitsReference_Object = MibScalar
acSysTDMClockBitsReference = _AcSysTDMClockBitsReference_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 2, 1, 8),
    _AcSysTDMClockBitsReference_Type()
)
acSysTDMClockBitsReference.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acSysTDMClockBitsReference.setStatus("current")


class _AcSysTDMClockPLLOutOfRange_Type(Integer32):
    """Custom type acSysTDMClockPLLOutOfRange based on Integer32"""
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
        *(("oor-9-2to12ppm", 0),
          ("oor-40to52ppm", 1),
          ("oor-100to130ppm", 2),
          ("oor-64to83ppm", 3),
          ("oor-13-8to18ppm", 4),
          ("oor-24-6to32ppm", 5),
          ("oor-36-6to47-5ppm", 6),
          ("oor-52to67-5ppm", 7))
    )


_AcSysTDMClockPLLOutOfRange_Type.__name__ = "Integer32"
_AcSysTDMClockPLLOutOfRange_Object = MibScalar
acSysTDMClockPLLOutOfRange = _AcSysTDMClockPLLOutOfRange_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 2, 1, 9),
    _AcSysTDMClockPLLOutOfRange_Type()
)
acSysTDMClockPLLOutOfRange.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acSysTDMClockPLLOutOfRange.setStatus("current")


class _AcSysTDMClockFallbackClock_Type(Integer32):
    """Custom type acSysTDMClockFallbackClock based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(4,
              8,
              9,
              10,
              11)
        )
    )
    namedValues = NamedValues(
        *(("network", 4),
          ("h110-A", 8),
          ("h110-B", 9),
          ("netReference1", 10),
          ("netReference2", 11))
    )


_AcSysTDMClockFallbackClock_Type.__name__ = "Integer32"
_AcSysTDMClockFallbackClock_Object = MibScalar
acSysTDMClockFallbackClock = _AcSysTDMClockFallbackClock_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 2, 1, 10),
    _AcSysTDMClockFallbackClock_Type()
)
acSysTDMClockFallbackClock.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acSysTDMClockFallbackClock.setStatus("current")
_AcSysTDMBus_ObjectIdentity = ObjectIdentity
acSysTDMBus = _AcSysTDMBus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 2, 2)
)


class _AcSysTDMBusType_Type(Integer32):
    """Custom type acSysTDMBusType based on Integer32"""
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("mVIP-BUS", 0),
          ("sC-BUS", 1),
          ("uSE-FRAMERS", 2),
          ("qSLAC-BUS", 3),
          ("uSE-H110-BUS", 4),
          ("uSE-EXT-BUS", 5),
          ("aNALOG-BUS", 6),
          ("uSE-PSTN-SW-ONLY", 8))
    )


_AcSysTDMBusType_Type.__name__ = "Integer32"
_AcSysTDMBusType_Object = MibScalar
acSysTDMBusType = _AcSysTDMBusType_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 2, 2, 1),
    _AcSysTDMBusType_Type()
)
acSysTDMBusType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acSysTDMBusType.setStatus("current")


class _AcSysTDMBusSpeed_Type(Integer32):
    """Custom type acSysTDMBusSpeed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("acTDMBusSpeed-2Mbps", 0),
          ("acTDMBusSpeed-4Mbps", 2),
          ("acTDMBusSpeed-8Mbps", 3),
          ("acTDMBusSpeed-16Mbps", 4))
    )


_AcSysTDMBusSpeed_Type.__name__ = "Integer32"
_AcSysTDMBusSpeed_Object = MibScalar
acSysTDMBusSpeed = _AcSysTDMBusSpeed_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 2, 2, 2),
    _AcSysTDMBusSpeed_Type()
)
acSysTDMBusSpeed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acSysTDMBusSpeed.setStatus("current")


class _AcSysTDMBusOutputPort_Type(Unsigned32):
    """Custom type acSysTDMBusOutputPort based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 31),
    )


_AcSysTDMBusOutputPort_Type.__name__ = "Unsigned32"
_AcSysTDMBusOutputPort_Object = MibScalar
acSysTDMBusOutputPort = _AcSysTDMBusOutputPort_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 2, 2, 3),
    _AcSysTDMBusOutputPort_Type()
)
acSysTDMBusOutputPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acSysTDMBusOutputPort.setStatus("current")


class _AcSysTDMBusOutputStartingChannel_Type(Unsigned32):
    """Custom type acSysTDMBusOutputStartingChannel based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 127),
    )


_AcSysTDMBusOutputStartingChannel_Type.__name__ = "Unsigned32"
_AcSysTDMBusOutputStartingChannel_Object = MibScalar
acSysTDMBusOutputStartingChannel = _AcSysTDMBusOutputStartingChannel_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 2, 2, 4),
    _AcSysTDMBusOutputStartingChannel_Type()
)
acSysTDMBusOutputStartingChannel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acSysTDMBusOutputStartingChannel.setStatus("current")
_AcSysPCM_ObjectIdentity = ObjectIdentity
acSysPCM = _AcSysPCM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 2, 3)
)


class _AcSysPCMLawSelect_Type(Integer32):
    """Custom type acSysPCMLawSelect based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              3)
        )
    )
    namedValues = NamedValues(
        *(("automatic", 0),
          ("aLaw", 1),
          ("muLaw", 3))
    )


_AcSysPCMLawSelect_Type.__name__ = "Integer32"
_AcSysPCMLawSelect_Object = MibScalar
acSysPCMLawSelect = _AcSysPCMLawSelect_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 2, 3, 1),
    _AcSysPCMLawSelect_Type()
)
acSysPCMLawSelect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acSysPCMLawSelect.setStatus("current")


class _AcSysPCMIdlePattern_Type(Unsigned32):
    """Custom type acSysPCMIdlePattern based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AcSysPCMIdlePattern_Type.__name__ = "Unsigned32"
_AcSysPCMIdlePattern_Object = MibScalar
acSysPCMIdlePattern = _AcSysPCMIdlePattern_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 2, 3, 2),
    _AcSysPCMIdlePattern_Type()
)
acSysPCMIdlePattern.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acSysPCMIdlePattern.setStatus("current")


class _AcSysPCMIdleABCDPattern_Type(Unsigned32):
    """Custom type acSysPCMIdleABCDPattern based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AcSysPCMIdleABCDPattern_Type.__name__ = "Unsigned32"
_AcSysPCMIdleABCDPattern_Object = MibScalar
acSysPCMIdleABCDPattern = _AcSysPCMIdleABCDPattern_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 2, 3, 3),
    _AcSysPCMIdleABCDPattern_Type()
)
acSysPCMIdleABCDPattern.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acSysPCMIdleABCDPattern.setStatus("current")


class _AcSysPCMSerialPortAuditIntervalMin_Type(Unsigned32):
    """Custom type acSysPCMSerialPortAuditIntervalMin based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 60),
    )


_AcSysPCMSerialPortAuditIntervalMin_Type.__name__ = "Unsigned32"
_AcSysPCMSerialPortAuditIntervalMin_Object = MibScalar
acSysPCMSerialPortAuditIntervalMin = _AcSysPCMSerialPortAuditIntervalMin_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 2, 3, 4),
    _AcSysPCMSerialPortAuditIntervalMin_Type()
)
acSysPCMSerialPortAuditIntervalMin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acSysPCMSerialPortAuditIntervalMin.setStatus("current")
_AcSysNetworkConfig_ObjectIdentity = ObjectIdentity
acSysNetworkConfig = _AcSysNetworkConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 3)
)
_AcSysIP_ObjectIdentity = ObjectIdentity
acSysIP = _AcSysIP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 3, 1)
)
_AcSysIPAddress_Type = IpAddress
_AcSysIPAddress_Object = MibScalar
acSysIPAddress = _AcSysIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 3, 1, 1),
    _AcSysIPAddress_Type()
)
acSysIPAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acSysIPAddress.setStatus("current")
_AcSysIPSubNetAddress_Type = IpAddress
_AcSysIPSubNetAddress_Object = MibScalar
acSysIPSubNetAddress = _AcSysIPSubNetAddress_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 3, 1, 2),
    _AcSysIPSubNetAddress_Type()
)
acSysIPSubNetAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acSysIPSubNetAddress.setStatus("obsolete")
_AcSysIPDefaultGatewayAddress_Type = IpAddress
_AcSysIPDefaultGatewayAddress_Object = MibScalar
acSysIPDefaultGatewayAddress = _AcSysIPDefaultGatewayAddress_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 3, 1, 3),
    _AcSysIPDefaultGatewayAddress_Type()
)
acSysIPDefaultGatewayAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acSysIPDefaultGatewayAddress.setStatus("obsolete")


class _AcSysIPDHCPEnable_Type(Integer32):
    """Custom type acSysIPDHCPEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_AcSysIPDHCPEnable_Type.__name__ = "Integer32"
_AcSysIPDHCPEnable_Object = MibScalar
acSysIPDHCPEnable = _AcSysIPDHCPEnable_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 3, 1, 4),
    _AcSysIPDHCPEnable_Type()
)
acSysIPDHCPEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acSysIPDHCPEnable.setStatus("obsolete")


class _AcSysIPDHCPSpeedFactor_Type(Unsigned32):
    """Custom type acSysIPDHCPSpeedFactor based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10),
    )


_AcSysIPDHCPSpeedFactor_Type.__name__ = "Unsigned32"
_AcSysIPDHCPSpeedFactor_Object = MibScalar
acSysIPDHCPSpeedFactor = _AcSysIPDHCPSpeedFactor_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 3, 1, 5),
    _AcSysIPDHCPSpeedFactor_Type()
)
acSysIPDHCPSpeedFactor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acSysIPDHCPSpeedFactor.setStatus("obsolete")


class _AcSysIPDnsPrimaryServerType_Type(Integer32):
    """Custom type acSysIPDnsPrimaryServerType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("ipv4", 1)
    )


_AcSysIPDnsPrimaryServerType_Type.__name__ = "Integer32"
_AcSysIPDnsPrimaryServerType_Object = MibScalar
acSysIPDnsPrimaryServerType = _AcSysIPDnsPrimaryServerType_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 3, 1, 6),
    _AcSysIPDnsPrimaryServerType_Type()
)
acSysIPDnsPrimaryServerType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acSysIPDnsPrimaryServerType.setStatus("obsolete")
_AcSysIPDnsPrimaryServer_Type = IpAddress
_AcSysIPDnsPrimaryServer_Object = MibScalar
acSysIPDnsPrimaryServer = _AcSysIPDnsPrimaryServer_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 3, 1, 7),
    _AcSysIPDnsPrimaryServer_Type()
)
acSysIPDnsPrimaryServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acSysIPDnsPrimaryServer.setStatus("obsolete")


class _AcSysIPDnsSecondaryServerType_Type(Integer32):
    """Custom type acSysIPDnsSecondaryServerType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("ipv4", 1)
    )


_AcSysIPDnsSecondaryServerType_Type.__name__ = "Integer32"
_AcSysIPDnsSecondaryServerType_Object = MibScalar
acSysIPDnsSecondaryServerType = _AcSysIPDnsSecondaryServerType_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 3, 1, 8),
    _AcSysIPDnsSecondaryServerType_Type()
)
acSysIPDnsSecondaryServerType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acSysIPDnsSecondaryServerType.setStatus("obsolete")
_AcSysIPDnsSecondaryServer_Type = IpAddress
_AcSysIPDnsSecondaryServer_Object = MibScalar
acSysIPDnsSecondaryServer = _AcSysIPDnsSecondaryServer_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 3, 1, 9),
    _AcSysIPDnsSecondaryServer_Type()
)
acSysIPDnsSecondaryServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acSysIPDnsSecondaryServer.setStatus("obsolete")


class _AcSysIPDHCPLeaseRenewalEnable_Type(Integer32):
    """Custom type acSysIPDHCPLeaseRenewalEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_AcSysIPDHCPLeaseRenewalEnable_Type.__name__ = "Integer32"
_AcSysIPDHCPLeaseRenewalEnable_Object = MibScalar
acSysIPDHCPLeaseRenewalEnable = _AcSysIPDHCPLeaseRenewalEnable_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 3, 1, 10),
    _AcSysIPDHCPLeaseRenewalEnable_Type()
)
acSysIPDHCPLeaseRenewalEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acSysIPDHCPLeaseRenewalEnable.setStatus("obsolete")


class _AcSysIPWanInterfaceName_Type(SnmpAdminString):
    """Custom type acSysIPWanInterfaceName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 38),
    )


_AcSysIPWanInterfaceName_Type.__name__ = "SnmpAdminString"
_AcSysIPWanInterfaceName_Object = MibScalar
acSysIPWanInterfaceName = _AcSysIPWanInterfaceName_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 3, 1, 11),
    _AcSysIPWanInterfaceName_Type()
)
acSysIPWanInterfaceName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acSysIPWanInterfaceName.setStatus("current")
_AcSysIPV6Address_Type = InetAddress
_AcSysIPV6Address_Object = MibScalar
acSysIPV6Address = _AcSysIPV6Address_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 3, 1, 12),
    _AcSysIPV6Address_Type()
)
acSysIPV6Address.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acSysIPV6Address.setStatus("current")
_AcMultipleIP_ObjectIdentity = ObjectIdentity
acMultipleIP = _AcMultipleIP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 3, 1, 30)
)


class _AcMultipleIPEnable_Type(Integer32):
    """Custom type acMultipleIPEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_AcMultipleIPEnable_Type.__name__ = "Integer32"
_AcMultipleIPEnable_Object = MibScalar
acMultipleIPEnable = _AcMultipleIPEnable_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 3, 1, 30, 1),
    _AcMultipleIPEnable_Type()
)
acMultipleIPEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acMultipleIPEnable.setStatus("obsolete")


class _AcMultipleIPEnableTPNCPasOAM_Type(Integer32):
    """Custom type acMultipleIPEnableTPNCPasOAM based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_AcMultipleIPEnableTPNCPasOAM_Type.__name__ = "Integer32"
_AcMultipleIPEnableTPNCPasOAM_Object = MibScalar
acMultipleIPEnableTPNCPasOAM = _AcMultipleIPEnableTPNCPasOAM_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 3, 1, 30, 2),
    _AcMultipleIPEnableTPNCPasOAM_Type()
)
acMultipleIPEnableTPNCPasOAM.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acMultipleIPEnableTPNCPasOAM.setStatus("current")


class _AcMultipleIPEnableDNSasOAM_Type(Integer32):
    """Custom type acMultipleIPEnableDNSasOAM based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_AcMultipleIPEnableDNSasOAM_Type.__name__ = "Integer32"
_AcMultipleIPEnableDNSasOAM_Object = MibScalar
acMultipleIPEnableDNSasOAM = _AcMultipleIPEnableDNSasOAM_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 3, 1, 30, 3),
    _AcMultipleIPEnableDNSasOAM_Type()
)
acMultipleIPEnableDNSasOAM.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acMultipleIPEnableDNSasOAM.setStatus("current")


class _AcMultipleIPEnableNTPasOAM_Type(Integer32):
    """Custom type acMultipleIPEnableNTPasOAM based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_AcMultipleIPEnableNTPasOAM_Type.__name__ = "Integer32"
_AcMultipleIPEnableNTPasOAM_Object = MibScalar
acMultipleIPEnableNTPasOAM = _AcMultipleIPEnableNTPasOAM_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 3, 1, 30, 4),
    _AcMultipleIPEnableNTPasOAM_Type()
)
acMultipleIPEnableNTPasOAM.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acMultipleIPEnableNTPasOAM.setStatus("current")


class _AcMultipleIPEnableSCTPasControl_Type(Integer32):
    """Custom type acMultipleIPEnableSCTPasControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_AcMultipleIPEnableSCTPasControl_Type.__name__ = "Integer32"
_AcMultipleIPEnableSCTPasControl_Object = MibScalar
acMultipleIPEnableSCTPasControl = _AcMultipleIPEnableSCTPasControl_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 3, 1, 30, 5),
    _AcMultipleIPEnableSCTPasControl_Type()
)
acMultipleIPEnableSCTPasControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acMultipleIPEnableSCTPasControl.setStatus("obsolete")


class _AcMultipleIPEnableNetwotkSeparation_Type(Integer32):
    """Custom type acMultipleIPEnableNetwotkSeparation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_AcMultipleIPEnableNetwotkSeparation_Type.__name__ = "Integer32"
_AcMultipleIPEnableNetwotkSeparation_Object = MibScalar
acMultipleIPEnableNetwotkSeparation = _AcMultipleIPEnableNetwotkSeparation_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 3, 1, 30, 6),
    _AcMultipleIPEnableNetwotkSeparation_Type()
)
acMultipleIPEnableNetwotkSeparation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acMultipleIPEnableNetwotkSeparation.setStatus("current")


class _AcMultipleIPInterfaceTableAction_Type(Integer32):
    """Custom type acMultipleIPInterfaceTableAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("done", 1),
          ("validateConfiguration", 2))
    )


_AcMultipleIPInterfaceTableAction_Type.__name__ = "Integer32"
_AcMultipleIPInterfaceTableAction_Object = MibScalar
acMultipleIPInterfaceTableAction = _AcMultipleIPInterfaceTableAction_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 3, 1, 30, 7),
    _AcMultipleIPInterfaceTableAction_Type()
)
acMultipleIPInterfaceTableAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acMultipleIPInterfaceTableAction.setStatus("current")
_AcNetworkIPTable_Object = MibTable
acNetworkIPTable = _AcNetworkIPTable_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 3, 1, 30, 21)
)
if mibBuilder.loadTexts:
    acNetworkIPTable.setStatus("obsolete")
_AcNetworkIPEntry_Object = MibTableRow
acNetworkIPEntry = _AcNetworkIPEntry_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 3, 1, 30, 21, 1)
)
acNetworkIPEntry.setIndexNames(
    (0, "AC-SYSTEM-MIB", "acNetworkIPIndex"),
)
if mibBuilder.loadTexts:
    acNetworkIPEntry.setStatus("obsolete")


class _AcNetworkIPIndex_Type(Integer32):
    """Custom type acNetworkIPIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("oam", 1),
          ("media", 2),
          ("control", 3))
    )


_AcNetworkIPIndex_Type.__name__ = "Integer32"
_AcNetworkIPIndex_Object = MibTableColumn
acNetworkIPIndex = _AcNetworkIPIndex_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 3, 1, 30, 21, 1, 1),
    _AcNetworkIPIndex_Type()
)
acNetworkIPIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    acNetworkIPIndex.setStatus("obsolete")


class _AcNetworkIPIfIndex_Type(Unsigned32):
    """Custom type acNetworkIPIfIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_AcNetworkIPIfIndex_Type.__name__ = "Unsigned32"
_AcNetworkIPIfIndex_Object = MibTableColumn
acNetworkIPIfIndex = _AcNetworkIPIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 3, 1, 30, 21, 1, 2),
    _AcNetworkIPIfIndex_Type()
)
acNetworkIPIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acNetworkIPIfIndex.setStatus("obsolete")
_AcNetworkIPLocalIPAddress_Type = IpAddress
_AcNetworkIPLocalIPAddress_Object = MibTableColumn
acNetworkIPLocalIPAddress = _AcNetworkIPLocalIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 3, 1, 30, 21, 1, 3),
    _AcNetworkIPLocalIPAddress_Type()
)
acNetworkIPLocalIPAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acNetworkIPLocalIPAddress.setStatus("obsolete")
_AcNetworkIPLocalSubnetMask_Type = IpAddress
_AcNetworkIPLocalSubnetMask_Object = MibTableColumn
acNetworkIPLocalSubnetMask = _AcNetworkIPLocalSubnetMask_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 3, 1, 30, 21, 1, 4),
    _AcNetworkIPLocalSubnetMask_Type()
)
acNetworkIPLocalSubnetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acNetworkIPLocalSubnetMask.setStatus("obsolete")
_AcNetworkIPLocalDefGW_Type = IpAddress
_AcNetworkIPLocalDefGW_Object = MibTableColumn
acNetworkIPLocalDefGW = _AcNetworkIPLocalDefGW_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 3, 1, 30, 21, 1, 5),
    _AcNetworkIPLocalDefGW_Type()
)
acNetworkIPLocalDefGW.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acNetworkIPLocalDefGW.setStatus("obsolete")


class _AcNetworkIPAdminState_Type(Integer32):
    """Custom type acNetworkIPAdminState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("lock", 1),
          ("unLock", 2))
    )


_AcNetworkIPAdminState_Type.__name__ = "Integer32"
_AcNetworkIPAdminState_Object = MibTableColumn
acNetworkIPAdminState = _AcNetworkIPAdminState_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 3, 1, 30, 21, 1, 6),
    _AcNetworkIPAdminState_Type()
)
acNetworkIPAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acNetworkIPAdminState.setStatus("obsolete")
_AcSysInterfaceTable_Object = MibTable
acSysInterfaceTable = _AcSysInterfaceTable_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 3, 1, 30, 22)
)
if mibBuilder.loadTexts:
    acSysInterfaceTable.setStatus("current")
_AcSysInterfaceEntry_Object = MibTableRow
acSysInterfaceEntry = _AcSysInterfaceEntry_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 3, 1, 30, 22, 1)
)
acSysInterfaceEntry.setIndexNames(
    (0, "AC-SYSTEM-MIB", "acSysInterfaceIndex"),
)
if mibBuilder.loadTexts:
    acSysInterfaceEntry.setStatus("current")


class _AcSysInterfaceIndex_Type(Unsigned32):
    """Custom type acSysInterfaceIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_AcSysInterfaceIndex_Type.__name__ = "Unsigned32"
_AcSysInterfaceIndex_Object = MibTableColumn
acSysInterfaceIndex = _AcSysInterfaceIndex_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 3, 1, 30, 22, 1, 1),
    _AcSysInterfaceIndex_Type()
)
acSysInterfaceIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    acSysInterfaceIndex.setStatus("current")
_AcSysInterfaceRowStatus_Type = RowStatus
_AcSysInterfaceRowStatus_Object = MibTableColumn
acSysInterfaceRowStatus = _AcSysInterfaceRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 3, 1, 30, 22, 1, 2),
    _AcSysInterfaceRowStatus_Type()
)
acSysInterfaceRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acSysInterfaceRowStatus.setStatus("current")


class _AcSysInterfaceAction_Type(Integer32):
    """Custom type acSysInterfaceAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            0
        )
    )
    namedValues = NamedValues(
        ("none", 0)
    )


_AcSysInterfaceAction_Type.__name__ = "Integer32"
_AcSysInterfaceAction_Object = MibTableColumn
acSysInterfaceAction = _AcSysInterfaceAction_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 3, 1, 30, 22, 1, 3),
    _AcSysInterfaceAction_Type()
)
acSysInterfaceAction.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acSysInterfaceAction.setStatus("current")


class _AcSysInterfaceActionRes_Type(Integer32):
    """Custom type acSysInterfaceActionRes based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            0
        )
    )
    namedValues = NamedValues(
        ("succeeded", 0)
    )


_AcSysInterfaceActionRes_Type.__name__ = "Integer32"
_AcSysInterfaceActionRes_Object = MibTableColumn
acSysInterfaceActionRes = _AcSysInterfaceActionRes_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 3, 1, 30, 22, 1, 4),
    _AcSysInterfaceActionRes_Type()
)
acSysInterfaceActionRes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSysInterfaceActionRes.setStatus("current")


class _AcSysInterfaceApplicationTypes_Type(Integer32):
    """Custom type acSysInterfaceApplicationTypes based on Integer32"""
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
              99)
        )
    )
    namedValues = NamedValues(
        *(("oam", 0),
          ("media", 1),
          ("control", 2),
          ("oamAndMedia", 3),
          ("oamAndControl", 4),
          ("mediaAndControl", 5),
          ("oamAndMediaAndControl", 6),
          ("maintenance", 99))
    )


_AcSysInterfaceApplicationTypes_Type.__name__ = "Integer32"
_AcSysInterfaceApplicationTypes_Object = MibTableColumn
acSysInterfaceApplicationTypes = _AcSysInterfaceApplicationTypes_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 3, 1, 30, 22, 1, 5),
    _AcSysInterfaceApplicationTypes_Type()
)
acSysInterfaceApplicationTypes.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acSysInterfaceApplicationTypes.setStatus("current")


class _AcSysInterfaceMode_Type(Integer32):
    """Custom type acSysInterfaceMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(3,
              4,
              10)
        )
    )
    namedValues = NamedValues(
        *(("iPv6PrefixManual", 3),
          ("iPv6Manual", 4),
          ("iPv4Manual", 10))
    )


_AcSysInterfaceMode_Type.__name__ = "Integer32"
_AcSysInterfaceMode_Object = MibTableColumn
acSysInterfaceMode = _AcSysInterfaceMode_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 3, 1, 30, 22, 1, 6),
    _AcSysInterfaceMode_Type()
)
acSysInterfaceMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acSysInterfaceMode.setStatus("current")


class _AcSysInterfaceIPAddress_Type(SnmpAdminString):
    """Custom type acSysInterfaceIPAddress based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 45),
    )


_AcSysInterfaceIPAddress_Type.__name__ = "SnmpAdminString"
_AcSysInterfaceIPAddress_Object = MibTableColumn
acSysInterfaceIPAddress = _AcSysInterfaceIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 3, 1, 30, 22, 1, 7),
    _AcSysInterfaceIPAddress_Type()
)
acSysInterfaceIPAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acSysInterfaceIPAddress.setStatus("current")


class _AcSysInterfacePrefixLength_Type(Unsigned32):
    """Custom type acSysInterfacePrefixLength based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_AcSysInterfacePrefixLength_Type.__name__ = "Unsigned32"
_AcSysInterfacePrefixLength_Object = MibTableColumn
acSysInterfacePrefixLength = _AcSysInterfacePrefixLength_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 3, 1, 30, 22, 1, 8),
    _AcSysInterfacePrefixLength_Type()
)
acSysInterfacePrefixLength.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acSysInterfacePrefixLength.setStatus("current")


class _AcSysInterfaceGateway_Type(SnmpAdminString):
    """Custom type acSysInterfaceGateway based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 45),
    )


_AcSysInterfaceGateway_Type.__name__ = "SnmpAdminString"
_AcSysInterfaceGateway_Object = MibTableColumn
acSysInterfaceGateway = _AcSysInterfaceGateway_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 3, 1, 30, 22, 1, 9),
    _AcSysInterfaceGateway_Type()
)
acSysInterfaceGateway.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acSysInterfaceGateway.setStatus("current")


class _AcSysInterfaceVlanID_Type(Unsigned32):
    """Custom type acSysInterfaceVlanID based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_AcSysInterfaceVlanID_Type.__name__ = "Unsigned32"
_AcSysInterfaceVlanID_Object = MibTableColumn
acSysInterfaceVlanID = _AcSysInterfaceVlanID_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 3, 1, 30, 22, 1, 10),
    _AcSysInterfaceVlanID_Type()
)
acSysInterfaceVlanID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acSysInterfaceVlanID.setStatus("current")


class _AcSysInterfaceName_Type(SnmpAdminString):
    """Custom type acSysInterfaceName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_AcSysInterfaceName_Type.__name__ = "SnmpAdminString"
_AcSysInterfaceName_Object = MibTableColumn
acSysInterfaceName = _AcSysInterfaceName_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 3, 1, 30, 22, 1, 11),
    _AcSysInterfaceName_Type()
)
acSysInterfaceName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acSysInterfaceName.setStatus("current")


class _AcSysInterfacePrimaryDNSServerIPAddress_Type(SnmpAdminString):
    """Custom type acSysInterfacePrimaryDNSServerIPAddress based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 45),
    )


_AcSysInterfacePrimaryDNSServerIPAddress_Type.__name__ = "SnmpAdminString"
_AcSysInterfacePrimaryDNSServerIPAddress_Object = MibTableColumn
acSysInterfacePrimaryDNSServerIPAddress = _AcSysInterfacePrimaryDNSServerIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 3, 1, 30, 22, 1, 12),
    _AcSysInterfacePrimaryDNSServerIPAddress_Type()
)
acSysInterfacePrimaryDNSServerIPAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acSysInterfacePrimaryDNSServerIPAddress.setStatus("current")


class _AcSysInterfaceSecondaryDNSServerIPAddress_Type(SnmpAdminString):
    """Custom type acSysInterfaceSecondaryDNSServerIPAddress based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 45),
    )


_AcSysInterfaceSecondaryDNSServerIPAddress_Type.__name__ = "SnmpAdminString"
_AcSysInterfaceSecondaryDNSServerIPAddress_Object = MibTableColumn
acSysInterfaceSecondaryDNSServerIPAddress = _AcSysInterfaceSecondaryDNSServerIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 3, 1, 30, 22, 1, 13),
    _AcSysInterfaceSecondaryDNSServerIPAddress_Type()
)
acSysInterfaceSecondaryDNSServerIPAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acSysInterfaceSecondaryDNSServerIPAddress.setStatus("current")
_AcSysInterfaceUnderlyingInterface_Type = RowPointer
_AcSysInterfaceUnderlyingInterface_Object = MibTableColumn
acSysInterfaceUnderlyingInterface = _AcSysInterfaceUnderlyingInterface_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 3, 1, 30, 22, 1, 14),
    _AcSysInterfaceUnderlyingInterface_Type()
)
acSysInterfaceUnderlyingInterface.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acSysInterfaceUnderlyingInterface.setStatus("current")
_AcSysInterfaceUnderlyingDevice_Type = RowPointer
_AcSysInterfaceUnderlyingDevice_Object = MibTableColumn
acSysInterfaceUnderlyingDevice = _AcSysInterfaceUnderlyingDevice_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 3, 1, 30, 22, 1, 15),
    _AcSysInterfaceUnderlyingDevice_Type()
)
acSysInterfaceUnderlyingDevice.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acSysInterfaceUnderlyingDevice.setStatus("current")
_AcSysPhysicalPortsTable_Object = MibTable
acSysPhysicalPortsTable = _AcSysPhysicalPortsTable_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 3, 1, 30, 23)
)
if mibBuilder.loadTexts:
    acSysPhysicalPortsTable.setStatus("current")
_AcSysPhysicalPortsEntry_Object = MibTableRow
acSysPhysicalPortsEntry = _AcSysPhysicalPortsEntry_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 3, 1, 30, 23, 1)
)
acSysPhysicalPortsEntry.setIndexNames(
    (0, "AC-SYSTEM-MIB", "acSysPhysicalPortsIndex"),
)
if mibBuilder.loadTexts:
    acSysPhysicalPortsEntry.setStatus("current")


class _AcSysPhysicalPortsIndex_Type(Unsigned32):
    """Custom type acSysPhysicalPortsIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5),
    )


_AcSysPhysicalPortsIndex_Type.__name__ = "Unsigned32"
_AcSysPhysicalPortsIndex_Object = MibTableColumn
acSysPhysicalPortsIndex = _AcSysPhysicalPortsIndex_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 3, 1, 30, 23, 1, 1),
    _AcSysPhysicalPortsIndex_Type()
)
acSysPhysicalPortsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    acSysPhysicalPortsIndex.setStatus("current")
_AcSysPhysicalPortsRowStatus_Type = RowStatus
_AcSysPhysicalPortsRowStatus_Object = MibTableColumn
acSysPhysicalPortsRowStatus = _AcSysPhysicalPortsRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 3, 1, 30, 23, 1, 2),
    _AcSysPhysicalPortsRowStatus_Type()
)
acSysPhysicalPortsRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acSysPhysicalPortsRowStatus.setStatus("current")


class _AcSysPhysicalPortsAction_Type(Integer32):
    """Custom type acSysPhysicalPortsAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            0
        )
    )
    namedValues = NamedValues(
        ("none", 0)
    )


_AcSysPhysicalPortsAction_Type.__name__ = "Integer32"
_AcSysPhysicalPortsAction_Object = MibTableColumn
acSysPhysicalPortsAction = _AcSysPhysicalPortsAction_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 3, 1, 30, 23, 1, 3),
    _AcSysPhysicalPortsAction_Type()
)
acSysPhysicalPortsAction.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acSysPhysicalPortsAction.setStatus("current")


class _AcSysPhysicalPortsActionRes_Type(Integer32):
    """Custom type acSysPhysicalPortsActionRes based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            0
        )
    )
    namedValues = NamedValues(
        ("succeeded", 0)
    )


_AcSysPhysicalPortsActionRes_Type.__name__ = "Integer32"
_AcSysPhysicalPortsActionRes_Object = MibTableColumn
acSysPhysicalPortsActionRes = _AcSysPhysicalPortsActionRes_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 3, 1, 30, 23, 1, 4),
    _AcSysPhysicalPortsActionRes_Type()
)
acSysPhysicalPortsActionRes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSysPhysicalPortsActionRes.setStatus("current")


class _AcSysPhysicalPortsPort_Type(SnmpAdminString):
    """Custom type acSysPhysicalPortsPort based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 17),
    )


_AcSysPhysicalPortsPort_Type.__name__ = "SnmpAdminString"
_AcSysPhysicalPortsPort_Object = MibTableColumn
acSysPhysicalPortsPort = _AcSysPhysicalPortsPort_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 3, 1, 30, 23, 1, 5),
    _AcSysPhysicalPortsPort_Type()
)
acSysPhysicalPortsPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSysPhysicalPortsPort.setStatus("current")


class _AcSysPhysicalPortsMode_Type(Integer32):
    """Custom type acSysPhysicalPortsMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_AcSysPhysicalPortsMode_Type.__name__ = "Integer32"
_AcSysPhysicalPortsMode_Object = MibTableColumn
acSysPhysicalPortsMode = _AcSysPhysicalPortsMode_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 3, 1, 30, 23, 1, 6),
    _AcSysPhysicalPortsMode_Type()
)
acSysPhysicalPortsMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSysPhysicalPortsMode.setStatus("current")


class _AcSysPhysicalPortsNativeVlan_Type(Unsigned32):
    """Custom type acSysPhysicalPortsNativeVlan based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4096),
    )


_AcSysPhysicalPortsNativeVlan_Type.__name__ = "Unsigned32"
_AcSysPhysicalPortsNativeVlan_Object = MibTableColumn
acSysPhysicalPortsNativeVlan = _AcSysPhysicalPortsNativeVlan_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 3, 1, 30, 23, 1, 7),
    _AcSysPhysicalPortsNativeVlan_Type()
)
acSysPhysicalPortsNativeVlan.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acSysPhysicalPortsNativeVlan.setStatus("current")


class _AcSysPhysicalPortsSpeedDuplex_Type(Integer32):
    """Custom type acSysPhysicalPortsSpeedDuplex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("s10BaseTHalfDuplex", 0),
          ("s10BaseTFullDuplex", 1),
          ("s100BaseTHalfDuplex", 2),
          ("s100BaseTFullDuplex", 3),
          ("autoNegotiation", 4),
          ("s1000BaseTHalfDuplex", 6),
          ("s1000BaseTFullDuplex", 7))
    )


_AcSysPhysicalPortsSpeedDuplex_Type.__name__ = "Integer32"
_AcSysPhysicalPortsSpeedDuplex_Object = MibTableColumn
acSysPhysicalPortsSpeedDuplex = _AcSysPhysicalPortsSpeedDuplex_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 3, 1, 30, 23, 1, 8),
    _AcSysPhysicalPortsSpeedDuplex_Type()
)
acSysPhysicalPortsSpeedDuplex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acSysPhysicalPortsSpeedDuplex.setStatus("current")


class _AcSysPhysicalPortsPortDescription_Type(SnmpAdminString):
    """Custom type acSysPhysicalPortsPortDescription based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 17),
    )


_AcSysPhysicalPortsPortDescription_Type.__name__ = "SnmpAdminString"
_AcSysPhysicalPortsPortDescription_Object = MibTableColumn
acSysPhysicalPortsPortDescription = _AcSysPhysicalPortsPortDescription_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 3, 1, 30, 23, 1, 9),
    _AcSysPhysicalPortsPortDescription_Type()
)
acSysPhysicalPortsPortDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acSysPhysicalPortsPortDescription.setStatus("current")


class _AcSysPhysicalPortsGroupMember_Type(SnmpAdminString):
    """Custom type acSysPhysicalPortsGroupMember based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 17),
    )


_AcSysPhysicalPortsGroupMember_Type.__name__ = "SnmpAdminString"
_AcSysPhysicalPortsGroupMember_Object = MibTableColumn
acSysPhysicalPortsGroupMember = _AcSysPhysicalPortsGroupMember_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 3, 1, 30, 23, 1, 10),
    _AcSysPhysicalPortsGroupMember_Type()
)
acSysPhysicalPortsGroupMember.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSysPhysicalPortsGroupMember.setStatus("current")


class _AcSysPhysicalPortsGroupStatus_Type(SnmpAdminString):
    """Custom type acSysPhysicalPortsGroupStatus based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 17),
    )


_AcSysPhysicalPortsGroupStatus_Type.__name__ = "SnmpAdminString"
_AcSysPhysicalPortsGroupStatus_Object = MibTableColumn
acSysPhysicalPortsGroupStatus = _AcSysPhysicalPortsGroupStatus_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 3, 1, 30, 23, 1, 11),
    _AcSysPhysicalPortsGroupStatus_Type()
)
acSysPhysicalPortsGroupStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSysPhysicalPortsGroupStatus.setStatus("current")
_AcSysEtherGroupTable_Object = MibTable
acSysEtherGroupTable = _AcSysEtherGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 3, 1, 30, 24)
)
if mibBuilder.loadTexts:
    acSysEtherGroupTable.setStatus("current")
_AcSysEtherGroupEntry_Object = MibTableRow
acSysEtherGroupEntry = _AcSysEtherGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 3, 1, 30, 24, 1)
)
acSysEtherGroupEntry.setIndexNames(
    (0, "AC-SYSTEM-MIB", "acSysEtherGroupIndex"),
)
if mibBuilder.loadTexts:
    acSysEtherGroupEntry.setStatus("current")


class _AcSysEtherGroupIndex_Type(Unsigned32):
    """Custom type acSysEtherGroupIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5),
    )


_AcSysEtherGroupIndex_Type.__name__ = "Unsigned32"
_AcSysEtherGroupIndex_Object = MibTableColumn
acSysEtherGroupIndex = _AcSysEtherGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 3, 1, 30, 24, 1, 1),
    _AcSysEtherGroupIndex_Type()
)
acSysEtherGroupIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    acSysEtherGroupIndex.setStatus("current")
_AcSysEtherGroupRowStatus_Type = RowStatus
_AcSysEtherGroupRowStatus_Object = MibTableColumn
acSysEtherGroupRowStatus = _AcSysEtherGroupRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 3, 1, 30, 24, 1, 2),
    _AcSysEtherGroupRowStatus_Type()
)
acSysEtherGroupRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acSysEtherGroupRowStatus.setStatus("current")


class _AcSysEtherGroupAction_Type(Integer32):
    """Custom type acSysEtherGroupAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            0
        )
    )
    namedValues = NamedValues(
        ("none", 0)
    )


_AcSysEtherGroupAction_Type.__name__ = "Integer32"
_AcSysEtherGroupAction_Object = MibTableColumn
acSysEtherGroupAction = _AcSysEtherGroupAction_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 3, 1, 30, 24, 1, 3),
    _AcSysEtherGroupAction_Type()
)
acSysEtherGroupAction.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acSysEtherGroupAction.setStatus("current")


class _AcSysEtherGroupActionRes_Type(Integer32):
    """Custom type acSysEtherGroupActionRes based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            0
        )
    )
    namedValues = NamedValues(
        ("succeeded", 0)
    )


_AcSysEtherGroupActionRes_Type.__name__ = "Integer32"
_AcSysEtherGroupActionRes_Object = MibTableColumn
acSysEtherGroupActionRes = _AcSysEtherGroupActionRes_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 3, 1, 30, 24, 1, 4),
    _AcSysEtherGroupActionRes_Type()
)
acSysEtherGroupActionRes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSysEtherGroupActionRes.setStatus("current")


class _AcSysEtherGroupGroup_Type(SnmpAdminString):
    """Custom type acSysEtherGroupGroup based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_AcSysEtherGroupGroup_Type.__name__ = "SnmpAdminString"
_AcSysEtherGroupGroup_Object = MibTableColumn
acSysEtherGroupGroup = _AcSysEtherGroupGroup_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 3, 1, 30, 24, 1, 5),
    _AcSysEtherGroupGroup_Type()
)
acSysEtherGroupGroup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSysEtherGroupGroup.setStatus("current")


class _AcSysEtherGroupMode_Type(Integer32):
    """Custom type acSysEtherGroupMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("oneRXoneTX", 2),
          ("twoRXoneTX", 3),
          ("twoRXtwoTX", 4))
    )


_AcSysEtherGroupMode_Type.__name__ = "Integer32"
_AcSysEtherGroupMode_Object = MibTableColumn
acSysEtherGroupMode = _AcSysEtherGroupMode_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 3, 1, 30, 24, 1, 6),
    _AcSysEtherGroupMode_Type()
)
acSysEtherGroupMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acSysEtherGroupMode.setStatus("current")
_AcSysEtherGroupMember1_Type = RowPointer
_AcSysEtherGroupMember1_Object = MibTableColumn
acSysEtherGroupMember1 = _AcSysEtherGroupMember1_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 3, 1, 30, 24, 1, 7),
    _AcSysEtherGroupMember1_Type()
)
acSysEtherGroupMember1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acSysEtherGroupMember1.setStatus("current")
_AcSysEtherGroupMember2_Type = RowPointer
_AcSysEtherGroupMember2_Object = MibTableColumn
acSysEtherGroupMember2 = _AcSysEtherGroupMember2_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 3, 1, 30, 24, 1, 8),
    _AcSysEtherGroupMember2_Type()
)
acSysEtherGroupMember2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acSysEtherGroupMember2.setStatus("current")
_AcSysStaticRouteTable_Object = MibTable
acSysStaticRouteTable = _AcSysStaticRouteTable_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 3, 1, 30, 25)
)
if mibBuilder.loadTexts:
    acSysStaticRouteTable.setStatus("current")
_AcSysStaticRouteEntry_Object = MibTableRow
acSysStaticRouteEntry = _AcSysStaticRouteEntry_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 3, 1, 30, 25, 1)
)
acSysStaticRouteEntry.setIndexNames(
    (0, "AC-SYSTEM-MIB", "acSysStaticRouteIndex"),
)
if mibBuilder.loadTexts:
    acSysStaticRouteEntry.setStatus("current")


class _AcSysStaticRouteIndex_Type(Unsigned32):
    """Custom type acSysStaticRouteIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 200),
    )


_AcSysStaticRouteIndex_Type.__name__ = "Unsigned32"
_AcSysStaticRouteIndex_Object = MibTableColumn
acSysStaticRouteIndex = _AcSysStaticRouteIndex_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 3, 1, 30, 25, 1, 1),
    _AcSysStaticRouteIndex_Type()
)
acSysStaticRouteIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    acSysStaticRouteIndex.setStatus("current")
_AcSysStaticRouteRowStatus_Type = RowStatus
_AcSysStaticRouteRowStatus_Object = MibTableColumn
acSysStaticRouteRowStatus = _AcSysStaticRouteRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 3, 1, 30, 25, 1, 2),
    _AcSysStaticRouteRowStatus_Type()
)
acSysStaticRouteRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acSysStaticRouteRowStatus.setStatus("current")


class _AcSysStaticRouteAction_Type(Integer32):
    """Custom type acSysStaticRouteAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            0
        )
    )
    namedValues = NamedValues(
        ("none", 0)
    )


_AcSysStaticRouteAction_Type.__name__ = "Integer32"
_AcSysStaticRouteAction_Object = MibTableColumn
acSysStaticRouteAction = _AcSysStaticRouteAction_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 3, 1, 30, 25, 1, 3),
    _AcSysStaticRouteAction_Type()
)
acSysStaticRouteAction.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acSysStaticRouteAction.setStatus("current")


class _AcSysStaticRouteActionRes_Type(Integer32):
    """Custom type acSysStaticRouteActionRes based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            0
        )
    )
    namedValues = NamedValues(
        ("succeeded", 0)
    )


_AcSysStaticRouteActionRes_Type.__name__ = "Integer32"
_AcSysStaticRouteActionRes_Object = MibTableColumn
acSysStaticRouteActionRes = _AcSysStaticRouteActionRes_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 3, 1, 30, 25, 1, 4),
    _AcSysStaticRouteActionRes_Type()
)
acSysStaticRouteActionRes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSysStaticRouteActionRes.setStatus("current")


class _AcSysStaticRouteInterfaceName_Type(SnmpAdminString):
    """Custom type acSysStaticRouteInterfaceName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_AcSysStaticRouteInterfaceName_Type.__name__ = "SnmpAdminString"
_AcSysStaticRouteInterfaceName_Object = MibTableColumn
acSysStaticRouteInterfaceName = _AcSysStaticRouteInterfaceName_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 3, 1, 30, 25, 1, 5),
    _AcSysStaticRouteInterfaceName_Type()
)
acSysStaticRouteInterfaceName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acSysStaticRouteInterfaceName.setStatus("current")
_AcSysStaticRouteDeviceName_Type = RowPointer
_AcSysStaticRouteDeviceName_Object = MibTableColumn
acSysStaticRouteDeviceName = _AcSysStaticRouteDeviceName_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 3, 1, 30, 25, 1, 6),
    _AcSysStaticRouteDeviceName_Type()
)
acSysStaticRouteDeviceName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acSysStaticRouteDeviceName.setStatus("current")


class _AcSysStaticRouteDestination_Type(SnmpAdminString):
    """Custom type acSysStaticRouteDestination based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 45),
    )


_AcSysStaticRouteDestination_Type.__name__ = "SnmpAdminString"
_AcSysStaticRouteDestination_Object = MibTableColumn
acSysStaticRouteDestination = _AcSysStaticRouteDestination_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 3, 1, 30, 25, 1, 7),
    _AcSysStaticRouteDestination_Type()
)
acSysStaticRouteDestination.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acSysStaticRouteDestination.setStatus("current")


class _AcSysStaticRoutePrefixLength_Type(Unsigned32):
    """Custom type acSysStaticRoutePrefixLength based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_AcSysStaticRoutePrefixLength_Type.__name__ = "Unsigned32"
_AcSysStaticRoutePrefixLength_Object = MibTableColumn
acSysStaticRoutePrefixLength = _AcSysStaticRoutePrefixLength_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 3, 1, 30, 25, 1, 8),
    _AcSysStaticRoutePrefixLength_Type()
)
acSysStaticRoutePrefixLength.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acSysStaticRoutePrefixLength.setStatus("current")


class _AcSysStaticRouteGateway_Type(SnmpAdminString):
    """Custom type acSysStaticRouteGateway based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 45),
    )


_AcSysStaticRouteGateway_Type.__name__ = "SnmpAdminString"
_AcSysStaticRouteGateway_Object = MibTableColumn
acSysStaticRouteGateway = _AcSysStaticRouteGateway_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 3, 1, 30, 25, 1, 9),
    _AcSysStaticRouteGateway_Type()
)
acSysStaticRouteGateway.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acSysStaticRouteGateway.setStatus("current")


class _AcSysStaticRouteDescription_Type(SnmpAdminString):
    """Custom type acSysStaticRouteDescription based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 29),
    )


_AcSysStaticRouteDescription_Type.__name__ = "SnmpAdminString"
_AcSysStaticRouteDescription_Object = MibTableColumn
acSysStaticRouteDescription = _AcSysStaticRouteDescription_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 3, 1, 30, 25, 1, 10),
    _AcSysStaticRouteDescription_Type()
)
acSysStaticRouteDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acSysStaticRouteDescription.setStatus("current")
_AcSysEthernetDeviceTable_Object = MibTable
acSysEthernetDeviceTable = _AcSysEthernetDeviceTable_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 3, 1, 30, 26)
)
if mibBuilder.loadTexts:
    acSysEthernetDeviceTable.setStatus("current")
_AcSysEthernetDeviceEntry_Object = MibTableRow
acSysEthernetDeviceEntry = _AcSysEthernetDeviceEntry_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 3, 1, 30, 26, 1)
)
acSysEthernetDeviceEntry.setIndexNames(
    (0, "AC-SYSTEM-MIB", "acSysEthernetDeviceIndex"),
)
if mibBuilder.loadTexts:
    acSysEthernetDeviceEntry.setStatus("current")


class _AcSysEthernetDeviceIndex_Type(Unsigned32):
    """Custom type acSysEthernetDeviceIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_AcSysEthernetDeviceIndex_Type.__name__ = "Unsigned32"
_AcSysEthernetDeviceIndex_Object = MibTableColumn
acSysEthernetDeviceIndex = _AcSysEthernetDeviceIndex_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 3, 1, 30, 26, 1, 1),
    _AcSysEthernetDeviceIndex_Type()
)
acSysEthernetDeviceIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    acSysEthernetDeviceIndex.setStatus("current")
_AcSysEthernetDeviceRowStatus_Type = RowStatus
_AcSysEthernetDeviceRowStatus_Object = MibTableColumn
acSysEthernetDeviceRowStatus = _AcSysEthernetDeviceRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 3, 1, 30, 26, 1, 2),
    _AcSysEthernetDeviceRowStatus_Type()
)
acSysEthernetDeviceRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acSysEthernetDeviceRowStatus.setStatus("current")


class _AcSysEthernetDeviceAction_Type(Integer32):
    """Custom type acSysEthernetDeviceAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            0
        )
    )
    namedValues = NamedValues(
        ("none", 0)
    )


_AcSysEthernetDeviceAction_Type.__name__ = "Integer32"
_AcSysEthernetDeviceAction_Object = MibTableColumn
acSysEthernetDeviceAction = _AcSysEthernetDeviceAction_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 3, 1, 30, 26, 1, 3),
    _AcSysEthernetDeviceAction_Type()
)
acSysEthernetDeviceAction.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acSysEthernetDeviceAction.setStatus("current")


class _AcSysEthernetDeviceActionRes_Type(Integer32):
    """Custom type acSysEthernetDeviceActionRes based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            0
        )
    )
    namedValues = NamedValues(
        ("succeeded", 0)
    )


_AcSysEthernetDeviceActionRes_Type.__name__ = "Integer32"
_AcSysEthernetDeviceActionRes_Object = MibTableColumn
acSysEthernetDeviceActionRes = _AcSysEthernetDeviceActionRes_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 3, 1, 30, 26, 1, 4),
    _AcSysEthernetDeviceActionRes_Type()
)
acSysEthernetDeviceActionRes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSysEthernetDeviceActionRes.setStatus("current")


class _AcSysEthernetDeviceVlanID_Type(Unsigned32):
    """Custom type acSysEthernetDeviceVlanID based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_AcSysEthernetDeviceVlanID_Type.__name__ = "Unsigned32"
_AcSysEthernetDeviceVlanID_Object = MibTableColumn
acSysEthernetDeviceVlanID = _AcSysEthernetDeviceVlanID_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 3, 1, 30, 26, 1, 5),
    _AcSysEthernetDeviceVlanID_Type()
)
acSysEthernetDeviceVlanID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acSysEthernetDeviceVlanID.setStatus("current")
_AcSysEthernetDeviceUnderlyingInterface_Type = RowPointer
_AcSysEthernetDeviceUnderlyingInterface_Object = MibTableColumn
acSysEthernetDeviceUnderlyingInterface = _AcSysEthernetDeviceUnderlyingInterface_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 3, 1, 30, 26, 1, 6),
    _AcSysEthernetDeviceUnderlyingInterface_Type()
)
acSysEthernetDeviceUnderlyingInterface.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acSysEthernetDeviceUnderlyingInterface.setStatus("current")


class _AcSysEthernetDeviceName_Type(SnmpAdminString):
    """Custom type acSysEthernetDeviceName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_AcSysEthernetDeviceName_Type.__name__ = "SnmpAdminString"
_AcSysEthernetDeviceName_Object = MibTableColumn
acSysEthernetDeviceName = _AcSysEthernetDeviceName_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 3, 1, 30, 26, 1, 7),
    _AcSysEthernetDeviceName_Type()
)
acSysEthernetDeviceName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acSysEthernetDeviceName.setStatus("current")
_AcSyslog_ObjectIdentity = ObjectIdentity
acSyslog = _AcSyslog_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 3, 2)
)
_AcSyslogServerIPAddress_Type = IpAddress
_AcSyslogServerIPAddress_Object = MibScalar
acSyslogServerIPAddress = _AcSyslogServerIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 3, 2, 1),
    _AcSyslogServerIPAddress_Type()
)
acSyslogServerIPAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acSyslogServerIPAddress.setStatus("deprecated")


class _AcSyslogEnable_Type(Integer32):
    """Custom type acSyslogEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_AcSyslogEnable_Type.__name__ = "Integer32"
_AcSyslogEnable_Object = MibScalar
acSyslogEnable = _AcSyslogEnable_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 3, 2, 2),
    _AcSyslogEnable_Type()
)
acSyslogEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acSyslogEnable.setStatus("current")


class _AcSyslogAcSyslogServerPortNumber_Type(Unsigned32):
    """Custom type acSyslogAcSyslogServerPortNumber based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AcSyslogAcSyslogServerPortNumber_Type.__name__ = "Unsigned32"
_AcSyslogAcSyslogServerPortNumber_Object = MibScalar
acSyslogAcSyslogServerPortNumber = _AcSyslogAcSyslogServerPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 3, 2, 3),
    _AcSyslogAcSyslogServerPortNumber_Type()
)
acSyslogAcSyslogServerPortNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acSyslogAcSyslogServerPortNumber.setStatus("current")


class _AcSyslogFacility_Type(Unsigned32):
    """Custom type acSyslogFacility based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(16, 23),
    )


_AcSyslogFacility_Type.__name__ = "Unsigned32"
_AcSyslogFacility_Object = MibScalar
acSyslogFacility = _AcSyslogFacility_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 3, 2, 4),
    _AcSyslogFacility_Type()
)
acSyslogFacility.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acSyslogFacility.setStatus("obsolete")
_AcSysNTP_ObjectIdentity = ObjectIdentity
acSysNTP = _AcSysNTP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 3, 3)
)
_AcSysNTPServerIPAddress_Type = IpAddress
_AcSysNTPServerIPAddress_Object = MibScalar
acSysNTPServerIPAddress = _AcSysNTPServerIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 3, 3, 1),
    _AcSysNTPServerIPAddress_Type()
)
acSysNTPServerIPAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acSysNTPServerIPAddress.setStatus("obsolete")


class _AcSysNTPUtcOffset_Type(Integer32):
    """Custom type acSysNTPUtcOffset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-86400, 86400),
    )


_AcSysNTPUtcOffset_Type.__name__ = "Integer32"
_AcSysNTPUtcOffset_Object = MibScalar
acSysNTPUtcOffset = _AcSysNTPUtcOffset_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 3, 3, 2),
    _AcSysNTPUtcOffset_Type()
)
acSysNTPUtcOffset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acSysNTPUtcOffset.setStatus("current")


class _AcSysNTPUpdateInterval_Type(Unsigned32):
    """Custom type acSysNTPUpdateInterval based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_AcSysNTPUpdateInterval_Type.__name__ = "Unsigned32"
_AcSysNTPUpdateInterval_Object = MibScalar
acSysNTPUpdateInterval = _AcSysNTPUpdateInterval_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 3, 3, 3),
    _AcSysNTPUpdateInterval_Type()
)
acSysNTPUpdateInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acSysNTPUpdateInterval.setStatus("current")
_AcSysNTPSecondaryServerIP_Type = IpAddress
_AcSysNTPSecondaryServerIP_Object = MibScalar
acSysNTPSecondaryServerIP = _AcSysNTPSecondaryServerIP_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 3, 3, 4),
    _AcSysNTPSecondaryServerIP_Type()
)
acSysNTPSecondaryServerIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acSysNTPSecondaryServerIP.setStatus("obsolete")


class _AcSysNTPAuthKeyId_Type(Integer32):
    """Custom type acSysNTPAuthKeyId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_AcSysNTPAuthKeyId_Type.__name__ = "Integer32"
_AcSysNTPAuthKeyId_Object = MibScalar
acSysNTPAuthKeyId = _AcSysNTPAuthKeyId_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 3, 3, 5),
    _AcSysNTPAuthKeyId_Type()
)
acSysNTPAuthKeyId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acSysNTPAuthKeyId.setStatus("current")


class _AcSysNTPAuthMd5Key_Type(SnmpAdminString):
    """Custom type acSysNTPAuthMd5Key based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_AcSysNTPAuthMd5Key_Type.__name__ = "SnmpAdminString"
_AcSysNTPAuthMd5Key_Object = MibScalar
acSysNTPAuthMd5Key = _AcSysNTPAuthMd5Key_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 3, 3, 6),
    _AcSysNTPAuthMd5Key_Type()
)
acSysNTPAuthMd5Key.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acSysNTPAuthMd5Key.setStatus("current")


class _AcSysNTPPrimaryServerAddress_Type(SnmpAdminString):
    """Custom type acSysNTPPrimaryServerAddress based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 100),
    )


_AcSysNTPPrimaryServerAddress_Type.__name__ = "SnmpAdminString"
_AcSysNTPPrimaryServerAddress_Object = MibScalar
acSysNTPPrimaryServerAddress = _AcSysNTPPrimaryServerAddress_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 3, 3, 7),
    _AcSysNTPPrimaryServerAddress_Type()
)
acSysNTPPrimaryServerAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acSysNTPPrimaryServerAddress.setStatus("current")


class _AcSysNTPSecondaryServerAddress_Type(SnmpAdminString):
    """Custom type acSysNTPSecondaryServerAddress based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 100),
    )


_AcSysNTPSecondaryServerAddress_Type.__name__ = "SnmpAdminString"
_AcSysNTPSecondaryServerAddress_Object = MibScalar
acSysNTPSecondaryServerAddress = _AcSysNTPSecondaryServerAddress_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 3, 3, 8),
    _AcSysNTPSecondaryServerAddress_Type()
)
acSysNTPSecondaryServerAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acSysNTPSecondaryServerAddress.setStatus("current")
_AcSysDayLightSavingTime_ObjectIdentity = ObjectIdentity
acSysDayLightSavingTime = _AcSysDayLightSavingTime_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 3, 3, 21)
)


class _AcSysDayLightSavingTimeMode_Type(Integer32):
    """Custom type acSysDayLightSavingTimeMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_AcSysDayLightSavingTimeMode_Type.__name__ = "Integer32"
_AcSysDayLightSavingTimeMode_Object = MibScalar
acSysDayLightSavingTimeMode = _AcSysDayLightSavingTimeMode_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 3, 3, 21, 1),
    _AcSysDayLightSavingTimeMode_Type()
)
acSysDayLightSavingTimeMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acSysDayLightSavingTimeMode.setStatus("current")


class _AcSysDayLightSavingTimeOffset_Type(Unsigned32):
    """Custom type acSysDayLightSavingTimeOffset based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 120),
    )


_AcSysDayLightSavingTimeOffset_Type.__name__ = "Unsigned32"
_AcSysDayLightSavingTimeOffset_Object = MibScalar
acSysDayLightSavingTimeOffset = _AcSysDayLightSavingTimeOffset_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 3, 3, 21, 2),
    _AcSysDayLightSavingTimeOffset_Type()
)
acSysDayLightSavingTimeOffset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acSysDayLightSavingTimeOffset.setStatus("current")


class _AcSysDayLightSavingTimeStart_Type(SnmpAdminString):
    """Custom type acSysDayLightSavingTimeStart based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_AcSysDayLightSavingTimeStart_Type.__name__ = "SnmpAdminString"
_AcSysDayLightSavingTimeStart_Object = MibScalar
acSysDayLightSavingTimeStart = _AcSysDayLightSavingTimeStart_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 3, 3, 21, 3),
    _AcSysDayLightSavingTimeStart_Type()
)
acSysDayLightSavingTimeStart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acSysDayLightSavingTimeStart.setStatus("current")


class _AcSysDayLightSavingTimeEnd_Type(SnmpAdminString):
    """Custom type acSysDayLightSavingTimeEnd based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_AcSysDayLightSavingTimeEnd_Type.__name__ = "SnmpAdminString"
_AcSysDayLightSavingTimeEnd_Object = MibScalar
acSysDayLightSavingTimeEnd = _AcSysDayLightSavingTimeEnd_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 3, 3, 21, 4),
    _AcSysDayLightSavingTimeEnd_Type()
)
acSysDayLightSavingTimeEnd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acSysDayLightSavingTimeEnd.setStatus("current")
_AcSysWEB_ObjectIdentity = ObjectIdentity
acSysWEB = _AcSysWEB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 3, 4)
)


class _AcSysWEBConfigDisable_Type(Integer32):
    """Custom type acSysWEBConfigDisable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("enable", 0),
          ("disable", 1))
    )


_AcSysWEBConfigDisable_Type.__name__ = "Integer32"
_AcSysWEBConfigDisable_Object = MibScalar
acSysWEBConfigDisable = _AcSysWEBConfigDisable_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 3, 4, 1),
    _AcSysWEBConfigDisable_Type()
)
acSysWEBConfigDisable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acSysWEBConfigDisable.setStatus("current")


class _AcSysWEBHTTPSOnly_Type(Integer32):
    """Custom type acSysWEBHTTPSOnly based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_AcSysWEBHTTPSOnly_Type.__name__ = "Integer32"
_AcSysWEBHTTPSOnly_Object = MibScalar
acSysWEBHTTPSOnly = _AcSysWEBHTTPSOnly_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 3, 4, 2),
    _AcSysWEBHTTPSOnly_Type()
)
acSysWEBHTTPSOnly.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acSysWEBHTTPSOnly.setStatus("current")


class _AcSysWEBHTTPSPort_Type(Unsigned32):
    """Custom type acSysWEBHTTPSPort based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AcSysWEBHTTPSPort_Type.__name__ = "Unsigned32"
_AcSysWEBHTTPSPort_Object = MibScalar
acSysWEBHTTPSPort = _AcSysWEBHTTPSPort_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 3, 4, 3),
    _AcSysWEBHTTPSPort_Type()
)
acSysWEBHTTPSPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acSysWEBHTTPSPort.setStatus("current")


class _AcSysWEBWebUseRadiusLogin_Type(Integer32):
    """Custom type acSysWEBWebUseRadiusLogin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_AcSysWEBWebUseRadiusLogin_Type.__name__ = "Integer32"
_AcSysWEBWebUseRadiusLogin_Object = MibScalar
acSysWEBWebUseRadiusLogin = _AcSysWEBWebUseRadiusLogin_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 3, 4, 4),
    _AcSysWEBWebUseRadiusLogin_Type()
)
acSysWEBWebUseRadiusLogin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acSysWEBWebUseRadiusLogin.setStatus("current")


class _AcSysWEBHTTPSCipherString_Type(SnmpAdminString):
    """Custom type acSysWEBHTTPSCipherString based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 200),
    )


_AcSysWEBHTTPSCipherString_Type.__name__ = "SnmpAdminString"
_AcSysWEBHTTPSCipherString_Object = MibScalar
acSysWEBHTTPSCipherString = _AcSysWEBHTTPSCipherString_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 3, 4, 5),
    _AcSysWEBHTTPSCipherString_Type()
)
acSysWEBHTTPSCipherString.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acSysWEBHTTPSCipherString.setStatus("current")


class _AcSysWEBDenyAuthenticationTimer_Type(Unsigned32):
    """Custom type acSysWEBDenyAuthenticationTimer based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 86400),
    )


_AcSysWEBDenyAuthenticationTimer_Type.__name__ = "Unsigned32"
_AcSysWEBDenyAuthenticationTimer_Object = MibScalar
acSysWEBDenyAuthenticationTimer = _AcSysWEBDenyAuthenticationTimer_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 3, 4, 6),
    _AcSysWEBDenyAuthenticationTimer_Type()
)
acSysWEBDenyAuthenticationTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acSysWEBDenyAuthenticationTimer.setStatus("current")


class _AcSysWEBWanHttpPort_Type(Unsigned32):
    """Custom type acSysWEBWanHttpPort based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AcSysWEBWanHttpPort_Type.__name__ = "Unsigned32"
_AcSysWEBWanHttpPort_Object = MibScalar
acSysWEBWanHttpPort = _AcSysWEBWanHttpPort_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 3, 4, 7),
    _AcSysWEBWanHttpPort_Type()
)
acSysWEBWanHttpPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acSysWEBWanHttpPort.setStatus("obsolete")


class _AcSysWEBWanHttpsPort_Type(Unsigned32):
    """Custom type acSysWEBWanHttpsPort based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AcSysWEBWanHttpsPort_Type.__name__ = "Unsigned32"
_AcSysWEBWanHttpsPort_Object = MibScalar
acSysWEBWanHttpsPort = _AcSysWEBWanHttpsPort_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 3, 4, 8),
    _AcSysWEBWanHttpsPort_Type()
)
acSysWEBWanHttpsPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acSysWEBWanHttpsPort.setStatus("obsolete")


class _AcSysWEBAllowWanHttp_Type(Integer32):
    """Custom type acSysWEBAllowWanHttp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_AcSysWEBAllowWanHttp_Type.__name__ = "Integer32"
_AcSysWEBAllowWanHttp_Object = MibScalar
acSysWEBAllowWanHttp = _AcSysWEBAllowWanHttp_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 3, 4, 9),
    _AcSysWEBAllowWanHttp_Type()
)
acSysWEBAllowWanHttp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acSysWEBAllowWanHttp.setStatus("current")


class _AcSysWEBAllowWanHttps_Type(Integer32):
    """Custom type acSysWEBAllowWanHttps based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_AcSysWEBAllowWanHttps_Type.__name__ = "Integer32"
_AcSysWEBAllowWanHttps_Object = MibScalar
acSysWEBAllowWanHttps = _AcSysWEBAllowWanHttps_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 3, 4, 10),
    _AcSysWEBAllowWanHttps_Type()
)
acSysWEBAllowWanHttps.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acSysWEBAllowWanHttps.setStatus("current")


class _AcSysWEBTLSClientCipherString_Type(SnmpAdminString):
    """Custom type acSysWEBTLSClientCipherString based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 254),
    )


_AcSysWEBTLSClientCipherString_Type.__name__ = "SnmpAdminString"
_AcSysWEBTLSClientCipherString_Object = MibScalar
acSysWEBTLSClientCipherString = _AcSysWEBTLSClientCipherString_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 3, 4, 11),
    _AcSysWEBTLSClientCipherString_Type()
)
acSysWEBTLSClientCipherString.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acSysWEBTLSClientCipherString.setStatus("current")


class _AcSysWEBUseLdapForLogin_Type(Integer32):
    """Custom type acSysWEBUseLdapForLogin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_AcSysWEBUseLdapForLogin_Type.__name__ = "Integer32"
_AcSysWEBUseLdapForLogin_Object = MibScalar
acSysWEBUseLdapForLogin = _AcSysWEBUseLdapForLogin_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 3, 4, 12),
    _AcSysWEBUseLdapForLogin_Type()
)
acSysWEBUseLdapForLogin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acSysWEBUseLdapForLogin.setStatus("current")
_AcSysWEBACLTable_Object = MibTable
acSysWEBACLTable = _AcSysWEBACLTable_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 3, 4, 21)
)
if mibBuilder.loadTexts:
    acSysWEBACLTable.setStatus("current")
_AcSysWEBACLEntry_Object = MibTableRow
acSysWEBACLEntry = _AcSysWEBACLEntry_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 3, 4, 21, 1)
)
acSysWEBACLEntry.setIndexNames(
    (0, "AC-SYSTEM-MIB", "acSysWEBACLIndex"),
)
if mibBuilder.loadTexts:
    acSysWEBACLEntry.setStatus("current")


class _AcSysWEBACLIndex_Type(Unsigned32):
    """Custom type acSysWEBACLIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 9),
    )


_AcSysWEBACLIndex_Type.__name__ = "Unsigned32"
_AcSysWEBACLIndex_Object = MibTableColumn
acSysWEBACLIndex = _AcSysWEBACLIndex_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 3, 4, 21, 1, 1),
    _AcSysWEBACLIndex_Type()
)
acSysWEBACLIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSysWEBACLIndex.setStatus("current")
_AcSysWEBACLIP_Type = IpAddress
_AcSysWEBACLIP_Object = MibTableColumn
acSysWEBACLIP = _AcSysWEBACLIP_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 3, 4, 21, 1, 2),
    _AcSysWEBACLIP_Type()
)
acSysWEBACLIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acSysWEBACLIP.setStatus("deprecated")
_AcSysWEBAccess_ObjectIdentity = ObjectIdentity
acSysWEBAccess = _AcSysWEBAccess_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 3, 5)
)
_AcSysWEBAccessTable_Object = MibTable
acSysWEBAccessTable = _AcSysWEBAccessTable_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 3, 5, 1)
)
if mibBuilder.loadTexts:
    acSysWEBAccessTable.setStatus("current")
_AcSysWEBAccessEntry_Object = MibTableRow
acSysWEBAccessEntry = _AcSysWEBAccessEntry_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 3, 5, 1, 1)
)
acSysWEBAccessEntry.setIndexNames(
    (0, "AC-SYSTEM-MIB", "acSysWEBAccessIndex"),
)
if mibBuilder.loadTexts:
    acSysWEBAccessEntry.setStatus("current")


class _AcSysWEBAccessRowStatus_Type(Unsigned32):
    """Custom type acSysWEBAccessRowStatus based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
    )


_AcSysWEBAccessRowStatus_Type.__name__ = "Unsigned32"
_AcSysWEBAccessRowStatus_Object = MibTableColumn
acSysWEBAccessRowStatus = _AcSysWEBAccessRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 3, 5, 1, 1, 1),
    _AcSysWEBAccessRowStatus_Type()
)
acSysWEBAccessRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acSysWEBAccessRowStatus.setStatus("current")


class _AcSysWEBAccessAction_Type(Unsigned32):
    """Custom type acSysWEBAccessAction based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
    )


_AcSysWEBAccessAction_Type.__name__ = "Unsigned32"
_AcSysWEBAccessAction_Object = MibTableColumn
acSysWEBAccessAction = _AcSysWEBAccessAction_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 3, 5, 1, 1, 2),
    _AcSysWEBAccessAction_Type()
)
acSysWEBAccessAction.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acSysWEBAccessAction.setStatus("current")


class _AcSysWEBAccessActionResult_Type(Unsigned32):
    """Custom type acSysWEBAccessActionResult based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
    )


_AcSysWEBAccessActionResult_Type.__name__ = "Unsigned32"
_AcSysWEBAccessActionResult_Object = MibTableColumn
acSysWEBAccessActionResult = _AcSysWEBAccessActionResult_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 3, 5, 1, 1, 3),
    _AcSysWEBAccessActionResult_Type()
)
acSysWEBAccessActionResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSysWEBAccessActionResult.setStatus("current")


class _AcSysWEBAccessIndex_Type(Integer32):
    """Custom type acSysWEBAccessIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("administrator", 0),
          ("monitoringLevel", 1))
    )


_AcSysWEBAccessIndex_Type.__name__ = "Integer32"
_AcSysWEBAccessIndex_Object = MibTableColumn
acSysWEBAccessIndex = _AcSysWEBAccessIndex_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 3, 5, 1, 1, 4),
    _AcSysWEBAccessIndex_Type()
)
acSysWEBAccessIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSysWEBAccessIndex.setStatus("current")


class _AcSysWEBAccessUserName_Type(SnmpAdminString):
    """Custom type acSysWEBAccessUserName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 60),
    )


_AcSysWEBAccessUserName_Type.__name__ = "SnmpAdminString"
_AcSysWEBAccessUserName_Object = MibTableColumn
acSysWEBAccessUserName = _AcSysWEBAccessUserName_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 3, 5, 1, 1, 5),
    _AcSysWEBAccessUserName_Type()
)
acSysWEBAccessUserName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acSysWEBAccessUserName.setStatus("current")


class _AcSysWEBAccessUserCode_Type(SnmpAdminString):
    """Custom type acSysWEBAccessUserCode based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 60),
    )


_AcSysWEBAccessUserCode_Type.__name__ = "SnmpAdminString"
_AcSysWEBAccessUserCode_Object = MibTableColumn
acSysWEBAccessUserCode = _AcSysWEBAccessUserCode_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 3, 5, 1, 1, 6),
    _AcSysWEBAccessUserCode_Type()
)
acSysWEBAccessUserCode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acSysWEBAccessUserCode.setStatus("current")


class _AcSysWEBAccessWebAuthMode_Type(Integer32):
    """Custom type acSysWEBAccessWebAuthMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("basicMode", 0),
          ("digestModeWhenPossible", 1),
          ("digestModeHTTPOnly", 2))
    )


_AcSysWEBAccessWebAuthMode_Type.__name__ = "Integer32"
_AcSysWEBAccessWebAuthMode_Object = MibTableColumn
acSysWEBAccessWebAuthMode = _AcSysWEBAccessWebAuthMode_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 3, 5, 1, 1, 7),
    _AcSysWEBAccessWebAuthMode_Type()
)
acSysWEBAccessWebAuthMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acSysWEBAccessWebAuthMode.setStatus("current")
_AcSysNATTraversal_ObjectIdentity = ObjectIdentity
acSysNATTraversal = _AcSysNATTraversal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 3, 6)
)
_AcSysSTUN_ObjectIdentity = ObjectIdentity
acSysSTUN = _AcSysSTUN_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 3, 6, 21)
)


class _AcSysSTUNEnable_Type(Integer32):
    """Custom type acSysSTUNEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_AcSysSTUNEnable_Type.__name__ = "Integer32"
_AcSysSTUNEnable_Object = MibScalar
acSysSTUNEnable = _AcSysSTUNEnable_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 3, 6, 21, 1),
    _AcSysSTUNEnable_Type()
)
acSysSTUNEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acSysSTUNEnable.setStatus("current")
_AcSysSTUNPrimaryServerIP_Type = IpAddress
_AcSysSTUNPrimaryServerIP_Object = MibScalar
acSysSTUNPrimaryServerIP = _AcSysSTUNPrimaryServerIP_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 3, 6, 21, 2),
    _AcSysSTUNPrimaryServerIP_Type()
)
acSysSTUNPrimaryServerIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acSysSTUNPrimaryServerIP.setStatus("deprecated")
_AcSysSTUNSecondaryServerIP_Type = IpAddress
_AcSysSTUNSecondaryServerIP_Object = MibScalar
acSysSTUNSecondaryServerIP = _AcSysSTUNSecondaryServerIP_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 3, 6, 21, 3),
    _AcSysSTUNSecondaryServerIP_Type()
)
acSysSTUNSecondaryServerIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acSysSTUNSecondaryServerIP.setStatus("deprecated")


class _AcSysSTUNBindingLifeTime_Type(Unsigned32):
    """Custom type acSysSTUNBindingLifeTime based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AcSysSTUNBindingLifeTime_Type.__name__ = "Unsigned32"
_AcSysSTUNBindingLifeTime_Object = MibScalar
acSysSTUNBindingLifeTime = _AcSysSTUNBindingLifeTime_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 3, 6, 21, 4),
    _AcSysSTUNBindingLifeTime_Type()
)
acSysSTUNBindingLifeTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acSysSTUNBindingLifeTime.setStatus("current")
_AcSysTelnet_ObjectIdentity = ObjectIdentity
acSysTelnet = _AcSysTelnet_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 3, 7)
)


class _AcSysTelnetServerEnable_Type(Integer32):
    """Custom type acSysTelnetServerEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1),
          ("ssl", 2))
    )


_AcSysTelnetServerEnable_Type.__name__ = "Integer32"
_AcSysTelnetServerEnable_Object = MibScalar
acSysTelnetServerEnable = _AcSysTelnetServerEnable_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 3, 7, 1),
    _AcSysTelnetServerEnable_Type()
)
acSysTelnetServerEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acSysTelnetServerEnable.setStatus("current")


class _AcSysTelnetServerPort_Type(Unsigned32):
    """Custom type acSysTelnetServerPort based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AcSysTelnetServerPort_Type.__name__ = "Unsigned32"
_AcSysTelnetServerPort_Object = MibScalar
acSysTelnetServerPort = _AcSysTelnetServerPort_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 3, 7, 2),
    _AcSysTelnetServerPort_Type()
)
acSysTelnetServerPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acSysTelnetServerPort.setStatus("current")


class _AcSysTelnetServerIdleDisconnect_Type(Unsigned32):
    """Custom type acSysTelnetServerIdleDisconnect based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AcSysTelnetServerIdleDisconnect_Type.__name__ = "Unsigned32"
_AcSysTelnetServerIdleDisconnect_Object = MibScalar
acSysTelnetServerIdleDisconnect = _AcSysTelnetServerIdleDisconnect_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 3, 7, 3),
    _AcSysTelnetServerIdleDisconnect_Type()
)
acSysTelnetServerIdleDisconnect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acSysTelnetServerIdleDisconnect.setStatus("current")


class _AcSysTelnetSSHServerPort_Type(Unsigned32):
    """Custom type acSysTelnetSSHServerPort based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AcSysTelnetSSHServerPort_Type.__name__ = "Unsigned32"
_AcSysTelnetSSHServerPort_Object = MibScalar
acSysTelnetSSHServerPort = _AcSysTelnetSSHServerPort_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 3, 7, 4),
    _AcSysTelnetSSHServerPort_Type()
)
acSysTelnetSSHServerPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acSysTelnetSSHServerPort.setStatus("current")


class _AcSysTelnetSSHServerEnable_Type(Integer32):
    """Custom type acSysTelnetSSHServerEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_AcSysTelnetSSHServerEnable_Type.__name__ = "Integer32"
_AcSysTelnetSSHServerEnable_Object = MibScalar
acSysTelnetSSHServerEnable = _AcSysTelnetSSHServerEnable_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 3, 7, 5),
    _AcSysTelnetSSHServerEnable_Type()
)
acSysTelnetSSHServerEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acSysTelnetSSHServerEnable.setStatus("current")


class _AcSysTelnetSSHAdminKey_Type(SnmpAdminString):
    """Custom type acSysTelnetSSHAdminKey based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 510),
    )


_AcSysTelnetSSHAdminKey_Type.__name__ = "SnmpAdminString"
_AcSysTelnetSSHAdminKey_Object = MibScalar
acSysTelnetSSHAdminKey = _AcSysTelnetSSHAdminKey_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 3, 7, 6),
    _AcSysTelnetSSHAdminKey_Type()
)
acSysTelnetSSHAdminKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acSysTelnetSSHAdminKey.setStatus("current")


class _AcSysTelnetSSHRequirePublicKey_Type(Integer32):
    """Custom type acSysTelnetSSHRequirePublicKey based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_AcSysTelnetSSHRequirePublicKey_Type.__name__ = "Integer32"
_AcSysTelnetSSHRequirePublicKey_Object = MibScalar
acSysTelnetSSHRequirePublicKey = _AcSysTelnetSSHRequirePublicKey_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 3, 7, 7),
    _AcSysTelnetSSHRequirePublicKey_Type()
)
acSysTelnetSSHRequirePublicKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acSysTelnetSSHRequirePublicKey.setStatus("current")


class _AcSysTelnetServerWanPort_Type(Unsigned32):
    """Custom type acSysTelnetServerWanPort based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AcSysTelnetServerWanPort_Type.__name__ = "Unsigned32"
_AcSysTelnetServerWanPort_Object = MibScalar
acSysTelnetServerWanPort = _AcSysTelnetServerWanPort_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 3, 7, 8),
    _AcSysTelnetServerWanPort_Type()
)
acSysTelnetServerWanPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acSysTelnetServerWanPort.setStatus("obsolete")


class _AcSysTelnetWanSSHServerPort_Type(Unsigned32):
    """Custom type acSysTelnetWanSSHServerPort based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AcSysTelnetWanSSHServerPort_Type.__name__ = "Unsigned32"
_AcSysTelnetWanSSHServerPort_Object = MibScalar
acSysTelnetWanSSHServerPort = _AcSysTelnetWanSSHServerPort_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 3, 7, 9),
    _AcSysTelnetWanSSHServerPort_Type()
)
acSysTelnetWanSSHServerPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acSysTelnetWanSSHServerPort.setStatus("obsolete")


class _AcSysTelnetSSHMaxSessions_Type(Unsigned32):
    """Custom type acSysTelnetSSHMaxSessions based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_AcSysTelnetSSHMaxSessions_Type.__name__ = "Unsigned32"
_AcSysTelnetSSHMaxSessions_Object = MibScalar
acSysTelnetSSHMaxSessions = _AcSysTelnetSSHMaxSessions_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 3, 7, 10),
    _AcSysTelnetSSHMaxSessions_Type()
)
acSysTelnetSSHMaxSessions.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acSysTelnetSSHMaxSessions.setStatus("current")


class _AcSysTelnetSSHMaxPayloadSize_Type(Unsigned32):
    """Custom type acSysTelnetSSHMaxPayloadSize based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(550, 32768),
    )


_AcSysTelnetSSHMaxPayloadSize_Type.__name__ = "Unsigned32"
_AcSysTelnetSSHMaxPayloadSize_Object = MibScalar
acSysTelnetSSHMaxPayloadSize = _AcSysTelnetSSHMaxPayloadSize_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 3, 7, 11),
    _AcSysTelnetSSHMaxPayloadSize_Type()
)
acSysTelnetSSHMaxPayloadSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acSysTelnetSSHMaxPayloadSize.setStatus("current")


class _AcSysTelnetSSHMaxBinaryPacketSize_Type(Unsigned32):
    """Custom type acSysTelnetSSHMaxBinaryPacketSize based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(582, 35000),
    )


_AcSysTelnetSSHMaxBinaryPacketSize_Type.__name__ = "Unsigned32"
_AcSysTelnetSSHMaxBinaryPacketSize_Object = MibScalar
acSysTelnetSSHMaxBinaryPacketSize = _AcSysTelnetSSHMaxBinaryPacketSize_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 3, 7, 12),
    _AcSysTelnetSSHMaxBinaryPacketSize_Type()
)
acSysTelnetSSHMaxBinaryPacketSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acSysTelnetSSHMaxBinaryPacketSize.setStatus("current")


class _AcSysTelnetAllowWanTelnet_Type(Integer32):
    """Custom type acSysTelnetAllowWanTelnet based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_AcSysTelnetAllowWanTelnet_Type.__name__ = "Integer32"
_AcSysTelnetAllowWanTelnet_Object = MibScalar
acSysTelnetAllowWanTelnet = _AcSysTelnetAllowWanTelnet_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 3, 7, 13),
    _AcSysTelnetAllowWanTelnet_Type()
)
acSysTelnetAllowWanTelnet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acSysTelnetAllowWanTelnet.setStatus("current")


class _AcSysTelnetAllowWanSSH_Type(Integer32):
    """Custom type acSysTelnetAllowWanSSH based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_AcSysTelnetAllowWanSSH_Type.__name__ = "Integer32"
_AcSysTelnetAllowWanSSH_Object = MibScalar
acSysTelnetAllowWanSSH = _AcSysTelnetAllowWanSSH_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 3, 7, 14),
    _AcSysTelnetAllowWanSSH_Type()
)
acSysTelnetAllowWanSSH.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acSysTelnetAllowWanSSH.setStatus("current")


class _AcSysTelnetMaxSessions_Type(Unsigned32):
    """Custom type acSysTelnetMaxSessions based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_AcSysTelnetMaxSessions_Type.__name__ = "Unsigned32"
_AcSysTelnetMaxSessions_Object = MibScalar
acSysTelnetMaxSessions = _AcSysTelnetMaxSessions_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 3, 7, 15),
    _AcSysTelnetMaxSessions_Type()
)
acSysTelnetMaxSessions.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acSysTelnetMaxSessions.setStatus("current")
_AcSysHTTPClient_ObjectIdentity = ObjectIdentity
acSysHTTPClient = _AcSysHTTPClient_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 3, 8)
)


class _AcSysHTTPClientAutoUpdatePredefinedTime_Type(SnmpAdminString):
    """Custom type acSysHTTPClientAutoUpdatePredefinedTime based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 6),
    )


_AcSysHTTPClientAutoUpdatePredefinedTime_Type.__name__ = "SnmpAdminString"
_AcSysHTTPClientAutoUpdatePredefinedTime_Object = MibScalar
acSysHTTPClientAutoUpdatePredefinedTime = _AcSysHTTPClientAutoUpdatePredefinedTime_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 3, 8, 1),
    _AcSysHTTPClientAutoUpdatePredefinedTime_Type()
)
acSysHTTPClientAutoUpdatePredefinedTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acSysHTTPClientAutoUpdatePredefinedTime.setStatus("current")


class _AcSysHTTPClientAutoUpdateFrequency_Type(Unsigned32):
    """Custom type acSysHTTPClientAutoUpdateFrequency based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_AcSysHTTPClientAutoUpdateFrequency_Type.__name__ = "Unsigned32"
_AcSysHTTPClientAutoUpdateFrequency_Object = MibScalar
acSysHTTPClientAutoUpdateFrequency = _AcSysHTTPClientAutoUpdateFrequency_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 3, 8, 2),
    _AcSysHTTPClientAutoUpdateFrequency_Type()
)
acSysHTTPClientAutoUpdateFrequency.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acSysHTTPClientAutoUpdateFrequency.setStatus("current")


class _AcSysHTTPClientAutoUpdateCmpFile_Type(Integer32):
    """Custom type acSysHTTPClientAutoUpdateCmpFile based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_AcSysHTTPClientAutoUpdateCmpFile_Type.__name__ = "Integer32"
_AcSysHTTPClientAutoUpdateCmpFile_Object = MibScalar
acSysHTTPClientAutoUpdateCmpFile = _AcSysHTTPClientAutoUpdateCmpFile_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 3, 8, 3),
    _AcSysHTTPClientAutoUpdateCmpFile_Type()
)
acSysHTTPClientAutoUpdateCmpFile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acSysHTTPClientAutoUpdateCmpFile.setStatus("current")


class _AcSysHTTPClientCmpFileURL_Type(SnmpAdminString):
    """Custom type acSysHTTPClientCmpFileURL based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 254),
    )


_AcSysHTTPClientCmpFileURL_Type.__name__ = "SnmpAdminString"
_AcSysHTTPClientCmpFileURL_Object = MibScalar
acSysHTTPClientCmpFileURL = _AcSysHTTPClientCmpFileURL_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 3, 8, 4),
    _AcSysHTTPClientCmpFileURL_Type()
)
acSysHTTPClientCmpFileURL.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acSysHTTPClientCmpFileURL.setStatus("current")


class _AcSysHTTPClientIniFileURL_Type(SnmpAdminString):
    """Custom type acSysHTTPClientIniFileURL based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 758),
    )


_AcSysHTTPClientIniFileURL_Type.__name__ = "SnmpAdminString"
_AcSysHTTPClientIniFileURL_Object = MibScalar
acSysHTTPClientIniFileURL = _AcSysHTTPClientIniFileURL_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 3, 8, 5),
    _AcSysHTTPClientIniFileURL_Type()
)
acSysHTTPClientIniFileURL.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acSysHTTPClientIniFileURL.setStatus("current")


class _AcSysHTTPClientIniFileTemplateURL_Type(SnmpAdminString):
    """Custom type acSysHTTPClientIniFileTemplateURL based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 254),
    )


_AcSysHTTPClientIniFileTemplateURL_Type.__name__ = "SnmpAdminString"
_AcSysHTTPClientIniFileTemplateURL_Object = MibScalar
acSysHTTPClientIniFileTemplateURL = _AcSysHTTPClientIniFileTemplateURL_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 3, 8, 6),
    _AcSysHTTPClientIniFileTemplateURL_Type()
)
acSysHTTPClientIniFileTemplateURL.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acSysHTTPClientIniFileTemplateURL.setStatus("current")


class _AcSysHTTPClientCPTFileURL_Type(SnmpAdminString):
    """Custom type acSysHTTPClientCPTFileURL based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 254),
    )


_AcSysHTTPClientCPTFileURL_Type.__name__ = "SnmpAdminString"
_AcSysHTTPClientCPTFileURL_Object = MibScalar
acSysHTTPClientCPTFileURL = _AcSysHTTPClientCPTFileURL_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 3, 8, 7),
    _AcSysHTTPClientCPTFileURL_Type()
)
acSysHTTPClientCPTFileURL.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acSysHTTPClientCPTFileURL.setStatus("current")


class _AcSysHTTPClientVPFileURL_Type(SnmpAdminString):
    """Custom type acSysHTTPClientVPFileURL based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 254),
    )


_AcSysHTTPClientVPFileURL_Type.__name__ = "SnmpAdminString"
_AcSysHTTPClientVPFileURL_Object = MibScalar
acSysHTTPClientVPFileURL = _AcSysHTTPClientVPFileURL_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 3, 8, 8),
    _AcSysHTTPClientVPFileURL_Type()
)
acSysHTTPClientVPFileURL.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acSysHTTPClientVPFileURL.setStatus("current")


class _AcSysHTTPClientPRTFileURL_Type(SnmpAdminString):
    """Custom type acSysHTTPClientPRTFileURL based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 254),
    )


_AcSysHTTPClientPRTFileURL_Type.__name__ = "SnmpAdminString"
_AcSysHTTPClientPRTFileURL_Object = MibScalar
acSysHTTPClientPRTFileURL = _AcSysHTTPClientPRTFileURL_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 3, 8, 9),
    _AcSysHTTPClientPRTFileURL_Type()
)
acSysHTTPClientPRTFileURL.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acSysHTTPClientPRTFileURL.setStatus("current")


class _AcSysHTTPClientFXSCoeffFileURL_Type(SnmpAdminString):
    """Custom type acSysHTTPClientFXSCoeffFileURL based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 254),
    )


_AcSysHTTPClientFXSCoeffFileURL_Type.__name__ = "SnmpAdminString"
_AcSysHTTPClientFXSCoeffFileURL_Object = MibScalar
acSysHTTPClientFXSCoeffFileURL = _AcSysHTTPClientFXSCoeffFileURL_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 3, 8, 10),
    _AcSysHTTPClientFXSCoeffFileURL_Type()
)
acSysHTTPClientFXSCoeffFileURL.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acSysHTTPClientFXSCoeffFileURL.setStatus("deprecated")


class _AcSysHTTPClientFXOCoeffFileURL_Type(SnmpAdminString):
    """Custom type acSysHTTPClientFXOCoeffFileURL based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 254),
    )


_AcSysHTTPClientFXOCoeffFileURL_Type.__name__ = "SnmpAdminString"
_AcSysHTTPClientFXOCoeffFileURL_Object = MibScalar
acSysHTTPClientFXOCoeffFileURL = _AcSysHTTPClientFXOCoeffFileURL_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 3, 8, 11),
    _AcSysHTTPClientFXOCoeffFileURL_Type()
)
acSysHTTPClientFXOCoeffFileURL.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acSysHTTPClientFXOCoeffFileURL.setStatus("deprecated")


class _AcSysHTTPClientCASFileURL_Type(SnmpAdminString):
    """Custom type acSysHTTPClientCASFileURL based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 254),
    )


_AcSysHTTPClientCASFileURL_Type.__name__ = "SnmpAdminString"
_AcSysHTTPClientCASFileURL_Object = MibScalar
acSysHTTPClientCASFileURL = _AcSysHTTPClientCASFileURL_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 3, 8, 12),
    _AcSysHTTPClientCASFileURL_Type()
)
acSysHTTPClientCASFileURL.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acSysHTTPClientCASFileURL.setStatus("current")


class _AcSysHTTPClientXMLFileUrl_Type(SnmpAdminString):
    """Custom type acSysHTTPClientXMLFileUrl based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 254),
    )


_AcSysHTTPClientXMLFileUrl_Type.__name__ = "SnmpAdminString"
_AcSysHTTPClientXMLFileUrl_Object = MibScalar
acSysHTTPClientXMLFileUrl = _AcSysHTTPClientXMLFileUrl_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 3, 8, 13),
    _AcSysHTTPClientXMLFileUrl_Type()
)
acSysHTTPClientXMLFileUrl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acSysHTTPClientXMLFileUrl.setStatus("current")


class _AcSysHTTPClientCoderTableFileUrl_Type(SnmpAdminString):
    """Custom type acSysHTTPClientCoderTableFileUrl based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 254),
    )


_AcSysHTTPClientCoderTableFileUrl_Type.__name__ = "SnmpAdminString"
_AcSysHTTPClientCoderTableFileUrl_Object = MibScalar
acSysHTTPClientCoderTableFileUrl = _AcSysHTTPClientCoderTableFileUrl_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 3, 8, 14),
    _AcSysHTTPClientCoderTableFileUrl_Type()
)
acSysHTTPClientCoderTableFileUrl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acSysHTTPClientCoderTableFileUrl.setStatus("current")


class _AcSysHTTPClientUserInfoFileURL_Type(SnmpAdminString):
    """Custom type acSysHTTPClientUserInfoFileURL based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 254),
    )


_AcSysHTTPClientUserInfoFileURL_Type.__name__ = "SnmpAdminString"
_AcSysHTTPClientUserInfoFileURL_Object = MibScalar
acSysHTTPClientUserInfoFileURL = _AcSysHTTPClientUserInfoFileURL_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 3, 8, 15),
    _AcSysHTTPClientUserInfoFileURL_Type()
)
acSysHTTPClientUserInfoFileURL.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acSysHTTPClientUserInfoFileURL.setStatus("current")


class _AcSysHTTPClientDialPlanFileURL_Type(SnmpAdminString):
    """Custom type acSysHTTPClientDialPlanFileURL based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 254),
    )


_AcSysHTTPClientDialPlanFileURL_Type.__name__ = "SnmpAdminString"
_AcSysHTTPClientDialPlanFileURL_Object = MibScalar
acSysHTTPClientDialPlanFileURL = _AcSysHTTPClientDialPlanFileURL_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 3, 8, 16),
    _AcSysHTTPClientDialPlanFileURL_Type()
)
acSysHTTPClientDialPlanFileURL.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acSysHTTPClientDialPlanFileURL.setStatus("current")


class _AcSysHTTPClientTLSPkeyFileUrl_Type(SnmpAdminString):
    """Custom type acSysHTTPClientTLSPkeyFileUrl based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 254),
    )


_AcSysHTTPClientTLSPkeyFileUrl_Type.__name__ = "SnmpAdminString"
_AcSysHTTPClientTLSPkeyFileUrl_Object = MibScalar
acSysHTTPClientTLSPkeyFileUrl = _AcSysHTTPClientTLSPkeyFileUrl_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 3, 8, 17),
    _AcSysHTTPClientTLSPkeyFileUrl_Type()
)
acSysHTTPClientTLSPkeyFileUrl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acSysHTTPClientTLSPkeyFileUrl.setStatus("current")


class _AcSysHTTPClientTLSCertFileUrl_Type(SnmpAdminString):
    """Custom type acSysHTTPClientTLSCertFileUrl based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 254),
    )


_AcSysHTTPClientTLSCertFileUrl_Type.__name__ = "SnmpAdminString"
_AcSysHTTPClientTLSCertFileUrl_Object = MibScalar
acSysHTTPClientTLSCertFileUrl = _AcSysHTTPClientTLSCertFileUrl_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 3, 8, 18),
    _AcSysHTTPClientTLSCertFileUrl_Type()
)
acSysHTTPClientTLSCertFileUrl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acSysHTTPClientTLSCertFileUrl.setStatus("current")


class _AcSysHTTPClientTLSRootFileUrl_Type(SnmpAdminString):
    """Custom type acSysHTTPClientTLSRootFileUrl based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 254),
    )


_AcSysHTTPClientTLSRootFileUrl_Type.__name__ = "SnmpAdminString"
_AcSysHTTPClientTLSRootFileUrl_Object = MibScalar
acSysHTTPClientTLSRootFileUrl = _AcSysHTTPClientTLSRootFileUrl_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 3, 8, 19),
    _AcSysHTTPClientTLSRootFileUrl_Type()
)
acSysHTTPClientTLSRootFileUrl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acSysHTTPClientTLSRootFileUrl.setStatus("current")


class _AcSysHTTPClientWebLogoFileUrl_Type(SnmpAdminString):
    """Custom type acSysHTTPClientWebLogoFileUrl based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 254),
    )


_AcSysHTTPClientWebLogoFileUrl_Type.__name__ = "SnmpAdminString"
_AcSysHTTPClientWebLogoFileUrl_Object = MibScalar
acSysHTTPClientWebLogoFileUrl = _AcSysHTTPClientWebLogoFileUrl_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 3, 8, 20),
    _AcSysHTTPClientWebLogoFileUrl_Type()
)
acSysHTTPClientWebLogoFileUrl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acSysHTTPClientWebLogoFileUrl.setStatus("current")


class _AcSysHTTPClientVideoFontFileURL_Type(SnmpAdminString):
    """Custom type acSysHTTPClientVideoFontFileURL based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 254),
    )


_AcSysHTTPClientVideoFontFileURL_Type.__name__ = "SnmpAdminString"
_AcSysHTTPClientVideoFontFileURL_Object = MibScalar
acSysHTTPClientVideoFontFileURL = _AcSysHTTPClientVideoFontFileURL_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 3, 8, 21),
    _AcSysHTTPClientVideoFontFileURL_Type()
)
acSysHTTPClientVideoFontFileURL.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acSysHTTPClientVideoFontFileURL.setStatus("obsolete")


class _AcSysHTTPClientV5PortConfFileURL_Type(SnmpAdminString):
    """Custom type acSysHTTPClientV5PortConfFileURL based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 254),
    )


_AcSysHTTPClientV5PortConfFileURL_Type.__name__ = "SnmpAdminString"
_AcSysHTTPClientV5PortConfFileURL_Object = MibScalar
acSysHTTPClientV5PortConfFileURL = _AcSysHTTPClientV5PortConfFileURL_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 3, 8, 22),
    _AcSysHTTPClientV5PortConfFileURL_Type()
)
acSysHTTPClientV5PortConfFileURL.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acSysHTTPClientV5PortConfFileURL.setStatus("current")


class _AcSysHTTPClientDataConfigurationFileUrl_Type(SnmpAdminString):
    """Custom type acSysHTTPClientDataConfigurationFileUrl based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 254),
    )


_AcSysHTTPClientDataConfigurationFileUrl_Type.__name__ = "SnmpAdminString"
_AcSysHTTPClientDataConfigurationFileUrl_Object = MibScalar
acSysHTTPClientDataConfigurationFileUrl = _AcSysHTTPClientDataConfigurationFileUrl_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 3, 8, 23),
    _AcSysHTTPClientDataConfigurationFileUrl_Type()
)
acSysHTTPClientDataConfigurationFileUrl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acSysHTTPClientDataConfigurationFileUrl.setStatus("current")


class _AcSysHTTPClientAmdSensitivityFileUrl_Type(SnmpAdminString):
    """Custom type acSysHTTPClientAmdSensitivityFileUrl based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 254),
    )


_AcSysHTTPClientAmdSensitivityFileUrl_Type.__name__ = "SnmpAdminString"
_AcSysHTTPClientAmdSensitivityFileUrl_Object = MibScalar
acSysHTTPClientAmdSensitivityFileUrl = _AcSysHTTPClientAmdSensitivityFileUrl_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 3, 8, 24),
    _AcSysHTTPClientAmdSensitivityFileUrl_Type()
)
acSysHTTPClientAmdSensitivityFileUrl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acSysHTTPClientAmdSensitivityFileUrl.setStatus("current")


class _AcSysHTTPClientCliScriptFileUrl_Type(SnmpAdminString):
    """Custom type acSysHTTPClientCliScriptFileUrl based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 254),
    )


_AcSysHTTPClientCliScriptFileUrl_Type.__name__ = "SnmpAdminString"
_AcSysHTTPClientCliScriptFileUrl_Object = MibScalar
acSysHTTPClientCliScriptFileUrl = _AcSysHTTPClientCliScriptFileUrl_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 3, 8, 25),
    _AcSysHTTPClientCliScriptFileUrl_Type()
)
acSysHTTPClientCliScriptFileUrl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acSysHTTPClientCliScriptFileUrl.setStatus("current")


class _AcSysHTTPClientConfigurationPackageUrlFile_Type(SnmpAdminString):
    """Custom type acSysHTTPClientConfigurationPackageUrlFile based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 254),
    )


_AcSysHTTPClientConfigurationPackageUrlFile_Type.__name__ = "SnmpAdminString"
_AcSysHTTPClientConfigurationPackageUrlFile_Object = MibScalar
acSysHTTPClientConfigurationPackageUrlFile = _AcSysHTTPClientConfigurationPackageUrlFile_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 3, 8, 26),
    _AcSysHTTPClientConfigurationPackageUrlFile_Type()
)
acSysHTTPClientConfigurationPackageUrlFile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acSysHTTPClientConfigurationPackageUrlFile.setStatus("current")


class _AcSysHTTPClientIncrementalIniFileURL_Type(SnmpAdminString):
    """Custom type acSysHTTPClientIncrementalIniFileURL based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 254),
    )


_AcSysHTTPClientIncrementalIniFileURL_Type.__name__ = "SnmpAdminString"
_AcSysHTTPClientIncrementalIniFileURL_Object = MibScalar
acSysHTTPClientIncrementalIniFileURL = _AcSysHTTPClientIncrementalIniFileURL_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 3, 8, 27),
    _AcSysHTTPClientIncrementalIniFileURL_Type()
)
acSysHTTPClientIncrementalIniFileURL.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acSysHTTPClientIncrementalIniFileURL.setStatus("current")


class _AcSysHTTPClientMTCFirmwareUrlFile_Type(SnmpAdminString):
    """Custom type acSysHTTPClientMTCFirmwareUrlFile based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 254),
    )


_AcSysHTTPClientMTCFirmwareUrlFile_Type.__name__ = "SnmpAdminString"
_AcSysHTTPClientMTCFirmwareUrlFile_Object = MibScalar
acSysHTTPClientMTCFirmwareUrlFile = _AcSysHTTPClientMTCFirmwareUrlFile_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 3, 8, 28),
    _AcSysHTTPClientMTCFirmwareUrlFile_Type()
)
acSysHTTPClientMTCFirmwareUrlFile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acSysHTTPClientMTCFirmwareUrlFile.setStatus("current")


class _AcSysHTTPClientVMTFirmwareUrlFile_Type(SnmpAdminString):
    """Custom type acSysHTTPClientVMTFirmwareUrlFile based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 254),
    )


_AcSysHTTPClientVMTFirmwareUrlFile_Type.__name__ = "SnmpAdminString"
_AcSysHTTPClientVMTFirmwareUrlFile_Object = MibScalar
acSysHTTPClientVMTFirmwareUrlFile = _AcSysHTTPClientVMTFirmwareUrlFile_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 3, 8, 29),
    _AcSysHTTPClientVMTFirmwareUrlFile_Type()
)
acSysHTTPClientVMTFirmwareUrlFile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acSysHTTPClientVMTFirmwareUrlFile.setStatus("current")


class _AcSysHTTPClientTLSRootIncrementalFileUrl_Type(SnmpAdminString):
    """Custom type acSysHTTPClientTLSRootIncrementalFileUrl based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 254),
    )


_AcSysHTTPClientTLSRootIncrementalFileUrl_Type.__name__ = "SnmpAdminString"
_AcSysHTTPClientTLSRootIncrementalFileUrl_Object = MibScalar
acSysHTTPClientTLSRootIncrementalFileUrl = _AcSysHTTPClientTLSRootIncrementalFileUrl_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 3, 8, 30),
    _AcSysHTTPClientTLSRootIncrementalFileUrl_Type()
)
acSysHTTPClientTLSRootIncrementalFileUrl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acSysHTTPClientTLSRootIncrementalFileUrl.setStatus("current")
_AcSysSNMP_ObjectIdentity = ObjectIdentity
acSysSNMP = _AcSysSNMP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 3, 9)
)


class _AcSysSNMPKeepAliveTrapPort_Type(Unsigned32):
    """Custom type acSysSNMPKeepAliveTrapPort based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65334),
    )


_AcSysSNMPKeepAliveTrapPort_Type.__name__ = "Unsigned32"
_AcSysSNMPKeepAliveTrapPort_Object = MibScalar
acSysSNMPKeepAliveTrapPort = _AcSysSNMPKeepAliveTrapPort_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 3, 9, 1),
    _AcSysSNMPKeepAliveTrapPort_Type()
)
acSysSNMPKeepAliveTrapPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acSysSNMPKeepAliveTrapPort.setStatus("current")


class _AcSysSNMPEmsColdStrartIndication_Type(Unsigned32):
    """Custom type acSysSNMPEmsColdStrartIndication based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AcSysSNMPEmsColdStrartIndication_Type.__name__ = "Unsigned32"
_AcSysSNMPEmsColdStrartIndication_Object = MibScalar
acSysSNMPEmsColdStrartIndication = _AcSysSNMPEmsColdStrartIndication_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 3, 9, 2),
    _AcSysSNMPEmsColdStrartIndication_Type()
)
acSysSNMPEmsColdStrartIndication.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acSysSNMPEmsColdStrartIndication.setStatus("current")


class _AcSysSNMPWanPort_Type(Unsigned32):
    """Custom type acSysSNMPWanPort based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AcSysSNMPWanPort_Type.__name__ = "Unsigned32"
_AcSysSNMPWanPort_Object = MibScalar
acSysSNMPWanPort = _AcSysSNMPWanPort_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 3, 9, 3),
    _AcSysSNMPWanPort_Type()
)
acSysSNMPWanPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acSysSNMPWanPort.setStatus("obsolete")


class _AcSysSNMPAllowWanSnmp_Type(Integer32):
    """Custom type acSysSNMPAllowWanSnmp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_AcSysSNMPAllowWanSnmp_Type.__name__ = "Integer32"
_AcSysSNMPAllowWanSnmp_Object = MibScalar
acSysSNMPAllowWanSnmp = _AcSysSNMPAllowWanSnmp_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 3, 9, 4),
    _AcSysSNMPAllowWanSnmp_Type()
)
acSysSNMPAllowWanSnmp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acSysSNMPAllowWanSnmp.setStatus("current")
_AcSysVLAN_ObjectIdentity = ObjectIdentity
acSysVLAN = _AcSysVLAN_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 3, 10)
)


class _AcSysVLANOamVlanId_Type(Unsigned32):
    """Custom type acSysVLANOamVlanId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_AcSysVLANOamVlanId_Type.__name__ = "Unsigned32"
_AcSysVLANOamVlanId_Object = MibScalar
acSysVLANOamVlanId = _AcSysVLANOamVlanId_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 3, 10, 1),
    _AcSysVLANOamVlanId_Type()
)
acSysVLANOamVlanId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acSysVLANOamVlanId.setStatus("obsolete")


class _AcSysVLANControlVlanId_Type(Unsigned32):
    """Custom type acSysVLANControlVlanId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_AcSysVLANControlVlanId_Type.__name__ = "Unsigned32"
_AcSysVLANControlVlanId_Object = MibScalar
acSysVLANControlVlanId = _AcSysVLANControlVlanId_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 3, 10, 2),
    _AcSysVLANControlVlanId_Type()
)
acSysVLANControlVlanId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acSysVLANControlVlanId.setStatus("obsolete")


class _AcSysVLANMediaVlanId_Type(Unsigned32):
    """Custom type acSysVLANMediaVlanId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_AcSysVLANMediaVlanId_Type.__name__ = "Unsigned32"
_AcSysVLANMediaVlanId_Object = MibScalar
acSysVLANMediaVlanId = _AcSysVLANMediaVlanId_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 3, 10, 3),
    _AcSysVLANMediaVlanId_Type()
)
acSysVLANMediaVlanId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acSysVLANMediaVlanId.setStatus("obsolete")


class _AcSysVLANNetworkServiceClassPriority_Type(Unsigned32):
    """Custom type acSysVLANNetworkServiceClassPriority based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_AcSysVLANNetworkServiceClassPriority_Type.__name__ = "Unsigned32"
_AcSysVLANNetworkServiceClassPriority_Object = MibScalar
acSysVLANNetworkServiceClassPriority = _AcSysVLANNetworkServiceClassPriority_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 3, 10, 4),
    _AcSysVLANNetworkServiceClassPriority_Type()
)
acSysVLANNetworkServiceClassPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acSysVLANNetworkServiceClassPriority.setStatus("deprecated")


class _AcSysVLANPremiumServiceClassMediaPriority_Type(Unsigned32):
    """Custom type acSysVLANPremiumServiceClassMediaPriority based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_AcSysVLANPremiumServiceClassMediaPriority_Type.__name__ = "Unsigned32"
_AcSysVLANPremiumServiceClassMediaPriority_Object = MibScalar
acSysVLANPremiumServiceClassMediaPriority = _AcSysVLANPremiumServiceClassMediaPriority_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 3, 10, 5),
    _AcSysVLANPremiumServiceClassMediaPriority_Type()
)
acSysVLANPremiumServiceClassMediaPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acSysVLANPremiumServiceClassMediaPriority.setStatus("deprecated")


class _AcSysVLANGoldServiceClassPriority_Type(Unsigned32):
    """Custom type acSysVLANGoldServiceClassPriority based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_AcSysVLANGoldServiceClassPriority_Type.__name__ = "Unsigned32"
_AcSysVLANGoldServiceClassPriority_Object = MibScalar
acSysVLANGoldServiceClassPriority = _AcSysVLANGoldServiceClassPriority_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 3, 10, 6),
    _AcSysVLANGoldServiceClassPriority_Type()
)
acSysVLANGoldServiceClassPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acSysVLANGoldServiceClassPriority.setStatus("deprecated")


class _AcSysVLANBronzeServiceClassPriority_Type(Unsigned32):
    """Custom type acSysVLANBronzeServiceClassPriority based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_AcSysVLANBronzeServiceClassPriority_Type.__name__ = "Unsigned32"
_AcSysVLANBronzeServiceClassPriority_Object = MibScalar
acSysVLANBronzeServiceClassPriority = _AcSysVLANBronzeServiceClassPriority_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 3, 10, 7),
    _AcSysVLANBronzeServiceClassPriority_Type()
)
acSysVLANBronzeServiceClassPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acSysVLANBronzeServiceClassPriority.setStatus("deprecated")


class _AcSysVLANPremiumServiceClassControlPriority_Type(Unsigned32):
    """Custom type acSysVLANPremiumServiceClassControlPriority based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_AcSysVLANPremiumServiceClassControlPriority_Type.__name__ = "Unsigned32"
_AcSysVLANPremiumServiceClassControlPriority_Object = MibScalar
acSysVLANPremiumServiceClassControlPriority = _AcSysVLANPremiumServiceClassControlPriority_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 3, 10, 8),
    _AcSysVLANPremiumServiceClassControlPriority_Type()
)
acSysVLANPremiumServiceClassControlPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acSysVLANPremiumServiceClassControlPriority.setStatus("deprecated")


class _AcSysVLANNetworkServiceClassDiffServ_Type(Unsigned32):
    """Custom type acSysVLANNetworkServiceClassDiffServ based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_AcSysVLANNetworkServiceClassDiffServ_Type.__name__ = "Unsigned32"
_AcSysVLANNetworkServiceClassDiffServ_Object = MibScalar
acSysVLANNetworkServiceClassDiffServ = _AcSysVLANNetworkServiceClassDiffServ_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 3, 10, 9),
    _AcSysVLANNetworkServiceClassDiffServ_Type()
)
acSysVLANNetworkServiceClassDiffServ.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acSysVLANNetworkServiceClassDiffServ.setStatus("current")


class _AcSysVLANPremiumServiceClassMediaDiffServ_Type(Unsigned32):
    """Custom type acSysVLANPremiumServiceClassMediaDiffServ based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_AcSysVLANPremiumServiceClassMediaDiffServ_Type.__name__ = "Unsigned32"
_AcSysVLANPremiumServiceClassMediaDiffServ_Object = MibScalar
acSysVLANPremiumServiceClassMediaDiffServ = _AcSysVLANPremiumServiceClassMediaDiffServ_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 3, 10, 10),
    _AcSysVLANPremiumServiceClassMediaDiffServ_Type()
)
acSysVLANPremiumServiceClassMediaDiffServ.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acSysVLANPremiumServiceClassMediaDiffServ.setStatus("current")


class _AcSysVLANPremiumServiceClassControlDiffServ_Type(Unsigned32):
    """Custom type acSysVLANPremiumServiceClassControlDiffServ based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_AcSysVLANPremiumServiceClassControlDiffServ_Type.__name__ = "Unsigned32"
_AcSysVLANPremiumServiceClassControlDiffServ_Object = MibScalar
acSysVLANPremiumServiceClassControlDiffServ = _AcSysVLANPremiumServiceClassControlDiffServ_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 3, 10, 11),
    _AcSysVLANPremiumServiceClassControlDiffServ_Type()
)
acSysVLANPremiumServiceClassControlDiffServ.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acSysVLANPremiumServiceClassControlDiffServ.setStatus("current")


class _AcSysVLANGoldServiceClassDiffServ_Type(Unsigned32):
    """Custom type acSysVLANGoldServiceClassDiffServ based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_AcSysVLANGoldServiceClassDiffServ_Type.__name__ = "Unsigned32"
_AcSysVLANGoldServiceClassDiffServ_Object = MibScalar
acSysVLANGoldServiceClassDiffServ = _AcSysVLANGoldServiceClassDiffServ_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 3, 10, 12),
    _AcSysVLANGoldServiceClassDiffServ_Type()
)
acSysVLANGoldServiceClassDiffServ.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acSysVLANGoldServiceClassDiffServ.setStatus("current")


class _AcSysVLANBronzeServiceClassDiffServ_Type(Unsigned32):
    """Custom type acSysVLANBronzeServiceClassDiffServ based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_AcSysVLANBronzeServiceClassDiffServ_Type.__name__ = "Unsigned32"
_AcSysVLANBronzeServiceClassDiffServ_Object = MibScalar
acSysVLANBronzeServiceClassDiffServ = _AcSysVLANBronzeServiceClassDiffServ_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 3, 10, 13),
    _AcSysVLANBronzeServiceClassDiffServ_Type()
)
acSysVLANBronzeServiceClassDiffServ.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acSysVLANBronzeServiceClassDiffServ.setStatus("current")


class _AcSysVLANVlanNativeVlanId_Type(Unsigned32):
    """Custom type acSysVLANVlanNativeVlanId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_AcSysVLANVlanNativeVlanId_Type.__name__ = "Unsigned32"
_AcSysVLANVlanNativeVlanId_Object = MibScalar
acSysVLANVlanNativeVlanId = _AcSysVLANVlanNativeVlanId_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 3, 10, 14),
    _AcSysVLANVlanNativeVlanId_Type()
)
acSysVLANVlanNativeVlanId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acSysVLANVlanNativeVlanId.setStatus("current")


class _AcSysVLANMode_Type(Integer32):
    """Custom type acSysVLANMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_AcSysVLANMode_Type.__name__ = "Integer32"
_AcSysVLANMode_Object = MibScalar
acSysVLANMode = _AcSysVLANMode_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 3, 10, 15),
    _AcSysVLANMode_Type()
)
acSysVLANMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acSysVLANMode.setStatus("current")


class _AcSysVLANOsnNativeVlanId_Type(Unsigned32):
    """Custom type acSysVLANOsnNativeVlanId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4000),
    )


_AcSysVLANOsnNativeVlanId_Type.__name__ = "Unsigned32"
_AcSysVLANOsnNativeVlanId_Object = MibScalar
acSysVLANOsnNativeVlanId = _AcSysVLANOsnNativeVlanId_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 3, 10, 16),
    _AcSysVLANOsnNativeVlanId_Type()
)
acSysVLANOsnNativeVlanId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acSysVLANOsnNativeVlanId.setStatus("current")
_AcSysVlanMapTable_Object = MibTable
acSysVlanMapTable = _AcSysVlanMapTable_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 3, 10, 21)
)
if mibBuilder.loadTexts:
    acSysVlanMapTable.setStatus("current")
_AcSysVlanMapEntry_Object = MibTableRow
acSysVlanMapEntry = _AcSysVlanMapEntry_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 3, 10, 21, 1)
)
acSysVlanMapEntry.setIndexNames(
    (0, "AC-SYSTEM-MIB", "acSysVlanMapIndex"),
)
if mibBuilder.loadTexts:
    acSysVlanMapEntry.setStatus("current")


class _AcSysVlanMapIndex_Type(Unsigned32):
    """Custom type acSysVlanMapIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_AcSysVlanMapIndex_Type.__name__ = "Unsigned32"
_AcSysVlanMapIndex_Object = MibTableColumn
acSysVlanMapIndex = _AcSysVlanMapIndex_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 3, 10, 21, 1, 1),
    _AcSysVlanMapIndex_Type()
)
acSysVlanMapIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    acSysVlanMapIndex.setStatus("current")
_AcSysVlanMapRowStatus_Type = RowStatus
_AcSysVlanMapRowStatus_Object = MibTableColumn
acSysVlanMapRowStatus = _AcSysVlanMapRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 3, 10, 21, 1, 2),
    _AcSysVlanMapRowStatus_Type()
)
acSysVlanMapRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acSysVlanMapRowStatus.setStatus("current")


class _AcSysVlanMapAction_Type(Integer32):
    """Custom type acSysVlanMapAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            0
        )
    )
    namedValues = NamedValues(
        ("none", 0)
    )


_AcSysVlanMapAction_Type.__name__ = "Integer32"
_AcSysVlanMapAction_Object = MibTableColumn
acSysVlanMapAction = _AcSysVlanMapAction_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 3, 10, 21, 1, 3),
    _AcSysVlanMapAction_Type()
)
acSysVlanMapAction.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acSysVlanMapAction.setStatus("current")


class _AcSysVlanMapActionRes_Type(Integer32):
    """Custom type acSysVlanMapActionRes based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            0
        )
    )
    namedValues = NamedValues(
        ("succeeded", 0)
    )


_AcSysVlanMapActionRes_Type.__name__ = "Integer32"
_AcSysVlanMapActionRes_Object = MibTableColumn
acSysVlanMapActionRes = _AcSysVlanMapActionRes_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 3, 10, 21, 1, 4),
    _AcSysVlanMapActionRes_Type()
)
acSysVlanMapActionRes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSysVlanMapActionRes.setStatus("current")


class _AcSysVlanMapDiffServ_Type(Unsigned32):
    """Custom type acSysVlanMapDiffServ based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_AcSysVlanMapDiffServ_Type.__name__ = "Unsigned32"
_AcSysVlanMapDiffServ_Object = MibTableColumn
acSysVlanMapDiffServ = _AcSysVlanMapDiffServ_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 3, 10, 21, 1, 5),
    _AcSysVlanMapDiffServ_Type()
)
acSysVlanMapDiffServ.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acSysVlanMapDiffServ.setStatus("current")


class _AcSysVlanMapVlanPriority_Type(Unsigned32):
    """Custom type acSysVlanMapVlanPriority based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_AcSysVlanMapVlanPriority_Type.__name__ = "Unsigned32"
_AcSysVlanMapVlanPriority_Object = MibTableColumn
acSysVlanMapVlanPriority = _AcSysVlanMapVlanPriority_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 3, 10, 21, 1, 6),
    _AcSysVlanMapVlanPriority_Type()
)
acSysVlanMapVlanPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acSysVlanMapVlanPriority.setStatus("current")
_AcSysSCTP_ObjectIdentity = ObjectIdentity
acSysSCTP = _AcSysSCTP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 3, 11)
)


class _AcSysSCTPHeartBeatInterval_Type(Unsigned32):
    """Custom type acSysSCTPHeartBeatInterval based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3600),
    )


_AcSysSCTPHeartBeatInterval_Type.__name__ = "Unsigned32"
_AcSysSCTPHeartBeatInterval_Object = MibScalar
acSysSCTPHeartBeatInterval = _AcSysSCTPHeartBeatInterval_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 3, 11, 1),
    _AcSysSCTPHeartBeatInterval_Type()
)
acSysSCTPHeartBeatInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acSysSCTPHeartBeatInterval.setStatus("obsolete")


class _AcSysSCTPT4SACKTimer_Type(Unsigned32):
    """Custom type acSysSCTPT4SACKTimer based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_AcSysSCTPT4SACKTimer_Type.__name__ = "Unsigned32"
_AcSysSCTPT4SACKTimer_Object = MibScalar
acSysSCTPT4SACKTimer = _AcSysSCTPT4SACKTimer_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 3, 11, 2),
    _AcSysSCTPT4SACKTimer_Type()
)
acSysSCTPT4SACKTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acSysSCTPT4SACKTimer.setStatus("obsolete")


class _AcSysSCTPCheckSumMethod_Type(Integer32):
    """Custom type acSysSCTPCheckSumMethod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("adler", 0),
          ("crc", 1))
    )


_AcSysSCTPCheckSumMethod_Type.__name__ = "Integer32"
_AcSysSCTPCheckSumMethod_Object = MibScalar
acSysSCTPCheckSumMethod = _AcSysSCTPCheckSumMethod_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 3, 11, 3),
    _AcSysSCTPCheckSumMethod_Type()
)
acSysSCTPCheckSumMethod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acSysSCTPCheckSumMethod.setStatus("obsolete")


class _AcSysSCTPHostName_Type(SnmpAdminString):
    """Custom type acSysSCTPHostName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_AcSysSCTPHostName_Type.__name__ = "SnmpAdminString"
_AcSysSCTPHostName_Object = MibScalar
acSysSCTPHostName = _AcSysSCTPHostName_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 3, 11, 4),
    _AcSysSCTPHostName_Type()
)
acSysSCTPHostName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acSysSCTPHostName.setStatus("obsolete")


class _AcSysSCTPAssociationsNum_Type(Unsigned32):
    """Custom type acSysSCTPAssociationsNum based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_AcSysSCTPAssociationsNum_Type.__name__ = "Unsigned32"
_AcSysSCTPAssociationsNum_Object = MibScalar
acSysSCTPAssociationsNum = _AcSysSCTPAssociationsNum_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 3, 11, 5),
    _AcSysSCTPAssociationsNum_Type()
)
acSysSCTPAssociationsNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acSysSCTPAssociationsNum.setStatus("obsolete")
_AcSysEthernetPort_ObjectIdentity = ObjectIdentity
acSysEthernetPort = _AcSysEthernetPort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 3, 12)
)


class _AcSysEthernetPortPhyConfiguration_Type(Integer32):
    """Custom type acSysEthernetPortPhyConfiguration based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              7)
        )
    )
    namedValues = NamedValues(
        *(("halfDuplex10BaseT", 0),
          ("fullDuplex10BaseT", 1),
          ("halfDuplex100BaseT", 2),
          ("fullDuplex100BaseT", 3),
          ("autoNegotiate", 4),
          ("fullDuplex1000BaseT", 7))
    )


_AcSysEthernetPortPhyConfiguration_Type.__name__ = "Integer32"
_AcSysEthernetPortPhyConfiguration_Object = MibScalar
acSysEthernetPortPhyConfiguration = _AcSysEthernetPortPhyConfiguration_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 3, 12, 1),
    _AcSysEthernetPortPhyConfiguration_Type()
)
acSysEthernetPortPhyConfiguration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acSysEthernetPortPhyConfiguration.setStatus("current")
_AcSysPOE_ObjectIdentity = ObjectIdentity
acSysPOE = _AcSysPOE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 3, 12, 21)
)
_AcSysPOETable_Object = MibTable
acSysPOETable = _AcSysPOETable_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 3, 12, 21, 1)
)
if mibBuilder.loadTexts:
    acSysPOETable.setStatus("current")
_AcSysPOEEntry_Object = MibTableRow
acSysPOEEntry = _AcSysPOEEntry_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 3, 12, 21, 1, 1)
)
acSysPOEEntry.setIndexNames(
    (0, "AC-SYSTEM-MIB", "acSysPOEIndex"),
)
if mibBuilder.loadTexts:
    acSysPOEEntry.setStatus("current")


class _AcSysPOEIndex_Type(Unsigned32):
    """Custom type acSysPOEIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 11),
    )


_AcSysPOEIndex_Type.__name__ = "Unsigned32"
_AcSysPOEIndex_Object = MibTableColumn
acSysPOEIndex = _AcSysPOEIndex_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 3, 12, 21, 1, 1, 1),
    _AcSysPOEIndex_Type()
)
acSysPOEIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    acSysPOEIndex.setStatus("current")
_AcSysPOERowStatus_Type = RowStatus
_AcSysPOERowStatus_Object = MibTableColumn
acSysPOERowStatus = _AcSysPOERowStatus_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 3, 12, 21, 1, 1, 2),
    _AcSysPOERowStatus_Type()
)
acSysPOERowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acSysPOERowStatus.setStatus("current")


class _AcSysPOEAction_Type(Integer32):
    """Custom type acSysPOEAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            0
        )
    )
    namedValues = NamedValues(
        ("none", 0)
    )


_AcSysPOEAction_Type.__name__ = "Integer32"
_AcSysPOEAction_Object = MibTableColumn
acSysPOEAction = _AcSysPOEAction_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 3, 12, 21, 1, 1, 3),
    _AcSysPOEAction_Type()
)
acSysPOEAction.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acSysPOEAction.setStatus("current")


class _AcSysPOEActionRes_Type(Integer32):
    """Custom type acSysPOEActionRes based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            0
        )
    )
    namedValues = NamedValues(
        ("succeeded", 0)
    )


_AcSysPOEActionRes_Type.__name__ = "Integer32"
_AcSysPOEActionRes_Object = MibTableColumn
acSysPOEActionRes = _AcSysPOEActionRes_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 3, 12, 21, 1, 1, 4),
    _AcSysPOEActionRes_Type()
)
acSysPOEActionRes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSysPOEActionRes.setStatus("current")


class _AcSysPOEPortEnable_Type(Integer32):
    """Custom type acSysPOEPortEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_AcSysPOEPortEnable_Type.__name__ = "Integer32"
_AcSysPOEPortEnable_Object = MibTableColumn
acSysPOEPortEnable = _AcSysPOEPortEnable_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 3, 12, 21, 1, 1, 5),
    _AcSysPOEPortEnable_Type()
)
acSysPOEPortEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acSysPOEPortEnable.setStatus("current")


class _AcSysPOEPortPower_Type(Unsigned32):
    """Custom type acSysPOEPortPower based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(4000, 30000),
    )


_AcSysPOEPortPower_Type.__name__ = "Unsigned32"
_AcSysPOEPortPower_Object = MibTableColumn
acSysPOEPortPower = _AcSysPOEPortPower_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 3, 12, 21, 1, 1, 6),
    _AcSysPOEPortPower_Type()
)
acSysPOEPortPower.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acSysPOEPortPower.setStatus("current")


class _AcSysPOEPortATEnable_Type(Integer32):
    """Custom type acSysPOEPortATEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_AcSysPOEPortATEnable_Type.__name__ = "Integer32"
_AcSysPOEPortATEnable_Object = MibTableColumn
acSysPOEPortATEnable = _AcSysPOEPortATEnable_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 3, 12, 21, 1, 1, 7),
    _AcSysPOEPortATEnable_Type()
)
acSysPOEPortATEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acSysPOEPortATEnable.setStatus("current")
_AcSysNetworkSettings_ObjectIdentity = ObjectIdentity
acSysNetworkSettings = _AcSysNetworkSettings_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 3, 13)
)


class _AcSysNetworkSettingsDisableICMPRedirects_Type(Integer32):
    """Custom type acSysNetworkSettingsDisableICMPRedirects based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_AcSysNetworkSettingsDisableICMPRedirects_Type.__name__ = "Integer32"
_AcSysNetworkSettingsDisableICMPRedirects_Object = MibScalar
acSysNetworkSettingsDisableICMPRedirects = _AcSysNetworkSettingsDisableICMPRedirects_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 3, 13, 1),
    _AcSysNetworkSettingsDisableICMPRedirects_Type()
)
acSysNetworkSettingsDisableICMPRedirects.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acSysNetworkSettingsDisableICMPRedirects.setStatus("current")


class _AcSysNetworkSettingsDisableICMPUnreachable_Type(Integer32):
    """Custom type acSysNetworkSettingsDisableICMPUnreachable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_AcSysNetworkSettingsDisableICMPUnreachable_Type.__name__ = "Integer32"
_AcSysNetworkSettingsDisableICMPUnreachable_Object = MibScalar
acSysNetworkSettingsDisableICMPUnreachable = _AcSysNetworkSettingsDisableICMPUnreachable_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 3, 13, 2),
    _AcSysNetworkSettingsDisableICMPUnreachable_Type()
)
acSysNetworkSettingsDisableICMPUnreachable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acSysNetworkSettingsDisableICMPUnreachable.setStatus("current")
_AcSysMiscConfig_ObjectIdentity = ObjectIdentity
acSysMiscConfig = _AcSysMiscConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 4)
)
_AcSysDiagnostics_ObjectIdentity = ObjectIdentity
acSysDiagnostics = _AcSysDiagnostics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 4, 1)
)


class _AcSysDiagnosticsEnable_Type(Integer32):
    """Custom type acSysDiagnosticsEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              99)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("builtInTest", 1),
          ("builtInTestwithPartialFlash", 2),
          ("builtInTestWithSDRAM", 3),
          ("builtInTestOnUtopiaVxb", 4),
          ("internalUse", 99))
    )


_AcSysDiagnosticsEnable_Type.__name__ = "Integer32"
_AcSysDiagnosticsEnable_Object = MibScalar
acSysDiagnosticsEnable = _AcSysDiagnosticsEnable_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 4, 1, 1),
    _AcSysDiagnosticsEnable_Type()
)
acSysDiagnosticsEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acSysDiagnosticsEnable.setStatus("current")


class _AcSysDiagnosticsEnablePerformanceThresholdAlarms_Type(Integer32):
    """Custom type acSysDiagnosticsEnablePerformanceThresholdAlarms based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_AcSysDiagnosticsEnablePerformanceThresholdAlarms_Type.__name__ = "Integer32"
_AcSysDiagnosticsEnablePerformanceThresholdAlarms_Object = MibScalar
acSysDiagnosticsEnablePerformanceThresholdAlarms = _AcSysDiagnosticsEnablePerformanceThresholdAlarms_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 4, 1, 2),
    _AcSysDiagnosticsEnablePerformanceThresholdAlarms_Type()
)
acSysDiagnosticsEnablePerformanceThresholdAlarms.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acSysDiagnosticsEnablePerformanceThresholdAlarms.setStatus("current")


class _AcSysDiagnosticsListOfActivitiesToLog_Type(SnmpAdminString):
    """Custom type acSysDiagnosticsListOfActivitiesToLog based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 35),
    )


_AcSysDiagnosticsListOfActivitiesToLog_Type.__name__ = "SnmpAdminString"
_AcSysDiagnosticsListOfActivitiesToLog_Object = MibScalar
acSysDiagnosticsListOfActivitiesToLog = _AcSysDiagnosticsListOfActivitiesToLog_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 4, 1, 3),
    _AcSysDiagnosticsListOfActivitiesToLog_Type()
)
acSysDiagnosticsListOfActivitiesToLog.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acSysDiagnosticsListOfActivitiesToLog.setStatus("current")
_AcSysGenericINI_ObjectIdentity = ObjectIdentity
acSysGenericINI = _AcSysGenericINI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 4, 2)
)


class _AcSysGenericINILine_Type(SnmpAdminString):
    """Custom type acSysGenericINILine based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 512),
    )


_AcSysGenericINILine_Type.__name__ = "SnmpAdminString"
_AcSysGenericINILine_Object = MibScalar
acSysGenericINILine = _AcSysGenericINILine_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 4, 2, 1),
    _AcSysGenericINILine_Type()
)
acSysGenericINILine.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acSysGenericINILine.setStatus("current")


class _AcSysGenericINISecureStartup_Type(Integer32):
    """Custom type acSysGenericINISecureStartup based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_AcSysGenericINISecureStartup_Type.__name__ = "Integer32"
_AcSysGenericINISecureStartup_Object = MibScalar
acSysGenericINISecureStartup = _AcSysGenericINISecureStartup_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 4, 2, 2),
    _AcSysGenericINISecureStartup_Type()
)
acSysGenericINISecureStartup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acSysGenericINISecureStartup.setStatus("current")
_AcSysGenericCli_ObjectIdentity = ObjectIdentity
acSysGenericCli = _AcSysGenericCli_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 4, 3)
)


class _AcSysGenericCliCommand_Type(SnmpAdminString):
    """Custom type acSysGenericCliCommand based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 512),
    )


_AcSysGenericCliCommand_Type.__name__ = "SnmpAdminString"
_AcSysGenericCliCommand_Object = MibScalar
acSysGenericCliCommand = _AcSysGenericCliCommand_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 4, 3, 1),
    _AcSysGenericCliCommand_Type()
)
acSysGenericCliCommand.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acSysGenericCliCommand.setStatus("current")


class _AcSysGenericCliCommandResponse_Type(SnmpAdminString):
    """Custom type acSysGenericCliCommandResponse based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 512),
    )


_AcSysGenericCliCommandResponse_Type.__name__ = "SnmpAdminString"
_AcSysGenericCliCommandResponse_Object = MibScalar
acSysGenericCliCommandResponse = _AcSysGenericCliCommandResponse_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 4, 3, 2),
    _AcSysGenericCliCommandResponse_Type()
)
acSysGenericCliCommandResponse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSysGenericCliCommandResponse.setStatus("current")
_AcSysLicenseKey_ObjectIdentity = ObjectIdentity
acSysLicenseKey = _AcSysLicenseKey_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 5)
)


class _AcSysLicenseKeyString_Type(SnmpAdminString):
    """Custom type acSysLicenseKeyString based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_AcSysLicenseKeyString_Type.__name__ = "SnmpAdminString"
_AcSysLicenseKeyString_Object = MibScalar
acSysLicenseKeyString = _AcSysLicenseKeyString_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 5, 1),
    _AcSysLicenseKeyString_Type()
)
acSysLicenseKeyString.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acSysLicenseKeyString.setStatus("current")


class _AcSysLicenseKeyActiveList_Type(SnmpAdminString):
    """Custom type acSysLicenseKeyActiveList based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 484),
    )


_AcSysLicenseKeyActiveList_Type.__name__ = "SnmpAdminString"
_AcSysLicenseKeyActiveList_Object = MibScalar
acSysLicenseKeyActiveList = _AcSysLicenseKeyActiveList_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 5, 2),
    _AcSysLicenseKeyActiveList_Type()
)
acSysLicenseKeyActiveList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSysLicenseKeyActiveList.setStatus("current")


class _AcSysLicenseKeyProductKey_Type(SnmpAdminString):
    """Custom type acSysLicenseKeyProductKey based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_AcSysLicenseKeyProductKey_Type.__name__ = "SnmpAdminString"
_AcSysLicenseKeyProductKey_Object = MibScalar
acSysLicenseKeyProductKey = _AcSysLicenseKeyProductKey_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 5, 3),
    _AcSysLicenseKeyProductKey_Type()
)
acSysLicenseKeyProductKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acSysLicenseKeyProductKey.setStatus("current")
_AcSysFile_ObjectIdentity = ObjectIdentity
acSysFile = _AcSysFile_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 6)
)


class _AcSysFileCpt_Type(SnmpAdminString):
    """Custom type acSysFileCpt based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 47),
    )


_AcSysFileCpt_Type.__name__ = "SnmpAdminString"
_AcSysFileCpt_Object = MibScalar
acSysFileCpt = _AcSysFileCpt_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 6, 1),
    _AcSysFileCpt_Type()
)
acSysFileCpt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSysFileCpt.setStatus("current")


class _AcSysFileVp_Type(SnmpAdminString):
    """Custom type acSysFileVp based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 47),
    )


_AcSysFileVp_Type.__name__ = "SnmpAdminString"
_AcSysFileVp_Object = MibScalar
acSysFileVp = _AcSysFileVp_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 6, 2),
    _AcSysFileVp_Type()
)
acSysFileVp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSysFileVp.setStatus("current")


class _AcSysFilePrerecordedTones_Type(SnmpAdminString):
    """Custom type acSysFilePrerecordedTones based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 47),
    )


_AcSysFilePrerecordedTones_Type.__name__ = "SnmpAdminString"
_AcSysFilePrerecordedTones_Object = MibScalar
acSysFilePrerecordedTones = _AcSysFilePrerecordedTones_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 6, 3),
    _AcSysFilePrerecordedTones_Type()
)
acSysFilePrerecordedTones.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSysFilePrerecordedTones.setStatus("current")


class _AcSysFileXml_Type(SnmpAdminString):
    """Custom type acSysFileXml based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 47),
    )


_AcSysFileXml_Type.__name__ = "SnmpAdminString"
_AcSysFileXml_Object = MibScalar
acSysFileXml = _AcSysFileXml_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 6, 4),
    _AcSysFileXml_Type()
)
acSysFileXml.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSysFileXml.setStatus("current")


class _AcSysFileExternalCoder_Type(SnmpAdminString):
    """Custom type acSysFileExternalCoder based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 47),
    )


_AcSysFileExternalCoder_Type.__name__ = "SnmpAdminString"
_AcSysFileExternalCoder_Object = MibScalar
acSysFileExternalCoder = _AcSysFileExternalCoder_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 6, 5),
    _AcSysFileExternalCoder_Type()
)
acSysFileExternalCoder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSysFileExternalCoder.setStatus("current")


class _AcSysFileUserInfo_Type(SnmpAdminString):
    """Custom type acSysFileUserInfo based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 47),
    )


_AcSysFileUserInfo_Type.__name__ = "SnmpAdminString"
_AcSysFileUserInfo_Object = MibScalar
acSysFileUserInfo = _AcSysFileUserInfo_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 6, 6),
    _AcSysFileUserInfo_Type()
)
acSysFileUserInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSysFileUserInfo.setStatus("current")


class _AcSysFileDialPlanFileName_Type(SnmpAdminString):
    """Custom type acSysFileDialPlanFileName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 47),
    )


_AcSysFileDialPlanFileName_Type.__name__ = "SnmpAdminString"
_AcSysFileDialPlanFileName_Object = MibScalar
acSysFileDialPlanFileName = _AcSysFileDialPlanFileName_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 6, 7),
    _AcSysFileDialPlanFileName_Type()
)
acSysFileDialPlanFileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSysFileDialPlanFileName.setStatus("current")


class _AcSysFileTLSPkeyFileName_Type(SnmpAdminString):
    """Custom type acSysFileTLSPkeyFileName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 47),
    )


_AcSysFileTLSPkeyFileName_Type.__name__ = "SnmpAdminString"
_AcSysFileTLSPkeyFileName_Object = MibScalar
acSysFileTLSPkeyFileName = _AcSysFileTLSPkeyFileName_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 6, 8),
    _AcSysFileTLSPkeyFileName_Type()
)
acSysFileTLSPkeyFileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSysFileTLSPkeyFileName.setStatus("current")


class _AcSysFileTLSCertFileName_Type(SnmpAdminString):
    """Custom type acSysFileTLSCertFileName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 47),
    )


_AcSysFileTLSCertFileName_Type.__name__ = "SnmpAdminString"
_AcSysFileTLSCertFileName_Object = MibScalar
acSysFileTLSCertFileName = _AcSysFileTLSCertFileName_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 6, 9),
    _AcSysFileTLSCertFileName_Type()
)
acSysFileTLSCertFileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSysFileTLSCertFileName.setStatus("current")


class _AcSysFileTLSRootFileName_Type(SnmpAdminString):
    """Custom type acSysFileTLSRootFileName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 47),
    )


_AcSysFileTLSRootFileName_Type.__name__ = "SnmpAdminString"
_AcSysFileTLSRootFileName_Object = MibScalar
acSysFileTLSRootFileName = _AcSysFileTLSRootFileName_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 6, 10),
    _AcSysFileTLSRootFileName_Type()
)
acSysFileTLSRootFileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSysFileTLSRootFileName.setStatus("current")


class _AcSysFileFirstVideoFontFileName_Type(SnmpAdminString):
    """Custom type acSysFileFirstVideoFontFileName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 47),
    )


_AcSysFileFirstVideoFontFileName_Type.__name__ = "SnmpAdminString"
_AcSysFileFirstVideoFontFileName_Object = MibScalar
acSysFileFirstVideoFontFileName = _AcSysFileFirstVideoFontFileName_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 6, 11),
    _AcSysFileFirstVideoFontFileName_Type()
)
acSysFileFirstVideoFontFileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSysFileFirstVideoFontFileName.setStatus("current")


class _AcSysFileSecondVideoFontFileName_Type(SnmpAdminString):
    """Custom type acSysFileSecondVideoFontFileName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 47),
    )


_AcSysFileSecondVideoFontFileName_Type.__name__ = "SnmpAdminString"
_AcSysFileSecondVideoFontFileName_Object = MibScalar
acSysFileSecondVideoFontFileName = _AcSysFileSecondVideoFontFileName_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 6, 12),
    _AcSysFileSecondVideoFontFileName_Type()
)
acSysFileSecondVideoFontFileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSysFileSecondVideoFontFileName.setStatus("current")


class _AcSysFileThirdVideoFontFileName_Type(SnmpAdminString):
    """Custom type acSysFileThirdVideoFontFileName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 47),
    )


_AcSysFileThirdVideoFontFileName_Type.__name__ = "SnmpAdminString"
_AcSysFileThirdVideoFontFileName_Object = MibScalar
acSysFileThirdVideoFontFileName = _AcSysFileThirdVideoFontFileName_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 6, 13),
    _AcSysFileThirdVideoFontFileName_Type()
)
acSysFileThirdVideoFontFileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSysFileThirdVideoFontFileName.setStatus("current")


class _AcSysFileV5PortConfFileName_Type(SnmpAdminString):
    """Custom type acSysFileV5PortConfFileName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 47),
    )


_AcSysFileV5PortConfFileName_Type.__name__ = "SnmpAdminString"
_AcSysFileV5PortConfFileName_Object = MibScalar
acSysFileV5PortConfFileName = _AcSysFileV5PortConfFileName_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 6, 14),
    _AcSysFileV5PortConfFileName_Type()
)
acSysFileV5PortConfFileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSysFileV5PortConfFileName.setStatus("current")


class _AcSysFileAmdSensitivityFileName_Type(SnmpAdminString):
    """Custom type acSysFileAmdSensitivityFileName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 47),
    )


_AcSysFileAmdSensitivityFileName_Type.__name__ = "SnmpAdminString"
_AcSysFileAmdSensitivityFileName_Object = MibScalar
acSysFileAmdSensitivityFileName = _AcSysFileAmdSensitivityFileName_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 6, 15),
    _AcSysFileAmdSensitivityFileName_Type()
)
acSysFileAmdSensitivityFileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSysFileAmdSensitivityFileName.setStatus("current")
_AcSysSecurity_ObjectIdentity = ObjectIdentity
acSysSecurity = _AcSysSecurity_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 7)
)


class _AcSysSecurityTLSVersion_Type(Integer32):
    """Custom type acSysSecurityTLSVersion based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("sSL-2-3-and-TLS-1", 0),
          ("tLS-1-only", 1))
    )


_AcSysSecurityTLSVersion_Type.__name__ = "Integer32"
_AcSysSecurityTLSVersion_Object = MibScalar
acSysSecurityTLSVersion = _AcSysSecurityTLSVersion_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 7, 1),
    _AcSysSecurityTLSVersion_Type()
)
acSysSecurityTLSVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acSysSecurityTLSVersion.setStatus("current")


class _AcSysSecurityOcspEnable_Type(Integer32):
    """Custom type acSysSecurityOcspEnable based on Integer32"""
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


_AcSysSecurityOcspEnable_Type.__name__ = "Integer32"
_AcSysSecurityOcspEnable_Object = MibScalar
acSysSecurityOcspEnable = _AcSysSecurityOcspEnable_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 7, 2),
    _AcSysSecurityOcspEnable_Type()
)
acSysSecurityOcspEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acSysSecurityOcspEnable.setStatus("current")
_AcSysSecurityOcspServerIPType_Type = InetAddressType
_AcSysSecurityOcspServerIPType_Object = MibScalar
acSysSecurityOcspServerIPType = _AcSysSecurityOcspServerIPType_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 7, 3),
    _AcSysSecurityOcspServerIPType_Type()
)
acSysSecurityOcspServerIPType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acSysSecurityOcspServerIPType.setStatus("current")
_AcSysSecurityOcspServerIP_Type = InetAddress
_AcSysSecurityOcspServerIP_Object = MibScalar
acSysSecurityOcspServerIP = _AcSysSecurityOcspServerIP_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 7, 4),
    _AcSysSecurityOcspServerIP_Type()
)
acSysSecurityOcspServerIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acSysSecurityOcspServerIP.setStatus("current")


class _AcSysSecurityOcspServerPort_Type(Unsigned32):
    """Custom type acSysSecurityOcspServerPort based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32767),
    )


_AcSysSecurityOcspServerPort_Type.__name__ = "Unsigned32"
_AcSysSecurityOcspServerPort_Object = MibScalar
acSysSecurityOcspServerPort = _AcSysSecurityOcspServerPort_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 7, 5),
    _AcSysSecurityOcspServerPort_Type()
)
acSysSecurityOcspServerPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acSysSecurityOcspServerPort.setStatus("current")


class _AcSysSecurityOcspDefaultResponse_Type(Integer32):
    """Custom type acSysSecurityOcspDefaultResponse based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("rejectPeerCertificate", 0),
          ("allowPeerCertificate", 1))
    )


_AcSysSecurityOcspDefaultResponse_Type.__name__ = "Integer32"
_AcSysSecurityOcspDefaultResponse_Object = MibScalar
acSysSecurityOcspDefaultResponse = _AcSysSecurityOcspDefaultResponse_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 7, 6),
    _AcSysSecurityOcspDefaultResponse_Type()
)
acSysSecurityOcspDefaultResponse.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acSysSecurityOcspDefaultResponse.setStatus("current")


class _AcSysSecurityTLSFIPS140Mode_Type(Integer32):
    """Custom type acSysSecurityTLSFIPS140Mode based on Integer32"""
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


_AcSysSecurityTLSFIPS140Mode_Type.__name__ = "Integer32"
_AcSysSecurityTLSFIPS140Mode_Object = MibScalar
acSysSecurityTLSFIPS140Mode = _AcSysSecurityTLSFIPS140Mode_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 7, 7),
    _AcSysSecurityTLSFIPS140Mode_Type()
)
acSysSecurityTLSFIPS140Mode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acSysSecurityTLSFIPS140Mode.setStatus("current")


class _AcSysSecurityGenCsrSubjectName_Type(SnmpAdminString):
    """Custom type acSysSecurityGenCsrSubjectName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 1200),
    )


_AcSysSecurityGenCsrSubjectName_Type.__name__ = "SnmpAdminString"
_AcSysSecurityGenCsrSubjectName_Object = MibScalar
acSysSecurityGenCsrSubjectName = _AcSysSecurityGenCsrSubjectName_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 7, 8),
    _AcSysSecurityGenCsrSubjectName_Type()
)
acSysSecurityGenCsrSubjectName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acSysSecurityGenCsrSubjectName.setStatus("current")


class _AcSysSecuritySelfSignedCertificateSubjectName_Type(SnmpAdminString):
    """Custom type acSysSecuritySelfSignedCertificateSubjectName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_AcSysSecuritySelfSignedCertificateSubjectName_Type.__name__ = "SnmpAdminString"
_AcSysSecuritySelfSignedCertificateSubjectName_Object = MibScalar
acSysSecuritySelfSignedCertificateSubjectName = _AcSysSecuritySelfSignedCertificateSubjectName_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 7, 9),
    _AcSysSecuritySelfSignedCertificateSubjectName_Type()
)
acSysSecuritySelfSignedCertificateSubjectName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acSysSecuritySelfSignedCertificateSubjectName.setStatus("current")
_AcSysSecurityOcspSecondaryServerIPType_Type = InetAddressType
_AcSysSecurityOcspSecondaryServerIPType_Object = MibScalar
acSysSecurityOcspSecondaryServerIPType = _AcSysSecurityOcspSecondaryServerIPType_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 7, 10),
    _AcSysSecurityOcspSecondaryServerIPType_Type()
)
acSysSecurityOcspSecondaryServerIPType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acSysSecurityOcspSecondaryServerIPType.setStatus("current")
_AcSysSecurityOcspSecondaryServerIP_Type = InetAddress
_AcSysSecurityOcspSecondaryServerIP_Object = MibScalar
acSysSecurityOcspSecondaryServerIP = _AcSysSecurityOcspSecondaryServerIP_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 7, 11),
    _AcSysSecurityOcspSecondaryServerIP_Type()
)
acSysSecurityOcspSecondaryServerIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acSysSecurityOcspSecondaryServerIP.setStatus("current")


class _AcSysSecurityHTTPSRequireClientCertificate_Type(Integer32):
    """Custom type acSysSecurityHTTPSRequireClientCertificate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_AcSysSecurityHTTPSRequireClientCertificate_Type.__name__ = "Integer32"
_AcSysSecurityHTTPSRequireClientCertificate_Object = MibScalar
acSysSecurityHTTPSRequireClientCertificate = _AcSysSecurityHTTPSRequireClientCertificate_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 7, 12),
    _AcSysSecurityHTTPSRequireClientCertificate_Type()
)
acSysSecurityHTTPSRequireClientCertificate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acSysSecurityHTTPSRequireClientCertificate.setStatus("current")


class _AcSysSecurityAUPDVerifyCertificates_Type(Integer32):
    """Custom type acSysSecurityAUPDVerifyCertificates based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_AcSysSecurityAUPDVerifyCertificates_Type.__name__ = "Integer32"
_AcSysSecurityAUPDVerifyCertificates_Object = MibScalar
acSysSecurityAUPDVerifyCertificates = _AcSysSecurityAUPDVerifyCertificates_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 7, 13),
    _AcSysSecurityAUPDVerifyCertificates_Type()
)
acSysSecurityAUPDVerifyCertificates.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acSysSecurityAUPDVerifyCertificates.setStatus("current")


class _AcSysSecurityRequireStrictCertification_Type(Integer32):
    """Custom type acSysSecurityRequireStrictCertification based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_AcSysSecurityRequireStrictCertification_Type.__name__ = "Integer32"
_AcSysSecurityRequireStrictCertification_Object = MibScalar
acSysSecurityRequireStrictCertification = _AcSysSecurityRequireStrictCertification_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 7, 14),
    _AcSysSecurityRequireStrictCertification_Type()
)
acSysSecurityRequireStrictCertification.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acSysSecurityRequireStrictCertification.setStatus("current")


class _AcSysSecurityTLSExpiryCheckStart_Type(Unsigned32):
    """Custom type acSysSecurityTLSExpiryCheckStart based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3650),
    )


_AcSysSecurityTLSExpiryCheckStart_Type.__name__ = "Unsigned32"
_AcSysSecurityTLSExpiryCheckStart_Object = MibScalar
acSysSecurityTLSExpiryCheckStart = _AcSysSecurityTLSExpiryCheckStart_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 7, 15),
    _AcSysSecurityTLSExpiryCheckStart_Type()
)
acSysSecurityTLSExpiryCheckStart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acSysSecurityTLSExpiryCheckStart.setStatus("current")


class _AcSysSecurityTLSExpiryCheckPeriod_Type(Unsigned32):
    """Custom type acSysSecurityTLSExpiryCheckPeriod based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3650),
    )


_AcSysSecurityTLSExpiryCheckPeriod_Type.__name__ = "Unsigned32"
_AcSysSecurityTLSExpiryCheckPeriod_Object = MibScalar
acSysSecurityTLSExpiryCheckPeriod = _AcSysSecurityTLSExpiryCheckPeriod_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 7, 16),
    _AcSysSecurityTLSExpiryCheckPeriod_Type()
)
acSysSecurityTLSExpiryCheckPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acSysSecurityTLSExpiryCheckPeriod.setStatus("current")
_AcSysIKE_ObjectIdentity = ObjectIdentity
acSysIKE = _AcSysIKE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 7, 21)
)
_AcSysIKEPolicyTable_Object = MibTable
acSysIKEPolicyTable = _AcSysIKEPolicyTable_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 7, 21, 1)
)
if mibBuilder.loadTexts:
    acSysIKEPolicyTable.setStatus("obsolete")
_AcSysIKEPolicyEntry_Object = MibTableRow
acSysIKEPolicyEntry = _AcSysIKEPolicyEntry_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 7, 21, 1, 1)
)
acSysIKEPolicyEntry.setIndexNames(
    (0, "AC-SYSTEM-MIB", "acSysIKEPolicyIndex"),
)
if mibBuilder.loadTexts:
    acSysIKEPolicyEntry.setStatus("obsolete")


class _AcSysIKEPolicyIndex_Type(Unsigned32):
    """Custom type acSysIKEPolicyIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 19),
    )


_AcSysIKEPolicyIndex_Type.__name__ = "Unsigned32"
_AcSysIKEPolicyIndex_Object = MibTableColumn
acSysIKEPolicyIndex = _AcSysIKEPolicyIndex_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 7, 21, 1, 1, 1),
    _AcSysIKEPolicyIndex_Type()
)
acSysIKEPolicyIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    acSysIKEPolicyIndex.setStatus("obsolete")
_AcSysIKEPolicyRowStatus_Type = RowStatus
_AcSysIKEPolicyRowStatus_Object = MibTableColumn
acSysIKEPolicyRowStatus = _AcSysIKEPolicyRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 7, 21, 1, 1, 2),
    _AcSysIKEPolicyRowStatus_Type()
)
acSysIKEPolicyRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acSysIKEPolicyRowStatus.setStatus("obsolete")


class _AcSysIKEPolicyAction_Type(Integer32):
    """Custom type acSysIKEPolicyAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            0
        )
    )
    namedValues = NamedValues(
        ("none", 0)
    )


_AcSysIKEPolicyAction_Type.__name__ = "Integer32"
_AcSysIKEPolicyAction_Object = MibTableColumn
acSysIKEPolicyAction = _AcSysIKEPolicyAction_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 7, 21, 1, 1, 3),
    _AcSysIKEPolicyAction_Type()
)
acSysIKEPolicyAction.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acSysIKEPolicyAction.setStatus("obsolete")


class _AcSysIKEPolicyActionRes_Type(Integer32):
    """Custom type acSysIKEPolicyActionRes based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            0
        )
    )
    namedValues = NamedValues(
        ("succeeded", 0)
    )


_AcSysIKEPolicyActionRes_Type.__name__ = "Integer32"
_AcSysIKEPolicyActionRes_Object = MibTableColumn
acSysIKEPolicyActionRes = _AcSysIKEPolicyActionRes_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 7, 21, 1, 1, 4),
    _AcSysIKEPolicyActionRes_Type()
)
acSysIKEPolicyActionRes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSysIKEPolicyActionRes.setStatus("obsolete")


class _AcSysIKEPolicyShardKey_Type(SnmpAdminString):
    """Custom type acSysIKEPolicyShardKey based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_AcSysIKEPolicyShardKey_Type.__name__ = "SnmpAdminString"
_AcSysIKEPolicyShardKey_Object = MibTableColumn
acSysIKEPolicyShardKey = _AcSysIKEPolicyShardKey_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 7, 21, 1, 1, 5),
    _AcSysIKEPolicyShardKey_Type()
)
acSysIKEPolicyShardKey.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acSysIKEPolicyShardKey.setStatus("obsolete")


class _AcSysIKEPolicyLifeInSeconds_Type(Unsigned32):
    """Custom type acSysIKEPolicyLifeInSeconds based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AcSysIKEPolicyLifeInSeconds_Type.__name__ = "Unsigned32"
_AcSysIKEPolicyLifeInSeconds_Object = MibTableColumn
acSysIKEPolicyLifeInSeconds = _AcSysIKEPolicyLifeInSeconds_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 7, 21, 1, 1, 6),
    _AcSysIKEPolicyLifeInSeconds_Type()
)
acSysIKEPolicyLifeInSeconds.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acSysIKEPolicyLifeInSeconds.setStatus("obsolete")


class _AcSysIKEPolicyLifeInKB_Type(Unsigned32):
    """Custom type acSysIKEPolicyLifeInKB based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AcSysIKEPolicyLifeInKB_Type.__name__ = "Unsigned32"
_AcSysIKEPolicyLifeInKB_Object = MibTableColumn
acSysIKEPolicyLifeInKB = _AcSysIKEPolicyLifeInKB_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 7, 21, 1, 1, 7),
    _AcSysIKEPolicyLifeInKB_Type()
)
acSysIKEPolicyLifeInKB.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acSysIKEPolicyLifeInKB.setStatus("obsolete")


class _AcSysIKEPolicyProposal0Encryption_Type(Integer32):
    """Custom type acSysIKEPolicyProposal0Encryption based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              10)
        )
    )
    namedValues = NamedValues(
        *(("dES-CBC", 1),
          ("triple-DES-CBC", 2),
          ("aES", 3),
          ("not-set", 10))
    )


_AcSysIKEPolicyProposal0Encryption_Type.__name__ = "Integer32"
_AcSysIKEPolicyProposal0Encryption_Object = MibTableColumn
acSysIKEPolicyProposal0Encryption = _AcSysIKEPolicyProposal0Encryption_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 7, 21, 1, 1, 8),
    _AcSysIKEPolicyProposal0Encryption_Type()
)
acSysIKEPolicyProposal0Encryption.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acSysIKEPolicyProposal0Encryption.setStatus("obsolete")


class _AcSysIKEPolicyProposal1Encryption_Type(Integer32):
    """Custom type acSysIKEPolicyProposal1Encryption based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              10)
        )
    )
    namedValues = NamedValues(
        *(("dES-CBC", 1),
          ("triple-DES-CBC", 2),
          ("aES", 3),
          ("not-set", 10))
    )


_AcSysIKEPolicyProposal1Encryption_Type.__name__ = "Integer32"
_AcSysIKEPolicyProposal1Encryption_Object = MibTableColumn
acSysIKEPolicyProposal1Encryption = _AcSysIKEPolicyProposal1Encryption_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 7, 21, 1, 1, 9),
    _AcSysIKEPolicyProposal1Encryption_Type()
)
acSysIKEPolicyProposal1Encryption.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acSysIKEPolicyProposal1Encryption.setStatus("obsolete")


class _AcSysIKEPolicyProposal2Encryption_Type(Integer32):
    """Custom type acSysIKEPolicyProposal2Encryption based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              10)
        )
    )
    namedValues = NamedValues(
        *(("dES-CBC", 1),
          ("triple-DES-CBC", 2),
          ("aES", 3),
          ("not-set", 10))
    )


_AcSysIKEPolicyProposal2Encryption_Type.__name__ = "Integer32"
_AcSysIKEPolicyProposal2Encryption_Object = MibTableColumn
acSysIKEPolicyProposal2Encryption = _AcSysIKEPolicyProposal2Encryption_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 7, 21, 1, 1, 10),
    _AcSysIKEPolicyProposal2Encryption_Type()
)
acSysIKEPolicyProposal2Encryption.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acSysIKEPolicyProposal2Encryption.setStatus("obsolete")


class _AcSysIKEPolicyProposal3Encryption_Type(Integer32):
    """Custom type acSysIKEPolicyProposal3Encryption based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              10)
        )
    )
    namedValues = NamedValues(
        *(("dES-CBC", 1),
          ("triple-DES-CBC", 2),
          ("aES", 3),
          ("not-set", 10))
    )


_AcSysIKEPolicyProposal3Encryption_Type.__name__ = "Integer32"
_AcSysIKEPolicyProposal3Encryption_Object = MibTableColumn
acSysIKEPolicyProposal3Encryption = _AcSysIKEPolicyProposal3Encryption_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 7, 21, 1, 1, 11),
    _AcSysIKEPolicyProposal3Encryption_Type()
)
acSysIKEPolicyProposal3Encryption.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acSysIKEPolicyProposal3Encryption.setStatus("obsolete")


class _AcSysIKEPolicyProposal0Authentication_Type(Integer32):
    """Custom type acSysIKEPolicyProposal0Authentication based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              4,
              10)
        )
    )
    namedValues = NamedValues(
        *(("hMAC-SHA-1-96", 2),
          ("hMAC-MD5-96", 4),
          ("not-set", 10))
    )


_AcSysIKEPolicyProposal0Authentication_Type.__name__ = "Integer32"
_AcSysIKEPolicyProposal0Authentication_Object = MibTableColumn
acSysIKEPolicyProposal0Authentication = _AcSysIKEPolicyProposal0Authentication_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 7, 21, 1, 1, 12),
    _AcSysIKEPolicyProposal0Authentication_Type()
)
acSysIKEPolicyProposal0Authentication.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acSysIKEPolicyProposal0Authentication.setStatus("obsolete")


class _AcSysIKEPolicyProposal1Authentication_Type(Integer32):
    """Custom type acSysIKEPolicyProposal1Authentication based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              4,
              10)
        )
    )
    namedValues = NamedValues(
        *(("hMAC-SHA-1-96", 2),
          ("hMAC-MD5-96", 4),
          ("not-set", 10))
    )


_AcSysIKEPolicyProposal1Authentication_Type.__name__ = "Integer32"
_AcSysIKEPolicyProposal1Authentication_Object = MibTableColumn
acSysIKEPolicyProposal1Authentication = _AcSysIKEPolicyProposal1Authentication_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 7, 21, 1, 1, 13),
    _AcSysIKEPolicyProposal1Authentication_Type()
)
acSysIKEPolicyProposal1Authentication.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acSysIKEPolicyProposal1Authentication.setStatus("obsolete")


class _AcSysIKEPolicyProposal2Authentication_Type(Integer32):
    """Custom type acSysIKEPolicyProposal2Authentication based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              4,
              10)
        )
    )
    namedValues = NamedValues(
        *(("hMAC-SHA-1-96", 2),
          ("hMAC-MD5-96", 4),
          ("not-set", 10))
    )


_AcSysIKEPolicyProposal2Authentication_Type.__name__ = "Integer32"
_AcSysIKEPolicyProposal2Authentication_Object = MibTableColumn
acSysIKEPolicyProposal2Authentication = _AcSysIKEPolicyProposal2Authentication_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 7, 21, 1, 1, 14),
    _AcSysIKEPolicyProposal2Authentication_Type()
)
acSysIKEPolicyProposal2Authentication.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acSysIKEPolicyProposal2Authentication.setStatus("obsolete")


class _AcSysIKEPolicyProposal3Authentication_Type(Integer32):
    """Custom type acSysIKEPolicyProposal3Authentication based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              4,
              10)
        )
    )
    namedValues = NamedValues(
        *(("hMAC-SHA-1-96", 2),
          ("hMAC-MD5-96", 4),
          ("not-set", 10))
    )


_AcSysIKEPolicyProposal3Authentication_Type.__name__ = "Integer32"
_AcSysIKEPolicyProposal3Authentication_Object = MibTableColumn
acSysIKEPolicyProposal3Authentication = _AcSysIKEPolicyProposal3Authentication_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 7, 21, 1, 1, 15),
    _AcSysIKEPolicyProposal3Authentication_Type()
)
acSysIKEPolicyProposal3Authentication.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acSysIKEPolicyProposal3Authentication.setStatus("obsolete")


class _AcSysIKEPolicyProposal0DHGroup_Type(Integer32):
    """Custom type acSysIKEPolicyProposal0DHGroup based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              10)
        )
    )
    namedValues = NamedValues(
        *(("dH-786-BIT", 0),
          ("dH-1024-BIT", 1),
          ("not-set", 10))
    )


_AcSysIKEPolicyProposal0DHGroup_Type.__name__ = "Integer32"
_AcSysIKEPolicyProposal0DHGroup_Object = MibTableColumn
acSysIKEPolicyProposal0DHGroup = _AcSysIKEPolicyProposal0DHGroup_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 7, 21, 1, 1, 16),
    _AcSysIKEPolicyProposal0DHGroup_Type()
)
acSysIKEPolicyProposal0DHGroup.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acSysIKEPolicyProposal0DHGroup.setStatus("obsolete")


class _AcSysIKEPolicyProposal1DHGroup_Type(Integer32):
    """Custom type acSysIKEPolicyProposal1DHGroup based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              10)
        )
    )
    namedValues = NamedValues(
        *(("dH-786-BIT", 0),
          ("dH-1024-BIT", 1),
          ("not-set", 10))
    )


_AcSysIKEPolicyProposal1DHGroup_Type.__name__ = "Integer32"
_AcSysIKEPolicyProposal1DHGroup_Object = MibTableColumn
acSysIKEPolicyProposal1DHGroup = _AcSysIKEPolicyProposal1DHGroup_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 7, 21, 1, 1, 17),
    _AcSysIKEPolicyProposal1DHGroup_Type()
)
acSysIKEPolicyProposal1DHGroup.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acSysIKEPolicyProposal1DHGroup.setStatus("obsolete")


class _AcSysIKEPolicyProposal2DHGroup_Type(Integer32):
    """Custom type acSysIKEPolicyProposal2DHGroup based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              10)
        )
    )
    namedValues = NamedValues(
        *(("dH-786-BIT", 0),
          ("dH-1024-BIT", 1),
          ("not-set", 10))
    )


_AcSysIKEPolicyProposal2DHGroup_Type.__name__ = "Integer32"
_AcSysIKEPolicyProposal2DHGroup_Object = MibTableColumn
acSysIKEPolicyProposal2DHGroup = _AcSysIKEPolicyProposal2DHGroup_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 7, 21, 1, 1, 18),
    _AcSysIKEPolicyProposal2DHGroup_Type()
)
acSysIKEPolicyProposal2DHGroup.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acSysIKEPolicyProposal2DHGroup.setStatus("obsolete")


class _AcSysIKEPolicyProposal3DHGroup_Type(Integer32):
    """Custom type acSysIKEPolicyProposal3DHGroup based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              10)
        )
    )
    namedValues = NamedValues(
        *(("dH-786-BIT", 0),
          ("dH-1024-BIT", 1),
          ("not-set", 10))
    )


_AcSysIKEPolicyProposal3DHGroup_Type.__name__ = "Integer32"
_AcSysIKEPolicyProposal3DHGroup_Object = MibTableColumn
acSysIKEPolicyProposal3DHGroup = _AcSysIKEPolicyProposal3DHGroup_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 7, 21, 1, 1, 19),
    _AcSysIKEPolicyProposal3DHGroup_Type()
)
acSysIKEPolicyProposal3DHGroup.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acSysIKEPolicyProposal3DHGroup.setStatus("obsolete")


class _AcSysIKEPolicyAuthenticationMethod_Type(Integer32):
    """Custom type acSysIKEPolicyAuthenticationMethod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("presharedKey", 0),
          ("rsaSignature", 1))
    )


_AcSysIKEPolicyAuthenticationMethod_Type.__name__ = "Integer32"
_AcSysIKEPolicyAuthenticationMethod_Object = MibTableColumn
acSysIKEPolicyAuthenticationMethod = _AcSysIKEPolicyAuthenticationMethod_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 7, 21, 1, 1, 20),
    _AcSysIKEPolicyAuthenticationMethod_Type()
)
acSysIKEPolicyAuthenticationMethod.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acSysIKEPolicyAuthenticationMethod.setStatus("obsolete")
_AcSysIPSec_ObjectIdentity = ObjectIdentity
acSysIPSec = _AcSysIPSec_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 7, 22)
)


class _AcSysIPSecEnable_Type(Integer32):
    """Custom type acSysIPSecEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("yes", 1))
    )


_AcSysIPSecEnable_Type.__name__ = "Integer32"
_AcSysIPSecEnable_Object = MibScalar
acSysIPSecEnable = _AcSysIPSecEnable_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 7, 22, 1),
    _AcSysIPSecEnable_Type()
)
acSysIPSecEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acSysIPSecEnable.setStatus("obsolete")


class _AcSysIPSecDpdMode_Type(Integer32):
    """Custom type acSysIPSecDpdMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("periodic", 1),
          ("ondemand", 2))
    )


_AcSysIPSecDpdMode_Type.__name__ = "Integer32"
_AcSysIPSecDpdMode_Object = MibScalar
acSysIPSecDpdMode = _AcSysIPSecDpdMode_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 7, 22, 2),
    _AcSysIPSecDpdMode_Type()
)
acSysIPSecDpdMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acSysIPSecDpdMode.setStatus("obsolete")


class _AcSysIPSecIKECertificateExtValidate_Type(Integer32):
    """Custom type acSysIPSecIKECertificateExtValidate based on Integer32"""
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


_AcSysIPSecIKECertificateExtValidate_Type.__name__ = "Integer32"
_AcSysIPSecIKECertificateExtValidate_Object = MibScalar
acSysIPSecIKECertificateExtValidate = _AcSysIPSecIKECertificateExtValidate_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 7, 22, 3),
    _AcSysIPSecIKECertificateExtValidate_Type()
)
acSysIPSecIKECertificateExtValidate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acSysIPSecIKECertificateExtValidate.setStatus("obsolete")
_AcSysIPSecSPDTable_Object = MibTable
acSysIPSecSPDTable = _AcSysIPSecSPDTable_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 7, 22, 21)
)
if mibBuilder.loadTexts:
    acSysIPSecSPDTable.setStatus("obsolete")
_AcSysIPSecSPDEntry_Object = MibTableRow
acSysIPSecSPDEntry = _AcSysIPSecSPDEntry_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 7, 22, 21, 1)
)
acSysIPSecSPDEntry.setIndexNames(
    (0, "AC-SYSTEM-MIB", "acSysIPSecSPDIndex"),
)
if mibBuilder.loadTexts:
    acSysIPSecSPDEntry.setStatus("obsolete")


class _AcSysIPSecSPDIndex_Type(Unsigned32):
    """Custom type acSysIPSecSPDIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 19),
    )


_AcSysIPSecSPDIndex_Type.__name__ = "Unsigned32"
_AcSysIPSecSPDIndex_Object = MibTableColumn
acSysIPSecSPDIndex = _AcSysIPSecSPDIndex_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 7, 22, 21, 1, 1),
    _AcSysIPSecSPDIndex_Type()
)
acSysIPSecSPDIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    acSysIPSecSPDIndex.setStatus("obsolete")
_AcSysIPSecSPDRowStatus_Type = RowStatus
_AcSysIPSecSPDRowStatus_Object = MibTableColumn
acSysIPSecSPDRowStatus = _AcSysIPSecSPDRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 7, 22, 21, 1, 2),
    _AcSysIPSecSPDRowStatus_Type()
)
acSysIPSecSPDRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acSysIPSecSPDRowStatus.setStatus("obsolete")


class _AcSysIPSecSPDAction_Type(Integer32):
    """Custom type acSysIPSecSPDAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            0
        )
    )
    namedValues = NamedValues(
        ("none", 0)
    )


_AcSysIPSecSPDAction_Type.__name__ = "Integer32"
_AcSysIPSecSPDAction_Object = MibTableColumn
acSysIPSecSPDAction = _AcSysIPSecSPDAction_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 7, 22, 21, 1, 3),
    _AcSysIPSecSPDAction_Type()
)
acSysIPSecSPDAction.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acSysIPSecSPDAction.setStatus("obsolete")


class _AcSysIPSecSPDActionRes_Type(Integer32):
    """Custom type acSysIPSecSPDActionRes based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            0
        )
    )
    namedValues = NamedValues(
        ("succeeded", 0)
    )


_AcSysIPSecSPDActionRes_Type.__name__ = "Integer32"
_AcSysIPSecSPDActionRes_Object = MibTableColumn
acSysIPSecSPDActionRes = _AcSysIPSecSPDActionRes_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 7, 22, 21, 1, 4),
    _AcSysIPSecSPDActionRes_Type()
)
acSysIPSecSPDActionRes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSysIPSecSPDActionRes.setStatus("obsolete")


class _AcSysIPSecSPDPolicyRemoteIPAddr_Type(SnmpAdminString):
    """Custom type acSysIPSecSPDPolicyRemoteIPAddr based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 99),
    )


_AcSysIPSecSPDPolicyRemoteIPAddr_Type.__name__ = "SnmpAdminString"
_AcSysIPSecSPDPolicyRemoteIPAddr_Object = MibTableColumn
acSysIPSecSPDPolicyRemoteIPAddr = _AcSysIPSecSPDPolicyRemoteIPAddr_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 7, 22, 21, 1, 5),
    _AcSysIPSecSPDPolicyRemoteIPAddr_Type()
)
acSysIPSecSPDPolicyRemoteIPAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acSysIPSecSPDPolicyRemoteIPAddr.setStatus("obsolete")


class _AcSysIPSecSPDPolicySrcPort_Type(Unsigned32):
    """Custom type acSysIPSecSPDPolicySrcPort based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_AcSysIPSecSPDPolicySrcPort_Type.__name__ = "Unsigned32"
_AcSysIPSecSPDPolicySrcPort_Object = MibTableColumn
acSysIPSecSPDPolicySrcPort = _AcSysIPSecSPDPolicySrcPort_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 7, 22, 21, 1, 6),
    _AcSysIPSecSPDPolicySrcPort_Type()
)
acSysIPSecSPDPolicySrcPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acSysIPSecSPDPolicySrcPort.setStatus("obsolete")


class _AcSysIPSecSPDPolicyDestPort_Type(Unsigned32):
    """Custom type acSysIPSecSPDPolicyDestPort based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_AcSysIPSecSPDPolicyDestPort_Type.__name__ = "Unsigned32"
_AcSysIPSecSPDPolicyDestPort_Object = MibTableColumn
acSysIPSecSPDPolicyDestPort = _AcSysIPSecSPDPolicyDestPort_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 7, 22, 21, 1, 7),
    _AcSysIPSecSPDPolicyDestPort_Type()
)
acSysIPSecSPDPolicyDestPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acSysIPSecSPDPolicyDestPort.setStatus("obsolete")


class _AcSysIPSecSPDPolicyProtocol_Type(Unsigned32):
    """Custom type acSysIPSecSPDPolicyProtocol based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AcSysIPSecSPDPolicyProtocol_Type.__name__ = "Unsigned32"
_AcSysIPSecSPDPolicyProtocol_Object = MibTableColumn
acSysIPSecSPDPolicyProtocol = _AcSysIPSecSPDPolicyProtocol_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 7, 22, 21, 1, 8),
    _AcSysIPSecSPDPolicyProtocol_Type()
)
acSysIPSecSPDPolicyProtocol.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acSysIPSecSPDPolicyProtocol.setStatus("obsolete")


class _AcSysIPSecSPDKeyExchangeMethodIndex_Type(Unsigned32):
    """Custom type acSysIPSecSPDKeyExchangeMethodIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AcSysIPSecSPDKeyExchangeMethodIndex_Type.__name__ = "Unsigned32"
_AcSysIPSecSPDKeyExchangeMethodIndex_Object = MibTableColumn
acSysIPSecSPDKeyExchangeMethodIndex = _AcSysIPSecSPDKeyExchangeMethodIndex_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 7, 22, 21, 1, 9),
    _AcSysIPSecSPDKeyExchangeMethodIndex_Type()
)
acSysIPSecSPDKeyExchangeMethodIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acSysIPSecSPDKeyExchangeMethodIndex.setStatus("obsolete")


class _AcSysIPSecSPDLifeInSeconds_Type(Unsigned32):
    """Custom type acSysIPSecSPDLifeInSeconds based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AcSysIPSecSPDLifeInSeconds_Type.__name__ = "Unsigned32"
_AcSysIPSecSPDLifeInSeconds_Object = MibTableColumn
acSysIPSecSPDLifeInSeconds = _AcSysIPSecSPDLifeInSeconds_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 7, 22, 21, 1, 10),
    _AcSysIPSecSPDLifeInSeconds_Type()
)
acSysIPSecSPDLifeInSeconds.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acSysIPSecSPDLifeInSeconds.setStatus("obsolete")


class _AcSysIPSecSPDLifeInKB_Type(Unsigned32):
    """Custom type acSysIPSecSPDLifeInKB based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AcSysIPSecSPDLifeInKB_Type.__name__ = "Unsigned32"
_AcSysIPSecSPDLifeInKB_Object = MibTableColumn
acSysIPSecSPDLifeInKB = _AcSysIPSecSPDLifeInKB_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 7, 22, 21, 1, 11),
    _AcSysIPSecSPDLifeInKB_Type()
)
acSysIPSecSPDLifeInKB.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acSysIPSecSPDLifeInKB.setStatus("obsolete")


class _AcSysIPSecSPDProposal0Encryption_Type(Integer32):
    """Custom type acSysIPSecSPDProposal0Encryption based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              10)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("dES-CBC", 1),
          ("triple-DES-CBC", 2),
          ("aES", 3),
          ("not-set", 10))
    )


_AcSysIPSecSPDProposal0Encryption_Type.__name__ = "Integer32"
_AcSysIPSecSPDProposal0Encryption_Object = MibTableColumn
acSysIPSecSPDProposal0Encryption = _AcSysIPSecSPDProposal0Encryption_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 7, 22, 21, 1, 12),
    _AcSysIPSecSPDProposal0Encryption_Type()
)
acSysIPSecSPDProposal0Encryption.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acSysIPSecSPDProposal0Encryption.setStatus("obsolete")


class _AcSysIPSecSPDProposal1Encryption_Type(Integer32):
    """Custom type acSysIPSecSPDProposal1Encryption based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              10)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("dES-CBC", 1),
          ("triple-DES-CBC", 2),
          ("aES", 3),
          ("not-set", 10))
    )


_AcSysIPSecSPDProposal1Encryption_Type.__name__ = "Integer32"
_AcSysIPSecSPDProposal1Encryption_Object = MibTableColumn
acSysIPSecSPDProposal1Encryption = _AcSysIPSecSPDProposal1Encryption_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 7, 22, 21, 1, 13),
    _AcSysIPSecSPDProposal1Encryption_Type()
)
acSysIPSecSPDProposal1Encryption.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acSysIPSecSPDProposal1Encryption.setStatus("obsolete")


class _AcSysIPSecSPDProposal2Encryption_Type(Integer32):
    """Custom type acSysIPSecSPDProposal2Encryption based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              10)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("dES-CBC", 1),
          ("triple-DES-CBC", 2),
          ("aES", 3),
          ("not-set", 10))
    )


_AcSysIPSecSPDProposal2Encryption_Type.__name__ = "Integer32"
_AcSysIPSecSPDProposal2Encryption_Object = MibTableColumn
acSysIPSecSPDProposal2Encryption = _AcSysIPSecSPDProposal2Encryption_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 7, 22, 21, 1, 14),
    _AcSysIPSecSPDProposal2Encryption_Type()
)
acSysIPSecSPDProposal2Encryption.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acSysIPSecSPDProposal2Encryption.setStatus("obsolete")


class _AcSysIPSecSPDProposal3Encryption_Type(Integer32):
    """Custom type acSysIPSecSPDProposal3Encryption based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              10)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("dES-CBC", 1),
          ("triple-DES-CBC", 2),
          ("aES", 3),
          ("not-set", 10))
    )


_AcSysIPSecSPDProposal3Encryption_Type.__name__ = "Integer32"
_AcSysIPSecSPDProposal3Encryption_Object = MibTableColumn
acSysIPSecSPDProposal3Encryption = _AcSysIPSecSPDProposal3Encryption_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 7, 22, 21, 1, 15),
    _AcSysIPSecSPDProposal3Encryption_Type()
)
acSysIPSecSPDProposal3Encryption.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acSysIPSecSPDProposal3Encryption.setStatus("obsolete")


class _AcSysIPSecSPDProposal0Authentication_Type(Integer32):
    """Custom type acSysIPSecSPDProposal0Authentication based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              4,
              10)
        )
    )
    namedValues = NamedValues(
        *(("hMAC-SHA-1-96", 2),
          ("hMAC-MD5-96", 4),
          ("not-set", 10))
    )


_AcSysIPSecSPDProposal0Authentication_Type.__name__ = "Integer32"
_AcSysIPSecSPDProposal0Authentication_Object = MibTableColumn
acSysIPSecSPDProposal0Authentication = _AcSysIPSecSPDProposal0Authentication_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 7, 22, 21, 1, 16),
    _AcSysIPSecSPDProposal0Authentication_Type()
)
acSysIPSecSPDProposal0Authentication.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acSysIPSecSPDProposal0Authentication.setStatus("obsolete")


class _AcSysIPSecSPDProposal1Authentication_Type(Integer32):
    """Custom type acSysIPSecSPDProposal1Authentication based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              4,
              10)
        )
    )
    namedValues = NamedValues(
        *(("hMAC-SHA-1-96", 2),
          ("hMAC-MD5-96", 4),
          ("not-set", 10))
    )


_AcSysIPSecSPDProposal1Authentication_Type.__name__ = "Integer32"
_AcSysIPSecSPDProposal1Authentication_Object = MibTableColumn
acSysIPSecSPDProposal1Authentication = _AcSysIPSecSPDProposal1Authentication_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 7, 22, 21, 1, 17),
    _AcSysIPSecSPDProposal1Authentication_Type()
)
acSysIPSecSPDProposal1Authentication.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acSysIPSecSPDProposal1Authentication.setStatus("obsolete")


class _AcSysIPSecSPDProposal2Authentication_Type(Integer32):
    """Custom type acSysIPSecSPDProposal2Authentication based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              4,
              10)
        )
    )
    namedValues = NamedValues(
        *(("hMAC-SHA-1-96", 2),
          ("hMAC-MD5-96", 4),
          ("not-set", 10))
    )


_AcSysIPSecSPDProposal2Authentication_Type.__name__ = "Integer32"
_AcSysIPSecSPDProposal2Authentication_Object = MibTableColumn
acSysIPSecSPDProposal2Authentication = _AcSysIPSecSPDProposal2Authentication_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 7, 22, 21, 1, 18),
    _AcSysIPSecSPDProposal2Authentication_Type()
)
acSysIPSecSPDProposal2Authentication.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acSysIPSecSPDProposal2Authentication.setStatus("obsolete")


class _AcSysIPSecSPDProposal3Authentication_Type(Integer32):
    """Custom type acSysIPSecSPDProposal3Authentication based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              4,
              10)
        )
    )
    namedValues = NamedValues(
        *(("hMAC-SHA-1-96", 2),
          ("hMAC-MD5-96", 4),
          ("not-set", 10))
    )


_AcSysIPSecSPDProposal3Authentication_Type.__name__ = "Integer32"
_AcSysIPSecSPDProposal3Authentication_Object = MibTableColumn
acSysIPSecSPDProposal3Authentication = _AcSysIPSecSPDProposal3Authentication_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 7, 22, 21, 1, 19),
    _AcSysIPSecSPDProposal3Authentication_Type()
)
acSysIPSecSPDProposal3Authentication.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acSysIPSecSPDProposal3Authentication.setStatus("obsolete")


class _AcSysIPSecSPDPolicyLocalIPAddrType_Type(Integer32):
    """Custom type acSysIPSecSPDPolicyLocalIPAddrType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              2)
        )
    )
    namedValues = NamedValues(
        *(("oam", 0),
          ("control", 2))
    )


_AcSysIPSecSPDPolicyLocalIPAddrType_Type.__name__ = "Integer32"
_AcSysIPSecSPDPolicyLocalIPAddrType_Object = MibTableColumn
acSysIPSecSPDPolicyLocalIPAddrType = _AcSysIPSecSPDPolicyLocalIPAddrType_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 7, 22, 21, 1, 20),
    _AcSysIPSecSPDPolicyLocalIPAddrType_Type()
)
acSysIPSecSPDPolicyLocalIPAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acSysIPSecSPDPolicyLocalIPAddrType.setStatus("obsolete")


class _AcSysIPSecSPDMode_Type(Integer32):
    """Custom type acSysIPSecSPDMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("transport", 0),
          ("tunneling", 1))
    )


_AcSysIPSecSPDMode_Type.__name__ = "Integer32"
_AcSysIPSecSPDMode_Object = MibTableColumn
acSysIPSecSPDMode = _AcSysIPSecSPDMode_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 7, 22, 21, 1, 21),
    _AcSysIPSecSPDMode_Type()
)
acSysIPSecSPDMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acSysIPSecSPDMode.setStatus("obsolete")
_AcSysIPSecSPDPolicyRemoteTunnelIPAddress_Type = IpAddress
_AcSysIPSecSPDPolicyRemoteTunnelIPAddress_Object = MibTableColumn
acSysIPSecSPDPolicyRemoteTunnelIPAddress = _AcSysIPSecSPDPolicyRemoteTunnelIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 7, 22, 21, 1, 22),
    _AcSysIPSecSPDPolicyRemoteTunnelIPAddress_Type()
)
acSysIPSecSPDPolicyRemoteTunnelIPAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acSysIPSecSPDPolicyRemoteTunnelIPAddress.setStatus("obsolete")
_AcSysIPSecSPDPolicyLocalTunnelIPAddress_Type = IpAddress
_AcSysIPSecSPDPolicyLocalTunnelIPAddress_Object = MibTableColumn
acSysIPSecSPDPolicyLocalTunnelIPAddress = _AcSysIPSecSPDPolicyLocalTunnelIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 7, 22, 21, 1, 23),
    _AcSysIPSecSPDPolicyLocalTunnelIPAddress_Type()
)
acSysIPSecSPDPolicyLocalTunnelIPAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acSysIPSecSPDPolicyLocalTunnelIPAddress.setStatus("obsolete")
_AcSysIPSecSPDPolicyRemoteTunnelSubnetMask_Type = IpAddress
_AcSysIPSecSPDPolicyRemoteTunnelSubnetMask_Object = MibTableColumn
acSysIPSecSPDPolicyRemoteTunnelSubnetMask = _AcSysIPSecSPDPolicyRemoteTunnelSubnetMask_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 7, 22, 21, 1, 24),
    _AcSysIPSecSPDPolicyRemoteTunnelSubnetMask_Type()
)
acSysIPSecSPDPolicyRemoteTunnelSubnetMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acSysIPSecSPDPolicyRemoteTunnelSubnetMask.setStatus("obsolete")
_AcSysIPsecProposalTable_Object = MibTable
acSysIPsecProposalTable = _AcSysIPsecProposalTable_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 7, 22, 22)
)
if mibBuilder.loadTexts:
    acSysIPsecProposalTable.setStatus("obsolete")
_AcSysIPsecProposalEntry_Object = MibTableRow
acSysIPsecProposalEntry = _AcSysIPsecProposalEntry_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 7, 22, 22, 1)
)
acSysIPsecProposalEntry.setIndexNames(
    (0, "AC-SYSTEM-MIB", "acSysIPsecProposalIndex"),
)
if mibBuilder.loadTexts:
    acSysIPsecProposalEntry.setStatus("obsolete")


class _AcSysIPsecProposalIndex_Type(Unsigned32):
    """Custom type acSysIPsecProposalIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4),
    )


_AcSysIPsecProposalIndex_Type.__name__ = "Unsigned32"
_AcSysIPsecProposalIndex_Object = MibTableColumn
acSysIPsecProposalIndex = _AcSysIPsecProposalIndex_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 7, 22, 22, 1, 1),
    _AcSysIPsecProposalIndex_Type()
)
acSysIPsecProposalIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    acSysIPsecProposalIndex.setStatus("obsolete")
_AcSysIPsecProposalRowStatus_Type = RowStatus
_AcSysIPsecProposalRowStatus_Object = MibTableColumn
acSysIPsecProposalRowStatus = _AcSysIPsecProposalRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 7, 22, 22, 1, 2),
    _AcSysIPsecProposalRowStatus_Type()
)
acSysIPsecProposalRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acSysIPsecProposalRowStatus.setStatus("obsolete")


class _AcSysIPsecProposalAction_Type(Integer32):
    """Custom type acSysIPsecProposalAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            0
        )
    )
    namedValues = NamedValues(
        ("none", 0)
    )


_AcSysIPsecProposalAction_Type.__name__ = "Integer32"
_AcSysIPsecProposalAction_Object = MibTableColumn
acSysIPsecProposalAction = _AcSysIPsecProposalAction_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 7, 22, 22, 1, 3),
    _AcSysIPsecProposalAction_Type()
)
acSysIPsecProposalAction.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acSysIPsecProposalAction.setStatus("obsolete")


class _AcSysIPsecProposalActionRes_Type(Integer32):
    """Custom type acSysIPsecProposalActionRes based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            0
        )
    )
    namedValues = NamedValues(
        ("succeeded", 0)
    )


_AcSysIPsecProposalActionRes_Type.__name__ = "Integer32"
_AcSysIPsecProposalActionRes_Object = MibTableColumn
acSysIPsecProposalActionRes = _AcSysIPsecProposalActionRes_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 7, 22, 22, 1, 4),
    _AcSysIPsecProposalActionRes_Type()
)
acSysIPsecProposalActionRes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSysIPsecProposalActionRes.setStatus("obsolete")


class _AcSysIPsecProposalEncryptionAlgorithm_Type(Integer32):
    """Custom type acSysIPsecProposalEncryptionAlgorithm based on Integer32"""
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
          ("desCbc", 1),
          ("tripleDesCbc", 2),
          ("aes", 3))
    )


_AcSysIPsecProposalEncryptionAlgorithm_Type.__name__ = "Integer32"
_AcSysIPsecProposalEncryptionAlgorithm_Object = MibTableColumn
acSysIPsecProposalEncryptionAlgorithm = _AcSysIPsecProposalEncryptionAlgorithm_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 7, 22, 22, 1, 5),
    _AcSysIPsecProposalEncryptionAlgorithm_Type()
)
acSysIPsecProposalEncryptionAlgorithm.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acSysIPsecProposalEncryptionAlgorithm.setStatus("obsolete")


class _AcSysIPsecProposalAuthenticationAlgorithm_Type(Integer32):
    """Custom type acSysIPsecProposalAuthenticationAlgorithm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              2,
              4)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("hmacSha1-96", 2),
          ("hmacMd5-96", 4))
    )


_AcSysIPsecProposalAuthenticationAlgorithm_Type.__name__ = "Integer32"
_AcSysIPsecProposalAuthenticationAlgorithm_Object = MibTableColumn
acSysIPsecProposalAuthenticationAlgorithm = _AcSysIPsecProposalAuthenticationAlgorithm_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 7, 22, 22, 1, 6),
    _AcSysIPsecProposalAuthenticationAlgorithm_Type()
)
acSysIPsecProposalAuthenticationAlgorithm.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acSysIPsecProposalAuthenticationAlgorithm.setStatus("obsolete")


class _AcSysIPsecProposalDiffieHellmanGroup_Type(Integer32):
    """Custom type acSysIPsecProposalDiffieHellmanGroup based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("group1-768Bits", 0),
          ("group2-1024Bits", 1))
    )


_AcSysIPsecProposalDiffieHellmanGroup_Type.__name__ = "Integer32"
_AcSysIPsecProposalDiffieHellmanGroup_Object = MibTableColumn
acSysIPsecProposalDiffieHellmanGroup = _AcSysIPsecProposalDiffieHellmanGroup_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 7, 22, 22, 1, 7),
    _AcSysIPsecProposalDiffieHellmanGroup_Type()
)
acSysIPsecProposalDiffieHellmanGroup.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acSysIPsecProposalDiffieHellmanGroup.setStatus("obsolete")
_AcSysIPsecSATable_Object = MibTable
acSysIPsecSATable = _AcSysIPsecSATable_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 7, 22, 23)
)
if mibBuilder.loadTexts:
    acSysIPsecSATable.setStatus("obsolete")
_AcSysIPsecSAEntry_Object = MibTableRow
acSysIPsecSAEntry = _AcSysIPsecSAEntry_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 7, 22, 23, 1)
)
acSysIPsecSAEntry.setIndexNames(
    (0, "AC-SYSTEM-MIB", "acSysIPsecSAIndex"),
)
if mibBuilder.loadTexts:
    acSysIPsecSAEntry.setStatus("obsolete")


class _AcSysIPsecSAIndex_Type(Unsigned32):
    """Custom type acSysIPsecSAIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 20),
    )


_AcSysIPsecSAIndex_Type.__name__ = "Unsigned32"
_AcSysIPsecSAIndex_Object = MibTableColumn
acSysIPsecSAIndex = _AcSysIPsecSAIndex_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 7, 22, 23, 1, 1),
    _AcSysIPsecSAIndex_Type()
)
acSysIPsecSAIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    acSysIPsecSAIndex.setStatus("obsolete")
_AcSysIPsecSARowStatus_Type = RowStatus
_AcSysIPsecSARowStatus_Object = MibTableColumn
acSysIPsecSARowStatus = _AcSysIPsecSARowStatus_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 7, 22, 23, 1, 2),
    _AcSysIPsecSARowStatus_Type()
)
acSysIPsecSARowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acSysIPsecSARowStatus.setStatus("obsolete")


class _AcSysIPsecSAAction_Type(Unsigned32):
    """Custom type acSysIPsecSAAction based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
    )


_AcSysIPsecSAAction_Type.__name__ = "Unsigned32"
_AcSysIPsecSAAction_Object = MibTableColumn
acSysIPsecSAAction = _AcSysIPsecSAAction_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 7, 22, 23, 1, 3),
    _AcSysIPsecSAAction_Type()
)
acSysIPsecSAAction.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acSysIPsecSAAction.setStatus("obsolete")


class _AcSysIPsecSAActionRes_Type(Unsigned32):
    """Custom type acSysIPsecSAActionRes based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
    )


_AcSysIPsecSAActionRes_Type.__name__ = "Unsigned32"
_AcSysIPsecSAActionRes_Object = MibTableColumn
acSysIPsecSAActionRes = _AcSysIPsecSAActionRes_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 7, 22, 23, 1, 4),
    _AcSysIPsecSAActionRes_Type()
)
acSysIPsecSAActionRes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSysIPsecSAActionRes.setStatus("obsolete")


class _AcSysIPsecSARemoteEndpointAddress_Type(SnmpAdminString):
    """Custom type acSysIPsecSARemoteEndpointAddress based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 98),
    )


_AcSysIPsecSARemoteEndpointAddress_Type.__name__ = "SnmpAdminString"
_AcSysIPsecSARemoteEndpointAddress_Object = MibTableColumn
acSysIPsecSARemoteEndpointAddress = _AcSysIPsecSARemoteEndpointAddress_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 7, 22, 23, 1, 5),
    _AcSysIPsecSARemoteEndpointAddress_Type()
)
acSysIPsecSARemoteEndpointAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acSysIPsecSARemoteEndpointAddress.setStatus("obsolete")


class _AcSysIPsecSAAuthenticationMethod_Type(Integer32):
    """Custom type acSysIPsecSAAuthenticationMethod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("presharedKey", 0),
          ("rSASignature", 1))
    )


_AcSysIPsecSAAuthenticationMethod_Type.__name__ = "Integer32"
_AcSysIPsecSAAuthenticationMethod_Object = MibTableColumn
acSysIPsecSAAuthenticationMethod = _AcSysIPsecSAAuthenticationMethod_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 7, 22, 23, 1, 6),
    _AcSysIPsecSAAuthenticationMethod_Type()
)
acSysIPsecSAAuthenticationMethod.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acSysIPsecSAAuthenticationMethod.setStatus("obsolete")


class _AcSysIPsecSASharedKey_Type(SnmpAdminString):
    """Custom type acSysIPsecSASharedKey based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 79),
    )


_AcSysIPsecSASharedKey_Type.__name__ = "SnmpAdminString"
_AcSysIPsecSASharedKey_Object = MibTableColumn
acSysIPsecSASharedKey = _AcSysIPsecSASharedKey_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 7, 22, 23, 1, 7),
    _AcSysIPsecSASharedKey_Type()
)
acSysIPsecSASharedKey.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acSysIPsecSASharedKey.setStatus("obsolete")


class _AcSysIPsecSASourcePort_Type(Unsigned32):
    """Custom type acSysIPsecSASourcePort based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AcSysIPsecSASourcePort_Type.__name__ = "Unsigned32"
_AcSysIPsecSASourcePort_Object = MibTableColumn
acSysIPsecSASourcePort = _AcSysIPsecSASourcePort_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 7, 22, 23, 1, 8),
    _AcSysIPsecSASourcePort_Type()
)
acSysIPsecSASourcePort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acSysIPsecSASourcePort.setStatus("obsolete")


class _AcSysIPsecSADestPort_Type(Unsigned32):
    """Custom type acSysIPsecSADestPort based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AcSysIPsecSADestPort_Type.__name__ = "Unsigned32"
_AcSysIPsecSADestPort_Object = MibTableColumn
acSysIPsecSADestPort = _AcSysIPsecSADestPort_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 7, 22, 23, 1, 9),
    _AcSysIPsecSADestPort_Type()
)
acSysIPsecSADestPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acSysIPsecSADestPort.setStatus("obsolete")


class _AcSysIPsecSAProtocol_Type(Unsigned32):
    """Custom type acSysIPsecSAProtocol based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AcSysIPsecSAProtocol_Type.__name__ = "Unsigned32"
_AcSysIPsecSAProtocol_Object = MibTableColumn
acSysIPsecSAProtocol = _AcSysIPsecSAProtocol_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 7, 22, 23, 1, 10),
    _AcSysIPsecSAProtocol_Type()
)
acSysIPsecSAProtocol.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acSysIPsecSAProtocol.setStatus("obsolete")


class _AcSysIPsecSAPhase1SaLifetimeInSec_Type(Unsigned32):
    """Custom type acSysIPsecSAPhase1SaLifetimeInSec based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AcSysIPsecSAPhase1SaLifetimeInSec_Type.__name__ = "Unsigned32"
_AcSysIPsecSAPhase1SaLifetimeInSec_Object = MibTableColumn
acSysIPsecSAPhase1SaLifetimeInSec = _AcSysIPsecSAPhase1SaLifetimeInSec_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 7, 22, 23, 1, 11),
    _AcSysIPsecSAPhase1SaLifetimeInSec_Type()
)
acSysIPsecSAPhase1SaLifetimeInSec.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acSysIPsecSAPhase1SaLifetimeInSec.setStatus("obsolete")


class _AcSysIPsecSAPhase2SaLifetimeInSec_Type(Unsigned32):
    """Custom type acSysIPsecSAPhase2SaLifetimeInSec based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AcSysIPsecSAPhase2SaLifetimeInSec_Type.__name__ = "Unsigned32"
_AcSysIPsecSAPhase2SaLifetimeInSec_Object = MibTableColumn
acSysIPsecSAPhase2SaLifetimeInSec = _AcSysIPsecSAPhase2SaLifetimeInSec_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 7, 22, 23, 1, 12),
    _AcSysIPsecSAPhase2SaLifetimeInSec_Type()
)
acSysIPsecSAPhase2SaLifetimeInSec.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acSysIPsecSAPhase2SaLifetimeInSec.setStatus("obsolete")


class _AcSysIPsecSAPhase2SaLifetimeInKB_Type(Unsigned32):
    """Custom type acSysIPsecSAPhase2SaLifetimeInKB based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AcSysIPsecSAPhase2SaLifetimeInKB_Type.__name__ = "Unsigned32"
_AcSysIPsecSAPhase2SaLifetimeInKB_Object = MibTableColumn
acSysIPsecSAPhase2SaLifetimeInKB = _AcSysIPsecSAPhase2SaLifetimeInKB_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 7, 22, 23, 1, 13),
    _AcSysIPsecSAPhase2SaLifetimeInKB_Type()
)
acSysIPsecSAPhase2SaLifetimeInKB.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acSysIPsecSAPhase2SaLifetimeInKB.setStatus("obsolete")


class _AcSysIPsecSADPDmode_Type(Integer32):
    """Custom type acSysIPsecSADPDmode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dPDDisabled", 0),
          ("dPDPeriodic", 1),
          ("dPDOnDemand", 2))
    )


_AcSysIPsecSADPDmode_Type.__name__ = "Integer32"
_AcSysIPsecSADPDmode_Object = MibTableColumn
acSysIPsecSADPDmode = _AcSysIPsecSADPDmode_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 7, 22, 23, 1, 14),
    _AcSysIPsecSADPDmode_Type()
)
acSysIPsecSADPDmode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acSysIPsecSADPDmode.setStatus("obsolete")


class _AcSysIPsecSAIPsecMode_Type(Integer32):
    """Custom type acSysIPsecSAIPsecMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("transport", 0),
          ("tunnel", 1))
    )


_AcSysIPsecSAIPsecMode_Type.__name__ = "Integer32"
_AcSysIPsecSAIPsecMode_Object = MibTableColumn
acSysIPsecSAIPsecMode = _AcSysIPsecSAIPsecMode_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 7, 22, 23, 1, 15),
    _AcSysIPsecSAIPsecMode_Type()
)
acSysIPsecSAIPsecMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acSysIPsecSAIPsecMode.setStatus("obsolete")


class _AcSysIPsecSARemoteTunnelAddress_Type(SnmpAdminString):
    """Custom type acSysIPsecSARemoteTunnelAddress based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 45),
    )


_AcSysIPsecSARemoteTunnelAddress_Type.__name__ = "SnmpAdminString"
_AcSysIPsecSARemoteTunnelAddress_Object = MibTableColumn
acSysIPsecSARemoteTunnelAddress = _AcSysIPsecSARemoteTunnelAddress_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 7, 22, 23, 1, 16),
    _AcSysIPsecSARemoteTunnelAddress_Type()
)
acSysIPsecSARemoteTunnelAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acSysIPsecSARemoteTunnelAddress.setStatus("obsolete")


class _AcSysIPsecSARemoteSubnetIPAddress_Type(SnmpAdminString):
    """Custom type acSysIPsecSARemoteSubnetIPAddress based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 45),
    )


_AcSysIPsecSARemoteSubnetIPAddress_Type.__name__ = "SnmpAdminString"
_AcSysIPsecSARemoteSubnetIPAddress_Object = MibTableColumn
acSysIPsecSARemoteSubnetIPAddress = _AcSysIPsecSARemoteSubnetIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 7, 22, 23, 1, 17),
    _AcSysIPsecSARemoteSubnetIPAddress_Type()
)
acSysIPsecSARemoteSubnetIPAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acSysIPsecSARemoteSubnetIPAddress.setStatus("obsolete")


class _AcSysIPsecSARemoteSubnetPrefixLength_Type(Unsigned32):
    """Custom type acSysIPsecSARemoteSubnetPrefixLength based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_AcSysIPsecSARemoteSubnetPrefixLength_Type.__name__ = "Unsigned32"
_AcSysIPsecSARemoteSubnetPrefixLength_Object = MibTableColumn
acSysIPsecSARemoteSubnetPrefixLength = _AcSysIPsecSARemoteSubnetPrefixLength_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 7, 22, 23, 1, 18),
    _AcSysIPsecSARemoteSubnetPrefixLength_Type()
)
acSysIPsecSARemoteSubnetPrefixLength.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acSysIPsecSARemoteSubnetPrefixLength.setStatus("obsolete")
_AcSysIPsecSAInterfaceName_Type = RowPointer
_AcSysIPsecSAInterfaceName_Object = MibTableColumn
acSysIPsecSAInterfaceName = _AcSysIPsecSAInterfaceName_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 7, 22, 23, 1, 19),
    _AcSysIPsecSAInterfaceName_Type()
)
acSysIPsecSAInterfaceName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acSysIPsecSAInterfaceName.setStatus("obsolete")
_AcFirewall_ObjectIdentity = ObjectIdentity
acFirewall = _AcFirewall_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 7, 23)
)
_AcSysAccessListTable_Object = MibTable
acSysAccessListTable = _AcSysAccessListTable_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 7, 23, 1)
)
if mibBuilder.loadTexts:
    acSysAccessListTable.setStatus("current")
_AcSysAccessListEntry_Object = MibTableRow
acSysAccessListEntry = _AcSysAccessListEntry_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 7, 23, 1, 1)
)
acSysAccessListEntry.setIndexNames(
    (0, "AC-SYSTEM-MIB", "acSysAccessListIndex"),
)
if mibBuilder.loadTexts:
    acSysAccessListEntry.setStatus("current")


class _AcSysAccessListIndex_Type(Unsigned32):
    """Custom type acSysAccessListIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 49),
    )


_AcSysAccessListIndex_Type.__name__ = "Unsigned32"
_AcSysAccessListIndex_Object = MibTableColumn
acSysAccessListIndex = _AcSysAccessListIndex_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 7, 23, 1, 1, 1),
    _AcSysAccessListIndex_Type()
)
acSysAccessListIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    acSysAccessListIndex.setStatus("current")
_AcSysAccessListRowStatus_Type = RowStatus
_AcSysAccessListRowStatus_Object = MibTableColumn
acSysAccessListRowStatus = _AcSysAccessListRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 7, 23, 1, 1, 2),
    _AcSysAccessListRowStatus_Type()
)
acSysAccessListRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acSysAccessListRowStatus.setStatus("current")


class _AcSysAccessListAction_Type(Integer32):
    """Custom type acSysAccessListAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            0
        )
    )
    namedValues = NamedValues(
        ("none", 0)
    )


_AcSysAccessListAction_Type.__name__ = "Integer32"
_AcSysAccessListAction_Object = MibTableColumn
acSysAccessListAction = _AcSysAccessListAction_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 7, 23, 1, 1, 3),
    _AcSysAccessListAction_Type()
)
acSysAccessListAction.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acSysAccessListAction.setStatus("current")


class _AcSysAccessListActionRes_Type(Integer32):
    """Custom type acSysAccessListActionRes based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            0
        )
    )
    namedValues = NamedValues(
        ("succeeded", 0)
    )


_AcSysAccessListActionRes_Type.__name__ = "Integer32"
_AcSysAccessListActionRes_Object = MibTableColumn
acSysAccessListActionRes = _AcSysAccessListActionRes_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 7, 23, 1, 1, 4),
    _AcSysAccessListActionRes_Type()
)
acSysAccessListActionRes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSysAccessListActionRes.setStatus("current")


class _AcSysAccessListSourceIP_Type(SnmpAdminString):
    """Custom type acSysAccessListSourceIP based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 60),
    )


_AcSysAccessListSourceIP_Type.__name__ = "SnmpAdminString"
_AcSysAccessListSourceIP_Object = MibTableColumn
acSysAccessListSourceIP = _AcSysAccessListSourceIP_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 7, 23, 1, 1, 5),
    _AcSysAccessListSourceIP_Type()
)
acSysAccessListSourceIP.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acSysAccessListSourceIP.setStatus("current")
_AcSysAccessListNetMask_Type = IpAddress
_AcSysAccessListNetMask_Object = MibTableColumn
acSysAccessListNetMask = _AcSysAccessListNetMask_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 7, 23, 1, 1, 6),
    _AcSysAccessListNetMask_Type()
)
acSysAccessListNetMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acSysAccessListNetMask.setStatus("obsolete")


class _AcSysAccessListStartPort_Type(Unsigned32):
    """Custom type acSysAccessListStartPort based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AcSysAccessListStartPort_Type.__name__ = "Unsigned32"
_AcSysAccessListStartPort_Object = MibTableColumn
acSysAccessListStartPort = _AcSysAccessListStartPort_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 7, 23, 1, 1, 7),
    _AcSysAccessListStartPort_Type()
)
acSysAccessListStartPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acSysAccessListStartPort.setStatus("current")


class _AcSysAccessListEndPort_Type(Unsigned32):
    """Custom type acSysAccessListEndPort based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AcSysAccessListEndPort_Type.__name__ = "Unsigned32"
_AcSysAccessListEndPort_Object = MibTableColumn
acSysAccessListEndPort = _AcSysAccessListEndPort_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 7, 23, 1, 1, 8),
    _AcSysAccessListEndPort_Type()
)
acSysAccessListEndPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acSysAccessListEndPort.setStatus("current")


class _AcSysAccessListProtocol_Type(SnmpAdminString):
    """Custom type acSysAccessListProtocol based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_AcSysAccessListProtocol_Type.__name__ = "SnmpAdminString"
_AcSysAccessListProtocol_Object = MibTableColumn
acSysAccessListProtocol = _AcSysAccessListProtocol_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 7, 23, 1, 1, 9),
    _AcSysAccessListProtocol_Type()
)
acSysAccessListProtocol.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acSysAccessListProtocol.setStatus("current")


class _AcSysAccessListPacketSize_Type(Unsigned32):
    """Custom type acSysAccessListPacketSize based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AcSysAccessListPacketSize_Type.__name__ = "Unsigned32"
_AcSysAccessListPacketSize_Object = MibTableColumn
acSysAccessListPacketSize = _AcSysAccessListPacketSize_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 7, 23, 1, 1, 10),
    _AcSysAccessListPacketSize_Type()
)
acSysAccessListPacketSize.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acSysAccessListPacketSize.setStatus("current")


class _AcSysAccessListByteRate_Type(Unsigned32):
    """Custom type acSysAccessListByteRate based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AcSysAccessListByteRate_Type.__name__ = "Unsigned32"
_AcSysAccessListByteRate_Object = MibTableColumn
acSysAccessListByteRate = _AcSysAccessListByteRate_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 7, 23, 1, 1, 11),
    _AcSysAccessListByteRate_Type()
)
acSysAccessListByteRate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acSysAccessListByteRate.setStatus("current")


class _AcSysAccessListByteBurst_Type(Unsigned32):
    """Custom type acSysAccessListByteBurst based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AcSysAccessListByteBurst_Type.__name__ = "Unsigned32"
_AcSysAccessListByteBurst_Object = MibTableColumn
acSysAccessListByteBurst = _AcSysAccessListByteBurst_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 7, 23, 1, 1, 12),
    _AcSysAccessListByteBurst_Type()
)
acSysAccessListByteBurst.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acSysAccessListByteBurst.setStatus("current")


class _AcSysAccessListAllowType_Type(Integer32):
    """Custom type acSysAccessListAllowType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notSet", 0),
          ("allow", 1),
          ("block", 2))
    )


_AcSysAccessListAllowType_Type.__name__ = "Integer32"
_AcSysAccessListAllowType_Object = MibTableColumn
acSysAccessListAllowType = _AcSysAccessListAllowType_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 7, 23, 1, 1, 13),
    _AcSysAccessListAllowType_Type()
)
acSysAccessListAllowType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acSysAccessListAllowType.setStatus("current")


class _AcSysAccessListMatchCount_Type(Unsigned32):
    """Custom type acSysAccessListMatchCount based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AcSysAccessListMatchCount_Type.__name__ = "Unsigned32"
_AcSysAccessListMatchCount_Object = MibTableColumn
acSysAccessListMatchCount = _AcSysAccessListMatchCount_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 7, 23, 1, 1, 14),
    _AcSysAccessListMatchCount_Type()
)
acSysAccessListMatchCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSysAccessListMatchCount.setStatus("current")


class _AcSysAccessListInterfaceName_Type(SnmpAdminString):
    """Custom type acSysAccessListInterfaceName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_AcSysAccessListInterfaceName_Type.__name__ = "SnmpAdminString"
_AcSysAccessListInterfaceName_Object = MibTableColumn
acSysAccessListInterfaceName = _AcSysAccessListInterfaceName_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 7, 23, 1, 1, 15),
    _AcSysAccessListInterfaceName_Type()
)
acSysAccessListInterfaceName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acSysAccessListInterfaceName.setStatus("current")


class _AcSysAccessListUseSpecificInterface_Type(Integer32):
    """Custom type acSysAccessListUseSpecificInterface based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_AcSysAccessListUseSpecificInterface_Type.__name__ = "Integer32"
_AcSysAccessListUseSpecificInterface_Object = MibTableColumn
acSysAccessListUseSpecificInterface = _AcSysAccessListUseSpecificInterface_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 7, 23, 1, 1, 16),
    _AcSysAccessListUseSpecificInterface_Type()
)
acSysAccessListUseSpecificInterface.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acSysAccessListUseSpecificInterface.setStatus("current")


class _AcSysAccessListSourcePort_Type(Unsigned32):
    """Custom type acSysAccessListSourcePort based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AcSysAccessListSourcePort_Type.__name__ = "Unsigned32"
_AcSysAccessListSourcePort_Object = MibTableColumn
acSysAccessListSourcePort = _AcSysAccessListSourcePort_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 7, 23, 1, 1, 17),
    _AcSysAccessListSourcePort_Type()
)
acSysAccessListSourcePort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acSysAccessListSourcePort.setStatus("current")


class _AcSysAccessListPrefixLength_Type(Unsigned32):
    """Custom type acSysAccessListPrefixLength based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_AcSysAccessListPrefixLength_Type.__name__ = "Unsigned32"
_AcSysAccessListPrefixLength_Object = MibTableColumn
acSysAccessListPrefixLength = _AcSysAccessListPrefixLength_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 7, 23, 1, 1, 18),
    _AcSysAccessListPrefixLength_Type()
)
acSysAccessListPrefixLength.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acSysAccessListPrefixLength.setStatus("current")
_AcSysMediaEncription_ObjectIdentity = ObjectIdentity
acSysMediaEncription = _AcSysMediaEncription_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 7, 24)
)


class _AcSysMediaEncriptionRTPAuthenticationDisableTx_Type(Integer32):
    """Custom type acSysMediaEncriptionRTPAuthenticationDisableTx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("inactive", 0),
          ("active", 1))
    )


_AcSysMediaEncriptionRTPAuthenticationDisableTx_Type.__name__ = "Integer32"
_AcSysMediaEncriptionRTPAuthenticationDisableTx_Object = MibScalar
acSysMediaEncriptionRTPAuthenticationDisableTx = _AcSysMediaEncriptionRTPAuthenticationDisableTx_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 7, 24, 1),
    _AcSysMediaEncriptionRTPAuthenticationDisableTx_Type()
)
acSysMediaEncriptionRTPAuthenticationDisableTx.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acSysMediaEncriptionRTPAuthenticationDisableTx.setStatus("current")


class _AcSysMediaEncriptionRTPAuthenticationDisableRx_Type(Integer32):
    """Custom type acSysMediaEncriptionRTPAuthenticationDisableRx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("inactive", 0),
          ("active", 1))
    )


_AcSysMediaEncriptionRTPAuthenticationDisableRx_Type.__name__ = "Integer32"
_AcSysMediaEncriptionRTPAuthenticationDisableRx_Object = MibScalar
acSysMediaEncriptionRTPAuthenticationDisableRx = _AcSysMediaEncriptionRTPAuthenticationDisableRx_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 7, 24, 2),
    _AcSysMediaEncriptionRTPAuthenticationDisableRx_Type()
)
acSysMediaEncriptionRTPAuthenticationDisableRx.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acSysMediaEncriptionRTPAuthenticationDisableRx.setStatus("current")


class _AcSysMediaEncriptionRTPEncryptionDisableTx_Type(Integer32):
    """Custom type acSysMediaEncriptionRTPEncryptionDisableTx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("inactive", 0),
          ("active", 1))
    )


_AcSysMediaEncriptionRTPEncryptionDisableTx_Type.__name__ = "Integer32"
_AcSysMediaEncriptionRTPEncryptionDisableTx_Object = MibScalar
acSysMediaEncriptionRTPEncryptionDisableTx = _AcSysMediaEncriptionRTPEncryptionDisableTx_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 7, 24, 3),
    _AcSysMediaEncriptionRTPEncryptionDisableTx_Type()
)
acSysMediaEncriptionRTPEncryptionDisableTx.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acSysMediaEncriptionRTPEncryptionDisableTx.setStatus("current")


class _AcSysMediaEncriptionRTPEncryptionDisableRx_Type(Integer32):
    """Custom type acSysMediaEncriptionRTPEncryptionDisableRx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("inactive", 0),
          ("active", 1))
    )


_AcSysMediaEncriptionRTPEncryptionDisableRx_Type.__name__ = "Integer32"
_AcSysMediaEncriptionRTPEncryptionDisableRx_Object = MibScalar
acSysMediaEncriptionRTPEncryptionDisableRx = _AcSysMediaEncriptionRTPEncryptionDisableRx_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 7, 24, 4),
    _AcSysMediaEncriptionRTPEncryptionDisableRx_Type()
)
acSysMediaEncriptionRTPEncryptionDisableRx.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acSysMediaEncriptionRTPEncryptionDisableRx.setStatus("current")


class _AcSysMediaEncriptionRTCPEncryptionDisableTx_Type(Integer32):
    """Custom type acSysMediaEncriptionRTCPEncryptionDisableTx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("inactive", 0),
          ("active", 1))
    )


_AcSysMediaEncriptionRTCPEncryptionDisableTx_Type.__name__ = "Integer32"
_AcSysMediaEncriptionRTCPEncryptionDisableTx_Object = MibScalar
acSysMediaEncriptionRTCPEncryptionDisableTx = _AcSysMediaEncriptionRTCPEncryptionDisableTx_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 7, 24, 5),
    _AcSysMediaEncriptionRTCPEncryptionDisableTx_Type()
)
acSysMediaEncriptionRTCPEncryptionDisableTx.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acSysMediaEncriptionRTCPEncryptionDisableTx.setStatus("current")


class _AcSysMediaEncriptionRTCPEncryptionDisableRx_Type(Integer32):
    """Custom type acSysMediaEncriptionRTCPEncryptionDisableRx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("inactive", 0),
          ("active", 1))
    )


_AcSysMediaEncriptionRTCPEncryptionDisableRx_Type.__name__ = "Integer32"
_AcSysMediaEncriptionRTCPEncryptionDisableRx_Object = MibScalar
acSysMediaEncriptionRTCPEncryptionDisableRx = _AcSysMediaEncriptionRTCPEncryptionDisableRx_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 7, 24, 6),
    _AcSysMediaEncriptionRTCPEncryptionDisableRx_Type()
)
acSysMediaEncriptionRTCPEncryptionDisableRx.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acSysMediaEncriptionRTCPEncryptionDisableRx.setStatus("current")
_AcSysSRTP_ObjectIdentity = ObjectIdentity
acSysSRTP = _AcSysSRTP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 7, 24, 21)
)


class _AcSysSRTPPacketMKISize_Type(Unsigned32):
    """Custom type acSysSRTPPacketMKISize based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4),
    )


_AcSysSRTPPacketMKISize_Type.__name__ = "Unsigned32"
_AcSysSRTPPacketMKISize_Object = MibScalar
acSysSRTPPacketMKISize = _AcSysSRTPPacketMKISize_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 7, 24, 21, 1),
    _AcSysSRTPPacketMKISize_Type()
)
acSysSRTPPacketMKISize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acSysSRTPPacketMKISize.setStatus("current")
_AcSys802dot1x_ObjectIdentity = ObjectIdentity
acSys802dot1x = _AcSys802dot1x_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 7, 25)
)


class _AcSys802dot1xMode_Type(Integer32):
    """Custom type acSys802dot1xMode based on Integer32"""
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
        *(("disabled", 0),
          ("eapMd5", 1),
          ("protectedEap", 2),
          ("eapTls", 3))
    )


_AcSys802dot1xMode_Type.__name__ = "Integer32"
_AcSys802dot1xMode_Object = MibScalar
acSys802dot1xMode = _AcSys802dot1xMode_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 7, 25, 1),
    _AcSys802dot1xMode_Type()
)
acSys802dot1xMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acSys802dot1xMode.setStatus("obsolete")


class _AcSys802dot1xUsername_Type(SnmpAdminString):
    """Custom type acSys802dot1xUsername based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_AcSys802dot1xUsername_Type.__name__ = "SnmpAdminString"
_AcSys802dot1xUsername_Object = MibScalar
acSys802dot1xUsername = _AcSys802dot1xUsername_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 7, 25, 2),
    _AcSys802dot1xUsername_Type()
)
acSys802dot1xUsername.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acSys802dot1xUsername.setStatus("obsolete")


class _AcSys802dot1xPassword_Type(SnmpAdminString):
    """Custom type acSys802dot1xPassword based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_AcSys802dot1xPassword_Type.__name__ = "SnmpAdminString"
_AcSys802dot1xPassword_Object = MibScalar
acSys802dot1xPassword = _AcSys802dot1xPassword_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 7, 25, 3),
    _AcSys802dot1xPassword_Type()
)
acSys802dot1xPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acSys802dot1xPassword.setStatus("obsolete")


class _AcSys802dot1xVerifyPeerCertificate_Type(Integer32):
    """Custom type acSys802dot1xVerifyPeerCertificate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_AcSys802dot1xVerifyPeerCertificate_Type.__name__ = "Integer32"
_AcSys802dot1xVerifyPeerCertificate_Object = MibScalar
acSys802dot1xVerifyPeerCertificate = _AcSys802dot1xVerifyPeerCertificate_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 7, 25, 4),
    _AcSys802dot1xVerifyPeerCertificate_Type()
)
acSys802dot1xVerifyPeerCertificate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acSys802dot1xVerifyPeerCertificate.setStatus("obsolete")
_AcSysTLSContexts_ObjectIdentity = ObjectIdentity
acSysTLSContexts = _AcSysTLSContexts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 7, 26)
)
_AcSysTLSContextsTable_Object = MibTable
acSysTLSContextsTable = _AcSysTLSContextsTable_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 7, 26, 1)
)
if mibBuilder.loadTexts:
    acSysTLSContextsTable.setStatus("current")
_AcSysTLSContextsEntry_Object = MibTableRow
acSysTLSContextsEntry = _AcSysTLSContextsEntry_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 7, 26, 1, 1)
)
acSysTLSContextsEntry.setIndexNames(
    (0, "AC-SYSTEM-MIB", "acSysTLSContextsIndex"),
)
if mibBuilder.loadTexts:
    acSysTLSContextsEntry.setStatus("current")


class _AcSysTLSContextsIndex_Type(Unsigned32):
    """Custom type acSysTLSContextsIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_AcSysTLSContextsIndex_Type.__name__ = "Unsigned32"
_AcSysTLSContextsIndex_Object = MibTableColumn
acSysTLSContextsIndex = _AcSysTLSContextsIndex_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 7, 26, 1, 1, 1),
    _AcSysTLSContextsIndex_Type()
)
acSysTLSContextsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    acSysTLSContextsIndex.setStatus("current")
_AcSysTLSContextsRowStatus_Type = RowStatus
_AcSysTLSContextsRowStatus_Object = MibTableColumn
acSysTLSContextsRowStatus = _AcSysTLSContextsRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 7, 26, 1, 1, 2),
    _AcSysTLSContextsRowStatus_Type()
)
acSysTLSContextsRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSysTLSContextsRowStatus.setStatus("current")


class _AcSysTLSContextsAction_Type(Unsigned32):
    """Custom type acSysTLSContextsAction based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
    )


_AcSysTLSContextsAction_Type.__name__ = "Unsigned32"
_AcSysTLSContextsAction_Object = MibTableColumn
acSysTLSContextsAction = _AcSysTLSContextsAction_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 7, 26, 1, 1, 3),
    _AcSysTLSContextsAction_Type()
)
acSysTLSContextsAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSysTLSContextsAction.setStatus("current")


class _AcSysTLSContextsActionResult_Type(Unsigned32):
    """Custom type acSysTLSContextsActionResult based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
    )


_AcSysTLSContextsActionResult_Type.__name__ = "Unsigned32"
_AcSysTLSContextsActionResult_Object = MibTableColumn
acSysTLSContextsActionResult = _AcSysTLSContextsActionResult_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 7, 26, 1, 1, 4),
    _AcSysTLSContextsActionResult_Type()
)
acSysTLSContextsActionResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSysTLSContextsActionResult.setStatus("current")


class _AcSysTLSContextsName_Type(SnmpAdminString):
    """Custom type acSysTLSContextsName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AcSysTLSContextsName_Type.__name__ = "SnmpAdminString"
_AcSysTLSContextsName_Object = MibTableColumn
acSysTLSContextsName = _AcSysTLSContextsName_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 7, 26, 1, 1, 5),
    _AcSysTLSContextsName_Type()
)
acSysTLSContextsName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSysTLSContextsName.setStatus("current")


class _AcSysTLSContextsTlsVersion_Type(Integer32):
    """Custom type acSysTLSContextsTlsVersion based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              6,
              7,
              8,
              12,
              14,
              15)
        )
    )
    namedValues = NamedValues(
        *(("anyTLS1dotx", 0),
          ("tLSv1dot0", 1),
          ("tLSv1dot1", 2),
          ("tLSv1dot0AndTLSv1dot1", 3),
          ("tLSv1dot2", 4),
          ("tLSv1dot1AndTLSv1dot2", 6),
          ("tLSv1dot0TLSv1dot1AndTLSv1dot2", 7),
          ("tLSv1dot3", 8),
          ("tLSv1dot2AndTLSv1dot3", 12),
          ("tLSv1dot1TLSv1dot2AndTLSv1dot3", 14),
          ("tLSv1dot0TLSv1dot1TLSv1dot2AndTLSv1dot3", 15))
    )


_AcSysTLSContextsTlsVersion_Type.__name__ = "Integer32"
_AcSysTLSContextsTlsVersion_Object = MibTableColumn
acSysTLSContextsTlsVersion = _AcSysTLSContextsTlsVersion_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 7, 26, 1, 1, 6),
    _AcSysTLSContextsTlsVersion_Type()
)
acSysTLSContextsTlsVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSysTLSContextsTlsVersion.setStatus("current")


class _AcSysTLSContextsDTLSVersion_Type(Integer32):
    """Custom type acSysTLSContextsDTLSVersion based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dTLSv1dot0AndDTLSv1dot2", 0),
          ("dTLSv1dot0", 1),
          ("dTLSv1dot2", 2))
    )


_AcSysTLSContextsDTLSVersion_Type.__name__ = "Integer32"
_AcSysTLSContextsDTLSVersion_Object = MibTableColumn
acSysTLSContextsDTLSVersion = _AcSysTLSContextsDTLSVersion_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 7, 26, 1, 1, 7),
    _AcSysTLSContextsDTLSVersion_Type()
)
acSysTLSContextsDTLSVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSysTLSContextsDTLSVersion.setStatus("current")


class _AcSysTLSContextsCipherServer_Type(SnmpAdminString):
    """Custom type acSysTLSContextsCipherServer based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_AcSysTLSContextsCipherServer_Type.__name__ = "SnmpAdminString"
_AcSysTLSContextsCipherServer_Object = MibTableColumn
acSysTLSContextsCipherServer = _AcSysTLSContextsCipherServer_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 7, 26, 1, 1, 8),
    _AcSysTLSContextsCipherServer_Type()
)
acSysTLSContextsCipherServer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSysTLSContextsCipherServer.setStatus("current")


class _AcSysTLSContextsCipherClient_Type(SnmpAdminString):
    """Custom type acSysTLSContextsCipherClient based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_AcSysTLSContextsCipherClient_Type.__name__ = "SnmpAdminString"
_AcSysTLSContextsCipherClient_Object = MibTableColumn
acSysTLSContextsCipherClient = _AcSysTLSContextsCipherClient_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 7, 26, 1, 1, 9),
    _AcSysTLSContextsCipherClient_Type()
)
acSysTLSContextsCipherClient.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSysTLSContextsCipherClient.setStatus("current")


class _AcSysTLSContextsCipherServer13_Type(SnmpAdminString):
    """Custom type acSysTLSContextsCipherServer13 based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_AcSysTLSContextsCipherServer13_Type.__name__ = "SnmpAdminString"
_AcSysTLSContextsCipherServer13_Object = MibTableColumn
acSysTLSContextsCipherServer13 = _AcSysTLSContextsCipherServer13_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 7, 26, 1, 1, 10),
    _AcSysTLSContextsCipherServer13_Type()
)
acSysTLSContextsCipherServer13.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSysTLSContextsCipherServer13.setStatus("current")


class _AcSysTLSContextsCipherClient13_Type(SnmpAdminString):
    """Custom type acSysTLSContextsCipherClient13 based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_AcSysTLSContextsCipherClient13_Type.__name__ = "SnmpAdminString"
_AcSysTLSContextsCipherClient13_Object = MibTableColumn
acSysTLSContextsCipherClient13 = _AcSysTLSContextsCipherClient13_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 7, 26, 1, 1, 11),
    _AcSysTLSContextsCipherClient13_Type()
)
acSysTLSContextsCipherClient13.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSysTLSContextsCipherClient13.setStatus("current")


class _AcSysTLSContextsExchangeGroups_Type(SnmpAdminString):
    """Custom type acSysTLSContextsExchangeGroups based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_AcSysTLSContextsExchangeGroups_Type.__name__ = "SnmpAdminString"
_AcSysTLSContextsExchangeGroups_Object = MibTableColumn
acSysTLSContextsExchangeGroups = _AcSysTLSContextsExchangeGroups_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 7, 26, 1, 1, 12),
    _AcSysTLSContextsExchangeGroups_Type()
)
acSysTLSContextsExchangeGroups.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSysTLSContextsExchangeGroups.setStatus("current")


class _AcSysTLSContextsStrictValidation_Type(Integer32):
    """Custom type acSysTLSContextsStrictValidation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_AcSysTLSContextsStrictValidation_Type.__name__ = "Integer32"
_AcSysTLSContextsStrictValidation_Object = MibTableColumn
acSysTLSContextsStrictValidation = _AcSysTLSContextsStrictValidation_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 7, 26, 1, 1, 13),
    _AcSysTLSContextsStrictValidation_Type()
)
acSysTLSContextsStrictValidation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSysTLSContextsStrictValidation.setStatus("current")


class _AcSysTLSContextsDHKeySize_Type(Integer32):
    """Custom type acSysTLSContextsDHKeySize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1024,
              2048,
              3072)
        )
    )
    namedValues = NamedValues(
        *(("dHKeySize1024", 1024),
          ("dHKeySize2048", 2048),
          ("dHKeySize3072", 3072))
    )


_AcSysTLSContextsDHKeySize_Type.__name__ = "Integer32"
_AcSysTLSContextsDHKeySize_Object = MibTableColumn
acSysTLSContextsDHKeySize = _AcSysTLSContextsDHKeySize_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 7, 26, 1, 1, 14),
    _AcSysTLSContextsDHKeySize_Type()
)
acSysTLSContextsDHKeySize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSysTLSContextsDHKeySize.setStatus("current")


class _AcSysTLSContextsTlsRenegotiation_Type(Integer32):
    """Custom type acSysTLSContextsTlsRenegotiation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_AcSysTLSContextsTlsRenegotiation_Type.__name__ = "Integer32"
_AcSysTLSContextsTlsRenegotiation_Object = MibTableColumn
acSysTLSContextsTlsRenegotiation = _AcSysTLSContextsTlsRenegotiation_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 7, 26, 1, 1, 15),
    _AcSysTLSContextsTlsRenegotiation_Type()
)
acSysTLSContextsTlsRenegotiation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSysTLSContextsTlsRenegotiation.setStatus("current")
_AcSysSerialIF_ObjectIdentity = ObjectIdentity
acSysSerialIF = _AcSysSerialIF_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 8)
)


class _AcSysSerialIFBaudRate_Type(Integer32):
    """Custom type acSysSerialIFBaudRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1200,
              2400,
              4800,
              9600,
              14400,
              19200,
              38400,
              57600,
              115200)
        )
    )
    namedValues = NamedValues(
        *(("r1200", 1200),
          ("r2400", 2400),
          ("r4800", 4800),
          ("r9600", 9600),
          ("r14400", 14400),
          ("r19200", 19200),
          ("r38400", 38400),
          ("r57600", 57600),
          ("r115200", 115200))
    )


_AcSysSerialIFBaudRate_Type.__name__ = "Integer32"
_AcSysSerialIFBaudRate_Object = MibScalar
acSysSerialIFBaudRate = _AcSysSerialIFBaudRate_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 8, 1),
    _AcSysSerialIFBaudRate_Type()
)
acSysSerialIFBaudRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acSysSerialIFBaudRate.setStatus("current")


class _AcSysSerialIFData_Type(Unsigned32):
    """Custom type acSysSerialIFData based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(7, 8),
    )


_AcSysSerialIFData_Type.__name__ = "Unsigned32"
_AcSysSerialIFData_Object = MibScalar
acSysSerialIFData = _AcSysSerialIFData_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 8, 2),
    _AcSysSerialIFData_Type()
)
acSysSerialIFData.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acSysSerialIFData.setStatus("current")


class _AcSysSerialIFParity_Type(Integer32):
    """Custom type acSysSerialIFParity based on Integer32"""
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
          ("odd", 1),
          ("even", 2))
    )


_AcSysSerialIFParity_Type.__name__ = "Integer32"
_AcSysSerialIFParity_Object = MibScalar
acSysSerialIFParity = _AcSysSerialIFParity_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 8, 3),
    _AcSysSerialIFParity_Type()
)
acSysSerialIFParity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acSysSerialIFParity.setStatus("current")


class _AcSysSerialIFStop_Type(Unsigned32):
    """Custom type acSysSerialIFStop based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_AcSysSerialIFStop_Type.__name__ = "Unsigned32"
_AcSysSerialIFStop_Object = MibScalar
acSysSerialIFStop = _AcSysSerialIFStop_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 8, 4),
    _AcSysSerialIFStop_Type()
)
acSysSerialIFStop.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acSysSerialIFStop.setStatus("current")


class _AcSysSerialIFFlowControl_Type(Integer32):
    """Custom type acSysSerialIFFlowControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("hardware", 1))
    )


_AcSysSerialIFFlowControl_Type.__name__ = "Integer32"
_AcSysSerialIFFlowControl_Object = MibScalar
acSysSerialIFFlowControl = _AcSysSerialIFFlowControl_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 8, 5),
    _AcSysSerialIFFlowControl_Type()
)
acSysSerialIFFlowControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acSysSerialIFFlowControl.setStatus("current")
_AcVoiceStream_ObjectIdentity = ObjectIdentity
acVoiceStream = _AcVoiceStream_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 9)
)


class _AcVoiceStreamStatus_Type(Integer32):
    """Custom type acVoiceStreamStatus based on Integer32"""
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


_AcVoiceStreamStatus_Type.__name__ = "Integer32"
_AcVoiceStreamStatus_Object = MibScalar
acVoiceStreamStatus = _AcVoiceStreamStatus_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 9, 1),
    _AcVoiceStreamStatus_Type()
)
acVoiceStreamStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acVoiceStreamStatus.setStatus("current")


class _AcVoiceStreamUploadMethod_Type(Integer32):
    """Custom type acVoiceStreamUploadMethod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("httpPostMethod", 0),
          ("httpPutMethod", 1))
    )


_AcVoiceStreamUploadMethod_Type.__name__ = "Integer32"
_AcVoiceStreamUploadMethod_Object = MibScalar
acVoiceStreamUploadMethod = _AcVoiceStreamUploadMethod_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 9, 2),
    _AcVoiceStreamUploadMethod_Type()
)
acVoiceStreamUploadMethod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acVoiceStreamUploadMethod.setStatus("current")


class _AcVoiceStreamUploadPostUri_Type(SnmpAdminString):
    """Custom type acVoiceStreamUploadPostUri based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 59),
    )


_AcVoiceStreamUploadPostUri_Type.__name__ = "SnmpAdminString"
_AcVoiceStreamUploadPostUri_Object = MibScalar
acVoiceStreamUploadPostUri = _AcVoiceStreamUploadPostUri_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 9, 3),
    _AcVoiceStreamUploadPostUri_Type()
)
acVoiceStreamUploadPostUri.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acVoiceStreamUploadPostUri.setStatus("current")
_AcSysAMS_ObjectIdentity = ObjectIdentity
acSysAMS = _AcSysAMS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 10)
)


class _AcSysAMSProfile_Type(Unsigned32):
    """Custom type acSysAMSProfile based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_AcSysAMSProfile_Type.__name__ = "Unsigned32"
_AcSysAMSProfile_Object = MibScalar
acSysAMSProfile = _AcSysAMSProfile_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 10, 1),
    _AcSysAMSProfile_Type()
)
acSysAMSProfile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acSysAMSProfile.setStatus("obsolete")
_AcSysAMSApsIpAddress_Type = IpAddress
_AcSysAMSApsIpAddress_Object = MibScalar
acSysAMSApsIpAddress = _AcSysAMSApsIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 10, 2),
    _AcSysAMSApsIpAddress_Type()
)
acSysAMSApsIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acSysAMSApsIpAddress.setStatus("obsolete")


class _AcSysAMSApsPort_Type(Unsigned32):
    """Custom type acSysAMSApsPort based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 64000),
    )


_AcSysAMSApsPort_Type.__name__ = "Unsigned32"
_AcSysAMSApsPort_Object = MibScalar
acSysAMSApsPort = _AcSysAMSApsPort_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 10, 3),
    _AcSysAMSApsPort_Type()
)
acSysAMSApsPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acSysAMSApsPort.setStatus("obsolete")


class _AcSysAMSPrimaryLanguage_Type(SnmpAdminString):
    """Custom type acSysAMSPrimaryLanguage based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 3),
    )


_AcSysAMSPrimaryLanguage_Type.__name__ = "SnmpAdminString"
_AcSysAMSPrimaryLanguage_Object = MibScalar
acSysAMSPrimaryLanguage = _AcSysAMSPrimaryLanguage_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 10, 4),
    _AcSysAMSPrimaryLanguage_Type()
)
acSysAMSPrimaryLanguage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acSysAMSPrimaryLanguage.setStatus("obsolete")


class _AcSysAMSSecondaryLanguage_Type(SnmpAdminString):
    """Custom type acSysAMSSecondaryLanguage based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 3),
    )


_AcSysAMSSecondaryLanguage_Type.__name__ = "SnmpAdminString"
_AcSysAMSSecondaryLanguage_Object = MibScalar
acSysAMSSecondaryLanguage = _AcSysAMSSecondaryLanguage_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 10, 5),
    _AcSysAMSSecondaryLanguage_Type()
)
acSysAMSSecondaryLanguage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acSysAMSSecondaryLanguage.setStatus("obsolete")


class _AcSysAMSAPSProfile_Type(Integer32):
    """Custom type acSysAMSAPSProfile based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("vpDatProvidedAudio", 0),
          ("apsProvidedAudio", 1))
    )


_AcSysAMSAPSProfile_Type.__name__ = "Integer32"
_AcSysAMSAPSProfile_Object = MibScalar
acSysAMSAPSProfile = _AcSysAMSAPSProfile_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 10, 6),
    _AcSysAMSAPSProfile_Type()
)
acSysAMSAPSProfile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acSysAMSAPSProfile.setStatus("obsolete")


class _AcSysAMSForceRepositoryEnable_Type(Integer32):
    """Custom type acSysAMSForceRepositoryEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_AcSysAMSForceRepositoryEnable_Type.__name__ = "Integer32"
_AcSysAMSForceRepositoryEnable_Object = MibScalar
acSysAMSForceRepositoryEnable = _AcSysAMSForceRepositoryEnable_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 10, 7),
    _AcSysAMSForceRepositoryEnable_Type()
)
acSysAMSForceRepositoryEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acSysAMSForceRepositoryEnable.setStatus("obsolete")
_AcSysNetworkFileSystem_ObjectIdentity = ObjectIdentity
acSysNetworkFileSystem = _AcSysNetworkFileSystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 11)
)
_AcSysNFSTable_Object = MibTable
acSysNFSTable = _AcSysNFSTable_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 11, 21)
)
if mibBuilder.loadTexts:
    acSysNFSTable.setStatus("current")
_AcSysNFSEntry_Object = MibTableRow
acSysNFSEntry = _AcSysNFSEntry_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 11, 21, 1)
)
acSysNFSEntry.setIndexNames(
    (0, "AC-SYSTEM-MIB", "acSysNFSIndex"),
)
if mibBuilder.loadTexts:
    acSysNFSEntry.setStatus("current")


class _AcSysNFSIndex_Type(Unsigned32):
    """Custom type acSysNFSIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_AcSysNFSIndex_Type.__name__ = "Unsigned32"
_AcSysNFSIndex_Object = MibTableColumn
acSysNFSIndex = _AcSysNFSIndex_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 11, 21, 1, 1),
    _AcSysNFSIndex_Type()
)
acSysNFSIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    acSysNFSIndex.setStatus("current")
_AcSysNFSRowStatus_Type = RowStatus
_AcSysNFSRowStatus_Object = MibTableColumn
acSysNFSRowStatus = _AcSysNFSRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 11, 21, 1, 2),
    _AcSysNFSRowStatus_Type()
)
acSysNFSRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acSysNFSRowStatus.setStatus("current")


class _AcSysNFSAction_Type(Integer32):
    """Custom type acSysNFSAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            0
        )
    )
    namedValues = NamedValues(
        ("none", 0)
    )


_AcSysNFSAction_Type.__name__ = "Integer32"
_AcSysNFSAction_Object = MibTableColumn
acSysNFSAction = _AcSysNFSAction_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 11, 21, 1, 3),
    _AcSysNFSAction_Type()
)
acSysNFSAction.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acSysNFSAction.setStatus("current")


class _AcSysNFSActionRes_Type(Integer32):
    """Custom type acSysNFSActionRes based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            0
        )
    )
    namedValues = NamedValues(
        ("succeeded", 0)
    )


_AcSysNFSActionRes_Type.__name__ = "Integer32"
_AcSysNFSActionRes_Object = MibTableColumn
acSysNFSActionRes = _AcSysNFSActionRes_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 11, 21, 1, 4),
    _AcSysNFSActionRes_Type()
)
acSysNFSActionRes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSysNFSActionRes.setStatus("current")


class _AcSysNFSHostOrIP_Type(SnmpAdminString):
    """Custom type acSysNFSHostOrIP based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 39),
    )


_AcSysNFSHostOrIP_Type.__name__ = "SnmpAdminString"
_AcSysNFSHostOrIP_Object = MibTableColumn
acSysNFSHostOrIP = _AcSysNFSHostOrIP_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 11, 21, 1, 5),
    _AcSysNFSHostOrIP_Type()
)
acSysNFSHostOrIP.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acSysNFSHostOrIP.setStatus("current")


class _AcSysNFSRootPath_Type(SnmpAdminString):
    """Custom type acSysNFSRootPath based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 99),
    )


_AcSysNFSRootPath_Type.__name__ = "SnmpAdminString"
_AcSysNFSRootPath_Object = MibTableColumn
acSysNFSRootPath = _AcSysNFSRootPath_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 11, 21, 1, 6),
    _AcSysNFSRootPath_Type()
)
acSysNFSRootPath.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acSysNFSRootPath.setStatus("current")


class _AcSysNFSNfsVersion_Type(Integer32):
    """Custom type acSysNFSNfsVersion based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("v2", 2),
          ("v3", 3))
    )


_AcSysNFSNfsVersion_Type.__name__ = "Integer32"
_AcSysNFSNfsVersion_Object = MibTableColumn
acSysNFSNfsVersion = _AcSysNFSNfsVersion_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 11, 21, 1, 7),
    _AcSysNFSNfsVersion_Type()
)
acSysNFSNfsVersion.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acSysNFSNfsVersion.setStatus("current")


class _AcSysNFSAuthType_Type(Integer32):
    """Custom type acSysNFSAuthType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("null", 0),
          ("unix", 1))
    )


_AcSysNFSAuthType_Type.__name__ = "Integer32"
_AcSysNFSAuthType_Object = MibTableColumn
acSysNFSAuthType = _AcSysNFSAuthType_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 11, 21, 1, 8),
    _AcSysNFSAuthType_Type()
)
acSysNFSAuthType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acSysNFSAuthType.setStatus("current")


class _AcSysNFSUID_Type(Unsigned32):
    """Custom type acSysNFSUID based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AcSysNFSUID_Type.__name__ = "Unsigned32"
_AcSysNFSUID_Object = MibTableColumn
acSysNFSUID = _AcSysNFSUID_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 11, 21, 1, 9),
    _AcSysNFSUID_Type()
)
acSysNFSUID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acSysNFSUID.setStatus("current")


class _AcSysNFSGID_Type(Unsigned32):
    """Custom type acSysNFSGID based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AcSysNFSGID_Type.__name__ = "Unsigned32"
_AcSysNFSGID_Object = MibTableColumn
acSysNFSGID = _AcSysNFSGID_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 11, 21, 1, 10),
    _AcSysNFSGID_Type()
)
acSysNFSGID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acSysNFSGID.setStatus("current")


class _AcSysNFSVlanType_Type(Integer32):
    """Custom type acSysNFSVlanType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("oam", 0),
          ("media", 1))
    )


_AcSysNFSVlanType_Type.__name__ = "Integer32"
_AcSysNFSVlanType_Object = MibTableColumn
acSysNFSVlanType = _AcSysNFSVlanType_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 11, 21, 1, 11),
    _AcSysNFSVlanType_Type()
)
acSysNFSVlanType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acSysNFSVlanType.setStatus("current")
_AcSysHA_ObjectIdentity = ObjectIdentity
acSysHA = _AcSysHA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 12)
)
_AcSysHAGlobalIPAddress_Type = IpAddress
_AcSysHAGlobalIPAddress_Object = MibScalar
acSysHAGlobalIPAddress = _AcSysHAGlobalIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 12, 1),
    _AcSysHAGlobalIPAddress_Type()
)
acSysHAGlobalIPAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acSysHAGlobalIPAddress.setStatus("obsolete")
_AcSysHARemoteAddress_Type = IpAddress
_AcSysHARemoteAddress_Object = MibScalar
acSysHARemoteAddress = _AcSysHARemoteAddress_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 12, 2),
    _AcSysHARemoteAddress_Type()
)
acSysHARemoteAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acSysHARemoteAddress.setStatus("deprecated")


class _AcSysHARevertive_Type(Integer32):
    """Custom type acSysHARevertive based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_AcSysHARevertive_Type.__name__ = "Integer32"
_AcSysHARevertive_Object = MibScalar
acSysHARevertive = _AcSysHARevertive_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 12, 3),
    _AcSysHARevertive_Type()
)
acSysHARevertive.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acSysHARevertive.setStatus("current")


class _AcSysHAPriority_Type(Unsigned32):
    """Custom type acSysHAPriority based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_AcSysHAPriority_Type.__name__ = "Unsigned32"
_AcSysHAPriority_Object = MibScalar
acSysHAPriority = _AcSysHAPriority_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 12, 4),
    _AcSysHAPriority_Type()
)
acSysHAPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acSysHAPriority.setStatus("current")


class _AcSysHARedundantPriority_Type(Unsigned32):
    """Custom type acSysHARedundantPriority based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10),
    )


_AcSysHARedundantPriority_Type.__name__ = "Unsigned32"
_AcSysHARedundantPriority_Object = MibScalar
acSysHARedundantPriority = _AcSysHARedundantPriority_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 12, 5),
    _AcSysHARedundantPriority_Type()
)
acSysHARedundantPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acSysHARedundantPriority.setStatus("current")


class _AcSysHAPingEnabled_Type(Integer32):
    """Custom type acSysHAPingEnabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_AcSysHAPingEnabled_Type.__name__ = "Integer32"
_AcSysHAPingEnabled_Object = MibScalar
acSysHAPingEnabled = _AcSysHAPingEnabled_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 12, 6),
    _AcSysHAPingEnabled_Type()
)
acSysHAPingEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acSysHAPingEnabled.setStatus("current")
_AcSysHAPingDestination_Type = IpAddress
_AcSysHAPingDestination_Object = MibScalar
acSysHAPingDestination = _AcSysHAPingDestination_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 12, 7),
    _AcSysHAPingDestination_Type()
)
acSysHAPingDestination.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acSysHAPingDestination.setStatus("deprecated")


class _AcSysHAPingSourceIfName_Type(SnmpAdminString):
    """Custom type acSysHAPingSourceIfName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_AcSysHAPingSourceIfName_Type.__name__ = "SnmpAdminString"
_AcSysHAPingSourceIfName_Object = MibScalar
acSysHAPingSourceIfName = _AcSysHAPingSourceIfName_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 12, 8),
    _AcSysHAPingSourceIfName_Type()
)
acSysHAPingSourceIfName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acSysHAPingSourceIfName.setStatus("current")


class _AcSysHAPingTimeout_Type(Unsigned32):
    """Custom type acSysHAPingTimeout based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 60),
    )


_AcSysHAPingTimeout_Type.__name__ = "Unsigned32"
_AcSysHAPingTimeout_Object = MibScalar
acSysHAPingTimeout = _AcSysHAPingTimeout_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 12, 9),
    _AcSysHAPingTimeout_Type()
)
acSysHAPingTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acSysHAPingTimeout.setStatus("current")


class _AcSysHAPingRetries_Type(Unsigned32):
    """Custom type acSysHAPingRetries based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_AcSysHAPingRetries_Type.__name__ = "Unsigned32"
_AcSysHAPingRetries_Object = MibScalar
acSysHAPingRetries = _AcSysHAPingRetries_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 12, 10),
    _AcSysHAPingRetries_Type()
)
acSysHAPingRetries.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acSysHAPingRetries.setStatus("current")
_AcSysTransmission_ObjectIdentity = ObjectIdentity
acSysTransmission = _AcSysTransmission_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 13)
)


class _AcSysTransmissionType_Type(Integer32):
    """Custom type acSysTransmissionType based on Integer32"""
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
          ("opticalSonetSdh", 1),
          ("copperDs3", 2),
          ("copperE1Ds1", 3))
    )


_AcSysTransmissionType_Type.__name__ = "Integer32"
_AcSysTransmissionType_Object = MibScalar
acSysTransmissionType = _AcSysTransmissionType_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 13, 1),
    _AcSysTransmissionType_Type()
)
acSysTransmissionType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acSysTransmissionType.setStatus("current")
_AcSysTiming_ObjectIdentity = ObjectIdentity
acSysTiming = _AcSysTiming_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 14)
)


class _AcSysTimingMode_Type(Integer32):
    """Custom type acSysTimingMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("standAlone", 0),
          ("external", 1),
          ("lineSync", 2))
    )


_AcSysTimingMode_Type.__name__ = "Integer32"
_AcSysTimingMode_Object = MibScalar
acSysTimingMode = _AcSysTimingMode_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 14, 1),
    _AcSysTimingMode_Type()
)
acSysTimingMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acSysTimingMode.setStatus("current")


class _AcSysTimingValidationTime_Type(Unsigned32):
    """Custom type acSysTimingValidationTime based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_AcSysTimingValidationTime_Type.__name__ = "Unsigned32"
_AcSysTimingValidationTime_Object = MibScalar
acSysTimingValidationTime = _AcSysTimingValidationTime_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 14, 2),
    _AcSysTimingValidationTime_Type()
)
acSysTimingValidationTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acSysTimingValidationTime.setStatus("current")


class _AcSysTimingClockToDeriveA_Type(Integer32):
    """Custom type acSysTimingClockToDeriveA based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              4,
              7)
        )
    )
    namedValues = NamedValues(
        *(("deriveREFFromLineClock1", 0),
          ("deriveInternalClock", 4),
          ("clockFromReceiveSide", 7))
    )


_AcSysTimingClockToDeriveA_Type.__name__ = "Integer32"
_AcSysTimingClockToDeriveA_Object = MibScalar
acSysTimingClockToDeriveA = _AcSysTimingClockToDeriveA_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 14, 3),
    _AcSysTimingClockToDeriveA_Type()
)
acSysTimingClockToDeriveA.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acSysTimingClockToDeriveA.setStatus("obsolete")


class _AcSysTimingClockToDeriveB_Type(Integer32):
    """Custom type acSysTimingClockToDeriveB based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              4,
              7)
        )
    )
    namedValues = NamedValues(
        *(("deriveREFFromLineClock1", 0),
          ("deriveInternalClock", 4),
          ("clockFromReceiveSide", 7))
    )


_AcSysTimingClockToDeriveB_Type.__name__ = "Integer32"
_AcSysTimingClockToDeriveB_Object = MibScalar
acSysTimingClockToDeriveB = _AcSysTimingClockToDeriveB_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 14, 4),
    _AcSysTimingClockToDeriveB_Type()
)
acSysTimingClockToDeriveB.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acSysTimingClockToDeriveB.setStatus("obsolete")


class _AcSysTimingExternalIFType_Type(Integer32):
    """Custom type acSysTimingExternalIFType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("e1CRC4", 0),
          ("e1CAS", 1),
          ("e1FAS", 2),
          ("t1D4", 3),
          ("t1ESF", 4),
          ("t12", 5))
    )


_AcSysTimingExternalIFType_Type.__name__ = "Integer32"
_AcSysTimingExternalIFType_Object = MibScalar
acSysTimingExternalIFType = _AcSysTimingExternalIFType_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 14, 5),
    _AcSysTimingExternalIFType_Type()
)
acSysTimingExternalIFType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acSysTimingExternalIFType.setStatus("current")


class _AcSysTimingLoopBackRef1_Type(Integer32):
    """Custom type acSysTimingLoopBackRef1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("loopDisable", 0),
          ("loopEnable", 1))
    )


_AcSysTimingLoopBackRef1_Type.__name__ = "Integer32"
_AcSysTimingLoopBackRef1_Object = MibScalar
acSysTimingLoopBackRef1 = _AcSysTimingLoopBackRef1_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 14, 6),
    _AcSysTimingLoopBackRef1_Type()
)
acSysTimingLoopBackRef1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acSysTimingLoopBackRef1.setStatus("current")


class _AcSysTimingLoopBackRef2_Type(Integer32):
    """Custom type acSysTimingLoopBackRef2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("loopDisable", 0),
          ("loopEnable", 1))
    )


_AcSysTimingLoopBackRef2_Type.__name__ = "Integer32"
_AcSysTimingLoopBackRef2_Object = MibScalar
acSysTimingLoopBackRef2 = _AcSysTimingLoopBackRef2_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 14, 7),
    _AcSysTimingLoopBackRef2_Type()
)
acSysTimingLoopBackRef2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acSysTimingLoopBackRef2.setStatus("current")


class _AcSysTimingTransmitControl_Type(Integer32):
    """Custom type acSysTimingTransmitControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("systemClock", 0),
          ("aIS", 1),
          ("disableTransmit", 2))
    )


_AcSysTimingTransmitControl_Type.__name__ = "Integer32"
_AcSysTimingTransmitControl_Object = MibScalar
acSysTimingTransmitControl = _AcSysTimingTransmitControl_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 14, 8),
    _AcSysTimingTransmitControl_Type()
)
acSysTimingTransmitControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acSysTimingTransmitControl.setStatus("obsolete")


class _AcSysTimingE1LineBuildOut_Type(Integer32):
    """Custom type acSysTimingE1LineBuildOut based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("tm75OhmNormal", 0),
          ("tm120OhmNormal", 1),
          ("tm75OhmHighReturnLoss", 4),
          ("tm120OhmHighReturnLoss", 5),
          ("tm75OhmNormalGappedClock", 6),
          ("tm120OhmNormalGappedClock", 7))
    )


_AcSysTimingE1LineBuildOut_Type.__name__ = "Integer32"
_AcSysTimingE1LineBuildOut_Object = MibScalar
acSysTimingE1LineBuildOut = _AcSysTimingE1LineBuildOut_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 14, 9),
    _AcSysTimingE1LineBuildOut_Type()
)
acSysTimingE1LineBuildOut.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acSysTimingE1LineBuildOut.setStatus("obsolete")


class _AcSysTimingT1LineBuildOut_Type(Integer32):
    """Custom type acSysTimingT1LineBuildOut based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              7)
        )
    )
    namedValues = NamedValues(
        *(("dSX10to133feet0dBCSU", 0),
          ("dSX1133to266feet", 1),
          ("dSX1266to399feet", 2),
          ("dSX1399to533feet", 3),
          ("dSX1533to655feet", 4),
          ("dSX10to133ft0dBgappedclock", 7))
    )


_AcSysTimingT1LineBuildOut_Type.__name__ = "Integer32"
_AcSysTimingT1LineBuildOut_Object = MibScalar
acSysTimingT1LineBuildOut = _AcSysTimingT1LineBuildOut_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 14, 10),
    _AcSysTimingT1LineBuildOut_Type()
)
acSysTimingT1LineBuildOut.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acSysTimingT1LineBuildOut.setStatus("obsolete")
_AcSysLDAP_ObjectIdentity = ObjectIdentity
acSysLDAP = _AcSysLDAP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 15)
)
_AcSysLDAPServerIp_Type = IpAddress
_AcSysLDAPServerIp_Object = MibScalar
acSysLDAPServerIp = _AcSysLDAPServerIp_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 15, 1),
    _AcSysLDAPServerIp_Type()
)
acSysLDAPServerIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acSysLDAPServerIp.setStatus("obsolete")


class _AcSysLDAPServerPort_Type(Unsigned32):
    """Custom type acSysLDAPServerPort based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AcSysLDAPServerPort_Type.__name__ = "Unsigned32"
_AcSysLDAPServerPort_Object = MibScalar
acSysLDAPServerPort = _AcSysLDAPServerPort_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 15, 2),
    _AcSysLDAPServerPort_Type()
)
acSysLDAPServerPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acSysLDAPServerPort.setStatus("obsolete")


class _AcSysLDAPServerMaxRespondTime_Type(Unsigned32):
    """Custom type acSysLDAPServerMaxRespondTime based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 86400),
    )


_AcSysLDAPServerMaxRespondTime_Type.__name__ = "Unsigned32"
_AcSysLDAPServerMaxRespondTime_Object = MibScalar
acSysLDAPServerMaxRespondTime = _AcSysLDAPServerMaxRespondTime_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 15, 3),
    _AcSysLDAPServerMaxRespondTime_Type()
)
acSysLDAPServerMaxRespondTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acSysLDAPServerMaxRespondTime.setStatus("obsolete")


class _AcSysLDAPServerDomainName_Type(SnmpAdminString):
    """Custom type acSysLDAPServerDomainName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_AcSysLDAPServerDomainName_Type.__name__ = "SnmpAdminString"
_AcSysLDAPServerDomainName_Object = MibScalar
acSysLDAPServerDomainName = _AcSysLDAPServerDomainName_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 15, 4),
    _AcSysLDAPServerDomainName_Type()
)
acSysLDAPServerDomainName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acSysLDAPServerDomainName.setStatus("obsolete")


class _AcSysLDAPSearchDN_Type(SnmpAdminString):
    """Custom type acSysLDAPSearchDN based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_AcSysLDAPSearchDN_Type.__name__ = "SnmpAdminString"
_AcSysLDAPSearchDN_Object = MibScalar
acSysLDAPSearchDN = _AcSysLDAPSearchDN_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 15, 5),
    _AcSysLDAPSearchDN_Type()
)
acSysLDAPSearchDN.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acSysLDAPSearchDN.setStatus("obsolete")


class _AcSysLDAPPassword_Type(SnmpAdminString):
    """Custom type acSysLDAPPassword based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_AcSysLDAPPassword_Type.__name__ = "SnmpAdminString"
_AcSysLDAPPassword_Object = MibScalar
acSysLDAPPassword = _AcSysLDAPPassword_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 15, 6),
    _AcSysLDAPPassword_Type()
)
acSysLDAPPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acSysLDAPPassword.setStatus("obsolete")


class _AcSysLDAPBindDN_Type(SnmpAdminString):
    """Custom type acSysLDAPBindDN based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_AcSysLDAPBindDN_Type.__name__ = "SnmpAdminString"
_AcSysLDAPBindDN_Object = MibScalar
acSysLDAPBindDN = _AcSysLDAPBindDN_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 15, 7),
    _AcSysLDAPBindDN_Type()
)
acSysLDAPBindDN.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acSysLDAPBindDN.setStatus("obsolete")


class _AcSysLDAPServiceEnable_Type(Integer32):
    """Custom type acSysLDAPServiceEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_AcSysLDAPServiceEnable_Type.__name__ = "Integer32"
_AcSysLDAPServiceEnable_Object = MibScalar
acSysLDAPServiceEnable = _AcSysLDAPServiceEnable_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 15, 8),
    _AcSysLDAPServiceEnable_Type()
)
acSysLDAPServiceEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acSysLDAPServiceEnable.setStatus("current")


class _AcSysLDAPCacheEnable_Type(Integer32):
    """Custom type acSysLDAPCacheEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_AcSysLDAPCacheEnable_Type.__name__ = "Integer32"
_AcSysLDAPCacheEnable_Object = MibScalar
acSysLDAPCacheEnable = _AcSysLDAPCacheEnable_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 15, 9),
    _AcSysLDAPCacheEnable_Type()
)
acSysLDAPCacheEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acSysLDAPCacheEnable.setStatus("current")


class _AcSysLDAPCacheEntryTimeout_Type(Unsigned32):
    """Custom type acSysLDAPCacheEntryTimeout based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AcSysLDAPCacheEntryTimeout_Type.__name__ = "Unsigned32"
_AcSysLDAPCacheEntryTimeout_Object = MibScalar
acSysLDAPCacheEntryTimeout = _AcSysLDAPCacheEntryTimeout_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 15, 10),
    _AcSysLDAPCacheEntryTimeout_Type()
)
acSysLDAPCacheEntryTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acSysLDAPCacheEntryTimeout.setStatus("current")


class _AcSysLDAPCacheEntryRemovalTimeout_Type(Unsigned32):
    """Custom type acSysLDAPCacheEntryRemovalTimeout based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AcSysLDAPCacheEntryRemovalTimeout_Type.__name__ = "Unsigned32"
_AcSysLDAPCacheEntryRemovalTimeout_Object = MibScalar
acSysLDAPCacheEntryRemovalTimeout = _AcSysLDAPCacheEntryRemovalTimeout_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 15, 11),
    _AcSysLDAPCacheEntryRemovalTimeout_Type()
)
acSysLDAPCacheEntryRemovalTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acSysLDAPCacheEntryRemovalTimeout.setStatus("current")
_AcSysLdapConfigurationTable_Object = MibTable
acSysLdapConfigurationTable = _AcSysLdapConfigurationTable_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 15, 21)
)
if mibBuilder.loadTexts:
    acSysLdapConfigurationTable.setStatus("current")
_AcSysLdapConfigurationEntry_Object = MibTableRow
acSysLdapConfigurationEntry = _AcSysLdapConfigurationEntry_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 15, 21, 1)
)
acSysLdapConfigurationEntry.setIndexNames(
    (0, "AC-SYSTEM-MIB", "acSysLdapConfigurationIndex"),
)
if mibBuilder.loadTexts:
    acSysLdapConfigurationEntry.setStatus("current")


class _AcSysLdapConfigurationIndex_Type(Unsigned32):
    """Custom type acSysLdapConfigurationIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_AcSysLdapConfigurationIndex_Type.__name__ = "Unsigned32"
_AcSysLdapConfigurationIndex_Object = MibTableColumn
acSysLdapConfigurationIndex = _AcSysLdapConfigurationIndex_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 15, 21, 1, 1),
    _AcSysLdapConfigurationIndex_Type()
)
acSysLdapConfigurationIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    acSysLdapConfigurationIndex.setStatus("current")
_AcSysLdapConfigurationRowStatus_Type = RowStatus
_AcSysLdapConfigurationRowStatus_Object = MibTableColumn
acSysLdapConfigurationRowStatus = _AcSysLdapConfigurationRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 15, 21, 1, 2),
    _AcSysLdapConfigurationRowStatus_Type()
)
acSysLdapConfigurationRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acSysLdapConfigurationRowStatus.setStatus("current")


class _AcSysLdapConfigurationAction_Type(Integer32):
    """Custom type acSysLdapConfigurationAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            0
        )
    )
    namedValues = NamedValues(
        ("none", 0)
    )


_AcSysLdapConfigurationAction_Type.__name__ = "Integer32"
_AcSysLdapConfigurationAction_Object = MibTableColumn
acSysLdapConfigurationAction = _AcSysLdapConfigurationAction_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 15, 21, 1, 3),
    _AcSysLdapConfigurationAction_Type()
)
acSysLdapConfigurationAction.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acSysLdapConfigurationAction.setStatus("current")


class _AcSysLdapConfigurationActionRes_Type(Integer32):
    """Custom type acSysLdapConfigurationActionRes based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            0
        )
    )
    namedValues = NamedValues(
        ("succeeded", 0)
    )


_AcSysLdapConfigurationActionRes_Type.__name__ = "Integer32"
_AcSysLdapConfigurationActionRes_Object = MibTableColumn
acSysLdapConfigurationActionRes = _AcSysLdapConfigurationActionRes_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 15, 21, 1, 4),
    _AcSysLdapConfigurationActionRes_Type()
)
acSysLdapConfigurationActionRes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSysLdapConfigurationActionRes.setStatus("current")
_AcSysLdapConfigurationServerIp_Type = IpAddress
_AcSysLdapConfigurationServerIp_Object = MibTableColumn
acSysLdapConfigurationServerIp = _AcSysLdapConfigurationServerIp_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 15, 21, 1, 5),
    _AcSysLdapConfigurationServerIp_Type()
)
acSysLdapConfigurationServerIp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acSysLdapConfigurationServerIp.setStatus("deprecated")


class _AcSysLdapConfigurationServerPort_Type(Unsigned32):
    """Custom type acSysLdapConfigurationServerPort based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AcSysLdapConfigurationServerPort_Type.__name__ = "Unsigned32"
_AcSysLdapConfigurationServerPort_Object = MibTableColumn
acSysLdapConfigurationServerPort = _AcSysLdapConfigurationServerPort_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 15, 21, 1, 6),
    _AcSysLdapConfigurationServerPort_Type()
)
acSysLdapConfigurationServerPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acSysLdapConfigurationServerPort.setStatus("current")


class _AcSysLdapConfigurationMaxRespondTime_Type(Unsigned32):
    """Custom type acSysLdapConfigurationMaxRespondTime based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 86400),
    )


_AcSysLdapConfigurationMaxRespondTime_Type.__name__ = "Unsigned32"
_AcSysLdapConfigurationMaxRespondTime_Object = MibTableColumn
acSysLdapConfigurationMaxRespondTime = _AcSysLdapConfigurationMaxRespondTime_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 15, 21, 1, 7),
    _AcSysLdapConfigurationMaxRespondTime_Type()
)
acSysLdapConfigurationMaxRespondTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acSysLdapConfigurationMaxRespondTime.setStatus("current")


class _AcSysLdapConfigurationServerDomainName_Type(SnmpAdminString):
    """Custom type acSysLdapConfigurationServerDomainName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_AcSysLdapConfigurationServerDomainName_Type.__name__ = "SnmpAdminString"
_AcSysLdapConfigurationServerDomainName_Object = MibTableColumn
acSysLdapConfigurationServerDomainName = _AcSysLdapConfigurationServerDomainName_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 15, 21, 1, 8),
    _AcSysLdapConfigurationServerDomainName_Type()
)
acSysLdapConfigurationServerDomainName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acSysLdapConfigurationServerDomainName.setStatus("current")


class _AcSysLdapConfigurationPassword_Type(SnmpAdminString):
    """Custom type acSysLdapConfigurationPassword based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_AcSysLdapConfigurationPassword_Type.__name__ = "SnmpAdminString"
_AcSysLdapConfigurationPassword_Object = MibTableColumn
acSysLdapConfigurationPassword = _AcSysLdapConfigurationPassword_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 15, 21, 1, 9),
    _AcSysLdapConfigurationPassword_Type()
)
acSysLdapConfigurationPassword.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acSysLdapConfigurationPassword.setStatus("current")


class _AcSysLdapConfigurationBindDn_Type(SnmpAdminString):
    """Custom type acSysLdapConfigurationBindDn based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_AcSysLdapConfigurationBindDn_Type.__name__ = "SnmpAdminString"
_AcSysLdapConfigurationBindDn_Object = MibTableColumn
acSysLdapConfigurationBindDn = _AcSysLdapConfigurationBindDn_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 15, 21, 1, 10),
    _AcSysLdapConfigurationBindDn_Type()
)
acSysLdapConfigurationBindDn.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acSysLdapConfigurationBindDn.setStatus("current")


class _AcSysLdapConfigurationInterfaceType_Type(Unsigned32):
    """Custom type acSysLdapConfigurationInterfaceType based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_AcSysLdapConfigurationInterfaceType_Type.__name__ = "Unsigned32"
_AcSysLdapConfigurationInterfaceType_Object = MibTableColumn
acSysLdapConfigurationInterfaceType = _AcSysLdapConfigurationInterfaceType_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 15, 21, 1, 11),
    _AcSysLdapConfigurationInterfaceType_Type()
)
acSysLdapConfigurationInterfaceType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acSysLdapConfigurationInterfaceType.setStatus("current")


class _AcSysLdapConfigurationConnectionStatus_Type(Integer32):
    """Custom type acSysLdapConfigurationConnectionStatus based on Integer32"""
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
        *(("ldapNotApplicable", 0),
          ("ldapConnectionBroken", 1),
          ("ldapConnecting", 2),
          ("ldapConnected", 3))
    )


_AcSysLdapConfigurationConnectionStatus_Type.__name__ = "Integer32"
_AcSysLdapConfigurationConnectionStatus_Object = MibTableColumn
acSysLdapConfigurationConnectionStatus = _AcSysLdapConfigurationConnectionStatus_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 15, 21, 1, 12),
    _AcSysLdapConfigurationConnectionStatus_Type()
)
acSysLdapConfigurationConnectionStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSysLdapConfigurationConnectionStatus.setStatus("current")
_AcSysLdapServersSearchDNsTable_Object = MibTable
acSysLdapServersSearchDNsTable = _AcSysLdapServersSearchDNsTable_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 15, 22)
)
if mibBuilder.loadTexts:
    acSysLdapServersSearchDNsTable.setStatus("current")
_AcSysLdapServersSearchDNsEntry_Object = MibTableRow
acSysLdapServersSearchDNsEntry = _AcSysLdapServersSearchDNsEntry_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 15, 22, 1)
)
acSysLdapServersSearchDNsEntry.setIndexNames(
    (0, "AC-SYSTEM-MIB", "acSysLdapServersSearchDNsLdapConfigurationIndex"),
    (0, "AC-SYSTEM-MIB", "acSysLdapServersSearchDNsInternalIndex"),
)
if mibBuilder.loadTexts:
    acSysLdapServersSearchDNsEntry.setStatus("current")


class _AcSysLdapServersSearchDNsLdapConfigurationIndex_Type(Unsigned32):
    """Custom type acSysLdapServersSearchDNsLdapConfigurationIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_AcSysLdapServersSearchDNsLdapConfigurationIndex_Type.__name__ = "Unsigned32"
_AcSysLdapServersSearchDNsLdapConfigurationIndex_Object = MibTableColumn
acSysLdapServersSearchDNsLdapConfigurationIndex = _AcSysLdapServersSearchDNsLdapConfigurationIndex_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 15, 22, 1, 1),
    _AcSysLdapServersSearchDNsLdapConfigurationIndex_Type()
)
acSysLdapServersSearchDNsLdapConfigurationIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    acSysLdapServersSearchDNsLdapConfigurationIndex.setStatus("current")


class _AcSysLdapServersSearchDNsInternalIndex_Type(Unsigned32):
    """Custom type acSysLdapServersSearchDNsInternalIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5),
    )


_AcSysLdapServersSearchDNsInternalIndex_Type.__name__ = "Unsigned32"
_AcSysLdapServersSearchDNsInternalIndex_Object = MibTableColumn
acSysLdapServersSearchDNsInternalIndex = _AcSysLdapServersSearchDNsInternalIndex_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 15, 22, 1, 2),
    _AcSysLdapServersSearchDNsInternalIndex_Type()
)
acSysLdapServersSearchDNsInternalIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    acSysLdapServersSearchDNsInternalIndex.setStatus("current")
_AcSysLdapServersSearchDNsRowStatus_Type = RowStatus
_AcSysLdapServersSearchDNsRowStatus_Object = MibTableColumn
acSysLdapServersSearchDNsRowStatus = _AcSysLdapServersSearchDNsRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 15, 22, 1, 3),
    _AcSysLdapServersSearchDNsRowStatus_Type()
)
acSysLdapServersSearchDNsRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acSysLdapServersSearchDNsRowStatus.setStatus("current")


class _AcSysLdapServersSearchDNsAction_Type(Integer32):
    """Custom type acSysLdapServersSearchDNsAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            0
        )
    )
    namedValues = NamedValues(
        ("none", 0)
    )


_AcSysLdapServersSearchDNsAction_Type.__name__ = "Integer32"
_AcSysLdapServersSearchDNsAction_Object = MibTableColumn
acSysLdapServersSearchDNsAction = _AcSysLdapServersSearchDNsAction_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 15, 22, 1, 4),
    _AcSysLdapServersSearchDNsAction_Type()
)
acSysLdapServersSearchDNsAction.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acSysLdapServersSearchDNsAction.setStatus("current")


class _AcSysLdapServersSearchDNsActionRes_Type(Integer32):
    """Custom type acSysLdapServersSearchDNsActionRes based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            0
        )
    )
    namedValues = NamedValues(
        ("succeeded", 0)
    )


_AcSysLdapServersSearchDNsActionRes_Type.__name__ = "Integer32"
_AcSysLdapServersSearchDNsActionRes_Object = MibTableColumn
acSysLdapServersSearchDNsActionRes = _AcSysLdapServersSearchDNsActionRes_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 15, 22, 1, 5),
    _AcSysLdapServersSearchDNsActionRes_Type()
)
acSysLdapServersSearchDNsActionRes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSysLdapServersSearchDNsActionRes.setStatus("current")


class _AcSysLdapServersSearchDNsBasePath_Type(SnmpAdminString):
    """Custom type acSysLdapServersSearchDNsBasePath based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_AcSysLdapServersSearchDNsBasePath_Type.__name__ = "SnmpAdminString"
_AcSysLdapServersSearchDNsBasePath_Object = MibTableColumn
acSysLdapServersSearchDNsBasePath = _AcSysLdapServersSearchDNsBasePath_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 15, 22, 1, 6),
    _AcSysLdapServersSearchDNsBasePath_Type()
)
acSysLdapServersSearchDNsBasePath.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acSysLdapServersSearchDNsBasePath.setStatus("current")
_AsSysNqm_ObjectIdentity = ObjectIdentity
asSysNqm = _AsSysNqm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 16)
)
_AcSysNqmSenderTable_Object = MibTable
acSysNqmSenderTable = _AcSysNqmSenderTable_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 16, 21)
)
if mibBuilder.loadTexts:
    acSysNqmSenderTable.setStatus("current")
_AcSysNqmSenderEntry_Object = MibTableRow
acSysNqmSenderEntry = _AcSysNqmSenderEntry_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 16, 21, 1)
)
acSysNqmSenderEntry.setIndexNames(
    (0, "AC-SYSTEM-MIB", "acSysNqmSenderIndex"),
)
if mibBuilder.loadTexts:
    acSysNqmSenderEntry.setStatus("current")


class _AcSysNqmSenderIndex_Type(Unsigned32):
    """Custom type acSysNqmSenderIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 9),
    )


_AcSysNqmSenderIndex_Type.__name__ = "Unsigned32"
_AcSysNqmSenderIndex_Object = MibTableColumn
acSysNqmSenderIndex = _AcSysNqmSenderIndex_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 16, 21, 1, 1),
    _AcSysNqmSenderIndex_Type()
)
acSysNqmSenderIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    acSysNqmSenderIndex.setStatus("current")
_AcSysNqmSenderRowStatus_Type = RowStatus
_AcSysNqmSenderRowStatus_Object = MibTableColumn
acSysNqmSenderRowStatus = _AcSysNqmSenderRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 16, 21, 1, 2),
    _AcSysNqmSenderRowStatus_Type()
)
acSysNqmSenderRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acSysNqmSenderRowStatus.setStatus("current")


class _AcSysNqmSenderAction_Type(Integer32):
    """Custom type acSysNqmSenderAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            0
        )
    )
    namedValues = NamedValues(
        ("none", 0)
    )


_AcSysNqmSenderAction_Type.__name__ = "Integer32"
_AcSysNqmSenderAction_Object = MibTableColumn
acSysNqmSenderAction = _AcSysNqmSenderAction_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 16, 21, 1, 3),
    _AcSysNqmSenderAction_Type()
)
acSysNqmSenderAction.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acSysNqmSenderAction.setStatus("current")


class _AcSysNqmSenderActionRes_Type(Integer32):
    """Custom type acSysNqmSenderActionRes based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            0
        )
    )
    namedValues = NamedValues(
        ("succeeded", 0)
    )


_AcSysNqmSenderActionRes_Type.__name__ = "Integer32"
_AcSysNqmSenderActionRes_Object = MibTableColumn
acSysNqmSenderActionRes = _AcSysNqmSenderActionRes_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 16, 21, 1, 4),
    _AcSysNqmSenderActionRes_Type()
)
acSysNqmSenderActionRes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSysNqmSenderActionRes.setStatus("current")


class _AcSysNqmSenderSenderName_Type(SnmpAdminString):
    """Custom type acSysNqmSenderSenderName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_AcSysNqmSenderSenderName_Type.__name__ = "SnmpAdminString"
_AcSysNqmSenderSenderName_Object = MibTableColumn
acSysNqmSenderSenderName = _AcSysNqmSenderSenderName_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 16, 21, 1, 5),
    _AcSysNqmSenderSenderName_Type()
)
acSysNqmSenderSenderName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acSysNqmSenderSenderName.setStatus("current")


class _AcSysNqmSenderActive_Type(Integer32):
    """Custom type acSysNqmSenderActive based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_AcSysNqmSenderActive_Type.__name__ = "Integer32"
_AcSysNqmSenderActive_Object = MibTableColumn
acSysNqmSenderActive = _AcSysNqmSenderActive_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 16, 21, 1, 6),
    _AcSysNqmSenderActive_Type()
)
acSysNqmSenderActive.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acSysNqmSenderActive.setStatus("current")


class _AcSysNqmSenderTargetIpAddress_Type(SnmpAdminString):
    """Custom type acSysNqmSenderTargetIpAddress based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 45),
    )


_AcSysNqmSenderTargetIpAddress_Type.__name__ = "SnmpAdminString"
_AcSysNqmSenderTargetIpAddress_Object = MibTableColumn
acSysNqmSenderTargetIpAddress = _AcSysNqmSenderTargetIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 16, 21, 1, 7),
    _AcSysNqmSenderTargetIpAddress_Type()
)
acSysNqmSenderTargetIpAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acSysNqmSenderTargetIpAddress.setStatus("current")


class _AcSysNqmSenderTargetPort_Type(Unsigned32):
    """Custom type acSysNqmSenderTargetPort based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(3900, 3990),
    )


_AcSysNqmSenderTargetPort_Type.__name__ = "Unsigned32"
_AcSysNqmSenderTargetPort_Object = MibTableColumn
acSysNqmSenderTargetPort = _AcSysNqmSenderTargetPort_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 16, 21, 1, 8),
    _AcSysNqmSenderTargetPort_Type()
)
acSysNqmSenderTargetPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acSysNqmSenderTargetPort.setStatus("current")


class _AcSysNqmSenderPacketInterval_Type(Unsigned32):
    """Custom type acSysNqmSenderPacketInterval based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 1000),
    )


_AcSysNqmSenderPacketInterval_Type.__name__ = "Unsigned32"
_AcSysNqmSenderPacketInterval_Object = MibTableColumn
acSysNqmSenderPacketInterval = _AcSysNqmSenderPacketInterval_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 16, 21, 1, 9),
    _AcSysNqmSenderPacketInterval_Type()
)
acSysNqmSenderPacketInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acSysNqmSenderPacketInterval.setStatus("current")


class _AcSysNqmSenderPayloadSize_Type(Unsigned32):
    """Custom type acSysNqmSenderPayloadSize based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(28, 1420),
    )


_AcSysNqmSenderPayloadSize_Type.__name__ = "Unsigned32"
_AcSysNqmSenderPayloadSize_Object = MibTableColumn
acSysNqmSenderPayloadSize = _AcSysNqmSenderPayloadSize_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 16, 21, 1, 10),
    _AcSysNqmSenderPayloadSize_Type()
)
acSysNqmSenderPayloadSize.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acSysNqmSenderPayloadSize.setStatus("current")


class _AcSysNqmSenderIpTos_Type(Unsigned32):
    """Custom type acSysNqmSenderIpTos based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AcSysNqmSenderIpTos_Type.__name__ = "Unsigned32"
_AcSysNqmSenderIpTos_Object = MibTableColumn
acSysNqmSenderIpTos = _AcSysNqmSenderIpTos_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 16, 21, 1, 11),
    _AcSysNqmSenderIpTos_Type()
)
acSysNqmSenderIpTos.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acSysNqmSenderIpTos.setStatus("current")


class _AcSysNqmSenderTimeout_Type(Unsigned32):
    """Custom type acSysNqmSenderTimeout based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32000),
    )


_AcSysNqmSenderTimeout_Type.__name__ = "Unsigned32"
_AcSysNqmSenderTimeout_Object = MibTableColumn
acSysNqmSenderTimeout = _AcSysNqmSenderTimeout_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 16, 21, 1, 12),
    _AcSysNqmSenderTimeout_Type()
)
acSysNqmSenderTimeout.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acSysNqmSenderTimeout.setStatus("current")


class _AcSysNqmSenderRttThreshold_Type(Unsigned32):
    """Custom type acSysNqmSenderRttThreshold based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32000),
    )


_AcSysNqmSenderRttThreshold_Type.__name__ = "Unsigned32"
_AcSysNqmSenderRttThreshold_Object = MibTableColumn
acSysNqmSenderRttThreshold = _AcSysNqmSenderRttThreshold_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 16, 21, 1, 13),
    _AcSysNqmSenderRttThreshold_Type()
)
acSysNqmSenderRttThreshold.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acSysNqmSenderRttThreshold.setStatus("current")


class _AcSysNqmSenderJitterThreshold_Type(Unsigned32):
    """Custom type acSysNqmSenderJitterThreshold based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32000),
    )


_AcSysNqmSenderJitterThreshold_Type.__name__ = "Unsigned32"
_AcSysNqmSenderJitterThreshold_Object = MibTableColumn
acSysNqmSenderJitterThreshold = _AcSysNqmSenderJitterThreshold_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 16, 21, 1, 14),
    _AcSysNqmSenderJitterThreshold_Type()
)
acSysNqmSenderJitterThreshold.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acSysNqmSenderJitterThreshold.setStatus("current")


class _AcSysNqmSenderPacketLossThershold_Type(Unsigned32):
    """Custom type acSysNqmSenderPacketLossThershold based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32000),
    )


_AcSysNqmSenderPacketLossThershold_Type.__name__ = "Unsigned32"
_AcSysNqmSenderPacketLossThershold_Object = MibTableColumn
acSysNqmSenderPacketLossThershold = _AcSysNqmSenderPacketLossThershold_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 16, 21, 1, 15),
    _AcSysNqmSenderPacketLossThershold_Type()
)
acSysNqmSenderPacketLossThershold.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acSysNqmSenderPacketLossThershold.setStatus("current")
_AcSysNqmSenderProbingConfigName_Type = RowPointer
_AcSysNqmSenderProbingConfigName_Object = MibTableColumn
acSysNqmSenderProbingConfigName = _AcSysNqmSenderProbingConfigName_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 16, 21, 1, 16),
    _AcSysNqmSenderProbingConfigName_Type()
)
acSysNqmSenderProbingConfigName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acSysNqmSenderProbingConfigName.setStatus("current")
_AcSysNqmSenderSourceInterfaceName_Type = RowPointer
_AcSysNqmSenderSourceInterfaceName_Object = MibTableColumn
acSysNqmSenderSourceInterfaceName = _AcSysNqmSenderSourceInterfaceName_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 16, 21, 1, 17),
    _AcSysNqmSenderSourceInterfaceName_Type()
)
acSysNqmSenderSourceInterfaceName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acSysNqmSenderSourceInterfaceName.setStatus("current")
_AcSysNqmProbingTable_Object = MibTable
acSysNqmProbingTable = _AcSysNqmProbingTable_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 16, 22)
)
if mibBuilder.loadTexts:
    acSysNqmProbingTable.setStatus("current")
_AcSysNqmProbingEntry_Object = MibTableRow
acSysNqmProbingEntry = _AcSysNqmProbingEntry_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 16, 22, 1)
)
acSysNqmProbingEntry.setIndexNames(
    (0, "AC-SYSTEM-MIB", "acSysNqmProbingIndex"),
)
if mibBuilder.loadTexts:
    acSysNqmProbingEntry.setStatus("current")


class _AcSysNqmProbingIndex_Type(Unsigned32):
    """Custom type acSysNqmProbingIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 9),
    )


_AcSysNqmProbingIndex_Type.__name__ = "Unsigned32"
_AcSysNqmProbingIndex_Object = MibTableColumn
acSysNqmProbingIndex = _AcSysNqmProbingIndex_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 16, 22, 1, 1),
    _AcSysNqmProbingIndex_Type()
)
acSysNqmProbingIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    acSysNqmProbingIndex.setStatus("current")
_AcSysNqmProbingRowStatus_Type = RowStatus
_AcSysNqmProbingRowStatus_Object = MibTableColumn
acSysNqmProbingRowStatus = _AcSysNqmProbingRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 16, 22, 1, 2),
    _AcSysNqmProbingRowStatus_Type()
)
acSysNqmProbingRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acSysNqmProbingRowStatus.setStatus("current")


class _AcSysNqmProbingAction_Type(Integer32):
    """Custom type acSysNqmProbingAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            0
        )
    )
    namedValues = NamedValues(
        ("none", 0)
    )


_AcSysNqmProbingAction_Type.__name__ = "Integer32"
_AcSysNqmProbingAction_Object = MibTableColumn
acSysNqmProbingAction = _AcSysNqmProbingAction_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 16, 22, 1, 3),
    _AcSysNqmProbingAction_Type()
)
acSysNqmProbingAction.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acSysNqmProbingAction.setStatus("current")


class _AcSysNqmProbingActionRes_Type(Integer32):
    """Custom type acSysNqmProbingActionRes based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            0
        )
    )
    namedValues = NamedValues(
        ("succeeded", 0)
    )


_AcSysNqmProbingActionRes_Type.__name__ = "Integer32"
_AcSysNqmProbingActionRes_Object = MibTableColumn
acSysNqmProbingActionRes = _AcSysNqmProbingActionRes_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 16, 22, 1, 4),
    _AcSysNqmProbingActionRes_Type()
)
acSysNqmProbingActionRes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSysNqmProbingActionRes.setStatus("current")


class _AcSysNqmProbingProbeName_Type(SnmpAdminString):
    """Custom type acSysNqmProbingProbeName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_AcSysNqmProbingProbeName_Type.__name__ = "SnmpAdminString"
_AcSysNqmProbingProbeName_Object = MibTableColumn
acSysNqmProbingProbeName = _AcSysNqmProbingProbeName_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 16, 22, 1, 5),
    _AcSysNqmProbingProbeName_Type()
)
acSysNqmProbingProbeName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acSysNqmProbingProbeName.setStatus("current")


class _AcSysNqmProbingDuration_Type(Unsigned32):
    """Custom type acSysNqmProbingDuration based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(20, 32000),
    )


_AcSysNqmProbingDuration_Type.__name__ = "Unsigned32"
_AcSysNqmProbingDuration_Object = MibTableColumn
acSysNqmProbingDuration = _AcSysNqmProbingDuration_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 16, 22, 1, 6),
    _AcSysNqmProbingDuration_Type()
)
acSysNqmProbingDuration.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acSysNqmProbingDuration.setStatus("current")


class _AcSysNqmProbingFrequency_Type(Unsigned32):
    """Custom type acSysNqmProbingFrequency based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32000),
    )


_AcSysNqmProbingFrequency_Type.__name__ = "Unsigned32"
_AcSysNqmProbingFrequency_Object = MibTableColumn
acSysNqmProbingFrequency = _AcSysNqmProbingFrequency_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 16, 22, 1, 7),
    _AcSysNqmProbingFrequency_Type()
)
acSysNqmProbingFrequency.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acSysNqmProbingFrequency.setStatus("current")


class _AcSysNqmProbingLifeSpan_Type(Unsigned32):
    """Custom type acSysNqmProbingLifeSpan based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2000000000),
    )


_AcSysNqmProbingLifeSpan_Type.__name__ = "Unsigned32"
_AcSysNqmProbingLifeSpan_Object = MibTableColumn
acSysNqmProbingLifeSpan = _AcSysNqmProbingLifeSpan_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 16, 22, 1, 8),
    _AcSysNqmProbingLifeSpan_Type()
)
acSysNqmProbingLifeSpan.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acSysNqmProbingLifeSpan.setStatus("current")


class _AcSysNqmProbingStartTime_Type(SnmpAdminString):
    """Custom type acSysNqmProbingStartTime based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_AcSysNqmProbingStartTime_Type.__name__ = "SnmpAdminString"
_AcSysNqmProbingStartTime_Object = MibTableColumn
acSysNqmProbingStartTime = _AcSysNqmProbingStartTime_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 16, 22, 1, 9),
    _AcSysNqmProbingStartTime_Type()
)
acSysNqmProbingStartTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acSysNqmProbingStartTime.setStatus("current")


class _AcSysNqmProbingHistoryEntriesToKeep_Type(Unsigned32):
    """Custom type acSysNqmProbingHistoryEntriesToKeep based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1000),
    )


_AcSysNqmProbingHistoryEntriesToKeep_Type.__name__ = "Unsigned32"
_AcSysNqmProbingHistoryEntriesToKeep_Object = MibTableColumn
acSysNqmProbingHistoryEntriesToKeep = _AcSysNqmProbingHistoryEntriesToKeep_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 16, 22, 1, 10),
    _AcSysNqmProbingHistoryEntriesToKeep_Type()
)
acSysNqmProbingHistoryEntriesToKeep.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acSysNqmProbingHistoryEntriesToKeep.setStatus("current")
_AcSysNqmResponderTable_Object = MibTable
acSysNqmResponderTable = _AcSysNqmResponderTable_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 16, 23)
)
if mibBuilder.loadTexts:
    acSysNqmResponderTable.setStatus("current")
_AcSysNqmResponderEntry_Object = MibTableRow
acSysNqmResponderEntry = _AcSysNqmResponderEntry_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 16, 23, 1)
)
acSysNqmResponderEntry.setIndexNames(
    (0, "AC-SYSTEM-MIB", "acSysNqmResponderIndex"),
)
if mibBuilder.loadTexts:
    acSysNqmResponderEntry.setStatus("current")


class _AcSysNqmResponderIndex_Type(Unsigned32):
    """Custom type acSysNqmResponderIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 9),
    )


_AcSysNqmResponderIndex_Type.__name__ = "Unsigned32"
_AcSysNqmResponderIndex_Object = MibTableColumn
acSysNqmResponderIndex = _AcSysNqmResponderIndex_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 16, 23, 1, 1),
    _AcSysNqmResponderIndex_Type()
)
acSysNqmResponderIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    acSysNqmResponderIndex.setStatus("current")
_AcSysNqmResponderRowStatus_Type = RowStatus
_AcSysNqmResponderRowStatus_Object = MibTableColumn
acSysNqmResponderRowStatus = _AcSysNqmResponderRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 16, 23, 1, 2),
    _AcSysNqmResponderRowStatus_Type()
)
acSysNqmResponderRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acSysNqmResponderRowStatus.setStatus("current")


class _AcSysNqmResponderAction_Type(Integer32):
    """Custom type acSysNqmResponderAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            0
        )
    )
    namedValues = NamedValues(
        ("none", 0)
    )


_AcSysNqmResponderAction_Type.__name__ = "Integer32"
_AcSysNqmResponderAction_Object = MibTableColumn
acSysNqmResponderAction = _AcSysNqmResponderAction_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 16, 23, 1, 3),
    _AcSysNqmResponderAction_Type()
)
acSysNqmResponderAction.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acSysNqmResponderAction.setStatus("current")


class _AcSysNqmResponderActionRes_Type(Integer32):
    """Custom type acSysNqmResponderActionRes based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            0
        )
    )
    namedValues = NamedValues(
        ("succeeded", 0)
    )


_AcSysNqmResponderActionRes_Type.__name__ = "Integer32"
_AcSysNqmResponderActionRes_Object = MibTableColumn
acSysNqmResponderActionRes = _AcSysNqmResponderActionRes_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 16, 23, 1, 4),
    _AcSysNqmResponderActionRes_Type()
)
acSysNqmResponderActionRes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSysNqmResponderActionRes.setStatus("current")


class _AcSysNqmResponderResponderName_Type(SnmpAdminString):
    """Custom type acSysNqmResponderResponderName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_AcSysNqmResponderResponderName_Type.__name__ = "SnmpAdminString"
_AcSysNqmResponderResponderName_Object = MibTableColumn
acSysNqmResponderResponderName = _AcSysNqmResponderResponderName_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 16, 23, 1, 5),
    _AcSysNqmResponderResponderName_Type()
)
acSysNqmResponderResponderName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acSysNqmResponderResponderName.setStatus("current")


class _AcSysNqmResponderActive_Type(Unsigned32):
    """Custom type acSysNqmResponderActive based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_AcSysNqmResponderActive_Type.__name__ = "Unsigned32"
_AcSysNqmResponderActive_Object = MibTableColumn
acSysNqmResponderActive = _AcSysNqmResponderActive_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 16, 23, 1, 6),
    _AcSysNqmResponderActive_Type()
)
acSysNqmResponderActive.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acSysNqmResponderActive.setStatus("current")


class _AcSysNqmResponderLocalPort_Type(Unsigned32):
    """Custom type acSysNqmResponderLocalPort based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(3900, 3990),
    )


_AcSysNqmResponderLocalPort_Type.__name__ = "Unsigned32"
_AcSysNqmResponderLocalPort_Object = MibTableColumn
acSysNqmResponderLocalPort = _AcSysNqmResponderLocalPort_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 16, 23, 1, 7),
    _AcSysNqmResponderLocalPort_Type()
)
acSysNqmResponderLocalPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acSysNqmResponderLocalPort.setStatus("current")
_AcSysNqmResponderSourceInterfaceName_Type = RowPointer
_AcSysNqmResponderSourceInterfaceName_Object = MibTableColumn
acSysNqmResponderSourceInterfaceName = _AcSysNqmResponderSourceInterfaceName_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 16, 23, 1, 8),
    _AcSysNqmResponderSourceInterfaceName_Type()
)
acSysNqmResponderSourceInterfaceName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acSysNqmResponderSourceInterfaceName.setStatus("current")
_AcSysLicenseServer_ObjectIdentity = ObjectIdentity
acSysLicenseServer = _AcSysLicenseServer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 17)
)
_AcSysLicenseServerPrimaryIP_Type = IpAddress
_AcSysLicenseServerPrimaryIP_Object = MibScalar
acSysLicenseServerPrimaryIP = _AcSysLicenseServerPrimaryIP_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 17, 1),
    _AcSysLicenseServerPrimaryIP_Type()
)
acSysLicenseServerPrimaryIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acSysLicenseServerPrimaryIP.setStatus("deprecated")
_AcSysLicenseServerSecondaryIP_Type = IpAddress
_AcSysLicenseServerSecondaryIP_Object = MibScalar
acSysLicenseServerSecondaryIP = _AcSysLicenseServerSecondaryIP_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 17, 2),
    _AcSysLicenseServerSecondaryIP_Type()
)
acSysLicenseServerSecondaryIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acSysLicenseServerSecondaryIP.setStatus("deprecated")


class _AcSysLicenseServerPort_Type(Unsigned32):
    """Custom type acSysLicenseServerPort based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_AcSysLicenseServerPort_Type.__name__ = "Unsigned32"
_AcSysLicenseServerPort_Object = MibScalar
acSysLicenseServerPort = _AcSysLicenseServerPort_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 17, 3),
    _AcSysLicenseServerPort_Type()
)
acSysLicenseServerPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acSysLicenseServerPort.setStatus("current")


class _AcSysLicenseServerUsername_Type(SnmpAdminString):
    """Custom type acSysLicenseServerUsername based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_AcSysLicenseServerUsername_Type.__name__ = "SnmpAdminString"
_AcSysLicenseServerUsername_Object = MibScalar
acSysLicenseServerUsername = _AcSysLicenseServerUsername_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 17, 4),
    _AcSysLicenseServerUsername_Type()
)
acSysLicenseServerUsername.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acSysLicenseServerUsername.setStatus("current")


class _AcSysLicenseServerPassword_Type(SnmpAdminString):
    """Custom type acSysLicenseServerPassword based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_AcSysLicenseServerPassword_Type.__name__ = "SnmpAdminString"
_AcSysLicenseServerPassword_Object = MibScalar
acSysLicenseServerPassword = _AcSysLicenseServerPassword_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 17, 5),
    _AcSysLicenseServerPassword_Type()
)
acSysLicenseServerPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acSysLicenseServerPassword.setStatus("current")


class _AcSysLicenseServerEnable_Type(Integer32):
    """Custom type acSysLicenseServerEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_AcSysLicenseServerEnable_Type.__name__ = "Integer32"
_AcSysLicenseServerEnable_Object = MibScalar
acSysLicenseServerEnable = _AcSysLicenseServerEnable_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 17, 6),
    _AcSysLicenseServerEnable_Type()
)
acSysLicenseServerEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acSysLicenseServerEnable.setStatus("current")


class _AcSysLicenseServerActionStatus_Type(Integer32):
    """Custom type acSysLicenseServerActionStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("failure", 0),
          ("inProgress", 1),
          ("success", 2))
    )


_AcSysLicenseServerActionStatus_Type.__name__ = "Integer32"
_AcSysLicenseServerActionStatus_Object = MibScalar
acSysLicenseServerActionStatus = _AcSysLicenseServerActionStatus_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 17, 7),
    _AcSysLicenseServerActionStatus_Type()
)
acSysLicenseServerActionStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSysLicenseServerActionStatus.setStatus("current")


class _AcSysLicenseServerPrimaryAddress_Type(SnmpAdminString):
    """Custom type acSysLicenseServerPrimaryAddress based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 100),
    )


_AcSysLicenseServerPrimaryAddress_Type.__name__ = "SnmpAdminString"
_AcSysLicenseServerPrimaryAddress_Object = MibScalar
acSysLicenseServerPrimaryAddress = _AcSysLicenseServerPrimaryAddress_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 17, 8),
    _AcSysLicenseServerPrimaryAddress_Type()
)
acSysLicenseServerPrimaryAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acSysLicenseServerPrimaryAddress.setStatus("current")


class _AcSysLicenseServerSecondaryAddress_Type(SnmpAdminString):
    """Custom type acSysLicenseServerSecondaryAddress based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 100),
    )


_AcSysLicenseServerSecondaryAddress_Type.__name__ = "SnmpAdminString"
_AcSysLicenseServerSecondaryAddress_Object = MibScalar
acSysLicenseServerSecondaryAddress = _AcSysLicenseServerSecondaryAddress_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 17, 9),
    _AcSysLicenseServerSecondaryAddress_Type()
)
acSysLicenseServerSecondaryAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acSysLicenseServerSecondaryAddress.setStatus("current")
_AcSysFloatingLicense_ObjectIdentity = ObjectIdentity
acSysFloatingLicense = _AcSysFloatingLicense_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 18)
)


class _AcSysFloatingLicenseEnable_Type(Integer32):
    """Custom type acSysFloatingLicenseEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_AcSysFloatingLicenseEnable_Type.__name__ = "Integer32"
_AcSysFloatingLicenseEnable_Object = MibScalar
acSysFloatingLicenseEnable = _AcSysFloatingLicenseEnable_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 18, 1),
    _AcSysFloatingLicenseEnable_Type()
)
acSysFloatingLicenseEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acSysFloatingLicenseEnable.setStatus("current")
_AcSysFloatingLicensePrimaryIP_Type = IpAddress
_AcSysFloatingLicensePrimaryIP_Object = MibScalar
acSysFloatingLicensePrimaryIP = _AcSysFloatingLicensePrimaryIP_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 18, 2),
    _AcSysFloatingLicensePrimaryIP_Type()
)
acSysFloatingLicensePrimaryIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acSysFloatingLicensePrimaryIP.setStatus("deprecated")
_AcSysFloatingLicenseSecondaryIP_Type = IpAddress
_AcSysFloatingLicenseSecondaryIP_Object = MibScalar
acSysFloatingLicenseSecondaryIP = _AcSysFloatingLicenseSecondaryIP_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 18, 3),
    _AcSysFloatingLicenseSecondaryIP_Type()
)
acSysFloatingLicenseSecondaryIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acSysFloatingLicenseSecondaryIP.setStatus("deprecated")


class _AcSysFloatingLicensePort_Type(Unsigned32):
    """Custom type acSysFloatingLicensePort based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_AcSysFloatingLicensePort_Type.__name__ = "Unsigned32"
_AcSysFloatingLicensePort_Object = MibScalar
acSysFloatingLicensePort = _AcSysFloatingLicensePort_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 18, 4),
    _AcSysFloatingLicensePort_Type()
)
acSysFloatingLicensePort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acSysFloatingLicensePort.setStatus("current")


class _AcSysFloatingLicenseUsername_Type(SnmpAdminString):
    """Custom type acSysFloatingLicenseUsername based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_AcSysFloatingLicenseUsername_Type.__name__ = "SnmpAdminString"
_AcSysFloatingLicenseUsername_Object = MibScalar
acSysFloatingLicenseUsername = _AcSysFloatingLicenseUsername_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 18, 5),
    _AcSysFloatingLicenseUsername_Type()
)
acSysFloatingLicenseUsername.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acSysFloatingLicenseUsername.setStatus("current")


class _AcSysFloatingLicensePassword_Type(SnmpAdminString):
    """Custom type acSysFloatingLicensePassword based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_AcSysFloatingLicensePassword_Type.__name__ = "SnmpAdminString"
_AcSysFloatingLicensePassword_Object = MibScalar
acSysFloatingLicensePassword = _AcSysFloatingLicensePassword_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 18, 6),
    _AcSysFloatingLicensePassword_Type()
)
acSysFloatingLicensePassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acSysFloatingLicensePassword.setStatus("current")


class _AcSysFloatingLicenseUpdate_Type(Integer32):
    """Custom type acSysFloatingLicenseUpdate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("updateDone", 0),
          ("upadate", 1))
    )


_AcSysFloatingLicenseUpdate_Type.__name__ = "Integer32"
_AcSysFloatingLicenseUpdate_Object = MibScalar
acSysFloatingLicenseUpdate = _AcSysFloatingLicenseUpdate_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 18, 7),
    _AcSysFloatingLicenseUpdate_Type()
)
acSysFloatingLicenseUpdate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acSysFloatingLicenseUpdate.setStatus("current")


class _AcSysFloatingLicenseServerStatus_Type(Integer32):
    """Custom type acSysFloatingLicenseServerStatus based on Integer32"""
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
        *(("notApplicable", 0),
          ("notConnected", 1),
          ("rejected", 2),
          ("temporaryDisconnected", 3),
          ("connected", 4))
    )


_AcSysFloatingLicenseServerStatus_Type.__name__ = "Integer32"
_AcSysFloatingLicenseServerStatus_Object = MibScalar
acSysFloatingLicenseServerStatus = _AcSysFloatingLicenseServerStatus_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 18, 8),
    _AcSysFloatingLicenseServerStatus_Type()
)
acSysFloatingLicenseServerStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSysFloatingLicenseServerStatus.setStatus("current")


class _AcSysFloatingLicenseOvocProductID_Type(SnmpAdminString):
    """Custom type acSysFloatingLicenseOvocProductID based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_AcSysFloatingLicenseOvocProductID_Type.__name__ = "SnmpAdminString"
_AcSysFloatingLicenseOvocProductID_Object = MibScalar
acSysFloatingLicenseOvocProductID = _AcSysFloatingLicenseOvocProductID_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 18, 9),
    _AcSysFloatingLicenseOvocProductID_Type()
)
acSysFloatingLicenseOvocProductID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acSysFloatingLicenseOvocProductID.setStatus("current")


class _AcSysFloatingLicensePrimaryAddress_Type(SnmpAdminString):
    """Custom type acSysFloatingLicensePrimaryAddress based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 100),
    )


_AcSysFloatingLicensePrimaryAddress_Type.__name__ = "SnmpAdminString"
_AcSysFloatingLicensePrimaryAddress_Object = MibScalar
acSysFloatingLicensePrimaryAddress = _AcSysFloatingLicensePrimaryAddress_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 18, 10),
    _AcSysFloatingLicensePrimaryAddress_Type()
)
acSysFloatingLicensePrimaryAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acSysFloatingLicensePrimaryAddress.setStatus("current")
_AcSystemStatus_ObjectIdentity = ObjectIdentity
acSystemStatus = _AcSystemStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 2)
)
_AcSysType_ObjectIdentity = ObjectIdentity
acSysType = _AcSysType_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 2, 1)
)


class _AcSysTypeProduct_Type(Integer32):
    """Custom type acSysTypeProduct based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              20,
              22,
              23,
              24,
              25,
              26,
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
              71,
              72,
              73,
              74,
              75,
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
              90)
        )
    )
    namedValues = NamedValues(
        *(("acUnknown", 0),
          ("acTrunkPack-08", 1),
          ("acMediaPack-108", 2),
          ("acMediaPack-124", 3),
          ("acTrunkPack-1600", 20),
          ("acTPM1100", 22),
          ("acTrunkPack-260-IpMedia", 23),
          ("acTrunkPack-1610", 24),
          ("acMediaPack-104", 25),
          ("acMediaPack-102", 26),
          ("acTrunkPack-1610-SB", 29),
          ("acTrunkPack-1610-IpMedia", 30),
          ("acTrunkPack-MEDIANT2000", 31),
          ("acTrunkPack-STRETTO2000", 32),
          ("acTrunkPack-IPMServer2000", 33),
          ("acTrunkPack-2810", 34),
          ("acTrunkPack-260-UN-IpMedia", 35),
          ("acTrunkPack-260-IpMedia-30Ch", 36),
          ("acTrunkPack-260-IpMedia-60Ch", 37),
          ("acTrunkPack-260-IpMedia-120Ch", 38),
          ("acTrunkPack-260RT-IpMedia-30Ch", 39),
          ("acTrunkPack-260RT-IpMedia-60Ch", 40),
          ("acTrunkPack-260RT-IpMedia-120Ch", 41),
          ("acTrunkPack-260", 42),
          ("acTrunkPack-260-UN", 43),
          ("acTPM1100-PCM", 44),
          ("acTrunkPack-6310", 45),
          ("acTPM6300", 46),
          ("acMediant1000", 47),
          ("acIPMedia3000", 48),
          ("acMediant3000", 49),
          ("acStretto3000", 50),
          ("acTrunkPack-6310-IpMedia", 51),
          ("acTrunkPack-6310-SB", 52),
          ("acATP-1610", 53),
          ("acATP-260", 54),
          ("acATP-260-UN", 55),
          ("acMediaPack-118", 56),
          ("acMediaPack114", 57),
          ("acMediaPack112", 58),
          ("acTrunkPack-6310-T3", 59),
          ("acMediant3000-T3", 60),
          ("acIPmedia3000-T3", 61),
          ("acTrunkPack-6310-T3-IpMedia", 62),
          ("acTrunkPack-8410", 63),
          ("acTrunkPack-8410-IpMedia", 64),
          ("acMediant-600", 65),
          ("acTrunkPack-12610", 66),
          ("acMediant1000-MSBR", 67),
          ("acMediant-600-MSBR", 68),
          ("acMediant800-MSBR", 69),
          ("acMediant-4000", 70),
          ("acMediant1000-ESBC", 71),
          ("acMediant800-ESBC", 72),
          ("acHosted", 73),
          ("acMediant-800B-MSBR", 74),
          ("acMediant-800B-ESBC", 75),
          ("acMediant-500-MSBR", 76),
          ("acMediant-500-ESBC", 77),
          ("acMediant-2600", 78),
          ("acMediant-VE-SBC", 79),
          ("acMediant-VE-H-SBC", 80),
          ("acMediant-SE-SBC", 81),
          ("acMediant-SE-H-SBC", 82),
          ("acMediant-9000-SBC", 83),
          ("acMediant-500L-MSBR", 84),
          ("acMediant-500L-ESBC", 85),
          ("acMediaPack-1288", 86),
          ("acMediaTranscoder", 87),
          ("acVirtualMediaTranscoder", 88),
          ("acMediant-500NG", 89),
          ("acMediant-3100", 90))
    )


_AcSysTypeProduct_Type.__name__ = "Integer32"
_AcSysTypeProduct_Object = MibScalar
acSysTypeProduct = _AcSysTypeProduct_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 2, 1, 1),
    _AcSysTypeProduct_Type()
)
acSysTypeProduct.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSysTypeProduct.setStatus("current")


class _AcSysTypeDSP_Type(Unsigned32):
    """Custom type acSysTypeDSP based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AcSysTypeDSP_Type.__name__ = "Unsigned32"
_AcSysTypeDSP_Object = MibScalar
acSysTypeDSP = _AcSysTypeDSP_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 2, 1, 2),
    _AcSysTypeDSP_Type()
)
acSysTypeDSP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSysTypeDSP.setStatus("current")


class _AcSysTypeModule_Type(Integer32):
    """Custom type acSysTypeModule based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("soloist", 0),
          ("second", 1),
          ("first", 2))
    )


_AcSysTypeModule_Type.__name__ = "Integer32"
_AcSysTypeModule_Object = MibScalar
acSysTypeModule = _AcSysTypeModule_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 2, 1, 3),
    _AcSysTypeModule_Type()
)
acSysTypeModule.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSysTypeModule.setStatus("current")


class _AcSysTypeCPUSpeed_Type(Unsigned32):
    """Custom type acSysTypeCPUSpeed based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AcSysTypeCPUSpeed_Type.__name__ = "Unsigned32"
_AcSysTypeCPUSpeed_Object = MibScalar
acSysTypeCPUSpeed = _AcSysTypeCPUSpeed_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 2, 1, 4),
    _AcSysTypeCPUSpeed_Type()
)
acSysTypeCPUSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSysTypeCPUSpeed.setStatus("current")


class _AcSysTypeOSType_Type(SnmpAdminString):
    """Custom type acSysTypeOSType based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_AcSysTypeOSType_Type.__name__ = "SnmpAdminString"
_AcSysTypeOSType_Object = MibScalar
acSysTypeOSType = _AcSysTypeOSType_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 2, 1, 5),
    _AcSysTypeOSType_Type()
)
acSysTypeOSType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSysTypeOSType.setStatus("current")
_AcSysVersion_ObjectIdentity = ObjectIdentity
acSysVersion = _AcSysVersion_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 2, 2)
)


class _AcSysVersionSoftware_Type(SnmpAdminString):
    """Custom type acSysVersionSoftware based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_AcSysVersionSoftware_Type.__name__ = "SnmpAdminString"
_AcSysVersionSoftware_Object = MibScalar
acSysVersionSoftware = _AcSysVersionSoftware_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 2, 2, 1),
    _AcSysVersionSoftware_Type()
)
acSysVersionSoftware.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSysVersionSoftware.setStatus("current")


class _AcSysVersionFlash_Type(Unsigned32):
    """Custom type acSysVersionFlash based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AcSysVersionFlash_Type.__name__ = "Unsigned32"
_AcSysVersionFlash_Object = MibScalar
acSysVersionFlash = _AcSysVersionFlash_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 2, 2, 2),
    _AcSysVersionFlash_Type()
)
acSysVersionFlash.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSysVersionFlash.setStatus("current")


class _AcSysVersionIniFile_Type(Unsigned32):
    """Custom type acSysVersionIniFile based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AcSysVersionIniFile_Type.__name__ = "Unsigned32"
_AcSysVersionIniFile_Object = MibScalar
acSysVersionIniFile = _AcSysVersionIniFile_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 2, 2, 3),
    _AcSysVersionIniFile_Type()
)
acSysVersionIniFile.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSysVersionIniFile.setStatus("current")


class _AcSysVersionSoftwareDate_Type(SnmpAdminString):
    """Custom type acSysVersionSoftwareDate based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_AcSysVersionSoftwareDate_Type.__name__ = "SnmpAdminString"
_AcSysVersionSoftwareDate_Object = MibScalar
acSysVersionSoftwareDate = _AcSysVersionSoftwareDate_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 2, 2, 4),
    _AcSysVersionSoftwareDate_Type()
)
acSysVersionSoftwareDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSysVersionSoftwareDate.setStatus("current")
_AcSysId_ObjectIdentity = ObjectIdentity
acSysId = _AcSysId_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 2, 3)
)


class _AcSysIdName_Type(SnmpAdminString):
    """Custom type acSysIdName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_AcSysIdName_Type.__name__ = "SnmpAdminString"
_AcSysIdName_Object = MibScalar
acSysIdName = _AcSysIdName_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 2, 3, 1),
    _AcSysIdName_Type()
)
acSysIdName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSysIdName.setStatus("current")


class _AcSysIdSerialNumber_Type(Unsigned32):
    """Custom type acSysIdSerialNumber based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AcSysIdSerialNumber_Type.__name__ = "Unsigned32"
_AcSysIdSerialNumber_Object = MibScalar
acSysIdSerialNumber = _AcSysIdSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 2, 3, 2),
    _AcSysIdSerialNumber_Type()
)
acSysIdSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSysIdSerialNumber.setStatus("current")


class _AcSysIdSlotNumber_Type(Unsigned32):
    """Custom type acSysIdSlotNumber based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AcSysIdSlotNumber_Type.__name__ = "Unsigned32"
_AcSysIdSlotNumber_Object = MibScalar
acSysIdSlotNumber = _AcSysIdSlotNumber_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 2, 3, 3),
    _AcSysIdSlotNumber_Type()
)
acSysIdSlotNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSysIdSlotNumber.setStatus("current")


class _AcSysIdFirstSerialNumber_Type(Unsigned32):
    """Custom type acSysIdFirstSerialNumber based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AcSysIdFirstSerialNumber_Type.__name__ = "Unsigned32"
_AcSysIdFirstSerialNumber_Object = MibScalar
acSysIdFirstSerialNumber = _AcSysIdFirstSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 2, 3, 4),
    _AcSysIdFirstSerialNumber_Type()
)
acSysIdFirstSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSysIdFirstSerialNumber.setStatus("current")


class _AcSysIdSerialNumberString_Type(SnmpAdminString):
    """Custom type acSysIdSerialNumberString based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_AcSysIdSerialNumberString_Type.__name__ = "SnmpAdminString"
_AcSysIdSerialNumberString_Object = MibScalar
acSysIdSerialNumberString = _AcSysIdSerialNumberString_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 2, 3, 5),
    _AcSysIdSerialNumberString_Type()
)
acSysIdSerialNumberString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSysIdSerialNumberString.setStatus("current")


class _AcSysIdProductClass_Type(SnmpAdminString):
    """Custom type acSysIdProductClass based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_AcSysIdProductClass_Type.__name__ = "SnmpAdminString"
_AcSysIdProductClass_Object = MibScalar
acSysIdProductClass = _AcSysIdProductClass_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 2, 3, 6),
    _AcSysIdProductClass_Type()
)
acSysIdProductClass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSysIdProductClass.setStatus("current")


class _AcSysIdModelName_Type(SnmpAdminString):
    """Custom type acSysIdModelName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_AcSysIdModelName_Type.__name__ = "SnmpAdminString"
_AcSysIdModelName_Object = MibScalar
acSysIdModelName = _AcSysIdModelName_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 2, 3, 7),
    _AcSysIdModelName_Type()
)
acSysIdModelName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSysIdModelName.setStatus("current")
_AcSysCount_ObjectIdentity = ObjectIdentity
acSysCount = _AcSysCount_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 2, 4)
)


class _AcSysCountDSPs_Type(Unsigned32):
    """Custom type acSysCountDSPs based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AcSysCountDSPs_Type.__name__ = "Unsigned32"
_AcSysCountDSPs_Object = MibScalar
acSysCountDSPs = _AcSysCountDSPs_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 2, 4, 1),
    _AcSysCountDSPs_Type()
)
acSysCountDSPs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSysCountDSPs.setStatus("current")


class _AcSysCountChannels_Type(Unsigned32):
    """Custom type acSysCountChannels based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AcSysCountChannels_Type.__name__ = "Unsigned32"
_AcSysCountChannels_Object = MibScalar
acSysCountChannels = _AcSysCountChannels_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 2, 4, 2),
    _AcSysCountChannels_Type()
)
acSysCountChannels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSysCountChannels.setStatus("current")


class _AcSysCountTrunks_Type(Unsigned32):
    """Custom type acSysCountTrunks based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AcSysCountTrunks_Type.__name__ = "Unsigned32"
_AcSysCountTrunks_Object = MibScalar
acSysCountTrunks = _AcSysCountTrunks_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 2, 4, 3),
    _AcSysCountTrunks_Type()
)
acSysCountTrunks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSysCountTrunks.setStatus("current")
_AcSysState_ObjectIdentity = ObjectIdentity
acSysState = _AcSysState_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 2, 5)
)


class _AcSysStateTemperature_Type(Unsigned32):
    """Custom type acSysStateTemperature based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_AcSysStateTemperature_Type.__name__ = "Unsigned32"
_AcSysStateTemperature_Object = MibScalar
acSysStateTemperature = _AcSysStateTemperature_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 2, 5, 1),
    _AcSysStateTemperature_Type()
)
acSysStateTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSysStateTemperature.setStatus("current")


class _AcSysStateOperational_Type(Integer32):
    """Custom type acSysStateOperational based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_AcSysStateOperational_Type.__name__ = "Integer32"
_AcSysStateOperational_Object = MibScalar
acSysStateOperational = _AcSysStateOperational_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 2, 5, 2),
    _AcSysStateOperational_Type()
)
acSysStateOperational.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSysStateOperational.setStatus("current")


class _AcSysStateHAupdateInProgress_Type(Integer32):
    """Custom type acSysStateHAupdateInProgress based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("updateDone", 1),
          ("updateInProgress", 2))
    )


_AcSysStateHAupdateInProgress_Type.__name__ = "Integer32"
_AcSysStateHAupdateInProgress_Object = MibScalar
acSysStateHAupdateInProgress = _AcSysStateHAupdateInProgress_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 2, 5, 3),
    _AcSysStateHAupdateInProgress_Type()
)
acSysStateHAupdateInProgress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSysStateHAupdateInProgress.setStatus("current")


class _AcSysStateGWSeverity_Type(Integer32):
    """Custom type acSysStateGWSeverity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("noAlarm", 0),
          ("indeterminate", 1),
          ("warning", 2),
          ("minor", 3),
          ("major", 4),
          ("critical", 5))
    )


_AcSysStateGWSeverity_Type.__name__ = "Integer32"
_AcSysStateGWSeverity_Object = MibScalar
acSysStateGWSeverity = _AcSysStateGWSeverity_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 2, 5, 4),
    _AcSysStateGWSeverity_Type()
)
acSysStateGWSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSysStateGWSeverity.setStatus("current")


class _AcSysStateIsPstnManagementEnable_Type(Integer32):
    """Custom type acSysStateIsPstnManagementEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_AcSysStateIsPstnManagementEnable_Type.__name__ = "Integer32"
_AcSysStateIsPstnManagementEnable_Object = MibScalar
acSysStateIsPstnManagementEnable = _AcSysStateIsPstnManagementEnable_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 2, 5, 5),
    _AcSysStateIsPstnManagementEnable_Type()
)
acSysStateIsPstnManagementEnable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSysStateIsPstnManagementEnable.setStatus("current")


class _AcSysStateErrorMessage_Type(SnmpAdminString):
    """Custom type acSysStateErrorMessage based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 512),
    )


_AcSysStateErrorMessage_Type.__name__ = "SnmpAdminString"
_AcSysStateErrorMessage_Object = MibScalar
acSysStateErrorMessage = _AcSysStateErrorMessage_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 2, 5, 6),
    _AcSysStateErrorMessage_Type()
)
acSysStateErrorMessage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSysStateErrorMessage.setStatus("current")


class _AcSysStateErrorID_Type(Unsigned32):
    """Custom type acSysStateErrorID based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AcSysStateErrorID_Type.__name__ = "Unsigned32"
_AcSysStateErrorID_Object = MibScalar
acSysStateErrorID = _AcSysStateErrorID_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 2, 5, 7),
    _AcSysStateErrorID_Type()
)
acSysStateErrorID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acSysStateErrorID.setStatus("current")


class _AcSysStateDataCpuUtilization_Type(Unsigned32):
    """Custom type acSysStateDataCpuUtilization based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_AcSysStateDataCpuUtilization_Type.__name__ = "Unsigned32"
_AcSysStateDataCpuUtilization_Object = MibScalar
acSysStateDataCpuUtilization = _AcSysStateDataCpuUtilization_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 2, 5, 8),
    _AcSysStateDataCpuUtilization_Type()
)
acSysStateDataCpuUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSysStateDataCpuUtilization.setStatus("current")


class _AcSysStateDataMemoryUtilization_Type(Unsigned32):
    """Custom type acSysStateDataMemoryUtilization based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_AcSysStateDataMemoryUtilization_Type.__name__ = "Unsigned32"
_AcSysStateDataMemoryUtilization_Object = MibScalar
acSysStateDataMemoryUtilization = _AcSysStateDataMemoryUtilization_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 2, 5, 9),
    _AcSysStateDataMemoryUtilization_Type()
)
acSysStateDataMemoryUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSysStateDataMemoryUtilization.setStatus("current")


class _AcSysStateVoIpCpuUtilization_Type(Unsigned32):
    """Custom type acSysStateVoIpCpuUtilization based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_AcSysStateVoIpCpuUtilization_Type.__name__ = "Unsigned32"
_AcSysStateVoIpCpuUtilization_Object = MibScalar
acSysStateVoIpCpuUtilization = _AcSysStateVoIpCpuUtilization_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 2, 5, 10),
    _AcSysStateVoIpCpuUtilization_Type()
)
acSysStateVoIpCpuUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSysStateVoIpCpuUtilization.setStatus("current")


class _AcSysStateVoIpMemoryUtilization_Type(Unsigned32):
    """Custom type acSysStateVoIpMemoryUtilization based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_AcSysStateVoIpMemoryUtilization_Type.__name__ = "Unsigned32"
_AcSysStateVoIpMemoryUtilization_Object = MibScalar
acSysStateVoIpMemoryUtilization = _AcSysStateVoIpMemoryUtilization_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 2, 5, 11),
    _AcSysStateVoIpMemoryUtilization_Type()
)
acSysStateVoIpMemoryUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSysStateVoIpMemoryUtilization.setStatus("current")


class _AcSysStateManagedByEMS_Type(Integer32):
    """Custom type acSysStateManagedByEMS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enabled", 1))
    )


_AcSysStateManagedByEMS_Type.__name__ = "Integer32"
_AcSysStateManagedByEMS_Object = MibScalar
acSysStateManagedByEMS = _AcSysStateManagedByEMS_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 2, 5, 12),
    _AcSysStateManagedByEMS_Type()
)
acSysStateManagedByEMS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSysStateManagedByEMS.setStatus("current")


class _AcSysStateMonitoredBySEM_Type(Integer32):
    """Custom type acSysStateMonitoredBySEM based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enabled", 1))
    )


_AcSysStateMonitoredBySEM_Type.__name__ = "Integer32"
_AcSysStateMonitoredBySEM_Object = MibScalar
acSysStateMonitoredBySEM = _AcSysStateMonitoredBySEM_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 2, 5, 13),
    _AcSysStateMonitoredBySEM_Type()
)
acSysStateMonitoredBySEM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSysStateMonitoredBySEM.setStatus("current")


class _AcSysStateBurnFlag_Type(Integer32):
    """Custom type acSysStateBurnFlag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("burnFlagOFF", 0),
          ("burnFlagON", 1))
    )


_AcSysStateBurnFlag_Type.__name__ = "Integer32"
_AcSysStateBurnFlag_Object = MibScalar
acSysStateBurnFlag = _AcSysStateBurnFlag_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 2, 5, 14),
    _AcSysStateBurnFlag_Type()
)
acSysStateBurnFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSysStateBurnFlag.setStatus("current")


class _AcSysStateResetFlag_Type(Integer32):
    """Custom type acSysStateResetFlag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("resetFlagOFF", 0),
          ("resetFlagON", 1))
    )


_AcSysStateResetFlag_Type.__name__ = "Integer32"
_AcSysStateResetFlag_Object = MibScalar
acSysStateResetFlag = _AcSysStateResetFlag_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 2, 5, 15),
    _AcSysStateResetFlag_Type()
)
acSysStateResetFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSysStateResetFlag.setStatus("current")
_AcSysNetwork_ObjectIdentity = ObjectIdentity
acSysNetwork = _AcSysNetwork_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 2, 6)
)
_AcSysEthernet_ObjectIdentity = ObjectIdentity
acSysEthernet = _AcSysEthernet_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 2, 6, 1)
)


class _AcSysEthernetFirstPortDuplexMode_Type(Integer32):
    """Custom type acSysEthernetFirstPortDuplexMode based on Integer32"""
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
        *(("halfDuplex", 0),
          ("fullDuplex", 1),
          ("forceModeValue", 2),
          ("notAvailable", 3))
    )


_AcSysEthernetFirstPortDuplexMode_Type.__name__ = "Integer32"
_AcSysEthernetFirstPortDuplexMode_Object = MibScalar
acSysEthernetFirstPortDuplexMode = _AcSysEthernetFirstPortDuplexMode_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 2, 6, 1, 1),
    _AcSysEthernetFirstPortDuplexMode_Type()
)
acSysEthernetFirstPortDuplexMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSysEthernetFirstPortDuplexMode.setStatus("current")


class _AcSysEthernetFirstPortSpeed_Type(Integer32):
    """Custom type acSysEthernetFirstPortSpeed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              10,
              100,
              1000)
        )
    )
    namedValues = NamedValues(
        *(("forceModeValue", 2),
          ("notAvailable", 3),
          ("ac10Mbps", 10),
          ("ac100Mbps", 100),
          ("ac1000Mbps", 1000))
    )


_AcSysEthernetFirstPortSpeed_Type.__name__ = "Integer32"
_AcSysEthernetFirstPortSpeed_Object = MibScalar
acSysEthernetFirstPortSpeed = _AcSysEthernetFirstPortSpeed_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 2, 6, 1, 2),
    _AcSysEthernetFirstPortSpeed_Type()
)
acSysEthernetFirstPortSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSysEthernetFirstPortSpeed.setStatus("current")


class _AcSysEthernetSecondPortDuplexMode_Type(Integer32):
    """Custom type acSysEthernetSecondPortDuplexMode based on Integer32"""
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
        *(("halfDuplex", 0),
          ("fullDuplex", 1),
          ("forceModeValue", 2),
          ("notAvailable", 3))
    )


_AcSysEthernetSecondPortDuplexMode_Type.__name__ = "Integer32"
_AcSysEthernetSecondPortDuplexMode_Object = MibScalar
acSysEthernetSecondPortDuplexMode = _AcSysEthernetSecondPortDuplexMode_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 2, 6, 1, 3),
    _AcSysEthernetSecondPortDuplexMode_Type()
)
acSysEthernetSecondPortDuplexMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSysEthernetSecondPortDuplexMode.setStatus("current")


class _AcSysEthernetSecondPortSpeed_Type(Integer32):
    """Custom type acSysEthernetSecondPortSpeed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              10,
              100,
              1000)
        )
    )
    namedValues = NamedValues(
        *(("forceModeValue", 2),
          ("notAvailable", 3),
          ("ac10Mbps", 10),
          ("ac100Mbps", 100),
          ("ac1000Mbps", 1000))
    )


_AcSysEthernetSecondPortSpeed_Type.__name__ = "Integer32"
_AcSysEthernetSecondPortSpeed_Object = MibScalar
acSysEthernetSecondPortSpeed = _AcSysEthernetSecondPortSpeed_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 2, 6, 1, 4),
    _AcSysEthernetSecondPortSpeed_Type()
)
acSysEthernetSecondPortSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSysEthernetSecondPortSpeed.setStatus("current")


class _AcSysEthernetActivePortNumber_Type(Unsigned32):
    """Custom type acSysEthernetActivePortNumber based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_AcSysEthernetActivePortNumber_Type.__name__ = "Unsigned32"
_AcSysEthernetActivePortNumber_Object = MibScalar
acSysEthernetActivePortNumber = _AcSysEthernetActivePortNumber_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 2, 6, 1, 5),
    _AcSysEthernetActivePortNumber_Type()
)
acSysEthernetActivePortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSysEthernetActivePortNumber.setStatus("current")


class _AcSysEthernetPowerBudget_Type(Unsigned32):
    """Custom type acSysEthernetPowerBudget based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AcSysEthernetPowerBudget_Type.__name__ = "Unsigned32"
_AcSysEthernetPowerBudget_Object = MibScalar
acSysEthernetPowerBudget = _AcSysEthernetPowerBudget_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 2, 6, 1, 6),
    _AcSysEthernetPowerBudget_Type()
)
acSysEthernetPowerBudget.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSysEthernetPowerBudget.setStatus("current")


class _AcSysEthernetPowerAllocated_Type(Unsigned32):
    """Custom type acSysEthernetPowerAllocated based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AcSysEthernetPowerAllocated_Type.__name__ = "Unsigned32"
_AcSysEthernetPowerAllocated_Object = MibScalar
acSysEthernetPowerAllocated = _AcSysEthernetPowerAllocated_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 2, 6, 1, 7),
    _AcSysEthernetPowerAllocated_Type()
)
acSysEthernetPowerAllocated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSysEthernetPowerAllocated.setStatus("current")


class _AcSysEthernetPowerRemaining_Type(Unsigned32):
    """Custom type acSysEthernetPowerRemaining based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AcSysEthernetPowerRemaining_Type.__name__ = "Unsigned32"
_AcSysEthernetPowerRemaining_Object = MibScalar
acSysEthernetPowerRemaining = _AcSysEthernetPowerRemaining_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 2, 6, 1, 8),
    _AcSysEthernetPowerRemaining_Type()
)
acSysEthernetPowerRemaining.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSysEthernetPowerRemaining.setStatus("current")
_AcSysEthernetStatusTable_Object = MibTable
acSysEthernetStatusTable = _AcSysEthernetStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 2, 6, 1, 21)
)
if mibBuilder.loadTexts:
    acSysEthernetStatusTable.setStatus("current")
_AcSysEthernetStatusEntry_Object = MibTableRow
acSysEthernetStatusEntry = _AcSysEthernetStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 2, 6, 1, 21, 1)
)
acSysEthernetStatusEntry.setIndexNames(
    (0, "AC-SYSTEM-MIB", "acSysEthernetStatusIndex"),
)
if mibBuilder.loadTexts:
    acSysEthernetStatusEntry.setStatus("current")


class _AcSysEthernetStatusIndex_Type(Unsigned32):
    """Custom type acSysEthernetStatusIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 12),
    )


_AcSysEthernetStatusIndex_Type.__name__ = "Unsigned32"
_AcSysEthernetStatusIndex_Object = MibTableColumn
acSysEthernetStatusIndex = _AcSysEthernetStatusIndex_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 2, 6, 1, 21, 1, 1),
    _AcSysEthernetStatusIndex_Type()
)
acSysEthernetStatusIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    acSysEthernetStatusIndex.setStatus("current")


class _AcSysEthernetStatusPortDuplexMode_Type(Integer32):
    """Custom type acSysEthernetStatusPortDuplexMode based on Integer32"""
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
        *(("halfDuplex", 0),
          ("fullDuplex", 1),
          ("forceModeValue", 2),
          ("notAvailable", 3))
    )


_AcSysEthernetStatusPortDuplexMode_Type.__name__ = "Integer32"
_AcSysEthernetStatusPortDuplexMode_Object = MibTableColumn
acSysEthernetStatusPortDuplexMode = _AcSysEthernetStatusPortDuplexMode_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 2, 6, 1, 21, 1, 2),
    _AcSysEthernetStatusPortDuplexMode_Type()
)
acSysEthernetStatusPortDuplexMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSysEthernetStatusPortDuplexMode.setStatus("current")


class _AcSysEthernetStatusPortSpeed_Type(Integer32):
    """Custom type acSysEthernetStatusPortSpeed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              10,
              100,
              1000,
              10000)
        )
    )
    namedValues = NamedValues(
        *(("forceModeValue", 2),
          ("notAvailable", 3),
          ("ac10Mbps", 10),
          ("ac100Mbps", 100),
          ("ac1000Mbps", 1000),
          ("ac10Gbps", 10000))
    )


_AcSysEthernetStatusPortSpeed_Type.__name__ = "Integer32"
_AcSysEthernetStatusPortSpeed_Object = MibTableColumn
acSysEthernetStatusPortSpeed = _AcSysEthernetStatusPortSpeed_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 2, 6, 1, 21, 1, 3),
    _AcSysEthernetStatusPortSpeed_Type()
)
acSysEthernetStatusPortSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSysEthernetStatusPortSpeed.setStatus("current")


class _AcSysEthernetStatusActivePortNumber_Type(Integer32):
    """Custom type acSysEthernetStatusActivePortNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("notActive", 0),
          ("active", 1))
    )


_AcSysEthernetStatusActivePortNumber_Type.__name__ = "Integer32"
_AcSysEthernetStatusActivePortNumber_Object = MibTableColumn
acSysEthernetStatusActivePortNumber = _AcSysEthernetStatusActivePortNumber_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 2, 6, 1, 21, 1, 4),
    _AcSysEthernetStatusActivePortNumber_Type()
)
acSysEthernetStatusActivePortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSysEthernetStatusActivePortNumber.setStatus("current")


class _AcSysEthernetStatusPortState_Type(Integer32):
    """Custom type acSysEthernetStatusPortState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              10)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("blocking", 1),
          ("learning", 2),
          ("forwarding", 3),
          ("notApplicable", 10))
    )


_AcSysEthernetStatusPortState_Type.__name__ = "Integer32"
_AcSysEthernetStatusPortState_Object = MibTableColumn
acSysEthernetStatusPortState = _AcSysEthernetStatusPortState_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 2, 6, 1, 21, 1, 5),
    _AcSysEthernetStatusPortState_Type()
)
acSysEthernetStatusPortState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSysEthernetStatusPortState.setStatus("current")


class _AcSysEthernetStatusPowerOverEthernet_Type(Integer32):
    """Custom type acSysEthernetStatusPowerOverEthernet based on Integer32"""
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
        *(("notApplicable", 0),
          ("active", 1),
          ("notActive", 2),
          ("poeAlarm", 3))
    )


_AcSysEthernetStatusPowerOverEthernet_Type.__name__ = "Integer32"
_AcSysEthernetStatusPowerOverEthernet_Object = MibTableColumn
acSysEthernetStatusPowerOverEthernet = _AcSysEthernetStatusPowerOverEthernet_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 2, 6, 1, 21, 1, 6),
    _AcSysEthernetStatusPowerOverEthernet_Type()
)
acSysEthernetStatusPowerOverEthernet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSysEthernetStatusPowerOverEthernet.setStatus("current")


class _AcSysEthernetStatusAllocatedPower_Type(SnmpAdminString):
    """Custom type acSysEthernetStatusAllocatedPower based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_AcSysEthernetStatusAllocatedPower_Type.__name__ = "SnmpAdminString"
_AcSysEthernetStatusAllocatedPower_Object = MibTableColumn
acSysEthernetStatusAllocatedPower = _AcSysEthernetStatusAllocatedPower_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 2, 6, 1, 21, 1, 7),
    _AcSysEthernetStatusAllocatedPower_Type()
)
acSysEthernetStatusAllocatedPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSysEthernetStatusAllocatedPower.setStatus("current")


class _AcSysEthernetStatusGroup_Type(SnmpAdminString):
    """Custom type acSysEthernetStatusGroup based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_AcSysEthernetStatusGroup_Type.__name__ = "SnmpAdminString"
_AcSysEthernetStatusGroup_Object = MibTableColumn
acSysEthernetStatusGroup = _AcSysEthernetStatusGroup_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 2, 6, 1, 21, 1, 8),
    _AcSysEthernetStatusGroup_Type()
)
acSysEthernetStatusGroup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSysEthernetStatusGroup.setStatus("current")


class _AcSysEthernetStatusPowerOverEthernetDetails_Type(SnmpAdminString):
    """Custom type acSysEthernetStatusPowerOverEthernetDetails based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 100),
    )


_AcSysEthernetStatusPowerOverEthernetDetails_Type.__name__ = "SnmpAdminString"
_AcSysEthernetStatusPowerOverEthernetDetails_Object = MibTableColumn
acSysEthernetStatusPowerOverEthernetDetails = _AcSysEthernetStatusPowerOverEthernetDetails_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 2, 6, 1, 21, 1, 9),
    _AcSysEthernetStatusPowerOverEthernetDetails_Type()
)
acSysEthernetStatusPowerOverEthernetDetails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSysEthernetStatusPowerOverEthernetDetails.setStatus("current")


class _AcSysEthernetStatusPortType_Type(Integer32):
    """Custom type acSysEthernetStatusPortType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notApplicable", 0),
          ("gigabitEthernet", 1),
          ("fastEthernet", 2))
    )


_AcSysEthernetStatusPortType_Type.__name__ = "Integer32"
_AcSysEthernetStatusPortType_Object = MibTableColumn
acSysEthernetStatusPortType = _AcSysEthernetStatusPortType_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 2, 6, 1, 21, 1, 10),
    _AcSysEthernetStatusPortType_Type()
)
acSysEthernetStatusPortType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSysEthernetStatusPortType.setStatus("current")
_AcSysWanStatusTable_Object = MibTable
acSysWanStatusTable = _AcSysWanStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 2, 6, 1, 22)
)
if mibBuilder.loadTexts:
    acSysWanStatusTable.setStatus("current")
_AcSysWanStatusEntry_Object = MibTableRow
acSysWanStatusEntry = _AcSysWanStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 2, 6, 1, 22, 1)
)
acSysWanStatusEntry.setIndexNames(
    (0, "AC-SYSTEM-MIB", "acSysWanStatusIndex"),
)
if mibBuilder.loadTexts:
    acSysWanStatusEntry.setStatus("current")


class _AcSysWanStatusIndex_Type(Unsigned32):
    """Custom type acSysWanStatusIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_AcSysWanStatusIndex_Type.__name__ = "Unsigned32"
_AcSysWanStatusIndex_Object = MibTableColumn
acSysWanStatusIndex = _AcSysWanStatusIndex_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 2, 6, 1, 22, 1, 1),
    _AcSysWanStatusIndex_Type()
)
acSysWanStatusIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    acSysWanStatusIndex.setStatus("current")


class _AcSysWanStatusPortType_Type(Integer32):
    """Custom type acSysWanStatusPortType based on Integer32"""
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
        *(("ethernet", 0),
          ("t1", 1),
          ("sHDSL", 2),
          ("adslVdsl", 3),
          ("invalidPhyType", 4))
    )


_AcSysWanStatusPortType_Type.__name__ = "Integer32"
_AcSysWanStatusPortType_Object = MibTableColumn
acSysWanStatusPortType = _AcSysWanStatusPortType_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 2, 6, 1, 22, 1, 2),
    _AcSysWanStatusPortType_Type()
)
acSysWanStatusPortType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSysWanStatusPortType.setStatus("current")


class _AcSysWanStatusPortDuplexMode_Type(Integer32):
    """Custom type acSysWanStatusPortDuplexMode based on Integer32"""
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
        *(("halfDuplex", 0),
          ("fullDuplex", 1),
          ("forceModeValue", 2),
          ("notAvailable", 3))
    )


_AcSysWanStatusPortDuplexMode_Type.__name__ = "Integer32"
_AcSysWanStatusPortDuplexMode_Object = MibTableColumn
acSysWanStatusPortDuplexMode = _AcSysWanStatusPortDuplexMode_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 2, 6, 1, 22, 1, 3),
    _AcSysWanStatusPortDuplexMode_Type()
)
acSysWanStatusPortDuplexMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSysWanStatusPortDuplexMode.setStatus("current")


class _AcSysWanStatusPortSpeed_Type(Integer32):
    """Custom type acSysWanStatusPortSpeed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              10,
              100,
              1000)
        )
    )
    namedValues = NamedValues(
        *(("forceModeValue", 2),
          ("notAvailable", 3),
          ("ac10Mbps", 10),
          ("ac100Mbps", 100),
          ("ac1000Mbps", 1000))
    )


_AcSysWanStatusPortSpeed_Type.__name__ = "Integer32"
_AcSysWanStatusPortSpeed_Object = MibTableColumn
acSysWanStatusPortSpeed = _AcSysWanStatusPortSpeed_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 2, 6, 1, 22, 1, 4),
    _AcSysWanStatusPortSpeed_Type()
)
acSysWanStatusPortSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSysWanStatusPortSpeed.setStatus("current")


class _AcSysWanStatusActivePortNumber_Type(Integer32):
    """Custom type acSysWanStatusActivePortNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("notActive", 0),
          ("active", 1))
    )


_AcSysWanStatusActivePortNumber_Type.__name__ = "Integer32"
_AcSysWanStatusActivePortNumber_Object = MibTableColumn
acSysWanStatusActivePortNumber = _AcSysWanStatusActivePortNumber_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 2, 6, 1, 22, 1, 5),
    _AcSysWanStatusActivePortNumber_Type()
)
acSysWanStatusActivePortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSysWanStatusActivePortNumber.setStatus("current")


class _AcSysWanStatusPortState_Type(Integer32):
    """Custom type acSysWanStatusPortState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              10)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("blocking", 1),
          ("learning", 2),
          ("forwarding", 3),
          ("notApplicable", 10))
    )


_AcSysWanStatusPortState_Type.__name__ = "Integer32"
_AcSysWanStatusPortState_Object = MibTableColumn
acSysWanStatusPortState = _AcSysWanStatusPortState_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 2, 6, 1, 22, 1, 6),
    _AcSysWanStatusPortState_Type()
)
acSysWanStatusPortState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSysWanStatusPortState.setStatus("current")


class _AcSysWanStatusPowerOverEthernet_Type(Integer32):
    """Custom type acSysWanStatusPowerOverEthernet based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notApplicable", 0),
          ("active", 1),
          ("notActive", 2))
    )


_AcSysWanStatusPowerOverEthernet_Type.__name__ = "Integer32"
_AcSysWanStatusPowerOverEthernet_Object = MibTableColumn
acSysWanStatusPowerOverEthernet = _AcSysWanStatusPowerOverEthernet_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 2, 6, 1, 22, 1, 7),
    _AcSysWanStatusPowerOverEthernet_Type()
)
acSysWanStatusPowerOverEthernet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSysWanStatusPowerOverEthernet.setStatus("current")
_AcSysEthernetRedundantStatusTable_Object = MibTable
acSysEthernetRedundantStatusTable = _AcSysEthernetRedundantStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 2, 6, 1, 23)
)
if mibBuilder.loadTexts:
    acSysEthernetRedundantStatusTable.setStatus("current")
_AcSysEthernetRedundantStatusEntry_Object = MibTableRow
acSysEthernetRedundantStatusEntry = _AcSysEthernetRedundantStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 2, 6, 1, 23, 1)
)
acSysEthernetRedundantStatusEntry.setIndexNames(
    (0, "AC-SYSTEM-MIB", "acSysEthernetRedundantStatusIndex"),
)
if mibBuilder.loadTexts:
    acSysEthernetRedundantStatusEntry.setStatus("current")


class _AcSysEthernetRedundantStatusIndex_Type(Unsigned32):
    """Custom type acSysEthernetRedundantStatusIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 12),
    )


_AcSysEthernetRedundantStatusIndex_Type.__name__ = "Unsigned32"
_AcSysEthernetRedundantStatusIndex_Object = MibTableColumn
acSysEthernetRedundantStatusIndex = _AcSysEthernetRedundantStatusIndex_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 2, 6, 1, 23, 1, 1),
    _AcSysEthernetRedundantStatusIndex_Type()
)
acSysEthernetRedundantStatusIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    acSysEthernetRedundantStatusIndex.setStatus("current")


class _AcSysEthernetRedundantStatusPortDuplexMode_Type(Integer32):
    """Custom type acSysEthernetRedundantStatusPortDuplexMode based on Integer32"""
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
        *(("halfDuplex", 0),
          ("fullDuplex", 1),
          ("forceModeValue", 2),
          ("notAvailable", 3))
    )


_AcSysEthernetRedundantStatusPortDuplexMode_Type.__name__ = "Integer32"
_AcSysEthernetRedundantStatusPortDuplexMode_Object = MibTableColumn
acSysEthernetRedundantStatusPortDuplexMode = _AcSysEthernetRedundantStatusPortDuplexMode_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 2, 6, 1, 23, 1, 2),
    _AcSysEthernetRedundantStatusPortDuplexMode_Type()
)
acSysEthernetRedundantStatusPortDuplexMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSysEthernetRedundantStatusPortDuplexMode.setStatus("current")


class _AcSysEthernetRedundantStatusPortSpeed_Type(Integer32):
    """Custom type acSysEthernetRedundantStatusPortSpeed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              10,
              100,
              1000)
        )
    )
    namedValues = NamedValues(
        *(("forceModeValue", 2),
          ("notAvailable", 3),
          ("ac10Mbps", 10),
          ("ac100Mbps", 100),
          ("ac1000Mbps", 1000))
    )


_AcSysEthernetRedundantStatusPortSpeed_Type.__name__ = "Integer32"
_AcSysEthernetRedundantStatusPortSpeed_Object = MibTableColumn
acSysEthernetRedundantStatusPortSpeed = _AcSysEthernetRedundantStatusPortSpeed_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 2, 6, 1, 23, 1, 3),
    _AcSysEthernetRedundantStatusPortSpeed_Type()
)
acSysEthernetRedundantStatusPortSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSysEthernetRedundantStatusPortSpeed.setStatus("current")


class _AcSysEthernetRedundantStatusActivePortNumber_Type(Integer32):
    """Custom type acSysEthernetRedundantStatusActivePortNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("notActive", 0),
          ("active", 1))
    )


_AcSysEthernetRedundantStatusActivePortNumber_Type.__name__ = "Integer32"
_AcSysEthernetRedundantStatusActivePortNumber_Object = MibTableColumn
acSysEthernetRedundantStatusActivePortNumber = _AcSysEthernetRedundantStatusActivePortNumber_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 2, 6, 1, 23, 1, 4),
    _AcSysEthernetRedundantStatusActivePortNumber_Type()
)
acSysEthernetRedundantStatusActivePortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSysEthernetRedundantStatusActivePortNumber.setStatus("current")


class _AcSysEthernetRedundantStatusPortState_Type(Integer32):
    """Custom type acSysEthernetRedundantStatusPortState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              10)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("blocking", 1),
          ("learning", 2),
          ("forwarding", 3),
          ("notApplicable", 10))
    )


_AcSysEthernetRedundantStatusPortState_Type.__name__ = "Integer32"
_AcSysEthernetRedundantStatusPortState_Object = MibTableColumn
acSysEthernetRedundantStatusPortState = _AcSysEthernetRedundantStatusPortState_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 2, 6, 1, 23, 1, 5),
    _AcSysEthernetRedundantStatusPortState_Type()
)
acSysEthernetRedundantStatusPortState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSysEthernetRedundantStatusPortState.setStatus("current")


class _AcSysEthernetRedundantStatusPowerOverEthernet_Type(Integer32):
    """Custom type acSysEthernetRedundantStatusPowerOverEthernet based on Integer32"""
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
        *(("notApplicable", 0),
          ("active", 1),
          ("notActive", 2),
          ("poeAlarm", 3))
    )


_AcSysEthernetRedundantStatusPowerOverEthernet_Type.__name__ = "Integer32"
_AcSysEthernetRedundantStatusPowerOverEthernet_Object = MibTableColumn
acSysEthernetRedundantStatusPowerOverEthernet = _AcSysEthernetRedundantStatusPowerOverEthernet_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 2, 6, 1, 23, 1, 6),
    _AcSysEthernetRedundantStatusPowerOverEthernet_Type()
)
acSysEthernetRedundantStatusPowerOverEthernet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSysEthernetRedundantStatusPowerOverEthernet.setStatus("current")


class _AcSysEthernetRedundantStatusAllocatedPower_Type(SnmpAdminString):
    """Custom type acSysEthernetRedundantStatusAllocatedPower based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_AcSysEthernetRedundantStatusAllocatedPower_Type.__name__ = "SnmpAdminString"
_AcSysEthernetRedundantStatusAllocatedPower_Object = MibTableColumn
acSysEthernetRedundantStatusAllocatedPower = _AcSysEthernetRedundantStatusAllocatedPower_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 2, 6, 1, 23, 1, 7),
    _AcSysEthernetRedundantStatusAllocatedPower_Type()
)
acSysEthernetRedundantStatusAllocatedPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSysEthernetRedundantStatusAllocatedPower.setStatus("current")


class _AcSysEthernetRedundantStatusGroup_Type(SnmpAdminString):
    """Custom type acSysEthernetRedundantStatusGroup based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_AcSysEthernetRedundantStatusGroup_Type.__name__ = "SnmpAdminString"
_AcSysEthernetRedundantStatusGroup_Object = MibTableColumn
acSysEthernetRedundantStatusGroup = _AcSysEthernetRedundantStatusGroup_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 2, 6, 1, 23, 1, 8),
    _AcSysEthernetRedundantStatusGroup_Type()
)
acSysEthernetRedundantStatusGroup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSysEthernetRedundantStatusGroup.setStatus("current")


class _AcSysEthernetRedundantStatusPowerOverEthernetDetails_Type(SnmpAdminString):
    """Custom type acSysEthernetRedundantStatusPowerOverEthernetDetails based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 100),
    )


_AcSysEthernetRedundantStatusPowerOverEthernetDetails_Type.__name__ = "SnmpAdminString"
_AcSysEthernetRedundantStatusPowerOverEthernetDetails_Object = MibTableColumn
acSysEthernetRedundantStatusPowerOverEthernetDetails = _AcSysEthernetRedundantStatusPowerOverEthernetDetails_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 2, 6, 1, 23, 1, 9),
    _AcSysEthernetRedundantStatusPowerOverEthernetDetails_Type()
)
acSysEthernetRedundantStatusPowerOverEthernetDetails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSysEthernetRedundantStatusPowerOverEthernetDetails.setStatus("current")
_AcSysMultiWanStatusTable_Object = MibTable
acSysMultiWanStatusTable = _AcSysMultiWanStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 2, 6, 1, 24)
)
if mibBuilder.loadTexts:
    acSysMultiWanStatusTable.setStatus("current")
_AcSysMultiWanStatusEntry_Object = MibTableRow
acSysMultiWanStatusEntry = _AcSysMultiWanStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 2, 6, 1, 24, 1)
)
acSysMultiWanStatusEntry.setIndexNames(
    (0, "AC-SYSTEM-MIB", "acSysMultiWanStatusSite"),
    (0, "AC-SYSTEM-MIB", "acSysMultiWanStatusPort"),
)
if mibBuilder.loadTexts:
    acSysMultiWanStatusEntry.setStatus("current")


class _AcSysMultiWanStatusSite_Type(Unsigned32):
    """Custom type acSysMultiWanStatusSite based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4),
    )


_AcSysMultiWanStatusSite_Type.__name__ = "Unsigned32"
_AcSysMultiWanStatusSite_Object = MibTableColumn
acSysMultiWanStatusSite = _AcSysMultiWanStatusSite_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 2, 6, 1, 24, 1, 1),
    _AcSysMultiWanStatusSite_Type()
)
acSysMultiWanStatusSite.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    acSysMultiWanStatusSite.setStatus("current")


class _AcSysMultiWanStatusPort_Type(Unsigned32):
    """Custom type acSysMultiWanStatusPort based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_AcSysMultiWanStatusPort_Type.__name__ = "Unsigned32"
_AcSysMultiWanStatusPort_Object = MibTableColumn
acSysMultiWanStatusPort = _AcSysMultiWanStatusPort_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 2, 6, 1, 24, 1, 2),
    _AcSysMultiWanStatusPort_Type()
)
acSysMultiWanStatusPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    acSysMultiWanStatusPort.setStatus("current")


class _AcSysMultiWanStatusType_Type(Integer32):
    """Custom type acSysMultiWanStatusType based on Integer32"""
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
        *(("ethernet", 0),
          ("t1", 1),
          ("e1", 2),
          ("sHDSL", 3),
          ("adslVdsl", 4),
          ("gPON", 5),
          ("geSFP", 6),
          ("invalidPhyType", 7))
    )


_AcSysMultiWanStatusType_Type.__name__ = "Integer32"
_AcSysMultiWanStatusType_Object = MibTableColumn
acSysMultiWanStatusType = _AcSysMultiWanStatusType_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 2, 6, 1, 24, 1, 3),
    _AcSysMultiWanStatusType_Type()
)
acSysMultiWanStatusType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSysMultiWanStatusType.setStatus("current")


class _AcSysMultiWanStatusStatus_Type(Integer32):
    """Custom type acSysMultiWanStatusStatus based on Integer32"""
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
        *(("inactive", 0),
          ("working", 1),
          ("process", 2),
          ("unknown", 3))
    )


_AcSysMultiWanStatusStatus_Type.__name__ = "Integer32"
_AcSysMultiWanStatusStatus_Object = MibTableColumn
acSysMultiWanStatusStatus = _AcSysMultiWanStatusStatus_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 2, 6, 1, 24, 1, 4),
    _AcSysMultiWanStatusStatus_Type()
)
acSysMultiWanStatusStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSysMultiWanStatusStatus.setStatus("current")
_AcSysNAT_ObjectIdentity = ObjectIdentity
acSysNAT = _AcSysNAT_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 2, 6, 2)
)


class _AcSysNATType_Type(Integer32):
    """Custom type acSysNATType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              10)
        )
    )
    namedValues = NamedValues(
        *(("stunDisabled", -1),
          ("none", 0),
          ("fullCone", 1),
          ("restricted", 2),
          ("portRestricted", 3),
          ("symmetric", 4),
          ("symmetricFireWall", 5),
          ("blocked", 6),
          ("unknown", 7),
          ("natIdentificationInProgress", 10))
    )


_AcSysNATType_Type.__name__ = "Integer32"
_AcSysNATType_Object = MibScalar
acSysNATType = _AcSysNATType_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 2, 6, 2, 1),
    _AcSysNATType_Type()
)
acSysNATType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSysNATType.setStatus("current")
_AcSysWebStat_ObjectIdentity = ObjectIdentity
acSysWebStat = _AcSysWebStat_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 2, 6, 3)
)


class _AcSysWebStatPasswordControlViaSNMP_Type(Integer32):
    """Custom type acSysWebStatPasswordControlViaSNMP based on Integer32"""
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


_AcSysWebStatPasswordControlViaSNMP_Type.__name__ = "Integer32"
_AcSysWebStatPasswordControlViaSNMP_Object = MibScalar
acSysWebStatPasswordControlViaSNMP = _AcSysWebStatPasswordControlViaSNMP_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 2, 6, 3, 1),
    _AcSysWebStatPasswordControlViaSNMP_Type()
)
acSysWebStatPasswordControlViaSNMP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSysWebStatPasswordControlViaSNMP.setStatus("current")
_AcSysIPStatus_ObjectIdentity = ObjectIdentity
acSysIPStatus = _AcSysIPStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 2, 6, 4)
)
_AcSysInterfaceStatusTable_Object = MibTable
acSysInterfaceStatusTable = _AcSysInterfaceStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 2, 6, 4, 21)
)
if mibBuilder.loadTexts:
    acSysInterfaceStatusTable.setStatus("current")
_AcSysInterfaceStatusEntry_Object = MibTableRow
acSysInterfaceStatusEntry = _AcSysInterfaceStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 2, 6, 4, 21, 1)
)
acSysInterfaceStatusEntry.setIndexNames(
    (0, "AC-SYSTEM-MIB", "acSysInterfaceStatusEntryIndex"),
    (0, "AC-SYSTEM-MIB", "acSysInterfaceStatusTypeIndex"),
)
if mibBuilder.loadTexts:
    acSysInterfaceStatusEntry.setStatus("current")


class _AcSysInterfaceStatusEntryIndex_Type(Unsigned32):
    """Custom type acSysInterfaceStatusEntryIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 47),
    )


_AcSysInterfaceStatusEntryIndex_Type.__name__ = "Unsigned32"
_AcSysInterfaceStatusEntryIndex_Object = MibTableColumn
acSysInterfaceStatusEntryIndex = _AcSysInterfaceStatusEntryIndex_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 2, 6, 4, 21, 1, 1),
    _AcSysInterfaceStatusEntryIndex_Type()
)
acSysInterfaceStatusEntryIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    acSysInterfaceStatusEntryIndex.setStatus("current")


class _AcSysInterfaceStatusTypeIndex_Type(Unsigned32):
    """Custom type acSysInterfaceStatusTypeIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_AcSysInterfaceStatusTypeIndex_Type.__name__ = "Unsigned32"
_AcSysInterfaceStatusTypeIndex_Object = MibTableColumn
acSysInterfaceStatusTypeIndex = _AcSysInterfaceStatusTypeIndex_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 2, 6, 4, 21, 1, 2),
    _AcSysInterfaceStatusTypeIndex_Type()
)
acSysInterfaceStatusTypeIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    acSysInterfaceStatusTypeIndex.setStatus("current")


class _AcSysInterfaceStatusApplicationTypes_Type(Integer32):
    """Custom type acSysInterfaceStatusApplicationTypes based on Integer32"""
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
              11,
              99,
              100)
        )
    )
    namedValues = NamedValues(
        *(("oam", 0),
          ("media", 1),
          ("control", 2),
          ("oamAndMedia", 3),
          ("oamAndControl", 4),
          ("mediaAndControl", 5),
          ("oamAndMediaAndControl", 6),
          ("data", 11),
          ("maintenance", 99),
          ("internal", 100))
    )


_AcSysInterfaceStatusApplicationTypes_Type.__name__ = "Integer32"
_AcSysInterfaceStatusApplicationTypes_Object = MibTableColumn
acSysInterfaceStatusApplicationTypes = _AcSysInterfaceStatusApplicationTypes_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 2, 6, 4, 21, 1, 3),
    _AcSysInterfaceStatusApplicationTypes_Type()
)
acSysInterfaceStatusApplicationTypes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSysInterfaceStatusApplicationTypes.setStatus("current")


class _AcSysInterfaceStatusMode_Type(Integer32):
    """Custom type acSysInterfaceStatusMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(3,
              4,
              10)
        )
    )
    namedValues = NamedValues(
        *(("iPv6PrefixManual", 3),
          ("iPv6Manual", 4),
          ("iPv4Manual", 10))
    )


_AcSysInterfaceStatusMode_Type.__name__ = "Integer32"
_AcSysInterfaceStatusMode_Object = MibTableColumn
acSysInterfaceStatusMode = _AcSysInterfaceStatusMode_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 2, 6, 4, 21, 1, 4),
    _AcSysInterfaceStatusMode_Type()
)
acSysInterfaceStatusMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSysInterfaceStatusMode.setStatus("current")


class _AcSysInterfaceStatusIPAddress_Type(SnmpAdminString):
    """Custom type acSysInterfaceStatusIPAddress based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 45),
    )


_AcSysInterfaceStatusIPAddress_Type.__name__ = "SnmpAdminString"
_AcSysInterfaceStatusIPAddress_Object = MibTableColumn
acSysInterfaceStatusIPAddress = _AcSysInterfaceStatusIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 2, 6, 4, 21, 1, 5),
    _AcSysInterfaceStatusIPAddress_Type()
)
acSysInterfaceStatusIPAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSysInterfaceStatusIPAddress.setStatus("current")


class _AcSysInterfaceStatusPrefixLength_Type(Unsigned32):
    """Custom type acSysInterfaceStatusPrefixLength based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_AcSysInterfaceStatusPrefixLength_Type.__name__ = "Unsigned32"
_AcSysInterfaceStatusPrefixLength_Object = MibTableColumn
acSysInterfaceStatusPrefixLength = _AcSysInterfaceStatusPrefixLength_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 2, 6, 4, 21, 1, 6),
    _AcSysInterfaceStatusPrefixLength_Type()
)
acSysInterfaceStatusPrefixLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSysInterfaceStatusPrefixLength.setStatus("current")


class _AcSysInterfaceStatusGateway_Type(SnmpAdminString):
    """Custom type acSysInterfaceStatusGateway based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 45),
    )


_AcSysInterfaceStatusGateway_Type.__name__ = "SnmpAdminString"
_AcSysInterfaceStatusGateway_Object = MibTableColumn
acSysInterfaceStatusGateway = _AcSysInterfaceStatusGateway_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 2, 6, 4, 21, 1, 7),
    _AcSysInterfaceStatusGateway_Type()
)
acSysInterfaceStatusGateway.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSysInterfaceStatusGateway.setStatus("current")


class _AcSysInterfaceStatusVlanID_Type(Integer32):
    """Custom type acSysInterfaceStatusVlanID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 4094),
    )


_AcSysInterfaceStatusVlanID_Type.__name__ = "Integer32"
_AcSysInterfaceStatusVlanID_Object = MibTableColumn
acSysInterfaceStatusVlanID = _AcSysInterfaceStatusVlanID_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 2, 6, 4, 21, 1, 8),
    _AcSysInterfaceStatusVlanID_Type()
)
acSysInterfaceStatusVlanID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSysInterfaceStatusVlanID.setStatus("current")


class _AcSysInterfaceStatusName_Type(SnmpAdminString):
    """Custom type acSysInterfaceStatusName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_AcSysInterfaceStatusName_Type.__name__ = "SnmpAdminString"
_AcSysInterfaceStatusName_Object = MibTableColumn
acSysInterfaceStatusName = _AcSysInterfaceStatusName_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 2, 6, 4, 21, 1, 9),
    _AcSysInterfaceStatusName_Type()
)
acSysInterfaceStatusName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSysInterfaceStatusName.setStatus("current")


class _AcSysInterfaceStatusRelatedIndex_Type(Integer32):
    """Custom type acSysInterfaceStatusRelatedIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 47),
    )


_AcSysInterfaceStatusRelatedIndex_Type.__name__ = "Integer32"
_AcSysInterfaceStatusRelatedIndex_Object = MibTableColumn
acSysInterfaceStatusRelatedIndex = _AcSysInterfaceStatusRelatedIndex_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 2, 6, 4, 21, 1, 10),
    _AcSysInterfaceStatusRelatedIndex_Type()
)
acSysInterfaceStatusRelatedIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSysInterfaceStatusRelatedIndex.setStatus("current")


class _AcSysInterfaceStatusPrimaryDNSServerIPAddress_Type(SnmpAdminString):
    """Custom type acSysInterfaceStatusPrimaryDNSServerIPAddress based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 45),
    )


_AcSysInterfaceStatusPrimaryDNSServerIPAddress_Type.__name__ = "SnmpAdminString"
_AcSysInterfaceStatusPrimaryDNSServerIPAddress_Object = MibTableColumn
acSysInterfaceStatusPrimaryDNSServerIPAddress = _AcSysInterfaceStatusPrimaryDNSServerIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 2, 6, 4, 21, 1, 11),
    _AcSysInterfaceStatusPrimaryDNSServerIPAddress_Type()
)
acSysInterfaceStatusPrimaryDNSServerIPAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSysInterfaceStatusPrimaryDNSServerIPAddress.setStatus("current")


class _AcSysInterfaceStatusSecondaryDNSServerIPAddress_Type(SnmpAdminString):
    """Custom type acSysInterfaceStatusSecondaryDNSServerIPAddress based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 45),
    )


_AcSysInterfaceStatusSecondaryDNSServerIPAddress_Type.__name__ = "SnmpAdminString"
_AcSysInterfaceStatusSecondaryDNSServerIPAddress_Object = MibTableColumn
acSysInterfaceStatusSecondaryDNSServerIPAddress = _AcSysInterfaceStatusSecondaryDNSServerIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 2, 6, 4, 21, 1, 12),
    _AcSysInterfaceStatusSecondaryDNSServerIPAddress_Type()
)
acSysInterfaceStatusSecondaryDNSServerIPAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSysInterfaceStatusSecondaryDNSServerIPAddress.setStatus("current")


class _AcSysInterfaceStatusUnderlyingDevice_Type(SnmpAdminString):
    """Custom type acSysInterfaceStatusUnderlyingDevice based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 17),
    )


_AcSysInterfaceStatusUnderlyingDevice_Type.__name__ = "SnmpAdminString"
_AcSysInterfaceStatusUnderlyingDevice_Object = MibTableColumn
acSysInterfaceStatusUnderlyingDevice = _AcSysInterfaceStatusUnderlyingDevice_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 2, 6, 4, 21, 1, 13),
    _AcSysInterfaceStatusUnderlyingDevice_Type()
)
acSysInterfaceStatusUnderlyingDevice.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSysInterfaceStatusUnderlyingDevice.setStatus("current")
_AcSysDataInterfaceStatusTable_Object = MibTable
acSysDataInterfaceStatusTable = _AcSysDataInterfaceStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 2, 6, 4, 22)
)
if mibBuilder.loadTexts:
    acSysDataInterfaceStatusTable.setStatus("current")
_AcSysDataInterfaceStatusEntry_Object = MibTableRow
acSysDataInterfaceStatusEntry = _AcSysDataInterfaceStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 2, 6, 4, 22, 1)
)
acSysDataInterfaceStatusEntry.setIndexNames(
    (0, "AC-SYSTEM-MIB", "acSysDataInterfaceStatusIndex"),
)
if mibBuilder.loadTexts:
    acSysDataInterfaceStatusEntry.setStatus("current")


class _AcSysDataInterfaceStatusIndex_Type(Unsigned32):
    """Custom type acSysDataInterfaceStatusIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 69),
    )


_AcSysDataInterfaceStatusIndex_Type.__name__ = "Unsigned32"
_AcSysDataInterfaceStatusIndex_Object = MibTableColumn
acSysDataInterfaceStatusIndex = _AcSysDataInterfaceStatusIndex_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 2, 6, 4, 22, 1, 1),
    _AcSysDataInterfaceStatusIndex_Type()
)
acSysDataInterfaceStatusIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    acSysDataInterfaceStatusIndex.setStatus("current")


class _AcSysDataInterfaceStatusName_Type(SnmpAdminString):
    """Custom type acSysDataInterfaceStatusName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 70),
    )


_AcSysDataInterfaceStatusName_Type.__name__ = "SnmpAdminString"
_AcSysDataInterfaceStatusName_Object = MibTableColumn
acSysDataInterfaceStatusName = _AcSysDataInterfaceStatusName_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 2, 6, 4, 22, 1, 2),
    _AcSysDataInterfaceStatusName_Type()
)
acSysDataInterfaceStatusName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSysDataInterfaceStatusName.setStatus("current")


class _AcSysDataInterfaceStatusIPAddress_Type(SnmpAdminString):
    """Custom type acSysDataInterfaceStatusIPAddress based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 45),
    )


_AcSysDataInterfaceStatusIPAddress_Type.__name__ = "SnmpAdminString"
_AcSysDataInterfaceStatusIPAddress_Object = MibTableColumn
acSysDataInterfaceStatusIPAddress = _AcSysDataInterfaceStatusIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 2, 6, 4, 22, 1, 3),
    _AcSysDataInterfaceStatusIPAddress_Type()
)
acSysDataInterfaceStatusIPAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSysDataInterfaceStatusIPAddress.setStatus("current")


class _AcSysDataInterfaceStatusNetmask_Type(SnmpAdminString):
    """Custom type acSysDataInterfaceStatusNetmask based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 45),
    )


_AcSysDataInterfaceStatusNetmask_Type.__name__ = "SnmpAdminString"
_AcSysDataInterfaceStatusNetmask_Object = MibTableColumn
acSysDataInterfaceStatusNetmask = _AcSysDataInterfaceStatusNetmask_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 2, 6, 4, 22, 1, 4),
    _AcSysDataInterfaceStatusNetmask_Type()
)
acSysDataInterfaceStatusNetmask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSysDataInterfaceStatusNetmask.setStatus("current")


class _AcSysDataInterfaceStatusInfo_Type(SnmpAdminString):
    """Custom type acSysDataInterfaceStatusInfo based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 30),
    )


_AcSysDataInterfaceStatusInfo_Type.__name__ = "SnmpAdminString"
_AcSysDataInterfaceStatusInfo_Object = MibTableColumn
acSysDataInterfaceStatusInfo = _AcSysDataInterfaceStatusInfo_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 2, 6, 4, 22, 1, 5),
    _AcSysDataInterfaceStatusInfo_Type()
)
acSysDataInterfaceStatusInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSysDataInterfaceStatusInfo.setStatus("current")


class _AcSysDataInterfaceStatusDescription_Type(SnmpAdminString):
    """Custom type acSysDataInterfaceStatusDescription based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 30),
    )


_AcSysDataInterfaceStatusDescription_Type.__name__ = "SnmpAdminString"
_AcSysDataInterfaceStatusDescription_Object = MibTableColumn
acSysDataInterfaceStatusDescription = _AcSysDataInterfaceStatusDescription_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 2, 6, 4, 22, 1, 6),
    _AcSysDataInterfaceStatusDescription_Type()
)
acSysDataInterfaceStatusDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSysDataInterfaceStatusDescription.setStatus("current")


class _AcSysDataInterfaceStatusOperationalState_Type(Integer32):
    """Custom type acSysDataInterfaceStatusOperationalState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("down", 0),
          ("up", 1))
    )


_AcSysDataInterfaceStatusOperationalState_Type.__name__ = "Integer32"
_AcSysDataInterfaceStatusOperationalState_Object = MibTableColumn
acSysDataInterfaceStatusOperationalState = _AcSysDataInterfaceStatusOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 2, 6, 4, 22, 1, 7),
    _AcSysDataInterfaceStatusOperationalState_Type()
)
acSysDataInterfaceStatusOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSysDataInterfaceStatusOperationalState.setStatus("current")


class _AcSysDataInterfaceStatusStateTime_Type(SnmpAdminString):
    """Custom type acSysDataInterfaceStatusStateTime based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 9),
    )


_AcSysDataInterfaceStatusStateTime_Type.__name__ = "SnmpAdminString"
_AcSysDataInterfaceStatusStateTime_Object = MibTableColumn
acSysDataInterfaceStatusStateTime = _AcSysDataInterfaceStatusStateTime_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 2, 6, 4, 22, 1, 8),
    _AcSysDataInterfaceStatusStateTime_Type()
)
acSysDataInterfaceStatusStateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSysDataInterfaceStatusStateTime.setStatus("current")


class _AcSysDataInterfaceStatusUptime_Type(SnmpAdminString):
    """Custom type acSysDataInterfaceStatusUptime based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 9),
    )


_AcSysDataInterfaceStatusUptime_Type.__name__ = "SnmpAdminString"
_AcSysDataInterfaceStatusUptime_Object = MibTableColumn
acSysDataInterfaceStatusUptime = _AcSysDataInterfaceStatusUptime_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 2, 6, 4, 22, 1, 9),
    _AcSysDataInterfaceStatusUptime_Type()
)
acSysDataInterfaceStatusUptime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSysDataInterfaceStatusUptime.setStatus("current")


class _AcSysDataInterfaceStatusMtuMode_Type(SnmpAdminString):
    """Custom type acSysDataInterfaceStatusMtuMode based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_AcSysDataInterfaceStatusMtuMode_Type.__name__ = "SnmpAdminString"
_AcSysDataInterfaceStatusMtuMode_Object = MibTableColumn
acSysDataInterfaceStatusMtuMode = _AcSysDataInterfaceStatusMtuMode_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 2, 6, 4, 22, 1, 10),
    _AcSysDataInterfaceStatusMtuMode_Type()
)
acSysDataInterfaceStatusMtuMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSysDataInterfaceStatusMtuMode.setStatus("current")


class _AcSysDataInterfaceStatusDnsStatus_Type(SnmpAdminString):
    """Custom type acSysDataInterfaceStatusDnsStatus based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_AcSysDataInterfaceStatusDnsStatus_Type.__name__ = "SnmpAdminString"
_AcSysDataInterfaceStatusDnsStatus_Object = MibTableColumn
acSysDataInterfaceStatusDnsStatus = _AcSysDataInterfaceStatusDnsStatus_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 2, 6, 4, 22, 1, 11),
    _AcSysDataInterfaceStatusDnsStatus_Type()
)
acSysDataInterfaceStatusDnsStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSysDataInterfaceStatusDnsStatus.setStatus("current")
_AcSysDataInterfaceStatusRxPackets_Type = Counter32
_AcSysDataInterfaceStatusRxPackets_Object = MibTableColumn
acSysDataInterfaceStatusRxPackets = _AcSysDataInterfaceStatusRxPackets_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 2, 6, 4, 22, 1, 12),
    _AcSysDataInterfaceStatusRxPackets_Type()
)
acSysDataInterfaceStatusRxPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSysDataInterfaceStatusRxPackets.setStatus("current")
_AcSysDataInterfaceStatusRxBytes_Type = Counter32
_AcSysDataInterfaceStatusRxBytes_Object = MibTableColumn
acSysDataInterfaceStatusRxBytes = _AcSysDataInterfaceStatusRxBytes_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 2, 6, 4, 22, 1, 13),
    _AcSysDataInterfaceStatusRxBytes_Type()
)
acSysDataInterfaceStatusRxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSysDataInterfaceStatusRxBytes.setStatus("current")
_AcSysDataInterfaceStatusRxDropped_Type = Counter32
_AcSysDataInterfaceStatusRxDropped_Object = MibTableColumn
acSysDataInterfaceStatusRxDropped = _AcSysDataInterfaceStatusRxDropped_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 2, 6, 4, 22, 1, 14),
    _AcSysDataInterfaceStatusRxDropped_Type()
)
acSysDataInterfaceStatusRxDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSysDataInterfaceStatusRxDropped.setStatus("current")
_AcSysDataInterfaceStatusRxErrors_Type = Counter32
_AcSysDataInterfaceStatusRxErrors_Object = MibTableColumn
acSysDataInterfaceStatusRxErrors = _AcSysDataInterfaceStatusRxErrors_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 2, 6, 4, 22, 1, 15),
    _AcSysDataInterfaceStatusRxErrors_Type()
)
acSysDataInterfaceStatusRxErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSysDataInterfaceStatusRxErrors.setStatus("current")
_AcSysDataInterfaceStatusTxPackets_Type = Counter32
_AcSysDataInterfaceStatusTxPackets_Object = MibTableColumn
acSysDataInterfaceStatusTxPackets = _AcSysDataInterfaceStatusTxPackets_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 2, 6, 4, 22, 1, 16),
    _AcSysDataInterfaceStatusTxPackets_Type()
)
acSysDataInterfaceStatusTxPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSysDataInterfaceStatusTxPackets.setStatus("current")
_AcSysDataInterfaceStatusTxBytes_Type = Counter32
_AcSysDataInterfaceStatusTxBytes_Object = MibTableColumn
acSysDataInterfaceStatusTxBytes = _AcSysDataInterfaceStatusTxBytes_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 2, 6, 4, 22, 1, 17),
    _AcSysDataInterfaceStatusTxBytes_Type()
)
acSysDataInterfaceStatusTxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSysDataInterfaceStatusTxBytes.setStatus("current")
_AcSysDataInterfaceStatusTxDropped_Type = Counter32
_AcSysDataInterfaceStatusTxDropped_Object = MibTableColumn
acSysDataInterfaceStatusTxDropped = _AcSysDataInterfaceStatusTxDropped_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 2, 6, 4, 22, 1, 18),
    _AcSysDataInterfaceStatusTxDropped_Type()
)
acSysDataInterfaceStatusTxDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSysDataInterfaceStatusTxDropped.setStatus("current")
_AcSysDataInterfaceStatusTxErrors_Type = Counter32
_AcSysDataInterfaceStatusTxErrors_Object = MibTableColumn
acSysDataInterfaceStatusTxErrors = _AcSysDataInterfaceStatusTxErrors_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 2, 6, 4, 22, 1, 19),
    _AcSysDataInterfaceStatusTxErrors_Type()
)
acSysDataInterfaceStatusTxErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSysDataInterfaceStatusTxErrors.setStatus("current")


class _AcSysDataInterfaceStatusMinutes_Type(Unsigned32):
    """Custom type acSysDataInterfaceStatusMinutes based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AcSysDataInterfaceStatusMinutes_Type.__name__ = "Unsigned32"
_AcSysDataInterfaceStatusMinutes_Object = MibTableColumn
acSysDataInterfaceStatusMinutes = _AcSysDataInterfaceStatusMinutes_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 2, 6, 4, 22, 1, 20),
    _AcSysDataInterfaceStatusMinutes_Type()
)
acSysDataInterfaceStatusMinutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSysDataInterfaceStatusMinutes.setStatus("current")


class _AcSysDataInterfaceStatusMinuteInputRate_Type(SnmpAdminString):
    """Custom type acSysDataInterfaceStatusMinuteInputRate based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 100),
    )


_AcSysDataInterfaceStatusMinuteInputRate_Type.__name__ = "SnmpAdminString"
_AcSysDataInterfaceStatusMinuteInputRate_Object = MibTableColumn
acSysDataInterfaceStatusMinuteInputRate = _AcSysDataInterfaceStatusMinuteInputRate_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 2, 6, 4, 22, 1, 21),
    _AcSysDataInterfaceStatusMinuteInputRate_Type()
)
acSysDataInterfaceStatusMinuteInputRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSysDataInterfaceStatusMinuteInputRate.setStatus("current")


class _AcSysDataInterfaceStatusMinuteOutputRate_Type(SnmpAdminString):
    """Custom type acSysDataInterfaceStatusMinuteOutputRate based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 100),
    )


_AcSysDataInterfaceStatusMinuteOutputRate_Type.__name__ = "SnmpAdminString"
_AcSysDataInterfaceStatusMinuteOutputRate_Object = MibTableColumn
acSysDataInterfaceStatusMinuteOutputRate = _AcSysDataInterfaceStatusMinuteOutputRate_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 2, 6, 4, 22, 1, 22),
    _AcSysDataInterfaceStatusMinuteOutputRate_Type()
)
acSysDataInterfaceStatusMinuteOutputRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSysDataInterfaceStatusMinuteOutputRate.setStatus("current")


class _AcSysDataInterfaceStatusSeconds_Type(Unsigned32):
    """Custom type acSysDataInterfaceStatusSeconds based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AcSysDataInterfaceStatusSeconds_Type.__name__ = "Unsigned32"
_AcSysDataInterfaceStatusSeconds_Object = MibTableColumn
acSysDataInterfaceStatusSeconds = _AcSysDataInterfaceStatusSeconds_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 2, 6, 4, 22, 1, 23),
    _AcSysDataInterfaceStatusSeconds_Type()
)
acSysDataInterfaceStatusSeconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSysDataInterfaceStatusSeconds.setStatus("current")


class _AcSysDataInterfaceStatusSecondInputRate_Type(SnmpAdminString):
    """Custom type acSysDataInterfaceStatusSecondInputRate based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 100),
    )


_AcSysDataInterfaceStatusSecondInputRate_Type.__name__ = "SnmpAdminString"
_AcSysDataInterfaceStatusSecondInputRate_Object = MibTableColumn
acSysDataInterfaceStatusSecondInputRate = _AcSysDataInterfaceStatusSecondInputRate_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 2, 6, 4, 22, 1, 24),
    _AcSysDataInterfaceStatusSecondInputRate_Type()
)
acSysDataInterfaceStatusSecondInputRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSysDataInterfaceStatusSecondInputRate.setStatus("current")


class _AcSysDataInterfaceStatusSecondOutputRate_Type(SnmpAdminString):
    """Custom type acSysDataInterfaceStatusSecondOutputRate based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 100),
    )


_AcSysDataInterfaceStatusSecondOutputRate_Type.__name__ = "SnmpAdminString"
_AcSysDataInterfaceStatusSecondOutputRate_Object = MibTableColumn
acSysDataInterfaceStatusSecondOutputRate = _AcSysDataInterfaceStatusSecondOutputRate_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 2, 6, 4, 22, 1, 25),
    _AcSysDataInterfaceStatusSecondOutputRate_Type()
)
acSysDataInterfaceStatusSecondOutputRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSysDataInterfaceStatusSecondOutputRate.setStatus("current")
_AcSysDeviceStatus_ObjectIdentity = ObjectIdentity
acSysDeviceStatus = _AcSysDeviceStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 2, 6, 5)
)
_AcSysEthernetDeviceStatusTable_Object = MibTable
acSysEthernetDeviceStatusTable = _AcSysEthernetDeviceStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 2, 6, 5, 21)
)
if mibBuilder.loadTexts:
    acSysEthernetDeviceStatusTable.setStatus("current")
_AcSysEthernetDeviceStatusEntry_Object = MibTableRow
acSysEthernetDeviceStatusEntry = _AcSysEthernetDeviceStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 2, 6, 5, 21, 1)
)
acSysEthernetDeviceStatusEntry.setIndexNames(
    (0, "AC-SYSTEM-MIB", "acSysEthernetDeviceStatusIndex"),
)
if mibBuilder.loadTexts:
    acSysEthernetDeviceStatusEntry.setStatus("current")


class _AcSysEthernetDeviceStatusIndex_Type(Unsigned32):
    """Custom type acSysEthernetDeviceStatusIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 47),
    )


_AcSysEthernetDeviceStatusIndex_Type.__name__ = "Unsigned32"
_AcSysEthernetDeviceStatusIndex_Object = MibTableColumn
acSysEthernetDeviceStatusIndex = _AcSysEthernetDeviceStatusIndex_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 2, 6, 5, 21, 1, 1),
    _AcSysEthernetDeviceStatusIndex_Type()
)
acSysEthernetDeviceStatusIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    acSysEthernetDeviceStatusIndex.setStatus("current")


class _AcSysEthernetDeviceStatusVlanID_Type(Unsigned32):
    """Custom type acSysEthernetDeviceStatusVlanID based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_AcSysEthernetDeviceStatusVlanID_Type.__name__ = "Unsigned32"
_AcSysEthernetDeviceStatusVlanID_Object = MibTableColumn
acSysEthernetDeviceStatusVlanID = _AcSysEthernetDeviceStatusVlanID_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 2, 6, 5, 21, 1, 2),
    _AcSysEthernetDeviceStatusVlanID_Type()
)
acSysEthernetDeviceStatusVlanID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSysEthernetDeviceStatusVlanID.setStatus("current")
_AcSysEthernetDeviceStatusUnderlyingInterface_Type = RowPointer
_AcSysEthernetDeviceStatusUnderlyingInterface_Object = MibTableColumn
acSysEthernetDeviceStatusUnderlyingInterface = _AcSysEthernetDeviceStatusUnderlyingInterface_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 2, 6, 5, 21, 1, 3),
    _AcSysEthernetDeviceStatusUnderlyingInterface_Type()
)
acSysEthernetDeviceStatusUnderlyingInterface.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSysEthernetDeviceStatusUnderlyingInterface.setStatus("current")


class _AcSysEthernetDeviceStatusDeviceName_Type(SnmpAdminString):
    """Custom type acSysEthernetDeviceStatusDeviceName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_AcSysEthernetDeviceStatusDeviceName_Type.__name__ = "SnmpAdminString"
_AcSysEthernetDeviceStatusDeviceName_Object = MibTableColumn
acSysEthernetDeviceStatusDeviceName = _AcSysEthernetDeviceStatusDeviceName_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 2, 6, 5, 21, 1, 4),
    _AcSysEthernetDeviceStatusDeviceName_Type()
)
acSysEthernetDeviceStatusDeviceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSysEthernetDeviceStatusDeviceName.setStatus("current")
_AcSysNetworkWiFiStats_ObjectIdentity = ObjectIdentity
acSysNetworkWiFiStats = _AcSysNetworkWiFiStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 2, 6, 6)
)
_AcSysNetworkWiFiStatsLinuxWatchdogTimeouts_Type = Counter32
_AcSysNetworkWiFiStatsLinuxWatchdogTimeouts_Object = MibScalar
acSysNetworkWiFiStatsLinuxWatchdogTimeouts = _AcSysNetworkWiFiStatsLinuxWatchdogTimeouts_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 2, 6, 6, 1),
    _AcSysNetworkWiFiStatsLinuxWatchdogTimeouts_Type()
)
acSysNetworkWiFiStatsLinuxWatchdogTimeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSysNetworkWiFiStatsLinuxWatchdogTimeouts.setStatus("current")
_AcSysNetworkWiFiStatsSWWatchdogTimeouts_Type = Counter32
_AcSysNetworkWiFiStatsSWWatchdogTimeouts_Object = MibScalar
acSysNetworkWiFiStatsSWWatchdogTimeouts = _AcSysNetworkWiFiStatsSWWatchdogTimeouts_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 2, 6, 6, 2),
    _AcSysNetworkWiFiStatsSWWatchdogTimeouts_Type()
)
acSysNetworkWiFiStatsSWWatchdogTimeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSysNetworkWiFiStatsSWWatchdogTimeouts.setStatus("current")
_AcSysNetworkWiFiStatsHWFatalInterrupts_Type = Counter32
_AcSysNetworkWiFiStatsHWFatalInterrupts_Object = MibScalar
acSysNetworkWiFiStatsHWFatalInterrupts = _AcSysNetworkWiFiStatsHWFatalInterrupts_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 2, 6, 6, 3),
    _AcSysNetworkWiFiStatsHWFatalInterrupts_Type()
)
acSysNetworkWiFiStatsHWFatalInterrupts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSysNetworkWiFiStatsHWFatalInterrupts.setStatus("current")
_AcSysNetworkWiFiStatsBeaconMissInterrupts_Type = Counter32
_AcSysNetworkWiFiStatsBeaconMissInterrupts_Object = MibScalar
acSysNetworkWiFiStatsBeaconMissInterrupts = _AcSysNetworkWiFiStatsBeaconMissInterrupts_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 2, 6, 6, 4),
    _AcSysNetworkWiFiStatsBeaconMissInterrupts_Type()
)
acSysNetworkWiFiStatsBeaconMissInterrupts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSysNetworkWiFiStatsBeaconMissInterrupts.setStatus("current")
_AcSysNetworkWiFiStatsRcvOverrunInterrupts_Type = Counter32
_AcSysNetworkWiFiStatsRcvOverrunInterrupts_Object = MibScalar
acSysNetworkWiFiStatsRcvOverrunInterrupts = _AcSysNetworkWiFiStatsRcvOverrunInterrupts_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 2, 6, 6, 5),
    _AcSysNetworkWiFiStatsRcvOverrunInterrupts_Type()
)
acSysNetworkWiFiStatsRcvOverrunInterrupts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSysNetworkWiFiStatsRcvOverrunInterrupts.setStatus("current")
_AcSysNetworkWiFiStatsRcvEolInterrupts_Type = Counter32
_AcSysNetworkWiFiStatsRcvEolInterrupts_Object = MibScalar
acSysNetworkWiFiStatsRcvEolInterrupts = _AcSysNetworkWiFiStatsRcvEolInterrupts_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 2, 6, 6, 6),
    _AcSysNetworkWiFiStatsRcvEolInterrupts_Type()
)
acSysNetworkWiFiStatsRcvEolInterrupts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSysNetworkWiFiStatsRcvEolInterrupts.setStatus("current")
_AcSysNetworkWiFiStatsTxUnderrunInterrupts_Type = Counter32
_AcSysNetworkWiFiStatsTxUnderrunInterrupts_Object = MibScalar
acSysNetworkWiFiStatsTxUnderrunInterrupts = _AcSysNetworkWiFiStatsTxUnderrunInterrupts_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 2, 6, 6, 7),
    _AcSysNetworkWiFiStatsTxUnderrunInterrupts_Type()
)
acSysNetworkWiFiStatsTxUnderrunInterrupts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSysNetworkWiFiStatsTxUnderrunInterrupts.setStatus("current")
_AcSysNetworkWiFiStatsGlobalTxTimeoutInterrupts_Type = Counter32
_AcSysNetworkWiFiStatsGlobalTxTimeoutInterrupts_Object = MibScalar
acSysNetworkWiFiStatsGlobalTxTimeoutInterrupts = _AcSysNetworkWiFiStatsGlobalTxTimeoutInterrupts_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 2, 6, 6, 8),
    _AcSysNetworkWiFiStatsGlobalTxTimeoutInterrupts_Type()
)
acSysNetworkWiFiStatsGlobalTxTimeoutInterrupts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSysNetworkWiFiStatsGlobalTxTimeoutInterrupts.setStatus("current")
_AcSysNetworkWiFiStatsCarrierSenseTimeoutInterrupts_Type = Counter32
_AcSysNetworkWiFiStatsCarrierSenseTimeoutInterrupts_Object = MibScalar
acSysNetworkWiFiStatsCarrierSenseTimeoutInterrupts = _AcSysNetworkWiFiStatsCarrierSenseTimeoutInterrupts_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 2, 6, 6, 9),
    _AcSysNetworkWiFiStatsCarrierSenseTimeoutInterrupts_Type()
)
acSysNetworkWiFiStatsCarrierSenseTimeoutInterrupts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSysNetworkWiFiStatsCarrierSenseTimeoutInterrupts.setStatus("current")
_AcSysNetworkWiFiStatsTxFramesTailDropped_Type = Counter32
_AcSysNetworkWiFiStatsTxFramesTailDropped_Object = MibScalar
acSysNetworkWiFiStatsTxFramesTailDropped = _AcSysNetworkWiFiStatsTxFramesTailDropped_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 2, 6, 6, 10),
    _AcSysNetworkWiFiStatsTxFramesTailDropped_Type()
)
acSysNetworkWiFiStatsTxFramesTailDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSysNetworkWiFiStatsTxFramesTailDropped.setStatus("current")
_AcSysNetworkWiFiStatsTxFramesTailDroppedDueDeadLink_Type = Counter32
_AcSysNetworkWiFiStatsTxFramesTailDroppedDueDeadLink_Object = MibScalar
acSysNetworkWiFiStatsTxFramesTailDroppedDueDeadLink = _AcSysNetworkWiFiStatsTxFramesTailDroppedDueDeadLink_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 2, 6, 6, 11),
    _AcSysNetworkWiFiStatsTxFramesTailDroppedDueDeadLink_Type()
)
acSysNetworkWiFiStatsTxFramesTailDroppedDueDeadLink.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSysNetworkWiFiStatsTxFramesTailDroppedDueDeadLink.setStatus("current")
_AcSysNetworkWiFiStatsTxDropsWrongState_Type = Counter32
_AcSysNetworkWiFiStatsTxDropsWrongState_Object = MibScalar
acSysNetworkWiFiStatsTxDropsWrongState = _AcSysNetworkWiFiStatsTxDropsWrongState_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 2, 6, 6, 12),
    _AcSysNetworkWiFiStatsTxDropsWrongState_Type()
)
acSysNetworkWiFiStatsTxDropsWrongState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSysNetworkWiFiStatsTxDropsWrongState.setStatus("current")
_AcSysNetworkWiFiStatsTxFramesDiscardedDeviceGone_Type = Counter32
_AcSysNetworkWiFiStatsTxFramesDiscardedDeviceGone_Object = MibScalar
acSysNetworkWiFiStatsTxFramesDiscardedDeviceGone = _AcSysNetworkWiFiStatsTxFramesDiscardedDeviceGone_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 2, 6, 6, 13),
    _AcSysNetworkWiFiStatsTxFramesDiscardedDeviceGone_Type()
)
acSysNetworkWiFiStatsTxFramesDiscardedDeviceGone.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSysNetworkWiFiStatsTxFramesDiscardedDeviceGone.setStatus("current")
_AcSysNetworkWiFiStatsTxQueueStoppedNoTxBuffers_Type = Counter32
_AcSysNetworkWiFiStatsTxQueueStoppedNoTxBuffers_Object = MibScalar
acSysNetworkWiFiStatsTxQueueStoppedNoTxBuffers = _AcSysNetworkWiFiStatsTxQueueStoppedNoTxBuffers_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 2, 6, 6, 14),
    _AcSysNetworkWiFiStatsTxQueueStoppedNoTxBuffers_Type()
)
acSysNetworkWiFiStatsTxQueueStoppedNoTxBuffers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSysNetworkWiFiStatsTxQueueStoppedNoTxBuffers.setStatus("current")
_AcSysNetworkWiFiStatsDataTxFailedNoTxBuffer_Type = Counter32
_AcSysNetworkWiFiStatsDataTxFailedNoTxBuffer_Object = MibScalar
acSysNetworkWiFiStatsDataTxFailedNoTxBuffer = _AcSysNetworkWiFiStatsDataTxFailedNoTxBuffer_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 2, 6, 6, 15),
    _AcSysNetworkWiFiStatsDataTxFailedNoTxBuffer_Type()
)
acSysNetworkWiFiStatsDataTxFailedNoTxBuffer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSysNetworkWiFiStatsDataTxFailedNoTxBuffer.setStatus("current")
_AcSysNetworkWiFiStatsMgtTxFailedNoTxBuffer_Type = Counter32
_AcSysNetworkWiFiStatsMgtTxFailedNoTxBuffer_Object = MibScalar
acSysNetworkWiFiStatsMgtTxFailedNoTxBuffer = _AcSysNetworkWiFiStatsMgtTxFailedNoTxBuffer_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 2, 6, 6, 16),
    _AcSysNetworkWiFiStatsMgtTxFailedNoTxBuffer_Type()
)
acSysNetworkWiFiStatsMgtTxFailedNoTxBuffer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSysNetworkWiFiStatsMgtTxFailedNoTxBuffer.setStatus("current")
_AcSysNetworkWiFiStatsBKTxFailedNoTxBuffer_Type = Counter32
_AcSysNetworkWiFiStatsBKTxFailedNoTxBuffer_Object = MibScalar
acSysNetworkWiFiStatsBKTxFailedNoTxBuffer = _AcSysNetworkWiFiStatsBKTxFailedNoTxBuffer_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 2, 6, 6, 17),
    _AcSysNetworkWiFiStatsBKTxFailedNoTxBuffer_Type()
)
acSysNetworkWiFiStatsBKTxFailedNoTxBuffer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSysNetworkWiFiStatsBKTxFailedNoTxBuffer.setStatus("current")
_AcSysNetworkWiFiStatsBETxFailedNoTxBuffer_Type = Counter32
_AcSysNetworkWiFiStatsBETxFailedNoTxBuffer_Object = MibScalar
acSysNetworkWiFiStatsBETxFailedNoTxBuffer = _AcSysNetworkWiFiStatsBETxFailedNoTxBuffer_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 2, 6, 6, 18),
    _AcSysNetworkWiFiStatsBETxFailedNoTxBuffer_Type()
)
acSysNetworkWiFiStatsBETxFailedNoTxBuffer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSysNetworkWiFiStatsBETxFailedNoTxBuffer.setStatus("current")
_AcSysNetworkWiFiStatsVITxFailedNoTxBuffer_Type = Counter32
_AcSysNetworkWiFiStatsVITxFailedNoTxBuffer_Object = MibScalar
acSysNetworkWiFiStatsVITxFailedNoTxBuffer = _AcSysNetworkWiFiStatsVITxFailedNoTxBuffer_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 2, 6, 6, 19),
    _AcSysNetworkWiFiStatsVITxFailedNoTxBuffer_Type()
)
acSysNetworkWiFiStatsVITxFailedNoTxBuffer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSysNetworkWiFiStatsVITxFailedNoTxBuffer.setStatus("current")
_AcSysNetworkWiFiStatsVOTxFailedNoTxBuffer_Type = Counter32
_AcSysNetworkWiFiStatsVOTxFailedNoTxBuffer_Object = MibScalar
acSysNetworkWiFiStatsVOTxFailedNoTxBuffer = _AcSysNetworkWiFiStatsVOTxFailedNoTxBuffer_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 2, 6, 6, 20),
    _AcSysNetworkWiFiStatsVOTxFailedNoTxBuffer_Type()
)
acSysNetworkWiFiStatsVOTxFailedNoTxBuffer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSysNetworkWiFiStatsVOTxFailedNoTxBuffer.setStatus("current")
_AcSysNetworkWiFiStatsTxFailedNoDescriptors_Type = Counter32
_AcSysNetworkWiFiStatsTxFailedNoDescriptors_Object = MibScalar
acSysNetworkWiFiStatsTxFailedNoDescriptors = _AcSysNetworkWiFiStatsTxFailedNoDescriptors_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 2, 6, 6, 21),
    _AcSysNetworkWiFiStatsTxFailedNoDescriptors_Type()
)
acSysNetworkWiFiStatsTxFailedNoDescriptors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSysNetworkWiFiStatsTxFailedNoDescriptors.setStatus("current")
_AcSysNetworkWiFiStatsTxFailedNoDescriptorsLegacyPackets_Type = Counter32
_AcSysNetworkWiFiStatsTxFailedNoDescriptorsLegacyPackets_Object = MibScalar
acSysNetworkWiFiStatsTxFailedNoDescriptorsLegacyPackets = _AcSysNetworkWiFiStatsTxFailedNoDescriptorsLegacyPackets_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 2, 6, 6, 22),
    _AcSysNetworkWiFiStatsTxFailedNoDescriptorsLegacyPackets_Type()
)
acSysNetworkWiFiStatsTxFailedNoDescriptorsLegacyPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSysNetworkWiFiStatsTxFailedNoDescriptorsLegacyPackets.setStatus("current")
_AcSysNetworkWiFiStatsTxFailedNoDescriptorsAggr_Type = Counter32
_AcSysNetworkWiFiStatsTxFailedNoDescriptorsAggr_Object = MibScalar
acSysNetworkWiFiStatsTxFailedNoDescriptorsAggr = _AcSysNetworkWiFiStatsTxFailedNoDescriptorsAggr_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 2, 6, 6, 23),
    _AcSysNetworkWiFiStatsTxFailedNoDescriptorsAggr_Type()
)
acSysNetworkWiFiStatsTxFailedNoDescriptorsAggr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSysNetworkWiFiStatsTxFailedNoDescriptorsAggr.setStatus("current")
_AcSysNetworkWiFiStatsTxFailedBadSetupLegacyPackets_Type = Counter32
_AcSysNetworkWiFiStatsTxFailedBadSetupLegacyPackets_Object = MibScalar
acSysNetworkWiFiStatsTxFailedBadSetupLegacyPackets = _AcSysNetworkWiFiStatsTxFailedBadSetupLegacyPackets_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 2, 6, 6, 24),
    _AcSysNetworkWiFiStatsTxFailedBadSetupLegacyPackets_Type()
)
acSysNetworkWiFiStatsTxFailedBadSetupLegacyPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSysNetworkWiFiStatsTxFailedBadSetupLegacyPackets.setStatus("current")
_AcSysNetworkWiFiStatsTxFailedBadSetupAggr_Type = Counter32
_AcSysNetworkWiFiStatsTxFailedBadSetupAggr_Object = MibScalar
acSysNetworkWiFiStatsTxFailedBadSetupAggr = _AcSysNetworkWiFiStatsTxFailedBadSetupAggr_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 2, 6, 6, 25),
    _AcSysNetworkWiFiStatsTxFailedBadSetupAggr_Type()
)
acSysNetworkWiFiStatsTxFailedBadSetupAggr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSysNetworkWiFiStatsTxFailedBadSetupAggr.setStatus("current")
_AcSysNetworkWiFiStatsTxFailedNoSKBSLegacyEncaps_Type = Counter32
_AcSysNetworkWiFiStatsTxFailedNoSKBSLegacyEncaps_Object = MibScalar
acSysNetworkWiFiStatsTxFailedNoSKBSLegacyEncaps = _AcSysNetworkWiFiStatsTxFailedNoSKBSLegacyEncaps_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 2, 6, 6, 26),
    _AcSysNetworkWiFiStatsTxFailedNoSKBSLegacyEncaps_Type()
)
acSysNetworkWiFiStatsTxFailedNoSKBSLegacyEncaps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSysNetworkWiFiStatsTxFailedNoSKBSLegacyEncaps.setStatus("current")
_AcSysNetworkWiFiStatsTxFailedNoSKBSAggrEncaps_Type = Counter32
_AcSysNetworkWiFiStatsTxFailedNoSKBSAggrEncaps_Object = MibScalar
acSysNetworkWiFiStatsTxFailedNoSKBSAggrEncaps = _AcSysNetworkWiFiStatsTxFailedNoSKBSAggrEncaps_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 2, 6, 6, 27),
    _AcSysNetworkWiFiStatsTxFailedNoSKBSAggrEncaps_Type()
)
acSysNetworkWiFiStatsTxFailedNoSKBSAggrEncaps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSysNetworkWiFiStatsTxFailedNoSKBSAggrEncaps.setStatus("current")
_AcSysNetworkWiFiStatsTxFailedNoNode_Type = Counter32
_AcSysNetworkWiFiStatsTxFailedNoNode_Object = MibScalar
acSysNetworkWiFiStatsTxFailedNoNode = _AcSysNetworkWiFiStatsTxFailedNoNode_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 2, 6, 6, 28),
    _AcSysNetworkWiFiStatsTxFailedNoNode_Type()
)
acSysNetworkWiFiStatsTxFailedNoNode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSysNetworkWiFiStatsTxFailedNoNode.setStatus("current")
_AcSysNetworkWiFiStatsTxFailedFIFOUnderrunAggr_Type = Counter32
_AcSysNetworkWiFiStatsTxFailedFIFOUnderrunAggr_Object = MibScalar
acSysNetworkWiFiStatsTxFailedFIFOUnderrunAggr = _AcSysNetworkWiFiStatsTxFailedFIFOUnderrunAggr_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 2, 6, 6, 29),
    _AcSysNetworkWiFiStatsTxFailedFIFOUnderrunAggr_Type()
)
acSysNetworkWiFiStatsTxFailedFIFOUnderrunAggr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSysNetworkWiFiStatsTxFailedFIFOUnderrunAggr.setStatus("current")
_AcSysNetworkWiFiStatsTxFailedFIFOUnderrunLegacyPackets_Type = Counter32
_AcSysNetworkWiFiStatsTxFailedFIFOUnderrunLegacyPackets_Object = MibScalar
acSysNetworkWiFiStatsTxFailedFIFOUnderrunLegacyPackets = _AcSysNetworkWiFiStatsTxFailedFIFOUnderrunLegacyPackets_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 2, 6, 6, 30),
    _AcSysNetworkWiFiStatsTxFailedFIFOUnderrunLegacyPackets_Type()
)
acSysNetworkWiFiStatsTxFailedFIFOUnderrunLegacyPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSysNetworkWiFiStatsTxFailedFIFOUnderrunLegacyPackets.setStatus("current")
_AcSysNetworkWiFiStatsTxFailedXmitFiter_Type = Counter32
_AcSysNetworkWiFiStatsTxFailedXmitFiter_Object = MibScalar
acSysNetworkWiFiStatsTxFailedXmitFiter = _AcSysNetworkWiFiStatsTxFailedXmitFiter_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 2, 6, 6, 31),
    _AcSysNetworkWiFiStatsTxFailedXmitFiter_Type()
)
acSysNetworkWiFiStatsTxFailedXmitFiter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSysNetworkWiFiStatsTxFailedXmitFiter.setStatus("current")
_AcSysNetworkWiFiStatsTxFailedTimerExp_Type = Counter32
_AcSysNetworkWiFiStatsTxFailedTimerExp_Object = MibScalar
acSysNetworkWiFiStatsTxFailedTimerExp = _AcSysNetworkWiFiStatsTxFailedTimerExp_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 2, 6, 6, 32),
    _AcSysNetworkWiFiStatsTxFailedTimerExp_Type()
)
acSysNetworkWiFiStatsTxFailedTimerExp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSysNetworkWiFiStatsTxFailedTimerExp.setStatus("current")
_AcSysNetworkWiFiStatsTxFailedTxopExceededAggr_Type = Counter32
_AcSysNetworkWiFiStatsTxFailedTxopExceededAggr_Object = MibScalar
acSysNetworkWiFiStatsTxFailedTxopExceededAggr = _AcSysNetworkWiFiStatsTxFailedTxopExceededAggr_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 2, 6, 6, 33),
    _AcSysNetworkWiFiStatsTxFailedTxopExceededAggr_Type()
)
acSysNetworkWiFiStatsTxFailedTxopExceededAggr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSysNetworkWiFiStatsTxFailedTxopExceededAggr.setStatus("current")
_AcSysNetworkWiFiStatsTxFailedDescriptorCfgErrAggr_Type = Counter32
_AcSysNetworkWiFiStatsTxFailedDescriptorCfgErrAggr_Object = MibScalar
acSysNetworkWiFiStatsTxFailedDescriptorCfgErrAggr = _AcSysNetworkWiFiStatsTxFailedDescriptorCfgErrAggr_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 2, 6, 6, 34),
    _AcSysNetworkWiFiStatsTxFailedDescriptorCfgErrAggr_Type()
)
acSysNetworkWiFiStatsTxFailedDescriptorCfgErrAggr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSysNetworkWiFiStatsTxFailedDescriptorCfgErrAggr.setStatus("current")
_AcSysNetworkWiFiStatsTxFailedDataUnderrunAggr_Type = Counter32
_AcSysNetworkWiFiStatsTxFailedDataUnderrunAggr_Object = MibScalar
acSysNetworkWiFiStatsTxFailedDataUnderrunAggr = _AcSysNetworkWiFiStatsTxFailedDataUnderrunAggr_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 2, 6, 6, 35),
    _AcSysNetworkWiFiStatsTxFailedDataUnderrunAggr_Type()
)
acSysNetworkWiFiStatsTxFailedDataUnderrunAggr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSysNetworkWiFiStatsTxFailedDataUnderrunAggr.setStatus("current")
_AcSysNetworkWiFiStatsTxFailedDelimiterUnderrunAggr_Type = Counter32
_AcSysNetworkWiFiStatsTxFailedDelimiterUnderrunAggr_Object = MibScalar
acSysNetworkWiFiStatsTxFailedDelimiterUnderrunAggr = _AcSysNetworkWiFiStatsTxFailedDelimiterUnderrunAggr_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 2, 6, 6, 36),
    _AcSysNetworkWiFiStatsTxFailedDelimiterUnderrunAggr_Type()
)
acSysNetworkWiFiStatsTxFailedDelimiterUnderrunAggr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSysNetworkWiFiStatsTxFailedDelimiterUnderrunAggr.setStatus("current")
_AcSysNetworkWiFiStatsTxFailedInvalidBAState_Type = Counter32
_AcSysNetworkWiFiStatsTxFailedInvalidBAState_Object = MibScalar
acSysNetworkWiFiStatsTxFailedInvalidBAState = _AcSysNetworkWiFiStatsTxFailedInvalidBAState_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 2, 6, 6, 37),
    _AcSysNetworkWiFiStatsTxFailedInvalidBAState_Type()
)
acSysNetworkWiFiStatsTxFailedInvalidBAState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSysNetworkWiFiStatsTxFailedInvalidBAState.setStatus("current")
_AcSysNetworkWiFiStatsRxFailedFIFOOverrun_Type = Counter32
_AcSysNetworkWiFiStatsRxFailedFIFOOverrun_Object = MibScalar
acSysNetworkWiFiStatsRxFailedFIFOOverrun = _AcSysNetworkWiFiStatsRxFailedFIFOOverrun_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 2, 6, 6, 38),
    _AcSysNetworkWiFiStatsRxFailedFIFOOverrun_Type()
)
acSysNetworkWiFiStatsRxFailedFIFOOverrun.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSysNetworkWiFiStatsRxFailedFIFOOverrun.setStatus("current")
_AcSysNetworkWiFiStatsRxDiscardedFrameTooBig_Type = Counter32
_AcSysNetworkWiFiStatsRxDiscardedFrameTooBig_Object = MibScalar
acSysNetworkWiFiStatsRxDiscardedFrameTooBig = _AcSysNetworkWiFiStatsRxDiscardedFrameTooBig_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 2, 6, 6, 39),
    _AcSysNetworkWiFiStatsRxDiscardedFrameTooBig_Type()
)
acSysNetworkWiFiStatsRxDiscardedFrameTooBig.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSysNetworkWiFiStatsRxDiscardedFrameTooBig.setStatus("current")
_AcSysNetworkWiFiStatsRxFailedNoBuff_Type = Counter32
_AcSysNetworkWiFiStatsRxFailedNoBuff_Object = MibScalar
acSysNetworkWiFiStatsRxFailedNoBuff = _AcSysNetworkWiFiStatsRxFailedNoBuff_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 2, 6, 6, 40),
    _AcSysNetworkWiFiStatsRxFailedNoBuff_Type()
)
acSysNetworkWiFiStatsRxFailedNoBuff.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSysNetworkWiFiStatsRxFailedNoBuff.setStatus("current")
_AcSysNetworkWiFiStatsRxFailedDecryption_Type = Counter32
_AcSysNetworkWiFiStatsRxFailedDecryption_Object = MibScalar
acSysNetworkWiFiStatsRxFailedDecryption = _AcSysNetworkWiFiStatsRxFailedDecryption_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 2, 6, 6, 41),
    _AcSysNetworkWiFiStatsRxFailedDecryption_Type()
)
acSysNetworkWiFiStatsRxFailedDecryption.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSysNetworkWiFiStatsRxFailedDecryption.setStatus("current")
_AcSysNetworkWiFiStatsRxFailedMICFailure_Type = Counter32
_AcSysNetworkWiFiStatsRxFailedMICFailure_Object = MibScalar
acSysNetworkWiFiStatsRxFailedMICFailure = _AcSysNetworkWiFiStatsRxFailedMICFailure_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 2, 6, 6, 42),
    _AcSysNetworkWiFiStatsRxFailedMICFailure_Type()
)
acSysNetworkWiFiStatsRxFailedMICFailure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSysNetworkWiFiStatsRxFailedMICFailure.setStatus("current")
_AcSysNetworkWiFiStatsRxFailedDecryptBusyError_Type = Counter32
_AcSysNetworkWiFiStatsRxFailedDecryptBusyError_Object = MibScalar
acSysNetworkWiFiStatsRxFailedDecryptBusyError = _AcSysNetworkWiFiStatsRxFailedDecryptBusyError_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 2, 6, 6, 43),
    _AcSysNetworkWiFiStatsRxFailedDecryptBusyError_Type()
)
acSysNetworkWiFiStatsRxFailedDecryptBusyError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSysNetworkWiFiStatsRxFailedDecryptBusyError.setStatus("current")
_AcSysNetworkWiFiStatsRxFailedPktsBadVer_Type = Counter32
_AcSysNetworkWiFiStatsRxFailedPktsBadVer_Object = MibScalar
acSysNetworkWiFiStatsRxFailedPktsBadVer = _AcSysNetworkWiFiStatsRxFailedPktsBadVer_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 2, 6, 6, 44),
    _AcSysNetworkWiFiStatsRxFailedPktsBadVer_Type()
)
acSysNetworkWiFiStatsRxFailedPktsBadVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSysNetworkWiFiStatsRxFailedPktsBadVer.setStatus("current")
_AcSysNetworkWiFiStatsNoBuffForBeacon_Type = Counter32
_AcSysNetworkWiFiStatsNoBuffForBeacon_Object = MibScalar
acSysNetworkWiFiStatsNoBuffForBeacon = _AcSysNetworkWiFiStatsNoBuffForBeacon_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 2, 6, 6, 45),
    _AcSysNetworkWiFiStatsNoBuffForBeacon_Type()
)
acSysNetworkWiFiStatsNoBuffForBeacon.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSysNetworkWiFiStatsNoBuffForBeacon.setStatus("current")
_AcSysNetworkWiFiStatsBeaconStuck_Type = Counter32
_AcSysNetworkWiFiStatsBeaconStuck_Object = MibScalar
acSysNetworkWiFiStatsBeaconStuck = _AcSysNetworkWiFiStatsBeaconStuck_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 2, 6, 6, 46),
    _AcSysNetworkWiFiStatsBeaconStuck_Type()
)
acSysNetworkWiFiStatsBeaconStuck.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSysNetworkWiFiStatsBeaconStuck.setStatus("current")
_AcSysNetworkWiFiStatsPeriodicCalibrationFail_Type = Counter32
_AcSysNetworkWiFiStatsPeriodicCalibrationFail_Object = MibScalar
acSysNetworkWiFiStatsPeriodicCalibrationFail = _AcSysNetworkWiFiStatsPeriodicCalibrationFail_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 2, 6, 6, 47),
    _AcSysNetworkWiFiStatsPeriodicCalibrationFail_Type()
)
acSysNetworkWiFiStatsPeriodicCalibrationFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSysNetworkWiFiStatsPeriodicCalibrationFail.setStatus("current")
_AcSysNetworkWiFiStatsFastChannelChangeFail_Type = Counter32
_AcSysNetworkWiFiStatsFastChannelChangeFail_Object = MibScalar
acSysNetworkWiFiStatsFastChannelChangeFail = _AcSysNetworkWiFiStatsFastChannelChangeFail_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 2, 6, 6, 48),
    _AcSysNetworkWiFiStatsFastChannelChangeFail_Type()
)
acSysNetworkWiFiStatsFastChannelChangeFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSysNetworkWiFiStatsFastChannelChangeFail.setStatus("current")
_AcSysNetworkCell_ObjectIdentity = ObjectIdentity
acSysNetworkCell = _AcSysNetworkCell_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 2, 6, 7)
)


class _AcSysNetworkCellCurrentNetworkTypeDescription_Type(SnmpAdminString):
    """Custom type acSysNetworkCellCurrentNetworkTypeDescription based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_AcSysNetworkCellCurrentNetworkTypeDescription_Type.__name__ = "SnmpAdminString"
_AcSysNetworkCellCurrentNetworkTypeDescription_Object = MibScalar
acSysNetworkCellCurrentNetworkTypeDescription = _AcSysNetworkCellCurrentNetworkTypeDescription_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 2, 6, 7, 1),
    _AcSysNetworkCellCurrentNetworkTypeDescription_Type()
)
acSysNetworkCellCurrentNetworkTypeDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSysNetworkCellCurrentNetworkTypeDescription.setStatus("current")


class _AcSysNetworkCellSignalStrength_Type(Integer32):
    """Custom type acSysNetworkCellSignalStrength based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-120, -30),
    )


_AcSysNetworkCellSignalStrength_Type.__name__ = "Integer32"
_AcSysNetworkCellSignalStrength_Object = MibScalar
acSysNetworkCellSignalStrength = _AcSysNetworkCellSignalStrength_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 2, 6, 7, 2),
    _AcSysNetworkCellSignalStrength_Type()
)
acSysNetworkCellSignalStrength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSysNetworkCellSignalStrength.setStatus("current")


class _AcSysNetworkCellInterfaceWorkingMode_Type(Integer32):
    """Custom type acSysNetworkCellInterfaceWorkingMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("ppp", 0),
          ("dhcp", 1))
    )


_AcSysNetworkCellInterfaceWorkingMode_Type.__name__ = "Integer32"
_AcSysNetworkCellInterfaceWorkingMode_Object = MibScalar
acSysNetworkCellInterfaceWorkingMode = _AcSysNetworkCellInterfaceWorkingMode_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 2, 6, 7, 3),
    _AcSysNetworkCellInterfaceWorkingMode_Type()
)
acSysNetworkCellInterfaceWorkingMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSysNetworkCellInterfaceWorkingMode.setStatus("current")


class _AcSysNetworkCellWanIPAddress_Type(SnmpAdminString):
    """Custom type acSysNetworkCellWanIPAddress based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_AcSysNetworkCellWanIPAddress_Type.__name__ = "SnmpAdminString"
_AcSysNetworkCellWanIPAddress_Object = MibScalar
acSysNetworkCellWanIPAddress = _AcSysNetworkCellWanIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 2, 6, 7, 4),
    _AcSysNetworkCellWanIPAddress_Type()
)
acSysNetworkCellWanIPAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSysNetworkCellWanIPAddress.setStatus("current")
_AcSysTime_ObjectIdentity = ObjectIdentity
acSysTime = _AcSysTime_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 2, 7)
)


class _AcSysTimeUp_Type(Unsigned32):
    """Custom type acSysTimeUp based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AcSysTimeUp_Type.__name__ = "Unsigned32"
_AcSysTimeUp_Object = MibScalar
acSysTimeUp = _AcSysTimeUp_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 2, 7, 1),
    _AcSysTimeUp_Type()
)
acSysTimeUp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSysTimeUp.setStatus("current")
_AcSysTimeLastConfig_Type = TimeTicks
_AcSysTimeLastConfig_Object = MibScalar
acSysTimeLastConfig = _AcSysTimeLastConfig_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 2, 7, 2),
    _AcSysTimeLastConfig_Type()
)
acSysTimeLastConfig.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSysTimeLastConfig.setStatus("current")


class _AcSysTimeAlarmLastChange_Type(SnmpAdminString):
    """Custom type acSysTimeAlarmLastChange based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 50),
    )


_AcSysTimeAlarmLastChange_Type.__name__ = "SnmpAdminString"
_AcSysTimeAlarmLastChange_Object = MibScalar
acSysTimeAlarmLastChange = _AcSysTimeAlarmLastChange_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 2, 7, 3),
    _AcSysTimeAlarmLastChange_Type()
)
acSysTimeAlarmLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSysTimeAlarmLastChange.setStatus("current")


class _AcSysTimeSystemAvailabilityStartTime_Type(SnmpAdminString):
    """Custom type acSysTimeSystemAvailabilityStartTime based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_AcSysTimeSystemAvailabilityStartTime_Type.__name__ = "SnmpAdminString"
_AcSysTimeSystemAvailabilityStartTime_Object = MibScalar
acSysTimeSystemAvailabilityStartTime = _AcSysTimeSystemAvailabilityStartTime_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 2, 7, 4),
    _AcSysTimeSystemAvailabilityStartTime_Type()
)
acSysTimeSystemAvailabilityStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSysTimeSystemAvailabilityStartTime.setStatus("current")


class _AcSysTimeSystemAvailability_Type(Unsigned32):
    """Custom type acSysTimeSystemAvailability based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AcSysTimeSystemAvailability_Type.__name__ = "Unsigned32"
_AcSysTimeSystemAvailability_Object = MibScalar
acSysTimeSystemAvailability = _AcSysTimeSystemAvailability_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 2, 7, 5),
    _AcSysTimeSystemAvailability_Type()
)
acSysTimeSystemAvailability.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSysTimeSystemAvailability.setStatus("current")
_AcSysVoicePrompt_ObjectIdentity = ObjectIdentity
acSysVoicePrompt = _AcSysVoicePrompt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 2, 8)
)


class _AcSysVoicePromptTotalMemorySize_Type(Unsigned32):
    """Custom type acSysVoicePromptTotalMemorySize based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AcSysVoicePromptTotalMemorySize_Type.__name__ = "Unsigned32"
_AcSysVoicePromptTotalMemorySize_Object = MibScalar
acSysVoicePromptTotalMemorySize = _AcSysVoicePromptTotalMemorySize_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 2, 8, 1),
    _AcSysVoicePromptTotalMemorySize_Type()
)
acSysVoicePromptTotalMemorySize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSysVoicePromptTotalMemorySize.setStatus("current")


class _AcSysVoicePromptMaxFreeMemorySize_Type(Unsigned32):
    """Custom type acSysVoicePromptMaxFreeMemorySize based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AcSysVoicePromptMaxFreeMemorySize_Type.__name__ = "Unsigned32"
_AcSysVoicePromptMaxFreeMemorySize_Object = MibScalar
acSysVoicePromptMaxFreeMemorySize = _AcSysVoicePromptMaxFreeMemorySize_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 2, 8, 2),
    _AcSysVoicePromptMaxFreeMemorySize_Type()
)
acSysVoicePromptMaxFreeMemorySize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSysVoicePromptMaxFreeMemorySize.setStatus("current")
_AcSysRepositoryAMS_ObjectIdentity = ObjectIdentity
acSysRepositoryAMS = _AcSysRepositoryAMS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 2, 9)
)


class _AcSysRepositoryAMSIsReadyForUpdate_Type(Integer32):
    """Custom type acSysRepositoryAMSIsReadyForUpdate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("false", 0),
          ("true", 1))
    )


_AcSysRepositoryAMSIsReadyForUpdate_Type.__name__ = "Integer32"
_AcSysRepositoryAMSIsReadyForUpdate_Object = MibScalar
acSysRepositoryAMSIsReadyForUpdate = _AcSysRepositoryAMSIsReadyForUpdate_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 2, 9, 1),
    _AcSysRepositoryAMSIsReadyForUpdate_Type()
)
acSysRepositoryAMSIsReadyForUpdate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSysRepositoryAMSIsReadyForUpdate.setStatus("current")
_AcSysHAStatus_ObjectIdentity = ObjectIdentity
acSysHAStatus = _AcSysHAStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 2, 10)
)


class _AcSysHAStatusReady_Type(Integer32):
    """Custom type acSysHAStatusReady based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("notApplicable", 1),
          ("yes", 2),
          ("no", 3))
    )


_AcSysHAStatusReady_Type.__name__ = "Integer32"
_AcSysHAStatusReady_Object = MibScalar
acSysHAStatusReady = _AcSysHAStatusReady_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 2, 10, 1),
    _AcSysHAStatusReady_Type()
)
acSysHAStatusReady.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSysHAStatusReady.setStatus("current")


class _AcSysHAStatusNetworkWatchdogStatus_Type(SnmpAdminString):
    """Custom type acSysHAStatusNetworkWatchdogStatus based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 400),
    )


_AcSysHAStatusNetworkWatchdogStatus_Type.__name__ = "SnmpAdminString"
_AcSysHAStatusNetworkWatchdogStatus_Object = MibScalar
acSysHAStatusNetworkWatchdogStatus = _AcSysHAStatusNetworkWatchdogStatus_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 2, 10, 2),
    _AcSysHAStatusNetworkWatchdogStatus_Type()
)
acSysHAStatusNetworkWatchdogStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSysHAStatusNetworkWatchdogStatus.setStatus("current")
_AcSysLDAPStatus_ObjectIdentity = ObjectIdentity
acSysLDAPStatus = _AcSysLDAPStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 2, 11)
)


class _AcSysLDAPStatusServerMode_Type(Integer32):
    """Custom type acSysLDAPStatusServerMode based on Integer32"""
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
        *(("notApplicable", 0),
          ("connectionBroken", 1),
          ("connecting", 2),
          ("connected", 3))
    )


_AcSysLDAPStatusServerMode_Type.__name__ = "Integer32"
_AcSysLDAPStatusServerMode_Object = MibScalar
acSysLDAPStatusServerMode = _AcSysLDAPStatusServerMode_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 2, 11, 1),
    _AcSysLDAPStatusServerMode_Type()
)
acSysLDAPStatusServerMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSysLDAPStatusServerMode.setStatus("obsolete")
_AcSysNqmStatus_ObjectIdentity = ObjectIdentity
acSysNqmStatus = _AcSysNqmStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 2, 12)
)
_AcSysNqmHistoryTable_Object = MibTable
acSysNqmHistoryTable = _AcSysNqmHistoryTable_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 2, 12, 1)
)
if mibBuilder.loadTexts:
    acSysNqmHistoryTable.setStatus("current")
_AcSysNqmHistoryEntry_Object = MibTableRow
acSysNqmHistoryEntry = _AcSysNqmHistoryEntry_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 2, 12, 1, 1)
)
acSysNqmHistoryEntry.setIndexNames(
    (0, "AC-SYSTEM-MIB", "acSysNqmHistorySenderIndex"),
    (0, "AC-SYSTEM-MIB", "acSysNqmHistoryIndex"),
)
if mibBuilder.loadTexts:
    acSysNqmHistoryEntry.setStatus("current")


class _AcSysNqmHistorySenderIndex_Type(Unsigned32):
    """Custom type acSysNqmHistorySenderIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 9),
    )


_AcSysNqmHistorySenderIndex_Type.__name__ = "Unsigned32"
_AcSysNqmHistorySenderIndex_Object = MibTableColumn
acSysNqmHistorySenderIndex = _AcSysNqmHistorySenderIndex_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 2, 12, 1, 1, 1),
    _AcSysNqmHistorySenderIndex_Type()
)
acSysNqmHistorySenderIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    acSysNqmHistorySenderIndex.setStatus("current")
_AcSysNqmHistoryIndex_Type = Unsigned32
_AcSysNqmHistoryIndex_Object = MibTableColumn
acSysNqmHistoryIndex = _AcSysNqmHistoryIndex_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 2, 12, 1, 1, 2),
    _AcSysNqmHistoryIndex_Type()
)
acSysNqmHistoryIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    acSysNqmHistoryIndex.setStatus("current")


class _AcSysNqmHistoryProbeTime_Type(SnmpAdminString):
    """Custom type acSysNqmHistoryProbeTime based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AcSysNqmHistoryProbeTime_Type.__name__ = "SnmpAdminString"
_AcSysNqmHistoryProbeTime_Object = MibTableColumn
acSysNqmHistoryProbeTime = _AcSysNqmHistoryProbeTime_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 2, 12, 1, 1, 3),
    _AcSysNqmHistoryProbeTime_Type()
)
acSysNqmHistoryProbeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSysNqmHistoryProbeTime.setStatus("current")


class _AcSysNqmHistoryIsValid_Type(SnmpAdminString):
    """Custom type acSysNqmHistoryIsValid based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_AcSysNqmHistoryIsValid_Type.__name__ = "SnmpAdminString"
_AcSysNqmHistoryIsValid_Object = MibTableColumn
acSysNqmHistoryIsValid = _AcSysNqmHistoryIsValid_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 2, 12, 1, 1, 4),
    _AcSysNqmHistoryIsValid_Type()
)
acSysNqmHistoryIsValid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSysNqmHistoryIsValid.setStatus("current")


class _AcSysNqmHistoryRoundTripTime_Type(Unsigned32):
    """Custom type acSysNqmHistoryRoundTripTime based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 99999),
    )


_AcSysNqmHistoryRoundTripTime_Type.__name__ = "Unsigned32"
_AcSysNqmHistoryRoundTripTime_Object = MibTableColumn
acSysNqmHistoryRoundTripTime = _AcSysNqmHistoryRoundTripTime_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 2, 12, 1, 1, 5),
    _AcSysNqmHistoryRoundTripTime_Type()
)
acSysNqmHistoryRoundTripTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSysNqmHistoryRoundTripTime.setStatus("current")


class _AcSysNqmHistoryPacketLossTx_Type(Unsigned32):
    """Custom type acSysNqmHistoryPacketLossTx based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 999999),
    )


_AcSysNqmHistoryPacketLossTx_Type.__name__ = "Unsigned32"
_AcSysNqmHistoryPacketLossTx_Object = MibTableColumn
acSysNqmHistoryPacketLossTx = _AcSysNqmHistoryPacketLossTx_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 2, 12, 1, 1, 6),
    _AcSysNqmHistoryPacketLossTx_Type()
)
acSysNqmHistoryPacketLossTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSysNqmHistoryPacketLossTx.setStatus("current")


class _AcSysNqmHistoryPacketLossRx_Type(Unsigned32):
    """Custom type acSysNqmHistoryPacketLossRx based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 999999),
    )


_AcSysNqmHistoryPacketLossRx_Type.__name__ = "Unsigned32"
_AcSysNqmHistoryPacketLossRx_Object = MibTableColumn
acSysNqmHistoryPacketLossRx = _AcSysNqmHistoryPacketLossRx_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 2, 12, 1, 1, 7),
    _AcSysNqmHistoryPacketLossRx_Type()
)
acSysNqmHistoryPacketLossRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSysNqmHistoryPacketLossRx.setStatus("current")


class _AcSysNqmHistoryTotalPacketLoss_Type(Unsigned32):
    """Custom type acSysNqmHistoryTotalPacketLoss based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 9999999),
    )


_AcSysNqmHistoryTotalPacketLoss_Type.__name__ = "Unsigned32"
_AcSysNqmHistoryTotalPacketLoss_Object = MibTableColumn
acSysNqmHistoryTotalPacketLoss = _AcSysNqmHistoryTotalPacketLoss_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 2, 12, 1, 1, 8),
    _AcSysNqmHistoryTotalPacketLoss_Type()
)
acSysNqmHistoryTotalPacketLoss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSysNqmHistoryTotalPacketLoss.setStatus("current")


class _AcSysNqmHistoryJitterTx_Type(Unsigned32):
    """Custom type acSysNqmHistoryJitterTx based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 999999),
    )


_AcSysNqmHistoryJitterTx_Type.__name__ = "Unsigned32"
_AcSysNqmHistoryJitterTx_Object = MibTableColumn
acSysNqmHistoryJitterTx = _AcSysNqmHistoryJitterTx_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 2, 12, 1, 1, 9),
    _AcSysNqmHistoryJitterTx_Type()
)
acSysNqmHistoryJitterTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSysNqmHistoryJitterTx.setStatus("current")


class _AcSysNqmHistoryJitterRx_Type(Unsigned32):
    """Custom type acSysNqmHistoryJitterRx based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 999999),
    )


_AcSysNqmHistoryJitterRx_Type.__name__ = "Unsigned32"
_AcSysNqmHistoryJitterRx_Object = MibTableColumn
acSysNqmHistoryJitterRx = _AcSysNqmHistoryJitterRx_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 2, 12, 1, 1, 10),
    _AcSysNqmHistoryJitterRx_Type()
)
acSysNqmHistoryJitterRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSysNqmHistoryJitterRx.setStatus("current")


class _AcSysNqmHistoryTotalJitter_Type(Unsigned32):
    """Custom type acSysNqmHistoryTotalJitter based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 9999999),
    )


_AcSysNqmHistoryTotalJitter_Type.__name__ = "Unsigned32"
_AcSysNqmHistoryTotalJitter_Object = MibTableColumn
acSysNqmHistoryTotalJitter = _AcSysNqmHistoryTotalJitter_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 2, 12, 1, 1, 11),
    _AcSysNqmHistoryTotalJitter_Type()
)
acSysNqmHistoryTotalJitter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSysNqmHistoryTotalJitter.setStatus("current")


class _AcSysNqmHistoryCqMos_Type(Unsigned32):
    """Custom type acSysNqmHistoryCqMos based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 99999),
    )


_AcSysNqmHistoryCqMos_Type.__name__ = "Unsigned32"
_AcSysNqmHistoryCqMos_Object = MibTableColumn
acSysNqmHistoryCqMos = _AcSysNqmHistoryCqMos_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 2, 12, 1, 1, 12),
    _AcSysNqmHistoryCqMos_Type()
)
acSysNqmHistoryCqMos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSysNqmHistoryCqMos.setStatus("current")


class _AcSysNqmHistoryLqMos_Type(Unsigned32):
    """Custom type acSysNqmHistoryLqMos based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 99999),
    )


_AcSysNqmHistoryLqMos_Type.__name__ = "Unsigned32"
_AcSysNqmHistoryLqMos_Object = MibTableColumn
acSysNqmHistoryLqMos = _AcSysNqmHistoryLqMos_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 2, 12, 1, 1, 13),
    _AcSysNqmHistoryLqMos_Type()
)
acSysNqmHistoryLqMos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSysNqmHistoryLqMos.setStatus("current")
_AcSysDataStatus_ObjectIdentity = ObjectIdentity
acSysDataStatus = _AcSysDataStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 2, 13)
)
_AcSysDataStatusFirewallTCPConnections_Type = Unsigned32
_AcSysDataStatusFirewallTCPConnections_Object = MibScalar
acSysDataStatusFirewallTCPConnections = _AcSysDataStatusFirewallTCPConnections_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 2, 13, 1),
    _AcSysDataStatusFirewallTCPConnections_Type()
)
acSysDataStatusFirewallTCPConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSysDataStatusFirewallTCPConnections.setStatus("current")
_AcSysDataStatusFirewallUDPConnections_Type = Unsigned32
_AcSysDataStatusFirewallUDPConnections_Object = MibScalar
acSysDataStatusFirewallUDPConnections = _AcSysDataStatusFirewallUDPConnections_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 2, 13, 2),
    _AcSysDataStatusFirewallUDPConnections_Type()
)
acSysDataStatusFirewallUDPConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSysDataStatusFirewallUDPConnections.setStatus("current")
_AcSysDataStatusFirewallICMPConnections_Type = Unsigned32
_AcSysDataStatusFirewallICMPConnections_Object = MibScalar
acSysDataStatusFirewallICMPConnections = _AcSysDataStatusFirewallICMPConnections_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 2, 13, 3),
    _AcSysDataStatusFirewallICMPConnections_Type()
)
acSysDataStatusFirewallICMPConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSysDataStatusFirewallICMPConnections.setStatus("current")
_AcSysDataStatusFirewallIGMPConnections_Type = Unsigned32
_AcSysDataStatusFirewallIGMPConnections_Object = MibScalar
acSysDataStatusFirewallIGMPConnections = _AcSysDataStatusFirewallIGMPConnections_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 2, 13, 4),
    _AcSysDataStatusFirewallIGMPConnections_Type()
)
acSysDataStatusFirewallIGMPConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSysDataStatusFirewallIGMPConnections.setStatus("current")
_AcSysInventory_ObjectIdentity = ObjectIdentity
acSysInventory = _AcSysInventory_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 2, 14)
)


class _AcSysInventoryChassis_Type(SnmpAdminString):
    """Custom type acSysInventoryChassis based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_AcSysInventoryChassis_Type.__name__ = "SnmpAdminString"
_AcSysInventoryChassis_Object = MibScalar
acSysInventoryChassis = _AcSysInventoryChassis_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 2, 14, 1),
    _AcSysInventoryChassis_Type()
)
acSysInventoryChassis.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSysInventoryChassis.setStatus("current")


class _AcSysInventoryCPU_Type(SnmpAdminString):
    """Custom type acSysInventoryCPU based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_AcSysInventoryCPU_Type.__name__ = "SnmpAdminString"
_AcSysInventoryCPU_Object = MibScalar
acSysInventoryCPU = _AcSysInventoryCPU_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 2, 14, 2),
    _AcSysInventoryCPU_Type()
)
acSysInventoryCPU.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSysInventoryCPU.setStatus("current")


class _AcSysInventoryMemory_Type(SnmpAdminString):
    """Custom type acSysInventoryMemory based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_AcSysInventoryMemory_Type.__name__ = "SnmpAdminString"
_AcSysInventoryMemory_Object = MibScalar
acSysInventoryMemory = _AcSysInventoryMemory_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 2, 14, 3),
    _AcSysInventoryMemory_Type()
)
acSysInventoryMemory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSysInventoryMemory.setStatus("current")


class _AcSysInventoryNetworkCards_Type(SnmpAdminString):
    """Custom type acSysInventoryNetworkCards based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 1024),
    )


_AcSysInventoryNetworkCards_Type.__name__ = "SnmpAdminString"
_AcSysInventoryNetworkCards_Object = MibScalar
acSysInventoryNetworkCards = _AcSysInventoryNetworkCards_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 2, 14, 4),
    _AcSysInventoryNetworkCards_Type()
)
acSysInventoryNetworkCards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSysInventoryNetworkCards.setStatus("current")


class _AcSysInventoryVirtualEnvironment_Type(SnmpAdminString):
    """Custom type acSysInventoryVirtualEnvironment based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_AcSysInventoryVirtualEnvironment_Type.__name__ = "SnmpAdminString"
_AcSysInventoryVirtualEnvironment_Object = MibScalar
acSysInventoryVirtualEnvironment = _AcSysInventoryVirtualEnvironment_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 2, 14, 5),
    _AcSysInventoryVirtualEnvironment_Type()
)
acSysInventoryVirtualEnvironment.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSysInventoryVirtualEnvironment.setStatus("current")
_AcSystemAction_ObjectIdentity = ObjectIdentity
acSystemAction = _AcSystemAction_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 3)
)
_AcSysAction_ObjectIdentity = ObjectIdentity
acSysAction = _AcSysAction_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 3, 1)
)
_AcSysActionSet_ObjectIdentity = ObjectIdentity
acSysActionSet = _AcSysActionSet_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 3, 1, 1)
)


class _AcSysActionSetReset_Type(Unsigned32):
    """Custom type acSysActionSetReset based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_AcSysActionSetReset_Type.__name__ = "Unsigned32"
_AcSysActionSetReset_Object = MibScalar
acSysActionSetReset = _AcSysActionSetReset_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 3, 1, 1, 1),
    _AcSysActionSetReset_Type()
)
acSysActionSetReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acSysActionSetReset.setStatus("current")


class _AcSysActionSetResetControl_Type(Integer32):
    """Custom type acSysActionSetResetControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("resetFromFlashAfterBurn", 1),
          ("resetFromFlashNoBurn", 2),
          ("resetFromBootP", 3))
    )


_AcSysActionSetResetControl_Type.__name__ = "Integer32"
_AcSysActionSetResetControl_Object = MibScalar
acSysActionSetResetControl = _AcSysActionSetResetControl_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 3, 1, 1, 2),
    _AcSysActionSetResetControl_Type()
)
acSysActionSetResetControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acSysActionSetResetControl.setStatus("current")


class _AcSysActionSetDefaults_Type(Unsigned32):
    """Custom type acSysActionSetDefaults based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_AcSysActionSetDefaults_Type.__name__ = "Unsigned32"
_AcSysActionSetDefaults_Object = MibScalar
acSysActionSetDefaults = _AcSysActionSetDefaults_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 3, 1, 1, 3),
    _AcSysActionSetDefaults_Type()
)
acSysActionSetDefaults.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acSysActionSetDefaults.setStatus("current")


class _AcSysActionSetSaveConfig_Type(Unsigned32):
    """Custom type acSysActionSetSaveConfig based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_AcSysActionSetSaveConfig_Type.__name__ = "Unsigned32"
_AcSysActionSetSaveConfig_Object = MibScalar
acSysActionSetSaveConfig = _AcSysActionSetSaveConfig_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 3, 1, 1, 4),
    _AcSysActionSetSaveConfig_Type()
)
acSysActionSetSaveConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acSysActionSetSaveConfig.setStatus("current")


class _AcSysActionSetAutoUpdate_Type(Unsigned32):
    """Custom type acSysActionSetAutoUpdate based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_AcSysActionSetAutoUpdate_Type.__name__ = "Unsigned32"
_AcSysActionSetAutoUpdate_Object = MibScalar
acSysActionSetAutoUpdate = _AcSysActionSetAutoUpdate_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 3, 1, 1, 5),
    _AcSysActionSetAutoUpdate_Type()
)
acSysActionSetAutoUpdate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acSysActionSetAutoUpdate.setStatus("current")


class _AcSysActionSetGetTimeFromNTPServer_Type(Unsigned32):
    """Custom type acSysActionSetGetTimeFromNTPServer based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_AcSysActionSetGetTimeFromNTPServer_Type.__name__ = "Unsigned32"
_AcSysActionSetGetTimeFromNTPServer_Object = MibScalar
acSysActionSetGetTimeFromNTPServer = _AcSysActionSetGetTimeFromNTPServer_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 3, 1, 1, 6),
    _AcSysActionSetGetTimeFromNTPServer_Type()
)
acSysActionSetGetTimeFromNTPServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acSysActionSetGetTimeFromNTPServer.setStatus("current")


class _AcSysActionSetSwUpgrade_Type(Integer32):
    """Custom type acSysActionSetSwUpgrade based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("hitLessUpGrade", 1),
          ("systemResetUpGrade", 2))
    )


_AcSysActionSetSwUpgrade_Type.__name__ = "Integer32"
_AcSysActionSetSwUpgrade_Object = MibScalar
acSysActionSetSwUpgrade = _AcSysActionSetSwUpgrade_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 3, 1, 1, 7),
    _AcSysActionSetSwUpgrade_Type()
)
acSysActionSetSwUpgrade.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acSysActionSetSwUpgrade.setStatus("current")


class _AcSysActionSetOnLineChangesApply_Type(Integer32):
    """Custom type acSysActionSetOnLineChangesApply based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("defaultValue", 0),
          ("applyChanges", 1))
    )


_AcSysActionSetOnLineChangesApply_Type.__name__ = "Integer32"
_AcSysActionSetOnLineChangesApply_Object = MibScalar
acSysActionSetOnLineChangesApply = _AcSysActionSetOnLineChangesApply_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 3, 1, 1, 8),
    _AcSysActionSetOnLineChangesApply_Type()
)
acSysActionSetOnLineChangesApply.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acSysActionSetOnLineChangesApply.setStatus("current")


class _AcSysActionSetIPSecTLSUpgrade_Type(Integer32):
    """Custom type acSysActionSetIPSecTLSUpgrade based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("defaultValue", 0),
          ("upDateChanges", 1))
    )


_AcSysActionSetIPSecTLSUpgrade_Type.__name__ = "Integer32"
_AcSysActionSetIPSecTLSUpgrade_Object = MibScalar
acSysActionSetIPSecTLSUpgrade = _AcSysActionSetIPSecTLSUpgrade_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 3, 1, 1, 9),
    _AcSysActionSetIPSecTLSUpgrade_Type()
)
acSysActionSetIPSecTLSUpgrade.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acSysActionSetIPSecTLSUpgrade.setStatus("obsolete")


class _AcSysActionSetGWAppTLSUpgrade_Type(Integer32):
    """Custom type acSysActionSetGWAppTLSUpgrade based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("defaultValue", 0),
          ("upDateChanges", 1))
    )


_AcSysActionSetGWAppTLSUpgrade_Type.__name__ = "Integer32"
_AcSysActionSetGWAppTLSUpgrade_Object = MibScalar
acSysActionSetGWAppTLSUpgrade = _AcSysActionSetGWAppTLSUpgrade_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 3, 1, 1, 10),
    _AcSysActionSetGWAppTLSUpgrade_Type()
)
acSysActionSetGWAppTLSUpgrade.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acSysActionSetGWAppTLSUpgrade.setStatus("current")


class _AcSysActionSetConvertNetworkIFsConfiguration_Type(Integer32):
    """Custom type acSysActionSetConvertNetworkIFsConfiguration based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("defaultValue", 0),
          ("convertAction", 1))
    )


_AcSysActionSetConvertNetworkIFsConfiguration_Type.__name__ = "Integer32"
_AcSysActionSetConvertNetworkIFsConfiguration_Object = MibScalar
acSysActionSetConvertNetworkIFsConfiguration = _AcSysActionSetConvertNetworkIFsConfiguration_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 3, 1, 1, 11),
    _AcSysActionSetConvertNetworkIFsConfiguration_Type()
)
acSysActionSetConvertNetworkIFsConfiguration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acSysActionSetConvertNetworkIFsConfiguration.setStatus("current")


class _AcSysActionSetActionId_Type(Unsigned32):
    """Custom type acSysActionSetActionId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AcSysActionSetActionId_Type.__name__ = "Unsigned32"
_AcSysActionSetActionId_Object = MibScalar
acSysActionSetActionId = _AcSysActionSetActionId_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 3, 1, 1, 12),
    _AcSysActionSetActionId_Type()
)
acSysActionSetActionId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acSysActionSetActionId.setStatus("current")


class _AcSysActionSetAutoUpdateActionResult_Type(SnmpAdminString):
    """Custom type acSysActionSetAutoUpdateActionResult based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 200),
    )


_AcSysActionSetAutoUpdateActionResult_Type.__name__ = "SnmpAdminString"
_AcSysActionSetAutoUpdateActionResult_Object = MibScalar
acSysActionSetAutoUpdateActionResult = _AcSysActionSetAutoUpdateActionResult_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 3, 1, 1, 13),
    _AcSysActionSetAutoUpdateActionResult_Type()
)
acSysActionSetAutoUpdateActionResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSysActionSetAutoUpdateActionResult.setStatus("current")


class _AcSysActionSetApplyINImethod_Type(Integer32):
    """Custom type acSysActionSetApplyINImethod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("applyAfterReset", 0),
          ("applyImmediate", 1))
    )


_AcSysActionSetApplyINImethod_Type.__name__ = "Integer32"
_AcSysActionSetApplyINImethod_Object = MibScalar
acSysActionSetApplyINImethod = _AcSysActionSetApplyINImethod_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 3, 1, 1, 14),
    _AcSysActionSetApplyINImethod_Type()
)
acSysActionSetApplyINImethod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acSysActionSetApplyINImethod.setStatus("current")


class _AcSysActionSetLicensePoolUpdate_Type(Integer32):
    """Custom type acSysActionSetLicensePoolUpdate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("unset", 0),
          ("newPool", 1))
    )


_AcSysActionSetLicensePoolUpdate_Type.__name__ = "Integer32"
_AcSysActionSetLicensePoolUpdate_Object = MibScalar
acSysActionSetLicensePoolUpdate = _AcSysActionSetLicensePoolUpdate_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 3, 1, 1, 15),
    _AcSysActionSetLicensePoolUpdate_Type()
)
acSysActionSetLicensePoolUpdate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acSysActionSetLicensePoolUpdate.setStatus("current")


class _AcSysActionSetAupdNetworkSource_Type(SnmpAdminString):
    """Custom type acSysActionSetAupdNetworkSource based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 100),
    )


_AcSysActionSetAupdNetworkSource_Type.__name__ = "SnmpAdminString"
_AcSysActionSetAupdNetworkSource_Object = MibScalar
acSysActionSetAupdNetworkSource = _AcSysActionSetAupdNetworkSource_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 3, 1, 1, 16),
    _AcSysActionSetAupdNetworkSource_Type()
)
acSysActionSetAupdNetworkSource.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acSysActionSetAupdNetworkSource.setStatus("current")


class _AcSysActionSetLicensePoolHitless_Type(Integer32):
    """Custom type acSysActionSetLicensePoolHitless based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("unset", 0),
          ("hitlessApply", 1))
    )


_AcSysActionSetLicensePoolHitless_Type.__name__ = "Integer32"
_AcSysActionSetLicensePoolHitless_Object = MibScalar
acSysActionSetLicensePoolHitless = _AcSysActionSetLicensePoolHitless_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 3, 1, 1, 17),
    _AcSysActionSetLicensePoolHitless_Type()
)
acSysActionSetLicensePoolHitless.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acSysActionSetLicensePoolHitless.setStatus("current")


class _AcSysActionSetLicensePoolRefreshRequest_Type(Integer32):
    """Custom type acSysActionSetLicensePoolRefreshRequest based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("noRequest", 0),
          ("request", 1))
    )


_AcSysActionSetLicensePoolRefreshRequest_Type.__name__ = "Integer32"
_AcSysActionSetLicensePoolRefreshRequest_Object = MibScalar
acSysActionSetLicensePoolRefreshRequest = _AcSysActionSetLicensePoolRefreshRequest_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 3, 1, 1, 18),
    _AcSysActionSetLicensePoolRefreshRequest_Type()
)
acSysActionSetLicensePoolRefreshRequest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acSysActionSetLicensePoolRefreshRequest.setStatus("current")
_AcSysActionAdmin_ObjectIdentity = ObjectIdentity
acSysActionAdmin = _AcSysActionAdmin_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 3, 1, 2)
)


class _AcSysActionAdminState_Type(Integer32):
    """Custom type acSysActionAdminState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("locked", 0),
          ("shuttingDown", 1),
          ("unlocked", 2))
    )


_AcSysActionAdminState_Type.__name__ = "Integer32"
_AcSysActionAdminState_Object = MibScalar
acSysActionAdminState = _AcSysActionAdminState_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 3, 1, 2, 1),
    _AcSysActionAdminState_Type()
)
acSysActionAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acSysActionAdminState.setStatus("current")


class _AcSysActionAdminStateLockTimeout_Type(Integer32):
    """Custom type acSysActionAdminStateLockTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 32768),
    )


_AcSysActionAdminStateLockTimeout_Type.__name__ = "Integer32"
_AcSysActionAdminStateLockTimeout_Object = MibScalar
acSysActionAdminStateLockTimeout = _AcSysActionAdminStateLockTimeout_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 3, 1, 2, 2),
    _AcSysActionAdminStateLockTimeout_Type()
)
acSysActionAdminStateLockTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acSysActionAdminStateLockTimeout.setStatus("current")
_AcSysUpload_ObjectIdentity = ObjectIdentity
acSysUpload = _AcSysUpload_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 3, 1, 3)
)


class _AcSysUploadActionType_Type(Integer32):
    """Custom type acSysUploadActionType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              10)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("upload", 1),
          ("remove", 2),
          ("actionDone", 10))
    )


_AcSysUploadActionType_Type.__name__ = "Integer32"
_AcSysUploadActionType_Object = MibScalar
acSysUploadActionType = _AcSysUploadActionType_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 3, 1, 3, 1),
    _AcSysUploadActionType_Type()
)
acSysUploadActionType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acSysUploadActionType.setStatus("current")


class _AcSysUploadFileType_Type(Integer32):
    """Custom type acSysUploadFileType based on Integer32"""
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
              22)
        )
    )
    namedValues = NamedValues(
        *(("iniFile", 1),
          ("cptFile", 2),
          ("vpFile", 3),
          ("prerecordedTonesFile", 4),
          ("fxsCoeffFile", 5),
          ("fxoCoeffFile", 6),
          ("casFile", 7),
          ("xmlFile", 8),
          ("externalCoderFile", 9),
          ("userInfoFile", 10),
          ("dialPlanFile", 11),
          ("tlsPKeyFile", 12),
          ("tlsCertFile", 13),
          ("tlsRootFile", 14),
          ("videoFontFile", 15),
          ("v5PortFile", 16),
          ("dataConfigurationFile", 17),
          ("amdSensitivityFile", 18),
          ("debugFile", 19),
          ("cliScriptFile", 20),
          ("cliScriptLogFile", 21),
          ("configurationPackageFile", 22))
    )


_AcSysUploadFileType_Type.__name__ = "Integer32"
_AcSysUploadFileType_Object = MibScalar
acSysUploadFileType = _AcSysUploadFileType_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 3, 1, 3, 2),
    _AcSysUploadFileType_Type()
)
acSysUploadFileType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acSysUploadFileType.setStatus("current")


class _AcSysUploadFileNumber_Type(Integer32):
    """Custom type acSysUploadFileNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 7),
    )


_AcSysUploadFileNumber_Type.__name__ = "Integer32"
_AcSysUploadFileNumber_Object = MibScalar
acSysUploadFileNumber = _AcSysUploadFileNumber_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 3, 1, 3, 3),
    _AcSysUploadFileNumber_Type()
)
acSysUploadFileNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acSysUploadFileNumber.setStatus("current")


class _AcSysUploadFileURI_Type(SnmpAdminString):
    """Custom type acSysUploadFileURI based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 512),
    )


_AcSysUploadFileURI_Type.__name__ = "SnmpAdminString"
_AcSysUploadFileURI_Object = MibScalar
acSysUploadFileURI = _AcSysUploadFileURI_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 3, 1, 3, 4),
    _AcSysUploadFileURI_Type()
)
acSysUploadFileURI.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acSysUploadFileURI.setStatus("current")


class _AcSysUploadActionID_Type(Unsigned32):
    """Custom type acSysUploadActionID based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AcSysUploadActionID_Type.__name__ = "Unsigned32"
_AcSysUploadActionID_Object = MibScalar
acSysUploadActionID = _AcSysUploadActionID_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 3, 1, 3, 5),
    _AcSysUploadActionID_Type()
)
acSysUploadActionID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acSysUploadActionID.setStatus("current")


class _AcSysUploadActionResult_Type(SnmpAdminString):
    """Custom type acSysUploadActionResult based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_AcSysUploadActionResult_Type.__name__ = "SnmpAdminString"
_AcSysUploadActionResult_Object = MibScalar
acSysUploadActionResult = _AcSysUploadActionResult_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 3, 1, 3, 6),
    _AcSysUploadActionResult_Type()
)
acSysUploadActionResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSysUploadActionResult.setStatus("current")
_AcSysMcUpgrade_ObjectIdentity = ObjectIdentity
acSysMcUpgrade = _AcSysMcUpgrade_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 3, 1, 4)
)


class _AcSysMcUpgradeActionType_Type(Integer32):
    """Custom type acSysMcUpgradeActionType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", -1),
          ("immediateUpgrade", 0),
          ("hitlessUpgrade", 1),
          ("stopHitlessUpgrade", 2))
    )


_AcSysMcUpgradeActionType_Type.__name__ = "Integer32"
_AcSysMcUpgradeActionType_Object = MibScalar
acSysMcUpgradeActionType = _AcSysMcUpgradeActionType_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 3, 1, 4, 1),
    _AcSysMcUpgradeActionType_Type()
)
acSysMcUpgradeActionType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acSysMcUpgradeActionType.setStatus("current")


class _AcSysMcUpgradeMcType_Type(SnmpAdminString):
    """Custom type acSysMcUpgradeMcType based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_AcSysMcUpgradeMcType_Type.__name__ = "SnmpAdminString"
_AcSysMcUpgradeMcType_Object = MibScalar
acSysMcUpgradeMcType = _AcSysMcUpgradeMcType_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 3, 1, 4, 2),
    _AcSysMcUpgradeMcType_Type()
)
acSysMcUpgradeMcType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSysMcUpgradeMcType.setStatus("current")


class _AcSysMcUpgradeGracefulTimeout_Type(Unsigned32):
    """Custom type acSysMcUpgradeGracefulTimeout based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2000000),
    )


_AcSysMcUpgradeGracefulTimeout_Type.__name__ = "Unsigned32"
_AcSysMcUpgradeGracefulTimeout_Object = MibScalar
acSysMcUpgradeGracefulTimeout = _AcSysMcUpgradeGracefulTimeout_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 3, 1, 4, 3),
    _AcSysMcUpgradeGracefulTimeout_Type()
)
acSysMcUpgradeGracefulTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acSysMcUpgradeGracefulTimeout.setStatus("current")


class _AcSysMcUpgradeActionID_Type(Unsigned32):
    """Custom type acSysMcUpgradeActionID based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AcSysMcUpgradeActionID_Type.__name__ = "Unsigned32"
_AcSysMcUpgradeActionID_Object = MibScalar
acSysMcUpgradeActionID = _AcSysMcUpgradeActionID_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 3, 1, 4, 4),
    _AcSysMcUpgradeActionID_Type()
)
acSysMcUpgradeActionID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acSysMcUpgradeActionID.setStatus("current")


class _AcSysMcUpgradeActionResult_Type(SnmpAdminString):
    """Custom type acSysMcUpgradeActionResult based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_AcSysMcUpgradeActionResult_Type.__name__ = "SnmpAdminString"
_AcSysMcUpgradeActionResult_Object = MibScalar
acSysMcUpgradeActionResult = _AcSysMcUpgradeActionResult_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 3, 1, 4, 5),
    _AcSysMcUpgradeActionResult_Type()
)
acSysMcUpgradeActionResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSysMcUpgradeActionResult.setStatus("current")
_AcSysConfigurationPackageChecksum_ObjectIdentity = ObjectIdentity
acSysConfigurationPackageChecksum = _AcSysConfigurationPackageChecksum_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 3, 1, 5)
)


class _AcSysConfigurationPackageChecksumActionType_Type(Integer32):
    """Custom type acSysConfigurationPackageChecksumActionType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              10)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("calculate", 1),
          ("actionDone", 10))
    )


_AcSysConfigurationPackageChecksumActionType_Type.__name__ = "Integer32"
_AcSysConfigurationPackageChecksumActionType_Object = MibScalar
acSysConfigurationPackageChecksumActionType = _AcSysConfigurationPackageChecksumActionType_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 3, 1, 5, 1),
    _AcSysConfigurationPackageChecksumActionType_Type()
)
acSysConfigurationPackageChecksumActionType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acSysConfigurationPackageChecksumActionType.setStatus("current")


class _AcSysConfigurationPackageChecksumActionID_Type(Unsigned32):
    """Custom type acSysConfigurationPackageChecksumActionID based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AcSysConfigurationPackageChecksumActionID_Type.__name__ = "Unsigned32"
_AcSysConfigurationPackageChecksumActionID_Object = MibScalar
acSysConfigurationPackageChecksumActionID = _AcSysConfigurationPackageChecksumActionID_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 3, 1, 5, 2),
    _AcSysConfigurationPackageChecksumActionID_Type()
)
acSysConfigurationPackageChecksumActionID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acSysConfigurationPackageChecksumActionID.setStatus("current")


class _AcSysConfigurationPackageChecksumActionResult_Type(SnmpAdminString):
    """Custom type acSysConfigurationPackageChecksumActionResult based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_AcSysConfigurationPackageChecksumActionResult_Type.__name__ = "SnmpAdminString"
_AcSysConfigurationPackageChecksumActionResult_Object = MibScalar
acSysConfigurationPackageChecksumActionResult = _AcSysConfigurationPackageChecksumActionResult_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 3, 1, 5, 3),
    _AcSysConfigurationPackageChecksumActionResult_Type()
)
acSysConfigurationPackageChecksumActionResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSysConfigurationPackageChecksumActionResult.setStatus("current")


class _AcSysConfigurationPackageChecksumValue_Type(SnmpAdminString):
    """Custom type acSysConfigurationPackageChecksumValue based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_AcSysConfigurationPackageChecksumValue_Type.__name__ = "SnmpAdminString"
_AcSysConfigurationPackageChecksumValue_Object = MibScalar
acSysConfigurationPackageChecksumValue = _AcSysConfigurationPackageChecksumValue_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 3, 1, 5, 4),
    _AcSysConfigurationPackageChecksumValue_Type()
)
acSysConfigurationPackageChecksumValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSysConfigurationPackageChecksumValue.setStatus("current")
_AcSystemChassis_ObjectIdentity = ObjectIdentity
acSystemChassis = _AcSystemChassis_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 4)
)


class _AcSystemChassisDryContactsOutStatus_Type(Bits):
    """Custom type acSystemChassisDryContactsOutStatus based on Bits"""
    namedValues = NamedValues(
        *(("noAlarm", 0),
          ("criticalAlarm", 1),
          ("majorAlarm", 2),
          ("minorAlarm", 3))
    )

_AcSystemChassisDryContactsOutStatus_Type.__name__ = "Bits"
_AcSystemChassisDryContactsOutStatus_Object = MibScalar
acSystemChassisDryContactsOutStatus = _AcSystemChassisDryContactsOutStatus_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 4, 1),
    _AcSystemChassisDryContactsOutStatus_Type()
)
acSystemChassisDryContactsOutStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSystemChassisDryContactsOutStatus.setStatus("current")


class _AcSystemChassisDryContactsInStatus_Type(Bits):
    """Custom type acSystemChassisDryContactsInStatus based on Bits"""
    namedValues = NamedValues(
        *(("noAlarm", 0),
          ("alarm1", 1))
    )

_AcSystemChassisDryContactsInStatus_Type.__name__ = "Bits"
_AcSystemChassisDryContactsInStatus_Object = MibScalar
acSystemChassisDryContactsInStatus = _AcSystemChassisDryContactsInStatus_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 4, 2),
    _AcSystemChassisDryContactsInStatus_Type()
)
acSystemChassisDryContactsInStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSystemChassisDryContactsInStatus.setStatus("current")


class _AcSystemChassisLastChanged_Type(Unsigned32):
    """Custom type acSystemChassisLastChanged based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_AcSystemChassisLastChanged_Type.__name__ = "Unsigned32"
_AcSystemChassisLastChanged_Object = MibScalar
acSystemChassisLastChanged = _AcSystemChassisLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 4, 3),
    _AcSystemChassisLastChanged_Type()
)
acSystemChassisLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSystemChassisLastChanged.setStatus("current")
_AcSysModuleTable_Object = MibTable
acSysModuleTable = _AcSysModuleTable_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 4, 21)
)
if mibBuilder.loadTexts:
    acSysModuleTable.setStatus("current")
_AcSysModuleEntry_Object = MibTableRow
acSysModuleEntry = _AcSysModuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 4, 21, 1)
)
acSysModuleEntry.setIndexNames(
    (0, "AC-SYSTEM-MIB", "acSysModuleIndex"),
)
if mibBuilder.loadTexts:
    acSysModuleEntry.setStatus("current")


class _AcSysModuleIndex_Type(Unsigned32):
    """Custom type acSysModuleIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_AcSysModuleIndex_Type.__name__ = "Unsigned32"
_AcSysModuleIndex_Object = MibTableColumn
acSysModuleIndex = _AcSysModuleIndex_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 4, 21, 1, 1),
    _AcSysModuleIndex_Type()
)
acSysModuleIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    acSysModuleIndex.setStatus("current")


class _AcSysModuleGeographicalPosition_Type(Unsigned32):
    """Custom type acSysModuleGeographicalPosition based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 12),
    )


_AcSysModuleGeographicalPosition_Type.__name__ = "Unsigned32"
_AcSysModuleGeographicalPosition_Object = MibTableColumn
acSysModuleGeographicalPosition = _AcSysModuleGeographicalPosition_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 4, 21, 1, 2),
    _AcSysModuleGeographicalPosition_Type()
)
acSysModuleGeographicalPosition.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSysModuleGeographicalPosition.setStatus("current")


class _AcSysModuleType_Type(Integer32):
    """Custom type acSysModuleType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              20,
              22,
              23,
              24,
              25,
              26,
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
              79,
              80,
              81,
              82,
              83,
              84,
              85,
              250,
              251,
              252,
              253,
              254,
              255,
              256,
              257,
              258,
              259,
              260,
              261,
              262,
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
              275,
              276,
              277,
              278,
              279,
              280,
              281,
              282,
              283,
              284,
              285,
              286,
              287,
              288,
              289,
              290,
              291,
              292,
              293,
              294,
              295,
              296,
              297,
              298,
              299,
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
              313)
        )
    )
    namedValues = NamedValues(
        *(("acUnknown", 0),
          ("acTrunkPack-08", 1),
          ("acMediaPack-108", 2),
          ("acMediaPack-124", 3),
          ("acTrunkPack-1600", 20),
          ("acTPM1100", 22),
          ("acTrunkPack-260-IpMedia", 23),
          ("acTrunkPack-1610", 24),
          ("acMediaPack-104", 25),
          ("acMediaPack-102", 26),
          ("acTrunkPack-1610-SB", 29),
          ("acTrunkPack-1610-IpMedia", 30),
          ("acTrunkPack-MEDIANT2000", 31),
          ("acTrunkPack-STRETTO2000", 32),
          ("acTrunkPack-IPMServer2000", 33),
          ("acTrunkPack-2810", 34),
          ("acTrunkPack-260-UN-IpMedia", 35),
          ("acTrunkPack-260-IpMedia-30Ch", 36),
          ("acTrunkPack-260-IpMedia-60Ch", 37),
          ("acTrunkPack-260-IpMedia-120Ch", 38),
          ("acTrunkPack-260RT-IpMedia-30Ch", 39),
          ("acTrunkPack-260RT-IpMedia-60Ch", 40),
          ("acTrunkPack-260RT-IpMedia-120Ch", 41),
          ("acTrunkPack-260", 42),
          ("acTrunkPack-260-UN", 43),
          ("acTPM1100-PCM", 44),
          ("acTrunkPack-6310", 45),
          ("acTPM6300", 46),
          ("acMediant1000", 47),
          ("acIPMedia3000", 48),
          ("acMediant3000", 49),
          ("acStretto3000", 50),
          ("acTrunkPack-6310-IpMedia", 51),
          ("acTrunkPack-6310-SB", 52),
          ("acATP-1610", 53),
          ("acATP-260", 54),
          ("acATP-260-UN", 55),
          ("acMediaPack-118", 56),
          ("acMediaPack114", 57),
          ("acMediaPack112", 58),
          ("acTrunkPack-6310-T3", 59),
          ("acMediant3000-T3", 60),
          ("acIPmedia3000-T3", 61),
          ("acTrunkPack-6310-T3-IpMedia", 62),
          ("acTrunkPack-8410", 63),
          ("acTrunkPack-8410-IpMedia", 64),
          ("acMediant-800-MSBR", 69),
          ("acMediant-4000", 70),
          ("acMediant-1000-ESBC", 71),
          ("acMediaPack-500-ESBC", 72),
          ("acMediantSW", 73),
          ("acMediant-800B-MSBG", 74),
          ("acMediant-800B-ESBC", 75),
          ("acMediant-500-MSBG", 76),
          ("acMediant-500-ESBC", 77),
          ("acMediant-2600", 78),
          ("acMediant-VE-SBC", 79),
          ("acMediant-VE-H-SBC", 80),
          ("acMediant-SE-SBC", 81),
          ("acMediant-SE-H-SBC", 82),
          ("acMediant-9000-SBC", 83),
          ("acMediant-500L-MSBR", 84),
          ("acMediant-500L-ESBC", 85),
          ("sA1", 250),
          ("sA2", 251),
          ("sA3", 252),
          ("acMediant1000CPUmodule", 253),
          ("acMediant1000IFDigitalModule", 254),
          ("acMediant1000IFAnalogModule", 255),
          ("acMediant1000IFBRIModule", 256),
          ("acMediant1000IPMediaModule", 257),
          ("acMediant600CPUmodule", 258),
          ("acMediant600IFDigitalModule", 259),
          ("acMediant600IFAnalogModule", 260),
          ("acMediant600IFBRIModule", 261),
          ("acMediant600IPMediaModule", 262),
          ("acMediant800CPUmodule", 265),
          ("acMediant800IFDigitalModule", 266),
          ("acMediant800IFAnalogModule", 267),
          ("acMediant800IFBRIModule", 268),
          ("acMediant800IFWANModule", 269),
          ("acMediant800IFWiFiModule", 270),
          ("acMediant800IPMediaModule", 271),
          ("acMediant800EthernetModule", 272),
          ("acMediant800IFT1WANModule", 273),
          ("acMediant800IFSHDSLModule", 274),
          ("acMediant800IFADSLModule", 275),
          ("acMediant1000IFWANModule", 276),
          ("acMediant1000IFT1WANModule", 277),
          ("acMediant1000IFSHDSLModule", 278),
          ("acMediant1000IFADSLModule", 279),
          ("acMediant4000CPUmodule", 280),
          ("acMediant1000EthernetModule", 281),
          ("acSWESBCModule", 282),
          ("acMediant500CPUmodule", 283),
          ("acMediant500IFDigitalModule", 284),
          ("acMediant500IFAnalogModule", 285),
          ("acMediant500IFBRIModule", 286),
          ("acMediant500IFWANModule", 287),
          ("acMediant500IFWiFiModule", 288),
          ("acMediant500IPMediaModule", 289),
          ("acMediant500EthernetModule", 290),
          ("acMediant500IFT1WANModule", 291),
          ("acMediant500IFSHDSLModule", 292),
          ("acMediant500IFADSLModule", 293),
          ("acMediant500IFGESFPModule", 294),
          ("acMediant4000MPModule", 295),
          ("acMediant-800B-MSBR", 296),
          ("acMediant800BCPUmodule", 297),
          ("acMediant800BIFDigitalModule", 298),
          ("acMediant800BIFAnalogModule", 299),
          ("acMediant800BIFBRIModule", 300),
          ("acMediant800BIFWANModule", 301),
          ("acMediant800BIFWiFiModule", 302),
          ("acMediant800BIPMediaModule", 303),
          ("acMediant800BEthernetModule", 304),
          ("acMediant800BIFT1WANModule", 305),
          ("acMediant800BIFSHDSLModule", 306),
          ("acMediant800BIFADSLModule", 307),
          ("acMediant2600CPUmodule", 308),
          ("acMediant2600MPModule", 309),
          ("acMediaPack1288CPUmodule", 310),
          ("acMediaPack1288FXSAnalogModule", 311),
          ("acMediant3100CPUModule", 312),
          ("acMediant3100IFDigitalModule", 313))
    )


_AcSysModuleType_Type.__name__ = "Integer32"
_AcSysModuleType_Object = MibTableColumn
acSysModuleType = _AcSysModuleType_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 4, 21, 1, 3),
    _AcSysModuleType_Type()
)
acSysModuleType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSysModuleType.setStatus("current")


class _AcSysModulePresence_Type(Integer32):
    """Custom type acSysModulePresence based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("present", 1),
          ("missing", 2))
    )


_AcSysModulePresence_Type.__name__ = "Integer32"
_AcSysModulePresence_Object = MibTableColumn
acSysModulePresence = _AcSysModulePresence_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 4, 21, 1, 4),
    _AcSysModulePresence_Type()
)
acSysModulePresence.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSysModulePresence.setStatus("current")


class _AcSysModuleLicenseKeyList_Type(SnmpAdminString):
    """Custom type acSysModuleLicenseKeyList based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 1400),
    )


_AcSysModuleLicenseKeyList_Type.__name__ = "SnmpAdminString"
_AcSysModuleLicenseKeyList_Object = MibTableColumn
acSysModuleLicenseKeyList = _AcSysModuleLicenseKeyList_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 4, 21, 1, 5),
    _AcSysModuleLicenseKeyList_Type()
)
acSysModuleLicenseKeyList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSysModuleLicenseKeyList.setStatus("current")


class _AcSysModuleSerialNumber_Type(Integer32):
    """Custom type acSysModuleSerialNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_AcSysModuleSerialNumber_Type.__name__ = "Integer32"
_AcSysModuleSerialNumber_Object = MibTableColumn
acSysModuleSerialNumber = _AcSysModuleSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 4, 21, 1, 6),
    _AcSysModuleSerialNumber_Type()
)
acSysModuleSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSysModuleSerialNumber.setStatus("current")


class _AcSysModuleSWVersion_Type(SnmpAdminString):
    """Custom type acSysModuleSWVersion based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_AcSysModuleSWVersion_Type.__name__ = "SnmpAdminString"
_AcSysModuleSWVersion_Object = MibTableColumn
acSysModuleSWVersion = _AcSysModuleSWVersion_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 4, 21, 1, 7),
    _AcSysModuleSWVersion_Type()
)
acSysModuleSWVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSysModuleSWVersion.setStatus("current")


class _AcSysModuleOperationalState_Type(Integer32):
    """Custom type acSysModuleOperationalState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_AcSysModuleOperationalState_Type.__name__ = "Integer32"
_AcSysModuleOperationalState_Object = MibTableColumn
acSysModuleOperationalState = _AcSysModuleOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 4, 21, 1, 8),
    _AcSysModuleOperationalState_Type()
)
acSysModuleOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSysModuleOperationalState.setStatus("current")


class _AcSysModuleHAStatus_Type(Integer32):
    """Custom type acSysModuleHAStatus based on Integer32"""
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
        *(("acitveNonHA", 1),
          ("active", 2),
          ("redundant", 3),
          ("standAlone", 4),
          ("redundantNonHA", 5),
          ("notApplicable", 6))
    )


_AcSysModuleHAStatus_Type.__name__ = "Integer32"
_AcSysModuleHAStatus_Object = MibTableColumn
acSysModuleHAStatus = _AcSysModuleHAStatus_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 4, 21, 1, 9),
    _AcSysModuleHAStatus_Type()
)
acSysModuleHAStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSysModuleHAStatus.setStatus("current")


class _AcSysModuleLEDs_Type(OctetString):
    """Custom type acSysModuleLEDs based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 50),
    )


_AcSysModuleLEDs_Type.__name__ = "OctetString"
_AcSysModuleLEDs_Object = MibTableColumn
acSysModuleLEDs = _AcSysModuleLEDs_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 4, 21, 1, 10),
    _AcSysModuleLEDs_Type()
)
acSysModuleLEDs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSysModuleLEDs.setStatus("current")


class _AcSysModuleTemperature_Type(Integer32):
    """Custom type acSysModuleTemperature based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 100),
    )


_AcSysModuleTemperature_Type.__name__ = "Integer32"
_AcSysModuleTemperature_Object = MibTableColumn
acSysModuleTemperature = _AcSysModuleTemperature_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 4, 21, 1, 11),
    _AcSysModuleTemperature_Type()
)
acSysModuleTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSysModuleTemperature.setStatus("current")


class _AcSysModuleActions_Type(Integer32):
    """Custom type acSysModuleActions based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("reset", 1),
          ("switchOver", 2),
          ("actionDone", 3))
    )


_AcSysModuleActions_Type.__name__ = "Integer32"
_AcSysModuleActions_Object = MibTableColumn
acSysModuleActions = _AcSysModuleActions_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 4, 21, 1, 12),
    _AcSysModuleActions_Type()
)
acSysModuleActions.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acSysModuleActions.setStatus("current")


class _AcSysModuleFRUaction_Type(Integer32):
    """Custom type acSysModuleFRUaction based on Integer32"""
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
        *(("fruActionDone", 1),
          ("fruOutOfServiceAction", 2),
          ("fruBackToServiceAction", 3),
          ("fruNotApplicable", 4))
    )


_AcSysModuleFRUaction_Type.__name__ = "Integer32"
_AcSysModuleFRUaction_Object = MibTableColumn
acSysModuleFRUaction = _AcSysModuleFRUaction_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 4, 21, 1, 13),
    _AcSysModuleFRUaction_Type()
)
acSysModuleFRUaction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acSysModuleFRUaction.setStatus("current")


class _AcSysModuleFRUstatus_Type(Integer32):
    """Custom type acSysModuleFRUstatus based on Integer32"""
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
        *(("moduleNotExist", 1),
          ("moduleExistOk", 2),
          ("moduleOutOfService", 3),
          ("moduleBackToServiceStart", 4),
          ("moduleMismatch", 5),
          ("moduleFaulty", 6),
          ("notApplicable", 7))
    )


_AcSysModuleFRUstatus_Type.__name__ = "Integer32"
_AcSysModuleFRUstatus_Object = MibTableColumn
acSysModuleFRUstatus = _AcSysModuleFRUstatus_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 4, 21, 1, 14),
    _AcSysModuleFRUstatus_Type()
)
acSysModuleFRUstatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSysModuleFRUstatus.setStatus("current")


class _AcSysModuleNumOfPorts_Type(Unsigned32):
    """Custom type acSysModuleNumOfPorts based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_AcSysModuleNumOfPorts_Type.__name__ = "Unsigned32"
_AcSysModuleNumOfPorts_Object = MibTableColumn
acSysModuleNumOfPorts = _AcSysModuleNumOfPorts_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 4, 21, 1, 15),
    _AcSysModuleNumOfPorts_Type()
)
acSysModuleNumOfPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSysModuleNumOfPorts.setStatus("current")


class _AcSysModuleFirstPortNum_Type(Unsigned32):
    """Custom type acSysModuleFirstPortNum based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 19),
    )


_AcSysModuleFirstPortNum_Type.__name__ = "Unsigned32"
_AcSysModuleFirstPortNum_Object = MibTableColumn
acSysModuleFirstPortNum = _AcSysModuleFirstPortNum_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 4, 21, 1, 16),
    _AcSysModuleFirstPortNum_Type()
)
acSysModuleFirstPortNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSysModuleFirstPortNum.setStatus("current")


class _AcSysModuleSerialNumberString_Type(SnmpAdminString):
    """Custom type acSysModuleSerialNumberString based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_AcSysModuleSerialNumberString_Type.__name__ = "SnmpAdminString"
_AcSysModuleSerialNumberString_Object = MibTableColumn
acSysModuleSerialNumberString = _AcSysModuleSerialNumberString_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 4, 21, 1, 17),
    _AcSysModuleSerialNumberString_Type()
)
acSysModuleSerialNumberString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSysModuleSerialNumberString.setStatus("current")
_AcSysFanTrayTable_Object = MibTable
acSysFanTrayTable = _AcSysFanTrayTable_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 4, 22)
)
if mibBuilder.loadTexts:
    acSysFanTrayTable.setStatus("current")
_AcSysFanTrayEntry_Object = MibTableRow
acSysFanTrayEntry = _AcSysFanTrayEntry_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 4, 22, 1)
)
acSysFanTrayEntry.setIndexNames(
    (0, "AC-SYSTEM-MIB", "acSysFanTrayIndex"),
)
if mibBuilder.loadTexts:
    acSysFanTrayEntry.setStatus("current")


class _AcSysFanTrayIndex_Type(Unsigned32):
    """Custom type acSysFanTrayIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_AcSysFanTrayIndex_Type.__name__ = "Unsigned32"
_AcSysFanTrayIndex_Object = MibTableColumn
acSysFanTrayIndex = _AcSysFanTrayIndex_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 4, 22, 1, 1),
    _AcSysFanTrayIndex_Type()
)
acSysFanTrayIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    acSysFanTrayIndex.setStatus("current")


class _AcSysFanTrayGeographicalPosition_Type(Unsigned32):
    """Custom type acSysFanTrayGeographicalPosition based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
    )


_AcSysFanTrayGeographicalPosition_Type.__name__ = "Unsigned32"
_AcSysFanTrayGeographicalPosition_Object = MibTableColumn
acSysFanTrayGeographicalPosition = _AcSysFanTrayGeographicalPosition_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 4, 22, 1, 2),
    _AcSysFanTrayGeographicalPosition_Type()
)
acSysFanTrayGeographicalPosition.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSysFanTrayGeographicalPosition.setStatus("current")


class _AcSysFanTrayExistence_Type(Integer32):
    """Custom type acSysFanTrayExistence based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("present", 1),
          ("missing", 2))
    )


_AcSysFanTrayExistence_Type.__name__ = "Integer32"
_AcSysFanTrayExistence_Object = MibTableColumn
acSysFanTrayExistence = _AcSysFanTrayExistence_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 4, 22, 1, 3),
    _AcSysFanTrayExistence_Type()
)
acSysFanTrayExistence.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSysFanTrayExistence.setStatus("current")


class _AcSysFanTrayType_Type(SnmpAdminString):
    """Custom type acSysFanTrayType based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 50),
    )


_AcSysFanTrayType_Type.__name__ = "SnmpAdminString"
_AcSysFanTrayType_Object = MibTableColumn
acSysFanTrayType = _AcSysFanTrayType_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 4, 22, 1, 4),
    _AcSysFanTrayType_Type()
)
acSysFanTrayType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSysFanTrayType.setStatus("current")


class _AcSysFanTrayLEDs_Type(OctetString):
    """Custom type acSysFanTrayLEDs based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_AcSysFanTrayLEDs_Type.__name__ = "OctetString"
_AcSysFanTrayLEDs_Object = MibTableColumn
acSysFanTrayLEDs = _AcSysFanTrayLEDs_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 4, 22, 1, 5),
    _AcSysFanTrayLEDs_Type()
)
acSysFanTrayLEDs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSysFanTrayLEDs.setStatus("current")


class _AcSysFanTraySeverity_Type(Integer32):
    """Custom type acSysFanTraySeverity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("cleared", 0),
          ("indeterminate", 1),
          ("warning", 2),
          ("minor", 3),
          ("major", 4),
          ("critical", 5))
    )


_AcSysFanTraySeverity_Type.__name__ = "Integer32"
_AcSysFanTraySeverity_Object = MibTableColumn
acSysFanTraySeverity = _AcSysFanTraySeverity_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 4, 22, 1, 6),
    _AcSysFanTraySeverity_Type()
)
acSysFanTraySeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSysFanTraySeverity.setStatus("current")


class _AcSysFanTrayFansConfiguredSpeed_Type(OctetString):
    """Custom type acSysFanTrayFansConfiguredSpeed based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_AcSysFanTrayFansConfiguredSpeed_Type.__name__ = "OctetString"
_AcSysFanTrayFansConfiguredSpeed_Object = MibTableColumn
acSysFanTrayFansConfiguredSpeed = _AcSysFanTrayFansConfiguredSpeed_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 4, 22, 1, 7),
    _AcSysFanTrayFansConfiguredSpeed_Type()
)
acSysFanTrayFansConfiguredSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSysFanTrayFansConfiguredSpeed.setStatus("current")


class _AcSysFanTrayFansCurrentSpeed_Type(OctetString):
    """Custom type acSysFanTrayFansCurrentSpeed based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_AcSysFanTrayFansCurrentSpeed_Type.__name__ = "OctetString"
_AcSysFanTrayFansCurrentSpeed_Object = MibTableColumn
acSysFanTrayFansCurrentSpeed = _AcSysFanTrayFansCurrentSpeed_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 4, 22, 1, 8),
    _AcSysFanTrayFansCurrentSpeed_Type()
)
acSysFanTrayFansCurrentSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSysFanTrayFansCurrentSpeed.setStatus("current")


class _AcSysFanTrayFansStatus_Type(OctetString):
    """Custom type acSysFanTrayFansStatus based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 1),
    )


_AcSysFanTrayFansStatus_Type.__name__ = "OctetString"
_AcSysFanTrayFansStatus_Object = MibTableColumn
acSysFanTrayFansStatus = _AcSysFanTrayFansStatus_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 4, 22, 1, 9),
    _AcSysFanTrayFansStatus_Type()
)
acSysFanTrayFansStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSysFanTrayFansStatus.setStatus("current")
_AcSysPowerSupplyTable_Object = MibTable
acSysPowerSupplyTable = _AcSysPowerSupplyTable_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 4, 23)
)
if mibBuilder.loadTexts:
    acSysPowerSupplyTable.setStatus("current")
_AcSysPowerSupplyEntry_Object = MibTableRow
acSysPowerSupplyEntry = _AcSysPowerSupplyEntry_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 4, 23, 1)
)
acSysPowerSupplyEntry.setIndexNames(
    (0, "AC-SYSTEM-MIB", "acSysPowerSupplyIndex"),
)
if mibBuilder.loadTexts:
    acSysPowerSupplyEntry.setStatus("current")


class _AcSysPowerSupplyIndex_Type(Unsigned32):
    """Custom type acSysPowerSupplyIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_AcSysPowerSupplyIndex_Type.__name__ = "Unsigned32"
_AcSysPowerSupplyIndex_Object = MibTableColumn
acSysPowerSupplyIndex = _AcSysPowerSupplyIndex_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 4, 23, 1, 1),
    _AcSysPowerSupplyIndex_Type()
)
acSysPowerSupplyIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    acSysPowerSupplyIndex.setStatus("current")


class _AcSysPowerSupplyGeographicalPosition_Type(Unsigned32):
    """Custom type acSysPowerSupplyGeographicalPosition based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_AcSysPowerSupplyGeographicalPosition_Type.__name__ = "Unsigned32"
_AcSysPowerSupplyGeographicalPosition_Object = MibTableColumn
acSysPowerSupplyGeographicalPosition = _AcSysPowerSupplyGeographicalPosition_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 4, 23, 1, 2),
    _AcSysPowerSupplyGeographicalPosition_Type()
)
acSysPowerSupplyGeographicalPosition.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSysPowerSupplyGeographicalPosition.setStatus("current")


class _AcSysPowerSupplyExistence_Type(Integer32):
    """Custom type acSysPowerSupplyExistence based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("present", 1),
          ("missing", 2))
    )


_AcSysPowerSupplyExistence_Type.__name__ = "Integer32"
_AcSysPowerSupplyExistence_Object = MibTableColumn
acSysPowerSupplyExistence = _AcSysPowerSupplyExistence_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 4, 23, 1, 3),
    _AcSysPowerSupplyExistence_Type()
)
acSysPowerSupplyExistence.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSysPowerSupplyExistence.setStatus("current")


class _AcSysPowerSupplyHwversion_Type(SnmpAdminString):
    """Custom type acSysPowerSupplyHwversion based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_AcSysPowerSupplyHwversion_Type.__name__ = "SnmpAdminString"
_AcSysPowerSupplyHwversion_Object = MibTableColumn
acSysPowerSupplyHwversion = _AcSysPowerSupplyHwversion_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 4, 23, 1, 4),
    _AcSysPowerSupplyHwversion_Type()
)
acSysPowerSupplyHwversion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSysPowerSupplyHwversion.setStatus("current")


class _AcSysPowerSupplyLEDs_Type(OctetString):
    """Custom type acSysPowerSupplyLEDs based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_AcSysPowerSupplyLEDs_Type.__name__ = "OctetString"
_AcSysPowerSupplyLEDs_Object = MibTableColumn
acSysPowerSupplyLEDs = _AcSysPowerSupplyLEDs_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 4, 23, 1, 5),
    _AcSysPowerSupplyLEDs_Type()
)
acSysPowerSupplyLEDs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSysPowerSupplyLEDs.setStatus("current")


class _AcSysPowerSupplySeverity_Type(Integer32):
    """Custom type acSysPowerSupplySeverity based on Integer32"""
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
        *(("cleared", 1),
          ("indeterminate", 2),
          ("warning", 3),
          ("minor", 4),
          ("major", 5),
          ("critical", 6))
    )


_AcSysPowerSupplySeverity_Type.__name__ = "Integer32"
_AcSysPowerSupplySeverity_Object = MibTableColumn
acSysPowerSupplySeverity = _AcSysPowerSupplySeverity_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 4, 23, 1, 6),
    _AcSysPowerSupplySeverity_Type()
)
acSysPowerSupplySeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSysPowerSupplySeverity.setStatus("current")
_AcSysPEMTable_Object = MibTable
acSysPEMTable = _AcSysPEMTable_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 4, 24)
)
if mibBuilder.loadTexts:
    acSysPEMTable.setStatus("current")
_AcSysPEMEntry_Object = MibTableRow
acSysPEMEntry = _AcSysPEMEntry_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 4, 24, 1)
)
acSysPEMEntry.setIndexNames(
    (0, "AC-SYSTEM-MIB", "acSysPEMIndex"),
)
if mibBuilder.loadTexts:
    acSysPEMEntry.setStatus("current")


class _AcSysPEMIndex_Type(Unsigned32):
    """Custom type acSysPEMIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_AcSysPEMIndex_Type.__name__ = "Unsigned32"
_AcSysPEMIndex_Object = MibTableColumn
acSysPEMIndex = _AcSysPEMIndex_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 4, 24, 1, 1),
    _AcSysPEMIndex_Type()
)
acSysPEMIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    acSysPEMIndex.setStatus("current")


class _AcSysPEMGeographicalPosition_Type(Unsigned32):
    """Custom type acSysPEMGeographicalPosition based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_AcSysPEMGeographicalPosition_Type.__name__ = "Unsigned32"
_AcSysPEMGeographicalPosition_Object = MibTableColumn
acSysPEMGeographicalPosition = _AcSysPEMGeographicalPosition_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 4, 24, 1, 2),
    _AcSysPEMGeographicalPosition_Type()
)
acSysPEMGeographicalPosition.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSysPEMGeographicalPosition.setStatus("current")


class _AcSysPEMExistence_Type(Integer32):
    """Custom type acSysPEMExistence based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("present", 1),
          ("missing", 2))
    )


_AcSysPEMExistence_Type.__name__ = "Integer32"
_AcSysPEMExistence_Object = MibTableColumn
acSysPEMExistence = _AcSysPEMExistence_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 4, 24, 1, 3),
    _AcSysPEMExistence_Type()
)
acSysPEMExistence.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSysPEMExistence.setStatus("current")


class _AcSysPEMType_Type(SnmpAdminString):
    """Custom type acSysPEMType based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_AcSysPEMType_Type.__name__ = "SnmpAdminString"
_AcSysPEMType_Object = MibTableColumn
acSysPEMType = _AcSysPEMType_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 4, 24, 1, 4),
    _AcSysPEMType_Type()
)
acSysPEMType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSysPEMType.setStatus("current")


class _AcSysPEMElectricWireConnection_Type(Integer32):
    """Custom type acSysPEMElectricWireConnection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("connected", 1),
          ("disconnected", 2))
    )


_AcSysPEMElectricWireConnection_Type.__name__ = "Integer32"
_AcSysPEMElectricWireConnection_Object = MibTableColumn
acSysPEMElectricWireConnection = _AcSysPEMElectricWireConnection_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 4, 24, 1, 5),
    _AcSysPEMElectricWireConnection_Type()
)
acSysPEMElectricWireConnection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSysPEMElectricWireConnection.setStatus("current")
_AcSysSATModule_ObjectIdentity = ObjectIdentity
acSysSATModule = _AcSysSATModule_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 4, 25)
)
_AcSysSATTable_Object = MibTable
acSysSATTable = _AcSysSATTable_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 4, 25, 21)
)
if mibBuilder.loadTexts:
    acSysSATTable.setStatus("current")
_AcSysSATEntry_Object = MibTableRow
acSysSATEntry = _AcSysSATEntry_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 4, 25, 21, 1)
)
acSysSATEntry.setIndexNames(
    (0, "AC-SYSTEM-MIB", "acSysSATSatIndex"),
)
if mibBuilder.loadTexts:
    acSysSATEntry.setStatus("current")


class _AcSysSATSatIndex_Type(Unsigned32):
    """Custom type acSysSATSatIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_AcSysSATSatIndex_Type.__name__ = "Unsigned32"
_AcSysSATSatIndex_Object = MibTableColumn
acSysSATSatIndex = _AcSysSATSatIndex_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 4, 25, 21, 1, 1),
    _AcSysSATSatIndex_Type()
)
acSysSATSatIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    acSysSATSatIndex.setStatus("current")


class _AcSysSATGeographicalPosition_Type(Unsigned32):
    """Custom type acSysSATGeographicalPosition based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 4),
    )


_AcSysSATGeographicalPosition_Type.__name__ = "Unsigned32"
_AcSysSATGeographicalPosition_Object = MibTableColumn
acSysSATGeographicalPosition = _AcSysSATGeographicalPosition_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 4, 25, 21, 1, 2),
    _AcSysSATGeographicalPosition_Type()
)
acSysSATGeographicalPosition.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSysSATGeographicalPosition.setStatus("current")


class _AcSysSATType_Type(SnmpAdminString):
    """Custom type acSysSATType based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_AcSysSATType_Type.__name__ = "SnmpAdminString"
_AcSysSATType_Object = MibTableColumn
acSysSATType = _AcSysSATType_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 4, 25, 21, 1, 3),
    _AcSysSATType_Type()
)
acSysSATType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSysSATType.setStatus("current")


class _AcSysSATInitInformation_Type(Integer32):
    """Custom type acSysSATInitInformation based on Integer32"""
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
              11)
        )
    )
    namedValues = NamedValues(
        *(("detected", 0),
          ("reConfig", 1),
          ("reConfigTry2", 2),
          ("reConfigTry3", 3),
          ("notInitialized", 4),
          ("initIsMissing", 5),
          ("initWasReset", 6),
          ("initFail", 7),
          ("initInProgress", 8),
          ("initUpdateREFTable", 9),
          ("remoteKeepAlive", 10),
          ("initComplete", 11))
    )


_AcSysSATInitInformation_Type.__name__ = "Integer32"
_AcSysSATInitInformation_Object = MibTableColumn
acSysSATInitInformation = _AcSysSATInitInformation_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 4, 25, 21, 1, 4),
    _AcSysSATInitInformation_Type()
)
acSysSATInitInformation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSysSATInitInformation.setStatus("current")


class _AcSysSATTimingUnitExistence_Type(Integer32):
    """Custom type acSysSATTimingUnitExistence based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("exist", 1),
          ("notExist", 2))
    )


_AcSysSATTimingUnitExistence_Type.__name__ = "Integer32"
_AcSysSATTimingUnitExistence_Object = MibTableColumn
acSysSATTimingUnitExistence = _AcSysSATTimingUnitExistence_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 4, 25, 21, 1, 5),
    _AcSysSATTimingUnitExistence_Type()
)
acSysSATTimingUnitExistence.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSysSATTimingUnitExistence.setStatus("current")


class _AcSysSATTimingRefSelection_Type(Integer32):
    """Custom type acSysSATTimingRefSelection based on Integer32"""
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
        *(("bITSNOREF", 0),
          ("rEFFromBITSA", 1),
          ("rEFFromBITSB", 2),
          ("bITSNOREF1", 3),
          ("rEFFromLineClock1", 4),
          ("rEFFromLineClock2", 5),
          ("rEFFromLineClock3", 6),
          ("rEFFromLineClock7", 7))
    )


_AcSysSATTimingRefSelection_Type.__name__ = "Integer32"
_AcSysSATTimingRefSelection_Object = MibTableColumn
acSysSATTimingRefSelection = _AcSysSATTimingRefSelection_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 4, 25, 21, 1, 6),
    _AcSysSATTimingRefSelection_Type()
)
acSysSATTimingRefSelection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSysSATTimingRefSelection.setStatus("current")
_AcSysSATFramersTable_Object = MibTable
acSysSATFramersTable = _AcSysSATFramersTable_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 4, 25, 22)
)
if mibBuilder.loadTexts:
    acSysSATFramersTable.setStatus("current")
_AcSysSATFramersEntry_Object = MibTableRow
acSysSATFramersEntry = _AcSysSATFramersEntry_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 4, 25, 22, 1)
)
acSysSATFramersEntry.setIndexNames(
    (0, "AC-SYSTEM-MIB", "acSysSATFramersSatIndex"),
    (0, "AC-SYSTEM-MIB", "acSysSATFramersFramerIndex"),
)
if mibBuilder.loadTexts:
    acSysSATFramersEntry.setStatus("current")


class _AcSysSATFramersSatIndex_Type(Unsigned32):
    """Custom type acSysSATFramersSatIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_AcSysSATFramersSatIndex_Type.__name__ = "Unsigned32"
_AcSysSATFramersSatIndex_Object = MibTableColumn
acSysSATFramersSatIndex = _AcSysSATFramersSatIndex_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 4, 25, 22, 1, 1),
    _AcSysSATFramersSatIndex_Type()
)
acSysSATFramersSatIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    acSysSATFramersSatIndex.setStatus("current")


class _AcSysSATFramersFramerIndex_Type(Unsigned32):
    """Custom type acSysSATFramersFramerIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_AcSysSATFramersFramerIndex_Type.__name__ = "Unsigned32"
_AcSysSATFramersFramerIndex_Object = MibTableColumn
acSysSATFramersFramerIndex = _AcSysSATFramersFramerIndex_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 4, 25, 22, 1, 2),
    _AcSysSATFramersFramerIndex_Type()
)
acSysSATFramersFramerIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    acSysSATFramersFramerIndex.setStatus("current")


class _AcSysSATFramersFramerInterfaceStatus_Type(Integer32):
    """Custom type acSysSATFramersFramerInterfaceStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("framerInitialized", 0),
          ("framerNotInitialized", 1))
    )


_AcSysSATFramersFramerInterfaceStatus_Type.__name__ = "Integer32"
_AcSysSATFramersFramerInterfaceStatus_Object = MibTableColumn
acSysSATFramersFramerInterfaceStatus = _AcSysSATFramersFramerInterfaceStatus_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 4, 25, 22, 1, 3),
    _AcSysSATFramersFramerInterfaceStatus_Type()
)
acSysSATFramersFramerInterfaceStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSysSATFramersFramerInterfaceStatus.setStatus("current")


class _AcSysSATFramersFramerLoopBackRef_Type(Integer32):
    """Custom type acSysSATFramersFramerLoopBackRef based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("loopdisable", 0),
          ("loopenable", 1))
    )


_AcSysSATFramersFramerLoopBackRef_Type.__name__ = "Integer32"
_AcSysSATFramersFramerLoopBackRef_Object = MibTableColumn
acSysSATFramersFramerLoopBackRef = _AcSysSATFramersFramerLoopBackRef_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 4, 25, 22, 1, 4),
    _AcSysSATFramersFramerLoopBackRef_Type()
)
acSysSATFramersFramerLoopBackRef.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSysSATFramersFramerLoopBackRef.setStatus("current")


class _AcSysSATFramersFramerInterfaceType_Type(Integer32):
    """Custom type acSysSATFramersFramerInterfaceType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("e1CRC4", 0),
          ("e1CAS", 1),
          ("e1FAS", 2),
          ("t1D4", 3),
          ("t1ESF", 4),
          ("t12", 5))
    )


_AcSysSATFramersFramerInterfaceType_Type.__name__ = "Integer32"
_AcSysSATFramersFramerInterfaceType_Object = MibTableColumn
acSysSATFramersFramerInterfaceType = _AcSysSATFramersFramerInterfaceType_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 4, 25, 22, 1, 5),
    _AcSysSATFramersFramerInterfaceType_Type()
)
acSysSATFramersFramerInterfaceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSysSATFramersFramerInterfaceType.setStatus("current")


class _AcSysSATFramersFramerTransmitControl_Type(Integer32):
    """Custom type acSysSATFramersFramerTransmitControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("systemClock", 0),
          ("aIS", 1),
          ("disableTransmit", 2))
    )


_AcSysSATFramersFramerTransmitControl_Type.__name__ = "Integer32"
_AcSysSATFramersFramerTransmitControl_Object = MibTableColumn
acSysSATFramersFramerTransmitControl = _AcSysSATFramersFramerTransmitControl_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 4, 25, 22, 1, 6),
    _AcSysSATFramersFramerTransmitControl_Type()
)
acSysSATFramersFramerTransmitControl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSysSATFramersFramerTransmitControl.setStatus("current")


class _AcSysSATFramersRxStatus_Type(Integer32):
    """Custom type acSysSATFramersRxStatus based on Integer32"""
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
        *(("alarmClear", 0),
          ("lOFAlarm", 1),
          ("lOSAlarm", 2),
          ("aISAlarm", 3),
          ("aISInit", 4))
    )


_AcSysSATFramersRxStatus_Type.__name__ = "Integer32"
_AcSysSATFramersRxStatus_Object = MibTableColumn
acSysSATFramersRxStatus = _AcSysSATFramersRxStatus_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 4, 25, 22, 1, 7),
    _AcSysSATFramersRxStatus_Type()
)
acSysSATFramersRxStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSysSATFramersRxStatus.setStatus("current")


class _AcSysSATFramersIsUsedAsPLLClock_Type(Integer32):
    """Custom type acSysSATFramersIsUsedAsPLLClock based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("notUsed", 0),
          ("used", 1))
    )


_AcSysSATFramersIsUsedAsPLLClock_Type.__name__ = "Integer32"
_AcSysSATFramersIsUsedAsPLLClock_Object = MibTableColumn
acSysSATFramersIsUsedAsPLLClock = _AcSysSATFramersIsUsedAsPLLClock_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 4, 25, 22, 1, 8),
    _AcSysSATFramersIsUsedAsPLLClock_Type()
)
acSysSATFramersIsUsedAsPLLClock.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSysSATFramersIsUsedAsPLLClock.setStatus("current")
_AcSysTimingModule_ObjectIdentity = ObjectIdentity
acSysTimingModule = _AcSysTimingModule_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 4, 26)
)
_AcSysPLLStatusTable_Object = MibTable
acSysPLLStatusTable = _AcSysPLLStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 4, 26, 21)
)
if mibBuilder.loadTexts:
    acSysPLLStatusTable.setStatus("current")
_AcSysPLLStatusEntry_Object = MibTableRow
acSysPLLStatusEntry = _AcSysPLLStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 4, 26, 21, 1)
)
acSysPLLStatusEntry.setIndexNames(
    (0, "AC-SYSTEM-MIB", "acSysPLLStatusIndex"),
)
if mibBuilder.loadTexts:
    acSysPLLStatusEntry.setStatus("current")


class _AcSysPLLStatusIndex_Type(Unsigned32):
    """Custom type acSysPLLStatusIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_AcSysPLLStatusIndex_Type.__name__ = "Unsigned32"
_AcSysPLLStatusIndex_Object = MibTableColumn
acSysPLLStatusIndex = _AcSysPLLStatusIndex_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 4, 26, 21, 1, 1),
    _AcSysPLLStatusIndex_Type()
)
acSysPLLStatusIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    acSysPLLStatusIndex.setStatus("current")


class _AcSysPLLStatusOperatingMode_Type(Integer32):
    """Custom type acSysPLLStatusOperatingMode based on Integer32"""
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
        *(("freeRun", 0),
          ("lockToRef1", 1),
          ("lockToRef2", 2),
          ("lockToLocal", 3),
          ("holdOver", 4))
    )


_AcSysPLLStatusOperatingMode_Type.__name__ = "Integer32"
_AcSysPLLStatusOperatingMode_Object = MibTableColumn
acSysPLLStatusOperatingMode = _AcSysPLLStatusOperatingMode_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 4, 26, 21, 1, 2),
    _AcSysPLLStatusOperatingMode_Type()
)
acSysPLLStatusOperatingMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSysPLLStatusOperatingMode.setStatus("current")
_AcSystemChassisHA_ObjectIdentity = ObjectIdentity
acSystemChassisHA = _AcSystemChassisHA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 4, 27)
)


class _AcSystemChassisHADevice1Name_Type(SnmpAdminString):
    """Custom type acSystemChassisHADevice1Name based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_AcSystemChassisHADevice1Name_Type.__name__ = "SnmpAdminString"
_AcSystemChassisHADevice1Name_Object = MibScalar
acSystemChassisHADevice1Name = _AcSystemChassisHADevice1Name_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 4, 27, 1),
    _AcSystemChassisHADevice1Name_Type()
)
acSystemChassisHADevice1Name.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acSystemChassisHADevice1Name.setStatus("current")


class _AcSystemChassisHADevice2Name_Type(SnmpAdminString):
    """Custom type acSystemChassisHADevice2Name based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_AcSystemChassisHADevice2Name_Type.__name__ = "SnmpAdminString"
_AcSystemChassisHADevice2Name_Object = MibScalar
acSystemChassisHADevice2Name = _AcSystemChassisHADevice2Name_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 4, 27, 2),
    _AcSystemChassisHADevice2Name_Type()
)
acSystemChassisHADevice2Name.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acSystemChassisHADevice2Name.setStatus("current")


class _AcSystemChassisHAActiveDevice_Type(Integer32):
    """Custom type acSystemChassisHAActiveDevice based on Integer32"""
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
        *(("notApplicable", 0),
          ("device1", 1),
          ("device2", 2),
          ("standAlone", 3),
          ("haReady", 4))
    )


_AcSystemChassisHAActiveDevice_Type.__name__ = "Integer32"
_AcSystemChassisHAActiveDevice_Object = MibScalar
acSystemChassisHAActiveDevice = _AcSystemChassisHAActiveDevice_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 4, 27, 3),
    _AcSystemChassisHAActiveDevice_Type()
)
acSystemChassisHAActiveDevice.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSystemChassisHAActiveDevice.setStatus("current")
_AcSysRedundantModuleTable_Object = MibTable
acSysRedundantModuleTable = _AcSysRedundantModuleTable_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 4, 27, 21)
)
if mibBuilder.loadTexts:
    acSysRedundantModuleTable.setStatus("current")
_AcSysRedundantModuleEntry_Object = MibTableRow
acSysRedundantModuleEntry = _AcSysRedundantModuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 4, 27, 21, 1)
)
acSysRedundantModuleEntry.setIndexNames(
    (0, "AC-SYSTEM-MIB", "acSysRedundantModuleIndex"),
)
if mibBuilder.loadTexts:
    acSysRedundantModuleEntry.setStatus("current")


class _AcSysRedundantModuleIndex_Type(Unsigned32):
    """Custom type acSysRedundantModuleIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_AcSysRedundantModuleIndex_Type.__name__ = "Unsigned32"
_AcSysRedundantModuleIndex_Object = MibTableColumn
acSysRedundantModuleIndex = _AcSysRedundantModuleIndex_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 4, 27, 21, 1, 1),
    _AcSysRedundantModuleIndex_Type()
)
acSysRedundantModuleIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    acSysRedundantModuleIndex.setStatus("current")


class _AcSysRedundantModuleGeographicalPosition_Type(Unsigned32):
    """Custom type acSysRedundantModuleGeographicalPosition based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 12),
    )


_AcSysRedundantModuleGeographicalPosition_Type.__name__ = "Unsigned32"
_AcSysRedundantModuleGeographicalPosition_Object = MibTableColumn
acSysRedundantModuleGeographicalPosition = _AcSysRedundantModuleGeographicalPosition_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 4, 27, 21, 1, 2),
    _AcSysRedundantModuleGeographicalPosition_Type()
)
acSysRedundantModuleGeographicalPosition.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSysRedundantModuleGeographicalPosition.setStatus("current")


class _AcSysRedundantModuleType_Type(Integer32):
    """Custom type acSysRedundantModuleType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              73,
              79,
              80,
              81,
              82,
              83,
              84,
              85,
              265,
              266,
              267,
              268,
              272,
              280,
              283,
              284,
              285,
              286,
              290,
              295,
              308,
              309)
        )
    )
    namedValues = NamedValues(
        *(("acUnknown", 0),
          ("acMediantSW", 73),
          ("acMediant-VE-SBC", 79),
          ("acMediant-VE-H-SBC", 80),
          ("acMediant-SE-SBC", 81),
          ("acMediant-SE-H-SBC", 82),
          ("acMediant-9000-SBC", 83),
          ("acMediant-500L-MSBR", 84),
          ("acMediant-500L-ESBC", 85),
          ("acMediant800CPUmodule", 265),
          ("acMediant800IFDigitalModule", 266),
          ("acMediant800IFAnalogModule", 267),
          ("acMediant800IFBRIModule", 268),
          ("acMediant800EthernetModule", 272),
          ("acMediant4000CPUmodule", 280),
          ("acMediant500CPUmodule", 283),
          ("acMediant500IFDigitalModule", 284),
          ("acMediant500IFAnalogModule", 285),
          ("acMediant500IFBRIModule", 286),
          ("acMediant500EthernetModule", 290),
          ("acMediant4000MPModule", 295),
          ("acMediant2600CPUmodule", 308),
          ("acMediant2600MPModule", 309))
    )


_AcSysRedundantModuleType_Type.__name__ = "Integer32"
_AcSysRedundantModuleType_Object = MibTableColumn
acSysRedundantModuleType = _AcSysRedundantModuleType_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 4, 27, 21, 1, 3),
    _AcSysRedundantModuleType_Type()
)
acSysRedundantModuleType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSysRedundantModuleType.setStatus("current")


class _AcSysRedundantModulePresence_Type(Integer32):
    """Custom type acSysRedundantModulePresence based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("present", 1),
          ("missing", 2))
    )


_AcSysRedundantModulePresence_Type.__name__ = "Integer32"
_AcSysRedundantModulePresence_Object = MibTableColumn
acSysRedundantModulePresence = _AcSysRedundantModulePresence_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 4, 27, 21, 1, 4),
    _AcSysRedundantModulePresence_Type()
)
acSysRedundantModulePresence.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSysRedundantModulePresence.setStatus("current")


class _AcSysRedundantModuleLicenseKeyList_Type(SnmpAdminString):
    """Custom type acSysRedundantModuleLicenseKeyList based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 1400),
    )


_AcSysRedundantModuleLicenseKeyList_Type.__name__ = "SnmpAdminString"
_AcSysRedundantModuleLicenseKeyList_Object = MibTableColumn
acSysRedundantModuleLicenseKeyList = _AcSysRedundantModuleLicenseKeyList_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 4, 27, 21, 1, 5),
    _AcSysRedundantModuleLicenseKeyList_Type()
)
acSysRedundantModuleLicenseKeyList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSysRedundantModuleLicenseKeyList.setStatus("current")


class _AcSysRedundantModuleSerialNumber_Type(Integer32):
    """Custom type acSysRedundantModuleSerialNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_AcSysRedundantModuleSerialNumber_Type.__name__ = "Integer32"
_AcSysRedundantModuleSerialNumber_Object = MibTableColumn
acSysRedundantModuleSerialNumber = _AcSysRedundantModuleSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 4, 27, 21, 1, 6),
    _AcSysRedundantModuleSerialNumber_Type()
)
acSysRedundantModuleSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSysRedundantModuleSerialNumber.setStatus("current")


class _AcSysRedundantModuleSWVersion_Type(SnmpAdminString):
    """Custom type acSysRedundantModuleSWVersion based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_AcSysRedundantModuleSWVersion_Type.__name__ = "SnmpAdminString"
_AcSysRedundantModuleSWVersion_Object = MibTableColumn
acSysRedundantModuleSWVersion = _AcSysRedundantModuleSWVersion_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 4, 27, 21, 1, 7),
    _AcSysRedundantModuleSWVersion_Type()
)
acSysRedundantModuleSWVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSysRedundantModuleSWVersion.setStatus("current")


class _AcSysRedundantModuleOperationalState_Type(Integer32):
    """Custom type acSysRedundantModuleOperationalState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_AcSysRedundantModuleOperationalState_Type.__name__ = "Integer32"
_AcSysRedundantModuleOperationalState_Object = MibTableColumn
acSysRedundantModuleOperationalState = _AcSysRedundantModuleOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 4, 27, 21, 1, 8),
    _AcSysRedundantModuleOperationalState_Type()
)
acSysRedundantModuleOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSysRedundantModuleOperationalState.setStatus("current")


class _AcSysRedundantModuleHAStatus_Type(Integer32):
    """Custom type acSysRedundantModuleHAStatus based on Integer32"""
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
        *(("acitveNonHA", 1),
          ("active", 2),
          ("redundant", 3),
          ("standAlone", 4),
          ("redundantNonHA", 5),
          ("notApplicable", 6))
    )


_AcSysRedundantModuleHAStatus_Type.__name__ = "Integer32"
_AcSysRedundantModuleHAStatus_Object = MibTableColumn
acSysRedundantModuleHAStatus = _AcSysRedundantModuleHAStatus_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 4, 27, 21, 1, 9),
    _AcSysRedundantModuleHAStatus_Type()
)
acSysRedundantModuleHAStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSysRedundantModuleHAStatus.setStatus("current")


class _AcSysRedundantModuleLEDs_Type(OctetString):
    """Custom type acSysRedundantModuleLEDs based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 50),
    )


_AcSysRedundantModuleLEDs_Type.__name__ = "OctetString"
_AcSysRedundantModuleLEDs_Object = MibTableColumn
acSysRedundantModuleLEDs = _AcSysRedundantModuleLEDs_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 4, 27, 21, 1, 10),
    _AcSysRedundantModuleLEDs_Type()
)
acSysRedundantModuleLEDs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSysRedundantModuleLEDs.setStatus("current")


class _AcSysRedundantModuleTemperature_Type(Integer32):
    """Custom type acSysRedundantModuleTemperature based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 100),
    )


_AcSysRedundantModuleTemperature_Type.__name__ = "Integer32"
_AcSysRedundantModuleTemperature_Object = MibTableColumn
acSysRedundantModuleTemperature = _AcSysRedundantModuleTemperature_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 4, 27, 21, 1, 11),
    _AcSysRedundantModuleTemperature_Type()
)
acSysRedundantModuleTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSysRedundantModuleTemperature.setStatus("current")


class _AcSysRedundantModuleActions_Type(Integer32):
    """Custom type acSysRedundantModuleActions based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              3)
        )
    )
    namedValues = NamedValues(
        *(("reset", 1),
          ("actionDone", 3))
    )


_AcSysRedundantModuleActions_Type.__name__ = "Integer32"
_AcSysRedundantModuleActions_Object = MibTableColumn
acSysRedundantModuleActions = _AcSysRedundantModuleActions_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 4, 27, 21, 1, 12),
    _AcSysRedundantModuleActions_Type()
)
acSysRedundantModuleActions.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acSysRedundantModuleActions.setStatus("current")


class _AcSysRedundantModuleFRUaction_Type(Integer32):
    """Custom type acSysRedundantModuleFRUaction based on Integer32"""
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
        *(("fruActionDone", 1),
          ("fruOutOfServiceAction", 2),
          ("fruBackToServiceAction", 3),
          ("fruNotApplicable", 4))
    )


_AcSysRedundantModuleFRUaction_Type.__name__ = "Integer32"
_AcSysRedundantModuleFRUaction_Object = MibTableColumn
acSysRedundantModuleFRUaction = _AcSysRedundantModuleFRUaction_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 4, 27, 21, 1, 13),
    _AcSysRedundantModuleFRUaction_Type()
)
acSysRedundantModuleFRUaction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acSysRedundantModuleFRUaction.setStatus("current")


class _AcSysRedundantModuleFRUstatus_Type(Integer32):
    """Custom type acSysRedundantModuleFRUstatus based on Integer32"""
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
        *(("moduleNotExist", 1),
          ("moduleExistOk", 2),
          ("moduleOutOfService", 3),
          ("moduleBackToServiceStart", 4),
          ("moduleMismatch", 5),
          ("moduleFaulty", 6),
          ("notApplicable", 7))
    )


_AcSysRedundantModuleFRUstatus_Type.__name__ = "Integer32"
_AcSysRedundantModuleFRUstatus_Object = MibTableColumn
acSysRedundantModuleFRUstatus = _AcSysRedundantModuleFRUstatus_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 4, 27, 21, 1, 14),
    _AcSysRedundantModuleFRUstatus_Type()
)
acSysRedundantModuleFRUstatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSysRedundantModuleFRUstatus.setStatus("current")


class _AcSysRedundantModuleNumOfPorts_Type(Unsigned32):
    """Custom type acSysRedundantModuleNumOfPorts based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_AcSysRedundantModuleNumOfPorts_Type.__name__ = "Unsigned32"
_AcSysRedundantModuleNumOfPorts_Object = MibTableColumn
acSysRedundantModuleNumOfPorts = _AcSysRedundantModuleNumOfPorts_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 4, 27, 21, 1, 15),
    _AcSysRedundantModuleNumOfPorts_Type()
)
acSysRedundantModuleNumOfPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSysRedundantModuleNumOfPorts.setStatus("current")


class _AcSysRedundantModuleFirstPortNum_Type(Unsigned32):
    """Custom type acSysRedundantModuleFirstPortNum based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 19),
    )


_AcSysRedundantModuleFirstPortNum_Type.__name__ = "Unsigned32"
_AcSysRedundantModuleFirstPortNum_Object = MibTableColumn
acSysRedundantModuleFirstPortNum = _AcSysRedundantModuleFirstPortNum_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 4, 27, 21, 1, 16),
    _AcSysRedundantModuleFirstPortNum_Type()
)
acSysRedundantModuleFirstPortNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSysRedundantModuleFirstPortNum.setStatus("current")


class _AcSysRedundantModuleSerialNumberString_Type(SnmpAdminString):
    """Custom type acSysRedundantModuleSerialNumberString based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_AcSysRedundantModuleSerialNumberString_Type.__name__ = "SnmpAdminString"
_AcSysRedundantModuleSerialNumberString_Object = MibTableColumn
acSysRedundantModuleSerialNumberString = _AcSysRedundantModuleSerialNumberString_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 4, 27, 21, 1, 17),
    _AcSysRedundantModuleSerialNumberString_Type()
)
acSysRedundantModuleSerialNumberString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSysRedundantModuleSerialNumberString.setStatus("current")
_AcSysRedundantFanTrayTable_Object = MibTable
acSysRedundantFanTrayTable = _AcSysRedundantFanTrayTable_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 4, 27, 22)
)
if mibBuilder.loadTexts:
    acSysRedundantFanTrayTable.setStatus("current")
_AcSysRedundantFanTrayEntry_Object = MibTableRow
acSysRedundantFanTrayEntry = _AcSysRedundantFanTrayEntry_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 4, 27, 22, 1)
)
acSysRedundantFanTrayEntry.setIndexNames(
    (0, "AC-SYSTEM-MIB", "acSysRedundantFanTrayIndex"),
)
if mibBuilder.loadTexts:
    acSysRedundantFanTrayEntry.setStatus("current")


class _AcSysRedundantFanTrayIndex_Type(Unsigned32):
    """Custom type acSysRedundantFanTrayIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_AcSysRedundantFanTrayIndex_Type.__name__ = "Unsigned32"
_AcSysRedundantFanTrayIndex_Object = MibTableColumn
acSysRedundantFanTrayIndex = _AcSysRedundantFanTrayIndex_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 4, 27, 22, 1, 1),
    _AcSysRedundantFanTrayIndex_Type()
)
acSysRedundantFanTrayIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    acSysRedundantFanTrayIndex.setStatus("current")


class _AcSysRedundantFanTrayGeographicalPosition_Type(Unsigned32):
    """Custom type acSysRedundantFanTrayGeographicalPosition based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
    )


_AcSysRedundantFanTrayGeographicalPosition_Type.__name__ = "Unsigned32"
_AcSysRedundantFanTrayGeographicalPosition_Object = MibTableColumn
acSysRedundantFanTrayGeographicalPosition = _AcSysRedundantFanTrayGeographicalPosition_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 4, 27, 22, 1, 2),
    _AcSysRedundantFanTrayGeographicalPosition_Type()
)
acSysRedundantFanTrayGeographicalPosition.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSysRedundantFanTrayGeographicalPosition.setStatus("current")


class _AcSysRedundantFanTrayExistence_Type(Integer32):
    """Custom type acSysRedundantFanTrayExistence based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("present", 1),
          ("missing", 2))
    )


_AcSysRedundantFanTrayExistence_Type.__name__ = "Integer32"
_AcSysRedundantFanTrayExistence_Object = MibTableColumn
acSysRedundantFanTrayExistence = _AcSysRedundantFanTrayExistence_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 4, 27, 22, 1, 3),
    _AcSysRedundantFanTrayExistence_Type()
)
acSysRedundantFanTrayExistence.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSysRedundantFanTrayExistence.setStatus("current")


class _AcSysRedundantFanTrayType_Type(SnmpAdminString):
    """Custom type acSysRedundantFanTrayType based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 50),
    )


_AcSysRedundantFanTrayType_Type.__name__ = "SnmpAdminString"
_AcSysRedundantFanTrayType_Object = MibTableColumn
acSysRedundantFanTrayType = _AcSysRedundantFanTrayType_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 4, 27, 22, 1, 4),
    _AcSysRedundantFanTrayType_Type()
)
acSysRedundantFanTrayType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSysRedundantFanTrayType.setStatus("current")


class _AcSysRedundantFanTrayLEDs_Type(OctetString):
    """Custom type acSysRedundantFanTrayLEDs based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_AcSysRedundantFanTrayLEDs_Type.__name__ = "OctetString"
_AcSysRedundantFanTrayLEDs_Object = MibTableColumn
acSysRedundantFanTrayLEDs = _AcSysRedundantFanTrayLEDs_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 4, 27, 22, 1, 5),
    _AcSysRedundantFanTrayLEDs_Type()
)
acSysRedundantFanTrayLEDs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSysRedundantFanTrayLEDs.setStatus("current")


class _AcSysRedundantFanTraySeverity_Type(Integer32):
    """Custom type acSysRedundantFanTraySeverity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("cleared", 0),
          ("indeterminate", 1),
          ("warning", 2),
          ("minor", 3),
          ("major", 4),
          ("critical", 5))
    )


_AcSysRedundantFanTraySeverity_Type.__name__ = "Integer32"
_AcSysRedundantFanTraySeverity_Object = MibTableColumn
acSysRedundantFanTraySeverity = _AcSysRedundantFanTraySeverity_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 4, 27, 22, 1, 6),
    _AcSysRedundantFanTraySeverity_Type()
)
acSysRedundantFanTraySeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSysRedundantFanTraySeverity.setStatus("current")


class _AcSysRedundantFanTrayFansConfiguredSpeed_Type(OctetString):
    """Custom type acSysRedundantFanTrayFansConfiguredSpeed based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_AcSysRedundantFanTrayFansConfiguredSpeed_Type.__name__ = "OctetString"
_AcSysRedundantFanTrayFansConfiguredSpeed_Object = MibTableColumn
acSysRedundantFanTrayFansConfiguredSpeed = _AcSysRedundantFanTrayFansConfiguredSpeed_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 4, 27, 22, 1, 7),
    _AcSysRedundantFanTrayFansConfiguredSpeed_Type()
)
acSysRedundantFanTrayFansConfiguredSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSysRedundantFanTrayFansConfiguredSpeed.setStatus("current")


class _AcSysRedundantFanTrayFansCurrentSpeed_Type(OctetString):
    """Custom type acSysRedundantFanTrayFansCurrentSpeed based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_AcSysRedundantFanTrayFansCurrentSpeed_Type.__name__ = "OctetString"
_AcSysRedundantFanTrayFansCurrentSpeed_Object = MibTableColumn
acSysRedundantFanTrayFansCurrentSpeed = _AcSysRedundantFanTrayFansCurrentSpeed_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 4, 27, 22, 1, 8),
    _AcSysRedundantFanTrayFansCurrentSpeed_Type()
)
acSysRedundantFanTrayFansCurrentSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSysRedundantFanTrayFansCurrentSpeed.setStatus("current")


class _AcSysRedundantFanTrayFansStatus_Type(OctetString):
    """Custom type acSysRedundantFanTrayFansStatus based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 1),
    )


_AcSysRedundantFanTrayFansStatus_Type.__name__ = "OctetString"
_AcSysRedundantFanTrayFansStatus_Object = MibTableColumn
acSysRedundantFanTrayFansStatus = _AcSysRedundantFanTrayFansStatus_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 4, 27, 22, 1, 9),
    _AcSysRedundantFanTrayFansStatus_Type()
)
acSysRedundantFanTrayFansStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSysRedundantFanTrayFansStatus.setStatus("current")
_AcSysRedundantPowerSupplyTable_Object = MibTable
acSysRedundantPowerSupplyTable = _AcSysRedundantPowerSupplyTable_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 4, 27, 23)
)
if mibBuilder.loadTexts:
    acSysRedundantPowerSupplyTable.setStatus("current")
_AcSysRedundantPowerSupplyEntry_Object = MibTableRow
acSysRedundantPowerSupplyEntry = _AcSysRedundantPowerSupplyEntry_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 4, 27, 23, 1)
)
acSysRedundantPowerSupplyEntry.setIndexNames(
    (0, "AC-SYSTEM-MIB", "acSysRedundantPowerSupplyIndex"),
)
if mibBuilder.loadTexts:
    acSysRedundantPowerSupplyEntry.setStatus("current")


class _AcSysRedundantPowerSupplyIndex_Type(Unsigned32):
    """Custom type acSysRedundantPowerSupplyIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_AcSysRedundantPowerSupplyIndex_Type.__name__ = "Unsigned32"
_AcSysRedundantPowerSupplyIndex_Object = MibTableColumn
acSysRedundantPowerSupplyIndex = _AcSysRedundantPowerSupplyIndex_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 4, 27, 23, 1, 1),
    _AcSysRedundantPowerSupplyIndex_Type()
)
acSysRedundantPowerSupplyIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    acSysRedundantPowerSupplyIndex.setStatus("current")


class _AcSysRedundantPowerSupplyGeographicalPosition_Type(Unsigned32):
    """Custom type acSysRedundantPowerSupplyGeographicalPosition based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_AcSysRedundantPowerSupplyGeographicalPosition_Type.__name__ = "Unsigned32"
_AcSysRedundantPowerSupplyGeographicalPosition_Object = MibTableColumn
acSysRedundantPowerSupplyGeographicalPosition = _AcSysRedundantPowerSupplyGeographicalPosition_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 4, 27, 23, 1, 2),
    _AcSysRedundantPowerSupplyGeographicalPosition_Type()
)
acSysRedundantPowerSupplyGeographicalPosition.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSysRedundantPowerSupplyGeographicalPosition.setStatus("current")


class _AcSysRedundantPowerSupplyExistence_Type(Integer32):
    """Custom type acSysRedundantPowerSupplyExistence based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("present", 1),
          ("missing", 2))
    )


_AcSysRedundantPowerSupplyExistence_Type.__name__ = "Integer32"
_AcSysRedundantPowerSupplyExistence_Object = MibTableColumn
acSysRedundantPowerSupplyExistence = _AcSysRedundantPowerSupplyExistence_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 4, 27, 23, 1, 3),
    _AcSysRedundantPowerSupplyExistence_Type()
)
acSysRedundantPowerSupplyExistence.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSysRedundantPowerSupplyExistence.setStatus("current")


class _AcSysRedundantPowerSupplyHwversion_Type(SnmpAdminString):
    """Custom type acSysRedundantPowerSupplyHwversion based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_AcSysRedundantPowerSupplyHwversion_Type.__name__ = "SnmpAdminString"
_AcSysRedundantPowerSupplyHwversion_Object = MibTableColumn
acSysRedundantPowerSupplyHwversion = _AcSysRedundantPowerSupplyHwversion_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 4, 27, 23, 1, 4),
    _AcSysRedundantPowerSupplyHwversion_Type()
)
acSysRedundantPowerSupplyHwversion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSysRedundantPowerSupplyHwversion.setStatus("current")


class _AcSysRedundantPowerSupplyLEDs_Type(OctetString):
    """Custom type acSysRedundantPowerSupplyLEDs based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_AcSysRedundantPowerSupplyLEDs_Type.__name__ = "OctetString"
_AcSysRedundantPowerSupplyLEDs_Object = MibTableColumn
acSysRedundantPowerSupplyLEDs = _AcSysRedundantPowerSupplyLEDs_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 4, 27, 23, 1, 5),
    _AcSysRedundantPowerSupplyLEDs_Type()
)
acSysRedundantPowerSupplyLEDs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSysRedundantPowerSupplyLEDs.setStatus("current")


class _AcSysRedundantPowerSupplySeverity_Type(Integer32):
    """Custom type acSysRedundantPowerSupplySeverity based on Integer32"""
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
        *(("cleared", 1),
          ("indeterminate", 2),
          ("warning", 3),
          ("minor", 4),
          ("major", 5),
          ("critical", 6))
    )


_AcSysRedundantPowerSupplySeverity_Type.__name__ = "Integer32"
_AcSysRedundantPowerSupplySeverity_Object = MibTableColumn
acSysRedundantPowerSupplySeverity = _AcSysRedundantPowerSupplySeverity_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 4, 27, 23, 1, 6),
    _AcSysRedundantPowerSupplySeverity_Type()
)
acSysRedundantPowerSupplySeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSysRedundantPowerSupplySeverity.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "AC-SYSTEM-MIB",
    **{"acSystem": acSystem,
       "acSystemConfiguration": acSystemConfiguration,
       "acSysControl": acSysControl,
       "acSysControlProtocolType": acSysControlProtocolType,
       "acSysControlTrunkingToAnalogFunctionalityProfile": acSysControlTrunkingToAnalogFunctionalityProfile,
       "acSysTDM": acSysTDM,
       "acSysTDMClock": acSysTDMClock,
       "acSysTDMClockSource": acSysTDMClockSource,
       "acSysTDMClockEnableFallBack": acSysTDMClockEnableFallBack,
       "acSysTDMClockLocalReference": acSysTDMClockLocalReference,
       "acSysTDMClockMasterSlaveSelection": acSysTDMClockMasterSlaveSelection,
       "acSysTDMClockNetRefSpeed": acSysTDMClockNetRefSpeed,
       "acSysTDMClockAutoFallBackEnable": acSysTDMClockAutoFallBackEnable,
       "acSysTDMClockAutoFallBackRevertingEnable": acSysTDMClockAutoFallBackRevertingEnable,
       "acSysTDMClockBitsReference": acSysTDMClockBitsReference,
       "acSysTDMClockPLLOutOfRange": acSysTDMClockPLLOutOfRange,
       "acSysTDMClockFallbackClock": acSysTDMClockFallbackClock,
       "acSysTDMBus": acSysTDMBus,
       "acSysTDMBusType": acSysTDMBusType,
       "acSysTDMBusSpeed": acSysTDMBusSpeed,
       "acSysTDMBusOutputPort": acSysTDMBusOutputPort,
       "acSysTDMBusOutputStartingChannel": acSysTDMBusOutputStartingChannel,
       "acSysPCM": acSysPCM,
       "acSysPCMLawSelect": acSysPCMLawSelect,
       "acSysPCMIdlePattern": acSysPCMIdlePattern,
       "acSysPCMIdleABCDPattern": acSysPCMIdleABCDPattern,
       "acSysPCMSerialPortAuditIntervalMin": acSysPCMSerialPortAuditIntervalMin,
       "acSysNetworkConfig": acSysNetworkConfig,
       "acSysIP": acSysIP,
       "acSysIPAddress": acSysIPAddress,
       "acSysIPSubNetAddress": acSysIPSubNetAddress,
       "acSysIPDefaultGatewayAddress": acSysIPDefaultGatewayAddress,
       "acSysIPDHCPEnable": acSysIPDHCPEnable,
       "acSysIPDHCPSpeedFactor": acSysIPDHCPSpeedFactor,
       "acSysIPDnsPrimaryServerType": acSysIPDnsPrimaryServerType,
       "acSysIPDnsPrimaryServer": acSysIPDnsPrimaryServer,
       "acSysIPDnsSecondaryServerType": acSysIPDnsSecondaryServerType,
       "acSysIPDnsSecondaryServer": acSysIPDnsSecondaryServer,
       "acSysIPDHCPLeaseRenewalEnable": acSysIPDHCPLeaseRenewalEnable,
       "acSysIPWanInterfaceName": acSysIPWanInterfaceName,
       "acSysIPV6Address": acSysIPV6Address,
       "acMultipleIP": acMultipleIP,
       "acMultipleIPEnable": acMultipleIPEnable,
       "acMultipleIPEnableTPNCPasOAM": acMultipleIPEnableTPNCPasOAM,
       "acMultipleIPEnableDNSasOAM": acMultipleIPEnableDNSasOAM,
       "acMultipleIPEnableNTPasOAM": acMultipleIPEnableNTPasOAM,
       "acMultipleIPEnableSCTPasControl": acMultipleIPEnableSCTPasControl,
       "acMultipleIPEnableNetwotkSeparation": acMultipleIPEnableNetwotkSeparation,
       "acMultipleIPInterfaceTableAction": acMultipleIPInterfaceTableAction,
       "acNetworkIPTable": acNetworkIPTable,
       "acNetworkIPEntry": acNetworkIPEntry,
       "acNetworkIPIndex": acNetworkIPIndex,
       "acNetworkIPIfIndex": acNetworkIPIfIndex,
       "acNetworkIPLocalIPAddress": acNetworkIPLocalIPAddress,
       "acNetworkIPLocalSubnetMask": acNetworkIPLocalSubnetMask,
       "acNetworkIPLocalDefGW": acNetworkIPLocalDefGW,
       "acNetworkIPAdminState": acNetworkIPAdminState,
       "acSysInterfaceTable": acSysInterfaceTable,
       "acSysInterfaceEntry": acSysInterfaceEntry,
       "acSysInterfaceIndex": acSysInterfaceIndex,
       "acSysInterfaceRowStatus": acSysInterfaceRowStatus,
       "acSysInterfaceAction": acSysInterfaceAction,
       "acSysInterfaceActionRes": acSysInterfaceActionRes,
       "acSysInterfaceApplicationTypes": acSysInterfaceApplicationTypes,
       "acSysInterfaceMode": acSysInterfaceMode,
       "acSysInterfaceIPAddress": acSysInterfaceIPAddress,
       "acSysInterfacePrefixLength": acSysInterfacePrefixLength,
       "acSysInterfaceGateway": acSysInterfaceGateway,
       "acSysInterfaceVlanID": acSysInterfaceVlanID,
       "acSysInterfaceName": acSysInterfaceName,
       "acSysInterfacePrimaryDNSServerIPAddress": acSysInterfacePrimaryDNSServerIPAddress,
       "acSysInterfaceSecondaryDNSServerIPAddress": acSysInterfaceSecondaryDNSServerIPAddress,
       "acSysInterfaceUnderlyingInterface": acSysInterfaceUnderlyingInterface,
       "acSysInterfaceUnderlyingDevice": acSysInterfaceUnderlyingDevice,
       "acSysPhysicalPortsTable": acSysPhysicalPortsTable,
       "acSysPhysicalPortsEntry": acSysPhysicalPortsEntry,
       "acSysPhysicalPortsIndex": acSysPhysicalPortsIndex,
       "acSysPhysicalPortsRowStatus": acSysPhysicalPortsRowStatus,
       "acSysPhysicalPortsAction": acSysPhysicalPortsAction,
       "acSysPhysicalPortsActionRes": acSysPhysicalPortsActionRes,
       "acSysPhysicalPortsPort": acSysPhysicalPortsPort,
       "acSysPhysicalPortsMode": acSysPhysicalPortsMode,
       "acSysPhysicalPortsNativeVlan": acSysPhysicalPortsNativeVlan,
       "acSysPhysicalPortsSpeedDuplex": acSysPhysicalPortsSpeedDuplex,
       "acSysPhysicalPortsPortDescription": acSysPhysicalPortsPortDescription,
       "acSysPhysicalPortsGroupMember": acSysPhysicalPortsGroupMember,
       "acSysPhysicalPortsGroupStatus": acSysPhysicalPortsGroupStatus,
       "acSysEtherGroupTable": acSysEtherGroupTable,
       "acSysEtherGroupEntry": acSysEtherGroupEntry,
       "acSysEtherGroupIndex": acSysEtherGroupIndex,
       "acSysEtherGroupRowStatus": acSysEtherGroupRowStatus,
       "acSysEtherGroupAction": acSysEtherGroupAction,
       "acSysEtherGroupActionRes": acSysEtherGroupActionRes,
       "acSysEtherGroupGroup": acSysEtherGroupGroup,
       "acSysEtherGroupMode": acSysEtherGroupMode,
       "acSysEtherGroupMember1": acSysEtherGroupMember1,
       "acSysEtherGroupMember2": acSysEtherGroupMember2,
       "acSysStaticRouteTable": acSysStaticRouteTable,
       "acSysStaticRouteEntry": acSysStaticRouteEntry,
       "acSysStaticRouteIndex": acSysStaticRouteIndex,
       "acSysStaticRouteRowStatus": acSysStaticRouteRowStatus,
       "acSysStaticRouteAction": acSysStaticRouteAction,
       "acSysStaticRouteActionRes": acSysStaticRouteActionRes,
       "acSysStaticRouteInterfaceName": acSysStaticRouteInterfaceName,
       "acSysStaticRouteDeviceName": acSysStaticRouteDeviceName,
       "acSysStaticRouteDestination": acSysStaticRouteDestination,
       "acSysStaticRoutePrefixLength": acSysStaticRoutePrefixLength,
       "acSysStaticRouteGateway": acSysStaticRouteGateway,
       "acSysStaticRouteDescription": acSysStaticRouteDescription,
       "acSysEthernetDeviceTable": acSysEthernetDeviceTable,
       "acSysEthernetDeviceEntry": acSysEthernetDeviceEntry,
       "acSysEthernetDeviceIndex": acSysEthernetDeviceIndex,
       "acSysEthernetDeviceRowStatus": acSysEthernetDeviceRowStatus,
       "acSysEthernetDeviceAction": acSysEthernetDeviceAction,
       "acSysEthernetDeviceActionRes": acSysEthernetDeviceActionRes,
       "acSysEthernetDeviceVlanID": acSysEthernetDeviceVlanID,
       "acSysEthernetDeviceUnderlyingInterface": acSysEthernetDeviceUnderlyingInterface,
       "acSysEthernetDeviceName": acSysEthernetDeviceName,
       "acSyslog": acSyslog,
       "acSyslogServerIPAddress": acSyslogServerIPAddress,
       "acSyslogEnable": acSyslogEnable,
       "acSyslogAcSyslogServerPortNumber": acSyslogAcSyslogServerPortNumber,
       "acSyslogFacility": acSyslogFacility,
       "acSysNTP": acSysNTP,
       "acSysNTPServerIPAddress": acSysNTPServerIPAddress,
       "acSysNTPUtcOffset": acSysNTPUtcOffset,
       "acSysNTPUpdateInterval": acSysNTPUpdateInterval,
       "acSysNTPSecondaryServerIP": acSysNTPSecondaryServerIP,
       "acSysNTPAuthKeyId": acSysNTPAuthKeyId,
       "acSysNTPAuthMd5Key": acSysNTPAuthMd5Key,
       "acSysNTPPrimaryServerAddress": acSysNTPPrimaryServerAddress,
       "acSysNTPSecondaryServerAddress": acSysNTPSecondaryServerAddress,
       "acSysDayLightSavingTime": acSysDayLightSavingTime,
       "acSysDayLightSavingTimeMode": acSysDayLightSavingTimeMode,
       "acSysDayLightSavingTimeOffset": acSysDayLightSavingTimeOffset,
       "acSysDayLightSavingTimeStart": acSysDayLightSavingTimeStart,
       "acSysDayLightSavingTimeEnd": acSysDayLightSavingTimeEnd,
       "acSysWEB": acSysWEB,
       "acSysWEBConfigDisable": acSysWEBConfigDisable,
       "acSysWEBHTTPSOnly": acSysWEBHTTPSOnly,
       "acSysWEBHTTPSPort": acSysWEBHTTPSPort,
       "acSysWEBWebUseRadiusLogin": acSysWEBWebUseRadiusLogin,
       "acSysWEBHTTPSCipherString": acSysWEBHTTPSCipherString,
       "acSysWEBDenyAuthenticationTimer": acSysWEBDenyAuthenticationTimer,
       "acSysWEBWanHttpPort": acSysWEBWanHttpPort,
       "acSysWEBWanHttpsPort": acSysWEBWanHttpsPort,
       "acSysWEBAllowWanHttp": acSysWEBAllowWanHttp,
       "acSysWEBAllowWanHttps": acSysWEBAllowWanHttps,
       "acSysWEBTLSClientCipherString": acSysWEBTLSClientCipherString,
       "acSysWEBUseLdapForLogin": acSysWEBUseLdapForLogin,
       "acSysWEBACLTable": acSysWEBACLTable,
       "acSysWEBACLEntry": acSysWEBACLEntry,
       "acSysWEBACLIndex": acSysWEBACLIndex,
       "acSysWEBACLIP": acSysWEBACLIP,
       "acSysWEBAccess": acSysWEBAccess,
       "acSysWEBAccessTable": acSysWEBAccessTable,
       "acSysWEBAccessEntry": acSysWEBAccessEntry,
       "acSysWEBAccessRowStatus": acSysWEBAccessRowStatus,
       "acSysWEBAccessAction": acSysWEBAccessAction,
       "acSysWEBAccessActionResult": acSysWEBAccessActionResult,
       "acSysWEBAccessIndex": acSysWEBAccessIndex,
       "acSysWEBAccessUserName": acSysWEBAccessUserName,
       "acSysWEBAccessUserCode": acSysWEBAccessUserCode,
       "acSysWEBAccessWebAuthMode": acSysWEBAccessWebAuthMode,
       "acSysNATTraversal": acSysNATTraversal,
       "acSysSTUN": acSysSTUN,
       "acSysSTUNEnable": acSysSTUNEnable,
       "acSysSTUNPrimaryServerIP": acSysSTUNPrimaryServerIP,
       "acSysSTUNSecondaryServerIP": acSysSTUNSecondaryServerIP,
       "acSysSTUNBindingLifeTime": acSysSTUNBindingLifeTime,
       "acSysTelnet": acSysTelnet,
       "acSysTelnetServerEnable": acSysTelnetServerEnable,
       "acSysTelnetServerPort": acSysTelnetServerPort,
       "acSysTelnetServerIdleDisconnect": acSysTelnetServerIdleDisconnect,
       "acSysTelnetSSHServerPort": acSysTelnetSSHServerPort,
       "acSysTelnetSSHServerEnable": acSysTelnetSSHServerEnable,
       "acSysTelnetSSHAdminKey": acSysTelnetSSHAdminKey,
       "acSysTelnetSSHRequirePublicKey": acSysTelnetSSHRequirePublicKey,
       "acSysTelnetServerWanPort": acSysTelnetServerWanPort,
       "acSysTelnetWanSSHServerPort": acSysTelnetWanSSHServerPort,
       "acSysTelnetSSHMaxSessions": acSysTelnetSSHMaxSessions,
       "acSysTelnetSSHMaxPayloadSize": acSysTelnetSSHMaxPayloadSize,
       "acSysTelnetSSHMaxBinaryPacketSize": acSysTelnetSSHMaxBinaryPacketSize,
       "acSysTelnetAllowWanTelnet": acSysTelnetAllowWanTelnet,
       "acSysTelnetAllowWanSSH": acSysTelnetAllowWanSSH,
       "acSysTelnetMaxSessions": acSysTelnetMaxSessions,
       "acSysHTTPClient": acSysHTTPClient,
       "acSysHTTPClientAutoUpdatePredefinedTime": acSysHTTPClientAutoUpdatePredefinedTime,
       "acSysHTTPClientAutoUpdateFrequency": acSysHTTPClientAutoUpdateFrequency,
       "acSysHTTPClientAutoUpdateCmpFile": acSysHTTPClientAutoUpdateCmpFile,
       "acSysHTTPClientCmpFileURL": acSysHTTPClientCmpFileURL,
       "acSysHTTPClientIniFileURL": acSysHTTPClientIniFileURL,
       "acSysHTTPClientIniFileTemplateURL": acSysHTTPClientIniFileTemplateURL,
       "acSysHTTPClientCPTFileURL": acSysHTTPClientCPTFileURL,
       "acSysHTTPClientVPFileURL": acSysHTTPClientVPFileURL,
       "acSysHTTPClientPRTFileURL": acSysHTTPClientPRTFileURL,
       "acSysHTTPClientFXSCoeffFileURL": acSysHTTPClientFXSCoeffFileURL,
       "acSysHTTPClientFXOCoeffFileURL": acSysHTTPClientFXOCoeffFileURL,
       "acSysHTTPClientCASFileURL": acSysHTTPClientCASFileURL,
       "acSysHTTPClientXMLFileUrl": acSysHTTPClientXMLFileUrl,
       "acSysHTTPClientCoderTableFileUrl": acSysHTTPClientCoderTableFileUrl,
       "acSysHTTPClientUserInfoFileURL": acSysHTTPClientUserInfoFileURL,
       "acSysHTTPClientDialPlanFileURL": acSysHTTPClientDialPlanFileURL,
       "acSysHTTPClientTLSPkeyFileUrl": acSysHTTPClientTLSPkeyFileUrl,
       "acSysHTTPClientTLSCertFileUrl": acSysHTTPClientTLSCertFileUrl,
       "acSysHTTPClientTLSRootFileUrl": acSysHTTPClientTLSRootFileUrl,
       "acSysHTTPClientWebLogoFileUrl": acSysHTTPClientWebLogoFileUrl,
       "acSysHTTPClientVideoFontFileURL": acSysHTTPClientVideoFontFileURL,
       "acSysHTTPClientV5PortConfFileURL": acSysHTTPClientV5PortConfFileURL,
       "acSysHTTPClientDataConfigurationFileUrl": acSysHTTPClientDataConfigurationFileUrl,
       "acSysHTTPClientAmdSensitivityFileUrl": acSysHTTPClientAmdSensitivityFileUrl,
       "acSysHTTPClientCliScriptFileUrl": acSysHTTPClientCliScriptFileUrl,
       "acSysHTTPClientConfigurationPackageUrlFile": acSysHTTPClientConfigurationPackageUrlFile,
       "acSysHTTPClientIncrementalIniFileURL": acSysHTTPClientIncrementalIniFileURL,
       "acSysHTTPClientMTCFirmwareUrlFile": acSysHTTPClientMTCFirmwareUrlFile,
       "acSysHTTPClientVMTFirmwareUrlFile": acSysHTTPClientVMTFirmwareUrlFile,
       "acSysHTTPClientTLSRootIncrementalFileUrl": acSysHTTPClientTLSRootIncrementalFileUrl,
       "acSysSNMP": acSysSNMP,
       "acSysSNMPKeepAliveTrapPort": acSysSNMPKeepAliveTrapPort,
       "acSysSNMPEmsColdStrartIndication": acSysSNMPEmsColdStrartIndication,
       "acSysSNMPWanPort": acSysSNMPWanPort,
       "acSysSNMPAllowWanSnmp": acSysSNMPAllowWanSnmp,
       "acSysVLAN": acSysVLAN,
       "acSysVLANOamVlanId": acSysVLANOamVlanId,
       "acSysVLANControlVlanId": acSysVLANControlVlanId,
       "acSysVLANMediaVlanId": acSysVLANMediaVlanId,
       "acSysVLANNetworkServiceClassPriority": acSysVLANNetworkServiceClassPriority,
       "acSysVLANPremiumServiceClassMediaPriority": acSysVLANPremiumServiceClassMediaPriority,
       "acSysVLANGoldServiceClassPriority": acSysVLANGoldServiceClassPriority,
       "acSysVLANBronzeServiceClassPriority": acSysVLANBronzeServiceClassPriority,
       "acSysVLANPremiumServiceClassControlPriority": acSysVLANPremiumServiceClassControlPriority,
       "acSysVLANNetworkServiceClassDiffServ": acSysVLANNetworkServiceClassDiffServ,
       "acSysVLANPremiumServiceClassMediaDiffServ": acSysVLANPremiumServiceClassMediaDiffServ,
       "acSysVLANPremiumServiceClassControlDiffServ": acSysVLANPremiumServiceClassControlDiffServ,
       "acSysVLANGoldServiceClassDiffServ": acSysVLANGoldServiceClassDiffServ,
       "acSysVLANBronzeServiceClassDiffServ": acSysVLANBronzeServiceClassDiffServ,
       "acSysVLANVlanNativeVlanId": acSysVLANVlanNativeVlanId,
       "acSysVLANMode": acSysVLANMode,
       "acSysVLANOsnNativeVlanId": acSysVLANOsnNativeVlanId,
       "acSysVlanMapTable": acSysVlanMapTable,
       "acSysVlanMapEntry": acSysVlanMapEntry,
       "acSysVlanMapIndex": acSysVlanMapIndex,
       "acSysVlanMapRowStatus": acSysVlanMapRowStatus,
       "acSysVlanMapAction": acSysVlanMapAction,
       "acSysVlanMapActionRes": acSysVlanMapActionRes,
       "acSysVlanMapDiffServ": acSysVlanMapDiffServ,
       "acSysVlanMapVlanPriority": acSysVlanMapVlanPriority,
       "acSysSCTP": acSysSCTP,
       "acSysSCTPHeartBeatInterval": acSysSCTPHeartBeatInterval,
       "acSysSCTPT4SACKTimer": acSysSCTPT4SACKTimer,
       "acSysSCTPCheckSumMethod": acSysSCTPCheckSumMethod,
       "acSysSCTPHostName": acSysSCTPHostName,
       "acSysSCTPAssociationsNum": acSysSCTPAssociationsNum,
       "acSysEthernetPort": acSysEthernetPort,
       "acSysEthernetPortPhyConfiguration": acSysEthernetPortPhyConfiguration,
       "acSysPOE": acSysPOE,
       "acSysPOETable": acSysPOETable,
       "acSysPOEEntry": acSysPOEEntry,
       "acSysPOEIndex": acSysPOEIndex,
       "acSysPOERowStatus": acSysPOERowStatus,
       "acSysPOEAction": acSysPOEAction,
       "acSysPOEActionRes": acSysPOEActionRes,
       "acSysPOEPortEnable": acSysPOEPortEnable,
       "acSysPOEPortPower": acSysPOEPortPower,
       "acSysPOEPortATEnable": acSysPOEPortATEnable,
       "acSysNetworkSettings": acSysNetworkSettings,
       "acSysNetworkSettingsDisableICMPRedirects": acSysNetworkSettingsDisableICMPRedirects,
       "acSysNetworkSettingsDisableICMPUnreachable": acSysNetworkSettingsDisableICMPUnreachable,
       "acSysMiscConfig": acSysMiscConfig,
       "acSysDiagnostics": acSysDiagnostics,
       "acSysDiagnosticsEnable": acSysDiagnosticsEnable,
       "acSysDiagnosticsEnablePerformanceThresholdAlarms": acSysDiagnosticsEnablePerformanceThresholdAlarms,
       "acSysDiagnosticsListOfActivitiesToLog": acSysDiagnosticsListOfActivitiesToLog,
       "acSysGenericINI": acSysGenericINI,
       "acSysGenericINILine": acSysGenericINILine,
       "acSysGenericINISecureStartup": acSysGenericINISecureStartup,
       "acSysGenericCli": acSysGenericCli,
       "acSysGenericCliCommand": acSysGenericCliCommand,
       "acSysGenericCliCommandResponse": acSysGenericCliCommandResponse,
       "acSysLicenseKey": acSysLicenseKey,
       "acSysLicenseKeyString": acSysLicenseKeyString,
       "acSysLicenseKeyActiveList": acSysLicenseKeyActiveList,
       "acSysLicenseKeyProductKey": acSysLicenseKeyProductKey,
       "acSysFile": acSysFile,
       "acSysFileCpt": acSysFileCpt,
       "acSysFileVp": acSysFileVp,
       "acSysFilePrerecordedTones": acSysFilePrerecordedTones,
       "acSysFileXml": acSysFileXml,
       "acSysFileExternalCoder": acSysFileExternalCoder,
       "acSysFileUserInfo": acSysFileUserInfo,
       "acSysFileDialPlanFileName": acSysFileDialPlanFileName,
       "acSysFileTLSPkeyFileName": acSysFileTLSPkeyFileName,
       "acSysFileTLSCertFileName": acSysFileTLSCertFileName,
       "acSysFileTLSRootFileName": acSysFileTLSRootFileName,
       "acSysFileFirstVideoFontFileName": acSysFileFirstVideoFontFileName,
       "acSysFileSecondVideoFontFileName": acSysFileSecondVideoFontFileName,
       "acSysFileThirdVideoFontFileName": acSysFileThirdVideoFontFileName,
       "acSysFileV5PortConfFileName": acSysFileV5PortConfFileName,
       "acSysFileAmdSensitivityFileName": acSysFileAmdSensitivityFileName,
       "acSysSecurity": acSysSecurity,
       "acSysSecurityTLSVersion": acSysSecurityTLSVersion,
       "acSysSecurityOcspEnable": acSysSecurityOcspEnable,
       "acSysSecurityOcspServerIPType": acSysSecurityOcspServerIPType,
       "acSysSecurityOcspServerIP": acSysSecurityOcspServerIP,
       "acSysSecurityOcspServerPort": acSysSecurityOcspServerPort,
       "acSysSecurityOcspDefaultResponse": acSysSecurityOcspDefaultResponse,
       "acSysSecurityTLSFIPS140Mode": acSysSecurityTLSFIPS140Mode,
       "acSysSecurityGenCsrSubjectName": acSysSecurityGenCsrSubjectName,
       "acSysSecuritySelfSignedCertificateSubjectName": acSysSecuritySelfSignedCertificateSubjectName,
       "acSysSecurityOcspSecondaryServerIPType": acSysSecurityOcspSecondaryServerIPType,
       "acSysSecurityOcspSecondaryServerIP": acSysSecurityOcspSecondaryServerIP,
       "acSysSecurityHTTPSRequireClientCertificate": acSysSecurityHTTPSRequireClientCertificate,
       "acSysSecurityAUPDVerifyCertificates": acSysSecurityAUPDVerifyCertificates,
       "acSysSecurityRequireStrictCertification": acSysSecurityRequireStrictCertification,
       "acSysSecurityTLSExpiryCheckStart": acSysSecurityTLSExpiryCheckStart,
       "acSysSecurityTLSExpiryCheckPeriod": acSysSecurityTLSExpiryCheckPeriod,
       "acSysIKE": acSysIKE,
       "acSysIKEPolicyTable": acSysIKEPolicyTable,
       "acSysIKEPolicyEntry": acSysIKEPolicyEntry,
       "acSysIKEPolicyIndex": acSysIKEPolicyIndex,
       "acSysIKEPolicyRowStatus": acSysIKEPolicyRowStatus,
       "acSysIKEPolicyAction": acSysIKEPolicyAction,
       "acSysIKEPolicyActionRes": acSysIKEPolicyActionRes,
       "acSysIKEPolicyShardKey": acSysIKEPolicyShardKey,
       "acSysIKEPolicyLifeInSeconds": acSysIKEPolicyLifeInSeconds,
       "acSysIKEPolicyLifeInKB": acSysIKEPolicyLifeInKB,
       "acSysIKEPolicyProposal0Encryption": acSysIKEPolicyProposal0Encryption,
       "acSysIKEPolicyProposal1Encryption": acSysIKEPolicyProposal1Encryption,
       "acSysIKEPolicyProposal2Encryption": acSysIKEPolicyProposal2Encryption,
       "acSysIKEPolicyProposal3Encryption": acSysIKEPolicyProposal3Encryption,
       "acSysIKEPolicyProposal0Authentication": acSysIKEPolicyProposal0Authentication,
       "acSysIKEPolicyProposal1Authentication": acSysIKEPolicyProposal1Authentication,
       "acSysIKEPolicyProposal2Authentication": acSysIKEPolicyProposal2Authentication,
       "acSysIKEPolicyProposal3Authentication": acSysIKEPolicyProposal3Authentication,
       "acSysIKEPolicyProposal0DHGroup": acSysIKEPolicyProposal0DHGroup,
       "acSysIKEPolicyProposal1DHGroup": acSysIKEPolicyProposal1DHGroup,
       "acSysIKEPolicyProposal2DHGroup": acSysIKEPolicyProposal2DHGroup,
       "acSysIKEPolicyProposal3DHGroup": acSysIKEPolicyProposal3DHGroup,
       "acSysIKEPolicyAuthenticationMethod": acSysIKEPolicyAuthenticationMethod,
       "acSysIPSec": acSysIPSec,
       "acSysIPSecEnable": acSysIPSecEnable,
       "acSysIPSecDpdMode": acSysIPSecDpdMode,
       "acSysIPSecIKECertificateExtValidate": acSysIPSecIKECertificateExtValidate,
       "acSysIPSecSPDTable": acSysIPSecSPDTable,
       "acSysIPSecSPDEntry": acSysIPSecSPDEntry,
       "acSysIPSecSPDIndex": acSysIPSecSPDIndex,
       "acSysIPSecSPDRowStatus": acSysIPSecSPDRowStatus,
       "acSysIPSecSPDAction": acSysIPSecSPDAction,
       "acSysIPSecSPDActionRes": acSysIPSecSPDActionRes,
       "acSysIPSecSPDPolicyRemoteIPAddr": acSysIPSecSPDPolicyRemoteIPAddr,
       "acSysIPSecSPDPolicySrcPort": acSysIPSecSPDPolicySrcPort,
       "acSysIPSecSPDPolicyDestPort": acSysIPSecSPDPolicyDestPort,
       "acSysIPSecSPDPolicyProtocol": acSysIPSecSPDPolicyProtocol,
       "acSysIPSecSPDKeyExchangeMethodIndex": acSysIPSecSPDKeyExchangeMethodIndex,
       "acSysIPSecSPDLifeInSeconds": acSysIPSecSPDLifeInSeconds,
       "acSysIPSecSPDLifeInKB": acSysIPSecSPDLifeInKB,
       "acSysIPSecSPDProposal0Encryption": acSysIPSecSPDProposal0Encryption,
       "acSysIPSecSPDProposal1Encryption": acSysIPSecSPDProposal1Encryption,
       "acSysIPSecSPDProposal2Encryption": acSysIPSecSPDProposal2Encryption,
       "acSysIPSecSPDProposal3Encryption": acSysIPSecSPDProposal3Encryption,
       "acSysIPSecSPDProposal0Authentication": acSysIPSecSPDProposal0Authentication,
       "acSysIPSecSPDProposal1Authentication": acSysIPSecSPDProposal1Authentication,
       "acSysIPSecSPDProposal2Authentication": acSysIPSecSPDProposal2Authentication,
       "acSysIPSecSPDProposal3Authentication": acSysIPSecSPDProposal3Authentication,
       "acSysIPSecSPDPolicyLocalIPAddrType": acSysIPSecSPDPolicyLocalIPAddrType,
       "acSysIPSecSPDMode": acSysIPSecSPDMode,
       "acSysIPSecSPDPolicyRemoteTunnelIPAddress": acSysIPSecSPDPolicyRemoteTunnelIPAddress,
       "acSysIPSecSPDPolicyLocalTunnelIPAddress": acSysIPSecSPDPolicyLocalTunnelIPAddress,
       "acSysIPSecSPDPolicyRemoteTunnelSubnetMask": acSysIPSecSPDPolicyRemoteTunnelSubnetMask,
       "acSysIPsecProposalTable": acSysIPsecProposalTable,
       "acSysIPsecProposalEntry": acSysIPsecProposalEntry,
       "acSysIPsecProposalIndex": acSysIPsecProposalIndex,
       "acSysIPsecProposalRowStatus": acSysIPsecProposalRowStatus,
       "acSysIPsecProposalAction": acSysIPsecProposalAction,
       "acSysIPsecProposalActionRes": acSysIPsecProposalActionRes,
       "acSysIPsecProposalEncryptionAlgorithm": acSysIPsecProposalEncryptionAlgorithm,
       "acSysIPsecProposalAuthenticationAlgorithm": acSysIPsecProposalAuthenticationAlgorithm,
       "acSysIPsecProposalDiffieHellmanGroup": acSysIPsecProposalDiffieHellmanGroup,
       "acSysIPsecSATable": acSysIPsecSATable,
       "acSysIPsecSAEntry": acSysIPsecSAEntry,
       "acSysIPsecSAIndex": acSysIPsecSAIndex,
       "acSysIPsecSARowStatus": acSysIPsecSARowStatus,
       "acSysIPsecSAAction": acSysIPsecSAAction,
       "acSysIPsecSAActionRes": acSysIPsecSAActionRes,
       "acSysIPsecSARemoteEndpointAddress": acSysIPsecSARemoteEndpointAddress,
       "acSysIPsecSAAuthenticationMethod": acSysIPsecSAAuthenticationMethod,
       "acSysIPsecSASharedKey": acSysIPsecSASharedKey,
       "acSysIPsecSASourcePort": acSysIPsecSASourcePort,
       "acSysIPsecSADestPort": acSysIPsecSADestPort,
       "acSysIPsecSAProtocol": acSysIPsecSAProtocol,
       "acSysIPsecSAPhase1SaLifetimeInSec": acSysIPsecSAPhase1SaLifetimeInSec,
       "acSysIPsecSAPhase2SaLifetimeInSec": acSysIPsecSAPhase2SaLifetimeInSec,
       "acSysIPsecSAPhase2SaLifetimeInKB": acSysIPsecSAPhase2SaLifetimeInKB,
       "acSysIPsecSADPDmode": acSysIPsecSADPDmode,
       "acSysIPsecSAIPsecMode": acSysIPsecSAIPsecMode,
       "acSysIPsecSARemoteTunnelAddress": acSysIPsecSARemoteTunnelAddress,
       "acSysIPsecSARemoteSubnetIPAddress": acSysIPsecSARemoteSubnetIPAddress,
       "acSysIPsecSARemoteSubnetPrefixLength": acSysIPsecSARemoteSubnetPrefixLength,
       "acSysIPsecSAInterfaceName": acSysIPsecSAInterfaceName,
       "acFirewall": acFirewall,
       "acSysAccessListTable": acSysAccessListTable,
       "acSysAccessListEntry": acSysAccessListEntry,
       "acSysAccessListIndex": acSysAccessListIndex,
       "acSysAccessListRowStatus": acSysAccessListRowStatus,
       "acSysAccessListAction": acSysAccessListAction,
       "acSysAccessListActionRes": acSysAccessListActionRes,
       "acSysAccessListSourceIP": acSysAccessListSourceIP,
       "acSysAccessListNetMask": acSysAccessListNetMask,
       "acSysAccessListStartPort": acSysAccessListStartPort,
       "acSysAccessListEndPort": acSysAccessListEndPort,
       "acSysAccessListProtocol": acSysAccessListProtocol,
       "acSysAccessListPacketSize": acSysAccessListPacketSize,
       "acSysAccessListByteRate": acSysAccessListByteRate,
       "acSysAccessListByteBurst": acSysAccessListByteBurst,
       "acSysAccessListAllowType": acSysAccessListAllowType,
       "acSysAccessListMatchCount": acSysAccessListMatchCount,
       "acSysAccessListInterfaceName": acSysAccessListInterfaceName,
       "acSysAccessListUseSpecificInterface": acSysAccessListUseSpecificInterface,
       "acSysAccessListSourcePort": acSysAccessListSourcePort,
       "acSysAccessListPrefixLength": acSysAccessListPrefixLength,
       "acSysMediaEncription": acSysMediaEncription,
       "acSysMediaEncriptionRTPAuthenticationDisableTx": acSysMediaEncriptionRTPAuthenticationDisableTx,
       "acSysMediaEncriptionRTPAuthenticationDisableRx": acSysMediaEncriptionRTPAuthenticationDisableRx,
       "acSysMediaEncriptionRTPEncryptionDisableTx": acSysMediaEncriptionRTPEncryptionDisableTx,
       "acSysMediaEncriptionRTPEncryptionDisableRx": acSysMediaEncriptionRTPEncryptionDisableRx,
       "acSysMediaEncriptionRTCPEncryptionDisableTx": acSysMediaEncriptionRTCPEncryptionDisableTx,
       "acSysMediaEncriptionRTCPEncryptionDisableRx": acSysMediaEncriptionRTCPEncryptionDisableRx,
       "acSysSRTP": acSysSRTP,
       "acSysSRTPPacketMKISize": acSysSRTPPacketMKISize,
       "acSys802dot1x": acSys802dot1x,
       "acSys802dot1xMode": acSys802dot1xMode,
       "acSys802dot1xUsername": acSys802dot1xUsername,
       "acSys802dot1xPassword": acSys802dot1xPassword,
       "acSys802dot1xVerifyPeerCertificate": acSys802dot1xVerifyPeerCertificate,
       "acSysTLSContexts": acSysTLSContexts,
       "acSysTLSContextsTable": acSysTLSContextsTable,
       "acSysTLSContextsEntry": acSysTLSContextsEntry,
       "acSysTLSContextsIndex": acSysTLSContextsIndex,
       "acSysTLSContextsRowStatus": acSysTLSContextsRowStatus,
       "acSysTLSContextsAction": acSysTLSContextsAction,
       "acSysTLSContextsActionResult": acSysTLSContextsActionResult,
       "acSysTLSContextsName": acSysTLSContextsName,
       "acSysTLSContextsTlsVersion": acSysTLSContextsTlsVersion,
       "acSysTLSContextsDTLSVersion": acSysTLSContextsDTLSVersion,
       "acSysTLSContextsCipherServer": acSysTLSContextsCipherServer,
       "acSysTLSContextsCipherClient": acSysTLSContextsCipherClient,
       "acSysTLSContextsCipherServer13": acSysTLSContextsCipherServer13,
       "acSysTLSContextsCipherClient13": acSysTLSContextsCipherClient13,
       "acSysTLSContextsExchangeGroups": acSysTLSContextsExchangeGroups,
       "acSysTLSContextsStrictValidation": acSysTLSContextsStrictValidation,
       "acSysTLSContextsDHKeySize": acSysTLSContextsDHKeySize,
       "acSysTLSContextsTlsRenegotiation": acSysTLSContextsTlsRenegotiation,
       "acSysSerialIF": acSysSerialIF,
       "acSysSerialIFBaudRate": acSysSerialIFBaudRate,
       "acSysSerialIFData": acSysSerialIFData,
       "acSysSerialIFParity": acSysSerialIFParity,
       "acSysSerialIFStop": acSysSerialIFStop,
       "acSysSerialIFFlowControl": acSysSerialIFFlowControl,
       "acVoiceStream": acVoiceStream,
       "acVoiceStreamStatus": acVoiceStreamStatus,
       "acVoiceStreamUploadMethod": acVoiceStreamUploadMethod,
       "acVoiceStreamUploadPostUri": acVoiceStreamUploadPostUri,
       "acSysAMS": acSysAMS,
       "acSysAMSProfile": acSysAMSProfile,
       "acSysAMSApsIpAddress": acSysAMSApsIpAddress,
       "acSysAMSApsPort": acSysAMSApsPort,
       "acSysAMSPrimaryLanguage": acSysAMSPrimaryLanguage,
       "acSysAMSSecondaryLanguage": acSysAMSSecondaryLanguage,
       "acSysAMSAPSProfile": acSysAMSAPSProfile,
       "acSysAMSForceRepositoryEnable": acSysAMSForceRepositoryEnable,
       "acSysNetworkFileSystem": acSysNetworkFileSystem,
       "acSysNFSTable": acSysNFSTable,
       "acSysNFSEntry": acSysNFSEntry,
       "acSysNFSIndex": acSysNFSIndex,
       "acSysNFSRowStatus": acSysNFSRowStatus,
       "acSysNFSAction": acSysNFSAction,
       "acSysNFSActionRes": acSysNFSActionRes,
       "acSysNFSHostOrIP": acSysNFSHostOrIP,
       "acSysNFSRootPath": acSysNFSRootPath,
       "acSysNFSNfsVersion": acSysNFSNfsVersion,
       "acSysNFSAuthType": acSysNFSAuthType,
       "acSysNFSUID": acSysNFSUID,
       "acSysNFSGID": acSysNFSGID,
       "acSysNFSVlanType": acSysNFSVlanType,
       "acSysHA": acSysHA,
       "acSysHAGlobalIPAddress": acSysHAGlobalIPAddress,
       "acSysHARemoteAddress": acSysHARemoteAddress,
       "acSysHARevertive": acSysHARevertive,
       "acSysHAPriority": acSysHAPriority,
       "acSysHARedundantPriority": acSysHARedundantPriority,
       "acSysHAPingEnabled": acSysHAPingEnabled,
       "acSysHAPingDestination": acSysHAPingDestination,
       "acSysHAPingSourceIfName": acSysHAPingSourceIfName,
       "acSysHAPingTimeout": acSysHAPingTimeout,
       "acSysHAPingRetries": acSysHAPingRetries,
       "acSysTransmission": acSysTransmission,
       "acSysTransmissionType": acSysTransmissionType,
       "acSysTiming": acSysTiming,
       "acSysTimingMode": acSysTimingMode,
       "acSysTimingValidationTime": acSysTimingValidationTime,
       "acSysTimingClockToDeriveA": acSysTimingClockToDeriveA,
       "acSysTimingClockToDeriveB": acSysTimingClockToDeriveB,
       "acSysTimingExternalIFType": acSysTimingExternalIFType,
       "acSysTimingLoopBackRef1": acSysTimingLoopBackRef1,
       "acSysTimingLoopBackRef2": acSysTimingLoopBackRef2,
       "acSysTimingTransmitControl": acSysTimingTransmitControl,
       "acSysTimingE1LineBuildOut": acSysTimingE1LineBuildOut,
       "acSysTimingT1LineBuildOut": acSysTimingT1LineBuildOut,
       "acSysLDAP": acSysLDAP,
       "acSysLDAPServerIp": acSysLDAPServerIp,
       "acSysLDAPServerPort": acSysLDAPServerPort,
       "acSysLDAPServerMaxRespondTime": acSysLDAPServerMaxRespondTime,
       "acSysLDAPServerDomainName": acSysLDAPServerDomainName,
       "acSysLDAPSearchDN": acSysLDAPSearchDN,
       "acSysLDAPPassword": acSysLDAPPassword,
       "acSysLDAPBindDN": acSysLDAPBindDN,
       "acSysLDAPServiceEnable": acSysLDAPServiceEnable,
       "acSysLDAPCacheEnable": acSysLDAPCacheEnable,
       "acSysLDAPCacheEntryTimeout": acSysLDAPCacheEntryTimeout,
       "acSysLDAPCacheEntryRemovalTimeout": acSysLDAPCacheEntryRemovalTimeout,
       "acSysLdapConfigurationTable": acSysLdapConfigurationTable,
       "acSysLdapConfigurationEntry": acSysLdapConfigurationEntry,
       "acSysLdapConfigurationIndex": acSysLdapConfigurationIndex,
       "acSysLdapConfigurationRowStatus": acSysLdapConfigurationRowStatus,
       "acSysLdapConfigurationAction": acSysLdapConfigurationAction,
       "acSysLdapConfigurationActionRes": acSysLdapConfigurationActionRes,
       "acSysLdapConfigurationServerIp": acSysLdapConfigurationServerIp,
       "acSysLdapConfigurationServerPort": acSysLdapConfigurationServerPort,
       "acSysLdapConfigurationMaxRespondTime": acSysLdapConfigurationMaxRespondTime,
       "acSysLdapConfigurationServerDomainName": acSysLdapConfigurationServerDomainName,
       "acSysLdapConfigurationPassword": acSysLdapConfigurationPassword,
       "acSysLdapConfigurationBindDn": acSysLdapConfigurationBindDn,
       "acSysLdapConfigurationInterfaceType": acSysLdapConfigurationInterfaceType,
       "acSysLdapConfigurationConnectionStatus": acSysLdapConfigurationConnectionStatus,
       "acSysLdapServersSearchDNsTable": acSysLdapServersSearchDNsTable,
       "acSysLdapServersSearchDNsEntry": acSysLdapServersSearchDNsEntry,
       "acSysLdapServersSearchDNsLdapConfigurationIndex": acSysLdapServersSearchDNsLdapConfigurationIndex,
       "acSysLdapServersSearchDNsInternalIndex": acSysLdapServersSearchDNsInternalIndex,
       "acSysLdapServersSearchDNsRowStatus": acSysLdapServersSearchDNsRowStatus,
       "acSysLdapServersSearchDNsAction": acSysLdapServersSearchDNsAction,
       "acSysLdapServersSearchDNsActionRes": acSysLdapServersSearchDNsActionRes,
       "acSysLdapServersSearchDNsBasePath": acSysLdapServersSearchDNsBasePath,
       "asSysNqm": asSysNqm,
       "acSysNqmSenderTable": acSysNqmSenderTable,
       "acSysNqmSenderEntry": acSysNqmSenderEntry,
       "acSysNqmSenderIndex": acSysNqmSenderIndex,
       "acSysNqmSenderRowStatus": acSysNqmSenderRowStatus,
       "acSysNqmSenderAction": acSysNqmSenderAction,
       "acSysNqmSenderActionRes": acSysNqmSenderActionRes,
       "acSysNqmSenderSenderName": acSysNqmSenderSenderName,
       "acSysNqmSenderActive": acSysNqmSenderActive,
       "acSysNqmSenderTargetIpAddress": acSysNqmSenderTargetIpAddress,
       "acSysNqmSenderTargetPort": acSysNqmSenderTargetPort,
       "acSysNqmSenderPacketInterval": acSysNqmSenderPacketInterval,
       "acSysNqmSenderPayloadSize": acSysNqmSenderPayloadSize,
       "acSysNqmSenderIpTos": acSysNqmSenderIpTos,
       "acSysNqmSenderTimeout": acSysNqmSenderTimeout,
       "acSysNqmSenderRttThreshold": acSysNqmSenderRttThreshold,
       "acSysNqmSenderJitterThreshold": acSysNqmSenderJitterThreshold,
       "acSysNqmSenderPacketLossThershold": acSysNqmSenderPacketLossThershold,
       "acSysNqmSenderProbingConfigName": acSysNqmSenderProbingConfigName,
       "acSysNqmSenderSourceInterfaceName": acSysNqmSenderSourceInterfaceName,
       "acSysNqmProbingTable": acSysNqmProbingTable,
       "acSysNqmProbingEntry": acSysNqmProbingEntry,
       "acSysNqmProbingIndex": acSysNqmProbingIndex,
       "acSysNqmProbingRowStatus": acSysNqmProbingRowStatus,
       "acSysNqmProbingAction": acSysNqmProbingAction,
       "acSysNqmProbingActionRes": acSysNqmProbingActionRes,
       "acSysNqmProbingProbeName": acSysNqmProbingProbeName,
       "acSysNqmProbingDuration": acSysNqmProbingDuration,
       "acSysNqmProbingFrequency": acSysNqmProbingFrequency,
       "acSysNqmProbingLifeSpan": acSysNqmProbingLifeSpan,
       "acSysNqmProbingStartTime": acSysNqmProbingStartTime,
       "acSysNqmProbingHistoryEntriesToKeep": acSysNqmProbingHistoryEntriesToKeep,
       "acSysNqmResponderTable": acSysNqmResponderTable,
       "acSysNqmResponderEntry": acSysNqmResponderEntry,
       "acSysNqmResponderIndex": acSysNqmResponderIndex,
       "acSysNqmResponderRowStatus": acSysNqmResponderRowStatus,
       "acSysNqmResponderAction": acSysNqmResponderAction,
       "acSysNqmResponderActionRes": acSysNqmResponderActionRes,
       "acSysNqmResponderResponderName": acSysNqmResponderResponderName,
       "acSysNqmResponderActive": acSysNqmResponderActive,
       "acSysNqmResponderLocalPort": acSysNqmResponderLocalPort,
       "acSysNqmResponderSourceInterfaceName": acSysNqmResponderSourceInterfaceName,
       "acSysLicenseServer": acSysLicenseServer,
       "acSysLicenseServerPrimaryIP": acSysLicenseServerPrimaryIP,
       "acSysLicenseServerSecondaryIP": acSysLicenseServerSecondaryIP,
       "acSysLicenseServerPort": acSysLicenseServerPort,
       "acSysLicenseServerUsername": acSysLicenseServerUsername,
       "acSysLicenseServerPassword": acSysLicenseServerPassword,
       "acSysLicenseServerEnable": acSysLicenseServerEnable,
       "acSysLicenseServerActionStatus": acSysLicenseServerActionStatus,
       "acSysLicenseServerPrimaryAddress": acSysLicenseServerPrimaryAddress,
       "acSysLicenseServerSecondaryAddress": acSysLicenseServerSecondaryAddress,
       "acSysFloatingLicense": acSysFloatingLicense,
       "acSysFloatingLicenseEnable": acSysFloatingLicenseEnable,
       "acSysFloatingLicensePrimaryIP": acSysFloatingLicensePrimaryIP,
       "acSysFloatingLicenseSecondaryIP": acSysFloatingLicenseSecondaryIP,
       "acSysFloatingLicensePort": acSysFloatingLicensePort,
       "acSysFloatingLicenseUsername": acSysFloatingLicenseUsername,
       "acSysFloatingLicensePassword": acSysFloatingLicensePassword,
       "acSysFloatingLicenseUpdate": acSysFloatingLicenseUpdate,
       "acSysFloatingLicenseServerStatus": acSysFloatingLicenseServerStatus,
       "acSysFloatingLicenseOvocProductID": acSysFloatingLicenseOvocProductID,
       "acSysFloatingLicensePrimaryAddress": acSysFloatingLicensePrimaryAddress,
       "acSystemStatus": acSystemStatus,
       "acSysType": acSysType,
       "acSysTypeProduct": acSysTypeProduct,
       "acSysTypeDSP": acSysTypeDSP,
       "acSysTypeModule": acSysTypeModule,
       "acSysTypeCPUSpeed": acSysTypeCPUSpeed,
       "acSysTypeOSType": acSysTypeOSType,
       "acSysVersion": acSysVersion,
       "acSysVersionSoftware": acSysVersionSoftware,
       "acSysVersionFlash": acSysVersionFlash,
       "acSysVersionIniFile": acSysVersionIniFile,
       "acSysVersionSoftwareDate": acSysVersionSoftwareDate,
       "acSysId": acSysId,
       "acSysIdName": acSysIdName,
       "acSysIdSerialNumber": acSysIdSerialNumber,
       "acSysIdSlotNumber": acSysIdSlotNumber,
       "acSysIdFirstSerialNumber": acSysIdFirstSerialNumber,
       "acSysIdSerialNumberString": acSysIdSerialNumberString,
       "acSysIdProductClass": acSysIdProductClass,
       "acSysIdModelName": acSysIdModelName,
       "acSysCount": acSysCount,
       "acSysCountDSPs": acSysCountDSPs,
       "acSysCountChannels": acSysCountChannels,
       "acSysCountTrunks": acSysCountTrunks,
       "acSysState": acSysState,
       "acSysStateTemperature": acSysStateTemperature,
       "acSysStateOperational": acSysStateOperational,
       "acSysStateHAupdateInProgress": acSysStateHAupdateInProgress,
       "acSysStateGWSeverity": acSysStateGWSeverity,
       "acSysStateIsPstnManagementEnable": acSysStateIsPstnManagementEnable,
       "acSysStateErrorMessage": acSysStateErrorMessage,
       "acSysStateErrorID": acSysStateErrorID,
       "acSysStateDataCpuUtilization": acSysStateDataCpuUtilization,
       "acSysStateDataMemoryUtilization": acSysStateDataMemoryUtilization,
       "acSysStateVoIpCpuUtilization": acSysStateVoIpCpuUtilization,
       "acSysStateVoIpMemoryUtilization": acSysStateVoIpMemoryUtilization,
       "acSysStateManagedByEMS": acSysStateManagedByEMS,
       "acSysStateMonitoredBySEM": acSysStateMonitoredBySEM,
       "acSysStateBurnFlag": acSysStateBurnFlag,
       "acSysStateResetFlag": acSysStateResetFlag,
       "acSysNetwork": acSysNetwork,
       "acSysEthernet": acSysEthernet,
       "acSysEthernetFirstPortDuplexMode": acSysEthernetFirstPortDuplexMode,
       "acSysEthernetFirstPortSpeed": acSysEthernetFirstPortSpeed,
       "acSysEthernetSecondPortDuplexMode": acSysEthernetSecondPortDuplexMode,
       "acSysEthernetSecondPortSpeed": acSysEthernetSecondPortSpeed,
       "acSysEthernetActivePortNumber": acSysEthernetActivePortNumber,
       "acSysEthernetPowerBudget": acSysEthernetPowerBudget,
       "acSysEthernetPowerAllocated": acSysEthernetPowerAllocated,
       "acSysEthernetPowerRemaining": acSysEthernetPowerRemaining,
       "acSysEthernetStatusTable": acSysEthernetStatusTable,
       "acSysEthernetStatusEntry": acSysEthernetStatusEntry,
       "acSysEthernetStatusIndex": acSysEthernetStatusIndex,
       "acSysEthernetStatusPortDuplexMode": acSysEthernetStatusPortDuplexMode,
       "acSysEthernetStatusPortSpeed": acSysEthernetStatusPortSpeed,
       "acSysEthernetStatusActivePortNumber": acSysEthernetStatusActivePortNumber,
       "acSysEthernetStatusPortState": acSysEthernetStatusPortState,
       "acSysEthernetStatusPowerOverEthernet": acSysEthernetStatusPowerOverEthernet,
       "acSysEthernetStatusAllocatedPower": acSysEthernetStatusAllocatedPower,
       "acSysEthernetStatusGroup": acSysEthernetStatusGroup,
       "acSysEthernetStatusPowerOverEthernetDetails": acSysEthernetStatusPowerOverEthernetDetails,
       "acSysEthernetStatusPortType": acSysEthernetStatusPortType,
       "acSysWanStatusTable": acSysWanStatusTable,
       "acSysWanStatusEntry": acSysWanStatusEntry,
       "acSysWanStatusIndex": acSysWanStatusIndex,
       "acSysWanStatusPortType": acSysWanStatusPortType,
       "acSysWanStatusPortDuplexMode": acSysWanStatusPortDuplexMode,
       "acSysWanStatusPortSpeed": acSysWanStatusPortSpeed,
       "acSysWanStatusActivePortNumber": acSysWanStatusActivePortNumber,
       "acSysWanStatusPortState": acSysWanStatusPortState,
       "acSysWanStatusPowerOverEthernet": acSysWanStatusPowerOverEthernet,
       "acSysEthernetRedundantStatusTable": acSysEthernetRedundantStatusTable,
       "acSysEthernetRedundantStatusEntry": acSysEthernetRedundantStatusEntry,
       "acSysEthernetRedundantStatusIndex": acSysEthernetRedundantStatusIndex,
       "acSysEthernetRedundantStatusPortDuplexMode": acSysEthernetRedundantStatusPortDuplexMode,
       "acSysEthernetRedundantStatusPortSpeed": acSysEthernetRedundantStatusPortSpeed,
       "acSysEthernetRedundantStatusActivePortNumber": acSysEthernetRedundantStatusActivePortNumber,
       "acSysEthernetRedundantStatusPortState": acSysEthernetRedundantStatusPortState,
       "acSysEthernetRedundantStatusPowerOverEthernet": acSysEthernetRedundantStatusPowerOverEthernet,
       "acSysEthernetRedundantStatusAllocatedPower": acSysEthernetRedundantStatusAllocatedPower,
       "acSysEthernetRedundantStatusGroup": acSysEthernetRedundantStatusGroup,
       "acSysEthernetRedundantStatusPowerOverEthernetDetails": acSysEthernetRedundantStatusPowerOverEthernetDetails,
       "acSysMultiWanStatusTable": acSysMultiWanStatusTable,
       "acSysMultiWanStatusEntry": acSysMultiWanStatusEntry,
       "acSysMultiWanStatusSite": acSysMultiWanStatusSite,
       "acSysMultiWanStatusPort": acSysMultiWanStatusPort,
       "acSysMultiWanStatusType": acSysMultiWanStatusType,
       "acSysMultiWanStatusStatus": acSysMultiWanStatusStatus,
       "acSysNAT": acSysNAT,
       "acSysNATType": acSysNATType,
       "acSysWebStat": acSysWebStat,
       "acSysWebStatPasswordControlViaSNMP": acSysWebStatPasswordControlViaSNMP,
       "acSysIPStatus": acSysIPStatus,
       "acSysInterfaceStatusTable": acSysInterfaceStatusTable,
       "acSysInterfaceStatusEntry": acSysInterfaceStatusEntry,
       "acSysInterfaceStatusEntryIndex": acSysInterfaceStatusEntryIndex,
       "acSysInterfaceStatusTypeIndex": acSysInterfaceStatusTypeIndex,
       "acSysInterfaceStatusApplicationTypes": acSysInterfaceStatusApplicationTypes,
       "acSysInterfaceStatusMode": acSysInterfaceStatusMode,
       "acSysInterfaceStatusIPAddress": acSysInterfaceStatusIPAddress,
       "acSysInterfaceStatusPrefixLength": acSysInterfaceStatusPrefixLength,
       "acSysInterfaceStatusGateway": acSysInterfaceStatusGateway,
       "acSysInterfaceStatusVlanID": acSysInterfaceStatusVlanID,
       "acSysInterfaceStatusName": acSysInterfaceStatusName,
       "acSysInterfaceStatusRelatedIndex": acSysInterfaceStatusRelatedIndex,
       "acSysInterfaceStatusPrimaryDNSServerIPAddress": acSysInterfaceStatusPrimaryDNSServerIPAddress,
       "acSysInterfaceStatusSecondaryDNSServerIPAddress": acSysInterfaceStatusSecondaryDNSServerIPAddress,
       "acSysInterfaceStatusUnderlyingDevice": acSysInterfaceStatusUnderlyingDevice,
       "acSysDataInterfaceStatusTable": acSysDataInterfaceStatusTable,
       "acSysDataInterfaceStatusEntry": acSysDataInterfaceStatusEntry,
       "acSysDataInterfaceStatusIndex": acSysDataInterfaceStatusIndex,
       "acSysDataInterfaceStatusName": acSysDataInterfaceStatusName,
       "acSysDataInterfaceStatusIPAddress": acSysDataInterfaceStatusIPAddress,
       "acSysDataInterfaceStatusNetmask": acSysDataInterfaceStatusNetmask,
       "acSysDataInterfaceStatusInfo": acSysDataInterfaceStatusInfo,
       "acSysDataInterfaceStatusDescription": acSysDataInterfaceStatusDescription,
       "acSysDataInterfaceStatusOperationalState": acSysDataInterfaceStatusOperationalState,
       "acSysDataInterfaceStatusStateTime": acSysDataInterfaceStatusStateTime,
       "acSysDataInterfaceStatusUptime": acSysDataInterfaceStatusUptime,
       "acSysDataInterfaceStatusMtuMode": acSysDataInterfaceStatusMtuMode,
       "acSysDataInterfaceStatusDnsStatus": acSysDataInterfaceStatusDnsStatus,
       "acSysDataInterfaceStatusRxPackets": acSysDataInterfaceStatusRxPackets,
       "acSysDataInterfaceStatusRxBytes": acSysDataInterfaceStatusRxBytes,
       "acSysDataInterfaceStatusRxDropped": acSysDataInterfaceStatusRxDropped,
       "acSysDataInterfaceStatusRxErrors": acSysDataInterfaceStatusRxErrors,
       "acSysDataInterfaceStatusTxPackets": acSysDataInterfaceStatusTxPackets,
       "acSysDataInterfaceStatusTxBytes": acSysDataInterfaceStatusTxBytes,
       "acSysDataInterfaceStatusTxDropped": acSysDataInterfaceStatusTxDropped,
       "acSysDataInterfaceStatusTxErrors": acSysDataInterfaceStatusTxErrors,
       "acSysDataInterfaceStatusMinutes": acSysDataInterfaceStatusMinutes,
       "acSysDataInterfaceStatusMinuteInputRate": acSysDataInterfaceStatusMinuteInputRate,
       "acSysDataInterfaceStatusMinuteOutputRate": acSysDataInterfaceStatusMinuteOutputRate,
       "acSysDataInterfaceStatusSeconds": acSysDataInterfaceStatusSeconds,
       "acSysDataInterfaceStatusSecondInputRate": acSysDataInterfaceStatusSecondInputRate,
       "acSysDataInterfaceStatusSecondOutputRate": acSysDataInterfaceStatusSecondOutputRate,
       "acSysDeviceStatus": acSysDeviceStatus,
       "acSysEthernetDeviceStatusTable": acSysEthernetDeviceStatusTable,
       "acSysEthernetDeviceStatusEntry": acSysEthernetDeviceStatusEntry,
       "acSysEthernetDeviceStatusIndex": acSysEthernetDeviceStatusIndex,
       "acSysEthernetDeviceStatusVlanID": acSysEthernetDeviceStatusVlanID,
       "acSysEthernetDeviceStatusUnderlyingInterface": acSysEthernetDeviceStatusUnderlyingInterface,
       "acSysEthernetDeviceStatusDeviceName": acSysEthernetDeviceStatusDeviceName,
       "acSysNetworkWiFiStats": acSysNetworkWiFiStats,
       "acSysNetworkWiFiStatsLinuxWatchdogTimeouts": acSysNetworkWiFiStatsLinuxWatchdogTimeouts,
       "acSysNetworkWiFiStatsSWWatchdogTimeouts": acSysNetworkWiFiStatsSWWatchdogTimeouts,
       "acSysNetworkWiFiStatsHWFatalInterrupts": acSysNetworkWiFiStatsHWFatalInterrupts,
       "acSysNetworkWiFiStatsBeaconMissInterrupts": acSysNetworkWiFiStatsBeaconMissInterrupts,
       "acSysNetworkWiFiStatsRcvOverrunInterrupts": acSysNetworkWiFiStatsRcvOverrunInterrupts,
       "acSysNetworkWiFiStatsRcvEolInterrupts": acSysNetworkWiFiStatsRcvEolInterrupts,
       "acSysNetworkWiFiStatsTxUnderrunInterrupts": acSysNetworkWiFiStatsTxUnderrunInterrupts,
       "acSysNetworkWiFiStatsGlobalTxTimeoutInterrupts": acSysNetworkWiFiStatsGlobalTxTimeoutInterrupts,
       "acSysNetworkWiFiStatsCarrierSenseTimeoutInterrupts": acSysNetworkWiFiStatsCarrierSenseTimeoutInterrupts,
       "acSysNetworkWiFiStatsTxFramesTailDropped": acSysNetworkWiFiStatsTxFramesTailDropped,
       "acSysNetworkWiFiStatsTxFramesTailDroppedDueDeadLink": acSysNetworkWiFiStatsTxFramesTailDroppedDueDeadLink,
       "acSysNetworkWiFiStatsTxDropsWrongState": acSysNetworkWiFiStatsTxDropsWrongState,
       "acSysNetworkWiFiStatsTxFramesDiscardedDeviceGone": acSysNetworkWiFiStatsTxFramesDiscardedDeviceGone,
       "acSysNetworkWiFiStatsTxQueueStoppedNoTxBuffers": acSysNetworkWiFiStatsTxQueueStoppedNoTxBuffers,
       "acSysNetworkWiFiStatsDataTxFailedNoTxBuffer": acSysNetworkWiFiStatsDataTxFailedNoTxBuffer,
       "acSysNetworkWiFiStatsMgtTxFailedNoTxBuffer": acSysNetworkWiFiStatsMgtTxFailedNoTxBuffer,
       "acSysNetworkWiFiStatsBKTxFailedNoTxBuffer": acSysNetworkWiFiStatsBKTxFailedNoTxBuffer,
       "acSysNetworkWiFiStatsBETxFailedNoTxBuffer": acSysNetworkWiFiStatsBETxFailedNoTxBuffer,
       "acSysNetworkWiFiStatsVITxFailedNoTxBuffer": acSysNetworkWiFiStatsVITxFailedNoTxBuffer,
       "acSysNetworkWiFiStatsVOTxFailedNoTxBuffer": acSysNetworkWiFiStatsVOTxFailedNoTxBuffer,
       "acSysNetworkWiFiStatsTxFailedNoDescriptors": acSysNetworkWiFiStatsTxFailedNoDescriptors,
       "acSysNetworkWiFiStatsTxFailedNoDescriptorsLegacyPackets": acSysNetworkWiFiStatsTxFailedNoDescriptorsLegacyPackets,
       "acSysNetworkWiFiStatsTxFailedNoDescriptorsAggr": acSysNetworkWiFiStatsTxFailedNoDescriptorsAggr,
       "acSysNetworkWiFiStatsTxFailedBadSetupLegacyPackets": acSysNetworkWiFiStatsTxFailedBadSetupLegacyPackets,
       "acSysNetworkWiFiStatsTxFailedBadSetupAggr": acSysNetworkWiFiStatsTxFailedBadSetupAggr,
       "acSysNetworkWiFiStatsTxFailedNoSKBSLegacyEncaps": acSysNetworkWiFiStatsTxFailedNoSKBSLegacyEncaps,
       "acSysNetworkWiFiStatsTxFailedNoSKBSAggrEncaps": acSysNetworkWiFiStatsTxFailedNoSKBSAggrEncaps,
       "acSysNetworkWiFiStatsTxFailedNoNode": acSysNetworkWiFiStatsTxFailedNoNode,
       "acSysNetworkWiFiStatsTxFailedFIFOUnderrunAggr": acSysNetworkWiFiStatsTxFailedFIFOUnderrunAggr,
       "acSysNetworkWiFiStatsTxFailedFIFOUnderrunLegacyPackets": acSysNetworkWiFiStatsTxFailedFIFOUnderrunLegacyPackets,
       "acSysNetworkWiFiStatsTxFailedXmitFiter": acSysNetworkWiFiStatsTxFailedXmitFiter,
       "acSysNetworkWiFiStatsTxFailedTimerExp": acSysNetworkWiFiStatsTxFailedTimerExp,
       "acSysNetworkWiFiStatsTxFailedTxopExceededAggr": acSysNetworkWiFiStatsTxFailedTxopExceededAggr,
       "acSysNetworkWiFiStatsTxFailedDescriptorCfgErrAggr": acSysNetworkWiFiStatsTxFailedDescriptorCfgErrAggr,
       "acSysNetworkWiFiStatsTxFailedDataUnderrunAggr": acSysNetworkWiFiStatsTxFailedDataUnderrunAggr,
       "acSysNetworkWiFiStatsTxFailedDelimiterUnderrunAggr": acSysNetworkWiFiStatsTxFailedDelimiterUnderrunAggr,
       "acSysNetworkWiFiStatsTxFailedInvalidBAState": acSysNetworkWiFiStatsTxFailedInvalidBAState,
       "acSysNetworkWiFiStatsRxFailedFIFOOverrun": acSysNetworkWiFiStatsRxFailedFIFOOverrun,
       "acSysNetworkWiFiStatsRxDiscardedFrameTooBig": acSysNetworkWiFiStatsRxDiscardedFrameTooBig,
       "acSysNetworkWiFiStatsRxFailedNoBuff": acSysNetworkWiFiStatsRxFailedNoBuff,
       "acSysNetworkWiFiStatsRxFailedDecryption": acSysNetworkWiFiStatsRxFailedDecryption,
       "acSysNetworkWiFiStatsRxFailedMICFailure": acSysNetworkWiFiStatsRxFailedMICFailure,
       "acSysNetworkWiFiStatsRxFailedDecryptBusyError": acSysNetworkWiFiStatsRxFailedDecryptBusyError,
       "acSysNetworkWiFiStatsRxFailedPktsBadVer": acSysNetworkWiFiStatsRxFailedPktsBadVer,
       "acSysNetworkWiFiStatsNoBuffForBeacon": acSysNetworkWiFiStatsNoBuffForBeacon,
       "acSysNetworkWiFiStatsBeaconStuck": acSysNetworkWiFiStatsBeaconStuck,
       "acSysNetworkWiFiStatsPeriodicCalibrationFail": acSysNetworkWiFiStatsPeriodicCalibrationFail,
       "acSysNetworkWiFiStatsFastChannelChangeFail": acSysNetworkWiFiStatsFastChannelChangeFail,
       "acSysNetworkCell": acSysNetworkCell,
       "acSysNetworkCellCurrentNetworkTypeDescription": acSysNetworkCellCurrentNetworkTypeDescription,
       "acSysNetworkCellSignalStrength": acSysNetworkCellSignalStrength,
       "acSysNetworkCellInterfaceWorkingMode": acSysNetworkCellInterfaceWorkingMode,
       "acSysNetworkCellWanIPAddress": acSysNetworkCellWanIPAddress,
       "acSysTime": acSysTime,
       "acSysTimeUp": acSysTimeUp,
       "acSysTimeLastConfig": acSysTimeLastConfig,
       "acSysTimeAlarmLastChange": acSysTimeAlarmLastChange,
       "acSysTimeSystemAvailabilityStartTime": acSysTimeSystemAvailabilityStartTime,
       "acSysTimeSystemAvailability": acSysTimeSystemAvailability,
       "acSysVoicePrompt": acSysVoicePrompt,
       "acSysVoicePromptTotalMemorySize": acSysVoicePromptTotalMemorySize,
       "acSysVoicePromptMaxFreeMemorySize": acSysVoicePromptMaxFreeMemorySize,
       "acSysRepositoryAMS": acSysRepositoryAMS,
       "acSysRepositoryAMSIsReadyForUpdate": acSysRepositoryAMSIsReadyForUpdate,
       "acSysHAStatus": acSysHAStatus,
       "acSysHAStatusReady": acSysHAStatusReady,
       "acSysHAStatusNetworkWatchdogStatus": acSysHAStatusNetworkWatchdogStatus,
       "acSysLDAPStatus": acSysLDAPStatus,
       "acSysLDAPStatusServerMode": acSysLDAPStatusServerMode,
       "acSysNqmStatus": acSysNqmStatus,
       "acSysNqmHistoryTable": acSysNqmHistoryTable,
       "acSysNqmHistoryEntry": acSysNqmHistoryEntry,
       "acSysNqmHistorySenderIndex": acSysNqmHistorySenderIndex,
       "acSysNqmHistoryIndex": acSysNqmHistoryIndex,
       "acSysNqmHistoryProbeTime": acSysNqmHistoryProbeTime,
       "acSysNqmHistoryIsValid": acSysNqmHistoryIsValid,
       "acSysNqmHistoryRoundTripTime": acSysNqmHistoryRoundTripTime,
       "acSysNqmHistoryPacketLossTx": acSysNqmHistoryPacketLossTx,
       "acSysNqmHistoryPacketLossRx": acSysNqmHistoryPacketLossRx,
       "acSysNqmHistoryTotalPacketLoss": acSysNqmHistoryTotalPacketLoss,
       "acSysNqmHistoryJitterTx": acSysNqmHistoryJitterTx,
       "acSysNqmHistoryJitterRx": acSysNqmHistoryJitterRx,
       "acSysNqmHistoryTotalJitter": acSysNqmHistoryTotalJitter,
       "acSysNqmHistoryCqMos": acSysNqmHistoryCqMos,
       "acSysNqmHistoryLqMos": acSysNqmHistoryLqMos,
       "acSysDataStatus": acSysDataStatus,
       "acSysDataStatusFirewallTCPConnections": acSysDataStatusFirewallTCPConnections,
       "acSysDataStatusFirewallUDPConnections": acSysDataStatusFirewallUDPConnections,
       "acSysDataStatusFirewallICMPConnections": acSysDataStatusFirewallICMPConnections,
       "acSysDataStatusFirewallIGMPConnections": acSysDataStatusFirewallIGMPConnections,
       "acSysInventory": acSysInventory,
       "acSysInventoryChassis": acSysInventoryChassis,
       "acSysInventoryCPU": acSysInventoryCPU,
       "acSysInventoryMemory": acSysInventoryMemory,
       "acSysInventoryNetworkCards": acSysInventoryNetworkCards,
       "acSysInventoryVirtualEnvironment": acSysInventoryVirtualEnvironment,
       "acSystemAction": acSystemAction,
       "acSysAction": acSysAction,
       "acSysActionSet": acSysActionSet,
       "acSysActionSetReset": acSysActionSetReset,
       "acSysActionSetResetControl": acSysActionSetResetControl,
       "acSysActionSetDefaults": acSysActionSetDefaults,
       "acSysActionSetSaveConfig": acSysActionSetSaveConfig,
       "acSysActionSetAutoUpdate": acSysActionSetAutoUpdate,
       "acSysActionSetGetTimeFromNTPServer": acSysActionSetGetTimeFromNTPServer,
       "acSysActionSetSwUpgrade": acSysActionSetSwUpgrade,
       "acSysActionSetOnLineChangesApply": acSysActionSetOnLineChangesApply,
       "acSysActionSetIPSecTLSUpgrade": acSysActionSetIPSecTLSUpgrade,
       "acSysActionSetGWAppTLSUpgrade": acSysActionSetGWAppTLSUpgrade,
       "acSysActionSetConvertNetworkIFsConfiguration": acSysActionSetConvertNetworkIFsConfiguration,
       "acSysActionSetActionId": acSysActionSetActionId,
       "acSysActionSetAutoUpdateActionResult": acSysActionSetAutoUpdateActionResult,
       "acSysActionSetApplyINImethod": acSysActionSetApplyINImethod,
       "acSysActionSetLicensePoolUpdate": acSysActionSetLicensePoolUpdate,
       "acSysActionSetAupdNetworkSource": acSysActionSetAupdNetworkSource,
       "acSysActionSetLicensePoolHitless": acSysActionSetLicensePoolHitless,
       "acSysActionSetLicensePoolRefreshRequest": acSysActionSetLicensePoolRefreshRequest,
       "acSysActionAdmin": acSysActionAdmin,
       "acSysActionAdminState": acSysActionAdminState,
       "acSysActionAdminStateLockTimeout": acSysActionAdminStateLockTimeout,
       "acSysUpload": acSysUpload,
       "acSysUploadActionType": acSysUploadActionType,
       "acSysUploadFileType": acSysUploadFileType,
       "acSysUploadFileNumber": acSysUploadFileNumber,
       "acSysUploadFileURI": acSysUploadFileURI,
       "acSysUploadActionID": acSysUploadActionID,
       "acSysUploadActionResult": acSysUploadActionResult,
       "acSysMcUpgrade": acSysMcUpgrade,
       "acSysMcUpgradeActionType": acSysMcUpgradeActionType,
       "acSysMcUpgradeMcType": acSysMcUpgradeMcType,
       "acSysMcUpgradeGracefulTimeout": acSysMcUpgradeGracefulTimeout,
       "acSysMcUpgradeActionID": acSysMcUpgradeActionID,
       "acSysMcUpgradeActionResult": acSysMcUpgradeActionResult,
       "acSysConfigurationPackageChecksum": acSysConfigurationPackageChecksum,
       "acSysConfigurationPackageChecksumActionType": acSysConfigurationPackageChecksumActionType,
       "acSysConfigurationPackageChecksumActionID": acSysConfigurationPackageChecksumActionID,
       "acSysConfigurationPackageChecksumActionResult": acSysConfigurationPackageChecksumActionResult,
       "acSysConfigurationPackageChecksumValue": acSysConfigurationPackageChecksumValue,
       "acSystemChassis": acSystemChassis,
       "acSystemChassisDryContactsOutStatus": acSystemChassisDryContactsOutStatus,
       "acSystemChassisDryContactsInStatus": acSystemChassisDryContactsInStatus,
       "acSystemChassisLastChanged": acSystemChassisLastChanged,
       "acSysModuleTable": acSysModuleTable,
       "acSysModuleEntry": acSysModuleEntry,
       "acSysModuleIndex": acSysModuleIndex,
       "acSysModuleGeographicalPosition": acSysModuleGeographicalPosition,
       "acSysModuleType": acSysModuleType,
       "acSysModulePresence": acSysModulePresence,
       "acSysModuleLicenseKeyList": acSysModuleLicenseKeyList,
       "acSysModuleSerialNumber": acSysModuleSerialNumber,
       "acSysModuleSWVersion": acSysModuleSWVersion,
       "acSysModuleOperationalState": acSysModuleOperationalState,
       "acSysModuleHAStatus": acSysModuleHAStatus,
       "acSysModuleLEDs": acSysModuleLEDs,
       "acSysModuleTemperature": acSysModuleTemperature,
       "acSysModuleActions": acSysModuleActions,
       "acSysModuleFRUaction": acSysModuleFRUaction,
       "acSysModuleFRUstatus": acSysModuleFRUstatus,
       "acSysModuleNumOfPorts": acSysModuleNumOfPorts,
       "acSysModuleFirstPortNum": acSysModuleFirstPortNum,
       "acSysModuleSerialNumberString": acSysModuleSerialNumberString,
       "acSysFanTrayTable": acSysFanTrayTable,
       "acSysFanTrayEntry": acSysFanTrayEntry,
       "acSysFanTrayIndex": acSysFanTrayIndex,
       "acSysFanTrayGeographicalPosition": acSysFanTrayGeographicalPosition,
       "acSysFanTrayExistence": acSysFanTrayExistence,
       "acSysFanTrayType": acSysFanTrayType,
       "acSysFanTrayLEDs": acSysFanTrayLEDs,
       "acSysFanTraySeverity": acSysFanTraySeverity,
       "acSysFanTrayFansConfiguredSpeed": acSysFanTrayFansConfiguredSpeed,
       "acSysFanTrayFansCurrentSpeed": acSysFanTrayFansCurrentSpeed,
       "acSysFanTrayFansStatus": acSysFanTrayFansStatus,
       "acSysPowerSupplyTable": acSysPowerSupplyTable,
       "acSysPowerSupplyEntry": acSysPowerSupplyEntry,
       "acSysPowerSupplyIndex": acSysPowerSupplyIndex,
       "acSysPowerSupplyGeographicalPosition": acSysPowerSupplyGeographicalPosition,
       "acSysPowerSupplyExistence": acSysPowerSupplyExistence,
       "acSysPowerSupplyHwversion": acSysPowerSupplyHwversion,
       "acSysPowerSupplyLEDs": acSysPowerSupplyLEDs,
       "acSysPowerSupplySeverity": acSysPowerSupplySeverity,
       "acSysPEMTable": acSysPEMTable,
       "acSysPEMEntry": acSysPEMEntry,
       "acSysPEMIndex": acSysPEMIndex,
       "acSysPEMGeographicalPosition": acSysPEMGeographicalPosition,
       "acSysPEMExistence": acSysPEMExistence,
       "acSysPEMType": acSysPEMType,
       "acSysPEMElectricWireConnection": acSysPEMElectricWireConnection,
       "acSysSATModule": acSysSATModule,
       "acSysSATTable": acSysSATTable,
       "acSysSATEntry": acSysSATEntry,
       "acSysSATSatIndex": acSysSATSatIndex,
       "acSysSATGeographicalPosition": acSysSATGeographicalPosition,
       "acSysSATType": acSysSATType,
       "acSysSATInitInformation": acSysSATInitInformation,
       "acSysSATTimingUnitExistence": acSysSATTimingUnitExistence,
       "acSysSATTimingRefSelection": acSysSATTimingRefSelection,
       "acSysSATFramersTable": acSysSATFramersTable,
       "acSysSATFramersEntry": acSysSATFramersEntry,
       "acSysSATFramersSatIndex": acSysSATFramersSatIndex,
       "acSysSATFramersFramerIndex": acSysSATFramersFramerIndex,
       "acSysSATFramersFramerInterfaceStatus": acSysSATFramersFramerInterfaceStatus,
       "acSysSATFramersFramerLoopBackRef": acSysSATFramersFramerLoopBackRef,
       "acSysSATFramersFramerInterfaceType": acSysSATFramersFramerInterfaceType,
       "acSysSATFramersFramerTransmitControl": acSysSATFramersFramerTransmitControl,
       "acSysSATFramersRxStatus": acSysSATFramersRxStatus,
       "acSysSATFramersIsUsedAsPLLClock": acSysSATFramersIsUsedAsPLLClock,
       "acSysTimingModule": acSysTimingModule,
       "acSysPLLStatusTable": acSysPLLStatusTable,
       "acSysPLLStatusEntry": acSysPLLStatusEntry,
       "acSysPLLStatusIndex": acSysPLLStatusIndex,
       "acSysPLLStatusOperatingMode": acSysPLLStatusOperatingMode,
       "acSystemChassisHA": acSystemChassisHA,
       "acSystemChassisHADevice1Name": acSystemChassisHADevice1Name,
       "acSystemChassisHADevice2Name": acSystemChassisHADevice2Name,
       "acSystemChassisHAActiveDevice": acSystemChassisHAActiveDevice,
       "acSysRedundantModuleTable": acSysRedundantModuleTable,
       "acSysRedundantModuleEntry": acSysRedundantModuleEntry,
       "acSysRedundantModuleIndex": acSysRedundantModuleIndex,
       "acSysRedundantModuleGeographicalPosition": acSysRedundantModuleGeographicalPosition,
       "acSysRedundantModuleType": acSysRedundantModuleType,
       "acSysRedundantModulePresence": acSysRedundantModulePresence,
       "acSysRedundantModuleLicenseKeyList": acSysRedundantModuleLicenseKeyList,
       "acSysRedundantModuleSerialNumber": acSysRedundantModuleSerialNumber,
       "acSysRedundantModuleSWVersion": acSysRedundantModuleSWVersion,
       "acSysRedundantModuleOperationalState": acSysRedundantModuleOperationalState,
       "acSysRedundantModuleHAStatus": acSysRedundantModuleHAStatus,
       "acSysRedundantModuleLEDs": acSysRedundantModuleLEDs,
       "acSysRedundantModuleTemperature": acSysRedundantModuleTemperature,
       "acSysRedundantModuleActions": acSysRedundantModuleActions,
       "acSysRedundantModuleFRUaction": acSysRedundantModuleFRUaction,
       "acSysRedundantModuleFRUstatus": acSysRedundantModuleFRUstatus,
       "acSysRedundantModuleNumOfPorts": acSysRedundantModuleNumOfPorts,
       "acSysRedundantModuleFirstPortNum": acSysRedundantModuleFirstPortNum,
       "acSysRedundantModuleSerialNumberString": acSysRedundantModuleSerialNumberString,
       "acSysRedundantFanTrayTable": acSysRedundantFanTrayTable,
       "acSysRedundantFanTrayEntry": acSysRedundantFanTrayEntry,
       "acSysRedundantFanTrayIndex": acSysRedundantFanTrayIndex,
       "acSysRedundantFanTrayGeographicalPosition": acSysRedundantFanTrayGeographicalPosition,
       "acSysRedundantFanTrayExistence": acSysRedundantFanTrayExistence,
       "acSysRedundantFanTrayType": acSysRedundantFanTrayType,
       "acSysRedundantFanTrayLEDs": acSysRedundantFanTrayLEDs,
       "acSysRedundantFanTraySeverity": acSysRedundantFanTraySeverity,
       "acSysRedundantFanTrayFansConfiguredSpeed": acSysRedundantFanTrayFansConfiguredSpeed,
       "acSysRedundantFanTrayFansCurrentSpeed": acSysRedundantFanTrayFansCurrentSpeed,
       "acSysRedundantFanTrayFansStatus": acSysRedundantFanTrayFansStatus,
       "acSysRedundantPowerSupplyTable": acSysRedundantPowerSupplyTable,
       "acSysRedundantPowerSupplyEntry": acSysRedundantPowerSupplyEntry,
       "acSysRedundantPowerSupplyIndex": acSysRedundantPowerSupplyIndex,
       "acSysRedundantPowerSupplyGeographicalPosition": acSysRedundantPowerSupplyGeographicalPosition,
       "acSysRedundantPowerSupplyExistence": acSysRedundantPowerSupplyExistence,
       "acSysRedundantPowerSupplyHwversion": acSysRedundantPowerSupplyHwversion,
       "acSysRedundantPowerSupplyLEDs": acSysRedundantPowerSupplyLEDs,
       "acSysRedundantPowerSupplySeverity": acSysRedundantPowerSupplySeverity}
)
