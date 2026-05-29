# SNMP MIB module (STORMSHIELD-HOSTS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\stormshield\STORMSHIELD-HOSTS-MIB

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

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

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

snsHosts = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 11256, 1, 3)
)
if mibBuilder.loadTexts:
    snsHosts.setRevisions(
        ("2017-02-20 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_SnsHostsTable_Object = MibTable
snsHostsTable = _SnsHostsTable_Object(
    (1, 3, 6, 1, 4, 1, 11256, 1, 3, 1)
)
if mibBuilder.loadTexts:
    snsHostsTable.setStatus("current")
_SnsHostsEntry_Object = MibTableRow
snsHostsEntry = _SnsHostsEntry_Object(
    (1, 3, 6, 1, 4, 1, 11256, 1, 3, 1, 1)
)
snsHostsEntry.setIndexNames(
    (0, "STORMSHIELD-HOSTS-MIB", "snsHostIPAddr"),
)
if mibBuilder.loadTexts:
    snsHostsEntry.setStatus("current")


class _SnsHostIPAddr_Type(DisplayString):
    """Custom type snsHostIPAddr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SnsHostIPAddr_Type.__name__ = "DisplayString"
_SnsHostIPAddr_Object = MibTableColumn
snsHostIPAddr = _SnsHostIPAddr_Object(
    (1, 3, 6, 1, 4, 1, 11256, 1, 3, 1, 1, 1),
    _SnsHostIPAddr_Type()
)
snsHostIPAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snsHostIPAddr.setStatus("current")
_SnsHostName_Type = SnmpAdminString
_SnsHostName_Object = MibTableColumn
snsHostName = _SnsHostName_Object(
    (1, 3, 6, 1, 4, 1, 11256, 1, 3, 1, 1, 2),
    _SnsHostName_Type()
)
snsHostName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snsHostName.setStatus("current")
_SnsInterface_Type = DisplayString
_SnsInterface_Object = MibTableColumn
snsInterface = _SnsInterface_Object(
    (1, 3, 6, 1, 4, 1, 11256, 1, 3, 1, 1, 3),
    _SnsInterface_Type()
)
snsInterface.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snsInterface.setStatus("current")
_SnsPackets_Type = Counter64
_SnsPackets_Object = MibTableColumn
snsPackets = _SnsPackets_Object(
    (1, 3, 6, 1, 4, 1, 11256, 1, 3, 1, 1, 4),
    _SnsPackets_Type()
)
snsPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snsPackets.setStatus("current")
_SnsBytes_Type = Counter64
_SnsBytes_Object = MibTableColumn
snsBytes = _SnsBytes_Object(
    (1, 3, 6, 1, 4, 1, 11256, 1, 3, 1, 1, 5),
    _SnsBytes_Type()
)
snsBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snsBytes.setStatus("current")
_SnsCurThroughput_Type = Counter64
_SnsCurThroughput_Object = MibTableColumn
snsCurThroughput = _SnsCurThroughput_Object(
    (1, 3, 6, 1, 4, 1, 11256, 1, 3, 1, 1, 7),
    _SnsCurThroughput_Type()
)
snsCurThroughput.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snsCurThroughput.setStatus("current")
_SnsMaxThroughput_Type = Counter64
_SnsMaxThroughput_Object = MibTableColumn
snsMaxThroughput = _SnsMaxThroughput_Object(
    (1, 3, 6, 1, 4, 1, 11256, 1, 3, 1, 1, 8),
    _SnsMaxThroughput_Type()
)
snsMaxThroughput.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snsMaxThroughput.setStatus("current")
_SnsInBytes_Type = Counter64
_SnsInBytes_Object = MibTableColumn
snsInBytes = _SnsInBytes_Object(
    (1, 3, 6, 1, 4, 1, 11256, 1, 3, 1, 1, 9),
    _SnsInBytes_Type()
)
snsInBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snsInBytes.setStatus("current")
_SnsOutBytes_Type = Counter64
_SnsOutBytes_Object = MibTableColumn
snsOutBytes = _SnsOutBytes_Object(
    (1, 3, 6, 1, 4, 1, 11256, 1, 3, 1, 1, 10),
    _SnsOutBytes_Type()
)
snsOutBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snsOutBytes.setStatus("current")
_SnsInCurThroughput_Type = Counter64
_SnsInCurThroughput_Object = MibTableColumn
snsInCurThroughput = _SnsInCurThroughput_Object(
    (1, 3, 6, 1, 4, 1, 11256, 1, 3, 1, 1, 11),
    _SnsInCurThroughput_Type()
)
snsInCurThroughput.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snsInCurThroughput.setStatus("current")
_SnsOutCurThroughput_Type = Counter64
_SnsOutCurThroughput_Object = MibTableColumn
snsOutCurThroughput = _SnsOutCurThroughput_Object(
    (1, 3, 6, 1, 4, 1, 11256, 1, 3, 1, 1, 12),
    _SnsOutCurThroughput_Type()
)
snsOutCurThroughput.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snsOutCurThroughput.setStatus("current")
_SnsInMaxCurThroughput_Type = Counter64
_SnsInMaxCurThroughput_Object = MibTableColumn
snsInMaxCurThroughput = _SnsInMaxCurThroughput_Object(
    (1, 3, 6, 1, 4, 1, 11256, 1, 3, 1, 1, 13),
    _SnsInMaxCurThroughput_Type()
)
snsInMaxCurThroughput.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snsInMaxCurThroughput.setStatus("current")
_SnsOutMaxCurThroughput_Type = Counter64
_SnsOutMaxCurThroughput_Object = MibTableColumn
snsOutMaxCurThroughput = _SnsOutMaxCurThroughput_Object(
    (1, 3, 6, 1, 4, 1, 11256, 1, 3, 1, 1, 14),
    _SnsOutMaxCurThroughput_Type()
)
snsOutMaxCurThroughput.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snsOutMaxCurThroughput.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "STORMSHIELD-HOSTS-MIB",
    **{"snsHosts": snsHosts,
       "snsHostsTable": snsHostsTable,
       "snsHostsEntry": snsHostsEntry,
       "snsHostIPAddr": snsHostIPAddr,
       "snsHostName": snsHostName,
       "snsInterface": snsInterface,
       "snsPackets": snsPackets,
       "snsBytes": snsBytes,
       "snsCurThroughput": snsCurThroughput,
       "snsMaxThroughput": snsMaxThroughput,
       "snsInBytes": snsInBytes,
       "snsOutBytes": snsOutBytes,
       "snsInCurThroughput": snsInCurThroughput,
       "snsOutCurThroughput": snsOutCurThroughput,
       "snsInMaxCurThroughput": snsInMaxCurThroughput,
       "snsOutMaxCurThroughput": snsOutMaxCurThroughput}
)
