# SNMP MIB module (PRIV-LSL-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\telco-systems\binos\PRIV-LSL-MIB

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
 MacAddress,
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

privLsl = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 113)
)
if mibBuilder.loadTexts:
    privLsl.setRevisions(
        ("2008-03-21 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class PrivLslStates(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )



# MIB Managed Objects in the order of their OIDs

_PrivLslLevel1_ObjectIdentity = ObjectIdentity
privLslLevel1 = _PrivLslLevel1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 113, 1)
)
_PrivLslObjects_ObjectIdentity = ObjectIdentity
privLslObjects = _PrivLslObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 113, 1, 1)
)
_PrivLslGlobalMacAddress_Type = MacAddress
_PrivLslGlobalMacAddress_Object = MibScalar
privLslGlobalMacAddress = _PrivLslGlobalMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 113, 1, 1, 1),
    _PrivLslGlobalMacAddress_Type()
)
privLslGlobalMacAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    privLslGlobalMacAddress.setStatus("current")
_PrivLslManagementTable_Object = MibTable
privLslManagementTable = _PrivLslManagementTable_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 113, 1, 1, 2)
)
if mibBuilder.loadTexts:
    privLslManagementTable.setStatus("current")
_PrivLslManagementEntry_Object = MibTableRow
privLslManagementEntry = _PrivLslManagementEntry_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 113, 1, 1, 2, 1)
)
privLslManagementEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    privLslManagementEntry.setStatus("current")
_PrivLslStatus_Type = PrivLslStates
_PrivLslStatus_Object = MibTableColumn
privLslStatus = _PrivLslStatus_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 113, 1, 1, 2, 1, 1),
    _PrivLslStatus_Type()
)
privLslStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    privLslStatus.setStatus("current")
_PrivIometrixManagementTable_Object = MibTable
privIometrixManagementTable = _PrivIometrixManagementTable_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 113, 1, 1, 3)
)
if mibBuilder.loadTexts:
    privIometrixManagementTable.setStatus("current")
_PrivIometrixManagementEntry_Object = MibTableRow
privIometrixManagementEntry = _PrivIometrixManagementEntry_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 113, 1, 1, 3, 1)
)
privIometrixManagementEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    privIometrixManagementEntry.setStatus("current")
_PrivIometrixStatus_Type = PrivLslStates
_PrivIometrixStatus_Object = MibTableColumn
privIometrixStatus = _PrivIometrixStatus_Object(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 113, 1, 1, 3, 1, 1),
    _PrivIometrixStatus_Type()
)
privIometrixStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    privIometrixStatus.setStatus("current")
_PrivLslNotifications_ObjectIdentity = ObjectIdentity
privLslNotifications = _PrivLslNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 113, 1, 2)
)
_PrivLslConformance_ObjectIdentity = ObjectIdentity
privLslConformance = _PrivLslConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 113, 1, 3)
)
_PrivLslGroups_ObjectIdentity = ObjectIdentity
privLslGroups = _PrivLslGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 113, 1, 3, 1)
)
_PrivLslCompliances_ObjectIdentity = ObjectIdentity
privLslCompliances = _PrivLslCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 113, 1, 3, 2)
)

# Managed Objects groups

privLevel1ObjectsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 113, 1, 3, 1, 1)
)
privLevel1ObjectsGroup.setObjects(
      *(("PRIV-LSL-MIB", "privLslGlobalMacAddress"),
        ("PRIV-LSL-MIB", "privLslStatus"),
        ("PRIV-LSL-MIB", "privIometrixStatus"))
)
if mibBuilder.loadTexts:
    privLevel1ObjectsGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

privLevel1Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 738, 1, 5, 113, 1, 3, 2, 1)
)
privLevel1Compliance.setObjects(
    ("PRIV-LSL-MIB", "privLevel1ObjectsGroup")
)
if mibBuilder.loadTexts:
    privLevel1Compliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "PRIV-LSL-MIB",
    **{"PrivLslStates": PrivLslStates,
       "privLsl": privLsl,
       "privLslLevel1": privLslLevel1,
       "privLslObjects": privLslObjects,
       "privLslGlobalMacAddress": privLslGlobalMacAddress,
       "privLslManagementTable": privLslManagementTable,
       "privLslManagementEntry": privLslManagementEntry,
       "privLslStatus": privLslStatus,
       "privIometrixManagementTable": privIometrixManagementTable,
       "privIometrixManagementEntry": privIometrixManagementEntry,
       "privIometrixStatus": privIometrixStatus,
       "privLslNotifications": privLslNotifications,
       "privLslConformance": privLslConformance,
       "privLslGroups": privLslGroups,
       "privLevel1ObjectsGroup": privLevel1ObjectsGroup,
       "privLslCompliances": privLslCompliances,
       "privLevel1Compliance": privLevel1Compliance}
)
