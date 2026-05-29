# SNMP MIB module (PRVT-OSPF-EXTENSION-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\telco-systems\binos\PRVT-OSPF-EXTENSION-MIB

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

(ipSwitch,) = mibBuilder.importSymbols(
    "PRVT-SWITCH-MIB",
    "ipSwitch")

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

prvtOSPFExtensionMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 4, 2)
)
if mibBuilder.loadTexts:
    prvtOSPFExtensionMib.setRevisions(
        ("2008-01-01 00:00",
         "2005-02-16 00:00",
         "2002-11-11 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_RoutingProtocols_ObjectIdentity = ObjectIdentity
routingProtocols = _RoutingProtocols_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 4)
)
_OspfExtension_ObjectIdentity = ObjectIdentity
ospfExtension = _OspfExtension_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 4, 2, 1)
)
_OspfEnable_Type = TruthValue
_OspfEnable_Object = MibScalar
ospfEnable = _OspfEnable_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 4, 2, 1, 1),
    _OspfEnable_Type()
)
ospfEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ospfEnable.setStatus("current")
_OspfRedistributeTable_Object = MibTable
ospfRedistributeTable = _OspfRedistributeTable_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 4, 2, 1, 2)
)
if mibBuilder.loadTexts:
    ospfRedistributeTable.setStatus("current")
_OspfRedistributeEntry_Object = MibTableRow
ospfRedistributeEntry = _OspfRedistributeEntry_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 4, 2, 1, 2, 1)
)
ospfRedistributeEntry.setIndexNames(
    (0, "PRVT-OSPF-EXTENSION-MIB", "ospfRedistributeProtocol"),
)
if mibBuilder.loadTexts:
    ospfRedistributeEntry.setStatus("current")


class _OspfRedistributeProtocol_Type(Integer32):
    """Custom type ospfRedistributeProtocol based on Integer32"""
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
        *(("kernel", 1),
          ("connected", 2),
          ("static", 3),
          ("rip", 4),
          ("bgp", 5))
    )


_OspfRedistributeProtocol_Type.__name__ = "Integer32"
_OspfRedistributeProtocol_Object = MibTableColumn
ospfRedistributeProtocol = _OspfRedistributeProtocol_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 4, 2, 1, 2, 1, 1),
    _OspfRedistributeProtocol_Type()
)
ospfRedistributeProtocol.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ospfRedistributeProtocol.setStatus("current")


class _OspfRedistributeMetric_Type(Integer32):
    """Custom type ospfRedistributeMetric based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16777214),
    )


_OspfRedistributeMetric_Type.__name__ = "Integer32"
_OspfRedistributeMetric_Object = MibTableColumn
ospfRedistributeMetric = _OspfRedistributeMetric_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 4, 2, 1, 2, 1, 2),
    _OspfRedistributeMetric_Type()
)
ospfRedistributeMetric.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ospfRedistributeMetric.setStatus("current")


class _OspfRedistributeMetricType_Type(Integer32):
    """Custom type ospfRedistributeMetricType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("e1", 1),
          ("e2", 2))
    )


_OspfRedistributeMetricType_Type.__name__ = "Integer32"
_OspfRedistributeMetricType_Object = MibTableColumn
ospfRedistributeMetricType = _OspfRedistributeMetricType_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 4, 2, 1, 2, 1, 3),
    _OspfRedistributeMetricType_Type()
)
ospfRedistributeMetricType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ospfRedistributeMetricType.setStatus("current")
_OspfRedistributeRouteMap_Type = OctetString
_OspfRedistributeRouteMap_Object = MibTableColumn
ospfRedistributeRouteMap = _OspfRedistributeRouteMap_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 4, 2, 1, 2, 1, 4),
    _OspfRedistributeRouteMap_Type()
)
ospfRedistributeRouteMap.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ospfRedistributeRouteMap.setStatus("current")
_OspfRedistributeRowStatus_Type = RowStatus
_OspfRedistributeRowStatus_Object = MibTableColumn
ospfRedistributeRowStatus = _OspfRedistributeRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 4, 2, 1, 2, 1, 5),
    _OspfRedistributeRowStatus_Type()
)
ospfRedistributeRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ospfRedistributeRowStatus.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "PRVT-OSPF-EXTENSION-MIB",
    **{"routingProtocols": routingProtocols,
       "prvtOSPFExtensionMib": prvtOSPFExtensionMib,
       "ospfExtension": ospfExtension,
       "ospfEnable": ospfEnable,
       "ospfRedistributeTable": ospfRedistributeTable,
       "ospfRedistributeEntry": ospfRedistributeEntry,
       "ospfRedistributeProtocol": ospfRedistributeProtocol,
       "ospfRedistributeMetric": ospfRedistributeMetric,
       "ospfRedistributeMetricType": ospfRedistributeMetricType,
       "ospfRedistributeRouteMap": ospfRedistributeRouteMap,
       "ospfRedistributeRowStatus": ospfRedistributeRowStatus}
)
