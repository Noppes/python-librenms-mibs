# SNMP MIB module (PRVT-MST-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\telco-systems\binos\PRVT-MST-MIB

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

(BridgeId,
 Timeout,
 dot1dBasePort,
 dot1dStpPortEntry) = mibBuilder.importSymbols(
    "BRIDGE-MIB",
    "BridgeId",
    "Timeout",
    "dot1dBasePort",
    "dot1dStpPortEntry")

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
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention",
    "TimeStamp",
    "TruthValue")


# MODULE-IDENTITY

prvtMSTMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 107)
)
if mibBuilder.loadTexts:
    prvtMSTMib.setRevisions(
        ("2005-02-16 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_PrvtMSTNotifications_ObjectIdentity = ObjectIdentity
prvtMSTNotifications = _PrvtMSTNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 107, 0)
)
_PrvtMSTObjects_ObjectIdentity = ObjectIdentity
prvtMSTObjects = _PrvtMSTObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 107, 1)
)
_MSTRegion_ObjectIdentity = ObjectIdentity
mSTRegion = _MSTRegion_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 107, 1, 1)
)
_MSTRegionEditControl_ObjectIdentity = ObjectIdentity
mSTRegionEditControl = _MSTRegionEditControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 107, 1, 1, 1)
)


class _MSTRegionEditBufferStatus_Type(Integer32):
    """Custom type mSTRegionEditBufferStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("released", 1),
          ("acquiredBySnmp", 2),
          ("acquiredByNonSnmp", 3))
    )


_MSTRegionEditBufferStatus_Type.__name__ = "Integer32"
_MSTRegionEditBufferStatus_Object = MibScalar
mSTRegionEditBufferStatus = _MSTRegionEditBufferStatus_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 107, 1, 1, 1, 1),
    _MSTRegionEditBufferStatus_Type()
)
mSTRegionEditBufferStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mSTRegionEditBufferStatus.setStatus("current")


class _MSTRegionEditBufferOperation_Type(Integer32):
    """Custom type mSTRegionEditBufferOperation based on Integer32"""
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
        *(("other", 1),
          ("acquire", 2),
          ("releaseWithForce", 3),
          ("commit", 4),
          ("rollBack", 5))
    )


_MSTRegionEditBufferOperation_Type.__name__ = "Integer32"
_MSTRegionEditBufferOperation_Object = MibScalar
mSTRegionEditBufferOperation = _MSTRegionEditBufferOperation_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 107, 1, 1, 1, 2),
    _MSTRegionEditBufferOperation_Type()
)
mSTRegionEditBufferOperation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mSTRegionEditBufferOperation.setStatus("current")
_MSTRegionParameters_ObjectIdentity = ObjectIdentity
mSTRegionParameters = _MSTRegionParameters_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 107, 1, 1, 2)
)


class _MSTRegionName_Type(DisplayString):
    """Custom type mSTRegionName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_MSTRegionName_Type.__name__ = "DisplayString"
_MSTRegionName_Object = MibScalar
mSTRegionName = _MSTRegionName_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 107, 1, 1, 2, 1),
    _MSTRegionName_Type()
)
mSTRegionName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mSTRegionName.setStatus("current")


class _MSTRegionEditName_Type(DisplayString):
    """Custom type mSTRegionEditName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_MSTRegionEditName_Type.__name__ = "DisplayString"
_MSTRegionEditName_Object = MibScalar
mSTRegionEditName = _MSTRegionEditName_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 107, 1, 1, 2, 2),
    _MSTRegionEditName_Type()
)
mSTRegionEditName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mSTRegionEditName.setStatus("current")


class _MSTRegionRevision_Type(Integer32):
    """Custom type mSTRegionRevision based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MSTRegionRevision_Type.__name__ = "Integer32"
_MSTRegionRevision_Object = MibScalar
mSTRegionRevision = _MSTRegionRevision_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 107, 1, 1, 2, 3),
    _MSTRegionRevision_Type()
)
mSTRegionRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mSTRegionRevision.setStatus("current")


class _MSTRegionEditRevision_Type(Integer32):
    """Custom type mSTRegionEditRevision based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MSTRegionEditRevision_Type.__name__ = "Integer32"
_MSTRegionEditRevision_Object = MibScalar
mSTRegionEditRevision = _MSTRegionEditRevision_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 107, 1, 1, 2, 4),
    _MSTRegionEditRevision_Type()
)
mSTRegionEditRevision.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mSTRegionEditRevision.setStatus("current")
_MSTInstanceVlanTable_Object = MibTable
mSTInstanceVlanTable = _MSTInstanceVlanTable_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 107, 1, 1, 2, 5)
)
if mibBuilder.loadTexts:
    mSTInstanceVlanTable.setStatus("current")
_MSTInstanceVlanEntry_Object = MibTableRow
mSTInstanceVlanEntry = _MSTInstanceVlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 107, 1, 1, 2, 5, 1)
)
mSTInstanceVlanEntry.setIndexNames(
    (0, "PRVT-MST-MIB", "mSTInstanceIndex"),
)
if mibBuilder.loadTexts:
    mSTInstanceVlanEntry.setStatus("current")


class _MSTInstanceIndex_Type(Integer32):
    """Custom type mSTInstanceIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 256),
    )


_MSTInstanceIndex_Type.__name__ = "Integer32"
_MSTInstanceIndex_Object = MibTableColumn
mSTInstanceIndex = _MSTInstanceIndex_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 107, 1, 1, 2, 5, 1, 1),
    _MSTInstanceIndex_Type()
)
mSTInstanceIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    mSTInstanceIndex.setStatus("current")


class _MSTInstanceVlansMapped_Type(OctetString):
    """Custom type mSTInstanceVlansMapped based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_MSTInstanceVlansMapped_Type.__name__ = "OctetString"
_MSTInstanceVlansMapped_Object = MibTableColumn
mSTInstanceVlansMapped = _MSTInstanceVlansMapped_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 107, 1, 1, 2, 5, 1, 2),
    _MSTInstanceVlansMapped_Type()
)
mSTInstanceVlansMapped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mSTInstanceVlansMapped.setStatus("current")


class _MSTInstanceVlansMapped2k_Type(OctetString):
    """Custom type mSTInstanceVlansMapped2k based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_MSTInstanceVlansMapped2k_Type.__name__ = "OctetString"
_MSTInstanceVlansMapped2k_Object = MibTableColumn
mSTInstanceVlansMapped2k = _MSTInstanceVlansMapped2k_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 107, 1, 1, 2, 5, 1, 3),
    _MSTInstanceVlansMapped2k_Type()
)
mSTInstanceVlansMapped2k.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mSTInstanceVlansMapped2k.setStatus("current")


class _MSTInstanceVlansMapped3k_Type(OctetString):
    """Custom type mSTInstanceVlansMapped3k based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_MSTInstanceVlansMapped3k_Type.__name__ = "OctetString"
_MSTInstanceVlansMapped3k_Object = MibTableColumn
mSTInstanceVlansMapped3k = _MSTInstanceVlansMapped3k_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 107, 1, 1, 2, 5, 1, 4),
    _MSTInstanceVlansMapped3k_Type()
)
mSTInstanceVlansMapped3k.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mSTInstanceVlansMapped3k.setStatus("current")


class _MSTInstanceVlansMapped4k_Type(OctetString):
    """Custom type mSTInstanceVlansMapped4k based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_MSTInstanceVlansMapped4k_Type.__name__ = "OctetString"
_MSTInstanceVlansMapped4k_Object = MibTableColumn
mSTInstanceVlansMapped4k = _MSTInstanceVlansMapped4k_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 107, 1, 1, 2, 5, 1, 5),
    _MSTInstanceVlansMapped4k_Type()
)
mSTInstanceVlansMapped4k.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mSTInstanceVlansMapped4k.setStatus("current")
_MSTInstanceVlanEditTable_Object = MibTable
mSTInstanceVlanEditTable = _MSTInstanceVlanEditTable_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 107, 1, 1, 2, 6)
)
if mibBuilder.loadTexts:
    mSTInstanceVlanEditTable.setStatus("current")
_MSTInstanceVlanEditEntry_Object = MibTableRow
mSTInstanceVlanEditEntry = _MSTInstanceVlanEditEntry_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 107, 1, 1, 2, 6, 1)
)
mSTInstanceVlanEditEntry.setIndexNames(
    (0, "PRVT-MST-MIB", "mSTInstanceIndex"),
)
if mibBuilder.loadTexts:
    mSTInstanceVlanEditEntry.setStatus("current")


class _MSTInstanceEditVlansMap_Type(OctetString):
    """Custom type mSTInstanceEditVlansMap based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_MSTInstanceEditVlansMap_Type.__name__ = "OctetString"
_MSTInstanceEditVlansMap_Object = MibTableColumn
mSTInstanceEditVlansMap = _MSTInstanceEditVlansMap_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 107, 1, 1, 2, 6, 1, 1),
    _MSTInstanceEditVlansMap_Type()
)
mSTInstanceEditVlansMap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mSTInstanceEditVlansMap.setStatus("current")


class _MSTInstanceEditVlansMap2k_Type(OctetString):
    """Custom type mSTInstanceEditVlansMap2k based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_MSTInstanceEditVlansMap2k_Type.__name__ = "OctetString"
_MSTInstanceEditVlansMap2k_Object = MibTableColumn
mSTInstanceEditVlansMap2k = _MSTInstanceEditVlansMap2k_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 107, 1, 1, 2, 6, 1, 2),
    _MSTInstanceEditVlansMap2k_Type()
)
mSTInstanceEditVlansMap2k.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mSTInstanceEditVlansMap2k.setStatus("current")


class _MSTInstanceEditVlansMap3k_Type(OctetString):
    """Custom type mSTInstanceEditVlansMap3k based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_MSTInstanceEditVlansMap3k_Type.__name__ = "OctetString"
_MSTInstanceEditVlansMap3k_Object = MibTableColumn
mSTInstanceEditVlansMap3k = _MSTInstanceEditVlansMap3k_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 107, 1, 1, 2, 6, 1, 3),
    _MSTInstanceEditVlansMap3k_Type()
)
mSTInstanceEditVlansMap3k.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mSTInstanceEditVlansMap3k.setStatus("current")


class _MSTInstanceEditVlansMap4k_Type(OctetString):
    """Custom type mSTInstanceEditVlansMap4k based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_MSTInstanceEditVlansMap4k_Type.__name__ = "OctetString"
_MSTInstanceEditVlansMap4k_Object = MibTableColumn
mSTInstanceEditVlansMap4k = _MSTInstanceEditVlansMap4k_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 107, 1, 1, 2, 6, 1, 4),
    _MSTInstanceEditVlansMap4k_Type()
)
mSTInstanceEditVlansMap4k.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mSTInstanceEditVlansMap4k.setStatus("current")
_MSTBridgeParams_ObjectIdentity = ObjectIdentity
mSTBridgeParams = _MSTBridgeParams_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 107, 1, 2)
)


class _MSTMaxHopCount_Type(Integer32):
    """Custom type mSTMaxHopCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 40),
    )


_MSTMaxHopCount_Type.__name__ = "Integer32"
_MSTMaxHopCount_Object = MibScalar
mSTMaxHopCount = _MSTMaxHopCount_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 107, 1, 2, 1),
    _MSTMaxHopCount_Type()
)
mSTMaxHopCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mSTMaxHopCount.setStatus("current")


class _MSTMaxInstanceNumber_Type(Integer32):
    """Custom type mSTMaxInstanceNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 256),
    )


_MSTMaxInstanceNumber_Type.__name__ = "Integer32"
_MSTMaxInstanceNumber_Object = MibScalar
mSTMaxInstanceNumber = _MSTMaxInstanceNumber_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 107, 1, 2, 2),
    _MSTMaxInstanceNumber_Type()
)
mSTMaxInstanceNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mSTMaxInstanceNumber.setStatus("current")
_MSTInstanceTable_Object = MibTable
mSTInstanceTable = _MSTInstanceTable_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 107, 1, 2, 3)
)
if mibBuilder.loadTexts:
    mSTInstanceTable.setStatus("current")
_MSTInstanceEntry_Object = MibTableRow
mSTInstanceEntry = _MSTInstanceEntry_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 107, 1, 2, 3, 1)
)
mSTInstanceEntry.setIndexNames(
    (0, "PRVT-MST-MIB", "mSTInstanceIndex"),
)
if mibBuilder.loadTexts:
    mSTInstanceEntry.setStatus("current")
_MSTInstanceDesignatedRoot_Type = BridgeId
_MSTInstanceDesignatedRoot_Object = MibTableColumn
mSTInstanceDesignatedRoot = _MSTInstanceDesignatedRoot_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 107, 1, 2, 3, 1, 1),
    _MSTInstanceDesignatedRoot_Type()
)
mSTInstanceDesignatedRoot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mSTInstanceDesignatedRoot.setStatus("current")
_MSTInstanceRootCost_Type = Integer32
_MSTInstanceRootCost_Object = MibTableColumn
mSTInstanceRootCost = _MSTInstanceRootCost_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 107, 1, 2, 3, 1, 2),
    _MSTInstanceRootCost_Type()
)
mSTInstanceRootCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mSTInstanceRootCost.setStatus("current")
_MSTInstanceRootPort_Type = Integer32
_MSTInstanceRootPort_Object = MibTableColumn
mSTInstanceRootPort = _MSTInstanceRootPort_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 107, 1, 2, 3, 1, 3),
    _MSTInstanceRootPort_Type()
)
mSTInstanceRootPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mSTInstanceRootPort.setStatus("current")
_MSTInstanceDesignatedBridge_Type = BridgeId
_MSTInstanceDesignatedBridge_Object = MibTableColumn
mSTInstanceDesignatedBridge = _MSTInstanceDesignatedBridge_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 107, 1, 2, 3, 1, 4),
    _MSTInstanceDesignatedBridge_Type()
)
mSTInstanceDesignatedBridge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mSTInstanceDesignatedBridge.setStatus("current")
_MSTInstanceRootPriority_Type = Integer32
_MSTInstanceRootPriority_Object = MibTableColumn
mSTInstanceRootPriority = _MSTInstanceRootPriority_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 107, 1, 2, 3, 1, 5),
    _MSTInstanceRootPriority_Type()
)
mSTInstanceRootPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mSTInstanceRootPriority.setStatus("current")


class _MSTInstanceRemainingHopCount_Type(Integer32):
    """Custom type mSTInstanceRemainingHopCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 40),
    )


_MSTInstanceRemainingHopCount_Type.__name__ = "Integer32"
_MSTInstanceRemainingHopCount_Object = MibTableColumn
mSTInstanceRemainingHopCount = _MSTInstanceRemainingHopCount_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 107, 1, 2, 3, 1, 6),
    _MSTInstanceRemainingHopCount_Type()
)
mSTInstanceRemainingHopCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mSTInstanceRemainingHopCount.setStatus("current")


class _MSTInstancePriority_Type(Integer32):
    """Custom type mSTInstancePriority based on Integer32"""
    defaultValue = 32768

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 61440),
    )


_MSTInstancePriority_Type.__name__ = "Integer32"
_MSTInstancePriority_Object = MibTableColumn
mSTInstancePriority = _MSTInstancePriority_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 107, 1, 2, 3, 1, 7),
    _MSTInstancePriority_Type()
)
mSTInstancePriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mSTInstancePriority.setStatus("current")
_MSTTimers_ObjectIdentity = ObjectIdentity
mSTTimers = _MSTTimers_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 107, 1, 3)
)
_MSTMigrationTimer_Type = Integer32
_MSTMigrationTimer_Object = MibScalar
mSTMigrationTimer = _MSTMigrationTimer_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 107, 1, 3, 1),
    _MSTMigrationTimer_Type()
)
mSTMigrationTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mSTMigrationTimer.setStatus("current")
_MSTTxHoldCount_Type = Integer32
_MSTTxHoldCount_Object = MibScalar
mSTTxHoldCount = _MSTTxHoldCount_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 107, 1, 3, 2),
    _MSTTxHoldCount_Type()
)
mSTTxHoldCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mSTTxHoldCount.setStatus("current")


class _MSTMaxAge_Type(Timeout):
    """Custom type mSTMaxAge based on Timeout"""
    subtypeSpec = Timeout.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(600, 4000),
    )


_MSTMaxAge_Type.__name__ = "Timeout"
_MSTMaxAge_Object = MibScalar
mSTMaxAge = _MSTMaxAge_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 107, 1, 3, 3),
    _MSTMaxAge_Type()
)
mSTMaxAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mSTMaxAge.setStatus("current")


class _MSTHelloTime_Type(Timeout):
    """Custom type mSTHelloTime based on Timeout"""
    subtypeSpec = Timeout.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 1000),
    )


_MSTHelloTime_Type.__name__ = "Timeout"
_MSTHelloTime_Object = MibScalar
mSTHelloTime = _MSTHelloTime_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 107, 1, 3, 4),
    _MSTHelloTime_Type()
)
mSTHelloTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mSTHelloTime.setStatus("current")


class _MSTForwardDelay_Type(Timeout):
    """Custom type mSTForwardDelay based on Timeout"""
    subtypeSpec = Timeout.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(400, 3000),
    )


_MSTForwardDelay_Type.__name__ = "Timeout"
_MSTForwardDelay_Object = MibScalar
mSTForwardDelay = _MSTForwardDelay_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 107, 1, 3, 5),
    _MSTForwardDelay_Type()
)
mSTForwardDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mSTForwardDelay.setStatus("current")


class _MSTBridgeMaxAge_Type(Timeout):
    """Custom type mSTBridgeMaxAge based on Timeout"""
    subtypeSpec = Timeout.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(600, 4000),
    )


_MSTBridgeMaxAge_Type.__name__ = "Timeout"
_MSTBridgeMaxAge_Object = MibScalar
mSTBridgeMaxAge = _MSTBridgeMaxAge_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 107, 1, 3, 6),
    _MSTBridgeMaxAge_Type()
)
mSTBridgeMaxAge.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mSTBridgeMaxAge.setStatus("current")


class _MSTBridgeHelloTime_Type(Timeout):
    """Custom type mSTBridgeHelloTime based on Timeout"""
    subtypeSpec = Timeout.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 1000),
    )


_MSTBridgeHelloTime_Type.__name__ = "Timeout"
_MSTBridgeHelloTime_Object = MibScalar
mSTBridgeHelloTime = _MSTBridgeHelloTime_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 107, 1, 3, 7),
    _MSTBridgeHelloTime_Type()
)
mSTBridgeHelloTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mSTBridgeHelloTime.setStatus("current")


class _MSTBridgeForwardDelay_Type(Timeout):
    """Custom type mSTBridgeForwardDelay based on Timeout"""
    subtypeSpec = Timeout.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(400, 3000),
    )


_MSTBridgeForwardDelay_Type.__name__ = "Timeout"
_MSTBridgeForwardDelay_Object = MibScalar
mSTBridgeForwardDelay = _MSTBridgeForwardDelay_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 107, 1, 3, 8),
    _MSTBridgeForwardDelay_Type()
)
mSTBridgeForwardDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mSTBridgeForwardDelay.setStatus("current")
_MSTPort_ObjectIdentity = ObjectIdentity
mSTPort = _MSTPort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 107, 1, 4)
)
_MSTPortTable_Object = MibTable
mSTPortTable = _MSTPortTable_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 107, 1, 4, 1)
)
if mibBuilder.loadTexts:
    mSTPortTable.setStatus("current")
_MSTPortEntry_Object = MibTableRow
mSTPortEntry = _MSTPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 107, 1, 4, 1, 1)
)
mSTPortEntry.setIndexNames(
    (0, "BRIDGE-MIB", "dot1dBasePort"),
)
if mibBuilder.loadTexts:
    mSTPortEntry.setStatus("current")


class _MSTPortAdminLinkType_Type(Integer32):
    """Custom type mSTPortAdminLinkType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("pointToPoint", 1),
          ("shared", 2),
          ("auto", 3))
    )


_MSTPortAdminLinkType_Type.__name__ = "Integer32"
_MSTPortAdminLinkType_Object = MibTableColumn
mSTPortAdminLinkType = _MSTPortAdminLinkType_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 107, 1, 4, 1, 1, 1),
    _MSTPortAdminLinkType_Type()
)
mSTPortAdminLinkType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mSTPortAdminLinkType.setStatus("current")


class _MSTPortOperLinkType_Type(Integer32):
    """Custom type mSTPortOperLinkType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("pointToPoint", 1),
          ("shared", 2),
          ("other", 3))
    )


_MSTPortOperLinkType_Type.__name__ = "Integer32"
_MSTPortOperLinkType_Object = MibTableColumn
mSTPortOperLinkType = _MSTPortOperLinkType_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 107, 1, 4, 1, 1, 2),
    _MSTPortOperLinkType_Type()
)
mSTPortOperLinkType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mSTPortOperLinkType.setStatus("current")
_MSTPortProtocolMigration_Type = TruthValue
_MSTPortProtocolMigration_Object = MibTableColumn
mSTPortProtocolMigration = _MSTPortProtocolMigration_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 107, 1, 4, 1, 1, 3),
    _MSTPortProtocolMigration_Type()
)
mSTPortProtocolMigration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mSTPortProtocolMigration.setStatus("current")


class _MSTPortStatus_Type(Bits):
    """Custom type mSTPortStatus based on Bits"""
    namedValues = NamedValues(
        *(("edge", 0),
          ("boundary", 1),
          ("pvst", 2),
          ("stp", 3))
    )

_MSTPortStatus_Type.__name__ = "Bits"
_MSTPortStatus_Object = MibTableColumn
mSTPortStatus = _MSTPortStatus_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 107, 1, 4, 1, 1, 4),
    _MSTPortStatus_Type()
)
mSTPortStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mSTPortStatus.setStatus("current")
_MSTPortAdminEdgePort_Type = TruthValue
_MSTPortAdminEdgePort_Object = MibTableColumn
mSTPortAdminEdgePort = _MSTPortAdminEdgePort_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 107, 1, 4, 1, 1, 5),
    _MSTPortAdminEdgePort_Type()
)
mSTPortAdminEdgePort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mSTPortAdminEdgePort.setStatus("current")
_MSTPortOperEdgePort_Type = TruthValue
_MSTPortOperEdgePort_Object = MibTableColumn
mSTPortOperEdgePort = _MSTPortOperEdgePort_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 107, 1, 4, 1, 1, 6),
    _MSTPortOperEdgePort_Type()
)
mSTPortOperEdgePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mSTPortOperEdgePort.setStatus("current")


class _MSTPortEnable_Type(Integer32):
    """Custom type mSTPortEnable based on Integer32"""
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


_MSTPortEnable_Type.__name__ = "Integer32"
_MSTPortEnable_Object = MibTableColumn
mSTPortEnable = _MSTPortEnable_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 107, 1, 4, 1, 1, 7),
    _MSTPortEnable_Type()
)
mSTPortEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mSTPortEnable.setStatus("current")
_MSTPortPerMstTable_Object = MibTable
mSTPortPerMstTable = _MSTPortPerMstTable_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 107, 1, 4, 2)
)
if mibBuilder.loadTexts:
    mSTPortPerMstTable.setStatus("current")
_MSTPortPerMstEntry_Object = MibTableRow
mSTPortPerMstEntry = _MSTPortPerMstEntry_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 107, 1, 4, 2, 1)
)
mSTPortPerMstEntry.setIndexNames(
    (0, "PRVT-MST-MIB", "mSTInstanceIndex"),
    (0, "BRIDGE-MIB", "dot1dBasePort"),
)
if mibBuilder.loadTexts:
    mSTPortPerMstEntry.setStatus("current")


class _MSTPortPerMstRoleValue_Type(Integer32):
    """Custom type mSTPortPerMstRoleValue based on Integer32"""
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
        *(("disabled", 1),
          ("root", 2),
          ("designated", 3),
          ("alternate", 4),
          ("backUp", 5),
          ("boundary", 6))
    )


_MSTPortPerMstRoleValue_Type.__name__ = "Integer32"
_MSTPortPerMstRoleValue_Object = MibTableColumn
mSTPortPerMstRoleValue = _MSTPortPerMstRoleValue_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 107, 1, 4, 2, 1, 1),
    _MSTPortPerMstRoleValue_Type()
)
mSTPortPerMstRoleValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mSTPortPerMstRoleValue.setStatus("current")


class _MSTPortPerMstPriority_Type(Integer32):
    """Custom type mSTPortPerMstPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_MSTPortPerMstPriority_Type.__name__ = "Integer32"
_MSTPortPerMstPriority_Object = MibTableColumn
mSTPortPerMstPriority = _MSTPortPerMstPriority_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 107, 1, 4, 2, 1, 2),
    _MSTPortPerMstPriority_Type()
)
mSTPortPerMstPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mSTPortPerMstPriority.setStatus("current")


class _MSTPortPerMstState_Type(Integer32):
    """Custom type mSTPortPerMstState based on Integer32"""
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
        *(("disabled", 1),
          ("blocking", 2),
          ("listening", 3),
          ("learning", 4),
          ("forwarding", 5),
          ("broken", 6))
    )


_MSTPortPerMstState_Type.__name__ = "Integer32"
_MSTPortPerMstState_Object = MibTableColumn
mSTPortPerMstState = _MSTPortPerMstState_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 107, 1, 4, 2, 1, 3),
    _MSTPortPerMstState_Type()
)
mSTPortPerMstState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mSTPortPerMstState.setStatus("current")


class _MSTPortPerMstPathCost_Type(Integer32):
    """Custom type mSTPortPerMstPathCost based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 200000000),
    )


_MSTPortPerMstPathCost_Type.__name__ = "Integer32"
_MSTPortPerMstPathCost_Object = MibTableColumn
mSTPortPerMstPathCost = _MSTPortPerMstPathCost_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 107, 1, 4, 2, 1, 4),
    _MSTPortPerMstPathCost_Type()
)
mSTPortPerMstPathCost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mSTPortPerMstPathCost.setStatus("current")
_MSTPortPerMstDesignatedCost_Type = Integer32
_MSTPortPerMstDesignatedCost_Object = MibTableColumn
mSTPortPerMstDesignatedCost = _MSTPortPerMstDesignatedCost_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 107, 1, 4, 2, 1, 5),
    _MSTPortPerMstDesignatedCost_Type()
)
mSTPortPerMstDesignatedCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mSTPortPerMstDesignatedCost.setStatus("current")
_MSTPortPerMstDesignatedBridge_Type = BridgeId
_MSTPortPerMstDesignatedBridge_Object = MibTableColumn
mSTPortPerMstDesignatedBridge = _MSTPortPerMstDesignatedBridge_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 107, 1, 4, 2, 1, 6),
    _MSTPortPerMstDesignatedBridge_Type()
)
mSTPortPerMstDesignatedBridge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mSTPortPerMstDesignatedBridge.setStatus("current")


class _MSTPortPerMstDesignatedPort_Type(OctetString):
    """Custom type mSTPortPerMstDesignatedPort based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )
    fixed_length = 2


_MSTPortPerMstDesignatedPort_Type.__name__ = "OctetString"
_MSTPortPerMstDesignatedPort_Object = MibTableColumn
mSTPortPerMstDesignatedPort = _MSTPortPerMstDesignatedPort_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 107, 1, 4, 2, 1, 7),
    _MSTPortPerMstDesignatedPort_Type()
)
mSTPortPerMstDesignatedPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mSTPortPerMstDesignatedPort.setStatus("current")

# Managed Objects groups


# Notification objects

mstpNewRoot = NotificationType(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 107, 0, 1)
)
mstpNewRoot.setObjects(
    ("PRVT-MST-MIB", "mSTInstanceIndex")
)
if mibBuilder.loadTexts:
    mstpNewRoot.setStatus(
        "current"
    )

mstpTopologyChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 107, 0, 2)
)
mstpTopologyChange.setObjects(
    ("PRVT-MST-MIB", "mSTInstanceIndex")
)
if mibBuilder.loadTexts:
    mstpTopologyChange.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "PRVT-MST-MIB",
    **{"prvtMSTMib": prvtMSTMib,
       "prvtMSTNotifications": prvtMSTNotifications,
       "mstpNewRoot": mstpNewRoot,
       "mstpTopologyChange": mstpTopologyChange,
       "prvtMSTObjects": prvtMSTObjects,
       "mSTRegion": mSTRegion,
       "mSTRegionEditControl": mSTRegionEditControl,
       "mSTRegionEditBufferStatus": mSTRegionEditBufferStatus,
       "mSTRegionEditBufferOperation": mSTRegionEditBufferOperation,
       "mSTRegionParameters": mSTRegionParameters,
       "mSTRegionName": mSTRegionName,
       "mSTRegionEditName": mSTRegionEditName,
       "mSTRegionRevision": mSTRegionRevision,
       "mSTRegionEditRevision": mSTRegionEditRevision,
       "mSTInstanceVlanTable": mSTInstanceVlanTable,
       "mSTInstanceVlanEntry": mSTInstanceVlanEntry,
       "mSTInstanceIndex": mSTInstanceIndex,
       "mSTInstanceVlansMapped": mSTInstanceVlansMapped,
       "mSTInstanceVlansMapped2k": mSTInstanceVlansMapped2k,
       "mSTInstanceVlansMapped3k": mSTInstanceVlansMapped3k,
       "mSTInstanceVlansMapped4k": mSTInstanceVlansMapped4k,
       "mSTInstanceVlanEditTable": mSTInstanceVlanEditTable,
       "mSTInstanceVlanEditEntry": mSTInstanceVlanEditEntry,
       "mSTInstanceEditVlansMap": mSTInstanceEditVlansMap,
       "mSTInstanceEditVlansMap2k": mSTInstanceEditVlansMap2k,
       "mSTInstanceEditVlansMap3k": mSTInstanceEditVlansMap3k,
       "mSTInstanceEditVlansMap4k": mSTInstanceEditVlansMap4k,
       "mSTBridgeParams": mSTBridgeParams,
       "mSTMaxHopCount": mSTMaxHopCount,
       "mSTMaxInstanceNumber": mSTMaxInstanceNumber,
       "mSTInstanceTable": mSTInstanceTable,
       "mSTInstanceEntry": mSTInstanceEntry,
       "mSTInstanceDesignatedRoot": mSTInstanceDesignatedRoot,
       "mSTInstanceRootCost": mSTInstanceRootCost,
       "mSTInstanceRootPort": mSTInstanceRootPort,
       "mSTInstanceDesignatedBridge": mSTInstanceDesignatedBridge,
       "mSTInstanceRootPriority": mSTInstanceRootPriority,
       "mSTInstanceRemainingHopCount": mSTInstanceRemainingHopCount,
       "mSTInstancePriority": mSTInstancePriority,
       "mSTTimers": mSTTimers,
       "mSTMigrationTimer": mSTMigrationTimer,
       "mSTTxHoldCount": mSTTxHoldCount,
       "mSTMaxAge": mSTMaxAge,
       "mSTHelloTime": mSTHelloTime,
       "mSTForwardDelay": mSTForwardDelay,
       "mSTBridgeMaxAge": mSTBridgeMaxAge,
       "mSTBridgeHelloTime": mSTBridgeHelloTime,
       "mSTBridgeForwardDelay": mSTBridgeForwardDelay,
       "mSTPort": mSTPort,
       "mSTPortTable": mSTPortTable,
       "mSTPortEntry": mSTPortEntry,
       "mSTPortAdminLinkType": mSTPortAdminLinkType,
       "mSTPortOperLinkType": mSTPortOperLinkType,
       "mSTPortProtocolMigration": mSTPortProtocolMigration,
       "mSTPortStatus": mSTPortStatus,
       "mSTPortAdminEdgePort": mSTPortAdminEdgePort,
       "mSTPortOperEdgePort": mSTPortOperEdgePort,
       "mSTPortEnable": mSTPortEnable,
       "mSTPortPerMstTable": mSTPortPerMstTable,
       "mSTPortPerMstEntry": mSTPortPerMstEntry,
       "mSTPortPerMstRoleValue": mSTPortPerMstRoleValue,
       "mSTPortPerMstPriority": mSTPortPerMstPriority,
       "mSTPortPerMstState": mSTPortPerMstState,
       "mSTPortPerMstPathCost": mSTPortPerMstPathCost,
       "mSTPortPerMstDesignatedCost": mSTPortPerMstDesignatedCost,
       "mSTPortPerMstDesignatedBridge": mSTPortPerMstDesignatedBridge,
       "mSTPortPerMstDesignatedPort": mSTPortPerMstDesignatedPort}
)
