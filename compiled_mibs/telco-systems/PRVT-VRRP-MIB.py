# SNMP MIB module (PRVT-VRRP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\telco-systems\binox\PRVT-VRRP-MIB

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

(switch,) = mibBuilder.importSymbols(
    "PRVT-SWITCH-MIB",
    "switch")

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

prvtVrrpMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 167)
)
if mibBuilder.loadTexts:
    prvtVrrpMIB.setRevisions(
        ("2014-11-10 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_PrvtVrrpObjects_ObjectIdentity = ObjectIdentity
prvtVrrpObjects = _PrvtVrrpObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 167, 1)
)
_PrvtVrrpVirtualRouterTable_Object = MibTable
prvtVrrpVirtualRouterTable = _PrvtVrrpVirtualRouterTable_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 167, 1, 1)
)
if mibBuilder.loadTexts:
    prvtVrrpVirtualRouterTable.setStatus("current")
_PrvtVrrpVirtualRouterEntry_Object = MibTableRow
prvtVrrpVirtualRouterEntry = _PrvtVrrpVirtualRouterEntry_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 167, 1, 1, 1)
)
prvtVrrpVirtualRouterEntry.setIndexNames(
    (0, "PRVT-VRRP-MIB", "prvtVrrpVirtualRouterId"),
)
if mibBuilder.loadTexts:
    prvtVrrpVirtualRouterEntry.setStatus("current")


class _PrvtVrrpVirtualRouterId_Type(Unsigned32):
    """Custom type prvtVrrpVirtualRouterId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_PrvtVrrpVirtualRouterId_Type.__name__ = "Unsigned32"
_PrvtVrrpVirtualRouterId_Object = MibTableColumn
prvtVrrpVirtualRouterId = _PrvtVrrpVirtualRouterId_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 167, 1, 1, 1, 1),
    _PrvtVrrpVirtualRouterId_Type()
)
prvtVrrpVirtualRouterId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    prvtVrrpVirtualRouterId.setStatus("current")
_PrvtVrrpVirtualRouterRowStatus_Type = RowStatus
_PrvtVrrpVirtualRouterRowStatus_Object = MibTableColumn
prvtVrrpVirtualRouterRowStatus = _PrvtVrrpVirtualRouterRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 167, 1, 1, 1, 2),
    _PrvtVrrpVirtualRouterRowStatus_Type()
)
prvtVrrpVirtualRouterRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    prvtVrrpVirtualRouterRowStatus.setStatus("current")
_PrvtVrrpVirtualRouterShutdown_Type = TruthValue
_PrvtVrrpVirtualRouterShutdown_Object = MibTableColumn
prvtVrrpVirtualRouterShutdown = _PrvtVrrpVirtualRouterShutdown_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 167, 1, 1, 1, 3),
    _PrvtVrrpVirtualRouterShutdown_Type()
)
prvtVrrpVirtualRouterShutdown.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    prvtVrrpVirtualRouterShutdown.setStatus("current")
_PrvtVrrpVirtualRouterPreempt_Type = TruthValue
_PrvtVrrpVirtualRouterPreempt_Object = MibTableColumn
prvtVrrpVirtualRouterPreempt = _PrvtVrrpVirtualRouterPreempt_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 167, 1, 1, 1, 4),
    _PrvtVrrpVirtualRouterPreempt_Type()
)
prvtVrrpVirtualRouterPreempt.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    prvtVrrpVirtualRouterPreempt.setStatus("current")


class _PrvtVrrpVirtualRouterPriority_Type(Unsigned32):
    """Custom type prvtVrrpVirtualRouterPriority based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 254),
    )


_PrvtVrrpVirtualRouterPriority_Type.__name__ = "Unsigned32"
_PrvtVrrpVirtualRouterPriority_Object = MibTableColumn
prvtVrrpVirtualRouterPriority = _PrvtVrrpVirtualRouterPriority_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 167, 1, 1, 1, 5),
    _PrvtVrrpVirtualRouterPriority_Type()
)
prvtVrrpVirtualRouterPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    prvtVrrpVirtualRouterPriority.setStatus("current")


class _PrvtVrrpVirtualRouterVersion_Type(Unsigned32):
    """Custom type prvtVrrpVirtualRouterVersion based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_PrvtVrrpVirtualRouterVersion_Type.__name__ = "Unsigned32"
_PrvtVrrpVirtualRouterVersion_Object = MibTableColumn
prvtVrrpVirtualRouterVersion = _PrvtVrrpVirtualRouterVersion_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 167, 1, 1, 1, 6),
    _PrvtVrrpVirtualRouterVersion_Type()
)
prvtVrrpVirtualRouterVersion.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    prvtVrrpVirtualRouterVersion.setStatus("current")


class _PrvtVrrpVirtualRouterAdvertisedInterval_Type(Unsigned32):
    """Custom type prvtVrrpVirtualRouterAdvertisedInterval based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(10, 4095),
    )


_PrvtVrrpVirtualRouterAdvertisedInterval_Type.__name__ = "Unsigned32"
_PrvtVrrpVirtualRouterAdvertisedInterval_Object = MibTableColumn
prvtVrrpVirtualRouterAdvertisedInterval = _PrvtVrrpVirtualRouterAdvertisedInterval_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 167, 1, 1, 1, 7),
    _PrvtVrrpVirtualRouterAdvertisedInterval_Type()
)
prvtVrrpVirtualRouterAdvertisedInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    prvtVrrpVirtualRouterAdvertisedInterval.setStatus("current")


class _PrvtVrrpVirtualRouterAcceptMode_Type(Integer32):
    """Custom type prvtVrrpVirtualRouterAcceptMode based on Integer32"""
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
          ("icmp", 1),
          ("all", 2))
    )


_PrvtVrrpVirtualRouterAcceptMode_Type.__name__ = "Integer32"
_PrvtVrrpVirtualRouterAcceptMode_Object = MibTableColumn
prvtVrrpVirtualRouterAcceptMode = _PrvtVrrpVirtualRouterAcceptMode_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 167, 1, 1, 1, 8),
    _PrvtVrrpVirtualRouterAcceptMode_Type()
)
prvtVrrpVirtualRouterAcceptMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    prvtVrrpVirtualRouterAcceptMode.setStatus("current")
_PrvtVrrpVirtualRouterInterface_Type = OctetString
_PrvtVrrpVirtualRouterInterface_Object = MibTableColumn
prvtVrrpVirtualRouterInterface = _PrvtVrrpVirtualRouterInterface_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 167, 1, 1, 1, 9),
    _PrvtVrrpVirtualRouterInterface_Type()
)
prvtVrrpVirtualRouterInterface.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    prvtVrrpVirtualRouterInterface.setStatus("current")


class _PrvtVrrpVirtualRouterTraceUplinkThreshold_Type(Unsigned32):
    """Custom type prvtVrrpVirtualRouterTraceUplinkThreshold based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_PrvtVrrpVirtualRouterTraceUplinkThreshold_Type.__name__ = "Unsigned32"
_PrvtVrrpVirtualRouterTraceUplinkThreshold_Object = MibTableColumn
prvtVrrpVirtualRouterTraceUplinkThreshold = _PrvtVrrpVirtualRouterTraceUplinkThreshold_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 167, 1, 1, 1, 10),
    _PrvtVrrpVirtualRouterTraceUplinkThreshold_Type()
)
prvtVrrpVirtualRouterTraceUplinkThreshold.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    prvtVrrpVirtualRouterTraceUplinkThreshold.setStatus("current")


class _PrvtVrrpVirtualRouterTraceUplinkFlushTimer_Type(Unsigned32):
    """Custom type prvtVrrpVirtualRouterTraceUplinkFlushTimer based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 101),
    )


_PrvtVrrpVirtualRouterTraceUplinkFlushTimer_Type.__name__ = "Unsigned32"
_PrvtVrrpVirtualRouterTraceUplinkFlushTimer_Object = MibTableColumn
prvtVrrpVirtualRouterTraceUplinkFlushTimer = _PrvtVrrpVirtualRouterTraceUplinkFlushTimer_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 167, 1, 1, 1, 11),
    _PrvtVrrpVirtualRouterTraceUplinkFlushTimer_Type()
)
prvtVrrpVirtualRouterTraceUplinkFlushTimer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    prvtVrrpVirtualRouterTraceUplinkFlushTimer.setStatus("current")


class _PrvtVrrpVirtualRouterStateVrrp_Type(Integer32):
    """Custom type prvtVrrpVirtualRouterStateVrrp based on Integer32"""
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
        *(("init", 1),
          ("backup", 2),
          ("master", 3),
          ("initWait", 4),
          ("none", 5))
    )


_PrvtVrrpVirtualRouterStateVrrp_Type.__name__ = "Integer32"
_PrvtVrrpVirtualRouterStateVrrp_Object = MibTableColumn
prvtVrrpVirtualRouterStateVrrp = _PrvtVrrpVirtualRouterStateVrrp_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 167, 1, 1, 1, 12),
    _PrvtVrrpVirtualRouterStateVrrp_Type()
)
prvtVrrpVirtualRouterStateVrrp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prvtVrrpVirtualRouterStateVrrp.setStatus("current")
_PrvtVrrpVirtualIpAddressTable_Object = MibTable
prvtVrrpVirtualIpAddressTable = _PrvtVrrpVirtualIpAddressTable_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 167, 1, 2)
)
if mibBuilder.loadTexts:
    prvtVrrpVirtualIpAddressTable.setStatus("current")
_PrvtVrrpVirtualIpAddressEntry_Object = MibTableRow
prvtVrrpVirtualIpAddressEntry = _PrvtVrrpVirtualIpAddressEntry_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 167, 1, 2, 1)
)
prvtVrrpVirtualIpAddressEntry.setIndexNames(
    (0, "PRVT-VRRP-MIB", "prvtVrrpVirtualRouterId"),
    (0, "PRVT-VRRP-MIB", "prvtVrrpVirtualIpAddress"),
)
if mibBuilder.loadTexts:
    prvtVrrpVirtualIpAddressEntry.setStatus("current")
_PrvtVrrpVirtualIpAddress_Type = IpAddress
_PrvtVrrpVirtualIpAddress_Object = MibTableColumn
prvtVrrpVirtualIpAddress = _PrvtVrrpVirtualIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 167, 1, 2, 1, 1),
    _PrvtVrrpVirtualIpAddress_Type()
)
prvtVrrpVirtualIpAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    prvtVrrpVirtualIpAddress.setStatus("current")
_PrvtVrrpVirtualIpAddressRowStatus_Type = RowStatus
_PrvtVrrpVirtualIpAddressRowStatus_Object = MibTableColumn
prvtVrrpVirtualIpAddressRowStatus = _PrvtVrrpVirtualIpAddressRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 167, 1, 2, 1, 2),
    _PrvtVrrpVirtualIpAddressRowStatus_Type()
)
prvtVrrpVirtualIpAddressRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    prvtVrrpVirtualIpAddressRowStatus.setStatus("current")


class _PrvtVrrpVirtualIpAddressRange_Type(Unsigned32):
    """Custom type prvtVrrpVirtualIpAddressRange based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10),
    )


_PrvtVrrpVirtualIpAddressRange_Type.__name__ = "Unsigned32"
_PrvtVrrpVirtualIpAddressRange_Object = MibTableColumn
prvtVrrpVirtualIpAddressRange = _PrvtVrrpVirtualIpAddressRange_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 167, 1, 2, 1, 3),
    _PrvtVrrpVirtualIpAddressRange_Type()
)
prvtVrrpVirtualIpAddressRange.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    prvtVrrpVirtualIpAddressRange.setStatus("current")
_PrvtVrrpTraceUplinkTable_Object = MibTable
prvtVrrpTraceUplinkTable = _PrvtVrrpTraceUplinkTable_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 167, 1, 3)
)
if mibBuilder.loadTexts:
    prvtVrrpTraceUplinkTable.setStatus("current")
_PrvtVrrpTraceUplinkEntry_Object = MibTableRow
prvtVrrpTraceUplinkEntry = _PrvtVrrpTraceUplinkEntry_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 167, 1, 3, 1)
)
prvtVrrpTraceUplinkEntry.setIndexNames(
    (0, "PRVT-VRRP-MIB", "prvtVrrpVirtualRouterId"),
    (0, "PRVT-VRRP-MIB", "prvtVrrpTraceUplinkName"),
)
if mibBuilder.loadTexts:
    prvtVrrpTraceUplinkEntry.setStatus("current")
_PrvtVrrpTraceUplinkName_Type = OctetString
_PrvtVrrpTraceUplinkName_Object = MibTableColumn
prvtVrrpTraceUplinkName = _PrvtVrrpTraceUplinkName_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 167, 1, 3, 1, 1),
    _PrvtVrrpTraceUplinkName_Type()
)
prvtVrrpTraceUplinkName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    prvtVrrpTraceUplinkName.setStatus("current")
_PrvtVrrpTraceUplinkRowStatus_Type = RowStatus
_PrvtVrrpTraceUplinkRowStatus_Object = MibTableColumn
prvtVrrpTraceUplinkRowStatus = _PrvtVrrpTraceUplinkRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 167, 1, 3, 1, 2),
    _PrvtVrrpTraceUplinkRowStatus_Type()
)
prvtVrrpTraceUplinkRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    prvtVrrpTraceUplinkRowStatus.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "PRVT-VRRP-MIB",
    **{"prvtVrrpMIB": prvtVrrpMIB,
       "prvtVrrpObjects": prvtVrrpObjects,
       "prvtVrrpVirtualRouterTable": prvtVrrpVirtualRouterTable,
       "prvtVrrpVirtualRouterEntry": prvtVrrpVirtualRouterEntry,
       "prvtVrrpVirtualRouterId": prvtVrrpVirtualRouterId,
       "prvtVrrpVirtualRouterRowStatus": prvtVrrpVirtualRouterRowStatus,
       "prvtVrrpVirtualRouterShutdown": prvtVrrpVirtualRouterShutdown,
       "prvtVrrpVirtualRouterPreempt": prvtVrrpVirtualRouterPreempt,
       "prvtVrrpVirtualRouterPriority": prvtVrrpVirtualRouterPriority,
       "prvtVrrpVirtualRouterVersion": prvtVrrpVirtualRouterVersion,
       "prvtVrrpVirtualRouterAdvertisedInterval": prvtVrrpVirtualRouterAdvertisedInterval,
       "prvtVrrpVirtualRouterAcceptMode": prvtVrrpVirtualRouterAcceptMode,
       "prvtVrrpVirtualRouterInterface": prvtVrrpVirtualRouterInterface,
       "prvtVrrpVirtualRouterTraceUplinkThreshold": prvtVrrpVirtualRouterTraceUplinkThreshold,
       "prvtVrrpVirtualRouterTraceUplinkFlushTimer": prvtVrrpVirtualRouterTraceUplinkFlushTimer,
       "prvtVrrpVirtualRouterStateVrrp": prvtVrrpVirtualRouterStateVrrp,
       "prvtVrrpVirtualIpAddressTable": prvtVrrpVirtualIpAddressTable,
       "prvtVrrpVirtualIpAddressEntry": prvtVrrpVirtualIpAddressEntry,
       "prvtVrrpVirtualIpAddress": prvtVrrpVirtualIpAddress,
       "prvtVrrpVirtualIpAddressRowStatus": prvtVrrpVirtualIpAddressRowStatus,
       "prvtVrrpVirtualIpAddressRange": prvtVrrpVirtualIpAddressRange,
       "prvtVrrpTraceUplinkTable": prvtVrrpTraceUplinkTable,
       "prvtVrrpTraceUplinkEntry": prvtVrrpTraceUplinkEntry,
       "prvtVrrpTraceUplinkName": prvtVrrpTraceUplinkName,
       "prvtVrrpTraceUplinkRowStatus": prvtVrrpTraceUplinkRowStatus}
)
