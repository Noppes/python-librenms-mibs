# SNMP MIB module (SSU2000-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\microsemi\SSU2000-MIB

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

(austron,) = mibBuilder.importSymbols(
    "DATUM-MIB",
    "austron")

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

ssu2000 = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1)
)


# Types definitions



class OkValue(Integer32):
    """Custom type OkValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ok", 1),
          ("fault", 2))
    )





class OnValue(Integer32):
    """Custom type OnValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("on", 1),
          ("off", 2))
    )





class YesValue(Integer32):
    """Custom type YesValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("yes", 1),
          ("no", 2))
    )





class EnaValue(Integer32):
    """Custom type EnaValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ena", 1),
          ("dis", 2))
    )





class ActiveValue(Integer32):
    """Custom type ActiveValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("inactive", 2))
    )





class ValidValue(Integer32):
    """Custom type ValidValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("valid", 1),
          ("invalid", 2))
    )





class TrueValue(Integer32):
    """Custom type TrueValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("true", 1),
          ("false", 2))
    )




# TEXTUAL-CONVENTIONS



class DateAndTime(TextualConvention, OctetString):
    status = "current"
    displayHint = "2d-1d-1d,1d:1d:1d.1d,1a1d:1d"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
        ValueSizeConstraint(11, 11),
    )



class TLocalTimeOffset(TextualConvention, OctetString):
    status = "current"
    displayHint = "1a1d:1d"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 3),
    )
    fixed_length = 3



class TModuleCode(TextualConvention, Integer32):
    status = "current"
    displayHint = "x"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )



class TSsm(TextualConvention, Integer32):
    status = "current"
    displayHint = "x"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )



class TLatAndLon(TextualConvention, OctetString):
    status = "current"
    displayHint = "1a1d:1d:1d.1d"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(5, 5),
    )
    fixed_length = 5



class TAntHeight(TextualConvention, OctetString):
    status = "current"
    displayHint = "1a2d.1d"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )
    fixed_length = 4



# MIB Managed Objects in the order of their OIDs

_Inventory_ObjectIdentity = ObjectIdentity
inventory = _Inventory_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 1)
)
_InventoryTable_Object = MibTable
inventoryTable = _InventoryTable_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 1, 1)
)
if mibBuilder.loadTexts:
    inventoryTable.setStatus("current")
_InEntry_Object = MibTableRow
inEntry = _InEntry_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 1, 1, 1)
)
inEntry.setIndexNames(
    (0, "SSU2000-MIB", "inChassis"),
    (0, "SSU2000-MIB", "inSlot"),
)
if mibBuilder.loadTexts:
    inEntry.setStatus("current")


class _InChassis_Type(Integer32):
    """Custom type inChassis based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_InChassis_Type.__name__ = "Integer32"
_InChassis_Object = MibTableColumn
inChassis = _InChassis_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 1, 1, 1, 1),
    _InChassis_Type()
)
inChassis.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    inChassis.setStatus("current")


class _InSlot_Type(Integer32):
    """Custom type inSlot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 20),
    )


_InSlot_Type.__name__ = "Integer32"
_InSlot_Object = MibTableColumn
inSlot = _InSlot_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 1, 1, 1, 2),
    _InSlot_Type()
)
inSlot.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    inSlot.setStatus("current")
_InModCode_Type = TModuleCode
_InModCode_Object = MibTableColumn
inModCode = _InModCode_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 1, 1, 1, 3),
    _InModCode_Type()
)
inModCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inModCode.setStatus("current")


class _InName_Type(DisplayString):
    """Custom type inName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_InName_Type.__name__ = "DisplayString"
_InName_Object = MibTableColumn
inName = _InName_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 1, 1, 1, 4),
    _InName_Type()
)
inName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inName.setStatus("current")


class _InSerial_Type(DisplayString):
    """Custom type inSerial based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_InSerial_Type.__name__ = "DisplayString"
_InSerial_Object = MibTableColumn
inSerial = _InSerial_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 1, 1, 1, 5),
    _InSerial_Type()
)
inSerial.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inSerial.setStatus("current")
_InService_Type = DateAndTime
_InService_Object = MibTableColumn
inService = _InService_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 1, 1, 1, 6),
    _InService_Type()
)
inService.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inService.setStatus("current")


class _InHwPart_Type(DisplayString):
    """Custom type inHwPart based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 14),
    )


_InHwPart_Type.__name__ = "DisplayString"
_InHwPart_Object = MibTableColumn
inHwPart = _InHwPart_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 1, 1, 1, 7),
    _InHwPart_Type()
)
inHwPart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inHwPart.setStatus("current")


class _InHwRev_Type(DisplayString):
    """Custom type inHwRev based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_InHwRev_Type.__name__ = "DisplayString"
_InHwRev_Object = MibTableColumn
inHwRev = _InHwRev_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 1, 1, 1, 8),
    _InHwRev_Type()
)
inHwRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inHwRev.setStatus("current")
_InHwDate_Type = DateAndTime
_InHwDate_Object = MibTableColumn
inHwDate = _InHwDate_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 1, 1, 1, 9),
    _InHwDate_Type()
)
inHwDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inHwDate.setStatus("current")


class _InSwPart_Type(DisplayString):
    """Custom type inSwPart based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 14),
    )


_InSwPart_Type.__name__ = "DisplayString"
_InSwPart_Object = MibTableColumn
inSwPart = _InSwPart_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 1, 1, 1, 10),
    _InSwPart_Type()
)
inSwPart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inSwPart.setStatus("current")


class _InSwRev_Type(DisplayString):
    """Custom type inSwRev based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_InSwRev_Type.__name__ = "DisplayString"
_InSwRev_Object = MibTableColumn
inSwRev = _InSwRev_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 1, 1, 1, 11),
    _InSwRev_Type()
)
inSwRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inSwRev.setStatus("current")


class _InRevision_Type(DisplayString):
    """Custom type inRevision based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 60),
    )


_InRevision_Type.__name__ = "DisplayString"
_InRevision_Object = MibTableColumn
inRevision = _InRevision_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 1, 1, 1, 12),
    _InRevision_Type()
)
inRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inRevision.setStatus("current")


class _InShelfDesc_Type(DisplayString):
    """Custom type inShelfDesc based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_InShelfDesc_Type.__name__ = "DisplayString"
_InShelfDesc_Object = MibTableColumn
inShelfDesc = _InShelfDesc_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 1, 1, 1, 13),
    _InShelfDesc_Type()
)
inShelfDesc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inShelfDesc.setStatus("current")


class _InShelfPart_Type(DisplayString):
    """Custom type inShelfPart based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 14),
    )


_InShelfPart_Type.__name__ = "DisplayString"
_InShelfPart_Object = MibTableColumn
inShelfPart = _InShelfPart_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 1, 1, 1, 14),
    _InShelfPart_Type()
)
inShelfPart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inShelfPart.setStatus("current")
_InInstalled_Type = YesValue
_InInstalled_Object = MibTableColumn
inInstalled = _InInstalled_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 1, 1, 1, 15),
    _InInstalled_Type()
)
inInstalled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inInstalled.setStatus("current")


class _InAction_Type(Integer32):
    """Custom type inAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2),
          ("remove", 3))
    )


_InAction_Type.__name__ = "Integer32"
_InAction_Object = MibTableColumn
inAction = _InAction_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 1, 1, 1, 16),
    _InAction_Type()
)
inAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    inAction.setStatus("current")


class _InAdapterPart_Type(DisplayString):
    """Custom type inAdapterPart based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 14),
    )


_InAdapterPart_Type.__name__ = "DisplayString"
_InAdapterPart_Object = MibTableColumn
inAdapterPart = _InAdapterPart_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 1, 1, 1, 17),
    _InAdapterPart_Type()
)
inAdapterPart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inAdapterPart.setStatus("current")
_InFeatureTable_Object = MibTable
inFeatureTable = _InFeatureTable_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 1, 2)
)
if mibBuilder.loadTexts:
    inFeatureTable.setStatus("current")
_InFeatureEntry_Object = MibTableRow
inFeatureEntry = _InFeatureEntry_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 1, 2, 1)
)
inFeatureEntry.setIndexNames(
    (0, "SSU2000-MIB", "inFeatureIndex"),
)
if mibBuilder.loadTexts:
    inFeatureEntry.setStatus("current")


class _InFeatureIndex_Type(Integer32):
    """Custom type inFeatureIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_InFeatureIndex_Type.__name__ = "Integer32"
_InFeatureIndex_Object = MibTableColumn
inFeatureIndex = _InFeatureIndex_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 1, 2, 1, 1),
    _InFeatureIndex_Type()
)
inFeatureIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    inFeatureIndex.setStatus("current")
_InFeature_Type = EnaValue
_InFeature_Object = MibTableColumn
inFeature = _InFeature_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 1, 2, 1, 2),
    _InFeature_Type()
)
inFeature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inFeature.setStatus("current")
_Mstatus_ObjectIdentity = ObjectIdentity
mstatus = _Mstatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 2)
)
_StatusCom_ObjectIdentity = ObjectIdentity
statusCom = _StatusCom_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 2, 1)
)
_StatusClk_ObjectIdentity = ObjectIdentity
statusClk = _StatusClk_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 2, 2)
)
_StaClkTable_Object = MibTable
staClkTable = _StaClkTable_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 2, 2, 1)
)
if mibBuilder.loadTexts:
    staClkTable.setStatus("current")
_StaCkEntry_Object = MibTableRow
staCkEntry = _StaCkEntry_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 2, 2, 1, 1)
)
staCkEntry.setIndexNames(
    (0, "SSU2000-MIB", "staCkChassis"),
    (0, "SSU2000-MIB", "staCkSlot"),
)
if mibBuilder.loadTexts:
    staCkEntry.setStatus("current")


class _StaCkChassis_Type(Integer32):
    """Custom type staCkChassis based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
    )


_StaCkChassis_Type.__name__ = "Integer32"
_StaCkChassis_Object = MibTableColumn
staCkChassis = _StaCkChassis_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 2, 2, 1, 1, 1),
    _StaCkChassis_Type()
)
staCkChassis.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    staCkChassis.setStatus("current")


class _StaCkSlot_Type(Integer32):
    """Custom type staCkSlot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 20),
    )


_StaCkSlot_Type.__name__ = "Integer32"
_StaCkSlot_Object = MibTableColumn
staCkSlot = _StaCkSlot_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 2, 2, 1, 1, 2),
    _StaCkSlot_Type()
)
staCkSlot.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    staCkSlot.setStatus("current")


class _StaCkStatus_Type(Integer32):
    """Custom type staCkStatus based on Integer32"""
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
        *(("ok", 1),
          ("selected", 2),
          ("disable", 3),
          ("fault", 4))
    )


_StaCkStatus_Type.__name__ = "Integer32"
_StaCkStatus_Object = MibTableColumn
staCkStatus = _StaCkStatus_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 2, 2, 1, 1, 3),
    _StaCkStatus_Type()
)
staCkStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staCkStatus.setStatus("current")


class _StaCkPLLMode_Type(Integer32):
    """Custom type staCkPLLMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("failed", 1),
          ("warmup", 2),
          ("acquire", 3),
          ("holdover", 4),
          ("lock", 5))
    )


_StaCkPLLMode_Type.__name__ = "Integer32"
_StaCkPLLMode_Object = MibTableColumn
staCkPLLMode = _StaCkPLLMode_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 2, 2, 1, 1, 4),
    _StaCkPLLMode_Type()
)
staCkPLLMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staCkPLLMode.setStatus("current")
_StaCkTau_Type = Counter32
_StaCkTau_Object = MibTableColumn
staCkTau = _StaCkTau_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 2, 2, 1, 1, 5),
    _StaCkTau_Type()
)
staCkTau.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staCkTau.setStatus("current")


class _StaCkPql_Type(Integer32):
    """Custom type staCkPql based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 16),
    )


_StaCkPql_Type.__name__ = "Integer32"
_StaCkPql_Object = MibTableColumn
staCkPql = _StaCkPql_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 2, 2, 1, 1, 6),
    _StaCkPql_Type()
)
staCkPql.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staCkPql.setStatus("current")
_StaCkUtc_Type = YesValue
_StaCkUtc_Object = MibTableColumn
staCkUtc = _StaCkUtc_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 2, 2, 1, 1, 7),
    _StaCkUtc_Type()
)
staCkUtc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staCkUtc.setStatus("current")
_StatusGps_ObjectIdentity = ObjectIdentity
statusGps = _StatusGps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 2, 5)
)
_StaGpsTable_Object = MibTable
staGpsTable = _StaGpsTable_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 2, 5, 1)
)
if mibBuilder.loadTexts:
    staGpsTable.setStatus("current")
_StaGpsEntry_Object = MibTableRow
staGpsEntry = _StaGpsEntry_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 2, 5, 1, 1)
)
staGpsEntry.setIndexNames(
    (0, "SSU2000-MIB", "staGpsChassis"),
    (0, "SSU2000-MIB", "staGpsSlot"),
)
if mibBuilder.loadTexts:
    staGpsEntry.setStatus("current")


class _StaGpsChassis_Type(Integer32):
    """Custom type staGpsChassis based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
    )


_StaGpsChassis_Type.__name__ = "Integer32"
_StaGpsChassis_Object = MibTableColumn
staGpsChassis = _StaGpsChassis_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 2, 5, 1, 1, 1),
    _StaGpsChassis_Type()
)
staGpsChassis.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    staGpsChassis.setStatus("current")


class _StaGpsSlot_Type(Integer32):
    """Custom type staGpsSlot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 20),
    )


_StaGpsSlot_Type.__name__ = "Integer32"
_StaGpsSlot_Object = MibTableColumn
staGpsSlot = _StaGpsSlot_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 2, 5, 1, 1, 2),
    _StaGpsSlot_Type()
)
staGpsSlot.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    staGpsSlot.setStatus("current")


class _StaGpsStatus_Type(Integer32):
    """Custom type staGpsStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("ok", 1),
          ("selected", 2),
          ("disable", 3),
          ("fault", 4),
          ("reject", 5))
    )


_StaGpsStatus_Type.__name__ = "Integer32"
_StaGpsStatus_Object = MibTableColumn
staGpsStatus = _StaGpsStatus_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 2, 5, 1, 1, 3),
    _StaGpsStatus_Type()
)
staGpsStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staGpsStatus.setStatus("current")


class _StaGpsPhaseA_Type(Integer32):
    """Custom type staGpsPhaseA based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1999999998, 1999999998),
        ValueRangeConstraint(1999999999, 1999999999),
    )


_StaGpsPhaseA_Type.__name__ = "Integer32"
_StaGpsPhaseA_Object = MibTableColumn
staGpsPhaseA = _StaGpsPhaseA_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 2, 5, 1, 1, 4),
    _StaGpsPhaseA_Type()
)
staGpsPhaseA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staGpsPhaseA.setStatus("current")


class _StaGpsPhaseB_Type(Integer32):
    """Custom type staGpsPhaseB based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1999999998, 1999999998),
        ValueRangeConstraint(1999999999, 1999999999),
    )


_StaGpsPhaseB_Type.__name__ = "Integer32"
_StaGpsPhaseB_Object = MibTableColumn
staGpsPhaseB = _StaGpsPhaseB_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 2, 5, 1, 1, 5),
    _StaGpsPhaseB_Type()
)
staGpsPhaseB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staGpsPhaseB.setStatus("current")
_StaGpsUtc_Type = YesValue
_StaGpsUtc_Object = MibTableColumn
staGpsUtc = _StaGpsUtc_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 2, 5, 1, 1, 6),
    _StaGpsUtc_Type()
)
staGpsUtc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staGpsUtc.setStatus("current")


class _StaGpsMStatus_Type(Integer32):
    """Custom type staGpsMStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("ok", 1),
          ("disable", 2),
          ("fault", 3))
    )


_StaGpsMStatus_Type.__name__ = "Integer32"
_StaGpsMStatus_Object = MibTableColumn
staGpsMStatus = _StaGpsMStatus_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 2, 5, 1, 1, 7),
    _StaGpsMStatus_Type()
)
staGpsMStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staGpsMStatus.setStatus("current")


class _StaGpsMtie1A_Type(Integer32):
    """Custom type staGpsMtie1A based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              10,
              100,
              1000,
              10000,
              100000)
        )
    )
    namedValues = NamedValues(
        *(("ok", 1),
          ("mtie10", 10),
          ("mtie100", 100),
          ("mtie1000", 1000),
          ("mtie10000", 10000),
          ("mtie100000", 100000))
    )


_StaGpsMtie1A_Type.__name__ = "Integer32"
_StaGpsMtie1A_Object = MibTableColumn
staGpsMtie1A = _StaGpsMtie1A_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 2, 5, 1, 1, 8),
    _StaGpsMtie1A_Type()
)
staGpsMtie1A.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staGpsMtie1A.setStatus("current")


class _StaGpsMtie2A_Type(Integer32):
    """Custom type staGpsMtie2A based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              10,
              100,
              1000,
              10000,
              100000)
        )
    )
    namedValues = NamedValues(
        *(("ok", 1),
          ("mtie10", 10),
          ("mtie100", 100),
          ("mtie1000", 1000),
          ("mtie10000", 10000),
          ("mtie100000", 100000))
    )


_StaGpsMtie2A_Type.__name__ = "Integer32"
_StaGpsMtie2A_Object = MibTableColumn
staGpsMtie2A = _StaGpsMtie2A_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 2, 5, 1, 1, 9),
    _StaGpsMtie2A_Type()
)
staGpsMtie2A.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staGpsMtie2A.setStatus("current")


class _StaGpsMtie1B_Type(Integer32):
    """Custom type staGpsMtie1B based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              10,
              100,
              1000,
              10000,
              100000)
        )
    )
    namedValues = NamedValues(
        *(("ok", 1),
          ("mtie10", 10),
          ("mtie100", 100),
          ("mtie1000", 1000),
          ("mtie10000", 10000),
          ("mtie100000", 100000))
    )


_StaGpsMtie1B_Type.__name__ = "Integer32"
_StaGpsMtie1B_Object = MibTableColumn
staGpsMtie1B = _StaGpsMtie1B_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 2, 5, 1, 1, 10),
    _StaGpsMtie1B_Type()
)
staGpsMtie1B.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staGpsMtie1B.setStatus("current")


class _StaGpsMtie2B_Type(Integer32):
    """Custom type staGpsMtie2B based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              10,
              100,
              1000,
              10000,
              100000)
        )
    )
    namedValues = NamedValues(
        *(("ok", 1),
          ("mtie10", 10),
          ("mtie100", 100),
          ("mtie1000", 1000),
          ("mtie10000", 10000),
          ("mtie100000", 100000))
    )


_StaGpsMtie2B_Type.__name__ = "Integer32"
_StaGpsMtie2B_Object = MibTableColumn
staGpsMtie2B = _StaGpsMtie2B_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 2, 5, 1, 1, 11),
    _StaGpsMtie2B_Type()
)
staGpsMtie2B.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staGpsMtie2B.setStatus("current")
_StaGpsFreqA_Type = OkValue
_StaGpsFreqA_Object = MibTableColumn
staGpsFreqA = _StaGpsFreqA_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 2, 5, 1, 1, 12),
    _StaGpsFreqA_Type()
)
staGpsFreqA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staGpsFreqA.setStatus("current")
_StaGpsFreqB_Type = OkValue
_StaGpsFreqB_Object = MibTableColumn
staGpsFreqB = _StaGpsFreqB_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 2, 5, 1, 1, 13),
    _StaGpsFreqB_Type()
)
staGpsFreqB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staGpsFreqB.setStatus("current")


class _StaGpsPpsSigma_Type(DisplayString):
    """Custom type staGpsPpsSigma based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_StaGpsPpsSigma_Type.__name__ = "DisplayString"
_StaGpsPpsSigma_Object = MibTableColumn
staGpsPpsSigma = _StaGpsPpsSigma_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 2, 5, 1, 1, 14),
    _StaGpsPpsSigma_Type()
)
staGpsPpsSigma.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staGpsPpsSigma.setStatus("current")


class _StaGps3Sigma_Type(DisplayString):
    """Custom type staGps3Sigma based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_StaGps3Sigma_Type.__name__ = "DisplayString"
_StaGps3Sigma_Object = MibTableColumn
staGps3Sigma = _StaGps3Sigma_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 2, 5, 1, 1, 15),
    _StaGps3Sigma_Type()
)
staGps3Sigma.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staGps3Sigma.setStatus("current")
_StGpsPosTable_Object = MibTable
stGpsPosTable = _StGpsPosTable_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 2, 5, 2)
)
if mibBuilder.loadTexts:
    stGpsPosTable.setStatus("current")
_StGpsPosEntry_Object = MibTableRow
stGpsPosEntry = _StGpsPosEntry_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 2, 5, 2, 1)
)
stGpsPosEntry.setIndexNames(
    (0, "SSU2000-MIB", "stGpsPosChassis"),
    (0, "SSU2000-MIB", "stGpsPosSlot"),
)
if mibBuilder.loadTexts:
    stGpsPosEntry.setStatus("current")


class _StGpsPosChassis_Type(Integer32):
    """Custom type stGpsPosChassis based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
    )


_StGpsPosChassis_Type.__name__ = "Integer32"
_StGpsPosChassis_Object = MibTableColumn
stGpsPosChassis = _StGpsPosChassis_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 2, 5, 2, 1, 1),
    _StGpsPosChassis_Type()
)
stGpsPosChassis.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    stGpsPosChassis.setStatus("current")


class _StGpsPosSlot_Type(Integer32):
    """Custom type stGpsPosSlot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 20),
    )


_StGpsPosSlot_Type.__name__ = "Integer32"
_StGpsPosSlot_Object = MibTableColumn
stGpsPosSlot = _StGpsPosSlot_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 2, 5, 2, 1, 2),
    _StGpsPosSlot_Type()
)
stGpsPosSlot.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    stGpsPosSlot.setStatus("current")
_StGpsPosValid_Type = ValidValue
_StGpsPosValid_Object = MibTableColumn
stGpsPosValid = _StGpsPosValid_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 2, 5, 2, 1, 3),
    _StGpsPosValid_Type()
)
stGpsPosValid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stGpsPosValid.setStatus("current")
_StGpsPosLat_Type = TLatAndLon
_StGpsPosLat_Object = MibTableColumn
stGpsPosLat = _StGpsPosLat_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 2, 5, 2, 1, 4),
    _StGpsPosLat_Type()
)
stGpsPosLat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stGpsPosLat.setStatus("current")
_StGpsPosLon_Type = TLatAndLon
_StGpsPosLon_Object = MibTableColumn
stGpsPosLon = _StGpsPosLon_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 2, 5, 2, 1, 5),
    _StGpsPosLon_Type()
)
stGpsPosLon.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stGpsPosLon.setStatus("current")
_StGpsPosHgt_Type = TAntHeight
_StGpsPosHgt_Object = MibTableColumn
stGpsPosHgt = _StGpsPosHgt_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 2, 5, 2, 1, 6),
    _StGpsPosHgt_Type()
)
stGpsPosHgt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stGpsPosHgt.setStatus("current")


class _StGpsPosAccurate_Type(Integer32):
    """Custom type stGpsPosAccurate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("approx", 1),
          ("d2", 2),
          ("d3", 3))
    )


_StGpsPosAccurate_Type.__name__ = "Integer32"
_StGpsPosAccurate_Object = MibTableColumn
stGpsPosAccurate = _StGpsPosAccurate_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 2, 5, 2, 1, 7),
    _StGpsPosAccurate_Type()
)
stGpsPosAccurate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stGpsPosAccurate.setStatus("current")


class _StGpsPosPdop_Type(Integer32):
    """Custom type stGpsPosPdop based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_StGpsPosPdop_Type.__name__ = "Integer32"
_StGpsPosPdop_Object = MibTableColumn
stGpsPosPdop = _StGpsPosPdop_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 2, 5, 2, 1, 8),
    _StGpsPosPdop_Type()
)
stGpsPosPdop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stGpsPosPdop.setStatus("current")


class _StGpsPosAvg_Type(Integer32):
    """Custom type stGpsPosAvg based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3600),
    )


_StGpsPosAvg_Type.__name__ = "Integer32"
_StGpsPosAvg_Object = MibTableColumn
stGpsPosAvg = _StGpsPosAvg_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 2, 5, 2, 1, 9),
    _StGpsPosAvg_Type()
)
stGpsPosAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stGpsPosAvg.setStatus("current")
_StGpsAvailTable_Object = MibTable
stGpsAvailTable = _StGpsAvailTable_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 2, 5, 3)
)
if mibBuilder.loadTexts:
    stGpsAvailTable.setStatus("current")
_StGpsAvEntry_Object = MibTableRow
stGpsAvEntry = _StGpsAvEntry_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 2, 5, 3, 1)
)
stGpsAvEntry.setIndexNames(
    (0, "SSU2000-MIB", "stGpsAvChassis"),
    (0, "SSU2000-MIB", "stGpsAvSlot"),
    (0, "SSU2000-MIB", "stGpsAvChnl"),
)
if mibBuilder.loadTexts:
    stGpsAvEntry.setStatus("current")


class _StGpsAvChassis_Type(Integer32):
    """Custom type stGpsAvChassis based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
    )


_StGpsAvChassis_Type.__name__ = "Integer32"
_StGpsAvChassis_Object = MibTableColumn
stGpsAvChassis = _StGpsAvChassis_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 2, 5, 3, 1, 1),
    _StGpsAvChassis_Type()
)
stGpsAvChassis.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    stGpsAvChassis.setStatus("current")


class _StGpsAvSlot_Type(Integer32):
    """Custom type stGpsAvSlot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 20),
    )


_StGpsAvSlot_Type.__name__ = "Integer32"
_StGpsAvSlot_Object = MibTableColumn
stGpsAvSlot = _StGpsAvSlot_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 2, 5, 3, 1, 2),
    _StGpsAvSlot_Type()
)
stGpsAvSlot.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    stGpsAvSlot.setStatus("current")


class _StGpsAvChnl_Type(Integer32):
    """Custom type stGpsAvChnl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_StGpsAvChnl_Type.__name__ = "Integer32"
_StGpsAvChnl_Object = MibTableColumn
stGpsAvChnl = _StGpsAvChnl_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 2, 5, 3, 1, 3),
    _StGpsAvChnl_Type()
)
stGpsAvChnl.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    stGpsAvChnl.setStatus("current")


class _StGpsAvPNCode_Type(Integer32):
    """Custom type stGpsAvPNCode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 99),
    )


_StGpsAvPNCode_Type.__name__ = "Integer32"
_StGpsAvPNCode_Object = MibTableColumn
stGpsAvPNCode = _StGpsAvPNCode_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 2, 5, 3, 1, 4),
    _StGpsAvPNCode_Type()
)
stGpsAvPNCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stGpsAvPNCode.setStatus("current")


class _StGpsAvElevation_Type(Integer32):
    """Custom type stGpsAvElevation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 90),
    )


_StGpsAvElevation_Type.__name__ = "Integer32"
_StGpsAvElevation_Object = MibTableColumn
stGpsAvElevation = _StGpsAvElevation_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 2, 5, 3, 1, 5),
    _StGpsAvElevation_Type()
)
stGpsAvElevation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stGpsAvElevation.setStatus("current")


class _StGpsAvAzimuth_Type(Integer32):
    """Custom type stGpsAvAzimuth based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 360),
    )


_StGpsAvAzimuth_Type.__name__ = "Integer32"
_StGpsAvAzimuth_Object = MibTableColumn
stGpsAvAzimuth = _StGpsAvAzimuth_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 2, 5, 3, 1, 6),
    _StGpsAvAzimuth_Type()
)
stGpsAvAzimuth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stGpsAvAzimuth.setStatus("current")
_StGpsAvHealthy_Type = YesValue
_StGpsAvHealthy_Object = MibTableColumn
stGpsAvHealthy = _StGpsAvHealthy_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 2, 5, 3, 1, 7),
    _StGpsAvHealthy_Type()
)
stGpsAvHealthy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stGpsAvHealthy.setStatus("current")
_StGpsTrackTable_Object = MibTable
stGpsTrackTable = _StGpsTrackTable_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 2, 5, 5)
)
if mibBuilder.loadTexts:
    stGpsTrackTable.setStatus("current")
_StGpsTkEntry_Object = MibTableRow
stGpsTkEntry = _StGpsTkEntry_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 2, 5, 5, 1)
)
stGpsTkEntry.setIndexNames(
    (0, "SSU2000-MIB", "stGpsTkChassis"),
    (0, "SSU2000-MIB", "stGpsTkSlot"),
    (0, "SSU2000-MIB", "stGpsTkChnl"),
)
if mibBuilder.loadTexts:
    stGpsTkEntry.setStatus("current")


class _StGpsTkChassis_Type(Integer32):
    """Custom type stGpsTkChassis based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
    )


_StGpsTkChassis_Type.__name__ = "Integer32"
_StGpsTkChassis_Object = MibTableColumn
stGpsTkChassis = _StGpsTkChassis_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 2, 5, 5, 1, 1),
    _StGpsTkChassis_Type()
)
stGpsTkChassis.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    stGpsTkChassis.setStatus("current")


class _StGpsTkSlot_Type(Integer32):
    """Custom type stGpsTkSlot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 20),
    )


_StGpsTkSlot_Type.__name__ = "Integer32"
_StGpsTkSlot_Object = MibTableColumn
stGpsTkSlot = _StGpsTkSlot_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 2, 5, 5, 1, 2),
    _StGpsTkSlot_Type()
)
stGpsTkSlot.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    stGpsTkSlot.setStatus("current")


class _StGpsTkChnl_Type(Integer32):
    """Custom type stGpsTkChnl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_StGpsTkChnl_Type.__name__ = "Integer32"
_StGpsTkChnl_Object = MibTableColumn
stGpsTkChnl = _StGpsTkChnl_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 2, 5, 5, 1, 3),
    _StGpsTkChnl_Type()
)
stGpsTkChnl.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    stGpsTkChnl.setStatus("current")


class _StGpsTkSv_Type(Integer32):
    """Custom type stGpsTkSv based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 32),
    )


_StGpsTkSv_Type.__name__ = "Integer32"
_StGpsTkSv_Object = MibTableColumn
stGpsTkSv = _StGpsTkSv_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 2, 5, 5, 1, 4),
    _StGpsTkSv_Type()
)
stGpsTkSv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stGpsTkSv.setStatus("current")


class _StGpsTkSnr_Type(Integer32):
    """Custom type stGpsTkSnr based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 255),
    )


_StGpsTkSnr_Type.__name__ = "Integer32"
_StGpsTkSnr_Object = MibTableColumn
stGpsTkSnr = _StGpsTkSnr_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 2, 5, 5, 1, 5),
    _StGpsTkSnr_Type()
)
stGpsTkSnr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stGpsTkSnr.setStatus("current")


class _StGpsTkStatus_Type(Integer32):
    """Custom type stGpsTkStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9)
        )
    )
    namedValues = NamedValues(
        *(("src", 1),
          ("acq", 2),
          ("agc", 3),
          ("frq", 4),
          ("cod", 5),
          ("msg", 6),
          ("tim", 7),
          ("eph", 8),
          ("ok", 9))
    )


_StGpsTkStatus_Type.__name__ = "Integer32"
_StGpsTkStatus_Object = MibTableColumn
stGpsTkStatus = _StGpsTkStatus_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 2, 5, 5, 1, 6),
    _StGpsTkStatus_Type()
)
stGpsTkStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stGpsTkStatus.setStatus("current")
_StatusDs1E1Inp_ObjectIdentity = ObjectIdentity
statusDs1E1Inp = _StatusDs1E1Inp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 2, 7)
)
_StaDs1E1InpTable_Object = MibTable
staDs1E1InpTable = _StaDs1E1InpTable_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 2, 7, 2)
)
if mibBuilder.loadTexts:
    staDs1E1InpTable.setStatus("current")
_StaDiEntry_Object = MibTableRow
staDiEntry = _StaDiEntry_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 2, 7, 2, 1)
)
staDiEntry.setIndexNames(
    (0, "SSU2000-MIB", "staDiChassis"),
    (0, "SSU2000-MIB", "staDiSlot"),
    (0, "SSU2000-MIB", "staDiPort"),
)
if mibBuilder.loadTexts:
    staDiEntry.setStatus("current")


class _StaDiChassis_Type(Integer32):
    """Custom type staDiChassis based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
    )


_StaDiChassis_Type.__name__ = "Integer32"
_StaDiChassis_Object = MibTableColumn
staDiChassis = _StaDiChassis_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 2, 7, 2, 1, 1),
    _StaDiChassis_Type()
)
staDiChassis.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    staDiChassis.setStatus("current")


class _StaDiSlot_Type(Integer32):
    """Custom type staDiSlot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 20),
    )


_StaDiSlot_Type.__name__ = "Integer32"
_StaDiSlot_Object = MibTableColumn
staDiSlot = _StaDiSlot_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 2, 7, 2, 1, 2),
    _StaDiSlot_Type()
)
staDiSlot.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    staDiSlot.setStatus("current")


class _StaDiPort_Type(Integer32):
    """Custom type staDiPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_StaDiPort_Type.__name__ = "Integer32"
_StaDiPort_Object = MibTableColumn
staDiPort = _StaDiPort_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 2, 7, 2, 1, 3),
    _StaDiPort_Type()
)
staDiPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    staDiPort.setStatus("current")


class _StaDiStatus_Type(Integer32):
    """Custom type staDiStatus based on Integer32"""
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
        *(("ok", 1),
          ("selected", 2),
          ("disable", 3),
          ("fault", 4))
    )


_StaDiStatus_Type.__name__ = "Integer32"
_StaDiStatus_Object = MibTableColumn
staDiStatus = _StaDiStatus_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 2, 7, 2, 1, 4),
    _StaDiStatus_Type()
)
staDiStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staDiStatus.setStatus("current")


class _StaDiPhaseA_Type(Integer32):
    """Custom type staDiPhaseA based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1999999998, 1999999998),
        ValueRangeConstraint(1999999999, 1999999999),
    )


_StaDiPhaseA_Type.__name__ = "Integer32"
_StaDiPhaseA_Object = MibTableColumn
staDiPhaseA = _StaDiPhaseA_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 2, 7, 2, 1, 5),
    _StaDiPhaseA_Type()
)
staDiPhaseA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staDiPhaseA.setStatus("current")


class _StaDiPhaseB_Type(Integer32):
    """Custom type staDiPhaseB based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1999999998, 1999999998),
        ValueRangeConstraint(1999999999, 1999999999),
    )


_StaDiPhaseB_Type.__name__ = "Integer32"
_StaDiPhaseB_Object = MibTableColumn
staDiPhaseB = _StaDiPhaseB_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 2, 7, 2, 1, 6),
    _StaDiPhaseB_Type()
)
staDiPhaseB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staDiPhaseB.setStatus("current")


class _StaDiPql_Type(Integer32):
    """Custom type staDiPql based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 16),
    )


_StaDiPql_Type.__name__ = "Integer32"
_StaDiPql_Object = MibTableColumn
staDiPql = _StaDiPql_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 2, 7, 2, 1, 7),
    _StaDiPql_Type()
)
staDiPql.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staDiPql.setStatus("current")
_StaDiPqlRcv_Type = YesValue
_StaDiPqlRcv_Object = MibTableColumn
staDiPqlRcv = _StaDiPqlRcv_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 2, 7, 2, 1, 8),
    _StaDiPqlRcv_Type()
)
staDiPqlRcv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staDiPqlRcv.setStatus("current")
_StaDiLOS_Type = OkValue
_StaDiLOS_Object = MibTableColumn
staDiLOS = _StaDiLOS_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 2, 7, 2, 1, 9),
    _StaDiLOS_Type()
)
staDiLOS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staDiLOS.setStatus("current")
_StaDiAIS_Type = OkValue
_StaDiAIS_Object = MibTableColumn
staDiAIS = _StaDiAIS_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 2, 7, 2, 1, 10),
    _StaDiAIS_Type()
)
staDiAIS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staDiAIS.setStatus("current")
_StaDiOOF_Type = OkValue
_StaDiOOF_Object = MibTableColumn
staDiOOF = _StaDiOOF_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 2, 7, 2, 1, 11),
    _StaDiOOF_Type()
)
staDiOOF.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staDiOOF.setStatus("current")
_StaDiBPV_Type = OkValue
_StaDiBPV_Object = MibTableColumn
staDiBPV = _StaDiBPV_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 2, 7, 2, 1, 12),
    _StaDiBPV_Type()
)
staDiBPV.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staDiBPV.setStatus("current")
_StaDiCRC_Type = OkValue
_StaDiCRC_Object = MibTableColumn
staDiCRC = _StaDiCRC_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 2, 7, 2, 1, 13),
    _StaDiCRC_Type()
)
staDiCRC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staDiCRC.setStatus("current")


class _StaDiMtie1A_Type(Integer32):
    """Custom type staDiMtie1A based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              10,
              100,
              1000,
              10000,
              100000)
        )
    )
    namedValues = NamedValues(
        *(("ok", 1),
          ("mtie10", 10),
          ("mtie100", 100),
          ("mtie1000", 1000),
          ("mtie10000", 10000),
          ("mtie100000", 100000))
    )


_StaDiMtie1A_Type.__name__ = "Integer32"
_StaDiMtie1A_Object = MibTableColumn
staDiMtie1A = _StaDiMtie1A_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 2, 7, 2, 1, 14),
    _StaDiMtie1A_Type()
)
staDiMtie1A.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staDiMtie1A.setStatus("current")


class _StaDiMtie2A_Type(Integer32):
    """Custom type staDiMtie2A based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              10,
              100,
              1000,
              10000,
              100000)
        )
    )
    namedValues = NamedValues(
        *(("ok", 1),
          ("mtie10", 10),
          ("mtie100", 100),
          ("mtie1000", 1000),
          ("mtie10000", 10000),
          ("mtie100000", 100000))
    )


_StaDiMtie2A_Type.__name__ = "Integer32"
_StaDiMtie2A_Object = MibTableColumn
staDiMtie2A = _StaDiMtie2A_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 2, 7, 2, 1, 15),
    _StaDiMtie2A_Type()
)
staDiMtie2A.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staDiMtie2A.setStatus("current")


class _StaDiMtie1B_Type(Integer32):
    """Custom type staDiMtie1B based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              10,
              100,
              1000,
              10000,
              100000)
        )
    )
    namedValues = NamedValues(
        *(("ok", 1),
          ("mtie10", 10),
          ("mtie100", 100),
          ("mtie1000", 1000),
          ("mtie10000", 10000),
          ("mtie100000", 100000))
    )


_StaDiMtie1B_Type.__name__ = "Integer32"
_StaDiMtie1B_Object = MibTableColumn
staDiMtie1B = _StaDiMtie1B_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 2, 7, 2, 1, 16),
    _StaDiMtie1B_Type()
)
staDiMtie1B.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staDiMtie1B.setStatus("current")


class _StaDiMtie2B_Type(Integer32):
    """Custom type staDiMtie2B based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              10,
              100,
              1000,
              10000,
              100000)
        )
    )
    namedValues = NamedValues(
        *(("ok", 1),
          ("mtie10", 10),
          ("mtie100", 100),
          ("mtie1000", 1000),
          ("mtie10000", 10000),
          ("mtie100000", 100000))
    )


_StaDiMtie2B_Type.__name__ = "Integer32"
_StaDiMtie2B_Object = MibTableColumn
staDiMtie2B = _StaDiMtie2B_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 2, 7, 2, 1, 17),
    _StaDiMtie2B_Type()
)
staDiMtie2B.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staDiMtie2B.setStatus("current")
_StaDiFreqA_Type = OkValue
_StaDiFreqA_Object = MibTableColumn
staDiFreqA = _StaDiFreqA_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 2, 7, 2, 1, 18),
    _StaDiFreqA_Type()
)
staDiFreqA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staDiFreqA.setStatus("current")
_StaDiFreqB_Type = OkValue
_StaDiFreqB_Object = MibTableColumn
staDiFreqB = _StaDiFreqB_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 2, 7, 2, 1, 19),
    _StaDiFreqB_Type()
)
staDiFreqB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staDiFreqB.setStatus("current")
_StaLOSErCnt_Type = Counter32
_StaLOSErCnt_Object = MibTableColumn
staLOSErCnt = _StaLOSErCnt_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 2, 7, 2, 1, 20),
    _StaLOSErCnt_Type()
)
staLOSErCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staLOSErCnt.setStatus("current")
_StaLOSClCnt_Type = Counter32
_StaLOSClCnt_Object = MibTableColumn
staLOSClCnt = _StaLOSClCnt_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 2, 7, 2, 1, 21),
    _StaLOSClCnt_Type()
)
staLOSClCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staLOSClCnt.setStatus("current")
_StaAISErCnt_Type = Counter32
_StaAISErCnt_Object = MibTableColumn
staAISErCnt = _StaAISErCnt_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 2, 7, 2, 1, 22),
    _StaAISErCnt_Type()
)
staAISErCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staAISErCnt.setStatus("current")
_StaAISClCnt_Type = Counter32
_StaAISClCnt_Object = MibTableColumn
staAISClCnt = _StaAISClCnt_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 2, 7, 2, 1, 23),
    _StaAISClCnt_Type()
)
staAISClCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staAISClCnt.setStatus("current")
_StaOOFErCnt_Type = Counter32
_StaOOFErCnt_Object = MibTableColumn
staOOFErCnt = _StaOOFErCnt_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 2, 7, 2, 1, 24),
    _StaOOFErCnt_Type()
)
staOOFErCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staOOFErCnt.setStatus("current")
_StaOOFClCnt_Type = Counter32
_StaOOFClCnt_Object = MibTableColumn
staOOFClCnt = _StaOOFClCnt_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 2, 7, 2, 1, 25),
    _StaOOFClCnt_Type()
)
staOOFClCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staOOFClCnt.setStatus("current")
_StaBPVErCnt_Type = Counter32
_StaBPVErCnt_Object = MibTableColumn
staBPVErCnt = _StaBPVErCnt_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 2, 7, 2, 1, 26),
    _StaBPVErCnt_Type()
)
staBPVErCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staBPVErCnt.setStatus("current")
_StaBPVClCnt_Type = Counter32
_StaBPVClCnt_Object = MibTableColumn
staBPVClCnt = _StaBPVClCnt_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 2, 7, 2, 1, 27),
    _StaBPVClCnt_Type()
)
staBPVClCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staBPVClCnt.setStatus("current")
_StaCRCErCnt_Type = Counter32
_StaCRCErCnt_Object = MibTableColumn
staCRCErCnt = _StaCRCErCnt_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 2, 7, 2, 1, 28),
    _StaCRCErCnt_Type()
)
staCRCErCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staCRCErCnt.setStatus("current")
_StaCRCClCnt_Type = Counter32
_StaCRCClCnt_Object = MibTableColumn
staCRCClCnt = _StaCRCClCnt_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 2, 7, 2, 1, 29),
    _StaCRCClCnt_Type()
)
staCRCClCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staCRCClCnt.setStatus("current")


class _StaDiMStatus_Type(Integer32):
    """Custom type staDiMStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("ok", 1),
          ("disable", 2),
          ("fault", 3))
    )


_StaDiMStatus_Type.__name__ = "Integer32"
_StaDiMStatus_Object = MibTableColumn
staDiMStatus = _StaDiMStatus_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 2, 7, 2, 1, 30),
    _StaDiMStatus_Type()
)
staDiMStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staDiMStatus.setStatus("current")
_StatusCcInp_ObjectIdentity = ObjectIdentity
statusCcInp = _StatusCcInp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 2, 8)
)
_StaCcInpTable_Object = MibTable
staCcInpTable = _StaCcInpTable_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 2, 8, 2)
)
if mibBuilder.loadTexts:
    staCcInpTable.setStatus("current")
_StaCiEntry_Object = MibTableRow
staCiEntry = _StaCiEntry_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 2, 8, 2, 1)
)
staCiEntry.setIndexNames(
    (0, "SSU2000-MIB", "staCiChassis"),
    (0, "SSU2000-MIB", "staCiSlot"),
    (0, "SSU2000-MIB", "staCiPort"),
)
if mibBuilder.loadTexts:
    staCiEntry.setStatus("current")


class _StaCiChassis_Type(Integer32):
    """Custom type staCiChassis based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
    )


_StaCiChassis_Type.__name__ = "Integer32"
_StaCiChassis_Object = MibTableColumn
staCiChassis = _StaCiChassis_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 2, 8, 2, 1, 1),
    _StaCiChassis_Type()
)
staCiChassis.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    staCiChassis.setStatus("current")


class _StaCiSlot_Type(Integer32):
    """Custom type staCiSlot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 20),
    )


_StaCiSlot_Type.__name__ = "Integer32"
_StaCiSlot_Object = MibTableColumn
staCiSlot = _StaCiSlot_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 2, 8, 2, 1, 2),
    _StaCiSlot_Type()
)
staCiSlot.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    staCiSlot.setStatus("current")


class _StaCiPort_Type(Integer32):
    """Custom type staCiPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_StaCiPort_Type.__name__ = "Integer32"
_StaCiPort_Object = MibTableColumn
staCiPort = _StaCiPort_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 2, 8, 2, 1, 3),
    _StaCiPort_Type()
)
staCiPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    staCiPort.setStatus("current")


class _StaCiStatus_Type(Integer32):
    """Custom type staCiStatus based on Integer32"""
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
        *(("ok", 1),
          ("selected", 2),
          ("disable", 3),
          ("fault", 4))
    )


_StaCiStatus_Type.__name__ = "Integer32"
_StaCiStatus_Object = MibTableColumn
staCiStatus = _StaCiStatus_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 2, 8, 2, 1, 4),
    _StaCiStatus_Type()
)
staCiStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staCiStatus.setStatus("current")


class _StaCiPhaseA_Type(Integer32):
    """Custom type staCiPhaseA based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1999999998, 1999999998),
        ValueRangeConstraint(1999999999, 1999999999),
    )


_StaCiPhaseA_Type.__name__ = "Integer32"
_StaCiPhaseA_Object = MibTableColumn
staCiPhaseA = _StaCiPhaseA_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 2, 8, 2, 1, 5),
    _StaCiPhaseA_Type()
)
staCiPhaseA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staCiPhaseA.setStatus("current")


class _StaCiPhaseB_Type(Integer32):
    """Custom type staCiPhaseB based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1999999998, 1999999998),
        ValueRangeConstraint(1999999999, 1999999999),
    )


_StaCiPhaseB_Type.__name__ = "Integer32"
_StaCiPhaseB_Object = MibTableColumn
staCiPhaseB = _StaCiPhaseB_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 2, 8, 2, 1, 6),
    _StaCiPhaseB_Type()
)
staCiPhaseB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staCiPhaseB.setStatus("current")
_StaCiLOS_Type = OkValue
_StaCiLOS_Object = MibTableColumn
staCiLOS = _StaCiLOS_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 2, 8, 2, 1, 9),
    _StaCiLOS_Type()
)
staCiLOS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staCiLOS.setStatus("current")
_StaCiBPV_Type = OkValue
_StaCiBPV_Object = MibTableColumn
staCiBPV = _StaCiBPV_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 2, 8, 2, 1, 12),
    _StaCiBPV_Type()
)
staCiBPV.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staCiBPV.setStatus("current")
_StaCiLOSErCnt_Type = Counter32
_StaCiLOSErCnt_Object = MibTableColumn
staCiLOSErCnt = _StaCiLOSErCnt_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 2, 8, 2, 1, 14),
    _StaCiLOSErCnt_Type()
)
staCiLOSErCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staCiLOSErCnt.setStatus("current")
_StaCiLOSClCnt_Type = Counter32
_StaCiLOSClCnt_Object = MibTableColumn
staCiLOSClCnt = _StaCiLOSClCnt_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 2, 8, 2, 1, 15),
    _StaCiLOSClCnt_Type()
)
staCiLOSClCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staCiLOSClCnt.setStatus("current")
_StaCiBPVErCnt_Type = Counter32
_StaCiBPVErCnt_Object = MibTableColumn
staCiBPVErCnt = _StaCiBPVErCnt_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 2, 8, 2, 1, 20),
    _StaCiBPVErCnt_Type()
)
staCiBPVErCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staCiBPVErCnt.setStatus("current")
_StaCiBPVClCnt_Type = Counter32
_StaCiBPVClCnt_Object = MibTableColumn
staCiBPVClCnt = _StaCiBPVClCnt_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 2, 8, 2, 1, 21),
    _StaCiBPVClCnt_Type()
)
staCiBPVClCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staCiBPVClCnt.setStatus("current")


class _StaCiMStatus_Type(Integer32):
    """Custom type staCiMStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("ok", 1),
          ("disable", 2),
          ("fault", 3))
    )


_StaCiMStatus_Type.__name__ = "Integer32"
_StaCiMStatus_Object = MibTableColumn
staCiMStatus = _StaCiMStatus_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 2, 8, 2, 1, 24),
    _StaCiMStatus_Type()
)
staCiMStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staCiMStatus.setStatus("current")
_StatusOut_ObjectIdentity = ObjectIdentity
statusOut = _StatusOut_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 2, 10)
)
_StaOutTable_Object = MibTable
staOutTable = _StaOutTable_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 2, 10, 2)
)
if mibBuilder.loadTexts:
    staOutTable.setStatus("current")
_StaOtEntry_Object = MibTableRow
staOtEntry = _StaOtEntry_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 2, 10, 2, 1)
)
staOtEntry.setIndexNames(
    (0, "SSU2000-MIB", "staOtChassis"),
    (0, "SSU2000-MIB", "staOtSlot"),
)
if mibBuilder.loadTexts:
    staOtEntry.setStatus("current")


class _StaOtChassis_Type(Integer32):
    """Custom type staOtChassis based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_StaOtChassis_Type.__name__ = "Integer32"
_StaOtChassis_Object = MibTableColumn
staOtChassis = _StaOtChassis_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 2, 10, 2, 1, 1),
    _StaOtChassis_Type()
)
staOtChassis.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    staOtChassis.setStatus("current")


class _StaOtSlot_Type(Integer32):
    """Custom type staOtSlot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 20),
    )


_StaOtSlot_Type.__name__ = "Integer32"
_StaOtSlot_Object = MibTableColumn
staOtSlot = _StaOtSlot_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 2, 10, 2, 1, 2),
    _StaOtSlot_Type()
)
staOtSlot.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    staOtSlot.setStatus("current")


class _StaOtStatus_Type(Integer32):
    """Custom type staOtStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("ok", 1),
          ("disable", 3),
          ("fault", 4),
          ("reject", 5))
    )


_StaOtStatus_Type.__name__ = "Integer32"
_StaOtStatus_Object = MibTableColumn
staOtStatus = _StaOtStatus_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 2, 10, 2, 1, 3),
    _StaOtStatus_Type()
)
staOtStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staOtStatus.setStatus("current")


class _StaOtClkSel_Type(Integer32):
    """Custom type staOtClkSel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("clka", 1),
          ("clkb", 2),
          ("clkc", 3),
          ("clkd", 4),
          ("none", 5))
    )


_StaOtClkSel_Type.__name__ = "Integer32"
_StaOtClkSel_Object = MibTableColumn
staOtClkSel = _StaOtClkSel_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 2, 10, 2, 1, 4),
    _StaOtClkSel_Type()
)
staOtClkSel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staOtClkSel.setStatus("current")
_StaOtClka_Type = ActiveValue
_StaOtClka_Object = MibTableColumn
staOtClka = _StaOtClka_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 2, 10, 2, 1, 5),
    _StaOtClka_Type()
)
staOtClka.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staOtClka.setStatus("current")
_StaOtClkb_Type = ActiveValue
_StaOtClkb_Object = MibTableColumn
staOtClkb = _StaOtClkb_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 2, 10, 2, 1, 6),
    _StaOtClkb_Type()
)
staOtClkb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staOtClkb.setStatus("current")
_StaOtClkc_Type = ActiveValue
_StaOtClkc_Object = MibTableColumn
staOtClkc = _StaOtClkc_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 2, 10, 2, 1, 7),
    _StaOtClkc_Type()
)
staOtClkc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staOtClkc.setStatus("current")
_StaOtClkd_Type = ActiveValue
_StaOtClkd_Object = MibTableColumn
staOtClkd = _StaOtClkd_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 2, 10, 2, 1, 8),
    _StaOtClkd_Type()
)
staOtClkd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staOtClkd.setStatus("current")


class _StaOtRednt_Type(Integer32):
    """Custom type staOtRednt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 20),
    )


_StaOtRednt_Type.__name__ = "Integer32"
_StaOtRednt_Object = MibTableColumn
staOtRednt = _StaOtRednt_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 2, 10, 2, 1, 9),
    _StaOtRednt_Type()
)
staOtRednt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staOtRednt.setStatus("current")


class _StaOtPql_Type(Integer32):
    """Custom type staOtPql based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 16),
    )


_StaOtPql_Type.__name__ = "Integer32"
_StaOtPql_Object = MibTableColumn
staOtPql = _StaOtPql_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 2, 10, 2, 1, 10),
    _StaOtPql_Type()
)
staOtPql.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staOtPql.setStatus("current")


class _StaOtPortSta_Type(OctetString):
    """Custom type staOtPortSta based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(20, 20),
    )
    fixed_length = 20


_StaOtPortSta_Type.__name__ = "OctetString"
_StaOtPortSta_Object = MibTableColumn
staOtPortSta = _StaOtPortSta_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 2, 10, 2, 1, 11),
    _StaOtPortSta_Type()
)
staOtPortSta.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staOtPortSta.setStatus("current")
_StatusLrm_ObjectIdentity = ObjectIdentity
statusLrm = _StatusLrm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 2, 11)
)
_StaLrmMTable_Object = MibTable
staLrmMTable = _StaLrmMTable_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 2, 11, 2)
)
if mibBuilder.loadTexts:
    staLrmMTable.setStatus("current")
_StaLrmMEntry_Object = MibTableRow
staLrmMEntry = _StaLrmMEntry_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 2, 11, 2, 1)
)
staLrmMEntry.setIndexNames(
    (0, "SSU2000-MIB", "staLrmMChassis"),
    (0, "SSU2000-MIB", "staLrmMSlot"),
)
if mibBuilder.loadTexts:
    staLrmMEntry.setStatus("current")


class _StaLrmMChassis_Type(Integer32):
    """Custom type staLrmMChassis based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_StaLrmMChassis_Type.__name__ = "Integer32"
_StaLrmMChassis_Object = MibTableColumn
staLrmMChassis = _StaLrmMChassis_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 2, 11, 2, 1, 1),
    _StaLrmMChassis_Type()
)
staLrmMChassis.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    staLrmMChassis.setStatus("current")


class _StaLrmMSlot_Type(Integer32):
    """Custom type staLrmMSlot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 20),
    )


_StaLrmMSlot_Type.__name__ = "Integer32"
_StaLrmMSlot_Object = MibTableColumn
staLrmMSlot = _StaLrmMSlot_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 2, 11, 2, 1, 2),
    _StaLrmMSlot_Type()
)
staLrmMSlot.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    staLrmMSlot.setStatus("current")


class _StaLrmMStatus_Type(Integer32):
    """Custom type staLrmMStatus based on Integer32"""
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


_StaLrmMStatus_Type.__name__ = "Integer32"
_StaLrmMStatus_Object = MibTableColumn
staLrmMStatus = _StaLrmMStatus_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 2, 11, 2, 1, 3),
    _StaLrmMStatus_Type()
)
staLrmMStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staLrmMStatus.setStatus("current")


class _StaLrmMRefSrc_Type(Integer32):
    """Custom type staLrmMRefSrc based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("clka", 1),
          ("clkb", 2),
          ("clkc", 3),
          ("clkd", 4),
          ("none", 5),
          ("pllflt", 6))
    )


_StaLrmMRefSrc_Type.__name__ = "Integer32"
_StaLrmMRefSrc_Object = MibTableColumn
staLrmMRefSrc = _StaLrmMRefSrc_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 2, 11, 2, 1, 4),
    _StaLrmMRefSrc_Type()
)
staLrmMRefSrc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staLrmMRefSrc.setStatus("current")


class _StaLrmMCtaId_Type(Integer32):
    """Custom type staLrmMCtaId based on Integer32"""
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
        *(("dual", 1),
          ("quad", 2),
          ("none", 3),
          ("unknown", 4))
    )


_StaLrmMCtaId_Type.__name__ = "Integer32"
_StaLrmMCtaId_Object = MibTableColumn
staLrmMCtaId = _StaLrmMCtaId_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 2, 11, 2, 1, 5),
    _StaLrmMCtaId_Type()
)
staLrmMCtaId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staLrmMCtaId.setStatus("current")
_StaLrmPTable_Object = MibTable
staLrmPTable = _StaLrmPTable_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 2, 11, 3)
)
if mibBuilder.loadTexts:
    staLrmPTable.setStatus("current")
_StaLrmPEntry_Object = MibTableRow
staLrmPEntry = _StaLrmPEntry_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 2, 11, 3, 1)
)
staLrmPEntry.setIndexNames(
    (0, "SSU2000-MIB", "staLrmPChassis"),
    (0, "SSU2000-MIB", "staLrmPSlot"),
    (0, "SSU2000-MIB", "staLrmPPort"),
)
if mibBuilder.loadTexts:
    staLrmPEntry.setStatus("current")


class _StaLrmPChassis_Type(Integer32):
    """Custom type staLrmPChassis based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_StaLrmPChassis_Type.__name__ = "Integer32"
_StaLrmPChassis_Object = MibTableColumn
staLrmPChassis = _StaLrmPChassis_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 2, 11, 3, 1, 1),
    _StaLrmPChassis_Type()
)
staLrmPChassis.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    staLrmPChassis.setStatus("current")


class _StaLrmPSlot_Type(Integer32):
    """Custom type staLrmPSlot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 20),
    )


_StaLrmPSlot_Type.__name__ = "Integer32"
_StaLrmPSlot_Object = MibTableColumn
staLrmPSlot = _StaLrmPSlot_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 2, 11, 3, 1, 2),
    _StaLrmPSlot_Type()
)
staLrmPSlot.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    staLrmPSlot.setStatus("current")


class _StaLrmPPort_Type(Integer32):
    """Custom type staLrmPPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_StaLrmPPort_Type.__name__ = "Integer32"
_StaLrmPPort_Object = MibTableColumn
staLrmPPort = _StaLrmPPort_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 2, 11, 3, 1, 3),
    _StaLrmPPort_Type()
)
staLrmPPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    staLrmPPort.setStatus("current")


class _StaLrmPStatus_Type(Integer32):
    """Custom type staLrmPStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("ok", 1),
          ("cut", 2),
          ("disable", 3))
    )


_StaLrmPStatus_Type.__name__ = "Integer32"
_StaLrmPStatus_Object = MibTableColumn
staLrmPStatus = _StaLrmPStatus_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 2, 11, 3, 1, 4),
    _StaLrmPStatus_Type()
)
staLrmPStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staLrmPStatus.setStatus("current")


class _StaLrmPFrame_Type(Integer32):
    """Custom type staLrmPFrame based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("d4", 1),
          ("esf", 2),
          ("none", 3))
    )


_StaLrmPFrame_Type.__name__ = "Integer32"
_StaLrmPFrame_Object = MibTableColumn
staLrmPFrame = _StaLrmPFrame_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 2, 11, 3, 1, 5),
    _StaLrmPFrame_Type()
)
staLrmPFrame.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staLrmPFrame.setStatus("current")
_StaLrmPLos_Type = OkValue
_StaLrmPLos_Object = MibTableColumn
staLrmPLos = _StaLrmPLos_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 2, 11, 3, 1, 6),
    _StaLrmPLos_Type()
)
staLrmPLos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staLrmPLos.setStatus("current")
_StaLrmPAis_Type = OkValue
_StaLrmPAis_Object = MibTableColumn
staLrmPAis = _StaLrmPAis_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 2, 11, 3, 1, 7),
    _StaLrmPAis_Type()
)
staLrmPAis.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staLrmPAis.setStatus("current")
_StaLrmPLof_Type = OkValue
_StaLrmPLof_Object = MibTableColumn
staLrmPLof = _StaLrmPLof_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 2, 11, 3, 1, 8),
    _StaLrmPLof_Type()
)
staLrmPLof.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staLrmPLof.setStatus("current")
_StaLrmPBpv_Type = OkValue
_StaLrmPBpv_Object = MibTableColumn
staLrmPBpv = _StaLrmPBpv_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 2, 11, 3, 1, 9),
    _StaLrmPBpv_Type()
)
staLrmPBpv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staLrmPBpv.setStatus("current")
_StaLrmPSlip_Type = OkValue
_StaLrmPSlip_Object = MibTableColumn
staLrmPSlip = _StaLrmPSlip_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 2, 11, 3, 1, 10),
    _StaLrmPSlip_Type()
)
staLrmPSlip.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staLrmPSlip.setStatus("current")
_StaLrmPSlips_Type = Counter32
_StaLrmPSlips_Object = MibTableColumn
staLrmPSlips = _StaLrmPSlips_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 2, 11, 3, 1, 11),
    _StaLrmPSlips_Type()
)
staLrmPSlips.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staLrmPSlips.setStatus("current")
_StaLrmPLosSide2_Type = OkValue
_StaLrmPLosSide2_Object = MibTableColumn
staLrmPLosSide2 = _StaLrmPLosSide2_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 2, 11, 3, 1, 12),
    _StaLrmPLosSide2_Type()
)
staLrmPLosSide2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staLrmPLosSide2.setStatus("current")
_StaLrmPBpvTestTime_Type = Counter32
_StaLrmPBpvTestTime_Object = MibTableColumn
staLrmPBpvTestTime = _StaLrmPBpvTestTime_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 2, 11, 3, 1, 13),
    _StaLrmPBpvTestTime_Type()
)
staLrmPBpvTestTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staLrmPBpvTestTime.setStatus("current")


class _StaLrmPBpv60SRate_Type(DisplayString):
    """Custom type staLrmPBpv60SRate based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_StaLrmPBpv60SRate_Type.__name__ = "DisplayString"
_StaLrmPBpv60SRate_Object = MibTableColumn
staLrmPBpv60SRate = _StaLrmPBpv60SRate_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 2, 11, 3, 1, 14),
    _StaLrmPBpv60SRate_Type()
)
staLrmPBpv60SRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staLrmPBpv60SRate.setStatus("current")


class _StaLrmPBpv24HRate_Type(DisplayString):
    """Custom type staLrmPBpv24HRate based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_StaLrmPBpv24HRate_Type.__name__ = "DisplayString"
_StaLrmPBpv24HRate_Object = MibTableColumn
staLrmPBpv24HRate = _StaLrmPBpv24HRate_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 2, 11, 3, 1, 15),
    _StaLrmPBpv24HRate_Type()
)
staLrmPBpv24HRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staLrmPBpv24HRate.setStatus("current")
_StaLrmPBpvErrSecs_Type = Counter32
_StaLrmPBpvErrSecs_Object = MibTableColumn
staLrmPBpvErrSecs = _StaLrmPBpvErrSecs_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 2, 11, 3, 1, 16),
    _StaLrmPBpvErrSecs_Type()
)
staLrmPBpvErrSecs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staLrmPBpvErrSecs.setStatus("current")
_StaLrmPBpvSevErrSecs_Type = Counter32
_StaLrmPBpvSevErrSecs_Object = MibTableColumn
staLrmPBpvSevErrSecs = _StaLrmPBpvSevErrSecs_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 2, 11, 3, 1, 17),
    _StaLrmPBpvSevErrSecs_Type()
)
staLrmPBpvSevErrSecs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staLrmPBpvSevErrSecs.setStatus("current")


class _StaLrmPBpvSevErrRatio_Type(DisplayString):
    """Custom type staLrmPBpvSevErrRatio based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_StaLrmPBpvSevErrRatio_Type.__name__ = "DisplayString"
_StaLrmPBpvSevErrRatio_Object = MibTableColumn
staLrmPBpvSevErrRatio = _StaLrmPBpvSevErrRatio_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 2, 11, 3, 1, 18),
    _StaLrmPBpvSevErrRatio_Type()
)
staLrmPBpvSevErrRatio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staLrmPBpvSevErrRatio.setStatus("current")
_StatusSineInp_ObjectIdentity = ObjectIdentity
statusSineInp = _StatusSineInp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 2, 12)
)
_StaSineInpTable_Object = MibTable
staSineInpTable = _StaSineInpTable_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 2, 12, 2)
)
if mibBuilder.loadTexts:
    staSineInpTable.setStatus("current")
_StaSineiEntry_Object = MibTableRow
staSineiEntry = _StaSineiEntry_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 2, 12, 2, 1)
)
staSineiEntry.setIndexNames(
    (0, "SSU2000-MIB", "staSineiChassis"),
    (0, "SSU2000-MIB", "staSineiSlot"),
    (0, "SSU2000-MIB", "staSineiPort"),
)
if mibBuilder.loadTexts:
    staSineiEntry.setStatus("current")


class _StaSineiChassis_Type(Integer32):
    """Custom type staSineiChassis based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
    )


_StaSineiChassis_Type.__name__ = "Integer32"
_StaSineiChassis_Object = MibTableColumn
staSineiChassis = _StaSineiChassis_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 2, 12, 2, 1, 1),
    _StaSineiChassis_Type()
)
staSineiChassis.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    staSineiChassis.setStatus("current")


class _StaSineiSlot_Type(Integer32):
    """Custom type staSineiSlot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 20),
    )


_StaSineiSlot_Type.__name__ = "Integer32"
_StaSineiSlot_Object = MibTableColumn
staSineiSlot = _StaSineiSlot_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 2, 12, 2, 1, 2),
    _StaSineiSlot_Type()
)
staSineiSlot.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    staSineiSlot.setStatus("current")


class _StaSineiPort_Type(Integer32):
    """Custom type staSineiPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_StaSineiPort_Type.__name__ = "Integer32"
_StaSineiPort_Object = MibTableColumn
staSineiPort = _StaSineiPort_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 2, 12, 2, 1, 3),
    _StaSineiPort_Type()
)
staSineiPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    staSineiPort.setStatus("current")


class _StaSineiStatus_Type(Integer32):
    """Custom type staSineiStatus based on Integer32"""
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
        *(("ok", 1),
          ("selected", 2),
          ("disable", 3),
          ("fault", 4))
    )


_StaSineiStatus_Type.__name__ = "Integer32"
_StaSineiStatus_Object = MibTableColumn
staSineiStatus = _StaSineiStatus_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 2, 12, 2, 1, 4),
    _StaSineiStatus_Type()
)
staSineiStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staSineiStatus.setStatus("current")


class _StaSineiPhaseA_Type(Integer32):
    """Custom type staSineiPhaseA based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1999999998, 1999999998),
        ValueRangeConstraint(1999999999, 1999999999),
    )


_StaSineiPhaseA_Type.__name__ = "Integer32"
_StaSineiPhaseA_Object = MibTableColumn
staSineiPhaseA = _StaSineiPhaseA_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 2, 12, 2, 1, 5),
    _StaSineiPhaseA_Type()
)
staSineiPhaseA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staSineiPhaseA.setStatus("current")


class _StaSineiPhaseB_Type(Integer32):
    """Custom type staSineiPhaseB based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1999999998, 1999999998),
        ValueRangeConstraint(1999999999, 1999999999),
    )


_StaSineiPhaseB_Type.__name__ = "Integer32"
_StaSineiPhaseB_Object = MibTableColumn
staSineiPhaseB = _StaSineiPhaseB_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 2, 12, 2, 1, 6),
    _StaSineiPhaseB_Type()
)
staSineiPhaseB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staSineiPhaseB.setStatus("current")
_StaSineiLOS_Type = OkValue
_StaSineiLOS_Object = MibTableColumn
staSineiLOS = _StaSineiLOS_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 2, 12, 2, 1, 7),
    _StaSineiLOS_Type()
)
staSineiLOS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staSineiLOS.setStatus("current")


class _StaSineiMStatus_Type(Integer32):
    """Custom type staSineiMStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("ok", 1),
          ("disable", 2),
          ("fault", 3))
    )


_StaSineiMStatus_Type.__name__ = "Integer32"
_StaSineiMStatus_Object = MibTableColumn
staSineiMStatus = _StaSineiMStatus_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 2, 12, 2, 1, 8),
    _StaSineiMStatus_Type()
)
staSineiMStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staSineiMStatus.setStatus("current")


class _StaSineiPql_Type(Integer32):
    """Custom type staSineiPql based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 16),
    )


_StaSineiPql_Type.__name__ = "Integer32"
_StaSineiPql_Object = MibTableColumn
staSineiPql = _StaSineiPql_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 2, 12, 2, 1, 9),
    _StaSineiPql_Type()
)
staSineiPql.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staSineiPql.setStatus("current")


class _StaSineiMtie1A_Type(Integer32):
    """Custom type staSineiMtie1A based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              10,
              100,
              1000,
              10000,
              100000)
        )
    )
    namedValues = NamedValues(
        *(("ok", 1),
          ("mtie10", 10),
          ("mtie100", 100),
          ("mtie1000", 1000),
          ("mtie10000", 10000),
          ("mtie100000", 100000))
    )


_StaSineiMtie1A_Type.__name__ = "Integer32"
_StaSineiMtie1A_Object = MibTableColumn
staSineiMtie1A = _StaSineiMtie1A_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 2, 12, 2, 1, 10),
    _StaSineiMtie1A_Type()
)
staSineiMtie1A.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staSineiMtie1A.setStatus("current")


class _StaSineiMtie2A_Type(Integer32):
    """Custom type staSineiMtie2A based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              10,
              100,
              1000,
              10000,
              100000)
        )
    )
    namedValues = NamedValues(
        *(("ok", 1),
          ("mtie10", 10),
          ("mtie100", 100),
          ("mtie1000", 1000),
          ("mtie10000", 10000),
          ("mtie100000", 100000))
    )


_StaSineiMtie2A_Type.__name__ = "Integer32"
_StaSineiMtie2A_Object = MibTableColumn
staSineiMtie2A = _StaSineiMtie2A_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 2, 12, 2, 1, 11),
    _StaSineiMtie2A_Type()
)
staSineiMtie2A.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staSineiMtie2A.setStatus("current")


class _StaSineiMtie1B_Type(Integer32):
    """Custom type staSineiMtie1B based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              10,
              100,
              1000,
              10000,
              100000)
        )
    )
    namedValues = NamedValues(
        *(("ok", 1),
          ("mtie10", 10),
          ("mtie100", 100),
          ("mtie1000", 1000),
          ("mtie10000", 10000),
          ("mtie100000", 100000))
    )


_StaSineiMtie1B_Type.__name__ = "Integer32"
_StaSineiMtie1B_Object = MibTableColumn
staSineiMtie1B = _StaSineiMtie1B_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 2, 12, 2, 1, 12),
    _StaSineiMtie1B_Type()
)
staSineiMtie1B.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staSineiMtie1B.setStatus("current")


class _StaSineiMtie2B_Type(Integer32):
    """Custom type staSineiMtie2B based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              10,
              100,
              1000,
              10000,
              100000)
        )
    )
    namedValues = NamedValues(
        *(("ok", 1),
          ("mtie10", 10),
          ("mtie100", 100),
          ("mtie1000", 1000),
          ("mtie10000", 10000),
          ("mtie100000", 100000))
    )


_StaSineiMtie2B_Type.__name__ = "Integer32"
_StaSineiMtie2B_Object = MibTableColumn
staSineiMtie2B = _StaSineiMtie2B_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 2, 12, 2, 1, 13),
    _StaSineiMtie2B_Type()
)
staSineiMtie2B.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staSineiMtie2B.setStatus("current")
_StaSineiFreqA_Type = OkValue
_StaSineiFreqA_Object = MibTableColumn
staSineiFreqA = _StaSineiFreqA_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 2, 12, 2, 1, 14),
    _StaSineiFreqA_Type()
)
staSineiFreqA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staSineiFreqA.setStatus("current")
_StaSineiFreqB_Type = OkValue
_StaSineiFreqB_Object = MibTableColumn
staSineiFreqB = _StaSineiFreqB_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 2, 12, 2, 1, 15),
    _StaSineiFreqB_Type()
)
staSineiFreqB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staSineiFreqB.setStatus("current")
_StatusJccInp_ObjectIdentity = ObjectIdentity
statusJccInp = _StatusJccInp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 2, 13)
)
_StaJccInpTable_Object = MibTable
staJccInpTable = _StaJccInpTable_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 2, 13, 2)
)
if mibBuilder.loadTexts:
    staJccInpTable.setStatus("current")
_StaJcciEntry_Object = MibTableRow
staJcciEntry = _StaJcciEntry_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 2, 13, 2, 1)
)
staJcciEntry.setIndexNames(
    (0, "SSU2000-MIB", "staCiChassis"),
    (0, "SSU2000-MIB", "staCiSlot"),
    (0, "SSU2000-MIB", "staCiPort"),
)
if mibBuilder.loadTexts:
    staJcciEntry.setStatus("current")


class _StaJcciChassis_Type(Integer32):
    """Custom type staJcciChassis based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
    )


_StaJcciChassis_Type.__name__ = "Integer32"
_StaJcciChassis_Object = MibTableColumn
staJcciChassis = _StaJcciChassis_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 2, 13, 2, 1, 1),
    _StaJcciChassis_Type()
)
staJcciChassis.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    staJcciChassis.setStatus("current")


class _StaJcciSlot_Type(Integer32):
    """Custom type staJcciSlot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 20),
    )


_StaJcciSlot_Type.__name__ = "Integer32"
_StaJcciSlot_Object = MibTableColumn
staJcciSlot = _StaJcciSlot_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 2, 13, 2, 1, 2),
    _StaJcciSlot_Type()
)
staJcciSlot.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    staJcciSlot.setStatus("current")


class _StaJcciPort_Type(Integer32):
    """Custom type staJcciPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_StaJcciPort_Type.__name__ = "Integer32"
_StaJcciPort_Object = MibTableColumn
staJcciPort = _StaJcciPort_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 2, 13, 2, 1, 3),
    _StaJcciPort_Type()
)
staJcciPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    staJcciPort.setStatus("current")


class _StaJcciStatus_Type(Integer32):
    """Custom type staJcciStatus based on Integer32"""
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
        *(("ok", 1),
          ("selected", 2),
          ("disable", 3),
          ("fault", 4))
    )


_StaJcciStatus_Type.__name__ = "Integer32"
_StaJcciStatus_Object = MibTableColumn
staJcciStatus = _StaJcciStatus_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 2, 13, 2, 1, 4),
    _StaJcciStatus_Type()
)
staJcciStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staJcciStatus.setStatus("current")


class _StaJcciPhaseA_Type(Integer32):
    """Custom type staJcciPhaseA based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1999999998, 1999999998),
        ValueRangeConstraint(1999999999, 1999999999),
    )


_StaJcciPhaseA_Type.__name__ = "Integer32"
_StaJcciPhaseA_Object = MibTableColumn
staJcciPhaseA = _StaJcciPhaseA_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 2, 13, 2, 1, 5),
    _StaJcciPhaseA_Type()
)
staJcciPhaseA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staJcciPhaseA.setStatus("current")


class _StaJcciPhaseB_Type(Integer32):
    """Custom type staJcciPhaseB based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1999999998, 1999999998),
        ValueRangeConstraint(1999999999, 1999999999),
    )


_StaJcciPhaseB_Type.__name__ = "Integer32"
_StaJcciPhaseB_Object = MibTableColumn
staJcciPhaseB = _StaJcciPhaseB_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 2, 13, 2, 1, 6),
    _StaJcciPhaseB_Type()
)
staJcciPhaseB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staJcciPhaseB.setStatus("current")
_StaJcciLOS_Type = OkValue
_StaJcciLOS_Object = MibTableColumn
staJcciLOS = _StaJcciLOS_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 2, 13, 2, 1, 7),
    _StaJcciLOS_Type()
)
staJcciLOS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staJcciLOS.setStatus("current")
_StaJcciBPV_Type = OkValue
_StaJcciBPV_Object = MibTableColumn
staJcciBPV = _StaJcciBPV_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 2, 13, 2, 1, 8),
    _StaJcciBPV_Type()
)
staJcciBPV.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staJcciBPV.setStatus("current")
_StaJcci400Hz_Type = OnValue
_StaJcci400Hz_Object = MibTableColumn
staJcci400Hz = _StaJcci400Hz_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 2, 13, 2, 1, 9),
    _StaJcci400Hz_Type()
)
staJcci400Hz.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staJcci400Hz.setStatus("current")


class _StaJcciMStatus_Type(Integer32):
    """Custom type staJcciMStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("ok", 1),
          ("disable", 2),
          ("fault", 3))
    )


_StaJcciMStatus_Type.__name__ = "Integer32"
_StaJcciMStatus_Object = MibTableColumn
staJcciMStatus = _StaJcciMStatus_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 2, 13, 2, 1, 10),
    _StaJcciMStatus_Type()
)
staJcciMStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staJcciMStatus.setStatus("current")
_StatusLrmE1_ObjectIdentity = ObjectIdentity
statusLrmE1 = _StatusLrmE1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 2, 14)
)
_StaLrme1MTable_Object = MibTable
staLrme1MTable = _StaLrme1MTable_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 2, 14, 2)
)
if mibBuilder.loadTexts:
    staLrme1MTable.setStatus("current")
_StaLrme1MEntry_Object = MibTableRow
staLrme1MEntry = _StaLrme1MEntry_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 2, 14, 2, 1)
)
staLrme1MEntry.setIndexNames(
    (0, "SSU2000-MIB", "staLrme1MChassis"),
    (0, "SSU2000-MIB", "staLrme1MSlot"),
)
if mibBuilder.loadTexts:
    staLrme1MEntry.setStatus("current")


class _StaLrme1MChassis_Type(Integer32):
    """Custom type staLrme1MChassis based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_StaLrme1MChassis_Type.__name__ = "Integer32"
_StaLrme1MChassis_Object = MibTableColumn
staLrme1MChassis = _StaLrme1MChassis_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 2, 14, 2, 1, 1),
    _StaLrme1MChassis_Type()
)
staLrme1MChassis.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    staLrme1MChassis.setStatus("current")


class _StaLrme1MSlot_Type(Integer32):
    """Custom type staLrme1MSlot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 20),
    )


_StaLrme1MSlot_Type.__name__ = "Integer32"
_StaLrme1MSlot_Object = MibTableColumn
staLrme1MSlot = _StaLrme1MSlot_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 2, 14, 2, 1, 2),
    _StaLrme1MSlot_Type()
)
staLrme1MSlot.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    staLrme1MSlot.setStatus("current")


class _StaLrme1MStatus_Type(Integer32):
    """Custom type staLrme1MStatus based on Integer32"""
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


_StaLrme1MStatus_Type.__name__ = "Integer32"
_StaLrme1MStatus_Object = MibTableColumn
staLrme1MStatus = _StaLrme1MStatus_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 2, 14, 2, 1, 3),
    _StaLrme1MStatus_Type()
)
staLrme1MStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staLrme1MStatus.setStatus("current")


class _StaLrme1MRefSrc_Type(Integer32):
    """Custom type staLrme1MRefSrc based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("clka", 1),
          ("clkb", 2),
          ("clkc", 3),
          ("clkd", 4),
          ("none", 5),
          ("pllflt", 6))
    )


_StaLrme1MRefSrc_Type.__name__ = "Integer32"
_StaLrme1MRefSrc_Object = MibTableColumn
staLrme1MRefSrc = _StaLrme1MRefSrc_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 2, 14, 2, 1, 4),
    _StaLrme1MRefSrc_Type()
)
staLrme1MRefSrc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staLrme1MRefSrc.setStatus("current")


class _StaLrme1MCtaId_Type(Integer32):
    """Custom type staLrme1MCtaId based on Integer32"""
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
        *(("dual", 1),
          ("quad", 2),
          ("none", 3),
          ("unknown", 4))
    )


_StaLrme1MCtaId_Type.__name__ = "Integer32"
_StaLrme1MCtaId_Object = MibTableColumn
staLrme1MCtaId = _StaLrme1MCtaId_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 2, 14, 2, 1, 5),
    _StaLrme1MCtaId_Type()
)
staLrme1MCtaId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staLrme1MCtaId.setStatus("current")
_StaLrme1PTable_Object = MibTable
staLrme1PTable = _StaLrme1PTable_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 2, 14, 3)
)
if mibBuilder.loadTexts:
    staLrme1PTable.setStatus("current")
_StaLrme1PEntry_Object = MibTableRow
staLrme1PEntry = _StaLrme1PEntry_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 2, 14, 3, 1)
)
staLrme1PEntry.setIndexNames(
    (0, "SSU2000-MIB", "staLrme1PChassis"),
    (0, "SSU2000-MIB", "staLrme1PSlot"),
    (0, "SSU2000-MIB", "staLrme1PPort"),
)
if mibBuilder.loadTexts:
    staLrme1PEntry.setStatus("current")


class _StaLrme1PChassis_Type(Integer32):
    """Custom type staLrme1PChassis based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_StaLrme1PChassis_Type.__name__ = "Integer32"
_StaLrme1PChassis_Object = MibTableColumn
staLrme1PChassis = _StaLrme1PChassis_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 2, 14, 3, 1, 1),
    _StaLrme1PChassis_Type()
)
staLrme1PChassis.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    staLrme1PChassis.setStatus("current")


class _StaLrme1PSlot_Type(Integer32):
    """Custom type staLrme1PSlot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 20),
    )


_StaLrme1PSlot_Type.__name__ = "Integer32"
_StaLrme1PSlot_Object = MibTableColumn
staLrme1PSlot = _StaLrme1PSlot_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 2, 14, 3, 1, 2),
    _StaLrme1PSlot_Type()
)
staLrme1PSlot.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    staLrme1PSlot.setStatus("current")


class _StaLrme1PPort_Type(Integer32):
    """Custom type staLrme1PPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_StaLrme1PPort_Type.__name__ = "Integer32"
_StaLrme1PPort_Object = MibTableColumn
staLrme1PPort = _StaLrme1PPort_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 2, 14, 3, 1, 3),
    _StaLrme1PPort_Type()
)
staLrme1PPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    staLrme1PPort.setStatus("current")


class _StaLrme1PStatus_Type(Integer32):
    """Custom type staLrme1PStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("ok", 1),
          ("cut", 2),
          ("disable", 3))
    )


_StaLrme1PStatus_Type.__name__ = "Integer32"
_StaLrme1PStatus_Object = MibTableColumn
staLrme1PStatus = _StaLrme1PStatus_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 2, 14, 3, 1, 4),
    _StaLrme1PStatus_Type()
)
staLrme1PStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staLrme1PStatus.setStatus("current")
_StaLrme1PFrame_Type = OnValue
_StaLrme1PFrame_Object = MibTableColumn
staLrme1PFrame = _StaLrme1PFrame_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 2, 14, 3, 1, 5),
    _StaLrme1PFrame_Type()
)
staLrme1PFrame.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staLrme1PFrame.setStatus("current")
_StaLrme1PLos_Type = OkValue
_StaLrme1PLos_Object = MibTableColumn
staLrme1PLos = _StaLrme1PLos_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 2, 14, 3, 1, 6),
    _StaLrme1PLos_Type()
)
staLrme1PLos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staLrme1PLos.setStatus("current")
_StaLrme1PAis_Type = OkValue
_StaLrme1PAis_Object = MibTableColumn
staLrme1PAis = _StaLrme1PAis_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 2, 14, 3, 1, 7),
    _StaLrme1PAis_Type()
)
staLrme1PAis.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staLrme1PAis.setStatus("current")
_StaLrme1PLof_Type = OkValue
_StaLrme1PLof_Object = MibTableColumn
staLrme1PLof = _StaLrme1PLof_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 2, 14, 3, 1, 8),
    _StaLrme1PLof_Type()
)
staLrme1PLof.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staLrme1PLof.setStatus("current")
_StaLrme1PBpv_Type = OkValue
_StaLrme1PBpv_Object = MibTableColumn
staLrme1PBpv = _StaLrme1PBpv_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 2, 14, 3, 1, 9),
    _StaLrme1PBpv_Type()
)
staLrme1PBpv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staLrme1PBpv.setStatus("current")
_StaLrme1PSlip_Type = OkValue
_StaLrme1PSlip_Object = MibTableColumn
staLrme1PSlip = _StaLrme1PSlip_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 2, 14, 3, 1, 10),
    _StaLrme1PSlip_Type()
)
staLrme1PSlip.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staLrme1PSlip.setStatus("current")
_StaLrme1PSlips_Type = Counter32
_StaLrme1PSlips_Object = MibTableColumn
staLrme1PSlips = _StaLrme1PSlips_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 2, 14, 3, 1, 11),
    _StaLrme1PSlips_Type()
)
staLrme1PSlips.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staLrme1PSlips.setStatus("current")
_StaLrme1PLosSide2_Type = OkValue
_StaLrme1PLosSide2_Object = MibTableColumn
staLrme1PLosSide2 = _StaLrme1PLosSide2_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 2, 14, 3, 1, 12),
    _StaLrme1PLosSide2_Type()
)
staLrme1PLosSide2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staLrme1PLosSide2.setStatus("current")


class _StaLrme1PBpv60SRate_Type(DisplayString):
    """Custom type staLrme1PBpv60SRate based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_StaLrme1PBpv60SRate_Type.__name__ = "DisplayString"
_StaLrme1PBpv60SRate_Object = MibTableColumn
staLrme1PBpv60SRate = _StaLrme1PBpv60SRate_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 2, 14, 3, 1, 13),
    _StaLrme1PBpv60SRate_Type()
)
staLrme1PBpv60SRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staLrme1PBpv60SRate.setStatus("current")


class _StaLrme1PBpv24HRate_Type(DisplayString):
    """Custom type staLrme1PBpv24HRate based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_StaLrme1PBpv24HRate_Type.__name__ = "DisplayString"
_StaLrme1PBpv24HRate_Object = MibTableColumn
staLrme1PBpv24HRate = _StaLrme1PBpv24HRate_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 2, 14, 3, 1, 14),
    _StaLrme1PBpv24HRate_Type()
)
staLrme1PBpv24HRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staLrme1PBpv24HRate.setStatus("current")
_StaLrme1PBpvErrSecs_Type = Counter32
_StaLrme1PBpvErrSecs_Object = MibTableColumn
staLrme1PBpvErrSecs = _StaLrme1PBpvErrSecs_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 2, 14, 3, 1, 15),
    _StaLrme1PBpvErrSecs_Type()
)
staLrme1PBpvErrSecs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staLrme1PBpvErrSecs.setStatus("current")
_StaLrme1PBpvSevErrSecs_Type = Counter32
_StaLrme1PBpvSevErrSecs_Object = MibTableColumn
staLrme1PBpvSevErrSecs = _StaLrme1PBpvSevErrSecs_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 2, 14, 3, 1, 16),
    _StaLrme1PBpvSevErrSecs_Type()
)
staLrme1PBpvSevErrSecs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staLrme1PBpvSevErrSecs.setStatus("current")


class _StaLrme1PBpvSevErrRatio_Type(DisplayString):
    """Custom type staLrme1PBpvSevErrRatio based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_StaLrme1PBpvSevErrRatio_Type.__name__ = "DisplayString"
_StaLrme1PBpvSevErrRatio_Object = MibTableColumn
staLrme1PBpvSevErrRatio = _StaLrme1PBpvSevErrRatio_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 2, 14, 3, 1, 17),
    _StaLrme1PBpvSevErrRatio_Type()
)
staLrme1PBpvSevErrRatio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staLrme1PBpvSevErrRatio.setStatus("current")
_StatusPtNtp_ObjectIdentity = ObjectIdentity
statusPtNtp = _StatusPtNtp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 2, 15)
)
_StaPtNtpTable_Object = MibTable
staPtNtpTable = _StaPtNtpTable_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 2, 15, 1)
)
if mibBuilder.loadTexts:
    staPtNtpTable.setStatus("current")
_StaPtNtpEntry_Object = MibTableRow
staPtNtpEntry = _StaPtNtpEntry_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 2, 15, 1, 1)
)
staPtNtpEntry.setIndexNames(
    (0, "SSU2000-MIB", "staPtNtpChassis"),
    (0, "SSU2000-MIB", "staPtNtpSlot"),
)
if mibBuilder.loadTexts:
    staPtNtpEntry.setStatus("current")


class _StaPtNtpChassis_Type(Integer32):
    """Custom type staPtNtpChassis based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_StaPtNtpChassis_Type.__name__ = "Integer32"
_StaPtNtpChassis_Object = MibTableColumn
staPtNtpChassis = _StaPtNtpChassis_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 2, 15, 1, 1, 1),
    _StaPtNtpChassis_Type()
)
staPtNtpChassis.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    staPtNtpChassis.setStatus("current")


class _StaPtNtpSlot_Type(Integer32):
    """Custom type staPtNtpSlot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 20),
    )


_StaPtNtpSlot_Type.__name__ = "Integer32"
_StaPtNtpSlot_Object = MibTableColumn
staPtNtpSlot = _StaPtNtpSlot_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 2, 15, 1, 1, 2),
    _StaPtNtpSlot_Type()
)
staPtNtpSlot.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    staPtNtpSlot.setStatus("current")


class _StaPtNtpStatus_Type(Integer32):
    """Custom type staPtNtpStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("ok", 1),
          ("disable", 3),
          ("fault", 4),
          ("reject", 5))
    )


_StaPtNtpStatus_Type.__name__ = "Integer32"
_StaPtNtpStatus_Object = MibTableColumn
staPtNtpStatus = _StaPtNtpStatus_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 2, 15, 1, 1, 3),
    _StaPtNtpStatus_Type()
)
staPtNtpStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staPtNtpStatus.setStatus("current")


class _StaPtNtpClkSel_Type(Integer32):
    """Custom type staPtNtpClkSel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("clka", 1),
          ("clkb", 2),
          ("clkc", 3),
          ("clkd", 4),
          ("none", 5))
    )


_StaPtNtpClkSel_Type.__name__ = "Integer32"
_StaPtNtpClkSel_Object = MibTableColumn
staPtNtpClkSel = _StaPtNtpClkSel_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 2, 15, 1, 1, 4),
    _StaPtNtpClkSel_Type()
)
staPtNtpClkSel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staPtNtpClkSel.setStatus("current")
_StaPtNtpClka_Type = ActiveValue
_StaPtNtpClka_Object = MibTableColumn
staPtNtpClka = _StaPtNtpClka_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 2, 15, 1, 1, 5),
    _StaPtNtpClka_Type()
)
staPtNtpClka.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staPtNtpClka.setStatus("current")
_StaPtNtpClkb_Type = ActiveValue
_StaPtNtpClkb_Object = MibTableColumn
staPtNtpClkb = _StaPtNtpClkb_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 2, 15, 1, 1, 6),
    _StaPtNtpClkb_Type()
)
staPtNtpClkb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staPtNtpClkb.setStatus("current")
_StaPtNtpClkc_Type = ActiveValue
_StaPtNtpClkc_Object = MibTableColumn
staPtNtpClkc = _StaPtNtpClkc_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 2, 15, 1, 1, 7),
    _StaPtNtpClkc_Type()
)
staPtNtpClkc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staPtNtpClkc.setStatus("current")
_StaPtNtpClkd_Type = ActiveValue
_StaPtNtpClkd_Object = MibTableColumn
staPtNtpClkd = _StaPtNtpClkd_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 2, 15, 1, 1, 8),
    _StaPtNtpClkd_Type()
)
staPtNtpClkd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staPtNtpClkd.setStatus("current")


class _StaPtNtpRednt_Type(Integer32):
    """Custom type staPtNtpRednt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 20),
    )


_StaPtNtpRednt_Type.__name__ = "Integer32"
_StaPtNtpRednt_Object = MibTableColumn
staPtNtpRednt = _StaPtNtpRednt_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 2, 15, 1, 1, 9),
    _StaPtNtpRednt_Type()
)
staPtNtpRednt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staPtNtpRednt.setStatus("current")


class _StaPtNtpModState_Type(Integer32):
    """Custom type staPtNtpModState based on Integer32"""
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
        *(("active", 1),
          ("stdby", 2),
          ("fault", 3),
          ("stdalone", 4))
    )


_StaPtNtpModState_Type.__name__ = "Integer32"
_StaPtNtpModState_Object = MibTableColumn
staPtNtpModState = _StaPtNtpModState_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 2, 15, 1, 1, 10),
    _StaPtNtpModState_Type()
)
staPtNtpModState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staPtNtpModState.setStatus("current")


class _StaPtNtpPAState_Type(Integer32):
    """Custom type staPtNtpPAState based on Integer32"""
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
        *(("active", 1),
          ("stdby", 2),
          ("fault", 3),
          ("stdalone", 4))
    )


_StaPtNtpPAState_Type.__name__ = "Integer32"
_StaPtNtpPAState_Object = MibTableColumn
staPtNtpPAState = _StaPtNtpPAState_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 2, 15, 1, 1, 11),
    _StaPtNtpPAState_Type()
)
staPtNtpPAState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staPtNtpPAState.setStatus("current")


class _StaPtNtpPBState_Type(Integer32):
    """Custom type staPtNtpPBState based on Integer32"""
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
        *(("active", 1),
          ("stdby", 2),
          ("fault", 3),
          ("stdalone", 4))
    )


_StaPtNtpPBState_Type.__name__ = "Integer32"
_StaPtNtpPBState_Object = MibTableColumn
staPtNtpPBState = _StaPtNtpPBState_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 2, 15, 1, 1, 12),
    _StaPtNtpPBState_Type()
)
staPtNtpPBState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staPtNtpPBState.setStatus("current")
_StaPtNtpTod_Type = OnValue
_StaPtNtpTod_Object = MibTableColumn
staPtNtpTod = _StaPtNtpTod_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 2, 15, 1, 1, 13),
    _StaPtNtpTod_Type()
)
staPtNtpTod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staPtNtpTod.setStatus("current")


class _StaPtNtpCommit_Type(Integer32):
    """Custom type staPtNtpCommit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("done", 1),
          ("prog", 2))
    )


_StaPtNtpCommit_Type.__name__ = "Integer32"
_StaPtNtpCommit_Object = MibTableColumn
staPtNtpCommit = _StaPtNtpCommit_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 2, 15, 1, 1, 14),
    _StaPtNtpCommit_Type()
)
staPtNtpCommit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staPtNtpCommit.setStatus("current")
_StatusPtPtp_ObjectIdentity = ObjectIdentity
statusPtPtp = _StatusPtPtp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 2, 16)
)
_StaPtPtpTable_Object = MibTable
staPtPtpTable = _StaPtPtpTable_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 2, 16, 1)
)
if mibBuilder.loadTexts:
    staPtPtpTable.setStatus("current")
_StaPtPtpEntry_Object = MibTableRow
staPtPtpEntry = _StaPtPtpEntry_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 2, 16, 1, 1)
)
staPtPtpEntry.setIndexNames(
    (0, "SSU2000-MIB", "staPtPtpChassis"),
    (0, "SSU2000-MIB", "staPtPtpSlot"),
)
if mibBuilder.loadTexts:
    staPtPtpEntry.setStatus("current")


class _StaPtPtpChassis_Type(Integer32):
    """Custom type staPtPtpChassis based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_StaPtPtpChassis_Type.__name__ = "Integer32"
_StaPtPtpChassis_Object = MibTableColumn
staPtPtpChassis = _StaPtPtpChassis_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 2, 16, 1, 1, 1),
    _StaPtPtpChassis_Type()
)
staPtPtpChassis.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    staPtPtpChassis.setStatus("current")


class _StaPtPtpSlot_Type(Integer32):
    """Custom type staPtPtpSlot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 20),
    )


_StaPtPtpSlot_Type.__name__ = "Integer32"
_StaPtPtpSlot_Object = MibTableColumn
staPtPtpSlot = _StaPtPtpSlot_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 2, 16, 1, 1, 2),
    _StaPtPtpSlot_Type()
)
staPtPtpSlot.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    staPtPtpSlot.setStatus("current")


class _StaPtPtpStatus_Type(Integer32):
    """Custom type staPtPtpStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("ok", 1),
          ("disable", 3),
          ("fault", 4),
          ("reject", 5))
    )


_StaPtPtpStatus_Type.__name__ = "Integer32"
_StaPtPtpStatus_Object = MibTableColumn
staPtPtpStatus = _StaPtPtpStatus_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 2, 16, 1, 1, 3),
    _StaPtPtpStatus_Type()
)
staPtPtpStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staPtPtpStatus.setStatus("current")


class _StaPtPtpClkSel_Type(Integer32):
    """Custom type staPtPtpClkSel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("clka", 1),
          ("clkb", 2),
          ("clkc", 3),
          ("clkd", 4),
          ("none", 5))
    )


_StaPtPtpClkSel_Type.__name__ = "Integer32"
_StaPtPtpClkSel_Object = MibTableColumn
staPtPtpClkSel = _StaPtPtpClkSel_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 2, 16, 1, 1, 4),
    _StaPtPtpClkSel_Type()
)
staPtPtpClkSel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staPtPtpClkSel.setStatus("current")
_StaPtPtpClka_Type = ActiveValue
_StaPtPtpClka_Object = MibTableColumn
staPtPtpClka = _StaPtPtpClka_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 2, 16, 1, 1, 5),
    _StaPtPtpClka_Type()
)
staPtPtpClka.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staPtPtpClka.setStatus("current")
_StaPtPtpClkb_Type = ActiveValue
_StaPtPtpClkb_Object = MibTableColumn
staPtPtpClkb = _StaPtPtpClkb_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 2, 16, 1, 1, 6),
    _StaPtPtpClkb_Type()
)
staPtPtpClkb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staPtPtpClkb.setStatus("current")
_StaPtPtpClkc_Type = ActiveValue
_StaPtPtpClkc_Object = MibTableColumn
staPtPtpClkc = _StaPtPtpClkc_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 2, 16, 1, 1, 7),
    _StaPtPtpClkc_Type()
)
staPtPtpClkc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staPtPtpClkc.setStatus("current")
_StaPtPtpClkd_Type = ActiveValue
_StaPtPtpClkd_Object = MibTableColumn
staPtPtpClkd = _StaPtPtpClkd_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 2, 16, 1, 1, 8),
    _StaPtPtpClkd_Type()
)
staPtPtpClkd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staPtPtpClkd.setStatus("current")


class _StaPtPtpRednt_Type(Integer32):
    """Custom type staPtPtpRednt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 20),
    )


_StaPtPtpRednt_Type.__name__ = "Integer32"
_StaPtPtpRednt_Object = MibTableColumn
staPtPtpRednt = _StaPtPtpRednt_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 2, 16, 1, 1, 9),
    _StaPtPtpRednt_Type()
)
staPtPtpRednt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staPtPtpRednt.setStatus("current")


class _StaPtPtpModState_Type(Integer32):
    """Custom type staPtPtpModState based on Integer32"""
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
        *(("active", 1),
          ("stdby", 2),
          ("fault", 3),
          ("stdalone", 4))
    )


_StaPtPtpModState_Type.__name__ = "Integer32"
_StaPtPtpModState_Object = MibTableColumn
staPtPtpModState = _StaPtPtpModState_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 2, 16, 1, 1, 10),
    _StaPtPtpModState_Type()
)
staPtPtpModState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staPtPtpModState.setStatus("current")


class _StaPtPtpPAState_Type(Integer32):
    """Custom type staPtPtpPAState based on Integer32"""
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
        *(("active", 1),
          ("stdby", 2),
          ("fault", 3),
          ("stdalone", 4))
    )


_StaPtPtpPAState_Type.__name__ = "Integer32"
_StaPtPtpPAState_Object = MibTableColumn
staPtPtpPAState = _StaPtPtpPAState_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 2, 16, 1, 1, 11),
    _StaPtPtpPAState_Type()
)
staPtPtpPAState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staPtPtpPAState.setStatus("current")
_StaPtPtpTod_Type = OnValue
_StaPtPtpTod_Object = MibTableColumn
staPtPtpTod = _StaPtPtpTod_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 2, 16, 1, 1, 12),
    _StaPtPtpTod_Type()
)
staPtPtpTod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staPtPtpTod.setStatus("current")


class _StaPtPtpCommit_Type(Integer32):
    """Custom type staPtPtpCommit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("done", 1),
          ("prog", 2))
    )


_StaPtPtpCommit_Type.__name__ = "Integer32"
_StaPtPtpCommit_Object = MibTableColumn
staPtPtpCommit = _StaPtPtpCommit_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 2, 16, 1, 1, 13),
    _StaPtPtpCommit_Type()
)
staPtPtpCommit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staPtPtpCommit.setStatus("current")
_PtpDfltDataSetTable_Object = MibTable
ptpDfltDataSetTable = _PtpDfltDataSetTable_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 2, 16, 2)
)
if mibBuilder.loadTexts:
    ptpDfltDataSetTable.setStatus("current")
_PtpDfltDataSetEntry_Object = MibTableRow
ptpDfltDataSetEntry = _PtpDfltDataSetEntry_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 2, 16, 2, 1)
)
ptpDfltDataSetEntry.setIndexNames(
    (0, "SSU2000-MIB", "ptpDfltDataSetChassis"),
    (0, "SSU2000-MIB", "ptpDfltDataSetSlot"),
)
if mibBuilder.loadTexts:
    ptpDfltDataSetEntry.setStatus("current")


class _PtpDfltDataSetChassis_Type(Integer32):
    """Custom type ptpDfltDataSetChassis based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_PtpDfltDataSetChassis_Type.__name__ = "Integer32"
_PtpDfltDataSetChassis_Object = MibTableColumn
ptpDfltDataSetChassis = _PtpDfltDataSetChassis_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 2, 16, 2, 1, 1),
    _PtpDfltDataSetChassis_Type()
)
ptpDfltDataSetChassis.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ptpDfltDataSetChassis.setStatus("current")


class _PtpDfltDataSetSlot_Type(Integer32):
    """Custom type ptpDfltDataSetSlot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 20),
    )


_PtpDfltDataSetSlot_Type.__name__ = "Integer32"
_PtpDfltDataSetSlot_Object = MibTableColumn
ptpDfltDataSetSlot = _PtpDfltDataSetSlot_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 2, 16, 2, 1, 2),
    _PtpDfltDataSetSlot_Type()
)
ptpDfltDataSetSlot.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ptpDfltDataSetSlot.setStatus("current")


class _PtpDfltDataSetClockId_Type(OctetString):
    """Custom type ptpDfltDataSetClockId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )
    fixed_length = 8


_PtpDfltDataSetClockId_Type.__name__ = "OctetString"
_PtpDfltDataSetClockId_Object = MibTableColumn
ptpDfltDataSetClockId = _PtpDfltDataSetClockId_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 2, 16, 2, 1, 3),
    _PtpDfltDataSetClockId_Type()
)
ptpDfltDataSetClockId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ptpDfltDataSetClockId.setStatus("current")


class _PtpDfltDataSetClockClass_Type(Integer32):
    """Custom type ptpDfltDataSetClockClass based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_PtpDfltDataSetClockClass_Type.__name__ = "Integer32"
_PtpDfltDataSetClockClass_Object = MibTableColumn
ptpDfltDataSetClockClass = _PtpDfltDataSetClockClass_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 2, 16, 2, 1, 4),
    _PtpDfltDataSetClockClass_Type()
)
ptpDfltDataSetClockClass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ptpDfltDataSetClockClass.setStatus("current")


class _PtpDfltDataSetClockAccuracy_Type(Integer32):
    """Custom type ptpDfltDataSetClockAccuracy based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(32,
              33,
              34,
              35,
              36,
              37,
              38,
              39,
              40,
              41,
              42,
              43,
              44,
              45,
              46,
              47,
              48,
              49,
              254)
        )
    )
    namedValues = NamedValues(
        *(("within25ns", 32),
          ("within100ns", 33),
          ("within250ns", 34),
          ("within1000ns", 35),
          ("within2p5us", 36),
          ("within10us", 37),
          ("within25us", 38),
          ("within100us", 39),
          ("within250us", 40),
          ("within1ms", 41),
          ("within2p5ms", 42),
          ("within10ms", 43),
          ("within25ms", 44),
          ("within100ms", 45),
          ("within250ms", 46),
          ("within1sec", 47),
          ("within10sec", 48),
          ("beyond10sec", 49),
          ("unknown", 254))
    )


_PtpDfltDataSetClockAccuracy_Type.__name__ = "Integer32"
_PtpDfltDataSetClockAccuracy_Object = MibTableColumn
ptpDfltDataSetClockAccuracy = _PtpDfltDataSetClockAccuracy_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 2, 16, 2, 1, 5),
    _PtpDfltDataSetClockAccuracy_Type()
)
ptpDfltDataSetClockAccuracy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ptpDfltDataSetClockAccuracy.setStatus("current")
_PtpDfltDataSetTimeTraceable_Type = TrueValue
_PtpDfltDataSetTimeTraceable_Object = MibTableColumn
ptpDfltDataSetTimeTraceable = _PtpDfltDataSetTimeTraceable_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 2, 16, 2, 1, 6),
    _PtpDfltDataSetTimeTraceable_Type()
)
ptpDfltDataSetTimeTraceable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ptpDfltDataSetTimeTraceable.setStatus("current")
_PtpDfltDataSetFreqTraceable_Type = TrueValue
_PtpDfltDataSetFreqTraceable_Object = MibTableColumn
ptpDfltDataSetFreqTraceable = _PtpDfltDataSetFreqTraceable_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 2, 16, 2, 1, 7),
    _PtpDfltDataSetFreqTraceable_Type()
)
ptpDfltDataSetFreqTraceable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ptpDfltDataSetFreqTraceable.setStatus("current")


class _PtpDfltDataSetDomainNumber_Type(Integer32):
    """Custom type ptpDfltDataSetDomainNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_PtpDfltDataSetDomainNumber_Type.__name__ = "Integer32"
_PtpDfltDataSetDomainNumber_Object = MibTableColumn
ptpDfltDataSetDomainNumber = _PtpDfltDataSetDomainNumber_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 2, 16, 2, 1, 8),
    _PtpDfltDataSetDomainNumber_Type()
)
ptpDfltDataSetDomainNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ptpDfltDataSetDomainNumber.setStatus("current")
_PtpClockDescrTable_Object = MibTable
ptpClockDescrTable = _PtpClockDescrTable_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 2, 16, 3)
)
if mibBuilder.loadTexts:
    ptpClockDescrTable.setStatus("current")
_PtpClockDescrEntry_Object = MibTableRow
ptpClockDescrEntry = _PtpClockDescrEntry_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 2, 16, 3, 1)
)
ptpClockDescrEntry.setIndexNames(
    (0, "SSU2000-MIB", "ptpClockDescrChassis"),
    (0, "SSU2000-MIB", "ptpClockDescrSlot"),
)
if mibBuilder.loadTexts:
    ptpClockDescrEntry.setStatus("current")


class _PtpClockDescrChassis_Type(Integer32):
    """Custom type ptpClockDescrChassis based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_PtpClockDescrChassis_Type.__name__ = "Integer32"
_PtpClockDescrChassis_Object = MibTableColumn
ptpClockDescrChassis = _PtpClockDescrChassis_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 2, 16, 3, 1, 1),
    _PtpClockDescrChassis_Type()
)
ptpClockDescrChassis.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ptpClockDescrChassis.setStatus("current")


class _PtpClockDescrSlot_Type(Integer32):
    """Custom type ptpClockDescrSlot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 20),
    )


_PtpClockDescrSlot_Type.__name__ = "Integer32"
_PtpClockDescrSlot_Object = MibTableColumn
ptpClockDescrSlot = _PtpClockDescrSlot_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 2, 16, 3, 1, 2),
    _PtpClockDescrSlot_Type()
)
ptpClockDescrSlot.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ptpClockDescrSlot.setStatus("current")


class _PtpClockDescrClockType_Type(Integer32):
    """Custom type ptpClockDescrClockType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            32768
        )
    )
    namedValues = NamedValues(
        ("ordinary", 32768)
    )


_PtpClockDescrClockType_Type.__name__ = "Integer32"
_PtpClockDescrClockType_Object = MibTableColumn
ptpClockDescrClockType = _PtpClockDescrClockType_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 2, 16, 3, 1, 3),
    _PtpClockDescrClockType_Type()
)
ptpClockDescrClockType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ptpClockDescrClockType.setStatus("current")
_PtpClockDescrProtocolAddress_Type = IpAddress
_PtpClockDescrProtocolAddress_Object = MibTableColumn
ptpClockDescrProtocolAddress = _PtpClockDescrProtocolAddress_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 2, 16, 3, 1, 4),
    _PtpClockDescrProtocolAddress_Type()
)
ptpClockDescrProtocolAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ptpClockDescrProtocolAddress.setStatus("current")


class _PtpClockDescrManufacturerId_Type(OctetString):
    """Custom type ptpClockDescrManufacturerId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 3),
    )
    fixed_length = 3


_PtpClockDescrManufacturerId_Type.__name__ = "OctetString"
_PtpClockDescrManufacturerId_Object = MibTableColumn
ptpClockDescrManufacturerId = _PtpClockDescrManufacturerId_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 2, 16, 3, 1, 5),
    _PtpClockDescrManufacturerId_Type()
)
ptpClockDescrManufacturerId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ptpClockDescrManufacturerId.setStatus("current")


class _PtpClockDescrProfileId_Type(OctetString):
    """Custom type ptpClockDescrProfileId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )
    fixed_length = 6


_PtpClockDescrProfileId_Type.__name__ = "OctetString"
_PtpClockDescrProfileId_Object = MibTableColumn
ptpClockDescrProfileId = _PtpClockDescrProfileId_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 2, 16, 3, 1, 6),
    _PtpClockDescrProfileId_Type()
)
ptpClockDescrProfileId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ptpClockDescrProfileId.setStatus("current")
_PtpTimeMessageTable_Object = MibTable
ptpTimeMessageTable = _PtpTimeMessageTable_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 2, 16, 4)
)
if mibBuilder.loadTexts:
    ptpTimeMessageTable.setStatus("current")
_PtpTimeMessageEntry_Object = MibTableRow
ptpTimeMessageEntry = _PtpTimeMessageEntry_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 2, 16, 4, 1)
)
ptpTimeMessageEntry.setIndexNames(
    (0, "SSU2000-MIB", "ptpTimeMessageChassis"),
    (0, "SSU2000-MIB", "ptpTimeMessageSlot"),
)
if mibBuilder.loadTexts:
    ptpTimeMessageEntry.setStatus("current")


class _PtpTimeMessageChassis_Type(Integer32):
    """Custom type ptpTimeMessageChassis based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_PtpTimeMessageChassis_Type.__name__ = "Integer32"
_PtpTimeMessageChassis_Object = MibTableColumn
ptpTimeMessageChassis = _PtpTimeMessageChassis_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 2, 16, 4, 1, 1),
    _PtpTimeMessageChassis_Type()
)
ptpTimeMessageChassis.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ptpTimeMessageChassis.setStatus("current")


class _PtpTimeMessageSlot_Type(Integer32):
    """Custom type ptpTimeMessageSlot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 20),
    )


_PtpTimeMessageSlot_Type.__name__ = "Integer32"
_PtpTimeMessageSlot_Object = MibTableColumn
ptpTimeMessageSlot = _PtpTimeMessageSlot_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 2, 16, 4, 1, 2),
    _PtpTimeMessageSlot_Type()
)
ptpTimeMessageSlot.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ptpTimeMessageSlot.setStatus("current")


class _PtpTimeMessageCurrentTimeSec_Type(OctetString):
    """Custom type ptpTimeMessageCurrentTimeSec based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )
    fixed_length = 6


_PtpTimeMessageCurrentTimeSec_Type.__name__ = "OctetString"
_PtpTimeMessageCurrentTimeSec_Object = MibTableColumn
ptpTimeMessageCurrentTimeSec = _PtpTimeMessageCurrentTimeSec_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 2, 16, 4, 1, 3),
    _PtpTimeMessageCurrentTimeSec_Type()
)
ptpTimeMessageCurrentTimeSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ptpTimeMessageCurrentTimeSec.setStatus("current")
_PtpTimeMessageCurrentTimeNSec_Type = Counter32
_PtpTimeMessageCurrentTimeNSec_Object = MibTableColumn
ptpTimeMessageCurrentTimeNSec = _PtpTimeMessageCurrentTimeNSec_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 2, 16, 4, 1, 4),
    _PtpTimeMessageCurrentTimeNSec_Type()
)
ptpTimeMessageCurrentTimeNSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ptpTimeMessageCurrentTimeNSec.setStatus("current")
_PtpPortDataSetTable_Object = MibTable
ptpPortDataSetTable = _PtpPortDataSetTable_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 2, 16, 5)
)
if mibBuilder.loadTexts:
    ptpPortDataSetTable.setStatus("current")
_PtpPortDataSetEntry_Object = MibTableRow
ptpPortDataSetEntry = _PtpPortDataSetEntry_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 2, 16, 5, 1)
)
ptpPortDataSetEntry.setIndexNames(
    (0, "SSU2000-MIB", "ptpPortDataSetChassis"),
    (0, "SSU2000-MIB", "ptpPortDataSetSlot"),
)
if mibBuilder.loadTexts:
    ptpPortDataSetEntry.setStatus("current")


class _PtpPortDataSetChassis_Type(Integer32):
    """Custom type ptpPortDataSetChassis based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_PtpPortDataSetChassis_Type.__name__ = "Integer32"
_PtpPortDataSetChassis_Object = MibTableColumn
ptpPortDataSetChassis = _PtpPortDataSetChassis_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 2, 16, 5, 1, 1),
    _PtpPortDataSetChassis_Type()
)
ptpPortDataSetChassis.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ptpPortDataSetChassis.setStatus("current")


class _PtpPortDataSetSlot_Type(Integer32):
    """Custom type ptpPortDataSetSlot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 20),
    )


_PtpPortDataSetSlot_Type.__name__ = "Integer32"
_PtpPortDataSetSlot_Object = MibTableColumn
ptpPortDataSetSlot = _PtpPortDataSetSlot_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 2, 16, 5, 1, 2),
    _PtpPortDataSetSlot_Type()
)
ptpPortDataSetSlot.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ptpPortDataSetSlot.setStatus("current")


class _PtpPortDataSetClockId_Type(OctetString):
    """Custom type ptpPortDataSetClockId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )
    fixed_length = 8


_PtpPortDataSetClockId_Type.__name__ = "OctetString"
_PtpPortDataSetClockId_Object = MibTableColumn
ptpPortDataSetClockId = _PtpPortDataSetClockId_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 2, 16, 5, 1, 3),
    _PtpPortDataSetClockId_Type()
)
ptpPortDataSetClockId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ptpPortDataSetClockId.setStatus("current")


class _PtpPortDataSetPortNumber_Type(Integer32):
    """Custom type ptpPortDataSetPortNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_PtpPortDataSetPortNumber_Type.__name__ = "Integer32"
_PtpPortDataSetPortNumber_Object = MibTableColumn
ptpPortDataSetPortNumber = _PtpPortDataSetPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 2, 16, 5, 1, 4),
    _PtpPortDataSetPortNumber_Type()
)
ptpPortDataSetPortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ptpPortDataSetPortNumber.setStatus("current")


class _PtpPortDataSetPortState_Type(Integer32):
    """Custom type ptpPortDataSetPortState based on Integer32"""
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
              7,
              8,
              9)
        )
    )
    namedValues = NamedValues(
        *(("notdefined", 0),
          ("initializing", 1),
          ("faulty", 2),
          ("disabled", 3),
          ("listening", 4),
          ("premaster", 5),
          ("master", 6),
          ("passive", 7),
          ("uncalibrated", 8),
          ("slave", 9))
    )


_PtpPortDataSetPortState_Type.__name__ = "Integer32"
_PtpPortDataSetPortState_Object = MibTableColumn
ptpPortDataSetPortState = _PtpPortDataSetPortState_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 2, 16, 5, 1, 5),
    _PtpPortDataSetPortState_Type()
)
ptpPortDataSetPortState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ptpPortDataSetPortState.setStatus("current")
_StatusSynce_ObjectIdentity = ObjectIdentity
statusSynce = _StatusSynce_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 2, 17)
)
_StaSynceTable_Object = MibTable
staSynceTable = _StaSynceTable_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 2, 17, 1)
)
if mibBuilder.loadTexts:
    staSynceTable.setStatus("current")
_StaSynceEntry_Object = MibTableRow
staSynceEntry = _StaSynceEntry_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 2, 17, 1, 1)
)
staSynceEntry.setIndexNames(
    (0, "SSU2000-MIB", "staSynceChassis"),
    (0, "SSU2000-MIB", "staSynceSlot"),
)
if mibBuilder.loadTexts:
    staSynceEntry.setStatus("current")


class _StaSynceChassis_Type(Integer32):
    """Custom type staSynceChassis based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_StaSynceChassis_Type.__name__ = "Integer32"
_StaSynceChassis_Object = MibTableColumn
staSynceChassis = _StaSynceChassis_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 2, 17, 1, 1, 1),
    _StaSynceChassis_Type()
)
staSynceChassis.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    staSynceChassis.setStatus("current")


class _StaSynceSlot_Type(Integer32):
    """Custom type staSynceSlot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 20),
    )


_StaSynceSlot_Type.__name__ = "Integer32"
_StaSynceSlot_Object = MibTableColumn
staSynceSlot = _StaSynceSlot_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 2, 17, 1, 1, 2),
    _StaSynceSlot_Type()
)
staSynceSlot.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    staSynceSlot.setStatus("current")


class _StaSyncePortDirection_Type(Integer32):
    """Custom type staSyncePortDirection based on Integer32"""
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


_StaSyncePortDirection_Type.__name__ = "Integer32"
_StaSyncePortDirection_Object = MibTableColumn
staSyncePortDirection = _StaSyncePortDirection_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 2, 17, 1, 1, 3),
    _StaSyncePortDirection_Type()
)
staSyncePortDirection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staSyncePortDirection.setStatus("current")


class _StaSynceEthernetMode_Type(Integer32):
    """Custom type staSynceEthernetMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("synchronous", 1),
          ("asynchronous", 2))
    )


_StaSynceEthernetMode_Type.__name__ = "Integer32"
_StaSynceEthernetMode_Object = MibTableColumn
staSynceEthernetMode = _StaSynceEthernetMode_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 2, 17, 1, 1, 4),
    _StaSynceEthernetMode_Type()
)
staSynceEthernetMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staSynceEthernetMode.setStatus("current")


class _StaSynceRxSsm_Type(Integer32):
    """Custom type staSynceRxSsm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
        ValueRangeConstraint(255, 255),
    )


_StaSynceRxSsm_Type.__name__ = "Integer32"
_StaSynceRxSsm_Object = MibTableColumn
staSynceRxSsm = _StaSynceRxSsm_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 2, 17, 1, 1, 5),
    _StaSynceRxSsm_Type()
)
staSynceRxSsm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staSynceRxSsm.setStatus("current")


class _StaSynceTxSsm_Type(Integer32):
    """Custom type staSynceTxSsm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
        ValueRangeConstraint(255, 255),
    )


_StaSynceTxSsm_Type.__name__ = "Integer32"
_StaSynceTxSsm_Object = MibTableColumn
staSynceTxSsm = _StaSynceTxSsm_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 2, 17, 1, 1, 6),
    _StaSynceTxSsm_Type()
)
staSynceTxSsm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staSynceTxSsm.setStatus("current")
_Msetup_ObjectIdentity = ObjectIdentity
msetup = _Msetup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 3)
)
_SetupCom_ObjectIdentity = ObjectIdentity
setupCom = _SetupCom_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 3, 1)
)


class _SetCmId_Type(DisplayString):
    """Custom type setCmId based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(7, 7),
    )
    fixed_length = 7


_SetCmId_Type.__name__ = "DisplayString"
_SetCmId_Object = MibScalar
setCmId = _SetCmId_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 3, 1, 1),
    _SetCmId_Type()
)
setCmId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    setCmId.setStatus("current")


class _SetCmInfo_Type(DisplayString):
    """Custom type setCmInfo based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SetCmInfo_Type.__name__ = "DisplayString"
_SetCmInfo_Object = MibScalar
setCmInfo = _SetCmInfo_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 3, 1, 2),
    _SetCmInfo_Type()
)
setCmInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    setCmInfo.setStatus("current")


class _SetCmVer_Type(DisplayString):
    """Custom type setCmVer based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 100),
    )


_SetCmVer_Type.__name__ = "DisplayString"
_SetCmVer_Object = MibScalar
setCmVer = _SetCmVer_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 3, 1, 3),
    _SetCmVer_Type()
)
setCmVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    setCmVer.setStatus("current")


class _SetCmName_Type(DisplayString):
    """Custom type setCmName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 20),
    )


_SetCmName_Type.__name__ = "DisplayString"
_SetCmName_Object = MibScalar
setCmName = _SetCmName_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 3, 1, 4),
    _SetCmName_Type()
)
setCmName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    setCmName.setStatus("current")
_SetupClk_ObjectIdentity = ObjectIdentity
setupClk = _SetupClk_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 3, 2)
)
_SetClkTable_Object = MibTable
setClkTable = _SetClkTable_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 3, 2, 1)
)
if mibBuilder.loadTexts:
    setClkTable.setStatus("current")
_SetCkEntry_Object = MibTableRow
setCkEntry = _SetCkEntry_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 3, 2, 1, 1)
)
setCkEntry.setIndexNames(
    (0, "SSU2000-MIB", "setCkChassis"),
    (0, "SSU2000-MIB", "setCkSlot"),
)
if mibBuilder.loadTexts:
    setCkEntry.setStatus("current")


class _SetCkChassis_Type(Integer32):
    """Custom type setCkChassis based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_SetCkChassis_Type.__name__ = "Integer32"
_SetCkChassis_Object = MibTableColumn
setCkChassis = _SetCkChassis_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 3, 2, 1, 1, 1),
    _SetCkChassis_Type()
)
setCkChassis.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    setCkChassis.setStatus("current")


class _SetCkSlot_Type(Integer32):
    """Custom type setCkSlot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 20),
    )


_SetCkSlot_Type.__name__ = "Integer32"
_SetCkSlot_Object = MibTableColumn
setCkSlot = _SetCkSlot_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 3, 2, 1, 1, 2),
    _SetCkSlot_Type()
)
setCkSlot.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    setCkSlot.setStatus("current")


class _SetCkWarmup_Type(Integer32):
    """Custom type setCkWarmup based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(900, 3600),
    )


_SetCkWarmup_Type.__name__ = "Integer32"
_SetCkWarmup_Object = MibTableColumn
setCkWarmup = _SetCkWarmup_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 3, 2, 1, 1, 3),
    _SetCkWarmup_Type()
)
setCkWarmup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    setCkWarmup.setStatus("current")


class _SetCkMinTau_Type(Integer32):
    """Custom type setCkMinTau based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(150, 10000),
    )


_SetCkMinTau_Type.__name__ = "Integer32"
_SetCkMinTau_Object = MibTableColumn
setCkMinTau = _SetCkMinTau_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 3, 2, 1, 1, 4),
    _SetCkMinTau_Type()
)
setCkMinTau.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    setCkMinTau.setStatus("current")


class _SetCkMaxTau_Type(Integer32):
    """Custom type setCkMaxTau based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(150, 10000),
    )


_SetCkMaxTau_Type.__name__ = "Integer32"
_SetCkMaxTau_Object = MibTableColumn
setCkMaxTau = _SetCkMaxTau_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 3, 2, 1, 1, 5),
    _SetCkMaxTau_Type()
)
setCkMaxTau.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    setCkMaxTau.setStatus("current")


class _SetCkPLLMode_Type(Integer32):
    """Custom type setCkPLLMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("acq", 2),
          ("lock", 3),
          ("hold", 4))
    )


_SetCkPLLMode_Type.__name__ = "Integer32"
_SetCkPLLMode_Object = MibTableColumn
setCkPLLMode = _SetCkPLLMode_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 3, 2, 1, 1, 6),
    _SetCkPLLMode_Type()
)
setCkPLLMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    setCkPLLMode.setStatus("current")


class _SetCkTodTimeout_Type(Integer32):
    """Custom type setCkTodTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(60, 10000),
    )


_SetCkTodTimeout_Type.__name__ = "Integer32"
_SetCkTodTimeout_Object = MibTableColumn
setCkTodTimeout = _SetCkTodTimeout_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 3, 2, 1, 1, 7),
    _SetCkTodTimeout_Type()
)
setCkTodTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    setCkTodTimeout.setStatus("current")


class _SetCkFreqTimeout_Type(Integer32):
    """Custom type setCkFreqTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(60, 10000),
    )


_SetCkFreqTimeout_Type.__name__ = "Integer32"
_SetCkFreqTimeout_Object = MibTableColumn
setCkFreqTimeout = _SetCkFreqTimeout_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 3, 2, 1, 1, 8),
    _SetCkFreqTimeout_Type()
)
setCkFreqTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    setCkFreqTimeout.setStatus("current")
_SetupGps_ObjectIdentity = ObjectIdentity
setupGps = _SetupGps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 3, 5)
)
_SetGpsTable_Object = MibTable
setGpsTable = _SetGpsTable_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 3, 5, 1)
)
if mibBuilder.loadTexts:
    setGpsTable.setStatus("current")
_SetGpsEntry_Object = MibTableRow
setGpsEntry = _SetGpsEntry_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 3, 5, 1, 1)
)
setGpsEntry.setIndexNames(
    (0, "SSU2000-MIB", "setGpsChassis"),
    (0, "SSU2000-MIB", "setGpsSlot"),
)
if mibBuilder.loadTexts:
    setGpsEntry.setStatus("current")


class _SetGpsChassis_Type(Integer32):
    """Custom type setGpsChassis based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
    )


_SetGpsChassis_Type.__name__ = "Integer32"
_SetGpsChassis_Object = MibTableColumn
setGpsChassis = _SetGpsChassis_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 3, 5, 1, 1, 1),
    _SetGpsChassis_Type()
)
setGpsChassis.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    setGpsChassis.setStatus("current")


class _SetGpsSlot_Type(Integer32):
    """Custom type setGpsSlot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 20),
    )


_SetGpsSlot_Type.__name__ = "Integer32"
_SetGpsSlot_Object = MibTableColumn
setGpsSlot = _SetGpsSlot_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 3, 5, 1, 1, 2),
    _SetGpsSlot_Type()
)
setGpsSlot.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    setGpsSlot.setStatus("current")


class _SetGpsEngine_Type(Integer32):
    """Custom type setGpsEngine based on Integer32"""
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
        *(("na", 1),
          ("unknown", 2),
          ("mot", 3),
          ("nvs", 4))
    )


_SetGpsEngine_Type.__name__ = "Integer32"
_SetGpsEngine_Object = MibTableColumn
setGpsEngine = _SetGpsEngine_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 3, 5, 1, 1, 3),
    _SetGpsEngine_Type()
)
setGpsEngine.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    setGpsEngine.setStatus("current")


class _SetGpsProvPql_Type(Integer32):
    """Custom type setGpsProvPql based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 9),
    )


_SetGpsProvPql_Type.__name__ = "Integer32"
_SetGpsProvPql_Object = MibTableColumn
setGpsProvPql = _SetGpsProvPql_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 3, 5, 1, 1, 4),
    _SetGpsProvPql_Type()
)
setGpsProvPql.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    setGpsProvPql.setStatus("current")


class _SetGpsPriority_Type(Integer32):
    """Custom type setGpsPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10),
    )


_SetGpsPriority_Type.__name__ = "Integer32"
_SetGpsPriority_Object = MibTableColumn
setGpsPriority = _SetGpsPriority_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 3, 5, 1, 1, 5),
    _SetGpsPriority_Type()
)
setGpsPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    setGpsPriority.setStatus("current")


class _SetGpsPdop_Type(Integer32):
    """Custom type setGpsPdop based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(3, 10),
    )


_SetGpsPdop_Type.__name__ = "Integer32"
_SetGpsPdop_Object = MibTableColumn
setGpsPdop = _SetGpsPdop_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 3, 5, 1, 1, 6),
    _SetGpsPdop_Type()
)
setGpsPdop.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    setGpsPdop.setStatus("current")


class _SetGpsPosel_Type(Integer32):
    """Custom type setGpsPosel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 90),
    )


_SetGpsPosel_Type.__name__ = "Integer32"
_SetGpsPosel_Object = MibTableColumn
setGpsPosel = _SetGpsPosel_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 3, 5, 1, 1, 7),
    _SetGpsPosel_Type()
)
setGpsPosel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    setGpsPosel.setStatus("current")


class _SetGpsTimel_Type(Integer32):
    """Custom type setGpsTimel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 90),
    )


_SetGpsTimel_Type.__name__ = "Integer32"
_SetGpsTimel_Object = MibTableColumn
setGpsTimel = _SetGpsTimel_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 3, 5, 1, 1, 8),
    _SetGpsTimel_Type()
)
setGpsTimel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    setGpsTimel.setStatus("current")


class _SetGpsAvg_Type(Integer32):
    """Custom type setGpsAvg based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(20, 3600),
    )


_SetGpsAvg_Type.__name__ = "Integer32"
_SetGpsAvg_Object = MibTableColumn
setGpsAvg = _SetGpsAvg_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 3, 5, 1, 1, 9),
    _SetGpsAvg_Type()
)
setGpsAvg.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    setGpsAvg.setStatus("current")
_SetGpsLat_Type = TLatAndLon
_SetGpsLat_Object = MibTableColumn
setGpsLat = _SetGpsLat_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 3, 5, 1, 1, 10),
    _SetGpsLat_Type()
)
setGpsLat.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    setGpsLat.setStatus("current")
_SetGpsLon_Type = TLatAndLon
_SetGpsLon_Object = MibTableColumn
setGpsLon = _SetGpsLon_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 3, 5, 1, 1, 11),
    _SetGpsLon_Type()
)
setGpsLon.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    setGpsLon.setStatus("current")
_SetGpsHgt_Type = TAntHeight
_SetGpsHgt_Object = MibTableColumn
setGpsHgt = _SetGpsHgt_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 3, 5, 1, 1, 12),
    _SetGpsHgt_Type()
)
setGpsHgt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    setGpsHgt.setStatus("current")


class _SetGpsZeroPhase_Type(Integer32):
    """Custom type setGpsZeroPhase based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("zeroPhA", 1),
          ("zeroPhB", 2),
          ("zeroPhAB", 3))
    )


_SetGpsZeroPhase_Type.__name__ = "Integer32"
_SetGpsZeroPhase_Object = MibTableColumn
setGpsZeroPhase = _SetGpsZeroPhase_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 3, 5, 1, 1, 13),
    _SetGpsZeroPhase_Type()
)
setGpsZeroPhase.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    setGpsZeroPhase.setStatus("current")


class _SetGpsTodsrcPriority_Type(Integer32):
    """Custom type setGpsTodsrcPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8),
    )


_SetGpsTodsrcPriority_Type.__name__ = "Integer32"
_SetGpsTodsrcPriority_Object = MibTableColumn
setGpsTodsrcPriority = _SetGpsTodsrcPriority_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 3, 5, 1, 1, 14),
    _SetGpsTodsrcPriority_Type()
)
setGpsTodsrcPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    setGpsTodsrcPriority.setStatus("current")


class _SetGpsTodsrcCompensation_Type(Integer32):
    """Custom type setGpsTodsrcCompensation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 250),
    )


_SetGpsTodsrcCompensation_Type.__name__ = "Integer32"
_SetGpsTodsrcCompensation_Object = MibTableColumn
setGpsTodsrcCompensation = _SetGpsTodsrcCompensation_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 3, 5, 1, 1, 15),
    _SetGpsTodsrcCompensation_Type()
)
setGpsTodsrcCompensation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    setGpsTodsrcCompensation.setStatus("current")


class _SetGnssConsMode_Type(Integer32):
    """Custom type setGnssConsMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("gps", 1),
          ("glonass", 2),
          ("gpsGlonass", 3))
    )


_SetGnssConsMode_Type.__name__ = "Integer32"
_SetGnssConsMode_Object = MibTableColumn
setGnssConsMode = _SetGnssConsMode_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 3, 5, 1, 1, 16),
    _SetGnssConsMode_Type()
)
setGnssConsMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    setGnssConsMode.setStatus("current")
_SetAlmThGpsInpTable_Object = MibTable
setAlmThGpsInpTable = _SetAlmThGpsInpTable_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 3, 5, 2)
)
if mibBuilder.loadTexts:
    setAlmThGpsInpTable.setStatus("current")
_SetMgEntry_Object = MibTableRow
setMgEntry = _SetMgEntry_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 3, 5, 2, 1)
)
setMgEntry.setIndexNames(
    (0, "SSU2000-MIB", "setMgChassis"),
    (0, "SSU2000-MIB", "setMgSlot"),
)
if mibBuilder.loadTexts:
    setMgEntry.setStatus("current")


class _SetMgChassis_Type(Integer32):
    """Custom type setMgChassis based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
    )


_SetMgChassis_Type.__name__ = "Integer32"
_SetMgChassis_Object = MibTableColumn
setMgChassis = _SetMgChassis_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 3, 5, 2, 1, 1),
    _SetMgChassis_Type()
)
setMgChassis.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    setMgChassis.setStatus("current")


class _SetMgSlot_Type(Integer32):
    """Custom type setMgSlot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 20),
    )


_SetMgSlot_Type.__name__ = "Integer32"
_SetMgSlot_Object = MibTableColumn
setMgSlot = _SetMgSlot_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 3, 5, 2, 1, 2),
    _SetMgSlot_Type()
)
setMgSlot.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    setMgSlot.setStatus("current")


class _SetMgMtieStd_Type(Integer32):
    """Custom type setMgMtieStd based on Integer32"""
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
        *(("prs", 1),
          ("ds1", 2),
          ("g811", 3),
          ("g823", 4))
    )


_SetMgMtieStd_Type.__name__ = "Integer32"
_SetMgMtieStd_Object = MibTableColumn
setMgMtieStd = _SetMgMtieStd_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 3, 5, 2, 1, 3),
    _SetMgMtieStd_Type()
)
setMgMtieStd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    setMgMtieStd.setStatus("current")


class _SetMgMtie10EL1_Type(Integer32):
    """Custom type setMgMtie10EL1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 60000),
    )


_SetMgMtie10EL1_Type.__name__ = "Integer32"
_SetMgMtie10EL1_Object = MibTableColumn
setMgMtie10EL1 = _SetMgMtie10EL1_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 3, 5, 2, 1, 4),
    _SetMgMtie10EL1_Type()
)
setMgMtie10EL1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    setMgMtie10EL1.setStatus("current")


class _SetMgMtie10EL2_Type(Integer32):
    """Custom type setMgMtie10EL2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 60000),
    )


_SetMgMtie10EL2_Type.__name__ = "Integer32"
_SetMgMtie10EL2_Object = MibTableColumn
setMgMtie10EL2 = _SetMgMtie10EL2_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 3, 5, 2, 1, 5),
    _SetMgMtie10EL2_Type()
)
setMgMtie10EL2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    setMgMtie10EL2.setStatus("current")


class _SetMgMtie10CL1_Type(Integer32):
    """Custom type setMgMtie10CL1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 60000),
    )


_SetMgMtie10CL1_Type.__name__ = "Integer32"
_SetMgMtie10CL1_Object = MibTableColumn
setMgMtie10CL1 = _SetMgMtie10CL1_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 3, 5, 2, 1, 6),
    _SetMgMtie10CL1_Type()
)
setMgMtie10CL1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    setMgMtie10CL1.setStatus("current")


class _SetMgMtie10CL2_Type(Integer32):
    """Custom type setMgMtie10CL2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 60000),
    )


_SetMgMtie10CL2_Type.__name__ = "Integer32"
_SetMgMtie10CL2_Object = MibTableColumn
setMgMtie10CL2 = _SetMgMtie10CL2_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 3, 5, 2, 1, 7),
    _SetMgMtie10CL2_Type()
)
setMgMtie10CL2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    setMgMtie10CL2.setStatus("current")


class _SetMgMtie100EL1_Type(Integer32):
    """Custom type setMgMtie100EL1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 60000),
    )


_SetMgMtie100EL1_Type.__name__ = "Integer32"
_SetMgMtie100EL1_Object = MibTableColumn
setMgMtie100EL1 = _SetMgMtie100EL1_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 3, 5, 2, 1, 8),
    _SetMgMtie100EL1_Type()
)
setMgMtie100EL1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    setMgMtie100EL1.setStatus("current")


class _SetMgMtie100EL2_Type(Integer32):
    """Custom type setMgMtie100EL2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 60000),
    )


_SetMgMtie100EL2_Type.__name__ = "Integer32"
_SetMgMtie100EL2_Object = MibTableColumn
setMgMtie100EL2 = _SetMgMtie100EL2_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 3, 5, 2, 1, 9),
    _SetMgMtie100EL2_Type()
)
setMgMtie100EL2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    setMgMtie100EL2.setStatus("current")


class _SetMgMtie100CL1_Type(Integer32):
    """Custom type setMgMtie100CL1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 60000),
    )


_SetMgMtie100CL1_Type.__name__ = "Integer32"
_SetMgMtie100CL1_Object = MibTableColumn
setMgMtie100CL1 = _SetMgMtie100CL1_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 3, 5, 2, 1, 10),
    _SetMgMtie100CL1_Type()
)
setMgMtie100CL1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    setMgMtie100CL1.setStatus("current")


class _SetMgMtie100CL2_Type(Integer32):
    """Custom type setMgMtie100CL2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 60000),
    )


_SetMgMtie100CL2_Type.__name__ = "Integer32"
_SetMgMtie100CL2_Object = MibTableColumn
setMgMtie100CL2 = _SetMgMtie100CL2_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 3, 5, 2, 1, 11),
    _SetMgMtie100CL2_Type()
)
setMgMtie100CL2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    setMgMtie100CL2.setStatus("current")


class _SetMgMtie1000EL1_Type(Integer32):
    """Custom type setMgMtie1000EL1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 60000),
    )


_SetMgMtie1000EL1_Type.__name__ = "Integer32"
_SetMgMtie1000EL1_Object = MibTableColumn
setMgMtie1000EL1 = _SetMgMtie1000EL1_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 3, 5, 2, 1, 12),
    _SetMgMtie1000EL1_Type()
)
setMgMtie1000EL1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    setMgMtie1000EL1.setStatus("current")


class _SetMgMtie1000EL2_Type(Integer32):
    """Custom type setMgMtie1000EL2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 60000),
    )


_SetMgMtie1000EL2_Type.__name__ = "Integer32"
_SetMgMtie1000EL2_Object = MibTableColumn
setMgMtie1000EL2 = _SetMgMtie1000EL2_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 3, 5, 2, 1, 13),
    _SetMgMtie1000EL2_Type()
)
setMgMtie1000EL2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    setMgMtie1000EL2.setStatus("current")


class _SetMgMtie1000CL1_Type(Integer32):
    """Custom type setMgMtie1000CL1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 60000),
    )


_SetMgMtie1000CL1_Type.__name__ = "Integer32"
_SetMgMtie1000CL1_Object = MibTableColumn
setMgMtie1000CL1 = _SetMgMtie1000CL1_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 3, 5, 2, 1, 14),
    _SetMgMtie1000CL1_Type()
)
setMgMtie1000CL1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    setMgMtie1000CL1.setStatus("current")


class _SetMgMtie1000CL2_Type(Integer32):
    """Custom type setMgMtie1000CL2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 60000),
    )


_SetMgMtie1000CL2_Type.__name__ = "Integer32"
_SetMgMtie1000CL2_Object = MibTableColumn
setMgMtie1000CL2 = _SetMgMtie1000CL2_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 3, 5, 2, 1, 15),
    _SetMgMtie1000CL2_Type()
)
setMgMtie1000CL2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    setMgMtie1000CL2.setStatus("current")


class _SetMgMtie10000EL1_Type(Integer32):
    """Custom type setMgMtie10000EL1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 60000),
    )


_SetMgMtie10000EL1_Type.__name__ = "Integer32"
_SetMgMtie10000EL1_Object = MibTableColumn
setMgMtie10000EL1 = _SetMgMtie10000EL1_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 3, 5, 2, 1, 16),
    _SetMgMtie10000EL1_Type()
)
setMgMtie10000EL1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    setMgMtie10000EL1.setStatus("current")


class _SetMgMtie10000EL2_Type(Integer32):
    """Custom type setMgMtie10000EL2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 60000),
    )


_SetMgMtie10000EL2_Type.__name__ = "Integer32"
_SetMgMtie10000EL2_Object = MibTableColumn
setMgMtie10000EL2 = _SetMgMtie10000EL2_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 3, 5, 2, 1, 17),
    _SetMgMtie10000EL2_Type()
)
setMgMtie10000EL2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    setMgMtie10000EL2.setStatus("current")


class _SetMgMtie10000CL1_Type(Integer32):
    """Custom type setMgMtie10000CL1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 60000),
    )


_SetMgMtie10000CL1_Type.__name__ = "Integer32"
_SetMgMtie10000CL1_Object = MibTableColumn
setMgMtie10000CL1 = _SetMgMtie10000CL1_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 3, 5, 2, 1, 18),
    _SetMgMtie10000CL1_Type()
)
setMgMtie10000CL1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    setMgMtie10000CL1.setStatus("current")


class _SetMgMtie10000CL2_Type(Integer32):
    """Custom type setMgMtie10000CL2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 60000),
    )


_SetMgMtie10000CL2_Type.__name__ = "Integer32"
_SetMgMtie10000CL2_Object = MibTableColumn
setMgMtie10000CL2 = _SetMgMtie10000CL2_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 3, 5, 2, 1, 19),
    _SetMgMtie10000CL2_Type()
)
setMgMtie10000CL2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    setMgMtie10000CL2.setStatus("current")


class _SetMgMtie100000EL1_Type(Integer32):
    """Custom type setMgMtie100000EL1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 60000),
    )


_SetMgMtie100000EL1_Type.__name__ = "Integer32"
_SetMgMtie100000EL1_Object = MibTableColumn
setMgMtie100000EL1 = _SetMgMtie100000EL1_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 3, 5, 2, 1, 20),
    _SetMgMtie100000EL1_Type()
)
setMgMtie100000EL1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    setMgMtie100000EL1.setStatus("current")


class _SetMgMtie100000EL2_Type(Integer32):
    """Custom type setMgMtie100000EL2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 60000),
    )


_SetMgMtie100000EL2_Type.__name__ = "Integer32"
_SetMgMtie100000EL2_Object = MibTableColumn
setMgMtie100000EL2 = _SetMgMtie100000EL2_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 3, 5, 2, 1, 21),
    _SetMgMtie100000EL2_Type()
)
setMgMtie100000EL2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    setMgMtie100000EL2.setStatus("current")


class _SetMgMtie100000CL1_Type(Integer32):
    """Custom type setMgMtie100000CL1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 60000),
    )


_SetMgMtie100000CL1_Type.__name__ = "Integer32"
_SetMgMtie100000CL1_Object = MibTableColumn
setMgMtie100000CL1 = _SetMgMtie100000CL1_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 3, 5, 2, 1, 22),
    _SetMgMtie100000CL1_Type()
)
setMgMtie100000CL1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    setMgMtie100000CL1.setStatus("current")


class _SetMgMtie100000CL2_Type(Integer32):
    """Custom type setMgMtie100000CL2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 60000),
    )


_SetMgMtie100000CL2_Type.__name__ = "Integer32"
_SetMgMtie100000CL2_Object = MibTableColumn
setMgMtie100000CL2 = _SetMgMtie100000CL2_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 3, 5, 2, 1, 23),
    _SetMgMtie100000CL2_Type()
)
setMgMtie100000CL2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    setMgMtie100000CL2.setStatus("current")


class _SetMgFreqAErrLmt_Type(Integer32):
    """Custom type setMgFreqAErrLmt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000000),
    )


_SetMgFreqAErrLmt_Type.__name__ = "Integer32"
_SetMgFreqAErrLmt_Object = MibTableColumn
setMgFreqAErrLmt = _SetMgFreqAErrLmt_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 3, 5, 2, 1, 24),
    _SetMgFreqAErrLmt_Type()
)
setMgFreqAErrLmt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    setMgFreqAErrLmt.setStatus("current")


class _SetMgFreqAClrLmt_Type(Integer32):
    """Custom type setMgFreqAClrLmt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000000),
    )


_SetMgFreqAClrLmt_Type.__name__ = "Integer32"
_SetMgFreqAClrLmt_Object = MibTableColumn
setMgFreqAClrLmt = _SetMgFreqAClrLmt_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 3, 5, 2, 1, 25),
    _SetMgFreqAClrLmt_Type()
)
setMgFreqAClrLmt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    setMgFreqAClrLmt.setStatus("current")


class _SetMgFreqATau_Type(Integer32):
    """Custom type setMgFreqATau based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 1000),
    )


_SetMgFreqATau_Type.__name__ = "Integer32"
_SetMgFreqATau_Object = MibTableColumn
setMgFreqATau = _SetMgFreqATau_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 3, 5, 2, 1, 26),
    _SetMgFreqATau_Type()
)
setMgFreqATau.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    setMgFreqATau.setStatus("current")


class _SetMgFreqBErrLmt_Type(Integer32):
    """Custom type setMgFreqBErrLmt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000000),
    )


_SetMgFreqBErrLmt_Type.__name__ = "Integer32"
_SetMgFreqBErrLmt_Object = MibTableColumn
setMgFreqBErrLmt = _SetMgFreqBErrLmt_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 3, 5, 2, 1, 27),
    _SetMgFreqBErrLmt_Type()
)
setMgFreqBErrLmt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    setMgFreqBErrLmt.setStatus("current")


class _SetMgFreqBClrLmt_Type(Integer32):
    """Custom type setMgFreqBClrLmt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000000),
    )


_SetMgFreqBClrLmt_Type.__name__ = "Integer32"
_SetMgFreqBClrLmt_Object = MibTableColumn
setMgFreqBClrLmt = _SetMgFreqBClrLmt_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 3, 5, 2, 1, 28),
    _SetMgFreqBClrLmt_Type()
)
setMgFreqBClrLmt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    setMgFreqBClrLmt.setStatus("current")


class _SetMgFreqBTau_Type(Integer32):
    """Custom type setMgFreqBTau based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 1000),
    )


_SetMgFreqBTau_Type.__name__ = "Integer32"
_SetMgFreqBTau_Object = MibTableColumn
setMgFreqBTau = _SetMgFreqBTau_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 3, 5, 2, 1, 29),
    _SetMgFreqBTau_Type()
)
setMgFreqBTau.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    setMgFreqBTau.setStatus("current")
_SetupDs1E1Inp_ObjectIdentity = ObjectIdentity
setupDs1E1Inp = _SetupDs1E1Inp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 3, 7)
)
_SetDs1E1InpTable_Object = MibTable
setDs1E1InpTable = _SetDs1E1InpTable_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 3, 7, 2)
)
if mibBuilder.loadTexts:
    setDs1E1InpTable.setStatus("current")
_SetDiEntry_Object = MibTableRow
setDiEntry = _SetDiEntry_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 3, 7, 2, 1)
)
setDiEntry.setIndexNames(
    (0, "SSU2000-MIB", "setDiChassis"),
    (0, "SSU2000-MIB", "setDiSlot"),
    (0, "SSU2000-MIB", "setDiPort"),
)
if mibBuilder.loadTexts:
    setDiEntry.setStatus("current")


class _SetDiChassis_Type(Integer32):
    """Custom type setDiChassis based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
    )


_SetDiChassis_Type.__name__ = "Integer32"
_SetDiChassis_Object = MibTableColumn
setDiChassis = _SetDiChassis_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 3, 7, 2, 1, 1),
    _SetDiChassis_Type()
)
setDiChassis.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    setDiChassis.setStatus("current")


class _SetDiSlot_Type(Integer32):
    """Custom type setDiSlot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 20),
    )


_SetDiSlot_Type.__name__ = "Integer32"
_SetDiSlot_Object = MibTableColumn
setDiSlot = _SetDiSlot_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 3, 7, 2, 1, 2),
    _SetDiSlot_Type()
)
setDiSlot.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    setDiSlot.setStatus("current")


class _SetDiPort_Type(Integer32):
    """Custom type setDiPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_SetDiPort_Type.__name__ = "Integer32"
_SetDiPort_Object = MibTableColumn
setDiPort = _SetDiPort_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 3, 7, 2, 1, 3),
    _SetDiPort_Type()
)
setDiPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    setDiPort.setStatus("current")
_SetDiEnable_Type = EnaValue
_SetDiEnable_Object = MibTableColumn
setDiEnable = _SetDiEnable_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 3, 7, 2, 1, 4),
    _SetDiEnable_Type()
)
setDiEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    setDiEnable.setStatus("current")


class _SetDiFrame_Type(Integer32):
    """Custom type setDiFrame based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9)
        )
    )
    namedValues = NamedValues(
        *(("esf", 1),
          ("d4", 2),
          ("ccs", 3),
          ("cas", 4),
          ("mhz1", 5),
          ("khz1544", 6),
          ("khz2048", 7),
          ("mhz5", 8),
          ("mhz10", 9))
    )


_SetDiFrame_Type.__name__ = "Integer32"
_SetDiFrame_Object = MibTableColumn
setDiFrame = _SetDiFrame_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 3, 7, 2, 1, 5),
    _SetDiFrame_Type()
)
setDiFrame.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    setDiFrame.setStatus("current")
_SetDiZS_Type = OnValue
_SetDiZS_Object = MibTableColumn
setDiZS = _SetDiZS_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 3, 7, 2, 1, 6),
    _SetDiZS_Type()
)
setDiZS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    setDiZS.setStatus("current")
_SetDiCRC_Type = OnValue
_SetDiCRC_Object = MibTableColumn
setDiCRC = _SetDiCRC_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 3, 7, 2, 1, 7),
    _SetDiCRC_Type()
)
setDiCRC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    setDiCRC.setStatus("current")
_SetDiSSM_Type = OnValue
_SetDiSSM_Object = MibTableColumn
setDiSSM = _SetDiSSM_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 3, 7, 2, 1, 8),
    _SetDiSSM_Type()
)
setDiSSM.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    setDiSSM.setStatus("current")


class _SetDiProvPql_Type(Integer32):
    """Custom type setDiProvPql based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 9),
    )


_SetDiProvPql_Type.__name__ = "Integer32"
_SetDiProvPql_Object = MibTableColumn
setDiProvPql = _SetDiProvPql_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 3, 7, 2, 1, 9),
    _SetDiProvPql_Type()
)
setDiProvPql.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    setDiProvPql.setStatus("current")


class _SetDiPriority_Type(Integer32):
    """Custom type setDiPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10),
    )


_SetDiPriority_Type.__name__ = "Integer32"
_SetDiPriority_Object = MibTableColumn
setDiPriority = _SetDiPriority_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 3, 7, 2, 1, 10),
    _SetDiPriority_Type()
)
setDiPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    setDiPriority.setStatus("current")
_SetDiGain_Type = OnValue
_SetDiGain_Object = MibTableColumn
setDiGain = _SetDiGain_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 3, 7, 2, 1, 11),
    _SetDiGain_Type()
)
setDiGain.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    setDiGain.setStatus("current")


class _SetDiCSFlt_Type(Integer32):
    """Custom type setDiCSFlt based on Integer32"""
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
        *(("off", 1),
          ("low", 2),
          ("high", 3),
          ("na", 4))
    )


_SetDiCSFlt_Type.__name__ = "Integer32"
_SetDiCSFlt_Object = MibTableColumn
setDiCSFlt = _SetDiCSFlt_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 3, 7, 2, 1, 12),
    _SetDiCSFlt_Type()
)
setDiCSFlt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    setDiCSFlt.setStatus("current")


class _SetDiE1SsmBit_Type(Integer32):
    """Custom type setDiE1SsmBit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(4, 8),
    )


_SetDiE1SsmBit_Type.__name__ = "Integer32"
_SetDiE1SsmBit_Object = MibTableColumn
setDiE1SsmBit = _SetDiE1SsmBit_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 3, 7, 2, 1, 13),
    _SetDiE1SsmBit_Type()
)
setDiE1SsmBit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    setDiE1SsmBit.setStatus("current")


class _SetDiZeroPhase_Type(Integer32):
    """Custom type setDiZeroPhase based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("zeroPhA", 1),
          ("zeroPhB", 2),
          ("zeroPhAB", 3))
    )


_SetDiZeroPhase_Type.__name__ = "Integer32"
_SetDiZeroPhase_Object = MibTableColumn
setDiZeroPhase = _SetDiZeroPhase_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 3, 7, 2, 1, 14),
    _SetDiZeroPhase_Type()
)
setDiZeroPhase.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    setDiZeroPhase.setStatus("current")


class _SetDiMtieCalc_Type(Integer32):
    """Custom type setDiMtieCalc based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("hz40", 1),
          ("hz1", 2))
    )


_SetDiMtieCalc_Type.__name__ = "Integer32"
_SetDiMtieCalc_Object = MibTableColumn
setDiMtieCalc = _SetDiMtieCalc_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 3, 7, 2, 1, 15),
    _SetDiMtieCalc_Type()
)
setDiMtieCalc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    setDiMtieCalc.setStatus("current")
_SetAlmThDs1E1InpTable_Object = MibTable
setAlmThDs1E1InpTable = _SetAlmThDs1E1InpTable_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 3, 7, 4)
)
if mibBuilder.loadTexts:
    setAlmThDs1E1InpTable.setStatus("current")
_SetMiEntry_Object = MibTableRow
setMiEntry = _SetMiEntry_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 3, 7, 4, 1)
)
setMiEntry.setIndexNames(
    (0, "SSU2000-MIB", "setMiChassis"),
    (0, "SSU2000-MIB", "setMiSlot"),
    (0, "SSU2000-MIB", "setMiPort"),
)
if mibBuilder.loadTexts:
    setMiEntry.setStatus("current")


class _SetMiChassis_Type(Integer32):
    """Custom type setMiChassis based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
    )


_SetMiChassis_Type.__name__ = "Integer32"
_SetMiChassis_Object = MibTableColumn
setMiChassis = _SetMiChassis_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 3, 7, 4, 1, 1),
    _SetMiChassis_Type()
)
setMiChassis.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    setMiChassis.setStatus("current")


class _SetMiSlot_Type(Integer32):
    """Custom type setMiSlot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 20),
    )


_SetMiSlot_Type.__name__ = "Integer32"
_SetMiSlot_Object = MibTableColumn
setMiSlot = _SetMiSlot_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 3, 7, 4, 1, 2),
    _SetMiSlot_Type()
)
setMiSlot.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    setMiSlot.setStatus("current")


class _SetMiPort_Type(Integer32):
    """Custom type setMiPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_SetMiPort_Type.__name__ = "Integer32"
_SetMiPort_Object = MibTableColumn
setMiPort = _SetMiPort_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 3, 7, 4, 1, 3),
    _SetMiPort_Type()
)
setMiPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    setMiPort.setStatus("current")


class _SetMiMtieStd_Type(Integer32):
    """Custom type setMiMtieStd based on Integer32"""
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
        *(("prs", 1),
          ("ds1", 2),
          ("g811", 3),
          ("g823", 4))
    )


_SetMiMtieStd_Type.__name__ = "Integer32"
_SetMiMtieStd_Object = MibTableColumn
setMiMtieStd = _SetMiMtieStd_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 3, 7, 4, 1, 4),
    _SetMiMtieStd_Type()
)
setMiMtieStd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    setMiMtieStd.setStatus("current")


class _SetMiMtie10EL1_Type(Integer32):
    """Custom type setMiMtie10EL1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 60000),
    )


_SetMiMtie10EL1_Type.__name__ = "Integer32"
_SetMiMtie10EL1_Object = MibTableColumn
setMiMtie10EL1 = _SetMiMtie10EL1_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 3, 7, 4, 1, 5),
    _SetMiMtie10EL1_Type()
)
setMiMtie10EL1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    setMiMtie10EL1.setStatus("current")


class _SetMiMtie10EL2_Type(Integer32):
    """Custom type setMiMtie10EL2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 60000),
    )


_SetMiMtie10EL2_Type.__name__ = "Integer32"
_SetMiMtie10EL2_Object = MibTableColumn
setMiMtie10EL2 = _SetMiMtie10EL2_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 3, 7, 4, 1, 6),
    _SetMiMtie10EL2_Type()
)
setMiMtie10EL2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    setMiMtie10EL2.setStatus("current")


class _SetMiMtie10CL1_Type(Integer32):
    """Custom type setMiMtie10CL1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 60000),
    )


_SetMiMtie10CL1_Type.__name__ = "Integer32"
_SetMiMtie10CL1_Object = MibTableColumn
setMiMtie10CL1 = _SetMiMtie10CL1_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 3, 7, 4, 1, 7),
    _SetMiMtie10CL1_Type()
)
setMiMtie10CL1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    setMiMtie10CL1.setStatus("current")


class _SetMiMtie10CL2_Type(Integer32):
    """Custom type setMiMtie10CL2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 60000),
    )


_SetMiMtie10CL2_Type.__name__ = "Integer32"
_SetMiMtie10CL2_Object = MibTableColumn
setMiMtie10CL2 = _SetMiMtie10CL2_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 3, 7, 4, 1, 8),
    _SetMiMtie10CL2_Type()
)
setMiMtie10CL2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    setMiMtie10CL2.setStatus("current")


class _SetMiMtie100EL1_Type(Integer32):
    """Custom type setMiMtie100EL1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 60000),
    )


_SetMiMtie100EL1_Type.__name__ = "Integer32"
_SetMiMtie100EL1_Object = MibTableColumn
setMiMtie100EL1 = _SetMiMtie100EL1_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 3, 7, 4, 1, 9),
    _SetMiMtie100EL1_Type()
)
setMiMtie100EL1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    setMiMtie100EL1.setStatus("current")


class _SetMiMtie100EL2_Type(Integer32):
    """Custom type setMiMtie100EL2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 60000),
    )


_SetMiMtie100EL2_Type.__name__ = "Integer32"
_SetMiMtie100EL2_Object = MibTableColumn
setMiMtie100EL2 = _SetMiMtie100EL2_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 3, 7, 4, 1, 10),
    _SetMiMtie100EL2_Type()
)
setMiMtie100EL2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    setMiMtie100EL2.setStatus("current")


class _SetMiMtie100CL1_Type(Integer32):
    """Custom type setMiMtie100CL1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 60000),
    )


_SetMiMtie100CL1_Type.__name__ = "Integer32"
_SetMiMtie100CL1_Object = MibTableColumn
setMiMtie100CL1 = _SetMiMtie100CL1_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 3, 7, 4, 1, 11),
    _SetMiMtie100CL1_Type()
)
setMiMtie100CL1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    setMiMtie100CL1.setStatus("current")


class _SetMiMtie100CL2_Type(Integer32):
    """Custom type setMiMtie100CL2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 60000),
    )


_SetMiMtie100CL2_Type.__name__ = "Integer32"
_SetMiMtie100CL2_Object = MibTableColumn
setMiMtie100CL2 = _SetMiMtie100CL2_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 3, 7, 4, 1, 12),
    _SetMiMtie100CL2_Type()
)
setMiMtie100CL2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    setMiMtie100CL2.setStatus("current")


class _SetMiMtie1000EL1_Type(Integer32):
    """Custom type setMiMtie1000EL1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 60000),
    )


_SetMiMtie1000EL1_Type.__name__ = "Integer32"
_SetMiMtie1000EL1_Object = MibTableColumn
setMiMtie1000EL1 = _SetMiMtie1000EL1_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 3, 7, 4, 1, 13),
    _SetMiMtie1000EL1_Type()
)
setMiMtie1000EL1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    setMiMtie1000EL1.setStatus("current")


class _SetMiMtie1000EL2_Type(Integer32):
    """Custom type setMiMtie1000EL2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 60000),
    )


_SetMiMtie1000EL2_Type.__name__ = "Integer32"
_SetMiMtie1000EL2_Object = MibTableColumn
setMiMtie1000EL2 = _SetMiMtie1000EL2_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 3, 7, 4, 1, 14),
    _SetMiMtie1000EL2_Type()
)
setMiMtie1000EL2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    setMiMtie1000EL2.setStatus("current")


class _SetMiMtie1000CL1_Type(Integer32):
    """Custom type setMiMtie1000CL1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 60000),
    )


_SetMiMtie1000CL1_Type.__name__ = "Integer32"
_SetMiMtie1000CL1_Object = MibTableColumn
setMiMtie1000CL1 = _SetMiMtie1000CL1_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 3, 7, 4, 1, 15),
    _SetMiMtie1000CL1_Type()
)
setMiMtie1000CL1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    setMiMtie1000CL1.setStatus("current")


class _SetMiMtie1000CL2_Type(Integer32):
    """Custom type setMiMtie1000CL2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 60000),
    )


_SetMiMtie1000CL2_Type.__name__ = "Integer32"
_SetMiMtie1000CL2_Object = MibTableColumn
setMiMtie1000CL2 = _SetMiMtie1000CL2_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 3, 7, 4, 1, 16),
    _SetMiMtie1000CL2_Type()
)
setMiMtie1000CL2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    setMiMtie1000CL2.setStatus("current")


class _SetMiMtie10000EL1_Type(Integer32):
    """Custom type setMiMtie10000EL1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 60000),
    )


_SetMiMtie10000EL1_Type.__name__ = "Integer32"
_SetMiMtie10000EL1_Object = MibTableColumn
setMiMtie10000EL1 = _SetMiMtie10000EL1_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 3, 7, 4, 1, 17),
    _SetMiMtie10000EL1_Type()
)
setMiMtie10000EL1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    setMiMtie10000EL1.setStatus("current")


class _SetMiMtie10000EL2_Type(Integer32):
    """Custom type setMiMtie10000EL2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 60000),
    )


_SetMiMtie10000EL2_Type.__name__ = "Integer32"
_SetMiMtie10000EL2_Object = MibTableColumn
setMiMtie10000EL2 = _SetMiMtie10000EL2_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 3, 7, 4, 1, 18),
    _SetMiMtie10000EL2_Type()
)
setMiMtie10000EL2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    setMiMtie10000EL2.setStatus("current")


class _SetMiMtie10000CL1_Type(Integer32):
    """Custom type setMiMtie10000CL1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 60000),
    )


_SetMiMtie10000CL1_Type.__name__ = "Integer32"
_SetMiMtie10000CL1_Object = MibTableColumn
setMiMtie10000CL1 = _SetMiMtie10000CL1_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 3, 7, 4, 1, 19),
    _SetMiMtie10000CL1_Type()
)
setMiMtie10000CL1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    setMiMtie10000CL1.setStatus("current")


class _SetMiMtie10000CL2_Type(Integer32):
    """Custom type setMiMtie10000CL2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 60000),
    )


_SetMiMtie10000CL2_Type.__name__ = "Integer32"
_SetMiMtie10000CL2_Object = MibTableColumn
setMiMtie10000CL2 = _SetMiMtie10000CL2_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 3, 7, 4, 1, 20),
    _SetMiMtie10000CL2_Type()
)
setMiMtie10000CL2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    setMiMtie10000CL2.setStatus("current")


class _SetMiMtie100000EL1_Type(Integer32):
    """Custom type setMiMtie100000EL1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 60000),
    )


_SetMiMtie100000EL1_Type.__name__ = "Integer32"
_SetMiMtie100000EL1_Object = MibTableColumn
setMiMtie100000EL1 = _SetMiMtie100000EL1_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 3, 7, 4, 1, 21),
    _SetMiMtie100000EL1_Type()
)
setMiMtie100000EL1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    setMiMtie100000EL1.setStatus("current")


class _SetMiMtie100000EL2_Type(Integer32):
    """Custom type setMiMtie100000EL2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 60000),
    )


_SetMiMtie100000EL2_Type.__name__ = "Integer32"
_SetMiMtie100000EL2_Object = MibTableColumn
setMiMtie100000EL2 = _SetMiMtie100000EL2_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 3, 7, 4, 1, 22),
    _SetMiMtie100000EL2_Type()
)
setMiMtie100000EL2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    setMiMtie100000EL2.setStatus("current")


class _SetMiMtie100000CL1_Type(Integer32):
    """Custom type setMiMtie100000CL1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 60000),
    )


_SetMiMtie100000CL1_Type.__name__ = "Integer32"
_SetMiMtie100000CL1_Object = MibTableColumn
setMiMtie100000CL1 = _SetMiMtie100000CL1_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 3, 7, 4, 1, 23),
    _SetMiMtie100000CL1_Type()
)
setMiMtie100000CL1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    setMiMtie100000CL1.setStatus("current")


class _SetMiMtie100000CL2_Type(Integer32):
    """Custom type setMiMtie100000CL2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 60000),
    )


_SetMiMtie100000CL2_Type.__name__ = "Integer32"
_SetMiMtie100000CL2_Object = MibTableColumn
setMiMtie100000CL2 = _SetMiMtie100000CL2_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 3, 7, 4, 1, 24),
    _SetMiMtie100000CL2_Type()
)
setMiMtie100000CL2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    setMiMtie100000CL2.setStatus("current")


class _SetMiFreqAErrLmt_Type(Integer32):
    """Custom type setMiFreqAErrLmt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000000),
    )


_SetMiFreqAErrLmt_Type.__name__ = "Integer32"
_SetMiFreqAErrLmt_Object = MibTableColumn
setMiFreqAErrLmt = _SetMiFreqAErrLmt_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 3, 7, 4, 1, 25),
    _SetMiFreqAErrLmt_Type()
)
setMiFreqAErrLmt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    setMiFreqAErrLmt.setStatus("current")


class _SetMiFreqAClrLmt_Type(Integer32):
    """Custom type setMiFreqAClrLmt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000000),
    )


_SetMiFreqAClrLmt_Type.__name__ = "Integer32"
_SetMiFreqAClrLmt_Object = MibTableColumn
setMiFreqAClrLmt = _SetMiFreqAClrLmt_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 3, 7, 4, 1, 26),
    _SetMiFreqAClrLmt_Type()
)
setMiFreqAClrLmt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    setMiFreqAClrLmt.setStatus("current")


class _SetMiFreqATau_Type(Integer32):
    """Custom type setMiFreqATau based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 1000),
    )


_SetMiFreqATau_Type.__name__ = "Integer32"
_SetMiFreqATau_Object = MibTableColumn
setMiFreqATau = _SetMiFreqATau_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 3, 7, 4, 1, 27),
    _SetMiFreqATau_Type()
)
setMiFreqATau.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    setMiFreqATau.setStatus("current")


class _SetMiFreqBErrLmt_Type(Integer32):
    """Custom type setMiFreqBErrLmt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000000),
    )


_SetMiFreqBErrLmt_Type.__name__ = "Integer32"
_SetMiFreqBErrLmt_Object = MibTableColumn
setMiFreqBErrLmt = _SetMiFreqBErrLmt_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 3, 7, 4, 1, 28),
    _SetMiFreqBErrLmt_Type()
)
setMiFreqBErrLmt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    setMiFreqBErrLmt.setStatus("current")


class _SetMiFreqBClrLmt_Type(Integer32):
    """Custom type setMiFreqBClrLmt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000000),
    )


_SetMiFreqBClrLmt_Type.__name__ = "Integer32"
_SetMiFreqBClrLmt_Object = MibTableColumn
setMiFreqBClrLmt = _SetMiFreqBClrLmt_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 3, 7, 4, 1, 29),
    _SetMiFreqBClrLmt_Type()
)
setMiFreqBClrLmt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    setMiFreqBClrLmt.setStatus("current")


class _SetMiFreqBTau_Type(Integer32):
    """Custom type setMiFreqBTau based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 1000),
    )


_SetMiFreqBTau_Type.__name__ = "Integer32"
_SetMiFreqBTau_Object = MibTableColumn
setMiFreqBTau = _SetMiFreqBTau_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 3, 7, 4, 1, 30),
    _SetMiFreqBTau_Type()
)
setMiFreqBTau.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    setMiFreqBTau.setStatus("current")


class _SetMiLOSErrCnt_Type(Integer32):
    """Custom type setMiLOSErrCnt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_SetMiLOSErrCnt_Type.__name__ = "Integer32"
_SetMiLOSErrCnt_Object = MibTableColumn
setMiLOSErrCnt = _SetMiLOSErrCnt_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 3, 7, 4, 1, 31),
    _SetMiLOSErrCnt_Type()
)
setMiLOSErrCnt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    setMiLOSErrCnt.setStatus("current")


class _SetMiLOSClrCnt_Type(Integer32):
    """Custom type setMiLOSClrCnt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_SetMiLOSClrCnt_Type.__name__ = "Integer32"
_SetMiLOSClrCnt_Object = MibTableColumn
setMiLOSClrCnt = _SetMiLOSClrCnt_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 3, 7, 4, 1, 32),
    _SetMiLOSClrCnt_Type()
)
setMiLOSClrCnt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    setMiLOSClrCnt.setStatus("current")


class _SetMiAISErrCnt_Type(Integer32):
    """Custom type setMiAISErrCnt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_SetMiAISErrCnt_Type.__name__ = "Integer32"
_SetMiAISErrCnt_Object = MibTableColumn
setMiAISErrCnt = _SetMiAISErrCnt_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 3, 7, 4, 1, 33),
    _SetMiAISErrCnt_Type()
)
setMiAISErrCnt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    setMiAISErrCnt.setStatus("current")


class _SetMiAISClrCnt_Type(Integer32):
    """Custom type setMiAISClrCnt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_SetMiAISClrCnt_Type.__name__ = "Integer32"
_SetMiAISClrCnt_Object = MibTableColumn
setMiAISClrCnt = _SetMiAISClrCnt_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 3, 7, 4, 1, 34),
    _SetMiAISClrCnt_Type()
)
setMiAISClrCnt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    setMiAISClrCnt.setStatus("current")


class _SetMiOOFErrCnt_Type(Integer32):
    """Custom type setMiOOFErrCnt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10000),
    )


_SetMiOOFErrCnt_Type.__name__ = "Integer32"
_SetMiOOFErrCnt_Object = MibTableColumn
setMiOOFErrCnt = _SetMiOOFErrCnt_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 3, 7, 4, 1, 35),
    _SetMiOOFErrCnt_Type()
)
setMiOOFErrCnt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    setMiOOFErrCnt.setStatus("current")


class _SetMiOOFClrCnt_Type(Integer32):
    """Custom type setMiOOFClrCnt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10000),
    )


_SetMiOOFClrCnt_Type.__name__ = "Integer32"
_SetMiOOFClrCnt_Object = MibTableColumn
setMiOOFClrCnt = _SetMiOOFClrCnt_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 3, 7, 4, 1, 36),
    _SetMiOOFClrCnt_Type()
)
setMiOOFClrCnt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    setMiOOFClrCnt.setStatus("current")


class _SetMiBPVErrCnt_Type(Integer32):
    """Custom type setMiBPVErrCnt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10000),
    )


_SetMiBPVErrCnt_Type.__name__ = "Integer32"
_SetMiBPVErrCnt_Object = MibTableColumn
setMiBPVErrCnt = _SetMiBPVErrCnt_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 3, 7, 4, 1, 37),
    _SetMiBPVErrCnt_Type()
)
setMiBPVErrCnt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    setMiBPVErrCnt.setStatus("current")


class _SetMiBPVClrCnt_Type(Integer32):
    """Custom type setMiBPVClrCnt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10000),
    )


_SetMiBPVClrCnt_Type.__name__ = "Integer32"
_SetMiBPVClrCnt_Object = MibTableColumn
setMiBPVClrCnt = _SetMiBPVClrCnt_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 3, 7, 4, 1, 38),
    _SetMiBPVClrCnt_Type()
)
setMiBPVClrCnt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    setMiBPVClrCnt.setStatus("current")


class _SetMiCRCErrCnt_Type(Integer32):
    """Custom type setMiCRCErrCnt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10000),
    )


_SetMiCRCErrCnt_Type.__name__ = "Integer32"
_SetMiCRCErrCnt_Object = MibTableColumn
setMiCRCErrCnt = _SetMiCRCErrCnt_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 3, 7, 4, 1, 39),
    _SetMiCRCErrCnt_Type()
)
setMiCRCErrCnt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    setMiCRCErrCnt.setStatus("current")


class _SetMiCRCClrCnt_Type(Integer32):
    """Custom type setMiCRCClrCnt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10000),
    )


_SetMiCRCClrCnt_Type.__name__ = "Integer32"
_SetMiCRCClrCnt_Object = MibTableColumn
setMiCRCClrCnt = _SetMiCRCClrCnt_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 3, 7, 4, 1, 40),
    _SetMiCRCClrCnt_Type()
)
setMiCRCClrCnt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    setMiCRCClrCnt.setStatus("current")
_SetupCcInp_ObjectIdentity = ObjectIdentity
setupCcInp = _SetupCcInp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 3, 8)
)
_SetCcInpTable_Object = MibTable
setCcInpTable = _SetCcInpTable_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 3, 8, 2)
)
if mibBuilder.loadTexts:
    setCcInpTable.setStatus("current")
_SetCiEntry_Object = MibTableRow
setCiEntry = _SetCiEntry_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 3, 8, 2, 1)
)
setCiEntry.setIndexNames(
    (0, "SSU2000-MIB", "setCiChassis"),
    (0, "SSU2000-MIB", "setCiSlot"),
    (0, "SSU2000-MIB", "setCiPort"),
)
if mibBuilder.loadTexts:
    setCiEntry.setStatus("current")


class _SetCiChassis_Type(Integer32):
    """Custom type setCiChassis based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
    )


_SetCiChassis_Type.__name__ = "Integer32"
_SetCiChassis_Object = MibTableColumn
setCiChassis = _SetCiChassis_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 3, 8, 2, 1, 1),
    _SetCiChassis_Type()
)
setCiChassis.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    setCiChassis.setStatus("current")


class _SetCiSlot_Type(Integer32):
    """Custom type setCiSlot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 20),
    )


_SetCiSlot_Type.__name__ = "Integer32"
_SetCiSlot_Object = MibTableColumn
setCiSlot = _SetCiSlot_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 3, 8, 2, 1, 2),
    _SetCiSlot_Type()
)
setCiSlot.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    setCiSlot.setStatus("current")


class _SetCiPort_Type(Integer32):
    """Custom type setCiPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_SetCiPort_Type.__name__ = "Integer32"
_SetCiPort_Object = MibTableColumn
setCiPort = _SetCiPort_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 3, 8, 2, 1, 3),
    _SetCiPort_Type()
)
setCiPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    setCiPort.setStatus("current")
_SetCiEnable_Type = EnaValue
_SetCiEnable_Object = MibTableColumn
setCiEnable = _SetCiEnable_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 3, 8, 2, 1, 4),
    _SetCiEnable_Type()
)
setCiEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    setCiEnable.setStatus("current")


class _SetCiProvPql_Type(Integer32):
    """Custom type setCiProvPql based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 9),
    )


_SetCiProvPql_Type.__name__ = "Integer32"
_SetCiProvPql_Object = MibTableColumn
setCiProvPql = _SetCiProvPql_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 3, 8, 2, 1, 7),
    _SetCiProvPql_Type()
)
setCiProvPql.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    setCiProvPql.setStatus("current")


class _SetCiPriority_Type(Integer32):
    """Custom type setCiPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10),
    )


_SetCiPriority_Type.__name__ = "Integer32"
_SetCiPriority_Object = MibTableColumn
setCiPriority = _SetCiPriority_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 3, 8, 2, 1, 8),
    _SetCiPriority_Type()
)
setCiPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    setCiPriority.setStatus("current")


class _SetCiZeroPhase_Type(Integer32):
    """Custom type setCiZeroPhase based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("zeroPhA", 1),
          ("zeroPhB", 2),
          ("zeroPhAB", 3))
    )


_SetCiZeroPhase_Type.__name__ = "Integer32"
_SetCiZeroPhase_Object = MibTableColumn
setCiZeroPhase = _SetCiZeroPhase_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 3, 8, 2, 1, 9),
    _SetCiZeroPhase_Type()
)
setCiZeroPhase.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    setCiZeroPhase.setStatus("current")
_SetAlmThCcInpTable_Object = MibTable
setAlmThCcInpTable = _SetAlmThCcInpTable_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 3, 8, 4)
)
if mibBuilder.loadTexts:
    setAlmThCcInpTable.setStatus("current")
_SetCimEntry_Object = MibTableRow
setCimEntry = _SetCimEntry_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 3, 8, 4, 1)
)
setCimEntry.setIndexNames(
    (0, "SSU2000-MIB", "setCimChassis"),
    (0, "SSU2000-MIB", "setCimSlot"),
    (0, "SSU2000-MIB", "setCimPort"),
)
if mibBuilder.loadTexts:
    setCimEntry.setStatus("current")


class _SetCimChassis_Type(Integer32):
    """Custom type setCimChassis based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
    )


_SetCimChassis_Type.__name__ = "Integer32"
_SetCimChassis_Object = MibTableColumn
setCimChassis = _SetCimChassis_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 3, 8, 4, 1, 1),
    _SetCimChassis_Type()
)
setCimChassis.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    setCimChassis.setStatus("current")


class _SetCimSlot_Type(Integer32):
    """Custom type setCimSlot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 20),
    )


_SetCimSlot_Type.__name__ = "Integer32"
_SetCimSlot_Object = MibTableColumn
setCimSlot = _SetCimSlot_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 3, 8, 4, 1, 2),
    _SetCimSlot_Type()
)
setCimSlot.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    setCimSlot.setStatus("current")


class _SetCimPort_Type(Integer32):
    """Custom type setCimPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_SetCimPort_Type.__name__ = "Integer32"
_SetCimPort_Object = MibTableColumn
setCimPort = _SetCimPort_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 3, 8, 4, 1, 3),
    _SetCimPort_Type()
)
setCimPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    setCimPort.setStatus("current")


class _SetCimLOSErrCnt_Type(Integer32):
    """Custom type setCimLOSErrCnt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_SetCimLOSErrCnt_Type.__name__ = "Integer32"
_SetCimLOSErrCnt_Object = MibTableColumn
setCimLOSErrCnt = _SetCimLOSErrCnt_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 3, 8, 4, 1, 4),
    _SetCimLOSErrCnt_Type()
)
setCimLOSErrCnt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    setCimLOSErrCnt.setStatus("current")


class _SetCimLOSClrCnt_Type(Integer32):
    """Custom type setCimLOSClrCnt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_SetCimLOSClrCnt_Type.__name__ = "Integer32"
_SetCimLOSClrCnt_Object = MibTableColumn
setCimLOSClrCnt = _SetCimLOSClrCnt_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 3, 8, 4, 1, 5),
    _SetCimLOSClrCnt_Type()
)
setCimLOSClrCnt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    setCimLOSClrCnt.setStatus("current")


class _SetCimBPVErrCnt_Type(Integer32):
    """Custom type setCimBPVErrCnt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10000),
    )


_SetCimBPVErrCnt_Type.__name__ = "Integer32"
_SetCimBPVErrCnt_Object = MibTableColumn
setCimBPVErrCnt = _SetCimBPVErrCnt_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 3, 8, 4, 1, 10),
    _SetCimBPVErrCnt_Type()
)
setCimBPVErrCnt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    setCimBPVErrCnt.setStatus("current")


class _SetCimBPVClrCnt_Type(Integer32):
    """Custom type setCimBPVClrCnt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10000),
    )


_SetCimBPVClrCnt_Type.__name__ = "Integer32"
_SetCimBPVClrCnt_Object = MibTableColumn
setCimBPVClrCnt = _SetCimBPVClrCnt_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 3, 8, 4, 1, 11),
    _SetCimBPVClrCnt_Type()
)
setCimBPVClrCnt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    setCimBPVClrCnt.setStatus("current")
_SetupDs1Out_ObjectIdentity = ObjectIdentity
setupDs1Out = _SetupDs1Out_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 3, 10)
)
_SetDsTable_Object = MibTable
setDsTable = _SetDsTable_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 3, 10, 2)
)
if mibBuilder.loadTexts:
    setDsTable.setStatus("current")
_SetDsEntry_Object = MibTableRow
setDsEntry = _SetDsEntry_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 3, 10, 2, 1)
)
setDsEntry.setIndexNames(
    (0, "SSU2000-MIB", "setDsChassis"),
    (0, "SSU2000-MIB", "setDsSlot"),
)
if mibBuilder.loadTexts:
    setDsEntry.setStatus("current")


class _SetDsChassis_Type(Integer32):
    """Custom type setDsChassis based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_SetDsChassis_Type.__name__ = "Integer32"
_SetDsChassis_Object = MibTableColumn
setDsChassis = _SetDsChassis_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 3, 10, 2, 1, 1),
    _SetDsChassis_Type()
)
setDsChassis.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    setDsChassis.setStatus("current")


class _SetDsSlot_Type(Integer32):
    """Custom type setDsSlot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 20),
    )


_SetDsSlot_Type.__name__ = "Integer32"
_SetDsSlot_Object = MibTableColumn
setDsSlot = _SetDsSlot_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 3, 10, 2, 1, 2),
    _SetDsSlot_Type()
)
setDsSlot.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    setDsSlot.setStatus("current")


class _SetDsFrame_Type(Integer32):
    """Custom type setDsFrame based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("esf", 1),
          ("d4", 2))
    )


_SetDsFrame_Type.__name__ = "Integer32"
_SetDsFrame_Object = MibTableColumn
setDsFrame = _SetDsFrame_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 3, 10, 2, 1, 3),
    _SetDsFrame_Type()
)
setDsFrame.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    setDsFrame.setStatus("current")
_SetDsBypass_Type = OnValue
_SetDsBypass_Object = MibTableColumn
setDsBypass = _SetDsBypass_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 3, 10, 2, 1, 4),
    _SetDsBypass_Type()
)
setDsBypass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    setDsBypass.setStatus("current")
_SetDsZs_Type = OnValue
_SetDsZs_Object = MibTableColumn
setDsZs = _SetDsZs_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 3, 10, 2, 1, 5),
    _SetDsZs_Type()
)
setDsZs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    setDsZs.setStatus("current")


class _SetDsEnable_Type(OctetString):
    """Custom type setDsEnable based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(20, 20),
    )
    fixed_length = 20


_SetDsEnable_Type.__name__ = "OctetString"
_SetDsEnable_Object = MibTableColumn
setDsEnable = _SetDsEnable_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 3, 10, 2, 1, 6),
    _SetDsEnable_Type()
)
setDsEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    setDsEnable.setStatus("current")


class _SetDsLength_Type(OctetString):
    """Custom type setDsLength based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(20, 20),
    )
    fixed_length = 20


_SetDsLength_Type.__name__ = "OctetString"
_SetDsLength_Object = MibTableColumn
setDsLength = _SetDsLength_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 3, 10, 2, 1, 7),
    _SetDsLength_Type()
)
setDsLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    setDsLength.setStatus("current")
_SetupE1Out_ObjectIdentity = ObjectIdentity
setupE1Out = _SetupE1Out_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 3, 11)
)
_SetE1Table_Object = MibTable
setE1Table = _SetE1Table_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 3, 11, 2)
)
if mibBuilder.loadTexts:
    setE1Table.setStatus("current")
_SetE1Entry_Object = MibTableRow
setE1Entry = _SetE1Entry_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 3, 11, 2, 1)
)
setE1Entry.setIndexNames(
    (0, "SSU2000-MIB", "setE1Chassis"),
    (0, "SSU2000-MIB", "setE1Slot"),
)
if mibBuilder.loadTexts:
    setE1Entry.setStatus("current")


class _SetE1Chassis_Type(Integer32):
    """Custom type setE1Chassis based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_SetE1Chassis_Type.__name__ = "Integer32"
_SetE1Chassis_Object = MibTableColumn
setE1Chassis = _SetE1Chassis_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 3, 11, 2, 1, 1),
    _SetE1Chassis_Type()
)
setE1Chassis.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    setE1Chassis.setStatus("current")


class _SetE1Slot_Type(Integer32):
    """Custom type setE1Slot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 20),
    )


_SetE1Slot_Type.__name__ = "Integer32"
_SetE1Slot_Object = MibTableColumn
setE1Slot = _SetE1Slot_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 3, 11, 2, 1, 2),
    _SetE1Slot_Type()
)
setE1Slot.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    setE1Slot.setStatus("current")


class _SetE1Frame_Type(Integer32):
    """Custom type setE1Frame based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ccs", 1),
          ("cas", 2))
    )


_SetE1Frame_Type.__name__ = "Integer32"
_SetE1Frame_Object = MibTableColumn
setE1Frame = _SetE1Frame_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 3, 11, 2, 1, 3),
    _SetE1Frame_Type()
)
setE1Frame.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    setE1Frame.setStatus("current")
_SetE1Bypass_Type = OnValue
_SetE1Bypass_Object = MibTableColumn
setE1Bypass = _SetE1Bypass_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 3, 11, 2, 1, 4),
    _SetE1Bypass_Type()
)
setE1Bypass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    setE1Bypass.setStatus("current")
_SetE1Zs_Type = OnValue
_SetE1Zs_Object = MibTableColumn
setE1Zs = _SetE1Zs_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 3, 11, 2, 1, 5),
    _SetE1Zs_Type()
)
setE1Zs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    setE1Zs.setStatus("current")
_SetE1Crc_Type = OnValue
_SetE1Crc_Object = MibTableColumn
setE1Crc = _SetE1Crc_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 3, 11, 2, 1, 6),
    _SetE1Crc_Type()
)
setE1Crc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    setE1Crc.setStatus("current")


class _SetE1SsmBit_Type(Integer32):
    """Custom type setE1SsmBit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(4, 8),
    )


_SetE1SsmBit_Type.__name__ = "Integer32"
_SetE1SsmBit_Object = MibTableColumn
setE1SsmBit = _SetE1SsmBit_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 3, 11, 2, 1, 7),
    _SetE1SsmBit_Type()
)
setE1SsmBit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    setE1SsmBit.setStatus("current")


class _SetE1Enable_Type(OctetString):
    """Custom type setE1Enable based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(20, 20),
    )
    fixed_length = 20


_SetE1Enable_Type.__name__ = "OctetString"
_SetE1Enable_Object = MibTableColumn
setE1Enable = _SetE1Enable_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 3, 11, 2, 1, 8),
    _SetE1Enable_Type()
)
setE1Enable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    setE1Enable.setStatus("current")
_Setup2048Out_ObjectIdentity = ObjectIdentity
setup2048Out = _Setup2048Out_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 3, 12)
)
_SetCoTable_Object = MibTable
setCoTable = _SetCoTable_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 3, 12, 2)
)
if mibBuilder.loadTexts:
    setCoTable.setStatus("current")
_SetCoEntry_Object = MibTableRow
setCoEntry = _SetCoEntry_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 3, 12, 2, 1)
)
setCoEntry.setIndexNames(
    (0, "SSU2000-MIB", "setCoChassis"),
    (0, "SSU2000-MIB", "setCoSlot"),
)
if mibBuilder.loadTexts:
    setCoEntry.setStatus("current")


class _SetCoChassis_Type(Integer32):
    """Custom type setCoChassis based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_SetCoChassis_Type.__name__ = "Integer32"
_SetCoChassis_Object = MibTableColumn
setCoChassis = _SetCoChassis_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 3, 12, 2, 1, 1),
    _SetCoChassis_Type()
)
setCoChassis.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    setCoChassis.setStatus("current")


class _SetCoSlot_Type(Integer32):
    """Custom type setCoSlot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 20),
    )


_SetCoSlot_Type.__name__ = "Integer32"
_SetCoSlot_Object = MibTableColumn
setCoSlot = _SetCoSlot_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 3, 12, 2, 1, 2),
    _SetCoSlot_Type()
)
setCoSlot.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    setCoSlot.setStatus("current")
_SetCoBypass_Type = OnValue
_SetCoBypass_Object = MibTableColumn
setCoBypass = _SetCoBypass_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 3, 12, 2, 1, 3),
    _SetCoBypass_Type()
)
setCoBypass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    setCoBypass.setStatus("current")


class _SetCoFltMode_Type(Integer32):
    """Custom type setCoFltMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2),
          ("auto", 3))
    )


_SetCoFltMode_Type.__name__ = "Integer32"
_SetCoFltMode_Object = MibTableColumn
setCoFltMode = _SetCoFltMode_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 3, 12, 2, 1, 4),
    _SetCoFltMode_Type()
)
setCoFltMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    setCoFltMode.setStatus("current")


class _SetCoEnable_Type(OctetString):
    """Custom type setCoEnable based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(20, 20),
    )
    fixed_length = 20


_SetCoEnable_Type.__name__ = "OctetString"
_SetCoEnable_Object = MibTableColumn
setCoEnable = _SetCoEnable_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 3, 12, 2, 1, 5),
    _SetCoEnable_Type()
)
setCoEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    setCoEnable.setStatus("current")


class _SetCoSquelch_Type(OctetString):
    """Custom type setCoSquelch based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(20, 20),
    )
    fixed_length = 20


_SetCoSquelch_Type.__name__ = "OctetString"
_SetCoSquelch_Object = MibTableColumn
setCoSquelch = _SetCoSquelch_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 3, 12, 2, 1, 6),
    _SetCoSquelch_Type()
)
setCoSquelch.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    setCoSquelch.setStatus("current")
_SetupCCOut_ObjectIdentity = ObjectIdentity
setupCCOut = _SetupCCOut_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 3, 13)
)
_SetCcTable_Object = MibTable
setCcTable = _SetCcTable_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 3, 13, 2)
)
if mibBuilder.loadTexts:
    setCcTable.setStatus("current")
_SetCcEntry_Object = MibTableRow
setCcEntry = _SetCcEntry_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 3, 13, 2, 1)
)
setCcEntry.setIndexNames(
    (0, "SSU2000-MIB", "setCcChassis"),
    (0, "SSU2000-MIB", "setCcSlot"),
)
if mibBuilder.loadTexts:
    setCcEntry.setStatus("current")


class _SetCcChassis_Type(Integer32):
    """Custom type setCcChassis based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_SetCcChassis_Type.__name__ = "Integer32"
_SetCcChassis_Object = MibTableColumn
setCcChassis = _SetCcChassis_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 3, 13, 2, 1, 1),
    _SetCcChassis_Type()
)
setCcChassis.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    setCcChassis.setStatus("current")


class _SetCcSlot_Type(Integer32):
    """Custom type setCcSlot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 20),
    )


_SetCcSlot_Type.__name__ = "Integer32"
_SetCcSlot_Object = MibTableColumn
setCcSlot = _SetCcSlot_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 3, 13, 2, 1, 2),
    _SetCcSlot_Type()
)
setCcSlot.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    setCcSlot.setStatus("current")
_SetCcBypass_Type = OnValue
_SetCcBypass_Object = MibTableColumn
setCcBypass = _SetCcBypass_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 3, 13, 2, 1, 3),
    _SetCcBypass_Type()
)
setCcBypass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    setCcBypass.setStatus("current")


class _SetCcEnable_Type(OctetString):
    """Custom type setCcEnable based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(20, 20),
    )
    fixed_length = 20


_SetCcEnable_Type.__name__ = "OctetString"
_SetCcEnable_Object = MibTableColumn
setCcEnable = _SetCcEnable_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 3, 13, 2, 1, 4),
    _SetCcEnable_Type()
)
setCcEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    setCcEnable.setStatus("current")


class _SetCcDuty_Type(OctetString):
    """Custom type setCcDuty based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(20, 20),
    )
    fixed_length = 20


_SetCcDuty_Type.__name__ = "OctetString"
_SetCcDuty_Object = MibTableColumn
setCcDuty = _SetCcDuty_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 3, 13, 2, 1, 5),
    _SetCcDuty_Type()
)
setCcDuty.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    setCcDuty.setStatus("current")


class _SetCcComp_Type(OctetString):
    """Custom type setCcComp based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(20, 20),
    )
    fixed_length = 20


_SetCcComp_Type.__name__ = "OctetString"
_SetCcComp_Object = MibTableColumn
setCcComp = _SetCcComp_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 3, 13, 2, 1, 6),
    _SetCcComp_Type()
)
setCcComp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    setCcComp.setStatus("current")
_Setup422Out_ObjectIdentity = ObjectIdentity
setup422Out = _Setup422Out_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 3, 14)
)
_Set422oTable_Object = MibTable
set422oTable = _Set422oTable_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 3, 14, 2)
)
if mibBuilder.loadTexts:
    set422oTable.setStatus("current")
_Set422oEntry_Object = MibTableRow
set422oEntry = _Set422oEntry_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 3, 14, 2, 1)
)
set422oEntry.setIndexNames(
    (0, "SSU2000-MIB", "set422oChassis"),
    (0, "SSU2000-MIB", "set422oSlot"),
)
if mibBuilder.loadTexts:
    set422oEntry.setStatus("current")


class _Set422oChassis_Type(Integer32):
    """Custom type set422oChassis based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_Set422oChassis_Type.__name__ = "Integer32"
_Set422oChassis_Object = MibTableColumn
set422oChassis = _Set422oChassis_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 3, 14, 2, 1, 1),
    _Set422oChassis_Type()
)
set422oChassis.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    set422oChassis.setStatus("current")


class _Set422oSlot_Type(Integer32):
    """Custom type set422oSlot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 20),
    )


_Set422oSlot_Type.__name__ = "Integer32"
_Set422oSlot_Object = MibTableColumn
set422oSlot = _Set422oSlot_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 3, 14, 2, 1, 2),
    _Set422oSlot_Type()
)
set422oSlot.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    set422oSlot.setStatus("current")
_Set422oBypass_Type = OnValue
_Set422oBypass_Object = MibTableColumn
set422oBypass = _Set422oBypass_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 3, 14, 2, 1, 3),
    _Set422oBypass_Type()
)
set422oBypass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    set422oBypass.setStatus("current")


class _Set422oFltMode_Type(Integer32):
    """Custom type set422oFltMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2),
          ("auto", 3))
    )


_Set422oFltMode_Type.__name__ = "Integer32"
_Set422oFltMode_Object = MibTableColumn
set422oFltMode = _Set422oFltMode_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 3, 14, 2, 1, 4),
    _Set422oFltMode_Type()
)
set422oFltMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    set422oFltMode.setStatus("current")


class _Set422oEnable_Type(OctetString):
    """Custom type set422oEnable based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(20, 20),
    )
    fixed_length = 20


_Set422oEnable_Type.__name__ = "OctetString"
_Set422oEnable_Object = MibTableColumn
set422oEnable = _Set422oEnable_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 3, 14, 2, 1, 5),
    _Set422oEnable_Type()
)
set422oEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    set422oEnable.setStatus("current")


class _Set422oFrequency_Type(OctetString):
    """Custom type set422oFrequency based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(20, 20),
    )
    fixed_length = 20


_Set422oFrequency_Type.__name__ = "OctetString"
_Set422oFrequency_Object = MibTableColumn
set422oFrequency = _Set422oFrequency_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 3, 14, 2, 1, 6),
    _Set422oFrequency_Type()
)
set422oFrequency.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    set422oFrequency.setStatus("current")
_SetupE12048Out_ObjectIdentity = ObjectIdentity
setupE12048Out = _SetupE12048Out_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 3, 15)
)
_SetE12048oTable_Object = MibTable
setE12048oTable = _SetE12048oTable_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 3, 15, 2)
)
if mibBuilder.loadTexts:
    setE12048oTable.setStatus("current")
_SetE12048oEntry_Object = MibTableRow
setE12048oEntry = _SetE12048oEntry_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 3, 15, 2, 1)
)
setE12048oEntry.setIndexNames(
    (0, "SSU2000-MIB", "setE12048oChassis"),
    (0, "SSU2000-MIB", "setE12048oSlot"),
)
if mibBuilder.loadTexts:
    setE12048oEntry.setStatus("current")


class _SetE12048oChassis_Type(Integer32):
    """Custom type setE12048oChassis based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_SetE12048oChassis_Type.__name__ = "Integer32"
_SetE12048oChassis_Object = MibTableColumn
setE12048oChassis = _SetE12048oChassis_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 3, 15, 2, 1, 1),
    _SetE12048oChassis_Type()
)
setE12048oChassis.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    setE12048oChassis.setStatus("current")


class _SetE12048oSlot_Type(Integer32):
    """Custom type setE12048oSlot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 20),
    )


_SetE12048oSlot_Type.__name__ = "Integer32"
_SetE12048oSlot_Object = MibTableColumn
setE12048oSlot = _SetE12048oSlot_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 3, 15, 2, 1, 2),
    _SetE12048oSlot_Type()
)
setE12048oSlot.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    setE12048oSlot.setStatus("current")
_SetE12048oBypass_Type = OnValue
_SetE12048oBypass_Object = MibTableColumn
setE12048oBypass = _SetE12048oBypass_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 3, 15, 2, 1, 3),
    _SetE12048oBypass_Type()
)
setE12048oBypass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    setE12048oBypass.setStatus("current")
_SetE12048oZs_Type = OnValue
_SetE12048oZs_Object = MibTableColumn
setE12048oZs = _SetE12048oZs_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 3, 15, 2, 1, 4),
    _SetE12048oZs_Type()
)
setE12048oZs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    setE12048oZs.setStatus("current")


class _SetE12048oSignal_Type(OctetString):
    """Custom type setE12048oSignal based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(20, 20),
    )
    fixed_length = 20


_SetE12048oSignal_Type.__name__ = "OctetString"
_SetE12048oSignal_Object = MibTableColumn
setE12048oSignal = _SetE12048oSignal_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 3, 15, 2, 1, 5),
    _SetE12048oSignal_Type()
)
setE12048oSignal.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    setE12048oSignal.setStatus("current")


class _SetE12048oEnable_Type(OctetString):
    """Custom type setE12048oEnable based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(20, 20),
    )
    fixed_length = 20


_SetE12048oEnable_Type.__name__ = "OctetString"
_SetE12048oEnable_Object = MibTableColumn
setE12048oEnable = _SetE12048oEnable_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 3, 15, 2, 1, 6),
    _SetE12048oEnable_Type()
)
setE12048oEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    setE12048oEnable.setStatus("current")


class _SetE12048oSquelch_Type(OctetString):
    """Custom type setE12048oSquelch based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(20, 20),
    )
    fixed_length = 20


_SetE12048oSquelch_Type.__name__ = "OctetString"
_SetE12048oSquelch_Object = MibTableColumn
setE12048oSquelch = _SetE12048oSquelch_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 3, 15, 2, 1, 7),
    _SetE12048oSquelch_Type()
)
setE12048oSquelch.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    setE12048oSquelch.setStatus("current")


class _SetE12048oFrame_Type(Integer32):
    """Custom type setE12048oFrame based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ccs", 1),
          ("cas", 2))
    )


_SetE12048oFrame_Type.__name__ = "Integer32"
_SetE12048oFrame_Object = MibTableColumn
setE12048oFrame = _SetE12048oFrame_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 3, 15, 2, 1, 8),
    _SetE12048oFrame_Type()
)
setE12048oFrame.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    setE12048oFrame.setStatus("current")
_SetE12048oCrc_Type = OnValue
_SetE12048oCrc_Object = MibTableColumn
setE12048oCrc = _SetE12048oCrc_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 3, 15, 2, 1, 9),
    _SetE12048oCrc_Type()
)
setE12048oCrc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    setE12048oCrc.setStatus("current")
_SetE12048oSsm_Type = OnValue
_SetE12048oSsm_Object = MibTableColumn
setE12048oSsm = _SetE12048oSsm_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 3, 15, 2, 1, 10),
    _SetE12048oSsm_Type()
)
setE12048oSsm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    setE12048oSsm.setStatus("current")


class _SetE12048oSsmBit_Type(Integer32):
    """Custom type setE12048oSsmBit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(4, 8),
    )


_SetE12048oSsmBit_Type.__name__ = "Integer32"
_SetE12048oSsmBit_Object = MibTableColumn
setE12048oSsmBit = _SetE12048oSsmBit_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 3, 15, 2, 1, 11),
    _SetE12048oSsmBit_Type()
)
setE12048oSsmBit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    setE12048oSsmBit.setStatus("current")
_SetupLrm_ObjectIdentity = ObjectIdentity
setupLrm = _SetupLrm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 3, 16)
)
_SetLrmPTable_Object = MibTable
setLrmPTable = _SetLrmPTable_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 3, 16, 2)
)
if mibBuilder.loadTexts:
    setLrmPTable.setStatus("current")
_SetLrmPEntry_Object = MibTableRow
setLrmPEntry = _SetLrmPEntry_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 3, 16, 2, 1)
)
setLrmPEntry.setIndexNames(
    (0, "SSU2000-MIB", "setLrmPChassis"),
    (0, "SSU2000-MIB", "setLrmPSlot"),
    (0, "SSU2000-MIB", "setLrmPPort"),
)
if mibBuilder.loadTexts:
    setLrmPEntry.setStatus("current")


class _SetLrmPChassis_Type(Integer32):
    """Custom type setLrmPChassis based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_SetLrmPChassis_Type.__name__ = "Integer32"
_SetLrmPChassis_Object = MibTableColumn
setLrmPChassis = _SetLrmPChassis_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 3, 16, 2, 1, 1),
    _SetLrmPChassis_Type()
)
setLrmPChassis.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    setLrmPChassis.setStatus("current")


class _SetLrmPSlot_Type(Integer32):
    """Custom type setLrmPSlot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 20),
    )


_SetLrmPSlot_Type.__name__ = "Integer32"
_SetLrmPSlot_Object = MibTableColumn
setLrmPSlot = _SetLrmPSlot_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 3, 16, 2, 1, 2),
    _SetLrmPSlot_Type()
)
setLrmPSlot.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    setLrmPSlot.setStatus("current")


class _SetLrmPPort_Type(Integer32):
    """Custom type setLrmPPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_SetLrmPPort_Type.__name__ = "Integer32"
_SetLrmPPort_Object = MibTableColumn
setLrmPPort = _SetLrmPPort_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 3, 16, 2, 1, 3),
    _SetLrmPPort_Type()
)
setLrmPPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    setLrmPPort.setStatus("current")
_SetLrmPEnable_Type = OnValue
_SetLrmPEnable_Object = MibTableColumn
setLrmPEnable = _SetLrmPEnable_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 3, 16, 2, 1, 4),
    _SetLrmPEnable_Type()
)
setLrmPEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    setLrmPEnable.setStatus("current")


class _SetLrmPLbo_Type(Integer32):
    """Custom type setLrmPLbo based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("lbo133ft", 1),
          ("lbo266ft", 2),
          ("lbo399ft", 3),
          ("lbo533ft", 4),
          ("lbo655ft", 5))
    )


_SetLrmPLbo_Type.__name__ = "Integer32"
_SetLrmPLbo_Object = MibTableColumn
setLrmPLbo = _SetLrmPLbo_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 3, 16, 2, 1, 5),
    _SetLrmPLbo_Type()
)
setLrmPLbo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    setLrmPLbo.setStatus("current")


class _SetLrmPSlip_Type(Integer32):
    """Custom type setLrmPSlip based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_SetLrmPSlip_Type.__name__ = "Integer32"
_SetLrmPSlip_Object = MibTableColumn
setLrmPSlip = _SetLrmPSlip_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 3, 16, 2, 1, 6),
    _SetLrmPSlip_Type()
)
setLrmPSlip.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    setLrmPSlip.setStatus("current")


class _SetLrmPBpv_Type(Integer32):
    """Custom type setLrmPBpv based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("clr", 1),
          ("nop", 2))
    )


_SetLrmPBpv_Type.__name__ = "Integer32"
_SetLrmPBpv_Object = MibTableColumn
setLrmPBpv = _SetLrmPBpv_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 3, 16, 2, 1, 7),
    _SetLrmPBpv_Type()
)
setLrmPBpv.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    setLrmPBpv.setStatus("current")


class _SetLrmPFlt_Type(Integer32):
    """Custom type setLrmPFlt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("squelch", 1),
          ("ais", 2))
    )


_SetLrmPFlt_Type.__name__ = "Integer32"
_SetLrmPFlt_Object = MibTableColumn
setLrmPFlt = _SetLrmPFlt_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 3, 16, 2, 1, 8),
    _SetLrmPFlt_Type()
)
setLrmPFlt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    setLrmPFlt.setStatus("current")


class _SetLrmPCid_Type(DisplayString):
    """Custom type setLrmPCid based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 43),
    )


_SetLrmPCid_Type.__name__ = "DisplayString"
_SetLrmPCid_Object = MibTableColumn
setLrmPCid = _SetLrmPCid_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 3, 16, 2, 1, 9),
    _SetLrmPCid_Type()
)
setLrmPCid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    setLrmPCid.setStatus("current")
_SetupSineOut_ObjectIdentity = ObjectIdentity
setupSineOut = _SetupSineOut_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 3, 17)
)
_SetSineoTable_Object = MibTable
setSineoTable = _SetSineoTable_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 3, 17, 2)
)
if mibBuilder.loadTexts:
    setSineoTable.setStatus("current")
_SetSineoEntry_Object = MibTableRow
setSineoEntry = _SetSineoEntry_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 3, 17, 2, 1)
)
setSineoEntry.setIndexNames(
    (0, "SSU2000-MIB", "setSineoChassis"),
    (0, "SSU2000-MIB", "setSineoSlot"),
)
if mibBuilder.loadTexts:
    setSineoEntry.setStatus("current")


class _SetSineoChassis_Type(Integer32):
    """Custom type setSineoChassis based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_SetSineoChassis_Type.__name__ = "Integer32"
_SetSineoChassis_Object = MibTableColumn
setSineoChassis = _SetSineoChassis_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 3, 17, 2, 1, 1),
    _SetSineoChassis_Type()
)
setSineoChassis.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    setSineoChassis.setStatus("current")


class _SetSineoSlot_Type(Integer32):
    """Custom type setSineoSlot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 20),
    )


_SetSineoSlot_Type.__name__ = "Integer32"
_SetSineoSlot_Object = MibTableColumn
setSineoSlot = _SetSineoSlot_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 3, 17, 2, 1, 2),
    _SetSineoSlot_Type()
)
setSineoSlot.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    setSineoSlot.setStatus("current")
_SetSineoBypass_Type = OnValue
_SetSineoBypass_Object = MibTableColumn
setSineoBypass = _SetSineoBypass_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 3, 17, 2, 1, 3),
    _SetSineoBypass_Type()
)
setSineoBypass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    setSineoBypass.setStatus("current")


class _SetSineoFrequency_Type(Integer32):
    """Custom type setSineoFrequency based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1544, 1544),
        ValueRangeConstraint(6312, 6312),
    )


_SetSineoFrequency_Type.__name__ = "Integer32"
_SetSineoFrequency_Object = MibTableColumn
setSineoFrequency = _SetSineoFrequency_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 3, 17, 2, 1, 4),
    _SetSineoFrequency_Type()
)
setSineoFrequency.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    setSineoFrequency.setStatus("current")


class _SetSineoEnable_Type(OctetString):
    """Custom type setSineoEnable based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(20, 20),
    )
    fixed_length = 20


_SetSineoEnable_Type.__name__ = "OctetString"
_SetSineoEnable_Object = MibTableColumn
setSineoEnable = _SetSineoEnable_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 3, 17, 2, 1, 5),
    _SetSineoEnable_Type()
)
setSineoEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    setSineoEnable.setStatus("current")


class _SetSineoSquelch_Type(OctetString):
    """Custom type setSineoSquelch based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(20, 20),
    )
    fixed_length = 20


_SetSineoSquelch_Type.__name__ = "OctetString"
_SetSineoSquelch_Object = MibTableColumn
setSineoSquelch = _SetSineoSquelch_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 3, 17, 2, 1, 6),
    _SetSineoSquelch_Type()
)
setSineoSquelch.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    setSineoSquelch.setStatus("current")
_SetupSineInp_ObjectIdentity = ObjectIdentity
setupSineInp = _SetupSineInp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 3, 18)
)
_SetSineInpTable_Object = MibTable
setSineInpTable = _SetSineInpTable_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 3, 18, 2)
)
if mibBuilder.loadTexts:
    setSineInpTable.setStatus("current")
_SetSineiEntry_Object = MibTableRow
setSineiEntry = _SetSineiEntry_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 3, 18, 2, 1)
)
setSineiEntry.setIndexNames(
    (0, "SSU2000-MIB", "setSineiChassis"),
    (0, "SSU2000-MIB", "setSineiSlot"),
    (0, "SSU2000-MIB", "setSineiPort"),
)
if mibBuilder.loadTexts:
    setSineiEntry.setStatus("current")


class _SetSineiChassis_Type(Integer32):
    """Custom type setSineiChassis based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
    )


_SetSineiChassis_Type.__name__ = "Integer32"
_SetSineiChassis_Object = MibTableColumn
setSineiChassis = _SetSineiChassis_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 3, 18, 2, 1, 1),
    _SetSineiChassis_Type()
)
setSineiChassis.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    setSineiChassis.setStatus("current")


class _SetSineiSlot_Type(Integer32):
    """Custom type setSineiSlot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 20),
    )


_SetSineiSlot_Type.__name__ = "Integer32"
_SetSineiSlot_Object = MibTableColumn
setSineiSlot = _SetSineiSlot_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 3, 18, 2, 1, 2),
    _SetSineiSlot_Type()
)
setSineiSlot.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    setSineiSlot.setStatus("current")


class _SetSineiPort_Type(Integer32):
    """Custom type setSineiPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_SetSineiPort_Type.__name__ = "Integer32"
_SetSineiPort_Object = MibTableColumn
setSineiPort = _SetSineiPort_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 3, 18, 2, 1, 3),
    _SetSineiPort_Type()
)
setSineiPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    setSineiPort.setStatus("current")
_SetSineiEnable_Type = EnaValue
_SetSineiEnable_Object = MibTableColumn
setSineiEnable = _SetSineiEnable_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 3, 18, 2, 1, 4),
    _SetSineiEnable_Type()
)
setSineiEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    setSineiEnable.setStatus("current")


class _SetSineiFrequency_Type(Integer32):
    """Custom type setSineiFrequency based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1544, 1544),
        ValueRangeConstraint(6312, 6312),
    )


_SetSineiFrequency_Type.__name__ = "Integer32"
_SetSineiFrequency_Object = MibTableColumn
setSineiFrequency = _SetSineiFrequency_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 3, 18, 2, 1, 5),
    _SetSineiFrequency_Type()
)
setSineiFrequency.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    setSineiFrequency.setStatus("current")


class _SetSineiProvPql_Type(Integer32):
    """Custom type setSineiProvPql based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 9),
    )


_SetSineiProvPql_Type.__name__ = "Integer32"
_SetSineiProvPql_Object = MibTableColumn
setSineiProvPql = _SetSineiProvPql_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 3, 18, 2, 1, 6),
    _SetSineiProvPql_Type()
)
setSineiProvPql.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    setSineiProvPql.setStatus("current")


class _SetSineiPriority_Type(Integer32):
    """Custom type setSineiPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10),
    )


_SetSineiPriority_Type.__name__ = "Integer32"
_SetSineiPriority_Object = MibTableColumn
setSineiPriority = _SetSineiPriority_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 3, 18, 2, 1, 7),
    _SetSineiPriority_Type()
)
setSineiPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    setSineiPriority.setStatus("current")


class _SetSineiCSFlt_Type(Integer32):
    """Custom type setSineiCSFlt based on Integer32"""
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
        *(("off", 1),
          ("low", 2),
          ("high", 3),
          ("na", 4))
    )


_SetSineiCSFlt_Type.__name__ = "Integer32"
_SetSineiCSFlt_Object = MibTableColumn
setSineiCSFlt = _SetSineiCSFlt_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 3, 18, 2, 1, 8),
    _SetSineiCSFlt_Type()
)
setSineiCSFlt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    setSineiCSFlt.setStatus("current")


class _SetSineiZeroPhase_Type(Integer32):
    """Custom type setSineiZeroPhase based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("zeroPhA", 1),
          ("zeroPhB", 2),
          ("zeroPhAB", 3))
    )


_SetSineiZeroPhase_Type.__name__ = "Integer32"
_SetSineiZeroPhase_Object = MibTableColumn
setSineiZeroPhase = _SetSineiZeroPhase_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 3, 18, 2, 1, 9),
    _SetSineiZeroPhase_Type()
)
setSineiZeroPhase.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    setSineiZeroPhase.setStatus("current")
_SetAlmThSineInpTable_Object = MibTable
setAlmThSineInpTable = _SetAlmThSineInpTable_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 3, 18, 4)
)
if mibBuilder.loadTexts:
    setAlmThSineInpTable.setStatus("current")
_SetMsiEntry_Object = MibTableRow
setMsiEntry = _SetMsiEntry_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 3, 18, 4, 1)
)
setMsiEntry.setIndexNames(
    (0, "SSU2000-MIB", "setMsiChassis"),
    (0, "SSU2000-MIB", "setMsiSlot"),
    (0, "SSU2000-MIB", "setMsiPort"),
)
if mibBuilder.loadTexts:
    setMsiEntry.setStatus("current")


class _SetMsiChassis_Type(Integer32):
    """Custom type setMsiChassis based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
    )


_SetMsiChassis_Type.__name__ = "Integer32"
_SetMsiChassis_Object = MibTableColumn
setMsiChassis = _SetMsiChassis_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 3, 18, 4, 1, 1),
    _SetMsiChassis_Type()
)
setMsiChassis.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    setMsiChassis.setStatus("current")


class _SetMsiSlot_Type(Integer32):
    """Custom type setMsiSlot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 20),
    )


_SetMsiSlot_Type.__name__ = "Integer32"
_SetMsiSlot_Object = MibTableColumn
setMsiSlot = _SetMsiSlot_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 3, 18, 4, 1, 2),
    _SetMsiSlot_Type()
)
setMsiSlot.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    setMsiSlot.setStatus("current")


class _SetMsiPort_Type(Integer32):
    """Custom type setMsiPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_SetMsiPort_Type.__name__ = "Integer32"
_SetMsiPort_Object = MibTableColumn
setMsiPort = _SetMsiPort_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 3, 18, 4, 1, 3),
    _SetMsiPort_Type()
)
setMsiPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    setMsiPort.setStatus("current")


class _SetMsiMtieStd_Type(Integer32):
    """Custom type setMsiMtieStd based on Integer32"""
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
        *(("prs", 1),
          ("ds1", 2),
          ("g811", 3),
          ("g823", 4))
    )


_SetMsiMtieStd_Type.__name__ = "Integer32"
_SetMsiMtieStd_Object = MibTableColumn
setMsiMtieStd = _SetMsiMtieStd_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 3, 18, 4, 1, 4),
    _SetMsiMtieStd_Type()
)
setMsiMtieStd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    setMsiMtieStd.setStatus("current")


class _SetMsiMtie10EL1_Type(Integer32):
    """Custom type setMsiMtie10EL1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 60000),
    )


_SetMsiMtie10EL1_Type.__name__ = "Integer32"
_SetMsiMtie10EL1_Object = MibTableColumn
setMsiMtie10EL1 = _SetMsiMtie10EL1_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 3, 18, 4, 1, 5),
    _SetMsiMtie10EL1_Type()
)
setMsiMtie10EL1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    setMsiMtie10EL1.setStatus("current")


class _SetMsiMtie10EL2_Type(Integer32):
    """Custom type setMsiMtie10EL2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 60000),
    )


_SetMsiMtie10EL2_Type.__name__ = "Integer32"
_SetMsiMtie10EL2_Object = MibTableColumn
setMsiMtie10EL2 = _SetMsiMtie10EL2_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 3, 18, 4, 1, 6),
    _SetMsiMtie10EL2_Type()
)
setMsiMtie10EL2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    setMsiMtie10EL2.setStatus("current")


class _SetMsiMtie10CL1_Type(Integer32):
    """Custom type setMsiMtie10CL1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 60000),
    )


_SetMsiMtie10CL1_Type.__name__ = "Integer32"
_SetMsiMtie10CL1_Object = MibTableColumn
setMsiMtie10CL1 = _SetMsiMtie10CL1_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 3, 18, 4, 1, 7),
    _SetMsiMtie10CL1_Type()
)
setMsiMtie10CL1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    setMsiMtie10CL1.setStatus("current")


class _SetMsiMtie10CL2_Type(Integer32):
    """Custom type setMsiMtie10CL2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 60000),
    )


_SetMsiMtie10CL2_Type.__name__ = "Integer32"
_SetMsiMtie10CL2_Object = MibTableColumn
setMsiMtie10CL2 = _SetMsiMtie10CL2_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 3, 18, 4, 1, 8),
    _SetMsiMtie10CL2_Type()
)
setMsiMtie10CL2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    setMsiMtie10CL2.setStatus("current")


class _SetMsiMtie100EL1_Type(Integer32):
    """Custom type setMsiMtie100EL1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 60000),
    )


_SetMsiMtie100EL1_Type.__name__ = "Integer32"
_SetMsiMtie100EL1_Object = MibTableColumn
setMsiMtie100EL1 = _SetMsiMtie100EL1_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 3, 18, 4, 1, 9),
    _SetMsiMtie100EL1_Type()
)
setMsiMtie100EL1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    setMsiMtie100EL1.setStatus("current")


class _SetMsiMtie100EL2_Type(Integer32):
    """Custom type setMsiMtie100EL2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 60000),
    )


_SetMsiMtie100EL2_Type.__name__ = "Integer32"
_SetMsiMtie100EL2_Object = MibTableColumn
setMsiMtie100EL2 = _SetMsiMtie100EL2_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 3, 18, 4, 1, 10),
    _SetMsiMtie100EL2_Type()
)
setMsiMtie100EL2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    setMsiMtie100EL2.setStatus("current")


class _SetMsiMtie100CL1_Type(Integer32):
    """Custom type setMsiMtie100CL1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 60000),
    )


_SetMsiMtie100CL1_Type.__name__ = "Integer32"
_SetMsiMtie100CL1_Object = MibTableColumn
setMsiMtie100CL1 = _SetMsiMtie100CL1_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 3, 18, 4, 1, 11),
    _SetMsiMtie100CL1_Type()
)
setMsiMtie100CL1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    setMsiMtie100CL1.setStatus("current")


class _SetMsiMtie100CL2_Type(Integer32):
    """Custom type setMsiMtie100CL2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 60000),
    )


_SetMsiMtie100CL2_Type.__name__ = "Integer32"
_SetMsiMtie100CL2_Object = MibTableColumn
setMsiMtie100CL2 = _SetMsiMtie100CL2_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 3, 18, 4, 1, 12),
    _SetMsiMtie100CL2_Type()
)
setMsiMtie100CL2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    setMsiMtie100CL2.setStatus("current")


class _SetMsiMtie1000EL1_Type(Integer32):
    """Custom type setMsiMtie1000EL1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 60000),
    )


_SetMsiMtie1000EL1_Type.__name__ = "Integer32"
_SetMsiMtie1000EL1_Object = MibTableColumn
setMsiMtie1000EL1 = _SetMsiMtie1000EL1_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 3, 18, 4, 1, 13),
    _SetMsiMtie1000EL1_Type()
)
setMsiMtie1000EL1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    setMsiMtie1000EL1.setStatus("current")


class _SetMsiMtie1000EL2_Type(Integer32):
    """Custom type setMsiMtie1000EL2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 60000),
    )


_SetMsiMtie1000EL2_Type.__name__ = "Integer32"
_SetMsiMtie1000EL2_Object = MibTableColumn
setMsiMtie1000EL2 = _SetMsiMtie1000EL2_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 3, 18, 4, 1, 14),
    _SetMsiMtie1000EL2_Type()
)
setMsiMtie1000EL2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    setMsiMtie1000EL2.setStatus("current")


class _SetMsiMtie1000CL1_Type(Integer32):
    """Custom type setMsiMtie1000CL1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 60000),
    )


_SetMsiMtie1000CL1_Type.__name__ = "Integer32"
_SetMsiMtie1000CL1_Object = MibTableColumn
setMsiMtie1000CL1 = _SetMsiMtie1000CL1_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 3, 18, 4, 1, 15),
    _SetMsiMtie1000CL1_Type()
)
setMsiMtie1000CL1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    setMsiMtie1000CL1.setStatus("current")


class _SetMsiMtie1000CL2_Type(Integer32):
    """Custom type setMsiMtie1000CL2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 60000),
    )


_SetMsiMtie1000CL2_Type.__name__ = "Integer32"
_SetMsiMtie1000CL2_Object = MibTableColumn
setMsiMtie1000CL2 = _SetMsiMtie1000CL2_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 3, 18, 4, 1, 16),
    _SetMsiMtie1000CL2_Type()
)
setMsiMtie1000CL2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    setMsiMtie1000CL2.setStatus("current")


class _SetMsiMtie10000EL1_Type(Integer32):
    """Custom type setMsiMtie10000EL1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 60000),
    )


_SetMsiMtie10000EL1_Type.__name__ = "Integer32"
_SetMsiMtie10000EL1_Object = MibTableColumn
setMsiMtie10000EL1 = _SetMsiMtie10000EL1_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 3, 18, 4, 1, 17),
    _SetMsiMtie10000EL1_Type()
)
setMsiMtie10000EL1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    setMsiMtie10000EL1.setStatus("current")


class _SetMsiMtie10000EL2_Type(Integer32):
    """Custom type setMsiMtie10000EL2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 60000),
    )


_SetMsiMtie10000EL2_Type.__name__ = "Integer32"
_SetMsiMtie10000EL2_Object = MibTableColumn
setMsiMtie10000EL2 = _SetMsiMtie10000EL2_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 3, 18, 4, 1, 18),
    _SetMsiMtie10000EL2_Type()
)
setMsiMtie10000EL2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    setMsiMtie10000EL2.setStatus("current")


class _SetMsiMtie10000CL1_Type(Integer32):
    """Custom type setMsiMtie10000CL1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 60000),
    )


_SetMsiMtie10000CL1_Type.__name__ = "Integer32"
_SetMsiMtie10000CL1_Object = MibTableColumn
setMsiMtie10000CL1 = _SetMsiMtie10000CL1_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 3, 18, 4, 1, 19),
    _SetMsiMtie10000CL1_Type()
)
setMsiMtie10000CL1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    setMsiMtie10000CL1.setStatus("current")


class _SetMsiMtie10000CL2_Type(Integer32):
    """Custom type setMsiMtie10000CL2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 60000),
    )


_SetMsiMtie10000CL2_Type.__name__ = "Integer32"
_SetMsiMtie10000CL2_Object = MibTableColumn
setMsiMtie10000CL2 = _SetMsiMtie10000CL2_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 3, 18, 4, 1, 20),
    _SetMsiMtie10000CL2_Type()
)
setMsiMtie10000CL2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    setMsiMtie10000CL2.setStatus("current")


class _SetMsiMtie100000EL1_Type(Integer32):
    """Custom type setMsiMtie100000EL1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 60000),
    )


_SetMsiMtie100000EL1_Type.__name__ = "Integer32"
_SetMsiMtie100000EL1_Object = MibTableColumn
setMsiMtie100000EL1 = _SetMsiMtie100000EL1_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 3, 18, 4, 1, 21),
    _SetMsiMtie100000EL1_Type()
)
setMsiMtie100000EL1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    setMsiMtie100000EL1.setStatus("current")


class _SetMsiMtie100000EL2_Type(Integer32):
    """Custom type setMsiMtie100000EL2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 60000),
    )


_SetMsiMtie100000EL2_Type.__name__ = "Integer32"
_SetMsiMtie100000EL2_Object = MibTableColumn
setMsiMtie100000EL2 = _SetMsiMtie100000EL2_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 3, 18, 4, 1, 22),
    _SetMsiMtie100000EL2_Type()
)
setMsiMtie100000EL2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    setMsiMtie100000EL2.setStatus("current")


class _SetMsiMtie100000CL1_Type(Integer32):
    """Custom type setMsiMtie100000CL1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 60000),
    )


_SetMsiMtie100000CL1_Type.__name__ = "Integer32"
_SetMsiMtie100000CL1_Object = MibTableColumn
setMsiMtie100000CL1 = _SetMsiMtie100000CL1_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 3, 18, 4, 1, 23),
    _SetMsiMtie100000CL1_Type()
)
setMsiMtie100000CL1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    setMsiMtie100000CL1.setStatus("current")


class _SetMsiMtie100000CL2_Type(Integer32):
    """Custom type setMsiMtie100000CL2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 60000),
    )


_SetMsiMtie100000CL2_Type.__name__ = "Integer32"
_SetMsiMtie100000CL2_Object = MibTableColumn
setMsiMtie100000CL2 = _SetMsiMtie100000CL2_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 3, 18, 4, 1, 24),
    _SetMsiMtie100000CL2_Type()
)
setMsiMtie100000CL2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    setMsiMtie100000CL2.setStatus("current")


class _SetMsiFreqAErrLmt_Type(Integer32):
    """Custom type setMsiFreqAErrLmt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000000),
    )


_SetMsiFreqAErrLmt_Type.__name__ = "Integer32"
_SetMsiFreqAErrLmt_Object = MibTableColumn
setMsiFreqAErrLmt = _SetMsiFreqAErrLmt_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 3, 18, 4, 1, 25),
    _SetMsiFreqAErrLmt_Type()
)
setMsiFreqAErrLmt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    setMsiFreqAErrLmt.setStatus("current")


class _SetMsiFreqAClrLmt_Type(Integer32):
    """Custom type setMsiFreqAClrLmt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000000),
    )


_SetMsiFreqAClrLmt_Type.__name__ = "Integer32"
_SetMsiFreqAClrLmt_Object = MibTableColumn
setMsiFreqAClrLmt = _SetMsiFreqAClrLmt_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 3, 18, 4, 1, 26),
    _SetMsiFreqAClrLmt_Type()
)
setMsiFreqAClrLmt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    setMsiFreqAClrLmt.setStatus("current")


class _SetMsiFreqATau_Type(Integer32):
    """Custom type setMsiFreqATau based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 1000),
    )


_SetMsiFreqATau_Type.__name__ = "Integer32"
_SetMsiFreqATau_Object = MibTableColumn
setMsiFreqATau = _SetMsiFreqATau_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 3, 18, 4, 1, 27),
    _SetMsiFreqATau_Type()
)
setMsiFreqATau.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    setMsiFreqATau.setStatus("current")


class _SetMsiFreqBErrLmt_Type(Integer32):
    """Custom type setMsiFreqBErrLmt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000000),
    )


_SetMsiFreqBErrLmt_Type.__name__ = "Integer32"
_SetMsiFreqBErrLmt_Object = MibTableColumn
setMsiFreqBErrLmt = _SetMsiFreqBErrLmt_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 3, 18, 4, 1, 28),
    _SetMsiFreqBErrLmt_Type()
)
setMsiFreqBErrLmt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    setMsiFreqBErrLmt.setStatus("current")


class _SetMsiFreqBClrLmt_Type(Integer32):
    """Custom type setMsiFreqBClrLmt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000000),
    )


_SetMsiFreqBClrLmt_Type.__name__ = "Integer32"
_SetMsiFreqBClrLmt_Object = MibTableColumn
setMsiFreqBClrLmt = _SetMsiFreqBClrLmt_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 3, 18, 4, 1, 29),
    _SetMsiFreqBClrLmt_Type()
)
setMsiFreqBClrLmt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    setMsiFreqBClrLmt.setStatus("current")


class _SetMsiFreqBTau_Type(Integer32):
    """Custom type setMsiFreqBTau based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 1000),
    )


_SetMsiFreqBTau_Type.__name__ = "Integer32"
_SetMsiFreqBTau_Object = MibTableColumn
setMsiFreqBTau = _SetMsiFreqBTau_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 3, 18, 4, 1, 30),
    _SetMsiFreqBTau_Type()
)
setMsiFreqBTau.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    setMsiFreqBTau.setStatus("current")
_SetupJccOut_ObjectIdentity = ObjectIdentity
setupJccOut = _SetupJccOut_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 3, 19)
)
_SetJccoTable_Object = MibTable
setJccoTable = _SetJccoTable_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 3, 19, 2)
)
if mibBuilder.loadTexts:
    setJccoTable.setStatus("current")
_SetJccoEntry_Object = MibTableRow
setJccoEntry = _SetJccoEntry_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 3, 19, 2, 1)
)
setJccoEntry.setIndexNames(
    (0, "SSU2000-MIB", "setJccoChassis"),
    (0, "SSU2000-MIB", "setJccoSlot"),
)
if mibBuilder.loadTexts:
    setJccoEntry.setStatus("current")


class _SetJccoChassis_Type(Integer32):
    """Custom type setJccoChassis based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_SetJccoChassis_Type.__name__ = "Integer32"
_SetJccoChassis_Object = MibTableColumn
setJccoChassis = _SetJccoChassis_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 3, 19, 2, 1, 1),
    _SetJccoChassis_Type()
)
setJccoChassis.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    setJccoChassis.setStatus("current")


class _SetJccoSlot_Type(Integer32):
    """Custom type setJccoSlot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 20),
    )


_SetJccoSlot_Type.__name__ = "Integer32"
_SetJccoSlot_Object = MibTableColumn
setJccoSlot = _SetJccoSlot_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 3, 19, 2, 1, 2),
    _SetJccoSlot_Type()
)
setJccoSlot.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    setJccoSlot.setStatus("current")
_SetJccoBypass_Type = OnValue
_SetJccoBypass_Object = MibTableColumn
setJccoBypass = _SetJccoBypass_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 3, 19, 2, 1, 3),
    _SetJccoBypass_Type()
)
setJccoBypass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    setJccoBypass.setStatus("current")
_SetJcco400Hz_Type = OnValue
_SetJcco400Hz_Object = MibTableColumn
setJcco400Hz = _SetJcco400Hz_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 3, 19, 2, 1, 4),
    _SetJcco400Hz_Type()
)
setJcco400Hz.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    setJcco400Hz.setStatus("current")


class _SetJccoEnable_Type(OctetString):
    """Custom type setJccoEnable based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(20, 20),
    )
    fixed_length = 20


_SetJccoEnable_Type.__name__ = "OctetString"
_SetJccoEnable_Object = MibTableColumn
setJccoEnable = _SetJccoEnable_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 3, 19, 2, 1, 5),
    _SetJccoEnable_Type()
)
setJccoEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    setJccoEnable.setStatus("current")


class _SetJccoComp_Type(OctetString):
    """Custom type setJccoComp based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(20, 20),
    )
    fixed_length = 20


_SetJccoComp_Type.__name__ = "OctetString"
_SetJccoComp_Object = MibTableColumn
setJccoComp = _SetJccoComp_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 3, 19, 2, 1, 6),
    _SetJccoComp_Type()
)
setJccoComp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    setJccoComp.setStatus("current")
_SetupJccInp_ObjectIdentity = ObjectIdentity
setupJccInp = _SetupJccInp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 3, 20)
)
_SetJccInpTable_Object = MibTable
setJccInpTable = _SetJccInpTable_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 3, 20, 2)
)
if mibBuilder.loadTexts:
    setJccInpTable.setStatus("current")
_SetJcciEntry_Object = MibTableRow
setJcciEntry = _SetJcciEntry_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 3, 20, 2, 1)
)
setJcciEntry.setIndexNames(
    (0, "SSU2000-MIB", "setJcciChassis"),
    (0, "SSU2000-MIB", "setJcciSlot"),
    (0, "SSU2000-MIB", "setJcciPort"),
)
if mibBuilder.loadTexts:
    setJcciEntry.setStatus("current")


class _SetJcciChassis_Type(Integer32):
    """Custom type setJcciChassis based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
    )


_SetJcciChassis_Type.__name__ = "Integer32"
_SetJcciChassis_Object = MibTableColumn
setJcciChassis = _SetJcciChassis_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 3, 20, 2, 1, 1),
    _SetJcciChassis_Type()
)
setJcciChassis.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    setJcciChassis.setStatus("current")


class _SetJcciSlot_Type(Integer32):
    """Custom type setJcciSlot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 20),
    )


_SetJcciSlot_Type.__name__ = "Integer32"
_SetJcciSlot_Object = MibTableColumn
setJcciSlot = _SetJcciSlot_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 3, 20, 2, 1, 2),
    _SetJcciSlot_Type()
)
setJcciSlot.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    setJcciSlot.setStatus("current")


class _SetJcciPort_Type(Integer32):
    """Custom type setJcciPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_SetJcciPort_Type.__name__ = "Integer32"
_SetJcciPort_Object = MibTableColumn
setJcciPort = _SetJcciPort_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 3, 20, 2, 1, 3),
    _SetJcciPort_Type()
)
setJcciPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    setJcciPort.setStatus("current")
_SetJcciEnable_Type = EnaValue
_SetJcciEnable_Object = MibTableColumn
setJcciEnable = _SetJcciEnable_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 3, 20, 2, 1, 4),
    _SetJcciEnable_Type()
)
setJcciEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    setJcciEnable.setStatus("current")


class _SetJcciProvPql_Type(Integer32):
    """Custom type setJcciProvPql based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 9),
    )


_SetJcciProvPql_Type.__name__ = "Integer32"
_SetJcciProvPql_Object = MibTableColumn
setJcciProvPql = _SetJcciProvPql_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 3, 20, 2, 1, 5),
    _SetJcciProvPql_Type()
)
setJcciProvPql.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    setJcciProvPql.setStatus("current")


class _SetJcciPriority_Type(Integer32):
    """Custom type setJcciPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10),
    )


_SetJcciPriority_Type.__name__ = "Integer32"
_SetJcciPriority_Object = MibTableColumn
setJcciPriority = _SetJcciPriority_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 3, 20, 2, 1, 6),
    _SetJcciPriority_Type()
)
setJcciPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    setJcciPriority.setStatus("current")
_SetJcci400Hz_Type = OnValue
_SetJcci400Hz_Object = MibTableColumn
setJcci400Hz = _SetJcci400Hz_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 3, 20, 2, 1, 7),
    _SetJcci400Hz_Type()
)
setJcci400Hz.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    setJcci400Hz.setStatus("current")


class _SetJcciZeroPhase_Type(Integer32):
    """Custom type setJcciZeroPhase based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("zeroPhA", 1),
          ("zeroPhB", 2),
          ("zeroPhAB", 3))
    )


_SetJcciZeroPhase_Type.__name__ = "Integer32"
_SetJcciZeroPhase_Object = MibTableColumn
setJcciZeroPhase = _SetJcciZeroPhase_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 3, 20, 2, 1, 8),
    _SetJcciZeroPhase_Type()
)
setJcciZeroPhase.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    setJcciZeroPhase.setStatus("current")
_SetupLrmE1_ObjectIdentity = ObjectIdentity
setupLrmE1 = _SetupLrmE1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 3, 21)
)
_SetLrme1PTable_Object = MibTable
setLrme1PTable = _SetLrme1PTable_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 3, 21, 2)
)
if mibBuilder.loadTexts:
    setLrme1PTable.setStatus("current")
_SetLrme1PEntry_Object = MibTableRow
setLrme1PEntry = _SetLrme1PEntry_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 3, 21, 2, 1)
)
setLrme1PEntry.setIndexNames(
    (0, "SSU2000-MIB", "setLrme1PChassis"),
    (0, "SSU2000-MIB", "setLrme1PSlot"),
    (0, "SSU2000-MIB", "setLrme1PPort"),
)
if mibBuilder.loadTexts:
    setLrme1PEntry.setStatus("current")


class _SetLrme1PChassis_Type(Integer32):
    """Custom type setLrme1PChassis based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_SetLrme1PChassis_Type.__name__ = "Integer32"
_SetLrme1PChassis_Object = MibTableColumn
setLrme1PChassis = _SetLrme1PChassis_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 3, 21, 2, 1, 1),
    _SetLrme1PChassis_Type()
)
setLrme1PChassis.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    setLrme1PChassis.setStatus("current")


class _SetLrme1PSlot_Type(Integer32):
    """Custom type setLrme1PSlot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 20),
    )


_SetLrme1PSlot_Type.__name__ = "Integer32"
_SetLrme1PSlot_Object = MibTableColumn
setLrme1PSlot = _SetLrme1PSlot_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 3, 21, 2, 1, 2),
    _SetLrme1PSlot_Type()
)
setLrme1PSlot.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    setLrme1PSlot.setStatus("current")


class _SetLrme1PPort_Type(Integer32):
    """Custom type setLrme1PPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_SetLrme1PPort_Type.__name__ = "Integer32"
_SetLrme1PPort_Object = MibTableColumn
setLrme1PPort = _SetLrme1PPort_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 3, 21, 2, 1, 3),
    _SetLrme1PPort_Type()
)
setLrme1PPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    setLrme1PPort.setStatus("current")
_SetLrme1PEnable_Type = OnValue
_SetLrme1PEnable_Object = MibTableColumn
setLrme1PEnable = _SetLrme1PEnable_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 3, 21, 2, 1, 4),
    _SetLrme1PEnable_Type()
)
setLrme1PEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    setLrme1PEnable.setStatus("current")


class _SetLrme1PSlip_Type(Integer32):
    """Custom type setLrme1PSlip based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_SetLrme1PSlip_Type.__name__ = "Integer32"
_SetLrme1PSlip_Object = MibTableColumn
setLrme1PSlip = _SetLrme1PSlip_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 3, 21, 2, 1, 5),
    _SetLrme1PSlip_Type()
)
setLrme1PSlip.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    setLrme1PSlip.setStatus("current")


class _SetLrme1PBpv_Type(Integer32):
    """Custom type setLrme1PBpv based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("clr", 1),
          ("nop", 2))
    )


_SetLrme1PBpv_Type.__name__ = "Integer32"
_SetLrme1PBpv_Object = MibTableColumn
setLrme1PBpv = _SetLrme1PBpv_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 3, 21, 2, 1, 6),
    _SetLrme1PBpv_Type()
)
setLrme1PBpv.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    setLrme1PBpv.setStatus("current")


class _SetLrme1PFlt_Type(Integer32):
    """Custom type setLrme1PFlt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("squelch", 1),
          ("ais", 2))
    )


_SetLrme1PFlt_Type.__name__ = "Integer32"
_SetLrme1PFlt_Object = MibTableColumn
setLrme1PFlt = _SetLrme1PFlt_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 3, 21, 2, 1, 7),
    _SetLrme1PFlt_Type()
)
setLrme1PFlt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    setLrme1PFlt.setStatus("current")


class _SetLrme1PCid_Type(DisplayString):
    """Custom type setLrme1PCid based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 43),
    )


_SetLrme1PCid_Type.__name__ = "DisplayString"
_SetLrme1PCid_Object = MibTableColumn
setLrme1PCid = _SetLrme1PCid_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 3, 21, 2, 1, 8),
    _SetLrme1PCid_Type()
)
setLrme1PCid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    setLrme1PCid.setStatus("current")
_SetupPtNtp_ObjectIdentity = ObjectIdentity
setupPtNtp = _SetupPtNtp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 3, 22)
)
_SetPtNtpTable_Object = MibTable
setPtNtpTable = _SetPtNtpTable_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 3, 22, 1)
)
if mibBuilder.loadTexts:
    setPtNtpTable.setStatus("current")
_SetPtNtpEntry_Object = MibTableRow
setPtNtpEntry = _SetPtNtpEntry_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 3, 22, 1, 1)
)
setPtNtpEntry.setIndexNames(
    (0, "SSU2000-MIB", "setPtNtpChassis"),
    (0, "SSU2000-MIB", "setPtNtpSlot"),
)
if mibBuilder.loadTexts:
    setPtNtpEntry.setStatus("current")


class _SetPtNtpChassis_Type(Integer32):
    """Custom type setPtNtpChassis based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_SetPtNtpChassis_Type.__name__ = "Integer32"
_SetPtNtpChassis_Object = MibTableColumn
setPtNtpChassis = _SetPtNtpChassis_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 3, 22, 1, 1, 1),
    _SetPtNtpChassis_Type()
)
setPtNtpChassis.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    setPtNtpChassis.setStatus("current")


class _SetPtNtpSlot_Type(Integer32):
    """Custom type setPtNtpSlot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 20),
    )


_SetPtNtpSlot_Type.__name__ = "Integer32"
_SetPtNtpSlot_Object = MibTableColumn
setPtNtpSlot = _SetPtNtpSlot_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 3, 22, 1, 1, 2),
    _SetPtNtpSlot_Type()
)
setPtNtpSlot.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    setPtNtpSlot.setStatus("current")


class _SetPtNtpCommit_Type(Integer32):
    """Custom type setPtNtpCommit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("yes", 1)
    )


_SetPtNtpCommit_Type.__name__ = "Integer32"
_SetPtNtpCommit_Object = MibTableColumn
setPtNtpCommit = _SetPtNtpCommit_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 3, 22, 1, 1, 3),
    _SetPtNtpCommit_Type()
)
setPtNtpCommit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    setPtNtpCommit.setStatus("current")
_SetPtNtpProbe_Type = EnaValue
_SetPtNtpProbe_Object = MibTableColumn
setPtNtpProbe = _SetPtNtpProbe_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 3, 22, 1, 1, 4),
    _SetPtNtpProbe_Type()
)
setPtNtpProbe.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    setPtNtpProbe.setStatus("current")
_SetPtNtpBond_Type = EnaValue
_SetPtNtpBond_Object = MibTableColumn
setPtNtpBond = _SetPtNtpBond_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 3, 22, 1, 1, 5),
    _SetPtNtpBond_Type()
)
setPtNtpBond.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    setPtNtpBond.setStatus("current")
_SetPtNtpNTPd_Type = EnaValue
_SetPtNtpNTPd_Object = MibTableColumn
setPtNtpNTPd = _SetPtNtpNTPd_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 3, 22, 1, 1, 6),
    _SetPtNtpNTPd_Type()
)
setPtNtpNTPd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    setPtNtpNTPd.setStatus("current")


class _SetPtNtpTodsrcPrefer_Type(Integer32):
    """Custom type setPtNtpTodsrcPrefer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("todsrc", 1),
          ("peer", 2))
    )


_SetPtNtpTodsrcPrefer_Type.__name__ = "Integer32"
_SetPtNtpTodsrcPrefer_Object = MibTableColumn
setPtNtpTodsrcPrefer = _SetPtNtpTodsrcPrefer_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 3, 22, 1, 1, 7),
    _SetPtNtpTodsrcPrefer_Type()
)
setPtNtpTodsrcPrefer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    setPtNtpTodsrcPrefer.setStatus("current")


class _SetPtNtpTodsrcPriority_Type(Integer32):
    """Custom type setPtNtpTodsrcPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8),
    )


_SetPtNtpTodsrcPriority_Type.__name__ = "Integer32"
_SetPtNtpTodsrcPriority_Object = MibTableColumn
setPtNtpTodsrcPriority = _SetPtNtpTodsrcPriority_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 3, 22, 1, 1, 8),
    _SetPtNtpTodsrcPriority_Type()
)
setPtNtpTodsrcPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    setPtNtpTodsrcPriority.setStatus("current")


class _SetPtNtpWeight_Type(Integer32):
    """Custom type setPtNtpWeight based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 100),
    )


_SetPtNtpWeight_Type.__name__ = "Integer32"
_SetPtNtpWeight_Object = MibTableColumn
setPtNtpWeight = _SetPtNtpWeight_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 3, 22, 1, 1, 9),
    _SetPtNtpWeight_Type()
)
setPtNtpWeight.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    setPtNtpWeight.setStatus("current")


class _SetPtNtpCompensation_Type(Integer32):
    """Custom type setPtNtpCompensation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 250),
    )


_SetPtNtpCompensation_Type.__name__ = "Integer32"
_SetPtNtpCompensation_Object = MibTableColumn
setPtNtpCompensation = _SetPtNtpCompensation_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 3, 22, 1, 1, 10),
    _SetPtNtpCompensation_Type()
)
setPtNtpCompensation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    setPtNtpCompensation.setStatus("current")


class _SetPtNtpPeerTimeout_Type(Integer32):
    """Custom type setPtNtpPeerTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(60, 10000),
    )


_SetPtNtpPeerTimeout_Type.__name__ = "Integer32"
_SetPtNtpPeerTimeout_Object = MibTableColumn
setPtNtpPeerTimeout = _SetPtNtpPeerTimeout_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 3, 22, 1, 1, 11),
    _SetPtNtpPeerTimeout_Type()
)
setPtNtpPeerTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    setPtNtpPeerTimeout.setStatus("current")


class _SetPtNtpPeerPrefer_Type(Integer32):
    """Custom type setPtNtpPeerPrefer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8),
    )


_SetPtNtpPeerPrefer_Type.__name__ = "Integer32"
_SetPtNtpPeerPrefer_Object = MibTableColumn
setPtNtpPeerPrefer = _SetPtNtpPeerPrefer_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 3, 22, 1, 1, 12),
    _SetPtNtpPeerPrefer_Type()
)
setPtNtpPeerPrefer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    setPtNtpPeerPrefer.setStatus("current")
_SetPtNtpBypass_Type = OnValue
_SetPtNtpBypass_Object = MibTableColumn
setPtNtpBypass = _SetPtNtpBypass_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 3, 22, 1, 1, 13),
    _SetPtNtpBypass_Type()
)
setPtNtpBypass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    setPtNtpBypass.setStatus("current")
_SetPtNtpModActive_Type = YesValue
_SetPtNtpModActive_Object = MibTableColumn
setPtNtpModActive = _SetPtNtpModActive_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 3, 22, 1, 1, 14),
    _SetPtNtpModActive_Type()
)
setPtNtpModActive.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    setPtNtpModActive.setStatus("current")
_SetPtNtpPAActive_Type = YesValue
_SetPtNtpPAActive_Object = MibTableColumn
setPtNtpPAActive = _SetPtNtpPAActive_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 3, 22, 1, 1, 15),
    _SetPtNtpPAActive_Type()
)
setPtNtpPAActive.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    setPtNtpPAActive.setStatus("current")
_SetPtNtpPBActive_Type = YesValue
_SetPtNtpPBActive_Object = MibTableColumn
setPtNtpPBActive = _SetPtNtpPBActive_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 3, 22, 1, 1, 16),
    _SetPtNtpPBActive_Type()
)
setPtNtpPBActive.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    setPtNtpPBActive.setStatus("current")
_SetPtNtpPortTable_Object = MibTable
setPtNtpPortTable = _SetPtNtpPortTable_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 3, 22, 2)
)
if mibBuilder.loadTexts:
    setPtNtpPortTable.setStatus("current")
_SetPtNtpPortEntry_Object = MibTableRow
setPtNtpPortEntry = _SetPtNtpPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 3, 22, 2, 1)
)
setPtNtpPortEntry.setIndexNames(
    (0, "SSU2000-MIB", "setPtNtpPortChassis"),
    (0, "SSU2000-MIB", "setPtNtpPortSlot"),
    (0, "SSU2000-MIB", "setPtNtpPortNum"),
)
if mibBuilder.loadTexts:
    setPtNtpPortEntry.setStatus("current")


class _SetPtNtpPortChassis_Type(Integer32):
    """Custom type setPtNtpPortChassis based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_SetPtNtpPortChassis_Type.__name__ = "Integer32"
_SetPtNtpPortChassis_Object = MibTableColumn
setPtNtpPortChassis = _SetPtNtpPortChassis_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 3, 22, 2, 1, 1),
    _SetPtNtpPortChassis_Type()
)
setPtNtpPortChassis.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    setPtNtpPortChassis.setStatus("current")


class _SetPtNtpPortSlot_Type(Integer32):
    """Custom type setPtNtpPortSlot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 20),
    )


_SetPtNtpPortSlot_Type.__name__ = "Integer32"
_SetPtNtpPortSlot_Object = MibTableColumn
setPtNtpPortSlot = _SetPtNtpPortSlot_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 3, 22, 2, 1, 2),
    _SetPtNtpPortSlot_Type()
)
setPtNtpPortSlot.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    setPtNtpPortSlot.setStatus("current")


class _SetPtNtpPortNum_Type(Integer32):
    """Custom type setPtNtpPortNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_SetPtNtpPortNum_Type.__name__ = "Integer32"
_SetPtNtpPortNum_Object = MibTableColumn
setPtNtpPortNum = _SetPtNtpPortNum_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 3, 22, 2, 1, 3),
    _SetPtNtpPortNum_Type()
)
setPtNtpPortNum.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    setPtNtpPortNum.setStatus("current")
_SetPtNtpPortAddr_Type = IpAddress
_SetPtNtpPortAddr_Object = MibTableColumn
setPtNtpPortAddr = _SetPtNtpPortAddr_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 3, 22, 2, 1, 4),
    _SetPtNtpPortAddr_Type()
)
setPtNtpPortAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    setPtNtpPortAddr.setStatus("current")
_SetPtNtpPortMask_Type = IpAddress
_SetPtNtpPortMask_Object = MibTableColumn
setPtNtpPortMask = _SetPtNtpPortMask_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 3, 22, 2, 1, 5),
    _SetPtNtpPortMask_Type()
)
setPtNtpPortMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    setPtNtpPortMask.setStatus("current")
_SetPtNtpPortGate_Type = IpAddress
_SetPtNtpPortGate_Object = MibTableColumn
setPtNtpPortGate = _SetPtNtpPortGate_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 3, 22, 2, 1, 6),
    _SetPtNtpPortGate_Type()
)
setPtNtpPortGate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    setPtNtpPortGate.setStatus("current")
_SetPtNtpPeerTable_Object = MibTable
setPtNtpPeerTable = _SetPtNtpPeerTable_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 3, 22, 3)
)
if mibBuilder.loadTexts:
    setPtNtpPeerTable.setStatus("current")
_SetPtNtpPeerEntry_Object = MibTableRow
setPtNtpPeerEntry = _SetPtNtpPeerEntry_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 3, 22, 3, 1)
)
setPtNtpPeerEntry.setIndexNames(
    (0, "SSU2000-MIB", "setPtNtpPeerChassis"),
    (0, "SSU2000-MIB", "setPtNtpPeerSlot"),
    (0, "SSU2000-MIB", "setPtNtpPeerNum"),
)
if mibBuilder.loadTexts:
    setPtNtpPeerEntry.setStatus("current")


class _SetPtNtpPeerChassis_Type(Integer32):
    """Custom type setPtNtpPeerChassis based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_SetPtNtpPeerChassis_Type.__name__ = "Integer32"
_SetPtNtpPeerChassis_Object = MibTableColumn
setPtNtpPeerChassis = _SetPtNtpPeerChassis_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 3, 22, 3, 1, 1),
    _SetPtNtpPeerChassis_Type()
)
setPtNtpPeerChassis.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    setPtNtpPeerChassis.setStatus("current")


class _SetPtNtpPeerSlot_Type(Integer32):
    """Custom type setPtNtpPeerSlot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 20),
    )


_SetPtNtpPeerSlot_Type.__name__ = "Integer32"
_SetPtNtpPeerSlot_Object = MibTableColumn
setPtNtpPeerSlot = _SetPtNtpPeerSlot_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 3, 22, 3, 1, 2),
    _SetPtNtpPeerSlot_Type()
)
setPtNtpPeerSlot.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    setPtNtpPeerSlot.setStatus("current")


class _SetPtNtpPeerNum_Type(Integer32):
    """Custom type setPtNtpPeerNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_SetPtNtpPeerNum_Type.__name__ = "Integer32"
_SetPtNtpPeerNum_Object = MibTableColumn
setPtNtpPeerNum = _SetPtNtpPeerNum_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 3, 22, 3, 1, 3),
    _SetPtNtpPeerNum_Type()
)
setPtNtpPeerNum.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    setPtNtpPeerNum.setStatus("current")
_SetPtNtpPeerAddr_Type = IpAddress
_SetPtNtpPeerAddr_Object = MibTableColumn
setPtNtpPeerAddr = _SetPtNtpPeerAddr_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 3, 22, 3, 1, 4),
    _SetPtNtpPeerAddr_Type()
)
setPtNtpPeerAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    setPtNtpPeerAddr.setStatus("current")


class _SetPtNtpPeerPmin_Type(Integer32):
    """Custom type setPtNtpPeerPmin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(16, 16),
        ValueRangeConstraint(32, 32),
        ValueRangeConstraint(64, 64),
        ValueRangeConstraint(128, 128),
        ValueRangeConstraint(256, 256),
        ValueRangeConstraint(512, 512),
        ValueRangeConstraint(1024, 1024),
    )


_SetPtNtpPeerPmin_Type.__name__ = "Integer32"
_SetPtNtpPeerPmin_Object = MibTableColumn
setPtNtpPeerPmin = _SetPtNtpPeerPmin_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 3, 22, 3, 1, 5),
    _SetPtNtpPeerPmin_Type()
)
setPtNtpPeerPmin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    setPtNtpPeerPmin.setStatus("current")


class _SetPtNtpPeerPmax_Type(Integer32):
    """Custom type setPtNtpPeerPmax based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(16, 16),
        ValueRangeConstraint(32, 32),
        ValueRangeConstraint(64, 64),
        ValueRangeConstraint(128, 128),
        ValueRangeConstraint(256, 256),
        ValueRangeConstraint(512, 512),
        ValueRangeConstraint(1024, 1024),
    )


_SetPtNtpPeerPmax_Type.__name__ = "Integer32"
_SetPtNtpPeerPmax_Object = MibTableColumn
setPtNtpPeerPmax = _SetPtNtpPeerPmax_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 3, 22, 3, 1, 6),
    _SetPtNtpPeerPmax_Type()
)
setPtNtpPeerPmax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    setPtNtpPeerPmax.setStatus("current")


class _SetPtNtpPeerKeyId_Type(Integer32):
    """Custom type setPtNtpPeerKeyId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65534),
    )


_SetPtNtpPeerKeyId_Type.__name__ = "Integer32"
_SetPtNtpPeerKeyId_Object = MibTableColumn
setPtNtpPeerKeyId = _SetPtNtpPeerKeyId_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 3, 22, 3, 1, 7),
    _SetPtNtpPeerKeyId_Type()
)
setPtNtpPeerKeyId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    setPtNtpPeerKeyId.setStatus("current")
_SetPtNtpAuthTable_Object = MibTable
setPtNtpAuthTable = _SetPtNtpAuthTable_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 3, 22, 4)
)
if mibBuilder.loadTexts:
    setPtNtpAuthTable.setStatus("current")
_SetPtNtpAuthEntry_Object = MibTableRow
setPtNtpAuthEntry = _SetPtNtpAuthEntry_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 3, 22, 4, 1)
)
setPtNtpAuthEntry.setIndexNames(
    (0, "SSU2000-MIB", "setPtNtpAuthChassis"),
    (0, "SSU2000-MIB", "setPtNtpAuthSlot"),
    (0, "SSU2000-MIB", "setPtNtpAuthNum"),
)
if mibBuilder.loadTexts:
    setPtNtpAuthEntry.setStatus("current")


class _SetPtNtpAuthChassis_Type(Integer32):
    """Custom type setPtNtpAuthChassis based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_SetPtNtpAuthChassis_Type.__name__ = "Integer32"
_SetPtNtpAuthChassis_Object = MibTableColumn
setPtNtpAuthChassis = _SetPtNtpAuthChassis_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 3, 22, 4, 1, 1),
    _SetPtNtpAuthChassis_Type()
)
setPtNtpAuthChassis.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    setPtNtpAuthChassis.setStatus("current")


class _SetPtNtpAuthSlot_Type(Integer32):
    """Custom type setPtNtpAuthSlot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 20),
    )


_SetPtNtpAuthSlot_Type.__name__ = "Integer32"
_SetPtNtpAuthSlot_Object = MibTableColumn
setPtNtpAuthSlot = _SetPtNtpAuthSlot_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 3, 22, 4, 1, 2),
    _SetPtNtpAuthSlot_Type()
)
setPtNtpAuthSlot.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    setPtNtpAuthSlot.setStatus("current")


class _SetPtNtpAuthNum_Type(Integer32):
    """Custom type setPtNtpAuthNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_SetPtNtpAuthNum_Type.__name__ = "Integer32"
_SetPtNtpAuthNum_Object = MibTableColumn
setPtNtpAuthNum = _SetPtNtpAuthNum_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 3, 22, 4, 1, 3),
    _SetPtNtpAuthNum_Type()
)
setPtNtpAuthNum.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    setPtNtpAuthNum.setStatus("current")


class _SetPtNtpAuthKeyId_Type(Integer32):
    """Custom type setPtNtpAuthKeyId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65534),
    )


_SetPtNtpAuthKeyId_Type.__name__ = "Integer32"
_SetPtNtpAuthKeyId_Object = MibTableColumn
setPtNtpAuthKeyId = _SetPtNtpAuthKeyId_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 3, 22, 4, 1, 4),
    _SetPtNtpAuthKeyId_Type()
)
setPtNtpAuthKeyId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    setPtNtpAuthKeyId.setStatus("current")


class _SetPtNtpAuthKeyValue_Type(DisplayString):
    """Custom type setPtNtpAuthKeyValue based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(8, 32),
    )


_SetPtNtpAuthKeyValue_Type.__name__ = "DisplayString"
_SetPtNtpAuthKeyValue_Object = MibTableColumn
setPtNtpAuthKeyValue = _SetPtNtpAuthKeyValue_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 3, 22, 4, 1, 5),
    _SetPtNtpAuthKeyValue_Type()
)
setPtNtpAuthKeyValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    setPtNtpAuthKeyValue.setStatus("current")
_SetPtNtpRouteTable_Object = MibTable
setPtNtpRouteTable = _SetPtNtpRouteTable_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 3, 22, 5)
)
if mibBuilder.loadTexts:
    setPtNtpRouteTable.setStatus("current")
_SetPtNtpRouteEntry_Object = MibTableRow
setPtNtpRouteEntry = _SetPtNtpRouteEntry_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 3, 22, 5, 1)
)
setPtNtpRouteEntry.setIndexNames(
    (0, "SSU2000-MIB", "setPtNtpRouteChassis"),
    (0, "SSU2000-MIB", "setPtNtpRouteSlot"),
    (0, "SSU2000-MIB", "setPtNtpRouteNum"),
)
if mibBuilder.loadTexts:
    setPtNtpRouteEntry.setStatus("current")


class _SetPtNtpRouteChassis_Type(Integer32):
    """Custom type setPtNtpRouteChassis based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_SetPtNtpRouteChassis_Type.__name__ = "Integer32"
_SetPtNtpRouteChassis_Object = MibTableColumn
setPtNtpRouteChassis = _SetPtNtpRouteChassis_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 3, 22, 5, 1, 1),
    _SetPtNtpRouteChassis_Type()
)
setPtNtpRouteChassis.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    setPtNtpRouteChassis.setStatus("current")


class _SetPtNtpRouteSlot_Type(Integer32):
    """Custom type setPtNtpRouteSlot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 20),
    )


_SetPtNtpRouteSlot_Type.__name__ = "Integer32"
_SetPtNtpRouteSlot_Object = MibTableColumn
setPtNtpRouteSlot = _SetPtNtpRouteSlot_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 3, 22, 5, 1, 2),
    _SetPtNtpRouteSlot_Type()
)
setPtNtpRouteSlot.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    setPtNtpRouteSlot.setStatus("current")


class _SetPtNtpRouteNum_Type(Integer32):
    """Custom type setPtNtpRouteNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 6),
    )


_SetPtNtpRouteNum_Type.__name__ = "Integer32"
_SetPtNtpRouteNum_Object = MibTableColumn
setPtNtpRouteNum = _SetPtNtpRouteNum_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 3, 22, 5, 1, 3),
    _SetPtNtpRouteNum_Type()
)
setPtNtpRouteNum.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    setPtNtpRouteNum.setStatus("current")
_SetPtNtpRouteAddr_Type = IpAddress
_SetPtNtpRouteAddr_Object = MibTableColumn
setPtNtpRouteAddr = _SetPtNtpRouteAddr_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 3, 22, 5, 1, 4),
    _SetPtNtpRouteAddr_Type()
)
setPtNtpRouteAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    setPtNtpRouteAddr.setStatus("current")
_SetPtNtpRouteMask_Type = IpAddress
_SetPtNtpRouteMask_Object = MibTableColumn
setPtNtpRouteMask = _SetPtNtpRouteMask_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 3, 22, 5, 1, 5),
    _SetPtNtpRouteMask_Type()
)
setPtNtpRouteMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    setPtNtpRouteMask.setStatus("current")
_SetPtNtpRouteGate_Type = IpAddress
_SetPtNtpRouteGate_Object = MibTableColumn
setPtNtpRouteGate = _SetPtNtpRouteGate_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 3, 22, 5, 1, 6),
    _SetPtNtpRouteGate_Type()
)
setPtNtpRouteGate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    setPtNtpRouteGate.setStatus("current")


class _SetPtNtpRouteIface_Type(Integer32):
    """Custom type setPtNtpRouteIface based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_SetPtNtpRouteIface_Type.__name__ = "Integer32"
_SetPtNtpRouteIface_Object = MibTableColumn
setPtNtpRouteIface = _SetPtNtpRouteIface_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 3, 22, 5, 1, 7),
    _SetPtNtpRouteIface_Type()
)
setPtNtpRouteIface.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    setPtNtpRouteIface.setStatus("current")
_SetPtNtpVlanTable_Object = MibTable
setPtNtpVlanTable = _SetPtNtpVlanTable_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 3, 22, 6)
)
if mibBuilder.loadTexts:
    setPtNtpVlanTable.setStatus("current")
_SetPtNtpVlanEntry_Object = MibTableRow
setPtNtpVlanEntry = _SetPtNtpVlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 3, 22, 6, 1)
)
setPtNtpVlanEntry.setIndexNames(
    (0, "SSU2000-MIB", "setPtNtpVlanChassis"),
    (0, "SSU2000-MIB", "setPtNtpVlanSlot"),
)
if mibBuilder.loadTexts:
    setPtNtpVlanEntry.setStatus("current")


class _SetPtNtpVlanChassis_Type(Integer32):
    """Custom type setPtNtpVlanChassis based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_SetPtNtpVlanChassis_Type.__name__ = "Integer32"
_SetPtNtpVlanChassis_Object = MibTableColumn
setPtNtpVlanChassis = _SetPtNtpVlanChassis_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 3, 22, 6, 1, 1),
    _SetPtNtpVlanChassis_Type()
)
setPtNtpVlanChassis.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    setPtNtpVlanChassis.setStatus("current")


class _SetPtNtpVlanSlot_Type(Integer32):
    """Custom type setPtNtpVlanSlot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 20),
    )


_SetPtNtpVlanSlot_Type.__name__ = "Integer32"
_SetPtNtpVlanSlot_Object = MibTableColumn
setPtNtpVlanSlot = _SetPtNtpVlanSlot_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 3, 22, 6, 1, 2),
    _SetPtNtpVlanSlot_Type()
)
setPtNtpVlanSlot.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    setPtNtpVlanSlot.setStatus("current")
_SetPtNtpVlan_Type = EnaValue
_SetPtNtpVlan_Object = MibTableColumn
setPtNtpVlan = _SetPtNtpVlan_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 3, 22, 6, 1, 3),
    _SetPtNtpVlan_Type()
)
setPtNtpVlan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    setPtNtpVlan.setStatus("current")


class _SetPtNtpVlanPAId_Type(Integer32):
    """Custom type setPtNtpVlanPAId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_SetPtNtpVlanPAId_Type.__name__ = "Integer32"
_SetPtNtpVlanPAId_Object = MibTableColumn
setPtNtpVlanPAId = _SetPtNtpVlanPAId_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 3, 22, 6, 1, 4),
    _SetPtNtpVlanPAId_Type()
)
setPtNtpVlanPAId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    setPtNtpVlanPAId.setStatus("current")


class _SetPtNtpVlanPAPriority_Type(Integer32):
    """Custom type setPtNtpVlanPAPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_SetPtNtpVlanPAPriority_Type.__name__ = "Integer32"
_SetPtNtpVlanPAPriority_Object = MibTableColumn
setPtNtpVlanPAPriority = _SetPtNtpVlanPAPriority_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 3, 22, 6, 1, 5),
    _SetPtNtpVlanPAPriority_Type()
)
setPtNtpVlanPAPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    setPtNtpVlanPAPriority.setStatus("current")


class _SetPtNtpVlanPBId_Type(Integer32):
    """Custom type setPtNtpVlanPBId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_SetPtNtpVlanPBId_Type.__name__ = "Integer32"
_SetPtNtpVlanPBId_Object = MibTableColumn
setPtNtpVlanPBId = _SetPtNtpVlanPBId_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 3, 22, 6, 1, 6),
    _SetPtNtpVlanPBId_Type()
)
setPtNtpVlanPBId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    setPtNtpVlanPBId.setStatus("current")


class _SetPtNtpVlanPBPriority_Type(Integer32):
    """Custom type setPtNtpVlanPBPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_SetPtNtpVlanPBPriority_Type.__name__ = "Integer32"
_SetPtNtpVlanPBPriority_Object = MibTableColumn
setPtNtpVlanPBPriority = _SetPtNtpVlanPBPriority_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 3, 22, 6, 1, 7),
    _SetPtNtpVlanPBPriority_Type()
)
setPtNtpVlanPBPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    setPtNtpVlanPBPriority.setStatus("current")


class _SetPtNtpVlanBondId_Type(Integer32):
    """Custom type setPtNtpVlanBondId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_SetPtNtpVlanBondId_Type.__name__ = "Integer32"
_SetPtNtpVlanBondId_Object = MibTableColumn
setPtNtpVlanBondId = _SetPtNtpVlanBondId_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 3, 22, 6, 1, 8),
    _SetPtNtpVlanBondId_Type()
)
setPtNtpVlanBondId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    setPtNtpVlanBondId.setStatus("current")


class _SetPtNtpVlanBondPriority_Type(Integer32):
    """Custom type setPtNtpVlanBondPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_SetPtNtpVlanBondPriority_Type.__name__ = "Integer32"
_SetPtNtpVlanBondPriority_Object = MibTableColumn
setPtNtpVlanBondPriority = _SetPtNtpVlanBondPriority_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 3, 22, 6, 1, 9),
    _SetPtNtpVlanBondPriority_Type()
)
setPtNtpVlanBondPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    setPtNtpVlanBondPriority.setStatus("current")
_SetupPtPtp_ObjectIdentity = ObjectIdentity
setupPtPtp = _SetupPtPtp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 3, 23)
)
_SetPtPtpTable_Object = MibTable
setPtPtpTable = _SetPtPtpTable_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 3, 23, 1)
)
if mibBuilder.loadTexts:
    setPtPtpTable.setStatus("current")
_SetPtPtpEntry_Object = MibTableRow
setPtPtpEntry = _SetPtPtpEntry_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 3, 23, 1, 1)
)
setPtPtpEntry.setIndexNames(
    (0, "SSU2000-MIB", "setPtPtpChassis"),
    (0, "SSU2000-MIB", "setPtPtpSlot"),
)
if mibBuilder.loadTexts:
    setPtPtpEntry.setStatus("current")


class _SetPtPtpChassis_Type(Integer32):
    """Custom type setPtPtpChassis based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_SetPtPtpChassis_Type.__name__ = "Integer32"
_SetPtPtpChassis_Object = MibTableColumn
setPtPtpChassis = _SetPtPtpChassis_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 3, 23, 1, 1, 1),
    _SetPtPtpChassis_Type()
)
setPtPtpChassis.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    setPtPtpChassis.setStatus("current")


class _SetPtPtpSlot_Type(Integer32):
    """Custom type setPtPtpSlot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 20),
    )


_SetPtPtpSlot_Type.__name__ = "Integer32"
_SetPtPtpSlot_Object = MibTableColumn
setPtPtpSlot = _SetPtPtpSlot_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 3, 23, 1, 1, 2),
    _SetPtPtpSlot_Type()
)
setPtPtpSlot.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    setPtPtpSlot.setStatus("current")


class _SetPtPtpCommit_Type(Integer32):
    """Custom type setPtPtpCommit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("yes", 1)
    )


_SetPtPtpCommit_Type.__name__ = "Integer32"
_SetPtPtpCommit_Object = MibTableColumn
setPtPtpCommit = _SetPtPtpCommit_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 3, 23, 1, 1, 3),
    _SetPtPtpCommit_Type()
)
setPtPtpCommit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    setPtPtpCommit.setStatus("current")
_SetPtPtpService_Type = EnaValue
_SetPtPtpService_Object = MibTableColumn
setPtPtpService = _SetPtPtpService_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 3, 23, 1, 1, 4),
    _SetPtPtpService_Type()
)
setPtPtpService.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    setPtPtpService.setStatus("current")


class _SetPtPtpClockId_Type(OctetString):
    """Custom type setPtPtpClockId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )
    fixed_length = 8


_SetPtPtpClockId_Type.__name__ = "OctetString"
_SetPtPtpClockId_Object = MibTableColumn
setPtPtpClockId = _SetPtPtpClockId_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 3, 23, 1, 1, 5),
    _SetPtPtpClockId_Type()
)
setPtPtpClockId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    setPtPtpClockId.setStatus("current")


class _SetPtPtpDomain_Type(Integer32):
    """Custom type setPtPtpDomain based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_SetPtPtpDomain_Type.__name__ = "Integer32"
_SetPtPtpDomain_Object = MibTableColumn
setPtPtpDomain = _SetPtPtpDomain_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 3, 23, 1, 1, 6),
    _SetPtPtpDomain_Type()
)
setPtPtpDomain.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    setPtPtpDomain.setStatus("current")


class _SetPtPtpTimescale_Type(Integer32):
    """Custom type setPtPtpTimescale based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ptp", 1),
          ("arb", 2))
    )


_SetPtPtpTimescale_Type.__name__ = "Integer32"
_SetPtPtpTimescale_Object = MibTableColumn
setPtPtpTimescale = _SetPtPtpTimescale_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 3, 23, 1, 1, 7),
    _SetPtPtpTimescale_Type()
)
setPtPtpTimescale.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    setPtPtpTimescale.setStatus("current")


class _SetPtPtpSyncLimit_Type(Integer32):
    """Custom type setPtPtpSyncLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-7, 7),
    )


_SetPtPtpSyncLimit_Type.__name__ = "Integer32"
_SetPtPtpSyncLimit_Object = MibTableColumn
setPtPtpSyncLimit = _SetPtPtpSyncLimit_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 3, 23, 1, 1, 8),
    _SetPtPtpSyncLimit_Type()
)
setPtPtpSyncLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    setPtPtpSyncLimit.setStatus("current")


class _SetPtPtpAnnounceLimit_Type(Integer32):
    """Custom type setPtPtpAnnounceLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-3, 4),
    )


_SetPtPtpAnnounceLimit_Type.__name__ = "Integer32"
_SetPtPtpAnnounceLimit_Object = MibTableColumn
setPtPtpAnnounceLimit = _SetPtPtpAnnounceLimit_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 3, 23, 1, 1, 9),
    _SetPtPtpAnnounceLimit_Type()
)
setPtPtpAnnounceLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    setPtPtpAnnounceLimit.setStatus("current")


class _SetPtPtpDelayLimit_Type(Integer32):
    """Custom type setPtPtpDelayLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-7, 7),
    )


_SetPtPtpDelayLimit_Type.__name__ = "Integer32"
_SetPtPtpDelayLimit_Object = MibTableColumn
setPtPtpDelayLimit = _SetPtPtpDelayLimit_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 3, 23, 1, 1, 10),
    _SetPtPtpDelayLimit_Type()
)
setPtPtpDelayLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    setPtPtpDelayLimit.setStatus("current")
_SetPtPtpDscpState_Type = EnaValue
_SetPtPtpDscpState_Object = MibTableColumn
setPtPtpDscpState = _SetPtPtpDscpState_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 3, 23, 1, 1, 11),
    _SetPtPtpDscpState_Type()
)
setPtPtpDscpState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    setPtPtpDscpState.setStatus("current")


class _SetPtPtpDscpValue_Type(Integer32):
    """Custom type setPtPtpDscpValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_SetPtPtpDscpValue_Type.__name__ = "Integer32"
_SetPtPtpDscpValue_Object = MibTableColumn
setPtPtpDscpValue = _SetPtPtpDscpValue_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 3, 23, 1, 1, 12),
    _SetPtPtpDscpValue_Type()
)
setPtPtpDscpValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    setPtPtpDscpValue.setStatus("current")


class _SetPtPtpMaxClient_Type(Integer32):
    """Custom type setPtPtpMaxClient based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(64, 400),
    )


_SetPtPtpMaxClient_Type.__name__ = "Integer32"
_SetPtPtpMaxClient_Object = MibTableColumn
setPtPtpMaxClient = _SetPtPtpMaxClient_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 3, 23, 1, 1, 13),
    _SetPtPtpMaxClient_Type()
)
setPtPtpMaxClient.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    setPtPtpMaxClient.setStatus("current")


class _SetPtPtpPortPriority1_Type(Integer32):
    """Custom type setPtPtpPortPriority1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_SetPtPtpPortPriority1_Type.__name__ = "Integer32"
_SetPtPtpPortPriority1_Object = MibTableColumn
setPtPtpPortPriority1 = _SetPtPtpPortPriority1_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 3, 23, 1, 1, 14),
    _SetPtPtpPortPriority1_Type()
)
setPtPtpPortPriority1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    setPtPtpPortPriority1.setStatus("current")


class _SetPtPtpPortPriority2_Type(Integer32):
    """Custom type setPtPtpPortPriority2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_SetPtPtpPortPriority2_Type.__name__ = "Integer32"
_SetPtPtpPortPriority2_Object = MibTableColumn
setPtPtpPortPriority2 = _SetPtPtpPortPriority2_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 3, 23, 1, 1, 15),
    _SetPtPtpPortPriority2_Type()
)
setPtPtpPortPriority2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    setPtPtpPortPriority2.setStatus("current")


class _SetPtPtpUniLeaseDuration_Type(Integer32):
    """Custom type setPtPtpUniLeaseDuration based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 1000),
    )


_SetPtPtpUniLeaseDuration_Type.__name__ = "Integer32"
_SetPtPtpUniLeaseDuration_Object = MibTableColumn
setPtPtpUniLeaseDuration = _SetPtPtpUniLeaseDuration_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 3, 23, 1, 1, 16),
    _SetPtPtpUniLeaseDuration_Type()
)
setPtPtpUniLeaseDuration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    setPtPtpUniLeaseDuration.setStatus("current")
_SetPtPtpUniNegotiation_Type = EnaValue
_SetPtPtpUniNegotiation_Object = MibTableColumn
setPtPtpUniNegotiation = _SetPtPtpUniNegotiation_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 3, 23, 1, 1, 17),
    _SetPtPtpUniNegotiation_Type()
)
setPtPtpUniNegotiation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    setPtPtpUniNegotiation.setStatus("current")
_SetPtPtpTwostep_Type = EnaValue
_SetPtPtpTwostep_Object = MibTableColumn
setPtPtpTwostep = _SetPtPtpTwostep_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 3, 23, 1, 1, 18),
    _SetPtPtpTwostep_Type()
)
setPtPtpTwostep.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    setPtPtpTwostep.setStatus("current")


class _SetPtPtpProfile_Type(Integer32):
    """Custom type setPtPtpProfile based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              4)
        )
    )
    namedValues = NamedValues(
        *(("telecom2008", 1),
          ("ituG8265dot1", 4))
    )


_SetPtPtpProfile_Type.__name__ = "Integer32"
_SetPtPtpProfile_Object = MibTableColumn
setPtPtpProfile = _SetPtPtpProfile_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 3, 23, 1, 1, 19),
    _SetPtPtpProfile_Type()
)
setPtPtpProfile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    setPtPtpProfile.setStatus("current")


class _SetPtPtpSsmOption_Type(Integer32):
    """Custom type setPtPtpSsmOption based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("option1", 1),
          ("option2", 2))
    )


_SetPtPtpSsmOption_Type.__name__ = "Integer32"
_SetPtPtpSsmOption_Object = MibTableColumn
setPtPtpSsmOption = _SetPtPtpSsmOption_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 3, 23, 1, 1, 20),
    _SetPtPtpSsmOption_Type()
)
setPtPtpSsmOption.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    setPtPtpSsmOption.setStatus("current")
_SetPtPtpBypass_Type = OnValue
_SetPtPtpBypass_Object = MibTableColumn
setPtPtpBypass = _SetPtPtpBypass_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 3, 23, 1, 1, 30),
    _SetPtPtpBypass_Type()
)
setPtPtpBypass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    setPtPtpBypass.setStatus("current")
_SetPtPtpModActive_Type = YesValue
_SetPtPtpModActive_Object = MibTableColumn
setPtPtpModActive = _SetPtPtpModActive_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 3, 23, 1, 1, 31),
    _SetPtPtpModActive_Type()
)
setPtPtpModActive.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    setPtPtpModActive.setStatus("current")


class _SetPtPtpEthRate_Type(Integer32):
    """Custom type setPtPtpEthRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("all", 0),
          ("r100", 1),
          ("r1000", 2))
    )


_SetPtPtpEthRate_Type.__name__ = "Integer32"
_SetPtPtpEthRate_Object = MibTableColumn
setPtPtpEthRate = _SetPtPtpEthRate_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 3, 23, 1, 1, 32),
    _SetPtPtpEthRate_Type()
)
setPtPtpEthRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    setPtPtpEthRate.setStatus("current")
_SetPtPtpVlan_Type = EnaValue
_SetPtPtpVlan_Object = MibTableColumn
setPtPtpVlan = _SetPtPtpVlan_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 3, 23, 1, 1, 33),
    _SetPtPtpVlan_Type()
)
setPtPtpVlan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    setPtPtpVlan.setStatus("current")


class _SetPtPtpRmvClient_Type(OctetString):
    """Custom type setPtPtpRmvClient based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )
    fixed_length = 8


_SetPtPtpRmvClient_Type.__name__ = "OctetString"
_SetPtPtpRmvClient_Object = MibTableColumn
setPtPtpRmvClient = _SetPtPtpRmvClient_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 3, 23, 1, 1, 34),
    _SetPtPtpRmvClient_Type()
)
setPtPtpRmvClient.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    setPtPtpRmvClient.setStatus("current")
_SetPtpPortTable_Object = MibTable
setPtpPortTable = _SetPtpPortTable_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 3, 23, 2)
)
if mibBuilder.loadTexts:
    setPtpPortTable.setStatus("current")
_SetPtpPortEntry_Object = MibTableRow
setPtpPortEntry = _SetPtpPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 3, 23, 2, 1)
)
setPtpPortEntry.setIndexNames(
    (0, "SSU2000-MIB", "setPtpPortChassis"),
    (0, "SSU2000-MIB", "setPtpPortSlot"),
    (0, "SSU2000-MIB", "setPtpPortNum"),
)
if mibBuilder.loadTexts:
    setPtpPortEntry.setStatus("current")


class _SetPtpPortChassis_Type(Integer32):
    """Custom type setPtpPortChassis based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_SetPtpPortChassis_Type.__name__ = "Integer32"
_SetPtpPortChassis_Object = MibTableColumn
setPtpPortChassis = _SetPtpPortChassis_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 3, 23, 2, 1, 1),
    _SetPtpPortChassis_Type()
)
setPtpPortChassis.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    setPtpPortChassis.setStatus("current")


class _SetPtpPortSlot_Type(Integer32):
    """Custom type setPtpPortSlot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 20),
    )


_SetPtpPortSlot_Type.__name__ = "Integer32"
_SetPtpPortSlot_Object = MibTableColumn
setPtpPortSlot = _SetPtpPortSlot_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 3, 23, 2, 1, 2),
    _SetPtpPortSlot_Type()
)
setPtpPortSlot.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    setPtpPortSlot.setStatus("current")


class _SetPtpPortNum_Type(Integer32):
    """Custom type setPtpPortNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_SetPtpPortNum_Type.__name__ = "Integer32"
_SetPtpPortNum_Object = MibTableColumn
setPtpPortNum = _SetPtpPortNum_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 3, 23, 2, 1, 3),
    _SetPtpPortNum_Type()
)
setPtpPortNum.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    setPtpPortNum.setStatus("current")
_SetPtpPortAddr_Type = IpAddress
_SetPtpPortAddr_Object = MibTableColumn
setPtpPortAddr = _SetPtpPortAddr_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 3, 23, 2, 1, 4),
    _SetPtpPortAddr_Type()
)
setPtpPortAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    setPtpPortAddr.setStatus("current")
_SetPtpPortMask_Type = IpAddress
_SetPtpPortMask_Object = MibTableColumn
setPtpPortMask = _SetPtpPortMask_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 3, 23, 2, 1, 5),
    _SetPtpPortMask_Type()
)
setPtpPortMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    setPtpPortMask.setStatus("current")
_SetPtpPortGate_Type = IpAddress
_SetPtpPortGate_Object = MibTableColumn
setPtpPortGate = _SetPtpPortGate_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 3, 23, 2, 1, 6),
    _SetPtpPortGate_Type()
)
setPtpPortGate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    setPtpPortGate.setStatus("current")
_SetPtpVlanTable_Object = MibTable
setPtpVlanTable = _SetPtpVlanTable_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 3, 23, 3)
)
if mibBuilder.loadTexts:
    setPtpVlanTable.setStatus("current")
_SetPtpVlanEntry_Object = MibTableRow
setPtpVlanEntry = _SetPtpVlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 3, 23, 3, 1)
)
setPtpVlanEntry.setIndexNames(
    (0, "SSU2000-MIB", "setPtpVlanChassis"),
    (0, "SSU2000-MIB", "setPtpVlanSlot"),
    (0, "SSU2000-MIB", "setPtpVlanIndex"),
)
if mibBuilder.loadTexts:
    setPtpVlanEntry.setStatus("current")


class _SetPtpVlanChassis_Type(Integer32):
    """Custom type setPtpVlanChassis based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_SetPtpVlanChassis_Type.__name__ = "Integer32"
_SetPtpVlanChassis_Object = MibTableColumn
setPtpVlanChassis = _SetPtpVlanChassis_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 3, 23, 3, 1, 1),
    _SetPtpVlanChassis_Type()
)
setPtpVlanChassis.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    setPtpVlanChassis.setStatus("current")


class _SetPtpVlanSlot_Type(Integer32):
    """Custom type setPtpVlanSlot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 20),
    )


_SetPtpVlanSlot_Type.__name__ = "Integer32"
_SetPtpVlanSlot_Object = MibTableColumn
setPtpVlanSlot = _SetPtpVlanSlot_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 3, 23, 3, 1, 2),
    _SetPtpVlanSlot_Type()
)
setPtpVlanSlot.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    setPtpVlanSlot.setStatus("current")


class _SetPtpVlanIndex_Type(Integer32):
    """Custom type setPtpVlanIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_SetPtpVlanIndex_Type.__name__ = "Integer32"
_SetPtpVlanIndex_Object = MibTableColumn
setPtpVlanIndex = _SetPtpVlanIndex_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 3, 23, 3, 1, 3),
    _SetPtpVlanIndex_Type()
)
setPtpVlanIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    setPtpVlanIndex.setStatus("current")
_SetPtpVlanState_Type = EnaValue
_SetPtpVlanState_Object = MibTableColumn
setPtpVlanState = _SetPtpVlanState_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 3, 23, 3, 1, 4),
    _SetPtpVlanState_Type()
)
setPtpVlanState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    setPtpVlanState.setStatus("current")
_SetPtpVlanAddr_Type = IpAddress
_SetPtpVlanAddr_Object = MibTableColumn
setPtpVlanAddr = _SetPtpVlanAddr_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 3, 23, 3, 1, 5),
    _SetPtpVlanAddr_Type()
)
setPtpVlanAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    setPtpVlanAddr.setStatus("current")
_SetPtpVlanMask_Type = IpAddress
_SetPtpVlanMask_Object = MibTableColumn
setPtpVlanMask = _SetPtpVlanMask_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 3, 23, 3, 1, 6),
    _SetPtpVlanMask_Type()
)
setPtpVlanMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    setPtpVlanMask.setStatus("current")
_SetPtpVlanGate_Type = IpAddress
_SetPtpVlanGate_Object = MibTableColumn
setPtpVlanGate = _SetPtpVlanGate_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 3, 23, 3, 1, 7),
    _SetPtpVlanGate_Type()
)
setPtpVlanGate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    setPtpVlanGate.setStatus("current")


class _SetPtpVlanId_Type(Integer32):
    """Custom type setPtpVlanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 4094),
    )


_SetPtpVlanId_Type.__name__ = "Integer32"
_SetPtpVlanId_Object = MibTableColumn
setPtpVlanId = _SetPtpVlanId_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 3, 23, 3, 1, 8),
    _SetPtpVlanId_Type()
)
setPtpVlanId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    setPtpVlanId.setStatus("current")


class _SetPtpVlanPriority_Type(Integer32):
    """Custom type setPtpVlanPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_SetPtpVlanPriority_Type.__name__ = "Integer32"
_SetPtpVlanPriority_Object = MibTableColumn
setPtpVlanPriority = _SetPtpVlanPriority_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 3, 23, 3, 1, 9),
    _SetPtpVlanPriority_Type()
)
setPtpVlanPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    setPtpVlanPriority.setStatus("current")
_SetupSynce_ObjectIdentity = ObjectIdentity
setupSynce = _SetupSynce_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 3, 24)
)
_SetSynceTable_Object = MibTable
setSynceTable = _SetSynceTable_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 3, 24, 1)
)
if mibBuilder.loadTexts:
    setSynceTable.setStatus("current")
_SetSynceEntry_Object = MibTableRow
setSynceEntry = _SetSynceEntry_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 3, 24, 1, 1)
)
setSynceEntry.setIndexNames(
    (0, "SSU2000-MIB", "setSynceChassis"),
    (0, "SSU2000-MIB", "setSynceSlot"),
)
if mibBuilder.loadTexts:
    setSynceEntry.setStatus("current")


class _SetSynceChassis_Type(Integer32):
    """Custom type setSynceChassis based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_SetSynceChassis_Type.__name__ = "Integer32"
_SetSynceChassis_Object = MibTableColumn
setSynceChassis = _SetSynceChassis_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 3, 24, 1, 1, 1),
    _SetSynceChassis_Type()
)
setSynceChassis.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    setSynceChassis.setStatus("current")


class _SetSynceSlot_Type(Integer32):
    """Custom type setSynceSlot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 20),
    )


_SetSynceSlot_Type.__name__ = "Integer32"
_SetSynceSlot_Object = MibTableColumn
setSynceSlot = _SetSynceSlot_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 3, 24, 1, 1, 2),
    _SetSynceSlot_Type()
)
setSynceSlot.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    setSynceSlot.setStatus("current")


class _SetSyncePortDirection_Type(Integer32):
    """Custom type setSyncePortDirection based on Integer32"""
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


_SetSyncePortDirection_Type.__name__ = "Integer32"
_SetSyncePortDirection_Object = MibTableColumn
setSyncePortDirection = _SetSyncePortDirection_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 3, 24, 1, 1, 3),
    _SetSyncePortDirection_Type()
)
setSyncePortDirection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    setSyncePortDirection.setStatus("current")
_SetSynceEsmc_Type = EnaValue
_SetSynceEsmc_Object = MibTableColumn
setSynceEsmc = _SetSynceEsmc_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 3, 24, 1, 1, 4),
    _SetSynceEsmc_Type()
)
setSynceEsmc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    setSynceEsmc.setStatus("current")
_SetSynceQl_Type = EnaValue
_SetSynceQl_Object = MibTableColumn
setSynceQl = _SetSynceQl_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 3, 24, 1, 1, 5),
    _SetSynceQl_Type()
)
setSynceQl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    setSynceQl.setStatus("current")


class _SetSynceOutQl_Type(Integer32):
    """Custom type setSynceOutQl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("bidirectional", 1),
          ("unidirectional", 2))
    )


_SetSynceOutQl_Type.__name__ = "Integer32"
_SetSynceOutQl_Object = MibTableColumn
setSynceOutQl = _SetSynceOutQl_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 3, 24, 1, 1, 6),
    _SetSynceOutQl_Type()
)
setSynceOutQl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    setSynceOutQl.setStatus("current")
_General_ObjectIdentity = ObjectIdentity
general = _General_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 4)
)
_InfoTable_Object = MibTable
infoTable = _InfoTable_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 4, 1)
)
if mibBuilder.loadTexts:
    infoTable.setStatus("current")
_GiEntry_Object = MibTableRow
giEntry = _GiEntry_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 4, 1, 1)
)
giEntry.setIndexNames(
    (0, "SSU2000-MIB", "giChassis"),
    (0, "SSU2000-MIB", "giSlot"),
)
if mibBuilder.loadTexts:
    giEntry.setStatus("current")


class _GiChassis_Type(Integer32):
    """Custom type giChassis based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_GiChassis_Type.__name__ = "Integer32"
_GiChassis_Object = MibTableColumn
giChassis = _GiChassis_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 4, 1, 1, 1),
    _GiChassis_Type()
)
giChassis.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    giChassis.setStatus("current")


class _GiSlot_Type(Integer32):
    """Custom type giSlot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 20),
    )


_GiSlot_Type.__name__ = "Integer32"
_GiSlot_Object = MibTableColumn
giSlot = _GiSlot_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 4, 1, 1, 2),
    _GiSlot_Type()
)
giSlot.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    giSlot.setStatus("current")
_GiSystime_Type = Counter32
_GiSystime_Object = MibTableColumn
giSystime = _GiSystime_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 4, 1, 1, 3),
    _GiSystime_Type()
)
giSystime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    giSystime.setStatus("current")


class _GiElevation_Type(Integer32):
    """Custom type giElevation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(60, 500000),
    )


_GiElevation_Type.__name__ = "Integer32"
_GiElevation_Object = MibTableColumn
giElevation = _GiElevation_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 4, 1, 1, 4),
    _GiElevation_Type()
)
giElevation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    giElevation.setStatus("current")


class _GiSetup_Type(Integer32):
    """Custom type giSetup based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("factory", 1),
          ("user", 2),
          ("save", 3))
    )


_GiSetup_Type.__name__ = "Integer32"
_GiSetup_Object = MibTableColumn
giSetup = _GiSetup_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 4, 1, 1, 5),
    _GiSetup_Type()
)
giSetup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    giSetup.setStatus("current")
_GiRestart_Type = YesValue
_GiRestart_Object = MibTableColumn
giRestart = _GiRestart_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 4, 1, 1, 6),
    _GiRestart_Type()
)
giRestart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    giRestart.setStatus("current")
_Event_ObjectIdentity = ObjectIdentity
event = _Event_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 5)
)


class _EvCount_Type(Integer32):
    """Custom type evCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1000),
    )


_EvCount_Type.__name__ = "Integer32"
_EvCount_Object = MibScalar
evCount = _EvCount_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 5, 1),
    _EvCount_Type()
)
evCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    evCount.setStatus("current")


class _EvType_Type(Integer32):
    """Custom type evType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("alarm", 1),
          ("report", 2),
          ("all", 3))
    )


_EvType_Type.__name__ = "Integer32"
_EvType_Object = MibScalar
evType = _EvType_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 5, 2),
    _EvType_Type()
)
evType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    evType.setStatus("current")
_EventTable_Object = MibTable
eventTable = _EventTable_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 5, 3)
)
if mibBuilder.loadTexts:
    eventTable.setStatus("current")
_EvEntry_Object = MibTableRow
evEntry = _EvEntry_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 5, 3, 1)
)
evEntry.setIndexNames(
    (0, "SSU2000-MIB", "evIndex"),
)
if mibBuilder.loadTexts:
    evEntry.setStatus("current")


class _EvIndex_Type(Integer32):
    """Custom type evIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1000),
    )


_EvIndex_Type.__name__ = "Integer32"
_EvIndex_Object = MibTableColumn
evIndex = _EvIndex_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 5, 3, 1, 1),
    _EvIndex_Type()
)
evIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    evIndex.setStatus("current")


class _EvT_Type(OctetString):
    """Custom type evT based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(36, 116),
    )


_EvT_Type.__name__ = "OctetString"
_EvT_Object = MibTableColumn
evT = _EvT_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 5, 3, 1, 2),
    _EvT_Type()
)
evT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    evT.setStatus("current")
_Alarm_ObjectIdentity = ObjectIdentity
alarm = _Alarm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 6)
)
_AlarmTable_Object = MibTable
alarmTable = _AlarmTable_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 6, 1)
)
if mibBuilder.loadTexts:
    alarmTable.setStatus("current")
_AlmEntry_Object = MibTableRow
almEntry = _AlmEntry_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 6, 1, 1)
)
almEntry.setIndexNames(
    (0, "SSU2000-MIB", "almChassis"),
    (0, "SSU2000-MIB", "almSlot"),
    (0, "SSU2000-MIB", "almPort"),
    (0, "SSU2000-MIB", "almIndex"),
)
if mibBuilder.loadTexts:
    almEntry.setStatus("current")


class _AlmChassis_Type(Integer32):
    """Custom type almChassis based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_AlmChassis_Type.__name__ = "Integer32"
_AlmChassis_Object = MibTableColumn
almChassis = _AlmChassis_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 6, 1, 1, 1),
    _AlmChassis_Type()
)
almChassis.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    almChassis.setStatus("current")


class _AlmSlot_Type(Integer32):
    """Custom type almSlot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 20),
    )


_AlmSlot_Type.__name__ = "Integer32"
_AlmSlot_Object = MibTableColumn
almSlot = _AlmSlot_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 6, 1, 1, 2),
    _AlmSlot_Type()
)
almSlot.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    almSlot.setStatus("current")


class _AlmPort_Type(Integer32):
    """Custom type almPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_AlmPort_Type.__name__ = "Integer32"
_AlmPort_Object = MibTableColumn
almPort = _AlmPort_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 6, 1, 1, 3),
    _AlmPort_Type()
)
almPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    almPort.setStatus("current")


class _AlmIndex_Type(Integer32):
    """Custom type almIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_AlmIndex_Type.__name__ = "Integer32"
_AlmIndex_Object = MibTableColumn
almIndex = _AlmIndex_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 6, 1, 1, 4),
    _AlmIndex_Type()
)
almIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    almIndex.setStatus("current")


class _AlmId_Type(Integer32):
    """Custom type almId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 31),
    )


_AlmId_Type.__name__ = "Integer32"
_AlmId_Object = MibTableColumn
almId = _AlmId_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 6, 1, 1, 5),
    _AlmId_Type()
)
almId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    almId.setStatus("current")


class _AlmName_Type(DisplayString):
    """Custom type almName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_AlmName_Type.__name__ = "DisplayString"
_AlmName_Object = MibTableColumn
almName = _AlmName_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 6, 1, 1, 6),
    _AlmName_Type()
)
almName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    almName.setStatus("current")


class _AlmLevel_Type(Integer32):
    """Custom type almLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("minor", 1),
          ("major", 2),
          ("critical", 3),
          ("ignore", 4),
          ("report", 5),
          ("clear", 6))
    )


_AlmLevel_Type.__name__ = "Integer32"
_AlmLevel_Object = MibTableColumn
almLevel = _AlmLevel_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 6, 1, 1, 7),
    _AlmLevel_Type()
)
almLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    almLevel.setStatus("current")
_AlmElevate_Type = YesValue
_AlmElevate_Object = MibTableColumn
almElevate = _AlmElevate_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 6, 1, 1, 8),
    _AlmElevate_Type()
)
almElevate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    almElevate.setStatus("current")


class _AlmStatus_Type(DisplayString):
    """Custom type almStatus based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_AlmStatus_Type.__name__ = "DisplayString"
_AlmStatus_Object = MibTableColumn
almStatus = _AlmStatus_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 6, 1, 1, 9),
    _AlmStatus_Type()
)
almStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    almStatus.setStatus("current")


class _SetAlmLoc_Type(DisplayString):
    """Custom type setAlmLoc based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_SetAlmLoc_Type.__name__ = "DisplayString"
_SetAlmLoc_Object = MibScalar
setAlmLoc = _SetAlmLoc_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 6, 2),
    _SetAlmLoc_Type()
)
setAlmLoc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    setAlmLoc.setStatus("current")
_SetAlmTable_Object = MibTable
setAlmTable = _SetAlmTable_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 6, 3)
)
if mibBuilder.loadTexts:
    setAlmTable.setStatus("current")
_SalEntry_Object = MibTableRow
salEntry = _SalEntry_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 6, 3, 1)
)
salEntry.setIndexNames(
    (0, "SSU2000-MIB", "salChassis"),
    (0, "SSU2000-MIB", "salSlot"),
    (0, "SSU2000-MIB", "salPort"),
    (0, "SSU2000-MIB", "salIndex"),
)
if mibBuilder.loadTexts:
    salEntry.setStatus("current")


class _SalChassis_Type(Integer32):
    """Custom type salChassis based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_SalChassis_Type.__name__ = "Integer32"
_SalChassis_Object = MibTableColumn
salChassis = _SalChassis_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 6, 3, 1, 1),
    _SalChassis_Type()
)
salChassis.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    salChassis.setStatus("current")


class _SalSlot_Type(Integer32):
    """Custom type salSlot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 20),
    )


_SalSlot_Type.__name__ = "Integer32"
_SalSlot_Object = MibTableColumn
salSlot = _SalSlot_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 6, 3, 1, 2),
    _SalSlot_Type()
)
salSlot.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    salSlot.setStatus("current")


class _SalPort_Type(Integer32):
    """Custom type salPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_SalPort_Type.__name__ = "Integer32"
_SalPort_Object = MibTableColumn
salPort = _SalPort_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 6, 3, 1, 3),
    _SalPort_Type()
)
salPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    salPort.setStatus("current")


class _SalIndex_Type(Integer32):
    """Custom type salIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_SalIndex_Type.__name__ = "Integer32"
_SalIndex_Object = MibTableColumn
salIndex = _SalIndex_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 6, 3, 1, 4),
    _SalIndex_Type()
)
salIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    salIndex.setStatus("current")


class _SalId_Type(Integer32):
    """Custom type salId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 31),
    )


_SalId_Type.__name__ = "Integer32"
_SalId_Object = MibTableColumn
salId = _SalId_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 6, 3, 1, 5),
    _SalId_Type()
)
salId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    salId.setStatus("current")


class _SalName_Type(DisplayString):
    """Custom type salName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_SalName_Type.__name__ = "DisplayString"
_SalName_Object = MibTableColumn
salName = _SalName_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 6, 3, 1, 6),
    _SalName_Type()
)
salName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    salName.setStatus("current")
_SalSet_Type = YesValue
_SalSet_Object = MibTableColumn
salSet = _SalSet_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 6, 3, 1, 7),
    _SalSet_Type()
)
salSet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    salSet.setStatus("current")
_SalElevate_Type = YesValue
_SalElevate_Object = MibTableColumn
salElevate = _SalElevate_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 6, 3, 1, 8),
    _SalElevate_Type()
)
salElevate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    salElevate.setStatus("current")


class _SalLevel_Type(Integer32):
    """Custom type salLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("minor", 1),
          ("major", 2),
          ("critical", 3),
          ("ignore", 4),
          ("report", 5))
    )


_SalLevel_Type.__name__ = "Integer32"
_SalLevel_Object = MibTableColumn
salLevel = _SalLevel_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 6, 3, 1, 9),
    _SalLevel_Type()
)
salLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    salLevel.setStatus("current")


class _SalDelay_Type(Integer32):
    """Custom type salDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 86400),
    )


_SalDelay_Type.__name__ = "Integer32"
_SalDelay_Object = MibTableColumn
salDelay = _SalDelay_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 6, 3, 1, 10),
    _SalDelay_Type()
)
salDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    salDelay.setStatus("current")
_Ref_ObjectIdentity = ObjectIdentity
ref = _Ref_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 7)
)


class _RefClk_Type(Integer32):
    """Custom type refClk based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("clka", 1),
          ("clkb", 2),
          ("none", 3))
    )


_RefClk_Type.__name__ = "Integer32"
_RefClk_Object = MibScalar
refClk = _RefClk_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 7, 1),
    _RefClk_Type()
)
refClk.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    refClk.setStatus("current")


class _RefInp_Type(DisplayString):
    """Custom type refInp based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_RefInp_Type.__name__ = "DisplayString"
_RefInp_Object = MibScalar
refInp = _RefInp_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 7, 2),
    _RefInp_Type()
)
refInp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    refInp.setStatus("current")


class _RefBypass_Type(DisplayString):
    """Custom type refBypass based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_RefBypass_Type.__name__ = "DisplayString"
_RefBypass_Object = MibScalar
refBypass = _RefBypass_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 7, 3),
    _RefBypass_Type()
)
refBypass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    refBypass.setStatus("current")


class _RefClkSwitch_Type(Integer32):
    """Custom type refClkSwitch based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ar", 1),
          ("off", 2))
    )


_RefClkSwitch_Type.__name__ = "Integer32"
_RefClkSwitch_Object = MibScalar
refClkSwitch = _RefClkSwitch_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 7, 4),
    _RefClkSwitch_Type()
)
refClkSwitch.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    refClkSwitch.setStatus("current")


class _RefInpSwitch_Type(Integer32):
    """Custom type refInpSwitch based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("ar", 1),
          ("as", 2),
          ("off", 3))
    )


_RefInpSwitch_Type.__name__ = "Integer32"
_RefInpSwitch_Object = MibScalar
refInpSwitch = _RefInpSwitch_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 7, 5),
    _RefInpSwitch_Type()
)
refInpSwitch.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    refInpSwitch.setStatus("current")


class _RefInpSelection_Type(Integer32):
    """Custom type refInpSelection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("priority", 1),
          ("pql", 2))
    )


_RefInpSelection_Type.__name__ = "Integer32"
_RefInpSelection_Object = MibScalar
refInpSelection = _RefInpSelection_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 7, 6),
    _RefInpSelection_Type()
)
refInpSelection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    refInpSelection.setStatus("current")


class _RefClkTodsrc_Type(DisplayString):
    """Custom type refClkTodsrc based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_RefClkTodsrc_Type.__name__ = "DisplayString"
_RefClkTodsrc_Object = MibScalar
refClkTodsrc = _RefClkTodsrc_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 7, 7),
    _RefClkTodsrc_Type()
)
refClkTodsrc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    refClkTodsrc.setStatus("current")
_Phase_ObjectIdentity = ObjectIdentity
phase = _Phase_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 8)
)
_PhaseTable_Object = MibTable
phaseTable = _PhaseTable_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 8, 1)
)
if mibBuilder.loadTexts:
    phaseTable.setStatus("current")
_PhEntry_Object = MibTableRow
phEntry = _PhEntry_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 8, 1, 1)
)
phEntry.setIndexNames(
    (0, "SSU2000-MIB", "phChassis"),
    (0, "SSU2000-MIB", "phSlot"),
    (0, "SSU2000-MIB", "phPort"),
)
if mibBuilder.loadTexts:
    phEntry.setStatus("current")


class _PhChassis_Type(Integer32):
    """Custom type phChassis based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
    )


_PhChassis_Type.__name__ = "Integer32"
_PhChassis_Object = MibTableColumn
phChassis = _PhChassis_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 8, 1, 1, 1),
    _PhChassis_Type()
)
phChassis.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    phChassis.setStatus("current")


class _PhSlot_Type(Integer32):
    """Custom type phSlot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 20),
    )


_PhSlot_Type.__name__ = "Integer32"
_PhSlot_Object = MibTableColumn
phSlot = _PhSlot_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 8, 1, 1, 2),
    _PhSlot_Type()
)
phSlot.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    phSlot.setStatus("current")


class _PhPort_Type(Integer32):
    """Custom type phPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_PhPort_Type.__name__ = "Integer32"
_PhPort_Object = MibTableColumn
phPort = _PhPort_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 8, 1, 1, 3),
    _PhPort_Type()
)
phPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    phPort.setStatus("current")


class _PhA_Type(OctetString):
    """Custom type phA based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )
    fixed_length = 16


_PhA_Type.__name__ = "OctetString"
_PhA_Object = MibTableColumn
phA = _PhA_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 8, 1, 1, 4),
    _PhA_Type()
)
phA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    phA.setStatus("current")


class _PhB_Type(OctetString):
    """Custom type phB based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )
    fixed_length = 16


_PhB_Type.__name__ = "OctetString"
_PhB_Object = MibTableColumn
phB = _PhB_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 8, 1, 1, 5),
    _PhB_Type()
)
phB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    phB.setStatus("current")


class _Ph100A_Type(OctetString):
    """Custom type ph100A based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )
    fixed_length = 16


_Ph100A_Type.__name__ = "OctetString"
_Ph100A_Object = MibTableColumn
ph100A = _Ph100A_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 8, 1, 1, 6),
    _Ph100A_Type()
)
ph100A.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ph100A.setStatus("current")


class _Ph100B_Type(OctetString):
    """Custom type ph100B based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )
    fixed_length = 16


_Ph100B_Type.__name__ = "OctetString"
_Ph100B_Object = MibTableColumn
ph100B = _Ph100B_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 8, 1, 1, 7),
    _Ph100B_Type()
)
ph100B.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ph100B.setStatus("current")


class _Ph1000A_Type(OctetString):
    """Custom type ph1000A based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )
    fixed_length = 16


_Ph1000A_Type.__name__ = "OctetString"
_Ph1000A_Object = MibTableColumn
ph1000A = _Ph1000A_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 8, 1, 1, 8),
    _Ph1000A_Type()
)
ph1000A.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ph1000A.setStatus("current")


class _Ph1000B_Type(OctetString):
    """Custom type ph1000B based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )
    fixed_length = 16


_Ph1000B_Type.__name__ = "OctetString"
_Ph1000B_Object = MibTableColumn
ph1000B = _Ph1000B_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 8, 1, 1, 9),
    _Ph1000B_Type()
)
ph1000B.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ph1000B.setStatus("current")


class _Ph10000A_Type(OctetString):
    """Custom type ph10000A based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )
    fixed_length = 16


_Ph10000A_Type.__name__ = "OctetString"
_Ph10000A_Object = MibTableColumn
ph10000A = _Ph10000A_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 8, 1, 1, 10),
    _Ph10000A_Type()
)
ph10000A.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ph10000A.setStatus("current")


class _Ph10000B_Type(OctetString):
    """Custom type ph10000B based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )
    fixed_length = 16


_Ph10000B_Type.__name__ = "OctetString"
_Ph10000B_Object = MibTableColumn
ph10000B = _Ph10000B_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 8, 1, 1, 11),
    _Ph10000B_Type()
)
ph10000B.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ph10000B.setStatus("current")


class _PhHisInpLoc_Type(DisplayString):
    """Custom type phHisInpLoc based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_PhHisInpLoc_Type.__name__ = "DisplayString"
_PhHisInpLoc_Object = MibScalar
phHisInpLoc = _PhHisInpLoc_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 8, 2),
    _PhHisInpLoc_Type()
)
phHisInpLoc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    phHisInpLoc.setStatus("current")


class _PhHisTimeAvg_Type(Integer32):
    """Custom type phHisTimeAvg based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(100,
              1000,
              10000)
        )
    )
    namedValues = NamedValues(
        *(("t100", 100),
          ("t1000", 1000),
          ("t10000", 10000))
    )


_PhHisTimeAvg_Type.__name__ = "Integer32"
_PhHisTimeAvg_Object = MibScalar
phHisTimeAvg = _PhHisTimeAvg_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 8, 3),
    _PhHisTimeAvg_Type()
)
phHisTimeAvg.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    phHisTimeAvg.setStatus("current")


class _PhHisClk_Type(Integer32):
    """Custom type phHisClk based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("clka", 1),
          ("clkb", 2))
    )


_PhHisClk_Type.__name__ = "Integer32"
_PhHisClk_Object = MibScalar
phHisClk = _PhHisClk_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 8, 4),
    _PhHisClk_Type()
)
phHisClk.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    phHisClk.setStatus("current")


class _PhHisCnt_Type(Integer32):
    """Custom type phHisCnt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 7000),
    )


_PhHisCnt_Type.__name__ = "Integer32"
_PhHisCnt_Object = MibScalar
phHisCnt = _PhHisCnt_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 8, 5),
    _PhHisCnt_Type()
)
phHisCnt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    phHisCnt.setStatus("current")
_PhHisTable_Object = MibTable
phHisTable = _PhHisTable_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 8, 6)
)
if mibBuilder.loadTexts:
    phHisTable.setStatus("current")
_PhHisEntry_Object = MibTableRow
phHisEntry = _PhHisEntry_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 8, 6, 1)
)
phHisEntry.setIndexNames(
    (0, "SSU2000-MIB", "phHisChassis"),
    (0, "SSU2000-MIB", "phHisSlot"),
    (0, "SSU2000-MIB", "phHisPort"),
    (0, "SSU2000-MIB", "phHisIndex"),
)
if mibBuilder.loadTexts:
    phHisEntry.setStatus("current")


class _PhHisChassis_Type(Integer32):
    """Custom type phHisChassis based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
    )


_PhHisChassis_Type.__name__ = "Integer32"
_PhHisChassis_Object = MibTableColumn
phHisChassis = _PhHisChassis_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 8, 6, 1, 1),
    _PhHisChassis_Type()
)
phHisChassis.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    phHisChassis.setStatus("current")


class _PhHisSlot_Type(Integer32):
    """Custom type phHisSlot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 20),
    )


_PhHisSlot_Type.__name__ = "Integer32"
_PhHisSlot_Object = MibTableColumn
phHisSlot = _PhHisSlot_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 8, 6, 1, 2),
    _PhHisSlot_Type()
)
phHisSlot.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    phHisSlot.setStatus("current")


class _PhHisPort_Type(Integer32):
    """Custom type phHisPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_PhHisPort_Type.__name__ = "Integer32"
_PhHisPort_Object = MibTableColumn
phHisPort = _PhHisPort_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 8, 6, 1, 3),
    _PhHisPort_Type()
)
phHisPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    phHisPort.setStatus("current")


class _PhHisIndex_Type(Integer32):
    """Custom type phHisIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 7000),
    )


_PhHisIndex_Type.__name__ = "Integer32"
_PhHisIndex_Object = MibTableColumn
phHisIndex = _PhHisIndex_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 8, 6, 1, 4),
    _PhHisIndex_Type()
)
phHisIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    phHisIndex.setStatus("current")


class _PhHisV_Type(OctetString):
    """Custom type phHisV based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )
    fixed_length = 16


_PhHisV_Type.__name__ = "OctetString"
_PhHisV_Object = MibTableColumn
phHisV = _PhHisV_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 8, 6, 1, 5),
    _PhHisV_Type()
)
phHisV.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    phHisV.setStatus("current")
_Freq_ObjectIdentity = ObjectIdentity
freq = _Freq_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 9)
)
_FreqTable_Object = MibTable
freqTable = _FreqTable_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 9, 1)
)
if mibBuilder.loadTexts:
    freqTable.setStatus("current")
_FqEntry_Object = MibTableRow
fqEntry = _FqEntry_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 9, 1, 1)
)
fqEntry.setIndexNames(
    (0, "SSU2000-MIB", "fqChassis"),
    (0, "SSU2000-MIB", "fqSlot"),
    (0, "SSU2000-MIB", "fqPort"),
)
if mibBuilder.loadTexts:
    fqEntry.setStatus("current")


class _FqChassis_Type(Integer32):
    """Custom type fqChassis based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
    )


_FqChassis_Type.__name__ = "Integer32"
_FqChassis_Object = MibTableColumn
fqChassis = _FqChassis_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 9, 1, 1, 1),
    _FqChassis_Type()
)
fqChassis.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fqChassis.setStatus("current")


class _FqSlot_Type(Integer32):
    """Custom type fqSlot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 20),
    )


_FqSlot_Type.__name__ = "Integer32"
_FqSlot_Object = MibTableColumn
fqSlot = _FqSlot_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 9, 1, 1, 2),
    _FqSlot_Type()
)
fqSlot.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fqSlot.setStatus("current")


class _FqPort_Type(Integer32):
    """Custom type fqPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_FqPort_Type.__name__ = "Integer32"
_FqPort_Object = MibTableColumn
fqPort = _FqPort_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 9, 1, 1, 3),
    _FqPort_Type()
)
fqPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fqPort.setStatus("current")


class _FqA_Type(OctetString):
    """Custom type fqA based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )
    fixed_length = 16


_FqA_Type.__name__ = "OctetString"
_FqA_Object = MibTableColumn
fqA = _FqA_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 9, 1, 1, 4),
    _FqA_Type()
)
fqA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fqA.setStatus("current")


class _FqB_Type(OctetString):
    """Custom type fqB based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )
    fixed_length = 16


_FqB_Type.__name__ = "OctetString"
_FqB_Object = MibTableColumn
fqB = _FqB_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 9, 1, 1, 5),
    _FqB_Type()
)
fqB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fqB.setStatus("current")
_Ntp_ObjectIdentity = ObjectIdentity
ntp = _Ntp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 10)
)


class _NtpMode_Type(Integer32):
    """Custom type ntpMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("server", 1),
          ("client", 2),
          ("local", 3))
    )


_NtpMode_Type.__name__ = "Integer32"
_NtpMode_Object = MibScalar
ntpMode = _NtpMode_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 10, 1),
    _NtpMode_Type()
)
ntpMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntpMode.setStatus("current")
_NtpSysPeer_Type = IpAddress
_NtpSysPeer_Object = MibScalar
ntpSysPeer = _NtpSysPeer_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 10, 2),
    _NtpSysPeer_Type()
)
ntpSysPeer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntpSysPeer.setStatus("current")


class _NtpSysPeerOffset_Type(DisplayString):
    """Custom type ntpSysPeerOffset based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_NtpSysPeerOffset_Type.__name__ = "DisplayString"
_NtpSysPeerOffset_Object = MibScalar
ntpSysPeerOffset = _NtpSysPeerOffset_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 10, 3),
    _NtpSysPeerOffset_Type()
)
ntpSysPeerOffset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntpSysPeerOffset.setStatus("current")
_PeerStaTable_Object = MibTable
peerStaTable = _PeerStaTable_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 10, 4)
)
if mibBuilder.loadTexts:
    peerStaTable.setStatus("current")
_PeerStaEntry_Object = MibTableRow
peerStaEntry = _PeerStaEntry_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 10, 4, 1)
)
peerStaEntry.setIndexNames(
    (0, "SSU2000-MIB", "peerStaIndex"),
)
if mibBuilder.loadTexts:
    peerStaEntry.setStatus("current")


class _PeerStaIndex_Type(Integer32):
    """Custom type peerStaIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_PeerStaIndex_Type.__name__ = "Integer32"
_PeerStaIndex_Object = MibTableColumn
peerStaIndex = _PeerStaIndex_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 10, 4, 1, 1),
    _PeerStaIndex_Type()
)
peerStaIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    peerStaIndex.setStatus("current")
_PeerStaAddress_Type = IpAddress
_PeerStaAddress_Object = MibTableColumn
peerStaAddress = _PeerStaAddress_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 10, 4, 1, 2),
    _PeerStaAddress_Type()
)
peerStaAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    peerStaAddress.setStatus("current")


class _PeerStaHomeMode_Type(Integer32):
    """Custom type peerStaHomeMode based on Integer32"""
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
              7,
              8)
        )
    )
    namedValues = NamedValues(
        *(("unspect", 0),
          ("active", 1),
          ("passive", 2),
          ("client", 3),
          ("server", 4),
          ("broadcast", 5),
          ("control", 6),
          ("private", 7),
          ("bclient", 8))
    )


_PeerStaHomeMode_Type.__name__ = "Integer32"
_PeerStaHomeMode_Object = MibTableColumn
peerStaHomeMode = _PeerStaHomeMode_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 10, 4, 1, 3),
    _PeerStaHomeMode_Type()
)
peerStaHomeMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    peerStaHomeMode.setStatus("current")


class _PeerStaParentMode_Type(Integer32):
    """Custom type peerStaParentMode based on Integer32"""
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
              7,
              8)
        )
    )
    namedValues = NamedValues(
        *(("unspect", 0),
          ("active", 1),
          ("passive", 2),
          ("client", 3),
          ("server", 4),
          ("broadcast", 5),
          ("control", 6),
          ("private", 7),
          ("bclient", 8))
    )


_PeerStaParentMode_Type.__name__ = "Integer32"
_PeerStaParentMode_Object = MibTableColumn
peerStaParentMode = _PeerStaParentMode_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 10, 4, 1, 4),
    _PeerStaParentMode_Type()
)
peerStaParentMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    peerStaParentMode.setStatus("current")


class _PeerStaLeap_Type(Integer32):
    """Custom type peerStaLeap based on Integer32"""
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
        *(("nowarning", 0),
          ("addsec", 1),
          ("delsec", 2),
          ("notinsync", 3))
    )


_PeerStaLeap_Type.__name__ = "Integer32"
_PeerStaLeap_Object = MibTableColumn
peerStaLeap = _PeerStaLeap_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 10, 4, 1, 5),
    _PeerStaLeap_Type()
)
peerStaLeap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    peerStaLeap.setStatus("current")


class _PeerStaStratum_Type(Integer32):
    """Custom type peerStaStratum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 16),
    )


_PeerStaStratum_Type.__name__ = "Integer32"
_PeerStaStratum_Object = MibTableColumn
peerStaStratum = _PeerStaStratum_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 10, 4, 1, 6),
    _PeerStaStratum_Type()
)
peerStaStratum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    peerStaStratum.setStatus("current")


class _PeerStaPrecision_Type(Integer32):
    """Custom type peerStaPrecision based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1000, 1000),
    )


_PeerStaPrecision_Type.__name__ = "Integer32"
_PeerStaPrecision_Object = MibTableColumn
peerStaPrecision = _PeerStaPrecision_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 10, 4, 1, 7),
    _PeerStaPrecision_Type()
)
peerStaPrecision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    peerStaPrecision.setStatus("current")


class _PeerStaDelay_Type(DisplayString):
    """Custom type peerStaDelay based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_PeerStaDelay_Type.__name__ = "DisplayString"
_PeerStaDelay_Object = MibTableColumn
peerStaDelay = _PeerStaDelay_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 10, 4, 1, 8),
    _PeerStaDelay_Type()
)
peerStaDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    peerStaDelay.setStatus("current")


class _PeerStaDispersion_Type(DisplayString):
    """Custom type peerStaDispersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_PeerStaDispersion_Type.__name__ = "DisplayString"
_PeerStaDispersion_Object = MibTableColumn
peerStaDispersion = _PeerStaDispersion_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 10, 4, 1, 9),
    _PeerStaDispersion_Type()
)
peerStaDispersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    peerStaDispersion.setStatus("current")


class _PeerStaOffset_Type(DisplayString):
    """Custom type peerStaOffset based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_PeerStaOffset_Type.__name__ = "DisplayString"
_PeerStaOffset_Object = MibTableColumn
peerStaOffset = _PeerStaOffset_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 10, 4, 1, 10),
    _PeerStaOffset_Type()
)
peerStaOffset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    peerStaOffset.setStatus("current")
_PeerStaSentCnt_Type = Counter32
_PeerStaSentCnt_Object = MibTableColumn
peerStaSentCnt = _PeerStaSentCnt_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 10, 4, 1, 11),
    _PeerStaSentCnt_Type()
)
peerStaSentCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    peerStaSentCnt.setStatus("current")
_PeerStaProcessCnt_Type = Counter32
_PeerStaProcessCnt_Object = MibTableColumn
peerStaProcessCnt = _PeerStaProcessCnt_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 10, 4, 1, 12),
    _PeerStaProcessCnt_Type()
)
peerStaProcessCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    peerStaProcessCnt.setStatus("current")
_PeerStaSanity_Type = YesValue
_PeerStaSanity_Object = MibTableColumn
peerStaSanity = _PeerStaSanity_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 10, 4, 1, 13),
    _PeerStaSanity_Type()
)
peerStaSanity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    peerStaSanity.setStatus("current")
_NtpTable_Object = MibTable
ntpTable = _NtpTable_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 10, 5)
)
if mibBuilder.loadTexts:
    ntpTable.setStatus("current")
_NtpEntry_Object = MibTableRow
ntpEntry = _NtpEntry_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 10, 5, 1)
)
ntpEntry.setIndexNames(
    (0, "SSU2000-MIB", "ntpIndex"),
)
if mibBuilder.loadTexts:
    ntpEntry.setStatus("current")


class _NtpIndex_Type(Integer32):
    """Custom type ntpIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_NtpIndex_Type.__name__ = "Integer32"
_NtpIndex_Object = MibTableColumn
ntpIndex = _NtpIndex_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 10, 5, 1, 1),
    _NtpIndex_Type()
)
ntpIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ntpIndex.setStatus("current")
_NtpPeer_Type = IpAddress
_NtpPeer_Object = MibTableColumn
ntpPeer = _NtpPeer_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 10, 5, 1, 2),
    _NtpPeer_Type()
)
ntpPeer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntpPeer.setStatus("current")


class _NtpPeerType_Type(Integer32):
    """Custom type ntpPeerType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("client", 1),
          ("broadcast", 2),
          ("bclient", 3))
    )


_NtpPeerType_Type.__name__ = "Integer32"
_NtpPeerType_Object = MibTableColumn
ntpPeerType = _NtpPeerType_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 10, 5, 1, 3),
    _NtpPeerType_Type()
)
ntpPeerType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntpPeerType.setStatus("current")


class _NtpBrdTimer_Type(Integer32):
    """Custom type ntpBrdTimer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              32,
              64,
              128,
              256,
              512,
              1024)
        )
    )
    namedValues = NamedValues(
        *(("notuse", 0),
          ("t32", 32),
          ("t64", 64),
          ("t128", 128),
          ("t256", 256),
          ("t512", 512),
          ("t1024", 1024))
    )


_NtpBrdTimer_Type.__name__ = "Integer32"
_NtpBrdTimer_Object = MibTableColumn
ntpBrdTimer = _NtpBrdTimer_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 10, 5, 1, 4),
    _NtpBrdTimer_Type()
)
ntpBrdTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntpBrdTimer.setStatus("current")
_NtpAddClient_Type = IpAddress
_NtpAddClient_Object = MibScalar
ntpAddClient = _NtpAddClient_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 10, 6),
    _NtpAddClient_Type()
)
ntpAddClient.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntpAddClient.setStatus("current")
_NtpAddBrd_Type = IpAddress
_NtpAddBrd_Object = MibScalar
ntpAddBrd = _NtpAddBrd_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 10, 7),
    _NtpAddBrd_Type()
)
ntpAddBrd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntpAddBrd.setStatus("current")
_NtpAddBclient_Type = IpAddress
_NtpAddBclient_Object = MibScalar
ntpAddBclient = _NtpAddBclient_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 10, 8),
    _NtpAddBclient_Type()
)
ntpAddBclient.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntpAddBclient.setStatus("current")
_NtpDelPeer_Type = IpAddress
_NtpDelPeer_Object = MibScalar
ntpDelPeer = _NtpDelPeer_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 10, 9),
    _NtpDelPeer_Type()
)
ntpDelPeer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntpDelPeer.setStatus("current")


class _NtpClr_Type(Integer32):
    """Custom type ntpClr based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("clr", 1)
    )


_NtpClr_Type.__name__ = "Integer32"
_NtpClr_Object = MibScalar
ntpClr = _NtpClr_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 10, 10),
    _NtpClr_Type()
)
ntpClr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntpClr.setStatus("current")


class _NtpBTimer_Type(Integer32):
    """Custom type ntpBTimer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(32,
              64,
              128,
              256,
              512,
              1024)
        )
    )
    namedValues = NamedValues(
        *(("t32", 32),
          ("t64", 64),
          ("t128", 128),
          ("t256", 256),
          ("t512", 512),
          ("t1024", 1024))
    )


_NtpBTimer_Type.__name__ = "Integer32"
_NtpBTimer_Object = MibScalar
ntpBTimer = _NtpBTimer_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 10, 11),
    _NtpBTimer_Type()
)
ntpBTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntpBTimer.setStatus("current")


class _NtpPrefer_Type(Integer32):
    """Custom type ntpPrefer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("gps", 1),
          ("client", 2))
    )


_NtpPrefer_Type.__name__ = "Integer32"
_NtpPrefer_Object = MibScalar
ntpPrefer = _NtpPrefer_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 10, 12),
    _NtpPrefer_Type()
)
ntpPrefer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntpPrefer.setStatus("current")
_Time_ObjectIdentity = ObjectIdentity
time = _Time_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 11)
)
_TmCurTime_Type = DateAndTime
_TmCurTime_Object = MibScalar
tmCurTime = _TmCurTime_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 11, 1),
    _TmCurTime_Type()
)
tmCurTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmCurTime.setStatus("current")
_TmLocalOffset_Type = TLocalTimeOffset
_TmLocalOffset_Object = MibScalar
tmLocalOffset = _TmLocalOffset_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 11, 2),
    _TmLocalOffset_Type()
)
tmLocalOffset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmLocalOffset.setStatus("current")
_PqlTable_ObjectIdentity = ObjectIdentity
pqlTable = _PqlTable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 12)
)
_PqlDs1Table_Object = MibTable
pqlDs1Table = _PqlDs1Table_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 12, 1)
)
if mibBuilder.loadTexts:
    pqlDs1Table.setStatus("current")
_PqlDs1Entry_Object = MibTableRow
pqlDs1Entry = _PqlDs1Entry_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 12, 1, 1)
)
pqlDs1Entry.setIndexNames(
    (0, "SSU2000-MIB", "pqlDs1Index"),
)
if mibBuilder.loadTexts:
    pqlDs1Entry.setStatus("current")


class _PqlDs1Index_Type(Integer32):
    """Custom type pqlDs1Index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_PqlDs1Index_Type.__name__ = "Integer32"
_PqlDs1Index_Object = MibTableColumn
pqlDs1Index = _PqlDs1Index_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 12, 1, 1, 1),
    _PqlDs1Index_Type()
)
pqlDs1Index.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pqlDs1Index.setStatus("current")
_PqlDs1Ssm_Type = TSsm
_PqlDs1Ssm_Object = MibTableColumn
pqlDs1Ssm = _PqlDs1Ssm_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 12, 1, 1, 2),
    _PqlDs1Ssm_Type()
)
pqlDs1Ssm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pqlDs1Ssm.setStatus("current")


class _PqlDs1Descr_Type(DisplayString):
    """Custom type pqlDs1Descr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 14),
    )


_PqlDs1Descr_Type.__name__ = "DisplayString"
_PqlDs1Descr_Object = MibTableColumn
pqlDs1Descr = _PqlDs1Descr_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 12, 1, 1, 3),
    _PqlDs1Descr_Type()
)
pqlDs1Descr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pqlDs1Descr.setStatus("current")
_PqlE1Table_Object = MibTable
pqlE1Table = _PqlE1Table_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 12, 2)
)
if mibBuilder.loadTexts:
    pqlE1Table.setStatus("current")
_PqlE1Entry_Object = MibTableRow
pqlE1Entry = _PqlE1Entry_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 12, 2, 1)
)
pqlE1Entry.setIndexNames(
    (0, "SSU2000-MIB", "pqlE1Index"),
)
if mibBuilder.loadTexts:
    pqlE1Entry.setStatus("current")


class _PqlE1Index_Type(Integer32):
    """Custom type pqlE1Index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_PqlE1Index_Type.__name__ = "Integer32"
_PqlE1Index_Object = MibTableColumn
pqlE1Index = _PqlE1Index_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 12, 2, 1, 1),
    _PqlE1Index_Type()
)
pqlE1Index.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pqlE1Index.setStatus("current")
_PqlE1Ssm_Type = TSsm
_PqlE1Ssm_Object = MibTableColumn
pqlE1Ssm = _PqlE1Ssm_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 12, 2, 1, 2),
    _PqlE1Ssm_Type()
)
pqlE1Ssm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pqlE1Ssm.setStatus("current")


class _PqlE1Descr_Type(DisplayString):
    """Custom type pqlE1Descr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 14),
    )


_PqlE1Descr_Type.__name__ = "DisplayString"
_PqlE1Descr_Object = MibTableColumn
pqlE1Descr = _PqlE1Descr_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 12, 2, 1, 3),
    _PqlE1Descr_Type()
)
pqlE1Descr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pqlE1Descr.setStatus("current")


class _PqlReset_Type(Integer32):
    """Custom type pqlReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("factory", 1)
    )


_PqlReset_Type.__name__ = "Integer32"
_PqlReset_Object = MibScalar
pqlReset = _PqlReset_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 12, 3),
    _PqlReset_Type()
)
pqlReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pqlReset.setStatus("current")
_Ioname_ObjectIdentity = ObjectIdentity
ioname = _Ioname_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 13)
)
_IonameTable_Object = MibTable
ionameTable = _IonameTable_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 13, 1)
)
if mibBuilder.loadTexts:
    ionameTable.setStatus("current")
_IonEntry_Object = MibTableRow
ionEntry = _IonEntry_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 13, 1, 1)
)
ionEntry.setIndexNames(
    (0, "SSU2000-MIB", "ionChassis"),
    (0, "SSU2000-MIB", "ionSlot"),
    (0, "SSU2000-MIB", "ionPort"),
)
if mibBuilder.loadTexts:
    ionEntry.setStatus("current")


class _IonChassis_Type(Integer32):
    """Custom type ionChassis based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_IonChassis_Type.__name__ = "Integer32"
_IonChassis_Object = MibTableColumn
ionChassis = _IonChassis_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 13, 1, 1, 1),
    _IonChassis_Type()
)
ionChassis.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ionChassis.setStatus("current")


class _IonSlot_Type(Integer32):
    """Custom type ionSlot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 20),
    )


_IonSlot_Type.__name__ = "Integer32"
_IonSlot_Object = MibTableColumn
ionSlot = _IonSlot_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 13, 1, 1, 2),
    _IonSlot_Type()
)
ionSlot.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ionSlot.setStatus("current")


class _IonPort_Type(Integer32):
    """Custom type ionPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 20),
    )


_IonPort_Type.__name__ = "Integer32"
_IonPort_Object = MibTableColumn
ionPort = _IonPort_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 13, 1, 1, 3),
    _IonPort_Type()
)
ionPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ionPort.setStatus("current")


class _IonName_Type(DisplayString):
    """Custom type ionName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_IonName_Type.__name__ = "DisplayString"
_IonName_Object = MibTableColumn
ionName = _IonName_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 13, 1, 1, 4),
    _IonName_Type()
)
ionName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ionName.setStatus("current")


class _IonameLoc_Type(DisplayString):
    """Custom type ionameLoc based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 20),
    )


_IonameLoc_Type.__name__ = "DisplayString"
_IonameLoc_Object = MibScalar
ionameLoc = _IonameLoc_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 13, 2),
    _IonameLoc_Type()
)
ionameLoc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ionameLoc.setStatus("current")


class _IonameSet_Type(DisplayString):
    """Custom type ionameSet based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_IonameSet_Type.__name__ = "DisplayString"
_IonameSet_Object = MibScalar
ionameSet = _IonameSet_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 13, 3),
    _IonameSet_Type()
)
ionameSet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ionameSet.setStatus("current")
_Comm_ObjectIdentity = ObjectIdentity
comm = _Comm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 14)
)
_Com232Table_Object = MibTable
com232Table = _Com232Table_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 14, 1)
)
if mibBuilder.loadTexts:
    com232Table.setStatus("current")
_ComEntry_Object = MibTableRow
comEntry = _ComEntry_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 14, 1, 1)
)
comEntry.setIndexNames(
    (0, "SSU2000-MIB", "comIndex"),
)
if mibBuilder.loadTexts:
    comEntry.setStatus("current")


class _ComIndex_Type(Integer32):
    """Custom type comIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_ComIndex_Type.__name__ = "Integer32"
_ComIndex_Object = MibTableColumn
comIndex = _ComIndex_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 14, 1, 1, 1),
    _ComIndex_Type()
)
comIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    comIndex.setStatus("current")


class _ComMode_Type(Integer32):
    """Custom type comMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ics", 1),
          ("tl1", 2))
    )


_ComMode_Type.__name__ = "Integer32"
_ComMode_Object = MibTableColumn
comMode = _ComMode_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 14, 1, 1, 2),
    _ComMode_Type()
)
comMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    comMode.setStatus("current")
_ComEcho_Type = OnValue
_ComEcho_Object = MibTableColumn
comEcho = _ComEcho_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 14, 1, 1, 3),
    _ComEcho_Type()
)
comEcho.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    comEcho.setStatus("current")


class _ComEol_Type(Integer32):
    """Custom type comEol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("cr", 1),
          ("lf", 2),
          ("crlf", 3))
    )


_ComEol_Type.__name__ = "Integer32"
_ComEol_Object = MibTableColumn
comEol = _ComEol_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 14, 1, 1, 4),
    _ComEol_Type()
)
comEol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    comEol.setStatus("current")


class _ComBaud_Type(Integer32):
    """Custom type comBaud based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1200,
              2400,
              4800,
              9600,
              19200)
        )
    )
    namedValues = NamedValues(
        *(("baud1200", 1200),
          ("baud2400", 2400),
          ("baud4800", 4800),
          ("baud9600", 9600),
          ("baud19200", 19200))
    )


_ComBaud_Type.__name__ = "Integer32"
_ComBaud_Object = MibTableColumn
comBaud = _ComBaud_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 14, 1, 1, 5),
    _ComBaud_Type()
)
comBaud.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    comBaud.setStatus("current")
_ComParmTable_Object = MibTable
comParmTable = _ComParmTable_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 14, 2)
)
if mibBuilder.loadTexts:
    comParmTable.setStatus("current")
_ComParmEntry_Object = MibTableRow
comParmEntry = _ComParmEntry_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 14, 2, 1)
)
comParmEntry.setIndexNames(
    (0, "SSU2000-MIB", "comParmIndex"),
)
if mibBuilder.loadTexts:
    comParmEntry.setStatus("current")


class _ComParmIndex_Type(Integer32):
    """Custom type comParmIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_ComParmIndex_Type.__name__ = "Integer32"
_ComParmIndex_Object = MibTableColumn
comParmIndex = _ComParmIndex_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 14, 2, 1, 1),
    _ComParmIndex_Type()
)
comParmIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    comParmIndex.setStatus("current")


class _ComType_Type(Integer32):
    """Custom type comType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("local", 1),
          ("coma", 2),
          ("comb", 3),
          ("telnet", 4),
          ("etl1", 5))
    )


_ComType_Type.__name__ = "Integer32"
_ComType_Object = MibTableColumn
comType = _ComType_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 14, 2, 1, 2),
    _ComType_Type()
)
comType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    comType.setStatus("current")


class _ComTimeout_Type(Integer32):
    """Custom type comTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(5, 43200),
    )


_ComTimeout_Type.__name__ = "Integer32"
_ComTimeout_Object = MibTableColumn
comTimeout = _ComTimeout_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 14, 2, 1, 3),
    _ComTimeout_Type()
)
comTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    comTimeout.setStatus("current")


class _ComLogoff_Type(Integer32):
    """Custom type comLogoff based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11)
        )
    )
    namedValues = NamedValues(
        *(("local", 1),
          ("coma", 2),
          ("comb", 3),
          ("telneta", 4),
          ("telnetb", 5),
          ("telnetc", 6),
          ("telnetd", 7),
          ("etl1a", 8),
          ("etl1b", 9),
          ("etl1c", 10),
          ("etl1d", 11))
    )


_ComLogoff_Type.__name__ = "Integer32"
_ComLogoff_Object = MibScalar
comLogoff = _ComLogoff_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 14, 3),
    _ComLogoff_Type()
)
comLogoff.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    comLogoff.setStatus("current")
_Snmpman_ObjectIdentity = ObjectIdentity
snmpman = _Snmpman_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 15)
)
_Snmpv2manTable_Object = MibTable
snmpv2manTable = _Snmpv2manTable_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 15, 1)
)
if mibBuilder.loadTexts:
    snmpv2manTable.setStatus("current")
_Snmpv2manEntry_Object = MibTableRow
snmpv2manEntry = _Snmpv2manEntry_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 15, 1, 1)
)
snmpv2manEntry.setIndexNames(
    (0, "SSU2000-MIB", "snmpv2manIndex"),
)
if mibBuilder.loadTexts:
    snmpv2manEntry.setStatus("current")


class _Snmpv2manIndex_Type(Integer32):
    """Custom type snmpv2manIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_Snmpv2manIndex_Type.__name__ = "Integer32"
_Snmpv2manIndex_Object = MibTableColumn
snmpv2manIndex = _Snmpv2manIndex_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 15, 1, 1, 1),
    _Snmpv2manIndex_Type()
)
snmpv2manIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    snmpv2manIndex.setStatus("current")
_Snmpv2manIp_Type = IpAddress
_Snmpv2manIp_Object = MibTableColumn
snmpv2manIp = _Snmpv2manIp_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 15, 1, 1, 2),
    _Snmpv2manIp_Type()
)
snmpv2manIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpv2manIp.setStatus("current")


class _SnmpmanInit_Type(Integer32):
    """Custom type snmpmanInit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("initv2", 1),
          ("initv3", 2))
    )


_SnmpmanInit_Type.__name__ = "Integer32"
_SnmpmanInit_Object = MibScalar
snmpmanInit = _SnmpmanInit_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 15, 2),
    _SnmpmanInit_Type()
)
snmpmanInit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpmanInit.setStatus("current")


class _SnmpmanTrap_Type(Integer32):
    """Custom type snmpmanTrap based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("alarm", 1),
          ("all", 2))
    )


_SnmpmanTrap_Type.__name__ = "Integer32"
_SnmpmanTrap_Object = MibScalar
snmpmanTrap = _SnmpmanTrap_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 15, 3),
    _SnmpmanTrap_Type()
)
snmpmanTrap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpmanTrap.setStatus("current")


class _SnmpNotification_Type(Integer32):
    """Custom type snmpNotification based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("v2", 1),
          ("v3", 2),
          ("all", 3))
    )


_SnmpNotification_Type.__name__ = "Integer32"
_SnmpNotification_Object = MibScalar
snmpNotification = _SnmpNotification_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 15, 4),
    _SnmpNotification_Type()
)
snmpNotification.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpNotification.setStatus("current")


class _SnmpEnable_Type(Integer32):
    """Custom type snmpEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("v2enable", 1),
          ("v2disable", 2))
    )


_SnmpEnable_Type.__name__ = "Integer32"
_SnmpEnable_Object = MibScalar
snmpEnable = _SnmpEnable_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 15, 5),
    _SnmpEnable_Type()
)
snmpEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpEnable.setStatus("current")
_Snmpv2userTable_Object = MibTable
snmpv2userTable = _Snmpv2userTable_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 15, 6)
)
if mibBuilder.loadTexts:
    snmpv2userTable.setStatus("current")
_Snmpv2userEntry_Object = MibTableRow
snmpv2userEntry = _Snmpv2userEntry_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 15, 6, 1)
)
snmpv2userEntry.setIndexNames(
    (0, "SSU2000-MIB", "snmpv2userIndex"),
)
if mibBuilder.loadTexts:
    snmpv2userEntry.setStatus("current")


class _Snmpv2userIndex_Type(Integer32):
    """Custom type snmpv2userIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 6),
    )


_Snmpv2userIndex_Type.__name__ = "Integer32"
_Snmpv2userIndex_Object = MibTableColumn
snmpv2userIndex = _Snmpv2userIndex_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 15, 6, 1, 1),
    _Snmpv2userIndex_Type()
)
snmpv2userIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    snmpv2userIndex.setStatus("current")


class _Snmpv2user_Type(DisplayString):
    """Custom type snmpv2user based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_Snmpv2user_Type.__name__ = "DisplayString"
_Snmpv2user_Object = MibTableColumn
snmpv2user = _Snmpv2user_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 15, 6, 1, 2),
    _Snmpv2user_Type()
)
snmpv2user.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmpv2user.setStatus("current")
_Snmpv3userTable_Object = MibTable
snmpv3userTable = _Snmpv3userTable_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 15, 7)
)
if mibBuilder.loadTexts:
    snmpv3userTable.setStatus("current")
_Snmpv3userEntry_Object = MibTableRow
snmpv3userEntry = _Snmpv3userEntry_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 15, 7, 1)
)
snmpv3userEntry.setIndexNames(
    (0, "SSU2000-MIB", "snmpv3userIndex"),
)
if mibBuilder.loadTexts:
    snmpv3userEntry.setStatus("current")


class _Snmpv3userIndex_Type(Integer32):
    """Custom type snmpv3userIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 6),
    )


_Snmpv3userIndex_Type.__name__ = "Integer32"
_Snmpv3userIndex_Object = MibTableColumn
snmpv3userIndex = _Snmpv3userIndex_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 15, 7, 1, 1),
    _Snmpv3userIndex_Type()
)
snmpv3userIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    snmpv3userIndex.setStatus("current")


class _Snmpv3user_Type(DisplayString):
    """Custom type snmpv3user based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_Snmpv3user_Type.__name__ = "DisplayString"
_Snmpv3user_Object = MibTableColumn
snmpv3user = _Snmpv3user_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 15, 7, 1, 2),
    _Snmpv3user_Type()
)
snmpv3user.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmpv3user.setStatus("current")
_Snmpv3manTable_Object = MibTable
snmpv3manTable = _Snmpv3manTable_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 15, 8)
)
if mibBuilder.loadTexts:
    snmpv3manTable.setStatus("current")
_Snmpv3manEntry_Object = MibTableRow
snmpv3manEntry = _Snmpv3manEntry_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 15, 8, 1)
)
snmpv3manEntry.setIndexNames(
    (0, "SSU2000-MIB", "snmpv3manIndex"),
)
if mibBuilder.loadTexts:
    snmpv3manEntry.setStatus("current")


class _Snmpv3manIndex_Type(Integer32):
    """Custom type snmpv3manIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_Snmpv3manIndex_Type.__name__ = "Integer32"
_Snmpv3manIndex_Object = MibTableColumn
snmpv3manIndex = _Snmpv3manIndex_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 15, 8, 1, 1),
    _Snmpv3manIndex_Type()
)
snmpv3manIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    snmpv3manIndex.setStatus("current")
_Snmpv3manIp_Type = IpAddress
_Snmpv3manIp_Object = MibTableColumn
snmpv3manIp = _Snmpv3manIp_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 15, 8, 1, 2),
    _Snmpv3manIp_Type()
)
snmpv3manIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpv3manIp.setStatus("current")


class _Snmpv3manUser_Type(DisplayString):
    """Custom type snmpv3manUser based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_Snmpv3manUser_Type.__name__ = "DisplayString"
_Snmpv3manUser_Object = MibTableColumn
snmpv3manUser = _Snmpv3manUser_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 15, 8, 1, 3),
    _Snmpv3manUser_Type()
)
snmpv3manUser.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpv3manUser.setStatus("current")
_Sys_ObjectIdentity = ObjectIdentity
sys = _Sys_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 16)
)


class _SysPbo_Type(Integer32):
    """Custom type sysPbo based on Integer32"""
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
        *(("event", 1),
          ("report", 2),
          ("none", 3),
          ("disable", 4))
    )


_SysPbo_Type.__name__ = "Integer32"
_SysPbo_Object = MibScalar
sysPbo = _SysPbo_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 16, 1),
    _SysPbo_Type()
)
sysPbo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysPbo.setStatus("current")


class _SysResetClk_Type(Integer32):
    """Custom type sysResetClk based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("clka", 1),
          ("clkb", 2))
    )


_SysResetClk_Type.__name__ = "Integer32"
_SysResetClk_Object = MibScalar
sysResetClk = _SysResetClk_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 16, 2),
    _SysResetClk_Type()
)
sysResetClk.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysResetClk.setStatus("current")
_SysKeepAliveTable_Object = MibTable
sysKeepAliveTable = _SysKeepAliveTable_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 16, 3)
)
if mibBuilder.loadTexts:
    sysKeepAliveTable.setStatus("current")
_SysAliveEntry_Object = MibTableRow
sysAliveEntry = _SysAliveEntry_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 16, 3, 1)
)
sysAliveEntry.setIndexNames(
    (0, "SSU2000-MIB", "sysAliveIndex"),
)
if mibBuilder.loadTexts:
    sysAliveEntry.setStatus("current")


class _SysAliveIndex_Type(Integer32):
    """Custom type sysAliveIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_SysAliveIndex_Type.__name__ = "Integer32"
_SysAliveIndex_Object = MibTableColumn
sysAliveIndex = _SysAliveIndex_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 16, 3, 1, 1),
    _SysAliveIndex_Type()
)
sysAliveIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sysAliveIndex.setStatus("current")


class _SysAliveType_Type(Integer32):
    """Custom type sysAliveType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("tl1", 1),
          ("snmp", 2))
    )


_SysAliveType_Type.__name__ = "Integer32"
_SysAliveType_Object = MibTableColumn
sysAliveType = _SysAliveType_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 16, 3, 1, 2),
    _SysAliveType_Type()
)
sysAliveType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysAliveType.setStatus("current")


class _SysAliveTime_Type(Integer32):
    """Custom type sysAliveTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 60),
    )


_SysAliveTime_Type.__name__ = "Integer32"
_SysAliveTime_Object = MibTableColumn
sysAliveTime = _SysAliveTime_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 16, 3, 1, 3),
    _SysAliveTime_Type()
)
sysAliveTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysAliveTime.setStatus("current")


class _SysOpmode_Type(Integer32):
    """Custom type sysOpmode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("normal", 1),
          ("subtending", 2),
          ("japanese", 3))
    )


_SysOpmode_Type.__name__ = "Integer32"
_SysOpmode_Object = MibScalar
sysOpmode = _SysOpmode_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 16, 4),
    _SysOpmode_Type()
)
sysOpmode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysOpmode.setStatus("current")


class _SysTl1Format_Type(Integer32):
    """Custom type sysTl1Format based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("gr831", 1),
          ("gr833", 2))
    )


_SysTl1Format_Type.__name__ = "Integer32"
_SysTl1Format_Object = MibScalar
sysTl1Format = _SysTl1Format_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 16, 5),
    _SysTl1Format_Type()
)
sysTl1Format.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysTl1Format.setStatus("current")


class _SysEvtLogin_Type(Integer32):
    """Custom type sysEvtLogin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_SysEvtLogin_Type.__name__ = "Integer32"
_SysEvtLogin_Object = MibScalar
sysEvtLogin = _SysEvtLogin_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 16, 6),
    _SysEvtLogin_Type()
)
sysEvtLogin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysEvtLogin.setStatus("current")


class _SysAco_Type(Integer32):
    """Custom type sysAco based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("inactive", 2))
    )


_SysAco_Type.__name__ = "Integer32"
_SysAco_Object = MibScalar
sysAco = _SysAco_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 16, 7),
    _SysAco_Type()
)
sysAco.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysAco.setStatus("current")
_Users_ObjectIdentity = ObjectIdentity
users = _Users_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 17)
)
_UserTable_Object = MibTable
userTable = _UserTable_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 17, 1)
)
if mibBuilder.loadTexts:
    userTable.setStatus("current")
_UserEntry_Object = MibTableRow
userEntry = _UserEntry_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 17, 1, 1)
)
userEntry.setIndexNames(
    (0, "SSU2000-MIB", "userIndex"),
)
if mibBuilder.loadTexts:
    userEntry.setStatus("current")


class _UserIndex_Type(Integer32):
    """Custom type userIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 25),
    )


_UserIndex_Type.__name__ = "Integer32"
_UserIndex_Object = MibTableColumn
userIndex = _UserIndex_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 17, 1, 1, 1),
    _UserIndex_Type()
)
userIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    userIndex.setStatus("current")


class _Userlevel_Type(Integer32):
    """Custom type userlevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_Userlevel_Type.__name__ = "Integer32"
_Userlevel_Object = MibTableColumn
userlevel = _Userlevel_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 17, 1, 1, 2),
    _Userlevel_Type()
)
userlevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    userlevel.setStatus("current")


class _Username_Type(DisplayString):
    """Custom type username based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 10),
    )


_Username_Type.__name__ = "DisplayString"
_Username_Object = MibTableColumn
username = _Username_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 17, 1, 1, 3),
    _Username_Type()
)
username.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    username.setStatus("current")
_Who_ObjectIdentity = ObjectIdentity
who = _Who_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 18)
)
_WhoTable_Object = MibTable
whoTable = _WhoTable_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 18, 1)
)
if mibBuilder.loadTexts:
    whoTable.setStatus("current")
_WhoEntry_Object = MibTableRow
whoEntry = _WhoEntry_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 18, 1, 1)
)
whoEntry.setIndexNames(
    (0, "SSU2000-MIB", "whoIndex"),
)
if mibBuilder.loadTexts:
    whoEntry.setStatus("current")


class _WhoIndex_Type(Integer32):
    """Custom type whoIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 12),
    )


_WhoIndex_Type.__name__ = "Integer32"
_WhoIndex_Object = MibTableColumn
whoIndex = _WhoIndex_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 18, 1, 1, 1),
    _WhoIndex_Type()
)
whoIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    whoIndex.setStatus("current")


class _WhoPort_Type(Integer32):
    """Custom type whoPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11)
        )
    )
    namedValues = NamedValues(
        *(("local", 1),
          ("coma", 2),
          ("comb", 3),
          ("telneta", 4),
          ("telnetb", 5),
          ("telnetc", 6),
          ("telnetd", 7),
          ("etl1a", 8),
          ("etl1b", 9),
          ("etl1c", 10),
          ("etl1d", 11))
    )


_WhoPort_Type.__name__ = "Integer32"
_WhoPort_Object = MibTableColumn
whoPort = _WhoPort_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 18, 1, 1, 2),
    _WhoPort_Type()
)
whoPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    whoPort.setStatus("current")


class _WhoName_Type(DisplayString):
    """Custom type whoName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 10),
    )


_WhoName_Type.__name__ = "DisplayString"
_WhoName_Object = MibTableColumn
whoName = _WhoName_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 18, 1, 1, 3),
    _WhoName_Type()
)
whoName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    whoName.setStatus("current")
_Ntpq_ObjectIdentity = ObjectIdentity
ntpq = _Ntpq_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 19)
)


class _NtpqXeq_Type(DisplayString):
    """Custom type ntpqXeq based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_NtpqXeq_Type.__name__ = "DisplayString"
_NtpqXeq_Object = MibScalar
ntpqXeq = _NtpqXeq_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 19, 1),
    _NtpqXeq_Type()
)
ntpqXeq.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntpqXeq.setStatus("current")
_NtpqTable_Object = MibTable
ntpqTable = _NtpqTable_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 19, 3)
)
if mibBuilder.loadTexts:
    ntpqTable.setStatus("current")
_NtpqEntry_Object = MibTableRow
ntpqEntry = _NtpqEntry_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 19, 3, 1)
)
ntpqEntry.setIndexNames(
    (0, "SSU2000-MIB", "ntpqChassis"),
    (0, "SSU2000-MIB", "ntpqSlot"),
    (0, "SSU2000-MIB", "ntpqIndex"),
)
if mibBuilder.loadTexts:
    ntpqEntry.setStatus("current")


class _NtpqChassis_Type(Integer32):
    """Custom type ntpqChassis based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
    )


_NtpqChassis_Type.__name__ = "Integer32"
_NtpqChassis_Object = MibTableColumn
ntpqChassis = _NtpqChassis_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 19, 3, 1, 1),
    _NtpqChassis_Type()
)
ntpqChassis.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ntpqChassis.setStatus("current")


class _NtpqSlot_Type(Integer32):
    """Custom type ntpqSlot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 20),
    )


_NtpqSlot_Type.__name__ = "Integer32"
_NtpqSlot_Object = MibTableColumn
ntpqSlot = _NtpqSlot_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 19, 3, 1, 2),
    _NtpqSlot_Type()
)
ntpqSlot.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ntpqSlot.setStatus("current")


class _NtpqIndex_Type(Integer32):
    """Custom type ntpqIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 9),
    )


_NtpqIndex_Type.__name__ = "Integer32"
_NtpqIndex_Object = MibTableColumn
ntpqIndex = _NtpqIndex_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 19, 3, 1, 3),
    _NtpqIndex_Type()
)
ntpqIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ntpqIndex.setStatus("current")
_NtpqValid_Type = ValidValue
_NtpqValid_Object = MibTableColumn
ntpqValid = _NtpqValid_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 19, 3, 1, 4),
    _NtpqValid_Type()
)
ntpqValid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntpqValid.setStatus("current")


class _NtpqPeer_Type(DisplayString):
    """Custom type ntpqPeer based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_NtpqPeer_Type.__name__ = "DisplayString"
_NtpqPeer_Object = MibTableColumn
ntpqPeer = _NtpqPeer_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 19, 3, 1, 5),
    _NtpqPeer_Type()
)
ntpqPeer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntpqPeer.setStatus("current")


class _NtpqRefid_Type(DisplayString):
    """Custom type ntpqRefid based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_NtpqRefid_Type.__name__ = "DisplayString"
_NtpqRefid_Object = MibTableColumn
ntpqRefid = _NtpqRefid_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 19, 3, 1, 6),
    _NtpqRefid_Type()
)
ntpqRefid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntpqRefid.setStatus("current")


class _NtpqStratum_Type(Integer32):
    """Custom type ntpqStratum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )


_NtpqStratum_Type.__name__ = "Integer32"
_NtpqStratum_Object = MibTableColumn
ntpqStratum = _NtpqStratum_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 19, 3, 1, 7),
    _NtpqStratum_Type()
)
ntpqStratum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntpqStratum.setStatus("current")


class _NtpqPoll_Type(Integer32):
    """Custom type ntpqPoll based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1024),
    )


_NtpqPoll_Type.__name__ = "Integer32"
_NtpqPoll_Object = MibTableColumn
ntpqPoll = _NtpqPoll_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 19, 3, 1, 8),
    _NtpqPoll_Type()
)
ntpqPoll.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntpqPoll.setStatus("current")


class _NtpqReach_Type(DisplayString):
    """Custom type ntpqReach based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_NtpqReach_Type.__name__ = "DisplayString"
_NtpqReach_Object = MibTableColumn
ntpqReach = _NtpqReach_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 19, 3, 1, 9),
    _NtpqReach_Type()
)
ntpqReach.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntpqReach.setStatus("current")


class _NtpqDelay_Type(DisplayString):
    """Custom type ntpqDelay based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_NtpqDelay_Type.__name__ = "DisplayString"
_NtpqDelay_Object = MibTableColumn
ntpqDelay = _NtpqDelay_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 19, 3, 1, 10),
    _NtpqDelay_Type()
)
ntpqDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntpqDelay.setStatus("current")


class _NtpqOffset_Type(DisplayString):
    """Custom type ntpqOffset based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_NtpqOffset_Type.__name__ = "DisplayString"
_NtpqOffset_Object = MibTableColumn
ntpqOffset = _NtpqOffset_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 19, 3, 1, 11),
    _NtpqOffset_Type()
)
ntpqOffset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntpqOffset.setStatus("current")


class _NtpqJitter_Type(DisplayString):
    """Custom type ntpqJitter based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_NtpqJitter_Type.__name__ = "DisplayString"
_NtpqJitter_Object = MibTableColumn
ntpqJitter = _NtpqJitter_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 19, 3, 1, 12),
    _NtpqJitter_Type()
)
ntpqJitter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntpqJitter.setStatus("current")


class _NtpqSyspeer_Type(DisplayString):
    """Custom type ntpqSyspeer based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_NtpqSyspeer_Type.__name__ = "DisplayString"
_NtpqSyspeer_Object = MibScalar
ntpqSyspeer = _NtpqSyspeer_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 19, 4),
    _NtpqSyspeer_Type()
)
ntpqSyspeer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntpqSyspeer.setStatus("current")


class _NtpqSysleap_Type(Integer32):
    """Custom type ntpqSysleap based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2),
    )


_NtpqSysleap_Type.__name__ = "Integer32"
_NtpqSysleap_Object = MibScalar
ntpqSysleap = _NtpqSysleap_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 19, 5),
    _NtpqSysleap_Type()
)
ntpqSysleap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntpqSysleap.setStatus("current")


class _NtpqSysstratum_Type(Integer32):
    """Custom type ntpqSysstratum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )


_NtpqSysstratum_Type.__name__ = "Integer32"
_NtpqSysstratum_Object = MibScalar
ntpqSysstratum = _NtpqSysstratum_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 19, 6),
    _NtpqSysstratum_Type()
)
ntpqSysstratum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntpqSysstratum.setStatus("current")


class _NtpqSysprecision_Type(Integer32):
    """Custom type ntpqSysprecision based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-100, 0),
    )


_NtpqSysprecision_Type.__name__ = "Integer32"
_NtpqSysprecision_Object = MibScalar
ntpqSysprecision = _NtpqSysprecision_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 19, 7),
    _NtpqSysprecision_Type()
)
ntpqSysprecision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntpqSysprecision.setStatus("current")


class _NtpqRootdelay_Type(DisplayString):
    """Custom type ntpqRootdelay based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_NtpqRootdelay_Type.__name__ = "DisplayString"
_NtpqRootdelay_Object = MibScalar
ntpqRootdelay = _NtpqRootdelay_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 19, 8),
    _NtpqRootdelay_Type()
)
ntpqRootdelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntpqRootdelay.setStatus("current")


class _NtpqRootdispersion_Type(DisplayString):
    """Custom type ntpqRootdispersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_NtpqRootdispersion_Type.__name__ = "DisplayString"
_NtpqRootdispersion_Object = MibScalar
ntpqRootdispersion = _NtpqRootdispersion_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 19, 9),
    _NtpqRootdispersion_Type()
)
ntpqRootdispersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntpqRootdispersion.setStatus("current")


class _NtpqSysoffset_Type(DisplayString):
    """Custom type ntpqSysoffset based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_NtpqSysoffset_Type.__name__ = "DisplayString"
_NtpqSysoffset_Object = MibScalar
ntpqSysoffset = _NtpqSysoffset_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 19, 10),
    _NtpqSysoffset_Type()
)
ntpqSysoffset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntpqSysoffset.setStatus("current")


class _NtpqReftime_Type(DisplayString):
    """Custom type ntpqReftime based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 60),
    )


_NtpqReftime_Type.__name__ = "DisplayString"
_NtpqReftime_Object = MibScalar
ntpqReftime = _NtpqReftime_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 19, 11),
    _NtpqReftime_Type()
)
ntpqReftime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntpqReftime.setStatus("current")
_Route_ObjectIdentity = ObjectIdentity
route = _Route_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 20)
)


class _RtXeq_Type(DisplayString):
    """Custom type rtXeq based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_RtXeq_Type.__name__ = "DisplayString"
_RtXeq_Object = MibScalar
rtXeq = _RtXeq_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 20, 1),
    _RtXeq_Type()
)
rtXeq.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rtXeq.setStatus("current")
_RouteTable_Object = MibTable
routeTable = _RouteTable_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 20, 3)
)
if mibBuilder.loadTexts:
    routeTable.setStatus("current")
_RtEntry_Object = MibTableRow
rtEntry = _RtEntry_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 20, 3, 1)
)
rtEntry.setIndexNames(
    (0, "SSU2000-MIB", "rtChassis"),
    (0, "SSU2000-MIB", "rtSlot"),
    (0, "SSU2000-MIB", "rtIndex"),
)
if mibBuilder.loadTexts:
    rtEntry.setStatus("current")


class _RtChassis_Type(Integer32):
    """Custom type rtChassis based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
    )


_RtChassis_Type.__name__ = "Integer32"
_RtChassis_Object = MibTableColumn
rtChassis = _RtChassis_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 20, 3, 1, 1),
    _RtChassis_Type()
)
rtChassis.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rtChassis.setStatus("current")


class _RtSlot_Type(Integer32):
    """Custom type rtSlot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 20),
    )


_RtSlot_Type.__name__ = "Integer32"
_RtSlot_Object = MibTableColumn
rtSlot = _RtSlot_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 20, 3, 1, 2),
    _RtSlot_Type()
)
rtSlot.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rtSlot.setStatus("current")


class _RtIndex_Type(Integer32):
    """Custom type rtIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 20),
    )


_RtIndex_Type.__name__ = "Integer32"
_RtIndex_Object = MibTableColumn
rtIndex = _RtIndex_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 20, 3, 1, 3),
    _RtIndex_Type()
)
rtIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rtIndex.setStatus("current")
_RtValid_Type = ValidValue
_RtValid_Object = MibTableColumn
rtValid = _RtValid_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 20, 3, 1, 4),
    _RtValid_Type()
)
rtValid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtValid.setStatus("current")
_RtDest_Type = IpAddress
_RtDest_Object = MibTableColumn
rtDest = _RtDest_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 20, 3, 1, 5),
    _RtDest_Type()
)
rtDest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtDest.setStatus("current")
_RtGate_Type = IpAddress
_RtGate_Object = MibTableColumn
rtGate = _RtGate_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 20, 3, 1, 6),
    _RtGate_Type()
)
rtGate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtGate.setStatus("current")
_RtMask_Type = IpAddress
_RtMask_Object = MibTableColumn
rtMask = _RtMask_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 20, 3, 1, 7),
    _RtMask_Type()
)
rtMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtMask.setStatus("current")


class _RtFlags_Type(DisplayString):
    """Custom type rtFlags based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 6),
    )


_RtFlags_Type.__name__ = "DisplayString"
_RtFlags_Object = MibTableColumn
rtFlags = _RtFlags_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 20, 3, 1, 8),
    _RtFlags_Type()
)
rtFlags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtFlags.setStatus("current")


class _RtMetric_Type(Integer32):
    """Custom type rtMetric based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4),
    )


_RtMetric_Type.__name__ = "Integer32"
_RtMetric_Object = MibTableColumn
rtMetric = _RtMetric_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 20, 3, 1, 9),
    _RtMetric_Type()
)
rtMetric.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtMetric.setStatus("current")


class _RtRef_Type(Integer32):
    """Custom type rtRef based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4),
    )


_RtRef_Type.__name__ = "Integer32"
_RtRef_Object = MibTableColumn
rtRef = _RtRef_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 20, 3, 1, 10),
    _RtRef_Type()
)
rtRef.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtRef.setStatus("current")


class _RtUse_Type(Integer32):
    """Custom type rtUse based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_RtUse_Type.__name__ = "Integer32"
_RtUse_Object = MibTableColumn
rtUse = _RtUse_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 20, 3, 1, 11),
    _RtUse_Type()
)
rtUse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtUse.setStatus("current")


class _RtIface_Type(Integer32):
    """Custom type rtIface based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 34094),
    )


_RtIface_Type.__name__ = "Integer32"
_RtIface_Object = MibTableColumn
rtIface = _RtIface_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 20, 3, 1, 12),
    _RtIface_Type()
)
rtIface.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtIface.setStatus("current")
_Mtie_ObjectIdentity = ObjectIdentity
mtie = _Mtie_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 30)
)


class _MtInpLoc_Type(DisplayString):
    """Custom type mtInpLoc based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 10),
    )


_MtInpLoc_Type.__name__ = "DisplayString"
_MtInpLoc_Object = MibScalar
mtInpLoc = _MtInpLoc_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 30, 1),
    _MtInpLoc_Type()
)
mtInpLoc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mtInpLoc.setStatus("current")
_MtFrTime_Type = DateAndTime
_MtFrTime_Object = MibScalar
mtFrTime = _MtFrTime_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 30, 2),
    _MtFrTime_Type()
)
mtFrTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mtFrTime.setStatus("current")
_MtToTime_Type = DateAndTime
_MtToTime_Object = MibScalar
mtToTime = _MtToTime_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 30, 3),
    _MtToTime_Type()
)
mtToTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mtToTime.setStatus("current")
_MtTable_Object = MibTable
mtTable = _MtTable_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 30, 5)
)
if mibBuilder.loadTexts:
    mtTable.setStatus("current")
_MtEntry_Object = MibTableRow
mtEntry = _MtEntry_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 30, 5, 1)
)
mtEntry.setIndexNames(
    (0, "SSU2000-MIB", "mtChassis"),
    (0, "SSU2000-MIB", "mtSlot"),
    (0, "SSU2000-MIB", "mtPort"),
)
if mibBuilder.loadTexts:
    mtEntry.setStatus("current")


class _MtChassis_Type(Integer32):
    """Custom type mtChassis based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
    )


_MtChassis_Type.__name__ = "Integer32"
_MtChassis_Object = MibTableColumn
mtChassis = _MtChassis_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 30, 5, 1, 1),
    _MtChassis_Type()
)
mtChassis.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mtChassis.setStatus("current")


class _MtSlot_Type(Integer32):
    """Custom type mtSlot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 20),
    )


_MtSlot_Type.__name__ = "Integer32"
_MtSlot_Object = MibTableColumn
mtSlot = _MtSlot_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 30, 5, 1, 2),
    _MtSlot_Type()
)
mtSlot.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mtSlot.setStatus("current")


class _MtPort_Type(Integer32):
    """Custom type mtPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_MtPort_Type.__name__ = "Integer32"
_MtPort_Object = MibTableColumn
mtPort = _MtPort_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 30, 5, 1, 3),
    _MtPort_Type()
)
mtPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mtPort.setStatus("current")


class _MtA_Type(OctetString):
    """Custom type mtA based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(76, 76),
    )
    fixed_length = 76


_MtA_Type.__name__ = "OctetString"
_MtA_Object = MibTableColumn
mtA = _MtA_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 30, 5, 1, 4),
    _MtA_Type()
)
mtA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtA.setStatus("current")


class _MtB_Type(OctetString):
    """Custom type mtB based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(76, 76),
    )
    fixed_length = 76


_MtB_Type.__name__ = "OctetString"
_MtB_Object = MibTableColumn
mtB = _MtB_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 30, 5, 1, 5),
    _MtB_Type()
)
mtB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtB.setStatus("current")


class _MtHisInpLoc_Type(DisplayString):
    """Custom type mtHisInpLoc based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_MtHisInpLoc_Type.__name__ = "DisplayString"
_MtHisInpLoc_Object = MibScalar
mtHisInpLoc = _MtHisInpLoc_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 30, 6),
    _MtHisInpLoc_Type()
)
mtHisInpLoc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mtHisInpLoc.setStatus("current")


class _MtHisClk_Type(Integer32):
    """Custom type mtHisClk based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("clka", 1),
          ("clkb", 2))
    )


_MtHisClk_Type.__name__ = "Integer32"
_MtHisClk_Object = MibScalar
mtHisClk = _MtHisClk_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 30, 7),
    _MtHisClk_Type()
)
mtHisClk.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mtHisClk.setStatus("current")


class _MtHisCnt_Type(Integer32):
    """Custom type mtHisCnt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_MtHisCnt_Type.__name__ = "Integer32"
_MtHisCnt_Object = MibScalar
mtHisCnt = _MtHisCnt_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 30, 8),
    _MtHisCnt_Type()
)
mtHisCnt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mtHisCnt.setStatus("current")
_MtHisTable_Object = MibTable
mtHisTable = _MtHisTable_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 30, 9)
)
if mibBuilder.loadTexts:
    mtHisTable.setStatus("current")
_MtHisEntry_Object = MibTableRow
mtHisEntry = _MtHisEntry_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 30, 9, 1)
)
mtHisEntry.setIndexNames(
    (0, "SSU2000-MIB", "mtHisChassis"),
    (0, "SSU2000-MIB", "mtHisSlot"),
    (0, "SSU2000-MIB", "mtHisPort"),
    (0, "SSU2000-MIB", "mtHisIndex"),
)
if mibBuilder.loadTexts:
    mtHisEntry.setStatus("current")


class _MtHisChassis_Type(Integer32):
    """Custom type mtHisChassis based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
    )


_MtHisChassis_Type.__name__ = "Integer32"
_MtHisChassis_Object = MibTableColumn
mtHisChassis = _MtHisChassis_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 30, 9, 1, 1),
    _MtHisChassis_Type()
)
mtHisChassis.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mtHisChassis.setStatus("current")


class _MtHisSlot_Type(Integer32):
    """Custom type mtHisSlot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 20),
    )


_MtHisSlot_Type.__name__ = "Integer32"
_MtHisSlot_Object = MibTableColumn
mtHisSlot = _MtHisSlot_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 30, 9, 1, 2),
    _MtHisSlot_Type()
)
mtHisSlot.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mtHisSlot.setStatus("current")


class _MtHisPort_Type(Integer32):
    """Custom type mtHisPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_MtHisPort_Type.__name__ = "Integer32"
_MtHisPort_Object = MibTableColumn
mtHisPort = _MtHisPort_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 30, 9, 1, 3),
    _MtHisPort_Type()
)
mtHisPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mtHisPort.setStatus("current")


class _MtHisIndex_Type(Integer32):
    """Custom type mtHisIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_MtHisIndex_Type.__name__ = "Integer32"
_MtHisIndex_Object = MibTableColumn
mtHisIndex = _MtHisIndex_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 30, 9, 1, 4),
    _MtHisIndex_Type()
)
mtHisIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mtHisIndex.setStatus("current")


class _MtHisV_Type(OctetString):
    """Custom type mtHisV based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(76, 76),
    )
    fixed_length = 76


_MtHisV_Type.__name__ = "OctetString"
_MtHisV_Object = MibTableColumn
mtHisV = _MtHisV_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 30, 9, 1, 5),
    _MtHisV_Type()
)
mtHisV.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtHisV.setStatus("current")
_Tdev_ObjectIdentity = ObjectIdentity
tdev = _Tdev_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 31)
)


class _TdInpLoc_Type(DisplayString):
    """Custom type tdInpLoc based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 10),
    )


_TdInpLoc_Type.__name__ = "DisplayString"
_TdInpLoc_Object = MibScalar
tdInpLoc = _TdInpLoc_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 31, 1),
    _TdInpLoc_Type()
)
tdInpLoc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tdInpLoc.setStatus("current")
_TdFrTime_Type = DateAndTime
_TdFrTime_Object = MibScalar
tdFrTime = _TdFrTime_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 31, 2),
    _TdFrTime_Type()
)
tdFrTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tdFrTime.setStatus("current")
_TdToTime_Type = DateAndTime
_TdToTime_Object = MibScalar
tdToTime = _TdToTime_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 31, 3),
    _TdToTime_Type()
)
tdToTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tdToTime.setStatus("current")
_TdTable_Object = MibTable
tdTable = _TdTable_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 31, 5)
)
if mibBuilder.loadTexts:
    tdTable.setStatus("current")
_TdEntry_Object = MibTableRow
tdEntry = _TdEntry_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 31, 5, 1)
)
tdEntry.setIndexNames(
    (0, "SSU2000-MIB", "tdChassis"),
    (0, "SSU2000-MIB", "tdSlot"),
    (0, "SSU2000-MIB", "tdPort"),
)
if mibBuilder.loadTexts:
    tdEntry.setStatus("current")


class _TdChassis_Type(Integer32):
    """Custom type tdChassis based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
    )


_TdChassis_Type.__name__ = "Integer32"
_TdChassis_Object = MibTableColumn
tdChassis = _TdChassis_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 31, 5, 1, 1),
    _TdChassis_Type()
)
tdChassis.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tdChassis.setStatus("current")


class _TdSlot_Type(Integer32):
    """Custom type tdSlot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 20),
    )


_TdSlot_Type.__name__ = "Integer32"
_TdSlot_Object = MibTableColumn
tdSlot = _TdSlot_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 31, 5, 1, 2),
    _TdSlot_Type()
)
tdSlot.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tdSlot.setStatus("current")


class _TdPort_Type(Integer32):
    """Custom type tdPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_TdPort_Type.__name__ = "Integer32"
_TdPort_Object = MibTableColumn
tdPort = _TdPort_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 31, 5, 1, 3),
    _TdPort_Type()
)
tdPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tdPort.setStatus("current")


class _TdA_Type(OctetString):
    """Custom type tdA based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(124, 124),
    )
    fixed_length = 124


_TdA_Type.__name__ = "OctetString"
_TdA_Object = MibTableColumn
tdA = _TdA_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 31, 5, 1, 4),
    _TdA_Type()
)
tdA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tdA.setStatus("current")


class _TdB_Type(OctetString):
    """Custom type tdB based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(124, 124),
    )
    fixed_length = 124


_TdB_Type.__name__ = "OctetString"
_TdB_Object = MibTableColumn
tdB = _TdB_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 31, 5, 1, 5),
    _TdB_Type()
)
tdB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tdB.setStatus("current")


class _TdHisInpLoc_Type(DisplayString):
    """Custom type tdHisInpLoc based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_TdHisInpLoc_Type.__name__ = "DisplayString"
_TdHisInpLoc_Object = MibScalar
tdHisInpLoc = _TdHisInpLoc_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 31, 6),
    _TdHisInpLoc_Type()
)
tdHisInpLoc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tdHisInpLoc.setStatus("current")


class _TdHisClk_Type(Integer32):
    """Custom type tdHisClk based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("clka", 1),
          ("clkb", 2))
    )


_TdHisClk_Type.__name__ = "Integer32"
_TdHisClk_Object = MibScalar
tdHisClk = _TdHisClk_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 31, 7),
    _TdHisClk_Type()
)
tdHisClk.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tdHisClk.setStatus("current")


class _TdHisCnt_Type(Integer32):
    """Custom type tdHisCnt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_TdHisCnt_Type.__name__ = "Integer32"
_TdHisCnt_Object = MibScalar
tdHisCnt = _TdHisCnt_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 31, 8),
    _TdHisCnt_Type()
)
tdHisCnt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tdHisCnt.setStatus("current")
_TdHisTable_Object = MibTable
tdHisTable = _TdHisTable_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 31, 9)
)
if mibBuilder.loadTexts:
    tdHisTable.setStatus("current")
_TdHisEntry_Object = MibTableRow
tdHisEntry = _TdHisEntry_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 31, 9, 1)
)
tdHisEntry.setIndexNames(
    (0, "SSU2000-MIB", "tdHisChassis"),
    (0, "SSU2000-MIB", "tdHisSlot"),
    (0, "SSU2000-MIB", "tdHisPort"),
    (0, "SSU2000-MIB", "tdHisIndex"),
)
if mibBuilder.loadTexts:
    tdHisEntry.setStatus("current")


class _TdHisChassis_Type(Integer32):
    """Custom type tdHisChassis based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
    )


_TdHisChassis_Type.__name__ = "Integer32"
_TdHisChassis_Object = MibTableColumn
tdHisChassis = _TdHisChassis_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 31, 9, 1, 1),
    _TdHisChassis_Type()
)
tdHisChassis.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tdHisChassis.setStatus("current")


class _TdHisSlot_Type(Integer32):
    """Custom type tdHisSlot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 20),
    )


_TdHisSlot_Type.__name__ = "Integer32"
_TdHisSlot_Object = MibTableColumn
tdHisSlot = _TdHisSlot_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 31, 9, 1, 2),
    _TdHisSlot_Type()
)
tdHisSlot.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tdHisSlot.setStatus("current")


class _TdHisPort_Type(Integer32):
    """Custom type tdHisPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_TdHisPort_Type.__name__ = "Integer32"
_TdHisPort_Object = MibTableColumn
tdHisPort = _TdHisPort_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 31, 9, 1, 3),
    _TdHisPort_Type()
)
tdHisPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tdHisPort.setStatus("current")


class _TdHisIndex_Type(Integer32):
    """Custom type tdHisIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_TdHisIndex_Type.__name__ = "Integer32"
_TdHisIndex_Object = MibTableColumn
tdHisIndex = _TdHisIndex_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 31, 9, 1, 4),
    _TdHisIndex_Type()
)
tdHisIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tdHisIndex.setStatus("current")


class _TdHisV_Type(OctetString):
    """Custom type tdHisV based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(124, 124),
    )
    fixed_length = 124


_TdHisV_Type.__name__ = "OctetString"
_TdHisV_Object = MibTableColumn
tdHisV = _TdHisV_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 31, 9, 1, 5),
    _TdHisV_Type()
)
tdHisV.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tdHisV.setStatus("current")
_Ptpclient_ObjectIdentity = ObjectIdentity
ptpclient = _Ptpclient_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 36)
)
_PtpclientTable_Object = MibTable
ptpclientTable = _PtpclientTable_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 36, 1)
)
if mibBuilder.loadTexts:
    ptpclientTable.setStatus("current")
_PtpclientEntry_Object = MibTableRow
ptpclientEntry = _PtpclientEntry_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 36, 1, 1)
)
ptpclientEntry.setIndexNames(
    (0, "SSU2000-MIB", "ptpclientChassis"),
    (0, "SSU2000-MIB", "ptpclientSlot"),
)
if mibBuilder.loadTexts:
    ptpclientEntry.setStatus("current")


class _PtpclientChassis_Type(Integer32):
    """Custom type ptpclientChassis based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_PtpclientChassis_Type.__name__ = "Integer32"
_PtpclientChassis_Object = MibTableColumn
ptpclientChassis = _PtpclientChassis_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 36, 1, 1, 1),
    _PtpclientChassis_Type()
)
ptpclientChassis.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ptpclientChassis.setStatus("current")


class _PtpclientSlot_Type(Integer32):
    """Custom type ptpclientSlot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 20),
    )


_PtpclientSlot_Type.__name__ = "Integer32"
_PtpclientSlot_Object = MibTableColumn
ptpclientSlot = _PtpclientSlot_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 36, 1, 1, 2),
    _PtpclientSlot_Type()
)
ptpclientSlot.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ptpclientSlot.setStatus("current")


class _PtpclientData_Type(OctetString):
    """Custom type ptpclientData based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(40, 40),
    )
    fixed_length = 40


_PtpclientData_Type.__name__ = "OctetString"
_PtpclientData_Object = MibTableColumn
ptpclientData = _PtpclientData_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 36, 1, 1, 3),
    _PtpclientData_Type()
)
ptpclientData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ptpclientData.setStatus("current")


class _PtpclientParmLoc_Type(DisplayString):
    """Custom type ptpclientParmLoc based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_PtpclientParmLoc_Type.__name__ = "DisplayString"
_PtpclientParmLoc_Object = MibScalar
ptpclientParmLoc = _PtpclientParmLoc_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 36, 2),
    _PtpclientParmLoc_Type()
)
ptpclientParmLoc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ptpclientParmLoc.setStatus("current")
_PtpclientCmdXeq_Type = YesValue
_PtpclientCmdXeq_Object = MibScalar
ptpclientCmdXeq = _PtpclientCmdXeq_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 36, 3),
    _PtpclientCmdXeq_Type()
)
ptpclientCmdXeq.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ptpclientCmdXeq.setStatus("current")
_MTrapReq_ObjectIdentity = ObjectIdentity
mTrapReq = _MTrapReq_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 50)
)


class _TprTag_Type(Integer32):
    """Custom type tprTag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_TprTag_Type.__name__ = "Integer32"
_TprTag_Object = MibScalar
tprTag = _TprTag_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 50, 1),
    _TprTag_Type()
)
tprTag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tprTag.setStatus("current")
_MTrapObjs_ObjectIdentity = ObjectIdentity
mTrapObjs = _MTrapObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 51)
)


class _TpTag_Type(Integer32):
    """Custom type tpTag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_TpTag_Type.__name__ = "Integer32"
_TpTag_Object = MibScalar
tpTag = _TpTag_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 51, 1),
    _TpTag_Type()
)
tpTag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tpTag.setStatus("current")


class _TpEvt_Type(Integer32):
    """Custom type tpEvt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("autonomous", 1),
          ("resend", 2))
    )


_TpEvt_Type.__name__ = "Integer32"
_TpEvt_Object = MibScalar
tpEvt = _TpEvt_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 51, 2),
    _TpEvt_Type()
)
tpEvt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tpEvt.setStatus("current")


class _TpId_Type(Integer32):
    """Custom type tpId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_TpId_Type.__name__ = "Integer32"
_TpId_Object = MibScalar
tpId = _TpId_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 51, 3),
    _TpId_Type()
)
tpId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tpId.setStatus("current")
_TpMCode_Type = TModuleCode
_TpMCode_Object = MibScalar
tpMCode = _TpMCode_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 51, 4),
    _TpMCode_Type()
)
tpMCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tpMCode.setStatus("current")
_TpTimestamp_Type = DateAndTime
_TpTimestamp_Object = MibScalar
tpTimestamp = _TpTimestamp_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 51, 5),
    _TpTimestamp_Type()
)
tpTimestamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tpTimestamp.setStatus("current")


class _TpChassis_Type(Integer32):
    """Custom type tpChassis based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_TpChassis_Type.__name__ = "Integer32"
_TpChassis_Object = MibScalar
tpChassis = _TpChassis_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 51, 6),
    _TpChassis_Type()
)
tpChassis.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tpChassis.setStatus("current")


class _TpSlot_Type(Integer32):
    """Custom type tpSlot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 20),
    )


_TpSlot_Type.__name__ = "Integer32"
_TpSlot_Object = MibScalar
tpSlot = _TpSlot_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 51, 7),
    _TpSlot_Type()
)
tpSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tpSlot.setStatus("current")


class _TpPort_Type(Integer32):
    """Custom type tpPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 20),
    )


_TpPort_Type.__name__ = "Integer32"
_TpPort_Object = MibScalar
tpPort = _TpPort_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 51, 8),
    _TpPort_Type()
)
tpPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tpPort.setStatus("current")


class _TpAlmCode_Type(Integer32):
    """Custom type tpAlmCode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("minor", 1),
          ("major", 2),
          ("critical", 3),
          ("ignore", 4),
          ("report", 5))
    )


_TpAlmCode_Type.__name__ = "Integer32"
_TpAlmCode_Object = MibScalar
tpAlmCode = _TpAlmCode_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 51, 9),
    _TpAlmCode_Type()
)
tpAlmCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tpAlmCode.setStatus("current")


class _TpNtfCode_Type(Integer32):
    """Custom type tpNtfCode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("minor", 1),
          ("major", 2),
          ("critical", 3),
          ("report", 5),
          ("clear", 6))
    )


_TpNtfCode_Type.__name__ = "Integer32"
_TpNtfCode_Object = MibScalar
tpNtfCode = _TpNtfCode_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 51, 10),
    _TpNtfCode_Type()
)
tpNtfCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tpNtfCode.setStatus("current")


class _TpElevated_Type(Integer32):
    """Custom type tpElevated based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("yes", 1),
          ("no", 2))
    )


_TpElevated_Type.__name__ = "Integer32"
_TpElevated_Object = MibScalar
tpElevated = _TpElevated_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 51, 11),
    _TpElevated_Type()
)
tpElevated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tpElevated.setStatus("current")


class _TpDescr_Type(DisplayString):
    """Custom type tpDescr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_TpDescr_Type.__name__ = "DisplayString"
_TpDescr_Object = MibScalar
tpDescr = _TpDescr_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 51, 12),
    _TpDescr_Type()
)
tpDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tpDescr.setStatus("current")
_MTraps_ObjectIdentity = ObjectIdentity
mTraps = _MTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 52)
)
_SsuTraps_ObjectIdentity = ObjectIdentity
ssuTraps = _SsuTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 52, 0)
)
if mibBuilder.loadTexts:
    ssuTraps.setStatus("current")
_SInterfaces_ObjectIdentity = ObjectIdentity
sInterfaces = _SInterfaces_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 60)
)


class _SifNtpNumber_Type(Integer32):
    """Custom type sifNtpNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_SifNtpNumber_Type.__name__ = "Integer32"
_SifNtpNumber_Object = MibScalar
sifNtpNumber = _SifNtpNumber_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 60, 1),
    _SifNtpNumber_Type()
)
sifNtpNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sifNtpNumber.setStatus("current")


class _SifSnmpv2Number_Type(Integer32):
    """Custom type sifSnmpv2Number based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_SifSnmpv2Number_Type.__name__ = "Integer32"
_SifSnmpv2Number_Object = MibScalar
sifSnmpv2Number = _SifSnmpv2Number_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 60, 2),
    _SifSnmpv2Number_Type()
)
sifSnmpv2Number.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sifSnmpv2Number.setStatus("current")


class _SifSnmpv3Number_Type(Integer32):
    """Custom type sifSnmpv3Number based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_SifSnmpv3Number_Type.__name__ = "Integer32"
_SifSnmpv3Number_Object = MibScalar
sifSnmpv3Number = _SifSnmpv3Number_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 60, 3),
    _SifSnmpv3Number_Type()
)
sifSnmpv3Number.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sifSnmpv3Number.setStatus("current")


class _SifClkNumber_Type(Integer32):
    """Custom type sifClkNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_SifClkNumber_Type.__name__ = "Integer32"
_SifClkNumber_Object = MibScalar
sifClkNumber = _SifClkNumber_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 60, 10),
    _SifClkNumber_Type()
)
sifClkNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sifClkNumber.setStatus("current")


class _SifGpsNumber_Type(Integer32):
    """Custom type sifGpsNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_SifGpsNumber_Type.__name__ = "Integer32"
_SifGpsNumber_Object = MibScalar
sifGpsNumber = _SifGpsNumber_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 60, 11),
    _SifGpsNumber_Type()
)
sifGpsNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sifGpsNumber.setStatus("current")


class _SifInpDs1Number_Type(Integer32):
    """Custom type sifInpDs1Number based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10),
    )


_SifInpDs1Number_Type.__name__ = "Integer32"
_SifInpDs1Number_Object = MibScalar
sifInpDs1Number = _SifInpDs1Number_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 60, 12),
    _SifInpDs1Number_Type()
)
sifInpDs1Number.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sifInpDs1Number.setStatus("current")


class _SifInpE1Number_Type(Integer32):
    """Custom type sifInpE1Number based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10),
    )


_SifInpE1Number_Type.__name__ = "Integer32"
_SifInpE1Number_Object = MibScalar
sifInpE1Number = _SifInpE1Number_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 60, 13),
    _SifInpE1Number_Type()
)
sifInpE1Number.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sifInpE1Number.setStatus("current")


class _SifInpCcNumber_Type(Integer32):
    """Custom type sifInpCcNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10),
    )


_SifInpCcNumber_Type.__name__ = "Integer32"
_SifInpCcNumber_Object = MibScalar
sifInpCcNumber = _SifInpCcNumber_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 60, 14),
    _SifInpCcNumber_Type()
)
sifInpCcNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sifInpCcNumber.setStatus("current")


class _SifOutDs1Number_Type(Integer32):
    """Custom type sifOutDs1Number based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_SifOutDs1Number_Type.__name__ = "Integer32"
_SifOutDs1Number_Object = MibScalar
sifOutDs1Number = _SifOutDs1Number_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 60, 15),
    _SifOutDs1Number_Type()
)
sifOutDs1Number.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sifOutDs1Number.setStatus("current")


class _SifOutE1Number_Type(Integer32):
    """Custom type sifOutE1Number based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_SifOutE1Number_Type.__name__ = "Integer32"
_SifOutE1Number_Object = MibScalar
sifOutE1Number = _SifOutE1Number_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 60, 16),
    _SifOutE1Number_Type()
)
sifOutE1Number.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sifOutE1Number.setStatus("current")


class _SifOut2048Number_Type(Integer32):
    """Custom type sifOut2048Number based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_SifOut2048Number_Type.__name__ = "Integer32"
_SifOut2048Number_Object = MibScalar
sifOut2048Number = _SifOut2048Number_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 60, 17),
    _SifOut2048Number_Type()
)
sifOut2048Number.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sifOut2048Number.setStatus("current")


class _SifOutCcNumber_Type(Integer32):
    """Custom type sifOutCcNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_SifOutCcNumber_Type.__name__ = "Integer32"
_SifOutCcNumber_Object = MibScalar
sifOutCcNumber = _SifOutCcNumber_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 60, 18),
    _SifOutCcNumber_Type()
)
sifOutCcNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sifOutCcNumber.setStatus("current")


class _SifOutE12048Number_Type(Integer32):
    """Custom type sifOutE12048Number based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_SifOutE12048Number_Type.__name__ = "Integer32"
_SifOutE12048Number_Object = MibScalar
sifOutE12048Number = _SifOutE12048Number_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 60, 19),
    _SifOutE12048Number_Type()
)
sifOutE12048Number.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sifOutE12048Number.setStatus("current")


class _SifOut422Number_Type(Integer32):
    """Custom type sifOut422Number based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_SifOut422Number_Type.__name__ = "Integer32"
_SifOut422Number_Object = MibScalar
sifOut422Number = _SifOut422Number_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 60, 20),
    _SifOut422Number_Type()
)
sifOut422Number.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sifOut422Number.setStatus("current")


class _SifLrmDs1Number_Type(Integer32):
    """Custom type sifLrmDs1Number based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_SifLrmDs1Number_Type.__name__ = "Integer32"
_SifLrmDs1Number_Object = MibScalar
sifLrmDs1Number = _SifLrmDs1Number_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 60, 21),
    _SifLrmDs1Number_Type()
)
sifLrmDs1Number.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sifLrmDs1Number.setStatus("current")


class _SifOutJsineNumber_Type(Integer32):
    """Custom type sifOutJsineNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_SifOutJsineNumber_Type.__name__ = "Integer32"
_SifOutJsineNumber_Object = MibScalar
sifOutJsineNumber = _SifOutJsineNumber_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 60, 22),
    _SifOutJsineNumber_Type()
)
sifOutJsineNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sifOutJsineNumber.setStatus("current")


class _SifInpJsineNumber_Type(Integer32):
    """Custom type sifInpJsineNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10),
    )


_SifInpJsineNumber_Type.__name__ = "Integer32"
_SifInpJsineNumber_Object = MibScalar
sifInpJsineNumber = _SifInpJsineNumber_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 60, 23),
    _SifInpJsineNumber_Type()
)
sifInpJsineNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sifInpJsineNumber.setStatus("current")


class _SifOutJccNumber_Type(Integer32):
    """Custom type sifOutJccNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_SifOutJccNumber_Type.__name__ = "Integer32"
_SifOutJccNumber_Object = MibScalar
sifOutJccNumber = _SifOutJccNumber_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 60, 24),
    _SifOutJccNumber_Type()
)
sifOutJccNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sifOutJccNumber.setStatus("current")


class _SifInpJccNumber_Type(Integer32):
    """Custom type sifInpJccNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10),
    )


_SifInpJccNumber_Type.__name__ = "Integer32"
_SifInpJccNumber_Object = MibScalar
sifInpJccNumber = _SifInpJccNumber_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 60, 25),
    _SifInpJccNumber_Type()
)
sifInpJccNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sifInpJccNumber.setStatus("current")


class _SifLrmE1Number_Type(Integer32):
    """Custom type sifLrmE1Number based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_SifLrmE1Number_Type.__name__ = "Integer32"
_SifLrmE1Number_Object = MibScalar
sifLrmE1Number = _SifLrmE1Number_Object(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 60, 26),
    _SifLrmE1Number_Type()
)
sifLrmE1Number.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sifLrmE1Number.setStatus("current")

# Managed Objects groups


# Notification objects

ssuEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 601, 3, 1, 1, 52, 0, 1)
)
ssuEvent.setObjects(
      *(("SSU2000-MIB", "tpTag"),
        ("SSU2000-MIB", "tpEvt"),
        ("SSU2000-MIB", "tpId"),
        ("SSU2000-MIB", "tpMCode"),
        ("SSU2000-MIB", "tpTimestamp"),
        ("SSU2000-MIB", "tpChassis"),
        ("SSU2000-MIB", "tpSlot"),
        ("SSU2000-MIB", "tpPort"),
        ("SSU2000-MIB", "tpAlmCode"),
        ("SSU2000-MIB", "tpNtfCode"),
        ("SSU2000-MIB", "tpElevated"),
        ("SSU2000-MIB", "tpDescr"))
)
if mibBuilder.loadTexts:
    ssuEvent.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SSU2000-MIB",
    **{"OkValue": OkValue,
       "OnValue": OnValue,
       "YesValue": YesValue,
       "EnaValue": EnaValue,
       "ActiveValue": ActiveValue,
       "ValidValue": ValidValue,
       "TrueValue": TrueValue,
       "DateAndTime": DateAndTime,
       "TLocalTimeOffset": TLocalTimeOffset,
       "TModuleCode": TModuleCode,
       "TSsm": TSsm,
       "TLatAndLon": TLatAndLon,
       "TAntHeight": TAntHeight,
       "ssu2000": ssu2000,
       "inventory": inventory,
       "inventoryTable": inventoryTable,
       "inEntry": inEntry,
       "inChassis": inChassis,
       "inSlot": inSlot,
       "inModCode": inModCode,
       "inName": inName,
       "inSerial": inSerial,
       "inService": inService,
       "inHwPart": inHwPart,
       "inHwRev": inHwRev,
       "inHwDate": inHwDate,
       "inSwPart": inSwPart,
       "inSwRev": inSwRev,
       "inRevision": inRevision,
       "inShelfDesc": inShelfDesc,
       "inShelfPart": inShelfPart,
       "inInstalled": inInstalled,
       "inAction": inAction,
       "inAdapterPart": inAdapterPart,
       "inFeatureTable": inFeatureTable,
       "inFeatureEntry": inFeatureEntry,
       "inFeatureIndex": inFeatureIndex,
       "inFeature": inFeature,
       "mstatus": mstatus,
       "statusCom": statusCom,
       "statusClk": statusClk,
       "staClkTable": staClkTable,
       "staCkEntry": staCkEntry,
       "staCkChassis": staCkChassis,
       "staCkSlot": staCkSlot,
       "staCkStatus": staCkStatus,
       "staCkPLLMode": staCkPLLMode,
       "staCkTau": staCkTau,
       "staCkPql": staCkPql,
       "staCkUtc": staCkUtc,
       "statusGps": statusGps,
       "staGpsTable": staGpsTable,
       "staGpsEntry": staGpsEntry,
       "staGpsChassis": staGpsChassis,
       "staGpsSlot": staGpsSlot,
       "staGpsStatus": staGpsStatus,
       "staGpsPhaseA": staGpsPhaseA,
       "staGpsPhaseB": staGpsPhaseB,
       "staGpsUtc": staGpsUtc,
       "staGpsMStatus": staGpsMStatus,
       "staGpsMtie1A": staGpsMtie1A,
       "staGpsMtie2A": staGpsMtie2A,
       "staGpsMtie1B": staGpsMtie1B,
       "staGpsMtie2B": staGpsMtie2B,
       "staGpsFreqA": staGpsFreqA,
       "staGpsFreqB": staGpsFreqB,
       "staGpsPpsSigma": staGpsPpsSigma,
       "staGps3Sigma": staGps3Sigma,
       "stGpsPosTable": stGpsPosTable,
       "stGpsPosEntry": stGpsPosEntry,
       "stGpsPosChassis": stGpsPosChassis,
       "stGpsPosSlot": stGpsPosSlot,
       "stGpsPosValid": stGpsPosValid,
       "stGpsPosLat": stGpsPosLat,
       "stGpsPosLon": stGpsPosLon,
       "stGpsPosHgt": stGpsPosHgt,
       "stGpsPosAccurate": stGpsPosAccurate,
       "stGpsPosPdop": stGpsPosPdop,
       "stGpsPosAvg": stGpsPosAvg,
       "stGpsAvailTable": stGpsAvailTable,
       "stGpsAvEntry": stGpsAvEntry,
       "stGpsAvChassis": stGpsAvChassis,
       "stGpsAvSlot": stGpsAvSlot,
       "stGpsAvChnl": stGpsAvChnl,
       "stGpsAvPNCode": stGpsAvPNCode,
       "stGpsAvElevation": stGpsAvElevation,
       "stGpsAvAzimuth": stGpsAvAzimuth,
       "stGpsAvHealthy": stGpsAvHealthy,
       "stGpsTrackTable": stGpsTrackTable,
       "stGpsTkEntry": stGpsTkEntry,
       "stGpsTkChassis": stGpsTkChassis,
       "stGpsTkSlot": stGpsTkSlot,
       "stGpsTkChnl": stGpsTkChnl,
       "stGpsTkSv": stGpsTkSv,
       "stGpsTkSnr": stGpsTkSnr,
       "stGpsTkStatus": stGpsTkStatus,
       "statusDs1E1Inp": statusDs1E1Inp,
       "staDs1E1InpTable": staDs1E1InpTable,
       "staDiEntry": staDiEntry,
       "staDiChassis": staDiChassis,
       "staDiSlot": staDiSlot,
       "staDiPort": staDiPort,
       "staDiStatus": staDiStatus,
       "staDiPhaseA": staDiPhaseA,
       "staDiPhaseB": staDiPhaseB,
       "staDiPql": staDiPql,
       "staDiPqlRcv": staDiPqlRcv,
       "staDiLOS": staDiLOS,
       "staDiAIS": staDiAIS,
       "staDiOOF": staDiOOF,
       "staDiBPV": staDiBPV,
       "staDiCRC": staDiCRC,
       "staDiMtie1A": staDiMtie1A,
       "staDiMtie2A": staDiMtie2A,
       "staDiMtie1B": staDiMtie1B,
       "staDiMtie2B": staDiMtie2B,
       "staDiFreqA": staDiFreqA,
       "staDiFreqB": staDiFreqB,
       "staLOSErCnt": staLOSErCnt,
       "staLOSClCnt": staLOSClCnt,
       "staAISErCnt": staAISErCnt,
       "staAISClCnt": staAISClCnt,
       "staOOFErCnt": staOOFErCnt,
       "staOOFClCnt": staOOFClCnt,
       "staBPVErCnt": staBPVErCnt,
       "staBPVClCnt": staBPVClCnt,
       "staCRCErCnt": staCRCErCnt,
       "staCRCClCnt": staCRCClCnt,
       "staDiMStatus": staDiMStatus,
       "statusCcInp": statusCcInp,
       "staCcInpTable": staCcInpTable,
       "staCiEntry": staCiEntry,
       "staCiChassis": staCiChassis,
       "staCiSlot": staCiSlot,
       "staCiPort": staCiPort,
       "staCiStatus": staCiStatus,
       "staCiPhaseA": staCiPhaseA,
       "staCiPhaseB": staCiPhaseB,
       "staCiLOS": staCiLOS,
       "staCiBPV": staCiBPV,
       "staCiLOSErCnt": staCiLOSErCnt,
       "staCiLOSClCnt": staCiLOSClCnt,
       "staCiBPVErCnt": staCiBPVErCnt,
       "staCiBPVClCnt": staCiBPVClCnt,
       "staCiMStatus": staCiMStatus,
       "statusOut": statusOut,
       "staOutTable": staOutTable,
       "staOtEntry": staOtEntry,
       "staOtChassis": staOtChassis,
       "staOtSlot": staOtSlot,
       "staOtStatus": staOtStatus,
       "staOtClkSel": staOtClkSel,
       "staOtClka": staOtClka,
       "staOtClkb": staOtClkb,
       "staOtClkc": staOtClkc,
       "staOtClkd": staOtClkd,
       "staOtRednt": staOtRednt,
       "staOtPql": staOtPql,
       "staOtPortSta": staOtPortSta,
       "statusLrm": statusLrm,
       "staLrmMTable": staLrmMTable,
       "staLrmMEntry": staLrmMEntry,
       "staLrmMChassis": staLrmMChassis,
       "staLrmMSlot": staLrmMSlot,
       "staLrmMStatus": staLrmMStatus,
       "staLrmMRefSrc": staLrmMRefSrc,
       "staLrmMCtaId": staLrmMCtaId,
       "staLrmPTable": staLrmPTable,
       "staLrmPEntry": staLrmPEntry,
       "staLrmPChassis": staLrmPChassis,
       "staLrmPSlot": staLrmPSlot,
       "staLrmPPort": staLrmPPort,
       "staLrmPStatus": staLrmPStatus,
       "staLrmPFrame": staLrmPFrame,
       "staLrmPLos": staLrmPLos,
       "staLrmPAis": staLrmPAis,
       "staLrmPLof": staLrmPLof,
       "staLrmPBpv": staLrmPBpv,
       "staLrmPSlip": staLrmPSlip,
       "staLrmPSlips": staLrmPSlips,
       "staLrmPLosSide2": staLrmPLosSide2,
       "staLrmPBpvTestTime": staLrmPBpvTestTime,
       "staLrmPBpv60SRate": staLrmPBpv60SRate,
       "staLrmPBpv24HRate": staLrmPBpv24HRate,
       "staLrmPBpvErrSecs": staLrmPBpvErrSecs,
       "staLrmPBpvSevErrSecs": staLrmPBpvSevErrSecs,
       "staLrmPBpvSevErrRatio": staLrmPBpvSevErrRatio,
       "statusSineInp": statusSineInp,
       "staSineInpTable": staSineInpTable,
       "staSineiEntry": staSineiEntry,
       "staSineiChassis": staSineiChassis,
       "staSineiSlot": staSineiSlot,
       "staSineiPort": staSineiPort,
       "staSineiStatus": staSineiStatus,
       "staSineiPhaseA": staSineiPhaseA,
       "staSineiPhaseB": staSineiPhaseB,
       "staSineiLOS": staSineiLOS,
       "staSineiMStatus": staSineiMStatus,
       "staSineiPql": staSineiPql,
       "staSineiMtie1A": staSineiMtie1A,
       "staSineiMtie2A": staSineiMtie2A,
       "staSineiMtie1B": staSineiMtie1B,
       "staSineiMtie2B": staSineiMtie2B,
       "staSineiFreqA": staSineiFreqA,
       "staSineiFreqB": staSineiFreqB,
       "statusJccInp": statusJccInp,
       "staJccInpTable": staJccInpTable,
       "staJcciEntry": staJcciEntry,
       "staJcciChassis": staJcciChassis,
       "staJcciSlot": staJcciSlot,
       "staJcciPort": staJcciPort,
       "staJcciStatus": staJcciStatus,
       "staJcciPhaseA": staJcciPhaseA,
       "staJcciPhaseB": staJcciPhaseB,
       "staJcciLOS": staJcciLOS,
       "staJcciBPV": staJcciBPV,
       "staJcci400Hz": staJcci400Hz,
       "staJcciMStatus": staJcciMStatus,
       "statusLrmE1": statusLrmE1,
       "staLrme1MTable": staLrme1MTable,
       "staLrme1MEntry": staLrme1MEntry,
       "staLrme1MChassis": staLrme1MChassis,
       "staLrme1MSlot": staLrme1MSlot,
       "staLrme1MStatus": staLrme1MStatus,
       "staLrme1MRefSrc": staLrme1MRefSrc,
       "staLrme1MCtaId": staLrme1MCtaId,
       "staLrme1PTable": staLrme1PTable,
       "staLrme1PEntry": staLrme1PEntry,
       "staLrme1PChassis": staLrme1PChassis,
       "staLrme1PSlot": staLrme1PSlot,
       "staLrme1PPort": staLrme1PPort,
       "staLrme1PStatus": staLrme1PStatus,
       "staLrme1PFrame": staLrme1PFrame,
       "staLrme1PLos": staLrme1PLos,
       "staLrme1PAis": staLrme1PAis,
       "staLrme1PLof": staLrme1PLof,
       "staLrme1PBpv": staLrme1PBpv,
       "staLrme1PSlip": staLrme1PSlip,
       "staLrme1PSlips": staLrme1PSlips,
       "staLrme1PLosSide2": staLrme1PLosSide2,
       "staLrme1PBpv60SRate": staLrme1PBpv60SRate,
       "staLrme1PBpv24HRate": staLrme1PBpv24HRate,
       "staLrme1PBpvErrSecs": staLrme1PBpvErrSecs,
       "staLrme1PBpvSevErrSecs": staLrme1PBpvSevErrSecs,
       "staLrme1PBpvSevErrRatio": staLrme1PBpvSevErrRatio,
       "statusPtNtp": statusPtNtp,
       "staPtNtpTable": staPtNtpTable,
       "staPtNtpEntry": staPtNtpEntry,
       "staPtNtpChassis": staPtNtpChassis,
       "staPtNtpSlot": staPtNtpSlot,
       "staPtNtpStatus": staPtNtpStatus,
       "staPtNtpClkSel": staPtNtpClkSel,
       "staPtNtpClka": staPtNtpClka,
       "staPtNtpClkb": staPtNtpClkb,
       "staPtNtpClkc": staPtNtpClkc,
       "staPtNtpClkd": staPtNtpClkd,
       "staPtNtpRednt": staPtNtpRednt,
       "staPtNtpModState": staPtNtpModState,
       "staPtNtpPAState": staPtNtpPAState,
       "staPtNtpPBState": staPtNtpPBState,
       "staPtNtpTod": staPtNtpTod,
       "staPtNtpCommit": staPtNtpCommit,
       "statusPtPtp": statusPtPtp,
       "staPtPtpTable": staPtPtpTable,
       "staPtPtpEntry": staPtPtpEntry,
       "staPtPtpChassis": staPtPtpChassis,
       "staPtPtpSlot": staPtPtpSlot,
       "staPtPtpStatus": staPtPtpStatus,
       "staPtPtpClkSel": staPtPtpClkSel,
       "staPtPtpClka": staPtPtpClka,
       "staPtPtpClkb": staPtPtpClkb,
       "staPtPtpClkc": staPtPtpClkc,
       "staPtPtpClkd": staPtPtpClkd,
       "staPtPtpRednt": staPtPtpRednt,
       "staPtPtpModState": staPtPtpModState,
       "staPtPtpPAState": staPtPtpPAState,
       "staPtPtpTod": staPtPtpTod,
       "staPtPtpCommit": staPtPtpCommit,
       "ptpDfltDataSetTable": ptpDfltDataSetTable,
       "ptpDfltDataSetEntry": ptpDfltDataSetEntry,
       "ptpDfltDataSetChassis": ptpDfltDataSetChassis,
       "ptpDfltDataSetSlot": ptpDfltDataSetSlot,
       "ptpDfltDataSetClockId": ptpDfltDataSetClockId,
       "ptpDfltDataSetClockClass": ptpDfltDataSetClockClass,
       "ptpDfltDataSetClockAccuracy": ptpDfltDataSetClockAccuracy,
       "ptpDfltDataSetTimeTraceable": ptpDfltDataSetTimeTraceable,
       "ptpDfltDataSetFreqTraceable": ptpDfltDataSetFreqTraceable,
       "ptpDfltDataSetDomainNumber": ptpDfltDataSetDomainNumber,
       "ptpClockDescrTable": ptpClockDescrTable,
       "ptpClockDescrEntry": ptpClockDescrEntry,
       "ptpClockDescrChassis": ptpClockDescrChassis,
       "ptpClockDescrSlot": ptpClockDescrSlot,
       "ptpClockDescrClockType": ptpClockDescrClockType,
       "ptpClockDescrProtocolAddress": ptpClockDescrProtocolAddress,
       "ptpClockDescrManufacturerId": ptpClockDescrManufacturerId,
       "ptpClockDescrProfileId": ptpClockDescrProfileId,
       "ptpTimeMessageTable": ptpTimeMessageTable,
       "ptpTimeMessageEntry": ptpTimeMessageEntry,
       "ptpTimeMessageChassis": ptpTimeMessageChassis,
       "ptpTimeMessageSlot": ptpTimeMessageSlot,
       "ptpTimeMessageCurrentTimeSec": ptpTimeMessageCurrentTimeSec,
       "ptpTimeMessageCurrentTimeNSec": ptpTimeMessageCurrentTimeNSec,
       "ptpPortDataSetTable": ptpPortDataSetTable,
       "ptpPortDataSetEntry": ptpPortDataSetEntry,
       "ptpPortDataSetChassis": ptpPortDataSetChassis,
       "ptpPortDataSetSlot": ptpPortDataSetSlot,
       "ptpPortDataSetClockId": ptpPortDataSetClockId,
       "ptpPortDataSetPortNumber": ptpPortDataSetPortNumber,
       "ptpPortDataSetPortState": ptpPortDataSetPortState,
       "statusSynce": statusSynce,
       "staSynceTable": staSynceTable,
       "staSynceEntry": staSynceEntry,
       "staSynceChassis": staSynceChassis,
       "staSynceSlot": staSynceSlot,
       "staSyncePortDirection": staSyncePortDirection,
       "staSynceEthernetMode": staSynceEthernetMode,
       "staSynceRxSsm": staSynceRxSsm,
       "staSynceTxSsm": staSynceTxSsm,
       "msetup": msetup,
       "setupCom": setupCom,
       "setCmId": setCmId,
       "setCmInfo": setCmInfo,
       "setCmVer": setCmVer,
       "setCmName": setCmName,
       "setupClk": setupClk,
       "setClkTable": setClkTable,
       "setCkEntry": setCkEntry,
       "setCkChassis": setCkChassis,
       "setCkSlot": setCkSlot,
       "setCkWarmup": setCkWarmup,
       "setCkMinTau": setCkMinTau,
       "setCkMaxTau": setCkMaxTau,
       "setCkPLLMode": setCkPLLMode,
       "setCkTodTimeout": setCkTodTimeout,
       "setCkFreqTimeout": setCkFreqTimeout,
       "setupGps": setupGps,
       "setGpsTable": setGpsTable,
       "setGpsEntry": setGpsEntry,
       "setGpsChassis": setGpsChassis,
       "setGpsSlot": setGpsSlot,
       "setGpsEngine": setGpsEngine,
       "setGpsProvPql": setGpsProvPql,
       "setGpsPriority": setGpsPriority,
       "setGpsPdop": setGpsPdop,
       "setGpsPosel": setGpsPosel,
       "setGpsTimel": setGpsTimel,
       "setGpsAvg": setGpsAvg,
       "setGpsLat": setGpsLat,
       "setGpsLon": setGpsLon,
       "setGpsHgt": setGpsHgt,
       "setGpsZeroPhase": setGpsZeroPhase,
       "setGpsTodsrcPriority": setGpsTodsrcPriority,
       "setGpsTodsrcCompensation": setGpsTodsrcCompensation,
       "setGnssConsMode": setGnssConsMode,
       "setAlmThGpsInpTable": setAlmThGpsInpTable,
       "setMgEntry": setMgEntry,
       "setMgChassis": setMgChassis,
       "setMgSlot": setMgSlot,
       "setMgMtieStd": setMgMtieStd,
       "setMgMtie10EL1": setMgMtie10EL1,
       "setMgMtie10EL2": setMgMtie10EL2,
       "setMgMtie10CL1": setMgMtie10CL1,
       "setMgMtie10CL2": setMgMtie10CL2,
       "setMgMtie100EL1": setMgMtie100EL1,
       "setMgMtie100EL2": setMgMtie100EL2,
       "setMgMtie100CL1": setMgMtie100CL1,
       "setMgMtie100CL2": setMgMtie100CL2,
       "setMgMtie1000EL1": setMgMtie1000EL1,
       "setMgMtie1000EL2": setMgMtie1000EL2,
       "setMgMtie1000CL1": setMgMtie1000CL1,
       "setMgMtie1000CL2": setMgMtie1000CL2,
       "setMgMtie10000EL1": setMgMtie10000EL1,
       "setMgMtie10000EL2": setMgMtie10000EL2,
       "setMgMtie10000CL1": setMgMtie10000CL1,
       "setMgMtie10000CL2": setMgMtie10000CL2,
       "setMgMtie100000EL1": setMgMtie100000EL1,
       "setMgMtie100000EL2": setMgMtie100000EL2,
       "setMgMtie100000CL1": setMgMtie100000CL1,
       "setMgMtie100000CL2": setMgMtie100000CL2,
       "setMgFreqAErrLmt": setMgFreqAErrLmt,
       "setMgFreqAClrLmt": setMgFreqAClrLmt,
       "setMgFreqATau": setMgFreqATau,
       "setMgFreqBErrLmt": setMgFreqBErrLmt,
       "setMgFreqBClrLmt": setMgFreqBClrLmt,
       "setMgFreqBTau": setMgFreqBTau,
       "setupDs1E1Inp": setupDs1E1Inp,
       "setDs1E1InpTable": setDs1E1InpTable,
       "setDiEntry": setDiEntry,
       "setDiChassis": setDiChassis,
       "setDiSlot": setDiSlot,
       "setDiPort": setDiPort,
       "setDiEnable": setDiEnable,
       "setDiFrame": setDiFrame,
       "setDiZS": setDiZS,
       "setDiCRC": setDiCRC,
       "setDiSSM": setDiSSM,
       "setDiProvPql": setDiProvPql,
       "setDiPriority": setDiPriority,
       "setDiGain": setDiGain,
       "setDiCSFlt": setDiCSFlt,
       "setDiE1SsmBit": setDiE1SsmBit,
       "setDiZeroPhase": setDiZeroPhase,
       "setDiMtieCalc": setDiMtieCalc,
       "setAlmThDs1E1InpTable": setAlmThDs1E1InpTable,
       "setMiEntry": setMiEntry,
       "setMiChassis": setMiChassis,
       "setMiSlot": setMiSlot,
       "setMiPort": setMiPort,
       "setMiMtieStd": setMiMtieStd,
       "setMiMtie10EL1": setMiMtie10EL1,
       "setMiMtie10EL2": setMiMtie10EL2,
       "setMiMtie10CL1": setMiMtie10CL1,
       "setMiMtie10CL2": setMiMtie10CL2,
       "setMiMtie100EL1": setMiMtie100EL1,
       "setMiMtie100EL2": setMiMtie100EL2,
       "setMiMtie100CL1": setMiMtie100CL1,
       "setMiMtie100CL2": setMiMtie100CL2,
       "setMiMtie1000EL1": setMiMtie1000EL1,
       "setMiMtie1000EL2": setMiMtie1000EL2,
       "setMiMtie1000CL1": setMiMtie1000CL1,
       "setMiMtie1000CL2": setMiMtie1000CL2,
       "setMiMtie10000EL1": setMiMtie10000EL1,
       "setMiMtie10000EL2": setMiMtie10000EL2,
       "setMiMtie10000CL1": setMiMtie10000CL1,
       "setMiMtie10000CL2": setMiMtie10000CL2,
       "setMiMtie100000EL1": setMiMtie100000EL1,
       "setMiMtie100000EL2": setMiMtie100000EL2,
       "setMiMtie100000CL1": setMiMtie100000CL1,
       "setMiMtie100000CL2": setMiMtie100000CL2,
       "setMiFreqAErrLmt": setMiFreqAErrLmt,
       "setMiFreqAClrLmt": setMiFreqAClrLmt,
       "setMiFreqATau": setMiFreqATau,
       "setMiFreqBErrLmt": setMiFreqBErrLmt,
       "setMiFreqBClrLmt": setMiFreqBClrLmt,
       "setMiFreqBTau": setMiFreqBTau,
       "setMiLOSErrCnt": setMiLOSErrCnt,
       "setMiLOSClrCnt": setMiLOSClrCnt,
       "setMiAISErrCnt": setMiAISErrCnt,
       "setMiAISClrCnt": setMiAISClrCnt,
       "setMiOOFErrCnt": setMiOOFErrCnt,
       "setMiOOFClrCnt": setMiOOFClrCnt,
       "setMiBPVErrCnt": setMiBPVErrCnt,
       "setMiBPVClrCnt": setMiBPVClrCnt,
       "setMiCRCErrCnt": setMiCRCErrCnt,
       "setMiCRCClrCnt": setMiCRCClrCnt,
       "setupCcInp": setupCcInp,
       "setCcInpTable": setCcInpTable,
       "setCiEntry": setCiEntry,
       "setCiChassis": setCiChassis,
       "setCiSlot": setCiSlot,
       "setCiPort": setCiPort,
       "setCiEnable": setCiEnable,
       "setCiProvPql": setCiProvPql,
       "setCiPriority": setCiPriority,
       "setCiZeroPhase": setCiZeroPhase,
       "setAlmThCcInpTable": setAlmThCcInpTable,
       "setCimEntry": setCimEntry,
       "setCimChassis": setCimChassis,
       "setCimSlot": setCimSlot,
       "setCimPort": setCimPort,
       "setCimLOSErrCnt": setCimLOSErrCnt,
       "setCimLOSClrCnt": setCimLOSClrCnt,
       "setCimBPVErrCnt": setCimBPVErrCnt,
       "setCimBPVClrCnt": setCimBPVClrCnt,
       "setupDs1Out": setupDs1Out,
       "setDsTable": setDsTable,
       "setDsEntry": setDsEntry,
       "setDsChassis": setDsChassis,
       "setDsSlot": setDsSlot,
       "setDsFrame": setDsFrame,
       "setDsBypass": setDsBypass,
       "setDsZs": setDsZs,
       "setDsEnable": setDsEnable,
       "setDsLength": setDsLength,
       "setupE1Out": setupE1Out,
       "setE1Table": setE1Table,
       "setE1Entry": setE1Entry,
       "setE1Chassis": setE1Chassis,
       "setE1Slot": setE1Slot,
       "setE1Frame": setE1Frame,
       "setE1Bypass": setE1Bypass,
       "setE1Zs": setE1Zs,
       "setE1Crc": setE1Crc,
       "setE1SsmBit": setE1SsmBit,
       "setE1Enable": setE1Enable,
       "setup2048Out": setup2048Out,
       "setCoTable": setCoTable,
       "setCoEntry": setCoEntry,
       "setCoChassis": setCoChassis,
       "setCoSlot": setCoSlot,
       "setCoBypass": setCoBypass,
       "setCoFltMode": setCoFltMode,
       "setCoEnable": setCoEnable,
       "setCoSquelch": setCoSquelch,
       "setupCCOut": setupCCOut,
       "setCcTable": setCcTable,
       "setCcEntry": setCcEntry,
       "setCcChassis": setCcChassis,
       "setCcSlot": setCcSlot,
       "setCcBypass": setCcBypass,
       "setCcEnable": setCcEnable,
       "setCcDuty": setCcDuty,
       "setCcComp": setCcComp,
       "setup422Out": setup422Out,
       "set422oTable": set422oTable,
       "set422oEntry": set422oEntry,
       "set422oChassis": set422oChassis,
       "set422oSlot": set422oSlot,
       "set422oBypass": set422oBypass,
       "set422oFltMode": set422oFltMode,
       "set422oEnable": set422oEnable,
       "set422oFrequency": set422oFrequency,
       "setupE12048Out": setupE12048Out,
       "setE12048oTable": setE12048oTable,
       "setE12048oEntry": setE12048oEntry,
       "setE12048oChassis": setE12048oChassis,
       "setE12048oSlot": setE12048oSlot,
       "setE12048oBypass": setE12048oBypass,
       "setE12048oZs": setE12048oZs,
       "setE12048oSignal": setE12048oSignal,
       "setE12048oEnable": setE12048oEnable,
       "setE12048oSquelch": setE12048oSquelch,
       "setE12048oFrame": setE12048oFrame,
       "setE12048oCrc": setE12048oCrc,
       "setE12048oSsm": setE12048oSsm,
       "setE12048oSsmBit": setE12048oSsmBit,
       "setupLrm": setupLrm,
       "setLrmPTable": setLrmPTable,
       "setLrmPEntry": setLrmPEntry,
       "setLrmPChassis": setLrmPChassis,
       "setLrmPSlot": setLrmPSlot,
       "setLrmPPort": setLrmPPort,
       "setLrmPEnable": setLrmPEnable,
       "setLrmPLbo": setLrmPLbo,
       "setLrmPSlip": setLrmPSlip,
       "setLrmPBpv": setLrmPBpv,
       "setLrmPFlt": setLrmPFlt,
       "setLrmPCid": setLrmPCid,
       "setupSineOut": setupSineOut,
       "setSineoTable": setSineoTable,
       "setSineoEntry": setSineoEntry,
       "setSineoChassis": setSineoChassis,
       "setSineoSlot": setSineoSlot,
       "setSineoBypass": setSineoBypass,
       "setSineoFrequency": setSineoFrequency,
       "setSineoEnable": setSineoEnable,
       "setSineoSquelch": setSineoSquelch,
       "setupSineInp": setupSineInp,
       "setSineInpTable": setSineInpTable,
       "setSineiEntry": setSineiEntry,
       "setSineiChassis": setSineiChassis,
       "setSineiSlot": setSineiSlot,
       "setSineiPort": setSineiPort,
       "setSineiEnable": setSineiEnable,
       "setSineiFrequency": setSineiFrequency,
       "setSineiProvPql": setSineiProvPql,
       "setSineiPriority": setSineiPriority,
       "setSineiCSFlt": setSineiCSFlt,
       "setSineiZeroPhase": setSineiZeroPhase,
       "setAlmThSineInpTable": setAlmThSineInpTable,
       "setMsiEntry": setMsiEntry,
       "setMsiChassis": setMsiChassis,
       "setMsiSlot": setMsiSlot,
       "setMsiPort": setMsiPort,
       "setMsiMtieStd": setMsiMtieStd,
       "setMsiMtie10EL1": setMsiMtie10EL1,
       "setMsiMtie10EL2": setMsiMtie10EL2,
       "setMsiMtie10CL1": setMsiMtie10CL1,
       "setMsiMtie10CL2": setMsiMtie10CL2,
       "setMsiMtie100EL1": setMsiMtie100EL1,
       "setMsiMtie100EL2": setMsiMtie100EL2,
       "setMsiMtie100CL1": setMsiMtie100CL1,
       "setMsiMtie100CL2": setMsiMtie100CL2,
       "setMsiMtie1000EL1": setMsiMtie1000EL1,
       "setMsiMtie1000EL2": setMsiMtie1000EL2,
       "setMsiMtie1000CL1": setMsiMtie1000CL1,
       "setMsiMtie1000CL2": setMsiMtie1000CL2,
       "setMsiMtie10000EL1": setMsiMtie10000EL1,
       "setMsiMtie10000EL2": setMsiMtie10000EL2,
       "setMsiMtie10000CL1": setMsiMtie10000CL1,
       "setMsiMtie10000CL2": setMsiMtie10000CL2,
       "setMsiMtie100000EL1": setMsiMtie100000EL1,
       "setMsiMtie100000EL2": setMsiMtie100000EL2,
       "setMsiMtie100000CL1": setMsiMtie100000CL1,
       "setMsiMtie100000CL2": setMsiMtie100000CL2,
       "setMsiFreqAErrLmt": setMsiFreqAErrLmt,
       "setMsiFreqAClrLmt": setMsiFreqAClrLmt,
       "setMsiFreqATau": setMsiFreqATau,
       "setMsiFreqBErrLmt": setMsiFreqBErrLmt,
       "setMsiFreqBClrLmt": setMsiFreqBClrLmt,
       "setMsiFreqBTau": setMsiFreqBTau,
       "setupJccOut": setupJccOut,
       "setJccoTable": setJccoTable,
       "setJccoEntry": setJccoEntry,
       "setJccoChassis": setJccoChassis,
       "setJccoSlot": setJccoSlot,
       "setJccoBypass": setJccoBypass,
       "setJcco400Hz": setJcco400Hz,
       "setJccoEnable": setJccoEnable,
       "setJccoComp": setJccoComp,
       "setupJccInp": setupJccInp,
       "setJccInpTable": setJccInpTable,
       "setJcciEntry": setJcciEntry,
       "setJcciChassis": setJcciChassis,
       "setJcciSlot": setJcciSlot,
       "setJcciPort": setJcciPort,
       "setJcciEnable": setJcciEnable,
       "setJcciProvPql": setJcciProvPql,
       "setJcciPriority": setJcciPriority,
       "setJcci400Hz": setJcci400Hz,
       "setJcciZeroPhase": setJcciZeroPhase,
       "setupLrmE1": setupLrmE1,
       "setLrme1PTable": setLrme1PTable,
       "setLrme1PEntry": setLrme1PEntry,
       "setLrme1PChassis": setLrme1PChassis,
       "setLrme1PSlot": setLrme1PSlot,
       "setLrme1PPort": setLrme1PPort,
       "setLrme1PEnable": setLrme1PEnable,
       "setLrme1PSlip": setLrme1PSlip,
       "setLrme1PBpv": setLrme1PBpv,
       "setLrme1PFlt": setLrme1PFlt,
       "setLrme1PCid": setLrme1PCid,
       "setupPtNtp": setupPtNtp,
       "setPtNtpTable": setPtNtpTable,
       "setPtNtpEntry": setPtNtpEntry,
       "setPtNtpChassis": setPtNtpChassis,
       "setPtNtpSlot": setPtNtpSlot,
       "setPtNtpCommit": setPtNtpCommit,
       "setPtNtpProbe": setPtNtpProbe,
       "setPtNtpBond": setPtNtpBond,
       "setPtNtpNTPd": setPtNtpNTPd,
       "setPtNtpTodsrcPrefer": setPtNtpTodsrcPrefer,
       "setPtNtpTodsrcPriority": setPtNtpTodsrcPriority,
       "setPtNtpWeight": setPtNtpWeight,
       "setPtNtpCompensation": setPtNtpCompensation,
       "setPtNtpPeerTimeout": setPtNtpPeerTimeout,
       "setPtNtpPeerPrefer": setPtNtpPeerPrefer,
       "setPtNtpBypass": setPtNtpBypass,
       "setPtNtpModActive": setPtNtpModActive,
       "setPtNtpPAActive": setPtNtpPAActive,
       "setPtNtpPBActive": setPtNtpPBActive,
       "setPtNtpPortTable": setPtNtpPortTable,
       "setPtNtpPortEntry": setPtNtpPortEntry,
       "setPtNtpPortChassis": setPtNtpPortChassis,
       "setPtNtpPortSlot": setPtNtpPortSlot,
       "setPtNtpPortNum": setPtNtpPortNum,
       "setPtNtpPortAddr": setPtNtpPortAddr,
       "setPtNtpPortMask": setPtNtpPortMask,
       "setPtNtpPortGate": setPtNtpPortGate,
       "setPtNtpPeerTable": setPtNtpPeerTable,
       "setPtNtpPeerEntry": setPtNtpPeerEntry,
       "setPtNtpPeerChassis": setPtNtpPeerChassis,
       "setPtNtpPeerSlot": setPtNtpPeerSlot,
       "setPtNtpPeerNum": setPtNtpPeerNum,
       "setPtNtpPeerAddr": setPtNtpPeerAddr,
       "setPtNtpPeerPmin": setPtNtpPeerPmin,
       "setPtNtpPeerPmax": setPtNtpPeerPmax,
       "setPtNtpPeerKeyId": setPtNtpPeerKeyId,
       "setPtNtpAuthTable": setPtNtpAuthTable,
       "setPtNtpAuthEntry": setPtNtpAuthEntry,
       "setPtNtpAuthChassis": setPtNtpAuthChassis,
       "setPtNtpAuthSlot": setPtNtpAuthSlot,
       "setPtNtpAuthNum": setPtNtpAuthNum,
       "setPtNtpAuthKeyId": setPtNtpAuthKeyId,
       "setPtNtpAuthKeyValue": setPtNtpAuthKeyValue,
       "setPtNtpRouteTable": setPtNtpRouteTable,
       "setPtNtpRouteEntry": setPtNtpRouteEntry,
       "setPtNtpRouteChassis": setPtNtpRouteChassis,
       "setPtNtpRouteSlot": setPtNtpRouteSlot,
       "setPtNtpRouteNum": setPtNtpRouteNum,
       "setPtNtpRouteAddr": setPtNtpRouteAddr,
       "setPtNtpRouteMask": setPtNtpRouteMask,
       "setPtNtpRouteGate": setPtNtpRouteGate,
       "setPtNtpRouteIface": setPtNtpRouteIface,
       "setPtNtpVlanTable": setPtNtpVlanTable,
       "setPtNtpVlanEntry": setPtNtpVlanEntry,
       "setPtNtpVlanChassis": setPtNtpVlanChassis,
       "setPtNtpVlanSlot": setPtNtpVlanSlot,
       "setPtNtpVlan": setPtNtpVlan,
       "setPtNtpVlanPAId": setPtNtpVlanPAId,
       "setPtNtpVlanPAPriority": setPtNtpVlanPAPriority,
       "setPtNtpVlanPBId": setPtNtpVlanPBId,
       "setPtNtpVlanPBPriority": setPtNtpVlanPBPriority,
       "setPtNtpVlanBondId": setPtNtpVlanBondId,
       "setPtNtpVlanBondPriority": setPtNtpVlanBondPriority,
       "setupPtPtp": setupPtPtp,
       "setPtPtpTable": setPtPtpTable,
       "setPtPtpEntry": setPtPtpEntry,
       "setPtPtpChassis": setPtPtpChassis,
       "setPtPtpSlot": setPtPtpSlot,
       "setPtPtpCommit": setPtPtpCommit,
       "setPtPtpService": setPtPtpService,
       "setPtPtpClockId": setPtPtpClockId,
       "setPtPtpDomain": setPtPtpDomain,
       "setPtPtpTimescale": setPtPtpTimescale,
       "setPtPtpSyncLimit": setPtPtpSyncLimit,
       "setPtPtpAnnounceLimit": setPtPtpAnnounceLimit,
       "setPtPtpDelayLimit": setPtPtpDelayLimit,
       "setPtPtpDscpState": setPtPtpDscpState,
       "setPtPtpDscpValue": setPtPtpDscpValue,
       "setPtPtpMaxClient": setPtPtpMaxClient,
       "setPtPtpPortPriority1": setPtPtpPortPriority1,
       "setPtPtpPortPriority2": setPtPtpPortPriority2,
       "setPtPtpUniLeaseDuration": setPtPtpUniLeaseDuration,
       "setPtPtpUniNegotiation": setPtPtpUniNegotiation,
       "setPtPtpTwostep": setPtPtpTwostep,
       "setPtPtpProfile": setPtPtpProfile,
       "setPtPtpSsmOption": setPtPtpSsmOption,
       "setPtPtpBypass": setPtPtpBypass,
       "setPtPtpModActive": setPtPtpModActive,
       "setPtPtpEthRate": setPtPtpEthRate,
       "setPtPtpVlan": setPtPtpVlan,
       "setPtPtpRmvClient": setPtPtpRmvClient,
       "setPtpPortTable": setPtpPortTable,
       "setPtpPortEntry": setPtpPortEntry,
       "setPtpPortChassis": setPtpPortChassis,
       "setPtpPortSlot": setPtpPortSlot,
       "setPtpPortNum": setPtpPortNum,
       "setPtpPortAddr": setPtpPortAddr,
       "setPtpPortMask": setPtpPortMask,
       "setPtpPortGate": setPtpPortGate,
       "setPtpVlanTable": setPtpVlanTable,
       "setPtpVlanEntry": setPtpVlanEntry,
       "setPtpVlanChassis": setPtpVlanChassis,
       "setPtpVlanSlot": setPtpVlanSlot,
       "setPtpVlanIndex": setPtpVlanIndex,
       "setPtpVlanState": setPtpVlanState,
       "setPtpVlanAddr": setPtpVlanAddr,
       "setPtpVlanMask": setPtpVlanMask,
       "setPtpVlanGate": setPtpVlanGate,
       "setPtpVlanId": setPtpVlanId,
       "setPtpVlanPriority": setPtpVlanPriority,
       "setupSynce": setupSynce,
       "setSynceTable": setSynceTable,
       "setSynceEntry": setSynceEntry,
       "setSynceChassis": setSynceChassis,
       "setSynceSlot": setSynceSlot,
       "setSyncePortDirection": setSyncePortDirection,
       "setSynceEsmc": setSynceEsmc,
       "setSynceQl": setSynceQl,
       "setSynceOutQl": setSynceOutQl,
       "general": general,
       "infoTable": infoTable,
       "giEntry": giEntry,
       "giChassis": giChassis,
       "giSlot": giSlot,
       "giSystime": giSystime,
       "giElevation": giElevation,
       "giSetup": giSetup,
       "giRestart": giRestart,
       "event": event,
       "evCount": evCount,
       "evType": evType,
       "eventTable": eventTable,
       "evEntry": evEntry,
       "evIndex": evIndex,
       "evT": evT,
       "alarm": alarm,
       "alarmTable": alarmTable,
       "almEntry": almEntry,
       "almChassis": almChassis,
       "almSlot": almSlot,
       "almPort": almPort,
       "almIndex": almIndex,
       "almId": almId,
       "almName": almName,
       "almLevel": almLevel,
       "almElevate": almElevate,
       "almStatus": almStatus,
       "setAlmLoc": setAlmLoc,
       "setAlmTable": setAlmTable,
       "salEntry": salEntry,
       "salChassis": salChassis,
       "salSlot": salSlot,
       "salPort": salPort,
       "salIndex": salIndex,
       "salId": salId,
       "salName": salName,
       "salSet": salSet,
       "salElevate": salElevate,
       "salLevel": salLevel,
       "salDelay": salDelay,
       "ref": ref,
       "refClk": refClk,
       "refInp": refInp,
       "refBypass": refBypass,
       "refClkSwitch": refClkSwitch,
       "refInpSwitch": refInpSwitch,
       "refInpSelection": refInpSelection,
       "refClkTodsrc": refClkTodsrc,
       "phase": phase,
       "phaseTable": phaseTable,
       "phEntry": phEntry,
       "phChassis": phChassis,
       "phSlot": phSlot,
       "phPort": phPort,
       "phA": phA,
       "phB": phB,
       "ph100A": ph100A,
       "ph100B": ph100B,
       "ph1000A": ph1000A,
       "ph1000B": ph1000B,
       "ph10000A": ph10000A,
       "ph10000B": ph10000B,
       "phHisInpLoc": phHisInpLoc,
       "phHisTimeAvg": phHisTimeAvg,
       "phHisClk": phHisClk,
       "phHisCnt": phHisCnt,
       "phHisTable": phHisTable,
       "phHisEntry": phHisEntry,
       "phHisChassis": phHisChassis,
       "phHisSlot": phHisSlot,
       "phHisPort": phHisPort,
       "phHisIndex": phHisIndex,
       "phHisV": phHisV,
       "freq": freq,
       "freqTable": freqTable,
       "fqEntry": fqEntry,
       "fqChassis": fqChassis,
       "fqSlot": fqSlot,
       "fqPort": fqPort,
       "fqA": fqA,
       "fqB": fqB,
       "ntp": ntp,
       "ntpMode": ntpMode,
       "ntpSysPeer": ntpSysPeer,
       "ntpSysPeerOffset": ntpSysPeerOffset,
       "peerStaTable": peerStaTable,
       "peerStaEntry": peerStaEntry,
       "peerStaIndex": peerStaIndex,
       "peerStaAddress": peerStaAddress,
       "peerStaHomeMode": peerStaHomeMode,
       "peerStaParentMode": peerStaParentMode,
       "peerStaLeap": peerStaLeap,
       "peerStaStratum": peerStaStratum,
       "peerStaPrecision": peerStaPrecision,
       "peerStaDelay": peerStaDelay,
       "peerStaDispersion": peerStaDispersion,
       "peerStaOffset": peerStaOffset,
       "peerStaSentCnt": peerStaSentCnt,
       "peerStaProcessCnt": peerStaProcessCnt,
       "peerStaSanity": peerStaSanity,
       "ntpTable": ntpTable,
       "ntpEntry": ntpEntry,
       "ntpIndex": ntpIndex,
       "ntpPeer": ntpPeer,
       "ntpPeerType": ntpPeerType,
       "ntpBrdTimer": ntpBrdTimer,
       "ntpAddClient": ntpAddClient,
       "ntpAddBrd": ntpAddBrd,
       "ntpAddBclient": ntpAddBclient,
       "ntpDelPeer": ntpDelPeer,
       "ntpClr": ntpClr,
       "ntpBTimer": ntpBTimer,
       "ntpPrefer": ntpPrefer,
       "time": time,
       "tmCurTime": tmCurTime,
       "tmLocalOffset": tmLocalOffset,
       "pqlTable": pqlTable,
       "pqlDs1Table": pqlDs1Table,
       "pqlDs1Entry": pqlDs1Entry,
       "pqlDs1Index": pqlDs1Index,
       "pqlDs1Ssm": pqlDs1Ssm,
       "pqlDs1Descr": pqlDs1Descr,
       "pqlE1Table": pqlE1Table,
       "pqlE1Entry": pqlE1Entry,
       "pqlE1Index": pqlE1Index,
       "pqlE1Ssm": pqlE1Ssm,
       "pqlE1Descr": pqlE1Descr,
       "pqlReset": pqlReset,
       "ioname": ioname,
       "ionameTable": ionameTable,
       "ionEntry": ionEntry,
       "ionChassis": ionChassis,
       "ionSlot": ionSlot,
       "ionPort": ionPort,
       "ionName": ionName,
       "ionameLoc": ionameLoc,
       "ionameSet": ionameSet,
       "comm": comm,
       "com232Table": com232Table,
       "comEntry": comEntry,
       "comIndex": comIndex,
       "comMode": comMode,
       "comEcho": comEcho,
       "comEol": comEol,
       "comBaud": comBaud,
       "comParmTable": comParmTable,
       "comParmEntry": comParmEntry,
       "comParmIndex": comParmIndex,
       "comType": comType,
       "comTimeout": comTimeout,
       "comLogoff": comLogoff,
       "snmpman": snmpman,
       "snmpv2manTable": snmpv2manTable,
       "snmpv2manEntry": snmpv2manEntry,
       "snmpv2manIndex": snmpv2manIndex,
       "snmpv2manIp": snmpv2manIp,
       "snmpmanInit": snmpmanInit,
       "snmpmanTrap": snmpmanTrap,
       "snmpNotification": snmpNotification,
       "snmpEnable": snmpEnable,
       "snmpv2userTable": snmpv2userTable,
       "snmpv2userEntry": snmpv2userEntry,
       "snmpv2userIndex": snmpv2userIndex,
       "snmpv2user": snmpv2user,
       "snmpv3userTable": snmpv3userTable,
       "snmpv3userEntry": snmpv3userEntry,
       "snmpv3userIndex": snmpv3userIndex,
       "snmpv3user": snmpv3user,
       "snmpv3manTable": snmpv3manTable,
       "snmpv3manEntry": snmpv3manEntry,
       "snmpv3manIndex": snmpv3manIndex,
       "snmpv3manIp": snmpv3manIp,
       "snmpv3manUser": snmpv3manUser,
       "sys": sys,
       "sysPbo": sysPbo,
       "sysResetClk": sysResetClk,
       "sysKeepAliveTable": sysKeepAliveTable,
       "sysAliveEntry": sysAliveEntry,
       "sysAliveIndex": sysAliveIndex,
       "sysAliveType": sysAliveType,
       "sysAliveTime": sysAliveTime,
       "sysOpmode": sysOpmode,
       "sysTl1Format": sysTl1Format,
       "sysEvtLogin": sysEvtLogin,
       "sysAco": sysAco,
       "users": users,
       "userTable": userTable,
       "userEntry": userEntry,
       "userIndex": userIndex,
       "userlevel": userlevel,
       "username": username,
       "who": who,
       "whoTable": whoTable,
       "whoEntry": whoEntry,
       "whoIndex": whoIndex,
       "whoPort": whoPort,
       "whoName": whoName,
       "ntpq": ntpq,
       "ntpqXeq": ntpqXeq,
       "ntpqTable": ntpqTable,
       "ntpqEntry": ntpqEntry,
       "ntpqChassis": ntpqChassis,
       "ntpqSlot": ntpqSlot,
       "ntpqIndex": ntpqIndex,
       "ntpqValid": ntpqValid,
       "ntpqPeer": ntpqPeer,
       "ntpqRefid": ntpqRefid,
       "ntpqStratum": ntpqStratum,
       "ntpqPoll": ntpqPoll,
       "ntpqReach": ntpqReach,
       "ntpqDelay": ntpqDelay,
       "ntpqOffset": ntpqOffset,
       "ntpqJitter": ntpqJitter,
       "ntpqSyspeer": ntpqSyspeer,
       "ntpqSysleap": ntpqSysleap,
       "ntpqSysstratum": ntpqSysstratum,
       "ntpqSysprecision": ntpqSysprecision,
       "ntpqRootdelay": ntpqRootdelay,
       "ntpqRootdispersion": ntpqRootdispersion,
       "ntpqSysoffset": ntpqSysoffset,
       "ntpqReftime": ntpqReftime,
       "route": route,
       "rtXeq": rtXeq,
       "routeTable": routeTable,
       "rtEntry": rtEntry,
       "rtChassis": rtChassis,
       "rtSlot": rtSlot,
       "rtIndex": rtIndex,
       "rtValid": rtValid,
       "rtDest": rtDest,
       "rtGate": rtGate,
       "rtMask": rtMask,
       "rtFlags": rtFlags,
       "rtMetric": rtMetric,
       "rtRef": rtRef,
       "rtUse": rtUse,
       "rtIface": rtIface,
       "mtie": mtie,
       "mtInpLoc": mtInpLoc,
       "mtFrTime": mtFrTime,
       "mtToTime": mtToTime,
       "mtTable": mtTable,
       "mtEntry": mtEntry,
       "mtChassis": mtChassis,
       "mtSlot": mtSlot,
       "mtPort": mtPort,
       "mtA": mtA,
       "mtB": mtB,
       "mtHisInpLoc": mtHisInpLoc,
       "mtHisClk": mtHisClk,
       "mtHisCnt": mtHisCnt,
       "mtHisTable": mtHisTable,
       "mtHisEntry": mtHisEntry,
       "mtHisChassis": mtHisChassis,
       "mtHisSlot": mtHisSlot,
       "mtHisPort": mtHisPort,
       "mtHisIndex": mtHisIndex,
       "mtHisV": mtHisV,
       "tdev": tdev,
       "tdInpLoc": tdInpLoc,
       "tdFrTime": tdFrTime,
       "tdToTime": tdToTime,
       "tdTable": tdTable,
       "tdEntry": tdEntry,
       "tdChassis": tdChassis,
       "tdSlot": tdSlot,
       "tdPort": tdPort,
       "tdA": tdA,
       "tdB": tdB,
       "tdHisInpLoc": tdHisInpLoc,
       "tdHisClk": tdHisClk,
       "tdHisCnt": tdHisCnt,
       "tdHisTable": tdHisTable,
       "tdHisEntry": tdHisEntry,
       "tdHisChassis": tdHisChassis,
       "tdHisSlot": tdHisSlot,
       "tdHisPort": tdHisPort,
       "tdHisIndex": tdHisIndex,
       "tdHisV": tdHisV,
       "ptpclient": ptpclient,
       "ptpclientTable": ptpclientTable,
       "ptpclientEntry": ptpclientEntry,
       "ptpclientChassis": ptpclientChassis,
       "ptpclientSlot": ptpclientSlot,
       "ptpclientData": ptpclientData,
       "ptpclientParmLoc": ptpclientParmLoc,
       "ptpclientCmdXeq": ptpclientCmdXeq,
       "mTrapReq": mTrapReq,
       "tprTag": tprTag,
       "mTrapObjs": mTrapObjs,
       "tpTag": tpTag,
       "tpEvt": tpEvt,
       "tpId": tpId,
       "tpMCode": tpMCode,
       "tpTimestamp": tpTimestamp,
       "tpChassis": tpChassis,
       "tpSlot": tpSlot,
       "tpPort": tpPort,
       "tpAlmCode": tpAlmCode,
       "tpNtfCode": tpNtfCode,
       "tpElevated": tpElevated,
       "tpDescr": tpDescr,
       "mTraps": mTraps,
       "ssuTraps": ssuTraps,
       "ssuEvent": ssuEvent,
       "sInterfaces": sInterfaces,
       "sifNtpNumber": sifNtpNumber,
       "sifSnmpv2Number": sifSnmpv2Number,
       "sifSnmpv3Number": sifSnmpv3Number,
       "sifClkNumber": sifClkNumber,
       "sifGpsNumber": sifGpsNumber,
       "sifInpDs1Number": sifInpDs1Number,
       "sifInpE1Number": sifInpE1Number,
       "sifInpCcNumber": sifInpCcNumber,
       "sifOutDs1Number": sifOutDs1Number,
       "sifOutE1Number": sifOutE1Number,
       "sifOut2048Number": sifOut2048Number,
       "sifOutCcNumber": sifOutCcNumber,
       "sifOutE12048Number": sifOutE12048Number,
       "sifOut422Number": sifOut422Number,
       "sifLrmDs1Number": sifLrmDs1Number,
       "sifOutJsineNumber": sifOutJsineNumber,
       "sifInpJsineNumber": sifInpJsineNumber,
       "sifOutJccNumber": sifOutJccNumber,
       "sifInpJccNumber": sifInpJccNumber,
       "sifLrmE1Number": sifLrmE1Number}
)
