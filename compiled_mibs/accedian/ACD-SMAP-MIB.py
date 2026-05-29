# SNMP MIB module (ACD-SMAP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\accedian\ACD-SMAP-MIB

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

(acdMibs,) = mibBuilder.importSymbols(
    "ACCEDIAN-SMI",
    "acdMibs")

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

acdSmap = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 22420, 2, 8)
)
if mibBuilder.loadTexts:
    acdSmap.setRevisions(
        ("2013-05-11 01:00",
         "2008-10-01 01:00",
         "2008-06-15 01:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AcdSmapNotifications_ObjectIdentity = ObjectIdentity
acdSmapNotifications = _AcdSmapNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22420, 2, 8, 0)
)
_AcdSmapMIBObjects_ObjectIdentity = ObjectIdentity
acdSmapMIBObjects = _AcdSmapMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22420, 2, 8, 1)
)
_AcdSmapConfig_ObjectIdentity = ObjectIdentity
acdSmapConfig = _AcdSmapConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22420, 2, 8, 1, 1)
)
_AcdSmapCoSProfTable_Object = MibTable
acdSmapCoSProfTable = _AcdSmapCoSProfTable_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 8, 1, 1, 1)
)
if mibBuilder.loadTexts:
    acdSmapCoSProfTable.setStatus("current")
_AcdSmapCoSProfEntry_Object = MibTableRow
acdSmapCoSProfEntry = _AcdSmapCoSProfEntry_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 8, 1, 1, 1, 1)
)
acdSmapCoSProfEntry.setIndexNames(
    (0, "ACD-SMAP-MIB", "acdSmapCoSProfID"),
)
if mibBuilder.loadTexts:
    acdSmapCoSProfEntry.setStatus("current")
_AcdSmapCoSProfID_Type = Unsigned32
_AcdSmapCoSProfID_Object = MibTableColumn
acdSmapCoSProfID = _AcdSmapCoSProfID_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 8, 1, 1, 1, 1, 1),
    _AcdSmapCoSProfID_Type()
)
acdSmapCoSProfID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    acdSmapCoSProfID.setStatus("current")
_AcdSmapCoSProfRowStatus_Type = RowStatus
_AcdSmapCoSProfRowStatus_Object = MibTableColumn
acdSmapCoSProfRowStatus = _AcdSmapCoSProfRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 8, 1, 1, 1, 1, 2),
    _AcdSmapCoSProfRowStatus_Type()
)
acdSmapCoSProfRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acdSmapCoSProfRowStatus.setStatus("current")


class _AcdSmapCoSProfName_Type(DisplayString):
    """Custom type acdSmapCoSProfName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_AcdSmapCoSProfName_Type.__name__ = "DisplayString"
_AcdSmapCoSProfName_Object = MibTableColumn
acdSmapCoSProfName = _AcdSmapCoSProfName_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 8, 1, 1, 1, 1, 3),
    _AcdSmapCoSProfName_Type()
)
acdSmapCoSProfName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acdSmapCoSProfName.setStatus("current")


class _AcdSmapCoSProfType_Type(Integer32):
    """Custom type acdSmapCoSProfType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("pcp", 1),
          ("dscp", 2),
          ("pre", 3))
    )


_AcdSmapCoSProfType_Type.__name__ = "Integer32"
_AcdSmapCoSProfType_Object = MibTableColumn
acdSmapCoSProfType = _AcdSmapCoSProfType_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 8, 1, 1, 1, 1, 4),
    _AcdSmapCoSProfType_Type()
)
acdSmapCoSProfType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acdSmapCoSProfType.setStatus("current")


class _AcdSmapCoSProfDecodeDropBit_Type(TruthValue):
    """Custom type acdSmapCoSProfDecodeDropBit based on TruthValue"""
    defaultValue = 2


_AcdSmapCoSProfDecodeDropBit_Type.__name__ = "TruthValue"
_AcdSmapCoSProfDecodeDropBit_Object = MibTableColumn
acdSmapCoSProfDecodeDropBit = _AcdSmapCoSProfDecodeDropBit_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 8, 1, 1, 1, 1, 5),
    _AcdSmapCoSProfDecodeDropBit_Type()
)
acdSmapCoSProfDecodeDropBit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acdSmapCoSProfDecodeDropBit.setStatus("current")


class _AcdSmapCoSProfEncodeDropBit_Type(TruthValue):
    """Custom type acdSmapCoSProfEncodeDropBit based on TruthValue"""
    defaultValue = 2


_AcdSmapCoSProfEncodeDropBit_Type.__name__ = "TruthValue"
_AcdSmapCoSProfEncodeDropBit_Object = MibTableColumn
acdSmapCoSProfEncodeDropBit = _AcdSmapCoSProfEncodeDropBit_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 8, 1, 1, 1, 1, 6),
    _AcdSmapCoSProfEncodeDropBit_Type()
)
acdSmapCoSProfEncodeDropBit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acdSmapCoSProfEncodeDropBit.setStatus("current")
_AcdSmapCoSProfCodePointTable_Object = MibTable
acdSmapCoSProfCodePointTable = _AcdSmapCoSProfCodePointTable_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 8, 1, 1, 2)
)
if mibBuilder.loadTexts:
    acdSmapCoSProfCodePointTable.setStatus("current")
_AcdSmapCoSProfCodePointEntry_Object = MibTableRow
acdSmapCoSProfCodePointEntry = _AcdSmapCoSProfCodePointEntry_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 8, 1, 1, 2, 1)
)
acdSmapCoSProfCodePointEntry.setIndexNames(
    (0, "ACD-SMAP-MIB", "acdSmapCoSProfID"),
    (0, "ACD-SMAP-MIB", "acdSmapCoSProfCodePointID"),
)
if mibBuilder.loadTexts:
    acdSmapCoSProfCodePointEntry.setStatus("current")


class _AcdSmapCoSProfCodePointID_Type(Unsigned32):
    """Custom type acdSmapCoSProfCodePointID based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_AcdSmapCoSProfCodePointID_Type.__name__ = "Unsigned32"
_AcdSmapCoSProfCodePointID_Object = MibTableColumn
acdSmapCoSProfCodePointID = _AcdSmapCoSProfCodePointID_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 8, 1, 1, 2, 1, 1),
    _AcdSmapCoSProfCodePointID_Type()
)
acdSmapCoSProfCodePointID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    acdSmapCoSProfCodePointID.setStatus("current")


class _AcdSmapCoSProfCodePointPreMarkingColor_Type(Integer32):
    """Custom type acdSmapCoSProfCodePointPreMarkingColor based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("green", 1),
          ("yellow", 2))
    )


_AcdSmapCoSProfCodePointPreMarkingColor_Type.__name__ = "Integer32"
_AcdSmapCoSProfCodePointPreMarkingColor_Object = MibTableColumn
acdSmapCoSProfCodePointPreMarkingColor = _AcdSmapCoSProfCodePointPreMarkingColor_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 8, 1, 1, 2, 1, 2),
    _AcdSmapCoSProfCodePointPreMarkingColor_Type()
)
acdSmapCoSProfCodePointPreMarkingColor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acdSmapCoSProfCodePointPreMarkingColor.setStatus("current")


class _AcdSmapCoSProfCodePointGreenOut_Type(Unsigned32):
    """Custom type acdSmapCoSProfCodePointGreenOut based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_AcdSmapCoSProfCodePointGreenOut_Type.__name__ = "Unsigned32"
_AcdSmapCoSProfCodePointGreenOut_Object = MibTableColumn
acdSmapCoSProfCodePointGreenOut = _AcdSmapCoSProfCodePointGreenOut_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 8, 1, 1, 2, 1, 3),
    _AcdSmapCoSProfCodePointGreenOut_Type()
)
acdSmapCoSProfCodePointGreenOut.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acdSmapCoSProfCodePointGreenOut.setStatus("current")


class _AcdSmapCoSProfCodePointYellowOut_Type(Unsigned32):
    """Custom type acdSmapCoSProfCodePointYellowOut based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_AcdSmapCoSProfCodePointYellowOut_Type.__name__ = "Unsigned32"
_AcdSmapCoSProfCodePointYellowOut_Object = MibTableColumn
acdSmapCoSProfCodePointYellowOut = _AcdSmapCoSProfCodePointYellowOut_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 8, 1, 1, 2, 1, 4),
    _AcdSmapCoSProfCodePointYellowOut_Type()
)
acdSmapCoSProfCodePointYellowOut.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acdSmapCoSProfCodePointYellowOut.setStatus("current")
_AcdSmapRegSetTable_Object = MibTable
acdSmapRegSetTable = _AcdSmapRegSetTable_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 8, 1, 1, 3)
)
if mibBuilder.loadTexts:
    acdSmapRegSetTable.setStatus("current")
_AcdSmapRegSetEntry_Object = MibTableRow
acdSmapRegSetEntry = _AcdSmapRegSetEntry_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 8, 1, 1, 3, 1)
)
acdSmapRegSetEntry.setIndexNames(
    (0, "ACD-SMAP-MIB", "acdSmapRegSetID"),
)
if mibBuilder.loadTexts:
    acdSmapRegSetEntry.setStatus("current")
_AcdSmapRegSetID_Type = Unsigned32
_AcdSmapRegSetID_Object = MibTableColumn
acdSmapRegSetID = _AcdSmapRegSetID_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 8, 1, 1, 3, 1, 1),
    _AcdSmapRegSetID_Type()
)
acdSmapRegSetID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    acdSmapRegSetID.setStatus("current")
_AcdSmapRegSetRowStatus_Type = RowStatus
_AcdSmapRegSetRowStatus_Object = MibTableColumn
acdSmapRegSetRowStatus = _AcdSmapRegSetRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 8, 1, 1, 3, 1, 2),
    _AcdSmapRegSetRowStatus_Type()
)
acdSmapRegSetRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acdSmapRegSetRowStatus.setStatus("current")


class _AcdSmapRegSetName_Type(DisplayString):
    """Custom type acdSmapRegSetName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_AcdSmapRegSetName_Type.__name__ = "DisplayString"
_AcdSmapRegSetName_Object = MibTableColumn
acdSmapRegSetName = _AcdSmapRegSetName_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 8, 1, 1, 3, 1, 3),
    _AcdSmapRegSetName_Type()
)
acdSmapRegSetName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acdSmapRegSetName.setStatus("current")


class _AcdSmapRegSetType_Type(Integer32):
    """Custom type acdSmapRegSetType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("pcp", 1),
          ("dscp", 2),
          ("pre", 3))
    )


_AcdSmapRegSetType_Type.__name__ = "Integer32"
_AcdSmapRegSetType_Object = MibTableColumn
acdSmapRegSetType = _AcdSmapRegSetType_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 8, 1, 1, 3, 1, 4),
    _AcdSmapRegSetType_Type()
)
acdSmapRegSetType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acdSmapRegSetType.setStatus("current")
_AcdSmapRegSetCodePointTable_Object = MibTable
acdSmapRegSetCodePointTable = _AcdSmapRegSetCodePointTable_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 8, 1, 1, 4)
)
if mibBuilder.loadTexts:
    acdSmapRegSetCodePointTable.setStatus("current")
_AcdSmapRegSetCodePointEntry_Object = MibTableRow
acdSmapRegSetCodePointEntry = _AcdSmapRegSetCodePointEntry_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 8, 1, 1, 4, 1)
)
acdSmapRegSetCodePointEntry.setIndexNames(
    (0, "ACD-SMAP-MIB", "acdSmapRegSetID"),
    (0, "ACD-SMAP-MIB", "acdSmapRegSetCodePointID"),
)
if mibBuilder.loadTexts:
    acdSmapRegSetCodePointEntry.setStatus("current")


class _AcdSmapRegSetCodePointID_Type(Unsigned32):
    """Custom type acdSmapRegSetCodePointID based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_AcdSmapRegSetCodePointID_Type.__name__ = "Unsigned32"
_AcdSmapRegSetCodePointID_Object = MibTableColumn
acdSmapRegSetCodePointID = _AcdSmapRegSetCodePointID_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 8, 1, 1, 4, 1, 1),
    _AcdSmapRegSetCodePointID_Type()
)
acdSmapRegSetCodePointID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    acdSmapRegSetCodePointID.setStatus("current")


class _AcdSmapRegSetCodePointRegulatorID_Type(Unsigned32):
    """Custom type acdSmapRegSetCodePointRegulatorID based on Unsigned32"""
    defaultValue = 0


_AcdSmapRegSetCodePointRegulatorID_Type.__name__ = "Unsigned32"
_AcdSmapRegSetCodePointRegulatorID_Object = MibTableColumn
acdSmapRegSetCodePointRegulatorID = _AcdSmapRegSetCodePointRegulatorID_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 8, 1, 1, 4, 1, 2),
    _AcdSmapRegSetCodePointRegulatorID_Type()
)
acdSmapRegSetCodePointRegulatorID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acdSmapRegSetCodePointRegulatorID.setStatus("current")


class _AcdSmapRegSetCodePointRegulatorEnable_Type(TruthValue):
    """Custom type acdSmapRegSetCodePointRegulatorEnable based on TruthValue"""
    defaultValue = 2


_AcdSmapRegSetCodePointRegulatorEnable_Type.__name__ = "TruthValue"
_AcdSmapRegSetCodePointRegulatorEnable_Object = MibTableColumn
acdSmapRegSetCodePointRegulatorEnable = _AcdSmapRegSetCodePointRegulatorEnable_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 8, 1, 1, 4, 1, 3),
    _AcdSmapRegSetCodePointRegulatorEnable_Type()
)
acdSmapRegSetCodePointRegulatorEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acdSmapRegSetCodePointRegulatorEnable.setStatus("current")
_AcdSmapPortCoSEncodeDeiTable_Object = MibTable
acdSmapPortCoSEncodeDeiTable = _AcdSmapPortCoSEncodeDeiTable_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 8, 1, 1, 5)
)
if mibBuilder.loadTexts:
    acdSmapPortCoSEncodeDeiTable.setStatus("current")
_AcdSmapPortCoSEncodeDeiEntry_Object = MibTableRow
acdSmapPortCoSEncodeDeiEntry = _AcdSmapPortCoSEncodeDeiEntry_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 8, 1, 1, 5, 1)
)
acdSmapPortCoSEncodeDeiEntry.setIndexNames(
    (0, "ACD-SMAP-MIB", "acdSmapPortCoSPortID"),
)
if mibBuilder.loadTexts:
    acdSmapPortCoSEncodeDeiEntry.setStatus("current")
_AcdSmapPortCoSPortID_Type = Unsigned32
_AcdSmapPortCoSPortID_Object = MibTableColumn
acdSmapPortCoSPortID = _AcdSmapPortCoSPortID_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 8, 1, 1, 5, 1, 1),
    _AcdSmapPortCoSPortID_Type()
)
acdSmapPortCoSPortID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    acdSmapPortCoSPortID.setStatus("current")


class _AcdSmapPortCoSEncodeDeiEnable_Type(Integer32):
    """Custom type acdSmapPortCoSEncodeDeiEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("enable", 0),
          ("disable", 1))
    )


_AcdSmapPortCoSEncodeDeiEnable_Type.__name__ = "Integer32"
_AcdSmapPortCoSEncodeDeiEnable_Object = MibTableColumn
acdSmapPortCoSEncodeDeiEnable = _AcdSmapPortCoSEncodeDeiEnable_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 8, 1, 1, 5, 1, 2),
    _AcdSmapPortCoSEncodeDeiEnable_Type()
)
acdSmapPortCoSEncodeDeiEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acdSmapPortCoSEncodeDeiEnable.setStatus("current")
_AcdSmapPortCoSMapTable_Object = MibTable
acdSmapPortCoSMapTable = _AcdSmapPortCoSMapTable_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 8, 1, 1, 6)
)
if mibBuilder.loadTexts:
    acdSmapPortCoSMapTable.setStatus("current")
_AcdSmapPortCoSMapEntry_Object = MibTableRow
acdSmapPortCoSMapEntry = _AcdSmapPortCoSMapEntry_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 8, 1, 1, 6, 1)
)
acdSmapPortCoSMapEntry.setIndexNames(
    (0, "ACD-SMAP-MIB", "acdSmapPortCoSPortID"),
    (0, "ACD-SMAP-MIB", "acdSmapPortCoSMapID"),
)
if mibBuilder.loadTexts:
    acdSmapPortCoSMapEntry.setStatus("current")


class _AcdSmapPortCoSMapID_Type(Unsigned32):
    """Custom type acdSmapPortCoSMapID based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_AcdSmapPortCoSMapID_Type.__name__ = "Unsigned32"
_AcdSmapPortCoSMapID_Object = MibTableColumn
acdSmapPortCoSMapID = _AcdSmapPortCoSMapID_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 8, 1, 1, 6, 1, 1),
    _AcdSmapPortCoSMapID_Type()
)
acdSmapPortCoSMapID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    acdSmapPortCoSMapID.setStatus("current")


class _AcdSmapPortCoSMapCosIn_Type(Unsigned32):
    """Custom type acdSmapPortCoSMapCosIn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_AcdSmapPortCoSMapCosIn_Type.__name__ = "Unsigned32"
_AcdSmapPortCoSMapCosIn_Object = MibTableColumn
acdSmapPortCoSMapCosIn = _AcdSmapPortCoSMapCosIn_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 8, 1, 1, 6, 1, 2),
    _AcdSmapPortCoSMapCosIn_Type()
)
acdSmapPortCoSMapCosIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdSmapPortCoSMapCosIn.setStatus("current")


class _AcdSmapPortCoSMapGreenOut_Type(Unsigned32):
    """Custom type acdSmapPortCoSMapGreenOut based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_AcdSmapPortCoSMapGreenOut_Type.__name__ = "Unsigned32"
_AcdSmapPortCoSMapGreenOut_Object = MibTableColumn
acdSmapPortCoSMapGreenOut = _AcdSmapPortCoSMapGreenOut_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 8, 1, 1, 6, 1, 3),
    _AcdSmapPortCoSMapGreenOut_Type()
)
acdSmapPortCoSMapGreenOut.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acdSmapPortCoSMapGreenOut.setStatus("current")


class _AcdSmapPortCoSMapYellowOut_Type(Unsigned32):
    """Custom type acdSmapPortCoSMapYellowOut based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_AcdSmapPortCoSMapYellowOut_Type.__name__ = "Unsigned32"
_AcdSmapPortCoSMapYellowOut_Object = MibTableColumn
acdSmapPortCoSMapYellowOut = _AcdSmapPortCoSMapYellowOut_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 8, 1, 1, 6, 1, 4),
    _AcdSmapPortCoSMapYellowOut_Type()
)
acdSmapPortCoSMapYellowOut.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acdSmapPortCoSMapYellowOut.setStatus("current")
_AcdSmapConformance_ObjectIdentity = ObjectIdentity
acdSmapConformance = _AcdSmapConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22420, 2, 8, 2)
)
_AcdSmapCompliances_ObjectIdentity = ObjectIdentity
acdSmapCompliances = _AcdSmapCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22420, 2, 8, 2, 1)
)
_AcdSmapGroups_ObjectIdentity = ObjectIdentity
acdSmapGroups = _AcdSmapGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22420, 2, 8, 2, 2)
)

# Managed Objects groups

acdSmapCoSProfGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 22420, 2, 8, 2, 2, 1)
)
acdSmapCoSProfGroup.setObjects(
      *(("ACD-SMAP-MIB", "acdSmapCoSProfRowStatus"),
        ("ACD-SMAP-MIB", "acdSmapCoSProfName"),
        ("ACD-SMAP-MIB", "acdSmapCoSProfType"),
        ("ACD-SMAP-MIB", "acdSmapCoSProfDecodeDropBit"),
        ("ACD-SMAP-MIB", "acdSmapCoSProfEncodeDropBit"))
)
if mibBuilder.loadTexts:
    acdSmapCoSProfGroup.setStatus("current")

acdSmapCoSProfCodePointGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 22420, 2, 8, 2, 2, 2)
)
acdSmapCoSProfCodePointGroup.setObjects(
      *(("ACD-SMAP-MIB", "acdSmapCoSProfCodePointPreMarkingColor"),
        ("ACD-SMAP-MIB", "acdSmapCoSProfCodePointGreenOut"),
        ("ACD-SMAP-MIB", "acdSmapCoSProfCodePointYellowOut"))
)
if mibBuilder.loadTexts:
    acdSmapCoSProfCodePointGroup.setStatus("current")

acdSmapRegSetGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 22420, 2, 8, 2, 2, 3)
)
acdSmapRegSetGroup.setObjects(
      *(("ACD-SMAP-MIB", "acdSmapRegSetRowStatus"),
        ("ACD-SMAP-MIB", "acdSmapRegSetName"),
        ("ACD-SMAP-MIB", "acdSmapRegSetType"))
)
if mibBuilder.loadTexts:
    acdSmapRegSetGroup.setStatus("current")

acdSmapRegSetCodePointGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 22420, 2, 8, 2, 2, 4)
)
acdSmapRegSetCodePointGroup.setObjects(
      *(("ACD-SMAP-MIB", "acdSmapRegSetCodePointRegulatorID"),
        ("ACD-SMAP-MIB", "acdSmapRegSetCodePointRegulatorEnable"))
)
if mibBuilder.loadTexts:
    acdSmapRegSetCodePointGroup.setStatus("current")

acdSmapPortCoSEncodeDeiGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 22420, 2, 8, 2, 2, 5)
)
acdSmapPortCoSEncodeDeiGroup.setObjects(
    ("ACD-SMAP-MIB", "acdSmapPortCoSEncodeDeiEnable")
)
if mibBuilder.loadTexts:
    acdSmapPortCoSEncodeDeiGroup.setStatus("current")

acdSmapPortCoSMapGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 22420, 2, 8, 2, 2, 6)
)
acdSmapPortCoSMapGroup.setObjects(
      *(("ACD-SMAP-MIB", "acdSmapPortCoSMapCosIn"),
        ("ACD-SMAP-MIB", "acdSmapPortCoSMapGreenOut"),
        ("ACD-SMAP-MIB", "acdSmapPortCoSMapYellowOut"))
)
if mibBuilder.loadTexts:
    acdSmapPortCoSMapGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

acdSmapCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 22420, 2, 8, 2, 1, 1)
)
acdSmapCompliance.setObjects(
      *(("ACD-SMAP-MIB", "acdSmapCoSProfGroup"),
        ("ACD-SMAP-MIB", "acdSmapCoSProfCodePointGroup"),
        ("ACD-SMAP-MIB", "acdSmapRegSetGroup"),
        ("ACD-SMAP-MIB", "acdSmapRegSetCodePointGroup"),
        ("ACD-SMAP-MIB", "acdSmapPortCoSEncodeDeiGroup"),
        ("ACD-SMAP-MIB", "acdSmapPortCoSMapGroup"))
)
if mibBuilder.loadTexts:
    acdSmapCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ACD-SMAP-MIB",
    **{"acdSmap": acdSmap,
       "acdSmapNotifications": acdSmapNotifications,
       "acdSmapMIBObjects": acdSmapMIBObjects,
       "acdSmapConfig": acdSmapConfig,
       "acdSmapCoSProfTable": acdSmapCoSProfTable,
       "acdSmapCoSProfEntry": acdSmapCoSProfEntry,
       "acdSmapCoSProfID": acdSmapCoSProfID,
       "acdSmapCoSProfRowStatus": acdSmapCoSProfRowStatus,
       "acdSmapCoSProfName": acdSmapCoSProfName,
       "acdSmapCoSProfType": acdSmapCoSProfType,
       "acdSmapCoSProfDecodeDropBit": acdSmapCoSProfDecodeDropBit,
       "acdSmapCoSProfEncodeDropBit": acdSmapCoSProfEncodeDropBit,
       "acdSmapCoSProfCodePointTable": acdSmapCoSProfCodePointTable,
       "acdSmapCoSProfCodePointEntry": acdSmapCoSProfCodePointEntry,
       "acdSmapCoSProfCodePointID": acdSmapCoSProfCodePointID,
       "acdSmapCoSProfCodePointPreMarkingColor": acdSmapCoSProfCodePointPreMarkingColor,
       "acdSmapCoSProfCodePointGreenOut": acdSmapCoSProfCodePointGreenOut,
       "acdSmapCoSProfCodePointYellowOut": acdSmapCoSProfCodePointYellowOut,
       "acdSmapRegSetTable": acdSmapRegSetTable,
       "acdSmapRegSetEntry": acdSmapRegSetEntry,
       "acdSmapRegSetID": acdSmapRegSetID,
       "acdSmapRegSetRowStatus": acdSmapRegSetRowStatus,
       "acdSmapRegSetName": acdSmapRegSetName,
       "acdSmapRegSetType": acdSmapRegSetType,
       "acdSmapRegSetCodePointTable": acdSmapRegSetCodePointTable,
       "acdSmapRegSetCodePointEntry": acdSmapRegSetCodePointEntry,
       "acdSmapRegSetCodePointID": acdSmapRegSetCodePointID,
       "acdSmapRegSetCodePointRegulatorID": acdSmapRegSetCodePointRegulatorID,
       "acdSmapRegSetCodePointRegulatorEnable": acdSmapRegSetCodePointRegulatorEnable,
       "acdSmapPortCoSEncodeDeiTable": acdSmapPortCoSEncodeDeiTable,
       "acdSmapPortCoSEncodeDeiEntry": acdSmapPortCoSEncodeDeiEntry,
       "acdSmapPortCoSPortID": acdSmapPortCoSPortID,
       "acdSmapPortCoSEncodeDeiEnable": acdSmapPortCoSEncodeDeiEnable,
       "acdSmapPortCoSMapTable": acdSmapPortCoSMapTable,
       "acdSmapPortCoSMapEntry": acdSmapPortCoSMapEntry,
       "acdSmapPortCoSMapID": acdSmapPortCoSMapID,
       "acdSmapPortCoSMapCosIn": acdSmapPortCoSMapCosIn,
       "acdSmapPortCoSMapGreenOut": acdSmapPortCoSMapGreenOut,
       "acdSmapPortCoSMapYellowOut": acdSmapPortCoSMapYellowOut,
       "acdSmapConformance": acdSmapConformance,
       "acdSmapCompliances": acdSmapCompliances,
       "acdSmapCompliance": acdSmapCompliance,
       "acdSmapGroups": acdSmapGroups,
       "acdSmapCoSProfGroup": acdSmapCoSProfGroup,
       "acdSmapCoSProfCodePointGroup": acdSmapCoSProfCodePointGroup,
       "acdSmapRegSetGroup": acdSmapRegSetGroup,
       "acdSmapRegSetCodePointGroup": acdSmapRegSetCodePointGroup,
       "acdSmapPortCoSEncodeDeiGroup": acdSmapPortCoSEncodeDeiGroup,
       "acdSmapPortCoSMapGroup": acdSmapPortCoSMapGroup}
)
