# SNMP MIB module (PRVT-STATISTICS-HISTORY-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\telco-systems\binox\PRVT-STATISTICS-HISTORY-MIB

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

(switch,) = mibBuilder.importSymbols(
    "PRVT-SWITCH-MIB",
    "switch")

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
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

prvtStatHistMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 180)
)
if mibBuilder.loadTexts:
    prvtStatHistMIB.setRevisions(
        ("2012-02-20 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_PrvtStatHistObjects_ObjectIdentity = ObjectIdentity
prvtStatHistObjects = _PrvtStatHistObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 180, 1)
)
_PrvtStatHistShutdown_Type = TruthValue
_PrvtStatHistShutdown_Object = MibScalar
prvtStatHistShutdown = _PrvtStatHistShutdown_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 180, 1, 1),
    _PrvtStatHistShutdown_Type()
)
prvtStatHistShutdown.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prvtStatHistShutdown.setStatus("current")


class _PrvtStatHistGetInterval_Type(Unsigned32):
    """Custom type prvtStatHistGetInterval based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 3600),
    )


_PrvtStatHistGetInterval_Type.__name__ = "Unsigned32"
_PrvtStatHistGetInterval_Object = MibScalar
prvtStatHistGetInterval = _PrvtStatHistGetInterval_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 180, 1, 2),
    _PrvtStatHistGetInterval_Type()
)
prvtStatHistGetInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prvtStatHistGetInterval.setStatus("current")


class _PrvtStatHistType_Type(Integer32):
    """Custom type prvtStatHistType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("absolute", 1),
          ("delta", 2))
    )


_PrvtStatHistType_Type.__name__ = "Integer32"
_PrvtStatHistType_Object = MibScalar
prvtStatHistType = _PrvtStatHistType_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 180, 1, 3),
    _PrvtStatHistType_Type()
)
prvtStatHistType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prvtStatHistType.setStatus("current")
_PrvtStatHistProfileTable_Object = MibTable
prvtStatHistProfileTable = _PrvtStatHistProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 180, 1, 4)
)
if mibBuilder.loadTexts:
    prvtStatHistProfileTable.setStatus("current")
_PrvtStatHistProfileEntry_Object = MibTableRow
prvtStatHistProfileEntry = _PrvtStatHistProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 180, 1, 4, 1)
)
prvtStatHistProfileEntry.setIndexNames(
    (0, "PRVT-STATISTICS-HISTORY-MIB", "prvtStatHistProfileName"),
)
if mibBuilder.loadTexts:
    prvtStatHistProfileEntry.setStatus("current")


class _PrvtStatHistProfileName_Type(OctetString):
    """Custom type prvtStatHistProfileName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_PrvtStatHistProfileName_Type.__name__ = "OctetString"
_PrvtStatHistProfileName_Object = MibTableColumn
prvtStatHistProfileName = _PrvtStatHistProfileName_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 180, 1, 4, 1, 1),
    _PrvtStatHistProfileName_Type()
)
prvtStatHistProfileName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    prvtStatHistProfileName.setStatus("current")
_PrvtStatHistProfileRowStatus_Type = RowStatus
_PrvtStatHistProfileRowStatus_Object = MibTableColumn
prvtStatHistProfileRowStatus = _PrvtStatHistProfileRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 180, 1, 4, 1, 2),
    _PrvtStatHistProfileRowStatus_Type()
)
prvtStatHistProfileRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    prvtStatHistProfileRowStatus.setStatus("current")


class _PrvtStatHistProfileXPathTemplate_Type(OctetString):
    """Custom type prvtStatHistProfileXPathTemplate based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_PrvtStatHistProfileXPathTemplate_Type.__name__ = "OctetString"
_PrvtStatHistProfileXPathTemplate_Object = MibTableColumn
prvtStatHistProfileXPathTemplate = _PrvtStatHistProfileXPathTemplate_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 180, 1, 4, 1, 3),
    _PrvtStatHistProfileXPathTemplate_Type()
)
prvtStatHistProfileXPathTemplate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    prvtStatHistProfileXPathTemplate.setStatus("current")
_PrvtStatHistControlTable_Object = MibTable
prvtStatHistControlTable = _PrvtStatHistControlTable_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 180, 1, 5)
)
if mibBuilder.loadTexts:
    prvtStatHistControlTable.setStatus("current")
_PrvtStatHistControlEntry_Object = MibTableRow
prvtStatHistControlEntry = _PrvtStatHistControlEntry_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 180, 1, 5, 1)
)
prvtStatHistControlEntry.setIndexNames(
    (0, "PRVT-STATISTICS-HISTORY-MIB", "prvtStatHistControlId"),
)
if mibBuilder.loadTexts:
    prvtStatHistControlEntry.setStatus("current")


class _PrvtStatHistControlId_Type(Unsigned32):
    """Custom type prvtStatHistControlId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 200),
    )


_PrvtStatHistControlId_Type.__name__ = "Unsigned32"
_PrvtStatHistControlId_Object = MibTableColumn
prvtStatHistControlId = _PrvtStatHistControlId_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 180, 1, 5, 1, 1),
    _PrvtStatHistControlId_Type()
)
prvtStatHistControlId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    prvtStatHistControlId.setStatus("current")
_PrvtStatHistControlRowStatus_Type = RowStatus
_PrvtStatHistControlRowStatus_Object = MibTableColumn
prvtStatHistControlRowStatus = _PrvtStatHistControlRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 180, 1, 5, 1, 2),
    _PrvtStatHistControlRowStatus_Type()
)
prvtStatHistControlRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    prvtStatHistControlRowStatus.setStatus("current")


class _PrvtStatHistControlProfileName_Type(OctetString):
    """Custom type prvtStatHistControlProfileName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_PrvtStatHistControlProfileName_Type.__name__ = "OctetString"
_PrvtStatHistControlProfileName_Object = MibTableColumn
prvtStatHistControlProfileName = _PrvtStatHistControlProfileName_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 180, 1, 5, 1, 3),
    _PrvtStatHistControlProfileName_Type()
)
prvtStatHistControlProfileName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    prvtStatHistControlProfileName.setStatus("current")


class _PrvtStatHistControlXPathKey_Type(OctetString):
    """Custom type prvtStatHistControlXPathKey based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_PrvtStatHistControlXPathKey_Type.__name__ = "OctetString"
_PrvtStatHistControlXPathKey_Object = MibTableColumn
prvtStatHistControlXPathKey = _PrvtStatHistControlXPathKey_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 180, 1, 5, 1, 4),
    _PrvtStatHistControlXPathKey_Type()
)
prvtStatHistControlXPathKey.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    prvtStatHistControlXPathKey.setStatus("current")
_PrvtStatHistControlValue_Type = OctetString
_PrvtStatHistControlValue_Object = MibTableColumn
prvtStatHistControlValue = _PrvtStatHistControlValue_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 180, 1, 5, 1, 5),
    _PrvtStatHistControlValue_Type()
)
prvtStatHistControlValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtStatHistControlValue.setStatus("current")
_PrvtStatHistControlFirstDataId_Type = OctetString
_PrvtStatHistControlFirstDataId_Object = MibTableColumn
prvtStatHistControlFirstDataId = _PrvtStatHistControlFirstDataId_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 180, 1, 5, 1, 6),
    _PrvtStatHistControlFirstDataId_Type()
)
prvtStatHistControlFirstDataId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtStatHistControlFirstDataId.setStatus("current")
_PrvtStatHistControlLastDataId_Type = OctetString
_PrvtStatHistControlLastDataId_Object = MibTableColumn
prvtStatHistControlLastDataId = _PrvtStatHistControlLastDataId_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 180, 1, 5, 1, 7),
    _PrvtStatHistControlLastDataId_Type()
)
prvtStatHistControlLastDataId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtStatHistControlLastDataId.setStatus("current")
_PrvtStatHistDataTable_Object = MibTable
prvtStatHistDataTable = _PrvtStatHistDataTable_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 180, 1, 6)
)
if mibBuilder.loadTexts:
    prvtStatHistDataTable.setStatus("current")
_PrvtStatHistDataEntry_Object = MibTableRow
prvtStatHistDataEntry = _PrvtStatHistDataEntry_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 180, 1, 6, 1)
)
prvtStatHistDataEntry.setIndexNames(
    (0, "PRVT-STATISTICS-HISTORY-MIB", "prvtStatHistControlId"),
    (0, "PRVT-STATISTICS-HISTORY-MIB", "prvtStatHistDataId"),
)
if mibBuilder.loadTexts:
    prvtStatHistDataEntry.setStatus("current")
_PrvtStatHistDataId_Type = OctetString
_PrvtStatHistDataId_Object = MibTableColumn
prvtStatHistDataId = _PrvtStatHistDataId_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 180, 1, 6, 1, 1),
    _PrvtStatHistDataId_Type()
)
prvtStatHistDataId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    prvtStatHistDataId.setStatus("current")
_PrvtStatHistDataIntervalStart_Type = OctetString
_PrvtStatHistDataIntervalStart_Object = MibTableColumn
prvtStatHistDataIntervalStart = _PrvtStatHistDataIntervalStart_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 180, 1, 6, 1, 2),
    _PrvtStatHistDataIntervalStart_Type()
)
prvtStatHistDataIntervalStart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtStatHistDataIntervalStart.setStatus("current")
_PrvtStatHistDataIntervalEnd_Type = OctetString
_PrvtStatHistDataIntervalEnd_Object = MibTableColumn
prvtStatHistDataIntervalEnd = _PrvtStatHistDataIntervalEnd_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 180, 1, 6, 1, 3),
    _PrvtStatHistDataIntervalEnd_Type()
)
prvtStatHistDataIntervalEnd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtStatHistDataIntervalEnd.setStatus("current")
_PrvtStatHistDataProfile_Type = OctetString
_PrvtStatHistDataProfile_Object = MibTableColumn
prvtStatHistDataProfile = _PrvtStatHistDataProfile_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 180, 1, 6, 1, 4),
    _PrvtStatHistDataProfile_Type()
)
prvtStatHistDataProfile.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtStatHistDataProfile.setStatus("current")
_PrvtStatHistDataKey_Type = OctetString
_PrvtStatHistDataKey_Object = MibTableColumn
prvtStatHistDataKey = _PrvtStatHistDataKey_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 180, 1, 6, 1, 5),
    _PrvtStatHistDataKey_Type()
)
prvtStatHistDataKey.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtStatHistDataKey.setStatus("current")
_PrvtStatHistDataValue_Type = OctetString
_PrvtStatHistDataValue_Object = MibTableColumn
prvtStatHistDataValue = _PrvtStatHistDataValue_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 180, 1, 6, 1, 6),
    _PrvtStatHistDataValue_Type()
)
prvtStatHistDataValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtStatHistDataValue.setStatus("current")


class _PrvtStatHistDataStatus_Type(Integer32):
    """Custom type prvtStatHistDataStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("notAvailable", 1),
          ("positive", 2),
          ("negative", 3))
    )


_PrvtStatHistDataStatus_Type.__name__ = "Integer32"
_PrvtStatHistDataStatus_Object = MibTableColumn
prvtStatHistDataStatus = _PrvtStatHistDataStatus_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 180, 1, 6, 1, 7),
    _PrvtStatHistDataStatus_Type()
)
prvtStatHistDataStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtStatHistDataStatus.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "PRVT-STATISTICS-HISTORY-MIB",
    **{"prvtStatHistMIB": prvtStatHistMIB,
       "prvtStatHistObjects": prvtStatHistObjects,
       "prvtStatHistShutdown": prvtStatHistShutdown,
       "prvtStatHistGetInterval": prvtStatHistGetInterval,
       "prvtStatHistType": prvtStatHistType,
       "prvtStatHistProfileTable": prvtStatHistProfileTable,
       "prvtStatHistProfileEntry": prvtStatHistProfileEntry,
       "prvtStatHistProfileName": prvtStatHistProfileName,
       "prvtStatHistProfileRowStatus": prvtStatHistProfileRowStatus,
       "prvtStatHistProfileXPathTemplate": prvtStatHistProfileXPathTemplate,
       "prvtStatHistControlTable": prvtStatHistControlTable,
       "prvtStatHistControlEntry": prvtStatHistControlEntry,
       "prvtStatHistControlId": prvtStatHistControlId,
       "prvtStatHistControlRowStatus": prvtStatHistControlRowStatus,
       "prvtStatHistControlProfileName": prvtStatHistControlProfileName,
       "prvtStatHistControlXPathKey": prvtStatHistControlXPathKey,
       "prvtStatHistControlValue": prvtStatHistControlValue,
       "prvtStatHistControlFirstDataId": prvtStatHistControlFirstDataId,
       "prvtStatHistControlLastDataId": prvtStatHistControlLastDataId,
       "prvtStatHistDataTable": prvtStatHistDataTable,
       "prvtStatHistDataEntry": prvtStatHistDataEntry,
       "prvtStatHistDataId": prvtStatHistDataId,
       "prvtStatHistDataIntervalStart": prvtStatHistDataIntervalStart,
       "prvtStatHistDataIntervalEnd": prvtStatHistDataIntervalEnd,
       "prvtStatHistDataProfile": prvtStatHistDataProfile,
       "prvtStatHistDataKey": prvtStatHistDataKey,
       "prvtStatHistDataValue": prvtStatHistDataValue,
       "prvtStatHistDataStatus": prvtStatHistDataStatus}
)
