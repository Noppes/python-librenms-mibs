# SNMP MIB module (PRVT-EVENT-PROPAGATION-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\telco-systems\binox\PRVT-EVENT-PROPAGATION-MIB

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

(switch,) = mibBuilder.importSymbols(
    "PRVT-SWITCH-MIB",
    "switch")

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
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

prvtEventPropagationMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 166)
)
if mibBuilder.loadTexts:
    prvtEventPropagationMIB.setRevisions(
        ("2014-11-10 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_PrvtEventPropagationObjects_ObjectIdentity = ObjectIdentity
prvtEventPropagationObjects = _PrvtEventPropagationObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 166, 1)
)
_PrvtEventPropagationProfileTable_Object = MibTable
prvtEventPropagationProfileTable = _PrvtEventPropagationProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 166, 1, 1)
)
if mibBuilder.loadTexts:
    prvtEventPropagationProfileTable.setStatus("current")
_PrvtEventPropagationProfileEntry_Object = MibTableRow
prvtEventPropagationProfileEntry = _PrvtEventPropagationProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 166, 1, 1, 1)
)
prvtEventPropagationProfileEntry.setIndexNames(
    (0, "PRVT-EVENT-PROPAGATION-MIB", "prvtEventPropagationProfileName"),
)
if mibBuilder.loadTexts:
    prvtEventPropagationProfileEntry.setStatus("current")


class _PrvtEventPropagationProfileName_Type(OctetString):
    """Custom type prvtEventPropagationProfileName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_PrvtEventPropagationProfileName_Type.__name__ = "OctetString"
_PrvtEventPropagationProfileName_Object = MibTableColumn
prvtEventPropagationProfileName = _PrvtEventPropagationProfileName_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 166, 1, 1, 1, 1),
    _PrvtEventPropagationProfileName_Type()
)
prvtEventPropagationProfileName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    prvtEventPropagationProfileName.setStatus("current")
_PrvtEventPropagationProfileRowStatus_Type = RowStatus
_PrvtEventPropagationProfileRowStatus_Object = MibTableColumn
prvtEventPropagationProfileRowStatus = _PrvtEventPropagationProfileRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 166, 1, 1, 1, 2),
    _PrvtEventPropagationProfileRowStatus_Type()
)
prvtEventPropagationProfileRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    prvtEventPropagationProfileRowStatus.setStatus("current")


class _PrvtEventPropagationSourceRemMep_Type(Unsigned32):
    """Custom type prvtEventPropagationSourceRemMep based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8191),
    )


_PrvtEventPropagationSourceRemMep_Type.__name__ = "Unsigned32"
_PrvtEventPropagationSourceRemMep_Object = MibTableColumn
prvtEventPropagationSourceRemMep = _PrvtEventPropagationSourceRemMep_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 166, 1, 1, 1, 3),
    _PrvtEventPropagationSourceRemMep_Type()
)
prvtEventPropagationSourceRemMep.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    prvtEventPropagationSourceRemMep.setStatus("current")


class _PrvtEventPropagationSourceLocalMep_Type(Unsigned32):
    """Custom type prvtEventPropagationSourceLocalMep based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8191),
    )


_PrvtEventPropagationSourceLocalMep_Type.__name__ = "Unsigned32"
_PrvtEventPropagationSourceLocalMep_Object = MibTableColumn
prvtEventPropagationSourceLocalMep = _PrvtEventPropagationSourceLocalMep_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 166, 1, 1, 1, 4),
    _PrvtEventPropagationSourceLocalMep_Type()
)
prvtEventPropagationSourceLocalMep.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    prvtEventPropagationSourceLocalMep.setStatus("current")


class _PrvtEventPropagationSourceVrrpGroup_Type(Unsigned32):
    """Custom type prvtEventPropagationSourceVrrpGroup based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_PrvtEventPropagationSourceVrrpGroup_Type.__name__ = "Unsigned32"
_PrvtEventPropagationSourceVrrpGroup_Object = MibTableColumn
prvtEventPropagationSourceVrrpGroup = _PrvtEventPropagationSourceVrrpGroup_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 166, 1, 1, 1, 5),
    _PrvtEventPropagationSourceVrrpGroup_Type()
)
prvtEventPropagationSourceVrrpGroup.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    prvtEventPropagationSourceVrrpGroup.setStatus("current")


class _PrvtEventPropagationEvent_Type(Integer32):
    """Custom type prvtEventPropagationEvent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("statusDown", 1),
          ("conLost", 2),
          ("aisLck", 4),
          ("rcvdTcBpdu", 5),
          ("vrrpStatusBackup", 6))
    )


_PrvtEventPropagationEvent_Type.__name__ = "Integer32"
_PrvtEventPropagationEvent_Object = MibTableColumn
prvtEventPropagationEvent = _PrvtEventPropagationEvent_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 166, 1, 1, 1, 6),
    _PrvtEventPropagationEvent_Type()
)
prvtEventPropagationEvent.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    prvtEventPropagationEvent.setStatus("current")


class _PrvtEventPropagationAction_Type(Integer32):
    """Custom type prvtEventPropagationAction based on Integer32"""
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
        *(("none", 0),
          ("linkDrop", 1),
          ("macWithdraw", 2),
          ("lacpStandby", 3),
          ("restrictForwarding", 4),
          ("noRestrictForwarding", 5))
    )


_PrvtEventPropagationAction_Type.__name__ = "Integer32"
_PrvtEventPropagationAction_Object = MibTableColumn
prvtEventPropagationAction = _PrvtEventPropagationAction_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 166, 1, 1, 1, 7),
    _PrvtEventPropagationAction_Type()
)
prvtEventPropagationAction.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    prvtEventPropagationAction.setStatus("current")


class _PrvtEventPropagationReverse_Type(Integer32):
    """Custom type prvtEventPropagationReverse based on Integer32"""
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
        *(("none", 0),
          ("linkRestore", 1),
          ("lacpActive", 2),
          ("restrictForwarding", 3),
          ("noRestrictForwarding", 4))
    )


_PrvtEventPropagationReverse_Type.__name__ = "Integer32"
_PrvtEventPropagationReverse_Object = MibTableColumn
prvtEventPropagationReverse = _PrvtEventPropagationReverse_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 166, 1, 1, 1, 8),
    _PrvtEventPropagationReverse_Type()
)
prvtEventPropagationReverse.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    prvtEventPropagationReverse.setStatus("current")


class _PrvtEventPropagationThreshold_Type(Unsigned32):
    """Custom type prvtEventPropagationThreshold based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_PrvtEventPropagationThreshold_Type.__name__ = "Unsigned32"
_PrvtEventPropagationThreshold_Object = MibTableColumn
prvtEventPropagationThreshold = _PrvtEventPropagationThreshold_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 166, 1, 1, 1, 9),
    _PrvtEventPropagationThreshold_Type()
)
prvtEventPropagationThreshold.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    prvtEventPropagationThreshold.setStatus("current")


class _PrvtEventPropagationTimerWaitToRestore_Type(Unsigned32):
    """Custom type prvtEventPropagationTimerWaitToRestore based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 600000),
    )


_PrvtEventPropagationTimerWaitToRestore_Type.__name__ = "Unsigned32"
_PrvtEventPropagationTimerWaitToRestore_Object = MibTableColumn
prvtEventPropagationTimerWaitToRestore = _PrvtEventPropagationTimerWaitToRestore_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 166, 1, 1, 1, 10),
    _PrvtEventPropagationTimerWaitToRestore_Type()
)
prvtEventPropagationTimerWaitToRestore.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    prvtEventPropagationTimerWaitToRestore.setStatus("current")


class _PrvtEventPropagationTimerHoldOff_Type(Unsigned32):
    """Custom type prvtEventPropagationTimerHoldOff based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 600000),
    )


_PrvtEventPropagationTimerHoldOff_Type.__name__ = "Unsigned32"
_PrvtEventPropagationTimerHoldOff_Object = MibTableColumn
prvtEventPropagationTimerHoldOff = _PrvtEventPropagationTimerHoldOff_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 166, 1, 1, 1, 11),
    _PrvtEventPropagationTimerHoldOff_Type()
)
prvtEventPropagationTimerHoldOff.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    prvtEventPropagationTimerHoldOff.setStatus("current")
_PrvtEventPropagationPerformMacFlush_Type = TruthValue
_PrvtEventPropagationPerformMacFlush_Object = MibTableColumn
prvtEventPropagationPerformMacFlush = _PrvtEventPropagationPerformMacFlush_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 166, 1, 1, 1, 12),
    _PrvtEventPropagationPerformMacFlush_Type()
)
prvtEventPropagationPerformMacFlush.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    prvtEventPropagationPerformMacFlush.setStatus("current")
_PrvtEventPropagationSourcePortTable_Object = MibTable
prvtEventPropagationSourcePortTable = _PrvtEventPropagationSourcePortTable_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 166, 1, 2)
)
if mibBuilder.loadTexts:
    prvtEventPropagationSourcePortTable.setStatus("current")
_PrvtEventPropagationSourcePortEntry_Object = MibTableRow
prvtEventPropagationSourcePortEntry = _PrvtEventPropagationSourcePortEntry_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 166, 1, 2, 1)
)
prvtEventPropagationSourcePortEntry.setIndexNames(
    (0, "PRVT-EVENT-PROPAGATION-MIB", "prvtEventPropagationProfileName"),
    (0, "PRVT-EVENT-PROPAGATION-MIB", "prvtEventPropagationSourcePortName"),
)
if mibBuilder.loadTexts:
    prvtEventPropagationSourcePortEntry.setStatus("current")
_PrvtEventPropagationSourcePortName_Type = OctetString
_PrvtEventPropagationSourcePortName_Object = MibTableColumn
prvtEventPropagationSourcePortName = _PrvtEventPropagationSourcePortName_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 166, 1, 2, 1, 1),
    _PrvtEventPropagationSourcePortName_Type()
)
prvtEventPropagationSourcePortName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    prvtEventPropagationSourcePortName.setStatus("current")
_PrvtEventPropagationSourcePortRowStatus_Type = RowStatus
_PrvtEventPropagationSourcePortRowStatus_Object = MibTableColumn
prvtEventPropagationSourcePortRowStatus = _PrvtEventPropagationSourcePortRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 166, 1, 2, 1, 2),
    _PrvtEventPropagationSourcePortRowStatus_Type()
)
prvtEventPropagationSourcePortRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    prvtEventPropagationSourcePortRowStatus.setStatus("current")
_PrvtEventPropagationSessionTable_Object = MibTable
prvtEventPropagationSessionTable = _PrvtEventPropagationSessionTable_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 166, 1, 3)
)
if mibBuilder.loadTexts:
    prvtEventPropagationSessionTable.setStatus("current")
_PrvtEventPropagationSessionEntry_Object = MibTableRow
prvtEventPropagationSessionEntry = _PrvtEventPropagationSessionEntry_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 166, 1, 3, 1)
)
prvtEventPropagationSessionEntry.setIndexNames(
    (0, "PRVT-EVENT-PROPAGATION-MIB", "prvtEventPropagationProfileName"),
    (0, "PRVT-EVENT-PROPAGATION-MIB", "prvtEventPropagationSessionIndex"),
)
if mibBuilder.loadTexts:
    prvtEventPropagationSessionEntry.setStatus("current")
_PrvtEventPropagationSessionIndex_Type = Unsigned32
_PrvtEventPropagationSessionIndex_Object = MibTableColumn
prvtEventPropagationSessionIndex = _PrvtEventPropagationSessionIndex_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 166, 1, 3, 1, 1),
    _PrvtEventPropagationSessionIndex_Type()
)
prvtEventPropagationSessionIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    prvtEventPropagationSessionIndex.setStatus("current")
_PrvtEventPropagationSessionProfileName_Type = OctetString
_PrvtEventPropagationSessionProfileName_Object = MibTableColumn
prvtEventPropagationSessionProfileName = _PrvtEventPropagationSessionProfileName_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 166, 1, 3, 1, 2),
    _PrvtEventPropagationSessionProfileName_Type()
)
prvtEventPropagationSessionProfileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtEventPropagationSessionProfileName.setStatus("current")


class _PrvtEventPropagationSessionTarget_Type(Integer32):
    """Custom type prvtEventPropagationSessionTarget based on Integer32"""
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
        *(("none", 0),
          ("sap", 1),
          ("port", 2),
          ("lag", 3),
          ("sdp", 4))
    )


_PrvtEventPropagationSessionTarget_Type.__name__ = "Integer32"
_PrvtEventPropagationSessionTarget_Object = MibTableColumn
prvtEventPropagationSessionTarget = _PrvtEventPropagationSessionTarget_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 166, 1, 3, 1, 3),
    _PrvtEventPropagationSessionTarget_Type()
)
prvtEventPropagationSessionTarget.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtEventPropagationSessionTarget.setStatus("current")
_PrvtEventPropagationSessionId_Type = OctetString
_PrvtEventPropagationSessionId_Object = MibTableColumn
prvtEventPropagationSessionId = _PrvtEventPropagationSessionId_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 166, 1, 3, 1, 4),
    _PrvtEventPropagationSessionId_Type()
)
prvtEventPropagationSessionId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtEventPropagationSessionId.setStatus("current")


class _PrvtEventPropagationSessionState_Type(Integer32):
    """Custom type prvtEventPropagationSessionState based on Integer32"""
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
        *(("none", 0),
          ("linkDropped", 1),
          ("linkRestored", 2),
          ("linkActionPend", 3),
          ("linkRevertivePend", 4))
    )


_PrvtEventPropagationSessionState_Type.__name__ = "Integer32"
_PrvtEventPropagationSessionState_Object = MibTableColumn
prvtEventPropagationSessionState = _PrvtEventPropagationSessionState_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 166, 1, 3, 1, 5),
    _PrvtEventPropagationSessionState_Type()
)
prvtEventPropagationSessionState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtEventPropagationSessionState.setStatus("current")
_PrvtEventPropagationSessionActions_Type = Unsigned32
_PrvtEventPropagationSessionActions_Object = MibTableColumn
prvtEventPropagationSessionActions = _PrvtEventPropagationSessionActions_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 166, 1, 3, 1, 6),
    _PrvtEventPropagationSessionActions_Type()
)
prvtEventPropagationSessionActions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtEventPropagationSessionActions.setStatus("current")
_PrvtEventPropagationSessionRevertives_Type = Unsigned32
_PrvtEventPropagationSessionRevertives_Object = MibTableColumn
prvtEventPropagationSessionRevertives = _PrvtEventPropagationSessionRevertives_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 166, 1, 3, 1, 7),
    _PrvtEventPropagationSessionRevertives_Type()
)
prvtEventPropagationSessionRevertives.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtEventPropagationSessionRevertives.setStatus("current")
_EpappPortTable_Object = MibTable
epappPortTable = _EpappPortTable_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 166, 1, 4)
)
if mibBuilder.loadTexts:
    epappPortTable.setStatus("current")
_EpappPortEntry_Object = MibTableRow
epappPortEntry = _EpappPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 166, 1, 4, 1)
)
epappPortEntry.setIndexNames(
    (0, "PRVT-EVENT-PROPAGATION-MIB", "epappPortName"),
)
if mibBuilder.loadTexts:
    epappPortEntry.setStatus("current")
_EpappPortName_Type = OctetString
_EpappPortName_Object = MibTableColumn
epappPortName = _EpappPortName_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 166, 1, 4, 1, 1),
    _EpappPortName_Type()
)
epappPortName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    epappPortName.setStatus("current")
_EpappPortRowStatus_Type = RowStatus
_EpappPortRowStatus_Object = MibTableColumn
epappPortRowStatus = _EpappPortRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 166, 1, 4, 1, 2),
    _EpappPortRowStatus_Type()
)
epappPortRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    epappPortRowStatus.setStatus("current")


class _EpappPortProfile_Type(OctetString):
    """Custom type epappPortProfile based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_EpappPortProfile_Type.__name__ = "OctetString"
_EpappPortProfile_Object = MibTableColumn
epappPortProfile = _EpappPortProfile_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 166, 1, 4, 1, 3),
    _EpappPortProfile_Type()
)
epappPortProfile.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    epappPortProfile.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "PRVT-EVENT-PROPAGATION-MIB",
    **{"prvtEventPropagationMIB": prvtEventPropagationMIB,
       "prvtEventPropagationObjects": prvtEventPropagationObjects,
       "prvtEventPropagationProfileTable": prvtEventPropagationProfileTable,
       "prvtEventPropagationProfileEntry": prvtEventPropagationProfileEntry,
       "prvtEventPropagationProfileName": prvtEventPropagationProfileName,
       "prvtEventPropagationProfileRowStatus": prvtEventPropagationProfileRowStatus,
       "prvtEventPropagationSourceRemMep": prvtEventPropagationSourceRemMep,
       "prvtEventPropagationSourceLocalMep": prvtEventPropagationSourceLocalMep,
       "prvtEventPropagationSourceVrrpGroup": prvtEventPropagationSourceVrrpGroup,
       "prvtEventPropagationEvent": prvtEventPropagationEvent,
       "prvtEventPropagationAction": prvtEventPropagationAction,
       "prvtEventPropagationReverse": prvtEventPropagationReverse,
       "prvtEventPropagationThreshold": prvtEventPropagationThreshold,
       "prvtEventPropagationTimerWaitToRestore": prvtEventPropagationTimerWaitToRestore,
       "prvtEventPropagationTimerHoldOff": prvtEventPropagationTimerHoldOff,
       "prvtEventPropagationPerformMacFlush": prvtEventPropagationPerformMacFlush,
       "prvtEventPropagationSourcePortTable": prvtEventPropagationSourcePortTable,
       "prvtEventPropagationSourcePortEntry": prvtEventPropagationSourcePortEntry,
       "prvtEventPropagationSourcePortName": prvtEventPropagationSourcePortName,
       "prvtEventPropagationSourcePortRowStatus": prvtEventPropagationSourcePortRowStatus,
       "prvtEventPropagationSessionTable": prvtEventPropagationSessionTable,
       "prvtEventPropagationSessionEntry": prvtEventPropagationSessionEntry,
       "prvtEventPropagationSessionIndex": prvtEventPropagationSessionIndex,
       "prvtEventPropagationSessionProfileName": prvtEventPropagationSessionProfileName,
       "prvtEventPropagationSessionTarget": prvtEventPropagationSessionTarget,
       "prvtEventPropagationSessionId": prvtEventPropagationSessionId,
       "prvtEventPropagationSessionState": prvtEventPropagationSessionState,
       "prvtEventPropagationSessionActions": prvtEventPropagationSessionActions,
       "prvtEventPropagationSessionRevertives": prvtEventPropagationSessionRevertives,
       "epappPortTable": epappPortTable,
       "epappPortEntry": epappPortEntry,
       "epappPortName": epappPortName,
       "epappPortRowStatus": epappPortRowStatus,
       "epappPortProfile": epappPortProfile}
)
