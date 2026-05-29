# SNMP MIB module (PRVT-TEMIB-ENTITY-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\telco-systems\binos\PRVT-TEMIB-ENTITY-MIB

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

(mpls,) = mibBuilder.importSymbols(
    "PRVT-CR-LDP-MIB",
    "mpls")

(PrvtLmgrIndex,
 PrvtLmgrPartnerStatus) = mibBuilder.importSymbols(
    "PRVT-LMGR-MIB",
    "PrvtLmgrIndex",
    "PrvtLmgrPartnerStatus")

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

prvtTeMibEntityMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 8)
)
if mibBuilder.loadTexts:
    prvtTeMibEntityMib.setRevisions(
        ("2007-12-06 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class PrvtTeMibAdminStatus(TextualConvention, Integer32):
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



class PrvtTeMibOperStatus(TextualConvention, Integer32):
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



class PrvtTeMibEntityIndex(TextualConvention, Unsigned32):
    status = "current"


class PrvtTeMibPartnerStatus(TextualConvention, Integer32):
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



# MIB Managed Objects in the order of their OIDs

_PrvtTeMibEntityObjects_ObjectIdentity = ObjectIdentity
prvtTeMibEntityObjects = _PrvtTeMibEntityObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 8, 1)
)
_PrvtMplsTeMibEntityTable_Object = MibTable
prvtMplsTeMibEntityTable = _PrvtMplsTeMibEntityTable_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 8, 1, 1)
)
if mibBuilder.loadTexts:
    prvtMplsTeMibEntityTable.setStatus("current")
_PrvtMplsTeMibEntityEntry_Object = MibTableRow
prvtMplsTeMibEntityEntry = _PrvtMplsTeMibEntityEntry_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 8, 1, 1, 1)
)
prvtMplsTeMibEntityEntry.setIndexNames(
    (0, "PRVT-TEMIB-ENTITY-MIB", "prvtMplsTeMibEntityIndex"),
)
if mibBuilder.loadTexts:
    prvtMplsTeMibEntityEntry.setStatus("current")
_PrvtMplsTeMibEntityIndex_Type = PrvtTeMibEntityIndex
_PrvtMplsTeMibEntityIndex_Object = MibTableColumn
prvtMplsTeMibEntityIndex = _PrvtMplsTeMibEntityIndex_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 8, 1, 1, 1, 1),
    _PrvtMplsTeMibEntityIndex_Type()
)
prvtMplsTeMibEntityIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    prvtMplsTeMibEntityIndex.setStatus("current")


class _PrvtMplsTeMibEntityAdminStatus_Type(PrvtTeMibAdminStatus):
    """Custom type prvtMplsTeMibEntityAdminStatus based on PrvtTeMibAdminStatus"""
    defaultValue = 1


_PrvtMplsTeMibEntityAdminStatus_Type.__name__ = "PrvtTeMibAdminStatus"
_PrvtMplsTeMibEntityAdminStatus_Object = MibTableColumn
prvtMplsTeMibEntityAdminStatus = _PrvtMplsTeMibEntityAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 8, 1, 1, 1, 2),
    _PrvtMplsTeMibEntityAdminStatus_Type()
)
prvtMplsTeMibEntityAdminStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    prvtMplsTeMibEntityAdminStatus.setStatus("current")
_PrvtMplsTeMibEntityOperStatus_Type = PrvtTeMibOperStatus
_PrvtMplsTeMibEntityOperStatus_Object = MibTableColumn
prvtMplsTeMibEntityOperStatus = _PrvtMplsTeMibEntityOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 8, 1, 1, 1, 3),
    _PrvtMplsTeMibEntityOperStatus_Type()
)
prvtMplsTeMibEntityOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtMplsTeMibEntityOperStatus.setStatus("current")
_PrvtMplsTeMibEntityRowStatus_Type = RowStatus
_PrvtMplsTeMibEntityRowStatus_Object = MibTableColumn
prvtMplsTeMibEntityRowStatus = _PrvtMplsTeMibEntityRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 8, 1, 1, 1, 4),
    _PrvtMplsTeMibEntityRowStatus_Type()
)
prvtMplsTeMibEntityRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    prvtMplsTeMibEntityRowStatus.setStatus("current")


class _PrvtMplsTeMibTunnelRetryInterval_Type(Unsigned32):
    """Custom type prvtMplsTeMibTunnelRetryInterval based on Unsigned32"""
    defaultValue = 3000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_PrvtMplsTeMibTunnelRetryInterval_Type.__name__ = "Unsigned32"
_PrvtMplsTeMibTunnelRetryInterval_Object = MibTableColumn
prvtMplsTeMibTunnelRetryInterval = _PrvtMplsTeMibTunnelRetryInterval_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 8, 1, 1, 1, 5),
    _PrvtMplsTeMibTunnelRetryInterval_Type()
)
prvtMplsTeMibTunnelRetryInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    prvtMplsTeMibTunnelRetryInterval.setStatus("current")
if mibBuilder.loadTexts:
    prvtMplsTeMibTunnelRetryInterval.setUnits("milliseconds")


class _PrvtMplsTeMibTunnelRetryDecayRate_Type(Unsigned32):
    """Custom type prvtMplsTeMibTunnelRetryDecayRate based on Unsigned32"""
    defaultValue = 50

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_PrvtMplsTeMibTunnelRetryDecayRate_Type.__name__ = "Unsigned32"
_PrvtMplsTeMibTunnelRetryDecayRate_Object = MibTableColumn
prvtMplsTeMibTunnelRetryDecayRate = _PrvtMplsTeMibTunnelRetryDecayRate_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 8, 1, 1, 1, 6),
    _PrvtMplsTeMibTunnelRetryDecayRate_Type()
)
prvtMplsTeMibTunnelRetryDecayRate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    prvtMplsTeMibTunnelRetryDecayRate.setStatus("current")


class _PrvtMplsTeMibTunnelRetryMax_Type(Integer32):
    """Custom type prvtMplsTeMibTunnelRetryMax based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 255),
    )


_PrvtMplsTeMibTunnelRetryMax_Type.__name__ = "Integer32"
_PrvtMplsTeMibTunnelRetryMax_Object = MibTableColumn
prvtMplsTeMibTunnelRetryMax = _PrvtMplsTeMibTunnelRetryMax_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 8, 1, 1, 1, 7),
    _PrvtMplsTeMibTunnelRetryMax_Type()
)
prvtMplsTeMibTunnelRetryMax.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    prvtMplsTeMibTunnelRetryMax.setStatus("current")


class _PrvtMplsTeMibTnnlBufPoolSize_Type(Unsigned32):
    """Custom type prvtMplsTeMibTnnlBufPoolSize based on Unsigned32"""
    defaultValue = 8

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_PrvtMplsTeMibTnnlBufPoolSize_Type.__name__ = "Unsigned32"
_PrvtMplsTeMibTnnlBufPoolSize_Object = MibTableColumn
prvtMplsTeMibTnnlBufPoolSize = _PrvtMplsTeMibTnnlBufPoolSize_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 8, 1, 1, 1, 8),
    _PrvtMplsTeMibTnnlBufPoolSize_Type()
)
prvtMplsTeMibTnnlBufPoolSize.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    prvtMplsTeMibTnnlBufPoolSize.setStatus("current")


class _PrvtMplsTeMibLsrIndex_Type(PrvtLmgrIndex):
    """Custom type prvtMplsTeMibLsrIndex based on PrvtLmgrIndex"""
    defaultValue = 0


_PrvtMplsTeMibLsrIndex_Type.__name__ = "PrvtLmgrIndex"
_PrvtMplsTeMibLsrIndex_Object = MibTableColumn
prvtMplsTeMibLsrIndex = _PrvtMplsTeMibLsrIndex_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 8, 1, 1, 1, 9),
    _PrvtMplsTeMibLsrIndex_Type()
)
prvtMplsTeMibLsrIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    prvtMplsTeMibLsrIndex.setStatus("current")
_PrvtMplsTeMibLdbStatus_Type = PrvtTeMibPartnerStatus
_PrvtMplsTeMibLdbStatus_Object = MibTableColumn
prvtMplsTeMibLdbStatus = _PrvtMplsTeMibLdbStatus_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 8, 1, 1, 1, 10),
    _PrvtMplsTeMibLdbStatus_Type()
)
prvtMplsTeMibLdbStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtMplsTeMibLdbStatus.setStatus("current")
_PrvtMplsTeMibLraStatus_Type = PrvtLmgrPartnerStatus
_PrvtMplsTeMibLraStatus_Object = MibTableColumn
prvtMplsTeMibLraStatus = _PrvtMplsTeMibLraStatus_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 8, 1, 1, 1, 11),
    _PrvtMplsTeMibLraStatus_Type()
)
prvtMplsTeMibLraStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtMplsTeMibLraStatus.setStatus("current")
_PrvtMplsTeMibLdiStatus_Type = PrvtTeMibPartnerStatus
_PrvtMplsTeMibLdiStatus_Object = MibTableColumn
prvtMplsTeMibLdiStatus = _PrvtMplsTeMibLdiStatus_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 8, 1, 1, 1, 12),
    _PrvtMplsTeMibLdiStatus_Type()
)
prvtMplsTeMibLdiStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtMplsTeMibLdiStatus.setStatus("current")


class _PrvtMplsTeMibRsvpEnable_Type(TruthValue):
    """Custom type prvtMplsTeMibRsvpEnable based on TruthValue"""
    defaultValue = 1


_PrvtMplsTeMibRsvpEnable_Type.__name__ = "TruthValue"
_PrvtMplsTeMibRsvpEnable_Object = MibTableColumn
prvtMplsTeMibRsvpEnable = _PrvtMplsTeMibRsvpEnable_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 8, 1, 1, 1, 13),
    _PrvtMplsTeMibRsvpEnable_Type()
)
prvtMplsTeMibRsvpEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    prvtMplsTeMibRsvpEnable.setStatus("current")


class _PrvtMplsTeMibCrldpEnable_Type(TruthValue):
    """Custom type prvtMplsTeMibCrldpEnable based on TruthValue"""
    defaultValue = 2


_PrvtMplsTeMibCrldpEnable_Type.__name__ = "TruthValue"
_PrvtMplsTeMibCrldpEnable_Object = MibTableColumn
prvtMplsTeMibCrldpEnable = _PrvtMplsTeMibCrldpEnable_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 8, 1, 1, 1, 14),
    _PrvtMplsTeMibCrldpEnable_Type()
)
prvtMplsTeMibCrldpEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    prvtMplsTeMibCrldpEnable.setStatus("current")


class _PrvtMplsTeMibCrldpIndex_Type(Unsigned32):
    """Custom type prvtMplsTeMibCrldpIndex based on Unsigned32"""
    defaultValue = 0


_PrvtMplsTeMibCrldpIndex_Type.__name__ = "Unsigned32"
_PrvtMplsTeMibCrldpIndex_Object = MibTableColumn
prvtMplsTeMibCrldpIndex = _PrvtMplsTeMibCrldpIndex_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 8, 1, 1, 1, 15),
    _PrvtMplsTeMibCrldpIndex_Type()
)
prvtMplsTeMibCrldpIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    prvtMplsTeMibCrldpIndex.setStatus("current")


class _PrvtMplsTeMibUseRsvpResvConf_Type(Bits):
    """Custom type prvtMplsTeMibUseRsvpResvConf based on Bits"""
    namedValues = NamedValues(
        *(("useResvConfForUNI", 0),
          ("useResvConfForGMPLS", 1))
    )

_PrvtMplsTeMibUseRsvpResvConf_Type.__name__ = "Bits"
_PrvtMplsTeMibUseRsvpResvConf_Object = MibTableColumn
prvtMplsTeMibUseRsvpResvConf = _PrvtMplsTeMibUseRsvpResvConf_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 8, 1, 1, 1, 16),
    _PrvtMplsTeMibUseRsvpResvConf_Type()
)
prvtMplsTeMibUseRsvpResvConf.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    prvtMplsTeMibUseRsvpResvConf.setStatus("current")


class _PrvtMplsTeMibAllowGracefulDeletion_Type(TruthValue):
    """Custom type prvtMplsTeMibAllowGracefulDeletion based on TruthValue"""
    defaultValue = 2


_PrvtMplsTeMibAllowGracefulDeletion_Type.__name__ = "TruthValue"
_PrvtMplsTeMibAllowGracefulDeletion_Object = MibTableColumn
prvtMplsTeMibAllowGracefulDeletion = _PrvtMplsTeMibAllowGracefulDeletion_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 8, 1, 1, 1, 17),
    _PrvtMplsTeMibAllowGracefulDeletion_Type()
)
prvtMplsTeMibAllowGracefulDeletion.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    prvtMplsTeMibAllowGracefulDeletion.setStatus("current")


class _PrvtMplsTeMibShowTransitTunnels_Type(TruthValue):
    """Custom type prvtMplsTeMibShowTransitTunnels based on TruthValue"""
    defaultValue = 2


_PrvtMplsTeMibShowTransitTunnels_Type.__name__ = "TruthValue"
_PrvtMplsTeMibShowTransitTunnels_Object = MibTableColumn
prvtMplsTeMibShowTransitTunnels = _PrvtMplsTeMibShowTransitTunnels_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 8, 1, 1, 1, 18),
    _PrvtMplsTeMibShowTransitTunnels_Type()
)
prvtMplsTeMibShowTransitTunnels.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    prvtMplsTeMibShowTransitTunnels.setStatus("current")


class _PrvtMplsTeMibSupportCHopTable_Type(TruthValue):
    """Custom type prvtMplsTeMibSupportCHopTable based on TruthValue"""
    defaultValue = 2


_PrvtMplsTeMibSupportCHopTable_Type.__name__ = "TruthValue"
_PrvtMplsTeMibSupportCHopTable_Object = MibTableColumn
prvtMplsTeMibSupportCHopTable = _PrvtMplsTeMibSupportCHopTable_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 8, 1, 1, 1, 19),
    _PrvtMplsTeMibSupportCHopTable_Type()
)
prvtMplsTeMibSupportCHopTable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    prvtMplsTeMibSupportCHopTable.setStatus("current")


class _PrvtMplsTeMibNhrIndex_Type(Unsigned32):
    """Custom type prvtMplsTeMibNhrIndex based on Unsigned32"""
    defaultValue = 0


_PrvtMplsTeMibNhrIndex_Type.__name__ = "Unsigned32"
_PrvtMplsTeMibNhrIndex_Object = MibTableColumn
prvtMplsTeMibNhrIndex = _PrvtMplsTeMibNhrIndex_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 8, 1, 1, 1, 20),
    _PrvtMplsTeMibNhrIndex_Type()
)
prvtMplsTeMibNhrIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    prvtMplsTeMibNhrIndex.setStatus("current")


class _PrvtMplsTeMibNhrBufPoolSize_Type(Unsigned32):
    """Custom type prvtMplsTeMibNhrBufPoolSize based on Unsigned32"""
    defaultValue = 8

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_PrvtMplsTeMibNhrBufPoolSize_Type.__name__ = "Unsigned32"
_PrvtMplsTeMibNhrBufPoolSize_Object = MibTableColumn
prvtMplsTeMibNhrBufPoolSize = _PrvtMplsTeMibNhrBufPoolSize_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 8, 1, 1, 1, 21),
    _PrvtMplsTeMibNhrBufPoolSize_Type()
)
prvtMplsTeMibNhrBufPoolSize.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    prvtMplsTeMibNhrBufPoolSize.setStatus("current")
_PrvtMplsTeMibNhrStatus_Type = PrvtTeMibPartnerStatus
_PrvtMplsTeMibNhrStatus_Object = MibTableColumn
prvtMplsTeMibNhrStatus = _PrvtMplsTeMibNhrStatus_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 8, 1, 1, 1, 22),
    _PrvtMplsTeMibNhrStatus_Type()
)
prvtMplsTeMibNhrStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtMplsTeMibNhrStatus.setStatus("current")


class _PrvtMplsTeMibExtPrtSuppAdminStatus_Type(PrvtTeMibAdminStatus):
    """Custom type prvtMplsTeMibExtPrtSuppAdminStatus based on PrvtTeMibAdminStatus"""
    defaultValue = 2


_PrvtMplsTeMibExtPrtSuppAdminStatus_Type.__name__ = "PrvtTeMibAdminStatus"
_PrvtMplsTeMibExtPrtSuppAdminStatus_Object = MibTableColumn
prvtMplsTeMibExtPrtSuppAdminStatus = _PrvtMplsTeMibExtPrtSuppAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 8, 1, 1, 1, 23),
    _PrvtMplsTeMibExtPrtSuppAdminStatus_Type()
)
prvtMplsTeMibExtPrtSuppAdminStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    prvtMplsTeMibExtPrtSuppAdminStatus.setStatus("current")


class _PrvtMplsTeMibRsvpIpv6AdminStatus_Type(PrvtTeMibAdminStatus):
    """Custom type prvtMplsTeMibRsvpIpv6AdminStatus based on PrvtTeMibAdminStatus"""
    defaultValue = 2


_PrvtMplsTeMibRsvpIpv6AdminStatus_Type.__name__ = "PrvtTeMibAdminStatus"
_PrvtMplsTeMibRsvpIpv6AdminStatus_Object = MibTableColumn
prvtMplsTeMibRsvpIpv6AdminStatus = _PrvtMplsTeMibRsvpIpv6AdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 8, 1, 1, 1, 24),
    _PrvtMplsTeMibRsvpIpv6AdminStatus_Type()
)
prvtMplsTeMibRsvpIpv6AdminStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    prvtMplsTeMibRsvpIpv6AdminStatus.setStatus("current")
_PrvtMplsTeMibRsvpIpv6OperStatus_Type = PrvtTeMibOperStatus
_PrvtMplsTeMibRsvpIpv6OperStatus_Object = MibTableColumn
prvtMplsTeMibRsvpIpv6OperStatus = _PrvtMplsTeMibRsvpIpv6OperStatus_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 8, 1, 1, 1, 25),
    _PrvtMplsTeMibRsvpIpv6OperStatus_Type()
)
prvtMplsTeMibRsvpIpv6OperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtMplsTeMibRsvpIpv6OperStatus.setStatus("current")


class _PrvtMplsTeMibDynFacilityBypass_Type(TruthValue):
    """Custom type prvtMplsTeMibDynFacilityBypass based on TruthValue"""
    defaultValue = 1


_PrvtMplsTeMibDynFacilityBypass_Type.__name__ = "TruthValue"
_PrvtMplsTeMibDynFacilityBypass_Object = MibTableColumn
prvtMplsTeMibDynFacilityBypass = _PrvtMplsTeMibDynFacilityBypass_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 8, 1, 1, 1, 26),
    _PrvtMplsTeMibDynFacilityBypass_Type()
)
prvtMplsTeMibDynFacilityBypass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prvtMplsTeMibDynFacilityBypass.setStatus("current")
_PrvtTeMibEntityConformance_ObjectIdentity = ObjectIdentity
prvtTeMibEntityConformance = _PrvtTeMibEntityConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 8, 2)
)
_PrvtTeMibEntityCompliances_ObjectIdentity = ObjectIdentity
prvtTeMibEntityCompliances = _PrvtTeMibEntityCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 8, 2, 1)
)
_PrvtTeMibEntityGroups_ObjectIdentity = ObjectIdentity
prvtTeMibEntityGroups = _PrvtTeMibEntityGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 8, 2, 2)
)

# Managed Objects groups

mplsTeMibMandatoryGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 8, 2, 2, 2)
)
mplsTeMibMandatoryGroup.setObjects(
    ("PRVT-TEMIB-ENTITY-MIB", "prvtMplsTeMibEntityRowStatus")
)
if mibBuilder.loadTexts:
    mplsTeMibMandatoryGroup.setStatus("current")

mplsTeMibOptionalGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 8, 2, 2, 3)
)
mplsTeMibOptionalGroup.setObjects(
      *(("PRVT-TEMIB-ENTITY-MIB", "prvtMplsTeMibEntityAdminStatus"),
        ("PRVT-TEMIB-ENTITY-MIB", "prvtMplsTeMibEntityOperStatus"),
        ("PRVT-TEMIB-ENTITY-MIB", "prvtMplsTeMibTunnelRetryInterval"),
        ("PRVT-TEMIB-ENTITY-MIB", "prvtMplsTeMibTunnelRetryDecayRate"),
        ("PRVT-TEMIB-ENTITY-MIB", "prvtMplsTeMibTunnelRetryMax"),
        ("PRVT-TEMIB-ENTITY-MIB", "prvtMplsTeMibTnnlBufPoolSize"),
        ("PRVT-TEMIB-ENTITY-MIB", "prvtMplsTeMibLsrIndex"),
        ("PRVT-TEMIB-ENTITY-MIB", "prvtMplsTeMibLdbStatus"),
        ("PRVT-TEMIB-ENTITY-MIB", "prvtMplsTeMibLraStatus"),
        ("PRVT-TEMIB-ENTITY-MIB", "prvtMplsTeMibRsvpEnable"),
        ("PRVT-TEMIB-ENTITY-MIB", "prvtMplsTeMibUseRsvpResvConf"),
        ("PRVT-TEMIB-ENTITY-MIB", "prvtMplsTeMibAllowGracefulDeletion"),
        ("PRVT-TEMIB-ENTITY-MIB", "prvtMplsTeMibShowTransitTunnels"),
        ("PRVT-TEMIB-ENTITY-MIB", "prvtMplsTeMibSupportCHopTable"),
        ("PRVT-TEMIB-ENTITY-MIB", "prvtMplsTeMibNhrIndex"),
        ("PRVT-TEMIB-ENTITY-MIB", "prvtMplsTeMibNhrBufPoolSize"),
        ("PRVT-TEMIB-ENTITY-MIB", "prvtMplsTeMibNhrStatus"),
        ("PRVT-TEMIB-ENTITY-MIB", "prvtMplsTeMibExtPrtSuppAdminStatus"),
        ("PRVT-TEMIB-ENTITY-MIB", "prvtMplsTeMibRsvpIpv6AdminStatus"),
        ("PRVT-TEMIB-ENTITY-MIB", "prvtMplsTeMibRsvpIpv6OperStatus"),
        ("PRVT-TEMIB-ENTITY-MIB", "prvtMplsTeMibDynFacilityBypass"))
)
if mibBuilder.loadTexts:
    mplsTeMibOptionalGroup.setStatus("current")

mplsTeMibCrldpGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 8, 2, 2, 4)
)
mplsTeMibCrldpGroup.setObjects(
      *(("PRVT-TEMIB-ENTITY-MIB", "prvtMplsTeMibLdiStatus"),
        ("PRVT-TEMIB-ENTITY-MIB", "prvtMplsTeMibCrldpEnable"),
        ("PRVT-TEMIB-ENTITY-MIB", "prvtMplsTeMibCrldpIndex"))
)
if mibBuilder.loadTexts:
    mplsTeMibCrldpGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

prvtTeMibEntityMibCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 8, 2, 1, 1)
)
prvtTeMibEntityMibCompliance.setObjects(
      *(("PRVT-TEMIB-ENTITY-MIB", "mplsTeMibMandatoryGroup"),
        ("PRVT-TEMIB-ENTITY-MIB", "mplsTeMibOptionalGroup"),
        ("PRVT-TEMIB-ENTITY-MIB", "mplsTeMibCrldpGroup"))
)
if mibBuilder.loadTexts:
    prvtTeMibEntityMibCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "PRVT-TEMIB-ENTITY-MIB",
    **{"PrvtTeMibAdminStatus": PrvtTeMibAdminStatus,
       "PrvtTeMibOperStatus": PrvtTeMibOperStatus,
       "PrvtTeMibEntityIndex": PrvtTeMibEntityIndex,
       "PrvtTeMibPartnerStatus": PrvtTeMibPartnerStatus,
       "prvtTeMibEntityMib": prvtTeMibEntityMib,
       "prvtTeMibEntityObjects": prvtTeMibEntityObjects,
       "prvtMplsTeMibEntityTable": prvtMplsTeMibEntityTable,
       "prvtMplsTeMibEntityEntry": prvtMplsTeMibEntityEntry,
       "prvtMplsTeMibEntityIndex": prvtMplsTeMibEntityIndex,
       "prvtMplsTeMibEntityAdminStatus": prvtMplsTeMibEntityAdminStatus,
       "prvtMplsTeMibEntityOperStatus": prvtMplsTeMibEntityOperStatus,
       "prvtMplsTeMibEntityRowStatus": prvtMplsTeMibEntityRowStatus,
       "prvtMplsTeMibTunnelRetryInterval": prvtMplsTeMibTunnelRetryInterval,
       "prvtMplsTeMibTunnelRetryDecayRate": prvtMplsTeMibTunnelRetryDecayRate,
       "prvtMplsTeMibTunnelRetryMax": prvtMplsTeMibTunnelRetryMax,
       "prvtMplsTeMibTnnlBufPoolSize": prvtMplsTeMibTnnlBufPoolSize,
       "prvtMplsTeMibLsrIndex": prvtMplsTeMibLsrIndex,
       "prvtMplsTeMibLdbStatus": prvtMplsTeMibLdbStatus,
       "prvtMplsTeMibLraStatus": prvtMplsTeMibLraStatus,
       "prvtMplsTeMibLdiStatus": prvtMplsTeMibLdiStatus,
       "prvtMplsTeMibRsvpEnable": prvtMplsTeMibRsvpEnable,
       "prvtMplsTeMibCrldpEnable": prvtMplsTeMibCrldpEnable,
       "prvtMplsTeMibCrldpIndex": prvtMplsTeMibCrldpIndex,
       "prvtMplsTeMibUseRsvpResvConf": prvtMplsTeMibUseRsvpResvConf,
       "prvtMplsTeMibAllowGracefulDeletion": prvtMplsTeMibAllowGracefulDeletion,
       "prvtMplsTeMibShowTransitTunnels": prvtMplsTeMibShowTransitTunnels,
       "prvtMplsTeMibSupportCHopTable": prvtMplsTeMibSupportCHopTable,
       "prvtMplsTeMibNhrIndex": prvtMplsTeMibNhrIndex,
       "prvtMplsTeMibNhrBufPoolSize": prvtMplsTeMibNhrBufPoolSize,
       "prvtMplsTeMibNhrStatus": prvtMplsTeMibNhrStatus,
       "prvtMplsTeMibExtPrtSuppAdminStatus": prvtMplsTeMibExtPrtSuppAdminStatus,
       "prvtMplsTeMibRsvpIpv6AdminStatus": prvtMplsTeMibRsvpIpv6AdminStatus,
       "prvtMplsTeMibRsvpIpv6OperStatus": prvtMplsTeMibRsvpIpv6OperStatus,
       "prvtMplsTeMibDynFacilityBypass": prvtMplsTeMibDynFacilityBypass,
       "prvtTeMibEntityConformance": prvtTeMibEntityConformance,
       "prvtTeMibEntityCompliances": prvtTeMibEntityCompliances,
       "prvtTeMibEntityMibCompliance": prvtTeMibEntityMibCompliance,
       "prvtTeMibEntityGroups": prvtTeMibEntityGroups,
       "mplsTeMibMandatoryGroup": mplsTeMibMandatoryGroup,
       "mplsTeMibOptionalGroup": mplsTeMibOptionalGroup,
       "mplsTeMibCrldpGroup": mplsTeMibCrldpGroup}
)
