# SNMP MIB module (AX-MANAGEMENT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\alaxala\AX-MANAGEMENT-MIB

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

axManagementMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 1004)
)
if mibBuilder.loadTexts:
    axManagementMIB.setRevisions(
        ("2014-05-08 00:01",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AxOperationCommand_ObjectIdentity = ObjectIdentity
axOperationCommand = _AxOperationCommand_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 1004, 1)
)
_AxFdbClearMIB_ObjectIdentity = ObjectIdentity
axFdbClearMIB = _AxFdbClearMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 1004, 1, 1)
)


class _AxFdbClearSet_Type(Integer32):
    """Custom type axFdbClearSet based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("initialValue", 1),
          ("processing", 2),
          ("failure", 3),
          ("success", 4))
    )


_AxFdbClearSet_Type.__name__ = "Integer32"
_AxFdbClearSet_Object = MibScalar
axFdbClearSet = _AxFdbClearSet_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 1004, 1, 1, 1),
    _AxFdbClearSet_Type()
)
axFdbClearSet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    axFdbClearSet.setStatus("current")
_AxFdbClearReqTime_Type = TimeTicks
_AxFdbClearReqTime_Object = MibScalar
axFdbClearReqTime = _AxFdbClearReqTime_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 1004, 1, 1, 2),
    _AxFdbClearReqTime_Type()
)
axFdbClearReqTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axFdbClearReqTime.setStatus("current")
_AxFdbClearSuccessTime_Type = TimeTicks
_AxFdbClearSuccessTime_Object = MibScalar
axFdbClearSuccessTime = _AxFdbClearSuccessTime_Object(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 1004, 1, 1, 3),
    _AxFdbClearSuccessTime_Type()
)
axFdbClearSuccessTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axFdbClearSuccessTime.setStatus("current")
_AxManagementMIBConformance_ObjectIdentity = ObjectIdentity
axManagementMIBConformance = _AxManagementMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 1004, 1000)
)
_AxManagementMIBCompliances_ObjectIdentity = ObjectIdentity
axManagementMIBCompliances = _AxManagementMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 1004, 1000, 1)
)
_AxManagementMIBGroups_ObjectIdentity = ObjectIdentity
axManagementMIBGroups = _AxManagementMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 1004, 1000, 2)
)

# Managed Objects groups

axManagementMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 1004, 1000, 2, 1)
)
axManagementMIBGroup.setObjects(
      *(("AX-MANAGEMENT-MIB", "axFdbClearSet"),
        ("AX-MANAGEMENT-MIB", "axFdbClearReqTime"),
        ("AX-MANAGEMENT-MIB", "axFdbClearSuccessTime"))
)
if mibBuilder.loadTexts:
    axManagementMIBGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

axManagementMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 21839, 2, 4, 1, 1004, 1000, 1, 1)
)
axManagementMIBCompliance.setObjects(
    ("AX-MANAGEMENT-MIB", "axManagementMIBGroup")
)
if mibBuilder.loadTexts:
    axManagementMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "AX-MANAGEMENT-MIB",
    **{"axManagementMIB": axManagementMIB,
       "axOperationCommand": axOperationCommand,
       "axFdbClearMIB": axFdbClearMIB,
       "axFdbClearSet": axFdbClearSet,
       "axFdbClearReqTime": axFdbClearReqTime,
       "axFdbClearSuccessTime": axFdbClearSuccessTime,
       "axManagementMIBConformance": axManagementMIBConformance,
       "axManagementMIBCompliances": axManagementMIBCompliances,
       "axManagementMIBCompliance": axManagementMIBCompliance,
       "axManagementMIBGroups": axManagementMIBGroups,
       "axManagementMIBGroup": axManagementMIBGroup}
)
