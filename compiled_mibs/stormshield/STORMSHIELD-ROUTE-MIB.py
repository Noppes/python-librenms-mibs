# SNMP MIB module (STORMSHIELD-ROUTE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\stormshield\STORMSHIELD-ROUTE-MIB

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

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

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

(stormshieldMIB,) = mibBuilder.importSymbols(
    "STORMSHIELD-SMI-MIB",
    "stormshieldMIB")


# MODULE-IDENTITY

snsRoute = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 11256, 1, 14)
)
if mibBuilder.loadTexts:
    snsRoute.setRevisions(
        ("2021-06-03 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_SnsRouteTable_Object = MibTable
snsRouteTable = _SnsRouteTable_Object(
    (1, 3, 6, 1, 4, 1, 11256, 1, 14, 1)
)
if mibBuilder.loadTexts:
    snsRouteTable.setStatus("current")
_SnsRouteEntry_Object = MibTableRow
snsRouteEntry = _SnsRouteEntry_Object(
    (1, 3, 6, 1, 4, 1, 11256, 1, 14, 1, 1)
)
snsRouteEntry.setIndexNames(
    (0, "STORMSHIELD-ROUTE-MIB", "snsRouteIndex"),
)
if mibBuilder.loadTexts:
    snsRouteEntry.setStatus("current")


class _SnsRouteIndex_Type(Integer32):
    """Custom type snsRouteIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_SnsRouteIndex_Type.__name__ = "Integer32"
_SnsRouteIndex_Object = MibTableColumn
snsRouteIndex = _SnsRouteIndex_Object(
    (1, 3, 6, 1, 4, 1, 11256, 1, 14, 1, 1, 1),
    _SnsRouteIndex_Type()
)
snsRouteIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snsRouteIndex.setStatus("current")
_SnsRouteType_Type = DisplayString
_SnsRouteType_Object = MibTableColumn
snsRouteType = _SnsRouteType_Object(
    (1, 3, 6, 1, 4, 1, 11256, 1, 14, 1, 1, 2),
    _SnsRouteType_Type()
)
snsRouteType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snsRouteType.setStatus("current")
_SnsRouteIPVersion_Type = Integer32
_SnsRouteIPVersion_Object = MibTableColumn
snsRouteIPVersion = _SnsRouteIPVersion_Object(
    (1, 3, 6, 1, 4, 1, 11256, 1, 14, 1, 1, 3),
    _SnsRouteIPVersion_Type()
)
snsRouteIPVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snsRouteIPVersion.setStatus("current")
_SnsRouteRouterName_Type = SnmpAdminString
_SnsRouteRouterName_Object = MibTableColumn
snsRouteRouterName = _SnsRouteRouterName_Object(
    (1, 3, 6, 1, 4, 1, 11256, 1, 14, 1, 1, 4),
    _SnsRouteRouterName_Type()
)
snsRouteRouterName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snsRouteRouterName.setStatus("current")
_SnsRouteGatewayName_Type = SnmpAdminString
_SnsRouteGatewayName_Object = MibTableColumn
snsRouteGatewayName = _SnsRouteGatewayName_Object(
    (1, 3, 6, 1, 4, 1, 11256, 1, 14, 1, 1, 5),
    _SnsRouteGatewayName_Type()
)
snsRouteGatewayName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snsRouteGatewayName.setStatus("current")
_SnsRouteGatewayAddr_Type = DisplayString
_SnsRouteGatewayAddr_Object = MibTableColumn
snsRouteGatewayAddr = _SnsRouteGatewayAddr_Object(
    (1, 3, 6, 1, 4, 1, 11256, 1, 14, 1, 1, 6),
    _SnsRouteGatewayAddr_Type()
)
snsRouteGatewayAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snsRouteGatewayAddr.setStatus("current")
_SnsRouteGatewayType_Type = DisplayString
_SnsRouteGatewayType_Object = MibTableColumn
snsRouteGatewayType = _SnsRouteGatewayType_Object(
    (1, 3, 6, 1, 4, 1, 11256, 1, 14, 1, 1, 7),
    _SnsRouteGatewayType_Type()
)
snsRouteGatewayType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snsRouteGatewayType.setStatus("current")
_SnsRouteLastCheck_Type = DisplayString
_SnsRouteLastCheck_Object = MibTableColumn
snsRouteLastCheck = _SnsRouteLastCheck_Object(
    (1, 3, 6, 1, 4, 1, 11256, 1, 14, 1, 1, 8),
    _SnsRouteLastCheck_Type()
)
snsRouteLastCheck.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snsRouteLastCheck.setStatus("current")
_SnsRouteState_Type = DisplayString
_SnsRouteState_Object = MibTableColumn
snsRouteState = _SnsRouteState_Object(
    (1, 3, 6, 1, 4, 1, 11256, 1, 14, 1, 1, 9),
    _SnsRouteState_Type()
)
snsRouteState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snsRouteState.setStatus("current")
_SnsRouteStateLastChange_Type = DisplayString
_SnsRouteStateLastChange_Object = MibTableColumn
snsRouteStateLastChange = _SnsRouteStateLastChange_Object(
    (1, 3, 6, 1, 4, 1, 11256, 1, 14, 1, 1, 10),
    _SnsRouteStateLastChange_Type()
)
snsRouteStateLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snsRouteStateLastChange.setStatus("current")
_SnsRouteActive_Type = Integer32
_SnsRouteActive_Object = MibTableColumn
snsRouteActive = _SnsRouteActive_Object(
    (1, 3, 6, 1, 4, 1, 11256, 1, 14, 1, 1, 11),
    _SnsRouteActive_Type()
)
snsRouteActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snsRouteActive.setStatus("current")
_SnsRouteActiveLastChange_Type = DisplayString
_SnsRouteActiveLastChange_Object = MibTableColumn
snsRouteActiveLastChange = _SnsRouteActiveLastChange_Object(
    (1, 3, 6, 1, 4, 1, 11256, 1, 14, 1, 1, 12),
    _SnsRouteActiveLastChange_Type()
)
snsRouteActiveLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snsRouteActiveLastChange.setStatus("current")
_SnsRouteSysDefaultGateway_Type = Integer32
_SnsRouteSysDefaultGateway_Object = MibTableColumn
snsRouteSysDefaultGateway = _SnsRouteSysDefaultGateway_Object(
    (1, 3, 6, 1, 4, 1, 11256, 1, 14, 1, 1, 13),
    _SnsRouteSysDefaultGateway_Type()
)
snsRouteSysDefaultGateway.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snsRouteSysDefaultGateway.setStatus("current")
_SnsRouteSysDefaultGatewayLastChange_Type = DisplayString
_SnsRouteSysDefaultGatewayLastChange_Object = MibTableColumn
snsRouteSysDefaultGatewayLastChange = _SnsRouteSysDefaultGatewayLastChange_Object(
    (1, 3, 6, 1, 4, 1, 11256, 1, 14, 1, 1, 14),
    _SnsRouteSysDefaultGatewayLastChange_Type()
)
snsRouteSysDefaultGatewayLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snsRouteSysDefaultGatewayLastChange.setStatus("current")
_SnsRouteRtid_Type = Integer32
_SnsRouteRtid_Object = MibTableColumn
snsRouteRtid = _SnsRouteRtid_Object(
    (1, 3, 6, 1, 4, 1, 11256, 1, 14, 1, 1, 15),
    _SnsRouteRtid_Type()
)
snsRouteRtid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snsRouteRtid.setStatus("current")
_SnsRouteUsagePrct_Type = DisplayString
_SnsRouteUsagePrct_Object = MibTableColumn
snsRouteUsagePrct = _SnsRouteUsagePrct_Object(
    (1, 3, 6, 1, 4, 1, 11256, 1, 14, 1, 1, 16),
    _SnsRouteUsagePrct_Type()
)
snsRouteUsagePrct.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snsRouteUsagePrct.setStatus("current")
_SnsRouteMonitoringMethod_Type = DisplayString
_SnsRouteMonitoringMethod_Object = MibTableColumn
snsRouteMonitoringMethod = _SnsRouteMonitoringMethod_Object(
    (1, 3, 6, 1, 4, 1, 11256, 1, 14, 1, 1, 17),
    _SnsRouteMonitoringMethod_Type()
)
snsRouteMonitoringMethod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snsRouteMonitoringMethod.setStatus("current")
_SnsRouteLatency_Type = Unsigned32
_SnsRouteLatency_Object = MibTableColumn
snsRouteLatency = _SnsRouteLatency_Object(
    (1, 3, 6, 1, 4, 1, 11256, 1, 14, 1, 1, 18),
    _SnsRouteLatency_Type()
)
snsRouteLatency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snsRouteLatency.setStatus("current")
_SnsRouteJitter_Type = Unsigned32
_SnsRouteJitter_Object = MibTableColumn
snsRouteJitter = _SnsRouteJitter_Object(
    (1, 3, 6, 1, 4, 1, 11256, 1, 14, 1, 1, 19),
    _SnsRouteJitter_Type()
)
snsRouteJitter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snsRouteJitter.setStatus("current")
_SnsRoutePacketLossPrct_Type = DisplayString
_SnsRoutePacketLossPrct_Object = MibTableColumn
snsRoutePacketLossPrct = _SnsRoutePacketLossPrct_Object(
    (1, 3, 6, 1, 4, 1, 11256, 1, 14, 1, 1, 20),
    _SnsRoutePacketLossPrct_Type()
)
snsRoutePacketLossPrct.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snsRoutePacketLossPrct.setStatus("current")
_SnsRouteUnreachPrct_Type = DisplayString
_SnsRouteUnreachPrct_Object = MibTableColumn
snsRouteUnreachPrct = _SnsRouteUnreachPrct_Object(
    (1, 3, 6, 1, 4, 1, 11256, 1, 14, 1, 1, 21),
    _SnsRouteUnreachPrct_Type()
)
snsRouteUnreachPrct.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snsRouteUnreachPrct.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "STORMSHIELD-ROUTE-MIB",
    **{"snsRoute": snsRoute,
       "snsRouteTable": snsRouteTable,
       "snsRouteEntry": snsRouteEntry,
       "snsRouteIndex": snsRouteIndex,
       "snsRouteType": snsRouteType,
       "snsRouteIPVersion": snsRouteIPVersion,
       "snsRouteRouterName": snsRouteRouterName,
       "snsRouteGatewayName": snsRouteGatewayName,
       "snsRouteGatewayAddr": snsRouteGatewayAddr,
       "snsRouteGatewayType": snsRouteGatewayType,
       "snsRouteLastCheck": snsRouteLastCheck,
       "snsRouteState": snsRouteState,
       "snsRouteStateLastChange": snsRouteStateLastChange,
       "snsRouteActive": snsRouteActive,
       "snsRouteActiveLastChange": snsRouteActiveLastChange,
       "snsRouteSysDefaultGateway": snsRouteSysDefaultGateway,
       "snsRouteSysDefaultGatewayLastChange": snsRouteSysDefaultGatewayLastChange,
       "snsRouteRtid": snsRouteRtid,
       "snsRouteUsagePrct": snsRouteUsagePrct,
       "snsRouteMonitoringMethod": snsRouteMonitoringMethod,
       "snsRouteLatency": snsRouteLatency,
       "snsRouteJitter": snsRouteJitter,
       "snsRoutePacketLossPrct": snsRoutePacketLossPrct,
       "snsRouteUnreachPrct": snsRouteUnreachPrct}
)
