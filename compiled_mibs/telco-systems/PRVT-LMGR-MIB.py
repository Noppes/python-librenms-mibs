# SNMP MIB module (PRVT-LMGR-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\telco-systems\binos\PRVT-LMGR-MIB

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

(InetAddress,
 InetAddressIPv4,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressIPv4",
    "InetAddressType")

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

prvtLmgr = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 4)
)
if mibBuilder.loadTexts:
    prvtLmgr.setRevisions(
        ("2006-06-11 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class PrvtLmgrAdminStatus(TextualConvention, Integer32):
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



class PrvtLmgrOperStatus(TextualConvention, Integer32):
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



class PrvtLmgrPartnerStatus(TextualConvention, Integer32):
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
              6)
        )
    )
    namedValues = NamedValues(
        *(("initial", 0),
          ("activating", 1),
          ("active", 2),
          ("deactivating", 3),
          ("failedOver", 4),
          ("failed", 5),
          ("unavailable", 6))
    )



class PrvtLmgrIndex(TextualConvention, Unsigned32):
    status = "current"


class PrvtLmgrControlModes(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ordered", 1),
          ("independent", 2))
    )



# MIB Managed Objects in the order of their OIDs

_PrvtLmgrObjects_ObjectIdentity = ObjectIdentity
prvtLmgrObjects = _PrvtLmgrObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 4, 1)
)
_PrvtLsrId_Type = InetAddressIPv4
_PrvtLsrId_Object = MibScalar
prvtLsrId = _PrvtLsrId_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 4, 1, 1),
    _PrvtLsrId_Type()
)
prvtLsrId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prvtLsrId.setStatus("current")
_PrvtLmgrLsrEntityTable_Object = MibTable
prvtLmgrLsrEntityTable = _PrvtLmgrLsrEntityTable_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 4, 1, 2)
)
if mibBuilder.loadTexts:
    prvtLmgrLsrEntityTable.setStatus("current")
_PrvtLmgrLsrEntityEntry_Object = MibTableRow
prvtLmgrLsrEntityEntry = _PrvtLmgrLsrEntityEntry_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 4, 1, 2, 1)
)
prvtLmgrLsrEntityEntry.setIndexNames(
    (0, "PRVT-LMGR-MIB", "prvtlmgrLsrEntityLsrIndex"),
)
if mibBuilder.loadTexts:
    prvtLmgrLsrEntityEntry.setStatus("current")
_PrvtlmgrLsrEntityLsrIndex_Type = PrvtLmgrIndex
_PrvtlmgrLsrEntityLsrIndex_Object = MibTableColumn
prvtlmgrLsrEntityLsrIndex = _PrvtlmgrLsrEntityLsrIndex_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 4, 1, 2, 1, 1),
    _PrvtlmgrLsrEntityLsrIndex_Type()
)
prvtlmgrLsrEntityLsrIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    prvtlmgrLsrEntityLsrIndex.setStatus("current")


class _PrvtLmgrLsrEntityAdminStatus_Type(PrvtLmgrAdminStatus):
    """Custom type prvtLmgrLsrEntityAdminStatus based on PrvtLmgrAdminStatus"""
    defaultValue = 1


_PrvtLmgrLsrEntityAdminStatus_Type.__name__ = "PrvtLmgrAdminStatus"
_PrvtLmgrLsrEntityAdminStatus_Object = MibTableColumn
prvtLmgrLsrEntityAdminStatus = _PrvtLmgrLsrEntityAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 4, 1, 2, 1, 2),
    _PrvtLmgrLsrEntityAdminStatus_Type()
)
prvtLmgrLsrEntityAdminStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    prvtLmgrLsrEntityAdminStatus.setStatus("current")
_PrvtLmgrLsrEntityOperStatus_Type = PrvtLmgrOperStatus
_PrvtLmgrLsrEntityOperStatus_Object = MibTableColumn
prvtLmgrLsrEntityOperStatus = _PrvtLmgrLsrEntityOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 4, 1, 2, 1, 3),
    _PrvtLmgrLsrEntityOperStatus_Type()
)
prvtLmgrLsrEntityOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtLmgrLsrEntityOperStatus.setStatus("current")
_PrvtLmgrLsrEntityRowStatus_Type = RowStatus
_PrvtLmgrLsrEntityRowStatus_Object = MibTableColumn
prvtLmgrLsrEntityRowStatus = _PrvtLmgrLsrEntityRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 4, 1, 2, 1, 4),
    _PrvtLmgrLsrEntityRowStatus_Type()
)
prvtLmgrLsrEntityRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    prvtLmgrLsrEntityRowStatus.setStatus("current")
_PrvtLmgrLsrEntityMinLsiBuffers_Type = Unsigned32
_PrvtLmgrLsrEntityMinLsiBuffers_Object = MibTableColumn
prvtLmgrLsrEntityMinLsiBuffers = _PrvtLmgrLsrEntityMinLsiBuffers_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 4, 1, 2, 1, 5),
    _PrvtLmgrLsrEntityMinLsiBuffers_Type()
)
prvtLmgrLsrEntityMinLsiBuffers.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    prvtLmgrLsrEntityMinLsiBuffers.setStatus("current")
_PrvtLmgrLsrEntityMaxLsiBuffers_Type = Unsigned32
_PrvtLmgrLsrEntityMaxLsiBuffers_Object = MibTableColumn
prvtLmgrLsrEntityMaxLsiBuffers = _PrvtLmgrLsrEntityMaxLsiBuffers_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 4, 1, 2, 1, 6),
    _PrvtLmgrLsrEntityMaxLsiBuffers_Type()
)
prvtLmgrLsrEntityMaxLsiBuffers.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    prvtLmgrLsrEntityMaxLsiBuffers.setStatus("current")
_PrvtLmgrLscStatus_Type = PrvtLmgrPartnerStatus
_PrvtLmgrLscStatus_Object = MibTableColumn
prvtLmgrLscStatus = _PrvtLmgrLscStatus_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 4, 1, 2, 1, 7),
    _PrvtLmgrLscStatus_Type()
)
prvtLmgrLscStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtLmgrLscStatus.setStatus("current")
_PrvtLmgrLdbCount_Type = Unsigned32
_PrvtLmgrLdbCount_Object = MibTableColumn
prvtLmgrLdbCount = _PrvtLmgrLdbCount_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 4, 1, 2, 1, 8),
    _PrvtLmgrLdbCount_Type()
)
prvtLmgrLdbCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtLmgrLdbCount.setStatus("current")
_PrvtLmgrLsrEntityLsrId_Type = Unsigned32
_PrvtLmgrLsrEntityLsrId_Object = MibTableColumn
prvtLmgrLsrEntityLsrId = _PrvtLmgrLsrEntityLsrId_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 4, 1, 2, 1, 9),
    _PrvtLmgrLsrEntityLsrId_Type()
)
prvtLmgrLsrEntityLsrId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtLmgrLsrEntityLsrId.setStatus("current")
_PrvtLmgrLsrEntityTranAddrType_Type = InetAddressType
_PrvtLmgrLsrEntityTranAddrType_Object = MibTableColumn
prvtLmgrLsrEntityTranAddrType = _PrvtLmgrLsrEntityTranAddrType_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 4, 1, 2, 1, 10),
    _PrvtLmgrLsrEntityTranAddrType_Type()
)
prvtLmgrLsrEntityTranAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    prvtLmgrLsrEntityTranAddrType.setStatus("current")
_PrvtLmgrLsrEntityTranAddrLen_Type = Unsigned32
_PrvtLmgrLsrEntityTranAddrLen_Object = MibTableColumn
prvtLmgrLsrEntityTranAddrLen = _PrvtLmgrLsrEntityTranAddrLen_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 4, 1, 2, 1, 11),
    _PrvtLmgrLsrEntityTranAddrLen_Type()
)
prvtLmgrLsrEntityTranAddrLen.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    prvtLmgrLsrEntityTranAddrLen.setStatus("current")
_PrvtLmgrLsrEntityTranAddr_Type = InetAddress
_PrvtLmgrLsrEntityTranAddr_Object = MibTableColumn
prvtLmgrLsrEntityTranAddr = _PrvtLmgrLsrEntityTranAddr_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 4, 1, 2, 1, 12),
    _PrvtLmgrLsrEntityTranAddr_Type()
)
prvtLmgrLsrEntityTranAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    prvtLmgrLsrEntityTranAddr.setStatus("current")
_PrvtLmgrLsrEntityControlMode_Type = PrvtLmgrControlModes
_PrvtLmgrLsrEntityControlMode_Object = MibTableColumn
prvtLmgrLsrEntityControlMode = _PrvtLmgrLsrEntityControlMode_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 4, 1, 2, 1, 13),
    _PrvtLmgrLsrEntityControlMode_Type()
)
prvtLmgrLsrEntityControlMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    prvtLmgrLsrEntityControlMode.setStatus("current")


class _PrvtLmgrLsrEntityMergeLsps_Type(TruthValue):
    """Custom type prvtLmgrLsrEntityMergeLsps based on TruthValue"""
    defaultValue = 2


_PrvtLmgrLsrEntityMergeLsps_Type.__name__ = "TruthValue"
_PrvtLmgrLsrEntityMergeLsps_Object = MibTableColumn
prvtLmgrLsrEntityMergeLsps = _PrvtLmgrLsrEntityMergeLsps_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 4, 1, 2, 1, 14),
    _PrvtLmgrLsrEntityMergeLsps_Type()
)
prvtLmgrLsrEntityMergeLsps.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    prvtLmgrLsrEntityMergeLsps.setStatus("current")


class _PrvtLmgrLsrEntityLoopDetection_Type(TruthValue):
    """Custom type prvtLmgrLsrEntityLoopDetection based on TruthValue"""
    defaultValue = 2


_PrvtLmgrLsrEntityLoopDetection_Type.__name__ = "TruthValue"
_PrvtLmgrLsrEntityLoopDetection_Object = MibTableColumn
prvtLmgrLsrEntityLoopDetection = _PrvtLmgrLsrEntityLoopDetection_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 4, 1, 2, 1, 15),
    _PrvtLmgrLsrEntityLoopDetection_Type()
)
prvtLmgrLsrEntityLoopDetection.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    prvtLmgrLsrEntityLoopDetection.setStatus("current")


class _PrvtLmgrLsrEntityPerformGrouping_Type(TruthValue):
    """Custom type prvtLmgrLsrEntityPerformGrouping based on TruthValue"""
    defaultValue = 2


_PrvtLmgrLsrEntityPerformGrouping_Type.__name__ = "TruthValue"
_PrvtLmgrLsrEntityPerformGrouping_Object = MibTableColumn
prvtLmgrLsrEntityPerformGrouping = _PrvtLmgrLsrEntityPerformGrouping_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 4, 1, 2, 1, 16),
    _PrvtLmgrLsrEntityPerformGrouping_Type()
)
prvtLmgrLsrEntityPerformGrouping.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    prvtLmgrLsrEntityPerformGrouping.setStatus("current")


class _PrvtLmgrLsrAutoStaticLsps_Type(TruthValue):
    """Custom type prvtLmgrLsrAutoStaticLsps based on TruthValue"""
    defaultValue = 2


_PrvtLmgrLsrAutoStaticLsps_Type.__name__ = "TruthValue"
_PrvtLmgrLsrAutoStaticLsps_Object = MibTableColumn
prvtLmgrLsrAutoStaticLsps = _PrvtLmgrLsrAutoStaticLsps_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 4, 1, 2, 1, 17),
    _PrvtLmgrLsrAutoStaticLsps_Type()
)
prvtLmgrLsrAutoStaticLsps.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    prvtLmgrLsrAutoStaticLsps.setStatus("current")


class _PrvtLmgrLsrDisplayPhpXCs_Type(TruthValue):
    """Custom type prvtLmgrLsrDisplayPhpXCs based on TruthValue"""
    defaultValue = 2


_PrvtLmgrLsrDisplayPhpXCs_Type.__name__ = "TruthValue"
_PrvtLmgrLsrDisplayPhpXCs_Object = MibTableColumn
prvtLmgrLsrDisplayPhpXCs = _PrvtLmgrLsrDisplayPhpXCs_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 4, 1, 2, 1, 18),
    _PrvtLmgrLsrDisplayPhpXCs_Type()
)
prvtLmgrLsrDisplayPhpXCs.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    prvtLmgrLsrDisplayPhpXCs.setStatus("current")
_PrvtLmgrLsrEntityIpv6TranAddr_Type = InetAddress
_PrvtLmgrLsrEntityIpv6TranAddr_Object = MibTableColumn
prvtLmgrLsrEntityIpv6TranAddr = _PrvtLmgrLsrEntityIpv6TranAddr_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 4, 1, 2, 1, 19),
    _PrvtLmgrLsrEntityIpv6TranAddr_Type()
)
prvtLmgrLsrEntityIpv6TranAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    prvtLmgrLsrEntityIpv6TranAddr.setStatus("current")
_PrvtLmgrLsrLspXcTable_Object = MibTable
prvtLmgrLsrLspXcTable = _PrvtLmgrLsrLspXcTable_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 4, 1, 3)
)
if mibBuilder.loadTexts:
    prvtLmgrLsrLspXcTable.setStatus("current")
_PrvtLmgrLsrLspXcEntry_Object = MibTableRow
prvtLmgrLsrLspXcEntry = _PrvtLmgrLsrLspXcEntry_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 4, 1, 3, 1)
)
prvtLmgrLsrLspXcEntry.setIndexNames(
    (0, "PRVT-LMGR-MIB", "prvtlmgrLsrEntityLsrIndex"),
    (0, "PRVT-LMGR-MIB", "prvtLmgrLsrLspXcIndex"),
    (0, "PRVT-LMGR-MIB", "prvtLmgrLsrLspInSegLabel"),
    (0, "PRVT-LMGR-MIB", "prvtLmgrLsrLspOutSegIndex"),
)
if mibBuilder.loadTexts:
    prvtLmgrLsrLspXcEntry.setStatus("current")
_PrvtLmgrLsrLspXcIndex_Type = Unsigned32
_PrvtLmgrLsrLspXcIndex_Object = MibTableColumn
prvtLmgrLsrLspXcIndex = _PrvtLmgrLsrLspXcIndex_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 4, 1, 3, 1, 2),
    _PrvtLmgrLsrLspXcIndex_Type()
)
prvtLmgrLsrLspXcIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    prvtLmgrLsrLspXcIndex.setStatus("current")
_PrvtLmgrLsrLspInSegIndex_Type = Unsigned32
_PrvtLmgrLsrLspInSegIndex_Object = MibTableColumn
prvtLmgrLsrLspInSegIndex = _PrvtLmgrLsrLspInSegIndex_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 4, 1, 3, 1, 3),
    _PrvtLmgrLsrLspInSegIndex_Type()
)
prvtLmgrLsrLspInSegIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    prvtLmgrLsrLspInSegIndex.setStatus("current")
_PrvtLmgrLsrLspInSegIfIndex_Type = Unsigned32
_PrvtLmgrLsrLspInSegIfIndex_Object = MibTableColumn
prvtLmgrLsrLspInSegIfIndex = _PrvtLmgrLsrLspInSegIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 4, 1, 3, 1, 4),
    _PrvtLmgrLsrLspInSegIfIndex_Type()
)
prvtLmgrLsrLspInSegIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtLmgrLsrLspInSegIfIndex.setStatus("current")
_PrvtLmgrLsrLspInSegLabel_Type = Unsigned32
_PrvtLmgrLsrLspInSegLabel_Object = MibTableColumn
prvtLmgrLsrLspInSegLabel = _PrvtLmgrLsrLspInSegLabel_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 4, 1, 3, 1, 5),
    _PrvtLmgrLsrLspInSegLabel_Type()
)
prvtLmgrLsrLspInSegLabel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtLmgrLsrLspInSegLabel.setStatus("current")
_PrvtLmgrLsrLspOutSegIndex_Type = Unsigned32
_PrvtLmgrLsrLspOutSegIndex_Object = MibTableColumn
prvtLmgrLsrLspOutSegIndex = _PrvtLmgrLsrLspOutSegIndex_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 4, 1, 3, 1, 6),
    _PrvtLmgrLsrLspOutSegIndex_Type()
)
prvtLmgrLsrLspOutSegIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    prvtLmgrLsrLspOutSegIndex.setStatus("current")
_PrvtLmgrLsrLspOutSegIfIndex_Type = Unsigned32
_PrvtLmgrLsrLspOutSegIfIndex_Object = MibTableColumn
prvtLmgrLsrLspOutSegIfIndex = _PrvtLmgrLsrLspOutSegIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 4, 1, 3, 1, 7),
    _PrvtLmgrLsrLspOutSegIfIndex_Type()
)
prvtLmgrLsrLspOutSegIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtLmgrLsrLspOutSegIfIndex.setStatus("current")
_PrvtLmgrLsrLspOutSegLabel_Type = Unsigned32
_PrvtLmgrLsrLspOutSegLabel_Object = MibTableColumn
prvtLmgrLsrLspOutSegLabel = _PrvtLmgrLsrLspOutSegLabel_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 4, 1, 3, 1, 8),
    _PrvtLmgrLsrLspOutSegLabel_Type()
)
prvtLmgrLsrLspOutSegLabel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtLmgrLsrLspOutSegLabel.setStatus("current")
_PrvtLmgrLsrLspOutSegNextHopAddr_Type = InetAddressIPv4
_PrvtLmgrLsrLspOutSegNextHopAddr_Object = MibTableColumn
prvtLmgrLsrLspOutSegNextHopAddr = _PrvtLmgrLsrLspOutSegNextHopAddr_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 4, 1, 3, 1, 9),
    _PrvtLmgrLsrLspOutSegNextHopAddr_Type()
)
prvtLmgrLsrLspOutSegNextHopAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtLmgrLsrLspOutSegNextHopAddr.setStatus("current")
_PrvtLmgrConformance_ObjectIdentity = ObjectIdentity
prvtLmgrConformance = _PrvtLmgrConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 4, 2)
)
_PrvtLmgrCompliances_ObjectIdentity = ObjectIdentity
prvtLmgrCompliances = _PrvtLmgrCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 4, 2, 1)
)
_PrvtLmgrGroups_ObjectIdentity = ObjectIdentity
prvtLmgrGroups = _PrvtLmgrGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 4, 2, 2)
)

# Managed Objects groups

prvtLmgrEntityGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 4, 2, 2, 2)
)
prvtLmgrEntityGroup.setObjects(
      *(("PRVT-LMGR-MIB", "prvtLmgrLsrEntityAdminStatus"),
        ("PRVT-LMGR-MIB", "prvtLmgrLsrEntityOperStatus"),
        ("PRVT-LMGR-MIB", "prvtLmgrLsrEntityRowStatus"),
        ("PRVT-LMGR-MIB", "prvtLmgrLsrEntityMinLsiBuffers"),
        ("PRVT-LMGR-MIB", "prvtLmgrLsrEntityMaxLsiBuffers"),
        ("PRVT-LMGR-MIB", "prvtLmgrLsrEntityLsrId"),
        ("PRVT-LMGR-MIB", "prvtLmgrLsrEntityTranAddrType"),
        ("PRVT-LMGR-MIB", "prvtLmgrLsrEntityTranAddrLen"),
        ("PRVT-LMGR-MIB", "prvtLmgrLsrEntityTranAddr"),
        ("PRVT-LMGR-MIB", "prvtLmgrLsrEntityControlMode"),
        ("PRVT-LMGR-MIB", "prvtLmgrLsrEntityMergeLsps"),
        ("PRVT-LMGR-MIB", "prvtLmgrLsrEntityLoopDetection"),
        ("PRVT-LMGR-MIB", "prvtLmgrLsrEntityPerformGrouping"))
)
if mibBuilder.loadTexts:
    prvtLmgrEntityGroup.setStatus("current")

prvtLmgrMiscGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 4, 2, 2, 3)
)
prvtLmgrMiscGroup.setObjects(
      *(("PRVT-LMGR-MIB", "prvtLmgrLscStatus"),
        ("PRVT-LMGR-MIB", "prvtLmgrLdbCount"),
        ("PRVT-LMGR-MIB", "prvtLmgrLsrAutoStaticLsps"),
        ("PRVT-LMGR-MIB", "prvtLmgrLsrDisplayPhpXCs"),
        ("PRVT-LMGR-MIB", "prvtLmgrLsrLspInSegIfIndex"),
        ("PRVT-LMGR-MIB", "prvtLmgrLsrLspInSegLabel"),
        ("PRVT-LMGR-MIB", "prvtLmgrLsrLspOutSegIfIndex"),
        ("PRVT-LMGR-MIB", "prvtLmgrLsrLspOutSegLabel"),
        ("PRVT-LMGR-MIB", "prvtLmgrLsrLspOutSegNextHopAddr"),
        ("PRVT-LMGR-MIB", "prvtLmgrLsrEntityIpv6TranAddr"))
)
if mibBuilder.loadTexts:
    prvtLmgrMiscGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

prvtLmgrCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 4, 2, 1, 1)
)
prvtLmgrCompliance.setObjects(
      *(("PRVT-LMGR-MIB", "prvtLmgrEntityGroup"),
        ("PRVT-LMGR-MIB", "prvtLmgrMiscGroup"))
)
if mibBuilder.loadTexts:
    prvtLmgrCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "PRVT-LMGR-MIB",
    **{"PrvtLmgrAdminStatus": PrvtLmgrAdminStatus,
       "PrvtLmgrOperStatus": PrvtLmgrOperStatus,
       "PrvtLmgrPartnerStatus": PrvtLmgrPartnerStatus,
       "PrvtLmgrIndex": PrvtLmgrIndex,
       "PrvtLmgrControlModes": PrvtLmgrControlModes,
       "prvtLmgr": prvtLmgr,
       "prvtLmgrObjects": prvtLmgrObjects,
       "prvtLsrId": prvtLsrId,
       "prvtLmgrLsrEntityTable": prvtLmgrLsrEntityTable,
       "prvtLmgrLsrEntityEntry": prvtLmgrLsrEntityEntry,
       "prvtlmgrLsrEntityLsrIndex": prvtlmgrLsrEntityLsrIndex,
       "prvtLmgrLsrEntityAdminStatus": prvtLmgrLsrEntityAdminStatus,
       "prvtLmgrLsrEntityOperStatus": prvtLmgrLsrEntityOperStatus,
       "prvtLmgrLsrEntityRowStatus": prvtLmgrLsrEntityRowStatus,
       "prvtLmgrLsrEntityMinLsiBuffers": prvtLmgrLsrEntityMinLsiBuffers,
       "prvtLmgrLsrEntityMaxLsiBuffers": prvtLmgrLsrEntityMaxLsiBuffers,
       "prvtLmgrLscStatus": prvtLmgrLscStatus,
       "prvtLmgrLdbCount": prvtLmgrLdbCount,
       "prvtLmgrLsrEntityLsrId": prvtLmgrLsrEntityLsrId,
       "prvtLmgrLsrEntityTranAddrType": prvtLmgrLsrEntityTranAddrType,
       "prvtLmgrLsrEntityTranAddrLen": prvtLmgrLsrEntityTranAddrLen,
       "prvtLmgrLsrEntityTranAddr": prvtLmgrLsrEntityTranAddr,
       "prvtLmgrLsrEntityControlMode": prvtLmgrLsrEntityControlMode,
       "prvtLmgrLsrEntityMergeLsps": prvtLmgrLsrEntityMergeLsps,
       "prvtLmgrLsrEntityLoopDetection": prvtLmgrLsrEntityLoopDetection,
       "prvtLmgrLsrEntityPerformGrouping": prvtLmgrLsrEntityPerformGrouping,
       "prvtLmgrLsrAutoStaticLsps": prvtLmgrLsrAutoStaticLsps,
       "prvtLmgrLsrDisplayPhpXCs": prvtLmgrLsrDisplayPhpXCs,
       "prvtLmgrLsrEntityIpv6TranAddr": prvtLmgrLsrEntityIpv6TranAddr,
       "prvtLmgrLsrLspXcTable": prvtLmgrLsrLspXcTable,
       "prvtLmgrLsrLspXcEntry": prvtLmgrLsrLspXcEntry,
       "prvtLmgrLsrLspXcIndex": prvtLmgrLsrLspXcIndex,
       "prvtLmgrLsrLspInSegIndex": prvtLmgrLsrLspInSegIndex,
       "prvtLmgrLsrLspInSegIfIndex": prvtLmgrLsrLspInSegIfIndex,
       "prvtLmgrLsrLspInSegLabel": prvtLmgrLsrLspInSegLabel,
       "prvtLmgrLsrLspOutSegIndex": prvtLmgrLsrLspOutSegIndex,
       "prvtLmgrLsrLspOutSegIfIndex": prvtLmgrLsrLspOutSegIfIndex,
       "prvtLmgrLsrLspOutSegLabel": prvtLmgrLsrLspOutSegLabel,
       "prvtLmgrLsrLspOutSegNextHopAddr": prvtLmgrLsrLspOutSegNextHopAddr,
       "prvtLmgrConformance": prvtLmgrConformance,
       "prvtLmgrCompliances": prvtLmgrCompliances,
       "prvtLmgrCompliance": prvtLmgrCompliance,
       "prvtLmgrGroups": prvtLmgrGroups,
       "prvtLmgrEntityGroup": prvtLmgrEntityGroup,
       "prvtLmgrMiscGroup": prvtLmgrMiscGroup}
)
