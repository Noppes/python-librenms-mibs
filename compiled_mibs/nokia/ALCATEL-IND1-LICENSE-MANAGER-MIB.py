# SNMP MIB module (ALCATEL-IND1-LICENSE-MANAGER-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\nokia\aos6\ALCATEL-IND1-LICENSE-MANAGER-MIB

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

(softentIND1LicenseManager,) = mibBuilder.importSymbols(
    "ALCATEL-IND1-BASE",
    "softentIND1LicenseManager")

(ModuleCompliance,
 NotificationGroup,
 ObjectGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup",
    "ObjectGroup")

(snmpTraps,) = mibBuilder.importSymbols(
    "SNMPv2-MIB",
    "snmpTraps")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

aluLicenseManagerMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 54, 1)
)
if mibBuilder.loadTexts:
    aluLicenseManagerMIB.setRevisions(
        ("2009-03-23 00:00",
         "2011-07-14 00:00",
         "2019-10-07 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AluLicenseManagerMIBNotifications_ObjectIdentity = ObjectIdentity
aluLicenseManagerMIBNotifications = _AluLicenseManagerMIBNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 54, 1, 0)
)
_AluLicenseManagerMIBObjects_ObjectIdentity = ObjectIdentity
aluLicenseManagerMIBObjects = _AluLicenseManagerMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 54, 1, 1)
)
if mibBuilder.loadTexts:
    aluLicenseManagerMIBObjects.setStatus("current")
_AluLicenseManagerConfig_ObjectIdentity = ObjectIdentity
aluLicenseManagerConfig = _AluLicenseManagerConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 54, 1, 1, 1)
)


class _AluLicenseManagerApplyLicense_Type(Integer32):
    """Custom type aluLicenseManagerApplyLicense based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("default", 0),
          ("apply", 1))
    )


_AluLicenseManagerApplyLicense_Type.__name__ = "Integer32"
_AluLicenseManagerApplyLicense_Object = MibScalar
aluLicenseManagerApplyLicense = _AluLicenseManagerApplyLicense_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 54, 1, 1, 1, 1),
    _AluLicenseManagerApplyLicense_Type()
)
aluLicenseManagerApplyLicense.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aluLicenseManagerApplyLicense.setStatus("current")


class _AluLicensedFileName_Type(DisplayString):
    """Custom type aluLicensedFileName based on DisplayString"""
    defaultValue = OctetString("lmlicense.dat")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_AluLicensedFileName_Type.__name__ = "DisplayString"
_AluLicensedFileName_Object = MibScalar
aluLicensedFileName = _AluLicensedFileName_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 54, 1, 1, 1, 2),
    _AluLicensedFileName_Type()
)
aluLicensedFileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aluLicensedFileName.setStatus("current")
_AluLicenseManagerInfoTable_Object = MibTable
aluLicenseManagerInfoTable = _AluLicenseManagerInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 54, 1, 1, 2)
)
if mibBuilder.loadTexts:
    aluLicenseManagerInfoTable.setStatus("current")
_AluLicenseManagerInfoEntry_Object = MibTableRow
aluLicenseManagerInfoEntry = _AluLicenseManagerInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 54, 1, 1, 2, 1)
)
aluLicenseManagerInfoEntry.setIndexNames(
    (0, "ALCATEL-IND1-LICENSE-MANAGER-MIB", "aluLicenseId"),
)
if mibBuilder.loadTexts:
    aluLicenseManagerInfoEntry.setStatus("current")


class _AluLicenseId_Type(Unsigned32):
    """Custom type aluLicenseId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_AluLicenseId_Type.__name__ = "Unsigned32"
_AluLicenseId_Object = MibTableColumn
aluLicenseId = _AluLicenseId_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 54, 1, 1, 2, 1, 1),
    _AluLicenseId_Type()
)
aluLicenseId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    aluLicenseId.setStatus("current")


class _AluLicensedApplication_Type(DisplayString):
    """Custom type aluLicensedApplication based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_AluLicensedApplication_Type.__name__ = "DisplayString"
_AluLicensedApplication_Object = MibTableColumn
aluLicensedApplication = _AluLicensedApplication_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 54, 1, 1, 2, 1, 2),
    _AluLicensedApplication_Type()
)
aluLicensedApplication.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluLicensedApplication.setStatus("current")


class _AluLicenseType_Type(Integer32):
    """Custom type aluLicenseType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("demo", 1),
          ("permanent", 2))
    )


_AluLicenseType_Type.__name__ = "Integer32"
_AluLicenseType_Object = MibTableColumn
aluLicenseType = _AluLicenseType_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 54, 1, 1, 2, 1, 3),
    _AluLicenseType_Type()
)
aluLicenseType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluLicenseType.setStatus("current")


class _AluLicenseTimeRemaining_Type(Integer32):
    """Custom type aluLicenseTimeRemaining based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 60),
    )


_AluLicenseTimeRemaining_Type.__name__ = "Integer32"
_AluLicenseTimeRemaining_Object = MibTableColumn
aluLicenseTimeRemaining = _AluLicenseTimeRemaining_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 54, 1, 1, 2, 1, 4),
    _AluLicenseTimeRemaining_Type()
)
aluLicenseTimeRemaining.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluLicenseTimeRemaining.setStatus("current")
_AluLicenseManagerFileInfoTable_Object = MibTable
aluLicenseManagerFileInfoTable = _AluLicenseManagerFileInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 54, 1, 1, 3)
)
if mibBuilder.loadTexts:
    aluLicenseManagerFileInfoTable.setStatus("current")
_AluLicenseManagerFileInfoEntry_Object = MibTableRow
aluLicenseManagerFileInfoEntry = _AluLicenseManagerFileInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 54, 1, 1, 3, 1)
)
aluLicenseManagerFileInfoEntry.setIndexNames(
    (0, "ALCATEL-IND1-LICENSE-MANAGER-MIB", "aluLicenseFileIndex"),
)
if mibBuilder.loadTexts:
    aluLicenseManagerFileInfoEntry.setStatus("current")


class _AluLicenseFileIndex_Type(Unsigned32):
    """Custom type aluLicenseFileIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_AluLicenseFileIndex_Type.__name__ = "Unsigned32"
_AluLicenseFileIndex_Object = MibTableColumn
aluLicenseFileIndex = _AluLicenseFileIndex_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 54, 1, 1, 3, 1, 1),
    _AluLicenseFileIndex_Type()
)
aluLicenseFileIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    aluLicenseFileIndex.setStatus("current")
_AluSwitchMacAddress_Type = MacAddress
_AluSwitchMacAddress_Object = MibTableColumn
aluSwitchMacAddress = _AluSwitchMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 54, 1, 1, 3, 1, 2),
    _AluSwitchMacAddress_Type()
)
aluSwitchMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluSwitchMacAddress.setStatus("current")


class _AluLicensedFileApplication_Type(DisplayString):
    """Custom type aluLicensedFileApplication based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_AluLicensedFileApplication_Type.__name__ = "DisplayString"
_AluLicensedFileApplication_Object = MibTableColumn
aluLicensedFileApplication = _AluLicensedFileApplication_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 54, 1, 1, 3, 1, 3),
    _AluLicensedFileApplication_Type()
)
aluLicensedFileApplication.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluLicensedFileApplication.setStatus("current")


class _AluLicensedFileLocal_Type(Integer32):
    """Custom type aluLicensedFileLocal based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("local", 1),
          ("other", 2))
    )


_AluLicensedFileLocal_Type.__name__ = "Integer32"
_AluLicensedFileLocal_Object = MibTableColumn
aluLicensedFileLocal = _AluLicensedFileLocal_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 54, 1, 1, 3, 1, 4),
    _AluLicensedFileLocal_Type()
)
aluLicensedFileLocal.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aluLicensedFileLocal.setStatus("current")
_AluLicenseManagerRemoveTable_Object = MibTable
aluLicenseManagerRemoveTable = _AluLicenseManagerRemoveTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 54, 1, 1, 4)
)
if mibBuilder.loadTexts:
    aluLicenseManagerRemoveTable.setStatus("current")
_AluLicenseManagerRemoveEntry_Object = MibTableRow
aluLicenseManagerRemoveEntry = _AluLicenseManagerRemoveEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 54, 1, 1, 4, 1)
)
aluLicenseManagerRemoveEntry.setIndexNames(
    (0, "ALCATEL-IND1-LICENSE-MANAGER-MIB", "aluLicenseRemoveIndex"),
)
if mibBuilder.loadTexts:
    aluLicenseManagerRemoveEntry.setStatus("current")


class _AluLicenseRemoveIndex_Type(Integer32):
    """Custom type aluLicenseRemoveIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
    )


_AluLicenseRemoveIndex_Type.__name__ = "Integer32"
_AluLicenseRemoveIndex_Object = MibTableColumn
aluLicenseRemoveIndex = _AluLicenseRemoveIndex_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 54, 1, 1, 4, 1, 1),
    _AluLicenseRemoveIndex_Type()
)
aluLicenseRemoveIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    aluLicenseRemoveIndex.setStatus("current")


class _AluLicenseRemoveFeatureID_Type(Integer32):
    """Custom type aluLicenseRemoveFeatureID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("metro", 1),
          ("oneGig", 2),
          ("tenGig", 3))
    )


_AluLicenseRemoveFeatureID_Type.__name__ = "Integer32"
_AluLicenseRemoveFeatureID_Object = MibTableColumn
aluLicenseRemoveFeatureID = _AluLicenseRemoveFeatureID_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 54, 1, 1, 4, 1, 2),
    _AluLicenseRemoveFeatureID_Type()
)
aluLicenseRemoveFeatureID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aluLicenseRemoveFeatureID.setStatus("current")


class _AluLicenseRemoveSlotID_Type(Integer32):
    """Custom type aluLicenseRemoveSlotID based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1008),
    )


_AluLicenseRemoveSlotID_Type.__name__ = "Integer32"
_AluLicenseRemoveSlotID_Object = MibTableColumn
aluLicenseRemoveSlotID = _AluLicenseRemoveSlotID_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 54, 1, 1, 4, 1, 3),
    _AluLicenseRemoveSlotID_Type()
)
aluLicenseRemoveSlotID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aluLicenseRemoveSlotID.setStatus("current")
_AluLicenseManagerDemoLicenseTable_Object = MibTable
aluLicenseManagerDemoLicenseTable = _AluLicenseManagerDemoLicenseTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 54, 1, 1, 5)
)
if mibBuilder.loadTexts:
    aluLicenseManagerDemoLicenseTable.setStatus("current")
_AluLicenseManagerDemoLicenseEntry_Object = MibTableRow
aluLicenseManagerDemoLicenseEntry = _AluLicenseManagerDemoLicenseEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 54, 1, 1, 5, 1)
)
aluLicenseManagerDemoLicenseEntry.setIndexNames(
    (0, "ALCATEL-IND1-LICENSE-MANAGER-MIB", "aluLicenseDemoIndex"),
)
if mibBuilder.loadTexts:
    aluLicenseManagerDemoLicenseEntry.setStatus("current")


class _AluLicenseDemoIndex_Type(Integer32):
    """Custom type aluLicenseDemoIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
    )


_AluLicenseDemoIndex_Type.__name__ = "Integer32"
_AluLicenseDemoIndex_Object = MibTableColumn
aluLicenseDemoIndex = _AluLicenseDemoIndex_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 54, 1, 1, 5, 1, 1),
    _AluLicenseDemoIndex_Type()
)
aluLicenseDemoIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    aluLicenseDemoIndex.setStatus("current")


class _AluLicenseDemoFeatureID_Type(Integer32):
    """Custom type aluLicenseDemoFeatureID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("metro", 1),
          ("oneGig", 2),
          ("tenGig", 3))
    )


_AluLicenseDemoFeatureID_Type.__name__ = "Integer32"
_AluLicenseDemoFeatureID_Object = MibTableColumn
aluLicenseDemoFeatureID = _AluLicenseDemoFeatureID_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 54, 1, 1, 5, 1, 2),
    _AluLicenseDemoFeatureID_Type()
)
aluLicenseDemoFeatureID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aluLicenseDemoFeatureID.setStatus("current")


class _AluLicenseDemoSlotID_Type(Integer32):
    """Custom type aluLicenseDemoSlotID based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1008),
    )


_AluLicenseDemoSlotID_Type.__name__ = "Integer32"
_AluLicenseDemoSlotID_Object = MibTableColumn
aluLicenseDemoSlotID = _AluLicenseDemoSlotID_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 54, 1, 1, 5, 1, 3),
    _AluLicenseDemoSlotID_Type()
)
aluLicenseDemoSlotID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aluLicenseDemoSlotID.setStatus("current")
_AluLicenseManagerLicenseInfoTable_Object = MibTable
aluLicenseManagerLicenseInfoTable = _AluLicenseManagerLicenseInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 54, 1, 1, 6)
)
if mibBuilder.loadTexts:
    aluLicenseManagerLicenseInfoTable.setStatus("current")
_AluLicenseManagerLicenseInfoEntry_Object = MibTableRow
aluLicenseManagerLicenseInfoEntry = _AluLicenseManagerLicenseInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 54, 1, 1, 6, 1)
)
aluLicenseManagerLicenseInfoEntry.setIndexNames(
    (0, "ALCATEL-IND1-LICENSE-MANAGER-MIB", "aluLicenseInfoSlotId"),
    (0, "ALCATEL-IND1-LICENSE-MANAGER-MIB", "aluLicensedInfoApplication"),
)
if mibBuilder.loadTexts:
    aluLicenseManagerLicenseInfoEntry.setStatus("current")


class _AluLicenseInfoSlotId_Type(Unsigned32):
    """Custom type aluLicenseInfoSlotId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1008),
    )


_AluLicenseInfoSlotId_Type.__name__ = "Unsigned32"
_AluLicenseInfoSlotId_Object = MibTableColumn
aluLicenseInfoSlotId = _AluLicenseInfoSlotId_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 54, 1, 1, 6, 1, 1),
    _AluLicenseInfoSlotId_Type()
)
aluLicenseInfoSlotId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    aluLicenseInfoSlotId.setStatus("current")


class _AluLicensedInfoApplication_Type(DisplayString):
    """Custom type aluLicensedInfoApplication based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_AluLicensedInfoApplication_Type.__name__ = "DisplayString"
_AluLicensedInfoApplication_Object = MibTableColumn
aluLicensedInfoApplication = _AluLicensedInfoApplication_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 54, 1, 1, 6, 1, 2),
    _AluLicensedInfoApplication_Type()
)
aluLicensedInfoApplication.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    aluLicensedInfoApplication.setStatus("current")


class _AluLicenseInfoType_Type(Integer32):
    """Custom type aluLicenseInfoType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("demo", 1),
          ("permanent", 2))
    )


_AluLicenseInfoType_Type.__name__ = "Integer32"
_AluLicenseInfoType_Object = MibTableColumn
aluLicenseInfoType = _AluLicenseInfoType_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 54, 1, 1, 6, 1, 3),
    _AluLicenseInfoType_Type()
)
aluLicenseInfoType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluLicenseInfoType.setStatus("current")


class _AluLicenseInfoTimeRemaining_Type(Integer32):
    """Custom type aluLicenseInfoTimeRemaining based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 60),
    )


_AluLicenseInfoTimeRemaining_Type.__name__ = "Integer32"
_AluLicenseInfoTimeRemaining_Object = MibTableColumn
aluLicenseInfoTimeRemaining = _AluLicenseInfoTimeRemaining_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 54, 1, 1, 6, 1, 4),
    _AluLicenseInfoTimeRemaining_Type()
)
aluLicenseInfoTimeRemaining.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluLicenseInfoTimeRemaining.setStatus("current")


class _AluLicenseInfoCustomerInfo_Type(DisplayString):
    """Custom type aluLicenseInfoCustomerInfo based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 40),
    )


_AluLicenseInfoCustomerInfo_Type.__name__ = "DisplayString"
_AluLicenseInfoCustomerInfo_Object = MibTableColumn
aluLicenseInfoCustomerInfo = _AluLicenseInfoCustomerInfo_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 54, 1, 1, 6, 1, 5),
    _AluLicenseInfoCustomerInfo_Type()
)
aluLicenseInfoCustomerInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluLicenseInfoCustomerInfo.setStatus("current")
_AluLicenseManagerMIBConformance_ObjectIdentity = ObjectIdentity
aluLicenseManagerMIBConformance = _AluLicenseManagerMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 54, 1, 2)
)
if mibBuilder.loadTexts:
    aluLicenseManagerMIBConformance.setStatus("current")
_AluLicenseManagerMIBGroups_ObjectIdentity = ObjectIdentity
aluLicenseManagerMIBGroups = _AluLicenseManagerMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 54, 1, 2, 1)
)
if mibBuilder.loadTexts:
    aluLicenseManagerMIBGroups.setStatus("current")
_AluLicenseManagerMIBCompliances_ObjectIdentity = ObjectIdentity
aluLicenseManagerMIBCompliances = _AluLicenseManagerMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 54, 1, 2, 2)
)
if mibBuilder.loadTexts:
    aluLicenseManagerMIBCompliances.setStatus("current")
_AluLicenseManagerMIBTrapObjects_ObjectIdentity = ObjectIdentity
aluLicenseManagerMIBTrapObjects = _AluLicenseManagerMIBTrapObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 54, 1, 3)
)


class _AluLicensedInfoSlot_Type(Integer32):
    """Custom type aluLicensedInfoSlot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1008),
    )


_AluLicensedInfoSlot_Type.__name__ = "Integer32"
_AluLicensedInfoSlot_Object = MibScalar
aluLicensedInfoSlot = _AluLicensedInfoSlot_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 54, 1, 3, 1),
    _AluLicensedInfoSlot_Type()
)
aluLicensedInfoSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluLicensedInfoSlot.setStatus("current")


class _AluLicenseInfoFeature_Type(DisplayString):
    """Custom type aluLicenseInfoFeature based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_AluLicenseInfoFeature_Type.__name__ = "DisplayString"
_AluLicenseInfoFeature_Object = MibScalar
aluLicenseInfoFeature = _AluLicenseInfoFeature_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 54, 1, 3, 2),
    _AluLicenseInfoFeature_Type()
)
aluLicenseInfoFeature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluLicenseInfoFeature.setStatus("current")

# Managed Objects groups

aluLicenseManagerConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 54, 1, 2, 1, 1)
)
aluLicenseManagerConfigGroup.setObjects(
      *(("ALCATEL-IND1-LICENSE-MANAGER-MIB", "aluLicenseManagerApplyLicense"),
        ("ALCATEL-IND1-LICENSE-MANAGER-MIB", "aluLicensedFileName"))
)
if mibBuilder.loadTexts:
    aluLicenseManagerConfigGroup.setStatus("current")

aluLicenseManagerInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 54, 1, 2, 1, 2)
)
aluLicenseManagerInfoGroup.setObjects(
      *(("ALCATEL-IND1-LICENSE-MANAGER-MIB", "aluLicensedApplication"),
        ("ALCATEL-IND1-LICENSE-MANAGER-MIB", "aluLicenseType"),
        ("ALCATEL-IND1-LICENSE-MANAGER-MIB", "aluLicenseTimeRemaining"))
)
if mibBuilder.loadTexts:
    aluLicenseManagerInfoGroup.setStatus("current")

aluLicenseManagerFileInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 54, 1, 2, 1, 4)
)
aluLicenseManagerFileInfoGroup.setObjects(
      *(("ALCATEL-IND1-LICENSE-MANAGER-MIB", "aluSwitchMacAddress"),
        ("ALCATEL-IND1-LICENSE-MANAGER-MIB", "aluLicensedFileApplication"),
        ("ALCATEL-IND1-LICENSE-MANAGER-MIB", "aluLicensedFileLocal"))
)
if mibBuilder.loadTexts:
    aluLicenseManagerFileInfoGroup.setStatus("current")

aluLicenseManagerRemoveInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 54, 1, 2, 1, 5)
)
aluLicenseManagerRemoveInfoGroup.setObjects(
      *(("ALCATEL-IND1-LICENSE-MANAGER-MIB", "aluLicenseRemoveFeatureID"),
        ("ALCATEL-IND1-LICENSE-MANAGER-MIB", "aluLicenseRemoveSlotID"))
)
if mibBuilder.loadTexts:
    aluLicenseManagerRemoveInfoGroup.setStatus("current")

aluLicenseManagerDemoInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 54, 1, 2, 1, 6)
)
aluLicenseManagerDemoInfoGroup.setObjects(
      *(("ALCATEL-IND1-LICENSE-MANAGER-MIB", "aluLicenseDemoFeatureID"),
        ("ALCATEL-IND1-LICENSE-MANAGER-MIB", "aluLicenseDemoSlotID"))
)
if mibBuilder.loadTexts:
    aluLicenseManagerDemoInfoGroup.setStatus("current")

aluLicenseManagerLicenseInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 54, 1, 2, 1, 7)
)
aluLicenseManagerLicenseInfoGroup.setObjects(
      *(("ALCATEL-IND1-LICENSE-MANAGER-MIB", "aluLicenseInfoType"),
        ("ALCATEL-IND1-LICENSE-MANAGER-MIB", "aluLicenseInfoTimeRemaining"),
        ("ALCATEL-IND1-LICENSE-MANAGER-MIB", "aluLicenseInfoCustomerInfo"))
)
if mibBuilder.loadTexts:
    aluLicenseManagerLicenseInfoGroup.setStatus("current")


# Notification objects

aluLicenseManagerLicenseExpired = NotificationType(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 54, 1, 0, 0, 1)
)
aluLicenseManagerLicenseExpired.setObjects(
      *(("ALCATEL-IND1-LICENSE-MANAGER-MIB", "aluLicensedApplication"),
        ("ALCATEL-IND1-LICENSE-MANAGER-MIB", "aluLicenseTimeRemaining"))
)
if mibBuilder.loadTexts:
    aluLicenseManagerLicenseExpired.setStatus(
        "current"
    )

aluLicenseManagerLicenseExpiry = NotificationType(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 54, 1, 0, 0, 2)
)
aluLicenseManagerLicenseExpiry.setObjects(
      *(("ALCATEL-IND1-LICENSE-MANAGER-MIB", "aluLicenseInfoFeature"),
        ("ALCATEL-IND1-LICENSE-MANAGER-MIB", "aluLicenseInfoTimeRemaining"),
        ("ALCATEL-IND1-LICENSE-MANAGER-MIB", "aluLicensedInfoSlot"))
)
if mibBuilder.loadTexts:
    aluLicenseManagerLicenseExpiry.setStatus(
        "current"
    )


# Notifications groups

aluLicenseManagerNotificationsGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 54, 1, 2, 1, 3)
)
aluLicenseManagerNotificationsGroup.setObjects(
      *(("ALCATEL-IND1-LICENSE-MANAGER-MIB", "aluLicenseManagerLicenseExpired"),
        ("ALCATEL-IND1-LICENSE-MANAGER-MIB", "aluLicenseManagerLicenseExpiry"))
)
if mibBuilder.loadTexts:
    aluLicenseManagerNotificationsGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

aluLicenseManagerMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 54, 1, 2, 2, 1)
)
aluLicenseManagerMIBCompliance.setObjects(
      *(("ALCATEL-IND1-LICENSE-MANAGER-MIB", "aluLicenseManagerConfigGroup"),
        ("ALCATEL-IND1-LICENSE-MANAGER-MIB", "aluLicenseManagerLicenseInfoGroup"),
        ("ALCATEL-IND1-LICENSE-MANAGER-MIB", "aluLicenseManagerNotificationsGroup"),
        ("ALCATEL-IND1-LICENSE-MANAGER-MIB", "aluLicenseManagerFileInfoGroup"),
        ("ALCATEL-IND1-LICENSE-MANAGER-MIB", "aluLicenseManagerRemoveInfoGroup"),
        ("ALCATEL-IND1-LICENSE-MANAGER-MIB", "aluLicenseManagerDemoInfoGroup"),
        ("ALCATEL-IND1-LICENSE-MANAGER-MIB", "aluLicenseManagerInfoGroup"))
)
if mibBuilder.loadTexts:
    aluLicenseManagerMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ALCATEL-IND1-LICENSE-MANAGER-MIB",
    **{"aluLicenseManagerMIB": aluLicenseManagerMIB,
       "aluLicenseManagerMIBNotifications": aluLicenseManagerMIBNotifications,
       "aluLicenseManagerLicenseExpired": aluLicenseManagerLicenseExpired,
       "aluLicenseManagerLicenseExpiry": aluLicenseManagerLicenseExpiry,
       "aluLicenseManagerMIBObjects": aluLicenseManagerMIBObjects,
       "aluLicenseManagerConfig": aluLicenseManagerConfig,
       "aluLicenseManagerApplyLicense": aluLicenseManagerApplyLicense,
       "aluLicensedFileName": aluLicensedFileName,
       "aluLicenseManagerInfoTable": aluLicenseManagerInfoTable,
       "aluLicenseManagerInfoEntry": aluLicenseManagerInfoEntry,
       "aluLicenseId": aluLicenseId,
       "aluLicensedApplication": aluLicensedApplication,
       "aluLicenseType": aluLicenseType,
       "aluLicenseTimeRemaining": aluLicenseTimeRemaining,
       "aluLicenseManagerFileInfoTable": aluLicenseManagerFileInfoTable,
       "aluLicenseManagerFileInfoEntry": aluLicenseManagerFileInfoEntry,
       "aluLicenseFileIndex": aluLicenseFileIndex,
       "aluSwitchMacAddress": aluSwitchMacAddress,
       "aluLicensedFileApplication": aluLicensedFileApplication,
       "aluLicensedFileLocal": aluLicensedFileLocal,
       "aluLicenseManagerRemoveTable": aluLicenseManagerRemoveTable,
       "aluLicenseManagerRemoveEntry": aluLicenseManagerRemoveEntry,
       "aluLicenseRemoveIndex": aluLicenseRemoveIndex,
       "aluLicenseRemoveFeatureID": aluLicenseRemoveFeatureID,
       "aluLicenseRemoveSlotID": aluLicenseRemoveSlotID,
       "aluLicenseManagerDemoLicenseTable": aluLicenseManagerDemoLicenseTable,
       "aluLicenseManagerDemoLicenseEntry": aluLicenseManagerDemoLicenseEntry,
       "aluLicenseDemoIndex": aluLicenseDemoIndex,
       "aluLicenseDemoFeatureID": aluLicenseDemoFeatureID,
       "aluLicenseDemoSlotID": aluLicenseDemoSlotID,
       "aluLicenseManagerLicenseInfoTable": aluLicenseManagerLicenseInfoTable,
       "aluLicenseManagerLicenseInfoEntry": aluLicenseManagerLicenseInfoEntry,
       "aluLicenseInfoSlotId": aluLicenseInfoSlotId,
       "aluLicensedInfoApplication": aluLicensedInfoApplication,
       "aluLicenseInfoType": aluLicenseInfoType,
       "aluLicenseInfoTimeRemaining": aluLicenseInfoTimeRemaining,
       "aluLicenseInfoCustomerInfo": aluLicenseInfoCustomerInfo,
       "aluLicenseManagerMIBConformance": aluLicenseManagerMIBConformance,
       "aluLicenseManagerMIBGroups": aluLicenseManagerMIBGroups,
       "aluLicenseManagerConfigGroup": aluLicenseManagerConfigGroup,
       "aluLicenseManagerInfoGroup": aluLicenseManagerInfoGroup,
       "aluLicenseManagerNotificationsGroup": aluLicenseManagerNotificationsGroup,
       "aluLicenseManagerFileInfoGroup": aluLicenseManagerFileInfoGroup,
       "aluLicenseManagerRemoveInfoGroup": aluLicenseManagerRemoveInfoGroup,
       "aluLicenseManagerDemoInfoGroup": aluLicenseManagerDemoInfoGroup,
       "aluLicenseManagerLicenseInfoGroup": aluLicenseManagerLicenseInfoGroup,
       "aluLicenseManagerMIBCompliances": aluLicenseManagerMIBCompliances,
       "aluLicenseManagerMIBCompliance": aluLicenseManagerMIBCompliance,
       "aluLicenseManagerMIBTrapObjects": aluLicenseManagerMIBTrapObjects,
       "aluLicensedInfoSlot": aluLicensedInfoSlot,
       "aluLicenseInfoFeature": aluLicenseInfoFeature}
)
