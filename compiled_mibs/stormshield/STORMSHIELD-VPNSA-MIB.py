# SNMP MIB module (STORMSHIELD-VPNSA-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\stormshield\STORMSHIELD-VPNSA-MIB

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")

(snsVPN,) = mibBuilder.importSymbols(
    "STORMSHIELD-VPN-MIB",
    "snsVPN")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_SnsVPNSATable_Object = MibTable
snsVPNSATable = _SnsVPNSATable_Object(
    (1, 3, 6, 1, 4, 1, 11256, 1, 1, 1)
)
if mibBuilder.loadTexts:
    snsVPNSATable.setStatus("current")
_SnsVPNSAEntry_Object = MibTableRow
snsVPNSAEntry = _SnsVPNSAEntry_Object(
    (1, 3, 6, 1, 4, 1, 11256, 1, 1, 1, 1)
)
snsVPNSAEntry.setIndexNames(
    (0, "STORMSHIELD-VPNSA-MIB", "snsVPNSAIndex"),
)
if mibBuilder.loadTexts:
    snsVPNSAEntry.setStatus("current")


class _SnsVPNSAIndex_Type(Integer32):
    """Custom type snsVPNSAIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_SnsVPNSAIndex_Type.__name__ = "Integer32"
_SnsVPNSAIndex_Object = MibTableColumn
snsVPNSAIndex = _SnsVPNSAIndex_Object(
    (1, 3, 6, 1, 4, 1, 11256, 1, 1, 1, 1, 1),
    _SnsVPNSAIndex_Type()
)
snsVPNSAIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snsVPNSAIndex.setStatus("current")
_SnsVPNSARulename_Type = DisplayString
_SnsVPNSARulename_Object = MibTableColumn
snsVPNSARulename = _SnsVPNSARulename_Object(
    (1, 3, 6, 1, 4, 1, 11256, 1, 1, 1, 1, 2),
    _SnsVPNSARulename_Type()
)
snsVPNSARulename.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snsVPNSARulename.setStatus("current")


class _SnsVPNSAIKEIndex_Type(Integer32):
    """Custom type snsVPNSAIKEIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_SnsVPNSAIKEIndex_Type.__name__ = "Integer32"
_SnsVPNSAIKEIndex_Object = MibTableColumn
snsVPNSAIKEIndex = _SnsVPNSAIKEIndex_Object(
    (1, 3, 6, 1, 4, 1, 11256, 1, 1, 1, 1, 3),
    _SnsVPNSAIKEIndex_Type()
)
snsVPNSAIKEIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snsVPNSAIKEIndex.setStatus("current")
_SnsVPNSAIKERulename_Type = DisplayString
_SnsVPNSAIKERulename_Object = MibTableColumn
snsVPNSAIKERulename = _SnsVPNSAIKERulename_Object(
    (1, 3, 6, 1, 4, 1, 11256, 1, 1, 1, 1, 4),
    _SnsVPNSAIKERulename_Type()
)
snsVPNSAIKERulename.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snsVPNSAIKERulename.setStatus("current")
_SnsVPNSAIPSrc_Type = DisplayString
_SnsVPNSAIPSrc_Object = MibTableColumn
snsVPNSAIPSrc = _SnsVPNSAIPSrc_Object(
    (1, 3, 6, 1, 4, 1, 11256, 1, 1, 1, 1, 5),
    _SnsVPNSAIPSrc_Type()
)
snsVPNSAIPSrc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snsVPNSAIPSrc.setStatus("current")
_SnsVPNSAIPDst_Type = DisplayString
_SnsVPNSAIPDst_Object = MibTableColumn
snsVPNSAIPDst = _SnsVPNSAIPDst_Object(
    (1, 3, 6, 1, 4, 1, 11256, 1, 1, 1, 1, 6),
    _SnsVPNSAIPDst_Type()
)
snsVPNSAIPDst.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snsVPNSAIPDst.setStatus("current")


class _SnsVPNSAType_Type(Integer32):
    """Custom type snsVPNSAType based on Integer32"""
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
        *(("unspec", 0),
          ("unknown", 1),
          ("ah", 2),
          ("esp", 3),
          ("rsvp", 4),
          ("ospfv2", 5),
          ("ripv2", 6),
          ("mip", 7),
          ("ipcomp", 8))
    )


_SnsVPNSAType_Type.__name__ = "Integer32"
_SnsVPNSAType_Object = MibTableColumn
snsVPNSAType = _SnsVPNSAType_Object(
    (1, 3, 6, 1, 4, 1, 11256, 1, 1, 1, 1, 7),
    _SnsVPNSAType_Type()
)
snsVPNSAType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snsVPNSAType.setStatus("current")
_SnsVPNSAMode_Type = DisplayString
_SnsVPNSAMode_Object = MibTableColumn
snsVPNSAMode = _SnsVPNSAMode_Object(
    (1, 3, 6, 1, 4, 1, 11256, 1, 1, 1, 1, 8),
    _SnsVPNSAMode_Type()
)
snsVPNSAMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snsVPNSAMode.setStatus("current")


class _SnsVPNSAEncap_Type(Integer32):
    """Custom type snsVPNSAEncap based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("yes", 1))
    )


_SnsVPNSAEncap_Type.__name__ = "Integer32"
_SnsVPNSAEncap_Object = MibTableColumn
snsVPNSAEncap = _SnsVPNSAEncap_Object(
    (1, 3, 6, 1, 4, 1, 11256, 1, 1, 1, 1, 9),
    _SnsVPNSAEncap_Type()
)
snsVPNSAEncap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snsVPNSAEncap.setStatus("current")


class _SnsVPNSAEsn_Type(Integer32):
    """Custom type snsVPNSAEsn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("yes", 1))
    )


_SnsVPNSAEsn_Type.__name__ = "Integer32"
_SnsVPNSAEsn_Object = MibTableColumn
snsVPNSAEsn = _SnsVPNSAEsn_Object(
    (1, 3, 6, 1, 4, 1, 11256, 1, 1, 1, 1, 10),
    _SnsVPNSAEsn_Type()
)
snsVPNSAEsn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snsVPNSAEsn.setStatus("current")
_SnsVPNSASpi_Type = Unsigned32
_SnsVPNSASpi_Object = MibTableColumn
snsVPNSASpi = _SnsVPNSASpi_Object(
    (1, 3, 6, 1, 4, 1, 11256, 1, 1, 1, 1, 11),
    _SnsVPNSASpi_Type()
)
snsVPNSASpi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snsVPNSASpi.setStatus("current")
_SnsVPNSAPeerSpi_Type = Unsigned32
_SnsVPNSAPeerSpi_Object = MibTableColumn
snsVPNSAPeerSpi = _SnsVPNSAPeerSpi_Object(
    (1, 3, 6, 1, 4, 1, 11256, 1, 1, 1, 1, 12),
    _SnsVPNSAPeerSpi_Type()
)
snsVPNSAPeerSpi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snsVPNSAPeerSpi.setStatus("current")
_SnsVPNSAReqID_Type = Integer32
_SnsVPNSAReqID_Object = MibTableColumn
snsVPNSAReqID = _SnsVPNSAReqID_Object(
    (1, 3, 6, 1, 4, 1, 11256, 1, 1, 1, 1, 13),
    _SnsVPNSAReqID_Type()
)
snsVPNSAReqID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snsVPNSAReqID.setStatus("current")
_SnsVPNSAEnc_Type = DisplayString
_SnsVPNSAEnc_Object = MibTableColumn
snsVPNSAEnc = _SnsVPNSAEnc_Object(
    (1, 3, 6, 1, 4, 1, 11256, 1, 1, 1, 1, 14),
    _SnsVPNSAEnc_Type()
)
snsVPNSAEnc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snsVPNSAEnc.setStatus("current")
_SnsVPNSAAuth_Type = DisplayString
_SnsVPNSAAuth_Object = MibTableColumn
snsVPNSAAuth = _SnsVPNSAAuth_Object(
    (1, 3, 6, 1, 4, 1, 11256, 1, 1, 1, 1, 15),
    _SnsVPNSAAuth_Type()
)
snsVPNSAAuth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snsVPNSAAuth.setStatus("current")
_SnsVPNSAPrf_Type = DisplayString
_SnsVPNSAPrf_Object = MibTableColumn
snsVPNSAPrf = _SnsVPNSAPrf_Object(
    (1, 3, 6, 1, 4, 1, 11256, 1, 1, 1, 1, 16),
    _SnsVPNSAPrf_Type()
)
snsVPNSAPrf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snsVPNSAPrf.setStatus("current")
_SnsVPNSAPfs_Type = DisplayString
_SnsVPNSAPfs_Object = MibTableColumn
snsVPNSAPfs = _SnsVPNSAPfs_Object(
    (1, 3, 6, 1, 4, 1, 11256, 1, 1, 1, 1, 17),
    _SnsVPNSAPfs_Type()
)
snsVPNSAPfs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snsVPNSAPfs.setStatus("current")
_SnsVPNSAState_Type = DisplayString
_SnsVPNSAState_Object = MibTableColumn
snsVPNSAState = _SnsVPNSAState_Object(
    (1, 3, 6, 1, 4, 1, 11256, 1, 1, 1, 1, 18),
    _SnsVPNSAState_Type()
)
snsVPNSAState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snsVPNSAState.setStatus("current")
_SnsVPNSABytesIn_Type = Counter64
_SnsVPNSABytesIn_Object = MibTableColumn
snsVPNSABytesIn = _SnsVPNSABytesIn_Object(
    (1, 3, 6, 1, 4, 1, 11256, 1, 1, 1, 1, 19),
    _SnsVPNSABytesIn_Type()
)
snsVPNSABytesIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snsVPNSABytesIn.setStatus("current")
_SnsVPNSABytesOut_Type = Counter64
_SnsVPNSABytesOut_Object = MibTableColumn
snsVPNSABytesOut = _SnsVPNSABytesOut_Object(
    (1, 3, 6, 1, 4, 1, 11256, 1, 1, 1, 1, 20),
    _SnsVPNSABytesOut_Type()
)
snsVPNSABytesOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snsVPNSABytesOut.setStatus("current")
_SnsVPNSAPacketsIn_Type = Counter64
_SnsVPNSAPacketsIn_Object = MibTableColumn
snsVPNSAPacketsIn = _SnsVPNSAPacketsIn_Object(
    (1, 3, 6, 1, 4, 1, 11256, 1, 1, 1, 1, 21),
    _SnsVPNSAPacketsIn_Type()
)
snsVPNSAPacketsIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snsVPNSAPacketsIn.setStatus("current")
_SnsVPNSAPacketsOut_Type = Counter64
_SnsVPNSAPacketsOut_Object = MibTableColumn
snsVPNSAPacketsOut = _SnsVPNSAPacketsOut_Object(
    (1, 3, 6, 1, 4, 1, 11256, 1, 1, 1, 1, 22),
    _SnsVPNSAPacketsOut_Type()
)
snsVPNSAPacketsOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snsVPNSAPacketsOut.setStatus("current")
_SnsVPNSALifetime_Type = Counter64
_SnsVPNSALifetime_Object = MibTableColumn
snsVPNSALifetime = _SnsVPNSALifetime_Object(
    (1, 3, 6, 1, 4, 1, 11256, 1, 1, 1, 1, 23),
    _SnsVPNSALifetime_Type()
)
snsVPNSALifetime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snsVPNSALifetime.setStatus("current")
_SnsVPNSAMaxLifetime_Type = Counter64
_SnsVPNSAMaxLifetime_Object = MibTableColumn
snsVPNSAMaxLifetime = _SnsVPNSAMaxLifetime_Object(
    (1, 3, 6, 1, 4, 1, 11256, 1, 1, 1, 1, 24),
    _SnsVPNSAMaxLifetime_Type()
)
snsVPNSAMaxLifetime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snsVPNSAMaxLifetime.setStatus("current")
_SnsVPNSAGlobal_Type = Integer32
_SnsVPNSAGlobal_Object = MibTableColumn
snsVPNSAGlobal = _SnsVPNSAGlobal_Object(
    (1, 3, 6, 1, 4, 1, 11256, 1, 1, 1, 1, 25),
    _SnsVPNSAGlobal_Type()
)
snsVPNSAGlobal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snsVPNSAGlobal.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "STORMSHIELD-VPNSA-MIB",
    **{"snsVPNSATable": snsVPNSATable,
       "snsVPNSAEntry": snsVPNSAEntry,
       "snsVPNSAIndex": snsVPNSAIndex,
       "snsVPNSARulename": snsVPNSARulename,
       "snsVPNSAIKEIndex": snsVPNSAIKEIndex,
       "snsVPNSAIKERulename": snsVPNSAIKERulename,
       "snsVPNSAIPSrc": snsVPNSAIPSrc,
       "snsVPNSAIPDst": snsVPNSAIPDst,
       "snsVPNSAType": snsVPNSAType,
       "snsVPNSAMode": snsVPNSAMode,
       "snsVPNSAEncap": snsVPNSAEncap,
       "snsVPNSAEsn": snsVPNSAEsn,
       "snsVPNSASpi": snsVPNSASpi,
       "snsVPNSAPeerSpi": snsVPNSAPeerSpi,
       "snsVPNSAReqID": snsVPNSAReqID,
       "snsVPNSAEnc": snsVPNSAEnc,
       "snsVPNSAAuth": snsVPNSAAuth,
       "snsVPNSAPrf": snsVPNSAPrf,
       "snsVPNSAPfs": snsVPNSAPfs,
       "snsVPNSAState": snsVPNSAState,
       "snsVPNSABytesIn": snsVPNSABytesIn,
       "snsVPNSABytesOut": snsVPNSABytesOut,
       "snsVPNSAPacketsIn": snsVPNSAPacketsIn,
       "snsVPNSAPacketsOut": snsVPNSAPacketsOut,
       "snsVPNSALifetime": snsVPNSALifetime,
       "snsVPNSAMaxLifetime": snsVPNSAMaxLifetime,
       "snsVPNSAGlobal": snsVPNSAGlobal}
)
