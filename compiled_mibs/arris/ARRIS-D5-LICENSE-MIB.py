# SNMP MIB module (ARRIS-D5-LICENSE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\arris\d5\ARRIS-D5-LICENSE-MIB

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

(arrisD5UEQam,) = mibBuilder.importSymbols(
    "ARRIS-MIB",
    "arrisD5UEQam")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

d5LicenseMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4115, 1, 8, 1, 22)
)
if mibBuilder.loadTexts:
    d5LicenseMib.setRevisions(
        ("2009-05-14 08:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class D5LicenseType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("qamQuadToHex", 1),
          ("qamHexToOctal", 2),
          ("qamQuadToOctal", 3))
    )



class D5EncryptionKeyType(TextualConvention, OctetString):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 150),
    )



class D5EncryptedType(TextualConvention, OctetString):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )



# MIB Managed Objects in the order of their OIDs

_D5LicenseTrapDelay_Type = D5EncryptedType
_D5LicenseTrapDelay_Object = MibScalar
d5LicenseTrapDelay = _D5LicenseTrapDelay_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 8, 1, 22, 1, 1),
    _D5LicenseTrapDelay_Type()
)
d5LicenseTrapDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    d5LicenseTrapDelay.setStatus("current")
_D5LicenseTrapResendRate_Type = D5EncryptedType
_D5LicenseTrapResendRate_Object = MibScalar
d5LicenseTrapResendRate = _D5LicenseTrapResendRate_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 8, 1, 22, 1, 2),
    _D5LicenseTrapResendRate_Type()
)
d5LicenseTrapResendRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    d5LicenseTrapResendRate.setStatus("current")
_D5LicenseTimeToLive_Type = D5EncryptedType
_D5LicenseTimeToLive_Object = MibScalar
d5LicenseTimeToLive = _D5LicenseTimeToLive_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 8, 1, 22, 1, 3),
    _D5LicenseTimeToLive_Type()
)
d5LicenseTimeToLive.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    d5LicenseTimeToLive.setStatus("current")
_D5LicenseRemotePublicKey_Type = D5EncryptionKeyType
_D5LicenseRemotePublicKey_Object = MibScalar
d5LicenseRemotePublicKey = _D5LicenseRemotePublicKey_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 8, 1, 22, 1, 4),
    _D5LicenseRemotePublicKey_Type()
)
d5LicenseRemotePublicKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    d5LicenseRemotePublicKey.setStatus("current")
_D5LicenseLocalPublicKey_Type = D5EncryptionKeyType
_D5LicenseLocalPublicKey_Object = MibScalar
d5LicenseLocalPublicKey = _D5LicenseLocalPublicKey_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 8, 1, 22, 1, 5),
    _D5LicenseLocalPublicKey_Type()
)
d5LicenseLocalPublicKey.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    d5LicenseLocalPublicKey.setStatus("current")
_D5LicenseAllocationTable_Object = MibTable
d5LicenseAllocationTable = _D5LicenseAllocationTable_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 8, 1, 22, 2)
)
if mibBuilder.loadTexts:
    d5LicenseAllocationTable.setStatus("current")
_D5LicenseAllocationEntry_Object = MibTableRow
d5LicenseAllocationEntry = _D5LicenseAllocationEntry_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 8, 1, 22, 2, 1)
)
d5LicenseAllocationEntry.setIndexNames(
    (0, "ARRIS-D5-LICENSE-MIB", "d5LicenseAllocationType"),
)
if mibBuilder.loadTexts:
    d5LicenseAllocationEntry.setStatus("current")
_D5LicenseAllocationType_Type = D5LicenseType
_D5LicenseAllocationType_Object = MibTableColumn
d5LicenseAllocationType = _D5LicenseAllocationType_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 8, 1, 22, 2, 1, 1),
    _D5LicenseAllocationType_Type()
)
d5LicenseAllocationType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    d5LicenseAllocationType.setStatus("current")
_D5LicensesAllocated_Type = D5EncryptedType
_D5LicensesAllocated_Object = MibTableColumn
d5LicensesAllocated = _D5LicensesAllocated_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 8, 1, 22, 2, 1, 2),
    _D5LicensesAllocated_Type()
)
d5LicensesAllocated.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    d5LicensesAllocated.setStatus("current")
_D5LicensesInUse_Type = Unsigned32
_D5LicensesInUse_Object = MibTableColumn
d5LicensesInUse = _D5LicensesInUse_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 8, 1, 22, 2, 1, 3),
    _D5LicensesInUse_Type()
)
d5LicensesInUse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    d5LicensesInUse.setStatus("current")


class _D5LicMgrId_Type(OctetString):
    """Custom type d5LicMgrId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_D5LicMgrId_Type.__name__ = "OctetString"
_D5LicMgrId_Object = MibTableColumn
d5LicMgrId = _D5LicMgrId_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 8, 1, 22, 2, 1, 4),
    _D5LicMgrId_Type()
)
d5LicMgrId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    d5LicMgrId.setStatus("current")
_D5LicenseInUseTable_Object = MibTable
d5LicenseInUseTable = _D5LicenseInUseTable_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 8, 1, 22, 3)
)
if mibBuilder.loadTexts:
    d5LicenseInUseTable.setStatus("current")
_D5LicenseInUseEntry_Object = MibTableRow
d5LicenseInUseEntry = _D5LicenseInUseEntry_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 8, 1, 22, 3, 1)
)
d5LicenseInUseEntry.setIndexNames(
    (0, "ARRIS-D5-LICENSE-MIB", "d5LicenseInUseType"),
    (0, "ARRIS-D5-LICENSE-MIB", "d5LicenseIndex"),
)
if mibBuilder.loadTexts:
    d5LicenseInUseEntry.setStatus("current")
_D5LicenseInUseType_Type = D5LicenseType
_D5LicenseInUseType_Object = MibTableColumn
d5LicenseInUseType = _D5LicenseInUseType_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 8, 1, 22, 3, 1, 1),
    _D5LicenseInUseType_Type()
)
d5LicenseInUseType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    d5LicenseInUseType.setStatus("current")


class _D5LicenseIndex_Type(Unsigned32):
    """Custom type d5LicenseIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_D5LicenseIndex_Type.__name__ = "Unsigned32"
_D5LicenseIndex_Object = MibTableColumn
d5LicenseIndex = _D5LicenseIndex_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 8, 1, 22, 3, 1, 2),
    _D5LicenseIndex_Type()
)
d5LicenseIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    d5LicenseIndex.setStatus("current")
_D5LicenseRowStatus_Type = RowStatus
_D5LicenseRowStatus_Object = MibTableColumn
d5LicenseRowStatus = _D5LicenseRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 8, 1, 22, 3, 1, 3),
    _D5LicenseRowStatus_Type()
)
d5LicenseRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    d5LicenseRowStatus.setStatus("current")


class _D5LicenseInUseMgrId_Type(OctetString):
    """Custom type d5LicenseInUseMgrId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_D5LicenseInUseMgrId_Type.__name__ = "OctetString"
_D5LicenseInUseMgrId_Object = MibTableColumn
d5LicenseInUseMgrId = _D5LicenseInUseMgrId_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 8, 1, 22, 3, 1, 4),
    _D5LicenseInUseMgrId_Type()
)
d5LicenseInUseMgrId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    d5LicenseInUseMgrId.setStatus("current")
_D5LicMgrAllocationTable_Object = MibTable
d5LicMgrAllocationTable = _D5LicMgrAllocationTable_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 8, 1, 22, 4)
)
if mibBuilder.loadTexts:
    d5LicMgrAllocationTable.setStatus("current")
_D5LicMgrAllocationEntry_Object = MibTableRow
d5LicMgrAllocationEntry = _D5LicMgrAllocationEntry_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 8, 1, 22, 4, 1)
)
d5LicMgrAllocationEntry.setIndexNames(
    (0, "ARRIS-D5-LICENSE-MIB", "d5LicMgrIndex"),
)
if mibBuilder.loadTexts:
    d5LicMgrAllocationEntry.setStatus("current")


class _D5LicMgrIndex_Type(OctetString):
    """Custom type d5LicMgrIndex based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_D5LicMgrIndex_Type.__name__ = "OctetString"
_D5LicMgrIndex_Object = MibTableColumn
d5LicMgrIndex = _D5LicMgrIndex_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 8, 1, 22, 4, 1, 1),
    _D5LicMgrIndex_Type()
)
d5LicMgrIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    d5LicMgrIndex.setStatus("current")
_D5LicMgrQuadToHexAllocated_Type = Unsigned32
_D5LicMgrQuadToHexAllocated_Object = MibTableColumn
d5LicMgrQuadToHexAllocated = _D5LicMgrQuadToHexAllocated_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 8, 1, 22, 4, 1, 2),
    _D5LicMgrQuadToHexAllocated_Type()
)
d5LicMgrQuadToHexAllocated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    d5LicMgrQuadToHexAllocated.setStatus("current")
_D5LicMgrHexToOctalAllocated_Type = Unsigned32
_D5LicMgrHexToOctalAllocated_Object = MibTableColumn
d5LicMgrHexToOctalAllocated = _D5LicMgrHexToOctalAllocated_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 8, 1, 22, 4, 1, 3),
    _D5LicMgrHexToOctalAllocated_Type()
)
d5LicMgrHexToOctalAllocated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    d5LicMgrHexToOctalAllocated.setStatus("current")
_D5LicMgrQuadToOctalAllocated_Type = Unsigned32
_D5LicMgrQuadToOctalAllocated_Object = MibTableColumn
d5LicMgrQuadToOctalAllocated = _D5LicMgrQuadToOctalAllocated_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 8, 1, 22, 4, 1, 4),
    _D5LicMgrQuadToOctalAllocated_Type()
)
d5LicMgrQuadToOctalAllocated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    d5LicMgrQuadToOctalAllocated.setStatus("current")
_D5LicenseTraps_ObjectIdentity = ObjectIdentity
d5LicenseTraps = _D5LicenseTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4115, 1, 8, 1, 22, 5)
)

# Managed Objects groups

d5LicenseConfigurationGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4115, 1, 8, 1, 22, 1)
)
d5LicenseConfigurationGroup.setObjects(
      *(("ARRIS-D5-LICENSE-MIB", "d5LicenseTrapDelay"),
        ("ARRIS-D5-LICENSE-MIB", "d5LicenseTrapResendRate"),
        ("ARRIS-D5-LICENSE-MIB", "d5LicenseTimeToLive"),
        ("ARRIS-D5-LICENSE-MIB", "d5LicenseRemotePublicKey"),
        ("ARRIS-D5-LICENSE-MIB", "d5LicenseLocalPublicKey"))
)
if mibBuilder.loadTexts:
    d5LicenseConfigurationGroup.setStatus("current")


# Notification objects

d5LMNoKeyAvailable = NotificationType(
    (1, 3, 6, 1, 4, 1, 4115, 1, 8, 1, 22, 5, 1)
)
d5LMNoKeyAvailable.setObjects(
      *(("ARRIS-D5-LICENSE-MIB", "d5LicenseAllocationType"),
        ("ARRIS-D5-LICENSE-MIB", "d5LicensesAllocated"),
        ("ARRIS-D5-LICENSE-MIB", "d5LicensesInUse"))
)
if mibBuilder.loadTexts:
    d5LMNoKeyAvailable.setStatus(
        "current"
    )

d5LMServicePeriodExpire = NotificationType(
    (1, 3, 6, 1, 4, 1, 4115, 1, 8, 1, 22, 5, 2)
)
d5LMServicePeriodExpire.setObjects(
      *(("ARRIS-D5-LICENSE-MIB", "d5LicenseAllocationType"),
        ("ARRIS-D5-LICENSE-MIB", "d5LicensesAllocated"),
        ("ARRIS-D5-LICENSE-MIB", "d5LicensesInUse"),
        ("ARRIS-D5-LICENSE-MIB", "d5LicenseIndex"))
)
if mibBuilder.loadTexts:
    d5LMServicePeriodExpire.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ARRIS-D5-LICENSE-MIB",
    **{"D5LicenseType": D5LicenseType,
       "D5EncryptionKeyType": D5EncryptionKeyType,
       "D5EncryptedType": D5EncryptedType,
       "d5LicenseMib": d5LicenseMib,
       "d5LicenseConfigurationGroup": d5LicenseConfigurationGroup,
       "d5LicenseTrapDelay": d5LicenseTrapDelay,
       "d5LicenseTrapResendRate": d5LicenseTrapResendRate,
       "d5LicenseTimeToLive": d5LicenseTimeToLive,
       "d5LicenseRemotePublicKey": d5LicenseRemotePublicKey,
       "d5LicenseLocalPublicKey": d5LicenseLocalPublicKey,
       "d5LicenseAllocationTable": d5LicenseAllocationTable,
       "d5LicenseAllocationEntry": d5LicenseAllocationEntry,
       "d5LicenseAllocationType": d5LicenseAllocationType,
       "d5LicensesAllocated": d5LicensesAllocated,
       "d5LicensesInUse": d5LicensesInUse,
       "d5LicMgrId": d5LicMgrId,
       "d5LicenseInUseTable": d5LicenseInUseTable,
       "d5LicenseInUseEntry": d5LicenseInUseEntry,
       "d5LicenseInUseType": d5LicenseInUseType,
       "d5LicenseIndex": d5LicenseIndex,
       "d5LicenseRowStatus": d5LicenseRowStatus,
       "d5LicenseInUseMgrId": d5LicenseInUseMgrId,
       "d5LicMgrAllocationTable": d5LicMgrAllocationTable,
       "d5LicMgrAllocationEntry": d5LicMgrAllocationEntry,
       "d5LicMgrIndex": d5LicMgrIndex,
       "d5LicMgrQuadToHexAllocated": d5LicMgrQuadToHexAllocated,
       "d5LicMgrHexToOctalAllocated": d5LicMgrHexToOctalAllocated,
       "d5LicMgrQuadToOctalAllocated": d5LicMgrQuadToOctalAllocated,
       "d5LicenseTraps": d5LicenseTraps,
       "d5LMNoKeyAvailable": d5LMNoKeyAvailable,
       "d5LMServicePeriodExpire": d5LMServicePeriodExpire}
)
