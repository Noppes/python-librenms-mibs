# SNMP MIB module (PRVT-RIP-EXTENSION-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\telco-systems\binos\PRVT-RIP-EXTENSION-MIB

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

prvtRIPExtensionMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 4, 1)
)
if mibBuilder.loadTexts:
    prvtRIPExtensionMib.setRevisions(
        ("2008-01-01 00:00",
         "2005-02-16 00:00",
         "2003-05-06 00:00",
         "2002-11-11 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_RoutingProtocols_ObjectIdentity = ObjectIdentity
routingProtocols = _RoutingProtocols_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 4)
)
_RipExtension_ObjectIdentity = ObjectIdentity
ripExtension = _RipExtension_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 4, 1, 1)
)
_RipEnable_Type = TruthValue
_RipEnable_Object = MibScalar
ripEnable = _RipEnable_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 4, 1, 1, 1),
    _RipEnable_Type()
)
ripEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ripEnable.setStatus("current")
_RipRedistributeTable_Object = MibTable
ripRedistributeTable = _RipRedistributeTable_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 4, 1, 1, 2)
)
if mibBuilder.loadTexts:
    ripRedistributeTable.setStatus("current")
_RipRedistributeEntry_Object = MibTableRow
ripRedistributeEntry = _RipRedistributeEntry_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 4, 1, 1, 2, 1)
)
ripRedistributeEntry.setIndexNames(
    (0, "PRVT-RIP-EXTENSION-MIB", "ripRedistributeProtocol"),
)
if mibBuilder.loadTexts:
    ripRedistributeEntry.setStatus("current")


class _RipRedistributeProtocol_Type(Integer32):
    """Custom type ripRedistributeProtocol based on Integer32"""
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
          ("ospf", 4),
          ("bgp", 5))
    )


_RipRedistributeProtocol_Type.__name__ = "Integer32"
_RipRedistributeProtocol_Object = MibTableColumn
ripRedistributeProtocol = _RipRedistributeProtocol_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 4, 1, 1, 2, 1, 1),
    _RipRedistributeProtocol_Type()
)
ripRedistributeProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ripRedistributeProtocol.setStatus("current")


class _RipRedistributeMetric_Type(Integer32):
    """Custom type ripRedistributeMetric based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_RipRedistributeMetric_Type.__name__ = "Integer32"
_RipRedistributeMetric_Object = MibTableColumn
ripRedistributeMetric = _RipRedistributeMetric_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 4, 1, 1, 2, 1, 2),
    _RipRedistributeMetric_Type()
)
ripRedistributeMetric.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ripRedistributeMetric.setStatus("current")
_RipRedistributeRouteMap_Type = OctetString
_RipRedistributeRouteMap_Object = MibTableColumn
ripRedistributeRouteMap = _RipRedistributeRouteMap_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 4, 1, 1, 2, 1, 3),
    _RipRedistributeRouteMap_Type()
)
ripRedistributeRouteMap.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ripRedistributeRouteMap.setStatus("current")
_RipRedistributeRowStatus_Type = RowStatus
_RipRedistributeRowStatus_Object = MibTableColumn
ripRedistributeRowStatus = _RipRedistributeRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 6, 4, 1, 1, 2, 1, 4),
    _RipRedistributeRowStatus_Type()
)
ripRedistributeRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ripRedistributeRowStatus.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "PRVT-RIP-EXTENSION-MIB",
    **{"routingProtocols": routingProtocols,
       "prvtRIPExtensionMib": prvtRIPExtensionMib,
       "ripExtension": ripExtension,
       "ripEnable": ripEnable,
       "ripRedistributeTable": ripRedistributeTable,
       "ripRedistributeEntry": ripRedistributeEntry,
       "ripRedistributeProtocol": ripRedistributeProtocol,
       "ripRedistributeMetric": ripRedistributeMetric,
       "ripRedistributeRouteMap": ripRedistributeRouteMap,
       "ripRedistributeRowStatus": ripRedistributeRowStatus}
)
