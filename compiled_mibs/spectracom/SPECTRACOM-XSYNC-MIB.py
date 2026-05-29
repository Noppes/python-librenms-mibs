# SNMP MIB module (SPECTRACOM-XSYNC-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\spectracom\SPECTRACOM-XSYNC-MIB

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")

(specModules,
 specProducts) = mibBuilder.importSymbols(
    "SPECTRACOM-GLOBAL-REG-MIB",
    "specModules",
    "specProducts")


# MODULE-IDENTITY

spectracomxSyncMibModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 18837, 1, 1, 4)
)
if mibBuilder.loadTexts:
    spectracomxSyncMibModule.setRevisions(
        ("2022-12-09 10:30",
         "2022-06-20 09:31",
         "2022-01-10 16:01",
         "2022-01-07 00:00",
         "2017-10-04 11:51",
         "2015-11-10 13:00",
         "2015-02-20 19:24",
         "2014-10-08 14:53",
         "2013-06-17 14:53",
         "2012-02-02 00:00",
         "2011-10-31 00:00",
         "2011-03-28 00:00",
         "2010-07-26 00:00",
         "2010-04-17 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_SpecxSyncMIB_ObjectIdentity = ObjectIdentity
specxSyncMIB = _SpecxSyncMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18837, 3, 2)
)
_SpecxSyncConfs_ObjectIdentity = ObjectIdentity
specxSyncConfs = _SpecxSyncConfs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18837, 3, 2, 1)
)
_SpecxSyncGroups_ObjectIdentity = ObjectIdentity
specxSyncGroups = _SpecxSyncGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18837, 3, 2, 1, 1)
)
_SpecxSyncCompl_ObjectIdentity = ObjectIdentity
specxSyncCompl = _SpecxSyncCompl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18837, 3, 2, 1, 2)
)
_SpecxSyncObjs_ObjectIdentity = ObjectIdentity
specxSyncObjs = _SpecxSyncObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18837, 3, 2, 2)
)
_SsSystemStatusObjs_ObjectIdentity = ObjectIdentity
ssSystemStatusObjs = _SsSystemStatusObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18837, 3, 2, 2, 1)
)


class _SsSysStaPowerDC_Type(Integer32):
    """Custom type ssSysStaPowerDC based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("ok", 1),
          ("alarm", 2),
          ("none", 3))
    )


_SsSysStaPowerDC_Type.__name__ = "Integer32"
_SsSysStaPowerDC_Object = MibScalar
ssSysStaPowerDC = _SsSysStaPowerDC_Object(
    (1, 3, 6, 1, 4, 1, 18837, 3, 2, 2, 1, 2),
    _SsSysStaPowerDC_Type()
)
ssSysStaPowerDC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssSysStaPowerDC.setStatus("current")


class _SsSysStaTimeReference_Type(DisplayString):
    """Custom type ssSysStaTimeReference based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(5, 5),
    )
    fixed_length = 5


_SsSysStaTimeReference_Type.__name__ = "DisplayString"
_SsSysStaTimeReference_Object = MibScalar
ssSysStaTimeReference = _SsSysStaTimeReference_Object(
    (1, 3, 6, 1, 4, 1, 18837, 3, 2, 2, 1, 3),
    _SsSysStaTimeReference_Type()
)
ssSysStaTimeReference.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssSysStaTimeReference.setStatus("current")


class _SsSysSta1PPSReference_Type(DisplayString):
    """Custom type ssSysSta1PPSReference based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(5, 5),
    )
    fixed_length = 5


_SsSysSta1PPSReference_Type.__name__ = "DisplayString"
_SsSysSta1PPSReference_Object = MibScalar
ssSysSta1PPSReference = _SsSysSta1PPSReference_Object(
    (1, 3, 6, 1, 4, 1, 18837, 3, 2, 2, 1, 4),
    _SsSysSta1PPSReference_Type()
)
ssSysSta1PPSReference.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssSysSta1PPSReference.setStatus("current")


class _SsSysStaSyncState_Type(Integer32):
    """Custom type ssSysStaSyncState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("sync", 1),
          ("nosync", 2))
    )


_SsSysStaSyncState_Type.__name__ = "Integer32"
_SsSysStaSyncState_Object = MibScalar
ssSysStaSyncState = _SsSysStaSyncState_Object(
    (1, 3, 6, 1, 4, 1, 18837, 3, 2, 2, 1, 5),
    _SsSysStaSyncState_Type()
)
ssSysStaSyncState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssSysStaSyncState.setStatus("current")


class _SsSysStaHoldoverState_Type(Integer32):
    """Custom type ssSysStaHoldoverState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("inHoldover", 1),
          ("notInHoldover", 2))
    )


_SsSysStaHoldoverState_Type.__name__ = "Integer32"
_SsSysStaHoldoverState_Object = MibScalar
ssSysStaHoldoverState = _SsSysStaHoldoverState_Object(
    (1, 3, 6, 1, 4, 1, 18837, 3, 2, 2, 1, 6),
    _SsSysStaHoldoverState_Type()
)
ssSysStaHoldoverState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssSysStaHoldoverState.setStatus("current")


class _SsSysStaTfom_Type(Unsigned32):
    """Custom type ssSysStaTfom based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_SsSysStaTfom_Type.__name__ = "Unsigned32"
_SsSysStaTfom_Object = MibScalar
ssSysStaTfom = _SsSysStaTfom_Object(
    (1, 3, 6, 1, 4, 1, 18837, 3, 2, 2, 1, 7),
    _SsSysStaTfom_Type()
)
ssSysStaTfom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssSysStaTfom.setStatus("current")
_SsSysStaEstPhaseError_Type = Integer32
_SsSysStaEstPhaseError_Object = MibScalar
ssSysStaEstPhaseError = _SsSysStaEstPhaseError_Object(
    (1, 3, 6, 1, 4, 1, 18837, 3, 2, 2, 1, 8),
    _SsSysStaEstPhaseError_Type()
)
ssSysStaEstPhaseError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssSysStaEstPhaseError.setStatus("current")
if mibBuilder.loadTexts:
    ssSysStaEstPhaseError.setUnits("nanoseconds")


class _SsSysStaEstFreqError_Type(DisplayString):
    """Custom type ssSysStaEstFreqError based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(20, 20),
    )
    fixed_length = 20


_SsSysStaEstFreqError_Type.__name__ = "DisplayString"
_SsSysStaEstFreqError_Object = MibScalar
ssSysStaEstFreqError = _SsSysStaEstFreqError_Object(
    (1, 3, 6, 1, 4, 1, 18837, 3, 2, 2, 1, 9),
    _SsSysStaEstFreqError_Type()
)
ssSysStaEstFreqError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssSysStaEstFreqError.setStatus("current")
if mibBuilder.loadTexts:
    ssSysStaEstFreqError.setUnits("hertz")


class _SsSysStaTimeScale_Type(Integer32):
    """Custom type ssSysStaTimeScale based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("utc", 1),
          ("tai", 2),
          ("gps", 3))
    )


_SsSysStaTimeScale_Type.__name__ = "Integer32"
_SsSysStaTimeScale_Object = MibScalar
ssSysStaTimeScale = _SsSysStaTimeScale_Object(
    (1, 3, 6, 1, 4, 1, 18837, 3, 2, 2, 1, 10),
    _SsSysStaTimeScale_Type()
)
ssSysStaTimeScale.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssSysStaTimeScale.setStatus("current")


class _SsSysStaVersion_Type(DisplayString):
    """Custom type ssSysStaVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(20, 20),
    )
    fixed_length = 20


_SsSysStaVersion_Type.__name__ = "DisplayString"
_SsSysStaVersion_Object = MibScalar
ssSysStaVersion = _SsSysStaVersion_Object(
    (1, 3, 6, 1, 4, 1, 18837, 3, 2, 2, 1, 11),
    _SsSysStaVersion_Type()
)
ssSysStaVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssSysStaVersion.setStatus("current")


class _SsSysStaTimingVersion_Type(DisplayString):
    """Custom type ssSysStaTimingVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(20, 20),
    )
    fixed_length = 20


_SsSysStaTimingVersion_Type.__name__ = "DisplayString"
_SsSysStaTimingVersion_Object = MibScalar
ssSysStaTimingVersion = _SsSysStaTimingVersion_Object(
    (1, 3, 6, 1, 4, 1, 18837, 3, 2, 2, 1, 12),
    _SsSysStaTimingVersion_Type()
)
ssSysStaTimingVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssSysStaTimingVersion.setStatus("current")


class _SsSysStaMinorAlarm_Type(Integer32):
    """Custom type ssSysStaMinorAlarm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("pending", 1),
          ("clear", 2))
    )


_SsSysStaMinorAlarm_Type.__name__ = "Integer32"
_SsSysStaMinorAlarm_Object = MibScalar
ssSysStaMinorAlarm = _SsSysStaMinorAlarm_Object(
    (1, 3, 6, 1, 4, 1, 18837, 3, 2, 2, 1, 13),
    _SsSysStaMinorAlarm_Type()
)
ssSysStaMinorAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssSysStaMinorAlarm.setStatus("current")


class _SsSysStaMajorAlarm_Type(Integer32):
    """Custom type ssSysStaMajorAlarm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("pending", 1),
          ("clear", 2))
    )


_SsSysStaMajorAlarm_Type.__name__ = "Integer32"
_SsSysStaMajorAlarm_Object = MibScalar
ssSysStaMajorAlarm = _SsSysStaMajorAlarm_Object(
    (1, 3, 6, 1, 4, 1, 18837, 3, 2, 2, 1, 14),
    _SsSysStaMajorAlarm_Type()
)
ssSysStaMajorAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssSysStaMajorAlarm.setStatus("current")


class _SsSysStaDateTime_Type(DisplayString):
    """Custom type ssSysStaDateTime based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(30, 30),
    )
    fixed_length = 30


_SsSysStaDateTime_Type.__name__ = "DisplayString"
_SsSysStaDateTime_Object = MibScalar
ssSysStaDateTime = _SsSysStaDateTime_Object(
    (1, 3, 6, 1, 4, 1, 18837, 3, 2, 2, 1, 15),
    _SsSysStaDateTime_Type()
)
ssSysStaDateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssSysStaDateTime.setStatus("current")


class _SsSysStaSerial_Type(DisplayString):
    """Custom type ssSysStaSerial based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(20, 20),
    )
    fixed_length = 20


_SsSysStaSerial_Type.__name__ = "DisplayString"
_SsSysStaSerial_Object = MibScalar
ssSysStaSerial = _SsSysStaSerial_Object(
    (1, 3, 6, 1, 4, 1, 18837, 3, 2, 2, 1, 16),
    _SsSysStaSerial_Type()
)
ssSysStaSerial.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssSysStaSerial.setStatus("current")


class _SsSysStaOscTemp_Type(DisplayString):
    """Custom type ssSysStaOscTemp based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(20, 20),
    )
    fixed_length = 20


_SsSysStaOscTemp_Type.__name__ = "DisplayString"
_SsSysStaOscTemp_Object = MibScalar
ssSysStaOscTemp = _SsSysStaOscTemp_Object(
    (1, 3, 6, 1, 4, 1, 18837, 3, 2, 2, 1, 17),
    _SsSysStaOscTemp_Type()
)
ssSysStaOscTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssSysStaOscTemp.setStatus("current")


class _SsSysStaBrdTemp_Type(DisplayString):
    """Custom type ssSysStaBrdTemp based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(20, 20),
    )
    fixed_length = 20


_SsSysStaBrdTemp_Type.__name__ = "DisplayString"
_SsSysStaBrdTemp_Object = MibScalar
ssSysStaBrdTemp = _SsSysStaBrdTemp_Object(
    (1, 3, 6, 1, 4, 1, 18837, 3, 2, 2, 1, 18),
    _SsSysStaBrdTemp_Type()
)
ssSysStaBrdTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssSysStaBrdTemp.setStatus("current")


class _SsSysStaCpuTemp_Type(DisplayString):
    """Custom type ssSysStaCpuTemp based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(20, 20),
    )
    fixed_length = 20


_SsSysStaCpuTemp_Type.__name__ = "DisplayString"
_SsSysStaCpuTemp_Object = MibScalar
ssSysStaCpuTemp = _SsSysStaCpuTemp_Object(
    (1, 3, 6, 1, 4, 1, 18837, 3, 2, 2, 1, 19),
    _SsSysStaCpuTemp_Type()
)
ssSysStaCpuTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssSysStaCpuTemp.setStatus("current")


class _SsSysStaMinorAlarmCauses_Type(DisplayString):
    """Custom type ssSysStaMinorAlarmCauses based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(128, 128),
    )
    fixed_length = 128


_SsSysStaMinorAlarmCauses_Type.__name__ = "DisplayString"
_SsSysStaMinorAlarmCauses_Object = MibScalar
ssSysStaMinorAlarmCauses = _SsSysStaMinorAlarmCauses_Object(
    (1, 3, 6, 1, 4, 1, 18837, 3, 2, 2, 1, 20),
    _SsSysStaMinorAlarmCauses_Type()
)
ssSysStaMinorAlarmCauses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssSysStaMinorAlarmCauses.setStatus("current")


class _SsSysStaMajorAlarmCauses_Type(DisplayString):
    """Custom type ssSysStaMajorAlarmCauses based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(128, 128),
    )
    fixed_length = 128


_SsSysStaMajorAlarmCauses_Type.__name__ = "DisplayString"
_SsSysStaMajorAlarmCauses_Object = MibScalar
ssSysStaMajorAlarmCauses = _SsSysStaMajorAlarmCauses_Object(
    (1, 3, 6, 1, 4, 1, 18837, 3, 2, 2, 1, 21),
    _SsSysStaMajorAlarmCauses_Type()
)
ssSysStaMajorAlarmCauses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssSysStaMajorAlarmCauses.setStatus("current")


class _SsSysStaBshJammingState_Type(Integer32):
    """Custom type ssSysStaBshJammingState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("noactive", 2))
    )


_SsSysStaBshJammingState_Type.__name__ = "Integer32"
_SsSysStaBshJammingState_Object = MibScalar
ssSysStaBshJammingState = _SsSysStaBshJammingState_Object(
    (1, 3, 6, 1, 4, 1, 18837, 3, 2, 2, 1, 22),
    _SsSysStaBshJammingState_Type()
)
ssSysStaBshJammingState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssSysStaBshJammingState.setStatus("current")


class _SsSysStaBshSpoofingState_Type(Integer32):
    """Custom type ssSysStaBshSpoofingState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("noactive", 2))
    )


_SsSysStaBshSpoofingState_Type.__name__ = "Integer32"
_SsSysStaBshSpoofingState_Object = MibScalar
ssSysStaBshSpoofingState = _SsSysStaBshSpoofingState_Object(
    (1, 3, 6, 1, 4, 1, 18837, 3, 2, 2, 1, 23),
    _SsSysStaBshSpoofingState_Type()
)
ssSysStaBshSpoofingState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssSysStaBshSpoofingState.setStatus("current")


class _SsSysStaDisciplining_Type(Integer32):
    """Custom type ssSysStaDisciplining based on Integer32"""
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
          ("warmup", 1),
          ("calibration", 2),
          ("trackSetup", 3),
          ("trackLock", 4),
          ("freerun", 5),
          ("fault", 6))
    )


_SsSysStaDisciplining_Type.__name__ = "Integer32"
_SsSysStaDisciplining_Object = MibScalar
ssSysStaDisciplining = _SsSysStaDisciplining_Object(
    (1, 3, 6, 1, 4, 1, 18837, 3, 2, 2, 1, 24),
    _SsSysStaDisciplining_Type()
)
ssSysStaDisciplining.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssSysStaDisciplining.setStatus("current")
_SsGpsRefStatusObjs_ObjectIdentity = ObjectIdentity
ssGpsRefStatusObjs = _SsGpsRefStatusObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18837, 3, 2, 2, 2)
)
_SsGpsRefTable_Object = MibTable
ssGpsRefTable = _SsGpsRefTable_Object(
    (1, 3, 6, 1, 4, 1, 18837, 3, 2, 2, 2, 1)
)
if mibBuilder.loadTexts:
    ssGpsRefTable.setStatus("current")
_SsGpsRefTableEntry_Object = MibTableRow
ssGpsRefTableEntry = _SsGpsRefTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 18837, 3, 2, 2, 2, 1, 1)
)
ssGpsRefTableEntry.setIndexNames(
    (0, "SPECTRACOM-XSYNC-MIB", "ssGpsRefRow"),
)
if mibBuilder.loadTexts:
    ssGpsRefTableEntry.setStatus("current")


class _SsGpsRefRow_Type(Unsigned32):
    """Custom type ssGpsRefRow based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_SsGpsRefRow_Type.__name__ = "Unsigned32"
_SsGpsRefRow_Object = MibTableColumn
ssGpsRefRow = _SsGpsRefRow_Object(
    (1, 3, 6, 1, 4, 1, 18837, 3, 2, 2, 2, 1, 1, 1),
    _SsGpsRefRow_Type()
)
ssGpsRefRow.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ssGpsRefRow.setStatus("current")


class _SsGpsRefInstance_Type(Unsigned32):
    """Custom type ssGpsRefInstance based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_SsGpsRefInstance_Type.__name__ = "Unsigned32"
_SsGpsRefInstance_Object = MibTableColumn
ssGpsRefInstance = _SsGpsRefInstance_Object(
    (1, 3, 6, 1, 4, 1, 18837, 3, 2, 2, 2, 1, 1, 2),
    _SsGpsRefInstance_Type()
)
ssGpsRefInstance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssGpsRefInstance.setStatus("current")


class _SsGpsReference_Type(DisplayString):
    """Custom type ssGpsReference based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(5, 5),
    )
    fixed_length = 5


_SsGpsReference_Type.__name__ = "DisplayString"
_SsGpsReference_Object = MibTableColumn
ssGpsReference = _SsGpsReference_Object(
    (1, 3, 6, 1, 4, 1, 18837, 3, 2, 2, 2, 1, 1, 3),
    _SsGpsReference_Type()
)
ssGpsReference.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssGpsReference.setStatus("current")


class _SsGpsRefTimeValid_Type(Integer32):
    """Custom type ssGpsRefTimeValid based on Integer32"""
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


_SsGpsRefTimeValid_Type.__name__ = "Integer32"
_SsGpsRefTimeValid_Object = MibTableColumn
ssGpsRefTimeValid = _SsGpsRefTimeValid_Object(
    (1, 3, 6, 1, 4, 1, 18837, 3, 2, 2, 2, 1, 1, 4),
    _SsGpsRefTimeValid_Type()
)
ssGpsRefTimeValid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssGpsRefTimeValid.setStatus("current")


class _SsGpsRef1ppsValid_Type(Integer32):
    """Custom type ssGpsRef1ppsValid based on Integer32"""
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


_SsGpsRef1ppsValid_Type.__name__ = "Integer32"
_SsGpsRef1ppsValid_Object = MibTableColumn
ssGpsRef1ppsValid = _SsGpsRef1ppsValid_Object(
    (1, 3, 6, 1, 4, 1, 18837, 3, 2, 2, 2, 1, 1, 5),
    _SsGpsRef1ppsValid_Type()
)
ssGpsRef1ppsValid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssGpsRef1ppsValid.setStatus("current")


class _SsGpsRefRcvMode_Type(Integer32):
    """Custom type ssGpsRefRcvMode based on Integer32"""
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
        *(("singleSat", 1),
          ("standard", 2),
          ("continuous", 3),
          ("averaging", 4),
          ("timeOnly", 5),
          ("standby", 6),
          ("selfTest", 7))
    )


_SsGpsRefRcvMode_Type.__name__ = "Integer32"
_SsGpsRefRcvMode_Object = MibTableColumn
ssGpsRefRcvMode = _SsGpsRefRcvMode_Object(
    (1, 3, 6, 1, 4, 1, 18837, 3, 2, 2, 2, 1, 1, 6),
    _SsGpsRefRcvMode_Type()
)
ssGpsRefRcvMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssGpsRefRcvMode.setStatus("current")


class _SsGpsRefDynMode_Type(Integer32):
    """Custom type ssGpsRefDynMode based on Integer32"""
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
        *(("land", 1),
          ("sea", 2),
          ("air", 3),
          ("stationary", 4))
    )


_SsGpsRefDynMode_Type.__name__ = "Integer32"
_SsGpsRefDynMode_Object = MibTableColumn
ssGpsRefDynMode = _SsGpsRefDynMode_Object(
    (1, 3, 6, 1, 4, 1, 18837, 3, 2, 2, 2, 1, 1, 7),
    _SsGpsRefDynMode_Type()
)
ssGpsRefDynMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssGpsRefDynMode.setStatus("current")
_SsGpsRefNumSats_Type = Unsigned32
_SsGpsRefNumSats_Object = MibTableColumn
ssGpsRefNumSats = _SsGpsRefNumSats_Object(
    (1, 3, 6, 1, 4, 1, 18837, 3, 2, 2, 2, 1, 1, 8),
    _SsGpsRefNumSats_Type()
)
ssGpsRefNumSats.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssGpsRefNumSats.setStatus("current")


class _SsGpsRefPdop_Type(DisplayString):
    """Custom type ssGpsRefPdop based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(20, 20),
    )
    fixed_length = 20


_SsGpsRefPdop_Type.__name__ = "DisplayString"
_SsGpsRefPdop_Object = MibTableColumn
ssGpsRefPdop = _SsGpsRefPdop_Object(
    (1, 3, 6, 1, 4, 1, 18837, 3, 2, 2, 2, 1, 1, 9),
    _SsGpsRefPdop_Type()
)
ssGpsRefPdop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssGpsRefPdop.setStatus("current")


class _SsGpsRefHdop_Type(DisplayString):
    """Custom type ssGpsRefHdop based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(20, 20),
    )
    fixed_length = 20


_SsGpsRefHdop_Type.__name__ = "DisplayString"
_SsGpsRefHdop_Object = MibTableColumn
ssGpsRefHdop = _SsGpsRefHdop_Object(
    (1, 3, 6, 1, 4, 1, 18837, 3, 2, 2, 2, 1, 1, 10),
    _SsGpsRefHdop_Type()
)
ssGpsRefHdop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssGpsRefHdop.setStatus("current")


class _SsGpsRefVdop_Type(DisplayString):
    """Custom type ssGpsRefVdop based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(20, 20),
    )
    fixed_length = 20


_SsGpsRefVdop_Type.__name__ = "DisplayString"
_SsGpsRefVdop_Object = MibTableColumn
ssGpsRefVdop = _SsGpsRefVdop_Object(
    (1, 3, 6, 1, 4, 1, 18837, 3, 2, 2, 2, 1, 1, 11),
    _SsGpsRefVdop_Type()
)
ssGpsRefVdop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssGpsRefVdop.setStatus("current")


class _SsGpsRefTdop_Type(DisplayString):
    """Custom type ssGpsRefTdop based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(20, 20),
    )
    fixed_length = 20


_SsGpsRefTdop_Type.__name__ = "DisplayString"
_SsGpsRefTdop_Object = MibTableColumn
ssGpsRefTdop = _SsGpsRefTdop_Object(
    (1, 3, 6, 1, 4, 1, 18837, 3, 2, 2, 2, 1, 1, 12),
    _SsGpsRefTdop_Type()
)
ssGpsRefTdop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssGpsRefTdop.setStatus("current")


class _SsGpsRefLatitude_Type(DisplayString):
    """Custom type ssGpsRefLatitude based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(20, 20),
    )
    fixed_length = 20


_SsGpsRefLatitude_Type.__name__ = "DisplayString"
_SsGpsRefLatitude_Object = MibTableColumn
ssGpsRefLatitude = _SsGpsRefLatitude_Object(
    (1, 3, 6, 1, 4, 1, 18837, 3, 2, 2, 2, 1, 1, 13),
    _SsGpsRefLatitude_Type()
)
ssGpsRefLatitude.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssGpsRefLatitude.setStatus("current")
if mibBuilder.loadTexts:
    ssGpsRefLatitude.setUnits("degrees")


class _SsGpsRefLongitude_Type(DisplayString):
    """Custom type ssGpsRefLongitude based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(20, 20),
    )
    fixed_length = 20


_SsGpsRefLongitude_Type.__name__ = "DisplayString"
_SsGpsRefLongitude_Object = MibTableColumn
ssGpsRefLongitude = _SsGpsRefLongitude_Object(
    (1, 3, 6, 1, 4, 1, 18837, 3, 2, 2, 2, 1, 1, 14),
    _SsGpsRefLongitude_Type()
)
ssGpsRefLongitude.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssGpsRefLongitude.setStatus("current")
if mibBuilder.loadTexts:
    ssGpsRefLongitude.setUnits("degrees")


class _SsGpsRefAltitude_Type(DisplayString):
    """Custom type ssGpsRefAltitude based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(20, 20),
    )
    fixed_length = 20


_SsGpsRefAltitude_Type.__name__ = "DisplayString"
_SsGpsRefAltitude_Object = MibTableColumn
ssGpsRefAltitude = _SsGpsRefAltitude_Object(
    (1, 3, 6, 1, 4, 1, 18837, 3, 2, 2, 2, 1, 1, 15),
    _SsGpsRefAltitude_Type()
)
ssGpsRefAltitude.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssGpsRefAltitude.setStatus("current")
if mibBuilder.loadTexts:
    ssGpsRefAltitude.setUnits("meters")
_SsGpsRefOffset_Type = Integer32
_SsGpsRefOffset_Object = MibTableColumn
ssGpsRefOffset = _SsGpsRefOffset_Object(
    (1, 3, 6, 1, 4, 1, 18837, 3, 2, 2, 2, 1, 1, 16),
    _SsGpsRefOffset_Type()
)
ssGpsRefOffset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssGpsRefOffset.setStatus("current")
if mibBuilder.loadTexts:
    ssGpsRefOffset.setUnits("nanoseconds")


class _SsGpsRefAntennaState_Type(Integer32):
    """Custom type ssGpsRefAntennaState based on Integer32"""
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
        *(("ok", 1),
          ("short", 2),
          ("open", 3),
          ("unknown", 4))
    )


_SsGpsRefAntennaState_Type.__name__ = "Integer32"
_SsGpsRefAntennaState_Object = MibTableColumn
ssGpsRefAntennaState = _SsGpsRefAntennaState_Object(
    (1, 3, 6, 1, 4, 1, 18837, 3, 2, 2, 2, 1, 1, 17),
    _SsGpsRefAntennaState_Type()
)
ssGpsRefAntennaState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssGpsRefAntennaState.setStatus("current")
_SsOptionCardObjs_ObjectIdentity = ObjectIdentity
ssOptionCardObjs = _SsOptionCardObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18837, 3, 2, 2, 3)
)
_SsReferenceMgmtObjs_ObjectIdentity = ObjectIdentity
ssReferenceMgmtObjs = _SsReferenceMgmtObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18837, 3, 2, 2, 4)
)
_SsRefMgmtTable_Object = MibTable
ssRefMgmtTable = _SsRefMgmtTable_Object(
    (1, 3, 6, 1, 4, 1, 18837, 3, 2, 2, 4, 1)
)
if mibBuilder.loadTexts:
    ssRefMgmtTable.setStatus("current")
_SsRefMgmtTableEntry_Object = MibTableRow
ssRefMgmtTableEntry = _SsRefMgmtTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 18837, 3, 2, 2, 4, 1, 1)
)
ssRefMgmtTableEntry.setIndexNames(
    (0, "SPECTRACOM-XSYNC-MIB", "ssRefMgmtRow"),
)
if mibBuilder.loadTexts:
    ssRefMgmtTableEntry.setStatus("current")


class _SsRefMgmtRow_Type(Unsigned32):
    """Custom type ssRefMgmtRow based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_SsRefMgmtRow_Type.__name__ = "Unsigned32"
_SsRefMgmtRow_Object = MibTableColumn
ssRefMgmtRow = _SsRefMgmtRow_Object(
    (1, 3, 6, 1, 4, 1, 18837, 3, 2, 2, 4, 1, 1, 1),
    _SsRefMgmtRow_Type()
)
ssRefMgmtRow.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ssRefMgmtRow.setStatus("current")


class _SsRefMgmtIndex_Type(Unsigned32):
    """Custom type ssRefMgmtIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 14),
    )


_SsRefMgmtIndex_Type.__name__ = "Unsigned32"
_SsRefMgmtIndex_Object = MibTableColumn
ssRefMgmtIndex = _SsRefMgmtIndex_Object(
    (1, 3, 6, 1, 4, 1, 18837, 3, 2, 2, 4, 1, 1, 2),
    _SsRefMgmtIndex_Type()
)
ssRefMgmtIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssRefMgmtIndex.setStatus("current")


class _SsRefMgmtState_Type(Integer32):
    """Custom type ssRefMgmtState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enabled", 1),
          ("disabled", 2))
    )


_SsRefMgmtState_Type.__name__ = "Integer32"
_SsRefMgmtState_Object = MibTableColumn
ssRefMgmtState = _SsRefMgmtState_Object(
    (1, 3, 6, 1, 4, 1, 18837, 3, 2, 2, 4, 1, 1, 3),
    _SsRefMgmtState_Type()
)
ssRefMgmtState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ssRefMgmtState.setStatus("current")


class _SsRefMgmtPriority_Type(Unsigned32):
    """Custom type ssRefMgmtPriority based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_SsRefMgmtPriority_Type.__name__ = "Unsigned32"
_SsRefMgmtPriority_Object = MibTableColumn
ssRefMgmtPriority = _SsRefMgmtPriority_Object(
    (1, 3, 6, 1, 4, 1, 18837, 3, 2, 2, 4, 1, 1, 4),
    _SsRefMgmtPriority_Type()
)
ssRefMgmtPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ssRefMgmtPriority.setStatus("current")


class _SsRefMgmtTime_Type(DisplayString):
    """Custom type ssRefMgmtTime based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(5, 5),
    )
    fixed_length = 5


_SsRefMgmtTime_Type.__name__ = "DisplayString"
_SsRefMgmtTime_Object = MibTableColumn
ssRefMgmtTime = _SsRefMgmtTime_Object(
    (1, 3, 6, 1, 4, 1, 18837, 3, 2, 2, 4, 1, 1, 5),
    _SsRefMgmtTime_Type()
)
ssRefMgmtTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssRefMgmtTime.setStatus("current")


class _SsRefMgmt1PPS_Type(DisplayString):
    """Custom type ssRefMgmt1PPS based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(5, 5),
    )
    fixed_length = 5


_SsRefMgmt1PPS_Type.__name__ = "DisplayString"
_SsRefMgmt1PPS_Object = MibTableColumn
ssRefMgmt1PPS = _SsRefMgmt1PPS_Object(
    (1, 3, 6, 1, 4, 1, 18837, 3, 2, 2, 4, 1, 1, 6),
    _SsRefMgmt1PPS_Type()
)
ssRefMgmt1PPS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssRefMgmt1PPS.setStatus("current")


class _SsRefMgmtTimeValid_Type(Integer32):
    """Custom type ssRefMgmtTimeValid based on Integer32"""
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


_SsRefMgmtTimeValid_Type.__name__ = "Integer32"
_SsRefMgmtTimeValid_Object = MibTableColumn
ssRefMgmtTimeValid = _SsRefMgmtTimeValid_Object(
    (1, 3, 6, 1, 4, 1, 18837, 3, 2, 2, 4, 1, 1, 7),
    _SsRefMgmtTimeValid_Type()
)
ssRefMgmtTimeValid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssRefMgmtTimeValid.setStatus("current")


class _SsRefMgmt1PPSValid_Type(Integer32):
    """Custom type ssRefMgmt1PPSValid based on Integer32"""
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


_SsRefMgmt1PPSValid_Type.__name__ = "Integer32"
_SsRefMgmt1PPSValid_Object = MibTableColumn
ssRefMgmt1PPSValid = _SsRefMgmt1PPSValid_Object(
    (1, 3, 6, 1, 4, 1, 18837, 3, 2, 2, 4, 1, 1, 8),
    _SsRefMgmt1PPSValid_Type()
)
ssRefMgmt1PPSValid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssRefMgmt1PPSValid.setStatus("current")
_SsSystemControlObjs_ObjectIdentity = ObjectIdentity
ssSystemControlObjs = _SsSystemControlObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18837, 3, 2, 2, 5)
)


class _SsSysCtrlCommand_Type(Integer32):
    """Custom type ssSysCtrlCommand based on Integer32"""
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
        *(("idle", 1),
          ("update", 2),
          ("forceupdate", 3),
          ("reboot", 4))
    )


_SsSysCtrlCommand_Type.__name__ = "Integer32"
_SsSysCtrlCommand_Object = MibScalar
ssSysCtrlCommand = _SsSysCtrlCommand_Object(
    (1, 3, 6, 1, 4, 1, 18837, 3, 2, 2, 5, 1),
    _SsSysCtrlCommand_Type()
)
ssSysCtrlCommand.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ssSysCtrlCommand.setStatus("current")


class _SsSysUpdateFile_Type(DisplayString):
    """Custom type ssSysUpdateFile based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(80, 80),
    )
    fixed_length = 80


_SsSysUpdateFile_Type.__name__ = "DisplayString"
_SsSysUpdateFile_Object = MibScalar
ssSysUpdateFile = _SsSysUpdateFile_Object(
    (1, 3, 6, 1, 4, 1, 18837, 3, 2, 2, 5, 2),
    _SsSysUpdateFile_Type()
)
ssSysUpdateFile.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssSysUpdateFile.setStatus("current")


class _SsSysSetManualTime_Type(OctetString):
    """Custom type ssSysSetManualTime based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_SsSysSetManualTime_Type.__name__ = "OctetString"
_SsSysSetManualTime_Object = MibScalar
ssSysSetManualTime = _SsSysSetManualTime_Object(
    (1, 3, 6, 1, 4, 1, 18837, 3, 2, 2, 5, 3),
    _SsSysSetManualTime_Type()
)
ssSysSetManualTime.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    ssSysSetManualTime.setStatus("current")
_SsHotSwapObjs_ObjectIdentity = ObjectIdentity
ssHotSwapObjs = _SsHotSwapObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18837, 3, 2, 2, 6)
)


class _SsHotSwapOverallHealth_Type(Integer32):
    """Custom type ssHotSwapOverallHealth based on Integer32"""
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
        *(("ok", 0),
          ("noMonitoring", 1),
          ("warning", 2),
          ("fault", 3))
    )


_SsHotSwapOverallHealth_Type.__name__ = "Integer32"
_SsHotSwapOverallHealth_Object = MibScalar
ssHotSwapOverallHealth = _SsHotSwapOverallHealth_Object(
    (1, 3, 6, 1, 4, 1, 18837, 3, 2, 2, 6, 0),
    _SsHotSwapOverallHealth_Type()
)
ssHotSwapOverallHealth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssHotSwapOverallHealth.setStatus("current")
_SsHotSwapBay1_ObjectIdentity = ObjectIdentity
ssHotSwapBay1 = _SsHotSwapBay1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18837, 3, 2, 2, 6, 1)
)


class _SsHotSwapBay1Health_Type(Integer32):
    """Custom type ssHotSwapBay1Health based on Integer32"""
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
        *(("ok", 0),
          ("noMonitoring", 1),
          ("warning", 2),
          ("fault", 3))
    )


_SsHotSwapBay1Health_Type.__name__ = "Integer32"
_SsHotSwapBay1Health_Object = MibScalar
ssHotSwapBay1Health = _SsHotSwapBay1Health_Object(
    (1, 3, 6, 1, 4, 1, 18837, 3, 2, 2, 6, 1, 0),
    _SsHotSwapBay1Health_Type()
)
ssHotSwapBay1Health.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssHotSwapBay1Health.setStatus("current")


class _SsHotSwapBay1Type_Type(Integer32):
    """Custom type ssHotSwapBay1Type based on Integer32"""
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
        *(("ac", 0),
          ("dc12", 1),
          ("dc24", 2),
          ("none", 3))
    )


_SsHotSwapBay1Type_Type.__name__ = "Integer32"
_SsHotSwapBay1Type_Object = MibScalar
ssHotSwapBay1Type = _SsHotSwapBay1Type_Object(
    (1, 3, 6, 1, 4, 1, 18837, 3, 2, 2, 6, 1, 1),
    _SsHotSwapBay1Type_Type()
)
ssHotSwapBay1Type.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssHotSwapBay1Type.setStatus("current")


class _SsHotSwapBay1Presence_Type(Integer32):
    """Custom type ssHotSwapBay1Presence based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("notInstalled", 0),
          ("installed", 1))
    )


_SsHotSwapBay1Presence_Type.__name__ = "Integer32"
_SsHotSwapBay1Presence_Object = MibScalar
ssHotSwapBay1Presence = _SsHotSwapBay1Presence_Object(
    (1, 3, 6, 1, 4, 1, 18837, 3, 2, 2, 6, 1, 2),
    _SsHotSwapBay1Presence_Type()
)
ssHotSwapBay1Presence.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssHotSwapBay1Presence.setStatus("current")


class _SsHotSwapBay1Voltage_Type(DisplayString):
    """Custom type ssHotSwapBay1Voltage based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(20, 20),
    )
    fixed_length = 20


_SsHotSwapBay1Voltage_Type.__name__ = "DisplayString"
_SsHotSwapBay1Voltage_Object = MibScalar
ssHotSwapBay1Voltage = _SsHotSwapBay1Voltage_Object(
    (1, 3, 6, 1, 4, 1, 18837, 3, 2, 2, 6, 1, 3),
    _SsHotSwapBay1Voltage_Type()
)
ssHotSwapBay1Voltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssHotSwapBay1Voltage.setStatus("current")


class _SsHotSwapBay1Current_Type(DisplayString):
    """Custom type ssHotSwapBay1Current based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(20, 20),
    )
    fixed_length = 20


_SsHotSwapBay1Current_Type.__name__ = "DisplayString"
_SsHotSwapBay1Current_Object = MibScalar
ssHotSwapBay1Current = _SsHotSwapBay1Current_Object(
    (1, 3, 6, 1, 4, 1, 18837, 3, 2, 2, 6, 1, 4),
    _SsHotSwapBay1Current_Type()
)
ssHotSwapBay1Current.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssHotSwapBay1Current.setStatus("current")


class _SsHotSwapBay1FanEnabled_Type(Integer32):
    """Custom type ssHotSwapBay1FanEnabled based on Integer32"""
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


_SsHotSwapBay1FanEnabled_Type.__name__ = "Integer32"
_SsHotSwapBay1FanEnabled_Object = MibScalar
ssHotSwapBay1FanEnabled = _SsHotSwapBay1FanEnabled_Object(
    (1, 3, 6, 1, 4, 1, 18837, 3, 2, 2, 6, 1, 5),
    _SsHotSwapBay1FanEnabled_Type()
)
ssHotSwapBay1FanEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssHotSwapBay1FanEnabled.setStatus("current")
_SsHotSwapBay1FanSpeed_Type = Integer32
_SsHotSwapBay1FanSpeed_Object = MibScalar
ssHotSwapBay1FanSpeed = _SsHotSwapBay1FanSpeed_Object(
    (1, 3, 6, 1, 4, 1, 18837, 3, 2, 2, 6, 1, 6),
    _SsHotSwapBay1FanSpeed_Type()
)
ssHotSwapBay1FanSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssHotSwapBay1FanSpeed.setStatus("current")


class _SsHotSwapBay1Temp_Type(DisplayString):
    """Custom type ssHotSwapBay1Temp based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(20, 20),
    )
    fixed_length = 20


_SsHotSwapBay1Temp_Type.__name__ = "DisplayString"
_SsHotSwapBay1Temp_Object = MibScalar
ssHotSwapBay1Temp = _SsHotSwapBay1Temp_Object(
    (1, 3, 6, 1, 4, 1, 18837, 3, 2, 2, 6, 1, 7),
    _SsHotSwapBay1Temp_Type()
)
ssHotSwapBay1Temp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssHotSwapBay1Temp.setStatus("current")


class _SsHotSwapBay1VoltageInRange_Type(Integer32):
    """Custom type ssHotSwapBay1VoltageInRange based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("outOfRange", 0),
          ("inRange", 1))
    )


_SsHotSwapBay1VoltageInRange_Type.__name__ = "Integer32"
_SsHotSwapBay1VoltageInRange_Object = MibScalar
ssHotSwapBay1VoltageInRange = _SsHotSwapBay1VoltageInRange_Object(
    (1, 3, 6, 1, 4, 1, 18837, 3, 2, 2, 6, 1, 8),
    _SsHotSwapBay1VoltageInRange_Type()
)
ssHotSwapBay1VoltageInRange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssHotSwapBay1VoltageInRange.setStatus("current")


class _SsHotSwapBay1CurrentInRange_Type(Integer32):
    """Custom type ssHotSwapBay1CurrentInRange based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("outOfRange", 0),
          ("inRange", 1))
    )


_SsHotSwapBay1CurrentInRange_Type.__name__ = "Integer32"
_SsHotSwapBay1CurrentInRange_Object = MibScalar
ssHotSwapBay1CurrentInRange = _SsHotSwapBay1CurrentInRange_Object(
    (1, 3, 6, 1, 4, 1, 18837, 3, 2, 2, 6, 1, 9),
    _SsHotSwapBay1CurrentInRange_Type()
)
ssHotSwapBay1CurrentInRange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssHotSwapBay1CurrentInRange.setStatus("current")


class _SsHotSwapBay1FanSpeedInRange_Type(Integer32):
    """Custom type ssHotSwapBay1FanSpeedInRange based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("outOfRange", 0),
          ("inRange", 1))
    )


_SsHotSwapBay1FanSpeedInRange_Type.__name__ = "Integer32"
_SsHotSwapBay1FanSpeedInRange_Object = MibScalar
ssHotSwapBay1FanSpeedInRange = _SsHotSwapBay1FanSpeedInRange_Object(
    (1, 3, 6, 1, 4, 1, 18837, 3, 2, 2, 6, 1, 10),
    _SsHotSwapBay1FanSpeedInRange_Type()
)
ssHotSwapBay1FanSpeedInRange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssHotSwapBay1FanSpeedInRange.setStatus("current")


class _SsHotSwapBay1TempInRange_Type(Integer32):
    """Custom type ssHotSwapBay1TempInRange based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("outOfRange", 0),
          ("inRange", 1))
    )


_SsHotSwapBay1TempInRange_Type.__name__ = "Integer32"
_SsHotSwapBay1TempInRange_Object = MibScalar
ssHotSwapBay1TempInRange = _SsHotSwapBay1TempInRange_Object(
    (1, 3, 6, 1, 4, 1, 18837, 3, 2, 2, 6, 1, 11),
    _SsHotSwapBay1TempInRange_Type()
)
ssHotSwapBay1TempInRange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssHotSwapBay1TempInRange.setStatus("current")
_SsHotSwapBay2_ObjectIdentity = ObjectIdentity
ssHotSwapBay2 = _SsHotSwapBay2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18837, 3, 2, 2, 6, 2)
)


class _SsHotSwapBay2Health_Type(Integer32):
    """Custom type ssHotSwapBay2Health based on Integer32"""
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
        *(("ok", 0),
          ("noMonitoring", 1),
          ("warning", 2),
          ("fault", 3))
    )


_SsHotSwapBay2Health_Type.__name__ = "Integer32"
_SsHotSwapBay2Health_Object = MibScalar
ssHotSwapBay2Health = _SsHotSwapBay2Health_Object(
    (1, 3, 6, 1, 4, 1, 18837, 3, 2, 2, 6, 2, 0),
    _SsHotSwapBay2Health_Type()
)
ssHotSwapBay2Health.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssHotSwapBay2Health.setStatus("current")


class _SsHotSwapBay2Type_Type(Integer32):
    """Custom type ssHotSwapBay2Type based on Integer32"""
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
        *(("ac", 0),
          ("dc12", 1),
          ("dc24", 2),
          ("none", 3))
    )


_SsHotSwapBay2Type_Type.__name__ = "Integer32"
_SsHotSwapBay2Type_Object = MibScalar
ssHotSwapBay2Type = _SsHotSwapBay2Type_Object(
    (1, 3, 6, 1, 4, 1, 18837, 3, 2, 2, 6, 2, 1),
    _SsHotSwapBay2Type_Type()
)
ssHotSwapBay2Type.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssHotSwapBay2Type.setStatus("current")


class _SsHotSwapBay2Presence_Type(Integer32):
    """Custom type ssHotSwapBay2Presence based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("notInstalled", 0),
          ("installed", 1))
    )


_SsHotSwapBay2Presence_Type.__name__ = "Integer32"
_SsHotSwapBay2Presence_Object = MibScalar
ssHotSwapBay2Presence = _SsHotSwapBay2Presence_Object(
    (1, 3, 6, 1, 4, 1, 18837, 3, 2, 2, 6, 2, 2),
    _SsHotSwapBay2Presence_Type()
)
ssHotSwapBay2Presence.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssHotSwapBay2Presence.setStatus("current")


class _SsHotSwapBay2Voltage_Type(DisplayString):
    """Custom type ssHotSwapBay2Voltage based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(20, 20),
    )
    fixed_length = 20


_SsHotSwapBay2Voltage_Type.__name__ = "DisplayString"
_SsHotSwapBay2Voltage_Object = MibScalar
ssHotSwapBay2Voltage = _SsHotSwapBay2Voltage_Object(
    (1, 3, 6, 1, 4, 1, 18837, 3, 2, 2, 6, 2, 3),
    _SsHotSwapBay2Voltage_Type()
)
ssHotSwapBay2Voltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssHotSwapBay2Voltage.setStatus("current")


class _SsHotSwapBay2Current_Type(DisplayString):
    """Custom type ssHotSwapBay2Current based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(20, 20),
    )
    fixed_length = 20


_SsHotSwapBay2Current_Type.__name__ = "DisplayString"
_SsHotSwapBay2Current_Object = MibScalar
ssHotSwapBay2Current = _SsHotSwapBay2Current_Object(
    (1, 3, 6, 1, 4, 1, 18837, 3, 2, 2, 6, 2, 4),
    _SsHotSwapBay2Current_Type()
)
ssHotSwapBay2Current.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssHotSwapBay2Current.setStatus("current")


class _SsHotSwapBay2FanEnabled_Type(Integer32):
    """Custom type ssHotSwapBay2FanEnabled based on Integer32"""
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


_SsHotSwapBay2FanEnabled_Type.__name__ = "Integer32"
_SsHotSwapBay2FanEnabled_Object = MibScalar
ssHotSwapBay2FanEnabled = _SsHotSwapBay2FanEnabled_Object(
    (1, 3, 6, 1, 4, 1, 18837, 3, 2, 2, 6, 2, 5),
    _SsHotSwapBay2FanEnabled_Type()
)
ssHotSwapBay2FanEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssHotSwapBay2FanEnabled.setStatus("current")
_SsHotSwapBay2FanSpeed_Type = Integer32
_SsHotSwapBay2FanSpeed_Object = MibScalar
ssHotSwapBay2FanSpeed = _SsHotSwapBay2FanSpeed_Object(
    (1, 3, 6, 1, 4, 1, 18837, 3, 2, 2, 6, 2, 6),
    _SsHotSwapBay2FanSpeed_Type()
)
ssHotSwapBay2FanSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssHotSwapBay2FanSpeed.setStatus("current")


class _SsHotSwapBay2Temp_Type(DisplayString):
    """Custom type ssHotSwapBay2Temp based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(20, 20),
    )
    fixed_length = 20


_SsHotSwapBay2Temp_Type.__name__ = "DisplayString"
_SsHotSwapBay2Temp_Object = MibScalar
ssHotSwapBay2Temp = _SsHotSwapBay2Temp_Object(
    (1, 3, 6, 1, 4, 1, 18837, 3, 2, 2, 6, 2, 7),
    _SsHotSwapBay2Temp_Type()
)
ssHotSwapBay2Temp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssHotSwapBay2Temp.setStatus("current")


class _SsHotSwapBay2VoltageInRange_Type(Integer32):
    """Custom type ssHotSwapBay2VoltageInRange based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("outOfRange", 0),
          ("inRange", 1))
    )


_SsHotSwapBay2VoltageInRange_Type.__name__ = "Integer32"
_SsHotSwapBay2VoltageInRange_Object = MibScalar
ssHotSwapBay2VoltageInRange = _SsHotSwapBay2VoltageInRange_Object(
    (1, 3, 6, 1, 4, 1, 18837, 3, 2, 2, 6, 2, 8),
    _SsHotSwapBay2VoltageInRange_Type()
)
ssHotSwapBay2VoltageInRange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssHotSwapBay2VoltageInRange.setStatus("current")


class _SsHotSwapBay2CurrentInRange_Type(Integer32):
    """Custom type ssHotSwapBay2CurrentInRange based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("outOfRange", 0),
          ("inRange", 1))
    )


_SsHotSwapBay2CurrentInRange_Type.__name__ = "Integer32"
_SsHotSwapBay2CurrentInRange_Object = MibScalar
ssHotSwapBay2CurrentInRange = _SsHotSwapBay2CurrentInRange_Object(
    (1, 3, 6, 1, 4, 1, 18837, 3, 2, 2, 6, 2, 9),
    _SsHotSwapBay2CurrentInRange_Type()
)
ssHotSwapBay2CurrentInRange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssHotSwapBay2CurrentInRange.setStatus("current")


class _SsHotSwapBay2FanSpeedInRange_Type(Integer32):
    """Custom type ssHotSwapBay2FanSpeedInRange based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("outOfRange", 0),
          ("inRange", 1))
    )


_SsHotSwapBay2FanSpeedInRange_Type.__name__ = "Integer32"
_SsHotSwapBay2FanSpeedInRange_Object = MibScalar
ssHotSwapBay2FanSpeedInRange = _SsHotSwapBay2FanSpeedInRange_Object(
    (1, 3, 6, 1, 4, 1, 18837, 3, 2, 2, 6, 2, 10),
    _SsHotSwapBay2FanSpeedInRange_Type()
)
ssHotSwapBay2FanSpeedInRange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssHotSwapBay2FanSpeedInRange.setStatus("current")


class _SsHotSwapBay2TempInRange_Type(Integer32):
    """Custom type ssHotSwapBay2TempInRange based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("outOfRange", 0),
          ("inRange", 1))
    )


_SsHotSwapBay2TempInRange_Type.__name__ = "Integer32"
_SsHotSwapBay2TempInRange_Object = MibScalar
ssHotSwapBay2TempInRange = _SsHotSwapBay2TempInRange_Object(
    (1, 3, 6, 1, 4, 1, 18837, 3, 2, 2, 6, 2, 11),
    _SsHotSwapBay2TempInRange_Type()
)
ssHotSwapBay2TempInRange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssHotSwapBay2TempInRange.setStatus("current")
_SpecxSyncEvents_ObjectIdentity = ObjectIdentity
specxSyncEvents = _SpecxSyncEvents_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18837, 3, 2, 3)
)
_SsEventsV2_ObjectIdentity = ObjectIdentity
ssEventsV2 = _SsEventsV2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18837, 3, 2, 3, 0)
)
_SsConformance_ObjectIdentity = ObjectIdentity
ssConformance = _SsConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18837, 3, 2, 90)
)
_SsCompliances_ObjectIdentity = ObjectIdentity
ssCompliances = _SsCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18837, 3, 2, 90, 1)
)
_SsGroups_ObjectIdentity = ObjectIdentity
ssGroups = _SsGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18837, 3, 2, 90, 2)
)

# Managed Objects groups

ssObjectsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 18837, 3, 2, 90, 2, 1)
)
ssObjectsGroup.setObjects(
      *(("SPECTRACOM-XSYNC-MIB", "ssSysStaPowerDC"),
        ("SPECTRACOM-XSYNC-MIB", "ssSysStaTimeReference"),
        ("SPECTRACOM-XSYNC-MIB", "ssSysSta1PPSReference"),
        ("SPECTRACOM-XSYNC-MIB", "ssSysStaSyncState"),
        ("SPECTRACOM-XSYNC-MIB", "ssSysStaHoldoverState"),
        ("SPECTRACOM-XSYNC-MIB", "ssSysStaTfom"),
        ("SPECTRACOM-XSYNC-MIB", "ssSysStaEstPhaseError"),
        ("SPECTRACOM-XSYNC-MIB", "ssSysStaEstFreqError"),
        ("SPECTRACOM-XSYNC-MIB", "ssSysStaTimeScale"),
        ("SPECTRACOM-XSYNC-MIB", "ssSysStaVersion"),
        ("SPECTRACOM-XSYNC-MIB", "ssSysStaTimingVersion"),
        ("SPECTRACOM-XSYNC-MIB", "ssSysStaMinorAlarm"),
        ("SPECTRACOM-XSYNC-MIB", "ssSysStaMajorAlarm"),
        ("SPECTRACOM-XSYNC-MIB", "ssSysStaDateTime"),
        ("SPECTRACOM-XSYNC-MIB", "ssSysStaSerial"),
        ("SPECTRACOM-XSYNC-MIB", "ssSysStaOscTemp"),
        ("SPECTRACOM-XSYNC-MIB", "ssSysStaBrdTemp"),
        ("SPECTRACOM-XSYNC-MIB", "ssSysStaCpuTemp"),
        ("SPECTRACOM-XSYNC-MIB", "ssSysStaBshJammingState"),
        ("SPECTRACOM-XSYNC-MIB", "ssSysStaBshSpoofingState"),
        ("SPECTRACOM-XSYNC-MIB", "ssSysStaDisciplining"),
        ("SPECTRACOM-XSYNC-MIB", "ssGpsRefInstance"),
        ("SPECTRACOM-XSYNC-MIB", "ssGpsReference"),
        ("SPECTRACOM-XSYNC-MIB", "ssGpsRefTimeValid"),
        ("SPECTRACOM-XSYNC-MIB", "ssGpsRef1ppsValid"),
        ("SPECTRACOM-XSYNC-MIB", "ssGpsRefRcvMode"),
        ("SPECTRACOM-XSYNC-MIB", "ssGpsRefDynMode"),
        ("SPECTRACOM-XSYNC-MIB", "ssGpsRefNumSats"),
        ("SPECTRACOM-XSYNC-MIB", "ssGpsRefPdop"),
        ("SPECTRACOM-XSYNC-MIB", "ssGpsRefHdop"),
        ("SPECTRACOM-XSYNC-MIB", "ssGpsRefVdop"),
        ("SPECTRACOM-XSYNC-MIB", "ssGpsRefTdop"),
        ("SPECTRACOM-XSYNC-MIB", "ssGpsRefLatitude"),
        ("SPECTRACOM-XSYNC-MIB", "ssGpsRefLongitude"),
        ("SPECTRACOM-XSYNC-MIB", "ssGpsRefAltitude"),
        ("SPECTRACOM-XSYNC-MIB", "ssGpsRefOffset"),
        ("SPECTRACOM-XSYNC-MIB", "ssGpsRefAntennaState"),
        ("SPECTRACOM-XSYNC-MIB", "ssRefMgmtIndex"),
        ("SPECTRACOM-XSYNC-MIB", "ssRefMgmtState"),
        ("SPECTRACOM-XSYNC-MIB", "ssRefMgmtPriority"),
        ("SPECTRACOM-XSYNC-MIB", "ssRefMgmtTime"),
        ("SPECTRACOM-XSYNC-MIB", "ssRefMgmt1PPS"),
        ("SPECTRACOM-XSYNC-MIB", "ssRefMgmtTimeValid"),
        ("SPECTRACOM-XSYNC-MIB", "ssRefMgmt1PPSValid"),
        ("SPECTRACOM-XSYNC-MIB", "ssSysCtrlCommand"),
        ("SPECTRACOM-XSYNC-MIB", "ssSysUpdateFile"),
        ("SPECTRACOM-XSYNC-MIB", "ssSysSetManualTime"),
        ("SPECTRACOM-XSYNC-MIB", "ssHotSwapOverallHealth"),
        ("SPECTRACOM-XSYNC-MIB", "ssHotSwapBay1Health"),
        ("SPECTRACOM-XSYNC-MIB", "ssHotSwapBay1Type"),
        ("SPECTRACOM-XSYNC-MIB", "ssHotSwapBay1Presence"),
        ("SPECTRACOM-XSYNC-MIB", "ssHotSwapBay1Voltage"),
        ("SPECTRACOM-XSYNC-MIB", "ssHotSwapBay1Current"),
        ("SPECTRACOM-XSYNC-MIB", "ssHotSwapBay1FanEnabled"),
        ("SPECTRACOM-XSYNC-MIB", "ssHotSwapBay1FanSpeed"),
        ("SPECTRACOM-XSYNC-MIB", "ssHotSwapBay1Temp"),
        ("SPECTRACOM-XSYNC-MIB", "ssHotSwapBay1VoltageInRange"),
        ("SPECTRACOM-XSYNC-MIB", "ssHotSwapBay1CurrentInRange"),
        ("SPECTRACOM-XSYNC-MIB", "ssHotSwapBay1FanSpeedInRange"),
        ("SPECTRACOM-XSYNC-MIB", "ssHotSwapBay1TempInRange"),
        ("SPECTRACOM-XSYNC-MIB", "ssHotSwapBay2Health"),
        ("SPECTRACOM-XSYNC-MIB", "ssHotSwapBay2Type"),
        ("SPECTRACOM-XSYNC-MIB", "ssHotSwapBay2Presence"),
        ("SPECTRACOM-XSYNC-MIB", "ssHotSwapBay2Voltage"),
        ("SPECTRACOM-XSYNC-MIB", "ssHotSwapBay2Current"),
        ("SPECTRACOM-XSYNC-MIB", "ssHotSwapBay2FanEnabled"),
        ("SPECTRACOM-XSYNC-MIB", "ssHotSwapBay2FanSpeed"),
        ("SPECTRACOM-XSYNC-MIB", "ssHotSwapBay2Temp"),
        ("SPECTRACOM-XSYNC-MIB", "ssHotSwapBay2VoltageInRange"),
        ("SPECTRACOM-XSYNC-MIB", "ssHotSwapBay2CurrentInRange"),
        ("SPECTRACOM-XSYNC-MIB", "ssHotSwapBay2FanSpeedInRange"),
        ("SPECTRACOM-XSYNC-MIB", "ssHotSwapBay2TempInRange"))
)
if mibBuilder.loadTexts:
    ssObjectsGroup.setStatus("current")


# Notification objects

ssEvtV2TimeSync = NotificationType(
    (1, 3, 6, 1, 4, 1, 18837, 3, 2, 3, 0, 1)
)
ssEvtV2TimeSync.setObjects(
    ("SPECTRACOM-XSYNC-MIB", "ssSysStaSyncState")
)
if mibBuilder.loadTexts:
    ssEvtV2TimeSync.setStatus(
        "current"
    )

ssEvtV2Holdover = NotificationType(
    (1, 3, 6, 1, 4, 1, 18837, 3, 2, 3, 0, 2)
)
ssEvtV2Holdover.setObjects(
    ("SPECTRACOM-XSYNC-MIB", "ssSysStaHoldoverState")
)
if mibBuilder.loadTexts:
    ssEvtV2Holdover.setStatus(
        "current"
    )

ssEvtV2FrequencyError = NotificationType(
    (1, 3, 6, 1, 4, 1, 18837, 3, 2, 3, 0, 3)
)
ssEvtV2FrequencyError.setObjects(
    ("SPECTRACOM-XSYNC-MIB", "ssSysStaEstFreqError")
)
if mibBuilder.loadTexts:
    ssEvtV2FrequencyError.setStatus(
        "current"
    )

ssEvtV2FrequencyOK = NotificationType(
    (1, 3, 6, 1, 4, 1, 18837, 3, 2, 3, 0, 4)
)
ssEvtV2FrequencyOK.setObjects(
    ("SPECTRACOM-XSYNC-MIB", "ssSysStaEstFreqError")
)
if mibBuilder.loadTexts:
    ssEvtV2FrequencyOK.setStatus(
        "current"
    )

ssEvtV2UserMinorAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 18837, 3, 2, 3, 0, 5)
)
ssEvtV2UserMinorAlarm.setObjects(
    ("SPECTRACOM-XSYNC-MIB", "ssGpsRefNumSats")
)
if mibBuilder.loadTexts:
    ssEvtV2UserMinorAlarm.setStatus(
        "current"
    )

ssEvtV2UserMinorClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 18837, 3, 2, 3, 0, 6)
)
ssEvtV2UserMinorClear.setObjects(
    ("SPECTRACOM-XSYNC-MIB", "ssGpsRefNumSats")
)
if mibBuilder.loadTexts:
    ssEvtV2UserMinorClear.setStatus(
        "current"
    )

ssEvtV2UserMajorAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 18837, 3, 2, 3, 0, 7)
)
ssEvtV2UserMajorAlarm.setObjects(
    ("SPECTRACOM-XSYNC-MIB", "ssGpsRefNumSats")
)
if mibBuilder.loadTexts:
    ssEvtV2UserMajorAlarm.setStatus(
        "current"
    )

ssEvtV2UserMajorClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 18837, 3, 2, 3, 0, 8)
)
ssEvtV2UserMajorClear.setObjects(
    ("SPECTRACOM-XSYNC-MIB", "ssGpsRefNumSats")
)
if mibBuilder.loadTexts:
    ssEvtV2UserMajorClear.setStatus(
        "current"
    )

ssEvtV2GpsAntenna = NotificationType(
    (1, 3, 6, 1, 4, 1, 18837, 3, 2, 3, 0, 9)
)
ssEvtV2GpsAntenna.setObjects(
    ("SPECTRACOM-XSYNC-MIB", "ssGpsRefAntennaState")
)
if mibBuilder.loadTexts:
    ssEvtV2GpsAntenna.setStatus(
        "current"
    )

ssEvtV2MinorAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 18837, 3, 2, 3, 0, 10)
)
ssEvtV2MinorAlarm.setObjects(
    ("SPECTRACOM-XSYNC-MIB", "ssSysStaMinorAlarm")
)
if mibBuilder.loadTexts:
    ssEvtV2MinorAlarm.setStatus(
        "current"
    )

ssEvtV2MajorAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 18837, 3, 2, 3, 0, 11)
)
ssEvtV2MajorAlarm.setObjects(
    ("SPECTRACOM-XSYNC-MIB", "ssSysStaMajorAlarm")
)
if mibBuilder.loadTexts:
    ssEvtV2MajorAlarm.setStatus(
        "current"
    )

ssEvtV2RefChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 18837, 3, 2, 3, 0, 12)
)
ssEvtV2RefChange.setObjects(
      *(("SPECTRACOM-XSYNC-MIB", "ssSysStaTimeReference"),
        ("SPECTRACOM-XSYNC-MIB", "ssSysSta1PPSReference"))
)
if mibBuilder.loadTexts:
    ssEvtV2RefChange.setStatus(
        "current"
    )

ssEvtV21ppsError = NotificationType(
    (1, 3, 6, 1, 4, 1, 18837, 3, 2, 3, 0, 13)
)
ssEvtV21ppsError.setObjects(
      *(("SPECTRACOM-XSYNC-MIB", "ssSysStaTimeReference"),
        ("SPECTRACOM-XSYNC-MIB", "ssSysSta1PPSReference"))
)
if mibBuilder.loadTexts:
    ssEvtV21ppsError.setStatus(
        "current"
    )

ssEvtV21ppsOK = NotificationType(
    (1, 3, 6, 1, 4, 1, 18837, 3, 2, 3, 0, 14)
)
ssEvtV21ppsOK.setObjects(
      *(("SPECTRACOM-XSYNC-MIB", "ssSysStaTimeReference"),
        ("SPECTRACOM-XSYNC-MIB", "ssSysSta1PPSReference"))
)
if mibBuilder.loadTexts:
    ssEvtV21ppsOK.setStatus(
        "current"
    )

ssEvtV2HwError = NotificationType(
    (1, 3, 6, 1, 4, 1, 18837, 3, 2, 3, 0, 15)
)
ssEvtV2HwError.setObjects(
      *(("SPECTRACOM-XSYNC-MIB", "ssSysStaTimeReference"),
        ("SPECTRACOM-XSYNC-MIB", "ssSysSta1PPSReference"))
)
if mibBuilder.loadTexts:
    ssEvtV2HwError.setStatus(
        "current"
    )

ssEvtV2OscillatorAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 18837, 3, 2, 3, 0, 16)
)
ssEvtV2OscillatorAlarm.setObjects(
    ("SPECTRACOM-XSYNC-MIB", "ssSysStaEstFreqError")
)
if mibBuilder.loadTexts:
    ssEvtV2OscillatorAlarm.setStatus(
        "current"
    )

ssEvtV2OscillatorOK = NotificationType(
    (1, 3, 6, 1, 4, 1, 18837, 3, 2, 3, 0, 17)
)
ssEvtV2OscillatorOK.setObjects(
    ("SPECTRACOM-XSYNC-MIB", "ssSysStaEstFreqError")
)
if mibBuilder.loadTexts:
    ssEvtV2OscillatorOK.setStatus(
        "current"
    )

ssEvtV2Reboot = NotificationType(
    (1, 3, 6, 1, 4, 1, 18837, 3, 2, 3, 0, 18)
)
if mibBuilder.loadTexts:
    ssEvtV2Reboot.setStatus(
        "current"
    )

ssEvtV2MaxTempMinorAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 18837, 3, 2, 3, 0, 19)
)
ssEvtV2MaxTempMinorAlarm.setObjects(
    ("SPECTRACOM-XSYNC-MIB", "ssSysStaCpuTemp")
)
if mibBuilder.loadTexts:
    ssEvtV2MaxTempMinorAlarm.setStatus(
        "current"
    )

ssEvtV2MaxTempMinorClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 18837, 3, 2, 3, 0, 20)
)
ssEvtV2MaxTempMinorClear.setObjects(
    ("SPECTRACOM-XSYNC-MIB", "ssSysStaCpuTemp")
)
if mibBuilder.loadTexts:
    ssEvtV2MaxTempMinorClear.setStatus(
        "current"
    )

ssEvtV2MaxTempMajorAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 18837, 3, 2, 3, 0, 21)
)
ssEvtV2MaxTempMajorAlarm.setObjects(
    ("SPECTRACOM-XSYNC-MIB", "ssSysStaCpuTemp")
)
if mibBuilder.loadTexts:
    ssEvtV2MaxTempMajorAlarm.setStatus(
        "current"
    )

ssEvtV2MaxTempMajorClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 18837, 3, 2, 3, 0, 22)
)
ssEvtV2MaxTempMajorClear.setObjects(
    ("SPECTRACOM-XSYNC-MIB", "ssSysStaCpuTemp")
)
if mibBuilder.loadTexts:
    ssEvtV2MaxTempMajorClear.setStatus(
        "current"
    )

ssEvtV2BshMajorAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 18837, 3, 2, 3, 0, 23)
)
ssEvtV2BshMajorAlarm.setObjects(
      *(("SPECTRACOM-XSYNC-MIB", "ssSysStaBshJammingState"),
        ("SPECTRACOM-XSYNC-MIB", "ssSysStaBshSpoofingState"))
)
if mibBuilder.loadTexts:
    ssEvtV2BshMajorAlarm.setStatus(
        "current"
    )

ssEvtV2HSHealth = NotificationType(
    (1, 3, 6, 1, 4, 1, 18837, 3, 2, 3, 0, 24)
)
ssEvtV2HSHealth.setObjects(
      *(("SPECTRACOM-XSYNC-MIB", "ssHotSwapOverallHealth"),
        ("SPECTRACOM-XSYNC-MIB", "ssHotSwapBay1Health"),
        ("SPECTRACOM-XSYNC-MIB", "ssHotSwapBay2Health"))
)
if mibBuilder.loadTexts:
    ssEvtV2HSHealth.setStatus(
        "current"
    )


# Notifications groups

ssTrapsGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 18837, 3, 2, 90, 2, 2)
)
ssTrapsGroup.setObjects(
      *(("SPECTRACOM-XSYNC-MIB", "ssEvtV2TimeSync"),
        ("SPECTRACOM-XSYNC-MIB", "ssEvtV2Holdover"),
        ("SPECTRACOM-XSYNC-MIB", "ssEvtV2FrequencyError"),
        ("SPECTRACOM-XSYNC-MIB", "ssEvtV2FrequencyOK"),
        ("SPECTRACOM-XSYNC-MIB", "ssEvtV2UserMinorAlarm"),
        ("SPECTRACOM-XSYNC-MIB", "ssEvtV2UserMinorClear"),
        ("SPECTRACOM-XSYNC-MIB", "ssEvtV2UserMajorAlarm"),
        ("SPECTRACOM-XSYNC-MIB", "ssEvtV2UserMajorClear"),
        ("SPECTRACOM-XSYNC-MIB", "ssEvtV2GpsAntenna"),
        ("SPECTRACOM-XSYNC-MIB", "ssEvtV2MinorAlarm"),
        ("SPECTRACOM-XSYNC-MIB", "ssEvtV2MajorAlarm"),
        ("SPECTRACOM-XSYNC-MIB", "ssEvtV2RefChange"),
        ("SPECTRACOM-XSYNC-MIB", "ssEvtV21ppsError"),
        ("SPECTRACOM-XSYNC-MIB", "ssEvtV21ppsOK"),
        ("SPECTRACOM-XSYNC-MIB", "ssEvtV2HwError"),
        ("SPECTRACOM-XSYNC-MIB", "ssEvtV2OscillatorAlarm"),
        ("SPECTRACOM-XSYNC-MIB", "ssEvtV2OscillatorOK"),
        ("SPECTRACOM-XSYNC-MIB", "ssEvtV2Reboot"),
        ("SPECTRACOM-XSYNC-MIB", "ssEvtV2MaxTempMinorAlarm"),
        ("SPECTRACOM-XSYNC-MIB", "ssEvtV2MaxTempMinorClear"),
        ("SPECTRACOM-XSYNC-MIB", "ssEvtV2MaxTempMajorAlarm"),
        ("SPECTRACOM-XSYNC-MIB", "ssEvtV2MaxTempMajorClear"),
        ("SPECTRACOM-XSYNC-MIB", "ssEvtV2BshMajorAlarm"),
        ("SPECTRACOM-XSYNC-MIB", "ssEvtV2HSHealth"))
)
if mibBuilder.loadTexts:
    ssTrapsGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

ssCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 18837, 3, 2, 90, 1, 1)
)
ssCompliance.setObjects(
      *(("SPECTRACOM-XSYNC-MIB", "ssObjectsGroup"),
        ("SPECTRACOM-XSYNC-MIB", "ssTrapsGroup"))
)
if mibBuilder.loadTexts:
    ssCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SPECTRACOM-XSYNC-MIB",
    **{"spectracomxSyncMibModule": spectracomxSyncMibModule,
       "specxSyncMIB": specxSyncMIB,
       "specxSyncConfs": specxSyncConfs,
       "specxSyncGroups": specxSyncGroups,
       "specxSyncCompl": specxSyncCompl,
       "specxSyncObjs": specxSyncObjs,
       "ssSystemStatusObjs": ssSystemStatusObjs,
       "ssSysStaPowerDC": ssSysStaPowerDC,
       "ssSysStaTimeReference": ssSysStaTimeReference,
       "ssSysSta1PPSReference": ssSysSta1PPSReference,
       "ssSysStaSyncState": ssSysStaSyncState,
       "ssSysStaHoldoverState": ssSysStaHoldoverState,
       "ssSysStaTfom": ssSysStaTfom,
       "ssSysStaEstPhaseError": ssSysStaEstPhaseError,
       "ssSysStaEstFreqError": ssSysStaEstFreqError,
       "ssSysStaTimeScale": ssSysStaTimeScale,
       "ssSysStaVersion": ssSysStaVersion,
       "ssSysStaTimingVersion": ssSysStaTimingVersion,
       "ssSysStaMinorAlarm": ssSysStaMinorAlarm,
       "ssSysStaMajorAlarm": ssSysStaMajorAlarm,
       "ssSysStaDateTime": ssSysStaDateTime,
       "ssSysStaSerial": ssSysStaSerial,
       "ssSysStaOscTemp": ssSysStaOscTemp,
       "ssSysStaBrdTemp": ssSysStaBrdTemp,
       "ssSysStaCpuTemp": ssSysStaCpuTemp,
       "ssSysStaMinorAlarmCauses": ssSysStaMinorAlarmCauses,
       "ssSysStaMajorAlarmCauses": ssSysStaMajorAlarmCauses,
       "ssSysStaBshJammingState": ssSysStaBshJammingState,
       "ssSysStaBshSpoofingState": ssSysStaBshSpoofingState,
       "ssSysStaDisciplining": ssSysStaDisciplining,
       "ssGpsRefStatusObjs": ssGpsRefStatusObjs,
       "ssGpsRefTable": ssGpsRefTable,
       "ssGpsRefTableEntry": ssGpsRefTableEntry,
       "ssGpsRefRow": ssGpsRefRow,
       "ssGpsRefInstance": ssGpsRefInstance,
       "ssGpsReference": ssGpsReference,
       "ssGpsRefTimeValid": ssGpsRefTimeValid,
       "ssGpsRef1ppsValid": ssGpsRef1ppsValid,
       "ssGpsRefRcvMode": ssGpsRefRcvMode,
       "ssGpsRefDynMode": ssGpsRefDynMode,
       "ssGpsRefNumSats": ssGpsRefNumSats,
       "ssGpsRefPdop": ssGpsRefPdop,
       "ssGpsRefHdop": ssGpsRefHdop,
       "ssGpsRefVdop": ssGpsRefVdop,
       "ssGpsRefTdop": ssGpsRefTdop,
       "ssGpsRefLatitude": ssGpsRefLatitude,
       "ssGpsRefLongitude": ssGpsRefLongitude,
       "ssGpsRefAltitude": ssGpsRefAltitude,
       "ssGpsRefOffset": ssGpsRefOffset,
       "ssGpsRefAntennaState": ssGpsRefAntennaState,
       "ssOptionCardObjs": ssOptionCardObjs,
       "ssReferenceMgmtObjs": ssReferenceMgmtObjs,
       "ssRefMgmtTable": ssRefMgmtTable,
       "ssRefMgmtTableEntry": ssRefMgmtTableEntry,
       "ssRefMgmtRow": ssRefMgmtRow,
       "ssRefMgmtIndex": ssRefMgmtIndex,
       "ssRefMgmtState": ssRefMgmtState,
       "ssRefMgmtPriority": ssRefMgmtPriority,
       "ssRefMgmtTime": ssRefMgmtTime,
       "ssRefMgmt1PPS": ssRefMgmt1PPS,
       "ssRefMgmtTimeValid": ssRefMgmtTimeValid,
       "ssRefMgmt1PPSValid": ssRefMgmt1PPSValid,
       "ssSystemControlObjs": ssSystemControlObjs,
       "ssSysCtrlCommand": ssSysCtrlCommand,
       "ssSysUpdateFile": ssSysUpdateFile,
       "ssSysSetManualTime": ssSysSetManualTime,
       "ssHotSwapObjs": ssHotSwapObjs,
       "ssHotSwapOverallHealth": ssHotSwapOverallHealth,
       "ssHotSwapBay1": ssHotSwapBay1,
       "ssHotSwapBay1Health": ssHotSwapBay1Health,
       "ssHotSwapBay1Type": ssHotSwapBay1Type,
       "ssHotSwapBay1Presence": ssHotSwapBay1Presence,
       "ssHotSwapBay1Voltage": ssHotSwapBay1Voltage,
       "ssHotSwapBay1Current": ssHotSwapBay1Current,
       "ssHotSwapBay1FanEnabled": ssHotSwapBay1FanEnabled,
       "ssHotSwapBay1FanSpeed": ssHotSwapBay1FanSpeed,
       "ssHotSwapBay1Temp": ssHotSwapBay1Temp,
       "ssHotSwapBay1VoltageInRange": ssHotSwapBay1VoltageInRange,
       "ssHotSwapBay1CurrentInRange": ssHotSwapBay1CurrentInRange,
       "ssHotSwapBay1FanSpeedInRange": ssHotSwapBay1FanSpeedInRange,
       "ssHotSwapBay1TempInRange": ssHotSwapBay1TempInRange,
       "ssHotSwapBay2": ssHotSwapBay2,
       "ssHotSwapBay2Health": ssHotSwapBay2Health,
       "ssHotSwapBay2Type": ssHotSwapBay2Type,
       "ssHotSwapBay2Presence": ssHotSwapBay2Presence,
       "ssHotSwapBay2Voltage": ssHotSwapBay2Voltage,
       "ssHotSwapBay2Current": ssHotSwapBay2Current,
       "ssHotSwapBay2FanEnabled": ssHotSwapBay2FanEnabled,
       "ssHotSwapBay2FanSpeed": ssHotSwapBay2FanSpeed,
       "ssHotSwapBay2Temp": ssHotSwapBay2Temp,
       "ssHotSwapBay2VoltageInRange": ssHotSwapBay2VoltageInRange,
       "ssHotSwapBay2CurrentInRange": ssHotSwapBay2CurrentInRange,
       "ssHotSwapBay2FanSpeedInRange": ssHotSwapBay2FanSpeedInRange,
       "ssHotSwapBay2TempInRange": ssHotSwapBay2TempInRange,
       "specxSyncEvents": specxSyncEvents,
       "ssEventsV2": ssEventsV2,
       "ssEvtV2TimeSync": ssEvtV2TimeSync,
       "ssEvtV2Holdover": ssEvtV2Holdover,
       "ssEvtV2FrequencyError": ssEvtV2FrequencyError,
       "ssEvtV2FrequencyOK": ssEvtV2FrequencyOK,
       "ssEvtV2UserMinorAlarm": ssEvtV2UserMinorAlarm,
       "ssEvtV2UserMinorClear": ssEvtV2UserMinorClear,
       "ssEvtV2UserMajorAlarm": ssEvtV2UserMajorAlarm,
       "ssEvtV2UserMajorClear": ssEvtV2UserMajorClear,
       "ssEvtV2GpsAntenna": ssEvtV2GpsAntenna,
       "ssEvtV2MinorAlarm": ssEvtV2MinorAlarm,
       "ssEvtV2MajorAlarm": ssEvtV2MajorAlarm,
       "ssEvtV2RefChange": ssEvtV2RefChange,
       "ssEvtV21ppsError": ssEvtV21ppsError,
       "ssEvtV21ppsOK": ssEvtV21ppsOK,
       "ssEvtV2HwError": ssEvtV2HwError,
       "ssEvtV2OscillatorAlarm": ssEvtV2OscillatorAlarm,
       "ssEvtV2OscillatorOK": ssEvtV2OscillatorOK,
       "ssEvtV2Reboot": ssEvtV2Reboot,
       "ssEvtV2MaxTempMinorAlarm": ssEvtV2MaxTempMinorAlarm,
       "ssEvtV2MaxTempMinorClear": ssEvtV2MaxTempMinorClear,
       "ssEvtV2MaxTempMajorAlarm": ssEvtV2MaxTempMajorAlarm,
       "ssEvtV2MaxTempMajorClear": ssEvtV2MaxTempMajorClear,
       "ssEvtV2BshMajorAlarm": ssEvtV2BshMajorAlarm,
       "ssEvtV2HSHealth": ssEvtV2HSHealth,
       "ssConformance": ssConformance,
       "ssCompliances": ssCompliances,
       "ssCompliance": ssCompliance,
       "ssGroups": ssGroups,
       "ssObjectsGroup": ssObjectsGroup,
       "ssTrapsGroup": ssTrapsGroup}
)
