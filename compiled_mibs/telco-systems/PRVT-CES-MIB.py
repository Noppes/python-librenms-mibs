# SNMP MIB module (PRVT-CES-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\telco-systems\binos\PRVT-CES-MIB

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

(dsx1ConfigEntry,) = mibBuilder.importSymbols(
    "DS1-MIB",
    "dsx1ConfigEntry")

(switch,) = mibBuilder.importSymbols(
    "PRVT-SWITCH-MIB",
    "switch")

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
 TimeStamp) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention",
    "TimeStamp")


# MODULE-IDENTITY

prvtCESMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 111)
)
if mibBuilder.loadTexts:
    prvtCESMib.setRevisions(
        ("2009-05-18 00:00",
         "2009-05-14 00:00",
         "2009-05-05 00:00",
         "2009-03-19 00:00",
         "2009-02-25 00:00",
         "2009-02-16 00:00",
         "2008-06-19 00:00",
         "2006-03-07 00:00",
         "2006-02-23 00:00",
         "2005-03-11 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class ConfigAction(TextualConvention, Integer32):
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
        *(("noop", 1),
          ("applyConfiguration", 2),
          ("rejectConfiguration", 3),
          ("restart", 4))
    )



class E1Impedance(TextualConvention, Integer32):
    status = "current"
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
          ("e1-75ohm", 1),
          ("e1-75hrl", 2),
          ("e1-120ohm", 3),
          ("e1-120hrl", 4))
    )



class T1LongCableLength(TextualConvention, Integer32):
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
        *(("notApplicable", 1),
          ("neg75dB", 2),
          ("neg15dB", 3),
          ("neg225dB", 4),
          ("zerodB", 5))
    )



class T1GainLimit(TextualConvention, Integer32):
    status = "current"
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
          ("none", 1),
          ("gain30", 2),
          ("gain36", 3))
    )



class CESLineType(TextualConvention, Integer32):
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
        *(("e1", 1),
          ("t1", 2),
          ("e1-sdh", 3),
          ("t1-sdh", 4),
          ("t1-sonet", 5))
    )



class ServiceClock(TextualConvention, Integer32):
    status = "current"
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
        *(("notAplicable", 0),
          ("loopTiming", 1),
          ("localTiming", 2),
          ("adaptive", 3),
          ("differntial", 4))
    )



# MIB Managed Objects in the order of their OIDs

_PrvtCESNotifications_ObjectIdentity = ObjectIdentity
prvtCESNotifications = _PrvtCESNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 111, 0)
)
_PrvtCESObjects_ObjectIdentity = ObjectIdentity
prvtCESObjects = _PrvtCESObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 111, 1)
)
_PrvtCESDsx1ExtTable_Object = MibTable
prvtCESDsx1ExtTable = _PrvtCESDsx1ExtTable_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 111, 1, 1)
)
if mibBuilder.loadTexts:
    prvtCESDsx1ExtTable.setStatus("current")
_PrvtCESDsx1ExtEntry_Object = MibTableRow
prvtCESDsx1ExtEntry = _PrvtCESDsx1ExtEntry_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 111, 1, 1, 1)
)
if mibBuilder.loadTexts:
    prvtCESDsx1ExtEntry.setStatus("current")
_PrvtCESE1Impedance_Type = E1Impedance
_PrvtCESE1Impedance_Object = MibTableColumn
prvtCESE1Impedance = _PrvtCESE1Impedance_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 111, 1, 1, 1, 1),
    _PrvtCESE1Impedance_Type()
)
prvtCESE1Impedance.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prvtCESE1Impedance.setStatus("current")
_PrvtCEST1GainLimit_Type = T1GainLimit
_PrvtCEST1GainLimit_Object = MibTableColumn
prvtCEST1GainLimit = _PrvtCEST1GainLimit_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 111, 1, 1, 1, 2),
    _PrvtCEST1GainLimit_Type()
)
prvtCEST1GainLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prvtCEST1GainLimit.setStatus("current")


class _PrvtCESPortShutdown_Type(Integer32):
    """Custom type prvtCESPortShutdown based on Integer32"""
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


_PrvtCESPortShutdown_Type.__name__ = "Integer32"
_PrvtCESPortShutdown_Object = MibTableColumn
prvtCESPortShutdown = _PrvtCESPortShutdown_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 111, 1, 1, 1, 3),
    _PrvtCESPortShutdown_Type()
)
prvtCESPortShutdown.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prvtCESPortShutdown.setStatus("current")


class _PrvtCESPortLineType_Type(Integer32):
    """Custom type prvtCESPortLineType based on Integer32"""
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
              16)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("dsx1ESF", 2),
          ("dsx1D4", 3),
          ("dsx1E1", 4),
          ("dsx1E1CRC", 5),
          ("dsx1E1MF", 6),
          ("dsx1E1CRCMF", 7),
          ("dsx1Unframed", 8),
          ("dsx1E1Unframed", 9),
          ("dsx1DS2M12", 10),
          ("dsx1E2", 11),
          ("dsx1E1Q50", 12),
          ("dsx1E1Q50CRC", 13),
          ("dsx1SFCAS", 14),
          ("dsx1ESFCAS", 15),
          ("notApplicable", 16))
    )


_PrvtCESPortLineType_Type.__name__ = "Integer32"
_PrvtCESPortLineType_Object = MibTableColumn
prvtCESPortLineType = _PrvtCESPortLineType_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 111, 1, 1, 1, 4),
    _PrvtCESPortLineType_Type()
)
prvtCESPortLineType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prvtCESPortLineType.setStatus("current")
_PrvtCEST1LongCableLength_Type = T1LongCableLength
_PrvtCEST1LongCableLength_Object = MibTableColumn
prvtCEST1LongCableLength = _PrvtCEST1LongCableLength_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 111, 1, 1, 1, 5),
    _PrvtCEST1LongCableLength_Type()
)
prvtCEST1LongCableLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prvtCEST1LongCableLength.setStatus("current")


class _PrvtCESPortOperStatus_Type(Integer32):
    """Custom type prvtCESPortOperStatus based on Integer32"""
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
          ("lowerlayerDown", 7))
    )


_PrvtCESPortOperStatus_Type.__name__ = "Integer32"
_PrvtCESPortOperStatus_Object = MibTableColumn
prvtCESPortOperStatus = _PrvtCESPortOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 111, 1, 1, 1, 6),
    _PrvtCESPortOperStatus_Type()
)
prvtCESPortOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtCESPortOperStatus.setStatus("current")


class _PrvtCESClearPortStatistics_Type(Integer32):
    """Custom type prvtCESClearPortStatistics based on Integer32"""
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


_PrvtCESClearPortStatistics_Type.__name__ = "Integer32"
_PrvtCESClearPortStatistics_Object = MibTableColumn
prvtCESClearPortStatistics = _PrvtCESClearPortStatistics_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 111, 1, 1, 1, 7),
    _PrvtCESClearPortStatistics_Type()
)
prvtCESClearPortStatistics.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prvtCESClearPortStatistics.setStatus("current")
_PrvtCESServiceClock_Type = ServiceClock
_PrvtCESServiceClock_Object = MibTableColumn
prvtCESServiceClock = _PrvtCESServiceClock_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 111, 1, 1, 1, 8),
    _PrvtCESServiceClock_Type()
)
prvtCESServiceClock.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prvtCESServiceClock.setStatus("current")
_PrvtCESModuleConfTable_Object = MibTable
prvtCESModuleConfTable = _PrvtCESModuleConfTable_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 111, 1, 2)
)
if mibBuilder.loadTexts:
    prvtCESModuleConfTable.setStatus("current")
_PrvtCESModuleConfEntry_Object = MibTableRow
prvtCESModuleConfEntry = _PrvtCESModuleConfEntry_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 111, 1, 2, 1)
)
prvtCESModuleConfEntry.setIndexNames(
    (0, "PRVT-CES-MIB", "prvtCESModuleIndex"),
)
if mibBuilder.loadTexts:
    prvtCESModuleConfEntry.setStatus("current")


class _PrvtCESModuleIndex_Type(Integer32):
    """Custom type prvtCESModuleIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_PrvtCESModuleIndex_Type.__name__ = "Integer32"
_PrvtCESModuleIndex_Object = MibTableColumn
prvtCESModuleIndex = _PrvtCESModuleIndex_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 111, 1, 2, 1, 1),
    _PrvtCESModuleIndex_Type()
)
prvtCESModuleIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    prvtCESModuleIndex.setStatus("current")
_PrvtCESModuleLineType_Type = CESLineType
_PrvtCESModuleLineType_Object = MibTableColumn
prvtCESModuleLineType = _PrvtCESModuleLineType_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 111, 1, 2, 1, 2),
    _PrvtCESModuleLineType_Type()
)
prvtCESModuleLineType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prvtCESModuleLineType.setStatus("current")


class _PrvtCESModuleTxClock_Type(Integer32):
    """Custom type prvtCESModuleTxClock based on Integer32"""
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
        *(("loopTiming", 1),
          ("localTiming", 2),
          ("throughTiming", 3),
          ("adaptive", 4),
          ("external-port", 5),
          ("line", 6),
          ("ptp", 7))
    )


_PrvtCESModuleTxClock_Type.__name__ = "Integer32"
_PrvtCESModuleTxClock_Object = MibTableColumn
prvtCESModuleTxClock = _PrvtCESModuleTxClock_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 111, 1, 2, 1, 3),
    _PrvtCESModuleTxClock_Type()
)
prvtCESModuleTxClock.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prvtCESModuleTxClock.setStatus("current")


class _PrvtCESModuleTxBackupClock_Type(Integer32):
    """Custom type prvtCESModuleTxBackupClock based on Integer32"""
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


_PrvtCESModuleTxBackupClock_Type.__name__ = "Integer32"
_PrvtCESModuleTxBackupClock_Object = MibTableColumn
prvtCESModuleTxBackupClock = _PrvtCESModuleTxBackupClock_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 111, 1, 2, 1, 4),
    _PrvtCESModuleTxBackupClock_Type()
)
prvtCESModuleTxBackupClock.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prvtCESModuleTxBackupClock.setStatus("current")
_PrvtCESModuleConfig_Type = ConfigAction
_PrvtCESModuleConfig_Object = MibTableColumn
prvtCESModuleConfig = _PrvtCESModuleConfig_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 111, 1, 2, 1, 5),
    _PrvtCESModuleConfig_Type()
)
prvtCESModuleConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prvtCESModuleConfig.setStatus("current")
_PrvtCESModuleIPAddress_Type = IpAddress
_PrvtCESModuleIPAddress_Object = MibTableColumn
prvtCESModuleIPAddress = _PrvtCESModuleIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 111, 1, 2, 1, 6),
    _PrvtCESModuleIPAddress_Type()
)
prvtCESModuleIPAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prvtCESModuleIPAddress.setStatus("current")
_PrvtCESModuleIPAddressMask_Type = IpAddress
_PrvtCESModuleIPAddressMask_Object = MibTableColumn
prvtCESModuleIPAddressMask = _PrvtCESModuleIPAddressMask_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 111, 1, 2, 1, 7),
    _PrvtCESModuleIPAddressMask_Type()
)
prvtCESModuleIPAddressMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prvtCESModuleIPAddressMask.setStatus("current")
_PrvtCESModuleGateway_Type = IpAddress
_PrvtCESModuleGateway_Object = MibTableColumn
prvtCESModuleGateway = _PrvtCESModuleGateway_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 111, 1, 2, 1, 8),
    _PrvtCESModuleGateway_Type()
)
prvtCESModuleGateway.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prvtCESModuleGateway.setStatus("current")
_PrvtCESModuleUpTime_Type = TimeStamp
_PrvtCESModuleUpTime_Object = MibTableColumn
prvtCESModuleUpTime = _PrvtCESModuleUpTime_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 111, 1, 2, 1, 9),
    _PrvtCESModuleUpTime_Type()
)
prvtCESModuleUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtCESModuleUpTime.setStatus("current")
_PrvtCESModuleMACAddress_Type = OctetString
_PrvtCESModuleMACAddress_Object = MibTableColumn
prvtCESModuleMACAddress = _PrvtCESModuleMACAddress_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 111, 1, 2, 1, 10),
    _PrvtCESModuleMACAddress_Type()
)
prvtCESModuleMACAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtCESModuleMACAddress.setStatus("current")
_PrvtCESModuleHardwareRevision_Type = OctetString
_PrvtCESModuleHardwareRevision_Object = MibTableColumn
prvtCESModuleHardwareRevision = _PrvtCESModuleHardwareRevision_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 111, 1, 2, 1, 11),
    _PrvtCESModuleHardwareRevision_Type()
)
prvtCESModuleHardwareRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtCESModuleHardwareRevision.setStatus("current")
_PrvtCESModuleFirmwareVersion_Type = OctetString
_PrvtCESModuleFirmwareVersion_Object = MibTableColumn
prvtCESModuleFirmwareVersion = _PrvtCESModuleFirmwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 111, 1, 2, 1, 12),
    _PrvtCESModuleFirmwareVersion_Type()
)
prvtCESModuleFirmwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtCESModuleFirmwareVersion.setStatus("current")


class _PrvtCESModuleClearCircuitStatistics_Type(Integer32):
    """Custom type prvtCESModuleClearCircuitStatistics based on Integer32"""
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


_PrvtCESModuleClearCircuitStatistics_Type.__name__ = "Integer32"
_PrvtCESModuleClearCircuitStatistics_Object = MibTableColumn
prvtCESModuleClearCircuitStatistics = _PrvtCESModuleClearCircuitStatistics_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 111, 1, 2, 1, 13),
    _PrvtCESModuleClearCircuitStatistics_Type()
)
prvtCESModuleClearCircuitStatistics.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prvtCESModuleClearCircuitStatistics.setStatus("current")


class _PrvtCESModuleLbit_Type(Integer32):
    """Custom type prvtCESModuleLbit based on Integer32"""
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


_PrvtCESModuleLbit_Type.__name__ = "Integer32"
_PrvtCESModuleLbit_Object = MibTableColumn
prvtCESModuleLbit = _PrvtCESModuleLbit_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 111, 1, 2, 1, 14),
    _PrvtCESModuleLbit_Type()
)
prvtCESModuleLbit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prvtCESModuleLbit.setStatus("current")


class _PrvtCESModulePolicyLops_Type(Integer32):
    """Custom type prvtCESModulePolicyLops based on Integer32"""
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
        *(("idle", 0),
          ("all-one", 1),
          ("channel-idle", 2),
          ("none", 3))
    )


_PrvtCESModulePolicyLops_Type.__name__ = "Integer32"
_PrvtCESModulePolicyLops_Object = MibTableColumn
prvtCESModulePolicyLops = _PrvtCESModulePolicyLops_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 111, 1, 2, 1, 15),
    _PrvtCESModulePolicyLops_Type()
)
prvtCESModulePolicyLops.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prvtCESModulePolicyLops.setStatus("current")


class _PrvtCESModulePolicyLbit_Type(Integer32):
    """Custom type prvtCESModulePolicyLbit based on Integer32"""
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
        *(("idle", 0),
          ("all-one", 1),
          ("channel-idle", 2),
          ("none", 3))
    )


_PrvtCESModulePolicyLbit_Type.__name__ = "Integer32"
_PrvtCESModulePolicyLbit_Object = MibTableColumn
prvtCESModulePolicyLbit = _PrvtCESModulePolicyLbit_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 111, 1, 2, 1, 16),
    _PrvtCESModulePolicyLbit_Type()
)
prvtCESModulePolicyLbit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prvtCESModulePolicyLbit.setStatus("current")


class _PrvtCESModulePolicyRbit_Type(Integer32):
    """Custom type prvtCESModulePolicyRbit based on Integer32"""
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
          ("rai", 1),
          ("channel-idle", 2))
    )


_PrvtCESModulePolicyRbit_Type.__name__ = "Integer32"
_PrvtCESModulePolicyRbit_Object = MibTableColumn
prvtCESModulePolicyRbit = _PrvtCESModulePolicyRbit_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 111, 1, 2, 1, 17),
    _PrvtCESModulePolicyRbit_Type()
)
prvtCESModulePolicyRbit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prvtCESModulePolicyRbit.setStatus("current")


class _PrvtCESModulePolicyRd_Type(Integer32):
    """Custom type prvtCESModulePolicyRd based on Integer32"""
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
          ("rai", 1),
          ("channel-idle", 2))
    )


_PrvtCESModulePolicyRd_Type.__name__ = "Integer32"
_PrvtCESModulePolicyRd_Object = MibTableColumn
prvtCESModulePolicyRd = _PrvtCESModulePolicyRd_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 111, 1, 2, 1, 18),
    _PrvtCESModulePolicyRd_Type()
)
prvtCESModulePolicyRd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prvtCESModulePolicyRd.setStatus("current")


class _PrvtCESModulePolicyIdlePattern_Type(Unsigned32):
    """Custom type prvtCESModulePolicyIdlePattern based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_PrvtCESModulePolicyIdlePattern_Type.__name__ = "Unsigned32"
_PrvtCESModulePolicyIdlePattern_Object = MibTableColumn
prvtCESModulePolicyIdlePattern = _PrvtCESModulePolicyIdlePattern_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 111, 1, 2, 1, 19),
    _PrvtCESModulePolicyIdlePattern_Type()
)
prvtCESModulePolicyIdlePattern.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prvtCESModulePolicyIdlePattern.setStatus("current")


class _PrvtCESModulePolicyIdleSignalling_Type(Unsigned32):
    """Custom type prvtCESModulePolicyIdleSignalling based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_PrvtCESModulePolicyIdleSignalling_Type.__name__ = "Unsigned32"
_PrvtCESModulePolicyIdleSignalling_Object = MibTableColumn
prvtCESModulePolicyIdleSignalling = _PrvtCESModulePolicyIdleSignalling_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 111, 1, 2, 1, 20),
    _PrvtCESModulePolicyIdleSignalling_Type()
)
prvtCESModulePolicyIdleSignalling.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prvtCESModulePolicyIdleSignalling.setStatus("current")


class _PrvtCESModulePolicyLopsEnter_Type(Integer32):
    """Custom type prvtCESModulePolicyLopsEnter based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1023),
    )


_PrvtCESModulePolicyLopsEnter_Type.__name__ = "Integer32"
_PrvtCESModulePolicyLopsEnter_Object = MibTableColumn
prvtCESModulePolicyLopsEnter = _PrvtCESModulePolicyLopsEnter_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 111, 1, 2, 1, 21),
    _PrvtCESModulePolicyLopsEnter_Type()
)
prvtCESModulePolicyLopsEnter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prvtCESModulePolicyLopsEnter.setStatus("current")


class _PrvtCESModulePolicyLopsExit_Type(Integer32):
    """Custom type prvtCESModulePolicyLopsExit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1023),
    )


_PrvtCESModulePolicyLopsExit_Type.__name__ = "Integer32"
_PrvtCESModulePolicyLopsExit_Object = MibTableColumn
prvtCESModulePolicyLopsExit = _PrvtCESModulePolicyLopsExit_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 111, 1, 2, 1, 22),
    _PrvtCESModulePolicyLopsExit_Type()
)
prvtCESModulePolicyLopsExit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prvtCESModulePolicyLopsExit.setStatus("current")


class _PrvtCESModulePolicyuUnstrLbit_Type(Integer32):
    """Custom type prvtCESModulePolicyuUnstrLbit based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("all-one", 1))
    )


_PrvtCESModulePolicyuUnstrLbit_Type.__name__ = "Integer32"
_PrvtCESModulePolicyuUnstrLbit_Object = MibTableColumn
prvtCESModulePolicyuUnstrLbit = _PrvtCESModulePolicyuUnstrLbit_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 111, 1, 2, 1, 23),
    _PrvtCESModulePolicyuUnstrLbit_Type()
)
prvtCESModulePolicyuUnstrLbit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prvtCESModulePolicyuUnstrLbit.setStatus("current")


class _PrvtCESModulePolicyuStrReplace_Type(Integer32):
    """Custom type prvtCESModulePolicyuStrReplace based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("all-one", 1),
          ("idle", 2))
    )


_PrvtCESModulePolicyuStrReplace_Type.__name__ = "Integer32"
_PrvtCESModulePolicyuStrReplace_Object = MibTableColumn
prvtCESModulePolicyuStrReplace = _PrvtCESModulePolicyuStrReplace_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 111, 1, 2, 1, 24),
    _PrvtCESModulePolicyuStrReplace_Type()
)
prvtCESModulePolicyuStrReplace.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prvtCESModulePolicyuStrReplace.setStatus("current")


class _PrvtCESModulePolicyuUnstrReplace_Type(Integer32):
    """Custom type prvtCESModulePolicyuUnstrReplace based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("all-one", 1),
          ("idle", 2))
    )


_PrvtCESModulePolicyuUnstrReplace_Type.__name__ = "Integer32"
_PrvtCESModulePolicyuUnstrReplace_Object = MibTableColumn
prvtCESModulePolicyuUnstrReplace = _PrvtCESModulePolicyuUnstrReplace_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 111, 1, 2, 1, 25),
    _PrvtCESModulePolicyuUnstrReplace_Type()
)
prvtCESModulePolicyuUnstrReplace.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prvtCESModulePolicyuUnstrReplace.setStatus("current")


class _PrvtCESModulePolicyuUnstrLops_Type(Integer32):
    """Custom type prvtCESModulePolicyuUnstrLops based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("all-one", 1))
    )


_PrvtCESModulePolicyuUnstrLops_Type.__name__ = "Integer32"
_PrvtCESModulePolicyuUnstrLops_Object = MibTableColumn
prvtCESModulePolicyuUnstrLops = _PrvtCESModulePolicyuUnstrLops_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 111, 1, 2, 1, 26),
    _PrvtCESModulePolicyuUnstrLops_Type()
)
prvtCESModulePolicyuUnstrLops.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prvtCESModulePolicyuUnstrLops.setStatus("current")
_PrvtCESModuleServiceClock_Type = ServiceClock
_PrvtCESModuleServiceClock_Object = MibTableColumn
prvtCESModuleServiceClock = _PrvtCESModuleServiceClock_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 111, 1, 2, 1, 27),
    _PrvtCESModuleServiceClock_Type()
)
prvtCESModuleServiceClock.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prvtCESModuleServiceClock.setStatus("current")


class _PrvtCESModulePolicyuUnstrReplacePattern_Type(Integer32):
    """Custom type prvtCESModulePolicyuUnstrReplacePattern based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_PrvtCESModulePolicyuUnstrReplacePattern_Type.__name__ = "Integer32"
_PrvtCESModulePolicyuUnstrReplacePattern_Object = MibTableColumn
prvtCESModulePolicyuUnstrReplacePattern = _PrvtCESModulePolicyuUnstrReplacePattern_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 111, 1, 2, 1, 28),
    _PrvtCESModulePolicyuUnstrReplacePattern_Type()
)
prvtCESModulePolicyuUnstrReplacePattern.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prvtCESModulePolicyuUnstrReplacePattern.setStatus("current")
_PrvtCESUnappTable_Object = MibTable
prvtCESUnappTable = _PrvtCESUnappTable_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 111, 1, 3)
)
if mibBuilder.loadTexts:
    prvtCESUnappTable.setStatus("current")
_PrvtCESUnappEntry_Object = MibTableRow
prvtCESUnappEntry = _PrvtCESUnappEntry_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 111, 1, 3, 1)
)
if mibBuilder.loadTexts:
    prvtCESUnappEntry.setStatus("current")


class _PrvtCESUnappLineType_Type(Integer32):
    """Custom type prvtCESUnappLineType based on Integer32"""
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
        *(("other", 1),
          ("dsx1ESF", 2),
          ("dsx1D4", 3),
          ("dsx1E1", 4),
          ("dsx1E1CRC", 5),
          ("dsx1E1MF", 6),
          ("dsx1E1CRCMF", 7),
          ("dsx1Unframed", 8),
          ("dsx1E1Unframed", 9),
          ("dsx1DS2M12", 10),
          ("dsx1E2", 11),
          ("dsx1E1Q50", 12),
          ("dsx1E1Q50CRC", 13))
    )


_PrvtCESUnappLineType_Type.__name__ = "Integer32"
_PrvtCESUnappLineType_Object = MibTableColumn
prvtCESUnappLineType = _PrvtCESUnappLineType_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 111, 1, 3, 1, 1),
    _PrvtCESUnappLineType_Type()
)
prvtCESUnappLineType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtCESUnappLineType.setStatus("current")


class _PrvtCESUnappLineCoding_Type(Integer32):
    """Custom type prvtCESUnappLineCoding based on Integer32"""
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
        *(("dsx1JBZS", 1),
          ("dsx1B8ZS", 2),
          ("dsx1HDB3", 3),
          ("dsx1ZBTSI", 4),
          ("dsx1AMI", 5),
          ("other", 6),
          ("dsx1B6ZS", 7))
    )


_PrvtCESUnappLineCoding_Type.__name__ = "Integer32"
_PrvtCESUnappLineCoding_Object = MibTableColumn
prvtCESUnappLineCoding = _PrvtCESUnappLineCoding_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 111, 1, 3, 1, 2),
    _PrvtCESUnappLineCoding_Type()
)
prvtCESUnappLineCoding.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtCESUnappLineCoding.setStatus("current")


class _PrvtCESUnappLoopbackConfig_Type(Integer32):
    """Custom type prvtCESUnappLoopbackConfig based on Integer32"""
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
        *(("dsx1NoLoop", 1),
          ("dsx1PayloadLoop", 2),
          ("dsx1LineLoop", 3),
          ("dsx1OtherLoop", 4),
          ("dsx1InwardLoop", 5),
          ("dsx1DualLoop", 6))
    )


_PrvtCESUnappLoopbackConfig_Type.__name__ = "Integer32"
_PrvtCESUnappLoopbackConfig_Object = MibTableColumn
prvtCESUnappLoopbackConfig = _PrvtCESUnappLoopbackConfig_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 111, 1, 3, 1, 3),
    _PrvtCESUnappLoopbackConfig_Type()
)
prvtCESUnappLoopbackConfig.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtCESUnappLoopbackConfig.setStatus("current")


class _PrvtCESUnappSignalMode_Type(Integer32):
    """Custom type prvtCESUnappSignalMode based on Integer32"""
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
        *(("none", 1),
          ("robbedBit", 2),
          ("bitOriented", 3),
          ("messageOriented", 4),
          ("other", 5))
    )


_PrvtCESUnappSignalMode_Type.__name__ = "Integer32"
_PrvtCESUnappSignalMode_Object = MibTableColumn
prvtCESUnappSignalMode = _PrvtCESUnappSignalMode_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 111, 1, 3, 1, 4),
    _PrvtCESUnappSignalMode_Type()
)
prvtCESUnappSignalMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtCESUnappSignalMode.setStatus("current")


class _PrvtCESUnappTransmitClockSource_Type(Integer32):
    """Custom type prvtCESUnappTransmitClockSource based on Integer32"""
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
        *(("loopTiming", 1),
          ("localTiming", 2),
          ("throughTiming", 3),
          ("adaptive", 4),
          ("external-port", 5))
    )


_PrvtCESUnappTransmitClockSource_Type.__name__ = "Integer32"
_PrvtCESUnappTransmitClockSource_Object = MibTableColumn
prvtCESUnappTransmitClockSource = _PrvtCESUnappTransmitClockSource_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 111, 1, 3, 1, 5),
    _PrvtCESUnappTransmitClockSource_Type()
)
prvtCESUnappTransmitClockSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtCESUnappTransmitClockSource.setStatus("current")


class _PrvtCESUnappTransmitClockBackup_Type(Integer32):
    """Custom type prvtCESUnappTransmitClockBackup based on Integer32"""
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


_PrvtCESUnappTransmitClockBackup_Type.__name__ = "Integer32"
_PrvtCESUnappTransmitClockBackup_Object = MibTableColumn
prvtCESUnappTransmitClockBackup = _PrvtCESUnappTransmitClockBackup_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 111, 1, 3, 1, 6),
    _PrvtCESUnappTransmitClockBackup_Type()
)
prvtCESUnappTransmitClockBackup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtCESUnappTransmitClockBackup.setStatus("current")


class _PrvtCESUnappLineLength_Type(Integer32):
    """Custom type prvtCESUnappLineLength based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 64000),
    )


_PrvtCESUnappLineLength_Type.__name__ = "Integer32"
_PrvtCESUnappLineLength_Object = MibTableColumn
prvtCESUnappLineLength = _PrvtCESUnappLineLength_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 111, 1, 3, 1, 7),
    _PrvtCESUnappLineLength_Type()
)
prvtCESUnappLineLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtCESUnappLineLength.setStatus("current")
if mibBuilder.loadTexts:
    prvtCESUnappLineLength.setUnits("meters")


class _PrvtCESUnappLineMode_Type(Integer32):
    """Custom type prvtCESUnappLineMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("csu", 1),
          ("dsu", 2))
    )


_PrvtCESUnappLineMode_Type.__name__ = "Integer32"
_PrvtCESUnappLineMode_Object = MibTableColumn
prvtCESUnappLineMode = _PrvtCESUnappLineMode_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 111, 1, 3, 1, 8),
    _PrvtCESUnappLineMode_Type()
)
prvtCESUnappLineMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtCESUnappLineMode.setStatus("current")


class _PrvtCESUnappLineBuildOut_Type(Integer32):
    """Custom type prvtCESUnappLineBuildOut based on Integer32"""
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
        *(("notApplicable", 1),
          ("neg75dB", 2),
          ("neg15dB", 3),
          ("neg225dB", 4),
          ("zerodB", 5))
    )


_PrvtCESUnappLineBuildOut_Type.__name__ = "Integer32"
_PrvtCESUnappLineBuildOut_Object = MibTableColumn
prvtCESUnappLineBuildOut = _PrvtCESUnappLineBuildOut_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 111, 1, 3, 1, 9),
    _PrvtCESUnappLineBuildOut_Type()
)
prvtCESUnappLineBuildOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtCESUnappLineBuildOut.setStatus("current")
_PrvtCESUnappE1Impedance_Type = E1Impedance
_PrvtCESUnappE1Impedance_Object = MibTableColumn
prvtCESUnappE1Impedance = _PrvtCESUnappE1Impedance_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 111, 1, 3, 1, 10),
    _PrvtCESUnappE1Impedance_Type()
)
prvtCESUnappE1Impedance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtCESUnappE1Impedance.setStatus("current")
_PrvtCESUnappT1GainLimit_Type = T1GainLimit
_PrvtCESUnappT1GainLimit_Object = MibTableColumn
prvtCESUnappT1GainLimit = _PrvtCESUnappT1GainLimit_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 111, 1, 3, 1, 11),
    _PrvtCESUnappT1GainLimit_Type()
)
prvtCESUnappT1GainLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtCESUnappT1GainLimit.setStatus("current")
_PrvtCESUnappIPAddress_Type = IpAddress
_PrvtCESUnappIPAddress_Object = MibTableColumn
prvtCESUnappIPAddress = _PrvtCESUnappIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 111, 1, 3, 1, 12),
    _PrvtCESUnappIPAddress_Type()
)
prvtCESUnappIPAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtCESUnappIPAddress.setStatus("current")
_PrvtCESUnappIPAddressMask_Type = IpAddress
_PrvtCESUnappIPAddressMask_Object = MibTableColumn
prvtCESUnappIPAddressMask = _PrvtCESUnappIPAddressMask_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 111, 1, 3, 1, 13),
    _PrvtCESUnappIPAddressMask_Type()
)
prvtCESUnappIPAddressMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtCESUnappIPAddressMask.setStatus("current")
_PrvtCESUnappGateway_Type = IpAddress
_PrvtCESUnappGateway_Object = MibTableColumn
prvtCESUnappGateway = _PrvtCESUnappGateway_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 111, 1, 3, 1, 14),
    _PrvtCESUnappGateway_Type()
)
prvtCESUnappGateway.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtCESUnappGateway.setStatus("current")
_PrvtCESDsx1AlarmTable_Object = MibTable
prvtCESDsx1AlarmTable = _PrvtCESDsx1AlarmTable_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 111, 1, 4)
)
if mibBuilder.loadTexts:
    prvtCESDsx1AlarmTable.setStatus("current")
_PrvtCESDsx1AlarmEntry_Object = MibTableRow
prvtCESDsx1AlarmEntry = _PrvtCESDsx1AlarmEntry_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 111, 1, 4, 1)
)
prvtCESDsx1AlarmEntry.setIndexNames(
    (0, "PRVT-CES-MIB", "prvtCESDsx1AlarmPort"),
    (0, "PRVT-CES-MIB", "prvtCESDsx1AlarmIndex"),
)
if mibBuilder.loadTexts:
    prvtCESDsx1AlarmEntry.setStatus("current")


class _PrvtCESDsx1AlarmPort_Type(Integer32):
    """Custom type prvtCESDsx1AlarmPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_PrvtCESDsx1AlarmPort_Type.__name__ = "Integer32"
_PrvtCESDsx1AlarmPort_Object = MibTableColumn
prvtCESDsx1AlarmPort = _PrvtCESDsx1AlarmPort_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 111, 1, 4, 1, 1),
    _PrvtCESDsx1AlarmPort_Type()
)
prvtCESDsx1AlarmPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    prvtCESDsx1AlarmPort.setStatus("current")
_PrvtCESDsx1AlarmIndex_Type = Gauge32
_PrvtCESDsx1AlarmIndex_Object = MibTableColumn
prvtCESDsx1AlarmIndex = _PrvtCESDsx1AlarmIndex_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 111, 1, 4, 1, 2),
    _PrvtCESDsx1AlarmIndex_Type()
)
prvtCESDsx1AlarmIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    prvtCESDsx1AlarmIndex.setStatus("current")
_PrvtCESDsx1AlarmVariable_Type = ObjectIdentifier
_PrvtCESDsx1AlarmVariable_Object = MibTableColumn
prvtCESDsx1AlarmVariable = _PrvtCESDsx1AlarmVariable_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 111, 1, 4, 1, 3),
    _PrvtCESDsx1AlarmVariable_Type()
)
prvtCESDsx1AlarmVariable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtCESDsx1AlarmVariable.setStatus("current")
_PrvtCESDsx1AlarmThreshold_Type = Integer32
_PrvtCESDsx1AlarmThreshold_Object = MibTableColumn
prvtCESDsx1AlarmThreshold = _PrvtCESDsx1AlarmThreshold_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 111, 1, 4, 1, 4),
    _PrvtCESDsx1AlarmThreshold_Type()
)
prvtCESDsx1AlarmThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prvtCESDsx1AlarmThreshold.setStatus("current")
_PrvtCESDsx1AlarmValue_Type = Integer32
_PrvtCESDsx1AlarmValue_Object = MibTableColumn
prvtCESDsx1AlarmValue = _PrvtCESDsx1AlarmValue_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 111, 1, 4, 1, 5),
    _PrvtCESDsx1AlarmValue_Type()
)
prvtCESDsx1AlarmValue.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    prvtCESDsx1AlarmValue.setStatus("current")


class _PrvtCESAlarmMonitor_Type(Integer32):
    """Custom type prvtCESAlarmMonitor based on Integer32"""
    defaultValue = 1

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


_PrvtCESAlarmMonitor_Type.__name__ = "Integer32"
_PrvtCESAlarmMonitor_Object = MibScalar
prvtCESAlarmMonitor = _PrvtCESAlarmMonitor_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 111, 1, 5),
    _PrvtCESAlarmMonitor_Type()
)
prvtCESAlarmMonitor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prvtCESAlarmMonitor.setStatus("current")
_PrvtCESCICTable_Object = MibTable
prvtCESCICTable = _PrvtCESCICTable_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 111, 1, 6)
)
if mibBuilder.loadTexts:
    prvtCESCICTable.setStatus("current")
_PrvtCESCICEntry_Object = MibTableRow
prvtCESCICEntry = _PrvtCESCICEntry_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 111, 1, 6, 1)
)
prvtCESCICEntry.setIndexNames(
    (0, "PRVT-CES-MIB", "prvtCESCICModuleId"),
    (0, "PRVT-CES-MIB", "prvtCESCICNumber"),
)
if mibBuilder.loadTexts:
    prvtCESCICEntry.setStatus("current")


class _PrvtCESCICModuleId_Type(Integer32):
    """Custom type prvtCESCICModuleId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_PrvtCESCICModuleId_Type.__name__ = "Integer32"
_PrvtCESCICModuleId_Object = MibTableColumn
prvtCESCICModuleId = _PrvtCESCICModuleId_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 111, 1, 6, 1, 1),
    _PrvtCESCICModuleId_Type()
)
prvtCESCICModuleId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    prvtCESCICModuleId.setStatus("current")
_PrvtCESCICNumber_Type = Gauge32
_PrvtCESCICNumber_Object = MibTableColumn
prvtCESCICNumber = _PrvtCESCICNumber_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 111, 1, 6, 1, 2),
    _PrvtCESCICNumber_Type()
)
prvtCESCICNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    prvtCESCICNumber.setStatus("current")
_PrvtCESCICClockNumber_Type = Integer32
_PrvtCESCICClockNumber_Object = MibTableColumn
prvtCESCICClockNumber = _PrvtCESCICClockNumber_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 111, 1, 6, 1, 3),
    _PrvtCESCICClockNumber_Type()
)
prvtCESCICClockNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtCESCICClockNumber.setStatus("current")


class _PrvtCESCICMode_Type(Integer32):
    """Custom type prvtCESCICMode based on Integer32"""
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
        *(("freeRun", 1),
          ("acquisition", 2),
          ("normal", 3),
          ("holdover", 4),
          ("fastAcquisiton", 5))
    )


_PrvtCESCICMode_Type.__name__ = "Integer32"
_PrvtCESCICMode_Object = MibTableColumn
prvtCESCICMode = _PrvtCESCICMode_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 111, 1, 6, 1, 4),
    _PrvtCESCICMode_Type()
)
prvtCESCICMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtCESCICMode.setStatus("current")


class _PrvtCESCICTdmPort_Type(Integer32):
    """Custom type prvtCESCICTdmPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4),
    )


_PrvtCESCICTdmPort_Type.__name__ = "Integer32"
_PrvtCESCICTdmPort_Object = MibTableColumn
prvtCESCICTdmPort = _PrvtCESCICTdmPort_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 111, 1, 6, 1, 5),
    _PrvtCESCICTdmPort_Type()
)
prvtCESCICTdmPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prvtCESCICTdmPort.setStatus("current")
_PrvtCESCICCircuit_Type = Integer32
_PrvtCESCICCircuit_Object = MibTableColumn
prvtCESCICCircuit = _PrvtCESCICCircuit_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 111, 1, 6, 1, 6),
    _PrvtCESCICCircuit_Type()
)
prvtCESCICCircuit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prvtCESCICCircuit.setStatus("current")


class _PrvtCESCICStatus_Type(Integer32):
    """Custom type prvtCESCICStatus based on Integer32"""
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
        *(("locked", 1),
          ("notlocked", 2),
          ("sourceInputLost", 3),
          ("sourceInputDegraded", 4),
          ("sourceTraceLost", 5),
          ("sourceTraceDegraded", 6),
          ("sourceFreqOffsetFailure", 7),
          ("recoveredClockDegraded", 8),
          ("localReferenceFailure", 9),
          ("remoteReferenceFailure", 10))
    )


_PrvtCESCICStatus_Type.__name__ = "Integer32"
_PrvtCESCICStatus_Object = MibTableColumn
prvtCESCICStatus = _PrvtCESCICStatus_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 111, 1, 6, 1, 7),
    _PrvtCESCICStatus_Type()
)
prvtCESCICStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtCESCICStatus.setStatus("current")


class _PrvtCESCICState_Type(Integer32):
    """Custom type prvtCESCICState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("backup", 2))
    )


_PrvtCESCICState_Type.__name__ = "Integer32"
_PrvtCESCICState_Object = MibTableColumn
prvtCESCICState = _PrvtCESCICState_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 111, 1, 6, 1, 8),
    _PrvtCESCICState_Type()
)
prvtCESCICState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtCESCICState.setStatus("current")
_PrvtCESCICMappTable_Object = MibTable
prvtCESCICMappTable = _PrvtCESCICMappTable_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 111, 1, 7)
)
if mibBuilder.loadTexts:
    prvtCESCICMappTable.setStatus("current")
_PrvtCESCICMappEntry_Object = MibTableRow
prvtCESCICMappEntry = _PrvtCESCICMappEntry_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 111, 1, 7, 1)
)
prvtCESCICMappEntry.setIndexNames(
    (0, "PRVT-CES-MIB", "prvtCESCICMappModuleId"),
    (0, "PRVT-CES-MIB", "prvtCESCICMappClockNumber"),
    (0, "PRVT-CES-MIB", "prvtCESCICMappCICNumber"),
)
if mibBuilder.loadTexts:
    prvtCESCICMappEntry.setStatus("current")


class _PrvtCESCICMappModuleId_Type(Integer32):
    """Custom type prvtCESCICMappModuleId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_PrvtCESCICMappModuleId_Type.__name__ = "Integer32"
_PrvtCESCICMappModuleId_Object = MibTableColumn
prvtCESCICMappModuleId = _PrvtCESCICMappModuleId_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 111, 1, 7, 1, 1),
    _PrvtCESCICMappModuleId_Type()
)
prvtCESCICMappModuleId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtCESCICMappModuleId.setStatus("current")
_PrvtCESCICMappClockNumber_Type = Gauge32
_PrvtCESCICMappClockNumber_Object = MibTableColumn
prvtCESCICMappClockNumber = _PrvtCESCICMappClockNumber_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 111, 1, 7, 1, 2),
    _PrvtCESCICMappClockNumber_Type()
)
prvtCESCICMappClockNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtCESCICMappClockNumber.setStatus("current")
_PrvtCESCICMappCICNumber_Type = Gauge32
_PrvtCESCICMappCICNumber_Object = MibTableColumn
prvtCESCICMappCICNumber = _PrvtCESCICMappCICNumber_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 111, 1, 7, 1, 3),
    _PrvtCESCICMappCICNumber_Type()
)
prvtCESCICMappCICNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtCESCICMappCICNumber.setStatus("current")


class _PrvtCESCICMappState_Type(Integer32):
    """Custom type prvtCESCICMappState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("backup", 2))
    )


_PrvtCESCICMappState_Type.__name__ = "Integer32"
_PrvtCESCICMappState_Object = MibTableColumn
prvtCESCICMappState = _PrvtCESCICMappState_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 111, 1, 7, 1, 4),
    _PrvtCESCICMappState_Type()
)
prvtCESCICMappState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtCESCICMappState.setStatus("current")
_PrvtCESApsTable_Object = MibTable
prvtCESApsTable = _PrvtCESApsTable_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 111, 1, 8)
)
if mibBuilder.loadTexts:
    prvtCESApsTable.setStatus("current")
_PrvtCESApsEntry_Object = MibTableRow
prvtCESApsEntry = _PrvtCESApsEntry_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 111, 1, 8, 1)
)
prvtCESApsEntry.setIndexNames(
    (0, "PRVT-CES-MIB", "prvtCESModuleId"),
)
if mibBuilder.loadTexts:
    prvtCESApsEntry.setStatus("current")
_PrvtCESApsModuleId_Type = Integer32
_PrvtCESApsModuleId_Object = MibTableColumn
prvtCESApsModuleId = _PrvtCESApsModuleId_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 111, 1, 8, 1, 1),
    _PrvtCESApsModuleId_Type()
)
prvtCESApsModuleId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    prvtCESApsModuleId.setStatus("current")


class _PrvtCESApsEnable_Type(Integer32):
    """Custom type prvtCESApsEnable based on Integer32"""
    defaultValue = 1

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


_PrvtCESApsEnable_Type.__name__ = "Integer32"
_PrvtCESApsEnable_Object = MibTableColumn
prvtCESApsEnable = _PrvtCESApsEnable_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 111, 1, 8, 1, 2),
    _PrvtCESApsEnable_Type()
)
prvtCESApsEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prvtCESApsEnable.setStatus("current")


class _PrvtCESApsActiveLine_Type(Integer32):
    """Custom type prvtCESApsActiveLine based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_PrvtCESApsActiveLine_Type.__name__ = "Integer32"
_PrvtCESApsActiveLine_Object = MibTableColumn
prvtCESApsActiveLine = _PrvtCESApsActiveLine_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 111, 1, 8, 1, 3),
    _PrvtCESApsActiveLine_Type()
)
prvtCESApsActiveLine.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prvtCESApsActiveLine.setStatus("current")


class _PrvtSdBerThreshold_Type(Integer32):
    """Custom type prvtSdBerThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 9),
    )


_PrvtSdBerThreshold_Type.__name__ = "Integer32"
_PrvtSdBerThreshold_Object = MibTableColumn
prvtSdBerThreshold = _PrvtSdBerThreshold_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 111, 1, 8, 1, 4),
    _PrvtSdBerThreshold_Type()
)
prvtSdBerThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prvtSdBerThreshold.setStatus("current")


class _PrvtSfBerThreshold_Type(Integer32):
    """Custom type prvtSfBerThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(3, 5),
    )


_PrvtSfBerThreshold_Type.__name__ = "Integer32"
_PrvtSfBerThreshold_Object = MibTableColumn
prvtSfBerThreshold = _PrvtSfBerThreshold_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 111, 1, 8, 1, 5),
    _PrvtSfBerThreshold_Type()
)
prvtSfBerThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prvtSfBerThreshold.setStatus("current")
_PrvtCESUpdateFirmwareTable_Object = MibTable
prvtCESUpdateFirmwareTable = _PrvtCESUpdateFirmwareTable_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 111, 1, 9)
)
if mibBuilder.loadTexts:
    prvtCESUpdateFirmwareTable.setStatus("current")
_PrvtCESUpdateFirmwareEntry_Object = MibTableRow
prvtCESUpdateFirmwareEntry = _PrvtCESUpdateFirmwareEntry_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 111, 1, 9, 1)
)
prvtCESUpdateFirmwareEntry.setIndexNames(
    (0, "PRVT-CES-MIB", "prvtCESModuleId"),
)
if mibBuilder.loadTexts:
    prvtCESUpdateFirmwareEntry.setStatus("current")


class _PrvtCESModuleId_Type(Integer32):
    """Custom type prvtCESModuleId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32000),
    )


_PrvtCESModuleId_Type.__name__ = "Integer32"
_PrvtCESModuleId_Object = MibTableColumn
prvtCESModuleId = _PrvtCESModuleId_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 111, 1, 9, 1, 1),
    _PrvtCESModuleId_Type()
)
prvtCESModuleId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    prvtCESModuleId.setStatus("current")
_PrvtCESFirmwareImageName_Type = OctetString
_PrvtCESFirmwareImageName_Object = MibTableColumn
prvtCESFirmwareImageName = _PrvtCESFirmwareImageName_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 111, 1, 9, 1, 2),
    _PrvtCESFirmwareImageName_Type()
)
prvtCESFirmwareImageName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prvtCESFirmwareImageName.setStatus("current")


class _PrvtCESUpdateAction_Type(Integer32):
    """Custom type prvtCESUpdateAction based on Integer32"""
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
          ("update", 2),
          ("updateThroughUART", 3))
    )


_PrvtCESUpdateAction_Type.__name__ = "Integer32"
_PrvtCESUpdateAction_Object = MibTableColumn
prvtCESUpdateAction = _PrvtCESUpdateAction_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 111, 1, 9, 1, 3),
    _PrvtCESUpdateAction_Type()
)
prvtCESUpdateAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prvtCESUpdateAction.setStatus("current")


class _PrvtCESUpdateStatus_Type(Integer32):
    """Custom type prvtCESUpdateStatus based on Integer32"""
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
        *(("updateStatusUnknown", 1),
          ("updateSuccess", 2),
          ("updateInProgress", 3),
          ("updateFailed", 4))
    )


_PrvtCESUpdateStatus_Type.__name__ = "Integer32"
_PrvtCESUpdateStatus_Object = MibTableColumn
prvtCESUpdateStatus = _PrvtCESUpdateStatus_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 111, 1, 9, 1, 4),
    _PrvtCESUpdateStatus_Type()
)
prvtCESUpdateStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtCESUpdateStatus.setStatus("current")
_PrvtCESTFTPServer_Type = IpAddress
_PrvtCESTFTPServer_Object = MibTableColumn
prvtCESTFTPServer = _PrvtCESTFTPServer_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 111, 1, 9, 1, 5),
    _PrvtCESTFTPServer_Type()
)
prvtCESTFTPServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prvtCESTFTPServer.setStatus("current")
_PrvtCESConformance_ObjectIdentity = ObjectIdentity
prvtCESConformance = _PrvtCESConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 111, 2)
)
_PrvtCESDsx1Compliances_ObjectIdentity = ObjectIdentity
prvtCESDsx1Compliances = _PrvtCESDsx1Compliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 111, 2, 1)
)
_PrvtCESDsx1Groups_ObjectIdentity = ObjectIdentity
prvtCESDsx1Groups = _PrvtCESDsx1Groups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 111, 2, 2)
)
dsx1ConfigEntry.registerAugmentions(
    ("PRVT-CES-MIB",
     "prvtCESDsx1ExtEntry")
)
prvtCESDsx1ExtEntry.setIndexNames(*dsx1ConfigEntry.getIndexNames())
dsx1ConfigEntry.registerAugmentions(
    ("PRVT-CES-MIB",
     "prvtCESUnappEntry")
)
prvtCESUnappEntry.setIndexNames(*dsx1ConfigEntry.getIndexNames())

# Managed Objects groups

prvtCESDsx1ROGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 111, 2, 2, 2)
)
prvtCESDsx1ROGroup.setObjects(
      *(("PRVT-CES-MIB", "prvtCESE1Impedance"),
        ("PRVT-CES-MIB", "prvtCEST1GainLimit"),
        ("PRVT-CES-MIB", "prvtCESModuleLineType"),
        ("PRVT-CES-MIB", "prvtCESModuleTxClock"),
        ("PRVT-CES-MIB", "prvtCESModuleConfig"),
        ("PRVT-CES-MIB", "prvtCESModuleIPAddress"),
        ("PRVT-CES-MIB", "prvtCESModuleIPAddressMask"),
        ("PRVT-CES-MIB", "prvtCESModuleGateway"),
        ("PRVT-CES-MIB", "prvtCESDsx1AlarmThreshold"))
)
if mibBuilder.loadTexts:
    prvtCESDsx1ROGroup.setStatus("current")


# Notification objects

prvtCESDsx1Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 111, 0, 1)
)
prvtCESDsx1Alarm.setObjects(
      *(("PRVT-CES-MIB", "prvtCESDsx1AlarmVariable"),
        ("PRVT-CES-MIB", "prvtCESDsx1AlarmThreshold"),
        ("PRVT-CES-MIB", "prvtCESDsx1AlarmValue"))
)
if mibBuilder.loadTexts:
    prvtCESDsx1Alarm.setStatus(
        "current"
    )

prvtCESModuleAvailable = NotificationType(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 111, 0, 2)
)
prvtCESModuleAvailable.setObjects(
    ("PRVT-CES-MIB", "prvtCESModuleIndex")
)
if mibBuilder.loadTexts:
    prvtCESModuleAvailable.setStatus(
        "current"
    )

prvtCESModuleUnAvailableDueExtract = NotificationType(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 111, 0, 3)
)
prvtCESModuleUnAvailableDueExtract.setObjects(
    ("PRVT-CES-MIB", "prvtCESModuleIndex")
)
if mibBuilder.loadTexts:
    prvtCESModuleUnAvailableDueExtract.setStatus(
        "current"
    )

prvtCESModuleUnAvailableDueReload = NotificationType(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 111, 0, 4)
)
prvtCESModuleUnAvailableDueReload.setObjects(
    ("PRVT-CES-MIB", "prvtCESModuleIndex")
)
if mibBuilder.loadTexts:
    prvtCESModuleUnAvailableDueReload.setStatus(
        "current"
    )


# Notifications groups

prvtCESDsx1NotificationsGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 111, 2, 2, 1)
)
prvtCESDsx1NotificationsGroup.setObjects(
    ("PRVT-CES-MIB", "prvtCESDsx1Alarm")
)
if mibBuilder.loadTexts:
    prvtCESDsx1NotificationsGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

prvtCESDsx1Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 111, 2, 1, 1)
)
prvtCESDsx1Compliance.setObjects(
      *(("PRVT-CES-MIB", "prvtCESDsx1NotificationsGroup"),
        ("PRVT-CES-MIB", "prvtCESDsx1ROGroup"))
)
if mibBuilder.loadTexts:
    prvtCESDsx1Compliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "PRVT-CES-MIB",
    **{"ConfigAction": ConfigAction,
       "E1Impedance": E1Impedance,
       "T1LongCableLength": T1LongCableLength,
       "T1GainLimit": T1GainLimit,
       "CESLineType": CESLineType,
       "ServiceClock": ServiceClock,
       "prvtCESMib": prvtCESMib,
       "prvtCESNotifications": prvtCESNotifications,
       "prvtCESDsx1Alarm": prvtCESDsx1Alarm,
       "prvtCESModuleAvailable": prvtCESModuleAvailable,
       "prvtCESModuleUnAvailableDueExtract": prvtCESModuleUnAvailableDueExtract,
       "prvtCESModuleUnAvailableDueReload": prvtCESModuleUnAvailableDueReload,
       "prvtCESObjects": prvtCESObjects,
       "prvtCESDsx1ExtTable": prvtCESDsx1ExtTable,
       "prvtCESDsx1ExtEntry": prvtCESDsx1ExtEntry,
       "prvtCESE1Impedance": prvtCESE1Impedance,
       "prvtCEST1GainLimit": prvtCEST1GainLimit,
       "prvtCESPortShutdown": prvtCESPortShutdown,
       "prvtCESPortLineType": prvtCESPortLineType,
       "prvtCEST1LongCableLength": prvtCEST1LongCableLength,
       "prvtCESPortOperStatus": prvtCESPortOperStatus,
       "prvtCESClearPortStatistics": prvtCESClearPortStatistics,
       "prvtCESServiceClock": prvtCESServiceClock,
       "prvtCESModuleConfTable": prvtCESModuleConfTable,
       "prvtCESModuleConfEntry": prvtCESModuleConfEntry,
       "prvtCESModuleIndex": prvtCESModuleIndex,
       "prvtCESModuleLineType": prvtCESModuleLineType,
       "prvtCESModuleTxClock": prvtCESModuleTxClock,
       "prvtCESModuleTxBackupClock": prvtCESModuleTxBackupClock,
       "prvtCESModuleConfig": prvtCESModuleConfig,
       "prvtCESModuleIPAddress": prvtCESModuleIPAddress,
       "prvtCESModuleIPAddressMask": prvtCESModuleIPAddressMask,
       "prvtCESModuleGateway": prvtCESModuleGateway,
       "prvtCESModuleUpTime": prvtCESModuleUpTime,
       "prvtCESModuleMACAddress": prvtCESModuleMACAddress,
       "prvtCESModuleHardwareRevision": prvtCESModuleHardwareRevision,
       "prvtCESModuleFirmwareVersion": prvtCESModuleFirmwareVersion,
       "prvtCESModuleClearCircuitStatistics": prvtCESModuleClearCircuitStatistics,
       "prvtCESModuleLbit": prvtCESModuleLbit,
       "prvtCESModulePolicyLops": prvtCESModulePolicyLops,
       "prvtCESModulePolicyLbit": prvtCESModulePolicyLbit,
       "prvtCESModulePolicyRbit": prvtCESModulePolicyRbit,
       "prvtCESModulePolicyRd": prvtCESModulePolicyRd,
       "prvtCESModulePolicyIdlePattern": prvtCESModulePolicyIdlePattern,
       "prvtCESModulePolicyIdleSignalling": prvtCESModulePolicyIdleSignalling,
       "prvtCESModulePolicyLopsEnter": prvtCESModulePolicyLopsEnter,
       "prvtCESModulePolicyLopsExit": prvtCESModulePolicyLopsExit,
       "prvtCESModulePolicyuUnstrLbit": prvtCESModulePolicyuUnstrLbit,
       "prvtCESModulePolicyuStrReplace": prvtCESModulePolicyuStrReplace,
       "prvtCESModulePolicyuUnstrReplace": prvtCESModulePolicyuUnstrReplace,
       "prvtCESModulePolicyuUnstrLops": prvtCESModulePolicyuUnstrLops,
       "prvtCESModuleServiceClock": prvtCESModuleServiceClock,
       "prvtCESModulePolicyuUnstrReplacePattern": prvtCESModulePolicyuUnstrReplacePattern,
       "prvtCESUnappTable": prvtCESUnappTable,
       "prvtCESUnappEntry": prvtCESUnappEntry,
       "prvtCESUnappLineType": prvtCESUnappLineType,
       "prvtCESUnappLineCoding": prvtCESUnappLineCoding,
       "prvtCESUnappLoopbackConfig": prvtCESUnappLoopbackConfig,
       "prvtCESUnappSignalMode": prvtCESUnappSignalMode,
       "prvtCESUnappTransmitClockSource": prvtCESUnappTransmitClockSource,
       "prvtCESUnappTransmitClockBackup": prvtCESUnappTransmitClockBackup,
       "prvtCESUnappLineLength": prvtCESUnappLineLength,
       "prvtCESUnappLineMode": prvtCESUnappLineMode,
       "prvtCESUnappLineBuildOut": prvtCESUnappLineBuildOut,
       "prvtCESUnappE1Impedance": prvtCESUnappE1Impedance,
       "prvtCESUnappT1GainLimit": prvtCESUnappT1GainLimit,
       "prvtCESUnappIPAddress": prvtCESUnappIPAddress,
       "prvtCESUnappIPAddressMask": prvtCESUnappIPAddressMask,
       "prvtCESUnappGateway": prvtCESUnappGateway,
       "prvtCESDsx1AlarmTable": prvtCESDsx1AlarmTable,
       "prvtCESDsx1AlarmEntry": prvtCESDsx1AlarmEntry,
       "prvtCESDsx1AlarmPort": prvtCESDsx1AlarmPort,
       "prvtCESDsx1AlarmIndex": prvtCESDsx1AlarmIndex,
       "prvtCESDsx1AlarmVariable": prvtCESDsx1AlarmVariable,
       "prvtCESDsx1AlarmThreshold": prvtCESDsx1AlarmThreshold,
       "prvtCESDsx1AlarmValue": prvtCESDsx1AlarmValue,
       "prvtCESAlarmMonitor": prvtCESAlarmMonitor,
       "prvtCESCICTable": prvtCESCICTable,
       "prvtCESCICEntry": prvtCESCICEntry,
       "prvtCESCICModuleId": prvtCESCICModuleId,
       "prvtCESCICNumber": prvtCESCICNumber,
       "prvtCESCICClockNumber": prvtCESCICClockNumber,
       "prvtCESCICMode": prvtCESCICMode,
       "prvtCESCICTdmPort": prvtCESCICTdmPort,
       "prvtCESCICCircuit": prvtCESCICCircuit,
       "prvtCESCICStatus": prvtCESCICStatus,
       "prvtCESCICState": prvtCESCICState,
       "prvtCESCICMappTable": prvtCESCICMappTable,
       "prvtCESCICMappEntry": prvtCESCICMappEntry,
       "prvtCESCICMappModuleId": prvtCESCICMappModuleId,
       "prvtCESCICMappClockNumber": prvtCESCICMappClockNumber,
       "prvtCESCICMappCICNumber": prvtCESCICMappCICNumber,
       "prvtCESCICMappState": prvtCESCICMappState,
       "prvtCESApsTable": prvtCESApsTable,
       "prvtCESApsEntry": prvtCESApsEntry,
       "prvtCESApsModuleId": prvtCESApsModuleId,
       "prvtCESApsEnable": prvtCESApsEnable,
       "prvtCESApsActiveLine": prvtCESApsActiveLine,
       "prvtSdBerThreshold": prvtSdBerThreshold,
       "prvtSfBerThreshold": prvtSfBerThreshold,
       "prvtCESUpdateFirmwareTable": prvtCESUpdateFirmwareTable,
       "prvtCESUpdateFirmwareEntry": prvtCESUpdateFirmwareEntry,
       "prvtCESModuleId": prvtCESModuleId,
       "prvtCESFirmwareImageName": prvtCESFirmwareImageName,
       "prvtCESUpdateAction": prvtCESUpdateAction,
       "prvtCESUpdateStatus": prvtCESUpdateStatus,
       "prvtCESTFTPServer": prvtCESTFTPServer,
       "prvtCESConformance": prvtCESConformance,
       "prvtCESDsx1Compliances": prvtCESDsx1Compliances,
       "prvtCESDsx1Compliance": prvtCESDsx1Compliance,
       "prvtCESDsx1Groups": prvtCESDsx1Groups,
       "prvtCESDsx1NotificationsGroup": prvtCESDsx1NotificationsGroup,
       "prvtCESDsx1ROGroup": prvtCESDsx1ROGroup}
)
