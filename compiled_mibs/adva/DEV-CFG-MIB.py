# SNMP MIB module (DEV-CFG-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\adva\DEV-CFG-MIB

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

(nbSwitchG1Il,) = mibBuilder.importSymbols(
    "OS-COMMON-TC-MIB",
    "nbSwitchG1Il")

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
 NotificationType,
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
    "NotificationType",
    "TimeTicks",
    "Unsigned32",
    "enterprises",
    "iso")

(DisplayString,
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_NbDeviceConfig_ObjectIdentity = ObjectIdentity
nbDeviceConfig = _NbDeviceConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 11)
)
_NbDevGen_ObjectIdentity = ObjectIdentity
nbDevGen = _NbDevGen_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 11, 1)
)


class _NbDevOperationMode_Type(Integer32):
    """Custom type nbDevOperationMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("accelerouter", 1),
          ("router", 2),
          ("switch", 3))
    )


_NbDevOperationMode_Type.__name__ = "Integer32"
_NbDevOperationMode_Object = MibScalar
nbDevOperationMode = _NbDevOperationMode_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 11, 1, 1),
    _NbDevOperationMode_Type()
)
nbDevOperationMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbDevOperationMode.setStatus("mandatory")
_NbDevErrorText_Type = DisplayString
_NbDevErrorText_Object = MibScalar
nbDevErrorText = _NbDevErrorText_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 11, 1, 2),
    _NbDevErrorText_Type()
)
nbDevErrorText.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbDevErrorText.setStatus("mandatory")


class _NbsDevTftpMode_Type(Integer32):
    """Custom type nbsDevTftpMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("server", 2),
          ("client", 3))
    )


_NbsDevTftpMode_Type.__name__ = "Integer32"
_NbsDevTftpMode_Object = MibScalar
nbsDevTftpMode = _NbsDevTftpMode_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 11, 1, 3),
    _NbsDevTftpMode_Type()
)
nbsDevTftpMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbsDevTftpMode.setStatus("mandatory")


class _NbDevRouterSaveConfig_Type(Integer32):
    """Custom type nbDevRouterSaveConfig based on Integer32"""
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
        *(("saveConfig", 1),
          ("warmReset", 2),
          ("coldReset", 3),
          ("backupReset", 4))
    )


_NbDevRouterSaveConfig_Type.__name__ = "Integer32"
_NbDevRouterSaveConfig_Object = MibScalar
nbDevRouterSaveConfig = _NbDevRouterSaveConfig_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 11, 1, 4),
    _NbDevRouterSaveConfig_Type()
)
nbDevRouterSaveConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbDevRouterSaveConfig.setStatus("mandatory")


class _NbsDevProperties_Type(Integer32):
    """Custom type nbsDevProperties based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              4,
              8,
              16,
              32,
              64,
              128,
              256,
              512)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("redundantPowerSupply", 1),
          ("highDensityFibrePorts", 2),
          ("dcPowerSupply", 4),
          ("optiSwitch100FX", 8),
          ("chipModification", 16),
          ("expensiveModification", 32),
          ("telcoSubType", 64),
          ("extendedTempRange", 128),
          ("extraExtendedTempRange", 256),
          ("ptpSlaveSync", 512))
    )


_NbsDevProperties_Type.__name__ = "Integer32"
_NbsDevProperties_Object = MibScalar
nbsDevProperties = _NbsDevProperties_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 11, 1, 5),
    _NbsDevProperties_Type()
)
nbsDevProperties.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsDevProperties.setStatus("mandatory")


class _NbsDevTemperatureMode_Type(Integer32):
    """Custom type nbsDevTemperatureMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("normal", 2),
          ("high", 3))
    )


_NbsDevTemperatureMode_Type.__name__ = "Integer32"
_NbsDevTemperatureMode_Object = MibScalar
nbsDevTemperatureMode = _NbsDevTemperatureMode_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 11, 1, 6),
    _NbsDevTemperatureMode_Type()
)
nbsDevTemperatureMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsDevTemperatureMode.setStatus("mandatory")


class _NbsDevResetAfterDnldMode_Type(Integer32):
    """Custom type nbsDevResetAfterDnldMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("yes", 2),
          ("no", 3))
    )


_NbsDevResetAfterDnldMode_Type.__name__ = "Integer32"
_NbsDevResetAfterDnldMode_Object = MibScalar
nbsDevResetAfterDnldMode = _NbsDevResetAfterDnldMode_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 11, 1, 7),
    _NbsDevResetAfterDnldMode_Type()
)
nbsDevResetAfterDnldMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbsDevResetAfterDnldMode.setStatus("mandatory")
_NbsDevPS_ObjectIdentity = ObjectIdentity
nbsDevPS = _NbsDevPS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 11, 1, 8)
)
_NbsDevPSNumber_Type = Integer32
_NbsDevPSNumber_Object = MibScalar
nbsDevPSNumber = _NbsDevPSNumber_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 11, 1, 8, 1),
    _NbsDevPSNumber_Type()
)
nbsDevPSNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsDevPSNumber.setStatus("mandatory")
_NbsDevPSTable_Object = MibTable
nbsDevPSTable = _NbsDevPSTable_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 11, 1, 8, 2)
)
if mibBuilder.loadTexts:
    nbsDevPSTable.setStatus("mandatory")
_NbsDevPSEntry_Object = MibTableRow
nbsDevPSEntry = _NbsDevPSEntry_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 11, 1, 8, 2, 1)
)
nbsDevPSEntry.setIndexNames(
    (0, "DEV-CFG-MIB", "nbsDevPSIndex"),
)
if mibBuilder.loadTexts:
    nbsDevPSEntry.setStatus("mandatory")
_NbsDevPSIndex_Type = Integer32
_NbsDevPSIndex_Object = MibTableColumn
nbsDevPSIndex = _NbsDevPSIndex_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 11, 1, 8, 2, 1, 1),
    _NbsDevPSIndex_Type()
)
nbsDevPSIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsDevPSIndex.setStatus("mandatory")


class _NbsDevPSType_Type(Integer32):
    """Custom type nbsDevPSType based on Integer32"""
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
        *(("none", 1),
          ("acPS", 2),
          ("dcPS", 3),
          ("externalPS", 4))
    )


_NbsDevPSType_Type.__name__ = "Integer32"
_NbsDevPSType_Object = MibTableColumn
nbsDevPSType = _NbsDevPSType_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 11, 1, 8, 2, 1, 2),
    _NbsDevPSType_Type()
)
nbsDevPSType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsDevPSType.setStatus("mandatory")
_NbsDevPSDescription_Type = DisplayString
_NbsDevPSDescription_Object = MibTableColumn
nbsDevPSDescription = _NbsDevPSDescription_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 11, 1, 8, 2, 1, 3),
    _NbsDevPSDescription_Type()
)
nbsDevPSDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsDevPSDescription.setStatus("mandatory")


class _NbsDevPSRedundantMode_Type(Integer32):
    """Custom type nbsDevPSRedundantMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("mainPS", 2),
          ("secondaryPS", 3))
    )


_NbsDevPSRedundantMode_Type.__name__ = "Integer32"
_NbsDevPSRedundantMode_Object = MibTableColumn
nbsDevPSRedundantMode = _NbsDevPSRedundantMode_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 11, 1, 8, 2, 1, 4),
    _NbsDevPSRedundantMode_Type()
)
nbsDevPSRedundantMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsDevPSRedundantMode.setStatus("mandatory")


class _NbsDevPSOperStatus_Type(Integer32):
    """Custom type nbsDevPSOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("active", 2),
          ("notActive", 3))
    )


_NbsDevPSOperStatus_Type.__name__ = "Integer32"
_NbsDevPSOperStatus_Object = MibTableColumn
nbsDevPSOperStatus = _NbsDevPSOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 11, 1, 8, 2, 1, 5),
    _NbsDevPSOperStatus_Type()
)
nbsDevPSOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsDevPSOperStatus.setStatus("mandatory")


class _NbsDevPSAdminStatus_Type(Integer32):
    """Custom type nbsDevPSAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("active", 2),
          ("notActive", 3))
    )


_NbsDevPSAdminStatus_Type.__name__ = "Integer32"
_NbsDevPSAdminStatus_Object = MibTableColumn
nbsDevPSAdminStatus = _NbsDevPSAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 11, 1, 8, 2, 1, 6),
    _NbsDevPSAdminStatus_Type()
)
nbsDevPSAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbsDevPSAdminStatus.setStatus("mandatory")
_NbsDevPSInput_ObjectIdentity = ObjectIdentity
nbsDevPSInput = _NbsDevPSInput_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 11, 1, 9)
)
_NbsDevPSInputNumber_Type = Integer32
_NbsDevPSInputNumber_Object = MibScalar
nbsDevPSInputNumber = _NbsDevPSInputNumber_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 11, 1, 9, 1),
    _NbsDevPSInputNumber_Type()
)
nbsDevPSInputNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsDevPSInputNumber.setStatus("mandatory")
_NbsDevPSInputTable_Object = MibTable
nbsDevPSInputTable = _NbsDevPSInputTable_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 11, 1, 9, 2)
)
if mibBuilder.loadTexts:
    nbsDevPSInputTable.setStatus("mandatory")
_NbsDevPSInputEntry_Object = MibTableRow
nbsDevPSInputEntry = _NbsDevPSInputEntry_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 11, 1, 9, 2, 1)
)
nbsDevPSInputEntry.setIndexNames(
    (0, "DEV-CFG-MIB", "nbsDevPSInputIndex"),
)
if mibBuilder.loadTexts:
    nbsDevPSInputEntry.setStatus("mandatory")
_NbsDevPSInputIndex_Type = Integer32
_NbsDevPSInputIndex_Object = MibTableColumn
nbsDevPSInputIndex = _NbsDevPSInputIndex_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 11, 1, 9, 2, 1, 1),
    _NbsDevPSInputIndex_Type()
)
nbsDevPSInputIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsDevPSInputIndex.setStatus("mandatory")


class _NbsDevPSInputType_Type(Integer32):
    """Custom type nbsDevPSInputType based on Integer32"""
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
        *(("none", 1),
          ("acInput", 2),
          ("dcInput", 3),
          ("dcRedundInput", 4))
    )


_NbsDevPSInputType_Type.__name__ = "Integer32"
_NbsDevPSInputType_Object = MibTableColumn
nbsDevPSInputType = _NbsDevPSInputType_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 11, 1, 9, 2, 1, 2),
    _NbsDevPSInputType_Type()
)
nbsDevPSInputType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsDevPSInputType.setStatus("mandatory")
_NbsDevPSInputDescription_Type = DisplayString
_NbsDevPSInputDescription_Object = MibTableColumn
nbsDevPSInputDescription = _NbsDevPSInputDescription_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 11, 1, 9, 2, 1, 3),
    _NbsDevPSInputDescription_Type()
)
nbsDevPSInputDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsDevPSInputDescription.setStatus("mandatory")


class _NbsDevPSInputRedundantMode_Type(Integer32):
    """Custom type nbsDevPSInputRedundantMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("mainInput", 2),
          ("secondaryInput", 3))
    )


_NbsDevPSInputRedundantMode_Type.__name__ = "Integer32"
_NbsDevPSInputRedundantMode_Object = MibTableColumn
nbsDevPSInputRedundantMode = _NbsDevPSInputRedundantMode_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 11, 1, 9, 2, 1, 4),
    _NbsDevPSInputRedundantMode_Type()
)
nbsDevPSInputRedundantMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsDevPSInputRedundantMode.setStatus("mandatory")


class _NbsDevPSInputOperStatus_Type(Integer32):
    """Custom type nbsDevPSInputOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("active", 2),
          ("notActive", 3))
    )


_NbsDevPSInputOperStatus_Type.__name__ = "Integer32"
_NbsDevPSInputOperStatus_Object = MibTableColumn
nbsDevPSInputOperStatus = _NbsDevPSInputOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 11, 1, 9, 2, 1, 5),
    _NbsDevPSInputOperStatus_Type()
)
nbsDevPSInputOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsDevPSInputOperStatus.setStatus("mandatory")


class _NbsDevPSInputAdminStatus_Type(Integer32):
    """Custom type nbsDevPSInputAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("active", 2),
          ("notActive", 3))
    )


_NbsDevPSInputAdminStatus_Type.__name__ = "Integer32"
_NbsDevPSInputAdminStatus_Object = MibTableColumn
nbsDevPSInputAdminStatus = _NbsDevPSInputAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 11, 1, 9, 2, 1, 6),
    _NbsDevPSInputAdminStatus_Type()
)
nbsDevPSInputAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbsDevPSInputAdminStatus.setStatus("mandatory")
_NbsDevCPU_ObjectIdentity = ObjectIdentity
nbsDevCPU = _NbsDevCPU_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 11, 1, 10)
)
_NbsDevCPUNumber_Type = Integer32
_NbsDevCPUNumber_Object = MibScalar
nbsDevCPUNumber = _NbsDevCPUNumber_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 11, 1, 10, 1),
    _NbsDevCPUNumber_Type()
)
nbsDevCPUNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsDevCPUNumber.setStatus("mandatory")
_NbsDevCPUTable_Object = MibTable
nbsDevCPUTable = _NbsDevCPUTable_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 11, 1, 10, 2)
)
if mibBuilder.loadTexts:
    nbsDevCPUTable.setStatus("mandatory")
_NbsDevCPUEntry_Object = MibTableRow
nbsDevCPUEntry = _NbsDevCPUEntry_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 11, 1, 10, 2, 1)
)
nbsDevCPUEntry.setIndexNames(
    (0, "DEV-CFG-MIB", "nbsDevCPUIndex"),
)
if mibBuilder.loadTexts:
    nbsDevCPUEntry.setStatus("mandatory")
_NbsDevCPUIndex_Type = Integer32
_NbsDevCPUIndex_Object = MibTableColumn
nbsDevCPUIndex = _NbsDevCPUIndex_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 11, 1, 10, 2, 1, 1),
    _NbsDevCPUIndex_Type()
)
nbsDevCPUIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsDevCPUIndex.setStatus("mandatory")


class _NbsDevCPUType_Type(Integer32):
    """Custom type nbsDevCPUType based on Integer32"""
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
        *(("none", 1),
          ("cx33cpu2MBflash16MBdram", 2),
          ("cx33cpu4MBflash16MBdram", 3),
          ("cx33cpu4MBflash64MBdram", 4))
    )


_NbsDevCPUType_Type.__name__ = "Integer32"
_NbsDevCPUType_Object = MibTableColumn
nbsDevCPUType = _NbsDevCPUType_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 11, 1, 10, 2, 1, 2),
    _NbsDevCPUType_Type()
)
nbsDevCPUType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsDevCPUType.setStatus("mandatory")
_NbsDevCPUDescription_Type = DisplayString
_NbsDevCPUDescription_Object = MibTableColumn
nbsDevCPUDescription = _NbsDevCPUDescription_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 11, 1, 10, 2, 1, 3),
    _NbsDevCPUDescription_Type()
)
nbsDevCPUDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsDevCPUDescription.setStatus("mandatory")


class _NbsDevCPURedundantMode_Type(Integer32):
    """Custom type nbsDevCPURedundantMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("mainCPU", 2),
          ("redundantCPU", 3))
    )


_NbsDevCPURedundantMode_Type.__name__ = "Integer32"
_NbsDevCPURedundantMode_Object = MibTableColumn
nbsDevCPURedundantMode = _NbsDevCPURedundantMode_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 11, 1, 10, 2, 1, 4),
    _NbsDevCPURedundantMode_Type()
)
nbsDevCPURedundantMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsDevCPURedundantMode.setStatus("mandatory")


class _NbsDevCPUOperStatus_Type(Integer32):
    """Custom type nbsDevCPUOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("enabled", 2),
          ("disabled", 3))
    )


_NbsDevCPUOperStatus_Type.__name__ = "Integer32"
_NbsDevCPUOperStatus_Object = MibTableColumn
nbsDevCPUOperStatus = _NbsDevCPUOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 11, 1, 10, 2, 1, 5),
    _NbsDevCPUOperStatus_Type()
)
nbsDevCPUOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsDevCPUOperStatus.setStatus("mandatory")


class _NbsDevCPUAdminStatus_Type(Integer32):
    """Custom type nbsDevCPUAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("enable", 2),
          ("disable", 3))
    )


_NbsDevCPUAdminStatus_Type.__name__ = "Integer32"
_NbsDevCPUAdminStatus_Object = MibTableColumn
nbsDevCPUAdminStatus = _NbsDevCPUAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 11, 1, 10, 2, 1, 6),
    _NbsDevCPUAdminStatus_Type()
)
nbsDevCPUAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbsDevCPUAdminStatus.setStatus("mandatory")
_NbsDevCPUOrderNumber_Type = Integer32
_NbsDevCPUOrderNumber_Object = MibTableColumn
nbsDevCPUOrderNumber = _NbsDevCPUOrderNumber_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 11, 1, 10, 2, 1, 7),
    _NbsDevCPUOrderNumber_Type()
)
nbsDevCPUOrderNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsDevCPUOrderNumber.setStatus("mandatory")
_NbsDevFAN_ObjectIdentity = ObjectIdentity
nbsDevFAN = _NbsDevFAN_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 11, 1, 11)
)
_NbsDevFANsNumber_Type = Integer32
_NbsDevFANsNumber_Object = MibScalar
nbsDevFANsNumber = _NbsDevFANsNumber_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 11, 1, 11, 1),
    _NbsDevFANsNumber_Type()
)
nbsDevFANsNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsDevFANsNumber.setStatus("mandatory")
_NbsDevFANTable_Object = MibTable
nbsDevFANTable = _NbsDevFANTable_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 11, 1, 11, 2)
)
if mibBuilder.loadTexts:
    nbsDevFANTable.setStatus("mandatory")
_NbsDevFANEntry_Object = MibTableRow
nbsDevFANEntry = _NbsDevFANEntry_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 11, 1, 11, 2, 1)
)
nbsDevFANEntry.setIndexNames(
    (0, "DEV-CFG-MIB", "nbsDevFANIndex"),
)
if mibBuilder.loadTexts:
    nbsDevFANEntry.setStatus("mandatory")
_NbsDevFANIndex_Type = Integer32
_NbsDevFANIndex_Object = MibTableColumn
nbsDevFANIndex = _NbsDevFANIndex_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 11, 1, 11, 2, 1, 1),
    _NbsDevFANIndex_Type()
)
nbsDevFANIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsDevFANIndex.setStatus("mandatory")


class _NbsDevFANType_Type(Integer32):
    """Custom type nbsDevFANType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("fixed", 2),
          ("pwm", 3))
    )


_NbsDevFANType_Type.__name__ = "Integer32"
_NbsDevFANType_Object = MibTableColumn
nbsDevFANType = _NbsDevFANType_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 11, 1, 11, 2, 1, 2),
    _NbsDevFANType_Type()
)
nbsDevFANType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsDevFANType.setStatus("mandatory")
_NbsDevFANDescription_Type = DisplayString
_NbsDevFANDescription_Object = MibTableColumn
nbsDevFANDescription = _NbsDevFANDescription_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 11, 1, 11, 2, 1, 3),
    _NbsDevFANDescription_Type()
)
nbsDevFANDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsDevFANDescription.setStatus("mandatory")


class _NbsDevFANOperStatus_Type(Integer32):
    """Custom type nbsDevFANOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("active", 2),
          ("notActive", 3))
    )


_NbsDevFANOperStatus_Type.__name__ = "Integer32"
_NbsDevFANOperStatus_Object = MibTableColumn
nbsDevFANOperStatus = _NbsDevFANOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 11, 1, 11, 2, 1, 5),
    _NbsDevFANOperStatus_Type()
)
nbsDevFANOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsDevFANOperStatus.setStatus("mandatory")


class _NbsDevFANAdminStatus_Type(Integer32):
    """Custom type nbsDevFANAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("active", 2),
          ("notActive", 3))
    )


_NbsDevFANAdminStatus_Type.__name__ = "Integer32"
_NbsDevFANAdminStatus_Object = MibTableColumn
nbsDevFANAdminStatus = _NbsDevFANAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 11, 1, 11, 2, 1, 6),
    _NbsDevFANAdminStatus_Type()
)
nbsDevFANAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbsDevFANAdminStatus.setStatus("mandatory")
_NbsDevFANSpeed_Type = Integer32
_NbsDevFANSpeed_Object = MibTableColumn
nbsDevFANSpeed = _NbsDevFANSpeed_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 11, 1, 11, 2, 1, 7),
    _NbsDevFANSpeed_Type()
)
nbsDevFANSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsDevFANSpeed.setStatus("mandatory")


class _NbsDevHeaterStatus_Type(Integer32):
    """Custom type nbsDevHeaterStatus based on Integer32"""
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
          ("on", 2),
          ("off", 3))
    )


_NbsDevHeaterStatus_Type.__name__ = "Integer32"
_NbsDevHeaterStatus_Object = MibScalar
nbsDevHeaterStatus = _NbsDevHeaterStatus_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 11, 1, 12),
    _NbsDevHeaterStatus_Type()
)
nbsDevHeaterStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsDevHeaterStatus.setStatus("mandatory")
_NbsDevPhysParams_ObjectIdentity = ObjectIdentity
nbsDevPhysParams = _NbsDevPhysParams_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 11, 1, 13)
)
_NbsDevPhParamDevAmbientTempC_Type = Unsigned32
_NbsDevPhParamDevAmbientTempC_Object = MibScalar
nbsDevPhParamDevAmbientTempC = _NbsDevPhParamDevAmbientTempC_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 11, 1, 13, 1),
    _NbsDevPhParamDevAmbientTempC_Type()
)
nbsDevPhParamDevAmbientTempC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsDevPhParamDevAmbientTempC.setStatus("mandatory")
_NbsDevPhParamPackProcTempC_Type = Unsigned32
_NbsDevPhParamPackProcTempC_Object = MibScalar
nbsDevPhParamPackProcTempC = _NbsDevPhParamPackProcTempC_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 11, 1, 13, 2),
    _NbsDevPhParamPackProcTempC_Type()
)
nbsDevPhParamPackProcTempC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsDevPhParamPackProcTempC.setStatus("mandatory")
_NbsDevPhParamCpuTempC_Type = Unsigned32
_NbsDevPhParamCpuTempC_Object = MibScalar
nbsDevPhParamCpuTempC = _NbsDevPhParamCpuTempC_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 11, 1, 13, 3),
    _NbsDevPhParamCpuTempC_Type()
)
nbsDevPhParamCpuTempC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsDevPhParamCpuTempC.setStatus("mandatory")
_NbsDevPhParamDevAmbientTempF_Type = Unsigned32
_NbsDevPhParamDevAmbientTempF_Object = MibScalar
nbsDevPhParamDevAmbientTempF = _NbsDevPhParamDevAmbientTempF_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 11, 1, 13, 7),
    _NbsDevPhParamDevAmbientTempF_Type()
)
nbsDevPhParamDevAmbientTempF.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsDevPhParamDevAmbientTempF.setStatus("mandatory")
_NbsDevPhParamPackProcTempF_Type = Unsigned32
_NbsDevPhParamPackProcTempF_Object = MibScalar
nbsDevPhParamPackProcTempF = _NbsDevPhParamPackProcTempF_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 11, 1, 13, 8),
    _NbsDevPhParamPackProcTempF_Type()
)
nbsDevPhParamPackProcTempF.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsDevPhParamPackProcTempF.setStatus("mandatory")
_NbsDevPhParamCpuTempF_Type = Unsigned32
_NbsDevPhParamCpuTempF_Object = MibScalar
nbsDevPhParamCpuTempF = _NbsDevPhParamCpuTempF_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 11, 1, 13, 9),
    _NbsDevPhParamCpuTempF_Type()
)
nbsDevPhParamCpuTempF.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsDevPhParamCpuTempF.setStatus("mandatory")
_NbsDevPSHost_ObjectIdentity = ObjectIdentity
nbsDevPSHost = _NbsDevPSHost_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 11, 1, 14)
)
_NbsDevPSHostsNumber_Type = Integer32
_NbsDevPSHostsNumber_Object = MibScalar
nbsDevPSHostsNumber = _NbsDevPSHostsNumber_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 11, 1, 14, 1),
    _NbsDevPSHostsNumber_Type()
)
nbsDevPSHostsNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsDevPSHostsNumber.setStatus("mandatory")
_NbsDevPSHostTable_Object = MibTable
nbsDevPSHostTable = _NbsDevPSHostTable_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 11, 1, 14, 2)
)
if mibBuilder.loadTexts:
    nbsDevPSHostTable.setStatus("mandatory")
_NbsDevPSHostEntry_Object = MibTableRow
nbsDevPSHostEntry = _NbsDevPSHostEntry_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 11, 1, 14, 2, 1)
)
nbsDevPSHostEntry.setIndexNames(
    (0, "DEV-CFG-MIB", "nbsDevPSHostIndex"),
)
if mibBuilder.loadTexts:
    nbsDevPSHostEntry.setStatus("mandatory")
_NbsDevPSHostIndex_Type = Integer32
_NbsDevPSHostIndex_Object = MibTableColumn
nbsDevPSHostIndex = _NbsDevPSHostIndex_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 11, 1, 14, 2, 1, 1),
    _NbsDevPSHostIndex_Type()
)
nbsDevPSHostIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsDevPSHostIndex.setStatus("mandatory")


class _NbsDevPSHostType_Type(Integer32):
    """Custom type nbsDevPSHostType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("acPSHost", 2),
          ("dcPSHost", 3))
    )


_NbsDevPSHostType_Type.__name__ = "Integer32"
_NbsDevPSHostType_Object = MibTableColumn
nbsDevPSHostType = _NbsDevPSHostType_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 11, 1, 14, 2, 1, 2),
    _NbsDevPSHostType_Type()
)
nbsDevPSHostType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsDevPSHostType.setStatus("mandatory")
_NbsDevPSHostDescr_Type = DisplayString
_NbsDevPSHostDescr_Object = MibTableColumn
nbsDevPSHostDescr = _NbsDevPSHostDescr_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 11, 1, 14, 2, 1, 3),
    _NbsDevPSHostDescr_Type()
)
nbsDevPSHostDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsDevPSHostDescr.setStatus("mandatory")
_NbsDevPSHostPSNumber_Type = Integer32
_NbsDevPSHostPSNumber_Object = MibTableColumn
nbsDevPSHostPSNumber = _NbsDevPSHostPSNumber_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 11, 1, 14, 2, 1, 4),
    _NbsDevPSHostPSNumber_Type()
)
nbsDevPSHostPSNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsDevPSHostPSNumber.setStatus("mandatory")
_NbsDevPSHostFirstPS_Type = Integer32
_NbsDevPSHostFirstPS_Object = MibTableColumn
nbsDevPSHostFirstPS = _NbsDevPSHostFirstPS_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 11, 1, 14, 2, 1, 6),
    _NbsDevPSHostFirstPS_Type()
)
nbsDevPSHostFirstPS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsDevPSHostFirstPS.setStatus("mandatory")


class _NbsDevPSHostOperStatus_Type(Integer32):
    """Custom type nbsDevPSHostOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("active", 2),
          ("notActive", 3))
    )


_NbsDevPSHostOperStatus_Type.__name__ = "Integer32"
_NbsDevPSHostOperStatus_Object = MibTableColumn
nbsDevPSHostOperStatus = _NbsDevPSHostOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 11, 1, 14, 2, 1, 8),
    _NbsDevPSHostOperStatus_Type()
)
nbsDevPSHostOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsDevPSHostOperStatus.setStatus("mandatory")


class _NbsDevPSHostAdminStatus_Type(Integer32):
    """Custom type nbsDevPSHostAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("active", 2),
          ("notActive", 3))
    )


_NbsDevPSHostAdminStatus_Type.__name__ = "Integer32"
_NbsDevPSHostAdminStatus_Object = MibTableColumn
nbsDevPSHostAdminStatus = _NbsDevPSHostAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 11, 1, 14, 2, 1, 10),
    _NbsDevPSHostAdminStatus_Type()
)
nbsDevPSHostAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbsDevPSHostAdminStatus.setStatus("mandatory")


class _NbsDevTemperatureProfile_Type(Integer32):
    """Custom type nbsDevTemperatureProfile based on Integer32"""
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
        *(("unknown", 1),
          ("commercial", 2),
          ("extreme", 3),
          ("industrial", 4),
          ("nebsF2B", 5),
          ("nebsS2S", 6))
    )


_NbsDevTemperatureProfile_Type.__name__ = "Integer32"
_NbsDevTemperatureProfile_Object = MibScalar
nbsDevTemperatureProfile = _NbsDevTemperatureProfile_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 11, 1, 15),
    _NbsDevTemperatureProfile_Type()
)
nbsDevTemperatureProfile.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsDevTemperatureProfile.setStatus("mandatory")
_NbsDevTrapVars_ObjectIdentity = ObjectIdentity
nbsDevTrapVars = _NbsDevTrapVars_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 11, 1, 50)
)


class _NbsDevSessionType_Type(Integer32):
    """Custom type nbsDevSessionType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("cliSession", 1),
          ("telnetSession", 2),
          ("none", 3))
    )


_NbsDevSessionType_Type.__name__ = "Integer32"
_NbsDevSessionType_Object = MibScalar
nbsDevSessionType = _NbsDevSessionType_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 11, 1, 50, 1),
    _NbsDevSessionType_Type()
)
nbsDevSessionType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsDevSessionType.setStatus("mandatory")


class _NbsDevAuthenticationRejectReason_Type(Integer32):
    """Custom type nbsDevAuthenticationRejectReason based on Integer32"""
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
        *(("localAgentReject", 1),
          ("radiusServerReject", 2),
          ("radiusServerNotFound", 3),
          ("none", 4))
    )


_NbsDevAuthenticationRejectReason_Type.__name__ = "Integer32"
_NbsDevAuthenticationRejectReason_Object = MibScalar
nbsDevAuthenticationRejectReason = _NbsDevAuthenticationRejectReason_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 11, 1, 50, 2),
    _NbsDevAuthenticationRejectReason_Type()
)
nbsDevAuthenticationRejectReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsDevAuthenticationRejectReason.setStatus("mandatory")


class _NbsTrapLoginName_Type(DisplayString):
    """Custom type nbsTrapLoginName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_NbsTrapLoginName_Type.__name__ = "DisplayString"
_NbsTrapLoginName_Object = MibScalar
nbsTrapLoginName = _NbsTrapLoginName_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 11, 1, 50, 5),
    _NbsTrapLoginName_Type()
)
nbsTrapLoginName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsTrapLoginName.setStatus("mandatory")


class _NbsTrapHostIpAddress_Type(DisplayString):
    """Custom type nbsTrapHostIpAddress based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_NbsTrapHostIpAddress_Type.__name__ = "DisplayString"
_NbsTrapHostIpAddress_Object = MibScalar
nbsTrapHostIpAddress = _NbsTrapHostIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 11, 1, 50, 6),
    _NbsTrapHostIpAddress_Type()
)
nbsTrapHostIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsTrapHostIpAddress.setStatus("mandatory")


class _NbsTrapWrongAccessDateTime_Type(DisplayString):
    """Custom type nbsTrapWrongAccessDateTime based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_NbsTrapWrongAccessDateTime_Type.__name__ = "DisplayString"
_NbsTrapWrongAccessDateTime_Object = MibScalar
nbsTrapWrongAccessDateTime = _NbsTrapWrongAccessDateTime_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 11, 1, 50, 7),
    _NbsTrapWrongAccessDateTime_Type()
)
nbsTrapWrongAccessDateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsTrapWrongAccessDateTime.setStatus("mandatory")
_NbsTrapRCMredundancyState_Type = DisplayString
_NbsTrapRCMredundancyState_Object = MibScalar
nbsTrapRCMredundancyState = _NbsTrapRCMredundancyState_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 11, 1, 50, 8),
    _NbsTrapRCMredundancyState_Type()
)
nbsTrapRCMredundancyState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsTrapRCMredundancyState.setStatus("mandatory")


class _NbsDevSNMPAccessMode_Type(Integer32):
    """Custom type nbsDevSNMPAccessMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("readOnWriteOn", 1),
          ("readOnWriteOff", 2),
          ("readOffWriteOff", 3))
    )


_NbsDevSNMPAccessMode_Type.__name__ = "Integer32"
_NbsDevSNMPAccessMode_Object = MibScalar
nbsDevSNMPAccessMode = _NbsDevSNMPAccessMode_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 11, 1, 50, 10),
    _NbsDevSNMPAccessMode_Type()
)
nbsDevSNMPAccessMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsDevSNMPAccessMode.setStatus("mandatory")
_NbsDeviceTrapReason_Type = DisplayString
_NbsDeviceTrapReason_Object = MibScalar
nbsDeviceTrapReason = _NbsDeviceTrapReason_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 11, 1, 50, 11),
    _NbsDeviceTrapReason_Type()
)
nbsDeviceTrapReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsDeviceTrapReason.setStatus("mandatory")
_NbsDeviceTrapAdminPasswdChangeDescripton_Type = DisplayString
_NbsDeviceTrapAdminPasswdChangeDescripton_Object = MibScalar
nbsDeviceTrapAdminPasswdChangeDescripton = _NbsDeviceTrapAdminPasswdChangeDescripton_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 11, 1, 50, 12),
    _NbsDeviceTrapAdminPasswdChangeDescripton_Type()
)
nbsDeviceTrapAdminPasswdChangeDescripton.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsDeviceTrapAdminPasswdChangeDescripton.setStatus("mandatory")

# Managed Objects groups


# Notification objects

invalidPassword = NotificationType(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 11, 1, 0, 7)
)
invalidPassword.setObjects(
      *(("DEV-CFG-MIB", "nbsDevSessionType"),
        ("DEV-CFG-MIB", "nbsDevAuthenticationRejectReason"),
        ("DEV-CFG-MIB", "nbsTrapHostIpAddress"))
)
if mibBuilder.loadTexts:
    invalidPassword.setStatus(
        ""
    )

wrongAccess = NotificationType(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 11, 1, 0, 8)
)
wrongAccess.setObjects(
      *(("DEV-CFG-MIB", "nbsTrapWrongAccessDateTime"),
        ("DEV-CFG-MIB", "nbsDevSessionType"),
        ("DEV-CFG-MIB", "nbsDevAuthenticationRejectReason"),
        ("DEV-CFG-MIB", "nbsTrapLoginName"),
        ("DEV-CFG-MIB", "nbsTrapHostIpAddress"))
)
if mibBuilder.loadTexts:
    wrongAccess.setStatus(
        ""
    )

deviceRCMredundancyState = NotificationType(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 11, 1, 0, 12)
)
deviceRCMredundancyState.setObjects(
    ("DEV-CFG-MIB", "nbsTrapRCMredundancyState")
)
if mibBuilder.loadTexts:
    deviceRCMredundancyState.setStatus(
        ""
    )

snmpAccessMode = NotificationType(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 11, 1, 0, 20)
)
snmpAccessMode.setObjects(
    ("DEV-CFG-MIB", "nbsDevSNMPAccessMode")
)
if mibBuilder.loadTexts:
    snmpAccessMode.setStatus(
        ""
    )

snmpRequestRejected = NotificationType(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 11, 1, 0, 21)
)
snmpRequestRejected.setObjects(
    ("DEV-CFG-MIB", "nbsDevSNMPAccessMode")
)
if mibBuilder.loadTexts:
    snmpRequestRejected.setStatus(
        ""
    )

deviceTemperatureNormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 11, 1, 0, 48)
)
if mibBuilder.loadTexts:
    deviceTemperatureNormal.setStatus(
        ""
    )

deviceTemperatureHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 11, 1, 0, 49)
)
if mibBuilder.loadTexts:
    deviceTemperatureHigh.setStatus(
        ""
    )

AdminPasswdChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 11, 1, 0, 50)
)
AdminPasswdChange.setObjects(
    ("DEV-CFG-MIB", "nbsDeviceTrapAdminPasswdChangeDescripton")
)
if mibBuilder.loadTexts:
    AdminPasswdChange.setStatus(
        ""
    )

powerSupplyUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 11, 1, 8, 0, 2)
)
powerSupplyUp.setObjects(
    ("DEV-CFG-MIB", "nbsDevPSIndex")
)
if mibBuilder.loadTexts:
    powerSupplyUp.setStatus(
        ""
    )

powerSupplyDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 11, 1, 8, 0, 3)
)
powerSupplyDown.setObjects(
    ("DEV-CFG-MIB", "nbsDevPSIndex")
)
if mibBuilder.loadTexts:
    powerSupplyDown.setStatus(
        ""
    )

fanUnitUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 11, 1, 11, 0, 46)
)
fanUnitUp.setObjects(
    ("DEV-CFG-MIB", "nbsDevFANIndex")
)
if mibBuilder.loadTexts:
    fanUnitUp.setStatus(
        ""
    )

fanUnitDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 11, 1, 11, 0, 47)
)
fanUnitDown.setObjects(
    ("DEV-CFG-MIB", "nbsDevFANIndex")
)
if mibBuilder.loadTexts:
    fanUnitDown.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "DEV-CFG-MIB",
    **{"nbDeviceConfig": nbDeviceConfig,
       "nbDevGen": nbDevGen,
       "invalidPassword": invalidPassword,
       "wrongAccess": wrongAccess,
       "deviceRCMredundancyState": deviceRCMredundancyState,
       "snmpAccessMode": snmpAccessMode,
       "snmpRequestRejected": snmpRequestRejected,
       "deviceTemperatureNormal": deviceTemperatureNormal,
       "deviceTemperatureHigh": deviceTemperatureHigh,
       "AdminPasswdChange": AdminPasswdChange,
       "nbDevOperationMode": nbDevOperationMode,
       "nbDevErrorText": nbDevErrorText,
       "nbsDevTftpMode": nbsDevTftpMode,
       "nbDevRouterSaveConfig": nbDevRouterSaveConfig,
       "nbsDevProperties": nbsDevProperties,
       "nbsDevTemperatureMode": nbsDevTemperatureMode,
       "nbsDevResetAfterDnldMode": nbsDevResetAfterDnldMode,
       "nbsDevPS": nbsDevPS,
       "powerSupplyUp": powerSupplyUp,
       "powerSupplyDown": powerSupplyDown,
       "nbsDevPSNumber": nbsDevPSNumber,
       "nbsDevPSTable": nbsDevPSTable,
       "nbsDevPSEntry": nbsDevPSEntry,
       "nbsDevPSIndex": nbsDevPSIndex,
       "nbsDevPSType": nbsDevPSType,
       "nbsDevPSDescription": nbsDevPSDescription,
       "nbsDevPSRedundantMode": nbsDevPSRedundantMode,
       "nbsDevPSOperStatus": nbsDevPSOperStatus,
       "nbsDevPSAdminStatus": nbsDevPSAdminStatus,
       "nbsDevPSInput": nbsDevPSInput,
       "nbsDevPSInputNumber": nbsDevPSInputNumber,
       "nbsDevPSInputTable": nbsDevPSInputTable,
       "nbsDevPSInputEntry": nbsDevPSInputEntry,
       "nbsDevPSInputIndex": nbsDevPSInputIndex,
       "nbsDevPSInputType": nbsDevPSInputType,
       "nbsDevPSInputDescription": nbsDevPSInputDescription,
       "nbsDevPSInputRedundantMode": nbsDevPSInputRedundantMode,
       "nbsDevPSInputOperStatus": nbsDevPSInputOperStatus,
       "nbsDevPSInputAdminStatus": nbsDevPSInputAdminStatus,
       "nbsDevCPU": nbsDevCPU,
       "nbsDevCPUNumber": nbsDevCPUNumber,
       "nbsDevCPUTable": nbsDevCPUTable,
       "nbsDevCPUEntry": nbsDevCPUEntry,
       "nbsDevCPUIndex": nbsDevCPUIndex,
       "nbsDevCPUType": nbsDevCPUType,
       "nbsDevCPUDescription": nbsDevCPUDescription,
       "nbsDevCPURedundantMode": nbsDevCPURedundantMode,
       "nbsDevCPUOperStatus": nbsDevCPUOperStatus,
       "nbsDevCPUAdminStatus": nbsDevCPUAdminStatus,
       "nbsDevCPUOrderNumber": nbsDevCPUOrderNumber,
       "nbsDevFAN": nbsDevFAN,
       "fanUnitUp": fanUnitUp,
       "fanUnitDown": fanUnitDown,
       "nbsDevFANsNumber": nbsDevFANsNumber,
       "nbsDevFANTable": nbsDevFANTable,
       "nbsDevFANEntry": nbsDevFANEntry,
       "nbsDevFANIndex": nbsDevFANIndex,
       "nbsDevFANType": nbsDevFANType,
       "nbsDevFANDescription": nbsDevFANDescription,
       "nbsDevFANOperStatus": nbsDevFANOperStatus,
       "nbsDevFANAdminStatus": nbsDevFANAdminStatus,
       "nbsDevFANSpeed": nbsDevFANSpeed,
       "nbsDevHeaterStatus": nbsDevHeaterStatus,
       "nbsDevPhysParams": nbsDevPhysParams,
       "nbsDevPhParamDevAmbientTempC": nbsDevPhParamDevAmbientTempC,
       "nbsDevPhParamPackProcTempC": nbsDevPhParamPackProcTempC,
       "nbsDevPhParamCpuTempC": nbsDevPhParamCpuTempC,
       "nbsDevPhParamDevAmbientTempF": nbsDevPhParamDevAmbientTempF,
       "nbsDevPhParamPackProcTempF": nbsDevPhParamPackProcTempF,
       "nbsDevPhParamCpuTempF": nbsDevPhParamCpuTempF,
       "nbsDevPSHost": nbsDevPSHost,
       "nbsDevPSHostsNumber": nbsDevPSHostsNumber,
       "nbsDevPSHostTable": nbsDevPSHostTable,
       "nbsDevPSHostEntry": nbsDevPSHostEntry,
       "nbsDevPSHostIndex": nbsDevPSHostIndex,
       "nbsDevPSHostType": nbsDevPSHostType,
       "nbsDevPSHostDescr": nbsDevPSHostDescr,
       "nbsDevPSHostPSNumber": nbsDevPSHostPSNumber,
       "nbsDevPSHostFirstPS": nbsDevPSHostFirstPS,
       "nbsDevPSHostOperStatus": nbsDevPSHostOperStatus,
       "nbsDevPSHostAdminStatus": nbsDevPSHostAdminStatus,
       "nbsDevTemperatureProfile": nbsDevTemperatureProfile,
       "nbsDevTrapVars": nbsDevTrapVars,
       "nbsDevSessionType": nbsDevSessionType,
       "nbsDevAuthenticationRejectReason": nbsDevAuthenticationRejectReason,
       "nbsTrapLoginName": nbsTrapLoginName,
       "nbsTrapHostIpAddress": nbsTrapHostIpAddress,
       "nbsTrapWrongAccessDateTime": nbsTrapWrongAccessDateTime,
       "nbsTrapRCMredundancyState": nbsTrapRCMredundancyState,
       "nbsDevSNMPAccessMode": nbsDevSNMPAccessMode,
       "nbsDeviceTrapReason": nbsDeviceTrapReason,
       "nbsDeviceTrapAdminPasswdChangeDescripton": nbsDeviceTrapAdminPasswdChangeDescripton}
)
