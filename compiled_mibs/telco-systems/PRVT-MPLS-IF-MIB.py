# SNMP MIB module (PRVT-MPLS-IF-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\telco-systems\binos\PRVT-MPLS-IF-MIB

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

(ifEntry,
 ifIndex) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifEntry",
    "ifIndex")

(InetAddress,) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress")

(mpls,) = mibBuilder.importSymbols(
    "PRVT-CR-LDP-MIB",
    "mpls")

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

prvtMPLSIfMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 6)
)
if mibBuilder.loadTexts:
    prvtMPLSIfMib.setRevisions(
        ("2008-01-01 00:00",
         "2007-01-23 00:00",
         "2006-06-27 00:00",
         "2006-01-08 00:00",
         "2005-11-11 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_PrvtMPLSIfaceObjs_ObjectIdentity = ObjectIdentity
prvtMPLSIfaceObjs = _PrvtMPLSIfaceObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 6, 1)
)
_PrvtMplsIfaceTable_Object = MibTable
prvtMplsIfaceTable = _PrvtMplsIfaceTable_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 6, 1, 1)
)
if mibBuilder.loadTexts:
    prvtMplsIfaceTable.setStatus("current")
_PrvtMplsIfaceEntry_Object = MibTableRow
prvtMplsIfaceEntry = _PrvtMplsIfaceEntry_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 6, 1, 1, 1)
)
prvtMplsIfaceEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    prvtMplsIfaceEntry.setStatus("current")
_IfaceMplsEnable_Type = TruthValue
_IfaceMplsEnable_Object = MibTableColumn
ifaceMplsEnable = _IfaceMplsEnable_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 6, 1, 1, 1, 1),
    _IfaceMplsEnable_Type()
)
ifaceMplsEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ifaceMplsEnable.setStatus("current")
_IfaceMplsPHPEnable_Type = TruthValue
_IfaceMplsPHPEnable_Object = MibTableColumn
ifaceMplsPHPEnable = _IfaceMplsPHPEnable_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 6, 1, 1, 1, 2),
    _IfaceMplsPHPEnable_Type()
)
ifaceMplsPHPEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ifaceMplsPHPEnable.setStatus("current")


class _IfaceMplsIngressLblRangeLow_Type(Integer32):
    """Custom type ifaceMplsIngressLblRangeLow based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(32768, 131071),
    )


_IfaceMplsIngressLblRangeLow_Type.__name__ = "Integer32"
_IfaceMplsIngressLblRangeLow_Object = MibTableColumn
ifaceMplsIngressLblRangeLow = _IfaceMplsIngressLblRangeLow_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 6, 1, 1, 1, 3),
    _IfaceMplsIngressLblRangeLow_Type()
)
ifaceMplsIngressLblRangeLow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ifaceMplsIngressLblRangeLow.setStatus("current")


class _IfaceMplsIngressLblRangeHigh_Type(Integer32):
    """Custom type ifaceMplsIngressLblRangeHigh based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(32768, 131071),
    )


_IfaceMplsIngressLblRangeHigh_Type.__name__ = "Integer32"
_IfaceMplsIngressLblRangeHigh_Object = MibTableColumn
ifaceMplsIngressLblRangeHigh = _IfaceMplsIngressLblRangeHigh_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 6, 1, 1, 1, 4),
    _IfaceMplsIngressLblRangeHigh_Type()
)
ifaceMplsIngressLblRangeHigh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ifaceMplsIngressLblRangeHigh.setStatus("current")


class _IfaceMplsEgressLblRangeLow_Type(Integer32):
    """Custom type ifaceMplsEgressLblRangeLow based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(32768, 131071),
    )


_IfaceMplsEgressLblRangeLow_Type.__name__ = "Integer32"
_IfaceMplsEgressLblRangeLow_Object = MibTableColumn
ifaceMplsEgressLblRangeLow = _IfaceMplsEgressLblRangeLow_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 6, 1, 1, 1, 5),
    _IfaceMplsEgressLblRangeLow_Type()
)
ifaceMplsEgressLblRangeLow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ifaceMplsEgressLblRangeLow.setStatus("current")


class _IfaceMplsEgressLblRangeHigh_Type(Integer32):
    """Custom type ifaceMplsEgressLblRangeHigh based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(32768, 131071),
    )


_IfaceMplsEgressLblRangeHigh_Type.__name__ = "Integer32"
_IfaceMplsEgressLblRangeHigh_Object = MibTableColumn
ifaceMplsEgressLblRangeHigh = _IfaceMplsEgressLblRangeHigh_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 6, 1, 1, 1, 6),
    _IfaceMplsEgressLblRangeHigh_Type()
)
ifaceMplsEgressLblRangeHigh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ifaceMplsEgressLblRangeHigh.setStatus("current")


class _IfaceMplsLdpHelloHoldTimer_Type(Integer32):
    """Custom type ifaceMplsLdpHelloHoldTimer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_IfaceMplsLdpHelloHoldTimer_Type.__name__ = "Integer32"
_IfaceMplsLdpHelloHoldTimer_Object = MibTableColumn
ifaceMplsLdpHelloHoldTimer = _IfaceMplsLdpHelloHoldTimer_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 6, 1, 1, 1, 7),
    _IfaceMplsLdpHelloHoldTimer_Type()
)
ifaceMplsLdpHelloHoldTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ifaceMplsLdpHelloHoldTimer.setStatus("current")


class _IfaceMplsLdpKeepaliveHoldTimer_Type(Integer32):
    """Custom type ifaceMplsLdpKeepaliveHoldTimer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_IfaceMplsLdpKeepaliveHoldTimer_Type.__name__ = "Integer32"
_IfaceMplsLdpKeepaliveHoldTimer_Object = MibTableColumn
ifaceMplsLdpKeepaliveHoldTimer = _IfaceMplsLdpKeepaliveHoldTimer_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 6, 1, 1, 1, 8),
    _IfaceMplsLdpKeepaliveHoldTimer_Type()
)
ifaceMplsLdpKeepaliveHoldTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ifaceMplsLdpKeepaliveHoldTimer.setStatus("current")
_IfaceMplsLdpUseGlobalLabelSpace_Type = TruthValue
_IfaceMplsLdpUseGlobalLabelSpace_Object = MibTableColumn
ifaceMplsLdpUseGlobalLabelSpace = _IfaceMplsLdpUseGlobalLabelSpace_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 6, 1, 1, 1, 9),
    _IfaceMplsLdpUseGlobalLabelSpace_Type()
)
ifaceMplsLdpUseGlobalLabelSpace.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ifaceMplsLdpUseGlobalLabelSpace.setStatus("current")
_PrvtRsvpIfaceTable_Object = MibTable
prvtRsvpIfaceTable = _PrvtRsvpIfaceTable_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 6, 1, 2)
)
if mibBuilder.loadTexts:
    prvtRsvpIfaceTable.setStatus("current")
_PrvtRsvpIfaceEntry_Object = MibTableRow
prvtRsvpIfaceEntry = _PrvtRsvpIfaceEntry_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 6, 1, 2, 1)
)
if mibBuilder.loadTexts:
    prvtRsvpIfaceEntry.setStatus("current")
_IfaceRsvpRefreshInterval_Type = Integer32
_IfaceRsvpRefreshInterval_Object = MibTableColumn
ifaceRsvpRefreshInterval = _IfaceRsvpRefreshInterval_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 6, 1, 2, 1, 1),
    _IfaceRsvpRefreshInterval_Type()
)
ifaceRsvpRefreshInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ifaceRsvpRefreshInterval.setStatus("current")
_IfaceRsvpRefreshMultiple_Type = Integer32
_IfaceRsvpRefreshMultiple_Object = MibTableColumn
ifaceRsvpRefreshMultiple = _IfaceRsvpRefreshMultiple_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 6, 1, 2, 1, 2),
    _IfaceRsvpRefreshMultiple_Type()
)
ifaceRsvpRefreshMultiple.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ifaceRsvpRefreshMultiple.setStatus("current")


class _IfaceRsvpSlewNumerator_Type(Integer32):
    """Custom type ifaceRsvpSlewNumerator based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 214783647),
    )


_IfaceRsvpSlewNumerator_Type.__name__ = "Integer32"
_IfaceRsvpSlewNumerator_Object = MibTableColumn
ifaceRsvpSlewNumerator = _IfaceRsvpSlewNumerator_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 6, 1, 2, 1, 3),
    _IfaceRsvpSlewNumerator_Type()
)
ifaceRsvpSlewNumerator.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ifaceRsvpSlewNumerator.setStatus("current")


class _IfaceRsvpSlewDenom_Type(Integer32):
    """Custom type ifaceRsvpSlewDenom based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 214783647),
    )


_IfaceRsvpSlewDenom_Type.__name__ = "Integer32"
_IfaceRsvpSlewDenom_Object = MibTableColumn
ifaceRsvpSlewDenom = _IfaceRsvpSlewDenom_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 6, 1, 2, 1, 4),
    _IfaceRsvpSlewDenom_Type()
)
ifaceRsvpSlewDenom.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ifaceRsvpSlewDenom.setStatus("current")


class _IfaceRsvpBlockadeMultiple_Type(Integer32):
    """Custom type ifaceRsvpBlockadeMultiple based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 214783647),
    )


_IfaceRsvpBlockadeMultiple_Type.__name__ = "Integer32"
_IfaceRsvpBlockadeMultiple_Object = MibTableColumn
ifaceRsvpBlockadeMultiple = _IfaceRsvpBlockadeMultiple_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 6, 1, 2, 1, 5),
    _IfaceRsvpBlockadeMultiple_Type()
)
ifaceRsvpBlockadeMultiple.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ifaceRsvpBlockadeMultiple.setStatus("current")


class _IfaceRsvpNotifyRRDecay_Type(Integer32):
    """Custom type ifaceRsvpNotifyRRDecay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_IfaceRsvpNotifyRRDecay_Type.__name__ = "Integer32"
_IfaceRsvpNotifyRRDecay_Object = MibTableColumn
ifaceRsvpNotifyRRDecay = _IfaceRsvpNotifyRRDecay_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 6, 1, 2, 1, 6),
    _IfaceRsvpNotifyRRDecay_Type()
)
ifaceRsvpNotifyRRDecay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ifaceRsvpNotifyRRDecay.setStatus("current")


class _IfaceRsvpNotifyRRInterval_Type(Integer32):
    """Custom type ifaceRsvpNotifyRRInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 214783647),
    )


_IfaceRsvpNotifyRRInterval_Type.__name__ = "Integer32"
_IfaceRsvpNotifyRRInterval_Object = MibTableColumn
ifaceRsvpNotifyRRInterval = _IfaceRsvpNotifyRRInterval_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 6, 1, 2, 1, 7),
    _IfaceRsvpNotifyRRInterval_Type()
)
ifaceRsvpNotifyRRInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ifaceRsvpNotifyRRInterval.setStatus("current")


class _IfaceRsvpNotifyRRLimit_Type(Integer32):
    """Custom type ifaceRsvpNotifyRRLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 214783647),
    )


_IfaceRsvpNotifyRRLimit_Type.__name__ = "Integer32"
_IfaceRsvpNotifyRRLimit_Object = MibTableColumn
ifaceRsvpNotifyRRLimit = _IfaceRsvpNotifyRRLimit_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 6, 1, 2, 1, 8),
    _IfaceRsvpNotifyRRLimit_Type()
)
ifaceRsvpNotifyRRLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ifaceRsvpNotifyRRLimit.setStatus("current")
_IfaceRsvpHelloInterval_Type = Integer32
_IfaceRsvpHelloInterval_Object = MibTableColumn
ifaceRsvpHelloInterval = _IfaceRsvpHelloInterval_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 6, 1, 2, 1, 9),
    _IfaceRsvpHelloInterval_Type()
)
ifaceRsvpHelloInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ifaceRsvpHelloInterval.setStatus("current")


class _IfaceRsvpHelloDecay_Type(Integer32):
    """Custom type ifaceRsvpHelloDecay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_IfaceRsvpHelloDecay_Type.__name__ = "Integer32"
_IfaceRsvpHelloDecay_Object = MibTableColumn
ifaceRsvpHelloDecay = _IfaceRsvpHelloDecay_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 6, 1, 2, 1, 10),
    _IfaceRsvpHelloDecay_Type()
)
ifaceRsvpHelloDecay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ifaceRsvpHelloDecay.setStatus("current")
_IfaceRsvpHelloTolerance_Type = Unsigned32
_IfaceRsvpHelloTolerance_Object = MibTableColumn
ifaceRsvpHelloTolerance = _IfaceRsvpHelloTolerance_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 6, 1, 2, 1, 11),
    _IfaceRsvpHelloTolerance_Type()
)
ifaceRsvpHelloTolerance.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ifaceRsvpHelloTolerance.setStatus("current")
_IfaceRsvpHelloPersist_Type = Unsigned32
_IfaceRsvpHelloPersist_Object = MibTableColumn
ifaceRsvpHelloPersist = _IfaceRsvpHelloPersist_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 6, 1, 2, 1, 12),
    _IfaceRsvpHelloPersist_Type()
)
ifaceRsvpHelloPersist.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ifaceRsvpHelloPersist.setStatus("current")


class _IfaceRsvpHelloTTL_Type(Integer32):
    """Custom type ifaceRsvpHelloTTL based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_IfaceRsvpHelloTTL_Type.__name__ = "Integer32"
_IfaceRsvpHelloTTL_Object = MibTableColumn
ifaceRsvpHelloTTL = _IfaceRsvpHelloTTL_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 6, 1, 2, 1, 13),
    _IfaceRsvpHelloTTL_Type()
)
ifaceRsvpHelloTTL.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ifaceRsvpHelloTTL.setStatus("current")
_PrvtMPLSRouteObjs_ObjectIdentity = ObjectIdentity
prvtMPLSRouteObjs = _PrvtMPLSRouteObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 6, 2)
)
_PrvtMplsRouteProtocolTable_Object = MibTable
prvtMplsRouteProtocolTable = _PrvtMplsRouteProtocolTable_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 6, 2, 1)
)
if mibBuilder.loadTexts:
    prvtMplsRouteProtocolTable.setStatus("current")
_PrvtMplsRouteProtocolEntry_Object = MibTableRow
prvtMplsRouteProtocolEntry = _PrvtMplsRouteProtocolEntry_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 6, 2, 1, 1)
)
prvtMplsRouteProtocolEntry.setIndexNames(
    (0, "PRVT-MPLS-IF-MIB", "prvtMplsRouteDirection"),
    (0, "PRVT-MPLS-IF-MIB", "prvtMplsRouteType"),
)
if mibBuilder.loadTexts:
    prvtMplsRouteProtocolEntry.setStatus("current")


class _PrvtMplsRouteDirection_Type(Integer32):
    """Custom type prvtMplsRouteDirection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ingress", 1),
          ("egress", 2))
    )


_PrvtMplsRouteDirection_Type.__name__ = "Integer32"
_PrvtMplsRouteDirection_Object = MibTableColumn
prvtMplsRouteDirection = _PrvtMplsRouteDirection_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 6, 2, 1, 1, 1),
    _PrvtMplsRouteDirection_Type()
)
prvtMplsRouteDirection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtMplsRouteDirection.setStatus("current")


class _PrvtMplsRouteType_Type(Integer32):
    """Custom type prvtMplsRouteType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("bgp", 1),
          ("connected", 2),
          ("isis", 3),
          ("kernel", 4),
          ("ospf", 5),
          ("rip", 6),
          ("static", 7))
    )


_PrvtMplsRouteType_Type.__name__ = "Integer32"
_PrvtMplsRouteType_Object = MibTableColumn
prvtMplsRouteType = _PrvtMplsRouteType_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 6, 2, 1, 1, 2),
    _PrvtMplsRouteType_Type()
)
prvtMplsRouteType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtMplsRouteType.setStatus("current")
_PrvtMplsRouteRowStatus_Type = RowStatus
_PrvtMplsRouteRowStatus_Object = MibTableColumn
prvtMplsRouteRowStatus = _PrvtMplsRouteRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 6, 2, 1, 1, 3),
    _PrvtMplsRouteRowStatus_Type()
)
prvtMplsRouteRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    prvtMplsRouteRowStatus.setStatus("current")
_PrvtMplsRouteAddressTable_Object = MibTable
prvtMplsRouteAddressTable = _PrvtMplsRouteAddressTable_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 6, 2, 2)
)
if mibBuilder.loadTexts:
    prvtMplsRouteAddressTable.setStatus("current")
_PrvtMplsRouteAddressEntry_Object = MibTableRow
prvtMplsRouteAddressEntry = _PrvtMplsRouteAddressEntry_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 6, 2, 2, 1)
)
prvtMplsRouteAddressEntry.setIndexNames(
    (0, "PRVT-MPLS-IF-MIB", "prvtMplsAddressDirection"),
    (0, "PRVT-MPLS-IF-MIB", "prvtMplsAddressIPAddr"),
    (0, "PRVT-MPLS-IF-MIB", "prvtMplsAddressMask"),
)
if mibBuilder.loadTexts:
    prvtMplsRouteAddressEntry.setStatus("current")


class _PrvtMplsAddressDirection_Type(Integer32):
    """Custom type prvtMplsAddressDirection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ingress", 1),
          ("egress", 2))
    )


_PrvtMplsAddressDirection_Type.__name__ = "Integer32"
_PrvtMplsAddressDirection_Object = MibTableColumn
prvtMplsAddressDirection = _PrvtMplsAddressDirection_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 6, 2, 2, 1, 1),
    _PrvtMplsAddressDirection_Type()
)
prvtMplsAddressDirection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtMplsAddressDirection.setStatus("current")
_PrvtMplsAddressIPAddr_Type = InetAddress
_PrvtMplsAddressIPAddr_Object = MibTableColumn
prvtMplsAddressIPAddr = _PrvtMplsAddressIPAddr_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 6, 2, 2, 1, 2),
    _PrvtMplsAddressIPAddr_Type()
)
prvtMplsAddressIPAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtMplsAddressIPAddr.setStatus("current")


class _PrvtMplsAddressMask_Type(Integer32):
    """Custom type prvtMplsAddressMask based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32),
    )


_PrvtMplsAddressMask_Type.__name__ = "Integer32"
_PrvtMplsAddressMask_Object = MibTableColumn
prvtMplsAddressMask = _PrvtMplsAddressMask_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 6, 2, 2, 1, 3),
    _PrvtMplsAddressMask_Type()
)
prvtMplsAddressMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtMplsAddressMask.setStatus("current")
_PrvtMplsAddressRowStatus_Type = RowStatus
_PrvtMplsAddressRowStatus_Object = MibTableColumn
prvtMplsAddressRowStatus = _PrvtMplsAddressRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 6, 2, 2, 1, 4),
    _PrvtMplsAddressRowStatus_Type()
)
prvtMplsAddressRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    prvtMplsAddressRowStatus.setStatus("current")
ifEntry.registerAugmentions(
    ("PRVT-MPLS-IF-MIB",
     "prvtRsvpIfaceEntry")
)
prvtRsvpIfaceEntry.setIndexNames(*ifEntry.getIndexNames())

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "PRVT-MPLS-IF-MIB",
    **{"prvtMPLSIfMib": prvtMPLSIfMib,
       "prvtMPLSIfaceObjs": prvtMPLSIfaceObjs,
       "prvtMplsIfaceTable": prvtMplsIfaceTable,
       "prvtMplsIfaceEntry": prvtMplsIfaceEntry,
       "ifaceMplsEnable": ifaceMplsEnable,
       "ifaceMplsPHPEnable": ifaceMplsPHPEnable,
       "ifaceMplsIngressLblRangeLow": ifaceMplsIngressLblRangeLow,
       "ifaceMplsIngressLblRangeHigh": ifaceMplsIngressLblRangeHigh,
       "ifaceMplsEgressLblRangeLow": ifaceMplsEgressLblRangeLow,
       "ifaceMplsEgressLblRangeHigh": ifaceMplsEgressLblRangeHigh,
       "ifaceMplsLdpHelloHoldTimer": ifaceMplsLdpHelloHoldTimer,
       "ifaceMplsLdpKeepaliveHoldTimer": ifaceMplsLdpKeepaliveHoldTimer,
       "ifaceMplsLdpUseGlobalLabelSpace": ifaceMplsLdpUseGlobalLabelSpace,
       "prvtRsvpIfaceTable": prvtRsvpIfaceTable,
       "prvtRsvpIfaceEntry": prvtRsvpIfaceEntry,
       "ifaceRsvpRefreshInterval": ifaceRsvpRefreshInterval,
       "ifaceRsvpRefreshMultiple": ifaceRsvpRefreshMultiple,
       "ifaceRsvpSlewNumerator": ifaceRsvpSlewNumerator,
       "ifaceRsvpSlewDenom": ifaceRsvpSlewDenom,
       "ifaceRsvpBlockadeMultiple": ifaceRsvpBlockadeMultiple,
       "ifaceRsvpNotifyRRDecay": ifaceRsvpNotifyRRDecay,
       "ifaceRsvpNotifyRRInterval": ifaceRsvpNotifyRRInterval,
       "ifaceRsvpNotifyRRLimit": ifaceRsvpNotifyRRLimit,
       "ifaceRsvpHelloInterval": ifaceRsvpHelloInterval,
       "ifaceRsvpHelloDecay": ifaceRsvpHelloDecay,
       "ifaceRsvpHelloTolerance": ifaceRsvpHelloTolerance,
       "ifaceRsvpHelloPersist": ifaceRsvpHelloPersist,
       "ifaceRsvpHelloTTL": ifaceRsvpHelloTTL,
       "prvtMPLSRouteObjs": prvtMPLSRouteObjs,
       "prvtMplsRouteProtocolTable": prvtMplsRouteProtocolTable,
       "prvtMplsRouteProtocolEntry": prvtMplsRouteProtocolEntry,
       "prvtMplsRouteDirection": prvtMplsRouteDirection,
       "prvtMplsRouteType": prvtMplsRouteType,
       "prvtMplsRouteRowStatus": prvtMplsRouteRowStatus,
       "prvtMplsRouteAddressTable": prvtMplsRouteAddressTable,
       "prvtMplsRouteAddressEntry": prvtMplsRouteAddressEntry,
       "prvtMplsAddressDirection": prvtMplsAddressDirection,
       "prvtMplsAddressIPAddr": prvtMplsAddressIPAddr,
       "prvtMplsAddressMask": prvtMplsAddressMask,
       "prvtMplsAddressRowStatus": prvtMplsAddressRowStatus}
)
