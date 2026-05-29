# SNMP MIB module (PERFORMANCE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\sagemcom\PERFORMANCE-MIB

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

(IntDateTime,) = mibBuilder.importSymbols(
    "EQUIPMENT-MIB",
    "IntDateTime")

(sagemDr,) = mibBuilder.importSymbols(
    "SAGEM-DR-MIB",
    "sagemDr")

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

performance = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 1038, 102)
)


# Types definitions



class NearFar(Integer32):
    """Custom type NearFar based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("near", 1),
          ("far", 2))
    )




# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_PerfTraps_ObjectIdentity = ObjectIdentity
perfTraps = _PerfTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1038, 102, 0)
)
_PerfClear_Type = ObjectIdentifier
_PerfClear_Object = MibScalar
perfClear = _PerfClear_Object(
    (1, 3, 6, 1, 4, 1, 1038, 102, 1),
    _PerfClear_Type()
)
perfClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    perfClear.setStatus("current")


class _CptNumber_Type(Integer32):
    """Custom type cptNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CptNumber_Type.__name__ = "Integer32"
_CptNumber_Object = MibScalar
cptNumber = _CptNumber_Object(
    (1, 3, 6, 1, 4, 1, 1038, 102, 2),
    _CptNumber_Type()
)
cptNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cptNumber.setStatus("current")
_CptTable_Object = MibTable
cptTable = _CptTable_Object(
    (1, 3, 6, 1, 4, 1, 1038, 102, 3)
)
if mibBuilder.loadTexts:
    cptTable.setStatus("current")
_CptEntry_Object = MibTableRow
cptEntry = _CptEntry_Object(
    (1, 3, 6, 1, 4, 1, 1038, 102, 3, 1)
)
cptEntry.setIndexNames(
    (0, "PERFORMANCE-MIB", "cptObject"),
    (0, "PERFORMANCE-MIB", "cptNearFar"),
    (0, "PERFORMANCE-MIB", "cptDuration"),
    (0, "PERFORMANCE-MIB", "cptDate"),
)
if mibBuilder.loadTexts:
    cptEntry.setStatus("current")
_CptObject_Type = ObjectIdentifier
_CptObject_Object = MibTableColumn
cptObject = _CptObject_Object(
    (1, 3, 6, 1, 4, 1, 1038, 102, 3, 1, 1),
    _CptObject_Type()
)
cptObject.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cptObject.setStatus("current")


class _CptName_Type(DisplayString):
    """Custom type cptName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_CptName_Type.__name__ = "DisplayString"
_CptName_Object = MibTableColumn
cptName = _CptName_Object(
    (1, 3, 6, 1, 4, 1, 1038, 102, 3, 1, 2),
    _CptName_Type()
)
cptName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cptName.setStatus("current")
_CptNearFar_Type = NearFar
_CptNearFar_Object = MibTableColumn
cptNearFar = _CptNearFar_Object(
    (1, 3, 6, 1, 4, 1, 1038, 102, 3, 1, 3),
    _CptNearFar_Type()
)
cptNearFar.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cptNearFar.setStatus("current")
_CptDuration_Type = TimeTicks
_CptDuration_Object = MibTableColumn
cptDuration = _CptDuration_Object(
    (1, 3, 6, 1, 4, 1, 1038, 102, 3, 1, 4),
    _CptDuration_Type()
)
cptDuration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cptDuration.setStatus("current")
_CptDate_Type = IntDateTime
_CptDate_Object = MibTableColumn
cptDate = _CptDate_Object(
    (1, 3, 6, 1, 4, 1, 1038, 102, 3, 1, 5),
    _CptDate_Type()
)
cptDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cptDate.setStatus("current")
_CptUAS_Type = Gauge32
_CptUAS_Object = MibTableColumn
cptUAS = _CptUAS_Object(
    (1, 3, 6, 1, 4, 1, 1038, 102, 3, 1, 6),
    _CptUAS_Type()
)
cptUAS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cptUAS.setStatus("current")
_CptSES_Type = Gauge32
_CptSES_Object = MibTableColumn
cptSES = _CptSES_Object(
    (1, 3, 6, 1, 4, 1, 1038, 102, 3, 1, 7),
    _CptSES_Type()
)
cptSES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cptSES.setStatus("current")
_CptES_Type = Gauge32
_CptES_Object = MibTableColumn
cptES = _CptES_Object(
    (1, 3, 6, 1, 4, 1, 1038, 102, 3, 1, 8),
    _CptES_Type()
)
cptES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cptES.setStatus("current")
_CptBBE_Type = Gauge32
_CptBBE_Object = MibTableColumn
cptBBE = _CptBBE_Object(
    (1, 3, 6, 1, 4, 1, 1038, 102, 3, 1, 9),
    _CptBBE_Type()
)
cptBBE.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cptBBE.setStatus("current")


class _UapNumber_Type(Integer32):
    """Custom type uapNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_UapNumber_Type.__name__ = "Integer32"
_UapNumber_Object = MibScalar
uapNumber = _UapNumber_Object(
    (1, 3, 6, 1, 4, 1, 1038, 102, 4),
    _UapNumber_Type()
)
uapNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uapNumber.setStatus("current")
_UapTable_Object = MibTable
uapTable = _UapTable_Object(
    (1, 3, 6, 1, 4, 1, 1038, 102, 5)
)
if mibBuilder.loadTexts:
    uapTable.setStatus("current")
_UapEntry_Object = MibTableRow
uapEntry = _UapEntry_Object(
    (1, 3, 6, 1, 4, 1, 1038, 102, 5, 1)
)
uapEntry.setIndexNames(
    (0, "PERFORMANCE-MIB", "uapObject"),
    (0, "PERFORMANCE-MIB", "uapNearFar"),
    (0, "PERFORMANCE-MIB", "uapBegin"),
)
if mibBuilder.loadTexts:
    uapEntry.setStatus("current")
_UapObject_Type = ObjectIdentifier
_UapObject_Object = MibTableColumn
uapObject = _UapObject_Object(
    (1, 3, 6, 1, 4, 1, 1038, 102, 5, 1, 1),
    _UapObject_Type()
)
uapObject.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uapObject.setStatus("current")


class _UapName_Type(DisplayString):
    """Custom type uapName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_UapName_Type.__name__ = "DisplayString"
_UapName_Object = MibTableColumn
uapName = _UapName_Object(
    (1, 3, 6, 1, 4, 1, 1038, 102, 5, 1, 2),
    _UapName_Type()
)
uapName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uapName.setStatus("current")
_UapNearFar_Type = NearFar
_UapNearFar_Object = MibTableColumn
uapNearFar = _UapNearFar_Object(
    (1, 3, 6, 1, 4, 1, 1038, 102, 5, 1, 3),
    _UapNearFar_Type()
)
uapNearFar.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uapNearFar.setStatus("current")
_UapBegin_Type = IntDateTime
_UapBegin_Object = MibTableColumn
uapBegin = _UapBegin_Object(
    (1, 3, 6, 1, 4, 1, 1038, 102, 5, 1, 4),
    _UapBegin_Type()
)
uapBegin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uapBegin.setStatus("current")
_UapEnd_Type = IntDateTime
_UapEnd_Object = MibTableColumn
uapEnd = _UapEnd_Object(
    (1, 3, 6, 1, 4, 1, 1038, 102, 5, 1, 5),
    _UapEnd_Type()
)
uapEnd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uapEnd.setStatus("current")


class _ThresholdNumber_Type(Integer32):
    """Custom type thresholdNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_ThresholdNumber_Type.__name__ = "Integer32"
_ThresholdNumber_Object = MibScalar
thresholdNumber = _ThresholdNumber_Object(
    (1, 3, 6, 1, 4, 1, 1038, 102, 6),
    _ThresholdNumber_Type()
)
thresholdNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    thresholdNumber.setStatus("current")
_ThresholdTable_Object = MibTable
thresholdTable = _ThresholdTable_Object(
    (1, 3, 6, 1, 4, 1, 1038, 102, 7)
)
if mibBuilder.loadTexts:
    thresholdTable.setStatus("current")
_ThresholdEntry_Object = MibTableRow
thresholdEntry = _ThresholdEntry_Object(
    (1, 3, 6, 1, 4, 1, 1038, 102, 7, 1)
)
thresholdEntry.setIndexNames(
    (0, "PERFORMANCE-MIB", "thresholdObject"),
    (0, "PERFORMANCE-MIB", "thresholdNearFar"),
    (0, "PERFORMANCE-MIB", "thresholdDuration"),
    (0, "PERFORMANCE-MIB", "thresholdType"),
)
if mibBuilder.loadTexts:
    thresholdEntry.setStatus("current")
_ThresholdObject_Type = ObjectIdentifier
_ThresholdObject_Object = MibTableColumn
thresholdObject = _ThresholdObject_Object(
    (1, 3, 6, 1, 4, 1, 1038, 102, 7, 1, 1),
    _ThresholdObject_Type()
)
thresholdObject.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    thresholdObject.setStatus("current")


class _ThresholdName_Type(DisplayString):
    """Custom type thresholdName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_ThresholdName_Type.__name__ = "DisplayString"
_ThresholdName_Object = MibTableColumn
thresholdName = _ThresholdName_Object(
    (1, 3, 6, 1, 4, 1, 1038, 102, 7, 1, 2),
    _ThresholdName_Type()
)
thresholdName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    thresholdName.setStatus("current")
_ThresholdNearFar_Type = NearFar
_ThresholdNearFar_Object = MibTableColumn
thresholdNearFar = _ThresholdNearFar_Object(
    (1, 3, 6, 1, 4, 1, 1038, 102, 7, 1, 3),
    _ThresholdNearFar_Type()
)
thresholdNearFar.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    thresholdNearFar.setStatus("current")
_ThresholdDuration_Type = TimeTicks
_ThresholdDuration_Object = MibTableColumn
thresholdDuration = _ThresholdDuration_Object(
    (1, 3, 6, 1, 4, 1, 1038, 102, 7, 1, 4),
    _ThresholdDuration_Type()
)
thresholdDuration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    thresholdDuration.setStatus("current")


class _ThresholdType_Type(Integer32):
    """Custom type thresholdType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("raise", 1),
          ("clear", 2))
    )


_ThresholdType_Type.__name__ = "Integer32"
_ThresholdType_Object = MibTableColumn
thresholdType = _ThresholdType_Object(
    (1, 3, 6, 1, 4, 1, 1038, 102, 7, 1, 5),
    _ThresholdType_Type()
)
thresholdType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    thresholdType.setStatus("current")


class _ThresholdUas_Type(Integer32):
    """Custom type thresholdUas based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_ThresholdUas_Type.__name__ = "Integer32"
_ThresholdUas_Object = MibTableColumn
thresholdUas = _ThresholdUas_Object(
    (1, 3, 6, 1, 4, 1, 1038, 102, 7, 1, 6),
    _ThresholdUas_Type()
)
thresholdUas.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    thresholdUas.setStatus("current")


class _ThresholdSes_Type(Integer32):
    """Custom type thresholdSes based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_ThresholdSes_Type.__name__ = "Integer32"
_ThresholdSes_Object = MibTableColumn
thresholdSes = _ThresholdSes_Object(
    (1, 3, 6, 1, 4, 1, 1038, 102, 7, 1, 7),
    _ThresholdSes_Type()
)
thresholdSes.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    thresholdSes.setStatus("current")


class _ThresholdEs_Type(Integer32):
    """Custom type thresholdEs based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_ThresholdEs_Type.__name__ = "Integer32"
_ThresholdEs_Object = MibTableColumn
thresholdEs = _ThresholdEs_Object(
    (1, 3, 6, 1, 4, 1, 1038, 102, 7, 1, 8),
    _ThresholdEs_Type()
)
thresholdEs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    thresholdEs.setStatus("current")


class _ThresholdBbe_Type(Integer32):
    """Custom type thresholdBbe based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_ThresholdBbe_Type.__name__ = "Integer32"
_ThresholdBbe_Object = MibTableColumn
thresholdBbe = _ThresholdBbe_Object(
    (1, 3, 6, 1, 4, 1, 1038, 102, 7, 1, 9),
    _ThresholdBbe_Type()
)
thresholdBbe.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    thresholdBbe.setStatus("current")

# Managed Objects groups


# Notification objects

qualityTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 1038, 102, 0, 2)
)
qualityTrap.setObjects(
      *(("PERFORMANCE-MIB", "cptObject"),
        ("PERFORMANCE-MIB", "cptName"),
        ("PERFORMANCE-MIB", "cptNearFar"),
        ("PERFORMANCE-MIB", "cptDuration"),
        ("PERFORMANCE-MIB", "cptDate"),
        ("PERFORMANCE-MIB", "cptUAS"),
        ("PERFORMANCE-MIB", "cptSES"),
        ("PERFORMANCE-MIB", "cptES"),
        ("PERFORMANCE-MIB", "cptBBE"))
)
if mibBuilder.loadTexts:
    qualityTrap.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "PERFORMANCE-MIB",
    **{"NearFar": NearFar,
       "performance": performance,
       "perfTraps": perfTraps,
       "qualityTrap": qualityTrap,
       "perfClear": perfClear,
       "cptNumber": cptNumber,
       "cptTable": cptTable,
       "cptEntry": cptEntry,
       "cptObject": cptObject,
       "cptName": cptName,
       "cptNearFar": cptNearFar,
       "cptDuration": cptDuration,
       "cptDate": cptDate,
       "cptUAS": cptUAS,
       "cptSES": cptSES,
       "cptES": cptES,
       "cptBBE": cptBBE,
       "uapNumber": uapNumber,
       "uapTable": uapTable,
       "uapEntry": uapEntry,
       "uapObject": uapObject,
       "uapName": uapName,
       "uapNearFar": uapNearFar,
       "uapBegin": uapBegin,
       "uapEnd": uapEnd,
       "thresholdNumber": thresholdNumber,
       "thresholdTable": thresholdTable,
       "thresholdEntry": thresholdEntry,
       "thresholdObject": thresholdObject,
       "thresholdName": thresholdName,
       "thresholdNearFar": thresholdNearFar,
       "thresholdDuration": thresholdDuration,
       "thresholdType": thresholdType,
       "thresholdUas": thresholdUas,
       "thresholdSes": thresholdSes,
       "thresholdEs": thresholdEs,
       "thresholdBbe": thresholdBbe}
)
