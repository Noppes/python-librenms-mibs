# SNMP MIB module (OA-SFP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\adva\OA-SFP-MIB

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

(oaccess,) = mibBuilder.importSymbols(
    "OS-COMMON-TC-MIB",
    "oaccess")

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

oaSfpMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6926, 1, 18)
)
if mibBuilder.loadTexts:
    oaSfpMib.setRevisions(
        ("2005-05-26 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class SlotIndex(TextualConvention, Integer32):
    status = "current"
    displayHint = "d"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )



class PortInSlotIndex(TextualConvention, Integer32):
    status = "current"
    displayHint = "d"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )



# MIB Managed Objects in the order of their OIDs

_OaManagement_ObjectIdentity = ObjectIdentity
oaManagement = _OaManagement_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6926, 1)
)
_OaSfp_ObjectIdentity = ObjectIdentity
oaSfp = _OaSfp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6926, 1, 18, 1)
)
_OaSfpMIBObjects_ObjectIdentity = ObjectIdentity
oaSfpMIBObjects = _OaSfpMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6926, 1, 18, 1, 1)
)
_OaSfpCompatibleInterfaceCount_Type = Integer32
_OaSfpCompatibleInterfaceCount_Object = MibScalar
oaSfpCompatibleInterfaceCount = _OaSfpCompatibleInterfaceCount_Object(
    (1, 3, 6, 1, 4, 1, 6926, 1, 18, 1, 1, 1),
    _OaSfpCompatibleInterfaceCount_Type()
)
oaSfpCompatibleInterfaceCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaSfpCompatibleInterfaceCount.setStatus("current")
_OaSfpInfoTable_Object = MibTable
oaSfpInfoTable = _OaSfpInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 6926, 1, 18, 1, 1, 2)
)
if mibBuilder.loadTexts:
    oaSfpInfoTable.setStatus("current")
_OaSfpInfoEntry_Object = MibTableRow
oaSfpInfoEntry = _OaSfpInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 6926, 1, 18, 1, 1, 2, 1)
)
oaSfpInfoEntry.setIndexNames(
    (0, "OA-SFP-MIB", "oaSfpInfoSlotIndex"),
    (0, "OA-SFP-MIB", "oaSfpInfoPortIndex"),
)
if mibBuilder.loadTexts:
    oaSfpInfoEntry.setStatus("current")
_OaSfpInfoSlotIndex_Type = SlotIndex
_OaSfpInfoSlotIndex_Object = MibTableColumn
oaSfpInfoSlotIndex = _OaSfpInfoSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 6926, 1, 18, 1, 1, 2, 1, 1),
    _OaSfpInfoSlotIndex_Type()
)
oaSfpInfoSlotIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    oaSfpInfoSlotIndex.setStatus("current")
_OaSfpInfoPortIndex_Type = PortInSlotIndex
_OaSfpInfoPortIndex_Object = MibTableColumn
oaSfpInfoPortIndex = _OaSfpInfoPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 6926, 1, 18, 1, 1, 2, 1, 2),
    _OaSfpInfoPortIndex_Type()
)
oaSfpInfoPortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    oaSfpInfoPortIndex.setStatus("current")


class _OaSfpInfoIdentifier_Type(Integer32):
    """Custom type oaSfpInfoIdentifier based on Integer32"""
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
              11,
              12,
              13)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 1),
          ("other", 2),
          ("gbic", 3),
          ("fixed", 4),
          ("sfp", 5),
          ("xbi300pin", 6),
          ("xenpak", 7),
          ("xfp", 8),
          ("xff", 9),
          ("xfpE", 10),
          ("xpak", 11),
          ("x2", 12),
          ("dsfp", 13))
    )


_OaSfpInfoIdentifier_Type.__name__ = "Integer32"
_OaSfpInfoIdentifier_Object = MibTableColumn
oaSfpInfoIdentifier = _OaSfpInfoIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 6926, 1, 18, 1, 1, 2, 1, 3),
    _OaSfpInfoIdentifier_Type()
)
oaSfpInfoIdentifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaSfpInfoIdentifier.setStatus("current")


class _OaSfpInfoVendorSpecificIdentifier_Type(DisplayString):
    """Custom type oaSfpInfoVendorSpecificIdentifier based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 30),
    )


_OaSfpInfoVendorSpecificIdentifier_Type.__name__ = "DisplayString"
_OaSfpInfoVendorSpecificIdentifier_Object = MibTableColumn
oaSfpInfoVendorSpecificIdentifier = _OaSfpInfoVendorSpecificIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 6926, 1, 18, 1, 1, 2, 1, 4),
    _OaSfpInfoVendorSpecificIdentifier_Type()
)
oaSfpInfoVendorSpecificIdentifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaSfpInfoVendorSpecificIdentifier.setStatus("current")


class _OaSfpInfoConnector_Type(Integer32):
    """Custom type oaSfpInfoConnector based on Integer32"""
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
              11,
              12,
              13,
              34,
              35)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 1),
          ("other", 2),
          ("sc", 3),
          ("fcs1cc", 4),
          ("fcs2cc", 5),
          ("bnctnc", 6),
          ("fcch", 7),
          ("fiberJack", 8),
          ("lc", 9),
          ("mtrj", 10),
          ("mu", 11),
          ("sg", 12),
          ("opticalPigtail", 13),
          ("hssdcii", 34),
          ("copperPigtail", 35))
    )


_OaSfpInfoConnector_Type.__name__ = "Integer32"
_OaSfpInfoConnector_Object = MibTableColumn
oaSfpInfoConnector = _OaSfpInfoConnector_Object(
    (1, 3, 6, 1, 4, 1, 6926, 1, 18, 1, 1, 2, 1, 8),
    _OaSfpInfoConnector_Type()
)
oaSfpInfoConnector.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaSfpInfoConnector.setStatus("current")


class _OaSfpInfoVendorSpecificConnector_Type(DisplayString):
    """Custom type oaSfpInfoVendorSpecificConnector based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 30),
    )


_OaSfpInfoVendorSpecificConnector_Type.__name__ = "DisplayString"
_OaSfpInfoVendorSpecificConnector_Object = MibTableColumn
oaSfpInfoVendorSpecificConnector = _OaSfpInfoVendorSpecificConnector_Object(
    (1, 3, 6, 1, 4, 1, 6926, 1, 18, 1, 1, 2, 1, 9),
    _OaSfpInfoVendorSpecificConnector_Type()
)
oaSfpInfoVendorSpecificConnector.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaSfpInfoVendorSpecificConnector.setStatus("current")


class _OaSfpInfoVendorName_Type(DisplayString):
    """Custom type oaSfpInfoVendorName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_OaSfpInfoVendorName_Type.__name__ = "DisplayString"
_OaSfpInfoVendorName_Object = MibTableColumn
oaSfpInfoVendorName = _OaSfpInfoVendorName_Object(
    (1, 3, 6, 1, 4, 1, 6926, 1, 18, 1, 1, 2, 1, 24),
    _OaSfpInfoVendorName_Type()
)
oaSfpInfoVendorName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaSfpInfoVendorName.setStatus("current")


class _OaSfpInfoVendorOUI_Type(DisplayString):
    """Custom type oaSfpInfoVendorOUI based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 3),
    )
    fixed_length = 3


_OaSfpInfoVendorOUI_Type.__name__ = "DisplayString"
_OaSfpInfoVendorOUI_Object = MibTableColumn
oaSfpInfoVendorOUI = _OaSfpInfoVendorOUI_Object(
    (1, 3, 6, 1, 4, 1, 6926, 1, 18, 1, 1, 2, 1, 25),
    _OaSfpInfoVendorOUI_Type()
)
oaSfpInfoVendorOUI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaSfpInfoVendorOUI.setStatus("current")


class _OaSfpInfoVendorPN_Type(DisplayString):
    """Custom type oaSfpInfoVendorPN based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_OaSfpInfoVendorPN_Type.__name__ = "DisplayString"
_OaSfpInfoVendorPN_Object = MibTableColumn
oaSfpInfoVendorPN = _OaSfpInfoVendorPN_Object(
    (1, 3, 6, 1, 4, 1, 6926, 1, 18, 1, 1, 2, 1, 26),
    _OaSfpInfoVendorPN_Type()
)
oaSfpInfoVendorPN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaSfpInfoVendorPN.setStatus("current")


class _OaSfpInfoVendorRev_Type(DisplayString):
    """Custom type oaSfpInfoVendorRev based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 4),
    )


_OaSfpInfoVendorRev_Type.__name__ = "DisplayString"
_OaSfpInfoVendorRev_Object = MibTableColumn
oaSfpInfoVendorRev = _OaSfpInfoVendorRev_Object(
    (1, 3, 6, 1, 4, 1, 6926, 1, 18, 1, 1, 2, 1, 27),
    _OaSfpInfoVendorRev_Type()
)
oaSfpInfoVendorRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaSfpInfoVendorRev.setStatus("current")
_OaSfpInfoLaserWavelength_Type = Integer32
_OaSfpInfoLaserWavelength_Object = MibTableColumn
oaSfpInfoLaserWavelength = _OaSfpInfoLaserWavelength_Object(
    (1, 3, 6, 1, 4, 1, 6926, 1, 18, 1, 1, 2, 1, 28),
    _OaSfpInfoLaserWavelength_Type()
)
oaSfpInfoLaserWavelength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaSfpInfoLaserWavelength.setStatus("current")
if mibBuilder.loadTexts:
    oaSfpInfoLaserWavelength.setUnits("0.01 Nano Meter(nm)")


class _OaSfpTunability_Type(Integer32):
    """Custom type oaSfpTunability based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 1),
          ("tunable", 2),
          ("nonTunable", 3))
    )


_OaSfpTunability_Type.__name__ = "Integer32"
_OaSfpTunability_Object = MibTableColumn
oaSfpTunability = _OaSfpTunability_Object(
    (1, 3, 6, 1, 4, 1, 6926, 1, 18, 1, 1, 2, 1, 29),
    _OaSfpTunability_Type()
)
oaSfpTunability.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaSfpTunability.setStatus("current")


class _OaSfpInfoVendorSN_Type(DisplayString):
    """Custom type oaSfpInfoVendorSN based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_OaSfpInfoVendorSN_Type.__name__ = "DisplayString"
_OaSfpInfoVendorSN_Object = MibTableColumn
oaSfpInfoVendorSN = _OaSfpInfoVendorSN_Object(
    (1, 3, 6, 1, 4, 1, 6926, 1, 18, 1, 1, 2, 1, 32),
    _OaSfpInfoVendorSN_Type()
)
oaSfpInfoVendorSN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaSfpInfoVendorSN.setStatus("current")


class _OaSfpInfoVendorDate_Type(DisplayString):
    """Custom type oaSfpInfoVendorDate based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )
    fixed_length = 8


_OaSfpInfoVendorDate_Type.__name__ = "DisplayString"
_OaSfpInfoVendorDate_Object = MibTableColumn
oaSfpInfoVendorDate = _OaSfpInfoVendorDate_Object(
    (1, 3, 6, 1, 4, 1, 6926, 1, 18, 1, 1, 2, 1, 33),
    _OaSfpInfoVendorDate_Type()
)
oaSfpInfoVendorDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaSfpInfoVendorDate.setStatus("current")


class _OaSfpInfoVendorSpecificLotCode_Type(DisplayString):
    """Custom type oaSfpInfoVendorSpecificLotCode based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )
    fixed_length = 2


_OaSfpInfoVendorSpecificLotCode_Type.__name__ = "DisplayString"
_OaSfpInfoVendorSpecificLotCode_Object = MibTableColumn
oaSfpInfoVendorSpecificLotCode = _OaSfpInfoVendorSpecificLotCode_Object(
    (1, 3, 6, 1, 4, 1, 6926, 1, 18, 1, 1, 2, 1, 34),
    _OaSfpInfoVendorSpecificLotCode_Type()
)
oaSfpInfoVendorSpecificLotCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaSfpInfoVendorSpecificLotCode.setStatus("current")


class _OaSfpInfoVendorSpecificData_Type(OctetString):
    """Custom type oaSfpInfoVendorSpecificData based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_OaSfpInfoVendorSpecificData_Type.__name__ = "OctetString"
_OaSfpInfoVendorSpecificData_Object = MibTableColumn
oaSfpInfoVendorSpecificData = _OaSfpInfoVendorSpecificData_Object(
    (1, 3, 6, 1, 4, 1, 6926, 1, 18, 1, 1, 2, 1, 35),
    _OaSfpInfoVendorSpecificData_Type()
)
oaSfpInfoVendorSpecificData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaSfpInfoVendorSpecificData.setStatus("current")


class _OaSfpInfoDiagnosticPowerType_Type(Integer32):
    """Custom type oaSfpInfoDiagnosticPowerType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 1),
          ("average", 2),
          ("oma", 3))
    )


_OaSfpInfoDiagnosticPowerType_Type.__name__ = "Integer32"
_OaSfpInfoDiagnosticPowerType_Object = MibTableColumn
oaSfpInfoDiagnosticPowerType = _OaSfpInfoDiagnosticPowerType_Object(
    (1, 3, 6, 1, 4, 1, 6926, 1, 18, 1, 1, 2, 1, 36),
    _OaSfpInfoDiagnosticPowerType_Type()
)
oaSfpInfoDiagnosticPowerType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaSfpInfoDiagnosticPowerType.setStatus("current")


class _OaSfpInfoDigitalDiagnostic_Type(Integer32):
    """Custom type oaSfpInfoDigitalDiagnostic based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 1),
          ("digitalDiagnostic", 2),
          ("noDigitalDiagnostic", 3))
    )


_OaSfpInfoDigitalDiagnostic_Type.__name__ = "Integer32"
_OaSfpInfoDigitalDiagnostic_Object = MibTableColumn
oaSfpInfoDigitalDiagnostic = _OaSfpInfoDigitalDiagnostic_Object(
    (1, 3, 6, 1, 4, 1, 6926, 1, 18, 1, 1, 2, 1, 37),
    _OaSfpInfoDigitalDiagnostic_Type()
)
oaSfpInfoDigitalDiagnostic.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaSfpInfoDigitalDiagnostic.setStatus("current")


class _OaSfpInfoDiagnosticCalibration_Type(Integer32):
    """Custom type oaSfpInfoDiagnosticCalibration based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 1),
          ("externalCalibration", 2),
          ("internalCalibration", 3))
    )


_OaSfpInfoDiagnosticCalibration_Type.__name__ = "Integer32"
_OaSfpInfoDiagnosticCalibration_Object = MibTableColumn
oaSfpInfoDiagnosticCalibration = _OaSfpInfoDiagnosticCalibration_Object(
    (1, 3, 6, 1, 4, 1, 6926, 1, 18, 1, 1, 2, 1, 38),
    _OaSfpInfoDiagnosticCalibration_Type()
)
oaSfpInfoDiagnosticCalibration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaSfpInfoDiagnosticCalibration.setStatus("current")


class _OaSfpInfoInstalledStatus_Type(Integer32):
    """Custom type oaSfpInfoInstalledStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 1),
          ("notInstalled", 2),
          ("installed", 3))
    )


_OaSfpInfoInstalledStatus_Type.__name__ = "Integer32"
_OaSfpInfoInstalledStatus_Object = MibTableColumn
oaSfpInfoInstalledStatus = _OaSfpInfoInstalledStatus_Object(
    (1, 3, 6, 1, 4, 1, 6926, 1, 18, 1, 1, 2, 1, 40),
    _OaSfpInfoInstalledStatus_Type()
)
oaSfpInfoInstalledStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaSfpInfoInstalledStatus.setStatus("current")


class _OaSfpInfofaultStatus_Type(Integer32):
    """Custom type oaSfpInfofaultStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 1),
          ("faulty", 2),
          ("operational", 3))
    )


_OaSfpInfofaultStatus_Type.__name__ = "Integer32"
_OaSfpInfofaultStatus_Object = MibTableColumn
oaSfpInfofaultStatus = _OaSfpInfofaultStatus_Object(
    (1, 3, 6, 1, 4, 1, 6926, 1, 18, 1, 1, 2, 1, 41),
    _OaSfpInfofaultStatus_Type()
)
oaSfpInfofaultStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaSfpInfofaultStatus.setStatus("current")


class _OaSfpInfoEnableStatus_Type(Integer32):
    """Custom type oaSfpInfoEnableStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 1),
          ("enabled", 2),
          ("disabled", 3))
    )


_OaSfpInfoEnableStatus_Type.__name__ = "Integer32"
_OaSfpInfoEnableStatus_Object = MibTableColumn
oaSfpInfoEnableStatus = _OaSfpInfoEnableStatus_Object(
    (1, 3, 6, 1, 4, 1, 6926, 1, 18, 1, 1, 2, 1, 42),
    _OaSfpInfoEnableStatus_Type()
)
oaSfpInfoEnableStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaSfpInfoEnableStatus.setStatus("current")


class _OaSfpInfoUnitName_Type(DisplayString):
    """Custom type oaSfpInfoUnitName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 29),
    )


_OaSfpInfoUnitName_Type.__name__ = "DisplayString"
_OaSfpInfoUnitName_Object = MibTableColumn
oaSfpInfoUnitName = _OaSfpInfoUnitName_Object(
    (1, 3, 6, 1, 4, 1, 6926, 1, 18, 1, 1, 2, 1, 43),
    _OaSfpInfoUnitName_Type()
)
oaSfpInfoUnitName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaSfpInfoUnitName.setStatus("current")


class _OaSfpInfoFiberType_Type(DisplayString):
    """Custom type oaSfpInfoFiberType based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 9),
    )


_OaSfpInfoFiberType_Type.__name__ = "DisplayString"
_OaSfpInfoFiberType_Object = MibTableColumn
oaSfpInfoFiberType = _OaSfpInfoFiberType_Object(
    (1, 3, 6, 1, 4, 1, 6926, 1, 18, 1, 1, 2, 1, 44),
    _OaSfpInfoFiberType_Type()
)
oaSfpInfoFiberType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaSfpInfoFiberType.setStatus("current")


class _OaSfpInfoReach_Type(DisplayString):
    """Custom type oaSfpInfoReach based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_OaSfpInfoReach_Type.__name__ = "DisplayString"
_OaSfpInfoReach_Object = MibTableColumn
oaSfpInfoReach = _OaSfpInfoReach_Object(
    (1, 3, 6, 1, 4, 1, 6926, 1, 18, 1, 1, 2, 1, 45),
    _OaSfpInfoReach_Type()
)
oaSfpInfoReach.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaSfpInfoReach.setStatus("current")


class _OaSfpInfoConnectorType_Type(DisplayString):
    """Custom type oaSfpInfoConnectorType based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 4),
    )


_OaSfpInfoConnectorType_Type.__name__ = "DisplayString"
_OaSfpInfoConnectorType_Object = MibTableColumn
oaSfpInfoConnectorType = _OaSfpInfoConnectorType_Object(
    (1, 3, 6, 1, 4, 1, 6926, 1, 18, 1, 1, 2, 1, 46),
    _OaSfpInfoConnectorType_Type()
)
oaSfpInfoConnectorType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaSfpInfoConnectorType.setStatus("current")


class _OaSfpInfoItemNum_Type(DisplayString):
    """Custom type oaSfpInfoItemNum based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_OaSfpInfoItemNum_Type.__name__ = "DisplayString"
_OaSfpInfoItemNum_Object = MibTableColumn
oaSfpInfoItemNum = _OaSfpInfoItemNum_Object(
    (1, 3, 6, 1, 4, 1, 6926, 1, 18, 1, 1, 2, 1, 47),
    _OaSfpInfoItemNum_Type()
)
oaSfpInfoItemNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaSfpInfoItemNum.setStatus("current")


class _OaSfpInfoHWRev_Type(DisplayString):
    """Custom type oaSfpInfoHWRev based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_OaSfpInfoHWRev_Type.__name__ = "DisplayString"
_OaSfpInfoHWRev_Object = MibTableColumn
oaSfpInfoHWRev = _OaSfpInfoHWRev_Object(
    (1, 3, 6, 1, 4, 1, 6926, 1, 18, 1, 1, 2, 1, 48),
    _OaSfpInfoHWRev_Type()
)
oaSfpInfoHWRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaSfpInfoHWRev.setStatus("current")


class _OaSfpInfoCleiCode_Type(DisplayString):
    """Custom type oaSfpInfoCleiCode based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 12),
    )


_OaSfpInfoCleiCode_Type.__name__ = "DisplayString"
_OaSfpInfoCleiCode_Object = MibTableColumn
oaSfpInfoCleiCode = _OaSfpInfoCleiCode_Object(
    (1, 3, 6, 1, 4, 1, 6926, 1, 18, 1, 1, 2, 1, 49),
    _OaSfpInfoCleiCode_Type()
)
oaSfpInfoCleiCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaSfpInfoCleiCode.setStatus("current")


class _OaSfpInfoPageA2hSN_Type(DisplayString):
    """Custom type oaSfpInfoPageA2hSN based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 26),
    )


_OaSfpInfoPageA2hSN_Type.__name__ = "DisplayString"
_OaSfpInfoPageA2hSN_Object = MibTableColumn
oaSfpInfoPageA2hSN = _OaSfpInfoPageA2hSN_Object(
    (1, 3, 6, 1, 4, 1, 6926, 1, 18, 1, 1, 2, 1, 50),
    _OaSfpInfoPageA2hSN_Type()
)
oaSfpInfoPageA2hSN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaSfpInfoPageA2hSN.setStatus("current")


class _OaSfpInfoManufactureDate_Type(DisplayString):
    """Custom type oaSfpInfoManufactureDate based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 12),
    )


_OaSfpInfoManufactureDate_Type.__name__ = "DisplayString"
_OaSfpInfoManufactureDate_Object = MibTableColumn
oaSfpInfoManufactureDate = _OaSfpInfoManufactureDate_Object(
    (1, 3, 6, 1, 4, 1, 6926, 1, 18, 1, 1, 2, 1, 51),
    _OaSfpInfoManufactureDate_Type()
)
oaSfpInfoManufactureDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaSfpInfoManufactureDate.setStatus("current")


class _OaSfpInfoManufactureID_Type(DisplayString):
    """Custom type oaSfpInfoManufactureID based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 119),
    )


_OaSfpInfoManufactureID_Type.__name__ = "DisplayString"
_OaSfpInfoManufactureID_Object = MibTableColumn
oaSfpInfoManufactureID = _OaSfpInfoManufactureID_Object(
    (1, 3, 6, 1, 4, 1, 6926, 1, 18, 1, 1, 2, 1, 52),
    _OaSfpInfoManufactureID_Type()
)
oaSfpInfoManufactureID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaSfpInfoManufactureID.setStatus("current")
_OaSfpDiagnosticTable_Object = MibTable
oaSfpDiagnosticTable = _OaSfpDiagnosticTable_Object(
    (1, 3, 6, 1, 4, 1, 6926, 1, 18, 1, 1, 3)
)
if mibBuilder.loadTexts:
    oaSfpDiagnosticTable.setStatus("current")
_OaSfpDiagnosticEntry_Object = MibTableRow
oaSfpDiagnosticEntry = _OaSfpDiagnosticEntry_Object(
    (1, 3, 6, 1, 4, 1, 6926, 1, 18, 1, 1, 3, 1)
)
oaSfpDiagnosticEntry.setIndexNames(
    (0, "OA-SFP-MIB", "oaSfpDiagnosticSlotIndex"),
    (0, "OA-SFP-MIB", "oaSfpDiagnosticPortIndex"),
)
if mibBuilder.loadTexts:
    oaSfpDiagnosticEntry.setStatus("current")
_OaSfpDiagnosticSlotIndex_Type = SlotIndex
_OaSfpDiagnosticSlotIndex_Object = MibTableColumn
oaSfpDiagnosticSlotIndex = _OaSfpDiagnosticSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 6926, 1, 18, 1, 1, 3, 1, 1),
    _OaSfpDiagnosticSlotIndex_Type()
)
oaSfpDiagnosticSlotIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    oaSfpDiagnosticSlotIndex.setStatus("current")
_OaSfpDiagnosticPortIndex_Type = PortInSlotIndex
_OaSfpDiagnosticPortIndex_Object = MibTableColumn
oaSfpDiagnosticPortIndex = _OaSfpDiagnosticPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 6926, 1, 18, 1, 1, 3, 1, 2),
    _OaSfpDiagnosticPortIndex_Type()
)
oaSfpDiagnosticPortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    oaSfpDiagnosticPortIndex.setStatus("current")
_OaSfpDiagnosticTemperature_Type = Integer32
_OaSfpDiagnosticTemperature_Object = MibTableColumn
oaSfpDiagnosticTemperature = _OaSfpDiagnosticTemperature_Object(
    (1, 3, 6, 1, 4, 1, 6926, 1, 18, 1, 1, 3, 1, 3),
    _OaSfpDiagnosticTemperature_Type()
)
oaSfpDiagnosticTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaSfpDiagnosticTemperature.setStatus("current")
if mibBuilder.loadTexts:
    oaSfpDiagnosticTemperature.setUnits("1/10 degrees Celsius (C)")
_OaSfpDiagnosticVcc_Type = Integer32
_OaSfpDiagnosticVcc_Object = MibTableColumn
oaSfpDiagnosticVcc = _OaSfpDiagnosticVcc_Object(
    (1, 3, 6, 1, 4, 1, 6926, 1, 18, 1, 1, 3, 1, 4),
    _OaSfpDiagnosticVcc_Type()
)
oaSfpDiagnosticVcc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaSfpDiagnosticVcc.setStatus("current")
if mibBuilder.loadTexts:
    oaSfpDiagnosticVcc.setUnits("100 micro Volts (V)")
_OaSfpDiagnosticTxBias_Type = Integer32
_OaSfpDiagnosticTxBias_Object = MibTableColumn
oaSfpDiagnosticTxBias = _OaSfpDiagnosticTxBias_Object(
    (1, 3, 6, 1, 4, 1, 6926, 1, 18, 1, 1, 3, 1, 5),
    _OaSfpDiagnosticTxBias_Type()
)
oaSfpDiagnosticTxBias.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaSfpDiagnosticTxBias.setStatus("current")
if mibBuilder.loadTexts:
    oaSfpDiagnosticTxBias.setUnits("1 micro Amperes (A)")
_OaSfpDiagnosticTxPower_Type = Integer32
_OaSfpDiagnosticTxPower_Object = MibTableColumn
oaSfpDiagnosticTxPower = _OaSfpDiagnosticTxPower_Object(
    (1, 3, 6, 1, 4, 1, 6926, 1, 18, 1, 1, 3, 1, 6),
    _OaSfpDiagnosticTxPower_Type()
)
oaSfpDiagnosticTxPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaSfpDiagnosticTxPower.setStatus("current")
if mibBuilder.loadTexts:
    oaSfpDiagnosticTxPower.setUnits("0.01 decibel (dBm)")
_OaSfpDiagnosticRxPower_Type = Integer32
_OaSfpDiagnosticRxPower_Object = MibTableColumn
oaSfpDiagnosticRxPower = _OaSfpDiagnosticRxPower_Object(
    (1, 3, 6, 1, 4, 1, 6926, 1, 18, 1, 1, 3, 1, 7),
    _OaSfpDiagnosticRxPower_Type()
)
oaSfpDiagnosticRxPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaSfpDiagnosticRxPower.setStatus("current")
if mibBuilder.loadTexts:
    oaSfpDiagnosticRxPower.setUnits("0.01 decibel (dBm)")
_OaSfpRatesSupportedTable_Object = MibTable
oaSfpRatesSupportedTable = _OaSfpRatesSupportedTable_Object(
    (1, 3, 6, 1, 4, 1, 6926, 1, 18, 1, 1, 4)
)
if mibBuilder.loadTexts:
    oaSfpRatesSupportedTable.setStatus("current")
_OaSfpRatesSupportedEntry_Object = MibTableRow
oaSfpRatesSupportedEntry = _OaSfpRatesSupportedEntry_Object(
    (1, 3, 6, 1, 4, 1, 6926, 1, 18, 1, 1, 4, 1)
)
oaSfpRatesSupportedEntry.setIndexNames(
    (0, "OA-SFP-MIB", "oaSfpInfoSlotIndex"),
    (0, "OA-SFP-MIB", "oaSfpInfoPortIndex"),
    (0, "OA-SFP-MIB", "oaSfpRatesSupportedIndex"),
)
if mibBuilder.loadTexts:
    oaSfpRatesSupportedEntry.setStatus("current")
_OaSfpRatesSupportedIndex_Type = Unsigned32
_OaSfpRatesSupportedIndex_Object = MibTableColumn
oaSfpRatesSupportedIndex = _OaSfpRatesSupportedIndex_Object(
    (1, 3, 6, 1, 4, 1, 6926, 1, 18, 1, 1, 4, 1, 3),
    _OaSfpRatesSupportedIndex_Type()
)
oaSfpRatesSupportedIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    oaSfpRatesSupportedIndex.setStatus("current")
_OaSfpRatesSupportedValue_Type = Unsigned32
_OaSfpRatesSupportedValue_Object = MibTableColumn
oaSfpRatesSupportedValue = _OaSfpRatesSupportedValue_Object(
    (1, 3, 6, 1, 4, 1, 6926, 1, 18, 1, 1, 4, 1, 4),
    _OaSfpRatesSupportedValue_Type()
)
oaSfpRatesSupportedValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaSfpRatesSupportedValue.setStatus("current")
if mibBuilder.loadTexts:
    oaSfpRatesSupportedValue.setUnits("Mbps")
_OaXfpMIBObjects_ObjectIdentity = ObjectIdentity
oaXfpMIBObjects = _OaXfpMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6926, 1, 18, 1, 2)
)
_OaXfpCompatibleInterfaceCount_Type = Integer32
_OaXfpCompatibleInterfaceCount_Object = MibScalar
oaXfpCompatibleInterfaceCount = _OaXfpCompatibleInterfaceCount_Object(
    (1, 3, 6, 1, 4, 1, 6926, 1, 18, 1, 2, 1),
    _OaXfpCompatibleInterfaceCount_Type()
)
oaXfpCompatibleInterfaceCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaXfpCompatibleInterfaceCount.setStatus("current")
_OaXfpInfoTable_Object = MibTable
oaXfpInfoTable = _OaXfpInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 6926, 1, 18, 1, 2, 2)
)
if mibBuilder.loadTexts:
    oaXfpInfoTable.setStatus("current")
_OaXfpInfoEntry_Object = MibTableRow
oaXfpInfoEntry = _OaXfpInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 6926, 1, 18, 1, 2, 2, 1)
)
oaXfpInfoEntry.setIndexNames(
    (0, "OA-SFP-MIB", "oaXfpInfoSlotIndex"),
    (0, "OA-SFP-MIB", "oaXfpInfoPortIndex"),
)
if mibBuilder.loadTexts:
    oaXfpInfoEntry.setStatus("current")
_OaXfpInfoSlotIndex_Type = SlotIndex
_OaXfpInfoSlotIndex_Object = MibTableColumn
oaXfpInfoSlotIndex = _OaXfpInfoSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 6926, 1, 18, 1, 2, 2, 1, 1),
    _OaXfpInfoSlotIndex_Type()
)
oaXfpInfoSlotIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    oaXfpInfoSlotIndex.setStatus("current")
_OaXfpInfoPortIndex_Type = PortInSlotIndex
_OaXfpInfoPortIndex_Object = MibTableColumn
oaXfpInfoPortIndex = _OaXfpInfoPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 6926, 1, 18, 1, 2, 2, 1, 2),
    _OaXfpInfoPortIndex_Type()
)
oaXfpInfoPortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    oaXfpInfoPortIndex.setStatus("current")
_OaXfpInfoLaserWavelengthTolerance_Type = Integer32
_OaXfpInfoLaserWavelengthTolerance_Object = MibTableColumn
oaXfpInfoLaserWavelengthTolerance = _OaXfpInfoLaserWavelengthTolerance_Object(
    (1, 3, 6, 1, 4, 1, 6926, 1, 18, 1, 2, 2, 1, 28),
    _OaXfpInfoLaserWavelengthTolerance_Type()
)
oaXfpInfoLaserWavelengthTolerance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaXfpInfoLaserWavelengthTolerance.setStatus("current")
if mibBuilder.loadTexts:
    oaXfpInfoLaserWavelengthTolerance.setUnits("0.001 Nano Meter(nm)")
_OaXfpTunTable_Object = MibTable
oaXfpTunTable = _OaXfpTunTable_Object(
    (1, 3, 6, 1, 4, 1, 6926, 1, 18, 1, 2, 3)
)
if mibBuilder.loadTexts:
    oaXfpTunTable.setStatus("current")
_OaXfpTunEntry_Object = MibTableRow
oaXfpTunEntry = _OaXfpTunEntry_Object(
    (1, 3, 6, 1, 4, 1, 6926, 1, 18, 1, 2, 3, 1)
)
oaXfpTunEntry.setIndexNames(
    (0, "OA-SFP-MIB", "oaXfpTunSlotIndex"),
    (0, "OA-SFP-MIB", "oaXfpTunPortIndex"),
)
if mibBuilder.loadTexts:
    oaXfpTunEntry.setStatus("current")


class _OaXfpTunSlotIndex_Type(Integer32):
    """Custom type oaXfpTunSlotIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_OaXfpTunSlotIndex_Type.__name__ = "Integer32"
_OaXfpTunSlotIndex_Object = MibTableColumn
oaXfpTunSlotIndex = _OaXfpTunSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 6926, 1, 18, 1, 2, 3, 1, 1),
    _OaXfpTunSlotIndex_Type()
)
oaXfpTunSlotIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    oaXfpTunSlotIndex.setStatus("current")


class _OaXfpTunPortIndex_Type(Integer32):
    """Custom type oaXfpTunPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_OaXfpTunPortIndex_Type.__name__ = "Integer32"
_OaXfpTunPortIndex_Object = MibTableColumn
oaXfpTunPortIndex = _OaXfpTunPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 6926, 1, 18, 1, 2, 3, 1, 2),
    _OaXfpTunPortIndex_Type()
)
oaXfpTunPortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    oaXfpTunPortIndex.setStatus("current")
_OaXfpTunLaserFirstFrequency_Type = Integer32
_OaXfpTunLaserFirstFrequency_Object = MibTableColumn
oaXfpTunLaserFirstFrequency = _OaXfpTunLaserFirstFrequency_Object(
    (1, 3, 6, 1, 4, 1, 6926, 1, 18, 1, 2, 3, 1, 3),
    _OaXfpTunLaserFirstFrequency_Type()
)
oaXfpTunLaserFirstFrequency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaXfpTunLaserFirstFrequency.setStatus("current")
if mibBuilder.loadTexts:
    oaXfpTunLaserFirstFrequency.setUnits("0.001 Terahertz(THz)")
_OaXfpTunLaserLastFrequency_Type = Integer32
_OaXfpTunLaserLastFrequency_Object = MibTableColumn
oaXfpTunLaserLastFrequency = _OaXfpTunLaserLastFrequency_Object(
    (1, 3, 6, 1, 4, 1, 6926, 1, 18, 1, 2, 3, 1, 4),
    _OaXfpTunLaserLastFrequency_Type()
)
oaXfpTunLaserLastFrequency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaXfpTunLaserLastFrequency.setStatus("current")
if mibBuilder.loadTexts:
    oaXfpTunLaserLastFrequency.setUnits("0.001 Terahertz(THz)")


class _OaXfpTunGridSpacing_Type(Integer32):
    """Custom type oaXfpTunGridSpacing based on Integer32"""
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
        *(("unknown", 1),
          ("g200", 2),
          ("g100", 3),
          ("g50", 4),
          ("g25", 5))
    )


_OaXfpTunGridSpacing_Type.__name__ = "Integer32"
_OaXfpTunGridSpacing_Object = MibTableColumn
oaXfpTunGridSpacing = _OaXfpTunGridSpacing_Object(
    (1, 3, 6, 1, 4, 1, 6926, 1, 18, 1, 2, 3, 1, 5),
    _OaXfpTunGridSpacing_Type()
)
oaXfpTunGridSpacing.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaXfpTunGridSpacing.setStatus("current")


class _OaXfpTunLaserItuBand_Type(Integer32):
    """Custom type oaXfpTunLaserItuBand based on Integer32"""
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
        *(("unknown", 1),
          ("cBand", 2),
          ("lBand", 3),
          ("sBand", 4))
    )


_OaXfpTunLaserItuBand_Type.__name__ = "Integer32"
_OaXfpTunLaserItuBand_Object = MibTableColumn
oaXfpTunLaserItuBand = _OaXfpTunLaserItuBand_Object(
    (1, 3, 6, 1, 4, 1, 6926, 1, 18, 1, 2, 3, 1, 6),
    _OaXfpTunLaserItuBand_Type()
)
oaXfpTunLaserItuBand.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaXfpTunLaserItuBand.setStatus("current")
_OaXfpTunLaserItuCh_Type = Integer32
_OaXfpTunLaserItuCh_Object = MibTableColumn
oaXfpTunLaserItuCh = _OaXfpTunLaserItuCh_Object(
    (1, 3, 6, 1, 4, 1, 6926, 1, 18, 1, 2, 3, 1, 7),
    _OaXfpTunLaserItuCh_Type()
)
oaXfpTunLaserItuCh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oaXfpTunLaserItuCh.setStatus("current")
_OaDsfpMIBObjects_ObjectIdentity = ObjectIdentity
oaDsfpMIBObjects = _OaDsfpMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6926, 1, 18, 1, 3)
)
_OaDsfpCompatibleInterfaceCount_Type = Integer32
_OaDsfpCompatibleInterfaceCount_Object = MibScalar
oaDsfpCompatibleInterfaceCount = _OaDsfpCompatibleInterfaceCount_Object(
    (1, 3, 6, 1, 4, 1, 6926, 1, 18, 1, 3, 1),
    _OaDsfpCompatibleInterfaceCount_Type()
)
oaDsfpCompatibleInterfaceCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaDsfpCompatibleInterfaceCount.setStatus("current")
_OaDsfpInfoTable_Object = MibTable
oaDsfpInfoTable = _OaDsfpInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 6926, 1, 18, 1, 3, 2)
)
if mibBuilder.loadTexts:
    oaDsfpInfoTable.setStatus("current")
_OaDsfpInfoEntry_Object = MibTableRow
oaDsfpInfoEntry = _OaDsfpInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 6926, 1, 18, 1, 3, 2, 1)
)
oaDsfpInfoEntry.setIndexNames(
    (0, "OA-SFP-MIB", "oaDsfpInfoSlotIndex"),
    (0, "OA-SFP-MIB", "oaDsfpInfoPortIndex"),
)
if mibBuilder.loadTexts:
    oaDsfpInfoEntry.setStatus("current")
_OaDsfpInfoSlotIndex_Type = SlotIndex
_OaDsfpInfoSlotIndex_Object = MibTableColumn
oaDsfpInfoSlotIndex = _OaDsfpInfoSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 6926, 1, 18, 1, 3, 2, 1, 1),
    _OaDsfpInfoSlotIndex_Type()
)
oaDsfpInfoSlotIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    oaDsfpInfoSlotIndex.setStatus("current")
_OaDsfpInfoPortIndex_Type = PortInSlotIndex
_OaDsfpInfoPortIndex_Object = MibTableColumn
oaDsfpInfoPortIndex = _OaDsfpInfoPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 6926, 1, 18, 1, 3, 2, 1, 2),
    _OaDsfpInfoPortIndex_Type()
)
oaDsfpInfoPortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    oaDsfpInfoPortIndex.setStatus("current")


class _OaDsfpInfoChannelSpacing_Type(Integer32):
    """Custom type oaDsfpInfoChannelSpacing based on Integer32"""
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
        *(("unknown", 1),
          ("g200", 2),
          ("g100", 3),
          ("g50", 4))
    )


_OaDsfpInfoChannelSpacing_Type.__name__ = "Integer32"
_OaDsfpInfoChannelSpacing_Object = MibTableColumn
oaDsfpInfoChannelSpacing = _OaDsfpInfoChannelSpacing_Object(
    (1, 3, 6, 1, 4, 1, 6926, 1, 18, 1, 3, 2, 1, 4),
    _OaDsfpInfoChannelSpacing_Type()
)
oaDsfpInfoChannelSpacing.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaDsfpInfoChannelSpacing.setStatus("current")
_OaDsfpInfoChannelTuning_Type = Integer32
_OaDsfpInfoChannelTuning_Object = MibTableColumn
oaDsfpInfoChannelTuning = _OaDsfpInfoChannelTuning_Object(
    (1, 3, 6, 1, 4, 1, 6926, 1, 18, 1, 3, 2, 1, 5),
    _OaDsfpInfoChannelTuning_Type()
)
oaDsfpInfoChannelTuning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaDsfpInfoChannelTuning.setStatus("current")
_OaMsa300PinMIBObjects_ObjectIdentity = ObjectIdentity
oaMsa300PinMIBObjects = _OaMsa300PinMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6926, 1, 18, 1, 4)
)
_OaMsa300PinCompatibleIfCount_Type = Integer32
_OaMsa300PinCompatibleIfCount_Object = MibScalar
oaMsa300PinCompatibleIfCount = _OaMsa300PinCompatibleIfCount_Object(
    (1, 3, 6, 1, 4, 1, 6926, 1, 18, 1, 4, 1),
    _OaMsa300PinCompatibleIfCount_Type()
)
oaMsa300PinCompatibleIfCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaMsa300PinCompatibleIfCount.setStatus("current")
_OaMsa300PinIdTable_Object = MibTable
oaMsa300PinIdTable = _OaMsa300PinIdTable_Object(
    (1, 3, 6, 1, 4, 1, 6926, 1, 18, 1, 4, 2)
)
if mibBuilder.loadTexts:
    oaMsa300PinIdTable.setStatus("current")
_OaMsa300PinIdEntry_Object = MibTableRow
oaMsa300PinIdEntry = _OaMsa300PinIdEntry_Object(
    (1, 3, 6, 1, 4, 1, 6926, 1, 18, 1, 4, 2, 1)
)
oaMsa300PinIdEntry.setIndexNames(
    (0, "OA-SFP-MIB", "oaMsa300PinIdSlotIndex"),
    (0, "OA-SFP-MIB", "oaMsa300PinIdPortIndex"),
)
if mibBuilder.loadTexts:
    oaMsa300PinIdEntry.setStatus("current")
_OaMsa300PinIdSlotIndex_Type = SlotIndex
_OaMsa300PinIdSlotIndex_Object = MibTableColumn
oaMsa300PinIdSlotIndex = _OaMsa300PinIdSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 6926, 1, 18, 1, 4, 2, 1, 1),
    _OaMsa300PinIdSlotIndex_Type()
)
oaMsa300PinIdSlotIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    oaMsa300PinIdSlotIndex.setStatus("current")
_OaMsa300PinIdPortIndex_Type = PortInSlotIndex
_OaMsa300PinIdPortIndex_Object = MibTableColumn
oaMsa300PinIdPortIndex = _OaMsa300PinIdPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 6926, 1, 18, 1, 4, 2, 1, 2),
    _OaMsa300PinIdPortIndex_Type()
)
oaMsa300PinIdPortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    oaMsa300PinIdPortIndex.setStatus("current")


class _OaMsa300PinIdModuleTypeCode_Type(Integer32):
    """Custom type oaMsa300PinIdModuleTypeCode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              6,
              8)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 1),
          ("msa10Gb", 6),
          ("msa10GbWdm", 8))
    )


_OaMsa300PinIdModuleTypeCode_Type.__name__ = "Integer32"
_OaMsa300PinIdModuleTypeCode_Object = MibTableColumn
oaMsa300PinIdModuleTypeCode = _OaMsa300PinIdModuleTypeCode_Object(
    (1, 3, 6, 1, 4, 1, 6926, 1, 18, 1, 4, 2, 1, 4),
    _OaMsa300PinIdModuleTypeCode_Type()
)
oaMsa300PinIdModuleTypeCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaMsa300PinIdModuleTypeCode.setStatus("current")


class _OaMsa300PinIdFirstLaserItuBand_Type(Integer32):
    """Custom type oaMsa300PinIdFirstLaserItuBand based on Integer32"""
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
        *(("unknown", 1),
          ("cBand", 2),
          ("lBand", 3),
          ("sBand", 4))
    )


_OaMsa300PinIdFirstLaserItuBand_Type.__name__ = "Integer32"
_OaMsa300PinIdFirstLaserItuBand_Object = MibTableColumn
oaMsa300PinIdFirstLaserItuBand = _OaMsa300PinIdFirstLaserItuBand_Object(
    (1, 3, 6, 1, 4, 1, 6926, 1, 18, 1, 4, 2, 1, 6),
    _OaMsa300PinIdFirstLaserItuBand_Type()
)
oaMsa300PinIdFirstLaserItuBand.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaMsa300PinIdFirstLaserItuBand.setStatus("current")
_OaMsa300PinIdFirstLaserItuCh_Type = Integer32
_OaMsa300PinIdFirstLaserItuCh_Object = MibTableColumn
oaMsa300PinIdFirstLaserItuCh = _OaMsa300PinIdFirstLaserItuCh_Object(
    (1, 3, 6, 1, 4, 1, 6926, 1, 18, 1, 4, 2, 1, 7),
    _OaMsa300PinIdFirstLaserItuCh_Type()
)
oaMsa300PinIdFirstLaserItuCh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaMsa300PinIdFirstLaserItuCh.setStatus("current")
if mibBuilder.loadTexts:
    oaMsa300PinIdFirstLaserItuCh.setUnits("0.01 Nano Meter(nm)")


class _OaMsa300PinIdLastLaserItuBand_Type(Integer32):
    """Custom type oaMsa300PinIdLastLaserItuBand based on Integer32"""
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
        *(("unknown", 1),
          ("cBand", 2),
          ("lBand", 3),
          ("sBand", 4))
    )


_OaMsa300PinIdLastLaserItuBand_Type.__name__ = "Integer32"
_OaMsa300PinIdLastLaserItuBand_Object = MibTableColumn
oaMsa300PinIdLastLaserItuBand = _OaMsa300PinIdLastLaserItuBand_Object(
    (1, 3, 6, 1, 4, 1, 6926, 1, 18, 1, 4, 2, 1, 8),
    _OaMsa300PinIdLastLaserItuBand_Type()
)
oaMsa300PinIdLastLaserItuBand.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaMsa300PinIdLastLaserItuBand.setStatus("current")
_OaMsa300PinIdLastLaserItuCh_Type = Integer32
_OaMsa300PinIdLastLaserItuCh_Object = MibTableColumn
oaMsa300PinIdLastLaserItuCh = _OaMsa300PinIdLastLaserItuCh_Object(
    (1, 3, 6, 1, 4, 1, 6926, 1, 18, 1, 4, 2, 1, 9),
    _OaMsa300PinIdLastLaserItuCh_Type()
)
oaMsa300PinIdLastLaserItuCh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaMsa300PinIdLastLaserItuCh.setStatus("current")
if mibBuilder.loadTexts:
    oaMsa300PinIdLastLaserItuCh.setUnits("0.01 Nano Meter(nm)")


class _OaMsa300PinIdLaserItuChSpacing_Type(Integer32):
    """Custom type oaMsa300PinIdLaserItuChSpacing based on Integer32"""
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
        *(("unknown", 1),
          ("g200", 2),
          ("g100", 3),
          ("g50", 4),
          ("g25", 5))
    )


_OaMsa300PinIdLaserItuChSpacing_Type.__name__ = "Integer32"
_OaMsa300PinIdLaserItuChSpacing_Object = MibTableColumn
oaMsa300PinIdLaserItuChSpacing = _OaMsa300PinIdLaserItuChSpacing_Object(
    (1, 3, 6, 1, 4, 1, 6926, 1, 18, 1, 4, 2, 1, 10),
    _OaMsa300PinIdLaserItuChSpacing_Type()
)
oaMsa300PinIdLaserItuChSpacing.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaMsa300PinIdLaserItuChSpacing.setStatus("current")
_OaMsa300PinMeasTable_Object = MibTable
oaMsa300PinMeasTable = _OaMsa300PinMeasTable_Object(
    (1, 3, 6, 1, 4, 1, 6926, 1, 18, 1, 4, 3)
)
if mibBuilder.loadTexts:
    oaMsa300PinMeasTable.setStatus("current")
_OaMsa300PinMeasEntry_Object = MibTableRow
oaMsa300PinMeasEntry = _OaMsa300PinMeasEntry_Object(
    (1, 3, 6, 1, 4, 1, 6926, 1, 18, 1, 4, 3, 1)
)
oaMsa300PinMeasEntry.setIndexNames(
    (0, "OA-SFP-MIB", "oaMsa300PinMeasSlotIndex"),
    (0, "OA-SFP-MIB", "oaMsa300PinMeasPortIndex"),
)
if mibBuilder.loadTexts:
    oaMsa300PinMeasEntry.setStatus("current")
_OaMsa300PinMeasSlotIndex_Type = SlotIndex
_OaMsa300PinMeasSlotIndex_Object = MibTableColumn
oaMsa300PinMeasSlotIndex = _OaMsa300PinMeasSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 6926, 1, 18, 1, 4, 3, 1, 1),
    _OaMsa300PinMeasSlotIndex_Type()
)
oaMsa300PinMeasSlotIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    oaMsa300PinMeasSlotIndex.setStatus("current")
_OaMsa300PinMeasPortIndex_Type = PortInSlotIndex
_OaMsa300PinMeasPortIndex_Object = MibTableColumn
oaMsa300PinMeasPortIndex = _OaMsa300PinMeasPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 6926, 1, 18, 1, 4, 3, 1, 2),
    _OaMsa300PinMeasPortIndex_Type()
)
oaMsa300PinMeasPortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    oaMsa300PinMeasPortIndex.setStatus("current")
_OaMsa300PinMeasLaserOutputPwrMon_Type = Integer32
_OaMsa300PinMeasLaserOutputPwrMon_Object = MibTableColumn
oaMsa300PinMeasLaserOutputPwrMon = _OaMsa300PinMeasLaserOutputPwrMon_Object(
    (1, 3, 6, 1, 4, 1, 6926, 1, 18, 1, 4, 3, 1, 4),
    _OaMsa300PinMeasLaserOutputPwrMon_Type()
)
oaMsa300PinMeasLaserOutputPwrMon.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaMsa300PinMeasLaserOutputPwrMon.setStatus("current")
if mibBuilder.loadTexts:
    oaMsa300PinMeasLaserOutputPwrMon.setUnits("Micro Watt(uW)")
_OaMsa300PinMeasLaserTempMon_Type = Integer32
_OaMsa300PinMeasLaserTempMon_Object = MibTableColumn
oaMsa300PinMeasLaserTempMon = _OaMsa300PinMeasLaserTempMon_Object(
    (1, 3, 6, 1, 4, 1, 6926, 1, 18, 1, 4, 3, 1, 5),
    _OaMsa300PinMeasLaserTempMon_Type()
)
oaMsa300PinMeasLaserTempMon.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaMsa300PinMeasLaserTempMon.setStatus("current")
if mibBuilder.loadTexts:
    oaMsa300PinMeasLaserTempMon.setUnits("0.001 degrees Celsius (C)")
_OaMsa300PinMeasRecSigAvrOptPower_Type = Integer32
_OaMsa300PinMeasRecSigAvrOptPower_Object = MibTableColumn
oaMsa300PinMeasRecSigAvrOptPower = _OaMsa300PinMeasRecSigAvrOptPower_Object(
    (1, 3, 6, 1, 4, 1, 6926, 1, 18, 1, 4, 3, 1, 7),
    _OaMsa300PinMeasRecSigAvrOptPower_Type()
)
oaMsa300PinMeasRecSigAvrOptPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaMsa300PinMeasRecSigAvrOptPower.setStatus("current")
if mibBuilder.loadTexts:
    oaMsa300PinMeasRecSigAvrOptPower.setUnits("Nano Watt (nW)")
_OaMsa300PinMeasLaserWlengthMon_Type = Integer32
_OaMsa300PinMeasLaserWlengthMon_Object = MibTableColumn
oaMsa300PinMeasLaserWlengthMon = _OaMsa300PinMeasLaserWlengthMon_Object(
    (1, 3, 6, 1, 4, 1, 6926, 1, 18, 1, 4, 3, 1, 8),
    _OaMsa300PinMeasLaserWlengthMon_Type()
)
oaMsa300PinMeasLaserWlengthMon.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaMsa300PinMeasLaserWlengthMon.setStatus("current")
if mibBuilder.loadTexts:
    oaMsa300PinMeasLaserWlengthMon.setUnits("Mega Hertz (MHz)")
_OaMsa300PinMeasTransTempMon_Type = Integer32
_OaMsa300PinMeasTransTempMon_Object = MibTableColumn
oaMsa300PinMeasTransTempMon = _OaMsa300PinMeasTransTempMon_Object(
    (1, 3, 6, 1, 4, 1, 6926, 1, 18, 1, 4, 3, 1, 9),
    _OaMsa300PinMeasTransTempMon_Type()
)
oaMsa300PinMeasTransTempMon.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaMsa300PinMeasTransTempMon.setStatus("current")
if mibBuilder.loadTexts:
    oaMsa300PinMeasTransTempMon.setUnits("0.001 degrees Celsius (C)")
_OaMsa300PinAlarmTable_Object = MibTable
oaMsa300PinAlarmTable = _OaMsa300PinAlarmTable_Object(
    (1, 3, 6, 1, 4, 1, 6926, 1, 18, 1, 4, 4)
)
if mibBuilder.loadTexts:
    oaMsa300PinAlarmTable.setStatus("current")
_OaMsa300PinAlarmEntry_Object = MibTableRow
oaMsa300PinAlarmEntry = _OaMsa300PinAlarmEntry_Object(
    (1, 3, 6, 1, 4, 1, 6926, 1, 18, 1, 4, 4, 1)
)
oaMsa300PinAlarmEntry.setIndexNames(
    (0, "OA-SFP-MIB", "oaMsa300PinAlarmSlotIndex"),
    (0, "OA-SFP-MIB", "oaMsa300PinAlarmPortIndex"),
)
if mibBuilder.loadTexts:
    oaMsa300PinAlarmEntry.setStatus("current")
_OaMsa300PinAlarmSlotIndex_Type = SlotIndex
_OaMsa300PinAlarmSlotIndex_Object = MibTableColumn
oaMsa300PinAlarmSlotIndex = _OaMsa300PinAlarmSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 6926, 1, 18, 1, 4, 4, 1, 1),
    _OaMsa300PinAlarmSlotIndex_Type()
)
oaMsa300PinAlarmSlotIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    oaMsa300PinAlarmSlotIndex.setStatus("current")
_OaMsa300PinAlarmPortIndex_Type = PortInSlotIndex
_OaMsa300PinAlarmPortIndex_Object = MibTableColumn
oaMsa300PinAlarmPortIndex = _OaMsa300PinAlarmPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 6926, 1, 18, 1, 4, 4, 1, 2),
    _OaMsa300PinAlarmPortIndex_Type()
)
oaMsa300PinAlarmPortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    oaMsa300PinAlarmPortIndex.setStatus("current")


class _OaMsa300PinAlarmTxAlarm_Type(OctetString):
    """Custom type oaMsa300PinAlarmTxAlarm based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 3),
    )
    fixed_length = 3


_OaMsa300PinAlarmTxAlarm_Type.__name__ = "OctetString"
_OaMsa300PinAlarmTxAlarm_Object = MibTableColumn
oaMsa300PinAlarmTxAlarm = _OaMsa300PinAlarmTxAlarm_Object(
    (1, 3, 6, 1, 4, 1, 6926, 1, 18, 1, 4, 4, 1, 3),
    _OaMsa300PinAlarmTxAlarm_Type()
)
oaMsa300PinAlarmTxAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaMsa300PinAlarmTxAlarm.setStatus("current")


class _OaMsa300PinAlarmRxAlarm_Type(OctetString):
    """Custom type oaMsa300PinAlarmRxAlarm based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )
    fixed_length = 2


_OaMsa300PinAlarmRxAlarm_Type.__name__ = "OctetString"
_OaMsa300PinAlarmRxAlarm_Object = MibTableColumn
oaMsa300PinAlarmRxAlarm = _OaMsa300PinAlarmRxAlarm_Object(
    (1, 3, 6, 1, 4, 1, 6926, 1, 18, 1, 4, 4, 1, 4),
    _OaMsa300PinAlarmRxAlarm_Type()
)
oaMsa300PinAlarmRxAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaMsa300PinAlarmRxAlarm.setStatus("current")


class _OaMsa300PinAlarmPsAlarm_Type(OctetString):
    """Custom type oaMsa300PinAlarmPsAlarm based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )
    fixed_length = 1


_OaMsa300PinAlarmPsAlarm_Type.__name__ = "OctetString"
_OaMsa300PinAlarmPsAlarm_Object = MibTableColumn
oaMsa300PinAlarmPsAlarm = _OaMsa300PinAlarmPsAlarm_Object(
    (1, 3, 6, 1, 4, 1, 6926, 1, 18, 1, 4, 4, 1, 5),
    _OaMsa300PinAlarmPsAlarm_Type()
)
oaMsa300PinAlarmPsAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaMsa300PinAlarmPsAlarm.setStatus("current")
_OaMsa300PinComTable_Object = MibTable
oaMsa300PinComTable = _OaMsa300PinComTable_Object(
    (1, 3, 6, 1, 4, 1, 6926, 1, 18, 1, 4, 5)
)
if mibBuilder.loadTexts:
    oaMsa300PinComTable.setStatus("current")
_OaMsa300PinComEntry_Object = MibTableRow
oaMsa300PinComEntry = _OaMsa300PinComEntry_Object(
    (1, 3, 6, 1, 4, 1, 6926, 1, 18, 1, 4, 5, 1)
)
oaMsa300PinComEntry.setIndexNames(
    (0, "OA-SFP-MIB", "oaMsa300PinComSlotIndex"),
    (0, "OA-SFP-MIB", "oaMsa300PinComPortIndex"),
)
if mibBuilder.loadTexts:
    oaMsa300PinComEntry.setStatus("current")
_OaMsa300PinComSlotIndex_Type = SlotIndex
_OaMsa300PinComSlotIndex_Object = MibTableColumn
oaMsa300PinComSlotIndex = _OaMsa300PinComSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 6926, 1, 18, 1, 4, 5, 1, 1),
    _OaMsa300PinComSlotIndex_Type()
)
oaMsa300PinComSlotIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    oaMsa300PinComSlotIndex.setStatus("current")
_OaMsa300PinComPortIndex_Type = PortInSlotIndex
_OaMsa300PinComPortIndex_Object = MibTableColumn
oaMsa300PinComPortIndex = _OaMsa300PinComPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 6926, 1, 18, 1, 4, 5, 1, 2),
    _OaMsa300PinComPortIndex_Type()
)
oaMsa300PinComPortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    oaMsa300PinComPortIndex.setStatus("current")


class _OaMsa300PinComLaserItuBand_Type(Integer32):
    """Custom type oaMsa300PinComLaserItuBand based on Integer32"""
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
        *(("unknown", 1),
          ("cBand", 2),
          ("lBand", 3),
          ("sBand", 4))
    )


_OaMsa300PinComLaserItuBand_Type.__name__ = "Integer32"
_OaMsa300PinComLaserItuBand_Object = MibTableColumn
oaMsa300PinComLaserItuBand = _OaMsa300PinComLaserItuBand_Object(
    (1, 3, 6, 1, 4, 1, 6926, 1, 18, 1, 4, 5, 1, 7),
    _OaMsa300PinComLaserItuBand_Type()
)
oaMsa300PinComLaserItuBand.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oaMsa300PinComLaserItuBand.setStatus("current")
_OaMsa300PinComLaserItuCh_Type = Integer32
_OaMsa300PinComLaserItuCh_Object = MibTableColumn
oaMsa300PinComLaserItuCh = _OaMsa300PinComLaserItuCh_Object(
    (1, 3, 6, 1, 4, 1, 6926, 1, 18, 1, 4, 5, 1, 8),
    _OaMsa300PinComLaserItuCh_Type()
)
oaMsa300PinComLaserItuCh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oaMsa300PinComLaserItuCh.setStatus("current")
if mibBuilder.loadTexts:
    oaMsa300PinComLaserItuCh.setUnits("0.01 Nano Meter(nm)")
_OaSfpConformance_ObjectIdentity = ObjectIdentity
oaSfpConformance = _OaSfpConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6926, 1, 18, 2)
)
_OaSfpGroups_ObjectIdentity = ObjectIdentity
oaSfpGroups = _OaSfpGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6926, 1, 18, 2, 1)
)
_OaSfpCompliances_ObjectIdentity = ObjectIdentity
oaSfpCompliances = _OaSfpCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6926, 1, 18, 2, 2)
)

# Managed Objects groups

oaSfpCompatibleIfCountGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6926, 1, 18, 2, 1, 1)
)
oaSfpCompatibleIfCountGroup.setObjects(
      *(("OA-SFP-MIB", "oaSfpCompatibleInterfaceCount"),
        ("OA-SFP-MIB", "oaXfpCompatibleInterfaceCount"),
        ("OA-SFP-MIB", "oaDsfpCompatibleInterfaceCount"),
        ("OA-SFP-MIB", "oaMsa300PinCompatibleIfCount"))
)
if mibBuilder.loadTexts:
    oaSfpCompatibleIfCountGroup.setStatus("current")

oaSfpGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6926, 1, 18, 2, 1, 2)
)
oaSfpGroup.setObjects(
      *(("OA-SFP-MIB", "oaSfpInfoIdentifier"),
        ("OA-SFP-MIB", "oaSfpInfoVendorSpecificIdentifier"),
        ("OA-SFP-MIB", "oaSfpInfoConnector"),
        ("OA-SFP-MIB", "oaSfpInfoVendorSpecificConnector"),
        ("OA-SFP-MIB", "oaSfpInfoVendorName"),
        ("OA-SFP-MIB", "oaSfpInfoVendorOUI"),
        ("OA-SFP-MIB", "oaSfpInfoVendorPN"),
        ("OA-SFP-MIB", "oaSfpInfoVendorRev"),
        ("OA-SFP-MIB", "oaSfpInfoLaserWavelength"),
        ("OA-SFP-MIB", "oaSfpTunability"),
        ("OA-SFP-MIB", "oaSfpInfoVendorSN"),
        ("OA-SFP-MIB", "oaSfpInfoVendorDate"),
        ("OA-SFP-MIB", "oaSfpInfoVendorSpecificLotCode"),
        ("OA-SFP-MIB", "oaSfpInfoVendorSpecificData"),
        ("OA-SFP-MIB", "oaSfpInfoDiagnosticPowerType"),
        ("OA-SFP-MIB", "oaSfpInfoDigitalDiagnostic"),
        ("OA-SFP-MIB", "oaSfpInfoDiagnosticCalibration"),
        ("OA-SFP-MIB", "oaSfpInfoInstalledStatus"),
        ("OA-SFP-MIB", "oaSfpInfofaultStatus"),
        ("OA-SFP-MIB", "oaSfpInfoEnableStatus"),
        ("OA-SFP-MIB", "oaSfpDiagnosticTemperature"),
        ("OA-SFP-MIB", "oaSfpDiagnosticVcc"),
        ("OA-SFP-MIB", "oaSfpDiagnosticTxBias"),
        ("OA-SFP-MIB", "oaSfpDiagnosticTxPower"),
        ("OA-SFP-MIB", "oaSfpDiagnosticRxPower"),
        ("OA-SFP-MIB", "oaSfpRatesSupportedValue"))
)
if mibBuilder.loadTexts:
    oaSfpGroup.setStatus("current")

oaXfpGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6926, 1, 18, 2, 1, 3)
)
oaXfpGroup.setObjects(
    ("OA-SFP-MIB", "oaXfpInfoLaserWavelengthTolerance")
)
if mibBuilder.loadTexts:
    oaXfpGroup.setStatus("current")

oaDsfpGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6926, 1, 18, 2, 1, 4)
)
oaDsfpGroup.setObjects(
      *(("OA-SFP-MIB", "oaDsfpInfoChannelSpacing"),
        ("OA-SFP-MIB", "oaDsfpInfoChannelTuning"))
)
if mibBuilder.loadTexts:
    oaDsfpGroup.setStatus("current")

oaMsa300PinGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6926, 1, 18, 2, 1, 5)
)
oaMsa300PinGroup.setObjects(
      *(("OA-SFP-MIB", "oaMsa300PinIdModuleTypeCode"),
        ("OA-SFP-MIB", "oaMsa300PinIdFirstLaserItuBand"),
        ("OA-SFP-MIB", "oaMsa300PinIdFirstLaserItuCh"),
        ("OA-SFP-MIB", "oaMsa300PinIdLastLaserItuBand"),
        ("OA-SFP-MIB", "oaMsa300PinIdLastLaserItuCh"),
        ("OA-SFP-MIB", "oaMsa300PinIdLaserItuChSpacing"),
        ("OA-SFP-MIB", "oaMsa300PinMeasLaserOutputPwrMon"),
        ("OA-SFP-MIB", "oaMsa300PinMeasLaserTempMon"),
        ("OA-SFP-MIB", "oaMsa300PinMeasRecSigAvrOptPower"),
        ("OA-SFP-MIB", "oaMsa300PinMeasLaserWlengthMon"),
        ("OA-SFP-MIB", "oaMsa300PinMeasTransTempMon"),
        ("OA-SFP-MIB", "oaMsa300PinAlarmTxAlarm"),
        ("OA-SFP-MIB", "oaMsa300PinAlarmRxAlarm"),
        ("OA-SFP-MIB", "oaMsa300PinAlarmPsAlarm"),
        ("OA-SFP-MIB", "oaMsa300PinComLaserItuBand"),
        ("OA-SFP-MIB", "oaMsa300PinComLaserItuCh"))
)
if mibBuilder.loadTexts:
    oaMsa300PinGroup.setStatus("current")

oaXfpTunGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6926, 1, 18, 2, 1, 6)
)
oaXfpTunGroup.setObjects(
      *(("OA-SFP-MIB", "oaXfpTunLaserFirstFrequency"),
        ("OA-SFP-MIB", "oaXfpTunLaserLastFrequency"),
        ("OA-SFP-MIB", "oaXfpTunGridSpacing"),
        ("OA-SFP-MIB", "oaXfpTunLaserItuBand"),
        ("OA-SFP-MIB", "oaXfpTunLaserItuCh"))
)
if mibBuilder.loadTexts:
    oaXfpTunGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

oaSfpCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6926, 1, 18, 2, 2, 1)
)
oaSfpCompliance.setObjects(
      *(("OA-SFP-MIB", "oaSfpCompatibleIfCountGroup"),
        ("OA-SFP-MIB", "oaSfpGroup"),
        ("OA-SFP-MIB", "oaXfpGroup"),
        ("OA-SFP-MIB", "oaDsfpGroup"),
        ("OA-SFP-MIB", "oaMsa300PinGroup"),
        ("OA-SFP-MIB", "oaXfpTunGroup"))
)
if mibBuilder.loadTexts:
    oaSfpCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "OA-SFP-MIB",
    **{"SlotIndex": SlotIndex,
       "PortInSlotIndex": PortInSlotIndex,
       "oaManagement": oaManagement,
       "oaSfpMib": oaSfpMib,
       "oaSfp": oaSfp,
       "oaSfpMIBObjects": oaSfpMIBObjects,
       "oaSfpCompatibleInterfaceCount": oaSfpCompatibleInterfaceCount,
       "oaSfpInfoTable": oaSfpInfoTable,
       "oaSfpInfoEntry": oaSfpInfoEntry,
       "oaSfpInfoSlotIndex": oaSfpInfoSlotIndex,
       "oaSfpInfoPortIndex": oaSfpInfoPortIndex,
       "oaSfpInfoIdentifier": oaSfpInfoIdentifier,
       "oaSfpInfoVendorSpecificIdentifier": oaSfpInfoVendorSpecificIdentifier,
       "oaSfpInfoConnector": oaSfpInfoConnector,
       "oaSfpInfoVendorSpecificConnector": oaSfpInfoVendorSpecificConnector,
       "oaSfpInfoVendorName": oaSfpInfoVendorName,
       "oaSfpInfoVendorOUI": oaSfpInfoVendorOUI,
       "oaSfpInfoVendorPN": oaSfpInfoVendorPN,
       "oaSfpInfoVendorRev": oaSfpInfoVendorRev,
       "oaSfpInfoLaserWavelength": oaSfpInfoLaserWavelength,
       "oaSfpTunability": oaSfpTunability,
       "oaSfpInfoVendorSN": oaSfpInfoVendorSN,
       "oaSfpInfoVendorDate": oaSfpInfoVendorDate,
       "oaSfpInfoVendorSpecificLotCode": oaSfpInfoVendorSpecificLotCode,
       "oaSfpInfoVendorSpecificData": oaSfpInfoVendorSpecificData,
       "oaSfpInfoDiagnosticPowerType": oaSfpInfoDiagnosticPowerType,
       "oaSfpInfoDigitalDiagnostic": oaSfpInfoDigitalDiagnostic,
       "oaSfpInfoDiagnosticCalibration": oaSfpInfoDiagnosticCalibration,
       "oaSfpInfoInstalledStatus": oaSfpInfoInstalledStatus,
       "oaSfpInfofaultStatus": oaSfpInfofaultStatus,
       "oaSfpInfoEnableStatus": oaSfpInfoEnableStatus,
       "oaSfpInfoUnitName": oaSfpInfoUnitName,
       "oaSfpInfoFiberType": oaSfpInfoFiberType,
       "oaSfpInfoReach": oaSfpInfoReach,
       "oaSfpInfoConnectorType": oaSfpInfoConnectorType,
       "oaSfpInfoItemNum": oaSfpInfoItemNum,
       "oaSfpInfoHWRev": oaSfpInfoHWRev,
       "oaSfpInfoCleiCode": oaSfpInfoCleiCode,
       "oaSfpInfoPageA2hSN": oaSfpInfoPageA2hSN,
       "oaSfpInfoManufactureDate": oaSfpInfoManufactureDate,
       "oaSfpInfoManufactureID": oaSfpInfoManufactureID,
       "oaSfpDiagnosticTable": oaSfpDiagnosticTable,
       "oaSfpDiagnosticEntry": oaSfpDiagnosticEntry,
       "oaSfpDiagnosticSlotIndex": oaSfpDiagnosticSlotIndex,
       "oaSfpDiagnosticPortIndex": oaSfpDiagnosticPortIndex,
       "oaSfpDiagnosticTemperature": oaSfpDiagnosticTemperature,
       "oaSfpDiagnosticVcc": oaSfpDiagnosticVcc,
       "oaSfpDiagnosticTxBias": oaSfpDiagnosticTxBias,
       "oaSfpDiagnosticTxPower": oaSfpDiagnosticTxPower,
       "oaSfpDiagnosticRxPower": oaSfpDiagnosticRxPower,
       "oaSfpRatesSupportedTable": oaSfpRatesSupportedTable,
       "oaSfpRatesSupportedEntry": oaSfpRatesSupportedEntry,
       "oaSfpRatesSupportedIndex": oaSfpRatesSupportedIndex,
       "oaSfpRatesSupportedValue": oaSfpRatesSupportedValue,
       "oaXfpMIBObjects": oaXfpMIBObjects,
       "oaXfpCompatibleInterfaceCount": oaXfpCompatibleInterfaceCount,
       "oaXfpInfoTable": oaXfpInfoTable,
       "oaXfpInfoEntry": oaXfpInfoEntry,
       "oaXfpInfoSlotIndex": oaXfpInfoSlotIndex,
       "oaXfpInfoPortIndex": oaXfpInfoPortIndex,
       "oaXfpInfoLaserWavelengthTolerance": oaXfpInfoLaserWavelengthTolerance,
       "oaXfpTunTable": oaXfpTunTable,
       "oaXfpTunEntry": oaXfpTunEntry,
       "oaXfpTunSlotIndex": oaXfpTunSlotIndex,
       "oaXfpTunPortIndex": oaXfpTunPortIndex,
       "oaXfpTunLaserFirstFrequency": oaXfpTunLaserFirstFrequency,
       "oaXfpTunLaserLastFrequency": oaXfpTunLaserLastFrequency,
       "oaXfpTunGridSpacing": oaXfpTunGridSpacing,
       "oaXfpTunLaserItuBand": oaXfpTunLaserItuBand,
       "oaXfpTunLaserItuCh": oaXfpTunLaserItuCh,
       "oaDsfpMIBObjects": oaDsfpMIBObjects,
       "oaDsfpCompatibleInterfaceCount": oaDsfpCompatibleInterfaceCount,
       "oaDsfpInfoTable": oaDsfpInfoTable,
       "oaDsfpInfoEntry": oaDsfpInfoEntry,
       "oaDsfpInfoSlotIndex": oaDsfpInfoSlotIndex,
       "oaDsfpInfoPortIndex": oaDsfpInfoPortIndex,
       "oaDsfpInfoChannelSpacing": oaDsfpInfoChannelSpacing,
       "oaDsfpInfoChannelTuning": oaDsfpInfoChannelTuning,
       "oaMsa300PinMIBObjects": oaMsa300PinMIBObjects,
       "oaMsa300PinCompatibleIfCount": oaMsa300PinCompatibleIfCount,
       "oaMsa300PinIdTable": oaMsa300PinIdTable,
       "oaMsa300PinIdEntry": oaMsa300PinIdEntry,
       "oaMsa300PinIdSlotIndex": oaMsa300PinIdSlotIndex,
       "oaMsa300PinIdPortIndex": oaMsa300PinIdPortIndex,
       "oaMsa300PinIdModuleTypeCode": oaMsa300PinIdModuleTypeCode,
       "oaMsa300PinIdFirstLaserItuBand": oaMsa300PinIdFirstLaserItuBand,
       "oaMsa300PinIdFirstLaserItuCh": oaMsa300PinIdFirstLaserItuCh,
       "oaMsa300PinIdLastLaserItuBand": oaMsa300PinIdLastLaserItuBand,
       "oaMsa300PinIdLastLaserItuCh": oaMsa300PinIdLastLaserItuCh,
       "oaMsa300PinIdLaserItuChSpacing": oaMsa300PinIdLaserItuChSpacing,
       "oaMsa300PinMeasTable": oaMsa300PinMeasTable,
       "oaMsa300PinMeasEntry": oaMsa300PinMeasEntry,
       "oaMsa300PinMeasSlotIndex": oaMsa300PinMeasSlotIndex,
       "oaMsa300PinMeasPortIndex": oaMsa300PinMeasPortIndex,
       "oaMsa300PinMeasLaserOutputPwrMon": oaMsa300PinMeasLaserOutputPwrMon,
       "oaMsa300PinMeasLaserTempMon": oaMsa300PinMeasLaserTempMon,
       "oaMsa300PinMeasRecSigAvrOptPower": oaMsa300PinMeasRecSigAvrOptPower,
       "oaMsa300PinMeasLaserWlengthMon": oaMsa300PinMeasLaserWlengthMon,
       "oaMsa300PinMeasTransTempMon": oaMsa300PinMeasTransTempMon,
       "oaMsa300PinAlarmTable": oaMsa300PinAlarmTable,
       "oaMsa300PinAlarmEntry": oaMsa300PinAlarmEntry,
       "oaMsa300PinAlarmSlotIndex": oaMsa300PinAlarmSlotIndex,
       "oaMsa300PinAlarmPortIndex": oaMsa300PinAlarmPortIndex,
       "oaMsa300PinAlarmTxAlarm": oaMsa300PinAlarmTxAlarm,
       "oaMsa300PinAlarmRxAlarm": oaMsa300PinAlarmRxAlarm,
       "oaMsa300PinAlarmPsAlarm": oaMsa300PinAlarmPsAlarm,
       "oaMsa300PinComTable": oaMsa300PinComTable,
       "oaMsa300PinComEntry": oaMsa300PinComEntry,
       "oaMsa300PinComSlotIndex": oaMsa300PinComSlotIndex,
       "oaMsa300PinComPortIndex": oaMsa300PinComPortIndex,
       "oaMsa300PinComLaserItuBand": oaMsa300PinComLaserItuBand,
       "oaMsa300PinComLaserItuCh": oaMsa300PinComLaserItuCh,
       "oaSfpConformance": oaSfpConformance,
       "oaSfpGroups": oaSfpGroups,
       "oaSfpCompatibleIfCountGroup": oaSfpCompatibleIfCountGroup,
       "oaSfpGroup": oaSfpGroup,
       "oaXfpGroup": oaXfpGroup,
       "oaDsfpGroup": oaDsfpGroup,
       "oaMsa300PinGroup": oaMsa300PinGroup,
       "oaXfpTunGroup": oaXfpTunGroup,
       "oaSfpCompliances": oaSfpCompliances,
       "oaSfpCompliance": oaSfpCompliance}
)
