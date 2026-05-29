# SNMP MIB module (PRVT-STORM-CTL-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\telco-systems\binox\PRVT-STORM-CTL-MIB

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

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

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

prvtStormCtlMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 171)
)
if mibBuilder.loadTexts:
    prvtStormCtlMIB.setRevisions(
        ("2010-06-21 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class RateThresholdType(TextualConvention, Unsigned32):
    status = "current"
    displayHint = "d"


# MIB Managed Objects in the order of their OIDs

_PrvtStormCtlMIBObjects_ObjectIdentity = ObjectIdentity
prvtStormCtlMIBObjects = _PrvtStormCtlMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 171, 1)
)
_PrvtStrmCtlPortTable_Object = MibTable
prvtStrmCtlPortTable = _PrvtStrmCtlPortTable_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 171, 1, 1)
)
if mibBuilder.loadTexts:
    prvtStrmCtlPortTable.setStatus("current")
_PrvtStrmCtlPortEntry_Object = MibTableRow
prvtStrmCtlPortEntry = _PrvtStrmCtlPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 171, 1, 1, 1)
)
prvtStrmCtlPortEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    prvtStrmCtlPortEntry.setStatus("current")
_PrvtStrmCtlPortRowStatus_Type = RowStatus
_PrvtStrmCtlPortRowStatus_Object = MibTableColumn
prvtStrmCtlPortRowStatus = _PrvtStrmCtlPortRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 171, 1, 1, 1, 1),
    _PrvtStrmCtlPortRowStatus_Type()
)
prvtStrmCtlPortRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    prvtStrmCtlPortRowStatus.setStatus("current")
_PrvtStrmCtlPortShutdown_Type = TruthValue
_PrvtStrmCtlPortShutdown_Object = MibTableColumn
prvtStrmCtlPortShutdown = _PrvtStrmCtlPortShutdown_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 171, 1, 1, 1, 3),
    _PrvtStrmCtlPortShutdown_Type()
)
prvtStrmCtlPortShutdown.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    prvtStrmCtlPortShutdown.setStatus("current")
_PrvtStrmCtlPortTrafficTable_Object = MibTable
prvtStrmCtlPortTrafficTable = _PrvtStrmCtlPortTrafficTable_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 171, 1, 3)
)
if mibBuilder.loadTexts:
    prvtStrmCtlPortTrafficTable.setStatus("current")
_PrvtStrmCtlPortTrafficEntry_Object = MibTableRow
prvtStrmCtlPortTrafficEntry = _PrvtStrmCtlPortTrafficEntry_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 171, 1, 3, 1)
)
prvtStrmCtlPortTrafficEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "PRVT-STORM-CTL-MIB", "prvtStrmCtlPortTrafficType"),
)
if mibBuilder.loadTexts:
    prvtStrmCtlPortTrafficEntry.setStatus("current")


class _PrvtStrmCtlPortTrafficType_Type(Integer32):
    """Custom type prvtStrmCtlPortTrafficType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              4)
        )
    )
    namedValues = NamedValues(
        *(("all", 0),
          ("unknown", 1),
          ("multicast", 2),
          ("broadcast", 4))
    )


_PrvtStrmCtlPortTrafficType_Type.__name__ = "Integer32"
_PrvtStrmCtlPortTrafficType_Object = MibTableColumn
prvtStrmCtlPortTrafficType = _PrvtStrmCtlPortTrafficType_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 171, 1, 3, 1, 1),
    _PrvtStrmCtlPortTrafficType_Type()
)
prvtStrmCtlPortTrafficType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    prvtStrmCtlPortTrafficType.setStatus("current")
_PrvtStrmCtlPortTrafficRowStatus_Type = RowStatus
_PrvtStrmCtlPortTrafficRowStatus_Object = MibTableColumn
prvtStrmCtlPortTrafficRowStatus = _PrvtStrmCtlPortTrafficRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 171, 1, 3, 1, 2),
    _PrvtStrmCtlPortTrafficRowStatus_Type()
)
prvtStrmCtlPortTrafficRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    prvtStrmCtlPortTrafficRowStatus.setStatus("current")
_PrvtStrmCtlPortTrafficThreshold_Type = RateThresholdType
_PrvtStrmCtlPortTrafficThreshold_Object = MibTableColumn
prvtStrmCtlPortTrafficThreshold = _PrvtStrmCtlPortTrafficThreshold_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 171, 1, 3, 1, 3),
    _PrvtStrmCtlPortTrafficThreshold_Type()
)
prvtStrmCtlPortTrafficThreshold.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    prvtStrmCtlPortTrafficThreshold.setStatus("current")
if mibBuilder.loadTexts:
    prvtStrmCtlPortTrafficThreshold.setUnits("packets-per-second")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "PRVT-STORM-CTL-MIB",
    **{"RateThresholdType": RateThresholdType,
       "prvtStormCtlMIB": prvtStormCtlMIB,
       "prvtStormCtlMIBObjects": prvtStormCtlMIBObjects,
       "prvtStrmCtlPortTable": prvtStrmCtlPortTable,
       "prvtStrmCtlPortEntry": prvtStrmCtlPortEntry,
       "prvtStrmCtlPortRowStatus": prvtStrmCtlPortRowStatus,
       "prvtStrmCtlPortShutdown": prvtStrmCtlPortShutdown,
       "prvtStrmCtlPortTrafficTable": prvtStrmCtlPortTrafficTable,
       "prvtStrmCtlPortTrafficEntry": prvtStrmCtlPortTrafficEntry,
       "prvtStrmCtlPortTrafficType": prvtStrmCtlPortTrafficType,
       "prvtStrmCtlPortTrafficRowStatus": prvtStrmCtlPortTrafficRowStatus,
       "prvtStrmCtlPortTrafficThreshold": prvtStrmCtlPortTrafficThreshold}
)
