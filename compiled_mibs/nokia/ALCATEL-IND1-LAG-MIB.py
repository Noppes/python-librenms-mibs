# SNMP MIB module (ALCATEL-IND1-LAG-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\nokia\aos6\ALCATEL-IND1-LAG-MIB

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

(lnkaggTraps,
 softentIND1LnkAgg) = mibBuilder.importSymbols(
    "ALCATEL-IND1-BASE",
    "lnkaggTraps",
    "softentIND1LnkAgg")

(ChurnState,
 LacpKey,
 LacpState) = mibBuilder.importSymbols(
    "IEEE8023-LAG-MIB",
    "ChurnState",
    "LacpKey",
    "LacpState")

(InterfaceIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex")

(PortList,) = mibBuilder.importSymbols(
    "Q-BRIDGE-MIB",
    "PortList")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

alcatelIND1LAGMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 13, 1)
)
if mibBuilder.loadTexts:
    alcatelIND1LAGMIB.setRevisions(
        ("2019-10-07 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class LacpType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("lacpOff", 0),
          ("lacpOn", 1))
    )



class McLagType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("mcLagOff", 0),
          ("mcLagOn", 1))
    )



# MIB Managed Objects in the order of their OIDs

_AlcatelIND1LAGMIBObjects_ObjectIdentity = ObjectIdentity
alcatelIND1LAGMIBObjects = _AlcatelIND1LAGMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 13, 1, 1)
)
_AlclnkaggAgg_ObjectIdentity = ObjectIdentity
alclnkaggAgg = _AlclnkaggAgg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 13, 1, 1, 1)
)
_AlclnkaggAggTable_Object = MibTable
alclnkaggAggTable = _AlclnkaggAggTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 13, 1, 1, 1, 1)
)
if mibBuilder.loadTexts:
    alclnkaggAggTable.setStatus("current")
_AlclnkaggAggEntry_Object = MibTableRow
alclnkaggAggEntry = _AlclnkaggAggEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 13, 1, 1, 1, 1, 1)
)
alclnkaggAggEntry.setIndexNames(
    (0, "ALCATEL-IND1-LAG-MIB", "alclnkaggAggIndex"),
)
if mibBuilder.loadTexts:
    alclnkaggAggEntry.setStatus("current")
_AlclnkaggAggIndex_Type = InterfaceIndex
_AlclnkaggAggIndex_Object = MibTableColumn
alclnkaggAggIndex = _AlclnkaggAggIndex_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 13, 1, 1, 1, 1, 1, 1),
    _AlclnkaggAggIndex_Type()
)
alclnkaggAggIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alclnkaggAggIndex.setStatus("current")
_AlclnkaggAggMACAddress_Type = MacAddress
_AlclnkaggAggMACAddress_Object = MibTableColumn
alclnkaggAggMACAddress = _AlclnkaggAggMACAddress_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 13, 1, 1, 1, 1, 1, 2),
    _AlclnkaggAggMACAddress_Type()
)
alclnkaggAggMACAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alclnkaggAggMACAddress.setStatus("current")


class _AlclnkaggAggActorSystemPriority_Type(Integer32):
    """Custom type alclnkaggAggActorSystemPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AlclnkaggAggActorSystemPriority_Type.__name__ = "Integer32"
_AlclnkaggAggActorSystemPriority_Object = MibTableColumn
alclnkaggAggActorSystemPriority = _AlclnkaggAggActorSystemPriority_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 13, 1, 1, 1, 1, 1, 3),
    _AlclnkaggAggActorSystemPriority_Type()
)
alclnkaggAggActorSystemPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alclnkaggAggActorSystemPriority.setStatus("current")
_AlclnkaggAggActorSystemID_Type = MacAddress
_AlclnkaggAggActorSystemID_Object = MibTableColumn
alclnkaggAggActorSystemID = _AlclnkaggAggActorSystemID_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 13, 1, 1, 1, 1, 1, 4),
    _AlclnkaggAggActorSystemID_Type()
)
alclnkaggAggActorSystemID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alclnkaggAggActorSystemID.setStatus("current")
_AlclnkaggAggPartnerAdminKey_Type = LacpKey
_AlclnkaggAggPartnerAdminKey_Object = MibTableColumn
alclnkaggAggPartnerAdminKey = _AlclnkaggAggPartnerAdminKey_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 13, 1, 1, 1, 1, 1, 5),
    _AlclnkaggAggPartnerAdminKey_Type()
)
alclnkaggAggPartnerAdminKey.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alclnkaggAggPartnerAdminKey.setStatus("current")
_AlclnkaggAggActorAdminKey_Type = LacpKey
_AlclnkaggAggActorAdminKey_Object = MibTableColumn
alclnkaggAggActorAdminKey = _AlclnkaggAggActorAdminKey_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 13, 1, 1, 1, 1, 1, 6),
    _AlclnkaggAggActorAdminKey_Type()
)
alclnkaggAggActorAdminKey.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alclnkaggAggActorAdminKey.setStatus("current")
_AlclnkaggAggActorOperKey_Type = LacpKey
_AlclnkaggAggActorOperKey_Object = MibTableColumn
alclnkaggAggActorOperKey = _AlclnkaggAggActorOperKey_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 13, 1, 1, 1, 1, 1, 7),
    _AlclnkaggAggActorOperKey_Type()
)
alclnkaggAggActorOperKey.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alclnkaggAggActorOperKey.setStatus("current")
_AlclnkaggAggPartnerSystemID_Type = MacAddress
_AlclnkaggAggPartnerSystemID_Object = MibTableColumn
alclnkaggAggPartnerSystemID = _AlclnkaggAggPartnerSystemID_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 13, 1, 1, 1, 1, 1, 8),
    _AlclnkaggAggPartnerSystemID_Type()
)
alclnkaggAggPartnerSystemID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alclnkaggAggPartnerSystemID.setStatus("current")


class _AlclnkaggAggPartnerSystemPriority_Type(Integer32):
    """Custom type alclnkaggAggPartnerSystemPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AlclnkaggAggPartnerSystemPriority_Type.__name__ = "Integer32"
_AlclnkaggAggPartnerSystemPriority_Object = MibTableColumn
alclnkaggAggPartnerSystemPriority = _AlclnkaggAggPartnerSystemPriority_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 13, 1, 1, 1, 1, 1, 9),
    _AlclnkaggAggPartnerSystemPriority_Type()
)
alclnkaggAggPartnerSystemPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alclnkaggAggPartnerSystemPriority.setStatus("current")
_AlclnkaggAggPartnerOperKey_Type = LacpKey
_AlclnkaggAggPartnerOperKey_Object = MibTableColumn
alclnkaggAggPartnerOperKey = _AlclnkaggAggPartnerOperKey_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 13, 1, 1, 1, 1, 1, 10),
    _AlclnkaggAggPartnerOperKey_Type()
)
alclnkaggAggPartnerOperKey.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alclnkaggAggPartnerOperKey.setStatus("current")


class _AlclnkaggAggSize_Type(Integer32):
    """Custom type alclnkaggAggSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_AlclnkaggAggSize_Type.__name__ = "Integer32"
_AlclnkaggAggSize_Object = MibTableColumn
alclnkaggAggSize = _AlclnkaggAggSize_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 13, 1, 1, 1, 1, 1, 11),
    _AlclnkaggAggSize_Type()
)
alclnkaggAggSize.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alclnkaggAggSize.setStatus("current")


class _AlclnkaggAggNumber_Type(Integer32):
    """Custom type alclnkaggAggNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 127),
    )


_AlclnkaggAggNumber_Type.__name__ = "Integer32"
_AlclnkaggAggNumber_Object = MibTableColumn
alclnkaggAggNumber = _AlclnkaggAggNumber_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 13, 1, 1, 1, 1, 1, 12),
    _AlclnkaggAggNumber_Type()
)
alclnkaggAggNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alclnkaggAggNumber.setStatus("current")


class _AlclnkaggAggDescr_Type(DisplayString):
    """Custom type alclnkaggAggDescr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_AlclnkaggAggDescr_Type.__name__ = "DisplayString"
_AlclnkaggAggDescr_Object = MibTableColumn
alclnkaggAggDescr = _AlclnkaggAggDescr_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 13, 1, 1, 1, 1, 1, 13),
    _AlclnkaggAggDescr_Type()
)
alclnkaggAggDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alclnkaggAggDescr.setStatus("current")


class _AlclnkaggAggName_Type(DisplayString):
    """Custom type alclnkaggAggName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_AlclnkaggAggName_Type.__name__ = "DisplayString"
_AlclnkaggAggName_Object = MibTableColumn
alclnkaggAggName = _AlclnkaggAggName_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 13, 1, 1, 1, 1, 1, 14),
    _AlclnkaggAggName_Type()
)
alclnkaggAggName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alclnkaggAggName.setStatus("current")
_AlclnkaggAggLacpType_Type = LacpType
_AlclnkaggAggLacpType_Object = MibTableColumn
alclnkaggAggLacpType = _AlclnkaggAggLacpType_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 13, 1, 1, 1, 1, 1, 15),
    _AlclnkaggAggLacpType_Type()
)
alclnkaggAggLacpType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alclnkaggAggLacpType.setStatus("current")


class _AlclnkaggAggAdminState_Type(Integer32):
    """Custom type alclnkaggAggAdminState based on Integer32"""
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


_AlclnkaggAggAdminState_Type.__name__ = "Integer32"
_AlclnkaggAggAdminState_Object = MibTableColumn
alclnkaggAggAdminState = _AlclnkaggAggAdminState_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 13, 1, 1, 1, 1, 1, 16),
    _AlclnkaggAggAdminState_Type()
)
alclnkaggAggAdminState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alclnkaggAggAdminState.setStatus("current")


class _AlclnkaggAggOperState_Type(Integer32):
    """Custom type alclnkaggAggOperState based on Integer32"""
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
        *(("up", 1),
          ("down", 2),
          ("logicPortCreatFailed", 3),
          ("qReservationFailed", 4))
    )


_AlclnkaggAggOperState_Type.__name__ = "Integer32"
_AlclnkaggAggOperState_Object = MibTableColumn
alclnkaggAggOperState = _AlclnkaggAggOperState_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 13, 1, 1, 1, 1, 1, 17),
    _AlclnkaggAggOperState_Type()
)
alclnkaggAggOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alclnkaggAggOperState.setStatus("current")


class _AlclnkaggAggNbrSelectedPorts_Type(Integer32):
    """Custom type alclnkaggAggNbrSelectedPorts based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )


_AlclnkaggAggNbrSelectedPorts_Type.__name__ = "Integer32"
_AlclnkaggAggNbrSelectedPorts_Object = MibTableColumn
alclnkaggAggNbrSelectedPorts = _AlclnkaggAggNbrSelectedPorts_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 13, 1, 1, 1, 1, 1, 18),
    _AlclnkaggAggNbrSelectedPorts_Type()
)
alclnkaggAggNbrSelectedPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alclnkaggAggNbrSelectedPorts.setStatus("current")


class _AlclnkaggAggNbrAttachedPorts_Type(Integer32):
    """Custom type alclnkaggAggNbrAttachedPorts based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )


_AlclnkaggAggNbrAttachedPorts_Type.__name__ = "Integer32"
_AlclnkaggAggNbrAttachedPorts_Object = MibTableColumn
alclnkaggAggNbrAttachedPorts = _AlclnkaggAggNbrAttachedPorts_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 13, 1, 1, 1, 1, 1, 19),
    _AlclnkaggAggNbrAttachedPorts_Type()
)
alclnkaggAggNbrAttachedPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alclnkaggAggNbrAttachedPorts.setStatus("current")
_AlclnkaggAggPrimaryPortIndex_Type = InterfaceIndex
_AlclnkaggAggPrimaryPortIndex_Object = MibTableColumn
alclnkaggAggPrimaryPortIndex = _AlclnkaggAggPrimaryPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 13, 1, 1, 1, 1, 1, 20),
    _AlclnkaggAggPrimaryPortIndex_Type()
)
alclnkaggAggPrimaryPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alclnkaggAggPrimaryPortIndex.setStatus("current")


class _AlclnkaggAggPrimaryPortPosition_Type(Integer32):
    """Custom type alclnkaggAggPrimaryPortPosition based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 15),
    )


_AlclnkaggAggPrimaryPortPosition_Type.__name__ = "Integer32"
_AlclnkaggAggPrimaryPortPosition_Object = MibTableColumn
alclnkaggAggPrimaryPortPosition = _AlclnkaggAggPrimaryPortPosition_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 13, 1, 1, 1, 1, 1, 21),
    _AlclnkaggAggPrimaryPortPosition_Type()
)
alclnkaggAggPrimaryPortPosition.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alclnkaggAggPrimaryPortPosition.setStatus("current")
_AlclnkaggAggRowStatus_Type = RowStatus
_AlclnkaggAggRowStatus_Object = MibTableColumn
alclnkaggAggRowStatus = _AlclnkaggAggRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 13, 1, 1, 1, 1, 1, 22),
    _AlclnkaggAggRowStatus_Type()
)
alclnkaggAggRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alclnkaggAggRowStatus.setStatus("current")


class _AlclnkaggAggPreemptState_Type(Integer32):
    """Custom type alclnkaggAggPreemptState based on Integer32"""
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


_AlclnkaggAggPreemptState_Type.__name__ = "Integer32"
_AlclnkaggAggPreemptState_Object = MibTableColumn
alclnkaggAggPreemptState = _AlclnkaggAggPreemptState_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 13, 1, 1, 1, 1, 1, 23),
    _AlclnkaggAggPreemptState_Type()
)
alclnkaggAggPreemptState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alclnkaggAggPreemptState.setStatus("current")


class _AlclnkaggAggPreemptValue_Type(Integer32):
    """Custom type alclnkaggAggPreemptValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(30, 300),
    )


_AlclnkaggAggPreemptValue_Type.__name__ = "Integer32"
_AlclnkaggAggPreemptValue_Object = MibTableColumn
alclnkaggAggPreemptValue = _AlclnkaggAggPreemptValue_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 13, 1, 1, 1, 1, 1, 24),
    _AlclnkaggAggPreemptValue_Type()
)
alclnkaggAggPreemptValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alclnkaggAggPreemptValue.setStatus("current")


class _AlclnkaggAggMinimumSize_Type(Integer32):
    """Custom type alclnkaggAggMinimumSize based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_AlclnkaggAggMinimumSize_Type.__name__ = "Integer32"
_AlclnkaggAggMinimumSize_Object = MibTableColumn
alclnkaggAggMinimumSize = _AlclnkaggAggMinimumSize_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 13, 1, 1, 1, 1, 1, 25),
    _AlclnkaggAggMinimumSize_Type()
)
alclnkaggAggMinimumSize.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alclnkaggAggMinimumSize.setStatus("current")
_AlclnkaggAggMcLagType_Type = McLagType
_AlclnkaggAggMcLagType_Object = MibTableColumn
alclnkaggAggMcLagType = _AlclnkaggAggMcLagType_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 13, 1, 1, 1, 1, 1, 26),
    _AlclnkaggAggMcLagType_Type()
)
alclnkaggAggMcLagType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alclnkaggAggMcLagType.setStatus("current")


class _AlclnkaggAggWTRTimer_Type(Integer32):
    """Custom type alclnkaggAggWTRTimer based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 12),
    )


_AlclnkaggAggWTRTimer_Type.__name__ = "Integer32"
_AlclnkaggAggWTRTimer_Object = MibTableColumn
alclnkaggAggWTRTimer = _AlclnkaggAggWTRTimer_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 13, 1, 1, 1, 1, 1, 27),
    _AlclnkaggAggWTRTimer_Type()
)
alclnkaggAggWTRTimer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alclnkaggAggWTRTimer.setStatus("current")
_AlclnkaggAggPortListTable_Object = MibTable
alclnkaggAggPortListTable = _AlclnkaggAggPortListTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 13, 1, 1, 1, 2)
)
if mibBuilder.loadTexts:
    alclnkaggAggPortListTable.setStatus("current")
_AlclnkaggAggPortListEntry_Object = MibTableRow
alclnkaggAggPortListEntry = _AlclnkaggAggPortListEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 13, 1, 1, 1, 2, 1)
)
alclnkaggAggPortListEntry.setIndexNames(
    (0, "ALCATEL-IND1-LAG-MIB", "alclnkaggAggIndex"),
)
if mibBuilder.loadTexts:
    alclnkaggAggPortListEntry.setStatus("current")
_AlclnkaggAggPortListPorts_Type = PortList
_AlclnkaggAggPortListPorts_Object = MibTableColumn
alclnkaggAggPortListPorts = _AlclnkaggAggPortListPorts_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 13, 1, 1, 1, 2, 1, 1),
    _AlclnkaggAggPortListPorts_Type()
)
alclnkaggAggPortListPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alclnkaggAggPortListPorts.setStatus("current")


class _AlclnkaggAggEniActivate_Type(Integer32):
    """Custom type alclnkaggAggEniActivate based on Integer32"""
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


_AlclnkaggAggEniActivate_Type.__name__ = "Integer32"
_AlclnkaggAggEniActivate_Object = MibScalar
alclnkaggAggEniActivate = _AlclnkaggAggEniActivate_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 13, 1, 1, 1, 3),
    _AlclnkaggAggEniActivate_Type()
)
alclnkaggAggEniActivate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alclnkaggAggEniActivate.setStatus("obsolete")
_AlclnkaggSlotTable_Object = MibTable
alclnkaggSlotTable = _AlclnkaggSlotTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 13, 1, 1, 1, 4)
)
if mibBuilder.loadTexts:
    alclnkaggSlotTable.setStatus("current")
_AlclnkaggSlotEntry_Object = MibTableRow
alclnkaggSlotEntry = _AlclnkaggSlotEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 13, 1, 1, 1, 4, 1)
)
alclnkaggSlotEntry.setIndexNames(
    (0, "ALCATEL-IND1-LAG-MIB", "alclnkaggSlotNum"),
)
if mibBuilder.loadTexts:
    alclnkaggSlotEntry.setStatus("current")


class _AlclnkaggSlotNum_Type(Integer32):
    """Custom type alclnkaggSlotNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_AlclnkaggSlotNum_Type.__name__ = "Integer32"
_AlclnkaggSlotNum_Object = MibTableColumn
alclnkaggSlotNum = _AlclnkaggSlotNum_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 13, 1, 1, 1, 4, 1, 1),
    _AlclnkaggSlotNum_Type()
)
alclnkaggSlotNum.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alclnkaggSlotNum.setStatus("current")


class _AlclnkaggSlotStatus_Type(Integer32):
    """Custom type alclnkaggSlotStatus based on Integer32"""
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


_AlclnkaggSlotStatus_Type.__name__ = "Integer32"
_AlclnkaggSlotStatus_Object = MibTableColumn
alclnkaggSlotStatus = _AlclnkaggSlotStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 13, 1, 1, 1, 4, 1, 2),
    _AlclnkaggSlotStatus_Type()
)
alclnkaggSlotStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alclnkaggSlotStatus.setStatus("current")


class _AlclnkaggMultipleAggPerSlot_Type(Integer32):
    """Custom type alclnkaggMultipleAggPerSlot based on Integer32"""
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


_AlclnkaggMultipleAggPerSlot_Type.__name__ = "Integer32"
_AlclnkaggMultipleAggPerSlot_Object = MibTableColumn
alclnkaggMultipleAggPerSlot = _AlclnkaggMultipleAggPerSlot_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 13, 1, 1, 1, 4, 1, 3),
    _AlclnkaggMultipleAggPerSlot_Type()
)
alclnkaggMultipleAggPerSlot.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alclnkaggMultipleAggPerSlot.setStatus("current")
_AlclnkaggAggIdIfIndexTable_Object = MibTable
alclnkaggAggIdIfIndexTable = _AlclnkaggAggIdIfIndexTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 13, 1, 1, 1, 5)
)
if mibBuilder.loadTexts:
    alclnkaggAggIdIfIndexTable.setStatus("current")
_AlclnkaggAggIdIfIndexEntry_Object = MibTableRow
alclnkaggAggIdIfIndexEntry = _AlclnkaggAggIdIfIndexEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 13, 1, 1, 1, 5, 1)
)
alclnkaggAggIdIfIndexEntry.setIndexNames(
    (0, "ALCATEL-IND1-LAG-MIB", "alclnkaggIfIndex"),
)
if mibBuilder.loadTexts:
    alclnkaggAggIdIfIndexEntry.setStatus("current")


class _AlclnkaggIfIndex_Type(Integer32):
    """Custom type alclnkaggIfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_AlclnkaggIfIndex_Type.__name__ = "Integer32"
_AlclnkaggIfIndex_Object = MibTableColumn
alclnkaggIfIndex = _AlclnkaggIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 13, 1, 1, 1, 5, 1, 1),
    _AlclnkaggIfIndex_Type()
)
alclnkaggIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alclnkaggIfIndex.setStatus("current")


class _AlclnkaggAggId_Type(Integer32):
    """Custom type alclnkaggAggId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 127),
    )


_AlclnkaggAggId_Type.__name__ = "Integer32"
_AlclnkaggAggId_Object = MibTableColumn
alclnkaggAggId = _AlclnkaggAggId_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 13, 1, 1, 1, 5, 1, 2),
    _AlclnkaggAggId_Type()
)
alclnkaggAggId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alclnkaggAggId.setStatus("current")
_AlclnkaggAggIdAccountTable_Object = MibTable
alclnkaggAggIdAccountTable = _AlclnkaggAggIdAccountTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 13, 1, 1, 1, 6)
)
if mibBuilder.loadTexts:
    alclnkaggAggIdAccountTable.setStatus("current")
_AlclnkaggAggIdAccountEntry_Object = MibTableRow
alclnkaggAggIdAccountEntry = _AlclnkaggAggIdAccountEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 13, 1, 1, 1, 6, 1)
)
alclnkaggAggIdAccountEntry.setIndexNames(
    (0, "ALCATEL-IND1-LAG-MIB", "alclnkaggAggIndex"),
)
if mibBuilder.loadTexts:
    alclnkaggAggIdAccountEntry.setStatus("current")
_AlcRxUndersize_Type = Counter64
_AlcRxUndersize_Object = MibTableColumn
alcRxUndersize = _AlcRxUndersize_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 13, 1, 1, 1, 6, 1, 1),
    _AlcRxUndersize_Type()
)
alcRxUndersize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alcRxUndersize.setStatus("current")
_AlcTxUndersize_Type = Counter64
_AlcTxUndersize_Object = MibTableColumn
alcTxUndersize = _AlcTxUndersize_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 13, 1, 1, 1, 6, 1, 2),
    _AlcTxUndersize_Type()
)
alcTxUndersize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alcTxUndersize.setStatus("current")
_AlcRxOversize_Type = Counter64
_AlcRxOversize_Object = MibTableColumn
alcRxOversize = _AlcRxOversize_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 13, 1, 1, 1, 6, 1, 3),
    _AlcRxOversize_Type()
)
alcRxOversize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alcRxOversize.setStatus("current")
_AlcTxOversize_Type = Counter64
_AlcTxOversize_Object = MibTableColumn
alcTxOversize = _AlcTxOversize_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 13, 1, 1, 1, 6, 1, 4),
    _AlcTxOversize_Type()
)
alcTxOversize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alcTxOversize.setStatus("current")
_AlcRxPackets64_Type = Counter64
_AlcRxPackets64_Object = MibTableColumn
alcRxPackets64 = _AlcRxPackets64_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 13, 1, 1, 1, 6, 1, 5),
    _AlcRxPackets64_Type()
)
alcRxPackets64.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alcRxPackets64.setStatus("current")
_AlcRxPackets127_Type = Counter64
_AlcRxPackets127_Object = MibTableColumn
alcRxPackets127 = _AlcRxPackets127_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 13, 1, 1, 1, 6, 1, 6),
    _AlcRxPackets127_Type()
)
alcRxPackets127.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alcRxPackets127.setStatus("current")
_AlcRxPackets255_Type = Counter64
_AlcRxPackets255_Object = MibTableColumn
alcRxPackets255 = _AlcRxPackets255_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 13, 1, 1, 1, 6, 1, 7),
    _AlcRxPackets255_Type()
)
alcRxPackets255.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alcRxPackets255.setStatus("current")
_AlcRxPackets511_Type = Counter64
_AlcRxPackets511_Object = MibTableColumn
alcRxPackets511 = _AlcRxPackets511_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 13, 1, 1, 1, 6, 1, 8),
    _AlcRxPackets511_Type()
)
alcRxPackets511.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alcRxPackets511.setStatus("current")
_AlcRxPackets1023_Type = Counter64
_AlcRxPackets1023_Object = MibTableColumn
alcRxPackets1023 = _AlcRxPackets1023_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 13, 1, 1, 1, 6, 1, 9),
    _AlcRxPackets1023_Type()
)
alcRxPackets1023.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alcRxPackets1023.setStatus("current")
_AlcRxPacketsMax_Type = Counter64
_AlcRxPacketsMax_Object = MibTableColumn
alcRxPacketsMax = _AlcRxPacketsMax_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 13, 1, 1, 1, 6, 1, 10),
    _AlcRxPacketsMax_Type()
)
alcRxPacketsMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alcRxPacketsMax.setStatus("current")
_AlcRxJabberFrames_Type = Counter64
_AlcRxJabberFrames_Object = MibTableColumn
alcRxJabberFrames = _AlcRxJabberFrames_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 13, 1, 1, 1, 6, 1, 11),
    _AlcRxJabberFrames_Type()
)
alcRxJabberFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alcRxJabberFrames.setStatus("current")
_AlclnkaggAggIdCounterTable_Object = MibTable
alclnkaggAggIdCounterTable = _AlclnkaggAggIdCounterTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 13, 1, 1, 1, 7)
)
if mibBuilder.loadTexts:
    alclnkaggAggIdCounterTable.setStatus("current")
_AlclnkaggAggIdCounterEntry_Object = MibTableRow
alclnkaggAggIdCounterEntry = _AlclnkaggAggIdCounterEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 13, 1, 1, 1, 7, 1)
)
alclnkaggAggIdCounterEntry.setIndexNames(
    (0, "ALCATEL-IND1-LAG-MIB", "alclnkaggAggIndex"),
)
if mibBuilder.loadTexts:
    alclnkaggAggIdCounterEntry.setStatus("current")
_AlcInOctets_Type = Counter64
_AlcInOctets_Object = MibTableColumn
alcInOctets = _AlcInOctets_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 13, 1, 1, 1, 7, 1, 1),
    _AlcInOctets_Type()
)
alcInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alcInOctets.setStatus("current")
_AlcOutOctets_Type = Counter64
_AlcOutOctets_Object = MibTableColumn
alcOutOctets = _AlcOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 13, 1, 1, 1, 7, 1, 2),
    _AlcOutOctets_Type()
)
alcOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alcOutOctets.setStatus("current")
_AlcInUcastPkts_Type = Counter64
_AlcInUcastPkts_Object = MibTableColumn
alcInUcastPkts = _AlcInUcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 13, 1, 1, 1, 7, 1, 3),
    _AlcInUcastPkts_Type()
)
alcInUcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alcInUcastPkts.setStatus("current")
_AlcOutUcastPkts_Type = Counter64
_AlcOutUcastPkts_Object = MibTableColumn
alcOutUcastPkts = _AlcOutUcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 13, 1, 1, 1, 7, 1, 4),
    _AlcOutUcastPkts_Type()
)
alcOutUcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alcOutUcastPkts.setStatus("current")
_AlcInMcastPkts_Type = Counter64
_AlcInMcastPkts_Object = MibTableColumn
alcInMcastPkts = _AlcInMcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 13, 1, 1, 1, 7, 1, 5),
    _AlcInMcastPkts_Type()
)
alcInMcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alcInMcastPkts.setStatus("current")
_AlcOutMcastPkts_Type = Counter64
_AlcOutMcastPkts_Object = MibTableColumn
alcOutMcastPkts = _AlcOutMcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 13, 1, 1, 1, 7, 1, 6),
    _AlcOutMcastPkts_Type()
)
alcOutMcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alcOutMcastPkts.setStatus("current")
_AlcInBcastPkts_Type = Counter64
_AlcInBcastPkts_Object = MibTableColumn
alcInBcastPkts = _AlcInBcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 13, 1, 1, 1, 7, 1, 7),
    _AlcInBcastPkts_Type()
)
alcInBcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alcInBcastPkts.setStatus("current")
_AlcOutBcastPkts_Type = Counter64
_AlcOutBcastPkts_Object = MibTableColumn
alcOutBcastPkts = _AlcOutBcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 13, 1, 1, 1, 7, 1, 8),
    _AlcOutBcastPkts_Type()
)
alcOutBcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alcOutBcastPkts.setStatus("current")
_AlcInPauseFrames_Type = Counter64
_AlcInPauseFrames_Object = MibTableColumn
alcInPauseFrames = _AlcInPauseFrames_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 13, 1, 1, 1, 7, 1, 9),
    _AlcInPauseFrames_Type()
)
alcInPauseFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alcInPauseFrames.setStatus("current")
_AlcOutPauseFrames_Type = Counter64
_AlcOutPauseFrames_Object = MibTableColumn
alcOutPauseFrames = _AlcOutPauseFrames_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 13, 1, 1, 1, 7, 1, 10),
    _AlcOutPauseFrames_Type()
)
alcOutPauseFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alcOutPauseFrames.setStatus("current")
_AlclnkaggAggIdCounterErrTable_Object = MibTable
alclnkaggAggIdCounterErrTable = _AlclnkaggAggIdCounterErrTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 13, 1, 1, 1, 8)
)
if mibBuilder.loadTexts:
    alclnkaggAggIdCounterErrTable.setStatus("current")
_AlclnkaggAggIdCounterErrEntry_Object = MibTableRow
alclnkaggAggIdCounterErrEntry = _AlclnkaggAggIdCounterErrEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 13, 1, 1, 1, 8, 1)
)
alclnkaggAggIdCounterErrEntry.setIndexNames(
    (0, "ALCATEL-IND1-LAG-MIB", "alclnkaggAggIndex"),
)
if mibBuilder.loadTexts:
    alclnkaggAggIdCounterErrEntry.setStatus("current")
_AlcAlignmentsErrors_Type = Counter64
_AlcAlignmentsErrors_Object = MibTableColumn
alcAlignmentsErrors = _AlcAlignmentsErrors_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 13, 1, 1, 1, 8, 1, 1),
    _AlcAlignmentsErrors_Type()
)
alcAlignmentsErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alcAlignmentsErrors.setStatus("current")
_AlcFCSErrors_Type = Counter64
_AlcFCSErrors_Object = MibTableColumn
alcFCSErrors = _AlcFCSErrors_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 13, 1, 1, 1, 8, 1, 2),
    _AlcFCSErrors_Type()
)
alcFCSErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alcFCSErrors.setStatus("current")
_AlcIfInErrors_Type = Counter64
_AlcIfInErrors_Object = MibTableColumn
alcIfInErrors = _AlcIfInErrors_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 13, 1, 1, 1, 8, 1, 3),
    _AlcIfInErrors_Type()
)
alcIfInErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alcIfInErrors.setStatus("current")
_AlcIfOutErrors_Type = Counter64
_AlcIfOutErrors_Object = MibTableColumn
alcIfOutErrors = _AlcIfOutErrors_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 13, 1, 1, 1, 8, 1, 4),
    _AlcIfOutErrors_Type()
)
alcIfOutErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alcIfOutErrors.setStatus("current")
_AlclnkaggAggIdTrafficTable_Object = MibTable
alclnkaggAggIdTrafficTable = _AlclnkaggAggIdTrafficTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 13, 1, 1, 1, 9)
)
if mibBuilder.loadTexts:
    alclnkaggAggIdTrafficTable.setStatus("current")
_AlclnkaggAggIdTrafficEntry_Object = MibTableRow
alclnkaggAggIdTrafficEntry = _AlclnkaggAggIdTrafficEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 13, 1, 1, 1, 9, 1)
)
alclnkaggAggIdTrafficEntry.setIndexNames(
    (0, "ALCATEL-IND1-LAG-MIB", "alclnkaggAggIndex"),
)
if mibBuilder.loadTexts:
    alclnkaggAggIdTrafficEntry.setStatus("current")
_AlcInputPackets_Type = Counter64
_AlcInputPackets_Object = MibTableColumn
alcInputPackets = _AlcInputPackets_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 13, 1, 1, 1, 9, 1, 1),
    _AlcInputPackets_Type()
)
alcInputPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alcInputPackets.setStatus("current")
_AlcInputBytes_Type = Counter64
_AlcInputBytes_Object = MibTableColumn
alcInputBytes = _AlcInputBytes_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 13, 1, 1, 1, 9, 1, 2),
    _AlcInputBytes_Type()
)
alcInputBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alcInputBytes.setStatus("current")
_AlcOutputPackets_Type = Counter64
_AlcOutputPackets_Object = MibTableColumn
alcOutputPackets = _AlcOutputPackets_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 13, 1, 1, 1, 9, 1, 3),
    _AlcOutputPackets_Type()
)
alcOutputPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alcOutputPackets.setStatus("current")
_AlcOutputBytes_Type = Counter64
_AlcOutputBytes_Object = MibTableColumn
alcOutputBytes = _AlcOutputBytes_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 13, 1, 1, 1, 9, 1, 4),
    _AlcOutputBytes_Type()
)
alcOutputBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alcOutputBytes.setStatus("current")
_AlcLagStatsTable_Object = MibTable
alcLagStatsTable = _AlcLagStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 13, 1, 1, 1, 10)
)
if mibBuilder.loadTexts:
    alcLagStatsTable.setStatus("current")
_AlcLagStatsEntry_Object = MibTableRow
alcLagStatsEntry = _AlcLagStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 13, 1, 1, 1, 10, 1)
)
alcLagStatsEntry.setIndexNames(
    (0, "ALCATEL-IND1-LAG-MIB", "alclnkaggAggIndex"),
)
if mibBuilder.loadTexts:
    alcLagStatsEntry.setStatus("current")


class _AlcLagClearStats_Type(Integer32):
    """Custom type alcLagClearStats based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("reset", 1))
    )


_AlcLagClearStats_Type.__name__ = "Integer32"
_AlcLagClearStats_Object = MibTableColumn
alcLagClearStats = _AlcLagClearStats_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 13, 1, 1, 1, 10, 1, 1),
    _AlcLagClearStats_Type()
)
alcLagClearStats.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alcLagClearStats.setStatus("current")
_AlclnkaggAggPort_ObjectIdentity = ObjectIdentity
alclnkaggAggPort = _AlclnkaggAggPort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 13, 1, 1, 2)
)
_AlclnkaggAggPortTable_Object = MibTable
alclnkaggAggPortTable = _AlclnkaggAggPortTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 13, 1, 1, 2, 1)
)
if mibBuilder.loadTexts:
    alclnkaggAggPortTable.setStatus("current")
_AlclnkaggAggPortEntry_Object = MibTableRow
alclnkaggAggPortEntry = _AlclnkaggAggPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 13, 1, 1, 2, 1, 1)
)
alclnkaggAggPortEntry.setIndexNames(
    (0, "ALCATEL-IND1-LAG-MIB", "alclnkaggAggPortIndex"),
)
if mibBuilder.loadTexts:
    alclnkaggAggPortEntry.setStatus("current")
_AlclnkaggAggPortIndex_Type = InterfaceIndex
_AlclnkaggAggPortIndex_Object = MibTableColumn
alclnkaggAggPortIndex = _AlclnkaggAggPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 13, 1, 1, 2, 1, 1, 1),
    _AlclnkaggAggPortIndex_Type()
)
alclnkaggAggPortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alclnkaggAggPortIndex.setStatus("current")


class _AlclnkaggAggPortActorSystemPriority_Type(Integer32):
    """Custom type alclnkaggAggPortActorSystemPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AlclnkaggAggPortActorSystemPriority_Type.__name__ = "Integer32"
_AlclnkaggAggPortActorSystemPriority_Object = MibTableColumn
alclnkaggAggPortActorSystemPriority = _AlclnkaggAggPortActorSystemPriority_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 13, 1, 1, 2, 1, 1, 2),
    _AlclnkaggAggPortActorSystemPriority_Type()
)
alclnkaggAggPortActorSystemPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alclnkaggAggPortActorSystemPriority.setStatus("current")
_AlclnkaggAggPortActorSystemID_Type = MacAddress
_AlclnkaggAggPortActorSystemID_Object = MibTableColumn
alclnkaggAggPortActorSystemID = _AlclnkaggAggPortActorSystemID_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 13, 1, 1, 2, 1, 1, 3),
    _AlclnkaggAggPortActorSystemID_Type()
)
alclnkaggAggPortActorSystemID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alclnkaggAggPortActorSystemID.setStatus("current")
_AlclnkaggAggPortActorAdminKey_Type = LacpKey
_AlclnkaggAggPortActorAdminKey_Object = MibTableColumn
alclnkaggAggPortActorAdminKey = _AlclnkaggAggPortActorAdminKey_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 13, 1, 1, 2, 1, 1, 4),
    _AlclnkaggAggPortActorAdminKey_Type()
)
alclnkaggAggPortActorAdminKey.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alclnkaggAggPortActorAdminKey.setStatus("current")
_AlclnkaggAggPortActorOperKey_Type = LacpKey
_AlclnkaggAggPortActorOperKey_Object = MibTableColumn
alclnkaggAggPortActorOperKey = _AlclnkaggAggPortActorOperKey_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 13, 1, 1, 2, 1, 1, 5),
    _AlclnkaggAggPortActorOperKey_Type()
)
alclnkaggAggPortActorOperKey.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alclnkaggAggPortActorOperKey.setStatus("current")


class _AlclnkaggAggPortPartnerAdminSystemPriority_Type(Integer32):
    """Custom type alclnkaggAggPortPartnerAdminSystemPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AlclnkaggAggPortPartnerAdminSystemPriority_Type.__name__ = "Integer32"
_AlclnkaggAggPortPartnerAdminSystemPriority_Object = MibTableColumn
alclnkaggAggPortPartnerAdminSystemPriority = _AlclnkaggAggPortPartnerAdminSystemPriority_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 13, 1, 1, 2, 1, 1, 6),
    _AlclnkaggAggPortPartnerAdminSystemPriority_Type()
)
alclnkaggAggPortPartnerAdminSystemPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alclnkaggAggPortPartnerAdminSystemPriority.setStatus("current")


class _AlclnkaggAggPortPartnerOperSystemPriority_Type(Integer32):
    """Custom type alclnkaggAggPortPartnerOperSystemPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AlclnkaggAggPortPartnerOperSystemPriority_Type.__name__ = "Integer32"
_AlclnkaggAggPortPartnerOperSystemPriority_Object = MibTableColumn
alclnkaggAggPortPartnerOperSystemPriority = _AlclnkaggAggPortPartnerOperSystemPriority_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 13, 1, 1, 2, 1, 1, 7),
    _AlclnkaggAggPortPartnerOperSystemPriority_Type()
)
alclnkaggAggPortPartnerOperSystemPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alclnkaggAggPortPartnerOperSystemPriority.setStatus("current")
_AlclnkaggAggPortPartnerAdminSystemID_Type = MacAddress
_AlclnkaggAggPortPartnerAdminSystemID_Object = MibTableColumn
alclnkaggAggPortPartnerAdminSystemID = _AlclnkaggAggPortPartnerAdminSystemID_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 13, 1, 1, 2, 1, 1, 8),
    _AlclnkaggAggPortPartnerAdminSystemID_Type()
)
alclnkaggAggPortPartnerAdminSystemID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alclnkaggAggPortPartnerAdminSystemID.setStatus("current")
_AlclnkaggAggPortPartnerOperSystemID_Type = MacAddress
_AlclnkaggAggPortPartnerOperSystemID_Object = MibTableColumn
alclnkaggAggPortPartnerOperSystemID = _AlclnkaggAggPortPartnerOperSystemID_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 13, 1, 1, 2, 1, 1, 9),
    _AlclnkaggAggPortPartnerOperSystemID_Type()
)
alclnkaggAggPortPartnerOperSystemID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alclnkaggAggPortPartnerOperSystemID.setStatus("current")
_AlclnkaggAggPortPartnerAdminKey_Type = LacpKey
_AlclnkaggAggPortPartnerAdminKey_Object = MibTableColumn
alclnkaggAggPortPartnerAdminKey = _AlclnkaggAggPortPartnerAdminKey_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 13, 1, 1, 2, 1, 1, 10),
    _AlclnkaggAggPortPartnerAdminKey_Type()
)
alclnkaggAggPortPartnerAdminKey.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alclnkaggAggPortPartnerAdminKey.setStatus("current")
_AlclnkaggAggPortPartnerOperKey_Type = LacpKey
_AlclnkaggAggPortPartnerOperKey_Object = MibTableColumn
alclnkaggAggPortPartnerOperKey = _AlclnkaggAggPortPartnerOperKey_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 13, 1, 1, 2, 1, 1, 11),
    _AlclnkaggAggPortPartnerOperKey_Type()
)
alclnkaggAggPortPartnerOperKey.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alclnkaggAggPortPartnerOperKey.setStatus("current")
_AlclnkaggAggPortSelectedAggID_Type = InterfaceIndex
_AlclnkaggAggPortSelectedAggID_Object = MibTableColumn
alclnkaggAggPortSelectedAggID = _AlclnkaggAggPortSelectedAggID_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 13, 1, 1, 2, 1, 1, 12),
    _AlclnkaggAggPortSelectedAggID_Type()
)
alclnkaggAggPortSelectedAggID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alclnkaggAggPortSelectedAggID.setStatus("current")
_AlclnkaggAggPortAttachedAggID_Type = InterfaceIndex
_AlclnkaggAggPortAttachedAggID_Object = MibTableColumn
alclnkaggAggPortAttachedAggID = _AlclnkaggAggPortAttachedAggID_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 13, 1, 1, 2, 1, 1, 13),
    _AlclnkaggAggPortAttachedAggID_Type()
)
alclnkaggAggPortAttachedAggID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alclnkaggAggPortAttachedAggID.setStatus("current")


class _AlclnkaggAggPortActorPort_Type(Integer32):
    """Custom type alclnkaggAggPortActorPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AlclnkaggAggPortActorPort_Type.__name__ = "Integer32"
_AlclnkaggAggPortActorPort_Object = MibTableColumn
alclnkaggAggPortActorPort = _AlclnkaggAggPortActorPort_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 13, 1, 1, 2, 1, 1, 14),
    _AlclnkaggAggPortActorPort_Type()
)
alclnkaggAggPortActorPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alclnkaggAggPortActorPort.setStatus("current")


class _AlclnkaggAggPortActorPortPriority_Type(Integer32):
    """Custom type alclnkaggAggPortActorPortPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AlclnkaggAggPortActorPortPriority_Type.__name__ = "Integer32"
_AlclnkaggAggPortActorPortPriority_Object = MibTableColumn
alclnkaggAggPortActorPortPriority = _AlclnkaggAggPortActorPortPriority_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 13, 1, 1, 2, 1, 1, 15),
    _AlclnkaggAggPortActorPortPriority_Type()
)
alclnkaggAggPortActorPortPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alclnkaggAggPortActorPortPriority.setStatus("current")


class _AlclnkaggAggPortPartnerAdminPort_Type(Integer32):
    """Custom type alclnkaggAggPortPartnerAdminPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AlclnkaggAggPortPartnerAdminPort_Type.__name__ = "Integer32"
_AlclnkaggAggPortPartnerAdminPort_Object = MibTableColumn
alclnkaggAggPortPartnerAdminPort = _AlclnkaggAggPortPartnerAdminPort_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 13, 1, 1, 2, 1, 1, 16),
    _AlclnkaggAggPortPartnerAdminPort_Type()
)
alclnkaggAggPortPartnerAdminPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alclnkaggAggPortPartnerAdminPort.setStatus("current")


class _AlclnkaggAggPortPartnerOperPort_Type(Integer32):
    """Custom type alclnkaggAggPortPartnerOperPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AlclnkaggAggPortPartnerOperPort_Type.__name__ = "Integer32"
_AlclnkaggAggPortPartnerOperPort_Object = MibTableColumn
alclnkaggAggPortPartnerOperPort = _AlclnkaggAggPortPartnerOperPort_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 13, 1, 1, 2, 1, 1, 17),
    _AlclnkaggAggPortPartnerOperPort_Type()
)
alclnkaggAggPortPartnerOperPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alclnkaggAggPortPartnerOperPort.setStatus("current")


class _AlclnkaggAggPortPartnerAdminPortPriority_Type(Integer32):
    """Custom type alclnkaggAggPortPartnerAdminPortPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AlclnkaggAggPortPartnerAdminPortPriority_Type.__name__ = "Integer32"
_AlclnkaggAggPortPartnerAdminPortPriority_Object = MibTableColumn
alclnkaggAggPortPartnerAdminPortPriority = _AlclnkaggAggPortPartnerAdminPortPriority_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 13, 1, 1, 2, 1, 1, 18),
    _AlclnkaggAggPortPartnerAdminPortPriority_Type()
)
alclnkaggAggPortPartnerAdminPortPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alclnkaggAggPortPartnerAdminPortPriority.setStatus("current")


class _AlclnkaggAggPortPartnerOperPortPriority_Type(Integer32):
    """Custom type alclnkaggAggPortPartnerOperPortPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AlclnkaggAggPortPartnerOperPortPriority_Type.__name__ = "Integer32"
_AlclnkaggAggPortPartnerOperPortPriority_Object = MibTableColumn
alclnkaggAggPortPartnerOperPortPriority = _AlclnkaggAggPortPartnerOperPortPriority_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 13, 1, 1, 2, 1, 1, 19),
    _AlclnkaggAggPortPartnerOperPortPriority_Type()
)
alclnkaggAggPortPartnerOperPortPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alclnkaggAggPortPartnerOperPortPriority.setStatus("current")
_AlclnkaggAggPortActorAdminState_Type = LacpState
_AlclnkaggAggPortActorAdminState_Object = MibTableColumn
alclnkaggAggPortActorAdminState = _AlclnkaggAggPortActorAdminState_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 13, 1, 1, 2, 1, 1, 20),
    _AlclnkaggAggPortActorAdminState_Type()
)
alclnkaggAggPortActorAdminState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alclnkaggAggPortActorAdminState.setStatus("current")
_AlclnkaggAggPortActorOperState_Type = LacpState
_AlclnkaggAggPortActorOperState_Object = MibTableColumn
alclnkaggAggPortActorOperState = _AlclnkaggAggPortActorOperState_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 13, 1, 1, 2, 1, 1, 21),
    _AlclnkaggAggPortActorOperState_Type()
)
alclnkaggAggPortActorOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alclnkaggAggPortActorOperState.setStatus("current")
_AlclnkaggAggPortPartnerAdminState_Type = LacpState
_AlclnkaggAggPortPartnerAdminState_Object = MibTableColumn
alclnkaggAggPortPartnerAdminState = _AlclnkaggAggPortPartnerAdminState_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 13, 1, 1, 2, 1, 1, 22),
    _AlclnkaggAggPortPartnerAdminState_Type()
)
alclnkaggAggPortPartnerAdminState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alclnkaggAggPortPartnerAdminState.setStatus("current")
_AlclnkaggAggPortPartnerOperState_Type = LacpState
_AlclnkaggAggPortPartnerOperState_Object = MibTableColumn
alclnkaggAggPortPartnerOperState = _AlclnkaggAggPortPartnerOperState_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 13, 1, 1, 2, 1, 1, 23),
    _AlclnkaggAggPortPartnerOperState_Type()
)
alclnkaggAggPortPartnerOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alclnkaggAggPortPartnerOperState.setStatus("current")


class _AlclnkaggAggPortSelectedAggNumber_Type(Integer32):
    """Custom type alclnkaggAggPortSelectedAggNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 127),
    )


_AlclnkaggAggPortSelectedAggNumber_Type.__name__ = "Integer32"
_AlclnkaggAggPortSelectedAggNumber_Object = MibTableColumn
alclnkaggAggPortSelectedAggNumber = _AlclnkaggAggPortSelectedAggNumber_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 13, 1, 1, 2, 1, 1, 24),
    _AlclnkaggAggPortSelectedAggNumber_Type()
)
alclnkaggAggPortSelectedAggNumber.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alclnkaggAggPortSelectedAggNumber.setStatus("current")


class _AlclnkaggAggPortGlobalPortNumber_Type(Integer32):
    """Custom type alclnkaggAggPortGlobalPortNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AlclnkaggAggPortGlobalPortNumber_Type.__name__ = "Integer32"
_AlclnkaggAggPortGlobalPortNumber_Object = MibTableColumn
alclnkaggAggPortGlobalPortNumber = _AlclnkaggAggPortGlobalPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 13, 1, 1, 2, 1, 1, 25),
    _AlclnkaggAggPortGlobalPortNumber_Type()
)
alclnkaggAggPortGlobalPortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alclnkaggAggPortGlobalPortNumber.setStatus("current")


class _AlclnkaggAggPortAdminState_Type(Integer32):
    """Custom type alclnkaggAggPortAdminState based on Integer32"""
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


_AlclnkaggAggPortAdminState_Type.__name__ = "Integer32"
_AlclnkaggAggPortAdminState_Object = MibTableColumn
alclnkaggAggPortAdminState = _AlclnkaggAggPortAdminState_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 13, 1, 1, 2, 1, 1, 26),
    _AlclnkaggAggPortAdminState_Type()
)
alclnkaggAggPortAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alclnkaggAggPortAdminState.setStatus("current")


class _AlclnkaggAggPortOperState_Type(Integer32):
    """Custom type alclnkaggAggPortOperState based on Integer32"""
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
        *(("up", 1),
          ("down", 2),
          ("notAttached", 3),
          ("notAggregable", 4))
    )


_AlclnkaggAggPortOperState_Type.__name__ = "Integer32"
_AlclnkaggAggPortOperState_Object = MibTableColumn
alclnkaggAggPortOperState = _AlclnkaggAggPortOperState_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 13, 1, 1, 2, 1, 1, 27),
    _AlclnkaggAggPortOperState_Type()
)
alclnkaggAggPortOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alclnkaggAggPortOperState.setStatus("current")


class _AlclnkaggAggPortState_Type(Integer32):
    """Custom type alclnkaggAggPortState based on Integer32"""
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
        *(("created", 1),
          ("configurable", 2),
          ("configured", 3),
          ("selected", 4),
          ("reserved", 5),
          ("attached", 6))
    )


_AlclnkaggAggPortState_Type.__name__ = "Integer32"
_AlclnkaggAggPortState_Object = MibTableColumn
alclnkaggAggPortState = _AlclnkaggAggPortState_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 13, 1, 1, 2, 1, 1, 28),
    _AlclnkaggAggPortState_Type()
)
alclnkaggAggPortState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alclnkaggAggPortState.setStatus("current")


class _AlclnkaggAggPortLinkState_Type(Integer32):
    """Custom type alclnkaggAggPortLinkState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("up", 1),
          ("down", 2))
    )


_AlclnkaggAggPortLinkState_Type.__name__ = "Integer32"
_AlclnkaggAggPortLinkState_Object = MibTableColumn
alclnkaggAggPortLinkState = _AlclnkaggAggPortLinkState_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 13, 1, 1, 2, 1, 1, 29),
    _AlclnkaggAggPortLinkState_Type()
)
alclnkaggAggPortLinkState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alclnkaggAggPortLinkState.setStatus("current")


class _AlclnkaggAggPortPrimary_Type(Integer32):
    """Custom type alclnkaggAggPortPrimary based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("yes", 1),
          ("no", 2),
          ("notSignificant", 3))
    )


_AlclnkaggAggPortPrimary_Type.__name__ = "Integer32"
_AlclnkaggAggPortPrimary_Object = MibTableColumn
alclnkaggAggPortPrimary = _AlclnkaggAggPortPrimary_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 13, 1, 1, 2, 1, 1, 30),
    _AlclnkaggAggPortPrimary_Type()
)
alclnkaggAggPortPrimary.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alclnkaggAggPortPrimary.setStatus("current")
_AlclnkaggAggPortLacpType_Type = LacpType
_AlclnkaggAggPortLacpType_Object = MibTableColumn
alclnkaggAggPortLacpType = _AlclnkaggAggPortLacpType_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 13, 1, 1, 2, 1, 1, 31),
    _AlclnkaggAggPortLacpType_Type()
)
alclnkaggAggPortLacpType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alclnkaggAggPortLacpType.setStatus("current")
_AlclnkaggAggPortRowStatus_Type = RowStatus
_AlclnkaggAggPortRowStatus_Object = MibTableColumn
alclnkaggAggPortRowStatus = _AlclnkaggAggPortRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 13, 1, 1, 2, 1, 1, 32),
    _AlclnkaggAggPortRowStatus_Type()
)
alclnkaggAggPortRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alclnkaggAggPortRowStatus.setStatus("current")


class _AlclnkaggAggPortStandbyState_Type(Integer32):
    """Custom type alclnkaggAggPortStandbyState based on Integer32"""
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


_AlclnkaggAggPortStandbyState_Type.__name__ = "Integer32"
_AlclnkaggAggPortStandbyState_Object = MibTableColumn
alclnkaggAggPortStandbyState = _AlclnkaggAggPortStandbyState_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 13, 1, 1, 2, 1, 1, 33),
    _AlclnkaggAggPortStandbyState_Type()
)
alclnkaggAggPortStandbyState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alclnkaggAggPortStandbyState.setStatus("current")
_AlclnkaggAggPortMcLagType_Type = McLagType
_AlclnkaggAggPortMcLagType_Object = MibTableColumn
alclnkaggAggPortMcLagType = _AlclnkaggAggPortMcLagType_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 13, 1, 1, 2, 1, 1, 34),
    _AlclnkaggAggPortMcLagType_Type()
)
alclnkaggAggPortMcLagType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alclnkaggAggPortMcLagType.setStatus("current")
_AlclnkaggAggPortStatsTable_Object = MibTable
alclnkaggAggPortStatsTable = _AlclnkaggAggPortStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 13, 1, 1, 2, 2)
)
if mibBuilder.loadTexts:
    alclnkaggAggPortStatsTable.setStatus("current")
_AlclnkaggAggPortStatsEntry_Object = MibTableRow
alclnkaggAggPortStatsEntry = _AlclnkaggAggPortStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 13, 1, 1, 2, 2, 1)
)
alclnkaggAggPortStatsEntry.setIndexNames(
    (0, "ALCATEL-IND1-LAG-MIB", "alclnkaggAggPortIndex"),
)
if mibBuilder.loadTexts:
    alclnkaggAggPortStatsEntry.setStatus("current")
_AlclnkaggAggPortStatsLACPDUsRx_Type = Counter32
_AlclnkaggAggPortStatsLACPDUsRx_Object = MibTableColumn
alclnkaggAggPortStatsLACPDUsRx = _AlclnkaggAggPortStatsLACPDUsRx_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 13, 1, 1, 2, 2, 1, 1),
    _AlclnkaggAggPortStatsLACPDUsRx_Type()
)
alclnkaggAggPortStatsLACPDUsRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alclnkaggAggPortStatsLACPDUsRx.setStatus("current")
_AlclnkaggAggPortStatsMarkerPDUsRx_Type = Counter32
_AlclnkaggAggPortStatsMarkerPDUsRx_Object = MibTableColumn
alclnkaggAggPortStatsMarkerPDUsRx = _AlclnkaggAggPortStatsMarkerPDUsRx_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 13, 1, 1, 2, 2, 1, 2),
    _AlclnkaggAggPortStatsMarkerPDUsRx_Type()
)
alclnkaggAggPortStatsMarkerPDUsRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alclnkaggAggPortStatsMarkerPDUsRx.setStatus("current")
_AlclnkaggAggPortStatsMarkerResponsePDUsRx_Type = Counter32
_AlclnkaggAggPortStatsMarkerResponsePDUsRx_Object = MibTableColumn
alclnkaggAggPortStatsMarkerResponsePDUsRx = _AlclnkaggAggPortStatsMarkerResponsePDUsRx_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 13, 1, 1, 2, 2, 1, 3),
    _AlclnkaggAggPortStatsMarkerResponsePDUsRx_Type()
)
alclnkaggAggPortStatsMarkerResponsePDUsRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alclnkaggAggPortStatsMarkerResponsePDUsRx.setStatus("current")
_AlclnkaggAggPortStatsUnknownRx_Type = Counter32
_AlclnkaggAggPortStatsUnknownRx_Object = MibTableColumn
alclnkaggAggPortStatsUnknownRx = _AlclnkaggAggPortStatsUnknownRx_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 13, 1, 1, 2, 2, 1, 4),
    _AlclnkaggAggPortStatsUnknownRx_Type()
)
alclnkaggAggPortStatsUnknownRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alclnkaggAggPortStatsUnknownRx.setStatus("current")
_AlclnkaggAggPortStatsIllegalRx_Type = Counter32
_AlclnkaggAggPortStatsIllegalRx_Object = MibTableColumn
alclnkaggAggPortStatsIllegalRx = _AlclnkaggAggPortStatsIllegalRx_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 13, 1, 1, 2, 2, 1, 5),
    _AlclnkaggAggPortStatsIllegalRx_Type()
)
alclnkaggAggPortStatsIllegalRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alclnkaggAggPortStatsIllegalRx.setStatus("current")
_AlclnkaggAggPortStatsLACPDUsTx_Type = Counter32
_AlclnkaggAggPortStatsLACPDUsTx_Object = MibTableColumn
alclnkaggAggPortStatsLACPDUsTx = _AlclnkaggAggPortStatsLACPDUsTx_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 13, 1, 1, 2, 2, 1, 6),
    _AlclnkaggAggPortStatsLACPDUsTx_Type()
)
alclnkaggAggPortStatsLACPDUsTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alclnkaggAggPortStatsLACPDUsTx.setStatus("current")
_AlclnkaggAggPortStatsMarkerPDUsTx_Type = Counter32
_AlclnkaggAggPortStatsMarkerPDUsTx_Object = MibTableColumn
alclnkaggAggPortStatsMarkerPDUsTx = _AlclnkaggAggPortStatsMarkerPDUsTx_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 13, 1, 1, 2, 2, 1, 7),
    _AlclnkaggAggPortStatsMarkerPDUsTx_Type()
)
alclnkaggAggPortStatsMarkerPDUsTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alclnkaggAggPortStatsMarkerPDUsTx.setStatus("current")
_AlclnkaggAggPortStatsMarkerResponsePDUsTx_Type = Counter32
_AlclnkaggAggPortStatsMarkerResponsePDUsTx_Object = MibTableColumn
alclnkaggAggPortStatsMarkerResponsePDUsTx = _AlclnkaggAggPortStatsMarkerResponsePDUsTx_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 13, 1, 1, 2, 2, 1, 8),
    _AlclnkaggAggPortStatsMarkerResponsePDUsTx_Type()
)
alclnkaggAggPortStatsMarkerResponsePDUsTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alclnkaggAggPortStatsMarkerResponsePDUsTx.setStatus("current")
_AlclnkaggAggPortDebugTable_Object = MibTable
alclnkaggAggPortDebugTable = _AlclnkaggAggPortDebugTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 13, 1, 1, 2, 3)
)
if mibBuilder.loadTexts:
    alclnkaggAggPortDebugTable.setStatus("current")
_AlclnkaggAggPortDebugEntry_Object = MibTableRow
alclnkaggAggPortDebugEntry = _AlclnkaggAggPortDebugEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 13, 1, 1, 2, 3, 1)
)
alclnkaggAggPortDebugEntry.setIndexNames(
    (0, "ALCATEL-IND1-LAG-MIB", "alclnkaggAggPortIndex"),
)
if mibBuilder.loadTexts:
    alclnkaggAggPortDebugEntry.setStatus("current")


class _AlclnkaggAggPortDebugRxState_Type(Integer32):
    """Custom type alclnkaggAggPortDebugRxState based on Integer32"""
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
        *(("current", 1),
          ("expired", 2),
          ("defaulted", 3),
          ("initialize", 4),
          ("lacpDisabled", 5),
          ("portDisabled", 6))
    )


_AlclnkaggAggPortDebugRxState_Type.__name__ = "Integer32"
_AlclnkaggAggPortDebugRxState_Object = MibTableColumn
alclnkaggAggPortDebugRxState = _AlclnkaggAggPortDebugRxState_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 13, 1, 1, 2, 3, 1, 1),
    _AlclnkaggAggPortDebugRxState_Type()
)
alclnkaggAggPortDebugRxState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alclnkaggAggPortDebugRxState.setStatus("current")
_AlclnkaggAggPortDebugLastRxTime_Type = TimeTicks
_AlclnkaggAggPortDebugLastRxTime_Object = MibTableColumn
alclnkaggAggPortDebugLastRxTime = _AlclnkaggAggPortDebugLastRxTime_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 13, 1, 1, 2, 3, 1, 2),
    _AlclnkaggAggPortDebugLastRxTime_Type()
)
alclnkaggAggPortDebugLastRxTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alclnkaggAggPortDebugLastRxTime.setStatus("current")


class _AlclnkaggAggPortDebugMuxState_Type(Integer32):
    """Custom type alclnkaggAggPortDebugMuxState based on Integer32"""
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
        *(("detached", 1),
          ("waiting", 2),
          ("attached", 3),
          ("collecting", 4),
          ("distributing", 5),
          ("collectingDistributing", 6))
    )


_AlclnkaggAggPortDebugMuxState_Type.__name__ = "Integer32"
_AlclnkaggAggPortDebugMuxState_Object = MibTableColumn
alclnkaggAggPortDebugMuxState = _AlclnkaggAggPortDebugMuxState_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 13, 1, 1, 2, 3, 1, 3),
    _AlclnkaggAggPortDebugMuxState_Type()
)
alclnkaggAggPortDebugMuxState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alclnkaggAggPortDebugMuxState.setStatus("current")
_AlclnkaggAggPortDebugMuxReason_Type = DisplayString
_AlclnkaggAggPortDebugMuxReason_Object = MibTableColumn
alclnkaggAggPortDebugMuxReason = _AlclnkaggAggPortDebugMuxReason_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 13, 1, 1, 2, 3, 1, 4),
    _AlclnkaggAggPortDebugMuxReason_Type()
)
alclnkaggAggPortDebugMuxReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alclnkaggAggPortDebugMuxReason.setStatus("current")
_AlclnkaggAggPortDebugActorChurnState_Type = ChurnState
_AlclnkaggAggPortDebugActorChurnState_Object = MibTableColumn
alclnkaggAggPortDebugActorChurnState = _AlclnkaggAggPortDebugActorChurnState_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 13, 1, 1, 2, 3, 1, 5),
    _AlclnkaggAggPortDebugActorChurnState_Type()
)
alclnkaggAggPortDebugActorChurnState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alclnkaggAggPortDebugActorChurnState.setStatus("current")
_AlclnkaggAggPortDebugPartnerChurnState_Type = ChurnState
_AlclnkaggAggPortDebugPartnerChurnState_Object = MibTableColumn
alclnkaggAggPortDebugPartnerChurnState = _AlclnkaggAggPortDebugPartnerChurnState_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 13, 1, 1, 2, 3, 1, 6),
    _AlclnkaggAggPortDebugPartnerChurnState_Type()
)
alclnkaggAggPortDebugPartnerChurnState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alclnkaggAggPortDebugPartnerChurnState.setStatus("current")
_AlclnkaggAggPortDebugActorChurnCount_Type = Counter32
_AlclnkaggAggPortDebugActorChurnCount_Object = MibTableColumn
alclnkaggAggPortDebugActorChurnCount = _AlclnkaggAggPortDebugActorChurnCount_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 13, 1, 1, 2, 3, 1, 7),
    _AlclnkaggAggPortDebugActorChurnCount_Type()
)
alclnkaggAggPortDebugActorChurnCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alclnkaggAggPortDebugActorChurnCount.setStatus("current")
_AlclnkaggAggPortDebugPartnerChurnCount_Type = Counter32
_AlclnkaggAggPortDebugPartnerChurnCount_Object = MibTableColumn
alclnkaggAggPortDebugPartnerChurnCount = _AlclnkaggAggPortDebugPartnerChurnCount_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 13, 1, 1, 2, 3, 1, 8),
    _AlclnkaggAggPortDebugPartnerChurnCount_Type()
)
alclnkaggAggPortDebugPartnerChurnCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alclnkaggAggPortDebugPartnerChurnCount.setStatus("current")
_AlclnkaggAggPortDebugActorSyncTransitionCount_Type = Counter32
_AlclnkaggAggPortDebugActorSyncTransitionCount_Object = MibTableColumn
alclnkaggAggPortDebugActorSyncTransitionCount = _AlclnkaggAggPortDebugActorSyncTransitionCount_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 13, 1, 1, 2, 3, 1, 9),
    _AlclnkaggAggPortDebugActorSyncTransitionCount_Type()
)
alclnkaggAggPortDebugActorSyncTransitionCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alclnkaggAggPortDebugActorSyncTransitionCount.setStatus("current")
_AlclnkaggAggPortDebugPartnerSyncTransitionCount_Type = Counter32
_AlclnkaggAggPortDebugPartnerSyncTransitionCount_Object = MibTableColumn
alclnkaggAggPortDebugPartnerSyncTransitionCount = _AlclnkaggAggPortDebugPartnerSyncTransitionCount_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 13, 1, 1, 2, 3, 1, 10),
    _AlclnkaggAggPortDebugPartnerSyncTransitionCount_Type()
)
alclnkaggAggPortDebugPartnerSyncTransitionCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alclnkaggAggPortDebugPartnerSyncTransitionCount.setStatus("current")
_AlclnkaggAggPortDebugActorChangeCount_Type = Counter32
_AlclnkaggAggPortDebugActorChangeCount_Object = MibTableColumn
alclnkaggAggPortDebugActorChangeCount = _AlclnkaggAggPortDebugActorChangeCount_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 13, 1, 1, 2, 3, 1, 11),
    _AlclnkaggAggPortDebugActorChangeCount_Type()
)
alclnkaggAggPortDebugActorChangeCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alclnkaggAggPortDebugActorChangeCount.setStatus("current")
_AlclnkaggAggPortDebugPartnerChangeCount_Type = Counter32
_AlclnkaggAggPortDebugPartnerChangeCount_Object = MibTableColumn
alclnkaggAggPortDebugPartnerChangeCount = _AlclnkaggAggPortDebugPartnerChangeCount_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 13, 1, 1, 2, 3, 1, 12),
    _AlclnkaggAggPortDebugPartnerChangeCount_Type()
)
alclnkaggAggPortDebugPartnerChangeCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alclnkaggAggPortDebugPartnerChangeCount.setStatus("current")
_AlclnkaggTablesLastChanged_Type = TimeTicks
_AlclnkaggTablesLastChanged_Object = MibScalar
alclnkaggTablesLastChanged = _AlclnkaggTablesLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 13, 1, 1, 3),
    _AlclnkaggTablesLastChanged_Type()
)
alclnkaggTablesLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alclnkaggTablesLastChanged.setStatus("current")
_LnkaggNotificationVars_ObjectIdentity = ObjectIdentity
lnkaggNotificationVars = _LnkaggNotificationVars_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 13, 1, 1, 4)
)


class _TraplnkaggAggId_Type(Integer32):
    """Custom type traplnkaggAggId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32),
    )


_TraplnkaggAggId_Type.__name__ = "Integer32"
_TraplnkaggAggId_Object = MibScalar
traplnkaggAggId = _TraplnkaggAggId_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 13, 1, 1, 4, 1),
    _TraplnkaggAggId_Type()
)
traplnkaggAggId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    traplnkaggAggId.setStatus("current")


class _TraplnkaggPortIfIndex_Type(Integer32):
    """Custom type traplnkaggPortIfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_TraplnkaggPortIfIndex_Type.__name__ = "Integer32"
_TraplnkaggPortIfIndex_Object = MibScalar
traplnkaggPortIfIndex = _TraplnkaggPortIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 13, 1, 1, 4, 2),
    _TraplnkaggPortIfIndex_Type()
)
traplnkaggPortIfIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    traplnkaggPortIfIndex.setStatus("current")


class _TraplnkaggLagDownReason_Type(Integer32):
    """Custom type traplnkaggLagDownReason based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("adminDown", 1),
          ("allPortsDown", 2),
          ("minSize", 3))
    )


_TraplnkaggLagDownReason_Type.__name__ = "Integer32"
_TraplnkaggLagDownReason_Object = MibScalar
traplnkaggLagDownReason = _TraplnkaggLagDownReason_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 13, 1, 1, 4, 3),
    _TraplnkaggLagDownReason_Type()
)
traplnkaggLagDownReason.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    traplnkaggLagDownReason.setStatus("current")
_AlclnkaggAggConfig_ObjectIdentity = ObjectIdentity
alclnkaggAggConfig = _AlclnkaggAggConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 13, 1, 1, 5)
)


class _AlclnkAggLocalRangeOperMin_Type(Integer32):
    """Custom type alclnkAggLocalRangeOperMin based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 127),
    )


_AlclnkAggLocalRangeOperMin_Type.__name__ = "Integer32"
_AlclnkAggLocalRangeOperMin_Object = MibScalar
alclnkAggLocalRangeOperMin = _AlclnkAggLocalRangeOperMin_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 13, 1, 1, 5, 1),
    _AlclnkAggLocalRangeOperMin_Type()
)
alclnkAggLocalRangeOperMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alclnkAggLocalRangeOperMin.setStatus("current")


class _AlclnkAggLocalRangeOperMax_Type(Integer32):
    """Custom type alclnkAggLocalRangeOperMax based on Integer32"""
    defaultValue = 127

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 127),
    )


_AlclnkAggLocalRangeOperMax_Type.__name__ = "Integer32"
_AlclnkAggLocalRangeOperMax_Object = MibScalar
alclnkAggLocalRangeOperMax = _AlclnkAggLocalRangeOperMax_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 13, 1, 1, 5, 2),
    _AlclnkAggLocalRangeOperMax_Type()
)
alclnkAggLocalRangeOperMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alclnkAggLocalRangeOperMax.setStatus("current")


class _AlclnkAggLocalRangeConfiguredMin_Type(Integer32):
    """Custom type alclnkAggLocalRangeConfiguredMin based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 127),
    )


_AlclnkAggLocalRangeConfiguredMin_Type.__name__ = "Integer32"
_AlclnkAggLocalRangeConfiguredMin_Object = MibScalar
alclnkAggLocalRangeConfiguredMin = _AlclnkAggLocalRangeConfiguredMin_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 13, 1, 1, 5, 3),
    _AlclnkAggLocalRangeConfiguredMin_Type()
)
alclnkAggLocalRangeConfiguredMin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alclnkAggLocalRangeConfiguredMin.setStatus("current")


class _AlclnkAggLocalRangeConfiguredMax_Type(Integer32):
    """Custom type alclnkAggLocalRangeConfiguredMax based on Integer32"""
    defaultValue = 127

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 127),
    )


_AlclnkAggLocalRangeConfiguredMax_Type.__name__ = "Integer32"
_AlclnkAggLocalRangeConfiguredMax_Object = MibScalar
alclnkAggLocalRangeConfiguredMax = _AlclnkAggLocalRangeConfiguredMax_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 13, 1, 1, 5, 4),
    _AlclnkAggLocalRangeConfiguredMax_Type()
)
alclnkAggLocalRangeConfiguredMax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alclnkAggLocalRangeConfiguredMax.setStatus("current")


class _AlclnkAggPeerRangeOperMin_Type(Integer32):
    """Custom type alclnkAggPeerRangeOperMin based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 127),
    )


_AlclnkAggPeerRangeOperMin_Type.__name__ = "Integer32"
_AlclnkAggPeerRangeOperMin_Object = MibScalar
alclnkAggPeerRangeOperMin = _AlclnkAggPeerRangeOperMin_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 13, 1, 1, 5, 5),
    _AlclnkAggPeerRangeOperMin_Type()
)
alclnkAggPeerRangeOperMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alclnkAggPeerRangeOperMin.setStatus("current")


class _AlclnkAggPeerRangeOperMax_Type(Integer32):
    """Custom type alclnkAggPeerRangeOperMax based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 127),
    )


_AlclnkAggPeerRangeOperMax_Type.__name__ = "Integer32"
_AlclnkAggPeerRangeOperMax_Object = MibScalar
alclnkAggPeerRangeOperMax = _AlclnkAggPeerRangeOperMax_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 13, 1, 1, 5, 6),
    _AlclnkAggPeerRangeOperMax_Type()
)
alclnkAggPeerRangeOperMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alclnkAggPeerRangeOperMax.setStatus("current")


class _AlclnkAggPeerRangeConfiguredMin_Type(Integer32):
    """Custom type alclnkAggPeerRangeConfiguredMin based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 127),
    )


_AlclnkAggPeerRangeConfiguredMin_Type.__name__ = "Integer32"
_AlclnkAggPeerRangeConfiguredMin_Object = MibScalar
alclnkAggPeerRangeConfiguredMin = _AlclnkAggPeerRangeConfiguredMin_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 13, 1, 1, 5, 7),
    _AlclnkAggPeerRangeConfiguredMin_Type()
)
alclnkAggPeerRangeConfiguredMin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alclnkAggPeerRangeConfiguredMin.setStatus("current")


class _AlclnkAggPeerRangeConfiguredMax_Type(Integer32):
    """Custom type alclnkAggPeerRangeConfiguredMax based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 127),
    )


_AlclnkAggPeerRangeConfiguredMax_Type.__name__ = "Integer32"
_AlclnkAggPeerRangeConfiguredMax_Object = MibScalar
alclnkAggPeerRangeConfiguredMax = _AlclnkAggPeerRangeConfiguredMax_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 13, 1, 1, 5, 8),
    _AlclnkAggPeerRangeConfiguredMax_Type()
)
alclnkAggPeerRangeConfiguredMax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alclnkAggPeerRangeConfiguredMax.setStatus("current")


class _AlclnkAggMcLagRangeOperMin_Type(Integer32):
    """Custom type alclnkAggMcLagRangeOperMin based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 127),
    )


_AlclnkAggMcLagRangeOperMin_Type.__name__ = "Integer32"
_AlclnkAggMcLagRangeOperMin_Object = MibScalar
alclnkAggMcLagRangeOperMin = _AlclnkAggMcLagRangeOperMin_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 13, 1, 1, 5, 9),
    _AlclnkAggMcLagRangeOperMin_Type()
)
alclnkAggMcLagRangeOperMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alclnkAggMcLagRangeOperMin.setStatus("current")


class _AlclnkAggMcLagRangeOperMax_Type(Integer32):
    """Custom type alclnkAggMcLagRangeOperMax based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 127),
    )


_AlclnkAggMcLagRangeOperMax_Type.__name__ = "Integer32"
_AlclnkAggMcLagRangeOperMax_Object = MibScalar
alclnkAggMcLagRangeOperMax = _AlclnkAggMcLagRangeOperMax_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 13, 1, 1, 5, 10),
    _AlclnkAggMcLagRangeOperMax_Type()
)
alclnkAggMcLagRangeOperMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alclnkAggMcLagRangeOperMax.setStatus("current")


class _AlclnkAggMcLagRangeConfiguredMin_Type(Integer32):
    """Custom type alclnkAggMcLagRangeConfiguredMin based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 127),
    )


_AlclnkAggMcLagRangeConfiguredMin_Type.__name__ = "Integer32"
_AlclnkAggMcLagRangeConfiguredMin_Object = MibScalar
alclnkAggMcLagRangeConfiguredMin = _AlclnkAggMcLagRangeConfiguredMin_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 13, 1, 1, 5, 11),
    _AlclnkAggMcLagRangeConfiguredMin_Type()
)
alclnkAggMcLagRangeConfiguredMin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alclnkAggMcLagRangeConfiguredMin.setStatus("current")


class _AlclnkAggMcLagRangeConfiguredMax_Type(Integer32):
    """Custom type alclnkAggMcLagRangeConfiguredMax based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 127),
    )


_AlclnkAggMcLagRangeConfiguredMax_Type.__name__ = "Integer32"
_AlclnkAggMcLagRangeConfiguredMax_Object = MibScalar
alclnkAggMcLagRangeConfiguredMax = _AlclnkAggMcLagRangeConfiguredMax_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 13, 1, 1, 5, 12),
    _AlclnkAggMcLagRangeConfiguredMax_Type()
)
alclnkAggMcLagRangeConfiguredMax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alclnkAggMcLagRangeConfiguredMax.setStatus("current")
_AlcatelIND1LAGMIBConformance_ObjectIdentity = ObjectIdentity
alcatelIND1LAGMIBConformance = _AlcatelIND1LAGMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 13, 1, 2)
)
if mibBuilder.loadTexts:
    alcatelIND1LAGMIBConformance.setStatus("current")
_AlcatelIND1LAGMIBGroups_ObjectIdentity = ObjectIdentity
alcatelIND1LAGMIBGroups = _AlcatelIND1LAGMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 13, 1, 2, 1)
)
if mibBuilder.loadTexts:
    alcatelIND1LAGMIBGroups.setStatus("current")
_AlcatelIND1LAGMIBCompliances_ObjectIdentity = ObjectIdentity
alcatelIND1LAGMIBCompliances = _AlcatelIND1LAGMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 13, 1, 2, 2)
)
if mibBuilder.loadTexts:
    alcatelIND1LAGMIBCompliances.setStatus("current")

# Managed Objects groups

alclnkaggAggGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 13, 1, 2, 1, 1)
)
alclnkaggAggGroup.setObjects(
      *(("ALCATEL-IND1-LAG-MIB", "alclnkaggAggActorSystemID"),
        ("ALCATEL-IND1-LAG-MIB", "alclnkaggAggActorSystemPriority"),
        ("ALCATEL-IND1-LAG-MIB", "alclnkaggAggActorAdminKey"),
        ("ALCATEL-IND1-LAG-MIB", "alclnkaggAggMACAddress"),
        ("ALCATEL-IND1-LAG-MIB", "alclnkaggAggActorOperKey"),
        ("ALCATEL-IND1-LAG-MIB", "alclnkaggAggPartnerSystemID"),
        ("ALCATEL-IND1-LAG-MIB", "alclnkaggAggPartnerSystemPriority"),
        ("ALCATEL-IND1-LAG-MIB", "alclnkaggAggPartnerOperKey"),
        ("ALCATEL-IND1-LAG-MIB", "alclnkaggAggId"),
        ("ALCATEL-IND1-LAG-MIB", "alclnkaggAggMinimumSize"),
        ("ALCATEL-IND1-LAG-MIB", "alclnkaggAggPartnerAdminKey"),
        ("ALCATEL-IND1-LAG-MIB", "alclnkaggAggSize"),
        ("ALCATEL-IND1-LAG-MIB", "alclnkaggAggNumber"),
        ("ALCATEL-IND1-LAG-MIB", "alclnkaggAggDescr"),
        ("ALCATEL-IND1-LAG-MIB", "alclnkaggAggName"),
        ("ALCATEL-IND1-LAG-MIB", "alclnkaggAggLacpType"),
        ("ALCATEL-IND1-LAG-MIB", "alclnkaggAggAdminState"),
        ("ALCATEL-IND1-LAG-MIB", "alclnkaggAggOperState"),
        ("ALCATEL-IND1-LAG-MIB", "alclnkaggAggNbrSelectedPorts"),
        ("ALCATEL-IND1-LAG-MIB", "alclnkaggAggNbrAttachedPorts"),
        ("ALCATEL-IND1-LAG-MIB", "alclnkaggAggPrimaryPortIndex"),
        ("ALCATEL-IND1-LAG-MIB", "alclnkaggAggPrimaryPortPosition"),
        ("ALCATEL-IND1-LAG-MIB", "alclnkaggAggPreemptState"),
        ("ALCATEL-IND1-LAG-MIB", "alclnkaggAggPreemptValue"),
        ("ALCATEL-IND1-LAG-MIB", "alclnkaggAggEniActivate"),
        ("ALCATEL-IND1-LAG-MIB", "alclnkaggAggRowStatus"),
        ("ALCATEL-IND1-LAG-MIB", "alclnkaggAggMcLagType"),
        ("ALCATEL-IND1-LAG-MIB", "alclnkaggAggWTRTimer"))
)
if mibBuilder.loadTexts:
    alclnkaggAggGroup.setStatus("current")

alclnkaggAggPortListGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 13, 1, 2, 1, 2)
)
alclnkaggAggPortListGroup.setObjects(
    ("ALCATEL-IND1-LAG-MIB", "alclnkaggAggPortListPorts")
)
if mibBuilder.loadTexts:
    alclnkaggAggPortListGroup.setStatus("current")

alclnkaggAggPortGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 13, 1, 2, 1, 3)
)
alclnkaggAggPortGroup.setObjects(
      *(("ALCATEL-IND1-LAG-MIB", "alclnkaggAggPortActorSystemPriority"),
        ("ALCATEL-IND1-LAG-MIB", "alclnkaggAggPortActorSystemID"),
        ("ALCATEL-IND1-LAG-MIB", "alclnkaggAggPortActorAdminKey"),
        ("ALCATEL-IND1-LAG-MIB", "alclnkaggAggPortActorOperKey"),
        ("ALCATEL-IND1-LAG-MIB", "alclnkaggAggPortPartnerAdminSystemPriority"),
        ("ALCATEL-IND1-LAG-MIB", "alclnkaggAggPortPartnerOperSystemPriority"),
        ("ALCATEL-IND1-LAG-MIB", "alclnkaggAggPortPartnerAdminSystemID"),
        ("ALCATEL-IND1-LAG-MIB", "alclnkaggAggPortPartnerOperSystemID"),
        ("ALCATEL-IND1-LAG-MIB", "alclnkaggAggPortPartnerAdminKey"),
        ("ALCATEL-IND1-LAG-MIB", "alclnkaggAggPortPartnerOperKey"),
        ("ALCATEL-IND1-LAG-MIB", "alclnkaggAggPortSelectedAggID"),
        ("ALCATEL-IND1-LAG-MIB", "alclnkaggAggPortAttachedAggID"),
        ("ALCATEL-IND1-LAG-MIB", "alclnkaggAggPortActorPort"),
        ("ALCATEL-IND1-LAG-MIB", "alclnkaggAggPortActorPortPriority"),
        ("ALCATEL-IND1-LAG-MIB", "alclnkaggAggPortPartnerAdminPort"),
        ("ALCATEL-IND1-LAG-MIB", "alclnkaggAggPortPartnerOperPort"),
        ("ALCATEL-IND1-LAG-MIB", "alclnkaggAggPortPartnerAdminPortPriority"),
        ("ALCATEL-IND1-LAG-MIB", "alclnkaggAggPortPartnerOperPortPriority"),
        ("ALCATEL-IND1-LAG-MIB", "alclnkaggAggPortActorAdminState"),
        ("ALCATEL-IND1-LAG-MIB", "alclnkaggAggPortActorOperState"),
        ("ALCATEL-IND1-LAG-MIB", "alclnkaggAggPortPartnerAdminState"),
        ("ALCATEL-IND1-LAG-MIB", "alclnkaggAggPortPartnerOperState"),
        ("ALCATEL-IND1-LAG-MIB", "alclnkaggAggPortSelectedAggNumber"),
        ("ALCATEL-IND1-LAG-MIB", "alclnkaggAggPortGlobalPortNumber"),
        ("ALCATEL-IND1-LAG-MIB", "alclnkaggAggPortAdminState"),
        ("ALCATEL-IND1-LAG-MIB", "alclnkaggAggPortOperState"),
        ("ALCATEL-IND1-LAG-MIB", "alclnkaggAggPortState"),
        ("ALCATEL-IND1-LAG-MIB", "alclnkaggAggPortLinkState"),
        ("ALCATEL-IND1-LAG-MIB", "alclnkaggAggPortPrimary"),
        ("ALCATEL-IND1-LAG-MIB", "alclnkaggAggPortLacpType"),
        ("ALCATEL-IND1-LAG-MIB", "alclnkaggAggPortStandbyState"),
        ("ALCATEL-IND1-LAG-MIB", "alclnkaggAggPortRowStatus"),
        ("ALCATEL-IND1-LAG-MIB", "alclnkaggAggPortMcLagType"))
)
if mibBuilder.loadTexts:
    alclnkaggAggPortGroup.setStatus("current")

alclnkaggAggPortStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 13, 1, 2, 1, 4)
)
alclnkaggAggPortStatsGroup.setObjects(
      *(("ALCATEL-IND1-LAG-MIB", "alclnkaggAggPortStatsLACPDUsRx"),
        ("ALCATEL-IND1-LAG-MIB", "alclnkaggAggPortStatsMarkerPDUsRx"),
        ("ALCATEL-IND1-LAG-MIB", "alclnkaggAggPortStatsMarkerResponsePDUsRx"),
        ("ALCATEL-IND1-LAG-MIB", "alclnkaggAggPortStatsUnknownRx"),
        ("ALCATEL-IND1-LAG-MIB", "alclnkaggAggPortStatsIllegalRx"),
        ("ALCATEL-IND1-LAG-MIB", "alclnkaggAggPortStatsLACPDUsTx"),
        ("ALCATEL-IND1-LAG-MIB", "alclnkaggAggPortStatsMarkerPDUsTx"),
        ("ALCATEL-IND1-LAG-MIB", "alclnkaggAggPortStatsMarkerResponsePDUsTx"))
)
if mibBuilder.loadTexts:
    alclnkaggAggPortStatsGroup.setStatus("current")

alclnkaggAggPortDebugGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 13, 1, 2, 1, 5)
)
alclnkaggAggPortDebugGroup.setObjects(
      *(("ALCATEL-IND1-LAG-MIB", "alclnkaggAggPortDebugRxState"),
        ("ALCATEL-IND1-LAG-MIB", "alclnkaggAggPortDebugLastRxTime"),
        ("ALCATEL-IND1-LAG-MIB", "alclnkaggAggPortDebugActorChurnState"),
        ("ALCATEL-IND1-LAG-MIB", "alclnkaggAggPortDebugPartnerChurnState"),
        ("ALCATEL-IND1-LAG-MIB", "alclnkaggAggPortDebugActorChurnCount"),
        ("ALCATEL-IND1-LAG-MIB", "alclnkaggAggPortDebugPartnerChurnCount"),
        ("ALCATEL-IND1-LAG-MIB", "alclnkaggAggPortDebugActorSyncTransitionCount"),
        ("ALCATEL-IND1-LAG-MIB", "alclnkaggAggPortDebugPartnerSyncTransitionCount"),
        ("ALCATEL-IND1-LAG-MIB", "alclnkaggAggPortDebugActorChangeCount"),
        ("ALCATEL-IND1-LAG-MIB", "alclnkaggAggPortDebugPartnerChangeCount"),
        ("ALCATEL-IND1-LAG-MIB", "alclnkaggAggPortDebugMuxReason"),
        ("ALCATEL-IND1-LAG-MIB", "alclnkaggAggPortDebugMuxState"))
)
if mibBuilder.loadTexts:
    alclnkaggAggPortDebugGroup.setStatus("current")

alclnkaggTablesLastChangedGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 13, 1, 2, 1, 6)
)
alclnkaggTablesLastChangedGroup.setObjects(
    ("ALCATEL-IND1-LAG-MIB", "alclnkaggTablesLastChanged")
)
if mibBuilder.loadTexts:
    alclnkaggTablesLastChangedGroup.setStatus("current")

lnkaggNotificationVarsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 13, 1, 2, 1, 7)
)
lnkaggNotificationVarsGroup.setObjects(
      *(("ALCATEL-IND1-LAG-MIB", "traplnkaggAggId"),
        ("ALCATEL-IND1-LAG-MIB", "traplnkaggPortIfIndex"),
        ("ALCATEL-IND1-LAG-MIB", "traplnkaggLagDownReason"))
)
if mibBuilder.loadTexts:
    lnkaggNotificationVarsGroup.setStatus("current")

alclnkaggSlotGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 13, 1, 2, 1, 9)
)
alclnkaggSlotGroup.setObjects(
      *(("ALCATEL-IND1-LAG-MIB", "alclnkaggSlotStatus"),
        ("ALCATEL-IND1-LAG-MIB", "alclnkaggMultipleAggPerSlot"))
)
if mibBuilder.loadTexts:
    alclnkaggSlotGroup.setStatus("current")

alclnkaggAggConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 13, 1, 2, 1, 10)
)
alclnkaggAggConfigGroup.setObjects(
      *(("ALCATEL-IND1-LAG-MIB", "alclnkAggLocalRangeOperMin"),
        ("ALCATEL-IND1-LAG-MIB", "alclnkAggLocalRangeOperMax"),
        ("ALCATEL-IND1-LAG-MIB", "alclnkAggLocalRangeConfiguredMin"),
        ("ALCATEL-IND1-LAG-MIB", "alclnkAggLocalRangeConfiguredMax"),
        ("ALCATEL-IND1-LAG-MIB", "alclnkAggPeerRangeOperMin"),
        ("ALCATEL-IND1-LAG-MIB", "alclnkAggPeerRangeOperMax"),
        ("ALCATEL-IND1-LAG-MIB", "alclnkAggPeerRangeConfiguredMin"),
        ("ALCATEL-IND1-LAG-MIB", "alclnkAggPeerRangeConfiguredMax"),
        ("ALCATEL-IND1-LAG-MIB", "alclnkAggMcLagRangeOperMin"),
        ("ALCATEL-IND1-LAG-MIB", "alclnkAggMcLagRangeOperMax"),
        ("ALCATEL-IND1-LAG-MIB", "alclnkAggMcLagRangeConfiguredMin"),
        ("ALCATEL-IND1-LAG-MIB", "alclnkAggMcLagRangeConfiguredMax"))
)
if mibBuilder.loadTexts:
    alclnkaggAggConfigGroup.setStatus("current")

alclnkaggAggIdAccountGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 13, 1, 2, 1, 11)
)
alclnkaggAggIdAccountGroup.setObjects(
      *(("ALCATEL-IND1-LAG-MIB", "alcRxUndersize"),
        ("ALCATEL-IND1-LAG-MIB", "alcTxUndersize"),
        ("ALCATEL-IND1-LAG-MIB", "alcRxOversize"),
        ("ALCATEL-IND1-LAG-MIB", "alcTxOversize"),
        ("ALCATEL-IND1-LAG-MIB", "alcRxPackets64"),
        ("ALCATEL-IND1-LAG-MIB", "alcRxPackets127"),
        ("ALCATEL-IND1-LAG-MIB", "alcRxPackets255"),
        ("ALCATEL-IND1-LAG-MIB", "alcRxPackets511"),
        ("ALCATEL-IND1-LAG-MIB", "alcRxPackets1023"),
        ("ALCATEL-IND1-LAG-MIB", "alcRxPacketsMax"))
)
if mibBuilder.loadTexts:
    alclnkaggAggIdAccountGroup.setStatus("current")

alclnkaggAggIdCounterGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 13, 1, 2, 1, 12)
)
alclnkaggAggIdCounterGroup.setObjects(
      *(("ALCATEL-IND1-LAG-MIB", "alcInOctets"),
        ("ALCATEL-IND1-LAG-MIB", "alcOutOctets"),
        ("ALCATEL-IND1-LAG-MIB", "alcInUcastPkts"),
        ("ALCATEL-IND1-LAG-MIB", "alcOutUcastPkts"),
        ("ALCATEL-IND1-LAG-MIB", "alcInMcastPkts"),
        ("ALCATEL-IND1-LAG-MIB", "alcOutMcastPkts"),
        ("ALCATEL-IND1-LAG-MIB", "alcInBcastPkts"),
        ("ALCATEL-IND1-LAG-MIB", "alcOutBcastPkts"),
        ("ALCATEL-IND1-LAG-MIB", "alcInPauseFrames"),
        ("ALCATEL-IND1-LAG-MIB", "alcOutPauseFrames"))
)
if mibBuilder.loadTexts:
    alclnkaggAggIdCounterGroup.setStatus("current")

alclnkaggAggIdCounterErrGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 13, 1, 2, 1, 13)
)
alclnkaggAggIdCounterErrGroup.setObjects(
      *(("ALCATEL-IND1-LAG-MIB", "alcAlignmentsErrors"),
        ("ALCATEL-IND1-LAG-MIB", "alcFCSErrors"),
        ("ALCATEL-IND1-LAG-MIB", "alcIfInErrors"),
        ("ALCATEL-IND1-LAG-MIB", "alcIfOutErrors"))
)
if mibBuilder.loadTexts:
    alclnkaggAggIdCounterErrGroup.setStatus("current")

alclnkaggAggIdTrafficGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 13, 1, 2, 1, 14)
)
alclnkaggAggIdTrafficGroup.setObjects(
      *(("ALCATEL-IND1-LAG-MIB", "alcInputPackets"),
        ("ALCATEL-IND1-LAG-MIB", "alcInputBytes"),
        ("ALCATEL-IND1-LAG-MIB", "alcOutputPackets"),
        ("ALCATEL-IND1-LAG-MIB", "alcOutputBytes"))
)
if mibBuilder.loadTexts:
    alclnkaggAggIdTrafficGroup.setStatus("current")

alcLagStatsMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 13, 1, 2, 1, 15)
)
alcLagStatsMIBGroup.setObjects(
    ("ALCATEL-IND1-LAG-MIB", "alcLagClearStats")
)
if mibBuilder.loadTexts:
    alcLagStatsMIBGroup.setStatus("current")


# Notification objects

lnkaggAggUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 3, 2, 14, 0, 1)
)
lnkaggAggUp.setObjects(
      *(("ALCATEL-IND1-LAG-MIB", "traplnkaggAggId"),
        ("ALCATEL-IND1-LAG-MIB", "traplnkaggPortIfIndex"))
)
if mibBuilder.loadTexts:
    lnkaggAggUp.setStatus(
        "current"
    )

lnkaggAggDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 3, 2, 14, 0, 2)
)
lnkaggAggDown.setObjects(
      *(("ALCATEL-IND1-LAG-MIB", "traplnkaggAggId"),
        ("ALCATEL-IND1-LAG-MIB", "traplnkaggPortIfIndex"),
        ("ALCATEL-IND1-LAG-MIB", "traplnkaggLagDownReason"))
)
if mibBuilder.loadTexts:
    lnkaggAggDown.setStatus(
        "current"
    )

lnkaggPortJoin = NotificationType(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 3, 2, 14, 0, 3)
)
lnkaggPortJoin.setObjects(
      *(("ALCATEL-IND1-LAG-MIB", "traplnkaggAggId"),
        ("ALCATEL-IND1-LAG-MIB", "traplnkaggPortIfIndex"))
)
if mibBuilder.loadTexts:
    lnkaggPortJoin.setStatus(
        "current"
    )

lnkaggPortLeave = NotificationType(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 3, 2, 14, 0, 4)
)
lnkaggPortLeave.setObjects(
      *(("ALCATEL-IND1-LAG-MIB", "traplnkaggAggId"),
        ("ALCATEL-IND1-LAG-MIB", "traplnkaggPortIfIndex"))
)
if mibBuilder.loadTexts:
    lnkaggPortLeave.setStatus(
        "current"
    )

lnkaggPortRemove = NotificationType(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 3, 2, 14, 0, 5)
)
lnkaggPortRemove.setObjects(
      *(("ALCATEL-IND1-LAG-MIB", "traplnkaggAggId"),
        ("ALCATEL-IND1-LAG-MIB", "traplnkaggPortIfIndex"))
)
if mibBuilder.loadTexts:
    lnkaggPortRemove.setStatus(
        "current"
    )

lnkaggPortReserve = NotificationType(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 3, 2, 14, 0, 6)
)
lnkaggPortReserve.setObjects(
      *(("ALCATEL-IND1-LAG-MIB", "traplnkaggAggId"),
        ("ALCATEL-IND1-LAG-MIB", "traplnkaggPortIfIndex"))
)
if mibBuilder.loadTexts:
    lnkaggPortReserve.setStatus(
        "current"
    )


# Notifications groups

lnkaggTrapsGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 13, 1, 2, 1, 8)
)
lnkaggTrapsGroup.setObjects(
      *(("ALCATEL-IND1-LAG-MIB", "lnkaggAggUp"),
        ("ALCATEL-IND1-LAG-MIB", "lnkaggAggDown"),
        ("ALCATEL-IND1-LAG-MIB", "lnkaggPortJoin"),
        ("ALCATEL-IND1-LAG-MIB", "lnkaggPortLeave"),
        ("ALCATEL-IND1-LAG-MIB", "lnkaggPortRemove"),
        ("ALCATEL-IND1-LAG-MIB", "lnkaggPortReserve"))
)
if mibBuilder.loadTexts:
    lnkaggTrapsGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

alclnkaggAggCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 13, 1, 2, 2, 1)
)
alclnkaggAggCompliance.setObjects(
      *(("ALCATEL-IND1-LAG-MIB", "alclnkaggAggGroup"),
        ("ALCATEL-IND1-LAG-MIB", "alclnkaggAggPortGroup"),
        ("ALCATEL-IND1-LAG-MIB", "alclnkaggTablesLastChangedGroup"),
        ("ALCATEL-IND1-LAG-MIB", "lnkaggNotificationVarsGroup"),
        ("ALCATEL-IND1-LAG-MIB", "alclnkaggSlotGroup"),
        ("ALCATEL-IND1-LAG-MIB", "alclnkaggAggPortListGroup"),
        ("ALCATEL-IND1-LAG-MIB", "alclnkaggAggPortStatsGroup"),
        ("ALCATEL-IND1-LAG-MIB", "alclnkaggAggPortDebugGroup"),
        ("ALCATEL-IND1-LAG-MIB", "alclnkaggAggConfigGroup"))
)
if mibBuilder.loadTexts:
    alclnkaggAggCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ALCATEL-IND1-LAG-MIB",
    **{"LacpType": LacpType,
       "McLagType": McLagType,
       "alcatelIND1LAGMIB": alcatelIND1LAGMIB,
       "alcatelIND1LAGMIBObjects": alcatelIND1LAGMIBObjects,
       "alclnkaggAgg": alclnkaggAgg,
       "alclnkaggAggTable": alclnkaggAggTable,
       "alclnkaggAggEntry": alclnkaggAggEntry,
       "alclnkaggAggIndex": alclnkaggAggIndex,
       "alclnkaggAggMACAddress": alclnkaggAggMACAddress,
       "alclnkaggAggActorSystemPriority": alclnkaggAggActorSystemPriority,
       "alclnkaggAggActorSystemID": alclnkaggAggActorSystemID,
       "alclnkaggAggPartnerAdminKey": alclnkaggAggPartnerAdminKey,
       "alclnkaggAggActorAdminKey": alclnkaggAggActorAdminKey,
       "alclnkaggAggActorOperKey": alclnkaggAggActorOperKey,
       "alclnkaggAggPartnerSystemID": alclnkaggAggPartnerSystemID,
       "alclnkaggAggPartnerSystemPriority": alclnkaggAggPartnerSystemPriority,
       "alclnkaggAggPartnerOperKey": alclnkaggAggPartnerOperKey,
       "alclnkaggAggSize": alclnkaggAggSize,
       "alclnkaggAggNumber": alclnkaggAggNumber,
       "alclnkaggAggDescr": alclnkaggAggDescr,
       "alclnkaggAggName": alclnkaggAggName,
       "alclnkaggAggLacpType": alclnkaggAggLacpType,
       "alclnkaggAggAdminState": alclnkaggAggAdminState,
       "alclnkaggAggOperState": alclnkaggAggOperState,
       "alclnkaggAggNbrSelectedPorts": alclnkaggAggNbrSelectedPorts,
       "alclnkaggAggNbrAttachedPorts": alclnkaggAggNbrAttachedPorts,
       "alclnkaggAggPrimaryPortIndex": alclnkaggAggPrimaryPortIndex,
       "alclnkaggAggPrimaryPortPosition": alclnkaggAggPrimaryPortPosition,
       "alclnkaggAggRowStatus": alclnkaggAggRowStatus,
       "alclnkaggAggPreemptState": alclnkaggAggPreemptState,
       "alclnkaggAggPreemptValue": alclnkaggAggPreemptValue,
       "alclnkaggAggMinimumSize": alclnkaggAggMinimumSize,
       "alclnkaggAggMcLagType": alclnkaggAggMcLagType,
       "alclnkaggAggWTRTimer": alclnkaggAggWTRTimer,
       "alclnkaggAggPortListTable": alclnkaggAggPortListTable,
       "alclnkaggAggPortListEntry": alclnkaggAggPortListEntry,
       "alclnkaggAggPortListPorts": alclnkaggAggPortListPorts,
       "alclnkaggAggEniActivate": alclnkaggAggEniActivate,
       "alclnkaggSlotTable": alclnkaggSlotTable,
       "alclnkaggSlotEntry": alclnkaggSlotEntry,
       "alclnkaggSlotNum": alclnkaggSlotNum,
       "alclnkaggSlotStatus": alclnkaggSlotStatus,
       "alclnkaggMultipleAggPerSlot": alclnkaggMultipleAggPerSlot,
       "alclnkaggAggIdIfIndexTable": alclnkaggAggIdIfIndexTable,
       "alclnkaggAggIdIfIndexEntry": alclnkaggAggIdIfIndexEntry,
       "alclnkaggIfIndex": alclnkaggIfIndex,
       "alclnkaggAggId": alclnkaggAggId,
       "alclnkaggAggIdAccountTable": alclnkaggAggIdAccountTable,
       "alclnkaggAggIdAccountEntry": alclnkaggAggIdAccountEntry,
       "alcRxUndersize": alcRxUndersize,
       "alcTxUndersize": alcTxUndersize,
       "alcRxOversize": alcRxOversize,
       "alcTxOversize": alcTxOversize,
       "alcRxPackets64": alcRxPackets64,
       "alcRxPackets127": alcRxPackets127,
       "alcRxPackets255": alcRxPackets255,
       "alcRxPackets511": alcRxPackets511,
       "alcRxPackets1023": alcRxPackets1023,
       "alcRxPacketsMax": alcRxPacketsMax,
       "alcRxJabberFrames": alcRxJabberFrames,
       "alclnkaggAggIdCounterTable": alclnkaggAggIdCounterTable,
       "alclnkaggAggIdCounterEntry": alclnkaggAggIdCounterEntry,
       "alcInOctets": alcInOctets,
       "alcOutOctets": alcOutOctets,
       "alcInUcastPkts": alcInUcastPkts,
       "alcOutUcastPkts": alcOutUcastPkts,
       "alcInMcastPkts": alcInMcastPkts,
       "alcOutMcastPkts": alcOutMcastPkts,
       "alcInBcastPkts": alcInBcastPkts,
       "alcOutBcastPkts": alcOutBcastPkts,
       "alcInPauseFrames": alcInPauseFrames,
       "alcOutPauseFrames": alcOutPauseFrames,
       "alclnkaggAggIdCounterErrTable": alclnkaggAggIdCounterErrTable,
       "alclnkaggAggIdCounterErrEntry": alclnkaggAggIdCounterErrEntry,
       "alcAlignmentsErrors": alcAlignmentsErrors,
       "alcFCSErrors": alcFCSErrors,
       "alcIfInErrors": alcIfInErrors,
       "alcIfOutErrors": alcIfOutErrors,
       "alclnkaggAggIdTrafficTable": alclnkaggAggIdTrafficTable,
       "alclnkaggAggIdTrafficEntry": alclnkaggAggIdTrafficEntry,
       "alcInputPackets": alcInputPackets,
       "alcInputBytes": alcInputBytes,
       "alcOutputPackets": alcOutputPackets,
       "alcOutputBytes": alcOutputBytes,
       "alcLagStatsTable": alcLagStatsTable,
       "alcLagStatsEntry": alcLagStatsEntry,
       "alcLagClearStats": alcLagClearStats,
       "alclnkaggAggPort": alclnkaggAggPort,
       "alclnkaggAggPortTable": alclnkaggAggPortTable,
       "alclnkaggAggPortEntry": alclnkaggAggPortEntry,
       "alclnkaggAggPortIndex": alclnkaggAggPortIndex,
       "alclnkaggAggPortActorSystemPriority": alclnkaggAggPortActorSystemPriority,
       "alclnkaggAggPortActorSystemID": alclnkaggAggPortActorSystemID,
       "alclnkaggAggPortActorAdminKey": alclnkaggAggPortActorAdminKey,
       "alclnkaggAggPortActorOperKey": alclnkaggAggPortActorOperKey,
       "alclnkaggAggPortPartnerAdminSystemPriority": alclnkaggAggPortPartnerAdminSystemPriority,
       "alclnkaggAggPortPartnerOperSystemPriority": alclnkaggAggPortPartnerOperSystemPriority,
       "alclnkaggAggPortPartnerAdminSystemID": alclnkaggAggPortPartnerAdminSystemID,
       "alclnkaggAggPortPartnerOperSystemID": alclnkaggAggPortPartnerOperSystemID,
       "alclnkaggAggPortPartnerAdminKey": alclnkaggAggPortPartnerAdminKey,
       "alclnkaggAggPortPartnerOperKey": alclnkaggAggPortPartnerOperKey,
       "alclnkaggAggPortSelectedAggID": alclnkaggAggPortSelectedAggID,
       "alclnkaggAggPortAttachedAggID": alclnkaggAggPortAttachedAggID,
       "alclnkaggAggPortActorPort": alclnkaggAggPortActorPort,
       "alclnkaggAggPortActorPortPriority": alclnkaggAggPortActorPortPriority,
       "alclnkaggAggPortPartnerAdminPort": alclnkaggAggPortPartnerAdminPort,
       "alclnkaggAggPortPartnerOperPort": alclnkaggAggPortPartnerOperPort,
       "alclnkaggAggPortPartnerAdminPortPriority": alclnkaggAggPortPartnerAdminPortPriority,
       "alclnkaggAggPortPartnerOperPortPriority": alclnkaggAggPortPartnerOperPortPriority,
       "alclnkaggAggPortActorAdminState": alclnkaggAggPortActorAdminState,
       "alclnkaggAggPortActorOperState": alclnkaggAggPortActorOperState,
       "alclnkaggAggPortPartnerAdminState": alclnkaggAggPortPartnerAdminState,
       "alclnkaggAggPortPartnerOperState": alclnkaggAggPortPartnerOperState,
       "alclnkaggAggPortSelectedAggNumber": alclnkaggAggPortSelectedAggNumber,
       "alclnkaggAggPortGlobalPortNumber": alclnkaggAggPortGlobalPortNumber,
       "alclnkaggAggPortAdminState": alclnkaggAggPortAdminState,
       "alclnkaggAggPortOperState": alclnkaggAggPortOperState,
       "alclnkaggAggPortState": alclnkaggAggPortState,
       "alclnkaggAggPortLinkState": alclnkaggAggPortLinkState,
       "alclnkaggAggPortPrimary": alclnkaggAggPortPrimary,
       "alclnkaggAggPortLacpType": alclnkaggAggPortLacpType,
       "alclnkaggAggPortRowStatus": alclnkaggAggPortRowStatus,
       "alclnkaggAggPortStandbyState": alclnkaggAggPortStandbyState,
       "alclnkaggAggPortMcLagType": alclnkaggAggPortMcLagType,
       "alclnkaggAggPortStatsTable": alclnkaggAggPortStatsTable,
       "alclnkaggAggPortStatsEntry": alclnkaggAggPortStatsEntry,
       "alclnkaggAggPortStatsLACPDUsRx": alclnkaggAggPortStatsLACPDUsRx,
       "alclnkaggAggPortStatsMarkerPDUsRx": alclnkaggAggPortStatsMarkerPDUsRx,
       "alclnkaggAggPortStatsMarkerResponsePDUsRx": alclnkaggAggPortStatsMarkerResponsePDUsRx,
       "alclnkaggAggPortStatsUnknownRx": alclnkaggAggPortStatsUnknownRx,
       "alclnkaggAggPortStatsIllegalRx": alclnkaggAggPortStatsIllegalRx,
       "alclnkaggAggPortStatsLACPDUsTx": alclnkaggAggPortStatsLACPDUsTx,
       "alclnkaggAggPortStatsMarkerPDUsTx": alclnkaggAggPortStatsMarkerPDUsTx,
       "alclnkaggAggPortStatsMarkerResponsePDUsTx": alclnkaggAggPortStatsMarkerResponsePDUsTx,
       "alclnkaggAggPortDebugTable": alclnkaggAggPortDebugTable,
       "alclnkaggAggPortDebugEntry": alclnkaggAggPortDebugEntry,
       "alclnkaggAggPortDebugRxState": alclnkaggAggPortDebugRxState,
       "alclnkaggAggPortDebugLastRxTime": alclnkaggAggPortDebugLastRxTime,
       "alclnkaggAggPortDebugMuxState": alclnkaggAggPortDebugMuxState,
       "alclnkaggAggPortDebugMuxReason": alclnkaggAggPortDebugMuxReason,
       "alclnkaggAggPortDebugActorChurnState": alclnkaggAggPortDebugActorChurnState,
       "alclnkaggAggPortDebugPartnerChurnState": alclnkaggAggPortDebugPartnerChurnState,
       "alclnkaggAggPortDebugActorChurnCount": alclnkaggAggPortDebugActorChurnCount,
       "alclnkaggAggPortDebugPartnerChurnCount": alclnkaggAggPortDebugPartnerChurnCount,
       "alclnkaggAggPortDebugActorSyncTransitionCount": alclnkaggAggPortDebugActorSyncTransitionCount,
       "alclnkaggAggPortDebugPartnerSyncTransitionCount": alclnkaggAggPortDebugPartnerSyncTransitionCount,
       "alclnkaggAggPortDebugActorChangeCount": alclnkaggAggPortDebugActorChangeCount,
       "alclnkaggAggPortDebugPartnerChangeCount": alclnkaggAggPortDebugPartnerChangeCount,
       "alclnkaggTablesLastChanged": alclnkaggTablesLastChanged,
       "lnkaggNotificationVars": lnkaggNotificationVars,
       "traplnkaggAggId": traplnkaggAggId,
       "traplnkaggPortIfIndex": traplnkaggPortIfIndex,
       "traplnkaggLagDownReason": traplnkaggLagDownReason,
       "alclnkaggAggConfig": alclnkaggAggConfig,
       "alclnkAggLocalRangeOperMin": alclnkAggLocalRangeOperMin,
       "alclnkAggLocalRangeOperMax": alclnkAggLocalRangeOperMax,
       "alclnkAggLocalRangeConfiguredMin": alclnkAggLocalRangeConfiguredMin,
       "alclnkAggLocalRangeConfiguredMax": alclnkAggLocalRangeConfiguredMax,
       "alclnkAggPeerRangeOperMin": alclnkAggPeerRangeOperMin,
       "alclnkAggPeerRangeOperMax": alclnkAggPeerRangeOperMax,
       "alclnkAggPeerRangeConfiguredMin": alclnkAggPeerRangeConfiguredMin,
       "alclnkAggPeerRangeConfiguredMax": alclnkAggPeerRangeConfiguredMax,
       "alclnkAggMcLagRangeOperMin": alclnkAggMcLagRangeOperMin,
       "alclnkAggMcLagRangeOperMax": alclnkAggMcLagRangeOperMax,
       "alclnkAggMcLagRangeConfiguredMin": alclnkAggMcLagRangeConfiguredMin,
       "alclnkAggMcLagRangeConfiguredMax": alclnkAggMcLagRangeConfiguredMax,
       "alcatelIND1LAGMIBConformance": alcatelIND1LAGMIBConformance,
       "alcatelIND1LAGMIBGroups": alcatelIND1LAGMIBGroups,
       "alclnkaggAggGroup": alclnkaggAggGroup,
       "alclnkaggAggPortListGroup": alclnkaggAggPortListGroup,
       "alclnkaggAggPortGroup": alclnkaggAggPortGroup,
       "alclnkaggAggPortStatsGroup": alclnkaggAggPortStatsGroup,
       "alclnkaggAggPortDebugGroup": alclnkaggAggPortDebugGroup,
       "alclnkaggTablesLastChangedGroup": alclnkaggTablesLastChangedGroup,
       "lnkaggNotificationVarsGroup": lnkaggNotificationVarsGroup,
       "lnkaggTrapsGroup": lnkaggTrapsGroup,
       "alclnkaggSlotGroup": alclnkaggSlotGroup,
       "alclnkaggAggConfigGroup": alclnkaggAggConfigGroup,
       "alclnkaggAggIdAccountGroup": alclnkaggAggIdAccountGroup,
       "alclnkaggAggIdCounterGroup": alclnkaggAggIdCounterGroup,
       "alclnkaggAggIdCounterErrGroup": alclnkaggAggIdCounterErrGroup,
       "alclnkaggAggIdTrafficGroup": alclnkaggAggIdTrafficGroup,
       "alcLagStatsMIBGroup": alcLagStatsMIBGroup,
       "alcatelIND1LAGMIBCompliances": alcatelIND1LAGMIBCompliances,
       "alclnkaggAggCompliance": alclnkaggAggCompliance,
       "lnkaggAggUp": lnkaggAggUp,
       "lnkaggAggDown": lnkaggAggDown,
       "lnkaggPortJoin": lnkaggPortJoin,
       "lnkaggPortLeave": lnkaggPortLeave,
       "lnkaggPortRemove": lnkaggPortRemove,
       "lnkaggPortReserve": lnkaggPortReserve}
)
