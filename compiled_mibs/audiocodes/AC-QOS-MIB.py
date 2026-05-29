# SNMP MIB module (AC-QOS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\audiocodes\AC-QOS-MIB

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

(acBoardMibs,
 acGeneric,
 acProducts,
 acRegistrations,
 audioCodes) = mibBuilder.importSymbols(
    "AUDIOCODES-TYPES-MIB",
    "acBoardMibs",
    "acGeneric",
    "acProducts",
    "acRegistrations",
    "audioCodes")

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

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
 enterprises,
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
    "enterprises",
    "iso")

(DateAndTime,
 DisplayString,
 PhysAddress,
 RowPointer,
 RowStatus,
 TAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "PhysAddress",
    "RowPointer",
    "RowStatus",
    "TAddress",
    "TextualConvention")


# MODULE-IDENTITY

acQoS = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 14)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AcQoSConfiguration_ObjectIdentity = ObjectIdentity
acQoSConfiguration = _AcQoSConfiguration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 14, 1)
)
_AcQoSMatchMapTable_Object = MibTable
acQoSMatchMapTable = _AcQoSMatchMapTable_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 14, 1, 1)
)
if mibBuilder.loadTexts:
    acQoSMatchMapTable.setStatus("current")
_AcQoSMatchMapEntry_Object = MibTableRow
acQoSMatchMapEntry = _AcQoSMatchMapEntry_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 14, 1, 1, 1)
)
acQoSMatchMapEntry.setIndexNames(
    (0, "AC-QOS-MIB", "acQoSMatchMapIndex"),
)
if mibBuilder.loadTexts:
    acQoSMatchMapEntry.setStatus("current")


class _AcQoSMatchMapIndex_Type(Unsigned32):
    """Custom type acQoSMatchMapIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1000000, 2069099),
    )


_AcQoSMatchMapIndex_Type.__name__ = "Unsigned32"
_AcQoSMatchMapIndex_Object = MibTableColumn
acQoSMatchMapIndex = _AcQoSMatchMapIndex_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 14, 1, 1, 1, 1),
    _AcQoSMatchMapIndex_Type()
)
acQoSMatchMapIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    acQoSMatchMapIndex.setStatus("current")


class _AcQoSMatchMapName_Type(SnmpAdminString):
    """Custom type acQoSMatchMapName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_AcQoSMatchMapName_Type.__name__ = "SnmpAdminString"
_AcQoSMatchMapName_Object = MibTableColumn
acQoSMatchMapName = _AcQoSMatchMapName_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 14, 1, 1, 1, 2),
    _AcQoSMatchMapName_Type()
)
acQoSMatchMapName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acQoSMatchMapName.setStatus("current")


class _AcQoSMatchMapDirection_Type(Integer32):
    """Custom type acQoSMatchMapDirection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("input", 1),
          ("output", 2))
    )


_AcQoSMatchMapDirection_Type.__name__ = "Integer32"
_AcQoSMatchMapDirection_Object = MibTableColumn
acQoSMatchMapDirection = _AcQoSMatchMapDirection_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 14, 1, 1, 1, 3),
    _AcQoSMatchMapDirection_Type()
)
acQoSMatchMapDirection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acQoSMatchMapDirection.setStatus("current")


class _AcQoSMatchMapInterface_Type(SnmpAdminString):
    """Custom type acQoSMatchMapInterface based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_AcQoSMatchMapInterface_Type.__name__ = "SnmpAdminString"
_AcQoSMatchMapInterface_Object = MibTableColumn
acQoSMatchMapInterface = _AcQoSMatchMapInterface_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 14, 1, 1, 1, 4),
    _AcQoSMatchMapInterface_Type()
)
acQoSMatchMapInterface.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acQoSMatchMapInterface.setStatus("current")
_AcQoSMatchTable_Object = MibTable
acQoSMatchTable = _AcQoSMatchTable_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 14, 1, 2)
)
if mibBuilder.loadTexts:
    acQoSMatchTable.setStatus("current")
_AcQoSMatchEntry_Object = MibTableRow
acQoSMatchEntry = _AcQoSMatchEntry_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 14, 1, 2, 1)
)
acQoSMatchEntry.setIndexNames(
    (0, "AC-QOS-MIB", "acQoSMatchMatchMapIndex"),
    (0, "AC-QOS-MIB", "acQoSMatchIndex"),
)
if mibBuilder.loadTexts:
    acQoSMatchEntry.setStatus("current")


class _AcQoSMatchMatchMapIndex_Type(Unsigned32):
    """Custom type acQoSMatchMatchMapIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1000000, 2069099),
    )


_AcQoSMatchMatchMapIndex_Type.__name__ = "Unsigned32"
_AcQoSMatchMatchMapIndex_Object = MibTableColumn
acQoSMatchMatchMapIndex = _AcQoSMatchMatchMapIndex_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 14, 1, 2, 1, 1),
    _AcQoSMatchMatchMapIndex_Type()
)
acQoSMatchMatchMapIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    acQoSMatchMatchMapIndex.setStatus("current")


class _AcQoSMatchIndex_Type(Unsigned32):
    """Custom type acQoSMatchIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 6),
    )


_AcQoSMatchIndex_Type.__name__ = "Unsigned32"
_AcQoSMatchIndex_Object = MibTableColumn
acQoSMatchIndex = _AcQoSMatchIndex_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 14, 1, 2, 1, 2),
    _AcQoSMatchIndex_Type()
)
acQoSMatchIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    acQoSMatchIndex.setStatus("current")


class _AcQoSMatchType_Type(Integer32):
    """Custom type acQoSMatchType based on Integer32"""
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
        *(("any", 1),
          ("accessMap", 2),
          ("dscp", 3),
          ("dataLength", 4),
          ("packetLength", 5),
          ("precedence", 6),
          ("priority", 7))
    )


_AcQoSMatchType_Type.__name__ = "Integer32"
_AcQoSMatchType_Object = MibTableColumn
acQoSMatchType = _AcQoSMatchType_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 14, 1, 2, 1, 3),
    _AcQoSMatchType_Type()
)
acQoSMatchType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acQoSMatchType.setStatus("current")


class _AcQoSMatchAccessMap_Type(SnmpAdminString):
    """Custom type acQoSMatchAccessMap based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_AcQoSMatchAccessMap_Type.__name__ = "SnmpAdminString"
_AcQoSMatchAccessMap_Object = MibTableColumn
acQoSMatchAccessMap = _AcQoSMatchAccessMap_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 14, 1, 2, 1, 4),
    _AcQoSMatchAccessMap_Type()
)
acQoSMatchAccessMap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acQoSMatchAccessMap.setStatus("current")


class _AcQoSMatchDscpValue_Type(Unsigned32):
    """Custom type acQoSMatchDscpValue based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_AcQoSMatchDscpValue_Type.__name__ = "Unsigned32"
_AcQoSMatchDscpValue_Object = MibTableColumn
acQoSMatchDscpValue = _AcQoSMatchDscpValue_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 14, 1, 2, 1, 5),
    _AcQoSMatchDscpValue_Type()
)
acQoSMatchDscpValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acQoSMatchDscpValue.setStatus("current")


class _AcQoSMatchMinLength_Type(Unsigned32):
    """Custom type acQoSMatchMinLength based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AcQoSMatchMinLength_Type.__name__ = "Unsigned32"
_AcQoSMatchMinLength_Object = MibTableColumn
acQoSMatchMinLength = _AcQoSMatchMinLength_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 14, 1, 2, 1, 6),
    _AcQoSMatchMinLength_Type()
)
acQoSMatchMinLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acQoSMatchMinLength.setStatus("current")


class _AcQoSMatchMaxLength_Type(Unsigned32):
    """Custom type acQoSMatchMaxLength based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AcQoSMatchMaxLength_Type.__name__ = "Unsigned32"
_AcQoSMatchMaxLength_Object = MibTableColumn
acQoSMatchMaxLength = _AcQoSMatchMaxLength_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 14, 1, 2, 1, 7),
    _AcQoSMatchMaxLength_Type()
)
acQoSMatchMaxLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acQoSMatchMaxLength.setStatus("current")


class _AcQoSMatchPrecedenceValue_Type(Integer32):
    """Custom type acQoSMatchPrecedenceValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("routine", 0),
          ("priority", 1),
          ("immediate", 2),
          ("flash", 3),
          ("flash-override", 4),
          ("critical", 5),
          ("internet", 6),
          ("network", 7))
    )


_AcQoSMatchPrecedenceValue_Type.__name__ = "Integer32"
_AcQoSMatchPrecedenceValue_Object = MibTableColumn
acQoSMatchPrecedenceValue = _AcQoSMatchPrecedenceValue_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 14, 1, 2, 1, 8),
    _AcQoSMatchPrecedenceValue_Type()
)
acQoSMatchPrecedenceValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acQoSMatchPrecedenceValue.setStatus("current")


class _AcQoSMatchPriorityValue_Type(Unsigned32):
    """Custom type acQoSMatchPriorityValue based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_AcQoSMatchPriorityValue_Type.__name__ = "Unsigned32"
_AcQoSMatchPriorityValue_Object = MibTableColumn
acQoSMatchPriorityValue = _AcQoSMatchPriorityValue_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 14, 1, 2, 1, 9),
    _AcQoSMatchPriorityValue_Type()
)
acQoSMatchPriorityValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acQoSMatchPriorityValue.setStatus("current")
_AcQoSSetTable_Object = MibTable
acQoSSetTable = _AcQoSSetTable_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 14, 1, 3)
)
if mibBuilder.loadTexts:
    acQoSSetTable.setStatus("current")
_AcQoSSetEntry_Object = MibTableRow
acQoSSetEntry = _AcQoSSetEntry_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 14, 1, 3, 1)
)
acQoSSetEntry.setIndexNames(
    (0, "AC-QOS-MIB", "acQoSSetMatchMapIndex"),
    (0, "AC-QOS-MIB", "acQoSSetIndex"),
)
if mibBuilder.loadTexts:
    acQoSSetEntry.setStatus("current")


class _AcQoSSetMatchMapIndex_Type(Unsigned32):
    """Custom type acQoSSetMatchMapIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1000000, 2069099),
    )


_AcQoSSetMatchMapIndex_Type.__name__ = "Unsigned32"
_AcQoSSetMatchMapIndex_Object = MibTableColumn
acQoSSetMatchMapIndex = _AcQoSSetMatchMapIndex_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 14, 1, 3, 1, 1),
    _AcQoSSetMatchMapIndex_Type()
)
acQoSSetMatchMapIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    acQoSSetMatchMapIndex.setStatus("current")


class _AcQoSSetIndex_Type(Unsigned32):
    """Custom type acQoSSetIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_AcQoSSetIndex_Type.__name__ = "Unsigned32"
_AcQoSSetIndex_Object = MibTableColumn
acQoSSetIndex = _AcQoSSetIndex_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 14, 1, 3, 1, 2),
    _AcQoSSetIndex_Type()
)
acQoSSetIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    acQoSSetIndex.setStatus("current")


class _AcQoSSetType_Type(Integer32):
    """Custom type acQoSSetType based on Integer32"""
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
        *(("queue", 1),
          ("dscp", 2),
          ("precedence", 3),
          ("priority", 4))
    )


_AcQoSSetType_Type.__name__ = "Integer32"
_AcQoSSetType_Object = MibTableColumn
acQoSSetType = _AcQoSSetType_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 14, 1, 3, 1, 3),
    _AcQoSSetType_Type()
)
acQoSSetType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acQoSSetType.setStatus("current")


class _AcQoSSetQueueName_Type(SnmpAdminString):
    """Custom type acQoSSetQueueName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_AcQoSSetQueueName_Type.__name__ = "SnmpAdminString"
_AcQoSSetQueueName_Object = MibTableColumn
acQoSSetQueueName = _AcQoSSetQueueName_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 14, 1, 3, 1, 4),
    _AcQoSSetQueueName_Type()
)
acQoSSetQueueName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acQoSSetQueueName.setStatus("current")


class _AcQoSSetDscpValue_Type(Unsigned32):
    """Custom type acQoSSetDscpValue based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_AcQoSSetDscpValue_Type.__name__ = "Unsigned32"
_AcQoSSetDscpValue_Object = MibTableColumn
acQoSSetDscpValue = _AcQoSSetDscpValue_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 14, 1, 3, 1, 5),
    _AcQoSSetDscpValue_Type()
)
acQoSSetDscpValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acQoSSetDscpValue.setStatus("current")


class _AcQoSSetPrecedenceValue_Type(Integer32):
    """Custom type acQoSSetPrecedenceValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("routine", 0),
          ("priority", 1),
          ("immediate", 2),
          ("flash", 3),
          ("flash-override", 4),
          ("critical", 5),
          ("internet", 6),
          ("network", 7))
    )


_AcQoSSetPrecedenceValue_Type.__name__ = "Integer32"
_AcQoSSetPrecedenceValue_Object = MibTableColumn
acQoSSetPrecedenceValue = _AcQoSSetPrecedenceValue_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 14, 1, 3, 1, 6),
    _AcQoSSetPrecedenceValue_Type()
)
acQoSSetPrecedenceValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acQoSSetPrecedenceValue.setStatus("current")


class _AcQoSSetPriorityValue_Type(Unsigned32):
    """Custom type acQoSSetPriorityValue based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_AcQoSSetPriorityValue_Type.__name__ = "Unsigned32"
_AcQoSSetPriorityValue_Object = MibTableColumn
acQoSSetPriorityValue = _AcQoSSetPriorityValue_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 14, 1, 3, 1, 7),
    _AcQoSSetPriorityValue_Type()
)
acQoSSetPriorityValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acQoSSetPriorityValue.setStatus("current")
_AcQoSServiceMapTable_Object = MibTable
acQoSServiceMapTable = _AcQoSServiceMapTable_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 14, 1, 4)
)
if mibBuilder.loadTexts:
    acQoSServiceMapTable.setStatus("current")
_AcQoSServiceMapEntry_Object = MibTableRow
acQoSServiceMapEntry = _AcQoSServiceMapEntry_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 14, 1, 4, 1)
)
acQoSServiceMapEntry.setIndexNames(
    (0, "AC-QOS-MIB", "acQoSServiceMapIndex"),
)
if mibBuilder.loadTexts:
    acQoSServiceMapEntry.setStatus("current")


class _AcQoSServiceMapIndex_Type(Unsigned32):
    """Custom type acQoSServiceMapIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 69),
    )


_AcQoSServiceMapIndex_Type.__name__ = "Unsigned32"
_AcQoSServiceMapIndex_Object = MibTableColumn
acQoSServiceMapIndex = _AcQoSServiceMapIndex_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 14, 1, 4, 1, 1),
    _AcQoSServiceMapIndex_Type()
)
acQoSServiceMapIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    acQoSServiceMapIndex.setStatus("current")


class _AcQoSServiceMapInterface_Type(SnmpAdminString):
    """Custom type acQoSServiceMapInterface based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_AcQoSServiceMapInterface_Type.__name__ = "SnmpAdminString"
_AcQoSServiceMapInterface_Object = MibTableColumn
acQoSServiceMapInterface = _AcQoSServiceMapInterface_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 14, 1, 4, 1, 2),
    _AcQoSServiceMapInterface_Type()
)
acQoSServiceMapInterface.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acQoSServiceMapInterface.setStatus("current")


class _AcQoSServiceMapDirection_Type(Integer32):
    """Custom type acQoSServiceMapDirection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("input", 1),
          ("output", 2))
    )


_AcQoSServiceMapDirection_Type.__name__ = "Integer32"
_AcQoSServiceMapDirection_Object = MibTableColumn
acQoSServiceMapDirection = _AcQoSServiceMapDirection_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 14, 1, 4, 1, 3),
    _AcQoSServiceMapDirection_Type()
)
acQoSServiceMapDirection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acQoSServiceMapDirection.setStatus("current")


class _AcQoSServiceMapBandwidthLimit_Type(Integer32):
    """Custom type acQoSServiceMapBandwidthLimit based on Integer32"""
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
          ("limited", 2),
          ("automatic", 3))
    )


_AcQoSServiceMapBandwidthLimit_Type.__name__ = "Integer32"
_AcQoSServiceMapBandwidthLimit_Object = MibTableColumn
acQoSServiceMapBandwidthLimit = _AcQoSServiceMapBandwidthLimit_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 14, 1, 4, 1, 4),
    _AcQoSServiceMapBandwidthLimit_Type()
)
acQoSServiceMapBandwidthLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acQoSServiceMapBandwidthLimit.setStatus("current")
_AcQoSServiceMapMaxBandwidth_Type = Unsigned32
_AcQoSServiceMapMaxBandwidth_Object = MibTableColumn
acQoSServiceMapMaxBandwidth = _AcQoSServiceMapMaxBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 14, 1, 4, 1, 5),
    _AcQoSServiceMapMaxBandwidth_Type()
)
acQoSServiceMapMaxBandwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acQoSServiceMapMaxBandwidth.setStatus("current")
_AcQoSQueueTable_Object = MibTable
acQoSQueueTable = _AcQoSQueueTable_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 14, 1, 5)
)
if mibBuilder.loadTexts:
    acQoSQueueTable.setStatus("current")
_AcQoSQueueEntry_Object = MibTableRow
acQoSQueueEntry = _AcQoSQueueEntry_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 14, 1, 5, 1)
)
acQoSQueueEntry.setIndexNames(
    (0, "AC-QOS-MIB", "acQoSQueueServiceMapIndex"),
    (0, "AC-QOS-MIB", "acQoSQueueIndex"),
)
if mibBuilder.loadTexts:
    acQoSQueueEntry.setStatus("current")


class _AcQoSQueueServiceMapIndex_Type(Unsigned32):
    """Custom type acQoSQueueServiceMapIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 69),
    )


_AcQoSQueueServiceMapIndex_Type.__name__ = "Unsigned32"
_AcQoSQueueServiceMapIndex_Object = MibTableColumn
acQoSQueueServiceMapIndex = _AcQoSQueueServiceMapIndex_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 14, 1, 5, 1, 1),
    _AcQoSQueueServiceMapIndex_Type()
)
acQoSQueueServiceMapIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    acQoSQueueServiceMapIndex.setStatus("current")


class _AcQoSQueueIndex_Type(Unsigned32):
    """Custom type acQoSQueueIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 99),
    )


_AcQoSQueueIndex_Type.__name__ = "Unsigned32"
_AcQoSQueueIndex_Object = MibTableColumn
acQoSQueueIndex = _AcQoSQueueIndex_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 14, 1, 5, 1, 2),
    _AcQoSQueueIndex_Type()
)
acQoSQueueIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    acQoSQueueIndex.setStatus("current")


class _AcQoSQueueName_Type(SnmpAdminString):
    """Custom type acQoSQueueName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_AcQoSQueueName_Type.__name__ = "SnmpAdminString"
_AcQoSQueueName_Object = MibTableColumn
acQoSQueueName = _AcQoSQueueName_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 14, 1, 5, 1, 3),
    _AcQoSQueueName_Type()
)
acQoSQueueName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acQoSQueueName.setStatus("current")
_AcQoSQueueActionTable_Object = MibTable
acQoSQueueActionTable = _AcQoSQueueActionTable_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 14, 1, 6)
)
if mibBuilder.loadTexts:
    acQoSQueueActionTable.setStatus("current")
_AcQoSQueueActionEntry_Object = MibTableRow
acQoSQueueActionEntry = _AcQoSQueueActionEntry_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 14, 1, 6, 1)
)
acQoSQueueActionEntry.setIndexNames(
    (0, "AC-QOS-MIB", "acQoSQueueActionServiceMapIndex"),
    (0, "AC-QOS-MIB", "acQoSQueueActionQueueIndex"),
    (0, "AC-QOS-MIB", "acQoSQueueActionIndex"),
)
if mibBuilder.loadTexts:
    acQoSQueueActionEntry.setStatus("current")


class _AcQoSQueueActionServiceMapIndex_Type(Unsigned32):
    """Custom type acQoSQueueActionServiceMapIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 69),
    )


_AcQoSQueueActionServiceMapIndex_Type.__name__ = "Unsigned32"
_AcQoSQueueActionServiceMapIndex_Object = MibTableColumn
acQoSQueueActionServiceMapIndex = _AcQoSQueueActionServiceMapIndex_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 14, 1, 6, 1, 1),
    _AcQoSQueueActionServiceMapIndex_Type()
)
acQoSQueueActionServiceMapIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    acQoSQueueActionServiceMapIndex.setStatus("current")


class _AcQoSQueueActionQueueIndex_Type(Unsigned32):
    """Custom type acQoSQueueActionQueueIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 99),
    )


_AcQoSQueueActionQueueIndex_Type.__name__ = "Unsigned32"
_AcQoSQueueActionQueueIndex_Object = MibTableColumn
acQoSQueueActionQueueIndex = _AcQoSQueueActionQueueIndex_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 14, 1, 6, 1, 2),
    _AcQoSQueueActionQueueIndex_Type()
)
acQoSQueueActionQueueIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    acQoSQueueActionQueueIndex.setStatus("current")


class _AcQoSQueueActionIndex_Type(Unsigned32):
    """Custom type acQoSQueueActionIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_AcQoSQueueActionIndex_Type.__name__ = "Unsigned32"
_AcQoSQueueActionIndex_Object = MibTableColumn
acQoSQueueActionIndex = _AcQoSQueueActionIndex_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 14, 1, 6, 1, 3),
    _AcQoSQueueActionIndex_Type()
)
acQoSQueueActionIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    acQoSQueueActionIndex.setStatus("current")


class _AcQoSQueueActionType_Type(Integer32):
    """Custom type acQoSQueueActionType based on Integer32"""
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
        *(("bandwidth", 1),
          ("bandwidth-percent", 2),
          ("policy", 3),
          ("priority", 4))
    )


_AcQoSQueueActionType_Type.__name__ = "Integer32"
_AcQoSQueueActionType_Object = MibTableColumn
acQoSQueueActionType = _AcQoSQueueActionType_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 14, 1, 6, 1, 4),
    _AcQoSQueueActionType_Type()
)
acQoSQueueActionType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acQoSQueueActionType.setStatus("current")
_AcQoSQueueActionMinBandwidth_Type = Unsigned32
_AcQoSQueueActionMinBandwidth_Object = MibTableColumn
acQoSQueueActionMinBandwidth = _AcQoSQueueActionMinBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 14, 1, 6, 1, 5),
    _AcQoSQueueActionMinBandwidth_Type()
)
acQoSQueueActionMinBandwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acQoSQueueActionMinBandwidth.setStatus("current")
_AcQoSQueueActionMaxBandwidth_Type = Unsigned32
_AcQoSQueueActionMaxBandwidth_Object = MibTableColumn
acQoSQueueActionMaxBandwidth = _AcQoSQueueActionMaxBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 14, 1, 6, 1, 6),
    _AcQoSQueueActionMaxBandwidth_Type()
)
acQoSQueueActionMaxBandwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acQoSQueueActionMaxBandwidth.setStatus("current")


class _AcQoSQueueActionPolicyValue_Type(Integer32):
    """Custom type acQoSQueueActionPolicyValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 0),
          ("fairness", 1),
          ("fifo", 2),
          ("random-detect", 3),
          ("strict-priority", 4))
    )


_AcQoSQueueActionPolicyValue_Type.__name__ = "Integer32"
_AcQoSQueueActionPolicyValue_Object = MibTableColumn
acQoSQueueActionPolicyValue = _AcQoSQueueActionPolicyValue_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 14, 1, 6, 1, 7),
    _AcQoSQueueActionPolicyValue_Type()
)
acQoSQueueActionPolicyValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acQoSQueueActionPolicyValue.setStatus("current")


class _AcQoSQueueActionPriorityValue_Type(Unsigned32):
    """Custom type acQoSQueueActionPriorityValue based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_AcQoSQueueActionPriorityValue_Type.__name__ = "Unsigned32"
_AcQoSQueueActionPriorityValue_Object = MibTableColumn
acQoSQueueActionPriorityValue = _AcQoSQueueActionPriorityValue_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 14, 1, 6, 1, 8),
    _AcQoSQueueActionPriorityValue_Type()
)
acQoSQueueActionPriorityValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acQoSQueueActionPriorityValue.setStatus("current")
_AcQoSStatus_ObjectIdentity = ObjectIdentity
acQoSStatus = _AcQoSStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 14, 2)
)
_AcQoSQueueStatsTable_Object = MibTable
acQoSQueueStatsTable = _AcQoSQueueStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 14, 2, 1)
)
if mibBuilder.loadTexts:
    acQoSQueueStatsTable.setStatus("current")
_AcQoSQueueStatsEntry_Object = MibTableRow
acQoSQueueStatsEntry = _AcQoSQueueStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 14, 2, 1, 1)
)
acQoSQueueStatsEntry.setIndexNames(
    (0, "AC-QOS-MIB", "acQoSQueueStatsServiceMapIndex"),
    (0, "AC-QOS-MIB", "acQoSQueueStatsQueueIndex"),
)
if mibBuilder.loadTexts:
    acQoSQueueStatsEntry.setStatus("current")


class _AcQoSQueueStatsServiceMapIndex_Type(Unsigned32):
    """Custom type acQoSQueueStatsServiceMapIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 69),
    )


_AcQoSQueueStatsServiceMapIndex_Type.__name__ = "Unsigned32"
_AcQoSQueueStatsServiceMapIndex_Object = MibTableColumn
acQoSQueueStatsServiceMapIndex = _AcQoSQueueStatsServiceMapIndex_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 14, 2, 1, 1, 1),
    _AcQoSQueueStatsServiceMapIndex_Type()
)
acQoSQueueStatsServiceMapIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    acQoSQueueStatsServiceMapIndex.setStatus("current")


class _AcQoSQueueStatsQueueIndex_Type(Unsigned32):
    """Custom type acQoSQueueStatsQueueIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 99),
    )


_AcQoSQueueStatsQueueIndex_Type.__name__ = "Unsigned32"
_AcQoSQueueStatsQueueIndex_Object = MibTableColumn
acQoSQueueStatsQueueIndex = _AcQoSQueueStatsQueueIndex_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 14, 2, 1, 1, 2),
    _AcQoSQueueStatsQueueIndex_Type()
)
acQoSQueueStatsQueueIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    acQoSQueueStatsQueueIndex.setStatus("current")
_AcQoSQueueStatsPacketSent_Type = Counter32
_AcQoSQueueStatsPacketSent_Object = MibTableColumn
acQoSQueueStatsPacketSent = _AcQoSQueueStatsPacketSent_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 14, 2, 1, 1, 3),
    _AcQoSQueueStatsPacketSent_Type()
)
acQoSQueueStatsPacketSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acQoSQueueStatsPacketSent.setStatus("current")
_AcQoSQueueStatsBytesSent_Type = Counter32
_AcQoSQueueStatsBytesSent_Object = MibTableColumn
acQoSQueueStatsBytesSent = _AcQoSQueueStatsBytesSent_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 14, 2, 1, 1, 4),
    _AcQoSQueueStatsBytesSent_Type()
)
acQoSQueueStatsBytesSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acQoSQueueStatsBytesSent.setStatus("current")
_AcQoSQueueStatsPacketsRate_Type = Counter32
_AcQoSQueueStatsPacketsRate_Object = MibTableColumn
acQoSQueueStatsPacketsRate = _AcQoSQueueStatsPacketsRate_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 14, 2, 1, 1, 5),
    _AcQoSQueueStatsPacketsRate_Type()
)
acQoSQueueStatsPacketsRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acQoSQueueStatsPacketsRate.setStatus("current")
_AcQoSQueueStatsBytesRate_Type = Counter32
_AcQoSQueueStatsBytesRate_Object = MibTableColumn
acQoSQueueStatsBytesRate = _AcQoSQueueStatsBytesRate_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 14, 2, 1, 1, 6),
    _AcQoSQueueStatsBytesRate_Type()
)
acQoSQueueStatsBytesRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acQoSQueueStatsBytesRate.setStatus("current")
_AcQoSQueueStatsPacketsDelayed_Type = Counter32
_AcQoSQueueStatsPacketsDelayed_Object = MibTableColumn
acQoSQueueStatsPacketsDelayed = _AcQoSQueueStatsPacketsDelayed_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 14, 2, 1, 1, 7),
    _AcQoSQueueStatsPacketsDelayed_Type()
)
acQoSQueueStatsPacketsDelayed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acQoSQueueStatsPacketsDelayed.setStatus("current")
_AcQoSQueueStatsPacketsDropped_Type = Counter32
_AcQoSQueueStatsPacketsDropped_Object = MibTableColumn
acQoSQueueStatsPacketsDropped = _AcQoSQueueStatsPacketsDropped_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 14, 2, 1, 1, 8),
    _AcQoSQueueStatsPacketsDropped_Type()
)
acQoSQueueStatsPacketsDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acQoSQueueStatsPacketsDropped.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "AC-QOS-MIB",
    **{"acQoS": acQoS,
       "acQoSConfiguration": acQoSConfiguration,
       "acQoSMatchMapTable": acQoSMatchMapTable,
       "acQoSMatchMapEntry": acQoSMatchMapEntry,
       "acQoSMatchMapIndex": acQoSMatchMapIndex,
       "acQoSMatchMapName": acQoSMatchMapName,
       "acQoSMatchMapDirection": acQoSMatchMapDirection,
       "acQoSMatchMapInterface": acQoSMatchMapInterface,
       "acQoSMatchTable": acQoSMatchTable,
       "acQoSMatchEntry": acQoSMatchEntry,
       "acQoSMatchMatchMapIndex": acQoSMatchMatchMapIndex,
       "acQoSMatchIndex": acQoSMatchIndex,
       "acQoSMatchType": acQoSMatchType,
       "acQoSMatchAccessMap": acQoSMatchAccessMap,
       "acQoSMatchDscpValue": acQoSMatchDscpValue,
       "acQoSMatchMinLength": acQoSMatchMinLength,
       "acQoSMatchMaxLength": acQoSMatchMaxLength,
       "acQoSMatchPrecedenceValue": acQoSMatchPrecedenceValue,
       "acQoSMatchPriorityValue": acQoSMatchPriorityValue,
       "acQoSSetTable": acQoSSetTable,
       "acQoSSetEntry": acQoSSetEntry,
       "acQoSSetMatchMapIndex": acQoSSetMatchMapIndex,
       "acQoSSetIndex": acQoSSetIndex,
       "acQoSSetType": acQoSSetType,
       "acQoSSetQueueName": acQoSSetQueueName,
       "acQoSSetDscpValue": acQoSSetDscpValue,
       "acQoSSetPrecedenceValue": acQoSSetPrecedenceValue,
       "acQoSSetPriorityValue": acQoSSetPriorityValue,
       "acQoSServiceMapTable": acQoSServiceMapTable,
       "acQoSServiceMapEntry": acQoSServiceMapEntry,
       "acQoSServiceMapIndex": acQoSServiceMapIndex,
       "acQoSServiceMapInterface": acQoSServiceMapInterface,
       "acQoSServiceMapDirection": acQoSServiceMapDirection,
       "acQoSServiceMapBandwidthLimit": acQoSServiceMapBandwidthLimit,
       "acQoSServiceMapMaxBandwidth": acQoSServiceMapMaxBandwidth,
       "acQoSQueueTable": acQoSQueueTable,
       "acQoSQueueEntry": acQoSQueueEntry,
       "acQoSQueueServiceMapIndex": acQoSQueueServiceMapIndex,
       "acQoSQueueIndex": acQoSQueueIndex,
       "acQoSQueueName": acQoSQueueName,
       "acQoSQueueActionTable": acQoSQueueActionTable,
       "acQoSQueueActionEntry": acQoSQueueActionEntry,
       "acQoSQueueActionServiceMapIndex": acQoSQueueActionServiceMapIndex,
       "acQoSQueueActionQueueIndex": acQoSQueueActionQueueIndex,
       "acQoSQueueActionIndex": acQoSQueueActionIndex,
       "acQoSQueueActionType": acQoSQueueActionType,
       "acQoSQueueActionMinBandwidth": acQoSQueueActionMinBandwidth,
       "acQoSQueueActionMaxBandwidth": acQoSQueueActionMaxBandwidth,
       "acQoSQueueActionPolicyValue": acQoSQueueActionPolicyValue,
       "acQoSQueueActionPriorityValue": acQoSQueueActionPriorityValue,
       "acQoSStatus": acQoSStatus,
       "acQoSQueueStatsTable": acQoSQueueStatsTable,
       "acQoSQueueStatsEntry": acQoSQueueStatsEntry,
       "acQoSQueueStatsServiceMapIndex": acQoSQueueStatsServiceMapIndex,
       "acQoSQueueStatsQueueIndex": acQoSQueueStatsQueueIndex,
       "acQoSQueueStatsPacketSent": acQoSQueueStatsPacketSent,
       "acQoSQueueStatsBytesSent": acQoSQueueStatsBytesSent,
       "acQoSQueueStatsPacketsRate": acQoSQueueStatsPacketsRate,
       "acQoSQueueStatsBytesRate": acQoSQueueStatsBytesRate,
       "acQoSQueueStatsPacketsDelayed": acQoSQueueStatsPacketsDelayed,
       "acQoSQueueStatsPacketsDropped": acQoSQueueStatsPacketsDropped}
)
