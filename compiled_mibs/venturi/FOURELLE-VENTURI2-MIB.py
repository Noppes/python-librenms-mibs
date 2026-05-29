# SNMP MIB module (FOURELLE-VENTURI2-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\venturi\FOURELLE-VENTURI2-MIB

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")

(venturiWireless,) = mibBuilder.importSymbols(
    "VENTURI-WIRELESS-SMI",
    "venturiWireless")


# MODULE-IDENTITY

venturi2 = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 3382, 2)
)
if mibBuilder.loadTexts:
    venturi2.setRevisions(
        ("2011-01-03 00:00",
         "2010-01-06 00:00",
         "2005-04-26 00:00",
         "2004-11-30 00:00",
         "2004-08-23 00:00",
         "2004-05-19 00:00",
         "2004-01-05 00:00",
         "2003-03-27 00:00",
         "2002-07-31 00:00",
         "2002-06-10 15:00",
         "2002-06-10 00:00",
         "2001-07-16 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Traps_ObjectIdentity = ObjectIdentity
traps = _Traps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3382, 2, 0)
)
_General_ObjectIdentity = ObjectIdentity
general = _General_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3382, 2, 1)
)
_System_ObjectIdentity = ObjectIdentity
system = _System_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3382, 2, 1, 1)
)


class _SysType_Type(Bits):
    """Custom type sysType based on Bits"""
    namedValues = NamedValues(
        *(("server", 0),
          ("client", 1))
    )

_SysType_Type.__name__ = "Bits"
_SysType_Object = MibScalar
sysType = _SysType_Object(
    (1, 3, 6, 1, 4, 1, 3382, 2, 1, 1, 1),
    _SysType_Type()
)
sysType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysType.setStatus("current")


class _SysVersion_Type(OctetString):
    """Custom type sysVersion based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_SysVersion_Type.__name__ = "OctetString"
_SysVersion_Object = MibScalar
sysVersion = _SysVersion_Object(
    (1, 3, 6, 1, 4, 1, 3382, 2, 1, 1, 2),
    _SysVersion_Type()
)
sysVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysVersion.setStatus("current")
_SysStartTime_Type = Integer32
_SysStartTime_Object = MibScalar
sysStartTime = _SysStartTime_Object(
    (1, 3, 6, 1, 4, 1, 3382, 2, 1, 1, 3),
    _SysStartTime_Type()
)
sysStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysStartTime.setStatus("current")
_SysUpTime_Type = Integer32
_SysUpTime_Object = MibScalar
sysUpTime = _SysUpTime_Object(
    (1, 3, 6, 1, 4, 1, 3382, 2, 1, 1, 4),
    _SysUpTime_Type()
)
sysUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysUpTime.setStatus("current")


class _SysBuildId_Type(OctetString):
    """Custom type sysBuildId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_SysBuildId_Type.__name__ = "OctetString"
_SysBuildId_Object = MibScalar
sysBuildId = _SysBuildId_Object(
    (1, 3, 6, 1, 4, 1, 3382, 2, 1, 1, 5),
    _SysBuildId_Type()
)
sysBuildId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysBuildId.setStatus("current")
_SysLicenses_Type = Integer32
_SysLicenses_Object = MibScalar
sysLicenses = _SysLicenses_Object(
    (1, 3, 6, 1, 4, 1, 3382, 2, 1, 1, 6),
    _SysLicenses_Type()
)
sysLicenses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysLicenses.setStatus("current")
_SysLicensesUsed_Type = Integer32
_SysLicensesUsed_Object = MibScalar
sysLicensesUsed = _SysLicensesUsed_Object(
    (1, 3, 6, 1, 4, 1, 3382, 2, 1, 1, 7),
    _SysLicensesUsed_Type()
)
sysLicensesUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysLicensesUsed.setStatus("current")


class _SysCustomerId_Type(OctetString):
    """Custom type sysCustomerId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_SysCustomerId_Type.__name__ = "OctetString"
_SysCustomerId_Object = MibScalar
sysCustomerId = _SysCustomerId_Object(
    (1, 3, 6, 1, 4, 1, 3382, 2, 1, 1, 8),
    _SysCustomerId_Type()
)
sysCustomerId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysCustomerId.setStatus("current")
_SysNumCPUs_Type = Integer32
_SysNumCPUs_Object = MibScalar
sysNumCPUs = _SysNumCPUs_Object(
    (1, 3, 6, 1, 4, 1, 3382, 2, 1, 1, 9),
    _SysNumCPUs_Type()
)
sysNumCPUs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysNumCPUs.setStatus("current")
_Statistics_ObjectIdentity = ObjectIdentity
statistics = _Statistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3382, 2, 1, 2)
)
_StatOnlineUsers_Type = Integer32
_StatOnlineUsers_Object = MibScalar
statOnlineUsers = _StatOnlineUsers_Object(
    (1, 3, 6, 1, 4, 1, 3382, 2, 1, 2, 1),
    _StatOnlineUsers_Type()
)
statOnlineUsers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statOnlineUsers.setStatus("current")
_StatCurrentConnections_Type = Integer32
_StatCurrentConnections_Object = MibScalar
statCurrentConnections = _StatCurrentConnections_Object(
    (1, 3, 6, 1, 4, 1, 3382, 2, 1, 2, 2),
    _StatCurrentConnections_Type()
)
statCurrentConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statCurrentConnections.setStatus("current")
_StatTotalConnections_Type = Integer32
_StatTotalConnections_Object = MibScalar
statTotalConnections = _StatTotalConnections_Object(
    (1, 3, 6, 1, 4, 1, 3382, 2, 1, 2, 3),
    _StatTotalConnections_Type()
)
statTotalConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statTotalConnections.setStatus("current")
_StatTotalConnectionDuration_Type = Integer32
_StatTotalConnectionDuration_Object = MibScalar
statTotalConnectionDuration = _StatTotalConnectionDuration_Object(
    (1, 3, 6, 1, 4, 1, 3382, 2, 1, 2, 4),
    _StatTotalConnectionDuration_Type()
)
statTotalConnectionDuration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statTotalConnectionDuration.setStatus("current")
_StatVTPInOctets_Type = Counter32
_StatVTPInOctets_Object = MibScalar
statVTPInOctets = _StatVTPInOctets_Object(
    (1, 3, 6, 1, 4, 1, 3382, 2, 1, 2, 5),
    _StatVTPInOctets_Type()
)
statVTPInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statVTPInOctets.setStatus("current")
_StatVTPOutOctets_Type = Counter32
_StatVTPOutOctets_Object = MibScalar
statVTPOutOctets = _StatVTPOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 3382, 2, 1, 2, 6),
    _StatVTPOutOctets_Type()
)
statVTPOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statVTPOutOctets.setStatus("current")
_StatVTPInPkts_Type = Counter32
_StatVTPInPkts_Object = MibScalar
statVTPInPkts = _StatVTPInPkts_Object(
    (1, 3, 6, 1, 4, 1, 3382, 2, 1, 2, 7),
    _StatVTPInPkts_Type()
)
statVTPInPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statVTPInPkts.setStatus("current")
_StatVTPOutPkts_Type = Counter32
_StatVTPOutPkts_Object = MibScalar
statVTPOutPkts = _StatVTPOutPkts_Object(
    (1, 3, 6, 1, 4, 1, 3382, 2, 1, 2, 8),
    _StatVTPOutPkts_Type()
)
statVTPOutPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statVTPOutPkts.setStatus("current")
_StatToCompOctets_Type = Counter32
_StatToCompOctets_Object = MibScalar
statToCompOctets = _StatToCompOctets_Object(
    (1, 3, 6, 1, 4, 1, 3382, 2, 1, 2, 9),
    _StatToCompOctets_Type()
)
statToCompOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statToCompOctets.setStatus("current")
_StatFromCompOctets_Type = Counter32
_StatFromCompOctets_Object = MibScalar
statFromCompOctets = _StatFromCompOctets_Object(
    (1, 3, 6, 1, 4, 1, 3382, 2, 1, 2, 10),
    _StatFromCompOctets_Type()
)
statFromCompOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statFromCompOctets.setStatus("current")
_StatExtInOctets_Type = Counter32
_StatExtInOctets_Object = MibScalar
statExtInOctets = _StatExtInOctets_Object(
    (1, 3, 6, 1, 4, 1, 3382, 2, 1, 2, 11),
    _StatExtInOctets_Type()
)
statExtInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statExtInOctets.setStatus("current")
_StatExtOutOctets_Type = Counter32
_StatExtOutOctets_Object = MibScalar
statExtOutOctets = _StatExtOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 3382, 2, 1, 2, 12),
    _StatExtOutOctets_Type()
)
statExtOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statExtOutOctets.setStatus("current")
_AppStatsTable_Object = MibTable
appStatsTable = _AppStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 3382, 2, 1, 2, 13)
)
if mibBuilder.loadTexts:
    appStatsTable.setStatus("current")
_AppStatsEntry_Object = MibTableRow
appStatsEntry = _AppStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 3382, 2, 1, 2, 13, 1)
)
appStatsEntry.setIndexNames(
    (0, "FOURELLE-VENTURI2-MIB", "asRowId"),
)
if mibBuilder.loadTexts:
    appStatsEntry.setStatus("current")


class _AsRowId_Type(Integer32):
    """Custom type asRowId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 7),
    )


_AsRowId_Type.__name__ = "Integer32"
_AsRowId_Object = MibTableColumn
asRowId = _AsRowId_Object(
    (1, 3, 6, 1, 4, 1, 3382, 2, 1, 2, 13, 1, 1),
    _AsRowId_Type()
)
asRowId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    asRowId.setStatus("current")
_AsProtocol_Type = OctetString
_AsProtocol_Object = MibTableColumn
asProtocol = _AsProtocol_Object(
    (1, 3, 6, 1, 4, 1, 3382, 2, 1, 2, 13, 1, 2),
    _AsProtocol_Type()
)
asProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    asProtocol.setStatus("current")
_AsFromExternal_Type = Counter32
_AsFromExternal_Object = MibTableColumn
asFromExternal = _AsFromExternal_Object(
    (1, 3, 6, 1, 4, 1, 3382, 2, 1, 2, 13, 1, 3),
    _AsFromExternal_Type()
)
asFromExternal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    asFromExternal.setStatus("current")
_AsToExternal_Type = Counter32
_AsToExternal_Object = MibTableColumn
asToExternal = _AsToExternal_Object(
    (1, 3, 6, 1, 4, 1, 3382, 2, 1, 2, 13, 1, 4),
    _AsToExternal_Type()
)
asToExternal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    asToExternal.setStatus("current")
_AsFromTransport_Type = Counter32
_AsFromTransport_Object = MibTableColumn
asFromTransport = _AsFromTransport_Object(
    (1, 3, 6, 1, 4, 1, 3382, 2, 1, 2, 13, 1, 5),
    _AsFromTransport_Type()
)
asFromTransport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    asFromTransport.setStatus("current")
_AsToTransport_Type = Counter32
_AsToTransport_Object = MibTableColumn
asToTransport = _AsToTransport_Object(
    (1, 3, 6, 1, 4, 1, 3382, 2, 1, 2, 13, 1, 6),
    _AsToTransport_Type()
)
asToTransport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    asToTransport.setStatus("current")
_AsCurConnections_Type = Gauge32
_AsCurConnections_Object = MibTableColumn
asCurConnections = _AsCurConnections_Object(
    (1, 3, 6, 1, 4, 1, 3382, 2, 1, 2, 13, 1, 7),
    _AsCurConnections_Type()
)
asCurConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    asCurConnections.setStatus("current")
_AsNumRequests_Type = Counter32
_AsNumRequests_Object = MibTableColumn
asNumRequests = _AsNumRequests_Object(
    (1, 3, 6, 1, 4, 1, 3382, 2, 1, 2, 13, 1, 8),
    _AsNumRequests_Type()
)
asNumRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    asNumRequests.setStatus("current")
_AsMaxRequests_Type = Gauge32
_AsMaxRequests_Object = MibTableColumn
asMaxRequests = _AsMaxRequests_Object(
    (1, 3, 6, 1, 4, 1, 3382, 2, 1, 2, 13, 1, 9),
    _AsMaxRequests_Type()
)
asMaxRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    asMaxRequests.setStatus("current")
_AsFromClientless_Type = Counter32
_AsFromClientless_Object = MibTableColumn
asFromClientless = _AsFromClientless_Object(
    (1, 3, 6, 1, 4, 1, 3382, 2, 1, 2, 13, 1, 10),
    _AsFromClientless_Type()
)
asFromClientless.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    asFromClientless.setStatus("current")
_AsToClientless_Type = Counter32
_AsToClientless_Object = MibTableColumn
asToClientless = _AsToClientless_Object(
    (1, 3, 6, 1, 4, 1, 3382, 2, 1, 2, 13, 1, 11),
    _AsToClientless_Type()
)
asToClientless.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    asToClientless.setStatus("current")
_StatCpuUtilization_Type = Gauge32
_StatCpuUtilization_Object = MibScalar
statCpuUtilization = _StatCpuUtilization_Object(
    (1, 3, 6, 1, 4, 1, 3382, 2, 1, 2, 14),
    _StatCpuUtilization_Type()
)
statCpuUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statCpuUtilization.setStatus("current")
_StatQdepth2comp_Type = Integer32
_StatQdepth2comp_Object = MibScalar
statQdepth2comp = _StatQdepth2comp_Object(
    (1, 3, 6, 1, 4, 1, 3382, 2, 1, 2, 15),
    _StatQdepth2comp_Type()
)
statQdepth2comp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statQdepth2comp.setStatus("current")
_StatFromClientlessOctets_Type = Counter32
_StatFromClientlessOctets_Object = MibScalar
statFromClientlessOctets = _StatFromClientlessOctets_Object(
    (1, 3, 6, 1, 4, 1, 3382, 2, 1, 2, 16),
    _StatFromClientlessOctets_Type()
)
statFromClientlessOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statFromClientlessOctets.setStatus("current")
_StatToClientlessOctets_Type = Counter32
_StatToClientlessOctets_Object = MibScalar
statToClientlessOctets = _StatToClientlessOctets_Object(
    (1, 3, 6, 1, 4, 1, 3382, 2, 1, 2, 17),
    _StatToClientlessOctets_Type()
)
statToClientlessOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statToClientlessOctets.setStatus("current")
_Statistics64_ObjectIdentity = ObjectIdentity
statistics64 = _Statistics64_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3382, 2, 1, 3)
)
_StatVTPInOctets64_Type = Counter64
_StatVTPInOctets64_Object = MibScalar
statVTPInOctets64 = _StatVTPInOctets64_Object(
    (1, 3, 6, 1, 4, 1, 3382, 2, 1, 3, 5),
    _StatVTPInOctets64_Type()
)
statVTPInOctets64.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statVTPInOctets64.setStatus("current")
_StatVTPOutOctets64_Type = Counter64
_StatVTPOutOctets64_Object = MibScalar
statVTPOutOctets64 = _StatVTPOutOctets64_Object(
    (1, 3, 6, 1, 4, 1, 3382, 2, 1, 3, 6),
    _StatVTPOutOctets64_Type()
)
statVTPOutOctets64.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statVTPOutOctets64.setStatus("current")
_StatVTPInPkts64_Type = Counter64
_StatVTPInPkts64_Object = MibScalar
statVTPInPkts64 = _StatVTPInPkts64_Object(
    (1, 3, 6, 1, 4, 1, 3382, 2, 1, 3, 7),
    _StatVTPInPkts64_Type()
)
statVTPInPkts64.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statVTPInPkts64.setStatus("current")
_StatVTPOutPkts64_Type = Counter64
_StatVTPOutPkts64_Object = MibScalar
statVTPOutPkts64 = _StatVTPOutPkts64_Object(
    (1, 3, 6, 1, 4, 1, 3382, 2, 1, 3, 8),
    _StatVTPOutPkts64_Type()
)
statVTPOutPkts64.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statVTPOutPkts64.setStatus("current")
_StatToCompOctets64_Type = Counter64
_StatToCompOctets64_Object = MibScalar
statToCompOctets64 = _StatToCompOctets64_Object(
    (1, 3, 6, 1, 4, 1, 3382, 2, 1, 3, 9),
    _StatToCompOctets64_Type()
)
statToCompOctets64.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statToCompOctets64.setStatus("current")
_StatFromCompOctets64_Type = Counter64
_StatFromCompOctets64_Object = MibScalar
statFromCompOctets64 = _StatFromCompOctets64_Object(
    (1, 3, 6, 1, 4, 1, 3382, 2, 1, 3, 10),
    _StatFromCompOctets64_Type()
)
statFromCompOctets64.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statFromCompOctets64.setStatus("current")
_StatExtInOctets64_Type = Counter64
_StatExtInOctets64_Object = MibScalar
statExtInOctets64 = _StatExtInOctets64_Object(
    (1, 3, 6, 1, 4, 1, 3382, 2, 1, 3, 11),
    _StatExtInOctets64_Type()
)
statExtInOctets64.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statExtInOctets64.setStatus("current")
_StatExtOutOctets64_Type = Counter64
_StatExtOutOctets64_Object = MibScalar
statExtOutOctets64 = _StatExtOutOctets64_Object(
    (1, 3, 6, 1, 4, 1, 3382, 2, 1, 3, 12),
    _StatExtOutOctets64_Type()
)
statExtOutOctets64.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statExtOutOctets64.setStatus("current")
_AppStatsTable64_Object = MibTable
appStatsTable64 = _AppStatsTable64_Object(
    (1, 3, 6, 1, 4, 1, 3382, 2, 1, 3, 13)
)
if mibBuilder.loadTexts:
    appStatsTable64.setStatus("current")
_AppStatsEntry64_Object = MibTableRow
appStatsEntry64 = _AppStatsEntry64_Object(
    (1, 3, 6, 1, 4, 1, 3382, 2, 1, 3, 13, 1)
)
appStatsEntry64.setIndexNames(
    (0, "FOURELLE-VENTURI2-MIB", "asRowId64"),
)
if mibBuilder.loadTexts:
    appStatsEntry64.setStatus("current")


class _AsRowId64_Type(Integer32):
    """Custom type asRowId64 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 7),
    )


_AsRowId64_Type.__name__ = "Integer32"
_AsRowId64_Object = MibTableColumn
asRowId64 = _AsRowId64_Object(
    (1, 3, 6, 1, 4, 1, 3382, 2, 1, 3, 13, 1, 1),
    _AsRowId64_Type()
)
asRowId64.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    asRowId64.setStatus("current")
_AsProtocol64_Type = OctetString
_AsProtocol64_Object = MibTableColumn
asProtocol64 = _AsProtocol64_Object(
    (1, 3, 6, 1, 4, 1, 3382, 2, 1, 3, 13, 1, 2),
    _AsProtocol64_Type()
)
asProtocol64.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    asProtocol64.setStatus("current")
_AsFromExternal64_Type = Counter64
_AsFromExternal64_Object = MibTableColumn
asFromExternal64 = _AsFromExternal64_Object(
    (1, 3, 6, 1, 4, 1, 3382, 2, 1, 3, 13, 1, 3),
    _AsFromExternal64_Type()
)
asFromExternal64.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    asFromExternal64.setStatus("current")
_AsToExternal64_Type = Counter64
_AsToExternal64_Object = MibTableColumn
asToExternal64 = _AsToExternal64_Object(
    (1, 3, 6, 1, 4, 1, 3382, 2, 1, 3, 13, 1, 4),
    _AsToExternal64_Type()
)
asToExternal64.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    asToExternal64.setStatus("current")
_AsFromTransport64_Type = Counter64
_AsFromTransport64_Object = MibTableColumn
asFromTransport64 = _AsFromTransport64_Object(
    (1, 3, 6, 1, 4, 1, 3382, 2, 1, 3, 13, 1, 5),
    _AsFromTransport64_Type()
)
asFromTransport64.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    asFromTransport64.setStatus("current")
_AsToTransport64_Type = Counter64
_AsToTransport64_Object = MibTableColumn
asToTransport64 = _AsToTransport64_Object(
    (1, 3, 6, 1, 4, 1, 3382, 2, 1, 3, 13, 1, 6),
    _AsToTransport64_Type()
)
asToTransport64.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    asToTransport64.setStatus("current")
_AsCurConnections64_Type = Gauge32
_AsCurConnections64_Object = MibTableColumn
asCurConnections64 = _AsCurConnections64_Object(
    (1, 3, 6, 1, 4, 1, 3382, 2, 1, 3, 13, 1, 7),
    _AsCurConnections64_Type()
)
asCurConnections64.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    asCurConnections64.setStatus("current")
_AsNumRequests64_Type = Counter64
_AsNumRequests64_Object = MibTableColumn
asNumRequests64 = _AsNumRequests64_Object(
    (1, 3, 6, 1, 4, 1, 3382, 2, 1, 3, 13, 1, 8),
    _AsNumRequests64_Type()
)
asNumRequests64.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    asNumRequests64.setStatus("current")
_AsMaxRequests64_Type = Gauge32
_AsMaxRequests64_Object = MibTableColumn
asMaxRequests64 = _AsMaxRequests64_Object(
    (1, 3, 6, 1, 4, 1, 3382, 2, 1, 3, 13, 1, 9),
    _AsMaxRequests64_Type()
)
asMaxRequests64.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    asMaxRequests64.setStatus("current")
_AsFromClientless64_Type = Counter64
_AsFromClientless64_Object = MibTableColumn
asFromClientless64 = _AsFromClientless64_Object(
    (1, 3, 6, 1, 4, 1, 3382, 2, 1, 3, 13, 1, 10),
    _AsFromClientless64_Type()
)
asFromClientless64.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    asFromClientless64.setStatus("current")
_AsToClientless64_Type = Counter64
_AsToClientless64_Object = MibTableColumn
asToClientless64 = _AsToClientless64_Object(
    (1, 3, 6, 1, 4, 1, 3382, 2, 1, 3, 13, 1, 11),
    _AsToClientless64_Type()
)
asToClientless64.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    asToClientless64.setStatus("current")
_StatFromClientlessOctets64_Type = Counter64
_StatFromClientlessOctets64_Object = MibScalar
statFromClientlessOctets64 = _StatFromClientlessOctets64_Object(
    (1, 3, 6, 1, 4, 1, 3382, 2, 1, 3, 16),
    _StatFromClientlessOctets64_Type()
)
statFromClientlessOctets64.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statFromClientlessOctets64.setStatus("current")
_StatToClientlessOctets64_Type = Counter64
_StatToClientlessOctets64_Object = MibScalar
statToClientlessOctets64 = _StatToClientlessOctets64_Object(
    (1, 3, 6, 1, 4, 1, 3382, 2, 1, 3, 17),
    _StatToClientlessOctets64_Type()
)
statToClientlessOctets64.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statToClientlessOctets64.setStatus("current")
_TrapInfo_ObjectIdentity = ObjectIdentity
trapInfo = _TrapInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3382, 2, 2)
)
_ErrorCode_Type = Integer32
_ErrorCode_Object = MibScalar
errorCode = _ErrorCode_Object(
    (1, 3, 6, 1, 4, 1, 3382, 2, 2, 1),
    _ErrorCode_Type()
)
errorCode.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    errorCode.setStatus("current")


class _Filename_Type(OctetString):
    """Custom type filename based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_Filename_Type.__name__ = "OctetString"
_Filename_Object = MibScalar
filename = _Filename_Object(
    (1, 3, 6, 1, 4, 1, 3382, 2, 2, 2),
    _Filename_Type()
)
filename.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    filename.setStatus("current")


class _Fan_Type(OctetString):
    """Custom type fan based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_Fan_Type.__name__ = "OctetString"
_Fan_Object = MibScalar
fan = _Fan_Object(
    (1, 3, 6, 1, 4, 1, 3382, 2, 2, 3),
    _Fan_Type()
)
fan.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    fan.setStatus("current")


class _OpenFlags_Type(OctetString):
    """Custom type openFlags based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 8),
    )


_OpenFlags_Type.__name__ = "OctetString"
_OpenFlags_Object = MibScalar
openFlags = _OpenFlags_Object(
    (1, 3, 6, 1, 4, 1, 3382, 2, 2, 4),
    _OpenFlags_Type()
)
openFlags.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    openFlags.setStatus("current")
_MCode_Type = Integer32
_MCode_Object = MibScalar
mCode = _MCode_Object(
    (1, 3, 6, 1, 4, 1, 3382, 2, 2, 5),
    _MCode_Type()
)
mCode.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    mCode.setStatus("current")


class _TimeSyncMethod_Type(OctetString):
    """Custom type timeSyncMethod based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_TimeSyncMethod_Type.__name__ = "OctetString"
_TimeSyncMethod_Object = MibScalar
timeSyncMethod = _TimeSyncMethod_Object(
    (1, 3, 6, 1, 4, 1, 3382, 2, 2, 6),
    _TimeSyncMethod_Type()
)
timeSyncMethod.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    timeSyncMethod.setStatus("current")
_TotalPercent_Type = Integer32
_TotalPercent_Object = MibScalar
totalPercent = _TotalPercent_Object(
    (1, 3, 6, 1, 4, 1, 3382, 2, 2, 7),
    _TotalPercent_Type()
)
totalPercent.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    totalPercent.setStatus("current")
_TotalCount_Type = Integer32
_TotalCount_Object = MibScalar
totalCount = _TotalCount_Object(
    (1, 3, 6, 1, 4, 1, 3382, 2, 2, 8),
    _TotalCount_Type()
)
totalCount.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    totalCount.setStatus("current")
_Threshold_Type = Integer32
_Threshold_Object = MibScalar
threshold = _Threshold_Object(
    (1, 3, 6, 1, 4, 1, 3382, 2, 2, 9),
    _Threshold_Type()
)
threshold.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    threshold.setStatus("current")
_TimeWindow_Type = Integer32
_TimeWindow_Object = MibScalar
timeWindow = _TimeWindow_Object(
    (1, 3, 6, 1, 4, 1, 3382, 2, 2, 10),
    _TimeWindow_Type()
)
timeWindow.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    timeWindow.setStatus("current")


class _Disk_Type(OctetString):
    """Custom type disk based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_Disk_Type.__name__ = "OctetString"
_Disk_Object = MibScalar
disk = _Disk_Object(
    (1, 3, 6, 1, 4, 1, 3382, 2, 2, 11),
    _Disk_Type()
)
disk.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    disk.setStatus("current")


class _PowerSupplyLead_Type(OctetString):
    """Custom type powerSupplyLead based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_PowerSupplyLead_Type.__name__ = "OctetString"
_PowerSupplyLead_Object = MibScalar
powerSupplyLead = _PowerSupplyLead_Object(
    (1, 3, 6, 1, 4, 1, 3382, 2, 2, 12),
    _PowerSupplyLead_Type()
)
powerSupplyLead.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    powerSupplyLead.setStatus("current")
_ExtraInfo_Type = Integer32
_ExtraInfo_Object = MibScalar
extraInfo = _ExtraInfo_Object(
    (1, 3, 6, 1, 4, 1, 3382, 2, 2, 13),
    _ExtraInfo_Type()
)
extraInfo.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    extraInfo.setStatus("current")


class _SystemId_Type(OctetString):
    """Custom type systemId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_SystemId_Type.__name__ = "OctetString"
_SystemId_Object = MibScalar
systemId = _SystemId_Object(
    (1, 3, 6, 1, 4, 1, 3382, 2, 2, 14),
    _SystemId_Type()
)
systemId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    systemId.setStatus("current")
_CurrentValue_Type = Integer32
_CurrentValue_Object = MibScalar
currentValue = _CurrentValue_Object(
    (1, 3, 6, 1, 4, 1, 3382, 2, 2, 15),
    _CurrentValue_Type()
)
currentValue.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    currentValue.setStatus("current")


class _Name_Type(OctetString):
    """Custom type name based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_Name_Type.__name__ = "OctetString"
_Name_Object = MibScalar
name = _Name_Object(
    (1, 3, 6, 1, 4, 1, 3382, 2, 2, 16),
    _Name_Type()
)
name.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    name.setStatus("current")


class _Cur_Type(OctetString):
    """Custom type cur based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_Cur_Type.__name__ = "OctetString"
_Cur_Object = MibScalar
cur = _Cur_Object(
    (1, 3, 6, 1, 4, 1, 3382, 2, 2, 17),
    _Cur_Type()
)
cur.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cur.setStatus("current")


class _Min_Type(OctetString):
    """Custom type min based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_Min_Type.__name__ = "OctetString"
_Min_Object = MibScalar
min = _Min_Object(
    (1, 3, 6, 1, 4, 1, 3382, 2, 2, 18),
    _Min_Type()
)
min.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    min.setStatus("current")


class _Max_Type(OctetString):
    """Custom type max based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_Max_Type.__name__ = "OctetString"
_Max_Object = MibScalar
max = _Max_Object(
    (1, 3, 6, 1, 4, 1, 3382, 2, 2, 19),
    _Max_Type()
)
max.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    max.setStatus("current")


class _AlarmState_Type(Integer32):
    """Custom type alarmState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_AlarmState_Type.__name__ = "Integer32"
_AlarmState_Object = MibScalar
alarmState = _AlarmState_Object(
    (1, 3, 6, 1, 4, 1, 3382, 2, 2, 20),
    _AlarmState_Type()
)
alarmState.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    alarmState.setStatus("current")
_Limit_Type = Integer32
_Limit_Object = MibScalar
limit = _Limit_Object(
    (1, 3, 6, 1, 4, 1, 3382, 2, 2, 21),
    _Limit_Type()
)
limit.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    limit.setStatus("current")


class _TrapSeverity_Type(Integer32):
    """Custom type trapSeverity based on Integer32"""
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
        *(("critical", 1),
          ("major", 2),
          ("minor", 3),
          ("warning", 4),
          ("informational", 5))
    )


_TrapSeverity_Type.__name__ = "Integer32"
_TrapSeverity_Object = MibScalar
trapSeverity = _TrapSeverity_Object(
    (1, 3, 6, 1, 4, 1, 3382, 2, 2, 22),
    _TrapSeverity_Type()
)
trapSeverity.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    trapSeverity.setStatus("current")


class _FtpHost_Type(OctetString):
    """Custom type ftpHost based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_FtpHost_Type.__name__ = "OctetString"
_FtpHost_Object = MibScalar
ftpHost = _FtpHost_Object(
    (1, 3, 6, 1, 4, 1, 3382, 2, 2, 23),
    _FtpHost_Type()
)
ftpHost.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ftpHost.setStatus("current")


class _FtpUser_Type(OctetString):
    """Custom type ftpUser based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_FtpUser_Type.__name__ = "OctetString"
_FtpUser_Object = MibScalar
ftpUser = _FtpUser_Object(
    (1, 3, 6, 1, 4, 1, 3382, 2, 2, 24),
    _FtpUser_Type()
)
ftpUser.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ftpUser.setStatus("current")


class _FtpDirectory_Type(OctetString):
    """Custom type ftpDirectory based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_FtpDirectory_Type.__name__ = "OctetString"
_FtpDirectory_Object = MibScalar
ftpDirectory = _FtpDirectory_Object(
    (1, 3, 6, 1, 4, 1, 3382, 2, 2, 25),
    _FtpDirectory_Type()
)
ftpDirectory.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ftpDirectory.setStatus("current")
_Timeout_Type = Integer32
_Timeout_Object = MibScalar
timeout = _Timeout_Object(
    (1, 3, 6, 1, 4, 1, 3382, 2, 2, 26),
    _Timeout_Type()
)
timeout.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    timeout.setStatus("current")
_Retries_Type = Integer32
_Retries_Object = MibScalar
retries = _Retries_Object(
    (1, 3, 6, 1, 4, 1, 3382, 2, 2, 27),
    _Retries_Type()
)
retries.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    retries.setStatus("current")

# Managed Objects groups


# Notification objects

venturi2Started = NotificationType(
    (1, 3, 6, 1, 4, 1, 3382, 2, 0, 1)
)
venturi2Started.setObjects(
      *(("FOURELLE-VENTURI2-MIB", "mCode"),
        ("FOURELLE-VENTURI2-MIB", "errorCode"),
        ("FOURELLE-VENTURI2-MIB", "systemId"),
        ("FOURELLE-VENTURI2-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    venturi2Started.setStatus(
        "current"
    )

venturi2Stopped = NotificationType(
    (1, 3, 6, 1, 4, 1, 3382, 2, 0, 2)
)
venturi2Stopped.setObjects(
      *(("FOURELLE-VENTURI2-MIB", "mCode"),
        ("FOURELLE-VENTURI2-MIB", "errorCode"),
        ("FOURELLE-VENTURI2-MIB", "systemId"),
        ("FOURELLE-VENTURI2-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    venturi2Stopped.setStatus(
        "current"
    )

venturi2cpuOverload = NotificationType(
    (1, 3, 6, 1, 4, 1, 3382, 2, 0, 3)
)
venturi2cpuOverload.setObjects(
      *(("FOURELLE-VENTURI2-MIB", "mCode"),
        ("FOURELLE-VENTURI2-MIB", "errorCode"),
        ("FOURELLE-VENTURI2-MIB", "systemId"),
        ("FOURELLE-VENTURI2-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    venturi2cpuOverload.setStatus(
        "deprecated"
    )

venturi2memoryOverload = NotificationType(
    (1, 3, 6, 1, 4, 1, 3382, 2, 0, 4)
)
venturi2memoryOverload.setObjects(
      *(("FOURELLE-VENTURI2-MIB", "mCode"),
        ("FOURELLE-VENTURI2-MIB", "errorCode"),
        ("FOURELLE-VENTURI2-MIB", "systemId"),
        ("FOURELLE-VENTURI2-MIB", "currentValue"),
        ("FOURELLE-VENTURI2-MIB", "threshold"),
        ("FOURELLE-VENTURI2-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    venturi2memoryOverload.setStatus(
        "deprecated"
    )

venturi2diskOverload = NotificationType(
    (1, 3, 6, 1, 4, 1, 3382, 2, 0, 5)
)
venturi2diskOverload.setObjects(
      *(("FOURELLE-VENTURI2-MIB", "mCode"),
        ("FOURELLE-VENTURI2-MIB", "errorCode"),
        ("FOURELLE-VENTURI2-MIB", "systemId"),
        ("FOURELLE-VENTURI2-MIB", "disk"),
        ("FOURELLE-VENTURI2-MIB", "totalPercent"),
        ("FOURELLE-VENTURI2-MIB", "threshold"),
        ("FOURELLE-VENTURI2-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    venturi2diskOverload.setStatus(
        "deprecated"
    )

venturi2diskFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 3382, 2, 0, 6)
)
venturi2diskFailure.setObjects(
      *(("FOURELLE-VENTURI2-MIB", "mCode"),
        ("FOURELLE-VENTURI2-MIB", "errorCode"),
        ("FOURELLE-VENTURI2-MIB", "systemId"),
        ("FOURELLE-VENTURI2-MIB", "disk"),
        ("FOURELLE-VENTURI2-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    venturi2diskFailure.setStatus(
        "current"
    )

venturi2optimizationFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 3382, 2, 0, 7)
)
venturi2optimizationFailure.setObjects(
      *(("FOURELLE-VENTURI2-MIB", "mCode"),
        ("FOURELLE-VENTURI2-MIB", "errorCode"),
        ("FOURELLE-VENTURI2-MIB", "systemId"),
        ("FOURELLE-VENTURI2-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    venturi2optimizationFailure.setStatus(
        "deprecated"
    )

venturi2duplicatePackets = NotificationType(
    (1, 3, 6, 1, 4, 1, 3382, 2, 0, 8)
)
venturi2duplicatePackets.setObjects(
      *(("FOURELLE-VENTURI2-MIB", "mCode"),
        ("FOURELLE-VENTURI2-MIB", "errorCode"),
        ("FOURELLE-VENTURI2-MIB", "systemId"),
        ("FOURELLE-VENTURI2-MIB", "totalPercent"),
        ("FOURELLE-VENTURI2-MIB", "threshold"),
        ("FOURELLE-VENTURI2-MIB", "totalCount"),
        ("FOURELLE-VENTURI2-MIB", "timeWindow"),
        ("FOURELLE-VENTURI2-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    venturi2duplicatePackets.setStatus(
        "deprecated"
    )

venturi2droppedPackets = NotificationType(
    (1, 3, 6, 1, 4, 1, 3382, 2, 0, 9)
)
venturi2droppedPackets.setObjects(
      *(("FOURELLE-VENTURI2-MIB", "mCode"),
        ("FOURELLE-VENTURI2-MIB", "errorCode"),
        ("FOURELLE-VENTURI2-MIB", "systemId"),
        ("FOURELLE-VENTURI2-MIB", "totalPercent"),
        ("FOURELLE-VENTURI2-MIB", "threshold"),
        ("FOURELLE-VENTURI2-MIB", "totalCount"),
        ("FOURELLE-VENTURI2-MIB", "timeWindow"),
        ("FOURELLE-VENTURI2-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    venturi2droppedPackets.setStatus(
        "deprecated"
    )

venturi2outOfSequencePackets = NotificationType(
    (1, 3, 6, 1, 4, 1, 3382, 2, 0, 10)
)
venturi2outOfSequencePackets.setObjects(
      *(("FOURELLE-VENTURI2-MIB", "mCode"),
        ("FOURELLE-VENTURI2-MIB", "errorCode"),
        ("FOURELLE-VENTURI2-MIB", "systemId"),
        ("FOURELLE-VENTURI2-MIB", "totalPercent"),
        ("FOURELLE-VENTURI2-MIB", "threshold"),
        ("FOURELLE-VENTURI2-MIB", "totalCount"),
        ("FOURELLE-VENTURI2-MIB", "timeWindow"),
        ("FOURELLE-VENTURI2-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    venturi2outOfSequencePackets.setStatus(
        "deprecated"
    )

venturi2testTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3382, 2, 0, 11)
)
venturi2testTrap.setObjects(
      *(("FOURELLE-VENTURI2-MIB", "mCode"),
        ("FOURELLE-VENTURI2-MIB", "errorCode"),
        ("FOURELLE-VENTURI2-MIB", "systemId"),
        ("FOURELLE-VENTURI2-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    venturi2testTrap.setStatus(
        "current"
    )

venturi2fanAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 3382, 2, 0, 12)
)
venturi2fanAlarm.setObjects(
      *(("FOURELLE-VENTURI2-MIB", "mCode"),
        ("FOURELLE-VENTURI2-MIB", "errorCode"),
        ("FOURELLE-VENTURI2-MIB", "systemId"),
        ("FOURELLE-VENTURI2-MIB", "fan"),
        ("FOURELLE-VENTURI2-MIB", "currentValue"),
        ("FOURELLE-VENTURI2-MIB", "threshold"),
        ("FOURELLE-VENTURI2-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    venturi2fanAlarm.setStatus(
        "current"
    )

venturi2powerSupplyAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 3382, 2, 0, 13)
)
venturi2powerSupplyAlarm.setObjects(
      *(("FOURELLE-VENTURI2-MIB", "mCode"),
        ("FOURELLE-VENTURI2-MIB", "errorCode"),
        ("FOURELLE-VENTURI2-MIB", "systemId"),
        ("FOURELLE-VENTURI2-MIB", "powerSupplyLead"),
        ("FOURELLE-VENTURI2-MIB", "cur"),
        ("FOURELLE-VENTURI2-MIB", "min"),
        ("FOURELLE-VENTURI2-MIB", "max"),
        ("FOURELLE-VENTURI2-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    venturi2powerSupplyAlarm.setStatus(
        "current"
    )

venturi2temperatureAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 3382, 2, 0, 14)
)
venturi2temperatureAlarm.setObjects(
      *(("FOURELLE-VENTURI2-MIB", "mCode"),
        ("FOURELLE-VENTURI2-MIB", "errorCode"),
        ("FOURELLE-VENTURI2-MIB", "systemId"),
        ("FOURELLE-VENTURI2-MIB", "name"),
        ("FOURELLE-VENTURI2-MIB", "currentValue"),
        ("FOURELLE-VENTURI2-MIB", "threshold"),
        ("FOURELLE-VENTURI2-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    venturi2temperatureAlarm.setStatus(
        "current"
    )

venturi2licensesExceeded = NotificationType(
    (1, 3, 6, 1, 4, 1, 3382, 2, 0, 15)
)
venturi2licensesExceeded.setObjects(
      *(("FOURELLE-VENTURI2-MIB", "mCode"),
        ("FOURELLE-VENTURI2-MIB", "errorCode"),
        ("FOURELLE-VENTURI2-MIB", "systemId"),
        ("FOURELLE-VENTURI2-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    venturi2licensesExceeded.setStatus(
        "current"
    )

venturi2swapOverload = NotificationType(
    (1, 3, 6, 1, 4, 1, 3382, 2, 0, 16)
)
venturi2swapOverload.setObjects(
      *(("FOURELLE-VENTURI2-MIB", "mCode"),
        ("FOURELLE-VENTURI2-MIB", "errorCode"),
        ("FOURELLE-VENTURI2-MIB", "systemId"),
        ("FOURELLE-VENTURI2-MIB", "currentValue"),
        ("FOURELLE-VENTURI2-MIB", "threshold"),
        ("FOURELLE-VENTURI2-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    venturi2swapOverload.setStatus(
        "current"
    )

venturi2fileOpenFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 3382, 2, 0, 17)
)
venturi2fileOpenFailed.setObjects(
      *(("FOURELLE-VENTURI2-MIB", "mCode"),
        ("FOURELLE-VENTURI2-MIB", "errorCode"),
        ("FOURELLE-VENTURI2-MIB", "systemId"),
        ("FOURELLE-VENTURI2-MIB", "filename"),
        ("FOURELLE-VENTURI2-MIB", "openFlags"),
        ("FOURELLE-VENTURI2-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    venturi2fileOpenFailed.setStatus(
        "current"
    )

venturi2timeSyncError = NotificationType(
    (1, 3, 6, 1, 4, 1, 3382, 2, 0, 18)
)
venturi2timeSyncError.setObjects(
      *(("FOURELLE-VENTURI2-MIB", "mCode"),
        ("FOURELLE-VENTURI2-MIB", "errorCode"),
        ("FOURELLE-VENTURI2-MIB", "systemId"),
        ("FOURELLE-VENTURI2-MIB", "timeSyncMethod"),
        ("FOURELLE-VENTURI2-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    venturi2timeSyncError.setStatus(
        "deprecated"
    )

venturi2internalError = NotificationType(
    (1, 3, 6, 1, 4, 1, 3382, 2, 0, 19)
)
venturi2internalError.setObjects(
      *(("FOURELLE-VENTURI2-MIB", "mCode"),
        ("FOURELLE-VENTURI2-MIB", "errorCode"),
        ("FOURELLE-VENTURI2-MIB", "systemId"),
        ("FOURELLE-VENTURI2-MIB", "extraInfo"),
        ("FOURELLE-VENTURI2-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    venturi2internalError.setStatus(
        "deprecated"
    )

venturi2moduleInitFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 3382, 2, 0, 20)
)
venturi2moduleInitFailed.setObjects(
      *(("FOURELLE-VENTURI2-MIB", "mCode"),
        ("FOURELLE-VENTURI2-MIB", "errorCode"),
        ("FOURELLE-VENTURI2-MIB", "systemId"),
        ("FOURELLE-VENTURI2-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    venturi2moduleInitFailed.setStatus(
        "current"
    )

venturi2serverOverload = NotificationType(
    (1, 3, 6, 1, 4, 1, 3382, 2, 0, 21)
)
venturi2serverOverload.setObjects(
      *(("FOURELLE-VENTURI2-MIB", "mCode"),
        ("FOURELLE-VENTURI2-MIB", "errorCode"),
        ("FOURELLE-VENTURI2-MIB", "systemId"),
        ("FOURELLE-VENTURI2-MIB", "threshold"),
        ("FOURELLE-VENTURI2-MIB", "limit"),
        ("FOURELLE-VENTURI2-MIB", "alarmState"),
        ("FOURELLE-VENTURI2-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    venturi2serverOverload.setStatus(
        "deprecated"
    )

venturi2statsCollectionTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3382, 2, 0, 22)
)
venturi2statsCollectionTrap.setObjects(
      *(("FOURELLE-VENTURI2-MIB", "mCode"),
        ("FOURELLE-VENTURI2-MIB", "errorCode"),
        ("FOURELLE-VENTURI2-MIB", "systemId"),
        ("FOURELLE-VENTURI2-MIB", "trapSeverity"),
        ("FOURELLE-VENTURI2-MIB", "filename"),
        ("FOURELLE-VENTURI2-MIB", "ftpHost"),
        ("FOURELLE-VENTURI2-MIB", "ftpUser"),
        ("FOURELLE-VENTURI2-MIB", "ftpDirectory"),
        ("FOURELLE-VENTURI2-MIB", "timeout"),
        ("FOURELLE-VENTURI2-MIB", "retries"))
)
if mibBuilder.loadTexts:
    venturi2statsCollectionTrap.setStatus(
        "current"
    )

venturi2logCollectionTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3382, 2, 0, 23)
)
venturi2logCollectionTrap.setObjects(
      *(("FOURELLE-VENTURI2-MIB", "mCode"),
        ("FOURELLE-VENTURI2-MIB", "errorCode"),
        ("FOURELLE-VENTURI2-MIB", "systemId"),
        ("FOURELLE-VENTURI2-MIB", "trapSeverity"),
        ("FOURELLE-VENTURI2-MIB", "filename"),
        ("FOURELLE-VENTURI2-MIB", "ftpHost"),
        ("FOURELLE-VENTURI2-MIB", "ftpUser"),
        ("FOURELLE-VENTURI2-MIB", "ftpDirectory"),
        ("FOURELLE-VENTURI2-MIB", "timeout"),
        ("FOURELLE-VENTURI2-MIB", "retries"))
)
if mibBuilder.loadTexts:
    venturi2logCollectionTrap.setStatus(
        "current"
    )

venturi2networkErrorTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3382, 2, 0, 24)
)
venturi2networkErrorTrap.setObjects(
      *(("FOURELLE-VENTURI2-MIB", "mCode"),
        ("FOURELLE-VENTURI2-MIB", "errorCode"),
        ("FOURELLE-VENTURI2-MIB", "systemId"),
        ("FOURELLE-VENTURI2-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    venturi2networkErrorTrap.setStatus(
        "current"
    )

venturi2kernelTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3382, 2, 0, 25)
)
venturi2kernelTrap.setObjects(
      *(("FOURELLE-VENTURI2-MIB", "mCode"),
        ("FOURELLE-VENTURI2-MIB", "errorCode"),
        ("FOURELLE-VENTURI2-MIB", "systemId"),
        ("FOURELLE-VENTURI2-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    venturi2kernelTrap.setStatus(
        "current"
    )

venturi2licenseTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3382, 2, 0, 26)
)
venturi2licenseTrap.setObjects(
      *(("FOURELLE-VENTURI2-MIB", "mCode"),
        ("FOURELLE-VENTURI2-MIB", "errorCode"),
        ("FOURELLE-VENTURI2-MIB", "systemId"),
        ("FOURELLE-VENTURI2-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    venturi2licenseTrap.setStatus(
        "current"
    )

venturi2sharedMemoryTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3382, 2, 0, 27)
)
venturi2sharedMemoryTrap.setObjects(
      *(("FOURELLE-VENTURI2-MIB", "mCode"),
        ("FOURELLE-VENTURI2-MIB", "errorCode"),
        ("FOURELLE-VENTURI2-MIB", "systemId"),
        ("FOURELLE-VENTURI2-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    venturi2sharedMemoryTrap.setStatus(
        "current"
    )

venturi2fileSystemTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3382, 2, 0, 28)
)
venturi2fileSystemTrap.setObjects(
      *(("FOURELLE-VENTURI2-MIB", "mCode"),
        ("FOURELLE-VENTURI2-MIB", "errorCode"),
        ("FOURELLE-VENTURI2-MIB", "systemId"),
        ("FOURELLE-VENTURI2-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    venturi2fileSystemTrap.setStatus(
        "current"
    )

venturi2swapOverloadClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 3382, 2, 0, 30)
)
venturi2swapOverloadClear.setObjects(
      *(("FOURELLE-VENTURI2-MIB", "mCode"),
        ("FOURELLE-VENTURI2-MIB", "errorCode"),
        ("FOURELLE-VENTURI2-MIB", "systemId"),
        ("FOURELLE-VENTURI2-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    venturi2swapOverloadClear.setStatus(
        "current"
    )

venturi2networkClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 3382, 2, 0, 31)
)
venturi2networkClear.setObjects(
      *(("FOURELLE-VENTURI2-MIB", "mCode"),
        ("FOURELLE-VENTURI2-MIB", "errorCode"),
        ("FOURELLE-VENTURI2-MIB", "systemId"),
        ("FOURELLE-VENTURI2-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    venturi2networkClear.setStatus(
        "current"
    )

venturi2kernelClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 3382, 2, 0, 32)
)
venturi2kernelClear.setObjects(
      *(("FOURELLE-VENTURI2-MIB", "mCode"),
        ("FOURELLE-VENTURI2-MIB", "errorCode"),
        ("FOURELLE-VENTURI2-MIB", "systemId"),
        ("FOURELLE-VENTURI2-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    venturi2kernelClear.setStatus(
        "current"
    )

venturi2licenseClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 3382, 2, 0, 33)
)
venturi2licenseClear.setObjects(
      *(("FOURELLE-VENTURI2-MIB", "mCode"),
        ("FOURELLE-VENTURI2-MIB", "errorCode"),
        ("FOURELLE-VENTURI2-MIB", "systemId"),
        ("FOURELLE-VENTURI2-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    venturi2licenseClear.setStatus(
        "current"
    )

venturi2sharedMemoryClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 3382, 2, 0, 34)
)
venturi2sharedMemoryClear.setObjects(
      *(("FOURELLE-VENTURI2-MIB", "mCode"),
        ("FOURELLE-VENTURI2-MIB", "errorCode"),
        ("FOURELLE-VENTURI2-MIB", "systemId"),
        ("FOURELLE-VENTURI2-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    venturi2sharedMemoryClear.setStatus(
        "current"
    )

venturi2fileSystemClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 3382, 2, 0, 35)
)
venturi2fileSystemClear.setObjects(
      *(("FOURELLE-VENTURI2-MIB", "mCode"),
        ("FOURELLE-VENTURI2-MIB", "errorCode"),
        ("FOURELLE-VENTURI2-MIB", "systemId"),
        ("FOURELLE-VENTURI2-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    venturi2fileSystemClear.setStatus(
        "current"
    )

venturi2TCPOverload = NotificationType(
    (1, 3, 6, 1, 4, 1, 3382, 2, 0, 36)
)
venturi2TCPOverload.setObjects(
      *(("FOURELLE-VENTURI2-MIB", "mCode"),
        ("FOURELLE-VENTURI2-MIB", "errorCode"),
        ("FOURELLE-VENTURI2-MIB", "systemId"),
        ("FOURELLE-VENTURI2-MIB", "threshold"),
        ("FOURELLE-VENTURI2-MIB", "limit"),
        ("FOURELLE-VENTURI2-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    venturi2TCPOverload.setStatus(
        "current"
    )

venturi2TCPOverloadClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 3382, 2, 0, 37)
)
venturi2TCPOverloadClear.setObjects(
      *(("FOURELLE-VENTURI2-MIB", "mCode"),
        ("FOURELLE-VENTURI2-MIB", "errorCode"),
        ("FOURELLE-VENTURI2-MIB", "systemId"),
        ("FOURELLE-VENTURI2-MIB", "threshold"),
        ("FOURELLE-VENTURI2-MIB", "limit"),
        ("FOURELLE-VENTURI2-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    venturi2TCPOverloadClear.setStatus(
        "current"
    )

venturi2CacheOverload = NotificationType(
    (1, 3, 6, 1, 4, 1, 3382, 2, 0, 38)
)
venturi2CacheOverload.setObjects(
      *(("FOURELLE-VENTURI2-MIB", "mCode"),
        ("FOURELLE-VENTURI2-MIB", "errorCode"),
        ("FOURELLE-VENTURI2-MIB", "systemId"),
        ("FOURELLE-VENTURI2-MIB", "disk"),
        ("FOURELLE-VENTURI2-MIB", "totalPercent"),
        ("FOURELLE-VENTURI2-MIB", "threshold"),
        ("FOURELLE-VENTURI2-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    venturi2CacheOverload.setStatus(
        "current"
    )

venturi2CacheOverloadClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 3382, 2, 0, 39)
)
venturi2CacheOverloadClear.setObjects(
      *(("FOURELLE-VENTURI2-MIB", "mCode"),
        ("FOURELLE-VENTURI2-MIB", "errorCode"),
        ("FOURELLE-VENTURI2-MIB", "systemId"),
        ("FOURELLE-VENTURI2-MIB", "disk"),
        ("FOURELLE-VENTURI2-MIB", "totalPercent"),
        ("FOURELLE-VENTURI2-MIB", "threshold"),
        ("FOURELLE-VENTURI2-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    venturi2CacheOverloadClear.setStatus(
        "current"
    )

venturi2LogOverload = NotificationType(
    (1, 3, 6, 1, 4, 1, 3382, 2, 0, 40)
)
venturi2LogOverload.setObjects(
      *(("FOURELLE-VENTURI2-MIB", "mCode"),
        ("FOURELLE-VENTURI2-MIB", "errorCode"),
        ("FOURELLE-VENTURI2-MIB", "systemId"),
        ("FOURELLE-VENTURI2-MIB", "disk"),
        ("FOURELLE-VENTURI2-MIB", "totalPercent"),
        ("FOURELLE-VENTURI2-MIB", "threshold"),
        ("FOURELLE-VENTURI2-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    venturi2LogOverload.setStatus(
        "current"
    )

venturi2LogOverloadClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 3382, 2, 0, 41)
)
venturi2LogOverloadClear.setObjects(
      *(("FOURELLE-VENTURI2-MIB", "mCode"),
        ("FOURELLE-VENTURI2-MIB", "errorCode"),
        ("FOURELLE-VENTURI2-MIB", "systemId"),
        ("FOURELLE-VENTURI2-MIB", "disk"),
        ("FOURELLE-VENTURI2-MIB", "totalPercent"),
        ("FOURELLE-VENTURI2-MIB", "threshold"),
        ("FOURELLE-VENTURI2-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    venturi2LogOverloadClear.setStatus(
        "current"
    )

venturi2URLCollectionTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3382, 2, 0, 42)
)
venturi2URLCollectionTrap.setObjects(
      *(("FOURELLE-VENTURI2-MIB", "mCode"),
        ("FOURELLE-VENTURI2-MIB", "errorCode"),
        ("FOURELLE-VENTURI2-MIB", "systemId"),
        ("FOURELLE-VENTURI2-MIB", "trapSeverity"),
        ("FOURELLE-VENTURI2-MIB", "filename"),
        ("FOURELLE-VENTURI2-MIB", "ftpHost"),
        ("FOURELLE-VENTURI2-MIB", "ftpUser"),
        ("FOURELLE-VENTURI2-MIB", "ftpDirectory"),
        ("FOURELLE-VENTURI2-MIB", "timeout"),
        ("FOURELLE-VENTURI2-MIB", "retries"))
)
if mibBuilder.loadTexts:
    venturi2URLCollectionTrap.setStatus(
        "current"
    )

venturi2LowCriticalBufs = NotificationType(
    (1, 3, 6, 1, 4, 1, 3382, 2, 0, 43)
)
venturi2LowCriticalBufs.setObjects(
      *(("FOURELLE-VENTURI2-MIB", "mCode"),
        ("FOURELLE-VENTURI2-MIB", "errorCode"),
        ("FOURELLE-VENTURI2-MIB", "systemId"),
        ("FOURELLE-VENTURI2-MIB", "currentValue"),
        ("FOURELLE-VENTURI2-MIB", "threshold"),
        ("FOURELLE-VENTURI2-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    venturi2LowCriticalBufs.setStatus(
        "current"
    )

venturi2LowCriticalBufsClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 3382, 2, 0, 44)
)
venturi2LowCriticalBufsClear.setObjects(
      *(("FOURELLE-VENTURI2-MIB", "mCode"),
        ("FOURELLE-VENTURI2-MIB", "errorCode"),
        ("FOURELLE-VENTURI2-MIB", "systemId"),
        ("FOURELLE-VENTURI2-MIB", "currentValue"),
        ("FOURELLE-VENTURI2-MIB", "threshold"),
        ("FOURELLE-VENTURI2-MIB", "trapSeverity"))
)
if mibBuilder.loadTexts:
    venturi2LowCriticalBufsClear.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "FOURELLE-VENTURI2-MIB",
    **{"venturi2": venturi2,
       "traps": traps,
       "venturi2Started": venturi2Started,
       "venturi2Stopped": venturi2Stopped,
       "venturi2cpuOverload": venturi2cpuOverload,
       "venturi2memoryOverload": venturi2memoryOverload,
       "venturi2diskOverload": venturi2diskOverload,
       "venturi2diskFailure": venturi2diskFailure,
       "venturi2optimizationFailure": venturi2optimizationFailure,
       "venturi2duplicatePackets": venturi2duplicatePackets,
       "venturi2droppedPackets": venturi2droppedPackets,
       "venturi2outOfSequencePackets": venturi2outOfSequencePackets,
       "venturi2testTrap": venturi2testTrap,
       "venturi2fanAlarm": venturi2fanAlarm,
       "venturi2powerSupplyAlarm": venturi2powerSupplyAlarm,
       "venturi2temperatureAlarm": venturi2temperatureAlarm,
       "venturi2licensesExceeded": venturi2licensesExceeded,
       "venturi2swapOverload": venturi2swapOverload,
       "venturi2fileOpenFailed": venturi2fileOpenFailed,
       "venturi2timeSyncError": venturi2timeSyncError,
       "venturi2internalError": venturi2internalError,
       "venturi2moduleInitFailed": venturi2moduleInitFailed,
       "venturi2serverOverload": venturi2serverOverload,
       "venturi2statsCollectionTrap": venturi2statsCollectionTrap,
       "venturi2logCollectionTrap": venturi2logCollectionTrap,
       "venturi2networkErrorTrap": venturi2networkErrorTrap,
       "venturi2kernelTrap": venturi2kernelTrap,
       "venturi2licenseTrap": venturi2licenseTrap,
       "venturi2sharedMemoryTrap": venturi2sharedMemoryTrap,
       "venturi2fileSystemTrap": venturi2fileSystemTrap,
       "venturi2swapOverloadClear": venturi2swapOverloadClear,
       "venturi2networkClear": venturi2networkClear,
       "venturi2kernelClear": venturi2kernelClear,
       "venturi2licenseClear": venturi2licenseClear,
       "venturi2sharedMemoryClear": venturi2sharedMemoryClear,
       "venturi2fileSystemClear": venturi2fileSystemClear,
       "venturi2TCPOverload": venturi2TCPOverload,
       "venturi2TCPOverloadClear": venturi2TCPOverloadClear,
       "venturi2CacheOverload": venturi2CacheOverload,
       "venturi2CacheOverloadClear": venturi2CacheOverloadClear,
       "venturi2LogOverload": venturi2LogOverload,
       "venturi2LogOverloadClear": venturi2LogOverloadClear,
       "venturi2URLCollectionTrap": venturi2URLCollectionTrap,
       "venturi2LowCriticalBufs": venturi2LowCriticalBufs,
       "venturi2LowCriticalBufsClear": venturi2LowCriticalBufsClear,
       "general": general,
       "system": system,
       "sysType": sysType,
       "sysVersion": sysVersion,
       "sysStartTime": sysStartTime,
       "sysUpTime": sysUpTime,
       "sysBuildId": sysBuildId,
       "sysLicenses": sysLicenses,
       "sysLicensesUsed": sysLicensesUsed,
       "sysCustomerId": sysCustomerId,
       "sysNumCPUs": sysNumCPUs,
       "statistics": statistics,
       "statOnlineUsers": statOnlineUsers,
       "statCurrentConnections": statCurrentConnections,
       "statTotalConnections": statTotalConnections,
       "statTotalConnectionDuration": statTotalConnectionDuration,
       "statVTPInOctets": statVTPInOctets,
       "statVTPOutOctets": statVTPOutOctets,
       "statVTPInPkts": statVTPInPkts,
       "statVTPOutPkts": statVTPOutPkts,
       "statToCompOctets": statToCompOctets,
       "statFromCompOctets": statFromCompOctets,
       "statExtInOctets": statExtInOctets,
       "statExtOutOctets": statExtOutOctets,
       "appStatsTable": appStatsTable,
       "appStatsEntry": appStatsEntry,
       "asRowId": asRowId,
       "asProtocol": asProtocol,
       "asFromExternal": asFromExternal,
       "asToExternal": asToExternal,
       "asFromTransport": asFromTransport,
       "asToTransport": asToTransport,
       "asCurConnections": asCurConnections,
       "asNumRequests": asNumRequests,
       "asMaxRequests": asMaxRequests,
       "asFromClientless": asFromClientless,
       "asToClientless": asToClientless,
       "statCpuUtilization": statCpuUtilization,
       "statQdepth2comp": statQdepth2comp,
       "statFromClientlessOctets": statFromClientlessOctets,
       "statToClientlessOctets": statToClientlessOctets,
       "statistics64": statistics64,
       "statVTPInOctets64": statVTPInOctets64,
       "statVTPOutOctets64": statVTPOutOctets64,
       "statVTPInPkts64": statVTPInPkts64,
       "statVTPOutPkts64": statVTPOutPkts64,
       "statToCompOctets64": statToCompOctets64,
       "statFromCompOctets64": statFromCompOctets64,
       "statExtInOctets64": statExtInOctets64,
       "statExtOutOctets64": statExtOutOctets64,
       "appStatsTable64": appStatsTable64,
       "appStatsEntry64": appStatsEntry64,
       "asRowId64": asRowId64,
       "asProtocol64": asProtocol64,
       "asFromExternal64": asFromExternal64,
       "asToExternal64": asToExternal64,
       "asFromTransport64": asFromTransport64,
       "asToTransport64": asToTransport64,
       "asCurConnections64": asCurConnections64,
       "asNumRequests64": asNumRequests64,
       "asMaxRequests64": asMaxRequests64,
       "asFromClientless64": asFromClientless64,
       "asToClientless64": asToClientless64,
       "statFromClientlessOctets64": statFromClientlessOctets64,
       "statToClientlessOctets64": statToClientlessOctets64,
       "trapInfo": trapInfo,
       "errorCode": errorCode,
       "filename": filename,
       "fan": fan,
       "openFlags": openFlags,
       "mCode": mCode,
       "timeSyncMethod": timeSyncMethod,
       "totalPercent": totalPercent,
       "totalCount": totalCount,
       "threshold": threshold,
       "timeWindow": timeWindow,
       "disk": disk,
       "powerSupplyLead": powerSupplyLead,
       "extraInfo": extraInfo,
       "systemId": systemId,
       "currentValue": currentValue,
       "name": name,
       "cur": cur,
       "min": min,
       "max": max,
       "alarmState": alarmState,
       "limit": limit,
       "trapSeverity": trapSeverity,
       "ftpHost": ftpHost,
       "ftpUser": ftpUser,
       "ftpDirectory": ftpDirectory,
       "timeout": timeout,
       "retries": retries}
)
