# SNMP MIB module (FIBROLAN-MIB-METRO-STAR) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\fibrolan\FIBROLAN-MIB-METRO-STAR

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

(DisplayString,
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

flMetroStar = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4467, 100, 100)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Fibrolan_ObjectIdentity = ObjectIdentity
fibrolan = _Fibrolan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4467)
)
_FibrolanSNMP_ObjectIdentity = ObjectIdentity
fibrolanSNMP = _FibrolanSNMP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4467, 100)
)
_FlMetroStarMIBConformance_ObjectIdentity = ObjectIdentity
flMetroStarMIBConformance = _FlMetroStarMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4467, 100, 100, 1)
)
_FlMetroStarMIBCompliances_ObjectIdentity = ObjectIdentity
flMetroStarMIBCompliances = _FlMetroStarMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4467, 100, 100, 1, 1)
)
_FlMetroStarMIBGroups_ObjectIdentity = ObjectIdentity
flMetroStarMIBGroups = _FlMetroStarMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4467, 100, 100, 1, 2)
)
_FlMsChassis_ObjectIdentity = ObjectIdentity
flMsChassis = _FlMsChassis_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4467, 100, 100, 10)
)
_FlMsChassisDeviceTemperature_Type = Integer32
_FlMsChassisDeviceTemperature_Object = MibScalar
flMsChassisDeviceTemperature = _FlMsChassisDeviceTemperature_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 100, 10, 1),
    _FlMsChassisDeviceTemperature_Type()
)
flMsChassisDeviceTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flMsChassisDeviceTemperature.setStatus("current")
_FlMsChassisPsuTable_Object = MibTable
flMsChassisPsuTable = _FlMsChassisPsuTable_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 100, 10, 2)
)
if mibBuilder.loadTexts:
    flMsChassisPsuTable.setStatus("current")
_FlMsChassisPsuEntry_Object = MibTableRow
flMsChassisPsuEntry = _FlMsChassisPsuEntry_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 100, 10, 2, 1)
)
flMsChassisPsuEntry.setIndexNames(
    (0, "FIBROLAN-MIB-METRO-STAR", "flMsChassisPsuIndex"),
)
if mibBuilder.loadTexts:
    flMsChassisPsuEntry.setStatus("current")
_FlMsChassisPsuIndex_Type = Integer32
_FlMsChassisPsuIndex_Object = MibTableColumn
flMsChassisPsuIndex = _FlMsChassisPsuIndex_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 100, 10, 2, 1, 1),
    _FlMsChassisPsuIndex_Type()
)
flMsChassisPsuIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flMsChassisPsuIndex.setStatus("current")


class _FlMsChassisPsuStatus_Type(Integer32):
    """Custom type flMsChassisPsuStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("fail", 0),
          ("ok", 1),
          ("notInstalled", 2))
    )


_FlMsChassisPsuStatus_Type.__name__ = "Integer32"
_FlMsChassisPsuStatus_Object = MibTableColumn
flMsChassisPsuStatus = _FlMsChassisPsuStatus_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 100, 10, 2, 1, 2),
    _FlMsChassisPsuStatus_Type()
)
flMsChassisPsuStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flMsChassisPsuStatus.setStatus("current")
_FlMsChassisModuleTable_Object = MibTable
flMsChassisModuleTable = _FlMsChassisModuleTable_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 100, 10, 3)
)
if mibBuilder.loadTexts:
    flMsChassisModuleTable.setStatus("current")
_FlMsChassisModuleEntry_Object = MibTableRow
flMsChassisModuleEntry = _FlMsChassisModuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 100, 10, 3, 1)
)
flMsChassisModuleEntry.setIndexNames(
    (0, "FIBROLAN-MIB-METRO-STAR", "flMsChassisModuleNumber"),
    (0, "FIBROLAN-MIB-METRO-STAR", "flMsChassisChannelNumber"),
)
if mibBuilder.loadTexts:
    flMsChassisModuleEntry.setStatus("current")
_FlMsChassisModuleNumber_Type = Integer32
_FlMsChassisModuleNumber_Object = MibTableColumn
flMsChassisModuleNumber = _FlMsChassisModuleNumber_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 100, 10, 3, 1, 1),
    _FlMsChassisModuleNumber_Type()
)
flMsChassisModuleNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flMsChassisModuleNumber.setStatus("current")


class _FlMsChassisModuleType_Type(Integer32):
    """Custom type flMsChassisModuleType based on Integer32"""
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
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19,
              20,
              21,
              22,
              23,
              24,
              25,
              26,
              27,
              28,
              29,
              30,
              31,
              32,
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
              9999)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 0),
          ("mcm100-02", 1),
          ("mcm110-02", 2),
          ("mcm100-01", 3),
          ("mcm1000s", 4),
          ("mcm1000t", 5),
          ("mcm110-01", 6),
          ("mcm100-rl", 7),
          ("acm110-14", 8),
          ("acm110-12", 9),
          ("msm100u", 10),
          ("mcm100-1e1", 11),
          ("mcm100-2e1", 12),
          ("mdx41", 13),
          ("mdx81", 14),
          ("msm622u", 15),
          ("pcm110-8e1", 16),
          ("pcm110-4e1", 17),
          ("pcm110-8t1", 18),
          ("pcm110-4t1", 19),
          ("mcm1000x-rl", 20),
          ("mcm1000x", 21),
          ("mcm100-1t1", 22),
          ("mcm100-2t1", 23),
          ("msm2500u", 24),
          ("mcm1000x-rl-4e1", 25),
          ("mcm1000x-rl-4t1", 26),
          ("mdx21", 27),
          ("mddx51", 28),
          ("mdx81-e", 29),
          ("mdx41-sfa", 30),
          ("mdx41-sfb", 31),
          ("fadm1-47", 32),
          ("fadm1-49", 33),
          ("fadm1-51", 34),
          ("fadm1-53", 35),
          ("fadm1-55", 36),
          ("fadm1-57", 37),
          ("fadm1-59", 38),
          ("fadm1-61", 39),
          ("fadm2-47", 40),
          ("fadm2-49", 41),
          ("fadm2-51", 42),
          ("fadm2-53", 43),
          ("fadm2-55", 44),
          ("fadm2-57", 45),
          ("fadm2-59", 46),
          ("fadm2-61", 47),
          ("mdx41-3", 48),
          ("mdx41-3sa", 49),
          ("none", 9999))
    )


_FlMsChassisModuleType_Type.__name__ = "Integer32"
_FlMsChassisModuleType_Object = MibTableColumn
flMsChassisModuleType = _FlMsChassisModuleType_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 100, 10, 3, 1, 2),
    _FlMsChassisModuleType_Type()
)
flMsChassisModuleType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flMsChassisModuleType.setStatus("current")
_FlMsChassisChannelNumber_Type = Integer32
_FlMsChassisChannelNumber_Object = MibTableColumn
flMsChassisChannelNumber = _FlMsChassisChannelNumber_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 100, 10, 3, 1, 3),
    _FlMsChassisChannelNumber_Type()
)
flMsChassisChannelNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flMsChassisChannelNumber.setStatus("current")


class _FlMsChassisChannelTpLink_Type(Integer32):
    """Custom type flMsChassisChannelTpLink based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1),
          ("n-a", 2))
    )


_FlMsChassisChannelTpLink_Type.__name__ = "Integer32"
_FlMsChassisChannelTpLink_Object = MibTableColumn
flMsChassisChannelTpLink = _FlMsChassisChannelTpLink_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 100, 10, 3, 1, 4),
    _FlMsChassisChannelTpLink_Type()
)
flMsChassisChannelTpLink.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flMsChassisChannelTpLink.setStatus("current")


class _FlMsChassisChannelFoLink_Type(Integer32):
    """Custom type flMsChassisChannelFoLink based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_FlMsChassisChannelFoLink_Type.__name__ = "Integer32"
_FlMsChassisChannelFoLink_Object = MibTableColumn
flMsChassisChannelFoLink = _FlMsChassisChannelFoLink_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 100, 10, 3, 1, 5),
    _FlMsChassisChannelFoLink_Type()
)
flMsChassisChannelFoLink.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flMsChassisChannelFoLink.setStatus("current")


class _FlMsChassisChannelRemoteDevice_Type(Integer32):
    """Custom type flMsChassisChannelRemoteDevice based on Integer32"""
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
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              9999)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("hcon-ma", 1),
          ("scon1ma", 2),
          ("fcon1ma", 3),
          ("lta41ma", 4),
          ("gsm1000ma", 5),
          ("gsm1010ma", 6),
          ("atara100", 7),
          ("lta41-1e1", 8),
          ("lta41-2e1", 9),
          ("atara1000", 10),
          ("fcon1f", 11),
          ("atara1000rm", 12),
          ("gsm1000x", 13),
          ("lta41-1t1", 14),
          ("lta41-2t1", 15),
          ("lta41-4e1", 16),
          ("lta41-4t1", 17),
          ("unknown", 9999))
    )


_FlMsChassisChannelRemoteDevice_Type.__name__ = "Integer32"
_FlMsChassisChannelRemoteDevice_Object = MibTableColumn
flMsChassisChannelRemoteDevice = _FlMsChassisChannelRemoteDevice_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 100, 10, 3, 1, 6),
    _FlMsChassisChannelRemoteDevice_Type()
)
flMsChassisChannelRemoteDevice.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flMsChassisChannelRemoteDevice.setStatus("current")


class _FlMsChassisChannelRemoteState_Type(Integer32):
    """Custom type flMsChassisChannelRemoteState based on Integer32"""
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
          ("ok", 1),
          ("powerFail", 2))
    )


_FlMsChassisChannelRemoteState_Type.__name__ = "Integer32"
_FlMsChassisChannelRemoteState_Object = MibTableColumn
flMsChassisChannelRemoteState = _FlMsChassisChannelRemoteState_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 100, 10, 3, 1, 7),
    _FlMsChassisChannelRemoteState_Type()
)
flMsChassisChannelRemoteState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flMsChassisChannelRemoteState.setStatus("current")


class _FlMsChassisChannelRemoteTpLink_Type(Integer32):
    """Custom type flMsChassisChannelRemoteTpLink based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_FlMsChassisChannelRemoteTpLink_Type.__name__ = "Integer32"
_FlMsChassisChannelRemoteTpLink_Object = MibTableColumn
flMsChassisChannelRemoteTpLink = _FlMsChassisChannelRemoteTpLink_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 100, 10, 3, 1, 8),
    _FlMsChassisChannelRemoteTpLink_Type()
)
flMsChassisChannelRemoteTpLink.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flMsChassisChannelRemoteTpLink.setStatus("current")
_FlMsChassisSwVersion_Type = DisplayString
_FlMsChassisSwVersion_Object = MibScalar
flMsChassisSwVersion = _FlMsChassisSwVersion_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 100, 10, 4),
    _FlMsChassisSwVersion_Type()
)
flMsChassisSwVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flMsChassisSwVersion.setStatus("current")
_FlMsSwUpgradeTable_Object = MibTable
flMsSwUpgradeTable = _FlMsSwUpgradeTable_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 100, 10, 5)
)
if mibBuilder.loadTexts:
    flMsSwUpgradeTable.setStatus("current")
_FlMsChassisSwUpgradeEntry_Object = MibTableRow
flMsChassisSwUpgradeEntry = _FlMsChassisSwUpgradeEntry_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 100, 10, 5, 1)
)
flMsChassisSwUpgradeEntry.setIndexNames(
    (0, "FIBROLAN-MIB-METRO-STAR", "flMsSwUpgradeTableIndex"),
)
if mibBuilder.loadTexts:
    flMsChassisSwUpgradeEntry.setStatus("current")


class _FlMsSwUpgradeTableIndex_Type(Integer32):
    """Custom type flMsSwUpgradeTableIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 11),
    )


_FlMsSwUpgradeTableIndex_Type.__name__ = "Integer32"
_FlMsSwUpgradeTableIndex_Object = MibTableColumn
flMsSwUpgradeTableIndex = _FlMsSwUpgradeTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 100, 10, 5, 1, 1),
    _FlMsSwUpgradeTableIndex_Type()
)
flMsSwUpgradeTableIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flMsSwUpgradeTableIndex.setStatus("current")
_FlMsSwUpgradeTftpServer_Type = IpAddress
_FlMsSwUpgradeTftpServer_Object = MibTableColumn
flMsSwUpgradeTftpServer = _FlMsSwUpgradeTftpServer_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 100, 10, 5, 1, 2),
    _FlMsSwUpgradeTftpServer_Type()
)
flMsSwUpgradeTftpServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flMsSwUpgradeTftpServer.setStatus("current")
_FlMsSwUpgradeCurrentVersion_Type = DisplayString
_FlMsSwUpgradeCurrentVersion_Object = MibTableColumn
flMsSwUpgradeCurrentVersion = _FlMsSwUpgradeCurrentVersion_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 100, 10, 5, 1, 3),
    _FlMsSwUpgradeCurrentVersion_Type()
)
flMsSwUpgradeCurrentVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flMsSwUpgradeCurrentVersion.setStatus("current")
_FlMsSwUpgradeRollbackVersion_Type = DisplayString
_FlMsSwUpgradeRollbackVersion_Object = MibTableColumn
flMsSwUpgradeRollbackVersion = _FlMsSwUpgradeRollbackVersion_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 100, 10, 5, 1, 4),
    _FlMsSwUpgradeRollbackVersion_Type()
)
flMsSwUpgradeRollbackVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flMsSwUpgradeRollbackVersion.setStatus("current")
_FlMsSwUpgradeNewVersion_Type = DisplayString
_FlMsSwUpgradeNewVersion_Object = MibTableColumn
flMsSwUpgradeNewVersion = _FlMsSwUpgradeNewVersion_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 100, 10, 5, 1, 5),
    _FlMsSwUpgradeNewVersion_Type()
)
flMsSwUpgradeNewVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flMsSwUpgradeNewVersion.setStatus("current")
_FlMsSwUpgradeRemoteFileName_Type = DisplayString
_FlMsSwUpgradeRemoteFileName_Object = MibTableColumn
flMsSwUpgradeRemoteFileName = _FlMsSwUpgradeRemoteFileName_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 100, 10, 5, 1, 6),
    _FlMsSwUpgradeRemoteFileName_Type()
)
flMsSwUpgradeRemoteFileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flMsSwUpgradeRemoteFileName.setStatus("current")
_FlMsSwUpgradeRemotePath_Type = DisplayString
_FlMsSwUpgradeRemotePath_Object = MibTableColumn
flMsSwUpgradeRemotePath = _FlMsSwUpgradeRemotePath_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 100, 10, 5, 1, 7),
    _FlMsSwUpgradeRemotePath_Type()
)
flMsSwUpgradeRemotePath.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flMsSwUpgradeRemotePath.setStatus("current")


class _FlMsSwUpgradeAutoReboot_Type(Integer32):
    """Custom type flMsSwUpgradeAutoReboot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2))
    )


_FlMsSwUpgradeAutoReboot_Type.__name__ = "Integer32"
_FlMsSwUpgradeAutoReboot_Object = MibTableColumn
flMsSwUpgradeAutoReboot = _FlMsSwUpgradeAutoReboot_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 100, 10, 5, 1, 8),
    _FlMsSwUpgradeAutoReboot_Type()
)
flMsSwUpgradeAutoReboot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flMsSwUpgradeAutoReboot.setStatus("current")


class _FlMsSwUpgradeProcessBegin_Type(Integer32):
    """Custom type flMsSwUpgradeProcessBegin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("normal", 1),
          ("upgrade", 2))
    )


_FlMsSwUpgradeProcessBegin_Type.__name__ = "Integer32"
_FlMsSwUpgradeProcessBegin_Object = MibTableColumn
flMsSwUpgradeProcessBegin = _FlMsSwUpgradeProcessBegin_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 100, 10, 5, 1, 9),
    _FlMsSwUpgradeProcessBegin_Type()
)
flMsSwUpgradeProcessBegin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flMsSwUpgradeProcessBegin.setStatus("current")


class _FlMsSwUpgradeRollback_Type(Integer32):
    """Custom type flMsSwUpgradeRollback based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("normal", 1),
          ("rollback", 2))
    )


_FlMsSwUpgradeRollback_Type.__name__ = "Integer32"
_FlMsSwUpgradeRollback_Object = MibTableColumn
flMsSwUpgradeRollback = _FlMsSwUpgradeRollback_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 100, 10, 5, 1, 10),
    _FlMsSwUpgradeRollback_Type()
)
flMsSwUpgradeRollback.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flMsSwUpgradeRollback.setStatus("current")


class _FlMsSwUpgradeProcessStatus_Type(Integer32):
    """Custom type flMsSwUpgradeProcessStatus based on Integer32"""
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
        *(("notStarted", 1),
          ("upgradeFailed", 2),
          ("upgradeComplete", 3),
          ("retrievingFile", 4),
          ("erasingFlash", 5),
          ("programmingFlash", 6),
          ("verifyingFlash", 7),
          ("rollbackInProgress", 8),
          ("rollbackComplete", 9))
    )


_FlMsSwUpgradeProcessStatus_Type.__name__ = "Integer32"
_FlMsSwUpgradeProcessStatus_Object = MibTableColumn
flMsSwUpgradeProcessStatus = _FlMsSwUpgradeProcessStatus_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 100, 10, 5, 1, 11),
    _FlMsSwUpgradeProcessStatus_Type()
)
flMsSwUpgradeProcessStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flMsSwUpgradeProcessStatus.setStatus("current")
_FlMsConfigUploadTable_Object = MibTable
flMsConfigUploadTable = _FlMsConfigUploadTable_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 100, 10, 6)
)
if mibBuilder.loadTexts:
    flMsConfigUploadTable.setStatus("current")
_FlMsConfigUploadEntry_Object = MibTableRow
flMsConfigUploadEntry = _FlMsConfigUploadEntry_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 100, 10, 6, 1)
)
flMsConfigUploadEntry.setIndexNames(
    (0, "FIBROLAN-MIB-METRO-STAR", "flMsConfigUploadIndex"),
)
if mibBuilder.loadTexts:
    flMsConfigUploadEntry.setStatus("current")


class _FlMsConfigUploadIndex_Type(Integer32):
    """Custom type flMsConfigUploadIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 7),
    )


_FlMsConfigUploadIndex_Type.__name__ = "Integer32"
_FlMsConfigUploadIndex_Object = MibTableColumn
flMsConfigUploadIndex = _FlMsConfigUploadIndex_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 100, 10, 6, 1, 1),
    _FlMsConfigUploadIndex_Type()
)
flMsConfigUploadIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flMsConfigUploadIndex.setStatus("current")
_FlMsConfigUploadTftpServer_Type = IpAddress
_FlMsConfigUploadTftpServer_Object = MibTableColumn
flMsConfigUploadTftpServer = _FlMsConfigUploadTftpServer_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 100, 10, 6, 1, 2),
    _FlMsConfigUploadTftpServer_Type()
)
flMsConfigUploadTftpServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flMsConfigUploadTftpServer.setStatus("current")
_FlMsConfigUploadFileName_Type = DisplayString
_FlMsConfigUploadFileName_Object = MibTableColumn
flMsConfigUploadFileName = _FlMsConfigUploadFileName_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 100, 10, 6, 1, 3),
    _FlMsConfigUploadFileName_Type()
)
flMsConfigUploadFileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flMsConfigUploadFileName.setStatus("current")


class _FlMsConfigUploadFileStatus_Type(Integer32):
    """Custom type flMsConfigUploadFileStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notLoaded", 1),
          ("loaded", 2))
    )


_FlMsConfigUploadFileStatus_Type.__name__ = "Integer32"
_FlMsConfigUploadFileStatus_Object = MibTableColumn
flMsConfigUploadFileStatus = _FlMsConfigUploadFileStatus_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 100, 10, 6, 1, 4),
    _FlMsConfigUploadFileStatus_Type()
)
flMsConfigUploadFileStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flMsConfigUploadFileStatus.setStatus("current")
_FlMsConfigUploadRemotePath_Type = DisplayString
_FlMsConfigUploadRemotePath_Object = MibTableColumn
flMsConfigUploadRemotePath = _FlMsConfigUploadRemotePath_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 100, 10, 6, 1, 5),
    _FlMsConfigUploadRemotePath_Type()
)
flMsConfigUploadRemotePath.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flMsConfigUploadRemotePath.setStatus("current")


class _FlMsConfigUploadProcessBegin_Type(Integer32):
    """Custom type flMsConfigUploadProcessBegin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("normal", 1),
          ("uploadConfig", 2))
    )


_FlMsConfigUploadProcessBegin_Type.__name__ = "Integer32"
_FlMsConfigUploadProcessBegin_Object = MibTableColumn
flMsConfigUploadProcessBegin = _FlMsConfigUploadProcessBegin_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 100, 10, 6, 1, 6),
    _FlMsConfigUploadProcessBegin_Type()
)
flMsConfigUploadProcessBegin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flMsConfigUploadProcessBegin.setStatus("current")


class _FlMsConfigUploadProcessStatus_Type(Integer32):
    """Custom type flMsConfigUploadProcessStatus based on Integer32"""
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("uploadNotStarted", 1),
          ("fileLoadInProcess", 2),
          ("fileLoadFailed", 3),
          ("fileLoadComplete", 4),
          ("configInProgress", 5),
          ("configLoadedOk", 6),
          ("partiallyConfigured", 7),
          ("configFailed", 8))
    )


_FlMsConfigUploadProcessStatus_Type.__name__ = "Integer32"
_FlMsConfigUploadProcessStatus_Object = MibTableColumn
flMsConfigUploadProcessStatus = _FlMsConfigUploadProcessStatus_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 100, 10, 6, 1, 7),
    _FlMsConfigUploadProcessStatus_Type()
)
flMsConfigUploadProcessStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flMsConfigUploadProcessStatus.setStatus("current")
_FlMsChassisConfirm_Type = DisplayString
_FlMsChassisConfirm_Object = MibScalar
flMsChassisConfirm = _FlMsChassisConfirm_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 100, 10, 7),
    _FlMsChassisConfirm_Type()
)
flMsChassisConfirm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flMsChassisConfirm.setStatus("current")


class _FlMsChassisRebootSystem_Type(Integer32):
    """Custom type flMsChassisRebootSystem based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("normal", 1),
          ("reboot", 2))
    )


_FlMsChassisRebootSystem_Type.__name__ = "Integer32"
_FlMsChassisRebootSystem_Object = MibScalar
flMsChassisRebootSystem = _FlMsChassisRebootSystem_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 100, 10, 8),
    _FlMsChassisRebootSystem_Type()
)
flMsChassisRebootSystem.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flMsChassisRebootSystem.setStatus("current")

# Managed Objects groups

flMetroStarPsuGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4467, 100, 100, 1, 2, 1)
)
flMetroStarPsuGroup.setObjects(
      *(("FIBROLAN-MIB-METRO-STAR", "flMsChassisPsuIndex"),
        ("FIBROLAN-MIB-METRO-STAR", "flMsChassisPsuStatus"))
)
if mibBuilder.loadTexts:
    flMetroStarPsuGroup.setStatus("current")

flMetroStarModulesGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4467, 100, 100, 1, 2, 2)
)
flMetroStarModulesGroup.setObjects(
      *(("FIBROLAN-MIB-METRO-STAR", "flMsChassisModuleNumber"),
        ("FIBROLAN-MIB-METRO-STAR", "flMsChassisModuleType"),
        ("FIBROLAN-MIB-METRO-STAR", "flMsChassisChannelNumber"),
        ("FIBROLAN-MIB-METRO-STAR", "flMsChassisChannelTpLink"),
        ("FIBROLAN-MIB-METRO-STAR", "flMsChassisChannelFoLink"),
        ("FIBROLAN-MIB-METRO-STAR", "flMsChassisChannelRemoteDevice"),
        ("FIBROLAN-MIB-METRO-STAR", "flMsChassisChannelRemoteState"),
        ("FIBROLAN-MIB-METRO-STAR", "flMsChassisChannelRemoteTpLink"))
)
if mibBuilder.loadTexts:
    flMetroStarModulesGroup.setStatus("current")

flMetroStarSwUpgradeGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4467, 100, 100, 1, 2, 3)
)
flMetroStarSwUpgradeGroup.setObjects(
      *(("FIBROLAN-MIB-METRO-STAR", "flMsSwUpgradeTableIndex"),
        ("FIBROLAN-MIB-METRO-STAR", "flMsSwUpgradeTftpServer"),
        ("FIBROLAN-MIB-METRO-STAR", "flMsSwUpgradeCurrentVersion"),
        ("FIBROLAN-MIB-METRO-STAR", "flMsSwUpgradeRollbackVersion"),
        ("FIBROLAN-MIB-METRO-STAR", "flMsSwUpgradeNewVersion"),
        ("FIBROLAN-MIB-METRO-STAR", "flMsSwUpgradeRemoteFileName"),
        ("FIBROLAN-MIB-METRO-STAR", "flMsSwUpgradeRemotePath"),
        ("FIBROLAN-MIB-METRO-STAR", "flMsSwUpgradeAutoReboot"),
        ("FIBROLAN-MIB-METRO-STAR", "flMsSwUpgradeProcessBegin"),
        ("FIBROLAN-MIB-METRO-STAR", "flMsSwUpgradeRollback"),
        ("FIBROLAN-MIB-METRO-STAR", "flMsSwUpgradeProcessStatus"))
)
if mibBuilder.loadTexts:
    flMetroStarSwUpgradeGroup.setStatus("current")

flMetroStarConfigUploadGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4467, 100, 100, 1, 2, 4)
)
flMetroStarConfigUploadGroup.setObjects(
      *(("FIBROLAN-MIB-METRO-STAR", "flMsConfigUploadIndex"),
        ("FIBROLAN-MIB-METRO-STAR", "flMsConfigUploadTftpServer"),
        ("FIBROLAN-MIB-METRO-STAR", "flMsConfigUploadFileName"),
        ("FIBROLAN-MIB-METRO-STAR", "flMsConfigUploadFileStatus"),
        ("FIBROLAN-MIB-METRO-STAR", "flMsConfigUploadRemotePath"),
        ("FIBROLAN-MIB-METRO-STAR", "flMsConfigUploadProcessBegin"),
        ("FIBROLAN-MIB-METRO-STAR", "flMsConfigUploadProcessStatus"))
)
if mibBuilder.loadTexts:
    flMetroStarConfigUploadGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

flMetroStarMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4467, 100, 100, 1, 1, 1)
)
flMetroStarMIBCompliance.setObjects(
      *(("FIBROLAN-MIB-METRO-STAR", "flMetroStarPsuGroup"),
        ("FIBROLAN-MIB-METRO-STAR", "flMetroStarModulesGroup"),
        ("FIBROLAN-MIB-METRO-STAR", "flMetroStarSwUpgradeGroup"),
        ("FIBROLAN-MIB-METRO-STAR", "flMetroStarConfigUploadGroup"))
)
if mibBuilder.loadTexts:
    flMetroStarMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "FIBROLAN-MIB-METRO-STAR",
    **{"fibrolan": fibrolan,
       "fibrolanSNMP": fibrolanSNMP,
       "flMetroStar": flMetroStar,
       "flMetroStarMIBConformance": flMetroStarMIBConformance,
       "flMetroStarMIBCompliances": flMetroStarMIBCompliances,
       "flMetroStarMIBCompliance": flMetroStarMIBCompliance,
       "flMetroStarMIBGroups": flMetroStarMIBGroups,
       "flMetroStarPsuGroup": flMetroStarPsuGroup,
       "flMetroStarModulesGroup": flMetroStarModulesGroup,
       "flMetroStarSwUpgradeGroup": flMetroStarSwUpgradeGroup,
       "flMetroStarConfigUploadGroup": flMetroStarConfigUploadGroup,
       "flMsChassis": flMsChassis,
       "flMsChassisDeviceTemperature": flMsChassisDeviceTemperature,
       "flMsChassisPsuTable": flMsChassisPsuTable,
       "flMsChassisPsuEntry": flMsChassisPsuEntry,
       "flMsChassisPsuIndex": flMsChassisPsuIndex,
       "flMsChassisPsuStatus": flMsChassisPsuStatus,
       "flMsChassisModuleTable": flMsChassisModuleTable,
       "flMsChassisModuleEntry": flMsChassisModuleEntry,
       "flMsChassisModuleNumber": flMsChassisModuleNumber,
       "flMsChassisModuleType": flMsChassisModuleType,
       "flMsChassisChannelNumber": flMsChassisChannelNumber,
       "flMsChassisChannelTpLink": flMsChassisChannelTpLink,
       "flMsChassisChannelFoLink": flMsChassisChannelFoLink,
       "flMsChassisChannelRemoteDevice": flMsChassisChannelRemoteDevice,
       "flMsChassisChannelRemoteState": flMsChassisChannelRemoteState,
       "flMsChassisChannelRemoteTpLink": flMsChassisChannelRemoteTpLink,
       "flMsChassisSwVersion": flMsChassisSwVersion,
       "flMsSwUpgradeTable": flMsSwUpgradeTable,
       "flMsChassisSwUpgradeEntry": flMsChassisSwUpgradeEntry,
       "flMsSwUpgradeTableIndex": flMsSwUpgradeTableIndex,
       "flMsSwUpgradeTftpServer": flMsSwUpgradeTftpServer,
       "flMsSwUpgradeCurrentVersion": flMsSwUpgradeCurrentVersion,
       "flMsSwUpgradeRollbackVersion": flMsSwUpgradeRollbackVersion,
       "flMsSwUpgradeNewVersion": flMsSwUpgradeNewVersion,
       "flMsSwUpgradeRemoteFileName": flMsSwUpgradeRemoteFileName,
       "flMsSwUpgradeRemotePath": flMsSwUpgradeRemotePath,
       "flMsSwUpgradeAutoReboot": flMsSwUpgradeAutoReboot,
       "flMsSwUpgradeProcessBegin": flMsSwUpgradeProcessBegin,
       "flMsSwUpgradeRollback": flMsSwUpgradeRollback,
       "flMsSwUpgradeProcessStatus": flMsSwUpgradeProcessStatus,
       "flMsConfigUploadTable": flMsConfigUploadTable,
       "flMsConfigUploadEntry": flMsConfigUploadEntry,
       "flMsConfigUploadIndex": flMsConfigUploadIndex,
       "flMsConfigUploadTftpServer": flMsConfigUploadTftpServer,
       "flMsConfigUploadFileName": flMsConfigUploadFileName,
       "flMsConfigUploadFileStatus": flMsConfigUploadFileStatus,
       "flMsConfigUploadRemotePath": flMsConfigUploadRemotePath,
       "flMsConfigUploadProcessBegin": flMsConfigUploadProcessBegin,
       "flMsConfigUploadProcessStatus": flMsConfigUploadProcessStatus,
       "flMsChassisConfirm": flMsChassisConfirm,
       "flMsChassisRebootSystem": flMsChassisRebootSystem}
)
