# SNMP MIB module (PRVT-PROTO-PRIORITY-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\telco-systems\binox\PRVT-PROTO-PRIORITY-MIB

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

prvtProtoPriorityMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 182)
)
if mibBuilder.loadTexts:
    prvtProtoPriorityMIB.setRevisions(
        ("2014-02-03 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_PrvtProtoPriorityMIBObjects_ObjectIdentity = ObjectIdentity
prvtProtoPriorityMIBObjects = _PrvtProtoPriorityMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 182, 1)
)
_DscpRemarkingTable_Object = MibTable
dscpRemarkingTable = _DscpRemarkingTable_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 182, 1, 1)
)
if mibBuilder.loadTexts:
    dscpRemarkingTable.setStatus("current")
_DscpRemarkingEntry_Object = MibTableRow
dscpRemarkingEntry = _DscpRemarkingEntry_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 182, 1, 1, 1)
)
dscpRemarkingEntry.setIndexNames(
    (0, "PRVT-PROTO-PRIORITY-MIB", "dscpRemarkingValue"),
)
if mibBuilder.loadTexts:
    dscpRemarkingEntry.setStatus("current")


class _DscpRemarkingValue_Type(Unsigned32):
    """Custom type dscpRemarkingValue based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_DscpRemarkingValue_Type.__name__ = "Unsigned32"
_DscpRemarkingValue_Object = MibTableColumn
dscpRemarkingValue = _DscpRemarkingValue_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 182, 1, 1, 1, 1),
    _DscpRemarkingValue_Type()
)
dscpRemarkingValue.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dscpRemarkingValue.setStatus("current")
_DscpRemarkingRowStatus_Type = RowStatus
_DscpRemarkingRowStatus_Object = MibTableColumn
dscpRemarkingRowStatus = _DscpRemarkingRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 182, 1, 1, 1, 2),
    _DscpRemarkingRowStatus_Type()
)
dscpRemarkingRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dscpRemarkingRowStatus.setStatus("current")


class _DscpRemarkingFc_Type(Integer32):
    """Custom type dscpRemarkingFc based on Integer32"""
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
        *(("be", 1),
          ("l2", 2),
          ("af", 3),
          ("l1", 4),
          ("h2", 5),
          ("ef", 6),
          ("h1", 7),
          ("nc", 8))
    )


_DscpRemarkingFc_Type.__name__ = "Integer32"
_DscpRemarkingFc_Object = MibTableColumn
dscpRemarkingFc = _DscpRemarkingFc_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 182, 1, 1, 1, 3),
    _DscpRemarkingFc_Type()
)
dscpRemarkingFc.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dscpRemarkingFc.setStatus("current")


class _PrvtArpPriorityMappingToFc_Type(Integer32):
    """Custom type prvtArpPriorityMappingToFc based on Integer32"""
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
        *(("be", 1),
          ("l2", 2),
          ("af", 3),
          ("l1", 4),
          ("h2", 5),
          ("ef", 6),
          ("h1", 7),
          ("nc", 8))
    )


_PrvtArpPriorityMappingToFc_Type.__name__ = "Integer32"
_PrvtArpPriorityMappingToFc_Object = MibScalar
prvtArpPriorityMappingToFc = _PrvtArpPriorityMappingToFc_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 182, 1, 2),
    _PrvtArpPriorityMappingToFc_Type()
)
prvtArpPriorityMappingToFc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prvtArpPriorityMappingToFc.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "PRVT-PROTO-PRIORITY-MIB",
    **{"prvtProtoPriorityMIB": prvtProtoPriorityMIB,
       "prvtProtoPriorityMIBObjects": prvtProtoPriorityMIBObjects,
       "dscpRemarkingTable": dscpRemarkingTable,
       "dscpRemarkingEntry": dscpRemarkingEntry,
       "dscpRemarkingValue": dscpRemarkingValue,
       "dscpRemarkingRowStatus": dscpRemarkingRowStatus,
       "dscpRemarkingFc": dscpRemarkingFc,
       "prvtArpPriorityMappingToFc": prvtArpPriorityMappingToFc}
)
