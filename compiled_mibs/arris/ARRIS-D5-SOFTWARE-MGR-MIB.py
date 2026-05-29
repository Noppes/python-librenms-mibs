# SNMP MIB module (ARRIS-D5-SOFTWARE-MGR-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\arris\d5\ARRIS-D5-SOFTWARE-MGR-MIB

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
    "TimeTicks",
    "Unsigned32",
    "enterprises",
    "iso")

(DateAndTime,
 DisplayString,
 PhysAddress,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "PhysAddress",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

softwareManagerMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4115, 1, 8, 1, 10)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_SmControlGroup_ObjectIdentity = ObjectIdentity
smControlGroup = _SmControlGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4115, 1, 8, 1, 10, 1)
)


class _SmReloadAction_Type(Integer32):
    """Custom type smReloadAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("nil", 1),
          ("reloadConfigSave", 2),
          ("reloadNoConfigSave", 3))
    )


_SmReloadAction_Type.__name__ = "Integer32"
_SmReloadAction_Object = MibScalar
smReloadAction = _SmReloadAction_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 8, 1, 10, 1, 1),
    _SmReloadAction_Type()
)
smReloadAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    smReloadAction.setStatus("current")


class _SmConfigFileAction_Type(Integer32):
    """Custom type smConfigFileAction based on Integer32"""
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
        *(("nil", 1),
          ("saveRunningConfig", 2),
          ("eraseStartupConfig", 3),
          ("uploadStartupConfigToServer", 4))
    )


_SmConfigFileAction_Type.__name__ = "Integer32"
_SmConfigFileAction_Object = MibScalar
smConfigFileAction = _SmConfigFileAction_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 8, 1, 10, 1, 2),
    _SmConfigFileAction_Type()
)
smConfigFileAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    smConfigFileAction.setStatus("current")
_SmSoftwareListGroup_ObjectIdentity = ObjectIdentity
smSoftwareListGroup = _SmSoftwareListGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4115, 1, 8, 1, 10, 2)
)
_SmSoftwareListTable_Object = MibTable
smSoftwareListTable = _SmSoftwareListTable_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 8, 1, 10, 2, 1)
)
if mibBuilder.loadTexts:
    smSoftwareListTable.setStatus("current")
_SmSoftwareListEntry_Object = MibTableRow
smSoftwareListEntry = _SmSoftwareListEntry_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 8, 1, 10, 2, 1, 1)
)
smSoftwareListEntry.setIndexNames(
    (0, "ARRIS-D5-SOFTWARE-MGR-MIB", "smSoftwareEntryIndex"),
)
if mibBuilder.loadTexts:
    smSoftwareListEntry.setStatus("current")


class _SmSoftwareEntryIndex_Type(Unsigned32):
    """Custom type smSoftwareEntryIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 30),
    )


_SmSoftwareEntryIndex_Type.__name__ = "Unsigned32"
_SmSoftwareEntryIndex_Object = MibTableColumn
smSoftwareEntryIndex = _SmSoftwareEntryIndex_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 8, 1, 10, 2, 1, 1, 1),
    _SmSoftwareEntryIndex_Type()
)
smSoftwareEntryIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    smSoftwareEntryIndex.setStatus("current")


class _SmSoftwareEntryFilename_Type(OctetString):
    """Custom type smSoftwareEntryFilename based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_SmSoftwareEntryFilename_Type.__name__ = "OctetString"
_SmSoftwareEntryFilename_Object = MibTableColumn
smSoftwareEntryFilename = _SmSoftwareEntryFilename_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 8, 1, 10, 2, 1, 1, 2),
    _SmSoftwareEntryFilename_Type()
)
smSoftwareEntryFilename.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smSoftwareEntryFilename.setStatus("current")


class _SmSoftwareEntryVersion_Type(OctetString):
    """Custom type smSoftwareEntryVersion based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_SmSoftwareEntryVersion_Type.__name__ = "OctetString"
_SmSoftwareEntryVersion_Object = MibTableColumn
smSoftwareEntryVersion = _SmSoftwareEntryVersion_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 8, 1, 10, 2, 1, 1, 3),
    _SmSoftwareEntryVersion_Type()
)
smSoftwareEntryVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smSoftwareEntryVersion.setStatus("current")
_SmSoftwareEntryDate_Type = DateAndTime
_SmSoftwareEntryDate_Object = MibTableColumn
smSoftwareEntryDate = _SmSoftwareEntryDate_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 8, 1, 10, 2, 1, 1, 4),
    _SmSoftwareEntryDate_Type()
)
smSoftwareEntryDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smSoftwareEntryDate.setStatus("current")


class _SmSoftwareEntryState_Type(Integer32):
    """Custom type smSoftwareEntryState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("valid", 1),
          ("corrupt", 2),
          ("unknown", 3))
    )


_SmSoftwareEntryState_Type.__name__ = "Integer32"
_SmSoftwareEntryState_Object = MibTableColumn
smSoftwareEntryState = _SmSoftwareEntryState_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 8, 1, 10, 2, 1, 1, 5),
    _SmSoftwareEntryState_Type()
)
smSoftwareEntryState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smSoftwareEntryState.setStatus("current")
_SmSoftwareEntrySize_Type = Integer32
_SmSoftwareEntrySize_Object = MibTableColumn
smSoftwareEntrySize = _SmSoftwareEntrySize_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 8, 1, 10, 2, 1, 1, 6),
    _SmSoftwareEntrySize_Type()
)
smSoftwareEntrySize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smSoftwareEntrySize.setStatus("current")


class _SmSoftwareEntryStatus_Type(Integer32):
    """Custom type smSoftwareEntryStatus based on Integer32"""
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
        *(("running-boot", 1),
          ("running", 2),
          ("boot", 3),
          ("inactive", 4))
    )


_SmSoftwareEntryStatus_Type.__name__ = "Integer32"
_SmSoftwareEntryStatus_Object = MibTableColumn
smSoftwareEntryStatus = _SmSoftwareEntryStatus_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 8, 1, 10, 2, 1, 1, 7),
    _SmSoftwareEntryStatus_Type()
)
smSoftwareEntryStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smSoftwareEntryStatus.setStatus("current")


class _SmSoftwareEntryAction_Type(Integer32):
    """Custom type smSoftwareEntryAction based on Integer32"""
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
        *(("nil", 1),
          ("makeBoot", 2),
          ("upload", 3),
          ("delete", 4))
    )


_SmSoftwareEntryAction_Type.__name__ = "Integer32"
_SmSoftwareEntryAction_Object = MibTableColumn
smSoftwareEntryAction = _SmSoftwareEntryAction_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 8, 1, 10, 2, 1, 1, 8),
    _SmSoftwareEntryAction_Type()
)
smSoftwareEntryAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    smSoftwareEntryAction.setStatus("current")
_SmConfigFileListGroup_ObjectIdentity = ObjectIdentity
smConfigFileListGroup = _SmConfigFileListGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4115, 1, 8, 1, 10, 3)
)
_SmConfigFileListTable_Object = MibTable
smConfigFileListTable = _SmConfigFileListTable_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 8, 1, 10, 3, 1)
)
if mibBuilder.loadTexts:
    smConfigFileListTable.setStatus("current")
_SmConfigFileListEntry_Object = MibTableRow
smConfigFileListEntry = _SmConfigFileListEntry_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 8, 1, 10, 3, 1, 1)
)
smConfigFileListEntry.setIndexNames(
    (0, "ARRIS-D5-SOFTWARE-MGR-MIB", "smConfigFileEntryIndex"),
)
if mibBuilder.loadTexts:
    smConfigFileListEntry.setStatus("current")


class _SmConfigFileEntryIndex_Type(Unsigned32):
    """Custom type smConfigFileEntryIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 30),
    )


_SmConfigFileEntryIndex_Type.__name__ = "Unsigned32"
_SmConfigFileEntryIndex_Object = MibTableColumn
smConfigFileEntryIndex = _SmConfigFileEntryIndex_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 8, 1, 10, 3, 1, 1, 1),
    _SmConfigFileEntryIndex_Type()
)
smConfigFileEntryIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    smConfigFileEntryIndex.setStatus("current")


class _SmConfigFileEntryName_Type(OctetString):
    """Custom type smConfigFileEntryName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_SmConfigFileEntryName_Type.__name__ = "OctetString"
_SmConfigFileEntryName_Object = MibTableColumn
smConfigFileEntryName = _SmConfigFileEntryName_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 8, 1, 10, 3, 1, 1, 2),
    _SmConfigFileEntryName_Type()
)
smConfigFileEntryName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smConfigFileEntryName.setStatus("current")
_SmConfigFileTimestamp_Type = DateAndTime
_SmConfigFileTimestamp_Object = MibTableColumn
smConfigFileTimestamp = _SmConfigFileTimestamp_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 8, 1, 10, 3, 1, 1, 3),
    _SmConfigFileTimestamp_Type()
)
smConfigFileTimestamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smConfigFileTimestamp.setStatus("current")


class _SmConfigFileEntryAction_Type(Integer32):
    """Custom type smConfigFileEntryAction based on Integer32"""
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
        *(("nil", 1),
          ("makeStartupConfig", 2),
          ("copyIntoRunningConfig", 3),
          ("upload", 4),
          ("delete", 5))
    )


_SmConfigFileEntryAction_Type.__name__ = "Integer32"
_SmConfigFileEntryAction_Object = MibTableColumn
smConfigFileEntryAction = _SmConfigFileEntryAction_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 8, 1, 10, 3, 1, 1, 4),
    _SmConfigFileEntryAction_Type()
)
smConfigFileEntryAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    smConfigFileEntryAction.setStatus("current")
_SmSoftwareTransferGroup_ObjectIdentity = ObjectIdentity
smSoftwareTransferGroup = _SmSoftwareTransferGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4115, 1, 8, 1, 10, 4)
)


class _SmSoftwareTransferDevice_Type(Integer32):
    """Custom type smSoftwareTransferDevice based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("nfs", 1),
          ("tftp", 2),
          ("ftp", 3))
    )


_SmSoftwareTransferDevice_Type.__name__ = "Integer32"
_SmSoftwareTransferDevice_Object = MibScalar
smSoftwareTransferDevice = _SmSoftwareTransferDevice_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 8, 1, 10, 4, 1),
    _SmSoftwareTransferDevice_Type()
)
smSoftwareTransferDevice.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    smSoftwareTransferDevice.setStatus("current")


class _SmSoftwareTransferHostname_Type(OctetString):
    """Custom type smSoftwareTransferHostname based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_SmSoftwareTransferHostname_Type.__name__ = "OctetString"
_SmSoftwareTransferHostname_Object = MibScalar
smSoftwareTransferHostname = _SmSoftwareTransferHostname_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 8, 1, 10, 4, 2),
    _SmSoftwareTransferHostname_Type()
)
smSoftwareTransferHostname.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    smSoftwareTransferHostname.setStatus("current")


class _SmSoftwareTransferUsername_Type(OctetString):
    """Custom type smSoftwareTransferUsername based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_SmSoftwareTransferUsername_Type.__name__ = "OctetString"
_SmSoftwareTransferUsername_Object = MibScalar
smSoftwareTransferUsername = _SmSoftwareTransferUsername_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 8, 1, 10, 4, 3),
    _SmSoftwareTransferUsername_Type()
)
smSoftwareTransferUsername.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    smSoftwareTransferUsername.setStatus("current")


class _SmSoftwareTransferPassword_Type(OctetString):
    """Custom type smSoftwareTransferPassword based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_SmSoftwareTransferPassword_Type.__name__ = "OctetString"
_SmSoftwareTransferPassword_Object = MibScalar
smSoftwareTransferPassword = _SmSoftwareTransferPassword_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 8, 1, 10, 4, 4),
    _SmSoftwareTransferPassword_Type()
)
smSoftwareTransferPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    smSoftwareTransferPassword.setStatus("current")


class _SmSoftwareTransferPath_Type(OctetString):
    """Custom type smSoftwareTransferPath based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_SmSoftwareTransferPath_Type.__name__ = "OctetString"
_SmSoftwareTransferPath_Object = MibScalar
smSoftwareTransferPath = _SmSoftwareTransferPath_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 8, 1, 10, 4, 5),
    _SmSoftwareTransferPath_Type()
)
smSoftwareTransferPath.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    smSoftwareTransferPath.setStatus("current")


class _SmSoftwareTransferControl_Type(Integer32):
    """Custom type smSoftwareTransferControl based on Integer32"""
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
        *(("abort", 1),
          ("download", 2),
          ("upload", 3),
          ("downloadAsBoot", 4))
    )


_SmSoftwareTransferControl_Type.__name__ = "Integer32"
_SmSoftwareTransferControl_Object = MibScalar
smSoftwareTransferControl = _SmSoftwareTransferControl_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 8, 1, 10, 4, 6),
    _SmSoftwareTransferControl_Type()
)
smSoftwareTransferControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    smSoftwareTransferControl.setStatus("current")


class _SmSoftwareTransferStatus_Type(Integer32):
    """Custom type smSoftwareTransferStatus based on Integer32"""
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
        *(("none", 1),
          ("inprogress", 2),
          ("finished", 3),
          ("filenameError", 4),
          ("hostnameError", 5),
          ("tooManyImages", 6))
    )


_SmSoftwareTransferStatus_Type.__name__ = "Integer32"
_SmSoftwareTransferStatus_Object = MibScalar
smSoftwareTransferStatus = _SmSoftwareTransferStatus_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 8, 1, 10, 4, 7),
    _SmSoftwareTransferStatus_Type()
)
smSoftwareTransferStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smSoftwareTransferStatus.setStatus("current")
_SmConfigFileTransferGroup_ObjectIdentity = ObjectIdentity
smConfigFileTransferGroup = _SmConfigFileTransferGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4115, 1, 8, 1, 10, 5)
)


class _SmConfigFileTransferDevice_Type(Integer32):
    """Custom type smConfigFileTransferDevice based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("nfs", 1),
          ("tftp", 2),
          ("ftp", 3))
    )


_SmConfigFileTransferDevice_Type.__name__ = "Integer32"
_SmConfigFileTransferDevice_Object = MibScalar
smConfigFileTransferDevice = _SmConfigFileTransferDevice_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 8, 1, 10, 5, 1),
    _SmConfigFileTransferDevice_Type()
)
smConfigFileTransferDevice.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    smConfigFileTransferDevice.setStatus("current")


class _SmConfigFileTransferHostname_Type(OctetString):
    """Custom type smConfigFileTransferHostname based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_SmConfigFileTransferHostname_Type.__name__ = "OctetString"
_SmConfigFileTransferHostname_Object = MibScalar
smConfigFileTransferHostname = _SmConfigFileTransferHostname_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 8, 1, 10, 5, 2),
    _SmConfigFileTransferHostname_Type()
)
smConfigFileTransferHostname.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    smConfigFileTransferHostname.setStatus("current")


class _SmConfigFileTransferUsername_Type(OctetString):
    """Custom type smConfigFileTransferUsername based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_SmConfigFileTransferUsername_Type.__name__ = "OctetString"
_SmConfigFileTransferUsername_Object = MibScalar
smConfigFileTransferUsername = _SmConfigFileTransferUsername_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 8, 1, 10, 5, 3),
    _SmConfigFileTransferUsername_Type()
)
smConfigFileTransferUsername.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    smConfigFileTransferUsername.setStatus("current")


class _SmConfigFileTransferPassword_Type(OctetString):
    """Custom type smConfigFileTransferPassword based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_SmConfigFileTransferPassword_Type.__name__ = "OctetString"
_SmConfigFileTransferPassword_Object = MibScalar
smConfigFileTransferPassword = _SmConfigFileTransferPassword_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 8, 1, 10, 5, 4),
    _SmConfigFileTransferPassword_Type()
)
smConfigFileTransferPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    smConfigFileTransferPassword.setStatus("current")


class _SmConfigFileTransferPath_Type(OctetString):
    """Custom type smConfigFileTransferPath based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_SmConfigFileTransferPath_Type.__name__ = "OctetString"
_SmConfigFileTransferPath_Object = MibScalar
smConfigFileTransferPath = _SmConfigFileTransferPath_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 8, 1, 10, 5, 5),
    _SmConfigFileTransferPath_Type()
)
smConfigFileTransferPath.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    smConfigFileTransferPath.setStatus("current")


class _SmConfigFileTransferTargetPath_Type(OctetString):
    """Custom type smConfigFileTransferTargetPath based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_SmConfigFileTransferTargetPath_Type.__name__ = "OctetString"
_SmConfigFileTransferTargetPath_Object = MibScalar
smConfigFileTransferTargetPath = _SmConfigFileTransferTargetPath_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 8, 1, 10, 5, 6),
    _SmConfigFileTransferTargetPath_Type()
)
smConfigFileTransferTargetPath.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    smConfigFileTransferTargetPath.setStatus("current")


class _SmConfigFileTransferControl_Type(Integer32):
    """Custom type smConfigFileTransferControl based on Integer32"""
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
        *(("abort", 1),
          ("download", 2),
          ("upload", 3),
          ("downloadAsStartup", 4),
          ("downloadIntoRunning", 5))
    )


_SmConfigFileTransferControl_Type.__name__ = "Integer32"
_SmConfigFileTransferControl_Object = MibScalar
smConfigFileTransferControl = _SmConfigFileTransferControl_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 8, 1, 10, 5, 7),
    _SmConfigFileTransferControl_Type()
)
smConfigFileTransferControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    smConfigFileTransferControl.setStatus("current")


class _SmConfigFileTransferStatus_Type(Integer32):
    """Custom type smConfigFileTransferStatus based on Integer32"""
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
        *(("none", 1),
          ("inprogress", 2),
          ("finished", 3),
          ("filenameError", 4),
          ("hostnameError", 5),
          ("tooManyFiles", 6))
    )


_SmConfigFileTransferStatus_Type.__name__ = "Integer32"
_SmConfigFileTransferStatus_Object = MibScalar
smConfigFileTransferStatus = _SmConfigFileTransferStatus_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 8, 1, 10, 5, 8),
    _SmConfigFileTransferStatus_Type()
)
smConfigFileTransferStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smConfigFileTransferStatus.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ARRIS-D5-SOFTWARE-MGR-MIB",
    **{"softwareManagerMIB": softwareManagerMIB,
       "smControlGroup": smControlGroup,
       "smReloadAction": smReloadAction,
       "smConfigFileAction": smConfigFileAction,
       "smSoftwareListGroup": smSoftwareListGroup,
       "smSoftwareListTable": smSoftwareListTable,
       "smSoftwareListEntry": smSoftwareListEntry,
       "smSoftwareEntryIndex": smSoftwareEntryIndex,
       "smSoftwareEntryFilename": smSoftwareEntryFilename,
       "smSoftwareEntryVersion": smSoftwareEntryVersion,
       "smSoftwareEntryDate": smSoftwareEntryDate,
       "smSoftwareEntryState": smSoftwareEntryState,
       "smSoftwareEntrySize": smSoftwareEntrySize,
       "smSoftwareEntryStatus": smSoftwareEntryStatus,
       "smSoftwareEntryAction": smSoftwareEntryAction,
       "smConfigFileListGroup": smConfigFileListGroup,
       "smConfigFileListTable": smConfigFileListTable,
       "smConfigFileListEntry": smConfigFileListEntry,
       "smConfigFileEntryIndex": smConfigFileEntryIndex,
       "smConfigFileEntryName": smConfigFileEntryName,
       "smConfigFileTimestamp": smConfigFileTimestamp,
       "smConfigFileEntryAction": smConfigFileEntryAction,
       "smSoftwareTransferGroup": smSoftwareTransferGroup,
       "smSoftwareTransferDevice": smSoftwareTransferDevice,
       "smSoftwareTransferHostname": smSoftwareTransferHostname,
       "smSoftwareTransferUsername": smSoftwareTransferUsername,
       "smSoftwareTransferPassword": smSoftwareTransferPassword,
       "smSoftwareTransferPath": smSoftwareTransferPath,
       "smSoftwareTransferControl": smSoftwareTransferControl,
       "smSoftwareTransferStatus": smSoftwareTransferStatus,
       "smConfigFileTransferGroup": smConfigFileTransferGroup,
       "smConfigFileTransferDevice": smConfigFileTransferDevice,
       "smConfigFileTransferHostname": smConfigFileTransferHostname,
       "smConfigFileTransferUsername": smConfigFileTransferUsername,
       "smConfigFileTransferPassword": smConfigFileTransferPassword,
       "smConfigFileTransferPath": smConfigFileTransferPath,
       "smConfigFileTransferTargetPath": smConfigFileTransferTargetPath,
       "smConfigFileTransferControl": smConfigFileTransferControl,
       "smConfigFileTransferStatus": smConfigFileTransferStatus}
)
