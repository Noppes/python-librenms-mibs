# SNMP MIB module (AX-FDB-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\alaxala\AX-FDB-MIB

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

axFdb = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 5)
)
if mibBuilder.loadTexts:
    axFdb.setRevisions(
        ("2014-03-26 00:01",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AxFdbCounterTable_Object = MibTable
axFdbCounterTable = _AxFdbCounterTable_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 5, 1)
)
if mibBuilder.loadTexts:
    axFdbCounterTable.setStatus("current")
_AxFdbCounterEntry_Object = MibTableRow
axFdbCounterEntry = _AxFdbCounterEntry_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 5, 1, 1)
)
axFdbCounterEntry.setIndexNames(
    (0, "AX-FDB-MIB", "axFdbCounterNifIndex"),
    (0, "AX-FDB-MIB", "axFdbCounterLineIndex"),
)
if mibBuilder.loadTexts:
    axFdbCounterEntry.setStatus("current")
_AxFdbCounterNifIndex_Type = Integer32
_AxFdbCounterNifIndex_Object = MibTableColumn
axFdbCounterNifIndex = _AxFdbCounterNifIndex_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 5, 1, 1, 1),
    _AxFdbCounterNifIndex_Type()
)
axFdbCounterNifIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    axFdbCounterNifIndex.setStatus("current")
_AxFdbCounterLineIndex_Type = Integer32
_AxFdbCounterLineIndex_Object = MibTableColumn
axFdbCounterLineIndex = _AxFdbCounterLineIndex_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 5, 1, 1, 2),
    _AxFdbCounterLineIndex_Type()
)
axFdbCounterLineIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    axFdbCounterLineIndex.setStatus("current")
_AxFdbCounterCounts_Type = Counter32
_AxFdbCounterCounts_Object = MibTableColumn
axFdbCounterCounts = _AxFdbCounterCounts_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 5, 1, 1, 3),
    _AxFdbCounterCounts_Type()
)
axFdbCounterCounts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axFdbCounterCounts.setStatus("current")


class _AxFdbCounterType_Type(Integer32):
    """Custom type axFdbCounterType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("unlimited", 1),
          ("limitedAndForward", 2),
          ("limitedAndDiscard", 3))
    )


_AxFdbCounterType_Type.__name__ = "Integer32"
_AxFdbCounterType_Object = MibTableColumn
axFdbCounterType = _AxFdbCounterType_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 5, 1, 1, 4),
    _AxFdbCounterType_Type()
)
axFdbCounterType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axFdbCounterType.setStatus("current")
_AxFdbCounterLimits_Type = Counter32
_AxFdbCounterLimits_Object = MibTableColumn
axFdbCounterLimits = _AxFdbCounterLimits_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 5, 1, 1, 5),
    _AxFdbCounterLimits_Type()
)
axFdbCounterLimits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axFdbCounterLimits.setStatus("current")
_AxFdbConformance_ObjectIdentity = ObjectIdentity
axFdbConformance = _AxFdbConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 5, 1000)
)
_AxFdbCompliances_ObjectIdentity = ObjectIdentity
axFdbCompliances = _AxFdbCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 5, 1000, 1)
)
_AxFdbGroups_ObjectIdentity = ObjectIdentity
axFdbGroups = _AxFdbGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 5, 1000, 2)
)

# Managed Objects groups

axFdbGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 5, 1000, 2, 1)
)
axFdbGroup.setObjects(
      *(("AX-FDB-MIB", "axFdbCounterCounts"),
        ("AX-FDB-MIB", "axFdbCounterType"),
        ("AX-FDB-MIB", "axFdbCounterLimits"))
)
if mibBuilder.loadTexts:
    axFdbGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

axFdbCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 5, 1000, 1, 1)
)
axFdbCompliance.setObjects(
    ("AX-FDB-MIB", "axFdbGroup")
)
if mibBuilder.loadTexts:
    axFdbCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "AX-FDB-MIB",
    **{"axFdb": axFdb,
       "axFdbCounterTable": axFdbCounterTable,
       "axFdbCounterEntry": axFdbCounterEntry,
       "axFdbCounterNifIndex": axFdbCounterNifIndex,
       "axFdbCounterLineIndex": axFdbCounterLineIndex,
       "axFdbCounterCounts": axFdbCounterCounts,
       "axFdbCounterType": axFdbCounterType,
       "axFdbCounterLimits": axFdbCounterLimits,
       "axFdbConformance": axFdbConformance,
       "axFdbCompliances": axFdbCompliances,
       "axFdbCompliance": axFdbCompliance,
       "axFdbGroups": axFdbGroups,
       "axFdbGroup": axFdbGroup}
)
