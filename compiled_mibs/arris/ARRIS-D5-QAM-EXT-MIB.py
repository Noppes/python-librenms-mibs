# SNMP MIB module (ARRIS-D5-QAM-EXT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\arris\d5\ARRIS-D5-QAM-EXT-MIB

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

(arrisD5UEQam,) = mibBuilder.importSymbols(
    "ARRIS-MIB",
    "arrisD5UEQam")

(InterfaceIndex,
 ifIndex) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex",
    "ifIndex")

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

d5QamExtMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4115, 1, 8, 1, 12)
)
if mibBuilder.loadTexts:
    d5QamExtMib.setRevisions(
        ("2007-11-30 11:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_D5QamExtTable_Object = MibTable
d5QamExtTable = _D5QamExtTable_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 8, 1, 12, 1)
)
if mibBuilder.loadTexts:
    d5QamExtTable.setStatus("current")
_D5QamExtEntry_Object = MibTableRow
d5QamExtEntry = _D5QamExtEntry_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 8, 1, 12, 1, 1)
)
d5QamExtEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    d5QamExtEntry.setStatus("current")
_D5QamExtProtocolMappingErm_Type = DisplayString
_D5QamExtProtocolMappingErm_Object = MibTableColumn
d5QamExtProtocolMappingErm = _D5QamExtProtocolMappingErm_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 8, 1, 12, 1, 1, 2),
    _D5QamExtProtocolMappingErm_Type()
)
d5QamExtProtocolMappingErm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    d5QamExtProtocolMappingErm.setStatus("current")
_D5QamExtServingGroup_Type = DisplayString
_D5QamExtServingGroup_Object = MibTableColumn
d5QamExtServingGroup = _D5QamExtServingGroup_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 8, 1, 12, 1, 1, 3),
    _D5QamExtServingGroup_Type()
)
d5QamExtServingGroup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    d5QamExtServingGroup.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ARRIS-D5-QAM-EXT-MIB",
    **{"d5QamExtMib": d5QamExtMib,
       "d5QamExtTable": d5QamExtTable,
       "d5QamExtEntry": d5QamExtEntry,
       "d5QamExtProtocolMappingErm": d5QamExtProtocolMappingErm,
       "d5QamExtServingGroup": d5QamExtServingGroup}
)
