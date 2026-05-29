# SNMP MIB module (STORMSHIELD-VPNSP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\stormshield\STORMSHIELD-VPNSP-MIB

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

_SnsVPNSPTable_Object = MibTable
snsVPNSPTable = _SnsVPNSPTable_Object(
    (1, 3, 6, 1, 4, 1, 11256, 1, 1, 3)
)
if mibBuilder.loadTexts:
    snsVPNSPTable.setStatus("current")
_SnsVPNSPEntry_Object = MibTableRow
snsVPNSPEntry = _SnsVPNSPEntry_Object(
    (1, 3, 6, 1, 4, 1, 11256, 1, 1, 3, 1)
)
snsVPNSPEntry.setIndexNames(
    (0, "STORMSHIELD-VPNSP-MIB", "snsVPNSPIndex"),
)
if mibBuilder.loadTexts:
    snsVPNSPEntry.setStatus("current")


class _SnsVPNSPIndex_Type(Integer32):
    """Custom type snsVPNSPIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_SnsVPNSPIndex_Type.__name__ = "Integer32"
_SnsVPNSPIndex_Object = MibTableColumn
snsVPNSPIndex = _SnsVPNSPIndex_Object(
    (1, 3, 6, 1, 4, 1, 11256, 1, 1, 3, 1, 1),
    _SnsVPNSPIndex_Type()
)
snsVPNSPIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snsVPNSPIndex.setStatus("current")
_SnsVPNSPIKERulename_Type = DisplayString
_SnsVPNSPIKERulename_Object = MibTableColumn
snsVPNSPIKERulename = _SnsVPNSPIKERulename_Object(
    (1, 3, 6, 1, 4, 1, 11256, 1, 1, 3, 1, 2),
    _SnsVPNSPIKERulename_Type()
)
snsVPNSPIKERulename.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snsVPNSPIKERulename.setStatus("current")
_SnsVPNSPRulename_Type = DisplayString
_SnsVPNSPRulename_Object = MibTableColumn
snsVPNSPRulename = _SnsVPNSPRulename_Object(
    (1, 3, 6, 1, 4, 1, 11256, 1, 1, 3, 1, 3),
    _SnsVPNSPRulename_Type()
)
snsVPNSPRulename.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snsVPNSPRulename.setStatus("current")


class _SnsVPNSPVersion_Type(Integer32):
    """Custom type snsVPNSPVersion based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("both", 0),
          ("ikev1", 1),
          ("ikev2", 2))
    )


_SnsVPNSPVersion_Type.__name__ = "Integer32"
_SnsVPNSPVersion_Object = MibTableColumn
snsVPNSPVersion = _SnsVPNSPVersion_Object(
    (1, 3, 6, 1, 4, 1, 11256, 1, 1, 3, 1, 4),
    _SnsVPNSPVersion_Type()
)
snsVPNSPVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snsVPNSPVersion.setStatus("current")
_SnsVPNSPIPSrc_Type = DisplayString
_SnsVPNSPIPSrc_Object = MibTableColumn
snsVPNSPIPSrc = _SnsVPNSPIPSrc_Object(
    (1, 3, 6, 1, 4, 1, 11256, 1, 1, 3, 1, 5),
    _SnsVPNSPIPSrc_Type()
)
snsVPNSPIPSrc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snsVPNSPIPSrc.setStatus("current")
_SnsVPNSPIPDst_Type = DisplayString
_SnsVPNSPIPDst_Object = MibTableColumn
snsVPNSPIPDst = _SnsVPNSPIPDst_Object(
    (1, 3, 6, 1, 4, 1, 11256, 1, 1, 3, 1, 6),
    _SnsVPNSPIPDst_Type()
)
snsVPNSPIPDst.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snsVPNSPIPDst.setStatus("current")
_SnsVPNSPTSSrc_Type = DisplayString
_SnsVPNSPTSSrc_Object = MibTableColumn
snsVPNSPTSSrc = _SnsVPNSPTSSrc_Object(
    (1, 3, 6, 1, 4, 1, 11256, 1, 1, 3, 1, 7),
    _SnsVPNSPTSSrc_Type()
)
snsVPNSPTSSrc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snsVPNSPTSSrc.setStatus("current")
_SnsVPNSPTSDst_Type = DisplayString
_SnsVPNSPTSDst_Object = MibTableColumn
snsVPNSPTSDst = _SnsVPNSPTSDst_Object(
    (1, 3, 6, 1, 4, 1, 11256, 1, 1, 3, 1, 8),
    _SnsVPNSPTSDst_Type()
)
snsVPNSPTSDst.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snsVPNSPTSDst.setStatus("current")
_SnsVPNSPLocalid_Type = DisplayString
_SnsVPNSPLocalid_Object = MibTableColumn
snsVPNSPLocalid = _SnsVPNSPLocalid_Object(
    (1, 3, 6, 1, 4, 1, 11256, 1, 1, 3, 1, 9),
    _SnsVPNSPLocalid_Type()
)
snsVPNSPLocalid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snsVPNSPLocalid.setStatus("current")
_SnsVPNSPRemoteid_Type = DisplayString
_SnsVPNSPRemoteid_Object = MibTableColumn
snsVPNSPRemoteid = _SnsVPNSPRemoteid_Object(
    (1, 3, 6, 1, 4, 1, 11256, 1, 1, 3, 1, 10),
    _SnsVPNSPRemoteid_Type()
)
snsVPNSPRemoteid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snsVPNSPRemoteid.setStatus("current")
_SnsVPNSPPolicy_Type = DisplayString
_SnsVPNSPPolicy_Object = MibTableColumn
snsVPNSPPolicy = _SnsVPNSPPolicy_Object(
    (1, 3, 6, 1, 4, 1, 11256, 1, 1, 3, 1, 11),
    _SnsVPNSPPolicy_Type()
)
snsVPNSPPolicy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snsVPNSPPolicy.setStatus("current")


class _SnsVPNSPEnc_Type(Integer32):
    """Custom type snsVPNSPEnc based on Integer32"""
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


_SnsVPNSPEnc_Type.__name__ = "Integer32"
_SnsVPNSPEnc_Object = MibTableColumn
snsVPNSPEnc = _SnsVPNSPEnc_Object(
    (1, 3, 6, 1, 4, 1, 11256, 1, 1, 3, 1, 12),
    _SnsVPNSPEnc_Type()
)
snsVPNSPEnc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snsVPNSPEnc.setStatus("current")


class _SnsVPNSPType_Type(Integer32):
    """Custom type snsVPNSPType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 0),
          ("gateway", 1),
          ("mobile", 2))
    )


_SnsVPNSPType_Type.__name__ = "Integer32"
_SnsVPNSPType_Object = MibTableColumn
snsVPNSPType = _SnsVPNSPType_Object(
    (1, 3, 6, 1, 4, 1, 11256, 1, 1, 3, 1, 13),
    _SnsVPNSPType_Type()
)
snsVPNSPType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snsVPNSPType.setStatus("current")
_SnsVPNSPMaxLifetime_Type = Counter64
_SnsVPNSPMaxLifetime_Object = MibTableColumn
snsVPNSPMaxLifetime = _SnsVPNSPMaxLifetime_Object(
    (1, 3, 6, 1, 4, 1, 11256, 1, 1, 3, 1, 14),
    _SnsVPNSPMaxLifetime_Type()
)
snsVPNSPMaxLifetime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snsVPNSPMaxLifetime.setStatus("current")
_SnsVPNSPGlobal_Type = Integer32
_SnsVPNSPGlobal_Object = MibTableColumn
snsVPNSPGlobal = _SnsVPNSPGlobal_Object(
    (1, 3, 6, 1, 4, 1, 11256, 1, 1, 3, 1, 15),
    _SnsVPNSPGlobal_Type()
)
snsVPNSPGlobal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snsVPNSPGlobal.setStatus("current")
_SnsVPNSPPPKID_Type = DisplayString
_SnsVPNSPPPKID_Object = MibTableColumn
snsVPNSPPPKID = _SnsVPNSPPPKID_Object(
    (1, 3, 6, 1, 4, 1, 11256, 1, 1, 3, 1, 16),
    _SnsVPNSPPPKID_Type()
)
snsVPNSPPPKID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snsVPNSPPPKID.setStatus("current")
_SnsVPNSPPPKRequired_Type = Integer32
_SnsVPNSPPPKRequired_Object = MibTableColumn
snsVPNSPPPKRequired = _SnsVPNSPPPKRequired_Object(
    (1, 3, 6, 1, 4, 1, 11256, 1, 1, 3, 1, 17),
    _SnsVPNSPPPKRequired_Type()
)
snsVPNSPPPKRequired.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snsVPNSPPPKRequired.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "STORMSHIELD-VPNSP-MIB",
    **{"snsVPNSPTable": snsVPNSPTable,
       "snsVPNSPEntry": snsVPNSPEntry,
       "snsVPNSPIndex": snsVPNSPIndex,
       "snsVPNSPIKERulename": snsVPNSPIKERulename,
       "snsVPNSPRulename": snsVPNSPRulename,
       "snsVPNSPVersion": snsVPNSPVersion,
       "snsVPNSPIPSrc": snsVPNSPIPSrc,
       "snsVPNSPIPDst": snsVPNSPIPDst,
       "snsVPNSPTSSrc": snsVPNSPTSSrc,
       "snsVPNSPTSDst": snsVPNSPTSDst,
       "snsVPNSPLocalid": snsVPNSPLocalid,
       "snsVPNSPRemoteid": snsVPNSPRemoteid,
       "snsVPNSPPolicy": snsVPNSPPolicy,
       "snsVPNSPEnc": snsVPNSPEnc,
       "snsVPNSPType": snsVPNSPType,
       "snsVPNSPMaxLifetime": snsVPNSPMaxLifetime,
       "snsVPNSPGlobal": snsVPNSPGlobal,
       "snsVPNSPPPKID": snsVPNSPPPKID,
       "snsVPNSPPPKRequired": snsVPNSPPPKRequired}
)
