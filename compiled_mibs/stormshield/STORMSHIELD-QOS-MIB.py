# SNMP MIB module (STORMSHIELD-QOS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\stormshield\STORMSHIELD-QOS-MIB

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

snsQos = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 11256, 1, 15)
)
if mibBuilder.loadTexts:
    snsQos.setRevisions(
        ("2017-02-20 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_SnsQosStatsTable_Object = MibTable
snsQosStatsTable = _SnsQosStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 11256, 1, 15, 1)
)
if mibBuilder.loadTexts:
    snsQosStatsTable.setStatus("current")
_SnsQosStatsEntry_Object = MibTableRow
snsQosStatsEntry = _SnsQosStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 11256, 1, 15, 1, 1)
)
snsQosStatsEntry.setIndexNames(
    (0, "STORMSHIELD-QOS-MIB", "snsQosEntryIndex"),
)
if mibBuilder.loadTexts:
    snsQosStatsEntry.setStatus("current")


class _SnsQosEntryIndex_Type(Integer32):
    """Custom type snsQosEntryIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SnsQosEntryIndex_Type.__name__ = "Integer32"
_SnsQosEntryIndex_Object = MibTableColumn
snsQosEntryIndex = _SnsQosEntryIndex_Object(
    (1, 3, 6, 1, 4, 1, 11256, 1, 15, 1, 1, 1),
    _SnsQosEntryIndex_Type()
)
snsQosEntryIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snsQosEntryIndex.setStatus("current")
_SnsQosEntryName_Type = DisplayString
_SnsQosEntryName_Object = MibTableColumn
snsQosEntryName = _SnsQosEntryName_Object(
    (1, 3, 6, 1, 4, 1, 11256, 1, 15, 1, 1, 2),
    _SnsQosEntryName_Type()
)
snsQosEntryName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snsQosEntryName.setStatus("current")
_SnsQosEntryType_Type = DisplayString
_SnsQosEntryType_Object = MibTableColumn
snsQosEntryType = _SnsQosEntryType_Object(
    (1, 3, 6, 1, 4, 1, 11256, 1, 15, 1, 1, 3),
    _SnsQosEntryType_Type()
)
snsQosEntryType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snsQosEntryType.setStatus("current")
_SnsQosEntryInCounter_Type = Counter64
_SnsQosEntryInCounter_Object = MibTableColumn
snsQosEntryInCounter = _SnsQosEntryInCounter_Object(
    (1, 3, 6, 1, 4, 1, 11256, 1, 15, 1, 1, 4),
    _SnsQosEntryInCounter_Type()
)
snsQosEntryInCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snsQosEntryInCounter.setStatus("current")
_SnsQosEntryInMaxPeak_Type = Counter64
_SnsQosEntryInMaxPeak_Object = MibTableColumn
snsQosEntryInMaxPeak = _SnsQosEntryInMaxPeak_Object(
    (1, 3, 6, 1, 4, 1, 11256, 1, 15, 1, 1, 5),
    _SnsQosEntryInMaxPeak_Type()
)
snsQosEntryInMaxPeak.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snsQosEntryInMaxPeak.setStatus("current")
_SnsQosEntryInSpeedLimit_Type = Counter64
_SnsQosEntryInSpeedLimit_Object = MibTableColumn
snsQosEntryInSpeedLimit = _SnsQosEntryInSpeedLimit_Object(
    (1, 3, 6, 1, 4, 1, 11256, 1, 15, 1, 1, 6),
    _SnsQosEntryInSpeedLimit_Type()
)
snsQosEntryInSpeedLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snsQosEntryInSpeedLimit.setStatus("current")
_SnsQosEntryOutCounter_Type = Counter64
_SnsQosEntryOutCounter_Object = MibTableColumn
snsQosEntryOutCounter = _SnsQosEntryOutCounter_Object(
    (1, 3, 6, 1, 4, 1, 11256, 1, 15, 1, 1, 7),
    _SnsQosEntryOutCounter_Type()
)
snsQosEntryOutCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snsQosEntryOutCounter.setStatus("current")
_SnsQosEntryOutMaxPeak_Type = Counter64
_SnsQosEntryOutMaxPeak_Object = MibTableColumn
snsQosEntryOutMaxPeak = _SnsQosEntryOutMaxPeak_Object(
    (1, 3, 6, 1, 4, 1, 11256, 1, 15, 1, 1, 8),
    _SnsQosEntryOutMaxPeak_Type()
)
snsQosEntryOutMaxPeak.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snsQosEntryOutMaxPeak.setStatus("current")
_SnsQosEntryOutSpeedLimit_Type = Counter64
_SnsQosEntryOutSpeedLimit_Object = MibTableColumn
snsQosEntryOutSpeedLimit = _SnsQosEntryOutSpeedLimit_Object(
    (1, 3, 6, 1, 4, 1, 11256, 1, 15, 1, 1, 9),
    _SnsQosEntryOutSpeedLimit_Type()
)
snsQosEntryOutSpeedLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snsQosEntryOutSpeedLimit.setStatus("current")
_SnsQosEntryComment_Type = DisplayString
_SnsQosEntryComment_Object = MibTableColumn
snsQosEntryComment = _SnsQosEntryComment_Object(
    (1, 3, 6, 1, 4, 1, 11256, 1, 15, 1, 1, 10),
    _SnsQosEntryComment_Type()
)
snsQosEntryComment.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snsQosEntryComment.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "STORMSHIELD-QOS-MIB",
    **{"snsQos": snsQos,
       "snsQosStatsTable": snsQosStatsTable,
       "snsQosStatsEntry": snsQosStatsEntry,
       "snsQosEntryIndex": snsQosEntryIndex,
       "snsQosEntryName": snsQosEntryName,
       "snsQosEntryType": snsQosEntryType,
       "snsQosEntryInCounter": snsQosEntryInCounter,
       "snsQosEntryInMaxPeak": snsQosEntryInMaxPeak,
       "snsQosEntryInSpeedLimit": snsQosEntryInSpeedLimit,
       "snsQosEntryOutCounter": snsQosEntryOutCounter,
       "snsQosEntryOutMaxPeak": snsQosEntryOutMaxPeak,
       "snsQosEntryOutSpeedLimit": snsQosEntryOutSpeedLimit,
       "snsQosEntryComment": snsQosEntryComment}
)
