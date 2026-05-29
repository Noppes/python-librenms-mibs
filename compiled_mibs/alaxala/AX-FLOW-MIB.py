# SNMP MIB module (AX-FLOW-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\alaxala\AX-FLOW-MIB

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

axFlow = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 8)
)
if mibBuilder.loadTexts:
    axFlow.setRevisions(
        ("2016-03-22 00:00",
         "2013-10-03 00:00",
         "2013-04-26 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AxAccessFilterStats_ObjectIdentity = ObjectIdentity
axAccessFilterStats = _AxAccessFilterStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 8, 151)
)
_AxAccessFilterStatsInTotalTable_Object = MibTable
axAccessFilterStatsInTotalTable = _AxAccessFilterStatsInTotalTable_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 8, 151, 11)
)
if mibBuilder.loadTexts:
    axAccessFilterStatsInTotalTable.setStatus("current")
_AxAccessFilterStatsInTotalEntry_Object = MibTableRow
axAccessFilterStatsInTotalEntry = _AxAccessFilterStatsInTotalEntry_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 8, 151, 11, 1)
)
axAccessFilterStatsInTotalEntry.setIndexNames(
    (0, "AX-FLOW-MIB", "axAccessFilterStatsInTotalifIndex"),
    (0, "AX-FLOW-MIB", "axAccessFilterStatsInTotalGroupType"),
    (0, "AX-FLOW-MIB", "axAccessFilterStatsInTotalSequenceNumber"),
)
if mibBuilder.loadTexts:
    axAccessFilterStatsInTotalEntry.setStatus("current")


class _AxAccessFilterStatsInTotalifIndex_Type(Integer32):
    """Custom type axAccessFilterStatsInTotalifIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_AxAccessFilterStatsInTotalifIndex_Type.__name__ = "Integer32"
_AxAccessFilterStatsInTotalifIndex_Object = MibTableColumn
axAccessFilterStatsInTotalifIndex = _AxAccessFilterStatsInTotalifIndex_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 8, 151, 11, 1, 1),
    _AxAccessFilterStatsInTotalifIndex_Type()
)
axAccessFilterStatsInTotalifIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    axAccessFilterStatsInTotalifIndex.setStatus("current")


class _AxAccessFilterStatsInTotalGroupType_Type(Integer32):
    """Custom type axAccessFilterStatsInTotalGroupType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("mac", 1),
          ("ip", 2),
          ("ipv6", 3),
          ("advance", 4))
    )


_AxAccessFilterStatsInTotalGroupType_Type.__name__ = "Integer32"
_AxAccessFilterStatsInTotalGroupType_Object = MibTableColumn
axAccessFilterStatsInTotalGroupType = _AxAccessFilterStatsInTotalGroupType_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 8, 151, 11, 1, 2),
    _AxAccessFilterStatsInTotalGroupType_Type()
)
axAccessFilterStatsInTotalGroupType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    axAccessFilterStatsInTotalGroupType.setStatus("current")
_AxAccessFilterStatsInTotalSequenceNumber_Type = Unsigned32
_AxAccessFilterStatsInTotalSequenceNumber_Object = MibTableColumn
axAccessFilterStatsInTotalSequenceNumber = _AxAccessFilterStatsInTotalSequenceNumber_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 8, 151, 11, 1, 3),
    _AxAccessFilterStatsInTotalSequenceNumber_Type()
)
axAccessFilterStatsInTotalSequenceNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    axAccessFilterStatsInTotalSequenceNumber.setStatus("current")
_AxAccessFilterStatsInTotalListName_Type = DisplayString
_AxAccessFilterStatsInTotalListName_Object = MibTableColumn
axAccessFilterStatsInTotalListName = _AxAccessFilterStatsInTotalListName_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 8, 151, 11, 1, 4),
    _AxAccessFilterStatsInTotalListName_Type()
)
axAccessFilterStatsInTotalListName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axAccessFilterStatsInTotalListName.setStatus("current")
_AxAccessFilterStatsInTotalMatchedPackets_Type = Counter64
_AxAccessFilterStatsInTotalMatchedPackets_Object = MibTableColumn
axAccessFilterStatsInTotalMatchedPackets = _AxAccessFilterStatsInTotalMatchedPackets_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 8, 151, 11, 1, 5),
    _AxAccessFilterStatsInTotalMatchedPackets_Type()
)
axAccessFilterStatsInTotalMatchedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axAccessFilterStatsInTotalMatchedPackets.setStatus("current")
_AxAccessFilterStatsInTotalMatchedBytes_Type = Counter64
_AxAccessFilterStatsInTotalMatchedBytes_Object = MibTableColumn
axAccessFilterStatsInTotalMatchedBytes = _AxAccessFilterStatsInTotalMatchedBytes_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 8, 151, 11, 1, 6),
    _AxAccessFilterStatsInTotalMatchedBytes_Type()
)
axAccessFilterStatsInTotalMatchedBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axAccessFilterStatsInTotalMatchedBytes.setStatus("current")
_AxAccessFilterStatsOutTotalTable_Object = MibTable
axAccessFilterStatsOutTotalTable = _AxAccessFilterStatsOutTotalTable_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 8, 151, 21)
)
if mibBuilder.loadTexts:
    axAccessFilterStatsOutTotalTable.setStatus("current")
_AxAccessFilterStatsOutTotalEntry_Object = MibTableRow
axAccessFilterStatsOutTotalEntry = _AxAccessFilterStatsOutTotalEntry_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 8, 151, 21, 1)
)
axAccessFilterStatsOutTotalEntry.setIndexNames(
    (0, "AX-FLOW-MIB", "axAccessFilterStatsOutTotalifIndex"),
    (0, "AX-FLOW-MIB", "axAccessFilterStatsOutTotalGroupType"),
    (0, "AX-FLOW-MIB", "axAccessFilterStatsOutTotalSequenceNumber"),
)
if mibBuilder.loadTexts:
    axAccessFilterStatsOutTotalEntry.setStatus("current")


class _AxAccessFilterStatsOutTotalifIndex_Type(Integer32):
    """Custom type axAccessFilterStatsOutTotalifIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_AxAccessFilterStatsOutTotalifIndex_Type.__name__ = "Integer32"
_AxAccessFilterStatsOutTotalifIndex_Object = MibTableColumn
axAccessFilterStatsOutTotalifIndex = _AxAccessFilterStatsOutTotalifIndex_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 8, 151, 21, 1, 1),
    _AxAccessFilterStatsOutTotalifIndex_Type()
)
axAccessFilterStatsOutTotalifIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    axAccessFilterStatsOutTotalifIndex.setStatus("current")


class _AxAccessFilterStatsOutTotalGroupType_Type(Integer32):
    """Custom type axAccessFilterStatsOutTotalGroupType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("mac", 1),
          ("ip", 2),
          ("ipv6", 3),
          ("advance", 4))
    )


_AxAccessFilterStatsOutTotalGroupType_Type.__name__ = "Integer32"
_AxAccessFilterStatsOutTotalGroupType_Object = MibTableColumn
axAccessFilterStatsOutTotalGroupType = _AxAccessFilterStatsOutTotalGroupType_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 8, 151, 21, 1, 2),
    _AxAccessFilterStatsOutTotalGroupType_Type()
)
axAccessFilterStatsOutTotalGroupType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    axAccessFilterStatsOutTotalGroupType.setStatus("current")
_AxAccessFilterStatsOutTotalSequenceNumber_Type = Unsigned32
_AxAccessFilterStatsOutTotalSequenceNumber_Object = MibTableColumn
axAccessFilterStatsOutTotalSequenceNumber = _AxAccessFilterStatsOutTotalSequenceNumber_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 8, 151, 21, 1, 3),
    _AxAccessFilterStatsOutTotalSequenceNumber_Type()
)
axAccessFilterStatsOutTotalSequenceNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    axAccessFilterStatsOutTotalSequenceNumber.setStatus("current")
_AxAccessFilterStatsOutTotalListName_Type = DisplayString
_AxAccessFilterStatsOutTotalListName_Object = MibTableColumn
axAccessFilterStatsOutTotalListName = _AxAccessFilterStatsOutTotalListName_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 8, 151, 21, 1, 4),
    _AxAccessFilterStatsOutTotalListName_Type()
)
axAccessFilterStatsOutTotalListName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axAccessFilterStatsOutTotalListName.setStatus("current")
_AxAccessFilterStatsOutTotalMatchedPackets_Type = Counter64
_AxAccessFilterStatsOutTotalMatchedPackets_Object = MibTableColumn
axAccessFilterStatsOutTotalMatchedPackets = _AxAccessFilterStatsOutTotalMatchedPackets_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 8, 151, 21, 1, 5),
    _AxAccessFilterStatsOutTotalMatchedPackets_Type()
)
axAccessFilterStatsOutTotalMatchedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axAccessFilterStatsOutTotalMatchedPackets.setStatus("current")
_AxAccessFilterStatsOutTotalMatchedBytes_Type = Counter64
_AxAccessFilterStatsOutTotalMatchedBytes_Object = MibTableColumn
axAccessFilterStatsOutTotalMatchedBytes = _AxAccessFilterStatsOutTotalMatchedBytes_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 8, 151, 21, 1, 6),
    _AxAccessFilterStatsOutTotalMatchedBytes_Type()
)
axAccessFilterStatsOutTotalMatchedBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axAccessFilterStatsOutTotalMatchedBytes.setStatus("current")
_AxAccessFilterStatsInMirrorTotalTable_Object = MibTable
axAccessFilterStatsInMirrorTotalTable = _AxAccessFilterStatsInMirrorTotalTable_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 8, 151, 31)
)
if mibBuilder.loadTexts:
    axAccessFilterStatsInMirrorTotalTable.setStatus("current")
_AxAccessFilterStatsInMirrorTotalEntry_Object = MibTableRow
axAccessFilterStatsInMirrorTotalEntry = _AxAccessFilterStatsInMirrorTotalEntry_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 8, 151, 31, 1)
)
axAccessFilterStatsInMirrorTotalEntry.setIndexNames(
    (0, "AX-FLOW-MIB", "axAccessFilterStatsInMirrorTotalifIndex"),
    (0, "AX-FLOW-MIB", "axAccessFilterStatsInMirrorTotalGroupType"),
    (0, "AX-FLOW-MIB", "axAccessFilterStatsInMirrorTotalSequenceNumber"),
)
if mibBuilder.loadTexts:
    axAccessFilterStatsInMirrorTotalEntry.setStatus("current")


class _AxAccessFilterStatsInMirrorTotalifIndex_Type(Integer32):
    """Custom type axAccessFilterStatsInMirrorTotalifIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_AxAccessFilterStatsInMirrorTotalifIndex_Type.__name__ = "Integer32"
_AxAccessFilterStatsInMirrorTotalifIndex_Object = MibTableColumn
axAccessFilterStatsInMirrorTotalifIndex = _AxAccessFilterStatsInMirrorTotalifIndex_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 8, 151, 31, 1, 1),
    _AxAccessFilterStatsInMirrorTotalifIndex_Type()
)
axAccessFilterStatsInMirrorTotalifIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    axAccessFilterStatsInMirrorTotalifIndex.setStatus("current")


class _AxAccessFilterStatsInMirrorTotalGroupType_Type(Integer32):
    """Custom type axAccessFilterStatsInMirrorTotalGroupType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("mac", 1),
          ("ip", 2),
          ("ipv6", 3),
          ("advance", 4))
    )


_AxAccessFilterStatsInMirrorTotalGroupType_Type.__name__ = "Integer32"
_AxAccessFilterStatsInMirrorTotalGroupType_Object = MibTableColumn
axAccessFilterStatsInMirrorTotalGroupType = _AxAccessFilterStatsInMirrorTotalGroupType_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 8, 151, 31, 1, 2),
    _AxAccessFilterStatsInMirrorTotalGroupType_Type()
)
axAccessFilterStatsInMirrorTotalGroupType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    axAccessFilterStatsInMirrorTotalGroupType.setStatus("current")
_AxAccessFilterStatsInMirrorTotalSequenceNumber_Type = Unsigned32
_AxAccessFilterStatsInMirrorTotalSequenceNumber_Object = MibTableColumn
axAccessFilterStatsInMirrorTotalSequenceNumber = _AxAccessFilterStatsInMirrorTotalSequenceNumber_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 8, 151, 31, 1, 3),
    _AxAccessFilterStatsInMirrorTotalSequenceNumber_Type()
)
axAccessFilterStatsInMirrorTotalSequenceNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    axAccessFilterStatsInMirrorTotalSequenceNumber.setStatus("current")
_AxAccessFilterStatsInMirrorTotalListName_Type = DisplayString
_AxAccessFilterStatsInMirrorTotalListName_Object = MibTableColumn
axAccessFilterStatsInMirrorTotalListName = _AxAccessFilterStatsInMirrorTotalListName_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 8, 151, 31, 1, 4),
    _AxAccessFilterStatsInMirrorTotalListName_Type()
)
axAccessFilterStatsInMirrorTotalListName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axAccessFilterStatsInMirrorTotalListName.setStatus("current")
_AxAccessFilterStatsInMirrorTotalMatchedPackets_Type = Counter64
_AxAccessFilterStatsInMirrorTotalMatchedPackets_Object = MibTableColumn
axAccessFilterStatsInMirrorTotalMatchedPackets = _AxAccessFilterStatsInMirrorTotalMatchedPackets_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 8, 151, 31, 1, 5),
    _AxAccessFilterStatsInMirrorTotalMatchedPackets_Type()
)
axAccessFilterStatsInMirrorTotalMatchedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axAccessFilterStatsInMirrorTotalMatchedPackets.setStatus("current")
_AxAccessFilterStatsInMirrorTotalMatchedBytes_Type = Counter64
_AxAccessFilterStatsInMirrorTotalMatchedBytes_Object = MibTableColumn
axAccessFilterStatsInMirrorTotalMatchedBytes = _AxAccessFilterStatsInMirrorTotalMatchedBytes_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 8, 151, 31, 1, 6),
    _AxAccessFilterStatsInMirrorTotalMatchedBytes_Type()
)
axAccessFilterStatsInMirrorTotalMatchedBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axAccessFilterStatsInMirrorTotalMatchedBytes.setStatus("current")
_AxAccessFilterStatsOutMirrorTotalTable_Object = MibTable
axAccessFilterStatsOutMirrorTotalTable = _AxAccessFilterStatsOutMirrorTotalTable_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 8, 151, 41)
)
if mibBuilder.loadTexts:
    axAccessFilterStatsOutMirrorTotalTable.setStatus("current")
_AxAccessFilterStatsOutMirrorTotalEntry_Object = MibTableRow
axAccessFilterStatsOutMirrorTotalEntry = _AxAccessFilterStatsOutMirrorTotalEntry_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 8, 151, 41, 1)
)
axAccessFilterStatsOutMirrorTotalEntry.setIndexNames(
    (0, "AX-FLOW-MIB", "axAccessFilterStatsOutMirrorTotalifIndex"),
    (0, "AX-FLOW-MIB", "axAccessFilterStatsOutMirrorTotalGroupType"),
    (0, "AX-FLOW-MIB", "axAccessFilterStatsOutMirrorTotalSequenceNumber"),
)
if mibBuilder.loadTexts:
    axAccessFilterStatsOutMirrorTotalEntry.setStatus("current")


class _AxAccessFilterStatsOutMirrorTotalifIndex_Type(Integer32):
    """Custom type axAccessFilterStatsOutMirrorTotalifIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_AxAccessFilterStatsOutMirrorTotalifIndex_Type.__name__ = "Integer32"
_AxAccessFilterStatsOutMirrorTotalifIndex_Object = MibTableColumn
axAccessFilterStatsOutMirrorTotalifIndex = _AxAccessFilterStatsOutMirrorTotalifIndex_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 8, 151, 41, 1, 1),
    _AxAccessFilterStatsOutMirrorTotalifIndex_Type()
)
axAccessFilterStatsOutMirrorTotalifIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    axAccessFilterStatsOutMirrorTotalifIndex.setStatus("current")


class _AxAccessFilterStatsOutMirrorTotalGroupType_Type(Integer32):
    """Custom type axAccessFilterStatsOutMirrorTotalGroupType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("mac", 1),
          ("ip", 2),
          ("ipv6", 3),
          ("advance", 4))
    )


_AxAccessFilterStatsOutMirrorTotalGroupType_Type.__name__ = "Integer32"
_AxAccessFilterStatsOutMirrorTotalGroupType_Object = MibTableColumn
axAccessFilterStatsOutMirrorTotalGroupType = _AxAccessFilterStatsOutMirrorTotalGroupType_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 8, 151, 41, 1, 2),
    _AxAccessFilterStatsOutMirrorTotalGroupType_Type()
)
axAccessFilterStatsOutMirrorTotalGroupType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    axAccessFilterStatsOutMirrorTotalGroupType.setStatus("current")
_AxAccessFilterStatsOutMirrorTotalSequenceNumber_Type = Unsigned32
_AxAccessFilterStatsOutMirrorTotalSequenceNumber_Object = MibTableColumn
axAccessFilterStatsOutMirrorTotalSequenceNumber = _AxAccessFilterStatsOutMirrorTotalSequenceNumber_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 8, 151, 41, 1, 3),
    _AxAccessFilterStatsOutMirrorTotalSequenceNumber_Type()
)
axAccessFilterStatsOutMirrorTotalSequenceNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    axAccessFilterStatsOutMirrorTotalSequenceNumber.setStatus("current")
_AxAccessFilterStatsOutMirrorTotalListName_Type = DisplayString
_AxAccessFilterStatsOutMirrorTotalListName_Object = MibTableColumn
axAccessFilterStatsOutMirrorTotalListName = _AxAccessFilterStatsOutMirrorTotalListName_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 8, 151, 41, 1, 4),
    _AxAccessFilterStatsOutMirrorTotalListName_Type()
)
axAccessFilterStatsOutMirrorTotalListName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axAccessFilterStatsOutMirrorTotalListName.setStatus("current")
_AxAccessFilterStatsOutMirrorTotalMatchedPackets_Type = Counter64
_AxAccessFilterStatsOutMirrorTotalMatchedPackets_Object = MibTableColumn
axAccessFilterStatsOutMirrorTotalMatchedPackets = _AxAccessFilterStatsOutMirrorTotalMatchedPackets_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 8, 151, 41, 1, 5),
    _AxAccessFilterStatsOutMirrorTotalMatchedPackets_Type()
)
axAccessFilterStatsOutMirrorTotalMatchedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axAccessFilterStatsOutMirrorTotalMatchedPackets.setStatus("current")
_AxAccessFilterStatsOutMirrorTotalMatchedBytes_Type = Counter64
_AxAccessFilterStatsOutMirrorTotalMatchedBytes_Object = MibTableColumn
axAccessFilterStatsOutMirrorTotalMatchedBytes = _AxAccessFilterStatsOutMirrorTotalMatchedBytes_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 8, 151, 41, 1, 6),
    _AxAccessFilterStatsOutMirrorTotalMatchedBytes_Type()
)
axAccessFilterStatsOutMirrorTotalMatchedBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axAccessFilterStatsOutMirrorTotalMatchedBytes.setStatus("current")
_AxQosFlowStats_ObjectIdentity = ObjectIdentity
axQosFlowStats = _AxQosFlowStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 8, 251)
)
_AxQosFlowStatsInTotalTable_Object = MibTable
axQosFlowStatsInTotalTable = _AxQosFlowStatsInTotalTable_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 8, 251, 11)
)
if mibBuilder.loadTexts:
    axQosFlowStatsInTotalTable.setStatus("current")
_AxQosFlowStatsInTotalEntry_Object = MibTableRow
axQosFlowStatsInTotalEntry = _AxQosFlowStatsInTotalEntry_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 8, 251, 11, 1)
)
axQosFlowStatsInTotalEntry.setIndexNames(
    (0, "AX-FLOW-MIB", "axQosFlowStatsInTotalifIndex"),
    (0, "AX-FLOW-MIB", "axQosFlowStatsInTotalGroupType"),
    (0, "AX-FLOW-MIB", "axQosFlowStatsInTotalSequenceNumber"),
)
if mibBuilder.loadTexts:
    axQosFlowStatsInTotalEntry.setStatus("current")


class _AxQosFlowStatsInTotalifIndex_Type(Integer32):
    """Custom type axQosFlowStatsInTotalifIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_AxQosFlowStatsInTotalifIndex_Type.__name__ = "Integer32"
_AxQosFlowStatsInTotalifIndex_Object = MibTableColumn
axQosFlowStatsInTotalifIndex = _AxQosFlowStatsInTotalifIndex_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 8, 251, 11, 1, 1),
    _AxQosFlowStatsInTotalifIndex_Type()
)
axQosFlowStatsInTotalifIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    axQosFlowStatsInTotalifIndex.setStatus("current")


class _AxQosFlowStatsInTotalGroupType_Type(Integer32):
    """Custom type axQosFlowStatsInTotalGroupType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("mac", 1),
          ("ip", 2),
          ("ipv6", 3),
          ("advance", 4))
    )


_AxQosFlowStatsInTotalGroupType_Type.__name__ = "Integer32"
_AxQosFlowStatsInTotalGroupType_Object = MibTableColumn
axQosFlowStatsInTotalGroupType = _AxQosFlowStatsInTotalGroupType_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 8, 251, 11, 1, 2),
    _AxQosFlowStatsInTotalGroupType_Type()
)
axQosFlowStatsInTotalGroupType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    axQosFlowStatsInTotalGroupType.setStatus("current")
_AxQosFlowStatsInTotalSequenceNumber_Type = Unsigned32
_AxQosFlowStatsInTotalSequenceNumber_Object = MibTableColumn
axQosFlowStatsInTotalSequenceNumber = _AxQosFlowStatsInTotalSequenceNumber_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 8, 251, 11, 1, 3),
    _AxQosFlowStatsInTotalSequenceNumber_Type()
)
axQosFlowStatsInTotalSequenceNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    axQosFlowStatsInTotalSequenceNumber.setStatus("current")
_AxQosFlowStatsInTotalListName_Type = DisplayString
_AxQosFlowStatsInTotalListName_Object = MibTableColumn
axQosFlowStatsInTotalListName = _AxQosFlowStatsInTotalListName_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 8, 251, 11, 1, 4),
    _AxQosFlowStatsInTotalListName_Type()
)
axQosFlowStatsInTotalListName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axQosFlowStatsInTotalListName.setStatus("current")
_AxQosFlowStatsInTotalMatchedPackets_Type = Counter64
_AxQosFlowStatsInTotalMatchedPackets_Object = MibTableColumn
axQosFlowStatsInTotalMatchedPackets = _AxQosFlowStatsInTotalMatchedPackets_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 8, 251, 11, 1, 5),
    _AxQosFlowStatsInTotalMatchedPackets_Type()
)
axQosFlowStatsInTotalMatchedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axQosFlowStatsInTotalMatchedPackets.setStatus("current")
_AxQosFlowStatsInTotalMatchedBytes_Type = Counter64
_AxQosFlowStatsInTotalMatchedBytes_Object = MibTableColumn
axQosFlowStatsInTotalMatchedBytes = _AxQosFlowStatsInTotalMatchedBytes_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 8, 251, 11, 1, 6),
    _AxQosFlowStatsInTotalMatchedBytes_Type()
)
axQosFlowStatsInTotalMatchedBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axQosFlowStatsInTotalMatchedBytes.setStatus("current")
_AxQosFlowStatsOutTotalTable_Object = MibTable
axQosFlowStatsOutTotalTable = _AxQosFlowStatsOutTotalTable_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 8, 251, 21)
)
if mibBuilder.loadTexts:
    axQosFlowStatsOutTotalTable.setStatus("current")
_AxQosFlowStatsOutTotalEntry_Object = MibTableRow
axQosFlowStatsOutTotalEntry = _AxQosFlowStatsOutTotalEntry_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 8, 251, 21, 1)
)
axQosFlowStatsOutTotalEntry.setIndexNames(
    (0, "AX-FLOW-MIB", "axQosFlowStatsOutTotalifIndex"),
    (0, "AX-FLOW-MIB", "axQosFlowStatsOutTotalGroupType"),
    (0, "AX-FLOW-MIB", "axQosFlowStatsOutTotalSequenceNumber"),
)
if mibBuilder.loadTexts:
    axQosFlowStatsOutTotalEntry.setStatus("current")


class _AxQosFlowStatsOutTotalifIndex_Type(Integer32):
    """Custom type axQosFlowStatsOutTotalifIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_AxQosFlowStatsOutTotalifIndex_Type.__name__ = "Integer32"
_AxQosFlowStatsOutTotalifIndex_Object = MibTableColumn
axQosFlowStatsOutTotalifIndex = _AxQosFlowStatsOutTotalifIndex_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 8, 251, 21, 1, 1),
    _AxQosFlowStatsOutTotalifIndex_Type()
)
axQosFlowStatsOutTotalifIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    axQosFlowStatsOutTotalifIndex.setStatus("current")


class _AxQosFlowStatsOutTotalGroupType_Type(Integer32):
    """Custom type axQosFlowStatsOutTotalGroupType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("mac", 1),
          ("ip", 2),
          ("ipv6", 3),
          ("advance", 4))
    )


_AxQosFlowStatsOutTotalGroupType_Type.__name__ = "Integer32"
_AxQosFlowStatsOutTotalGroupType_Object = MibTableColumn
axQosFlowStatsOutTotalGroupType = _AxQosFlowStatsOutTotalGroupType_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 8, 251, 21, 1, 2),
    _AxQosFlowStatsOutTotalGroupType_Type()
)
axQosFlowStatsOutTotalGroupType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    axQosFlowStatsOutTotalGroupType.setStatus("current")
_AxQosFlowStatsOutTotalSequenceNumber_Type = Unsigned32
_AxQosFlowStatsOutTotalSequenceNumber_Object = MibTableColumn
axQosFlowStatsOutTotalSequenceNumber = _AxQosFlowStatsOutTotalSequenceNumber_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 8, 251, 21, 1, 3),
    _AxQosFlowStatsOutTotalSequenceNumber_Type()
)
axQosFlowStatsOutTotalSequenceNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    axQosFlowStatsOutTotalSequenceNumber.setStatus("current")
_AxQosFlowStatsOutTotalListName_Type = DisplayString
_AxQosFlowStatsOutTotalListName_Object = MibTableColumn
axQosFlowStatsOutTotalListName = _AxQosFlowStatsOutTotalListName_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 8, 251, 21, 1, 4),
    _AxQosFlowStatsOutTotalListName_Type()
)
axQosFlowStatsOutTotalListName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axQosFlowStatsOutTotalListName.setStatus("current")
_AxQosFlowStatsOutTotalMatchedPackets_Type = Counter64
_AxQosFlowStatsOutTotalMatchedPackets_Object = MibTableColumn
axQosFlowStatsOutTotalMatchedPackets = _AxQosFlowStatsOutTotalMatchedPackets_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 8, 251, 21, 1, 5),
    _AxQosFlowStatsOutTotalMatchedPackets_Type()
)
axQosFlowStatsOutTotalMatchedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axQosFlowStatsOutTotalMatchedPackets.setStatus("current")
_AxQosFlowStatsOutTotalMatchedBytes_Type = Counter64
_AxQosFlowStatsOutTotalMatchedBytes_Object = MibTableColumn
axQosFlowStatsOutTotalMatchedBytes = _AxQosFlowStatsOutTotalMatchedBytes_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 8, 251, 21, 1, 6),
    _AxQosFlowStatsOutTotalMatchedBytes_Type()
)
axQosFlowStatsOutTotalMatchedBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axQosFlowStatsOutTotalMatchedBytes.setStatus("current")
_AxFlowConformance_ObjectIdentity = ObjectIdentity
axFlowConformance = _AxFlowConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 8, 1000)
)
_AxFlowCompliances_ObjectIdentity = ObjectIdentity
axFlowCompliances = _AxFlowCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 8, 1000, 1)
)
_AxFlowGroups_ObjectIdentity = ObjectIdentity
axFlowGroups = _AxFlowGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 8, 1000, 2)
)

# Managed Objects groups

axFlowGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 8, 1000, 2, 1)
)
axFlowGroup.setObjects(
      *(("AX-FLOW-MIB", "axAccessFilterStatsInTotalListName"),
        ("AX-FLOW-MIB", "axAccessFilterStatsInTotalMatchedPackets"),
        ("AX-FLOW-MIB", "axAccessFilterStatsInTotalMatchedBytes"),
        ("AX-FLOW-MIB", "axAccessFilterStatsOutTotalListName"),
        ("AX-FLOW-MIB", "axAccessFilterStatsOutTotalMatchedPackets"),
        ("AX-FLOW-MIB", "axAccessFilterStatsOutTotalMatchedBytes"),
        ("AX-FLOW-MIB", "axAccessFilterStatsInMirrorTotalListName"),
        ("AX-FLOW-MIB", "axAccessFilterStatsInMirrorTotalMatchedPackets"),
        ("AX-FLOW-MIB", "axAccessFilterStatsInMirrorTotalMatchedBytes"),
        ("AX-FLOW-MIB", "axAccessFilterStatsOutMirrorTotalListName"),
        ("AX-FLOW-MIB", "axAccessFilterStatsOutMirrorTotalMatchedPackets"),
        ("AX-FLOW-MIB", "axAccessFilterStatsOutMirrorTotalMatchedBytes"),
        ("AX-FLOW-MIB", "axQosFlowStatsInTotalListName"),
        ("AX-FLOW-MIB", "axQosFlowStatsInTotalMatchedPackets"),
        ("AX-FLOW-MIB", "axQosFlowStatsInTotalMatchedBytes"),
        ("AX-FLOW-MIB", "axQosFlowStatsOutTotalListName"),
        ("AX-FLOW-MIB", "axQosFlowStatsOutTotalMatchedPackets"),
        ("AX-FLOW-MIB", "axQosFlowStatsOutTotalMatchedBytes"))
)
if mibBuilder.loadTexts:
    axFlowGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

axFlowCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 8, 1000, 1, 1)
)
axFlowCompliance.setObjects(
    ("AX-FLOW-MIB", "axFlowGroup")
)
if mibBuilder.loadTexts:
    axFlowCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "AX-FLOW-MIB",
    **{"axFlow": axFlow,
       "axAccessFilterStats": axAccessFilterStats,
       "axAccessFilterStatsInTotalTable": axAccessFilterStatsInTotalTable,
       "axAccessFilterStatsInTotalEntry": axAccessFilterStatsInTotalEntry,
       "axAccessFilterStatsInTotalifIndex": axAccessFilterStatsInTotalifIndex,
       "axAccessFilterStatsInTotalGroupType": axAccessFilterStatsInTotalGroupType,
       "axAccessFilterStatsInTotalSequenceNumber": axAccessFilterStatsInTotalSequenceNumber,
       "axAccessFilterStatsInTotalListName": axAccessFilterStatsInTotalListName,
       "axAccessFilterStatsInTotalMatchedPackets": axAccessFilterStatsInTotalMatchedPackets,
       "axAccessFilterStatsInTotalMatchedBytes": axAccessFilterStatsInTotalMatchedBytes,
       "axAccessFilterStatsOutTotalTable": axAccessFilterStatsOutTotalTable,
       "axAccessFilterStatsOutTotalEntry": axAccessFilterStatsOutTotalEntry,
       "axAccessFilterStatsOutTotalifIndex": axAccessFilterStatsOutTotalifIndex,
       "axAccessFilterStatsOutTotalGroupType": axAccessFilterStatsOutTotalGroupType,
       "axAccessFilterStatsOutTotalSequenceNumber": axAccessFilterStatsOutTotalSequenceNumber,
       "axAccessFilterStatsOutTotalListName": axAccessFilterStatsOutTotalListName,
       "axAccessFilterStatsOutTotalMatchedPackets": axAccessFilterStatsOutTotalMatchedPackets,
       "axAccessFilterStatsOutTotalMatchedBytes": axAccessFilterStatsOutTotalMatchedBytes,
       "axAccessFilterStatsInMirrorTotalTable": axAccessFilterStatsInMirrorTotalTable,
       "axAccessFilterStatsInMirrorTotalEntry": axAccessFilterStatsInMirrorTotalEntry,
       "axAccessFilterStatsInMirrorTotalifIndex": axAccessFilterStatsInMirrorTotalifIndex,
       "axAccessFilterStatsInMirrorTotalGroupType": axAccessFilterStatsInMirrorTotalGroupType,
       "axAccessFilterStatsInMirrorTotalSequenceNumber": axAccessFilterStatsInMirrorTotalSequenceNumber,
       "axAccessFilterStatsInMirrorTotalListName": axAccessFilterStatsInMirrorTotalListName,
       "axAccessFilterStatsInMirrorTotalMatchedPackets": axAccessFilterStatsInMirrorTotalMatchedPackets,
       "axAccessFilterStatsInMirrorTotalMatchedBytes": axAccessFilterStatsInMirrorTotalMatchedBytes,
       "axAccessFilterStatsOutMirrorTotalTable": axAccessFilterStatsOutMirrorTotalTable,
       "axAccessFilterStatsOutMirrorTotalEntry": axAccessFilterStatsOutMirrorTotalEntry,
       "axAccessFilterStatsOutMirrorTotalifIndex": axAccessFilterStatsOutMirrorTotalifIndex,
       "axAccessFilterStatsOutMirrorTotalGroupType": axAccessFilterStatsOutMirrorTotalGroupType,
       "axAccessFilterStatsOutMirrorTotalSequenceNumber": axAccessFilterStatsOutMirrorTotalSequenceNumber,
       "axAccessFilterStatsOutMirrorTotalListName": axAccessFilterStatsOutMirrorTotalListName,
       "axAccessFilterStatsOutMirrorTotalMatchedPackets": axAccessFilterStatsOutMirrorTotalMatchedPackets,
       "axAccessFilterStatsOutMirrorTotalMatchedBytes": axAccessFilterStatsOutMirrorTotalMatchedBytes,
       "axQosFlowStats": axQosFlowStats,
       "axQosFlowStatsInTotalTable": axQosFlowStatsInTotalTable,
       "axQosFlowStatsInTotalEntry": axQosFlowStatsInTotalEntry,
       "axQosFlowStatsInTotalifIndex": axQosFlowStatsInTotalifIndex,
       "axQosFlowStatsInTotalGroupType": axQosFlowStatsInTotalGroupType,
       "axQosFlowStatsInTotalSequenceNumber": axQosFlowStatsInTotalSequenceNumber,
       "axQosFlowStatsInTotalListName": axQosFlowStatsInTotalListName,
       "axQosFlowStatsInTotalMatchedPackets": axQosFlowStatsInTotalMatchedPackets,
       "axQosFlowStatsInTotalMatchedBytes": axQosFlowStatsInTotalMatchedBytes,
       "axQosFlowStatsOutTotalTable": axQosFlowStatsOutTotalTable,
       "axQosFlowStatsOutTotalEntry": axQosFlowStatsOutTotalEntry,
       "axQosFlowStatsOutTotalifIndex": axQosFlowStatsOutTotalifIndex,
       "axQosFlowStatsOutTotalGroupType": axQosFlowStatsOutTotalGroupType,
       "axQosFlowStatsOutTotalSequenceNumber": axQosFlowStatsOutTotalSequenceNumber,
       "axQosFlowStatsOutTotalListName": axQosFlowStatsOutTotalListName,
       "axQosFlowStatsOutTotalMatchedPackets": axQosFlowStatsOutTotalMatchedPackets,
       "axQosFlowStatsOutTotalMatchedBytes": axQosFlowStatsOutTotalMatchedBytes,
       "axFlowConformance": axFlowConformance,
       "axFlowCompliances": axFlowCompliances,
       "axFlowCompliance": axFlowCompliance,
       "axFlowGroups": axFlowGroups,
       "axFlowGroup": axFlowGroup}
)
