# SNMP MIB module (CMM3-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\cambium\CMM3-MIB

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

(whispBox,
 whispCMM,
 whispModules) = mibBuilder.importSymbols(
    "WHISP-GLOBAL-REG-MIB",
    "whispBox",
    "whispCMM",
    "whispModules")

(EventString,
 WhispLUID,
 WhispMACAddress) = mibBuilder.importSymbols(
    "WHISP-TCV2-MIB",
    "EventString",
    "WhispLUID",
    "WhispMACAddress")


# MODULE-IDENTITY

cmmIIIMibModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 161, 19, 1, 1, 15)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CmmGroups_ObjectIdentity = ObjectIdentity
cmmGroups = _CmmGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 4, 1)
)
_CmmSwitch_ObjectIdentity = ObjectIdentity
cmmSwitch = _CmmSwitch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 4, 2)
)
_CmmSwitchTable_Object = MibTable
cmmSwitchTable = _CmmSwitchTable_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 4, 2, 1)
)
if mibBuilder.loadTexts:
    cmmSwitchTable.setStatus("current")
_CmmSwitchEntry_Object = MibTableRow
cmmSwitchEntry = _CmmSwitchEntry_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 4, 2, 1, 1)
)
cmmSwitchEntry.setIndexNames(
    (0, "CMM3-MIB", "mirSrcPortNumber"),
)
if mibBuilder.loadTexts:
    cmmSwitchEntry.setStatus("current")


class _PortNumber_Type(Integer32):
    """Custom type portNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 9),
    )


_PortNumber_Type.__name__ = "Integer32"
_PortNumber_Object = MibTableColumn
portNumber = _PortNumber_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 4, 2, 1, 1, 1),
    _PortNumber_Type()
)
portNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portNumber.setStatus("current")
_RxDropPkts_Type = Counter32
_RxDropPkts_Object = MibTableColumn
rxDropPkts = _RxDropPkts_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 4, 2, 1, 1, 2),
    _RxDropPkts_Type()
)
rxDropPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rxDropPkts.setStatus("current")
_RxOctets_Type = Counter64
_RxOctets_Object = MibTableColumn
rxOctets = _RxOctets_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 4, 2, 1, 1, 3),
    _RxOctets_Type()
)
rxOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rxOctets.setStatus("current")
_RxBroadcastPkts_Type = Counter32
_RxBroadcastPkts_Object = MibTableColumn
rxBroadcastPkts = _RxBroadcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 4, 2, 1, 1, 4),
    _RxBroadcastPkts_Type()
)
rxBroadcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rxBroadcastPkts.setStatus("current")
_RxMulticastPkts_Type = Counter32
_RxMulticastPkts_Object = MibTableColumn
rxMulticastPkts = _RxMulticastPkts_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 4, 2, 1, 1, 5),
    _RxMulticastPkts_Type()
)
rxMulticastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rxMulticastPkts.setStatus("current")
_RxSAChanges_Type = Counter32
_RxSAChanges_Object = MibTableColumn
rxSAChanges = _RxSAChanges_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 4, 2, 1, 1, 6),
    _RxSAChanges_Type()
)
rxSAChanges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rxSAChanges.setStatus("current")
_RxUndersizePkts_Type = Counter32
_RxUndersizePkts_Object = MibTableColumn
rxUndersizePkts = _RxUndersizePkts_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 4, 2, 1, 1, 7),
    _RxUndersizePkts_Type()
)
rxUndersizePkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rxUndersizePkts.setStatus("current")
_RxOversizePkts_Type = Counter32
_RxOversizePkts_Object = MibTableColumn
rxOversizePkts = _RxOversizePkts_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 4, 2, 1, 1, 8),
    _RxOversizePkts_Type()
)
rxOversizePkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rxOversizePkts.setStatus("current")
_RxFragments_Type = Counter32
_RxFragments_Object = MibTableColumn
rxFragments = _RxFragments_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 4, 2, 1, 1, 9),
    _RxFragments_Type()
)
rxFragments.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rxFragments.setStatus("current")
_RxJabbers_Type = Counter32
_RxJabbers_Object = MibTableColumn
rxJabbers = _RxJabbers_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 4, 2, 1, 1, 10),
    _RxJabbers_Type()
)
rxJabbers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rxJabbers.setStatus("current")
_RxUnicastPkts_Type = Counter32
_RxUnicastPkts_Object = MibTableColumn
rxUnicastPkts = _RxUnicastPkts_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 4, 2, 1, 1, 11),
    _RxUnicastPkts_Type()
)
rxUnicastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rxUnicastPkts.setStatus("current")
_RxAlignmentErrors_Type = Counter32
_RxAlignmentErrors_Object = MibTableColumn
rxAlignmentErrors = _RxAlignmentErrors_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 4, 2, 1, 1, 12),
    _RxAlignmentErrors_Type()
)
rxAlignmentErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rxAlignmentErrors.setStatus("current")
_RxFCSErrors_Type = Counter32
_RxFCSErrors_Object = MibTableColumn
rxFCSErrors = _RxFCSErrors_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 4, 2, 1, 1, 13),
    _RxFCSErrors_Type()
)
rxFCSErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rxFCSErrors.setStatus("current")
_RxGoodOctets_Type = Counter64
_RxGoodOctets_Object = MibTableColumn
rxGoodOctets = _RxGoodOctets_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 4, 2, 1, 1, 14),
    _RxGoodOctets_Type()
)
rxGoodOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rxGoodOctets.setStatus("current")
_RxExcessSizeDisc_Type = Counter32
_RxExcessSizeDisc_Object = MibTableColumn
rxExcessSizeDisc = _RxExcessSizeDisc_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 4, 2, 1, 1, 15),
    _RxExcessSizeDisc_Type()
)
rxExcessSizeDisc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rxExcessSizeDisc.setStatus("current")
_RxPausePkts_Type = Counter32
_RxPausePkts_Object = MibTableColumn
rxPausePkts = _RxPausePkts_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 4, 2, 1, 1, 16),
    _RxPausePkts_Type()
)
rxPausePkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rxPausePkts.setStatus("current")
_RxSymbolErrors_Type = Counter32
_RxSymbolErrors_Object = MibTableColumn
rxSymbolErrors = _RxSymbolErrors_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 4, 2, 1, 1, 17),
    _RxSymbolErrors_Type()
)
rxSymbolErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rxSymbolErrors.setStatus("current")
_TxDropPkts_Type = Counter32
_TxDropPkts_Object = MibTableColumn
txDropPkts = _TxDropPkts_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 4, 2, 1, 1, 18),
    _TxDropPkts_Type()
)
txDropPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    txDropPkts.setStatus("current")
_TxOctets_Type = Counter64
_TxOctets_Object = MibTableColumn
txOctets = _TxOctets_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 4, 2, 1, 1, 19),
    _TxOctets_Type()
)
txOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    txOctets.setStatus("current")
_TxBroadcastPkts_Type = Counter32
_TxBroadcastPkts_Object = MibTableColumn
txBroadcastPkts = _TxBroadcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 4, 2, 1, 1, 20),
    _TxBroadcastPkts_Type()
)
txBroadcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    txBroadcastPkts.setStatus("current")
_TxMulticastPkts_Type = Counter32
_TxMulticastPkts_Object = MibTableColumn
txMulticastPkts = _TxMulticastPkts_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 4, 2, 1, 1, 21),
    _TxMulticastPkts_Type()
)
txMulticastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    txMulticastPkts.setStatus("current")
_TxCollisions_Type = Counter32
_TxCollisions_Object = MibTableColumn
txCollisions = _TxCollisions_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 4, 2, 1, 1, 22),
    _TxCollisions_Type()
)
txCollisions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    txCollisions.setStatus("current")
_TxUnicastPkts_Type = Counter32
_TxUnicastPkts_Object = MibTableColumn
txUnicastPkts = _TxUnicastPkts_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 4, 2, 1, 1, 23),
    _TxUnicastPkts_Type()
)
txUnicastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    txUnicastPkts.setStatus("current")
_TxSingleCollision_Type = Counter32
_TxSingleCollision_Object = MibTableColumn
txSingleCollision = _TxSingleCollision_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 4, 2, 1, 1, 24),
    _TxSingleCollision_Type()
)
txSingleCollision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    txSingleCollision.setStatus("current")
_TxMultipleCollision_Type = Counter32
_TxMultipleCollision_Object = MibTableColumn
txMultipleCollision = _TxMultipleCollision_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 4, 2, 1, 1, 25),
    _TxMultipleCollision_Type()
)
txMultipleCollision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    txMultipleCollision.setStatus("current")
_TxDeferredTransmit_Type = Counter32
_TxDeferredTransmit_Object = MibTableColumn
txDeferredTransmit = _TxDeferredTransmit_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 4, 2, 1, 1, 26),
    _TxDeferredTransmit_Type()
)
txDeferredTransmit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    txDeferredTransmit.setStatus("current")
_TxLateCollision_Type = Counter32
_TxLateCollision_Object = MibTableColumn
txLateCollision = _TxLateCollision_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 4, 2, 1, 1, 27),
    _TxLateCollision_Type()
)
txLateCollision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    txLateCollision.setStatus("current")
_TxExcessiveCollision_Type = Counter32
_TxExcessiveCollision_Object = MibTableColumn
txExcessiveCollision = _TxExcessiveCollision_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 4, 2, 1, 1, 28),
    _TxExcessiveCollision_Type()
)
txExcessiveCollision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    txExcessiveCollision.setStatus("current")
_TxPausePkts_Type = Counter32
_TxPausePkts_Object = MibTableColumn
txPausePkts = _TxPausePkts_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 4, 2, 1, 1, 29),
    _TxPausePkts_Type()
)
txPausePkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    txPausePkts.setStatus("current")
_TxFrameInDisc_Type = Counter32
_TxFrameInDisc_Object = MibTableColumn
txFrameInDisc = _TxFrameInDisc_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 4, 2, 1, 1, 30),
    _TxFrameInDisc_Type()
)
txFrameInDisc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    txFrameInDisc.setStatus("current")
_Pkts64Octets_Type = Counter32
_Pkts64Octets_Object = MibTableColumn
pkts64Octets = _Pkts64Octets_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 4, 2, 1, 1, 31),
    _Pkts64Octets_Type()
)
pkts64Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pkts64Octets.setStatus("current")
_Pkts65to127Octets_Type = Counter32
_Pkts65to127Octets_Object = MibTableColumn
pkts65to127Octets = _Pkts65to127Octets_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 4, 2, 1, 1, 32),
    _Pkts65to127Octets_Type()
)
pkts65to127Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pkts65to127Octets.setStatus("current")
_Pkts128to255Octets_Type = Counter32
_Pkts128to255Octets_Object = MibTableColumn
pkts128to255Octets = _Pkts128to255Octets_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 4, 2, 1, 1, 33),
    _Pkts128to255Octets_Type()
)
pkts128to255Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pkts128to255Octets.setStatus("current")
_Pkts256to511Octets_Type = Counter32
_Pkts256to511Octets_Object = MibTableColumn
pkts256to511Octets = _Pkts256to511Octets_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 4, 2, 1, 1, 34),
    _Pkts256to511Octets_Type()
)
pkts256to511Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pkts256to511Octets.setStatus("current")
_Pkts512to1023Octets_Type = Counter32
_Pkts512to1023Octets_Object = MibTableColumn
pkts512to1023Octets = _Pkts512to1023Octets_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 4, 2, 1, 1, 35),
    _Pkts512to1023Octets_Type()
)
pkts512to1023Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pkts512to1023Octets.setStatus("current")
_Pkts1024to1522Octets_Type = Counter32
_Pkts1024to1522Octets_Object = MibTableColumn
pkts1024to1522Octets = _Pkts1024to1522Octets_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 4, 2, 1, 1, 36),
    _Pkts1024to1522Octets_Type()
)
pkts1024to1522Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pkts1024to1522Octets.setStatus("current")


class _PortMirrorEnable_Type(Integer32):
    """Custom type portMirrorEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_PortMirrorEnable_Type.__name__ = "Integer32"
_PortMirrorEnable_Object = MibScalar
portMirrorEnable = _PortMirrorEnable_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 4, 2, 2),
    _PortMirrorEnable_Type()
)
portMirrorEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portMirrorEnable.setStatus("current")


class _MirrorCapturePort_Type(Integer32):
    """Custom type mirrorCapturePort based on Integer32"""
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
        *(("port1", 1),
          ("port2", 2),
          ("port3", 3),
          ("port4", 4),
          ("port5", 5),
          ("port6", 6),
          ("port7", 7),
          ("port8", 8))
    )


_MirrorCapturePort_Type.__name__ = "Integer32"
_MirrorCapturePort_Object = MibScalar
mirrorCapturePort = _MirrorCapturePort_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 4, 2, 3),
    _MirrorCapturePort_Type()
)
mirrorCapturePort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mirrorCapturePort.setStatus("current")
_CmmSwitchMirrorSrcPortsTable_Object = MibTable
cmmSwitchMirrorSrcPortsTable = _CmmSwitchMirrorSrcPortsTable_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 4, 2, 4)
)
if mibBuilder.loadTexts:
    cmmSwitchMirrorSrcPortsTable.setStatus("current")
_CmmSwitchMirrorSrcPortsEntry_Object = MibTableRow
cmmSwitchMirrorSrcPortsEntry = _CmmSwitchMirrorSrcPortsEntry_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 4, 2, 4, 1)
)
cmmSwitchMirrorSrcPortsEntry.setIndexNames(
    (0, "CMM3-MIB", "mirSrcPortNumber"),
)
if mibBuilder.loadTexts:
    cmmSwitchMirrorSrcPortsEntry.setStatus("current")


class _MirSrcPortNumber_Type(Integer32):
    """Custom type mirSrcPortNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 9),
    )


_MirSrcPortNumber_Type.__name__ = "Integer32"
_MirSrcPortNumber_Object = MibTableColumn
mirSrcPortNumber = _MirSrcPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 4, 2, 4, 1, 1),
    _MirSrcPortNumber_Type()
)
mirSrcPortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mirSrcPortNumber.setStatus("current")


class _MirSrcRxEnable_Type(Integer32):
    """Custom type mirSrcRxEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_MirSrcRxEnable_Type.__name__ = "Integer32"
_MirSrcRxEnable_Object = MibTableColumn
mirSrcRxEnable = _MirSrcRxEnable_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 4, 2, 4, 1, 2),
    _MirSrcRxEnable_Type()
)
mirSrcRxEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mirSrcRxEnable.setStatus("current")


class _MirSrcTxEnable_Type(Integer32):
    """Custom type mirSrcTxEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_MirSrcTxEnable_Type.__name__ = "Integer32"
_MirSrcTxEnable_Object = MibTableColumn
mirSrcTxEnable = _MirSrcTxEnable_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 4, 2, 4, 1, 3),
    _MirSrcTxEnable_Type()
)
mirSrcTxEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mirSrcTxEnable.setStatus("current")
_CmmConfig_ObjectIdentity = ObjectIdentity
cmmConfig = _CmmConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 4, 3)
)


class _GpsTimingPulse_Type(Integer32):
    """Custom type gpsTimingPulse based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("slave", 0),
          ("master", 1))
    )


_GpsTimingPulse_Type.__name__ = "Integer32"
_GpsTimingPulse_Object = MibScalar
gpsTimingPulse = _GpsTimingPulse_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 4, 3, 1),
    _GpsTimingPulse_Type()
)
gpsTimingPulse.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gpsTimingPulse.setStatus("current")
_Lan1Ip_Type = IpAddress
_Lan1Ip_Object = MibScalar
lan1Ip = _Lan1Ip_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 4, 3, 2),
    _Lan1Ip_Type()
)
lan1Ip.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lan1Ip.setStatus("current")
_Lan1SubnetMask_Type = IpAddress
_Lan1SubnetMask_Object = MibScalar
lan1SubnetMask = _Lan1SubnetMask_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 4, 3, 3),
    _Lan1SubnetMask_Type()
)
lan1SubnetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lan1SubnetMask.setStatus("current")
_DefaultGateway_Type = IpAddress
_DefaultGateway_Object = MibScalar
defaultGateway = _DefaultGateway_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 4, 3, 4),
    _DefaultGateway_Type()
)
defaultGateway.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    defaultGateway.setStatus("current")


class _Port1PowerCtr_Type(Integer32):
    """Custom type port1PowerCtr based on Integer32"""
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


_Port1PowerCtr_Type.__name__ = "Integer32"
_Port1PowerCtr_Object = MibScalar
port1PowerCtr = _Port1PowerCtr_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 4, 3, 5),
    _Port1PowerCtr_Type()
)
port1PowerCtr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    port1PowerCtr.setStatus("current")


class _Port2PowerCtr_Type(Integer32):
    """Custom type port2PowerCtr based on Integer32"""
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


_Port2PowerCtr_Type.__name__ = "Integer32"
_Port2PowerCtr_Object = MibScalar
port2PowerCtr = _Port2PowerCtr_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 4, 3, 6),
    _Port2PowerCtr_Type()
)
port2PowerCtr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    port2PowerCtr.setStatus("current")


class _Port3PowerCtr_Type(Integer32):
    """Custom type port3PowerCtr based on Integer32"""
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


_Port3PowerCtr_Type.__name__ = "Integer32"
_Port3PowerCtr_Object = MibScalar
port3PowerCtr = _Port3PowerCtr_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 4, 3, 7),
    _Port3PowerCtr_Type()
)
port3PowerCtr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    port3PowerCtr.setStatus("current")


class _Port4PowerCtr_Type(Integer32):
    """Custom type port4PowerCtr based on Integer32"""
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


_Port4PowerCtr_Type.__name__ = "Integer32"
_Port4PowerCtr_Object = MibScalar
port4PowerCtr = _Port4PowerCtr_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 4, 3, 8),
    _Port4PowerCtr_Type()
)
port4PowerCtr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    port4PowerCtr.setStatus("current")


class _Port5PowerCtr_Type(Integer32):
    """Custom type port5PowerCtr based on Integer32"""
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


_Port5PowerCtr_Type.__name__ = "Integer32"
_Port5PowerCtr_Object = MibScalar
port5PowerCtr = _Port5PowerCtr_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 4, 3, 9),
    _Port5PowerCtr_Type()
)
port5PowerCtr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    port5PowerCtr.setStatus("current")


class _Port6PowerCtr_Type(Integer32):
    """Custom type port6PowerCtr based on Integer32"""
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


_Port6PowerCtr_Type.__name__ = "Integer32"
_Port6PowerCtr_Object = MibScalar
port6PowerCtr = _Port6PowerCtr_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 4, 3, 10),
    _Port6PowerCtr_Type()
)
port6PowerCtr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    port6PowerCtr.setStatus("current")


class _Port7PowerCtr_Type(Integer32):
    """Custom type port7PowerCtr based on Integer32"""
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


_Port7PowerCtr_Type.__name__ = "Integer32"
_Port7PowerCtr_Object = MibScalar
port7PowerCtr = _Port7PowerCtr_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 4, 3, 11),
    _Port7PowerCtr_Type()
)
port7PowerCtr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    port7PowerCtr.setStatus("current")


class _Port8PowerCtr_Type(Integer32):
    """Custom type port8PowerCtr based on Integer32"""
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


_Port8PowerCtr_Type.__name__ = "Integer32"
_Port8PowerCtr_Object = MibScalar
port8PowerCtr = _Port8PowerCtr_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 4, 3, 12),
    _Port8PowerCtr_Type()
)
port8PowerCtr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    port8PowerCtr.setStatus("current")
_DisplayOnlyAccess_Type = DisplayString
_DisplayOnlyAccess_Object = MibScalar
displayOnlyAccess = _DisplayOnlyAccess_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 4, 3, 13),
    _DisplayOnlyAccess_Type()
)
displayOnlyAccess.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    displayOnlyAccess.setStatus("obsolete")
_FullAccess_Type = DisplayString
_FullAccess_Object = MibScalar
fullAccess = _FullAccess_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 4, 3, 14),
    _FullAccess_Type()
)
fullAccess.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fullAccess.setStatus("obsolete")
_DisplayOnlyStatus_Type = DisplayString
_DisplayOnlyStatus_Object = MibScalar
displayOnlyStatus = _DisplayOnlyStatus_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 4, 3, 15),
    _DisplayOnlyStatus_Type()
)
displayOnlyStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    displayOnlyStatus.setStatus("obsolete")
_FullAccessStatus_Type = DisplayString
_FullAccessStatus_Object = MibScalar
fullAccessStatus = _FullAccessStatus_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 4, 3, 16),
    _FullAccessStatus_Type()
)
fullAccessStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fullAccessStatus.setStatus("obsolete")
_WebAutoUpdate_Type = Integer32
_WebAutoUpdate_Object = MibScalar
webAutoUpdate = _WebAutoUpdate_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 4, 3, 17),
    _WebAutoUpdate_Type()
)
webAutoUpdate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    webAutoUpdate.setStatus("current")
if mibBuilder.loadTexts:
    webAutoUpdate.setUnits("Seconds")


class _Port1Config_Type(Integer32):
    """Custom type port1Config based on Integer32"""
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
        *(("auto", 1),
          ("hundredFDX", 2),
          ("hundredHDX", 3),
          ("tenFDX", 4),
          ("tenHDX", 5))
    )


_Port1Config_Type.__name__ = "Integer32"
_Port1Config_Object = MibScalar
port1Config = _Port1Config_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 4, 3, 18),
    _Port1Config_Type()
)
port1Config.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    port1Config.setStatus("current")


class _Port2Config_Type(Integer32):
    """Custom type port2Config based on Integer32"""
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
        *(("auto", 1),
          ("hundredFDX", 2),
          ("hundredHDX", 3),
          ("tenFDX", 4),
          ("tenHDX", 5))
    )


_Port2Config_Type.__name__ = "Integer32"
_Port2Config_Object = MibScalar
port2Config = _Port2Config_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 4, 3, 19),
    _Port2Config_Type()
)
port2Config.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    port2Config.setStatus("current")


class _Port3Config_Type(Integer32):
    """Custom type port3Config based on Integer32"""
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
        *(("auto", 1),
          ("hundredFDX", 2),
          ("hundredHDX", 3),
          ("tenFDX", 4),
          ("tenHDX", 5))
    )


_Port3Config_Type.__name__ = "Integer32"
_Port3Config_Object = MibScalar
port3Config = _Port3Config_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 4, 3, 20),
    _Port3Config_Type()
)
port3Config.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    port3Config.setStatus("current")


class _Port4Config_Type(Integer32):
    """Custom type port4Config based on Integer32"""
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
        *(("auto", 1),
          ("hundredFDX", 2),
          ("hundredHDX", 3),
          ("tenFDX", 4),
          ("tenHDX", 5))
    )


_Port4Config_Type.__name__ = "Integer32"
_Port4Config_Object = MibScalar
port4Config = _Port4Config_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 4, 3, 21),
    _Port4Config_Type()
)
port4Config.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    port4Config.setStatus("current")


class _Port5Config_Type(Integer32):
    """Custom type port5Config based on Integer32"""
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
        *(("auto", 1),
          ("hundredFDX", 2),
          ("hundredHDX", 3),
          ("tenFDX", 4),
          ("tenHDX", 5))
    )


_Port5Config_Type.__name__ = "Integer32"
_Port5Config_Object = MibScalar
port5Config = _Port5Config_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 4, 3, 22),
    _Port5Config_Type()
)
port5Config.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    port5Config.setStatus("current")


class _Port6Config_Type(Integer32):
    """Custom type port6Config based on Integer32"""
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
        *(("auto", 1),
          ("hundredFDX", 2),
          ("hundredHDX", 3),
          ("tenFDX", 4),
          ("tenHDX", 5))
    )


_Port6Config_Type.__name__ = "Integer32"
_Port6Config_Object = MibScalar
port6Config = _Port6Config_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 4, 3, 23),
    _Port6Config_Type()
)
port6Config.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    port6Config.setStatus("current")


class _Port7Config_Type(Integer32):
    """Custom type port7Config based on Integer32"""
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
        *(("auto", 1),
          ("hundredFDX", 2),
          ("hundredHDX", 3),
          ("tenFDX", 4),
          ("tenHDX", 5))
    )


_Port7Config_Type.__name__ = "Integer32"
_Port7Config_Object = MibScalar
port7Config = _Port7Config_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 4, 3, 24),
    _Port7Config_Type()
)
port7Config.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    port7Config.setStatus("current")


class _Port8Config_Type(Integer32):
    """Custom type port8Config based on Integer32"""
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
        *(("auto", 1),
          ("hundredFDX", 2),
          ("hundredHDX", 3),
          ("tenFDX", 4),
          ("tenHDX", 5))
    )


_Port8Config_Type.__name__ = "Integer32"
_Port8Config_Object = MibScalar
port8Config = _Port8Config_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 4, 3, 25),
    _Port8Config_Type()
)
port8Config.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    port8Config.setStatus("current")
_Port1Description_Type = DisplayString
_Port1Description_Object = MibScalar
port1Description = _Port1Description_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 4, 3, 26),
    _Port1Description_Type()
)
port1Description.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    port1Description.setStatus("current")
_Port2Description_Type = DisplayString
_Port2Description_Object = MibScalar
port2Description = _Port2Description_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 4, 3, 27),
    _Port2Description_Type()
)
port2Description.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    port2Description.setStatus("current")
_Port3Description_Type = DisplayString
_Port3Description_Object = MibScalar
port3Description = _Port3Description_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 4, 3, 28),
    _Port3Description_Type()
)
port3Description.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    port3Description.setStatus("current")
_Port4Description_Type = DisplayString
_Port4Description_Object = MibScalar
port4Description = _Port4Description_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 4, 3, 29),
    _Port4Description_Type()
)
port4Description.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    port4Description.setStatus("current")
_Port5Description_Type = DisplayString
_Port5Description_Object = MibScalar
port5Description = _Port5Description_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 4, 3, 30),
    _Port5Description_Type()
)
port5Description.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    port5Description.setStatus("current")
_Port6Description_Type = DisplayString
_Port6Description_Object = MibScalar
port6Description = _Port6Description_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 4, 3, 31),
    _Port6Description_Type()
)
port6Description.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    port6Description.setStatus("current")
_Port7Description_Type = DisplayString
_Port7Description_Object = MibScalar
port7Description = _Port7Description_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 4, 3, 32),
    _Port7Description_Type()
)
port7Description.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    port7Description.setStatus("current")
_Port8Description_Type = DisplayString
_Port8Description_Object = MibScalar
port8Description = _Port8Description_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 4, 3, 33),
    _Port8Description_Type()
)
port8Description.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    port8Description.setStatus("current")
_SnmpTrap1_Type = IpAddress
_SnmpTrap1_Object = MibScalar
snmpTrap1 = _SnmpTrap1_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 4, 3, 34),
    _SnmpTrap1_Type()
)
snmpTrap1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpTrap1.setStatus("current")
_SnmpTrap2_Type = IpAddress
_SnmpTrap2_Object = MibScalar
snmpTrap2 = _SnmpTrap2_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 4, 3, 35),
    _SnmpTrap2_Type()
)
snmpTrap2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpTrap2.setStatus("current")
_SnmpTrap3_Type = IpAddress
_SnmpTrap3_Object = MibScalar
snmpTrap3 = _SnmpTrap3_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 4, 3, 36),
    _SnmpTrap3_Type()
)
snmpTrap3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpTrap3.setStatus("current")
_SnmpTrap4_Type = IpAddress
_SnmpTrap4_Object = MibScalar
snmpTrap4 = _SnmpTrap4_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 4, 3, 37),
    _SnmpTrap4_Type()
)
snmpTrap4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpTrap4.setStatus("current")
_SnmpTrap5_Type = IpAddress
_SnmpTrap5_Object = MibScalar
snmpTrap5 = _SnmpTrap5_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 4, 3, 38),
    _SnmpTrap5_Type()
)
snmpTrap5.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpTrap5.setStatus("current")
_SnmpTrap6_Type = IpAddress
_SnmpTrap6_Object = MibScalar
snmpTrap6 = _SnmpTrap6_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 4, 3, 39),
    _SnmpTrap6_Type()
)
snmpTrap6.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpTrap6.setStatus("current")
_SnmpTrap7_Type = IpAddress
_SnmpTrap7_Object = MibScalar
snmpTrap7 = _SnmpTrap7_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 4, 3, 40),
    _SnmpTrap7_Type()
)
snmpTrap7.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpTrap7.setStatus("current")
_SnmpTrap8_Type = IpAddress
_SnmpTrap8_Object = MibScalar
snmpTrap8 = _SnmpTrap8_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 4, 3, 41),
    _SnmpTrap8_Type()
)
snmpTrap8.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpTrap8.setStatus("current")
_SnmpTrap9_Type = IpAddress
_SnmpTrap9_Object = MibScalar
snmpTrap9 = _SnmpTrap9_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 4, 3, 42),
    _SnmpTrap9_Type()
)
snmpTrap9.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpTrap9.setStatus("current")
_SnmpTrap10_Type = IpAddress
_SnmpTrap10_Object = MibScalar
snmpTrap10 = _SnmpTrap10_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 4, 3, 43),
    _SnmpTrap10_Type()
)
snmpTrap10.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpTrap10.setStatus("current")


class _VlanTagEnable_Type(Integer32):
    """Custom type vlanTagEnable based on Integer32"""
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


_VlanTagEnable_Type.__name__ = "Integer32"
_VlanTagEnable_Object = MibScalar
vlanTagEnable = _VlanTagEnable_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 4, 3, 44),
    _VlanTagEnable_Type()
)
vlanTagEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vlanTagEnable.setStatus("current")


class _VlanTagId_Type(Integer32):
    """Custom type vlanTagId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_VlanTagId_Type.__name__ = "Integer32"
_VlanTagId_Object = MibScalar
vlanTagId = _VlanTagId_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 4, 3, 45),
    _VlanTagId_Type()
)
vlanTagId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vlanTagId.setStatus("current")


class _Port1Uplink_Type(Integer32):
    """Custom type port1Uplink based on Integer32"""
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


_Port1Uplink_Type.__name__ = "Integer32"
_Port1Uplink_Object = MibScalar
port1Uplink = _Port1Uplink_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 4, 3, 46),
    _Port1Uplink_Type()
)
port1Uplink.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    port1Uplink.setStatus("current")


class _Port2Uplink_Type(Integer32):
    """Custom type port2Uplink based on Integer32"""
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


_Port2Uplink_Type.__name__ = "Integer32"
_Port2Uplink_Object = MibScalar
port2Uplink = _Port2Uplink_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 4, 3, 47),
    _Port2Uplink_Type()
)
port2Uplink.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    port2Uplink.setStatus("current")


class _Port3Uplink_Type(Integer32):
    """Custom type port3Uplink based on Integer32"""
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


_Port3Uplink_Type.__name__ = "Integer32"
_Port3Uplink_Object = MibScalar
port3Uplink = _Port3Uplink_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 4, 3, 48),
    _Port3Uplink_Type()
)
port3Uplink.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    port3Uplink.setStatus("current")


class _Port4Uplink_Type(Integer32):
    """Custom type port4Uplink based on Integer32"""
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


_Port4Uplink_Type.__name__ = "Integer32"
_Port4Uplink_Object = MibScalar
port4Uplink = _Port4Uplink_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 4, 3, 49),
    _Port4Uplink_Type()
)
port4Uplink.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    port4Uplink.setStatus("current")


class _Port5Uplink_Type(Integer32):
    """Custom type port5Uplink based on Integer32"""
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


_Port5Uplink_Type.__name__ = "Integer32"
_Port5Uplink_Object = MibScalar
port5Uplink = _Port5Uplink_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 4, 3, 50),
    _Port5Uplink_Type()
)
port5Uplink.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    port5Uplink.setStatus("current")


class _Port6Uplink_Type(Integer32):
    """Custom type port6Uplink based on Integer32"""
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


_Port6Uplink_Type.__name__ = "Integer32"
_Port6Uplink_Object = MibScalar
port6Uplink = _Port6Uplink_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 4, 3, 51),
    _Port6Uplink_Type()
)
port6Uplink.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    port6Uplink.setStatus("current")


class _Port7Uplink_Type(Integer32):
    """Custom type port7Uplink based on Integer32"""
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


_Port7Uplink_Type.__name__ = "Integer32"
_Port7Uplink_Object = MibScalar
port7Uplink = _Port7Uplink_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 4, 3, 52),
    _Port7Uplink_Type()
)
port7Uplink.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    port7Uplink.setStatus("current")


class _Port8Uplink_Type(Integer32):
    """Custom type port8Uplink based on Integer32"""
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


_Port8Uplink_Type.__name__ = "Integer32"
_Port8Uplink_Object = MibScalar
port8Uplink = _Port8Uplink_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 4, 3, 53),
    _Port8Uplink_Type()
)
port8Uplink.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    port8Uplink.setStatus("current")


class _RebootIfRequired_Type(Integer32):
    """Custom type rebootIfRequired based on Integer32"""
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


_RebootIfRequired_Type.__name__ = "Integer32"
_RebootIfRequired_Object = MibScalar
rebootIfRequired = _RebootIfRequired_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 4, 3, 54),
    _RebootIfRequired_Type()
)
rebootIfRequired.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rebootIfRequired.setStatus("current")


class _Port1VlanConf_Type(Integer32):
    """Custom type port1VlanConf based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_Port1VlanConf_Type.__name__ = "Integer32"
_Port1VlanConf_Object = MibScalar
port1VlanConf = _Port1VlanConf_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 4, 3, 55),
    _Port1VlanConf_Type()
)
port1VlanConf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    port1VlanConf.setStatus("current")


class _Port2VlanConf_Type(Integer32):
    """Custom type port2VlanConf based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_Port2VlanConf_Type.__name__ = "Integer32"
_Port2VlanConf_Object = MibScalar
port2VlanConf = _Port2VlanConf_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 4, 3, 56),
    _Port2VlanConf_Type()
)
port2VlanConf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    port2VlanConf.setStatus("current")


class _Port3VlanConf_Type(Integer32):
    """Custom type port3VlanConf based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_Port3VlanConf_Type.__name__ = "Integer32"
_Port3VlanConf_Object = MibScalar
port3VlanConf = _Port3VlanConf_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 4, 3, 57),
    _Port3VlanConf_Type()
)
port3VlanConf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    port3VlanConf.setStatus("current")


class _Port4VlanConf_Type(Integer32):
    """Custom type port4VlanConf based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_Port4VlanConf_Type.__name__ = "Integer32"
_Port4VlanConf_Object = MibScalar
port4VlanConf = _Port4VlanConf_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 4, 3, 58),
    _Port4VlanConf_Type()
)
port4VlanConf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    port4VlanConf.setStatus("current")


class _Port5VlanConf_Type(Integer32):
    """Custom type port5VlanConf based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_Port5VlanConf_Type.__name__ = "Integer32"
_Port5VlanConf_Object = MibScalar
port5VlanConf = _Port5VlanConf_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 4, 3, 59),
    _Port5VlanConf_Type()
)
port5VlanConf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    port5VlanConf.setStatus("current")


class _Port6VlanConf_Type(Integer32):
    """Custom type port6VlanConf based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_Port6VlanConf_Type.__name__ = "Integer32"
_Port6VlanConf_Object = MibScalar
port6VlanConf = _Port6VlanConf_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 4, 3, 60),
    _Port6VlanConf_Type()
)
port6VlanConf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    port6VlanConf.setStatus("current")


class _Port7VlanConf_Type(Integer32):
    """Custom type port7VlanConf based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_Port7VlanConf_Type.__name__ = "Integer32"
_Port7VlanConf_Object = MibScalar
port7VlanConf = _Port7VlanConf_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 4, 3, 61),
    _Port7VlanConf_Type()
)
port7VlanConf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    port7VlanConf.setStatus("current")


class _Port8VlanConf_Type(Integer32):
    """Custom type port8VlanConf based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_Port8VlanConf_Type.__name__ = "Integer32"
_Port8VlanConf_Object = MibScalar
port8VlanConf = _Port8VlanConf_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 4, 3, 62),
    _Port8VlanConf_Type()
)
port8VlanConf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    port8VlanConf.setStatus("current")


class _Port1PwrReset_Type(Integer32):
    """Custom type port1PwrReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Port1PwrReset_Type.__name__ = "Integer32"
_Port1PwrReset_Object = MibScalar
port1PwrReset = _Port1PwrReset_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 4, 3, 63),
    _Port1PwrReset_Type()
)
port1PwrReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    port1PwrReset.setStatus("current")


class _Port2PwrReset_Type(Integer32):
    """Custom type port2PwrReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Port2PwrReset_Type.__name__ = "Integer32"
_Port2PwrReset_Object = MibScalar
port2PwrReset = _Port2PwrReset_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 4, 3, 64),
    _Port2PwrReset_Type()
)
port2PwrReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    port2PwrReset.setStatus("current")


class _Port3PwrReset_Type(Integer32):
    """Custom type port3PwrReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Port3PwrReset_Type.__name__ = "Integer32"
_Port3PwrReset_Object = MibScalar
port3PwrReset = _Port3PwrReset_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 4, 3, 65),
    _Port3PwrReset_Type()
)
port3PwrReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    port3PwrReset.setStatus("current")


class _Port4PwrReset_Type(Integer32):
    """Custom type port4PwrReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Port4PwrReset_Type.__name__ = "Integer32"
_Port4PwrReset_Object = MibScalar
port4PwrReset = _Port4PwrReset_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 4, 3, 66),
    _Port4PwrReset_Type()
)
port4PwrReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    port4PwrReset.setStatus("current")


class _Port5PwrReset_Type(Integer32):
    """Custom type port5PwrReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Port5PwrReset_Type.__name__ = "Integer32"
_Port5PwrReset_Object = MibScalar
port5PwrReset = _Port5PwrReset_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 4, 3, 67),
    _Port5PwrReset_Type()
)
port5PwrReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    port5PwrReset.setStatus("current")


class _Port6PwrReset_Type(Integer32):
    """Custom type port6PwrReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Port6PwrReset_Type.__name__ = "Integer32"
_Port6PwrReset_Object = MibScalar
port6PwrReset = _Port6PwrReset_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 4, 3, 68),
    _Port6PwrReset_Type()
)
port6PwrReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    port6PwrReset.setStatus("current")


class _Port7PwrReset_Type(Integer32):
    """Custom type port7PwrReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Port7PwrReset_Type.__name__ = "Integer32"
_Port7PwrReset_Object = MibScalar
port7PwrReset = _Port7PwrReset_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 4, 3, 69),
    _Port7PwrReset_Type()
)
port7PwrReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    port7PwrReset.setStatus("current")


class _Port8PwrReset_Type(Integer32):
    """Custom type port8PwrReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Port8PwrReset_Type.__name__ = "Integer32"
_Port8PwrReset_Object = MibScalar
port8PwrReset = _Port8PwrReset_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 4, 3, 70),
    _Port8PwrReset_Type()
)
port8PwrReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    port8PwrReset.setStatus("current")


class _SnmpReadOnly_Type(Integer32):
    """Custom type snmpReadOnly based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("readWritePermissions", 0),
          ("readOnlyPermissions", 1))
    )


_SnmpReadOnly_Type.__name__ = "Integer32"
_SnmpReadOnly_Object = MibScalar
snmpReadOnly = _SnmpReadOnly_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 4, 3, 71),
    _SnmpReadOnly_Type()
)
snmpReadOnly.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpReadOnly.setStatus("current")
_SnmpCommunityString_Type = DisplayString
_SnmpCommunityString_Object = MibScalar
snmpCommunityString = _SnmpCommunityString_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 4, 3, 72),
    _SnmpCommunityString_Type()
)
snmpCommunityString.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpCommunityString.setStatus("current")
_SnmpAccessSubnet_Type = DisplayString
_SnmpAccessSubnet_Object = MibScalar
snmpAccessSubnet = _SnmpAccessSubnet_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 4, 3, 73),
    _SnmpAccessSubnet_Type()
)
snmpAccessSubnet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpAccessSubnet.setStatus("current")
_SnmpAccessSubnet2_Type = DisplayString
_SnmpAccessSubnet2_Object = MibScalar
snmpAccessSubnet2 = _SnmpAccessSubnet2_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 4, 3, 74),
    _SnmpAccessSubnet2_Type()
)
snmpAccessSubnet2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpAccessSubnet2.setStatus("current")
_SnmpAccessSubnet3_Type = DisplayString
_SnmpAccessSubnet3_Object = MibScalar
snmpAccessSubnet3 = _SnmpAccessSubnet3_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 4, 3, 75),
    _SnmpAccessSubnet3_Type()
)
snmpAccessSubnet3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpAccessSubnet3.setStatus("current")
_SnmpAccessSubnet4_Type = DisplayString
_SnmpAccessSubnet4_Object = MibScalar
snmpAccessSubnet4 = _SnmpAccessSubnet4_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 4, 3, 76),
    _SnmpAccessSubnet4_Type()
)
snmpAccessSubnet4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpAccessSubnet4.setStatus("current")
_SnmpAccessSubnet5_Type = DisplayString
_SnmpAccessSubnet5_Object = MibScalar
snmpAccessSubnet5 = _SnmpAccessSubnet5_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 4, 3, 77),
    _SnmpAccessSubnet5_Type()
)
snmpAccessSubnet5.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpAccessSubnet5.setStatus("current")
_SnmpAccessSubnet6_Type = DisplayString
_SnmpAccessSubnet6_Object = MibScalar
snmpAccessSubnet6 = _SnmpAccessSubnet6_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 4, 3, 78),
    _SnmpAccessSubnet6_Type()
)
snmpAccessSubnet6.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpAccessSubnet6.setStatus("current")
_SnmpAccessSubnet7_Type = DisplayString
_SnmpAccessSubnet7_Object = MibScalar
snmpAccessSubnet7 = _SnmpAccessSubnet7_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 4, 3, 79),
    _SnmpAccessSubnet7_Type()
)
snmpAccessSubnet7.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpAccessSubnet7.setStatus("current")
_SnmpAccessSubnet8_Type = DisplayString
_SnmpAccessSubnet8_Object = MibScalar
snmpAccessSubnet8 = _SnmpAccessSubnet8_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 4, 3, 80),
    _SnmpAccessSubnet8_Type()
)
snmpAccessSubnet8.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpAccessSubnet8.setStatus("current")
_SnmpAccessSubnet9_Type = DisplayString
_SnmpAccessSubnet9_Object = MibScalar
snmpAccessSubnet9 = _SnmpAccessSubnet9_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 4, 3, 81),
    _SnmpAccessSubnet9_Type()
)
snmpAccessSubnet9.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpAccessSubnet9.setStatus("current")
_SnmpAccessSubnet10_Type = DisplayString
_SnmpAccessSubnet10_Object = MibScalar
snmpAccessSubnet10 = _SnmpAccessSubnet10_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 4, 3, 82),
    _SnmpAccessSubnet10_Type()
)
snmpAccessSubnet10.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpAccessSubnet10.setStatus("current")


class _Port1Management_Type(Integer32):
    """Custom type port1Management based on Integer32"""
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


_Port1Management_Type.__name__ = "Integer32"
_Port1Management_Object = MibScalar
port1Management = _Port1Management_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 4, 3, 83),
    _Port1Management_Type()
)
port1Management.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    port1Management.setStatus("current")


class _Port2Management_Type(Integer32):
    """Custom type port2Management based on Integer32"""
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


_Port2Management_Type.__name__ = "Integer32"
_Port2Management_Object = MibScalar
port2Management = _Port2Management_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 4, 3, 84),
    _Port2Management_Type()
)
port2Management.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    port2Management.setStatus("current")


class _Port3Management_Type(Integer32):
    """Custom type port3Management based on Integer32"""
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


_Port3Management_Type.__name__ = "Integer32"
_Port3Management_Object = MibScalar
port3Management = _Port3Management_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 4, 3, 85),
    _Port3Management_Type()
)
port3Management.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    port3Management.setStatus("current")


class _Port4Management_Type(Integer32):
    """Custom type port4Management based on Integer32"""
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


_Port4Management_Type.__name__ = "Integer32"
_Port4Management_Object = MibScalar
port4Management = _Port4Management_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 4, 3, 86),
    _Port4Management_Type()
)
port4Management.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    port4Management.setStatus("current")


class _Port5Management_Type(Integer32):
    """Custom type port5Management based on Integer32"""
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


_Port5Management_Type.__name__ = "Integer32"
_Port5Management_Object = MibScalar
port5Management = _Port5Management_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 4, 3, 87),
    _Port5Management_Type()
)
port5Management.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    port5Management.setStatus("current")


class _Port6Management_Type(Integer32):
    """Custom type port6Management based on Integer32"""
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


_Port6Management_Type.__name__ = "Integer32"
_Port6Management_Object = MibScalar
port6Management = _Port6Management_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 4, 3, 88),
    _Port6Management_Type()
)
port6Management.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    port6Management.setStatus("current")


class _Port7Management_Type(Integer32):
    """Custom type port7Management based on Integer32"""
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


_Port7Management_Type.__name__ = "Integer32"
_Port7Management_Object = MibScalar
port7Management = _Port7Management_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 4, 3, 89),
    _Port7Management_Type()
)
port7Management.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    port7Management.setStatus("current")


class _Port8Management_Type(Integer32):
    """Custom type port8Management based on Integer32"""
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


_Port8Management_Type.__name__ = "Integer32"
_Port8Management_Object = MibScalar
port8Management = _Port8Management_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 4, 3, 90),
    _Port8Management_Type()
)
port8Management.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    port8Management.setStatus("current")
_SessionTimeout_Type = Integer32
_SessionTimeout_Object = MibScalar
sessionTimeout = _SessionTimeout_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 4, 3, 91),
    _SessionTimeout_Type()
)
sessionTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sessionTimeout.setStatus("current")


class _SiteInfoViewable_Type(Integer32):
    """Custom type siteInfoViewable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_SiteInfoViewable_Type.__name__ = "Integer32"
_SiteInfoViewable_Object = MibScalar
siteInfoViewable = _SiteInfoViewable_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 4, 3, 92),
    _SiteInfoViewable_Type()
)
siteInfoViewable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    siteInfoViewable.setStatus("current")


class _IpAccessFilterEnable_Type(Integer32):
    """Custom type ipAccessFilterEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_IpAccessFilterEnable_Type.__name__ = "Integer32"
_IpAccessFilterEnable_Object = MibScalar
ipAccessFilterEnable = _IpAccessFilterEnable_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 4, 3, 93),
    _IpAccessFilterEnable_Type()
)
ipAccessFilterEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipAccessFilterEnable.setStatus("current")
_AllowedIPAccess1_Type = IpAddress
_AllowedIPAccess1_Object = MibScalar
allowedIPAccess1 = _AllowedIPAccess1_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 4, 3, 94),
    _AllowedIPAccess1_Type()
)
allowedIPAccess1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    allowedIPAccess1.setStatus("current")
_AllowedIPAccess2_Type = IpAddress
_AllowedIPAccess2_Object = MibScalar
allowedIPAccess2 = _AllowedIPAccess2_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 4, 3, 95),
    _AllowedIPAccess2_Type()
)
allowedIPAccess2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    allowedIPAccess2.setStatus("current")
_AllowedIPAccess3_Type = IpAddress
_AllowedIPAccess3_Object = MibScalar
allowedIPAccess3 = _AllowedIPAccess3_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 4, 3, 96),
    _AllowedIPAccess3_Type()
)
allowedIPAccess3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    allowedIPAccess3.setStatus("current")


class _VerifyGPSChecksum_Type(Integer32):
    """Custom type verifyGPSChecksum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("doNotVerifyGPSMessageChecksum", 0),
          ("verifyGPSMessageChecksum", 1))
    )


_VerifyGPSChecksum_Type.__name__ = "Integer32"
_VerifyGPSChecksum_Object = MibScalar
verifyGPSChecksum = _VerifyGPSChecksum_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 4, 3, 97),
    _VerifyGPSChecksum_Type()
)
verifyGPSChecksum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    verifyGPSChecksum.setStatus("current")


class _Cmm3SnmpGPSSyncTrapEnable_Type(Integer32):
    """Custom type cmm3SnmpGPSSyncTrapEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_Cmm3SnmpGPSSyncTrapEnable_Type.__name__ = "Integer32"
_Cmm3SnmpGPSSyncTrapEnable_Object = MibScalar
cmm3SnmpGPSSyncTrapEnable = _Cmm3SnmpGPSSyncTrapEnable_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 4, 3, 98),
    _Cmm3SnmpGPSSyncTrapEnable_Type()
)
cmm3SnmpGPSSyncTrapEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmm3SnmpGPSSyncTrapEnable.setStatus("current")
_CmmStatus_ObjectIdentity = ObjectIdentity
cmmStatus = _CmmStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 4, 4)
)
_CmmPortTable_Object = MibTable
cmmPortTable = _CmmPortTable_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 4, 4, 1)
)
if mibBuilder.loadTexts:
    cmmPortTable.setStatus("current")
_CmmPortEntry_Object = MibTableRow
cmmPortEntry = _CmmPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 4, 4, 1, 1)
)
cmmPortEntry.setIndexNames(
    (0, "CMM3-MIB", "portIndex"),
)
if mibBuilder.loadTexts:
    cmmPortEntry.setStatus("current")


class _PortIndex_Type(Integer32):
    """Custom type portIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_PortIndex_Type.__name__ = "Integer32"
_PortIndex_Object = MibTableColumn
portIndex = _PortIndex_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 4, 4, 1, 1, 1),
    _PortIndex_Type()
)
portIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portIndex.setStatus("current")


class _LinkStatus_Type(Integer32):
    """Custom type linkStatus based on Integer32"""
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


_LinkStatus_Type.__name__ = "Integer32"
_LinkStatus_Object = MibTableColumn
linkStatus = _LinkStatus_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 4, 4, 1, 1, 2),
    _LinkStatus_Type()
)
linkStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkStatus.setStatus("current")


class _LinkSpeed_Type(Integer32):
    """Custom type linkSpeed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("tenBaseT", 0),
          ("hundredBaseT", 1))
    )


_LinkSpeed_Type.__name__ = "Integer32"
_LinkSpeed_Object = MibTableColumn
linkSpeed = _LinkSpeed_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 4, 4, 1, 1, 3),
    _LinkSpeed_Type()
)
linkSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkSpeed.setStatus("current")


class _DuplexStatus_Type(Integer32):
    """Custom type duplexStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("halfDuplex", 0),
          ("fullDuplex", 1))
    )


_DuplexStatus_Type.__name__ = "Integer32"
_DuplexStatus_Object = MibTableColumn
duplexStatus = _DuplexStatus_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 4, 4, 1, 1, 4),
    _DuplexStatus_Type()
)
duplexStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    duplexStatus.setStatus("current")


class _PowerStatus_Type(Integer32):
    """Custom type powerStatus based on Integer32"""
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


_PowerStatus_Type.__name__ = "Integer32"
_PowerStatus_Object = MibTableColumn
powerStatus = _PowerStatus_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 4, 4, 1, 1, 5),
    _PowerStatus_Type()
)
powerStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerStatus.setStatus("current")


class _UplinkStatus_Type(Integer32):
    """Custom type uplinkStatus based on Integer32"""
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


_UplinkStatus_Type.__name__ = "Integer32"
_UplinkStatus_Object = MibTableColumn
uplinkStatus = _UplinkStatus_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 4, 4, 1, 1, 6),
    _UplinkStatus_Type()
)
uplinkStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uplinkStatus.setStatus("current")


class _ManagementStatus_Type(Integer32):
    """Custom type managementStatus based on Integer32"""
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


_ManagementStatus_Type.__name__ = "Integer32"
_ManagementStatus_Object = MibTableColumn
managementStatus = _ManagementStatus_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 4, 4, 1, 1, 7),
    _ManagementStatus_Type()
)
managementStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    managementStatus.setStatus("current")
_DeviceType_Type = DisplayString
_DeviceType_Object = MibScalar
deviceType = _DeviceType_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 4, 4, 2),
    _DeviceType_Type()
)
deviceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deviceType.setStatus("current")
_PldVersion_Type = DisplayString
_PldVersion_Object = MibScalar
pldVersion = _PldVersion_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 4, 4, 3),
    _PldVersion_Type()
)
pldVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pldVersion.setStatus("current")
_SoftwareVersion_Type = DisplayString
_SoftwareVersion_Object = MibScalar
softwareVersion = _SoftwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 4, 4, 4),
    _SoftwareVersion_Type()
)
softwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    softwareVersion.setStatus("current")
_SystemTime_Type = DisplayString
_SystemTime_Object = MibScalar
systemTime = _SystemTime_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 4, 4, 5),
    _SystemTime_Type()
)
systemTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemTime.setStatus("current")
_UpTime_Type = DisplayString
_UpTime_Object = MibScalar
upTime = _UpTime_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 4, 4, 6),
    _UpTime_Type()
)
upTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upTime.setStatus("current")
_SatellitesVisible_Type = DisplayString
_SatellitesVisible_Object = MibScalar
satellitesVisible = _SatellitesVisible_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 4, 4, 7),
    _SatellitesVisible_Type()
)
satellitesVisible.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    satellitesVisible.setStatus("current")
_SatellitesTracked_Type = DisplayString
_SatellitesTracked_Object = MibScalar
satellitesTracked = _SatellitesTracked_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 4, 4, 8),
    _SatellitesTracked_Type()
)
satellitesTracked.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    satellitesTracked.setStatus("current")
_Latitude_Type = DisplayString
_Latitude_Object = MibScalar
latitude = _Latitude_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 4, 4, 9),
    _Latitude_Type()
)
latitude.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    latitude.setStatus("current")
_Longitude_Type = DisplayString
_Longitude_Object = MibScalar
longitude = _Longitude_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 4, 4, 10),
    _Longitude_Type()
)
longitude.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    longitude.setStatus("current")
_Height_Type = DisplayString
_Height_Object = MibScalar
height = _Height_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 4, 4, 11),
    _Height_Type()
)
height.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    height.setStatus("current")
_TrackingMode_Type = DisplayString
_TrackingMode_Object = MibScalar
trackingMode = _TrackingMode_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 4, 4, 12),
    _TrackingMode_Type()
)
trackingMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trackingMode.setStatus("current")
_SyncStatus_Type = DisplayString
_SyncStatus_Object = MibScalar
syncStatus = _SyncStatus_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 4, 4, 13),
    _SyncStatus_Type()
)
syncStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    syncStatus.setStatus("current")
_MacAddress_Type = DisplayString
_MacAddress_Object = MibScalar
macAddress = _MacAddress_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 4, 4, 14),
    _MacAddress_Type()
)
macAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    macAddress.setStatus("current")
_CmmGps_ObjectIdentity = ObjectIdentity
cmmGps = _CmmGps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 4, 5)
)
_GpsTrackingMode_Type = DisplayString
_GpsTrackingMode_Object = MibScalar
gpsTrackingMode = _GpsTrackingMode_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 4, 5, 1),
    _GpsTrackingMode_Type()
)
gpsTrackingMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gpsTrackingMode.setStatus("current")
_GpsTime_Type = DisplayString
_GpsTime_Object = MibScalar
gpsTime = _GpsTime_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 4, 5, 2),
    _GpsTime_Type()
)
gpsTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gpsTime.setStatus("current")
_GpsDate_Type = DisplayString
_GpsDate_Object = MibScalar
gpsDate = _GpsDate_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 4, 5, 3),
    _GpsDate_Type()
)
gpsDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gpsDate.setStatus("current")
_GpsSatellitesVisible_Type = DisplayString
_GpsSatellitesVisible_Object = MibScalar
gpsSatellitesVisible = _GpsSatellitesVisible_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 4, 5, 4),
    _GpsSatellitesVisible_Type()
)
gpsSatellitesVisible.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gpsSatellitesVisible.setStatus("current")
_GpsSatellitesTracked_Type = DisplayString
_GpsSatellitesTracked_Object = MibScalar
gpsSatellitesTracked = _GpsSatellitesTracked_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 4, 5, 5),
    _GpsSatellitesTracked_Type()
)
gpsSatellitesTracked.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gpsSatellitesTracked.setStatus("current")
_GpsHeight_Type = DisplayString
_GpsHeight_Object = MibScalar
gpsHeight = _GpsHeight_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 4, 5, 6),
    _GpsHeight_Type()
)
gpsHeight.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gpsHeight.setStatus("current")
_GpsAntennaConnection_Type = DisplayString
_GpsAntennaConnection_Object = MibScalar
gpsAntennaConnection = _GpsAntennaConnection_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 4, 5, 7),
    _GpsAntennaConnection_Type()
)
gpsAntennaConnection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gpsAntennaConnection.setStatus("current")
_GpsLatitude_Type = DisplayString
_GpsLatitude_Object = MibScalar
gpsLatitude = _GpsLatitude_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 4, 5, 8),
    _GpsLatitude_Type()
)
gpsLatitude.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gpsLatitude.setStatus("current")
_GpsLongitude_Type = DisplayString
_GpsLongitude_Object = MibScalar
gpsLongitude = _GpsLongitude_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 4, 5, 9),
    _GpsLongitude_Type()
)
gpsLongitude.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gpsLongitude.setStatus("current")
_GpsInvalidMsg_Type = DisplayString
_GpsInvalidMsg_Object = MibScalar
gpsInvalidMsg = _GpsInvalidMsg_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 4, 5, 10),
    _GpsInvalidMsg_Type()
)
gpsInvalidMsg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gpsInvalidMsg.setStatus("current")
_GpsRestartCount_Type = Integer32
_GpsRestartCount_Object = MibScalar
gpsRestartCount = _GpsRestartCount_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 4, 5, 11),
    _GpsRestartCount_Type()
)
gpsRestartCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gpsRestartCount.setStatus("current")
_GpsReceiverInfo_Type = DisplayString
_GpsReceiverInfo_Object = MibScalar
gpsReceiverInfo = _GpsReceiverInfo_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 4, 5, 12),
    _GpsReceiverInfo_Type()
)
gpsReceiverInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gpsReceiverInfo.setStatus("current")
_GpsReInitCount_Type = DisplayString
_GpsReInitCount_Object = MibScalar
gpsReInitCount = _GpsReInitCount_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 4, 5, 13),
    _GpsReInitCount_Type()
)
gpsReInitCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gpsReInitCount.setStatus("current")
_CmmEventLog_ObjectIdentity = ObjectIdentity
cmmEventLog = _CmmEventLog_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 4, 6)
)
_EventLog_Type = EventString
_EventLog_Object = MibScalar
eventLog = _EventLog_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 4, 6, 1),
    _EventLog_Type()
)
eventLog.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eventLog.setStatus("current")
_NtpLog_Type = EventString
_NtpLog_Object = MibScalar
ntpLog = _NtpLog_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 4, 6, 2),
    _NtpLog_Type()
)
ntpLog.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntpLog.setStatus("current")
_CmmControls_ObjectIdentity = ObjectIdentity
cmmControls = _CmmControls_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 4, 7)
)


class _Reboot_Type(Integer32):
    """Custom type reboot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("finishedReboot", 0),
          ("reboot", 1))
    )


_Reboot_Type.__name__ = "Integer32"
_Reboot_Object = MibScalar
reboot = _Reboot_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 4, 7, 1),
    _Reboot_Type()
)
reboot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    reboot.setStatus("current")


class _ClearEventLog_Type(Integer32):
    """Custom type clearEventLog based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("notClear", 0),
          ("clear", 1))
    )


_ClearEventLog_Type.__name__ = "Integer32"
_ClearEventLog_Object = MibScalar
clearEventLog = _ClearEventLog_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 4, 7, 2),
    _ClearEventLog_Type()
)
clearEventLog.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clearEventLog.setStatus("current")
_CmmUserTable_Object = MibTable
cmmUserTable = _CmmUserTable_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 4, 8)
)
if mibBuilder.loadTexts:
    cmmUserTable.setStatus("current")
_CmmUserEntry_Object = MibTableRow
cmmUserEntry = _CmmUserEntry_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 4, 8, 1)
)
cmmUserEntry.setIndexNames(
    (0, "CMM3-MIB", "entryIndex"),
)
if mibBuilder.loadTexts:
    cmmUserEntry.setStatus("current")


class _EntryIndex_Type(Integer32):
    """Custom type entryIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_EntryIndex_Type.__name__ = "Integer32"
_EntryIndex_Object = MibTableColumn
entryIndex = _EntryIndex_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 4, 8, 1, 1),
    _EntryIndex_Type()
)
entryIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    entryIndex.setStatus("current")
_UserLoginName_Type = DisplayString
_UserLoginName_Object = MibTableColumn
userLoginName = _UserLoginName_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 4, 8, 1, 2),
    _UserLoginName_Type()
)
userLoginName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    userLoginName.setStatus("current")
_UserPswd_Type = DisplayString
_UserPswd_Object = MibTableColumn
userPswd = _UserPswd_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 4, 8, 1, 3),
    _UserPswd_Type()
)
userPswd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    userPswd.setStatus("current")


class _AccessLevel_Type(Integer32):
    """Custom type accessLevel based on Integer32"""
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
        *(("noAdmin", 0),
          ("guest", 1),
          ("installer", 2),
          ("administrator", 3),
          ("technician", 4),
          ("engineering", 5))
    )


_AccessLevel_Type.__name__ = "Integer32"
_AccessLevel_Object = MibTableColumn
accessLevel = _AccessLevel_Object(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 4, 8, 1, 4),
    _AccessLevel_Type()
)
accessLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accessLevel.setStatus("current")

# Managed Objects groups

cmmSwitchGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 4, 1, 1)
)
cmmSwitchGroup.setObjects(
      *(("CMM3-MIB", "portNumber"),
        ("CMM3-MIB", "rxDropPkts"),
        ("CMM3-MIB", "rxOctets"),
        ("CMM3-MIB", "rxBroadcastPkts"),
        ("CMM3-MIB", "rxMulticastPkts"),
        ("CMM3-MIB", "rxSAChanges"),
        ("CMM3-MIB", "rxUndersizePkts"),
        ("CMM3-MIB", "rxOversizePkts"),
        ("CMM3-MIB", "rxFragments"),
        ("CMM3-MIB", "rxJabbers"),
        ("CMM3-MIB", "rxUnicastPkts"),
        ("CMM3-MIB", "rxAlignmentErrors"),
        ("CMM3-MIB", "rxFCSErrors"),
        ("CMM3-MIB", "rxGoodOctets"),
        ("CMM3-MIB", "rxExcessSizeDisc"),
        ("CMM3-MIB", "rxPausePkts"),
        ("CMM3-MIB", "rxSymbolErrors"),
        ("CMM3-MIB", "txDropPkts"),
        ("CMM3-MIB", "txOctets"),
        ("CMM3-MIB", "txBroadcastPkts"),
        ("CMM3-MIB", "txMulticastPkts"),
        ("CMM3-MIB", "txCollisions"),
        ("CMM3-MIB", "txUnicastPkts"),
        ("CMM3-MIB", "txSingleCollision"),
        ("CMM3-MIB", "txMultipleCollision"),
        ("CMM3-MIB", "txDeferredTransmit"),
        ("CMM3-MIB", "txLateCollision"),
        ("CMM3-MIB", "txExcessiveCollision"),
        ("CMM3-MIB", "txPausePkts"),
        ("CMM3-MIB", "txFrameInDisc"),
        ("CMM3-MIB", "pkts64Octets"),
        ("CMM3-MIB", "pkts65to127Octets"),
        ("CMM3-MIB", "pkts128to255Octets"),
        ("CMM3-MIB", "pkts256to511Octets"),
        ("CMM3-MIB", "pkts512to1023Octets"),
        ("CMM3-MIB", "pkts1024to1522Octets"),
        ("CMM3-MIB", "mirSrcPortNumber"),
        ("CMM3-MIB", "mirSrcRxEnable"),
        ("CMM3-MIB", "mirSrcTxEnable"),
        ("CMM3-MIB", "portMirrorEnable"),
        ("CMM3-MIB", "mirrorCapturePort"))
)
if mibBuilder.loadTexts:
    cmmSwitchGroup.setStatus("current")

cmmConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 4, 1, 2)
)
cmmConfigGroup.setObjects(
      *(("CMM3-MIB", "gpsTimingPulse"),
        ("CMM3-MIB", "lan1Ip"),
        ("CMM3-MIB", "lan1SubnetMask"),
        ("CMM3-MIB", "defaultGateway"),
        ("CMM3-MIB", "port1PowerCtr"),
        ("CMM3-MIB", "port2PowerCtr"),
        ("CMM3-MIB", "port3PowerCtr"),
        ("CMM3-MIB", "port4PowerCtr"),
        ("CMM3-MIB", "port5PowerCtr"),
        ("CMM3-MIB", "port6PowerCtr"),
        ("CMM3-MIB", "port7PowerCtr"),
        ("CMM3-MIB", "port8PowerCtr"),
        ("CMM3-MIB", "displayOnlyAccess"),
        ("CMM3-MIB", "fullAccess"),
        ("CMM3-MIB", "displayOnlyStatus"),
        ("CMM3-MIB", "fullAccessStatus"),
        ("CMM3-MIB", "webAutoUpdate"),
        ("CMM3-MIB", "port1Config"),
        ("CMM3-MIB", "port2Config"),
        ("CMM3-MIB", "port3Config"),
        ("CMM3-MIB", "port4Config"),
        ("CMM3-MIB", "port5Config"),
        ("CMM3-MIB", "port6Config"),
        ("CMM3-MIB", "port7Config"),
        ("CMM3-MIB", "port8Config"),
        ("CMM3-MIB", "port1Description"),
        ("CMM3-MIB", "port2Description"),
        ("CMM3-MIB", "port3Description"),
        ("CMM3-MIB", "port4Description"),
        ("CMM3-MIB", "port5Description"),
        ("CMM3-MIB", "port6Description"),
        ("CMM3-MIB", "port7Description"),
        ("CMM3-MIB", "port8Description"),
        ("CMM3-MIB", "snmpTrap1"),
        ("CMM3-MIB", "snmpTrap2"),
        ("CMM3-MIB", "snmpTrap3"),
        ("CMM3-MIB", "snmpTrap4"),
        ("CMM3-MIB", "snmpTrap5"),
        ("CMM3-MIB", "snmpTrap6"),
        ("CMM3-MIB", "snmpTrap7"),
        ("CMM3-MIB", "snmpTrap8"),
        ("CMM3-MIB", "snmpTrap9"),
        ("CMM3-MIB", "snmpTrap10"),
        ("CMM3-MIB", "vlanTagEnable"),
        ("CMM3-MIB", "vlanTagId"),
        ("CMM3-MIB", "port1Uplink"),
        ("CMM3-MIB", "port2Uplink"),
        ("CMM3-MIB", "port3Uplink"),
        ("CMM3-MIB", "port4Uplink"),
        ("CMM3-MIB", "port5Uplink"),
        ("CMM3-MIB", "port6Uplink"),
        ("CMM3-MIB", "port7Uplink"),
        ("CMM3-MIB", "port8Uplink"),
        ("CMM3-MIB", "port1Management"),
        ("CMM3-MIB", "port2Management"),
        ("CMM3-MIB", "port3Management"),
        ("CMM3-MIB", "port4Management"),
        ("CMM3-MIB", "port5Management"),
        ("CMM3-MIB", "port6Management"),
        ("CMM3-MIB", "port7Management"),
        ("CMM3-MIB", "port8Management"),
        ("CMM3-MIB", "rebootIfRequired"),
        ("CMM3-MIB", "port1VlanConf"),
        ("CMM3-MIB", "port2VlanConf"),
        ("CMM3-MIB", "port3VlanConf"),
        ("CMM3-MIB", "port4VlanConf"),
        ("CMM3-MIB", "port5VlanConf"),
        ("CMM3-MIB", "port6VlanConf"),
        ("CMM3-MIB", "port7VlanConf"),
        ("CMM3-MIB", "port8VlanConf"),
        ("CMM3-MIB", "port1PwrReset"),
        ("CMM3-MIB", "port2PwrReset"),
        ("CMM3-MIB", "port3PwrReset"),
        ("CMM3-MIB", "port4PwrReset"),
        ("CMM3-MIB", "port5PwrReset"),
        ("CMM3-MIB", "port6PwrReset"),
        ("CMM3-MIB", "port7PwrReset"),
        ("CMM3-MIB", "port8PwrReset"),
        ("CMM3-MIB", "snmpReadOnly"),
        ("CMM3-MIB", "snmpCommunityString"),
        ("CMM3-MIB", "snmpAccessSubnet"),
        ("CMM3-MIB", "snmpAccessSubnet2"),
        ("CMM3-MIB", "snmpAccessSubnet3"),
        ("CMM3-MIB", "snmpAccessSubnet4"),
        ("CMM3-MIB", "snmpAccessSubnet5"),
        ("CMM3-MIB", "snmpAccessSubnet6"),
        ("CMM3-MIB", "snmpAccessSubnet7"),
        ("CMM3-MIB", "snmpAccessSubnet8"),
        ("CMM3-MIB", "snmpAccessSubnet9"),
        ("CMM3-MIB", "snmpAccessSubnet10"),
        ("CMM3-MIB", "sessionTimeout"),
        ("CMM3-MIB", "ipAccessFilterEnable"),
        ("CMM3-MIB", "allowedIPAccess1"),
        ("CMM3-MIB", "allowedIPAccess2"),
        ("CMM3-MIB", "allowedIPAccess3"),
        ("CMM3-MIB", "cmm3SnmpGPSSyncTrapEnable"),
        ("CMM3-MIB", "siteInfoViewable"),
        ("CMM3-MIB", "verifyGPSChecksum"))
)
if mibBuilder.loadTexts:
    cmmConfigGroup.setStatus("current")

cmmStatusGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 4, 1, 3)
)
cmmStatusGroup.setObjects(
      *(("CMM3-MIB", "portIndex"),
        ("CMM3-MIB", "linkStatus"),
        ("CMM3-MIB", "linkSpeed"),
        ("CMM3-MIB", "duplexStatus"),
        ("CMM3-MIB", "powerStatus"),
        ("CMM3-MIB", "uplinkStatus"),
        ("CMM3-MIB", "managementStatus"),
        ("CMM3-MIB", "deviceType"),
        ("CMM3-MIB", "pldVersion"),
        ("CMM3-MIB", "softwareVersion"),
        ("CMM3-MIB", "systemTime"),
        ("CMM3-MIB", "upTime"),
        ("CMM3-MIB", "satellitesVisible"),
        ("CMM3-MIB", "satellitesTracked"),
        ("CMM3-MIB", "latitude"),
        ("CMM3-MIB", "longitude"),
        ("CMM3-MIB", "height"),
        ("CMM3-MIB", "trackingMode"),
        ("CMM3-MIB", "syncStatus"),
        ("CMM3-MIB", "macAddress"))
)
if mibBuilder.loadTexts:
    cmmStatusGroup.setStatus("current")

cmmGPSGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 4, 1, 4)
)
cmmGPSGroup.setObjects(
      *(("CMM3-MIB", "gpsTrackingMode"),
        ("CMM3-MIB", "gpsTime"),
        ("CMM3-MIB", "gpsDate"),
        ("CMM3-MIB", "gpsSatellitesVisible"),
        ("CMM3-MIB", "gpsSatellitesTracked"),
        ("CMM3-MIB", "gpsHeight"),
        ("CMM3-MIB", "gpsAntennaConnection"),
        ("CMM3-MIB", "gpsLatitude"),
        ("CMM3-MIB", "gpsLongitude"),
        ("CMM3-MIB", "gpsInvalidMsg"),
        ("CMM3-MIB", "gpsRestartCount"),
        ("CMM3-MIB", "gpsReceiverInfo"),
        ("CMM3-MIB", "gpsReInitCount"))
)
if mibBuilder.loadTexts:
    cmmGPSGroup.setStatus("current")

cmmUserTableGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 161, 19, 3, 4, 1, 5)
)
cmmUserTableGroup.setObjects(
      *(("CMM3-MIB", "entryIndex"),
        ("CMM3-MIB", "userLoginName"),
        ("CMM3-MIB", "userPswd"),
        ("CMM3-MIB", "accessLevel"))
)
if mibBuilder.loadTexts:
    cmmUserTableGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CMM3-MIB",
    **{"cmmIIIMibModule": cmmIIIMibModule,
       "cmmGroups": cmmGroups,
       "cmmSwitchGroup": cmmSwitchGroup,
       "cmmConfigGroup": cmmConfigGroup,
       "cmmStatusGroup": cmmStatusGroup,
       "cmmGPSGroup": cmmGPSGroup,
       "cmmUserTableGroup": cmmUserTableGroup,
       "cmmSwitch": cmmSwitch,
       "cmmSwitchTable": cmmSwitchTable,
       "cmmSwitchEntry": cmmSwitchEntry,
       "portNumber": portNumber,
       "rxDropPkts": rxDropPkts,
       "rxOctets": rxOctets,
       "rxBroadcastPkts": rxBroadcastPkts,
       "rxMulticastPkts": rxMulticastPkts,
       "rxSAChanges": rxSAChanges,
       "rxUndersizePkts": rxUndersizePkts,
       "rxOversizePkts": rxOversizePkts,
       "rxFragments": rxFragments,
       "rxJabbers": rxJabbers,
       "rxUnicastPkts": rxUnicastPkts,
       "rxAlignmentErrors": rxAlignmentErrors,
       "rxFCSErrors": rxFCSErrors,
       "rxGoodOctets": rxGoodOctets,
       "rxExcessSizeDisc": rxExcessSizeDisc,
       "rxPausePkts": rxPausePkts,
       "rxSymbolErrors": rxSymbolErrors,
       "txDropPkts": txDropPkts,
       "txOctets": txOctets,
       "txBroadcastPkts": txBroadcastPkts,
       "txMulticastPkts": txMulticastPkts,
       "txCollisions": txCollisions,
       "txUnicastPkts": txUnicastPkts,
       "txSingleCollision": txSingleCollision,
       "txMultipleCollision": txMultipleCollision,
       "txDeferredTransmit": txDeferredTransmit,
       "txLateCollision": txLateCollision,
       "txExcessiveCollision": txExcessiveCollision,
       "txPausePkts": txPausePkts,
       "txFrameInDisc": txFrameInDisc,
       "pkts64Octets": pkts64Octets,
       "pkts65to127Octets": pkts65to127Octets,
       "pkts128to255Octets": pkts128to255Octets,
       "pkts256to511Octets": pkts256to511Octets,
       "pkts512to1023Octets": pkts512to1023Octets,
       "pkts1024to1522Octets": pkts1024to1522Octets,
       "portMirrorEnable": portMirrorEnable,
       "mirrorCapturePort": mirrorCapturePort,
       "cmmSwitchMirrorSrcPortsTable": cmmSwitchMirrorSrcPortsTable,
       "cmmSwitchMirrorSrcPortsEntry": cmmSwitchMirrorSrcPortsEntry,
       "mirSrcPortNumber": mirSrcPortNumber,
       "mirSrcRxEnable": mirSrcRxEnable,
       "mirSrcTxEnable": mirSrcTxEnable,
       "cmmConfig": cmmConfig,
       "gpsTimingPulse": gpsTimingPulse,
       "lan1Ip": lan1Ip,
       "lan1SubnetMask": lan1SubnetMask,
       "defaultGateway": defaultGateway,
       "port1PowerCtr": port1PowerCtr,
       "port2PowerCtr": port2PowerCtr,
       "port3PowerCtr": port3PowerCtr,
       "port4PowerCtr": port4PowerCtr,
       "port5PowerCtr": port5PowerCtr,
       "port6PowerCtr": port6PowerCtr,
       "port7PowerCtr": port7PowerCtr,
       "port8PowerCtr": port8PowerCtr,
       "displayOnlyAccess": displayOnlyAccess,
       "fullAccess": fullAccess,
       "displayOnlyStatus": displayOnlyStatus,
       "fullAccessStatus": fullAccessStatus,
       "webAutoUpdate": webAutoUpdate,
       "port1Config": port1Config,
       "port2Config": port2Config,
       "port3Config": port3Config,
       "port4Config": port4Config,
       "port5Config": port5Config,
       "port6Config": port6Config,
       "port7Config": port7Config,
       "port8Config": port8Config,
       "port1Description": port1Description,
       "port2Description": port2Description,
       "port3Description": port3Description,
       "port4Description": port4Description,
       "port5Description": port5Description,
       "port6Description": port6Description,
       "port7Description": port7Description,
       "port8Description": port8Description,
       "snmpTrap1": snmpTrap1,
       "snmpTrap2": snmpTrap2,
       "snmpTrap3": snmpTrap3,
       "snmpTrap4": snmpTrap4,
       "snmpTrap5": snmpTrap5,
       "snmpTrap6": snmpTrap6,
       "snmpTrap7": snmpTrap7,
       "snmpTrap8": snmpTrap8,
       "snmpTrap9": snmpTrap9,
       "snmpTrap10": snmpTrap10,
       "vlanTagEnable": vlanTagEnable,
       "vlanTagId": vlanTagId,
       "port1Uplink": port1Uplink,
       "port2Uplink": port2Uplink,
       "port3Uplink": port3Uplink,
       "port4Uplink": port4Uplink,
       "port5Uplink": port5Uplink,
       "port6Uplink": port6Uplink,
       "port7Uplink": port7Uplink,
       "port8Uplink": port8Uplink,
       "rebootIfRequired": rebootIfRequired,
       "port1VlanConf": port1VlanConf,
       "port2VlanConf": port2VlanConf,
       "port3VlanConf": port3VlanConf,
       "port4VlanConf": port4VlanConf,
       "port5VlanConf": port5VlanConf,
       "port6VlanConf": port6VlanConf,
       "port7VlanConf": port7VlanConf,
       "port8VlanConf": port8VlanConf,
       "port1PwrReset": port1PwrReset,
       "port2PwrReset": port2PwrReset,
       "port3PwrReset": port3PwrReset,
       "port4PwrReset": port4PwrReset,
       "port5PwrReset": port5PwrReset,
       "port6PwrReset": port6PwrReset,
       "port7PwrReset": port7PwrReset,
       "port8PwrReset": port8PwrReset,
       "snmpReadOnly": snmpReadOnly,
       "snmpCommunityString": snmpCommunityString,
       "snmpAccessSubnet": snmpAccessSubnet,
       "snmpAccessSubnet2": snmpAccessSubnet2,
       "snmpAccessSubnet3": snmpAccessSubnet3,
       "snmpAccessSubnet4": snmpAccessSubnet4,
       "snmpAccessSubnet5": snmpAccessSubnet5,
       "snmpAccessSubnet6": snmpAccessSubnet6,
       "snmpAccessSubnet7": snmpAccessSubnet7,
       "snmpAccessSubnet8": snmpAccessSubnet8,
       "snmpAccessSubnet9": snmpAccessSubnet9,
       "snmpAccessSubnet10": snmpAccessSubnet10,
       "port1Management": port1Management,
       "port2Management": port2Management,
       "port3Management": port3Management,
       "port4Management": port4Management,
       "port5Management": port5Management,
       "port6Management": port6Management,
       "port7Management": port7Management,
       "port8Management": port8Management,
       "sessionTimeout": sessionTimeout,
       "siteInfoViewable": siteInfoViewable,
       "ipAccessFilterEnable": ipAccessFilterEnable,
       "allowedIPAccess1": allowedIPAccess1,
       "allowedIPAccess2": allowedIPAccess2,
       "allowedIPAccess3": allowedIPAccess3,
       "verifyGPSChecksum": verifyGPSChecksum,
       "cmm3SnmpGPSSyncTrapEnable": cmm3SnmpGPSSyncTrapEnable,
       "cmmStatus": cmmStatus,
       "cmmPortTable": cmmPortTable,
       "cmmPortEntry": cmmPortEntry,
       "portIndex": portIndex,
       "linkStatus": linkStatus,
       "linkSpeed": linkSpeed,
       "duplexStatus": duplexStatus,
       "powerStatus": powerStatus,
       "uplinkStatus": uplinkStatus,
       "managementStatus": managementStatus,
       "deviceType": deviceType,
       "pldVersion": pldVersion,
       "softwareVersion": softwareVersion,
       "systemTime": systemTime,
       "upTime": upTime,
       "satellitesVisible": satellitesVisible,
       "satellitesTracked": satellitesTracked,
       "latitude": latitude,
       "longitude": longitude,
       "height": height,
       "trackingMode": trackingMode,
       "syncStatus": syncStatus,
       "macAddress": macAddress,
       "cmmGps": cmmGps,
       "gpsTrackingMode": gpsTrackingMode,
       "gpsTime": gpsTime,
       "gpsDate": gpsDate,
       "gpsSatellitesVisible": gpsSatellitesVisible,
       "gpsSatellitesTracked": gpsSatellitesTracked,
       "gpsHeight": gpsHeight,
       "gpsAntennaConnection": gpsAntennaConnection,
       "gpsLatitude": gpsLatitude,
       "gpsLongitude": gpsLongitude,
       "gpsInvalidMsg": gpsInvalidMsg,
       "gpsRestartCount": gpsRestartCount,
       "gpsReceiverInfo": gpsReceiverInfo,
       "gpsReInitCount": gpsReInitCount,
       "cmmEventLog": cmmEventLog,
       "eventLog": eventLog,
       "ntpLog": ntpLog,
       "cmmControls": cmmControls,
       "reboot": reboot,
       "clearEventLog": clearEventLog,
       "cmmUserTable": cmmUserTable,
       "cmmUserEntry": cmmUserEntry,
       "entryIndex": entryIndex,
       "userLoginName": userLoginName,
       "userPswd": userPswd,
       "accessLevel": accessLevel}
)
