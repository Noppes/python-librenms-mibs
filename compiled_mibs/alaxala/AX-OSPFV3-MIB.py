# SNMP MIB module (AX-OSPFV3-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\alaxala\AX-OSPFV3-MIB

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

(axMib,) = mibBuilder.importSymbols(
    "AX-SMI-MIB",
    "axMib")

(InterfaceIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex")

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

(Status,) = mibBuilder.importSymbols(
    "OSPF-MIB",
    "Status")

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

axOspfv3 = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 15)
)
if mibBuilder.loadTexts:
    axOspfv3.setRevisions(
        ("2013-10-03 00:00",
         "2013-06-28 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AxOspfv3GeneralTable_Object = MibTable
axOspfv3GeneralTable = _AxOspfv3GeneralTable_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 15, 1)
)
if mibBuilder.loadTexts:
    axOspfv3GeneralTable.setStatus("current")
_AxOspfv3GeneralEntry_Object = MibTableRow
axOspfv3GeneralEntry = _AxOspfv3GeneralEntry_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 15, 1, 1)
)
axOspfv3GeneralEntry.setIndexNames(
    (0, "AX-OSPFV3-MIB", "axOspfv3GeneralDomainNumber"),
)
if mibBuilder.loadTexts:
    axOspfv3GeneralEntry.setStatus("current")
_AxOspfv3GeneralDomainNumber_Type = Integer32
_AxOspfv3GeneralDomainNumber_Object = MibTableColumn
axOspfv3GeneralDomainNumber = _AxOspfv3GeneralDomainNumber_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 15, 1, 1, 1),
    _AxOspfv3GeneralDomainNumber_Type()
)
axOspfv3GeneralDomainNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axOspfv3GeneralDomainNumber.setStatus("current")
_AxOspfv3RouterId_Type = Unsigned32
_AxOspfv3RouterId_Object = MibTableColumn
axOspfv3RouterId = _AxOspfv3RouterId_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 15, 1, 1, 2),
    _AxOspfv3RouterId_Type()
)
axOspfv3RouterId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axOspfv3RouterId.setStatus("current")
_AxOspfv3AdminStatus_Type = Status
_AxOspfv3AdminStatus_Object = MibTableColumn
axOspfv3AdminStatus = _AxOspfv3AdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 15, 1, 1, 3),
    _AxOspfv3AdminStatus_Type()
)
axOspfv3AdminStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axOspfv3AdminStatus.setStatus("current")


class _AxOspfv3VersionNumber_Type(Integer32):
    """Custom type axOspfv3VersionNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            3
        )
    )
    namedValues = NamedValues(
        ("version3", 3)
    )


_AxOspfv3VersionNumber_Type.__name__ = "Integer32"
_AxOspfv3VersionNumber_Object = MibTableColumn
axOspfv3VersionNumber = _AxOspfv3VersionNumber_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 15, 1, 1, 4),
    _AxOspfv3VersionNumber_Type()
)
axOspfv3VersionNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axOspfv3VersionNumber.setStatus("current")
_AxOspfv3AreaBdrRtrStatus_Type = TruthValue
_AxOspfv3AreaBdrRtrStatus_Object = MibTableColumn
axOspfv3AreaBdrRtrStatus = _AxOspfv3AreaBdrRtrStatus_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 15, 1, 1, 5),
    _AxOspfv3AreaBdrRtrStatus_Type()
)
axOspfv3AreaBdrRtrStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axOspfv3AreaBdrRtrStatus.setStatus("current")
_AxOspfv3ASBdrRtrStatus_Type = TruthValue
_AxOspfv3ASBdrRtrStatus_Object = MibTableColumn
axOspfv3ASBdrRtrStatus = _AxOspfv3ASBdrRtrStatus_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 15, 1, 1, 6),
    _AxOspfv3ASBdrRtrStatus_Type()
)
axOspfv3ASBdrRtrStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axOspfv3ASBdrRtrStatus.setStatus("current")
_AxOspfv3AsScopeLsaCount_Type = Gauge32
_AxOspfv3AsScopeLsaCount_Object = MibTableColumn
axOspfv3AsScopeLsaCount = _AxOspfv3AsScopeLsaCount_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 15, 1, 1, 7),
    _AxOspfv3AsScopeLsaCount_Type()
)
axOspfv3AsScopeLsaCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axOspfv3AsScopeLsaCount.setStatus("current")
_AxOspfv3AsScopeLsaCksumSum_Type = Integer32
_AxOspfv3AsScopeLsaCksumSum_Object = MibTableColumn
axOspfv3AsScopeLsaCksumSum = _AxOspfv3AsScopeLsaCksumSum_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 15, 1, 1, 8),
    _AxOspfv3AsScopeLsaCksumSum_Type()
)
axOspfv3AsScopeLsaCksumSum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axOspfv3AsScopeLsaCksumSum.setStatus("current")
_AxOspfv3OriginateNewLsas_Type = Counter32
_AxOspfv3OriginateNewLsas_Object = MibTableColumn
axOspfv3OriginateNewLsas = _AxOspfv3OriginateNewLsas_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 15, 1, 1, 9),
    _AxOspfv3OriginateNewLsas_Type()
)
axOspfv3OriginateNewLsas.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axOspfv3OriginateNewLsas.setStatus("current")
_AxOspfv3RxNewLsas_Type = Counter32
_AxOspfv3RxNewLsas_Object = MibTableColumn
axOspfv3RxNewLsas = _AxOspfv3RxNewLsas_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 15, 1, 1, 10),
    _AxOspfv3RxNewLsas_Type()
)
axOspfv3RxNewLsas.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axOspfv3RxNewLsas.setStatus("current")
_AxOspfv3ExtLsaCount_Type = Gauge32
_AxOspfv3ExtLsaCount_Object = MibTableColumn
axOspfv3ExtLsaCount = _AxOspfv3ExtLsaCount_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 15, 1, 1, 11),
    _AxOspfv3ExtLsaCount_Type()
)
axOspfv3ExtLsaCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axOspfv3ExtLsaCount.setStatus("current")
_AxOspfv3ExtAreaLsdbLimit_Type = Integer32
_AxOspfv3ExtAreaLsdbLimit_Object = MibTableColumn
axOspfv3ExtAreaLsdbLimit = _AxOspfv3ExtAreaLsdbLimit_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 15, 1, 1, 12),
    _AxOspfv3ExtAreaLsdbLimit_Type()
)
axOspfv3ExtAreaLsdbLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axOspfv3ExtAreaLsdbLimit.setStatus("current")
_AxOspfv3DemandExtensions_Type = TruthValue
_AxOspfv3DemandExtensions_Object = MibTableColumn
axOspfv3DemandExtensions = _AxOspfv3DemandExtensions_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 15, 1, 1, 14),
    _AxOspfv3DemandExtensions_Type()
)
axOspfv3DemandExtensions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axOspfv3DemandExtensions.setStatus("current")


class _AxOspfv3RestartSupport_Type(Integer32):
    """Custom type axOspfv3RestartSupport based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("plannedOnly", 2),
          ("plannedAndUnplanned", 3))
    )


_AxOspfv3RestartSupport_Type.__name__ = "Integer32"
_AxOspfv3RestartSupport_Object = MibTableColumn
axOspfv3RestartSupport = _AxOspfv3RestartSupport_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 15, 1, 1, 16),
    _AxOspfv3RestartSupport_Type()
)
axOspfv3RestartSupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axOspfv3RestartSupport.setStatus("current")
_AxOspfv3RestartInterval_Type = Unsigned32
_AxOspfv3RestartInterval_Object = MibTableColumn
axOspfv3RestartInterval = _AxOspfv3RestartInterval_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 15, 1, 1, 17),
    _AxOspfv3RestartInterval_Type()
)
axOspfv3RestartInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axOspfv3RestartInterval.setStatus("current")
_AxOspfv3RestartStrictLsaChecking_Type = TruthValue
_AxOspfv3RestartStrictLsaChecking_Object = MibTableColumn
axOspfv3RestartStrictLsaChecking = _AxOspfv3RestartStrictLsaChecking_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 15, 1, 1, 18),
    _AxOspfv3RestartStrictLsaChecking_Type()
)
axOspfv3RestartStrictLsaChecking.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axOspfv3RestartStrictLsaChecking.setStatus("current")
_AxOspfv3AreaTable_Object = MibTable
axOspfv3AreaTable = _AxOspfv3AreaTable_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 15, 2)
)
if mibBuilder.loadTexts:
    axOspfv3AreaTable.setStatus("current")
_AxOspfv3AreaEntry_Object = MibTableRow
axOspfv3AreaEntry = _AxOspfv3AreaEntry_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 15, 2, 1)
)
axOspfv3AreaEntry.setIndexNames(
    (0, "AX-OSPFV3-MIB", "axOspfv3AreaDomainNumber"),
    (0, "AX-OSPFV3-MIB", "axOspfv3AreaId"),
)
if mibBuilder.loadTexts:
    axOspfv3AreaEntry.setStatus("current")
_AxOspfv3AreaDomainNumber_Type = Integer32
_AxOspfv3AreaDomainNumber_Object = MibTableColumn
axOspfv3AreaDomainNumber = _AxOspfv3AreaDomainNumber_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 15, 2, 1, 1),
    _AxOspfv3AreaDomainNumber_Type()
)
axOspfv3AreaDomainNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    axOspfv3AreaDomainNumber.setStatus("current")
_AxOspfv3AreaId_Type = Unsigned32
_AxOspfv3AreaId_Object = MibTableColumn
axOspfv3AreaId = _AxOspfv3AreaId_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 15, 2, 1, 2),
    _AxOspfv3AreaId_Type()
)
axOspfv3AreaId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    axOspfv3AreaId.setStatus("current")


class _AxOspfv3AreaImportAsExtern_Type(Integer32):
    """Custom type axOspfv3AreaImportAsExtern based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("importExternal", 1),
          ("importNoExternal", 2),
          ("importNssa", 3))
    )


_AxOspfv3AreaImportAsExtern_Type.__name__ = "Integer32"
_AxOspfv3AreaImportAsExtern_Object = MibTableColumn
axOspfv3AreaImportAsExtern = _AxOspfv3AreaImportAsExtern_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 15, 2, 1, 3),
    _AxOspfv3AreaImportAsExtern_Type()
)
axOspfv3AreaImportAsExtern.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axOspfv3AreaImportAsExtern.setStatus("current")
_AxOspfv3AreaSpfRuns_Type = Counter32
_AxOspfv3AreaSpfRuns_Object = MibTableColumn
axOspfv3AreaSpfRuns = _AxOspfv3AreaSpfRuns_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 15, 2, 1, 4),
    _AxOspfv3AreaSpfRuns_Type()
)
axOspfv3AreaSpfRuns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axOspfv3AreaSpfRuns.setStatus("current")
_AxOspfv3AreaBdrRtrCount_Type = Gauge32
_AxOspfv3AreaBdrRtrCount_Object = MibTableColumn
axOspfv3AreaBdrRtrCount = _AxOspfv3AreaBdrRtrCount_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 15, 2, 1, 5),
    _AxOspfv3AreaBdrRtrCount_Type()
)
axOspfv3AreaBdrRtrCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axOspfv3AreaBdrRtrCount.setStatus("current")
_AxOspfv3AreaAsBdrRtrCount_Type = Gauge32
_AxOspfv3AreaAsBdrRtrCount_Object = MibTableColumn
axOspfv3AreaAsBdrRtrCount = _AxOspfv3AreaAsBdrRtrCount_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 15, 2, 1, 6),
    _AxOspfv3AreaAsBdrRtrCount_Type()
)
axOspfv3AreaAsBdrRtrCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axOspfv3AreaAsBdrRtrCount.setStatus("current")
_AxOspfv3AreaScopeLsaCount_Type = Gauge32
_AxOspfv3AreaScopeLsaCount_Object = MibTableColumn
axOspfv3AreaScopeLsaCount = _AxOspfv3AreaScopeLsaCount_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 15, 2, 1, 7),
    _AxOspfv3AreaScopeLsaCount_Type()
)
axOspfv3AreaScopeLsaCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axOspfv3AreaScopeLsaCount.setStatus("current")
_AxOspfv3AreaScopeLsaCksumSum_Type = Unsigned32
_AxOspfv3AreaScopeLsaCksumSum_Object = MibTableColumn
axOspfv3AreaScopeLsaCksumSum = _AxOspfv3AreaScopeLsaCksumSum_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 15, 2, 1, 8),
    _AxOspfv3AreaScopeLsaCksumSum_Type()
)
axOspfv3AreaScopeLsaCksumSum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axOspfv3AreaScopeLsaCksumSum.setStatus("current")


class _AxOspfv3AreaSummary_Type(Integer32):
    """Custom type axOspfv3AreaSummary based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noAreaSummary", 1),
          ("sendAreaSummary", 2))
    )


_AxOspfv3AreaSummary_Type.__name__ = "Integer32"
_AxOspfv3AreaSummary_Object = MibTableColumn
axOspfv3AreaSummary = _AxOspfv3AreaSummary_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 15, 2, 1, 9),
    _AxOspfv3AreaSummary_Type()
)
axOspfv3AreaSummary.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axOspfv3AreaSummary.setStatus("current")
_AxOspfv3AreaRowStatus_Type = RowStatus
_AxOspfv3AreaRowStatus_Object = MibTableColumn
axOspfv3AreaRowStatus = _AxOspfv3AreaRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 15, 2, 1, 10),
    _AxOspfv3AreaRowStatus_Type()
)
axOspfv3AreaRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    axOspfv3AreaRowStatus.setStatus("current")
_AxOspfv3AreaStubMetric_Type = Integer32
_AxOspfv3AreaStubMetric_Object = MibTableColumn
axOspfv3AreaStubMetric = _AxOspfv3AreaStubMetric_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 15, 2, 1, 11),
    _AxOspfv3AreaStubMetric_Type()
)
axOspfv3AreaStubMetric.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axOspfv3AreaStubMetric.setStatus("current")


class _AxOspfv3AreaStubMetricType_Type(Integer32):
    """Custom type axOspfv3AreaStubMetricType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("ospfv3Metric", 1),
          ("comparableCost", 2),
          ("nonComparable", 3))
    )


_AxOspfv3AreaStubMetricType_Type.__name__ = "Integer32"
_AxOspfv3AreaStubMetricType_Object = MibTableColumn
axOspfv3AreaStubMetricType = _AxOspfv3AreaStubMetricType_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 15, 2, 1, 16),
    _AxOspfv3AreaStubMetricType_Type()
)
axOspfv3AreaStubMetricType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axOspfv3AreaStubMetricType.setStatus("current")
_AxOspfv3AreaTEEnabled_Type = TruthValue
_AxOspfv3AreaTEEnabled_Object = MibTableColumn
axOspfv3AreaTEEnabled = _AxOspfv3AreaTEEnabled_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 15, 2, 1, 17),
    _AxOspfv3AreaTEEnabled_Type()
)
axOspfv3AreaTEEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axOspfv3AreaTEEnabled.setStatus("current")
_AxOspfv3AsLsdbTable_Object = MibTable
axOspfv3AsLsdbTable = _AxOspfv3AsLsdbTable_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 15, 3)
)
if mibBuilder.loadTexts:
    axOspfv3AsLsdbTable.setStatus("current")
_AxOspfv3AsLsdbEntry_Object = MibTableRow
axOspfv3AsLsdbEntry = _AxOspfv3AsLsdbEntry_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 15, 3, 1)
)
axOspfv3AsLsdbEntry.setIndexNames(
    (0, "AX-OSPFV3-MIB", "axOspfv3AsLsdbDomainNumber"),
    (0, "AX-OSPFV3-MIB", "axOspfv3AsLsdbType"),
    (0, "AX-OSPFV3-MIB", "axOspfv3AsLsdbRouterId"),
    (0, "AX-OSPFV3-MIB", "axOspfv3AsLsdbLsid"),
)
if mibBuilder.loadTexts:
    axOspfv3AsLsdbEntry.setStatus("current")
_AxOspfv3AsLsdbDomainNumber_Type = Integer32
_AxOspfv3AsLsdbDomainNumber_Object = MibTableColumn
axOspfv3AsLsdbDomainNumber = _AxOspfv3AsLsdbDomainNumber_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 15, 3, 1, 1),
    _AxOspfv3AsLsdbDomainNumber_Type()
)
axOspfv3AsLsdbDomainNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    axOspfv3AsLsdbDomainNumber.setStatus("current")
_AxOspfv3AsLsdbType_Type = Unsigned32
_AxOspfv3AsLsdbType_Object = MibTableColumn
axOspfv3AsLsdbType = _AxOspfv3AsLsdbType_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 15, 3, 1, 2),
    _AxOspfv3AsLsdbType_Type()
)
axOspfv3AsLsdbType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    axOspfv3AsLsdbType.setStatus("current")
_AxOspfv3AsLsdbRouterId_Type = Unsigned32
_AxOspfv3AsLsdbRouterId_Object = MibTableColumn
axOspfv3AsLsdbRouterId = _AxOspfv3AsLsdbRouterId_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 15, 3, 1, 3),
    _AxOspfv3AsLsdbRouterId_Type()
)
axOspfv3AsLsdbRouterId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    axOspfv3AsLsdbRouterId.setStatus("current")
_AxOspfv3AsLsdbLsid_Type = Unsigned32
_AxOspfv3AsLsdbLsid_Object = MibTableColumn
axOspfv3AsLsdbLsid = _AxOspfv3AsLsdbLsid_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 15, 3, 1, 4),
    _AxOspfv3AsLsdbLsid_Type()
)
axOspfv3AsLsdbLsid.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    axOspfv3AsLsdbLsid.setStatus("current")
_AxOspfv3AsLsdbSequence_Type = Integer32
_AxOspfv3AsLsdbSequence_Object = MibTableColumn
axOspfv3AsLsdbSequence = _AxOspfv3AsLsdbSequence_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 15, 3, 1, 5),
    _AxOspfv3AsLsdbSequence_Type()
)
axOspfv3AsLsdbSequence.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axOspfv3AsLsdbSequence.setStatus("current")
_AxOspfv3AsLsdbAge_Type = Unsigned32
_AxOspfv3AsLsdbAge_Object = MibTableColumn
axOspfv3AsLsdbAge = _AxOspfv3AsLsdbAge_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 15, 3, 1, 6),
    _AxOspfv3AsLsdbAge_Type()
)
axOspfv3AsLsdbAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axOspfv3AsLsdbAge.setStatus("current")
_AxOspfv3AsLsdbChecksum_Type = Integer32
_AxOspfv3AsLsdbChecksum_Object = MibTableColumn
axOspfv3AsLsdbChecksum = _AxOspfv3AsLsdbChecksum_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 15, 3, 1, 7),
    _AxOspfv3AsLsdbChecksum_Type()
)
axOspfv3AsLsdbChecksum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axOspfv3AsLsdbChecksum.setStatus("current")


class _AxOspfv3AsLsdbAdvertisement_Type(OctetString):
    """Custom type axOspfv3AsLsdbAdvertisement based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 65535),
    )


_AxOspfv3AsLsdbAdvertisement_Type.__name__ = "OctetString"
_AxOspfv3AsLsdbAdvertisement_Object = MibTableColumn
axOspfv3AsLsdbAdvertisement = _AxOspfv3AsLsdbAdvertisement_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 15, 3, 1, 8),
    _AxOspfv3AsLsdbAdvertisement_Type()
)
axOspfv3AsLsdbAdvertisement.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axOspfv3AsLsdbAdvertisement.setStatus("current")
_AxOspfv3AreaLsdbTable_Object = MibTable
axOspfv3AreaLsdbTable = _AxOspfv3AreaLsdbTable_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 15, 4)
)
if mibBuilder.loadTexts:
    axOspfv3AreaLsdbTable.setStatus("current")
_AxOspfv3AreaLsdbEntry_Object = MibTableRow
axOspfv3AreaLsdbEntry = _AxOspfv3AreaLsdbEntry_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 15, 4, 1)
)
axOspfv3AreaLsdbEntry.setIndexNames(
    (0, "AX-OSPFV3-MIB", "axOspfv3AreaLsdbDomainNumber"),
    (0, "AX-OSPFV3-MIB", "axOspfv3AreaLsdbAreaId"),
    (0, "AX-OSPFV3-MIB", "axOspfv3AreaLsdbType"),
    (0, "AX-OSPFV3-MIB", "axOspfv3AreaLsdbRouterId"),
    (0, "AX-OSPFV3-MIB", "axOspfv3AreaLsdbLsid"),
)
if mibBuilder.loadTexts:
    axOspfv3AreaLsdbEntry.setStatus("current")
_AxOspfv3AreaLsdbDomainNumber_Type = Integer32
_AxOspfv3AreaLsdbDomainNumber_Object = MibTableColumn
axOspfv3AreaLsdbDomainNumber = _AxOspfv3AreaLsdbDomainNumber_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 15, 4, 1, 1),
    _AxOspfv3AreaLsdbDomainNumber_Type()
)
axOspfv3AreaLsdbDomainNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    axOspfv3AreaLsdbDomainNumber.setStatus("current")
_AxOspfv3AreaLsdbAreaId_Type = Unsigned32
_AxOspfv3AreaLsdbAreaId_Object = MibTableColumn
axOspfv3AreaLsdbAreaId = _AxOspfv3AreaLsdbAreaId_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 15, 4, 1, 2),
    _AxOspfv3AreaLsdbAreaId_Type()
)
axOspfv3AreaLsdbAreaId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    axOspfv3AreaLsdbAreaId.setStatus("current")
_AxOspfv3AreaLsdbType_Type = Unsigned32
_AxOspfv3AreaLsdbType_Object = MibTableColumn
axOspfv3AreaLsdbType = _AxOspfv3AreaLsdbType_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 15, 4, 1, 3),
    _AxOspfv3AreaLsdbType_Type()
)
axOspfv3AreaLsdbType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    axOspfv3AreaLsdbType.setStatus("current")
_AxOspfv3AreaLsdbRouterId_Type = Unsigned32
_AxOspfv3AreaLsdbRouterId_Object = MibTableColumn
axOspfv3AreaLsdbRouterId = _AxOspfv3AreaLsdbRouterId_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 15, 4, 1, 4),
    _AxOspfv3AreaLsdbRouterId_Type()
)
axOspfv3AreaLsdbRouterId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    axOspfv3AreaLsdbRouterId.setStatus("current")
_AxOspfv3AreaLsdbLsid_Type = Unsigned32
_AxOspfv3AreaLsdbLsid_Object = MibTableColumn
axOspfv3AreaLsdbLsid = _AxOspfv3AreaLsdbLsid_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 15, 4, 1, 5),
    _AxOspfv3AreaLsdbLsid_Type()
)
axOspfv3AreaLsdbLsid.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    axOspfv3AreaLsdbLsid.setStatus("current")
_AxOspfv3AreaLsdbSequence_Type = Integer32
_AxOspfv3AreaLsdbSequence_Object = MibTableColumn
axOspfv3AreaLsdbSequence = _AxOspfv3AreaLsdbSequence_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 15, 4, 1, 6),
    _AxOspfv3AreaLsdbSequence_Type()
)
axOspfv3AreaLsdbSequence.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axOspfv3AreaLsdbSequence.setStatus("current")
_AxOspfv3AreaLsdbAge_Type = Unsigned32
_AxOspfv3AreaLsdbAge_Object = MibTableColumn
axOspfv3AreaLsdbAge = _AxOspfv3AreaLsdbAge_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 15, 4, 1, 7),
    _AxOspfv3AreaLsdbAge_Type()
)
axOspfv3AreaLsdbAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axOspfv3AreaLsdbAge.setStatus("current")
_AxOspfv3AreaLsdbChecksum_Type = Integer32
_AxOspfv3AreaLsdbChecksum_Object = MibTableColumn
axOspfv3AreaLsdbChecksum = _AxOspfv3AreaLsdbChecksum_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 15, 4, 1, 8),
    _AxOspfv3AreaLsdbChecksum_Type()
)
axOspfv3AreaLsdbChecksum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axOspfv3AreaLsdbChecksum.setStatus("current")


class _AxOspfv3AreaLsdbAdvertisement_Type(OctetString):
    """Custom type axOspfv3AreaLsdbAdvertisement based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 65535),
    )


_AxOspfv3AreaLsdbAdvertisement_Type.__name__ = "OctetString"
_AxOspfv3AreaLsdbAdvertisement_Object = MibTableColumn
axOspfv3AreaLsdbAdvertisement = _AxOspfv3AreaLsdbAdvertisement_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 15, 4, 1, 9),
    _AxOspfv3AreaLsdbAdvertisement_Type()
)
axOspfv3AreaLsdbAdvertisement.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axOspfv3AreaLsdbAdvertisement.setStatus("current")
_AxOspfv3LinkLsdbTable_Object = MibTable
axOspfv3LinkLsdbTable = _AxOspfv3LinkLsdbTable_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 15, 5)
)
if mibBuilder.loadTexts:
    axOspfv3LinkLsdbTable.setStatus("current")
_AxOspfv3LinkLsdbEntry_Object = MibTableRow
axOspfv3LinkLsdbEntry = _AxOspfv3LinkLsdbEntry_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 15, 5, 1)
)
axOspfv3LinkLsdbEntry.setIndexNames(
    (0, "AX-OSPFV3-MIB", "axOspfv3LinkLsdbDomainNumber"),
    (0, "AX-OSPFV3-MIB", "axOspfv3LinkLsdbIfIndex"),
    (0, "AX-OSPFV3-MIB", "axOspfv3LinkLsdbIfInstId"),
    (0, "AX-OSPFV3-MIB", "axOspfv3LinkLsdbType"),
    (0, "AX-OSPFV3-MIB", "axOspfv3LinkLsdbRouterId"),
    (0, "AX-OSPFV3-MIB", "axOspfv3LinkLsdbLsid"),
)
if mibBuilder.loadTexts:
    axOspfv3LinkLsdbEntry.setStatus("current")
_AxOspfv3LinkLsdbDomainNumber_Type = Integer32
_AxOspfv3LinkLsdbDomainNumber_Object = MibTableColumn
axOspfv3LinkLsdbDomainNumber = _AxOspfv3LinkLsdbDomainNumber_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 15, 5, 1, 1),
    _AxOspfv3LinkLsdbDomainNumber_Type()
)
axOspfv3LinkLsdbDomainNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    axOspfv3LinkLsdbDomainNumber.setStatus("current")
_AxOspfv3LinkLsdbIfIndex_Type = InterfaceIndex
_AxOspfv3LinkLsdbIfIndex_Object = MibTableColumn
axOspfv3LinkLsdbIfIndex = _AxOspfv3LinkLsdbIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 15, 5, 1, 2),
    _AxOspfv3LinkLsdbIfIndex_Type()
)
axOspfv3LinkLsdbIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    axOspfv3LinkLsdbIfIndex.setStatus("current")
_AxOspfv3LinkLsdbIfInstId_Type = Unsigned32
_AxOspfv3LinkLsdbIfInstId_Object = MibTableColumn
axOspfv3LinkLsdbIfInstId = _AxOspfv3LinkLsdbIfInstId_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 15, 5, 1, 3),
    _AxOspfv3LinkLsdbIfInstId_Type()
)
axOspfv3LinkLsdbIfInstId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    axOspfv3LinkLsdbIfInstId.setStatus("current")
_AxOspfv3LinkLsdbType_Type = Unsigned32
_AxOspfv3LinkLsdbType_Object = MibTableColumn
axOspfv3LinkLsdbType = _AxOspfv3LinkLsdbType_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 15, 5, 1, 4),
    _AxOspfv3LinkLsdbType_Type()
)
axOspfv3LinkLsdbType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    axOspfv3LinkLsdbType.setStatus("current")
_AxOspfv3LinkLsdbRouterId_Type = Unsigned32
_AxOspfv3LinkLsdbRouterId_Object = MibTableColumn
axOspfv3LinkLsdbRouterId = _AxOspfv3LinkLsdbRouterId_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 15, 5, 1, 5),
    _AxOspfv3LinkLsdbRouterId_Type()
)
axOspfv3LinkLsdbRouterId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    axOspfv3LinkLsdbRouterId.setStatus("current")
_AxOspfv3LinkLsdbLsid_Type = Unsigned32
_AxOspfv3LinkLsdbLsid_Object = MibTableColumn
axOspfv3LinkLsdbLsid = _AxOspfv3LinkLsdbLsid_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 15, 5, 1, 6),
    _AxOspfv3LinkLsdbLsid_Type()
)
axOspfv3LinkLsdbLsid.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    axOspfv3LinkLsdbLsid.setStatus("current")
_AxOspfv3LinkLsdbSequence_Type = Integer32
_AxOspfv3LinkLsdbSequence_Object = MibTableColumn
axOspfv3LinkLsdbSequence = _AxOspfv3LinkLsdbSequence_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 15, 5, 1, 7),
    _AxOspfv3LinkLsdbSequence_Type()
)
axOspfv3LinkLsdbSequence.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axOspfv3LinkLsdbSequence.setStatus("current")
_AxOspfv3LinkLsdbAge_Type = Unsigned32
_AxOspfv3LinkLsdbAge_Object = MibTableColumn
axOspfv3LinkLsdbAge = _AxOspfv3LinkLsdbAge_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 15, 5, 1, 8),
    _AxOspfv3LinkLsdbAge_Type()
)
axOspfv3LinkLsdbAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axOspfv3LinkLsdbAge.setStatus("current")
_AxOspfv3LinkLsdbChecksum_Type = Integer32
_AxOspfv3LinkLsdbChecksum_Object = MibTableColumn
axOspfv3LinkLsdbChecksum = _AxOspfv3LinkLsdbChecksum_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 15, 5, 1, 9),
    _AxOspfv3LinkLsdbChecksum_Type()
)
axOspfv3LinkLsdbChecksum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axOspfv3LinkLsdbChecksum.setStatus("current")


class _AxOspfv3LinkLsdbAdvertisement_Type(OctetString):
    """Custom type axOspfv3LinkLsdbAdvertisement based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 65535),
    )


_AxOspfv3LinkLsdbAdvertisement_Type.__name__ = "OctetString"
_AxOspfv3LinkLsdbAdvertisement_Object = MibTableColumn
axOspfv3LinkLsdbAdvertisement = _AxOspfv3LinkLsdbAdvertisement_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 15, 5, 1, 10),
    _AxOspfv3LinkLsdbAdvertisement_Type()
)
axOspfv3LinkLsdbAdvertisement.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axOspfv3LinkLsdbAdvertisement.setStatus("current")
_AxOspfv3IfTable_Object = MibTable
axOspfv3IfTable = _AxOspfv3IfTable_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 15, 7)
)
if mibBuilder.loadTexts:
    axOspfv3IfTable.setStatus("current")
_AxOspfv3IfEntry_Object = MibTableRow
axOspfv3IfEntry = _AxOspfv3IfEntry_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 15, 7, 1)
)
axOspfv3IfEntry.setIndexNames(
    (0, "AX-OSPFV3-MIB", "axOspfv3IfDomainNumber"),
    (0, "AX-OSPFV3-MIB", "axOspfv3IfIndex"),
    (0, "AX-OSPFV3-MIB", "axOspfv3IfInstId"),
)
if mibBuilder.loadTexts:
    axOspfv3IfEntry.setStatus("current")
_AxOspfv3IfDomainNumber_Type = Integer32
_AxOspfv3IfDomainNumber_Object = MibTableColumn
axOspfv3IfDomainNumber = _AxOspfv3IfDomainNumber_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 15, 7, 1, 1),
    _AxOspfv3IfDomainNumber_Type()
)
axOspfv3IfDomainNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    axOspfv3IfDomainNumber.setStatus("current")
_AxOspfv3IfIndex_Type = InterfaceIndex
_AxOspfv3IfIndex_Object = MibTableColumn
axOspfv3IfIndex = _AxOspfv3IfIndex_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 15, 7, 1, 2),
    _AxOspfv3IfIndex_Type()
)
axOspfv3IfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    axOspfv3IfIndex.setStatus("current")
_AxOspfv3IfInstId_Type = Unsigned32
_AxOspfv3IfInstId_Object = MibTableColumn
axOspfv3IfInstId = _AxOspfv3IfInstId_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 15, 7, 1, 3),
    _AxOspfv3IfInstId_Type()
)
axOspfv3IfInstId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    axOspfv3IfInstId.setStatus("current")
_AxOspfv3IfAreaId_Type = Unsigned32
_AxOspfv3IfAreaId_Object = MibTableColumn
axOspfv3IfAreaId = _AxOspfv3IfAreaId_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 15, 7, 1, 4),
    _AxOspfv3IfAreaId_Type()
)
axOspfv3IfAreaId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axOspfv3IfAreaId.setStatus("current")


class _AxOspfv3IfType_Type(Integer32):
    """Custom type axOspfv3IfType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              5)
        )
    )
    namedValues = NamedValues(
        *(("broadcast", 1),
          ("nbma", 2),
          ("pointToPoint", 3),
          ("pointToMultipoint", 5))
    )


_AxOspfv3IfType_Type.__name__ = "Integer32"
_AxOspfv3IfType_Object = MibTableColumn
axOspfv3IfType = _AxOspfv3IfType_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 15, 7, 1, 5),
    _AxOspfv3IfType_Type()
)
axOspfv3IfType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axOspfv3IfType.setStatus("current")
_AxOspfv3IfAdminStatus_Type = Status
_AxOspfv3IfAdminStatus_Object = MibTableColumn
axOspfv3IfAdminStatus = _AxOspfv3IfAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 15, 7, 1, 6),
    _AxOspfv3IfAdminStatus_Type()
)
axOspfv3IfAdminStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axOspfv3IfAdminStatus.setStatus("current")
_AxOspfv3IfRtrPriority_Type = Integer32
_AxOspfv3IfRtrPriority_Object = MibTableColumn
axOspfv3IfRtrPriority = _AxOspfv3IfRtrPriority_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 15, 7, 1, 7),
    _AxOspfv3IfRtrPriority_Type()
)
axOspfv3IfRtrPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axOspfv3IfRtrPriority.setStatus("current")
_AxOspfv3IfTransitDelay_Type = Unsigned32
_AxOspfv3IfTransitDelay_Object = MibTableColumn
axOspfv3IfTransitDelay = _AxOspfv3IfTransitDelay_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 15, 7, 1, 8),
    _AxOspfv3IfTransitDelay_Type()
)
axOspfv3IfTransitDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axOspfv3IfTransitDelay.setStatus("current")
_AxOspfv3IfRetransInterval_Type = Unsigned32
_AxOspfv3IfRetransInterval_Object = MibTableColumn
axOspfv3IfRetransInterval = _AxOspfv3IfRetransInterval_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 15, 7, 1, 9),
    _AxOspfv3IfRetransInterval_Type()
)
axOspfv3IfRetransInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axOspfv3IfRetransInterval.setStatus("current")
_AxOspfv3IfHelloInterval_Type = Integer32
_AxOspfv3IfHelloInterval_Object = MibTableColumn
axOspfv3IfHelloInterval = _AxOspfv3IfHelloInterval_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 15, 7, 1, 10),
    _AxOspfv3IfHelloInterval_Type()
)
axOspfv3IfHelloInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axOspfv3IfHelloInterval.setStatus("current")
_AxOspfv3IfRtrDeadInterval_Type = Unsigned32
_AxOspfv3IfRtrDeadInterval_Object = MibTableColumn
axOspfv3IfRtrDeadInterval = _AxOspfv3IfRtrDeadInterval_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 15, 7, 1, 11),
    _AxOspfv3IfRtrDeadInterval_Type()
)
axOspfv3IfRtrDeadInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axOspfv3IfRtrDeadInterval.setStatus("current")
_AxOspfv3IfPollInterval_Type = Unsigned32
_AxOspfv3IfPollInterval_Object = MibTableColumn
axOspfv3IfPollInterval = _AxOspfv3IfPollInterval_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 15, 7, 1, 12),
    _AxOspfv3IfPollInterval_Type()
)
axOspfv3IfPollInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axOspfv3IfPollInterval.setStatus("current")


class _AxOspfv3IfState_Type(Integer32):
    """Custom type axOspfv3IfState based on Integer32"""
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("down", 1),
          ("loopback", 2),
          ("waiting", 3),
          ("pointToPoint", 4),
          ("designatedRouter", 5),
          ("backupDesignatedRouter", 6),
          ("otherDesignatedRouter", 7),
          ("standby", 8))
    )


_AxOspfv3IfState_Type.__name__ = "Integer32"
_AxOspfv3IfState_Object = MibTableColumn
axOspfv3IfState = _AxOspfv3IfState_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 15, 7, 1, 13),
    _AxOspfv3IfState_Type()
)
axOspfv3IfState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axOspfv3IfState.setStatus("current")
_AxOspfv3IfDesignatedRouter_Type = Unsigned32
_AxOspfv3IfDesignatedRouter_Object = MibTableColumn
axOspfv3IfDesignatedRouter = _AxOspfv3IfDesignatedRouter_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 15, 7, 1, 14),
    _AxOspfv3IfDesignatedRouter_Type()
)
axOspfv3IfDesignatedRouter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axOspfv3IfDesignatedRouter.setStatus("current")
_AxOspfv3IfBackupDesignatedRouter_Type = Unsigned32
_AxOspfv3IfBackupDesignatedRouter_Object = MibTableColumn
axOspfv3IfBackupDesignatedRouter = _AxOspfv3IfBackupDesignatedRouter_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 15, 7, 1, 15),
    _AxOspfv3IfBackupDesignatedRouter_Type()
)
axOspfv3IfBackupDesignatedRouter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axOspfv3IfBackupDesignatedRouter.setStatus("current")
_AxOspfv3IfEvents_Type = Counter32
_AxOspfv3IfEvents_Object = MibTableColumn
axOspfv3IfEvents = _AxOspfv3IfEvents_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 15, 7, 1, 16),
    _AxOspfv3IfEvents_Type()
)
axOspfv3IfEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axOspfv3IfEvents.setStatus("current")
_AxOspfv3IfRowStatus_Type = RowStatus
_AxOspfv3IfRowStatus_Object = MibTableColumn
axOspfv3IfRowStatus = _AxOspfv3IfRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 15, 7, 1, 17),
    _AxOspfv3IfRowStatus_Type()
)
axOspfv3IfRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    axOspfv3IfRowStatus.setStatus("current")
_AxOspfv3IfDemand_Type = TruthValue
_AxOspfv3IfDemand_Object = MibTableColumn
axOspfv3IfDemand = _AxOspfv3IfDemand_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 15, 7, 1, 18),
    _AxOspfv3IfDemand_Type()
)
axOspfv3IfDemand.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axOspfv3IfDemand.setStatus("current")
_AxOspfv3IfMetricValue_Type = Integer32
_AxOspfv3IfMetricValue_Object = MibTableColumn
axOspfv3IfMetricValue = _AxOspfv3IfMetricValue_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 15, 7, 1, 19),
    _AxOspfv3IfMetricValue_Type()
)
axOspfv3IfMetricValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axOspfv3IfMetricValue.setStatus("current")
_AxOspfv3IfLinkScopeLsaCount_Type = Gauge32
_AxOspfv3IfLinkScopeLsaCount_Object = MibTableColumn
axOspfv3IfLinkScopeLsaCount = _AxOspfv3IfLinkScopeLsaCount_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 15, 7, 1, 20),
    _AxOspfv3IfLinkScopeLsaCount_Type()
)
axOspfv3IfLinkScopeLsaCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axOspfv3IfLinkScopeLsaCount.setStatus("current")
_AxOspfv3IfLinkLsaCksumSum_Type = Unsigned32
_AxOspfv3IfLinkLsaCksumSum_Object = MibTableColumn
axOspfv3IfLinkLsaCksumSum = _AxOspfv3IfLinkLsaCksumSum_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 15, 7, 1, 21),
    _AxOspfv3IfLinkLsaCksumSum_Type()
)
axOspfv3IfLinkLsaCksumSum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axOspfv3IfLinkLsaCksumSum.setStatus("current")
_AxOspfv3IfDemandNbrProbe_Type = TruthValue
_AxOspfv3IfDemandNbrProbe_Object = MibTableColumn
axOspfv3IfDemandNbrProbe = _AxOspfv3IfDemandNbrProbe_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 15, 7, 1, 22),
    _AxOspfv3IfDemandNbrProbe_Type()
)
axOspfv3IfDemandNbrProbe.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axOspfv3IfDemandNbrProbe.setStatus("current")
_AxOspfv3IfTEDisabled_Type = TruthValue
_AxOspfv3IfTEDisabled_Object = MibTableColumn
axOspfv3IfTEDisabled = _AxOspfv3IfTEDisabled_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 15, 7, 1, 25),
    _AxOspfv3IfTEDisabled_Type()
)
axOspfv3IfTEDisabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axOspfv3IfTEDisabled.setStatus("current")
_AxOspfv3IfLinkLSASuppression_Type = TruthValue
_AxOspfv3IfLinkLSASuppression_Object = MibTableColumn
axOspfv3IfLinkLSASuppression = _AxOspfv3IfLinkLSASuppression_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 15, 7, 1, 26),
    _AxOspfv3IfLinkLSASuppression_Type()
)
axOspfv3IfLinkLSASuppression.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axOspfv3IfLinkLSASuppression.setStatus("current")
_AxOspfv3VirtIfTable_Object = MibTable
axOspfv3VirtIfTable = _AxOspfv3VirtIfTable_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 15, 8)
)
if mibBuilder.loadTexts:
    axOspfv3VirtIfTable.setStatus("current")
_AxOspfv3VirtIfEntry_Object = MibTableRow
axOspfv3VirtIfEntry = _AxOspfv3VirtIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 15, 8, 1)
)
axOspfv3VirtIfEntry.setIndexNames(
    (0, "AX-OSPFV3-MIB", "axOspfv3VirtIfDomainNumber"),
    (0, "AX-OSPFV3-MIB", "axOspfv3VirtIfAreaId"),
    (0, "AX-OSPFV3-MIB", "axOspfv3VirtIfNeighbor"),
)
if mibBuilder.loadTexts:
    axOspfv3VirtIfEntry.setStatus("current")
_AxOspfv3VirtIfDomainNumber_Type = Integer32
_AxOspfv3VirtIfDomainNumber_Object = MibTableColumn
axOspfv3VirtIfDomainNumber = _AxOspfv3VirtIfDomainNumber_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 15, 8, 1, 1),
    _AxOspfv3VirtIfDomainNumber_Type()
)
axOspfv3VirtIfDomainNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    axOspfv3VirtIfDomainNumber.setStatus("current")
_AxOspfv3VirtIfAreaId_Type = Unsigned32
_AxOspfv3VirtIfAreaId_Object = MibTableColumn
axOspfv3VirtIfAreaId = _AxOspfv3VirtIfAreaId_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 15, 8, 1, 2),
    _AxOspfv3VirtIfAreaId_Type()
)
axOspfv3VirtIfAreaId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    axOspfv3VirtIfAreaId.setStatus("current")
_AxOspfv3VirtIfNeighbor_Type = Unsigned32
_AxOspfv3VirtIfNeighbor_Object = MibTableColumn
axOspfv3VirtIfNeighbor = _AxOspfv3VirtIfNeighbor_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 15, 8, 1, 3),
    _AxOspfv3VirtIfNeighbor_Type()
)
axOspfv3VirtIfNeighbor.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    axOspfv3VirtIfNeighbor.setStatus("current")
_AxOspfv3VirtIfIndex_Type = InterfaceIndex
_AxOspfv3VirtIfIndex_Object = MibTableColumn
axOspfv3VirtIfIndex = _AxOspfv3VirtIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 15, 8, 1, 4),
    _AxOspfv3VirtIfIndex_Type()
)
axOspfv3VirtIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axOspfv3VirtIfIndex.setStatus("current")
_AxOspfv3VirtIfInstId_Type = Unsigned32
_AxOspfv3VirtIfInstId_Object = MibTableColumn
axOspfv3VirtIfInstId = _AxOspfv3VirtIfInstId_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 15, 8, 1, 5),
    _AxOspfv3VirtIfInstId_Type()
)
axOspfv3VirtIfInstId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axOspfv3VirtIfInstId.setStatus("current")
_AxOspfv3VirtIfTransitDelay_Type = Unsigned32
_AxOspfv3VirtIfTransitDelay_Object = MibTableColumn
axOspfv3VirtIfTransitDelay = _AxOspfv3VirtIfTransitDelay_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 15, 8, 1, 6),
    _AxOspfv3VirtIfTransitDelay_Type()
)
axOspfv3VirtIfTransitDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axOspfv3VirtIfTransitDelay.setStatus("current")
_AxOspfv3VirtIfRetransInterval_Type = Unsigned32
_AxOspfv3VirtIfRetransInterval_Object = MibTableColumn
axOspfv3VirtIfRetransInterval = _AxOspfv3VirtIfRetransInterval_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 15, 8, 1, 7),
    _AxOspfv3VirtIfRetransInterval_Type()
)
axOspfv3VirtIfRetransInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axOspfv3VirtIfRetransInterval.setStatus("current")
_AxOspfv3VirtIfHelloInterval_Type = Integer32
_AxOspfv3VirtIfHelloInterval_Object = MibTableColumn
axOspfv3VirtIfHelloInterval = _AxOspfv3VirtIfHelloInterval_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 15, 8, 1, 8),
    _AxOspfv3VirtIfHelloInterval_Type()
)
axOspfv3VirtIfHelloInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axOspfv3VirtIfHelloInterval.setStatus("current")
_AxOspfv3VirtIfRtrDeadInterval_Type = Unsigned32
_AxOspfv3VirtIfRtrDeadInterval_Object = MibTableColumn
axOspfv3VirtIfRtrDeadInterval = _AxOspfv3VirtIfRtrDeadInterval_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 15, 8, 1, 9),
    _AxOspfv3VirtIfRtrDeadInterval_Type()
)
axOspfv3VirtIfRtrDeadInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axOspfv3VirtIfRtrDeadInterval.setStatus("current")


class _AxOspfv3VirtIfState_Type(Integer32):
    """Custom type axOspfv3VirtIfState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              4)
        )
    )
    namedValues = NamedValues(
        *(("down", 1),
          ("pointToPoint", 4))
    )


_AxOspfv3VirtIfState_Type.__name__ = "Integer32"
_AxOspfv3VirtIfState_Object = MibTableColumn
axOspfv3VirtIfState = _AxOspfv3VirtIfState_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 15, 8, 1, 10),
    _AxOspfv3VirtIfState_Type()
)
axOspfv3VirtIfState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axOspfv3VirtIfState.setStatus("current")
_AxOspfv3VirtIfEvents_Type = Counter32
_AxOspfv3VirtIfEvents_Object = MibTableColumn
axOspfv3VirtIfEvents = _AxOspfv3VirtIfEvents_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 15, 8, 1, 11),
    _AxOspfv3VirtIfEvents_Type()
)
axOspfv3VirtIfEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axOspfv3VirtIfEvents.setStatus("current")
_AxOspfv3VirtIfRowStatus_Type = RowStatus
_AxOspfv3VirtIfRowStatus_Object = MibTableColumn
axOspfv3VirtIfRowStatus = _AxOspfv3VirtIfRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 15, 8, 1, 12),
    _AxOspfv3VirtIfRowStatus_Type()
)
axOspfv3VirtIfRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    axOspfv3VirtIfRowStatus.setStatus("current")
_AxOspfv3VirtIfLinkScopeLsaCount_Type = Gauge32
_AxOspfv3VirtIfLinkScopeLsaCount_Object = MibTableColumn
axOspfv3VirtIfLinkScopeLsaCount = _AxOspfv3VirtIfLinkScopeLsaCount_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 15, 8, 1, 13),
    _AxOspfv3VirtIfLinkScopeLsaCount_Type()
)
axOspfv3VirtIfLinkScopeLsaCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axOspfv3VirtIfLinkScopeLsaCount.setStatus("current")
_AxOspfv3VirtIfLinkLsaCksumSum_Type = Unsigned32
_AxOspfv3VirtIfLinkLsaCksumSum_Object = MibTableColumn
axOspfv3VirtIfLinkLsaCksumSum = _AxOspfv3VirtIfLinkLsaCksumSum_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 15, 8, 1, 14),
    _AxOspfv3VirtIfLinkLsaCksumSum_Type()
)
axOspfv3VirtIfLinkLsaCksumSum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axOspfv3VirtIfLinkLsaCksumSum.setStatus("current")
_AxOspfv3NbrTable_Object = MibTable
axOspfv3NbrTable = _AxOspfv3NbrTable_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 15, 9)
)
if mibBuilder.loadTexts:
    axOspfv3NbrTable.setStatus("current")
_AxOspfv3NbrEntry_Object = MibTableRow
axOspfv3NbrEntry = _AxOspfv3NbrEntry_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 15, 9, 1)
)
axOspfv3NbrEntry.setIndexNames(
    (0, "AX-OSPFV3-MIB", "axOspfv3NbrDomainNumber"),
    (0, "AX-OSPFV3-MIB", "axOspfv3NbrIfIndex"),
    (0, "AX-OSPFV3-MIB", "axOspfv3NbrIfInstId"),
    (0, "AX-OSPFV3-MIB", "axOspfv3NbrRtrId"),
)
if mibBuilder.loadTexts:
    axOspfv3NbrEntry.setStatus("current")
_AxOspfv3NbrDomainNumber_Type = Integer32
_AxOspfv3NbrDomainNumber_Object = MibTableColumn
axOspfv3NbrDomainNumber = _AxOspfv3NbrDomainNumber_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 15, 9, 1, 1),
    _AxOspfv3NbrDomainNumber_Type()
)
axOspfv3NbrDomainNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    axOspfv3NbrDomainNumber.setStatus("current")
_AxOspfv3NbrIfIndex_Type = InterfaceIndex
_AxOspfv3NbrIfIndex_Object = MibTableColumn
axOspfv3NbrIfIndex = _AxOspfv3NbrIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 15, 9, 1, 2),
    _AxOspfv3NbrIfIndex_Type()
)
axOspfv3NbrIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    axOspfv3NbrIfIndex.setStatus("current")
_AxOspfv3NbrIfInstId_Type = Unsigned32
_AxOspfv3NbrIfInstId_Object = MibTableColumn
axOspfv3NbrIfInstId = _AxOspfv3NbrIfInstId_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 15, 9, 1, 3),
    _AxOspfv3NbrIfInstId_Type()
)
axOspfv3NbrIfInstId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    axOspfv3NbrIfInstId.setStatus("current")
_AxOspfv3NbrRtrId_Type = Unsigned32
_AxOspfv3NbrRtrId_Object = MibTableColumn
axOspfv3NbrRtrId = _AxOspfv3NbrRtrId_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 15, 9, 1, 4),
    _AxOspfv3NbrRtrId_Type()
)
axOspfv3NbrRtrId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    axOspfv3NbrRtrId.setStatus("current")
_AxOspfv3NbrAddressType_Type = InetAddressType
_AxOspfv3NbrAddressType_Object = MibTableColumn
axOspfv3NbrAddressType = _AxOspfv3NbrAddressType_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 15, 9, 1, 5),
    _AxOspfv3NbrAddressType_Type()
)
axOspfv3NbrAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axOspfv3NbrAddressType.setStatus("current")
_AxOspfv3NbrAddress_Type = InetAddress
_AxOspfv3NbrAddress_Object = MibTableColumn
axOspfv3NbrAddress = _AxOspfv3NbrAddress_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 15, 9, 1, 6),
    _AxOspfv3NbrAddress_Type()
)
axOspfv3NbrAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axOspfv3NbrAddress.setStatus("current")
_AxOspfv3NbrOptions_Type = Integer32
_AxOspfv3NbrOptions_Object = MibTableColumn
axOspfv3NbrOptions = _AxOspfv3NbrOptions_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 15, 9, 1, 7),
    _AxOspfv3NbrOptions_Type()
)
axOspfv3NbrOptions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axOspfv3NbrOptions.setStatus("current")
_AxOspfv3NbrPriority_Type = Integer32
_AxOspfv3NbrPriority_Object = MibTableColumn
axOspfv3NbrPriority = _AxOspfv3NbrPriority_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 15, 9, 1, 8),
    _AxOspfv3NbrPriority_Type()
)
axOspfv3NbrPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axOspfv3NbrPriority.setStatus("current")


class _AxOspfv3NbrState_Type(Integer32):
    """Custom type axOspfv3NbrState based on Integer32"""
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("down", 1),
          ("attempt", 2),
          ("init", 3),
          ("twoWay", 4),
          ("exchangeStart", 5),
          ("exchange", 6),
          ("loading", 7),
          ("full", 8))
    )


_AxOspfv3NbrState_Type.__name__ = "Integer32"
_AxOspfv3NbrState_Object = MibTableColumn
axOspfv3NbrState = _AxOspfv3NbrState_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 15, 9, 1, 9),
    _AxOspfv3NbrState_Type()
)
axOspfv3NbrState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axOspfv3NbrState.setStatus("current")
_AxOspfv3NbrEvents_Type = Counter32
_AxOspfv3NbrEvents_Object = MibTableColumn
axOspfv3NbrEvents = _AxOspfv3NbrEvents_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 15, 9, 1, 10),
    _AxOspfv3NbrEvents_Type()
)
axOspfv3NbrEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axOspfv3NbrEvents.setStatus("current")
_AxOspfv3NbrLsRetransQLen_Type = Gauge32
_AxOspfv3NbrLsRetransQLen_Object = MibTableColumn
axOspfv3NbrLsRetransQLen = _AxOspfv3NbrLsRetransQLen_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 15, 9, 1, 11),
    _AxOspfv3NbrLsRetransQLen_Type()
)
axOspfv3NbrLsRetransQLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axOspfv3NbrLsRetransQLen.setStatus("current")
_AxOspfv3NbrHelloSuppressed_Type = TruthValue
_AxOspfv3NbrHelloSuppressed_Object = MibTableColumn
axOspfv3NbrHelloSuppressed = _AxOspfv3NbrHelloSuppressed_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 15, 9, 1, 12),
    _AxOspfv3NbrHelloSuppressed_Type()
)
axOspfv3NbrHelloSuppressed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axOspfv3NbrHelloSuppressed.setStatus("current")
_AxOspfv3NbrIfId_Type = InterfaceIndex
_AxOspfv3NbrIfId_Object = MibTableColumn
axOspfv3NbrIfId = _AxOspfv3NbrIfId_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 15, 9, 1, 13),
    _AxOspfv3NbrIfId_Type()
)
axOspfv3NbrIfId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axOspfv3NbrIfId.setStatus("current")


class _AxOspfv3NbrRestartHelperStatus_Type(Integer32):
    """Custom type axOspfv3NbrRestartHelperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notHelping", 1),
          ("helping", 2))
    )


_AxOspfv3NbrRestartHelperStatus_Type.__name__ = "Integer32"
_AxOspfv3NbrRestartHelperStatus_Object = MibTableColumn
axOspfv3NbrRestartHelperStatus = _AxOspfv3NbrRestartHelperStatus_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 15, 9, 1, 14),
    _AxOspfv3NbrRestartHelperStatus_Type()
)
axOspfv3NbrRestartHelperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axOspfv3NbrRestartHelperStatus.setStatus("current")


class _AxOspfv3NbrRestartHelperExitReason_Type(Integer32):
    """Custom type axOspfv3NbrRestartHelperExitReason based on Integer32"""
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
        *(("none", 1),
          ("inProgress", 2),
          ("completed", 3),
          ("timedOut", 4),
          ("topologyChanged", 5))
    )


_AxOspfv3NbrRestartHelperExitReason_Type.__name__ = "Integer32"
_AxOspfv3NbrRestartHelperExitReason_Object = MibTableColumn
axOspfv3NbrRestartHelperExitReason = _AxOspfv3NbrRestartHelperExitReason_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 15, 9, 1, 16),
    _AxOspfv3NbrRestartHelperExitReason_Type()
)
axOspfv3NbrRestartHelperExitReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axOspfv3NbrRestartHelperExitReason.setStatus("current")
_AxOspfv3VirtNbrTable_Object = MibTable
axOspfv3VirtNbrTable = _AxOspfv3VirtNbrTable_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 15, 11)
)
if mibBuilder.loadTexts:
    axOspfv3VirtNbrTable.setStatus("current")
_AxOspfv3VirtNbrEntry_Object = MibTableRow
axOspfv3VirtNbrEntry = _AxOspfv3VirtNbrEntry_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 15, 11, 1)
)
axOspfv3VirtNbrEntry.setIndexNames(
    (0, "AX-OSPFV3-MIB", "axOspfv3VirtNbrDomainNumber"),
    (0, "AX-OSPFV3-MIB", "axOspfv3VirtNbrArea"),
    (0, "AX-OSPFV3-MIB", "axOspfv3VirtNbrRtrId"),
)
if mibBuilder.loadTexts:
    axOspfv3VirtNbrEntry.setStatus("current")
_AxOspfv3VirtNbrDomainNumber_Type = Integer32
_AxOspfv3VirtNbrDomainNumber_Object = MibTableColumn
axOspfv3VirtNbrDomainNumber = _AxOspfv3VirtNbrDomainNumber_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 15, 11, 1, 1),
    _AxOspfv3VirtNbrDomainNumber_Type()
)
axOspfv3VirtNbrDomainNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    axOspfv3VirtNbrDomainNumber.setStatus("current")
_AxOspfv3VirtNbrArea_Type = Unsigned32
_AxOspfv3VirtNbrArea_Object = MibTableColumn
axOspfv3VirtNbrArea = _AxOspfv3VirtNbrArea_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 15, 11, 1, 2),
    _AxOspfv3VirtNbrArea_Type()
)
axOspfv3VirtNbrArea.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    axOspfv3VirtNbrArea.setStatus("current")
_AxOspfv3VirtNbrRtrId_Type = Unsigned32
_AxOspfv3VirtNbrRtrId_Object = MibTableColumn
axOspfv3VirtNbrRtrId = _AxOspfv3VirtNbrRtrId_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 15, 11, 1, 3),
    _AxOspfv3VirtNbrRtrId_Type()
)
axOspfv3VirtNbrRtrId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    axOspfv3VirtNbrRtrId.setStatus("current")
_AxOspfv3VirtNbrIfIndex_Type = InterfaceIndex
_AxOspfv3VirtNbrIfIndex_Object = MibTableColumn
axOspfv3VirtNbrIfIndex = _AxOspfv3VirtNbrIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 15, 11, 1, 4),
    _AxOspfv3VirtNbrIfIndex_Type()
)
axOspfv3VirtNbrIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axOspfv3VirtNbrIfIndex.setStatus("current")
_AxOspfv3VirtNbrIfInstId_Type = Unsigned32
_AxOspfv3VirtNbrIfInstId_Object = MibTableColumn
axOspfv3VirtNbrIfInstId = _AxOspfv3VirtNbrIfInstId_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 15, 11, 1, 5),
    _AxOspfv3VirtNbrIfInstId_Type()
)
axOspfv3VirtNbrIfInstId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axOspfv3VirtNbrIfInstId.setStatus("current")
_AxOspfv3VirtNbrAddressType_Type = InetAddressType
_AxOspfv3VirtNbrAddressType_Object = MibTableColumn
axOspfv3VirtNbrAddressType = _AxOspfv3VirtNbrAddressType_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 15, 11, 1, 6),
    _AxOspfv3VirtNbrAddressType_Type()
)
axOspfv3VirtNbrAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axOspfv3VirtNbrAddressType.setStatus("current")
_AxOspfv3VirtNbrAddress_Type = InetAddress
_AxOspfv3VirtNbrAddress_Object = MibTableColumn
axOspfv3VirtNbrAddress = _AxOspfv3VirtNbrAddress_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 15, 11, 1, 7),
    _AxOspfv3VirtNbrAddress_Type()
)
axOspfv3VirtNbrAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axOspfv3VirtNbrAddress.setStatus("current")
_AxOspfv3VirtNbrOptions_Type = Integer32
_AxOspfv3VirtNbrOptions_Object = MibTableColumn
axOspfv3VirtNbrOptions = _AxOspfv3VirtNbrOptions_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 15, 11, 1, 8),
    _AxOspfv3VirtNbrOptions_Type()
)
axOspfv3VirtNbrOptions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axOspfv3VirtNbrOptions.setStatus("current")


class _AxOspfv3VirtNbrState_Type(Integer32):
    """Custom type axOspfv3VirtNbrState based on Integer32"""
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("down", 1),
          ("attempt", 2),
          ("init", 3),
          ("twoWay", 4),
          ("exchangeStart", 5),
          ("exchange", 6),
          ("loading", 7),
          ("full", 8))
    )


_AxOspfv3VirtNbrState_Type.__name__ = "Integer32"
_AxOspfv3VirtNbrState_Object = MibTableColumn
axOspfv3VirtNbrState = _AxOspfv3VirtNbrState_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 15, 11, 1, 9),
    _AxOspfv3VirtNbrState_Type()
)
axOspfv3VirtNbrState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axOspfv3VirtNbrState.setStatus("current")
_AxOspfv3VirtNbrEvents_Type = Counter32
_AxOspfv3VirtNbrEvents_Object = MibTableColumn
axOspfv3VirtNbrEvents = _AxOspfv3VirtNbrEvents_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 15, 11, 1, 10),
    _AxOspfv3VirtNbrEvents_Type()
)
axOspfv3VirtNbrEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axOspfv3VirtNbrEvents.setStatus("current")
_AxOspfv3VirtNbrLsRetransQLen_Type = Gauge32
_AxOspfv3VirtNbrLsRetransQLen_Object = MibTableColumn
axOspfv3VirtNbrLsRetransQLen = _AxOspfv3VirtNbrLsRetransQLen_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 15, 11, 1, 11),
    _AxOspfv3VirtNbrLsRetransQLen_Type()
)
axOspfv3VirtNbrLsRetransQLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axOspfv3VirtNbrLsRetransQLen.setStatus("current")
_AxOspfv3VirtNbrHelloSuppressed_Type = TruthValue
_AxOspfv3VirtNbrHelloSuppressed_Object = MibTableColumn
axOspfv3VirtNbrHelloSuppressed = _AxOspfv3VirtNbrHelloSuppressed_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 15, 11, 1, 12),
    _AxOspfv3VirtNbrHelloSuppressed_Type()
)
axOspfv3VirtNbrHelloSuppressed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axOspfv3VirtNbrHelloSuppressed.setStatus("current")
_AxOspfv3VirtNbrIfId_Type = InterfaceIndex
_AxOspfv3VirtNbrIfId_Object = MibTableColumn
axOspfv3VirtNbrIfId = _AxOspfv3VirtNbrIfId_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 15, 11, 1, 13),
    _AxOspfv3VirtNbrIfId_Type()
)
axOspfv3VirtNbrIfId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axOspfv3VirtNbrIfId.setStatus("current")


class _AxOspfv3VirtNbrRestartHelperStatus_Type(Integer32):
    """Custom type axOspfv3VirtNbrRestartHelperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notHelping", 1),
          ("helping", 2))
    )


_AxOspfv3VirtNbrRestartHelperStatus_Type.__name__ = "Integer32"
_AxOspfv3VirtNbrRestartHelperStatus_Object = MibTableColumn
axOspfv3VirtNbrRestartHelperStatus = _AxOspfv3VirtNbrRestartHelperStatus_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 15, 11, 1, 14),
    _AxOspfv3VirtNbrRestartHelperStatus_Type()
)
axOspfv3VirtNbrRestartHelperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axOspfv3VirtNbrRestartHelperStatus.setStatus("current")


class _AxOspfv3VirtNbrRestartHelperExitReason_Type(Integer32):
    """Custom type axOspfv3VirtNbrRestartHelperExitReason based on Integer32"""
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
        *(("none", 1),
          ("inProgress", 2),
          ("completed", 3),
          ("timedOut", 4),
          ("topologyChanged", 5))
    )


_AxOspfv3VirtNbrRestartHelperExitReason_Type.__name__ = "Integer32"
_AxOspfv3VirtNbrRestartHelperExitReason_Object = MibTableColumn
axOspfv3VirtNbrRestartHelperExitReason = _AxOspfv3VirtNbrRestartHelperExitReason_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 15, 11, 1, 16),
    _AxOspfv3VirtNbrRestartHelperExitReason_Type()
)
axOspfv3VirtNbrRestartHelperExitReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axOspfv3VirtNbrRestartHelperExitReason.setStatus("current")
_AxOspfv3AreaAggregateTable_Object = MibTable
axOspfv3AreaAggregateTable = _AxOspfv3AreaAggregateTable_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 15, 12)
)
if mibBuilder.loadTexts:
    axOspfv3AreaAggregateTable.setStatus("current")
_AxOspfv3AreaAggregateEntry_Object = MibTableRow
axOspfv3AreaAggregateEntry = _AxOspfv3AreaAggregateEntry_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 15, 12, 1)
)
axOspfv3AreaAggregateEntry.setIndexNames(
    (0, "AX-OSPFV3-MIB", "axOspfv3AreaAggregateDomainNumber"),
    (0, "AX-OSPFV3-MIB", "axOspfv3AreaAggregateAreaID"),
    (0, "AX-OSPFV3-MIB", "axOspfv3AreaAggregateAreaLsdbType"),
    (0, "AX-OSPFV3-MIB", "axOspfv3AreaAggregatePrefixType"),
    (0, "AX-OSPFV3-MIB", "axOspfv3AreaAggregatePrefix"),
    (0, "AX-OSPFV3-MIB", "axOspfv3AreaAggregatePrefixLength"),
)
if mibBuilder.loadTexts:
    axOspfv3AreaAggregateEntry.setStatus("current")
_AxOspfv3AreaAggregateDomainNumber_Type = Integer32
_AxOspfv3AreaAggregateDomainNumber_Object = MibTableColumn
axOspfv3AreaAggregateDomainNumber = _AxOspfv3AreaAggregateDomainNumber_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 15, 12, 1, 1),
    _AxOspfv3AreaAggregateDomainNumber_Type()
)
axOspfv3AreaAggregateDomainNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    axOspfv3AreaAggregateDomainNumber.setStatus("current")
_AxOspfv3AreaAggregateAreaID_Type = Unsigned32
_AxOspfv3AreaAggregateAreaID_Object = MibTableColumn
axOspfv3AreaAggregateAreaID = _AxOspfv3AreaAggregateAreaID_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 15, 12, 1, 2),
    _AxOspfv3AreaAggregateAreaID_Type()
)
axOspfv3AreaAggregateAreaID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    axOspfv3AreaAggregateAreaID.setStatus("current")


class _AxOspfv3AreaAggregateAreaLsdbType_Type(Integer32):
    """Custom type axOspfv3AreaAggregateAreaLsdbType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(8195,
              8199)
        )
    )
    namedValues = NamedValues(
        *(("interAreaPrefixLsa", 8195),
          ("nssaExternalLsa", 8199))
    )


_AxOspfv3AreaAggregateAreaLsdbType_Type.__name__ = "Integer32"
_AxOspfv3AreaAggregateAreaLsdbType_Object = MibTableColumn
axOspfv3AreaAggregateAreaLsdbType = _AxOspfv3AreaAggregateAreaLsdbType_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 15, 12, 1, 3),
    _AxOspfv3AreaAggregateAreaLsdbType_Type()
)
axOspfv3AreaAggregateAreaLsdbType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    axOspfv3AreaAggregateAreaLsdbType.setStatus("current")
_AxOspfv3AreaAggregatePrefixType_Type = InetAddressType
_AxOspfv3AreaAggregatePrefixType_Object = MibTableColumn
axOspfv3AreaAggregatePrefixType = _AxOspfv3AreaAggregatePrefixType_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 15, 12, 1, 4),
    _AxOspfv3AreaAggregatePrefixType_Type()
)
axOspfv3AreaAggregatePrefixType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    axOspfv3AreaAggregatePrefixType.setStatus("current")
_AxOspfv3AreaAggregatePrefix_Type = InetAddress
_AxOspfv3AreaAggregatePrefix_Object = MibTableColumn
axOspfv3AreaAggregatePrefix = _AxOspfv3AreaAggregatePrefix_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 15, 12, 1, 5),
    _AxOspfv3AreaAggregatePrefix_Type()
)
axOspfv3AreaAggregatePrefix.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    axOspfv3AreaAggregatePrefix.setStatus("current")
_AxOspfv3AreaAggregatePrefixLength_Type = Integer32
_AxOspfv3AreaAggregatePrefixLength_Object = MibTableColumn
axOspfv3AreaAggregatePrefixLength = _AxOspfv3AreaAggregatePrefixLength_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 15, 12, 1, 6),
    _AxOspfv3AreaAggregatePrefixLength_Type()
)
axOspfv3AreaAggregatePrefixLength.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    axOspfv3AreaAggregatePrefixLength.setStatus("current")
_AxOspfv3AreaAggregateRowStatus_Type = RowStatus
_AxOspfv3AreaAggregateRowStatus_Object = MibTableColumn
axOspfv3AreaAggregateRowStatus = _AxOspfv3AreaAggregateRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 15, 12, 1, 7),
    _AxOspfv3AreaAggregateRowStatus_Type()
)
axOspfv3AreaAggregateRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    axOspfv3AreaAggregateRowStatus.setStatus("current")


class _AxOspfv3AreaAggregateEffect_Type(Integer32):
    """Custom type axOspfv3AreaAggregateEffect based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("advertiseMatching", 1),
          ("doNotAdvertiseMatching", 2))
    )


_AxOspfv3AreaAggregateEffect_Type.__name__ = "Integer32"
_AxOspfv3AreaAggregateEffect_Object = MibTableColumn
axOspfv3AreaAggregateEffect = _AxOspfv3AreaAggregateEffect_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 15, 12, 1, 8),
    _AxOspfv3AreaAggregateEffect_Type()
)
axOspfv3AreaAggregateEffect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axOspfv3AreaAggregateEffect.setStatus("current")
_AxOspfv3AreaAggregateRouteTag_Type = Unsigned32
_AxOspfv3AreaAggregateRouteTag_Object = MibTableColumn
axOspfv3AreaAggregateRouteTag = _AxOspfv3AreaAggregateRouteTag_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 15, 12, 1, 9),
    _AxOspfv3AreaAggregateRouteTag_Type()
)
axOspfv3AreaAggregateRouteTag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axOspfv3AreaAggregateRouteTag.setStatus("current")
_AxOspfv3Conformance_ObjectIdentity = ObjectIdentity
axOspfv3Conformance = _AxOspfv3Conformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 15, 1000)
)
_AxOspfv3Compliances_ObjectIdentity = ObjectIdentity
axOspfv3Compliances = _AxOspfv3Compliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 15, 1000, 1)
)
_AxOspfv3Groups_ObjectIdentity = ObjectIdentity
axOspfv3Groups = _AxOspfv3Groups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 15, 1000, 2)
)

# Managed Objects groups

axOspfv3Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 15, 1000, 2, 1)
)
axOspfv3Group.setObjects(
      *(("AX-OSPFV3-MIB", "axOspfv3GeneralDomainNumber"),
        ("AX-OSPFV3-MIB", "axOspfv3RouterId"),
        ("AX-OSPFV3-MIB", "axOspfv3AdminStatus"),
        ("AX-OSPFV3-MIB", "axOspfv3VersionNumber"),
        ("AX-OSPFV3-MIB", "axOspfv3AreaBdrRtrStatus"),
        ("AX-OSPFV3-MIB", "axOspfv3ASBdrRtrStatus"),
        ("AX-OSPFV3-MIB", "axOspfv3AsScopeLsaCount"),
        ("AX-OSPFV3-MIB", "axOspfv3AsScopeLsaCksumSum"),
        ("AX-OSPFV3-MIB", "axOspfv3OriginateNewLsas"),
        ("AX-OSPFV3-MIB", "axOspfv3RxNewLsas"),
        ("AX-OSPFV3-MIB", "axOspfv3ExtLsaCount"),
        ("AX-OSPFV3-MIB", "axOspfv3ExtAreaLsdbLimit"),
        ("AX-OSPFV3-MIB", "axOspfv3DemandExtensions"),
        ("AX-OSPFV3-MIB", "axOspfv3RestartSupport"),
        ("AX-OSPFV3-MIB", "axOspfv3RestartInterval"),
        ("AX-OSPFV3-MIB", "axOspfv3RestartStrictLsaChecking"),
        ("AX-OSPFV3-MIB", "axOspfv3AreaImportAsExtern"),
        ("AX-OSPFV3-MIB", "axOspfv3AreaSpfRuns"),
        ("AX-OSPFV3-MIB", "axOspfv3AreaBdrRtrCount"),
        ("AX-OSPFV3-MIB", "axOspfv3AreaAsBdrRtrCount"),
        ("AX-OSPFV3-MIB", "axOspfv3AreaScopeLsaCount"),
        ("AX-OSPFV3-MIB", "axOspfv3AreaScopeLsaCksumSum"),
        ("AX-OSPFV3-MIB", "axOspfv3AreaSummary"),
        ("AX-OSPFV3-MIB", "axOspfv3AreaRowStatus"),
        ("AX-OSPFV3-MIB", "axOspfv3AreaStubMetric"),
        ("AX-OSPFV3-MIB", "axOspfv3AreaStubMetricType"),
        ("AX-OSPFV3-MIB", "axOspfv3AreaTEEnabled"),
        ("AX-OSPFV3-MIB", "axOspfv3AsLsdbSequence"),
        ("AX-OSPFV3-MIB", "axOspfv3AsLsdbAge"),
        ("AX-OSPFV3-MIB", "axOspfv3AsLsdbChecksum"),
        ("AX-OSPFV3-MIB", "axOspfv3AsLsdbAdvertisement"),
        ("AX-OSPFV3-MIB", "axOspfv3AreaLsdbSequence"),
        ("AX-OSPFV3-MIB", "axOspfv3AreaLsdbAge"),
        ("AX-OSPFV3-MIB", "axOspfv3AreaLsdbChecksum"),
        ("AX-OSPFV3-MIB", "axOspfv3AreaLsdbAdvertisement"),
        ("AX-OSPFV3-MIB", "axOspfv3LinkLsdbSequence"),
        ("AX-OSPFV3-MIB", "axOspfv3LinkLsdbAge"),
        ("AX-OSPFV3-MIB", "axOspfv3LinkLsdbChecksum"),
        ("AX-OSPFV3-MIB", "axOspfv3LinkLsdbAdvertisement"),
        ("AX-OSPFV3-MIB", "axOspfv3IfAreaId"),
        ("AX-OSPFV3-MIB", "axOspfv3IfType"),
        ("AX-OSPFV3-MIB", "axOspfv3IfAdminStatus"),
        ("AX-OSPFV3-MIB", "axOspfv3IfRtrPriority"),
        ("AX-OSPFV3-MIB", "axOspfv3IfTransitDelay"),
        ("AX-OSPFV3-MIB", "axOspfv3IfRetransInterval"),
        ("AX-OSPFV3-MIB", "axOspfv3IfHelloInterval"),
        ("AX-OSPFV3-MIB", "axOspfv3IfRtrDeadInterval"),
        ("AX-OSPFV3-MIB", "axOspfv3IfPollInterval"),
        ("AX-OSPFV3-MIB", "axOspfv3IfState"),
        ("AX-OSPFV3-MIB", "axOspfv3IfDesignatedRouter"),
        ("AX-OSPFV3-MIB", "axOspfv3IfBackupDesignatedRouter"),
        ("AX-OSPFV3-MIB", "axOspfv3IfEvents"),
        ("AX-OSPFV3-MIB", "axOspfv3IfRowStatus"),
        ("AX-OSPFV3-MIB", "axOspfv3IfDemand"),
        ("AX-OSPFV3-MIB", "axOspfv3IfMetricValue"),
        ("AX-OSPFV3-MIB", "axOspfv3IfLinkScopeLsaCount"),
        ("AX-OSPFV3-MIB", "axOspfv3IfLinkLsaCksumSum"),
        ("AX-OSPFV3-MIB", "axOspfv3IfDemandNbrProbe"),
        ("AX-OSPFV3-MIB", "axOspfv3IfTEDisabled"),
        ("AX-OSPFV3-MIB", "axOspfv3IfLinkLSASuppression"),
        ("AX-OSPFV3-MIB", "axOspfv3VirtIfIndex"),
        ("AX-OSPFV3-MIB", "axOspfv3VirtIfInstId"),
        ("AX-OSPFV3-MIB", "axOspfv3VirtIfTransitDelay"),
        ("AX-OSPFV3-MIB", "axOspfv3VirtIfRetransInterval"),
        ("AX-OSPFV3-MIB", "axOspfv3VirtIfHelloInterval"),
        ("AX-OSPFV3-MIB", "axOspfv3VirtIfRtrDeadInterval"),
        ("AX-OSPFV3-MIB", "axOspfv3VirtIfState"),
        ("AX-OSPFV3-MIB", "axOspfv3VirtIfEvents"),
        ("AX-OSPFV3-MIB", "axOspfv3VirtIfRowStatus"),
        ("AX-OSPFV3-MIB", "axOspfv3VirtIfLinkScopeLsaCount"),
        ("AX-OSPFV3-MIB", "axOspfv3VirtIfLinkLsaCksumSum"),
        ("AX-OSPFV3-MIB", "axOspfv3NbrAddressType"),
        ("AX-OSPFV3-MIB", "axOspfv3NbrAddress"),
        ("AX-OSPFV3-MIB", "axOspfv3NbrOptions"),
        ("AX-OSPFV3-MIB", "axOspfv3NbrPriority"),
        ("AX-OSPFV3-MIB", "axOspfv3NbrState"),
        ("AX-OSPFV3-MIB", "axOspfv3NbrEvents"),
        ("AX-OSPFV3-MIB", "axOspfv3NbrLsRetransQLen"),
        ("AX-OSPFV3-MIB", "axOspfv3NbrHelloSuppressed"),
        ("AX-OSPFV3-MIB", "axOspfv3NbrIfId"),
        ("AX-OSPFV3-MIB", "axOspfv3NbrRestartHelperStatus"),
        ("AX-OSPFV3-MIB", "axOspfv3NbrRestartHelperExitReason"),
        ("AX-OSPFV3-MIB", "axOspfv3VirtNbrIfIndex"),
        ("AX-OSPFV3-MIB", "axOspfv3VirtNbrIfInstId"),
        ("AX-OSPFV3-MIB", "axOspfv3VirtNbrAddressType"),
        ("AX-OSPFV3-MIB", "axOspfv3VirtNbrAddress"),
        ("AX-OSPFV3-MIB", "axOspfv3VirtNbrOptions"),
        ("AX-OSPFV3-MIB", "axOspfv3VirtNbrState"),
        ("AX-OSPFV3-MIB", "axOspfv3VirtNbrEvents"),
        ("AX-OSPFV3-MIB", "axOspfv3VirtNbrLsRetransQLen"),
        ("AX-OSPFV3-MIB", "axOspfv3VirtNbrHelloSuppressed"),
        ("AX-OSPFV3-MIB", "axOspfv3VirtNbrIfId"),
        ("AX-OSPFV3-MIB", "axOspfv3VirtNbrRestartHelperStatus"),
        ("AX-OSPFV3-MIB", "axOspfv3VirtNbrRestartHelperExitReason"),
        ("AX-OSPFV3-MIB", "axOspfv3AreaAggregateRowStatus"),
        ("AX-OSPFV3-MIB", "axOspfv3AreaAggregateEffect"),
        ("AX-OSPFV3-MIB", "axOspfv3AreaAggregateRouteTag"))
)
if mibBuilder.loadTexts:
    axOspfv3Group.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

axOspfv3Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 15, 1000, 1, 1)
)
axOspfv3Compliance.setObjects(
    ("AX-OSPFV3-MIB", "axOspfv3Group")
)
if mibBuilder.loadTexts:
    axOspfv3Compliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "AX-OSPFV3-MIB",
    **{"axOspfv3": axOspfv3,
       "axOspfv3GeneralTable": axOspfv3GeneralTable,
       "axOspfv3GeneralEntry": axOspfv3GeneralEntry,
       "axOspfv3GeneralDomainNumber": axOspfv3GeneralDomainNumber,
       "axOspfv3RouterId": axOspfv3RouterId,
       "axOspfv3AdminStatus": axOspfv3AdminStatus,
       "axOspfv3VersionNumber": axOspfv3VersionNumber,
       "axOspfv3AreaBdrRtrStatus": axOspfv3AreaBdrRtrStatus,
       "axOspfv3ASBdrRtrStatus": axOspfv3ASBdrRtrStatus,
       "axOspfv3AsScopeLsaCount": axOspfv3AsScopeLsaCount,
       "axOspfv3AsScopeLsaCksumSum": axOspfv3AsScopeLsaCksumSum,
       "axOspfv3OriginateNewLsas": axOspfv3OriginateNewLsas,
       "axOspfv3RxNewLsas": axOspfv3RxNewLsas,
       "axOspfv3ExtLsaCount": axOspfv3ExtLsaCount,
       "axOspfv3ExtAreaLsdbLimit": axOspfv3ExtAreaLsdbLimit,
       "axOspfv3DemandExtensions": axOspfv3DemandExtensions,
       "axOspfv3RestartSupport": axOspfv3RestartSupport,
       "axOspfv3RestartInterval": axOspfv3RestartInterval,
       "axOspfv3RestartStrictLsaChecking": axOspfv3RestartStrictLsaChecking,
       "axOspfv3AreaTable": axOspfv3AreaTable,
       "axOspfv3AreaEntry": axOspfv3AreaEntry,
       "axOspfv3AreaDomainNumber": axOspfv3AreaDomainNumber,
       "axOspfv3AreaId": axOspfv3AreaId,
       "axOspfv3AreaImportAsExtern": axOspfv3AreaImportAsExtern,
       "axOspfv3AreaSpfRuns": axOspfv3AreaSpfRuns,
       "axOspfv3AreaBdrRtrCount": axOspfv3AreaBdrRtrCount,
       "axOspfv3AreaAsBdrRtrCount": axOspfv3AreaAsBdrRtrCount,
       "axOspfv3AreaScopeLsaCount": axOspfv3AreaScopeLsaCount,
       "axOspfv3AreaScopeLsaCksumSum": axOspfv3AreaScopeLsaCksumSum,
       "axOspfv3AreaSummary": axOspfv3AreaSummary,
       "axOspfv3AreaRowStatus": axOspfv3AreaRowStatus,
       "axOspfv3AreaStubMetric": axOspfv3AreaStubMetric,
       "axOspfv3AreaStubMetricType": axOspfv3AreaStubMetricType,
       "axOspfv3AreaTEEnabled": axOspfv3AreaTEEnabled,
       "axOspfv3AsLsdbTable": axOspfv3AsLsdbTable,
       "axOspfv3AsLsdbEntry": axOspfv3AsLsdbEntry,
       "axOspfv3AsLsdbDomainNumber": axOspfv3AsLsdbDomainNumber,
       "axOspfv3AsLsdbType": axOspfv3AsLsdbType,
       "axOspfv3AsLsdbRouterId": axOspfv3AsLsdbRouterId,
       "axOspfv3AsLsdbLsid": axOspfv3AsLsdbLsid,
       "axOspfv3AsLsdbSequence": axOspfv3AsLsdbSequence,
       "axOspfv3AsLsdbAge": axOspfv3AsLsdbAge,
       "axOspfv3AsLsdbChecksum": axOspfv3AsLsdbChecksum,
       "axOspfv3AsLsdbAdvertisement": axOspfv3AsLsdbAdvertisement,
       "axOspfv3AreaLsdbTable": axOspfv3AreaLsdbTable,
       "axOspfv3AreaLsdbEntry": axOspfv3AreaLsdbEntry,
       "axOspfv3AreaLsdbDomainNumber": axOspfv3AreaLsdbDomainNumber,
       "axOspfv3AreaLsdbAreaId": axOspfv3AreaLsdbAreaId,
       "axOspfv3AreaLsdbType": axOspfv3AreaLsdbType,
       "axOspfv3AreaLsdbRouterId": axOspfv3AreaLsdbRouterId,
       "axOspfv3AreaLsdbLsid": axOspfv3AreaLsdbLsid,
       "axOspfv3AreaLsdbSequence": axOspfv3AreaLsdbSequence,
       "axOspfv3AreaLsdbAge": axOspfv3AreaLsdbAge,
       "axOspfv3AreaLsdbChecksum": axOspfv3AreaLsdbChecksum,
       "axOspfv3AreaLsdbAdvertisement": axOspfv3AreaLsdbAdvertisement,
       "axOspfv3LinkLsdbTable": axOspfv3LinkLsdbTable,
       "axOspfv3LinkLsdbEntry": axOspfv3LinkLsdbEntry,
       "axOspfv3LinkLsdbDomainNumber": axOspfv3LinkLsdbDomainNumber,
       "axOspfv3LinkLsdbIfIndex": axOspfv3LinkLsdbIfIndex,
       "axOspfv3LinkLsdbIfInstId": axOspfv3LinkLsdbIfInstId,
       "axOspfv3LinkLsdbType": axOspfv3LinkLsdbType,
       "axOspfv3LinkLsdbRouterId": axOspfv3LinkLsdbRouterId,
       "axOspfv3LinkLsdbLsid": axOspfv3LinkLsdbLsid,
       "axOspfv3LinkLsdbSequence": axOspfv3LinkLsdbSequence,
       "axOspfv3LinkLsdbAge": axOspfv3LinkLsdbAge,
       "axOspfv3LinkLsdbChecksum": axOspfv3LinkLsdbChecksum,
       "axOspfv3LinkLsdbAdvertisement": axOspfv3LinkLsdbAdvertisement,
       "axOspfv3IfTable": axOspfv3IfTable,
       "axOspfv3IfEntry": axOspfv3IfEntry,
       "axOspfv3IfDomainNumber": axOspfv3IfDomainNumber,
       "axOspfv3IfIndex": axOspfv3IfIndex,
       "axOspfv3IfInstId": axOspfv3IfInstId,
       "axOspfv3IfAreaId": axOspfv3IfAreaId,
       "axOspfv3IfType": axOspfv3IfType,
       "axOspfv3IfAdminStatus": axOspfv3IfAdminStatus,
       "axOspfv3IfRtrPriority": axOspfv3IfRtrPriority,
       "axOspfv3IfTransitDelay": axOspfv3IfTransitDelay,
       "axOspfv3IfRetransInterval": axOspfv3IfRetransInterval,
       "axOspfv3IfHelloInterval": axOspfv3IfHelloInterval,
       "axOspfv3IfRtrDeadInterval": axOspfv3IfRtrDeadInterval,
       "axOspfv3IfPollInterval": axOspfv3IfPollInterval,
       "axOspfv3IfState": axOspfv3IfState,
       "axOspfv3IfDesignatedRouter": axOspfv3IfDesignatedRouter,
       "axOspfv3IfBackupDesignatedRouter": axOspfv3IfBackupDesignatedRouter,
       "axOspfv3IfEvents": axOspfv3IfEvents,
       "axOspfv3IfRowStatus": axOspfv3IfRowStatus,
       "axOspfv3IfDemand": axOspfv3IfDemand,
       "axOspfv3IfMetricValue": axOspfv3IfMetricValue,
       "axOspfv3IfLinkScopeLsaCount": axOspfv3IfLinkScopeLsaCount,
       "axOspfv3IfLinkLsaCksumSum": axOspfv3IfLinkLsaCksumSum,
       "axOspfv3IfDemandNbrProbe": axOspfv3IfDemandNbrProbe,
       "axOspfv3IfTEDisabled": axOspfv3IfTEDisabled,
       "axOspfv3IfLinkLSASuppression": axOspfv3IfLinkLSASuppression,
       "axOspfv3VirtIfTable": axOspfv3VirtIfTable,
       "axOspfv3VirtIfEntry": axOspfv3VirtIfEntry,
       "axOspfv3VirtIfDomainNumber": axOspfv3VirtIfDomainNumber,
       "axOspfv3VirtIfAreaId": axOspfv3VirtIfAreaId,
       "axOspfv3VirtIfNeighbor": axOspfv3VirtIfNeighbor,
       "axOspfv3VirtIfIndex": axOspfv3VirtIfIndex,
       "axOspfv3VirtIfInstId": axOspfv3VirtIfInstId,
       "axOspfv3VirtIfTransitDelay": axOspfv3VirtIfTransitDelay,
       "axOspfv3VirtIfRetransInterval": axOspfv3VirtIfRetransInterval,
       "axOspfv3VirtIfHelloInterval": axOspfv3VirtIfHelloInterval,
       "axOspfv3VirtIfRtrDeadInterval": axOspfv3VirtIfRtrDeadInterval,
       "axOspfv3VirtIfState": axOspfv3VirtIfState,
       "axOspfv3VirtIfEvents": axOspfv3VirtIfEvents,
       "axOspfv3VirtIfRowStatus": axOspfv3VirtIfRowStatus,
       "axOspfv3VirtIfLinkScopeLsaCount": axOspfv3VirtIfLinkScopeLsaCount,
       "axOspfv3VirtIfLinkLsaCksumSum": axOspfv3VirtIfLinkLsaCksumSum,
       "axOspfv3NbrTable": axOspfv3NbrTable,
       "axOspfv3NbrEntry": axOspfv3NbrEntry,
       "axOspfv3NbrDomainNumber": axOspfv3NbrDomainNumber,
       "axOspfv3NbrIfIndex": axOspfv3NbrIfIndex,
       "axOspfv3NbrIfInstId": axOspfv3NbrIfInstId,
       "axOspfv3NbrRtrId": axOspfv3NbrRtrId,
       "axOspfv3NbrAddressType": axOspfv3NbrAddressType,
       "axOspfv3NbrAddress": axOspfv3NbrAddress,
       "axOspfv3NbrOptions": axOspfv3NbrOptions,
       "axOspfv3NbrPriority": axOspfv3NbrPriority,
       "axOspfv3NbrState": axOspfv3NbrState,
       "axOspfv3NbrEvents": axOspfv3NbrEvents,
       "axOspfv3NbrLsRetransQLen": axOspfv3NbrLsRetransQLen,
       "axOspfv3NbrHelloSuppressed": axOspfv3NbrHelloSuppressed,
       "axOspfv3NbrIfId": axOspfv3NbrIfId,
       "axOspfv3NbrRestartHelperStatus": axOspfv3NbrRestartHelperStatus,
       "axOspfv3NbrRestartHelperExitReason": axOspfv3NbrRestartHelperExitReason,
       "axOspfv3VirtNbrTable": axOspfv3VirtNbrTable,
       "axOspfv3VirtNbrEntry": axOspfv3VirtNbrEntry,
       "axOspfv3VirtNbrDomainNumber": axOspfv3VirtNbrDomainNumber,
       "axOspfv3VirtNbrArea": axOspfv3VirtNbrArea,
       "axOspfv3VirtNbrRtrId": axOspfv3VirtNbrRtrId,
       "axOspfv3VirtNbrIfIndex": axOspfv3VirtNbrIfIndex,
       "axOspfv3VirtNbrIfInstId": axOspfv3VirtNbrIfInstId,
       "axOspfv3VirtNbrAddressType": axOspfv3VirtNbrAddressType,
       "axOspfv3VirtNbrAddress": axOspfv3VirtNbrAddress,
       "axOspfv3VirtNbrOptions": axOspfv3VirtNbrOptions,
       "axOspfv3VirtNbrState": axOspfv3VirtNbrState,
       "axOspfv3VirtNbrEvents": axOspfv3VirtNbrEvents,
       "axOspfv3VirtNbrLsRetransQLen": axOspfv3VirtNbrLsRetransQLen,
       "axOspfv3VirtNbrHelloSuppressed": axOspfv3VirtNbrHelloSuppressed,
       "axOspfv3VirtNbrIfId": axOspfv3VirtNbrIfId,
       "axOspfv3VirtNbrRestartHelperStatus": axOspfv3VirtNbrRestartHelperStatus,
       "axOspfv3VirtNbrRestartHelperExitReason": axOspfv3VirtNbrRestartHelperExitReason,
       "axOspfv3AreaAggregateTable": axOspfv3AreaAggregateTable,
       "axOspfv3AreaAggregateEntry": axOspfv3AreaAggregateEntry,
       "axOspfv3AreaAggregateDomainNumber": axOspfv3AreaAggregateDomainNumber,
       "axOspfv3AreaAggregateAreaID": axOspfv3AreaAggregateAreaID,
       "axOspfv3AreaAggregateAreaLsdbType": axOspfv3AreaAggregateAreaLsdbType,
       "axOspfv3AreaAggregatePrefixType": axOspfv3AreaAggregatePrefixType,
       "axOspfv3AreaAggregatePrefix": axOspfv3AreaAggregatePrefix,
       "axOspfv3AreaAggregatePrefixLength": axOspfv3AreaAggregatePrefixLength,
       "axOspfv3AreaAggregateRowStatus": axOspfv3AreaAggregateRowStatus,
       "axOspfv3AreaAggregateEffect": axOspfv3AreaAggregateEffect,
       "axOspfv3AreaAggregateRouteTag": axOspfv3AreaAggregateRouteTag,
       "axOspfv3Conformance": axOspfv3Conformance,
       "axOspfv3Compliances": axOspfv3Compliances,
       "axOspfv3Compliance": axOspfv3Compliance,
       "axOspfv3Groups": axOspfv3Groups,
       "axOspfv3Group": axOspfv3Group}
)
