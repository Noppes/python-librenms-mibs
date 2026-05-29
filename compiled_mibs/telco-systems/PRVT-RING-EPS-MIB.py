# SNMP MIB module (PRVT-RING-EPS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\telco-systems\binos\PRVT-RING-EPS-MIB

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

(Dot1agCfmMDLevelOrNone,
 Dot1agCfmMepIdOrZero) = mibBuilder.importSymbols(
    "IEEE8021-CFM-MIB",
    "Dot1agCfmMDLevelOrNone",
    "Dot1agCfmMepIdOrZero")

(InterfaceIndexOrZero,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndexOrZero")

(switch,) = mibBuilder.importSymbols(
    "PRVT-SWITCH-MIB",
    "switch")

(VlanIdOrNone,) = mibBuilder.importSymbols(
    "Q-BRIDGE-MIB",
    "VlanIdOrNone")

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
 MacAddress,
 PhysAddress,
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

prvtRingEpsMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 134)
)
if mibBuilder.loadTexts:
    prvtRingEpsMib.setRevisions(
        ("2013-02-22 00:00",
         "2011-03-11 00:00",
         "2010-12-17 00:00",
         "2010-03-16 00:00",
         "2010-02-02 00:00",
         "2009-11-04 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class PrvtRingEpsModeType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("rapsMode8032v1", 1),
          ("rapsMode8032v2", 2))
    )



class PrvtRingEpsStateType(TextualConvention, Integer32):
    status = "current"
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
        *(("rapsInit", 0),
          ("rapsIdle", 1),
          ("rapsProtection", 2),
          ("rapsManualSwitch", 3),
          ("rapsForcedSwitch", 4),
          ("rapsPending", 5))
    )



class PrvtRingEpsLocalCommandType(TextualConvention, Integer32):
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
              7)
        )
    )
    namedValues = NamedValues(
        *(("rapsLcNoRequest", 0),
          ("rapsLcExercise", 1),
          ("rapsLcManualSwitch", 2),
          ("rapsLcSignalDegrade", 3),
          ("rapsLcSignalFail", 4),
          ("rapsLcForcedSwitch", 5),
          ("rapsLcClear", 6),
          ("rapsLcLockoutOfProtection", 7))
    )



class PrvtRingEpsRemoteRequestType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              0,
              7,
              11,
              13,
              14)
        )
    )
    namedValues = NamedValues(
        *(("rapsRsNone", -1),
          ("rapsRsNoRequest", 0),
          ("rapsRsManualSwitch", 7),
          ("rapsRsSignalFail", 11),
          ("rapsRsForcedSwitch", 13),
          ("rapsRsEvent", 14))
    )



class PrvtRingEpsNodeRoleType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("rapsNrSimpleNode", 0),
          ("rapsNrRplNeighborNode", 1),
          ("rapsNrRplOwner", 2))
    )



class PrvtRingEpsRplPortType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("port0", 0),
          ("port1", 1),
          ("none", 2))
    )



class PrvtRingEpsDefectType(TextualConvention, Bits):
    status = "current"
    namedValues = NamedValues(
        ("rapsDprovisioningMismatch", 0)
    )


class PrvtRingEpsPortStatusType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("rapsPsOk", 0),
          ("rapsPsBlocked", 1),
          ("rapsPsFailed", 2))
    )



class PrvtRingEpsPeerStatusType(TextualConvention, Bits):
    status = "current"
    namedValues = NamedValues(
        *(("bRplBlocked", 0),
          ("bDoNotFlush", 1),
          ("bBlockedPortReference", 2))
    )


# MIB Managed Objects in the order of their OIDs

_PrvtRingEpsNotifications_ObjectIdentity = ObjectIdentity
prvtRingEpsNotifications = _PrvtRingEpsNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 134, 0)
)
_PrvtRingEpsObjects_ObjectIdentity = ObjectIdentity
prvtRingEpsObjects = _PrvtRingEpsObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 134, 1)
)
_PrvtRingEpsInstances_ObjectIdentity = ObjectIdentity
prvtRingEpsInstances = _PrvtRingEpsInstances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 134, 1, 1)
)
_PrvtRingEpsInstanceTable_Object = MibTable
prvtRingEpsInstanceTable = _PrvtRingEpsInstanceTable_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 134, 1, 1, 1)
)
if mibBuilder.loadTexts:
    prvtRingEpsInstanceTable.setStatus("current")
_PrvtRingEpsInstanceEntry_Object = MibTableRow
prvtRingEpsInstanceEntry = _PrvtRingEpsInstanceEntry_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 134, 1, 1, 1, 1)
)
prvtRingEpsInstanceEntry.setIndexNames(
    (0, "PRVT-RING-EPS-MIB", "prvtRingEpsInstanceIndex"),
)
if mibBuilder.loadTexts:
    prvtRingEpsInstanceEntry.setStatus("current")


class _PrvtRingEpsInstanceIndex_Type(Unsigned32):
    """Custom type prvtRingEpsInstanceIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_PrvtRingEpsInstanceIndex_Type.__name__ = "Unsigned32"
_PrvtRingEpsInstanceIndex_Object = MibTableColumn
prvtRingEpsInstanceIndex = _PrvtRingEpsInstanceIndex_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 134, 1, 1, 1, 1, 1),
    _PrvtRingEpsInstanceIndex_Type()
)
prvtRingEpsInstanceIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    prvtRingEpsInstanceIndex.setStatus("current")


class _PrvtRingEpsMode_Type(PrvtRingEpsModeType):
    """Custom type prvtRingEpsMode based on PrvtRingEpsModeType"""
    defaultValue = 2


_PrvtRingEpsMode_Type.__name__ = "PrvtRingEpsModeType"
_PrvtRingEpsMode_Object = MibTableColumn
prvtRingEpsMode = _PrvtRingEpsMode_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 134, 1, 1, 1, 1, 2),
    _PrvtRingEpsMode_Type()
)
prvtRingEpsMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    prvtRingEpsMode.setStatus("current")


class _PrvtRingEpsNodeRole_Type(PrvtRingEpsNodeRoleType):
    """Custom type prvtRingEpsNodeRole based on PrvtRingEpsNodeRoleType"""
    defaultValue = 0


_PrvtRingEpsNodeRole_Type.__name__ = "PrvtRingEpsNodeRoleType"
_PrvtRingEpsNodeRole_Object = MibTableColumn
prvtRingEpsNodeRole = _PrvtRingEpsNodeRole_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 134, 1, 1, 1, 1, 3),
    _PrvtRingEpsNodeRole_Type()
)
prvtRingEpsNodeRole.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    prvtRingEpsNodeRole.setStatus("current")


class _PrvtRingEpsState_Type(PrvtRingEpsStateType):
    """Custom type prvtRingEpsState based on PrvtRingEpsStateType"""
    defaultValue = 0


_PrvtRingEpsState_Type.__name__ = "PrvtRingEpsStateType"
_PrvtRingEpsState_Object = MibTableColumn
prvtRingEpsState = _PrvtRingEpsState_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 134, 1, 1, 1, 1, 4),
    _PrvtRingEpsState_Type()
)
prvtRingEpsState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtRingEpsState.setStatus("current")


class _PrvtRingEpsLocalCommand_Type(PrvtRingEpsLocalCommandType):
    """Custom type prvtRingEpsLocalCommand based on PrvtRingEpsLocalCommandType"""
    defaultValue = 0


_PrvtRingEpsLocalCommand_Type.__name__ = "PrvtRingEpsLocalCommandType"
_PrvtRingEpsLocalCommand_Object = MibTableColumn
prvtRingEpsLocalCommand = _PrvtRingEpsLocalCommand_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 134, 1, 1, 1, 1, 5),
    _PrvtRingEpsLocalCommand_Type()
)
prvtRingEpsLocalCommand.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    prvtRingEpsLocalCommand.setStatus("current")


class _PrvtRingEpsControlVlan_Type(VlanIdOrNone):
    """Custom type prvtRingEpsControlVlan based on VlanIdOrNone"""
    defaultValue = 0


_PrvtRingEpsControlVlan_Type.__name__ = "VlanIdOrNone"
_PrvtRingEpsControlVlan_Object = MibTableColumn
prvtRingEpsControlVlan = _PrvtRingEpsControlVlan_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 134, 1, 1, 1, 1, 6),
    _PrvtRingEpsControlVlan_Type()
)
prvtRingEpsControlVlan.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    prvtRingEpsControlVlan.setStatus("current")


class _PrvtRingEpsPort0Ifindex_Type(InterfaceIndexOrZero):
    """Custom type prvtRingEpsPort0Ifindex based on InterfaceIndexOrZero"""
    defaultValue = 0


_PrvtRingEpsPort0Ifindex_Type.__name__ = "InterfaceIndexOrZero"
_PrvtRingEpsPort0Ifindex_Object = MibTableColumn
prvtRingEpsPort0Ifindex = _PrvtRingEpsPort0Ifindex_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 134, 1, 1, 1, 1, 7),
    _PrvtRingEpsPort0Ifindex_Type()
)
prvtRingEpsPort0Ifindex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    prvtRingEpsPort0Ifindex.setStatus("current")


class _PrvtRingEpsPort1Ifindex_Type(InterfaceIndexOrZero):
    """Custom type prvtRingEpsPort1Ifindex based on InterfaceIndexOrZero"""
    defaultValue = 0


_PrvtRingEpsPort1Ifindex_Type.__name__ = "InterfaceIndexOrZero"
_PrvtRingEpsPort1Ifindex_Object = MibTableColumn
prvtRingEpsPort1Ifindex = _PrvtRingEpsPort1Ifindex_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 134, 1, 1, 1, 1, 8),
    _PrvtRingEpsPort1Ifindex_Type()
)
prvtRingEpsPort1Ifindex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    prvtRingEpsPort1Ifindex.setStatus("current")


class _PrvtRingEpsRplPort_Type(PrvtRingEpsRplPortType):
    """Custom type prvtRingEpsRplPort based on PrvtRingEpsRplPortType"""
    defaultValue = 2


_PrvtRingEpsRplPort_Type.__name__ = "PrvtRingEpsRplPortType"
_PrvtRingEpsRplPort_Object = MibTableColumn
prvtRingEpsRplPort = _PrvtRingEpsRplPort_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 134, 1, 1, 1, 1, 9),
    _PrvtRingEpsRplPort_Type()
)
prvtRingEpsRplPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    prvtRingEpsRplPort.setStatus("current")


class _PrvtRingEpsManualSwitchPort_Type(PrvtRingEpsRplPortType):
    """Custom type prvtRingEpsManualSwitchPort based on PrvtRingEpsRplPortType"""
    defaultValue = 2


_PrvtRingEpsManualSwitchPort_Type.__name__ = "PrvtRingEpsRplPortType"
_PrvtRingEpsManualSwitchPort_Object = MibTableColumn
prvtRingEpsManualSwitchPort = _PrvtRingEpsManualSwitchPort_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 134, 1, 1, 1, 1, 10),
    _PrvtRingEpsManualSwitchPort_Type()
)
prvtRingEpsManualSwitchPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    prvtRingEpsManualSwitchPort.setStatus("current")


class _PrvtRingEpsCfmMdLevel_Type(Dot1agCfmMDLevelOrNone):
    """Custom type prvtRingEpsCfmMdLevel based on Dot1agCfmMDLevelOrNone"""
    defaultValue = -1


_PrvtRingEpsCfmMdLevel_Type.__name__ = "Dot1agCfmMDLevelOrNone"
_PrvtRingEpsCfmMdLevel_Object = MibTableColumn
prvtRingEpsCfmMdLevel = _PrvtRingEpsCfmMdLevel_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 134, 1, 1, 1, 1, 11),
    _PrvtRingEpsCfmMdLevel_Type()
)
prvtRingEpsCfmMdLevel.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    prvtRingEpsCfmMdLevel.setStatus("current")


class _PrvtRingEpsPort0Mep_Type(Dot1agCfmMepIdOrZero):
    """Custom type prvtRingEpsPort0Mep based on Dot1agCfmMepIdOrZero"""
    defaultValue = 0


_PrvtRingEpsPort0Mep_Type.__name__ = "Dot1agCfmMepIdOrZero"
_PrvtRingEpsPort0Mep_Object = MibTableColumn
prvtRingEpsPort0Mep = _PrvtRingEpsPort0Mep_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 134, 1, 1, 1, 1, 12),
    _PrvtRingEpsPort0Mep_Type()
)
prvtRingEpsPort0Mep.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    prvtRingEpsPort0Mep.setStatus("current")


class _PrvtRingEpsPort1Mep_Type(Dot1agCfmMepIdOrZero):
    """Custom type prvtRingEpsPort1Mep based on Dot1agCfmMepIdOrZero"""
    defaultValue = 0


_PrvtRingEpsPort1Mep_Type.__name__ = "Dot1agCfmMepIdOrZero"
_PrvtRingEpsPort1Mep_Object = MibTableColumn
prvtRingEpsPort1Mep = _PrvtRingEpsPort1Mep_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 134, 1, 1, 1, 1, 13),
    _PrvtRingEpsPort1Mep_Type()
)
prvtRingEpsPort1Mep.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    prvtRingEpsPort1Mep.setStatus("current")


class _PrvtRingEpsRevertive_Type(TruthValue):
    """Custom type prvtRingEpsRevertive based on TruthValue"""
    defaultValue = 1


_PrvtRingEpsRevertive_Type.__name__ = "TruthValue"
_PrvtRingEpsRevertive_Object = MibTableColumn
prvtRingEpsRevertive = _PrvtRingEpsRevertive_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 134, 1, 1, 1, 1, 14),
    _PrvtRingEpsRevertive_Type()
)
prvtRingEpsRevertive.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    prvtRingEpsRevertive.setStatus("current")


class _PrvtRingEpsNoVirtualChannel_Type(TruthValue):
    """Custom type prvtRingEpsNoVirtualChannel based on TruthValue"""
    defaultValue = 2


_PrvtRingEpsNoVirtualChannel_Type.__name__ = "TruthValue"
_PrvtRingEpsNoVirtualChannel_Object = MibTableColumn
prvtRingEpsNoVirtualChannel = _PrvtRingEpsNoVirtualChannel_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 134, 1, 1, 1, 1, 15),
    _PrvtRingEpsNoVirtualChannel_Type()
)
prvtRingEpsNoVirtualChannel.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    prvtRingEpsNoVirtualChannel.setStatus("current")


class _PrvtRingEpsHoldOffTimer_Type(Unsigned32):
    """Custom type prvtRingEpsHoldOffTimer based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000),
    )


_PrvtRingEpsHoldOffTimer_Type.__name__ = "Unsigned32"
_PrvtRingEpsHoldOffTimer_Object = MibTableColumn
prvtRingEpsHoldOffTimer = _PrvtRingEpsHoldOffTimer_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 134, 1, 1, 1, 1, 16),
    _PrvtRingEpsHoldOffTimer_Type()
)
prvtRingEpsHoldOffTimer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    prvtRingEpsHoldOffTimer.setStatus("current")


class _PrvtRingEpsWaitToRestoreTimer_Type(Unsigned32):
    """Custom type prvtRingEpsWaitToRestoreTimer based on Unsigned32"""
    defaultValue = 5

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 12),
    )


_PrvtRingEpsWaitToRestoreTimer_Type.__name__ = "Unsigned32"
_PrvtRingEpsWaitToRestoreTimer_Object = MibTableColumn
prvtRingEpsWaitToRestoreTimer = _PrvtRingEpsWaitToRestoreTimer_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 134, 1, 1, 1, 1, 17),
    _PrvtRingEpsWaitToRestoreTimer_Type()
)
prvtRingEpsWaitToRestoreTimer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    prvtRingEpsWaitToRestoreTimer.setStatus("current")


class _PrvtRingEpsGuardTimer_Type(Unsigned32):
    """Custom type prvtRingEpsGuardTimer based on Unsigned32"""
    defaultValue = 500

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 2000),
    )


_PrvtRingEpsGuardTimer_Type.__name__ = "Unsigned32"
_PrvtRingEpsGuardTimer_Object = MibTableColumn
prvtRingEpsGuardTimer = _PrvtRingEpsGuardTimer_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 134, 1, 1, 1, 1, 18),
    _PrvtRingEpsGuardTimer_Type()
)
prvtRingEpsGuardTimer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    prvtRingEpsGuardTimer.setStatus("current")


class _PrvtRingEpsWaitToBlockTimer_Type(Unsigned32):
    """Custom type prvtRingEpsWaitToBlockTimer based on Unsigned32"""
    defaultValue = 5500

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5010, 7000),
    )


_PrvtRingEpsWaitToBlockTimer_Type.__name__ = "Unsigned32"
_PrvtRingEpsWaitToBlockTimer_Object = MibTableColumn
prvtRingEpsWaitToBlockTimer = _PrvtRingEpsWaitToBlockTimer_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 134, 1, 1, 1, 1, 19),
    _PrvtRingEpsWaitToBlockTimer_Type()
)
prvtRingEpsWaitToBlockTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtRingEpsWaitToBlockTimer.setStatus("current")
_PrvtRingEpsDefectFop_Type = PrvtRingEpsDefectType
_PrvtRingEpsDefectFop_Object = MibTableColumn
prvtRingEpsDefectFop = _PrvtRingEpsDefectFop_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 134, 1, 1, 1, 1, 20),
    _PrvtRingEpsDefectFop_Type()
)
prvtRingEpsDefectFop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtRingEpsDefectFop.setStatus("current")


class _PrvtRingEpsPort0Status_Type(PrvtRingEpsPortStatusType):
    """Custom type prvtRingEpsPort0Status based on PrvtRingEpsPortStatusType"""
    defaultValue = 2


_PrvtRingEpsPort0Status_Type.__name__ = "PrvtRingEpsPortStatusType"
_PrvtRingEpsPort0Status_Object = MibTableColumn
prvtRingEpsPort0Status = _PrvtRingEpsPort0Status_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 134, 1, 1, 1, 1, 21),
    _PrvtRingEpsPort0Status_Type()
)
prvtRingEpsPort0Status.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtRingEpsPort0Status.setStatus("current")


class _PrvtRingEpsPort1Status_Type(PrvtRingEpsPortStatusType):
    """Custom type prvtRingEpsPort1Status based on PrvtRingEpsPortStatusType"""
    defaultValue = 2


_PrvtRingEpsPort1Status_Type.__name__ = "PrvtRingEpsPortStatusType"
_PrvtRingEpsPort1Status_Object = MibTableColumn
prvtRingEpsPort1Status = _PrvtRingEpsPort1Status_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 134, 1, 1, 1, 1, 22),
    _PrvtRingEpsPort1Status_Type()
)
prvtRingEpsPort1Status.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtRingEpsPort1Status.setStatus("current")
_PrvtRingEpsPort0PeerNodeId_Type = MacAddress
_PrvtRingEpsPort0PeerNodeId_Object = MibTableColumn
prvtRingEpsPort0PeerNodeId = _PrvtRingEpsPort0PeerNodeId_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 134, 1, 1, 1, 1, 23),
    _PrvtRingEpsPort0PeerNodeId_Type()
)
prvtRingEpsPort0PeerNodeId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtRingEpsPort0PeerNodeId.setStatus("current")
_PrvtRingEpsPort1PeerNodeId_Type = MacAddress
_PrvtRingEpsPort1PeerNodeId_Object = MibTableColumn
prvtRingEpsPort1PeerNodeId = _PrvtRingEpsPort1PeerNodeId_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 134, 1, 1, 1, 1, 24),
    _PrvtRingEpsPort1PeerNodeId_Type()
)
prvtRingEpsPort1PeerNodeId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtRingEpsPort1PeerNodeId.setStatus("current")


class _PrvtRingEpsPort0PeerCommand_Type(PrvtRingEpsRemoteRequestType):
    """Custom type prvtRingEpsPort0PeerCommand based on PrvtRingEpsRemoteRequestType"""
    defaultValue = -1


_PrvtRingEpsPort0PeerCommand_Type.__name__ = "PrvtRingEpsRemoteRequestType"
_PrvtRingEpsPort0PeerCommand_Object = MibTableColumn
prvtRingEpsPort0PeerCommand = _PrvtRingEpsPort0PeerCommand_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 134, 1, 1, 1, 1, 25),
    _PrvtRingEpsPort0PeerCommand_Type()
)
prvtRingEpsPort0PeerCommand.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtRingEpsPort0PeerCommand.setStatus("current")


class _PrvtRingEpsPort1PeerCommand_Type(PrvtRingEpsRemoteRequestType):
    """Custom type prvtRingEpsPort1PeerCommand based on PrvtRingEpsRemoteRequestType"""
    defaultValue = -1


_PrvtRingEpsPort1PeerCommand_Type.__name__ = "PrvtRingEpsRemoteRequestType"
_PrvtRingEpsPort1PeerCommand_Object = MibTableColumn
prvtRingEpsPort1PeerCommand = _PrvtRingEpsPort1PeerCommand_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 134, 1, 1, 1, 1, 26),
    _PrvtRingEpsPort1PeerCommand_Type()
)
prvtRingEpsPort1PeerCommand.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtRingEpsPort1PeerCommand.setStatus("current")
_PrvtRingEpsPort0PeerStatus_Type = PrvtRingEpsPeerStatusType
_PrvtRingEpsPort0PeerStatus_Object = MibTableColumn
prvtRingEpsPort0PeerStatus = _PrvtRingEpsPort0PeerStatus_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 134, 1, 1, 1, 1, 27),
    _PrvtRingEpsPort0PeerStatus_Type()
)
prvtRingEpsPort0PeerStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtRingEpsPort0PeerStatus.setStatus("current")
_PrvtRingEpsPort1PeerStatus_Type = PrvtRingEpsPeerStatusType
_PrvtRingEpsPort1PeerStatus_Object = MibTableColumn
prvtRingEpsPort1PeerStatus = _PrvtRingEpsPort1PeerStatus_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 134, 1, 1, 1, 1, 28),
    _PrvtRingEpsPort1PeerStatus_Type()
)
prvtRingEpsPort1PeerStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtRingEpsPort1PeerStatus.setStatus("current")


class _PrvtRingEpsOperationalStatus_Type(TruthValue):
    """Custom type prvtRingEpsOperationalStatus based on TruthValue"""
    defaultValue = 2


_PrvtRingEpsOperationalStatus_Type.__name__ = "TruthValue"
_PrvtRingEpsOperationalStatus_Object = MibTableColumn
prvtRingEpsOperationalStatus = _PrvtRingEpsOperationalStatus_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 134, 1, 1, 1, 1, 29),
    _PrvtRingEpsOperationalStatus_Type()
)
prvtRingEpsOperationalStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtRingEpsOperationalStatus.setStatus("current")


class _PrvtRingEpsAdminStatus_Type(TruthValue):
    """Custom type prvtRingEpsAdminStatus based on TruthValue"""
    defaultValue = 2


_PrvtRingEpsAdminStatus_Type.__name__ = "TruthValue"
_PrvtRingEpsAdminStatus_Object = MibTableColumn
prvtRingEpsAdminStatus = _PrvtRingEpsAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 134, 1, 1, 1, 1, 30),
    _PrvtRingEpsAdminStatus_Type()
)
prvtRingEpsAdminStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    prvtRingEpsAdminStatus.setStatus("current")
_PrvtRingEpsRowStatus_Type = RowStatus
_PrvtRingEpsRowStatus_Object = MibTableColumn
prvtRingEpsRowStatus = _PrvtRingEpsRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 134, 1, 1, 1, 1, 31),
    _PrvtRingEpsRowStatus_Type()
)
prvtRingEpsRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    prvtRingEpsRowStatus.setStatus("current")


class _PrvtRingEpsForcedSwitchPort_Type(PrvtRingEpsRplPortType):
    """Custom type prvtRingEpsForcedSwitchPort based on PrvtRingEpsRplPortType"""
    defaultValue = 2


_PrvtRingEpsForcedSwitchPort_Type.__name__ = "PrvtRingEpsRplPortType"
_PrvtRingEpsForcedSwitchPort_Object = MibTableColumn
prvtRingEpsForcedSwitchPort = _PrvtRingEpsForcedSwitchPort_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 134, 1, 1, 1, 1, 32),
    _PrvtRingEpsForcedSwitchPort_Type()
)
prvtRingEpsForcedSwitchPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    prvtRingEpsForcedSwitchPort.setStatus("current")
_PrvtRingEpsInstanceDescription_Type = DisplayString
_PrvtRingEpsInstanceDescription_Object = MibTableColumn
prvtRingEpsInstanceDescription = _PrvtRingEpsInstanceDescription_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 134, 1, 1, 1, 1, 33),
    _PrvtRingEpsInstanceDescription_Type()
)
prvtRingEpsInstanceDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    prvtRingEpsInstanceDescription.setStatus("current")


class _PrvtRingEpsRingId_Type(Unsigned32):
    """Custom type prvtRingEpsRingId based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_PrvtRingEpsRingId_Type.__name__ = "Unsigned32"
_PrvtRingEpsRingId_Object = MibTableColumn
prvtRingEpsRingId = _PrvtRingEpsRingId_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 134, 1, 1, 1, 1, 34),
    _PrvtRingEpsRingId_Type()
)
prvtRingEpsRingId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    prvtRingEpsRingId.setStatus("current")


class _PrvtRingEpsPort0MonitoringMethod_Type(Integer32):
    """Custom type prvtRingEpsPort0MonitoringMethod based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ccm", 1),
          ("link-status", 2))
    )


_PrvtRingEpsPort0MonitoringMethod_Type.__name__ = "Integer32"
_PrvtRingEpsPort0MonitoringMethod_Object = MibTableColumn
prvtRingEpsPort0MonitoringMethod = _PrvtRingEpsPort0MonitoringMethod_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 134, 1, 1, 1, 1, 35),
    _PrvtRingEpsPort0MonitoringMethod_Type()
)
prvtRingEpsPort0MonitoringMethod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prvtRingEpsPort0MonitoringMethod.setStatus("current")


class _PrvtRingEpsPort1MonitoringMethod_Type(Integer32):
    """Custom type prvtRingEpsPort1MonitoringMethod based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ccm", 1),
          ("link-status", 2))
    )


_PrvtRingEpsPort1MonitoringMethod_Type.__name__ = "Integer32"
_PrvtRingEpsPort1MonitoringMethod_Object = MibTableColumn
prvtRingEpsPort1MonitoringMethod = _PrvtRingEpsPort1MonitoringMethod_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 134, 1, 1, 1, 1, 36),
    _PrvtRingEpsPort1MonitoringMethod_Type()
)
prvtRingEpsPort1MonitoringMethod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prvtRingEpsPort1MonitoringMethod.setStatus("current")
_PrvtRingEpsVlans_ObjectIdentity = ObjectIdentity
prvtRingEpsVlans = _PrvtRingEpsVlans_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 134, 1, 2)
)
_PrvtRingEpsVlanTable_Object = MibTable
prvtRingEpsVlanTable = _PrvtRingEpsVlanTable_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 134, 1, 2, 1)
)
if mibBuilder.loadTexts:
    prvtRingEpsVlanTable.setStatus("current")
_PrvtRingEpsVlanEntry_Object = MibTableRow
prvtRingEpsVlanEntry = _PrvtRingEpsVlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 134, 1, 2, 1, 1)
)
prvtRingEpsVlanEntry.setIndexNames(
    (0, "PRVT-RING-EPS-MIB", "prvtRingEpsVlanIndex"),
)
if mibBuilder.loadTexts:
    prvtRingEpsVlanEntry.setStatus("current")


class _PrvtRingEpsVlanIndex_Type(Unsigned32):
    """Custom type prvtRingEpsVlanIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_PrvtRingEpsVlanIndex_Type.__name__ = "Unsigned32"
_PrvtRingEpsVlanIndex_Object = MibTableColumn
prvtRingEpsVlanIndex = _PrvtRingEpsVlanIndex_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 134, 1, 2, 1, 1, 1),
    _PrvtRingEpsVlanIndex_Type()
)
prvtRingEpsVlanIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    prvtRingEpsVlanIndex.setStatus("current")


class _PrvtRingEpsInstance_Type(Unsigned32):
    """Custom type prvtRingEpsInstance based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10),
    )


_PrvtRingEpsInstance_Type.__name__ = "Unsigned32"
_PrvtRingEpsInstance_Object = MibTableColumn
prvtRingEpsInstance = _PrvtRingEpsInstance_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 134, 1, 2, 1, 1, 2),
    _PrvtRingEpsInstance_Type()
)
prvtRingEpsInstance.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    prvtRingEpsInstance.setStatus("current")
_PrvtRingEpsVlanRowStatus_Type = RowStatus
_PrvtRingEpsVlanRowStatus_Object = MibTableColumn
prvtRingEpsVlanRowStatus = _PrvtRingEpsVlanRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 134, 1, 2, 1, 1, 3),
    _PrvtRingEpsVlanRowStatus_Type()
)
prvtRingEpsVlanRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    prvtRingEpsVlanRowStatus.setStatus("current")
_PrvtRingEpsSubRings_ObjectIdentity = ObjectIdentity
prvtRingEpsSubRings = _PrvtRingEpsSubRings_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 134, 1, 3)
)
_PrvtRingEpsSubRingTable_Object = MibTable
prvtRingEpsSubRingTable = _PrvtRingEpsSubRingTable_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 134, 1, 3, 1)
)
if mibBuilder.loadTexts:
    prvtRingEpsSubRingTable.setStatus("current")
_PrvtRingEpsSubRingEntry_Object = MibTableRow
prvtRingEpsSubRingEntry = _PrvtRingEpsSubRingEntry_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 134, 1, 3, 1, 1)
)
prvtRingEpsSubRingEntry.setIndexNames(
    (0, "PRVT-RING-EPS-MIB", "prvtRingEpsInstanceIndex"),
    (0, "PRVT-RING-EPS-MIB", "prvtRingEpsSubRingIndex"),
)
if mibBuilder.loadTexts:
    prvtRingEpsSubRingEntry.setStatus("current")


class _PrvtRingEpsSubRingIndex_Type(Unsigned32):
    """Custom type prvtRingEpsSubRingIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_PrvtRingEpsSubRingIndex_Type.__name__ = "Unsigned32"
_PrvtRingEpsSubRingIndex_Object = MibTableColumn
prvtRingEpsSubRingIndex = _PrvtRingEpsSubRingIndex_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 134, 1, 3, 1, 1, 1),
    _PrvtRingEpsSubRingIndex_Type()
)
prvtRingEpsSubRingIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    prvtRingEpsSubRingIndex.setStatus("current")


class _PrvtRingEpsSubRingNodeRole_Type(PrvtRingEpsNodeRoleType):
    """Custom type prvtRingEpsSubRingNodeRole based on PrvtRingEpsNodeRoleType"""
    defaultValue = 0


_PrvtRingEpsSubRingNodeRole_Type.__name__ = "PrvtRingEpsNodeRoleType"
_PrvtRingEpsSubRingNodeRole_Object = MibTableColumn
prvtRingEpsSubRingNodeRole = _PrvtRingEpsSubRingNodeRole_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 134, 1, 3, 1, 1, 2),
    _PrvtRingEpsSubRingNodeRole_Type()
)
prvtRingEpsSubRingNodeRole.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    prvtRingEpsSubRingNodeRole.setStatus("current")


class _PrvtRingEpsSubRingState_Type(PrvtRingEpsStateType):
    """Custom type prvtRingEpsSubRingState based on PrvtRingEpsStateType"""
    defaultValue = 0


_PrvtRingEpsSubRingState_Type.__name__ = "PrvtRingEpsStateType"
_PrvtRingEpsSubRingState_Object = MibTableColumn
prvtRingEpsSubRingState = _PrvtRingEpsSubRingState_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 134, 1, 3, 1, 1, 3),
    _PrvtRingEpsSubRingState_Type()
)
prvtRingEpsSubRingState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtRingEpsSubRingState.setStatus("current")


class _PrvtRingEpsSubRingLocalCommand_Type(PrvtRingEpsLocalCommandType):
    """Custom type prvtRingEpsSubRingLocalCommand based on PrvtRingEpsLocalCommandType"""
    defaultValue = 0


_PrvtRingEpsSubRingLocalCommand_Type.__name__ = "PrvtRingEpsLocalCommandType"
_PrvtRingEpsSubRingLocalCommand_Object = MibTableColumn
prvtRingEpsSubRingLocalCommand = _PrvtRingEpsSubRingLocalCommand_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 134, 1, 3, 1, 1, 4),
    _PrvtRingEpsSubRingLocalCommand_Type()
)
prvtRingEpsSubRingLocalCommand.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    prvtRingEpsSubRingLocalCommand.setStatus("current")


class _PrvtRingEpsSubRingPortIfindex_Type(InterfaceIndexOrZero):
    """Custom type prvtRingEpsSubRingPortIfindex based on InterfaceIndexOrZero"""
    defaultValue = 0


_PrvtRingEpsSubRingPortIfindex_Type.__name__ = "InterfaceIndexOrZero"
_PrvtRingEpsSubRingPortIfindex_Object = MibTableColumn
prvtRingEpsSubRingPortIfindex = _PrvtRingEpsSubRingPortIfindex_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 134, 1, 3, 1, 1, 5),
    _PrvtRingEpsSubRingPortIfindex_Type()
)
prvtRingEpsSubRingPortIfindex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    prvtRingEpsSubRingPortIfindex.setStatus("current")


class _PrvtRingEpsSubRingPortMep_Type(Dot1agCfmMepIdOrZero):
    """Custom type prvtRingEpsSubRingPortMep based on Dot1agCfmMepIdOrZero"""
    defaultValue = 0


_PrvtRingEpsSubRingPortMep_Type.__name__ = "Dot1agCfmMepIdOrZero"
_PrvtRingEpsSubRingPortMep_Object = MibTableColumn
prvtRingEpsSubRingPortMep = _PrvtRingEpsSubRingPortMep_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 134, 1, 3, 1, 1, 6),
    _PrvtRingEpsSubRingPortMep_Type()
)
prvtRingEpsSubRingPortMep.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    prvtRingEpsSubRingPortMep.setStatus("current")


class _PrvtRingEpsSubRingRplPort_Type(PrvtRingEpsRplPortType):
    """Custom type prvtRingEpsSubRingRplPort based on PrvtRingEpsRplPortType"""
    defaultValue = 2


_PrvtRingEpsSubRingRplPort_Type.__name__ = "PrvtRingEpsRplPortType"
_PrvtRingEpsSubRingRplPort_Object = MibTableColumn
prvtRingEpsSubRingRplPort = _PrvtRingEpsSubRingRplPort_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 134, 1, 3, 1, 1, 7),
    _PrvtRingEpsSubRingRplPort_Type()
)
prvtRingEpsSubRingRplPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    prvtRingEpsSubRingRplPort.setStatus("current")


class _PrvtRingEpsSubRingVirtualChannelVlan_Type(VlanIdOrNone):
    """Custom type prvtRingEpsSubRingVirtualChannelVlan based on VlanIdOrNone"""
    defaultValue = 0


_PrvtRingEpsSubRingVirtualChannelVlan_Type.__name__ = "VlanIdOrNone"
_PrvtRingEpsSubRingVirtualChannelVlan_Object = MibTableColumn
prvtRingEpsSubRingVirtualChannelVlan = _PrvtRingEpsSubRingVirtualChannelVlan_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 134, 1, 3, 1, 1, 8),
    _PrvtRingEpsSubRingVirtualChannelVlan_Type()
)
prvtRingEpsSubRingVirtualChannelVlan.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    prvtRingEpsSubRingVirtualChannelVlan.setStatus("current")


class _PrvtRingEpsSubRingRevertive_Type(TruthValue):
    """Custom type prvtRingEpsSubRingRevertive based on TruthValue"""
    defaultValue = 1


_PrvtRingEpsSubRingRevertive_Type.__name__ = "TruthValue"
_PrvtRingEpsSubRingRevertive_Object = MibTableColumn
prvtRingEpsSubRingRevertive = _PrvtRingEpsSubRingRevertive_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 134, 1, 3, 1, 1, 9),
    _PrvtRingEpsSubRingRevertive_Type()
)
prvtRingEpsSubRingRevertive.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    prvtRingEpsSubRingRevertive.setStatus("current")


class _PrvtRingEpsSubRingHoldOffTimer_Type(Unsigned32):
    """Custom type prvtRingEpsSubRingHoldOffTimer based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000),
    )


_PrvtRingEpsSubRingHoldOffTimer_Type.__name__ = "Unsigned32"
_PrvtRingEpsSubRingHoldOffTimer_Object = MibTableColumn
prvtRingEpsSubRingHoldOffTimer = _PrvtRingEpsSubRingHoldOffTimer_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 134, 1, 3, 1, 1, 10),
    _PrvtRingEpsSubRingHoldOffTimer_Type()
)
prvtRingEpsSubRingHoldOffTimer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    prvtRingEpsSubRingHoldOffTimer.setStatus("current")


class _PrvtRingEpsSubRingWaitToRestoreTimer_Type(Unsigned32):
    """Custom type prvtRingEpsSubRingWaitToRestoreTimer based on Unsigned32"""
    defaultValue = 5

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 12),
    )


_PrvtRingEpsSubRingWaitToRestoreTimer_Type.__name__ = "Unsigned32"
_PrvtRingEpsSubRingWaitToRestoreTimer_Object = MibTableColumn
prvtRingEpsSubRingWaitToRestoreTimer = _PrvtRingEpsSubRingWaitToRestoreTimer_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 134, 1, 3, 1, 1, 11),
    _PrvtRingEpsSubRingWaitToRestoreTimer_Type()
)
prvtRingEpsSubRingWaitToRestoreTimer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    prvtRingEpsSubRingWaitToRestoreTimer.setStatus("current")


class _PrvtRingEpsSubRingGuardTimer_Type(Unsigned32):
    """Custom type prvtRingEpsSubRingGuardTimer based on Unsigned32"""
    defaultValue = 500

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 2000),
    )


_PrvtRingEpsSubRingGuardTimer_Type.__name__ = "Unsigned32"
_PrvtRingEpsSubRingGuardTimer_Object = MibTableColumn
prvtRingEpsSubRingGuardTimer = _PrvtRingEpsSubRingGuardTimer_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 134, 1, 3, 1, 1, 12),
    _PrvtRingEpsSubRingGuardTimer_Type()
)
prvtRingEpsSubRingGuardTimer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    prvtRingEpsSubRingGuardTimer.setStatus("current")


class _PrvtRingEpsSubRingWaitToBlockTimer_Type(Unsigned32):
    """Custom type prvtRingEpsSubRingWaitToBlockTimer based on Unsigned32"""
    defaultValue = 5500

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5010, 7000),
    )


_PrvtRingEpsSubRingWaitToBlockTimer_Type.__name__ = "Unsigned32"
_PrvtRingEpsSubRingWaitToBlockTimer_Object = MibTableColumn
prvtRingEpsSubRingWaitToBlockTimer = _PrvtRingEpsSubRingWaitToBlockTimer_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 134, 1, 3, 1, 1, 13),
    _PrvtRingEpsSubRingWaitToBlockTimer_Type()
)
prvtRingEpsSubRingWaitToBlockTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtRingEpsSubRingWaitToBlockTimer.setStatus("current")
_PrvtRingEpsSubRingDefectFop_Type = PrvtRingEpsDefectType
_PrvtRingEpsSubRingDefectFop_Object = MibTableColumn
prvtRingEpsSubRingDefectFop = _PrvtRingEpsSubRingDefectFop_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 134, 1, 3, 1, 1, 14),
    _PrvtRingEpsSubRingDefectFop_Type()
)
prvtRingEpsSubRingDefectFop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtRingEpsSubRingDefectFop.setStatus("current")


class _PrvtRingEpsSubRingPortStatus_Type(PrvtRingEpsPortStatusType):
    """Custom type prvtRingEpsSubRingPortStatus based on PrvtRingEpsPortStatusType"""
    defaultValue = 2


_PrvtRingEpsSubRingPortStatus_Type.__name__ = "PrvtRingEpsPortStatusType"
_PrvtRingEpsSubRingPortStatus_Object = MibTableColumn
prvtRingEpsSubRingPortStatus = _PrvtRingEpsSubRingPortStatus_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 134, 1, 3, 1, 1, 15),
    _PrvtRingEpsSubRingPortStatus_Type()
)
prvtRingEpsSubRingPortStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtRingEpsSubRingPortStatus.setStatus("current")
_PrvtRingEpsSubRingPortPeerNodeId_Type = MacAddress
_PrvtRingEpsSubRingPortPeerNodeId_Object = MibTableColumn
prvtRingEpsSubRingPortPeerNodeId = _PrvtRingEpsSubRingPortPeerNodeId_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 134, 1, 3, 1, 1, 16),
    _PrvtRingEpsSubRingPortPeerNodeId_Type()
)
prvtRingEpsSubRingPortPeerNodeId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtRingEpsSubRingPortPeerNodeId.setStatus("current")


class _PrvtRingEpsSubRingPeerCommand_Type(PrvtRingEpsRemoteRequestType):
    """Custom type prvtRingEpsSubRingPeerCommand based on PrvtRingEpsRemoteRequestType"""
    defaultValue = -1


_PrvtRingEpsSubRingPeerCommand_Type.__name__ = "PrvtRingEpsRemoteRequestType"
_PrvtRingEpsSubRingPeerCommand_Object = MibTableColumn
prvtRingEpsSubRingPeerCommand = _PrvtRingEpsSubRingPeerCommand_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 134, 1, 3, 1, 1, 17),
    _PrvtRingEpsSubRingPeerCommand_Type()
)
prvtRingEpsSubRingPeerCommand.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtRingEpsSubRingPeerCommand.setStatus("current")
_PrvtRingEpsSubRingPeerStatus_Type = PrvtRingEpsPeerStatusType
_PrvtRingEpsSubRingPeerStatus_Object = MibTableColumn
prvtRingEpsSubRingPeerStatus = _PrvtRingEpsSubRingPeerStatus_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 134, 1, 3, 1, 1, 18),
    _PrvtRingEpsSubRingPeerStatus_Type()
)
prvtRingEpsSubRingPeerStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtRingEpsSubRingPeerStatus.setStatus("current")
_PrvtRingEpsSubRingVcPeerNodeId_Type = MacAddress
_PrvtRingEpsSubRingVcPeerNodeId_Object = MibTableColumn
prvtRingEpsSubRingVcPeerNodeId = _PrvtRingEpsSubRingVcPeerNodeId_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 134, 1, 3, 1, 1, 19),
    _PrvtRingEpsSubRingVcPeerNodeId_Type()
)
prvtRingEpsSubRingVcPeerNodeId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtRingEpsSubRingVcPeerNodeId.setStatus("current")


class _PrvtRingEpsSubRingVcPeerCommand_Type(PrvtRingEpsRemoteRequestType):
    """Custom type prvtRingEpsSubRingVcPeerCommand based on PrvtRingEpsRemoteRequestType"""
    defaultValue = -1


_PrvtRingEpsSubRingVcPeerCommand_Type.__name__ = "PrvtRingEpsRemoteRequestType"
_PrvtRingEpsSubRingVcPeerCommand_Object = MibTableColumn
prvtRingEpsSubRingVcPeerCommand = _PrvtRingEpsSubRingVcPeerCommand_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 134, 1, 3, 1, 1, 20),
    _PrvtRingEpsSubRingVcPeerCommand_Type()
)
prvtRingEpsSubRingVcPeerCommand.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtRingEpsSubRingVcPeerCommand.setStatus("current")
_PrvtRingEpsSubRingVcPeerStatus_Type = PrvtRingEpsPeerStatusType
_PrvtRingEpsSubRingVcPeerStatus_Object = MibTableColumn
prvtRingEpsSubRingVcPeerStatus = _PrvtRingEpsSubRingVcPeerStatus_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 134, 1, 3, 1, 1, 21),
    _PrvtRingEpsSubRingVcPeerStatus_Type()
)
prvtRingEpsSubRingVcPeerStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtRingEpsSubRingVcPeerStatus.setStatus("current")


class _PrvtRingEpsSubRingPropagateTC_Type(TruthValue):
    """Custom type prvtRingEpsSubRingPropagateTC based on TruthValue"""
    defaultValue = 2


_PrvtRingEpsSubRingPropagateTC_Type.__name__ = "TruthValue"
_PrvtRingEpsSubRingPropagateTC_Object = MibTableColumn
prvtRingEpsSubRingPropagateTC = _PrvtRingEpsSubRingPropagateTC_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 134, 1, 3, 1, 1, 22),
    _PrvtRingEpsSubRingPropagateTC_Type()
)
prvtRingEpsSubRingPropagateTC.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    prvtRingEpsSubRingPropagateTC.setStatus("current")


class _PrvtRingEpsSubRingOperationalStatus_Type(TruthValue):
    """Custom type prvtRingEpsSubRingOperationalStatus based on TruthValue"""
    defaultValue = 2


_PrvtRingEpsSubRingOperationalStatus_Type.__name__ = "TruthValue"
_PrvtRingEpsSubRingOperationalStatus_Object = MibTableColumn
prvtRingEpsSubRingOperationalStatus = _PrvtRingEpsSubRingOperationalStatus_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 134, 1, 3, 1, 1, 23),
    _PrvtRingEpsSubRingOperationalStatus_Type()
)
prvtRingEpsSubRingOperationalStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtRingEpsSubRingOperationalStatus.setStatus("current")


class _PrvtRingEpsSubRingAdminStatus_Type(TruthValue):
    """Custom type prvtRingEpsSubRingAdminStatus based on TruthValue"""
    defaultValue = 2


_PrvtRingEpsSubRingAdminStatus_Type.__name__ = "TruthValue"
_PrvtRingEpsSubRingAdminStatus_Object = MibTableColumn
prvtRingEpsSubRingAdminStatus = _PrvtRingEpsSubRingAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 134, 1, 3, 1, 1, 24),
    _PrvtRingEpsSubRingAdminStatus_Type()
)
prvtRingEpsSubRingAdminStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    prvtRingEpsSubRingAdminStatus.setStatus("current")
_PrvtRingEpsSubRingRowStatus_Type = RowStatus
_PrvtRingEpsSubRingRowStatus_Object = MibTableColumn
prvtRingEpsSubRingRowStatus = _PrvtRingEpsSubRingRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 134, 1, 3, 1, 1, 25),
    _PrvtRingEpsSubRingRowStatus_Type()
)
prvtRingEpsSubRingRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    prvtRingEpsSubRingRowStatus.setStatus("current")


class _PrvtRingEpsSubRingControlVlan_Type(VlanIdOrNone):
    """Custom type prvtRingEpsSubRingControlVlan based on VlanIdOrNone"""
    defaultValue = 0


_PrvtRingEpsSubRingControlVlan_Type.__name__ = "VlanIdOrNone"
_PrvtRingEpsSubRingControlVlan_Object = MibTableColumn
prvtRingEpsSubRingControlVlan = _PrvtRingEpsSubRingControlVlan_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 134, 1, 3, 1, 1, 26),
    _PrvtRingEpsSubRingControlVlan_Type()
)
prvtRingEpsSubRingControlVlan.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    prvtRingEpsSubRingControlVlan.setStatus("current")
_PrvtRingEpsSubRingDescription_Type = DisplayString
_PrvtRingEpsSubRingDescription_Object = MibTableColumn
prvtRingEpsSubRingDescription = _PrvtRingEpsSubRingDescription_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 134, 1, 3, 1, 1, 27),
    _PrvtRingEpsSubRingDescription_Type()
)
prvtRingEpsSubRingDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    prvtRingEpsSubRingDescription.setStatus("current")


class _PrvtRingEpsSubRingRingId_Type(Unsigned32):
    """Custom type prvtRingEpsSubRingRingId based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_PrvtRingEpsSubRingRingId_Type.__name__ = "Unsigned32"
_PrvtRingEpsSubRingRingId_Object = MibTableColumn
prvtRingEpsSubRingRingId = _PrvtRingEpsSubRingRingId_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 134, 1, 3, 1, 1, 28),
    _PrvtRingEpsSubRingRingId_Type()
)
prvtRingEpsSubRingRingId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    prvtRingEpsSubRingRingId.setStatus("current")


class _PrvtRingEpsSubRingMonitoringMethod_Type(Integer32):
    """Custom type prvtRingEpsSubRingMonitoringMethod based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ccm", 1),
          ("link-status", 2))
    )


_PrvtRingEpsSubRingMonitoringMethod_Type.__name__ = "Integer32"
_PrvtRingEpsSubRingMonitoringMethod_Object = MibTableColumn
prvtRingEpsSubRingMonitoringMethod = _PrvtRingEpsSubRingMonitoringMethod_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 134, 1, 3, 1, 1, 29),
    _PrvtRingEpsSubRingMonitoringMethod_Type()
)
prvtRingEpsSubRingMonitoringMethod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prvtRingEpsSubRingMonitoringMethod.setStatus("current")
_PrvtRingEpsConformance_ObjectIdentity = ObjectIdentity
prvtRingEpsConformance = _PrvtRingEpsConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 134, 2)
)
_PrvtRingEpsCompliances_ObjectIdentity = ObjectIdentity
prvtRingEpsCompliances = _PrvtRingEpsCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 134, 2, 1)
)
_PrvtRingEpsGroups_ObjectIdentity = ObjectIdentity
prvtRingEpsGroups = _PrvtRingEpsGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 134, 2, 2)
)

# Managed Objects groups

prvtRingEpsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 134, 2, 2, 1)
)
prvtRingEpsGroup.setObjects(
      *(("PRVT-RING-EPS-MIB", "prvtRingEpsMode"),
        ("PRVT-RING-EPS-MIB", "prvtRingEpsNodeRole"),
        ("PRVT-RING-EPS-MIB", "prvtRingEpsState"),
        ("PRVT-RING-EPS-MIB", "prvtRingEpsLocalCommand"),
        ("PRVT-RING-EPS-MIB", "prvtRingEpsControlVlan"),
        ("PRVT-RING-EPS-MIB", "prvtRingEpsPort0Ifindex"),
        ("PRVT-RING-EPS-MIB", "prvtRingEpsPort1Ifindex"),
        ("PRVT-RING-EPS-MIB", "prvtRingEpsRplPort"),
        ("PRVT-RING-EPS-MIB", "prvtRingEpsManualSwitchPort"),
        ("PRVT-RING-EPS-MIB", "prvtRingEpsCfmMdLevel"),
        ("PRVT-RING-EPS-MIB", "prvtRingEpsPort0Mep"),
        ("PRVT-RING-EPS-MIB", "prvtRingEpsPort1Mep"),
        ("PRVT-RING-EPS-MIB", "prvtRingEpsRevertive"),
        ("PRVT-RING-EPS-MIB", "prvtRingEpsNoVirtualChannel"),
        ("PRVT-RING-EPS-MIB", "prvtRingEpsHoldOffTimer"),
        ("PRVT-RING-EPS-MIB", "prvtRingEpsWaitToRestoreTimer"),
        ("PRVT-RING-EPS-MIB", "prvtRingEpsGuardTimer"),
        ("PRVT-RING-EPS-MIB", "prvtRingEpsWaitToBlockTimer"),
        ("PRVT-RING-EPS-MIB", "prvtRingEpsDefectFop"),
        ("PRVT-RING-EPS-MIB", "prvtRingEpsPort0Status"),
        ("PRVT-RING-EPS-MIB", "prvtRingEpsPort1Status"),
        ("PRVT-RING-EPS-MIB", "prvtRingEpsPort0PeerNodeId"),
        ("PRVT-RING-EPS-MIB", "prvtRingEpsPort1PeerNodeId"),
        ("PRVT-RING-EPS-MIB", "prvtRingEpsPort0PeerCommand"),
        ("PRVT-RING-EPS-MIB", "prvtRingEpsPort1PeerCommand"),
        ("PRVT-RING-EPS-MIB", "prvtRingEpsPort0PeerStatus"),
        ("PRVT-RING-EPS-MIB", "prvtRingEpsPort1PeerStatus"),
        ("PRVT-RING-EPS-MIB", "prvtRingEpsOperationalStatus"),
        ("PRVT-RING-EPS-MIB", "prvtRingEpsAdminStatus"),
        ("PRVT-RING-EPS-MIB", "prvtRingEpsRowStatus"),
        ("PRVT-RING-EPS-MIB", "prvtRingEpsForcedSwitchPort"),
        ("PRVT-RING-EPS-MIB", "prvtRingEpsInstanceDescription"),
        ("PRVT-RING-EPS-MIB", "prvtRingEpsRingId"),
        ("PRVT-RING-EPS-MIB", "prvtRingEpsPort0MonitoringMethod"),
        ("PRVT-RING-EPS-MIB", "prvtRingEpsPort1MonitoringMethod"))
)
if mibBuilder.loadTexts:
    prvtRingEpsGroup.setStatus("current")

prvtRingEpsVlanGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 134, 2, 2, 2)
)
prvtRingEpsVlanGroup.setObjects(
      *(("PRVT-RING-EPS-MIB", "prvtRingEpsInstance"),
        ("PRVT-RING-EPS-MIB", "prvtRingEpsVlanRowStatus"))
)
if mibBuilder.loadTexts:
    prvtRingEpsVlanGroup.setStatus("current")

prvtRingEpsSubRingGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 134, 2, 2, 3)
)
prvtRingEpsSubRingGroup.setObjects(
      *(("PRVT-RING-EPS-MIB", "prvtRingEpsSubRingNodeRole"),
        ("PRVT-RING-EPS-MIB", "prvtRingEpsSubRingState"),
        ("PRVT-RING-EPS-MIB", "prvtRingEpsSubRingLocalCommand"),
        ("PRVT-RING-EPS-MIB", "prvtRingEpsSubRingPortIfindex"),
        ("PRVT-RING-EPS-MIB", "prvtRingEpsSubRingPortMep"),
        ("PRVT-RING-EPS-MIB", "prvtRingEpsSubRingRplPort"),
        ("PRVT-RING-EPS-MIB", "prvtRingEpsSubRingVirtualChannelVlan"),
        ("PRVT-RING-EPS-MIB", "prvtRingEpsSubRingRevertive"),
        ("PRVT-RING-EPS-MIB", "prvtRingEpsSubRingHoldOffTimer"),
        ("PRVT-RING-EPS-MIB", "prvtRingEpsSubRingWaitToRestoreTimer"),
        ("PRVT-RING-EPS-MIB", "prvtRingEpsSubRingGuardTimer"),
        ("PRVT-RING-EPS-MIB", "prvtRingEpsSubRingWaitToBlockTimer"),
        ("PRVT-RING-EPS-MIB", "prvtRingEpsSubRingDefectFop"),
        ("PRVT-RING-EPS-MIB", "prvtRingEpsSubRingPortStatus"),
        ("PRVT-RING-EPS-MIB", "prvtRingEpsSubRingPortPeerNodeId"),
        ("PRVT-RING-EPS-MIB", "prvtRingEpsSubRingPeerCommand"),
        ("PRVT-RING-EPS-MIB", "prvtRingEpsSubRingPeerStatus"),
        ("PRVT-RING-EPS-MIB", "prvtRingEpsSubRingVcPeerNodeId"),
        ("PRVT-RING-EPS-MIB", "prvtRingEpsSubRingVcPeerCommand"),
        ("PRVT-RING-EPS-MIB", "prvtRingEpsSubRingVcPeerStatus"),
        ("PRVT-RING-EPS-MIB", "prvtRingEpsSubRingPropagateTC"),
        ("PRVT-RING-EPS-MIB", "prvtRingEpsSubRingOperationalStatus"),
        ("PRVT-RING-EPS-MIB", "prvtRingEpsSubRingAdminStatus"),
        ("PRVT-RING-EPS-MIB", "prvtRingEpsSubRingRowStatus"),
        ("PRVT-RING-EPS-MIB", "prvtRingEpsSubRingControlVlan"),
        ("PRVT-RING-EPS-MIB", "prvtRingEpsSubRingDescription"),
        ("PRVT-RING-EPS-MIB", "prvtRingEpsSubRingRingId"),
        ("PRVT-RING-EPS-MIB", "prvtRingEpsSubRingMonitoringMethod"))
)
if mibBuilder.loadTexts:
    prvtRingEpsSubRingGroup.setStatus("current")


# Notification objects

prvtRingEpsDefectAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 134, 0, 1)
)
prvtRingEpsDefectAlarm.setObjects(
      *(("PRVT-RING-EPS-MIB", "prvtRingEpsOperationalStatus"),
        ("PRVT-RING-EPS-MIB", "prvtRingEpsDefectFop"))
)
if mibBuilder.loadTexts:
    prvtRingEpsDefectAlarm.setStatus(
        "current"
    )

prvtRingEpsSwitchoverAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 134, 0, 2)
)
prvtRingEpsSwitchoverAlarm.setObjects(
    ("PRVT-RING-EPS-MIB", "prvtRingEpsState")
)
if mibBuilder.loadTexts:
    prvtRingEpsSwitchoverAlarm.setStatus(
        "current"
    )

prvtRingEpsSubRingDefectAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 134, 0, 3)
)
prvtRingEpsSubRingDefectAlarm.setObjects(
      *(("PRVT-RING-EPS-MIB", "prvtRingEpsSubRingOperationalStatus"),
        ("PRVT-RING-EPS-MIB", "prvtRingEpsSubRingDefectFop"))
)
if mibBuilder.loadTexts:
    prvtRingEpsSubRingDefectAlarm.setStatus(
        "current"
    )

prvtRingEpsSubRingSwitchoverAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 134, 0, 4)
)
prvtRingEpsSubRingSwitchoverAlarm.setObjects(
    ("PRVT-RING-EPS-MIB", "prvtRingEpsSubRingState")
)
if mibBuilder.loadTexts:
    prvtRingEpsSubRingSwitchoverAlarm.setStatus(
        "current"
    )


# Notifications groups

prvtRingEpsNotificationsGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 134, 2, 2, 4)
)
prvtRingEpsNotificationsGroup.setObjects(
      *(("PRVT-RING-EPS-MIB", "prvtRingEpsSwitchoverAlarm"),
        ("PRVT-RING-EPS-MIB", "prvtRingEpsDefectAlarm"),
        ("PRVT-RING-EPS-MIB", "prvtRingEpsSubRingSwitchoverAlarm"),
        ("PRVT-RING-EPS-MIB", "prvtRingEpsSubRingDefectAlarm"))
)
if mibBuilder.loadTexts:
    prvtRingEpsNotificationsGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

prvtRingEpsCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 134, 2, 1, 1)
)
prvtRingEpsCompliance.setObjects(
      *(("PRVT-RING-EPS-MIB", "prvtRingEpsGroup"),
        ("PRVT-RING-EPS-MIB", "prvtRingEpsVlanGroup"),
        ("PRVT-RING-EPS-MIB", "prvtRingEpsSubRingGroup"),
        ("PRVT-RING-EPS-MIB", "prvtRingEpsNotificationsGroup"))
)
if mibBuilder.loadTexts:
    prvtRingEpsCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "PRVT-RING-EPS-MIB",
    **{"PrvtRingEpsModeType": PrvtRingEpsModeType,
       "PrvtRingEpsStateType": PrvtRingEpsStateType,
       "PrvtRingEpsLocalCommandType": PrvtRingEpsLocalCommandType,
       "PrvtRingEpsRemoteRequestType": PrvtRingEpsRemoteRequestType,
       "PrvtRingEpsNodeRoleType": PrvtRingEpsNodeRoleType,
       "PrvtRingEpsRplPortType": PrvtRingEpsRplPortType,
       "PrvtRingEpsDefectType": PrvtRingEpsDefectType,
       "PrvtRingEpsPortStatusType": PrvtRingEpsPortStatusType,
       "PrvtRingEpsPeerStatusType": PrvtRingEpsPeerStatusType,
       "prvtRingEpsMib": prvtRingEpsMib,
       "prvtRingEpsNotifications": prvtRingEpsNotifications,
       "prvtRingEpsDefectAlarm": prvtRingEpsDefectAlarm,
       "prvtRingEpsSwitchoverAlarm": prvtRingEpsSwitchoverAlarm,
       "prvtRingEpsSubRingDefectAlarm": prvtRingEpsSubRingDefectAlarm,
       "prvtRingEpsSubRingSwitchoverAlarm": prvtRingEpsSubRingSwitchoverAlarm,
       "prvtRingEpsObjects": prvtRingEpsObjects,
       "prvtRingEpsInstances": prvtRingEpsInstances,
       "prvtRingEpsInstanceTable": prvtRingEpsInstanceTable,
       "prvtRingEpsInstanceEntry": prvtRingEpsInstanceEntry,
       "prvtRingEpsInstanceIndex": prvtRingEpsInstanceIndex,
       "prvtRingEpsMode": prvtRingEpsMode,
       "prvtRingEpsNodeRole": prvtRingEpsNodeRole,
       "prvtRingEpsState": prvtRingEpsState,
       "prvtRingEpsLocalCommand": prvtRingEpsLocalCommand,
       "prvtRingEpsControlVlan": prvtRingEpsControlVlan,
       "prvtRingEpsPort0Ifindex": prvtRingEpsPort0Ifindex,
       "prvtRingEpsPort1Ifindex": prvtRingEpsPort1Ifindex,
       "prvtRingEpsRplPort": prvtRingEpsRplPort,
       "prvtRingEpsManualSwitchPort": prvtRingEpsManualSwitchPort,
       "prvtRingEpsCfmMdLevel": prvtRingEpsCfmMdLevel,
       "prvtRingEpsPort0Mep": prvtRingEpsPort0Mep,
       "prvtRingEpsPort1Mep": prvtRingEpsPort1Mep,
       "prvtRingEpsRevertive": prvtRingEpsRevertive,
       "prvtRingEpsNoVirtualChannel": prvtRingEpsNoVirtualChannel,
       "prvtRingEpsHoldOffTimer": prvtRingEpsHoldOffTimer,
       "prvtRingEpsWaitToRestoreTimer": prvtRingEpsWaitToRestoreTimer,
       "prvtRingEpsGuardTimer": prvtRingEpsGuardTimer,
       "prvtRingEpsWaitToBlockTimer": prvtRingEpsWaitToBlockTimer,
       "prvtRingEpsDefectFop": prvtRingEpsDefectFop,
       "prvtRingEpsPort0Status": prvtRingEpsPort0Status,
       "prvtRingEpsPort1Status": prvtRingEpsPort1Status,
       "prvtRingEpsPort0PeerNodeId": prvtRingEpsPort0PeerNodeId,
       "prvtRingEpsPort1PeerNodeId": prvtRingEpsPort1PeerNodeId,
       "prvtRingEpsPort0PeerCommand": prvtRingEpsPort0PeerCommand,
       "prvtRingEpsPort1PeerCommand": prvtRingEpsPort1PeerCommand,
       "prvtRingEpsPort0PeerStatus": prvtRingEpsPort0PeerStatus,
       "prvtRingEpsPort1PeerStatus": prvtRingEpsPort1PeerStatus,
       "prvtRingEpsOperationalStatus": prvtRingEpsOperationalStatus,
       "prvtRingEpsAdminStatus": prvtRingEpsAdminStatus,
       "prvtRingEpsRowStatus": prvtRingEpsRowStatus,
       "prvtRingEpsForcedSwitchPort": prvtRingEpsForcedSwitchPort,
       "prvtRingEpsInstanceDescription": prvtRingEpsInstanceDescription,
       "prvtRingEpsRingId": prvtRingEpsRingId,
       "prvtRingEpsPort0MonitoringMethod": prvtRingEpsPort0MonitoringMethod,
       "prvtRingEpsPort1MonitoringMethod": prvtRingEpsPort1MonitoringMethod,
       "prvtRingEpsVlans": prvtRingEpsVlans,
       "prvtRingEpsVlanTable": prvtRingEpsVlanTable,
       "prvtRingEpsVlanEntry": prvtRingEpsVlanEntry,
       "prvtRingEpsVlanIndex": prvtRingEpsVlanIndex,
       "prvtRingEpsInstance": prvtRingEpsInstance,
       "prvtRingEpsVlanRowStatus": prvtRingEpsVlanRowStatus,
       "prvtRingEpsSubRings": prvtRingEpsSubRings,
       "prvtRingEpsSubRingTable": prvtRingEpsSubRingTable,
       "prvtRingEpsSubRingEntry": prvtRingEpsSubRingEntry,
       "prvtRingEpsSubRingIndex": prvtRingEpsSubRingIndex,
       "prvtRingEpsSubRingNodeRole": prvtRingEpsSubRingNodeRole,
       "prvtRingEpsSubRingState": prvtRingEpsSubRingState,
       "prvtRingEpsSubRingLocalCommand": prvtRingEpsSubRingLocalCommand,
       "prvtRingEpsSubRingPortIfindex": prvtRingEpsSubRingPortIfindex,
       "prvtRingEpsSubRingPortMep": prvtRingEpsSubRingPortMep,
       "prvtRingEpsSubRingRplPort": prvtRingEpsSubRingRplPort,
       "prvtRingEpsSubRingVirtualChannelVlan": prvtRingEpsSubRingVirtualChannelVlan,
       "prvtRingEpsSubRingRevertive": prvtRingEpsSubRingRevertive,
       "prvtRingEpsSubRingHoldOffTimer": prvtRingEpsSubRingHoldOffTimer,
       "prvtRingEpsSubRingWaitToRestoreTimer": prvtRingEpsSubRingWaitToRestoreTimer,
       "prvtRingEpsSubRingGuardTimer": prvtRingEpsSubRingGuardTimer,
       "prvtRingEpsSubRingWaitToBlockTimer": prvtRingEpsSubRingWaitToBlockTimer,
       "prvtRingEpsSubRingDefectFop": prvtRingEpsSubRingDefectFop,
       "prvtRingEpsSubRingPortStatus": prvtRingEpsSubRingPortStatus,
       "prvtRingEpsSubRingPortPeerNodeId": prvtRingEpsSubRingPortPeerNodeId,
       "prvtRingEpsSubRingPeerCommand": prvtRingEpsSubRingPeerCommand,
       "prvtRingEpsSubRingPeerStatus": prvtRingEpsSubRingPeerStatus,
       "prvtRingEpsSubRingVcPeerNodeId": prvtRingEpsSubRingVcPeerNodeId,
       "prvtRingEpsSubRingVcPeerCommand": prvtRingEpsSubRingVcPeerCommand,
       "prvtRingEpsSubRingVcPeerStatus": prvtRingEpsSubRingVcPeerStatus,
       "prvtRingEpsSubRingPropagateTC": prvtRingEpsSubRingPropagateTC,
       "prvtRingEpsSubRingOperationalStatus": prvtRingEpsSubRingOperationalStatus,
       "prvtRingEpsSubRingAdminStatus": prvtRingEpsSubRingAdminStatus,
       "prvtRingEpsSubRingRowStatus": prvtRingEpsSubRingRowStatus,
       "prvtRingEpsSubRingControlVlan": prvtRingEpsSubRingControlVlan,
       "prvtRingEpsSubRingDescription": prvtRingEpsSubRingDescription,
       "prvtRingEpsSubRingRingId": prvtRingEpsSubRingRingId,
       "prvtRingEpsSubRingMonitoringMethod": prvtRingEpsSubRingMonitoringMethod,
       "prvtRingEpsConformance": prvtRingEpsConformance,
       "prvtRingEpsCompliances": prvtRingEpsCompliances,
       "prvtRingEpsCompliance": prvtRingEpsCompliance,
       "prvtRingEpsGroups": prvtRingEpsGroups,
       "prvtRingEpsGroup": prvtRingEpsGroup,
       "prvtRingEpsVlanGroup": prvtRingEpsVlanGroup,
       "prvtRingEpsSubRingGroup": prvtRingEpsSubRingGroup,
       "prvtRingEpsNotificationsGroup": prvtRingEpsNotificationsGroup}
)
