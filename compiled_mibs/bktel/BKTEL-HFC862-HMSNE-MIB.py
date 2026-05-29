# SNMP MIB module (BKTEL-HFC862-HMSNE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\bktel\BKTEL-HFC862-HMSNE-MIB

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

(DisplayString,
 NESlotValue,
 PerceivedSeverityValue,
 TruthValue,
 ne) = mibBuilder.importSymbols(
    "BKTEL-HFC862-BASE-MIB",
    "DisplayString",
    "NESlotValue",
    "PerceivedSeverityValue",
    "TruthValue",
    "ne")

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

_NeCommon_ObjectIdentity = ObjectIdentity
neCommon = _NeCommon_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7501, 1, 1, 1)
)
_NeType_Type = DisplayString
_NeType_Object = MibScalar
neType = _NeType_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 1, 1, 1),
    _NeType_Type()
)
neType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    neType.setStatus("mandatory")
_NeDescription_Type = DisplayString
_NeDescription_Object = MibScalar
neDescription = _NeDescription_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 1, 1, 2),
    _NeDescription_Type()
)
neDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    neDescription.setStatus("mandatory")
_NeLocationStreet_Type = DisplayString
_NeLocationStreet_Object = MibScalar
neLocationStreet = _NeLocationStreet_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 1, 1, 3),
    _NeLocationStreet_Type()
)
neLocationStreet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    neLocationStreet.setStatus("mandatory")
_NeLocationCity_Type = DisplayString
_NeLocationCity_Object = MibScalar
neLocationCity = _NeLocationCity_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 1, 1, 4),
    _NeLocationCity_Type()
)
neLocationCity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    neLocationCity.setStatus("mandatory")
_NeObsolete_UsingAPS_Type = TruthValue
_NeObsolete_UsingAPS_Object = MibScalar
neObsolete_UsingAPS = _NeObsolete_UsingAPS_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 1, 1, 5),
    _NeObsolete_UsingAPS_Type()
)
neObsolete_UsingAPS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    neObsolete_UsingAPS.setStatus("obsolete")
_NeObsolete_APSMode_Type = Integer32
_NeObsolete_APSMode_Object = MibScalar
neObsolete_APSMode = _NeObsolete_APSMode_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 1, 1, 6),
    _NeObsolete_APSMode_Type()
)
neObsolete_APSMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    neObsolete_APSMode.setStatus("obsolete")
_NeObsolete_CommonSubrackWidth_Type = Integer32
_NeObsolete_CommonSubrackWidth_Object = MibScalar
neObsolete_CommonSubrackWidth = _NeObsolete_CommonSubrackWidth_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 1, 1, 8),
    _NeObsolete_CommonSubrackWidth_Type()
)
neObsolete_CommonSubrackWidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    neObsolete_CommonSubrackWidth.setStatus("obsolete")
_NeObsolete_CommonSubrackNumber_Type = Integer32
_NeObsolete_CommonSubrackNumber_Object = MibScalar
neObsolete_CommonSubrackNumber = _NeObsolete_CommonSubrackNumber_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 1, 1, 9),
    _NeObsolete_CommonSubrackNumber_Type()
)
neObsolete_CommonSubrackNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    neObsolete_CommonSubrackNumber.setStatus("obsolete")


class _NeObsolete_NumberModul_Type(Integer32):
    """Custom type neObsolete_NumberModul based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 61),
    )


_NeObsolete_NumberModul_Type.__name__ = "Integer32"
_NeObsolete_NumberModul_Object = MibScalar
neObsolete_NumberModul = _NeObsolete_NumberModul_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 1, 1, 10),
    _NeObsolete_NumberModul_Type()
)
neObsolete_NumberModul.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    neObsolete_NumberModul.setStatus("obsolete")
_NeObsolete_UsingRevertiveMode_Type = TruthValue
_NeObsolete_UsingRevertiveMode_Object = MibScalar
neObsolete_UsingRevertiveMode = _NeObsolete_UsingRevertiveMode_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 1, 1, 11),
    _NeObsolete_UsingRevertiveMode_Type()
)
neObsolete_UsingRevertiveMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    neObsolete_UsingRevertiveMode.setStatus("obsolete")


class _NeObsolete_RevertiveMode_Type(Integer32):
    """Custom type neObsolete_RevertiveMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 300),
    )


_NeObsolete_RevertiveMode_Type.__name__ = "Integer32"
_NeObsolete_RevertiveMode_Object = MibScalar
neObsolete_RevertiveMode = _NeObsolete_RevertiveMode_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 1, 1, 12),
    _NeObsolete_RevertiveMode_Type()
)
neObsolete_RevertiveMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    neObsolete_RevertiveMode.setStatus("obsolete")
_NeObsolete_InitPhase_Type = Integer32
_NeObsolete_InitPhase_Object = MibScalar
neObsolete_InitPhase = _NeObsolete_InitPhase_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 1, 1, 13),
    _NeObsolete_InitPhase_Type()
)
neObsolete_InitPhase.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    neObsolete_InitPhase.setStatus("obsolete")
_NeObsolete_PredecessorRedundantPath_Type = IpAddress
_NeObsolete_PredecessorRedundantPath_Object = MibScalar
neObsolete_PredecessorRedundantPath = _NeObsolete_PredecessorRedundantPath_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 1, 1, 14),
    _NeObsolete_PredecessorRedundantPath_Type()
)
neObsolete_PredecessorRedundantPath.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    neObsolete_PredecessorRedundantPath.setStatus("obsolete")
_NeObsolete_PredecessorNominalPath_Type = IpAddress
_NeObsolete_PredecessorNominalPath_Object = MibScalar
neObsolete_PredecessorNominalPath = _NeObsolete_PredecessorNominalPath_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 1, 1, 15),
    _NeObsolete_PredecessorNominalPath_Type()
)
neObsolete_PredecessorNominalPath.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    neObsolete_PredecessorNominalPath.setStatus("obsolete")
_NeModuleTable_Object = MibTable
neModuleTable = _NeModuleTable_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 1, 1, 16)
)
if mibBuilder.loadTexts:
    neModuleTable.setStatus("mandatory")
_NeModuleEntry_Object = MibTableRow
neModuleEntry = _NeModuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 1, 1, 16, 1)
)
neModuleEntry.setIndexNames(
    (0, "BKTEL-HFC862-HMSNE-MIB", "neModuleNESlot"),
)
if mibBuilder.loadTexts:
    neModuleEntry.setStatus("mandatory")
_NeModuleNESlot_Type = NESlotValue
_NeModuleNESlot_Object = MibTableColumn
neModuleNESlot = _NeModuleNESlot_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 1, 1, 16, 1, 1),
    _NeModuleNESlot_Type()
)
neModuleNESlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    neModuleNESlot.setStatus("mandatory")
_NeModuleSubrack_Type = Integer32
_NeModuleSubrack_Object = MibTableColumn
neModuleSubrack = _NeModuleSubrack_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 1, 1, 16, 1, 2),
    _NeModuleSubrack_Type()
)
neModuleSubrack.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    neModuleSubrack.setStatus("mandatory")
_NeModuleModelName_Type = DisplayString
_NeModuleModelName_Object = MibTableColumn
neModuleModelName = _NeModuleModelName_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 1, 1, 16, 1, 3),
    _NeModuleModelName_Type()
)
neModuleModelName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    neModuleModelName.setStatus("mandatory")
_NeModuleMibLink_Type = ObjectIdentifier
_NeModuleMibLink_Object = MibTableColumn
neModuleMibLink = _NeModuleMibLink_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 1, 1, 16, 1, 4),
    _NeModuleMibLink_Type()
)
neModuleMibLink.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    neModuleMibLink.setStatus("mandatory")
_NeModuleSubrackSlot_Type = Integer32
_NeModuleSubrackSlot_Object = MibTableColumn
neModuleSubrackSlot = _NeModuleSubrackSlot_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 1, 1, 16, 1, 5),
    _NeModuleSubrackSlot_Type()
)
neModuleSubrackSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    neModuleSubrackSlot.setStatus("mandatory")
_NeModuleSlotUnitsUsed_Type = Integer32
_NeModuleSlotUnitsUsed_Object = MibTableColumn
neModuleSlotUnitsUsed = _NeModuleSlotUnitsUsed_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 1, 1, 16, 1, 6),
    _NeModuleSlotUnitsUsed_Type()
)
neModuleSlotUnitsUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    neModuleSlotUnitsUsed.setStatus("mandatory")


class _NeModuleSlotRackDetection_Type(Integer32):
    """Custom type neModuleSlotRackDetection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("notSupported", 1),
          ("supported", 2),
          ("detectionError", 3))
    )


_NeModuleSlotRackDetection_Type.__name__ = "Integer32"
_NeModuleSlotRackDetection_Object = MibTableColumn
neModuleSlotRackDetection = _NeModuleSlotRackDetection_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 1, 1, 16, 1, 7),
    _NeModuleSlotRackDetection_Type()
)
neModuleSlotRackDetection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    neModuleSlotRackDetection.setStatus("mandatory")


class _NeModuleHousingType_Type(Integer32):
    """Custom type neModuleHousingType based on Integer32"""
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
        *(("housingUnknownOrDefault", 1),
          ("housingBk", 2),
          ("housing2G6", 3),
          ("housing19inch", 4))
    )


_NeModuleHousingType_Type.__name__ = "Integer32"
_NeModuleHousingType_Object = MibTableColumn
neModuleHousingType = _NeModuleHousingType_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 1, 1, 16, 1, 8),
    _NeModuleHousingType_Type()
)
neModuleHousingType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    neModuleHousingType.setStatus("mandatory")
_NeModuleFirmwareVersion_Type = DisplayString
_NeModuleFirmwareVersion_Object = MibTableColumn
neModuleFirmwareVersion = _NeModuleFirmwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 1, 1, 16, 1, 9),
    _NeModuleFirmwareVersion_Type()
)
neModuleFirmwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    neModuleFirmwareVersion.setStatus("mandatory")
_NeModuleHardwareVersion_Type = DisplayString
_NeModuleHardwareVersion_Object = MibTableColumn
neModuleHardwareVersion = _NeModuleHardwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 1, 1, 16, 1, 10),
    _NeModuleHardwareVersion_Type()
)
neModuleHardwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    neModuleHardwareVersion.setStatus("mandatory")
_NeModuleDateOfProduction_Type = DisplayString
_NeModuleDateOfProduction_Object = MibTableColumn
neModuleDateOfProduction = _NeModuleDateOfProduction_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 1, 1, 16, 1, 11),
    _NeModuleDateOfProduction_Type()
)
neModuleDateOfProduction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    neModuleDateOfProduction.setStatus("mandatory")
_NeModuleSerialNumber_Type = DisplayString
_NeModuleSerialNumber_Object = MibTableColumn
neModuleSerialNumber = _NeModuleSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 1, 1, 16, 1, 12),
    _NeModuleSerialNumber_Type()
)
neModuleSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    neModuleSerialNumber.setStatus("mandatory")
_NeModuleArticleNumber_Type = DisplayString
_NeModuleArticleNumber_Object = MibTableColumn
neModuleArticleNumber = _NeModuleArticleNumber_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 1, 1, 16, 1, 13),
    _NeModuleArticleNumber_Type()
)
neModuleArticleNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    neModuleArticleNumber.setStatus("mandatory")
_NeModuleCustomerCode_Type = DisplayString
_NeModuleCustomerCode_Object = MibTableColumn
neModuleCustomerCode = _NeModuleCustomerCode_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 1, 1, 16, 1, 14),
    _NeModuleCustomerCode_Type()
)
neModuleCustomerCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    neModuleCustomerCode.setStatus("mandatory")
_NeModuleAliasName_Type = DisplayString
_NeModuleAliasName_Object = MibTableColumn
neModuleAliasName = _NeModuleAliasName_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 1, 1, 16, 1, 15),
    _NeModuleAliasName_Type()
)
neModuleAliasName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    neModuleAliasName.setStatus("mandatory")
_NeModuleUserdata_Type = DisplayString
_NeModuleUserdata_Object = MibTableColumn
neModuleUserdata = _NeModuleUserdata_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 1, 1, 16, 1, 16),
    _NeModuleUserdata_Type()
)
neModuleUserdata.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    neModuleUserdata.setStatus("mandatory")
_NeModuleReset_Type = TruthValue
_NeModuleReset_Object = MibTableColumn
neModuleReset = _NeModuleReset_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 1, 1, 16, 1, 17),
    _NeModuleReset_Type()
)
neModuleReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    neModuleReset.setStatus("mandatory")
_NeModuleLedBlink_Type = TruthValue
_NeModuleLedBlink_Object = MibTableColumn
neModuleLedBlink = _NeModuleLedBlink_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 1, 1, 16, 1, 18),
    _NeModuleLedBlink_Type()
)
neModuleLedBlink.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    neModuleLedBlink.setStatus("mandatory")
_NeStates_ObjectIdentity = ObjectIdentity
neStates = _NeStates_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7501, 1, 1, 2)
)
_NeStatesObsolete_TrapDisable_Type = PerceivedSeverityValue
_NeStatesObsolete_TrapDisable_Object = MibScalar
neStatesObsolete_TrapDisable = _NeStatesObsolete_TrapDisable_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 1, 2, 1),
    _NeStatesObsolete_TrapDisable_Type()
)
neStatesObsolete_TrapDisable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    neStatesObsolete_TrapDisable.setStatus("obsolete")
_NeStatesObsolete_TerminalConnected_Type = PerceivedSeverityValue
_NeStatesObsolete_TerminalConnected_Object = MibScalar
neStatesObsolete_TerminalConnected = _NeStatesObsolete_TerminalConnected_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 1, 2, 2),
    _NeStatesObsolete_TerminalConnected_Type()
)
neStatesObsolete_TerminalConnected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    neStatesObsolete_TerminalConnected.setStatus("obsolete")
_NeStatesObsolete_Isolated_Type = PerceivedSeverityValue
_NeStatesObsolete_Isolated_Object = MibScalar
neStatesObsolete_Isolated = _NeStatesObsolete_Isolated_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 1, 2, 4),
    _NeStatesObsolete_Isolated_Type()
)
neStatesObsolete_Isolated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    neStatesObsolete_Isolated.setStatus("obsolete")
_NeStatesObsolete_ResetModullist_Type = PerceivedSeverityValue
_NeStatesObsolete_ResetModullist_Object = MibScalar
neStatesObsolete_ResetModullist = _NeStatesObsolete_ResetModullist_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 1, 2, 5),
    _NeStatesObsolete_ResetModullist_Type()
)
neStatesObsolete_ResetModullist.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    neStatesObsolete_ResetModullist.setStatus("obsolete")
_NeStatesObsolete_Redundant_Type = PerceivedSeverityValue
_NeStatesObsolete_Redundant_Object = MibScalar
neStatesObsolete_Redundant = _NeStatesObsolete_Redundant_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 1, 2, 6),
    _NeStatesObsolete_Redundant_Type()
)
neStatesObsolete_Redundant.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    neStatesObsolete_Redundant.setStatus("obsolete")
_NeStatesObsolete_ActivateRedundantPath_Type = PerceivedSeverityValue
_NeStatesObsolete_ActivateRedundantPath_Object = MibScalar
neStatesObsolete_ActivateRedundantPath = _NeStatesObsolete_ActivateRedundantPath_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 1, 2, 7),
    _NeStatesObsolete_ActivateRedundantPath_Type()
)
neStatesObsolete_ActivateRedundantPath.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    neStatesObsolete_ActivateRedundantPath.setStatus("obsolete")
_NeStatesObsolete_AutoOff_Type = PerceivedSeverityValue
_NeStatesObsolete_AutoOff_Object = MibScalar
neStatesObsolete_AutoOff = _NeStatesObsolete_AutoOff_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 1, 2, 8),
    _NeStatesObsolete_AutoOff_Type()
)
neStatesObsolete_AutoOff.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    neStatesObsolete_AutoOff.setStatus("obsolete")
_NeConfig_ObjectIdentity = ObjectIdentity
neConfig = _NeConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7501, 1, 1, 3)
)
_NeConfigObsolete_NEtype_Type = Integer32
_NeConfigObsolete_NEtype_Object = MibScalar
neConfigObsolete_NEtype = _NeConfigObsolete_NEtype_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 1, 3, 1),
    _NeConfigObsolete_NEtype_Type()
)
neConfigObsolete_NEtype.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    neConfigObsolete_NEtype.setStatus("obsolete")
_NeConfigObsolete_IPaddress_Type = IpAddress
_NeConfigObsolete_IPaddress_Object = MibScalar
neConfigObsolete_IPaddress = _NeConfigObsolete_IPaddress_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 1, 3, 2),
    _NeConfigObsolete_IPaddress_Type()
)
neConfigObsolete_IPaddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    neConfigObsolete_IPaddress.setStatus("obsolete")


class _NeConfigObsolete_Alarmdelay_Type(Integer32):
    """Custom type neConfigObsolete_Alarmdelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(3, 60),
    )


_NeConfigObsolete_Alarmdelay_Type.__name__ = "Integer32"
_NeConfigObsolete_Alarmdelay_Object = MibScalar
neConfigObsolete_Alarmdelay = _NeConfigObsolete_Alarmdelay_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 1, 3, 3),
    _NeConfigObsolete_Alarmdelay_Type()
)
neConfigObsolete_Alarmdelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    neConfigObsolete_Alarmdelay.setStatus("obsolete")


class _NeConfigDeprecated_MinTrapInterval_Type(Integer32):
    """Custom type neConfigDeprecated_MinTrapInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10),
    )


_NeConfigDeprecated_MinTrapInterval_Type.__name__ = "Integer32"
_NeConfigDeprecated_MinTrapInterval_Object = MibScalar
neConfigDeprecated_MinTrapInterval = _NeConfigDeprecated_MinTrapInterval_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 1, 3, 4),
    _NeConfigDeprecated_MinTrapInterval_Type()
)
neConfigDeprecated_MinTrapInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    neConfigDeprecated_MinTrapInterval.setStatus("optional")


class _NeConfigDeprecated_MaxTrapLifetime_Type(Integer32):
    """Custom type neConfigDeprecated_MaxTrapLifetime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(30, 300),
    )


_NeConfigDeprecated_MaxTrapLifetime_Type.__name__ = "Integer32"
_NeConfigDeprecated_MaxTrapLifetime_Object = MibScalar
neConfigDeprecated_MaxTrapLifetime = _NeConfigDeprecated_MaxTrapLifetime_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 1, 3, 5),
    _NeConfigDeprecated_MaxTrapLifetime_Type()
)
neConfigDeprecated_MaxTrapLifetime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    neConfigDeprecated_MaxTrapLifetime.setStatus("optional")
_NeControl_ObjectIdentity = ObjectIdentity
neControl = _NeControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7501, 1, 1, 4)
)
_NeControlTrapDisable_Type = TruthValue
_NeControlTrapDisable_Object = MibScalar
neControlTrapDisable = _NeControlTrapDisable_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 1, 4, 1),
    _NeControlTrapDisable_Type()
)
neControlTrapDisable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    neControlTrapDisable.setStatus("mandatory")
_NeControlResetModullist_Type = TruthValue
_NeControlResetModullist_Object = MibScalar
neControlResetModullist = _NeControlResetModullist_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 1, 4, 2),
    _NeControlResetModullist_Type()
)
neControlResetModullist.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    neControlResetModullist.setStatus("mandatory")
_NeControlObsolete_SetDefaultAPS_Type = TruthValue
_NeControlObsolete_SetDefaultAPS_Object = MibScalar
neControlObsolete_SetDefaultAPS = _NeControlObsolete_SetDefaultAPS_Object(
    (1, 3, 6, 1, 4, 1, 7501, 1, 1, 4, 3),
    _NeControlObsolete_SetDefaultAPS_Type()
)
neControlObsolete_SetDefaultAPS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    neControlObsolete_SetDefaultAPS.setStatus("obsolete")

# Managed Objects groups


# Notification objects

neSynchronizeEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 7501, 1, 1, 0, 1)
)
if mibBuilder.loadTexts:
    neSynchronizeEvent.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "BKTEL-HFC862-HMSNE-MIB",
    **{"neSynchronizeEvent": neSynchronizeEvent,
       "neCommon": neCommon,
       "neType": neType,
       "neDescription": neDescription,
       "neLocationStreet": neLocationStreet,
       "neLocationCity": neLocationCity,
       "neObsolete_UsingAPS": neObsolete_UsingAPS,
       "neObsolete_APSMode": neObsolete_APSMode,
       "neObsolete_CommonSubrackWidth": neObsolete_CommonSubrackWidth,
       "neObsolete_CommonSubrackNumber": neObsolete_CommonSubrackNumber,
       "neObsolete_NumberModul": neObsolete_NumberModul,
       "neObsolete_UsingRevertiveMode": neObsolete_UsingRevertiveMode,
       "neObsolete_RevertiveMode": neObsolete_RevertiveMode,
       "neObsolete_InitPhase": neObsolete_InitPhase,
       "neObsolete_PredecessorRedundantPath": neObsolete_PredecessorRedundantPath,
       "neObsolete_PredecessorNominalPath": neObsolete_PredecessorNominalPath,
       "neModuleTable": neModuleTable,
       "neModuleEntry": neModuleEntry,
       "neModuleNESlot": neModuleNESlot,
       "neModuleSubrack": neModuleSubrack,
       "neModuleModelName": neModuleModelName,
       "neModuleMibLink": neModuleMibLink,
       "neModuleSubrackSlot": neModuleSubrackSlot,
       "neModuleSlotUnitsUsed": neModuleSlotUnitsUsed,
       "neModuleSlotRackDetection": neModuleSlotRackDetection,
       "neModuleHousingType": neModuleHousingType,
       "neModuleFirmwareVersion": neModuleFirmwareVersion,
       "neModuleHardwareVersion": neModuleHardwareVersion,
       "neModuleDateOfProduction": neModuleDateOfProduction,
       "neModuleSerialNumber": neModuleSerialNumber,
       "neModuleArticleNumber": neModuleArticleNumber,
       "neModuleCustomerCode": neModuleCustomerCode,
       "neModuleAliasName": neModuleAliasName,
       "neModuleUserdata": neModuleUserdata,
       "neModuleReset": neModuleReset,
       "neModuleLedBlink": neModuleLedBlink,
       "neStates": neStates,
       "neStatesObsolete_TrapDisable": neStatesObsolete_TrapDisable,
       "neStatesObsolete_TerminalConnected": neStatesObsolete_TerminalConnected,
       "neStatesObsolete_Isolated": neStatesObsolete_Isolated,
       "neStatesObsolete_ResetModullist": neStatesObsolete_ResetModullist,
       "neStatesObsolete_Redundant": neStatesObsolete_Redundant,
       "neStatesObsolete_ActivateRedundantPath": neStatesObsolete_ActivateRedundantPath,
       "neStatesObsolete_AutoOff": neStatesObsolete_AutoOff,
       "neConfig": neConfig,
       "neConfigObsolete_NEtype": neConfigObsolete_NEtype,
       "neConfigObsolete_IPaddress": neConfigObsolete_IPaddress,
       "neConfigObsolete_Alarmdelay": neConfigObsolete_Alarmdelay,
       "neConfigDeprecated_MinTrapInterval": neConfigDeprecated_MinTrapInterval,
       "neConfigDeprecated_MaxTrapLifetime": neConfigDeprecated_MaxTrapLifetime,
       "neControl": neControl,
       "neControlTrapDisable": neControlTrapDisable,
       "neControlResetModullist": neControlResetModullist,
       "neControlObsolete_SetDefaultAPS": neControlObsolete_SetDefaultAPS}
)
