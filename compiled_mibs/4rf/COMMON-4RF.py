# SNMP MIB module (COMMON-4RF) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\4rf\COMMON-4RF

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

(FourRFFileSize,
 FourRFImageStatus,
 FourRFImageType,
 FourRFImageVersion,
 FourRFProcessResultType,
 FourRFResetType,
 FourRFSerialNumber,
 FourRFTftpFileName,
 FourRFTimeZone,
 FourRFWebUserEnabled,
 FourRFWebUserGroup) = mibBuilder.importSymbols(
    "COMMON-TC-4RF",
    "FourRFFileSize",
    "FourRFImageStatus",
    "FourRFImageType",
    "FourRFImageVersion",
    "FourRFProcessResultType",
    "FourRFResetType",
    "FourRFSerialNumber",
    "FourRFTftpFileName",
    "FourRFTimeZone",
    "FourRFWebUserEnabled",
    "FourRFWebUserGroup")

(fourRFGeneric,
 fourRFModules) = mibBuilder.importSymbols(
    "MIB-4RF",
    "fourRFGeneric",
    "fourRFModules")

(fourRFCommon,) = mibBuilder.importSymbols(
    "PRODUCTS-MIB-4RF",
    "fourRFCommon")

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

(DateAndTime,
 DisplayString,
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

fourRFCommonModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 14817, 2, 3)
)
if mibBuilder.loadTexts:
    fourRFCommonModule.setRevisions(
        ("2007-04-30 00:00",
         "2005-02-11 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_FourRFGroups_ObjectIdentity = ObjectIdentity
fourRFGroups = _FourRFGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14817, 7, 1, 1)
)
if mibBuilder.loadTexts:
    fourRFGroups.setStatus("current")
_FourRFObjects_ObjectIdentity = ObjectIdentity
fourRFObjects = _FourRFObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14817, 7, 1, 2)
)
if mibBuilder.loadTexts:
    fourRFObjects.setStatus("current")
_FourRFSystem_ObjectIdentity = ObjectIdentity
fourRFSystem = _FourRFSystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14817, 7, 1, 2, 1)
)


class _FourRFSystemID_Type(DisplayString):
    """Custom type fourRFSystemID based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_FourRFSystemID_Type.__name__ = "DisplayString"
_FourRFSystemID_Object = MibScalar
fourRFSystemID = _FourRFSystemID_Object(
    (1, 3, 6, 1, 4, 1, 14817, 7, 1, 2, 1, 1),
    _FourRFSystemID_Type()
)
fourRFSystemID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fourRFSystemID.setStatus("current")
_FourRFSystemSoftwareVersion_Type = FourRFImageVersion
_FourRFSystemSoftwareVersion_Object = MibScalar
fourRFSystemSoftwareVersion = _FourRFSystemSoftwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 14817, 7, 1, 2, 1, 2),
    _FourRFSystemSoftwareVersion_Type()
)
fourRFSystemSoftwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fourRFSystemSoftwareVersion.setStatus("current")
_FourRFSystemIpAddress_Type = IpAddress
_FourRFSystemIpAddress_Object = MibScalar
fourRFSystemIpAddress = _FourRFSystemIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 14817, 7, 1, 2, 1, 3),
    _FourRFSystemIpAddress_Type()
)
fourRFSystemIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fourRFSystemIpAddress.setStatus("current")
_FourRFSystemRemoteIpAddress_Type = IpAddress
_FourRFSystemRemoteIpAddress_Object = MibScalar
fourRFSystemRemoteIpAddress = _FourRFSystemRemoteIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 14817, 7, 1, 2, 1, 4),
    _FourRFSystemRemoteIpAddress_Type()
)
fourRFSystemRemoteIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fourRFSystemRemoteIpAddress.setStatus("current")
_FourRFSystemSubnetMask_Type = IpAddress
_FourRFSystemSubnetMask_Object = MibScalar
fourRFSystemSubnetMask = _FourRFSystemSubnetMask_Object(
    (1, 3, 6, 1, 4, 1, 14817, 7, 1, 2, 1, 5),
    _FourRFSystemSubnetMask_Type()
)
fourRFSystemSubnetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fourRFSystemSubnetMask.setStatus("current")
_FourRFSystemDefaultGateway_Type = IpAddress
_FourRFSystemDefaultGateway_Object = MibScalar
fourRFSystemDefaultGateway = _FourRFSystemDefaultGateway_Object(
    (1, 3, 6, 1, 4, 1, 14817, 7, 1, 2, 1, 6),
    _FourRFSystemDefaultGateway_Type()
)
fourRFSystemDefaultGateway.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fourRFSystemDefaultGateway.setStatus("current")


class _FourRFSystemIpAssignment_Type(Integer32):
    """Custom type fourRFSystemIpAssignment based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("useDHCP", 0),
          ("userAssigned", 1))
    )


_FourRFSystemIpAssignment_Type.__name__ = "Integer32"
_FourRFSystemIpAssignment_Object = MibScalar
fourRFSystemIpAssignment = _FourRFSystemIpAssignment_Object(
    (1, 3, 6, 1, 4, 1, 14817, 7, 1, 2, 1, 7),
    _FourRFSystemIpAssignment_Type()
)
fourRFSystemIpAssignment.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fourRFSystemIpAssignment.setStatus("current")
_FourRFSystemDateAndTime_Type = Unsigned32
_FourRFSystemDateAndTime_Object = MibScalar
fourRFSystemDateAndTime = _FourRFSystemDateAndTime_Object(
    (1, 3, 6, 1, 4, 1, 14817, 7, 1, 2, 1, 8),
    _FourRFSystemDateAndTime_Type()
)
fourRFSystemDateAndTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fourRFSystemDateAndTime.setStatus("current")
_FourRFSystemTftpServerAddress_Type = IpAddress
_FourRFSystemTftpServerAddress_Object = MibScalar
fourRFSystemTftpServerAddress = _FourRFSystemTftpServerAddress_Object(
    (1, 3, 6, 1, 4, 1, 14817, 7, 1, 2, 1, 9),
    _FourRFSystemTftpServerAddress_Type()
)
fourRFSystemTftpServerAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fourRFSystemTftpServerAddress.setStatus("current")
_FourRFSystemSerialNumber_Type = FourRFSerialNumber
_FourRFSystemSerialNumber_Object = MibScalar
fourRFSystemSerialNumber = _FourRFSystemSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 14817, 7, 1, 2, 1, 10),
    _FourRFSystemSerialNumber_Type()
)
fourRFSystemSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fourRFSystemSerialNumber.setStatus("current")
_FourRFSystemLastReset_Type = FourRFResetType
_FourRFSystemLastReset_Object = MibScalar
fourRFSystemLastReset = _FourRFSystemLastReset_Object(
    (1, 3, 6, 1, 4, 1, 14817, 7, 1, 2, 1, 11),
    _FourRFSystemLastReset_Type()
)
fourRFSystemLastReset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fourRFSystemLastReset.setStatus("current")
_FourRFSystemTimeZone_Type = Integer32
_FourRFSystemTimeZone_Object = MibScalar
fourRFSystemTimeZone = _FourRFSystemTimeZone_Object(
    (1, 3, 6, 1, 4, 1, 14817, 7, 1, 2, 1, 12),
    _FourRFSystemTimeZone_Type()
)
fourRFSystemTimeZone.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fourRFSystemTimeZone.setStatus("current")
_FourRFSystemSyslogAddress_Type = IpAddress
_FourRFSystemSyslogAddress_Object = MibScalar
fourRFSystemSyslogAddress = _FourRFSystemSyslogAddress_Object(
    (1, 3, 6, 1, 4, 1, 14817, 7, 1, 2, 1, 13),
    _FourRFSystemSyslogAddress_Type()
)
fourRFSystemSyslogAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fourRFSystemSyslogAddress.setStatus("current")
_FourRFSystemSyslogPort_Type = Unsigned32
_FourRFSystemSyslogPort_Object = MibScalar
fourRFSystemSyslogPort = _FourRFSystemSyslogPort_Object(
    (1, 3, 6, 1, 4, 1, 14817, 7, 1, 2, 1, 14),
    _FourRFSystemSyslogPort_Type()
)
fourRFSystemSyslogPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fourRFSystemSyslogPort.setStatus("current")


class _FourRFSystemTimeDaylightSavings_Type(Integer32):
    """Custom type fourRFSystemTimeDaylightSavings based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("daylightSavingsDisabled", 0),
          ("daylightSavingsEnabled", 1))
    )


_FourRFSystemTimeDaylightSavings_Type.__name__ = "Integer32"
_FourRFSystemTimeDaylightSavings_Object = MibScalar
fourRFSystemTimeDaylightSavings = _FourRFSystemTimeDaylightSavings_Object(
    (1, 3, 6, 1, 4, 1, 14817, 7, 1, 2, 1, 15),
    _FourRFSystemTimeDaylightSavings_Type()
)
fourRFSystemTimeDaylightSavings.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fourRFSystemTimeDaylightSavings.setStatus("current")
_FourRFSystemTimeZoneGMTOffset_Type = FourRFTimeZone
_FourRFSystemTimeZoneGMTOffset_Object = MibScalar
fourRFSystemTimeZoneGMTOffset = _FourRFSystemTimeZoneGMTOffset_Object(
    (1, 3, 6, 1, 4, 1, 14817, 7, 1, 2, 1, 16),
    _FourRFSystemTimeZoneGMTOffset_Type()
)
fourRFSystemTimeZoneGMTOffset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fourRFSystemTimeZoneGMTOffset.setStatus("current")


class _FourRFSystemMACAddress_Type(DisplayString):
    """Custom type fourRFSystemMACAddress based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_FourRFSystemMACAddress_Type.__name__ = "DisplayString"
_FourRFSystemMACAddress_Object = MibScalar
fourRFSystemMACAddress = _FourRFSystemMACAddress_Object(
    (1, 3, 6, 1, 4, 1, 14817, 7, 1, 2, 1, 17),
    _FourRFSystemMACAddress_Type()
)
fourRFSystemMACAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fourRFSystemMACAddress.setStatus("current")
_FourRFSystemLocalRadioBIpAddress_Type = IpAddress
_FourRFSystemLocalRadioBIpAddress_Object = MibScalar
fourRFSystemLocalRadioBIpAddress = _FourRFSystemLocalRadioBIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 14817, 7, 1, 2, 1, 18),
    _FourRFSystemLocalRadioBIpAddress_Type()
)
fourRFSystemLocalRadioBIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fourRFSystemLocalRadioBIpAddress.setStatus("current")
_FourRFSystemRemoteRadioBIpAddress_Type = IpAddress
_FourRFSystemRemoteRadioBIpAddress_Object = MibScalar
fourRFSystemRemoteRadioBIpAddress = _FourRFSystemRemoteRadioBIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 14817, 7, 1, 2, 1, 19),
    _FourRFSystemRemoteRadioBIpAddress_Type()
)
fourRFSystemRemoteRadioBIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fourRFSystemRemoteRadioBIpAddress.setStatus("current")
_FourRFSystemLocalRadioAIpAddress_Type = IpAddress
_FourRFSystemLocalRadioAIpAddress_Object = MibScalar
fourRFSystemLocalRadioAIpAddress = _FourRFSystemLocalRadioAIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 14817, 7, 1, 2, 1, 20),
    _FourRFSystemLocalRadioAIpAddress_Type()
)
fourRFSystemLocalRadioAIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fourRFSystemLocalRadioAIpAddress.setStatus("current")
_FourRFReset_ObjectIdentity = ObjectIdentity
fourRFReset = _FourRFReset_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14817, 7, 1, 2, 2)
)


class _FourRFResetType_Type(Integer32):
    """Custom type fourRFResetType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("softReset", 1),
          ("hardReset", 2))
    )


_FourRFResetType_Type.__name__ = "Integer32"
_FourRFResetType_Object = MibScalar
fourRFResetType = _FourRFResetType_Object(
    (1, 3, 6, 1, 4, 1, 14817, 7, 1, 2, 2, 1),
    _FourRFResetType_Type()
)
fourRFResetType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fourRFResetType.setStatus("current")
_FourRFResetTime_Type = Unsigned32
_FourRFResetTime_Object = MibScalar
fourRFResetTime = _FourRFResetTime_Object(
    (1, 3, 6, 1, 4, 1, 14817, 7, 1, 2, 2, 2),
    _FourRFResetTime_Type()
)
fourRFResetTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fourRFResetTime.setStatus("current")


class _FourRFResetCommand_Type(Integer32):
    """Custom type fourRFResetCommand based on Integer32"""
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
        *(("none", 0),
          ("resetNow", 1),
          ("timedReset", 2),
          ("cancelReset", 3))
    )


_FourRFResetCommand_Type.__name__ = "Integer32"
_FourRFResetCommand_Object = MibScalar
fourRFResetCommand = _FourRFResetCommand_Object(
    (1, 3, 6, 1, 4, 1, 14817, 7, 1, 2, 2, 3),
    _FourRFResetCommand_Type()
)
fourRFResetCommand.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fourRFResetCommand.setStatus("current")
_FourRFMibBackup_ObjectIdentity = ObjectIdentity
fourRFMibBackup = _FourRFMibBackup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14817, 7, 1, 2, 3)
)
_FourRFMibBackupFile_Type = FourRFTftpFileName
_FourRFMibBackupFile_Object = MibScalar
fourRFMibBackupFile = _FourRFMibBackupFile_Object(
    (1, 3, 6, 1, 4, 1, 14817, 7, 1, 2, 3, 1),
    _FourRFMibBackupFile_Type()
)
fourRFMibBackupFile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fourRFMibBackupFile.setStatus("current")


class _FourRFMibBackupCommand_Type(Integer32):
    """Custom type fourRFMibBackupCommand based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("remoteBackup", 1),
          ("localBackup", 2))
    )


_FourRFMibBackupCommand_Type.__name__ = "Integer32"
_FourRFMibBackupCommand_Object = MibScalar
fourRFMibBackupCommand = _FourRFMibBackupCommand_Object(
    (1, 3, 6, 1, 4, 1, 14817, 7, 1, 2, 3, 2),
    _FourRFMibBackupCommand_Type()
)
fourRFMibBackupCommand.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fourRFMibBackupCommand.setStatus("current")
_FourRFMibBackupResult_Type = FourRFProcessResultType
_FourRFMibBackupResult_Object = MibScalar
fourRFMibBackupResult = _FourRFMibBackupResult_Object(
    (1, 3, 6, 1, 4, 1, 14817, 7, 1, 2, 3, 3),
    _FourRFMibBackupResult_Type()
)
fourRFMibBackupResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fourRFMibBackupResult.setStatus("current")
_FourRFUpload_ObjectIdentity = ObjectIdentity
fourRFUpload = _FourRFUpload_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14817, 7, 1, 2, 4)
)
_FourRFUploadType_Type = FourRFImageType
_FourRFUploadType_Object = MibScalar
fourRFUploadType = _FourRFUploadType_Object(
    (1, 3, 6, 1, 4, 1, 14817, 7, 1, 2, 4, 1),
    _FourRFUploadType_Type()
)
fourRFUploadType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fourRFUploadType.setStatus("current")
_FourRFUploadFile_Type = FourRFTftpFileName
_FourRFUploadFile_Object = MibScalar
fourRFUploadFile = _FourRFUploadFile_Object(
    (1, 3, 6, 1, 4, 1, 14817, 7, 1, 2, 4, 2),
    _FourRFUploadFile_Type()
)
fourRFUploadFile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fourRFUploadFile.setStatus("current")


class _FourRFUploadCommand_Type(Integer32):
    """Custom type fourRFUploadCommand based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("upload", 1))
    )


_FourRFUploadCommand_Type.__name__ = "Integer32"
_FourRFUploadCommand_Object = MibScalar
fourRFUploadCommand = _FourRFUploadCommand_Object(
    (1, 3, 6, 1, 4, 1, 14817, 7, 1, 2, 4, 3),
    _FourRFUploadCommand_Type()
)
fourRFUploadCommand.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fourRFUploadCommand.setStatus("current")
_FourRFUploadResult_Type = FourRFProcessResultType
_FourRFUploadResult_Object = MibScalar
fourRFUploadResult = _FourRFUploadResult_Object(
    (1, 3, 6, 1, 4, 1, 14817, 7, 1, 2, 4, 4),
    _FourRFUploadResult_Type()
)
fourRFUploadResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fourRFUploadResult.setStatus("current")
_FourRFImageTable_Object = MibTable
fourRFImageTable = _FourRFImageTable_Object(
    (1, 3, 6, 1, 4, 1, 14817, 7, 1, 2, 5)
)
if mibBuilder.loadTexts:
    fourRFImageTable.setStatus("current")
_FourRFImageTableEntry_Object = MibTableRow
fourRFImageTableEntry = _FourRFImageTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 14817, 7, 1, 2, 5, 1)
)
fourRFImageTableEntry.setIndexNames(
    (0, "COMMON-4RF", "fourRFImageIndex"),
)
if mibBuilder.loadTexts:
    fourRFImageTableEntry.setStatus("current")
_FourRFImageIndex_Type = Integer32
_FourRFImageIndex_Object = MibTableColumn
fourRFImageIndex = _FourRFImageIndex_Object(
    (1, 3, 6, 1, 4, 1, 14817, 7, 1, 2, 5, 1, 1),
    _FourRFImageIndex_Type()
)
fourRFImageIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fourRFImageIndex.setStatus("current")
_FourRFImageType_Type = FourRFImageType
_FourRFImageType_Object = MibTableColumn
fourRFImageType = _FourRFImageType_Object(
    (1, 3, 6, 1, 4, 1, 14817, 7, 1, 2, 5, 1, 2),
    _FourRFImageType_Type()
)
fourRFImageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fourRFImageType.setStatus("current")
_FourRFImageStatus_Type = FourRFImageStatus
_FourRFImageStatus_Object = MibTableColumn
fourRFImageStatus = _FourRFImageStatus_Object(
    (1, 3, 6, 1, 4, 1, 14817, 7, 1, 2, 5, 1, 3),
    _FourRFImageStatus_Type()
)
fourRFImageStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fourRFImageStatus.setStatus("current")
_FourRFImageSize_Type = FourRFFileSize
_FourRFImageSize_Object = MibTableColumn
fourRFImageSize = _FourRFImageSize_Object(
    (1, 3, 6, 1, 4, 1, 14817, 7, 1, 2, 5, 1, 4),
    _FourRFImageSize_Type()
)
fourRFImageSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fourRFImageSize.setStatus("current")
_FourRFImageVersion_Type = FourRFImageVersion
_FourRFImageVersion_Object = MibTableColumn
fourRFImageVersion = _FourRFImageVersion_Object(
    (1, 3, 6, 1, 4, 1, 14817, 7, 1, 2, 5, 1, 5),
    _FourRFImageVersion_Type()
)
fourRFImageVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fourRFImageVersion.setStatus("current")
_FourRFImageControl_ObjectIdentity = ObjectIdentity
fourRFImageControl = _FourRFImageControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14817, 7, 1, 2, 6)
)
_FourRFImageTableIndex_Type = Integer32
_FourRFImageTableIndex_Object = MibScalar
fourRFImageTableIndex = _FourRFImageTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 14817, 7, 1, 2, 6, 1),
    _FourRFImageTableIndex_Type()
)
fourRFImageTableIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fourRFImageTableIndex.setStatus("current")


class _FourRFImageTableCommand_Type(Integer32):
    """Custom type fourRFImageTableCommand based on Integer32"""
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
        *(("none", 0),
          ("deactivateImage", 1),
          ("activateImage", 2),
          ("deleteImage", 3))
    )


_FourRFImageTableCommand_Type.__name__ = "Integer32"
_FourRFImageTableCommand_Object = MibScalar
fourRFImageTableCommand = _FourRFImageTableCommand_Object(
    (1, 3, 6, 1, 4, 1, 14817, 7, 1, 2, 6, 2),
    _FourRFImageTableCommand_Type()
)
fourRFImageTableCommand.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fourRFImageTableCommand.setStatus("current")
_FourRFWebUserManagementTable_Object = MibTable
fourRFWebUserManagementTable = _FourRFWebUserManagementTable_Object(
    (1, 3, 6, 1, 4, 1, 14817, 7, 1, 2, 7)
)
if mibBuilder.loadTexts:
    fourRFWebUserManagementTable.setStatus("current")
_FourRFWebUserEntry_Object = MibTableRow
fourRFWebUserEntry = _FourRFWebUserEntry_Object(
    (1, 3, 6, 1, 4, 1, 14817, 7, 1, 2, 7, 1)
)
fourRFWebUserEntry.setIndexNames(
    (0, "COMMON-4RF", "fourRFWebUserIndex"),
)
if mibBuilder.loadTexts:
    fourRFWebUserEntry.setStatus("current")


class _FourRFWebUserIndex_Type(Integer32):
    """Custom type fourRFWebUserIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10),
    )


_FourRFWebUserIndex_Type.__name__ = "Integer32"
_FourRFWebUserIndex_Object = MibTableColumn
fourRFWebUserIndex = _FourRFWebUserIndex_Object(
    (1, 3, 6, 1, 4, 1, 14817, 7, 1, 2, 7, 1, 1),
    _FourRFWebUserIndex_Type()
)
fourRFWebUserIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fourRFWebUserIndex.setStatus("current")


class _FourRFWebUserName_Type(DisplayString):
    """Custom type fourRFWebUserName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_FourRFWebUserName_Type.__name__ = "DisplayString"
_FourRFWebUserName_Object = MibTableColumn
fourRFWebUserName = _FourRFWebUserName_Object(
    (1, 3, 6, 1, 4, 1, 14817, 7, 1, 2, 7, 1, 2),
    _FourRFWebUserName_Type()
)
fourRFWebUserName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fourRFWebUserName.setStatus("current")


class _FourRFWebUserPassword_Type(OctetString):
    """Custom type fourRFWebUserPassword based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 32),
    )


_FourRFWebUserPassword_Type.__name__ = "OctetString"
_FourRFWebUserPassword_Object = MibTableColumn
fourRFWebUserPassword = _FourRFWebUserPassword_Object(
    (1, 3, 6, 1, 4, 1, 14817, 7, 1, 2, 7, 1, 3),
    _FourRFWebUserPassword_Type()
)
fourRFWebUserPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fourRFWebUserPassword.setStatus("current")
_FourRFWebUserGroup_Type = FourRFWebUserGroup
_FourRFWebUserGroup_Object = MibTableColumn
fourRFWebUserGroup = _FourRFWebUserGroup_Object(
    (1, 3, 6, 1, 4, 1, 14817, 7, 1, 2, 7, 1, 4),
    _FourRFWebUserGroup_Type()
)
fourRFWebUserGroup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fourRFWebUserGroup.setStatus("current")
_FourRFWebUserEnabled_Type = FourRFWebUserEnabled
_FourRFWebUserEnabled_Object = MibTableColumn
fourRFWebUserEnabled = _FourRFWebUserEnabled_Object(
    (1, 3, 6, 1, 4, 1, 14817, 7, 1, 2, 7, 1, 5),
    _FourRFWebUserEnabled_Type()
)
fourRFWebUserEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fourRFWebUserEnabled.setStatus("current")


class _FourRFWebUserPasswordConfirm_Type(OctetString):
    """Custom type fourRFWebUserPasswordConfirm based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 32),
    )


_FourRFWebUserPasswordConfirm_Type.__name__ = "OctetString"
_FourRFWebUserPasswordConfirm_Object = MibTableColumn
fourRFWebUserPasswordConfirm = _FourRFWebUserPasswordConfirm_Object(
    (1, 3, 6, 1, 4, 1, 14817, 7, 1, 2, 7, 1, 6),
    _FourRFWebUserPasswordConfirm_Type()
)
fourRFWebUserPasswordConfirm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fourRFWebUserPasswordConfirm.setStatus("current")
_FourRFEvents_ObjectIdentity = ObjectIdentity
fourRFEvents = _FourRFEvents_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14817, 7, 1, 3)
)
if mibBuilder.loadTexts:
    fourRFEvents.setStatus("current")
_FourRFEventsV2_ObjectIdentity = ObjectIdentity
fourRFEventsV2 = _FourRFEventsV2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14817, 7, 1, 3, 0)
)
if mibBuilder.loadTexts:
    fourRFEventsV2.setStatus("current")

# Managed Objects groups

fourRFSystemGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 14817, 7, 1, 1, 1)
)
fourRFSystemGroup.setObjects(
      *(("COMMON-4RF", "fourRFSystemID"),
        ("COMMON-4RF", "fourRFSystemSoftwareVersion"),
        ("COMMON-4RF", "fourRFSystemIpAddress"),
        ("COMMON-4RF", "fourRFSystemRemoteIpAddress"),
        ("COMMON-4RF", "fourRFSystemSubnetMask"),
        ("COMMON-4RF", "fourRFSystemDefaultGateway"),
        ("COMMON-4RF", "fourRFSystemIpAssignment"),
        ("COMMON-4RF", "fourRFSystemDateAndTime"),
        ("COMMON-4RF", "fourRFSystemTftpServerAddress"),
        ("COMMON-4RF", "fourRFSystemSerialNumber"),
        ("COMMON-4RF", "fourRFSystemLastReset"),
        ("COMMON-4RF", "fourRFSystemTimeZone"),
        ("COMMON-4RF", "fourRFSystemSyslogAddress"),
        ("COMMON-4RF", "fourRFSystemSyslogPort"),
        ("COMMON-4RF", "fourRFSystemTimeDaylightSavings"),
        ("COMMON-4RF", "fourRFSystemTimeZoneGMTOffset"),
        ("COMMON-4RF", "fourRFSystemMACAddress"),
        ("COMMON-4RF", "fourRFSystemLocalRadioBIpAddress"),
        ("COMMON-4RF", "fourRFSystemRemoteRadioBIpAddress"),
        ("COMMON-4RF", "fourRFSystemLocalRadioAIpAddress"))
)
if mibBuilder.loadTexts:
    fourRFSystemGroup.setStatus("current")

fourRFResetGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 14817, 7, 1, 1, 2)
)
fourRFResetGroup.setObjects(
      *(("COMMON-4RF", "fourRFResetType"),
        ("COMMON-4RF", "fourRFResetTime"),
        ("COMMON-4RF", "fourRFResetCommand"))
)
if mibBuilder.loadTexts:
    fourRFResetGroup.setStatus("current")

fourRFMibBackupGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 14817, 7, 1, 1, 3)
)
fourRFMibBackupGroup.setObjects(
      *(("COMMON-4RF", "fourRFMibBackupFile"),
        ("COMMON-4RF", "fourRFMibBackupCommand"),
        ("COMMON-4RF", "fourRFMibBackupResult"))
)
if mibBuilder.loadTexts:
    fourRFMibBackupGroup.setStatus("current")

fourRFUploadGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 14817, 7, 1, 1, 4)
)
fourRFUploadGroup.setObjects(
      *(("COMMON-4RF", "fourRFUploadType"),
        ("COMMON-4RF", "fourRFUploadFile"),
        ("COMMON-4RF", "fourRFUploadCommand"),
        ("COMMON-4RF", "fourRFUploadResult"))
)
if mibBuilder.loadTexts:
    fourRFUploadGroup.setStatus("current")

fourRFImageControlGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 14817, 7, 1, 1, 6)
)
fourRFImageControlGroup.setObjects(
      *(("COMMON-4RF", "fourRFImageTableIndex"),
        ("COMMON-4RF", "fourRFImageTableCommand"))
)
if mibBuilder.loadTexts:
    fourRFImageControlGroup.setStatus("current")


# Notification objects

fourRFResetEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 14817, 7, 1, 3, 0, 1)
)
fourRFResetEvent.setObjects(
    ("COMMON-4RF", "fourRFResetType")
)
if mibBuilder.loadTexts:
    fourRFResetEvent.setStatus(
        "current"
    )

fourRFMibBackupStatusEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 14817, 7, 1, 3, 0, 2)
)
fourRFMibBackupStatusEvent.setObjects(
      *(("COMMON-4RF", "fourRFMibBackupFile"),
        ("COMMON-4RF", "fourRFMibBackupCommand"),
        ("COMMON-4RF", "fourRFMibBackupResult"))
)
if mibBuilder.loadTexts:
    fourRFMibBackupStatusEvent.setStatus(
        "current"
    )

fouRFUploadStatusEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 14817, 7, 1, 3, 0, 3)
)
fouRFUploadStatusEvent.setObjects(
      *(("COMMON-4RF", "fourRFUploadFile"),
        ("COMMON-4RF", "fourRFUploadType"),
        ("COMMON-4RF", "fourRFUploadResult"))
)
if mibBuilder.loadTexts:
    fouRFUploadStatusEvent.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "COMMON-4RF",
    **{"fourRFCommonModule": fourRFCommonModule,
       "fourRFGroups": fourRFGroups,
       "fourRFSystemGroup": fourRFSystemGroup,
       "fourRFResetGroup": fourRFResetGroup,
       "fourRFMibBackupGroup": fourRFMibBackupGroup,
       "fourRFUploadGroup": fourRFUploadGroup,
       "fourRFImageControlGroup": fourRFImageControlGroup,
       "fourRFObjects": fourRFObjects,
       "fourRFSystem": fourRFSystem,
       "fourRFSystemID": fourRFSystemID,
       "fourRFSystemSoftwareVersion": fourRFSystemSoftwareVersion,
       "fourRFSystemIpAddress": fourRFSystemIpAddress,
       "fourRFSystemRemoteIpAddress": fourRFSystemRemoteIpAddress,
       "fourRFSystemSubnetMask": fourRFSystemSubnetMask,
       "fourRFSystemDefaultGateway": fourRFSystemDefaultGateway,
       "fourRFSystemIpAssignment": fourRFSystemIpAssignment,
       "fourRFSystemDateAndTime": fourRFSystemDateAndTime,
       "fourRFSystemTftpServerAddress": fourRFSystemTftpServerAddress,
       "fourRFSystemSerialNumber": fourRFSystemSerialNumber,
       "fourRFSystemLastReset": fourRFSystemLastReset,
       "fourRFSystemTimeZone": fourRFSystemTimeZone,
       "fourRFSystemSyslogAddress": fourRFSystemSyslogAddress,
       "fourRFSystemSyslogPort": fourRFSystemSyslogPort,
       "fourRFSystemTimeDaylightSavings": fourRFSystemTimeDaylightSavings,
       "fourRFSystemTimeZoneGMTOffset": fourRFSystemTimeZoneGMTOffset,
       "fourRFSystemMACAddress": fourRFSystemMACAddress,
       "fourRFSystemLocalRadioBIpAddress": fourRFSystemLocalRadioBIpAddress,
       "fourRFSystemRemoteRadioBIpAddress": fourRFSystemRemoteRadioBIpAddress,
       "fourRFSystemLocalRadioAIpAddress": fourRFSystemLocalRadioAIpAddress,
       "fourRFReset": fourRFReset,
       "fourRFResetType": fourRFResetType,
       "fourRFResetTime": fourRFResetTime,
       "fourRFResetCommand": fourRFResetCommand,
       "fourRFMibBackup": fourRFMibBackup,
       "fourRFMibBackupFile": fourRFMibBackupFile,
       "fourRFMibBackupCommand": fourRFMibBackupCommand,
       "fourRFMibBackupResult": fourRFMibBackupResult,
       "fourRFUpload": fourRFUpload,
       "fourRFUploadType": fourRFUploadType,
       "fourRFUploadFile": fourRFUploadFile,
       "fourRFUploadCommand": fourRFUploadCommand,
       "fourRFUploadResult": fourRFUploadResult,
       "fourRFImageTable": fourRFImageTable,
       "fourRFImageTableEntry": fourRFImageTableEntry,
       "fourRFImageIndex": fourRFImageIndex,
       "fourRFImageType": fourRFImageType,
       "fourRFImageStatus": fourRFImageStatus,
       "fourRFImageSize": fourRFImageSize,
       "fourRFImageVersion": fourRFImageVersion,
       "fourRFImageControl": fourRFImageControl,
       "fourRFImageTableIndex": fourRFImageTableIndex,
       "fourRFImageTableCommand": fourRFImageTableCommand,
       "fourRFWebUserManagementTable": fourRFWebUserManagementTable,
       "fourRFWebUserEntry": fourRFWebUserEntry,
       "fourRFWebUserIndex": fourRFWebUserIndex,
       "fourRFWebUserName": fourRFWebUserName,
       "fourRFWebUserPassword": fourRFWebUserPassword,
       "fourRFWebUserGroup": fourRFWebUserGroup,
       "fourRFWebUserEnabled": fourRFWebUserEnabled,
       "fourRFWebUserPasswordConfirm": fourRFWebUserPasswordConfirm,
       "fourRFEvents": fourRFEvents,
       "fourRFEventsV2": fourRFEventsV2,
       "fourRFResetEvent": fourRFResetEvent,
       "fourRFMibBackupStatusEvent": fourRFMibBackupStatusEvent,
       "fouRFUploadStatusEvent": fouRFUploadStatusEvent}
)
