# SNMP MIB module (STORMSHIELD-VPNIKESA-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\stormshield\STORMSHIELD-VPNIKESA-MIB

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

_SnsVPNIKESATable_Object = MibTable
snsVPNIKESATable = _SnsVPNIKESATable_Object(
    (1, 3, 6, 1, 4, 1, 11256, 1, 1, 2)
)
if mibBuilder.loadTexts:
    snsVPNIKESATable.setStatus("current")
_SnsVPNIKESAEntry_Object = MibTableRow
snsVPNIKESAEntry = _SnsVPNIKESAEntry_Object(
    (1, 3, 6, 1, 4, 1, 11256, 1, 1, 2, 1)
)
snsVPNIKESAEntry.setIndexNames(
    (0, "STORMSHIELD-VPNIKESA-MIB", "snsVPNIKESAIndex"),
)
if mibBuilder.loadTexts:
    snsVPNIKESAEntry.setStatus("current")


class _SnsVPNIKESAIndex_Type(Integer32):
    """Custom type snsVPNIKESAIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_SnsVPNIKESAIndex_Type.__name__ = "Integer32"
_SnsVPNIKESAIndex_Object = MibTableColumn
snsVPNIKESAIndex = _SnsVPNIKESAIndex_Object(
    (1, 3, 6, 1, 4, 1, 11256, 1, 1, 2, 1, 1),
    _SnsVPNIKESAIndex_Type()
)
snsVPNIKESAIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snsVPNIKESAIndex.setStatus("current")
_SnsVPNIKESARulename_Type = DisplayString
_SnsVPNIKESARulename_Object = MibTableColumn
snsVPNIKESARulename = _SnsVPNIKESARulename_Object(
    (1, 3, 6, 1, 4, 1, 11256, 1, 1, 2, 1, 2),
    _SnsVPNIKESARulename_Type()
)
snsVPNIKESARulename.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snsVPNIKESARulename.setStatus("current")


class _SnsVPNIKESAVersion_Type(Integer32):
    """Custom type snsVPNIKESAVersion based on Integer32"""
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


_SnsVPNIKESAVersion_Type.__name__ = "Integer32"
_SnsVPNIKESAVersion_Object = MibTableColumn
snsVPNIKESAVersion = _SnsVPNIKESAVersion_Object(
    (1, 3, 6, 1, 4, 1, 11256, 1, 1, 2, 1, 3),
    _SnsVPNIKESAVersion_Type()
)
snsVPNIKESAVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snsVPNIKESAVersion.setStatus("current")
_SnsVPNIKESAIPSrc_Type = DisplayString
_SnsVPNIKESAIPSrc_Object = MibTableColumn
snsVPNIKESAIPSrc = _SnsVPNIKESAIPSrc_Object(
    (1, 3, 6, 1, 4, 1, 11256, 1, 1, 2, 1, 4),
    _SnsVPNIKESAIPSrc_Type()
)
snsVPNIKESAIPSrc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snsVPNIKESAIPSrc.setStatus("current")
_SnsVPNIKESAIPDst_Type = DisplayString
_SnsVPNIKESAIPDst_Object = MibTableColumn
snsVPNIKESAIPDst = _SnsVPNIKESAIPDst_Object(
    (1, 3, 6, 1, 4, 1, 11256, 1, 1, 2, 1, 5),
    _SnsVPNIKESAIPDst_Type()
)
snsVPNIKESAIPDst.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snsVPNIKESAIPDst.setStatus("current")
_SnsVPNIKESAState_Type = DisplayString
_SnsVPNIKESAState_Object = MibTableColumn
snsVPNIKESAState = _SnsVPNIKESAState_Object(
    (1, 3, 6, 1, 4, 1, 11256, 1, 1, 2, 1, 6),
    _SnsVPNIKESAState_Type()
)
snsVPNIKESAState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snsVPNIKESAState.setStatus("current")


class _SnsVPNIKESASide_Type(Integer32):
    """Custom type snsVPNIKESASide based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("initiator", 0),
          ("responder", 1))
    )


_SnsVPNIKESASide_Type.__name__ = "Integer32"
_SnsVPNIKESASide_Object = MibTableColumn
snsVPNIKESASide = _SnsVPNIKESASide_Object(
    (1, 3, 6, 1, 4, 1, 11256, 1, 1, 2, 1, 7),
    _SnsVPNIKESASide_Type()
)
snsVPNIKESASide.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snsVPNIKESASide.setStatus("current")


class _SnsVPNIKESANat_Type(Integer32):
    """Custom type snsVPNIKESANat based on Integer32"""
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
          ("local", 1),
          ("remote", 2),
          ("both", 3))
    )


_SnsVPNIKESANat_Type.__name__ = "Integer32"
_SnsVPNIKESANat_Object = MibTableColumn
snsVPNIKESANat = _SnsVPNIKESANat_Object(
    (1, 3, 6, 1, 4, 1, 11256, 1, 1, 2, 1, 8),
    _SnsVPNIKESANat_Type()
)
snsVPNIKESANat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snsVPNIKESANat.setStatus("current")
_SnsVPNIKESACookiei_Type = DisplayString
_SnsVPNIKESACookiei_Object = MibTableColumn
snsVPNIKESACookiei = _SnsVPNIKESACookiei_Object(
    (1, 3, 6, 1, 4, 1, 11256, 1, 1, 2, 1, 9),
    _SnsVPNIKESACookiei_Type()
)
snsVPNIKESACookiei.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snsVPNIKESACookiei.setStatus("current")
_SnsVPNIKESACookier_Type = DisplayString
_SnsVPNIKESACookier_Object = MibTableColumn
snsVPNIKESACookier = _SnsVPNIKESACookier_Object(
    (1, 3, 6, 1, 4, 1, 11256, 1, 1, 2, 1, 10),
    _SnsVPNIKESACookier_Type()
)
snsVPNIKESACookier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snsVPNIKESACookier.setStatus("current")
_SnsVPNIKESALocalid_Type = DisplayString
_SnsVPNIKESALocalid_Object = MibTableColumn
snsVPNIKESALocalid = _SnsVPNIKESALocalid_Object(
    (1, 3, 6, 1, 4, 1, 11256, 1, 1, 2, 1, 11),
    _SnsVPNIKESALocalid_Type()
)
snsVPNIKESALocalid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snsVPNIKESALocalid.setStatus("current")
_SnsVPNIKESARemoteid_Type = DisplayString
_SnsVPNIKESARemoteid_Object = MibTableColumn
snsVPNIKESARemoteid = _SnsVPNIKESARemoteid_Object(
    (1, 3, 6, 1, 4, 1, 11256, 1, 1, 2, 1, 12),
    _SnsVPNIKESARemoteid_Type()
)
snsVPNIKESARemoteid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snsVPNIKESARemoteid.setStatus("current")
_SnsVPNIKESAEnc_Type = DisplayString
_SnsVPNIKESAEnc_Object = MibTableColumn
snsVPNIKESAEnc = _SnsVPNIKESAEnc_Object(
    (1, 3, 6, 1, 4, 1, 11256, 1, 1, 2, 1, 13),
    _SnsVPNIKESAEnc_Type()
)
snsVPNIKESAEnc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snsVPNIKESAEnc.setStatus("current")
_SnsVPNIKESAAuth_Type = DisplayString
_SnsVPNIKESAAuth_Object = MibTableColumn
snsVPNIKESAAuth = _SnsVPNIKESAAuth_Object(
    (1, 3, 6, 1, 4, 1, 11256, 1, 1, 2, 1, 14),
    _SnsVPNIKESAAuth_Type()
)
snsVPNIKESAAuth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snsVPNIKESAAuth.setStatus("current")
_SnsVPNIKESAPrf_Type = DisplayString
_SnsVPNIKESAPrf_Object = MibTableColumn
snsVPNIKESAPrf = _SnsVPNIKESAPrf_Object(
    (1, 3, 6, 1, 4, 1, 11256, 1, 1, 2, 1, 15),
    _SnsVPNIKESAPrf_Type()
)
snsVPNIKESAPrf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snsVPNIKESAPrf.setStatus("current")
_SnsVPNIKESAPfs_Type = DisplayString
_SnsVPNIKESAPfs_Object = MibTableColumn
snsVPNIKESAPfs = _SnsVPNIKESAPfs_Object(
    (1, 3, 6, 1, 4, 1, 11256, 1, 1, 2, 1, 16),
    _SnsVPNIKESAPfs_Type()
)
snsVPNIKESAPfs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snsVPNIKESAPfs.setStatus("current")
_SnsVPNIKESALifetime_Type = Counter64
_SnsVPNIKESALifetime_Object = MibTableColumn
snsVPNIKESALifetime = _SnsVPNIKESALifetime_Object(
    (1, 3, 6, 1, 4, 1, 11256, 1, 1, 2, 1, 17),
    _SnsVPNIKESALifetime_Type()
)
snsVPNIKESALifetime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snsVPNIKESALifetime.setStatus("current")
_SnsVPNIKESAMaxLifetime_Type = Counter64
_SnsVPNIKESAMaxLifetime_Object = MibTableColumn
snsVPNIKESAMaxLifetime = _SnsVPNIKESAMaxLifetime_Object(
    (1, 3, 6, 1, 4, 1, 11256, 1, 1, 2, 1, 18),
    _SnsVPNIKESAMaxLifetime_Type()
)
snsVPNIKESAMaxLifetime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snsVPNIKESAMaxLifetime.setStatus("current")
_SnsVPNIKESAGlobal_Type = Integer32
_SnsVPNIKESAGlobal_Object = MibTableColumn
snsVPNIKESAGlobal = _SnsVPNIKESAGlobal_Object(
    (1, 3, 6, 1, 4, 1, 11256, 1, 1, 2, 1, 19),
    _SnsVPNIKESAGlobal_Type()
)
snsVPNIKESAGlobal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snsVPNIKESAGlobal.setStatus("current")
_SnsVPNIKESAPPK_Type = Integer32
_SnsVPNIKESAPPK_Object = MibTableColumn
snsVPNIKESAPPK = _SnsVPNIKESAPPK_Object(
    (1, 3, 6, 1, 4, 1, 11256, 1, 1, 2, 1, 20),
    _SnsVPNIKESAPPK_Type()
)
snsVPNIKESAPPK.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snsVPNIKESAPPK.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "STORMSHIELD-VPNIKESA-MIB",
    **{"snsVPNIKESATable": snsVPNIKESATable,
       "snsVPNIKESAEntry": snsVPNIKESAEntry,
       "snsVPNIKESAIndex": snsVPNIKESAIndex,
       "snsVPNIKESARulename": snsVPNIKESARulename,
       "snsVPNIKESAVersion": snsVPNIKESAVersion,
       "snsVPNIKESAIPSrc": snsVPNIKESAIPSrc,
       "snsVPNIKESAIPDst": snsVPNIKESAIPDst,
       "snsVPNIKESAState": snsVPNIKESAState,
       "snsVPNIKESASide": snsVPNIKESASide,
       "snsVPNIKESANat": snsVPNIKESANat,
       "snsVPNIKESACookiei": snsVPNIKESACookiei,
       "snsVPNIKESACookier": snsVPNIKESACookier,
       "snsVPNIKESALocalid": snsVPNIKESALocalid,
       "snsVPNIKESARemoteid": snsVPNIKESARemoteid,
       "snsVPNIKESAEnc": snsVPNIKESAEnc,
       "snsVPNIKESAAuth": snsVPNIKESAAuth,
       "snsVPNIKESAPrf": snsVPNIKESAPrf,
       "snsVPNIKESAPfs": snsVPNIKESAPfs,
       "snsVPNIKESALifetime": snsVPNIKESALifetime,
       "snsVPNIKESAMaxLifetime": snsVPNIKESAMaxLifetime,
       "snsVPNIKESAGlobal": snsVPNIKESAGlobal,
       "snsVPNIKESAPPK": snsVPNIKESAPPK}
)
