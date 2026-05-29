# SNMP MIB module (PRVT-CFM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\telco-systems\binos\PRVT-CFM-MIB

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

(Dot1afCfmIndexIntegerNextFree,
 Dot1agCfmMDLevelOrNone,
 dot1agCfmLtrEntry,
 dot1agCfmMaCompEntry,
 dot1agCfmMaIndex,
 dot1agCfmMdIndex,
 dot1agCfmMepDbRMepIdentifier,
 dot1agCfmMepEntry,
 dot1agCfmMepIdentifier) = mibBuilder.importSymbols(
    "IEEE8021-CFM-MIB",
    "Dot1afCfmIndexIntegerNextFree",
    "Dot1agCfmMDLevelOrNone",
    "dot1agCfmLtrEntry",
    "dot1agCfmMaCompEntry",
    "dot1agCfmMaIndex",
    "dot1agCfmMdIndex",
    "dot1agCfmMepDbRMepIdentifier",
    "dot1agCfmMepEntry",
    "dot1agCfmMepIdentifier")

(switch,) = mibBuilder.importSymbols(
    "PRVT-SWITCH-MIB",
    "switch")

(VlanId,) = mibBuilder.importSymbols(
    "Q-BRIDGE-MIB",
    "VlanId")

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
 MacAddress,
 PhysAddress,
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

prvtCfmMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 131)
)
if mibBuilder.loadTexts:
    prvtCfmMib.setRevisions(
        ("2012-09-12 00:00",
         "2011-04-18 00:00",
         "2011-01-18 00:00",
         "2010-07-08 00:00",
         "2010-04-08 00:00",
         "2010-03-17 00:00",
         "2009-06-20 00:00",
         "2008-08-19 00:00",
         "2008-06-24 00:00",
         "2008-01-20 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_PrvtCfmMibNotifications_ObjectIdentity = ObjectIdentity
prvtCfmMibNotifications = _PrvtCfmMibNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 131, 0)
)
_PrvtCfmMibObjects_ObjectIdentity = ObjectIdentity
prvtCfmMibObjects = _PrvtCfmMibObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 131, 1)
)


class _PrvtCfmUpdateInterval_Type(Unsigned32):
    """Custom type prvtCfmUpdateInterval based on Unsigned32"""
    defaultValue = 20

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_PrvtCfmUpdateInterval_Type.__name__ = "Unsigned32"
_PrvtCfmUpdateInterval_Object = MibScalar
prvtCfmUpdateInterval = _PrvtCfmUpdateInterval_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 131, 1, 1),
    _PrvtCfmUpdateInterval_Type()
)
prvtCfmUpdateInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prvtCfmUpdateInterval.setStatus("current")


class _PrvtCfmStatus_Type(Integer32):
    """Custom type prvtCfmStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_PrvtCfmStatus_Type.__name__ = "Integer32"
_PrvtCfmStatus_Object = MibScalar
prvtCfmStatus = _PrvtCfmStatus_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 131, 1, 2),
    _PrvtCfmStatus_Type()
)
prvtCfmStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prvtCfmStatus.setStatus("current")
_PrvtCfmProfile_ObjectIdentity = ObjectIdentity
prvtCfmProfile = _PrvtCfmProfile_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 131, 1, 3)
)
_PrvtCfmProfileTableNextIndex_Type = Dot1afCfmIndexIntegerNextFree
_PrvtCfmProfileTableNextIndex_Object = MibScalar
prvtCfmProfileTableNextIndex = _PrvtCfmProfileTableNextIndex_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 131, 1, 3, 1),
    _PrvtCfmProfileTableNextIndex_Type()
)
prvtCfmProfileTableNextIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtCfmProfileTableNextIndex.setStatus("current")
_PrvtCfmProfileTable_Object = MibTable
prvtCfmProfileTable = _PrvtCfmProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 131, 1, 3, 2)
)
if mibBuilder.loadTexts:
    prvtCfmProfileTable.setStatus("current")
_PrvtCfmProfileEntry_Object = MibTableRow
prvtCfmProfileEntry = _PrvtCfmProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 131, 1, 3, 2, 1)
)
prvtCfmProfileEntry.setIndexNames(
    (0, "PRVT-CFM-MIB", "prvtCfmProfileIndex"),
)
if mibBuilder.loadTexts:
    prvtCfmProfileEntry.setStatus("current")
_PrvtCfmProfileIndex_Type = Unsigned32
_PrvtCfmProfileIndex_Object = MibTableColumn
prvtCfmProfileIndex = _PrvtCfmProfileIndex_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 131, 1, 3, 2, 1, 1),
    _PrvtCfmProfileIndex_Type()
)
prvtCfmProfileIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    prvtCfmProfileIndex.setStatus("current")


class _PrvtCfmProfileName_Type(DisplayString):
    """Custom type prvtCfmProfileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 20),
    )


_PrvtCfmProfileName_Type.__name__ = "DisplayString"
_PrvtCfmProfileName_Object = MibTableColumn
prvtCfmProfileName = _PrvtCfmProfileName_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 131, 1, 3, 2, 1, 2),
    _PrvtCfmProfileName_Type()
)
prvtCfmProfileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prvtCfmProfileName.setStatus("current")


class _PrvtCfmProfilePriority_Type(Unsigned32):
    """Custom type prvtCfmProfilePriority based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_PrvtCfmProfilePriority_Type.__name__ = "Unsigned32"
_PrvtCfmProfilePriority_Object = MibTableColumn
prvtCfmProfilePriority = _PrvtCfmProfilePriority_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 131, 1, 3, 2, 1, 3),
    _PrvtCfmProfilePriority_Type()
)
prvtCfmProfilePriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prvtCfmProfilePriority.setStatus("current")


class _PrvtCfmProfileRate_Type(Unsigned32):
    """Custom type prvtCfmProfileRate based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_PrvtCfmProfileRate_Type.__name__ = "Unsigned32"
_PrvtCfmProfileRate_Object = MibTableColumn
prvtCfmProfileRate = _PrvtCfmProfileRate_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 131, 1, 3, 2, 1, 4),
    _PrvtCfmProfileRate_Type()
)
prvtCfmProfileRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prvtCfmProfileRate.setStatus("current")


class _PrvtCfmProfileSize_Type(Unsigned32):
    """Custom type prvtCfmProfileSize based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1462),
    )


_PrvtCfmProfileSize_Type.__name__ = "Unsigned32"
_PrvtCfmProfileSize_Object = MibTableColumn
prvtCfmProfileSize = _PrvtCfmProfileSize_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 131, 1, 3, 2, 1, 5),
    _PrvtCfmProfileSize_Type()
)
prvtCfmProfileSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prvtCfmProfileSize.setStatus("current")


class _PrvtCfmProfileBucketSize_Type(Unsigned32):
    """Custom type prvtCfmProfileBucketSize based on Unsigned32"""
    defaultValue = 20

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 255),
    )


_PrvtCfmProfileBucketSize_Type.__name__ = "Unsigned32"
_PrvtCfmProfileBucketSize_Object = MibTableColumn
prvtCfmProfileBucketSize = _PrvtCfmProfileBucketSize_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 131, 1, 3, 2, 1, 6),
    _PrvtCfmProfileBucketSize_Type()
)
prvtCfmProfileBucketSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prvtCfmProfileBucketSize.setStatus("current")


class _PrvtCfmProfile1wJitterError_Type(Unsigned32):
    """Custom type prvtCfmProfile1wJitterError based on Unsigned32"""
    defaultValue = 350

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10000),
    )


_PrvtCfmProfile1wJitterError_Type.__name__ = "Unsigned32"
_PrvtCfmProfile1wJitterError_Object = MibTableColumn
prvtCfmProfile1wJitterError = _PrvtCfmProfile1wJitterError_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 131, 1, 3, 2, 1, 7),
    _PrvtCfmProfile1wJitterError_Type()
)
prvtCfmProfile1wJitterError.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prvtCfmProfile1wJitterError.setStatus("current")


class _PrvtCfmProfile1wJitterWarning_Type(Unsigned32):
    """Custom type prvtCfmProfile1wJitterWarning based on Unsigned32"""
    defaultValue = 300

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10000),
    )


_PrvtCfmProfile1wJitterWarning_Type.__name__ = "Unsigned32"
_PrvtCfmProfile1wJitterWarning_Object = MibTableColumn
prvtCfmProfile1wJitterWarning = _PrvtCfmProfile1wJitterWarning_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 131, 1, 3, 2, 1, 8),
    _PrvtCfmProfile1wJitterWarning_Type()
)
prvtCfmProfile1wJitterWarning.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prvtCfmProfile1wJitterWarning.setStatus("current")


class _PrvtCfmProfileJitterError_Type(Unsigned32):
    """Custom type prvtCfmProfileJitterError based on Unsigned32"""
    defaultValue = 700

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10000),
    )


_PrvtCfmProfileJitterError_Type.__name__ = "Unsigned32"
_PrvtCfmProfileJitterError_Object = MibTableColumn
prvtCfmProfileJitterError = _PrvtCfmProfileJitterError_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 131, 1, 3, 2, 1, 9),
    _PrvtCfmProfileJitterError_Type()
)
prvtCfmProfileJitterError.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prvtCfmProfileJitterError.setStatus("current")


class _PrvtCfmProfileJitterErrorPeriod_Type(Unsigned32):
    """Custom type prvtCfmProfileJitterErrorPeriod based on Unsigned32"""
    defaultValue = 90

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3600),
    )


_PrvtCfmProfileJitterErrorPeriod_Type.__name__ = "Unsigned32"
_PrvtCfmProfileJitterErrorPeriod_Object = MibTableColumn
prvtCfmProfileJitterErrorPeriod = _PrvtCfmProfileJitterErrorPeriod_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 131, 1, 3, 2, 1, 10),
    _PrvtCfmProfileJitterErrorPeriod_Type()
)
prvtCfmProfileJitterErrorPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prvtCfmProfileJitterErrorPeriod.setStatus("current")


class _PrvtCfmProfileJitterWarning_Type(Unsigned32):
    """Custom type prvtCfmProfileJitterWarning based on Unsigned32"""
    defaultValue = 600

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10000),
    )


_PrvtCfmProfileJitterWarning_Type.__name__ = "Unsigned32"
_PrvtCfmProfileJitterWarning_Object = MibTableColumn
prvtCfmProfileJitterWarning = _PrvtCfmProfileJitterWarning_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 131, 1, 3, 2, 1, 11),
    _PrvtCfmProfileJitterWarning_Type()
)
prvtCfmProfileJitterWarning.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prvtCfmProfileJitterWarning.setStatus("current")


class _PrvtCfmProfileJitterWarningPeriod_Type(Unsigned32):
    """Custom type prvtCfmProfileJitterWarningPeriod based on Unsigned32"""
    defaultValue = 180

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3600),
    )


_PrvtCfmProfileJitterWarningPeriod_Type.__name__ = "Unsigned32"
_PrvtCfmProfileJitterWarningPeriod_Object = MibTableColumn
prvtCfmProfileJitterWarningPeriod = _PrvtCfmProfileJitterWarningPeriod_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 131, 1, 3, 2, 1, 12),
    _PrvtCfmProfileJitterWarningPeriod_Type()
)
prvtCfmProfileJitterWarningPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prvtCfmProfileJitterWarningPeriod.setStatus("current")


class _PrvtCfmProfileFrameLossError_Type(Unsigned32):
    """Custom type prvtCfmProfileFrameLossError based on Unsigned32"""
    defaultValue = 10

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 99),
    )


_PrvtCfmProfileFrameLossError_Type.__name__ = "Unsigned32"
_PrvtCfmProfileFrameLossError_Object = MibTableColumn
prvtCfmProfileFrameLossError = _PrvtCfmProfileFrameLossError_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 131, 1, 3, 2, 1, 13),
    _PrvtCfmProfileFrameLossError_Type()
)
prvtCfmProfileFrameLossError.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prvtCfmProfileFrameLossError.setStatus("current")


class _PrvtCfmProfileFrameLossWarning_Type(Unsigned32):
    """Custom type prvtCfmProfileFrameLossWarning based on Unsigned32"""
    defaultValue = 8

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 99),
    )


_PrvtCfmProfileFrameLossWarning_Type.__name__ = "Unsigned32"
_PrvtCfmProfileFrameLossWarning_Object = MibTableColumn
prvtCfmProfileFrameLossWarning = _PrvtCfmProfileFrameLossWarning_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 131, 1, 3, 2, 1, 14),
    _PrvtCfmProfileFrameLossWarning_Type()
)
prvtCfmProfileFrameLossWarning.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prvtCfmProfileFrameLossWarning.setStatus("current")


class _PrvtCfmProfileLatencyError_Type(Unsigned32):
    """Custom type prvtCfmProfileLatencyError based on Unsigned32"""
    defaultValue = 2000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10000),
    )


_PrvtCfmProfileLatencyError_Type.__name__ = "Unsigned32"
_PrvtCfmProfileLatencyError_Object = MibTableColumn
prvtCfmProfileLatencyError = _PrvtCfmProfileLatencyError_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 131, 1, 3, 2, 1, 15),
    _PrvtCfmProfileLatencyError_Type()
)
prvtCfmProfileLatencyError.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prvtCfmProfileLatencyError.setStatus("current")


class _PrvtCfmProfileLatencyErrorPeriod_Type(Unsigned32):
    """Custom type prvtCfmProfileLatencyErrorPeriod based on Unsigned32"""
    defaultValue = 90

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3600),
    )


_PrvtCfmProfileLatencyErrorPeriod_Type.__name__ = "Unsigned32"
_PrvtCfmProfileLatencyErrorPeriod_Object = MibTableColumn
prvtCfmProfileLatencyErrorPeriod = _PrvtCfmProfileLatencyErrorPeriod_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 131, 1, 3, 2, 1, 16),
    _PrvtCfmProfileLatencyErrorPeriod_Type()
)
prvtCfmProfileLatencyErrorPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prvtCfmProfileLatencyErrorPeriod.setStatus("current")


class _PrvtCfmProfileLatencyWarning_Type(Unsigned32):
    """Custom type prvtCfmProfileLatencyWarning based on Unsigned32"""
    defaultValue = 1600

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10000),
    )


_PrvtCfmProfileLatencyWarning_Type.__name__ = "Unsigned32"
_PrvtCfmProfileLatencyWarning_Object = MibTableColumn
prvtCfmProfileLatencyWarning = _PrvtCfmProfileLatencyWarning_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 131, 1, 3, 2, 1, 17),
    _PrvtCfmProfileLatencyWarning_Type()
)
prvtCfmProfileLatencyWarning.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prvtCfmProfileLatencyWarning.setStatus("current")


class _PrvtCfmProfileLatencyWarningPeriod_Type(Unsigned32):
    """Custom type prvtCfmProfileLatencyWarningPeriod based on Unsigned32"""
    defaultValue = 180

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3600),
    )


_PrvtCfmProfileLatencyWarningPeriod_Type.__name__ = "Unsigned32"
_PrvtCfmProfileLatencyWarningPeriod_Object = MibTableColumn
prvtCfmProfileLatencyWarningPeriod = _PrvtCfmProfileLatencyWarningPeriod_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 131, 1, 3, 2, 1, 18),
    _PrvtCfmProfileLatencyWarningPeriod_Type()
)
prvtCfmProfileLatencyWarningPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prvtCfmProfileLatencyWarningPeriod.setStatus("current")
_PrvtCfmProfileRowStatus_Type = RowStatus
_PrvtCfmProfileRowStatus_Object = MibTableColumn
prvtCfmProfileRowStatus = _PrvtCfmProfileRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 131, 1, 3, 2, 1, 19),
    _PrvtCfmProfileRowStatus_Type()
)
prvtCfmProfileRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    prvtCfmProfileRowStatus.setStatus("current")


class _PrvtCfmProfile1wJitterEnable_Type(TruthValue):
    """Custom type prvtCfmProfile1wJitterEnable based on TruthValue"""
    defaultValue = 1


_PrvtCfmProfile1wJitterEnable_Type.__name__ = "TruthValue"
_PrvtCfmProfile1wJitterEnable_Object = MibTableColumn
prvtCfmProfile1wJitterEnable = _PrvtCfmProfile1wJitterEnable_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 131, 1, 3, 2, 1, 20),
    _PrvtCfmProfile1wJitterEnable_Type()
)
prvtCfmProfile1wJitterEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prvtCfmProfile1wJitterEnable.setStatus("current")


class _PrvtCfmProfileJitterEnable_Type(TruthValue):
    """Custom type prvtCfmProfileJitterEnable based on TruthValue"""
    defaultValue = 1


_PrvtCfmProfileJitterEnable_Type.__name__ = "TruthValue"
_PrvtCfmProfileJitterEnable_Object = MibTableColumn
prvtCfmProfileJitterEnable = _PrvtCfmProfileJitterEnable_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 131, 1, 3, 2, 1, 21),
    _PrvtCfmProfileJitterEnable_Type()
)
prvtCfmProfileJitterEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prvtCfmProfileJitterEnable.setStatus("current")


class _PrvtCfmProfileFrameLossEnable_Type(TruthValue):
    """Custom type prvtCfmProfileFrameLossEnable based on TruthValue"""
    defaultValue = 1


_PrvtCfmProfileFrameLossEnable_Type.__name__ = "TruthValue"
_PrvtCfmProfileFrameLossEnable_Object = MibTableColumn
prvtCfmProfileFrameLossEnable = _PrvtCfmProfileFrameLossEnable_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 131, 1, 3, 2, 1, 22),
    _PrvtCfmProfileFrameLossEnable_Type()
)
prvtCfmProfileFrameLossEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prvtCfmProfileFrameLossEnable.setStatus("current")


class _PrvtCfmProfileLatencyEnable_Type(TruthValue):
    """Custom type prvtCfmProfileLatencyEnable based on TruthValue"""
    defaultValue = 1


_PrvtCfmProfileLatencyEnable_Type.__name__ = "TruthValue"
_PrvtCfmProfileLatencyEnable_Object = MibTableColumn
prvtCfmProfileLatencyEnable = _PrvtCfmProfileLatencyEnable_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 131, 1, 3, 2, 1, 23),
    _PrvtCfmProfileLatencyEnable_Type()
)
prvtCfmProfileLatencyEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prvtCfmProfileLatencyEnable.setStatus("current")
_PrvtCfmProcess_ObjectIdentity = ObjectIdentity
prvtCfmProcess = _PrvtCfmProcess_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 131, 1, 4)
)
_PrvtCfmProcessTableNextIndex_Type = Dot1afCfmIndexIntegerNextFree
_PrvtCfmProcessTableNextIndex_Object = MibScalar
prvtCfmProcessTableNextIndex = _PrvtCfmProcessTableNextIndex_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 131, 1, 4, 1),
    _PrvtCfmProcessTableNextIndex_Type()
)
prvtCfmProcessTableNextIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtCfmProcessTableNextIndex.setStatus("current")
_PrvtCfmProcessTable_Object = MibTable
prvtCfmProcessTable = _PrvtCfmProcessTable_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 131, 1, 4, 2)
)
if mibBuilder.loadTexts:
    prvtCfmProcessTable.setStatus("current")
_PrvtCfmProcessEntry_Object = MibTableRow
prvtCfmProcessEntry = _PrvtCfmProcessEntry_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 131, 1, 4, 2, 1)
)
prvtCfmProcessEntry.setIndexNames(
    (0, "IEEE8021-CFM-MIB", "dot1agCfmMdIndex"),
    (0, "IEEE8021-CFM-MIB", "dot1agCfmMaIndex"),
    (0, "PRVT-CFM-MIB", "prvtCfmProcessIndex"),
)
if mibBuilder.loadTexts:
    prvtCfmProcessEntry.setStatus("current")
_PrvtCfmProcessIndex_Type = Unsigned32
_PrvtCfmProcessIndex_Object = MibTableColumn
prvtCfmProcessIndex = _PrvtCfmProcessIndex_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 131, 1, 4, 2, 1, 1),
    _PrvtCfmProcessIndex_Type()
)
prvtCfmProcessIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    prvtCfmProcessIndex.setStatus("current")


class _PrvtCfmProcessProfileIndex_Type(Unsigned32):
    """Custom type prvtCfmProcessProfileIndex based on Unsigned32"""
    defaultValue = 1


_PrvtCfmProcessProfileIndex_Type.__name__ = "Unsigned32"
_PrvtCfmProcessProfileIndex_Object = MibTableColumn
prvtCfmProcessProfileIndex = _PrvtCfmProcessProfileIndex_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 131, 1, 4, 2, 1, 2),
    _PrvtCfmProcessProfileIndex_Type()
)
prvtCfmProcessProfileIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prvtCfmProcessProfileIndex.setStatus("current")


class _PrvtCfmProcessName_Type(OctetString):
    """Custom type prvtCfmProcessName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 20),
    )


_PrvtCfmProcessName_Type.__name__ = "OctetString"
_PrvtCfmProcessName_Object = MibTableColumn
prvtCfmProcessName = _PrvtCfmProcessName_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 131, 1, 4, 2, 1, 3),
    _PrvtCfmProcessName_Type()
)
prvtCfmProcessName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    prvtCfmProcessName.setStatus("current")


class _PrvtCfmProcessStatus_Type(TruthValue):
    """Custom type prvtCfmProcessStatus based on TruthValue"""
    defaultValue = 1


_PrvtCfmProcessStatus_Type.__name__ = "TruthValue"
_PrvtCfmProcessStatus_Object = MibTableColumn
prvtCfmProcessStatus = _PrvtCfmProcessStatus_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 131, 1, 4, 2, 1, 4),
    _PrvtCfmProcessStatus_Type()
)
prvtCfmProcessStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prvtCfmProcessStatus.setStatus("current")


class _PrvtCfmProcessRepeatInterval_Type(Unsigned32):
    """Custom type prvtCfmProcessRepeatInterval based on Unsigned32"""
    defaultValue = 60

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 420),
    )


_PrvtCfmProcessRepeatInterval_Type.__name__ = "Unsigned32"
_PrvtCfmProcessRepeatInterval_Object = MibTableColumn
prvtCfmProcessRepeatInterval = _PrvtCfmProcessRepeatInterval_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 131, 1, 4, 2, 1, 5),
    _PrvtCfmProcessRepeatInterval_Type()
)
prvtCfmProcessRepeatInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prvtCfmProcessRepeatInterval.setStatus("current")


class _PrvtCfmProcessPacketType_Type(Integer32):
    """Custom type prvtCfmProcessPacketType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("cfm", 1),
          ("y1731", 2))
    )


_PrvtCfmProcessPacketType_Type.__name__ = "Integer32"
_PrvtCfmProcessPacketType_Object = MibTableColumn
prvtCfmProcessPacketType = _PrvtCfmProcessPacketType_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 131, 1, 4, 2, 1, 6),
    _PrvtCfmProcessPacketType_Type()
)
prvtCfmProcessPacketType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prvtCfmProcessPacketType.setStatus("current")


class _PrvtCfmProcessUnreturnedPkts_Type(Unsigned32):
    """Custom type prvtCfmProcessUnreturnedPkts based on Unsigned32"""
    defaultValue = 0


_PrvtCfmProcessUnreturnedPkts_Type.__name__ = "Unsigned32"
_PrvtCfmProcessUnreturnedPkts_Object = MibTableColumn
prvtCfmProcessUnreturnedPkts = _PrvtCfmProcessUnreturnedPkts_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 131, 1, 4, 2, 1, 7),
    _PrvtCfmProcessUnreturnedPkts_Type()
)
prvtCfmProcessUnreturnedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtCfmProcessUnreturnedPkts.setStatus("current")
_PrvtCfmProcessRowStatus_Type = RowStatus
_PrvtCfmProcessRowStatus_Object = MibTableColumn
prvtCfmProcessRowStatus = _PrvtCfmProcessRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 131, 1, 4, 2, 1, 8),
    _PrvtCfmProcessRowStatus_Type()
)
prvtCfmProcessRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    prvtCfmProcessRowStatus.setStatus("current")
_PrvtCfmProcessResult_ObjectIdentity = ObjectIdentity
prvtCfmProcessResult = _PrvtCfmProcessResult_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 131, 1, 5)
)
_PrvtCfmProcessResultTable_Object = MibTable
prvtCfmProcessResultTable = _PrvtCfmProcessResultTable_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 131, 1, 5, 1)
)
if mibBuilder.loadTexts:
    prvtCfmProcessResultTable.setStatus("current")
_PrvtCfmProcessResultEntry_Object = MibTableRow
prvtCfmProcessResultEntry = _PrvtCfmProcessResultEntry_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 131, 1, 5, 1, 1)
)
prvtCfmProcessResultEntry.setIndexNames(
    (0, "IEEE8021-CFM-MIB", "dot1agCfmMdIndex"),
    (0, "IEEE8021-CFM-MIB", "dot1agCfmMaIndex"),
    (0, "PRVT-CFM-MIB", "prvtCfmProcessIndex"),
    (0, "IEEE8021-CFM-MIB", "dot1agCfmMepDbRMepIdentifier"),
)
if mibBuilder.loadTexts:
    prvtCfmProcessResultEntry.setStatus("current")
_PrvtCfmProcessResultOneWayJitter_Type = Unsigned32
_PrvtCfmProcessResultOneWayJitter_Object = MibTableColumn
prvtCfmProcessResultOneWayJitter = _PrvtCfmProcessResultOneWayJitter_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 131, 1, 5, 1, 1, 1),
    _PrvtCfmProcessResultOneWayJitter_Type()
)
prvtCfmProcessResultOneWayJitter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtCfmProcessResultOneWayJitter.setStatus("current")
_PrvtCfmProcessResultTwoWayJitter_Type = Unsigned32
_PrvtCfmProcessResultTwoWayJitter_Object = MibTableColumn
prvtCfmProcessResultTwoWayJitter = _PrvtCfmProcessResultTwoWayJitter_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 131, 1, 5, 1, 1, 2),
    _PrvtCfmProcessResultTwoWayJitter_Type()
)
prvtCfmProcessResultTwoWayJitter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtCfmProcessResultTwoWayJitter.setStatus("current")
_PrvtCfmProcessResultLatency_Type = Unsigned32
_PrvtCfmProcessResultLatency_Object = MibTableColumn
prvtCfmProcessResultLatency = _PrvtCfmProcessResultLatency_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 131, 1, 5, 1, 1, 3),
    _PrvtCfmProcessResultLatency_Type()
)
prvtCfmProcessResultLatency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtCfmProcessResultLatency.setStatus("current")


class _PrvtCfmProcessResultFrameloss_Type(Unsigned32):
    """Custom type prvtCfmProcessResultFrameloss based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000),
    )


_PrvtCfmProcessResultFrameloss_Type.__name__ = "Unsigned32"
_PrvtCfmProcessResultFrameloss_Object = MibTableColumn
prvtCfmProcessResultFrameloss = _PrvtCfmProcessResultFrameloss_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 131, 1, 5, 1, 1, 4),
    _PrvtCfmProcessResultFrameloss_Type()
)
prvtCfmProcessResultFrameloss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtCfmProcessResultFrameloss.setStatus("current")
_PrvtCfmMa_ObjectIdentity = ObjectIdentity
prvtCfmMa = _PrvtCfmMa_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 131, 1, 6)
)
_PrvtCfmMaTable_Object = MibTable
prvtCfmMaTable = _PrvtCfmMaTable_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 131, 1, 6, 1)
)
if mibBuilder.loadTexts:
    prvtCfmMaTable.setStatus("current")
_PrvtCfmMaEntry_Object = MibTableRow
prvtCfmMaEntry = _PrvtCfmMaEntry_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 131, 1, 6, 1, 1)
)
if mibBuilder.loadTexts:
    prvtCfmMaEntry.setStatus("current")


class _PrvtCfmMaCompAisLckEnabled_Type(TruthValue):
    """Custom type prvtCfmMaCompAisLckEnabled based on TruthValue"""
    defaultValue = 2


_PrvtCfmMaCompAisLckEnabled_Type.__name__ = "TruthValue"
_PrvtCfmMaCompAisLckEnabled_Object = MibTableColumn
prvtCfmMaCompAisLckEnabled = _PrvtCfmMaCompAisLckEnabled_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 131, 1, 6, 1, 1, 1),
    _PrvtCfmMaCompAisLckEnabled_Type()
)
prvtCfmMaCompAisLckEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prvtCfmMaCompAisLckEnabled.setStatus("current")


class _PrvtCfmMaCompAisLckLevel_Type(Dot1agCfmMDLevelOrNone):
    """Custom type prvtCfmMaCompAisLckLevel based on Dot1agCfmMDLevelOrNone"""
    defaultValue = -1


_PrvtCfmMaCompAisLckLevel_Type.__name__ = "Dot1agCfmMDLevelOrNone"
_PrvtCfmMaCompAisLckLevel_Object = MibTableColumn
prvtCfmMaCompAisLckLevel = _PrvtCfmMaCompAisLckLevel_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 131, 1, 6, 1, 1, 2),
    _PrvtCfmMaCompAisLckLevel_Type()
)
prvtCfmMaCompAisLckLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prvtCfmMaCompAisLckLevel.setStatus("current")


class _PrvtCfmMaCompAisLckInterval_Type(Integer32):
    """Custom type prvtCfmMaCompAisLckInterval based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("interval1s", 1),
          ("interval1min", 2))
    )


_PrvtCfmMaCompAisLckInterval_Type.__name__ = "Integer32"
_PrvtCfmMaCompAisLckInterval_Object = MibTableColumn
prvtCfmMaCompAisLckInterval = _PrvtCfmMaCompAisLckInterval_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 131, 1, 6, 1, 1, 3),
    _PrvtCfmMaCompAisLckInterval_Type()
)
prvtCfmMaCompAisLckInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prvtCfmMaCompAisLckInterval.setStatus("current")


class _PrvtCfmMaCompAisLckPriority_Type(Unsigned32):
    """Custom type prvtCfmMaCompAisLckPriority based on Unsigned32"""
    defaultValue = 6

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_PrvtCfmMaCompAisLckPriority_Type.__name__ = "Unsigned32"
_PrvtCfmMaCompAisLckPriority_Object = MibTableColumn
prvtCfmMaCompAisLckPriority = _PrvtCfmMaCompAisLckPriority_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 131, 1, 6, 1, 1, 4),
    _PrvtCfmMaCompAisLckPriority_Type()
)
prvtCfmMaCompAisLckPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prvtCfmMaCompAisLckPriority.setStatus("current")


class _PrvtCfmMaCompServiceId_Type(Unsigned32):
    """Custom type prvtCfmMaCompServiceId based on Unsigned32"""
    defaultValue = 0


_PrvtCfmMaCompServiceId_Type.__name__ = "Unsigned32"
_PrvtCfmMaCompServiceId_Object = MibTableColumn
prvtCfmMaCompServiceId = _PrvtCfmMaCompServiceId_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 131, 1, 6, 1, 1, 5),
    _PrvtCfmMaCompServiceId_Type()
)
prvtCfmMaCompServiceId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prvtCfmMaCompServiceId.setStatus("current")


class _PrvtCfmMaCompNumberOfServices_Type(Unsigned32):
    """Custom type prvtCfmMaCompNumberOfServices based on Unsigned32"""
    defaultValue = 1


_PrvtCfmMaCompNumberOfServices_Type.__name__ = "Unsigned32"
_PrvtCfmMaCompNumberOfServices_Object = MibTableColumn
prvtCfmMaCompNumberOfServices = _PrvtCfmMaCompNumberOfServices_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 131, 1, 6, 1, 1, 6),
    _PrvtCfmMaCompNumberOfServices_Type()
)
prvtCfmMaCompNumberOfServices.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtCfmMaCompNumberOfServices.setStatus("current")


class _PrvtCfmMaCompClearConnectivity_Type(Unsigned32):
    """Custom type prvtCfmMaCompClearConnectivity based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8191),
    )


_PrvtCfmMaCompClearConnectivity_Type.__name__ = "Unsigned32"
_PrvtCfmMaCompClearConnectivity_Object = MibTableColumn
prvtCfmMaCompClearConnectivity = _PrvtCfmMaCompClearConnectivity_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 131, 1, 6, 1, 1, 7),
    _PrvtCfmMaCompClearConnectivity_Type()
)
prvtCfmMaCompClearConnectivity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prvtCfmMaCompClearConnectivity.setStatus("current")
_PrvtCfmMep_ObjectIdentity = ObjectIdentity
prvtCfmMep = _PrvtCfmMep_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 131, 1, 7)
)
_PrvtCfmMepTable_Object = MibTable
prvtCfmMepTable = _PrvtCfmMepTable_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 131, 1, 7, 1)
)
if mibBuilder.loadTexts:
    prvtCfmMepTable.setStatus("current")
_PrvtCfmMepEntry_Object = MibTableRow
prvtCfmMepEntry = _PrvtCfmMepEntry_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 131, 1, 7, 1, 1)
)
if mibBuilder.loadTexts:
    prvtCfmMepEntry.setStatus("current")


class _PrvtCfmMepAlarmSupressed_Type(TruthValue):
    """Custom type prvtCfmMepAlarmSupressed based on TruthValue"""
    defaultValue = 2


_PrvtCfmMepAlarmSupressed_Type.__name__ = "TruthValue"
_PrvtCfmMepAlarmSupressed_Object = MibTableColumn
prvtCfmMepAlarmSupressed = _PrvtCfmMepAlarmSupressed_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 131, 1, 7, 1, 1, 1),
    _PrvtCfmMepAlarmSupressed_Type()
)
prvtCfmMepAlarmSupressed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtCfmMepAlarmSupressed.setStatus("current")


class _PrvtCfmMepAisCondition_Type(TruthValue):
    """Custom type prvtCfmMepAisCondition based on TruthValue"""
    defaultValue = 2


_PrvtCfmMepAisCondition_Type.__name__ = "TruthValue"
_PrvtCfmMepAisCondition_Object = MibTableColumn
prvtCfmMepAisCondition = _PrvtCfmMepAisCondition_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 131, 1, 7, 1, 1, 2),
    _PrvtCfmMepAisCondition_Type()
)
prvtCfmMepAisCondition.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtCfmMepAisCondition.setStatus("current")


class _PrvtCfmMepLckCondition_Type(TruthValue):
    """Custom type prvtCfmMepLckCondition based on TruthValue"""
    defaultValue = 2


_PrvtCfmMepLckCondition_Type.__name__ = "TruthValue"
_PrvtCfmMepLckCondition_Object = MibTableColumn
prvtCfmMepLckCondition = _PrvtCfmMepLckCondition_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 131, 1, 7, 1, 1, 3),
    _PrvtCfmMepLckCondition_Type()
)
prvtCfmMepLckCondition.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtCfmMepLckCondition.setStatus("current")


class _PrvtCfmMepAisLifetime_Type(Integer32):
    """Custom type prvtCfmMepAisLifetime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("nolifetime", 0),
          ("lifetime35s", 1),
          ("lifetime35min", 2))
    )


_PrvtCfmMepAisLifetime_Type.__name__ = "Integer32"
_PrvtCfmMepAisLifetime_Object = MibTableColumn
prvtCfmMepAisLifetime = _PrvtCfmMepAisLifetime_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 131, 1, 7, 1, 1, 4),
    _PrvtCfmMepAisLifetime_Type()
)
prvtCfmMepAisLifetime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtCfmMepAisLifetime.setStatus("current")


class _PrvtCfmMepLckLifetime_Type(Integer32):
    """Custom type prvtCfmMepLckLifetime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("nolifetime", 0),
          ("lifetime35s", 1),
          ("lifetime35min", 2))
    )


_PrvtCfmMepLckLifetime_Type.__name__ = "Integer32"
_PrvtCfmMepLckLifetime_Object = MibTableColumn
prvtCfmMepLckLifetime = _PrvtCfmMepLckLifetime_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 131, 1, 7, 1, 1, 5),
    _PrvtCfmMepLckLifetime_Type()
)
prvtCfmMepLckLifetime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtCfmMepLckLifetime.setStatus("current")


class _PrvtCfmMepTransmitMcastLbm_Type(TruthValue):
    """Custom type prvtCfmMepTransmitMcastLbm based on TruthValue"""
    defaultValue = 2


_PrvtCfmMepTransmitMcastLbm_Type.__name__ = "TruthValue"
_PrvtCfmMepTransmitMcastLbm_Object = MibTableColumn
prvtCfmMepTransmitMcastLbm = _PrvtCfmMepTransmitMcastLbm_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 131, 1, 7, 1, 1, 6),
    _PrvtCfmMepTransmitMcastLbm_Type()
)
prvtCfmMepTransmitMcastLbm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prvtCfmMepTransmitMcastLbm.setStatus("current")


class _PrvtCfmMepTransmitLbmInfinite_Type(TruthValue):
    """Custom type prvtCfmMepTransmitLbmInfinite based on TruthValue"""
    defaultValue = 2


_PrvtCfmMepTransmitLbmInfinite_Type.__name__ = "TruthValue"
_PrvtCfmMepTransmitLbmInfinite_Object = MibTableColumn
prvtCfmMepTransmitLbmInfinite = _PrvtCfmMepTransmitLbmInfinite_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 131, 1, 7, 1, 1, 7),
    _PrvtCfmMepTransmitLbmInfinite_Type()
)
prvtCfmMepTransmitLbmInfinite.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prvtCfmMepTransmitLbmInfinite.setStatus("current")


class _PrvtCfmMepTransmitLbmDelay_Type(Unsigned32):
    """Custom type prvtCfmMepTransmitLbmDelay based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 60),
    )


_PrvtCfmMepTransmitLbmDelay_Type.__name__ = "Unsigned32"
_PrvtCfmMepTransmitLbmDelay_Object = MibTableColumn
prvtCfmMepTransmitLbmDelay = _PrvtCfmMepTransmitLbmDelay_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 131, 1, 7, 1, 1, 8),
    _PrvtCfmMepTransmitLbmDelay_Type()
)
prvtCfmMepTransmitLbmDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prvtCfmMepTransmitLbmDelay.setStatus("current")


class _PrvtCfmMepTransmitLbmTimeout_Type(Unsigned32):
    """Custom type prvtCfmMepTransmitLbmTimeout based on Unsigned32"""
    defaultValue = 5

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 60),
    )


_PrvtCfmMepTransmitLbmTimeout_Type.__name__ = "Unsigned32"
_PrvtCfmMepTransmitLbmTimeout_Object = MibTableColumn
prvtCfmMepTransmitLbmTimeout = _PrvtCfmMepTransmitLbmTimeout_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 131, 1, 7, 1, 1, 9),
    _PrvtCfmMepTransmitLbmTimeout_Type()
)
prvtCfmMepTransmitLbmTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prvtCfmMepTransmitLbmTimeout.setStatus("current")


class _PrvtCfmMepTransmitLtmTimeout_Type(Unsigned32):
    """Custom type prvtCfmMepTransmitLtmTimeout based on Unsigned32"""
    defaultValue = 5

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 60),
    )


_PrvtCfmMepTransmitLtmTimeout_Type.__name__ = "Unsigned32"
_PrvtCfmMepTransmitLtmTimeout_Object = MibTableColumn
prvtCfmMepTransmitLtmTimeout = _PrvtCfmMepTransmitLtmTimeout_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 131, 1, 7, 1, 1, 10),
    _PrvtCfmMepTransmitLtmTimeout_Type()
)
prvtCfmMepTransmitLtmTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prvtCfmMepTransmitLtmTimeout.setStatus("current")


class _PrvtCfmMepTransmitLbmSentPkts_Type(Unsigned32):
    """Custom type prvtCfmMepTransmitLbmSentPkts based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_PrvtCfmMepTransmitLbmSentPkts_Type.__name__ = "Unsigned32"
_PrvtCfmMepTransmitLbmSentPkts_Object = MibTableColumn
prvtCfmMepTransmitLbmSentPkts = _PrvtCfmMepTransmitLbmSentPkts_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 131, 1, 7, 1, 1, 11),
    _PrvtCfmMepTransmitLbmSentPkts_Type()
)
prvtCfmMepTransmitLbmSentPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtCfmMepTransmitLbmSentPkts.setStatus("current")


class _PrvtCfmMepTransmitLbmSuccessRate_Type(Unsigned32):
    """Custom type prvtCfmMepTransmitLbmSuccessRate based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10000),
    )


_PrvtCfmMepTransmitLbmSuccessRate_Type.__name__ = "Unsigned32"
_PrvtCfmMepTransmitLbmSuccessRate_Object = MibTableColumn
prvtCfmMepTransmitLbmSuccessRate = _PrvtCfmMepTransmitLbmSuccessRate_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 131, 1, 7, 1, 1, 12),
    _PrvtCfmMepTransmitLbmSuccessRate_Type()
)
prvtCfmMepTransmitLbmSuccessRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtCfmMepTransmitLbmSuccessRate.setStatus("current")
_PrvtCfmMepTransmitLbmMinTime_Type = Unsigned32
_PrvtCfmMepTransmitLbmMinTime_Object = MibTableColumn
prvtCfmMepTransmitLbmMinTime = _PrvtCfmMepTransmitLbmMinTime_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 131, 1, 7, 1, 1, 13),
    _PrvtCfmMepTransmitLbmMinTime_Type()
)
prvtCfmMepTransmitLbmMinTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtCfmMepTransmitLbmMinTime.setStatus("current")
_PrvtCfmMepTransmitLbmAvgTime_Type = Unsigned32
_PrvtCfmMepTransmitLbmAvgTime_Object = MibTableColumn
prvtCfmMepTransmitLbmAvgTime = _PrvtCfmMepTransmitLbmAvgTime_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 131, 1, 7, 1, 1, 14),
    _PrvtCfmMepTransmitLbmAvgTime_Type()
)
prvtCfmMepTransmitLbmAvgTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtCfmMepTransmitLbmAvgTime.setStatus("current")
_PrvtCfmMepTransmitLbmMaxTime_Type = Unsigned32
_PrvtCfmMepTransmitLbmMaxTime_Object = MibTableColumn
prvtCfmMepTransmitLbmMaxTime = _PrvtCfmMepTransmitLbmMaxTime_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 131, 1, 7, 1, 1, 15),
    _PrvtCfmMepTransmitLbmMaxTime_Type()
)
prvtCfmMepTransmitLbmMaxTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtCfmMepTransmitLbmMaxTime.setStatus("current")


class _PrvtCfmMepSuportedRemoteMepsNo_Type(Integer32):
    """Custom type prvtCfmMepSuportedRemoteMepsNo based on Integer32"""
    defaultValue = 8

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(8,
              16,
              24,
              32)
        )
    )
    namedValues = NamedValues(
        *(("remoteMeps8", 8),
          ("remoteMeps16", 16),
          ("remoteMeps24", 24),
          ("remoteMeps32", 32))
    )


_PrvtCfmMepSuportedRemoteMepsNo_Type.__name__ = "Integer32"
_PrvtCfmMepSuportedRemoteMepsNo_Object = MibTableColumn
prvtCfmMepSuportedRemoteMepsNo = _PrvtCfmMepSuportedRemoteMepsNo_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 131, 1, 7, 1, 1, 16),
    _PrvtCfmMepSuportedRemoteMepsNo_Type()
)
prvtCfmMepSuportedRemoteMepsNo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prvtCfmMepSuportedRemoteMepsNo.setStatus("current")


class _PrvtCfmMepExcludeCCMTLV_Type(DisplayString):
    """Custom type prvtCfmMepExcludeCCMTLV based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )
    fixed_length = 2


_PrvtCfmMepExcludeCCMTLV_Type.__name__ = "DisplayString"
_PrvtCfmMepExcludeCCMTLV_Object = MibTableColumn
prvtCfmMepExcludeCCMTLV = _PrvtCfmMepExcludeCCMTLV_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 131, 1, 7, 1, 1, 17),
    _PrvtCfmMepExcludeCCMTLV_Type()
)
prvtCfmMepExcludeCCMTLV.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prvtCfmMepExcludeCCMTLV.setStatus("current")
_PrvtCfmLbrTable_Object = MibTable
prvtCfmLbrTable = _PrvtCfmLbrTable_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 131, 1, 7, 2)
)
if mibBuilder.loadTexts:
    prvtCfmLbrTable.setStatus("current")
_PrvtCfmLbrEntry_Object = MibTableRow
prvtCfmLbrEntry = _PrvtCfmLbrEntry_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 131, 1, 7, 2, 1)
)
prvtCfmLbrEntry.setIndexNames(
    (0, "IEEE8021-CFM-MIB", "dot1agCfmMdIndex"),
    (0, "IEEE8021-CFM-MIB", "dot1agCfmMaIndex"),
    (0, "IEEE8021-CFM-MIB", "dot1agCfmMepIdentifier"),
    (0, "PRVT-CFM-MIB", "prvtCfmLbrSeqNumber"),
    (0, "PRVT-CFM-MIB", "prvtCfmLbrReceiveOrder"),
)
if mibBuilder.loadTexts:
    prvtCfmLbrEntry.setStatus("current")


class _PrvtCfmLbrSeqNumber_Type(Unsigned32):
    """Custom type prvtCfmLbrSeqNumber based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_PrvtCfmLbrSeqNumber_Type.__name__ = "Unsigned32"
_PrvtCfmLbrSeqNumber_Object = MibTableColumn
prvtCfmLbrSeqNumber = _PrvtCfmLbrSeqNumber_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 131, 1, 7, 2, 1, 1),
    _PrvtCfmLbrSeqNumber_Type()
)
prvtCfmLbrSeqNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    prvtCfmLbrSeqNumber.setStatus("current")


class _PrvtCfmLbrReceiveOrder_Type(Unsigned32):
    """Custom type prvtCfmLbrReceiveOrder based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_PrvtCfmLbrReceiveOrder_Type.__name__ = "Unsigned32"
_PrvtCfmLbrReceiveOrder_Object = MibTableColumn
prvtCfmLbrReceiveOrder = _PrvtCfmLbrReceiveOrder_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 131, 1, 7, 2, 1, 2),
    _PrvtCfmLbrReceiveOrder_Type()
)
prvtCfmLbrReceiveOrder.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    prvtCfmLbrReceiveOrder.setStatus("current")
_PrvtCfmLbrTime_Type = Unsigned32
_PrvtCfmLbrTime_Object = MibTableColumn
prvtCfmLbrTime = _PrvtCfmLbrTime_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 131, 1, 7, 2, 1, 3),
    _PrvtCfmLbrTime_Type()
)
prvtCfmLbrTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtCfmLbrTime.setStatus("current")
_PrvtCfmLbrMacAddress_Type = MacAddress
_PrvtCfmLbrMacAddress_Object = MibTableColumn
prvtCfmLbrMacAddress = _PrvtCfmLbrMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 131, 1, 7, 2, 1, 4),
    _PrvtCfmLbrMacAddress_Type()
)
prvtCfmLbrMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtCfmLbrMacAddress.setStatus("current")
_PrvtCfmLbrBadMsdu_Type = TruthValue
_PrvtCfmLbrBadMsdu_Object = MibTableColumn
prvtCfmLbrBadMsdu = _PrvtCfmLbrBadMsdu_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 131, 1, 7, 2, 1, 5),
    _PrvtCfmLbrBadMsdu_Type()
)
prvtCfmLbrBadMsdu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtCfmLbrBadMsdu.setStatus("current")
_PrvtCfmLtrTable_Object = MibTable
prvtCfmLtrTable = _PrvtCfmLtrTable_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 131, 1, 7, 3)
)
if mibBuilder.loadTexts:
    prvtCfmLtrTable.setStatus("current")
_PrvtCfmLtrEntry_Object = MibTableRow
prvtCfmLtrEntry = _PrvtCfmLtrEntry_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 131, 1, 7, 3, 1)
)
if mibBuilder.loadTexts:
    prvtCfmLtrEntry.setStatus("current")
_PrvtCfmLtrTime_Type = Unsigned32
_PrvtCfmLtrTime_Object = MibTableColumn
prvtCfmLtrTime = _PrvtCfmLtrTime_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 131, 1, 7, 3, 1, 1),
    _PrvtCfmLtrTime_Type()
)
prvtCfmLtrTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtCfmLtrTime.setStatus("current")
_PrvtCfmMaAisLckVlan_ObjectIdentity = ObjectIdentity
prvtCfmMaAisLckVlan = _PrvtCfmMaAisLckVlan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 131, 1, 8)
)
_PrvtCfmMaAisLckVlanTable_Object = MibTable
prvtCfmMaAisLckVlanTable = _PrvtCfmMaAisLckVlanTable_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 131, 1, 8, 1)
)
if mibBuilder.loadTexts:
    prvtCfmMaAisLckVlanTable.setStatus("current")
_PrvtCfmMaAisLckVlanEntry_Object = MibTableRow
prvtCfmMaAisLckVlanEntry = _PrvtCfmMaAisLckVlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 131, 1, 8, 1, 1)
)
prvtCfmMaAisLckVlanEntry.setIndexNames(
    (0, "IEEE8021-CFM-MIB", "dot1agCfmMdIndex"),
    (0, "IEEE8021-CFM-MIB", "dot1agCfmMaIndex"),
    (0, "PRVT-CFM-MIB", "prvtCfmMaAisLckVlanId"),
)
if mibBuilder.loadTexts:
    prvtCfmMaAisLckVlanEntry.setStatus("current")
_PrvtCfmMaAisLckVlanId_Type = VlanId
_PrvtCfmMaAisLckVlanId_Object = MibTableColumn
prvtCfmMaAisLckVlanId = _PrvtCfmMaAisLckVlanId_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 131, 1, 8, 1, 1, 1),
    _PrvtCfmMaAisLckVlanId_Type()
)
prvtCfmMaAisLckVlanId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prvtCfmMaAisLckVlanId.setStatus("current")
_PrvtCfmMaAisLckVlanRowStatus_Type = RowStatus
_PrvtCfmMaAisLckVlanRowStatus_Object = MibTableColumn
prvtCfmMaAisLckVlanRowStatus = _PrvtCfmMaAisLckVlanRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 131, 1, 8, 1, 1, 2),
    _PrvtCfmMaAisLckVlanRowStatus_Type()
)
prvtCfmMaAisLckVlanRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    prvtCfmMaAisLckVlanRowStatus.setStatus("current")
_PrvtCfmMibConformance_ObjectIdentity = ObjectIdentity
prvtCfmMibConformance = _PrvtCfmMibConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 131, 2)
)
dot1agCfmMaCompEntry.registerAugmentions(
    ("PRVT-CFM-MIB",
     "prvtCfmMaEntry")
)
prvtCfmMaEntry.setIndexNames(*dot1agCfmMaCompEntry.getIndexNames())
dot1agCfmMepEntry.registerAugmentions(
    ("PRVT-CFM-MIB",
     "prvtCfmMepEntry")
)
prvtCfmMepEntry.setIndexNames(*dot1agCfmMepEntry.getIndexNames())
dot1agCfmLtrEntry.registerAugmentions(
    ("PRVT-CFM-MIB",
     "prvtCfmLtrEntry")
)
prvtCfmLtrEntry.setIndexNames(*dot1agCfmLtrEntry.getIndexNames())

# Managed Objects groups


# Notification objects

prvtCfm1wJitterThreshold = NotificationType(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 131, 0, 1)
)
prvtCfm1wJitterThreshold.setObjects(
      *(("PRVT-CFM-MIB", "prvtCfmProcessResultOneWayJitter"),
        ("PRVT-CFM-MIB", "prvtCfmProfile1wJitterWarning"),
        ("PRVT-CFM-MIB", "prvtCfmProfile1wJitterError"))
)
if mibBuilder.loadTexts:
    prvtCfm1wJitterThreshold.setStatus(
        "current"
    )

prvtCfmJitterThreshold = NotificationType(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 131, 0, 2)
)
prvtCfmJitterThreshold.setObjects(
      *(("PRVT-CFM-MIB", "prvtCfmProcessResultTwoWayJitter"),
        ("PRVT-CFM-MIB", "prvtCfmProfileJitterWarning"),
        ("PRVT-CFM-MIB", "prvtCfmProfileJitterWarningPeriod"),
        ("PRVT-CFM-MIB", "prvtCfmProfileJitterError"),
        ("PRVT-CFM-MIB", "prvtCfmProfileJitterErrorPeriod"))
)
if mibBuilder.loadTexts:
    prvtCfmJitterThreshold.setStatus(
        "current"
    )

prvtCfmFrameLossThreshold = NotificationType(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 131, 0, 3)
)
prvtCfmFrameLossThreshold.setObjects(
      *(("PRVT-CFM-MIB", "prvtCfmProcessResultFrameloss"),
        ("PRVT-CFM-MIB", "prvtCfmProfileFrameLossWarning"),
        ("PRVT-CFM-MIB", "prvtCfmProfileFrameLossError"))
)
if mibBuilder.loadTexts:
    prvtCfmFrameLossThreshold.setStatus(
        "current"
    )

prvtCfmLatencyThreshold = NotificationType(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 131, 0, 4)
)
prvtCfmLatencyThreshold.setObjects(
      *(("PRVT-CFM-MIB", "prvtCfmProcessResultLatency"),
        ("PRVT-CFM-MIB", "prvtCfmProfileLatencyWarning"),
        ("PRVT-CFM-MIB", "prvtCfmProfileLatencyWarningPeriod"),
        ("PRVT-CFM-MIB", "prvtCfmProfileLatencyError"),
        ("PRVT-CFM-MIB", "prvtCfmProfileLatencyErrorPeriod"))
)
if mibBuilder.loadTexts:
    prvtCfmLatencyThreshold.setStatus(
        "current"
    )

prvtCfmAisReceived = NotificationType(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 131, 0, 5)
)
prvtCfmAisReceived.setObjects(
    ("PRVT-CFM-MIB", "prvtCfmMepAisLifetime")
)
if mibBuilder.loadTexts:
    prvtCfmAisReceived.setStatus(
        "current"
    )

prvtCfmLckReceived = NotificationType(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 131, 0, 6)
)
prvtCfmLckReceived.setObjects(
    ("PRVT-CFM-MIB", "prvtCfmMepLckLifetime")
)
if mibBuilder.loadTexts:
    prvtCfmLckReceived.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "PRVT-CFM-MIB",
    **{"prvtCfmMib": prvtCfmMib,
       "prvtCfmMibNotifications": prvtCfmMibNotifications,
       "prvtCfm1wJitterThreshold": prvtCfm1wJitterThreshold,
       "prvtCfmJitterThreshold": prvtCfmJitterThreshold,
       "prvtCfmFrameLossThreshold": prvtCfmFrameLossThreshold,
       "prvtCfmLatencyThreshold": prvtCfmLatencyThreshold,
       "prvtCfmAisReceived": prvtCfmAisReceived,
       "prvtCfmLckReceived": prvtCfmLckReceived,
       "prvtCfmMibObjects": prvtCfmMibObjects,
       "prvtCfmUpdateInterval": prvtCfmUpdateInterval,
       "prvtCfmStatus": prvtCfmStatus,
       "prvtCfmProfile": prvtCfmProfile,
       "prvtCfmProfileTableNextIndex": prvtCfmProfileTableNextIndex,
       "prvtCfmProfileTable": prvtCfmProfileTable,
       "prvtCfmProfileEntry": prvtCfmProfileEntry,
       "prvtCfmProfileIndex": prvtCfmProfileIndex,
       "prvtCfmProfileName": prvtCfmProfileName,
       "prvtCfmProfilePriority": prvtCfmProfilePriority,
       "prvtCfmProfileRate": prvtCfmProfileRate,
       "prvtCfmProfileSize": prvtCfmProfileSize,
       "prvtCfmProfileBucketSize": prvtCfmProfileBucketSize,
       "prvtCfmProfile1wJitterError": prvtCfmProfile1wJitterError,
       "prvtCfmProfile1wJitterWarning": prvtCfmProfile1wJitterWarning,
       "prvtCfmProfileJitterError": prvtCfmProfileJitterError,
       "prvtCfmProfileJitterErrorPeriod": prvtCfmProfileJitterErrorPeriod,
       "prvtCfmProfileJitterWarning": prvtCfmProfileJitterWarning,
       "prvtCfmProfileJitterWarningPeriod": prvtCfmProfileJitterWarningPeriod,
       "prvtCfmProfileFrameLossError": prvtCfmProfileFrameLossError,
       "prvtCfmProfileFrameLossWarning": prvtCfmProfileFrameLossWarning,
       "prvtCfmProfileLatencyError": prvtCfmProfileLatencyError,
       "prvtCfmProfileLatencyErrorPeriod": prvtCfmProfileLatencyErrorPeriod,
       "prvtCfmProfileLatencyWarning": prvtCfmProfileLatencyWarning,
       "prvtCfmProfileLatencyWarningPeriod": prvtCfmProfileLatencyWarningPeriod,
       "prvtCfmProfileRowStatus": prvtCfmProfileRowStatus,
       "prvtCfmProfile1wJitterEnable": prvtCfmProfile1wJitterEnable,
       "prvtCfmProfileJitterEnable": prvtCfmProfileJitterEnable,
       "prvtCfmProfileFrameLossEnable": prvtCfmProfileFrameLossEnable,
       "prvtCfmProfileLatencyEnable": prvtCfmProfileLatencyEnable,
       "prvtCfmProcess": prvtCfmProcess,
       "prvtCfmProcessTableNextIndex": prvtCfmProcessTableNextIndex,
       "prvtCfmProcessTable": prvtCfmProcessTable,
       "prvtCfmProcessEntry": prvtCfmProcessEntry,
       "prvtCfmProcessIndex": prvtCfmProcessIndex,
       "prvtCfmProcessProfileIndex": prvtCfmProcessProfileIndex,
       "prvtCfmProcessName": prvtCfmProcessName,
       "prvtCfmProcessStatus": prvtCfmProcessStatus,
       "prvtCfmProcessRepeatInterval": prvtCfmProcessRepeatInterval,
       "prvtCfmProcessPacketType": prvtCfmProcessPacketType,
       "prvtCfmProcessUnreturnedPkts": prvtCfmProcessUnreturnedPkts,
       "prvtCfmProcessRowStatus": prvtCfmProcessRowStatus,
       "prvtCfmProcessResult": prvtCfmProcessResult,
       "prvtCfmProcessResultTable": prvtCfmProcessResultTable,
       "prvtCfmProcessResultEntry": prvtCfmProcessResultEntry,
       "prvtCfmProcessResultOneWayJitter": prvtCfmProcessResultOneWayJitter,
       "prvtCfmProcessResultTwoWayJitter": prvtCfmProcessResultTwoWayJitter,
       "prvtCfmProcessResultLatency": prvtCfmProcessResultLatency,
       "prvtCfmProcessResultFrameloss": prvtCfmProcessResultFrameloss,
       "prvtCfmMa": prvtCfmMa,
       "prvtCfmMaTable": prvtCfmMaTable,
       "prvtCfmMaEntry": prvtCfmMaEntry,
       "prvtCfmMaCompAisLckEnabled": prvtCfmMaCompAisLckEnabled,
       "prvtCfmMaCompAisLckLevel": prvtCfmMaCompAisLckLevel,
       "prvtCfmMaCompAisLckInterval": prvtCfmMaCompAisLckInterval,
       "prvtCfmMaCompAisLckPriority": prvtCfmMaCompAisLckPriority,
       "prvtCfmMaCompServiceId": prvtCfmMaCompServiceId,
       "prvtCfmMaCompNumberOfServices": prvtCfmMaCompNumberOfServices,
       "prvtCfmMaCompClearConnectivity": prvtCfmMaCompClearConnectivity,
       "prvtCfmMep": prvtCfmMep,
       "prvtCfmMepTable": prvtCfmMepTable,
       "prvtCfmMepEntry": prvtCfmMepEntry,
       "prvtCfmMepAlarmSupressed": prvtCfmMepAlarmSupressed,
       "prvtCfmMepAisCondition": prvtCfmMepAisCondition,
       "prvtCfmMepLckCondition": prvtCfmMepLckCondition,
       "prvtCfmMepAisLifetime": prvtCfmMepAisLifetime,
       "prvtCfmMepLckLifetime": prvtCfmMepLckLifetime,
       "prvtCfmMepTransmitMcastLbm": prvtCfmMepTransmitMcastLbm,
       "prvtCfmMepTransmitLbmInfinite": prvtCfmMepTransmitLbmInfinite,
       "prvtCfmMepTransmitLbmDelay": prvtCfmMepTransmitLbmDelay,
       "prvtCfmMepTransmitLbmTimeout": prvtCfmMepTransmitLbmTimeout,
       "prvtCfmMepTransmitLtmTimeout": prvtCfmMepTransmitLtmTimeout,
       "prvtCfmMepTransmitLbmSentPkts": prvtCfmMepTransmitLbmSentPkts,
       "prvtCfmMepTransmitLbmSuccessRate": prvtCfmMepTransmitLbmSuccessRate,
       "prvtCfmMepTransmitLbmMinTime": prvtCfmMepTransmitLbmMinTime,
       "prvtCfmMepTransmitLbmAvgTime": prvtCfmMepTransmitLbmAvgTime,
       "prvtCfmMepTransmitLbmMaxTime": prvtCfmMepTransmitLbmMaxTime,
       "prvtCfmMepSuportedRemoteMepsNo": prvtCfmMepSuportedRemoteMepsNo,
       "prvtCfmMepExcludeCCMTLV": prvtCfmMepExcludeCCMTLV,
       "prvtCfmLbrTable": prvtCfmLbrTable,
       "prvtCfmLbrEntry": prvtCfmLbrEntry,
       "prvtCfmLbrSeqNumber": prvtCfmLbrSeqNumber,
       "prvtCfmLbrReceiveOrder": prvtCfmLbrReceiveOrder,
       "prvtCfmLbrTime": prvtCfmLbrTime,
       "prvtCfmLbrMacAddress": prvtCfmLbrMacAddress,
       "prvtCfmLbrBadMsdu": prvtCfmLbrBadMsdu,
       "prvtCfmLtrTable": prvtCfmLtrTable,
       "prvtCfmLtrEntry": prvtCfmLtrEntry,
       "prvtCfmLtrTime": prvtCfmLtrTime,
       "prvtCfmMaAisLckVlan": prvtCfmMaAisLckVlan,
       "prvtCfmMaAisLckVlanTable": prvtCfmMaAisLckVlanTable,
       "prvtCfmMaAisLckVlanEntry": prvtCfmMaAisLckVlanEntry,
       "prvtCfmMaAisLckVlanId": prvtCfmMaAisLckVlanId,
       "prvtCfmMaAisLckVlanRowStatus": prvtCfmMaAisLckVlanRowStatus,
       "prvtCfmMibConformance": prvtCfmMibConformance}
)
