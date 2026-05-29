# SNMP MIB module (HH3C-DOT11-ACMT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\comware\HH3C-DOT11-ACMT-MIB

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

(Hh3cDot11MACModeType,
 Hh3cDot11ObjectIDType,
 Hh3cDot11TunnelSecSchemType,
 hh3cDot11) = mibBuilder.importSymbols(
    "HH3C-DOT11-REF-MIB",
    "Hh3cDot11MACModeType",
    "Hh3cDot11ObjectIDType",
    "Hh3cDot11TunnelSecSchemType",
    "hh3cDot11")

(IANAifType,) = mibBuilder.importSymbols(
    "IANAifType-MIB",
    "IANAifType")

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
 MacAddress,
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

hh3cDot11ACMT = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 1)
)
if mibBuilder.loadTexts:
    hh3cDot11ACMT.setRevisions(
        ("2018-06-04 18:00",
         "2016-03-11 18:00",
         "2010-08-04 18:00",
         "2009-08-07 18:00",
         "2009-07-29 18:00",
         "2009-05-07 20:00",
         "2008-07-09 18:00",
         "2007-12-21 18:00",
         "2007-06-19 18:00",
         "2007-04-27 20:00",
         "2006-05-10 19:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Hh3cDot11ACObjectGroup_ObjectIdentity = ObjectIdentity
hh3cDot11ACObjectGroup = _Hh3cDot11ACObjectGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 1, 1)
)
_Hh3cDot11ACObject_ObjectIdentity = ObjectIdentity
hh3cDot11ACObject = _Hh3cDot11ACObject_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 1, 1, 1)
)


class _Hh3cDot11CurrentACMACMode_Type(Hh3cDot11MACModeType):
    """Custom type hh3cDot11CurrentACMACMode based on Hh3cDot11MACModeType"""
    defaultValue = 1


_Hh3cDot11CurrentACMACMode_Type.__name__ = "Hh3cDot11MACModeType"
_Hh3cDot11CurrentACMACMode_Object = MibScalar
hh3cDot11CurrentACMACMode = _Hh3cDot11CurrentACMACMode_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 1, 1, 1, 1),
    _Hh3cDot11CurrentACMACMode_Type()
)
hh3cDot11CurrentACMACMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11CurrentACMACMode.setStatus("current")
_Hh3cDot11MaxAPNumPermitted_Type = Integer32
_Hh3cDot11MaxAPNumPermitted_Object = MibScalar
hh3cDot11MaxAPNumPermitted = _Hh3cDot11MaxAPNumPermitted_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 1, 1, 1, 2),
    _Hh3cDot11MaxAPNumPermitted_Type()
)
hh3cDot11MaxAPNumPermitted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11MaxAPNumPermitted.setStatus("current")
_Hh3cDot11MaxStationNumPermitted_Type = Integer32
_Hh3cDot11MaxStationNumPermitted_Object = MibScalar
hh3cDot11MaxStationNumPermitted = _Hh3cDot11MaxStationNumPermitted_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 1, 1, 1, 3),
    _Hh3cDot11MaxStationNumPermitted_Type()
)
hh3cDot11MaxStationNumPermitted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11MaxStationNumPermitted.setStatus("current")


class _Hh3cDot11RunAPNumThreshold_Type(Integer32):
    """Custom type hh3cDot11RunAPNumThreshold based on Integer32"""
    defaultValue = 100

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(30, 100),
    )


_Hh3cDot11RunAPNumThreshold_Type.__name__ = "Integer32"
_Hh3cDot11RunAPNumThreshold_Object = MibScalar
hh3cDot11RunAPNumThreshold = _Hh3cDot11RunAPNumThreshold_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 1, 1, 1, 4),
    _Hh3cDot11RunAPNumThreshold_Type()
)
hh3cDot11RunAPNumThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDot11RunAPNumThreshold.setStatus("current")
if mibBuilder.loadTexts:
    hh3cDot11RunAPNumThreshold.setUnits("percent")


class _Hh3cDot11MaxNewConnCntPerSecCM_Type(Integer32):
    """Custom type hh3cDot11MaxNewConnCntPerSecCM based on Integer32"""
    defaultValue = 300


_Hh3cDot11MaxNewConnCntPerSecCM_Type.__name__ = "Integer32"
_Hh3cDot11MaxNewConnCntPerSecCM_Object = MibScalar
hh3cDot11MaxNewConnCntPerSecCM = _Hh3cDot11MaxNewConnCntPerSecCM_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 1, 1, 1, 5),
    _Hh3cDot11MaxNewConnCntPerSecCM_Type()
)
hh3cDot11MaxNewConnCntPerSecCM.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDot11MaxNewConnCntPerSecCM.setStatus("current")


class _Hh3cDot11IFNumberCM_Type(Integer32):
    """Custom type hh3cDot11IFNumberCM based on Integer32"""
    defaultValue = 24


_Hh3cDot11IFNumberCM_Type.__name__ = "Integer32"
_Hh3cDot11IFNumberCM_Object = MibScalar
hh3cDot11IFNumberCM = _Hh3cDot11IFNumberCM_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 1, 1, 1, 6),
    _Hh3cDot11IFNumberCM_Type()
)
hh3cDot11IFNumberCM.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDot11IFNumberCM.setStatus("current")
_Hh3cDot11APLicenseWeight_Type = OctetString
_Hh3cDot11APLicenseWeight_Object = MibScalar
hh3cDot11APLicenseWeight = _Hh3cDot11APLicenseWeight_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 1, 1, 1, 7),
    _Hh3cDot11APLicenseWeight_Type()
)
hh3cDot11APLicenseWeight.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11APLicenseWeight.setStatus("current")
_Hh3cDot11ACTotalRebootCnt_Type = Integer32
_Hh3cDot11ACTotalRebootCnt_Object = MibScalar
hh3cDot11ACTotalRebootCnt = _Hh3cDot11ACTotalRebootCnt_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 1, 1, 1, 8),
    _Hh3cDot11ACTotalRebootCnt_Type()
)
hh3cDot11ACTotalRebootCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11ACTotalRebootCnt.setStatus("current")
_Hh3cDot11ACLoadInfo_ObjectIdentity = ObjectIdentity
hh3cDot11ACLoadInfo = _Hh3cDot11ACLoadInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 1, 1, 2)
)
_Hh3cDot11APConnectCount_Type = Integer32
_Hh3cDot11APConnectCount_Object = MibScalar
hh3cDot11APConnectCount = _Hh3cDot11APConnectCount_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 1, 1, 2, 1),
    _Hh3cDot11APConnectCount_Type()
)
hh3cDot11APConnectCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11APConnectCount.setStatus("current")
_Hh3cDot11StationConnectCount_Type = Integer32
_Hh3cDot11StationConnectCount_Object = MibScalar
hh3cDot11StationConnectCount = _Hh3cDot11StationConnectCount_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 1, 1, 2, 2),
    _Hh3cDot11StationConnectCount_Type()
)
hh3cDot11StationConnectCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11StationConnectCount.setStatus("current")
_Hh3cDot11ACIFLoadInfoTable_Object = MibTable
hh3cDot11ACIFLoadInfoTable = _Hh3cDot11ACIFLoadInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 1, 1, 2, 3)
)
if mibBuilder.loadTexts:
    hh3cDot11ACIFLoadInfoTable.setStatus("current")
_Hh3cDot11ACIFLoadInfoEntry_Object = MibTableRow
hh3cDot11ACIFLoadInfoEntry = _Hh3cDot11ACIFLoadInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 1, 1, 2, 3, 1)
)
hh3cDot11ACIFLoadInfoEntry.setIndexNames(
    (0, "HH3C-DOT11-ACMT-MIB", "hh3cDot11ACIfIndex"),
)
if mibBuilder.loadTexts:
    hh3cDot11ACIFLoadInfoEntry.setStatus("current")
_Hh3cDot11ACIfIndex_Type = Integer32
_Hh3cDot11ACIfIndex_Object = MibTableColumn
hh3cDot11ACIfIndex = _Hh3cDot11ACIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 1, 1, 2, 3, 1, 1),
    _Hh3cDot11ACIfIndex_Type()
)
hh3cDot11ACIfIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cDot11ACIfIndex.setStatus("current")
_Hh3cDot11ACIfApNum_Type = Integer32
_Hh3cDot11ACIfApNum_Object = MibTableColumn
hh3cDot11ACIfApNum = _Hh3cDot11ACIfApNum_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 1, 1, 2, 3, 1, 2),
    _Hh3cDot11ACIfApNum_Type()
)
hh3cDot11ACIfApNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11ACIfApNum.setStatus("current")
_Hh3cDot11ACIfStaNum_Type = Integer32
_Hh3cDot11ACIfStaNum_Object = MibTableColumn
hh3cDot11ACIfStaNum = _Hh3cDot11ACIfStaNum_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 1, 1, 2, 3, 1, 3),
    _Hh3cDot11ACIfStaNum_Type()
)
hh3cDot11ACIfStaNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11ACIfStaNum.setStatus("current")
_Hh3cDot11ACIfName_Type = OctetString
_Hh3cDot11ACIfName_Object = MibTableColumn
hh3cDot11ACIfName = _Hh3cDot11ACIfName_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 1, 1, 2, 3, 1, 4),
    _Hh3cDot11ACIfName_Type()
)
hh3cDot11ACIfName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11ACIfName.setStatus("current")
_Hh3cDot11MasterAPCount_Type = Integer32
_Hh3cDot11MasterAPCount_Object = MibScalar
hh3cDot11MasterAPCount = _Hh3cDot11MasterAPCount_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 1, 1, 2, 4),
    _Hh3cDot11MasterAPCount_Type()
)
hh3cDot11MasterAPCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11MasterAPCount.setStatus("current")
_Hh3cDot11SlaveAPCount_Type = Integer32
_Hh3cDot11SlaveAPCount_Object = MibScalar
hh3cDot11SlaveAPCount = _Hh3cDot11SlaveAPCount_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 1, 1, 2, 5),
    _Hh3cDot11SlaveAPCount_Type()
)
hh3cDot11SlaveAPCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11SlaveAPCount.setStatus("current")
_Hh3cDot11ConnectAutoAPCount_Type = Integer32
_Hh3cDot11ConnectAutoAPCount_Object = MibScalar
hh3cDot11ConnectAutoAPCount = _Hh3cDot11ConnectAutoAPCount_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 1, 1, 2, 6),
    _Hh3cDot11ConnectAutoAPCount_Type()
)
hh3cDot11ConnectAutoAPCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11ConnectAutoAPCount.setStatus("current")
_Hh3cDot11PersistentAPCount_Type = Integer32
_Hh3cDot11PersistentAPCount_Object = MibScalar
hh3cDot11PersistentAPCount = _Hh3cDot11PersistentAPCount_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 1, 1, 2, 7),
    _Hh3cDot11PersistentAPCount_Type()
)
hh3cDot11PersistentAPCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11PersistentAPCount.setStatus("current")
_Hh3cDot11AcUploadFrameCnt_Type = Counter64
_Hh3cDot11AcUploadFrameCnt_Object = MibScalar
hh3cDot11AcUploadFrameCnt = _Hh3cDot11AcUploadFrameCnt_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 1, 1, 2, 8),
    _Hh3cDot11AcUploadFrameCnt_Type()
)
hh3cDot11AcUploadFrameCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11AcUploadFrameCnt.setStatus("current")
_Hh3cDot11AcDownloadFrameCnt_Type = Counter64
_Hh3cDot11AcDownloadFrameCnt_Object = MibScalar
hh3cDot11AcDownloadFrameCnt = _Hh3cDot11AcDownloadFrameCnt_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 1, 1, 2, 9),
    _Hh3cDot11AcDownloadFrameCnt_Type()
)
hh3cDot11AcDownloadFrameCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11AcDownloadFrameCnt.setStatus("current")
_Hh3cDot11AcUploadFrameBytes_Type = Counter64
_Hh3cDot11AcUploadFrameBytes_Object = MibScalar
hh3cDot11AcUploadFrameBytes = _Hh3cDot11AcUploadFrameBytes_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 1, 1, 2, 10),
    _Hh3cDot11AcUploadFrameBytes_Type()
)
hh3cDot11AcUploadFrameBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11AcUploadFrameBytes.setStatus("current")
_Hh3cDot11AcDownloadFrameBytes_Type = Counter64
_Hh3cDot11AcDownloadFrameBytes_Object = MibScalar
hh3cDot11AcDownloadFrameBytes = _Hh3cDot11AcDownloadFrameBytes_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 1, 1, 2, 11),
    _Hh3cDot11AcDownloadFrameBytes_Type()
)
hh3cDot11AcDownloadFrameBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11AcDownloadFrameBytes.setStatus("current")


class _Hh3cDot11BackupACRole_Type(Integer32):
    """Custom type hh3cDot11BackupACRole based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("null", 1),
          ("master", 2),
          ("slave", 3))
    )


_Hh3cDot11BackupACRole_Type.__name__ = "Integer32"
_Hh3cDot11BackupACRole_Object = MibScalar
hh3cDot11BackupACRole = _Hh3cDot11BackupACRole_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 1, 1, 2, 12),
    _Hh3cDot11BackupACRole_Type()
)
hh3cDot11BackupACRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11BackupACRole.setStatus("current")
_Hh3cDot11BackupACNMSIP_Type = IpAddress
_Hh3cDot11BackupACNMSIP_Object = MibScalar
hh3cDot11BackupACNMSIP = _Hh3cDot11BackupACNMSIP_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 1, 1, 2, 13),
    _Hh3cDot11BackupACNMSIP_Type()
)
hh3cDot11BackupACNMSIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11BackupACNMSIP.setStatus("current")


class _Hh3cDot11ACBackupMode_Type(Integer32):
    """Custom type hh3cDot11ACBackupMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("null", 1),
          ("hotBackup", 2),
          ("coldBackup", 3))
    )


_Hh3cDot11ACBackupMode_Type.__name__ = "Integer32"
_Hh3cDot11ACBackupMode_Object = MibScalar
hh3cDot11ACBackupMode = _Hh3cDot11ACBackupMode_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 1, 1, 2, 14),
    _Hh3cDot11ACBackupMode_Type()
)
hh3cDot11ACBackupMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11ACBackupMode.setStatus("current")


class _Hh3cDot11ACBackupStatus_Type(Integer32):
    """Custom type hh3cDot11ACBackupStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("standby", 2))
    )


_Hh3cDot11ACBackupStatus_Type.__name__ = "Integer32"
_Hh3cDot11ACBackupStatus_Object = MibScalar
hh3cDot11ACBackupStatus = _Hh3cDot11ACBackupStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 1, 1, 2, 15),
    _Hh3cDot11ACBackupStatus_Type()
)
hh3cDot11ACBackupStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11ACBackupStatus.setStatus("current")
_Hh3cDot11ACSwitchCnt_Type = Integer32
_Hh3cDot11ACSwitchCnt_Object = MibScalar
hh3cDot11ACSwitchCnt = _Hh3cDot11ACSwitchCnt_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 1, 1, 2, 16),
    _Hh3cDot11ACSwitchCnt_Type()
)
hh3cDot11ACSwitchCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11ACSwitchCnt.setStatus("current")
_Hh3cDot11ACSouthifPacketOutputCount_Type = Counter64
_Hh3cDot11ACSouthifPacketOutputCount_Object = MibScalar
hh3cDot11ACSouthifPacketOutputCount = _Hh3cDot11ACSouthifPacketOutputCount_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 1, 1, 2, 17),
    _Hh3cDot11ACSouthifPacketOutputCount_Type()
)
hh3cDot11ACSouthifPacketOutputCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11ACSouthifPacketOutputCount.setStatus("current")
_Hh3cDot11ACSouthifPacketOutputBytes_Type = Counter64
_Hh3cDot11ACSouthifPacketOutputBytes_Object = MibScalar
hh3cDot11ACSouthifPacketOutputBytes = _Hh3cDot11ACSouthifPacketOutputBytes_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 1, 1, 2, 18),
    _Hh3cDot11ACSouthifPacketOutputBytes_Type()
)
hh3cDot11ACSouthifPacketOutputBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11ACSouthifPacketOutputBytes.setStatus("current")
_Hh3cDot11ACSouthifPacketInputCount_Type = Counter64
_Hh3cDot11ACSouthifPacketInputCount_Object = MibScalar
hh3cDot11ACSouthifPacketInputCount = _Hh3cDot11ACSouthifPacketInputCount_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 1, 1, 2, 19),
    _Hh3cDot11ACSouthifPacketInputCount_Type()
)
hh3cDot11ACSouthifPacketInputCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11ACSouthifPacketInputCount.setStatus("current")
_Hh3cDot11ACSouthifPacketInputBytes_Type = Counter64
_Hh3cDot11ACSouthifPacketInputBytes_Object = MibScalar
hh3cDot11ACSouthifPacketInputBytes = _Hh3cDot11ACSouthifPacketInputBytes_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 1, 1, 2, 20),
    _Hh3cDot11ACSouthifPacketInputBytes_Type()
)
hh3cDot11ACSouthifPacketInputBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11ACSouthifPacketInputBytes.setStatus("current")
_Hh3cDot11TotalAPconnected_Type = Integer32
_Hh3cDot11TotalAPconnected_Object = MibScalar
hh3cDot11TotalAPconnected = _Hh3cDot11TotalAPconnected_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 1, 1, 2, 21),
    _Hh3cDot11TotalAPconnected_Type()
)
hh3cDot11TotalAPconnected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11TotalAPconnected.setStatus("current")
_Hh3cDot11RemainingAPcapacity_Type = Integer32
_Hh3cDot11RemainingAPcapacity_Object = MibScalar
hh3cDot11RemainingAPcapacity = _Hh3cDot11RemainingAPcapacity_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 1, 1, 2, 22),
    _Hh3cDot11RemainingAPcapacity_Type()
)
hh3cDot11RemainingAPcapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11RemainingAPcapacity.setStatus("current")
_Hh3cDot11WLANAssocStatisInfo_ObjectIdentity = ObjectIdentity
hh3cDot11WLANAssocStatisInfo = _Hh3cDot11WLANAssocStatisInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 1, 1, 3)
)
_Hh3cDot11StationAssocSum_Type = Counter32
_Hh3cDot11StationAssocSum_Object = MibScalar
hh3cDot11StationAssocSum = _Hh3cDot11StationAssocSum_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 1, 1, 3, 1),
    _Hh3cDot11StationAssocSum_Type()
)
hh3cDot11StationAssocSum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11StationAssocSum.setStatus("current")
_Hh3cDot11StationAssocFailSum_Type = Counter32
_Hh3cDot11StationAssocFailSum_Object = MibScalar
hh3cDot11StationAssocFailSum = _Hh3cDot11StationAssocFailSum_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 1, 1, 3, 2),
    _Hh3cDot11StationAssocFailSum_Type()
)
hh3cDot11StationAssocFailSum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11StationAssocFailSum.setStatus("current")
_Hh3cDot11StationReassocSum_Type = Counter32
_Hh3cDot11StationReassocSum_Object = MibScalar
hh3cDot11StationReassocSum = _Hh3cDot11StationReassocSum_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 1, 1, 3, 3),
    _Hh3cDot11StationReassocSum_Type()
)
hh3cDot11StationReassocSum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11StationReassocSum.setStatus("current")
_Hh3cDot11StationAssocRejectedSum_Type = Counter32
_Hh3cDot11StationAssocRejectedSum_Object = MibScalar
hh3cDot11StationAssocRejectedSum = _Hh3cDot11StationAssocRejectedSum_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 1, 1, 3, 4),
    _Hh3cDot11StationAssocRejectedSum_Type()
)
hh3cDot11StationAssocRejectedSum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11StationAssocRejectedSum.setStatus("current")
_Hh3cDot11StationExDeAuthenSum_Type = Counter32
_Hh3cDot11StationExDeAuthenSum_Object = MibScalar
hh3cDot11StationExDeAuthenSum = _Hh3cDot11StationExDeAuthenSum_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 1, 1, 3, 5),
    _Hh3cDot11StationExDeAuthenSum_Type()
)
hh3cDot11StationExDeAuthenSum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11StationExDeAuthenSum.setStatus("current")
_Hh3cDot11StationCurAssocSum_Type = Integer32
_Hh3cDot11StationCurAssocSum_Object = MibScalar
hh3cDot11StationCurAssocSum = _Hh3cDot11StationCurAssocSum_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 1, 1, 3, 6),
    _Hh3cDot11StationCurAssocSum_Type()
)
hh3cDot11StationCurAssocSum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11StationCurAssocSum.setStatus("current")
_Hh3cDot11StationAssocReqSum_Type = Counter32
_Hh3cDot11StationAssocReqSum_Object = MibScalar
hh3cDot11StationAssocReqSum = _Hh3cDot11StationAssocReqSum_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 1, 1, 3, 7),
    _Hh3cDot11StationAssocReqSum_Type()
)
hh3cDot11StationAssocReqSum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11StationAssocReqSum.setStatus("current")
_Hh3cDot11StationReassocReqSum_Type = Counter32
_Hh3cDot11StationReassocReqSum_Object = MibScalar
hh3cDot11StationReassocReqSum = _Hh3cDot11StationReassocReqSum_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 1, 1, 3, 8),
    _Hh3cDot11StationReassocReqSum_Type()
)
hh3cDot11StationReassocReqSum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11StationReassocReqSum.setStatus("current")
_Hh3cDot11StationReassocFailSum_Type = Counter32
_Hh3cDot11StationReassocFailSum_Object = MibScalar
hh3cDot11StationReassocFailSum = _Hh3cDot11StationReassocFailSum_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 1, 1, 3, 9),
    _Hh3cDot11StationReassocFailSum_Type()
)
hh3cDot11StationReassocFailSum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11StationReassocFailSum.setStatus("current")
_Hh3cDot11ACBASInfo_ObjectIdentity = ObjectIdentity
hh3cDot11ACBASInfo = _Hh3cDot11ACBASInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 1, 1, 4)
)
_Hh3cDot11ACBASSysObjects_ObjectIdentity = ObjectIdentity
hh3cDot11ACBASSysObjects = _Hh3cDot11ACBASSysObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 1, 1, 4, 1)
)
_Hh3cDot11ACBASTableObjects_ObjectIdentity = ObjectIdentity
hh3cDot11ACBASTableObjects = _Hh3cDot11ACBASTableObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 1, 1, 4, 2)
)
_Hh3cDot11ACBASIfTable_Object = MibTable
hh3cDot11ACBASIfTable = _Hh3cDot11ACBASIfTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 1, 1, 4, 2, 3)
)
if mibBuilder.loadTexts:
    hh3cDot11ACBASIfTable.setStatus("current")
_Hh3cDot11ACBASIfEntry_Object = MibTableRow
hh3cDot11ACBASIfEntry = _Hh3cDot11ACBASIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 1, 1, 4, 2, 3, 1)
)
hh3cDot11ACBASIfEntry.setIndexNames(
    (0, "HH3C-DOT11-ACMT-MIB", "hh3cDot11ACBASIfIndex"),
)
if mibBuilder.loadTexts:
    hh3cDot11ACBASIfEntry.setStatus("current")
_Hh3cDot11ACBASIfIndex_Type = Integer32
_Hh3cDot11ACBASIfIndex_Object = MibTableColumn
hh3cDot11ACBASIfIndex = _Hh3cDot11ACBASIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 1, 1, 4, 2, 3, 1, 1),
    _Hh3cDot11ACBASIfIndex_Type()
)
hh3cDot11ACBASIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cDot11ACBASIfIndex.setStatus("current")


class _Hh3cDot11ACBASIfDescr_Type(OctetString):
    """Custom type hh3cDot11ACBASIfDescr based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_Hh3cDot11ACBASIfDescr_Type.__name__ = "OctetString"
_Hh3cDot11ACBASIfDescr_Object = MibTableColumn
hh3cDot11ACBASIfDescr = _Hh3cDot11ACBASIfDescr_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 1, 1, 4, 2, 3, 1, 2),
    _Hh3cDot11ACBASIfDescr_Type()
)
hh3cDot11ACBASIfDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11ACBASIfDescr.setStatus("current")
_Hh3cDot11ACBASIfType_Type = IANAifType
_Hh3cDot11ACBASIfType_Object = MibTableColumn
hh3cDot11ACBASIfType = _Hh3cDot11ACBASIfType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 1, 1, 4, 2, 3, 1, 3),
    _Hh3cDot11ACBASIfType_Type()
)
hh3cDot11ACBASIfType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11ACBASIfType.setStatus("current")
_Hh3cDot11ACStaUserSecAuthStatis_ObjectIdentity = ObjectIdentity
hh3cDot11ACStaUserSecAuthStatis = _Hh3cDot11ACStaUserSecAuthStatis_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 1, 1, 5)
)
_Hh3cDot11ACStaUserAuthCurNumber_Type = Integer32
_Hh3cDot11ACStaUserAuthCurNumber_Object = MibScalar
hh3cDot11ACStaUserAuthCurNumber = _Hh3cDot11ACStaUserAuthCurNumber_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 1, 1, 5, 1),
    _Hh3cDot11ACStaUserAuthCurNumber_Type()
)
hh3cDot11ACStaUserAuthCurNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11ACStaUserAuthCurNumber.setStatus("current")
_Hh3cDot11ACStaUserConnFailCnt_Type = Counter32
_Hh3cDot11ACStaUserConnFailCnt_Object = MibScalar
hh3cDot11ACStaUserConnFailCnt = _Hh3cDot11ACStaUserConnFailCnt_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 1, 1, 5, 2),
    _Hh3cDot11ACStaUserConnFailCnt_Type()
)
hh3cDot11ACStaUserConnFailCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11ACStaUserConnFailCnt.setStatus("current")
_Hh3cDot11ACStaUserAuthReqCnt_Type = Counter32
_Hh3cDot11ACStaUserAuthReqCnt_Object = MibScalar
hh3cDot11ACStaUserAuthReqCnt = _Hh3cDot11ACStaUserAuthReqCnt_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 1, 1, 5, 3),
    _Hh3cDot11ACStaUserAuthReqCnt_Type()
)
hh3cDot11ACStaUserAuthReqCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11ACStaUserAuthReqCnt.setStatus("current")
_Hh3cDot11ACStaUserAuthSuccCnt_Type = Counter32
_Hh3cDot11ACStaUserAuthSuccCnt_Object = MibScalar
hh3cDot11ACStaUserAuthSuccCnt = _Hh3cDot11ACStaUserAuthSuccCnt_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 1, 1, 5, 4),
    _Hh3cDot11ACStaUserAuthSuccCnt_Type()
)
hh3cDot11ACStaUserAuthSuccCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11ACStaUserAuthSuccCnt.setStatus("current")
_Hh3cDot11ACStaUserAuthFailCnt_Type = Counter32
_Hh3cDot11ACStaUserAuthFailCnt_Object = MibScalar
hh3cDot11ACStaUserAuthFailCnt = _Hh3cDot11ACStaUserAuthFailCnt_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 1, 1, 5, 5),
    _Hh3cDot11ACStaUserAuthFailCnt_Type()
)
hh3cDot11ACStaUserAuthFailCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11ACStaUserAuthFailCnt.setStatus("current")
_Hh3cDot11ACStaUserAllAuthCntCM_Type = Counter32
_Hh3cDot11ACStaUserAllAuthCntCM_Object = MibScalar
hh3cDot11ACStaUserAllAuthCntCM = _Hh3cDot11ACStaUserAllAuthCntCM_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 1, 1, 5, 6),
    _Hh3cDot11ACStaUserAllAuthCntCM_Type()
)
hh3cDot11ACStaUserAllAuthCntCM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11ACStaUserAllAuthCntCM.setStatus("current")
_Hh3cDot11ACStaUserAuthRespCntCM_Type = Counter32
_Hh3cDot11ACStaUserAuthRespCntCM_Object = MibScalar
hh3cDot11ACStaUserAuthRespCntCM = _Hh3cDot11ACStaUserAuthRespCntCM_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 1, 1, 5, 7),
    _Hh3cDot11ACStaUserAuthRespCntCM_Type()
)
hh3cDot11ACStaUserAuthRespCntCM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11ACStaUserAuthRespCntCM.setStatus("current")
_Hh3cDot11ACStaSecAuthTypeStatis_ObjectIdentity = ObjectIdentity
hh3cDot11ACStaSecAuthTypeStatis = _Hh3cDot11ACStaSecAuthTypeStatis_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 1, 1, 6)
)
_Hh3cDot11ACStaUserPortalOnlineNum_Type = Integer32
_Hh3cDot11ACStaUserPortalOnlineNum_Object = MibScalar
hh3cDot11ACStaUserPortalOnlineNum = _Hh3cDot11ACStaUserPortalOnlineNum_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 1, 1, 6, 1),
    _Hh3cDot11ACStaUserPortalOnlineNum_Type()
)
hh3cDot11ACStaUserPortalOnlineNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11ACStaUserPortalOnlineNum.setStatus("current")
_Hh3cDot11ACStaUserFreeAuthOnlineNum_Type = Integer32
_Hh3cDot11ACStaUserFreeAuthOnlineNum_Object = MibScalar
hh3cDot11ACStaUserFreeAuthOnlineNum = _Hh3cDot11ACStaUserFreeAuthOnlineNum_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 1, 1, 6, 2),
    _Hh3cDot11ACStaUserFreeAuthOnlineNum_Type()
)
hh3cDot11ACStaUserFreeAuthOnlineNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11ACStaUserFreeAuthOnlineNum.setStatus("current")
_Hh3cDot11ACStaUserAssociateAuthOnlineNum_Type = Integer32
_Hh3cDot11ACStaUserAssociateAuthOnlineNum_Object = MibScalar
hh3cDot11ACStaUserAssociateAuthOnlineNum = _Hh3cDot11ACStaUserAssociateAuthOnlineNum_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 1, 1, 6, 3),
    _Hh3cDot11ACStaUserAssociateAuthOnlineNum_Type()
)
hh3cDot11ACStaUserAssociateAuthOnlineNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11ACStaUserAssociateAuthOnlineNum.setStatus("current")
_Hh3cDot11ACStaUserMacAuthOnlineNum_Type = Integer32
_Hh3cDot11ACStaUserMacAuthOnlineNum_Object = MibScalar
hh3cDot11ACStaUserMacAuthOnlineNum = _Hh3cDot11ACStaUserMacAuthOnlineNum_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 1, 1, 6, 4),
    _Hh3cDot11ACStaUserMacAuthOnlineNum_Type()
)
hh3cDot11ACStaUserMacAuthOnlineNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11ACStaUserMacAuthOnlineNum.setStatus("current")
_Hh3cDot11ACStaUserPortalLostConnectionCnt_Type = Counter32
_Hh3cDot11ACStaUserPortalLostConnectionCnt_Object = MibScalar
hh3cDot11ACStaUserPortalLostConnectionCnt = _Hh3cDot11ACStaUserPortalLostConnectionCnt_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 1, 1, 6, 5),
    _Hh3cDot11ACStaUserPortalLostConnectionCnt_Type()
)
hh3cDot11ACStaUserPortalLostConnectionCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11ACStaUserPortalLostConnectionCnt.setStatus("current")
_Hh3cDot11ACStaUserFreeAuthLostConnectionCnt_Type = Counter32
_Hh3cDot11ACStaUserFreeAuthLostConnectionCnt_Object = MibScalar
hh3cDot11ACStaUserFreeAuthLostConnectionCnt = _Hh3cDot11ACStaUserFreeAuthLostConnectionCnt_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 1, 1, 6, 6),
    _Hh3cDot11ACStaUserFreeAuthLostConnectionCnt_Type()
)
hh3cDot11ACStaUserFreeAuthLostConnectionCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11ACStaUserFreeAuthLostConnectionCnt.setStatus("current")
_Hh3cDot11ACStaUserAssociateAuthLostConnectionCnt_Type = Counter32
_Hh3cDot11ACStaUserAssociateAuthLostConnectionCnt_Object = MibScalar
hh3cDot11ACStaUserAssociateAuthLostConnectionCnt = _Hh3cDot11ACStaUserAssociateAuthLostConnectionCnt_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 1, 1, 6, 7),
    _Hh3cDot11ACStaUserAssociateAuthLostConnectionCnt_Type()
)
hh3cDot11ACStaUserAssociateAuthLostConnectionCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11ACStaUserAssociateAuthLostConnectionCnt.setStatus("current")
_Hh3cDot11ACStaUserMacAuthLostConnectionCnt_Type = Counter32
_Hh3cDot11ACStaUserMacAuthLostConnectionCnt_Object = MibScalar
hh3cDot11ACStaUserMacAuthLostConnectionCnt = _Hh3cDot11ACStaUserMacAuthLostConnectionCnt_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 1, 1, 6, 8),
    _Hh3cDot11ACStaUserMacAuthLostConnectionCnt_Type()
)
hh3cDot11ACStaUserMacAuthLostConnectionCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11ACStaUserMacAuthLostConnectionCnt.setStatus("current")
_Hh3cDot11ACStaPortalAuthReqCnt_Type = Counter32
_Hh3cDot11ACStaPortalAuthReqCnt_Object = MibScalar
hh3cDot11ACStaPortalAuthReqCnt = _Hh3cDot11ACStaPortalAuthReqCnt_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 1, 1, 6, 9),
    _Hh3cDot11ACStaPortalAuthReqCnt_Type()
)
hh3cDot11ACStaPortalAuthReqCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11ACStaPortalAuthReqCnt.setStatus("current")
_Hh3cDot11ACStaAssociateAuthReqCnt_Type = Counter32
_Hh3cDot11ACStaAssociateAuthReqCnt_Object = MibScalar
hh3cDot11ACStaAssociateAuthReqCnt = _Hh3cDot11ACStaAssociateAuthReqCnt_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 1, 1, 6, 10),
    _Hh3cDot11ACStaAssociateAuthReqCnt_Type()
)
hh3cDot11ACStaAssociateAuthReqCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11ACStaAssociateAuthReqCnt.setStatus("current")
_Hh3cDot11ACStaMacAuthReqCnt_Type = Counter32
_Hh3cDot11ACStaMacAuthReqCnt_Object = MibScalar
hh3cDot11ACStaMacAuthReqCnt = _Hh3cDot11ACStaMacAuthReqCnt_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 1, 1, 6, 11),
    _Hh3cDot11ACStaMacAuthReqCnt_Type()
)
hh3cDot11ACStaMacAuthReqCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11ACStaMacAuthReqCnt.setStatus("current")
_Hh3cDot11ACStaPortalAuthSuccCnt_Type = Counter32
_Hh3cDot11ACStaPortalAuthSuccCnt_Object = MibScalar
hh3cDot11ACStaPortalAuthSuccCnt = _Hh3cDot11ACStaPortalAuthSuccCnt_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 1, 1, 6, 12),
    _Hh3cDot11ACStaPortalAuthSuccCnt_Type()
)
hh3cDot11ACStaPortalAuthSuccCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11ACStaPortalAuthSuccCnt.setStatus("current")
_Hh3cDot11ACStaAssociateAuthSuccCnt_Type = Counter32
_Hh3cDot11ACStaAssociateAuthSuccCnt_Object = MibScalar
hh3cDot11ACStaAssociateAuthSuccCnt = _Hh3cDot11ACStaAssociateAuthSuccCnt_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 1, 1, 6, 13),
    _Hh3cDot11ACStaAssociateAuthSuccCnt_Type()
)
hh3cDot11ACStaAssociateAuthSuccCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11ACStaAssociateAuthSuccCnt.setStatus("current")
_Hh3cDot11ACStaMacAuthSuccCnt_Type = Counter32
_Hh3cDot11ACStaMacAuthSuccCnt_Object = MibScalar
hh3cDot11ACStaMacAuthSuccCnt = _Hh3cDot11ACStaMacAuthSuccCnt_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 1, 1, 6, 14),
    _Hh3cDot11ACStaMacAuthSuccCnt_Type()
)
hh3cDot11ACStaMacAuthSuccCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11ACStaMacAuthSuccCnt.setStatus("current")
_Hh3cDot11ACStaPortalAuthReqFailCnt_Type = Counter32
_Hh3cDot11ACStaPortalAuthReqFailCnt_Object = MibScalar
hh3cDot11ACStaPortalAuthReqFailCnt = _Hh3cDot11ACStaPortalAuthReqFailCnt_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 1, 1, 6, 15),
    _Hh3cDot11ACStaPortalAuthReqFailCnt_Type()
)
hh3cDot11ACStaPortalAuthReqFailCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11ACStaPortalAuthReqFailCnt.setStatus("current")
_Hh3cDot11ACStaAssociateAuthReqFailCnt_Type = Counter32
_Hh3cDot11ACStaAssociateAuthReqFailCnt_Object = MibScalar
hh3cDot11ACStaAssociateAuthReqFailCnt = _Hh3cDot11ACStaAssociateAuthReqFailCnt_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 1, 1, 6, 16),
    _Hh3cDot11ACStaAssociateAuthReqFailCnt_Type()
)
hh3cDot11ACStaAssociateAuthReqFailCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11ACStaAssociateAuthReqFailCnt.setStatus("current")
_Hh3cDot11ACStaMacAuthReqFailCnt_Type = Counter32
_Hh3cDot11ACStaMacAuthReqFailCnt_Object = MibScalar
hh3cDot11ACStaMacAuthReqFailCnt = _Hh3cDot11ACStaMacAuthReqFailCnt_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 1, 1, 6, 17),
    _Hh3cDot11ACStaMacAuthReqFailCnt_Type()
)
hh3cDot11ACStaMacAuthReqFailCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11ACStaMacAuthReqFailCnt.setStatus("current")
_Hh3cDot11ACStaUserAutoAuthOnlineNumCM_Type = Integer32
_Hh3cDot11ACStaUserAutoAuthOnlineNumCM_Object = MibScalar
hh3cDot11ACStaUserAutoAuthOnlineNumCM = _Hh3cDot11ACStaUserAutoAuthOnlineNumCM_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 1, 1, 6, 18),
    _Hh3cDot11ACStaUserAutoAuthOnlineNumCM_Type()
)
hh3cDot11ACStaUserAutoAuthOnlineNumCM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11ACStaUserAutoAuthOnlineNumCM.setStatus("current")
_Hh3cDot11ACStaUserAutoAuthLostConnectionCntCM_Type = Counter32
_Hh3cDot11ACStaUserAutoAuthLostConnectionCntCM_Object = MibScalar
hh3cDot11ACStaUserAutoAuthLostConnectionCntCM = _Hh3cDot11ACStaUserAutoAuthLostConnectionCntCM_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 1, 1, 6, 19),
    _Hh3cDot11ACStaUserAutoAuthLostConnectionCntCM_Type()
)
hh3cDot11ACStaUserAutoAuthLostConnectionCntCM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11ACStaUserAutoAuthLostConnectionCntCM.setStatus("current")
_Hh3cDot11ACStaAutoAuthReqCntCM_Type = Counter32
_Hh3cDot11ACStaAutoAuthReqCntCM_Object = MibScalar
hh3cDot11ACStaAutoAuthReqCntCM = _Hh3cDot11ACStaAutoAuthReqCntCM_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 1, 1, 6, 20),
    _Hh3cDot11ACStaAutoAuthReqCntCM_Type()
)
hh3cDot11ACStaAutoAuthReqCntCM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11ACStaAutoAuthReqCntCM.setStatus("current")
_Hh3cDot11ACStaAutoAuthSuccCntCM_Type = Counter32
_Hh3cDot11ACStaAutoAuthSuccCntCM_Object = MibScalar
hh3cDot11ACStaAutoAuthSuccCntCM = _Hh3cDot11ACStaAutoAuthSuccCntCM_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 1, 1, 6, 21),
    _Hh3cDot11ACStaAutoAuthSuccCntCM_Type()
)
hh3cDot11ACStaAutoAuthSuccCntCM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11ACStaAutoAuthSuccCntCM.setStatus("current")
_Hh3cDot11ACStaAutoAuthReqFailCntCM_Type = Counter32
_Hh3cDot11ACStaAutoAuthReqFailCntCM_Object = MibScalar
hh3cDot11ACStaAutoAuthReqFailCntCM = _Hh3cDot11ACStaAutoAuthReqFailCntCM_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 1, 1, 6, 22),
    _Hh3cDot11ACStaAutoAuthReqFailCntCM_Type()
)
hh3cDot11ACStaAutoAuthReqFailCntCM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11ACStaAutoAuthReqFailCntCM.setStatus("current")
_Hh3cDot11ACPortalStatisticCMTable_Object = MibTable
hh3cDot11ACPortalStatisticCMTable = _Hh3cDot11ACPortalStatisticCMTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 1, 1, 7)
)
if mibBuilder.loadTexts:
    hh3cDot11ACPortalStatisticCMTable.setStatus("current")
_Hh3cDot11ACPortalStatisticCMEntry_Object = MibTableRow
hh3cDot11ACPortalStatisticCMEntry = _Hh3cDot11ACPortalStatisticCMEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 1, 1, 7, 1)
)
hh3cDot11ACPortalStatisticCMEntry.setIndexNames(
    (0, "HH3C-DOT11-ACMT-MIB", "hh3cDot11ACPortalStatisticSSIDCM"),
)
if mibBuilder.loadTexts:
    hh3cDot11ACPortalStatisticCMEntry.setStatus("current")


class _Hh3cDot11ACPortalStatisticSSIDCM_Type(OctetString):
    """Custom type hh3cDot11ACPortalStatisticSSIDCM based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_Hh3cDot11ACPortalStatisticSSIDCM_Type.__name__ = "OctetString"
_Hh3cDot11ACPortalStatisticSSIDCM_Object = MibTableColumn
hh3cDot11ACPortalStatisticSSIDCM = _Hh3cDot11ACPortalStatisticSSIDCM_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 1, 1, 7, 1, 1),
    _Hh3cDot11ACPortalStatisticSSIDCM_Type()
)
hh3cDot11ACPortalStatisticSSIDCM.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cDot11ACPortalStatisticSSIDCM.setStatus("current")
_Hh3cDot11ACPortalStatAuthReqCM_Type = Counter32
_Hh3cDot11ACPortalStatAuthReqCM_Object = MibTableColumn
hh3cDot11ACPortalStatAuthReqCM = _Hh3cDot11ACPortalStatAuthReqCM_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 1, 1, 7, 1, 2),
    _Hh3cDot11ACPortalStatAuthReqCM_Type()
)
hh3cDot11ACPortalStatAuthReqCM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11ACPortalStatAuthReqCM.setStatus("current")
_Hh3cDot11ACPortalStatAuthRespCM_Type = Counter32
_Hh3cDot11ACPortalStatAuthRespCM_Object = MibTableColumn
hh3cDot11ACPortalStatAuthRespCM = _Hh3cDot11ACPortalStatAuthRespCM_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 1, 1, 7, 1, 3),
    _Hh3cDot11ACPortalStatAuthRespCM_Type()
)
hh3cDot11ACPortalStatAuthRespCM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11ACPortalStatAuthRespCM.setStatus("current")
_Hh3cDot11LocalACModelTable_Object = MibTable
hh3cDot11LocalACModelTable = _Hh3cDot11LocalACModelTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 1, 1, 8)
)
if mibBuilder.loadTexts:
    hh3cDot11LocalACModelTable.setStatus("current")
_Hh3cDot11LocalACModelEntry_Object = MibTableRow
hh3cDot11LocalACModelEntry = _Hh3cDot11LocalACModelEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 1, 1, 8, 1)
)
hh3cDot11LocalACModelEntry.setIndexNames(
    (0, "HH3C-DOT11-ACMT-MIB", "hh3cDot11LocalACModelAlias"),
)
if mibBuilder.loadTexts:
    hh3cDot11LocalACModelEntry.setStatus("current")


class _Hh3cDot11LocalACModelAlias_Type(OctetString):
    """Custom type hh3cDot11LocalACModelAlias based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_Hh3cDot11LocalACModelAlias_Type.__name__ = "OctetString"
_Hh3cDot11LocalACModelAlias_Object = MibTableColumn
hh3cDot11LocalACModelAlias = _Hh3cDot11LocalACModelAlias_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 1, 1, 8, 1, 1),
    _Hh3cDot11LocalACModelAlias_Type()
)
hh3cDot11LocalACModelAlias.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cDot11LocalACModelAlias.setStatus("current")
_Hh3cDot11LocalACModelName_Type = OctetString
_Hh3cDot11LocalACModelName_Object = MibTableColumn
hh3cDot11LocalACModelName = _Hh3cDot11LocalACModelName_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 1, 1, 8, 1, 2),
    _Hh3cDot11LocalACModelName_Type()
)
hh3cDot11LocalACModelName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11LocalACModelName.setStatus("current")
_Hh3cDot11LocalACManufacturer_Type = OctetString
_Hh3cDot11LocalACManufacturer_Object = MibTableColumn
hh3cDot11LocalACManufacturer = _Hh3cDot11LocalACManufacturer_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 1, 1, 8, 1, 3),
    _Hh3cDot11LocalACManufacturer_Type()
)
hh3cDot11LocalACManufacturer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11LocalACManufacturer.setStatus("current")
_Hh3cDot11LocalACCPUType_Type = OctetString
_Hh3cDot11LocalACCPUType_Object = MibTableColumn
hh3cDot11LocalACCPUType = _Hh3cDot11LocalACCPUType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 1, 1, 8, 1, 4),
    _Hh3cDot11LocalACCPUType_Type()
)
hh3cDot11LocalACCPUType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11LocalACCPUType.setStatus("current")
_Hh3cDot11LocalACCPUClockSpeed_Type = Unsigned32
_Hh3cDot11LocalACCPUClockSpeed_Object = MibTableColumn
hh3cDot11LocalACCPUClockSpeed = _Hh3cDot11LocalACCPUClockSpeed_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 1, 1, 8, 1, 5),
    _Hh3cDot11LocalACCPUClockSpeed_Type()
)
hh3cDot11LocalACCPUClockSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11LocalACCPUClockSpeed.setStatus("current")
if mibBuilder.loadTexts:
    hh3cDot11LocalACCPUClockSpeed.setUnits("Hz")
_Hh3cDot11LocalACMemoryType_Type = OctetString
_Hh3cDot11LocalACMemoryType_Object = MibTableColumn
hh3cDot11LocalACMemoryType = _Hh3cDot11LocalACMemoryType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 1, 1, 8, 1, 6),
    _Hh3cDot11LocalACMemoryType_Type()
)
hh3cDot11LocalACMemoryType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11LocalACMemoryType.setStatus("current")
_Hh3cDot11LocalACMemorySize_Type = Unsigned32
_Hh3cDot11LocalACMemorySize_Object = MibTableColumn
hh3cDot11LocalACMemorySize = _Hh3cDot11LocalACMemorySize_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 1, 1, 8, 1, 7),
    _Hh3cDot11LocalACMemorySize_Type()
)
hh3cDot11LocalACMemorySize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11LocalACMemorySize.setStatus("current")
if mibBuilder.loadTexts:
    hh3cDot11LocalACMemorySize.setUnits("kbytes")
_Hh3cDot11LocalACFlashType_Type = OctetString
_Hh3cDot11LocalACFlashType_Object = MibTableColumn
hh3cDot11LocalACFlashType = _Hh3cDot11LocalACFlashType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 1, 1, 8, 1, 8),
    _Hh3cDot11LocalACFlashType_Type()
)
hh3cDot11LocalACFlashType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11LocalACFlashType.setStatus("current")
_Hh3cDot11LocalACFlashSize_Type = Unsigned32
_Hh3cDot11LocalACFlashSize_Object = MibTableColumn
hh3cDot11LocalACFlashSize = _Hh3cDot11LocalACFlashSize_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 1, 1, 8, 1, 9),
    _Hh3cDot11LocalACFlashSize_Type()
)
hh3cDot11LocalACFlashSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11LocalACFlashSize.setStatus("current")
if mibBuilder.loadTexts:
    hh3cDot11LocalACFlashSize.setUnits("kbytes")
_Hh3cDot11LocalACMemSize_Type = Counter64
_Hh3cDot11LocalACMemSize_Object = MibTableColumn
hh3cDot11LocalACMemSize = _Hh3cDot11LocalACMemSize_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 1, 1, 8, 1, 10),
    _Hh3cDot11LocalACMemSize_Type()
)
hh3cDot11LocalACMemSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11LocalACMemSize.setStatus("current")
if mibBuilder.loadTexts:
    hh3cDot11LocalACMemSize.setUnits("bytes")
_Hh3cDot11LocalACFlashSizeInBytes_Type = Counter64
_Hh3cDot11LocalACFlashSizeInBytes_Object = MibTableColumn
hh3cDot11LocalACFlashSizeInBytes = _Hh3cDot11LocalACFlashSizeInBytes_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 1, 1, 8, 1, 11),
    _Hh3cDot11LocalACFlashSizeInBytes_Type()
)
hh3cDot11LocalACFlashSizeInBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11LocalACFlashSizeInBytes.setStatus("current")
if mibBuilder.loadTexts:
    hh3cDot11LocalACFlashSizeInBytes.setUnits("bytes")
_Hh3cDot11CAPWAPTunnelGroup_ObjectIdentity = ObjectIdentity
hh3cDot11CAPWAPTunnelGroup = _Hh3cDot11CAPWAPTunnelGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 1, 2)
)
_Hh3cDot11CAPWAPTunnelTable_Object = MibTable
hh3cDot11CAPWAPTunnelTable = _Hh3cDot11CAPWAPTunnelTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 1, 2, 1)
)
if mibBuilder.loadTexts:
    hh3cDot11CAPWAPTunnelTable.setStatus("current")
_Hh3cDot11CAPWAPTunnelEntry_Object = MibTableRow
hh3cDot11CAPWAPTunnelEntry = _Hh3cDot11CAPWAPTunnelEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 1, 2, 1, 1)
)
hh3cDot11CAPWAPTunnelEntry.setIndexNames(
    (0, "HH3C-DOT11-ACMT-MIB", "hh3cDot11CurrTunnelAPID"),
)
if mibBuilder.loadTexts:
    hh3cDot11CAPWAPTunnelEntry.setStatus("current")
_Hh3cDot11CurrTunnelAPID_Type = Hh3cDot11ObjectIDType
_Hh3cDot11CurrTunnelAPID_Object = MibTableColumn
hh3cDot11CurrTunnelAPID = _Hh3cDot11CurrTunnelAPID_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 1, 2, 1, 1, 1),
    _Hh3cDot11CurrTunnelAPID_Type()
)
hh3cDot11CurrTunnelAPID.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cDot11CurrTunnelAPID.setStatus("current")


class _Hh3cDot11CtrlTunnelCurrSec_Type(Hh3cDot11TunnelSecSchemType):
    """Custom type hh3cDot11CtrlTunnelCurrSec based on Hh3cDot11TunnelSecSchemType"""
    defaultValue = 1


_Hh3cDot11CtrlTunnelCurrSec_Type.__name__ = "Hh3cDot11TunnelSecSchemType"
_Hh3cDot11CtrlTunnelCurrSec_Object = MibTableColumn
hh3cDot11CtrlTunnelCurrSec = _Hh3cDot11CtrlTunnelCurrSec_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 1, 2, 1, 1, 2),
    _Hh3cDot11CtrlTunnelCurrSec_Type()
)
hh3cDot11CtrlTunnelCurrSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11CtrlTunnelCurrSec.setStatus("current")
_Hh3cDot11CtrlTunnelUpTime_Type = Integer32
_Hh3cDot11CtrlTunnelUpTime_Object = MibTableColumn
hh3cDot11CtrlTunnelUpTime = _Hh3cDot11CtrlTunnelUpTime_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 1, 2, 1, 1, 3),
    _Hh3cDot11CtrlTunnelUpTime_Type()
)
hh3cDot11CtrlTunnelUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11CtrlTunnelUpTime.setStatus("current")
if mibBuilder.loadTexts:
    hh3cDot11CtrlTunnelUpTime.setUnits("second")


class _Hh3cDot11DataTunnelCurrSec_Type(Hh3cDot11TunnelSecSchemType):
    """Custom type hh3cDot11DataTunnelCurrSec based on Hh3cDot11TunnelSecSchemType"""
    defaultValue = 1


_Hh3cDot11DataTunnelCurrSec_Type.__name__ = "Hh3cDot11TunnelSecSchemType"
_Hh3cDot11DataTunnelCurrSec_Object = MibTableColumn
hh3cDot11DataTunnelCurrSec = _Hh3cDot11DataTunnelCurrSec_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 1, 2, 1, 1, 4),
    _Hh3cDot11DataTunnelCurrSec_Type()
)
hh3cDot11DataTunnelCurrSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11DataTunnelCurrSec.setStatus("current")
_Hh3cDot11DataTunnelUpTime_Type = Integer32
_Hh3cDot11DataTunnelUpTime_Object = MibTableColumn
hh3cDot11DataTunnelUpTime = _Hh3cDot11DataTunnelUpTime_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 1, 2, 1, 1, 5),
    _Hh3cDot11DataTunnelUpTime_Type()
)
hh3cDot11DataTunnelUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11DataTunnelUpTime.setStatus("current")
if mibBuilder.loadTexts:
    hh3cDot11DataTunnelUpTime.setUnits("second")
_Hh3cDot11CtrlTunnelUpTimeTicks_Type = TimeTicks
_Hh3cDot11CtrlTunnelUpTimeTicks_Object = MibTableColumn
hh3cDot11CtrlTunnelUpTimeTicks = _Hh3cDot11CtrlTunnelUpTimeTicks_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 1, 2, 1, 1, 6),
    _Hh3cDot11CtrlTunnelUpTimeTicks_Type()
)
hh3cDot11CtrlTunnelUpTimeTicks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDot11CtrlTunnelUpTimeTicks.setStatus("current")
_Hh3cDot11ACMtNotifyGroup_ObjectIdentity = ObjectIdentity
hh3cDot11ACMtNotifyGroup = _Hh3cDot11ACMtNotifyGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 1, 3)
)
_Hh3cDot11ACMtTraps_ObjectIdentity = ObjectIdentity
hh3cDot11ACMtTraps = _Hh3cDot11ACMtTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 1, 3, 0)
)
_Hh3cDot11ACMtTrapVarObjects_ObjectIdentity = ObjectIdentity
hh3cDot11ACMtTrapVarObjects = _Hh3cDot11ACMtTrapVarObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 1, 3, 1)
)


class _Hh3cDot11ACMtTrapTunlDwnInfo_Type(Integer32):
    """Custom type hh3cDot11ACMtTrapTunlDwnInfo based on Integer32"""
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
        *(("tunnelTimeout", 1),
          ("keyUpdateFailure", 2),
          ("apReset", 3),
          ("apCrash", 4),
          ("apDeleted", 5),
          ("apCfgChange", 6))
    )


_Hh3cDot11ACMtTrapTunlDwnInfo_Type.__name__ = "Integer32"
_Hh3cDot11ACMtTrapTunlDwnInfo_Object = MibScalar
hh3cDot11ACMtTrapTunlDwnInfo = _Hh3cDot11ACMtTrapTunlDwnInfo_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 1, 3, 1, 1),
    _Hh3cDot11ACMtTrapTunlDwnInfo_Type()
)
hh3cDot11ACMtTrapTunlDwnInfo.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cDot11ACMtTrapTunlDwnInfo.setStatus("current")


class _Hh3cDot11ACMtTrapTunlUpInfo_Type(Integer32):
    """Custom type hh3cDot11ACMtTrapTunlUpInfo based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("up", 1)
    )


_Hh3cDot11ACMtTrapTunlUpInfo_Type.__name__ = "Integer32"
_Hh3cDot11ACMtTrapTunlUpInfo_Object = MibScalar
hh3cDot11ACMtTrapTunlUpInfo = _Hh3cDot11ACMtTrapTunlUpInfo_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 1, 3, 1, 2),
    _Hh3cDot11ACMtTrapTunlUpInfo_Type()
)
hh3cDot11ACMtTrapTunlUpInfo.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cDot11ACMtTrapTunlUpInfo.setStatus("current")


class _Hh3cDot11ACMtTrapBackupSwitchInfo_Type(Integer32):
    """Custom type hh3cDot11ACMtTrapBackupSwitchInfo based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("masterToSlave", 1),
          ("slaveToMaster", 2))
    )


_Hh3cDot11ACMtTrapBackupSwitchInfo_Type.__name__ = "Integer32"
_Hh3cDot11ACMtTrapBackupSwitchInfo_Object = MibScalar
hh3cDot11ACMtTrapBackupSwitchInfo = _Hh3cDot11ACMtTrapBackupSwitchInfo_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 1, 3, 1, 3),
    _Hh3cDot11ACMtTrapBackupSwitchInfo_Type()
)
hh3cDot11ACMtTrapBackupSwitchInfo.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cDot11ACMtTrapBackupSwitchInfo.setStatus("current")
_Hh3cDot11ACMtTrapTnlAPName_Type = OctetString
_Hh3cDot11ACMtTrapTnlAPName_Object = MibScalar
hh3cDot11ACMtTrapTnlAPName = _Hh3cDot11ACMtTrapTnlAPName_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 1, 3, 1, 4),
    _Hh3cDot11ACMtTrapTnlAPName_Type()
)
hh3cDot11ACMtTrapTnlAPName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cDot11ACMtTrapTnlAPName.setStatus("current")
_Hh3cDot11ACMtTrapTnlAPIPAddr_Type = IpAddress
_Hh3cDot11ACMtTrapTnlAPIPAddr_Object = MibScalar
hh3cDot11ACMtTrapTnlAPIPAddr = _Hh3cDot11ACMtTrapTnlAPIPAddr_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 1, 3, 1, 5),
    _Hh3cDot11ACMtTrapTnlAPIPAddr_Type()
)
hh3cDot11ACMtTrapTnlAPIPAddr.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cDot11ACMtTrapTnlAPIPAddr.setStatus("current")


class _Hh3cDot11LoadBalanceType_Type(Integer32):
    """Custom type hh3cDot11LoadBalanceType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("traffic", 1),
          ("session", 2))
    )


_Hh3cDot11LoadBalanceType_Type.__name__ = "Integer32"
_Hh3cDot11LoadBalanceType_Object = MibScalar
hh3cDot11LoadBalanceType = _Hh3cDot11LoadBalanceType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 1, 3, 1, 6),
    _Hh3cDot11LoadBalanceType_Type()
)
hh3cDot11LoadBalanceType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cDot11LoadBalanceType.setStatus("current")
_Hh3cDot11LoadBalanceThreshold_Type = Integer32
_Hh3cDot11LoadBalanceThreshold_Object = MibScalar
hh3cDot11LoadBalanceThreshold = _Hh3cDot11LoadBalanceThreshold_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 1, 3, 1, 7),
    _Hh3cDot11LoadBalanceThreshold_Type()
)
hh3cDot11LoadBalanceThreshold.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cDot11LoadBalanceThreshold.setStatus("current")
_Hh3cDot11ACMtTrapAPIPv6Addr_Type = OctetString
_Hh3cDot11ACMtTrapAPIPv6Addr_Object = MibScalar
hh3cDot11ACMtTrapAPIPv6Addr = _Hh3cDot11ACMtTrapAPIPv6Addr_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 1, 3, 1, 8),
    _Hh3cDot11ACMtTrapAPIPv6Addr_Type()
)
hh3cDot11ACMtTrapAPIPv6Addr.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cDot11ACMtTrapAPIPv6Addr.setStatus("current")
_Hh3cDot11ACMtTrapTunlDwnCount_Type = Integer32
_Hh3cDot11ACMtTrapTunlDwnCount_Object = MibScalar
hh3cDot11ACMtTrapTunlDwnCount = _Hh3cDot11ACMtTrapTunlDwnCount_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 1, 3, 1, 9),
    _Hh3cDot11ACMtTrapTunlDwnCount_Type()
)
hh3cDot11ACMtTrapTunlDwnCount.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cDot11ACMtTrapTunlDwnCount.setStatus("current")
_Hh3cDot11ACMaxStaNum_Type = Integer32
_Hh3cDot11ACMaxStaNum_Object = MibScalar
hh3cDot11ACMaxStaNum = _Hh3cDot11ACMaxStaNum_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 1, 3, 1, 10),
    _Hh3cDot11ACMaxStaNum_Type()
)
hh3cDot11ACMaxStaNum.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cDot11ACMaxStaNum.setStatus("current")
_Hh3cDot11ACMtTrapTnlAPSysName_Type = OctetString
_Hh3cDot11ACMtTrapTnlAPSysName_Object = MibScalar
hh3cDot11ACMtTrapTnlAPSysName = _Hh3cDot11ACMtTrapTnlAPSysName_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 1, 3, 1, 11),
    _Hh3cDot11ACMtTrapTnlAPSysName_Type()
)
hh3cDot11ACMtTrapTnlAPSysName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cDot11ACMtTrapTnlAPSysName.setStatus("current")
_Hh3cDot11ACMtFirstTrapTime_Type = TimeTicks
_Hh3cDot11ACMtFirstTrapTime_Object = MibScalar
hh3cDot11ACMtFirstTrapTime = _Hh3cDot11ACMtFirstTrapTime_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 1, 3, 1, 12),
    _Hh3cDot11ACMtFirstTrapTime_Type()
)
hh3cDot11ACMtFirstTrapTime.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cDot11ACMtFirstTrapTime.setStatus("current")


class _Hh3cDot11ACStatusSwitchInfo_Type(Integer32):
    """Custom type hh3cDot11ACStatusSwitchInfo based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("activeToStandby", 1),
          ("standbyToActive", 2))
    )


_Hh3cDot11ACStatusSwitchInfo_Type.__name__ = "Integer32"
_Hh3cDot11ACStatusSwitchInfo_Object = MibScalar
hh3cDot11ACStatusSwitchInfo = _Hh3cDot11ACStatusSwitchInfo_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 1, 3, 1, 13),
    _Hh3cDot11ACStatusSwitchInfo_Type()
)
hh3cDot11ACStatusSwitchInfo.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cDot11ACStatusSwitchInfo.setStatus("current")
_Hh3cDot11SourceACNmsIP_Type = IpAddress
_Hh3cDot11SourceACNmsIP_Object = MibScalar
hh3cDot11SourceACNmsIP = _Hh3cDot11SourceACNmsIP_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 1, 3, 1, 14),
    _Hh3cDot11SourceACNmsIP_Type()
)
hh3cDot11SourceACNmsIP.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cDot11SourceACNmsIP.setStatus("current")
_Hh3cDot11ACMtTrapAPMacAddress_Type = MacAddress
_Hh3cDot11ACMtTrapAPMacAddress_Object = MibScalar
hh3cDot11ACMtTrapAPMacAddress = _Hh3cDot11ACMtTrapAPMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 1, 3, 1, 15),
    _Hh3cDot11ACMtTrapAPMacAddress_Type()
)
hh3cDot11ACMtTrapAPMacAddress.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cDot11ACMtTrapAPMacAddress.setStatus("current")
_Hh3cDot11ACMtTrapACMacAddress_Type = MacAddress
_Hh3cDot11ACMtTrapACMacAddress_Object = MibScalar
hh3cDot11ACMtTrapACMacAddress = _Hh3cDot11ACMtTrapACMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 1, 3, 1, 16),
    _Hh3cDot11ACMtTrapACMacAddress_Type()
)
hh3cDot11ACMtTrapACMacAddress.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cDot11ACMtTrapACMacAddress.setStatus("current")

# Managed Objects groups


# Notification objects

hh3cDot11ACMtTunnelSetupTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 1, 3, 0, 1)
)
hh3cDot11ACMtTunnelSetupTrap.setObjects(
      *(("HH3C-DOT11-ACMT-MIB", "hh3cDot11CurrTunnelAPID"),
        ("HH3C-DOT11-ACMT-MIB", "hh3cDot11ACMtTrapTunlUpInfo"),
        ("HH3C-DOT11-ACMT-MIB", "hh3cDot11ACMtTrapTnlAPName"),
        ("HH3C-DOT11-ACMT-MIB", "hh3cDot11ACMtTrapTnlAPIPAddr"),
        ("HH3C-DOT11-ACMT-MIB", "hh3cDot11ACMtTrapAPIPv6Addr"),
        ("HH3C-DOT11-ACMT-MIB", "hh3cDot11ACMtFirstTrapTime"),
        ("HH3C-DOT11-ACMT-MIB", "hh3cDot11ACMtTrapAPMacAddress"))
)
if mibBuilder.loadTexts:
    hh3cDot11ACMtTunnelSetupTrap.setStatus(
        "current"
    )

hh3cDot11ACMtTunnelDownTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 1, 3, 0, 2)
)
hh3cDot11ACMtTunnelDownTrap.setObjects(
      *(("HH3C-DOT11-ACMT-MIB", "hh3cDot11CurrTunnelAPID"),
        ("HH3C-DOT11-ACMT-MIB", "hh3cDot11ACMtTrapTunlDwnInfo"),
        ("HH3C-DOT11-ACMT-MIB", "hh3cDot11ACMtTrapTnlAPName"),
        ("HH3C-DOT11-ACMT-MIB", "hh3cDot11ACMtTrapTnlAPIPAddr"),
        ("HH3C-DOT11-ACMT-MIB", "hh3cDot11ACMtTrapAPIPv6Addr"),
        ("HH3C-DOT11-ACMT-MIB", "hh3cDot11ACMtTrapTunlDwnCount"),
        ("HH3C-DOT11-ACMT-MIB", "hh3cDot11ACMtTrapTnlAPSysName"),
        ("HH3C-DOT11-ACMT-MIB", "hh3cDot11ACMtFirstTrapTime"),
        ("HH3C-DOT11-ACMT-MIB", "hh3cDot11ACMtTrapAPMacAddress"))
)
if mibBuilder.loadTexts:
    hh3cDot11ACMtTunnelDownTrap.setStatus(
        "current"
    )

hh3cDot11ACMtBackupSwtTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 1, 3, 0, 3)
)
hh3cDot11ACMtBackupSwtTrap.setObjects(
      *(("HH3C-DOT11-ACMT-MIB", "hh3cDot11ACMtTrapBackupSwitchInfo"),
        ("HH3C-DOT11-ACMT-MIB", "hh3cDot11ACMtFirstTrapTime"))
)
if mibBuilder.loadTexts:
    hh3cDot11ACMtBackupSwtTrap.setStatus(
        "current"
    )

hh3cDot11ACLoadBalanceTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 1, 3, 0, 4)
)
hh3cDot11ACLoadBalanceTrap.setObjects(
      *(("HH3C-DOT11-ACMT-MIB", "hh3cDot11LoadBalanceType"),
        ("HH3C-DOT11-ACMT-MIB", "hh3cDot11LoadBalanceThreshold"))
)
if mibBuilder.loadTexts:
    hh3cDot11ACLoadBalanceTrap.setStatus(
        "current"
    )

hh3cDot11ACStaFullTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 1, 3, 0, 5)
)
hh3cDot11ACStaFullTrap.setObjects(
    ("HH3C-DOT11-ACMT-MIB", "hh3cDot11ACMaxStaNum")
)
if mibBuilder.loadTexts:
    hh3cDot11ACStaFullTrap.setStatus(
        "current"
    )

hh3cDot11ACStatusSwitchTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 1, 3, 0, 6)
)
hh3cDot11ACStatusSwitchTrap.setObjects(
      *(("HH3C-DOT11-ACMT-MIB", "hh3cDot11ACStatusSwitchInfo"),
        ("HH3C-DOT11-ACMT-MIB", "hh3cDot11SourceACNmsIP"))
)
if mibBuilder.loadTexts:
    hh3cDot11ACStatusSwitchTrap.setStatus(
        "current"
    )

hh3cDot11RunAPNumOverload = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 1, 3, 0, 7)
)
hh3cDot11RunAPNumOverload.setObjects(
      *(("HH3C-DOT11-ACMT-MIB", "hh3cDot11MaxAPNumPermitted"),
        ("HH3C-DOT11-ACMT-MIB", "hh3cDot11APConnectCount"))
)
if mibBuilder.loadTexts:
    hh3cDot11RunAPNumOverload.setStatus(
        "current"
    )

hh3cDot11RunAPNumOverloadRecover = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 1, 3, 0, 8)
)
hh3cDot11RunAPNumOverloadRecover.setObjects(
      *(("HH3C-DOT11-ACMT-MIB", "hh3cDot11MaxAPNumPermitted"),
        ("HH3C-DOT11-ACMT-MIB", "hh3cDot11APConnectCount"))
)
if mibBuilder.loadTexts:
    hh3cDot11RunAPNumOverloadRecover.setStatus(
        "current"
    )

hh3cDot11APInvalidCertificateTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 75, 1, 3, 0, 9)
)
hh3cDot11APInvalidCertificateTrap.setObjects(
      *(("HH3C-DOT11-ACMT-MIB", "hh3cDot11ACMtTrapACMacAddress"),
        ("HH3C-DOT11-ACMT-MIB", "hh3cDot11ACMtTrapAPMacAddress"))
)
if mibBuilder.loadTexts:
    hh3cDot11APInvalidCertificateTrap.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HH3C-DOT11-ACMT-MIB",
    **{"hh3cDot11ACMT": hh3cDot11ACMT,
       "hh3cDot11ACObjectGroup": hh3cDot11ACObjectGroup,
       "hh3cDot11ACObject": hh3cDot11ACObject,
       "hh3cDot11CurrentACMACMode": hh3cDot11CurrentACMACMode,
       "hh3cDot11MaxAPNumPermitted": hh3cDot11MaxAPNumPermitted,
       "hh3cDot11MaxStationNumPermitted": hh3cDot11MaxStationNumPermitted,
       "hh3cDot11RunAPNumThreshold": hh3cDot11RunAPNumThreshold,
       "hh3cDot11MaxNewConnCntPerSecCM": hh3cDot11MaxNewConnCntPerSecCM,
       "hh3cDot11IFNumberCM": hh3cDot11IFNumberCM,
       "hh3cDot11APLicenseWeight": hh3cDot11APLicenseWeight,
       "hh3cDot11ACTotalRebootCnt": hh3cDot11ACTotalRebootCnt,
       "hh3cDot11ACLoadInfo": hh3cDot11ACLoadInfo,
       "hh3cDot11APConnectCount": hh3cDot11APConnectCount,
       "hh3cDot11StationConnectCount": hh3cDot11StationConnectCount,
       "hh3cDot11ACIFLoadInfoTable": hh3cDot11ACIFLoadInfoTable,
       "hh3cDot11ACIFLoadInfoEntry": hh3cDot11ACIFLoadInfoEntry,
       "hh3cDot11ACIfIndex": hh3cDot11ACIfIndex,
       "hh3cDot11ACIfApNum": hh3cDot11ACIfApNum,
       "hh3cDot11ACIfStaNum": hh3cDot11ACIfStaNum,
       "hh3cDot11ACIfName": hh3cDot11ACIfName,
       "hh3cDot11MasterAPCount": hh3cDot11MasterAPCount,
       "hh3cDot11SlaveAPCount": hh3cDot11SlaveAPCount,
       "hh3cDot11ConnectAutoAPCount": hh3cDot11ConnectAutoAPCount,
       "hh3cDot11PersistentAPCount": hh3cDot11PersistentAPCount,
       "hh3cDot11AcUploadFrameCnt": hh3cDot11AcUploadFrameCnt,
       "hh3cDot11AcDownloadFrameCnt": hh3cDot11AcDownloadFrameCnt,
       "hh3cDot11AcUploadFrameBytes": hh3cDot11AcUploadFrameBytes,
       "hh3cDot11AcDownloadFrameBytes": hh3cDot11AcDownloadFrameBytes,
       "hh3cDot11BackupACRole": hh3cDot11BackupACRole,
       "hh3cDot11BackupACNMSIP": hh3cDot11BackupACNMSIP,
       "hh3cDot11ACBackupMode": hh3cDot11ACBackupMode,
       "hh3cDot11ACBackupStatus": hh3cDot11ACBackupStatus,
       "hh3cDot11ACSwitchCnt": hh3cDot11ACSwitchCnt,
       "hh3cDot11ACSouthifPacketOutputCount": hh3cDot11ACSouthifPacketOutputCount,
       "hh3cDot11ACSouthifPacketOutputBytes": hh3cDot11ACSouthifPacketOutputBytes,
       "hh3cDot11ACSouthifPacketInputCount": hh3cDot11ACSouthifPacketInputCount,
       "hh3cDot11ACSouthifPacketInputBytes": hh3cDot11ACSouthifPacketInputBytes,
       "hh3cDot11TotalAPconnected": hh3cDot11TotalAPconnected,
       "hh3cDot11RemainingAPcapacity": hh3cDot11RemainingAPcapacity,
       "hh3cDot11WLANAssocStatisInfo": hh3cDot11WLANAssocStatisInfo,
       "hh3cDot11StationAssocSum": hh3cDot11StationAssocSum,
       "hh3cDot11StationAssocFailSum": hh3cDot11StationAssocFailSum,
       "hh3cDot11StationReassocSum": hh3cDot11StationReassocSum,
       "hh3cDot11StationAssocRejectedSum": hh3cDot11StationAssocRejectedSum,
       "hh3cDot11StationExDeAuthenSum": hh3cDot11StationExDeAuthenSum,
       "hh3cDot11StationCurAssocSum": hh3cDot11StationCurAssocSum,
       "hh3cDot11StationAssocReqSum": hh3cDot11StationAssocReqSum,
       "hh3cDot11StationReassocReqSum": hh3cDot11StationReassocReqSum,
       "hh3cDot11StationReassocFailSum": hh3cDot11StationReassocFailSum,
       "hh3cDot11ACBASInfo": hh3cDot11ACBASInfo,
       "hh3cDot11ACBASSysObjects": hh3cDot11ACBASSysObjects,
       "hh3cDot11ACBASTableObjects": hh3cDot11ACBASTableObjects,
       "hh3cDot11ACBASIfTable": hh3cDot11ACBASIfTable,
       "hh3cDot11ACBASIfEntry": hh3cDot11ACBASIfEntry,
       "hh3cDot11ACBASIfIndex": hh3cDot11ACBASIfIndex,
       "hh3cDot11ACBASIfDescr": hh3cDot11ACBASIfDescr,
       "hh3cDot11ACBASIfType": hh3cDot11ACBASIfType,
       "hh3cDot11ACStaUserSecAuthStatis": hh3cDot11ACStaUserSecAuthStatis,
       "hh3cDot11ACStaUserAuthCurNumber": hh3cDot11ACStaUserAuthCurNumber,
       "hh3cDot11ACStaUserConnFailCnt": hh3cDot11ACStaUserConnFailCnt,
       "hh3cDot11ACStaUserAuthReqCnt": hh3cDot11ACStaUserAuthReqCnt,
       "hh3cDot11ACStaUserAuthSuccCnt": hh3cDot11ACStaUserAuthSuccCnt,
       "hh3cDot11ACStaUserAuthFailCnt": hh3cDot11ACStaUserAuthFailCnt,
       "hh3cDot11ACStaUserAllAuthCntCM": hh3cDot11ACStaUserAllAuthCntCM,
       "hh3cDot11ACStaUserAuthRespCntCM": hh3cDot11ACStaUserAuthRespCntCM,
       "hh3cDot11ACStaSecAuthTypeStatis": hh3cDot11ACStaSecAuthTypeStatis,
       "hh3cDot11ACStaUserPortalOnlineNum": hh3cDot11ACStaUserPortalOnlineNum,
       "hh3cDot11ACStaUserFreeAuthOnlineNum": hh3cDot11ACStaUserFreeAuthOnlineNum,
       "hh3cDot11ACStaUserAssociateAuthOnlineNum": hh3cDot11ACStaUserAssociateAuthOnlineNum,
       "hh3cDot11ACStaUserMacAuthOnlineNum": hh3cDot11ACStaUserMacAuthOnlineNum,
       "hh3cDot11ACStaUserPortalLostConnectionCnt": hh3cDot11ACStaUserPortalLostConnectionCnt,
       "hh3cDot11ACStaUserFreeAuthLostConnectionCnt": hh3cDot11ACStaUserFreeAuthLostConnectionCnt,
       "hh3cDot11ACStaUserAssociateAuthLostConnectionCnt": hh3cDot11ACStaUserAssociateAuthLostConnectionCnt,
       "hh3cDot11ACStaUserMacAuthLostConnectionCnt": hh3cDot11ACStaUserMacAuthLostConnectionCnt,
       "hh3cDot11ACStaPortalAuthReqCnt": hh3cDot11ACStaPortalAuthReqCnt,
       "hh3cDot11ACStaAssociateAuthReqCnt": hh3cDot11ACStaAssociateAuthReqCnt,
       "hh3cDot11ACStaMacAuthReqCnt": hh3cDot11ACStaMacAuthReqCnt,
       "hh3cDot11ACStaPortalAuthSuccCnt": hh3cDot11ACStaPortalAuthSuccCnt,
       "hh3cDot11ACStaAssociateAuthSuccCnt": hh3cDot11ACStaAssociateAuthSuccCnt,
       "hh3cDot11ACStaMacAuthSuccCnt": hh3cDot11ACStaMacAuthSuccCnt,
       "hh3cDot11ACStaPortalAuthReqFailCnt": hh3cDot11ACStaPortalAuthReqFailCnt,
       "hh3cDot11ACStaAssociateAuthReqFailCnt": hh3cDot11ACStaAssociateAuthReqFailCnt,
       "hh3cDot11ACStaMacAuthReqFailCnt": hh3cDot11ACStaMacAuthReqFailCnt,
       "hh3cDot11ACStaUserAutoAuthOnlineNumCM": hh3cDot11ACStaUserAutoAuthOnlineNumCM,
       "hh3cDot11ACStaUserAutoAuthLostConnectionCntCM": hh3cDot11ACStaUserAutoAuthLostConnectionCntCM,
       "hh3cDot11ACStaAutoAuthReqCntCM": hh3cDot11ACStaAutoAuthReqCntCM,
       "hh3cDot11ACStaAutoAuthSuccCntCM": hh3cDot11ACStaAutoAuthSuccCntCM,
       "hh3cDot11ACStaAutoAuthReqFailCntCM": hh3cDot11ACStaAutoAuthReqFailCntCM,
       "hh3cDot11ACPortalStatisticCMTable": hh3cDot11ACPortalStatisticCMTable,
       "hh3cDot11ACPortalStatisticCMEntry": hh3cDot11ACPortalStatisticCMEntry,
       "hh3cDot11ACPortalStatisticSSIDCM": hh3cDot11ACPortalStatisticSSIDCM,
       "hh3cDot11ACPortalStatAuthReqCM": hh3cDot11ACPortalStatAuthReqCM,
       "hh3cDot11ACPortalStatAuthRespCM": hh3cDot11ACPortalStatAuthRespCM,
       "hh3cDot11LocalACModelTable": hh3cDot11LocalACModelTable,
       "hh3cDot11LocalACModelEntry": hh3cDot11LocalACModelEntry,
       "hh3cDot11LocalACModelAlias": hh3cDot11LocalACModelAlias,
       "hh3cDot11LocalACModelName": hh3cDot11LocalACModelName,
       "hh3cDot11LocalACManufacturer": hh3cDot11LocalACManufacturer,
       "hh3cDot11LocalACCPUType": hh3cDot11LocalACCPUType,
       "hh3cDot11LocalACCPUClockSpeed": hh3cDot11LocalACCPUClockSpeed,
       "hh3cDot11LocalACMemoryType": hh3cDot11LocalACMemoryType,
       "hh3cDot11LocalACMemorySize": hh3cDot11LocalACMemorySize,
       "hh3cDot11LocalACFlashType": hh3cDot11LocalACFlashType,
       "hh3cDot11LocalACFlashSize": hh3cDot11LocalACFlashSize,
       "hh3cDot11LocalACMemSize": hh3cDot11LocalACMemSize,
       "hh3cDot11LocalACFlashSizeInBytes": hh3cDot11LocalACFlashSizeInBytes,
       "hh3cDot11CAPWAPTunnelGroup": hh3cDot11CAPWAPTunnelGroup,
       "hh3cDot11CAPWAPTunnelTable": hh3cDot11CAPWAPTunnelTable,
       "hh3cDot11CAPWAPTunnelEntry": hh3cDot11CAPWAPTunnelEntry,
       "hh3cDot11CurrTunnelAPID": hh3cDot11CurrTunnelAPID,
       "hh3cDot11CtrlTunnelCurrSec": hh3cDot11CtrlTunnelCurrSec,
       "hh3cDot11CtrlTunnelUpTime": hh3cDot11CtrlTunnelUpTime,
       "hh3cDot11DataTunnelCurrSec": hh3cDot11DataTunnelCurrSec,
       "hh3cDot11DataTunnelUpTime": hh3cDot11DataTunnelUpTime,
       "hh3cDot11CtrlTunnelUpTimeTicks": hh3cDot11CtrlTunnelUpTimeTicks,
       "hh3cDot11ACMtNotifyGroup": hh3cDot11ACMtNotifyGroup,
       "hh3cDot11ACMtTraps": hh3cDot11ACMtTraps,
       "hh3cDot11ACMtTunnelSetupTrap": hh3cDot11ACMtTunnelSetupTrap,
       "hh3cDot11ACMtTunnelDownTrap": hh3cDot11ACMtTunnelDownTrap,
       "hh3cDot11ACMtBackupSwtTrap": hh3cDot11ACMtBackupSwtTrap,
       "hh3cDot11ACLoadBalanceTrap": hh3cDot11ACLoadBalanceTrap,
       "hh3cDot11ACStaFullTrap": hh3cDot11ACStaFullTrap,
       "hh3cDot11ACStatusSwitchTrap": hh3cDot11ACStatusSwitchTrap,
       "hh3cDot11RunAPNumOverload": hh3cDot11RunAPNumOverload,
       "hh3cDot11RunAPNumOverloadRecover": hh3cDot11RunAPNumOverloadRecover,
       "hh3cDot11APInvalidCertificateTrap": hh3cDot11APInvalidCertificateTrap,
       "hh3cDot11ACMtTrapVarObjects": hh3cDot11ACMtTrapVarObjects,
       "hh3cDot11ACMtTrapTunlDwnInfo": hh3cDot11ACMtTrapTunlDwnInfo,
       "hh3cDot11ACMtTrapTunlUpInfo": hh3cDot11ACMtTrapTunlUpInfo,
       "hh3cDot11ACMtTrapBackupSwitchInfo": hh3cDot11ACMtTrapBackupSwitchInfo,
       "hh3cDot11ACMtTrapTnlAPName": hh3cDot11ACMtTrapTnlAPName,
       "hh3cDot11ACMtTrapTnlAPIPAddr": hh3cDot11ACMtTrapTnlAPIPAddr,
       "hh3cDot11LoadBalanceType": hh3cDot11LoadBalanceType,
       "hh3cDot11LoadBalanceThreshold": hh3cDot11LoadBalanceThreshold,
       "hh3cDot11ACMtTrapAPIPv6Addr": hh3cDot11ACMtTrapAPIPv6Addr,
       "hh3cDot11ACMtTrapTunlDwnCount": hh3cDot11ACMtTrapTunlDwnCount,
       "hh3cDot11ACMaxStaNum": hh3cDot11ACMaxStaNum,
       "hh3cDot11ACMtTrapTnlAPSysName": hh3cDot11ACMtTrapTnlAPSysName,
       "hh3cDot11ACMtFirstTrapTime": hh3cDot11ACMtFirstTrapTime,
       "hh3cDot11ACStatusSwitchInfo": hh3cDot11ACStatusSwitchInfo,
       "hh3cDot11SourceACNmsIP": hh3cDot11SourceACNmsIP,
       "hh3cDot11ACMtTrapAPMacAddress": hh3cDot11ACMtTrapAPMacAddress,
       "hh3cDot11ACMtTrapACMacAddress": hh3cDot11ACMtTrapACMacAddress}
)
