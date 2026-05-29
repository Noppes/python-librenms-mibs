# SNMP MIB module (STORMSHIELD-OVPN-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\stormshield\STORMSHIELD-OVPN-MIB

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

(stormshieldMIB,) = mibBuilder.importSymbols(
    "STORMSHIELD-SMI-MIB",
    "stormshieldMIB")


# MODULE-IDENTITY

snsOVPN = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 11256, 1, 17)
)
if mibBuilder.loadTexts:
    snsOVPN.setRevisions(
        ("2020-05-25 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_SnsOVPNStatsTable_Object = MibTable
snsOVPNStatsTable = _SnsOVPNStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 11256, 1, 17, 1)
)
if mibBuilder.loadTexts:
    snsOVPNStatsTable.setStatus("current")
_SnsOVPNStatsEntry_Object = MibTableRow
snsOVPNStatsEntry = _SnsOVPNStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 11256, 1, 17, 1, 1)
)
snsOVPNStatsEntry.setIndexNames(
    (0, "STORMSHIELD-OVPN-MIB", "snsOVPNEntryIndex"),
)
if mibBuilder.loadTexts:
    snsOVPNStatsEntry.setStatus("current")


class _SnsOVPNEntryIndex_Type(Integer32):
    """Custom type snsOVPNEntryIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SnsOVPNEntryIndex_Type.__name__ = "Integer32"
_SnsOVPNEntryIndex_Object = MibTableColumn
snsOVPNEntryIndex = _SnsOVPNEntryIndex_Object(
    (1, 3, 6, 1, 4, 1, 11256, 1, 17, 1, 1, 1),
    _SnsOVPNEntryIndex_Type()
)
snsOVPNEntryIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snsOVPNEntryIndex.setStatus("current")
_SnsOVPNEntryIpProto_Type = DisplayString
_SnsOVPNEntryIpProto_Object = MibTableColumn
snsOVPNEntryIpProto = _SnsOVPNEntryIpProto_Object(
    (1, 3, 6, 1, 4, 1, 11256, 1, 17, 1, 1, 2),
    _SnsOVPNEntryIpProto_Type()
)
snsOVPNEntryIpProto.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snsOVPNEntryIpProto.setStatus("current")
_SnsOVPNEntryUser_Type = DisplayString
_SnsOVPNEntryUser_Object = MibTableColumn
snsOVPNEntryUser = _SnsOVPNEntryUser_Object(
    (1, 3, 6, 1, 4, 1, 11256, 1, 17, 1, 1, 3),
    _SnsOVPNEntryUser_Type()
)
snsOVPNEntryUser.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snsOVPNEntryUser.setStatus("current")
_SnsOVPNEntryDomain_Type = DisplayString
_SnsOVPNEntryDomain_Object = MibTableColumn
snsOVPNEntryDomain = _SnsOVPNEntryDomain_Object(
    (1, 3, 6, 1, 4, 1, 11256, 1, 17, 1, 1, 4),
    _SnsOVPNEntryDomain_Type()
)
snsOVPNEntryDomain.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snsOVPNEntryDomain.setStatus("current")
_SnsOVPNEntryRealIp_Type = DisplayString
_SnsOVPNEntryRealIp_Object = MibTableColumn
snsOVPNEntryRealIp = _SnsOVPNEntryRealIp_Object(
    (1, 3, 6, 1, 4, 1, 11256, 1, 17, 1, 1, 5),
    _SnsOVPNEntryRealIp_Type()
)
snsOVPNEntryRealIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snsOVPNEntryRealIp.setStatus("current")
_SnsOVPNEntryVPNIp_Type = DisplayString
_SnsOVPNEntryVPNIp_Object = MibTableColumn
snsOVPNEntryVPNIp = _SnsOVPNEntryVPNIp_Object(
    (1, 3, 6, 1, 4, 1, 11256, 1, 17, 1, 1, 6),
    _SnsOVPNEntryVPNIp_Type()
)
snsOVPNEntryVPNIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snsOVPNEntryVPNIp.setStatus("current")
_SnsOVPNEntryVPNIpv6_Type = DisplayString
_SnsOVPNEntryVPNIpv6_Object = MibTableColumn
snsOVPNEntryVPNIpv6 = _SnsOVPNEntryVPNIpv6_Object(
    (1, 3, 6, 1, 4, 1, 11256, 1, 17, 1, 1, 7),
    _SnsOVPNEntryVPNIpv6_Type()
)
snsOVPNEntryVPNIpv6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snsOVPNEntryVPNIpv6.setStatus("current")
_SnsOVPNEntryPort_Type = DisplayString
_SnsOVPNEntryPort_Object = MibTableColumn
snsOVPNEntryPort = _SnsOVPNEntryPort_Object(
    (1, 3, 6, 1, 4, 1, 11256, 1, 17, 1, 1, 8),
    _SnsOVPNEntryPort_Type()
)
snsOVPNEntryPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snsOVPNEntryPort.setStatus("current")
_SnsOVPNEntryRecv_Type = DisplayString
_SnsOVPNEntryRecv_Object = MibTableColumn
snsOVPNEntryRecv = _SnsOVPNEntryRecv_Object(
    (1, 3, 6, 1, 4, 1, 11256, 1, 17, 1, 1, 9),
    _SnsOVPNEntryRecv_Type()
)
snsOVPNEntryRecv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snsOVPNEntryRecv.setStatus("current")
_SnsOVPNEntrySent_Type = DisplayString
_SnsOVPNEntrySent_Object = MibTableColumn
snsOVPNEntrySent = _SnsOVPNEntrySent_Object(
    (1, 3, 6, 1, 4, 1, 11256, 1, 17, 1, 1, 10),
    _SnsOVPNEntrySent_Type()
)
snsOVPNEntrySent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snsOVPNEntrySent.setStatus("current")
_SnsOVPNEntryDuration_Type = Counter64
_SnsOVPNEntryDuration_Object = MibTableColumn
snsOVPNEntryDuration = _SnsOVPNEntryDuration_Object(
    (1, 3, 6, 1, 4, 1, 11256, 1, 17, 1, 1, 11),
    _SnsOVPNEntryDuration_Type()
)
snsOVPNEntryDuration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snsOVPNEntryDuration.setStatus("current")
_SnsOVPNEntryHostChecking_Type = DisplayString
_SnsOVPNEntryHostChecking_Object = MibTableColumn
snsOVPNEntryHostChecking = _SnsOVPNEntryHostChecking_Object(
    (1, 3, 6, 1, 4, 1, 11256, 1, 17, 1, 1, 12),
    _SnsOVPNEntryHostChecking_Type()
)
snsOVPNEntryHostChecking.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snsOVPNEntryHostChecking.setStatus("current")
_SnsOVPNEntryClientVersion_Type = DisplayString
_SnsOVPNEntryClientVersion_Object = MibTableColumn
snsOVPNEntryClientVersion = _SnsOVPNEntryClientVersion_Object(
    (1, 3, 6, 1, 4, 1, 11256, 1, 17, 1, 1, 13),
    _SnsOVPNEntryClientVersion_Type()
)
snsOVPNEntryClientVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snsOVPNEntryClientVersion.setStatus("current")
_SnsOVPNEntryOsType_Type = DisplayString
_SnsOVPNEntryOsType_Object = MibTableColumn
snsOVPNEntryOsType = _SnsOVPNEntryOsType_Object(
    (1, 3, 6, 1, 4, 1, 11256, 1, 17, 1, 1, 14),
    _SnsOVPNEntryOsType_Type()
)
snsOVPNEntryOsType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snsOVPNEntryOsType.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "STORMSHIELD-OVPN-MIB",
    **{"snsOVPN": snsOVPN,
       "snsOVPNStatsTable": snsOVPNStatsTable,
       "snsOVPNStatsEntry": snsOVPNStatsEntry,
       "snsOVPNEntryIndex": snsOVPNEntryIndex,
       "snsOVPNEntryIpProto": snsOVPNEntryIpProto,
       "snsOVPNEntryUser": snsOVPNEntryUser,
       "snsOVPNEntryDomain": snsOVPNEntryDomain,
       "snsOVPNEntryRealIp": snsOVPNEntryRealIp,
       "snsOVPNEntryVPNIp": snsOVPNEntryVPNIp,
       "snsOVPNEntryVPNIpv6": snsOVPNEntryVPNIpv6,
       "snsOVPNEntryPort": snsOVPNEntryPort,
       "snsOVPNEntryRecv": snsOVPNEntryRecv,
       "snsOVPNEntrySent": snsOVPNEntrySent,
       "snsOVPNEntryDuration": snsOVPNEntryDuration,
       "snsOVPNEntryHostChecking": snsOVPNEntryHostChecking,
       "snsOVPNEntryClientVersion": snsOVPNEntryClientVersion,
       "snsOVPNEntryOsType": snsOVPNEntryOsType}
)
