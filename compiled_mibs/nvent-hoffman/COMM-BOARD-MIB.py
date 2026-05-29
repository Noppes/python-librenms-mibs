# SNMP MIB module (COMM-BOARD-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\nvent-hoffman\COMM-BOARD-MIB

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



class DisplayString(OctetString):
    """Custom type DisplayString based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )





class TruthValue(Integer32):
    """Custom type TruthValue based on Integer32"""
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




# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_PentairTechProd_ObjectIdentity = ObjectIdentity
pentairTechProd = _PentairTechProd_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 26609)
)
_CarelBoardMIB_ObjectIdentity = ObjectIdentity
carelBoardMIB = _CarelBoardMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 26609, 2)
)
_MenuInfo_ObjectIdentity = ObjectIdentity
menuInfo = _MenuInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 26609, 2, 1)
)
_CoolSetPoint_ObjectIdentity = ObjectIdentity
coolSetPoint = _CoolSetPoint_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 26609, 2, 1, 1)
)
_CspName_Type = DisplayString
_CspName_Object = MibScalar
cspName = _CspName_Object(
    (1, 3, 6, 1, 4, 1, 26609, 2, 1, 1, 1),
    _CspName_Type()
)
cspName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cspName.setStatus("mandatory")
_CspValue_Type = Integer32
_CspValue_Object = MibScalar
cspValue = _CspValue_Object(
    (1, 3, 6, 1, 4, 1, 26609, 2, 1, 1, 2),
    _CspValue_Type()
)
cspValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cspValue.setStatus("mandatory")
_CoolSetPointMin_ObjectIdentity = ObjectIdentity
coolSetPointMin = _CoolSetPointMin_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 26609, 2, 1, 2)
)
_CsplName_Type = DisplayString
_CsplName_Object = MibScalar
csplName = _CsplName_Object(
    (1, 3, 6, 1, 4, 1, 26609, 2, 1, 2, 1),
    _CsplName_Type()
)
csplName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csplName.setStatus("mandatory")
_CsplValue_Type = Integer32
_CsplValue_Object = MibScalar
csplValue = _CsplValue_Object(
    (1, 3, 6, 1, 4, 1, 26609, 2, 1, 2, 2),
    _CsplValue_Type()
)
csplValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csplValue.setStatus("mandatory")
_CoolSetPointMax_ObjectIdentity = ObjectIdentity
coolSetPointMax = _CoolSetPointMax_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 26609, 2, 1, 3)
)
_CsphName_Type = DisplayString
_CsphName_Object = MibScalar
csphName = _CsphName_Object(
    (1, 3, 6, 1, 4, 1, 26609, 2, 1, 3, 1),
    _CsphName_Type()
)
csphName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csphName.setStatus("mandatory")
_CsphValue_Type = Integer32
_CsphValue_Object = MibScalar
csphValue = _CsphValue_Object(
    (1, 3, 6, 1, 4, 1, 26609, 2, 1, 3, 2),
    _CsphValue_Type()
)
csphValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csphValue.setStatus("mandatory")
_CoolDifferential_ObjectIdentity = ObjectIdentity
coolDifferential = _CoolDifferential_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 26609, 2, 1, 4)
)
_CdName_Type = DisplayString
_CdName_Object = MibScalar
cdName = _CdName_Object(
    (1, 3, 6, 1, 4, 1, 26609, 2, 1, 4, 1),
    _CdName_Type()
)
cdName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdName.setStatus("mandatory")
_CdValue_Type = Integer32
_CdValue_Object = MibScalar
cdValue = _CdValue_Object(
    (1, 3, 6, 1, 4, 1, 26609, 2, 1, 4, 2),
    _CdValue_Type()
)
cdValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdValue.setStatus("mandatory")
_HeatSetPoint_ObjectIdentity = ObjectIdentity
heatSetPoint = _HeatSetPoint_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 26609, 2, 1, 5)
)
_HspName_Type = DisplayString
_HspName_Object = MibScalar
hspName = _HspName_Object(
    (1, 3, 6, 1, 4, 1, 26609, 2, 1, 5, 1),
    _HspName_Type()
)
hspName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hspName.setStatus("mandatory")
_HspValue_Type = Integer32
_HspValue_Object = MibScalar
hspValue = _HspValue_Object(
    (1, 3, 6, 1, 4, 1, 26609, 2, 1, 5, 2),
    _HspValue_Type()
)
hspValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hspValue.setStatus("mandatory")
_HeatSetPointMin_ObjectIdentity = ObjectIdentity
heatSetPointMin = _HeatSetPointMin_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 26609, 2, 1, 6)
)
_HsplName_Type = DisplayString
_HsplName_Object = MibScalar
hsplName = _HsplName_Object(
    (1, 3, 6, 1, 4, 1, 26609, 2, 1, 6, 1),
    _HsplName_Type()
)
hsplName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hsplName.setStatus("mandatory")
_HsplValue_Type = Integer32
_HsplValue_Object = MibScalar
hsplValue = _HsplValue_Object(
    (1, 3, 6, 1, 4, 1, 26609, 2, 1, 6, 2),
    _HsplValue_Type()
)
hsplValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hsplValue.setStatus("mandatory")
_HeatSetPointMax_ObjectIdentity = ObjectIdentity
heatSetPointMax = _HeatSetPointMax_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 26609, 2, 1, 7)
)
_HsphName_Type = DisplayString
_HsphName_Object = MibScalar
hsphName = _HsphName_Object(
    (1, 3, 6, 1, 4, 1, 26609, 2, 1, 7, 1),
    _HsphName_Type()
)
hsphName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hsphName.setStatus("mandatory")
_HsphValue_Type = Integer32
_HsphValue_Object = MibScalar
hsphValue = _HsphValue_Object(
    (1, 3, 6, 1, 4, 1, 26609, 2, 1, 7, 2),
    _HsphValue_Type()
)
hsphValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hsphValue.setStatus("mandatory")
_HeatDifferential_ObjectIdentity = ObjectIdentity
heatDifferential = _HeatDifferential_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 26609, 2, 1, 8)
)
_HdName_Type = DisplayString
_HdName_Object = MibScalar
hdName = _HdName_Object(
    (1, 3, 6, 1, 4, 1, 26609, 2, 1, 8, 1),
    _HdName_Type()
)
hdName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hdName.setStatus("mandatory")
_HdValue_Type = Integer32
_HdValue_Object = MibScalar
hdValue = _HdValue_Object(
    (1, 3, 6, 1, 4, 1, 26609, 2, 1, 8, 2),
    _HdValue_Type()
)
hdValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hdValue.setStatus("mandatory")
_UnitOfMeasure_ObjectIdentity = ObjectIdentity
unitOfMeasure = _UnitOfMeasure_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 26609, 2, 1, 9)
)
_UmName_Type = DisplayString
_UmName_Object = MibScalar
umName = _UmName_Object(
    (1, 3, 6, 1, 4, 1, 26609, 2, 1, 9, 1),
    _UmName_Type()
)
umName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    umName.setStatus("mandatory")
_UmValue_Type = Integer32
_UmValue_Object = MibScalar
umValue = _UmValue_Object(
    (1, 3, 6, 1, 4, 1, 26609, 2, 1, 9, 2),
    _UmValue_Type()
)
umValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    umValue.setStatus("mandatory")
_HighTempSetP_Type = Integer32
_HighTempSetP_Object = MibScalar
highTempSetP = _HighTempSetP_Object(
    (1, 3, 6, 1, 4, 1, 26609, 2, 1, 10),
    _HighTempSetP_Type()
)
highTempSetP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    highTempSetP.setStatus("mandatory")
_LowTempSetP_Type = Integer32
_LowTempSetP_Object = MibScalar
lowTempSetP = _LowTempSetP_Object(
    (1, 3, 6, 1, 4, 1, 26609, 2, 1, 11),
    _LowTempSetP_Type()
)
lowTempSetP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lowTempSetP.setStatus("mandatory")
_FaultInfo_ObjectIdentity = ObjectIdentity
faultInfo = _FaultInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 26609, 2, 2)
)
_FrostAlarm_ObjectIdentity = ObjectIdentity
frostAlarm = _FrostAlarm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 26609, 2, 2, 1)
)
_FaName_Type = DisplayString
_FaName_Object = MibScalar
faName = _FaName_Object(
    (1, 3, 6, 1, 4, 1, 26609, 2, 2, 1, 1),
    _FaName_Type()
)
faName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    faName.setStatus("mandatory")
_FaEnable_Type = TruthValue
_FaEnable_Object = MibScalar
faEnable = _FaEnable_Object(
    (1, 3, 6, 1, 4, 1, 26609, 2, 2, 1, 2),
    _FaEnable_Type()
)
faEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    faEnable.setStatus("mandatory")
_FaState_Type = TruthValue
_FaState_Object = MibScalar
faState = _FaState_Object(
    (1, 3, 6, 1, 4, 1, 26609, 2, 2, 1, 3),
    _FaState_Type()
)
faState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    faState.setStatus("mandatory")
_HighTempAlarm_ObjectIdentity = ObjectIdentity
highTempAlarm = _HighTempAlarm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 26609, 2, 2, 4)
)
_HtaName_Type = DisplayString
_HtaName_Object = MibScalar
htaName = _HtaName_Object(
    (1, 3, 6, 1, 4, 1, 26609, 2, 2, 4, 1),
    _HtaName_Type()
)
htaName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    htaName.setStatus("mandatory")
_HtaEnable_Type = TruthValue
_HtaEnable_Object = MibScalar
htaEnable = _HtaEnable_Object(
    (1, 3, 6, 1, 4, 1, 26609, 2, 2, 4, 2),
    _HtaEnable_Type()
)
htaEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    htaEnable.setStatus("mandatory")
_HtaState_Type = TruthValue
_HtaState_Object = MibScalar
htaState = _HtaState_Object(
    (1, 3, 6, 1, 4, 1, 26609, 2, 2, 4, 3),
    _HtaState_Type()
)
htaState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    htaState.setStatus("mandatory")
_LowTempAlarm_ObjectIdentity = ObjectIdentity
lowTempAlarm = _LowTempAlarm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 26609, 2, 2, 5)
)
_LtaName_Type = DisplayString
_LtaName_Object = MibScalar
ltaName = _LtaName_Object(
    (1, 3, 6, 1, 4, 1, 26609, 2, 2, 5, 1),
    _LtaName_Type()
)
ltaName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ltaName.setStatus("mandatory")
_LtaEnable_Type = TruthValue
_LtaEnable_Object = MibScalar
ltaEnable = _LtaEnable_Object(
    (1, 3, 6, 1, 4, 1, 26609, 2, 2, 5, 2),
    _LtaEnable_Type()
)
ltaEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ltaEnable.setStatus("mandatory")
_LtaState_Type = TruthValue
_LtaState_Object = MibScalar
ltaState = _LtaState_Object(
    (1, 3, 6, 1, 4, 1, 26609, 2, 2, 5, 3),
    _LtaState_Type()
)
ltaState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ltaState.setStatus("mandatory")
_InletFailAlarm_ObjectIdentity = ObjectIdentity
inletFailAlarm = _InletFailAlarm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 26609, 2, 2, 6)
)
_IsfaName_Type = DisplayString
_IsfaName_Object = MibScalar
isfaName = _IsfaName_Object(
    (1, 3, 6, 1, 4, 1, 26609, 2, 2, 6, 1),
    _IsfaName_Type()
)
isfaName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isfaName.setStatus("mandatory")
_IsfaEnable_Type = TruthValue
_IsfaEnable_Object = MibScalar
isfaEnable = _IsfaEnable_Object(
    (1, 3, 6, 1, 4, 1, 26609, 2, 2, 6, 2),
    _IsfaEnable_Type()
)
isfaEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    isfaEnable.setStatus("mandatory")
_IsfaState_Type = TruthValue
_IsfaState_Object = MibScalar
isfaState = _IsfaState_Object(
    (1, 3, 6, 1, 4, 1, 26609, 2, 2, 6, 3),
    _IsfaState_Type()
)
isfaState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isfaState.setStatus("mandatory")
_OutletFailAlarm_ObjectIdentity = ObjectIdentity
outletFailAlarm = _OutletFailAlarm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 26609, 2, 2, 7)
)
_OsfaName_Type = DisplayString
_OsfaName_Object = MibScalar
osfaName = _OsfaName_Object(
    (1, 3, 6, 1, 4, 1, 26609, 2, 2, 7, 1),
    _OsfaName_Type()
)
osfaName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osfaName.setStatus("mandatory")
_OsfaEnable_Type = TruthValue
_OsfaEnable_Object = MibScalar
osfaEnable = _OsfaEnable_Object(
    (1, 3, 6, 1, 4, 1, 26609, 2, 2, 7, 2),
    _OsfaEnable_Type()
)
osfaEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    osfaEnable.setStatus("mandatory")
_OsfaState_Type = TruthValue
_OsfaState_Object = MibScalar
osfaState = _OsfaState_Object(
    (1, 3, 6, 1, 4, 1, 26609, 2, 2, 7, 3),
    _OsfaState_Type()
)
osfaState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osfaState.setStatus("mandatory")
_DoorSmokeAlarm_ObjectIdentity = ObjectIdentity
doorSmokeAlarm = _DoorSmokeAlarm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 26609, 2, 2, 8)
)
_DsaName_Type = DisplayString
_DsaName_Object = MibScalar
dsaName = _DsaName_Object(
    (1, 3, 6, 1, 4, 1, 26609, 2, 2, 8, 1),
    _DsaName_Type()
)
dsaName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsaName.setStatus("mandatory")
_DsaEnable_Type = TruthValue
_DsaEnable_Object = MibScalar
dsaEnable = _DsaEnable_Object(
    (1, 3, 6, 1, 4, 1, 26609, 2, 2, 8, 2),
    _DsaEnable_Type()
)
dsaEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsaEnable.setStatus("mandatory")
_DsaState_Type = TruthValue
_DsaState_Object = MibScalar
dsaState = _DsaState_Object(
    (1, 3, 6, 1, 4, 1, 26609, 2, 2, 8, 3),
    _DsaState_Type()
)
dsaState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsaState.setStatus("mandatory")
_HighPressureAlarm_ObjectIdentity = ObjectIdentity
highPressureAlarm = _HighPressureAlarm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 26609, 2, 2, 9)
)
_HpaName_Type = DisplayString
_HpaName_Object = MibScalar
hpaName = _HpaName_Object(
    (1, 3, 6, 1, 4, 1, 26609, 2, 2, 9, 1),
    _HpaName_Type()
)
hpaName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpaName.setStatus("mandatory")
_HpaEnable_Type = TruthValue
_HpaEnable_Object = MibScalar
hpaEnable = _HpaEnable_Object(
    (1, 3, 6, 1, 4, 1, 26609, 2, 2, 9, 2),
    _HpaEnable_Type()
)
hpaEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpaEnable.setStatus("mandatory")
_HpaState_Type = TruthValue
_HpaState_Object = MibScalar
hpaState = _HpaState_Object(
    (1, 3, 6, 1, 4, 1, 26609, 2, 2, 9, 3),
    _HpaState_Type()
)
hpaState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpaState.setStatus("mandatory")
_ContCommFailAlarm_ObjectIdentity = ObjectIdentity
contCommFailAlarm = _ContCommFailAlarm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 26609, 2, 2, 10)
)
_CcfaName_Type = DisplayString
_CcfaName_Object = MibScalar
ccfaName = _CcfaName_Object(
    (1, 3, 6, 1, 4, 1, 26609, 2, 2, 10, 1),
    _CcfaName_Type()
)
ccfaName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccfaName.setStatus("mandatory")
_CcfaEnable_Type = TruthValue
_CcfaEnable_Object = MibScalar
ccfaEnable = _CcfaEnable_Object(
    (1, 3, 6, 1, 4, 1, 26609, 2, 2, 10, 2),
    _CcfaEnable_Type()
)
ccfaEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccfaEnable.setStatus("mandatory")
_CcfaState_Type = TruthValue
_CcfaState_Object = MibScalar
ccfaState = _CcfaState_Object(
    (1, 3, 6, 1, 4, 1, 26609, 2, 2, 10, 3),
    _CcfaState_Type()
)
ccfaState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccfaState.setStatus("mandatory")
_FaultLog_ObjectIdentity = ObjectIdentity
faultLog = _FaultLog_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 26609, 2, 3)
)
_Log1Value_Type = Integer32
_Log1Value_Object = MibScalar
log1Value = _Log1Value_Object(
    (1, 3, 6, 1, 4, 1, 26609, 2, 3, 1),
    _Log1Value_Type()
)
log1Value.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    log1Value.setStatus("mandatory")
_Log2Value_Type = Integer32
_Log2Value_Object = MibScalar
log2Value = _Log2Value_Object(
    (1, 3, 6, 1, 4, 1, 26609, 2, 3, 2),
    _Log2Value_Type()
)
log2Value.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    log2Value.setStatus("mandatory")
_Log3Value_Type = Integer32
_Log3Value_Object = MibScalar
log3Value = _Log3Value_Object(
    (1, 3, 6, 1, 4, 1, 26609, 2, 3, 3),
    _Log3Value_Type()
)
log3Value.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    log3Value.setStatus("mandatory")
_Log4Value_Type = Integer32
_Log4Value_Object = MibScalar
log4Value = _Log4Value_Object(
    (1, 3, 6, 1, 4, 1, 26609, 2, 3, 4),
    _Log4Value_Type()
)
log4Value.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    log4Value.setStatus("mandatory")
_Log5Value_Type = Integer32
_Log5Value_Object = MibScalar
log5Value = _Log5Value_Object(
    (1, 3, 6, 1, 4, 1, 26609, 2, 3, 5),
    _Log5Value_Type()
)
log5Value.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    log5Value.setStatus("mandatory")
_Log6Value_Type = Integer32
_Log6Value_Object = MibScalar
log6Value = _Log6Value_Object(
    (1, 3, 6, 1, 4, 1, 26609, 2, 3, 6),
    _Log6Value_Type()
)
log6Value.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    log6Value.setStatus("mandatory")
_Log7Value_Type = Integer32
_Log7Value_Object = MibScalar
log7Value = _Log7Value_Object(
    (1, 3, 6, 1, 4, 1, 26609, 2, 3, 7),
    _Log7Value_Type()
)
log7Value.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    log7Value.setStatus("mandatory")
_Log8Value_Type = Integer32
_Log8Value_Object = MibScalar
log8Value = _Log8Value_Object(
    (1, 3, 6, 1, 4, 1, 26609, 2, 3, 8),
    _Log8Value_Type()
)
log8Value.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    log8Value.setStatus("mandatory")
_Log9Value_Type = Integer32
_Log9Value_Object = MibScalar
log9Value = _Log9Value_Object(
    (1, 3, 6, 1, 4, 1, 26609, 2, 3, 9),
    _Log9Value_Type()
)
log9Value.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    log9Value.setStatus("mandatory")
_Log10Value_Type = Integer32
_Log10Value_Object = MibScalar
log10Value = _Log10Value_Object(
    (1, 3, 6, 1, 4, 1, 26609, 2, 3, 10),
    _Log10Value_Type()
)
log10Value.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    log10Value.setStatus("mandatory")
_Log11Value_Type = Integer32
_Log11Value_Object = MibScalar
log11Value = _Log11Value_Object(
    (1, 3, 6, 1, 4, 1, 26609, 2, 3, 11),
    _Log11Value_Type()
)
log11Value.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    log11Value.setStatus("mandatory")
_Log12Value_Type = Integer32
_Log12Value_Object = MibScalar
log12Value = _Log12Value_Object(
    (1, 3, 6, 1, 4, 1, 26609, 2, 3, 12),
    _Log12Value_Type()
)
log12Value.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    log12Value.setStatus("mandatory")
_Log13Value_Type = Integer32
_Log13Value_Object = MibScalar
log13Value = _Log13Value_Object(
    (1, 3, 6, 1, 4, 1, 26609, 2, 3, 13),
    _Log13Value_Type()
)
log13Value.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    log13Value.setStatus("mandatory")
_Log14Value_Type = Integer32
_Log14Value_Object = MibScalar
log14Value = _Log14Value_Object(
    (1, 3, 6, 1, 4, 1, 26609, 2, 3, 14),
    _Log14Value_Type()
)
log14Value.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    log14Value.setStatus("mandatory")
_Log15Value_Type = Integer32
_Log15Value_Object = MibScalar
log15Value = _Log15Value_Object(
    (1, 3, 6, 1, 4, 1, 26609, 2, 3, 15),
    _Log15Value_Type()
)
log15Value.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    log15Value.setStatus("mandatory")
_Log16Value_Type = Integer32
_Log16Value_Object = MibScalar
log16Value = _Log16Value_Object(
    (1, 3, 6, 1, 4, 1, 26609, 2, 3, 16),
    _Log16Value_Type()
)
log16Value.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    log16Value.setStatus("mandatory")
_Log17Value_Type = Integer32
_Log17Value_Object = MibScalar
log17Value = _Log17Value_Object(
    (1, 3, 6, 1, 4, 1, 26609, 2, 3, 17),
    _Log17Value_Type()
)
log17Value.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    log17Value.setStatus("mandatory")
_Log18Value_Type = Integer32
_Log18Value_Object = MibScalar
log18Value = _Log18Value_Object(
    (1, 3, 6, 1, 4, 1, 26609, 2, 3, 18),
    _Log18Value_Type()
)
log18Value.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    log18Value.setStatus("mandatory")
_Log19Value_Type = Integer32
_Log19Value_Object = MibScalar
log19Value = _Log19Value_Object(
    (1, 3, 6, 1, 4, 1, 26609, 2, 3, 19),
    _Log19Value_Type()
)
log19Value.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    log19Value.setStatus("mandatory")
_Log20Value_Type = Integer32
_Log20Value_Object = MibScalar
log20Value = _Log20Value_Object(
    (1, 3, 6, 1, 4, 1, 26609, 2, 3, 20),
    _Log20Value_Type()
)
log20Value.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    log20Value.setStatus("mandatory")
_Log21Value_Type = Integer32
_Log21Value_Object = MibScalar
log21Value = _Log21Value_Object(
    (1, 3, 6, 1, 4, 1, 26609, 2, 3, 21),
    _Log21Value_Type()
)
log21Value.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    log21Value.setStatus("mandatory")
_Log22Value_Type = Integer32
_Log22Value_Object = MibScalar
log22Value = _Log22Value_Object(
    (1, 3, 6, 1, 4, 1, 26609, 2, 3, 22),
    _Log22Value_Type()
)
log22Value.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    log22Value.setStatus("mandatory")
_Log23Value_Type = Integer32
_Log23Value_Object = MibScalar
log23Value = _Log23Value_Object(
    (1, 3, 6, 1, 4, 1, 26609, 2, 3, 23),
    _Log23Value_Type()
)
log23Value.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    log23Value.setStatus("mandatory")
_Log24Value_Type = Integer32
_Log24Value_Object = MibScalar
log24Value = _Log24Value_Object(
    (1, 3, 6, 1, 4, 1, 26609, 2, 3, 24),
    _Log24Value_Type()
)
log24Value.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    log24Value.setStatus("mandatory")
_Log25Value_Type = Integer32
_Log25Value_Object = MibScalar
log25Value = _Log25Value_Object(
    (1, 3, 6, 1, 4, 1, 26609, 2, 3, 25),
    _Log25Value_Type()
)
log25Value.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    log25Value.setStatus("mandatory")
_DataLog_ObjectIdentity = ObjectIdentity
dataLog = _DataLog_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 26609, 2, 4)
)
_InletSensor_ObjectIdentity = ObjectIdentity
inletSensor = _InletSensor_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 26609, 2, 4, 1)
)
_P1iName_Type = DisplayString
_P1iName_Object = MibScalar
p1iName = _P1iName_Object(
    (1, 3, 6, 1, 4, 1, 26609, 2, 4, 1, 1),
    _P1iName_Type()
)
p1iName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    p1iName.setStatus("mandatory")
_P1iValue_Type = Integer32
_P1iValue_Object = MibScalar
p1iValue = _P1iValue_Object(
    (1, 3, 6, 1, 4, 1, 26609, 2, 4, 1, 2),
    _P1iValue_Type()
)
p1iValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    p1iValue.setStatus("mandatory")
_OutletSensor_ObjectIdentity = ObjectIdentity
outletSensor = _OutletSensor_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 26609, 2, 4, 2)
)
_P2iName_Type = DisplayString
_P2iName_Object = MibScalar
p2iName = _P2iName_Object(
    (1, 3, 6, 1, 4, 1, 26609, 2, 4, 2, 1),
    _P2iName_Type()
)
p2iName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    p2iName.setStatus("mandatory")
_P2iValue_Type = Integer32
_P2iValue_Object = MibScalar
p2iValue = _P2iValue_Object(
    (1, 3, 6, 1, 4, 1, 26609, 2, 4, 2, 2),
    _P2iValue_Type()
)
p2iValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    p2iValue.setStatus("mandatory")
_CbNotification_ObjectIdentity = ObjectIdentity
cbNotification = _CbNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 26609, 2, 5)
)
_TrapFreq_ObjectIdentity = ObjectIdentity
trapFreq = _TrapFreq_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 26609, 2, 5, 1)
)


class _TrapRate_Type(Integer32):
    """Custom type trapRate based on Integer32"""
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
          ("once", 2),
          ("interval", 3))
    )


_TrapRate_Type.__name__ = "Integer32"
_TrapRate_Object = MibScalar
trapRate = _TrapRate_Object(
    (1, 3, 6, 1, 4, 1, 26609, 2, 5, 1, 1),
    _TrapRate_Type()
)
trapRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trapRate.setStatus("mandatory")


class _TrapInterval_Type(Integer32):
    """Custom type trapInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 180),
    )


_TrapInterval_Type.__name__ = "Integer32"
_TrapInterval_Object = MibScalar
trapInterval = _TrapInterval_Object(
    (1, 3, 6, 1, 4, 1, 26609, 2, 5, 1, 2),
    _TrapInterval_Type()
)
trapInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trapInterval.setStatus("mandatory")
_TrapList_ObjectIdentity = ObjectIdentity
trapList = _TrapList_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 26609, 2, 5, 2)
)
_FrostTrap_Type = DisplayString
_FrostTrap_Object = MibScalar
frostTrap = _FrostTrap_Object(
    (1, 3, 6, 1, 4, 1, 26609, 2, 5, 2, 1),
    _FrostTrap_Type()
)
frostTrap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frostTrap.setStatus("mandatory")
_StartUpHiTempTrap_Type = DisplayString
_StartUpHiTempTrap_Object = MibScalar
startUpHiTempTrap = _StartUpHiTempTrap_Object(
    (1, 3, 6, 1, 4, 1, 26609, 2, 5, 2, 2),
    _StartUpHiTempTrap_Type()
)
startUpHiTempTrap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    startUpHiTempTrap.setStatus("mandatory")
_StartUpLowTempTrap_Type = DisplayString
_StartUpLowTempTrap_Object = MibScalar
startUpLowTempTrap = _StartUpLowTempTrap_Object(
    (1, 3, 6, 1, 4, 1, 26609, 2, 5, 2, 3),
    _StartUpLowTempTrap_Type()
)
startUpLowTempTrap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    startUpLowTempTrap.setStatus("mandatory")
_HighTempTrap_Type = DisplayString
_HighTempTrap_Object = MibScalar
highTempTrap = _HighTempTrap_Object(
    (1, 3, 6, 1, 4, 1, 26609, 2, 5, 2, 4),
    _HighTempTrap_Type()
)
highTempTrap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    highTempTrap.setStatus("mandatory")
_LowTempTrap_Type = DisplayString
_LowTempTrap_Object = MibScalar
lowTempTrap = _LowTempTrap_Object(
    (1, 3, 6, 1, 4, 1, 26609, 2, 5, 2, 5),
    _LowTempTrap_Type()
)
lowTempTrap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lowTempTrap.setStatus("mandatory")
_InletSensFailTrap_Type = DisplayString
_InletSensFailTrap_Object = MibScalar
inletSensFailTrap = _InletSensFailTrap_Object(
    (1, 3, 6, 1, 4, 1, 26609, 2, 5, 2, 6),
    _InletSensFailTrap_Type()
)
inletSensFailTrap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inletSensFailTrap.setStatus("mandatory")
_OutletSensFailTrap_Type = DisplayString
_OutletSensFailTrap_Object = MibScalar
outletSensFailTrap = _OutletSensFailTrap_Object(
    (1, 3, 6, 1, 4, 1, 26609, 2, 5, 2, 7),
    _OutletSensFailTrap_Type()
)
outletSensFailTrap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outletSensFailTrap.setStatus("mandatory")
_DoorSmokeTrap_Type = DisplayString
_DoorSmokeTrap_Object = MibScalar
doorSmokeTrap = _DoorSmokeTrap_Object(
    (1, 3, 6, 1, 4, 1, 26609, 2, 5, 2, 8),
    _DoorSmokeTrap_Type()
)
doorSmokeTrap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    doorSmokeTrap.setStatus("mandatory")
_HighPressureTrap_Type = DisplayString
_HighPressureTrap_Object = MibScalar
highPressureTrap = _HighPressureTrap_Object(
    (1, 3, 6, 1, 4, 1, 26609, 2, 5, 2, 9),
    _HighPressureTrap_Type()
)
highPressureTrap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    highPressureTrap.setStatus("mandatory")
_ContcommfailTrap_Type = DisplayString
_ContcommfailTrap_Object = MibScalar
contcommfailTrap = _ContcommfailTrap_Object(
    (1, 3, 6, 1, 4, 1, 26609, 2, 5, 2, 10),
    _ContcommfailTrap_Type()
)
contcommfailTrap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    contcommfailTrap.setStatus("mandatory")
_AddressInfo_ObjectIdentity = ObjectIdentity
addressInfo = _AddressInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 26609, 2, 20)
)
_DeviceIP_Type = IpAddress
_DeviceIP_Object = MibScalar
deviceIP = _DeviceIP_Object(
    (1, 3, 6, 1, 4, 1, 26609, 2, 20, 1),
    _DeviceIP_Type()
)
deviceIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    deviceIP.setStatus("mandatory")
_GatewayIP_Type = IpAddress
_GatewayIP_Object = MibScalar
gatewayIP = _GatewayIP_Object(
    (1, 3, 6, 1, 4, 1, 26609, 2, 20, 2),
    _GatewayIP_Type()
)
gatewayIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gatewayIP.setStatus("mandatory")
_SubnetMask_Type = IpAddress
_SubnetMask_Object = MibScalar
subnetMask = _SubnetMask_Object(
    (1, 3, 6, 1, 4, 1, 26609, 2, 20, 3),
    _SubnetMask_Type()
)
subnetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    subnetMask.setStatus("mandatory")
_TrapIP_Type = IpAddress
_TrapIP_Object = MibScalar
trapIP = _TrapIP_Object(
    (1, 3, 6, 1, 4, 1, 26609, 2, 20, 4),
    _TrapIP_Type()
)
trapIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trapIP.setStatus("mandatory")
_DhcpServer_Type = TruthValue
_DhcpServer_Object = MibScalar
dhcpServer = _DhcpServer_Object(
    (1, 3, 6, 1, 4, 1, 26609, 2, 20, 5),
    _DhcpServer_Type()
)
dhcpServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpServer.setStatus("mandatory")
_SnmpComm_Type = DisplayString
_SnmpComm_Object = MibScalar
snmpComm = _SnmpComm_Object(
    (1, 3, 6, 1, 4, 1, 26609, 2, 20, 6),
    _SnmpComm_Type()
)
snmpComm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpComm.setStatus("mandatory")
_RevisionIDInfo_ObjectIdentity = ObjectIdentity
revisionIDInfo = _RevisionIDInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 26609, 2, 21)
)
_Identification_Type = DisplayString
_Identification_Object = MibScalar
identification = _Identification_Object(
    (1, 3, 6, 1, 4, 1, 26609, 2, 21, 1),
    _Identification_Type()
)
identification.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    identification.setStatus("mandatory")
_CommRev_Type = DisplayString
_CommRev_Object = MibScalar
commRev = _CommRev_Object(
    (1, 3, 6, 1, 4, 1, 26609, 2, 21, 2),
    _CommRev_Type()
)
commRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    commRev.setStatus("mandatory")


class _ControlRev_Type(Integer32):
    """Custom type controlRev based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 999),
    )


_ControlRev_Type.__name__ = "Integer32"
_ControlRev_Object = MibScalar
controlRev = _ControlRev_Object(
    (1, 3, 6, 1, 4, 1, 26609, 2, 21, 3),
    _ControlRev_Type()
)
controlRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    controlRev.setStatus("mandatory")
_CommSerialNum_Type = DisplayString
_CommSerialNum_Object = MibScalar
commSerialNum = _CommSerialNum_Object(
    (1, 3, 6, 1, 4, 1, 26609, 2, 21, 4),
    _CommSerialNum_Type()
)
commSerialNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    commSerialNum.setStatus("mandatory")
_UnitSerialNum_Type = DisplayString
_UnitSerialNum_Object = MibScalar
unitSerialNum = _UnitSerialNum_Object(
    (1, 3, 6, 1, 4, 1, 26609, 2, 21, 5),
    _UnitSerialNum_Type()
)
unitSerialNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    unitSerialNum.setStatus("mandatory")
_UnitModelNum_Type = DisplayString
_UnitModelNum_Object = MibScalar
unitModelNum = _UnitModelNum_Object(
    (1, 3, 6, 1, 4, 1, 26609, 2, 21, 6),
    _UnitModelNum_Type()
)
unitModelNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    unitModelNum.setStatus("mandatory")
_StationName_Type = DisplayString
_StationName_Object = MibScalar
stationName = _StationName_Object(
    (1, 3, 6, 1, 4, 1, 26609, 2, 21, 7),
    _StationName_Type()
)
stationName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    stationName.setStatus("mandatory")

# Managed Objects groups


# Notification objects

frostAlarmEV = NotificationType(
    (1, 3, 6, 1, 4, 1, 26609, 2, 5, 2, 0, 51)
)
frostAlarmEV.setObjects(
    ("COMM-BOARD-MIB", "frostTrap")
)
if mibBuilder.loadTexts:
    frostAlarmEV.setStatus(
        ""
    )

startUpHiTempEV = NotificationType(
    (1, 3, 6, 1, 4, 1, 26609, 2, 5, 2, 0, 52)
)
startUpHiTempEV.setObjects(
    ("COMM-BOARD-MIB", "startUpHiTempTrap")
)
if mibBuilder.loadTexts:
    startUpHiTempEV.setStatus(
        ""
    )

startUpLowTempEV = NotificationType(
    (1, 3, 6, 1, 4, 1, 26609, 2, 5, 2, 0, 53)
)
startUpLowTempEV.setObjects(
    ("COMM-BOARD-MIB", "startUpLowTempTrap")
)
if mibBuilder.loadTexts:
    startUpLowTempEV.setStatus(
        ""
    )

highTempAlarmEV = NotificationType(
    (1, 3, 6, 1, 4, 1, 26609, 2, 5, 2, 0, 54)
)
highTempAlarmEV.setObjects(
    ("COMM-BOARD-MIB", "highTempTrap")
)
if mibBuilder.loadTexts:
    highTempAlarmEV.setStatus(
        ""
    )

lowTempAlarmEV = NotificationType(
    (1, 3, 6, 1, 4, 1, 26609, 2, 5, 2, 0, 55)
)
lowTempAlarmEV.setObjects(
    ("COMM-BOARD-MIB", "lowTempTrap")
)
if mibBuilder.loadTexts:
    lowTempAlarmEV.setStatus(
        ""
    )

inletSensAlarmEV = NotificationType(
    (1, 3, 6, 1, 4, 1, 26609, 2, 5, 2, 0, 56)
)
inletSensAlarmEV.setObjects(
    ("COMM-BOARD-MIB", "inletSensFailTrap")
)
if mibBuilder.loadTexts:
    inletSensAlarmEV.setStatus(
        ""
    )

outletSensAlarmEV = NotificationType(
    (1, 3, 6, 1, 4, 1, 26609, 2, 5, 2, 0, 57)
)
outletSensAlarmEV.setObjects(
    ("COMM-BOARD-MIB", "outletSensFailTrap")
)
if mibBuilder.loadTexts:
    outletSensAlarmEV.setStatus(
        ""
    )

doorSmokeEV = NotificationType(
    (1, 3, 6, 1, 4, 1, 26609, 2, 5, 2, 0, 58)
)
doorSmokeEV.setObjects(
    ("COMM-BOARD-MIB", "doorSmokeTrap")
)
if mibBuilder.loadTexts:
    doorSmokeEV.setStatus(
        ""
    )

highPressureEV = NotificationType(
    (1, 3, 6, 1, 4, 1, 26609, 2, 5, 2, 0, 59)
)
highPressureEV.setObjects(
    ("COMM-BOARD-MIB", "highPressureTrap")
)
if mibBuilder.loadTexts:
    highPressureEV.setStatus(
        ""
    )

contcommfailEV = NotificationType(
    (1, 3, 6, 1, 4, 1, 26609, 2, 5, 2, 0, 60)
)
contcommfailEV.setObjects(
    ("COMM-BOARD-MIB", "contcommfailTrap")
)
if mibBuilder.loadTexts:
    contcommfailEV.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "COMM-BOARD-MIB",
    **{"DisplayString": DisplayString,
       "TruthValue": TruthValue,
       "pentairTechProd": pentairTechProd,
       "carelBoardMIB": carelBoardMIB,
       "menuInfo": menuInfo,
       "coolSetPoint": coolSetPoint,
       "cspName": cspName,
       "cspValue": cspValue,
       "coolSetPointMin": coolSetPointMin,
       "csplName": csplName,
       "csplValue": csplValue,
       "coolSetPointMax": coolSetPointMax,
       "csphName": csphName,
       "csphValue": csphValue,
       "coolDifferential": coolDifferential,
       "cdName": cdName,
       "cdValue": cdValue,
       "heatSetPoint": heatSetPoint,
       "hspName": hspName,
       "hspValue": hspValue,
       "heatSetPointMin": heatSetPointMin,
       "hsplName": hsplName,
       "hsplValue": hsplValue,
       "heatSetPointMax": heatSetPointMax,
       "hsphName": hsphName,
       "hsphValue": hsphValue,
       "heatDifferential": heatDifferential,
       "hdName": hdName,
       "hdValue": hdValue,
       "unitOfMeasure": unitOfMeasure,
       "umName": umName,
       "umValue": umValue,
       "highTempSetP": highTempSetP,
       "lowTempSetP": lowTempSetP,
       "faultInfo": faultInfo,
       "frostAlarm": frostAlarm,
       "faName": faName,
       "faEnable": faEnable,
       "faState": faState,
       "highTempAlarm": highTempAlarm,
       "htaName": htaName,
       "htaEnable": htaEnable,
       "htaState": htaState,
       "lowTempAlarm": lowTempAlarm,
       "ltaName": ltaName,
       "ltaEnable": ltaEnable,
       "ltaState": ltaState,
       "inletFailAlarm": inletFailAlarm,
       "isfaName": isfaName,
       "isfaEnable": isfaEnable,
       "isfaState": isfaState,
       "outletFailAlarm": outletFailAlarm,
       "osfaName": osfaName,
       "osfaEnable": osfaEnable,
       "osfaState": osfaState,
       "doorSmokeAlarm": doorSmokeAlarm,
       "dsaName": dsaName,
       "dsaEnable": dsaEnable,
       "dsaState": dsaState,
       "highPressureAlarm": highPressureAlarm,
       "hpaName": hpaName,
       "hpaEnable": hpaEnable,
       "hpaState": hpaState,
       "contCommFailAlarm": contCommFailAlarm,
       "ccfaName": ccfaName,
       "ccfaEnable": ccfaEnable,
       "ccfaState": ccfaState,
       "faultLog": faultLog,
       "log1Value": log1Value,
       "log2Value": log2Value,
       "log3Value": log3Value,
       "log4Value": log4Value,
       "log5Value": log5Value,
       "log6Value": log6Value,
       "log7Value": log7Value,
       "log8Value": log8Value,
       "log9Value": log9Value,
       "log10Value": log10Value,
       "log11Value": log11Value,
       "log12Value": log12Value,
       "log13Value": log13Value,
       "log14Value": log14Value,
       "log15Value": log15Value,
       "log16Value": log16Value,
       "log17Value": log17Value,
       "log18Value": log18Value,
       "log19Value": log19Value,
       "log20Value": log20Value,
       "log21Value": log21Value,
       "log22Value": log22Value,
       "log23Value": log23Value,
       "log24Value": log24Value,
       "log25Value": log25Value,
       "dataLog": dataLog,
       "inletSensor": inletSensor,
       "p1iName": p1iName,
       "p1iValue": p1iValue,
       "outletSensor": outletSensor,
       "p2iName": p2iName,
       "p2iValue": p2iValue,
       "cbNotification": cbNotification,
       "trapFreq": trapFreq,
       "trapRate": trapRate,
       "trapInterval": trapInterval,
       "trapList": trapList,
       "frostAlarmEV": frostAlarmEV,
       "startUpHiTempEV": startUpHiTempEV,
       "startUpLowTempEV": startUpLowTempEV,
       "highTempAlarmEV": highTempAlarmEV,
       "lowTempAlarmEV": lowTempAlarmEV,
       "inletSensAlarmEV": inletSensAlarmEV,
       "outletSensAlarmEV": outletSensAlarmEV,
       "doorSmokeEV": doorSmokeEV,
       "highPressureEV": highPressureEV,
       "contcommfailEV": contcommfailEV,
       "frostTrap": frostTrap,
       "startUpHiTempTrap": startUpHiTempTrap,
       "startUpLowTempTrap": startUpLowTempTrap,
       "highTempTrap": highTempTrap,
       "lowTempTrap": lowTempTrap,
       "inletSensFailTrap": inletSensFailTrap,
       "outletSensFailTrap": outletSensFailTrap,
       "doorSmokeTrap": doorSmokeTrap,
       "highPressureTrap": highPressureTrap,
       "contcommfailTrap": contcommfailTrap,
       "addressInfo": addressInfo,
       "deviceIP": deviceIP,
       "gatewayIP": gatewayIP,
       "subnetMask": subnetMask,
       "trapIP": trapIP,
       "dhcpServer": dhcpServer,
       "snmpComm": snmpComm,
       "revisionIDInfo": revisionIDInfo,
       "identification": identification,
       "commRev": commRev,
       "controlRev": controlRev,
       "commSerialNum": commSerialNum,
       "unitSerialNum": unitSerialNum,
       "unitModelNum": unitModelNum,
       "stationName": stationName}
)
