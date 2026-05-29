# SNMP MIB module (ARRIS-D5-VIDEO-IP-BUNDLE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\arris\d5\ARRIS-D5-VIDEO-IP-BUNDLE-MIB

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

(InterfaceIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex")

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
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

arrisD5UEQamIpBundleMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4115, 1, 8, 1, 16)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs



class _D5UEQamIpBundlePolicy_Type(Integer32):
    """Custom type d5UEQamIpBundlePolicy based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("revertive", 1),
          ("nonrevertive", 2))
    )


_D5UEQamIpBundlePolicy_Type.__name__ = "Integer32"
_D5UEQamIpBundlePolicy_Object = MibScalar
d5UEQamIpBundlePolicy = _D5UEQamIpBundlePolicy_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 8, 1, 16, 1),
    _D5UEQamIpBundlePolicy_Type()
)
d5UEQamIpBundlePolicy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    d5UEQamIpBundlePolicy.setStatus("current")
_D5UEQamIpBundlePolicyRevertiveTimeout_Type = Unsigned32
_D5UEQamIpBundlePolicyRevertiveTimeout_Object = MibScalar
d5UEQamIpBundlePolicyRevertiveTimeout = _D5UEQamIpBundlePolicyRevertiveTimeout_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 8, 1, 16, 2),
    _D5UEQamIpBundlePolicyRevertiveTimeout_Type()
)
d5UEQamIpBundlePolicyRevertiveTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    d5UEQamIpBundlePolicyRevertiveTimeout.setStatus("current")


class _D5UEQamIpBundleRevertTo_Type(Integer32):
    """Custom type d5UEQamIpBundleRevertTo based on Integer32"""
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
        *(("none", 0),
          ("gig1", 1),
          ("gig2", 2),
          ("gig3", 3),
          ("gig4", 4))
    )


_D5UEQamIpBundleRevertTo_Type.__name__ = "Integer32"
_D5UEQamIpBundleRevertTo_Object = MibScalar
d5UEQamIpBundleRevertTo = _D5UEQamIpBundleRevertTo_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 8, 1, 16, 3),
    _D5UEQamIpBundleRevertTo_Type()
)
d5UEQamIpBundleRevertTo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    d5UEQamIpBundleRevertTo.setStatus("current")


class _D5UEQamIpBundleRevertFrom_Type(Integer32):
    """Custom type d5UEQamIpBundleRevertFrom based on Integer32"""
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
        *(("none", 0),
          ("gig1", 1),
          ("gig2", 2),
          ("gig3", 3),
          ("gig4", 4))
    )


_D5UEQamIpBundleRevertFrom_Type.__name__ = "Integer32"
_D5UEQamIpBundleRevertFrom_Object = MibScalar
d5UEQamIpBundleRevertFrom = _D5UEQamIpBundleRevertFrom_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 8, 1, 16, 4),
    _D5UEQamIpBundleRevertFrom_Type()
)
d5UEQamIpBundleRevertFrom.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    d5UEQamIpBundleRevertFrom.setStatus("current")
_D5UEQamIpBundleTable_Object = MibTable
d5UEQamIpBundleTable = _D5UEQamIpBundleTable_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 8, 1, 16, 5)
)
if mibBuilder.loadTexts:
    d5UEQamIpBundleTable.setStatus("current")
_D5UEQamIpBundleEntry_Object = MibTableRow
d5UEQamIpBundleEntry = _D5UEQamIpBundleEntry_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 8, 1, 16, 5, 1)
)
d5UEQamIpBundleEntry.setIndexNames(
    (0, "ARRIS-D5-VIDEO-IP-BUNDLE-MIB", "d5UEQamIpBundlePrimaryPort"),
)
if mibBuilder.loadTexts:
    d5UEQamIpBundleEntry.setStatus("current")


class _D5UEQamIpBundlePrimaryPort_Type(Integer32):
    """Custom type d5UEQamIpBundlePrimaryPort based on Integer32"""
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
        *(("gig1", 1),
          ("gig2", 2),
          ("gig3", 3),
          ("gig4", 4))
    )


_D5UEQamIpBundlePrimaryPort_Type.__name__ = "Integer32"
_D5UEQamIpBundlePrimaryPort_Object = MibTableColumn
d5UEQamIpBundlePrimaryPort = _D5UEQamIpBundlePrimaryPort_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 8, 1, 16, 5, 1, 1),
    _D5UEQamIpBundlePrimaryPort_Type()
)
d5UEQamIpBundlePrimaryPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    d5UEQamIpBundlePrimaryPort.setStatus("current")


class _D5UEQamIpBundleBackUpPort_Type(Integer32):
    """Custom type d5UEQamIpBundleBackUpPort based on Integer32"""
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
        *(("gig1", 1),
          ("gig2", 2),
          ("gig3", 3),
          ("gig4", 4),
          ("fe1", 5))
    )


_D5UEQamIpBundleBackUpPort_Type.__name__ = "Integer32"
_D5UEQamIpBundleBackUpPort_Object = MibTableColumn
d5UEQamIpBundleBackUpPort = _D5UEQamIpBundleBackUpPort_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 8, 1, 16, 5, 1, 2),
    _D5UEQamIpBundleBackUpPort_Type()
)
d5UEQamIpBundleBackUpPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    d5UEQamIpBundleBackUpPort.setStatus("current")
_D5UEQamIpBundlePrimaryFailedOver_Type = TruthValue
_D5UEQamIpBundlePrimaryFailedOver_Object = MibTableColumn
d5UEQamIpBundlePrimaryFailedOver = _D5UEQamIpBundlePrimaryFailedOver_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 8, 1, 16, 5, 1, 3),
    _D5UEQamIpBundlePrimaryFailedOver_Type()
)
d5UEQamIpBundlePrimaryFailedOver.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    d5UEQamIpBundlePrimaryFailedOver.setStatus("current")
_D5UEQamIpBundlePrimaryLinkUp_Type = TruthValue
_D5UEQamIpBundlePrimaryLinkUp_Object = MibTableColumn
d5UEQamIpBundlePrimaryLinkUp = _D5UEQamIpBundlePrimaryLinkUp_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 8, 1, 16, 5, 1, 4),
    _D5UEQamIpBundlePrimaryLinkUp_Type()
)
d5UEQamIpBundlePrimaryLinkUp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    d5UEQamIpBundlePrimaryLinkUp.setStatus("current")
_D5UEQamIpBundleBackupLinkUp_Type = TruthValue
_D5UEQamIpBundleBackupLinkUp_Object = MibTableColumn
d5UEQamIpBundleBackupLinkUp = _D5UEQamIpBundleBackupLinkUp_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 8, 1, 16, 5, 1, 5),
    _D5UEQamIpBundleBackupLinkUp_Type()
)
d5UEQamIpBundleBackupLinkUp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    d5UEQamIpBundleBackupLinkUp.setStatus("current")
_D5UEQamIpBundleStatus_Type = RowStatus
_D5UEQamIpBundleStatus_Object = MibTableColumn
d5UEQamIpBundleStatus = _D5UEQamIpBundleStatus_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 8, 1, 16, 5, 1, 6),
    _D5UEQamIpBundleStatus_Type()
)
d5UEQamIpBundleStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    d5UEQamIpBundleStatus.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ARRIS-D5-VIDEO-IP-BUNDLE-MIB",
    **{"arrisD5UEQamIpBundleMib": arrisD5UEQamIpBundleMib,
       "d5UEQamIpBundlePolicy": d5UEQamIpBundlePolicy,
       "d5UEQamIpBundlePolicyRevertiveTimeout": d5UEQamIpBundlePolicyRevertiveTimeout,
       "d5UEQamIpBundleRevertTo": d5UEQamIpBundleRevertTo,
       "d5UEQamIpBundleRevertFrom": d5UEQamIpBundleRevertFrom,
       "d5UEQamIpBundleTable": d5UEQamIpBundleTable,
       "d5UEQamIpBundleEntry": d5UEQamIpBundleEntry,
       "d5UEQamIpBundlePrimaryPort": d5UEQamIpBundlePrimaryPort,
       "d5UEQamIpBundleBackUpPort": d5UEQamIpBundleBackUpPort,
       "d5UEQamIpBundlePrimaryFailedOver": d5UEQamIpBundlePrimaryFailedOver,
       "d5UEQamIpBundlePrimaryLinkUp": d5UEQamIpBundlePrimaryLinkUp,
       "d5UEQamIpBundleBackupLinkUp": d5UEQamIpBundleBackupLinkUp,
       "d5UEQamIpBundleStatus": d5UEQamIpBundleStatus}
)
