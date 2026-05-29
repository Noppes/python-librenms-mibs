# SNMP MIB module (SONICWALL-FIREWALL-IP-STATISTICS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\sonicwall\SONICWALL-FIREWALL-IP-STATISTICS-MIB

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention",
    "TruthValue")

(sonicwallFw,) = mibBuilder.importSymbols(
    "SONICWALL-SMI",
    "sonicwallFw")


# MODULE-IDENTITY

sonicwallFwStatsModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 8741, 1, 3)
)
if mibBuilder.loadTexts:
    sonicwallFwStatsModule.setRevisions(
        ("2019-03-01 00:00",
         "2017-01-06 00:00",
         "2016-07-01 00:00",
         "2015-01-08 00:00",
         "2014-02-28 00:00",
         "2014-02-18 00:00",
         "2005-11-09 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class SyslogFacility(TextualConvention, Integer32):
    status = "current"
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
              23)
        )
    )
    namedValues = NamedValues(
        *(("kern", 0),
          ("user", 1),
          ("mail", 2),
          ("daemon", 3),
          ("auth", 4),
          ("syslog", 5),
          ("lpr", 6),
          ("news", 7),
          ("uucp", 8),
          ("cron", 9),
          ("authpriv", 10),
          ("ftp", 11),
          ("ntp", 12),
          ("audit", 13),
          ("alert", 14),
          ("cron2", 15),
          ("local0", 16),
          ("local1", 17),
          ("local2", 18),
          ("local3", 19),
          ("local4", 20),
          ("local5", 21),
          ("local6", 22),
          ("local7", 23))
    )



class SwSpRadioType(TextualConvention, Integer32):
    status = "current"
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("other", 0),
          ("dot11n-only-24", 1),
          ("dot11n-mixed-24", 2),
          ("dot11g-only-24", 3),
          ("dot11n-only-50", 4),
          ("dot11n-mixed-50", 5),
          ("dot11a-only-50", 6),
          ("dot11ac-mixed-50", 7),
          ("dot11ac-only-50", 8))
    )



class SwSpChannelWidthType(TextualConvention, Integer32):
    status = "current"
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
        *(("auto", 0),
          ("width20MHz", 1),
          ("width40MHz", 2),
          ("width80MHz", 3))
    )



class SwSpWorkState(TextualConvention, Integer32):
    status = "current"
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
              23)
        )
    )
    namedValues = NamedValues(
        *(("safemode", 0),
          ("unprovisioned", 1),
          ("provisioning", 2),
          ("operational", 3),
          ("unresponse", 4),
          ("updatingfirmware", 5),
          ("initializing", 6),
          ("overlimit", 7),
          ("rebooting", 8),
          ("failedprovision", 9),
          ("failedfirmware", 10),
          ("scanning", 11),
          ("manufacturing", 12),
          ("disable", 13),
          ("downloadingfirmware", 14),
          ("nofirmware", 15),
          ("failedscan", 16),
          ("widp", 17),
          ("widpto", 18),
          ("writingfirmware", 19),
          ("failedgetcrashlog", 20),
          ("autoshutoff", 21),
          ("gettingfirmware", 22),
          ("unregistered", 23))
    )



class SwStationStatus(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("authenticated", 1),
          ("associated", 2),
          ("joined", 3),
          ("connected", 4),
          ("up", 5),
          ("down", 6))
    )



class SwSpRadioChannelNumber(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 200),
    )



class SwSpRadioTxPower(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("fullpower", 0),
          ("half", 1),
          ("quarter", 2),
          ("eighth", 3),
          ("minimum", 4))
    )



class SwZoneSecurityType(TextualConvention, Integer32):
    status = "current"
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
              9)
        )
    )
    namedValues = NamedValues(
        *(("untrusted1", 0),
          ("trusted", 1),
          ("public", 2),
          ("other1", 3),
          ("wireless", 4),
          ("encrypted", 5),
          ("untrusted2", 6),
          ("other2", 7),
          ("sslvpn", 8),
          ("management", 9))
    )



class SwBoolState(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )



class SwWlanAuthenticationType(TextualConvention, Integer32):
    status = "current"
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
              9)
        )
    )
    namedValues = NamedValues(
        *(("other", 0),
          ("wep-both", 1),
          ("wep-open", 2),
          ("wep-shared", 3),
          ("wpa-psk", 4),
          ("wpa-eap", 5),
          ("wpa2-psk", 6),
          ("wpa2-eap", 7),
          ("wpa2-auto-psk", 8),
          ("wpa2-auto-eap", 9))
    )



class SwWlanCipherType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("open", 1),
          ("wep", 2),
          ("tkip", 3),
          ("aes", 4),
          ("auto", 5))
    )



# MIB Managed Objects in the order of their OIDs

_SonicwallFwStats_ObjectIdentity = ObjectIdentity
sonicwallFwStats = _SonicwallFwStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8741, 1, 3, 1)
)


class _SonicMaxConnCacheEntries_Type(Integer32):
    """Custom type sonicMaxConnCacheEntries based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_SonicMaxConnCacheEntries_Type.__name__ = "Integer32"
_SonicMaxConnCacheEntries_Object = MibScalar
sonicMaxConnCacheEntries = _SonicMaxConnCacheEntries_Object(
    (1, 3, 6, 1, 4, 1, 8741, 1, 3, 1, 1),
    _SonicMaxConnCacheEntries_Type()
)
sonicMaxConnCacheEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonicMaxConnCacheEntries.setStatus("current")
_SonicCurrentConnCacheEntries_Type = Gauge32
_SonicCurrentConnCacheEntries_Object = MibScalar
sonicCurrentConnCacheEntries = _SonicCurrentConnCacheEntries_Object(
    (1, 3, 6, 1, 4, 1, 8741, 1, 3, 1, 2),
    _SonicCurrentConnCacheEntries_Type()
)
sonicCurrentConnCacheEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonicCurrentConnCacheEntries.setStatus("current")
_SonicCurrentCPUUtil_Type = Gauge32
_SonicCurrentCPUUtil_Object = MibScalar
sonicCurrentCPUUtil = _SonicCurrentCPUUtil_Object(
    (1, 3, 6, 1, 4, 1, 8741, 1, 3, 1, 3),
    _SonicCurrentCPUUtil_Type()
)
sonicCurrentCPUUtil.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonicCurrentCPUUtil.setStatus("current")
_SonicCurrentRAMUtil_Type = Gauge32
_SonicCurrentRAMUtil_Object = MibScalar
sonicCurrentRAMUtil = _SonicCurrentRAMUtil_Object(
    (1, 3, 6, 1, 4, 1, 8741, 1, 3, 1, 4),
    _SonicCurrentRAMUtil_Type()
)
sonicCurrentRAMUtil.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonicCurrentRAMUtil.setStatus("current")
_SonicNatTranslationCount_Type = Gauge32
_SonicNatTranslationCount_Object = MibScalar
sonicNatTranslationCount = _SonicNatTranslationCount_Object(
    (1, 3, 6, 1, 4, 1, 8741, 1, 3, 1, 5),
    _SonicNatTranslationCount_Type()
)
sonicNatTranslationCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonicNatTranslationCount.setStatus("current")
_SonicCurrentManagementCPUUtil_Type = Gauge32
_SonicCurrentManagementCPUUtil_Object = MibScalar
sonicCurrentManagementCPUUtil = _SonicCurrentManagementCPUUtil_Object(
    (1, 3, 6, 1, 4, 1, 8741, 1, 3, 1, 6),
    _SonicCurrentManagementCPUUtil_Type()
)
sonicCurrentManagementCPUUtil.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonicCurrentManagementCPUUtil.setStatus("current")
_SonicCurrentFwdAndInspectCPUUtil_Type = Gauge32
_SonicCurrentFwdAndInspectCPUUtil_Object = MibScalar
sonicCurrentFwdAndInspectCPUUtil = _SonicCurrentFwdAndInspectCPUUtil_Object(
    (1, 3, 6, 1, 4, 1, 8741, 1, 3, 1, 7),
    _SonicCurrentFwdAndInspectCPUUtil_Type()
)
sonicCurrentFwdAndInspectCPUUtil.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonicCurrentFwdAndInspectCPUUtil.setStatus("current")
_SonicIfStatTable_Object = MibTable
sonicIfStatTable = _SonicIfStatTable_Object(
    (1, 3, 6, 1, 4, 1, 8741, 1, 3, 1, 8)
)
if mibBuilder.loadTexts:
    sonicIfStatTable.setStatus("current")
_SonicIfStatEntry_Object = MibTableRow
sonicIfStatEntry = _SonicIfStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 8741, 1, 3, 1, 8, 1)
)
sonicIfStatEntry.setIndexNames(
    (0, "SONICWALL-FIREWALL-IP-STATISTICS-MIB", "sonicIfIndex"),
)
if mibBuilder.loadTexts:
    sonicIfStatEntry.setStatus("current")
_SonicIfIndex_Type = Integer32
_SonicIfIndex_Object = MibTableColumn
sonicIfIndex = _SonicIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 8741, 1, 3, 1, 8, 1, 1),
    _SonicIfIndex_Type()
)
sonicIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonicIfIndex.setStatus("current")
_SonicIfUsage_Type = Integer32
_SonicIfUsage_Object = MibTableColumn
sonicIfUsage = _SonicIfUsage_Object(
    (1, 3, 6, 1, 4, 1, 8741, 1, 3, 1, 8, 1, 2),
    _SonicIfUsage_Type()
)
sonicIfUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonicIfUsage.setStatus("current")
_SonicIfThroughput_Type = Integer32
_SonicIfThroughput_Object = MibTableColumn
sonicIfThroughput = _SonicIfThroughput_Object(
    (1, 3, 6, 1, 4, 1, 8741, 1, 3, 1, 8, 1, 3),
    _SonicIfThroughput_Type()
)
sonicIfThroughput.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonicIfThroughput.setStatus("current")
_SonicCFS_Type = SwBoolState
_SonicCFS_Object = MibScalar
sonicCFS = _SonicCFS_Object(
    (1, 3, 6, 1, 4, 1, 8741, 1, 3, 1, 9),
    _SonicCFS_Type()
)
sonicCFS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonicCFS.setStatus("current")
_SonicwallFwVPNStats_ObjectIdentity = ObjectIdentity
sonicwallFwVPNStats = _SonicwallFwVPNStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8741, 1, 3, 2)
)
_SonicwallFwVpnIPSecStats_ObjectIdentity = ObjectIdentity
sonicwallFwVpnIPSecStats = _SonicwallFwVpnIPSecStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8741, 1, 3, 2, 1)
)
_SonicSAStatTable_Object = MibTable
sonicSAStatTable = _SonicSAStatTable_Object(
    (1, 3, 6, 1, 4, 1, 8741, 1, 3, 2, 1, 1)
)
if mibBuilder.loadTexts:
    sonicSAStatTable.setStatus("current")
_SonicSAStatEntry_Object = MibTableRow
sonicSAStatEntry = _SonicSAStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 8741, 1, 3, 2, 1, 1, 1)
)
sonicSAStatEntry.setIndexNames(
    (0, "SONICWALL-FIREWALL-IP-STATISTICS-MIB", "sonicIpsecSaIndex"),
)
if mibBuilder.loadTexts:
    sonicSAStatEntry.setStatus("current")
_SonicIpsecSaIndex_Type = Counter32
_SonicIpsecSaIndex_Object = MibTableColumn
sonicIpsecSaIndex = _SonicIpsecSaIndex_Object(
    (1, 3, 6, 1, 4, 1, 8741, 1, 3, 2, 1, 1, 1, 1),
    _SonicIpsecSaIndex_Type()
)
sonicIpsecSaIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonicIpsecSaIndex.setStatus("current")
_SonicSAStatPeerGateway_Type = IpAddress
_SonicSAStatPeerGateway_Object = MibTableColumn
sonicSAStatPeerGateway = _SonicSAStatPeerGateway_Object(
    (1, 3, 6, 1, 4, 1, 8741, 1, 3, 2, 1, 1, 1, 2),
    _SonicSAStatPeerGateway_Type()
)
sonicSAStatPeerGateway.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonicSAStatPeerGateway.setStatus("current")
_SonicSAStatSrcAddrBegin_Type = IpAddress
_SonicSAStatSrcAddrBegin_Object = MibTableColumn
sonicSAStatSrcAddrBegin = _SonicSAStatSrcAddrBegin_Object(
    (1, 3, 6, 1, 4, 1, 8741, 1, 3, 2, 1, 1, 1, 3),
    _SonicSAStatSrcAddrBegin_Type()
)
sonicSAStatSrcAddrBegin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonicSAStatSrcAddrBegin.setStatus("current")
_SonicSAStatSrcAddrEnd_Type = IpAddress
_SonicSAStatSrcAddrEnd_Object = MibTableColumn
sonicSAStatSrcAddrEnd = _SonicSAStatSrcAddrEnd_Object(
    (1, 3, 6, 1, 4, 1, 8741, 1, 3, 2, 1, 1, 1, 4),
    _SonicSAStatSrcAddrEnd_Type()
)
sonicSAStatSrcAddrEnd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonicSAStatSrcAddrEnd.setStatus("current")
_SonicSAStatDstAddrBegin_Type = IpAddress
_SonicSAStatDstAddrBegin_Object = MibTableColumn
sonicSAStatDstAddrBegin = _SonicSAStatDstAddrBegin_Object(
    (1, 3, 6, 1, 4, 1, 8741, 1, 3, 2, 1, 1, 1, 5),
    _SonicSAStatDstAddrBegin_Type()
)
sonicSAStatDstAddrBegin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonicSAStatDstAddrBegin.setStatus("current")
_SonicSAStatDstAddrEnd_Type = IpAddress
_SonicSAStatDstAddrEnd_Object = MibTableColumn
sonicSAStatDstAddrEnd = _SonicSAStatDstAddrEnd_Object(
    (1, 3, 6, 1, 4, 1, 8741, 1, 3, 2, 1, 1, 1, 6),
    _SonicSAStatDstAddrEnd_Type()
)
sonicSAStatDstAddrEnd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonicSAStatDstAddrEnd.setStatus("current")
_SonicSAStatCreateTime_Type = DisplayString
_SonicSAStatCreateTime_Object = MibTableColumn
sonicSAStatCreateTime = _SonicSAStatCreateTime_Object(
    (1, 3, 6, 1, 4, 1, 8741, 1, 3, 2, 1, 1, 1, 7),
    _SonicSAStatCreateTime_Type()
)
sonicSAStatCreateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonicSAStatCreateTime.setStatus("current")
_SonicSAStatEncryptPktCount_Type = Counter32
_SonicSAStatEncryptPktCount_Object = MibTableColumn
sonicSAStatEncryptPktCount = _SonicSAStatEncryptPktCount_Object(
    (1, 3, 6, 1, 4, 1, 8741, 1, 3, 2, 1, 1, 1, 8),
    _SonicSAStatEncryptPktCount_Type()
)
sonicSAStatEncryptPktCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonicSAStatEncryptPktCount.setStatus("current")
_SonicSAStatEncryptByteCount_Type = Counter32
_SonicSAStatEncryptByteCount_Object = MibTableColumn
sonicSAStatEncryptByteCount = _SonicSAStatEncryptByteCount_Object(
    (1, 3, 6, 1, 4, 1, 8741, 1, 3, 2, 1, 1, 1, 9),
    _SonicSAStatEncryptByteCount_Type()
)
sonicSAStatEncryptByteCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonicSAStatEncryptByteCount.setStatus("current")
_SonicSAStatDecryptPktCount_Type = Counter32
_SonicSAStatDecryptPktCount_Object = MibTableColumn
sonicSAStatDecryptPktCount = _SonicSAStatDecryptPktCount_Object(
    (1, 3, 6, 1, 4, 1, 8741, 1, 3, 2, 1, 1, 1, 10),
    _SonicSAStatDecryptPktCount_Type()
)
sonicSAStatDecryptPktCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonicSAStatDecryptPktCount.setStatus("current")
_SonicSAStatDecryptByteCount_Type = Counter32
_SonicSAStatDecryptByteCount_Object = MibTableColumn
sonicSAStatDecryptByteCount = _SonicSAStatDecryptByteCount_Object(
    (1, 3, 6, 1, 4, 1, 8741, 1, 3, 2, 1, 1, 1, 11),
    _SonicSAStatDecryptByteCount_Type()
)
sonicSAStatDecryptByteCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonicSAStatDecryptByteCount.setStatus("current")
_SonicSAStatInFragPktCount_Type = Counter32
_SonicSAStatInFragPktCount_Object = MibTableColumn
sonicSAStatInFragPktCount = _SonicSAStatInFragPktCount_Object(
    (1, 3, 6, 1, 4, 1, 8741, 1, 3, 2, 1, 1, 1, 12),
    _SonicSAStatInFragPktCount_Type()
)
sonicSAStatInFragPktCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonicSAStatInFragPktCount.setStatus("current")
_SonicSAStatOutFragPktCount_Type = Counter32
_SonicSAStatOutFragPktCount_Object = MibTableColumn
sonicSAStatOutFragPktCount = _SonicSAStatOutFragPktCount_Object(
    (1, 3, 6, 1, 4, 1, 8741, 1, 3, 2, 1, 1, 1, 13),
    _SonicSAStatOutFragPktCount_Type()
)
sonicSAStatOutFragPktCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonicSAStatOutFragPktCount.setStatus("current")
_SonicSAStatUserName_Type = DisplayString
_SonicSAStatUserName_Object = MibTableColumn
sonicSAStatUserName = _SonicSAStatUserName_Object(
    (1, 3, 6, 1, 4, 1, 8741, 1, 3, 2, 1, 1, 1, 14),
    _SonicSAStatUserName_Type()
)
sonicSAStatUserName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonicSAStatUserName.setStatus("current")
_SonicwallFwHWStats_ObjectIdentity = ObjectIdentity
sonicwallFwHWStats = _SonicwallFwHWStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8741, 1, 3, 3)
)
_SonicwallFwHWSensorStats_ObjectIdentity = ObjectIdentity
sonicwallFwHWSensorStats = _SonicwallFwHWSensorStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8741, 1, 3, 3, 3)
)
_SonicwallSensorsTable_Object = MibTable
sonicwallSensorsTable = _SonicwallSensorsTable_Object(
    (1, 3, 6, 1, 4, 1, 8741, 1, 3, 3, 3, 1)
)
if mibBuilder.loadTexts:
    sonicwallSensorsTable.setStatus("current")
_SonicwallSensorsEntry_Object = MibTableRow
sonicwallSensorsEntry = _SonicwallSensorsEntry_Object(
    (1, 3, 6, 1, 4, 1, 8741, 1, 3, 3, 3, 1, 1)
)
sonicwallSensorsEntry.setIndexNames(
    (0, "SONICWALL-FIREWALL-IP-STATISTICS-MIB", "sonicwallSensorsIndex"),
)
if mibBuilder.loadTexts:
    sonicwallSensorsEntry.setStatus("current")


class _SonicwallSensorsIndex_Type(Integer32):
    """Custom type sonicwallSensorsIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SonicwallSensorsIndex_Type.__name__ = "Integer32"
_SonicwallSensorsIndex_Object = MibTableColumn
sonicwallSensorsIndex = _SonicwallSensorsIndex_Object(
    (1, 3, 6, 1, 4, 1, 8741, 1, 3, 3, 3, 1, 1, 1),
    _SonicwallSensorsIndex_Type()
)
sonicwallSensorsIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonicwallSensorsIndex.setStatus("current")


class _SonicwallSensorsId_Type(Integer32):
    """Custom type sonicwallSensorsId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SonicwallSensorsId_Type.__name__ = "Integer32"
_SonicwallSensorsId_Object = MibTableColumn
sonicwallSensorsId = _SonicwallSensorsId_Object(
    (1, 3, 6, 1, 4, 1, 8741, 1, 3, 3, 3, 1, 1, 2),
    _SonicwallSensorsId_Type()
)
sonicwallSensorsId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonicwallSensorsId.setStatus("current")


class _SonicwallSensorsDevice_Type(DisplayString):
    """Custom type sonicwallSensorsDevice based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SonicwallSensorsDevice_Type.__name__ = "DisplayString"
_SonicwallSensorsDevice_Object = MibTableColumn
sonicwallSensorsDevice = _SonicwallSensorsDevice_Object(
    (1, 3, 6, 1, 4, 1, 8741, 1, 3, 3, 3, 1, 1, 3),
    _SonicwallSensorsDevice_Type()
)
sonicwallSensorsDevice.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonicwallSensorsDevice.setStatus("current")
_SonicwallSensorsValue_Type = Integer32
_SonicwallSensorsValue_Object = MibTableColumn
sonicwallSensorsValue = _SonicwallSensorsValue_Object(
    (1, 3, 6, 1, 4, 1, 8741, 1, 3, 3, 3, 1, 1, 4),
    _SonicwallSensorsValue_Type()
)
sonicwallSensorsValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonicwallSensorsValue.setStatus("current")


class _SonicwallSensorsUnit_Type(DisplayString):
    """Custom type sonicwallSensorsUnit based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SonicwallSensorsUnit_Type.__name__ = "DisplayString"
_SonicwallSensorsUnit_Object = MibTableColumn
sonicwallSensorsUnit = _SonicwallSensorsUnit_Object(
    (1, 3, 6, 1, 4, 1, 8741, 1, 3, 3, 3, 1, 1, 5),
    _SonicwallSensorsUnit_Type()
)
sonicwallSensorsUnit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonicwallSensorsUnit.setStatus("current")
_SonicwallFwSyslogStats_ObjectIdentity = ObjectIdentity
sonicwallFwSyslogStats = _SonicwallFwSyslogStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8741, 1, 3, 4)
)
_SonicwallFwSyslogSetting_ObjectIdentity = ObjectIdentity
sonicwallFwSyslogSetting = _SonicwallFwSyslogSetting_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8741, 1, 3, 4, 1)
)
_SonicSyslogFacility_Type = SyslogFacility
_SonicSyslogFacility_Object = MibScalar
sonicSyslogFacility = _SonicSyslogFacility_Object(
    (1, 3, 6, 1, 4, 1, 8741, 1, 3, 4, 1, 1),
    _SonicSyslogFacility_Type()
)
sonicSyslogFacility.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonicSyslogFacility.setStatus("current")
_SonicSyslogOverrideSetting_Type = TruthValue
_SonicSyslogOverrideSetting_Object = MibScalar
sonicSyslogOverrideSetting = _SonicSyslogOverrideSetting_Object(
    (1, 3, 6, 1, 4, 1, 8741, 1, 3, 4, 1, 2),
    _SonicSyslogOverrideSetting_Type()
)
sonicSyslogOverrideSetting.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonicSyslogOverrideSetting.setStatus("current")


class _SonicSyslogFormat_Type(Integer32):
    """Custom type sonicSyslogFormat based on Integer32"""
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
        *(("default", 0),
          ("webTrends", 1),
          ("enhSyslog", 2),
          ("arcSight", 3))
    )


_SonicSyslogFormat_Type.__name__ = "Integer32"
_SonicSyslogFormat_Object = MibScalar
sonicSyslogFormat = _SonicSyslogFormat_Object(
    (1, 3, 6, 1, 4, 1, 8741, 1, 3, 4, 1, 3),
    _SonicSyslogFormat_Type()
)
sonicSyslogFormat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonicSyslogFormat.setStatus("current")


class _SonicSyslogID_Type(DisplayString):
    """Custom type sonicSyslogID based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_SonicSyslogID_Type.__name__ = "DisplayString"
_SonicSyslogID_Object = MibScalar
sonicSyslogID = _SonicSyslogID_Object(
    (1, 3, 6, 1, 4, 1, 8741, 1, 3, 4, 1, 4),
    _SonicSyslogID_Type()
)
sonicSyslogID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonicSyslogID.setStatus("current")
_SonicSyslogEventRateLimitEnable_Type = TruthValue
_SonicSyslogEventRateLimitEnable_Object = MibScalar
sonicSyslogEventRateLimitEnable = _SonicSyslogEventRateLimitEnable_Object(
    (1, 3, 6, 1, 4, 1, 8741, 1, 3, 4, 1, 5),
    _SonicSyslogEventRateLimitEnable_Type()
)
sonicSyslogEventRateLimitEnable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonicSyslogEventRateLimitEnable.setStatus("current")
_SonicSyslogEventRateLimit_Type = Gauge32
_SonicSyslogEventRateLimit_Object = MibScalar
sonicSyslogEventRateLimit = _SonicSyslogEventRateLimit_Object(
    (1, 3, 6, 1, 4, 1, 8741, 1, 3, 4, 1, 6),
    _SonicSyslogEventRateLimit_Type()
)
sonicSyslogEventRateLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonicSyslogEventRateLimit.setStatus("current")
_SonicSyslogDataRateLimitEnable_Type = TruthValue
_SonicSyslogDataRateLimitEnable_Object = MibScalar
sonicSyslogDataRateLimitEnable = _SonicSyslogDataRateLimitEnable_Object(
    (1, 3, 6, 1, 4, 1, 8741, 1, 3, 4, 1, 7),
    _SonicSyslogDataRateLimitEnable_Type()
)
sonicSyslogDataRateLimitEnable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonicSyslogDataRateLimitEnable.setStatus("current")
_SonicSyslogDataRateLimit_Type = Gauge32
_SonicSyslogDataRateLimit_Object = MibScalar
sonicSyslogDataRateLimit = _SonicSyslogDataRateLimit_Object(
    (1, 3, 6, 1, 4, 1, 8741, 1, 3, 4, 1, 8),
    _SonicSyslogDataRateLimit_Type()
)
sonicSyslogDataRateLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonicSyslogDataRateLimit.setStatus("current")
_SonicSyslogNDPPEnable_Type = TruthValue
_SonicSyslogNDPPEnable_Object = MibScalar
sonicSyslogNDPPEnable = _SonicSyslogNDPPEnable_Object(
    (1, 3, 6, 1, 4, 1, 8741, 1, 3, 4, 1, 9),
    _SonicSyslogNDPPEnable_Type()
)
sonicSyslogNDPPEnable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonicSyslogNDPPEnable.setStatus("current")
_SonicwallFwSyslogServer_ObjectIdentity = ObjectIdentity
sonicwallFwSyslogServer = _SonicwallFwSyslogServer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8741, 1, 3, 4, 2)
)
_SonicSyslogMaxServers_Type = Unsigned32
_SonicSyslogMaxServers_Object = MibScalar
sonicSyslogMaxServers = _SonicSyslogMaxServers_Object(
    (1, 3, 6, 1, 4, 1, 8741, 1, 3, 4, 2, 1),
    _SonicSyslogMaxServers_Type()
)
sonicSyslogMaxServers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonicSyslogMaxServers.setStatus("current")
_SonicSyslogServerTable_Object = MibTable
sonicSyslogServerTable = _SonicSyslogServerTable_Object(
    (1, 3, 6, 1, 4, 1, 8741, 1, 3, 4, 2, 2)
)
if mibBuilder.loadTexts:
    sonicSyslogServerTable.setStatus("current")
_SonicSyslogServerEntry_Object = MibTableRow
sonicSyslogServerEntry = _SonicSyslogServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 8741, 1, 3, 4, 2, 2, 1)
)
sonicSyslogServerEntry.setIndexNames(
    (0, "SONICWALL-FIREWALL-IP-STATISTICS-MIB", "sonicSyslogServerIndex"),
)
if mibBuilder.loadTexts:
    sonicSyslogServerEntry.setStatus("current")
_SonicSyslogServerIndex_Type = Integer32
_SonicSyslogServerIndex_Object = MibTableColumn
sonicSyslogServerIndex = _SonicSyslogServerIndex_Object(
    (1, 3, 6, 1, 4, 1, 8741, 1, 3, 4, 2, 2, 1, 1),
    _SonicSyslogServerIndex_Type()
)
sonicSyslogServerIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonicSyslogServerIndex.setStatus("current")
_SonicSyslogServerAddr_Type = IpAddress
_SonicSyslogServerAddr_Object = MibTableColumn
sonicSyslogServerAddr = _SonicSyslogServerAddr_Object(
    (1, 3, 6, 1, 4, 1, 8741, 1, 3, 4, 2, 2, 1, 2),
    _SonicSyslogServerAddr_Type()
)
sonicSyslogServerAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonicSyslogServerAddr.setStatus("current")


class _SonicSyslogServerPort_Type(Integer32):
    """Custom type sonicSyslogServerPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SonicSyslogServerPort_Type.__name__ = "Integer32"
_SonicSyslogServerPort_Object = MibTableColumn
sonicSyslogServerPort = _SonicSyslogServerPort_Object(
    (1, 3, 6, 1, 4, 1, 8741, 1, 3, 4, 2, 2, 1, 3),
    _SonicSyslogServerPort_Type()
)
sonicSyslogServerPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonicSyslogServerPort.setStatus("current")
_SonicwallFwSyslogStatistic_ObjectIdentity = ObjectIdentity
sonicwallFwSyslogStatistic = _SonicwallFwSyslogStatistic_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8741, 1, 3, 4, 3)
)
_SonicSyslogMessage_Type = Counter32
_SonicSyslogMessage_Object = MibScalar
sonicSyslogMessage = _SonicSyslogMessage_Object(
    (1, 3, 6, 1, 4, 1, 8741, 1, 3, 4, 3, 1),
    _SonicSyslogMessage_Type()
)
sonicSyslogMessage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonicSyslogMessage.setStatus("current")
_SonicSyslogStreamData_Type = Counter32
_SonicSyslogStreamData_Object = MibScalar
sonicSyslogStreamData = _SonicSyslogStreamData_Object(
    (1, 3, 6, 1, 4, 1, 8741, 1, 3, 4, 3, 2),
    _SonicSyslogStreamData_Type()
)
sonicSyslogStreamData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonicSyslogStreamData.setStatus("current")
_SonicwallFwDpiSslStats_ObjectIdentity = ObjectIdentity
sonicwallFwDpiSslStats = _SonicwallFwDpiSslStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8741, 1, 3, 5)
)
_SonicDpiSslConnCountCur_Type = Gauge32
_SonicDpiSslConnCountCur_Object = MibScalar
sonicDpiSslConnCountCur = _SonicDpiSslConnCountCur_Object(
    (1, 3, 6, 1, 4, 1, 8741, 1, 3, 5, 1),
    _SonicDpiSslConnCountCur_Type()
)
sonicDpiSslConnCountCur.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonicDpiSslConnCountCur.setStatus("current")
_SonicDpiSslConnCountHighWater_Type = Gauge32
_SonicDpiSslConnCountHighWater_Object = MibScalar
sonicDpiSslConnCountHighWater = _SonicDpiSslConnCountHighWater_Object(
    (1, 3, 6, 1, 4, 1, 8741, 1, 3, 5, 2),
    _SonicDpiSslConnCountHighWater_Type()
)
sonicDpiSslConnCountHighWater.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonicDpiSslConnCountHighWater.setStatus("current")
_SonicDpiSslConnCountMax_Type = Gauge32
_SonicDpiSslConnCountMax_Object = MibScalar
sonicDpiSslConnCountMax = _SonicDpiSslConnCountMax_Object(
    (1, 3, 6, 1, 4, 1, 8741, 1, 3, 5, 3),
    _SonicDpiSslConnCountMax_Type()
)
sonicDpiSslConnCountMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonicDpiSslConnCountMax.setStatus("current")
_SonicwallFwWirelessStats_ObjectIdentity = ObjectIdentity
sonicwallFwWirelessStats = _SonicwallFwWirelessStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8741, 1, 3, 6)
)
_SonicWirelessSpInfo_ObjectIdentity = ObjectIdentity
sonicWirelessSpInfo = _SonicWirelessSpInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8741, 1, 3, 6, 1)
)


class _SonicWirelessSpVersion_Type(DisplayString):
    """Custom type sonicWirelessSpVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_SonicWirelessSpVersion_Type.__name__ = "DisplayString"
_SonicWirelessSpVersion_Object = MibScalar
sonicWirelessSpVersion = _SonicWirelessSpVersion_Object(
    (1, 3, 6, 1, 4, 1, 8741, 1, 3, 6, 1, 1),
    _SonicWirelessSpVersion_Type()
)
sonicWirelessSpVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonicWirelessSpVersion.setStatus("current")


class _SonicWirelessSpNVersion_Type(DisplayString):
    """Custom type sonicWirelessSpNVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_SonicWirelessSpNVersion_Type.__name__ = "DisplayString"
_SonicWirelessSpNVersion_Object = MibScalar
sonicWirelessSpNVersion = _SonicWirelessSpNVersion_Object(
    (1, 3, 6, 1, 4, 1, 8741, 1, 3, 6, 1, 2),
    _SonicWirelessSpNVersion_Type()
)
sonicWirelessSpNVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonicWirelessSpNVersion.setStatus("current")


class _SonicWirelessSpNvVersion_Type(DisplayString):
    """Custom type sonicWirelessSpNvVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_SonicWirelessSpNvVersion_Type.__name__ = "DisplayString"
_SonicWirelessSpNvVersion_Object = MibScalar
sonicWirelessSpNvVersion = _SonicWirelessSpNvVersion_Object(
    (1, 3, 6, 1, 4, 1, 8741, 1, 3, 6, 1, 3),
    _SonicWirelessSpNvVersion_Type()
)
sonicWirelessSpNvVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonicWirelessSpNvVersion.setStatus("current")


class _SonicWirelessSpNdrVersion_Type(DisplayString):
    """Custom type sonicWirelessSpNdrVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_SonicWirelessSpNdrVersion_Type.__name__ = "DisplayString"
_SonicWirelessSpNdrVersion_Object = MibScalar
sonicWirelessSpNdrVersion = _SonicWirelessSpNdrVersion_Object(
    (1, 3, 6, 1, 4, 1, 8741, 1, 3, 6, 1, 4),
    _SonicWirelessSpNdrVersion_Type()
)
sonicWirelessSpNdrVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonicWirelessSpNdrVersion.setStatus("current")


class _SonicWirelessSpAcVersion_Type(DisplayString):
    """Custom type sonicWirelessSpAcVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_SonicWirelessSpAcVersion_Type.__name__ = "DisplayString"
_SonicWirelessSpAcVersion_Object = MibScalar
sonicWirelessSpAcVersion = _SonicWirelessSpAcVersion_Object(
    (1, 3, 6, 1, 4, 1, 8741, 1, 3, 6, 1, 5),
    _SonicWirelessSpAcVersion_Type()
)
sonicWirelessSpAcVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonicWirelessSpAcVersion.setStatus("current")
_SonicWirelessApNumber_Type = Gauge32
_SonicWirelessApNumber_Object = MibScalar
sonicWirelessApNumber = _SonicWirelessApNumber_Object(
    (1, 3, 6, 1, 4, 1, 8741, 1, 3, 6, 1, 6),
    _SonicWirelessApNumber_Type()
)
sonicWirelessApNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonicWirelessApNumber.setStatus("current")
_SonicWirelessApTable_Object = MibTable
sonicWirelessApTable = _SonicWirelessApTable_Object(
    (1, 3, 6, 1, 4, 1, 8741, 1, 3, 6, 2)
)
if mibBuilder.loadTexts:
    sonicWirelessApTable.setStatus("current")
_SonicWirelessApEntry_Object = MibTableRow
sonicWirelessApEntry = _SonicWirelessApEntry_Object(
    (1, 3, 6, 1, 4, 1, 8741, 1, 3, 6, 2, 1)
)
sonicWirelessApEntry.setIndexNames(
    (0, "SONICWALL-FIREWALL-IP-STATISTICS-MIB", "sonicApIndex"),
)
if mibBuilder.loadTexts:
    sonicWirelessApEntry.setStatus("current")
_SonicApIndex_Type = Integer32
_SonicApIndex_Object = MibTableColumn
sonicApIndex = _SonicApIndex_Object(
    (1, 3, 6, 1, 4, 1, 8741, 1, 3, 6, 2, 1, 1),
    _SonicApIndex_Type()
)
sonicApIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sonicApIndex.setStatus("current")
_SonicApName_Type = DisplayString
_SonicApName_Object = MibTableColumn
sonicApName = _SonicApName_Object(
    (1, 3, 6, 1, 4, 1, 8741, 1, 3, 6, 2, 1, 2),
    _SonicApName_Type()
)
sonicApName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonicApName.setStatus("current")
_SonicApModel_Type = DisplayString
_SonicApModel_Object = MibTableColumn
sonicApModel = _SonicApModel_Object(
    (1, 3, 6, 1, 4, 1, 8741, 1, 3, 6, 2, 1, 3),
    _SonicApModel_Type()
)
sonicApModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonicApModel.setStatus("current")
_SonicApCountryCode_Type = Integer32
_SonicApCountryCode_Object = MibTableColumn
sonicApCountryCode = _SonicApCountryCode_Object(
    (1, 3, 6, 1, 4, 1, 8741, 1, 3, 6, 2, 1, 4),
    _SonicApCountryCode_Type()
)
sonicApCountryCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonicApCountryCode.setStatus("current")
_SonicApRetainSetting_Type = SwBoolState
_SonicApRetainSetting_Object = MibTableColumn
sonicApRetainSetting = _SonicApRetainSetting_Object(
    (1, 3, 6, 1, 4, 1, 8741, 1, 3, 6, 2, 1, 5),
    _SonicApRetainSetting_Type()
)
sonicApRetainSetting.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonicApRetainSetting.setStatus("current")
_SonicApRfManagement_Type = SwBoolState
_SonicApRfManagement_Object = MibTableColumn
sonicApRfManagement = _SonicApRfManagement_Object(
    (1, 3, 6, 1, 4, 1, 8741, 1, 3, 6, 2, 1, 6),
    _SonicApRfManagement_Type()
)
sonicApRfManagement.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonicApRfManagement.setStatus("current")
_SonicApInterface_Type = Integer32
_SonicApInterface_Object = MibTableColumn
sonicApInterface = _SonicApInterface_Object(
    (1, 3, 6, 1, 4, 1, 8741, 1, 3, 6, 2, 1, 7),
    _SonicApInterface_Type()
)
sonicApInterface.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonicApInterface.setStatus("current")
_SonicApIpAddr_Type = IpAddress
_SonicApIpAddr_Object = MibTableColumn
sonicApIpAddr = _SonicApIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 8741, 1, 3, 6, 2, 1, 8),
    _SonicApIpAddr_Type()
)
sonicApIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonicApIpAddr.setStatus("current")
_SonicApNetMask_Type = IpAddress
_SonicApNetMask_Object = MibTableColumn
sonicApNetMask = _SonicApNetMask_Object(
    (1, 3, 6, 1, 4, 1, 8741, 1, 3, 6, 2, 1, 9),
    _SonicApNetMask_Type()
)
sonicApNetMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonicApNetMask.setStatus("current")
_SonicApPhysicalAddress_Type = PhysAddress
_SonicApPhysicalAddress_Object = MibTableColumn
sonicApPhysicalAddress = _SonicApPhysicalAddress_Object(
    (1, 3, 6, 1, 4, 1, 8741, 1, 3, 6, 2, 1, 10),
    _SonicApPhysicalAddress_Type()
)
sonicApPhysicalAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonicApPhysicalAddress.setStatus("current")


class _SonicApMgmt_Type(Integer32):
    """Custom type sonicApMgmt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("layer-2", 1),
          ("layer-3", 2),
          ("sslvpn", 3))
    )


_SonicApMgmt_Type.__name__ = "Integer32"
_SonicApMgmt_Object = MibTableColumn
sonicApMgmt = _SonicApMgmt_Object(
    (1, 3, 6, 1, 4, 1, 8741, 1, 3, 6, 2, 1, 11),
    _SonicApMgmt_Type()
)
sonicApMgmt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonicApMgmt.setStatus("current")
_SonicApStatus_Type = SwSpWorkState
_SonicApStatus_Object = MibTableColumn
sonicApStatus = _SonicApStatus_Object(
    (1, 3, 6, 1, 4, 1, 8741, 1, 3, 6, 2, 1, 12),
    _SonicApStatus_Type()
)
sonicApStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonicApStatus.setStatus("current")
_SonicApProfile_Type = DisplayString
_SonicApProfile_Object = MibTableColumn
sonicApProfile = _SonicApProfile_Object(
    (1, 3, 6, 1, 4, 1, 8741, 1, 3, 6, 2, 1, 13),
    _SonicApProfile_Type()
)
sonicApProfile.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonicApProfile.setStatus("current")
_SonicApUpTime_Type = TimeTicks
_SonicApUpTime_Object = MibTableColumn
sonicApUpTime = _SonicApUpTime_Object(
    (1, 3, 6, 1, 4, 1, 8741, 1, 3, 6, 2, 1, 14),
    _SonicApUpTime_Type()
)
sonicApUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonicApUpTime.setStatus("current")


class _SonicApRadio0Bssid_Type(PhysAddress):
    """Custom type sonicApRadio0Bssid based on PhysAddress"""
    subtypeSpec = PhysAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
        ValueSizeConstraint(8, 8),
    )


_SonicApRadio0Bssid_Type.__name__ = "PhysAddress"
_SonicApRadio0Bssid_Object = MibTableColumn
sonicApRadio0Bssid = _SonicApRadio0Bssid_Object(
    (1, 3, 6, 1, 4, 1, 8741, 1, 3, 6, 2, 1, 15),
    _SonicApRadio0Bssid_Type()
)
sonicApRadio0Bssid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonicApRadio0Bssid.setStatus("current")
_SonicApRadio0SSID_Type = DisplayString
_SonicApRadio0SSID_Object = MibTableColumn
sonicApRadio0SSID = _SonicApRadio0SSID_Object(
    (1, 3, 6, 1, 4, 1, 8741, 1, 3, 6, 2, 1, 16),
    _SonicApRadio0SSID_Type()
)
sonicApRadio0SSID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonicApRadio0SSID.setStatus("current")
_SonicApRadio0Enable_Type = SwBoolState
_SonicApRadio0Enable_Object = MibTableColumn
sonicApRadio0Enable = _SonicApRadio0Enable_Object(
    (1, 3, 6, 1, 4, 1, 8741, 1, 3, 6, 2, 1, 17),
    _SonicApRadio0Enable_Type()
)
sonicApRadio0Enable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonicApRadio0Enable.setStatus("current")


class _SonicApRadio0Status_Type(Integer32):
    """Custom type sonicApRadio0Status based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("inactive", 1),
          ("active", 2))
    )


_SonicApRadio0Status_Type.__name__ = "Integer32"
_SonicApRadio0Status_Object = MibTableColumn
sonicApRadio0Status = _SonicApRadio0Status_Object(
    (1, 3, 6, 1, 4, 1, 8741, 1, 3, 6, 2, 1, 18),
    _SonicApRadio0Status_Type()
)
sonicApRadio0Status.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonicApRadio0Status.setStatus("current")
_SonicApRadio0Mode_Type = SwSpRadioType
_SonicApRadio0Mode_Object = MibTableColumn
sonicApRadio0Mode = _SonicApRadio0Mode_Object(
    (1, 3, 6, 1, 4, 1, 8741, 1, 3, 6, 2, 1, 19),
    _SonicApRadio0Mode_Type()
)
sonicApRadio0Mode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonicApRadio0Mode.setStatus("current")
_SonicApRadio0ChannelWidth_Type = SwSpChannelWidthType
_SonicApRadio0ChannelWidth_Object = MibTableColumn
sonicApRadio0ChannelWidth = _SonicApRadio0ChannelWidth_Object(
    (1, 3, 6, 1, 4, 1, 8741, 1, 3, 6, 2, 1, 20),
    _SonicApRadio0ChannelWidth_Type()
)
sonicApRadio0ChannelWidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonicApRadio0ChannelWidth.setStatus("current")
_SonicApRadio0Channel_Type = DisplayString
_SonicApRadio0Channel_Object = MibTableColumn
sonicApRadio0Channel = _SonicApRadio0Channel_Object(
    (1, 3, 6, 1, 4, 1, 8741, 1, 3, 6, 2, 1, 21),
    _SonicApRadio0Channel_Type()
)
sonicApRadio0Channel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonicApRadio0Channel.setStatus("current")
_SonicApRadio0ShortGuardInt_Type = SwBoolState
_SonicApRadio0ShortGuardInt_Object = MibTableColumn
sonicApRadio0ShortGuardInt = _SonicApRadio0ShortGuardInt_Object(
    (1, 3, 6, 1, 4, 1, 8741, 1, 3, 6, 2, 1, 22),
    _SonicApRadio0ShortGuardInt_Type()
)
sonicApRadio0ShortGuardInt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonicApRadio0ShortGuardInt.setStatus("current")
_SonicApRadio0Aggregation_Type = SwBoolState
_SonicApRadio0Aggregation_Object = MibTableColumn
sonicApRadio0Aggregation = _SonicApRadio0Aggregation_Object(
    (1, 3, 6, 1, 4, 1, 8741, 1, 3, 6, 2, 1, 23),
    _SonicApRadio0Aggregation_Type()
)
sonicApRadio0Aggregation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonicApRadio0Aggregation.setStatus("current")
_SonicApRadio0Mimo_Type = SwBoolState
_SonicApRadio0Mimo_Object = MibTableColumn
sonicApRadio0Mimo = _SonicApRadio0Mimo_Object(
    (1, 3, 6, 1, 4, 1, 8741, 1, 3, 6, 2, 1, 24),
    _SonicApRadio0Mimo_Type()
)
sonicApRadio0Mimo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonicApRadio0Mimo.setStatus("current")
_SonicApRadio0AuthType_Type = SwWlanAuthenticationType
_SonicApRadio0AuthType_Object = MibTableColumn
sonicApRadio0AuthType = _SonicApRadio0AuthType_Object(
    (1, 3, 6, 1, 4, 1, 8741, 1, 3, 6, 2, 1, 25),
    _SonicApRadio0AuthType_Type()
)
sonicApRadio0AuthType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonicApRadio0AuthType.setStatus("current")
_SonicApRadio0WpaCipher_Type = SwWlanCipherType
_SonicApRadio0WpaCipher_Object = MibTableColumn
sonicApRadio0WpaCipher = _SonicApRadio0WpaCipher_Object(
    (1, 3, 6, 1, 4, 1, 8741, 1, 3, 6, 2, 1, 26),
    _SonicApRadio0WpaCipher_Type()
)
sonicApRadio0WpaCipher.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonicApRadio0WpaCipher.setStatus("current")
_SonicApRadio0WpaPsk_Type = DisplayString
_SonicApRadio0WpaPsk_Object = MibTableColumn
sonicApRadio0WpaPsk = _SonicApRadio0WpaPsk_Object(
    (1, 3, 6, 1, 4, 1, 8741, 1, 3, 6, 2, 1, 27),
    _SonicApRadio0WpaPsk_Type()
)
sonicApRadio0WpaPsk.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonicApRadio0WpaPsk.setStatus("current")
_SonicApRadio0Acl_Type = SwBoolState
_SonicApRadio0Acl_Object = MibTableColumn
sonicApRadio0Acl = _SonicApRadio0Acl_Object(
    (1, 3, 6, 1, 4, 1, 8741, 1, 3, 6, 2, 1, 28),
    _SonicApRadio0Acl_Type()
)
sonicApRadio0Acl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonicApRadio0Acl.setStatus("current")
_SonicApRadio0BroadcastSsid_Type = SwBoolState
_SonicApRadio0BroadcastSsid_Object = MibTableColumn
sonicApRadio0BroadcastSsid = _SonicApRadio0BroadcastSsid_Object(
    (1, 3, 6, 1, 4, 1, 8741, 1, 3, 6, 2, 1, 29),
    _SonicApRadio0BroadcastSsid_Type()
)
sonicApRadio0BroadcastSsid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonicApRadio0BroadcastSsid.setStatus("current")
_SonicApRadio0TxPowerLevel_Type = SwSpRadioTxPower
_SonicApRadio0TxPowerLevel_Object = MibTableColumn
sonicApRadio0TxPowerLevel = _SonicApRadio0TxPowerLevel_Object(
    (1, 3, 6, 1, 4, 1, 8741, 1, 3, 6, 2, 1, 30),
    _SonicApRadio0TxPowerLevel_Type()
)
sonicApRadio0TxPowerLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonicApRadio0TxPowerLevel.setStatus("current")
_SonicApRadio0StaTimeout_Type = Gauge32
_SonicApRadio0StaTimeout_Object = MibTableColumn
sonicApRadio0StaTimeout = _SonicApRadio0StaTimeout_Object(
    (1, 3, 6, 1, 4, 1, 8741, 1, 3, 6, 2, 1, 31),
    _SonicApRadio0StaTimeout_Type()
)
sonicApRadio0StaTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonicApRadio0StaTimeout.setStatus("current")


class _SonicApRadio1Bssid_Type(PhysAddress):
    """Custom type sonicApRadio1Bssid based on PhysAddress"""
    subtypeSpec = PhysAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
        ValueSizeConstraint(8, 8),
    )


_SonicApRadio1Bssid_Type.__name__ = "PhysAddress"
_SonicApRadio1Bssid_Object = MibTableColumn
sonicApRadio1Bssid = _SonicApRadio1Bssid_Object(
    (1, 3, 6, 1, 4, 1, 8741, 1, 3, 6, 2, 1, 32),
    _SonicApRadio1Bssid_Type()
)
sonicApRadio1Bssid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonicApRadio1Bssid.setStatus("current")
_SonicApRadio1SSID_Type = DisplayString
_SonicApRadio1SSID_Object = MibTableColumn
sonicApRadio1SSID = _SonicApRadio1SSID_Object(
    (1, 3, 6, 1, 4, 1, 8741, 1, 3, 6, 2, 1, 33),
    _SonicApRadio1SSID_Type()
)
sonicApRadio1SSID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonicApRadio1SSID.setStatus("current")
_SonicApRadio1Enable_Type = SwBoolState
_SonicApRadio1Enable_Object = MibTableColumn
sonicApRadio1Enable = _SonicApRadio1Enable_Object(
    (1, 3, 6, 1, 4, 1, 8741, 1, 3, 6, 2, 1, 34),
    _SonicApRadio1Enable_Type()
)
sonicApRadio1Enable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonicApRadio1Enable.setStatus("current")


class _SonicApRadio1Status_Type(Integer32):
    """Custom type sonicApRadio1Status based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("inactive", 1),
          ("active", 2))
    )


_SonicApRadio1Status_Type.__name__ = "Integer32"
_SonicApRadio1Status_Object = MibTableColumn
sonicApRadio1Status = _SonicApRadio1Status_Object(
    (1, 3, 6, 1, 4, 1, 8741, 1, 3, 6, 2, 1, 35),
    _SonicApRadio1Status_Type()
)
sonicApRadio1Status.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonicApRadio1Status.setStatus("current")
_SonicApRadio1Mode_Type = SwSpRadioType
_SonicApRadio1Mode_Object = MibTableColumn
sonicApRadio1Mode = _SonicApRadio1Mode_Object(
    (1, 3, 6, 1, 4, 1, 8741, 1, 3, 6, 2, 1, 36),
    _SonicApRadio1Mode_Type()
)
sonicApRadio1Mode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonicApRadio1Mode.setStatus("current")
_SonicApRadio1ChannelWidth_Type = SwSpChannelWidthType
_SonicApRadio1ChannelWidth_Object = MibTableColumn
sonicApRadio1ChannelWidth = _SonicApRadio1ChannelWidth_Object(
    (1, 3, 6, 1, 4, 1, 8741, 1, 3, 6, 2, 1, 37),
    _SonicApRadio1ChannelWidth_Type()
)
sonicApRadio1ChannelWidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonicApRadio1ChannelWidth.setStatus("current")
_SonicApRadio1Channel_Type = DisplayString
_SonicApRadio1Channel_Object = MibTableColumn
sonicApRadio1Channel = _SonicApRadio1Channel_Object(
    (1, 3, 6, 1, 4, 1, 8741, 1, 3, 6, 2, 1, 38),
    _SonicApRadio1Channel_Type()
)
sonicApRadio1Channel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonicApRadio1Channel.setStatus("current")
_SonicApRadio1ShortGuardInt_Type = SwBoolState
_SonicApRadio1ShortGuardInt_Object = MibTableColumn
sonicApRadio1ShortGuardInt = _SonicApRadio1ShortGuardInt_Object(
    (1, 3, 6, 1, 4, 1, 8741, 1, 3, 6, 2, 1, 39),
    _SonicApRadio1ShortGuardInt_Type()
)
sonicApRadio1ShortGuardInt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonicApRadio1ShortGuardInt.setStatus("current")
_SonicApRadio1Aggregation_Type = SwBoolState
_SonicApRadio1Aggregation_Object = MibTableColumn
sonicApRadio1Aggregation = _SonicApRadio1Aggregation_Object(
    (1, 3, 6, 1, 4, 1, 8741, 1, 3, 6, 2, 1, 40),
    _SonicApRadio1Aggregation_Type()
)
sonicApRadio1Aggregation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonicApRadio1Aggregation.setStatus("current")
_SonicApRadio1Mimo_Type = SwBoolState
_SonicApRadio1Mimo_Object = MibTableColumn
sonicApRadio1Mimo = _SonicApRadio1Mimo_Object(
    (1, 3, 6, 1, 4, 1, 8741, 1, 3, 6, 2, 1, 41),
    _SonicApRadio1Mimo_Type()
)
sonicApRadio1Mimo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonicApRadio1Mimo.setStatus("current")
_SonicApRadio1AuthType_Type = SwWlanAuthenticationType
_SonicApRadio1AuthType_Object = MibTableColumn
sonicApRadio1AuthType = _SonicApRadio1AuthType_Object(
    (1, 3, 6, 1, 4, 1, 8741, 1, 3, 6, 2, 1, 42),
    _SonicApRadio1AuthType_Type()
)
sonicApRadio1AuthType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonicApRadio1AuthType.setStatus("current")
_SonicApRadio1WpaCipher_Type = SwWlanCipherType
_SonicApRadio1WpaCipher_Object = MibTableColumn
sonicApRadio1WpaCipher = _SonicApRadio1WpaCipher_Object(
    (1, 3, 6, 1, 4, 1, 8741, 1, 3, 6, 2, 1, 43),
    _SonicApRadio1WpaCipher_Type()
)
sonicApRadio1WpaCipher.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonicApRadio1WpaCipher.setStatus("current")
_SonicApRadio1WpaPsk_Type = DisplayString
_SonicApRadio1WpaPsk_Object = MibTableColumn
sonicApRadio1WpaPsk = _SonicApRadio1WpaPsk_Object(
    (1, 3, 6, 1, 4, 1, 8741, 1, 3, 6, 2, 1, 44),
    _SonicApRadio1WpaPsk_Type()
)
sonicApRadio1WpaPsk.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonicApRadio1WpaPsk.setStatus("current")
_SonicApRadio1Acl_Type = SwBoolState
_SonicApRadio1Acl_Object = MibTableColumn
sonicApRadio1Acl = _SonicApRadio1Acl_Object(
    (1, 3, 6, 1, 4, 1, 8741, 1, 3, 6, 2, 1, 45),
    _SonicApRadio1Acl_Type()
)
sonicApRadio1Acl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonicApRadio1Acl.setStatus("current")
_SonicApRadio1BroadcastSsid_Type = SwBoolState
_SonicApRadio1BroadcastSsid_Object = MibTableColumn
sonicApRadio1BroadcastSsid = _SonicApRadio1BroadcastSsid_Object(
    (1, 3, 6, 1, 4, 1, 8741, 1, 3, 6, 2, 1, 46),
    _SonicApRadio1BroadcastSsid_Type()
)
sonicApRadio1BroadcastSsid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonicApRadio1BroadcastSsid.setStatus("current")
_SonicApRadio1TxPowerLevel_Type = SwSpRadioTxPower
_SonicApRadio1TxPowerLevel_Object = MibTableColumn
sonicApRadio1TxPowerLevel = _SonicApRadio1TxPowerLevel_Object(
    (1, 3, 6, 1, 4, 1, 8741, 1, 3, 6, 2, 1, 47),
    _SonicApRadio1TxPowerLevel_Type()
)
sonicApRadio1TxPowerLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonicApRadio1TxPowerLevel.setStatus("current")
_SonicApRadio1StaTimeout_Type = Gauge32
_SonicApRadio1StaTimeout_Object = MibTableColumn
sonicApRadio1StaTimeout = _SonicApRadio1StaTimeout_Object(
    (1, 3, 6, 1, 4, 1, 8741, 1, 3, 6, 2, 1, 48),
    _SonicApRadio1StaTimeout_Type()
)
sonicApRadio1StaTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonicApRadio1StaTimeout.setStatus("current")
_SonicApRadiusServerIp1_Type = IpAddress
_SonicApRadiusServerIp1_Object = MibTableColumn
sonicApRadiusServerIp1 = _SonicApRadiusServerIp1_Object(
    (1, 3, 6, 1, 4, 1, 8741, 1, 3, 6, 2, 1, 49),
    _SonicApRadiusServerIp1_Type()
)
sonicApRadiusServerIp1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonicApRadiusServerIp1.setStatus("current")
_SonicApRadiusServerPort1_Type = Unsigned32
_SonicApRadiusServerPort1_Object = MibTableColumn
sonicApRadiusServerPort1 = _SonicApRadiusServerPort1_Object(
    (1, 3, 6, 1, 4, 1, 8741, 1, 3, 6, 2, 1, 50),
    _SonicApRadiusServerPort1_Type()
)
sonicApRadiusServerPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonicApRadiusServerPort1.setStatus("current")
_SonicApRadiusServerSecret1_Type = DisplayString
_SonicApRadiusServerSecret1_Object = MibTableColumn
sonicApRadiusServerSecret1 = _SonicApRadiusServerSecret1_Object(
    (1, 3, 6, 1, 4, 1, 8741, 1, 3, 6, 2, 1, 51),
    _SonicApRadiusServerSecret1_Type()
)
sonicApRadiusServerSecret1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonicApRadiusServerSecret1.setStatus("current")
_SonicApRadiusServerIp2_Type = IpAddress
_SonicApRadiusServerIp2_Object = MibTableColumn
sonicApRadiusServerIp2 = _SonicApRadiusServerIp2_Object(
    (1, 3, 6, 1, 4, 1, 8741, 1, 3, 6, 2, 1, 52),
    _SonicApRadiusServerIp2_Type()
)
sonicApRadiusServerIp2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonicApRadiusServerIp2.setStatus("current")
_SonicApRadiusServerPort2_Type = Unsigned32
_SonicApRadiusServerPort2_Object = MibTableColumn
sonicApRadiusServerPort2 = _SonicApRadiusServerPort2_Object(
    (1, 3, 6, 1, 4, 1, 8741, 1, 3, 6, 2, 1, 53),
    _SonicApRadiusServerPort2_Type()
)
sonicApRadiusServerPort2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonicApRadiusServerPort2.setStatus("current")
_SonicApRadiusServerSecret2_Type = DisplayString
_SonicApRadiusServerSecret2_Object = MibTableColumn
sonicApRadiusServerSecret2 = _SonicApRadiusServerSecret2_Object(
    (1, 3, 6, 1, 4, 1, 8741, 1, 3, 6, 2, 1, 54),
    _SonicApRadiusServerSecret2_Type()
)
sonicApRadiusServerSecret2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonicApRadiusServerSecret2.setStatus("current")
_SonicWirelessVapTable_Object = MibTable
sonicWirelessVapTable = _SonicWirelessVapTable_Object(
    (1, 3, 6, 1, 4, 1, 8741, 1, 3, 6, 3)
)
if mibBuilder.loadTexts:
    sonicWirelessVapTable.setStatus("current")
_SonicWirelessVapEntry_Object = MibTableRow
sonicWirelessVapEntry = _SonicWirelessVapEntry_Object(
    (1, 3, 6, 1, 4, 1, 8741, 1, 3, 6, 3, 1)
)
sonicWirelessVapEntry.setIndexNames(
    (0, "SONICWALL-FIREWALL-IP-STATISTICS-MIB", "sonicWirelessVapIndex"),
)
if mibBuilder.loadTexts:
    sonicWirelessVapEntry.setStatus("current")
_SonicWirelessVapIndex_Type = Integer32
_SonicWirelessVapIndex_Object = MibTableColumn
sonicWirelessVapIndex = _SonicWirelessVapIndex_Object(
    (1, 3, 6, 1, 4, 1, 8741, 1, 3, 6, 3, 1, 1),
    _SonicWirelessVapIndex_Type()
)
sonicWirelessVapIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonicWirelessVapIndex.setStatus("current")
_SonicWirelessVapName_Type = DisplayString
_SonicWirelessVapName_Object = MibTableColumn
sonicWirelessVapName = _SonicWirelessVapName_Object(
    (1, 3, 6, 1, 4, 1, 8741, 1, 3, 6, 3, 1, 2),
    _SonicWirelessVapName_Type()
)
sonicWirelessVapName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonicWirelessVapName.setStatus("current")
_SonicWirelessVapStatus_Type = SwBoolState
_SonicWirelessVapStatus_Object = MibTableColumn
sonicWirelessVapStatus = _SonicWirelessVapStatus_Object(
    (1, 3, 6, 1, 4, 1, 8741, 1, 3, 6, 3, 1, 3),
    _SonicWirelessVapStatus_Type()
)
sonicWirelessVapStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonicWirelessVapStatus.setStatus("current")


class _SonicWirelessVapSsid_Type(OctetString):
    """Custom type sonicWirelessVapSsid based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_SonicWirelessVapSsid_Type.__name__ = "OctetString"
_SonicWirelessVapSsid_Object = MibTableColumn
sonicWirelessVapSsid = _SonicWirelessVapSsid_Object(
    (1, 3, 6, 1, 4, 1, 8741, 1, 3, 6, 3, 1, 4),
    _SonicWirelessVapSsid_Type()
)
sonicWirelessVapSsid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonicWirelessVapSsid.setStatus("current")
_SonicWirelessVapBroadcastSsid_Type = SwBoolState
_SonicWirelessVapBroadcastSsid_Object = MibTableColumn
sonicWirelessVapBroadcastSsid = _SonicWirelessVapBroadcastSsid_Object(
    (1, 3, 6, 1, 4, 1, 8741, 1, 3, 6, 3, 1, 5),
    _SonicWirelessVapBroadcastSsid_Type()
)
sonicWirelessVapBroadcastSsid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonicWirelessVapBroadcastSsid.setStatus("current")


class _SonicWirelessVapVlanId_Type(Integer32):
    """Custom type sonicWirelessVapVlanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 4094),
        ValueRangeConstraint(4095, 4095),
    )


_SonicWirelessVapVlanId_Type.__name__ = "Integer32"
_SonicWirelessVapVlanId_Object = MibTableColumn
sonicWirelessVapVlanId = _SonicWirelessVapVlanId_Object(
    (1, 3, 6, 1, 4, 1, 8741, 1, 3, 6, 3, 1, 6),
    _SonicWirelessVapVlanId_Type()
)
sonicWirelessVapVlanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonicWirelessVapVlanId.setStatus("current")
_SonicWirelessVapAuthentication_Type = SwWlanAuthenticationType
_SonicWirelessVapAuthentication_Object = MibTableColumn
sonicWirelessVapAuthentication = _SonicWirelessVapAuthentication_Object(
    (1, 3, 6, 1, 4, 1, 8741, 1, 3, 6, 3, 1, 7),
    _SonicWirelessVapAuthentication_Type()
)
sonicWirelessVapAuthentication.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonicWirelessVapAuthentication.setStatus("current")
_SonicWirelessVapCipher_Type = SwWlanCipherType
_SonicWirelessVapCipher_Object = MibTableColumn
sonicWirelessVapCipher = _SonicWirelessVapCipher_Object(
    (1, 3, 6, 1, 4, 1, 8741, 1, 3, 6, 3, 1, 8),
    _SonicWirelessVapCipher_Type()
)
sonicWirelessVapCipher.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonicWirelessVapCipher.setStatus("current")
_SonicWirelessVapPassPhrase_Type = DisplayString
_SonicWirelessVapPassPhrase_Object = MibTableColumn
sonicWirelessVapPassPhrase = _SonicWirelessVapPassPhrase_Object(
    (1, 3, 6, 1, 4, 1, 8741, 1, 3, 6, 3, 1, 9),
    _SonicWirelessVapPassPhrase_Type()
)
sonicWirelessVapPassPhrase.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonicWirelessVapPassPhrase.setStatus("current")
_SonicWirelessVapRadiusServerIp1_Type = IpAddress
_SonicWirelessVapRadiusServerIp1_Object = MibTableColumn
sonicWirelessVapRadiusServerIp1 = _SonicWirelessVapRadiusServerIp1_Object(
    (1, 3, 6, 1, 4, 1, 8741, 1, 3, 6, 3, 1, 10),
    _SonicWirelessVapRadiusServerIp1_Type()
)
sonicWirelessVapRadiusServerIp1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonicWirelessVapRadiusServerIp1.setStatus("current")
_SonicWirelessVapRadiusServerPort1_Type = Unsigned32
_SonicWirelessVapRadiusServerPort1_Object = MibTableColumn
sonicWirelessVapRadiusServerPort1 = _SonicWirelessVapRadiusServerPort1_Object(
    (1, 3, 6, 1, 4, 1, 8741, 1, 3, 6, 3, 1, 11),
    _SonicWirelessVapRadiusServerPort1_Type()
)
sonicWirelessVapRadiusServerPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonicWirelessVapRadiusServerPort1.setStatus("current")
_SonicWirelessVapRadiusServerSecret1_Type = DisplayString
_SonicWirelessVapRadiusServerSecret1_Object = MibTableColumn
sonicWirelessVapRadiusServerSecret1 = _SonicWirelessVapRadiusServerSecret1_Object(
    (1, 3, 6, 1, 4, 1, 8741, 1, 3, 6, 3, 1, 12),
    _SonicWirelessVapRadiusServerSecret1_Type()
)
sonicWirelessVapRadiusServerSecret1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonicWirelessVapRadiusServerSecret1.setStatus("current")
_SonicWirelessVapRadiusServerIp2_Type = IpAddress
_SonicWirelessVapRadiusServerIp2_Object = MibTableColumn
sonicWirelessVapRadiusServerIp2 = _SonicWirelessVapRadiusServerIp2_Object(
    (1, 3, 6, 1, 4, 1, 8741, 1, 3, 6, 3, 1, 13),
    _SonicWirelessVapRadiusServerIp2_Type()
)
sonicWirelessVapRadiusServerIp2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonicWirelessVapRadiusServerIp2.setStatus("current")
_SonicWirelessVapRadiusServerPort2_Type = Unsigned32
_SonicWirelessVapRadiusServerPort2_Object = MibTableColumn
sonicWirelessVapRadiusServerPort2 = _SonicWirelessVapRadiusServerPort2_Object(
    (1, 3, 6, 1, 4, 1, 8741, 1, 3, 6, 3, 1, 14),
    _SonicWirelessVapRadiusServerPort2_Type()
)
sonicWirelessVapRadiusServerPort2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonicWirelessVapRadiusServerPort2.setStatus("current")
_SonicWirelessVapRadiusServerSecret2_Type = DisplayString
_SonicWirelessVapRadiusServerSecret2_Object = MibTableColumn
sonicWirelessVapRadiusServerSecret2 = _SonicWirelessVapRadiusServerSecret2_Object(
    (1, 3, 6, 1, 4, 1, 8741, 1, 3, 6, 3, 1, 15),
    _SonicWirelessVapRadiusServerSecret2_Type()
)
sonicWirelessVapRadiusServerSecret2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonicWirelessVapRadiusServerSecret2.setStatus("current")
_SonicWirelessVapReference_Type = DisplayString
_SonicWirelessVapReference_Object = MibTableColumn
sonicWirelessVapReference = _SonicWirelessVapReference_Object(
    (1, 3, 6, 1, 4, 1, 8741, 1, 3, 6, 3, 1, 16),
    _SonicWirelessVapReference_Type()
)
sonicWirelessVapReference.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonicWirelessVapReference.setStatus("current")
_SonicWirelessVapMaxClient_Type = Gauge32
_SonicWirelessVapMaxClient_Object = MibTableColumn
sonicWirelessVapMaxClient = _SonicWirelessVapMaxClient_Object(
    (1, 3, 6, 1, 4, 1, 8741, 1, 3, 6, 3, 1, 17),
    _SonicWirelessVapMaxClient_Type()
)
sonicWirelessVapMaxClient.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonicWirelessVapMaxClient.setStatus("current")
_SonicWirelessVapCurClient_Type = Gauge32
_SonicWirelessVapCurClient_Object = MibTableColumn
sonicWirelessVapCurClient = _SonicWirelessVapCurClient_Object(
    (1, 3, 6, 1, 4, 1, 8741, 1, 3, 6, 3, 1, 18),
    _SonicWirelessVapCurClient_Type()
)
sonicWirelessVapCurClient.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonicWirelessVapCurClient.setStatus("current")
_SonicWirelessStaTable_Object = MibTable
sonicWirelessStaTable = _SonicWirelessStaTable_Object(
    (1, 3, 6, 1, 4, 1, 8741, 1, 3, 6, 4)
)
if mibBuilder.loadTexts:
    sonicWirelessStaTable.setStatus("current")
_SonicWirelessStaEntry_Object = MibTableRow
sonicWirelessStaEntry = _SonicWirelessStaEntry_Object(
    (1, 3, 6, 1, 4, 1, 8741, 1, 3, 6, 4, 1)
)
sonicWirelessStaEntry.setIndexNames(
    (0, "SONICWALL-FIREWALL-IP-STATISTICS-MIB", "sonicStaPhysAddress"),
)
if mibBuilder.loadTexts:
    sonicWirelessStaEntry.setStatus("current")
_SonicStaPhysAddress_Type = PhysAddress
_SonicStaPhysAddress_Object = MibTableColumn
sonicStaPhysAddress = _SonicStaPhysAddress_Object(
    (1, 3, 6, 1, 4, 1, 8741, 1, 3, 6, 4, 1, 1),
    _SonicStaPhysAddress_Type()
)
sonicStaPhysAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonicStaPhysAddress.setStatus("current")
_SonicStaApName_Type = DisplayString
_SonicStaApName_Object = MibTableColumn
sonicStaApName = _SonicStaApName_Object(
    (1, 3, 6, 1, 4, 1, 8741, 1, 3, 6, 4, 1, 2),
    _SonicStaApName_Type()
)
sonicStaApName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonicStaApName.setStatus("current")
_SonicStaChannel_Type = SwSpRadioChannelNumber
_SonicStaChannel_Object = MibTableColumn
sonicStaChannel = _SonicStaChannel_Object(
    (1, 3, 6, 1, 4, 1, 8741, 1, 3, 6, 4, 1, 3),
    _SonicStaChannel_Type()
)
sonicStaChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonicStaChannel.setStatus("current")
_SonicStaAid_Type = Integer32
_SonicStaAid_Object = MibTableColumn
sonicStaAid = _SonicStaAid_Object(
    (1, 3, 6, 1, 4, 1, 8741, 1, 3, 6, 4, 1, 4),
    _SonicStaAid_Type()
)
sonicStaAid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonicStaAid.setStatus("current")
_SonicStaIpAddress_Type = IpAddress
_SonicStaIpAddress_Object = MibTableColumn
sonicStaIpAddress = _SonicStaIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 8741, 1, 3, 6, 4, 1, 5),
    _SonicStaIpAddress_Type()
)
sonicStaIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonicStaIpAddress.setStatus("current")
_SonicStaStatus_Type = SwStationStatus
_SonicStaStatus_Object = MibTableColumn
sonicStaStatus = _SonicStaStatus_Object(
    (1, 3, 6, 1, 4, 1, 8741, 1, 3, 6, 4, 1, 6),
    _SonicStaStatus_Type()
)
sonicStaStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonicStaStatus.setStatus("current")


class _SonicStaRadioType_Type(Integer32):
    """Custom type sonicStaRadioType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("radio0", 0),
          ("radio1", 1))
    )


_SonicStaRadioType_Type.__name__ = "Integer32"
_SonicStaRadioType_Object = MibTableColumn
sonicStaRadioType = _SonicStaRadioType_Object(
    (1, 3, 6, 1, 4, 1, 8741, 1, 3, 6, 4, 1, 7),
    _SonicStaRadioType_Type()
)
sonicStaRadioType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonicStaRadioType.setStatus("current")
_SonicStaSsid_Type = DisplayString
_SonicStaSsid_Object = MibTableColumn
sonicStaSsid = _SonicStaSsid_Object(
    (1, 3, 6, 1, 4, 1, 8741, 1, 3, 6, 4, 1, 8),
    _SonicStaSsid_Type()
)
sonicStaSsid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonicStaSsid.setStatus("current")


class _SonicStaVlanId_Type(Integer32):
    """Custom type sonicStaVlanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 4094),
        ValueRangeConstraint(4095, 4095),
    )


_SonicStaVlanId_Type.__name__ = "Integer32"
_SonicStaVlanId_Object = MibTableColumn
sonicStaVlanId = _SonicStaVlanId_Object(
    (1, 3, 6, 1, 4, 1, 8741, 1, 3, 6, 4, 1, 9),
    _SonicStaVlanId_Type()
)
sonicStaVlanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonicStaVlanId.setStatus("current")
_SonicStaConnRate_Type = Gauge32
_SonicStaConnRate_Object = MibTableColumn
sonicStaConnRate = _SonicStaConnRate_Object(
    (1, 3, 6, 1, 4, 1, 8741, 1, 3, 6, 4, 1, 10),
    _SonicStaConnRate_Type()
)
sonicStaConnRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonicStaConnRate.setStatus("current")
_SonicStaTxRate_Type = Gauge32
_SonicStaTxRate_Object = MibTableColumn
sonicStaTxRate = _SonicStaTxRate_Object(
    (1, 3, 6, 1, 4, 1, 8741, 1, 3, 6, 4, 1, 11),
    _SonicStaTxRate_Type()
)
sonicStaTxRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonicStaTxRate.setStatus("current")
_SonicStaSignalStrength_Type = Gauge32
_SonicStaSignalStrength_Object = MibTableColumn
sonicStaSignalStrength = _SonicStaSignalStrength_Object(
    (1, 3, 6, 1, 4, 1, 8741, 1, 3, 6, 4, 1, 12),
    _SonicStaSignalStrength_Type()
)
sonicStaSignalStrength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonicStaSignalStrength.setStatus("current")
_SonicStaAssociations_Type = Counter32
_SonicStaAssociations_Object = MibTableColumn
sonicStaAssociations = _SonicStaAssociations_Object(
    (1, 3, 6, 1, 4, 1, 8741, 1, 3, 6, 4, 1, 13),
    _SonicStaAssociations_Type()
)
sonicStaAssociations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonicStaAssociations.setStatus("current")
_SonicStaDisassociations_Type = Counter32
_SonicStaDisassociations_Object = MibTableColumn
sonicStaDisassociations = _SonicStaDisassociations_Object(
    (1, 3, 6, 1, 4, 1, 8741, 1, 3, 6, 4, 1, 14),
    _SonicStaDisassociations_Type()
)
sonicStaDisassociations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonicStaDisassociations.setStatus("current")
_SonicStaReassociations_Type = Counter32
_SonicStaReassociations_Object = MibTableColumn
sonicStaReassociations = _SonicStaReassociations_Object(
    (1, 3, 6, 1, 4, 1, 8741, 1, 3, 6, 4, 1, 15),
    _SonicStaReassociations_Type()
)
sonicStaReassociations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonicStaReassociations.setStatus("current")
_SonicStaAuthentications_Type = Counter32
_SonicStaAuthentications_Object = MibTableColumn
sonicStaAuthentications = _SonicStaAuthentications_Object(
    (1, 3, 6, 1, 4, 1, 8741, 1, 3, 6, 4, 1, 16),
    _SonicStaAuthentications_Type()
)
sonicStaAuthentications.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonicStaAuthentications.setStatus("current")
_SonicStaDeauthentications_Type = Counter32
_SonicStaDeauthentications_Object = MibTableColumn
sonicStaDeauthentications = _SonicStaDeauthentications_Object(
    (1, 3, 6, 1, 4, 1, 8741, 1, 3, 6, 4, 1, 17),
    _SonicStaDeauthentications_Type()
)
sonicStaDeauthentications.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonicStaDeauthentications.setStatus("current")
_SonicStaDiscardPkts_Type = Counter32
_SonicStaDiscardPkts_Object = MibTableColumn
sonicStaDiscardPkts = _SonicStaDiscardPkts_Object(
    (1, 3, 6, 1, 4, 1, 8741, 1, 3, 6, 4, 1, 18),
    _SonicStaDiscardPkts_Type()
)
sonicStaDiscardPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonicStaDiscardPkts.setStatus("current")
_SonicStaGoodPktsRx_Type = Counter32
_SonicStaGoodPktsRx_Object = MibTableColumn
sonicStaGoodPktsRx = _SonicStaGoodPktsRx_Object(
    (1, 3, 6, 1, 4, 1, 8741, 1, 3, 6, 4, 1, 19),
    _SonicStaGoodPktsRx_Type()
)
sonicStaGoodPktsRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonicStaGoodPktsRx.setStatus("current")
_SonicStaBadPktsRx_Type = Counter32
_SonicStaBadPktsRx_Object = MibTableColumn
sonicStaBadPktsRx = _SonicStaBadPktsRx_Object(
    (1, 3, 6, 1, 4, 1, 8741, 1, 3, 6, 4, 1, 20),
    _SonicStaBadPktsRx_Type()
)
sonicStaBadPktsRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonicStaBadPktsRx.setStatus("current")
_SonicStaGoodBytesRx_Type = Counter32
_SonicStaGoodBytesRx_Object = MibTableColumn
sonicStaGoodBytesRx = _SonicStaGoodBytesRx_Object(
    (1, 3, 6, 1, 4, 1, 8741, 1, 3, 6, 4, 1, 21),
    _SonicStaGoodBytesRx_Type()
)
sonicStaGoodBytesRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonicStaGoodBytesRx.setStatus("current")
_SonicStaMgmtPktsRx_Type = Counter32
_SonicStaMgmtPktsRx_Object = MibTableColumn
sonicStaMgmtPktsRx = _SonicStaMgmtPktsRx_Object(
    (1, 3, 6, 1, 4, 1, 8741, 1, 3, 6, 4, 1, 22),
    _SonicStaMgmtPktsRx_Type()
)
sonicStaMgmtPktsRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonicStaMgmtPktsRx.setStatus("current")
_SonicStaCtrlPktsRx_Type = Counter32
_SonicStaCtrlPktsRx_Object = MibTableColumn
sonicStaCtrlPktsRx = _SonicStaCtrlPktsRx_Object(
    (1, 3, 6, 1, 4, 1, 8741, 1, 3, 6, 4, 1, 23),
    _SonicStaCtrlPktsRx_Type()
)
sonicStaCtrlPktsRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonicStaCtrlPktsRx.setStatus("current")
_SonicStaDataPktsRx_Type = Counter32
_SonicStaDataPktsRx_Object = MibTableColumn
sonicStaDataPktsRx = _SonicStaDataPktsRx_Object(
    (1, 3, 6, 1, 4, 1, 8741, 1, 3, 6, 4, 1, 24),
    _SonicStaDataPktsRx_Type()
)
sonicStaDataPktsRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonicStaDataPktsRx.setStatus("current")
_SonicStaGoodPktsTx_Type = Counter32
_SonicStaGoodPktsTx_Object = MibTableColumn
sonicStaGoodPktsTx = _SonicStaGoodPktsTx_Object(
    (1, 3, 6, 1, 4, 1, 8741, 1, 3, 6, 4, 1, 25),
    _SonicStaGoodPktsTx_Type()
)
sonicStaGoodPktsTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonicStaGoodPktsTx.setStatus("current")
_SonicStaBadPktsTx_Type = Counter32
_SonicStaBadPktsTx_Object = MibTableColumn
sonicStaBadPktsTx = _SonicStaBadPktsTx_Object(
    (1, 3, 6, 1, 4, 1, 8741, 1, 3, 6, 4, 1, 26),
    _SonicStaBadPktsTx_Type()
)
sonicStaBadPktsTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonicStaBadPktsTx.setStatus("current")
_SonicStaGoodBytesTx_Type = Counter32
_SonicStaGoodBytesTx_Object = MibTableColumn
sonicStaGoodBytesTx = _SonicStaGoodBytesTx_Object(
    (1, 3, 6, 1, 4, 1, 8741, 1, 3, 6, 4, 1, 27),
    _SonicStaGoodBytesTx_Type()
)
sonicStaGoodBytesTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonicStaGoodBytesTx.setStatus("current")
_SonicStaMgmtPktsTx_Type = Counter32
_SonicStaMgmtPktsTx_Object = MibTableColumn
sonicStaMgmtPktsTx = _SonicStaMgmtPktsTx_Object(
    (1, 3, 6, 1, 4, 1, 8741, 1, 3, 6, 4, 1, 28),
    _SonicStaMgmtPktsTx_Type()
)
sonicStaMgmtPktsTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonicStaMgmtPktsTx.setStatus("current")
_SonicStaCtrlPktsTx_Type = Counter32
_SonicStaCtrlPktsTx_Object = MibTableColumn
sonicStaCtrlPktsTx = _SonicStaCtrlPktsTx_Object(
    (1, 3, 6, 1, 4, 1, 8741, 1, 3, 6, 4, 1, 29),
    _SonicStaCtrlPktsTx_Type()
)
sonicStaCtrlPktsTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonicStaCtrlPktsTx.setStatus("current")
_SonicStaDataPktsTx_Type = Counter32
_SonicStaDataPktsTx_Object = MibTableColumn
sonicStaDataPktsTx = _SonicStaDataPktsTx_Object(
    (1, 3, 6, 1, 4, 1, 8741, 1, 3, 6, 4, 1, 30),
    _SonicStaDataPktsTx_Type()
)
sonicStaDataPktsTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonicStaDataPktsTx.setStatus("current")
_SonicStaConnSta_Type = Gauge32
_SonicStaConnSta_Object = MibTableColumn
sonicStaConnSta = _SonicStaConnSta_Object(
    (1, 3, 6, 1, 4, 1, 8741, 1, 3, 6, 4, 1, 31),
    _SonicStaConnSta_Type()
)
sonicStaConnSta.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonicStaConnSta.setStatus("current")
_SonicwallFwZoneStats_ObjectIdentity = ObjectIdentity
sonicwallFwZoneStats = _SonicwallFwZoneStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8741, 1, 3, 7)
)
_SonicwallFwZoneTables_ObjectIdentity = ObjectIdentity
sonicwallFwZoneTables = _SonicwallFwZoneTables_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8741, 1, 3, 7, 1)
)
_SonicwallFwZoneTable_Object = MibTable
sonicwallFwZoneTable = _SonicwallFwZoneTable_Object(
    (1, 3, 6, 1, 4, 1, 8741, 1, 3, 7, 1, 1)
)
if mibBuilder.loadTexts:
    sonicwallFwZoneTable.setStatus("current")
_SonicwallFwZoneEntry_Object = MibTableRow
sonicwallFwZoneEntry = _SonicwallFwZoneEntry_Object(
    (1, 3, 6, 1, 4, 1, 8741, 1, 3, 7, 1, 1, 1)
)
sonicwallFwZoneEntry.setIndexNames(
    (0, "SONICWALL-FIREWALL-IP-STATISTICS-MIB", "sonicZoneName"),
)
if mibBuilder.loadTexts:
    sonicwallFwZoneEntry.setStatus("current")


class _SonicZoneName_Type(DisplayString):
    """Custom type sonicZoneName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_SonicZoneName_Type.__name__ = "DisplayString"
_SonicZoneName_Object = MibTableColumn
sonicZoneName = _SonicZoneName_Object(
    (1, 3, 6, 1, 4, 1, 8741, 1, 3, 7, 1, 1, 1, 1),
    _SonicZoneName_Type()
)
sonicZoneName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonicZoneName.setStatus("current")
_SonicZoneSecurity_Type = SwZoneSecurityType
_SonicZoneSecurity_Object = MibTableColumn
sonicZoneSecurity = _SonicZoneSecurity_Object(
    (1, 3, 6, 1, 4, 1, 8741, 1, 3, 7, 1, 1, 1, 2),
    _SonicZoneSecurity_Type()
)
sonicZoneSecurity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonicZoneSecurity.setStatus("current")


class _SonicZoneInterfaces_Type(DisplayString):
    """Custom type sonicZoneInterfaces based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_SonicZoneInterfaces_Type.__name__ = "DisplayString"
_SonicZoneInterfaces_Object = MibTableColumn
sonicZoneInterfaces = _SonicZoneInterfaces_Object(
    (1, 3, 6, 1, 4, 1, 8741, 1, 3, 7, 1, 1, 1, 3),
    _SonicZoneInterfaces_Type()
)
sonicZoneInterfaces.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonicZoneInterfaces.setStatus("current")
_SonicZoneIfTrust_Type = SwBoolState
_SonicZoneIfTrust_Object = MibTableColumn
sonicZoneIfTrust = _SonicZoneIfTrust_Object(
    (1, 3, 6, 1, 4, 1, 8741, 1, 3, 7, 1, 1, 1, 4),
    _SonicZoneIfTrust_Type()
)
sonicZoneIfTrust.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonicZoneIfTrust.setStatus("current")
_SonicZoneCFS_Type = SwBoolState
_SonicZoneCFS_Object = MibTableColumn
sonicZoneCFS = _SonicZoneCFS_Object(
    (1, 3, 6, 1, 4, 1, 8741, 1, 3, 7, 1, 1, 1, 5),
    _SonicZoneCFS_Type()
)
sonicZoneCFS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonicZoneCFS.setStatus("deprecated")
_SonicZoneClientAv_Type = SwBoolState
_SonicZoneClientAv_Object = MibTableColumn
sonicZoneClientAv = _SonicZoneClientAv_Object(
    (1, 3, 6, 1, 4, 1, 8741, 1, 3, 7, 1, 1, 1, 6),
    _SonicZoneClientAv_Type()
)
sonicZoneClientAv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonicZoneClientAv.setStatus("current")
_SonicZoneClientCf_Type = SwBoolState
_SonicZoneClientCf_Object = MibTableColumn
sonicZoneClientCf = _SonicZoneClientCf_Object(
    (1, 3, 6, 1, 4, 1, 8741, 1, 3, 7, 1, 1, 1, 7),
    _SonicZoneClientCf_Type()
)
sonicZoneClientCf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonicZoneClientCf.setStatus("current")
_SonicZoneGwAv_Type = SwBoolState
_SonicZoneGwAv_Object = MibTableColumn
sonicZoneGwAv = _SonicZoneGwAv_Object(
    (1, 3, 6, 1, 4, 1, 8741, 1, 3, 7, 1, 1, 1, 8),
    _SonicZoneGwAv_Type()
)
sonicZoneGwAv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonicZoneGwAv.setStatus("current")
_SonicZoneAntiSpyware_Type = SwBoolState
_SonicZoneAntiSpyware_Object = MibTableColumn
sonicZoneAntiSpyware = _SonicZoneAntiSpyware_Object(
    (1, 3, 6, 1, 4, 1, 8741, 1, 3, 7, 1, 1, 1, 9),
    _SonicZoneAntiSpyware_Type()
)
sonicZoneAntiSpyware.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonicZoneAntiSpyware.setStatus("current")
_SonicZoneIps_Type = SwBoolState
_SonicZoneIps_Object = MibTableColumn
sonicZoneIps = _SonicZoneIps_Object(
    (1, 3, 6, 1, 4, 1, 8741, 1, 3, 7, 1, 1, 1, 10),
    _SonicZoneIps_Type()
)
sonicZoneIps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonicZoneIps.setStatus("current")
_SonicZoneAppControl_Type = SwBoolState
_SonicZoneAppControl_Object = MibTableColumn
sonicZoneAppControl = _SonicZoneAppControl_Object(
    (1, 3, 6, 1, 4, 1, 8741, 1, 3, 7, 1, 1, 1, 11),
    _SonicZoneAppControl_Type()
)
sonicZoneAppControl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonicZoneAppControl.setStatus("current")
_SonicZoneSslControl_Type = SwBoolState
_SonicZoneSslControl_Object = MibTableColumn
sonicZoneSslControl = _SonicZoneSslControl_Object(
    (1, 3, 6, 1, 4, 1, 8741, 1, 3, 7, 1, 1, 1, 12),
    _SonicZoneSslControl_Type()
)
sonicZoneSslControl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonicZoneSslControl.setStatus("current")
_SonicZoneSslvpnAccess_Type = SwBoolState
_SonicZoneSslvpnAccess_Object = MibTableColumn
sonicZoneSslvpnAccess = _SonicZoneSslvpnAccess_Object(
    (1, 3, 6, 1, 4, 1, 8741, 1, 3, 7, 1, 1, 1, 13),
    _SonicZoneSslvpnAccess_Type()
)
sonicZoneSslvpnAccess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonicZoneSslvpnAccess.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SONICWALL-FIREWALL-IP-STATISTICS-MIB",
    **{"SyslogFacility": SyslogFacility,
       "SwSpRadioType": SwSpRadioType,
       "SwSpChannelWidthType": SwSpChannelWidthType,
       "SwSpWorkState": SwSpWorkState,
       "SwStationStatus": SwStationStatus,
       "SwSpRadioChannelNumber": SwSpRadioChannelNumber,
       "SwSpRadioTxPower": SwSpRadioTxPower,
       "SwZoneSecurityType": SwZoneSecurityType,
       "SwBoolState": SwBoolState,
       "SwWlanAuthenticationType": SwWlanAuthenticationType,
       "SwWlanCipherType": SwWlanCipherType,
       "sonicwallFwStatsModule": sonicwallFwStatsModule,
       "sonicwallFwStats": sonicwallFwStats,
       "sonicMaxConnCacheEntries": sonicMaxConnCacheEntries,
       "sonicCurrentConnCacheEntries": sonicCurrentConnCacheEntries,
       "sonicCurrentCPUUtil": sonicCurrentCPUUtil,
       "sonicCurrentRAMUtil": sonicCurrentRAMUtil,
       "sonicNatTranslationCount": sonicNatTranslationCount,
       "sonicCurrentManagementCPUUtil": sonicCurrentManagementCPUUtil,
       "sonicCurrentFwdAndInspectCPUUtil": sonicCurrentFwdAndInspectCPUUtil,
       "sonicIfStatTable": sonicIfStatTable,
       "sonicIfStatEntry": sonicIfStatEntry,
       "sonicIfIndex": sonicIfIndex,
       "sonicIfUsage": sonicIfUsage,
       "sonicIfThroughput": sonicIfThroughput,
       "sonicCFS": sonicCFS,
       "sonicwallFwVPNStats": sonicwallFwVPNStats,
       "sonicwallFwVpnIPSecStats": sonicwallFwVpnIPSecStats,
       "sonicSAStatTable": sonicSAStatTable,
       "sonicSAStatEntry": sonicSAStatEntry,
       "sonicIpsecSaIndex": sonicIpsecSaIndex,
       "sonicSAStatPeerGateway": sonicSAStatPeerGateway,
       "sonicSAStatSrcAddrBegin": sonicSAStatSrcAddrBegin,
       "sonicSAStatSrcAddrEnd": sonicSAStatSrcAddrEnd,
       "sonicSAStatDstAddrBegin": sonicSAStatDstAddrBegin,
       "sonicSAStatDstAddrEnd": sonicSAStatDstAddrEnd,
       "sonicSAStatCreateTime": sonicSAStatCreateTime,
       "sonicSAStatEncryptPktCount": sonicSAStatEncryptPktCount,
       "sonicSAStatEncryptByteCount": sonicSAStatEncryptByteCount,
       "sonicSAStatDecryptPktCount": sonicSAStatDecryptPktCount,
       "sonicSAStatDecryptByteCount": sonicSAStatDecryptByteCount,
       "sonicSAStatInFragPktCount": sonicSAStatInFragPktCount,
       "sonicSAStatOutFragPktCount": sonicSAStatOutFragPktCount,
       "sonicSAStatUserName": sonicSAStatUserName,
       "sonicwallFwHWStats": sonicwallFwHWStats,
       "sonicwallFwHWSensorStats": sonicwallFwHWSensorStats,
       "sonicwallSensorsTable": sonicwallSensorsTable,
       "sonicwallSensorsEntry": sonicwallSensorsEntry,
       "sonicwallSensorsIndex": sonicwallSensorsIndex,
       "sonicwallSensorsId": sonicwallSensorsId,
       "sonicwallSensorsDevice": sonicwallSensorsDevice,
       "sonicwallSensorsValue": sonicwallSensorsValue,
       "sonicwallSensorsUnit": sonicwallSensorsUnit,
       "sonicwallFwSyslogStats": sonicwallFwSyslogStats,
       "sonicwallFwSyslogSetting": sonicwallFwSyslogSetting,
       "sonicSyslogFacility": sonicSyslogFacility,
       "sonicSyslogOverrideSetting": sonicSyslogOverrideSetting,
       "sonicSyslogFormat": sonicSyslogFormat,
       "sonicSyslogID": sonicSyslogID,
       "sonicSyslogEventRateLimitEnable": sonicSyslogEventRateLimitEnable,
       "sonicSyslogEventRateLimit": sonicSyslogEventRateLimit,
       "sonicSyslogDataRateLimitEnable": sonicSyslogDataRateLimitEnable,
       "sonicSyslogDataRateLimit": sonicSyslogDataRateLimit,
       "sonicSyslogNDPPEnable": sonicSyslogNDPPEnable,
       "sonicwallFwSyslogServer": sonicwallFwSyslogServer,
       "sonicSyslogMaxServers": sonicSyslogMaxServers,
       "sonicSyslogServerTable": sonicSyslogServerTable,
       "sonicSyslogServerEntry": sonicSyslogServerEntry,
       "sonicSyslogServerIndex": sonicSyslogServerIndex,
       "sonicSyslogServerAddr": sonicSyslogServerAddr,
       "sonicSyslogServerPort": sonicSyslogServerPort,
       "sonicwallFwSyslogStatistic": sonicwallFwSyslogStatistic,
       "sonicSyslogMessage": sonicSyslogMessage,
       "sonicSyslogStreamData": sonicSyslogStreamData,
       "sonicwallFwDpiSslStats": sonicwallFwDpiSslStats,
       "sonicDpiSslConnCountCur": sonicDpiSslConnCountCur,
       "sonicDpiSslConnCountHighWater": sonicDpiSslConnCountHighWater,
       "sonicDpiSslConnCountMax": sonicDpiSslConnCountMax,
       "sonicwallFwWirelessStats": sonicwallFwWirelessStats,
       "sonicWirelessSpInfo": sonicWirelessSpInfo,
       "sonicWirelessSpVersion": sonicWirelessSpVersion,
       "sonicWirelessSpNVersion": sonicWirelessSpNVersion,
       "sonicWirelessSpNvVersion": sonicWirelessSpNvVersion,
       "sonicWirelessSpNdrVersion": sonicWirelessSpNdrVersion,
       "sonicWirelessSpAcVersion": sonicWirelessSpAcVersion,
       "sonicWirelessApNumber": sonicWirelessApNumber,
       "sonicWirelessApTable": sonicWirelessApTable,
       "sonicWirelessApEntry": sonicWirelessApEntry,
       "sonicApIndex": sonicApIndex,
       "sonicApName": sonicApName,
       "sonicApModel": sonicApModel,
       "sonicApCountryCode": sonicApCountryCode,
       "sonicApRetainSetting": sonicApRetainSetting,
       "sonicApRfManagement": sonicApRfManagement,
       "sonicApInterface": sonicApInterface,
       "sonicApIpAddr": sonicApIpAddr,
       "sonicApNetMask": sonicApNetMask,
       "sonicApPhysicalAddress": sonicApPhysicalAddress,
       "sonicApMgmt": sonicApMgmt,
       "sonicApStatus": sonicApStatus,
       "sonicApProfile": sonicApProfile,
       "sonicApUpTime": sonicApUpTime,
       "sonicApRadio0Bssid": sonicApRadio0Bssid,
       "sonicApRadio0SSID": sonicApRadio0SSID,
       "sonicApRadio0Enable": sonicApRadio0Enable,
       "sonicApRadio0Status": sonicApRadio0Status,
       "sonicApRadio0Mode": sonicApRadio0Mode,
       "sonicApRadio0ChannelWidth": sonicApRadio0ChannelWidth,
       "sonicApRadio0Channel": sonicApRadio0Channel,
       "sonicApRadio0ShortGuardInt": sonicApRadio0ShortGuardInt,
       "sonicApRadio0Aggregation": sonicApRadio0Aggregation,
       "sonicApRadio0Mimo": sonicApRadio0Mimo,
       "sonicApRadio0AuthType": sonicApRadio0AuthType,
       "sonicApRadio0WpaCipher": sonicApRadio0WpaCipher,
       "sonicApRadio0WpaPsk": sonicApRadio0WpaPsk,
       "sonicApRadio0Acl": sonicApRadio0Acl,
       "sonicApRadio0BroadcastSsid": sonicApRadio0BroadcastSsid,
       "sonicApRadio0TxPowerLevel": sonicApRadio0TxPowerLevel,
       "sonicApRadio0StaTimeout": sonicApRadio0StaTimeout,
       "sonicApRadio1Bssid": sonicApRadio1Bssid,
       "sonicApRadio1SSID": sonicApRadio1SSID,
       "sonicApRadio1Enable": sonicApRadio1Enable,
       "sonicApRadio1Status": sonicApRadio1Status,
       "sonicApRadio1Mode": sonicApRadio1Mode,
       "sonicApRadio1ChannelWidth": sonicApRadio1ChannelWidth,
       "sonicApRadio1Channel": sonicApRadio1Channel,
       "sonicApRadio1ShortGuardInt": sonicApRadio1ShortGuardInt,
       "sonicApRadio1Aggregation": sonicApRadio1Aggregation,
       "sonicApRadio1Mimo": sonicApRadio1Mimo,
       "sonicApRadio1AuthType": sonicApRadio1AuthType,
       "sonicApRadio1WpaCipher": sonicApRadio1WpaCipher,
       "sonicApRadio1WpaPsk": sonicApRadio1WpaPsk,
       "sonicApRadio1Acl": sonicApRadio1Acl,
       "sonicApRadio1BroadcastSsid": sonicApRadio1BroadcastSsid,
       "sonicApRadio1TxPowerLevel": sonicApRadio1TxPowerLevel,
       "sonicApRadio1StaTimeout": sonicApRadio1StaTimeout,
       "sonicApRadiusServerIp1": sonicApRadiusServerIp1,
       "sonicApRadiusServerPort1": sonicApRadiusServerPort1,
       "sonicApRadiusServerSecret1": sonicApRadiusServerSecret1,
       "sonicApRadiusServerIp2": sonicApRadiusServerIp2,
       "sonicApRadiusServerPort2": sonicApRadiusServerPort2,
       "sonicApRadiusServerSecret2": sonicApRadiusServerSecret2,
       "sonicWirelessVapTable": sonicWirelessVapTable,
       "sonicWirelessVapEntry": sonicWirelessVapEntry,
       "sonicWirelessVapIndex": sonicWirelessVapIndex,
       "sonicWirelessVapName": sonicWirelessVapName,
       "sonicWirelessVapStatus": sonicWirelessVapStatus,
       "sonicWirelessVapSsid": sonicWirelessVapSsid,
       "sonicWirelessVapBroadcastSsid": sonicWirelessVapBroadcastSsid,
       "sonicWirelessVapVlanId": sonicWirelessVapVlanId,
       "sonicWirelessVapAuthentication": sonicWirelessVapAuthentication,
       "sonicWirelessVapCipher": sonicWirelessVapCipher,
       "sonicWirelessVapPassPhrase": sonicWirelessVapPassPhrase,
       "sonicWirelessVapRadiusServerIp1": sonicWirelessVapRadiusServerIp1,
       "sonicWirelessVapRadiusServerPort1": sonicWirelessVapRadiusServerPort1,
       "sonicWirelessVapRadiusServerSecret1": sonicWirelessVapRadiusServerSecret1,
       "sonicWirelessVapRadiusServerIp2": sonicWirelessVapRadiusServerIp2,
       "sonicWirelessVapRadiusServerPort2": sonicWirelessVapRadiusServerPort2,
       "sonicWirelessVapRadiusServerSecret2": sonicWirelessVapRadiusServerSecret2,
       "sonicWirelessVapReference": sonicWirelessVapReference,
       "sonicWirelessVapMaxClient": sonicWirelessVapMaxClient,
       "sonicWirelessVapCurClient": sonicWirelessVapCurClient,
       "sonicWirelessStaTable": sonicWirelessStaTable,
       "sonicWirelessStaEntry": sonicWirelessStaEntry,
       "sonicStaPhysAddress": sonicStaPhysAddress,
       "sonicStaApName": sonicStaApName,
       "sonicStaChannel": sonicStaChannel,
       "sonicStaAid": sonicStaAid,
       "sonicStaIpAddress": sonicStaIpAddress,
       "sonicStaStatus": sonicStaStatus,
       "sonicStaRadioType": sonicStaRadioType,
       "sonicStaSsid": sonicStaSsid,
       "sonicStaVlanId": sonicStaVlanId,
       "sonicStaConnRate": sonicStaConnRate,
       "sonicStaTxRate": sonicStaTxRate,
       "sonicStaSignalStrength": sonicStaSignalStrength,
       "sonicStaAssociations": sonicStaAssociations,
       "sonicStaDisassociations": sonicStaDisassociations,
       "sonicStaReassociations": sonicStaReassociations,
       "sonicStaAuthentications": sonicStaAuthentications,
       "sonicStaDeauthentications": sonicStaDeauthentications,
       "sonicStaDiscardPkts": sonicStaDiscardPkts,
       "sonicStaGoodPktsRx": sonicStaGoodPktsRx,
       "sonicStaBadPktsRx": sonicStaBadPktsRx,
       "sonicStaGoodBytesRx": sonicStaGoodBytesRx,
       "sonicStaMgmtPktsRx": sonicStaMgmtPktsRx,
       "sonicStaCtrlPktsRx": sonicStaCtrlPktsRx,
       "sonicStaDataPktsRx": sonicStaDataPktsRx,
       "sonicStaGoodPktsTx": sonicStaGoodPktsTx,
       "sonicStaBadPktsTx": sonicStaBadPktsTx,
       "sonicStaGoodBytesTx": sonicStaGoodBytesTx,
       "sonicStaMgmtPktsTx": sonicStaMgmtPktsTx,
       "sonicStaCtrlPktsTx": sonicStaCtrlPktsTx,
       "sonicStaDataPktsTx": sonicStaDataPktsTx,
       "sonicStaConnSta": sonicStaConnSta,
       "sonicwallFwZoneStats": sonicwallFwZoneStats,
       "sonicwallFwZoneTables": sonicwallFwZoneTables,
       "sonicwallFwZoneTable": sonicwallFwZoneTable,
       "sonicwallFwZoneEntry": sonicwallFwZoneEntry,
       "sonicZoneName": sonicZoneName,
       "sonicZoneSecurity": sonicZoneSecurity,
       "sonicZoneInterfaces": sonicZoneInterfaces,
       "sonicZoneIfTrust": sonicZoneIfTrust,
       "sonicZoneCFS": sonicZoneCFS,
       "sonicZoneClientAv": sonicZoneClientAv,
       "sonicZoneClientCf": sonicZoneClientCf,
       "sonicZoneGwAv": sonicZoneGwAv,
       "sonicZoneAntiSpyware": sonicZoneAntiSpyware,
       "sonicZoneIps": sonicZoneIps,
       "sonicZoneAppControl": sonicZoneAppControl,
       "sonicZoneSslControl": sonicZoneSslControl,
       "sonicZoneSslvpnAccess": sonicZoneSslvpnAccess}
)
