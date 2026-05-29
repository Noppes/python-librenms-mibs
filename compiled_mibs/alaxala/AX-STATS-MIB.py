# SNMP MIB module (AX-STATS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\alaxala\AX-STATS-MIB

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

axStats = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 1)
)
if mibBuilder.loadTexts:
    axStats.setRevisions(
        ("2013-10-03 00:00",
         "2013-06-24 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AxIfStats_ObjectIdentity = ObjectIdentity
axIfStats = _AxIfStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 1, 4)
)
_AxIfStatsTable_Object = MibTable
axIfStatsTable = _AxIfStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 1, 4, 1)
)
if mibBuilder.loadTexts:
    axIfStatsTable.setStatus("current")
_AxIfStatsEntry_Object = MibTableRow
axIfStatsEntry = _AxIfStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 1, 4, 1, 1)
)
axIfStatsEntry.setIndexNames(
    (0, "AX-STATS-MIB", "axIfStatsIndex"),
)
if mibBuilder.loadTexts:
    axIfStatsEntry.setStatus("current")
_AxIfStatsIndex_Type = Integer32
_AxIfStatsIndex_Object = MibTableColumn
axIfStatsIndex = _AxIfStatsIndex_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 1, 4, 1, 1, 1),
    _AxIfStatsIndex_Type()
)
axIfStatsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    axIfStatsIndex.setStatus("current")
_AxIfStatsName_Type = DisplayString
_AxIfStatsName_Object = MibTableColumn
axIfStatsName = _AxIfStatsName_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 1, 4, 1, 1, 2),
    _AxIfStatsName_Type()
)
axIfStatsName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axIfStatsName.setStatus("current")
_AxIfStatsInMegaOctets_Type = Counter32
_AxIfStatsInMegaOctets_Object = MibTableColumn
axIfStatsInMegaOctets = _AxIfStatsInMegaOctets_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 1, 4, 1, 1, 3),
    _AxIfStatsInMegaOctets_Type()
)
axIfStatsInMegaOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axIfStatsInMegaOctets.setStatus("current")
_AxIfStatsInUcastMegaPkts_Type = Counter32
_AxIfStatsInUcastMegaPkts_Object = MibTableColumn
axIfStatsInUcastMegaPkts = _AxIfStatsInUcastMegaPkts_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 1, 4, 1, 1, 4),
    _AxIfStatsInUcastMegaPkts_Type()
)
axIfStatsInUcastMegaPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axIfStatsInUcastMegaPkts.setStatus("current")
_AxIfStatsInMulticastMegaPkts_Type = Counter32
_AxIfStatsInMulticastMegaPkts_Object = MibTableColumn
axIfStatsInMulticastMegaPkts = _AxIfStatsInMulticastMegaPkts_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 1, 4, 1, 1, 5),
    _AxIfStatsInMulticastMegaPkts_Type()
)
axIfStatsInMulticastMegaPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axIfStatsInMulticastMegaPkts.setStatus("current")
_AxIfStatsInBroadcastMegaPkts_Type = Counter32
_AxIfStatsInBroadcastMegaPkts_Object = MibTableColumn
axIfStatsInBroadcastMegaPkts = _AxIfStatsInBroadcastMegaPkts_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 1, 4, 1, 1, 6),
    _AxIfStatsInBroadcastMegaPkts_Type()
)
axIfStatsInBroadcastMegaPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axIfStatsInBroadcastMegaPkts.setStatus("current")
_AxIfStatsOutMegaOctets_Type = Counter32
_AxIfStatsOutMegaOctets_Object = MibTableColumn
axIfStatsOutMegaOctets = _AxIfStatsOutMegaOctets_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 1, 4, 1, 1, 7),
    _AxIfStatsOutMegaOctets_Type()
)
axIfStatsOutMegaOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axIfStatsOutMegaOctets.setStatus("current")
_AxIfStatsOutUcastMegaPkts_Type = Counter32
_AxIfStatsOutUcastMegaPkts_Object = MibTableColumn
axIfStatsOutUcastMegaPkts = _AxIfStatsOutUcastMegaPkts_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 1, 4, 1, 1, 8),
    _AxIfStatsOutUcastMegaPkts_Type()
)
axIfStatsOutUcastMegaPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axIfStatsOutUcastMegaPkts.setStatus("current")
_AxIfStatsOutMulticastMegaPkts_Type = Counter32
_AxIfStatsOutMulticastMegaPkts_Object = MibTableColumn
axIfStatsOutMulticastMegaPkts = _AxIfStatsOutMulticastMegaPkts_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 1, 4, 1, 1, 9),
    _AxIfStatsOutMulticastMegaPkts_Type()
)
axIfStatsOutMulticastMegaPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axIfStatsOutMulticastMegaPkts.setStatus("current")
_AxIfStatsOutBroadcastMegaPkts_Type = Counter32
_AxIfStatsOutBroadcastMegaPkts_Object = MibTableColumn
axIfStatsOutBroadcastMegaPkts = _AxIfStatsOutBroadcastMegaPkts_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 1, 4, 1, 1, 10),
    _AxIfStatsOutBroadcastMegaPkts_Type()
)
axIfStatsOutBroadcastMegaPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axIfStatsOutBroadcastMegaPkts.setStatus("current")
_AxIfStatsHighSpeed_Type = Counter32
_AxIfStatsHighSpeed_Object = MibTableColumn
axIfStatsHighSpeed = _AxIfStatsHighSpeed_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 1, 4, 1, 1, 11),
    _AxIfStatsHighSpeed_Type()
)
axIfStatsHighSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axIfStatsHighSpeed.setStatus("current")
_AxUrpf_ObjectIdentity = ObjectIdentity
axUrpf = _AxUrpf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 1, 13)
)
_AxUrpfIpv4DiscStrictPkts_Type = Counter64
_AxUrpfIpv4DiscStrictPkts_Object = MibScalar
axUrpfIpv4DiscStrictPkts = _AxUrpfIpv4DiscStrictPkts_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 1, 13, 1),
    _AxUrpfIpv4DiscStrictPkts_Type()
)
axUrpfIpv4DiscStrictPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axUrpfIpv4DiscStrictPkts.setStatus("current")
_AxUrpfIpv6DiscStrictPkts_Type = Counter64
_AxUrpfIpv6DiscStrictPkts_Object = MibScalar
axUrpfIpv6DiscStrictPkts = _AxUrpfIpv6DiscStrictPkts_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 1, 13, 2),
    _AxUrpfIpv6DiscStrictPkts_Type()
)
axUrpfIpv6DiscStrictPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axUrpfIpv6DiscStrictPkts.setStatus("current")
_AxUrpfIpv4DiscLoosePkts_Type = Counter64
_AxUrpfIpv4DiscLoosePkts_Object = MibScalar
axUrpfIpv4DiscLoosePkts = _AxUrpfIpv4DiscLoosePkts_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 1, 13, 3),
    _AxUrpfIpv4DiscLoosePkts_Type()
)
axUrpfIpv4DiscLoosePkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axUrpfIpv4DiscLoosePkts.setStatus("current")
_AxUrpfIpv6DiscLoosePkts_Type = Counter64
_AxUrpfIpv6DiscLoosePkts_Object = MibScalar
axUrpfIpv6DiscLoosePkts = _AxUrpfIpv6DiscLoosePkts_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 1, 13, 4),
    _AxUrpfIpv6DiscLoosePkts_Type()
)
axUrpfIpv6DiscLoosePkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axUrpfIpv6DiscLoosePkts.setStatus("current")
_AxUrpfIfStatsTable_Object = MibTable
axUrpfIfStatsTable = _AxUrpfIfStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 1, 13, 5)
)
if mibBuilder.loadTexts:
    axUrpfIfStatsTable.setStatus("current")
_AxUrpfIfStatsEntry_Object = MibTableRow
axUrpfIfStatsEntry = _AxUrpfIfStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 1, 13, 5, 1)
)
axUrpfIfStatsEntry.setIndexNames(
    (0, "AX-STATS-MIB", "axUrpfIfStatsIndex"),
)
if mibBuilder.loadTexts:
    axUrpfIfStatsEntry.setStatus("current")
_AxUrpfIfStatsIndex_Type = Integer32
_AxUrpfIfStatsIndex_Object = MibTableColumn
axUrpfIfStatsIndex = _AxUrpfIfStatsIndex_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 1, 13, 5, 1, 1),
    _AxUrpfIfStatsIndex_Type()
)
axUrpfIfStatsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    axUrpfIfStatsIndex.setStatus("current")
_AxUrpfIfStatsIpv4DiscPkts_Type = Counter64
_AxUrpfIfStatsIpv4DiscPkts_Object = MibTableColumn
axUrpfIfStatsIpv4DiscPkts = _AxUrpfIfStatsIpv4DiscPkts_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 1, 13, 5, 1, 2),
    _AxUrpfIfStatsIpv4DiscPkts_Type()
)
axUrpfIfStatsIpv4DiscPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axUrpfIfStatsIpv4DiscPkts.setStatus("current")
_AxUrpfIfStatsIpv6DiscPkts_Type = Counter64
_AxUrpfIfStatsIpv6DiscPkts_Object = MibTableColumn
axUrpfIfStatsIpv6DiscPkts = _AxUrpfIfStatsIpv6DiscPkts_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 1, 13, 5, 1, 3),
    _AxUrpfIfStatsIpv6DiscPkts_Type()
)
axUrpfIfStatsIpv6DiscPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axUrpfIfStatsIpv6DiscPkts.setStatus("current")
_AxStatsConformance_ObjectIdentity = ObjectIdentity
axStatsConformance = _AxStatsConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 1, 1000)
)
_AxStatsCompliances_ObjectIdentity = ObjectIdentity
axStatsCompliances = _AxStatsCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 1, 1000, 1)
)
_AxStatsGroups_ObjectIdentity = ObjectIdentity
axStatsGroups = _AxStatsGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 1, 1000, 2)
)

# Managed Objects groups

axStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 1, 1000, 2, 1)
)
axStatsGroup.setObjects(
      *(("AX-STATS-MIB", "axIfStatsName"),
        ("AX-STATS-MIB", "axIfStatsInMegaOctets"),
        ("AX-STATS-MIB", "axIfStatsInUcastMegaPkts"),
        ("AX-STATS-MIB", "axIfStatsInMulticastMegaPkts"),
        ("AX-STATS-MIB", "axIfStatsInBroadcastMegaPkts"),
        ("AX-STATS-MIB", "axIfStatsOutMegaOctets"),
        ("AX-STATS-MIB", "axIfStatsOutUcastMegaPkts"),
        ("AX-STATS-MIB", "axIfStatsOutMulticastMegaPkts"),
        ("AX-STATS-MIB", "axIfStatsOutBroadcastMegaPkts"),
        ("AX-STATS-MIB", "axIfStatsHighSpeed"),
        ("AX-STATS-MIB", "axUrpfIpv4DiscStrictPkts"),
        ("AX-STATS-MIB", "axUrpfIpv6DiscStrictPkts"),
        ("AX-STATS-MIB", "axUrpfIpv4DiscLoosePkts"),
        ("AX-STATS-MIB", "axUrpfIpv6DiscLoosePkts"),
        ("AX-STATS-MIB", "axUrpfIfStatsIpv4DiscPkts"),
        ("AX-STATS-MIB", "axUrpfIfStatsIpv6DiscPkts"))
)
if mibBuilder.loadTexts:
    axStatsGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

axStatsCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 1, 1000, 1, 1)
)
axStatsCompliance.setObjects(
    ("AX-STATS-MIB", "axStatsGroup")
)
if mibBuilder.loadTexts:
    axStatsCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "AX-STATS-MIB",
    **{"axStats": axStats,
       "axIfStats": axIfStats,
       "axIfStatsTable": axIfStatsTable,
       "axIfStatsEntry": axIfStatsEntry,
       "axIfStatsIndex": axIfStatsIndex,
       "axIfStatsName": axIfStatsName,
       "axIfStatsInMegaOctets": axIfStatsInMegaOctets,
       "axIfStatsInUcastMegaPkts": axIfStatsInUcastMegaPkts,
       "axIfStatsInMulticastMegaPkts": axIfStatsInMulticastMegaPkts,
       "axIfStatsInBroadcastMegaPkts": axIfStatsInBroadcastMegaPkts,
       "axIfStatsOutMegaOctets": axIfStatsOutMegaOctets,
       "axIfStatsOutUcastMegaPkts": axIfStatsOutUcastMegaPkts,
       "axIfStatsOutMulticastMegaPkts": axIfStatsOutMulticastMegaPkts,
       "axIfStatsOutBroadcastMegaPkts": axIfStatsOutBroadcastMegaPkts,
       "axIfStatsHighSpeed": axIfStatsHighSpeed,
       "axUrpf": axUrpf,
       "axUrpfIpv4DiscStrictPkts": axUrpfIpv4DiscStrictPkts,
       "axUrpfIpv6DiscStrictPkts": axUrpfIpv6DiscStrictPkts,
       "axUrpfIpv4DiscLoosePkts": axUrpfIpv4DiscLoosePkts,
       "axUrpfIpv6DiscLoosePkts": axUrpfIpv6DiscLoosePkts,
       "axUrpfIfStatsTable": axUrpfIfStatsTable,
       "axUrpfIfStatsEntry": axUrpfIfStatsEntry,
       "axUrpfIfStatsIndex": axUrpfIfStatsIndex,
       "axUrpfIfStatsIpv4DiscPkts": axUrpfIfStatsIpv4DiscPkts,
       "axUrpfIfStatsIpv6DiscPkts": axUrpfIfStatsIpv6DiscPkts,
       "axStatsConformance": axStatsConformance,
       "axStatsCompliances": axStatsCompliances,
       "axStatsCompliance": axStatsCompliance,
       "axStatsGroups": axStatsGroups,
       "axStatsGroup": axStatsGroup}
)
