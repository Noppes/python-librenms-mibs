# SNMP MIB module (AX-BOOTMANAGEMENT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\alaxala\AX-BOOTMANAGEMENT-MIB

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

axBootManagement = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 51)
)
if mibBuilder.loadTexts:
    axBootManagement.setRevisions(
        ("2013-03-06 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs



class _AxBootReason_Type(Integer32):
    """Custom type axBootReason based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              5,
              6,
              7,
              8)
        )
    )
    namedValues = NamedValues(
        *(("powerOn", 1),
          ("operationRestart", 2),
          ("fatalErrorRestart", 3),
          ("resetSwitchRestart", 5),
          ("achSwitchRestart", 6),
          ("defaultRestart", 7),
          ("autoRestart", 8))
    )


_AxBootReason_Type.__name__ = "Integer32"
_AxBootReason_Object = MibScalar
axBootReason = _AxBootReason_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 51, 1),
    _AxBootReason_Type()
)
axBootReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axBootReason.setStatus("current")
_AxBootManagementConformance_ObjectIdentity = ObjectIdentity
axBootManagementConformance = _AxBootManagementConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 51, 1000)
)
_AxBootManagementCompliances_ObjectIdentity = ObjectIdentity
axBootManagementCompliances = _AxBootManagementCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 51, 1000, 1)
)
_AxBootManagementGroups_ObjectIdentity = ObjectIdentity
axBootManagementGroups = _AxBootManagementGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 51, 1000, 2)
)

# Managed Objects groups

axBootManagementGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 51, 1000, 2, 1)
)
axBootManagementGroup.setObjects(
    ("AX-BOOTMANAGEMENT-MIB", "axBootReason")
)
if mibBuilder.loadTexts:
    axBootManagementGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

axBootManagementCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 51, 1000, 1, 1)
)
axBootManagementCompliance.setObjects(
    ("AX-BOOTMANAGEMENT-MIB", "axBootManagementGroup")
)
if mibBuilder.loadTexts:
    axBootManagementCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "AX-BOOTMANAGEMENT-MIB",
    **{"axBootManagement": axBootManagement,
       "axBootReason": axBootReason,
       "axBootManagementConformance": axBootManagementConformance,
       "axBootManagementCompliances": axBootManagementCompliances,
       "axBootManagementCompliance": axBootManagementCompliance,
       "axBootManagementGroups": axBootManagementGroups,
       "axBootManagementGroup": axBootManagementGroup}
)
