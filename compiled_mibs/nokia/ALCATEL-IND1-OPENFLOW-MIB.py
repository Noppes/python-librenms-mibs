# SNMP MIB module (ALCATEL-IND1-OPENFLOW-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\nokia\aos7\ALCATEL-IND1-OPENFLOW-MIB

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

(softentIND1OpenflowMIB,) = mibBuilder.importSymbols(
    "ALCATEL-IND1-BASE",
    "softentIND1OpenflowMIB")

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

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
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

alcatelIND1OpenflowMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 70, 1)
)
if mibBuilder.loadTexts:
    alcatelIND1OpenflowMIB.setRevisions(
        ("2019-11-27 00:00",
         "2014-03-26 00:00",
         "2014-10-08 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AlcatelIND1OpenflowMIBNotifications_ObjectIdentity = ObjectIdentity
alcatelIND1OpenflowMIBNotifications = _AlcatelIND1OpenflowMIBNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 70, 1, 0)
)
_AlcatelIND1OpenflowMIBObjects_ObjectIdentity = ObjectIdentity
alcatelIND1OpenflowMIBObjects = _AlcatelIND1OpenflowMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 70, 1, 1)
)
if mibBuilder.loadTexts:
    alcatelIND1OpenflowMIBObjects.setStatus("current")
_AlaOpenflowGlobalConfigObjects_ObjectIdentity = ObjectIdentity
alaOpenflowGlobalConfigObjects = _AlaOpenflowGlobalConfigObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 70, 1, 1, 1)
)


class _AlaOpenflowGlobalBackoffMax_Type(Integer32):
    """Custom type alaOpenflowGlobalBackoffMax based on Integer32"""
    defaultValue = 60

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 60),
    )


_AlaOpenflowGlobalBackoffMax_Type.__name__ = "Integer32"
_AlaOpenflowGlobalBackoffMax_Object = MibScalar
alaOpenflowGlobalBackoffMax = _AlaOpenflowGlobalBackoffMax_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 70, 1, 1, 1, 1),
    _AlaOpenflowGlobalBackoffMax_Type()
)
alaOpenflowGlobalBackoffMax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaOpenflowGlobalBackoffMax.setStatus("current")


class _AlaOpenflowGlobalIdleProbeTimeout_Type(Integer32):
    """Custom type alaOpenflowGlobalIdleProbeTimeout based on Integer32"""
    defaultValue = 15

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 60),
    )


_AlaOpenflowGlobalIdleProbeTimeout_Type.__name__ = "Integer32"
_AlaOpenflowGlobalIdleProbeTimeout_Object = MibScalar
alaOpenflowGlobalIdleProbeTimeout = _AlaOpenflowGlobalIdleProbeTimeout_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 70, 1, 1, 1, 2),
    _AlaOpenflowGlobalIdleProbeTimeout_Type()
)
alaOpenflowGlobalIdleProbeTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaOpenflowGlobalIdleProbeTimeout.setStatus("current")
_AlaOpenflowLogicalSwitchTable_Object = MibTable
alaOpenflowLogicalSwitchTable = _AlaOpenflowLogicalSwitchTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 70, 1, 1, 2)
)
if mibBuilder.loadTexts:
    alaOpenflowLogicalSwitchTable.setStatus("current")
_AlaOpenflowLogicalSwitchEntry_Object = MibTableRow
alaOpenflowLogicalSwitchEntry = _AlaOpenflowLogicalSwitchEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 70, 1, 1, 2, 1)
)
alaOpenflowLogicalSwitchEntry.setIndexNames(
    (0, "ALCATEL-IND1-OPENFLOW-MIB", "alaOpenflowLogicalSwitch"),
)
if mibBuilder.loadTexts:
    alaOpenflowLogicalSwitchEntry.setStatus("current")


class _AlaOpenflowLogicalSwitch_Type(SnmpAdminString):
    """Custom type alaOpenflowLogicalSwitch based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_AlaOpenflowLogicalSwitch_Type.__name__ = "SnmpAdminString"
_AlaOpenflowLogicalSwitch_Object = MibTableColumn
alaOpenflowLogicalSwitch = _AlaOpenflowLogicalSwitch_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 70, 1, 1, 2, 1, 1),
    _AlaOpenflowLogicalSwitch_Type()
)
alaOpenflowLogicalSwitch.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaOpenflowLogicalSwitch.setStatus("current")


class _AlaOpenflowLogicalSwitchAdminState_Type(Integer32):
    """Custom type alaOpenflowLogicalSwitchAdminState based on Integer32"""
    defaultValue = 1

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


_AlaOpenflowLogicalSwitchAdminState_Type.__name__ = "Integer32"
_AlaOpenflowLogicalSwitchAdminState_Object = MibTableColumn
alaOpenflowLogicalSwitchAdminState = _AlaOpenflowLogicalSwitchAdminState_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 70, 1, 1, 2, 1, 2),
    _AlaOpenflowLogicalSwitchAdminState_Type()
)
alaOpenflowLogicalSwitchAdminState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaOpenflowLogicalSwitchAdminState.setStatus("current")


class _AlaOpenflowLogicalSwitchMode_Type(Integer32):
    """Custom type alaOpenflowLogicalSwitchMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("normal", 1),
          ("api", 2),
          ("pfcChannel", 3))
    )


_AlaOpenflowLogicalSwitchMode_Type.__name__ = "Integer32"
_AlaOpenflowLogicalSwitchMode_Object = MibTableColumn
alaOpenflowLogicalSwitchMode = _AlaOpenflowLogicalSwitchMode_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 70, 1, 1, 2, 1, 3),
    _AlaOpenflowLogicalSwitchMode_Type()
)
alaOpenflowLogicalSwitchMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaOpenflowLogicalSwitchMode.setStatus("current")


class _AlaOpenflowLogicalSwitchVersions_Type(Bits):
    """Custom type alaOpenflowLogicalSwitchVersions based on Bits"""
    defaultBinValue = "11"

    namedValues = NamedValues(
        *(("v1dot0", 0),
          ("v1dot3dot1", 1))
    )

_AlaOpenflowLogicalSwitchVersions_Type.__name__ = "Bits"
_AlaOpenflowLogicalSwitchVersions_Object = MibTableColumn
alaOpenflowLogicalSwitchVersions = _AlaOpenflowLogicalSwitchVersions_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 70, 1, 1, 2, 1, 4),
    _AlaOpenflowLogicalSwitchVersions_Type()
)
alaOpenflowLogicalSwitchVersions.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaOpenflowLogicalSwitchVersions.setStatus("current")


class _AlaOpenflowLogicalSwitchVlan_Type(Integer32):
    """Custom type alaOpenflowLogicalSwitchVlan based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(2, 4093),
    )


_AlaOpenflowLogicalSwitchVlan_Type.__name__ = "Integer32"
_AlaOpenflowLogicalSwitchVlan_Object = MibTableColumn
alaOpenflowLogicalSwitchVlan = _AlaOpenflowLogicalSwitchVlan_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 70, 1, 1, 2, 1, 5),
    _AlaOpenflowLogicalSwitchVlan_Type()
)
alaOpenflowLogicalSwitchVlan.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaOpenflowLogicalSwitchVlan.setStatus("current")


class _AlaOpenflowLogicalSwitchControllerCount_Type(Integer32):
    """Custom type alaOpenflowLogicalSwitchControllerCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_AlaOpenflowLogicalSwitchControllerCount_Type.__name__ = "Integer32"
_AlaOpenflowLogicalSwitchControllerCount_Object = MibTableColumn
alaOpenflowLogicalSwitchControllerCount = _AlaOpenflowLogicalSwitchControllerCount_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 70, 1, 1, 2, 1, 6),
    _AlaOpenflowLogicalSwitchControllerCount_Type()
)
alaOpenflowLogicalSwitchControllerCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaOpenflowLogicalSwitchControllerCount.setStatus("current")


class _AlaOpenflowLogicalSwitchInterfaceCount_Type(Integer32):
    """Custom type alaOpenflowLogicalSwitchInterfaceCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5000),
    )


_AlaOpenflowLogicalSwitchInterfaceCount_Type.__name__ = "Integer32"
_AlaOpenflowLogicalSwitchInterfaceCount_Object = MibTableColumn
alaOpenflowLogicalSwitchInterfaceCount = _AlaOpenflowLogicalSwitchInterfaceCount_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 70, 1, 1, 2, 1, 7),
    _AlaOpenflowLogicalSwitchInterfaceCount_Type()
)
alaOpenflowLogicalSwitchInterfaceCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaOpenflowLogicalSwitchInterfaceCount.setStatus("current")


class _AlaOpenflowLogicalSwitchFlowCount_Type(Integer32):
    """Custom type alaOpenflowLogicalSwitchFlowCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 511),
    )


_AlaOpenflowLogicalSwitchFlowCount_Type.__name__ = "Integer32"
_AlaOpenflowLogicalSwitchFlowCount_Object = MibTableColumn
alaOpenflowLogicalSwitchFlowCount = _AlaOpenflowLogicalSwitchFlowCount_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 70, 1, 1, 2, 1, 8),
    _AlaOpenflowLogicalSwitchFlowCount_Type()
)
alaOpenflowLogicalSwitchFlowCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaOpenflowLogicalSwitchFlowCount.setStatus("current")
_AlaOpenflowLogicalSwitchRowStatus_Type = RowStatus
_AlaOpenflowLogicalSwitchRowStatus_Object = MibTableColumn
alaOpenflowLogicalSwitchRowStatus = _AlaOpenflowLogicalSwitchRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 70, 1, 1, 2, 1, 9),
    _AlaOpenflowLogicalSwitchRowStatus_Type()
)
alaOpenflowLogicalSwitchRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaOpenflowLogicalSwitchRowStatus.setStatus("current")


class _AlaOpenflowLogicalSwitchLearnedMacUpdate_Type(Integer32):
    """Custom type alaOpenflowLogicalSwitchLearnedMacUpdate based on Integer32"""
    defaultValue = 2

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


_AlaOpenflowLogicalSwitchLearnedMacUpdate_Type.__name__ = "Integer32"
_AlaOpenflowLogicalSwitchLearnedMacUpdate_Object = MibTableColumn
alaOpenflowLogicalSwitchLearnedMacUpdate = _AlaOpenflowLogicalSwitchLearnedMacUpdate_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 70, 1, 1, 2, 1, 10),
    _AlaOpenflowLogicalSwitchLearnedMacUpdate_Type()
)
alaOpenflowLogicalSwitchLearnedMacUpdate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaOpenflowLogicalSwitchLearnedMacUpdate.setStatus("current")


class _AlaOpenflowLogicalSwitchProbeTime_Type(Integer32):
    """Custom type alaOpenflowLogicalSwitchProbeTime based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 60),
    )


_AlaOpenflowLogicalSwitchProbeTime_Type.__name__ = "Integer32"
_AlaOpenflowLogicalSwitchProbeTime_Object = MibTableColumn
alaOpenflowLogicalSwitchProbeTime = _AlaOpenflowLogicalSwitchProbeTime_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 70, 1, 1, 2, 1, 11),
    _AlaOpenflowLogicalSwitchProbeTime_Type()
)
alaOpenflowLogicalSwitchProbeTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaOpenflowLogicalSwitchProbeTime.setStatus("current")


class _AlaOpenflowLogicalSwitchFailureDetectTime_Type(Integer32):
    """Custom type alaOpenflowLogicalSwitchFailureDetectTime based on Integer32"""
    defaultValue = 4

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 60),
    )


_AlaOpenflowLogicalSwitchFailureDetectTime_Type.__name__ = "Integer32"
_AlaOpenflowLogicalSwitchFailureDetectTime_Object = MibTableColumn
alaOpenflowLogicalSwitchFailureDetectTime = _AlaOpenflowLogicalSwitchFailureDetectTime_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 70, 1, 1, 2, 1, 12),
    _AlaOpenflowLogicalSwitchFailureDetectTime_Type()
)
alaOpenflowLogicalSwitchFailureDetectTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaOpenflowLogicalSwitchFailureDetectTime.setStatus("current")


class _AlaOpenflowLogicalSwitchDPID_Type(OctetString):
    """Custom type alaOpenflowLogicalSwitchDPID based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )
    fixed_length = 8


_AlaOpenflowLogicalSwitchDPID_Type.__name__ = "OctetString"
_AlaOpenflowLogicalSwitchDPID_Object = MibTableColumn
alaOpenflowLogicalSwitchDPID = _AlaOpenflowLogicalSwitchDPID_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 70, 1, 1, 2, 1, 13),
    _AlaOpenflowLogicalSwitchDPID_Type()
)
alaOpenflowLogicalSwitchDPID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaOpenflowLogicalSwitchDPID.setStatus("current")


class _AlaOpenflowLogicalSwitchTableMissAction_Type(Integer32):
    """Custom type alaOpenflowLogicalSwitchTableMissAction based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("drop", 1),
          ("controller", 2))
    )


_AlaOpenflowLogicalSwitchTableMissAction_Type.__name__ = "Integer32"
_AlaOpenflowLogicalSwitchTableMissAction_Object = MibTableColumn
alaOpenflowLogicalSwitchTableMissAction = _AlaOpenflowLogicalSwitchTableMissAction_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 70, 1, 1, 2, 1, 14),
    _AlaOpenflowLogicalSwitchTableMissAction_Type()
)
alaOpenflowLogicalSwitchTableMissAction.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaOpenflowLogicalSwitchTableMissAction.setStatus("current")


class _AlaOpenflowLogicalSwitchTCPBufferSizeTx_Type(Unsigned32):
    """Custom type alaOpenflowLogicalSwitchTCPBufferSizeTx based on Unsigned32"""
    defaultValue = 2

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 32),
    )


_AlaOpenflowLogicalSwitchTCPBufferSizeTx_Type.__name__ = "Unsigned32"
_AlaOpenflowLogicalSwitchTCPBufferSizeTx_Object = MibTableColumn
alaOpenflowLogicalSwitchTCPBufferSizeTx = _AlaOpenflowLogicalSwitchTCPBufferSizeTx_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 70, 1, 1, 2, 1, 15),
    _AlaOpenflowLogicalSwitchTCPBufferSizeTx_Type()
)
alaOpenflowLogicalSwitchTCPBufferSizeTx.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaOpenflowLogicalSwitchTCPBufferSizeTx.setStatus("current")
if mibBuilder.loadTexts:
    alaOpenflowLogicalSwitchTCPBufferSizeTx.setUnits("Kilo Bytes")


class _AlaOpenflowLogicalSwitchTCPBufferSizeRx_Type(Unsigned32):
    """Custom type alaOpenflowLogicalSwitchTCPBufferSizeRx based on Unsigned32"""
    defaultValue = 2

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 32),
    )


_AlaOpenflowLogicalSwitchTCPBufferSizeRx_Type.__name__ = "Unsigned32"
_AlaOpenflowLogicalSwitchTCPBufferSizeRx_Object = MibTableColumn
alaOpenflowLogicalSwitchTCPBufferSizeRx = _AlaOpenflowLogicalSwitchTCPBufferSizeRx_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 70, 1, 1, 2, 1, 16),
    _AlaOpenflowLogicalSwitchTCPBufferSizeRx_Type()
)
alaOpenflowLogicalSwitchTCPBufferSizeRx.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaOpenflowLogicalSwitchTCPBufferSizeRx.setStatus("current")
if mibBuilder.loadTexts:
    alaOpenflowLogicalSwitchTCPBufferSizeRx.setUnits("Kilo Bytes")
_AlaOpenflowControllerTable_Object = MibTable
alaOpenflowControllerTable = _AlaOpenflowControllerTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 70, 1, 1, 3)
)
if mibBuilder.loadTexts:
    alaOpenflowControllerTable.setStatus("current")
_AlaOpenflowControllerEntry_Object = MibTableRow
alaOpenflowControllerEntry = _AlaOpenflowControllerEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 70, 1, 1, 3, 1)
)
alaOpenflowControllerEntry.setIndexNames(
    (0, "ALCATEL-IND1-OPENFLOW-MIB", "alaOpenflowControllerLogicalSwitch"),
    (0, "ALCATEL-IND1-OPENFLOW-MIB", "alaOpenflowControllerIpType"),
    (0, "ALCATEL-IND1-OPENFLOW-MIB", "alaOpenflowControllerIp"),
    (0, "ALCATEL-IND1-OPENFLOW-MIB", "alaOpenflowControllerPort"),
)
if mibBuilder.loadTexts:
    alaOpenflowControllerEntry.setStatus("current")


class _AlaOpenflowControllerLogicalSwitch_Type(SnmpAdminString):
    """Custom type alaOpenflowControllerLogicalSwitch based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_AlaOpenflowControllerLogicalSwitch_Type.__name__ = "SnmpAdminString"
_AlaOpenflowControllerLogicalSwitch_Object = MibTableColumn
alaOpenflowControllerLogicalSwitch = _AlaOpenflowControllerLogicalSwitch_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 70, 1, 1, 3, 1, 1),
    _AlaOpenflowControllerLogicalSwitch_Type()
)
alaOpenflowControllerLogicalSwitch.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaOpenflowControllerLogicalSwitch.setStatus("current")


class _AlaOpenflowControllerIpType_Type(InetAddressType):
    """Custom type alaOpenflowControllerIpType based on InetAddressType"""
    subtypeSpec = InetAddressType.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              16)
        )
    )
    namedValues = NamedValues(
        *(("ipv4", 1),
          ("dns", 16))
    )


_AlaOpenflowControllerIpType_Type.__name__ = "InetAddressType"
_AlaOpenflowControllerIpType_Object = MibTableColumn
alaOpenflowControllerIpType = _AlaOpenflowControllerIpType_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 70, 1, 1, 3, 1, 2),
    _AlaOpenflowControllerIpType_Type()
)
alaOpenflowControllerIpType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaOpenflowControllerIpType.setStatus("current")


class _AlaOpenflowControllerIp_Type(InetAddress):
    """Custom type alaOpenflowControllerIp based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_AlaOpenflowControllerIp_Type.__name__ = "InetAddress"
_AlaOpenflowControllerIp_Object = MibTableColumn
alaOpenflowControllerIp = _AlaOpenflowControllerIp_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 70, 1, 1, 3, 1, 3),
    _AlaOpenflowControllerIp_Type()
)
alaOpenflowControllerIp.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaOpenflowControllerIp.setStatus("current")


class _AlaOpenflowControllerPort_Type(Integer32):
    """Custom type alaOpenflowControllerPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_AlaOpenflowControllerPort_Type.__name__ = "Integer32"
_AlaOpenflowControllerPort_Object = MibTableColumn
alaOpenflowControllerPort = _AlaOpenflowControllerPort_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 70, 1, 1, 3, 1, 4),
    _AlaOpenflowControllerPort_Type()
)
alaOpenflowControllerPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaOpenflowControllerPort.setStatus("current")


class _AlaOpenflowControllerRole_Type(Integer32):
    """Custom type alaOpenflowControllerRole based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("equal", 1),
          ("master", 2),
          ("slave", 3))
    )


_AlaOpenflowControllerRole_Type.__name__ = "Integer32"
_AlaOpenflowControllerRole_Object = MibTableColumn
alaOpenflowControllerRole = _AlaOpenflowControllerRole_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 70, 1, 1, 3, 1, 5),
    _AlaOpenflowControllerRole_Type()
)
alaOpenflowControllerRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaOpenflowControllerRole.setStatus("current")


class _AlaOpenflowControllerAdminState_Type(Integer32):
    """Custom type alaOpenflowControllerAdminState based on Integer32"""
    defaultValue = 1

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


_AlaOpenflowControllerAdminState_Type.__name__ = "Integer32"
_AlaOpenflowControllerAdminState_Object = MibTableColumn
alaOpenflowControllerAdminState = _AlaOpenflowControllerAdminState_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 70, 1, 1, 3, 1, 6),
    _AlaOpenflowControllerAdminState_Type()
)
alaOpenflowControllerAdminState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaOpenflowControllerAdminState.setStatus("current")


class _AlaOpenflowControllerOperState_Type(Integer32):
    """Custom type alaOpenflowControllerOperState based on Integer32"""
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
        *(("invalid", 1),
          ("disabled", 2),
          ("sendError", 3),
          ("init", 4),
          ("connecting", 5),
          ("backoff", 6),
          ("exchangingHello", 7),
          ("active", 8),
          ("idle", 9),
          ("disconnected", 10))
    )


_AlaOpenflowControllerOperState_Type.__name__ = "Integer32"
_AlaOpenflowControllerOperState_Object = MibTableColumn
alaOpenflowControllerOperState = _AlaOpenflowControllerOperState_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 70, 1, 1, 3, 1, 7),
    _AlaOpenflowControllerOperState_Type()
)
alaOpenflowControllerOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaOpenflowControllerOperState.setStatus("current")
_AlaOpenflowControllerRowStatus_Type = RowStatus
_AlaOpenflowControllerRowStatus_Object = MibTableColumn
alaOpenflowControllerRowStatus = _AlaOpenflowControllerRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 70, 1, 1, 3, 1, 8),
    _AlaOpenflowControllerRowStatus_Type()
)
alaOpenflowControllerRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaOpenflowControllerRowStatus.setStatus("current")


class _AlaOpenflowControllerPriority_Type(Integer32):
    """Custom type alaOpenflowControllerPriority based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_AlaOpenflowControllerPriority_Type.__name__ = "Integer32"
_AlaOpenflowControllerPriority_Object = MibTableColumn
alaOpenflowControllerPriority = _AlaOpenflowControllerPriority_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 70, 1, 1, 3, 1, 9),
    _AlaOpenflowControllerPriority_Type()
)
alaOpenflowControllerPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaOpenflowControllerPriority.setStatus("current")
_AlaOpenflowInterfaceTable_Object = MibTable
alaOpenflowInterfaceTable = _AlaOpenflowInterfaceTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 70, 1, 1, 4)
)
if mibBuilder.loadTexts:
    alaOpenflowInterfaceTable.setStatus("current")
_AlaOpenflowInterfaceEntry_Object = MibTableRow
alaOpenflowInterfaceEntry = _AlaOpenflowInterfaceEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 70, 1, 1, 4, 1)
)
alaOpenflowInterfaceEntry.setIndexNames(
    (0, "ALCATEL-IND1-OPENFLOW-MIB", "alaOpenflowInterfaceLogicalSwitch"),
    (0, "ALCATEL-IND1-OPENFLOW-MIB", "alaOpenflowInterface"),
)
if mibBuilder.loadTexts:
    alaOpenflowInterfaceEntry.setStatus("current")


class _AlaOpenflowInterfaceLogicalSwitch_Type(SnmpAdminString):
    """Custom type alaOpenflowInterfaceLogicalSwitch based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_AlaOpenflowInterfaceLogicalSwitch_Type.__name__ = "SnmpAdminString"
_AlaOpenflowInterfaceLogicalSwitch_Object = MibTableColumn
alaOpenflowInterfaceLogicalSwitch = _AlaOpenflowInterfaceLogicalSwitch_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 70, 1, 1, 4, 1, 1),
    _AlaOpenflowInterfaceLogicalSwitch_Type()
)
alaOpenflowInterfaceLogicalSwitch.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaOpenflowInterfaceLogicalSwitch.setStatus("current")


class _AlaOpenflowInterface_Type(Integer32):
    """Custom type alaOpenflowInterface based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_AlaOpenflowInterface_Type.__name__ = "Integer32"
_AlaOpenflowInterface_Object = MibTableColumn
alaOpenflowInterface = _AlaOpenflowInterface_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 70, 1, 1, 4, 1, 2),
    _AlaOpenflowInterface_Type()
)
alaOpenflowInterface.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaOpenflowInterface.setStatus("current")


class _AlaOpenflowInterfaceMode_Type(Integer32):
    """Custom type alaOpenflowInterfaceMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("normal", 1),
          ("api", 2),
          ("pfcChannel", 3))
    )


_AlaOpenflowInterfaceMode_Type.__name__ = "Integer32"
_AlaOpenflowInterfaceMode_Object = MibTableColumn
alaOpenflowInterfaceMode = _AlaOpenflowInterfaceMode_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 70, 1, 1, 4, 1, 3),
    _AlaOpenflowInterfaceMode_Type()
)
alaOpenflowInterfaceMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaOpenflowInterfaceMode.setStatus("current")
_AlaOpenflowInterfaceRowStatus_Type = RowStatus
_AlaOpenflowInterfaceRowStatus_Object = MibTableColumn
alaOpenflowInterfaceRowStatus = _AlaOpenflowInterfaceRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 70, 1, 1, 4, 1, 4),
    _AlaOpenflowInterfaceRowStatus_Type()
)
alaOpenflowInterfaceRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaOpenflowInterfaceRowStatus.setStatus("current")


class _AlaOpenflowInterfaceType_Type(Integer32):
    """Custom type alaOpenflowInterfaceType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("trunk", 1),
          ("access", 2))
    )


_AlaOpenflowInterfaceType_Type.__name__ = "Integer32"
_AlaOpenflowInterfaceType_Object = MibTableColumn
alaOpenflowInterfaceType = _AlaOpenflowInterfaceType_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 70, 1, 1, 4, 1, 5),
    _AlaOpenflowInterfaceType_Type()
)
alaOpenflowInterfaceType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaOpenflowInterfaceType.setStatus("current")


class _AlaOpenflowInterfaceNativeVlan_Type(Unsigned32):
    """Custom type alaOpenflowInterfaceNativeVlan based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 4093),
    )


_AlaOpenflowInterfaceNativeVlan_Type.__name__ = "Unsigned32"
_AlaOpenflowInterfaceNativeVlan_Object = MibTableColumn
alaOpenflowInterfaceNativeVlan = _AlaOpenflowInterfaceNativeVlan_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 70, 1, 1, 4, 1, 6),
    _AlaOpenflowInterfaceNativeVlan_Type()
)
alaOpenflowInterfaceNativeVlan.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaOpenflowInterfaceNativeVlan.setStatus("current")
_AlaOpenflowInterfaceVlanTable_Object = MibTable
alaOpenflowInterfaceVlanTable = _AlaOpenflowInterfaceVlanTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 70, 1, 1, 5)
)
if mibBuilder.loadTexts:
    alaOpenflowInterfaceVlanTable.setStatus("current")
_AlaOpenflowInterfaceVlanEntry_Object = MibTableRow
alaOpenflowInterfaceVlanEntry = _AlaOpenflowInterfaceVlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 70, 1, 1, 5, 1)
)
alaOpenflowInterfaceVlanEntry.setIndexNames(
    (0, "ALCATEL-IND1-OPENFLOW-MIB", "alaOpenflowInterfaceLogicalSwitch"),
    (0, "ALCATEL-IND1-OPENFLOW-MIB", "alaOpenflowInterface"),
    (0, "ALCATEL-IND1-OPENFLOW-MIB", "alaOpenflowInterfaceVlanVlanID"),
)
if mibBuilder.loadTexts:
    alaOpenflowInterfaceVlanEntry.setStatus("current")


class _AlaOpenflowInterfaceVlanVlanID_Type(Unsigned32):
    """Custom type alaOpenflowInterfaceVlanVlanID based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(2, 4093),
    )


_AlaOpenflowInterfaceVlanVlanID_Type.__name__ = "Unsigned32"
_AlaOpenflowInterfaceVlanVlanID_Object = MibTableColumn
alaOpenflowInterfaceVlanVlanID = _AlaOpenflowInterfaceVlanVlanID_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 70, 1, 1, 5, 1, 1),
    _AlaOpenflowInterfaceVlanVlanID_Type()
)
alaOpenflowInterfaceVlanVlanID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaOpenflowInterfaceVlanVlanID.setStatus("current")
_AlaOpenflowInterfaceVlanRowStatus_Type = RowStatus
_AlaOpenflowInterfaceVlanRowStatus_Object = MibTableColumn
alaOpenflowInterfaceVlanRowStatus = _AlaOpenflowInterfaceVlanRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 70, 1, 1, 5, 1, 2),
    _AlaOpenflowInterfaceVlanRowStatus_Type()
)
alaOpenflowInterfaceVlanRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaOpenflowInterfaceVlanRowStatus.setStatus("current")
_AlcatelIND1OpenflowMIBConformance_ObjectIdentity = ObjectIdentity
alcatelIND1OpenflowMIBConformance = _AlcatelIND1OpenflowMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 70, 1, 2)
)
if mibBuilder.loadTexts:
    alcatelIND1OpenflowMIBConformance.setStatus("current")
_AlcatelIND1OpenflowMIBGroups_ObjectIdentity = ObjectIdentity
alcatelIND1OpenflowMIBGroups = _AlcatelIND1OpenflowMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 70, 1, 2, 1)
)
if mibBuilder.loadTexts:
    alcatelIND1OpenflowMIBGroups.setStatus("current")
_AlcatelIND1OpenflowMIBCompliances_ObjectIdentity = ObjectIdentity
alcatelIND1OpenflowMIBCompliances = _AlcatelIND1OpenflowMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 70, 1, 2, 2)
)
if mibBuilder.loadTexts:
    alcatelIND1OpenflowMIBCompliances.setStatus("current")

# Managed Objects groups

alaOpenflowModuleConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 70, 1, 2, 1, 1)
)
alaOpenflowModuleConfigGroup.setObjects(
      *(("ALCATEL-IND1-OPENFLOW-MIB", "alaOpenflowGlobalBackoffMax"),
        ("ALCATEL-IND1-OPENFLOW-MIB", "alaOpenflowGlobalIdleProbeTimeout"))
)
if mibBuilder.loadTexts:
    alaOpenflowModuleConfigGroup.setStatus("current")

alaOpenflowModuleLogicalSwitchGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 70, 1, 2, 1, 2)
)
alaOpenflowModuleLogicalSwitchGroup.setObjects(
      *(("ALCATEL-IND1-OPENFLOW-MIB", "alaOpenflowLogicalSwitchAdminState"),
        ("ALCATEL-IND1-OPENFLOW-MIB", "alaOpenflowLogicalSwitchMode"),
        ("ALCATEL-IND1-OPENFLOW-MIB", "alaOpenflowLogicalSwitchVersions"),
        ("ALCATEL-IND1-OPENFLOW-MIB", "alaOpenflowLogicalSwitchVlan"),
        ("ALCATEL-IND1-OPENFLOW-MIB", "alaOpenflowLogicalSwitchControllerCount"),
        ("ALCATEL-IND1-OPENFLOW-MIB", "alaOpenflowLogicalSwitchInterfaceCount"),
        ("ALCATEL-IND1-OPENFLOW-MIB", "alaOpenflowLogicalSwitchFlowCount"),
        ("ALCATEL-IND1-OPENFLOW-MIB", "alaOpenflowLogicalSwitchRowStatus"),
        ("ALCATEL-IND1-OPENFLOW-MIB", "alaOpenflowLogicalSwitchLearnedMacUpdate"),
        ("ALCATEL-IND1-OPENFLOW-MIB", "alaOpenflowLogicalSwitchProbeTime"),
        ("ALCATEL-IND1-OPENFLOW-MIB", "alaOpenflowLogicalSwitchFailureDetectTime"),
        ("ALCATEL-IND1-OPENFLOW-MIB", "alaOpenflowLogicalSwitchDPID"),
        ("ALCATEL-IND1-OPENFLOW-MIB", "alaOpenflowLogicalSwitchTableMissAction"),
        ("ALCATEL-IND1-OPENFLOW-MIB", "alaOpenflowLogicalSwitchTCPBufferSizeTx"),
        ("ALCATEL-IND1-OPENFLOW-MIB", "alaOpenflowLogicalSwitchTCPBufferSizeRx"))
)
if mibBuilder.loadTexts:
    alaOpenflowModuleLogicalSwitchGroup.setStatus("current")

alaOpenflowModuleControllerGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 70, 1, 2, 1, 3)
)
alaOpenflowModuleControllerGroup.setObjects(
      *(("ALCATEL-IND1-OPENFLOW-MIB", "alaOpenflowControllerRole"),
        ("ALCATEL-IND1-OPENFLOW-MIB", "alaOpenflowControllerAdminState"),
        ("ALCATEL-IND1-OPENFLOW-MIB", "alaOpenflowControllerOperState"),
        ("ALCATEL-IND1-OPENFLOW-MIB", "alaOpenflowControllerRowStatus"),
        ("ALCATEL-IND1-OPENFLOW-MIB", "alaOpenflowControllerPriority"))
)
if mibBuilder.loadTexts:
    alaOpenflowModuleControllerGroup.setStatus("current")

alaOpenflowModuleInterfaceGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 70, 1, 2, 1, 4)
)
alaOpenflowModuleInterfaceGroup.setObjects(
      *(("ALCATEL-IND1-OPENFLOW-MIB", "alaOpenflowInterfaceMode"),
        ("ALCATEL-IND1-OPENFLOW-MIB", "alaOpenflowInterfaceRowStatus"),
        ("ALCATEL-IND1-OPENFLOW-MIB", "alaOpenflowInterfaceType"),
        ("ALCATEL-IND1-OPENFLOW-MIB", "alaOpenflowInterfaceNativeVlan"))
)
if mibBuilder.loadTexts:
    alaOpenflowModuleInterfaceGroup.setStatus("current")

alaOpenflowModuleInterfaceVlanGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 70, 1, 2, 1, 5)
)
alaOpenflowModuleInterfaceVlanGroup.setObjects(
    ("ALCATEL-IND1-OPENFLOW-MIB", "alaOpenflowInterfaceVlanRowStatus")
)
if mibBuilder.loadTexts:
    alaOpenflowModuleInterfaceVlanGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

alaOpenflowMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 70, 1, 2, 2, 1)
)
alaOpenflowMIBCompliance.setObjects(
      *(("ALCATEL-IND1-OPENFLOW-MIB", "alaOpenflowModuleConfigGroup"),
        ("ALCATEL-IND1-OPENFLOW-MIB", "alaOpenflowModuleLogicalSwitchGroup"),
        ("ALCATEL-IND1-OPENFLOW-MIB", "alaOpenflowModuleControllerGroup"),
        ("ALCATEL-IND1-OPENFLOW-MIB", "alaOpenflowModuleInterfaceGroup"),
        ("ALCATEL-IND1-OPENFLOW-MIB", "alaOpenflowModuleInterfaceVlanGroup"))
)
if mibBuilder.loadTexts:
    alaOpenflowMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ALCATEL-IND1-OPENFLOW-MIB",
    **{"alcatelIND1OpenflowMIB": alcatelIND1OpenflowMIB,
       "alcatelIND1OpenflowMIBNotifications": alcatelIND1OpenflowMIBNotifications,
       "alcatelIND1OpenflowMIBObjects": alcatelIND1OpenflowMIBObjects,
       "alaOpenflowGlobalConfigObjects": alaOpenflowGlobalConfigObjects,
       "alaOpenflowGlobalBackoffMax": alaOpenflowGlobalBackoffMax,
       "alaOpenflowGlobalIdleProbeTimeout": alaOpenflowGlobalIdleProbeTimeout,
       "alaOpenflowLogicalSwitchTable": alaOpenflowLogicalSwitchTable,
       "alaOpenflowLogicalSwitchEntry": alaOpenflowLogicalSwitchEntry,
       "alaOpenflowLogicalSwitch": alaOpenflowLogicalSwitch,
       "alaOpenflowLogicalSwitchAdminState": alaOpenflowLogicalSwitchAdminState,
       "alaOpenflowLogicalSwitchMode": alaOpenflowLogicalSwitchMode,
       "alaOpenflowLogicalSwitchVersions": alaOpenflowLogicalSwitchVersions,
       "alaOpenflowLogicalSwitchVlan": alaOpenflowLogicalSwitchVlan,
       "alaOpenflowLogicalSwitchControllerCount": alaOpenflowLogicalSwitchControllerCount,
       "alaOpenflowLogicalSwitchInterfaceCount": alaOpenflowLogicalSwitchInterfaceCount,
       "alaOpenflowLogicalSwitchFlowCount": alaOpenflowLogicalSwitchFlowCount,
       "alaOpenflowLogicalSwitchRowStatus": alaOpenflowLogicalSwitchRowStatus,
       "alaOpenflowLogicalSwitchLearnedMacUpdate": alaOpenflowLogicalSwitchLearnedMacUpdate,
       "alaOpenflowLogicalSwitchProbeTime": alaOpenflowLogicalSwitchProbeTime,
       "alaOpenflowLogicalSwitchFailureDetectTime": alaOpenflowLogicalSwitchFailureDetectTime,
       "alaOpenflowLogicalSwitchDPID": alaOpenflowLogicalSwitchDPID,
       "alaOpenflowLogicalSwitchTableMissAction": alaOpenflowLogicalSwitchTableMissAction,
       "alaOpenflowLogicalSwitchTCPBufferSizeTx": alaOpenflowLogicalSwitchTCPBufferSizeTx,
       "alaOpenflowLogicalSwitchTCPBufferSizeRx": alaOpenflowLogicalSwitchTCPBufferSizeRx,
       "alaOpenflowControllerTable": alaOpenflowControllerTable,
       "alaOpenflowControllerEntry": alaOpenflowControllerEntry,
       "alaOpenflowControllerLogicalSwitch": alaOpenflowControllerLogicalSwitch,
       "alaOpenflowControllerIpType": alaOpenflowControllerIpType,
       "alaOpenflowControllerIp": alaOpenflowControllerIp,
       "alaOpenflowControllerPort": alaOpenflowControllerPort,
       "alaOpenflowControllerRole": alaOpenflowControllerRole,
       "alaOpenflowControllerAdminState": alaOpenflowControllerAdminState,
       "alaOpenflowControllerOperState": alaOpenflowControllerOperState,
       "alaOpenflowControllerRowStatus": alaOpenflowControllerRowStatus,
       "alaOpenflowControllerPriority": alaOpenflowControllerPriority,
       "alaOpenflowInterfaceTable": alaOpenflowInterfaceTable,
       "alaOpenflowInterfaceEntry": alaOpenflowInterfaceEntry,
       "alaOpenflowInterfaceLogicalSwitch": alaOpenflowInterfaceLogicalSwitch,
       "alaOpenflowInterface": alaOpenflowInterface,
       "alaOpenflowInterfaceMode": alaOpenflowInterfaceMode,
       "alaOpenflowInterfaceRowStatus": alaOpenflowInterfaceRowStatus,
       "alaOpenflowInterfaceType": alaOpenflowInterfaceType,
       "alaOpenflowInterfaceNativeVlan": alaOpenflowInterfaceNativeVlan,
       "alaOpenflowInterfaceVlanTable": alaOpenflowInterfaceVlanTable,
       "alaOpenflowInterfaceVlanEntry": alaOpenflowInterfaceVlanEntry,
       "alaOpenflowInterfaceVlanVlanID": alaOpenflowInterfaceVlanVlanID,
       "alaOpenflowInterfaceVlanRowStatus": alaOpenflowInterfaceVlanRowStatus,
       "alcatelIND1OpenflowMIBConformance": alcatelIND1OpenflowMIBConformance,
       "alcatelIND1OpenflowMIBGroups": alcatelIND1OpenflowMIBGroups,
       "alaOpenflowModuleConfigGroup": alaOpenflowModuleConfigGroup,
       "alaOpenflowModuleLogicalSwitchGroup": alaOpenflowModuleLogicalSwitchGroup,
       "alaOpenflowModuleControllerGroup": alaOpenflowModuleControllerGroup,
       "alaOpenflowModuleInterfaceGroup": alaOpenflowModuleInterfaceGroup,
       "alaOpenflowModuleInterfaceVlanGroup": alaOpenflowModuleInterfaceVlanGroup,
       "alcatelIND1OpenflowMIBCompliances": alcatelIND1OpenflowMIBCompliances,
       "alaOpenflowMIBCompliance": alaOpenflowMIBCompliance}
)
