# SNMP MIB module (AX-MLD-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\alaxala\AX-MLD-MIB

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

(axMib,) = mibBuilder.importSymbols(
    "AX-SMI-MIB",
    "axMib")

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


# MODULE-IDENTITY

axMld = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 202)
)
if mibBuilder.loadTexts:
    axMld.setRevisions(
        ("2014-11-17 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AxMldObjects_ObjectIdentity = ObjectIdentity
axMldObjects = _AxMldObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 202, 1)
)
_AxMldBandPhys_ObjectIdentity = ObjectIdentity
axMldBandPhys = _AxMldBandPhys_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 202, 1, 1)
)
_AxMldBandPhysTable_Object = MibTable
axMldBandPhysTable = _AxMldBandPhysTable_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 202, 1, 1, 1)
)
if mibBuilder.loadTexts:
    axMldBandPhysTable.setStatus("current")
_AxMldBandPhysEntry_Object = MibTableRow
axMldBandPhysEntry = _AxMldBandPhysEntry_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 202, 1, 1, 1, 1)
)
axMldBandPhysEntry.setIndexNames(
    (0, "AX-MLD-MIB", "axMldBandPhysIfIndex"),
)
if mibBuilder.loadTexts:
    axMldBandPhysEntry.setStatus("current")
_AxMldBandPhysIfIndex_Type = Integer32
_AxMldBandPhysIfIndex_Object = MibTableColumn
axMldBandPhysIfIndex = _AxMldBandPhysIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 202, 1, 1, 1, 1, 1),
    _AxMldBandPhysIfIndex_Type()
)
axMldBandPhysIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    axMldBandPhysIfIndex.setStatus("current")
_AxMldBandPhysMaxRate_Type = Unsigned32
_AxMldBandPhysMaxRate_Object = MibTableColumn
axMldBandPhysMaxRate = _AxMldBandPhysMaxRate_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 202, 1, 1, 1, 1, 2),
    _AxMldBandPhysMaxRate_Type()
)
axMldBandPhysMaxRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axMldBandPhysMaxRate.setStatus("current")
_AxMldBandPhysCurrentRate_Type = Unsigned32
_AxMldBandPhysCurrentRate_Object = MibTableColumn
axMldBandPhysCurrentRate = _AxMldBandPhysCurrentRate_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 202, 1, 1, 1, 1, 3),
    _AxMldBandPhysCurrentRate_Type()
)
axMldBandPhysCurrentRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axMldBandPhysCurrentRate.setStatus("current")
_AxMldBandPhysAlarmRaise_Type = Integer32
_AxMldBandPhysAlarmRaise_Object = MibTableColumn
axMldBandPhysAlarmRaise = _AxMldBandPhysAlarmRaise_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 202, 1, 1, 1, 1, 4),
    _AxMldBandPhysAlarmRaise_Type()
)
axMldBandPhysAlarmRaise.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axMldBandPhysAlarmRaise.setStatus("current")
_AxMldBandPhysAlarmClear_Type = Integer32
_AxMldBandPhysAlarmClear_Object = MibTableColumn
axMldBandPhysAlarmClear = _AxMldBandPhysAlarmClear_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 202, 1, 1, 1, 1, 5),
    _AxMldBandPhysAlarmClear_Type()
)
axMldBandPhysAlarmClear.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axMldBandPhysAlarmClear.setStatus("current")
_AxMldBandPhysAlarmStatus_Type = Integer32
_AxMldBandPhysAlarmStatus_Object = MibTableColumn
axMldBandPhysAlarmStatus = _AxMldBandPhysAlarmStatus_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 202, 1, 1, 1, 1, 6),
    _AxMldBandPhysAlarmStatus_Type()
)
axMldBandPhysAlarmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axMldBandPhysAlarmStatus.setStatus("current")
_AxMldConformance_ObjectIdentity = ObjectIdentity
axMldConformance = _AxMldConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 202, 1000)
)
_AxMldCompliances_ObjectIdentity = ObjectIdentity
axMldCompliances = _AxMldCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 202, 1000, 1)
)
_AxMldGroups_ObjectIdentity = ObjectIdentity
axMldGroups = _AxMldGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 202, 1000, 2)
)

# Managed Objects groups

axMldGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 202, 1000, 2, 1)
)
axMldGroup.setObjects(
      *(("AX-MLD-MIB", "axMldBandPhysMaxRate"),
        ("AX-MLD-MIB", "axMldBandPhysCurrentRate"),
        ("AX-MLD-MIB", "axMldBandPhysAlarmRaise"),
        ("AX-MLD-MIB", "axMldBandPhysAlarmClear"),
        ("AX-MLD-MIB", "axMldBandPhysAlarmStatus"))
)
if mibBuilder.loadTexts:
    axMldGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

axMldCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 202, 1000, 1, 1)
)
axMldCompliance.setObjects(
    ("AX-MLD-MIB", "axMldGroup")
)
if mibBuilder.loadTexts:
    axMldCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "AX-MLD-MIB",
    **{"axMld": axMld,
       "axMldObjects": axMldObjects,
       "axMldBandPhys": axMldBandPhys,
       "axMldBandPhysTable": axMldBandPhysTable,
       "axMldBandPhysEntry": axMldBandPhysEntry,
       "axMldBandPhysIfIndex": axMldBandPhysIfIndex,
       "axMldBandPhysMaxRate": axMldBandPhysMaxRate,
       "axMldBandPhysCurrentRate": axMldBandPhysCurrentRate,
       "axMldBandPhysAlarmRaise": axMldBandPhysAlarmRaise,
       "axMldBandPhysAlarmClear": axMldBandPhysAlarmClear,
       "axMldBandPhysAlarmStatus": axMldBandPhysAlarmStatus,
       "axMldConformance": axMldConformance,
       "axMldCompliances": axMldCompliances,
       "axMldCompliance": axMldCompliance,
       "axMldGroups": axMldGroups,
       "axMldGroup": axMldGroup}
)
