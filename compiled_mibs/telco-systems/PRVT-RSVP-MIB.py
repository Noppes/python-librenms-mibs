# SNMP MIB module (PRVT-RSVP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\telco-systems\binos\PRVT-RSVP-MIB

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

(InterfaceIndexOrZero,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndexOrZero")

(InetAddressIPv6,) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddressIPv6")

(mpls,) = mibBuilder.importSymbols(
    "PRVT-CR-LDP-MIB",
    "mpls")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

prvtRsvp = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 7)
)
if mibBuilder.loadTexts:
    prvtRsvp.setRevisions(
        ("2008-04-14 00:00",
         "2006-06-02 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class PrvtRsvpAdminStatus(TextualConvention, Integer32):
    status = "current"
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



class PrvtRsvpOperStatus(TextualConvention, Integer32):
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
        *(("up", 1),
          ("down", 2),
          ("goingUp", 3),
          ("goingDown", 4),
          ("actFailed", 5))
    )



class PrvtRsvpIndex(TextualConvention, Unsigned32):
    status = "current"


class PrvtRsvpDiagReqIndex(TextualConvention, Unsigned32):
    status = "current"


class PrvtRsvpDiagNodeIndexType(TextualConvention, Unsigned32):
    status = "current"


class PrvtRsvpDiagNodeTypeVal(TextualConvention, Integer32):
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
        *(("missing", 1),
          ("ingress", 2),
          ("transit", 3),
          ("egress", 4))
    )



# MIB Managed Objects in the order of their OIDs

_PrvtRsvpObjects_ObjectIdentity = ObjectIdentity
prvtRsvpObjects = _PrvtRsvpObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 7, 1)
)
_PrvtRsvpProductTable_Object = MibTable
prvtRsvpProductTable = _PrvtRsvpProductTable_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 7, 1, 1)
)
if mibBuilder.loadTexts:
    prvtRsvpProductTable.setStatus("current")
_PrvtRsvpProductEntry_Object = MibTableRow
prvtRsvpProductEntry = _PrvtRsvpProductEntry_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 7, 1, 1, 1)
)
prvtRsvpProductEntry.setIndexNames(
    (0, "PRVT-RSVP-MIB", "prvtRsvpProductIndex"),
)
if mibBuilder.loadTexts:
    prvtRsvpProductEntry.setStatus("current")
_PrvtRsvpProductIndex_Type = PrvtRsvpIndex
_PrvtRsvpProductIndex_Object = MibTableColumn
prvtRsvpProductIndex = _PrvtRsvpProductIndex_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 7, 1, 1, 1, 1),
    _PrvtRsvpProductIndex_Type()
)
prvtRsvpProductIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    prvtRsvpProductIndex.setStatus("current")


class _PrvtRsvpProductASNumber_Type(Integer32):
    """Custom type prvtRsvpProductASNumber based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_PrvtRsvpProductASNumber_Type.__name__ = "Integer32"
_PrvtRsvpProductASNumber_Object = MibTableColumn
prvtRsvpProductASNumber = _PrvtRsvpProductASNumber_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 7, 1, 1, 1, 2),
    _PrvtRsvpProductASNumber_Type()
)
prvtRsvpProductASNumber.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    prvtRsvpProductASNumber.setStatus("current")


class _PrvtRsvpProductSenderTTL_Type(Integer32):
    """Custom type prvtRsvpProductSenderTTL based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_PrvtRsvpProductSenderTTL_Type.__name__ = "Integer32"
_PrvtRsvpProductSenderTTL_Object = MibTableColumn
prvtRsvpProductSenderTTL = _PrvtRsvpProductSenderTTL_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 7, 1, 1, 1, 3),
    _PrvtRsvpProductSenderTTL_Type()
)
prvtRsvpProductSenderTTL.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    prvtRsvpProductSenderTTL.setStatus("current")


class _PrvtRsvpProductMinTimerPeriod_Type(Integer32):
    """Custom type prvtRsvpProductMinTimerPeriod based on Integer32"""
    defaultValue = 200


_PrvtRsvpProductMinTimerPeriod_Type.__name__ = "Integer32"
_PrvtRsvpProductMinTimerPeriod_Object = MibTableColumn
prvtRsvpProductMinTimerPeriod = _PrvtRsvpProductMinTimerPeriod_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 7, 1, 1, 1, 4),
    _PrvtRsvpProductMinTimerPeriod_Type()
)
prvtRsvpProductMinTimerPeriod.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    prvtRsvpProductMinTimerPeriod.setStatus("current")
if mibBuilder.loadTexts:
    prvtRsvpProductMinTimerPeriod.setUnits("milliseconds")


class _PrvtRsvpProductAPIIfIndex_Type(InterfaceIndexOrZero):
    """Custom type prvtRsvpProductAPIIfIndex based on InterfaceIndexOrZero"""
    defaultValue = 2147483647


_PrvtRsvpProductAPIIfIndex_Type.__name__ = "InterfaceIndexOrZero"
_PrvtRsvpProductAPIIfIndex_Object = MibTableColumn
prvtRsvpProductAPIIfIndex = _PrvtRsvpProductAPIIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 7, 1, 1, 1, 5),
    _PrvtRsvpProductAPIIfIndex_Type()
)
prvtRsvpProductAPIIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    prvtRsvpProductAPIIfIndex.setStatus("current")


class _PrvtRsvpProductAPIAddress_Type(OctetString):
    """Custom type prvtRsvpProductAPIAddress based on OctetString"""
    defaultHexValue = "E0000000"

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 16),
    )


_PrvtRsvpProductAPIAddress_Type.__name__ = "OctetString"
_PrvtRsvpProductAPIAddress_Object = MibTableColumn
prvtRsvpProductAPIAddress = _PrvtRsvpProductAPIAddress_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 7, 1, 1, 1, 6),
    _PrvtRsvpProductAPIAddress_Type()
)
prvtRsvpProductAPIAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    prvtRsvpProductAPIAddress.setStatus("current")


class _PrvtRsvpProductAPIRefreshInterval_Type(Integer32):
    """Custom type prvtRsvpProductAPIRefreshInterval based on Integer32"""
    defaultValue = 30000


_PrvtRsvpProductAPIRefreshInterval_Type.__name__ = "Integer32"
_PrvtRsvpProductAPIRefreshInterval_Object = MibTableColumn
prvtRsvpProductAPIRefreshInterval = _PrvtRsvpProductAPIRefreshInterval_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 7, 1, 1, 1, 7),
    _PrvtRsvpProductAPIRefreshInterval_Type()
)
prvtRsvpProductAPIRefreshInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    prvtRsvpProductAPIRefreshInterval.setStatus("current")
if mibBuilder.loadTexts:
    prvtRsvpProductAPIRefreshInterval.setUnits("milliseconds")


class _PrvtRsvpProductLocalRepairDelay_Type(Integer32):
    """Custom type prvtRsvpProductLocalRepairDelay based on Integer32"""
    defaultValue = 1000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(1000, 2147483647),
    )


_PrvtRsvpProductLocalRepairDelay_Type.__name__ = "Integer32"
_PrvtRsvpProductLocalRepairDelay_Object = MibTableColumn
prvtRsvpProductLocalRepairDelay = _PrvtRsvpProductLocalRepairDelay_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 7, 1, 1, 1, 8),
    _PrvtRsvpProductLocalRepairDelay_Type()
)
prvtRsvpProductLocalRepairDelay.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    prvtRsvpProductLocalRepairDelay.setStatus("current")
if mibBuilder.loadTexts:
    prvtRsvpProductLocalRepairDelay.setUnits("milliseconds")


class _PrvtRsvpProductRefreshInterval_Type(Integer32):
    """Custom type prvtRsvpProductRefreshInterval based on Integer32"""
    defaultValue = 30000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1000, 2147483647),
    )


_PrvtRsvpProductRefreshInterval_Type.__name__ = "Integer32"
_PrvtRsvpProductRefreshInterval_Object = MibTableColumn
prvtRsvpProductRefreshInterval = _PrvtRsvpProductRefreshInterval_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 7, 1, 1, 1, 9),
    _PrvtRsvpProductRefreshInterval_Type()
)
prvtRsvpProductRefreshInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    prvtRsvpProductRefreshInterval.setStatus("current")
if mibBuilder.loadTexts:
    prvtRsvpProductRefreshInterval.setUnits("milliseconds")


class _PrvtRsvpProductRefreshMultiple_Type(Integer32):
    """Custom type prvtRsvpProductRefreshMultiple based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 214783647),
    )


_PrvtRsvpProductRefreshMultiple_Type.__name__ = "Integer32"
_PrvtRsvpProductRefreshMultiple_Object = MibTableColumn
prvtRsvpProductRefreshMultiple = _PrvtRsvpProductRefreshMultiple_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 7, 1, 1, 1, 10),
    _PrvtRsvpProductRefreshMultiple_Type()
)
prvtRsvpProductRefreshMultiple.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    prvtRsvpProductRefreshMultiple.setStatus("current")


class _PrvtRsvpProductRfrshSlewDenom_Type(Integer32):
    """Custom type prvtRsvpProductRfrshSlewDenom based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 214783647),
    )


_PrvtRsvpProductRfrshSlewDenom_Type.__name__ = "Integer32"
_PrvtRsvpProductRfrshSlewDenom_Object = MibTableColumn
prvtRsvpProductRfrshSlewDenom = _PrvtRsvpProductRfrshSlewDenom_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 7, 1, 1, 1, 11),
    _PrvtRsvpProductRfrshSlewDenom_Type()
)
prvtRsvpProductRfrshSlewDenom.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    prvtRsvpProductRfrshSlewDenom.setStatus("current")


class _PrvtRsvpProductRfrshSlewNumerator_Type(Integer32):
    """Custom type prvtRsvpProductRfrshSlewNumerator based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 214783647),
    )


_PrvtRsvpProductRfrshSlewNumerator_Type.__name__ = "Integer32"
_PrvtRsvpProductRfrshSlewNumerator_Object = MibTableColumn
prvtRsvpProductRfrshSlewNumerator = _PrvtRsvpProductRfrshSlewNumerator_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 7, 1, 1, 1, 12),
    _PrvtRsvpProductRfrshSlewNumerator_Type()
)
prvtRsvpProductRfrshSlewNumerator.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    prvtRsvpProductRfrshSlewNumerator.setStatus("current")


class _PrvtRsvpProductBlockadeMultiple_Type(Integer32):
    """Custom type prvtRsvpProductBlockadeMultiple based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 214783647),
    )


_PrvtRsvpProductBlockadeMultiple_Type.__name__ = "Integer32"
_PrvtRsvpProductBlockadeMultiple_Object = MibTableColumn
prvtRsvpProductBlockadeMultiple = _PrvtRsvpProductBlockadeMultiple_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 7, 1, 1, 1, 13),
    _PrvtRsvpProductBlockadeMultiple_Type()
)
prvtRsvpProductBlockadeMultiple.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    prvtRsvpProductBlockadeMultiple.setStatus("current")


class _PrvtRsvpProductSocketBufPoolSize_Type(Integer32):
    """Custom type prvtRsvpProductSocketBufPoolSize based on Integer32"""
    defaultValue = 8


_PrvtRsvpProductSocketBufPoolSize_Type.__name__ = "Integer32"
_PrvtRsvpProductSocketBufPoolSize_Object = MibTableColumn
prvtRsvpProductSocketBufPoolSize = _PrvtRsvpProductSocketBufPoolSize_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 7, 1, 1, 1, 14),
    _PrvtRsvpProductSocketBufPoolSize_Type()
)
prvtRsvpProductSocketBufPoolSize.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    prvtRsvpProductSocketBufPoolSize.setStatus("current")


class _PrvtRsvpProductSwitchBufPoolSize_Type(Integer32):
    """Custom type prvtRsvpProductSwitchBufPoolSize based on Integer32"""
    defaultValue = 8


_PrvtRsvpProductSwitchBufPoolSize_Type.__name__ = "Integer32"
_PrvtRsvpProductSwitchBufPoolSize_Object = MibTableColumn
prvtRsvpProductSwitchBufPoolSize = _PrvtRsvpProductSwitchBufPoolSize_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 7, 1, 1, 1, 15),
    _PrvtRsvpProductSwitchBufPoolSize_Type()
)
prvtRsvpProductSwitchBufPoolSize.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    prvtRsvpProductSwitchBufPoolSize.setStatus("current")


class _PrvtRsvpProductTeMibBufPoolSize_Type(Integer32):
    """Custom type prvtRsvpProductTeMibBufPoolSize based on Integer32"""
    defaultValue = 8


_PrvtRsvpProductTeMibBufPoolSize_Type.__name__ = "Integer32"
_PrvtRsvpProductTeMibBufPoolSize_Object = MibTableColumn
prvtRsvpProductTeMibBufPoolSize = _PrvtRsvpProductTeMibBufPoolSize_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 7, 1, 1, 1, 16),
    _PrvtRsvpProductTeMibBufPoolSize_Type()
)
prvtRsvpProductTeMibBufPoolSize.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    prvtRsvpProductTeMibBufPoolSize.setStatus("current")


class _PrvtRsvpProductRoutingBufPoolSize_Type(Integer32):
    """Custom type prvtRsvpProductRoutingBufPoolSize based on Integer32"""
    defaultValue = 8


_PrvtRsvpProductRoutingBufPoolSize_Type.__name__ = "Integer32"
_PrvtRsvpProductRoutingBufPoolSize_Object = MibTableColumn
prvtRsvpProductRoutingBufPoolSize = _PrvtRsvpProductRoutingBufPoolSize_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 7, 1, 1, 1, 17),
    _PrvtRsvpProductRoutingBufPoolSize_Type()
)
prvtRsvpProductRoutingBufPoolSize.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    prvtRsvpProductRoutingBufPoolSize.setStatus("current")


class _PrvtRsvpProductLSPSetupPriority_Type(Integer32):
    """Custom type prvtRsvpProductLSPSetupPriority based on Integer32"""
    defaultValue = 4

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_PrvtRsvpProductLSPSetupPriority_Type.__name__ = "Integer32"
_PrvtRsvpProductLSPSetupPriority_Object = MibTableColumn
prvtRsvpProductLSPSetupPriority = _PrvtRsvpProductLSPSetupPriority_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 7, 1, 1, 1, 18),
    _PrvtRsvpProductLSPSetupPriority_Type()
)
prvtRsvpProductLSPSetupPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    prvtRsvpProductLSPSetupPriority.setStatus("current")


class _PrvtRsvpProductLSPHoldingPriority_Type(Integer32):
    """Custom type prvtRsvpProductLSPHoldingPriority based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_PrvtRsvpProductLSPHoldingPriority_Type.__name__ = "Integer32"
_PrvtRsvpProductLSPHoldingPriority_Object = MibTableColumn
prvtRsvpProductLSPHoldingPriority = _PrvtRsvpProductLSPHoldingPriority_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 7, 1, 1, 1, 19),
    _PrvtRsvpProductLSPHoldingPriority_Type()
)
prvtRsvpProductLSPHoldingPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    prvtRsvpProductLSPHoldingPriority.setStatus("current")


class _PrvtRsvpProductAdminStatus_Type(PrvtRsvpAdminStatus):
    """Custom type prvtRsvpProductAdminStatus based on PrvtRsvpAdminStatus"""
    defaultValue = 1


_PrvtRsvpProductAdminStatus_Type.__name__ = "PrvtRsvpAdminStatus"
_PrvtRsvpProductAdminStatus_Object = MibTableColumn
prvtRsvpProductAdminStatus = _PrvtRsvpProductAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 7, 1, 1, 1, 20),
    _PrvtRsvpProductAdminStatus_Type()
)
prvtRsvpProductAdminStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    prvtRsvpProductAdminStatus.setStatus("current")
_PrvtRsvpProductOperStatus_Type = PrvtRsvpOperStatus
_PrvtRsvpProductOperStatus_Object = MibTableColumn
prvtRsvpProductOperStatus = _PrvtRsvpProductOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 7, 1, 1, 1, 21),
    _PrvtRsvpProductOperStatus_Type()
)
prvtRsvpProductOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtRsvpProductOperStatus.setStatus("current")


class _PrvtRsvpProductRowStatus_Type(RowStatus):
    """Custom type prvtRsvpProductRowStatus based on RowStatus"""
    defaultValue = 1


_PrvtRsvpProductRowStatus_Type.__name__ = "RowStatus"
_PrvtRsvpProductRowStatus_Object = MibTableColumn
prvtRsvpProductRowStatus = _PrvtRsvpProductRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 7, 1, 1, 1, 22),
    _PrvtRsvpProductRowStatus_Type()
)
prvtRsvpProductRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    prvtRsvpProductRowStatus.setStatus("current")


class _PrvtRsvpProductLsrIndex_Type(Unsigned32):
    """Custom type prvtRsvpProductLsrIndex based on Unsigned32"""
    defaultValue = 0


_PrvtRsvpProductLsrIndex_Type.__name__ = "Unsigned32"
_PrvtRsvpProductLsrIndex_Object = MibTableColumn
prvtRsvpProductLsrIndex = _PrvtRsvpProductLsrIndex_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 7, 1, 1, 1, 23),
    _PrvtRsvpProductLsrIndex_Type()
)
prvtRsvpProductLsrIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    prvtRsvpProductLsrIndex.setStatus("current")


class _PrvtRsvpProductTeMibIndex_Type(Unsigned32):
    """Custom type prvtRsvpProductTeMibIndex based on Unsigned32"""
    defaultValue = 0


_PrvtRsvpProductTeMibIndex_Type.__name__ = "Unsigned32"
_PrvtRsvpProductTeMibIndex_Object = MibTableColumn
prvtRsvpProductTeMibIndex = _PrvtRsvpProductTeMibIndex_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 7, 1, 1, 1, 24),
    _PrvtRsvpProductTeMibIndex_Type()
)
prvtRsvpProductTeMibIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    prvtRsvpProductTeMibIndex.setStatus("current")


class _PrvtRsvpProductMultiStackSupport_Type(Integer32):
    """Custom type prvtRsvpProductMultiStackSupport based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_PrvtRsvpProductMultiStackSupport_Type.__name__ = "Integer32"
_PrvtRsvpProductMultiStackSupport_Object = MibTableColumn
prvtRsvpProductMultiStackSupport = _PrvtRsvpProductMultiStackSupport_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 7, 1, 1, 1, 25),
    _PrvtRsvpProductMultiStackSupport_Type()
)
prvtRsvpProductMultiStackSupport.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    prvtRsvpProductMultiStackSupport.setStatus("current")


class _PrvtRsvpProductUseHopByHop_Type(TruthValue):
    """Custom type prvtRsvpProductUseHopByHop based on TruthValue"""
    defaultValue = 2


_PrvtRsvpProductUseHopByHop_Type.__name__ = "TruthValue"
_PrvtRsvpProductUseHopByHop_Object = MibTableColumn
prvtRsvpProductUseHopByHop = _PrvtRsvpProductUseHopByHop_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 7, 1, 1, 1, 26),
    _PrvtRsvpProductUseHopByHop_Type()
)
prvtRsvpProductUseHopByHop.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    prvtRsvpProductUseHopByHop.setStatus("current")


class _PrvtRsvpProductUseNotify_Type(TruthValue):
    """Custom type prvtRsvpProductUseNotify based on TruthValue"""
    defaultValue = 2


_PrvtRsvpProductUseNotify_Type.__name__ = "TruthValue"
_PrvtRsvpProductUseNotify_Object = MibTableColumn
prvtRsvpProductUseNotify = _PrvtRsvpProductUseNotify_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 7, 1, 1, 1, 27),
    _PrvtRsvpProductUseNotify_Type()
)
prvtRsvpProductUseNotify.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    prvtRsvpProductUseNotify.setStatus("current")


class _PrvtRsvpProductNotifyRRDecay_Type(Integer32):
    """Custom type prvtRsvpProductNotifyRRDecay based on Integer32"""
    defaultValue = 100

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_PrvtRsvpProductNotifyRRDecay_Type.__name__ = "Integer32"
_PrvtRsvpProductNotifyRRDecay_Object = MibTableColumn
prvtRsvpProductNotifyRRDecay = _PrvtRsvpProductNotifyRRDecay_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 7, 1, 1, 1, 28),
    _PrvtRsvpProductNotifyRRDecay_Type()
)
prvtRsvpProductNotifyRRDecay.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    prvtRsvpProductNotifyRRDecay.setStatus("current")


class _PrvtRsvpProductNotifyRRInterval_Type(Integer32):
    """Custom type prvtRsvpProductNotifyRRInterval based on Integer32"""
    defaultValue = 2000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1000, 2147483647),
    )


_PrvtRsvpProductNotifyRRInterval_Type.__name__ = "Integer32"
_PrvtRsvpProductNotifyRRInterval_Object = MibTableColumn
prvtRsvpProductNotifyRRInterval = _PrvtRsvpProductNotifyRRInterval_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 7, 1, 1, 1, 29),
    _PrvtRsvpProductNotifyRRInterval_Type()
)
prvtRsvpProductNotifyRRInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    prvtRsvpProductNotifyRRInterval.setStatus("current")


class _PrvtRsvpProductNotifyRRLimit_Type(Integer32):
    """Custom type prvtRsvpProductNotifyRRLimit based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_PrvtRsvpProductNotifyRRLimit_Type.__name__ = "Integer32"
_PrvtRsvpProductNotifyRRLimit_Object = MibTableColumn
prvtRsvpProductNotifyRRLimit = _PrvtRsvpProductNotifyRRLimit_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 7, 1, 1, 1, 30),
    _PrvtRsvpProductNotifyRRLimit_Type()
)
prvtRsvpProductNotifyRRLimit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    prvtRsvpProductNotifyRRLimit.setStatus("current")


class _PrvtRsvpProductAllowIPEncap_Type(TruthValue):
    """Custom type prvtRsvpProductAllowIPEncap based on TruthValue"""
    defaultValue = 2


_PrvtRsvpProductAllowIPEncap_Type.__name__ = "TruthValue"
_PrvtRsvpProductAllowIPEncap_Object = MibTableColumn
prvtRsvpProductAllowIPEncap = _PrvtRsvpProductAllowIPEncap_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 7, 1, 1, 1, 31),
    _PrvtRsvpProductAllowIPEncap_Type()
)
prvtRsvpProductAllowIPEncap.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    prvtRsvpProductAllowIPEncap.setStatus("current")


class _PrvtRsvpProductProtocolExtensions_Type(Bits):
    """Custom type prvtRsvpProductProtocolExtensions based on Bits"""
    defaultBinValue = "0"

    namedValues = NamedValues(
        *(("bypassFastReroute", 0),
          ("detourFastReroute", 1),
          ("noResAffOnInIf", 2))
    )

_PrvtRsvpProductProtocolExtensions_Type.__name__ = "Bits"
_PrvtRsvpProductProtocolExtensions_Object = MibTableColumn
prvtRsvpProductProtocolExtensions = _PrvtRsvpProductProtocolExtensions_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 7, 1, 1, 1, 32),
    _PrvtRsvpProductProtocolExtensions_Type()
)
prvtRsvpProductProtocolExtensions.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    prvtRsvpProductProtocolExtensions.setStatus("current")


class _PrvtRsvpProductPSRFlags_Type(Bits):
    """Custom type prvtRsvpProductPSRFlags based on Bits"""
    defaultBinValue = "0"

    namedValues = NamedValues(
        *(("pathErrPSRSet", 0),
          ("pathErrPSRNotSet", 1),
          ("ldbCommonRcvd", 2),
          ("ldbPreempted", 3),
          ("routingError", 4),
          ("invalidPathMsg", 5),
          ("sessionExpired", 6),
          ("unableToRepairRoute", 7),
          ("unableToRepairIf", 8),
          ("reachedRetryLimit", 9),
          ("unableToRefresh", 10),
          ("resvErrTurnaround", 11),
          ("incomingIfDown", 12),
          ("outgoingIfDown", 13))
    )

_PrvtRsvpProductPSRFlags_Type.__name__ = "Bits"
_PrvtRsvpProductPSRFlags_Object = MibTableColumn
prvtRsvpProductPSRFlags = _PrvtRsvpProductPSRFlags_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 7, 1, 1, 1, 33),
    _PrvtRsvpProductPSRFlags_Type()
)
prvtRsvpProductPSRFlags.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    prvtRsvpProductPSRFlags.setStatus("current")


class _PrvtRsvpProductInitPathRRDecay_Type(Integer32):
    """Custom type prvtRsvpProductInitPathRRDecay based on Integer32"""
    defaultValue = 100

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_PrvtRsvpProductInitPathRRDecay_Type.__name__ = "Integer32"
_PrvtRsvpProductInitPathRRDecay_Object = MibTableColumn
prvtRsvpProductInitPathRRDecay = _PrvtRsvpProductInitPathRRDecay_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 7, 1, 1, 1, 34),
    _PrvtRsvpProductInitPathRRDecay_Type()
)
prvtRsvpProductInitPathRRDecay.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    prvtRsvpProductInitPathRRDecay.setStatus("current")


class _PrvtRsvpProductInitPathRRInterval_Type(Integer32):
    """Custom type prvtRsvpProductInitPathRRInterval based on Integer32"""
    defaultValue = 2000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1000, 2147483647),
    )


_PrvtRsvpProductInitPathRRInterval_Type.__name__ = "Integer32"
_PrvtRsvpProductInitPathRRInterval_Object = MibTableColumn
prvtRsvpProductInitPathRRInterval = _PrvtRsvpProductInitPathRRInterval_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 7, 1, 1, 1, 35),
    _PrvtRsvpProductInitPathRRInterval_Type()
)
prvtRsvpProductInitPathRRInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    prvtRsvpProductInitPathRRInterval.setStatus("current")


class _PrvtRsvpProductInitPathRRLimit_Type(Integer32):
    """Custom type prvtRsvpProductInitPathRRLimit based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_PrvtRsvpProductInitPathRRLimit_Type.__name__ = "Integer32"
_PrvtRsvpProductInitPathRRLimit_Object = MibTableColumn
prvtRsvpProductInitPathRRLimit = _PrvtRsvpProductInitPathRRLimit_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 7, 1, 1, 1, 36),
    _PrvtRsvpProductInitPathRRLimit_Type()
)
prvtRsvpProductInitPathRRLimit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    prvtRsvpProductInitPathRRLimit.setStatus("current")


class _PrvtRsvpProductEnableUni_Type(TruthValue):
    """Custom type prvtRsvpProductEnableUni based on TruthValue"""
    defaultValue = 2


_PrvtRsvpProductEnableUni_Type.__name__ = "TruthValue"
_PrvtRsvpProductEnableUni_Object = MibTableColumn
prvtRsvpProductEnableUni = _PrvtRsvpProductEnableUni_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 7, 1, 1, 1, 37),
    _PrvtRsvpProductEnableUni_Type()
)
prvtRsvpProductEnableUni.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    prvtRsvpProductEnableUni.setStatus("current")


class _PrvtRsvpProductRestartCapable_Type(TruthValue):
    """Custom type prvtRsvpProductRestartCapable based on TruthValue"""
    defaultValue = 2


_PrvtRsvpProductRestartCapable_Type.__name__ = "TruthValue"
_PrvtRsvpProductRestartCapable_Object = MibTableColumn
prvtRsvpProductRestartCapable = _PrvtRsvpProductRestartCapable_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 7, 1, 1, 1, 38),
    _PrvtRsvpProductRestartCapable_Type()
)
prvtRsvpProductRestartCapable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    prvtRsvpProductRestartCapable.setStatus("current")


class _PrvtRsvpProductRestartTime_Type(Unsigned32):
    """Custom type prvtRsvpProductRestartTime based on Unsigned32"""
    defaultValue = 10000


_PrvtRsvpProductRestartTime_Type.__name__ = "Unsigned32"
_PrvtRsvpProductRestartTime_Object = MibTableColumn
prvtRsvpProductRestartTime = _PrvtRsvpProductRestartTime_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 7, 1, 1, 1, 39),
    _PrvtRsvpProductRestartTime_Type()
)
prvtRsvpProductRestartTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    prvtRsvpProductRestartTime.setStatus("current")


class _PrvtRsvpProductRecoveryTime_Type(Unsigned32):
    """Custom type prvtRsvpProductRecoveryTime based on Unsigned32"""
    defaultValue = 10000


_PrvtRsvpProductRecoveryTime_Type.__name__ = "Unsigned32"
_PrvtRsvpProductRecoveryTime_Object = MibTableColumn
prvtRsvpProductRecoveryTime = _PrvtRsvpProductRecoveryTime_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 7, 1, 1, 1, 40),
    _PrvtRsvpProductRecoveryTime_Type()
)
prvtRsvpProductRecoveryTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    prvtRsvpProductRecoveryTime.setStatus("current")


class _PrvtRsvpProductMinPeerRestart_Type(Integer32):
    """Custom type prvtRsvpProductMinPeerRestart based on Integer32"""
    defaultValue = 0


_PrvtRsvpProductMinPeerRestart_Type.__name__ = "Integer32"
_PrvtRsvpProductMinPeerRestart_Object = MibTableColumn
prvtRsvpProductMinPeerRestart = _PrvtRsvpProductMinPeerRestart_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 7, 1, 1, 1, 41),
    _PrvtRsvpProductMinPeerRestart_Type()
)
prvtRsvpProductMinPeerRestart.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    prvtRsvpProductMinPeerRestart.setStatus("current")


class _PrvtRsvpProductGracefulDelTimeout_Type(Integer32):
    """Custom type prvtRsvpProductGracefulDelTimeout based on Integer32"""
    defaultValue = 30000


_PrvtRsvpProductGracefulDelTimeout_Type.__name__ = "Integer32"
_PrvtRsvpProductGracefulDelTimeout_Object = MibTableColumn
prvtRsvpProductGracefulDelTimeout = _PrvtRsvpProductGracefulDelTimeout_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 7, 1, 1, 1, 42),
    _PrvtRsvpProductGracefulDelTimeout_Type()
)
prvtRsvpProductGracefulDelTimeout.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    prvtRsvpProductGracefulDelTimeout.setStatus("current")


class _PrvtRsvpProductEgressDelBehavior_Type(Integer32):
    """Custom type prvtRsvpProductEgressDelBehavior based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("delWithPathErr", 1),
          ("delWithResvD", 2))
    )


_PrvtRsvpProductEgressDelBehavior_Type.__name__ = "Integer32"
_PrvtRsvpProductEgressDelBehavior_Object = MibTableColumn
prvtRsvpProductEgressDelBehavior = _PrvtRsvpProductEgressDelBehavior_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 7, 1, 1, 1, 43),
    _PrvtRsvpProductEgressDelBehavior_Type()
)
prvtRsvpProductEgressDelBehavior.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    prvtRsvpProductEgressDelBehavior.setStatus("current")


class _PrvtRsvpProductEnabUniConnSplicing_Type(TruthValue):
    """Custom type prvtRsvpProductEnabUniConnSplicing based on TruthValue"""
    defaultValue = 2


_PrvtRsvpProductEnabUniConnSplicing_Type.__name__ = "TruthValue"
_PrvtRsvpProductEnabUniConnSplicing_Object = MibTableColumn
prvtRsvpProductEnabUniConnSplicing = _PrvtRsvpProductEnabUniConnSplicing_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 7, 1, 1, 1, 44),
    _PrvtRsvpProductEnabUniConnSplicing_Type()
)
prvtRsvpProductEnabUniConnSplicing.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    prvtRsvpProductEnabUniConnSplicing.setStatus("current")


class _PrvtRsvpProductFastRerouteCaps_Type(Bits):
    """Custom type prvtRsvpProductFastRerouteCaps based on Bits"""
    defaultBinValue = "0"

    namedValues = NamedValues(
        *(("fastReroutePLR", 0),
          ("fastRerouteMP", 1),
          ("fastRerouteDetourRestart", 2))
    )

_PrvtRsvpProductFastRerouteCaps_Type.__name__ = "Bits"
_PrvtRsvpProductFastRerouteCaps_Object = MibTableColumn
prvtRsvpProductFastRerouteCaps = _PrvtRsvpProductFastRerouteCaps_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 7, 1, 1, 1, 45),
    _PrvtRsvpProductFastRerouteCaps_Type()
)
prvtRsvpProductFastRerouteCaps.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    prvtRsvpProductFastRerouteCaps.setStatus("current")


class _PrvtRsvpProductFastRroutBkpRtryInt_Type(Integer32):
    """Custom type prvtRsvpProductFastRroutBkpRtryInt based on Integer32"""
    defaultValue = 30000


_PrvtRsvpProductFastRroutBkpRtryInt_Type.__name__ = "Integer32"
_PrvtRsvpProductFastRroutBkpRtryInt_Object = MibTableColumn
prvtRsvpProductFastRroutBkpRtryInt = _PrvtRsvpProductFastRroutBkpRtryInt_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 7, 1, 1, 1, 46),
    _PrvtRsvpProductFastRroutBkpRtryInt_Type()
)
prvtRsvpProductFastRroutBkpRtryInt.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    prvtRsvpProductFastRroutBkpRtryInt.setStatus("current")


class _PrvtRsvpProductErrorActionFlags_Type(Bits):
    """Custom type prvtRsvpProductErrorActionFlags based on Bits"""
    defaultBinValue = "0"

    namedValues = NamedValues(
        ("eafTearStateOnLSIErr", 0)
    )

_PrvtRsvpProductErrorActionFlags_Type.__name__ = "Bits"
_PrvtRsvpProductErrorActionFlags_Object = MibTableColumn
prvtRsvpProductErrorActionFlags = _PrvtRsvpProductErrorActionFlags_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 7, 1, 1, 1, 47),
    _PrvtRsvpProductErrorActionFlags_Type()
)
prvtRsvpProductErrorActionFlags.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    prvtRsvpProductErrorActionFlags.setStatus("current")


class _PrvtRsvpProductEnableNni_Type(Integer32):
    """Custom type prvtRsvpProductEnableNni based on Integer32"""
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
        *(("disabled", 1),
          ("enabled", 2),
          ("disabling", 3))
    )


_PrvtRsvpProductEnableNni_Type.__name__ = "Integer32"
_PrvtRsvpProductEnableNni_Object = MibTableColumn
prvtRsvpProductEnableNni = _PrvtRsvpProductEnableNni_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 7, 1, 1, 1, 48),
    _PrvtRsvpProductEnableNni_Type()
)
prvtRsvpProductEnableNni.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    prvtRsvpProductEnableNni.setStatus("current")


class _PrvtRsvpProductBehaviorFlags_Type(Bits):
    """Custom type prvtRsvpProductBehaviorFlags based on Bits"""
    defaultBinValue = "0"

    namedValues = NamedValues(
        ("enableTTLMatch", 0)
    )

_PrvtRsvpProductBehaviorFlags_Type.__name__ = "Bits"
_PrvtRsvpProductBehaviorFlags_Object = MibTableColumn
prvtRsvpProductBehaviorFlags = _PrvtRsvpProductBehaviorFlags_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 7, 1, 1, 1, 49),
    _PrvtRsvpProductBehaviorFlags_Type()
)
prvtRsvpProductBehaviorFlags.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    prvtRsvpProductBehaviorFlags.setStatus("current")


class _PrvtRsvpProductLabelSetStyle_Type(Integer32):
    """Custom type prvtRsvpProductLabelSetStyle based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("excludeLabelHeader", 1),
          ("includeLabelHeader", 2))
    )


_PrvtRsvpProductLabelSetStyle_Type.__name__ = "Integer32"
_PrvtRsvpProductLabelSetStyle_Object = MibTableColumn
prvtRsvpProductLabelSetStyle = _PrvtRsvpProductLabelSetStyle_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 7, 1, 1, 1, 50),
    _PrvtRsvpProductLabelSetStyle_Type()
)
prvtRsvpProductLabelSetStyle.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    prvtRsvpProductLabelSetStyle.setStatus("current")


class _PrvtRsvpProductLabelSetOperStatus_Type(Integer32):
    """Custom type prvtRsvpProductLabelSetOperStatus based on Integer32"""
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
        *(("excludeLabelHeader", 1),
          ("includeLabelHeader", 2),
          ("goingToExclude", 3),
          ("goingToInclude", 4))
    )


_PrvtRsvpProductLabelSetOperStatus_Type.__name__ = "Integer32"
_PrvtRsvpProductLabelSetOperStatus_Object = MibTableColumn
prvtRsvpProductLabelSetOperStatus = _PrvtRsvpProductLabelSetOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 7, 1, 1, 1, 51),
    _PrvtRsvpProductLabelSetOperStatus_Type()
)
prvtRsvpProductLabelSetOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtRsvpProductLabelSetOperStatus.setStatus("current")


class _PrvtRsvpProductLabelSetTrapEnable_Type(TruthValue):
    """Custom type prvtRsvpProductLabelSetTrapEnable based on TruthValue"""
    defaultValue = 2


_PrvtRsvpProductLabelSetTrapEnable_Type.__name__ = "TruthValue"
_PrvtRsvpProductLabelSetTrapEnable_Object = MibTableColumn
prvtRsvpProductLabelSetTrapEnable = _PrvtRsvpProductLabelSetTrapEnable_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 7, 1, 1, 1, 52),
    _PrvtRsvpProductLabelSetTrapEnable_Type()
)
prvtRsvpProductLabelSetTrapEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    prvtRsvpProductLabelSetTrapEnable.setStatus("current")


class _PrvtRsvpProductLabelSetChngAct_Type(Integer32):
    """Custom type prvtRsvpProductLabelSetChngAct based on Integer32"""
    defaultValue = 1


_PrvtRsvpProductLabelSetChngAct_Type.__name__ = "Integer32"
_PrvtRsvpProductLabelSetChngAct_Object = MibTableColumn
prvtRsvpProductLabelSetChngAct = _PrvtRsvpProductLabelSetChngAct_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 7, 1, 1, 1, 53),
    _PrvtRsvpProductLabelSetChngAct_Type()
)
prvtRsvpProductLabelSetChngAct.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    prvtRsvpProductLabelSetChngAct.setStatus("current")


class _PrvtRsvpProductExtPrtAdminStatus_Type(PrvtRsvpAdminStatus):
    """Custom type prvtRsvpProductExtPrtAdminStatus based on PrvtRsvpAdminStatus"""
    defaultValue = 2


_PrvtRsvpProductExtPrtAdminStatus_Type.__name__ = "PrvtRsvpAdminStatus"
_PrvtRsvpProductExtPrtAdminStatus_Object = MibTableColumn
prvtRsvpProductExtPrtAdminStatus = _PrvtRsvpProductExtPrtAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 7, 1, 1, 1, 54),
    _PrvtRsvpProductExtPrtAdminStatus_Type()
)
prvtRsvpProductExtPrtAdminStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    prvtRsvpProductExtPrtAdminStatus.setStatus("current")


class _PrvtRsvpProductUniIncSonetProfile_Type(Unsigned32):
    """Custom type prvtRsvpProductUniIncSonetProfile based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_PrvtRsvpProductUniIncSonetProfile_Type.__name__ = "Unsigned32"
_PrvtRsvpProductUniIncSonetProfile_Object = MibTableColumn
prvtRsvpProductUniIncSonetProfile = _PrvtRsvpProductUniIncSonetProfile_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 7, 1, 1, 1, 55),
    _PrvtRsvpProductUniIncSonetProfile_Type()
)
prvtRsvpProductUniIncSonetProfile.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    prvtRsvpProductUniIncSonetProfile.setStatus("current")


class _PrvtRsvpProductFrrFacAdminStatus_Type(PrvtRsvpAdminStatus):
    """Custom type prvtRsvpProductFrrFacAdminStatus based on PrvtRsvpAdminStatus"""
    defaultValue = 2


_PrvtRsvpProductFrrFacAdminStatus_Type.__name__ = "PrvtRsvpAdminStatus"
_PrvtRsvpProductFrrFacAdminStatus_Object = MibTableColumn
prvtRsvpProductFrrFacAdminStatus = _PrvtRsvpProductFrrFacAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 7, 1, 1, 1, 56),
    _PrvtRsvpProductFrrFacAdminStatus_Type()
)
prvtRsvpProductFrrFacAdminStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    prvtRsvpProductFrrFacAdminStatus.setStatus("current")
_PrvtRsvpProductFrrFacOperStatus_Type = PrvtRsvpOperStatus
_PrvtRsvpProductFrrFacOperStatus_Object = MibTableColumn
prvtRsvpProductFrrFacOperStatus = _PrvtRsvpProductFrrFacOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 7, 1, 1, 1, 57),
    _PrvtRsvpProductFrrFacOperStatus_Type()
)
prvtRsvpProductFrrFacOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtRsvpProductFrrFacOperStatus.setStatus("current")


class _PrvtRsvpProductIpv6AdminStatus_Type(PrvtRsvpAdminStatus):
    """Custom type prvtRsvpProductIpv6AdminStatus based on PrvtRsvpAdminStatus"""
    defaultValue = 2


_PrvtRsvpProductIpv6AdminStatus_Type.__name__ = "PrvtRsvpAdminStatus"
_PrvtRsvpProductIpv6AdminStatus_Object = MibTableColumn
prvtRsvpProductIpv6AdminStatus = _PrvtRsvpProductIpv6AdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 7, 1, 1, 1, 58),
    _PrvtRsvpProductIpv6AdminStatus_Type()
)
prvtRsvpProductIpv6AdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prvtRsvpProductIpv6AdminStatus.setStatus("current")
_PrvtRsvpProductIpv6OperStatus_Type = PrvtRsvpOperStatus
_PrvtRsvpProductIpv6OperStatus_Object = MibTableColumn
prvtRsvpProductIpv6OperStatus = _PrvtRsvpProductIpv6OperStatus_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 7, 1, 1, 1, 59),
    _PrvtRsvpProductIpv6OperStatus_Type()
)
prvtRsvpProductIpv6OperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtRsvpProductIpv6OperStatus.setStatus("current")
_PrvtRsvpProductAPIIpv6Address_Type = InetAddressIPv6
_PrvtRsvpProductAPIIpv6Address_Object = MibTableColumn
prvtRsvpProductAPIIpv6Address = _PrvtRsvpProductAPIIpv6Address_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 7, 1, 1, 1, 60),
    _PrvtRsvpProductAPIIpv6Address_Type()
)
prvtRsvpProductAPIIpv6Address.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    prvtRsvpProductAPIIpv6Address.setStatus("current")
_PrvtRsvpDiagnosticTable_Object = MibTable
prvtRsvpDiagnosticTable = _PrvtRsvpDiagnosticTable_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 7, 1, 2)
)
if mibBuilder.loadTexts:
    prvtRsvpDiagnosticTable.setStatus("current")
_PrvtRsvpDiagnosticEntry_Object = MibTableRow
prvtRsvpDiagnosticEntry = _PrvtRsvpDiagnosticEntry_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 7, 1, 2, 1)
)
prvtRsvpDiagnosticEntry.setIndexNames(
    (0, "PRVT-RSVP-MIB", "prvtRsvpDiagProductIndex"),
    (0, "PRVT-RSVP-MIB", "prvtRsvpDiagRequestIndex"),
)
if mibBuilder.loadTexts:
    prvtRsvpDiagnosticEntry.setStatus("current")
_PrvtRsvpDiagProductIndex_Type = PrvtRsvpIndex
_PrvtRsvpDiagProductIndex_Object = MibTableColumn
prvtRsvpDiagProductIndex = _PrvtRsvpDiagProductIndex_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 7, 1, 2, 1, 1),
    _PrvtRsvpDiagProductIndex_Type()
)
prvtRsvpDiagProductIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    prvtRsvpDiagProductIndex.setStatus("current")
_PrvtRsvpDiagRequestIndex_Type = PrvtRsvpDiagReqIndex
_PrvtRsvpDiagRequestIndex_Object = MibTableColumn
prvtRsvpDiagRequestIndex = _PrvtRsvpDiagRequestIndex_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 7, 1, 2, 1, 2),
    _PrvtRsvpDiagRequestIndex_Type()
)
prvtRsvpDiagRequestIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    prvtRsvpDiagRequestIndex.setStatus("current")
_PrvtRsvpDiagReqsInProgress_Type = Unsigned32
_PrvtRsvpDiagReqsInProgress_Object = MibTableColumn
prvtRsvpDiagReqsInProgress = _PrvtRsvpDiagReqsInProgress_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 7, 1, 2, 1, 3),
    _PrvtRsvpDiagReqsInProgress_Type()
)
prvtRsvpDiagReqsInProgress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtRsvpDiagReqsInProgress.setStatus("current")
_PrvtRsvpDiagSessionEndPoint_Type = IpAddress
_PrvtRsvpDiagSessionEndPoint_Object = MibTableColumn
prvtRsvpDiagSessionEndPoint = _PrvtRsvpDiagSessionEndPoint_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 7, 1, 2, 1, 4),
    _PrvtRsvpDiagSessionEndPoint_Type()
)
prvtRsvpDiagSessionEndPoint.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtRsvpDiagSessionEndPoint.setStatus("current")
_PrvtRsvpDiagSessionTunnelId_Type = Unsigned32
_PrvtRsvpDiagSessionTunnelId_Object = MibTableColumn
prvtRsvpDiagSessionTunnelId = _PrvtRsvpDiagSessionTunnelId_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 7, 1, 2, 1, 5),
    _PrvtRsvpDiagSessionTunnelId_Type()
)
prvtRsvpDiagSessionTunnelId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtRsvpDiagSessionTunnelId.setStatus("current")
_PrvtRsvpDiagSessionExtTunnelId_Type = Unsigned32
_PrvtRsvpDiagSessionExtTunnelId_Object = MibTableColumn
prvtRsvpDiagSessionExtTunnelId = _PrvtRsvpDiagSessionExtTunnelId_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 7, 1, 2, 1, 6),
    _PrvtRsvpDiagSessionExtTunnelId_Type()
)
prvtRsvpDiagSessionExtTunnelId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtRsvpDiagSessionExtTunnelId.setStatus("current")
_PrvtRsvpDiagLastHop_Type = IpAddress
_PrvtRsvpDiagLastHop_Object = MibTableColumn
prvtRsvpDiagLastHop = _PrvtRsvpDiagLastHop_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 7, 1, 2, 1, 7),
    _PrvtRsvpDiagLastHop_Type()
)
prvtRsvpDiagLastHop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtRsvpDiagLastHop.setStatus("current")
_PrvtRsvpDiagSender_Type = IpAddress
_PrvtRsvpDiagSender_Object = MibTableColumn
prvtRsvpDiagSender = _PrvtRsvpDiagSender_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 7, 1, 2, 1, 8),
    _PrvtRsvpDiagSender_Type()
)
prvtRsvpDiagSender.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtRsvpDiagSender.setStatus("current")


class _PrvtRsvpDiagMaxHops_Type(Integer32):
    """Custom type prvtRsvpDiagMaxHops based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_PrvtRsvpDiagMaxHops_Type.__name__ = "Integer32"
_PrvtRsvpDiagMaxHops_Object = MibTableColumn
prvtRsvpDiagMaxHops = _PrvtRsvpDiagMaxHops_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 7, 1, 2, 1, 9),
    _PrvtRsvpDiagMaxHops_Type()
)
prvtRsvpDiagMaxHops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtRsvpDiagMaxHops.setStatus("current")
_PrvtRsvpDiagHopByHopReply_Type = TruthValue
_PrvtRsvpDiagHopByHopReply_Object = MibTableColumn
prvtRsvpDiagHopByHopReply = _PrvtRsvpDiagHopByHopReply_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 7, 1, 2, 1, 10),
    _PrvtRsvpDiagHopByHopReply_Type()
)
prvtRsvpDiagHopByHopReply.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtRsvpDiagHopByHopReply.setStatus("current")
_PrvtRsvpDiagNodeTable_Object = MibTable
prvtRsvpDiagNodeTable = _PrvtRsvpDiagNodeTable_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 7, 1, 3)
)
if mibBuilder.loadTexts:
    prvtRsvpDiagNodeTable.setStatus("current")
_PrvtRsvpDiagNodeEntry_Object = MibTableRow
prvtRsvpDiagNodeEntry = _PrvtRsvpDiagNodeEntry_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 7, 1, 3, 1)
)
prvtRsvpDiagNodeEntry.setIndexNames(
    (0, "PRVT-RSVP-MIB", "prvtRsvpDiagNodeProductIndex"),
    (0, "PRVT-RSVP-MIB", "prvtRsvpDiagNodeRequestIndex"),
    (0, "PRVT-RSVP-MIB", "prvtRsvpDiagNodeIndex"),
)
if mibBuilder.loadTexts:
    prvtRsvpDiagNodeEntry.setStatus("current")
_PrvtRsvpDiagNodeProductIndex_Type = PrvtRsvpIndex
_PrvtRsvpDiagNodeProductIndex_Object = MibTableColumn
prvtRsvpDiagNodeProductIndex = _PrvtRsvpDiagNodeProductIndex_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 7, 1, 3, 1, 1),
    _PrvtRsvpDiagNodeProductIndex_Type()
)
prvtRsvpDiagNodeProductIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    prvtRsvpDiagNodeProductIndex.setStatus("current")
_PrvtRsvpDiagNodeRequestIndex_Type = PrvtRsvpDiagReqIndex
_PrvtRsvpDiagNodeRequestIndex_Object = MibTableColumn
prvtRsvpDiagNodeRequestIndex = _PrvtRsvpDiagNodeRequestIndex_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 7, 1, 3, 1, 2),
    _PrvtRsvpDiagNodeRequestIndex_Type()
)
prvtRsvpDiagNodeRequestIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    prvtRsvpDiagNodeRequestIndex.setStatus("current")
_PrvtRsvpDiagNodeIndex_Type = PrvtRsvpDiagNodeIndexType
_PrvtRsvpDiagNodeIndex_Object = MibTableColumn
prvtRsvpDiagNodeIndex = _PrvtRsvpDiagNodeIndex_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 7, 1, 3, 1, 3),
    _PrvtRsvpDiagNodeIndex_Type()
)
prvtRsvpDiagNodeIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    prvtRsvpDiagNodeIndex.setStatus("current")
_PrvtRsvpDiagNodeType_Type = PrvtRsvpDiagNodeTypeVal
_PrvtRsvpDiagNodeType_Object = MibTableColumn
prvtRsvpDiagNodeType = _PrvtRsvpDiagNodeType_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 7, 1, 3, 1, 4),
    _PrvtRsvpDiagNodeType_Type()
)
prvtRsvpDiagNodeType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtRsvpDiagNodeType.setStatus("current")
_PrvtRsvpDiagNodeDreqArrivalTime_Type = Unsigned32
_PrvtRsvpDiagNodeDreqArrivalTime_Object = MibTableColumn
prvtRsvpDiagNodeDreqArrivalTime = _PrvtRsvpDiagNodeDreqArrivalTime_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 7, 1, 3, 1, 5),
    _PrvtRsvpDiagNodeDreqArrivalTime_Type()
)
prvtRsvpDiagNodeDreqArrivalTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtRsvpDiagNodeDreqArrivalTime.setStatus("current")
_PrvtRsvpDiagNodeIncomingIfAddr_Type = IpAddress
_PrvtRsvpDiagNodeIncomingIfAddr_Object = MibTableColumn
prvtRsvpDiagNodeIncomingIfAddr = _PrvtRsvpDiagNodeIncomingIfAddr_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 7, 1, 3, 1, 6),
    _PrvtRsvpDiagNodeIncomingIfAddr_Type()
)
prvtRsvpDiagNodeIncomingIfAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtRsvpDiagNodeIncomingIfAddr.setStatus("current")
_PrvtRsvpDiagNodeOutgoingIfAddr_Type = IpAddress
_PrvtRsvpDiagNodeOutgoingIfAddr_Object = MibTableColumn
prvtRsvpDiagNodeOutgoingIfAddr = _PrvtRsvpDiagNodeOutgoingIfAddr_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 7, 1, 3, 1, 7),
    _PrvtRsvpDiagNodeOutgoingIfAddr_Type()
)
prvtRsvpDiagNodeOutgoingIfAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtRsvpDiagNodeOutgoingIfAddr.setStatus("current")
_PrvtRsvpDiagNodePrevHopAddr_Type = IpAddress
_PrvtRsvpDiagNodePrevHopAddr_Object = MibTableColumn
prvtRsvpDiagNodePrevHopAddr = _PrvtRsvpDiagNodePrevHopAddr_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 7, 1, 3, 1, 8),
    _PrvtRsvpDiagNodePrevHopAddr_Type()
)
prvtRsvpDiagNodePrevHopAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtRsvpDiagNodePrevHopAddr.setStatus("current")


class _PrvtRsvpDiagNodeDTTL_Type(Integer32):
    """Custom type prvtRsvpDiagNodeDTTL based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_PrvtRsvpDiagNodeDTTL_Type.__name__ = "Integer32"
_PrvtRsvpDiagNodeDTTL_Object = MibTableColumn
prvtRsvpDiagNodeDTTL = _PrvtRsvpDiagNodeDTTL_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 7, 1, 3, 1, 9),
    _PrvtRsvpDiagNodeDTTL_Type()
)
prvtRsvpDiagNodeDTTL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtRsvpDiagNodeDTTL.setStatus("current")
_PrvtRsvpDiagNodeMFlag_Type = TruthValue
_PrvtRsvpDiagNodeMFlag_Object = MibTableColumn
prvtRsvpDiagNodeMFlag = _PrvtRsvpDiagNodeMFlag_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 7, 1, 3, 1, 10),
    _PrvtRsvpDiagNodeMFlag_Type()
)
prvtRsvpDiagNodeMFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtRsvpDiagNodeMFlag.setStatus("current")


class _PrvtRsvpDiagNodeRErr_Type(Integer32):
    """Custom type prvtRsvpDiagNodeRErr based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_PrvtRsvpDiagNodeRErr_Type.__name__ = "Integer32"
_PrvtRsvpDiagNodeRErr_Object = MibTableColumn
prvtRsvpDiagNodeRErr = _PrvtRsvpDiagNodeRErr_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 7, 1, 3, 1, 11),
    _PrvtRsvpDiagNodeRErr_Type()
)
prvtRsvpDiagNodeRErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtRsvpDiagNodeRErr.setStatus("current")


class _PrvtRsvpDiagNodeKValue_Type(Integer32):
    """Custom type prvtRsvpDiagNodeKValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_PrvtRsvpDiagNodeKValue_Type.__name__ = "Integer32"
_PrvtRsvpDiagNodeKValue_Object = MibTableColumn
prvtRsvpDiagNodeKValue = _PrvtRsvpDiagNodeKValue_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 7, 1, 3, 1, 12),
    _PrvtRsvpDiagNodeKValue_Type()
)
prvtRsvpDiagNodeKValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtRsvpDiagNodeKValue.setStatus("current")


class _PrvtRsvpDiagNodeTimerValue_Type(Integer32):
    """Custom type prvtRsvpDiagNodeTimerValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_PrvtRsvpDiagNodeTimerValue_Type.__name__ = "Integer32"
_PrvtRsvpDiagNodeTimerValue_Object = MibTableColumn
prvtRsvpDiagNodeTimerValue = _PrvtRsvpDiagNodeTimerValue_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 7, 1, 3, 1, 13),
    _PrvtRsvpDiagNodeTimerValue_Type()
)
prvtRsvpDiagNodeTimerValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtRsvpDiagNodeTimerValue.setStatus("current")
if mibBuilder.loadTexts:
    prvtRsvpDiagNodeTimerValue.setUnits("seconds")
_PrvtRsvpDiagRsvpHopAddr_Type = IpAddress
_PrvtRsvpDiagRsvpHopAddr_Object = MibTableColumn
prvtRsvpDiagRsvpHopAddr = _PrvtRsvpDiagRsvpHopAddr_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 7, 1, 3, 1, 14),
    _PrvtRsvpDiagRsvpHopAddr_Type()
)
prvtRsvpDiagRsvpHopAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtRsvpDiagRsvpHopAddr.setStatus("current")
_PrvtRsvpDiagRsvpHopLIH_Type = Unsigned32
_PrvtRsvpDiagRsvpHopLIH_Object = MibTableColumn
prvtRsvpDiagRsvpHopLIH = _PrvtRsvpDiagRsvpHopLIH_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 7, 1, 3, 1, 15),
    _PrvtRsvpDiagRsvpHopLIH_Type()
)
prvtRsvpDiagRsvpHopLIH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtRsvpDiagRsvpHopLIH.setStatus("current")
_PrvtRsvpDiagSenderTpltAddress_Type = IpAddress
_PrvtRsvpDiagSenderTpltAddress_Object = MibTableColumn
prvtRsvpDiagSenderTpltAddress = _PrvtRsvpDiagSenderTpltAddress_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 7, 1, 3, 1, 16),
    _PrvtRsvpDiagSenderTpltAddress_Type()
)
prvtRsvpDiagSenderTpltAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtRsvpDiagSenderTpltAddress.setStatus("current")


class _PrvtRsvpDiagSenderTpltLSPId_Type(Integer32):
    """Custom type prvtRsvpDiagSenderTpltLSPId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_PrvtRsvpDiagSenderTpltLSPId_Type.__name__ = "Integer32"
_PrvtRsvpDiagSenderTpltLSPId_Object = MibTableColumn
prvtRsvpDiagSenderTpltLSPId = _PrvtRsvpDiagSenderTpltLSPId_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 7, 1, 3, 1, 17),
    _PrvtRsvpDiagSenderTpltLSPId_Type()
)
prvtRsvpDiagSenderTpltLSPId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtRsvpDiagSenderTpltLSPId.setStatus("current")
_PrvtRsvpDiagFlowSpecCLBktRate_Type = Unsigned32
_PrvtRsvpDiagFlowSpecCLBktRate_Object = MibTableColumn
prvtRsvpDiagFlowSpecCLBktRate = _PrvtRsvpDiagFlowSpecCLBktRate_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 7, 1, 3, 1, 18),
    _PrvtRsvpDiagFlowSpecCLBktRate_Type()
)
prvtRsvpDiagFlowSpecCLBktRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtRsvpDiagFlowSpecCLBktRate.setStatus("current")
_PrvtRsvpDiagFlowSpecCLBktDep_Type = Unsigned32
_PrvtRsvpDiagFlowSpecCLBktDep_Object = MibTableColumn
prvtRsvpDiagFlowSpecCLBktDep = _PrvtRsvpDiagFlowSpecCLBktDep_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 7, 1, 3, 1, 19),
    _PrvtRsvpDiagFlowSpecCLBktDep_Type()
)
prvtRsvpDiagFlowSpecCLBktDep.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtRsvpDiagFlowSpecCLBktDep.setStatus("current")
_PrvtRsvpDiagFlowSpecCLPkDataRate_Type = Unsigned32
_PrvtRsvpDiagFlowSpecCLPkDataRate_Object = MibTableColumn
prvtRsvpDiagFlowSpecCLPkDataRate = _PrvtRsvpDiagFlowSpecCLPkDataRate_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 7, 1, 3, 1, 20),
    _PrvtRsvpDiagFlowSpecCLPkDataRate_Type()
)
prvtRsvpDiagFlowSpecCLPkDataRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtRsvpDiagFlowSpecCLPkDataRate.setStatus("current")
_PrvtRsvpDiagFlowSpecCLMinPolUnit_Type = Unsigned32
_PrvtRsvpDiagFlowSpecCLMinPolUnit_Object = MibTableColumn
prvtRsvpDiagFlowSpecCLMinPolUnit = _PrvtRsvpDiagFlowSpecCLMinPolUnit_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 7, 1, 3, 1, 21),
    _PrvtRsvpDiagFlowSpecCLMinPolUnit_Type()
)
prvtRsvpDiagFlowSpecCLMinPolUnit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtRsvpDiagFlowSpecCLMinPolUnit.setStatus("current")
_PrvtRsvpDiagFlowSpecCLMaxPktSize_Type = Unsigned32
_PrvtRsvpDiagFlowSpecCLMaxPktSize_Object = MibTableColumn
prvtRsvpDiagFlowSpecCLMaxPktSize = _PrvtRsvpDiagFlowSpecCLMaxPktSize_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 7, 1, 3, 1, 22),
    _PrvtRsvpDiagFlowSpecCLMaxPktSize_Type()
)
prvtRsvpDiagFlowSpecCLMaxPktSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtRsvpDiagFlowSpecCLMaxPktSize.setStatus("current")
_PrvtRsvpDiagFlowSpecGQBktRate_Type = Unsigned32
_PrvtRsvpDiagFlowSpecGQBktRate_Object = MibTableColumn
prvtRsvpDiagFlowSpecGQBktRate = _PrvtRsvpDiagFlowSpecGQBktRate_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 7, 1, 3, 1, 23),
    _PrvtRsvpDiagFlowSpecGQBktRate_Type()
)
prvtRsvpDiagFlowSpecGQBktRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtRsvpDiagFlowSpecGQBktRate.setStatus("current")
_PrvtRsvpDiagFlowSpecGQBktDep_Type = Unsigned32
_PrvtRsvpDiagFlowSpecGQBktDep_Object = MibTableColumn
prvtRsvpDiagFlowSpecGQBktDep = _PrvtRsvpDiagFlowSpecGQBktDep_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 7, 1, 3, 1, 24),
    _PrvtRsvpDiagFlowSpecGQBktDep_Type()
)
prvtRsvpDiagFlowSpecGQBktDep.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtRsvpDiagFlowSpecGQBktDep.setStatus("current")
_PrvtRsvpDiagFlowSpecGQPkDataRate_Type = Unsigned32
_PrvtRsvpDiagFlowSpecGQPkDataRate_Object = MibTableColumn
prvtRsvpDiagFlowSpecGQPkDataRate = _PrvtRsvpDiagFlowSpecGQPkDataRate_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 7, 1, 3, 1, 25),
    _PrvtRsvpDiagFlowSpecGQPkDataRate_Type()
)
prvtRsvpDiagFlowSpecGQPkDataRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtRsvpDiagFlowSpecGQPkDataRate.setStatus("current")
_PrvtRsvpDiagFlowSpecGQMinPolUnit_Type = Unsigned32
_PrvtRsvpDiagFlowSpecGQMinPolUnit_Object = MibTableColumn
prvtRsvpDiagFlowSpecGQMinPolUnit = _PrvtRsvpDiagFlowSpecGQMinPolUnit_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 7, 1, 3, 1, 26),
    _PrvtRsvpDiagFlowSpecGQMinPolUnit_Type()
)
prvtRsvpDiagFlowSpecGQMinPolUnit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtRsvpDiagFlowSpecGQMinPolUnit.setStatus("current")
_PrvtRsvpDiagFlowSpecGQMaxPktSize_Type = Unsigned32
_PrvtRsvpDiagFlowSpecGQMaxPktSize_Object = MibTableColumn
prvtRsvpDiagFlowSpecGQMaxPktSize = _PrvtRsvpDiagFlowSpecGQMaxPktSize_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 7, 1, 3, 1, 27),
    _PrvtRsvpDiagFlowSpecGQMaxPktSize_Type()
)
prvtRsvpDiagFlowSpecGQMaxPktSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtRsvpDiagFlowSpecGQMaxPktSize.setStatus("current")
_PrvtRsvpDiagFlowSpecGQRate_Type = Unsigned32
_PrvtRsvpDiagFlowSpecGQRate_Object = MibTableColumn
prvtRsvpDiagFlowSpecGQRate = _PrvtRsvpDiagFlowSpecGQRate_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 7, 1, 3, 1, 28),
    _PrvtRsvpDiagFlowSpecGQRate_Type()
)
prvtRsvpDiagFlowSpecGQRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtRsvpDiagFlowSpecGQRate.setStatus("current")
_PrvtRsvpDiagFlowSpecGQSlack_Type = Unsigned32
_PrvtRsvpDiagFlowSpecGQSlack_Object = MibTableColumn
prvtRsvpDiagFlowSpecGQSlack = _PrvtRsvpDiagFlowSpecGQSlack_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 7, 1, 3, 1, 29),
    _PrvtRsvpDiagFlowSpecGQSlack_Type()
)
prvtRsvpDiagFlowSpecGQSlack.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtRsvpDiagFlowSpecGQSlack.setStatus("current")


class _PrvtRsvpDiagFlowSpecCoSCoS_Type(Integer32):
    """Custom type prvtRsvpDiagFlowSpecCoSCoS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_PrvtRsvpDiagFlowSpecCoSCoS_Type.__name__ = "Integer32"
_PrvtRsvpDiagFlowSpecCoSCoS_Object = MibTableColumn
prvtRsvpDiagFlowSpecCoSCoS = _PrvtRsvpDiagFlowSpecCoSCoS_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 7, 1, 3, 1, 30),
    _PrvtRsvpDiagFlowSpecCoSCoS_Type()
)
prvtRsvpDiagFlowSpecCoSCoS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtRsvpDiagFlowSpecCoSCoS.setStatus("current")


class _PrvtRsvpDiagFlowSpecCoSMTU_Type(Integer32):
    """Custom type prvtRsvpDiagFlowSpecCoSMTU based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_PrvtRsvpDiagFlowSpecCoSMTU_Type.__name__ = "Integer32"
_PrvtRsvpDiagFlowSpecCoSMTU_Object = MibTableColumn
prvtRsvpDiagFlowSpecCoSMTU = _PrvtRsvpDiagFlowSpecCoSMTU_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 7, 1, 3, 1, 31),
    _PrvtRsvpDiagFlowSpecCoSMTU_Type()
)
prvtRsvpDiagFlowSpecCoSMTU.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtRsvpDiagFlowSpecCoSMTU.setStatus("current")
_PrvtRsvpDiagFilterSpecAddress_Type = IpAddress
_PrvtRsvpDiagFilterSpecAddress_Object = MibTableColumn
prvtRsvpDiagFilterSpecAddress = _PrvtRsvpDiagFilterSpecAddress_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 7, 1, 3, 1, 32),
    _PrvtRsvpDiagFilterSpecAddress_Type()
)
prvtRsvpDiagFilterSpecAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtRsvpDiagFilterSpecAddress.setStatus("current")


class _PrvtRsvpDiagFilterSpecLSPId_Type(Integer32):
    """Custom type prvtRsvpDiagFilterSpecLSPId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_PrvtRsvpDiagFilterSpecLSPId_Type.__name__ = "Integer32"
_PrvtRsvpDiagFilterSpecLSPId_Object = MibTableColumn
prvtRsvpDiagFilterSpecLSPId = _PrvtRsvpDiagFilterSpecLSPId_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 7, 1, 3, 1, 33),
    _PrvtRsvpDiagFilterSpecLSPId_Type()
)
prvtRsvpDiagFilterSpecLSPId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtRsvpDiagFilterSpecLSPId.setStatus("current")
_PrvtRsvpDiagConfirmRcvAddr_Type = IpAddress
_PrvtRsvpDiagConfirmRcvAddr_Object = MibTableColumn
prvtRsvpDiagConfirmRcvAddr = _PrvtRsvpDiagConfirmRcvAddr_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 7, 1, 3, 1, 34),
    _PrvtRsvpDiagConfirmRcvAddr_Type()
)
prvtRsvpDiagConfirmRcvAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtRsvpDiagConfirmRcvAddr.setStatus("current")
_PrvtRsvpDiagStyle_Type = Unsigned32
_PrvtRsvpDiagStyle_Object = MibTableColumn
prvtRsvpDiagStyle = _PrvtRsvpDiagStyle_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 7, 1, 3, 1, 35),
    _PrvtRsvpDiagStyle_Type()
)
prvtRsvpDiagStyle.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtRsvpDiagStyle.setStatus("current")
_PrvtRsvpConformance_ObjectIdentity = ObjectIdentity
prvtRsvpConformance = _PrvtRsvpConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 7, 2)
)
_PrvtRsvpCompliances_ObjectIdentity = ObjectIdentity
prvtRsvpCompliances = _PrvtRsvpCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 7, 2, 1)
)
_PrvtRsvpGroups_ObjectIdentity = ObjectIdentity
prvtRsvpGroups = _PrvtRsvpGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 7, 2, 2)
)

# Managed Objects groups

prvtRsvpProductGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 7, 2, 2, 2)
)
prvtRsvpProductGroup.setObjects(
      *(("PRVT-RSVP-MIB", "prvtRsvpProductASNumber"),
        ("PRVT-RSVP-MIB", "prvtRsvpProductSenderTTL"),
        ("PRVT-RSVP-MIB", "prvtRsvpProductMinTimerPeriod"),
        ("PRVT-RSVP-MIB", "prvtRsvpProductAPIIfIndex"),
        ("PRVT-RSVP-MIB", "prvtRsvpProductAPIAddress"),
        ("PRVT-RSVP-MIB", "prvtRsvpProductAPIRefreshInterval"),
        ("PRVT-RSVP-MIB", "prvtRsvpProductLocalRepairDelay"),
        ("PRVT-RSVP-MIB", "prvtRsvpProductRefreshInterval"),
        ("PRVT-RSVP-MIB", "prvtRsvpProductRefreshMultiple"),
        ("PRVT-RSVP-MIB", "prvtRsvpProductRfrshSlewDenom"),
        ("PRVT-RSVP-MIB", "prvtRsvpProductRfrshSlewNumerator"),
        ("PRVT-RSVP-MIB", "prvtRsvpProductBlockadeMultiple"),
        ("PRVT-RSVP-MIB", "prvtRsvpProductSocketBufPoolSize"),
        ("PRVT-RSVP-MIB", "prvtRsvpProductSwitchBufPoolSize"),
        ("PRVT-RSVP-MIB", "prvtRsvpProductTeMibBufPoolSize"),
        ("PRVT-RSVP-MIB", "prvtRsvpProductRoutingBufPoolSize"),
        ("PRVT-RSVP-MIB", "prvtRsvpProductLSPSetupPriority"),
        ("PRVT-RSVP-MIB", "prvtRsvpProductLSPHoldingPriority"),
        ("PRVT-RSVP-MIB", "prvtRsvpProductAdminStatus"),
        ("PRVT-RSVP-MIB", "prvtRsvpProductOperStatus"),
        ("PRVT-RSVP-MIB", "prvtRsvpProductRowStatus"),
        ("PRVT-RSVP-MIB", "prvtRsvpProductLsrIndex"),
        ("PRVT-RSVP-MIB", "prvtRsvpProductTeMibIndex"),
        ("PRVT-RSVP-MIB", "prvtRsvpProductMultiStackSupport"),
        ("PRVT-RSVP-MIB", "prvtRsvpProductUseHopByHop"),
        ("PRVT-RSVP-MIB", "prvtRsvpProductUseNotify"),
        ("PRVT-RSVP-MIB", "prvtRsvpProductNotifyRRDecay"),
        ("PRVT-RSVP-MIB", "prvtRsvpProductNotifyRRInterval"),
        ("PRVT-RSVP-MIB", "prvtRsvpProductNotifyRRLimit"),
        ("PRVT-RSVP-MIB", "prvtRsvpProductAllowIPEncap"),
        ("PRVT-RSVP-MIB", "prvtRsvpProductProtocolExtensions"),
        ("PRVT-RSVP-MIB", "prvtRsvpProductPSRFlags"),
        ("PRVT-RSVP-MIB", "prvtRsvpProductInitPathRRDecay"),
        ("PRVT-RSVP-MIB", "prvtRsvpProductInitPathRRInterval"),
        ("PRVT-RSVP-MIB", "prvtRsvpProductInitPathRRLimit"),
        ("PRVT-RSVP-MIB", "prvtRsvpProductEnableUni"),
        ("PRVT-RSVP-MIB", "prvtRsvpProductRestartCapable"),
        ("PRVT-RSVP-MIB", "prvtRsvpProductRestartTime"),
        ("PRVT-RSVP-MIB", "prvtRsvpProductRecoveryTime"),
        ("PRVT-RSVP-MIB", "prvtRsvpProductMinPeerRestart"),
        ("PRVT-RSVP-MIB", "prvtRsvpProductGracefulDelTimeout"),
        ("PRVT-RSVP-MIB", "prvtRsvpProductEgressDelBehavior"),
        ("PRVT-RSVP-MIB", "prvtRsvpProductEnabUniConnSplicing"),
        ("PRVT-RSVP-MIB", "prvtRsvpProductFastRerouteCaps"),
        ("PRVT-RSVP-MIB", "prvtRsvpProductFastRroutBkpRtryInt"),
        ("PRVT-RSVP-MIB", "prvtRsvpProductErrorActionFlags"),
        ("PRVT-RSVP-MIB", "prvtRsvpProductEnableNni"),
        ("PRVT-RSVP-MIB", "prvtRsvpProductBehaviorFlags"),
        ("PRVT-RSVP-MIB", "prvtRsvpProductLabelSetStyle"),
        ("PRVT-RSVP-MIB", "prvtRsvpProductLabelSetOperStatus"),
        ("PRVT-RSVP-MIB", "prvtRsvpProductLabelSetTrapEnable"),
        ("PRVT-RSVP-MIB", "prvtRsvpProductLabelSetChngAct"),
        ("PRVT-RSVP-MIB", "prvtRsvpProductExtPrtAdminStatus"),
        ("PRVT-RSVP-MIB", "prvtRsvpProductUniIncSonetProfile"),
        ("PRVT-RSVP-MIB", "prvtRsvpProductFrrFacAdminStatus"),
        ("PRVT-RSVP-MIB", "prvtRsvpProductFrrFacOperStatus"),
        ("PRVT-RSVP-MIB", "prvtRsvpProductIpv6AdminStatus"),
        ("PRVT-RSVP-MIB", "prvtRsvpProductIpv6OperStatus"),
        ("PRVT-RSVP-MIB", "prvtRsvpProductAPIIpv6Address"))
)
if mibBuilder.loadTexts:
    prvtRsvpProductGroup.setStatus("current")

prvtRsvpDiagGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 7, 2, 2, 3)
)
prvtRsvpDiagGroup.setObjects(
      *(("PRVT-RSVP-MIB", "prvtRsvpDiagReqsInProgress"),
        ("PRVT-RSVP-MIB", "prvtRsvpDiagSessionEndPoint"),
        ("PRVT-RSVP-MIB", "prvtRsvpDiagSessionTunnelId"),
        ("PRVT-RSVP-MIB", "prvtRsvpDiagSessionExtTunnelId"),
        ("PRVT-RSVP-MIB", "prvtRsvpDiagLastHop"),
        ("PRVT-RSVP-MIB", "prvtRsvpDiagSender"),
        ("PRVT-RSVP-MIB", "prvtRsvpDiagMaxHops"),
        ("PRVT-RSVP-MIB", "prvtRsvpDiagHopByHopReply"))
)
if mibBuilder.loadTexts:
    prvtRsvpDiagGroup.setStatus("current")

prvtRsvpDiagNodeGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 7, 2, 2, 4)
)
prvtRsvpDiagNodeGroup.setObjects(
      *(("PRVT-RSVP-MIB", "prvtRsvpDiagNodeType"),
        ("PRVT-RSVP-MIB", "prvtRsvpDiagNodeDreqArrivalTime"),
        ("PRVT-RSVP-MIB", "prvtRsvpDiagNodeIncomingIfAddr"),
        ("PRVT-RSVP-MIB", "prvtRsvpDiagNodeOutgoingIfAddr"),
        ("PRVT-RSVP-MIB", "prvtRsvpDiagNodePrevHopAddr"),
        ("PRVT-RSVP-MIB", "prvtRsvpDiagNodeDTTL"),
        ("PRVT-RSVP-MIB", "prvtRsvpDiagNodeMFlag"),
        ("PRVT-RSVP-MIB", "prvtRsvpDiagNodeRErr"),
        ("PRVT-RSVP-MIB", "prvtRsvpDiagNodeKValue"),
        ("PRVT-RSVP-MIB", "prvtRsvpDiagNodeTimerValue"),
        ("PRVT-RSVP-MIB", "prvtRsvpDiagRsvpHopAddr"),
        ("PRVT-RSVP-MIB", "prvtRsvpDiagRsvpHopLIH"),
        ("PRVT-RSVP-MIB", "prvtRsvpDiagSenderTpltLSPId"),
        ("PRVT-RSVP-MIB", "prvtRsvpDiagSenderTpltAddress"),
        ("PRVT-RSVP-MIB", "prvtRsvpDiagFlowSpecCLBktRate"),
        ("PRVT-RSVP-MIB", "prvtRsvpDiagFlowSpecCLBktDep"),
        ("PRVT-RSVP-MIB", "prvtRsvpDiagFlowSpecCLPkDataRate"),
        ("PRVT-RSVP-MIB", "prvtRsvpDiagFlowSpecCLMinPolUnit"),
        ("PRVT-RSVP-MIB", "prvtRsvpDiagFlowSpecCLMaxPktSize"),
        ("PRVT-RSVP-MIB", "prvtRsvpDiagFlowSpecGQBktRate"),
        ("PRVT-RSVP-MIB", "prvtRsvpDiagFlowSpecGQBktDep"),
        ("PRVT-RSVP-MIB", "prvtRsvpDiagFlowSpecGQPkDataRate"),
        ("PRVT-RSVP-MIB", "prvtRsvpDiagFlowSpecGQMinPolUnit"),
        ("PRVT-RSVP-MIB", "prvtRsvpDiagFlowSpecGQMaxPktSize"),
        ("PRVT-RSVP-MIB", "prvtRsvpDiagFlowSpecGQRate"),
        ("PRVT-RSVP-MIB", "prvtRsvpDiagFlowSpecGQSlack"),
        ("PRVT-RSVP-MIB", "prvtRsvpDiagFlowSpecCoSCoS"),
        ("PRVT-RSVP-MIB", "prvtRsvpDiagFlowSpecCoSMTU"),
        ("PRVT-RSVP-MIB", "prvtRsvpDiagFilterSpecAddress"),
        ("PRVT-RSVP-MIB", "prvtRsvpDiagFilterSpecLSPId"),
        ("PRVT-RSVP-MIB", "prvtRsvpDiagConfirmRcvAddr"),
        ("PRVT-RSVP-MIB", "prvtRsvpDiagStyle"))
)
if mibBuilder.loadTexts:
    prvtRsvpDiagNodeGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

prvtRsvpCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 7, 2, 1, 1)
)
prvtRsvpCompliance.setObjects(
      *(("PRVT-RSVP-MIB", "prvtRsvpProductGroup"),
        ("PRVT-RSVP-MIB", "prvtRsvpDiagGroup"),
        ("PRVT-RSVP-MIB", "prvtRsvpDiagNodeGroup"))
)
if mibBuilder.loadTexts:
    prvtRsvpCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "PRVT-RSVP-MIB",
    **{"PrvtRsvpAdminStatus": PrvtRsvpAdminStatus,
       "PrvtRsvpOperStatus": PrvtRsvpOperStatus,
       "PrvtRsvpIndex": PrvtRsvpIndex,
       "PrvtRsvpDiagReqIndex": PrvtRsvpDiagReqIndex,
       "PrvtRsvpDiagNodeIndexType": PrvtRsvpDiagNodeIndexType,
       "PrvtRsvpDiagNodeTypeVal": PrvtRsvpDiagNodeTypeVal,
       "prvtRsvp": prvtRsvp,
       "prvtRsvpObjects": prvtRsvpObjects,
       "prvtRsvpProductTable": prvtRsvpProductTable,
       "prvtRsvpProductEntry": prvtRsvpProductEntry,
       "prvtRsvpProductIndex": prvtRsvpProductIndex,
       "prvtRsvpProductASNumber": prvtRsvpProductASNumber,
       "prvtRsvpProductSenderTTL": prvtRsvpProductSenderTTL,
       "prvtRsvpProductMinTimerPeriod": prvtRsvpProductMinTimerPeriod,
       "prvtRsvpProductAPIIfIndex": prvtRsvpProductAPIIfIndex,
       "prvtRsvpProductAPIAddress": prvtRsvpProductAPIAddress,
       "prvtRsvpProductAPIRefreshInterval": prvtRsvpProductAPIRefreshInterval,
       "prvtRsvpProductLocalRepairDelay": prvtRsvpProductLocalRepairDelay,
       "prvtRsvpProductRefreshInterval": prvtRsvpProductRefreshInterval,
       "prvtRsvpProductRefreshMultiple": prvtRsvpProductRefreshMultiple,
       "prvtRsvpProductRfrshSlewDenom": prvtRsvpProductRfrshSlewDenom,
       "prvtRsvpProductRfrshSlewNumerator": prvtRsvpProductRfrshSlewNumerator,
       "prvtRsvpProductBlockadeMultiple": prvtRsvpProductBlockadeMultiple,
       "prvtRsvpProductSocketBufPoolSize": prvtRsvpProductSocketBufPoolSize,
       "prvtRsvpProductSwitchBufPoolSize": prvtRsvpProductSwitchBufPoolSize,
       "prvtRsvpProductTeMibBufPoolSize": prvtRsvpProductTeMibBufPoolSize,
       "prvtRsvpProductRoutingBufPoolSize": prvtRsvpProductRoutingBufPoolSize,
       "prvtRsvpProductLSPSetupPriority": prvtRsvpProductLSPSetupPriority,
       "prvtRsvpProductLSPHoldingPriority": prvtRsvpProductLSPHoldingPriority,
       "prvtRsvpProductAdminStatus": prvtRsvpProductAdminStatus,
       "prvtRsvpProductOperStatus": prvtRsvpProductOperStatus,
       "prvtRsvpProductRowStatus": prvtRsvpProductRowStatus,
       "prvtRsvpProductLsrIndex": prvtRsvpProductLsrIndex,
       "prvtRsvpProductTeMibIndex": prvtRsvpProductTeMibIndex,
       "prvtRsvpProductMultiStackSupport": prvtRsvpProductMultiStackSupport,
       "prvtRsvpProductUseHopByHop": prvtRsvpProductUseHopByHop,
       "prvtRsvpProductUseNotify": prvtRsvpProductUseNotify,
       "prvtRsvpProductNotifyRRDecay": prvtRsvpProductNotifyRRDecay,
       "prvtRsvpProductNotifyRRInterval": prvtRsvpProductNotifyRRInterval,
       "prvtRsvpProductNotifyRRLimit": prvtRsvpProductNotifyRRLimit,
       "prvtRsvpProductAllowIPEncap": prvtRsvpProductAllowIPEncap,
       "prvtRsvpProductProtocolExtensions": prvtRsvpProductProtocolExtensions,
       "prvtRsvpProductPSRFlags": prvtRsvpProductPSRFlags,
       "prvtRsvpProductInitPathRRDecay": prvtRsvpProductInitPathRRDecay,
       "prvtRsvpProductInitPathRRInterval": prvtRsvpProductInitPathRRInterval,
       "prvtRsvpProductInitPathRRLimit": prvtRsvpProductInitPathRRLimit,
       "prvtRsvpProductEnableUni": prvtRsvpProductEnableUni,
       "prvtRsvpProductRestartCapable": prvtRsvpProductRestartCapable,
       "prvtRsvpProductRestartTime": prvtRsvpProductRestartTime,
       "prvtRsvpProductRecoveryTime": prvtRsvpProductRecoveryTime,
       "prvtRsvpProductMinPeerRestart": prvtRsvpProductMinPeerRestart,
       "prvtRsvpProductGracefulDelTimeout": prvtRsvpProductGracefulDelTimeout,
       "prvtRsvpProductEgressDelBehavior": prvtRsvpProductEgressDelBehavior,
       "prvtRsvpProductEnabUniConnSplicing": prvtRsvpProductEnabUniConnSplicing,
       "prvtRsvpProductFastRerouteCaps": prvtRsvpProductFastRerouteCaps,
       "prvtRsvpProductFastRroutBkpRtryInt": prvtRsvpProductFastRroutBkpRtryInt,
       "prvtRsvpProductErrorActionFlags": prvtRsvpProductErrorActionFlags,
       "prvtRsvpProductEnableNni": prvtRsvpProductEnableNni,
       "prvtRsvpProductBehaviorFlags": prvtRsvpProductBehaviorFlags,
       "prvtRsvpProductLabelSetStyle": prvtRsvpProductLabelSetStyle,
       "prvtRsvpProductLabelSetOperStatus": prvtRsvpProductLabelSetOperStatus,
       "prvtRsvpProductLabelSetTrapEnable": prvtRsvpProductLabelSetTrapEnable,
       "prvtRsvpProductLabelSetChngAct": prvtRsvpProductLabelSetChngAct,
       "prvtRsvpProductExtPrtAdminStatus": prvtRsvpProductExtPrtAdminStatus,
       "prvtRsvpProductUniIncSonetProfile": prvtRsvpProductUniIncSonetProfile,
       "prvtRsvpProductFrrFacAdminStatus": prvtRsvpProductFrrFacAdminStatus,
       "prvtRsvpProductFrrFacOperStatus": prvtRsvpProductFrrFacOperStatus,
       "prvtRsvpProductIpv6AdminStatus": prvtRsvpProductIpv6AdminStatus,
       "prvtRsvpProductIpv6OperStatus": prvtRsvpProductIpv6OperStatus,
       "prvtRsvpProductAPIIpv6Address": prvtRsvpProductAPIIpv6Address,
       "prvtRsvpDiagnosticTable": prvtRsvpDiagnosticTable,
       "prvtRsvpDiagnosticEntry": prvtRsvpDiagnosticEntry,
       "prvtRsvpDiagProductIndex": prvtRsvpDiagProductIndex,
       "prvtRsvpDiagRequestIndex": prvtRsvpDiagRequestIndex,
       "prvtRsvpDiagReqsInProgress": prvtRsvpDiagReqsInProgress,
       "prvtRsvpDiagSessionEndPoint": prvtRsvpDiagSessionEndPoint,
       "prvtRsvpDiagSessionTunnelId": prvtRsvpDiagSessionTunnelId,
       "prvtRsvpDiagSessionExtTunnelId": prvtRsvpDiagSessionExtTunnelId,
       "prvtRsvpDiagLastHop": prvtRsvpDiagLastHop,
       "prvtRsvpDiagSender": prvtRsvpDiagSender,
       "prvtRsvpDiagMaxHops": prvtRsvpDiagMaxHops,
       "prvtRsvpDiagHopByHopReply": prvtRsvpDiagHopByHopReply,
       "prvtRsvpDiagNodeTable": prvtRsvpDiagNodeTable,
       "prvtRsvpDiagNodeEntry": prvtRsvpDiagNodeEntry,
       "prvtRsvpDiagNodeProductIndex": prvtRsvpDiagNodeProductIndex,
       "prvtRsvpDiagNodeRequestIndex": prvtRsvpDiagNodeRequestIndex,
       "prvtRsvpDiagNodeIndex": prvtRsvpDiagNodeIndex,
       "prvtRsvpDiagNodeType": prvtRsvpDiagNodeType,
       "prvtRsvpDiagNodeDreqArrivalTime": prvtRsvpDiagNodeDreqArrivalTime,
       "prvtRsvpDiagNodeIncomingIfAddr": prvtRsvpDiagNodeIncomingIfAddr,
       "prvtRsvpDiagNodeOutgoingIfAddr": prvtRsvpDiagNodeOutgoingIfAddr,
       "prvtRsvpDiagNodePrevHopAddr": prvtRsvpDiagNodePrevHopAddr,
       "prvtRsvpDiagNodeDTTL": prvtRsvpDiagNodeDTTL,
       "prvtRsvpDiagNodeMFlag": prvtRsvpDiagNodeMFlag,
       "prvtRsvpDiagNodeRErr": prvtRsvpDiagNodeRErr,
       "prvtRsvpDiagNodeKValue": prvtRsvpDiagNodeKValue,
       "prvtRsvpDiagNodeTimerValue": prvtRsvpDiagNodeTimerValue,
       "prvtRsvpDiagRsvpHopAddr": prvtRsvpDiagRsvpHopAddr,
       "prvtRsvpDiagRsvpHopLIH": prvtRsvpDiagRsvpHopLIH,
       "prvtRsvpDiagSenderTpltAddress": prvtRsvpDiagSenderTpltAddress,
       "prvtRsvpDiagSenderTpltLSPId": prvtRsvpDiagSenderTpltLSPId,
       "prvtRsvpDiagFlowSpecCLBktRate": prvtRsvpDiagFlowSpecCLBktRate,
       "prvtRsvpDiagFlowSpecCLBktDep": prvtRsvpDiagFlowSpecCLBktDep,
       "prvtRsvpDiagFlowSpecCLPkDataRate": prvtRsvpDiagFlowSpecCLPkDataRate,
       "prvtRsvpDiagFlowSpecCLMinPolUnit": prvtRsvpDiagFlowSpecCLMinPolUnit,
       "prvtRsvpDiagFlowSpecCLMaxPktSize": prvtRsvpDiagFlowSpecCLMaxPktSize,
       "prvtRsvpDiagFlowSpecGQBktRate": prvtRsvpDiagFlowSpecGQBktRate,
       "prvtRsvpDiagFlowSpecGQBktDep": prvtRsvpDiagFlowSpecGQBktDep,
       "prvtRsvpDiagFlowSpecGQPkDataRate": prvtRsvpDiagFlowSpecGQPkDataRate,
       "prvtRsvpDiagFlowSpecGQMinPolUnit": prvtRsvpDiagFlowSpecGQMinPolUnit,
       "prvtRsvpDiagFlowSpecGQMaxPktSize": prvtRsvpDiagFlowSpecGQMaxPktSize,
       "prvtRsvpDiagFlowSpecGQRate": prvtRsvpDiagFlowSpecGQRate,
       "prvtRsvpDiagFlowSpecGQSlack": prvtRsvpDiagFlowSpecGQSlack,
       "prvtRsvpDiagFlowSpecCoSCoS": prvtRsvpDiagFlowSpecCoSCoS,
       "prvtRsvpDiagFlowSpecCoSMTU": prvtRsvpDiagFlowSpecCoSMTU,
       "prvtRsvpDiagFilterSpecAddress": prvtRsvpDiagFilterSpecAddress,
       "prvtRsvpDiagFilterSpecLSPId": prvtRsvpDiagFilterSpecLSPId,
       "prvtRsvpDiagConfirmRcvAddr": prvtRsvpDiagConfirmRcvAddr,
       "prvtRsvpDiagStyle": prvtRsvpDiagStyle,
       "prvtRsvpConformance": prvtRsvpConformance,
       "prvtRsvpCompliances": prvtRsvpCompliances,
       "prvtRsvpCompliance": prvtRsvpCompliance,
       "prvtRsvpGroups": prvtRsvpGroups,
       "prvtRsvpProductGroup": prvtRsvpProductGroup,
       "prvtRsvpDiagGroup": prvtRsvpDiagGroup,
       "prvtRsvpDiagNodeGroup": prvtRsvpDiagNodeGroup}
)
