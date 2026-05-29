# SNMP MIB module (A3COM0352-STACK-CONFIG) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\3com\A3COM0352-STACK-CONFIG

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

(superStackIIconfig,) = mibBuilder.importSymbols(
    "A3COM0004-GENERIC",
    "superStackIIconfig")

(a3Com,) = mibBuilder.importSymbols(
    "A3Com-products-MIB",
    "a3Com")

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

_StackConfiguration_ObjectIdentity = ObjectIdentity
stackConfiguration = _StackConfiguration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 10, 27, 1)
)
_StackConfigTable_Object = MibTable
stackConfigTable = _StackConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 27, 1, 1)
)
if mibBuilder.loadTexts:
    stackConfigTable.setStatus("mandatory")
_StackConfigEntry_Object = MibTableRow
stackConfigEntry = _StackConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 27, 1, 1, 1)
)
stackConfigEntry.setIndexNames(
    (0, "A3COM0352-STACK-CONFIG", "stackUnitLocation"),
)
if mibBuilder.loadTexts:
    stackConfigEntry.setStatus("mandatory")
_StackUnitLocation_Type = Integer32
_StackUnitLocation_Object = MibTableColumn
stackUnitLocation = _StackUnitLocation_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 27, 1, 1, 1, 1),
    _StackUnitLocation_Type()
)
stackUnitLocation.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    stackUnitLocation.setStatus("mandatory")
_StackUnitAddress_Type = PhysAddress
_StackUnitAddress_Object = MibTableColumn
stackUnitAddress = _StackUnitAddress_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 27, 1, 1, 1, 2),
    _StackUnitAddress_Type()
)
stackUnitAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stackUnitAddress.setStatus("mandatory")
_StackUnitLastReset_Type = TimeTicks
_StackUnitLastReset_Object = MibTableColumn
stackUnitLastReset = _StackUnitLastReset_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 27, 1, 1, 1, 3),
    _StackUnitLastReset_Type()
)
stackUnitLastReset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stackUnitLastReset.setStatus("mandatory")
_StackUnitType_Type = Integer32
_StackUnitType_Object = MibTableColumn
stackUnitType = _StackUnitType_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 27, 1, 1, 1, 4),
    _StackUnitType_Type()
)
stackUnitType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stackUnitType.setStatus("mandatory")
_StackUnitDesc_Type = DisplayString
_StackUnitDesc_Object = MibTableColumn
stackUnitDesc = _StackUnitDesc_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 27, 1, 1, 1, 5),
    _StackUnitDesc_Type()
)
stackUnitDesc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stackUnitDesc.setStatus("mandatory")


class _StackUnitName_Type(DisplayString):
    """Custom type stackUnitName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 30),
    )


_StackUnitName_Type.__name__ = "DisplayString"
_StackUnitName_Object = MibTableColumn
stackUnitName = _StackUnitName_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 27, 1, 1, 1, 6),
    _StackUnitName_Type()
)
stackUnitName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    stackUnitName.setStatus("mandatory")


class _StackUnitState_Type(Integer32):
    """Custom type stackUnitState based on Integer32"""
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
        *(("unitStateUnknown", 1),
          ("unitInactive", 2),
          ("unitOperational", 3),
          ("unitLoading", 4),
          ("unitAwaitReset", 5))
    )


_StackUnitState_Type.__name__ = "Integer32"
_StackUnitState_Object = MibTableColumn
stackUnitState = _StackUnitState_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 27, 1, 1, 1, 7),
    _StackUnitState_Type()
)
stackUnitState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stackUnitState.setStatus("mandatory")


class _StackUnitManagementType_Type(Integer32):
    """Custom type stackUnitManagementType based on Integer32"""
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
          ("distributed", 2),
          ("intelligent", 3))
    )


_StackUnitManagementType_Type.__name__ = "Integer32"
_StackUnitManagementType_Object = MibTableColumn
stackUnitManagementType = _StackUnitManagementType_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 27, 1, 1, 1, 8),
    _StackUnitManagementType_Type()
)
stackUnitManagementType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stackUnitManagementType.setStatus("mandatory")
_StackUnitCapabilities_Type = OctetString
_StackUnitCapabilities_Object = MibTableColumn
stackUnitCapabilities = _StackUnitCapabilities_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 27, 1, 1, 1, 9),
    _StackUnitCapabilities_Type()
)
stackUnitCapabilities.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stackUnitCapabilities.setStatus("mandatory")
_StackUnitPromVersion_Type = DisplayString
_StackUnitPromVersion_Object = MibTableColumn
stackUnitPromVersion = _StackUnitPromVersion_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 27, 1, 1, 1, 10),
    _StackUnitPromVersion_Type()
)
stackUnitPromVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stackUnitPromVersion.setStatus("mandatory")
_StackUnitHWVersion_Type = DisplayString
_StackUnitHWVersion_Object = MibTableColumn
stackUnitHWVersion = _StackUnitHWVersion_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 27, 1, 1, 1, 11),
    _StackUnitHWVersion_Type()
)
stackUnitHWVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stackUnitHWVersion.setStatus("mandatory")
_StackUnitSWVersion_Type = DisplayString
_StackUnitSWVersion_Object = MibTableColumn
stackUnitSWVersion = _StackUnitSWVersion_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 27, 1, 1, 1, 12),
    _StackUnitSWVersion_Type()
)
stackUnitSWVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stackUnitSWVersion.setStatus("mandatory")
_StackUnitSerialNumber_Type = DisplayString
_StackUnitSerialNumber_Object = MibTableColumn
stackUnitSerialNumber = _StackUnitSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 27, 1, 1, 1, 13),
    _StackUnitSerialNumber_Type()
)
stackUnitSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stackUnitSerialNumber.setStatus("mandatory")


class _StackUnitAttention_Type(Integer32):
    """Custom type stackUnitAttention based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noAttention", 1),
          ("attention", 2))
    )


_StackUnitAttention_Type.__name__ = "Integer32"
_StackUnitAttention_Object = MibTableColumn
stackUnitAttention = _StackUnitAttention_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 27, 1, 1, 1, 14),
    _StackUnitAttention_Type()
)
stackUnitAttention.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    stackUnitAttention.setStatus("mandatory")


class _StackUnitMgmtInterface_Type(Integer32):
    """Custom type stackUnitMgmtInterface based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_StackUnitMgmtInterface_Type.__name__ = "Integer32"
_StackUnitMgmtInterface_Object = MibTableColumn
stackUnitMgmtInterface = _StackUnitMgmtInterface_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 27, 1, 1, 1, 15),
    _StackUnitMgmtInterface_Type()
)
stackUnitMgmtInterface.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stackUnitMgmtInterface.setStatus("mandatory")
_StackUnitSummary_Type = OctetString
_StackUnitSummary_Object = MibTableColumn
stackUnitSummary = _StackUnitSummary_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 27, 1, 1, 1, 16),
    _StackUnitSummary_Type()
)
stackUnitSummary.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stackUnitSummary.setStatus("mandatory")


class _StackUnitSlipMgmtInterface_Type(Integer32):
    """Custom type stackUnitSlipMgmtInterface based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_StackUnitSlipMgmtInterface_Type.__name__ = "Integer32"
_StackUnitSlipMgmtInterface_Object = MibTableColumn
stackUnitSlipMgmtInterface = _StackUnitSlipMgmtInterface_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 27, 1, 1, 1, 17),
    _StackUnitSlipMgmtInterface_Type()
)
stackUnitSlipMgmtInterface.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stackUnitSlipMgmtInterface.setStatus("mandatory")


class _StackUnitNotepad_Type(OctetString):
    """Custom type stackUnitNotepad based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 512),
    )


_StackUnitNotepad_Type.__name__ = "OctetString"
_StackUnitNotepad_Object = MibTableColumn
stackUnitNotepad = _StackUnitNotepad_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 27, 1, 1, 1, 18),
    _StackUnitNotepad_Type()
)
stackUnitNotepad.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    stackUnitNotepad.setStatus("mandatory")
_StackUnitProductNumber_Type = DisplayString
_StackUnitProductNumber_Object = MibTableColumn
stackUnitProductNumber = _StackUnitProductNumber_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 27, 1, 1, 1, 19),
    _StackUnitProductNumber_Type()
)
stackUnitProductNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stackUnitProductNumber.setStatus("mandatory")
_StackBankSwapTable_Object = MibTable
stackBankSwapTable = _StackBankSwapTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 27, 1, 2)
)
if mibBuilder.loadTexts:
    stackBankSwapTable.setStatus("mandatory")
_StackBankSwapEntry_Object = MibTableRow
stackBankSwapEntry = _StackBankSwapEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 27, 1, 2, 1)
)
stackBankSwapEntry.setIndexNames(
    (0, "A3COM0352-STACK-CONFIG", "stackUnitLocation"),
    (0, "A3COM0352-STACK-CONFIG", "stackBankSwapId"),
)
if mibBuilder.loadTexts:
    stackBankSwapEntry.setStatus("mandatory")
_StackBankSwapId_Type = Integer32
_StackBankSwapId_Object = MibTableColumn
stackBankSwapId = _StackBankSwapId_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 27, 1, 2, 1, 1),
    _StackBankSwapId_Type()
)
stackBankSwapId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    stackBankSwapId.setStatus("mandatory")
_StackBankSwapSWVersion_Type = DisplayString
_StackBankSwapSWVersion_Object = MibTableColumn
stackBankSwapSWVersion = _StackBankSwapSWVersion_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 27, 1, 2, 1, 2),
    _StackBankSwapSWVersion_Type()
)
stackBankSwapSWVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stackBankSwapSWVersion.setStatus("mandatory")


class _StackBankSwapStatus_Type(Integer32):
    """Custom type stackBankSwapStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("activeOnLoad", 2),
          ("inactiveOnLoad", 3))
    )


_StackBankSwapStatus_Type.__name__ = "Integer32"
_StackBankSwapStatus_Object = MibTableColumn
stackBankSwapStatus = _StackBankSwapStatus_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 27, 1, 2, 1, 3),
    _StackBankSwapStatus_Type()
)
stackBankSwapStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    stackBankSwapStatus.setStatus("mandatory")


class _StackBankSwapNextActive_Type(Integer32):
    """Custom type stackBankSwapNextActive based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("nextActive", 1),
          ("nextActivePostLoad", 2),
          ("notNextActive", 3))
    )


_StackBankSwapNextActive_Type.__name__ = "Integer32"
_StackBankSwapNextActive_Object = MibTableColumn
stackBankSwapNextActive = _StackBankSwapNextActive_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 27, 1, 2, 1, 4),
    _StackBankSwapNextActive_Type()
)
stackBankSwapNextActive.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    stackBankSwapNextActive.setStatus("mandatory")
_StackAddressInformation_ObjectIdentity = ObjectIdentity
stackAddressInformation = _StackAddressInformation_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 10, 27, 2)
)
_StackAddressTable_Object = MibTable
stackAddressTable = _StackAddressTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 27, 2, 1)
)
if mibBuilder.loadTexts:
    stackAddressTable.setStatus("mandatory")
_StackAddressEntry_Object = MibTableRow
stackAddressEntry = _StackAddressEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 27, 2, 1, 1)
)
stackAddressEntry.setIndexNames(
    (0, "A3COM0352-STACK-CONFIG", "stackUnitLocation"),
    (0, "A3COM0352-STACK-CONFIG", "stackAddressNumber"),
)
if mibBuilder.loadTexts:
    stackAddressEntry.setStatus("mandatory")
_StackAddressNumber_Type = Integer32
_StackAddressNumber_Object = MibTableColumn
stackAddressNumber = _StackAddressNumber_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 27, 2, 1, 1, 1),
    _StackAddressNumber_Type()
)
stackAddressNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stackAddressNumber.setStatus("mandatory")


class _StackAddressType_Type(Integer32):
    """Custom type stackAddressType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ipAddress", 1),
          ("ipxAddress", 2))
    )


_StackAddressType_Type.__name__ = "Integer32"
_StackAddressType_Object = MibTableColumn
stackAddressType = _StackAddressType_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 27, 2, 1, 1, 2),
    _StackAddressType_Type()
)
stackAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stackAddressType.setStatus("mandatory")
_StackAddress_Type = OctetString
_StackAddress_Object = MibTableColumn
stackAddress = _StackAddress_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 27, 2, 1, 1, 3),
    _StackAddress_Type()
)
stackAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stackAddress.setStatus("mandatory")
_StackSysObjIdentities_ObjectIdentity = ObjectIdentity
stackSysObjIdentities = _StackSysObjIdentities_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 10, 27, 4)
)
_StackUnitTypes_ObjectIdentity = ObjectIdentity
stackUnitTypes = _StackUnitTypes_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 10, 27, 5)
)

# Managed Objects groups


# Notification objects

unitDeparture = NotificationType(
    (1, 3, 6, 1, 4, 1, 43, 0, 89)
)
unitDeparture.setObjects(
      *(("A3COM0352-STACK-CONFIG", "stackUnitDesc"),
        ("A3COM0352-STACK-CONFIG", "stackUnitSerialNumber"))
)
if mibBuilder.loadTexts:
    unitDeparture.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "A3COM0352-STACK-CONFIG",
    **{"unitDeparture": unitDeparture,
       "stackConfiguration": stackConfiguration,
       "stackConfigTable": stackConfigTable,
       "stackConfigEntry": stackConfigEntry,
       "stackUnitLocation": stackUnitLocation,
       "stackUnitAddress": stackUnitAddress,
       "stackUnitLastReset": stackUnitLastReset,
       "stackUnitType": stackUnitType,
       "stackUnitDesc": stackUnitDesc,
       "stackUnitName": stackUnitName,
       "stackUnitState": stackUnitState,
       "stackUnitManagementType": stackUnitManagementType,
       "stackUnitCapabilities": stackUnitCapabilities,
       "stackUnitPromVersion": stackUnitPromVersion,
       "stackUnitHWVersion": stackUnitHWVersion,
       "stackUnitSWVersion": stackUnitSWVersion,
       "stackUnitSerialNumber": stackUnitSerialNumber,
       "stackUnitAttention": stackUnitAttention,
       "stackUnitMgmtInterface": stackUnitMgmtInterface,
       "stackUnitSummary": stackUnitSummary,
       "stackUnitSlipMgmtInterface": stackUnitSlipMgmtInterface,
       "stackUnitNotepad": stackUnitNotepad,
       "stackUnitProductNumber": stackUnitProductNumber,
       "stackBankSwapTable": stackBankSwapTable,
       "stackBankSwapEntry": stackBankSwapEntry,
       "stackBankSwapId": stackBankSwapId,
       "stackBankSwapSWVersion": stackBankSwapSWVersion,
       "stackBankSwapStatus": stackBankSwapStatus,
       "stackBankSwapNextActive": stackBankSwapNextActive,
       "stackAddressInformation": stackAddressInformation,
       "stackAddressTable": stackAddressTable,
       "stackAddressEntry": stackAddressEntry,
       "stackAddressNumber": stackAddressNumber,
       "stackAddressType": stackAddressType,
       "stackAddress": stackAddress,
       "stackSysObjIdentities": stackSysObjIdentities,
       "stackUnitTypes": stackUnitTypes}
)
