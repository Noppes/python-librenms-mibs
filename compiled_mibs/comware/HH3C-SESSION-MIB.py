# SNMP MIB module (HH3C-SESSION-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\comware\HH3C-SESSION-MIB

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

(hh3cCommon,) = mibBuilder.importSymbols(
    "HH3C-OID-MIB",
    "hh3cCommon")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

hh3cSession = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 149)
)
if mibBuilder.loadTexts:
    hh3cSession.setRevisions(
        ("2019-11-11 14:27",
         "2019-07-25 11:05",
         "2018-05-16 11:05",
         "2016-12-25 11:05",
         "2014-10-14 18:30",
         "2014-07-15 15:30",
         "2013-12-20 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Hh3cSessionTables_ObjectIdentity = ObjectIdentity
hh3cSessionTables = _Hh3cSessionTables_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 149, 1)
)
_Hh3cSessionStatTable_Object = MibTable
hh3cSessionStatTable = _Hh3cSessionStatTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 149, 1, 1)
)
if mibBuilder.loadTexts:
    hh3cSessionStatTable.setStatus("current")
_Hh3cSessionStatEntry_Object = MibTableRow
hh3cSessionStatEntry = _Hh3cSessionStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 149, 1, 1, 1)
)
hh3cSessionStatEntry.setIndexNames(
    (0, "HH3C-SESSION-MIB", "hh3cSessionStatChassis"),
    (0, "HH3C-SESSION-MIB", "hh3cSessionStatSlot"),
    (0, "HH3C-SESSION-MIB", "hh3cSessionStatCPUID"),
)
if mibBuilder.loadTexts:
    hh3cSessionStatEntry.setStatus("current")


class _Hh3cSessionStatChassis_Type(Unsigned32):
    """Custom type hh3cSessionStatChassis based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65534),
    )


_Hh3cSessionStatChassis_Type.__name__ = "Unsigned32"
_Hh3cSessionStatChassis_Object = MibTableColumn
hh3cSessionStatChassis = _Hh3cSessionStatChassis_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 149, 1, 1, 1, 1),
    _Hh3cSessionStatChassis_Type()
)
hh3cSessionStatChassis.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cSessionStatChassis.setStatus("current")


class _Hh3cSessionStatSlot_Type(Unsigned32):
    """Custom type hh3cSessionStatSlot based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65534),
    )


_Hh3cSessionStatSlot_Type.__name__ = "Unsigned32"
_Hh3cSessionStatSlot_Object = MibTableColumn
hh3cSessionStatSlot = _Hh3cSessionStatSlot_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 149, 1, 1, 1, 2),
    _Hh3cSessionStatSlot_Type()
)
hh3cSessionStatSlot.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cSessionStatSlot.setStatus("current")


class _Hh3cSessionStatCPUID_Type(Unsigned32):
    """Custom type hh3cSessionStatCPUID based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_Hh3cSessionStatCPUID_Type.__name__ = "Unsigned32"
_Hh3cSessionStatCPUID_Object = MibTableColumn
hh3cSessionStatCPUID = _Hh3cSessionStatCPUID_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 149, 1, 1, 1, 3),
    _Hh3cSessionStatCPUID_Type()
)
hh3cSessionStatCPUID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cSessionStatCPUID.setStatus("current")
_Hh3cSessionStatCount_Type = Unsigned32
_Hh3cSessionStatCount_Object = MibTableColumn
hh3cSessionStatCount = _Hh3cSessionStatCount_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 149, 1, 1, 1, 4),
    _Hh3cSessionStatCount_Type()
)
hh3cSessionStatCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cSessionStatCount.setStatus("current")
_Hh3cSessionStatCreateRate_Type = Unsigned32
_Hh3cSessionStatCreateRate_Object = MibTableColumn
hh3cSessionStatCreateRate = _Hh3cSessionStatCreateRate_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 149, 1, 1, 1, 5),
    _Hh3cSessionStatCreateRate_Type()
)
hh3cSessionStatCreateRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cSessionStatCreateRate.setStatus("current")
_Hh3cSessionStatTCPCount_Type = Unsigned32
_Hh3cSessionStatTCPCount_Object = MibTableColumn
hh3cSessionStatTCPCount = _Hh3cSessionStatTCPCount_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 149, 1, 1, 1, 6),
    _Hh3cSessionStatTCPCount_Type()
)
hh3cSessionStatTCPCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cSessionStatTCPCount.setStatus("current")
_Hh3cSessionStatUDPCount_Type = Unsigned32
_Hh3cSessionStatUDPCount_Object = MibTableColumn
hh3cSessionStatUDPCount = _Hh3cSessionStatUDPCount_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 149, 1, 1, 1, 7),
    _Hh3cSessionStatUDPCount_Type()
)
hh3cSessionStatUDPCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cSessionStatUDPCount.setStatus("current")
_Hh3cSessionStatOtherCount_Type = Unsigned32
_Hh3cSessionStatOtherCount_Object = MibTableColumn
hh3cSessionStatOtherCount = _Hh3cSessionStatOtherCount_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 149, 1, 1, 1, 8),
    _Hh3cSessionStatOtherCount_Type()
)
hh3cSessionStatOtherCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cSessionStatOtherCount.setStatus("current")
_Hh3cSessionStatTCPCreateRate_Type = Unsigned32
_Hh3cSessionStatTCPCreateRate_Object = MibTableColumn
hh3cSessionStatTCPCreateRate = _Hh3cSessionStatTCPCreateRate_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 149, 1, 1, 1, 9),
    _Hh3cSessionStatTCPCreateRate_Type()
)
hh3cSessionStatTCPCreateRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cSessionStatTCPCreateRate.setStatus("current")
_Hh3cSessionStatUDPCreateRate_Type = Unsigned32
_Hh3cSessionStatUDPCreateRate_Object = MibTableColumn
hh3cSessionStatUDPCreateRate = _Hh3cSessionStatUDPCreateRate_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 149, 1, 1, 1, 10),
    _Hh3cSessionStatUDPCreateRate_Type()
)
hh3cSessionStatUDPCreateRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cSessionStatUDPCreateRate.setStatus("current")
_Hh3cSessionStatOtherCreateRate_Type = Unsigned32
_Hh3cSessionStatOtherCreateRate_Object = MibTableColumn
hh3cSessionStatOtherCreateRate = _Hh3cSessionStatOtherCreateRate_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 149, 1, 1, 1, 11),
    _Hh3cSessionStatOtherCreateRate_Type()
)
hh3cSessionStatOtherCreateRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cSessionStatOtherCreateRate.setStatus("current")
_Hh3cSessionStatTCPTotal_Type = Counter64
_Hh3cSessionStatTCPTotal_Object = MibTableColumn
hh3cSessionStatTCPTotal = _Hh3cSessionStatTCPTotal_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 149, 1, 1, 1, 12),
    _Hh3cSessionStatTCPTotal_Type()
)
hh3cSessionStatTCPTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cSessionStatTCPTotal.setStatus("current")
_Hh3cSessionStatUDPTotal_Type = Counter64
_Hh3cSessionStatUDPTotal_Object = MibTableColumn
hh3cSessionStatUDPTotal = _Hh3cSessionStatUDPTotal_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 149, 1, 1, 1, 13),
    _Hh3cSessionStatUDPTotal_Type()
)
hh3cSessionStatUDPTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cSessionStatUDPTotal.setStatus("current")
_Hh3cSessionStatOtherTotal_Type = Counter64
_Hh3cSessionStatOtherTotal_Object = MibTableColumn
hh3cSessionStatOtherTotal = _Hh3cSessionStatOtherTotal_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 149, 1, 1, 1, 14),
    _Hh3cSessionStatOtherTotal_Type()
)
hh3cSessionStatOtherTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cSessionStatOtherTotal.setStatus("current")
_Hh3cSessionStatDNSCount_Type = Unsigned32
_Hh3cSessionStatDNSCount_Object = MibTableColumn
hh3cSessionStatDNSCount = _Hh3cSessionStatDNSCount_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 149, 1, 1, 1, 15),
    _Hh3cSessionStatDNSCount_Type()
)
hh3cSessionStatDNSCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cSessionStatDNSCount.setStatus("current")
_Hh3cSessionStatFTPCount_Type = Unsigned32
_Hh3cSessionStatFTPCount_Object = MibTableColumn
hh3cSessionStatFTPCount = _Hh3cSessionStatFTPCount_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 149, 1, 1, 1, 16),
    _Hh3cSessionStatFTPCount_Type()
)
hh3cSessionStatFTPCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cSessionStatFTPCount.setStatus("current")
_Hh3cSessionStatGTPCount_Type = Unsigned32
_Hh3cSessionStatGTPCount_Object = MibTableColumn
hh3cSessionStatGTPCount = _Hh3cSessionStatGTPCount_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 149, 1, 1, 1, 17),
    _Hh3cSessionStatGTPCount_Type()
)
hh3cSessionStatGTPCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cSessionStatGTPCount.setStatus("current")
_Hh3cSessionStatH323Count_Type = Unsigned32
_Hh3cSessionStatH323Count_Object = MibTableColumn
hh3cSessionStatH323Count = _Hh3cSessionStatH323Count_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 149, 1, 1, 1, 18),
    _Hh3cSessionStatH323Count_Type()
)
hh3cSessionStatH323Count.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cSessionStatH323Count.setStatus("current")
_Hh3cSessionStatHTTPCount_Type = Unsigned32
_Hh3cSessionStatHTTPCount_Object = MibTableColumn
hh3cSessionStatHTTPCount = _Hh3cSessionStatHTTPCount_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 149, 1, 1, 1, 19),
    _Hh3cSessionStatHTTPCount_Type()
)
hh3cSessionStatHTTPCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cSessionStatHTTPCount.setStatus("current")
_Hh3cSessionStatILSCount_Type = Unsigned32
_Hh3cSessionStatILSCount_Object = MibTableColumn
hh3cSessionStatILSCount = _Hh3cSessionStatILSCount_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 149, 1, 1, 1, 20),
    _Hh3cSessionStatILSCount_Type()
)
hh3cSessionStatILSCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cSessionStatILSCount.setStatus("current")
_Hh3cSessionStatMGCPCount_Type = Unsigned32
_Hh3cSessionStatMGCPCount_Object = MibTableColumn
hh3cSessionStatMGCPCount = _Hh3cSessionStatMGCPCount_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 149, 1, 1, 1, 21),
    _Hh3cSessionStatMGCPCount_Type()
)
hh3cSessionStatMGCPCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cSessionStatMGCPCount.setStatus("current")
_Hh3cSessionStatNBTCount_Type = Unsigned32
_Hh3cSessionStatNBTCount_Object = MibTableColumn
hh3cSessionStatNBTCount = _Hh3cSessionStatNBTCount_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 149, 1, 1, 1, 22),
    _Hh3cSessionStatNBTCount_Type()
)
hh3cSessionStatNBTCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cSessionStatNBTCount.setStatus("current")
_Hh3cSessionStatPPTPCount_Type = Unsigned32
_Hh3cSessionStatPPTPCount_Object = MibTableColumn
hh3cSessionStatPPTPCount = _Hh3cSessionStatPPTPCount_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 149, 1, 1, 1, 23),
    _Hh3cSessionStatPPTPCount_Type()
)
hh3cSessionStatPPTPCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cSessionStatPPTPCount.setStatus("current")
_Hh3cSessionStatRSHCount_Type = Unsigned32
_Hh3cSessionStatRSHCount_Object = MibTableColumn
hh3cSessionStatRSHCount = _Hh3cSessionStatRSHCount_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 149, 1, 1, 1, 24),
    _Hh3cSessionStatRSHCount_Type()
)
hh3cSessionStatRSHCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cSessionStatRSHCount.setStatus("current")
_Hh3cSessionStatRTSPCount_Type = Unsigned32
_Hh3cSessionStatRTSPCount_Object = MibTableColumn
hh3cSessionStatRTSPCount = _Hh3cSessionStatRTSPCount_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 149, 1, 1, 1, 25),
    _Hh3cSessionStatRTSPCount_Type()
)
hh3cSessionStatRTSPCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cSessionStatRTSPCount.setStatus("current")
_Hh3cSessionStatSCCPCount_Type = Unsigned32
_Hh3cSessionStatSCCPCount_Object = MibTableColumn
hh3cSessionStatSCCPCount = _Hh3cSessionStatSCCPCount_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 149, 1, 1, 1, 26),
    _Hh3cSessionStatSCCPCount_Type()
)
hh3cSessionStatSCCPCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cSessionStatSCCPCount.setStatus("current")
_Hh3cSessionStatSIPCount_Type = Unsigned32
_Hh3cSessionStatSIPCount_Object = MibTableColumn
hh3cSessionStatSIPCount = _Hh3cSessionStatSIPCount_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 149, 1, 1, 1, 27),
    _Hh3cSessionStatSIPCount_Type()
)
hh3cSessionStatSIPCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cSessionStatSIPCount.setStatus("current")
_Hh3cSessionStatSMTPCount_Type = Unsigned32
_Hh3cSessionStatSMTPCount_Object = MibTableColumn
hh3cSessionStatSMTPCount = _Hh3cSessionStatSMTPCount_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 149, 1, 1, 1, 28),
    _Hh3cSessionStatSMTPCount_Type()
)
hh3cSessionStatSMTPCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cSessionStatSMTPCount.setStatus("current")
_Hh3cSessionStatSQLNETCount_Type = Unsigned32
_Hh3cSessionStatSQLNETCount_Object = MibTableColumn
hh3cSessionStatSQLNETCount = _Hh3cSessionStatSQLNETCount_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 149, 1, 1, 1, 29),
    _Hh3cSessionStatSQLNETCount_Type()
)
hh3cSessionStatSQLNETCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cSessionStatSQLNETCount.setStatus("current")
_Hh3cSessionStatSSHCount_Type = Unsigned32
_Hh3cSessionStatSSHCount_Object = MibTableColumn
hh3cSessionStatSSHCount = _Hh3cSessionStatSSHCount_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 149, 1, 1, 1, 30),
    _Hh3cSessionStatSSHCount_Type()
)
hh3cSessionStatSSHCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cSessionStatSSHCount.setStatus("current")
_Hh3cSessionStatTELNETCount_Type = Unsigned32
_Hh3cSessionStatTELNETCount_Object = MibTableColumn
hh3cSessionStatTELNETCount = _Hh3cSessionStatTELNETCount_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 149, 1, 1, 1, 31),
    _Hh3cSessionStatTELNETCount_Type()
)
hh3cSessionStatTELNETCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cSessionStatTELNETCount.setStatus("current")
_Hh3cSessionStatTFTPCount_Type = Unsigned32
_Hh3cSessionStatTFTPCount_Object = MibTableColumn
hh3cSessionStatTFTPCount = _Hh3cSessionStatTFTPCount_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 149, 1, 1, 1, 32),
    _Hh3cSessionStatTFTPCount_Type()
)
hh3cSessionStatTFTPCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cSessionStatTFTPCount.setStatus("current")
_Hh3cSessionStatXDMCPCount_Type = Unsigned32
_Hh3cSessionStatXDMCPCount_Object = MibTableColumn
hh3cSessionStatXDMCPCount = _Hh3cSessionStatXDMCPCount_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 149, 1, 1, 1, 33),
    _Hh3cSessionStatXDMCPCount_Type()
)
hh3cSessionStatXDMCPCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cSessionStatXDMCPCount.setStatus("current")
_Hh3cSessionEntTable_Object = MibTable
hh3cSessionEntTable = _Hh3cSessionEntTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 149, 1, 2)
)
if mibBuilder.loadTexts:
    hh3cSessionEntTable.setStatus("current")
_Hh3cSessionEntEntry_Object = MibTableRow
hh3cSessionEntEntry = _Hh3cSessionEntEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 149, 1, 2, 1)
)
hh3cSessionEntEntry.setIndexNames(
    (0, "HH3C-SESSION-MIB", "hh3cSessionEntIndex"),
)
if mibBuilder.loadTexts:
    hh3cSessionEntEntry.setStatus("current")


class _Hh3cSessionEntIndex_Type(Unsigned32):
    """Custom type hh3cSessionEntIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Hh3cSessionEntIndex_Type.__name__ = "Unsigned32"
_Hh3cSessionEntIndex_Object = MibTableColumn
hh3cSessionEntIndex = _Hh3cSessionEntIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 149, 1, 2, 1, 1),
    _Hh3cSessionEntIndex_Type()
)
hh3cSessionEntIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cSessionEntIndex.setStatus("current")
_Hh3cSessionEntCount_Type = Unsigned32
_Hh3cSessionEntCount_Object = MibTableColumn
hh3cSessionEntCount = _Hh3cSessionEntCount_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 149, 1, 2, 1, 2),
    _Hh3cSessionEntCount_Type()
)
hh3cSessionEntCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cSessionEntCount.setStatus("current")
_Hh3cSessionEntCreateRate_Type = Unsigned32
_Hh3cSessionEntCreateRate_Object = MibTableColumn
hh3cSessionEntCreateRate = _Hh3cSessionEntCreateRate_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 149, 1, 2, 1, 3),
    _Hh3cSessionEntCreateRate_Type()
)
hh3cSessionEntCreateRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cSessionEntCreateRate.setStatus("current")
_Hh3cSessionEntTCPCount_Type = Unsigned32
_Hh3cSessionEntTCPCount_Object = MibTableColumn
hh3cSessionEntTCPCount = _Hh3cSessionEntTCPCount_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 149, 1, 2, 1, 4),
    _Hh3cSessionEntTCPCount_Type()
)
hh3cSessionEntTCPCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cSessionEntTCPCount.setStatus("current")
_Hh3cSessionEntUDPCount_Type = Unsigned32
_Hh3cSessionEntUDPCount_Object = MibTableColumn
hh3cSessionEntUDPCount = _Hh3cSessionEntUDPCount_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 149, 1, 2, 1, 5),
    _Hh3cSessionEntUDPCount_Type()
)
hh3cSessionEntUDPCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cSessionEntUDPCount.setStatus("current")
_Hh3cSessionEntOtherCount_Type = Unsigned32
_Hh3cSessionEntOtherCount_Object = MibTableColumn
hh3cSessionEntOtherCount = _Hh3cSessionEntOtherCount_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 149, 1, 2, 1, 6),
    _Hh3cSessionEntOtherCount_Type()
)
hh3cSessionEntOtherCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cSessionEntOtherCount.setStatus("current")
_Hh3cSessionEntTCPCreateRate_Type = Unsigned32
_Hh3cSessionEntTCPCreateRate_Object = MibTableColumn
hh3cSessionEntTCPCreateRate = _Hh3cSessionEntTCPCreateRate_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 149, 1, 2, 1, 7),
    _Hh3cSessionEntTCPCreateRate_Type()
)
hh3cSessionEntTCPCreateRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cSessionEntTCPCreateRate.setStatus("current")
_Hh3cSessionEntUDPCreateRate_Type = Unsigned32
_Hh3cSessionEntUDPCreateRate_Object = MibTableColumn
hh3cSessionEntUDPCreateRate = _Hh3cSessionEntUDPCreateRate_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 149, 1, 2, 1, 8),
    _Hh3cSessionEntUDPCreateRate_Type()
)
hh3cSessionEntUDPCreateRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cSessionEntUDPCreateRate.setStatus("current")
_Hh3cSessionEntOtherCreateRate_Type = Unsigned32
_Hh3cSessionEntOtherCreateRate_Object = MibTableColumn
hh3cSessionEntOtherCreateRate = _Hh3cSessionEntOtherCreateRate_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 149, 1, 2, 1, 9),
    _Hh3cSessionEntOtherCreateRate_Type()
)
hh3cSessionEntOtherCreateRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cSessionEntOtherCreateRate.setStatus("current")
_Hh3cSessionEntTCPTotal_Type = Counter64
_Hh3cSessionEntTCPTotal_Object = MibTableColumn
hh3cSessionEntTCPTotal = _Hh3cSessionEntTCPTotal_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 149, 1, 2, 1, 10),
    _Hh3cSessionEntTCPTotal_Type()
)
hh3cSessionEntTCPTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cSessionEntTCPTotal.setStatus("current")
_Hh3cSessionEntUDPTotal_Type = Counter64
_Hh3cSessionEntUDPTotal_Object = MibTableColumn
hh3cSessionEntUDPTotal = _Hh3cSessionEntUDPTotal_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 149, 1, 2, 1, 11),
    _Hh3cSessionEntUDPTotal_Type()
)
hh3cSessionEntUDPTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cSessionEntUDPTotal.setStatus("current")
_Hh3cSessionEntOtherTotal_Type = Counter64
_Hh3cSessionEntOtherTotal_Object = MibTableColumn
hh3cSessionEntOtherTotal = _Hh3cSessionEntOtherTotal_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 149, 1, 2, 1, 12),
    _Hh3cSessionEntOtherTotal_Type()
)
hh3cSessionEntOtherTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cSessionEntOtherTotal.setStatus("current")
_Hh3cSessionDrvTraps_ObjectIdentity = ObjectIdentity
hh3cSessionDrvTraps = _Hh3cSessionDrvTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 149, 1, 3)
)
_Hh3cSessionDrvTrapPrefix_ObjectIdentity = ObjectIdentity
hh3cSessionDrvTrapPrefix = _Hh3cSessionDrvTrapPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 149, 1, 3, 0)
)
_Hh3cSessionDrvTrapObjects_ObjectIdentity = ObjectIdentity
hh3cSessionDrvTrapObjects = _Hh3cSessionDrvTrapObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 149, 1, 3, 1)
)
_Hh3cSessionDrvNum_Type = Unsigned32
_Hh3cSessionDrvNum_Object = MibScalar
hh3cSessionDrvNum = _Hh3cSessionDrvNum_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 149, 1, 3, 1, 1),
    _Hh3cSessionDrvNum_Type()
)
hh3cSessionDrvNum.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cSessionDrvNum.setStatus("current")
_Hh3cSessionChassis_Type = Unsigned32
_Hh3cSessionChassis_Object = MibScalar
hh3cSessionChassis = _Hh3cSessionChassis_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 149, 1, 3, 1, 2),
    _Hh3cSessionChassis_Type()
)
hh3cSessionChassis.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cSessionChassis.setStatus("current")
_Hh3cSessionSlot_Type = Unsigned32
_Hh3cSessionSlot_Object = MibScalar
hh3cSessionSlot = _Hh3cSessionSlot_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 149, 1, 3, 1, 3),
    _Hh3cSessionSlot_Type()
)
hh3cSessionSlot.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cSessionSlot.setStatus("current")
_Hh3cSessionCpu_Type = Unsigned32
_Hh3cSessionCpu_Object = MibScalar
hh3cSessionCpu = _Hh3cSessionCpu_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 149, 1, 3, 1, 4),
    _Hh3cSessionCpu_Type()
)
hh3cSessionCpu.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cSessionCpu.setStatus("current")
_Hh3cSessionUsage_Type = Unsigned32
_Hh3cSessionUsage_Object = MibScalar
hh3cSessionUsage = _Hh3cSessionUsage_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 149, 1, 3, 1, 5),
    _Hh3cSessionUsage_Type()
)
hh3cSessionUsage.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cSessionUsage.setStatus("current")
_Hh3cSessionThreshold_Type = Unsigned32
_Hh3cSessionThreshold_Object = MibScalar
hh3cSessionThreshold = _Hh3cSessionThreshold_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 149, 1, 3, 1, 6),
    _Hh3cSessionThreshold_Type()
)
hh3cSessionThreshold.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cSessionThreshold.setStatus("current")
_Hh3cSessionMonitor_ObjectIdentity = ObjectIdentity
hh3cSessionMonitor = _Hh3cSessionMonitor_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 149, 1, 4)
)
_Hh3cSessionTrapObjects_ObjectIdentity = ObjectIdentity
hh3cSessionTrapObjects = _Hh3cSessionTrapObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 149, 1, 4, 0)
)
_Hh3cSessionAbruptAlarm_ObjectIdentity = ObjectIdentity
hh3cSessionAbruptAlarm = _Hh3cSessionAbruptAlarm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 149, 1, 4, 1)
)
_Hh3cSessionUsageAbruptVar_Type = Unsigned32
_Hh3cSessionUsageAbruptVar_Object = MibScalar
hh3cSessionUsageAbruptVar = _Hh3cSessionUsageAbruptVar_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 149, 1, 4, 1, 1),
    _Hh3cSessionUsageAbruptVar_Type()
)
hh3cSessionUsageAbruptVar.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cSessionUsageAbruptVar.setStatus("current")
_Hh3cSessionRateAbruptVar_Type = Unsigned32
_Hh3cSessionRateAbruptVar_Object = MibScalar
hh3cSessionRateAbruptVar = _Hh3cSessionRateAbruptVar_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 149, 1, 4, 1, 2),
    _Hh3cSessionRateAbruptVar_Type()
)
hh3cSessionRateAbruptVar.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cSessionRateAbruptVar.setStatus("current")
_Hh3cSessionTryRateAbruptVar_Type = Unsigned32
_Hh3cSessionTryRateAbruptVar_Object = MibScalar
hh3cSessionTryRateAbruptVar = _Hh3cSessionTryRateAbruptVar_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 149, 1, 4, 1, 3),
    _Hh3cSessionTryRateAbruptVar_Type()
)
hh3cSessionTryRateAbruptVar.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cSessionTryRateAbruptVar.setStatus("current")
_Hh3cSessionLastStat_Type = Unsigned32
_Hh3cSessionLastStat_Object = MibScalar
hh3cSessionLastStat = _Hh3cSessionLastStat_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 149, 1, 4, 1, 4),
    _Hh3cSessionLastStat_Type()
)
hh3cSessionLastStat.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cSessionLastStat.setStatus("current")
_Hh3cSessionCurrentStat_Type = Unsigned32
_Hh3cSessionCurrentStat_Object = MibScalar
hh3cSessionCurrentStat = _Hh3cSessionCurrentStat_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 149, 1, 4, 1, 5),
    _Hh3cSessionCurrentStat_Type()
)
hh3cSessionCurrentStat.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cSessionCurrentStat.setStatus("current")

# Managed Objects groups


# Notification objects

hh3cSessionDrvMaxTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 149, 1, 3, 0, 1)
)
hh3cSessionDrvMaxTrap.setObjects(
      *(("HH3C-SESSION-MIB", "hh3cSessionDrvNum"),
        ("HH3C-SESSION-MIB", "hh3cSessionChassis"),
        ("HH3C-SESSION-MIB", "hh3cSessionSlot"),
        ("HH3C-SESSION-MIB", "hh3cSessionCpu"))
)
if mibBuilder.loadTexts:
    hh3cSessionDrvMaxTrap.setStatus(
        "current"
    )

hh3cSessionDrvRecoveryTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 149, 1, 3, 0, 2)
)
hh3cSessionDrvRecoveryTrap.setObjects(
      *(("HH3C-SESSION-MIB", "hh3cSessionChassis"),
        ("HH3C-SESSION-MIB", "hh3cSessionSlot"),
        ("HH3C-SESSION-MIB", "hh3cSessionCpu"))
)
if mibBuilder.loadTexts:
    hh3cSessionDrvRecoveryTrap.setStatus(
        "current"
    )

hh3cSessionThdMaxTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 149, 1, 3, 0, 3)
)
hh3cSessionThdMaxTrap.setObjects(
      *(("HH3C-SESSION-MIB", "hh3cSessionUsage"),
        ("HH3C-SESSION-MIB", "hh3cSessionThreshold"),
        ("HH3C-SESSION-MIB", "hh3cSessionChassis"),
        ("HH3C-SESSION-MIB", "hh3cSessionSlot"),
        ("HH3C-SESSION-MIB", "hh3cSessionCpu"))
)
if mibBuilder.loadTexts:
    hh3cSessionThdMaxTrap.setStatus(
        "current"
    )

hh3cSessionThdRecoveryTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 149, 1, 3, 0, 4)
)
hh3cSessionThdRecoveryTrap.setObjects(
      *(("HH3C-SESSION-MIB", "hh3cSessionUsage"),
        ("HH3C-SESSION-MIB", "hh3cSessionThreshold"),
        ("HH3C-SESSION-MIB", "hh3cSessionChassis"),
        ("HH3C-SESSION-MIB", "hh3cSessionSlot"),
        ("HH3C-SESSION-MIB", "hh3cSessionCpu"))
)
if mibBuilder.loadTexts:
    hh3cSessionThdRecoveryTrap.setStatus(
        "current"
    )

hh3cSessUsageAbruptAlarmTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 149, 1, 4, 0, 1)
)
hh3cSessUsageAbruptAlarmTrap.setObjects(
      *(("HH3C-SESSION-MIB", "hh3cSessionChassis"),
        ("HH3C-SESSION-MIB", "hh3cSessionSlot"),
        ("HH3C-SESSION-MIB", "hh3cSessionCpu"),
        ("HH3C-SESSION-MIB", "hh3cSessionUsageAbruptVar"),
        ("HH3C-SESSION-MIB", "hh3cSessionLastStat"),
        ("HH3C-SESSION-MIB", "hh3cSessionCurrentStat"))
)
if mibBuilder.loadTexts:
    hh3cSessUsageAbruptAlarmTrap.setStatus(
        "current"
    )

hh3cSessRateAbruptAlarmTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 149, 1, 4, 0, 2)
)
hh3cSessRateAbruptAlarmTrap.setObjects(
      *(("HH3C-SESSION-MIB", "hh3cSessionChassis"),
        ("HH3C-SESSION-MIB", "hh3cSessionSlot"),
        ("HH3C-SESSION-MIB", "hh3cSessionCpu"),
        ("HH3C-SESSION-MIB", "hh3cSessionRateAbruptVar"),
        ("HH3C-SESSION-MIB", "hh3cSessionLastStat"),
        ("HH3C-SESSION-MIB", "hh3cSessionCurrentStat"))
)
if mibBuilder.loadTexts:
    hh3cSessRateAbruptAlarmTrap.setStatus(
        "current"
    )

hh3cSessTryRateAbruptAlarmTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 149, 1, 4, 0, 3)
)
hh3cSessTryRateAbruptAlarmTrap.setObjects(
      *(("HH3C-SESSION-MIB", "hh3cSessionChassis"),
        ("HH3C-SESSION-MIB", "hh3cSessionSlot"),
        ("HH3C-SESSION-MIB", "hh3cSessionCpu"),
        ("HH3C-SESSION-MIB", "hh3cSessionTryRateAbruptVar"),
        ("HH3C-SESSION-MIB", "hh3cSessionLastStat"),
        ("HH3C-SESSION-MIB", "hh3cSessionCurrentStat"))
)
if mibBuilder.loadTexts:
    hh3cSessTryRateAbruptAlarmTrap.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HH3C-SESSION-MIB",
    **{"hh3cSession": hh3cSession,
       "hh3cSessionTables": hh3cSessionTables,
       "hh3cSessionStatTable": hh3cSessionStatTable,
       "hh3cSessionStatEntry": hh3cSessionStatEntry,
       "hh3cSessionStatChassis": hh3cSessionStatChassis,
       "hh3cSessionStatSlot": hh3cSessionStatSlot,
       "hh3cSessionStatCPUID": hh3cSessionStatCPUID,
       "hh3cSessionStatCount": hh3cSessionStatCount,
       "hh3cSessionStatCreateRate": hh3cSessionStatCreateRate,
       "hh3cSessionStatTCPCount": hh3cSessionStatTCPCount,
       "hh3cSessionStatUDPCount": hh3cSessionStatUDPCount,
       "hh3cSessionStatOtherCount": hh3cSessionStatOtherCount,
       "hh3cSessionStatTCPCreateRate": hh3cSessionStatTCPCreateRate,
       "hh3cSessionStatUDPCreateRate": hh3cSessionStatUDPCreateRate,
       "hh3cSessionStatOtherCreateRate": hh3cSessionStatOtherCreateRate,
       "hh3cSessionStatTCPTotal": hh3cSessionStatTCPTotal,
       "hh3cSessionStatUDPTotal": hh3cSessionStatUDPTotal,
       "hh3cSessionStatOtherTotal": hh3cSessionStatOtherTotal,
       "hh3cSessionStatDNSCount": hh3cSessionStatDNSCount,
       "hh3cSessionStatFTPCount": hh3cSessionStatFTPCount,
       "hh3cSessionStatGTPCount": hh3cSessionStatGTPCount,
       "hh3cSessionStatH323Count": hh3cSessionStatH323Count,
       "hh3cSessionStatHTTPCount": hh3cSessionStatHTTPCount,
       "hh3cSessionStatILSCount": hh3cSessionStatILSCount,
       "hh3cSessionStatMGCPCount": hh3cSessionStatMGCPCount,
       "hh3cSessionStatNBTCount": hh3cSessionStatNBTCount,
       "hh3cSessionStatPPTPCount": hh3cSessionStatPPTPCount,
       "hh3cSessionStatRSHCount": hh3cSessionStatRSHCount,
       "hh3cSessionStatRTSPCount": hh3cSessionStatRTSPCount,
       "hh3cSessionStatSCCPCount": hh3cSessionStatSCCPCount,
       "hh3cSessionStatSIPCount": hh3cSessionStatSIPCount,
       "hh3cSessionStatSMTPCount": hh3cSessionStatSMTPCount,
       "hh3cSessionStatSQLNETCount": hh3cSessionStatSQLNETCount,
       "hh3cSessionStatSSHCount": hh3cSessionStatSSHCount,
       "hh3cSessionStatTELNETCount": hh3cSessionStatTELNETCount,
       "hh3cSessionStatTFTPCount": hh3cSessionStatTFTPCount,
       "hh3cSessionStatXDMCPCount": hh3cSessionStatXDMCPCount,
       "hh3cSessionEntTable": hh3cSessionEntTable,
       "hh3cSessionEntEntry": hh3cSessionEntEntry,
       "hh3cSessionEntIndex": hh3cSessionEntIndex,
       "hh3cSessionEntCount": hh3cSessionEntCount,
       "hh3cSessionEntCreateRate": hh3cSessionEntCreateRate,
       "hh3cSessionEntTCPCount": hh3cSessionEntTCPCount,
       "hh3cSessionEntUDPCount": hh3cSessionEntUDPCount,
       "hh3cSessionEntOtherCount": hh3cSessionEntOtherCount,
       "hh3cSessionEntTCPCreateRate": hh3cSessionEntTCPCreateRate,
       "hh3cSessionEntUDPCreateRate": hh3cSessionEntUDPCreateRate,
       "hh3cSessionEntOtherCreateRate": hh3cSessionEntOtherCreateRate,
       "hh3cSessionEntTCPTotal": hh3cSessionEntTCPTotal,
       "hh3cSessionEntUDPTotal": hh3cSessionEntUDPTotal,
       "hh3cSessionEntOtherTotal": hh3cSessionEntOtherTotal,
       "hh3cSessionDrvTraps": hh3cSessionDrvTraps,
       "hh3cSessionDrvTrapPrefix": hh3cSessionDrvTrapPrefix,
       "hh3cSessionDrvMaxTrap": hh3cSessionDrvMaxTrap,
       "hh3cSessionDrvRecoveryTrap": hh3cSessionDrvRecoveryTrap,
       "hh3cSessionThdMaxTrap": hh3cSessionThdMaxTrap,
       "hh3cSessionThdRecoveryTrap": hh3cSessionThdRecoveryTrap,
       "hh3cSessionDrvTrapObjects": hh3cSessionDrvTrapObjects,
       "hh3cSessionDrvNum": hh3cSessionDrvNum,
       "hh3cSessionChassis": hh3cSessionChassis,
       "hh3cSessionSlot": hh3cSessionSlot,
       "hh3cSessionCpu": hh3cSessionCpu,
       "hh3cSessionUsage": hh3cSessionUsage,
       "hh3cSessionThreshold": hh3cSessionThreshold,
       "hh3cSessionMonitor": hh3cSessionMonitor,
       "hh3cSessionTrapObjects": hh3cSessionTrapObjects,
       "hh3cSessUsageAbruptAlarmTrap": hh3cSessUsageAbruptAlarmTrap,
       "hh3cSessRateAbruptAlarmTrap": hh3cSessRateAbruptAlarmTrap,
       "hh3cSessTryRateAbruptAlarmTrap": hh3cSessTryRateAbruptAlarmTrap,
       "hh3cSessionAbruptAlarm": hh3cSessionAbruptAlarm,
       "hh3cSessionUsageAbruptVar": hh3cSessionUsageAbruptVar,
       "hh3cSessionRateAbruptVar": hh3cSessionRateAbruptVar,
       "hh3cSessionTryRateAbruptVar": hh3cSessionTryRateAbruptVar,
       "hh3cSessionLastStat": hh3cSessionLastStat,
       "hh3cSessionCurrentStat": hh3cSessionCurrentStat}
)
