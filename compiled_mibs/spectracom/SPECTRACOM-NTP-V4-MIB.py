# SNMP MIB module (SPECTRACOM-NTP-V4-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\spectracom\SPECTRACOM-NTP-V4-MIB

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

(specModules,
 specProducts) = mibBuilder.importSymbols(
    "SPECTRACOM-GLOBAL-REG-MIB",
    "specModules",
    "specProducts")


# MODULE-IDENTITY

spectracomNtpV4MibModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 18837, 1, 1, 5)
)
if mibBuilder.loadTexts:
    spectracomNtpV4MibModule.setRevisions(
        ("2022-01-07 00:00",
         "2013-06-17 14:53",
         "2011-02-21 19:21",
         "2010-06-01 15:40")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_NtpSnmpObjs_ObjectIdentity = ObjectIdentity
ntpSnmpObjs = _NtpSnmpObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18837, 3, 3)
)
_NtpGeneralObjs_ObjectIdentity = ObjectIdentity
ntpGeneralObjs = _NtpGeneralObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18837, 3, 3, 1)
)
_NtpGenAppName_Type = DisplayString
_NtpGenAppName_Object = MibScalar
ntpGenAppName = _NtpGenAppName_Object(
    (1, 3, 6, 1, 4, 1, 18837, 3, 3, 1, 1),
    _NtpGenAppName_Type()
)
ntpGenAppName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntpGenAppName.setStatus("current")
_NtpGenAppRevision_Type = DisplayString
_NtpGenAppRevision_Object = MibScalar
ntpGenAppRevision = _NtpGenAppRevision_Object(
    (1, 3, 6, 1, 4, 1, 18837, 3, 3, 1, 2),
    _NtpGenAppRevision_Type()
)
ntpGenAppRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntpGenAppRevision.setStatus("current")
_NtpGenAppVendor_Type = DisplayString
_NtpGenAppVendor_Object = MibScalar
ntpGenAppVendor = _NtpGenAppVendor_Object(
    (1, 3, 6, 1, 4, 1, 18837, 3, 3, 1, 3),
    _NtpGenAppVendor_Type()
)
ntpGenAppVendor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntpGenAppVendor.setStatus("current")
_NtpGenSystemType_Type = DisplayString
_NtpGenSystemType_Object = MibScalar
ntpGenSystemType = _NtpGenSystemType_Object(
    (1, 3, 6, 1, 4, 1, 18837, 3, 3, 1, 4),
    _NtpGenSystemType_Type()
)
ntpGenSystemType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntpGenSystemType.setStatus("current")
_NtpSystemStatusObjs_ObjectIdentity = ObjectIdentity
ntpSystemStatusObjs = _NtpSystemStatusObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18837, 3, 3, 2)
)


class _NtpSysStaCurrentMode_Type(Integer32):
    """Custom type ntpSysStaCurrentMode based on Integer32"""
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
          ("notRunning", 2),
          ("notSynchonized", 3),
          ("synchronized", 4))
    )


_NtpSysStaCurrentMode_Type.__name__ = "Integer32"
_NtpSysStaCurrentMode_Object = MibScalar
ntpSysStaCurrentMode = _NtpSysStaCurrentMode_Object(
    (1, 3, 6, 1, 4, 1, 18837, 3, 3, 2, 1),
    _NtpSysStaCurrentMode_Type()
)
ntpSysStaCurrentMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntpSysStaCurrentMode.setStatus("current")
_NtpSysStaStratum_Type = Unsigned32
_NtpSysStaStratum_Object = MibScalar
ntpSysStaStratum = _NtpSysStaStratum_Object(
    (1, 3, 6, 1, 4, 1, 18837, 3, 3, 2, 2),
    _NtpSysStaStratum_Type()
)
ntpSysStaStratum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntpSysStaStratum.setStatus("current")
_NtpSysStaCurrentPeerAssc_Type = Unsigned32
_NtpSysStaCurrentPeerAssc_Object = MibScalar
ntpSysStaCurrentPeerAssc = _NtpSysStaCurrentPeerAssc_Object(
    (1, 3, 6, 1, 4, 1, 18837, 3, 3, 2, 3),
    _NtpSysStaCurrentPeerAssc_Type()
)
ntpSysStaCurrentPeerAssc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntpSysStaCurrentPeerAssc.setStatus("current")
_NtpSysStaCurrentPeerName_Type = DisplayString
_NtpSysStaCurrentPeerName_Object = MibScalar
ntpSysStaCurrentPeerName = _NtpSysStaCurrentPeerName_Object(
    (1, 3, 6, 1, 4, 1, 18837, 3, 3, 2, 4),
    _NtpSysStaCurrentPeerName_Type()
)
ntpSysStaCurrentPeerName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntpSysStaCurrentPeerName.setStatus("current")
_NtpSysStaPeerDelay_Type = DisplayString
_NtpSysStaPeerDelay_Object = MibScalar
ntpSysStaPeerDelay = _NtpSysStaPeerDelay_Object(
    (1, 3, 6, 1, 4, 1, 18837, 3, 3, 2, 5),
    _NtpSysStaPeerDelay_Type()
)
ntpSysStaPeerDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntpSysStaPeerDelay.setStatus("current")
if mibBuilder.loadTexts:
    ntpSysStaPeerDelay.setUnits("milliseconds")
_NtpSysStaPeerOffset_Type = DisplayString
_NtpSysStaPeerOffset_Object = MibScalar
ntpSysStaPeerOffset = _NtpSysStaPeerOffset_Object(
    (1, 3, 6, 1, 4, 1, 18837, 3, 3, 2, 6),
    _NtpSysStaPeerOffset_Type()
)
ntpSysStaPeerOffset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntpSysStaPeerOffset.setStatus("current")
if mibBuilder.loadTexts:
    ntpSysStaPeerOffset.setUnits("milliseconds")
_NtpSysStaPeerJitter_Type = DisplayString
_NtpSysStaPeerJitter_Object = MibScalar
ntpSysStaPeerJitter = _NtpSysStaPeerJitter_Object(
    (1, 3, 6, 1, 4, 1, 18837, 3, 3, 2, 7),
    _NtpSysStaPeerJitter_Type()
)
ntpSysStaPeerJitter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntpSysStaPeerJitter.setStatus("current")
if mibBuilder.loadTexts:
    ntpSysStaPeerJitter.setUnits("milliseconds")
_NtpAssociationsObjs_ObjectIdentity = ObjectIdentity
ntpAssociationsObjs = _NtpAssociationsObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18837, 3, 3, 3)
)
_NtpAssocCount_Type = Unsigned32
_NtpAssocCount_Object = MibScalar
ntpAssocCount = _NtpAssocCount_Object(
    (1, 3, 6, 1, 4, 1, 18837, 3, 3, 3, 1),
    _NtpAssocCount_Type()
)
ntpAssocCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntpAssocCount.setStatus("current")
_NtpAssocTable_Object = MibTable
ntpAssocTable = _NtpAssocTable_Object(
    (1, 3, 6, 1, 4, 1, 18837, 3, 3, 3, 2)
)
if mibBuilder.loadTexts:
    ntpAssocTable.setStatus("current")
_NtpAssocEntry_Object = MibTableRow
ntpAssocEntry = _NtpAssocEntry_Object(
    (1, 3, 6, 1, 4, 1, 18837, 3, 3, 3, 2, 1)
)
ntpAssocEntry.setIndexNames(
    (0, "SPECTRACOM-NTP-V4-MIB", "assocEntryIndex"),
)
if mibBuilder.loadTexts:
    ntpAssocEntry.setStatus("current")


class _AssocEntryIndex_Type(Unsigned32):
    """Custom type assocEntryIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_AssocEntryIndex_Type.__name__ = "Unsigned32"
_AssocEntryIndex_Object = MibTableColumn
assocEntryIndex = _AssocEntryIndex_Object(
    (1, 3, 6, 1, 4, 1, 18837, 3, 3, 3, 2, 1, 1),
    _AssocEntryIndex_Type()
)
assocEntryIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    assocEntryIndex.setStatus("current")
_AssocEntryIdentity_Type = DisplayString
_AssocEntryIdentity_Object = MibTableColumn
assocEntryIdentity = _AssocEntryIdentity_Object(
    (1, 3, 6, 1, 4, 1, 18837, 3, 3, 3, 2, 1, 2),
    _AssocEntryIdentity_Type()
)
assocEntryIdentity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    assocEntryIdentity.setStatus("current")
_AssocEntrySyncStatus_Type = DisplayString
_AssocEntrySyncStatus_Object = MibTableColumn
assocEntrySyncStatus = _AssocEntrySyncStatus_Object(
    (1, 3, 6, 1, 4, 1, 18837, 3, 3, 3, 2, 1, 3),
    _AssocEntrySyncStatus_Type()
)
assocEntrySyncStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    assocEntrySyncStatus.setStatus("current")
_AssocEntryRefId_Type = DisplayString
_AssocEntryRefId_Object = MibTableColumn
assocEntryRefId = _AssocEntryRefId_Object(
    (1, 3, 6, 1, 4, 1, 18837, 3, 3, 3, 2, 1, 4),
    _AssocEntryRefId_Type()
)
assocEntryRefId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    assocEntryRefId.setStatus("current")
_AssocEntryStratum_Type = Unsigned32
_AssocEntryStratum_Object = MibTableColumn
assocEntryStratum = _AssocEntryStratum_Object(
    (1, 3, 6, 1, 4, 1, 18837, 3, 3, 3, 2, 1, 5),
    _AssocEntryStratum_Type()
)
assocEntryStratum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    assocEntryStratum.setStatus("current")


class _AssocEntryMode_Type(Integer32):
    """Custom type assocEntryMode based on Integer32"""
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
        *(("symmetricActive", 1),
          ("symmetricPassive", 2),
          ("client", 3),
          ("server", 4),
          ("broadcast", 5))
    )


_AssocEntryMode_Type.__name__ = "Integer32"
_AssocEntryMode_Object = MibTableColumn
assocEntryMode = _AssocEntryMode_Object(
    (1, 3, 6, 1, 4, 1, 18837, 3, 3, 3, 2, 1, 6),
    _AssocEntryMode_Type()
)
assocEntryMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    assocEntryMode.setStatus("current")
_AssocEntryType_Type = DisplayString
_AssocEntryType_Object = MibTableColumn
assocEntryType = _AssocEntryType_Object(
    (1, 3, 6, 1, 4, 1, 18837, 3, 3, 3, 2, 1, 7),
    _AssocEntryType_Type()
)
assocEntryType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    assocEntryType.setStatus("current")
_AssocEntryAuthStatus_Type = DisplayString
_AssocEntryAuthStatus_Object = MibTableColumn
assocEntryAuthStatus = _AssocEntryAuthStatus_Object(
    (1, 3, 6, 1, 4, 1, 18837, 3, 3, 3, 2, 1, 8),
    _AssocEntryAuthStatus_Type()
)
assocEntryAuthStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    assocEntryAuthStatus.setStatus("current")
_AssocEntryLastPoll_Type = Unsigned32
_AssocEntryLastPoll_Object = MibTableColumn
assocEntryLastPoll = _AssocEntryLastPoll_Object(
    (1, 3, 6, 1, 4, 1, 18837, 3, 3, 3, 2, 1, 9),
    _AssocEntryLastPoll_Type()
)
assocEntryLastPoll.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    assocEntryLastPoll.setStatus("current")
_AssocEntryPollInterval_Type = Unsigned32
_AssocEntryPollInterval_Object = MibTableColumn
assocEntryPollInterval = _AssocEntryPollInterval_Object(
    (1, 3, 6, 1, 4, 1, 18837, 3, 3, 3, 2, 1, 10),
    _AssocEntryPollInterval_Type()
)
assocEntryPollInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    assocEntryPollInterval.setStatus("current")
_AssocEntryReach_Type = Unsigned32
_AssocEntryReach_Object = MibTableColumn
assocEntryReach = _AssocEntryReach_Object(
    (1, 3, 6, 1, 4, 1, 18837, 3, 3, 3, 2, 1, 11),
    _AssocEntryReach_Type()
)
assocEntryReach.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    assocEntryReach.setStatus("current")
_AssocEntryDelay_Type = DisplayString
_AssocEntryDelay_Object = MibTableColumn
assocEntryDelay = _AssocEntryDelay_Object(
    (1, 3, 6, 1, 4, 1, 18837, 3, 3, 3, 2, 1, 12),
    _AssocEntryDelay_Type()
)
assocEntryDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    assocEntryDelay.setStatus("current")
if mibBuilder.loadTexts:
    assocEntryDelay.setUnits("milliseconds")
_AssocEntryOffset_Type = DisplayString
_AssocEntryOffset_Object = MibTableColumn
assocEntryOffset = _AssocEntryOffset_Object(
    (1, 3, 6, 1, 4, 1, 18837, 3, 3, 3, 2, 1, 13),
    _AssocEntryOffset_Type()
)
assocEntryOffset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    assocEntryOffset.setStatus("current")
if mibBuilder.loadTexts:
    assocEntryOffset.setUnits("milliseconds")
_AssocEntryJitter_Type = DisplayString
_AssocEntryJitter_Object = MibTableColumn
assocEntryJitter = _AssocEntryJitter_Object(
    (1, 3, 6, 1, 4, 1, 18837, 3, 3, 3, 2, 1, 14),
    _AssocEntryJitter_Type()
)
assocEntryJitter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    assocEntryJitter.setStatus("current")
if mibBuilder.loadTexts:
    assocEntryJitter.setUnits("milliseconds")
_NtpAutoKeyObjs_ObjectIdentity = ObjectIdentity
ntpAutoKeyObjs = _NtpAutoKeyObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18837, 3, 3, 4)
)
_NtpAutoKeyTrustedRoot_Type = Unsigned32
_NtpAutoKeyTrustedRoot_Object = MibScalar
ntpAutoKeyTrustedRoot = _NtpAutoKeyTrustedRoot_Object(
    (1, 3, 6, 1, 4, 1, 18837, 3, 3, 4, 1),
    _NtpAutoKeyTrustedRoot_Type()
)
ntpAutoKeyTrustedRoot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntpAutoKeyTrustedRoot.setStatus("current")
_NtpAutoKeyNotBefore_Type = DisplayString
_NtpAutoKeyNotBefore_Object = MibScalar
ntpAutoKeyNotBefore = _NtpAutoKeyNotBefore_Object(
    (1, 3, 6, 1, 4, 1, 18837, 3, 3, 4, 2),
    _NtpAutoKeyNotBefore_Type()
)
ntpAutoKeyNotBefore.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntpAutoKeyNotBefore.setStatus("current")
_NtpAutoKeyNotAfter_Type = DisplayString
_NtpAutoKeyNotAfter_Object = MibScalar
ntpAutoKeyNotAfter = _NtpAutoKeyNotAfter_Object(
    (1, 3, 6, 1, 4, 1, 18837, 3, 3, 4, 3),
    _NtpAutoKeyNotAfter_Type()
)
ntpAutoKeyNotAfter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntpAutoKeyNotAfter.setStatus("current")
_NtpConformance_ObjectIdentity = ObjectIdentity
ntpConformance = _NtpConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18837, 3, 3, 90)
)
_NtpCompliances_ObjectIdentity = ObjectIdentity
ntpCompliances = _NtpCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18837, 3, 3, 90, 1)
)
_NtpGroups_ObjectIdentity = ObjectIdentity
ntpGroups = _NtpGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18837, 3, 3, 90, 2)
)

# Managed Objects groups

ntpObjectsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 18837, 3, 3, 90, 2, 1)
)
ntpObjectsGroup.setObjects(
      *(("SPECTRACOM-NTP-V4-MIB", "ntpGenAppName"),
        ("SPECTRACOM-NTP-V4-MIB", "ntpGenAppRevision"),
        ("SPECTRACOM-NTP-V4-MIB", "ntpGenAppVendor"),
        ("SPECTRACOM-NTP-V4-MIB", "ntpGenSystemType"),
        ("SPECTRACOM-NTP-V4-MIB", "ntpSysStaCurrentMode"),
        ("SPECTRACOM-NTP-V4-MIB", "ntpSysStaStratum"),
        ("SPECTRACOM-NTP-V4-MIB", "ntpSysStaCurrentPeerAssc"),
        ("SPECTRACOM-NTP-V4-MIB", "ntpSysStaCurrentPeerName"),
        ("SPECTRACOM-NTP-V4-MIB", "ntpSysStaPeerDelay"),
        ("SPECTRACOM-NTP-V4-MIB", "ntpSysStaPeerOffset"),
        ("SPECTRACOM-NTP-V4-MIB", "ntpSysStaPeerJitter"),
        ("SPECTRACOM-NTP-V4-MIB", "ntpAssocCount"),
        ("SPECTRACOM-NTP-V4-MIB", "assocEntryIdentity"),
        ("SPECTRACOM-NTP-V4-MIB", "assocEntrySyncStatus"),
        ("SPECTRACOM-NTP-V4-MIB", "assocEntryRefId"),
        ("SPECTRACOM-NTP-V4-MIB", "assocEntryStratum"),
        ("SPECTRACOM-NTP-V4-MIB", "assocEntryMode"),
        ("SPECTRACOM-NTP-V4-MIB", "assocEntryType"),
        ("SPECTRACOM-NTP-V4-MIB", "assocEntryAuthStatus"),
        ("SPECTRACOM-NTP-V4-MIB", "assocEntryLastPoll"),
        ("SPECTRACOM-NTP-V4-MIB", "assocEntryPollInterval"),
        ("SPECTRACOM-NTP-V4-MIB", "assocEntryReach"),
        ("SPECTRACOM-NTP-V4-MIB", "assocEntryDelay"),
        ("SPECTRACOM-NTP-V4-MIB", "assocEntryOffset"),
        ("SPECTRACOM-NTP-V4-MIB", "assocEntryJitter"),
        ("SPECTRACOM-NTP-V4-MIB", "ntpAutoKeyTrustedRoot"),
        ("SPECTRACOM-NTP-V4-MIB", "ntpAutoKeyNotBefore"),
        ("SPECTRACOM-NTP-V4-MIB", "ntpAutoKeyNotAfter"))
)
if mibBuilder.loadTexts:
    ntpObjectsGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

ntpCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 18837, 3, 3, 90, 1, 1)
)
ntpCompliance.setObjects(
    ("SPECTRACOM-NTP-V4-MIB", "ntpObjectsGroup")
)
if mibBuilder.loadTexts:
    ntpCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SPECTRACOM-NTP-V4-MIB",
    **{"spectracomNtpV4MibModule": spectracomNtpV4MibModule,
       "ntpSnmpObjs": ntpSnmpObjs,
       "ntpGeneralObjs": ntpGeneralObjs,
       "ntpGenAppName": ntpGenAppName,
       "ntpGenAppRevision": ntpGenAppRevision,
       "ntpGenAppVendor": ntpGenAppVendor,
       "ntpGenSystemType": ntpGenSystemType,
       "ntpSystemStatusObjs": ntpSystemStatusObjs,
       "ntpSysStaCurrentMode": ntpSysStaCurrentMode,
       "ntpSysStaStratum": ntpSysStaStratum,
       "ntpSysStaCurrentPeerAssc": ntpSysStaCurrentPeerAssc,
       "ntpSysStaCurrentPeerName": ntpSysStaCurrentPeerName,
       "ntpSysStaPeerDelay": ntpSysStaPeerDelay,
       "ntpSysStaPeerOffset": ntpSysStaPeerOffset,
       "ntpSysStaPeerJitter": ntpSysStaPeerJitter,
       "ntpAssociationsObjs": ntpAssociationsObjs,
       "ntpAssocCount": ntpAssocCount,
       "ntpAssocTable": ntpAssocTable,
       "ntpAssocEntry": ntpAssocEntry,
       "assocEntryIndex": assocEntryIndex,
       "assocEntryIdentity": assocEntryIdentity,
       "assocEntrySyncStatus": assocEntrySyncStatus,
       "assocEntryRefId": assocEntryRefId,
       "assocEntryStratum": assocEntryStratum,
       "assocEntryMode": assocEntryMode,
       "assocEntryType": assocEntryType,
       "assocEntryAuthStatus": assocEntryAuthStatus,
       "assocEntryLastPoll": assocEntryLastPoll,
       "assocEntryPollInterval": assocEntryPollInterval,
       "assocEntryReach": assocEntryReach,
       "assocEntryDelay": assocEntryDelay,
       "assocEntryOffset": assocEntryOffset,
       "assocEntryJitter": assocEntryJitter,
       "ntpAutoKeyObjs": ntpAutoKeyObjs,
       "ntpAutoKeyTrustedRoot": ntpAutoKeyTrustedRoot,
       "ntpAutoKeyNotBefore": ntpAutoKeyNotBefore,
       "ntpAutoKeyNotAfter": ntpAutoKeyNotAfter,
       "ntpConformance": ntpConformance,
       "ntpCompliances": ntpCompliances,
       "ntpCompliance": ntpCompliance,
       "ntpGroups": ntpGroups,
       "ntpObjectsGroup": ntpObjectsGroup}
)
