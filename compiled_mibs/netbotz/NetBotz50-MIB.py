# SNMP MIB module (NetBotz50-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\netbotz\NetBotz50-MIB

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

netBotz5_APC = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 52674, 500, 1)
)
if mibBuilder.loadTexts:
    netBotz5_APC.setRevisions(
        ("2018-10-17 00:00",
         "2019-01-24 00:00",
         "2019-07-17 00:00",
         "2020-01-31 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class OperStatus(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disconnected", 0),
          ("error", 1),
          ("normal", 2))
    )



class ErrorStatus(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("normal", 0),
          ("info", 1),
          ("warning", 2),
          ("error", 3),
          ("critical", 4),
          ("failure", 5))
    )



class BoolValue(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("yes", 1),
          ("null", 2))
    )



# MIB Managed Objects in the order of their OIDs

_NetBotzAPC_ObjectIdentity = ObjectIdentity
netBotzAPC = _NetBotzAPC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52674)
)
_NetBotz5_ObjectIdentity = ObjectIdentity
netBotz5 = _NetBotz5_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52674, 500)
)
_NetBotzEnclosures_ObjectIdentity = ObjectIdentity
netBotzEnclosures = _NetBotzEnclosures_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52674, 500, 2)
)
_EnclosureTable_Object = MibTable
enclosureTable = _EnclosureTable_Object(
    (1, 3, 6, 1, 4, 1, 52674, 500, 2, 1)
)
if mibBuilder.loadTexts:
    enclosureTable.setStatus("current")
_EnclosureEntry_Object = MibTableRow
enclosureEntry = _EnclosureEntry_Object(
    (1, 3, 6, 1, 4, 1, 52674, 500, 2, 1, 1)
)
enclosureEntry.setIndexNames(
    (0, "NetBotz50-MIB", "enclosureIndex"),
)
if mibBuilder.loadTexts:
    enclosureEntry.setStatus("current")


class _EnclosureId_Type(DisplayString):
    """Custom type enclosureId based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_EnclosureId_Type.__name__ = "DisplayString"
_EnclosureId_Object = MibTableColumn
enclosureId = _EnclosureId_Object(
    (1, 3, 6, 1, 4, 1, 52674, 500, 2, 1, 1, 1),
    _EnclosureId_Type()
)
enclosureId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enclosureId.setStatus("current")
_EnclosureStatus_Type = OperStatus
_EnclosureStatus_Object = MibTableColumn
enclosureStatus = _EnclosureStatus_Object(
    (1, 3, 6, 1, 4, 1, 52674, 500, 2, 1, 1, 2),
    _EnclosureStatus_Type()
)
enclosureStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enclosureStatus.setStatus("current")
_EnclosureErrorStatus_Type = ErrorStatus
_EnclosureErrorStatus_Object = MibTableColumn
enclosureErrorStatus = _EnclosureErrorStatus_Object(
    (1, 3, 6, 1, 4, 1, 52674, 500, 2, 1, 1, 3),
    _EnclosureErrorStatus_Type()
)
enclosureErrorStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enclosureErrorStatus.setStatus("current")
_EnclosureLabel_Type = DisplayString
_EnclosureLabel_Object = MibTableColumn
enclosureLabel = _EnclosureLabel_Object(
    (1, 3, 6, 1, 4, 1, 52674, 500, 2, 1, 1, 4),
    _EnclosureLabel_Type()
)
enclosureLabel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enclosureLabel.setStatus("current")


class _EnclosureParentEncId_Type(DisplayString):
    """Custom type enclosureParentEncId based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_EnclosureParentEncId_Type.__name__ = "DisplayString"
_EnclosureParentEncId_Object = MibTableColumn
enclosureParentEncId = _EnclosureParentEncId_Object(
    (1, 3, 6, 1, 4, 1, 52674, 500, 2, 1, 1, 5),
    _EnclosureParentEncId_Type()
)
enclosureParentEncId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enclosureParentEncId.setStatus("current")


class _EnclosureSerialNumber_Type(DisplayString):
    """Custom type enclosureSerialNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_EnclosureSerialNumber_Type.__name__ = "DisplayString"
_EnclosureSerialNumber_Object = MibTableColumn
enclosureSerialNumber = _EnclosureSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 52674, 500, 2, 1, 1, 6),
    _EnclosureSerialNumber_Type()
)
enclosureSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enclosureSerialNumber.setStatus("current")
_EnclosureIndex_Type = Counter32
_EnclosureIndex_Object = MibTableColumn
enclosureIndex = _EnclosureIndex_Object(
    (1, 3, 6, 1, 4, 1, 52674, 500, 2, 1, 1, 7),
    _EnclosureIndex_Type()
)
enclosureIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enclosureIndex.setStatus("current")
_NetBotzSensorCounts_ObjectIdentity = ObjectIdentity
netBotzSensorCounts = _NetBotzSensorCounts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52674, 500, 2, 2)
)
_AlinkSensorCountTable_Object = MibTable
alinkSensorCountTable = _AlinkSensorCountTable_Object(
    (1, 3, 6, 1, 4, 1, 52674, 500, 2, 2, 1)
)
if mibBuilder.loadTexts:
    alinkSensorCountTable.setStatus("current")
_AlinkSensorCountEntry_Object = MibTableRow
alinkSensorCountEntry = _AlinkSensorCountEntry_Object(
    (1, 3, 6, 1, 4, 1, 52674, 500, 2, 2, 1, 1)
)
alinkSensorCountEntry.setIndexNames(
    (0, "NetBotz50-MIB", "alinkSensorCountIndex"),
)
if mibBuilder.loadTexts:
    alinkSensorCountEntry.setStatus("current")


class _AlinkSensorCountId_Type(DisplayString):
    """Custom type alinkSensorCountId based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_AlinkSensorCountId_Type.__name__ = "DisplayString"
_AlinkSensorCountId_Object = MibTableColumn
alinkSensorCountId = _AlinkSensorCountId_Object(
    (1, 3, 6, 1, 4, 1, 52674, 500, 2, 2, 1, 1, 1),
    _AlinkSensorCountId_Type()
)
alinkSensorCountId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alinkSensorCountId.setStatus("current")


class _AlinkSensorCountValue_Type(Integer32):
    """Custom type alinkSensorCountValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AlinkSensorCountValue_Type.__name__ = "Integer32"
_AlinkSensorCountValue_Object = MibTableColumn
alinkSensorCountValue = _AlinkSensorCountValue_Object(
    (1, 3, 6, 1, 4, 1, 52674, 500, 2, 2, 1, 1, 2),
    _AlinkSensorCountValue_Type()
)
alinkSensorCountValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alinkSensorCountValue.setStatus("current")
_AlinkSensorCountLabel_Type = DisplayString
_AlinkSensorCountLabel_Object = MibTableColumn
alinkSensorCountLabel = _AlinkSensorCountLabel_Object(
    (1, 3, 6, 1, 4, 1, 52674, 500, 2, 2, 1, 1, 3),
    _AlinkSensorCountLabel_Type()
)
alinkSensorCountLabel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alinkSensorCountLabel.setStatus("current")


class _AlinkSensorCountEncId_Type(DisplayString):
    """Custom type alinkSensorCountEncId based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_AlinkSensorCountEncId_Type.__name__ = "DisplayString"
_AlinkSensorCountEncId_Object = MibTableColumn
alinkSensorCountEncId = _AlinkSensorCountEncId_Object(
    (1, 3, 6, 1, 4, 1, 52674, 500, 2, 2, 1, 1, 4),
    _AlinkSensorCountEncId_Type()
)
alinkSensorCountEncId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alinkSensorCountEncId.setStatus("current")
_AlinkSensorCountValueStr_Type = DisplayString
_AlinkSensorCountValueStr_Object = MibTableColumn
alinkSensorCountValueStr = _AlinkSensorCountValueStr_Object(
    (1, 3, 6, 1, 4, 1, 52674, 500, 2, 2, 1, 1, 5),
    _AlinkSensorCountValueStr_Type()
)
alinkSensorCountValueStr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alinkSensorCountValueStr.setStatus("current")


class _AlinkSensorCountValueInt_Type(Integer32):
    """Custom type alinkSensorCountValueInt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 6554),
    )


_AlinkSensorCountValueInt_Type.__name__ = "Integer32"
_AlinkSensorCountValueInt_Object = MibTableColumn
alinkSensorCountValueInt = _AlinkSensorCountValueInt_Object(
    (1, 3, 6, 1, 4, 1, 52674, 500, 2, 2, 1, 1, 6),
    _AlinkSensorCountValueInt_Type()
)
alinkSensorCountValueInt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alinkSensorCountValueInt.setStatus("current")
_AlinkSensorCountIndex_Type = Counter32
_AlinkSensorCountIndex_Object = MibTableColumn
alinkSensorCountIndex = _AlinkSensorCountIndex_Object(
    (1, 3, 6, 1, 4, 1, 52674, 500, 2, 2, 1, 1, 7),
    _AlinkSensorCountIndex_Type()
)
alinkSensorCountIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alinkSensorCountIndex.setStatus("current")
_NetBotzPorts_ObjectIdentity = ObjectIdentity
netBotzPorts = _NetBotzPorts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52674, 500, 3)
)
_OtherPortTable_Object = MibTable
otherPortTable = _OtherPortTable_Object(
    (1, 3, 6, 1, 4, 1, 52674, 500, 3, 10)
)
if mibBuilder.loadTexts:
    otherPortTable.setStatus("current")
_OtherPortEntry_Object = MibTableRow
otherPortEntry = _OtherPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 52674, 500, 3, 10, 1)
)
otherPortEntry.setIndexNames(
    (0, "NetBotz50-MIB", "otherPortIndex"),
)
if mibBuilder.loadTexts:
    otherPortEntry.setStatus("current")


class _OtherPortId_Type(DisplayString):
    """Custom type otherPortId based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_OtherPortId_Type.__name__ = "DisplayString"
_OtherPortId_Object = MibTableColumn
otherPortId = _OtherPortId_Object(
    (1, 3, 6, 1, 4, 1, 52674, 500, 3, 10, 1, 1),
    _OtherPortId_Type()
)
otherPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otherPortId.setStatus("current")
_OtherPortStatus_Type = OperStatus
_OtherPortStatus_Object = MibTableColumn
otherPortStatus = _OtherPortStatus_Object(
    (1, 3, 6, 1, 4, 1, 52674, 500, 3, 10, 1, 2),
    _OtherPortStatus_Type()
)
otherPortStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otherPortStatus.setStatus("current")
_OtherPortLabel_Type = DisplayString
_OtherPortLabel_Object = MibTableColumn
otherPortLabel = _OtherPortLabel_Object(
    (1, 3, 6, 1, 4, 1, 52674, 500, 3, 10, 1, 3),
    _OtherPortLabel_Type()
)
otherPortLabel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otherPortLabel.setStatus("current")


class _OtherPortEncId_Type(DisplayString):
    """Custom type otherPortEncId based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_OtherPortEncId_Type.__name__ = "DisplayString"
_OtherPortEncId_Object = MibTableColumn
otherPortEncId = _OtherPortEncId_Object(
    (1, 3, 6, 1, 4, 1, 52674, 500, 3, 10, 1, 4),
    _OtherPortEncId_Type()
)
otherPortEncId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otherPortEncId.setStatus("current")
_OtherPortIndex_Type = Counter32
_OtherPortIndex_Object = MibTableColumn
otherPortIndex = _OtherPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 52674, 500, 3, 10, 1, 5),
    _OtherPortIndex_Type()
)
otherPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otherPortIndex.setStatus("current")
_NetBotzSensors_ObjectIdentity = ObjectIdentity
netBotzSensors = _NetBotzSensors_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52674, 500, 4)
)
_NetBotzNumericSensors_ObjectIdentity = ObjectIdentity
netBotzNumericSensors = _NetBotzNumericSensors_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52674, 500, 4, 1)
)
_TempSensorTable_Object = MibTable
tempSensorTable = _TempSensorTable_Object(
    (1, 3, 6, 1, 4, 1, 52674, 500, 4, 1, 1)
)
if mibBuilder.loadTexts:
    tempSensorTable.setStatus("current")
_TempSensorEntry_Object = MibTableRow
tempSensorEntry = _TempSensorEntry_Object(
    (1, 3, 6, 1, 4, 1, 52674, 500, 4, 1, 1, 1)
)
tempSensorEntry.setIndexNames(
    (0, "NetBotz50-MIB", "tempSensorIndex"),
)
if mibBuilder.loadTexts:
    tempSensorEntry.setStatus("current")


class _TempSensorId_Type(DisplayString):
    """Custom type tempSensorId based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_TempSensorId_Type.__name__ = "DisplayString"
_TempSensorId_Object = MibTableColumn
tempSensorId = _TempSensorId_Object(
    (1, 3, 6, 1, 4, 1, 52674, 500, 4, 1, 1, 1, 1),
    _TempSensorId_Type()
)
tempSensorId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tempSensorId.setStatus("current")


class _TempSensorValue_Type(Integer32):
    """Custom type tempSensorValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-500, 1000),
    )


_TempSensorValue_Type.__name__ = "Integer32"
_TempSensorValue_Object = MibTableColumn
tempSensorValue = _TempSensorValue_Object(
    (1, 3, 6, 1, 4, 1, 52674, 500, 4, 1, 1, 1, 2),
    _TempSensorValue_Type()
)
tempSensorValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tempSensorValue.setStatus("current")
_TempSensorErrorStatus_Type = ErrorStatus
_TempSensorErrorStatus_Object = MibTableColumn
tempSensorErrorStatus = _TempSensorErrorStatus_Object(
    (1, 3, 6, 1, 4, 1, 52674, 500, 4, 1, 1, 1, 3),
    _TempSensorErrorStatus_Type()
)
tempSensorErrorStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tempSensorErrorStatus.setStatus("current")
_TempSensorLabel_Type = DisplayString
_TempSensorLabel_Object = MibTableColumn
tempSensorLabel = _TempSensorLabel_Object(
    (1, 3, 6, 1, 4, 1, 52674, 500, 4, 1, 1, 1, 4),
    _TempSensorLabel_Type()
)
tempSensorLabel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tempSensorLabel.setStatus("current")


class _TempSensorEncId_Type(DisplayString):
    """Custom type tempSensorEncId based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_TempSensorEncId_Type.__name__ = "DisplayString"
_TempSensorEncId_Object = MibTableColumn
tempSensorEncId = _TempSensorEncId_Object(
    (1, 3, 6, 1, 4, 1, 52674, 500, 4, 1, 1, 1, 5),
    _TempSensorEncId_Type()
)
tempSensorEncId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tempSensorEncId.setStatus("current")


class _TempSensorPortId_Type(DisplayString):
    """Custom type tempSensorPortId based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_TempSensorPortId_Type.__name__ = "DisplayString"
_TempSensorPortId_Object = MibTableColumn
tempSensorPortId = _TempSensorPortId_Object(
    (1, 3, 6, 1, 4, 1, 52674, 500, 4, 1, 1, 1, 6),
    _TempSensorPortId_Type()
)
tempSensorPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tempSensorPortId.setStatus("current")
_TempSensorValueStr_Type = DisplayString
_TempSensorValueStr_Object = MibTableColumn
tempSensorValueStr = _TempSensorValueStr_Object(
    (1, 3, 6, 1, 4, 1, 52674, 500, 4, 1, 1, 1, 7),
    _TempSensorValueStr_Type()
)
tempSensorValueStr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tempSensorValueStr.setStatus("current")


class _TempSensorValueInt_Type(Integer32):
    """Custom type tempSensorValueInt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-50, 100),
    )


_TempSensorValueInt_Type.__name__ = "Integer32"
_TempSensorValueInt_Object = MibTableColumn
tempSensorValueInt = _TempSensorValueInt_Object(
    (1, 3, 6, 1, 4, 1, 52674, 500, 4, 1, 1, 1, 8),
    _TempSensorValueInt_Type()
)
tempSensorValueInt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tempSensorValueInt.setStatus("current")


class _TempSensorValueIntF_Type(Integer32):
    """Custom type tempSensorValueIntF based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-50, 212),
    )


_TempSensorValueIntF_Type.__name__ = "Integer32"
_TempSensorValueIntF_Object = MibTableColumn
tempSensorValueIntF = _TempSensorValueIntF_Object(
    (1, 3, 6, 1, 4, 1, 52674, 500, 4, 1, 1, 1, 9),
    _TempSensorValueIntF_Type()
)
tempSensorValueIntF.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tempSensorValueIntF.setStatus("current")
_TempSensorIndex_Type = Counter32
_TempSensorIndex_Object = MibTableColumn
tempSensorIndex = _TempSensorIndex_Object(
    (1, 3, 6, 1, 4, 1, 52674, 500, 4, 1, 1, 1, 10),
    _TempSensorIndex_Type()
)
tempSensorIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tempSensorIndex.setStatus("current")
_HumiSensorTable_Object = MibTable
humiSensorTable = _HumiSensorTable_Object(
    (1, 3, 6, 1, 4, 1, 52674, 500, 4, 1, 2)
)
if mibBuilder.loadTexts:
    humiSensorTable.setStatus("current")
_HumiSensorEntry_Object = MibTableRow
humiSensorEntry = _HumiSensorEntry_Object(
    (1, 3, 6, 1, 4, 1, 52674, 500, 4, 1, 2, 1)
)
humiSensorEntry.setIndexNames(
    (0, "NetBotz50-MIB", "humiSensorIndex"),
)
if mibBuilder.loadTexts:
    humiSensorEntry.setStatus("current")


class _HumiSensorId_Type(DisplayString):
    """Custom type humiSensorId based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_HumiSensorId_Type.__name__ = "DisplayString"
_HumiSensorId_Object = MibTableColumn
humiSensorId = _HumiSensorId_Object(
    (1, 3, 6, 1, 4, 1, 52674, 500, 4, 1, 2, 1, 1),
    _HumiSensorId_Type()
)
humiSensorId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    humiSensorId.setStatus("current")


class _HumiSensorValue_Type(Integer32):
    """Custom type humiSensorValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_HumiSensorValue_Type.__name__ = "Integer32"
_HumiSensorValue_Object = MibTableColumn
humiSensorValue = _HumiSensorValue_Object(
    (1, 3, 6, 1, 4, 1, 52674, 500, 4, 1, 2, 1, 2),
    _HumiSensorValue_Type()
)
humiSensorValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    humiSensorValue.setStatus("current")
_HumiSensorErrorStatus_Type = ErrorStatus
_HumiSensorErrorStatus_Object = MibTableColumn
humiSensorErrorStatus = _HumiSensorErrorStatus_Object(
    (1, 3, 6, 1, 4, 1, 52674, 500, 4, 1, 2, 1, 3),
    _HumiSensorErrorStatus_Type()
)
humiSensorErrorStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    humiSensorErrorStatus.setStatus("current")
_HumiSensorLabel_Type = DisplayString
_HumiSensorLabel_Object = MibTableColumn
humiSensorLabel = _HumiSensorLabel_Object(
    (1, 3, 6, 1, 4, 1, 52674, 500, 4, 1, 2, 1, 4),
    _HumiSensorLabel_Type()
)
humiSensorLabel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    humiSensorLabel.setStatus("current")


class _HumiSensorEncId_Type(DisplayString):
    """Custom type humiSensorEncId based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_HumiSensorEncId_Type.__name__ = "DisplayString"
_HumiSensorEncId_Object = MibTableColumn
humiSensorEncId = _HumiSensorEncId_Object(
    (1, 3, 6, 1, 4, 1, 52674, 500, 4, 1, 2, 1, 5),
    _HumiSensorEncId_Type()
)
humiSensorEncId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    humiSensorEncId.setStatus("current")


class _HumiSensorPortId_Type(DisplayString):
    """Custom type humiSensorPortId based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_HumiSensorPortId_Type.__name__ = "DisplayString"
_HumiSensorPortId_Object = MibTableColumn
humiSensorPortId = _HumiSensorPortId_Object(
    (1, 3, 6, 1, 4, 1, 52674, 500, 4, 1, 2, 1, 6),
    _HumiSensorPortId_Type()
)
humiSensorPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    humiSensorPortId.setStatus("current")
_HumiSensorValueStr_Type = DisplayString
_HumiSensorValueStr_Object = MibTableColumn
humiSensorValueStr = _HumiSensorValueStr_Object(
    (1, 3, 6, 1, 4, 1, 52674, 500, 4, 1, 2, 1, 7),
    _HumiSensorValueStr_Type()
)
humiSensorValueStr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    humiSensorValueStr.setStatus("current")


class _HumiSensorValueInt_Type(Integer32):
    """Custom type humiSensorValueInt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_HumiSensorValueInt_Type.__name__ = "Integer32"
_HumiSensorValueInt_Object = MibTableColumn
humiSensorValueInt = _HumiSensorValueInt_Object(
    (1, 3, 6, 1, 4, 1, 52674, 500, 4, 1, 2, 1, 8),
    _HumiSensorValueInt_Type()
)
humiSensorValueInt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    humiSensorValueInt.setStatus("current")
_HumiSensorIndex_Type = Counter32
_HumiSensorIndex_Object = MibTableColumn
humiSensorIndex = _HumiSensorIndex_Object(
    (1, 3, 6, 1, 4, 1, 52674, 500, 4, 1, 2, 1, 9),
    _HumiSensorIndex_Type()
)
humiSensorIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    humiSensorIndex.setStatus("current")
_DewPointSensorTable_Object = MibTable
dewPointSensorTable = _DewPointSensorTable_Object(
    (1, 3, 6, 1, 4, 1, 52674, 500, 4, 1, 3)
)
if mibBuilder.loadTexts:
    dewPointSensorTable.setStatus("current")
_DewPointSensorEntry_Object = MibTableRow
dewPointSensorEntry = _DewPointSensorEntry_Object(
    (1, 3, 6, 1, 4, 1, 52674, 500, 4, 1, 3, 1)
)
dewPointSensorEntry.setIndexNames(
    (0, "NetBotz50-MIB", "dewPointSensorIndex"),
)
if mibBuilder.loadTexts:
    dewPointSensorEntry.setStatus("current")


class _DewPointSensorId_Type(DisplayString):
    """Custom type dewPointSensorId based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_DewPointSensorId_Type.__name__ = "DisplayString"
_DewPointSensorId_Object = MibTableColumn
dewPointSensorId = _DewPointSensorId_Object(
    (1, 3, 6, 1, 4, 1, 52674, 500, 4, 1, 3, 1, 1),
    _DewPointSensorId_Type()
)
dewPointSensorId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dewPointSensorId.setStatus("current")


class _DewPointSensorValue_Type(Integer32):
    """Custom type dewPointSensorValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-500, 1000),
    )


_DewPointSensorValue_Type.__name__ = "Integer32"
_DewPointSensorValue_Object = MibTableColumn
dewPointSensorValue = _DewPointSensorValue_Object(
    (1, 3, 6, 1, 4, 1, 52674, 500, 4, 1, 3, 1, 2),
    _DewPointSensorValue_Type()
)
dewPointSensorValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dewPointSensorValue.setStatus("current")
_DewPointSensorErrorStatus_Type = ErrorStatus
_DewPointSensorErrorStatus_Object = MibTableColumn
dewPointSensorErrorStatus = _DewPointSensorErrorStatus_Object(
    (1, 3, 6, 1, 4, 1, 52674, 500, 4, 1, 3, 1, 3),
    _DewPointSensorErrorStatus_Type()
)
dewPointSensorErrorStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dewPointSensorErrorStatus.setStatus("current")
_DewPointSensorLabel_Type = DisplayString
_DewPointSensorLabel_Object = MibTableColumn
dewPointSensorLabel = _DewPointSensorLabel_Object(
    (1, 3, 6, 1, 4, 1, 52674, 500, 4, 1, 3, 1, 4),
    _DewPointSensorLabel_Type()
)
dewPointSensorLabel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dewPointSensorLabel.setStatus("current")


class _DewPointSensorEncId_Type(DisplayString):
    """Custom type dewPointSensorEncId based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_DewPointSensorEncId_Type.__name__ = "DisplayString"
_DewPointSensorEncId_Object = MibTableColumn
dewPointSensorEncId = _DewPointSensorEncId_Object(
    (1, 3, 6, 1, 4, 1, 52674, 500, 4, 1, 3, 1, 5),
    _DewPointSensorEncId_Type()
)
dewPointSensorEncId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dewPointSensorEncId.setStatus("current")


class _DewPointSensorPortId_Type(DisplayString):
    """Custom type dewPointSensorPortId based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_DewPointSensorPortId_Type.__name__ = "DisplayString"
_DewPointSensorPortId_Object = MibTableColumn
dewPointSensorPortId = _DewPointSensorPortId_Object(
    (1, 3, 6, 1, 4, 1, 52674, 500, 4, 1, 3, 1, 6),
    _DewPointSensorPortId_Type()
)
dewPointSensorPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dewPointSensorPortId.setStatus("current")
_DewPointSensorValueStr_Type = DisplayString
_DewPointSensorValueStr_Object = MibTableColumn
dewPointSensorValueStr = _DewPointSensorValueStr_Object(
    (1, 3, 6, 1, 4, 1, 52674, 500, 4, 1, 3, 1, 7),
    _DewPointSensorValueStr_Type()
)
dewPointSensorValueStr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dewPointSensorValueStr.setStatus("current")


class _DewPointSensorValueInt_Type(Integer32):
    """Custom type dewPointSensorValueInt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-50, 100),
    )


_DewPointSensorValueInt_Type.__name__ = "Integer32"
_DewPointSensorValueInt_Object = MibTableColumn
dewPointSensorValueInt = _DewPointSensorValueInt_Object(
    (1, 3, 6, 1, 4, 1, 52674, 500, 4, 1, 3, 1, 8),
    _DewPointSensorValueInt_Type()
)
dewPointSensorValueInt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dewPointSensorValueInt.setStatus("current")


class _DewPointSensorValueIntF_Type(Integer32):
    """Custom type dewPointSensorValueIntF based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-40, 122),
    )


_DewPointSensorValueIntF_Type.__name__ = "Integer32"
_DewPointSensorValueIntF_Object = MibTableColumn
dewPointSensorValueIntF = _DewPointSensorValueIntF_Object(
    (1, 3, 6, 1, 4, 1, 52674, 500, 4, 1, 3, 1, 9),
    _DewPointSensorValueIntF_Type()
)
dewPointSensorValueIntF.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dewPointSensorValueIntF.setStatus("current")
_DewPointSensorIndex_Type = Counter32
_DewPointSensorIndex_Object = MibTableColumn
dewPointSensorIndex = _DewPointSensorIndex_Object(
    (1, 3, 6, 1, 4, 1, 52674, 500, 4, 1, 3, 1, 10),
    _DewPointSensorIndex_Type()
)
dewPointSensorIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dewPointSensorIndex.setStatus("current")
_AirFlowSensorTable_Object = MibTable
airFlowSensorTable = _AirFlowSensorTable_Object(
    (1, 3, 6, 1, 4, 1, 52674, 500, 4, 1, 5)
)
if mibBuilder.loadTexts:
    airFlowSensorTable.setStatus("current")
_AirFlowSensorEntry_Object = MibTableRow
airFlowSensorEntry = _AirFlowSensorEntry_Object(
    (1, 3, 6, 1, 4, 1, 52674, 500, 4, 1, 5, 1)
)
airFlowSensorEntry.setIndexNames(
    (0, "NetBotz50-MIB", "airFlowSensorIndex"),
)
if mibBuilder.loadTexts:
    airFlowSensorEntry.setStatus("current")


class _AirFlowSensorId_Type(DisplayString):
    """Custom type airFlowSensorId based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_AirFlowSensorId_Type.__name__ = "DisplayString"
_AirFlowSensorId_Object = MibTableColumn
airFlowSensorId = _AirFlowSensorId_Object(
    (1, 3, 6, 1, 4, 1, 52674, 500, 4, 1, 5, 1, 1),
    _AirFlowSensorId_Type()
)
airFlowSensorId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    airFlowSensorId.setStatus("current")


class _AirFlowSensorValue_Type(Integer32):
    """Custom type airFlowSensorValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000),
    )


_AirFlowSensorValue_Type.__name__ = "Integer32"
_AirFlowSensorValue_Object = MibTableColumn
airFlowSensorValue = _AirFlowSensorValue_Object(
    (1, 3, 6, 1, 4, 1, 52674, 500, 4, 1, 5, 1, 2),
    _AirFlowSensorValue_Type()
)
airFlowSensorValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    airFlowSensorValue.setStatus("current")
_AirFlowSensorErrorStatus_Type = ErrorStatus
_AirFlowSensorErrorStatus_Object = MibTableColumn
airFlowSensorErrorStatus = _AirFlowSensorErrorStatus_Object(
    (1, 3, 6, 1, 4, 1, 52674, 500, 4, 1, 5, 1, 3),
    _AirFlowSensorErrorStatus_Type()
)
airFlowSensorErrorStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    airFlowSensorErrorStatus.setStatus("current")
_AirFlowSensorLabel_Type = DisplayString
_AirFlowSensorLabel_Object = MibTableColumn
airFlowSensorLabel = _AirFlowSensorLabel_Object(
    (1, 3, 6, 1, 4, 1, 52674, 500, 4, 1, 5, 1, 4),
    _AirFlowSensorLabel_Type()
)
airFlowSensorLabel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    airFlowSensorLabel.setStatus("current")


class _AirFlowSensorEncId_Type(DisplayString):
    """Custom type airFlowSensorEncId based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_AirFlowSensorEncId_Type.__name__ = "DisplayString"
_AirFlowSensorEncId_Object = MibTableColumn
airFlowSensorEncId = _AirFlowSensorEncId_Object(
    (1, 3, 6, 1, 4, 1, 52674, 500, 4, 1, 5, 1, 5),
    _AirFlowSensorEncId_Type()
)
airFlowSensorEncId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    airFlowSensorEncId.setStatus("current")


class _AirFlowSensorPortId_Type(DisplayString):
    """Custom type airFlowSensorPortId based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_AirFlowSensorPortId_Type.__name__ = "DisplayString"
_AirFlowSensorPortId_Object = MibTableColumn
airFlowSensorPortId = _AirFlowSensorPortId_Object(
    (1, 3, 6, 1, 4, 1, 52674, 500, 4, 1, 5, 1, 6),
    _AirFlowSensorPortId_Type()
)
airFlowSensorPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    airFlowSensorPortId.setStatus("current")
_AirFlowSensorValueStr_Type = DisplayString
_AirFlowSensorValueStr_Object = MibTableColumn
airFlowSensorValueStr = _AirFlowSensorValueStr_Object(
    (1, 3, 6, 1, 4, 1, 52674, 500, 4, 1, 5, 1, 7),
    _AirFlowSensorValueStr_Type()
)
airFlowSensorValueStr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    airFlowSensorValueStr.setStatus("current")


class _AirFlowSensorValueInt_Type(Integer32):
    """Custom type airFlowSensorValueInt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_AirFlowSensorValueInt_Type.__name__ = "Integer32"
_AirFlowSensorValueInt_Object = MibTableColumn
airFlowSensorValueInt = _AirFlowSensorValueInt_Object(
    (1, 3, 6, 1, 4, 1, 52674, 500, 4, 1, 5, 1, 8),
    _AirFlowSensorValueInt_Type()
)
airFlowSensorValueInt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    airFlowSensorValueInt.setStatus("current")
_AirFlowSensorIndex_Type = Counter32
_AirFlowSensorIndex_Object = MibTableColumn
airFlowSensorIndex = _AirFlowSensorIndex_Object(
    (1, 3, 6, 1, 4, 1, 52674, 500, 4, 1, 5, 1, 9),
    _AirFlowSensorIndex_Type()
)
airFlowSensorIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    airFlowSensorIndex.setStatus("current")
_AmpDetectSensorTable_Object = MibTable
ampDetectSensorTable = _AmpDetectSensorTable_Object(
    (1, 3, 6, 1, 4, 1, 52674, 500, 4, 1, 6)
)
if mibBuilder.loadTexts:
    ampDetectSensorTable.setStatus("current")
_AmpDetectSensorEntry_Object = MibTableRow
ampDetectSensorEntry = _AmpDetectSensorEntry_Object(
    (1, 3, 6, 1, 4, 1, 52674, 500, 4, 1, 6, 1)
)
ampDetectSensorEntry.setIndexNames(
    (0, "NetBotz50-MIB", "ampDetectSensorIndex"),
)
if mibBuilder.loadTexts:
    ampDetectSensorEntry.setStatus("current")


class _AmpDetectSensorId_Type(DisplayString):
    """Custom type ampDetectSensorId based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_AmpDetectSensorId_Type.__name__ = "DisplayString"
_AmpDetectSensorId_Object = MibTableColumn
ampDetectSensorId = _AmpDetectSensorId_Object(
    (1, 3, 6, 1, 4, 1, 52674, 500, 4, 1, 6, 1, 1),
    _AmpDetectSensorId_Type()
)
ampDetectSensorId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ampDetectSensorId.setStatus("current")


class _AmpDetectSensorValue_Type(Integer32):
    """Custom type ampDetectSensorValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AmpDetectSensorValue_Type.__name__ = "Integer32"
_AmpDetectSensorValue_Object = MibTableColumn
ampDetectSensorValue = _AmpDetectSensorValue_Object(
    (1, 3, 6, 1, 4, 1, 52674, 500, 4, 1, 6, 1, 2),
    _AmpDetectSensorValue_Type()
)
ampDetectSensorValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ampDetectSensorValue.setStatus("current")
_AmpDetectSensorErrorStatus_Type = ErrorStatus
_AmpDetectSensorErrorStatus_Object = MibTableColumn
ampDetectSensorErrorStatus = _AmpDetectSensorErrorStatus_Object(
    (1, 3, 6, 1, 4, 1, 52674, 500, 4, 1, 6, 1, 3),
    _AmpDetectSensorErrorStatus_Type()
)
ampDetectSensorErrorStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ampDetectSensorErrorStatus.setStatus("current")
_AmpDetectSensorLabel_Type = DisplayString
_AmpDetectSensorLabel_Object = MibTableColumn
ampDetectSensorLabel = _AmpDetectSensorLabel_Object(
    (1, 3, 6, 1, 4, 1, 52674, 500, 4, 1, 6, 1, 4),
    _AmpDetectSensorLabel_Type()
)
ampDetectSensorLabel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ampDetectSensorLabel.setStatus("current")


class _AmpDetectSensorEncId_Type(DisplayString):
    """Custom type ampDetectSensorEncId based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_AmpDetectSensorEncId_Type.__name__ = "DisplayString"
_AmpDetectSensorEncId_Object = MibTableColumn
ampDetectSensorEncId = _AmpDetectSensorEncId_Object(
    (1, 3, 6, 1, 4, 1, 52674, 500, 4, 1, 6, 1, 5),
    _AmpDetectSensorEncId_Type()
)
ampDetectSensorEncId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ampDetectSensorEncId.setStatus("current")


class _AmpDetectSensorPortId_Type(DisplayString):
    """Custom type ampDetectSensorPortId based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_AmpDetectSensorPortId_Type.__name__ = "DisplayString"
_AmpDetectSensorPortId_Object = MibTableColumn
ampDetectSensorPortId = _AmpDetectSensorPortId_Object(
    (1, 3, 6, 1, 4, 1, 52674, 500, 4, 1, 6, 1, 6),
    _AmpDetectSensorPortId_Type()
)
ampDetectSensorPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ampDetectSensorPortId.setStatus("current")
_AmpDetectSensorValueStr_Type = DisplayString
_AmpDetectSensorValueStr_Object = MibTableColumn
ampDetectSensorValueStr = _AmpDetectSensorValueStr_Object(
    (1, 3, 6, 1, 4, 1, 52674, 500, 4, 1, 6, 1, 7),
    _AmpDetectSensorValueStr_Type()
)
ampDetectSensorValueStr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ampDetectSensorValueStr.setStatus("current")


class _AmpDetectSensorValueInt_Type(Integer32):
    """Custom type ampDetectSensorValueInt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 6554),
    )


_AmpDetectSensorValueInt_Type.__name__ = "Integer32"
_AmpDetectSensorValueInt_Object = MibTableColumn
ampDetectSensorValueInt = _AmpDetectSensorValueInt_Object(
    (1, 3, 6, 1, 4, 1, 52674, 500, 4, 1, 6, 1, 8),
    _AmpDetectSensorValueInt_Type()
)
ampDetectSensorValueInt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ampDetectSensorValueInt.setStatus("current")
_AmpDetectSensorIndex_Type = Counter32
_AmpDetectSensorIndex_Object = MibTableColumn
ampDetectSensorIndex = _AmpDetectSensorIndex_Object(
    (1, 3, 6, 1, 4, 1, 52674, 500, 4, 1, 6, 1, 9),
    _AmpDetectSensorIndex_Type()
)
ampDetectSensorIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ampDetectSensorIndex.setStatus("current")
_OtherNumericSensorTable_Object = MibTable
otherNumericSensorTable = _OtherNumericSensorTable_Object(
    (1, 3, 6, 1, 4, 1, 52674, 500, 4, 1, 10)
)
if mibBuilder.loadTexts:
    otherNumericSensorTable.setStatus("current")
_OtherNumericSensorEntry_Object = MibTableRow
otherNumericSensorEntry = _OtherNumericSensorEntry_Object(
    (1, 3, 6, 1, 4, 1, 52674, 500, 4, 1, 10, 1)
)
otherNumericSensorEntry.setIndexNames(
    (0, "NetBotz50-MIB", "otherNumericSensorIndex"),
)
if mibBuilder.loadTexts:
    otherNumericSensorEntry.setStatus("current")


class _OtherNumericSensorId_Type(DisplayString):
    """Custom type otherNumericSensorId based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_OtherNumericSensorId_Type.__name__ = "DisplayString"
_OtherNumericSensorId_Object = MibTableColumn
otherNumericSensorId = _OtherNumericSensorId_Object(
    (1, 3, 6, 1, 4, 1, 52674, 500, 4, 1, 10, 1, 1),
    _OtherNumericSensorId_Type()
)
otherNumericSensorId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otherNumericSensorId.setStatus("current")
_OtherNumericSensorValue_Type = Integer32
_OtherNumericSensorValue_Object = MibTableColumn
otherNumericSensorValue = _OtherNumericSensorValue_Object(
    (1, 3, 6, 1, 4, 1, 52674, 500, 4, 1, 10, 1, 2),
    _OtherNumericSensorValue_Type()
)
otherNumericSensorValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otherNumericSensorValue.setStatus("current")
_OtherNumericSensorErrorStatus_Type = ErrorStatus
_OtherNumericSensorErrorStatus_Object = MibTableColumn
otherNumericSensorErrorStatus = _OtherNumericSensorErrorStatus_Object(
    (1, 3, 6, 1, 4, 1, 52674, 500, 4, 1, 10, 1, 3),
    _OtherNumericSensorErrorStatus_Type()
)
otherNumericSensorErrorStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otherNumericSensorErrorStatus.setStatus("current")
_OtherNumericSensorLabel_Type = DisplayString
_OtherNumericSensorLabel_Object = MibTableColumn
otherNumericSensorLabel = _OtherNumericSensorLabel_Object(
    (1, 3, 6, 1, 4, 1, 52674, 500, 4, 1, 10, 1, 4),
    _OtherNumericSensorLabel_Type()
)
otherNumericSensorLabel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otherNumericSensorLabel.setStatus("current")


class _OtherNumericSensorEncId_Type(DisplayString):
    """Custom type otherNumericSensorEncId based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_OtherNumericSensorEncId_Type.__name__ = "DisplayString"
_OtherNumericSensorEncId_Object = MibTableColumn
otherNumericSensorEncId = _OtherNumericSensorEncId_Object(
    (1, 3, 6, 1, 4, 1, 52674, 500, 4, 1, 10, 1, 5),
    _OtherNumericSensorEncId_Type()
)
otherNumericSensorEncId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otherNumericSensorEncId.setStatus("current")


class _OtherNumericSensorPortId_Type(DisplayString):
    """Custom type otherNumericSensorPortId based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_OtherNumericSensorPortId_Type.__name__ = "DisplayString"
_OtherNumericSensorPortId_Object = MibTableColumn
otherNumericSensorPortId = _OtherNumericSensorPortId_Object(
    (1, 3, 6, 1, 4, 1, 52674, 500, 4, 1, 10, 1, 6),
    _OtherNumericSensorPortId_Type()
)
otherNumericSensorPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otherNumericSensorPortId.setStatus("current")
_OtherNumericSensorValueStr_Type = DisplayString
_OtherNumericSensorValueStr_Object = MibTableColumn
otherNumericSensorValueStr = _OtherNumericSensorValueStr_Object(
    (1, 3, 6, 1, 4, 1, 52674, 500, 4, 1, 10, 1, 7),
    _OtherNumericSensorValueStr_Type()
)
otherNumericSensorValueStr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otherNumericSensorValueStr.setStatus("current")
_OtherNumericSensorValueInt_Type = Integer32
_OtherNumericSensorValueInt_Object = MibTableColumn
otherNumericSensorValueInt = _OtherNumericSensorValueInt_Object(
    (1, 3, 6, 1, 4, 1, 52674, 500, 4, 1, 10, 1, 8),
    _OtherNumericSensorValueInt_Type()
)
otherNumericSensorValueInt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otherNumericSensorValueInt.setStatus("current")
_OtherNumericSensorUnits_Type = DisplayString
_OtherNumericSensorUnits_Object = MibTableColumn
otherNumericSensorUnits = _OtherNumericSensorUnits_Object(
    (1, 3, 6, 1, 4, 1, 52674, 500, 4, 1, 10, 1, 9),
    _OtherNumericSensorUnits_Type()
)
otherNumericSensorUnits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otherNumericSensorUnits.setStatus("current")
_OtherNumericSensorValueIntX1000_Type = Integer32
_OtherNumericSensorValueIntX1000_Object = MibTableColumn
otherNumericSensorValueIntX1000 = _OtherNumericSensorValueIntX1000_Object(
    (1, 3, 6, 1, 4, 1, 52674, 500, 4, 1, 10, 1, 10),
    _OtherNumericSensorValueIntX1000_Type()
)
otherNumericSensorValueIntX1000.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otherNumericSensorValueIntX1000.setStatus("current")
_OtherNumericSensorValueIntX1000000_Type = Integer32
_OtherNumericSensorValueIntX1000000_Object = MibTableColumn
otherNumericSensorValueIntX1000000 = _OtherNumericSensorValueIntX1000000_Object(
    (1, 3, 6, 1, 4, 1, 52674, 500, 4, 1, 10, 1, 11),
    _OtherNumericSensorValueIntX1000000_Type()
)
otherNumericSensorValueIntX1000000.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otherNumericSensorValueIntX1000000.setStatus("current")
_OtherNumericSensorIndex_Type = Counter32
_OtherNumericSensorIndex_Object = MibTableColumn
otherNumericSensorIndex = _OtherNumericSensorIndex_Object(
    (1, 3, 6, 1, 4, 1, 52674, 500, 4, 1, 10, 1, 12),
    _OtherNumericSensorIndex_Type()
)
otherNumericSensorIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otherNumericSensorIndex.setStatus("current")
_RssiSensorTable_Object = MibTable
rssiSensorTable = _RssiSensorTable_Object(
    (1, 3, 6, 1, 4, 1, 52674, 500, 4, 1, 11)
)
if mibBuilder.loadTexts:
    rssiSensorTable.setStatus("current")
_RssiSensorEntry_Object = MibTableRow
rssiSensorEntry = _RssiSensorEntry_Object(
    (1, 3, 6, 1, 4, 1, 52674, 500, 4, 1, 11, 1)
)
rssiSensorEntry.setIndexNames(
    (0, "NetBotz50-MIB", "rssiSensorIndex"),
)
if mibBuilder.loadTexts:
    rssiSensorEntry.setStatus("current")


class _RssiSensorId_Type(DisplayString):
    """Custom type rssiSensorId based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_RssiSensorId_Type.__name__ = "DisplayString"
_RssiSensorId_Object = MibTableColumn
rssiSensorId = _RssiSensorId_Object(
    (1, 3, 6, 1, 4, 1, 52674, 500, 4, 1, 11, 1, 1),
    _RssiSensorId_Type()
)
rssiSensorId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rssiSensorId.setStatus("current")
_RssiSensorValue_Type = Integer32
_RssiSensorValue_Object = MibTableColumn
rssiSensorValue = _RssiSensorValue_Object(
    (1, 3, 6, 1, 4, 1, 52674, 500, 4, 1, 11, 1, 2),
    _RssiSensorValue_Type()
)
rssiSensorValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rssiSensorValue.setStatus("current")
_RssiSensorErrorStatus_Type = ErrorStatus
_RssiSensorErrorStatus_Object = MibTableColumn
rssiSensorErrorStatus = _RssiSensorErrorStatus_Object(
    (1, 3, 6, 1, 4, 1, 52674, 500, 4, 1, 11, 1, 3),
    _RssiSensorErrorStatus_Type()
)
rssiSensorErrorStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rssiSensorErrorStatus.setStatus("current")
_RssiSensorLabel_Type = DisplayString
_RssiSensorLabel_Object = MibTableColumn
rssiSensorLabel = _RssiSensorLabel_Object(
    (1, 3, 6, 1, 4, 1, 52674, 500, 4, 1, 11, 1, 4),
    _RssiSensorLabel_Type()
)
rssiSensorLabel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rssiSensorLabel.setStatus("current")


class _RssiSensorEncId_Type(DisplayString):
    """Custom type rssiSensorEncId based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_RssiSensorEncId_Type.__name__ = "DisplayString"
_RssiSensorEncId_Object = MibTableColumn
rssiSensorEncId = _RssiSensorEncId_Object(
    (1, 3, 6, 1, 4, 1, 52674, 500, 4, 1, 11, 1, 5),
    _RssiSensorEncId_Type()
)
rssiSensorEncId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rssiSensorEncId.setStatus("current")


class _RssiSensorPortId_Type(DisplayString):
    """Custom type rssiSensorPortId based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_RssiSensorPortId_Type.__name__ = "DisplayString"
_RssiSensorPortId_Object = MibTableColumn
rssiSensorPortId = _RssiSensorPortId_Object(
    (1, 3, 6, 1, 4, 1, 52674, 500, 4, 1, 11, 1, 6),
    _RssiSensorPortId_Type()
)
rssiSensorPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rssiSensorPortId.setStatus("current")
_RssiSensorValueStr_Type = DisplayString
_RssiSensorValueStr_Object = MibTableColumn
rssiSensorValueStr = _RssiSensorValueStr_Object(
    (1, 3, 6, 1, 4, 1, 52674, 500, 4, 1, 11, 1, 7),
    _RssiSensorValueStr_Type()
)
rssiSensorValueStr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rssiSensorValueStr.setStatus("current")
_RssiSensorValueInt_Type = Integer32
_RssiSensorValueInt_Object = MibTableColumn
rssiSensorValueInt = _RssiSensorValueInt_Object(
    (1, 3, 6, 1, 4, 1, 52674, 500, 4, 1, 11, 1, 8),
    _RssiSensorValueInt_Type()
)
rssiSensorValueInt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rssiSensorValueInt.setStatus("current")
_RssiSensorUnits_Type = DisplayString
_RssiSensorUnits_Object = MibTableColumn
rssiSensorUnits = _RssiSensorUnits_Object(
    (1, 3, 6, 1, 4, 1, 52674, 500, 4, 1, 11, 1, 9),
    _RssiSensorUnits_Type()
)
rssiSensorUnits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rssiSensorUnits.setStatus("current")
_RssiSensorIndex_Type = Counter32
_RssiSensorIndex_Object = MibTableColumn
rssiSensorIndex = _RssiSensorIndex_Object(
    (1, 3, 6, 1, 4, 1, 52674, 500, 4, 1, 11, 1, 10),
    _RssiSensorIndex_Type()
)
rssiSensorIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rssiSensorIndex.setStatus("current")
_CurrentInputSensorTable_Object = MibTable
currentInputSensorTable = _CurrentInputSensorTable_Object(
    (1, 3, 6, 1, 4, 1, 52674, 500, 4, 1, 12)
)
if mibBuilder.loadTexts:
    currentInputSensorTable.setStatus("current")
_CurrentInputSensorEntry_Object = MibTableRow
currentInputSensorEntry = _CurrentInputSensorEntry_Object(
    (1, 3, 6, 1, 4, 1, 52674, 500, 4, 1, 12, 1)
)
currentInputSensorEntry.setIndexNames(
    (0, "NetBotz50-MIB", "currentInputSensorIndex"),
)
if mibBuilder.loadTexts:
    currentInputSensorEntry.setStatus("current")


class _CurrentInputSensorId_Type(DisplayString):
    """Custom type currentInputSensorId based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_CurrentInputSensorId_Type.__name__ = "DisplayString"
_CurrentInputSensorId_Object = MibTableColumn
currentInputSensorId = _CurrentInputSensorId_Object(
    (1, 3, 6, 1, 4, 1, 52674, 500, 4, 1, 12, 1, 1),
    _CurrentInputSensorId_Type()
)
currentInputSensorId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    currentInputSensorId.setStatus("current")
_CurrentInputSensorValue_Type = Integer32
_CurrentInputSensorValue_Object = MibTableColumn
currentInputSensorValue = _CurrentInputSensorValue_Object(
    (1, 3, 6, 1, 4, 1, 52674, 500, 4, 1, 12, 1, 2),
    _CurrentInputSensorValue_Type()
)
currentInputSensorValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    currentInputSensorValue.setStatus("current")
_CurrentInputSensorErrorStatus_Type = ErrorStatus
_CurrentInputSensorErrorStatus_Object = MibTableColumn
currentInputSensorErrorStatus = _CurrentInputSensorErrorStatus_Object(
    (1, 3, 6, 1, 4, 1, 52674, 500, 4, 1, 12, 1, 3),
    _CurrentInputSensorErrorStatus_Type()
)
currentInputSensorErrorStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    currentInputSensorErrorStatus.setStatus("current")
_CurrentInputSensorLabel_Type = DisplayString
_CurrentInputSensorLabel_Object = MibTableColumn
currentInputSensorLabel = _CurrentInputSensorLabel_Object(
    (1, 3, 6, 1, 4, 1, 52674, 500, 4, 1, 12, 1, 4),
    _CurrentInputSensorLabel_Type()
)
currentInputSensorLabel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    currentInputSensorLabel.setStatus("current")


class _CurrentInputSensorEncId_Type(DisplayString):
    """Custom type currentInputSensorEncId based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_CurrentInputSensorEncId_Type.__name__ = "DisplayString"
_CurrentInputSensorEncId_Object = MibTableColumn
currentInputSensorEncId = _CurrentInputSensorEncId_Object(
    (1, 3, 6, 1, 4, 1, 52674, 500, 4, 1, 12, 1, 5),
    _CurrentInputSensorEncId_Type()
)
currentInputSensorEncId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    currentInputSensorEncId.setStatus("current")


class _CurrentInputSensorPortId_Type(DisplayString):
    """Custom type currentInputSensorPortId based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_CurrentInputSensorPortId_Type.__name__ = "DisplayString"
_CurrentInputSensorPortId_Object = MibTableColumn
currentInputSensorPortId = _CurrentInputSensorPortId_Object(
    (1, 3, 6, 1, 4, 1, 52674, 500, 4, 1, 12, 1, 6),
    _CurrentInputSensorPortId_Type()
)
currentInputSensorPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    currentInputSensorPortId.setStatus("current")
_CurrentInputSensorValueStr_Type = DisplayString
_CurrentInputSensorValueStr_Object = MibTableColumn
currentInputSensorValueStr = _CurrentInputSensorValueStr_Object(
    (1, 3, 6, 1, 4, 1, 52674, 500, 4, 1, 12, 1, 7),
    _CurrentInputSensorValueStr_Type()
)
currentInputSensorValueStr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    currentInputSensorValueStr.setStatus("current")
_CurrentInputSensorValueInt_Type = Integer32
_CurrentInputSensorValueInt_Object = MibTableColumn
currentInputSensorValueInt = _CurrentInputSensorValueInt_Object(
    (1, 3, 6, 1, 4, 1, 52674, 500, 4, 1, 12, 1, 8),
    _CurrentInputSensorValueInt_Type()
)
currentInputSensorValueInt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    currentInputSensorValueInt.setStatus("current")
_CurrentInputSensorUnits_Type = DisplayString
_CurrentInputSensorUnits_Object = MibTableColumn
currentInputSensorUnits = _CurrentInputSensorUnits_Object(
    (1, 3, 6, 1, 4, 1, 52674, 500, 4, 1, 12, 1, 9),
    _CurrentInputSensorUnits_Type()
)
currentInputSensorUnits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    currentInputSensorUnits.setStatus("current")
_CurrentInputSensorValueIntX1000_Type = Integer32
_CurrentInputSensorValueIntX1000_Object = MibTableColumn
currentInputSensorValueIntX1000 = _CurrentInputSensorValueIntX1000_Object(
    (1, 3, 6, 1, 4, 1, 52674, 500, 4, 1, 12, 1, 10),
    _CurrentInputSensorValueIntX1000_Type()
)
currentInputSensorValueIntX1000.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    currentInputSensorValueIntX1000.setStatus("current")
_CurrentInputSensorValueIntX1000000_Type = Integer32
_CurrentInputSensorValueIntX1000000_Object = MibTableColumn
currentInputSensorValueIntX1000000 = _CurrentInputSensorValueIntX1000000_Object(
    (1, 3, 6, 1, 4, 1, 52674, 500, 4, 1, 12, 1, 11),
    _CurrentInputSensorValueIntX1000000_Type()
)
currentInputSensorValueIntX1000000.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    currentInputSensorValueIntX1000000.setStatus("current")
_CurrentInputSensorIndex_Type = Counter32
_CurrentInputSensorIndex_Object = MibTableColumn
currentInputSensorIndex = _CurrentInputSensorIndex_Object(
    (1, 3, 6, 1, 4, 1, 52674, 500, 4, 1, 12, 1, 12),
    _CurrentInputSensorIndex_Type()
)
currentInputSensorIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    currentInputSensorIndex.setStatus("current")
_VoltageSensorTable_Object = MibTable
voltageSensorTable = _VoltageSensorTable_Object(
    (1, 3, 6, 1, 4, 1, 52674, 500, 4, 1, 13)
)
if mibBuilder.loadTexts:
    voltageSensorTable.setStatus("current")
_VoltageSensorEntry_Object = MibTableRow
voltageSensorEntry = _VoltageSensorEntry_Object(
    (1, 3, 6, 1, 4, 1, 52674, 500, 4, 1, 13, 1)
)
voltageSensorEntry.setIndexNames(
    (0, "NetBotz50-MIB", "voltageSensorIndex"),
)
if mibBuilder.loadTexts:
    voltageSensorEntry.setStatus("current")


class _VoltageSensorId_Type(DisplayString):
    """Custom type voltageSensorId based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_VoltageSensorId_Type.__name__ = "DisplayString"
_VoltageSensorId_Object = MibTableColumn
voltageSensorId = _VoltageSensorId_Object(
    (1, 3, 6, 1, 4, 1, 52674, 500, 4, 1, 13, 1, 1),
    _VoltageSensorId_Type()
)
voltageSensorId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voltageSensorId.setStatus("current")
_VoltageSensorValue_Type = Integer32
_VoltageSensorValue_Object = MibTableColumn
voltageSensorValue = _VoltageSensorValue_Object(
    (1, 3, 6, 1, 4, 1, 52674, 500, 4, 1, 13, 1, 2),
    _VoltageSensorValue_Type()
)
voltageSensorValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voltageSensorValue.setStatus("current")
_VoltageSensorErrorStatus_Type = ErrorStatus
_VoltageSensorErrorStatus_Object = MibTableColumn
voltageSensorErrorStatus = _VoltageSensorErrorStatus_Object(
    (1, 3, 6, 1, 4, 1, 52674, 500, 4, 1, 13, 1, 3),
    _VoltageSensorErrorStatus_Type()
)
voltageSensorErrorStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voltageSensorErrorStatus.setStatus("current")
_VoltageSensorLabel_Type = DisplayString
_VoltageSensorLabel_Object = MibTableColumn
voltageSensorLabel = _VoltageSensorLabel_Object(
    (1, 3, 6, 1, 4, 1, 52674, 500, 4, 1, 13, 1, 4),
    _VoltageSensorLabel_Type()
)
voltageSensorLabel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voltageSensorLabel.setStatus("current")


class _VoltageSensorEncId_Type(DisplayString):
    """Custom type voltageSensorEncId based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_VoltageSensorEncId_Type.__name__ = "DisplayString"
_VoltageSensorEncId_Object = MibTableColumn
voltageSensorEncId = _VoltageSensorEncId_Object(
    (1, 3, 6, 1, 4, 1, 52674, 500, 4, 1, 13, 1, 5),
    _VoltageSensorEncId_Type()
)
voltageSensorEncId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voltageSensorEncId.setStatus("current")


class _VoltageSensorPortId_Type(DisplayString):
    """Custom type voltageSensorPortId based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_VoltageSensorPortId_Type.__name__ = "DisplayString"
_VoltageSensorPortId_Object = MibTableColumn
voltageSensorPortId = _VoltageSensorPortId_Object(
    (1, 3, 6, 1, 4, 1, 52674, 500, 4, 1, 13, 1, 6),
    _VoltageSensorPortId_Type()
)
voltageSensorPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voltageSensorPortId.setStatus("current")
_VoltageSensorValueStr_Type = DisplayString
_VoltageSensorValueStr_Object = MibTableColumn
voltageSensorValueStr = _VoltageSensorValueStr_Object(
    (1, 3, 6, 1, 4, 1, 52674, 500, 4, 1, 13, 1, 7),
    _VoltageSensorValueStr_Type()
)
voltageSensorValueStr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voltageSensorValueStr.setStatus("current")
_VoltageSensorValueInt_Type = Integer32
_VoltageSensorValueInt_Object = MibTableColumn
voltageSensorValueInt = _VoltageSensorValueInt_Object(
    (1, 3, 6, 1, 4, 1, 52674, 500, 4, 1, 13, 1, 8),
    _VoltageSensorValueInt_Type()
)
voltageSensorValueInt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voltageSensorValueInt.setStatus("current")
_VoltageSensorUnits_Type = DisplayString
_VoltageSensorUnits_Object = MibTableColumn
voltageSensorUnits = _VoltageSensorUnits_Object(
    (1, 3, 6, 1, 4, 1, 52674, 500, 4, 1, 13, 1, 9),
    _VoltageSensorUnits_Type()
)
voltageSensorUnits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voltageSensorUnits.setStatus("current")
_VoltageSensorValueIntX1000_Type = Integer32
_VoltageSensorValueIntX1000_Object = MibTableColumn
voltageSensorValueIntX1000 = _VoltageSensorValueIntX1000_Object(
    (1, 3, 6, 1, 4, 1, 52674, 500, 4, 1, 13, 1, 10),
    _VoltageSensorValueIntX1000_Type()
)
voltageSensorValueIntX1000.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voltageSensorValueIntX1000.setStatus("current")
_VoltageSensorValueIntX1000000_Type = Integer32
_VoltageSensorValueIntX1000000_Object = MibTableColumn
voltageSensorValueIntX1000000 = _VoltageSensorValueIntX1000000_Object(
    (1, 3, 6, 1, 4, 1, 52674, 500, 4, 1, 13, 1, 11),
    _VoltageSensorValueIntX1000000_Type()
)
voltageSensorValueIntX1000000.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voltageSensorValueIntX1000000.setStatus("current")
_VoltageSensorIndex_Type = Counter32
_VoltageSensorIndex_Object = MibTableColumn
voltageSensorIndex = _VoltageSensorIndex_Object(
    (1, 3, 6, 1, 4, 1, 52674, 500, 4, 1, 13, 1, 12),
    _VoltageSensorIndex_Type()
)
voltageSensorIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voltageSensorIndex.setStatus("current")
_BatterySensorTable_Object = MibTable
batterySensorTable = _BatterySensorTable_Object(
    (1, 3, 6, 1, 4, 1, 52674, 500, 4, 1, 14)
)
if mibBuilder.loadTexts:
    batterySensorTable.setStatus("current")
_BatterySensorEntry_Object = MibTableRow
batterySensorEntry = _BatterySensorEntry_Object(
    (1, 3, 6, 1, 4, 1, 52674, 500, 4, 1, 14, 1)
)
batterySensorEntry.setIndexNames(
    (0, "NetBotz50-MIB", "batterySensorIndex"),
)
if mibBuilder.loadTexts:
    batterySensorEntry.setStatus("current")


class _BatterySensorId_Type(DisplayString):
    """Custom type batterySensorId based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_BatterySensorId_Type.__name__ = "DisplayString"
_BatterySensorId_Object = MibTableColumn
batterySensorId = _BatterySensorId_Object(
    (1, 3, 6, 1, 4, 1, 52674, 500, 4, 1, 14, 1, 1),
    _BatterySensorId_Type()
)
batterySensorId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    batterySensorId.setStatus("current")
_BatterySensorValue_Type = Integer32
_BatterySensorValue_Object = MibTableColumn
batterySensorValue = _BatterySensorValue_Object(
    (1, 3, 6, 1, 4, 1, 52674, 500, 4, 1, 14, 1, 2),
    _BatterySensorValue_Type()
)
batterySensorValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    batterySensorValue.setStatus("current")
_BatterySensorErrorStatus_Type = ErrorStatus
_BatterySensorErrorStatus_Object = MibTableColumn
batterySensorErrorStatus = _BatterySensorErrorStatus_Object(
    (1, 3, 6, 1, 4, 1, 52674, 500, 4, 1, 14, 1, 3),
    _BatterySensorErrorStatus_Type()
)
batterySensorErrorStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    batterySensorErrorStatus.setStatus("current")
_BatterySensorLabel_Type = DisplayString
_BatterySensorLabel_Object = MibTableColumn
batterySensorLabel = _BatterySensorLabel_Object(
    (1, 3, 6, 1, 4, 1, 52674, 500, 4, 1, 14, 1, 4),
    _BatterySensorLabel_Type()
)
batterySensorLabel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    batterySensorLabel.setStatus("current")


class _BatterySensorEncId_Type(DisplayString):
    """Custom type batterySensorEncId based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_BatterySensorEncId_Type.__name__ = "DisplayString"
_BatterySensorEncId_Object = MibTableColumn
batterySensorEncId = _BatterySensorEncId_Object(
    (1, 3, 6, 1, 4, 1, 52674, 500, 4, 1, 14, 1, 5),
    _BatterySensorEncId_Type()
)
batterySensorEncId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    batterySensorEncId.setStatus("current")


class _BatterySensorPortId_Type(DisplayString):
    """Custom type batterySensorPortId based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_BatterySensorPortId_Type.__name__ = "DisplayString"
_BatterySensorPortId_Object = MibTableColumn
batterySensorPortId = _BatterySensorPortId_Object(
    (1, 3, 6, 1, 4, 1, 52674, 500, 4, 1, 14, 1, 6),
    _BatterySensorPortId_Type()
)
batterySensorPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    batterySensorPortId.setStatus("current")
_BatterySensorValueStr_Type = DisplayString
_BatterySensorValueStr_Object = MibTableColumn
batterySensorValueStr = _BatterySensorValueStr_Object(
    (1, 3, 6, 1, 4, 1, 52674, 500, 4, 1, 14, 1, 7),
    _BatterySensorValueStr_Type()
)
batterySensorValueStr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    batterySensorValueStr.setStatus("current")
_BatterySensorValueInt_Type = Integer32
_BatterySensorValueInt_Object = MibTableColumn
batterySensorValueInt = _BatterySensorValueInt_Object(
    (1, 3, 6, 1, 4, 1, 52674, 500, 4, 1, 14, 1, 8),
    _BatterySensorValueInt_Type()
)
batterySensorValueInt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    batterySensorValueInt.setStatus("current")
_BatterySensorUnits_Type = DisplayString
_BatterySensorUnits_Object = MibTableColumn
batterySensorUnits = _BatterySensorUnits_Object(
    (1, 3, 6, 1, 4, 1, 52674, 500, 4, 1, 14, 1, 9),
    _BatterySensorUnits_Type()
)
batterySensorUnits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    batterySensorUnits.setStatus("current")
_BatterySensorValueIntX1000_Type = Integer32
_BatterySensorValueIntX1000_Object = MibTableColumn
batterySensorValueIntX1000 = _BatterySensorValueIntX1000_Object(
    (1, 3, 6, 1, 4, 1, 52674, 500, 4, 1, 14, 1, 10),
    _BatterySensorValueIntX1000_Type()
)
batterySensorValueIntX1000.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    batterySensorValueIntX1000.setStatus("current")
_BatterySensorValueIntX1000000_Type = Integer32
_BatterySensorValueIntX1000000_Object = MibTableColumn
batterySensorValueIntX1000000 = _BatterySensorValueIntX1000000_Object(
    (1, 3, 6, 1, 4, 1, 52674, 500, 4, 1, 14, 1, 11),
    _BatterySensorValueIntX1000000_Type()
)
batterySensorValueIntX1000000.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    batterySensorValueIntX1000000.setStatus("current")
_BatterySensorIndex_Type = Counter32
_BatterySensorIndex_Object = MibTableColumn
batterySensorIndex = _BatterySensorIndex_Object(
    (1, 3, 6, 1, 4, 1, 52674, 500, 4, 1, 14, 1, 12),
    _BatterySensorIndex_Type()
)
batterySensorIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    batterySensorIndex.setStatus("current")
_NetBotzStateSensors_ObjectIdentity = ObjectIdentity
netBotzStateSensors = _NetBotzStateSensors_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52674, 500, 4, 2)
)
_DryContactSensorTable_Object = MibTable
dryContactSensorTable = _DryContactSensorTable_Object(
    (1, 3, 6, 1, 4, 1, 52674, 500, 4, 2, 1)
)
if mibBuilder.loadTexts:
    dryContactSensorTable.setStatus("current")
_DryContactSensorEntry_Object = MibTableRow
dryContactSensorEntry = _DryContactSensorEntry_Object(
    (1, 3, 6, 1, 4, 1, 52674, 500, 4, 2, 1, 1)
)
dryContactSensorEntry.setIndexNames(
    (0, "NetBotz50-MIB", "dryContactSensorIndex"),
)
if mibBuilder.loadTexts:
    dryContactSensorEntry.setStatus("current")


class _DryContactSensorId_Type(DisplayString):
    """Custom type dryContactSensorId based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_DryContactSensorId_Type.__name__ = "DisplayString"
_DryContactSensorId_Object = MibTableColumn
dryContactSensorId = _DryContactSensorId_Object(
    (1, 3, 6, 1, 4, 1, 52674, 500, 4, 2, 1, 1, 1),
    _DryContactSensorId_Type()
)
dryContactSensorId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dryContactSensorId.setStatus("current")


class _DryContactSensorValue_Type(Integer32):
    """Custom type dryContactSensorValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("undefined", -1),
          ("open", 0),
          ("closed", 1))
    )


_DryContactSensorValue_Type.__name__ = "Integer32"
_DryContactSensorValue_Object = MibTableColumn
dryContactSensorValue = _DryContactSensorValue_Object(
    (1, 3, 6, 1, 4, 1, 52674, 500, 4, 2, 1, 1, 2),
    _DryContactSensorValue_Type()
)
dryContactSensorValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dryContactSensorValue.setStatus("current")
_DryContactSensorErrorStatus_Type = ErrorStatus
_DryContactSensorErrorStatus_Object = MibTableColumn
dryContactSensorErrorStatus = _DryContactSensorErrorStatus_Object(
    (1, 3, 6, 1, 4, 1, 52674, 500, 4, 2, 1, 1, 3),
    _DryContactSensorErrorStatus_Type()
)
dryContactSensorErrorStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dryContactSensorErrorStatus.setStatus("current")
_DryContactSensorLabel_Type = DisplayString
_DryContactSensorLabel_Object = MibTableColumn
dryContactSensorLabel = _DryContactSensorLabel_Object(
    (1, 3, 6, 1, 4, 1, 52674, 500, 4, 2, 1, 1, 4),
    _DryContactSensorLabel_Type()
)
dryContactSensorLabel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dryContactSensorLabel.setStatus("current")


class _DryContactSensorEncId_Type(DisplayString):
    """Custom type dryContactSensorEncId based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_DryContactSensorEncId_Type.__name__ = "DisplayString"
_DryContactSensorEncId_Object = MibTableColumn
dryContactSensorEncId = _DryContactSensorEncId_Object(
    (1, 3, 6, 1, 4, 1, 52674, 500, 4, 2, 1, 1, 5),
    _DryContactSensorEncId_Type()
)
dryContactSensorEncId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dryContactSensorEncId.setStatus("current")


class _DryContactSensorPortId_Type(DisplayString):
    """Custom type dryContactSensorPortId based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_DryContactSensorPortId_Type.__name__ = "DisplayString"
_DryContactSensorPortId_Object = MibTableColumn
dryContactSensorPortId = _DryContactSensorPortId_Object(
    (1, 3, 6, 1, 4, 1, 52674, 500, 4, 2, 1, 1, 6),
    _DryContactSensorPortId_Type()
)
dryContactSensorPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dryContactSensorPortId.setStatus("current")
_DryContactSensorValueStr_Type = DisplayString
_DryContactSensorValueStr_Object = MibTableColumn
dryContactSensorValueStr = _DryContactSensorValueStr_Object(
    (1, 3, 6, 1, 4, 1, 52674, 500, 4, 2, 1, 1, 7),
    _DryContactSensorValueStr_Type()
)
dryContactSensorValueStr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dryContactSensorValueStr.setStatus("current")
_DryContactSensorIndex_Type = Counter32
_DryContactSensorIndex_Object = MibTableColumn
dryContactSensorIndex = _DryContactSensorIndex_Object(
    (1, 3, 6, 1, 4, 1, 52674, 500, 4, 2, 1, 1, 8),
    _DryContactSensorIndex_Type()
)
dryContactSensorIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dryContactSensorIndex.setStatus("current")
_DoorSwitchSensorTable_Object = MibTable
doorSwitchSensorTable = _DoorSwitchSensorTable_Object(
    (1, 3, 6, 1, 4, 1, 52674, 500, 4, 2, 2)
)
if mibBuilder.loadTexts:
    doorSwitchSensorTable.setStatus("current")
_DoorSwitchSensorEntry_Object = MibTableRow
doorSwitchSensorEntry = _DoorSwitchSensorEntry_Object(
    (1, 3, 6, 1, 4, 1, 52674, 500, 4, 2, 2, 1)
)
doorSwitchSensorEntry.setIndexNames(
    (0, "NetBotz50-MIB", "doorSwitchSensorIndex"),
)
if mibBuilder.loadTexts:
    doorSwitchSensorEntry.setStatus("current")


class _DoorSwitchSensorId_Type(DisplayString):
    """Custom type doorSwitchSensorId based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_DoorSwitchSensorId_Type.__name__ = "DisplayString"
_DoorSwitchSensorId_Object = MibTableColumn
doorSwitchSensorId = _DoorSwitchSensorId_Object(
    (1, 3, 6, 1, 4, 1, 52674, 500, 4, 2, 2, 1, 1),
    _DoorSwitchSensorId_Type()
)
doorSwitchSensorId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    doorSwitchSensorId.setStatus("current")


class _DoorSwitchSensorValue_Type(Integer32):
    """Custom type doorSwitchSensorValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("undefined", -1),
          ("open", 0),
          ("closed", 1))
    )


_DoorSwitchSensorValue_Type.__name__ = "Integer32"
_DoorSwitchSensorValue_Object = MibTableColumn
doorSwitchSensorValue = _DoorSwitchSensorValue_Object(
    (1, 3, 6, 1, 4, 1, 52674, 500, 4, 2, 2, 1, 2),
    _DoorSwitchSensorValue_Type()
)
doorSwitchSensorValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    doorSwitchSensorValue.setStatus("current")
_DoorSwitchSensorErrorStatus_Type = ErrorStatus
_DoorSwitchSensorErrorStatus_Object = MibTableColumn
doorSwitchSensorErrorStatus = _DoorSwitchSensorErrorStatus_Object(
    (1, 3, 6, 1, 4, 1, 52674, 500, 4, 2, 2, 1, 3),
    _DoorSwitchSensorErrorStatus_Type()
)
doorSwitchSensorErrorStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    doorSwitchSensorErrorStatus.setStatus("current")
_DoorSwitchSensorLabel_Type = DisplayString
_DoorSwitchSensorLabel_Object = MibTableColumn
doorSwitchSensorLabel = _DoorSwitchSensorLabel_Object(
    (1, 3, 6, 1, 4, 1, 52674, 500, 4, 2, 2, 1, 4),
    _DoorSwitchSensorLabel_Type()
)
doorSwitchSensorLabel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    doorSwitchSensorLabel.setStatus("current")


class _DoorSwitchSensorEncId_Type(DisplayString):
    """Custom type doorSwitchSensorEncId based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_DoorSwitchSensorEncId_Type.__name__ = "DisplayString"
_DoorSwitchSensorEncId_Object = MibTableColumn
doorSwitchSensorEncId = _DoorSwitchSensorEncId_Object(
    (1, 3, 6, 1, 4, 1, 52674, 500, 4, 2, 2, 1, 5),
    _DoorSwitchSensorEncId_Type()
)
doorSwitchSensorEncId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    doorSwitchSensorEncId.setStatus("current")


class _DoorSwitchSensorPortId_Type(DisplayString):
    """Custom type doorSwitchSensorPortId based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_DoorSwitchSensorPortId_Type.__name__ = "DisplayString"
_DoorSwitchSensorPortId_Object = MibTableColumn
doorSwitchSensorPortId = _DoorSwitchSensorPortId_Object(
    (1, 3, 6, 1, 4, 1, 52674, 500, 4, 2, 2, 1, 6),
    _DoorSwitchSensorPortId_Type()
)
doorSwitchSensorPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    doorSwitchSensorPortId.setStatus("current")
_DoorSwitchSensorValueStr_Type = DisplayString
_DoorSwitchSensorValueStr_Object = MibTableColumn
doorSwitchSensorValueStr = _DoorSwitchSensorValueStr_Object(
    (1, 3, 6, 1, 4, 1, 52674, 500, 4, 2, 2, 1, 7),
    _DoorSwitchSensorValueStr_Type()
)
doorSwitchSensorValueStr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    doorSwitchSensorValueStr.setStatus("current")
_DoorSwitchSensorIndex_Type = Counter32
_DoorSwitchSensorIndex_Object = MibTableColumn
doorSwitchSensorIndex = _DoorSwitchSensorIndex_Object(
    (1, 3, 6, 1, 4, 1, 52674, 500, 4, 2, 2, 1, 8),
    _DoorSwitchSensorIndex_Type()
)
doorSwitchSensorIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    doorSwitchSensorIndex.setStatus("current")
_CameraMotionSensorTable_Object = MibTable
cameraMotionSensorTable = _CameraMotionSensorTable_Object(
    (1, 3, 6, 1, 4, 1, 52674, 500, 4, 2, 3)
)
if mibBuilder.loadTexts:
    cameraMotionSensorTable.setStatus("current")
_CameraMotionSensorEntry_Object = MibTableRow
cameraMotionSensorEntry = _CameraMotionSensorEntry_Object(
    (1, 3, 6, 1, 4, 1, 52674, 500, 4, 2, 3, 1)
)
cameraMotionSensorEntry.setIndexNames(
    (0, "NetBotz50-MIB", "cameraMotionSensorIndex"),
)
if mibBuilder.loadTexts:
    cameraMotionSensorEntry.setStatus("current")


class _CameraMotionSensorId_Type(DisplayString):
    """Custom type cameraMotionSensorId based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_CameraMotionSensorId_Type.__name__ = "DisplayString"
_CameraMotionSensorId_Object = MibTableColumn
cameraMotionSensorId = _CameraMotionSensorId_Object(
    (1, 3, 6, 1, 4, 1, 52674, 500, 4, 2, 3, 1, 1),
    _CameraMotionSensorId_Type()
)
cameraMotionSensorId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cameraMotionSensorId.setStatus("current")


class _CameraMotionSensorValue_Type(Integer32):
    """Custom type cameraMotionSensorValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("undefined", -1),
          ("noMotion", 0),
          ("motionDetected", 1))
    )


_CameraMotionSensorValue_Type.__name__ = "Integer32"
_CameraMotionSensorValue_Object = MibTableColumn
cameraMotionSensorValue = _CameraMotionSensorValue_Object(
    (1, 3, 6, 1, 4, 1, 52674, 500, 4, 2, 3, 1, 2),
    _CameraMotionSensorValue_Type()
)
cameraMotionSensorValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cameraMotionSensorValue.setStatus("current")
_CameraMotionSensorErrorStatus_Type = ErrorStatus
_CameraMotionSensorErrorStatus_Object = MibTableColumn
cameraMotionSensorErrorStatus = _CameraMotionSensorErrorStatus_Object(
    (1, 3, 6, 1, 4, 1, 52674, 500, 4, 2, 3, 1, 3),
    _CameraMotionSensorErrorStatus_Type()
)
cameraMotionSensorErrorStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cameraMotionSensorErrorStatus.setStatus("current")
_CameraMotionSensorLabel_Type = DisplayString
_CameraMotionSensorLabel_Object = MibTableColumn
cameraMotionSensorLabel = _CameraMotionSensorLabel_Object(
    (1, 3, 6, 1, 4, 1, 52674, 500, 4, 2, 3, 1, 4),
    _CameraMotionSensorLabel_Type()
)
cameraMotionSensorLabel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cameraMotionSensorLabel.setStatus("current")


class _CameraMotionSensorEncId_Type(DisplayString):
    """Custom type cameraMotionSensorEncId based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_CameraMotionSensorEncId_Type.__name__ = "DisplayString"
_CameraMotionSensorEncId_Object = MibTableColumn
cameraMotionSensorEncId = _CameraMotionSensorEncId_Object(
    (1, 3, 6, 1, 4, 1, 52674, 500, 4, 2, 3, 1, 5),
    _CameraMotionSensorEncId_Type()
)
cameraMotionSensorEncId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cameraMotionSensorEncId.setStatus("current")


class _CameraMotionSensorPortId_Type(DisplayString):
    """Custom type cameraMotionSensorPortId based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_CameraMotionSensorPortId_Type.__name__ = "DisplayString"
_CameraMotionSensorPortId_Object = MibTableColumn
cameraMotionSensorPortId = _CameraMotionSensorPortId_Object(
    (1, 3, 6, 1, 4, 1, 52674, 500, 4, 2, 3, 1, 6),
    _CameraMotionSensorPortId_Type()
)
cameraMotionSensorPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cameraMotionSensorPortId.setStatus("current")
_CameraMotionSensorValueStr_Type = DisplayString
_CameraMotionSensorValueStr_Object = MibTableColumn
cameraMotionSensorValueStr = _CameraMotionSensorValueStr_Object(
    (1, 3, 6, 1, 4, 1, 52674, 500, 4, 2, 3, 1, 7),
    _CameraMotionSensorValueStr_Type()
)
cameraMotionSensorValueStr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cameraMotionSensorValueStr.setStatus("current")
_CameraMotionSensorIndex_Type = Counter32
_CameraMotionSensorIndex_Object = MibTableColumn
cameraMotionSensorIndex = _CameraMotionSensorIndex_Object(
    (1, 3, 6, 1, 4, 1, 52674, 500, 4, 2, 3, 1, 8),
    _CameraMotionSensorIndex_Type()
)
cameraMotionSensorIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cameraMotionSensorIndex.setStatus("current")
_OtherStateSensorTable_Object = MibTable
otherStateSensorTable = _OtherStateSensorTable_Object(
    (1, 3, 6, 1, 4, 1, 52674, 500, 4, 2, 10)
)
if mibBuilder.loadTexts:
    otherStateSensorTable.setStatus("current")
_OtherStateSensorEntry_Object = MibTableRow
otherStateSensorEntry = _OtherStateSensorEntry_Object(
    (1, 3, 6, 1, 4, 1, 52674, 500, 4, 2, 10, 1)
)
otherStateSensorEntry.setIndexNames(
    (0, "NetBotz50-MIB", "otherStateSensorIndex"),
)
if mibBuilder.loadTexts:
    otherStateSensorEntry.setStatus("current")


class _OtherStateSensorId_Type(DisplayString):
    """Custom type otherStateSensorId based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_OtherStateSensorId_Type.__name__ = "DisplayString"
_OtherStateSensorId_Object = MibTableColumn
otherStateSensorId = _OtherStateSensorId_Object(
    (1, 3, 6, 1, 4, 1, 52674, 500, 4, 2, 10, 1, 1),
    _OtherStateSensorId_Type()
)
otherStateSensorId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otherStateSensorId.setStatus("current")
_OtherStateSensorValue_Type = Integer32
_OtherStateSensorValue_Object = MibTableColumn
otherStateSensorValue = _OtherStateSensorValue_Object(
    (1, 3, 6, 1, 4, 1, 52674, 500, 4, 2, 10, 1, 2),
    _OtherStateSensorValue_Type()
)
otherStateSensorValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otherStateSensorValue.setStatus("current")
_OtherStateSensorErrorStatus_Type = ErrorStatus
_OtherStateSensorErrorStatus_Object = MibTableColumn
otherStateSensorErrorStatus = _OtherStateSensorErrorStatus_Object(
    (1, 3, 6, 1, 4, 1, 52674, 500, 4, 2, 10, 1, 3),
    _OtherStateSensorErrorStatus_Type()
)
otherStateSensorErrorStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otherStateSensorErrorStatus.setStatus("current")
_OtherStateSensorLabel_Type = DisplayString
_OtherStateSensorLabel_Object = MibTableColumn
otherStateSensorLabel = _OtherStateSensorLabel_Object(
    (1, 3, 6, 1, 4, 1, 52674, 500, 4, 2, 10, 1, 4),
    _OtherStateSensorLabel_Type()
)
otherStateSensorLabel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otherStateSensorLabel.setStatus("current")


class _OtherStateSensorEncId_Type(DisplayString):
    """Custom type otherStateSensorEncId based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_OtherStateSensorEncId_Type.__name__ = "DisplayString"
_OtherStateSensorEncId_Object = MibTableColumn
otherStateSensorEncId = _OtherStateSensorEncId_Object(
    (1, 3, 6, 1, 4, 1, 52674, 500, 4, 2, 10, 1, 5),
    _OtherStateSensorEncId_Type()
)
otherStateSensorEncId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otherStateSensorEncId.setStatus("current")


class _OtherStateSensorPortId_Type(DisplayString):
    """Custom type otherStateSensorPortId based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_OtherStateSensorPortId_Type.__name__ = "DisplayString"
_OtherStateSensorPortId_Object = MibTableColumn
otherStateSensorPortId = _OtherStateSensorPortId_Object(
    (1, 3, 6, 1, 4, 1, 52674, 500, 4, 2, 10, 1, 6),
    _OtherStateSensorPortId_Type()
)
otherStateSensorPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otherStateSensorPortId.setStatus("current")
_OtherStateSensorValueStr_Type = DisplayString
_OtherStateSensorValueStr_Object = MibTableColumn
otherStateSensorValueStr = _OtherStateSensorValueStr_Object(
    (1, 3, 6, 1, 4, 1, 52674, 500, 4, 2, 10, 1, 7),
    _OtherStateSensorValueStr_Type()
)
otherStateSensorValueStr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otherStateSensorValueStr.setStatus("current")
_OtherStateSensorIndex_Type = Counter32
_OtherStateSensorIndex_Object = MibTableColumn
otherStateSensorIndex = _OtherStateSensorIndex_Object(
    (1, 3, 6, 1, 4, 1, 52674, 500, 4, 2, 10, 1, 8),
    _OtherStateSensorIndex_Type()
)
otherStateSensorIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otherStateSensorIndex.setStatus("current")
_VibrationSensorTable_Object = MibTable
vibrationSensorTable = _VibrationSensorTable_Object(
    (1, 3, 6, 1, 4, 1, 52674, 500, 4, 2, 11)
)
if mibBuilder.loadTexts:
    vibrationSensorTable.setStatus("current")
_VibrationSensorEntry_Object = MibTableRow
vibrationSensorEntry = _VibrationSensorEntry_Object(
    (1, 3, 6, 1, 4, 1, 52674, 500, 4, 2, 11, 1)
)
vibrationSensorEntry.setIndexNames(
    (0, "NetBotz50-MIB", "vibrationSensorIndex"),
)
if mibBuilder.loadTexts:
    vibrationSensorEntry.setStatus("current")


class _VibrationSensorId_Type(DisplayString):
    """Custom type vibrationSensorId based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_VibrationSensorId_Type.__name__ = "DisplayString"
_VibrationSensorId_Object = MibTableColumn
vibrationSensorId = _VibrationSensorId_Object(
    (1, 3, 6, 1, 4, 1, 52674, 500, 4, 2, 11, 1, 1),
    _VibrationSensorId_Type()
)
vibrationSensorId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vibrationSensorId.setStatus("current")


class _VibrationSensorValue_Type(Integer32):
    """Custom type vibrationSensorValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("undefined", -1),
          ("noVibration", 0),
          ("vibrationDetected", 1))
    )


_VibrationSensorValue_Type.__name__ = "Integer32"
_VibrationSensorValue_Object = MibTableColumn
vibrationSensorValue = _VibrationSensorValue_Object(
    (1, 3, 6, 1, 4, 1, 52674, 500, 4, 2, 11, 1, 2),
    _VibrationSensorValue_Type()
)
vibrationSensorValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vibrationSensorValue.setStatus("current")
_VibrationSensorErrorStatus_Type = ErrorStatus
_VibrationSensorErrorStatus_Object = MibTableColumn
vibrationSensorErrorStatus = _VibrationSensorErrorStatus_Object(
    (1, 3, 6, 1, 4, 1, 52674, 500, 4, 2, 11, 1, 3),
    _VibrationSensorErrorStatus_Type()
)
vibrationSensorErrorStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vibrationSensorErrorStatus.setStatus("current")
_VibrationSensorLabel_Type = DisplayString
_VibrationSensorLabel_Object = MibTableColumn
vibrationSensorLabel = _VibrationSensorLabel_Object(
    (1, 3, 6, 1, 4, 1, 52674, 500, 4, 2, 11, 1, 4),
    _VibrationSensorLabel_Type()
)
vibrationSensorLabel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vibrationSensorLabel.setStatus("current")


class _VibrationSensorEncId_Type(DisplayString):
    """Custom type vibrationSensorEncId based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_VibrationSensorEncId_Type.__name__ = "DisplayString"
_VibrationSensorEncId_Object = MibTableColumn
vibrationSensorEncId = _VibrationSensorEncId_Object(
    (1, 3, 6, 1, 4, 1, 52674, 500, 4, 2, 11, 1, 5),
    _VibrationSensorEncId_Type()
)
vibrationSensorEncId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vibrationSensorEncId.setStatus("current")


class _VibrationSensorPortId_Type(DisplayString):
    """Custom type vibrationSensorPortId based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_VibrationSensorPortId_Type.__name__ = "DisplayString"
_VibrationSensorPortId_Object = MibTableColumn
vibrationSensorPortId = _VibrationSensorPortId_Object(
    (1, 3, 6, 1, 4, 1, 52674, 500, 4, 2, 11, 1, 6),
    _VibrationSensorPortId_Type()
)
vibrationSensorPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vibrationSensorPortId.setStatus("current")
_VibrationSensorValueStr_Type = DisplayString
_VibrationSensorValueStr_Object = MibTableColumn
vibrationSensorValueStr = _VibrationSensorValueStr_Object(
    (1, 3, 6, 1, 4, 1, 52674, 500, 4, 2, 11, 1, 7),
    _VibrationSensorValueStr_Type()
)
vibrationSensorValueStr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vibrationSensorValueStr.setStatus("current")
_VibrationSensorIndex_Type = Counter32
_VibrationSensorIndex_Object = MibTableColumn
vibrationSensorIndex = _VibrationSensorIndex_Object(
    (1, 3, 6, 1, 4, 1, 52674, 500, 4, 2, 11, 1, 8),
    _VibrationSensorIndex_Type()
)
vibrationSensorIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vibrationSensorIndex.setStatus("current")
_SmokeSensorTable_Object = MibTable
smokeSensorTable = _SmokeSensorTable_Object(
    (1, 3, 6, 1, 4, 1, 52674, 500, 4, 2, 12)
)
if mibBuilder.loadTexts:
    smokeSensorTable.setStatus("current")
_SmokeSensorEntry_Object = MibTableRow
smokeSensorEntry = _SmokeSensorEntry_Object(
    (1, 3, 6, 1, 4, 1, 52674, 500, 4, 2, 12, 1)
)
smokeSensorEntry.setIndexNames(
    (0, "NetBotz50-MIB", "smokeSensorIndex"),
)
if mibBuilder.loadTexts:
    smokeSensorEntry.setStatus("current")


class _SmokeSensorId_Type(DisplayString):
    """Custom type smokeSensorId based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_SmokeSensorId_Type.__name__ = "DisplayString"
_SmokeSensorId_Object = MibTableColumn
smokeSensorId = _SmokeSensorId_Object(
    (1, 3, 6, 1, 4, 1, 52674, 500, 4, 2, 12, 1, 1),
    _SmokeSensorId_Type()
)
smokeSensorId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smokeSensorId.setStatus("current")


class _SmokeSensorValue_Type(Integer32):
    """Custom type smokeSensorValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("undefined", -1),
          ("noSmoke", 0),
          ("smokeDetected", 1))
    )


_SmokeSensorValue_Type.__name__ = "Integer32"
_SmokeSensorValue_Object = MibTableColumn
smokeSensorValue = _SmokeSensorValue_Object(
    (1, 3, 6, 1, 4, 1, 52674, 500, 4, 2, 12, 1, 2),
    _SmokeSensorValue_Type()
)
smokeSensorValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smokeSensorValue.setStatus("current")
_SmokeSensorErrorStatus_Type = ErrorStatus
_SmokeSensorErrorStatus_Object = MibTableColumn
smokeSensorErrorStatus = _SmokeSensorErrorStatus_Object(
    (1, 3, 6, 1, 4, 1, 52674, 500, 4, 2, 12, 1, 3),
    _SmokeSensorErrorStatus_Type()
)
smokeSensorErrorStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smokeSensorErrorStatus.setStatus("current")
_SmokeSensorLabel_Type = DisplayString
_SmokeSensorLabel_Object = MibTableColumn
smokeSensorLabel = _SmokeSensorLabel_Object(
    (1, 3, 6, 1, 4, 1, 52674, 500, 4, 2, 12, 1, 4),
    _SmokeSensorLabel_Type()
)
smokeSensorLabel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smokeSensorLabel.setStatus("current")


class _SmokeSensorEncId_Type(DisplayString):
    """Custom type smokeSensorEncId based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_SmokeSensorEncId_Type.__name__ = "DisplayString"
_SmokeSensorEncId_Object = MibTableColumn
smokeSensorEncId = _SmokeSensorEncId_Object(
    (1, 3, 6, 1, 4, 1, 52674, 500, 4, 2, 12, 1, 5),
    _SmokeSensorEncId_Type()
)
smokeSensorEncId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smokeSensorEncId.setStatus("current")


class _SmokeSensorPortId_Type(DisplayString):
    """Custom type smokeSensorPortId based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_SmokeSensorPortId_Type.__name__ = "DisplayString"
_SmokeSensorPortId_Object = MibTableColumn
smokeSensorPortId = _SmokeSensorPortId_Object(
    (1, 3, 6, 1, 4, 1, 52674, 500, 4, 2, 12, 1, 6),
    _SmokeSensorPortId_Type()
)
smokeSensorPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smokeSensorPortId.setStatus("current")
_SmokeSensorValueStr_Type = DisplayString
_SmokeSensorValueStr_Object = MibTableColumn
smokeSensorValueStr = _SmokeSensorValueStr_Object(
    (1, 3, 6, 1, 4, 1, 52674, 500, 4, 2, 12, 1, 7),
    _SmokeSensorValueStr_Type()
)
smokeSensorValueStr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smokeSensorValueStr.setStatus("current")
_SmokeSensorIndex_Type = Counter32
_SmokeSensorIndex_Object = MibTableColumn
smokeSensorIndex = _SmokeSensorIndex_Object(
    (1, 3, 6, 1, 4, 1, 52674, 500, 4, 2, 12, 1, 8),
    _SmokeSensorIndex_Type()
)
smokeSensorIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smokeSensorIndex.setStatus("current")
_LeakSensorTable_Object = MibTable
leakSensorTable = _LeakSensorTable_Object(
    (1, 3, 6, 1, 4, 1, 52674, 500, 4, 2, 13)
)
if mibBuilder.loadTexts:
    leakSensorTable.setStatus("current")
_LeakSensorEntry_Object = MibTableRow
leakSensorEntry = _LeakSensorEntry_Object(
    (1, 3, 6, 1, 4, 1, 52674, 500, 4, 2, 13, 1)
)
leakSensorEntry.setIndexNames(
    (0, "NetBotz50-MIB", "leakSensorIndex"),
)
if mibBuilder.loadTexts:
    leakSensorEntry.setStatus("current")


class _LeakSensorId_Type(DisplayString):
    """Custom type leakSensorId based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_LeakSensorId_Type.__name__ = "DisplayString"
_LeakSensorId_Object = MibTableColumn
leakSensorId = _LeakSensorId_Object(
    (1, 3, 6, 1, 4, 1, 52674, 500, 4, 2, 13, 1, 1),
    _LeakSensorId_Type()
)
leakSensorId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    leakSensorId.setStatus("current")


class _LeakSensorValue_Type(Integer32):
    """Custom type leakSensorValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("undefined", -1),
          ("noLeak", 0),
          ("leakDetected", 1))
    )


_LeakSensorValue_Type.__name__ = "Integer32"
_LeakSensorValue_Object = MibTableColumn
leakSensorValue = _LeakSensorValue_Object(
    (1, 3, 6, 1, 4, 1, 52674, 500, 4, 2, 13, 1, 2),
    _LeakSensorValue_Type()
)
leakSensorValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    leakSensorValue.setStatus("current")
_LeakSensorErrorStatus_Type = ErrorStatus
_LeakSensorErrorStatus_Object = MibTableColumn
leakSensorErrorStatus = _LeakSensorErrorStatus_Object(
    (1, 3, 6, 1, 4, 1, 52674, 500, 4, 2, 13, 1, 3),
    _LeakSensorErrorStatus_Type()
)
leakSensorErrorStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    leakSensorErrorStatus.setStatus("current")
_LeakSensorLabel_Type = DisplayString
_LeakSensorLabel_Object = MibTableColumn
leakSensorLabel = _LeakSensorLabel_Object(
    (1, 3, 6, 1, 4, 1, 52674, 500, 4, 2, 13, 1, 4),
    _LeakSensorLabel_Type()
)
leakSensorLabel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    leakSensorLabel.setStatus("current")


class _LeakSensorEncId_Type(DisplayString):
    """Custom type leakSensorEncId based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_LeakSensorEncId_Type.__name__ = "DisplayString"
_LeakSensorEncId_Object = MibTableColumn
leakSensorEncId = _LeakSensorEncId_Object(
    (1, 3, 6, 1, 4, 1, 52674, 500, 4, 2, 13, 1, 5),
    _LeakSensorEncId_Type()
)
leakSensorEncId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    leakSensorEncId.setStatus("current")


class _LeakSensorPortId_Type(DisplayString):
    """Custom type leakSensorPortId based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_LeakSensorPortId_Type.__name__ = "DisplayString"
_LeakSensorPortId_Object = MibTableColumn
leakSensorPortId = _LeakSensorPortId_Object(
    (1, 3, 6, 1, 4, 1, 52674, 500, 4, 2, 13, 1, 6),
    _LeakSensorPortId_Type()
)
leakSensorPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    leakSensorPortId.setStatus("current")
_LeakSensorValueStr_Type = DisplayString
_LeakSensorValueStr_Object = MibTableColumn
leakSensorValueStr = _LeakSensorValueStr_Object(
    (1, 3, 6, 1, 4, 1, 52674, 500, 4, 2, 13, 1, 7),
    _LeakSensorValueStr_Type()
)
leakSensorValueStr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    leakSensorValueStr.setStatus("current")
_LeakSensorIndex_Type = Counter32
_LeakSensorIndex_Object = MibTableColumn
leakSensorIndex = _LeakSensorIndex_Object(
    (1, 3, 6, 1, 4, 1, 52674, 500, 4, 2, 13, 1, 8),
    _LeakSensorIndex_Type()
)
leakSensorIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    leakSensorIndex.setStatus("current")
_BeaconTable_Object = MibTable
beaconTable = _BeaconTable_Object(
    (1, 3, 6, 1, 4, 1, 52674, 500, 4, 2, 14)
)
if mibBuilder.loadTexts:
    beaconTable.setStatus("current")
_BeaconEntry_Object = MibTableRow
beaconEntry = _BeaconEntry_Object(
    (1, 3, 6, 1, 4, 1, 52674, 500, 4, 2, 14, 1)
)
beaconEntry.setIndexNames(
    (0, "NetBotz50-MIB", "beaconIndex"),
)
if mibBuilder.loadTexts:
    beaconEntry.setStatus("current")


class _BeaconId_Type(DisplayString):
    """Custom type beaconId based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_BeaconId_Type.__name__ = "DisplayString"
_BeaconId_Object = MibTableColumn
beaconId = _BeaconId_Object(
    (1, 3, 6, 1, 4, 1, 52674, 500, 4, 2, 14, 1, 1),
    _BeaconId_Type()
)
beaconId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    beaconId.setStatus("current")


class _BeaconValue_Type(Integer32):
    """Custom type beaconValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("undefined", -1),
          ("off", 0),
          ("on", 1))
    )


_BeaconValue_Type.__name__ = "Integer32"
_BeaconValue_Object = MibTableColumn
beaconValue = _BeaconValue_Object(
    (1, 3, 6, 1, 4, 1, 52674, 500, 4, 2, 14, 1, 2),
    _BeaconValue_Type()
)
beaconValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    beaconValue.setStatus("current")
_BeaconErrorStatus_Type = ErrorStatus
_BeaconErrorStatus_Object = MibTableColumn
beaconErrorStatus = _BeaconErrorStatus_Object(
    (1, 3, 6, 1, 4, 1, 52674, 500, 4, 2, 14, 1, 3),
    _BeaconErrorStatus_Type()
)
beaconErrorStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    beaconErrorStatus.setStatus("current")
_BeaconLabel_Type = DisplayString
_BeaconLabel_Object = MibTableColumn
beaconLabel = _BeaconLabel_Object(
    (1, 3, 6, 1, 4, 1, 52674, 500, 4, 2, 14, 1, 4),
    _BeaconLabel_Type()
)
beaconLabel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    beaconLabel.setStatus("current")


class _BeaconEncId_Type(DisplayString):
    """Custom type beaconEncId based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_BeaconEncId_Type.__name__ = "DisplayString"
_BeaconEncId_Object = MibTableColumn
beaconEncId = _BeaconEncId_Object(
    (1, 3, 6, 1, 4, 1, 52674, 500, 4, 2, 14, 1, 5),
    _BeaconEncId_Type()
)
beaconEncId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    beaconEncId.setStatus("current")


class _BeaconPortId_Type(DisplayString):
    """Custom type beaconPortId based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_BeaconPortId_Type.__name__ = "DisplayString"
_BeaconPortId_Object = MibTableColumn
beaconPortId = _BeaconPortId_Object(
    (1, 3, 6, 1, 4, 1, 52674, 500, 4, 2, 14, 1, 6),
    _BeaconPortId_Type()
)
beaconPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    beaconPortId.setStatus("current")
_BeaconValueStr_Type = DisplayString
_BeaconValueStr_Object = MibTableColumn
beaconValueStr = _BeaconValueStr_Object(
    (1, 3, 6, 1, 4, 1, 52674, 500, 4, 2, 14, 1, 7),
    _BeaconValueStr_Type()
)
beaconValueStr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    beaconValueStr.setStatus("current")
_BeaconIndex_Type = Counter32
_BeaconIndex_Object = MibTableColumn
beaconIndex = _BeaconIndex_Object(
    (1, 3, 6, 1, 4, 1, 52674, 500, 4, 2, 14, 1, 8),
    _BeaconIndex_Type()
)
beaconIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    beaconIndex.setStatus("current")
_SwitchedOutletTable_Object = MibTable
switchedOutletTable = _SwitchedOutletTable_Object(
    (1, 3, 6, 1, 4, 1, 52674, 500, 4, 2, 15)
)
if mibBuilder.loadTexts:
    switchedOutletTable.setStatus("current")
_SwitchedOutletEntry_Object = MibTableRow
switchedOutletEntry = _SwitchedOutletEntry_Object(
    (1, 3, 6, 1, 4, 1, 52674, 500, 4, 2, 15, 1)
)
switchedOutletEntry.setIndexNames(
    (0, "NetBotz50-MIB", "switchedOutletIndex"),
)
if mibBuilder.loadTexts:
    switchedOutletEntry.setStatus("current")


class _SwitchedOutletId_Type(DisplayString):
    """Custom type switchedOutletId based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_SwitchedOutletId_Type.__name__ = "DisplayString"
_SwitchedOutletId_Object = MibTableColumn
switchedOutletId = _SwitchedOutletId_Object(
    (1, 3, 6, 1, 4, 1, 52674, 500, 4, 2, 15, 1, 1),
    _SwitchedOutletId_Type()
)
switchedOutletId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    switchedOutletId.setStatus("current")


class _SwitchedOutletValue_Type(Integer32):
    """Custom type switchedOutletValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("undefined", -1),
          ("off", 0),
          ("on", 1))
    )


_SwitchedOutletValue_Type.__name__ = "Integer32"
_SwitchedOutletValue_Object = MibTableColumn
switchedOutletValue = _SwitchedOutletValue_Object(
    (1, 3, 6, 1, 4, 1, 52674, 500, 4, 2, 15, 1, 2),
    _SwitchedOutletValue_Type()
)
switchedOutletValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    switchedOutletValue.setStatus("current")
_SwitchedOutletErrorStatus_Type = ErrorStatus
_SwitchedOutletErrorStatus_Object = MibTableColumn
switchedOutletErrorStatus = _SwitchedOutletErrorStatus_Object(
    (1, 3, 6, 1, 4, 1, 52674, 500, 4, 2, 15, 1, 3),
    _SwitchedOutletErrorStatus_Type()
)
switchedOutletErrorStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    switchedOutletErrorStatus.setStatus("current")
_SwitchedOutletLabel_Type = DisplayString
_SwitchedOutletLabel_Object = MibTableColumn
switchedOutletLabel = _SwitchedOutletLabel_Object(
    (1, 3, 6, 1, 4, 1, 52674, 500, 4, 2, 15, 1, 4),
    _SwitchedOutletLabel_Type()
)
switchedOutletLabel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    switchedOutletLabel.setStatus("current")


class _SwitchedOutletEncId_Type(DisplayString):
    """Custom type switchedOutletEncId based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_SwitchedOutletEncId_Type.__name__ = "DisplayString"
_SwitchedOutletEncId_Object = MibTableColumn
switchedOutletEncId = _SwitchedOutletEncId_Object(
    (1, 3, 6, 1, 4, 1, 52674, 500, 4, 2, 15, 1, 5),
    _SwitchedOutletEncId_Type()
)
switchedOutletEncId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    switchedOutletEncId.setStatus("current")


class _SwitchedOutletPortId_Type(DisplayString):
    """Custom type switchedOutletPortId based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_SwitchedOutletPortId_Type.__name__ = "DisplayString"
_SwitchedOutletPortId_Object = MibTableColumn
switchedOutletPortId = _SwitchedOutletPortId_Object(
    (1, 3, 6, 1, 4, 1, 52674, 500, 4, 2, 15, 1, 6),
    _SwitchedOutletPortId_Type()
)
switchedOutletPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    switchedOutletPortId.setStatus("current")
_SwitchedOutletValueStr_Type = DisplayString
_SwitchedOutletValueStr_Object = MibTableColumn
switchedOutletValueStr = _SwitchedOutletValueStr_Object(
    (1, 3, 6, 1, 4, 1, 52674, 500, 4, 2, 15, 1, 7),
    _SwitchedOutletValueStr_Type()
)
switchedOutletValueStr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    switchedOutletValueStr.setStatus("current")
_SwitchedOutletIndex_Type = Counter32
_SwitchedOutletIndex_Object = MibTableColumn
switchedOutletIndex = _SwitchedOutletIndex_Object(
    (1, 3, 6, 1, 4, 1, 52674, 500, 4, 2, 15, 1, 8),
    _SwitchedOutletIndex_Type()
)
switchedOutletIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    switchedOutletIndex.setStatus("current")
_DoorLockSensorTable_Object = MibTable
doorLockSensorTable = _DoorLockSensorTable_Object(
    (1, 3, 6, 1, 4, 1, 52674, 500, 4, 2, 16)
)
if mibBuilder.loadTexts:
    doorLockSensorTable.setStatus("current")
_DoorLockSensorEntry_Object = MibTableRow
doorLockSensorEntry = _DoorLockSensorEntry_Object(
    (1, 3, 6, 1, 4, 1, 52674, 500, 4, 2, 16, 1)
)
doorLockSensorEntry.setIndexNames(
    (0, "NetBotz50-MIB", "doorLockSensorIndex"),
)
if mibBuilder.loadTexts:
    doorLockSensorEntry.setStatus("current")


class _DoorLockSensorId_Type(DisplayString):
    """Custom type doorLockSensorId based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_DoorLockSensorId_Type.__name__ = "DisplayString"
_DoorLockSensorId_Object = MibTableColumn
doorLockSensorId = _DoorLockSensorId_Object(
    (1, 3, 6, 1, 4, 1, 52674, 500, 4, 2, 16, 1, 1),
    _DoorLockSensorId_Type()
)
doorLockSensorId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    doorLockSensorId.setStatus("current")


class _DoorLockSensorValue_Type(Integer32):
    """Custom type doorLockSensorValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("undefined", -1),
          ("unlocked", 0),
          ("locked", 1))
    )


_DoorLockSensorValue_Type.__name__ = "Integer32"
_DoorLockSensorValue_Object = MibTableColumn
doorLockSensorValue = _DoorLockSensorValue_Object(
    (1, 3, 6, 1, 4, 1, 52674, 500, 4, 2, 16, 1, 2),
    _DoorLockSensorValue_Type()
)
doorLockSensorValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    doorLockSensorValue.setStatus("current")
_DoorLockSensorErrorStatus_Type = ErrorStatus
_DoorLockSensorErrorStatus_Object = MibTableColumn
doorLockSensorErrorStatus = _DoorLockSensorErrorStatus_Object(
    (1, 3, 6, 1, 4, 1, 52674, 500, 4, 2, 16, 1, 3),
    _DoorLockSensorErrorStatus_Type()
)
doorLockSensorErrorStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    doorLockSensorErrorStatus.setStatus("current")
_DoorLockSensorLabel_Type = DisplayString
_DoorLockSensorLabel_Object = MibTableColumn
doorLockSensorLabel = _DoorLockSensorLabel_Object(
    (1, 3, 6, 1, 4, 1, 52674, 500, 4, 2, 16, 1, 4),
    _DoorLockSensorLabel_Type()
)
doorLockSensorLabel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    doorLockSensorLabel.setStatus("current")


class _DoorLockSensorEncId_Type(DisplayString):
    """Custom type doorLockSensorEncId based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_DoorLockSensorEncId_Type.__name__ = "DisplayString"
_DoorLockSensorEncId_Object = MibTableColumn
doorLockSensorEncId = _DoorLockSensorEncId_Object(
    (1, 3, 6, 1, 4, 1, 52674, 500, 4, 2, 16, 1, 5),
    _DoorLockSensorEncId_Type()
)
doorLockSensorEncId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    doorLockSensorEncId.setStatus("current")


class _DoorLockSensorPortId_Type(DisplayString):
    """Custom type doorLockSensorPortId based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_DoorLockSensorPortId_Type.__name__ = "DisplayString"
_DoorLockSensorPortId_Object = MibTableColumn
doorLockSensorPortId = _DoorLockSensorPortId_Object(
    (1, 3, 6, 1, 4, 1, 52674, 500, 4, 2, 16, 1, 6),
    _DoorLockSensorPortId_Type()
)
doorLockSensorPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    doorLockSensorPortId.setStatus("current")
_DoorLockSensorValueStr_Type = DisplayString
_DoorLockSensorValueStr_Object = MibTableColumn
doorLockSensorValueStr = _DoorLockSensorValueStr_Object(
    (1, 3, 6, 1, 4, 1, 52674, 500, 4, 2, 16, 1, 7),
    _DoorLockSensorValueStr_Type()
)
doorLockSensorValueStr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    doorLockSensorValueStr.setStatus("current")
_DoorLockSensorIndex_Type = Counter32
_DoorLockSensorIndex_Object = MibTableColumn
doorLockSensorIndex = _DoorLockSensorIndex_Object(
    (1, 3, 6, 1, 4, 1, 52674, 500, 4, 2, 16, 1, 8),
    _DoorLockSensorIndex_Type()
)
doorLockSensorIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    doorLockSensorIndex.setStatus("current")
_RackHandleSensorTable_Object = MibTable
rackHandleSensorTable = _RackHandleSensorTable_Object(
    (1, 3, 6, 1, 4, 1, 52674, 500, 4, 2, 17)
)
if mibBuilder.loadTexts:
    rackHandleSensorTable.setStatus("current")
_RackHandleSensorEntry_Object = MibTableRow
rackHandleSensorEntry = _RackHandleSensorEntry_Object(
    (1, 3, 6, 1, 4, 1, 52674, 500, 4, 2, 17, 1)
)
rackHandleSensorEntry.setIndexNames(
    (0, "NetBotz50-MIB", "rackHandleSensorIndex"),
)
if mibBuilder.loadTexts:
    rackHandleSensorEntry.setStatus("current")


class _RackHandleSensorId_Type(DisplayString):
    """Custom type rackHandleSensorId based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_RackHandleSensorId_Type.__name__ = "DisplayString"
_RackHandleSensorId_Object = MibTableColumn
rackHandleSensorId = _RackHandleSensorId_Object(
    (1, 3, 6, 1, 4, 1, 52674, 500, 4, 2, 17, 1, 1),
    _RackHandleSensorId_Type()
)
rackHandleSensorId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rackHandleSensorId.setStatus("current")


class _RackHandleSensorValue_Type(Integer32):
    """Custom type rackHandleSensorValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("undefined", -1),
          ("open", 0),
          ("closed", 1))
    )


_RackHandleSensorValue_Type.__name__ = "Integer32"
_RackHandleSensorValue_Object = MibTableColumn
rackHandleSensorValue = _RackHandleSensorValue_Object(
    (1, 3, 6, 1, 4, 1, 52674, 500, 4, 2, 17, 1, 2),
    _RackHandleSensorValue_Type()
)
rackHandleSensorValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rackHandleSensorValue.setStatus("current")
_RackHandleSensorErrorStatus_Type = ErrorStatus
_RackHandleSensorErrorStatus_Object = MibTableColumn
rackHandleSensorErrorStatus = _RackHandleSensorErrorStatus_Object(
    (1, 3, 6, 1, 4, 1, 52674, 500, 4, 2, 17, 1, 3),
    _RackHandleSensorErrorStatus_Type()
)
rackHandleSensorErrorStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rackHandleSensorErrorStatus.setStatus("current")
_RackHandleSensorLabel_Type = DisplayString
_RackHandleSensorLabel_Object = MibTableColumn
rackHandleSensorLabel = _RackHandleSensorLabel_Object(
    (1, 3, 6, 1, 4, 1, 52674, 500, 4, 2, 17, 1, 4),
    _RackHandleSensorLabel_Type()
)
rackHandleSensorLabel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rackHandleSensorLabel.setStatus("current")


class _RackHandleSensorEncId_Type(DisplayString):
    """Custom type rackHandleSensorEncId based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_RackHandleSensorEncId_Type.__name__ = "DisplayString"
_RackHandleSensorEncId_Object = MibTableColumn
rackHandleSensorEncId = _RackHandleSensorEncId_Object(
    (1, 3, 6, 1, 4, 1, 52674, 500, 4, 2, 17, 1, 5),
    _RackHandleSensorEncId_Type()
)
rackHandleSensorEncId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rackHandleSensorEncId.setStatus("current")


class _RackHandleSensorPortId_Type(DisplayString):
    """Custom type rackHandleSensorPortId based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_RackHandleSensorPortId_Type.__name__ = "DisplayString"
_RackHandleSensorPortId_Object = MibTableColumn
rackHandleSensorPortId = _RackHandleSensorPortId_Object(
    (1, 3, 6, 1, 4, 1, 52674, 500, 4, 2, 17, 1, 6),
    _RackHandleSensorPortId_Type()
)
rackHandleSensorPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rackHandleSensorPortId.setStatus("current")
_RackHandleSensorValueStr_Type = DisplayString
_RackHandleSensorValueStr_Object = MibTableColumn
rackHandleSensorValueStr = _RackHandleSensorValueStr_Object(
    (1, 3, 6, 1, 4, 1, 52674, 500, 4, 2, 17, 1, 7),
    _RackHandleSensorValueStr_Type()
)
rackHandleSensorValueStr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rackHandleSensorValueStr.setStatus("current")
_RackHandleSensorIndex_Type = Counter32
_RackHandleSensorIndex_Object = MibTableColumn
rackHandleSensorIndex = _RackHandleSensorIndex_Object(
    (1, 3, 6, 1, 4, 1, 52674, 500, 4, 2, 17, 1, 8),
    _RackHandleSensorIndex_Type()
)
rackHandleSensorIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rackHandleSensorIndex.setStatus("current")
_OutputRelaySensorTable_Object = MibTable
outputRelaySensorTable = _OutputRelaySensorTable_Object(
    (1, 3, 6, 1, 4, 1, 52674, 500, 4, 2, 18)
)
if mibBuilder.loadTexts:
    outputRelaySensorTable.setStatus("current")
_OutputRelaySensorEntry_Object = MibTableRow
outputRelaySensorEntry = _OutputRelaySensorEntry_Object(
    (1, 3, 6, 1, 4, 1, 52674, 500, 4, 2, 18, 1)
)
outputRelaySensorEntry.setIndexNames(
    (0, "NetBotz50-MIB", "outputRelaySensorIndex"),
)
if mibBuilder.loadTexts:
    outputRelaySensorEntry.setStatus("current")


class _OutputRelaySensorId_Type(DisplayString):
    """Custom type outputRelaySensorId based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_OutputRelaySensorId_Type.__name__ = "DisplayString"
_OutputRelaySensorId_Object = MibTableColumn
outputRelaySensorId = _OutputRelaySensorId_Object(
    (1, 3, 6, 1, 4, 1, 52674, 500, 4, 2, 18, 1, 1),
    _OutputRelaySensorId_Type()
)
outputRelaySensorId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outputRelaySensorId.setStatus("current")


class _OutputRelaySensorValue_Type(Integer32):
    """Custom type outputRelaySensorValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("undefined", -1),
          ("open", 0),
          ("closed", 1))
    )


_OutputRelaySensorValue_Type.__name__ = "Integer32"
_OutputRelaySensorValue_Object = MibTableColumn
outputRelaySensorValue = _OutputRelaySensorValue_Object(
    (1, 3, 6, 1, 4, 1, 52674, 500, 4, 2, 18, 1, 2),
    _OutputRelaySensorValue_Type()
)
outputRelaySensorValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outputRelaySensorValue.setStatus("current")
_OutputRelaySensorErrorStatus_Type = ErrorStatus
_OutputRelaySensorErrorStatus_Object = MibTableColumn
outputRelaySensorErrorStatus = _OutputRelaySensorErrorStatus_Object(
    (1, 3, 6, 1, 4, 1, 52674, 500, 4, 2, 18, 1, 3),
    _OutputRelaySensorErrorStatus_Type()
)
outputRelaySensorErrorStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outputRelaySensorErrorStatus.setStatus("current")
_OutputRelaySensorLabel_Type = DisplayString
_OutputRelaySensorLabel_Object = MibTableColumn
outputRelaySensorLabel = _OutputRelaySensorLabel_Object(
    (1, 3, 6, 1, 4, 1, 52674, 500, 4, 2, 18, 1, 4),
    _OutputRelaySensorLabel_Type()
)
outputRelaySensorLabel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outputRelaySensorLabel.setStatus("current")


class _OutputRelaySensorEncId_Type(DisplayString):
    """Custom type outputRelaySensorEncId based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_OutputRelaySensorEncId_Type.__name__ = "DisplayString"
_OutputRelaySensorEncId_Object = MibTableColumn
outputRelaySensorEncId = _OutputRelaySensorEncId_Object(
    (1, 3, 6, 1, 4, 1, 52674, 500, 4, 2, 18, 1, 5),
    _OutputRelaySensorEncId_Type()
)
outputRelaySensorEncId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outputRelaySensorEncId.setStatus("current")


class _OutputRelaySensorPortId_Type(DisplayString):
    """Custom type outputRelaySensorPortId based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_OutputRelaySensorPortId_Type.__name__ = "DisplayString"
_OutputRelaySensorPortId_Object = MibTableColumn
outputRelaySensorPortId = _OutputRelaySensorPortId_Object(
    (1, 3, 6, 1, 4, 1, 52674, 500, 4, 2, 18, 1, 6),
    _OutputRelaySensorPortId_Type()
)
outputRelaySensorPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outputRelaySensorPortId.setStatus("current")
_OutputRelaySensorValueStr_Type = DisplayString
_OutputRelaySensorValueStr_Object = MibTableColumn
outputRelaySensorValueStr = _OutputRelaySensorValueStr_Object(
    (1, 3, 6, 1, 4, 1, 52674, 500, 4, 2, 18, 1, 7),
    _OutputRelaySensorValueStr_Type()
)
outputRelaySensorValueStr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outputRelaySensorValueStr.setStatus("current")
_OutputRelaySensorIndex_Type = Counter32
_OutputRelaySensorIndex_Object = MibTableColumn
outputRelaySensorIndex = _OutputRelaySensorIndex_Object(
    (1, 3, 6, 1, 4, 1, 52674, 500, 4, 2, 18, 1, 8),
    _OutputRelaySensorIndex_Type()
)
outputRelaySensorIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outputRelaySensorIndex.setStatus("current")
_NetBotzErrors_ObjectIdentity = ObjectIdentity
netBotzErrors = _NetBotzErrors_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52674, 500, 5)
)
_ErrorCondTable_Object = MibTable
errorCondTable = _ErrorCondTable_Object(
    (1, 3, 6, 1, 4, 1, 52674, 500, 5, 1)
)
if mibBuilder.loadTexts:
    errorCondTable.setStatus("current")
_ErrorCondEntry_Object = MibTableRow
errorCondEntry = _ErrorCondEntry_Object(
    (1, 3, 6, 1, 4, 1, 52674, 500, 5, 1, 1)
)
errorCondEntry.setIndexNames(
    (0, "NetBotz50-MIB", "errorCondIndex"),
)
if mibBuilder.loadTexts:
    errorCondEntry.setStatus("current")


class _ErrorCondId_Type(DisplayString):
    """Custom type errorCondId based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_ErrorCondId_Type.__name__ = "DisplayString"
_ErrorCondId_Object = MibTableColumn
errorCondId = _ErrorCondId_Object(
    (1, 3, 6, 1, 4, 1, 52674, 500, 5, 1, 1, 1),
    _ErrorCondId_Type()
)
errorCondId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    errorCondId.setStatus("current")
_ErrorCondSeverity_Type = ErrorStatus
_ErrorCondSeverity_Object = MibTableColumn
errorCondSeverity = _ErrorCondSeverity_Object(
    (1, 3, 6, 1, 4, 1, 52674, 500, 5, 1, 1, 2),
    _ErrorCondSeverity_Type()
)
errorCondSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    errorCondSeverity.setStatus("current")


class _ErrorCondTypeId_Type(DisplayString):
    """Custom type errorCondTypeId based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_ErrorCondTypeId_Type.__name__ = "DisplayString"
_ErrorCondTypeId_Object = MibTableColumn
errorCondTypeId = _ErrorCondTypeId_Object(
    (1, 3, 6, 1, 4, 1, 52674, 500, 5, 1, 1, 3),
    _ErrorCondTypeId_Type()
)
errorCondTypeId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    errorCondTypeId.setStatus("current")
_ErrorCondStartTime_Type = DateAndTime
_ErrorCondStartTime_Object = MibTableColumn
errorCondStartTime = _ErrorCondStartTime_Object(
    (1, 3, 6, 1, 4, 1, 52674, 500, 5, 1, 1, 4),
    _ErrorCondStartTime_Type()
)
errorCondStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    errorCondStartTime.setStatus("current")
_ErrorCondStartTimeStr_Type = DisplayString
_ErrorCondStartTimeStr_Object = MibTableColumn
errorCondStartTimeStr = _ErrorCondStartTimeStr_Object(
    (1, 3, 6, 1, 4, 1, 52674, 500, 5, 1, 1, 5),
    _ErrorCondStartTimeStr_Type()
)
errorCondStartTimeStr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    errorCondStartTimeStr.setStatus("current")
_ErrorCondResolved_Type = BoolValue
_ErrorCondResolved_Object = MibTableColumn
errorCondResolved = _ErrorCondResolved_Object(
    (1, 3, 6, 1, 4, 1, 52674, 500, 5, 1, 1, 6),
    _ErrorCondResolved_Type()
)
errorCondResolved.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    errorCondResolved.setStatus("current")
_ErrorCondResolvedTime_Type = DateAndTime
_ErrorCondResolvedTime_Object = MibTableColumn
errorCondResolvedTime = _ErrorCondResolvedTime_Object(
    (1, 3, 6, 1, 4, 1, 52674, 500, 5, 1, 1, 7),
    _ErrorCondResolvedTime_Type()
)
errorCondResolvedTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    errorCondResolvedTime.setStatus("current")
_ErrorCondResolvedTimeStr_Type = DisplayString
_ErrorCondResolvedTimeStr_Object = MibTableColumn
errorCondResolvedTimeStr = _ErrorCondResolvedTimeStr_Object(
    (1, 3, 6, 1, 4, 1, 52674, 500, 5, 1, 1, 8),
    _ErrorCondResolvedTimeStr_Type()
)
errorCondResolvedTimeStr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    errorCondResolvedTimeStr.setStatus("current")


class _ErrorCondEncId_Type(DisplayString):
    """Custom type errorCondEncId based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_ErrorCondEncId_Type.__name__ = "DisplayString"
_ErrorCondEncId_Object = MibTableColumn
errorCondEncId = _ErrorCondEncId_Object(
    (1, 3, 6, 1, 4, 1, 52674, 500, 5, 1, 1, 9),
    _ErrorCondEncId_Type()
)
errorCondEncId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    errorCondEncId.setStatus("current")


class _ErrorCondPortId_Type(DisplayString):
    """Custom type errorCondPortId based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_ErrorCondPortId_Type.__name__ = "DisplayString"
_ErrorCondPortId_Object = MibTableColumn
errorCondPortId = _ErrorCondPortId_Object(
    (1, 3, 6, 1, 4, 1, 52674, 500, 5, 1, 1, 10),
    _ErrorCondPortId_Type()
)
errorCondPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    errorCondPortId.setStatus("current")


class _ErrorCondSensorId_Type(DisplayString):
    """Custom type errorCondSensorId based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_ErrorCondSensorId_Type.__name__ = "DisplayString"
_ErrorCondSensorId_Object = MibTableColumn
errorCondSensorId = _ErrorCondSensorId_Object(
    (1, 3, 6, 1, 4, 1, 52674, 500, 5, 1, 1, 11),
    _ErrorCondSensorId_Type()
)
errorCondSensorId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    errorCondSensorId.setStatus("current")
_ErrorCondIndex_Type = Counter32
_ErrorCondIndex_Object = MibTableColumn
errorCondIndex = _ErrorCondIndex_Object(
    (1, 3, 6, 1, 4, 1, 52674, 500, 5, 1, 1, 12),
    _ErrorCondIndex_Type()
)
errorCondIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    errorCondIndex.setStatus("current")
_NetBotzCameras_ObjectIdentity = ObjectIdentity
netBotzCameras = _NetBotzCameras_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52674, 500, 6)
)
_CameraTable_Object = MibTable
cameraTable = _CameraTable_Object(
    (1, 3, 6, 1, 4, 1, 52674, 500, 6, 1)
)
if mibBuilder.loadTexts:
    cameraTable.setStatus("current")
_CameraEntry_Object = MibTableRow
cameraEntry = _CameraEntry_Object(
    (1, 3, 6, 1, 4, 1, 52674, 500, 6, 1, 1)
)
cameraEntry.setIndexNames(
    (0, "NetBotz50-MIB", "cameraIndex"),
)
if mibBuilder.loadTexts:
    cameraEntry.setStatus("current")


class _CameraId_Type(DisplayString):
    """Custom type cameraId based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_CameraId_Type.__name__ = "DisplayString"
_CameraId_Object = MibTableColumn
cameraId = _CameraId_Object(
    (1, 3, 6, 1, 4, 1, 52674, 500, 6, 1, 1, 1),
    _CameraId_Type()
)
cameraId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cameraId.setStatus("current")


class _CameraVendor_Type(DisplayString):
    """Custom type cameraVendor based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_CameraVendor_Type.__name__ = "DisplayString"
_CameraVendor_Object = MibTableColumn
cameraVendor = _CameraVendor_Object(
    (1, 3, 6, 1, 4, 1, 52674, 500, 6, 1, 1, 2),
    _CameraVendor_Type()
)
cameraVendor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cameraVendor.setStatus("current")


class _CameraModel_Type(DisplayString):
    """Custom type cameraModel based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_CameraModel_Type.__name__ = "DisplayString"
_CameraModel_Object = MibTableColumn
cameraModel = _CameraModel_Object(
    (1, 3, 6, 1, 4, 1, 52674, 500, 6, 1, 1, 3),
    _CameraModel_Type()
)
cameraModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cameraModel.setStatus("current")
_CameraConnectionStatus_Type = OperStatus
_CameraConnectionStatus_Object = MibTableColumn
cameraConnectionStatus = _CameraConnectionStatus_Object(
    (1, 3, 6, 1, 4, 1, 52674, 500, 6, 1, 1, 4),
    _CameraConnectionStatus_Type()
)
cameraConnectionStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cameraConnectionStatus.setStatus("current")
_CameraErrorStatus_Type = ErrorStatus
_CameraErrorStatus_Object = MibTableColumn
cameraErrorStatus = _CameraErrorStatus_Object(
    (1, 3, 6, 1, 4, 1, 52674, 500, 6, 1, 1, 5),
    _CameraErrorStatus_Type()
)
cameraErrorStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cameraErrorStatus.setStatus("current")
_CameraLabel_Type = DisplayString
_CameraLabel_Object = MibTableColumn
cameraLabel = _CameraLabel_Object(
    (1, 3, 6, 1, 4, 1, 52674, 500, 6, 1, 1, 6),
    _CameraLabel_Type()
)
cameraLabel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cameraLabel.setStatus("current")


class _CameraAddress_Type(DisplayString):
    """Custom type cameraAddress based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_CameraAddress_Type.__name__ = "DisplayString"
_CameraAddress_Object = MibTableColumn
cameraAddress = _CameraAddress_Object(
    (1, 3, 6, 1, 4, 1, 52674, 500, 6, 1, 1, 7),
    _CameraAddress_Type()
)
cameraAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cameraAddress.setStatus("current")
_CameraIndex_Type = Counter32
_CameraIndex_Object = MibTableColumn
cameraIndex = _CameraIndex_Object(
    (1, 3, 6, 1, 4, 1, 52674, 500, 6, 1, 1, 8),
    _CameraIndex_Type()
)
cameraIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cameraIndex.setStatus("current")
_NetBotzFirmware_ObjectIdentity = ObjectIdentity
netBotzFirmware = _NetBotzFirmware_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52674, 500, 7)
)
_FirmwareTable_Object = MibTable
firmwareTable = _FirmwareTable_Object(
    (1, 3, 6, 1, 4, 1, 52674, 500, 7, 1)
)
if mibBuilder.loadTexts:
    firmwareTable.setStatus("current")
_FirmwareEntry_Object = MibTableRow
firmwareEntry = _FirmwareEntry_Object(
    (1, 3, 6, 1, 4, 1, 52674, 500, 7, 1, 1)
)
firmwareEntry.setIndexNames(
    (0, "NetBotz50-MIB", "firmwareIndex"),
)
if mibBuilder.loadTexts:
    firmwareEntry.setStatus("current")


class _FirmwareDescription_Type(DisplayString):
    """Custom type firmwareDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_FirmwareDescription_Type.__name__ = "DisplayString"
_FirmwareDescription_Object = MibTableColumn
firmwareDescription = _FirmwareDescription_Object(
    (1, 3, 6, 1, 4, 1, 52674, 500, 7, 1, 1, 1),
    _FirmwareDescription_Type()
)
firmwareDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    firmwareDescription.setStatus("current")


class _FirmwareVersion_Type(DisplayString):
    """Custom type firmwareVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_FirmwareVersion_Type.__name__ = "DisplayString"
_FirmwareVersion_Object = MibTableColumn
firmwareVersion = _FirmwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 52674, 500, 7, 1, 1, 2),
    _FirmwareVersion_Type()
)
firmwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    firmwareVersion.setStatus("current")
_FirmwareIndex_Type = Counter32
_FirmwareIndex_Object = MibTableColumn
firmwareIndex = _FirmwareIndex_Object(
    (1, 3, 6, 1, 4, 1, 52674, 500, 7, 1, 1, 3),
    _FirmwareIndex_Type()
)
firmwareIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    firmwareIndex.setStatus("current")
_NetBotzTraps_ObjectIdentity = ObjectIdentity
netBotzTraps = _NetBotzTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52674, 500, 10)
)
_NetBotzSensorTraps_ObjectIdentity = ObjectIdentity
netBotzSensorTraps = _NetBotzSensorTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52674, 500, 10, 1)
)
_NetBotzTempSensorTraps_ObjectIdentity = ObjectIdentity
netBotzTempSensorTraps = _NetBotzTempSensorTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52674, 500, 10, 1, 1)
)
_NetBotzTempSensorPrefix_ObjectIdentity = ObjectIdentity
netBotzTempSensorPrefix = _NetBotzTempSensorPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52674, 500, 10, 1, 1, 0)
)
_NetBotzHumiditySensorTraps_ObjectIdentity = ObjectIdentity
netBotzHumiditySensorTraps = _NetBotzHumiditySensorTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52674, 500, 10, 1, 2)
)
_NetBotzHumiditySensorPrefix_ObjectIdentity = ObjectIdentity
netBotzHumiditySensorPrefix = _NetBotzHumiditySensorPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52674, 500, 10, 1, 2, 0)
)
_NetBotzDewPointSensorTraps_ObjectIdentity = ObjectIdentity
netBotzDewPointSensorTraps = _NetBotzDewPointSensorTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52674, 500, 10, 1, 3)
)
_NetBotzDewPointSensorPrefix_ObjectIdentity = ObjectIdentity
netBotzDewPointSensorPrefix = _NetBotzDewPointSensorPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52674, 500, 10, 1, 3, 0)
)
_NetBotzAirFlowSensorTraps_ObjectIdentity = ObjectIdentity
netBotzAirFlowSensorTraps = _NetBotzAirFlowSensorTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52674, 500, 10, 1, 4)
)
_NetBotzAirFlowSensorPrefix_ObjectIdentity = ObjectIdentity
netBotzAirFlowSensorPrefix = _NetBotzAirFlowSensorPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52674, 500, 10, 1, 4, 0)
)
_NetBotzAmpDetectSensorTraps_ObjectIdentity = ObjectIdentity
netBotzAmpDetectSensorTraps = _NetBotzAmpDetectSensorTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52674, 500, 10, 1, 5)
)
_NetBotzAmpDetectSensorPrefix_ObjectIdentity = ObjectIdentity
netBotzAmpDetectSensorPrefix = _NetBotzAmpDetectSensorPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52674, 500, 10, 1, 5, 0)
)
_NetBotzDryContactSensorTraps_ObjectIdentity = ObjectIdentity
netBotzDryContactSensorTraps = _NetBotzDryContactSensorTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52674, 500, 10, 1, 6)
)
_NetBotzDryContactSensorPrefix_ObjectIdentity = ObjectIdentity
netBotzDryContactSensorPrefix = _NetBotzDryContactSensorPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52674, 500, 10, 1, 6, 0)
)
_NetBotzCameraMotionSensorTraps_ObjectIdentity = ObjectIdentity
netBotzCameraMotionSensorTraps = _NetBotzCameraMotionSensorTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52674, 500, 10, 1, 7)
)
_NetBotzCameraMotionSensorPrefix_ObjectIdentity = ObjectIdentity
netBotzCameraMotionSensorPrefix = _NetBotzCameraMotionSensorPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52674, 500, 10, 1, 7, 0)
)
_NetBotzDoorSensorTraps_ObjectIdentity = ObjectIdentity
netBotzDoorSensorTraps = _NetBotzDoorSensorTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52674, 500, 10, 1, 8)
)
_NetBotzDoorSensorPrefix_ObjectIdentity = ObjectIdentity
netBotzDoorSensorPrefix = _NetBotzDoorSensorPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52674, 500, 10, 1, 8, 0)
)
_NetBotzWirelessStatusSensorTraps_ObjectIdentity = ObjectIdentity
netBotzWirelessStatusSensorTraps = _NetBotzWirelessStatusSensorTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52674, 500, 10, 1, 9)
)
_NetBotzWirelessStatusSensorPrefix_ObjectIdentity = ObjectIdentity
netBotzWirelessStatusSensorPrefix = _NetBotzWirelessStatusSensorPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52674, 500, 10, 1, 9, 0)
)
_NetBotzOutputControlSensorTraps_ObjectIdentity = ObjectIdentity
netBotzOutputControlSensorTraps = _NetBotzOutputControlSensorTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52674, 500, 10, 1, 10)
)
_NetBotzOutputControlSensorPrefix_ObjectIdentity = ObjectIdentity
netBotzOutputControlSensorPrefix = _NetBotzOutputControlSensorPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52674, 500, 10, 1, 10, 0)
)
_NetBotzLoopVoltageSensorTraps_ObjectIdentity = ObjectIdentity
netBotzLoopVoltageSensorTraps = _NetBotzLoopVoltageSensorTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52674, 500, 10, 1, 11)
)
_NetBotzLoopVoltageSensorPrefix_ObjectIdentity = ObjectIdentity
netBotzLoopVoltageSensorPrefix = _NetBotzLoopVoltageSensorPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52674, 500, 10, 1, 11, 0)
)
_NetBotzSpotLeakSensorTraps_ObjectIdentity = ObjectIdentity
netBotzSpotLeakSensorTraps = _NetBotzSpotLeakSensorTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52674, 500, 10, 1, 12)
)
_NetBotzSpotLeakSensorPrefix_ObjectIdentity = ObjectIdentity
netBotzSpotLeakSensorPrefix = _NetBotzSpotLeakSensorPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52674, 500, 10, 1, 12, 0)
)
_NetBotzRopeLeakSensorTraps_ObjectIdentity = ObjectIdentity
netBotzRopeLeakSensorTraps = _NetBotzRopeLeakSensorTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52674, 500, 10, 1, 13)
)
_NetBotzRopeLeakSensorPrefix_ObjectIdentity = ObjectIdentity
netBotzRopeLeakSensorPrefix = _NetBotzRopeLeakSensorPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52674, 500, 10, 1, 13, 0)
)
_NetBotzRSSISensorTraps_ObjectIdentity = ObjectIdentity
netBotzRSSISensorTraps = _NetBotzRSSISensorTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52674, 500, 10, 1, 14)
)
_NetBotzRSSISensorPrefix_ObjectIdentity = ObjectIdentity
netBotzRSSISensorPrefix = _NetBotzRSSISensorPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52674, 500, 10, 1, 14, 0)
)
_NetBotzBatterySensorTraps_ObjectIdentity = ObjectIdentity
netBotzBatterySensorTraps = _NetBotzBatterySensorTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52674, 500, 10, 1, 15)
)
_NetBotzBatterySensorPrefix_ObjectIdentity = ObjectIdentity
netBotzBatterySensorPrefix = _NetBotzBatterySensorPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52674, 500, 10, 1, 15, 0)
)
_NetBotzOutletSensorTraps_ObjectIdentity = ObjectIdentity
netBotzOutletSensorTraps = _NetBotzOutletSensorTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52674, 500, 10, 1, 16)
)
_NetBotzOutletSensorPrefix_ObjectIdentity = ObjectIdentity
netBotzOutletSensorPrefix = _NetBotzOutletSensorPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52674, 500, 10, 1, 16, 0)
)
_NetBotzBeaconTraps_ObjectIdentity = ObjectIdentity
netBotzBeaconTraps = _NetBotzBeaconTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52674, 500, 10, 1, 17)
)
_NetBotzBeaconPrefix_ObjectIdentity = ObjectIdentity
netBotzBeaconPrefix = _NetBotzBeaconPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52674, 500, 10, 1, 17, 0)
)
_NetBotzSmokeSensorTraps_ObjectIdentity = ObjectIdentity
netBotzSmokeSensorTraps = _NetBotzSmokeSensorTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52674, 500, 10, 1, 18)
)
_NetBotzSmokeSensorPrefix_ObjectIdentity = ObjectIdentity
netBotzSmokeSensorPrefix = _NetBotzSmokeSensorPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52674, 500, 10, 1, 18, 0)
)
_NetBotzVibrationSensorTraps_ObjectIdentity = ObjectIdentity
netBotzVibrationSensorTraps = _NetBotzVibrationSensorTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52674, 500, 10, 1, 19)
)
_NetBotzVibrationSensorPrefix_ObjectIdentity = ObjectIdentity
netBotzVibrationSensorPrefix = _NetBotzVibrationSensorPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52674, 500, 10, 1, 19, 0)
)
_NetBotzRackAccessTraps_ObjectIdentity = ObjectIdentity
netBotzRackAccessTraps = _NetBotzRackAccessTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52674, 500, 10, 1, 20)
)
_NetBotzRackAccessPrefix_ObjectIdentity = ObjectIdentity
netBotzRackAccessPrefix = _NetBotzRackAccessPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52674, 500, 10, 1, 20, 0)
)
_NetBotzTestTraps_ObjectIdentity = ObjectIdentity
netBotzTestTraps = _NetBotzTestTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52674, 500, 10, 1, 99)
)
_NetBotzTestPrefix_ObjectIdentity = ObjectIdentity
netBotzTestPrefix = _NetBotzTestPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52674, 500, 10, 1, 99, 0)
)
_NetBotzPodTraps_ObjectIdentity = ObjectIdentity
netBotzPodTraps = _NetBotzPodTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52674, 500, 10, 2)
)
_NetBotzPodPrefix_ObjectIdentity = ObjectIdentity
netBotzPodPrefix = _NetBotzPodPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52674, 500, 10, 2, 0)
)
_NetBotzSensorPodTraps_ObjectIdentity = ObjectIdentity
netBotzSensorPodTraps = _NetBotzSensorPodTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52674, 500, 10, 2, 1)
)
_NetBotzSensorPodPrefix_ObjectIdentity = ObjectIdentity
netBotzSensorPodPrefix = _NetBotzSensorPodPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52674, 500, 10, 2, 1, 0)
)
_NetBotzCameraTraps_ObjectIdentity = ObjectIdentity
netBotzCameraTraps = _NetBotzCameraTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52674, 500, 10, 2, 2)
)
_NetBotzCameraPrefix_ObjectIdentity = ObjectIdentity
netBotzCameraPrefix = _NetBotzCameraPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52674, 500, 10, 2, 2, 0)
)
_NetBotz4to20mAPodTraps_ObjectIdentity = ObjectIdentity
netBotz4to20mAPodTraps = _NetBotz4to20mAPodTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52674, 500, 10, 2, 3)
)
_NetBotz4to20mAPodPrefix_ObjectIdentity = ObjectIdentity
netBotz4to20mAPodPrefix = _NetBotz4to20mAPodPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52674, 500, 10, 2, 3, 0)
)
_NetBotzRpduTraps_ObjectIdentity = ObjectIdentity
netBotzRpduTraps = _NetBotzRpduTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52674, 500, 10, 3)
)
_NetBotzRpduPrefix_ObjectIdentity = ObjectIdentity
netBotzRpduPrefix = _NetBotzRpduPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52674, 500, 10, 3, 0)
)
_NetBotzUpsTraps_ObjectIdentity = ObjectIdentity
netBotzUpsTraps = _NetBotzUpsTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52674, 500, 10, 4)
)
_NetBotzUpsPrefix_ObjectIdentity = ObjectIdentity
netBotzUpsPrefix = _NetBotzUpsPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52674, 500, 10, 4, 0)
)
_NetBotzGenericTraps_ObjectIdentity = ObjectIdentity
netBotzGenericTraps = _NetBotzGenericTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52674, 500, 10, 5)
)
_NetBotzGenericPrefix_ObjectIdentity = ObjectIdentity
netBotzGenericPrefix = _NetBotzGenericPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52674, 500, 10, 5, 0)
)
_NetBotzTrapParms_ObjectIdentity = ObjectIdentity
netBotzTrapParms = _NetBotzTrapParms_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52674, 500, 11)
)


class _NetBotzTrapErrorID_Type(DisplayString):
    """Custom type netBotzTrapErrorID based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_NetBotzTrapErrorID_Type.__name__ = "DisplayString"
_NetBotzTrapErrorID_Object = MibScalar
netBotzTrapErrorID = _NetBotzTrapErrorID_Object(
    (1, 3, 6, 1, 4, 1, 52674, 500, 11, 1),
    _NetBotzTrapErrorID_Type()
)
netBotzTrapErrorID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netBotzTrapErrorID.setStatus("current")


class _NetBotzTrapErrorType_Type(DisplayString):
    """Custom type netBotzTrapErrorType based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_NetBotzTrapErrorType_Type.__name__ = "DisplayString"
_NetBotzTrapErrorType_Object = MibScalar
netBotzTrapErrorType = _NetBotzTrapErrorType_Object(
    (1, 3, 6, 1, 4, 1, 52674, 500, 11, 2),
    _NetBotzTrapErrorType_Type()
)
netBotzTrapErrorType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netBotzTrapErrorType.setStatus("current")
_NetBotzTrapErrorTypeLabel_Type = DisplayString
_NetBotzTrapErrorTypeLabel_Object = MibScalar
netBotzTrapErrorTypeLabel = _NetBotzTrapErrorTypeLabel_Object(
    (1, 3, 6, 1, 4, 1, 52674, 500, 11, 3),
    _NetBotzTrapErrorTypeLabel_Type()
)
netBotzTrapErrorTypeLabel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netBotzTrapErrorTypeLabel.setStatus("current")


class _NetBotzTrapSensorID_Type(DisplayString):
    """Custom type netBotzTrapSensorID based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_NetBotzTrapSensorID_Type.__name__ = "DisplayString"
_NetBotzTrapSensorID_Object = MibScalar
netBotzTrapSensorID = _NetBotzTrapSensorID_Object(
    (1, 3, 6, 1, 4, 1, 52674, 500, 11, 4),
    _NetBotzTrapSensorID_Type()
)
netBotzTrapSensorID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netBotzTrapSensorID.setStatus("current")
_NetBotzTrapSensorLabel_Type = DisplayString
_NetBotzTrapSensorLabel_Object = MibScalar
netBotzTrapSensorLabel = _NetBotzTrapSensorLabel_Object(
    (1, 3, 6, 1, 4, 1, 52674, 500, 11, 5),
    _NetBotzTrapSensorLabel_Type()
)
netBotzTrapSensorLabel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netBotzTrapSensorLabel.setStatus("current")


class _NetBotzTrapContainerID_Type(DisplayString):
    """Custom type netBotzTrapContainerID based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_NetBotzTrapContainerID_Type.__name__ = "DisplayString"
_NetBotzTrapContainerID_Object = MibScalar
netBotzTrapContainerID = _NetBotzTrapContainerID_Object(
    (1, 3, 6, 1, 4, 1, 52674, 500, 11, 6),
    _NetBotzTrapContainerID_Type()
)
netBotzTrapContainerID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netBotzTrapContainerID.setStatus("current")
_NetBotzTrapContainerLabel_Type = DisplayString
_NetBotzTrapContainerLabel_Object = MibScalar
netBotzTrapContainerLabel = _NetBotzTrapContainerLabel_Object(
    (1, 3, 6, 1, 4, 1, 52674, 500, 11, 7),
    _NetBotzTrapContainerLabel_Type()
)
netBotzTrapContainerLabel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netBotzTrapContainerLabel.setStatus("current")


class _NetBotzTrapPortID_Type(DisplayString):
    """Custom type netBotzTrapPortID based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_NetBotzTrapPortID_Type.__name__ = "DisplayString"
_NetBotzTrapPortID_Object = MibScalar
netBotzTrapPortID = _NetBotzTrapPortID_Object(
    (1, 3, 6, 1, 4, 1, 52674, 500, 11, 8),
    _NetBotzTrapPortID_Type()
)
netBotzTrapPortID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netBotzTrapPortID.setStatus("current")
_NetBotzTrapPortLabel_Type = DisplayString
_NetBotzTrapPortLabel_Object = MibScalar
netBotzTrapPortLabel = _NetBotzTrapPortLabel_Object(
    (1, 3, 6, 1, 4, 1, 52674, 500, 11, 9),
    _NetBotzTrapPortLabel_Type()
)
netBotzTrapPortLabel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netBotzTrapPortLabel.setStatus("current")
_NetBotzTrapStartTime_Type = DisplayString
_NetBotzTrapStartTime_Object = MibScalar
netBotzTrapStartTime = _NetBotzTrapStartTime_Object(
    (1, 3, 6, 1, 4, 1, 52674, 500, 11, 10),
    _NetBotzTrapStartTime_Type()
)
netBotzTrapStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netBotzTrapStartTime.setStatus("current")
_NetBotzTrapNotifyTime_Type = DisplayString
_NetBotzTrapNotifyTime_Object = MibScalar
netBotzTrapNotifyTime = _NetBotzTrapNotifyTime_Object(
    (1, 3, 6, 1, 4, 1, 52674, 500, 11, 11),
    _NetBotzTrapNotifyTime_Type()
)
netBotzTrapNotifyTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netBotzTrapNotifyTime.setStatus("current")
_NetBotzTrapResolveTime_Type = DisplayString
_NetBotzTrapResolveTime_Object = MibScalar
netBotzTrapResolveTime = _NetBotzTrapResolveTime_Object(
    (1, 3, 6, 1, 4, 1, 52674, 500, 11, 12),
    _NetBotzTrapResolveTime_Type()
)
netBotzTrapResolveTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netBotzTrapResolveTime.setStatus("current")


class _NetBotzTrapSeverity_Type(Integer32):
    """Custom type netBotzTrapSeverity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("ok", 0),
          ("information", 1),
          ("warning", 2),
          ("critical", 3))
    )


_NetBotzTrapSeverity_Type.__name__ = "Integer32"
_NetBotzTrapSeverity_Object = MibScalar
netBotzTrapSeverity = _NetBotzTrapSeverity_Object(
    (1, 3, 6, 1, 4, 1, 52674, 500, 11, 13),
    _NetBotzTrapSeverity_Type()
)
netBotzTrapSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netBotzTrapSeverity.setStatus("current")
_NetBotzTrapSensorValue_Type = DisplayString
_NetBotzTrapSensorValue_Object = MibScalar
netBotzTrapSensorValue = _NetBotzTrapSensorValue_Object(
    (1, 3, 6, 1, 4, 1, 52674, 500, 11, 14),
    _NetBotzTrapSensorValue_Type()
)
netBotzTrapSensorValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netBotzTrapSensorValue.setStatus("current")
_NetBotzTrapSensorValueInt_Type = Integer32
_NetBotzTrapSensorValueInt_Object = MibScalar
netBotzTrapSensorValueInt = _NetBotzTrapSensorValueInt_Object(
    (1, 3, 6, 1, 4, 1, 52674, 500, 11, 15),
    _NetBotzTrapSensorValueInt_Type()
)
netBotzTrapSensorValueInt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netBotzTrapSensorValueInt.setStatus("current")
_NetBotzTrapSensorValueFraction_Type = Integer32
_NetBotzTrapSensorValueFraction_Object = MibScalar
netBotzTrapSensorValueFraction = _NetBotzTrapSensorValueFraction_Object(
    (1, 3, 6, 1, 4, 1, 52674, 500, 11, 16),
    _NetBotzTrapSensorValueFraction_Type()
)
netBotzTrapSensorValueFraction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netBotzTrapSensorValueFraction.setStatus("current")
_NetBotzTrapData_Type = DisplayString
_NetBotzTrapData_Object = MibScalar
netBotzTrapData = _NetBotzTrapData_Object(
    (1, 3, 6, 1, 4, 1, 52674, 500, 11, 17),
    _NetBotzTrapData_Type()
)
netBotzTrapData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netBotzTrapData.setStatus("current")
_NetBotzProducts_ObjectIdentity = ObjectIdentity
netBotzProducts = _NetBotzProducts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52674, 500, 20)
)
_NetBotzBotz_ObjectIdentity = ObjectIdentity
netBotzBotz = _NetBotzBotz_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52674, 500, 20, 10)
)
_NetBotz750Rack_ObjectIdentity = ObjectIdentity
netBotz750Rack = _NetBotz750Rack_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52674, 500, 20, 10, 3000)
)
_NetBotz755Wall_ObjectIdentity = ObjectIdentity
netBotz755Wall = _NetBotz755Wall_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52674, 500, 20, 10, 3001)
)
_NetbotzBotzGroups_ObjectIdentity = ObjectIdentity
netbotzBotzGroups = _NetbotzBotzGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52674, 500, 30)
)
_NetBotzErrorStatus_Type = ErrorStatus
_NetBotzErrorStatus_Object = MibScalar
netBotzErrorStatus = _NetBotzErrorStatus_Object(
    (1, 3, 6, 1, 4, 1, 52674, 500, 100),
    _NetBotzErrorStatus_Type()
)
netBotzErrorStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netBotzErrorStatus.setStatus("current")

# Managed Objects groups

netbotzObjectGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 52674, 500, 30, 1)
)
netbotzObjectGroup.setObjects(
      *(("NetBotz50-MIB", "netBotzErrorStatus"),
        ("NetBotz50-MIB", "otherPortId"),
        ("NetBotz50-MIB", "otherPortStatus"),
        ("NetBotz50-MIB", "otherPortLabel"),
        ("NetBotz50-MIB", "otherPortEncId"),
        ("NetBotz50-MIB", "otherPortIndex"),
        ("NetBotz50-MIB", "otherNumericSensorValue"),
        ("NetBotz50-MIB", "otherNumericSensorErrorStatus"),
        ("NetBotz50-MIB", "otherNumericSensorLabel"),
        ("NetBotz50-MIB", "otherNumericSensorEncId"),
        ("NetBotz50-MIB", "otherNumericSensorPortId"),
        ("NetBotz50-MIB", "otherNumericSensorValueStr"),
        ("NetBotz50-MIB", "otherNumericSensorValueInt"),
        ("NetBotz50-MIB", "otherNumericSensorUnits"),
        ("NetBotz50-MIB", "otherNumericSensorValueIntX1000"),
        ("NetBotz50-MIB", "otherNumericSensorValueIntX1000000"),
        ("NetBotz50-MIB", "otherNumericSensorIndex"),
        ("NetBotz50-MIB", "otherStateSensorId"),
        ("NetBotz50-MIB", "otherStateSensorValue"),
        ("NetBotz50-MIB", "otherStateSensorErrorStatus"),
        ("NetBotz50-MIB", "otherStateSensorLabel"),
        ("NetBotz50-MIB", "otherStateSensorEncId"),
        ("NetBotz50-MIB", "otherStateSensorPortId"),
        ("NetBotz50-MIB", "otherStateSensorValueStr"),
        ("NetBotz50-MIB", "otherStateSensorIndex"),
        ("NetBotz50-MIB", "otherNumericSensorId"),
        ("NetBotz50-MIB", "netBotzTrapSensorLabel"),
        ("NetBotz50-MIB", "netBotzTrapStartTime"),
        ("NetBotz50-MIB", "netBotzTrapSeverity"),
        ("NetBotz50-MIB", "netBotzTrapSensorValue"),
        ("NetBotz50-MIB", "netBotzTrapSensorValueInt"),
        ("NetBotz50-MIB", "netBotzTrapSensorValueFraction"),
        ("NetBotz50-MIB", "netBotzTrapData"),
        ("NetBotz50-MIB", "tempSensorValue"),
        ("NetBotz50-MIB", "tempSensorValueStr"),
        ("NetBotz50-MIB", "tempSensorValueInt"),
        ("NetBotz50-MIB", "tempSensorValueIntF"),
        ("NetBotz50-MIB", "tempSensorId"),
        ("NetBotz50-MIB", "tempSensorErrorStatus"),
        ("NetBotz50-MIB", "tempSensorLabel"),
        ("NetBotz50-MIB", "tempSensorEncId"),
        ("NetBotz50-MIB", "tempSensorPortId"),
        ("NetBotz50-MIB", "tempSensorIndex"),
        ("NetBotz50-MIB", "alinkSensorCountId"),
        ("NetBotz50-MIB", "alinkSensorCountValue"),
        ("NetBotz50-MIB", "alinkSensorCountLabel"),
        ("NetBotz50-MIB", "alinkSensorCountEncId"),
        ("NetBotz50-MIB", "alinkSensorCountValueStr"),
        ("NetBotz50-MIB", "alinkSensorCountValueInt"),
        ("NetBotz50-MIB", "alinkSensorCountIndex"),
        ("NetBotz50-MIB", "dewPointSensorId"),
        ("NetBotz50-MIB", "dewPointSensorValue"),
        ("NetBotz50-MIB", "dewPointSensorErrorStatus"),
        ("NetBotz50-MIB", "dewPointSensorLabel"),
        ("NetBotz50-MIB", "dewPointSensorEncId"),
        ("NetBotz50-MIB", "dewPointSensorPortId"),
        ("NetBotz50-MIB", "dewPointSensorValueStr"),
        ("NetBotz50-MIB", "dewPointSensorValueInt"),
        ("NetBotz50-MIB", "dewPointSensorValueIntF"),
        ("NetBotz50-MIB", "dewPointSensorIndex"),
        ("NetBotz50-MIB", "airFlowSensorId"),
        ("NetBotz50-MIB", "airFlowSensorValue"),
        ("NetBotz50-MIB", "airFlowSensorErrorStatus"),
        ("NetBotz50-MIB", "airFlowSensorLabel"),
        ("NetBotz50-MIB", "airFlowSensorEncId"),
        ("NetBotz50-MIB", "airFlowSensorPortId"),
        ("NetBotz50-MIB", "airFlowSensorValueStr"),
        ("NetBotz50-MIB", "airFlowSensorValueInt"),
        ("NetBotz50-MIB", "airFlowSensorIndex"),
        ("NetBotz50-MIB", "ampDetectSensorId"),
        ("NetBotz50-MIB", "ampDetectSensorValue"),
        ("NetBotz50-MIB", "ampDetectSensorErrorStatus"),
        ("NetBotz50-MIB", "ampDetectSensorLabel"),
        ("NetBotz50-MIB", "ampDetectSensorEncId"),
        ("NetBotz50-MIB", "ampDetectSensorPortId"),
        ("NetBotz50-MIB", "ampDetectSensorValueStr"),
        ("NetBotz50-MIB", "ampDetectSensorValueInt"),
        ("NetBotz50-MIB", "ampDetectSensorIndex"),
        ("NetBotz50-MIB", "cameraId"),
        ("NetBotz50-MIB", "cameraModel"),
        ("NetBotz50-MIB", "cameraVendor"),
        ("NetBotz50-MIB", "cameraConnectionStatus"),
        ("NetBotz50-MIB", "cameraErrorStatus"),
        ("NetBotz50-MIB", "cameraLabel"),
        ("NetBotz50-MIB", "cameraAddress"),
        ("NetBotz50-MIB", "cameraIndex"),
        ("NetBotz50-MIB", "cameraMotionSensorId"),
        ("NetBotz50-MIB", "cameraMotionSensorValue"),
        ("NetBotz50-MIB", "cameraMotionSensorErrorStatus"),
        ("NetBotz50-MIB", "cameraMotionSensorLabel"),
        ("NetBotz50-MIB", "cameraMotionSensorEncId"),
        ("NetBotz50-MIB", "cameraMotionSensorPortId"),
        ("NetBotz50-MIB", "cameraMotionSensorValueStr"),
        ("NetBotz50-MIB", "cameraMotionSensorIndex"),
        ("NetBotz50-MIB", "enclosureId"),
        ("NetBotz50-MIB", "enclosureStatus"),
        ("NetBotz50-MIB", "enclosureErrorStatus"),
        ("NetBotz50-MIB", "enclosureLabel"),
        ("NetBotz50-MIB", "enclosureParentEncId"),
        ("NetBotz50-MIB", "enclosureSerialNumber"),
        ("NetBotz50-MIB", "enclosureIndex"),
        ("NetBotz50-MIB", "humiSensorId"),
        ("NetBotz50-MIB", "humiSensorValue"),
        ("NetBotz50-MIB", "humiSensorErrorStatus"),
        ("NetBotz50-MIB", "humiSensorLabel"),
        ("NetBotz50-MIB", "humiSensorEncId"),
        ("NetBotz50-MIB", "humiSensorPortId"),
        ("NetBotz50-MIB", "humiSensorValueStr"),
        ("NetBotz50-MIB", "humiSensorValueInt"),
        ("NetBotz50-MIB", "humiSensorIndex"),
        ("NetBotz50-MIB", "dryContactSensorId"),
        ("NetBotz50-MIB", "dryContactSensorErrorStatus"),
        ("NetBotz50-MIB", "dryContactSensorLabel"),
        ("NetBotz50-MIB", "dryContactSensorEncId"),
        ("NetBotz50-MIB", "dryContactSensorPortId"),
        ("NetBotz50-MIB", "dryContactSensorValueStr"),
        ("NetBotz50-MIB", "dryContactSensorIndex"),
        ("NetBotz50-MIB", "dryContactSensorValue"),
        ("NetBotz50-MIB", "doorSwitchSensorId"),
        ("NetBotz50-MIB", "doorSwitchSensorValue"),
        ("NetBotz50-MIB", "doorSwitchSensorErrorStatus"),
        ("NetBotz50-MIB", "doorSwitchSensorLabel"),
        ("NetBotz50-MIB", "doorSwitchSensorEncId"),
        ("NetBotz50-MIB", "doorSwitchSensorPortId"),
        ("NetBotz50-MIB", "doorSwitchSensorValueStr"),
        ("NetBotz50-MIB", "doorSwitchSensorIndex"),
        ("NetBotz50-MIB", "vibrationSensorId"),
        ("NetBotz50-MIB", "vibrationSensorValue"),
        ("NetBotz50-MIB", "vibrationSensorErrorStatus"),
        ("NetBotz50-MIB", "vibrationSensorLabel"),
        ("NetBotz50-MIB", "vibrationSensorEncId"),
        ("NetBotz50-MIB", "vibrationSensorPortId"),
        ("NetBotz50-MIB", "vibrationSensorValueStr"),
        ("NetBotz50-MIB", "vibrationSensorIndex"),
        ("NetBotz50-MIB", "smokeSensorId"),
        ("NetBotz50-MIB", "smokeSensorValue"),
        ("NetBotz50-MIB", "smokeSensorErrorStatus"),
        ("NetBotz50-MIB", "smokeSensorLabel"),
        ("NetBotz50-MIB", "smokeSensorEncId"),
        ("NetBotz50-MIB", "smokeSensorPortId"),
        ("NetBotz50-MIB", "smokeSensorValueStr"),
        ("NetBotz50-MIB", "smokeSensorIndex"),
        ("NetBotz50-MIB", "leakSensorId"),
        ("NetBotz50-MIB", "leakSensorValue"),
        ("NetBotz50-MIB", "leakSensorErrorStatus"),
        ("NetBotz50-MIB", "leakSensorLabel"),
        ("NetBotz50-MIB", "leakSensorEncId"),
        ("NetBotz50-MIB", "leakSensorPortId"),
        ("NetBotz50-MIB", "leakSensorValueStr"),
        ("NetBotz50-MIB", "leakSensorIndex"),
        ("NetBotz50-MIB", "beaconId"),
        ("NetBotz50-MIB", "beaconValue"),
        ("NetBotz50-MIB", "beaconErrorStatus"),
        ("NetBotz50-MIB", "beaconLabel"),
        ("NetBotz50-MIB", "beaconEncId"),
        ("NetBotz50-MIB", "beaconPortId"),
        ("NetBotz50-MIB", "beaconValueStr"),
        ("NetBotz50-MIB", "beaconIndex"),
        ("NetBotz50-MIB", "switchedOutletId"),
        ("NetBotz50-MIB", "switchedOutletValue"),
        ("NetBotz50-MIB", "switchedOutletErrorStatus"),
        ("NetBotz50-MIB", "switchedOutletLabel"),
        ("NetBotz50-MIB", "switchedOutletEncId"),
        ("NetBotz50-MIB", "switchedOutletPortId"),
        ("NetBotz50-MIB", "switchedOutletValueStr"),
        ("NetBotz50-MIB", "switchedOutletIndex"),
        ("NetBotz50-MIB", "doorLockSensorId"),
        ("NetBotz50-MIB", "doorLockSensorValue"),
        ("NetBotz50-MIB", "doorLockSensorErrorStatus"),
        ("NetBotz50-MIB", "doorLockSensorLabel"),
        ("NetBotz50-MIB", "doorLockSensorEncId"),
        ("NetBotz50-MIB", "doorLockSensorPortId"),
        ("NetBotz50-MIB", "doorLockSensorValueStr"),
        ("NetBotz50-MIB", "doorLockSensorIndex"),
        ("NetBotz50-MIB", "rackHandleSensorId"),
        ("NetBotz50-MIB", "rackHandleSensorValue"),
        ("NetBotz50-MIB", "rackHandleSensorErrorStatus"),
        ("NetBotz50-MIB", "rackHandleSensorLabel"),
        ("NetBotz50-MIB", "rackHandleSensorEncId"),
        ("NetBotz50-MIB", "rackHandleSensorPortId"),
        ("NetBotz50-MIB", "rackHandleSensorValueStr"),
        ("NetBotz50-MIB", "rackHandleSensorIndex"),
        ("NetBotz50-MIB", "outputRelaySensorId"),
        ("NetBotz50-MIB", "outputRelaySensorValue"),
        ("NetBotz50-MIB", "outputRelaySensorErrorStatus"),
        ("NetBotz50-MIB", "outputRelaySensorLabel"),
        ("NetBotz50-MIB", "outputRelaySensorEncId"),
        ("NetBotz50-MIB", "outputRelaySensorPortId"),
        ("NetBotz50-MIB", "outputRelaySensorValueStr"),
        ("NetBotz50-MIB", "outputRelaySensorIndex"),
        ("NetBotz50-MIB", "rssiSensorId"),
        ("NetBotz50-MIB", "rssiSensorValue"),
        ("NetBotz50-MIB", "rssiSensorErrorStatus"),
        ("NetBotz50-MIB", "rssiSensorLabel"),
        ("NetBotz50-MIB", "rssiSensorEncId"),
        ("NetBotz50-MIB", "rssiSensorPortId"),
        ("NetBotz50-MIB", "rssiSensorValueStr"),
        ("NetBotz50-MIB", "rssiSensorValueInt"),
        ("NetBotz50-MIB", "rssiSensorUnits"),
        ("NetBotz50-MIB", "rssiSensorIndex"),
        ("NetBotz50-MIB", "currentInputSensorId"),
        ("NetBotz50-MIB", "currentInputSensorValue"),
        ("NetBotz50-MIB", "currentInputSensorErrorStatus"),
        ("NetBotz50-MIB", "currentInputSensorLabel"),
        ("NetBotz50-MIB", "currentInputSensorEncId"),
        ("NetBotz50-MIB", "currentInputSensorPortId"),
        ("NetBotz50-MIB", "currentInputSensorValueStr"),
        ("NetBotz50-MIB", "currentInputSensorValueInt"),
        ("NetBotz50-MIB", "currentInputSensorUnits"),
        ("NetBotz50-MIB", "currentInputSensorValueIntX1000"),
        ("NetBotz50-MIB", "currentInputSensorValueIntX1000000"),
        ("NetBotz50-MIB", "currentInputSensorIndex"),
        ("NetBotz50-MIB", "voltageSensorId"),
        ("NetBotz50-MIB", "voltageSensorValue"),
        ("NetBotz50-MIB", "voltageSensorErrorStatus"),
        ("NetBotz50-MIB", "voltageSensorLabel"),
        ("NetBotz50-MIB", "voltageSensorEncId"),
        ("NetBotz50-MIB", "voltageSensorPortId"),
        ("NetBotz50-MIB", "voltageSensorValueStr"),
        ("NetBotz50-MIB", "voltageSensorValueInt"),
        ("NetBotz50-MIB", "voltageSensorUnits"),
        ("NetBotz50-MIB", "voltageSensorValueIntX1000"),
        ("NetBotz50-MIB", "voltageSensorValueIntX1000000"),
        ("NetBotz50-MIB", "voltageSensorIndex"),
        ("NetBotz50-MIB", "batterySensorId"),
        ("NetBotz50-MIB", "batterySensorValue"),
        ("NetBotz50-MIB", "batterySensorErrorStatus"),
        ("NetBotz50-MIB", "batterySensorLabel"),
        ("NetBotz50-MIB", "batterySensorEncId"),
        ("NetBotz50-MIB", "batterySensorPortId"),
        ("NetBotz50-MIB", "batterySensorValueStr"),
        ("NetBotz50-MIB", "batterySensorValueInt"),
        ("NetBotz50-MIB", "batterySensorUnits"),
        ("NetBotz50-MIB", "batterySensorValueIntX1000"),
        ("NetBotz50-MIB", "batterySensorValueIntX1000000"),
        ("NetBotz50-MIB", "batterySensorIndex"),
        ("NetBotz50-MIB", "errorCondId"),
        ("NetBotz50-MIB", "errorCondSeverity"),
        ("NetBotz50-MIB", "errorCondTypeId"),
        ("NetBotz50-MIB", "errorCondStartTime"),
        ("NetBotz50-MIB", "errorCondStartTimeStr"),
        ("NetBotz50-MIB", "errorCondResolved"),
        ("NetBotz50-MIB", "errorCondResolvedTime"),
        ("NetBotz50-MIB", "errorCondResolvedTimeStr"),
        ("NetBotz50-MIB", "errorCondEncId"),
        ("NetBotz50-MIB", "errorCondPortId"),
        ("NetBotz50-MIB", "errorCondSensorId"),
        ("NetBotz50-MIB", "errorCondIndex"),
        ("NetBotz50-MIB", "netBotzTrapErrorID"),
        ("NetBotz50-MIB", "netBotzTrapErrorType"),
        ("NetBotz50-MIB", "netBotzTrapErrorTypeLabel"),
        ("NetBotz50-MIB", "netBotzTrapSensorID"),
        ("NetBotz50-MIB", "netBotzTrapContainerID"),
        ("NetBotz50-MIB", "netBotzTrapContainerLabel"),
        ("NetBotz50-MIB", "netBotzTrapPortID"),
        ("NetBotz50-MIB", "netBotzTrapPortLabel"),
        ("NetBotz50-MIB", "netBotzTrapNotifyTime"),
        ("NetBotz50-MIB", "netBotzTrapResolveTime"),
        ("NetBotz50-MIB", "firmwareDescription"),
        ("NetBotz50-MIB", "firmwareVersion"),
        ("NetBotz50-MIB", "firmwareIndex"))
)
if mibBuilder.loadTexts:
    netbotzObjectGroup.setStatus("current")


# Notification objects

netBotzTempError = NotificationType(
    (1, 3, 6, 1, 4, 1, 52674, 500, 10, 1, 1, 0, 1)
)
netBotzTempError.setObjects(
      *(("NetBotz50-MIB", "netBotzTrapErrorID"),
        ("NetBotz50-MIB", "netBotzTrapErrorType"),
        ("NetBotz50-MIB", "netBotzTrapErrorTypeLabel"),
        ("NetBotz50-MIB", "netBotzTrapSensorID"),
        ("NetBotz50-MIB", "netBotzTrapSensorLabel"),
        ("NetBotz50-MIB", "netBotzTrapContainerID"),
        ("NetBotz50-MIB", "netBotzTrapContainerLabel"),
        ("NetBotz50-MIB", "netBotzTrapPortID"),
        ("NetBotz50-MIB", "netBotzTrapPortLabel"),
        ("NetBotz50-MIB", "netBotzTrapStartTime"),
        ("NetBotz50-MIB", "netBotzTrapNotifyTime"),
        ("NetBotz50-MIB", "netBotzTrapResolveTime"),
        ("NetBotz50-MIB", "netBotzTrapSeverity"),
        ("NetBotz50-MIB", "netBotzTrapSensorValue"),
        ("NetBotz50-MIB", "netBotzTrapSensorValueInt"),
        ("NetBotz50-MIB", "netBotzTrapSensorValueFraction"))
)
if mibBuilder.loadTexts:
    netBotzTempError.setStatus(
        "current"
    )

netBotzTempTooHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 52674, 500, 10, 1, 1, 0, 2)
)
netBotzTempTooHigh.setObjects(
      *(("NetBotz50-MIB", "netBotzTrapErrorID"),
        ("NetBotz50-MIB", "netBotzTrapErrorType"),
        ("NetBotz50-MIB", "netBotzTrapErrorTypeLabel"),
        ("NetBotz50-MIB", "netBotzTrapSensorID"),
        ("NetBotz50-MIB", "netBotzTrapSensorLabel"),
        ("NetBotz50-MIB", "netBotzTrapContainerID"),
        ("NetBotz50-MIB", "netBotzTrapContainerLabel"),
        ("NetBotz50-MIB", "netBotzTrapPortID"),
        ("NetBotz50-MIB", "netBotzTrapPortLabel"),
        ("NetBotz50-MIB", "netBotzTrapStartTime"),
        ("NetBotz50-MIB", "netBotzTrapNotifyTime"),
        ("NetBotz50-MIB", "netBotzTrapResolveTime"),
        ("NetBotz50-MIB", "netBotzTrapSeverity"),
        ("NetBotz50-MIB", "netBotzTrapSensorValue"),
        ("NetBotz50-MIB", "netBotzTrapSensorValueInt"),
        ("NetBotz50-MIB", "netBotzTrapSensorValueFraction"))
)
if mibBuilder.loadTexts:
    netBotzTempTooHigh.setStatus(
        "current"
    )

netBotzTempTooLow = NotificationType(
    (1, 3, 6, 1, 4, 1, 52674, 500, 10, 1, 1, 0, 3)
)
netBotzTempTooLow.setObjects(
      *(("NetBotz50-MIB", "netBotzTrapErrorID"),
        ("NetBotz50-MIB", "netBotzTrapErrorType"),
        ("NetBotz50-MIB", "netBotzTrapErrorTypeLabel"),
        ("NetBotz50-MIB", "netBotzTrapSensorID"),
        ("NetBotz50-MIB", "netBotzTrapSensorLabel"),
        ("NetBotz50-MIB", "netBotzTrapContainerID"),
        ("NetBotz50-MIB", "netBotzTrapContainerLabel"),
        ("NetBotz50-MIB", "netBotzTrapPortID"),
        ("NetBotz50-MIB", "netBotzTrapPortLabel"),
        ("NetBotz50-MIB", "netBotzTrapStartTime"),
        ("NetBotz50-MIB", "netBotzTrapNotifyTime"),
        ("NetBotz50-MIB", "netBotzTrapResolveTime"),
        ("NetBotz50-MIB", "netBotzTrapSeverity"),
        ("NetBotz50-MIB", "netBotzTrapSensorValue"),
        ("NetBotz50-MIB", "netBotzTrapSensorValueInt"),
        ("NetBotz50-MIB", "netBotzTrapSensorValueFraction"))
)
if mibBuilder.loadTexts:
    netBotzTempTooLow.setStatus(
        "current"
    )

netBotzTempUnplugged = NotificationType(
    (1, 3, 6, 1, 4, 1, 52674, 500, 10, 1, 1, 0, 6)
)
netBotzTempUnplugged.setObjects(
      *(("NetBotz50-MIB", "netBotzTrapErrorID"),
        ("NetBotz50-MIB", "netBotzTrapErrorType"),
        ("NetBotz50-MIB", "netBotzTrapErrorTypeLabel"),
        ("NetBotz50-MIB", "netBotzTrapSensorID"),
        ("NetBotz50-MIB", "netBotzTrapSensorLabel"),
        ("NetBotz50-MIB", "netBotzTrapContainerID"),
        ("NetBotz50-MIB", "netBotzTrapContainerLabel"),
        ("NetBotz50-MIB", "netBotzTrapPortID"),
        ("NetBotz50-MIB", "netBotzTrapPortLabel"),
        ("NetBotz50-MIB", "netBotzTrapStartTime"),
        ("NetBotz50-MIB", "netBotzTrapNotifyTime"),
        ("NetBotz50-MIB", "netBotzTrapResolveTime"),
        ("NetBotz50-MIB", "netBotzTrapSeverity"),
        ("NetBotz50-MIB", "netBotzTrapSensorValue"),
        ("NetBotz50-MIB", "netBotzTrapSensorValueInt"),
        ("NetBotz50-MIB", "netBotzTrapSensorValueFraction"))
)
if mibBuilder.loadTexts:
    netBotzTempUnplugged.setStatus(
        "current"
    )

netBotzTempErrorRTN = NotificationType(
    (1, 3, 6, 1, 4, 1, 52674, 500, 10, 1, 1, 0, 101)
)
netBotzTempErrorRTN.setObjects(
      *(("NetBotz50-MIB", "netBotzTrapErrorID"),
        ("NetBotz50-MIB", "netBotzTrapErrorType"),
        ("NetBotz50-MIB", "netBotzTrapErrorTypeLabel"),
        ("NetBotz50-MIB", "netBotzTrapSensorID"),
        ("NetBotz50-MIB", "netBotzTrapSensorLabel"),
        ("NetBotz50-MIB", "netBotzTrapContainerID"),
        ("NetBotz50-MIB", "netBotzTrapContainerLabel"),
        ("NetBotz50-MIB", "netBotzTrapPortID"),
        ("NetBotz50-MIB", "netBotzTrapPortLabel"),
        ("NetBotz50-MIB", "netBotzTrapStartTime"),
        ("NetBotz50-MIB", "netBotzTrapNotifyTime"),
        ("NetBotz50-MIB", "netBotzTrapResolveTime"),
        ("NetBotz50-MIB", "netBotzTrapSeverity"),
        ("NetBotz50-MIB", "netBotzTrapSensorValue"),
        ("NetBotz50-MIB", "netBotzTrapSensorValueInt"),
        ("NetBotz50-MIB", "netBotzTrapSensorValueFraction"))
)
if mibBuilder.loadTexts:
    netBotzTempErrorRTN.setStatus(
        "current"
    )

netBotzTempTooHighRTN = NotificationType(
    (1, 3, 6, 1, 4, 1, 52674, 500, 10, 1, 1, 0, 102)
)
netBotzTempTooHighRTN.setObjects(
      *(("NetBotz50-MIB", "netBotzTrapErrorID"),
        ("NetBotz50-MIB", "netBotzTrapErrorType"),
        ("NetBotz50-MIB", "netBotzTrapErrorTypeLabel"),
        ("NetBotz50-MIB", "netBotzTrapSensorID"),
        ("NetBotz50-MIB", "netBotzTrapSensorLabel"),
        ("NetBotz50-MIB", "netBotzTrapContainerID"),
        ("NetBotz50-MIB", "netBotzTrapContainerLabel"),
        ("NetBotz50-MIB", "netBotzTrapPortID"),
        ("NetBotz50-MIB", "netBotzTrapPortLabel"),
        ("NetBotz50-MIB", "netBotzTrapStartTime"),
        ("NetBotz50-MIB", "netBotzTrapNotifyTime"),
        ("NetBotz50-MIB", "netBotzTrapResolveTime"),
        ("NetBotz50-MIB", "netBotzTrapSeverity"),
        ("NetBotz50-MIB", "netBotzTrapSensorValue"),
        ("NetBotz50-MIB", "netBotzTrapSensorValueInt"),
        ("NetBotz50-MIB", "netBotzTrapSensorValueFraction"))
)
if mibBuilder.loadTexts:
    netBotzTempTooHighRTN.setStatus(
        "current"
    )

netBotzTempTooLowRTN = NotificationType(
    (1, 3, 6, 1, 4, 1, 52674, 500, 10, 1, 1, 0, 103)
)
netBotzTempTooLowRTN.setObjects(
      *(("NetBotz50-MIB", "netBotzTrapErrorID"),
        ("NetBotz50-MIB", "netBotzTrapErrorType"),
        ("NetBotz50-MIB", "netBotzTrapErrorTypeLabel"),
        ("NetBotz50-MIB", "netBotzTrapSensorID"),
        ("NetBotz50-MIB", "netBotzTrapSensorLabel"),
        ("NetBotz50-MIB", "netBotzTrapContainerID"),
        ("NetBotz50-MIB", "netBotzTrapContainerLabel"),
        ("NetBotz50-MIB", "netBotzTrapPortID"),
        ("NetBotz50-MIB", "netBotzTrapPortLabel"),
        ("NetBotz50-MIB", "netBotzTrapStartTime"),
        ("NetBotz50-MIB", "netBotzTrapNotifyTime"),
        ("NetBotz50-MIB", "netBotzTrapResolveTime"),
        ("NetBotz50-MIB", "netBotzTrapSeverity"),
        ("NetBotz50-MIB", "netBotzTrapSensorValue"),
        ("NetBotz50-MIB", "netBotzTrapSensorValueInt"),
        ("NetBotz50-MIB", "netBotzTrapSensorValueFraction"))
)
if mibBuilder.loadTexts:
    netBotzTempTooLowRTN.setStatus(
        "current"
    )

netBotzTempReplugged = NotificationType(
    (1, 3, 6, 1, 4, 1, 52674, 500, 10, 1, 1, 0, 106)
)
netBotzTempReplugged.setObjects(
      *(("NetBotz50-MIB", "netBotzTrapErrorID"),
        ("NetBotz50-MIB", "netBotzTrapErrorType"),
        ("NetBotz50-MIB", "netBotzTrapErrorTypeLabel"),
        ("NetBotz50-MIB", "netBotzTrapSensorID"),
        ("NetBotz50-MIB", "netBotzTrapSensorLabel"),
        ("NetBotz50-MIB", "netBotzTrapContainerID"),
        ("NetBotz50-MIB", "netBotzTrapContainerLabel"),
        ("NetBotz50-MIB", "netBotzTrapPortID"),
        ("NetBotz50-MIB", "netBotzTrapPortLabel"),
        ("NetBotz50-MIB", "netBotzTrapStartTime"),
        ("NetBotz50-MIB", "netBotzTrapNotifyTime"),
        ("NetBotz50-MIB", "netBotzTrapResolveTime"),
        ("NetBotz50-MIB", "netBotzTrapSeverity"),
        ("NetBotz50-MIB", "netBotzTrapSensorValue"),
        ("NetBotz50-MIB", "netBotzTrapSensorValueInt"),
        ("NetBotz50-MIB", "netBotzTrapSensorValueFraction"))
)
if mibBuilder.loadTexts:
    netBotzTempReplugged.setStatus(
        "current"
    )

netBotzHumidityError = NotificationType(
    (1, 3, 6, 1, 4, 1, 52674, 500, 10, 1, 2, 0, 1)
)
netBotzHumidityError.setObjects(
      *(("NetBotz50-MIB", "netBotzTrapErrorID"),
        ("NetBotz50-MIB", "netBotzTrapErrorType"),
        ("NetBotz50-MIB", "netBotzTrapErrorTypeLabel"),
        ("NetBotz50-MIB", "netBotzTrapSensorID"),
        ("NetBotz50-MIB", "netBotzTrapSensorLabel"),
        ("NetBotz50-MIB", "netBotzTrapContainerID"),
        ("NetBotz50-MIB", "netBotzTrapContainerLabel"),
        ("NetBotz50-MIB", "netBotzTrapPortID"),
        ("NetBotz50-MIB", "netBotzTrapPortLabel"),
        ("NetBotz50-MIB", "netBotzTrapStartTime"),
        ("NetBotz50-MIB", "netBotzTrapNotifyTime"),
        ("NetBotz50-MIB", "netBotzTrapResolveTime"),
        ("NetBotz50-MIB", "netBotzTrapSeverity"),
        ("NetBotz50-MIB", "netBotzTrapSensorValue"),
        ("NetBotz50-MIB", "netBotzTrapSensorValueInt"),
        ("NetBotz50-MIB", "netBotzTrapSensorValueFraction"))
)
if mibBuilder.loadTexts:
    netBotzHumidityError.setStatus(
        "current"
    )

netBotzHumidityTooHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 52674, 500, 10, 1, 2, 0, 2)
)
netBotzHumidityTooHigh.setObjects(
      *(("NetBotz50-MIB", "netBotzTrapErrorID"),
        ("NetBotz50-MIB", "netBotzTrapErrorType"),
        ("NetBotz50-MIB", "netBotzTrapErrorTypeLabel"),
        ("NetBotz50-MIB", "netBotzTrapSensorID"),
        ("NetBotz50-MIB", "netBotzTrapSensorLabel"),
        ("NetBotz50-MIB", "netBotzTrapContainerID"),
        ("NetBotz50-MIB", "netBotzTrapContainerLabel"),
        ("NetBotz50-MIB", "netBotzTrapPortID"),
        ("NetBotz50-MIB", "netBotzTrapPortLabel"),
        ("NetBotz50-MIB", "netBotzTrapStartTime"),
        ("NetBotz50-MIB", "netBotzTrapNotifyTime"),
        ("NetBotz50-MIB", "netBotzTrapResolveTime"),
        ("NetBotz50-MIB", "netBotzTrapSeverity"),
        ("NetBotz50-MIB", "netBotzTrapSensorValue"),
        ("NetBotz50-MIB", "netBotzTrapSensorValueInt"),
        ("NetBotz50-MIB", "netBotzTrapSensorValueFraction"))
)
if mibBuilder.loadTexts:
    netBotzHumidityTooHigh.setStatus(
        "current"
    )

netBotzHumidityTooLow = NotificationType(
    (1, 3, 6, 1, 4, 1, 52674, 500, 10, 1, 2, 0, 3)
)
netBotzHumidityTooLow.setObjects(
      *(("NetBotz50-MIB", "netBotzTrapErrorID"),
        ("NetBotz50-MIB", "netBotzTrapErrorType"),
        ("NetBotz50-MIB", "netBotzTrapErrorTypeLabel"),
        ("NetBotz50-MIB", "netBotzTrapSensorID"),
        ("NetBotz50-MIB", "netBotzTrapSensorLabel"),
        ("NetBotz50-MIB", "netBotzTrapContainerID"),
        ("NetBotz50-MIB", "netBotzTrapContainerLabel"),
        ("NetBotz50-MIB", "netBotzTrapPortID"),
        ("NetBotz50-MIB", "netBotzTrapPortLabel"),
        ("NetBotz50-MIB", "netBotzTrapStartTime"),
        ("NetBotz50-MIB", "netBotzTrapNotifyTime"),
        ("NetBotz50-MIB", "netBotzTrapResolveTime"),
        ("NetBotz50-MIB", "netBotzTrapSeverity"),
        ("NetBotz50-MIB", "netBotzTrapSensorValue"),
        ("NetBotz50-MIB", "netBotzTrapSensorValueInt"),
        ("NetBotz50-MIB", "netBotzTrapSensorValueFraction"))
)
if mibBuilder.loadTexts:
    netBotzHumidityTooLow.setStatus(
        "current"
    )

netBotzHumidityUnplugged = NotificationType(
    (1, 3, 6, 1, 4, 1, 52674, 500, 10, 1, 2, 0, 6)
)
netBotzHumidityUnplugged.setObjects(
      *(("NetBotz50-MIB", "netBotzTrapErrorID"),
        ("NetBotz50-MIB", "netBotzTrapErrorType"),
        ("NetBotz50-MIB", "netBotzTrapErrorTypeLabel"),
        ("NetBotz50-MIB", "netBotzTrapSensorID"),
        ("NetBotz50-MIB", "netBotzTrapSensorLabel"),
        ("NetBotz50-MIB", "netBotzTrapContainerID"),
        ("NetBotz50-MIB", "netBotzTrapContainerLabel"),
        ("NetBotz50-MIB", "netBotzTrapPortID"),
        ("NetBotz50-MIB", "netBotzTrapPortLabel"),
        ("NetBotz50-MIB", "netBotzTrapStartTime"),
        ("NetBotz50-MIB", "netBotzTrapNotifyTime"),
        ("NetBotz50-MIB", "netBotzTrapResolveTime"),
        ("NetBotz50-MIB", "netBotzTrapSeverity"),
        ("NetBotz50-MIB", "netBotzTrapSensorValue"),
        ("NetBotz50-MIB", "netBotzTrapSensorValueInt"),
        ("NetBotz50-MIB", "netBotzTrapSensorValueFraction"))
)
if mibBuilder.loadTexts:
    netBotzHumidityUnplugged.setStatus(
        "current"
    )

netBotzHumidityErrorRTN = NotificationType(
    (1, 3, 6, 1, 4, 1, 52674, 500, 10, 1, 2, 0, 101)
)
netBotzHumidityErrorRTN.setObjects(
      *(("NetBotz50-MIB", "netBotzTrapErrorID"),
        ("NetBotz50-MIB", "netBotzTrapErrorType"),
        ("NetBotz50-MIB", "netBotzTrapErrorTypeLabel"),
        ("NetBotz50-MIB", "netBotzTrapSensorID"),
        ("NetBotz50-MIB", "netBotzTrapSensorLabel"),
        ("NetBotz50-MIB", "netBotzTrapContainerID"),
        ("NetBotz50-MIB", "netBotzTrapContainerLabel"),
        ("NetBotz50-MIB", "netBotzTrapPortID"),
        ("NetBotz50-MIB", "netBotzTrapPortLabel"),
        ("NetBotz50-MIB", "netBotzTrapStartTime"),
        ("NetBotz50-MIB", "netBotzTrapNotifyTime"),
        ("NetBotz50-MIB", "netBotzTrapResolveTime"),
        ("NetBotz50-MIB", "netBotzTrapSeverity"),
        ("NetBotz50-MIB", "netBotzTrapSensorValue"),
        ("NetBotz50-MIB", "netBotzTrapSensorValueInt"),
        ("NetBotz50-MIB", "netBotzTrapSensorValueFraction"))
)
if mibBuilder.loadTexts:
    netBotzHumidityErrorRTN.setStatus(
        "current"
    )

netBotzHumidityTooHighRTN = NotificationType(
    (1, 3, 6, 1, 4, 1, 52674, 500, 10, 1, 2, 0, 102)
)
netBotzHumidityTooHighRTN.setObjects(
      *(("NetBotz50-MIB", "netBotzTrapErrorID"),
        ("NetBotz50-MIB", "netBotzTrapErrorType"),
        ("NetBotz50-MIB", "netBotzTrapErrorTypeLabel"),
        ("NetBotz50-MIB", "netBotzTrapSensorID"),
        ("NetBotz50-MIB", "netBotzTrapSensorLabel"),
        ("NetBotz50-MIB", "netBotzTrapContainerID"),
        ("NetBotz50-MIB", "netBotzTrapContainerLabel"),
        ("NetBotz50-MIB", "netBotzTrapPortID"),
        ("NetBotz50-MIB", "netBotzTrapPortLabel"),
        ("NetBotz50-MIB", "netBotzTrapStartTime"),
        ("NetBotz50-MIB", "netBotzTrapNotifyTime"),
        ("NetBotz50-MIB", "netBotzTrapResolveTime"),
        ("NetBotz50-MIB", "netBotzTrapSeverity"),
        ("NetBotz50-MIB", "netBotzTrapSensorValue"),
        ("NetBotz50-MIB", "netBotzTrapSensorValueInt"),
        ("NetBotz50-MIB", "netBotzTrapSensorValueFraction"))
)
if mibBuilder.loadTexts:
    netBotzHumidityTooHighRTN.setStatus(
        "current"
    )

netBotzHumidityTooLowRTN = NotificationType(
    (1, 3, 6, 1, 4, 1, 52674, 500, 10, 1, 2, 0, 103)
)
netBotzHumidityTooLowRTN.setObjects(
      *(("NetBotz50-MIB", "netBotzTrapErrorID"),
        ("NetBotz50-MIB", "netBotzTrapErrorType"),
        ("NetBotz50-MIB", "netBotzTrapErrorTypeLabel"),
        ("NetBotz50-MIB", "netBotzTrapSensorID"),
        ("NetBotz50-MIB", "netBotzTrapSensorLabel"),
        ("NetBotz50-MIB", "netBotzTrapContainerID"),
        ("NetBotz50-MIB", "netBotzTrapContainerLabel"),
        ("NetBotz50-MIB", "netBotzTrapPortID"),
        ("NetBotz50-MIB", "netBotzTrapPortLabel"),
        ("NetBotz50-MIB", "netBotzTrapStartTime"),
        ("NetBotz50-MIB", "netBotzTrapNotifyTime"),
        ("NetBotz50-MIB", "netBotzTrapResolveTime"),
        ("NetBotz50-MIB", "netBotzTrapSeverity"),
        ("NetBotz50-MIB", "netBotzTrapSensorValue"),
        ("NetBotz50-MIB", "netBotzTrapSensorValueInt"),
        ("NetBotz50-MIB", "netBotzTrapSensorValueFraction"))
)
if mibBuilder.loadTexts:
    netBotzHumidityTooLowRTN.setStatus(
        "current"
    )

netBotzHumidityReplugged = NotificationType(
    (1, 3, 6, 1, 4, 1, 52674, 500, 10, 1, 2, 0, 106)
)
netBotzHumidityReplugged.setObjects(
      *(("NetBotz50-MIB", "netBotzTrapErrorID"),
        ("NetBotz50-MIB", "netBotzTrapErrorType"),
        ("NetBotz50-MIB", "netBotzTrapErrorTypeLabel"),
        ("NetBotz50-MIB", "netBotzTrapSensorID"),
        ("NetBotz50-MIB", "netBotzTrapSensorLabel"),
        ("NetBotz50-MIB", "netBotzTrapContainerID"),
        ("NetBotz50-MIB", "netBotzTrapContainerLabel"),
        ("NetBotz50-MIB", "netBotzTrapPortID"),
        ("NetBotz50-MIB", "netBotzTrapPortLabel"),
        ("NetBotz50-MIB", "netBotzTrapStartTime"),
        ("NetBotz50-MIB", "netBotzTrapNotifyTime"),
        ("NetBotz50-MIB", "netBotzTrapResolveTime"),
        ("NetBotz50-MIB", "netBotzTrapSeverity"),
        ("NetBotz50-MIB", "netBotzTrapSensorValue"),
        ("NetBotz50-MIB", "netBotzTrapSensorValueInt"),
        ("NetBotz50-MIB", "netBotzTrapSensorValueFraction"))
)
if mibBuilder.loadTexts:
    netBotzHumidityReplugged.setStatus(
        "current"
    )

netBotzDewPointError = NotificationType(
    (1, 3, 6, 1, 4, 1, 52674, 500, 10, 1, 3, 0, 1)
)
netBotzDewPointError.setObjects(
      *(("NetBotz50-MIB", "netBotzTrapErrorID"),
        ("NetBotz50-MIB", "netBotzTrapErrorType"),
        ("NetBotz50-MIB", "netBotzTrapErrorTypeLabel"),
        ("NetBotz50-MIB", "netBotzTrapSensorID"),
        ("NetBotz50-MIB", "netBotzTrapSensorLabel"),
        ("NetBotz50-MIB", "netBotzTrapContainerID"),
        ("NetBotz50-MIB", "netBotzTrapContainerLabel"),
        ("NetBotz50-MIB", "netBotzTrapPortID"),
        ("NetBotz50-MIB", "netBotzTrapPortLabel"),
        ("NetBotz50-MIB", "netBotzTrapStartTime"),
        ("NetBotz50-MIB", "netBotzTrapNotifyTime"),
        ("NetBotz50-MIB", "netBotzTrapResolveTime"),
        ("NetBotz50-MIB", "netBotzTrapSeverity"),
        ("NetBotz50-MIB", "netBotzTrapSensorValue"),
        ("NetBotz50-MIB", "netBotzTrapSensorValueInt"),
        ("NetBotz50-MIB", "netBotzTrapSensorValueFraction"))
)
if mibBuilder.loadTexts:
    netBotzDewPointError.setStatus(
        "current"
    )

netBotzDewPointTooHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 52674, 500, 10, 1, 3, 0, 2)
)
netBotzDewPointTooHigh.setObjects(
      *(("NetBotz50-MIB", "netBotzTrapErrorID"),
        ("NetBotz50-MIB", "netBotzTrapErrorType"),
        ("NetBotz50-MIB", "netBotzTrapErrorTypeLabel"),
        ("NetBotz50-MIB", "netBotzTrapSensorID"),
        ("NetBotz50-MIB", "netBotzTrapSensorLabel"),
        ("NetBotz50-MIB", "netBotzTrapContainerID"),
        ("NetBotz50-MIB", "netBotzTrapContainerLabel"),
        ("NetBotz50-MIB", "netBotzTrapPortID"),
        ("NetBotz50-MIB", "netBotzTrapPortLabel"),
        ("NetBotz50-MIB", "netBotzTrapStartTime"),
        ("NetBotz50-MIB", "netBotzTrapNotifyTime"),
        ("NetBotz50-MIB", "netBotzTrapResolveTime"),
        ("NetBotz50-MIB", "netBotzTrapSeverity"),
        ("NetBotz50-MIB", "netBotzTrapSensorValue"),
        ("NetBotz50-MIB", "netBotzTrapSensorValueInt"),
        ("NetBotz50-MIB", "netBotzTrapSensorValueFraction"))
)
if mibBuilder.loadTexts:
    netBotzDewPointTooHigh.setStatus(
        "current"
    )

netBotzDewPointTooLow = NotificationType(
    (1, 3, 6, 1, 4, 1, 52674, 500, 10, 1, 3, 0, 3)
)
netBotzDewPointTooLow.setObjects(
      *(("NetBotz50-MIB", "netBotzTrapErrorID"),
        ("NetBotz50-MIB", "netBotzTrapErrorType"),
        ("NetBotz50-MIB", "netBotzTrapErrorTypeLabel"),
        ("NetBotz50-MIB", "netBotzTrapSensorID"),
        ("NetBotz50-MIB", "netBotzTrapSensorLabel"),
        ("NetBotz50-MIB", "netBotzTrapContainerID"),
        ("NetBotz50-MIB", "netBotzTrapContainerLabel"),
        ("NetBotz50-MIB", "netBotzTrapPortID"),
        ("NetBotz50-MIB", "netBotzTrapPortLabel"),
        ("NetBotz50-MIB", "netBotzTrapStartTime"),
        ("NetBotz50-MIB", "netBotzTrapNotifyTime"),
        ("NetBotz50-MIB", "netBotzTrapResolveTime"),
        ("NetBotz50-MIB", "netBotzTrapSeverity"),
        ("NetBotz50-MIB", "netBotzTrapSensorValue"),
        ("NetBotz50-MIB", "netBotzTrapSensorValueInt"),
        ("NetBotz50-MIB", "netBotzTrapSensorValueFraction"))
)
if mibBuilder.loadTexts:
    netBotzDewPointTooLow.setStatus(
        "current"
    )

netBotzDewPointUnplugged = NotificationType(
    (1, 3, 6, 1, 4, 1, 52674, 500, 10, 1, 3, 0, 6)
)
netBotzDewPointUnplugged.setObjects(
      *(("NetBotz50-MIB", "netBotzTrapErrorID"),
        ("NetBotz50-MIB", "netBotzTrapErrorType"),
        ("NetBotz50-MIB", "netBotzTrapErrorTypeLabel"),
        ("NetBotz50-MIB", "netBotzTrapSensorID"),
        ("NetBotz50-MIB", "netBotzTrapSensorLabel"),
        ("NetBotz50-MIB", "netBotzTrapContainerID"),
        ("NetBotz50-MIB", "netBotzTrapContainerLabel"),
        ("NetBotz50-MIB", "netBotzTrapPortID"),
        ("NetBotz50-MIB", "netBotzTrapPortLabel"),
        ("NetBotz50-MIB", "netBotzTrapStartTime"),
        ("NetBotz50-MIB", "netBotzTrapNotifyTime"),
        ("NetBotz50-MIB", "netBotzTrapResolveTime"),
        ("NetBotz50-MIB", "netBotzTrapSeverity"),
        ("NetBotz50-MIB", "netBotzTrapSensorValue"),
        ("NetBotz50-MIB", "netBotzTrapSensorValueInt"),
        ("NetBotz50-MIB", "netBotzTrapSensorValueFraction"))
)
if mibBuilder.loadTexts:
    netBotzDewPointUnplugged.setStatus(
        "current"
    )

netBotzDewPointErrorRTN = NotificationType(
    (1, 3, 6, 1, 4, 1, 52674, 500, 10, 1, 3, 0, 101)
)
netBotzDewPointErrorRTN.setObjects(
      *(("NetBotz50-MIB", "netBotzTrapErrorID"),
        ("NetBotz50-MIB", "netBotzTrapErrorType"),
        ("NetBotz50-MIB", "netBotzTrapErrorTypeLabel"),
        ("NetBotz50-MIB", "netBotzTrapSensorID"),
        ("NetBotz50-MIB", "netBotzTrapSensorLabel"),
        ("NetBotz50-MIB", "netBotzTrapContainerID"),
        ("NetBotz50-MIB", "netBotzTrapContainerLabel"),
        ("NetBotz50-MIB", "netBotzTrapPortID"),
        ("NetBotz50-MIB", "netBotzTrapPortLabel"),
        ("NetBotz50-MIB", "netBotzTrapStartTime"),
        ("NetBotz50-MIB", "netBotzTrapNotifyTime"),
        ("NetBotz50-MIB", "netBotzTrapResolveTime"),
        ("NetBotz50-MIB", "netBotzTrapSeverity"),
        ("NetBotz50-MIB", "netBotzTrapSensorValue"),
        ("NetBotz50-MIB", "netBotzTrapSensorValueInt"),
        ("NetBotz50-MIB", "netBotzTrapSensorValueFraction"))
)
if mibBuilder.loadTexts:
    netBotzDewPointErrorRTN.setStatus(
        "current"
    )

netBotzDewPointTooHighRTN = NotificationType(
    (1, 3, 6, 1, 4, 1, 52674, 500, 10, 1, 3, 0, 102)
)
netBotzDewPointTooHighRTN.setObjects(
      *(("NetBotz50-MIB", "netBotzTrapErrorID"),
        ("NetBotz50-MIB", "netBotzTrapErrorType"),
        ("NetBotz50-MIB", "netBotzTrapErrorTypeLabel"),
        ("NetBotz50-MIB", "netBotzTrapSensorID"),
        ("NetBotz50-MIB", "netBotzTrapSensorLabel"),
        ("NetBotz50-MIB", "netBotzTrapContainerID"),
        ("NetBotz50-MIB", "netBotzTrapContainerLabel"),
        ("NetBotz50-MIB", "netBotzTrapPortID"),
        ("NetBotz50-MIB", "netBotzTrapPortLabel"),
        ("NetBotz50-MIB", "netBotzTrapStartTime"),
        ("NetBotz50-MIB", "netBotzTrapNotifyTime"),
        ("NetBotz50-MIB", "netBotzTrapResolveTime"),
        ("NetBotz50-MIB", "netBotzTrapSeverity"),
        ("NetBotz50-MIB", "netBotzTrapSensorValue"),
        ("NetBotz50-MIB", "netBotzTrapSensorValueInt"),
        ("NetBotz50-MIB", "netBotzTrapSensorValueFraction"))
)
if mibBuilder.loadTexts:
    netBotzDewPointTooHighRTN.setStatus(
        "current"
    )

netBotzDewPointTooLowRTN = NotificationType(
    (1, 3, 6, 1, 4, 1, 52674, 500, 10, 1, 3, 0, 103)
)
netBotzDewPointTooLowRTN.setObjects(
      *(("NetBotz50-MIB", "netBotzTrapErrorID"),
        ("NetBotz50-MIB", "netBotzTrapErrorType"),
        ("NetBotz50-MIB", "netBotzTrapErrorTypeLabel"),
        ("NetBotz50-MIB", "netBotzTrapSensorID"),
        ("NetBotz50-MIB", "netBotzTrapSensorLabel"),
        ("NetBotz50-MIB", "netBotzTrapContainerID"),
        ("NetBotz50-MIB", "netBotzTrapContainerLabel"),
        ("NetBotz50-MIB", "netBotzTrapPortID"),
        ("NetBotz50-MIB", "netBotzTrapPortLabel"),
        ("NetBotz50-MIB", "netBotzTrapStartTime"),
        ("NetBotz50-MIB", "netBotzTrapNotifyTime"),
        ("NetBotz50-MIB", "netBotzTrapResolveTime"),
        ("NetBotz50-MIB", "netBotzTrapSeverity"),
        ("NetBotz50-MIB", "netBotzTrapSensorValue"),
        ("NetBotz50-MIB", "netBotzTrapSensorValueInt"),
        ("NetBotz50-MIB", "netBotzTrapSensorValueFraction"))
)
if mibBuilder.loadTexts:
    netBotzDewPointTooLowRTN.setStatus(
        "current"
    )

netBotzDewPointReplugged = NotificationType(
    (1, 3, 6, 1, 4, 1, 52674, 500, 10, 1, 3, 0, 106)
)
netBotzDewPointReplugged.setObjects(
      *(("NetBotz50-MIB", "netBotzTrapErrorID"),
        ("NetBotz50-MIB", "netBotzTrapErrorType"),
        ("NetBotz50-MIB", "netBotzTrapErrorTypeLabel"),
        ("NetBotz50-MIB", "netBotzTrapSensorID"),
        ("NetBotz50-MIB", "netBotzTrapSensorLabel"),
        ("NetBotz50-MIB", "netBotzTrapContainerID"),
        ("NetBotz50-MIB", "netBotzTrapContainerLabel"),
        ("NetBotz50-MIB", "netBotzTrapPortID"),
        ("NetBotz50-MIB", "netBotzTrapPortLabel"),
        ("NetBotz50-MIB", "netBotzTrapStartTime"),
        ("NetBotz50-MIB", "netBotzTrapNotifyTime"),
        ("NetBotz50-MIB", "netBotzTrapResolveTime"),
        ("NetBotz50-MIB", "netBotzTrapSeverity"),
        ("NetBotz50-MIB", "netBotzTrapSensorValue"),
        ("NetBotz50-MIB", "netBotzTrapSensorValueInt"),
        ("NetBotz50-MIB", "netBotzTrapSensorValueFraction"))
)
if mibBuilder.loadTexts:
    netBotzDewPointReplugged.setStatus(
        "current"
    )

netBotzAirFlowError = NotificationType(
    (1, 3, 6, 1, 4, 1, 52674, 500, 10, 1, 4, 0, 1)
)
netBotzAirFlowError.setObjects(
      *(("NetBotz50-MIB", "netBotzTrapErrorID"),
        ("NetBotz50-MIB", "netBotzTrapErrorType"),
        ("NetBotz50-MIB", "netBotzTrapErrorTypeLabel"),
        ("NetBotz50-MIB", "netBotzTrapSensorID"),
        ("NetBotz50-MIB", "netBotzTrapSensorLabel"),
        ("NetBotz50-MIB", "netBotzTrapContainerID"),
        ("NetBotz50-MIB", "netBotzTrapContainerLabel"),
        ("NetBotz50-MIB", "netBotzTrapPortID"),
        ("NetBotz50-MIB", "netBotzTrapPortLabel"),
        ("NetBotz50-MIB", "netBotzTrapStartTime"),
        ("NetBotz50-MIB", "netBotzTrapNotifyTime"),
        ("NetBotz50-MIB", "netBotzTrapResolveTime"),
        ("NetBotz50-MIB", "netBotzTrapSeverity"),
        ("NetBotz50-MIB", "netBotzTrapSensorValue"),
        ("NetBotz50-MIB", "netBotzTrapSensorValueInt"),
        ("NetBotz50-MIB", "netBotzTrapSensorValueFraction"))
)
if mibBuilder.loadTexts:
    netBotzAirFlowError.setStatus(
        "current"
    )

netBotzAirFlowTooHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 52674, 500, 10, 1, 4, 0, 2)
)
netBotzAirFlowTooHigh.setObjects(
      *(("NetBotz50-MIB", "netBotzTrapErrorID"),
        ("NetBotz50-MIB", "netBotzTrapErrorType"),
        ("NetBotz50-MIB", "netBotzTrapErrorTypeLabel"),
        ("NetBotz50-MIB", "netBotzTrapSensorID"),
        ("NetBotz50-MIB", "netBotzTrapSensorLabel"),
        ("NetBotz50-MIB", "netBotzTrapContainerID"),
        ("NetBotz50-MIB", "netBotzTrapContainerLabel"),
        ("NetBotz50-MIB", "netBotzTrapPortID"),
        ("NetBotz50-MIB", "netBotzTrapPortLabel"),
        ("NetBotz50-MIB", "netBotzTrapStartTime"),
        ("NetBotz50-MIB", "netBotzTrapNotifyTime"),
        ("NetBotz50-MIB", "netBotzTrapResolveTime"),
        ("NetBotz50-MIB", "netBotzTrapSeverity"),
        ("NetBotz50-MIB", "netBotzTrapSensorValue"),
        ("NetBotz50-MIB", "netBotzTrapSensorValueInt"),
        ("NetBotz50-MIB", "netBotzTrapSensorValueFraction"))
)
if mibBuilder.loadTexts:
    netBotzAirFlowTooHigh.setStatus(
        "current"
    )

netBotzAirFlowTooLow = NotificationType(
    (1, 3, 6, 1, 4, 1, 52674, 500, 10, 1, 4, 0, 3)
)
netBotzAirFlowTooLow.setObjects(
      *(("NetBotz50-MIB", "netBotzTrapErrorID"),
        ("NetBotz50-MIB", "netBotzTrapErrorType"),
        ("NetBotz50-MIB", "netBotzTrapErrorTypeLabel"),
        ("NetBotz50-MIB", "netBotzTrapSensorID"),
        ("NetBotz50-MIB", "netBotzTrapSensorLabel"),
        ("NetBotz50-MIB", "netBotzTrapContainerID"),
        ("NetBotz50-MIB", "netBotzTrapContainerLabel"),
        ("NetBotz50-MIB", "netBotzTrapPortID"),
        ("NetBotz50-MIB", "netBotzTrapPortLabel"),
        ("NetBotz50-MIB", "netBotzTrapStartTime"),
        ("NetBotz50-MIB", "netBotzTrapNotifyTime"),
        ("NetBotz50-MIB", "netBotzTrapResolveTime"),
        ("NetBotz50-MIB", "netBotzTrapSeverity"),
        ("NetBotz50-MIB", "netBotzTrapSensorValue"),
        ("NetBotz50-MIB", "netBotzTrapSensorValueInt"),
        ("NetBotz50-MIB", "netBotzTrapSensorValueFraction"))
)
if mibBuilder.loadTexts:
    netBotzAirFlowTooLow.setStatus(
        "current"
    )

netBotzAirFlowUnplugged = NotificationType(
    (1, 3, 6, 1, 4, 1, 52674, 500, 10, 1, 4, 0, 6)
)
netBotzAirFlowUnplugged.setObjects(
      *(("NetBotz50-MIB", "netBotzTrapErrorID"),
        ("NetBotz50-MIB", "netBotzTrapErrorType"),
        ("NetBotz50-MIB", "netBotzTrapErrorTypeLabel"),
        ("NetBotz50-MIB", "netBotzTrapSensorID"),
        ("NetBotz50-MIB", "netBotzTrapSensorLabel"),
        ("NetBotz50-MIB", "netBotzTrapContainerID"),
        ("NetBotz50-MIB", "netBotzTrapContainerLabel"),
        ("NetBotz50-MIB", "netBotzTrapPortID"),
        ("NetBotz50-MIB", "netBotzTrapPortLabel"),
        ("NetBotz50-MIB", "netBotzTrapStartTime"),
        ("NetBotz50-MIB", "netBotzTrapNotifyTime"),
        ("NetBotz50-MIB", "netBotzTrapResolveTime"),
        ("NetBotz50-MIB", "netBotzTrapSeverity"),
        ("NetBotz50-MIB", "netBotzTrapSensorValue"),
        ("NetBotz50-MIB", "netBotzTrapSensorValueInt"),
        ("NetBotz50-MIB", "netBotzTrapSensorValueFraction"))
)
if mibBuilder.loadTexts:
    netBotzAirFlowUnplugged.setStatus(
        "current"
    )

netBotzAirFlowErrorRTN = NotificationType(
    (1, 3, 6, 1, 4, 1, 52674, 500, 10, 1, 4, 0, 101)
)
netBotzAirFlowErrorRTN.setObjects(
      *(("NetBotz50-MIB", "netBotzTrapErrorID"),
        ("NetBotz50-MIB", "netBotzTrapErrorType"),
        ("NetBotz50-MIB", "netBotzTrapErrorTypeLabel"),
        ("NetBotz50-MIB", "netBotzTrapSensorID"),
        ("NetBotz50-MIB", "netBotzTrapSensorLabel"),
        ("NetBotz50-MIB", "netBotzTrapContainerID"),
        ("NetBotz50-MIB", "netBotzTrapContainerLabel"),
        ("NetBotz50-MIB", "netBotzTrapPortID"),
        ("NetBotz50-MIB", "netBotzTrapPortLabel"),
        ("NetBotz50-MIB", "netBotzTrapStartTime"),
        ("NetBotz50-MIB", "netBotzTrapNotifyTime"),
        ("NetBotz50-MIB", "netBotzTrapResolveTime"),
        ("NetBotz50-MIB", "netBotzTrapSeverity"),
        ("NetBotz50-MIB", "netBotzTrapSensorValue"),
        ("NetBotz50-MIB", "netBotzTrapSensorValueInt"),
        ("NetBotz50-MIB", "netBotzTrapSensorValueFraction"))
)
if mibBuilder.loadTexts:
    netBotzAirFlowErrorRTN.setStatus(
        "current"
    )

netBotzAirFlowTooHighRTN = NotificationType(
    (1, 3, 6, 1, 4, 1, 52674, 500, 10, 1, 4, 0, 102)
)
netBotzAirFlowTooHighRTN.setObjects(
      *(("NetBotz50-MIB", "netBotzTrapErrorID"),
        ("NetBotz50-MIB", "netBotzTrapErrorType"),
        ("NetBotz50-MIB", "netBotzTrapErrorTypeLabel"),
        ("NetBotz50-MIB", "netBotzTrapSensorID"),
        ("NetBotz50-MIB", "netBotzTrapSensorLabel"),
        ("NetBotz50-MIB", "netBotzTrapContainerID"),
        ("NetBotz50-MIB", "netBotzTrapContainerLabel"),
        ("NetBotz50-MIB", "netBotzTrapPortID"),
        ("NetBotz50-MIB", "netBotzTrapPortLabel"),
        ("NetBotz50-MIB", "netBotzTrapStartTime"),
        ("NetBotz50-MIB", "netBotzTrapNotifyTime"),
        ("NetBotz50-MIB", "netBotzTrapResolveTime"),
        ("NetBotz50-MIB", "netBotzTrapSeverity"),
        ("NetBotz50-MIB", "netBotzTrapSensorValue"),
        ("NetBotz50-MIB", "netBotzTrapSensorValueInt"),
        ("NetBotz50-MIB", "netBotzTrapSensorValueFraction"))
)
if mibBuilder.loadTexts:
    netBotzAirFlowTooHighRTN.setStatus(
        "current"
    )

netBotzAirFlowTooLowRTN = NotificationType(
    (1, 3, 6, 1, 4, 1, 52674, 500, 10, 1, 4, 0, 103)
)
netBotzAirFlowTooLowRTN.setObjects(
      *(("NetBotz50-MIB", "netBotzTrapErrorID"),
        ("NetBotz50-MIB", "netBotzTrapErrorType"),
        ("NetBotz50-MIB", "netBotzTrapErrorTypeLabel"),
        ("NetBotz50-MIB", "netBotzTrapSensorID"),
        ("NetBotz50-MIB", "netBotzTrapSensorLabel"),
        ("NetBotz50-MIB", "netBotzTrapContainerID"),
        ("NetBotz50-MIB", "netBotzTrapContainerLabel"),
        ("NetBotz50-MIB", "netBotzTrapPortID"),
        ("NetBotz50-MIB", "netBotzTrapPortLabel"),
        ("NetBotz50-MIB", "netBotzTrapStartTime"),
        ("NetBotz50-MIB", "netBotzTrapNotifyTime"),
        ("NetBotz50-MIB", "netBotzTrapResolveTime"),
        ("NetBotz50-MIB", "netBotzTrapSeverity"),
        ("NetBotz50-MIB", "netBotzTrapSensorValue"),
        ("NetBotz50-MIB", "netBotzTrapSensorValueInt"),
        ("NetBotz50-MIB", "netBotzTrapSensorValueFraction"))
)
if mibBuilder.loadTexts:
    netBotzAirFlowTooLowRTN.setStatus(
        "current"
    )

netBotzAirFlowReplugged = NotificationType(
    (1, 3, 6, 1, 4, 1, 52674, 500, 10, 1, 4, 0, 106)
)
netBotzAirFlowReplugged.setObjects(
      *(("NetBotz50-MIB", "netBotzTrapErrorID"),
        ("NetBotz50-MIB", "netBotzTrapErrorType"),
        ("NetBotz50-MIB", "netBotzTrapErrorTypeLabel"),
        ("NetBotz50-MIB", "netBotzTrapSensorID"),
        ("NetBotz50-MIB", "netBotzTrapSensorLabel"),
        ("NetBotz50-MIB", "netBotzTrapContainerID"),
        ("NetBotz50-MIB", "netBotzTrapContainerLabel"),
        ("NetBotz50-MIB", "netBotzTrapPortID"),
        ("NetBotz50-MIB", "netBotzTrapPortLabel"),
        ("NetBotz50-MIB", "netBotzTrapStartTime"),
        ("NetBotz50-MIB", "netBotzTrapNotifyTime"),
        ("NetBotz50-MIB", "netBotzTrapResolveTime"),
        ("NetBotz50-MIB", "netBotzTrapSeverity"),
        ("NetBotz50-MIB", "netBotzTrapSensorValue"),
        ("NetBotz50-MIB", "netBotzTrapSensorValueInt"),
        ("NetBotz50-MIB", "netBotzTrapSensorValueFraction"))
)
if mibBuilder.loadTexts:
    netBotzAirFlowReplugged.setStatus(
        "current"
    )

netBotzAmpDetectError = NotificationType(
    (1, 3, 6, 1, 4, 1, 52674, 500, 10, 1, 5, 0, 1)
)
netBotzAmpDetectError.setObjects(
      *(("NetBotz50-MIB", "netBotzTrapErrorID"),
        ("NetBotz50-MIB", "netBotzTrapErrorType"),
        ("NetBotz50-MIB", "netBotzTrapErrorTypeLabel"),
        ("NetBotz50-MIB", "netBotzTrapSensorID"),
        ("NetBotz50-MIB", "netBotzTrapSensorLabel"),
        ("NetBotz50-MIB", "netBotzTrapContainerID"),
        ("NetBotz50-MIB", "netBotzTrapContainerLabel"),
        ("NetBotz50-MIB", "netBotzTrapPortID"),
        ("NetBotz50-MIB", "netBotzTrapPortLabel"),
        ("NetBotz50-MIB", "netBotzTrapStartTime"),
        ("NetBotz50-MIB", "netBotzTrapNotifyTime"),
        ("NetBotz50-MIB", "netBotzTrapResolveTime"),
        ("NetBotz50-MIB", "netBotzTrapSeverity"),
        ("NetBotz50-MIB", "netBotzTrapSensorValue"),
        ("NetBotz50-MIB", "netBotzTrapSensorValueInt"),
        ("NetBotz50-MIB", "netBotzTrapSensorValueFraction"))
)
if mibBuilder.loadTexts:
    netBotzAmpDetectError.setStatus(
        "current"
    )

netBotzAmpDetectTooHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 52674, 500, 10, 1, 5, 0, 2)
)
netBotzAmpDetectTooHigh.setObjects(
      *(("NetBotz50-MIB", "netBotzTrapErrorID"),
        ("NetBotz50-MIB", "netBotzTrapErrorType"),
        ("NetBotz50-MIB", "netBotzTrapErrorTypeLabel"),
        ("NetBotz50-MIB", "netBotzTrapSensorID"),
        ("NetBotz50-MIB", "netBotzTrapSensorLabel"),
        ("NetBotz50-MIB", "netBotzTrapContainerID"),
        ("NetBotz50-MIB", "netBotzTrapContainerLabel"),
        ("NetBotz50-MIB", "netBotzTrapPortID"),
        ("NetBotz50-MIB", "netBotzTrapPortLabel"),
        ("NetBotz50-MIB", "netBotzTrapStartTime"),
        ("NetBotz50-MIB", "netBotzTrapNotifyTime"),
        ("NetBotz50-MIB", "netBotzTrapResolveTime"),
        ("NetBotz50-MIB", "netBotzTrapSeverity"),
        ("NetBotz50-MIB", "netBotzTrapSensorValue"),
        ("NetBotz50-MIB", "netBotzTrapSensorValueInt"),
        ("NetBotz50-MIB", "netBotzTrapSensorValueFraction"))
)
if mibBuilder.loadTexts:
    netBotzAmpDetectTooHigh.setStatus(
        "current"
    )

netBotzAmpDetectTooLow = NotificationType(
    (1, 3, 6, 1, 4, 1, 52674, 500, 10, 1, 5, 0, 3)
)
netBotzAmpDetectTooLow.setObjects(
      *(("NetBotz50-MIB", "netBotzTrapErrorID"),
        ("NetBotz50-MIB", "netBotzTrapErrorType"),
        ("NetBotz50-MIB", "netBotzTrapErrorTypeLabel"),
        ("NetBotz50-MIB", "netBotzTrapSensorID"),
        ("NetBotz50-MIB", "netBotzTrapSensorLabel"),
        ("NetBotz50-MIB", "netBotzTrapContainerID"),
        ("NetBotz50-MIB", "netBotzTrapContainerLabel"),
        ("NetBotz50-MIB", "netBotzTrapPortID"),
        ("NetBotz50-MIB", "netBotzTrapPortLabel"),
        ("NetBotz50-MIB", "netBotzTrapStartTime"),
        ("NetBotz50-MIB", "netBotzTrapNotifyTime"),
        ("NetBotz50-MIB", "netBotzTrapResolveTime"),
        ("NetBotz50-MIB", "netBotzTrapSeverity"),
        ("NetBotz50-MIB", "netBotzTrapSensorValue"),
        ("NetBotz50-MIB", "netBotzTrapSensorValueInt"),
        ("NetBotz50-MIB", "netBotzTrapSensorValueFraction"))
)
if mibBuilder.loadTexts:
    netBotzAmpDetectTooLow.setStatus(
        "current"
    )

netBotzAmpDetectUnplugged = NotificationType(
    (1, 3, 6, 1, 4, 1, 52674, 500, 10, 1, 5, 0, 6)
)
netBotzAmpDetectUnplugged.setObjects(
      *(("NetBotz50-MIB", "netBotzTrapErrorID"),
        ("NetBotz50-MIB", "netBotzTrapErrorType"),
        ("NetBotz50-MIB", "netBotzTrapErrorTypeLabel"),
        ("NetBotz50-MIB", "netBotzTrapSensorID"),
        ("NetBotz50-MIB", "netBotzTrapSensorLabel"),
        ("NetBotz50-MIB", "netBotzTrapContainerID"),
        ("NetBotz50-MIB", "netBotzTrapContainerLabel"),
        ("NetBotz50-MIB", "netBotzTrapPortID"),
        ("NetBotz50-MIB", "netBotzTrapPortLabel"),
        ("NetBotz50-MIB", "netBotzTrapStartTime"),
        ("NetBotz50-MIB", "netBotzTrapNotifyTime"),
        ("NetBotz50-MIB", "netBotzTrapResolveTime"),
        ("NetBotz50-MIB", "netBotzTrapSeverity"),
        ("NetBotz50-MIB", "netBotzTrapSensorValue"),
        ("NetBotz50-MIB", "netBotzTrapSensorValueInt"),
        ("NetBotz50-MIB", "netBotzTrapSensorValueFraction"))
)
if mibBuilder.loadTexts:
    netBotzAmpDetectUnplugged.setStatus(
        "current"
    )

netBotzAmpDetectErrorRTN = NotificationType(
    (1, 3, 6, 1, 4, 1, 52674, 500, 10, 1, 5, 0, 101)
)
netBotzAmpDetectErrorRTN.setObjects(
      *(("NetBotz50-MIB", "netBotzTrapErrorID"),
        ("NetBotz50-MIB", "netBotzTrapErrorType"),
        ("NetBotz50-MIB", "netBotzTrapErrorTypeLabel"),
        ("NetBotz50-MIB", "netBotzTrapSensorID"),
        ("NetBotz50-MIB", "netBotzTrapSensorLabel"),
        ("NetBotz50-MIB", "netBotzTrapContainerID"),
        ("NetBotz50-MIB", "netBotzTrapContainerLabel"),
        ("NetBotz50-MIB", "netBotzTrapPortID"),
        ("NetBotz50-MIB", "netBotzTrapPortLabel"),
        ("NetBotz50-MIB", "netBotzTrapStartTime"),
        ("NetBotz50-MIB", "netBotzTrapNotifyTime"),
        ("NetBotz50-MIB", "netBotzTrapResolveTime"),
        ("NetBotz50-MIB", "netBotzTrapSeverity"),
        ("NetBotz50-MIB", "netBotzTrapSensorValue"),
        ("NetBotz50-MIB", "netBotzTrapSensorValueInt"),
        ("NetBotz50-MIB", "netBotzTrapSensorValueFraction"))
)
if mibBuilder.loadTexts:
    netBotzAmpDetectErrorRTN.setStatus(
        "current"
    )

netBotzAmpDetectTooHighRTN = NotificationType(
    (1, 3, 6, 1, 4, 1, 52674, 500, 10, 1, 5, 0, 102)
)
netBotzAmpDetectTooHighRTN.setObjects(
      *(("NetBotz50-MIB", "netBotzTrapErrorID"),
        ("NetBotz50-MIB", "netBotzTrapErrorType"),
        ("NetBotz50-MIB", "netBotzTrapErrorTypeLabel"),
        ("NetBotz50-MIB", "netBotzTrapSensorID"),
        ("NetBotz50-MIB", "netBotzTrapSensorLabel"),
        ("NetBotz50-MIB", "netBotzTrapContainerID"),
        ("NetBotz50-MIB", "netBotzTrapContainerLabel"),
        ("NetBotz50-MIB", "netBotzTrapPortID"),
        ("NetBotz50-MIB", "netBotzTrapPortLabel"),
        ("NetBotz50-MIB", "netBotzTrapStartTime"),
        ("NetBotz50-MIB", "netBotzTrapNotifyTime"),
        ("NetBotz50-MIB", "netBotzTrapResolveTime"),
        ("NetBotz50-MIB", "netBotzTrapSeverity"),
        ("NetBotz50-MIB", "netBotzTrapSensorValue"),
        ("NetBotz50-MIB", "netBotzTrapSensorValueInt"),
        ("NetBotz50-MIB", "netBotzTrapSensorValueFraction"))
)
if mibBuilder.loadTexts:
    netBotzAmpDetectTooHighRTN.setStatus(
        "current"
    )

netBotzAmpDetectTooLowRTN = NotificationType(
    (1, 3, 6, 1, 4, 1, 52674, 500, 10, 1, 5, 0, 103)
)
netBotzAmpDetectTooLowRTN.setObjects(
      *(("NetBotz50-MIB", "netBotzTrapErrorID"),
        ("NetBotz50-MIB", "netBotzTrapErrorType"),
        ("NetBotz50-MIB", "netBotzTrapErrorTypeLabel"),
        ("NetBotz50-MIB", "netBotzTrapSensorID"),
        ("NetBotz50-MIB", "netBotzTrapSensorLabel"),
        ("NetBotz50-MIB", "netBotzTrapContainerID"),
        ("NetBotz50-MIB", "netBotzTrapContainerLabel"),
        ("NetBotz50-MIB", "netBotzTrapPortID"),
        ("NetBotz50-MIB", "netBotzTrapPortLabel"),
        ("NetBotz50-MIB", "netBotzTrapStartTime"),
        ("NetBotz50-MIB", "netBotzTrapNotifyTime"),
        ("NetBotz50-MIB", "netBotzTrapResolveTime"),
        ("NetBotz50-MIB", "netBotzTrapSeverity"),
        ("NetBotz50-MIB", "netBotzTrapSensorValue"),
        ("NetBotz50-MIB", "netBotzTrapSensorValueInt"),
        ("NetBotz50-MIB", "netBotzTrapSensorValueFraction"))
)
if mibBuilder.loadTexts:
    netBotzAmpDetectTooLowRTN.setStatus(
        "current"
    )

netBotzAmpDetectReplugged = NotificationType(
    (1, 3, 6, 1, 4, 1, 52674, 500, 10, 1, 5, 0, 106)
)
netBotzAmpDetectReplugged.setObjects(
      *(("NetBotz50-MIB", "netBotzTrapErrorID"),
        ("NetBotz50-MIB", "netBotzTrapErrorType"),
        ("NetBotz50-MIB", "netBotzTrapErrorTypeLabel"),
        ("NetBotz50-MIB", "netBotzTrapSensorID"),
        ("NetBotz50-MIB", "netBotzTrapSensorLabel"),
        ("NetBotz50-MIB", "netBotzTrapContainerID"),
        ("NetBotz50-MIB", "netBotzTrapContainerLabel"),
        ("NetBotz50-MIB", "netBotzTrapPortID"),
        ("NetBotz50-MIB", "netBotzTrapPortLabel"),
        ("NetBotz50-MIB", "netBotzTrapStartTime"),
        ("NetBotz50-MIB", "netBotzTrapNotifyTime"),
        ("NetBotz50-MIB", "netBotzTrapResolveTime"),
        ("NetBotz50-MIB", "netBotzTrapSeverity"),
        ("NetBotz50-MIB", "netBotzTrapSensorValue"),
        ("NetBotz50-MIB", "netBotzTrapSensorValueInt"),
        ("NetBotz50-MIB", "netBotzTrapSensorValueFraction"))
)
if mibBuilder.loadTexts:
    netBotzAmpDetectReplugged.setStatus(
        "current"
    )

netBotzDryContactError = NotificationType(
    (1, 3, 6, 1, 4, 1, 52674, 500, 10, 1, 6, 0, 1)
)
netBotzDryContactError.setObjects(
      *(("NetBotz50-MIB", "netBotzTrapErrorID"),
        ("NetBotz50-MIB", "netBotzTrapErrorType"),
        ("NetBotz50-MIB", "netBotzTrapErrorTypeLabel"),
        ("NetBotz50-MIB", "netBotzTrapSensorID"),
        ("NetBotz50-MIB", "netBotzTrapSensorLabel"),
        ("NetBotz50-MIB", "netBotzTrapContainerID"),
        ("NetBotz50-MIB", "netBotzTrapContainerLabel"),
        ("NetBotz50-MIB", "netBotzTrapPortID"),
        ("NetBotz50-MIB", "netBotzTrapPortLabel"),
        ("NetBotz50-MIB", "netBotzTrapStartTime"),
        ("NetBotz50-MIB", "netBotzTrapNotifyTime"),
        ("NetBotz50-MIB", "netBotzTrapResolveTime"),
        ("NetBotz50-MIB", "netBotzTrapSeverity"),
        ("NetBotz50-MIB", "netBotzTrapSensorValue"),
        ("NetBotz50-MIB", "netBotzTrapSensorValueInt"),
        ("NetBotz50-MIB", "netBotzTrapSensorValueFraction"))
)
if mibBuilder.loadTexts:
    netBotzDryContactError.setStatus(
        "current"
    )

netBotzDryContactUnplugged = NotificationType(
    (1, 3, 6, 1, 4, 1, 52674, 500, 10, 1, 6, 0, 6)
)
netBotzDryContactUnplugged.setObjects(
      *(("NetBotz50-MIB", "netBotzTrapErrorID"),
        ("NetBotz50-MIB", "netBotzTrapErrorType"),
        ("NetBotz50-MIB", "netBotzTrapErrorTypeLabel"),
        ("NetBotz50-MIB", "netBotzTrapSensorID"),
        ("NetBotz50-MIB", "netBotzTrapSensorLabel"),
        ("NetBotz50-MIB", "netBotzTrapContainerID"),
        ("NetBotz50-MIB", "netBotzTrapContainerLabel"),
        ("NetBotz50-MIB", "netBotzTrapPortID"),
        ("NetBotz50-MIB", "netBotzTrapPortLabel"),
        ("NetBotz50-MIB", "netBotzTrapStartTime"),
        ("NetBotz50-MIB", "netBotzTrapNotifyTime"),
        ("NetBotz50-MIB", "netBotzTrapResolveTime"),
        ("NetBotz50-MIB", "netBotzTrapSeverity"),
        ("NetBotz50-MIB", "netBotzTrapSensorValue"),
        ("NetBotz50-MIB", "netBotzTrapSensorValueInt"),
        ("NetBotz50-MIB", "netBotzTrapSensorValueFraction"))
)
if mibBuilder.loadTexts:
    netBotzDryContactUnplugged.setStatus(
        "current"
    )

netBotzDryContactValueError = NotificationType(
    (1, 3, 6, 1, 4, 1, 52674, 500, 10, 1, 6, 0, 10)
)
netBotzDryContactValueError.setObjects(
      *(("NetBotz50-MIB", "netBotzTrapErrorID"),
        ("NetBotz50-MIB", "netBotzTrapErrorType"),
        ("NetBotz50-MIB", "netBotzTrapErrorTypeLabel"),
        ("NetBotz50-MIB", "netBotzTrapSensorID"),
        ("NetBotz50-MIB", "netBotzTrapSensorLabel"),
        ("NetBotz50-MIB", "netBotzTrapContainerID"),
        ("NetBotz50-MIB", "netBotzTrapContainerLabel"),
        ("NetBotz50-MIB", "netBotzTrapPortID"),
        ("NetBotz50-MIB", "netBotzTrapPortLabel"),
        ("NetBotz50-MIB", "netBotzTrapStartTime"),
        ("NetBotz50-MIB", "netBotzTrapNotifyTime"),
        ("NetBotz50-MIB", "netBotzTrapResolveTime"),
        ("NetBotz50-MIB", "netBotzTrapSeverity"),
        ("NetBotz50-MIB", "netBotzTrapSensorValue"),
        ("NetBotz50-MIB", "netBotzTrapSensorValueInt"),
        ("NetBotz50-MIB", "netBotzTrapSensorValueFraction"))
)
if mibBuilder.loadTexts:
    netBotzDryContactValueError.setStatus(
        "current"
    )

netBotzDryContactErrorRTN = NotificationType(
    (1, 3, 6, 1, 4, 1, 52674, 500, 10, 1, 6, 0, 101)
)
netBotzDryContactErrorRTN.setObjects(
      *(("NetBotz50-MIB", "netBotzTrapErrorID"),
        ("NetBotz50-MIB", "netBotzTrapErrorType"),
        ("NetBotz50-MIB", "netBotzTrapErrorTypeLabel"),
        ("NetBotz50-MIB", "netBotzTrapSensorID"),
        ("NetBotz50-MIB", "netBotzTrapSensorLabel"),
        ("NetBotz50-MIB", "netBotzTrapContainerID"),
        ("NetBotz50-MIB", "netBotzTrapContainerLabel"),
        ("NetBotz50-MIB", "netBotzTrapPortID"),
        ("NetBotz50-MIB", "netBotzTrapPortLabel"),
        ("NetBotz50-MIB", "netBotzTrapStartTime"),
        ("NetBotz50-MIB", "netBotzTrapNotifyTime"),
        ("NetBotz50-MIB", "netBotzTrapResolveTime"),
        ("NetBotz50-MIB", "netBotzTrapSeverity"),
        ("NetBotz50-MIB", "netBotzTrapSensorValue"),
        ("NetBotz50-MIB", "netBotzTrapSensorValueInt"),
        ("NetBotz50-MIB", "netBotzTrapSensorValueFraction"))
)
if mibBuilder.loadTexts:
    netBotzDryContactErrorRTN.setStatus(
        "current"
    )

netBotzDryContactReplugged = NotificationType(
    (1, 3, 6, 1, 4, 1, 52674, 500, 10, 1, 6, 0, 106)
)
netBotzDryContactReplugged.setObjects(
      *(("NetBotz50-MIB", "netBotzTrapErrorID"),
        ("NetBotz50-MIB", "netBotzTrapErrorType"),
        ("NetBotz50-MIB", "netBotzTrapErrorTypeLabel"),
        ("NetBotz50-MIB", "netBotzTrapSensorID"),
        ("NetBotz50-MIB", "netBotzTrapSensorLabel"),
        ("NetBotz50-MIB", "netBotzTrapContainerID"),
        ("NetBotz50-MIB", "netBotzTrapContainerLabel"),
        ("NetBotz50-MIB", "netBotzTrapPortID"),
        ("NetBotz50-MIB", "netBotzTrapPortLabel"),
        ("NetBotz50-MIB", "netBotzTrapStartTime"),
        ("NetBotz50-MIB", "netBotzTrapNotifyTime"),
        ("NetBotz50-MIB", "netBotzTrapResolveTime"),
        ("NetBotz50-MIB", "netBotzTrapSeverity"),
        ("NetBotz50-MIB", "netBotzTrapSensorValue"),
        ("NetBotz50-MIB", "netBotzTrapSensorValueInt"),
        ("NetBotz50-MIB", "netBotzTrapSensorValueFraction"))
)
if mibBuilder.loadTexts:
    netBotzDryContactReplugged.setStatus(
        "current"
    )

netBotzDryContactValueErrorRTN = NotificationType(
    (1, 3, 6, 1, 4, 1, 52674, 500, 10, 1, 6, 0, 110)
)
netBotzDryContactValueErrorRTN.setObjects(
      *(("NetBotz50-MIB", "netBotzTrapErrorID"),
        ("NetBotz50-MIB", "netBotzTrapErrorType"),
        ("NetBotz50-MIB", "netBotzTrapErrorTypeLabel"),
        ("NetBotz50-MIB", "netBotzTrapSensorID"),
        ("NetBotz50-MIB", "netBotzTrapSensorLabel"),
        ("NetBotz50-MIB", "netBotzTrapContainerID"),
        ("NetBotz50-MIB", "netBotzTrapContainerLabel"),
        ("NetBotz50-MIB", "netBotzTrapPortID"),
        ("NetBotz50-MIB", "netBotzTrapPortLabel"),
        ("NetBotz50-MIB", "netBotzTrapStartTime"),
        ("NetBotz50-MIB", "netBotzTrapNotifyTime"),
        ("NetBotz50-MIB", "netBotzTrapResolveTime"),
        ("NetBotz50-MIB", "netBotzTrapSeverity"),
        ("NetBotz50-MIB", "netBotzTrapSensorValue"),
        ("NetBotz50-MIB", "netBotzTrapSensorValueInt"),
        ("NetBotz50-MIB", "netBotzTrapSensorValueFraction"))
)
if mibBuilder.loadTexts:
    netBotzDryContactValueErrorRTN.setStatus(
        "current"
    )

netBotzCameraMotionSensorError = NotificationType(
    (1, 3, 6, 1, 4, 1, 52674, 500, 10, 1, 7, 0, 1)
)
netBotzCameraMotionSensorError.setObjects(
      *(("NetBotz50-MIB", "netBotzTrapErrorID"),
        ("NetBotz50-MIB", "netBotzTrapErrorType"),
        ("NetBotz50-MIB", "netBotzTrapErrorTypeLabel"),
        ("NetBotz50-MIB", "netBotzTrapSensorID"),
        ("NetBotz50-MIB", "netBotzTrapSensorLabel"),
        ("NetBotz50-MIB", "netBotzTrapContainerID"),
        ("NetBotz50-MIB", "netBotzTrapContainerLabel"),
        ("NetBotz50-MIB", "netBotzTrapPortID"),
        ("NetBotz50-MIB", "netBotzTrapPortLabel"),
        ("NetBotz50-MIB", "netBotzTrapStartTime"),
        ("NetBotz50-MIB", "netBotzTrapNotifyTime"),
        ("NetBotz50-MIB", "netBotzTrapResolveTime"),
        ("NetBotz50-MIB", "netBotzTrapSeverity"),
        ("NetBotz50-MIB", "netBotzTrapSensorValue"),
        ("NetBotz50-MIB", "netBotzTrapSensorValueInt"),
        ("NetBotz50-MIB", "netBotzTrapSensorValueFraction"))
)
if mibBuilder.loadTexts:
    netBotzCameraMotionSensorError.setStatus(
        "current"
    )

netBotzCameraMotionSensorUnplugged = NotificationType(
    (1, 3, 6, 1, 4, 1, 52674, 500, 10, 1, 7, 0, 6)
)
netBotzCameraMotionSensorUnplugged.setObjects(
      *(("NetBotz50-MIB", "netBotzTrapErrorID"),
        ("NetBotz50-MIB", "netBotzTrapErrorType"),
        ("NetBotz50-MIB", "netBotzTrapErrorTypeLabel"),
        ("NetBotz50-MIB", "netBotzTrapSensorID"),
        ("NetBotz50-MIB", "netBotzTrapSensorLabel"),
        ("NetBotz50-MIB", "netBotzTrapContainerID"),
        ("NetBotz50-MIB", "netBotzTrapContainerLabel"),
        ("NetBotz50-MIB", "netBotzTrapPortID"),
        ("NetBotz50-MIB", "netBotzTrapPortLabel"),
        ("NetBotz50-MIB", "netBotzTrapStartTime"),
        ("NetBotz50-MIB", "netBotzTrapNotifyTime"),
        ("NetBotz50-MIB", "netBotzTrapResolveTime"),
        ("NetBotz50-MIB", "netBotzTrapSeverity"),
        ("NetBotz50-MIB", "netBotzTrapSensorValue"),
        ("NetBotz50-MIB", "netBotzTrapSensorValueInt"),
        ("NetBotz50-MIB", "netBotzTrapSensorValueFraction"))
)
if mibBuilder.loadTexts:
    netBotzCameraMotionSensorUnplugged.setStatus(
        "current"
    )

netBotzCameraMotionSensorValueError = NotificationType(
    (1, 3, 6, 1, 4, 1, 52674, 500, 10, 1, 7, 0, 10)
)
netBotzCameraMotionSensorValueError.setObjects(
      *(("NetBotz50-MIB", "netBotzTrapErrorID"),
        ("NetBotz50-MIB", "netBotzTrapErrorType"),
        ("NetBotz50-MIB", "netBotzTrapErrorTypeLabel"),
        ("NetBotz50-MIB", "netBotzTrapSensorID"),
        ("NetBotz50-MIB", "netBotzTrapSensorLabel"),
        ("NetBotz50-MIB", "netBotzTrapContainerID"),
        ("NetBotz50-MIB", "netBotzTrapContainerLabel"),
        ("NetBotz50-MIB", "netBotzTrapPortID"),
        ("NetBotz50-MIB", "netBotzTrapPortLabel"),
        ("NetBotz50-MIB", "netBotzTrapStartTime"),
        ("NetBotz50-MIB", "netBotzTrapNotifyTime"),
        ("NetBotz50-MIB", "netBotzTrapResolveTime"),
        ("NetBotz50-MIB", "netBotzTrapSeverity"),
        ("NetBotz50-MIB", "netBotzTrapSensorValue"),
        ("NetBotz50-MIB", "netBotzTrapSensorValueInt"),
        ("NetBotz50-MIB", "netBotzTrapSensorValueFraction"))
)
if mibBuilder.loadTexts:
    netBotzCameraMotionSensorValueError.setStatus(
        "current"
    )

netBotzCameraMotionSensorErrorRTN = NotificationType(
    (1, 3, 6, 1, 4, 1, 52674, 500, 10, 1, 7, 0, 101)
)
netBotzCameraMotionSensorErrorRTN.setObjects(
      *(("NetBotz50-MIB", "netBotzTrapErrorID"),
        ("NetBotz50-MIB", "netBotzTrapErrorType"),
        ("NetBotz50-MIB", "netBotzTrapErrorTypeLabel"),
        ("NetBotz50-MIB", "netBotzTrapSensorID"),
        ("NetBotz50-MIB", "netBotzTrapSensorLabel"),
        ("NetBotz50-MIB", "netBotzTrapContainerID"),
        ("NetBotz50-MIB", "netBotzTrapContainerLabel"),
        ("NetBotz50-MIB", "netBotzTrapPortID"),
        ("NetBotz50-MIB", "netBotzTrapPortLabel"),
        ("NetBotz50-MIB", "netBotzTrapStartTime"),
        ("NetBotz50-MIB", "netBotzTrapNotifyTime"),
        ("NetBotz50-MIB", "netBotzTrapResolveTime"),
        ("NetBotz50-MIB", "netBotzTrapSeverity"),
        ("NetBotz50-MIB", "netBotzTrapSensorValue"),
        ("NetBotz50-MIB", "netBotzTrapSensorValueInt"),
        ("NetBotz50-MIB", "netBotzTrapSensorValueFraction"))
)
if mibBuilder.loadTexts:
    netBotzCameraMotionSensorErrorRTN.setStatus(
        "current"
    )

netBotzCameraMotionSensorReplugged = NotificationType(
    (1, 3, 6, 1, 4, 1, 52674, 500, 10, 1, 7, 0, 106)
)
netBotzCameraMotionSensorReplugged.setObjects(
      *(("NetBotz50-MIB", "netBotzTrapErrorID"),
        ("NetBotz50-MIB", "netBotzTrapErrorType"),
        ("NetBotz50-MIB", "netBotzTrapErrorTypeLabel"),
        ("NetBotz50-MIB", "netBotzTrapSensorID"),
        ("NetBotz50-MIB", "netBotzTrapSensorLabel"),
        ("NetBotz50-MIB", "netBotzTrapContainerID"),
        ("NetBotz50-MIB", "netBotzTrapContainerLabel"),
        ("NetBotz50-MIB", "netBotzTrapPortID"),
        ("NetBotz50-MIB", "netBotzTrapPortLabel"),
        ("NetBotz50-MIB", "netBotzTrapStartTime"),
        ("NetBotz50-MIB", "netBotzTrapNotifyTime"),
        ("NetBotz50-MIB", "netBotzTrapResolveTime"),
        ("NetBotz50-MIB", "netBotzTrapSeverity"),
        ("NetBotz50-MIB", "netBotzTrapSensorValue"),
        ("NetBotz50-MIB", "netBotzTrapSensorValueInt"),
        ("NetBotz50-MIB", "netBotzTrapSensorValueFraction"))
)
if mibBuilder.loadTexts:
    netBotzCameraMotionSensorReplugged.setStatus(
        "current"
    )

netBotzCameraMotionSensorValueErrorRTN = NotificationType(
    (1, 3, 6, 1, 4, 1, 52674, 500, 10, 1, 7, 0, 110)
)
netBotzCameraMotionSensorValueErrorRTN.setObjects(
      *(("NetBotz50-MIB", "netBotzTrapErrorID"),
        ("NetBotz50-MIB", "netBotzTrapErrorType"),
        ("NetBotz50-MIB", "netBotzTrapErrorTypeLabel"),
        ("NetBotz50-MIB", "netBotzTrapSensorID"),
        ("NetBotz50-MIB", "netBotzTrapSensorLabel"),
        ("NetBotz50-MIB", "netBotzTrapContainerID"),
        ("NetBotz50-MIB", "netBotzTrapContainerLabel"),
        ("NetBotz50-MIB", "netBotzTrapPortID"),
        ("NetBotz50-MIB", "netBotzTrapPortLabel"),
        ("NetBotz50-MIB", "netBotzTrapStartTime"),
        ("NetBotz50-MIB", "netBotzTrapNotifyTime"),
        ("NetBotz50-MIB", "netBotzTrapResolveTime"),
        ("NetBotz50-MIB", "netBotzTrapSeverity"),
        ("NetBotz50-MIB", "netBotzTrapSensorValue"),
        ("NetBotz50-MIB", "netBotzTrapSensorValueInt"),
        ("NetBotz50-MIB", "netBotzTrapSensorValueFraction"))
)
if mibBuilder.loadTexts:
    netBotzCameraMotionSensorValueErrorRTN.setStatus(
        "current"
    )

netBotzDoorSensorError = NotificationType(
    (1, 3, 6, 1, 4, 1, 52674, 500, 10, 1, 8, 0, 1)
)
netBotzDoorSensorError.setObjects(
      *(("NetBotz50-MIB", "netBotzTrapErrorID"),
        ("NetBotz50-MIB", "netBotzTrapErrorType"),
        ("NetBotz50-MIB", "netBotzTrapErrorTypeLabel"),
        ("NetBotz50-MIB", "netBotzTrapSensorID"),
        ("NetBotz50-MIB", "netBotzTrapSensorLabel"),
        ("NetBotz50-MIB", "netBotzTrapContainerID"),
        ("NetBotz50-MIB", "netBotzTrapContainerLabel"),
        ("NetBotz50-MIB", "netBotzTrapPortID"),
        ("NetBotz50-MIB", "netBotzTrapPortLabel"),
        ("NetBotz50-MIB", "netBotzTrapStartTime"),
        ("NetBotz50-MIB", "netBotzTrapNotifyTime"),
        ("NetBotz50-MIB", "netBotzTrapResolveTime"),
        ("NetBotz50-MIB", "netBotzTrapSeverity"),
        ("NetBotz50-MIB", "netBotzTrapSensorValue"),
        ("NetBotz50-MIB", "netBotzTrapSensorValueInt"),
        ("NetBotz50-MIB", "netBotzTrapSensorValueFraction"))
)
if mibBuilder.loadTexts:
    netBotzDoorSensorError.setStatus(
        "current"
    )

netBotzDoorSensorUnplugged = NotificationType(
    (1, 3, 6, 1, 4, 1, 52674, 500, 10, 1, 8, 0, 6)
)
netBotzDoorSensorUnplugged.setObjects(
      *(("NetBotz50-MIB", "netBotzTrapErrorID"),
        ("NetBotz50-MIB", "netBotzTrapErrorType"),
        ("NetBotz50-MIB", "netBotzTrapErrorTypeLabel"),
        ("NetBotz50-MIB", "netBotzTrapSensorID"),
        ("NetBotz50-MIB", "netBotzTrapSensorLabel"),
        ("NetBotz50-MIB", "netBotzTrapContainerID"),
        ("NetBotz50-MIB", "netBotzTrapContainerLabel"),
        ("NetBotz50-MIB", "netBotzTrapPortID"),
        ("NetBotz50-MIB", "netBotzTrapPortLabel"),
        ("NetBotz50-MIB", "netBotzTrapStartTime"),
        ("NetBotz50-MIB", "netBotzTrapNotifyTime"),
        ("NetBotz50-MIB", "netBotzTrapResolveTime"),
        ("NetBotz50-MIB", "netBotzTrapSeverity"),
        ("NetBotz50-MIB", "netBotzTrapSensorValue"),
        ("NetBotz50-MIB", "netBotzTrapSensorValueInt"),
        ("NetBotz50-MIB", "netBotzTrapSensorValueFraction"))
)
if mibBuilder.loadTexts:
    netBotzDoorSensorUnplugged.setStatus(
        "current"
    )

netBotzDoorSensorValueError = NotificationType(
    (1, 3, 6, 1, 4, 1, 52674, 500, 10, 1, 8, 0, 10)
)
netBotzDoorSensorValueError.setObjects(
      *(("NetBotz50-MIB", "netBotzTrapErrorID"),
        ("NetBotz50-MIB", "netBotzTrapErrorType"),
        ("NetBotz50-MIB", "netBotzTrapErrorTypeLabel"),
        ("NetBotz50-MIB", "netBotzTrapSensorID"),
        ("NetBotz50-MIB", "netBotzTrapSensorLabel"),
        ("NetBotz50-MIB", "netBotzTrapContainerID"),
        ("NetBotz50-MIB", "netBotzTrapContainerLabel"),
        ("NetBotz50-MIB", "netBotzTrapPortID"),
        ("NetBotz50-MIB", "netBotzTrapPortLabel"),
        ("NetBotz50-MIB", "netBotzTrapStartTime"),
        ("NetBotz50-MIB", "netBotzTrapNotifyTime"),
        ("NetBotz50-MIB", "netBotzTrapResolveTime"),
        ("NetBotz50-MIB", "netBotzTrapSeverity"),
        ("NetBotz50-MIB", "netBotzTrapSensorValue"),
        ("NetBotz50-MIB", "netBotzTrapSensorValueInt"),
        ("NetBotz50-MIB", "netBotzTrapSensorValueFraction"))
)
if mibBuilder.loadTexts:
    netBotzDoorSensorValueError.setStatus(
        "current"
    )

netBotzDoorSensorErrorRTN = NotificationType(
    (1, 3, 6, 1, 4, 1, 52674, 500, 10, 1, 8, 0, 101)
)
netBotzDoorSensorErrorRTN.setObjects(
      *(("NetBotz50-MIB", "netBotzTrapErrorID"),
        ("NetBotz50-MIB", "netBotzTrapErrorType"),
        ("NetBotz50-MIB", "netBotzTrapErrorTypeLabel"),
        ("NetBotz50-MIB", "netBotzTrapSensorID"),
        ("NetBotz50-MIB", "netBotzTrapSensorLabel"),
        ("NetBotz50-MIB", "netBotzTrapContainerID"),
        ("NetBotz50-MIB", "netBotzTrapContainerLabel"),
        ("NetBotz50-MIB", "netBotzTrapPortID"),
        ("NetBotz50-MIB", "netBotzTrapPortLabel"),
        ("NetBotz50-MIB", "netBotzTrapStartTime"),
        ("NetBotz50-MIB", "netBotzTrapNotifyTime"),
        ("NetBotz50-MIB", "netBotzTrapResolveTime"),
        ("NetBotz50-MIB", "netBotzTrapSeverity"),
        ("NetBotz50-MIB", "netBotzTrapSensorValue"),
        ("NetBotz50-MIB", "netBotzTrapSensorValueInt"),
        ("NetBotz50-MIB", "netBotzTrapSensorValueFraction"))
)
if mibBuilder.loadTexts:
    netBotzDoorSensorErrorRTN.setStatus(
        "current"
    )

netBotzDoorSensorReplugged = NotificationType(
    (1, 3, 6, 1, 4, 1, 52674, 500, 10, 1, 8, 0, 106)
)
netBotzDoorSensorReplugged.setObjects(
      *(("NetBotz50-MIB", "netBotzTrapErrorID"),
        ("NetBotz50-MIB", "netBotzTrapErrorType"),
        ("NetBotz50-MIB", "netBotzTrapErrorTypeLabel"),
        ("NetBotz50-MIB", "netBotzTrapSensorID"),
        ("NetBotz50-MIB", "netBotzTrapSensorLabel"),
        ("NetBotz50-MIB", "netBotzTrapContainerID"),
        ("NetBotz50-MIB", "netBotzTrapContainerLabel"),
        ("NetBotz50-MIB", "netBotzTrapPortID"),
        ("NetBotz50-MIB", "netBotzTrapPortLabel"),
        ("NetBotz50-MIB", "netBotzTrapStartTime"),
        ("NetBotz50-MIB", "netBotzTrapNotifyTime"),
        ("NetBotz50-MIB", "netBotzTrapResolveTime"),
        ("NetBotz50-MIB", "netBotzTrapSeverity"),
        ("NetBotz50-MIB", "netBotzTrapSensorValue"),
        ("NetBotz50-MIB", "netBotzTrapSensorValueInt"),
        ("NetBotz50-MIB", "netBotzTrapSensorValueFraction"))
)
if mibBuilder.loadTexts:
    netBotzDoorSensorReplugged.setStatus(
        "current"
    )

netBotzDoorSensorValueErrorRTN = NotificationType(
    (1, 3, 6, 1, 4, 1, 52674, 500, 10, 1, 8, 0, 110)
)
netBotzDoorSensorValueErrorRTN.setObjects(
      *(("NetBotz50-MIB", "netBotzTrapErrorID"),
        ("NetBotz50-MIB", "netBotzTrapErrorType"),
        ("NetBotz50-MIB", "netBotzTrapErrorTypeLabel"),
        ("NetBotz50-MIB", "netBotzTrapSensorID"),
        ("NetBotz50-MIB", "netBotzTrapSensorLabel"),
        ("NetBotz50-MIB", "netBotzTrapContainerID"),
        ("NetBotz50-MIB", "netBotzTrapContainerLabel"),
        ("NetBotz50-MIB", "netBotzTrapPortID"),
        ("NetBotz50-MIB", "netBotzTrapPortLabel"),
        ("NetBotz50-MIB", "netBotzTrapStartTime"),
        ("NetBotz50-MIB", "netBotzTrapNotifyTime"),
        ("NetBotz50-MIB", "netBotzTrapResolveTime"),
        ("NetBotz50-MIB", "netBotzTrapSeverity"),
        ("NetBotz50-MIB", "netBotzTrapSensorValue"),
        ("NetBotz50-MIB", "netBotzTrapSensorValueInt"),
        ("NetBotz50-MIB", "netBotzTrapSensorValueFraction"))
)
if mibBuilder.loadTexts:
    netBotzDoorSensorValueErrorRTN.setStatus(
        "current"
    )

netBotzWirelessStatusSensorError = NotificationType(
    (1, 3, 6, 1, 4, 1, 52674, 500, 10, 1, 9, 0, 1)
)
netBotzWirelessStatusSensorError.setObjects(
      *(("NetBotz50-MIB", "netBotzTrapErrorID"),
        ("NetBotz50-MIB", "netBotzTrapErrorType"),
        ("NetBotz50-MIB", "netBotzTrapErrorTypeLabel"),
        ("NetBotz50-MIB", "netBotzTrapSensorID"),
        ("NetBotz50-MIB", "netBotzTrapSensorLabel"),
        ("NetBotz50-MIB", "netBotzTrapContainerID"),
        ("NetBotz50-MIB", "netBotzTrapContainerLabel"),
        ("NetBotz50-MIB", "netBotzTrapPortID"),
        ("NetBotz50-MIB", "netBotzTrapPortLabel"),
        ("NetBotz50-MIB", "netBotzTrapStartTime"),
        ("NetBotz50-MIB", "netBotzTrapNotifyTime"),
        ("NetBotz50-MIB", "netBotzTrapResolveTime"),
        ("NetBotz50-MIB", "netBotzTrapSeverity"),
        ("NetBotz50-MIB", "netBotzTrapSensorValue"),
        ("NetBotz50-MIB", "netBotzTrapSensorValueInt"),
        ("NetBotz50-MIB", "netBotzTrapSensorValueFraction"))
)
if mibBuilder.loadTexts:
    netBotzWirelessStatusSensorError.setStatus(
        "current"
    )

netBotzWirelessStatusSensorUnplugged = NotificationType(
    (1, 3, 6, 1, 4, 1, 52674, 500, 10, 1, 9, 0, 6)
)
netBotzWirelessStatusSensorUnplugged.setObjects(
      *(("NetBotz50-MIB", "netBotzTrapErrorID"),
        ("NetBotz50-MIB", "netBotzTrapErrorType"),
        ("NetBotz50-MIB", "netBotzTrapErrorTypeLabel"),
        ("NetBotz50-MIB", "netBotzTrapSensorID"),
        ("NetBotz50-MIB", "netBotzTrapSensorLabel"),
        ("NetBotz50-MIB", "netBotzTrapContainerID"),
        ("NetBotz50-MIB", "netBotzTrapContainerLabel"),
        ("NetBotz50-MIB", "netBotzTrapPortID"),
        ("NetBotz50-MIB", "netBotzTrapPortLabel"),
        ("NetBotz50-MIB", "netBotzTrapStartTime"),
        ("NetBotz50-MIB", "netBotzTrapNotifyTime"),
        ("NetBotz50-MIB", "netBotzTrapResolveTime"),
        ("NetBotz50-MIB", "netBotzTrapSeverity"),
        ("NetBotz50-MIB", "netBotzTrapSensorValue"),
        ("NetBotz50-MIB", "netBotzTrapSensorValueInt"),
        ("NetBotz50-MIB", "netBotzTrapSensorValueFraction"))
)
if mibBuilder.loadTexts:
    netBotzWirelessStatusSensorUnplugged.setStatus(
        "current"
    )

netBotzWirelessStatusSensorValueError = NotificationType(
    (1, 3, 6, 1, 4, 1, 52674, 500, 10, 1, 9, 0, 10)
)
netBotzWirelessStatusSensorValueError.setObjects(
      *(("NetBotz50-MIB", "netBotzTrapErrorID"),
        ("NetBotz50-MIB", "netBotzTrapErrorType"),
        ("NetBotz50-MIB", "netBotzTrapErrorTypeLabel"),
        ("NetBotz50-MIB", "netBotzTrapSensorID"),
        ("NetBotz50-MIB", "netBotzTrapSensorLabel"),
        ("NetBotz50-MIB", "netBotzTrapContainerID"),
        ("NetBotz50-MIB", "netBotzTrapContainerLabel"),
        ("NetBotz50-MIB", "netBotzTrapPortID"),
        ("NetBotz50-MIB", "netBotzTrapPortLabel"),
        ("NetBotz50-MIB", "netBotzTrapStartTime"),
        ("NetBotz50-MIB", "netBotzTrapNotifyTime"),
        ("NetBotz50-MIB", "netBotzTrapResolveTime"),
        ("NetBotz50-MIB", "netBotzTrapSeverity"),
        ("NetBotz50-MIB", "netBotzTrapSensorValue"),
        ("NetBotz50-MIB", "netBotzTrapSensorValueInt"),
        ("NetBotz50-MIB", "netBotzTrapSensorValueFraction"))
)
if mibBuilder.loadTexts:
    netBotzWirelessStatusSensorValueError.setStatus(
        "current"
    )

netBotzWirelessStatusSensorErrorRTN = NotificationType(
    (1, 3, 6, 1, 4, 1, 52674, 500, 10, 1, 9, 0, 101)
)
netBotzWirelessStatusSensorErrorRTN.setObjects(
      *(("NetBotz50-MIB", "netBotzTrapErrorID"),
        ("NetBotz50-MIB", "netBotzTrapErrorType"),
        ("NetBotz50-MIB", "netBotzTrapErrorTypeLabel"),
        ("NetBotz50-MIB", "netBotzTrapSensorID"),
        ("NetBotz50-MIB", "netBotzTrapSensorLabel"),
        ("NetBotz50-MIB", "netBotzTrapContainerID"),
        ("NetBotz50-MIB", "netBotzTrapContainerLabel"),
        ("NetBotz50-MIB", "netBotzTrapPortID"),
        ("NetBotz50-MIB", "netBotzTrapPortLabel"),
        ("NetBotz50-MIB", "netBotzTrapStartTime"),
        ("NetBotz50-MIB", "netBotzTrapNotifyTime"),
        ("NetBotz50-MIB", "netBotzTrapResolveTime"),
        ("NetBotz50-MIB", "netBotzTrapSeverity"),
        ("NetBotz50-MIB", "netBotzTrapSensorValue"),
        ("NetBotz50-MIB", "netBotzTrapSensorValueInt"),
        ("NetBotz50-MIB", "netBotzTrapSensorValueFraction"))
)
if mibBuilder.loadTexts:
    netBotzWirelessStatusSensorErrorRTN.setStatus(
        "current"
    )

netBotzWirelessStatusSensorReplugged = NotificationType(
    (1, 3, 6, 1, 4, 1, 52674, 500, 10, 1, 9, 0, 106)
)
netBotzWirelessStatusSensorReplugged.setObjects(
      *(("NetBotz50-MIB", "netBotzTrapErrorID"),
        ("NetBotz50-MIB", "netBotzTrapErrorType"),
        ("NetBotz50-MIB", "netBotzTrapErrorTypeLabel"),
        ("NetBotz50-MIB", "netBotzTrapSensorID"),
        ("NetBotz50-MIB", "netBotzTrapSensorLabel"),
        ("NetBotz50-MIB", "netBotzTrapContainerID"),
        ("NetBotz50-MIB", "netBotzTrapContainerLabel"),
        ("NetBotz50-MIB", "netBotzTrapPortID"),
        ("NetBotz50-MIB", "netBotzTrapPortLabel"),
        ("NetBotz50-MIB", "netBotzTrapStartTime"),
        ("NetBotz50-MIB", "netBotzTrapNotifyTime"),
        ("NetBotz50-MIB", "netBotzTrapResolveTime"),
        ("NetBotz50-MIB", "netBotzTrapSeverity"),
        ("NetBotz50-MIB", "netBotzTrapSensorValue"),
        ("NetBotz50-MIB", "netBotzTrapSensorValueInt"),
        ("NetBotz50-MIB", "netBotzTrapSensorValueFraction"))
)
if mibBuilder.loadTexts:
    netBotzWirelessStatusSensorReplugged.setStatus(
        "current"
    )

netBotzWirelessStatusSensorValueErrorRTN = NotificationType(
    (1, 3, 6, 1, 4, 1, 52674, 500, 10, 1, 9, 0, 110)
)
netBotzWirelessStatusSensorValueErrorRTN.setObjects(
      *(("NetBotz50-MIB", "netBotzTrapErrorID"),
        ("NetBotz50-MIB", "netBotzTrapErrorType"),
        ("NetBotz50-MIB", "netBotzTrapErrorTypeLabel"),
        ("NetBotz50-MIB", "netBotzTrapSensorID"),
        ("NetBotz50-MIB", "netBotzTrapSensorLabel"),
        ("NetBotz50-MIB", "netBotzTrapContainerID"),
        ("NetBotz50-MIB", "netBotzTrapContainerLabel"),
        ("NetBotz50-MIB", "netBotzTrapPortID"),
        ("NetBotz50-MIB", "netBotzTrapPortLabel"),
        ("NetBotz50-MIB", "netBotzTrapStartTime"),
        ("NetBotz50-MIB", "netBotzTrapNotifyTime"),
        ("NetBotz50-MIB", "netBotzTrapResolveTime"),
        ("NetBotz50-MIB", "netBotzTrapSeverity"),
        ("NetBotz50-MIB", "netBotzTrapSensorValue"),
        ("NetBotz50-MIB", "netBotzTrapSensorValueInt"),
        ("NetBotz50-MIB", "netBotzTrapSensorValueFraction"))
)
if mibBuilder.loadTexts:
    netBotzWirelessStatusSensorValueErrorRTN.setStatus(
        "current"
    )

netBotzOutputControlSensorError = NotificationType(
    (1, 3, 6, 1, 4, 1, 52674, 500, 10, 1, 10, 0, 1)
)
netBotzOutputControlSensorError.setObjects(
      *(("NetBotz50-MIB", "netBotzTrapErrorID"),
        ("NetBotz50-MIB", "netBotzTrapErrorType"),
        ("NetBotz50-MIB", "netBotzTrapErrorTypeLabel"),
        ("NetBotz50-MIB", "netBotzTrapSensorID"),
        ("NetBotz50-MIB", "netBotzTrapSensorLabel"),
        ("NetBotz50-MIB", "netBotzTrapContainerID"),
        ("NetBotz50-MIB", "netBotzTrapContainerLabel"),
        ("NetBotz50-MIB", "netBotzTrapPortID"),
        ("NetBotz50-MIB", "netBotzTrapPortLabel"),
        ("NetBotz50-MIB", "netBotzTrapStartTime"),
        ("NetBotz50-MIB", "netBotzTrapNotifyTime"),
        ("NetBotz50-MIB", "netBotzTrapResolveTime"),
        ("NetBotz50-MIB", "netBotzTrapSeverity"),
        ("NetBotz50-MIB", "netBotzTrapSensorValue"),
        ("NetBotz50-MIB", "netBotzTrapSensorValueInt"),
        ("NetBotz50-MIB", "netBotzTrapSensorValueFraction"))
)
if mibBuilder.loadTexts:
    netBotzOutputControlSensorError.setStatus(
        "current"
    )

netBotzOutputControlSensorUnplugged = NotificationType(
    (1, 3, 6, 1, 4, 1, 52674, 500, 10, 1, 10, 0, 6)
)
netBotzOutputControlSensorUnplugged.setObjects(
      *(("NetBotz50-MIB", "netBotzTrapErrorID"),
        ("NetBotz50-MIB", "netBotzTrapErrorType"),
        ("NetBotz50-MIB", "netBotzTrapErrorTypeLabel"),
        ("NetBotz50-MIB", "netBotzTrapSensorID"),
        ("NetBotz50-MIB", "netBotzTrapSensorLabel"),
        ("NetBotz50-MIB", "netBotzTrapContainerID"),
        ("NetBotz50-MIB", "netBotzTrapContainerLabel"),
        ("NetBotz50-MIB", "netBotzTrapPortID"),
        ("NetBotz50-MIB", "netBotzTrapPortLabel"),
        ("NetBotz50-MIB", "netBotzTrapStartTime"),
        ("NetBotz50-MIB", "netBotzTrapNotifyTime"),
        ("NetBotz50-MIB", "netBotzTrapResolveTime"),
        ("NetBotz50-MIB", "netBotzTrapSeverity"),
        ("NetBotz50-MIB", "netBotzTrapSensorValue"),
        ("NetBotz50-MIB", "netBotzTrapSensorValueInt"),
        ("NetBotz50-MIB", "netBotzTrapSensorValueFraction"))
)
if mibBuilder.loadTexts:
    netBotzOutputControlSensorUnplugged.setStatus(
        "current"
    )

netBotzOutputControlSensorValueError = NotificationType(
    (1, 3, 6, 1, 4, 1, 52674, 500, 10, 1, 10, 0, 10)
)
netBotzOutputControlSensorValueError.setObjects(
      *(("NetBotz50-MIB", "netBotzTrapErrorID"),
        ("NetBotz50-MIB", "netBotzTrapErrorType"),
        ("NetBotz50-MIB", "netBotzTrapErrorTypeLabel"),
        ("NetBotz50-MIB", "netBotzTrapSensorID"),
        ("NetBotz50-MIB", "netBotzTrapSensorLabel"),
        ("NetBotz50-MIB", "netBotzTrapContainerID"),
        ("NetBotz50-MIB", "netBotzTrapContainerLabel"),
        ("NetBotz50-MIB", "netBotzTrapPortID"),
        ("NetBotz50-MIB", "netBotzTrapPortLabel"),
        ("NetBotz50-MIB", "netBotzTrapStartTime"),
        ("NetBotz50-MIB", "netBotzTrapNotifyTime"),
        ("NetBotz50-MIB", "netBotzTrapResolveTime"),
        ("NetBotz50-MIB", "netBotzTrapSeverity"),
        ("NetBotz50-MIB", "netBotzTrapSensorValue"),
        ("NetBotz50-MIB", "netBotzTrapSensorValueInt"),
        ("NetBotz50-MIB", "netBotzTrapSensorValueFraction"))
)
if mibBuilder.loadTexts:
    netBotzOutputControlSensorValueError.setStatus(
        "current"
    )

netBotzOutputControlSensorErrorRTN = NotificationType(
    (1, 3, 6, 1, 4, 1, 52674, 500, 10, 1, 10, 0, 101)
)
netBotzOutputControlSensorErrorRTN.setObjects(
      *(("NetBotz50-MIB", "netBotzTrapErrorID"),
        ("NetBotz50-MIB", "netBotzTrapErrorType"),
        ("NetBotz50-MIB", "netBotzTrapErrorTypeLabel"),
        ("NetBotz50-MIB", "netBotzTrapSensorID"),
        ("NetBotz50-MIB", "netBotzTrapSensorLabel"),
        ("NetBotz50-MIB", "netBotzTrapContainerID"),
        ("NetBotz50-MIB", "netBotzTrapContainerLabel"),
        ("NetBotz50-MIB", "netBotzTrapPortID"),
        ("NetBotz50-MIB", "netBotzTrapPortLabel"),
        ("NetBotz50-MIB", "netBotzTrapStartTime"),
        ("NetBotz50-MIB", "netBotzTrapNotifyTime"),
        ("NetBotz50-MIB", "netBotzTrapResolveTime"),
        ("NetBotz50-MIB", "netBotzTrapSeverity"),
        ("NetBotz50-MIB", "netBotzTrapSensorValue"),
        ("NetBotz50-MIB", "netBotzTrapSensorValueInt"),
        ("NetBotz50-MIB", "netBotzTrapSensorValueFraction"))
)
if mibBuilder.loadTexts:
    netBotzOutputControlSensorErrorRTN.setStatus(
        "current"
    )

netBotzOutputControlSensorReplugged = NotificationType(
    (1, 3, 6, 1, 4, 1, 52674, 500, 10, 1, 10, 0, 106)
)
netBotzOutputControlSensorReplugged.setObjects(
      *(("NetBotz50-MIB", "netBotzTrapErrorID"),
        ("NetBotz50-MIB", "netBotzTrapErrorType"),
        ("NetBotz50-MIB", "netBotzTrapErrorTypeLabel"),
        ("NetBotz50-MIB", "netBotzTrapSensorID"),
        ("NetBotz50-MIB", "netBotzTrapSensorLabel"),
        ("NetBotz50-MIB", "netBotzTrapContainerID"),
        ("NetBotz50-MIB", "netBotzTrapContainerLabel"),
        ("NetBotz50-MIB", "netBotzTrapPortID"),
        ("NetBotz50-MIB", "netBotzTrapPortLabel"),
        ("NetBotz50-MIB", "netBotzTrapStartTime"),
        ("NetBotz50-MIB", "netBotzTrapNotifyTime"),
        ("NetBotz50-MIB", "netBotzTrapResolveTime"),
        ("NetBotz50-MIB", "netBotzTrapSeverity"),
        ("NetBotz50-MIB", "netBotzTrapSensorValue"),
        ("NetBotz50-MIB", "netBotzTrapSensorValueInt"),
        ("NetBotz50-MIB", "netBotzTrapSensorValueFraction"))
)
if mibBuilder.loadTexts:
    netBotzOutputControlSensorReplugged.setStatus(
        "current"
    )

netBotzOutputControlSensorValueErrorRTN = NotificationType(
    (1, 3, 6, 1, 4, 1, 52674, 500, 10, 1, 10, 0, 110)
)
netBotzOutputControlSensorValueErrorRTN.setObjects(
      *(("NetBotz50-MIB", "netBotzTrapErrorID"),
        ("NetBotz50-MIB", "netBotzTrapErrorType"),
        ("NetBotz50-MIB", "netBotzTrapErrorTypeLabel"),
        ("NetBotz50-MIB", "netBotzTrapSensorID"),
        ("NetBotz50-MIB", "netBotzTrapSensorLabel"),
        ("NetBotz50-MIB", "netBotzTrapContainerID"),
        ("NetBotz50-MIB", "netBotzTrapContainerLabel"),
        ("NetBotz50-MIB", "netBotzTrapPortID"),
        ("NetBotz50-MIB", "netBotzTrapPortLabel"),
        ("NetBotz50-MIB", "netBotzTrapStartTime"),
        ("NetBotz50-MIB", "netBotzTrapNotifyTime"),
        ("NetBotz50-MIB", "netBotzTrapResolveTime"),
        ("NetBotz50-MIB", "netBotzTrapSeverity"),
        ("NetBotz50-MIB", "netBotzTrapSensorValue"),
        ("NetBotz50-MIB", "netBotzTrapSensorValueInt"),
        ("NetBotz50-MIB", "netBotzTrapSensorValueFraction"))
)
if mibBuilder.loadTexts:
    netBotzOutputControlSensorValueErrorRTN.setStatus(
        "current"
    )

netBotzLoopVoltageError = NotificationType(
    (1, 3, 6, 1, 4, 1, 52674, 500, 10, 1, 11, 0, 1)
)
netBotzLoopVoltageError.setObjects(
      *(("NetBotz50-MIB", "netBotzTrapErrorID"),
        ("NetBotz50-MIB", "netBotzTrapErrorType"),
        ("NetBotz50-MIB", "netBotzTrapErrorTypeLabel"),
        ("NetBotz50-MIB", "netBotzTrapSensorID"),
        ("NetBotz50-MIB", "netBotzTrapSensorLabel"),
        ("NetBotz50-MIB", "netBotzTrapContainerID"),
        ("NetBotz50-MIB", "netBotzTrapContainerLabel"),
        ("NetBotz50-MIB", "netBotzTrapPortID"),
        ("NetBotz50-MIB", "netBotzTrapPortLabel"),
        ("NetBotz50-MIB", "netBotzTrapStartTime"),
        ("NetBotz50-MIB", "netBotzTrapNotifyTime"),
        ("NetBotz50-MIB", "netBotzTrapResolveTime"),
        ("NetBotz50-MIB", "netBotzTrapSeverity"),
        ("NetBotz50-MIB", "netBotzTrapSensorValue"),
        ("NetBotz50-MIB", "netBotzTrapSensorValueInt"),
        ("NetBotz50-MIB", "netBotzTrapSensorValueFraction"))
)
if mibBuilder.loadTexts:
    netBotzLoopVoltageError.setStatus(
        "current"
    )

netBotzLoopVoltageTooHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 52674, 500, 10, 1, 11, 0, 2)
)
netBotzLoopVoltageTooHigh.setObjects(
      *(("NetBotz50-MIB", "netBotzTrapErrorID"),
        ("NetBotz50-MIB", "netBotzTrapErrorType"),
        ("NetBotz50-MIB", "netBotzTrapErrorTypeLabel"),
        ("NetBotz50-MIB", "netBotzTrapSensorID"),
        ("NetBotz50-MIB", "netBotzTrapSensorLabel"),
        ("NetBotz50-MIB", "netBotzTrapContainerID"),
        ("NetBotz50-MIB", "netBotzTrapContainerLabel"),
        ("NetBotz50-MIB", "netBotzTrapPortID"),
        ("NetBotz50-MIB", "netBotzTrapPortLabel"),
        ("NetBotz50-MIB", "netBotzTrapStartTime"),
        ("NetBotz50-MIB", "netBotzTrapNotifyTime"),
        ("NetBotz50-MIB", "netBotzTrapResolveTime"),
        ("NetBotz50-MIB", "netBotzTrapSeverity"),
        ("NetBotz50-MIB", "netBotzTrapSensorValue"),
        ("NetBotz50-MIB", "netBotzTrapSensorValueInt"),
        ("NetBotz50-MIB", "netBotzTrapSensorValueFraction"))
)
if mibBuilder.loadTexts:
    netBotzLoopVoltageTooHigh.setStatus(
        "current"
    )

netBotzLoopVoltageTooLow = NotificationType(
    (1, 3, 6, 1, 4, 1, 52674, 500, 10, 1, 11, 0, 3)
)
netBotzLoopVoltageTooLow.setObjects(
      *(("NetBotz50-MIB", "netBotzTrapErrorID"),
        ("NetBotz50-MIB", "netBotzTrapErrorType"),
        ("NetBotz50-MIB", "netBotzTrapErrorTypeLabel"),
        ("NetBotz50-MIB", "netBotzTrapSensorID"),
        ("NetBotz50-MIB", "netBotzTrapSensorLabel"),
        ("NetBotz50-MIB", "netBotzTrapContainerID"),
        ("NetBotz50-MIB", "netBotzTrapContainerLabel"),
        ("NetBotz50-MIB", "netBotzTrapPortID"),
        ("NetBotz50-MIB", "netBotzTrapPortLabel"),
        ("NetBotz50-MIB", "netBotzTrapStartTime"),
        ("NetBotz50-MIB", "netBotzTrapNotifyTime"),
        ("NetBotz50-MIB", "netBotzTrapResolveTime"),
        ("NetBotz50-MIB", "netBotzTrapSeverity"),
        ("NetBotz50-MIB", "netBotzTrapSensorValue"),
        ("NetBotz50-MIB", "netBotzTrapSensorValueInt"),
        ("NetBotz50-MIB", "netBotzTrapSensorValueFraction"))
)
if mibBuilder.loadTexts:
    netBotzLoopVoltageTooLow.setStatus(
        "current"
    )

netBotzLoopVoltageUnplugged = NotificationType(
    (1, 3, 6, 1, 4, 1, 52674, 500, 10, 1, 11, 0, 6)
)
netBotzLoopVoltageUnplugged.setObjects(
      *(("NetBotz50-MIB", "netBotzTrapErrorID"),
        ("NetBotz50-MIB", "netBotzTrapErrorType"),
        ("NetBotz50-MIB", "netBotzTrapErrorTypeLabel"),
        ("NetBotz50-MIB", "netBotzTrapSensorID"),
        ("NetBotz50-MIB", "netBotzTrapSensorLabel"),
        ("NetBotz50-MIB", "netBotzTrapContainerID"),
        ("NetBotz50-MIB", "netBotzTrapContainerLabel"),
        ("NetBotz50-MIB", "netBotzTrapPortID"),
        ("NetBotz50-MIB", "netBotzTrapPortLabel"),
        ("NetBotz50-MIB", "netBotzTrapStartTime"),
        ("NetBotz50-MIB", "netBotzTrapNotifyTime"),
        ("NetBotz50-MIB", "netBotzTrapResolveTime"),
        ("NetBotz50-MIB", "netBotzTrapSeverity"),
        ("NetBotz50-MIB", "netBotzTrapSensorValue"),
        ("NetBotz50-MIB", "netBotzTrapSensorValueInt"),
        ("NetBotz50-MIB", "netBotzTrapSensorValueFraction"))
)
if mibBuilder.loadTexts:
    netBotzLoopVoltageUnplugged.setStatus(
        "current"
    )

netBotzLoopVoltageErrorRTN = NotificationType(
    (1, 3, 6, 1, 4, 1, 52674, 500, 10, 1, 11, 0, 101)
)
netBotzLoopVoltageErrorRTN.setObjects(
      *(("NetBotz50-MIB", "netBotzTrapErrorID"),
        ("NetBotz50-MIB", "netBotzTrapErrorType"),
        ("NetBotz50-MIB", "netBotzTrapErrorTypeLabel"),
        ("NetBotz50-MIB", "netBotzTrapSensorID"),
        ("NetBotz50-MIB", "netBotzTrapSensorLabel"),
        ("NetBotz50-MIB", "netBotzTrapContainerID"),
        ("NetBotz50-MIB", "netBotzTrapContainerLabel"),
        ("NetBotz50-MIB", "netBotzTrapPortID"),
        ("NetBotz50-MIB", "netBotzTrapPortLabel"),
        ("NetBotz50-MIB", "netBotzTrapStartTime"),
        ("NetBotz50-MIB", "netBotzTrapNotifyTime"),
        ("NetBotz50-MIB", "netBotzTrapResolveTime"),
        ("NetBotz50-MIB", "netBotzTrapSeverity"),
        ("NetBotz50-MIB", "netBotzTrapSensorValue"),
        ("NetBotz50-MIB", "netBotzTrapSensorValueInt"),
        ("NetBotz50-MIB", "netBotzTrapSensorValueFraction"))
)
if mibBuilder.loadTexts:
    netBotzLoopVoltageErrorRTN.setStatus(
        "current"
    )

netBotzLoopVoltageTooHighRTN = NotificationType(
    (1, 3, 6, 1, 4, 1, 52674, 500, 10, 1, 11, 0, 102)
)
netBotzLoopVoltageTooHighRTN.setObjects(
      *(("NetBotz50-MIB", "netBotzTrapErrorID"),
        ("NetBotz50-MIB", "netBotzTrapErrorType"),
        ("NetBotz50-MIB", "netBotzTrapErrorTypeLabel"),
        ("NetBotz50-MIB", "netBotzTrapSensorID"),
        ("NetBotz50-MIB", "netBotzTrapSensorLabel"),
        ("NetBotz50-MIB", "netBotzTrapContainerID"),
        ("NetBotz50-MIB", "netBotzTrapContainerLabel"),
        ("NetBotz50-MIB", "netBotzTrapPortID"),
        ("NetBotz50-MIB", "netBotzTrapPortLabel"),
        ("NetBotz50-MIB", "netBotzTrapStartTime"),
        ("NetBotz50-MIB", "netBotzTrapNotifyTime"),
        ("NetBotz50-MIB", "netBotzTrapResolveTime"),
        ("NetBotz50-MIB", "netBotzTrapSeverity"),
        ("NetBotz50-MIB", "netBotzTrapSensorValue"),
        ("NetBotz50-MIB", "netBotzTrapSensorValueInt"),
        ("NetBotz50-MIB", "netBotzTrapSensorValueFraction"))
)
if mibBuilder.loadTexts:
    netBotzLoopVoltageTooHighRTN.setStatus(
        "current"
    )

netBotzLoopVoltageTooLowRTN = NotificationType(
    (1, 3, 6, 1, 4, 1, 52674, 500, 10, 1, 11, 0, 103)
)
netBotzLoopVoltageTooLowRTN.setObjects(
      *(("NetBotz50-MIB", "netBotzTrapErrorID"),
        ("NetBotz50-MIB", "netBotzTrapErrorType"),
        ("NetBotz50-MIB", "netBotzTrapErrorTypeLabel"),
        ("NetBotz50-MIB", "netBotzTrapSensorID"),
        ("NetBotz50-MIB", "netBotzTrapSensorLabel"),
        ("NetBotz50-MIB", "netBotzTrapContainerID"),
        ("NetBotz50-MIB", "netBotzTrapContainerLabel"),
        ("NetBotz50-MIB", "netBotzTrapPortID"),
        ("NetBotz50-MIB", "netBotzTrapPortLabel"),
        ("NetBotz50-MIB", "netBotzTrapStartTime"),
        ("NetBotz50-MIB", "netBotzTrapNotifyTime"),
        ("NetBotz50-MIB", "netBotzTrapResolveTime"),
        ("NetBotz50-MIB", "netBotzTrapSeverity"),
        ("NetBotz50-MIB", "netBotzTrapSensorValue"),
        ("NetBotz50-MIB", "netBotzTrapSensorValueInt"),
        ("NetBotz50-MIB", "netBotzTrapSensorValueFraction"))
)
if mibBuilder.loadTexts:
    netBotzLoopVoltageTooLowRTN.setStatus(
        "current"
    )

netBotzLoopVoltageReplugged = NotificationType(
    (1, 3, 6, 1, 4, 1, 52674, 500, 10, 1, 11, 0, 106)
)
netBotzLoopVoltageReplugged.setObjects(
      *(("NetBotz50-MIB", "netBotzTrapErrorID"),
        ("NetBotz50-MIB", "netBotzTrapErrorType"),
        ("NetBotz50-MIB", "netBotzTrapErrorTypeLabel"),
        ("NetBotz50-MIB", "netBotzTrapSensorID"),
        ("NetBotz50-MIB", "netBotzTrapSensorLabel"),
        ("NetBotz50-MIB", "netBotzTrapContainerID"),
        ("NetBotz50-MIB", "netBotzTrapContainerLabel"),
        ("NetBotz50-MIB", "netBotzTrapPortID"),
        ("NetBotz50-MIB", "netBotzTrapPortLabel"),
        ("NetBotz50-MIB", "netBotzTrapStartTime"),
        ("NetBotz50-MIB", "netBotzTrapNotifyTime"),
        ("NetBotz50-MIB", "netBotzTrapResolveTime"),
        ("NetBotz50-MIB", "netBotzTrapSeverity"),
        ("NetBotz50-MIB", "netBotzTrapSensorValue"),
        ("NetBotz50-MIB", "netBotzTrapSensorValueInt"),
        ("NetBotz50-MIB", "netBotzTrapSensorValueFraction"))
)
if mibBuilder.loadTexts:
    netBotzLoopVoltageReplugged.setStatus(
        "current"
    )

netBotzSpotLeakSensorError = NotificationType(
    (1, 3, 6, 1, 4, 1, 52674, 500, 10, 1, 12, 0, 1)
)
netBotzSpotLeakSensorError.setObjects(
      *(("NetBotz50-MIB", "netBotzTrapErrorID"),
        ("NetBotz50-MIB", "netBotzTrapErrorType"),
        ("NetBotz50-MIB", "netBotzTrapErrorTypeLabel"),
        ("NetBotz50-MIB", "netBotzTrapSensorID"),
        ("NetBotz50-MIB", "netBotzTrapSensorLabel"),
        ("NetBotz50-MIB", "netBotzTrapContainerID"),
        ("NetBotz50-MIB", "netBotzTrapContainerLabel"),
        ("NetBotz50-MIB", "netBotzTrapPortID"),
        ("NetBotz50-MIB", "netBotzTrapPortLabel"),
        ("NetBotz50-MIB", "netBotzTrapStartTime"),
        ("NetBotz50-MIB", "netBotzTrapNotifyTime"),
        ("NetBotz50-MIB", "netBotzTrapResolveTime"),
        ("NetBotz50-MIB", "netBotzTrapSeverity"),
        ("NetBotz50-MIB", "netBotzTrapSensorValue"),
        ("NetBotz50-MIB", "netBotzTrapSensorValueInt"),
        ("NetBotz50-MIB", "netBotzTrapSensorValueFraction"))
)
if mibBuilder.loadTexts:
    netBotzSpotLeakSensorError.setStatus(
        "current"
    )

netBotzSpotLeakSensorUnplugged = NotificationType(
    (1, 3, 6, 1, 4, 1, 52674, 500, 10, 1, 12, 0, 6)
)
netBotzSpotLeakSensorUnplugged.setObjects(
      *(("NetBotz50-MIB", "netBotzTrapErrorID"),
        ("NetBotz50-MIB", "netBotzTrapErrorType"),
        ("NetBotz50-MIB", "netBotzTrapErrorTypeLabel"),
        ("NetBotz50-MIB", "netBotzTrapSensorID"),
        ("NetBotz50-MIB", "netBotzTrapSensorLabel"),
        ("NetBotz50-MIB", "netBotzTrapContainerID"),
        ("NetBotz50-MIB", "netBotzTrapContainerLabel"),
        ("NetBotz50-MIB", "netBotzTrapPortID"),
        ("NetBotz50-MIB", "netBotzTrapPortLabel"),
        ("NetBotz50-MIB", "netBotzTrapStartTime"),
        ("NetBotz50-MIB", "netBotzTrapNotifyTime"),
        ("NetBotz50-MIB", "netBotzTrapResolveTime"),
        ("NetBotz50-MIB", "netBotzTrapSeverity"),
        ("NetBotz50-MIB", "netBotzTrapSensorValue"),
        ("NetBotz50-MIB", "netBotzTrapSensorValueInt"),
        ("NetBotz50-MIB", "netBotzTrapSensorValueFraction"))
)
if mibBuilder.loadTexts:
    netBotzSpotLeakSensorUnplugged.setStatus(
        "current"
    )

netBotzSpotLeakSensorValueError = NotificationType(
    (1, 3, 6, 1, 4, 1, 52674, 500, 10, 1, 12, 0, 10)
)
netBotzSpotLeakSensorValueError.setObjects(
      *(("NetBotz50-MIB", "netBotzTrapErrorID"),
        ("NetBotz50-MIB", "netBotzTrapErrorType"),
        ("NetBotz50-MIB", "netBotzTrapErrorTypeLabel"),
        ("NetBotz50-MIB", "netBotzTrapSensorID"),
        ("NetBotz50-MIB", "netBotzTrapSensorLabel"),
        ("NetBotz50-MIB", "netBotzTrapContainerID"),
        ("NetBotz50-MIB", "netBotzTrapContainerLabel"),
        ("NetBotz50-MIB", "netBotzTrapPortID"),
        ("NetBotz50-MIB", "netBotzTrapPortLabel"),
        ("NetBotz50-MIB", "netBotzTrapStartTime"),
        ("NetBotz50-MIB", "netBotzTrapNotifyTime"),
        ("NetBotz50-MIB", "netBotzTrapResolveTime"),
        ("NetBotz50-MIB", "netBotzTrapSeverity"),
        ("NetBotz50-MIB", "netBotzTrapSensorValue"),
        ("NetBotz50-MIB", "netBotzTrapSensorValueInt"),
        ("NetBotz50-MIB", "netBotzTrapSensorValueFraction"))
)
if mibBuilder.loadTexts:
    netBotzSpotLeakSensorValueError.setStatus(
        "current"
    )

netBotzSpotLeakSensorErrorRTN = NotificationType(
    (1, 3, 6, 1, 4, 1, 52674, 500, 10, 1, 12, 0, 101)
)
netBotzSpotLeakSensorErrorRTN.setObjects(
      *(("NetBotz50-MIB", "netBotzTrapErrorID"),
        ("NetBotz50-MIB", "netBotzTrapErrorType"),
        ("NetBotz50-MIB", "netBotzTrapErrorTypeLabel"),
        ("NetBotz50-MIB", "netBotzTrapSensorID"),
        ("NetBotz50-MIB", "netBotzTrapSensorLabel"),
        ("NetBotz50-MIB", "netBotzTrapContainerID"),
        ("NetBotz50-MIB", "netBotzTrapContainerLabel"),
        ("NetBotz50-MIB", "netBotzTrapPortID"),
        ("NetBotz50-MIB", "netBotzTrapPortLabel"),
        ("NetBotz50-MIB", "netBotzTrapStartTime"),
        ("NetBotz50-MIB", "netBotzTrapNotifyTime"),
        ("NetBotz50-MIB", "netBotzTrapResolveTime"),
        ("NetBotz50-MIB", "netBotzTrapSeverity"),
        ("NetBotz50-MIB", "netBotzTrapSensorValue"),
        ("NetBotz50-MIB", "netBotzTrapSensorValueInt"),
        ("NetBotz50-MIB", "netBotzTrapSensorValueFraction"))
)
if mibBuilder.loadTexts:
    netBotzSpotLeakSensorErrorRTN.setStatus(
        "current"
    )

netBotzSpotLeakSensorReplugged = NotificationType(
    (1, 3, 6, 1, 4, 1, 52674, 500, 10, 1, 12, 0, 106)
)
netBotzSpotLeakSensorReplugged.setObjects(
      *(("NetBotz50-MIB", "netBotzTrapErrorID"),
        ("NetBotz50-MIB", "netBotzTrapErrorType"),
        ("NetBotz50-MIB", "netBotzTrapErrorTypeLabel"),
        ("NetBotz50-MIB", "netBotzTrapSensorID"),
        ("NetBotz50-MIB", "netBotzTrapSensorLabel"),
        ("NetBotz50-MIB", "netBotzTrapContainerID"),
        ("NetBotz50-MIB", "netBotzTrapContainerLabel"),
        ("NetBotz50-MIB", "netBotzTrapPortID"),
        ("NetBotz50-MIB", "netBotzTrapPortLabel"),
        ("NetBotz50-MIB", "netBotzTrapStartTime"),
        ("NetBotz50-MIB", "netBotzTrapNotifyTime"),
        ("NetBotz50-MIB", "netBotzTrapResolveTime"),
        ("NetBotz50-MIB", "netBotzTrapSeverity"),
        ("NetBotz50-MIB", "netBotzTrapSensorValue"),
        ("NetBotz50-MIB", "netBotzTrapSensorValueInt"),
        ("NetBotz50-MIB", "netBotzTrapSensorValueFraction"))
)
if mibBuilder.loadTexts:
    netBotzSpotLeakSensorReplugged.setStatus(
        "current"
    )

netBotzSpotLeakSensorValueErrorRTN = NotificationType(
    (1, 3, 6, 1, 4, 1, 52674, 500, 10, 1, 12, 0, 110)
)
netBotzSpotLeakSensorValueErrorRTN.setObjects(
      *(("NetBotz50-MIB", "netBotzTrapErrorID"),
        ("NetBotz50-MIB", "netBotzTrapErrorType"),
        ("NetBotz50-MIB", "netBotzTrapErrorTypeLabel"),
        ("NetBotz50-MIB", "netBotzTrapSensorID"),
        ("NetBotz50-MIB", "netBotzTrapSensorLabel"),
        ("NetBotz50-MIB", "netBotzTrapContainerID"),
        ("NetBotz50-MIB", "netBotzTrapContainerLabel"),
        ("NetBotz50-MIB", "netBotzTrapPortID"),
        ("NetBotz50-MIB", "netBotzTrapPortLabel"),
        ("NetBotz50-MIB", "netBotzTrapStartTime"),
        ("NetBotz50-MIB", "netBotzTrapNotifyTime"),
        ("NetBotz50-MIB", "netBotzTrapResolveTime"),
        ("NetBotz50-MIB", "netBotzTrapSeverity"),
        ("NetBotz50-MIB", "netBotzTrapSensorValue"),
        ("NetBotz50-MIB", "netBotzTrapSensorValueInt"),
        ("NetBotz50-MIB", "netBotzTrapSensorValueFraction"))
)
if mibBuilder.loadTexts:
    netBotzSpotLeakSensorValueErrorRTN.setStatus(
        "current"
    )

netBotzRopeLeakSensorError = NotificationType(
    (1, 3, 6, 1, 4, 1, 52674, 500, 10, 1, 13, 0, 1)
)
netBotzRopeLeakSensorError.setObjects(
      *(("NetBotz50-MIB", "netBotzTrapErrorID"),
        ("NetBotz50-MIB", "netBotzTrapErrorType"),
        ("NetBotz50-MIB", "netBotzTrapErrorTypeLabel"),
        ("NetBotz50-MIB", "netBotzTrapSensorID"),
        ("NetBotz50-MIB", "netBotzTrapSensorLabel"),
        ("NetBotz50-MIB", "netBotzTrapContainerID"),
        ("NetBotz50-MIB", "netBotzTrapContainerLabel"),
        ("NetBotz50-MIB", "netBotzTrapPortID"),
        ("NetBotz50-MIB", "netBotzTrapPortLabel"),
        ("NetBotz50-MIB", "netBotzTrapStartTime"),
        ("NetBotz50-MIB", "netBotzTrapNotifyTime"),
        ("NetBotz50-MIB", "netBotzTrapResolveTime"),
        ("NetBotz50-MIB", "netBotzTrapSeverity"),
        ("NetBotz50-MIB", "netBotzTrapSensorValue"),
        ("NetBotz50-MIB", "netBotzTrapSensorValueInt"),
        ("NetBotz50-MIB", "netBotzTrapSensorValueFraction"))
)
if mibBuilder.loadTexts:
    netBotzRopeLeakSensorError.setStatus(
        "current"
    )

netBotzRopeLeakSensorUnplugged = NotificationType(
    (1, 3, 6, 1, 4, 1, 52674, 500, 10, 1, 13, 0, 6)
)
netBotzRopeLeakSensorUnplugged.setObjects(
      *(("NetBotz50-MIB", "netBotzTrapErrorID"),
        ("NetBotz50-MIB", "netBotzTrapErrorType"),
        ("NetBotz50-MIB", "netBotzTrapErrorTypeLabel"),
        ("NetBotz50-MIB", "netBotzTrapSensorID"),
        ("NetBotz50-MIB", "netBotzTrapSensorLabel"),
        ("NetBotz50-MIB", "netBotzTrapContainerID"),
        ("NetBotz50-MIB", "netBotzTrapContainerLabel"),
        ("NetBotz50-MIB", "netBotzTrapPortID"),
        ("NetBotz50-MIB", "netBotzTrapPortLabel"),
        ("NetBotz50-MIB", "netBotzTrapStartTime"),
        ("NetBotz50-MIB", "netBotzTrapNotifyTime"),
        ("NetBotz50-MIB", "netBotzTrapResolveTime"),
        ("NetBotz50-MIB", "netBotzTrapSeverity"),
        ("NetBotz50-MIB", "netBotzTrapSensorValue"),
        ("NetBotz50-MIB", "netBotzTrapSensorValueInt"),
        ("NetBotz50-MIB", "netBotzTrapSensorValueFraction"))
)
if mibBuilder.loadTexts:
    netBotzRopeLeakSensorUnplugged.setStatus(
        "current"
    )

netBotzRopeLeakSensorValueError = NotificationType(
    (1, 3, 6, 1, 4, 1, 52674, 500, 10, 1, 13, 0, 10)
)
netBotzRopeLeakSensorValueError.setObjects(
      *(("NetBotz50-MIB", "netBotzTrapErrorID"),
        ("NetBotz50-MIB", "netBotzTrapErrorType"),
        ("NetBotz50-MIB", "netBotzTrapErrorTypeLabel"),
        ("NetBotz50-MIB", "netBotzTrapSensorID"),
        ("NetBotz50-MIB", "netBotzTrapSensorLabel"),
        ("NetBotz50-MIB", "netBotzTrapContainerID"),
        ("NetBotz50-MIB", "netBotzTrapContainerLabel"),
        ("NetBotz50-MIB", "netBotzTrapPortID"),
        ("NetBotz50-MIB", "netBotzTrapPortLabel"),
        ("NetBotz50-MIB", "netBotzTrapStartTime"),
        ("NetBotz50-MIB", "netBotzTrapNotifyTime"),
        ("NetBotz50-MIB", "netBotzTrapResolveTime"),
        ("NetBotz50-MIB", "netBotzTrapSeverity"),
        ("NetBotz50-MIB", "netBotzTrapSensorValue"),
        ("NetBotz50-MIB", "netBotzTrapSensorValueInt"),
        ("NetBotz50-MIB", "netBotzTrapSensorValueFraction"))
)
if mibBuilder.loadTexts:
    netBotzRopeLeakSensorValueError.setStatus(
        "current"
    )

netBotzRopeLeakSensorErrorRTN = NotificationType(
    (1, 3, 6, 1, 4, 1, 52674, 500, 10, 1, 13, 0, 101)
)
netBotzRopeLeakSensorErrorRTN.setObjects(
      *(("NetBotz50-MIB", "netBotzTrapErrorID"),
        ("NetBotz50-MIB", "netBotzTrapErrorType"),
        ("NetBotz50-MIB", "netBotzTrapErrorTypeLabel"),
        ("NetBotz50-MIB", "netBotzTrapSensorID"),
        ("NetBotz50-MIB", "netBotzTrapSensorLabel"),
        ("NetBotz50-MIB", "netBotzTrapContainerID"),
        ("NetBotz50-MIB", "netBotzTrapContainerLabel"),
        ("NetBotz50-MIB", "netBotzTrapPortID"),
        ("NetBotz50-MIB", "netBotzTrapPortLabel"),
        ("NetBotz50-MIB", "netBotzTrapStartTime"),
        ("NetBotz50-MIB", "netBotzTrapNotifyTime"),
        ("NetBotz50-MIB", "netBotzTrapResolveTime"),
        ("NetBotz50-MIB", "netBotzTrapSeverity"),
        ("NetBotz50-MIB", "netBotzTrapSensorValue"),
        ("NetBotz50-MIB", "netBotzTrapSensorValueInt"),
        ("NetBotz50-MIB", "netBotzTrapSensorValueFraction"))
)
if mibBuilder.loadTexts:
    netBotzRopeLeakSensorErrorRTN.setStatus(
        "current"
    )

netBotzRopeLeakSensorReplugged = NotificationType(
    (1, 3, 6, 1, 4, 1, 52674, 500, 10, 1, 13, 0, 106)
)
netBotzRopeLeakSensorReplugged.setObjects(
      *(("NetBotz50-MIB", "netBotzTrapErrorID"),
        ("NetBotz50-MIB", "netBotzTrapErrorType"),
        ("NetBotz50-MIB", "netBotzTrapErrorTypeLabel"),
        ("NetBotz50-MIB", "netBotzTrapSensorID"),
        ("NetBotz50-MIB", "netBotzTrapSensorLabel"),
        ("NetBotz50-MIB", "netBotzTrapContainerID"),
        ("NetBotz50-MIB", "netBotzTrapContainerLabel"),
        ("NetBotz50-MIB", "netBotzTrapPortID"),
        ("NetBotz50-MIB", "netBotzTrapPortLabel"),
        ("NetBotz50-MIB", "netBotzTrapStartTime"),
        ("NetBotz50-MIB", "netBotzTrapNotifyTime"),
        ("NetBotz50-MIB", "netBotzTrapResolveTime"),
        ("NetBotz50-MIB", "netBotzTrapSeverity"),
        ("NetBotz50-MIB", "netBotzTrapSensorValue"),
        ("NetBotz50-MIB", "netBotzTrapSensorValueInt"),
        ("NetBotz50-MIB", "netBotzTrapSensorValueFraction"))
)
if mibBuilder.loadTexts:
    netBotzRopeLeakSensorReplugged.setStatus(
        "current"
    )

netBotzRopeLeakSensorValueErrorRTN = NotificationType(
    (1, 3, 6, 1, 4, 1, 52674, 500, 10, 1, 13, 0, 110)
)
netBotzRopeLeakSensorValueErrorRTN.setObjects(
      *(("NetBotz50-MIB", "netBotzTrapErrorID"),
        ("NetBotz50-MIB", "netBotzTrapErrorType"),
        ("NetBotz50-MIB", "netBotzTrapErrorTypeLabel"),
        ("NetBotz50-MIB", "netBotzTrapSensorID"),
        ("NetBotz50-MIB", "netBotzTrapSensorLabel"),
        ("NetBotz50-MIB", "netBotzTrapContainerID"),
        ("NetBotz50-MIB", "netBotzTrapContainerLabel"),
        ("NetBotz50-MIB", "netBotzTrapPortID"),
        ("NetBotz50-MIB", "netBotzTrapPortLabel"),
        ("NetBotz50-MIB", "netBotzTrapStartTime"),
        ("NetBotz50-MIB", "netBotzTrapNotifyTime"),
        ("NetBotz50-MIB", "netBotzTrapResolveTime"),
        ("NetBotz50-MIB", "netBotzTrapSeverity"),
        ("NetBotz50-MIB", "netBotzTrapSensorValue"),
        ("NetBotz50-MIB", "netBotzTrapSensorValueInt"),
        ("NetBotz50-MIB", "netBotzTrapSensorValueFraction"))
)
if mibBuilder.loadTexts:
    netBotzRopeLeakSensorValueErrorRTN.setStatus(
        "current"
    )

netBotzRSSITooLow = NotificationType(
    (1, 3, 6, 1, 4, 1, 52674, 500, 10, 1, 14, 0, 3)
)
netBotzRSSITooLow.setObjects(
      *(("NetBotz50-MIB", "netBotzTrapErrorID"),
        ("NetBotz50-MIB", "netBotzTrapErrorType"),
        ("NetBotz50-MIB", "netBotzTrapErrorTypeLabel"),
        ("NetBotz50-MIB", "netBotzTrapSensorID"),
        ("NetBotz50-MIB", "netBotzTrapSensorLabel"),
        ("NetBotz50-MIB", "netBotzTrapContainerID"),
        ("NetBotz50-MIB", "netBotzTrapContainerLabel"),
        ("NetBotz50-MIB", "netBotzTrapPortID"),
        ("NetBotz50-MIB", "netBotzTrapPortLabel"),
        ("NetBotz50-MIB", "netBotzTrapStartTime"),
        ("NetBotz50-MIB", "netBotzTrapNotifyTime"),
        ("NetBotz50-MIB", "netBotzTrapResolveTime"),
        ("NetBotz50-MIB", "netBotzTrapSeverity"),
        ("NetBotz50-MIB", "netBotzTrapSensorValue"),
        ("NetBotz50-MIB", "netBotzTrapSensorValueInt"),
        ("NetBotz50-MIB", "netBotzTrapSensorValueFraction"))
)
if mibBuilder.loadTexts:
    netBotzRSSITooLow.setStatus(
        "current"
    )

netBotzRSSISensorValueError = NotificationType(
    (1, 3, 6, 1, 4, 1, 52674, 500, 10, 1, 14, 0, 10)
)
netBotzRSSISensorValueError.setObjects(
      *(("NetBotz50-MIB", "netBotzTrapErrorID"),
        ("NetBotz50-MIB", "netBotzTrapErrorType"),
        ("NetBotz50-MIB", "netBotzTrapErrorTypeLabel"),
        ("NetBotz50-MIB", "netBotzTrapSensorID"),
        ("NetBotz50-MIB", "netBotzTrapSensorLabel"),
        ("NetBotz50-MIB", "netBotzTrapContainerID"),
        ("NetBotz50-MIB", "netBotzTrapContainerLabel"),
        ("NetBotz50-MIB", "netBotzTrapPortID"),
        ("NetBotz50-MIB", "netBotzTrapPortLabel"),
        ("NetBotz50-MIB", "netBotzTrapStartTime"),
        ("NetBotz50-MIB", "netBotzTrapNotifyTime"),
        ("NetBotz50-MIB", "netBotzTrapResolveTime"),
        ("NetBotz50-MIB", "netBotzTrapSeverity"),
        ("NetBotz50-MIB", "netBotzTrapSensorValue"),
        ("NetBotz50-MIB", "netBotzTrapSensorValueInt"),
        ("NetBotz50-MIB", "netBotzTrapSensorValueFraction"))
)
if mibBuilder.loadTexts:
    netBotzRSSISensorValueError.setStatus(
        "current"
    )

netBotzRSSITooLowRTN = NotificationType(
    (1, 3, 6, 1, 4, 1, 52674, 500, 10, 1, 14, 0, 103)
)
netBotzRSSITooLowRTN.setObjects(
      *(("NetBotz50-MIB", "netBotzTrapErrorID"),
        ("NetBotz50-MIB", "netBotzTrapErrorType"),
        ("NetBotz50-MIB", "netBotzTrapErrorTypeLabel"),
        ("NetBotz50-MIB", "netBotzTrapSensorID"),
        ("NetBotz50-MIB", "netBotzTrapSensorLabel"),
        ("NetBotz50-MIB", "netBotzTrapContainerID"),
        ("NetBotz50-MIB", "netBotzTrapContainerLabel"),
        ("NetBotz50-MIB", "netBotzTrapPortID"),
        ("NetBotz50-MIB", "netBotzTrapPortLabel"),
        ("NetBotz50-MIB", "netBotzTrapStartTime"),
        ("NetBotz50-MIB", "netBotzTrapNotifyTime"),
        ("NetBotz50-MIB", "netBotzTrapResolveTime"),
        ("NetBotz50-MIB", "netBotzTrapSeverity"),
        ("NetBotz50-MIB", "netBotzTrapSensorValue"),
        ("NetBotz50-MIB", "netBotzTrapSensorValueInt"),
        ("NetBotz50-MIB", "netBotzTrapSensorValueFraction"))
)
if mibBuilder.loadTexts:
    netBotzRSSITooLowRTN.setStatus(
        "current"
    )

netBotzRSSISensorValueErrorRTN = NotificationType(
    (1, 3, 6, 1, 4, 1, 52674, 500, 10, 1, 14, 0, 110)
)
netBotzRSSISensorValueErrorRTN.setObjects(
      *(("NetBotz50-MIB", "netBotzTrapErrorID"),
        ("NetBotz50-MIB", "netBotzTrapErrorType"),
        ("NetBotz50-MIB", "netBotzTrapErrorTypeLabel"),
        ("NetBotz50-MIB", "netBotzTrapSensorID"),
        ("NetBotz50-MIB", "netBotzTrapSensorLabel"),
        ("NetBotz50-MIB", "netBotzTrapContainerID"),
        ("NetBotz50-MIB", "netBotzTrapContainerLabel"),
        ("NetBotz50-MIB", "netBotzTrapPortID"),
        ("NetBotz50-MIB", "netBotzTrapPortLabel"),
        ("NetBotz50-MIB", "netBotzTrapStartTime"),
        ("NetBotz50-MIB", "netBotzTrapNotifyTime"),
        ("NetBotz50-MIB", "netBotzTrapResolveTime"),
        ("NetBotz50-MIB", "netBotzTrapSeverity"),
        ("NetBotz50-MIB", "netBotzTrapSensorValue"),
        ("NetBotz50-MIB", "netBotzTrapSensorValueInt"),
        ("NetBotz50-MIB", "netBotzTrapSensorValueFraction"))
)
if mibBuilder.loadTexts:
    netBotzRSSISensorValueErrorRTN.setStatus(
        "current"
    )

netBotzBatterySensorError = NotificationType(
    (1, 3, 6, 1, 4, 1, 52674, 500, 10, 1, 15, 0, 1)
)
netBotzBatterySensorError.setObjects(
      *(("NetBotz50-MIB", "netBotzTrapErrorID"),
        ("NetBotz50-MIB", "netBotzTrapErrorType"),
        ("NetBotz50-MIB", "netBotzTrapErrorTypeLabel"),
        ("NetBotz50-MIB", "netBotzTrapSensorID"),
        ("NetBotz50-MIB", "netBotzTrapSensorLabel"),
        ("NetBotz50-MIB", "netBotzTrapContainerID"),
        ("NetBotz50-MIB", "netBotzTrapContainerLabel"),
        ("NetBotz50-MIB", "netBotzTrapPortID"),
        ("NetBotz50-MIB", "netBotzTrapPortLabel"),
        ("NetBotz50-MIB", "netBotzTrapStartTime"),
        ("NetBotz50-MIB", "netBotzTrapNotifyTime"),
        ("NetBotz50-MIB", "netBotzTrapResolveTime"),
        ("NetBotz50-MIB", "netBotzTrapSeverity"),
        ("NetBotz50-MIB", "netBotzTrapSensorValue"),
        ("NetBotz50-MIB", "netBotzTrapSensorValueInt"),
        ("NetBotz50-MIB", "netBotzTrapSensorValueFraction"))
)
if mibBuilder.loadTexts:
    netBotzBatterySensorError.setStatus(
        "current"
    )

netBotzBatteryTooLow = NotificationType(
    (1, 3, 6, 1, 4, 1, 52674, 500, 10, 1, 15, 0, 3)
)
netBotzBatteryTooLow.setObjects(
      *(("NetBotz50-MIB", "netBotzTrapErrorID"),
        ("NetBotz50-MIB", "netBotzTrapErrorType"),
        ("NetBotz50-MIB", "netBotzTrapErrorTypeLabel"),
        ("NetBotz50-MIB", "netBotzTrapSensorID"),
        ("NetBotz50-MIB", "netBotzTrapSensorLabel"),
        ("NetBotz50-MIB", "netBotzTrapContainerID"),
        ("NetBotz50-MIB", "netBotzTrapContainerLabel"),
        ("NetBotz50-MIB", "netBotzTrapPortID"),
        ("NetBotz50-MIB", "netBotzTrapPortLabel"),
        ("NetBotz50-MIB", "netBotzTrapStartTime"),
        ("NetBotz50-MIB", "netBotzTrapNotifyTime"),
        ("NetBotz50-MIB", "netBotzTrapResolveTime"),
        ("NetBotz50-MIB", "netBotzTrapSeverity"),
        ("NetBotz50-MIB", "netBotzTrapSensorValue"),
        ("NetBotz50-MIB", "netBotzTrapSensorValueInt"),
        ("NetBotz50-MIB", "netBotzTrapSensorValueFraction"))
)
if mibBuilder.loadTexts:
    netBotzBatteryTooLow.setStatus(
        "current"
    )

netBotzBatterySensorValueError = NotificationType(
    (1, 3, 6, 1, 4, 1, 52674, 500, 10, 1, 15, 0, 10)
)
netBotzBatterySensorValueError.setObjects(
      *(("NetBotz50-MIB", "netBotzTrapErrorID"),
        ("NetBotz50-MIB", "netBotzTrapErrorType"),
        ("NetBotz50-MIB", "netBotzTrapErrorTypeLabel"),
        ("NetBotz50-MIB", "netBotzTrapSensorID"),
        ("NetBotz50-MIB", "netBotzTrapSensorLabel"),
        ("NetBotz50-MIB", "netBotzTrapContainerID"),
        ("NetBotz50-MIB", "netBotzTrapContainerLabel"),
        ("NetBotz50-MIB", "netBotzTrapPortID"),
        ("NetBotz50-MIB", "netBotzTrapPortLabel"),
        ("NetBotz50-MIB", "netBotzTrapStartTime"),
        ("NetBotz50-MIB", "netBotzTrapNotifyTime"),
        ("NetBotz50-MIB", "netBotzTrapResolveTime"),
        ("NetBotz50-MIB", "netBotzTrapSeverity"),
        ("NetBotz50-MIB", "netBotzTrapSensorValue"),
        ("NetBotz50-MIB", "netBotzTrapSensorValueInt"),
        ("NetBotz50-MIB", "netBotzTrapSensorValueFraction"))
)
if mibBuilder.loadTexts:
    netBotzBatterySensorValueError.setStatus(
        "current"
    )

netBotzBatterySensorErrorRTN = NotificationType(
    (1, 3, 6, 1, 4, 1, 52674, 500, 10, 1, 15, 0, 101)
)
netBotzBatterySensorErrorRTN.setObjects(
      *(("NetBotz50-MIB", "netBotzTrapErrorID"),
        ("NetBotz50-MIB", "netBotzTrapErrorType"),
        ("NetBotz50-MIB", "netBotzTrapErrorTypeLabel"),
        ("NetBotz50-MIB", "netBotzTrapSensorID"),
        ("NetBotz50-MIB", "netBotzTrapSensorLabel"),
        ("NetBotz50-MIB", "netBotzTrapContainerID"),
        ("NetBotz50-MIB", "netBotzTrapContainerLabel"),
        ("NetBotz50-MIB", "netBotzTrapPortID"),
        ("NetBotz50-MIB", "netBotzTrapPortLabel"),
        ("NetBotz50-MIB", "netBotzTrapStartTime"),
        ("NetBotz50-MIB", "netBotzTrapNotifyTime"),
        ("NetBotz50-MIB", "netBotzTrapResolveTime"),
        ("NetBotz50-MIB", "netBotzTrapSeverity"),
        ("NetBotz50-MIB", "netBotzTrapSensorValue"),
        ("NetBotz50-MIB", "netBotzTrapSensorValueInt"),
        ("NetBotz50-MIB", "netBotzTrapSensorValueFraction"))
)
if mibBuilder.loadTexts:
    netBotzBatterySensorErrorRTN.setStatus(
        "current"
    )

netBotzBatteryTooLowRTN = NotificationType(
    (1, 3, 6, 1, 4, 1, 52674, 500, 10, 1, 15, 0, 103)
)
netBotzBatteryTooLowRTN.setObjects(
      *(("NetBotz50-MIB", "netBotzTrapErrorID"),
        ("NetBotz50-MIB", "netBotzTrapErrorType"),
        ("NetBotz50-MIB", "netBotzTrapErrorTypeLabel"),
        ("NetBotz50-MIB", "netBotzTrapSensorID"),
        ("NetBotz50-MIB", "netBotzTrapSensorLabel"),
        ("NetBotz50-MIB", "netBotzTrapContainerID"),
        ("NetBotz50-MIB", "netBotzTrapContainerLabel"),
        ("NetBotz50-MIB", "netBotzTrapPortID"),
        ("NetBotz50-MIB", "netBotzTrapPortLabel"),
        ("NetBotz50-MIB", "netBotzTrapStartTime"),
        ("NetBotz50-MIB", "netBotzTrapNotifyTime"),
        ("NetBotz50-MIB", "netBotzTrapResolveTime"),
        ("NetBotz50-MIB", "netBotzTrapSeverity"),
        ("NetBotz50-MIB", "netBotzTrapSensorValue"),
        ("NetBotz50-MIB", "netBotzTrapSensorValueInt"),
        ("NetBotz50-MIB", "netBotzTrapSensorValueFraction"))
)
if mibBuilder.loadTexts:
    netBotzBatteryTooLowRTN.setStatus(
        "current"
    )

netBotzBatterySensorValueErrorRTN = NotificationType(
    (1, 3, 6, 1, 4, 1, 52674, 500, 10, 1, 15, 0, 110)
)
netBotzBatterySensorValueErrorRTN.setObjects(
      *(("NetBotz50-MIB", "netBotzTrapErrorID"),
        ("NetBotz50-MIB", "netBotzTrapErrorType"),
        ("NetBotz50-MIB", "netBotzTrapErrorTypeLabel"),
        ("NetBotz50-MIB", "netBotzTrapSensorID"),
        ("NetBotz50-MIB", "netBotzTrapSensorLabel"),
        ("NetBotz50-MIB", "netBotzTrapContainerID"),
        ("NetBotz50-MIB", "netBotzTrapContainerLabel"),
        ("NetBotz50-MIB", "netBotzTrapPortID"),
        ("NetBotz50-MIB", "netBotzTrapPortLabel"),
        ("NetBotz50-MIB", "netBotzTrapStartTime"),
        ("NetBotz50-MIB", "netBotzTrapNotifyTime"),
        ("NetBotz50-MIB", "netBotzTrapResolveTime"),
        ("NetBotz50-MIB", "netBotzTrapSeverity"),
        ("NetBotz50-MIB", "netBotzTrapSensorValue"),
        ("NetBotz50-MIB", "netBotzTrapSensorValueInt"),
        ("NetBotz50-MIB", "netBotzTrapSensorValueFraction"))
)
if mibBuilder.loadTexts:
    netBotzBatterySensorValueErrorRTN.setStatus(
        "current"
    )

netBotzOutletSensorError = NotificationType(
    (1, 3, 6, 1, 4, 1, 52674, 500, 10, 1, 16, 0, 1)
)
netBotzOutletSensorError.setObjects(
      *(("NetBotz50-MIB", "netBotzTrapErrorID"),
        ("NetBotz50-MIB", "netBotzTrapErrorType"),
        ("NetBotz50-MIB", "netBotzTrapErrorTypeLabel"),
        ("NetBotz50-MIB", "netBotzTrapSensorID"),
        ("NetBotz50-MIB", "netBotzTrapSensorLabel"),
        ("NetBotz50-MIB", "netBotzTrapContainerID"),
        ("NetBotz50-MIB", "netBotzTrapContainerLabel"),
        ("NetBotz50-MIB", "netBotzTrapPortID"),
        ("NetBotz50-MIB", "netBotzTrapPortLabel"),
        ("NetBotz50-MIB", "netBotzTrapStartTime"),
        ("NetBotz50-MIB", "netBotzTrapNotifyTime"),
        ("NetBotz50-MIB", "netBotzTrapResolveTime"),
        ("NetBotz50-MIB", "netBotzTrapSeverity"),
        ("NetBotz50-MIB", "netBotzTrapSensorValue"),
        ("NetBotz50-MIB", "netBotzTrapSensorValueInt"),
        ("NetBotz50-MIB", "netBotzTrapSensorValueFraction"))
)
if mibBuilder.loadTexts:
    netBotzOutletSensorError.setStatus(
        "current"
    )

netBotzOutletSensorValueError = NotificationType(
    (1, 3, 6, 1, 4, 1, 52674, 500, 10, 1, 16, 0, 10)
)
netBotzOutletSensorValueError.setObjects(
      *(("NetBotz50-MIB", "netBotzTrapErrorID"),
        ("NetBotz50-MIB", "netBotzTrapErrorType"),
        ("NetBotz50-MIB", "netBotzTrapErrorTypeLabel"),
        ("NetBotz50-MIB", "netBotzTrapSensorID"),
        ("NetBotz50-MIB", "netBotzTrapSensorLabel"),
        ("NetBotz50-MIB", "netBotzTrapContainerID"),
        ("NetBotz50-MIB", "netBotzTrapContainerLabel"),
        ("NetBotz50-MIB", "netBotzTrapPortID"),
        ("NetBotz50-MIB", "netBotzTrapPortLabel"),
        ("NetBotz50-MIB", "netBotzTrapStartTime"),
        ("NetBotz50-MIB", "netBotzTrapNotifyTime"),
        ("NetBotz50-MIB", "netBotzTrapResolveTime"),
        ("NetBotz50-MIB", "netBotzTrapSeverity"),
        ("NetBotz50-MIB", "netBotzTrapSensorValue"),
        ("NetBotz50-MIB", "netBotzTrapSensorValueInt"),
        ("NetBotz50-MIB", "netBotzTrapSensorValueFraction"))
)
if mibBuilder.loadTexts:
    netBotzOutletSensorValueError.setStatus(
        "current"
    )

netBotzOutletSensorErrorRTN = NotificationType(
    (1, 3, 6, 1, 4, 1, 52674, 500, 10, 1, 16, 0, 101)
)
netBotzOutletSensorErrorRTN.setObjects(
      *(("NetBotz50-MIB", "netBotzTrapErrorID"),
        ("NetBotz50-MIB", "netBotzTrapErrorType"),
        ("NetBotz50-MIB", "netBotzTrapErrorTypeLabel"),
        ("NetBotz50-MIB", "netBotzTrapSensorID"),
        ("NetBotz50-MIB", "netBotzTrapSensorLabel"),
        ("NetBotz50-MIB", "netBotzTrapContainerID"),
        ("NetBotz50-MIB", "netBotzTrapContainerLabel"),
        ("NetBotz50-MIB", "netBotzTrapPortID"),
        ("NetBotz50-MIB", "netBotzTrapPortLabel"),
        ("NetBotz50-MIB", "netBotzTrapStartTime"),
        ("NetBotz50-MIB", "netBotzTrapNotifyTime"),
        ("NetBotz50-MIB", "netBotzTrapResolveTime"),
        ("NetBotz50-MIB", "netBotzTrapSeverity"),
        ("NetBotz50-MIB", "netBotzTrapSensorValue"),
        ("NetBotz50-MIB", "netBotzTrapSensorValueInt"),
        ("NetBotz50-MIB", "netBotzTrapSensorValueFraction"))
)
if mibBuilder.loadTexts:
    netBotzOutletSensorErrorRTN.setStatus(
        "current"
    )

netBotzOutletSensorValueErrorRTN = NotificationType(
    (1, 3, 6, 1, 4, 1, 52674, 500, 10, 1, 16, 0, 110)
)
netBotzOutletSensorValueErrorRTN.setObjects(
      *(("NetBotz50-MIB", "netBotzTrapErrorID"),
        ("NetBotz50-MIB", "netBotzTrapErrorType"),
        ("NetBotz50-MIB", "netBotzTrapErrorTypeLabel"),
        ("NetBotz50-MIB", "netBotzTrapSensorID"),
        ("NetBotz50-MIB", "netBotzTrapSensorLabel"),
        ("NetBotz50-MIB", "netBotzTrapContainerID"),
        ("NetBotz50-MIB", "netBotzTrapContainerLabel"),
        ("NetBotz50-MIB", "netBotzTrapPortID"),
        ("NetBotz50-MIB", "netBotzTrapPortLabel"),
        ("NetBotz50-MIB", "netBotzTrapStartTime"),
        ("NetBotz50-MIB", "netBotzTrapNotifyTime"),
        ("NetBotz50-MIB", "netBotzTrapResolveTime"),
        ("NetBotz50-MIB", "netBotzTrapSeverity"),
        ("NetBotz50-MIB", "netBotzTrapSensorValue"),
        ("NetBotz50-MIB", "netBotzTrapSensorValueInt"),
        ("NetBotz50-MIB", "netBotzTrapSensorValueFraction"))
)
if mibBuilder.loadTexts:
    netBotzOutletSensorValueErrorRTN.setStatus(
        "current"
    )

netBotzBeaconError = NotificationType(
    (1, 3, 6, 1, 4, 1, 52674, 500, 10, 1, 17, 0, 1)
)
netBotzBeaconError.setObjects(
      *(("NetBotz50-MIB", "netBotzTrapErrorID"),
        ("NetBotz50-MIB", "netBotzTrapErrorType"),
        ("NetBotz50-MIB", "netBotzTrapErrorTypeLabel"),
        ("NetBotz50-MIB", "netBotzTrapSensorID"),
        ("NetBotz50-MIB", "netBotzTrapSensorLabel"),
        ("NetBotz50-MIB", "netBotzTrapContainerID"),
        ("NetBotz50-MIB", "netBotzTrapContainerLabel"),
        ("NetBotz50-MIB", "netBotzTrapPortID"),
        ("NetBotz50-MIB", "netBotzTrapPortLabel"),
        ("NetBotz50-MIB", "netBotzTrapStartTime"),
        ("NetBotz50-MIB", "netBotzTrapNotifyTime"),
        ("NetBotz50-MIB", "netBotzTrapResolveTime"),
        ("NetBotz50-MIB", "netBotzTrapSeverity"),
        ("NetBotz50-MIB", "netBotzTrapSensorValue"),
        ("NetBotz50-MIB", "netBotzTrapSensorValueInt"),
        ("NetBotz50-MIB", "netBotzTrapSensorValueFraction"))
)
if mibBuilder.loadTexts:
    netBotzBeaconError.setStatus(
        "current"
    )

netBotzBeaconUnplugged = NotificationType(
    (1, 3, 6, 1, 4, 1, 52674, 500, 10, 1, 17, 0, 6)
)
netBotzBeaconUnplugged.setObjects(
      *(("NetBotz50-MIB", "netBotzTrapErrorID"),
        ("NetBotz50-MIB", "netBotzTrapErrorType"),
        ("NetBotz50-MIB", "netBotzTrapErrorTypeLabel"),
        ("NetBotz50-MIB", "netBotzTrapSensorID"),
        ("NetBotz50-MIB", "netBotzTrapSensorLabel"),
        ("NetBotz50-MIB", "netBotzTrapContainerID"),
        ("NetBotz50-MIB", "netBotzTrapContainerLabel"),
        ("NetBotz50-MIB", "netBotzTrapPortID"),
        ("NetBotz50-MIB", "netBotzTrapPortLabel"),
        ("NetBotz50-MIB", "netBotzTrapStartTime"),
        ("NetBotz50-MIB", "netBotzTrapNotifyTime"),
        ("NetBotz50-MIB", "netBotzTrapResolveTime"),
        ("NetBotz50-MIB", "netBotzTrapSeverity"),
        ("NetBotz50-MIB", "netBotzTrapSensorValue"),
        ("NetBotz50-MIB", "netBotzTrapSensorValueInt"),
        ("NetBotz50-MIB", "netBotzTrapSensorValueFraction"))
)
if mibBuilder.loadTexts:
    netBotzBeaconUnplugged.setStatus(
        "current"
    )

netBotzBeaconValueError = NotificationType(
    (1, 3, 6, 1, 4, 1, 52674, 500, 10, 1, 17, 0, 10)
)
netBotzBeaconValueError.setObjects(
      *(("NetBotz50-MIB", "netBotzTrapErrorID"),
        ("NetBotz50-MIB", "netBotzTrapErrorType"),
        ("NetBotz50-MIB", "netBotzTrapErrorTypeLabel"),
        ("NetBotz50-MIB", "netBotzTrapSensorID"),
        ("NetBotz50-MIB", "netBotzTrapSensorLabel"),
        ("NetBotz50-MIB", "netBotzTrapContainerID"),
        ("NetBotz50-MIB", "netBotzTrapContainerLabel"),
        ("NetBotz50-MIB", "netBotzTrapPortID"),
        ("NetBotz50-MIB", "netBotzTrapPortLabel"),
        ("NetBotz50-MIB", "netBotzTrapStartTime"),
        ("NetBotz50-MIB", "netBotzTrapNotifyTime"),
        ("NetBotz50-MIB", "netBotzTrapResolveTime"),
        ("NetBotz50-MIB", "netBotzTrapSeverity"),
        ("NetBotz50-MIB", "netBotzTrapSensorValue"),
        ("NetBotz50-MIB", "netBotzTrapSensorValueInt"),
        ("NetBotz50-MIB", "netBotzTrapSensorValueFraction"))
)
if mibBuilder.loadTexts:
    netBotzBeaconValueError.setStatus(
        "current"
    )

netBotzBeaconErrorRTN = NotificationType(
    (1, 3, 6, 1, 4, 1, 52674, 500, 10, 1, 17, 0, 101)
)
netBotzBeaconErrorRTN.setObjects(
      *(("NetBotz50-MIB", "netBotzTrapErrorID"),
        ("NetBotz50-MIB", "netBotzTrapErrorType"),
        ("NetBotz50-MIB", "netBotzTrapErrorTypeLabel"),
        ("NetBotz50-MIB", "netBotzTrapSensorID"),
        ("NetBotz50-MIB", "netBotzTrapSensorLabel"),
        ("NetBotz50-MIB", "netBotzTrapContainerID"),
        ("NetBotz50-MIB", "netBotzTrapContainerLabel"),
        ("NetBotz50-MIB", "netBotzTrapPortID"),
        ("NetBotz50-MIB", "netBotzTrapPortLabel"),
        ("NetBotz50-MIB", "netBotzTrapStartTime"),
        ("NetBotz50-MIB", "netBotzTrapNotifyTime"),
        ("NetBotz50-MIB", "netBotzTrapResolveTime"),
        ("NetBotz50-MIB", "netBotzTrapSeverity"),
        ("NetBotz50-MIB", "netBotzTrapSensorValue"),
        ("NetBotz50-MIB", "netBotzTrapSensorValueInt"),
        ("NetBotz50-MIB", "netBotzTrapSensorValueFraction"))
)
if mibBuilder.loadTexts:
    netBotzBeaconErrorRTN.setStatus(
        "current"
    )

netBotzBeaconReplugged = NotificationType(
    (1, 3, 6, 1, 4, 1, 52674, 500, 10, 1, 17, 0, 106)
)
netBotzBeaconReplugged.setObjects(
      *(("NetBotz50-MIB", "netBotzTrapErrorID"),
        ("NetBotz50-MIB", "netBotzTrapErrorType"),
        ("NetBotz50-MIB", "netBotzTrapErrorTypeLabel"),
        ("NetBotz50-MIB", "netBotzTrapSensorID"),
        ("NetBotz50-MIB", "netBotzTrapSensorLabel"),
        ("NetBotz50-MIB", "netBotzTrapContainerID"),
        ("NetBotz50-MIB", "netBotzTrapContainerLabel"),
        ("NetBotz50-MIB", "netBotzTrapPortID"),
        ("NetBotz50-MIB", "netBotzTrapPortLabel"),
        ("NetBotz50-MIB", "netBotzTrapStartTime"),
        ("NetBotz50-MIB", "netBotzTrapNotifyTime"),
        ("NetBotz50-MIB", "netBotzTrapResolveTime"),
        ("NetBotz50-MIB", "netBotzTrapSeverity"),
        ("NetBotz50-MIB", "netBotzTrapSensorValue"),
        ("NetBotz50-MIB", "netBotzTrapSensorValueInt"),
        ("NetBotz50-MIB", "netBotzTrapSensorValueFraction"))
)
if mibBuilder.loadTexts:
    netBotzBeaconReplugged.setStatus(
        "current"
    )

netBotzBeaconValueErrorRTN = NotificationType(
    (1, 3, 6, 1, 4, 1, 52674, 500, 10, 1, 17, 0, 110)
)
netBotzBeaconValueErrorRTN.setObjects(
      *(("NetBotz50-MIB", "netBotzTrapErrorID"),
        ("NetBotz50-MIB", "netBotzTrapErrorType"),
        ("NetBotz50-MIB", "netBotzTrapErrorTypeLabel"),
        ("NetBotz50-MIB", "netBotzTrapSensorID"),
        ("NetBotz50-MIB", "netBotzTrapSensorLabel"),
        ("NetBotz50-MIB", "netBotzTrapContainerID"),
        ("NetBotz50-MIB", "netBotzTrapContainerLabel"),
        ("NetBotz50-MIB", "netBotzTrapPortID"),
        ("NetBotz50-MIB", "netBotzTrapPortLabel"),
        ("NetBotz50-MIB", "netBotzTrapStartTime"),
        ("NetBotz50-MIB", "netBotzTrapNotifyTime"),
        ("NetBotz50-MIB", "netBotzTrapResolveTime"),
        ("NetBotz50-MIB", "netBotzTrapSeverity"),
        ("NetBotz50-MIB", "netBotzTrapSensorValue"),
        ("NetBotz50-MIB", "netBotzTrapSensorValueInt"),
        ("NetBotz50-MIB", "netBotzTrapSensorValueFraction"))
)
if mibBuilder.loadTexts:
    netBotzBeaconValueErrorRTN.setStatus(
        "current"
    )

netBotzSmokeSensorError = NotificationType(
    (1, 3, 6, 1, 4, 1, 52674, 500, 10, 1, 18, 0, 1)
)
netBotzSmokeSensorError.setObjects(
      *(("NetBotz50-MIB", "netBotzTrapErrorID"),
        ("NetBotz50-MIB", "netBotzTrapErrorType"),
        ("NetBotz50-MIB", "netBotzTrapErrorTypeLabel"),
        ("NetBotz50-MIB", "netBotzTrapSensorID"),
        ("NetBotz50-MIB", "netBotzTrapSensorLabel"),
        ("NetBotz50-MIB", "netBotzTrapContainerID"),
        ("NetBotz50-MIB", "netBotzTrapContainerLabel"),
        ("NetBotz50-MIB", "netBotzTrapPortID"),
        ("NetBotz50-MIB", "netBotzTrapPortLabel"),
        ("NetBotz50-MIB", "netBotzTrapStartTime"),
        ("NetBotz50-MIB", "netBotzTrapNotifyTime"),
        ("NetBotz50-MIB", "netBotzTrapResolveTime"),
        ("NetBotz50-MIB", "netBotzTrapSeverity"),
        ("NetBotz50-MIB", "netBotzTrapSensorValue"),
        ("NetBotz50-MIB", "netBotzTrapSensorValueInt"),
        ("NetBotz50-MIB", "netBotzTrapSensorValueFraction"))
)
if mibBuilder.loadTexts:
    netBotzSmokeSensorError.setStatus(
        "current"
    )

netBotzSmokeSensorUnplugged = NotificationType(
    (1, 3, 6, 1, 4, 1, 52674, 500, 10, 1, 18, 0, 6)
)
netBotzSmokeSensorUnplugged.setObjects(
      *(("NetBotz50-MIB", "netBotzTrapErrorID"),
        ("NetBotz50-MIB", "netBotzTrapErrorType"),
        ("NetBotz50-MIB", "netBotzTrapErrorTypeLabel"),
        ("NetBotz50-MIB", "netBotzTrapSensorID"),
        ("NetBotz50-MIB", "netBotzTrapSensorLabel"),
        ("NetBotz50-MIB", "netBotzTrapContainerID"),
        ("NetBotz50-MIB", "netBotzTrapContainerLabel"),
        ("NetBotz50-MIB", "netBotzTrapPortID"),
        ("NetBotz50-MIB", "netBotzTrapPortLabel"),
        ("NetBotz50-MIB", "netBotzTrapStartTime"),
        ("NetBotz50-MIB", "netBotzTrapNotifyTime"),
        ("NetBotz50-MIB", "netBotzTrapResolveTime"),
        ("NetBotz50-MIB", "netBotzTrapSeverity"),
        ("NetBotz50-MIB", "netBotzTrapSensorValue"),
        ("NetBotz50-MIB", "netBotzTrapSensorValueInt"),
        ("NetBotz50-MIB", "netBotzTrapSensorValueFraction"))
)
if mibBuilder.loadTexts:
    netBotzSmokeSensorUnplugged.setStatus(
        "current"
    )

netBotzSmokeSensorValueError = NotificationType(
    (1, 3, 6, 1, 4, 1, 52674, 500, 10, 1, 18, 0, 10)
)
netBotzSmokeSensorValueError.setObjects(
      *(("NetBotz50-MIB", "netBotzTrapErrorID"),
        ("NetBotz50-MIB", "netBotzTrapErrorType"),
        ("NetBotz50-MIB", "netBotzTrapErrorTypeLabel"),
        ("NetBotz50-MIB", "netBotzTrapSensorID"),
        ("NetBotz50-MIB", "netBotzTrapSensorLabel"),
        ("NetBotz50-MIB", "netBotzTrapContainerID"),
        ("NetBotz50-MIB", "netBotzTrapContainerLabel"),
        ("NetBotz50-MIB", "netBotzTrapPortID"),
        ("NetBotz50-MIB", "netBotzTrapPortLabel"),
        ("NetBotz50-MIB", "netBotzTrapStartTime"),
        ("NetBotz50-MIB", "netBotzTrapNotifyTime"),
        ("NetBotz50-MIB", "netBotzTrapResolveTime"),
        ("NetBotz50-MIB", "netBotzTrapSeverity"),
        ("NetBotz50-MIB", "netBotzTrapSensorValue"),
        ("NetBotz50-MIB", "netBotzTrapSensorValueInt"),
        ("NetBotz50-MIB", "netBotzTrapSensorValueFraction"))
)
if mibBuilder.loadTexts:
    netBotzSmokeSensorValueError.setStatus(
        "current"
    )

netBotzSmokeSensorErrorRTN = NotificationType(
    (1, 3, 6, 1, 4, 1, 52674, 500, 10, 1, 18, 0, 101)
)
netBotzSmokeSensorErrorRTN.setObjects(
      *(("NetBotz50-MIB", "netBotzTrapErrorID"),
        ("NetBotz50-MIB", "netBotzTrapErrorType"),
        ("NetBotz50-MIB", "netBotzTrapErrorTypeLabel"),
        ("NetBotz50-MIB", "netBotzTrapSensorID"),
        ("NetBotz50-MIB", "netBotzTrapSensorLabel"),
        ("NetBotz50-MIB", "netBotzTrapContainerID"),
        ("NetBotz50-MIB", "netBotzTrapContainerLabel"),
        ("NetBotz50-MIB", "netBotzTrapPortID"),
        ("NetBotz50-MIB", "netBotzTrapPortLabel"),
        ("NetBotz50-MIB", "netBotzTrapStartTime"),
        ("NetBotz50-MIB", "netBotzTrapNotifyTime"),
        ("NetBotz50-MIB", "netBotzTrapResolveTime"),
        ("NetBotz50-MIB", "netBotzTrapSeverity"),
        ("NetBotz50-MIB", "netBotzTrapSensorValue"),
        ("NetBotz50-MIB", "netBotzTrapSensorValueInt"),
        ("NetBotz50-MIB", "netBotzTrapSensorValueFraction"))
)
if mibBuilder.loadTexts:
    netBotzSmokeSensorErrorRTN.setStatus(
        "current"
    )

netBotzSmokeSensorReplugged = NotificationType(
    (1, 3, 6, 1, 4, 1, 52674, 500, 10, 1, 18, 0, 106)
)
netBotzSmokeSensorReplugged.setObjects(
      *(("NetBotz50-MIB", "netBotzTrapErrorID"),
        ("NetBotz50-MIB", "netBotzTrapErrorType"),
        ("NetBotz50-MIB", "netBotzTrapErrorTypeLabel"),
        ("NetBotz50-MIB", "netBotzTrapSensorID"),
        ("NetBotz50-MIB", "netBotzTrapSensorLabel"),
        ("NetBotz50-MIB", "netBotzTrapContainerID"),
        ("NetBotz50-MIB", "netBotzTrapContainerLabel"),
        ("NetBotz50-MIB", "netBotzTrapPortID"),
        ("NetBotz50-MIB", "netBotzTrapPortLabel"),
        ("NetBotz50-MIB", "netBotzTrapStartTime"),
        ("NetBotz50-MIB", "netBotzTrapNotifyTime"),
        ("NetBotz50-MIB", "netBotzTrapResolveTime"),
        ("NetBotz50-MIB", "netBotzTrapSeverity"),
        ("NetBotz50-MIB", "netBotzTrapSensorValue"),
        ("NetBotz50-MIB", "netBotzTrapSensorValueInt"),
        ("NetBotz50-MIB", "netBotzTrapSensorValueFraction"))
)
if mibBuilder.loadTexts:
    netBotzSmokeSensorReplugged.setStatus(
        "current"
    )

netBotzSmokeSensorValueErrorRTN = NotificationType(
    (1, 3, 6, 1, 4, 1, 52674, 500, 10, 1, 18, 0, 110)
)
netBotzSmokeSensorValueErrorRTN.setObjects(
      *(("NetBotz50-MIB", "netBotzTrapErrorID"),
        ("NetBotz50-MIB", "netBotzTrapErrorType"),
        ("NetBotz50-MIB", "netBotzTrapErrorTypeLabel"),
        ("NetBotz50-MIB", "netBotzTrapSensorID"),
        ("NetBotz50-MIB", "netBotzTrapSensorLabel"),
        ("NetBotz50-MIB", "netBotzTrapContainerID"),
        ("NetBotz50-MIB", "netBotzTrapContainerLabel"),
        ("NetBotz50-MIB", "netBotzTrapPortID"),
        ("NetBotz50-MIB", "netBotzTrapPortLabel"),
        ("NetBotz50-MIB", "netBotzTrapStartTime"),
        ("NetBotz50-MIB", "netBotzTrapNotifyTime"),
        ("NetBotz50-MIB", "netBotzTrapResolveTime"),
        ("NetBotz50-MIB", "netBotzTrapSeverity"),
        ("NetBotz50-MIB", "netBotzTrapSensorValue"),
        ("NetBotz50-MIB", "netBotzTrapSensorValueInt"),
        ("NetBotz50-MIB", "netBotzTrapSensorValueFraction"))
)
if mibBuilder.loadTexts:
    netBotzSmokeSensorValueErrorRTN.setStatus(
        "current"
    )

netBotzVibrationSensorError = NotificationType(
    (1, 3, 6, 1, 4, 1, 52674, 500, 10, 1, 19, 0, 1)
)
netBotzVibrationSensorError.setObjects(
      *(("NetBotz50-MIB", "netBotzTrapErrorID"),
        ("NetBotz50-MIB", "netBotzTrapErrorType"),
        ("NetBotz50-MIB", "netBotzTrapErrorTypeLabel"),
        ("NetBotz50-MIB", "netBotzTrapSensorID"),
        ("NetBotz50-MIB", "netBotzTrapSensorLabel"),
        ("NetBotz50-MIB", "netBotzTrapContainerID"),
        ("NetBotz50-MIB", "netBotzTrapContainerLabel"),
        ("NetBotz50-MIB", "netBotzTrapPortID"),
        ("NetBotz50-MIB", "netBotzTrapPortLabel"),
        ("NetBotz50-MIB", "netBotzTrapStartTime"),
        ("NetBotz50-MIB", "netBotzTrapNotifyTime"),
        ("NetBotz50-MIB", "netBotzTrapResolveTime"),
        ("NetBotz50-MIB", "netBotzTrapSeverity"),
        ("NetBotz50-MIB", "netBotzTrapSensorValue"),
        ("NetBotz50-MIB", "netBotzTrapSensorValueInt"),
        ("NetBotz50-MIB", "netBotzTrapSensorValueFraction"))
)
if mibBuilder.loadTexts:
    netBotzVibrationSensorError.setStatus(
        "current"
    )

netBotzVibrationSensorUnplugged = NotificationType(
    (1, 3, 6, 1, 4, 1, 52674, 500, 10, 1, 19, 0, 6)
)
netBotzVibrationSensorUnplugged.setObjects(
      *(("NetBotz50-MIB", "netBotzTrapErrorID"),
        ("NetBotz50-MIB", "netBotzTrapErrorType"),
        ("NetBotz50-MIB", "netBotzTrapErrorTypeLabel"),
        ("NetBotz50-MIB", "netBotzTrapSensorID"),
        ("NetBotz50-MIB", "netBotzTrapSensorLabel"),
        ("NetBotz50-MIB", "netBotzTrapContainerID"),
        ("NetBotz50-MIB", "netBotzTrapContainerLabel"),
        ("NetBotz50-MIB", "netBotzTrapPortID"),
        ("NetBotz50-MIB", "netBotzTrapPortLabel"),
        ("NetBotz50-MIB", "netBotzTrapStartTime"),
        ("NetBotz50-MIB", "netBotzTrapNotifyTime"),
        ("NetBotz50-MIB", "netBotzTrapResolveTime"),
        ("NetBotz50-MIB", "netBotzTrapSeverity"),
        ("NetBotz50-MIB", "netBotzTrapSensorValue"),
        ("NetBotz50-MIB", "netBotzTrapSensorValueInt"),
        ("NetBotz50-MIB", "netBotzTrapSensorValueFraction"))
)
if mibBuilder.loadTexts:
    netBotzVibrationSensorUnplugged.setStatus(
        "current"
    )

netBotzVibrationSensorValueError = NotificationType(
    (1, 3, 6, 1, 4, 1, 52674, 500, 10, 1, 19, 0, 10)
)
netBotzVibrationSensorValueError.setObjects(
      *(("NetBotz50-MIB", "netBotzTrapErrorID"),
        ("NetBotz50-MIB", "netBotzTrapErrorType"),
        ("NetBotz50-MIB", "netBotzTrapErrorTypeLabel"),
        ("NetBotz50-MIB", "netBotzTrapSensorID"),
        ("NetBotz50-MIB", "netBotzTrapSensorLabel"),
        ("NetBotz50-MIB", "netBotzTrapContainerID"),
        ("NetBotz50-MIB", "netBotzTrapContainerLabel"),
        ("NetBotz50-MIB", "netBotzTrapPortID"),
        ("NetBotz50-MIB", "netBotzTrapPortLabel"),
        ("NetBotz50-MIB", "netBotzTrapStartTime"),
        ("NetBotz50-MIB", "netBotzTrapNotifyTime"),
        ("NetBotz50-MIB", "netBotzTrapResolveTime"),
        ("NetBotz50-MIB", "netBotzTrapSeverity"),
        ("NetBotz50-MIB", "netBotzTrapSensorValue"),
        ("NetBotz50-MIB", "netBotzTrapSensorValueInt"),
        ("NetBotz50-MIB", "netBotzTrapSensorValueFraction"))
)
if mibBuilder.loadTexts:
    netBotzVibrationSensorValueError.setStatus(
        "current"
    )

netBotzVibrationSensorErrorRTN = NotificationType(
    (1, 3, 6, 1, 4, 1, 52674, 500, 10, 1, 19, 0, 101)
)
netBotzVibrationSensorErrorRTN.setObjects(
      *(("NetBotz50-MIB", "netBotzTrapErrorID"),
        ("NetBotz50-MIB", "netBotzTrapErrorType"),
        ("NetBotz50-MIB", "netBotzTrapErrorTypeLabel"),
        ("NetBotz50-MIB", "netBotzTrapSensorID"),
        ("NetBotz50-MIB", "netBotzTrapSensorLabel"),
        ("NetBotz50-MIB", "netBotzTrapContainerID"),
        ("NetBotz50-MIB", "netBotzTrapContainerLabel"),
        ("NetBotz50-MIB", "netBotzTrapPortID"),
        ("NetBotz50-MIB", "netBotzTrapPortLabel"),
        ("NetBotz50-MIB", "netBotzTrapStartTime"),
        ("NetBotz50-MIB", "netBotzTrapNotifyTime"),
        ("NetBotz50-MIB", "netBotzTrapResolveTime"),
        ("NetBotz50-MIB", "netBotzTrapSeverity"),
        ("NetBotz50-MIB", "netBotzTrapSensorValue"),
        ("NetBotz50-MIB", "netBotzTrapSensorValueInt"),
        ("NetBotz50-MIB", "netBotzTrapSensorValueFraction"))
)
if mibBuilder.loadTexts:
    netBotzVibrationSensorErrorRTN.setStatus(
        "current"
    )

netBotzVibrationSensorReplugged = NotificationType(
    (1, 3, 6, 1, 4, 1, 52674, 500, 10, 1, 19, 0, 106)
)
netBotzVibrationSensorReplugged.setObjects(
      *(("NetBotz50-MIB", "netBotzTrapErrorID"),
        ("NetBotz50-MIB", "netBotzTrapErrorType"),
        ("NetBotz50-MIB", "netBotzTrapErrorTypeLabel"),
        ("NetBotz50-MIB", "netBotzTrapSensorID"),
        ("NetBotz50-MIB", "netBotzTrapSensorLabel"),
        ("NetBotz50-MIB", "netBotzTrapContainerID"),
        ("NetBotz50-MIB", "netBotzTrapContainerLabel"),
        ("NetBotz50-MIB", "netBotzTrapPortID"),
        ("NetBotz50-MIB", "netBotzTrapPortLabel"),
        ("NetBotz50-MIB", "netBotzTrapStartTime"),
        ("NetBotz50-MIB", "netBotzTrapNotifyTime"),
        ("NetBotz50-MIB", "netBotzTrapResolveTime"),
        ("NetBotz50-MIB", "netBotzTrapSeverity"),
        ("NetBotz50-MIB", "netBotzTrapSensorValue"),
        ("NetBotz50-MIB", "netBotzTrapSensorValueInt"),
        ("NetBotz50-MIB", "netBotzTrapSensorValueFraction"))
)
if mibBuilder.loadTexts:
    netBotzVibrationSensorReplugged.setStatus(
        "current"
    )

netBotzVibrationSensorValueErrorRTN = NotificationType(
    (1, 3, 6, 1, 4, 1, 52674, 500, 10, 1, 19, 0, 110)
)
netBotzVibrationSensorValueErrorRTN.setObjects(
      *(("NetBotz50-MIB", "netBotzTrapErrorID"),
        ("NetBotz50-MIB", "netBotzTrapErrorType"),
        ("NetBotz50-MIB", "netBotzTrapErrorTypeLabel"),
        ("NetBotz50-MIB", "netBotzTrapSensorID"),
        ("NetBotz50-MIB", "netBotzTrapSensorLabel"),
        ("NetBotz50-MIB", "netBotzTrapContainerID"),
        ("NetBotz50-MIB", "netBotzTrapContainerLabel"),
        ("NetBotz50-MIB", "netBotzTrapPortID"),
        ("NetBotz50-MIB", "netBotzTrapPortLabel"),
        ("NetBotz50-MIB", "netBotzTrapStartTime"),
        ("NetBotz50-MIB", "netBotzTrapNotifyTime"),
        ("NetBotz50-MIB", "netBotzTrapResolveTime"),
        ("NetBotz50-MIB", "netBotzTrapSeverity"),
        ("NetBotz50-MIB", "netBotzTrapSensorValue"),
        ("NetBotz50-MIB", "netBotzTrapSensorValueInt"),
        ("NetBotz50-MIB", "netBotzTrapSensorValueFraction"))
)
if mibBuilder.loadTexts:
    netBotzVibrationSensorValueErrorRTN.setStatus(
        "current"
    )

netBotzDoorSensorForcedEntryError = NotificationType(
    (1, 3, 6, 1, 4, 1, 52674, 500, 10, 1, 20, 0, 10)
)
netBotzDoorSensorForcedEntryError.setObjects(
      *(("NetBotz50-MIB", "netBotzTrapErrorID"),
        ("NetBotz50-MIB", "netBotzTrapErrorType"),
        ("NetBotz50-MIB", "netBotzTrapErrorTypeLabel"),
        ("NetBotz50-MIB", "netBotzTrapSensorID"),
        ("NetBotz50-MIB", "netBotzTrapSensorLabel"),
        ("NetBotz50-MIB", "netBotzTrapContainerID"),
        ("NetBotz50-MIB", "netBotzTrapContainerLabel"),
        ("NetBotz50-MIB", "netBotzTrapPortID"),
        ("NetBotz50-MIB", "netBotzTrapPortLabel"),
        ("NetBotz50-MIB", "netBotzTrapStartTime"),
        ("NetBotz50-MIB", "netBotzTrapNotifyTime"),
        ("NetBotz50-MIB", "netBotzTrapResolveTime"),
        ("NetBotz50-MIB", "netBotzTrapSeverity"),
        ("NetBotz50-MIB", "netBotzTrapSensorValue"),
        ("NetBotz50-MIB", "netBotzTrapSensorValueInt"),
        ("NetBotz50-MIB", "netBotzTrapSensorValueFraction"))
)
if mibBuilder.loadTexts:
    netBotzDoorSensorForcedEntryError.setStatus(
        "current"
    )

netBotzRackHandleSensorOpenError = NotificationType(
    (1, 3, 6, 1, 4, 1, 52674, 500, 10, 1, 20, 0, 11)
)
netBotzRackHandleSensorOpenError.setObjects(
      *(("NetBotz50-MIB", "netBotzTrapErrorID"),
        ("NetBotz50-MIB", "netBotzTrapErrorType"),
        ("NetBotz50-MIB", "netBotzTrapErrorTypeLabel"),
        ("NetBotz50-MIB", "netBotzTrapSensorID"),
        ("NetBotz50-MIB", "netBotzTrapSensorLabel"),
        ("NetBotz50-MIB", "netBotzTrapContainerID"),
        ("NetBotz50-MIB", "netBotzTrapContainerLabel"),
        ("NetBotz50-MIB", "netBotzTrapPortID"),
        ("NetBotz50-MIB", "netBotzTrapPortLabel"),
        ("NetBotz50-MIB", "netBotzTrapStartTime"),
        ("NetBotz50-MIB", "netBotzTrapNotifyTime"),
        ("NetBotz50-MIB", "netBotzTrapResolveTime"),
        ("NetBotz50-MIB", "netBotzTrapSeverity"),
        ("NetBotz50-MIB", "netBotzTrapSensorValue"),
        ("NetBotz50-MIB", "netBotzTrapSensorValueInt"),
        ("NetBotz50-MIB", "netBotzTrapSensorValueFraction"))
)
if mibBuilder.loadTexts:
    netBotzRackHandleSensorOpenError.setStatus(
        "current"
    )

netBotzCardReaderLocalAuthorizationError = NotificationType(
    (1, 3, 6, 1, 4, 1, 52674, 500, 10, 1, 20, 0, 12)
)
netBotzCardReaderLocalAuthorizationError.setObjects(
      *(("NetBotz50-MIB", "netBotzTrapErrorID"),
        ("NetBotz50-MIB", "netBotzTrapErrorType"),
        ("NetBotz50-MIB", "netBotzTrapErrorTypeLabel"),
        ("NetBotz50-MIB", "netBotzTrapSensorID"),
        ("NetBotz50-MIB", "netBotzTrapSensorLabel"),
        ("NetBotz50-MIB", "netBotzTrapContainerID"),
        ("NetBotz50-MIB", "netBotzTrapContainerLabel"),
        ("NetBotz50-MIB", "netBotzTrapPortID"),
        ("NetBotz50-MIB", "netBotzTrapPortLabel"),
        ("NetBotz50-MIB", "netBotzTrapStartTime"),
        ("NetBotz50-MIB", "netBotzTrapNotifyTime"),
        ("NetBotz50-MIB", "netBotzTrapResolveTime"),
        ("NetBotz50-MIB", "netBotzTrapSeverity"),
        ("NetBotz50-MIB", "netBotzTrapSensorValue"),
        ("NetBotz50-MIB", "netBotzTrapSensorValueInt"),
        ("NetBotz50-MIB", "netBotzTrapSensorValueFraction"))
)
if mibBuilder.loadTexts:
    netBotzCardReaderLocalAuthorizationError.setStatus(
        "current"
    )

netBotzCardReaderLdapAuthorizationError = NotificationType(
    (1, 3, 6, 1, 4, 1, 52674, 500, 10, 1, 20, 0, 13)
)
netBotzCardReaderLdapAuthorizationError.setObjects(
      *(("NetBotz50-MIB", "netBotzTrapErrorID"),
        ("NetBotz50-MIB", "netBotzTrapErrorType"),
        ("NetBotz50-MIB", "netBotzTrapErrorTypeLabel"),
        ("NetBotz50-MIB", "netBotzTrapSensorID"),
        ("NetBotz50-MIB", "netBotzTrapSensorLabel"),
        ("NetBotz50-MIB", "netBotzTrapContainerID"),
        ("NetBotz50-MIB", "netBotzTrapContainerLabel"),
        ("NetBotz50-MIB", "netBotzTrapPortID"),
        ("NetBotz50-MIB", "netBotzTrapPortLabel"),
        ("NetBotz50-MIB", "netBotzTrapStartTime"),
        ("NetBotz50-MIB", "netBotzTrapNotifyTime"),
        ("NetBotz50-MIB", "netBotzTrapResolveTime"),
        ("NetBotz50-MIB", "netBotzTrapSeverity"),
        ("NetBotz50-MIB", "netBotzTrapSensorValue"),
        ("NetBotz50-MIB", "netBotzTrapSensorValueInt"),
        ("NetBotz50-MIB", "netBotzTrapSensorValueFraction"))
)
if mibBuilder.loadTexts:
    netBotzCardReaderLdapAuthorizationError.setStatus(
        "current"
    )

netBotzCardReaderUnplugged = NotificationType(
    (1, 3, 6, 1, 4, 1, 52674, 500, 10, 1, 20, 0, 14)
)
netBotzCardReaderUnplugged.setObjects(
      *(("NetBotz50-MIB", "netBotzTrapErrorID"),
        ("NetBotz50-MIB", "netBotzTrapErrorType"),
        ("NetBotz50-MIB", "netBotzTrapErrorTypeLabel"),
        ("NetBotz50-MIB", "netBotzTrapSensorID"),
        ("NetBotz50-MIB", "netBotzTrapSensorLabel"),
        ("NetBotz50-MIB", "netBotzTrapContainerID"),
        ("NetBotz50-MIB", "netBotzTrapContainerLabel"),
        ("NetBotz50-MIB", "netBotzTrapPortID"),
        ("NetBotz50-MIB", "netBotzTrapPortLabel"),
        ("NetBotz50-MIB", "netBotzTrapStartTime"),
        ("NetBotz50-MIB", "netBotzTrapNotifyTime"),
        ("NetBotz50-MIB", "netBotzTrapResolveTime"),
        ("NetBotz50-MIB", "netBotzTrapSeverity"),
        ("NetBotz50-MIB", "netBotzTrapSensorValue"),
        ("NetBotz50-MIB", "netBotzTrapSensorValueInt"),
        ("NetBotz50-MIB", "netBotzTrapSensorValueFraction"))
)
if mibBuilder.loadTexts:
    netBotzCardReaderUnplugged.setStatus(
        "current"
    )

netBotzCardReaderReplugged = NotificationType(
    (1, 3, 6, 1, 4, 1, 52674, 500, 10, 1, 20, 0, 15)
)
netBotzCardReaderReplugged.setObjects(
      *(("NetBotz50-MIB", "netBotzTrapErrorID"),
        ("NetBotz50-MIB", "netBotzTrapErrorType"),
        ("NetBotz50-MIB", "netBotzTrapErrorTypeLabel"),
        ("NetBotz50-MIB", "netBotzTrapSensorID"),
        ("NetBotz50-MIB", "netBotzTrapSensorLabel"),
        ("NetBotz50-MIB", "netBotzTrapContainerID"),
        ("NetBotz50-MIB", "netBotzTrapContainerLabel"),
        ("NetBotz50-MIB", "netBotzTrapPortID"),
        ("NetBotz50-MIB", "netBotzTrapPortLabel"),
        ("NetBotz50-MIB", "netBotzTrapStartTime"),
        ("NetBotz50-MIB", "netBotzTrapNotifyTime"),
        ("NetBotz50-MIB", "netBotzTrapResolveTime"),
        ("NetBotz50-MIB", "netBotzTrapSeverity"),
        ("NetBotz50-MIB", "netBotzTrapSensorValue"),
        ("NetBotz50-MIB", "netBotzTrapSensorValueInt"),
        ("NetBotz50-MIB", "netBotzTrapSensorValueFraction"))
)
if mibBuilder.loadTexts:
    netBotzCardReaderReplugged.setStatus(
        "current"
    )

netBotzCardReaderError = NotificationType(
    (1, 3, 6, 1, 4, 1, 52674, 500, 10, 1, 20, 0, 16)
)
netBotzCardReaderError.setObjects(
      *(("NetBotz50-MIB", "netBotzTrapErrorID"),
        ("NetBotz50-MIB", "netBotzTrapErrorType"),
        ("NetBotz50-MIB", "netBotzTrapErrorTypeLabel"),
        ("NetBotz50-MIB", "netBotzTrapSensorID"),
        ("NetBotz50-MIB", "netBotzTrapSensorLabel"),
        ("NetBotz50-MIB", "netBotzTrapContainerID"),
        ("NetBotz50-MIB", "netBotzTrapContainerLabel"),
        ("NetBotz50-MIB", "netBotzTrapPortID"),
        ("NetBotz50-MIB", "netBotzTrapPortLabel"),
        ("NetBotz50-MIB", "netBotzTrapStartTime"),
        ("NetBotz50-MIB", "netBotzTrapNotifyTime"),
        ("NetBotz50-MIB", "netBotzTrapResolveTime"),
        ("NetBotz50-MIB", "netBotzTrapSeverity"),
        ("NetBotz50-MIB", "netBotzTrapSensorValue"),
        ("NetBotz50-MIB", "netBotzTrapSensorValueInt"),
        ("NetBotz50-MIB", "netBotzTrapSensorValueFraction"))
)
if mibBuilder.loadTexts:
    netBotzCardReaderError.setStatus(
        "current"
    )

netBotzCardReaderErrorRTN = NotificationType(
    (1, 3, 6, 1, 4, 1, 52674, 500, 10, 1, 20, 0, 17)
)
netBotzCardReaderErrorRTN.setObjects(
      *(("NetBotz50-MIB", "netBotzTrapErrorID"),
        ("NetBotz50-MIB", "netBotzTrapErrorType"),
        ("NetBotz50-MIB", "netBotzTrapErrorTypeLabel"),
        ("NetBotz50-MIB", "netBotzTrapSensorID"),
        ("NetBotz50-MIB", "netBotzTrapSensorLabel"),
        ("NetBotz50-MIB", "netBotzTrapContainerID"),
        ("NetBotz50-MIB", "netBotzTrapContainerLabel"),
        ("NetBotz50-MIB", "netBotzTrapPortID"),
        ("NetBotz50-MIB", "netBotzTrapPortLabel"),
        ("NetBotz50-MIB", "netBotzTrapStartTime"),
        ("NetBotz50-MIB", "netBotzTrapNotifyTime"),
        ("NetBotz50-MIB", "netBotzTrapResolveTime"),
        ("NetBotz50-MIB", "netBotzTrapSeverity"),
        ("NetBotz50-MIB", "netBotzTrapSensorValue"),
        ("NetBotz50-MIB", "netBotzTrapSensorValueInt"),
        ("NetBotz50-MIB", "netBotzTrapSensorValueFraction"))
)
if mibBuilder.loadTexts:
    netBotzCardReaderErrorRTN.setStatus(
        "current"
    )

netBotzCardReaderValueError = NotificationType(
    (1, 3, 6, 1, 4, 1, 52674, 500, 10, 1, 20, 0, 18)
)
netBotzCardReaderValueError.setObjects(
      *(("NetBotz50-MIB", "netBotzTrapErrorID"),
        ("NetBotz50-MIB", "netBotzTrapErrorType"),
        ("NetBotz50-MIB", "netBotzTrapErrorTypeLabel"),
        ("NetBotz50-MIB", "netBotzTrapSensorID"),
        ("NetBotz50-MIB", "netBotzTrapSensorLabel"),
        ("NetBotz50-MIB", "netBotzTrapContainerID"),
        ("NetBotz50-MIB", "netBotzTrapContainerLabel"),
        ("NetBotz50-MIB", "netBotzTrapPortID"),
        ("NetBotz50-MIB", "netBotzTrapPortLabel"),
        ("NetBotz50-MIB", "netBotzTrapStartTime"),
        ("NetBotz50-MIB", "netBotzTrapNotifyTime"),
        ("NetBotz50-MIB", "netBotzTrapResolveTime"),
        ("NetBotz50-MIB", "netBotzTrapSeverity"),
        ("NetBotz50-MIB", "netBotzTrapSensorValue"),
        ("NetBotz50-MIB", "netBotzTrapSensorValueInt"),
        ("NetBotz50-MIB", "netBotzTrapSensorValueFraction"))
)
if mibBuilder.loadTexts:
    netBotzCardReaderValueError.setStatus(
        "current"
    )

netBotzCardReaderValueErrorRTN = NotificationType(
    (1, 3, 6, 1, 4, 1, 52674, 500, 10, 1, 20, 0, 19)
)
netBotzCardReaderValueErrorRTN.setObjects(
      *(("NetBotz50-MIB", "netBotzTrapErrorID"),
        ("NetBotz50-MIB", "netBotzTrapErrorType"),
        ("NetBotz50-MIB", "netBotzTrapErrorTypeLabel"),
        ("NetBotz50-MIB", "netBotzTrapSensorID"),
        ("NetBotz50-MIB", "netBotzTrapSensorLabel"),
        ("NetBotz50-MIB", "netBotzTrapContainerID"),
        ("NetBotz50-MIB", "netBotzTrapContainerLabel"),
        ("NetBotz50-MIB", "netBotzTrapPortID"),
        ("NetBotz50-MIB", "netBotzTrapPortLabel"),
        ("NetBotz50-MIB", "netBotzTrapStartTime"),
        ("NetBotz50-MIB", "netBotzTrapNotifyTime"),
        ("NetBotz50-MIB", "netBotzTrapResolveTime"),
        ("NetBotz50-MIB", "netBotzTrapSeverity"),
        ("NetBotz50-MIB", "netBotzTrapSensorValue"),
        ("NetBotz50-MIB", "netBotzTrapSensorValueInt"),
        ("NetBotz50-MIB", "netBotzTrapSensorValueFraction"))
)
if mibBuilder.loadTexts:
    netBotzCardReaderValueErrorRTN.setStatus(
        "current"
    )

netBotzRackHandleSensorUnplugged = NotificationType(
    (1, 3, 6, 1, 4, 1, 52674, 500, 10, 1, 20, 0, 20)
)
netBotzRackHandleSensorUnplugged.setObjects(
      *(("NetBotz50-MIB", "netBotzTrapErrorID"),
        ("NetBotz50-MIB", "netBotzTrapErrorType"),
        ("NetBotz50-MIB", "netBotzTrapErrorTypeLabel"),
        ("NetBotz50-MIB", "netBotzTrapSensorID"),
        ("NetBotz50-MIB", "netBotzTrapSensorLabel"),
        ("NetBotz50-MIB", "netBotzTrapContainerID"),
        ("NetBotz50-MIB", "netBotzTrapContainerLabel"),
        ("NetBotz50-MIB", "netBotzTrapPortID"),
        ("NetBotz50-MIB", "netBotzTrapPortLabel"),
        ("NetBotz50-MIB", "netBotzTrapStartTime"),
        ("NetBotz50-MIB", "netBotzTrapNotifyTime"),
        ("NetBotz50-MIB", "netBotzTrapResolveTime"),
        ("NetBotz50-MIB", "netBotzTrapSeverity"),
        ("NetBotz50-MIB", "netBotzTrapSensorValue"),
        ("NetBotz50-MIB", "netBotzTrapSensorValueInt"),
        ("NetBotz50-MIB", "netBotzTrapSensorValueFraction"))
)
if mibBuilder.loadTexts:
    netBotzRackHandleSensorUnplugged.setStatus(
        "current"
    )

netBotzRackHandleSensorReplugged = NotificationType(
    (1, 3, 6, 1, 4, 1, 52674, 500, 10, 1, 20, 0, 21)
)
netBotzRackHandleSensorReplugged.setObjects(
      *(("NetBotz50-MIB", "netBotzTrapErrorID"),
        ("NetBotz50-MIB", "netBotzTrapErrorType"),
        ("NetBotz50-MIB", "netBotzTrapErrorTypeLabel"),
        ("NetBotz50-MIB", "netBotzTrapSensorID"),
        ("NetBotz50-MIB", "netBotzTrapSensorLabel"),
        ("NetBotz50-MIB", "netBotzTrapContainerID"),
        ("NetBotz50-MIB", "netBotzTrapContainerLabel"),
        ("NetBotz50-MIB", "netBotzTrapPortID"),
        ("NetBotz50-MIB", "netBotzTrapPortLabel"),
        ("NetBotz50-MIB", "netBotzTrapStartTime"),
        ("NetBotz50-MIB", "netBotzTrapNotifyTime"),
        ("NetBotz50-MIB", "netBotzTrapResolveTime"),
        ("NetBotz50-MIB", "netBotzTrapSeverity"),
        ("NetBotz50-MIB", "netBotzTrapSensorValue"),
        ("NetBotz50-MIB", "netBotzTrapSensorValueInt"),
        ("NetBotz50-MIB", "netBotzTrapSensorValueFraction"))
)
if mibBuilder.loadTexts:
    netBotzRackHandleSensorReplugged.setStatus(
        "current"
    )

netBotzRackHandleSensorError = NotificationType(
    (1, 3, 6, 1, 4, 1, 52674, 500, 10, 1, 20, 0, 22)
)
netBotzRackHandleSensorError.setObjects(
      *(("NetBotz50-MIB", "netBotzTrapErrorID"),
        ("NetBotz50-MIB", "netBotzTrapErrorType"),
        ("NetBotz50-MIB", "netBotzTrapErrorTypeLabel"),
        ("NetBotz50-MIB", "netBotzTrapSensorID"),
        ("NetBotz50-MIB", "netBotzTrapSensorLabel"),
        ("NetBotz50-MIB", "netBotzTrapContainerID"),
        ("NetBotz50-MIB", "netBotzTrapContainerLabel"),
        ("NetBotz50-MIB", "netBotzTrapPortID"),
        ("NetBotz50-MIB", "netBotzTrapPortLabel"),
        ("NetBotz50-MIB", "netBotzTrapStartTime"),
        ("NetBotz50-MIB", "netBotzTrapNotifyTime"),
        ("NetBotz50-MIB", "netBotzTrapResolveTime"),
        ("NetBotz50-MIB", "netBotzTrapSeverity"),
        ("NetBotz50-MIB", "netBotzTrapSensorValue"),
        ("NetBotz50-MIB", "netBotzTrapSensorValueInt"),
        ("NetBotz50-MIB", "netBotzTrapSensorValueFraction"))
)
if mibBuilder.loadTexts:
    netBotzRackHandleSensorError.setStatus(
        "current"
    )

netBotzRackHandleSensorErrorRTN = NotificationType(
    (1, 3, 6, 1, 4, 1, 52674, 500, 10, 1, 20, 0, 23)
)
netBotzRackHandleSensorErrorRTN.setObjects(
      *(("NetBotz50-MIB", "netBotzTrapErrorID"),
        ("NetBotz50-MIB", "netBotzTrapErrorType"),
        ("NetBotz50-MIB", "netBotzTrapErrorTypeLabel"),
        ("NetBotz50-MIB", "netBotzTrapSensorID"),
        ("NetBotz50-MIB", "netBotzTrapSensorLabel"),
        ("NetBotz50-MIB", "netBotzTrapContainerID"),
        ("NetBotz50-MIB", "netBotzTrapContainerLabel"),
        ("NetBotz50-MIB", "netBotzTrapPortID"),
        ("NetBotz50-MIB", "netBotzTrapPortLabel"),
        ("NetBotz50-MIB", "netBotzTrapStartTime"),
        ("NetBotz50-MIB", "netBotzTrapNotifyTime"),
        ("NetBotz50-MIB", "netBotzTrapResolveTime"),
        ("NetBotz50-MIB", "netBotzTrapSeverity"),
        ("NetBotz50-MIB", "netBotzTrapSensorValue"),
        ("NetBotz50-MIB", "netBotzTrapSensorValueInt"),
        ("NetBotz50-MIB", "netBotzTrapSensorValueFraction"))
)
if mibBuilder.loadTexts:
    netBotzRackHandleSensorErrorRTN.setStatus(
        "current"
    )

netBotzRackHandleSensorValueError = NotificationType(
    (1, 3, 6, 1, 4, 1, 52674, 500, 10, 1, 20, 0, 24)
)
netBotzRackHandleSensorValueError.setObjects(
      *(("NetBotz50-MIB", "netBotzTrapErrorID"),
        ("NetBotz50-MIB", "netBotzTrapErrorType"),
        ("NetBotz50-MIB", "netBotzTrapErrorTypeLabel"),
        ("NetBotz50-MIB", "netBotzTrapSensorID"),
        ("NetBotz50-MIB", "netBotzTrapSensorLabel"),
        ("NetBotz50-MIB", "netBotzTrapContainerID"),
        ("NetBotz50-MIB", "netBotzTrapContainerLabel"),
        ("NetBotz50-MIB", "netBotzTrapPortID"),
        ("NetBotz50-MIB", "netBotzTrapPortLabel"),
        ("NetBotz50-MIB", "netBotzTrapStartTime"),
        ("NetBotz50-MIB", "netBotzTrapNotifyTime"),
        ("NetBotz50-MIB", "netBotzTrapResolveTime"),
        ("NetBotz50-MIB", "netBotzTrapSeverity"),
        ("NetBotz50-MIB", "netBotzTrapSensorValue"),
        ("NetBotz50-MIB", "netBotzTrapSensorValueInt"),
        ("NetBotz50-MIB", "netBotzTrapSensorValueFraction"))
)
if mibBuilder.loadTexts:
    netBotzRackHandleSensorValueError.setStatus(
        "current"
    )

netBotzRackHandleSensorValueErrorRTN = NotificationType(
    (1, 3, 6, 1, 4, 1, 52674, 500, 10, 1, 20, 0, 25)
)
netBotzRackHandleSensorValueErrorRTN.setObjects(
      *(("NetBotz50-MIB", "netBotzTrapErrorID"),
        ("NetBotz50-MIB", "netBotzTrapErrorType"),
        ("NetBotz50-MIB", "netBotzTrapErrorTypeLabel"),
        ("NetBotz50-MIB", "netBotzTrapSensorID"),
        ("NetBotz50-MIB", "netBotzTrapSensorLabel"),
        ("NetBotz50-MIB", "netBotzTrapContainerID"),
        ("NetBotz50-MIB", "netBotzTrapContainerLabel"),
        ("NetBotz50-MIB", "netBotzTrapPortID"),
        ("NetBotz50-MIB", "netBotzTrapPortLabel"),
        ("NetBotz50-MIB", "netBotzTrapStartTime"),
        ("NetBotz50-MIB", "netBotzTrapNotifyTime"),
        ("NetBotz50-MIB", "netBotzTrapResolveTime"),
        ("NetBotz50-MIB", "netBotzTrapSeverity"),
        ("NetBotz50-MIB", "netBotzTrapSensorValue"),
        ("NetBotz50-MIB", "netBotzTrapSensorValueInt"),
        ("NetBotz50-MIB", "netBotzTrapSensorValueFraction"))
)
if mibBuilder.loadTexts:
    netBotzRackHandleSensorValueErrorRTN.setStatus(
        "current"
    )

netBotzLockSensorUnplugged = NotificationType(
    (1, 3, 6, 1, 4, 1, 52674, 500, 10, 1, 20, 0, 26)
)
netBotzLockSensorUnplugged.setObjects(
      *(("NetBotz50-MIB", "netBotzTrapErrorID"),
        ("NetBotz50-MIB", "netBotzTrapErrorType"),
        ("NetBotz50-MIB", "netBotzTrapErrorTypeLabel"),
        ("NetBotz50-MIB", "netBotzTrapSensorID"),
        ("NetBotz50-MIB", "netBotzTrapSensorLabel"),
        ("NetBotz50-MIB", "netBotzTrapContainerID"),
        ("NetBotz50-MIB", "netBotzTrapContainerLabel"),
        ("NetBotz50-MIB", "netBotzTrapPortID"),
        ("NetBotz50-MIB", "netBotzTrapPortLabel"),
        ("NetBotz50-MIB", "netBotzTrapStartTime"),
        ("NetBotz50-MIB", "netBotzTrapNotifyTime"),
        ("NetBotz50-MIB", "netBotzTrapResolveTime"),
        ("NetBotz50-MIB", "netBotzTrapSeverity"),
        ("NetBotz50-MIB", "netBotzTrapSensorValue"),
        ("NetBotz50-MIB", "netBotzTrapSensorValueInt"),
        ("NetBotz50-MIB", "netBotzTrapSensorValueFraction"))
)
if mibBuilder.loadTexts:
    netBotzLockSensorUnplugged.setStatus(
        "current"
    )

netBotzLockSensorReplugged = NotificationType(
    (1, 3, 6, 1, 4, 1, 52674, 500, 10, 1, 20, 0, 27)
)
netBotzLockSensorReplugged.setObjects(
      *(("NetBotz50-MIB", "netBotzTrapErrorID"),
        ("NetBotz50-MIB", "netBotzTrapErrorType"),
        ("NetBotz50-MIB", "netBotzTrapErrorTypeLabel"),
        ("NetBotz50-MIB", "netBotzTrapSensorID"),
        ("NetBotz50-MIB", "netBotzTrapSensorLabel"),
        ("NetBotz50-MIB", "netBotzTrapContainerID"),
        ("NetBotz50-MIB", "netBotzTrapContainerLabel"),
        ("NetBotz50-MIB", "netBotzTrapPortID"),
        ("NetBotz50-MIB", "netBotzTrapPortLabel"),
        ("NetBotz50-MIB", "netBotzTrapStartTime"),
        ("NetBotz50-MIB", "netBotzTrapNotifyTime"),
        ("NetBotz50-MIB", "netBotzTrapResolveTime"),
        ("NetBotz50-MIB", "netBotzTrapSeverity"),
        ("NetBotz50-MIB", "netBotzTrapSensorValue"),
        ("NetBotz50-MIB", "netBotzTrapSensorValueInt"),
        ("NetBotz50-MIB", "netBotzTrapSensorValueFraction"))
)
if mibBuilder.loadTexts:
    netBotzLockSensorReplugged.setStatus(
        "current"
    )

netBotzLockSensorError = NotificationType(
    (1, 3, 6, 1, 4, 1, 52674, 500, 10, 1, 20, 0, 28)
)
netBotzLockSensorError.setObjects(
      *(("NetBotz50-MIB", "netBotzTrapErrorID"),
        ("NetBotz50-MIB", "netBotzTrapErrorType"),
        ("NetBotz50-MIB", "netBotzTrapErrorTypeLabel"),
        ("NetBotz50-MIB", "netBotzTrapSensorID"),
        ("NetBotz50-MIB", "netBotzTrapSensorLabel"),
        ("NetBotz50-MIB", "netBotzTrapContainerID"),
        ("NetBotz50-MIB", "netBotzTrapContainerLabel"),
        ("NetBotz50-MIB", "netBotzTrapPortID"),
        ("NetBotz50-MIB", "netBotzTrapPortLabel"),
        ("NetBotz50-MIB", "netBotzTrapStartTime"),
        ("NetBotz50-MIB", "netBotzTrapNotifyTime"),
        ("NetBotz50-MIB", "netBotzTrapResolveTime"),
        ("NetBotz50-MIB", "netBotzTrapSeverity"),
        ("NetBotz50-MIB", "netBotzTrapSensorValue"),
        ("NetBotz50-MIB", "netBotzTrapSensorValueInt"),
        ("NetBotz50-MIB", "netBotzTrapSensorValueFraction"))
)
if mibBuilder.loadTexts:
    netBotzLockSensorError.setStatus(
        "current"
    )

netBotzLockSensorErrorRTN = NotificationType(
    (1, 3, 6, 1, 4, 1, 52674, 500, 10, 1, 20, 0, 29)
)
netBotzLockSensorErrorRTN.setObjects(
      *(("NetBotz50-MIB", "netBotzTrapErrorID"),
        ("NetBotz50-MIB", "netBotzTrapErrorType"),
        ("NetBotz50-MIB", "netBotzTrapErrorTypeLabel"),
        ("NetBotz50-MIB", "netBotzTrapSensorID"),
        ("NetBotz50-MIB", "netBotzTrapSensorLabel"),
        ("NetBotz50-MIB", "netBotzTrapContainerID"),
        ("NetBotz50-MIB", "netBotzTrapContainerLabel"),
        ("NetBotz50-MIB", "netBotzTrapPortID"),
        ("NetBotz50-MIB", "netBotzTrapPortLabel"),
        ("NetBotz50-MIB", "netBotzTrapStartTime"),
        ("NetBotz50-MIB", "netBotzTrapNotifyTime"),
        ("NetBotz50-MIB", "netBotzTrapResolveTime"),
        ("NetBotz50-MIB", "netBotzTrapSeverity"),
        ("NetBotz50-MIB", "netBotzTrapSensorValue"),
        ("NetBotz50-MIB", "netBotzTrapSensorValueInt"),
        ("NetBotz50-MIB", "netBotzTrapSensorValueFraction"))
)
if mibBuilder.loadTexts:
    netBotzLockSensorErrorRTN.setStatus(
        "current"
    )

netBotzLockSensorValueError = NotificationType(
    (1, 3, 6, 1, 4, 1, 52674, 500, 10, 1, 20, 0, 30)
)
netBotzLockSensorValueError.setObjects(
      *(("NetBotz50-MIB", "netBotzTrapErrorID"),
        ("NetBotz50-MIB", "netBotzTrapErrorType"),
        ("NetBotz50-MIB", "netBotzTrapErrorTypeLabel"),
        ("NetBotz50-MIB", "netBotzTrapSensorID"),
        ("NetBotz50-MIB", "netBotzTrapSensorLabel"),
        ("NetBotz50-MIB", "netBotzTrapContainerID"),
        ("NetBotz50-MIB", "netBotzTrapContainerLabel"),
        ("NetBotz50-MIB", "netBotzTrapPortID"),
        ("NetBotz50-MIB", "netBotzTrapPortLabel"),
        ("NetBotz50-MIB", "netBotzTrapStartTime"),
        ("NetBotz50-MIB", "netBotzTrapNotifyTime"),
        ("NetBotz50-MIB", "netBotzTrapResolveTime"),
        ("NetBotz50-MIB", "netBotzTrapSeverity"),
        ("NetBotz50-MIB", "netBotzTrapSensorValue"),
        ("NetBotz50-MIB", "netBotzTrapSensorValueInt"),
        ("NetBotz50-MIB", "netBotzTrapSensorValueFraction"))
)
if mibBuilder.loadTexts:
    netBotzLockSensorValueError.setStatus(
        "current"
    )

netBotzLockSensorValueErrorRTN = NotificationType(
    (1, 3, 6, 1, 4, 1, 52674, 500, 10, 1, 20, 0, 31)
)
netBotzLockSensorValueErrorRTN.setObjects(
      *(("NetBotz50-MIB", "netBotzTrapErrorID"),
        ("NetBotz50-MIB", "netBotzTrapErrorType"),
        ("NetBotz50-MIB", "netBotzTrapErrorTypeLabel"),
        ("NetBotz50-MIB", "netBotzTrapSensorID"),
        ("NetBotz50-MIB", "netBotzTrapSensorLabel"),
        ("NetBotz50-MIB", "netBotzTrapContainerID"),
        ("NetBotz50-MIB", "netBotzTrapContainerLabel"),
        ("NetBotz50-MIB", "netBotzTrapPortID"),
        ("NetBotz50-MIB", "netBotzTrapPortLabel"),
        ("NetBotz50-MIB", "netBotzTrapStartTime"),
        ("NetBotz50-MIB", "netBotzTrapNotifyTime"),
        ("NetBotz50-MIB", "netBotzTrapResolveTime"),
        ("NetBotz50-MIB", "netBotzTrapSeverity"),
        ("NetBotz50-MIB", "netBotzTrapSensorValue"),
        ("NetBotz50-MIB", "netBotzTrapSensorValueInt"),
        ("NetBotz50-MIB", "netBotzTrapSensorValueFraction"))
)
if mibBuilder.loadTexts:
    netBotzLockSensorValueErrorRTN.setStatus(
        "current"
    )

netBotzDoorSensorForcedEntryErrorRTN = NotificationType(
    (1, 3, 6, 1, 4, 1, 52674, 500, 10, 1, 20, 0, 110)
)
netBotzDoorSensorForcedEntryErrorRTN.setObjects(
      *(("NetBotz50-MIB", "netBotzTrapErrorID"),
        ("NetBotz50-MIB", "netBotzTrapErrorType"),
        ("NetBotz50-MIB", "netBotzTrapErrorTypeLabel"),
        ("NetBotz50-MIB", "netBotzTrapSensorID"),
        ("NetBotz50-MIB", "netBotzTrapSensorLabel"),
        ("NetBotz50-MIB", "netBotzTrapContainerID"),
        ("NetBotz50-MIB", "netBotzTrapContainerLabel"),
        ("NetBotz50-MIB", "netBotzTrapPortID"),
        ("NetBotz50-MIB", "netBotzTrapPortLabel"),
        ("NetBotz50-MIB", "netBotzTrapStartTime"),
        ("NetBotz50-MIB", "netBotzTrapNotifyTime"),
        ("NetBotz50-MIB", "netBotzTrapResolveTime"),
        ("NetBotz50-MIB", "netBotzTrapSeverity"),
        ("NetBotz50-MIB", "netBotzTrapSensorValue"),
        ("NetBotz50-MIB", "netBotzTrapSensorValueInt"),
        ("NetBotz50-MIB", "netBotzTrapSensorValueFraction"))
)
if mibBuilder.loadTexts:
    netBotzDoorSensorForcedEntryErrorRTN.setStatus(
        "current"
    )

netBotzRackHandleSensorOpenErrorRTN = NotificationType(
    (1, 3, 6, 1, 4, 1, 52674, 500, 10, 1, 20, 0, 111)
)
netBotzRackHandleSensorOpenErrorRTN.setObjects(
      *(("NetBotz50-MIB", "netBotzTrapErrorID"),
        ("NetBotz50-MIB", "netBotzTrapErrorType"),
        ("NetBotz50-MIB", "netBotzTrapErrorTypeLabel"),
        ("NetBotz50-MIB", "netBotzTrapSensorID"),
        ("NetBotz50-MIB", "netBotzTrapSensorLabel"),
        ("NetBotz50-MIB", "netBotzTrapContainerID"),
        ("NetBotz50-MIB", "netBotzTrapContainerLabel"),
        ("NetBotz50-MIB", "netBotzTrapPortID"),
        ("NetBotz50-MIB", "netBotzTrapPortLabel"),
        ("NetBotz50-MIB", "netBotzTrapStartTime"),
        ("NetBotz50-MIB", "netBotzTrapNotifyTime"),
        ("NetBotz50-MIB", "netBotzTrapResolveTime"),
        ("NetBotz50-MIB", "netBotzTrapSeverity"),
        ("NetBotz50-MIB", "netBotzTrapSensorValue"),
        ("NetBotz50-MIB", "netBotzTrapSensorValueInt"),
        ("NetBotz50-MIB", "netBotzTrapSensorValueFraction"))
)
if mibBuilder.loadTexts:
    netBotzRackHandleSensorOpenErrorRTN.setStatus(
        "current"
    )

netBotzCardReaderLocalAuthorizationErrorRTN = NotificationType(
    (1, 3, 6, 1, 4, 1, 52674, 500, 10, 1, 20, 0, 112)
)
netBotzCardReaderLocalAuthorizationErrorRTN.setObjects(
      *(("NetBotz50-MIB", "netBotzTrapErrorID"),
        ("NetBotz50-MIB", "netBotzTrapErrorType"),
        ("NetBotz50-MIB", "netBotzTrapErrorTypeLabel"),
        ("NetBotz50-MIB", "netBotzTrapSensorID"),
        ("NetBotz50-MIB", "netBotzTrapSensorLabel"),
        ("NetBotz50-MIB", "netBotzTrapContainerID"),
        ("NetBotz50-MIB", "netBotzTrapContainerLabel"),
        ("NetBotz50-MIB", "netBotzTrapPortID"),
        ("NetBotz50-MIB", "netBotzTrapPortLabel"),
        ("NetBotz50-MIB", "netBotzTrapStartTime"),
        ("NetBotz50-MIB", "netBotzTrapNotifyTime"),
        ("NetBotz50-MIB", "netBotzTrapResolveTime"),
        ("NetBotz50-MIB", "netBotzTrapSeverity"),
        ("NetBotz50-MIB", "netBotzTrapSensorValue"),
        ("NetBotz50-MIB", "netBotzTrapSensorValueInt"),
        ("NetBotz50-MIB", "netBotzTrapSensorValueFraction"))
)
if mibBuilder.loadTexts:
    netBotzCardReaderLocalAuthorizationErrorRTN.setStatus(
        "current"
    )

netBotzCardReaderLdapAuthorizationErrorRTN = NotificationType(
    (1, 3, 6, 1, 4, 1, 52674, 500, 10, 1, 20, 0, 113)
)
netBotzCardReaderLdapAuthorizationErrorRTN.setObjects(
      *(("NetBotz50-MIB", "netBotzTrapErrorID"),
        ("NetBotz50-MIB", "netBotzTrapErrorType"),
        ("NetBotz50-MIB", "netBotzTrapErrorTypeLabel"),
        ("NetBotz50-MIB", "netBotzTrapSensorID"),
        ("NetBotz50-MIB", "netBotzTrapSensorLabel"),
        ("NetBotz50-MIB", "netBotzTrapContainerID"),
        ("NetBotz50-MIB", "netBotzTrapContainerLabel"),
        ("NetBotz50-MIB", "netBotzTrapPortID"),
        ("NetBotz50-MIB", "netBotzTrapPortLabel"),
        ("NetBotz50-MIB", "netBotzTrapStartTime"),
        ("NetBotz50-MIB", "netBotzTrapNotifyTime"),
        ("NetBotz50-MIB", "netBotzTrapResolveTime"),
        ("NetBotz50-MIB", "netBotzTrapSeverity"),
        ("NetBotz50-MIB", "netBotzTrapSensorValue"),
        ("NetBotz50-MIB", "netBotzTrapSensorValueInt"),
        ("NetBotz50-MIB", "netBotzTrapSensorValueFraction"))
)
if mibBuilder.loadTexts:
    netBotzCardReaderLdapAuthorizationErrorRTN.setStatus(
        "current"
    )

netBotzTestNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 52674, 500, 10, 1, 99, 0, 1)
)
netBotzTestNotification.setObjects(
      *(("NetBotz50-MIB", "netBotzTrapNotifyTime"),
        ("NetBotz50-MIB", "netBotzTrapData"))
)
if mibBuilder.loadTexts:
    netBotzTestNotification.setStatus(
        "current"
    )

netBotzPodUnplugged = NotificationType(
    (1, 3, 6, 1, 4, 1, 52674, 500, 10, 2, 0, 7)
)
netBotzPodUnplugged.setObjects(
      *(("NetBotz50-MIB", "netBotzTrapErrorID"),
        ("NetBotz50-MIB", "netBotzTrapErrorType"),
        ("NetBotz50-MIB", "netBotzTrapErrorTypeLabel"),
        ("NetBotz50-MIB", "netBotzTrapContainerID"),
        ("NetBotz50-MIB", "netBotzTrapContainerLabel"),
        ("NetBotz50-MIB", "netBotzTrapPortID"),
        ("NetBotz50-MIB", "netBotzTrapPortLabel"),
        ("NetBotz50-MIB", "netBotzTrapStartTime"),
        ("NetBotz50-MIB", "netBotzTrapNotifyTime"),
        ("NetBotz50-MIB", "netBotzTrapResolveTime"),
        ("NetBotz50-MIB", "netBotzTrapSeverity"))
)
if mibBuilder.loadTexts:
    netBotzPodUnplugged.setStatus(
        "current"
    )

netBotzLogonError = NotificationType(
    (1, 3, 6, 1, 4, 1, 52674, 500, 10, 2, 0, 11)
)
netBotzLogonError.setObjects(
      *(("NetBotz50-MIB", "netBotzTrapErrorID"),
        ("NetBotz50-MIB", "netBotzTrapErrorType"),
        ("NetBotz50-MIB", "netBotzTrapErrorTypeLabel"),
        ("NetBotz50-MIB", "netBotzTrapSensorID"),
        ("NetBotz50-MIB", "netBotzTrapSensorLabel"),
        ("NetBotz50-MIB", "netBotzTrapContainerID"),
        ("NetBotz50-MIB", "netBotzTrapContainerLabel"),
        ("NetBotz50-MIB", "netBotzTrapPortID"),
        ("NetBotz50-MIB", "netBotzTrapPortLabel"),
        ("NetBotz50-MIB", "netBotzTrapStartTime"),
        ("NetBotz50-MIB", "netBotzTrapNotifyTime"),
        ("NetBotz50-MIB", "netBotzTrapResolveTime"),
        ("NetBotz50-MIB", "netBotzTrapSeverity"),
        ("NetBotz50-MIB", "netBotzTrapSensorValue"),
        ("NetBotz50-MIB", "netBotzTrapSensorValueInt"),
        ("NetBotz50-MIB", "netBotzTrapSensorValueFraction"))
)
if mibBuilder.loadTexts:
    netBotzLogonError.setStatus(
        "current"
    )

netBotzRmtLinkError = NotificationType(
    (1, 3, 6, 1, 4, 1, 52674, 500, 10, 2, 0, 13)
)
netBotzRmtLinkError.setObjects(
      *(("NetBotz50-MIB", "netBotzTrapErrorID"),
        ("NetBotz50-MIB", "netBotzTrapErrorType"),
        ("NetBotz50-MIB", "netBotzTrapErrorTypeLabel"),
        ("NetBotz50-MIB", "netBotzTrapSensorID"),
        ("NetBotz50-MIB", "netBotzTrapSensorLabel"),
        ("NetBotz50-MIB", "netBotzTrapContainerID"),
        ("NetBotz50-MIB", "netBotzTrapContainerLabel"),
        ("NetBotz50-MIB", "netBotzTrapPortID"),
        ("NetBotz50-MIB", "netBotzTrapPortLabel"),
        ("NetBotz50-MIB", "netBotzTrapStartTime"),
        ("NetBotz50-MIB", "netBotzTrapNotifyTime"),
        ("NetBotz50-MIB", "netBotzTrapResolveTime"),
        ("NetBotz50-MIB", "netBotzTrapSeverity"),
        ("NetBotz50-MIB", "netBotzTrapSensorValue"),
        ("NetBotz50-MIB", "netBotzTrapSensorValueInt"),
        ("NetBotz50-MIB", "netBotzTrapSensorValueFraction"))
)
if mibBuilder.loadTexts:
    netBotzRmtLinkError.setStatus(
        "current"
    )

netBotzPodReplugged = NotificationType(
    (1, 3, 6, 1, 4, 1, 52674, 500, 10, 2, 0, 107)
)
netBotzPodReplugged.setObjects(
      *(("NetBotz50-MIB", "netBotzTrapErrorID"),
        ("NetBotz50-MIB", "netBotzTrapErrorType"),
        ("NetBotz50-MIB", "netBotzTrapErrorTypeLabel"),
        ("NetBotz50-MIB", "netBotzTrapContainerID"),
        ("NetBotz50-MIB", "netBotzTrapContainerLabel"),
        ("NetBotz50-MIB", "netBotzTrapPortID"),
        ("NetBotz50-MIB", "netBotzTrapPortLabel"),
        ("NetBotz50-MIB", "netBotzTrapStartTime"),
        ("NetBotz50-MIB", "netBotzTrapNotifyTime"),
        ("NetBotz50-MIB", "netBotzTrapResolveTime"),
        ("NetBotz50-MIB", "netBotzTrapSeverity"))
)
if mibBuilder.loadTexts:
    netBotzPodReplugged.setStatus(
        "current"
    )

netBotzLogonErrorResolved = NotificationType(
    (1, 3, 6, 1, 4, 1, 52674, 500, 10, 2, 0, 111)
)
netBotzLogonErrorResolved.setObjects(
      *(("NetBotz50-MIB", "netBotzTrapErrorID"),
        ("NetBotz50-MIB", "netBotzTrapErrorType"),
        ("NetBotz50-MIB", "netBotzTrapErrorTypeLabel"),
        ("NetBotz50-MIB", "netBotzTrapSensorID"),
        ("NetBotz50-MIB", "netBotzTrapSensorLabel"),
        ("NetBotz50-MIB", "netBotzTrapContainerID"),
        ("NetBotz50-MIB", "netBotzTrapContainerLabel"),
        ("NetBotz50-MIB", "netBotzTrapPortID"),
        ("NetBotz50-MIB", "netBotzTrapPortLabel"),
        ("NetBotz50-MIB", "netBotzTrapStartTime"),
        ("NetBotz50-MIB", "netBotzTrapNotifyTime"),
        ("NetBotz50-MIB", "netBotzTrapResolveTime"),
        ("NetBotz50-MIB", "netBotzTrapSeverity"),
        ("NetBotz50-MIB", "netBotzTrapSensorValue"),
        ("NetBotz50-MIB", "netBotzTrapSensorValueInt"),
        ("NetBotz50-MIB", "netBotzTrapSensorValueFraction"))
)
if mibBuilder.loadTexts:
    netBotzLogonErrorResolved.setStatus(
        "current"
    )

netBotzRmtLinkErrorResolved = NotificationType(
    (1, 3, 6, 1, 4, 1, 52674, 500, 10, 2, 0, 113)
)
netBotzRmtLinkErrorResolved.setObjects(
      *(("NetBotz50-MIB", "netBotzTrapErrorID"),
        ("NetBotz50-MIB", "netBotzTrapErrorType"),
        ("NetBotz50-MIB", "netBotzTrapErrorTypeLabel"),
        ("NetBotz50-MIB", "netBotzTrapSensorID"),
        ("NetBotz50-MIB", "netBotzTrapSensorLabel"),
        ("NetBotz50-MIB", "netBotzTrapContainerID"),
        ("NetBotz50-MIB", "netBotzTrapContainerLabel"),
        ("NetBotz50-MIB", "netBotzTrapPortID"),
        ("NetBotz50-MIB", "netBotzTrapPortLabel"),
        ("NetBotz50-MIB", "netBotzTrapStartTime"),
        ("NetBotz50-MIB", "netBotzTrapNotifyTime"),
        ("NetBotz50-MIB", "netBotzTrapResolveTime"),
        ("NetBotz50-MIB", "netBotzTrapSeverity"),
        ("NetBotz50-MIB", "netBotzTrapSensorValue"),
        ("NetBotz50-MIB", "netBotzTrapSensorValueInt"),
        ("NetBotz50-MIB", "netBotzTrapSensorValueFraction"))
)
if mibBuilder.loadTexts:
    netBotzRmtLinkErrorResolved.setStatus(
        "current"
    )

netBotzSensorPodUnplugged = NotificationType(
    (1, 3, 6, 1, 4, 1, 52674, 500, 10, 2, 1, 0, 7)
)
netBotzSensorPodUnplugged.setObjects(
      *(("NetBotz50-MIB", "netBotzTrapErrorID"),
        ("NetBotz50-MIB", "netBotzTrapErrorType"),
        ("NetBotz50-MIB", "netBotzTrapErrorTypeLabel"),
        ("NetBotz50-MIB", "netBotzTrapSensorID"),
        ("NetBotz50-MIB", "netBotzTrapSensorLabel"),
        ("NetBotz50-MIB", "netBotzTrapContainerID"),
        ("NetBotz50-MIB", "netBotzTrapContainerLabel"),
        ("NetBotz50-MIB", "netBotzTrapPortID"),
        ("NetBotz50-MIB", "netBotzTrapPortLabel"),
        ("NetBotz50-MIB", "netBotzTrapStartTime"),
        ("NetBotz50-MIB", "netBotzTrapNotifyTime"),
        ("NetBotz50-MIB", "netBotzTrapResolveTime"),
        ("NetBotz50-MIB", "netBotzTrapSeverity"),
        ("NetBotz50-MIB", "netBotzTrapSensorValue"),
        ("NetBotz50-MIB", "netBotzTrapSensorValueInt"),
        ("NetBotz50-MIB", "netBotzTrapSensorValueFraction"))
)
if mibBuilder.loadTexts:
    netBotzSensorPodUnplugged.setStatus(
        "current"
    )

netBotzSensorPodReplugged = NotificationType(
    (1, 3, 6, 1, 4, 1, 52674, 500, 10, 2, 1, 0, 107)
)
netBotzSensorPodReplugged.setObjects(
      *(("NetBotz50-MIB", "netBotzTrapErrorID"),
        ("NetBotz50-MIB", "netBotzTrapErrorType"),
        ("NetBotz50-MIB", "netBotzTrapErrorTypeLabel"),
        ("NetBotz50-MIB", "netBotzTrapSensorID"),
        ("NetBotz50-MIB", "netBotzTrapSensorLabel"),
        ("NetBotz50-MIB", "netBotzTrapContainerID"),
        ("NetBotz50-MIB", "netBotzTrapContainerLabel"),
        ("NetBotz50-MIB", "netBotzTrapPortID"),
        ("NetBotz50-MIB", "netBotzTrapPortLabel"),
        ("NetBotz50-MIB", "netBotzTrapStartTime"),
        ("NetBotz50-MIB", "netBotzTrapNotifyTime"),
        ("NetBotz50-MIB", "netBotzTrapResolveTime"),
        ("NetBotz50-MIB", "netBotzTrapSeverity"),
        ("NetBotz50-MIB", "netBotzTrapSensorValue"),
        ("NetBotz50-MIB", "netBotzTrapSensorValueInt"),
        ("NetBotz50-MIB", "netBotzTrapSensorValueFraction"))
)
if mibBuilder.loadTexts:
    netBotzSensorPodReplugged.setStatus(
        "current"
    )

netBotzCameraUnplugged = NotificationType(
    (1, 3, 6, 1, 4, 1, 52674, 500, 10, 2, 2, 0, 7)
)
netBotzCameraUnplugged.setObjects(
      *(("NetBotz50-MIB", "netBotzTrapErrorID"),
        ("NetBotz50-MIB", "netBotzTrapErrorType"),
        ("NetBotz50-MIB", "netBotzTrapErrorTypeLabel"),
        ("NetBotz50-MIB", "netBotzTrapContainerID"),
        ("NetBotz50-MIB", "netBotzTrapContainerLabel"),
        ("NetBotz50-MIB", "netBotzTrapPortID"),
        ("NetBotz50-MIB", "netBotzTrapPortLabel"),
        ("NetBotz50-MIB", "netBotzTrapStartTime"),
        ("NetBotz50-MIB", "netBotzTrapNotifyTime"),
        ("NetBotz50-MIB", "netBotzTrapResolveTime"),
        ("NetBotz50-MIB", "netBotzTrapSeverity"))
)
if mibBuilder.loadTexts:
    netBotzCameraUnplugged.setStatus(
        "current"
    )

netBotzCameraReplugged = NotificationType(
    (1, 3, 6, 1, 4, 1, 52674, 500, 10, 2, 2, 0, 107)
)
netBotzCameraReplugged.setObjects(
      *(("NetBotz50-MIB", "netBotzTrapErrorID"),
        ("NetBotz50-MIB", "netBotzTrapErrorType"),
        ("NetBotz50-MIB", "netBotzTrapErrorTypeLabel"),
        ("NetBotz50-MIB", "netBotzTrapContainerID"),
        ("NetBotz50-MIB", "netBotzTrapContainerLabel"),
        ("NetBotz50-MIB", "netBotzTrapPortID"),
        ("NetBotz50-MIB", "netBotzTrapPortLabel"),
        ("NetBotz50-MIB", "netBotzTrapStartTime"),
        ("NetBotz50-MIB", "netBotzTrapNotifyTime"),
        ("NetBotz50-MIB", "netBotzTrapResolveTime"),
        ("NetBotz50-MIB", "netBotzTrapSeverity"))
)
if mibBuilder.loadTexts:
    netBotzCameraReplugged.setStatus(
        "current"
    )

netBotzFourToTwentymAPodError = NotificationType(
    (1, 3, 6, 1, 4, 1, 52674, 500, 10, 2, 3, 0, 1)
)
netBotzFourToTwentymAPodError.setObjects(
      *(("NetBotz50-MIB", "netBotzTrapErrorID"),
        ("NetBotz50-MIB", "netBotzTrapErrorType"),
        ("NetBotz50-MIB", "netBotzTrapErrorTypeLabel"),
        ("NetBotz50-MIB", "netBotzTrapSensorID"),
        ("NetBotz50-MIB", "netBotzTrapSensorLabel"),
        ("NetBotz50-MIB", "netBotzTrapContainerID"),
        ("NetBotz50-MIB", "netBotzTrapContainerLabel"),
        ("NetBotz50-MIB", "netBotzTrapPortID"),
        ("NetBotz50-MIB", "netBotzTrapPortLabel"),
        ("NetBotz50-MIB", "netBotzTrapStartTime"),
        ("NetBotz50-MIB", "netBotzTrapNotifyTime"),
        ("NetBotz50-MIB", "netBotzTrapResolveTime"),
        ("NetBotz50-MIB", "netBotzTrapSeverity"),
        ("NetBotz50-MIB", "netBotzTrapSensorValue"),
        ("NetBotz50-MIB", "netBotzTrapSensorValueInt"),
        ("NetBotz50-MIB", "netBotzTrapSensorValueFraction"))
)
if mibBuilder.loadTexts:
    netBotzFourToTwentymAPodError.setStatus(
        "current"
    )

netBotzFourToTwentymAPodTooHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 52674, 500, 10, 2, 3, 0, 3)
)
netBotzFourToTwentymAPodTooHigh.setObjects(
      *(("NetBotz50-MIB", "netBotzTrapErrorID"),
        ("NetBotz50-MIB", "netBotzTrapErrorType"),
        ("NetBotz50-MIB", "netBotzTrapErrorTypeLabel"),
        ("NetBotz50-MIB", "netBotzTrapSensorID"),
        ("NetBotz50-MIB", "netBotzTrapSensorLabel"),
        ("NetBotz50-MIB", "netBotzTrapContainerID"),
        ("NetBotz50-MIB", "netBotzTrapContainerLabel"),
        ("NetBotz50-MIB", "netBotzTrapPortID"),
        ("NetBotz50-MIB", "netBotzTrapPortLabel"),
        ("NetBotz50-MIB", "netBotzTrapStartTime"),
        ("NetBotz50-MIB", "netBotzTrapNotifyTime"),
        ("NetBotz50-MIB", "netBotzTrapResolveTime"),
        ("NetBotz50-MIB", "netBotzTrapSeverity"),
        ("NetBotz50-MIB", "netBotzTrapSensorValue"),
        ("NetBotz50-MIB", "netBotzTrapSensorValueInt"),
        ("NetBotz50-MIB", "netBotzTrapSensorValueFraction"))
)
if mibBuilder.loadTexts:
    netBotzFourToTwentymAPodTooHigh.setStatus(
        "current"
    )

netBotzFourToTwentymAPodUnplugged = NotificationType(
    (1, 3, 6, 1, 4, 1, 52674, 500, 10, 2, 3, 0, 7)
)
netBotzFourToTwentymAPodUnplugged.setObjects(
      *(("NetBotz50-MIB", "netBotzTrapErrorID"),
        ("NetBotz50-MIB", "netBotzTrapErrorType"),
        ("NetBotz50-MIB", "netBotzTrapErrorTypeLabel"),
        ("NetBotz50-MIB", "netBotzTrapSensorID"),
        ("NetBotz50-MIB", "netBotzTrapSensorLabel"),
        ("NetBotz50-MIB", "netBotzTrapContainerID"),
        ("NetBotz50-MIB", "netBotzTrapContainerLabel"),
        ("NetBotz50-MIB", "netBotzTrapPortID"),
        ("NetBotz50-MIB", "netBotzTrapPortLabel"),
        ("NetBotz50-MIB", "netBotzTrapStartTime"),
        ("NetBotz50-MIB", "netBotzTrapNotifyTime"),
        ("NetBotz50-MIB", "netBotzTrapResolveTime"),
        ("NetBotz50-MIB", "netBotzTrapSeverity"),
        ("NetBotz50-MIB", "netBotzTrapSensorValue"),
        ("NetBotz50-MIB", "netBotzTrapSensorValueInt"),
        ("NetBotz50-MIB", "netBotzTrapSensorValueFraction"))
)
if mibBuilder.loadTexts:
    netBotzFourToTwentymAPodUnplugged.setStatus(
        "current"
    )

netBotzFourToTwentymAPodTooLow = NotificationType(
    (1, 3, 6, 1, 4, 1, 52674, 500, 10, 2, 3, 0, 10)
)
netBotzFourToTwentymAPodTooLow.setObjects(
      *(("NetBotz50-MIB", "netBotzTrapErrorID"),
        ("NetBotz50-MIB", "netBotzTrapErrorType"),
        ("NetBotz50-MIB", "netBotzTrapErrorTypeLabel"),
        ("NetBotz50-MIB", "netBotzTrapSensorID"),
        ("NetBotz50-MIB", "netBotzTrapSensorLabel"),
        ("NetBotz50-MIB", "netBotzTrapContainerID"),
        ("NetBotz50-MIB", "netBotzTrapContainerLabel"),
        ("NetBotz50-MIB", "netBotzTrapPortID"),
        ("NetBotz50-MIB", "netBotzTrapPortLabel"),
        ("NetBotz50-MIB", "netBotzTrapStartTime"),
        ("NetBotz50-MIB", "netBotzTrapNotifyTime"),
        ("NetBotz50-MIB", "netBotzTrapResolveTime"),
        ("NetBotz50-MIB", "netBotzTrapSeverity"),
        ("NetBotz50-MIB", "netBotzTrapSensorValue"),
        ("NetBotz50-MIB", "netBotzTrapSensorValueInt"),
        ("NetBotz50-MIB", "netBotzTrapSensorValueFraction"))
)
if mibBuilder.loadTexts:
    netBotzFourToTwentymAPodTooLow.setStatus(
        "current"
    )

netBotzFourToTwentymAPodErrorRTN = NotificationType(
    (1, 3, 6, 1, 4, 1, 52674, 500, 10, 2, 3, 0, 101)
)
netBotzFourToTwentymAPodErrorRTN.setObjects(
      *(("NetBotz50-MIB", "netBotzTrapErrorID"),
        ("NetBotz50-MIB", "netBotzTrapErrorType"),
        ("NetBotz50-MIB", "netBotzTrapErrorTypeLabel"),
        ("NetBotz50-MIB", "netBotzTrapSensorID"),
        ("NetBotz50-MIB", "netBotzTrapSensorLabel"),
        ("NetBotz50-MIB", "netBotzTrapContainerID"),
        ("NetBotz50-MIB", "netBotzTrapContainerLabel"),
        ("NetBotz50-MIB", "netBotzTrapPortID"),
        ("NetBotz50-MIB", "netBotzTrapPortLabel"),
        ("NetBotz50-MIB", "netBotzTrapStartTime"),
        ("NetBotz50-MIB", "netBotzTrapNotifyTime"),
        ("NetBotz50-MIB", "netBotzTrapResolveTime"),
        ("NetBotz50-MIB", "netBotzTrapSeverity"),
        ("NetBotz50-MIB", "netBotzTrapSensorValue"),
        ("NetBotz50-MIB", "netBotzTrapSensorValueInt"),
        ("NetBotz50-MIB", "netBotzTrapSensorValueFraction"))
)
if mibBuilder.loadTexts:
    netBotzFourToTwentymAPodErrorRTN.setStatus(
        "current"
    )

netBotzFourToTwentymAPodTooHighRTN = NotificationType(
    (1, 3, 6, 1, 4, 1, 52674, 500, 10, 2, 3, 0, 103)
)
netBotzFourToTwentymAPodTooHighRTN.setObjects(
      *(("NetBotz50-MIB", "netBotzTrapErrorID"),
        ("NetBotz50-MIB", "netBotzTrapErrorType"),
        ("NetBotz50-MIB", "netBotzTrapErrorTypeLabel"),
        ("NetBotz50-MIB", "netBotzTrapSensorID"),
        ("NetBotz50-MIB", "netBotzTrapSensorLabel"),
        ("NetBotz50-MIB", "netBotzTrapContainerID"),
        ("NetBotz50-MIB", "netBotzTrapContainerLabel"),
        ("NetBotz50-MIB", "netBotzTrapPortID"),
        ("NetBotz50-MIB", "netBotzTrapPortLabel"),
        ("NetBotz50-MIB", "netBotzTrapStartTime"),
        ("NetBotz50-MIB", "netBotzTrapNotifyTime"),
        ("NetBotz50-MIB", "netBotzTrapResolveTime"),
        ("NetBotz50-MIB", "netBotzTrapSeverity"),
        ("NetBotz50-MIB", "netBotzTrapSensorValue"),
        ("NetBotz50-MIB", "netBotzTrapSensorValueInt"),
        ("NetBotz50-MIB", "netBotzTrapSensorValueFraction"))
)
if mibBuilder.loadTexts:
    netBotzFourToTwentymAPodTooHighRTN.setStatus(
        "current"
    )

netBotzFourToTwentymAPodReplugged = NotificationType(
    (1, 3, 6, 1, 4, 1, 52674, 500, 10, 2, 3, 0, 107)
)
netBotzFourToTwentymAPodReplugged.setObjects(
      *(("NetBotz50-MIB", "netBotzTrapErrorID"),
        ("NetBotz50-MIB", "netBotzTrapErrorType"),
        ("NetBotz50-MIB", "netBotzTrapErrorTypeLabel"),
        ("NetBotz50-MIB", "netBotzTrapSensorID"),
        ("NetBotz50-MIB", "netBotzTrapSensorLabel"),
        ("NetBotz50-MIB", "netBotzTrapContainerID"),
        ("NetBotz50-MIB", "netBotzTrapContainerLabel"),
        ("NetBotz50-MIB", "netBotzTrapPortID"),
        ("NetBotz50-MIB", "netBotzTrapPortLabel"),
        ("NetBotz50-MIB", "netBotzTrapStartTime"),
        ("NetBotz50-MIB", "netBotzTrapNotifyTime"),
        ("NetBotz50-MIB", "netBotzTrapResolveTime"),
        ("NetBotz50-MIB", "netBotzTrapSeverity"),
        ("NetBotz50-MIB", "netBotzTrapSensorValue"),
        ("NetBotz50-MIB", "netBotzTrapSensorValueInt"),
        ("NetBotz50-MIB", "netBotzTrapSensorValueFraction"))
)
if mibBuilder.loadTexts:
    netBotzFourToTwentymAPodReplugged.setStatus(
        "current"
    )

netBotzFourToTwentymAPodTooLowRTN = NotificationType(
    (1, 3, 6, 1, 4, 1, 52674, 500, 10, 2, 3, 0, 110)
)
netBotzFourToTwentymAPodTooLowRTN.setObjects(
      *(("NetBotz50-MIB", "netBotzTrapErrorID"),
        ("NetBotz50-MIB", "netBotzTrapErrorType"),
        ("NetBotz50-MIB", "netBotzTrapErrorTypeLabel"),
        ("NetBotz50-MIB", "netBotzTrapSensorID"),
        ("NetBotz50-MIB", "netBotzTrapSensorLabel"),
        ("NetBotz50-MIB", "netBotzTrapContainerID"),
        ("NetBotz50-MIB", "netBotzTrapContainerLabel"),
        ("NetBotz50-MIB", "netBotzTrapPortID"),
        ("NetBotz50-MIB", "netBotzTrapPortLabel"),
        ("NetBotz50-MIB", "netBotzTrapStartTime"),
        ("NetBotz50-MIB", "netBotzTrapNotifyTime"),
        ("NetBotz50-MIB", "netBotzTrapResolveTime"),
        ("NetBotz50-MIB", "netBotzTrapSeverity"),
        ("NetBotz50-MIB", "netBotzTrapSensorValue"),
        ("NetBotz50-MIB", "netBotzTrapSensorValueInt"),
        ("NetBotz50-MIB", "netBotzTrapSensorValueFraction"))
)
if mibBuilder.loadTexts:
    netBotzFourToTwentymAPodTooLowRTN.setStatus(
        "current"
    )

netBotzRpduUnplugged = NotificationType(
    (1, 3, 6, 1, 4, 1, 52674, 500, 10, 3, 0, 101)
)
netBotzRpduUnplugged.setObjects(
      *(("NetBotz50-MIB", "netBotzTrapErrorID"),
        ("NetBotz50-MIB", "netBotzTrapErrorType"),
        ("NetBotz50-MIB", "netBotzTrapErrorTypeLabel"),
        ("NetBotz50-MIB", "netBotzTrapContainerID"),
        ("NetBotz50-MIB", "netBotzTrapContainerLabel"),
        ("NetBotz50-MIB", "netBotzTrapPortID"),
        ("NetBotz50-MIB", "netBotzTrapPortLabel"),
        ("NetBotz50-MIB", "netBotzTrapStartTime"),
        ("NetBotz50-MIB", "netBotzTrapNotifyTime"),
        ("NetBotz50-MIB", "netBotzTrapResolveTime"),
        ("NetBotz50-MIB", "netBotzTrapSeverity"))
)
if mibBuilder.loadTexts:
    netBotzRpduUnplugged.setStatus(
        "current"
    )

netBotzRpduReplugged = NotificationType(
    (1, 3, 6, 1, 4, 1, 52674, 500, 10, 3, 0, 102)
)
netBotzRpduReplugged.setObjects(
      *(("NetBotz50-MIB", "netBotzTrapErrorID"),
        ("NetBotz50-MIB", "netBotzTrapErrorType"),
        ("NetBotz50-MIB", "netBotzTrapErrorTypeLabel"),
        ("NetBotz50-MIB", "netBotzTrapContainerID"),
        ("NetBotz50-MIB", "netBotzTrapContainerLabel"),
        ("NetBotz50-MIB", "netBotzTrapPortID"),
        ("NetBotz50-MIB", "netBotzTrapPortLabel"),
        ("NetBotz50-MIB", "netBotzTrapStartTime"),
        ("NetBotz50-MIB", "netBotzTrapNotifyTime"),
        ("NetBotz50-MIB", "netBotzTrapResolveTime"),
        ("NetBotz50-MIB", "netBotzTrapSeverity"))
)
if mibBuilder.loadTexts:
    netBotzRpduReplugged.setStatus(
        "current"
    )

netBotzUpsUnplugged = NotificationType(
    (1, 3, 6, 1, 4, 1, 52674, 500, 10, 4, 0, 103)
)
netBotzUpsUnplugged.setObjects(
      *(("NetBotz50-MIB", "netBotzTrapErrorID"),
        ("NetBotz50-MIB", "netBotzTrapErrorType"),
        ("NetBotz50-MIB", "netBotzTrapErrorTypeLabel"),
        ("NetBotz50-MIB", "netBotzTrapContainerID"),
        ("NetBotz50-MIB", "netBotzTrapContainerLabel"),
        ("NetBotz50-MIB", "netBotzTrapPortID"),
        ("NetBotz50-MIB", "netBotzTrapPortLabel"),
        ("NetBotz50-MIB", "netBotzTrapStartTime"),
        ("NetBotz50-MIB", "netBotzTrapNotifyTime"),
        ("NetBotz50-MIB", "netBotzTrapResolveTime"),
        ("NetBotz50-MIB", "netBotzTrapSeverity"))
)
if mibBuilder.loadTexts:
    netBotzUpsUnplugged.setStatus(
        "current"
    )

netBotzUpsReplugged = NotificationType(
    (1, 3, 6, 1, 4, 1, 52674, 500, 10, 4, 0, 104)
)
netBotzUpsReplugged.setObjects(
      *(("NetBotz50-MIB", "netBotzTrapErrorID"),
        ("NetBotz50-MIB", "netBotzTrapErrorType"),
        ("NetBotz50-MIB", "netBotzTrapErrorTypeLabel"),
        ("NetBotz50-MIB", "netBotzTrapContainerID"),
        ("NetBotz50-MIB", "netBotzTrapContainerLabel"),
        ("NetBotz50-MIB", "netBotzTrapPortID"),
        ("NetBotz50-MIB", "netBotzTrapPortLabel"),
        ("NetBotz50-MIB", "netBotzTrapStartTime"),
        ("NetBotz50-MIB", "netBotzTrapNotifyTime"),
        ("NetBotz50-MIB", "netBotzTrapResolveTime"),
        ("NetBotz50-MIB", "netBotzTrapSeverity"))
)
if mibBuilder.loadTexts:
    netBotzUpsReplugged.setStatus(
        "current"
    )

netBotzGenericNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 52674, 500, 10, 5, 0, 1)
)
netBotzGenericNotification.setObjects(
      *(("NetBotz50-MIB", "netBotzTrapErrorID"),
        ("NetBotz50-MIB", "netBotzTrapErrorType"),
        ("NetBotz50-MIB", "netBotzTrapErrorTypeLabel"),
        ("NetBotz50-MIB", "netBotzTrapContainerID"),
        ("NetBotz50-MIB", "netBotzTrapContainerLabel"),
        ("NetBotz50-MIB", "netBotzTrapPortID"),
        ("NetBotz50-MIB", "netBotzTrapPortLabel"),
        ("NetBotz50-MIB", "netBotzTrapStartTime"),
        ("NetBotz50-MIB", "netBotzTrapNotifyTime"),
        ("NetBotz50-MIB", "netBotzTrapResolveTime"),
        ("NetBotz50-MIB", "netBotzTrapSeverity"))
)
if mibBuilder.loadTexts:
    netBotzGenericNotification.setStatus(
        "current"
    )


# Notifications groups

netbotzNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 52674, 500, 30, 2)
)
netbotzNotificationGroup.setObjects(
      *(("NetBotz50-MIB", "netBotzAirFlowTooHigh"),
        ("NetBotz50-MIB", "netBotzAirFlowTooHighRTN"),
        ("NetBotz50-MIB", "netBotzAirFlowTooLow"),
        ("NetBotz50-MIB", "netBotzAirFlowTooLowRTN"),
        ("NetBotz50-MIB", "netBotzAirFlowUnplugged"),
        ("NetBotz50-MIB", "netBotzAirFlowReplugged"),
        ("NetBotz50-MIB", "netBotzAirFlowError"),
        ("NetBotz50-MIB", "netBotzAirFlowErrorRTN"),
        ("NetBotz50-MIB", "netBotzAmpDetectTooHigh"),
        ("NetBotz50-MIB", "netBotzAmpDetectTooHighRTN"),
        ("NetBotz50-MIB", "netBotzAmpDetectTooLow"),
        ("NetBotz50-MIB", "netBotzAmpDetectTooLowRTN"),
        ("NetBotz50-MIB", "netBotzAmpDetectUnplugged"),
        ("NetBotz50-MIB", "netBotzAmpDetectReplugged"),
        ("NetBotz50-MIB", "netBotzAmpDetectError"),
        ("NetBotz50-MIB", "netBotzAmpDetectErrorRTN"),
        ("NetBotz50-MIB", "netBotzFourToTwentymAPodUnplugged"),
        ("NetBotz50-MIB", "netBotzFourToTwentymAPodReplugged"),
        ("NetBotz50-MIB", "netBotzFourToTwentymAPodError"),
        ("NetBotz50-MIB", "netBotzFourToTwentymAPodErrorRTN"),
        ("NetBotz50-MIB", "netBotzFourToTwentymAPodTooLow"),
        ("NetBotz50-MIB", "netBotzFourToTwentymAPodTooLowRTN"),
        ("NetBotz50-MIB", "netBotzFourToTwentymAPodTooHigh"),
        ("NetBotz50-MIB", "netBotzFourToTwentymAPodTooHighRTN"),
        ("NetBotz50-MIB", "netBotzDewPointTooHigh"),
        ("NetBotz50-MIB", "netBotzDewPointTooHighRTN"),
        ("NetBotz50-MIB", "netBotzDewPointTooLow"),
        ("NetBotz50-MIB", "netBotzDewPointTooLowRTN"),
        ("NetBotz50-MIB", "netBotzDewPointUnplugged"),
        ("NetBotz50-MIB", "netBotzDewPointReplugged"),
        ("NetBotz50-MIB", "netBotzDewPointError"),
        ("NetBotz50-MIB", "netBotzDewPointErrorRTN"),
        ("NetBotz50-MIB", "netBotzDryContactUnplugged"),
        ("NetBotz50-MIB", "netBotzDryContactReplugged"),
        ("NetBotz50-MIB", "netBotzDryContactError"),
        ("NetBotz50-MIB", "netBotzDryContactErrorRTN"),
        ("NetBotz50-MIB", "netBotzDryContactValueError"),
        ("NetBotz50-MIB", "netBotzDryContactValueErrorRTN"),
        ("NetBotz50-MIB", "netBotzCameraMotionSensorUnplugged"),
        ("NetBotz50-MIB", "netBotzCameraMotionSensorReplugged"),
        ("NetBotz50-MIB", "netBotzCameraMotionSensorError"),
        ("NetBotz50-MIB", "netBotzCameraMotionSensorErrorRTN"),
        ("NetBotz50-MIB", "netBotzCameraMotionSensorValueError"),
        ("NetBotz50-MIB", "netBotzCameraMotionSensorValueErrorRTN"),
        ("NetBotz50-MIB", "netBotzDoorSensorUnplugged"),
        ("NetBotz50-MIB", "netBotzDoorSensorReplugged"),
        ("NetBotz50-MIB", "netBotzDoorSensorError"),
        ("NetBotz50-MIB", "netBotzDoorSensorErrorRTN"),
        ("NetBotz50-MIB", "netBotzDoorSensorValueError"),
        ("NetBotz50-MIB", "netBotzDoorSensorValueErrorRTN"),
        ("NetBotz50-MIB", "netBotzCameraUnplugged"),
        ("NetBotz50-MIB", "netBotzCameraReplugged"),
        ("NetBotz50-MIB", "netBotzHumidityTooHigh"),
        ("NetBotz50-MIB", "netBotzHumidityTooHighRTN"),
        ("NetBotz50-MIB", "netBotzHumidityTooLow"),
        ("NetBotz50-MIB", "netBotzHumidityTooLowRTN"),
        ("NetBotz50-MIB", "netBotzHumidityUnplugged"),
        ("NetBotz50-MIB", "netBotzHumidityReplugged"),
        ("NetBotz50-MIB", "netBotzHumidityError"),
        ("NetBotz50-MIB", "netBotzHumidityErrorRTN"),
        ("NetBotz50-MIB", "netBotzLogonError"),
        ("NetBotz50-MIB", "netBotzLogonErrorResolved"),
        ("NetBotz50-MIB", "netBotzLoopVoltageTooHigh"),
        ("NetBotz50-MIB", "netBotzLoopVoltageTooHighRTN"),
        ("NetBotz50-MIB", "netBotzLoopVoltageTooLow"),
        ("NetBotz50-MIB", "netBotzLoopVoltageTooLowRTN"),
        ("NetBotz50-MIB", "netBotzLoopVoltageUnplugged"),
        ("NetBotz50-MIB", "netBotzLoopVoltageReplugged"),
        ("NetBotz50-MIB", "netBotzLoopVoltageError"),
        ("NetBotz50-MIB", "netBotzLoopVoltageErrorRTN"),
        ("NetBotz50-MIB", "netBotzPodUnplugged"),
        ("NetBotz50-MIB", "netBotzPodReplugged"),
        ("NetBotz50-MIB", "netBotzRmtLinkError"),
        ("NetBotz50-MIB", "netBotzRmtLinkErrorResolved"),
        ("NetBotz50-MIB", "netBotzOutputControlSensorUnplugged"),
        ("NetBotz50-MIB", "netBotzOutputControlSensorReplugged"),
        ("NetBotz50-MIB", "netBotzOutputControlSensorError"),
        ("NetBotz50-MIB", "netBotzOutputControlSensorErrorRTN"),
        ("NetBotz50-MIB", "netBotzOutputControlSensorValueError"),
        ("NetBotz50-MIB", "netBotzOutputControlSensorValueErrorRTN"),
        ("NetBotz50-MIB", "netBotzTempTooHigh"),
        ("NetBotz50-MIB", "netBotzTempTooHighRTN"),
        ("NetBotz50-MIB", "netBotzTempTooLow"),
        ("NetBotz50-MIB", "netBotzTempTooLowRTN"),
        ("NetBotz50-MIB", "netBotzTempUnplugged"),
        ("NetBotz50-MIB", "netBotzTempReplugged"),
        ("NetBotz50-MIB", "netBotzTempError"),
        ("NetBotz50-MIB", "netBotzTempErrorRTN"),
        ("NetBotz50-MIB", "netBotzSensorPodUnplugged"),
        ("NetBotz50-MIB", "netBotzSensorPodReplugged"),
        ("NetBotz50-MIB", "netBotzWirelessStatusSensorUnplugged"),
        ("NetBotz50-MIB", "netBotzWirelessStatusSensorReplugged"),
        ("NetBotz50-MIB", "netBotzWirelessStatusSensorError"),
        ("NetBotz50-MIB", "netBotzWirelessStatusSensorErrorRTN"),
        ("NetBotz50-MIB", "netBotzWirelessStatusSensorValueError"),
        ("NetBotz50-MIB", "netBotzWirelessStatusSensorValueErrorRTN"),
        ("NetBotz50-MIB", "netBotzRopeLeakSensorUnplugged"),
        ("NetBotz50-MIB", "netBotzRopeLeakSensorReplugged"),
        ("NetBotz50-MIB", "netBotzRopeLeakSensorError"),
        ("NetBotz50-MIB", "netBotzRopeLeakSensorErrorRTN"),
        ("NetBotz50-MIB", "netBotzRopeLeakSensorValueError"),
        ("NetBotz50-MIB", "netBotzRopeLeakSensorValueErrorRTN"),
        ("NetBotz50-MIB", "netBotzSpotLeakSensorUnplugged"),
        ("NetBotz50-MIB", "netBotzSpotLeakSensorReplugged"),
        ("NetBotz50-MIB", "netBotzSpotLeakSensorError"),
        ("NetBotz50-MIB", "netBotzSpotLeakSensorErrorRTN"),
        ("NetBotz50-MIB", "netBotzSpotLeakSensorValueError"),
        ("NetBotz50-MIB", "netBotzSpotLeakSensorValueErrorRTN"),
        ("NetBotz50-MIB", "netBotzSmokeSensorUnplugged"),
        ("NetBotz50-MIB", "netBotzSmokeSensorReplugged"),
        ("NetBotz50-MIB", "netBotzSmokeSensorError"),
        ("NetBotz50-MIB", "netBotzSmokeSensorErrorRTN"),
        ("NetBotz50-MIB", "netBotzSmokeSensorValueError"),
        ("NetBotz50-MIB", "netBotzSmokeSensorValueErrorRTN"),
        ("NetBotz50-MIB", "netBotzRSSITooLow"),
        ("NetBotz50-MIB", "netBotzRSSITooLowRTN"),
        ("NetBotz50-MIB", "netBotzRSSISensorValueError"),
        ("NetBotz50-MIB", "netBotzRSSISensorValueErrorRTN"),
        ("NetBotz50-MIB", "netBotzBatterySensorError"),
        ("NetBotz50-MIB", "netBotzBatterySensorErrorRTN"),
        ("NetBotz50-MIB", "netBotzBatterySensorValueError"),
        ("NetBotz50-MIB", "netBotzBatterySensorValueErrorRTN"),
        ("NetBotz50-MIB", "netBotzBatteryTooLow"),
        ("NetBotz50-MIB", "netBotzBatteryTooLowRTN"),
        ("NetBotz50-MIB", "netBotzBeaconUnplugged"),
        ("NetBotz50-MIB", "netBotzBeaconReplugged"),
        ("NetBotz50-MIB", "netBotzBeaconError"),
        ("NetBotz50-MIB", "netBotzBeaconErrorRTN"),
        ("NetBotz50-MIB", "netBotzBeaconValueError"),
        ("NetBotz50-MIB", "netBotzBeaconValueErrorRTN"),
        ("NetBotz50-MIB", "netBotzOutletSensorError"),
        ("NetBotz50-MIB", "netBotzOutletSensorErrorRTN"),
        ("NetBotz50-MIB", "netBotzOutletSensorValueError"),
        ("NetBotz50-MIB", "netBotzOutletSensorValueErrorRTN"),
        ("NetBotz50-MIB", "netBotzVibrationSensorUnplugged"),
        ("NetBotz50-MIB", "netBotzVibrationSensorReplugged"),
        ("NetBotz50-MIB", "netBotzVibrationSensorError"),
        ("NetBotz50-MIB", "netBotzVibrationSensorErrorRTN"),
        ("NetBotz50-MIB", "netBotzVibrationSensorValueError"),
        ("NetBotz50-MIB", "netBotzVibrationSensorValueErrorRTN"),
        ("NetBotz50-MIB", "netBotzDoorSensorForcedEntryError"),
        ("NetBotz50-MIB", "netBotzDoorSensorForcedEntryErrorRTN"),
        ("NetBotz50-MIB", "netBotzRackHandleSensorOpenError"),
        ("NetBotz50-MIB", "netBotzRackHandleSensorOpenErrorRTN"),
        ("NetBotz50-MIB", "netBotzCardReaderLocalAuthorizationError"),
        ("NetBotz50-MIB", "netBotzCardReaderLocalAuthorizationErrorRTN"),
        ("NetBotz50-MIB", "netBotzCardReaderLdapAuthorizationError"),
        ("NetBotz50-MIB", "netBotzCardReaderLdapAuthorizationErrorRTN"),
        ("NetBotz50-MIB", "netBotzCardReaderUnplugged"),
        ("NetBotz50-MIB", "netBotzCardReaderReplugged"),
        ("NetBotz50-MIB", "netBotzCardReaderError"),
        ("NetBotz50-MIB", "netBotzCardReaderErrorRTN"),
        ("NetBotz50-MIB", "netBotzCardReaderValueError"),
        ("NetBotz50-MIB", "netBotzCardReaderValueErrorRTN"),
        ("NetBotz50-MIB", "netBotzRackHandleSensorUnplugged"),
        ("NetBotz50-MIB", "netBotzRackHandleSensorReplugged"),
        ("NetBotz50-MIB", "netBotzRackHandleSensorError"),
        ("NetBotz50-MIB", "netBotzRackHandleSensorErrorRTN"),
        ("NetBotz50-MIB", "netBotzRackHandleSensorValueError"),
        ("NetBotz50-MIB", "netBotzRackHandleSensorValueErrorRTN"),
        ("NetBotz50-MIB", "netBotzLockSensorUnplugged"),
        ("NetBotz50-MIB", "netBotzLockSensorReplugged"),
        ("NetBotz50-MIB", "netBotzLockSensorError"),
        ("NetBotz50-MIB", "netBotzLockSensorErrorRTN"),
        ("NetBotz50-MIB", "netBotzLockSensorValueError"),
        ("NetBotz50-MIB", "netBotzLockSensorValueErrorRTN"),
        ("NetBotz50-MIB", "netBotzRpduUnplugged"),
        ("NetBotz50-MIB", "netBotzRpduReplugged"),
        ("NetBotz50-MIB", "netBotzUpsUnplugged"),
        ("NetBotz50-MIB", "netBotzUpsReplugged"),
        ("NetBotz50-MIB", "netBotzGenericNotification"),
        ("NetBotz50-MIB", "netBotzTestNotification"))
)
if mibBuilder.loadTexts:
    netbotzNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "NetBotz50-MIB",
    **{"OperStatus": OperStatus,
       "ErrorStatus": ErrorStatus,
       "BoolValue": BoolValue,
       "netBotzAPC": netBotzAPC,
       "netBotz5": netBotz5,
       "netBotz5-APC": netBotz5_APC,
       "netBotzEnclosures": netBotzEnclosures,
       "enclosureTable": enclosureTable,
       "enclosureEntry": enclosureEntry,
       "enclosureId": enclosureId,
       "enclosureStatus": enclosureStatus,
       "enclosureErrorStatus": enclosureErrorStatus,
       "enclosureLabel": enclosureLabel,
       "enclosureParentEncId": enclosureParentEncId,
       "enclosureSerialNumber": enclosureSerialNumber,
       "enclosureIndex": enclosureIndex,
       "netBotzSensorCounts": netBotzSensorCounts,
       "alinkSensorCountTable": alinkSensorCountTable,
       "alinkSensorCountEntry": alinkSensorCountEntry,
       "alinkSensorCountId": alinkSensorCountId,
       "alinkSensorCountValue": alinkSensorCountValue,
       "alinkSensorCountLabel": alinkSensorCountLabel,
       "alinkSensorCountEncId": alinkSensorCountEncId,
       "alinkSensorCountValueStr": alinkSensorCountValueStr,
       "alinkSensorCountValueInt": alinkSensorCountValueInt,
       "alinkSensorCountIndex": alinkSensorCountIndex,
       "netBotzPorts": netBotzPorts,
       "otherPortTable": otherPortTable,
       "otherPortEntry": otherPortEntry,
       "otherPortId": otherPortId,
       "otherPortStatus": otherPortStatus,
       "otherPortLabel": otherPortLabel,
       "otherPortEncId": otherPortEncId,
       "otherPortIndex": otherPortIndex,
       "netBotzSensors": netBotzSensors,
       "netBotzNumericSensors": netBotzNumericSensors,
       "tempSensorTable": tempSensorTable,
       "tempSensorEntry": tempSensorEntry,
       "tempSensorId": tempSensorId,
       "tempSensorValue": tempSensorValue,
       "tempSensorErrorStatus": tempSensorErrorStatus,
       "tempSensorLabel": tempSensorLabel,
       "tempSensorEncId": tempSensorEncId,
       "tempSensorPortId": tempSensorPortId,
       "tempSensorValueStr": tempSensorValueStr,
       "tempSensorValueInt": tempSensorValueInt,
       "tempSensorValueIntF": tempSensorValueIntF,
       "tempSensorIndex": tempSensorIndex,
       "humiSensorTable": humiSensorTable,
       "humiSensorEntry": humiSensorEntry,
       "humiSensorId": humiSensorId,
       "humiSensorValue": humiSensorValue,
       "humiSensorErrorStatus": humiSensorErrorStatus,
       "humiSensorLabel": humiSensorLabel,
       "humiSensorEncId": humiSensorEncId,
       "humiSensorPortId": humiSensorPortId,
       "humiSensorValueStr": humiSensorValueStr,
       "humiSensorValueInt": humiSensorValueInt,
       "humiSensorIndex": humiSensorIndex,
       "dewPointSensorTable": dewPointSensorTable,
       "dewPointSensorEntry": dewPointSensorEntry,
       "dewPointSensorId": dewPointSensorId,
       "dewPointSensorValue": dewPointSensorValue,
       "dewPointSensorErrorStatus": dewPointSensorErrorStatus,
       "dewPointSensorLabel": dewPointSensorLabel,
       "dewPointSensorEncId": dewPointSensorEncId,
       "dewPointSensorPortId": dewPointSensorPortId,
       "dewPointSensorValueStr": dewPointSensorValueStr,
       "dewPointSensorValueInt": dewPointSensorValueInt,
       "dewPointSensorValueIntF": dewPointSensorValueIntF,
       "dewPointSensorIndex": dewPointSensorIndex,
       "airFlowSensorTable": airFlowSensorTable,
       "airFlowSensorEntry": airFlowSensorEntry,
       "airFlowSensorId": airFlowSensorId,
       "airFlowSensorValue": airFlowSensorValue,
       "airFlowSensorErrorStatus": airFlowSensorErrorStatus,
       "airFlowSensorLabel": airFlowSensorLabel,
       "airFlowSensorEncId": airFlowSensorEncId,
       "airFlowSensorPortId": airFlowSensorPortId,
       "airFlowSensorValueStr": airFlowSensorValueStr,
       "airFlowSensorValueInt": airFlowSensorValueInt,
       "airFlowSensorIndex": airFlowSensorIndex,
       "ampDetectSensorTable": ampDetectSensorTable,
       "ampDetectSensorEntry": ampDetectSensorEntry,
       "ampDetectSensorId": ampDetectSensorId,
       "ampDetectSensorValue": ampDetectSensorValue,
       "ampDetectSensorErrorStatus": ampDetectSensorErrorStatus,
       "ampDetectSensorLabel": ampDetectSensorLabel,
       "ampDetectSensorEncId": ampDetectSensorEncId,
       "ampDetectSensorPortId": ampDetectSensorPortId,
       "ampDetectSensorValueStr": ampDetectSensorValueStr,
       "ampDetectSensorValueInt": ampDetectSensorValueInt,
       "ampDetectSensorIndex": ampDetectSensorIndex,
       "otherNumericSensorTable": otherNumericSensorTable,
       "otherNumericSensorEntry": otherNumericSensorEntry,
       "otherNumericSensorId": otherNumericSensorId,
       "otherNumericSensorValue": otherNumericSensorValue,
       "otherNumericSensorErrorStatus": otherNumericSensorErrorStatus,
       "otherNumericSensorLabel": otherNumericSensorLabel,
       "otherNumericSensorEncId": otherNumericSensorEncId,
       "otherNumericSensorPortId": otherNumericSensorPortId,
       "otherNumericSensorValueStr": otherNumericSensorValueStr,
       "otherNumericSensorValueInt": otherNumericSensorValueInt,
       "otherNumericSensorUnits": otherNumericSensorUnits,
       "otherNumericSensorValueIntX1000": otherNumericSensorValueIntX1000,
       "otherNumericSensorValueIntX1000000": otherNumericSensorValueIntX1000000,
       "otherNumericSensorIndex": otherNumericSensorIndex,
       "rssiSensorTable": rssiSensorTable,
       "rssiSensorEntry": rssiSensorEntry,
       "rssiSensorId": rssiSensorId,
       "rssiSensorValue": rssiSensorValue,
       "rssiSensorErrorStatus": rssiSensorErrorStatus,
       "rssiSensorLabel": rssiSensorLabel,
       "rssiSensorEncId": rssiSensorEncId,
       "rssiSensorPortId": rssiSensorPortId,
       "rssiSensorValueStr": rssiSensorValueStr,
       "rssiSensorValueInt": rssiSensorValueInt,
       "rssiSensorUnits": rssiSensorUnits,
       "rssiSensorIndex": rssiSensorIndex,
       "currentInputSensorTable": currentInputSensorTable,
       "currentInputSensorEntry": currentInputSensorEntry,
       "currentInputSensorId": currentInputSensorId,
       "currentInputSensorValue": currentInputSensorValue,
       "currentInputSensorErrorStatus": currentInputSensorErrorStatus,
       "currentInputSensorLabel": currentInputSensorLabel,
       "currentInputSensorEncId": currentInputSensorEncId,
       "currentInputSensorPortId": currentInputSensorPortId,
       "currentInputSensorValueStr": currentInputSensorValueStr,
       "currentInputSensorValueInt": currentInputSensorValueInt,
       "currentInputSensorUnits": currentInputSensorUnits,
       "currentInputSensorValueIntX1000": currentInputSensorValueIntX1000,
       "currentInputSensorValueIntX1000000": currentInputSensorValueIntX1000000,
       "currentInputSensorIndex": currentInputSensorIndex,
       "voltageSensorTable": voltageSensorTable,
       "voltageSensorEntry": voltageSensorEntry,
       "voltageSensorId": voltageSensorId,
       "voltageSensorValue": voltageSensorValue,
       "voltageSensorErrorStatus": voltageSensorErrorStatus,
       "voltageSensorLabel": voltageSensorLabel,
       "voltageSensorEncId": voltageSensorEncId,
       "voltageSensorPortId": voltageSensorPortId,
       "voltageSensorValueStr": voltageSensorValueStr,
       "voltageSensorValueInt": voltageSensorValueInt,
       "voltageSensorUnits": voltageSensorUnits,
       "voltageSensorValueIntX1000": voltageSensorValueIntX1000,
       "voltageSensorValueIntX1000000": voltageSensorValueIntX1000000,
       "voltageSensorIndex": voltageSensorIndex,
       "batterySensorTable": batterySensorTable,
       "batterySensorEntry": batterySensorEntry,
       "batterySensorId": batterySensorId,
       "batterySensorValue": batterySensorValue,
       "batterySensorErrorStatus": batterySensorErrorStatus,
       "batterySensorLabel": batterySensorLabel,
       "batterySensorEncId": batterySensorEncId,
       "batterySensorPortId": batterySensorPortId,
       "batterySensorValueStr": batterySensorValueStr,
       "batterySensorValueInt": batterySensorValueInt,
       "batterySensorUnits": batterySensorUnits,
       "batterySensorValueIntX1000": batterySensorValueIntX1000,
       "batterySensorValueIntX1000000": batterySensorValueIntX1000000,
       "batterySensorIndex": batterySensorIndex,
       "netBotzStateSensors": netBotzStateSensors,
       "dryContactSensorTable": dryContactSensorTable,
       "dryContactSensorEntry": dryContactSensorEntry,
       "dryContactSensorId": dryContactSensorId,
       "dryContactSensorValue": dryContactSensorValue,
       "dryContactSensorErrorStatus": dryContactSensorErrorStatus,
       "dryContactSensorLabel": dryContactSensorLabel,
       "dryContactSensorEncId": dryContactSensorEncId,
       "dryContactSensorPortId": dryContactSensorPortId,
       "dryContactSensorValueStr": dryContactSensorValueStr,
       "dryContactSensorIndex": dryContactSensorIndex,
       "doorSwitchSensorTable": doorSwitchSensorTable,
       "doorSwitchSensorEntry": doorSwitchSensorEntry,
       "doorSwitchSensorId": doorSwitchSensorId,
       "doorSwitchSensorValue": doorSwitchSensorValue,
       "doorSwitchSensorErrorStatus": doorSwitchSensorErrorStatus,
       "doorSwitchSensorLabel": doorSwitchSensorLabel,
       "doorSwitchSensorEncId": doorSwitchSensorEncId,
       "doorSwitchSensorPortId": doorSwitchSensorPortId,
       "doorSwitchSensorValueStr": doorSwitchSensorValueStr,
       "doorSwitchSensorIndex": doorSwitchSensorIndex,
       "cameraMotionSensorTable": cameraMotionSensorTable,
       "cameraMotionSensorEntry": cameraMotionSensorEntry,
       "cameraMotionSensorId": cameraMotionSensorId,
       "cameraMotionSensorValue": cameraMotionSensorValue,
       "cameraMotionSensorErrorStatus": cameraMotionSensorErrorStatus,
       "cameraMotionSensorLabel": cameraMotionSensorLabel,
       "cameraMotionSensorEncId": cameraMotionSensorEncId,
       "cameraMotionSensorPortId": cameraMotionSensorPortId,
       "cameraMotionSensorValueStr": cameraMotionSensorValueStr,
       "cameraMotionSensorIndex": cameraMotionSensorIndex,
       "otherStateSensorTable": otherStateSensorTable,
       "otherStateSensorEntry": otherStateSensorEntry,
       "otherStateSensorId": otherStateSensorId,
       "otherStateSensorValue": otherStateSensorValue,
       "otherStateSensorErrorStatus": otherStateSensorErrorStatus,
       "otherStateSensorLabel": otherStateSensorLabel,
       "otherStateSensorEncId": otherStateSensorEncId,
       "otherStateSensorPortId": otherStateSensorPortId,
       "otherStateSensorValueStr": otherStateSensorValueStr,
       "otherStateSensorIndex": otherStateSensorIndex,
       "vibrationSensorTable": vibrationSensorTable,
       "vibrationSensorEntry": vibrationSensorEntry,
       "vibrationSensorId": vibrationSensorId,
       "vibrationSensorValue": vibrationSensorValue,
       "vibrationSensorErrorStatus": vibrationSensorErrorStatus,
       "vibrationSensorLabel": vibrationSensorLabel,
       "vibrationSensorEncId": vibrationSensorEncId,
       "vibrationSensorPortId": vibrationSensorPortId,
       "vibrationSensorValueStr": vibrationSensorValueStr,
       "vibrationSensorIndex": vibrationSensorIndex,
       "smokeSensorTable": smokeSensorTable,
       "smokeSensorEntry": smokeSensorEntry,
       "smokeSensorId": smokeSensorId,
       "smokeSensorValue": smokeSensorValue,
       "smokeSensorErrorStatus": smokeSensorErrorStatus,
       "smokeSensorLabel": smokeSensorLabel,
       "smokeSensorEncId": smokeSensorEncId,
       "smokeSensorPortId": smokeSensorPortId,
       "smokeSensorValueStr": smokeSensorValueStr,
       "smokeSensorIndex": smokeSensorIndex,
       "leakSensorTable": leakSensorTable,
       "leakSensorEntry": leakSensorEntry,
       "leakSensorId": leakSensorId,
       "leakSensorValue": leakSensorValue,
       "leakSensorErrorStatus": leakSensorErrorStatus,
       "leakSensorLabel": leakSensorLabel,
       "leakSensorEncId": leakSensorEncId,
       "leakSensorPortId": leakSensorPortId,
       "leakSensorValueStr": leakSensorValueStr,
       "leakSensorIndex": leakSensorIndex,
       "beaconTable": beaconTable,
       "beaconEntry": beaconEntry,
       "beaconId": beaconId,
       "beaconValue": beaconValue,
       "beaconErrorStatus": beaconErrorStatus,
       "beaconLabel": beaconLabel,
       "beaconEncId": beaconEncId,
       "beaconPortId": beaconPortId,
       "beaconValueStr": beaconValueStr,
       "beaconIndex": beaconIndex,
       "switchedOutletTable": switchedOutletTable,
       "switchedOutletEntry": switchedOutletEntry,
       "switchedOutletId": switchedOutletId,
       "switchedOutletValue": switchedOutletValue,
       "switchedOutletErrorStatus": switchedOutletErrorStatus,
       "switchedOutletLabel": switchedOutletLabel,
       "switchedOutletEncId": switchedOutletEncId,
       "switchedOutletPortId": switchedOutletPortId,
       "switchedOutletValueStr": switchedOutletValueStr,
       "switchedOutletIndex": switchedOutletIndex,
       "doorLockSensorTable": doorLockSensorTable,
       "doorLockSensorEntry": doorLockSensorEntry,
       "doorLockSensorId": doorLockSensorId,
       "doorLockSensorValue": doorLockSensorValue,
       "doorLockSensorErrorStatus": doorLockSensorErrorStatus,
       "doorLockSensorLabel": doorLockSensorLabel,
       "doorLockSensorEncId": doorLockSensorEncId,
       "doorLockSensorPortId": doorLockSensorPortId,
       "doorLockSensorValueStr": doorLockSensorValueStr,
       "doorLockSensorIndex": doorLockSensorIndex,
       "rackHandleSensorTable": rackHandleSensorTable,
       "rackHandleSensorEntry": rackHandleSensorEntry,
       "rackHandleSensorId": rackHandleSensorId,
       "rackHandleSensorValue": rackHandleSensorValue,
       "rackHandleSensorErrorStatus": rackHandleSensorErrorStatus,
       "rackHandleSensorLabel": rackHandleSensorLabel,
       "rackHandleSensorEncId": rackHandleSensorEncId,
       "rackHandleSensorPortId": rackHandleSensorPortId,
       "rackHandleSensorValueStr": rackHandleSensorValueStr,
       "rackHandleSensorIndex": rackHandleSensorIndex,
       "outputRelaySensorTable": outputRelaySensorTable,
       "outputRelaySensorEntry": outputRelaySensorEntry,
       "outputRelaySensorId": outputRelaySensorId,
       "outputRelaySensorValue": outputRelaySensorValue,
       "outputRelaySensorErrorStatus": outputRelaySensorErrorStatus,
       "outputRelaySensorLabel": outputRelaySensorLabel,
       "outputRelaySensorEncId": outputRelaySensorEncId,
       "outputRelaySensorPortId": outputRelaySensorPortId,
       "outputRelaySensorValueStr": outputRelaySensorValueStr,
       "outputRelaySensorIndex": outputRelaySensorIndex,
       "netBotzErrors": netBotzErrors,
       "errorCondTable": errorCondTable,
       "errorCondEntry": errorCondEntry,
       "errorCondId": errorCondId,
       "errorCondSeverity": errorCondSeverity,
       "errorCondTypeId": errorCondTypeId,
       "errorCondStartTime": errorCondStartTime,
       "errorCondStartTimeStr": errorCondStartTimeStr,
       "errorCondResolved": errorCondResolved,
       "errorCondResolvedTime": errorCondResolvedTime,
       "errorCondResolvedTimeStr": errorCondResolvedTimeStr,
       "errorCondEncId": errorCondEncId,
       "errorCondPortId": errorCondPortId,
       "errorCondSensorId": errorCondSensorId,
       "errorCondIndex": errorCondIndex,
       "netBotzCameras": netBotzCameras,
       "cameraTable": cameraTable,
       "cameraEntry": cameraEntry,
       "cameraId": cameraId,
       "cameraVendor": cameraVendor,
       "cameraModel": cameraModel,
       "cameraConnectionStatus": cameraConnectionStatus,
       "cameraErrorStatus": cameraErrorStatus,
       "cameraLabel": cameraLabel,
       "cameraAddress": cameraAddress,
       "cameraIndex": cameraIndex,
       "netBotzFirmware": netBotzFirmware,
       "firmwareTable": firmwareTable,
       "firmwareEntry": firmwareEntry,
       "firmwareDescription": firmwareDescription,
       "firmwareVersion": firmwareVersion,
       "firmwareIndex": firmwareIndex,
       "netBotzTraps": netBotzTraps,
       "netBotzSensorTraps": netBotzSensorTraps,
       "netBotzTempSensorTraps": netBotzTempSensorTraps,
       "netBotzTempSensorPrefix": netBotzTempSensorPrefix,
       "netBotzTempError": netBotzTempError,
       "netBotzTempTooHigh": netBotzTempTooHigh,
       "netBotzTempTooLow": netBotzTempTooLow,
       "netBotzTempUnplugged": netBotzTempUnplugged,
       "netBotzTempErrorRTN": netBotzTempErrorRTN,
       "netBotzTempTooHighRTN": netBotzTempTooHighRTN,
       "netBotzTempTooLowRTN": netBotzTempTooLowRTN,
       "netBotzTempReplugged": netBotzTempReplugged,
       "netBotzHumiditySensorTraps": netBotzHumiditySensorTraps,
       "netBotzHumiditySensorPrefix": netBotzHumiditySensorPrefix,
       "netBotzHumidityError": netBotzHumidityError,
       "netBotzHumidityTooHigh": netBotzHumidityTooHigh,
       "netBotzHumidityTooLow": netBotzHumidityTooLow,
       "netBotzHumidityUnplugged": netBotzHumidityUnplugged,
       "netBotzHumidityErrorRTN": netBotzHumidityErrorRTN,
       "netBotzHumidityTooHighRTN": netBotzHumidityTooHighRTN,
       "netBotzHumidityTooLowRTN": netBotzHumidityTooLowRTN,
       "netBotzHumidityReplugged": netBotzHumidityReplugged,
       "netBotzDewPointSensorTraps": netBotzDewPointSensorTraps,
       "netBotzDewPointSensorPrefix": netBotzDewPointSensorPrefix,
       "netBotzDewPointError": netBotzDewPointError,
       "netBotzDewPointTooHigh": netBotzDewPointTooHigh,
       "netBotzDewPointTooLow": netBotzDewPointTooLow,
       "netBotzDewPointUnplugged": netBotzDewPointUnplugged,
       "netBotzDewPointErrorRTN": netBotzDewPointErrorRTN,
       "netBotzDewPointTooHighRTN": netBotzDewPointTooHighRTN,
       "netBotzDewPointTooLowRTN": netBotzDewPointTooLowRTN,
       "netBotzDewPointReplugged": netBotzDewPointReplugged,
       "netBotzAirFlowSensorTraps": netBotzAirFlowSensorTraps,
       "netBotzAirFlowSensorPrefix": netBotzAirFlowSensorPrefix,
       "netBotzAirFlowError": netBotzAirFlowError,
       "netBotzAirFlowTooHigh": netBotzAirFlowTooHigh,
       "netBotzAirFlowTooLow": netBotzAirFlowTooLow,
       "netBotzAirFlowUnplugged": netBotzAirFlowUnplugged,
       "netBotzAirFlowErrorRTN": netBotzAirFlowErrorRTN,
       "netBotzAirFlowTooHighRTN": netBotzAirFlowTooHighRTN,
       "netBotzAirFlowTooLowRTN": netBotzAirFlowTooLowRTN,
       "netBotzAirFlowReplugged": netBotzAirFlowReplugged,
       "netBotzAmpDetectSensorTraps": netBotzAmpDetectSensorTraps,
       "netBotzAmpDetectSensorPrefix": netBotzAmpDetectSensorPrefix,
       "netBotzAmpDetectError": netBotzAmpDetectError,
       "netBotzAmpDetectTooHigh": netBotzAmpDetectTooHigh,
       "netBotzAmpDetectTooLow": netBotzAmpDetectTooLow,
       "netBotzAmpDetectUnplugged": netBotzAmpDetectUnplugged,
       "netBotzAmpDetectErrorRTN": netBotzAmpDetectErrorRTN,
       "netBotzAmpDetectTooHighRTN": netBotzAmpDetectTooHighRTN,
       "netBotzAmpDetectTooLowRTN": netBotzAmpDetectTooLowRTN,
       "netBotzAmpDetectReplugged": netBotzAmpDetectReplugged,
       "netBotzDryContactSensorTraps": netBotzDryContactSensorTraps,
       "netBotzDryContactSensorPrefix": netBotzDryContactSensorPrefix,
       "netBotzDryContactError": netBotzDryContactError,
       "netBotzDryContactUnplugged": netBotzDryContactUnplugged,
       "netBotzDryContactValueError": netBotzDryContactValueError,
       "netBotzDryContactErrorRTN": netBotzDryContactErrorRTN,
       "netBotzDryContactReplugged": netBotzDryContactReplugged,
       "netBotzDryContactValueErrorRTN": netBotzDryContactValueErrorRTN,
       "netBotzCameraMotionSensorTraps": netBotzCameraMotionSensorTraps,
       "netBotzCameraMotionSensorPrefix": netBotzCameraMotionSensorPrefix,
       "netBotzCameraMotionSensorError": netBotzCameraMotionSensorError,
       "netBotzCameraMotionSensorUnplugged": netBotzCameraMotionSensorUnplugged,
       "netBotzCameraMotionSensorValueError": netBotzCameraMotionSensorValueError,
       "netBotzCameraMotionSensorErrorRTN": netBotzCameraMotionSensorErrorRTN,
       "netBotzCameraMotionSensorReplugged": netBotzCameraMotionSensorReplugged,
       "netBotzCameraMotionSensorValueErrorRTN": netBotzCameraMotionSensorValueErrorRTN,
       "netBotzDoorSensorTraps": netBotzDoorSensorTraps,
       "netBotzDoorSensorPrefix": netBotzDoorSensorPrefix,
       "netBotzDoorSensorError": netBotzDoorSensorError,
       "netBotzDoorSensorUnplugged": netBotzDoorSensorUnplugged,
       "netBotzDoorSensorValueError": netBotzDoorSensorValueError,
       "netBotzDoorSensorErrorRTN": netBotzDoorSensorErrorRTN,
       "netBotzDoorSensorReplugged": netBotzDoorSensorReplugged,
       "netBotzDoorSensorValueErrorRTN": netBotzDoorSensorValueErrorRTN,
       "netBotzWirelessStatusSensorTraps": netBotzWirelessStatusSensorTraps,
       "netBotzWirelessStatusSensorPrefix": netBotzWirelessStatusSensorPrefix,
       "netBotzWirelessStatusSensorError": netBotzWirelessStatusSensorError,
       "netBotzWirelessStatusSensorUnplugged": netBotzWirelessStatusSensorUnplugged,
       "netBotzWirelessStatusSensorValueError": netBotzWirelessStatusSensorValueError,
       "netBotzWirelessStatusSensorErrorRTN": netBotzWirelessStatusSensorErrorRTN,
       "netBotzWirelessStatusSensorReplugged": netBotzWirelessStatusSensorReplugged,
       "netBotzWirelessStatusSensorValueErrorRTN": netBotzWirelessStatusSensorValueErrorRTN,
       "netBotzOutputControlSensorTraps": netBotzOutputControlSensorTraps,
       "netBotzOutputControlSensorPrefix": netBotzOutputControlSensorPrefix,
       "netBotzOutputControlSensorError": netBotzOutputControlSensorError,
       "netBotzOutputControlSensorUnplugged": netBotzOutputControlSensorUnplugged,
       "netBotzOutputControlSensorValueError": netBotzOutputControlSensorValueError,
       "netBotzOutputControlSensorErrorRTN": netBotzOutputControlSensorErrorRTN,
       "netBotzOutputControlSensorReplugged": netBotzOutputControlSensorReplugged,
       "netBotzOutputControlSensorValueErrorRTN": netBotzOutputControlSensorValueErrorRTN,
       "netBotzLoopVoltageSensorTraps": netBotzLoopVoltageSensorTraps,
       "netBotzLoopVoltageSensorPrefix": netBotzLoopVoltageSensorPrefix,
       "netBotzLoopVoltageError": netBotzLoopVoltageError,
       "netBotzLoopVoltageTooHigh": netBotzLoopVoltageTooHigh,
       "netBotzLoopVoltageTooLow": netBotzLoopVoltageTooLow,
       "netBotzLoopVoltageUnplugged": netBotzLoopVoltageUnplugged,
       "netBotzLoopVoltageErrorRTN": netBotzLoopVoltageErrorRTN,
       "netBotzLoopVoltageTooHighRTN": netBotzLoopVoltageTooHighRTN,
       "netBotzLoopVoltageTooLowRTN": netBotzLoopVoltageTooLowRTN,
       "netBotzLoopVoltageReplugged": netBotzLoopVoltageReplugged,
       "netBotzSpotLeakSensorTraps": netBotzSpotLeakSensorTraps,
       "netBotzSpotLeakSensorPrefix": netBotzSpotLeakSensorPrefix,
       "netBotzSpotLeakSensorError": netBotzSpotLeakSensorError,
       "netBotzSpotLeakSensorUnplugged": netBotzSpotLeakSensorUnplugged,
       "netBotzSpotLeakSensorValueError": netBotzSpotLeakSensorValueError,
       "netBotzSpotLeakSensorErrorRTN": netBotzSpotLeakSensorErrorRTN,
       "netBotzSpotLeakSensorReplugged": netBotzSpotLeakSensorReplugged,
       "netBotzSpotLeakSensorValueErrorRTN": netBotzSpotLeakSensorValueErrorRTN,
       "netBotzRopeLeakSensorTraps": netBotzRopeLeakSensorTraps,
       "netBotzRopeLeakSensorPrefix": netBotzRopeLeakSensorPrefix,
       "netBotzRopeLeakSensorError": netBotzRopeLeakSensorError,
       "netBotzRopeLeakSensorUnplugged": netBotzRopeLeakSensorUnplugged,
       "netBotzRopeLeakSensorValueError": netBotzRopeLeakSensorValueError,
       "netBotzRopeLeakSensorErrorRTN": netBotzRopeLeakSensorErrorRTN,
       "netBotzRopeLeakSensorReplugged": netBotzRopeLeakSensorReplugged,
       "netBotzRopeLeakSensorValueErrorRTN": netBotzRopeLeakSensorValueErrorRTN,
       "netBotzRSSISensorTraps": netBotzRSSISensorTraps,
       "netBotzRSSISensorPrefix": netBotzRSSISensorPrefix,
       "netBotzRSSITooLow": netBotzRSSITooLow,
       "netBotzRSSISensorValueError": netBotzRSSISensorValueError,
       "netBotzRSSITooLowRTN": netBotzRSSITooLowRTN,
       "netBotzRSSISensorValueErrorRTN": netBotzRSSISensorValueErrorRTN,
       "netBotzBatterySensorTraps": netBotzBatterySensorTraps,
       "netBotzBatterySensorPrefix": netBotzBatterySensorPrefix,
       "netBotzBatterySensorError": netBotzBatterySensorError,
       "netBotzBatteryTooLow": netBotzBatteryTooLow,
       "netBotzBatterySensorValueError": netBotzBatterySensorValueError,
       "netBotzBatterySensorErrorRTN": netBotzBatterySensorErrorRTN,
       "netBotzBatteryTooLowRTN": netBotzBatteryTooLowRTN,
       "netBotzBatterySensorValueErrorRTN": netBotzBatterySensorValueErrorRTN,
       "netBotzOutletSensorTraps": netBotzOutletSensorTraps,
       "netBotzOutletSensorPrefix": netBotzOutletSensorPrefix,
       "netBotzOutletSensorError": netBotzOutletSensorError,
       "netBotzOutletSensorValueError": netBotzOutletSensorValueError,
       "netBotzOutletSensorErrorRTN": netBotzOutletSensorErrorRTN,
       "netBotzOutletSensorValueErrorRTN": netBotzOutletSensorValueErrorRTN,
       "netBotzBeaconTraps": netBotzBeaconTraps,
       "netBotzBeaconPrefix": netBotzBeaconPrefix,
       "netBotzBeaconError": netBotzBeaconError,
       "netBotzBeaconUnplugged": netBotzBeaconUnplugged,
       "netBotzBeaconValueError": netBotzBeaconValueError,
       "netBotzBeaconErrorRTN": netBotzBeaconErrorRTN,
       "netBotzBeaconReplugged": netBotzBeaconReplugged,
       "netBotzBeaconValueErrorRTN": netBotzBeaconValueErrorRTN,
       "netBotzSmokeSensorTraps": netBotzSmokeSensorTraps,
       "netBotzSmokeSensorPrefix": netBotzSmokeSensorPrefix,
       "netBotzSmokeSensorError": netBotzSmokeSensorError,
       "netBotzSmokeSensorUnplugged": netBotzSmokeSensorUnplugged,
       "netBotzSmokeSensorValueError": netBotzSmokeSensorValueError,
       "netBotzSmokeSensorErrorRTN": netBotzSmokeSensorErrorRTN,
       "netBotzSmokeSensorReplugged": netBotzSmokeSensorReplugged,
       "netBotzSmokeSensorValueErrorRTN": netBotzSmokeSensorValueErrorRTN,
       "netBotzVibrationSensorTraps": netBotzVibrationSensorTraps,
       "netBotzVibrationSensorPrefix": netBotzVibrationSensorPrefix,
       "netBotzVibrationSensorError": netBotzVibrationSensorError,
       "netBotzVibrationSensorUnplugged": netBotzVibrationSensorUnplugged,
       "netBotzVibrationSensorValueError": netBotzVibrationSensorValueError,
       "netBotzVibrationSensorErrorRTN": netBotzVibrationSensorErrorRTN,
       "netBotzVibrationSensorReplugged": netBotzVibrationSensorReplugged,
       "netBotzVibrationSensorValueErrorRTN": netBotzVibrationSensorValueErrorRTN,
       "netBotzRackAccessTraps": netBotzRackAccessTraps,
       "netBotzRackAccessPrefix": netBotzRackAccessPrefix,
       "netBotzDoorSensorForcedEntryError": netBotzDoorSensorForcedEntryError,
       "netBotzRackHandleSensorOpenError": netBotzRackHandleSensorOpenError,
       "netBotzCardReaderLocalAuthorizationError": netBotzCardReaderLocalAuthorizationError,
       "netBotzCardReaderLdapAuthorizationError": netBotzCardReaderLdapAuthorizationError,
       "netBotzCardReaderUnplugged": netBotzCardReaderUnplugged,
       "netBotzCardReaderReplugged": netBotzCardReaderReplugged,
       "netBotzCardReaderError": netBotzCardReaderError,
       "netBotzCardReaderErrorRTN": netBotzCardReaderErrorRTN,
       "netBotzCardReaderValueError": netBotzCardReaderValueError,
       "netBotzCardReaderValueErrorRTN": netBotzCardReaderValueErrorRTN,
       "netBotzRackHandleSensorUnplugged": netBotzRackHandleSensorUnplugged,
       "netBotzRackHandleSensorReplugged": netBotzRackHandleSensorReplugged,
       "netBotzRackHandleSensorError": netBotzRackHandleSensorError,
       "netBotzRackHandleSensorErrorRTN": netBotzRackHandleSensorErrorRTN,
       "netBotzRackHandleSensorValueError": netBotzRackHandleSensorValueError,
       "netBotzRackHandleSensorValueErrorRTN": netBotzRackHandleSensorValueErrorRTN,
       "netBotzLockSensorUnplugged": netBotzLockSensorUnplugged,
       "netBotzLockSensorReplugged": netBotzLockSensorReplugged,
       "netBotzLockSensorError": netBotzLockSensorError,
       "netBotzLockSensorErrorRTN": netBotzLockSensorErrorRTN,
       "netBotzLockSensorValueError": netBotzLockSensorValueError,
       "netBotzLockSensorValueErrorRTN": netBotzLockSensorValueErrorRTN,
       "netBotzDoorSensorForcedEntryErrorRTN": netBotzDoorSensorForcedEntryErrorRTN,
       "netBotzRackHandleSensorOpenErrorRTN": netBotzRackHandleSensorOpenErrorRTN,
       "netBotzCardReaderLocalAuthorizationErrorRTN": netBotzCardReaderLocalAuthorizationErrorRTN,
       "netBotzCardReaderLdapAuthorizationErrorRTN": netBotzCardReaderLdapAuthorizationErrorRTN,
       "netBotzTestTraps": netBotzTestTraps,
       "netBotzTestPrefix": netBotzTestPrefix,
       "netBotzTestNotification": netBotzTestNotification,
       "netBotzPodTraps": netBotzPodTraps,
       "netBotzPodPrefix": netBotzPodPrefix,
       "netBotzPodUnplugged": netBotzPodUnplugged,
       "netBotzLogonError": netBotzLogonError,
       "netBotzRmtLinkError": netBotzRmtLinkError,
       "netBotzPodReplugged": netBotzPodReplugged,
       "netBotzLogonErrorResolved": netBotzLogonErrorResolved,
       "netBotzRmtLinkErrorResolved": netBotzRmtLinkErrorResolved,
       "netBotzSensorPodTraps": netBotzSensorPodTraps,
       "netBotzSensorPodPrefix": netBotzSensorPodPrefix,
       "netBotzSensorPodUnplugged": netBotzSensorPodUnplugged,
       "netBotzSensorPodReplugged": netBotzSensorPodReplugged,
       "netBotzCameraTraps": netBotzCameraTraps,
       "netBotzCameraPrefix": netBotzCameraPrefix,
       "netBotzCameraUnplugged": netBotzCameraUnplugged,
       "netBotzCameraReplugged": netBotzCameraReplugged,
       "netBotz4to20mAPodTraps": netBotz4to20mAPodTraps,
       "netBotz4to20mAPodPrefix": netBotz4to20mAPodPrefix,
       "netBotzFourToTwentymAPodError": netBotzFourToTwentymAPodError,
       "netBotzFourToTwentymAPodTooHigh": netBotzFourToTwentymAPodTooHigh,
       "netBotzFourToTwentymAPodUnplugged": netBotzFourToTwentymAPodUnplugged,
       "netBotzFourToTwentymAPodTooLow": netBotzFourToTwentymAPodTooLow,
       "netBotzFourToTwentymAPodErrorRTN": netBotzFourToTwentymAPodErrorRTN,
       "netBotzFourToTwentymAPodTooHighRTN": netBotzFourToTwentymAPodTooHighRTN,
       "netBotzFourToTwentymAPodReplugged": netBotzFourToTwentymAPodReplugged,
       "netBotzFourToTwentymAPodTooLowRTN": netBotzFourToTwentymAPodTooLowRTN,
       "netBotzRpduTraps": netBotzRpduTraps,
       "netBotzRpduPrefix": netBotzRpduPrefix,
       "netBotzRpduUnplugged": netBotzRpduUnplugged,
       "netBotzRpduReplugged": netBotzRpduReplugged,
       "netBotzUpsTraps": netBotzUpsTraps,
       "netBotzUpsPrefix": netBotzUpsPrefix,
       "netBotzUpsUnplugged": netBotzUpsUnplugged,
       "netBotzUpsReplugged": netBotzUpsReplugged,
       "netBotzGenericTraps": netBotzGenericTraps,
       "netBotzGenericPrefix": netBotzGenericPrefix,
       "netBotzGenericNotification": netBotzGenericNotification,
       "netBotzTrapParms": netBotzTrapParms,
       "netBotzTrapErrorID": netBotzTrapErrorID,
       "netBotzTrapErrorType": netBotzTrapErrorType,
       "netBotzTrapErrorTypeLabel": netBotzTrapErrorTypeLabel,
       "netBotzTrapSensorID": netBotzTrapSensorID,
       "netBotzTrapSensorLabel": netBotzTrapSensorLabel,
       "netBotzTrapContainerID": netBotzTrapContainerID,
       "netBotzTrapContainerLabel": netBotzTrapContainerLabel,
       "netBotzTrapPortID": netBotzTrapPortID,
       "netBotzTrapPortLabel": netBotzTrapPortLabel,
       "netBotzTrapStartTime": netBotzTrapStartTime,
       "netBotzTrapNotifyTime": netBotzTrapNotifyTime,
       "netBotzTrapResolveTime": netBotzTrapResolveTime,
       "netBotzTrapSeverity": netBotzTrapSeverity,
       "netBotzTrapSensorValue": netBotzTrapSensorValue,
       "netBotzTrapSensorValueInt": netBotzTrapSensorValueInt,
       "netBotzTrapSensorValueFraction": netBotzTrapSensorValueFraction,
       "netBotzTrapData": netBotzTrapData,
       "netBotzProducts": netBotzProducts,
       "netBotzBotz": netBotzBotz,
       "netBotz750Rack": netBotz750Rack,
       "netBotz755Wall": netBotz755Wall,
       "netbotzBotzGroups": netbotzBotzGroups,
       "netbotzObjectGroup": netbotzObjectGroup,
       "netbotzNotificationGroup": netbotzNotificationGroup,
       "netBotzErrorStatus": netBotzErrorStatus}
)
