# SNMP MIB module (BEGEMOT-ATM-FREEBSD-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\pfsense\BEGEMOT-ATM-FREEBSD-MIB

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

(begemotAtmIfEntry,
 begemotAtmSysGroup) = mibBuilder.importSymbols(
    "BEGEMOT-ATM-MIB",
    "begemotAtmIfEntry",
    "begemotAtmSysGroup")

(NgNodeIdOrZero,) = mibBuilder.importSymbols(
    "BEGEMOT-NETGRAPH-MIB",
    "NgNodeIdOrZero")

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


# MODULE-IDENTITY

begemotAtmFreeBSDGroup = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 12325, 1, 101, 1, 4, 1)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_BegemotAtmNgGroup_ObjectIdentity = ObjectIdentity
begemotAtmNgGroup = _BegemotAtmNgGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12325, 1, 101, 1, 4, 1, 1)
)
_BegemotAtmNgIfTable_Object = MibTable
begemotAtmNgIfTable = _BegemotAtmNgIfTable_Object(
    (1, 3, 6, 1, 4, 1, 12325, 1, 101, 1, 4, 1, 1, 1)
)
if mibBuilder.loadTexts:
    begemotAtmNgIfTable.setStatus("current")
_BegemotAtmNgIfEntry_Object = MibTableRow
begemotAtmNgIfEntry = _BegemotAtmNgIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 12325, 1, 101, 1, 4, 1, 1, 1, 1)
)
if mibBuilder.loadTexts:
    begemotAtmNgIfEntry.setStatus("current")
_BegemotAtmNgIfNodeId_Type = NgNodeIdOrZero
_BegemotAtmNgIfNodeId_Object = MibTableColumn
begemotAtmNgIfNodeId = _BegemotAtmNgIfNodeId_Object(
    (1, 3, 6, 1, 4, 1, 12325, 1, 101, 1, 4, 1, 1, 1, 1, 1),
    _BegemotAtmNgIfNodeId_Type()
)
begemotAtmNgIfNodeId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    begemotAtmNgIfNodeId.setStatus("current")
begemotAtmIfEntry.registerAugmentions(
    ("BEGEMOT-ATM-FREEBSD-MIB",
     "begemotAtmNgIfEntry")
)
begemotAtmNgIfEntry.setIndexNames(*begemotAtmIfEntry.getIndexNames())

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "BEGEMOT-ATM-FREEBSD-MIB",
    **{"begemotAtmFreeBSDGroup": begemotAtmFreeBSDGroup,
       "begemotAtmNgGroup": begemotAtmNgGroup,
       "begemotAtmNgIfTable": begemotAtmNgIfTable,
       "begemotAtmNgIfEntry": begemotAtmNgIfEntry,
       "begemotAtmNgIfNodeId": begemotAtmNgIfNodeId}
)
