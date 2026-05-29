# SNMP MIB module (AX-OSPF-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\alaxala\AX-OSPF-MIB

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

axOspf = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 14)
)
if mibBuilder.loadTexts:
    axOspf.setRevisions(
        ("2014-12-03 00:00",
         "2013-10-03 00:00",
         "2013-06-28 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class InterfaceIndexOrZero(TextualConvention, Integer32):
    status = "current"
    displayHint = "d"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )



class Status(TextualConvention, Integer32):
    status = "current"
    displayHint = "d"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )



# MIB Managed Objects in the order of their OIDs

_AxOspfGeneralTable_Object = MibTable
axOspfGeneralTable = _AxOspfGeneralTable_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 14, 1)
)
if mibBuilder.loadTexts:
    axOspfGeneralTable.setStatus("current")
_AxOspfGeneralEntry_Object = MibTableRow
axOspfGeneralEntry = _AxOspfGeneralEntry_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 14, 1, 1)
)
axOspfGeneralEntry.setIndexNames(
    (0, "AX-OSPF-MIB", "axOspfGeneralDomainNumber"),
)
if mibBuilder.loadTexts:
    axOspfGeneralEntry.setStatus("current")
_AxOspfGeneralDomainNumber_Type = Integer32
_AxOspfGeneralDomainNumber_Object = MibTableColumn
axOspfGeneralDomainNumber = _AxOspfGeneralDomainNumber_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 14, 1, 1, 1),
    _AxOspfGeneralDomainNumber_Type()
)
axOspfGeneralDomainNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axOspfGeneralDomainNumber.setStatus("current")
_AxOspfRouterId_Type = IpAddress
_AxOspfRouterId_Object = MibTableColumn
axOspfRouterId = _AxOspfRouterId_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 14, 1, 1, 2),
    _AxOspfRouterId_Type()
)
axOspfRouterId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axOspfRouterId.setStatus("current")
_AxOspfAdminStat_Type = Status
_AxOspfAdminStat_Object = MibTableColumn
axOspfAdminStat = _AxOspfAdminStat_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 14, 1, 1, 3),
    _AxOspfAdminStat_Type()
)
axOspfAdminStat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axOspfAdminStat.setStatus("current")


class _AxOspfVersionNumber_Type(Integer32):
    """Custom type axOspfVersionNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            2
        )
    )
    namedValues = NamedValues(
        ("version", 2)
    )


_AxOspfVersionNumber_Type.__name__ = "Integer32"
_AxOspfVersionNumber_Object = MibTableColumn
axOspfVersionNumber = _AxOspfVersionNumber_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 14, 1, 1, 4),
    _AxOspfVersionNumber_Type()
)
axOspfVersionNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axOspfVersionNumber.setStatus("current")


class _AxOspfAreaBdrRtrStatus_Type(Integer32):
    """Custom type axOspfAreaBdrRtrStatus based on Integer32"""
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


_AxOspfAreaBdrRtrStatus_Type.__name__ = "Integer32"
_AxOspfAreaBdrRtrStatus_Object = MibTableColumn
axOspfAreaBdrRtrStatus = _AxOspfAreaBdrRtrStatus_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 14, 1, 1, 5),
    _AxOspfAreaBdrRtrStatus_Type()
)
axOspfAreaBdrRtrStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axOspfAreaBdrRtrStatus.setStatus("current")


class _AxOspfASBdrRtrStatus_Type(Integer32):
    """Custom type axOspfASBdrRtrStatus based on Integer32"""
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


_AxOspfASBdrRtrStatus_Type.__name__ = "Integer32"
_AxOspfASBdrRtrStatus_Object = MibTableColumn
axOspfASBdrRtrStatus = _AxOspfASBdrRtrStatus_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 14, 1, 1, 6),
    _AxOspfASBdrRtrStatus_Type()
)
axOspfASBdrRtrStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axOspfASBdrRtrStatus.setStatus("current")
_AxOspfExternLsaCount_Type = Gauge32
_AxOspfExternLsaCount_Object = MibTableColumn
axOspfExternLsaCount = _AxOspfExternLsaCount_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 14, 1, 1, 7),
    _AxOspfExternLsaCount_Type()
)
axOspfExternLsaCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axOspfExternLsaCount.setStatus("current")
_AxOspfExternLsaCksumSum_Type = Integer32
_AxOspfExternLsaCksumSum_Object = MibTableColumn
axOspfExternLsaCksumSum = _AxOspfExternLsaCksumSum_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 14, 1, 1, 8),
    _AxOspfExternLsaCksumSum_Type()
)
axOspfExternLsaCksumSum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axOspfExternLsaCksumSum.setStatus("current")


class _AxOspfTOSSupport_Type(Integer32):
    """Custom type axOspfTOSSupport based on Integer32"""
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


_AxOspfTOSSupport_Type.__name__ = "Integer32"
_AxOspfTOSSupport_Object = MibTableColumn
axOspfTOSSupport = _AxOspfTOSSupport_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 14, 1, 1, 9),
    _AxOspfTOSSupport_Type()
)
axOspfTOSSupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axOspfTOSSupport.setStatus("current")
_AxOspfOriginateNewLsas_Type = Counter32
_AxOspfOriginateNewLsas_Object = MibTableColumn
axOspfOriginateNewLsas = _AxOspfOriginateNewLsas_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 14, 1, 1, 10),
    _AxOspfOriginateNewLsas_Type()
)
axOspfOriginateNewLsas.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axOspfOriginateNewLsas.setStatus("current")
_AxOspfRxNewLsas_Type = Counter32
_AxOspfRxNewLsas_Object = MibTableColumn
axOspfRxNewLsas = _AxOspfRxNewLsas_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 14, 1, 1, 11),
    _AxOspfRxNewLsas_Type()
)
axOspfRxNewLsas.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axOspfRxNewLsas.setStatus("current")
_AxOspfExtLsdbLimit_Type = Integer32
_AxOspfExtLsdbLimit_Object = MibTableColumn
axOspfExtLsdbLimit = _AxOspfExtLsdbLimit_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 14, 1, 1, 12),
    _AxOspfExtLsdbLimit_Type()
)
axOspfExtLsdbLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axOspfExtLsdbLimit.setStatus("current")
_AxOspfMulticastExtensions_Type = Integer32
_AxOspfMulticastExtensions_Object = MibTableColumn
axOspfMulticastExtensions = _AxOspfMulticastExtensions_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 14, 1, 1, 13),
    _AxOspfMulticastExtensions_Type()
)
axOspfMulticastExtensions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axOspfMulticastExtensions.setStatus("current")
_AxOspfAreaTable_Object = MibTable
axOspfAreaTable = _AxOspfAreaTable_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 14, 2)
)
if mibBuilder.loadTexts:
    axOspfAreaTable.setStatus("current")
_AxOspfAreaEntry_Object = MibTableRow
axOspfAreaEntry = _AxOspfAreaEntry_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 14, 2, 1)
)
axOspfAreaEntry.setIndexNames(
    (0, "AX-OSPF-MIB", "axOspfAreaDomainNumber"),
    (0, "AX-OSPF-MIB", "axOspfAreaId"),
)
if mibBuilder.loadTexts:
    axOspfAreaEntry.setStatus("current")
_AxOspfAreaDomainNumber_Type = Integer32
_AxOspfAreaDomainNumber_Object = MibTableColumn
axOspfAreaDomainNumber = _AxOspfAreaDomainNumber_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 14, 2, 1, 1),
    _AxOspfAreaDomainNumber_Type()
)
axOspfAreaDomainNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axOspfAreaDomainNumber.setStatus("current")
_AxOspfAreaId_Type = IpAddress
_AxOspfAreaId_Object = MibTableColumn
axOspfAreaId = _AxOspfAreaId_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 14, 2, 1, 2),
    _AxOspfAreaId_Type()
)
axOspfAreaId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axOspfAreaId.setStatus("current")


class _AxOspfAuthType_Type(Integer32):
    """Custom type axOspfAuthType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("simplePassword", 1),
          ("md5", 2))
    )


_AxOspfAuthType_Type.__name__ = "Integer32"
_AxOspfAuthType_Object = MibTableColumn
axOspfAuthType = _AxOspfAuthType_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 14, 2, 1, 3),
    _AxOspfAuthType_Type()
)
axOspfAuthType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axOspfAuthType.setStatus("current")


class _AxOspfImportAsExtern_Type(Integer32):
    """Custom type axOspfImportAsExtern based on Integer32"""
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


_AxOspfImportAsExtern_Type.__name__ = "Integer32"
_AxOspfImportAsExtern_Object = MibTableColumn
axOspfImportAsExtern = _AxOspfImportAsExtern_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 14, 2, 1, 4),
    _AxOspfImportAsExtern_Type()
)
axOspfImportAsExtern.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axOspfImportAsExtern.setStatus("current")
_AxOspfSpfRuns_Type = Counter32
_AxOspfSpfRuns_Object = MibTableColumn
axOspfSpfRuns = _AxOspfSpfRuns_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 14, 2, 1, 5),
    _AxOspfSpfRuns_Type()
)
axOspfSpfRuns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axOspfSpfRuns.setStatus("current")
_AxOspfAreaBdrRtrCount_Type = Gauge32
_AxOspfAreaBdrRtrCount_Object = MibTableColumn
axOspfAreaBdrRtrCount = _AxOspfAreaBdrRtrCount_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 14, 2, 1, 6),
    _AxOspfAreaBdrRtrCount_Type()
)
axOspfAreaBdrRtrCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axOspfAreaBdrRtrCount.setStatus("current")
_AxOspfAsBdrRtrCount_Type = Gauge32
_AxOspfAsBdrRtrCount_Object = MibTableColumn
axOspfAsBdrRtrCount = _AxOspfAsBdrRtrCount_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 14, 2, 1, 7),
    _AxOspfAsBdrRtrCount_Type()
)
axOspfAsBdrRtrCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axOspfAsBdrRtrCount.setStatus("current")
_AxOspfAreaLsaCount_Type = Gauge32
_AxOspfAreaLsaCount_Object = MibTableColumn
axOspfAreaLsaCount = _AxOspfAreaLsaCount_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 14, 2, 1, 8),
    _AxOspfAreaLsaCount_Type()
)
axOspfAreaLsaCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axOspfAreaLsaCount.setStatus("current")
_AxOspfAreaLsaCksumSum_Type = Integer32
_AxOspfAreaLsaCksumSum_Object = MibTableColumn
axOspfAreaLsaCksumSum = _AxOspfAreaLsaCksumSum_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 14, 2, 1, 9),
    _AxOspfAreaLsaCksumSum_Type()
)
axOspfAreaLsaCksumSum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axOspfAreaLsaCksumSum.setStatus("current")


class _AxOspfAreaSummary_Type(Integer32):
    """Custom type axOspfAreaSummary based on Integer32"""
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


_AxOspfAreaSummary_Type.__name__ = "Integer32"
_AxOspfAreaSummary_Object = MibTableColumn
axOspfAreaSummary = _AxOspfAreaSummary_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 14, 2, 1, 10),
    _AxOspfAreaSummary_Type()
)
axOspfAreaSummary.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axOspfAreaSummary.setStatus("current")
_AxOspfAreaStatus_Type = RowStatus
_AxOspfAreaStatus_Object = MibTableColumn
axOspfAreaStatus = _AxOspfAreaStatus_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 14, 2, 1, 11),
    _AxOspfAreaStatus_Type()
)
axOspfAreaStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    axOspfAreaStatus.setStatus("current")
_AxOspfStubAreaTable_Object = MibTable
axOspfStubAreaTable = _AxOspfStubAreaTable_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 14, 3)
)
if mibBuilder.loadTexts:
    axOspfStubAreaTable.setStatus("current")
_AxOspfStubAreaEntry_Object = MibTableRow
axOspfStubAreaEntry = _AxOspfStubAreaEntry_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 14, 3, 1)
)
axOspfStubAreaEntry.setIndexNames(
    (0, "AX-OSPF-MIB", "axOspfStubDomainNumber"),
    (0, "AX-OSPF-MIB", "axOspfStubAreaId"),
    (0, "AX-OSPF-MIB", "axOspfStubTOS"),
)
if mibBuilder.loadTexts:
    axOspfStubAreaEntry.setStatus("current")
_AxOspfStubDomainNumber_Type = Integer32
_AxOspfStubDomainNumber_Object = MibTableColumn
axOspfStubDomainNumber = _AxOspfStubDomainNumber_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 14, 3, 1, 1),
    _AxOspfStubDomainNumber_Type()
)
axOspfStubDomainNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axOspfStubDomainNumber.setStatus("current")
_AxOspfStubAreaId_Type = IpAddress
_AxOspfStubAreaId_Object = MibTableColumn
axOspfStubAreaId = _AxOspfStubAreaId_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 14, 3, 1, 2),
    _AxOspfStubAreaId_Type()
)
axOspfStubAreaId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axOspfStubAreaId.setStatus("current")
_AxOspfStubTOS_Type = Integer32
_AxOspfStubTOS_Object = MibTableColumn
axOspfStubTOS = _AxOspfStubTOS_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 14, 3, 1, 3),
    _AxOspfStubTOS_Type()
)
axOspfStubTOS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axOspfStubTOS.setStatus("current")
_AxOspfStubMetric_Type = Integer32
_AxOspfStubMetric_Object = MibTableColumn
axOspfStubMetric = _AxOspfStubMetric_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 14, 3, 1, 4),
    _AxOspfStubMetric_Type()
)
axOspfStubMetric.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axOspfStubMetric.setStatus("current")
_AxOspfStubStatus_Type = RowStatus
_AxOspfStubStatus_Object = MibTableColumn
axOspfStubStatus = _AxOspfStubStatus_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 14, 3, 1, 5),
    _AxOspfStubStatus_Type()
)
axOspfStubStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    axOspfStubStatus.setStatus("current")


class _AxOspfStubMetricType_Type(Integer32):
    """Custom type axOspfStubMetricType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("ospfMetric", 1),
          ("comparableCost", 2),
          ("nonComparable", 3))
    )


_AxOspfStubMetricType_Type.__name__ = "Integer32"
_AxOspfStubMetricType_Object = MibTableColumn
axOspfStubMetricType = _AxOspfStubMetricType_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 14, 3, 1, 6),
    _AxOspfStubMetricType_Type()
)
axOspfStubMetricType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axOspfStubMetricType.setStatus("current")
_AxOspfLsdbTable_Object = MibTable
axOspfLsdbTable = _AxOspfLsdbTable_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 14, 4)
)
if mibBuilder.loadTexts:
    axOspfLsdbTable.setStatus("current")
_AxOspfLsdbEntry_Object = MibTableRow
axOspfLsdbEntry = _AxOspfLsdbEntry_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 14, 4, 1)
)
axOspfLsdbEntry.setIndexNames(
    (0, "AX-OSPF-MIB", "axOspfLsdbDomainNumber"),
    (0, "AX-OSPF-MIB", "axOspfLsdbAreaId"),
    (0, "AX-OSPF-MIB", "axOspfLsdbType"),
    (0, "AX-OSPF-MIB", "axOspfLsdbLsid"),
    (0, "AX-OSPF-MIB", "axOspfLsdbRouterId"),
)
if mibBuilder.loadTexts:
    axOspfLsdbEntry.setStatus("current")
_AxOspfLsdbDomainNumber_Type = Integer32
_AxOspfLsdbDomainNumber_Object = MibTableColumn
axOspfLsdbDomainNumber = _AxOspfLsdbDomainNumber_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 14, 4, 1, 1),
    _AxOspfLsdbDomainNumber_Type()
)
axOspfLsdbDomainNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axOspfLsdbDomainNumber.setStatus("current")
_AxOspfLsdbAreaId_Type = IpAddress
_AxOspfLsdbAreaId_Object = MibTableColumn
axOspfLsdbAreaId = _AxOspfLsdbAreaId_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 14, 4, 1, 2),
    _AxOspfLsdbAreaId_Type()
)
axOspfLsdbAreaId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axOspfLsdbAreaId.setStatus("current")


class _AxOspfLsdbType_Type(Integer32):
    """Custom type axOspfLsdbType based on Integer32"""
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
              10)
        )
    )
    namedValues = NamedValues(
        *(("routerLink", 1),
          ("networkLink", 2),
          ("summaryLink", 3),
          ("asSummaryLink", 4),
          ("asExternalLink", 5),
          ("multicastLink", 6),
          ("nssaExternalLink", 7),
          ("areaOpaqueLink", 10))
    )


_AxOspfLsdbType_Type.__name__ = "Integer32"
_AxOspfLsdbType_Object = MibTableColumn
axOspfLsdbType = _AxOspfLsdbType_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 14, 4, 1, 3),
    _AxOspfLsdbType_Type()
)
axOspfLsdbType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axOspfLsdbType.setStatus("current")
_AxOspfLsdbLsid_Type = IpAddress
_AxOspfLsdbLsid_Object = MibTableColumn
axOspfLsdbLsid = _AxOspfLsdbLsid_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 14, 4, 1, 4),
    _AxOspfLsdbLsid_Type()
)
axOspfLsdbLsid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axOspfLsdbLsid.setStatus("current")
_AxOspfLsdbRouterId_Type = IpAddress
_AxOspfLsdbRouterId_Object = MibTableColumn
axOspfLsdbRouterId = _AxOspfLsdbRouterId_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 14, 4, 1, 5),
    _AxOspfLsdbRouterId_Type()
)
axOspfLsdbRouterId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axOspfLsdbRouterId.setStatus("current")
_AxOspfLsdbSequence_Type = Integer32
_AxOspfLsdbSequence_Object = MibTableColumn
axOspfLsdbSequence = _AxOspfLsdbSequence_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 14, 4, 1, 6),
    _AxOspfLsdbSequence_Type()
)
axOspfLsdbSequence.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axOspfLsdbSequence.setStatus("current")
_AxOspfLsdbAge_Type = Integer32
_AxOspfLsdbAge_Object = MibTableColumn
axOspfLsdbAge = _AxOspfLsdbAge_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 14, 4, 1, 7),
    _AxOspfLsdbAge_Type()
)
axOspfLsdbAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axOspfLsdbAge.setStatus("current")
_AxOspfLsdbChecksum_Type = Integer32
_AxOspfLsdbChecksum_Object = MibTableColumn
axOspfLsdbChecksum = _AxOspfLsdbChecksum_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 14, 4, 1, 8),
    _AxOspfLsdbChecksum_Type()
)
axOspfLsdbChecksum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axOspfLsdbChecksum.setStatus("current")
_AxOspfLsdbAdvertisement_Type = OctetString
_AxOspfLsdbAdvertisement_Object = MibTableColumn
axOspfLsdbAdvertisement = _AxOspfLsdbAdvertisement_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 14, 4, 1, 9),
    _AxOspfLsdbAdvertisement_Type()
)
axOspfLsdbAdvertisement.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axOspfLsdbAdvertisement.setStatus("current")
_AxOspfAreaRangeTable_Object = MibTable
axOspfAreaRangeTable = _AxOspfAreaRangeTable_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 14, 5)
)
if mibBuilder.loadTexts:
    axOspfAreaRangeTable.setStatus("current")
_AxOspfAreaRangeEntry_Object = MibTableRow
axOspfAreaRangeEntry = _AxOspfAreaRangeEntry_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 14, 5, 1)
)
axOspfAreaRangeEntry.setIndexNames(
    (0, "AX-OSPF-MIB", "axOspfAreaRangeDomainNumber"),
    (0, "AX-OSPF-MIB", "axOspfAreaRangeAreaId"),
    (0, "AX-OSPF-MIB", "axOspfAreaRangeNet"),
)
if mibBuilder.loadTexts:
    axOspfAreaRangeEntry.setStatus("current")
_AxOspfAreaRangeDomainNumber_Type = Integer32
_AxOspfAreaRangeDomainNumber_Object = MibTableColumn
axOspfAreaRangeDomainNumber = _AxOspfAreaRangeDomainNumber_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 14, 5, 1, 1),
    _AxOspfAreaRangeDomainNumber_Type()
)
axOspfAreaRangeDomainNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axOspfAreaRangeDomainNumber.setStatus("current")
_AxOspfAreaRangeAreaId_Type = IpAddress
_AxOspfAreaRangeAreaId_Object = MibTableColumn
axOspfAreaRangeAreaId = _AxOspfAreaRangeAreaId_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 14, 5, 1, 2),
    _AxOspfAreaRangeAreaId_Type()
)
axOspfAreaRangeAreaId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axOspfAreaRangeAreaId.setStatus("current")
_AxOspfAreaRangeNet_Type = IpAddress
_AxOspfAreaRangeNet_Object = MibTableColumn
axOspfAreaRangeNet = _AxOspfAreaRangeNet_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 14, 5, 1, 3),
    _AxOspfAreaRangeNet_Type()
)
axOspfAreaRangeNet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axOspfAreaRangeNet.setStatus("current")
_AxOspfAreaRangeMask_Type = IpAddress
_AxOspfAreaRangeMask_Object = MibTableColumn
axOspfAreaRangeMask = _AxOspfAreaRangeMask_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 14, 5, 1, 4),
    _AxOspfAreaRangeMask_Type()
)
axOspfAreaRangeMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axOspfAreaRangeMask.setStatus("current")
_AxOspfAreaRangeStatus_Type = RowStatus
_AxOspfAreaRangeStatus_Object = MibTableColumn
axOspfAreaRangeStatus = _AxOspfAreaRangeStatus_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 14, 5, 1, 5),
    _AxOspfAreaRangeStatus_Type()
)
axOspfAreaRangeStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    axOspfAreaRangeStatus.setStatus("current")


class _AxOspfAreaRangeEffect_Type(Integer32):
    """Custom type axOspfAreaRangeEffect based on Integer32"""
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


_AxOspfAreaRangeEffect_Type.__name__ = "Integer32"
_AxOspfAreaRangeEffect_Object = MibTableColumn
axOspfAreaRangeEffect = _AxOspfAreaRangeEffect_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 14, 5, 1, 6),
    _AxOspfAreaRangeEffect_Type()
)
axOspfAreaRangeEffect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axOspfAreaRangeEffect.setStatus("current")
_AxOspfIfTable_Object = MibTable
axOspfIfTable = _AxOspfIfTable_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 14, 7)
)
if mibBuilder.loadTexts:
    axOspfIfTable.setStatus("current")
_AxOspfIfEntry_Object = MibTableRow
axOspfIfEntry = _AxOspfIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 14, 7, 1)
)
axOspfIfEntry.setIndexNames(
    (0, "AX-OSPF-MIB", "axOspfIfDomainNumber"),
    (0, "AX-OSPF-MIB", "axOspfIfIpAddress"),
    (0, "AX-OSPF-MIB", "axOspfAddressLessIf"),
)
if mibBuilder.loadTexts:
    axOspfIfEntry.setStatus("current")
_AxOspfIfDomainNumber_Type = Integer32
_AxOspfIfDomainNumber_Object = MibTableColumn
axOspfIfDomainNumber = _AxOspfIfDomainNumber_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 14, 7, 1, 1),
    _AxOspfIfDomainNumber_Type()
)
axOspfIfDomainNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axOspfIfDomainNumber.setStatus("current")
_AxOspfIfIpAddress_Type = IpAddress
_AxOspfIfIpAddress_Object = MibTableColumn
axOspfIfIpAddress = _AxOspfIfIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 14, 7, 1, 2),
    _AxOspfIfIpAddress_Type()
)
axOspfIfIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axOspfIfIpAddress.setStatus("current")
_AxOspfAddressLessIf_Type = InterfaceIndexOrZero
_AxOspfAddressLessIf_Object = MibTableColumn
axOspfAddressLessIf = _AxOspfAddressLessIf_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 14, 7, 1, 3),
    _AxOspfAddressLessIf_Type()
)
axOspfAddressLessIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axOspfAddressLessIf.setStatus("current")
_AxOspfIfAreaId_Type = IpAddress
_AxOspfIfAreaId_Object = MibTableColumn
axOspfIfAreaId = _AxOspfIfAreaId_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 14, 7, 1, 4),
    _AxOspfIfAreaId_Type()
)
axOspfIfAreaId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axOspfIfAreaId.setStatus("current")


class _AxOspfIfType_Type(Integer32):
    """Custom type axOspfIfType based on Integer32"""
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


_AxOspfIfType_Type.__name__ = "Integer32"
_AxOspfIfType_Object = MibTableColumn
axOspfIfType = _AxOspfIfType_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 14, 7, 1, 5),
    _AxOspfIfType_Type()
)
axOspfIfType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axOspfIfType.setStatus("current")
_AxOspfIfAdminStat_Type = Status
_AxOspfIfAdminStat_Object = MibTableColumn
axOspfIfAdminStat = _AxOspfIfAdminStat_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 14, 7, 1, 6),
    _AxOspfIfAdminStat_Type()
)
axOspfIfAdminStat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axOspfIfAdminStat.setStatus("current")
_AxOspfIfRtrPriority_Type = Integer32
_AxOspfIfRtrPriority_Object = MibTableColumn
axOspfIfRtrPriority = _AxOspfIfRtrPriority_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 14, 7, 1, 7),
    _AxOspfIfRtrPriority_Type()
)
axOspfIfRtrPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axOspfIfRtrPriority.setStatus("current")
_AxOspfIfTransitDelay_Type = Integer32
_AxOspfIfTransitDelay_Object = MibTableColumn
axOspfIfTransitDelay = _AxOspfIfTransitDelay_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 14, 7, 1, 8),
    _AxOspfIfTransitDelay_Type()
)
axOspfIfTransitDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axOspfIfTransitDelay.setStatus("current")
_AxOspfIfRetransInterval_Type = Integer32
_AxOspfIfRetransInterval_Object = MibTableColumn
axOspfIfRetransInterval = _AxOspfIfRetransInterval_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 14, 7, 1, 9),
    _AxOspfIfRetransInterval_Type()
)
axOspfIfRetransInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axOspfIfRetransInterval.setStatus("current")
_AxOspfIfHelloInterval_Type = Integer32
_AxOspfIfHelloInterval_Object = MibTableColumn
axOspfIfHelloInterval = _AxOspfIfHelloInterval_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 14, 7, 1, 10),
    _AxOspfIfHelloInterval_Type()
)
axOspfIfHelloInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axOspfIfHelloInterval.setStatus("current")
_AxOspfIfRtrDeadInterval_Type = Integer32
_AxOspfIfRtrDeadInterval_Object = MibTableColumn
axOspfIfRtrDeadInterval = _AxOspfIfRtrDeadInterval_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 14, 7, 1, 11),
    _AxOspfIfRtrDeadInterval_Type()
)
axOspfIfRtrDeadInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axOspfIfRtrDeadInterval.setStatus("current")
_AxOspfIfPollInterval_Type = Integer32
_AxOspfIfPollInterval_Object = MibTableColumn
axOspfIfPollInterval = _AxOspfIfPollInterval_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 14, 7, 1, 12),
    _AxOspfIfPollInterval_Type()
)
axOspfIfPollInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axOspfIfPollInterval.setStatus("current")


class _AxOspfIfState_Type(Integer32):
    """Custom type axOspfIfState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("down", 1),
          ("loopback", 2),
          ("waiting", 3),
          ("pointToPoint", 4),
          ("designatedRouter", 5),
          ("backupDesignatedRouter", 6),
          ("otherDesignatedRouter", 7))
    )


_AxOspfIfState_Type.__name__ = "Integer32"
_AxOspfIfState_Object = MibTableColumn
axOspfIfState = _AxOspfIfState_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 14, 7, 1, 13),
    _AxOspfIfState_Type()
)
axOspfIfState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axOspfIfState.setStatus("current")
_AxOspfIfDesignatedRouter_Type = IpAddress
_AxOspfIfDesignatedRouter_Object = MibTableColumn
axOspfIfDesignatedRouter = _AxOspfIfDesignatedRouter_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 14, 7, 1, 14),
    _AxOspfIfDesignatedRouter_Type()
)
axOspfIfDesignatedRouter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axOspfIfDesignatedRouter.setStatus("current")
_AxOspfIfBackupDesignatedRouter_Type = IpAddress
_AxOspfIfBackupDesignatedRouter_Object = MibTableColumn
axOspfIfBackupDesignatedRouter = _AxOspfIfBackupDesignatedRouter_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 14, 7, 1, 15),
    _AxOspfIfBackupDesignatedRouter_Type()
)
axOspfIfBackupDesignatedRouter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axOspfIfBackupDesignatedRouter.setStatus("current")
_AxOspfIfEvents_Type = Counter32
_AxOspfIfEvents_Object = MibTableColumn
axOspfIfEvents = _AxOspfIfEvents_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 14, 7, 1, 16),
    _AxOspfIfEvents_Type()
)
axOspfIfEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axOspfIfEvents.setStatus("current")
_AxOspfIfAuthKey_Type = OctetString
_AxOspfIfAuthKey_Object = MibTableColumn
axOspfIfAuthKey = _AxOspfIfAuthKey_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 14, 7, 1, 17),
    _AxOspfIfAuthKey_Type()
)
axOspfIfAuthKey.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axOspfIfAuthKey.setStatus("current")
_AxOspfIfStatus_Type = RowStatus
_AxOspfIfStatus_Object = MibTableColumn
axOspfIfStatus = _AxOspfIfStatus_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 14, 7, 1, 18),
    _AxOspfIfStatus_Type()
)
axOspfIfStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    axOspfIfStatus.setStatus("current")


class _AxOspfIfMulticastForwarding_Type(Integer32):
    """Custom type axOspfIfMulticastForwarding based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("blocked", 1),
          ("multicast", 2),
          ("unicast", 3))
    )


_AxOspfIfMulticastForwarding_Type.__name__ = "Integer32"
_AxOspfIfMulticastForwarding_Object = MibTableColumn
axOspfIfMulticastForwarding = _AxOspfIfMulticastForwarding_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 14, 7, 1, 19),
    _AxOspfIfMulticastForwarding_Type()
)
axOspfIfMulticastForwarding.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axOspfIfMulticastForwarding.setStatus("current")
_AxOspfIfMetricTable_Object = MibTable
axOspfIfMetricTable = _AxOspfIfMetricTable_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 14, 8)
)
if mibBuilder.loadTexts:
    axOspfIfMetricTable.setStatus("current")
_AxOspfIfMetricEntry_Object = MibTableRow
axOspfIfMetricEntry = _AxOspfIfMetricEntry_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 14, 8, 1)
)
axOspfIfMetricEntry.setIndexNames(
    (0, "AX-OSPF-MIB", "axOspfIfMetricDomainNumber"),
    (0, "AX-OSPF-MIB", "axOspfIfMetricIpAddress"),
    (0, "AX-OSPF-MIB", "axOspfIfMetricAddressLessIf"),
    (0, "AX-OSPF-MIB", "axOspfIfMetricTOS"),
)
if mibBuilder.loadTexts:
    axOspfIfMetricEntry.setStatus("current")
_AxOspfIfMetricDomainNumber_Type = Integer32
_AxOspfIfMetricDomainNumber_Object = MibTableColumn
axOspfIfMetricDomainNumber = _AxOspfIfMetricDomainNumber_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 14, 8, 1, 1),
    _AxOspfIfMetricDomainNumber_Type()
)
axOspfIfMetricDomainNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axOspfIfMetricDomainNumber.setStatus("current")
_AxOspfIfMetricIpAddress_Type = IpAddress
_AxOspfIfMetricIpAddress_Object = MibTableColumn
axOspfIfMetricIpAddress = _AxOspfIfMetricIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 14, 8, 1, 2),
    _AxOspfIfMetricIpAddress_Type()
)
axOspfIfMetricIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axOspfIfMetricIpAddress.setStatus("current")
_AxOspfIfMetricAddressLessIf_Type = InterfaceIndexOrZero
_AxOspfIfMetricAddressLessIf_Object = MibTableColumn
axOspfIfMetricAddressLessIf = _AxOspfIfMetricAddressLessIf_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 14, 8, 1, 3),
    _AxOspfIfMetricAddressLessIf_Type()
)
axOspfIfMetricAddressLessIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axOspfIfMetricAddressLessIf.setStatus("current")
_AxOspfIfMetricTOS_Type = Integer32
_AxOspfIfMetricTOS_Object = MibTableColumn
axOspfIfMetricTOS = _AxOspfIfMetricTOS_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 14, 8, 1, 4),
    _AxOspfIfMetricTOS_Type()
)
axOspfIfMetricTOS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axOspfIfMetricTOS.setStatus("current")
_AxOspfIfMetricValue_Type = Integer32
_AxOspfIfMetricValue_Object = MibTableColumn
axOspfIfMetricValue = _AxOspfIfMetricValue_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 14, 8, 1, 5),
    _AxOspfIfMetricValue_Type()
)
axOspfIfMetricValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axOspfIfMetricValue.setStatus("current")
_AxOspfIfMetricStatus_Type = RowStatus
_AxOspfIfMetricStatus_Object = MibTableColumn
axOspfIfMetricStatus = _AxOspfIfMetricStatus_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 14, 8, 1, 6),
    _AxOspfIfMetricStatus_Type()
)
axOspfIfMetricStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    axOspfIfMetricStatus.setStatus("current")
_AxOspfVirtIfTable_Object = MibTable
axOspfVirtIfTable = _AxOspfVirtIfTable_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 14, 9)
)
if mibBuilder.loadTexts:
    axOspfVirtIfTable.setStatus("current")
_AxOspfVirtIfEntry_Object = MibTableRow
axOspfVirtIfEntry = _AxOspfVirtIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 14, 9, 1)
)
axOspfVirtIfEntry.setIndexNames(
    (0, "AX-OSPF-MIB", "axOspfVirtIfDomainNumber"),
    (0, "AX-OSPF-MIB", "axOspfVirtIfAreaId"),
    (0, "AX-OSPF-MIB", "axOspfVirtIfNeighbor"),
)
if mibBuilder.loadTexts:
    axOspfVirtIfEntry.setStatus("current")
_AxOspfVirtIfDomainNumber_Type = Integer32
_AxOspfVirtIfDomainNumber_Object = MibTableColumn
axOspfVirtIfDomainNumber = _AxOspfVirtIfDomainNumber_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 14, 9, 1, 1),
    _AxOspfVirtIfDomainNumber_Type()
)
axOspfVirtIfDomainNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axOspfVirtIfDomainNumber.setStatus("current")
_AxOspfVirtIfAreaId_Type = IpAddress
_AxOspfVirtIfAreaId_Object = MibTableColumn
axOspfVirtIfAreaId = _AxOspfVirtIfAreaId_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 14, 9, 1, 2),
    _AxOspfVirtIfAreaId_Type()
)
axOspfVirtIfAreaId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axOspfVirtIfAreaId.setStatus("current")
_AxOspfVirtIfNeighbor_Type = IpAddress
_AxOspfVirtIfNeighbor_Object = MibTableColumn
axOspfVirtIfNeighbor = _AxOspfVirtIfNeighbor_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 14, 9, 1, 3),
    _AxOspfVirtIfNeighbor_Type()
)
axOspfVirtIfNeighbor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axOspfVirtIfNeighbor.setStatus("current")
_AxOspfVirtIfTransitDelay_Type = Integer32
_AxOspfVirtIfTransitDelay_Object = MibTableColumn
axOspfVirtIfTransitDelay = _AxOspfVirtIfTransitDelay_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 14, 9, 1, 4),
    _AxOspfVirtIfTransitDelay_Type()
)
axOspfVirtIfTransitDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axOspfVirtIfTransitDelay.setStatus("current")
_AxOspfVirtIfRetransInterval_Type = Integer32
_AxOspfVirtIfRetransInterval_Object = MibTableColumn
axOspfVirtIfRetransInterval = _AxOspfVirtIfRetransInterval_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 14, 9, 1, 5),
    _AxOspfVirtIfRetransInterval_Type()
)
axOspfVirtIfRetransInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axOspfVirtIfRetransInterval.setStatus("current")
_AxOspfVirtIfHelloInterval_Type = Integer32
_AxOspfVirtIfHelloInterval_Object = MibTableColumn
axOspfVirtIfHelloInterval = _AxOspfVirtIfHelloInterval_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 14, 9, 1, 6),
    _AxOspfVirtIfHelloInterval_Type()
)
axOspfVirtIfHelloInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axOspfVirtIfHelloInterval.setStatus("current")
_AxOspfVirtIfRtrDeadInterval_Type = Integer32
_AxOspfVirtIfRtrDeadInterval_Object = MibTableColumn
axOspfVirtIfRtrDeadInterval = _AxOspfVirtIfRtrDeadInterval_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 14, 9, 1, 7),
    _AxOspfVirtIfRtrDeadInterval_Type()
)
axOspfVirtIfRtrDeadInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axOspfVirtIfRtrDeadInterval.setStatus("current")


class _AxOspfVirtIfState_Type(Integer32):
    """Custom type axOspfVirtIfState based on Integer32"""
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


_AxOspfVirtIfState_Type.__name__ = "Integer32"
_AxOspfVirtIfState_Object = MibTableColumn
axOspfVirtIfState = _AxOspfVirtIfState_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 14, 9, 1, 8),
    _AxOspfVirtIfState_Type()
)
axOspfVirtIfState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axOspfVirtIfState.setStatus("current")
_AxOspfVirtIfEvents_Type = Counter32
_AxOspfVirtIfEvents_Object = MibTableColumn
axOspfVirtIfEvents = _AxOspfVirtIfEvents_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 14, 9, 1, 9),
    _AxOspfVirtIfEvents_Type()
)
axOspfVirtIfEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axOspfVirtIfEvents.setStatus("current")
_AxOspfVirtIfAuthKey_Type = OctetString
_AxOspfVirtIfAuthKey_Object = MibTableColumn
axOspfVirtIfAuthKey = _AxOspfVirtIfAuthKey_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 14, 9, 1, 10),
    _AxOspfVirtIfAuthKey_Type()
)
axOspfVirtIfAuthKey.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axOspfVirtIfAuthKey.setStatus("current")
_AxOspfVirtIfStatus_Type = RowStatus
_AxOspfVirtIfStatus_Object = MibTableColumn
axOspfVirtIfStatus = _AxOspfVirtIfStatus_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 14, 9, 1, 11),
    _AxOspfVirtIfStatus_Type()
)
axOspfVirtIfStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    axOspfVirtIfStatus.setStatus("current")
_AxOspfNbrTable_Object = MibTable
axOspfNbrTable = _AxOspfNbrTable_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 14, 10)
)
if mibBuilder.loadTexts:
    axOspfNbrTable.setStatus("current")
_AxOspfNbrEntry_Object = MibTableRow
axOspfNbrEntry = _AxOspfNbrEntry_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 14, 10, 1)
)
axOspfNbrEntry.setIndexNames(
    (0, "AX-OSPF-MIB", "axOspfNbrDomainNumber"),
    (0, "AX-OSPF-MIB", "axOspfNbrIpAddr"),
    (0, "AX-OSPF-MIB", "axOspfNbrAddressLessIndex"),
)
if mibBuilder.loadTexts:
    axOspfNbrEntry.setStatus("current")
_AxOspfNbrDomainNumber_Type = Integer32
_AxOspfNbrDomainNumber_Object = MibTableColumn
axOspfNbrDomainNumber = _AxOspfNbrDomainNumber_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 14, 10, 1, 1),
    _AxOspfNbrDomainNumber_Type()
)
axOspfNbrDomainNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axOspfNbrDomainNumber.setStatus("current")
_AxOspfNbrIpAddr_Type = IpAddress
_AxOspfNbrIpAddr_Object = MibTableColumn
axOspfNbrIpAddr = _AxOspfNbrIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 14, 10, 1, 2),
    _AxOspfNbrIpAddr_Type()
)
axOspfNbrIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axOspfNbrIpAddr.setStatus("current")
_AxOspfNbrAddressLessIndex_Type = InterfaceIndexOrZero
_AxOspfNbrAddressLessIndex_Object = MibTableColumn
axOspfNbrAddressLessIndex = _AxOspfNbrAddressLessIndex_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 14, 10, 1, 3),
    _AxOspfNbrAddressLessIndex_Type()
)
axOspfNbrAddressLessIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axOspfNbrAddressLessIndex.setStatus("current")
_AxOspfNbrRtrId_Type = IpAddress
_AxOspfNbrRtrId_Object = MibTableColumn
axOspfNbrRtrId = _AxOspfNbrRtrId_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 14, 10, 1, 4),
    _AxOspfNbrRtrId_Type()
)
axOspfNbrRtrId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axOspfNbrRtrId.setStatus("current")
_AxOspfNbrOptions_Type = Integer32
_AxOspfNbrOptions_Object = MibTableColumn
axOspfNbrOptions = _AxOspfNbrOptions_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 14, 10, 1, 5),
    _AxOspfNbrOptions_Type()
)
axOspfNbrOptions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axOspfNbrOptions.setStatus("current")
_AxOspfNbrPriority_Type = Integer32
_AxOspfNbrPriority_Object = MibTableColumn
axOspfNbrPriority = _AxOspfNbrPriority_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 14, 10, 1, 6),
    _AxOspfNbrPriority_Type()
)
axOspfNbrPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axOspfNbrPriority.setStatus("current")


class _AxOspfNbrState_Type(Integer32):
    """Custom type axOspfNbrState based on Integer32"""
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


_AxOspfNbrState_Type.__name__ = "Integer32"
_AxOspfNbrState_Object = MibTableColumn
axOspfNbrState = _AxOspfNbrState_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 14, 10, 1, 7),
    _AxOspfNbrState_Type()
)
axOspfNbrState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axOspfNbrState.setStatus("current")
_AxOspfNbrEvents_Type = Counter32
_AxOspfNbrEvents_Object = MibTableColumn
axOspfNbrEvents = _AxOspfNbrEvents_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 14, 10, 1, 8),
    _AxOspfNbrEvents_Type()
)
axOspfNbrEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axOspfNbrEvents.setStatus("current")
_AxOspfNbrLsRetransQLen_Type = Gauge32
_AxOspfNbrLsRetransQLen_Object = MibTableColumn
axOspfNbrLsRetransQLen = _AxOspfNbrLsRetransQLen_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 14, 10, 1, 9),
    _AxOspfNbrLsRetransQLen_Type()
)
axOspfNbrLsRetransQLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axOspfNbrLsRetransQLen.setStatus("current")
_AxOspfNbmaNbrStatus_Type = RowStatus
_AxOspfNbmaNbrStatus_Object = MibTableColumn
axOspfNbmaNbrStatus = _AxOspfNbmaNbrStatus_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 14, 10, 1, 10),
    _AxOspfNbmaNbrStatus_Type()
)
axOspfNbmaNbrStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    axOspfNbmaNbrStatus.setStatus("current")


class _AxOspfNbmaNbrPermanence_Type(Integer32):
    """Custom type axOspfNbmaNbrPermanence based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dynamic", 1),
          ("permanent", 2))
    )


_AxOspfNbmaNbrPermanence_Type.__name__ = "Integer32"
_AxOspfNbmaNbrPermanence_Object = MibTableColumn
axOspfNbmaNbrPermanence = _AxOspfNbmaNbrPermanence_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 14, 10, 1, 11),
    _AxOspfNbmaNbrPermanence_Type()
)
axOspfNbmaNbrPermanence.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axOspfNbmaNbrPermanence.setStatus("current")
_AxOspfVirtNbrTable_Object = MibTable
axOspfVirtNbrTable = _AxOspfVirtNbrTable_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 14, 11)
)
if mibBuilder.loadTexts:
    axOspfVirtNbrTable.setStatus("current")
_AxOspfVirtNbrEntry_Object = MibTableRow
axOspfVirtNbrEntry = _AxOspfVirtNbrEntry_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 14, 11, 1)
)
axOspfVirtNbrEntry.setIndexNames(
    (0, "AX-OSPF-MIB", "axOspfVirtNbrDomainNumber"),
    (0, "AX-OSPF-MIB", "axOspfVirtNbrArea"),
    (0, "AX-OSPF-MIB", "axOspfVirtNbrRtrId"),
)
if mibBuilder.loadTexts:
    axOspfVirtNbrEntry.setStatus("current")
_AxOspfVirtNbrDomainNumber_Type = Integer32
_AxOspfVirtNbrDomainNumber_Object = MibTableColumn
axOspfVirtNbrDomainNumber = _AxOspfVirtNbrDomainNumber_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 14, 11, 1, 1),
    _AxOspfVirtNbrDomainNumber_Type()
)
axOspfVirtNbrDomainNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axOspfVirtNbrDomainNumber.setStatus("current")
_AxOspfVirtNbrArea_Type = IpAddress
_AxOspfVirtNbrArea_Object = MibTableColumn
axOspfVirtNbrArea = _AxOspfVirtNbrArea_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 14, 11, 1, 2),
    _AxOspfVirtNbrArea_Type()
)
axOspfVirtNbrArea.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axOspfVirtNbrArea.setStatus("current")
_AxOspfVirtNbrRtrId_Type = IpAddress
_AxOspfVirtNbrRtrId_Object = MibTableColumn
axOspfVirtNbrRtrId = _AxOspfVirtNbrRtrId_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 14, 11, 1, 3),
    _AxOspfVirtNbrRtrId_Type()
)
axOspfVirtNbrRtrId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axOspfVirtNbrRtrId.setStatus("current")
_AxOspfVirtNbrIpAddr_Type = IpAddress
_AxOspfVirtNbrIpAddr_Object = MibTableColumn
axOspfVirtNbrIpAddr = _AxOspfVirtNbrIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 14, 11, 1, 4),
    _AxOspfVirtNbrIpAddr_Type()
)
axOspfVirtNbrIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axOspfVirtNbrIpAddr.setStatus("current")
_AxOspfVirtNbrOptions_Type = Integer32
_AxOspfVirtNbrOptions_Object = MibTableColumn
axOspfVirtNbrOptions = _AxOspfVirtNbrOptions_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 14, 11, 1, 5),
    _AxOspfVirtNbrOptions_Type()
)
axOspfVirtNbrOptions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axOspfVirtNbrOptions.setStatus("current")


class _AxOspfVirtNbrState_Type(Integer32):
    """Custom type axOspfVirtNbrState based on Integer32"""
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


_AxOspfVirtNbrState_Type.__name__ = "Integer32"
_AxOspfVirtNbrState_Object = MibTableColumn
axOspfVirtNbrState = _AxOspfVirtNbrState_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 14, 11, 1, 6),
    _AxOspfVirtNbrState_Type()
)
axOspfVirtNbrState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axOspfVirtNbrState.setStatus("current")
_AxOspfVirtNbrEvents_Type = Counter32
_AxOspfVirtNbrEvents_Object = MibTableColumn
axOspfVirtNbrEvents = _AxOspfVirtNbrEvents_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 14, 11, 1, 7),
    _AxOspfVirtNbrEvents_Type()
)
axOspfVirtNbrEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axOspfVirtNbrEvents.setStatus("current")
_AxOspfVirtNbrLsRetransQLen_Type = Gauge32
_AxOspfVirtNbrLsRetransQLen_Object = MibTableColumn
axOspfVirtNbrLsRetransQLen = _AxOspfVirtNbrLsRetransQLen_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 14, 11, 1, 8),
    _AxOspfVirtNbrLsRetransQLen_Type()
)
axOspfVirtNbrLsRetransQLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axOspfVirtNbrLsRetransQLen.setStatus("current")
_AxOspfExtLsdbTable_Object = MibTable
axOspfExtLsdbTable = _AxOspfExtLsdbTable_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 14, 12)
)
if mibBuilder.loadTexts:
    axOspfExtLsdbTable.setStatus("current")
_AxOspfExtLsdbEntry_Object = MibTableRow
axOspfExtLsdbEntry = _AxOspfExtLsdbEntry_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 14, 12, 1)
)
axOspfExtLsdbEntry.setIndexNames(
    (0, "AX-OSPF-MIB", "axOspfExtLsdbDomainNumber"),
    (0, "AX-OSPF-MIB", "axOspfExtLsdbType"),
    (0, "AX-OSPF-MIB", "axOspfExtLsdbLsid"),
    (0, "AX-OSPF-MIB", "axOspfExtLsdbRouterId"),
)
if mibBuilder.loadTexts:
    axOspfExtLsdbEntry.setStatus("current")
_AxOspfExtLsdbDomainNumber_Type = Integer32
_AxOspfExtLsdbDomainNumber_Object = MibTableColumn
axOspfExtLsdbDomainNumber = _AxOspfExtLsdbDomainNumber_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 14, 12, 1, 1),
    _AxOspfExtLsdbDomainNumber_Type()
)
axOspfExtLsdbDomainNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axOspfExtLsdbDomainNumber.setStatus("current")


class _AxOspfExtLsdbType_Type(Integer32):
    """Custom type axOspfExtLsdbType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            5
        )
    )
    namedValues = NamedValues(
        ("asExternalLink", 5)
    )


_AxOspfExtLsdbType_Type.__name__ = "Integer32"
_AxOspfExtLsdbType_Object = MibTableColumn
axOspfExtLsdbType = _AxOspfExtLsdbType_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 14, 12, 1, 2),
    _AxOspfExtLsdbType_Type()
)
axOspfExtLsdbType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axOspfExtLsdbType.setStatus("current")
_AxOspfExtLsdbLsid_Type = IpAddress
_AxOspfExtLsdbLsid_Object = MibTableColumn
axOspfExtLsdbLsid = _AxOspfExtLsdbLsid_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 14, 12, 1, 3),
    _AxOspfExtLsdbLsid_Type()
)
axOspfExtLsdbLsid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axOspfExtLsdbLsid.setStatus("current")
_AxOspfExtLsdbRouterId_Type = IpAddress
_AxOspfExtLsdbRouterId_Object = MibTableColumn
axOspfExtLsdbRouterId = _AxOspfExtLsdbRouterId_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 14, 12, 1, 4),
    _AxOspfExtLsdbRouterId_Type()
)
axOspfExtLsdbRouterId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axOspfExtLsdbRouterId.setStatus("current")
_AxOspfExtLsdbSequence_Type = Integer32
_AxOspfExtLsdbSequence_Object = MibTableColumn
axOspfExtLsdbSequence = _AxOspfExtLsdbSequence_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 14, 12, 1, 5),
    _AxOspfExtLsdbSequence_Type()
)
axOspfExtLsdbSequence.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axOspfExtLsdbSequence.setStatus("current")
_AxOspfExtLsdbAge_Type = Integer32
_AxOspfExtLsdbAge_Object = MibTableColumn
axOspfExtLsdbAge = _AxOspfExtLsdbAge_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 14, 12, 1, 6),
    _AxOspfExtLsdbAge_Type()
)
axOspfExtLsdbAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axOspfExtLsdbAge.setStatus("current")
_AxOspfExtLsdbChecksum_Type = Integer32
_AxOspfExtLsdbChecksum_Object = MibTableColumn
axOspfExtLsdbChecksum = _AxOspfExtLsdbChecksum_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 14, 12, 1, 7),
    _AxOspfExtLsdbChecksum_Type()
)
axOspfExtLsdbChecksum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axOspfExtLsdbChecksum.setStatus("current")
_AxOspfExtLsdbAdvertisement_Type = OctetString
_AxOspfExtLsdbAdvertisement_Object = MibTableColumn
axOspfExtLsdbAdvertisement = _AxOspfExtLsdbAdvertisement_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 14, 12, 1, 8),
    _AxOspfExtLsdbAdvertisement_Type()
)
axOspfExtLsdbAdvertisement.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axOspfExtLsdbAdvertisement.setStatus("current")
_AxOspfAreaAggregateTable_Object = MibTable
axOspfAreaAggregateTable = _AxOspfAreaAggregateTable_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 14, 14)
)
if mibBuilder.loadTexts:
    axOspfAreaAggregateTable.setStatus("current")
_AxOspfAreaAggregateEntry_Object = MibTableRow
axOspfAreaAggregateEntry = _AxOspfAreaAggregateEntry_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 14, 14, 1)
)
axOspfAreaAggregateEntry.setIndexNames(
    (0, "AX-OSPF-MIB", "axOspfAreaAggregateDomainNumber"),
    (0, "AX-OSPF-MIB", "axOspfAreaAggregateAreaID"),
    (0, "AX-OSPF-MIB", "axOspfAreaAggregateLsdbType"),
    (0, "AX-OSPF-MIB", "axOspfAreaAggregateNet"),
    (0, "AX-OSPF-MIB", "axOspfAreaAggregateMask"),
)
if mibBuilder.loadTexts:
    axOspfAreaAggregateEntry.setStatus("current")
_AxOspfAreaAggregateDomainNumber_Type = Integer32
_AxOspfAreaAggregateDomainNumber_Object = MibTableColumn
axOspfAreaAggregateDomainNumber = _AxOspfAreaAggregateDomainNumber_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 14, 14, 1, 1),
    _AxOspfAreaAggregateDomainNumber_Type()
)
axOspfAreaAggregateDomainNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axOspfAreaAggregateDomainNumber.setStatus("current")
_AxOspfAreaAggregateAreaID_Type = IpAddress
_AxOspfAreaAggregateAreaID_Object = MibTableColumn
axOspfAreaAggregateAreaID = _AxOspfAreaAggregateAreaID_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 14, 14, 1, 2),
    _AxOspfAreaAggregateAreaID_Type()
)
axOspfAreaAggregateAreaID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axOspfAreaAggregateAreaID.setStatus("current")


class _AxOspfAreaAggregateLsdbType_Type(Integer32):
    """Custom type axOspfAreaAggregateLsdbType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(3,
              7)
        )
    )
    namedValues = NamedValues(
        *(("summaryLink", 3),
          ("nssaExternalLink", 7))
    )


_AxOspfAreaAggregateLsdbType_Type.__name__ = "Integer32"
_AxOspfAreaAggregateLsdbType_Object = MibTableColumn
axOspfAreaAggregateLsdbType = _AxOspfAreaAggregateLsdbType_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 14, 14, 1, 3),
    _AxOspfAreaAggregateLsdbType_Type()
)
axOspfAreaAggregateLsdbType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axOspfAreaAggregateLsdbType.setStatus("current")
_AxOspfAreaAggregateNet_Type = IpAddress
_AxOspfAreaAggregateNet_Object = MibTableColumn
axOspfAreaAggregateNet = _AxOspfAreaAggregateNet_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 14, 14, 1, 4),
    _AxOspfAreaAggregateNet_Type()
)
axOspfAreaAggregateNet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axOspfAreaAggregateNet.setStatus("current")
_AxOspfAreaAggregateMask_Type = IpAddress
_AxOspfAreaAggregateMask_Object = MibTableColumn
axOspfAreaAggregateMask = _AxOspfAreaAggregateMask_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 14, 14, 1, 5),
    _AxOspfAreaAggregateMask_Type()
)
axOspfAreaAggregateMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axOspfAreaAggregateMask.setStatus("current")
_AxOspfAreaAggregateStatus_Type = RowStatus
_AxOspfAreaAggregateStatus_Object = MibTableColumn
axOspfAreaAggregateStatus = _AxOspfAreaAggregateStatus_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 14, 14, 1, 6),
    _AxOspfAreaAggregateStatus_Type()
)
axOspfAreaAggregateStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    axOspfAreaAggregateStatus.setStatus("current")


class _AxOspfAreaAggregateEffect_Type(Integer32):
    """Custom type axOspfAreaAggregateEffect based on Integer32"""
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


_AxOspfAreaAggregateEffect_Type.__name__ = "Integer32"
_AxOspfAreaAggregateEffect_Object = MibTableColumn
axOspfAreaAggregateEffect = _AxOspfAreaAggregateEffect_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 14, 14, 1, 7),
    _AxOspfAreaAggregateEffect_Type()
)
axOspfAreaAggregateEffect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axOspfAreaAggregateEffect.setStatus("current")
_AxOspfTrap_ObjectIdentity = ObjectIdentity
axOspfTrap = _AxOspfTrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 14, 16)
)
_AxOspfTrapControlTable_Object = MibTable
axOspfTrapControlTable = _AxOspfTrapControlTable_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 14, 16, 1)
)
if mibBuilder.loadTexts:
    axOspfTrapControlTable.setStatus("current")
_AxOspfTrapControlEntry_Object = MibTableRow
axOspfTrapControlEntry = _AxOspfTrapControlEntry_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 14, 16, 1, 1)
)
axOspfTrapControlEntry.setIndexNames(
    (0, "AX-OSPF-MIB", "axOspfTrapDomainNumber"),
)
if mibBuilder.loadTexts:
    axOspfTrapControlEntry.setStatus("current")
_AxOspfTrapDomainNumber_Type = Integer32
_AxOspfTrapDomainNumber_Object = MibTableColumn
axOspfTrapDomainNumber = _AxOspfTrapDomainNumber_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 14, 16, 1, 1, 1),
    _AxOspfTrapDomainNumber_Type()
)
axOspfTrapDomainNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axOspfTrapDomainNumber.setStatus("current")
_AxOspfSetTrap_Type = OctetString
_AxOspfSetTrap_Object = MibTableColumn
axOspfSetTrap = _AxOspfSetTrap_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 14, 16, 1, 1, 2),
    _AxOspfSetTrap_Type()
)
axOspfSetTrap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axOspfSetTrap.setStatus("current")


class _AxOspfConfigErrorType_Type(Integer32):
    """Custom type axOspfConfigErrorType based on Integer32"""
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
              10,
              11,
              12,
              13)
        )
    )
    namedValues = NamedValues(
        *(("badVersion", 1),
          ("areaMismatch", 2),
          ("unknownNbmaNbr", 3),
          ("unknownVirtualNbr", 4),
          ("authTypeMismatch", 5),
          ("authFailure", 6),
          ("netMaskMismatch", 7),
          ("helloIntervalMismatch", 8),
          ("deadIntervalMismatch", 9),
          ("optionMismatch", 10),
          ("mtuMismatch", 11),
          ("duplicateRouterId", 12),
          ("noError", 13))
    )


_AxOspfConfigErrorType_Type.__name__ = "Integer32"
_AxOspfConfigErrorType_Object = MibTableColumn
axOspfConfigErrorType = _AxOspfConfigErrorType_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 14, 16, 1, 1, 3),
    _AxOspfConfigErrorType_Type()
)
axOspfConfigErrorType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axOspfConfigErrorType.setStatus("current")


class _AxOspfPacketType_Type(Integer32):
    """Custom type axOspfPacketType based on Integer32"""
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
        *(("hello", 1),
          ("dbDescript", 2),
          ("lsReq", 3),
          ("lsUpdate", 4),
          ("lsAck", 5),
          ("nullPacket", 6))
    )


_AxOspfPacketType_Type.__name__ = "Integer32"
_AxOspfPacketType_Object = MibTableColumn
axOspfPacketType = _AxOspfPacketType_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 14, 16, 1, 1, 4),
    _AxOspfPacketType_Type()
)
axOspfPacketType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axOspfPacketType.setStatus("current")
_AxOspfPacketSrc_Type = IpAddress
_AxOspfPacketSrc_Object = MibTableColumn
axOspfPacketSrc = _AxOspfPacketSrc_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 14, 16, 1, 1, 5),
    _AxOspfPacketSrc_Type()
)
axOspfPacketSrc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axOspfPacketSrc.setStatus("current")
_AxOspfTraps_ObjectIdentity = ObjectIdentity
axOspfTraps = _AxOspfTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 14, 16, 2)
)
_AxOspfTrapsPrefix_ObjectIdentity = ObjectIdentity
axOspfTrapsPrefix = _AxOspfTrapsPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 14, 16, 2, 0)
)
_AxOspfConformance_ObjectIdentity = ObjectIdentity
axOspfConformance = _AxOspfConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 14, 1000)
)
_AxOspfCompliances_ObjectIdentity = ObjectIdentity
axOspfCompliances = _AxOspfCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 14, 1000, 1)
)
_AxOspfGroups_ObjectIdentity = ObjectIdentity
axOspfGroups = _AxOspfGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 14, 1000, 2)
)

# Managed Objects groups

axOspfGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 14, 1000, 2, 1)
)
axOspfGroup.setObjects(
      *(("AX-OSPF-MIB", "axOspfGeneralDomainNumber"),
        ("AX-OSPF-MIB", "axOspfRouterId"),
        ("AX-OSPF-MIB", "axOspfAdminStat"),
        ("AX-OSPF-MIB", "axOspfVersionNumber"),
        ("AX-OSPF-MIB", "axOspfAreaBdrRtrStatus"),
        ("AX-OSPF-MIB", "axOspfASBdrRtrStatus"),
        ("AX-OSPF-MIB", "axOspfExternLsaCount"),
        ("AX-OSPF-MIB", "axOspfExternLsaCksumSum"),
        ("AX-OSPF-MIB", "axOspfTOSSupport"),
        ("AX-OSPF-MIB", "axOspfOriginateNewLsas"),
        ("AX-OSPF-MIB", "axOspfRxNewLsas"),
        ("AX-OSPF-MIB", "axOspfExtLsdbLimit"),
        ("AX-OSPF-MIB", "axOspfMulticastExtensions"),
        ("AX-OSPF-MIB", "axOspfAreaDomainNumber"),
        ("AX-OSPF-MIB", "axOspfAreaId"),
        ("AX-OSPF-MIB", "axOspfAuthType"),
        ("AX-OSPF-MIB", "axOspfImportAsExtern"),
        ("AX-OSPF-MIB", "axOspfSpfRuns"),
        ("AX-OSPF-MIB", "axOspfAreaBdrRtrCount"),
        ("AX-OSPF-MIB", "axOspfAsBdrRtrCount"),
        ("AX-OSPF-MIB", "axOspfAreaLsaCount"),
        ("AX-OSPF-MIB", "axOspfAreaLsaCksumSum"),
        ("AX-OSPF-MIB", "axOspfAreaSummary"),
        ("AX-OSPF-MIB", "axOspfAreaStatus"),
        ("AX-OSPF-MIB", "axOspfStubDomainNumber"),
        ("AX-OSPF-MIB", "axOspfStubAreaId"),
        ("AX-OSPF-MIB", "axOspfStubTOS"),
        ("AX-OSPF-MIB", "axOspfStubMetric"),
        ("AX-OSPF-MIB", "axOspfStubStatus"),
        ("AX-OSPF-MIB", "axOspfStubMetricType"),
        ("AX-OSPF-MIB", "axOspfLsdbDomainNumber"),
        ("AX-OSPF-MIB", "axOspfLsdbAreaId"),
        ("AX-OSPF-MIB", "axOspfLsdbType"),
        ("AX-OSPF-MIB", "axOspfLsdbLsid"),
        ("AX-OSPF-MIB", "axOspfLsdbRouterId"),
        ("AX-OSPF-MIB", "axOspfLsdbSequence"),
        ("AX-OSPF-MIB", "axOspfLsdbAge"),
        ("AX-OSPF-MIB", "axOspfLsdbChecksum"),
        ("AX-OSPF-MIB", "axOspfLsdbAdvertisement"),
        ("AX-OSPF-MIB", "axOspfAreaRangeDomainNumber"),
        ("AX-OSPF-MIB", "axOspfAreaRangeAreaId"),
        ("AX-OSPF-MIB", "axOspfAreaRangeNet"),
        ("AX-OSPF-MIB", "axOspfAreaRangeMask"),
        ("AX-OSPF-MIB", "axOspfAreaRangeStatus"),
        ("AX-OSPF-MIB", "axOspfAreaRangeEffect"),
        ("AX-OSPF-MIB", "axOspfIfDomainNumber"),
        ("AX-OSPF-MIB", "axOspfIfIpAddress"),
        ("AX-OSPF-MIB", "axOspfAddressLessIf"),
        ("AX-OSPF-MIB", "axOspfIfAreaId"),
        ("AX-OSPF-MIB", "axOspfIfType"),
        ("AX-OSPF-MIB", "axOspfIfAdminStat"),
        ("AX-OSPF-MIB", "axOspfIfRtrPriority"),
        ("AX-OSPF-MIB", "axOspfIfTransitDelay"),
        ("AX-OSPF-MIB", "axOspfIfRetransInterval"),
        ("AX-OSPF-MIB", "axOspfIfHelloInterval"),
        ("AX-OSPF-MIB", "axOspfIfRtrDeadInterval"),
        ("AX-OSPF-MIB", "axOspfIfPollInterval"),
        ("AX-OSPF-MIB", "axOspfIfState"),
        ("AX-OSPF-MIB", "axOspfIfDesignatedRouter"),
        ("AX-OSPF-MIB", "axOspfIfBackupDesignatedRouter"),
        ("AX-OSPF-MIB", "axOspfIfEvents"),
        ("AX-OSPF-MIB", "axOspfIfAuthKey"),
        ("AX-OSPF-MIB", "axOspfIfStatus"),
        ("AX-OSPF-MIB", "axOspfIfMulticastForwarding"),
        ("AX-OSPF-MIB", "axOspfIfMetricDomainNumber"),
        ("AX-OSPF-MIB", "axOspfIfMetricIpAddress"),
        ("AX-OSPF-MIB", "axOspfIfMetricAddressLessIf"),
        ("AX-OSPF-MIB", "axOspfIfMetricTOS"),
        ("AX-OSPF-MIB", "axOspfIfMetricValue"),
        ("AX-OSPF-MIB", "axOspfIfMetricStatus"),
        ("AX-OSPF-MIB", "axOspfVirtIfDomainNumber"),
        ("AX-OSPF-MIB", "axOspfVirtIfAreaId"),
        ("AX-OSPF-MIB", "axOspfVirtIfNeighbor"),
        ("AX-OSPF-MIB", "axOspfVirtIfTransitDelay"),
        ("AX-OSPF-MIB", "axOspfVirtIfRetransInterval"),
        ("AX-OSPF-MIB", "axOspfVirtIfHelloInterval"),
        ("AX-OSPF-MIB", "axOspfVirtIfRtrDeadInterval"),
        ("AX-OSPF-MIB", "axOspfVirtIfState"),
        ("AX-OSPF-MIB", "axOspfVirtIfEvents"),
        ("AX-OSPF-MIB", "axOspfVirtIfAuthKey"),
        ("AX-OSPF-MIB", "axOspfVirtIfStatus"),
        ("AX-OSPF-MIB", "axOspfNbrDomainNumber"),
        ("AX-OSPF-MIB", "axOspfNbrIpAddr"),
        ("AX-OSPF-MIB", "axOspfNbrAddressLessIndex"),
        ("AX-OSPF-MIB", "axOspfNbrRtrId"),
        ("AX-OSPF-MIB", "axOspfNbrOptions"),
        ("AX-OSPF-MIB", "axOspfNbrPriority"),
        ("AX-OSPF-MIB", "axOspfNbrState"),
        ("AX-OSPF-MIB", "axOspfNbrEvents"),
        ("AX-OSPF-MIB", "axOspfNbrLsRetransQLen"),
        ("AX-OSPF-MIB", "axOspfNbmaNbrStatus"),
        ("AX-OSPF-MIB", "axOspfNbmaNbrPermanence"),
        ("AX-OSPF-MIB", "axOspfVirtNbrDomainNumber"),
        ("AX-OSPF-MIB", "axOspfVirtNbrArea"),
        ("AX-OSPF-MIB", "axOspfVirtNbrRtrId"),
        ("AX-OSPF-MIB", "axOspfVirtNbrIpAddr"),
        ("AX-OSPF-MIB", "axOspfVirtNbrOptions"),
        ("AX-OSPF-MIB", "axOspfVirtNbrState"),
        ("AX-OSPF-MIB", "axOspfVirtNbrEvents"),
        ("AX-OSPF-MIB", "axOspfVirtNbrLsRetransQLen"),
        ("AX-OSPF-MIB", "axOspfExtLsdbDomainNumber"),
        ("AX-OSPF-MIB", "axOspfExtLsdbType"),
        ("AX-OSPF-MIB", "axOspfExtLsdbLsid"),
        ("AX-OSPF-MIB", "axOspfExtLsdbRouterId"),
        ("AX-OSPF-MIB", "axOspfExtLsdbSequence"),
        ("AX-OSPF-MIB", "axOspfExtLsdbAge"),
        ("AX-OSPF-MIB", "axOspfExtLsdbChecksum"),
        ("AX-OSPF-MIB", "axOspfExtLsdbAdvertisement"),
        ("AX-OSPF-MIB", "axOspfAreaAggregateDomainNumber"),
        ("AX-OSPF-MIB", "axOspfAreaAggregateAreaID"),
        ("AX-OSPF-MIB", "axOspfAreaAggregateLsdbType"),
        ("AX-OSPF-MIB", "axOspfAreaAggregateNet"),
        ("AX-OSPF-MIB", "axOspfAreaAggregateMask"),
        ("AX-OSPF-MIB", "axOspfAreaAggregateStatus"),
        ("AX-OSPF-MIB", "axOspfAreaAggregateEffect"),
        ("AX-OSPF-MIB", "axOspfTrapDomainNumber"),
        ("AX-OSPF-MIB", "axOspfSetTrap"),
        ("AX-OSPF-MIB", "axOspfConfigErrorType"),
        ("AX-OSPF-MIB", "axOspfPacketType"),
        ("AX-OSPF-MIB", "axOspfPacketSrc"))
)
if mibBuilder.loadTexts:
    axOspfGroup.setStatus("current")


# Notification objects

axOspfVirtIfStateChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 14, 16, 2, 0, 1)
)
axOspfVirtIfStateChange.setObjects(
      *(("AX-OSPF-MIB", "axOspfVirtIfDomainNumber"),
        ("AX-OSPF-MIB", "axOspfRouterId"),
        ("AX-OSPF-MIB", "axOspfVirtIfAreaId"),
        ("AX-OSPF-MIB", "axOspfVirtIfNeighbor"),
        ("AX-OSPF-MIB", "axOspfVirtIfState"))
)
if mibBuilder.loadTexts:
    axOspfVirtIfStateChange.setStatus(
        "current"
    )

axOspfNbrStateChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 14, 16, 2, 0, 2)
)
axOspfNbrStateChange.setObjects(
      *(("AX-OSPF-MIB", "axOspfNbrDomainNumber"),
        ("AX-OSPF-MIB", "axOspfRouterId"),
        ("AX-OSPF-MIB", "axOspfNbrIpAddr"),
        ("AX-OSPF-MIB", "axOspfNbrAddressLessIndex"),
        ("AX-OSPF-MIB", "axOspfNbrRtrId"),
        ("AX-OSPF-MIB", "axOspfNbrState"))
)
if mibBuilder.loadTexts:
    axOspfNbrStateChange.setStatus(
        "current"
    )

axOspfVirtNbrStateChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 14, 16, 2, 0, 3)
)
axOspfVirtNbrStateChange.setObjects(
      *(("AX-OSPF-MIB", "axOspfVirtNbrDomainNumber"),
        ("AX-OSPF-MIB", "axOspfRouterId"),
        ("AX-OSPF-MIB", "axOspfVirtNbrArea"),
        ("AX-OSPF-MIB", "axOspfVirtNbrRtrId"),
        ("AX-OSPF-MIB", "axOspfVirtNbrState"))
)
if mibBuilder.loadTexts:
    axOspfVirtNbrStateChange.setStatus(
        "current"
    )

axOspfIfConfigError = NotificationType(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 14, 16, 2, 0, 4)
)
axOspfIfConfigError.setObjects(
      *(("AX-OSPF-MIB", "axOspfIfDomainNumber"),
        ("AX-OSPF-MIB", "axOspfRouterId"),
        ("AX-OSPF-MIB", "axOspfIfIpAddress"),
        ("AX-OSPF-MIB", "axOspfAddressLessIf"),
        ("AX-OSPF-MIB", "axOspfPacketSrc"),
        ("AX-OSPF-MIB", "axOspfConfigErrorType"),
        ("AX-OSPF-MIB", "axOspfPacketType"))
)
if mibBuilder.loadTexts:
    axOspfIfConfigError.setStatus(
        "current"
    )

axOspfVirtIfConfigError = NotificationType(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 14, 16, 2, 0, 5)
)
axOspfVirtIfConfigError.setObjects(
      *(("AX-OSPF-MIB", "axOspfVirtIfDomainNumber"),
        ("AX-OSPF-MIB", "axOspfRouterId"),
        ("AX-OSPF-MIB", "axOspfVirtIfAreaId"),
        ("AX-OSPF-MIB", "axOspfVirtIfNeighbor"),
        ("AX-OSPF-MIB", "axOspfConfigErrorType"),
        ("AX-OSPF-MIB", "axOspfPacketType"))
)
if mibBuilder.loadTexts:
    axOspfVirtIfConfigError.setStatus(
        "current"
    )

axOspfIfAuthFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 14, 16, 2, 0, 6)
)
axOspfIfAuthFailure.setObjects(
      *(("AX-OSPF-MIB", "axOspfIfDomainNumber"),
        ("AX-OSPF-MIB", "axOspfRouterId"),
        ("AX-OSPF-MIB", "axOspfIfIpAddress"),
        ("AX-OSPF-MIB", "axOspfAddressLessIf"),
        ("AX-OSPF-MIB", "axOspfPacketSrc"),
        ("AX-OSPF-MIB", "axOspfConfigErrorType"),
        ("AX-OSPF-MIB", "axOspfPacketType"))
)
if mibBuilder.loadTexts:
    axOspfIfAuthFailure.setStatus(
        "current"
    )

axOspfVirtIfAuthFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 14, 16, 2, 0, 7)
)
axOspfVirtIfAuthFailure.setObjects(
      *(("AX-OSPF-MIB", "axOspfVirtIfDomainNumber"),
        ("AX-OSPF-MIB", "axOspfRouterId"),
        ("AX-OSPF-MIB", "axOspfVirtIfAreaId"),
        ("AX-OSPF-MIB", "axOspfVirtIfNeighbor"),
        ("AX-OSPF-MIB", "axOspfConfigErrorType"),
        ("AX-OSPF-MIB", "axOspfPacketType"))
)
if mibBuilder.loadTexts:
    axOspfVirtIfAuthFailure.setStatus(
        "current"
    )

axOspfIfStateChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 14, 16, 2, 0, 16)
)
axOspfIfStateChange.setObjects(
      *(("AX-OSPF-MIB", "axOspfIfDomainNumber"),
        ("AX-OSPF-MIB", "axOspfRouterId"),
        ("AX-OSPF-MIB", "axOspfIfIpAddress"),
        ("AX-OSPF-MIB", "axOspfAddressLessIf"),
        ("AX-OSPF-MIB", "axOspfIfState"))
)
if mibBuilder.loadTexts:
    axOspfIfStateChange.setStatus(
        "current"
    )


# Notifications groups

axOspfTrapNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 14, 1000, 2, 100)
)
axOspfTrapNotificationGroup.setObjects(
      *(("AX-OSPF-MIB", "axOspfVirtIfStateChange"),
        ("AX-OSPF-MIB", "axOspfNbrStateChange"),
        ("AX-OSPF-MIB", "axOspfVirtNbrStateChange"),
        ("AX-OSPF-MIB", "axOspfIfStateChange"),
        ("AX-OSPF-MIB", "axOspfIfConfigError"),
        ("AX-OSPF-MIB", "axOspfVirtIfConfigError"),
        ("AX-OSPF-MIB", "axOspfIfAuthFailure"),
        ("AX-OSPF-MIB", "axOspfVirtIfAuthFailure"))
)
if mibBuilder.loadTexts:
    axOspfTrapNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

axOspfCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 14, 1000, 1, 1)
)
axOspfCompliance.setObjects(
      *(("AX-OSPF-MIB", "axOspfGroup"),
        ("AX-OSPF-MIB", "axOspfTrapNotificationGroup"))
)
if mibBuilder.loadTexts:
    axOspfCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "AX-OSPF-MIB",
    **{"InterfaceIndexOrZero": InterfaceIndexOrZero,
       "Status": Status,
       "axOspf": axOspf,
       "axOspfGeneralTable": axOspfGeneralTable,
       "axOspfGeneralEntry": axOspfGeneralEntry,
       "axOspfGeneralDomainNumber": axOspfGeneralDomainNumber,
       "axOspfRouterId": axOspfRouterId,
       "axOspfAdminStat": axOspfAdminStat,
       "axOspfVersionNumber": axOspfVersionNumber,
       "axOspfAreaBdrRtrStatus": axOspfAreaBdrRtrStatus,
       "axOspfASBdrRtrStatus": axOspfASBdrRtrStatus,
       "axOspfExternLsaCount": axOspfExternLsaCount,
       "axOspfExternLsaCksumSum": axOspfExternLsaCksumSum,
       "axOspfTOSSupport": axOspfTOSSupport,
       "axOspfOriginateNewLsas": axOspfOriginateNewLsas,
       "axOspfRxNewLsas": axOspfRxNewLsas,
       "axOspfExtLsdbLimit": axOspfExtLsdbLimit,
       "axOspfMulticastExtensions": axOspfMulticastExtensions,
       "axOspfAreaTable": axOspfAreaTable,
       "axOspfAreaEntry": axOspfAreaEntry,
       "axOspfAreaDomainNumber": axOspfAreaDomainNumber,
       "axOspfAreaId": axOspfAreaId,
       "axOspfAuthType": axOspfAuthType,
       "axOspfImportAsExtern": axOspfImportAsExtern,
       "axOspfSpfRuns": axOspfSpfRuns,
       "axOspfAreaBdrRtrCount": axOspfAreaBdrRtrCount,
       "axOspfAsBdrRtrCount": axOspfAsBdrRtrCount,
       "axOspfAreaLsaCount": axOspfAreaLsaCount,
       "axOspfAreaLsaCksumSum": axOspfAreaLsaCksumSum,
       "axOspfAreaSummary": axOspfAreaSummary,
       "axOspfAreaStatus": axOspfAreaStatus,
       "axOspfStubAreaTable": axOspfStubAreaTable,
       "axOspfStubAreaEntry": axOspfStubAreaEntry,
       "axOspfStubDomainNumber": axOspfStubDomainNumber,
       "axOspfStubAreaId": axOspfStubAreaId,
       "axOspfStubTOS": axOspfStubTOS,
       "axOspfStubMetric": axOspfStubMetric,
       "axOspfStubStatus": axOspfStubStatus,
       "axOspfStubMetricType": axOspfStubMetricType,
       "axOspfLsdbTable": axOspfLsdbTable,
       "axOspfLsdbEntry": axOspfLsdbEntry,
       "axOspfLsdbDomainNumber": axOspfLsdbDomainNumber,
       "axOspfLsdbAreaId": axOspfLsdbAreaId,
       "axOspfLsdbType": axOspfLsdbType,
       "axOspfLsdbLsid": axOspfLsdbLsid,
       "axOspfLsdbRouterId": axOspfLsdbRouterId,
       "axOspfLsdbSequence": axOspfLsdbSequence,
       "axOspfLsdbAge": axOspfLsdbAge,
       "axOspfLsdbChecksum": axOspfLsdbChecksum,
       "axOspfLsdbAdvertisement": axOspfLsdbAdvertisement,
       "axOspfAreaRangeTable": axOspfAreaRangeTable,
       "axOspfAreaRangeEntry": axOspfAreaRangeEntry,
       "axOspfAreaRangeDomainNumber": axOspfAreaRangeDomainNumber,
       "axOspfAreaRangeAreaId": axOspfAreaRangeAreaId,
       "axOspfAreaRangeNet": axOspfAreaRangeNet,
       "axOspfAreaRangeMask": axOspfAreaRangeMask,
       "axOspfAreaRangeStatus": axOspfAreaRangeStatus,
       "axOspfAreaRangeEffect": axOspfAreaRangeEffect,
       "axOspfIfTable": axOspfIfTable,
       "axOspfIfEntry": axOspfIfEntry,
       "axOspfIfDomainNumber": axOspfIfDomainNumber,
       "axOspfIfIpAddress": axOspfIfIpAddress,
       "axOspfAddressLessIf": axOspfAddressLessIf,
       "axOspfIfAreaId": axOspfIfAreaId,
       "axOspfIfType": axOspfIfType,
       "axOspfIfAdminStat": axOspfIfAdminStat,
       "axOspfIfRtrPriority": axOspfIfRtrPriority,
       "axOspfIfTransitDelay": axOspfIfTransitDelay,
       "axOspfIfRetransInterval": axOspfIfRetransInterval,
       "axOspfIfHelloInterval": axOspfIfHelloInterval,
       "axOspfIfRtrDeadInterval": axOspfIfRtrDeadInterval,
       "axOspfIfPollInterval": axOspfIfPollInterval,
       "axOspfIfState": axOspfIfState,
       "axOspfIfDesignatedRouter": axOspfIfDesignatedRouter,
       "axOspfIfBackupDesignatedRouter": axOspfIfBackupDesignatedRouter,
       "axOspfIfEvents": axOspfIfEvents,
       "axOspfIfAuthKey": axOspfIfAuthKey,
       "axOspfIfStatus": axOspfIfStatus,
       "axOspfIfMulticastForwarding": axOspfIfMulticastForwarding,
       "axOspfIfMetricTable": axOspfIfMetricTable,
       "axOspfIfMetricEntry": axOspfIfMetricEntry,
       "axOspfIfMetricDomainNumber": axOspfIfMetricDomainNumber,
       "axOspfIfMetricIpAddress": axOspfIfMetricIpAddress,
       "axOspfIfMetricAddressLessIf": axOspfIfMetricAddressLessIf,
       "axOspfIfMetricTOS": axOspfIfMetricTOS,
       "axOspfIfMetricValue": axOspfIfMetricValue,
       "axOspfIfMetricStatus": axOspfIfMetricStatus,
       "axOspfVirtIfTable": axOspfVirtIfTable,
       "axOspfVirtIfEntry": axOspfVirtIfEntry,
       "axOspfVirtIfDomainNumber": axOspfVirtIfDomainNumber,
       "axOspfVirtIfAreaId": axOspfVirtIfAreaId,
       "axOspfVirtIfNeighbor": axOspfVirtIfNeighbor,
       "axOspfVirtIfTransitDelay": axOspfVirtIfTransitDelay,
       "axOspfVirtIfRetransInterval": axOspfVirtIfRetransInterval,
       "axOspfVirtIfHelloInterval": axOspfVirtIfHelloInterval,
       "axOspfVirtIfRtrDeadInterval": axOspfVirtIfRtrDeadInterval,
       "axOspfVirtIfState": axOspfVirtIfState,
       "axOspfVirtIfEvents": axOspfVirtIfEvents,
       "axOspfVirtIfAuthKey": axOspfVirtIfAuthKey,
       "axOspfVirtIfStatus": axOspfVirtIfStatus,
       "axOspfNbrTable": axOspfNbrTable,
       "axOspfNbrEntry": axOspfNbrEntry,
       "axOspfNbrDomainNumber": axOspfNbrDomainNumber,
       "axOspfNbrIpAddr": axOspfNbrIpAddr,
       "axOspfNbrAddressLessIndex": axOspfNbrAddressLessIndex,
       "axOspfNbrRtrId": axOspfNbrRtrId,
       "axOspfNbrOptions": axOspfNbrOptions,
       "axOspfNbrPriority": axOspfNbrPriority,
       "axOspfNbrState": axOspfNbrState,
       "axOspfNbrEvents": axOspfNbrEvents,
       "axOspfNbrLsRetransQLen": axOspfNbrLsRetransQLen,
       "axOspfNbmaNbrStatus": axOspfNbmaNbrStatus,
       "axOspfNbmaNbrPermanence": axOspfNbmaNbrPermanence,
       "axOspfVirtNbrTable": axOspfVirtNbrTable,
       "axOspfVirtNbrEntry": axOspfVirtNbrEntry,
       "axOspfVirtNbrDomainNumber": axOspfVirtNbrDomainNumber,
       "axOspfVirtNbrArea": axOspfVirtNbrArea,
       "axOspfVirtNbrRtrId": axOspfVirtNbrRtrId,
       "axOspfVirtNbrIpAddr": axOspfVirtNbrIpAddr,
       "axOspfVirtNbrOptions": axOspfVirtNbrOptions,
       "axOspfVirtNbrState": axOspfVirtNbrState,
       "axOspfVirtNbrEvents": axOspfVirtNbrEvents,
       "axOspfVirtNbrLsRetransQLen": axOspfVirtNbrLsRetransQLen,
       "axOspfExtLsdbTable": axOspfExtLsdbTable,
       "axOspfExtLsdbEntry": axOspfExtLsdbEntry,
       "axOspfExtLsdbDomainNumber": axOspfExtLsdbDomainNumber,
       "axOspfExtLsdbType": axOspfExtLsdbType,
       "axOspfExtLsdbLsid": axOspfExtLsdbLsid,
       "axOspfExtLsdbRouterId": axOspfExtLsdbRouterId,
       "axOspfExtLsdbSequence": axOspfExtLsdbSequence,
       "axOspfExtLsdbAge": axOspfExtLsdbAge,
       "axOspfExtLsdbChecksum": axOspfExtLsdbChecksum,
       "axOspfExtLsdbAdvertisement": axOspfExtLsdbAdvertisement,
       "axOspfAreaAggregateTable": axOspfAreaAggregateTable,
       "axOspfAreaAggregateEntry": axOspfAreaAggregateEntry,
       "axOspfAreaAggregateDomainNumber": axOspfAreaAggregateDomainNumber,
       "axOspfAreaAggregateAreaID": axOspfAreaAggregateAreaID,
       "axOspfAreaAggregateLsdbType": axOspfAreaAggregateLsdbType,
       "axOspfAreaAggregateNet": axOspfAreaAggregateNet,
       "axOspfAreaAggregateMask": axOspfAreaAggregateMask,
       "axOspfAreaAggregateStatus": axOspfAreaAggregateStatus,
       "axOspfAreaAggregateEffect": axOspfAreaAggregateEffect,
       "axOspfTrap": axOspfTrap,
       "axOspfTrapControlTable": axOspfTrapControlTable,
       "axOspfTrapControlEntry": axOspfTrapControlEntry,
       "axOspfTrapDomainNumber": axOspfTrapDomainNumber,
       "axOspfSetTrap": axOspfSetTrap,
       "axOspfConfigErrorType": axOspfConfigErrorType,
       "axOspfPacketType": axOspfPacketType,
       "axOspfPacketSrc": axOspfPacketSrc,
       "axOspfTraps": axOspfTraps,
       "axOspfTrapsPrefix": axOspfTrapsPrefix,
       "axOspfVirtIfStateChange": axOspfVirtIfStateChange,
       "axOspfNbrStateChange": axOspfNbrStateChange,
       "axOspfVirtNbrStateChange": axOspfVirtNbrStateChange,
       "axOspfIfConfigError": axOspfIfConfigError,
       "axOspfVirtIfConfigError": axOspfVirtIfConfigError,
       "axOspfIfAuthFailure": axOspfIfAuthFailure,
       "axOspfVirtIfAuthFailure": axOspfVirtIfAuthFailure,
       "axOspfIfStateChange": axOspfIfStateChange,
       "axOspfConformance": axOspfConformance,
       "axOspfCompliances": axOspfCompliances,
       "axOspfCompliance": axOspfCompliance,
       "axOspfGroups": axOspfGroups,
       "axOspfGroup": axOspfGroup,
       "axOspfTrapNotificationGroup": axOspfTrapNotificationGroup}
)
